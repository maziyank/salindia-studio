"""Image-generation backends for the agent loop.

Mirrors the LLM provider layer: a small provider interface plus a factory that
picks the backend from `IMAGE_BACKEND` (openai | azure | gemini | qwen). The
agent loop only depends on `ImageProvider.generate`, never on a specific SDK.
"""
