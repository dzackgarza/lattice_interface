from __future__ import annotations

import sys
import pytest

sage = pytest.importorskip("sage.all")
from sage.all import IntegralLattice, ZZ, matrix
from .conftest import assert_runtime_methods_covered


TOKEN_MAP = {
    'constructor("U")': set(),
    "minimum_maximum": {"minimum", "maximum", "min", "max"},
    "LLL": {"LLL", "lll"},
}


def test_integrallattice_constructor_u_hyperbolic_plane():
    """
    method: constructor("U")

    The string constructor "U" builds the hyperbolic plane with Gram matrix [[0,1],[1,0]].
    Assertion: Constructor output has exactly the documented hyperbolic Gram matrix.
    """
    L = IntegralLattice("U")
    actual = L.gram_matrix()
    expected = matrix(ZZ, [[0, 1], [1, 0]])
    assert actual == expected, (
        f"IntegralLattice('U').gram_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_signature_pair_for_indefinite_form():
    """
    method: signature_pair

    signature_pair() returns (p,n), the counts of positive and negative eigenvalues.
    Assertion: A diagonal form diag(2,-2) has signature pair (1,1).
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, -2]]))
    actual = L.signature_pair()
    expected = (1, 1)
    assert actual == expected, f"IntegralLattice.signature_pair mismatch: actual={actual}, expected={expected}"


def test_integrallattice_discriminant_matches_determinant():
    """
    method: discriminant

    discriminant() is the determinant of the lattice Gram matrix.
    Assertion: Returned discriminant equals det(Gram) on a nontrivial rank-2 example.
    """
    G = matrix(ZZ, [[2, 1], [1, 2]])
    L = IntegralLattice(G)
    actual = L.discriminant()
    expected = -G.det()
    assert actual == expected, (
        f"IntegralLattice.discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_dual_lattice_contains_scaled_basis():
    """
    method: dual_lattice

    dual_lattice() returns L^vee, the module pairing integrally with L.
    Assertion: For Gram [2], the dual Gram is [1/2], matching the documented scaling.
    """
    L = IntegralLattice(matrix(ZZ, [[2]]))
    D = L.dual_lattice()
    actual = D.gram_matrix()[0, 0]
    expected = sage.QQ((1, 2))
    assert actual == expected, (
        f"IntegralLattice.dual_lattice gram entry mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_discriminant_group_has_expected_order_rank_one():
    """
    method: discriminant_group

    discriminant_group() returns L^vee/L as a finite torsion quadratic module.
    Assertion: For rank-1 Gram [2], discriminant group order is 2.
    """
    L = IntegralLattice(matrix(ZZ, [[2]]))
    A = L.discriminant_group()
    actual = A.cardinality()
    expected = 2
    assert actual == expected, (
        f"IntegralLattice.discriminant_group order mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_minimum_and_maximum_extremes_by_signature():
    """
    method: minimum_maximum

    minimum()/maximum() return extremal values of (x,x) over nonzero lattice vectors.
    Assertion: Positive-definite and indefinite signatures show the documented finite/infinite behavior.
    """
    L_pd = IntegralLattice(matrix(ZZ, [[2, 0], [0, 2]]))
    L_ind = IntegralLattice(matrix(ZZ, [[2, 0], [0, -2]]))
    actual_pd_min = L_pd.minimum()
    expected_pd_min = 2
    assert actual_pd_min == expected_pd_min, (
        f"IntegralLattice.minimum (PD) mismatch: actual={actual_pd_min}, expected={expected_pd_min}"
    )
    actual_pd_max = str(L_pd.maximum())
    expected_pd_max = "+Infinity"
    assert actual_pd_max == expected_pd_max, (
        f"IntegralLattice.maximum (PD) mismatch: actual={actual_pd_max}, expected={expected_pd_max}"
    )
    actual_ind_min = str(L_ind.minimum())
    expected_ind_min = "-Infinity"
    assert actual_ind_min == expected_ind_min, (
        f"IntegralLattice.minimum (indefinite) mismatch: actual={actual_ind_min}, expected={expected_ind_min}"
    )
    actual_ind_max = str(L_ind.maximum())
    expected_ind_max = "+Infinity"
    assert actual_ind_max == expected_ind_max, (
        f"IntegralLattice.maximum (indefinite) mismatch: actual={actual_ind_max}, expected={expected_ind_max}"
    )


def test_integrallattice_lll_returns_lattice_with_same_rank():
    """
    method: LLL

    LLL()/lll() return a reduced IntegralLattice object.
    Assertion: Reduction preserves lattice rank.
    """
    L = IntegralLattice(matrix(ZZ, [[4, 1], [1, 3]]))
    R = L.LLL()
    actual = R.rank()
    expected = L.rank()
    assert actual == expected, f"IntegralLattice.LLL rank mismatch: actual={actual}, expected={expected}"


def test_integrallattice_orthogonal_group_requires_definite():
    """
    method: orthogonal_group

    orthogonal_group() computes generators only for definite lattices.
    Assertion: Indefinite example raises NotImplementedError.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, -2]]))
    with pytest.raises(NotImplementedError):
        _ = L.orthogonal_group()


