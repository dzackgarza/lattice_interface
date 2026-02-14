from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import ZZ, matrix
from .conftest import assert_runtime_methods_covered


def test_matrix_lll_preserves_row_span_rank():
    """
    method: LLL

    Matrix.LLL() returns an LLL-reduced basis matrix of the row lattice.
    Assertion: Row-rank is preserved by reduction.
    """
    M = matrix(ZZ, [[4, 1], [1, 3]])
    R = M.LLL()
    actual = R.rank()
    expected = M.rank()
    assert actual == expected, f"Matrix.LLL rank mismatch: actual={actual}, expected={expected}"


def test_matrix_lll_gram_returns_unimodular_transform():
    """
    method: LLL_gram

    Matrix.LLL_gram() returns unimodular U with U^T G U reduced for Gram matrix G.
    Assertion: Returned transform has determinant ±1.
    """
    G = matrix(ZZ, [[4, 1], [1, 3]])
    U = G.LLL_gram()
    actual = abs(U.det())
    expected = 1
    assert actual == expected, f"Matrix.LLL_gram unimodularity mismatch: actual={actual}, expected={expected}"


def test_matrix_smith_form_diagonal_divisibility():
    """
    method: smith_form

    smith_form() returns diagonal invariant factors of an integer matrix.
    Assertion: Nonzero invariant factors satisfy divisibility d1 | d2.
    """
    M = matrix(ZZ, [[2, 4], [6, 8]])
    D, _, _ = M.smith_form()
    d1, d2 = D[0, 0], D[1, 1]
    actual_nonzero = d1 != 0
    expected_nonzero = True
    assert actual_nonzero == expected_nonzero, (
        f"Matrix.smith_form first invariant nonzero mismatch: actual={actual_nonzero}, expected={expected_nonzero}; d1={d1}"
    )
    actual_divides = (d2 % d1 == 0)
    expected_divides = True
    assert actual_divides == expected_divides, (
        f"Matrix.smith_form divisibility mismatch: actual={actual_divides}, expected={expected_divides}; d1={d1}, d2={d2}"
    )


def test_matrix_methods_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant Matrix runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = matrix(ZZ, [[2, 1], [1, 2]])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.matrix",),
    )
