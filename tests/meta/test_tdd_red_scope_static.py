from __future__ import annotations

from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_PREFIX = Path("tests/new_lattice_interface")
MARKER_PATTERN = re.compile(
    r"(?m)^\s*(?:@pytest\.mark\.tdd_red|pytestmark\s*=\s*pytest\.mark\.tdd_red)\s*$"
)


def test_tdd_red_marker_scope_is_new_interface_only():
    """
    Policy contract:
    tdd_red markers are reserved for NEW interface-contract tests and must
    not appear in existing library/tool test suites.
    """
    offenders: list[str] = []
    for pyfile in REPO_ROOT.rglob("tests/**/*.py"):
        rel = pyfile.relative_to(REPO_ROOT)
        if rel == Path("tests/meta/test_tdd_red_scope_static.py"):
            continue
        text = pyfile.read_text(encoding="utf-8")
        if MARKER_PATTERN.search(text) is None:
            continue
        if not str(rel).startswith(str(ALLOWED_PREFIX)):
            offenders.append(str(rel))

    assert not offenders, (
        "tdd_red marker is out of allowed scope. "
        "Allowed scope: tests/new_lattice_interface/*.py\n"
        f"Found in: {sorted(offenders)}"
    )
