from __future__ import annotations

from tests.new_lattice_interface.capability_registry import capabilities_by_domain
from tests.new_lattice_interface.types import DefiniteLattice, IndefiniteLattice, OrthogonalGroup


def _public_methods(cls: type) -> set[str]:
    return {name for name in dir(cls) if not name.startswith("_") and callable(getattr(cls, name))}


DEFINITE_METHOD_EXPECTATIONS = {
    "enumeration.minimum_kissing": {"minimum"},
    "enumeration.short_vectors": {"shortest_vector"},
}

INDEFINITE_METHOD_EXPECTATIONS = {
    "indefinite.witt": {"witt_index", "is_indefinite"},
    "indefinite.isotropic_vectors": {
        "has_isotropic_vector",
        "isotropic_vector",
        "primitive_isotropic_vectors",
        "isotropic_orbit_representatives",
    },
    "root.reflection": {"reflection"},
    "root.orthogonal_hyperplane": {"orthogonal_hyperplane"},
    "coxeter.vinberg": {"vinberg"},
}


def test_definite_domain_capabilities_have_definite_surface_methods():
    """method: capability_domain_definite_alignment"""
    methods = _public_methods(DefiniteLattice)
    missing: list[str] = []
    for capability in sorted(capabilities_by_domain("definite_only")):
        required = DEFINITE_METHOD_EXPECTATIONS.get(capability, set())
        if required and not required.issubset(methods):
            missing.append(f"{capability}:{sorted(required - methods)}")
    assert not missing, f"Definite domain capability/surface misalignment: missing={missing}"


def test_indefinite_domain_capabilities_have_indefinite_surface_methods():
    """method: capability_domain_indefinite_alignment"""
    methods = _public_methods(IndefiniteLattice)
    missing: list[str] = []
    for capability in sorted(capabilities_by_domain("indefinite_only")):
        required = INDEFINITE_METHOD_EXPECTATIONS.get(capability, set())
        if required and not required.issubset(methods):
            missing.append(f"{capability}:{sorted(required - methods)}")
    assert not missing, f"Indefinite domain capability/surface misalignment: missing={missing}"


def test_isometry_orbit_capability_aligns_with_group_surface():
    """method: capability_domain_isometry_alignment"""
    methods = _public_methods(OrthogonalGroup)
    required = {"orbit", "stabilizer", "same_orbit"}
    missing = sorted(required - methods)
    assert not missing, f"OrthogonalGroup missing orbit/stabilizer surface: missing={missing}"
