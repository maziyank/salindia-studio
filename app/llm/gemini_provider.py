"""Google Gemini provider (via the google-genai SDK). Gemini exposes function
declarations and returns function_call parts; we normalize those to our
LLMContent shape.
"""
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from google import genai
from google.genai import types as gtypes

from app.config import get_settings
from app.llm.base import LLMContent, LLMMessage, LLMProvider, LLMResponse


class GeminiProvider(LLMProvider):
    name = "gemini"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.gemini_api_key
        self.model = s.llm_model_gemini
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        self._client: Optional[genai.Client] = None

    def _ensure_client(self) -> genai.Client:
        if self._client is None:
            self._client = genai.Client(api_key=self.api_key)
        return self._client

    def available(self) -> bool:
        return bool(self.api_key)

    def _to_contents(self, messages: List[LLMMessage]) -> List[Dict[str, Any]]:
        """Convert to Gemini `contents` shape (role + parts)."""
        contents: List[Dict[str, Any]] = []
        for m in messages:
            if m.role == "tool":
                # Gemini: function response as a part under role "user"
                args = m.content if isinstance(m.content, dict) else {"result": str(m.content)}
                contents.append({
                    "role": "user",
                    "parts": [gtypes.Part(function_response=gtypes.FunctionResponse(name=m.name or "tool", response=args))],
                })
                continue
            role = "model" if m.role == "assistant" else "user"
            parts: List[Any] = []
            if isinstance(m.content, str):
                parts.append(gtypes.Part(text=m.content))
            else:
                for c in m.content:
                    if c.type == "text" and c.text:
                        parts.append(gtypes.Part(text=c.text))
                    elif c.type == "tool_use":
                        parts.append(gtypes.Part(function_call=gtypes.FunctionCall(
                            id=c.tool_call_id, name=c.tool_name, args=c.tool_args,
                        )))
            if parts:
                contents.append({"role": role, "parts": parts})
        return contents

    def _normalize_tools(self, tools: Optional[List[Dict[str, Any]]]) -> Optional[List[gtypes.Tool]]:
        if not tools:
            return None
        decls = []
        for t in tools:
            decls.append(gtypes.FunctionDeclaration(
                name=t["name"],
                description=t.get("description", ""),
                parameters=t.get("parameters", {"type": "object", "properties": {}}),
            ))
        return [gtypes.Tool(function_declarations=decls)]

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
        cfg = gtypes.GenerateContentConfig(
            temperature=temperature if temperature is not None else self.temperature,
            max_output_tokens=max_tokens or self.max_tokens,
            tools=self._normalize_tools(tools) or None,
            system_instruction=system if system else None,
        )
        contents = self._to_contents(messages)
        resp = await client.aio.models.generate_content(
            model=self.model,
            contents=contents,
            config=cfg,
        )
        content: List[LLMContent] = []
        # Each candidate has parts; iterate all parts
        for cand in (resp.candidates or []):
            for part in (cand.content.parts or []):
                if part.text:
                    content.append(LLMContent(type="text", text=part.text))
                elif part.function_call:
                    args = dict(part.function_call.args or {})
                    content.append(LLMContent(
                        type="tool_use",
                        tool_call_id=part.function_call.id or part.function_call.name,
                        tool_name=part.function_call.name,
                        tool_args=args,
                    ))
        stop_reason = "tool_use" if any(c.type == "tool_use" for c in content) else "stop"
        # Usage may be None for some flows
        usage_meta = getattr(resp, "usage_metadata", None)
        return LLMResponse(
            content=content,
            stop_reason=stop_reason,
            usage_input_tokens=getattr(usage_meta, "prompt_token_count", 0) or 0,
            usage_output_tokens=getattr(usage_meta, "candidates_token_count", 0) or 0,
            raw=None,
        )
