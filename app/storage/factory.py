"""Factory: pick storage backend from settings. SDK imports are deferred so
the service can boot with only the active backend's deps installed.
"""
from __future__ import annotations

from typing import Optional

from app.config import get_settings
from app.storage.base import StorageBackend


_cached: dict = {}


def _build(backend: str) -> StorageBackend:
    s = get_settings()
    if backend == "local":
        from app.storage.local import LocalStorage
        return LocalStorage(root=s.storage_local_root)
    if backend == "s3":
        if not s.storage_s3_bucket:
            raise RuntimeError("STORAGE_S3_BUCKET is required when STORAGE_BACKEND=s3")
        from app.storage.s3 import S3Storage
        return S3Storage(bucket=s.storage_s3_bucket, prefix=s.storage_s3_prefix, region=s.storage_s3_region)
    raise RuntimeError(f"unknown storage backend: {backend}")


def get_storage() -> StorageBackend:
    if "default" not in _cached:
        s = get_settings()
        _cached["default"] = _build(s.storage_backend)
    return _cached["default"]
