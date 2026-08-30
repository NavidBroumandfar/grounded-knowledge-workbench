"""Command-line evidence surface for the deterministic project foundation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .manifest import ManifestError, load_manifest


DEFAULT_MANIFEST = (
    Path(__file__).resolve().parent / "resources" / "synthetic" / "manifest.json"
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gkw")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="show validated foundation status")
    status.add_argument("--json", action="store_true", dest="as_json")

    access = subparsers.add_parser("access", help="show documents allowed for a role")
    access.add_argument("--role", required=True)
    access.add_argument("--json", action="store_true", dest="as_json")
    return parser


def _emit(payload: dict[str, object], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for key, value in payload.items():
        print(f"{key}: {value}")


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        manifest = load_manifest(args.manifest)
        if args.command == "status":
            payload: dict[str, object] = {
                "project": "Grounded Knowledge Workbench",
                "maturity": "contract_ready",
                "validated_slice": "synthetic manifest and role filtering",
                "delivery_stage": "deterministic_foundation",
                **manifest.summary(),
            }
            _emit(payload, args.as_json)
            return 0

        allowed = manifest.accessible_documents(args.role)
        payload = {
            "role": args.role,
            "allowed_document_count": len(allowed),
            "documents": [
                {
                    "id": document.document_id,
                    "title": document.title,
                    "path": document.path.name,
                }
                for document in allowed
            ],
        }
        _emit(payload, args.as_json)
        return 0
    except ManifestError as exc:
        print(f"error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
