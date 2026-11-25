"""Anthropic (Claude) provider. Claude natively uses content blocks for both
assistant text and tool_use, so the normalization is mostly a thin wrapper.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from anthropic import AsyncAnthropic

from app.config import get_settings
from app.llm.base import LLMContent, LLMMessage, LLMProvider, LLMResponse


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.anthropic_api_key
        self.model = s.llm_model_anthropic
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        self._client: Optional[AsyncAnthropic] = None

    def _ensure_client(self) -> AsyncAnthropic:
        if self._client is None:
            self._client = AsyncAnthropic(api_key=self.api_key)
        return self._client

    def available(self) -> bool:
        return bool(self.api_key)

    def _to_anthropic_messages(self, messages: List[LLMMessage]) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        for m in messages:
            if m.role == "tool":
                # Anthropic uses role="user" with tool_result content blocks
                out.append({
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": m.tool_call_id,
                        "content": m.content if isinstance(m.content, str) else json.dumps(m.content),
                    }],
                })
            elif m.role == "assistant":
                if isinstance(m.content, str):
                    out.append({"role": "assistant", "content": [{"type": "text", "text": m.content}]})
                else:
                    blocks: List[Dict[str, Any]] = []
                    for c in m.content:
                        if c.type == "text" and c.text:
                            blocks.append({"type": "text", "text": c.text})
                        elif c.type == "tool_use":
                            blocks.append({
                                "type": "tool_use",
                                "id": c.tool_call_id,
                                "name": c.tool_name,
                                "input": c.tool_args,
                            })
                    out.append({"role": "assistant", "content": blocks})
            else:  # user
                if isinstance(m.content, str):
                    out.append({"role": "user", "content": [{"type": "text", "text": m.content}]})
                else:
                    blocks = [{"type": "text", "text": c.text or ""} for c in m.content if c.type == "text"]
                    out.append({"role": "user", "content": blocks})
        return out

    def _normalize_tools(self, tools: Optional[List[Dict[str, Any]]]) -> Optional[List[Dict[str, Any]]]:
        if not tools:
            return None
        return [{
            "name": t["name"],
            "description": t.get("description", ""),
            "input_schema": t.get("parameters", {"type": "object", "properties": {}}),
        } for t in tools]

    async def chat(
        self,
        messages: List[LLMMessage],
        *,
        system: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> LLMResponse:
        client = self._ensure_client()
        kwargs: Dict[str, Any] = {
            "model": self.model,
            "messages": self._to_anthropic_messages(messages),
            "temperature": temperature if temperature is not None else self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
        }
        if system:
            kwargs["system"] = system
        norm_tools = self._normalize_tools(tools)
        if norm_tools:
            kwargs["tools"] = norm_tools
        resp = await client.messages.create(**kwargs)
        content: List[LLMContent] = []
        for block in resp.content:
            if block.type == "text":
                content.append(LLMContent(type="text", text=block.text))
            elif block.type == "tool_use":
                content.append(LLMContent(
                    type="tool_use",
                    tool_call_id=block.id,
                    tool_name=block.name,
                    tool_args=dict(block.input),
                ))
        return LLMResponse(
            content=content,
            stop_reason=resp.stop_reason or "stop",
            usage_input_tokens=getattr(resp.usage, "input_tokens", 0),
            usage_output_tokens=getattr(resp.usage, "output_tokens", 0),
            raw=resp.model_dump() if hasattr(resp, "model_dump") else None,
        )
