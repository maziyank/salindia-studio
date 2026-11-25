"""API key auth middleware. Validates `X-API-Key` header against the
configured list. Returns 401 if missing/invalid.

WebSocket auth: the key is passed as a `?api_key=` query parameter because
browsers cannot set custom headers on WS handshakes.
"""
from __future__ import annotations

from typing import Optional

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
