from __future__ import annotations

from tests.new_lattice_interface.types import DefiniteLattice, IndefiniteLattice


def _public_methods(cls: type) -> set[str]:
    return {name for name in dir(cls) if not name.startswith("_") and callable(getattr(cls, name))}


def test_definite_surface_excludes_indefinite_only_methods():
    """method: definite_surface_contract"""
    methods = _public_methods(DefiniteLattice)
    forbidden = sorted(
        {
            "is_indefinite",
            "witt_index",
            "has_isotropic_vector",
            "isotropic_vector",
            "primitive_isotropic_vectors",
            "isotropic_orbit_representatives",
            "vinberg",
            "reflection",
            "orthogonal_hyperplane",
        }
        & methods
    )
    assert not forbidden, f"Definite surface leaked indefinite-only methods: forbidden={forbidden}"


def test_indefinite_surface_excludes_definite_only_methods():
    """method: indefinite_surface_contract"""
    methods = _public_methods(IndefiniteLattice)
    forbidden = sorted({"minimum", "shortest_vector"} & methods)
    assert not forbidden, f"Indefinite surface leaked definite-only methods: forbidden={forbidden}"


def test_indefinite_surface_includes_core_indefinite_methods():
    """method: indefinite_surface_presence"""
    methods = _public_methods(IndefiniteLattice)
    required = {
        "is_indefinite",
        "witt_index",
        "has_isotropic_vector",
        "isotropic_vector",
        "primitive_isotropic_vectors",
        "isotropic_orbit_representatives",
    }
    missing = sorted(required - methods)
    assert not missing, f"Indefinite surface missing required methods: missing={missing}"
