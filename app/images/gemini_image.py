"""Google Gemini / Imagen image generation via the google-genai SDK.

Config: GEMINI_API_KEY + IMAGE_MODEL_GEMINI (e.g. imagen-3.0-generate-002).
Imagen controls output shape with an aspect ratio rather than pixel size, so
the `size` argument is accepted for interface parity but not used here.
"""
from __future__ import annotations

from typing import Any, Optional

from app.config import get_settings
from app.images.base import ImageProvider


class GeminiImageProvider(ImageProvider):
    name = "gemini"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.gemini_api_key
        self.model = s.image_model_gemini
        self._client: Optional[Any] = None

    def _ensure_client(self) -> Any:
        if self._client is None:
            from google import genai
            self._client = genai.Client(api_key=self.api_key)
        return self._client

    def available(self) -> bool:
        return bool(self.api_key and self.model)

    async def generate(self, prompt: str, *, size: str = "1024x1024") -> bytes:
        from google.genai import types as gtypes

        client = self._ensure_client()
        resp = await client.aio.models.generate_images(
            model=self.model,
            prompt=prompt,
            config=gtypes.GenerateImagesConfig(number_of_images=1),
        )
        images = getattr(resp, "generated_images", None) or []
        if not images:
            raise RuntimeError("gemini returned no images")
        data = getattr(images[0].image, "image_bytes", None)
        if not data:
            raise RuntimeError("gemini image had no bytes")
        return data
