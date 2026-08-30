"""Deterministic core for Grounded Knowledge Workbench."""

from .manifest import CorpusManifest, DocumentRecord, ManifestError, load_manifest

__all__ = ["CorpusManifest", "DocumentRecord", "ManifestError", "load_manifest"]
__version__ = "0.1.0"
