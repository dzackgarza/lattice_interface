from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import BinaryQF
from .conftest import assert_runtime_methods_covered


def test_binaryqf_discriminant_formula():
    """
    method: discriminant

    discriminant() returns D=b^2-4ac for ax^2+bxy+cy^2.
    Assertion: Computed value matches the exact defining formula.
    """
    Q = BinaryQF(1, 2, 3)
    actual = Q.discriminant()
    expected = 2 * 2 - 4 * 1 * 3
    assert actual == expected, f"BinaryQF.discriminant mismatch: actual={actual}, expected={expected}"


def test_binaryqf_determinant_relation_to_discriminant():
    """
    method: determinant

    determinant()/det() returns det(Gram)=-D/4.
    Assertion: Determinant equals -discriminant/4 on a concrete form.
    """
    Q = BinaryQF(1, -1, 67)
    actual = Q.determinant()
    expected = -Q.discriminant() / 4
    assert actual == expected, f"BinaryQF.determinant mismatch: actual={actual}, expected={expected}"


def test_binaryqf_positive_definite_criterion_example():
    """
    method: is_positive_definite

    is_positive_definite() uses classical binary criteria D<0 and a>0.
    Assertion: x^2+y^2 is detected as positive definite.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_positive_definite()
    expected = True
    assert actual is expected, (
        f"BinaryQF.is_positive_definite mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_reduced_form_preserves_discriminant():
    """
    method: reduced_form

    reduced_form() returns an equivalent reduced binary form.
    Assertion: Discriminant is invariant under reduction.
    """
    Q = BinaryQF(5, 7, 3)
    R = Q.reduced_form()
    actual = R.discriminant()
    expected = Q.discriminant()
    assert actual == expected, (
        f"BinaryQF.reduced_form discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_content_matches_coefficient_gcd():
    """
    method: content

    content() returns gcd(a,b,c) for BinaryQF(a,b,c).
    Assertion: Content equals gcd(2,4,6)=2.
    """
    Q = BinaryQF(2, 4, 6)
    actual = Q.content()
    expected = 2
    assert actual == expected, f"BinaryQF.content mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_primitive_detects_unit_content():
    """
    method: is_primitive

    is_primitive() checks whether gcd(a,b,c)=1.
    Assertion: Form (1,2,3) is primitive.
    """
    Q = BinaryQF(1, 2, 3)
    actual = Q.is_primitive()
    expected = True
    assert actual == expected, f"BinaryQF.is_primitive mismatch: actual={actual}, expected={expected}"


def test_binaryqf_polynomial_roundtrip_constructor():
    """
    method: from_polynomial

    from_polynomial(f) reconstructs the binary form from a bivariate polynomial.
    Assertion: Roundtrip preserves the discriminant.
    """
    Q = BinaryQF(3, -2, 5)
    R = BinaryQF.from_polynomial(Q.polynomial())
    actual = R.discriminant()
    expected = Q.discriminant()
    assert actual == expected, (
        f"BinaryQF.from_polynomial roundtrip mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_is_reduced_on_simple_posdef_example():
    """
    method: is_reduced

    is_reduced() checks Gauss reduction conditions.
    Assertion: x^2+y^2 is reduced.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_reduced()
    expected = True
    assert actual == expected, f"BinaryQF.is_reduced mismatch: actual={actual}, expected={expected}"


def test_binaryqf_principal_has_requested_discriminant():
    """
    method: principal

    principal(D) returns the principal form of discriminant D.
    Assertion: Resulting form has discriminant -4.
    """
    Q = BinaryQF.principal(-4)
    actual = Q.discriminant()
    expected = -4
    assert actual == expected, (
        f"BinaryQF.principal discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant BinaryQF runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = BinaryQF(5, 7, 3)
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.binary_qf",),
    )
