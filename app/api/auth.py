"""API key auth middleware. Validates `X-API-Key` header against the
configured list. Returns 401 if missing/invalid.

WebSocket auth: the key is passed as a `?api_key=` query parameter because
browsers cannot set custom headers on WS handshakes.

MCP auth: `MCPAuthMiddleware` guards the mounted MCP app with the same keys,
sent as `X-API-Key` or `Authorization: Bearer <key>`.
"""
from __future__ import annotations

import json
from typing import List, Optional

from fastapi import Header, HTTPException, Query, status

from app.config import get_settings


async def require_api_key(x_api_key: Optional[str] = Header(default=None, alias="X-API-Key")) -> str:
    s = get_settings()
    if not s.api_keys:
        # No keys configured -> deny all (fails closed). The default
        # .env.example ships with `changeme-dev-key` so this only triggers
        # if an operator explicitly empties the var.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="API_KEYS not configured")
    if not x_api_key or x_api_key not in s.api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid or missing API key")
    return x_api_key


async def require_api_key_sse(
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
    api_key: Optional[str] = Query(default=None),
) -> str:
    """Auth for the SSE stream. Browser `EventSource` cannot set custom
    headers, so the key may also arrive as `?api_key=` (same as WebSocket)."""
    s = get_settings()
    if not s.api_keys:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="API_KEYS not configured")
    key = x_api_key or api_key
    if not key or key not in s.api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid or missing API key")
    return key


async def require_api_key_ws(api_key: Optional[str] = Query(default=None)) -> str:
    s = get_settings()
    if not s.api_keys or not api_key or api_key not in s.api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid or missing api_key")
    return api_key


class MCPAuthMiddleware:
    """Pure-ASGI middleware guarding the mounted MCP app.

    Requests whose path is under `path_prefix` must present one of `api_keys`
    either as `X-API-Key` or as `Authorization: Bearer <key>`. Everything else
    is passed through untouched.
    """

    def __init__(self, app, path_prefix: str = "/mcp", api_keys: Optional[List[str]] = None) -> None:
        self.app = app
        self.path_prefix = "/" + path_prefix.strip("/")
        self.api_keys = api_keys or []

    def _guards(self, path: str) -> bool:
        return path == self.path_prefix or path.startswith(self.path_prefix + "/")

    def _presented_key(self, scope) -> str:
        headers = {k.decode("latin-1").lower(): v.decode("latin-1") for k, v in scope.get("headers", [])}
        key = headers.get("x-api-key", "")
        if not key:
            auth = headers.get("authorization", "")
            if auth.lower().startswith("bearer "):
                key = auth[7:].strip()
        return key

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] != "http" or not self._guards(scope.get("path", "")):
            await self.app(scope, receive, send)
            return
        if self.api_keys and self._presented_key(scope) in self.api_keys:
            await self.app(scope, receive, send)
            return
        body = json.dumps({"error": "unauthorized", "detail": "invalid or missing API key"}).encode()
        await send({
            "type": "http.response.start",
            "status": status.HTTP_401_UNAUTHORIZED,
            "headers": [(b"content-type", b"application/json"),
                        (b"content-length", str(len(body)).encode())],
        })
        await send({"type": "http.response.body", "body": body})
