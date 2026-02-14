from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import IntegralLattice, ZZ, matrix
from .conftest import assert_runtime_methods_covered


def _disc_module():
    L = IntegralLattice(matrix(ZZ, [[2]]))
    return L.discriminant_group()


def test_tqm_cardinality_matches_rank_one_discriminant():
    """
    method: cardinality

    cardinality() is the order of the finite discriminant module.
    Assertion: Rank-1 lattice with Gram [2] yields discriminant-module order 2.
    """
    T = _disc_module()
    actual = T.cardinality()
    expected = 2
    assert actual == expected, (
        f"TorsionQuadraticModule.cardinality mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_invariants_rank_one_even_lattice():
    """
    method: invariants

    invariants() returns finite abelian invariants of the module.
    Assertion: Rank-1 Gram [2] gives cyclic invariant tuple (2,).
    """
    T = _disc_module()
    actual = T.invariants()
    expected = (2,)
    assert actual == expected, (
        f"TorsionQuadraticModule.invariants mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_twist_multiplies_quadratic_values():
    """
    method: twist

    twist(c) rescales bilinear and quadratic forms by c on the same underlying group.
    Assertion: Generator quadratic value doubles after twist(2).
    """
    T = _disc_module()
    x = T.gens()[0]
    q0 = x.q()
    T2 = T.twist(2)
    x2 = T2.gens()[0]
    actual = x2.q()
    expected = 2 * q0
    assert actual == expected, (
        f"TorsionQuadraticModule.twist quadratic value mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_gens_nonempty_for_nontrivial_discriminant_group():
    """
    method: gens

    gens() returns a generating set for the finite module.
    Assertion: Rank-1 discriminant group has at least one generator.
    """
    T = _disc_module()
    actual = len(T.gens()) > 0
    expected = True
    assert actual == expected, f"TorsionQuadraticModule.gens mismatch: actual={actual}, expected={expected}"


def test_tqm_gram_matrix_bilinear_is_square():
    """
    method: gram_matrix_bilinear

    gram_matrix_bilinear() returns the bilinear pairing matrix on generators.
    Assertion: Returned matrix is square of size number_of_generators.
    """
    T = _disc_module()
    G = T.gram_matrix_bilinear()
    n = len(T.gens())
    actual = (G.nrows(), G.ncols())
    expected = (n, n)
    assert actual == expected, (
        f"TorsionQuadraticModule.gram_matrix_bilinear shape mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_gram_matrix_quadratic_has_same_shape_as_bilinear():
    """
    method: gram_matrix_quadratic

    gram_matrix_quadratic() returns quadratic-form matrix in the same generator basis.
    Assertion: Quadratic and bilinear Gram matrices have the same shape.
    """
    T = _disc_module()
    A = T.gram_matrix_bilinear()
    Q = T.gram_matrix_quadratic()
    actual = (Q.nrows(), Q.ncols())
    expected = (A.nrows(), A.ncols())
    assert actual == expected, (
        f"TorsionQuadraticModule.gram_matrix_quadratic shape mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_value_modules_are_defined():
    """
    method: value_module

    value_module() and value_module_qf() expose codomains for bilinear/quadratic values.
    Assertion: Both codomain objects are non-None.
    """
    T = _disc_module()
    bil = T.value_module()
    qf = T.value_module_qf()
    actual = (bil is not None, qf is not None)
    expected = (True, True)
    assert actual == expected, (
        f"TorsionQuadraticModule value modules mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_primary_part_of_two_group_is_itself():
    """
    method: primary_part

    primary_part(s) extracts the s-primary component.
    Assertion: For a 2-group discriminant module, 2-primary part has same cardinality.
    """
    T = _disc_module()
    P = T.primary_part(2)
    actual = P.cardinality()
    expected = T.cardinality()
    assert actual == expected, (
        f"TorsionQuadraticModule.primary_part mismatch: actual={actual}, expected={expected}"
    )


def test_torsionquadraticmodule_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant TorsionQuadraticModule runtime
    method should correspond to at least one explicit test method tag.
    """
    sample = _disc_module()
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.modules.torsion_quadratic_module",),
    )
