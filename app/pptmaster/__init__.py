"""PPT Master package: locates and (optionally) auto-installs the upstream
hugohe3/ppt-master repo so the agent loop has a real working tree to drive.
"""
from app.pptmaster.runtime import PPTMasterRuntime, get_runtime

__all__ = ["PPTMasterRuntime", "get_runtime"]
