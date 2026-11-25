"""LLM provider abstraction.

All providers expose a single async method `chat(messages, tools, system)`
returning a normalized response. The agent loop only depends on the abstract
interface, so providers can be swapped at runtime via env var.

Normalization is critical: each provider has a slightly different shape for
tool calls and content blocks, but the agent loop needs a single shape.

Note: provider SDK imports are deferred to factory build time, so importing
this package does NOT require all SDKs to be installed.
"""
from app.llm.base import (
    LLMProvider,
    LLMResponse,
    LLMToolCall,
    LLMContent,
    LLMMessage,
)

__all__ = [
    "LLMProvider",
    "LLMResponse",
    "LLMToolCall",
    "LLMContent",
    "LLMMessage",
]
