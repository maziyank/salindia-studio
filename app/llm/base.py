"""Abstract LLM provider + normalized types.

Design rationale: every provider SDK has its own JSON shape for tool calls
and content blocks. The agent loop must NOT know which provider is active, so
we normalize to these types here. Adding a new provider is a matter of
implementing `LLMProvider.chat` and translating to/from these types.
"""
from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class LLMContent:
    """One block of assistant content. Either text or a tool call, not both.
    Anthropic-style: a single assistant turn may contain multiple blocks.
    """
    type: str  # "text" | "tool_use"
    text: Optional[str] = None
    # Only set when type == "tool_use"
    tool_call_id: Optional[str] = None
    tool_name: Optional[str] = None
    tool_args: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LLMToolCall:
    """Tool call request from the model. Used by OpenAI-style providers
    that surface tool calls as a separate field rather than content blocks.
    """
    id: str
    name: str
    args: Dict[str, Any]


@dataclass
class LLMMessage:
    """Normalized conversation message. role is 'system' | 'user' | 'assistant'
    | 'tool'. For 'tool' messages, tool_call_id names which call this is the
    result of, and content is the stringified result.
    """
    role: str
    content: Any  # str | List[LLMContent]
    tool_call_id: Optional[str] = None
    name: Optional[str] = None  # tool name for role='tool'


@dataclass
class LLMResponse:
    """Normalized response from any provider."""
    content: List[LLMContent]            # assistant text + tool_use blocks
    stop_reason: str                     # "stop" | "tool_use" | "length" | ...
    usage_input_tokens: int = 0
    usage_output_tokens: int = 0
    raw: Any = None                      # original SDK response for debugging

    @property
    def text(self) -> str:
        return "".join(c.text or "" for c in self.content if c.type == "text")

    @property
    def tool_calls(self) -> List[LLMContent]:
        return [c for c in self.content if c.type == "tool_use"]


class LLMProvider(abc.ABC):
    """Provider-agnostic chat interface with tool calling."""

    name: str = "base"

    @abc.abstractmethod
    async def chat(
        self,
        messages: List[LLMMessage],
        *,
        system: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> LLMResponse:
        """Send a chat turn. Returns normalized response."""

    @abc.abstractmethod
    def available(self) -> bool:
        """Whether this provider is properly configured (has API key etc)."""
