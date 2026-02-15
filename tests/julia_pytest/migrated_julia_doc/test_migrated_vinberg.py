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


def test_1_vinberg_algorithm_finds_roots_of_hyperbolic_lattice():
    """
    method: vinberg_algorithm
    """
    code = r'''
    # method: vinberg_algorithm
    using Oscar
    # Hyperbolic plane direct sum with negative definite part
    # Use a simple (1,n) lattice: U + A1(-1)
    L = hyperbolic_plane_lattice()
    # vinberg_algorithm needs signature (1,0,n), so use from Gram matrix
    # Simple rank-2 hyperbolic: diag(1, -1)
    Q = ZZ[1 0; 0 -1]
    roots = vinberg_algorithm(Q, 2)
    @test length(roots) > 0
'''
    _jl_eval_testitem(code)

def test_2_vinberg_algorithm_from_zzlat():
    """
    method: vinberg_algorithm(S::ZZLat, ub)
    """
    code = r'''
    # method: vinberg_algorithm(S::ZZLat, ub)
    using Oscar
    # Construct a signature (1,0,n) lattice
    Q = ZZ[1 0; 0 -1]
    L = integer_lattice(gram = Q)
    roots = vinberg_algorithm(L, 2)
    @test length(roots) > 0
'''
    _jl_eval_testitem(code)

def test_3_short_vectors_affine_affine_enumeration():
    """
    method: short_vectors_affine
    """
    code = r'''
    # method: short_vectors_affine
    using Oscar
    # This is used internally by Vinberg; test with a simple lattice
    L = integer_lattice(gram = ZZ[1 0; 0 -1])
    # Find vectors x with x^2 = d and x . v = alpha
    # This may require specific setup; test that it returns a collection
    v = ZZ[1, 0]
    result = short_vectors_affine(L, v, 0, -1)
    @test result isa Vector || result isa AbstractVector
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'short_vectors_affine',
    'vinberg_algorithm',
    'vinberg_algorithm(S::ZZLat, ub)',
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
