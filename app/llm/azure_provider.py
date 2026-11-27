"""Azure OpenAI provider.

Azure OpenAI exposes the same Chat Completions API as OpenAI proper, so this
provider subclasses OpenAIProvider and only swaps the client construction.
The differences are authentication (api_key + azure_endpoint + api_version) and that
the `model` parameter passed to chat.completions.create is the deployment name.

Message/tool normalization is identical to the OpenAI provider, so we reuse
`_to_openai_messages`, `_normalize_tools`, and `chat` from the parent.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

import httpx

from openai import AsyncAzureOpenAI

from app.config import get_settings
from app.llm.base import LLMContent, LLMMessage, LLMResponse
from app.llm.openai_provider import OpenAIProvider


class AzureOpenAIProvider(OpenAIProvider):
    name = "azure"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.azure_api_key
        self.azure_endpoint = s.azure_endpoint
        self.api_version = s.azure_api_version
        self.responses_api_version = s.azure_responses_api_version
        # In Azure OpenAI the model name is the deployment name.
        self.model = s.llm_model_azure
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        # gpt-5.x / o-series Azure deployments require `max_completion_tokens`.
        self.use_max_completion_tokens = False
        self._client: Optional[AsyncAzureOpenAI] = None

    def _ensure_client(self) -> AsyncAzureOpenAI:
        if self._client is None:
            self._client = AsyncAzureOpenAI(
                azure_endpoint=self.azure_endpoint,
                api_key=self.api_key,
                api_version=self.api_version,
                azure_deployment=self.model,
            )
        return self._client

    def available(self) -> bool:
        return bool(self.api_key and self.azure_endpoint and self.model)

    async def chat(
        self,
        messages: List[LLMMessage],
        *,
        system: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> LLMResponse:
        """Azure gpt-6 deployments reject function tools over Chat Completions:
        tools require `reasoning_effort='none'`, but the model does not accept
        that value. Route tool-calling turns through the Responses API instead;
        plain text turns keep using Chat Completions."""
        if not tools:
            return await super().chat(
                messages, system=system, tools=tools,
                temperature=temperature, max_tokens=max_tokens,
            )
        resp = await self._chat_via_responses(
            messages, system=system, tools=tools, max_tokens=max_tokens
        )
        if resp is not None:
            return resp
        # Responses endpoint unavailable (older endpoint/api-version): fall
        # back to the Chat Completions path.
        return await super().chat(
            messages, system=system, tools=tools,
            temperature=temperature, max_tokens=max_tokens,
        )

    def _to_responses_input(
        self, messages: List[LLMMessage], system: Optional[str]
    ) -> List[Dict[str, Any]]:
        items: List[Dict[str, Any]] = []
        if system:
            items.append({"role": "system", "content": system})
        for m in messages:
            if m.role == "tool":
                output = m.content if isinstance(m.content, str) else json.dumps(
                    m.content, ensure_ascii=False
                )
                items.append({
                    "type": "function_call_output",
                    "call_id": m.tool_call_id,
                    "output": output,
                })
            elif m.role == "assistant":
                if isinstance(m.content, str):
                    if m.content:
                        items.append({
                            "role": "assistant",
                            "content": [{"type": "output_text", "text": m.content}],
                        })
                    continue
                text_parts: List[str] = []
                call_items: List[Dict[str, Any]] = []
                for c in m.content:
                    if c.type == "text" and c.text:
                        text_parts.append(c.text)
                    elif c.type == "tool_use":
                        call_items.append({
                            "type": "function_call",
                            "name": c.tool_name,
                            "arguments": json.dumps(c.tool_args or {}, ensure_ascii=False),
                            "call_id": c.tool_call_id,
                        })
                if text_parts:
                    items.append({
                        "role": "assistant",
                        "content": [{"type": "output_text", "text": "".join(text_parts)}],
                    })
                items.extend(call_items)
            else:  # user
                if isinstance(m.content, str):
                    items.append({"role": "user", "content": m.content})
                else:
                    text = "".join(c.text or "" for c in m.content if c.type == "text")
                    items.append({"role": "user", "content": text})
        return items

    @staticmethod
    def _to_responses_tools(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        for t in tools:
            out.append({
                "type": "function",
                "name": t.get("name", ""),
                "description": t.get("description", ""),
                "parameters": t.get("parameters") or {"type": "object", "properties": {}},
            })
        return out

    async def _chat_via_responses(
        self,
        messages: List[LLMMessage],
        *,
        system: Optional[str],
        tools: List[Dict[str, Any]],
        max_tokens: Optional[int],
    ) -> Optional[LLMResponse]:
        payload: Dict[str, Any] = {
            "model": self.model,
            "input": self._to_responses_input(messages, system),
            "tools": self._to_responses_tools(tools),
        }
        if max_tokens:
            payload["max_output_tokens"] = max_tokens
        url = f"{self.azure_endpoint.rstrip('/')}/openai/responses"
        headers = {"api-key": self.api_key, "content-type": "application/json"}
        params = {"api-version": self.responses_api_version}
        async with httpx.AsyncClient(timeout=httpx.Timeout(600.0, connect=10.0)) as client:
            r = await client.post(url, params=params, headers=headers, json=payload)
        if r.status_code in (404, 405):
            return None
        if r.status_code >= 400:
            raise RuntimeError(
                f"Azure Responses API error {r.status_code}: {r.text[:500]}"
            )
        return self._parse_responses(r.json())

    @staticmethod
    def _parse_responses(data: Dict[str, Any]) -> LLMResponse:
        content: List[LLMContent] = []
        for item in data.get("output") or []:
            typ = item.get("type")
            if typ == "message":
                for part in item.get("content") or []:
                    if part.get("type") in ("output_text", "text") and part.get("text"):
                        content.append(LLMContent(type="text", text=part["text"]))
            elif typ == "function_call":
                raw_args = item.get("arguments") or "{}"
                try:
                    args = json.loads(raw_args)
                except (json.JSONDecodeError, TypeError):
                    args = {"_raw": raw_args}
                content.append(LLMContent(
                    type="tool_use",
                    tool_call_id=item.get("call_id") or item.get("id"),
                    tool_name=item.get("name"),
                    tool_args=args,
                ))
        has_tools = any(c.type == "tool_use" for c in content)
        stop_reason = "tool_use" if has_tools else (
            "length" if data.get("status") == "incomplete" else "stop"
        )
        usage = data.get("usage") or {}
        return LLMResponse(
            content=content,
            stop_reason=stop_reason,
            usage_input_tokens=usage.get("input_tokens", 0) or 0,
            usage_output_tokens=usage.get("output_tokens", 0) or 0,
            raw=data,
        )
