from __future__ import annotations

import inspect
from types import ModuleType

import pytest

import sage.all  # noqa: F401
from sage.all import libgap


def _method_token_from_docstring(func) -> str | None:
    doc = inspect.getdoc(func) or ""
    for line in doc.splitlines():
        line = line.strip()
        if line.startswith("method:"):
            return line.split(":", 1)[1].strip()
    return None


def covered_methods_from_module(module: ModuleType) -> set[str]:
    covered: set[str] = set()
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if not name.startswith("test_") or name.endswith("_coverage"):
            continue
        token = _method_token_from_docstring(func)
        if token is None:
            continue
        covered.add(token)
    return covered


def gap_bound_methods(method_names: set[str]) -> set[str]:
    bound: set[str] = set()
    for name in method_names:
        if bool(libgap.eval(f'IsBoundGlobal("{name}")')):
            bound.add(name)
    return bound


def assert_gap_methods_covered(
    *,
    test_module: ModuleType,
    method_names: set[str],
) -> None:
    covered = covered_methods_from_module(test_module)
    relevant = gap_bound_methods(method_names)
    missing = sorted(relevant - covered)
    if missing:
        msg = [
            "Coverage failure: uncovered relevant GAP methods found.",
            f"Relevant GAP methods count: {len(relevant)}",
            f"Covered GAP methods count: {len(covered)}",
            f"Uncovered GAP methods count: {len(missing)}",
            "Uncovered GAP methods:",
            *[f"- {name}" for name in missing],
        ]
        raise AssertionError("\n".join(msg))

