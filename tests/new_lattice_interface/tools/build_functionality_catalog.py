from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tests.new_lattice_interface.capability_mapping import (
    build_parity_rows,
    collect_method_tags,
)
from tests.new_lattice_interface.capability_registry import CAPABILITY_REGISTRY


DEFAULT_GLOBS = [
    "tests/sage_doc/**/*.py",
    "tests/julia_doc/**/*.jl",
    "tests/julia_pytest/**/*.py",
    "tests/gap_doc/**/*.py",
]


def _discover_methods(globs: list[str]) -> set[str]:
    methods: set[str] = set()
    for pattern in globs:
        paths = [Path(p) for p in sorted(Path(".").glob(pattern))]
        methods.update(collect_method_tags(paths))
    return methods


def _render(rows) -> str:
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        grouped[row.capability].append(row.method)

    lines: list[str] = []
    lines.append("# Legacy Functionality Catalog")
    lines.append("")
    lines.append("Generated from existing documented test surfaces.")
    lines.append("")
    lines.append(f"Total mapped legacy methods: {len(rows)}")
    lines.append(f"Total capabilities used: {len(grouped)}")
    reason_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        reason_counts[row.reason] += 1
    lines.append(
        "Mapping reasons: "
        + ", ".join(f"{k}={reason_counts[k]}" for k in sorted(reason_counts))
    )
    lines.append("")
    for capability in sorted(grouped):
        spec = CAPABILITY_REGISTRY[capability]
        lines.append(f"## `{capability}`")
        lines.append(f"- Domain: `{spec.domain}`")
        lines.append(f"- Description: {spec.description}")
        lines.append("- Legacy methods:")
        for method in sorted(grouped[capability]):
            row = next(r for r in rows if r.capability == capability and r.method == method)
            lines.append(f"  - `{method}` ({row.reason})")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--globs", nargs="*", default=DEFAULT_GLOBS)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("tests/new_lattice_interface/docs/legacy_functionality_catalog.md"),
    )
    args = parser.parse_args()

    methods = _discover_methods(args.globs)
    rows = build_parity_rows(methods)
    content = _render(rows)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(content + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({len(rows)} methods)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
