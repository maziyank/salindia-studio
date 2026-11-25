"""Webhook dispatcher: POST job events to a configurable URL.

Signs each payload with HMAC-SHA256 using the shared WEBHOOK_SECRET, sent in
the `X-PPTMaster-Signature` header as `sha256=<hex>`.

Failures are logged but never raise: a webhook outage must not affect job
execution. Retries use simple exponential backoff (3 attempts).
"""
from __future__ import annotations

import asyncio
import hashlib
import hmac
import json
import logging
from typing import Any, Dict, Optional

import httpx

log = logging.getLogger("webhooks")


def sign_payload(payload: bytes, secret: str) -> str:
    mac = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256)
    return f"sha256={mac.hexdigest()}"


async def dispatch_event(url: str, event: Dict[str, Any], *, secret: Optional[str] = None) -> None:
    body = json.dumps(event, default=str).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if secret:
        headers["X-PPTMaster-Signature"] = sign_payload(body, secret)
    last_err: Optional[Exception] = None
    async with httpx.AsyncClient(timeout=10.0) as client:
        for attempt in range(1, 4):
            try:
                resp = await client.post(url, content=body, headers=headers)
                if resp.status_code < 400:
                    return
                log.info("webhook %s returned %s (attempt %d)", url, resp.status_code, attempt)
            except Exception as e:  # noqa: BLE001
                last_err = e
                log.info("webhook %s failed (attempt %d): %r", url, attempt, e)
            await asyncio.sleep(min(2 ** attempt, 8))
    if last_err:
        log.warning("webhook %s gave up: %r", url, last_err)
