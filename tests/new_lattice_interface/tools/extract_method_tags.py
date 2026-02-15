from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tests.new_lattice_interface.capability_mapping import extract_method_tags


DEFAULT_ROOTS = [
    "tests/sage_doc",
    "tests/julia_doc",
    "tests/julia_pytest",
    "tests/gap_doc",
    "tests/new_lattice_interface",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roots", nargs="*", default=DEFAULT_ROOTS)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    rows: list[str] = []
    for root in [Path(r) for r in args.roots]:
        for path in sorted(root.rglob("*")):
            if path.suffix not in {".py", ".jl"}:
                continue
            for tag in extract_method_tags(path):
                rows.append(f"{path}\t{tag}")

    content = "\n".join(rows) + ("\n" if rows else "")
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
