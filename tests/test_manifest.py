from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from grounded_knowledge_workbench.manifest import ManifestError, load_manifest
from grounded_knowledge_workbench.cli import DEFAULT_MANIFEST


MANIFEST_PATH = DEFAULT_MANIFEST


class ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = load_manifest(MANIFEST_PATH)

    def test_reader_sees_only_public_operations_overview(self) -> None:
        document_ids = {
            document.document_id
            for document in self.manifest.accessible_documents("reader")
        }
        self.assertEqual(document_ids, {"operations-overview"})

    def test_engineer_cannot_see_reviewer_register(self) -> None:
        document_ids = {
            document.document_id
            for document in self.manifest.accessible_documents("engineer")
        }
        self.assertEqual(
            document_ids, {"operations-overview", "maintenance-runbook"}
        )
        self.assertNotIn("review-register", document_ids)

    def test_reviewer_sees_complete_synthetic_corpus(self) -> None:
        document_ids = {
            document.document_id
            for document in self.manifest.accessible_documents("reviewer")
        }
        self.assertEqual(
            document_ids,
            {"operations-overview", "maintenance-runbook", "review-register"},
        )

    def test_unknown_role_fails_closed(self) -> None:
        with self.assertRaisesRegex(ManifestError, "unknown role"):
            self.manifest.accessible_documents("administrator")

    def test_traversal_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            payload = {
                "schema_version": 1,
                "corpus": "unsafe fixture",
                "roles": ["reader"],
                "documents": [
                    {
                        "id": "escape",
                        "title": "Escape",
                        "path": "../outside.md",
                        "provenance": "synthetic",
                        "roles": ["reader"],
                    }
                ],
            }
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "unsafe document path"):
                load_manifest(manifest_path)

    def test_absolute_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            outside = root / "outside.md"
            outside.write_text("synthetic", encoding="utf-8")
            manifest_path = self._write_single_document_manifest(
                root, str(outside.resolve())
            )
            with self.assertRaisesRegex(ManifestError, "unsafe document path"):
                load_manifest(manifest_path)

    def test_missing_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            manifest_path = self._write_single_document_manifest(root, "missing.md")
            with self.assertRaisesRegex(ManifestError, "document does not exist"):
                load_manifest(manifest_path)

    def test_symlink_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            corpus_root = temporary_root / "corpus"
            corpus_root.mkdir()
            outside = temporary_root / "outside.md"
            outside.write_text("synthetic", encoding="utf-8")
            (corpus_root / "linked.md").symlink_to(outside)
            manifest_path = self._write_single_document_manifest(
                corpus_root, "linked.md"
            )
            with self.assertRaisesRegex(ManifestError, "document escapes corpus root"):
                load_manifest(manifest_path)

    def test_malformed_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            manifest_path = Path(temporary_directory) / "manifest.json"
            manifest_path.write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "cannot read manifest"):
                load_manifest(manifest_path)

    @staticmethod
    def _write_single_document_manifest(root: Path, document_path: str) -> Path:
        payload = {
            "schema_version": 1,
            "corpus": "boundary fixture",
            "roles": ["reader"],
            "documents": [
                {
                    "id": "boundary-document",
                    "title": "Boundary Document",
                    "path": document_path,
                    "provenance": "synthetic",
                    "roles": ["reader"],
                }
            ],
        }
        manifest_path = root / "manifest.json"
        manifest_path.write_text(json.dumps(payload), encoding="utf-8")
        return manifest_path


if __name__ == "__main__":
    unittest.main()
