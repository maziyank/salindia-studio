"""Smoke test: verify the app imports, the router is wired, and the
health endpoint responds. Does NOT call a real LLM (no API key needed).

Run with:  python -m pytest tests/test_smoke.py -v
or:        python tests/test_smoke.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Ensure the project root is on sys.path so `app` imports work when run from anywhere.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Force a minimal env so settings load without a real .env
os.environ.setdefault("API_KEYS", "test-key")
os.environ.setdefault("OPENAI_API_KEY", "")
os.environ.setdefault("ANTHROPIC_API_KEY", "")
os.environ.setdefault("GEMINI_API_KEY", "")
os.environ.setdefault("KIMI_API_KEY", "")
os.environ.setdefault("PPTMASTER_AUTO_SETUP", "false")
os.environ.setdefault("STORAGE_LOCAL_ROOT", str(ROOT / "data"))


def test_imports():
    from app.config import get_settings
    from app.storage.factory import get_storage
    from app.llm.factory import list_available_providers
    from app.agent.loop import AgentLoop
    from app.agent.tools import get_default_tools
    from app.jobs.manager import get_job_manager
    from app.api.routes import router
    from app.main import app
    s = get_settings()
    assert s.api_keys == ["test-key"]
    assert "create" in s.allowed_routes
    tools = get_default_tools()
    schemas = tools.schemas()
    names = {t["name"] for t in schemas}
    assert "read_skill_md" in names
    assert "finalize_deck" in names
    assert "progress" in names
    print("OK: imports + tool registry")


def test_health_endpoint():
    from fastapi.testclient import TestClient
    from app.main import app
    # Skip lifespan (it would try to clone the repo)
    with TestClient(app) as client:
        r = client.get("/health")
        assert r.status_code == 200, r.text
        body = r.json()
        assert "ppt_master_ready" in body
        assert "available_providers" in body
        print("OK: /health ->", body["status"])


def test_auth_enforced():
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as client:
        # No API key
        r = client.get("/jobs")
        assert r.status_code == 401, r.text
        # Wrong API key
        r = client.get("/jobs", headers={"X-API-Key": "wrong"})
        assert r.status_code == 401, r.text
        # Right API key
        r = client.get("/jobs", headers={"X-API-Key": "test-key"})
        assert r.status_code == 200, r.text
        print("OK: API key auth enforced")


def test_job_create_validation():
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as client:
        # route not in ALLOWED_ROUTES
        r = client.post(
            "/jobs/json",
            headers={"X-API-Key": "test-key"},
            json={"prompt": "x", "route": "nonexistent"},
        )
        assert r.status_code in (400, 422, 500), r.text
        print("OK: route validation")


if __name__ == "__main__":
    test_imports()
    test_health_endpoint()
    test_auth_enforced()
    test_job_create_validation()
    print("\nAll smoke tests passed.")
