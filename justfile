set shell := ["bash", "-cu"]

default: test

# Bootstrap Python + Julia bridge dependencies used by tests/julia_pytest.
setup:
    HOME=/tmp/sage-home conda run -n sage python -m pip install pytest juliacall juliapkg
    HOME=/tmp/sage-home PYTHON_JULIAPKG_PROJECT=/tmp/sage-home/julia_env JULIA_DEPOT_PATH=/tmp/sage-home/.julia conda run -n sage python -c "from juliacall import Main as jl; jl.seval('using Pkg'); jl.seval(\"Pkg.activate(\\\"tests/julia_doc\\\")\"); jl.seval('Pkg.Registry.update()'); jl.seval('Pkg.instantiate()'); jl.seval('Pkg.precompile()'); print(jl.seval(\"VERSION\"))"

# Run all repository tests (non-Sage + Sage static docs tests, then Julia/Oscar).
test:
    HOME=/tmp/sage-home conda run -n sage /opt/conda/envs/sage/bin/python -m pytest -q tests --ignore=tests/new_lattice_interface

# Run full test suite, including in-progress wrapper-contract tests.
test-full:
    HOME=/tmp/sage-home conda run -n sage /opt/conda/envs/sage/bin/python -m pytest -q tests
