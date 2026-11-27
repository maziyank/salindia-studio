"""Abstract image-generation provider + shared response decoding.

Design rationale: every backend (Azure OpenAI, OpenAI, Gemini/Imagen, Qwen)
speaks its own shape. The agent loop must not know which one is active, so
each backend normalizes its result to raw image bytes through this interface.
"""
from __future__ import annotations

import abc
import base64
from typing import Any

import httpx


class ImageProvider(abc.ABC):
    """Provider-agnostic text-to-image interface."""

    name: str = "base"

    @abc.abstractmethod
    async def generate(self, prompt: str, *, size: str = "1024x1024") -> bytes:
        """Generate one image from `prompt` and return the raw image bytes."""

    @abc.abstractmethod
    def available(self) -> bool:
        """Whether this provider is properly configured (key/endpoint/model)."""


async def image_bytes_from_item(item: Any) -> bytes:
    """Decode one image from an OpenAI-style response item.

    Returns inline base64 when present (gpt-image-1, DashScope), otherwise
    downloads the returned URL (dall-e-3). Shared by the OpenAI-compatible
    backends so the decode logic lives in one place.
    """
    b64 = getattr(item, "b64_json", None)
    if b64:
        return base64.b64decode(b64)
    url = getattr(item, "url", None)
    if url:
        async with httpx.AsyncClient(timeout=60.0, follow_redirects=True) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.content
    raise RuntimeError("image provider returned neither b64_json nor url")
