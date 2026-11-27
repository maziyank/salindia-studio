"""OpenAI image generation, covering both OpenAI proper and Azure OpenAI.

Both expose the same `images.generate` API, so one class handles them; Azure
only differs in client construction (azure_endpoint + api_version) and the fact
that `model` is the deployment name. gpt-image-1 returns base64 inline, while
dall-e-3 returns a URL unless asked for b64_json — both are handled.

Config: OPENAI_API_KEY / IMAGE_MODEL_OPENAI (openai) and
AZURE_API_KEY / AZURE_ENDPOINT / AZURE_API_VERSION / IMAGE_MODEL_AZURE (azure).
"""
from __future__ import annotations

from typing import Any, Optional, Union

from openai import AsyncAzureOpenAI, AsyncOpenAI

from app.config import get_settings
from app.images.base import ImageProvider, image_bytes_from_item


class OpenAIImageProvider(ImageProvider):
    name = "openai"

    def __init__(self, *, azure: bool = False) -> None:
        s = get_settings()
        self.azure = azure
        if azure:
            self.name = "azure"
            self.api_key = s.azure_api_key
            self.endpoint = s.azure_endpoint
            self.api_version = s.azure_api_version
            # For Azure, `model` is the image deployment name.
            self.model = s.image_model_azure
        else:
            self.api_key = s.openai_api_key
            self.base_url = s.openai_base_url or None
            self.model = s.image_model_openai
        self._client: Optional[Union[AsyncOpenAI, AsyncAzureOpenAI]] = None

    def _ensure_client(self) -> Union[AsyncOpenAI, AsyncAzureOpenAI]:
        if self._client is None:
            if self.azure:
                self._client = AsyncAzureOpenAI(
                    azure_endpoint=self.endpoint,
                    api_key=self.api_key,
                    api_version=self.api_version,
                )
            else:
                self._client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        return self._client

    def available(self) -> bool:
        if self.azure:
            return bool(self.api_key and self.endpoint and self.model)
        return bool(self.api_key and self.model)

    async def generate(self, prompt: str, *, size: str = "1024x1024") -> bytes:
        client = self._ensure_client()
        resp = await client.images.generate(
            model=self.model, prompt=prompt, size=size, n=1
        )
        return await image_bytes_from_item(resp.data[0])
