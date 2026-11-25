"""Local filesystem backend."""
from __future__ import annotations

import mimetypes
import os
import shutil
import tempfile
from pathlib import Path
from typing import IO, List, Optional

import aiofiles

from app.storage.base import StorageBackend, StoredFile


class LocalStorage(StorageBackend):
    def __init__(self, root: str) -> None:
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        # Mirror of the S3 "presign" concept: a local file URL the client can
        # fetch if the API server is reachable.
        self._tmp_cache = Path(tempfile.gettempdir()) / "pptmaster_storage_cache"
        self._tmp_cache.mkdir(parents=True, exist_ok=True)

    def _full(self, logical_path: str) -> Path:
        # Disallow traversal.
        parts = [p for p in logical_path.split("/") if p not in ("", ".")]
        if any(p == ".." for p in parts):
            raise ValueError(f"illegal path: {logical_path}")
        return self.root.joinpath(*parts)

    async def put(self, logical_path: str, data: bytes, content_type: str = "application/octet-stream") -> StoredFile:
        full = self._full(logical_path)
        full.parent.mkdir(parents=True, exist_ok=True)
        async with aiofiles.open(full, "wb") as f:
            await f.write(data)
        ct = content_type or mimetypes.guess_type(full.name)[0] or "application/octet-stream"
        return StoredFile(path=logical_path, size=len(data), content_type=ct)

    async def put_stream(self, logical_path: str, stream: IO[bytes], content_type: str = "application/octet-stream") -> StoredFile:
        full = self._full(logical_path)
        full.parent.mkdir(parents=True, exist_ok=True)
        size = 0
        async with aiofiles.open(full, "wb") as f:
            while True:
                chunk = stream.read(1 << 20)
                if not chunk:
                    break
                await f.write(chunk)
                size += len(chunk)
        ct = content_type or mimetypes.guess_type(full.name)[0] or "application/octet-stream"
        return StoredFile(path=logical_path, size=size, content_type=ct)

    async def get(self, logical_path: str) -> bytes:
        full = self._full(logical_path)
        async with aiofiles.open(full, "rb") as f:
            return await f.read()

    async def open_read(self, logical_path: str) -> IO[bytes]:
        full = self._full(logical_path)
        return open(full, "rb")

    async def exists(self, logical_path: str) -> bool:
        return self._full(logical_path).exists()

    async def delete(self, logical_path: str) -> None:
        full = self._full(logical_path)
        if full.is_dir():
            shutil.rmtree(full, ignore_errors=True)
        elif full.exists():
            full.unlink()

    async def list_dir(self, prefix: str) -> List[StoredFile]:
        base = self._full(prefix)
        out: List[StoredFile] = []
        if not base.exists():
            return out
        for p in sorted(base.rglob("*")):
            if p.is_file():
                rel = p.relative_to(self.root).as_posix()
                out.append(StoredFile(path=rel, size=p.stat().st_size,
                                       content_type=mimetypes.guess_type(p.name)[0] or "application/octet-stream"))
        return out

    async def local_path(self, logical_path: str) -> Optional[str]:
        full = self._full(logical_path)
        return str(full) if full.exists() else None

    async def make_local_path(self, logical_path: str) -> str:
        full = self._full(logical_path)
        if not full.exists():
            raise FileNotFoundError(logical_path)
        return str(full)

    async def public_url(self, logical_path: str, expires_seconds: int = 3600) -> Optional[str]:
        # The HTTP layer exposes /files/{path} for downloads; we just confirm existence.
        full = self._full(logical_path)
        return f"file://{full}" if full.exists() else None
