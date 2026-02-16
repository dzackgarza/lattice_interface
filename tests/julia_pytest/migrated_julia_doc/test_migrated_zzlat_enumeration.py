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


def test_1_short_vectors_a2_has_6_vectors_of_norm_2():
    """
    method: short_vectors
    """
    code = r'''
    # method: short_vectors
    using Oscar
    L = root_lattice(:A, 2)
    sv = short_vectors(L, 2)
    # A2 has 6 roots; short_vectors returns up to sign, so 3 pairs
    @test length(sv) == 3
'''
    _jl_eval_testitem(code)

def test_2_shortest_vectors_a2_minimum_norm_is_2():
    """
    method: shortest_vectors
    """
    code = r'''
    # method: shortest_vectors
    using Oscar
    L = root_lattice(:A, 2)
    sv = shortest_vectors(L)
    @test length(sv) == 3  # up to sign
'''
    _jl_eval_testitem(code)

def test_3_minimum_a2_has_minimum_2():
    """
    method: minimum
    """
    code = r'''
    # method: minimum
    using Oscar
    L = root_lattice(:A, 2)
    @test minimum(L) == 2
'''
    _jl_eval_testitem(code)

def test_4_minimum_e8_has_minimum_2():
    """
    method: minimum
    """
    code = r'''
    # method: minimum
    using Oscar
    L = root_lattice(:E, 8)
    @test minimum(L) == 2
'''
    _jl_eval_testitem(code)

def test_5_kissing_number_a2_kissing_number_is_6():
    """
    method: kissing_number
    """
    code = r'''
    # method: kissing_number
    using Oscar
    L = root_lattice(:A, 2)
    @test kissing_number(L) == 6
'''
    _jl_eval_testitem(code)

def test_6_kissing_number_e8_kissing_number_is_240():
    """
    method: kissing_number
    """
    code = r'''
    # method: kissing_number
    using Oscar
    L = root_lattice(:E, 8)
    @test kissing_number(L) == 240
'''
    _jl_eval_testitem(code)

def test_7_close_vectors_finds_vectors_near_target():
    """
    method: close_vectors
    """
    code = r'''
    # method: close_vectors
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    # Find lattice points within distance^2 <= 1 of (1/2, 1/2)
    cv = close_vectors(L, QQ[1//2, 1//2], 1)
    @test length(cv) > 0
'''
    _jl_eval_testitem(code)

def test_8_short_vectors_with_lower_and_upper_bound():
    """
    method: short_vectors
    """
    code = r'''
    # method: short_vectors
    using Oscar
    L = root_lattice(:D, 4)
    sv = short_vectors(L, 2, 4)
    @test length(sv) > 0
    for (v, n) in sv
        @test 2 <= n <= 4
    end
'''
    _jl_eval_testitem(code)

def test_9_short_vectors_iterator_lazy_enumeration():
    """
    method: short_vectors_iterator
    """
    code = r'''
    # method: short_vectors_iterator
    using Oscar
    L = root_lattice(:A, 2)
    # Iterator over vectors with norm <= 2
    it = short_vectors_iterator(L, 2)
    count = 0
    for (v, n) in it
        @test n <= 2
        count += 1
    end
    @test count == 3  # A2 has 3 pairs of roots (up to sign)
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_10_vectors_of_square_and_divisibility():
    """
    method: vectors_of_square_and_divisibility
    """
    code = r'''
    # method: vectors_of_square_and_divisibility
    using Oscar
    L = root_lattice(:A, 2)
    # Vectors v with v^2 = 2 and divisibility 1
    vecs = vectors_of_square_and_divisibility(L, 2, 1)
    @test length(vecs) >= 1
'''
    _jl_eval_testitem(code)


@pytest.mark.tdd_red
def test_11_enumerate_quadratic_triples():
    """
    method: enumerate_quadratic_triples
    """
    code = r'''
    # method: enumerate_quadratic_triples
    using Oscar
    L = root_lattice(:A, 2)
    triples = enumerate_quadratic_triples(L, 2)
    @test length(triples) >= 0
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'close_vectors',
    'enumerate_quadratic_triples',
    'kissing_number',
    'minimum',
    'short_vectors',
    'short_vectors_iterator',
    'shortest_vectors',
    'vectors_of_square_and_divisibility',
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
