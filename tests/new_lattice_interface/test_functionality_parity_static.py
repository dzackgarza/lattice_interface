from __future__ import annotations

from pathlib import Path

from tests.new_lattice_interface.capability_mapping import (
    build_parity_rows,
    collect_method_tags,
)
from tests.new_lattice_interface.capability_registry import CAPABILITY_REGISTRY


LEGACY_GLOBS = [
    "tests/sage_doc/**/*.py",
    "tests/julia_doc/**/*.jl",
    "tests/julia_pytest/**/*.py",
    "tests/gap_doc/**/*.py",
]


def _legacy_paths() -> list[Path]:
    paths: list[Path] = []
    for pattern in LEGACY_GLOBS:
        paths.extend(Path(".").glob(pattern))
    return sorted(set(paths))


def test_legacy_method_union_maps_to_known_capabilities():
    """method: functionality_parity_map"""
    methods = collect_method_tags(_legacy_paths())
    rows = build_parity_rows(methods)
    unknown = sorted({row.capability for row in rows} - set(CAPABILITY_REGISTRY))
    assert not unknown, f"Methods mapped to unknown capabilities: unknown={unknown}"


def test_capability_mapping_covers_large_legacy_surface():
    """method: functionality_parity_size"""
    methods = collect_method_tags(_legacy_paths())
    assert len(methods) >= 600, (
        "Legacy method surface unexpectedly small; parity denominator changed: "
        f"legacy_method_count={len(methods)}"
    )
    rows = build_parity_rows(methods)
    assert len(rows) == len(methods), (
        f"Parity row cardinality mismatch: rows={len(rows)}, methods={len(methods)}"
    )


def test_parity_uses_nontrivial_capability_set():
    """method: functionality_parity_distribution"""
    methods = collect_method_tags(_legacy_paths())
    rows = build_parity_rows(methods)
    used_caps = {row.capability for row in rows}
    assert len(used_caps) >= 12, (
        "Too few capability buckets for legacy surface; taxonomy likely collapsed: "
        f"capabilities_used={len(used_caps)}, used={sorted(used_caps)}"
    )


def test_parity_uses_no_catch_all_capability():
    """method: functionality_parity_no_catchall"""
    methods = collect_method_tags(_legacy_paths())
    rows = build_parity_rows(methods)
    used_caps = {row.capability for row in rows}
    assert "legacy.general" not in used_caps, (
        "Catch-all capability must not be used for legacy parity mapping: "
        f"used={sorted(used_caps)}"
    )


def test_parity_uses_no_default_fallback_mapping():
    """method: functionality_parity_no_default_mapping"""
    methods = collect_method_tags(_legacy_paths())
    rows = build_parity_rows(methods)
    defaulted = sorted(row.method for row in rows if row.reason == "default")
    assert not defaulted, (
        "Every legacy method must be explicitly classified (exact or keyword), no default fallback: "
        f"defaulted={defaulted}"
    )
