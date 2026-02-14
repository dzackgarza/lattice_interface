set shell := ["bash", "-cu"]

default: test

# Run all repository tests (non-Sage + Sage static docs tests).
test:
    HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests
