from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import NumberField, QQ, ZZ, matrix
from .conftest import assert_runtime_methods_covered


TOKEN_MAP = {
    "integral_basis_trace_gram": {"integral_basis", "discriminant"},
}


def test_numberfield_trace_gram_matches_discriminant():
    """
    method: integral_basis_trace_gram

    The trace-pairing Gram matrix on an integral basis has determinant equal to field discriminant.
    Assertion: Exact trace Gram determinant equals K.discriminant().
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    B = K.integral_basis()
    n = K.degree()
    G = matrix(QQ, n, n, lambda i, j: (B[i] * B[j]).trace())
    actual = G.det()
    expected = K.discriminant()
    assert actual == expected, (
        f"NumberField trace Gram determinant mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_ideal_free_module_has_expected_rank():
    """
    method: free_module

    free_module() returns the underlying free Z-module of an ideal.
    Assertion: Free-module rank equals ambient number-field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    OK = K.ring_of_integers()
    I = OK.ideal(2)
    F = I.free_module()
    actual = F.rank()
    expected = K.degree()
    assert actual == expected, (
        f"NumberFieldFractionalIdeal.free_module rank mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_signature_matches_quadratic_real_field():
    """
    method: signature

    signature() returns (r,s) for real and complex embeddings.
    Assertion: Q(sqrt(5)) has signature (2,0).
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.signature()
    expected = (2, 0)
    assert actual == expected, f"NumberField.signature mismatch: actual={actual}, expected={expected}"


def test_numberfield_ring_of_integers_basis_rank():
    """
    method: ring_of_integers

    ring_of_integers() returns the maximal order with a Z-basis of full degree.
    Assertion: Basis length equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    OK = K.ring_of_integers()
    actual = len(OK.basis())
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.ring_of_integers basis size mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant NumberField runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    x = ZZ["x"].gen()
    sample = NumberField(x**2 - 5, "a")
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.rings.number_field",),
        token_map=TOKEN_MAP,
    )
