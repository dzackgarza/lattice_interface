from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import Genus, ZZ, matrix
from .conftest import assert_runtime_methods_covered


def test_genus_determinant_matches_input_gram_det():
    """
    method: determinant

    determinant() returns determinant of a representative Gram matrix.
    Assertion: Determinant equals det of the constructor matrix.
    """
    G = matrix(ZZ, [[2, 0], [0, 6]])
    g = Genus(G)
    actual = g.determinant()
    expected = G.det()
    assert actual == expected, f"Genus.determinant mismatch: actual={actual}, expected={expected}"


def test_genus_signature_pair_for_indefinite_example():
    """
    method: signature_pair

    signature_pair() returns (p,n) of any representative in the genus.
    Assertion: Indefinite diagonal input yields (1,1).
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, -2]]))
    actual = g.signature_pair()
    expected = (1, 1)
    assert actual == expected, f"Genus.signature_pair mismatch: actual={actual}, expected={expected}"


def test_genus_representative_preserves_dimension():
    """
    method: representative

    representative() returns an integer Gram matrix in the genus.
    Assertion: Returned representative has the documented genus dimension.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    R = g.representative()
    actual = R.nrows()
    expected = g.dimension()
    assert actual == expected, (
        f"Genus.representative dimension mismatch: actual={actual}, expected={expected}"
    )


def test_genus_rank_alias_matches_dimension():
    """
    method: rank

    rank() is an alias for genus dimension.
    Assertion: rank equals dimension on the same genus.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = g.rank()
    expected = g.dimension()
    assert actual == expected, f"Genus.rank mismatch: actual={actual}, expected={expected}"


def test_genus_local_symbols_nonempty_for_nonsingular_example():
    """
    method: local_symbols

    local_symbols() returns p-adic genus symbols at relevant primes.
    Assertion: Symbol list is nonempty for a nontrivial genus.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = len(g.local_symbols()) > 0
    expected = True
    assert actual == expected, f"Genus.local_symbols mismatch: actual={actual}, expected={expected}"


def test_genus_signature_is_difference_of_signature_pair():
    """
    method: signature

    signature() equals p-n for signature_pair()=(p,n).
    Assertion: Equality holds on an indefinite genus example.
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, -2]]))
    p, n = g.signature_pair()
    actual = g.signature()
    expected = p - n
    assert actual == expected, f"Genus.signature mismatch: actual={actual}, expected={expected}"


def test_genus_discriminant_form_cardinality_matches_abs_determinant():
    """
    method: discriminant_form

    discriminant_form() returns the finite discriminant module.
    Assertion: Cardinality equals absolute determinant in rank-1 example.
    """
    G = matrix(ZZ, [[2]])
    g = Genus(G)
    D = g.discriminant_form()
    actual = D.cardinality()
    expected = abs(G.det())
    assert actual == expected, (
        f"Genus.discriminant_form cardinality mismatch: actual={actual}, expected={expected}"
    )


def test_genus_direct_sum_dimension_adds():
    """
    method: direct_sum

    direct_sum(other) returns genus of orthogonal sum.
    Assertion: Dimension adds under direct sum.
    """
    g1 = Genus(matrix(ZZ, [[2]]))
    g2 = Genus(matrix(ZZ, [[4]]))
    gs = g1.direct_sum(g2)
    actual = gs.dimension()
    expected = g1.dimension() + g2.dimension()
    assert actual == expected, f"Genus.direct_sum dimension mismatch: actual={actual}, expected={expected}"


def test_genus_level_positive_integer():
    """
    method: level

    level() returns denominator of inverse Gram matrix representative.
    Assertion: Level is a positive integer.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = g.level()
    expected = actual > 0
    assert expected, f"Genus.level positivity mismatch: actual={actual}, expected=>0"


def test_genus_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant Genus runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.genera.genus",),
    )
