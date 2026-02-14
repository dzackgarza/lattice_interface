from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import QQ, ZZ, QuadraticForm, vector
from .conftest import assert_runtime_methods_covered


TOKEN_MAP = {
    "Gram_matrix_matrix": {"Gram_matrix", "matrix", "Hessian_matrix"},
    "discriminant_Gram_det": {"det", "Gram_det"},
}


def test_quadraticform_gram_and_hessian_relation():
    """
    method: Gram_matrix_matrix

    matrix() is the Hessian A and Gram_matrix() is G=A/2 for Q(x)=x^T G x.
    Assertion: Hessian equals two times Gram matrix on a nontrivial binary form.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.matrix()
    expected = 2 * Q.Gram_matrix()
    assert actual == expected, (
        f"QuadraticForm matrix/Gram relation mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_discriminant_equals_gram_det():
    """
    method: discriminant_Gram_det

    det() is the Hessian determinant and Gram_det() is the Gram determinant.
    Assertion: Determinant invariants coincide exactly.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.det()
    expected = 2 ** Q.dim() * Q.Gram_det()
    assert actual == expected, (
        f"QuadraticForm det/Gram_det mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_signature_vector_counts_eigenvalue_signs():
    """
    method: signature_vector

    signature_vector() returns (p,n,z), counts of positive/negative/zero eigenvalues.
    Assertion: Form x^2-y^2 has signature vector (1,1,0).
    """
    Q = QuadraticForm(ZZ, 2, [1, 0, -1])
    actual = Q.signature_vector()
    expected = (1, 1, 0)
    assert actual == expected, (
        f"QuadraticForm.signature_vector mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_bilinear_map_polarization_identity():
    """
    method: bilinear_map

    bilinear_map(v,w) is the polarization B(v,w)=(Q(v+w)-Q(v)-Q(w))/2.
    Assertion: Polarization identity gives B(v,v)=Q(v).
    """
    Q = QuadraticForm(ZZ, 2, [2, 0, 2])
    v = vector(ZZ, [1, 2])
    actual = Q.bilinear_map(v, v)
    expected = Q(v)
    assert actual == expected, (
        f"QuadraticForm.bilinear_map polarization mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_theta_series_leading_coefficient_one():
    """
    method: theta_series

    theta_series(prec) counts representation numbers with constant term from the zero vector.
    Assertion: Constant coefficient is exactly 1.
    """
    Q = QuadraticForm(ZZ, 2, [1, 0, 1])
    t = Q.theta_series(6)
    actual = t[0]
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.theta_series constant term mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_rational_diagonal_form_preserves_rank():
    """
    method: rational_diagonal_form

    rational_diagonal_form() diagonalizes over Q without changing rational isometry class.
    Assertion: Rank is preserved under rational diagonalization.
    """
    Q = QuadraticForm(QQ, 3, [2, 0, 0, 3, 0, 5])
    D = Q.rational_diagonal_form()
    actual = D.dim()
    expected = Q.dim()
    assert actual == expected, (
        f"QuadraticForm.rational_diagonal_form rank mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant QuadraticForm runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms",),
        token_map=TOKEN_MAP,
    )
