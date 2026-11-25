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
    elif p == "custom":
        from app.llm.custom_provider import CustomOpenAICompatibleProvider
        prov = CustomOpenAICompatibleProvider()
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


# Static catalog of every provider the factory can build, in display order,
# with human labels and the env vars needed to enable each. The web UI uses
# this to render all providers and show hints for the ones not yet configured.
PROVIDER_CATALOG: list[dict] = [
    {"id": "openai", "label": "OpenAI", "env": "OPENAI_API_KEY"},
    {"id": "anthropic", "label": "Anthropic / Claude", "env": "ANTHROPIC_API_KEY"},
    {"id": "gemini", "label": "Google Gemini", "env": "GEMINI_API_KEY"},
    {"id": "kimi", "label": "Kimi / Moonshot", "env": "KIMI_API_KEY"},
    {"id": "azure", "label": "Azure OpenAI", "env": "AZURE_API_KEY + AZURE_ENDPOINT + LLM_MODEL_AZURE"},
    {"id": "custom", "label": "Custom (OpenAI-compatible)",
     "env": "CUSTOM_BASE_URL + LLM_MODEL_CUSTOM (+ CUSTOM_API_KEY)"},
]


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
    if s.custom_base_url and s.llm_model_custom:
        out.append("custom")
    return out


def list_provider_catalog() -> list[dict]:
    """Full provider catalog with a `configured` flag for each entry, so the UI
    can show every option while disabling the ones missing credentials."""
    configured = set(list_available_providers())
    s = get_settings()
    out = []
    for p in PROVIDER_CATALOG:
        entry = {**p, "configured": p["id"] in configured}
        # Let the operator rename the generic provider for a clearer dropdown.
        if p["id"] == "custom" and s.custom_label:
            entry["label"] = s.custom_label
        out.append(entry)
    return out
