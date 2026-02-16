from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    DiscriminantOrthogonalGroup,
    Lattice,
    LatticeDiscriminantGroup,
    LatticeElement,
    LatticeOrthogonalSubgroup,
    OrthogonalGroup,
    StableOrthogonalGroup,
)


def test_lattice_group_accessors_have_explicit_types():
    """
    method: stable_orthogonal_group

    Group-accessor contract:
    lattice exposes O(L), O^+(L), and O(A_L) with explicitly typed accessors.
    """
    lattice: Lattice = Lattice.U()
    full_group: OrthogonalGroup = lattice.orthogonal_group()
    stable_group: StableOrthogonalGroup = lattice.stable_orthogonal_group()
    discr_group: DiscriminantOrthogonalGroup = lattice.discriminant_orthogonal_group()
    discr_data: LatticeDiscriminantGroup = lattice.discriminant()
    discr_group_from_discriminant: DiscriminantOrthogonalGroup = discr_data.orthogonal_group()

    assert_equal(
        discr_group == discr_group_from_discriminant,
        True,
        "Lattice.discriminant_orthogonal_group should match L.discriminant().orthogonal_group()",
    )
    assert_equal(
        full_group.contains(full_group.identity()),
        True,
        "Orthogonal group should contain identity isometry",
    )
    assert_equal(
        stable_group.contains(full_group.identity()),
        True,
        "Stable orthogonal group should contain identity isometry",
    )


def test_lattice_set_stabilizer_accessor_with_optional_subgroup():
    """
    method: orthogonal_set_stabilizer

    Stabilizer contract:
    lattice-level set stabilizer accepts optional subgroup and returns subgroup of O(L).
    """
    lattice: Lattice = Lattice.U()
    e1: LatticeElement = lattice.element((1, 0))
    e2: LatticeElement = lattice.element((0, 1))
    vectors: tuple[LatticeElement, LatticeElement] = (e1, e2)
    stable_group: StableOrthogonalGroup = lattice.stable_orthogonal_group()

    stabilizer_default: LatticeOrthogonalSubgroup = lattice.orthogonal_set_stabilizer(vectors)
    stabilizer_stable: LatticeOrthogonalSubgroup = lattice.orthogonal_set_stabilizer(vectors, subgroup=stable_group)

    identity = lattice.orthogonal_group().identity()
    assert_equal(
        stabilizer_default.contains(identity),
        True,
        "Default set stabilizer should contain identity",
    )
    assert_equal(
        stabilizer_stable.contains(identity),
        True,
        "Subgroup-restricted set stabilizer should contain identity",
    )


def test_orthogonal_group_set_stabilizer_accessor_with_typed_vectors():
    """
    method: stabilizer_of_set

    Stabilizer contract:
    group-level set stabilizer accepts typed vector collections and returns a subgroup object.
    """
    lattice: Lattice = Lattice.U()
    group: OrthogonalGroup = lattice.orthogonal_group()
    vectors: list[LatticeElement] = [lattice.element((1, 0)), lattice.element((0, 1))]

    stabilizer: LatticeOrthogonalSubgroup = group.stabilizer_of_set(vectors)
    assert_equal(
        stabilizer.contains(group.identity()),
        True,
        "OrthogonalGroup.stabilizer_of_set should contain identity",
    )
