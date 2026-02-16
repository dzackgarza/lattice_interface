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


def test_1_automorphism_group_generators_a2_automorphism_group():
    """
    method: automorphism_group_generators
    """
    code = r'''
    # method: automorphism_group_generators
    using Oscar
    L = root_lattice(:A, 2)
    gens = automorphism_group_generators(L)
    @test length(gens) >= 1
    # Each generator should preserve the Gram matrix
    G = gram_matrix(L)
    for g in gens
        @test g * G * transpose(g) == G
    end
'''
    _jl_eval_testitem(code)

def test_2_automorphism_group_order_a2_has_aut_12():
    """
    method: automorphism_group_order
    """
    code = r'''
    # method: automorphism_group_order
    using Oscar
    L = root_lattice(:A, 2)
    @test automorphism_group_order(L) == 12
'''
    _jl_eval_testitem(code)

def test_3_is_isometric_a2_is_isometric_to_itself():
    """
    method: is_isometric
    """
    code = r'''
    # method: is_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    @test is_isometric(L, M) == true
'''
    _jl_eval_testitem(code)

def test_4_is_isometric_a2_not_isometric_to_a3():
    """
    method: is_isometric
    """
    code = r'''
    # method: is_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 3)
    @test is_isometric(L, M) == false
'''
    _jl_eval_testitem(code)

def test_5_is_isometric_with_isometry_returns_transformation():
    """
    method: is_isometric_with_isometry
    """
    code = r'''
    # method: is_isometric_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    flag, T = is_isometric_with_isometry(L, M)
    @test flag == true
    @test T * gram_matrix(L) * transpose(T) == gram_matrix(M)
'''
    _jl_eval_testitem(code)

def test_6_is_rationally_isometric_same_genus_implies_rational_isometry():
    """
    method: is_rationally_isometric
    """
    code = r'''
    # method: is_rationally_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    @test is_rationally_isometric(L, M) == true
'''
    _jl_eval_testitem(code)

def test_7_hasse_invariant_a2_at_prime_2():
    """
    method: hasse_invariant
    """
    code = r'''
    # method: hasse_invariant
    using Oscar
    L = root_lattice(:A, 2)
    h = hasse_invariant(L, 2)
    @test h in [1, -1]
'''
    _jl_eval_testitem(code)

def test_8_witt_invariant_a2_at_prime_2():
    """
    method: witt_invariant
    """
    code = r'''
    # method: witt_invariant
    using Oscar
    L = root_lattice(:A, 2)
    w = witt_invariant(L, 2)
    @test w in [1, -1]
'''
    _jl_eval_testitem(code)

def test_9_is_locally_isometric_same_lattice_at_prime_2():
    """
    method: is_locally_isometric
    """
    code = r'''
    # method: is_locally_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    @test is_locally_isometric(L, M, 2) == true
    @test is_locally_isometric(L, M, 3) == true
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'automorphism_group_generators',
    'automorphism_group_order',
    'hasse_invariant',
    'is_isometric',
    'is_isometric_with_isometry',
    'is_locally_isometric',
    'is_rationally_isometric',
    'witt_invariant',
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
