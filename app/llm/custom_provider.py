"""Generic OpenAI-compatible provider.

Any endpoint that speaks the OpenAI Chat Completions API (Groq, OpenRouter,
Together, vLLM, Ollama, LM Studio, DeepSeek, a self-hosted gateway, etc.) can be
used by pointing CUSTOM_BASE_URL / CUSTOM_API_KEY / LLM_MODEL_CUSTOM at it.
Message/tool normalization is identical to OpenAI, so we reuse the parent.
"""
from __future__ import annotations

import json

import httpx
from openai import AsyncOpenAI

from app.config import get_settings
from app.llm.openai_provider import OpenAIProvider


def _strip_trailing_junk(body: bytes) -> bytes:
    """Return `body` unchanged when it is valid JSON. Otherwise decode the first
    JSON value and drop whatever follows it.

    Some OpenAI-compatible gateways append an SSE terminator (e.g. `data: [DONE]`)
    to non-streaming JSON responses. The OpenAI SDK parses the raw body with
    `json.loads`, which then fails with "Extra data".
    """
    if not body:
        return body
    try:
        json.loads(body)
        return body
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return body
    stripped = text.lstrip()
    if not stripped or stripped[0] not in "{[":
        return body
    try:
        value, _end = json.JSONDecoder().raw_decode(stripped)
    except json.JSONDecodeError:
        return body
    return json.dumps(value, ensure_ascii=False).encode("utf-8")


class _JsonBodySanitizingTransport(httpx.AsyncHTTPTransport):
    """Async HTTP transport that repairs malformed JSON bodies before the
    OpenAI SDK parses them. Non-JSON (e.g. SSE) responses pass through untouched."""

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await super().handle_async_request(request)
        if "application/json" not in response.headers.get("content-type", ""):
            return response
        try:
            await response.aread()
        except Exception:  # noqa: BLE001 - leave the response as-is on read errors
            return response
        cleaned = _strip_trailing_junk(response.content)
        if cleaned is not response.content:
            response._content = cleaned  # type: ignore[attr-defined]
            response._stream = httpx.ByteStream(cleaned)  # type: ignore[attr-defined]
            response.headers["content-length"] = str(len(cleaned))
        return response


class CustomOpenAICompatibleProvider(OpenAIProvider):
    name = "custom"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.custom_api_key
        self.base_url = s.custom_base_url or None
        self.model = s.llm_model_custom
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        self.use_max_completion_tokens = False
        self._client = None

    def _ensure_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
                http_client=httpx.AsyncClient(
                    transport=_JsonBodySanitizingTransport(),
                    timeout=httpx.Timeout(600.0, connect=10.0),
                ),
            )
        return self._client

    def available(self) -> bool:
        # A base URL and model are required; the API key is optional because
        # local/self-hosted endpoints often run without auth.
        return bool(self.base_url and self.model)
