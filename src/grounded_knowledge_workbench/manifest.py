"""Fail-closed loading and role filtering for public-safe corpus manifests."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


class ManifestError(ValueError):
    """Raised when a corpus manifest violates a deterministic boundary."""


@dataclass(frozen=True)
class DocumentRecord:
    document_id: str
    title: str
    path: Path
    provenance: str
    roles: tuple[str, ...]


@dataclass(frozen=True)
class CorpusManifest:
    schema_version: int
    corpus: str
    roles: tuple[str, ...]
    documents: tuple[DocumentRecord, ...]

    def accessible_documents(self, role: str) -> tuple[DocumentRecord, ...]:
        if role not in self.roles:
            raise ManifestError(f"unknown role: {role}")
        return tuple(document for document in self.documents if role in document.roles)

    def summary(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "corpus": self.corpus,
            "roles": list(self.roles),
            "document_count": len(self.documents),
        }


def _required_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{field} must be a non-empty string")
    return value.strip()


def _safe_document_path(root: Path, value: object) -> Path:
    relative = Path(_required_text(value, "document.path"))
    if relative.is_absolute() or ".." in relative.parts:
        raise ManifestError(f"unsafe document path: {relative}")

    root_resolved = root.resolve()
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise ManifestError(f"document escapes corpus root: {relative}") from exc

    if not resolved.is_file():
        raise ManifestError(f"document does not exist: {relative}")
    return resolved


def load_manifest(path: Path) -> CorpusManifest:
    manifest_path = path.resolve()
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"cannot read manifest: {manifest_path}") from exc

    if not isinstance(payload, dict):
        raise ManifestError("manifest root must be an object")
    if payload.get("schema_version") != 1:
        raise ManifestError("unsupported schema_version")

    raw_roles = payload.get("roles")
    if not isinstance(raw_roles, list) or not raw_roles:
        raise ManifestError("roles must be a non-empty list")
    roles = tuple(_required_text(role, "role") for role in raw_roles)
    if len(set(roles)) != len(roles):
        raise ManifestError("roles must be unique")

    raw_documents = payload.get("documents")
    if not isinstance(raw_documents, list) or not raw_documents:
        raise ManifestError("documents must be a non-empty list")

    documents: list[DocumentRecord] = []
    seen_ids: set[str] = set()
    for raw_document in raw_documents:
        if not isinstance(raw_document, dict):
            raise ManifestError("each document must be an object")
        document_id = _required_text(raw_document.get("id"), "document.id")
        if document_id in seen_ids:
            raise ManifestError(f"duplicate document id: {document_id}")
        seen_ids.add(document_id)

        raw_document_roles = raw_document.get("roles")
        if not isinstance(raw_document_roles, list) or not raw_document_roles:
            raise ManifestError(f"document {document_id} must define roles")
        document_roles = tuple(
            _required_text(role, f"document {document_id} role")
            for role in raw_document_roles
        )
        unknown_roles = sorted(set(document_roles) - set(roles))
        if unknown_roles:
            raise ManifestError(
                f"document {document_id} uses unknown roles: {', '.join(unknown_roles)}"
            )

        documents.append(
            DocumentRecord(
                document_id=document_id,
                title=_required_text(raw_document.get("title"), "document.title"),
                path=_safe_document_path(manifest_path.parent, raw_document.get("path")),
                provenance=_required_text(
                    raw_document.get("provenance"), "document.provenance"
                ),
                roles=document_roles,
            )
        )

    return CorpusManifest(
        schema_version=1,
        corpus=_required_text(payload.get("corpus"), "corpus"),
        roles=roles,
        documents=tuple(documents),
    )
