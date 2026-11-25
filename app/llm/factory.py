"""LLM factory. Resolves the active provider from settings, with a thin
runtime override so a per-job request can ask for a specific provider
(used by tests and future per-tenant routing).

Provider SDK imports are deferred so the service can boot even if some SDKs
aren't installed (only the active provider needs to be importable).
"""
from __future__ import annotations

from functools import lru_cache
from typing import Optional

from app.config import get_settings
from app.llm.base import LLMProvider


def _build(provider: str) -> LLMProvider:
    p = provider.lower()
    if p == "openai":
        from app.llm.openai_provider import OpenAIProvider
        prov = OpenAIProvider(kimi=False)
    elif p == "kimi":
        from app.llm.openai_provider import OpenAIProvider
        prov = OpenAIProvider(kimi=True)
    elif p == "anthropic":
        from app.llm.anthropic_provider import AnthropicProvider
        prov = AnthropicProvider()
    elif p == "gemini":
        from app.llm.gemini_provider import GeminiProvider
        prov = GeminiProvider()
    elif p == "azure":
        from app.llm.azure_provider import AzureOpenAIProvider
        prov = AzureOpenAIProvider()
    else:
        raise ValueError(f"unknown LLM provider: {provider}")
    if not prov.available():
        raise RuntimeError(
            f"LLM provider '{p}' is not configured. Set the corresponding API key in .env."
        )
    return prov


_cached: dict = {}


def get_llm(override: Optional[str] = None) -> LLMProvider:
    """Return the LLM provider. If `override` is given (e.g. 'gemini'), build a
    fresh instance bypassing the cache; otherwise return the cached default.
    """
    if override:
        return _build(override)
    if "default" not in _cached:
        s = get_settings()
        _cached["default"] = _build(s.llm_provider)
    return _cached["default"]


def list_available_providers() -> list[str]:
    """Which providers have API keys configured. Used by the /health endpoint.
    Does NOT verify the SDK is installed - just checks configuration."""
    s = get_settings()
    out = []
    if s.openai_api_key:
        out.append("openai")
    if s.kimi_api_key:
        out.append("kimi")
    if s.anthropic_api_key:
        out.append("anthropic")
    if s.gemini_api_key:
        out.append("gemini")
    if s.azure_api_key and s.azure_endpoint and s.llm_model_azure:
        out.append("azure")
    return out
