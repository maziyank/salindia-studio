"""OpenAI-compatible provider. Used for both OpenAI proper and Kimi (Moonshot),
which exposes an OpenAI-compatible endpoint.

The OpenAI Chat Completions API surfaces tool calls as a separate
`tool_calls` array on the assistant message; we normalize that into the
LLMContent list (one "tool_use" block per call) so the agent loop sees a
uniform shape across providers.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI, BadRequestError

from app.config import get_settings
from app.llm.base import LLMContent, LLMMessage, LLMProvider, LLMResponse


class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self, *, kimi: bool = False) -> None:
        s = get_settings()
        if kimi:
            self.api_key = s.kimi_api_key
            self.base_url = s.kimi_base_url or "https://api.moonshot.cn/v1"
            self.model = s.llm_model_kimi
            self.name = "kimi"
        else:
            self.api_key = s.openai_api_key
            self.base_url = s.openai_base_url or None
            self.model = s.llm_model_openai
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        # Newer OpenAI models (gpt-5/o-series, some Azure deployments) reject the
        # legacy `max_tokens` param and require `max_completion_tokens`.
        self.use_max_completion_tokens = False
        self._client: Optional[AsyncOpenAI] = None

    def _ensure_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        return self._client

    def available(self) -> bool:
        return bool(self.api_key)

    def _to_openai_messages(self, messages: List[LLMMessage], system: Optional[str]) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        if system:
            out.append({"role": "system", "content": system})
        for m in messages:
            if m.role == "tool":
                out.append({
                    "role": "tool",
                    "tool_call_id": m.tool_call_id,
                    "content": m.content if isinstance(m.content, str) else json.dumps(m.content),
                })
            elif m.role == "assistant":
                # Reconstruct assistant message: text + tool_calls
                if isinstance(m.content, str):
                    out.append({"role": "assistant", "content": m.content})
                else:
                    text_parts: List[str] = []
                    tool_calls: List[Dict[str, Any]] = []
                    for c in m.content:
                        if c.type == "text" and c.text:
                            text_parts.append(c.text)
                        elif c.type == "tool_use":
                            tool_calls.append({
                                "id": c.tool_call_id,
                                "type": "function",
                                "function": {"name": c.tool_name, "arguments": json.dumps(c.tool_args)},
                            })
                    msg: Dict[str, Any] = {"role": "assistant"}
                    if text_parts:
                        msg["content"] = "".join(text_parts)
                    if tool_calls:
                        msg["tool_calls"] = tool_calls
                    out.append(msg)
            else:  # user
                if isinstance(m.content, str):
                    out.append({"role": m.role, "content": m.content})
                else:
                    # Concatenate text blocks; we don't support vision here.
                    text = "".join(c.text or "" for c in m.content if c.type == "text")
                    out.append({"role": m.role, "content": text})
        return out

    def _normalize_tools(self, tools: Optional[List[Dict[str, Any]]]) -> Optional[List[Dict[str, Any]]]:
        if not tools:
            return None
        # Tools are passed in the abstract schema:
        #   {"name": str, "description": str, "parameters": <json schema>}
        return [{"type": "function", "function": t} for t in tools]

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
        oa_messages = self._to_openai_messages(messages, system)
        oa_tools = self._normalize_tools(tools)
        kwargs: Dict[str, Any] = {
            "model": self.model,
            "messages": oa_messages,
            "temperature": temperature if temperature is not None else self.temperature,
        }
        token_param = "max_completion_tokens" if self.use_max_completion_tokens else "max_tokens"
        kwargs[token_param] = max_tokens or self.max_tokens
        if oa_tools:
            kwargs["tools"] = oa_tools
        # Some models (gpt-5/o-series) reject `max_tokens` (want `max_completion_tokens`)
        # and/or a custom `temperature` (only the default is supported). Adapt as we
        # learn about the model, then retry (up to 3 corrections per call).
        for _ in range(4):
            try:
                resp = await client.chat.completions.create(**kwargs)
                break
            except BadRequestError as e:
                param = getattr(e, "param", None)
                message = str(e)
                if (
                    param in ("max_tokens", "max_completion_tokens")
                    or ("max_tokens" in message and "max_completion_tokens" in message)
                ) and "max_tokens" in kwargs:
                    kwargs.pop("max_tokens")
                    kwargs["max_completion_tokens"] = max_tokens or self.max_tokens
                    self.use_max_completion_tokens = True
                elif (param == "temperature" or "temperature" in message) and "temperature" in kwargs:
                    kwargs.pop("temperature")
                elif (param == "reasoning_effort" or "reasoning_effort" in message) and oa_tools:
                    # gpt-6 family: function tools over /v1/chat/completions are only
                    # allowed when reasoning_effort is 'none'. Disable reasoning for
                    # tool-calling turns and retry.
                    kwargs["reasoning_effort"] = "none"
                else:
                    raise
        choice = resp.choices[0]
        msg = choice.message
        content: List[LLMContent] = []
        if msg.content:
            content.append(LLMContent(type="text", text=msg.content))
        for tc in msg.tool_calls or []:
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {"_raw": tc.function.arguments}
            content.append(LLMContent(
                type="tool_use",
                tool_call_id=tc.id,
                tool_name=tc.function.name,
                tool_args=args,
            ))
        stop_reason = "tool_use" if msg.tool_calls else ("length" if choice.finish_reason == "length" else "stop")
        usage = resp.usage
        return LLMResponse(
            content=content,
            stop_reason=stop_reason,
            usage_input_tokens=getattr(usage, "prompt_tokens", 0) if usage else 0,
            usage_output_tokens=getattr(usage, "completion_tokens", 0) if usage else 0,
            raw=resp.model_dump() if hasattr(resp, "model_dump") else None,
        )
