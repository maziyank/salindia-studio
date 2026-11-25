"""Abstract storage interface.

The agent loop and job manager work against this interface, so they don't
care whether files end up on local disk or in S3. Each job gets a private
namespace `<storage_root>/<job_id>/` containing `sources/`, `work/`, and
`exports/`.
"""
from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import IO, List, Optional


@dataclass
class StoredFile:
    """Metadata about a stored file."""
    path: str          # logical path relative to the storage root, e.g. "<job_id>/sources/report.pdf"
    size: int          # bytes
    content_type: str  # best-effort MIME type


class StorageBackend(abc.ABC):
    """Pluggable storage backend. All paths are forward-slash logical paths
    relative to the configured root. Implementations must be safe to call
    from async contexts (use run_in_executor for blocking IO).
    """

    @abc.abstractmethod
    async def put(self, logical_path: str, data: bytes, content_type: str = "application/octet-stream") -> StoredFile:
        """Store raw bytes at logical_path."""

    @abc.abstractmethod
    async def put_stream(self, logical_path: str, stream: IO[bytes], content_type: str = "application/octet-stream") -> StoredFile:
        """Store from a file-like stream (used for upload form)."""

    @abc.abstractmethod
    async def get(self, logical_path: str) -> bytes:
        """Read raw bytes."""

    @abc.abstractmethod
    async def open_read(self, logical_path: str) -> IO[bytes]:
        """Return a readable binary file-like object. Caller closes it."""

    @abc.abstractmethod
    async def exists(self, logical_path: str) -> bool:
        ...

    @abc.abstractmethod
    async def delete(self, logical_path: str) -> None:
        ...

    @abc.abstractmethod
    async def list_dir(self, prefix: str) -> List[StoredFile]:
        """List files under a logical prefix."""

    @abc.abstractmethod
    async def local_path(self, logical_path: str) -> Optional[str]:
        """If the backend exposes a real filesystem path (local backend),
        return it; otherwise return None and callers must use `get`/`open_read`.
        The PPT Master pipeline needs a real on-disk path to feed its scripts,
        so when this returns None the job manager stages files to a temp dir.
        """

    @abc.abstractmethod
    async def public_url(self, logical_path: str, expires_seconds: int = 3600) -> Optional[str]:
        """A URL a client can fetch (presigned S3 URL or local file:// URL)."""

    @abc.abstractmethod
    async def make_local_path(self, logical_path: str) -> str:
        """Guarantee a real on-disk path for the file. For local backends this
        is a no-op; for S3 it downloads to a temp cache. Used to hand a real
        path to the PPT Master subprocess.
        """
