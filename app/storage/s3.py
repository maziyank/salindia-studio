"""S3-compatible backend (AWS S3, MinIO, R2, etc.). Uses boto3 in a thread
executor because boto3 is blocking.
"""
from __future__ import annotations

import asyncio
import io
import mimetypes
import tempfile
import uuid
from pathlib import Path
from typing import IO, List, Optional

import boto3
from botocore.client import Config as BotoConfig
from botocore.exceptions import ClientError

from app.storage.base import StorageBackend, StoredFile


class S3Storage(StorageBackend):
    def __init__(self, bucket: str, prefix: str, region: str) -> None:
        self.bucket = bucket
        self.prefix = prefix.rstrip("/") + "/"
        self.region = region
        self._client = boto3.client("s3", region_name=region, config=BotoConfig(signature_version="s3v4"))
        self._loop = asyncio.get_event_loop()
        self._cache_dir = Path(tempfile.gettempdir()) / "pptmaster_s3_cache"
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def _key(self, logical_path: str) -> str:
        return self.prefix + logical_path.lstrip("/")

    async def _run(self, fn, *args, **kwargs):
        return await self._loop.run_in_executor(None, lambda: fn(*args, **kwargs))

    async def put(self, logical_path: str, data: bytes, content_type: str = "application/octet-stream") -> StoredFile:
        ct = content_type or mimetypes.guess_type(logical_path)[0] or "application/octet-stream"
        key = self._key(logical_path)
        await self._run(self._client.put_object, Bucket=self.bucket, Key=key, Body=data, ContentType=ct)
        return StoredFile(path=logical_path, size=len(data), content_type=ct)

    async def put_stream(self, logical_path: str, stream: IO[bytes], content_type: str = "application/octet-stream") -> StoredFile:
        data = stream.read()
        return await self.put(logical_path, data, content_type)

    async def get(self, logical_path: str) -> bytes:
        key = self._key(logical_path)
        resp = await self._run(self._client.get_object, Bucket=self.bucket, Key=key)
        return await self._run(resp["Body"].read)

    async def open_read(self, logical_path: str) -> IO[bytes]:
        data = await self.get(logical_path)
        return io.BytesIO(data)

    async def exists(self, logical_path: str) -> bool:
        key = self._key(logical_path)
        try:
            await self._run(self._client.head_object, Bucket=self.bucket, Key=key)
            return True
        except ClientError:
            return False

    async def delete(self, logical_path: str) -> None:
        key = self._key(logical_path)
        await self._run(self._client.delete_object, Bucket=self.bucket, Key=key)

    async def list_dir(self, prefix: str) -> List[StoredFile]:
        key_prefix = self._key(prefix)
        paginator = self._client.get_paginator("list_objects_v2")
        out: List[StoredFile] = []
        for page in await self._run(lambda: list(paginator.paginate(Bucket=self.bucket, Prefix=key_prefix))):
            for obj in page.get("Contents", []):
                rel = obj["Key"][len(self.prefix):]
                out.append(StoredFile(path=rel, size=obj.get("Size", 0),
                                       content_type=mimetypes.guess_type(obj["Key"])[0] or "application/octet-stream"))
        return out

    async def local_path(self, logical_path: str) -> Optional[str]:
        # S3 has no native on-disk path; callers must use make_local_path.
        return None

    async def make_local_path(self, logical_path: str) -> str:
        """Download the object to a temp cache and return its path. The path
        is stable for the process lifetime (keyed by object key), so repeated
        reads of the same file in one job reuse the cache.
        """
        key = self._key(logical_path)
        cache_file = self._cache_dir / f"{uuid.uuid4().hex}_{logical_path.replace('/', '_')}"
        await cache_file.parent.mkdir(parents=True, exist_ok=True)
        await self._run(self._client.download_file, self.bucket, key, str(cache_file))
        return str(cache_file)

    async def public_url(self, logical_path: str, expires_seconds: int = 3600) -> Optional[str]:
        key = self._key(logical_path)
        try:
            url = await self._run(
                self._client.generate_presigned_url,
                "get_object",
                Params={"Bucket": self.bucket, "Key": key},
                ExpiresIn=expires_seconds,
            )
            return url
        except ClientError:
            return None
