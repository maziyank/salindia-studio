"""Storage package: pluggable backend for source files and output .pptx.

Backend SDK imports (boto3) are deferred to factory build time so this
package imports cleanly without optional deps installed.
"""
from app.storage.base import StorageBackend

__all__ = ["StorageBackend"]
