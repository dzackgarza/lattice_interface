from __future__ import annotations

import re
from pathlib import Path


TEST_FILES = [
    p
    for p in sorted(Path("tests/new_lattice_interface").glob("test_*.py"))
    if p.name not in {"test_quality_guardrails_static.py", "test_functionality_parity_static.py"}
]


def _file_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_no_content_free_nonemptiness_assertions():
    """method: quality_nonemptiness_guard"""
    banned = [
        r"assert\s+len\([^)]*\)\s*>\s*0",
        r"assert\s+len\([^)]*\)\s*>=\s*1",
        r"assert\s+bool\(",
    ]
    hits: list[str] = []
    for path in TEST_FILES:
        text = _file_text(path)
        for pattern in banned:
            if re.search(pattern, text):
                hits.append(f"{path}:{pattern}")
    assert not hits, f"Content-free non-emptiness assertions detected: hits={hits}"


def test_no_actual_expected_ceremony_wrapper_pattern():
    """method: quality_direct_assertion_guard"""
    hits: list[str] = []
    for path in TEST_FILES:
        text = _file_text(path)
        if re.search(r"\n\s*actual\s*=", text) and re.search(r"\n\s*expected\s*=", text):
            hits.append(str(path))
    assert not hits, f"Found actual/expected ceremony pattern in tests: hits={hits}"
