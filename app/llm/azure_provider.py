"""Azure OpenAI provider.

Azure OpenAI exposes the same Chat Completions API as OpenAI proper, so this
provider subclasses OpenAIProvider and only swaps the client construction.
The differences are authentication (api_key + azure_endpoint + api_version) and that
the `model` parameter passed to chat.completions.create is the deployment name.

Message/tool normalization is identical to the OpenAI provider, so we reuse
`_to_openai_messages`, `_normalize_tools`, and `chat` from the parent.
"""
from __future__ import annotations

from typing import Optional

from openai import AsyncAzureOpenAI

from app.config import get_settings
from app.llm.openai_provider import OpenAIProvider


class AzureOpenAIProvider(OpenAIProvider):
    name = "azure"

    def __init__(self) -> None:
        s = get_settings()
        self.api_key = s.azure_api_key
        self.azure_endpoint = s.azure_endpoint
        self.api_version = s.azure_api_version
        # In Azure OpenAI the model name is the deployment name.
        self.model = s.llm_model_azure
        self.temperature = s.llm_temperature
        self.max_tokens = s.llm_max_tokens
        # gpt-5.x / o-series Azure deployments require `max_completion_tokens`.
        self.use_max_completion_tokens = False
        self._client: Optional[AsyncAzureOpenAI] = None

    def _ensure_client(self) -> AsyncAzureOpenAI:
        if self._client is None:
            self._client = AsyncAzureOpenAI(
                azure_endpoint=self.azure_endpoint,
                api_key=self.api_key,
                api_version=self.api_version,
                azure_deployment=self.model,
            )
        return self._client

    def available(self) -> bool:
        return bool(self.api_key and self.azure_endpoint and self.model)
