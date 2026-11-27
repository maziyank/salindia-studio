"""Image provider factory. Resolves the active backend from IMAGE_BACKEND.

SDK imports are deferred so the service boots even when a given backend's SDK
isn't installed (only the active backend needs to be importable).
"""
from __future__ import annotations

from functools import lru_cache

from app.config import get_settings
from app.images.base import ImageProvider


def _build(backend: str) -> ImageProvider:
    b = backend.lower()
    if b == "openai":
        from app.images.openai_image import OpenAIImageProvider
        return OpenAIImageProvider()
    if b == "azure":
        from app.images.openai_image import OpenAIImageProvider
        return OpenAIImageProvider(azure=True)
    if b == "gemini":
        from app.images.gemini_image import GeminiImageProvider
        return GeminiImageProvider()
    if b == "qwen":
        from app.images.qwen_image import QwenImageProvider
        return QwenImageProvider()
    raise ValueError(f"unknown image backend: {backend}")


@lru_cache
def get_image_provider() -> ImageProvider:
    """Return the image provider selected by IMAGE_BACKEND."""
    return _build(get_settings().image_backend)


CATALOG: list[dict] = [
    {"id": "openai", "label": "OpenAI", "env": "OPENAI_API_KEY + IMAGE_MODEL_OPENAI"},
    {"id": "azure", "label": "Azure OpenAI",
     "env": "AZURE_API_KEY + AZURE_ENDPOINT + IMAGE_MODEL_AZURE"},
    {"id": "gemini", "label": "Google Gemini / Imagen",
     "env": "GEMINI_API_KEY + IMAGE_MODEL_GEMINI"},
    {"id": "qwen", "label": "Qwen / DashScope",
     "env": "QWEN_API_KEY + IMAGE_MODEL_QWEN"},
]
