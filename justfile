set shell := ["bash", "-cu"]

default: test

# Run all repository tests (non-Sage + Sage static docs tests, then Julia/Oscar).
test:
    HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests --ignore=tests/new_lattice_interface

# Run full test suite, including in-progress wrapper-contract tests.
test-full:
    HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests
