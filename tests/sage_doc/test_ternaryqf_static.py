from __future__ import annotations

import sys
import pytest

pytest.importorskip("sage.all")
from sage.all import TernaryQF
from .conftest import assert_runtime_methods_covered


TOKEN_MAP = {
    "content_primitive": {"content", "primitive"},
}


def test_ternaryqf_content_and_primitive_scaling():
    """
    method: content_primitive

    content() is gcd of coefficients and primitive() divides coefficients by content.
    Assertion: Primitive form has content 1 after normalization.
    """
    Q = TernaryQF([2, 4, 6, 8, 10, 12])
    actual_content = Q.content()
    expected_content = 2
    assert actual_content == expected_content, (
        f"TernaryQF.content mismatch: actual={actual_content}, expected={expected_content}"
    )
    actual_primitive_content = Q.primitive().content()
    expected_primitive_content = 1
    assert actual_primitive_content == expected_primitive_content, (
        "TernaryQF.primitive().content mismatch: "
        f"actual={actual_primitive_content}, expected={expected_primitive_content}"
    )


def test_ternaryqf_disc_matches_hessian_det_half():
    """
    method: disc

    disc() is det(Hessian)/2 in Sage's ternary convention.
    Assertion: Returned discriminant matches det(matrix())/2.
    """
    Q = TernaryQF([1, 1, 1, 0, 0, 0])
    actual = Q.disc()
    expected = Q.matrix().det() / 2
    assert actual == expected, f"TernaryQF.disc mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_quadratic_form_conversion_preserves_values():
    """
    method: quadratic_form

    quadratic_form() converts a TernaryQF to an equivalent QuadraticForm.
    Assertion: Both forms evaluate equally on a sample vector.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    QQF = Q.quadratic_form()
    v = (1, 2, -1)
    actual = QQF(v)
    expected = Q(v)
    assert actual == expected, (
        f"TernaryQF.quadratic_form value mismatch: actual={actual}, expected={expected}, v={v}"
    )


def test_ternaryqf_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant TernaryQF runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = TernaryQF([2, 3, 5, 1, -1, 2])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.ternary_qf",),
        token_map=TOKEN_MAP,
    )
