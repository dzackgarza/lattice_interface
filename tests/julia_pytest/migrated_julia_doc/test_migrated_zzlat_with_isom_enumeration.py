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


def test_1_enumerate_classes_of_lattices_with_isometry_a1_genus_m_2():
    """
    method: enumerate_classes_of_lattices_with_isometry
    """
    code = r'''
    # method: enumerate_classes_of_lattices_with_isometry
    using Oscar
    L = root_lattice(:A, 1)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = enumerate_classes_of_lattices_with_isometry(g, x + 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 2, reps)
'''
    _jl_eval_testitem(code)

def test_2_enumerate_classes_of_lattices_with_isometry_a1_genus_m_1():
    """
    method: enumerate_classes_of_lattices_with_isometry
    """
    code = r'''
    # method: enumerate_classes_of_lattices_with_isometry
    using Oscar
    L = root_lattice(:A, 1)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = enumerate_classes_of_lattices_with_isometry(g, x - 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 1, reps)
'''
    _jl_eval_testitem(code)

def test_3_representatives_of_hermitian_type_a2_genus_order_2():
    """
    method: representatives_of_hermitian_type
    """
    code = r'''
    # method: representatives_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = representatives_of_hermitian_type(g, x + 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 2, reps)
'''
    _jl_eval_testitem(code)

def test_4_admissible_triples_small_genus():
    """
    method: admissible_triples
    """
    code = r'''
    # method: admissible_triples
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    @test triples isa Vector
    for (g1, g2) in triples
        @test rank(g1) + rank(g2) == rank(g)
    end
'''
    _jl_eval_testitem(code)

def test_5_is_admissible_triple_roundtrip_from_admissible_triples():
    """
    method: is_admissible_triple
    """
    code = r'''
    # method: is_admissible_triple
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    if !isempty(triples)
        g1, g2 = first(triples)
        @test is_admissible_triple(g, g1, g2, 2)
    else
        @test true
    end
'''
    _jl_eval_testitem(code)

def test_6_splitting_of_hermitian_type_a2_negation():
    """
    method: splitting_of_hermitian_type
    """
    code = r'''
    # method: splitting_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_hermitian_type(Lf)
    @test result isa Vector
    @test all(r -> r isa Oscar.ZZLatWithIsom, result)
'''
    _jl_eval_testitem(code)

def test_7_splitting_generic_splitting():
    """
    method: splitting
    """
    code = r'''
    # method: splitting
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting(Lf)
    @test result isa Vector
    @test all(r -> r isa Oscar.ZZLatWithIsom, result)
'''
    _jl_eval_testitem(code)

def test_8_splitting_of_prime_power_small_example():
    """
    method: splitting_of_prime_power
    """
    code = r'''
    # method: splitting_of_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_prime_power(Lf, 2)
    @test result isa Vector
'''
    _jl_eval_testitem(code)

def test_9_splitting_of_pure_mixed_prime_power_small_example():
    """
    method: splitting_of_pure_mixed_prime_power
    """
    code = r'''
    # method: splitting_of_pure_mixed_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_pure_mixed_prime_power(Lf, 2)
    @test result isa Vector
'''
    _jl_eval_testitem(code)

def test_10_splitting_of_mixed_prime_power_small_example():
    """
    method: splitting_of_mixed_prime_power
    """
    code = r'''
    # method: splitting_of_mixed_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_mixed_prime_power(Lf, 2)
    @test result isa Vector
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'admissible_triples',
    'enumerate_classes_of_lattices_with_isometry',
    'is_admissible_triple',
    'representatives_of_hermitian_type',
    'splitting',
    'splitting_of_hermitian_type',
    'splitting_of_mixed_prime_power',
    'splitting_of_prime_power',
    'splitting_of_pure_mixed_prime_power',
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
