# fpylll Lattice Reduction Reference
## Comprehensive API surface for Euclidean lattice reduction/search

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite Euclidean lattice regime |
| `[ZZMOD]` | Integer basis-matrix setting |
| `[EUCLID]` | Euclidean metric algorithms |
| `[RED]` | Reduction algorithms |
| `[ENUM]` | Enumeration/SVP/CVP search |

---

## 1. Scope

`fpylll` is a Python interface to `fplll` for Euclidean lattice algorithms.

Primary focus:

- basis reduction (`LLL`, `BKZ`),
- Gram-Schmidt machinery (`GSO`),
- enumeration/SVP/CVP solvers.

Not the focus:

- arithmetic genus classification,
- indefinite quadratic-form classification.

---

## 2. Core Data Structures

| API | Description | Tags |
|-----|-------------|------|
| `IntegerMatrix` | Integer lattice basis matrix container | `[ZZMOD]` |
| `GSO.Mat(B, ...)` | Gram-Schmidt state for basis `B` | `[EUCLID]` |
| `MatGSO` | Lower-level GSO matrix machinery | `[EUCLID]` |
| `LLL.Reduction(M, ...)` | Stateful LLL reducer over GSO object | `[RED, EUCLID]` |
| `BKZ.Reduction(M, lll_obj, params)` | Stateful BKZ reducer | `[RED, EUCLID]` |
| `BKZ.Param(...)` | BKZ parameter object (block size, flags, strategies) | `[RED, EUCLID]` |

---

## 3. LLL Surface

| API | Description | Tags |
|-----|-------------|------|
| `LLL.reduction(B, ...)` | In-place LLL reduction of integer basis | `[RED, EUCLID]` |
| `lll_reduction(B, ...)` | Module-level LLL helper | `[RED, EUCLID]` |
| `LLL.Reduction(M, ...)` | Incremental/stateful LLL on GSO object | `[RED, EUCLID]` |

Common parameters:

- `delta`, `eta`
- `method` (`wrapper`, `proved`, `heuristic`, `fast`)
- `float_type`, `precision`
- optional transform matrix `U`

---

## 4. BKZ Surface

| API | Description | Tags |
|-----|-------------|------|
| `BKZ.reduction(B, BKZ.Param(...))` | One-shot BKZ reduction | `[RED, EUCLID]` |
| `BKZ.Reduction(...)` | Stateful BKZ reducer for repeated tours | `[RED, EUCLID]` |
| `BKZ.Param(block_size=..., flags=..., strategies=...)` | BKZ configuration | `[RED, EUCLID]` |

Typical flags include verbose/abort/loop and GH-bound controls (implementation/version dependent).

DeepWiki confirms both C++-backed and pure-Python algorithm layers (e.g. `fpylll.algorithms.bkz`, `bkz2`).

---

## 5. Enumeration/SVP/CVP Surface

| API | Description | Tags |
|-----|-------------|------|
| `Enumeration(...)` | Low-level bounded enumeration primitives | `[ENUM, PD, EUCLID]` |
| `SVP.shortest_vector(B, ...)` | Shortest-vector search | `[ENUM, PD, EUCLID]` |
| `CVP.closest_vector(B, t, ...)` | Closest-vector search | `[ENUM, EUCLID]` |
| `CVP.babai(B, t, ...)` | Babai nearest-plane approximation | `[ENUM, EUCLID]` |

`SVP.shortest_vector` methods:

- `method="proved"` for guaranteed search,
- `method="fast"` for heuristic/pruned workflows.

`CVP.closest_vector` practical requirement:

- use an LLL-reduced basis (standard documented workflow).

---

## 6. GSO/Pruning/Utilities

| API | Description | Tags |
|-----|-------------|------|
| `GSO.Mat(B, U=..., UinvT=...)` | GSO state with optional transform tracking | `[EUCLID]` |
| `Pruning` tooling | Pruning coefficient computation for enumeration/BKZ | `[ENUM, EUCLID]` |
| BKZ stats/tracing (`bkz_stats` helpers) | Runtime telemetry and strategy analysis | `[RED, EUCLID]` |

---

## 7. Indefinite Caveat

`fpylll` algorithms are Euclidean-lattice algorithms. They do not provide indefinite arithmetic-form classification semantics.

For indefinite lattices, use arithmetic stacks (e.g. Hecke/Indefinite.jl/Sage quadratic-form tools) and treat `fpylll` as a PD reduction/search engine only.

---

## 8. Practical Workflow Patterns

1. Build `IntegerMatrix` basis.
2. Run `LLL.reduction` preconditioning.
3. Run `BKZ.reduction` with tuned `BKZ.Param` when stronger basis quality is needed.
4. Use `SVP.shortest_vector` or `CVP.closest_vector` for search tasks.
5. Add pruning/strategy tuning for higher dimensions.

---

## 9. Sources

- fpylll docs index: https://fpylll.readthedocs.io/en/latest/modules.html
- Context7 library used: `/websites/fpylll_readthedocs_io_en`
- DeepWiki fpylll reduction overview: https://deepwiki.com/fplll/fpylll/4-lattice-reduction-algorithms
- DeepWiki fpylll SVP/CVP overview: https://deepwiki.com/fplll/fpylll/5-solving-lattice-problems
- fpylll repo: https://github.com/fplll/fpylll
