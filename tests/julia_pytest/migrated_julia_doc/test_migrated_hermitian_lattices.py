import os
import re
import sys

import pytest

os.environ.setdefault("HOME", "/tmp/sage-home")
os.environ.setdefault("PYTHON_JULIAPKG_PROJECT", "/tmp/sage-home/julia_env")
os.environ.setdefault("JULIA_DEPOT_PATH", "/tmp/sage-home/.julia")

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")
    jl.seval("using Oscar")
    jl.seval("using Test")


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def _method_token_from_docstring(func) -> str | None:
    doc = getattr(func, "__doc__", "") or ""
    for line in doc.splitlines():
        line = line.strip()
        if line.startswith("method:"):
            return line.split(":", 1)[1].strip()
    return None


def _covered_methods_from_module(module) -> set[str]:
    covered: set[str] = set()
    for name, func in module.__dict__.items():
        if not name.startswith("test_") or not callable(func) or name.endswith("_coverage"):
            continue
        token = _method_token_from_docstring(func)
        if token is not None:
            covered.add(token)
    return covered


def test_1_hermitian_lattice_construct_over_gaussian_integers():
    """
    method: hermitian_lattice
    """
    code = r'''
    # method: hermitian_lattice
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_2_base_field_returns_number_field():
    """
    method: base_field
    """
    code = r'''
    # method: base_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    E = base_field(L)
    @test degree(E) == 2
'''
    _jl_eval_testitem(code)

def test_3_fixed_field_returns_fixed_field_under_involution():
    """
    method: fixed_field
    """
    code = r'''
    # method: fixed_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    F = fixed_field(L)
    @test degree(F) == 1  # QQ
'''
    _jl_eval_testitem(code)

def test_4_pseudo_matrix_returns_pseudo_matrix_representation():
    """
    method: pseudo_matrix
    """
    code = r'''
    # method: pseudo_matrix
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    PM = pseudo_matrix(L)
    @test nrows(matrix(PM)) == 2
'''
    _jl_eval_testitem(code)

def test_5_is_positive_definite_pd_hermitian_lattice():
    """
    method: is_positive_definite
    """
    code = r'''
    # method: is_positive_definite
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test is_positive_definite(L) == true
'''
    _jl_eval_testitem(code)

def test_6_jordan_decomposition_at_a_prime():
    """
    method: jordan_decomposition
    """
    code = r'''
    # method: jordan_decomposition
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    J = jordan_decomposition(L, p)
    @test length(J) >= 1
'''
    _jl_eval_testitem(code)

def test_7_genus_representatives_hermitian_genus():
    """
    method: genus_representatives
    """
    code = r'''
    # method: genus_representatives
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    reps = genus_representatives(L)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'base_field',
    'fixed_field',
    'genus_representatives',
    'hermitian_lattice',
    'is_positive_definite',
    'jordan_decomposition',
    'pseudo_matrix',
}

def test_migrated_method_coverage():
    """
    method: runtime_coverage
    """
    covered = _covered_methods_from_module(sys.modules[__name__])
    missing = sorted(MIGRATED_METHODS - covered)
    assert not missing, (
        "Coverage failure: uncovered migrated methods found.\n"
        f"Declared methods: {sorted(MIGRATED_METHODS)}\n"
        f"Covered methods: {sorted(covered)}\n"
        f"Missing methods: {missing}"
    )
