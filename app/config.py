"""Centralized configuration via pydantic-settings."""
from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # App
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_log_level: str = "info"
    api_keys_raw: str = Field(default="changeme-dev-key", alias="API_KEYS")
    allowed_routes_raw: str = Field(
        default="create,edit,template,postprocess", alias="ALLOWED_ROUTES"
    )
    max_concurrent_jobs: int = 2
    max_job_timeout_seconds: int = 1800
    max_source_size_mb: int = 50

    # Storage
    storage_backend: str = "local"
    storage_local_root: str = "/data"
    storage_s3_bucket: str = ""
    storage_s3_prefix: str = "pptmaster/"
    storage_s3_region: str = "us-east-1"

    # PPT Master repo
    pptmaster_repo_dir: str = "/opt/ppt-master"
    pptmaster_repo_url: str = "https://github.com/hugohe3/ppt-master.git"
    pptmaster_repo_branch: str = "main"
    pptmaster_auto_setup: bool = True

    # LLM
    llm_provider: str = "openai"
    llm_model_openai: str = "gpt-4.1"
    llm_model_anthropic: str = "claude-sonnet-4-20250514"
    llm_model_gemini: str = "gemini-2.5-pro"
    llm_model_kimi: str = "moonshot-v1-128k"
    llm_model_azure: str = ""
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    gemini_api_key: str = ""
    kimi_api_key: str = ""
    azure_api_key: str = ""
    azure_endpoint: str = ""
    azure_api_version: str = "2024-02-15-preview"
    openai_base_url: str = ""
    kimi_base_url: str = "https://api.moonshot.cn/v1"
    # Generic OpenAI-compatible provider (any endpoint speaking the OpenAI
    # Chat Completions API, e.g. Groq, OpenRouter, vLLM, Ollama, Together...).
    llm_model_custom: str = ""
    custom_api_key: str = ""
    custom_base_url: str = ""
    # Optional display name shown in the web UI (defaults to "Custom").
    custom_label: str = ""
    llm_temperature: float = 0.4
    llm_max_tokens: int = 8192
    llm_max_iterations: int = 40

    # Webhooks
    webhook_default_url: str = ""
    webhook_secret: str = ""

    # MCP server (exposes this service as Model Context Protocol tools)
    mcp_enabled: bool = True
    mcp_path: str = "/mcp"
    # Comma-separated Host values the MCP endpoint accepts. Empty = no Host
    # filtering (needed behind a reverse proxy/domain).
    mcp_allowed_hosts_raw: str = Field(default="", alias="MCP_ALLOWED_HOSTS")

    # ----- Derived -----
    @property
    def api_keys(self) -> List[str]:
        return [k.strip() for k in self.api_keys_raw.split(",") if k.strip()]

    @property
    def allowed_routes(self) -> List[str]:
        return [r.strip().lower() for r in self.allowed_routes_raw.split(",") if r.strip()]

    @property
    def mcp_allowed_hosts(self) -> List[str]:
        return [h.strip() for h in self.mcp_allowed_hosts_raw.split(",") if h.strip()]

    @field_validator("storage_backend")
    @classmethod
    def _validate_backend(cls, v: str) -> str:
        v = v.lower()
        if v not in {"local", "s3"}:
            raise ValueError("STORAGE_BACKEND must be 'local' or 's3'")
        return v

    @field_validator("llm_provider")
    @classmethod
    def _validate_provider(cls, v: str) -> str:
        v = v.lower()
        if v not in {"openai", "anthropic", "gemini", "kimi", "azure", "custom"}:
            raise ValueError(
                "LLM_PROVIDER must be one of openai|anthropic|gemini|kimi|azure|custom"
            )
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
