from __future__ import annotations

import ast
from pathlib import Path

from tests.new_lattice_interface.capability_mapping import (
    build_parity_rows,
    collect_method_tags,
)
from tests.new_lattice_interface.capability_registry import CAPABILITY_REGISTRY


def _new_interface_tests() -> list[Path]:
    return sorted(Path("tests/new_lattice_interface").glob("test_*.py"))


def _test_functions(path: Path) -> list[ast.FunctionDef]:
    module = ast.parse(path.read_text(encoding="utf-8"))
    return [n for n in module.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]


def test_every_new_interface_test_has_method_tag():
    """method: capability_tag_presence"""
    missing: list[str] = []
    for path in _new_interface_tests():
        for fn in _test_functions(path):
            doc = ast.get_docstring(fn) or ""
            if "method:" not in doc:
                missing.append(f"{path}:{fn.lineno}:{fn.name}")
    assert not missing, f"Missing method tags in new interface tests: missing={missing}"


def test_required_capabilities_have_contract_tests():
    """method: capability_contract_coverage"""
    methods = collect_method_tags(_new_interface_tests())
    used_caps = {row.capability for row in build_parity_rows(methods)}
    required = {
        "constructor.from_gram",
        "constructor.root",
        "constructor.hyperbolic",
        "element.norm",
        "enumeration.minimum_kissing",
        "enumeration.short_vectors",
        "indefinite.isotropic_vectors",
        "indefinite.witt",
        "isometry.orbits_stabilizers",
        "substructure.sublattice",
        "substructure.quotient",
        "substructure.dual",
        "discriminant.forms",
        "coxeter.vinberg",
        "root_system.isomorphism",
    }
    missing = sorted(required - used_caps)
    assert not missing, f"Required capabilities missing contract tests: missing={missing}"


def test_new_interface_capability_map_uses_known_registry_ids():
    """method: capability_contract_registry_consistency"""
    methods = collect_method_tags(_new_interface_tests())
    used_caps = {row.capability for row in build_parity_rows(methods)}
    unknown = sorted(used_caps - set(CAPABILITY_REGISTRY))
    assert not unknown, f"New interface tests mapped to unknown capabilities: unknown={unknown}"
