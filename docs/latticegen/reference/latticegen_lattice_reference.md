# latticegen Reference
## Comprehensive guide to the two different "latticegen" toolchains

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[GEN]` | Instance generation |
| `[ZZMOD]` | Integer-basis lattice setting |
| `[EUCLID]` | Euclidean lattice benchmark setting |
| `[IMG]` | Image/moire lattice generation |

---

## 1. Scope and Naming Collision

"latticegen" refers to two different ecosystems:

1. `fplll` ecosystem utility (`latticegen`) for lattice basis instance generation (benchmark/reduction pipelines).
2. Python package `latticegen` (`TAdeJong/moire-lattice-generator`) for moire lattice image synthesis/analysis.

This file documents both so downstream docs do not mix them.

---

## 2. fplll latticegen (benchmark instance generator)

### 2.1 What it is

`latticegen` in `fplll` is a command-line generator for integer lattice bases used with LLL/BKZ/SVP/CVP benchmarking.

### 2.2 Typical usage

- Generate instance with `latticegen ...`
- Pipe/read into `fplll`/`fpylll` for reduction or search

### 2.3 Common generator families/options

The `fplll` `latticegen` CLI exposes method codes and argument shapes:

`latticegen [-randseed <int|time>] <method> <args...>`

| Method | Arguments | Generator in source | Typical use |
|--------|-----------|---------------------|-------------|
| `r` | `<d> <b>` | `gen_intrel` | Integer relation instances |
| `s` | `<d> <b> <b2>` | `gen_simdioph` | Simultaneous Diophantine-style instances |
| `u` | `<d> <b>` | `gen_uniform` | Uniform random integer lattices |
| `n` | `<d> <b> <c>` | `gen_ntrulike` / `gen_ntrulike_bits` | NTRU-like bases |
| `N` | `<d> <b> <c>` | `gen_ntrulike2` / `gen_ntrulike2_bits` | Alternate NTRU-like family |
| `q` | `<d> <k> <b> <c>` | `gen_qary` / `gen_qary_bits` / `gen_qary_prime` | q-ary lattices |
| `t` | `<d> <f>` | `gen_trg` | Triangular/randomized geometric family |
| `T` | `<d>` + stdin weights | `gen_trg2` | Weighted/trg2 family from stdin data |

Selector values in source:

- For `n` / `N`: `c in {'b','q'}`.
- For `q`: `c in {'b','q','p'}`.
- `-randseed time` or explicit integer seed controls reproducibility.

| Option family | Purpose | Tags |
|---------------|---------|------|
| random/uniform style families | Synthetic random lattice bases | `[GEN, ZZMOD, EUCLID]` |
| knapsack/NTRU-style families | Structured cryptanalytic benchmark lattices | `[GEN, ZZMOD, EUCLID]` |
| dimension/seed controls | Reproducible scaling studies | `[GEN]` |

This toolchain is the one relevant for reduction benchmarking workflows.

---

## 3. Python `latticegen` (moire package)

### 3.1 What it is

The PyPI/GitHub package named `latticegen` is moire-lattice/image oriented and targets geometric/image analysis tasks.

### 3.2 Capability surface

| Capability | Description | Tags |
|------------|-------------|------|
| Moire lattice generation | Build synthetic moire lattice imagery and patterns | `[GEN, IMG]` |
| Image-space lattice analysis | Analyze periodic structures in image data | `[IMG]` |
| Python package workflow | Install/import as standard Python package | `[IMG]` |

This package is not a drop-in replacement for `fplll` benchmark lattice generation.

---

## 4. Selection Guide

Use `fplll latticegen` when you need:

- integer basis instances,
- reduction benchmark corpora,
- cryptanalytic test lattices for `fpylll`/`fplll`.

Use Python `latticegen` when you need:

- moire pattern generation,
- image-centric lattice analysis.

---

## 5. Source-Backed Notes

- DeepWiki did not provide docs for the `TAdeJong/moire-lattice-generator` repository in this session.
- `fplll` documentation is the canonical source for the CLI generator in reduction workflows.

---

## 6. Sources

- fplll docs home: https://fplll.github.io/fplll/
- fplll `latticegen` manpage index: https://fplll.github.io/fplll/latticegen_8cpp.html
- fplll source (`latticegen.cpp`): https://raw.githubusercontent.com/fplll/fplll/master/fplll/latticegen.cpp
- fplll repository: https://github.com/fplll/fplll
- PyPI `latticegen`: https://pypi.org/project/latticegen/
- `TAdeJong/moire-lattice-generator`: https://github.com/TAdeJong/moire-lattice-generator
