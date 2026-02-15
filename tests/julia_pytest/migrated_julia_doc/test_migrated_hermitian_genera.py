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


def test_1_genus_global_genus_of_hermitian_lattice():
    """
    method: genus(L::HermLat)
    """
    code = r'''
    # method: genus(L::HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_2_genus_local_genus_of_hermitian_lattice():
    """
    method: genus(L::HermLat, p)
    """
    code = r'''
    # method: genus(L::HermLat, p)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    g = genus(L, p)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_3_representative_hermitian_genus_representative():
    """
    method: representative(G)
    """
    code = r'''
    # method: representative(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    R = representative(g)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_4_representatives_all_classes_in_hermitian_genus():
    """
    method: representatives(G)
    """
    code = r'''
    # method: representatives(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    reps = representatives(g)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

def test_5_mass_hermitian_lattice_mass():
    """
    method: mass
    """
    code = r'''
    # method: mass
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    m = mass(L)
    @test m > 0
'''
    _jl_eval_testitem(code)

def test_6_rank_hermitian_genus_rank():
    """
    method: rank(G)
    """
    code = r'''
    # method: rank(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_7_signatures_hermitian_genus_signatures():
    """
    method: signatures(G)
    """
    code = r'''
    # method: signatures(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    sigs = signatures(g)
    @test length(sigs) >= 1
'''
    _jl_eval_testitem(code)

def test_8_is_integral_hermitian_genus_integrality():
    """
    method: is_integral(G)
    """
    code = r'''
    # method: is_integral(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test is_integral(g) == true
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'genus(L::HermLat)',
    'genus(L::HermLat, p)',
    'is_integral(G)',
    'mass',
    'rank(G)',
    'representative(G)',
    'representatives(G)',
    'signatures(G)',
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
