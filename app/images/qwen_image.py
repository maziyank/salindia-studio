"""Qwen-Image generation via Alibaba DashScope.

DashScope exposes an OpenAI-compatible `/images/generations` endpoint in its
"compatible-mode", so we reuse the OpenAI client pointed at the DashScope base
URL. Model and base URL are configurable so any DashScope image model works
(qwen-image, wanx2.1-t2i-*, ...).

Config: QWEN_API_KEY + IMAGE_MODEL_QWEN + QWEN_BASE_URL.
"""
from __future__ import annotations

from typing import Optional

from openai import AsyncOpenAI

from app.config import get_settings
from app.images.base import ImageProvider, image_bytes_from_item


class QwenImageProvider(ImageProvider):
    name = "qwen"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.qwen_api_key
        self.base_url = s.qwen_base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.model = s.image_model_qwen
        self._client: Optional[AsyncOpenAI] = None

    def _ensure_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        return self._client

    def available(self) -> bool:
        return bool(self.api_key and self.model and self.base_url)

    async def generate(self, prompt: str, *, size: str = "1024x1024") -> bytes:
        client = self._ensure_client()
        resp = await client.images.generate(
            model=self.model, prompt=prompt, size=size, n=1
        )
        return await image_bytes_from_item(resp.data[0])
