set shell := ["bash", "-cu"]

default: test

# Bootstrap Python + Julia bridge dependencies used by tests/julia_pytest.
setup:
    conda run -n sage python -m pip install pytest juliacall juliapkg pydantic pyright black
    julia -e "using Pkg; Pkg.add(\"Nemo\"); Pkg.add(\"Hecke\"); Pkg.add(\"Oscar\");"
    # julia -e "using Pkg; Pkg.add(\"Indefinite\");" # Unsatsfiable requirements, needs its own environment.
    # PYTHON_JULIAPKG_EXE=/home/codespace/.juliaup/bin/julia 
    conda run -n sage python -c "from juliacall import Main as jl; print(jl.seval(\"VERSION\"))"

# Run all repository tests (non-Sage + Sage static docs tests, then Julia/Oscar).
test:
    HOME=/tmp/sage-home conda run -n sage /opt/conda/envs/sage/bin/python -m pytest -q tests --ignore=tests/new_lattice_interface

# Run full test suite, including in-progress wrapper-contract tests.
test-full:
    HOME=/tmp/sage-home conda run -n sage /opt/conda/envs/sage/bin/python -m pytest -q tests