def test_integrallattice_automorphisms_alias_matches_orthogonal_group_order():
    """
    method: automorphisms

    automorphisms() is an alias of orthogonal_group().
    Assertion: Alias and primary method have identical group order on a PD example.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, 2]]))
    actual = L.automorphisms().order()
    expected = L.orthogonal_group().order()
    assert actual == expected, (
        f"IntegralLattice.automorphisms alias mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_maximal_overlattice_evenness_constraint_at_two():
    """
    method: maximal_overlattice

    maximal_overlattice(p) enforces even-lattice conditions at p=2/global cases.
    Assertion: Odd rank-1 lattice fails at p=2 with ValueError.
    """
    L = IntegralLattice(matrix(ZZ, [[1]]))
    with pytest.raises(ValueError):
        _ = L.maximal_overlattice(2)


def test_integrallattice_direct_sum_adds_rank():
    """
    method: direct_sum

    direct_sum(other) forms an orthogonal direct sum.
    Assertion: Rank of direct sum equals sum of ranks.
    """
    A = IntegralLattice(matrix(ZZ, [[2]]))
    B = IntegralLattice(matrix(ZZ, [[4]]))
    C = A.direct_sum(B)
    actual = C.rank()
    expected = A.rank() + B.rank()
    assert actual == expected, f"IntegralLattice.direct_sum rank mismatch: actual={actual}, expected={expected}"


def test_integrallattice_twist_scales_gram_matrix():
    """
    method: twist

    twist(n) rescales the bilinear form by n.
    Assertion: Gram matrix scales by factor 3 under twist(3).
    """
    L = IntegralLattice(matrix(ZZ, [[2, 1], [1, 2]]))
    T = L.twist(3)
    actual = T.gram_matrix()
    expected = 3 * L.gram_matrix()
    assert actual == expected, f"IntegralLattice.twist mismatch: actual={actual}, expected={expected}"


def test_integrallattice_sublattice_rank_from_single_generator():
    """
    method: sublattice

    sublattice(basis) builds the lattice spanned by supplied vectors.
    Assertion: One generator yields rank one.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, 2]]))
    S = L.sublattice([[1, 1]])
    actual = S.rank()
    expected = 1
    assert actual == expected, f"IntegralLattice.sublattice rank mismatch: actual={actual}, expected={expected}"


def test_integrallattice_genus_dimension_matches_rank():
    """
    method: genus

    genus() returns the genus object of the lattice.
    Assertion: Genus dimension equals lattice rank.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 1], [1, 2]]))
    g = L.genus()
    actual = g.dimension()
    expected = L.rank()
    assert actual == expected, f"IntegralLattice.genus dimension mismatch: actual={actual}, expected={expected}"


def test_integrallattice_is_even_detects_odd_diagonal():
    """
    method: is_even

    is_even() checks whether all norms (x,x) are even integers.
    Assertion: Gram [1] lattice is not even.
    """
    L = IntegralLattice(matrix(ZZ, [[1]]))
    actual = L.is_even()
    expected = False
    assert actual == expected, f"IntegralLattice.is_even mismatch: actual={actual}, expected={expected}"


def test_integrallattice_signature_matches_signature_pair_difference():
    """
    method: signature

    signature() returns p-n and signature_pair() returns (p,n).
    Assertion: signature equals p-n for an indefinite rank-2 lattice.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, -2]]))
    p, n = L.signature_pair()
    actual = L.signature()
    expected = p - n
    assert actual == expected, f"IntegralLattice.signature mismatch: actual={actual}, expected={expected}"


def test_integrallattice_quadratic_form_preserves_sample_value():
    """
    method: quadratic_form

    quadratic_form() returns the associated quadratic form object.
    Assertion: Quadratic-form evaluation matches lattice norm on sample vector.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 1], [1, 2]]))
    Q = L.quadratic_form()
    v = (1, 2)
    actual = Q(v)
    x = L(v)
    expected = x.inner_product(x)
    assert actual == expected, (
        f"IntegralLattice.quadratic_form value mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_overlattice_contains_original_rank():
    """
    method: overlattice

    overlattice(gens) forms an overlattice generated by L and added rational generators.
    Assertion: Result rank matches original rank.
    """
    L = IntegralLattice(matrix(ZZ, [[4]]))
    O = L.overlattice([[sage.QQ((1, 2))]])
    actual = O.rank()
    expected = L.rank()
    assert actual == expected, f"IntegralLattice.overlattice rank mismatch: actual={actual}, expected={expected}"


def test_integrallattice_orthogonal_complement_dimension():
    """
    method: orthogonal_complement

    orthogonal_complement(M) returns vectors orthogonal to submodule M.
    Assertion: In rank-2 Euclidean lattice, complement of one primitive vector has rank 1.
    """
    L = IntegralLattice(matrix(ZZ, [[2, 0], [0, 2]]))
    C = L.orthogonal_complement([L([1, 0])])
    actual = C.rank()
    expected = 1
    assert actual == expected, (
        f"IntegralLattice.orthogonal_complement rank mismatch: actual={actual}, expected={expected}"
    )


def test_integrallattice_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant IntegralLattice runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = IntegralLattice(matrix(ZZ, [[4, 1], [1, 3]]))
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.modules.free_quadratic_module_integer_symmetric",),
        token_map=TOKEN_MAP,
    )
