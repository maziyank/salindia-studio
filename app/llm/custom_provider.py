"""Generic OpenAI-compatible provider.

Any endpoint that speaks the OpenAI Chat Completions API (Groq, OpenRouter,
Together, vLLM, Ollama, LM Studio, DeepSeek, a self-hosted gateway, etc.) can be
used by pointing CUSTOM_BASE_URL / CUSTOM_API_KEY / LLM_MODEL_CUSTOM at it.
Message/tool normalization is identical to OpenAI, so we reuse the parent.
"""
from __future__ import annotations

from app.config import get_settings
from app.llm.openai_provider import OpenAIProvider


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

    def available(self) -> bool:
        # A base URL and model are required; the API key is optional because
        # local/self-hosted endpoints often run without auth.
        return bool(self.base_url and self.model)
