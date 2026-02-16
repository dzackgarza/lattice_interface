from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import Lattice, LatticeDiscriminantGroup, LatticeGenus


def test_lattice_in_genus_of_reflexive_and_alias_hyperbolic_plane():
    """
    method: in_genus_of

    Classification-query contract:
    genus membership must be reflexive and invariant under equal-model aliases of U.
    """
    u: Lattice = Lattice.U()
    h: Lattice = Lattice.H()
    assert_equal(u.in_genus_of(u), True, f"Genus relation must be reflexive: lattice={u}")
    assert_equal(u.in_genus_of(h), True, f"U and H aliases should be in same genus: U={u}, H={h}")


def test_lattice_in_genus_of_detects_signature_obstruction():
    """
    method: in_genus_of

    Classification-query contract:
    lattices with different signatures cannot lie in the same genus.
    """
    u: Lattice = Lattice.U()
    e8: Lattice = Lattice.E(8)
    assert_equal(
        u.in_genus_of(e8),
        False,
        f"Different signatures should obstruct genus equality: U.sig={u.signature()}, E8.sig={e8.signature()}",
    )


def test_discriminant_form_exists_even_lattice_for_small_unimodular_examples():
    """
    method: exists_even_lattice

    Existence-query contract:
    for trivial discriminant form, even lattice existence agrees with small known examples:
    U exists at (1,1), while odd signature difference case (2,1) is rejected.
    """
    a_u: LatticeDiscriminantGroup = Lattice.U().discriminant()
    assert_equal(
        a_u.exists_even_lattice(t_plus=1, t_minus=1),
        True,
        "Trivial discriminant form should admit the known even lattice U of signature (1,1)",
    )
    assert_equal(
        a_u.exists_even_lattice(t_plus=2, t_minus=1),
        False,
        "Trivial discriminant form should reject incompatible odd signature-difference example (2,1)",
    )


def test_lattice_class_number_for_u_is_one():
    """
    method: class_number

    Classification-query contract:
    in this small interface example, U has single class in its genus.
    """
    u: Lattice = Lattice.U()
    assert_equal(u.class_number(), 1, f"Expected class_number(U)=1 in contract example, got {u.class_number()}")


def test_lattice_is_unique_in_genus_for_u():
    """
    method: is_unique_in_genus

    Classification-query contract:
    uniqueness predicate agrees with class-number one on U.
    """
    u: Lattice = Lattice.U()
    assert_equal(u.is_unique_in_genus(), True, f"Expected U to be unique in genus in contract example: U={u}")


def test_lattice_genus_object_exposes_classification_invariants():
    """
    method: genus

    Genus-object contract:
    `L.genus()` exposes signature, discriminant form, membership, and class-number answers.
    """
    u: Lattice = Lattice.U()
    g: LatticeGenus = u.genus()
    a_u: LatticeDiscriminantGroup = u.discriminant()
    a_g: LatticeDiscriminantGroup = g.discriminant_form()

    assert_equal(g.signature(), (1, 1), f"Genus signature mismatch for U: got {g.signature()}")
    assert_equal(g.contains(u), True, f"Genus must contain its defining lattice: genus={g}, lattice={u}")
    assert_equal(g.class_number(), 1, f"Expected class number 1 for contract genus of U: genus={g}")
    assert_equal(g.is_single_class(), True, f"Single-class predicate mismatch for contract genus of U: genus={g}")
    assert_equal(
        a_g.is_isomorphic(a_u),
        True,
        "Genus discriminant form should match lattice discriminant form up to isomorphism",
    )


def test_discriminant_form_invariants_support_classification_queries():
    """
    method: minimal_number_of_generators

    Invariant contract:
    discriminant-form helper invariants used by classification queries are explicitly available.
    """
    a_u: LatticeDiscriminantGroup = Lattice.U().discriminant()
    assert_equal(
        a_u.minimal_number_of_generators(),
        0,
        "Trivial discriminant form of U should have generator length 0",
    )
    assert_equal(
        a_u.minimal_number_of_generators(prime=2),
        0,
        "2-primary generator length should be 0 for trivial discriminant form",
    )


def test_discriminant_form_signature_mod_8_for_u():
    """
    method: signature_mod_8

    Invariant contract:
    trivial discriminant form in the U example reports signature congruence class 0 mod 8.
    """
    a_u: LatticeDiscriminantGroup = Lattice.U().discriminant()
    assert_equal(a_u.signature_mod_8(), 0, "Expected signature_mod_8=0 for U contract discriminant form")


def test_discriminant_form_isomorphism_small_examples():
    """
    method: is_isomorphic

    Invariant contract:
    discriminant-form isomorphism recognizes identical trivial forms and rejects A2-vs-U mismatch.
    """
    a_u: LatticeDiscriminantGroup = Lattice.U().discriminant()
    a_h: LatticeDiscriminantGroup = Lattice.H().discriminant()
    a_a2: LatticeDiscriminantGroup = Lattice.A(2).discriminant()

    assert_equal(a_u.is_isomorphic(a_h), True, "U and H should have isomorphic trivial discriminant forms")
    assert_equal(
        a_u.is_isomorphic(a_a2),
        False,
        "U trivial discriminant form should not be isomorphic to nontrivial A2 discriminant form",
    )
