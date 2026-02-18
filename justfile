set shell := ["bash", "-cu"]

default: test

# Bootstrap Python + Julia bridge dependencies used by tests/julia_pytest.
setup:
    conda run -n sage python -m pip install pytest juliacall juliapkg pydantic pyright black
    julia -e "using Pkg; Pkg.add(\"Nemo\"); Pkg.add(\"Hecke\"); Pkg.add(\"Oscar\");"
    # julia -e "using Pkg; Pkg.add(\"Indefinite\");" # Unsatsfiable requirements, needs its own environment.
    # PYTHON_JULIAPKG_EXE=/home/codespace/.juliaup/bin/julia 
    conda run -n sage python -c "from juliacall import Main as jl; print(jl.seval(\"VERSION\"))"

install-sage:
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash "Miniforge3-$(uname)-$(uname -m).sh" -b -p ~/miniforge3
    rm "Miniforge3-$(uname)-$(uname -m).sh"
    ~/miniforge3/bin/conda init bash
    ~/miniforge3/bin/conda create -n sage sage -y
    ~/miniforge3/bin/conda run -n sage python -m pip install pytest juliacall juliapkg pydantic pyright black
    ~/miniforge3/bin/conda run -n sage sage -c "print('SageMath installed OK')"

# Run all repository tests (non-Sage + Sage static docs tests, then Julia/Oscar).
test:
    HOME=/tmp/sage-home ~/miniforge3/bin/conda run -n sage ~/miniforge3/envs/sage/bin/python -m pytest -q tests --ignore=tests/new_lattice_interface

# Run full test suite, including in-progress wrapper-contract tests.
test-full:
    HOME=/tmp/sage-home ~/miniforge3/bin/conda run -n sage ~/miniforge3/envs/sage/bin/python -m pytest -q tests
