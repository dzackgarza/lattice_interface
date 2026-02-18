# fpylll Lattice Reduction Reference
## Canonical API surface for Euclidean lattice reduction/search

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite Euclidean lattice regime |
| `[ZZMOD]` | Integer basis-matrix setting |
| `[EUCLID]` | Euclidean metric algorithms |
| `[RED]` | Reduction algorithms |
| `[ENUM]` | Enumeration/SVP/CVP search |
| `[SRC]` | Signature taken from upstream source files |

---

## 1. Scope

`fpylll` is a Python interface to `fplll` for Euclidean lattice algorithms.

Primary scope:

- basis reduction (`LLL`, `BKZ`),
- Gram-Schmidt machinery (`GSO`),
- enumeration/SVP/CVP search.

Out of scope:

- arithmetic genus/spinor-genus/discriminant-form classification,
- indefinite quadratic-form classification semantics.

---

## 2. Core Data Structures and Contracts

| API | Contract summary | Tags |
|-----|------------------|------|
| `IntegerMatrix(arg0, arg1=None, int_type='mpz')` | Integer matrix container for lattice basis/Gram workflows. `arg0,arg1` encode dimensions or copy/conversion input per docs. | `[ZZMOD, EUCLID]` |
| `GSO.Mat(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | Build GSO state from `IntegerMatrix` `B`; optional transform tracking (`U`, `UinvT`), options via `flags`, and optional Gram-mode (`gram=True`). | `[EUCLID]` |
| `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | Same constructor surface as `GSO.Mat` (alias/class exposure). | `[EUCLID]` |
| `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)` | Stateful LLL reducer over GSO object `M`; validates parameter ranges before reduction. | `[RED, EUCLID, SRC]` |
| `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` | BKZ parameter object from source-backed signature (`bkz_param.pyx`). | `[RED, EUCLID, SRC]` |
| `BKZ.Reduction(M, lll_obj, param)` | Stateful BKZ reducer over GSO object `M` with LLL helper and BKZ parameter object. | `[RED, EUCLID]` |

---

## 3. LLL Surface

| API | Contract summary | Tags |
|-----|------------------|------|
| `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | One-shot in-place reduction of basis matrix `B`; optional transform matrix `U`; optional backend/precision controls. | `[RED, EUCLID, ZZMOD]` |
| `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | Module-level helper with the same contract as `LLL.reduction`. | `[RED, EUCLID, ZZMOD]` |
| `LLL.is_reduced(B, delta=0.99, eta=0.51)` | Predicate for LLL-reducedness under given Lovasz/size-reduction parameters. | `[RED, EUCLID, ZZMOD]` |

Parameter constraints from docs/source:

- `delta` must satisfy `0.25 < delta <= 1.0`,
- `eta` must satisfy `0.5 <= eta < sqrt(delta)`,
- invalid parameter ranges raise errors before running reduction.

---

## 4. BKZ Surface

| API | Contract summary | Tags |
|-----|------------------|------|
| `BKZ.reduction(B, BKZ.Param(...), U=None, float_type=None, precision=0)` | One-shot BKZ reduction over `IntegerMatrix` basis `B`. | `[RED, EUCLID, ZZMOD]` |
| `BKZ.Reduction(M, lll_obj, param)` | Stateful BKZ for repeated tours over the same GSO object. | `[RED, EUCLID]` |
| `BKZ.Param(...)` | Full BKZ tuning surface (block size, strategies, abort/loop/time controls, GH/pruning controls). | `[RED, EUCLID, SRC]` |
| `BKZ.EasyParam(block_size, **kwds)` | Convenience parameter builder (`bkz_param.pyx`) with default strategy file and keyword passthrough. | `[RED, EUCLID, SRC]` |

Documentation caveat:

- Current `modules.html` exposes BKZ section headers but not the full member signatures.
- BKZ signatures above are source-anchored to upstream `bkz.pyx` / `bkz_param.pyx`.

---

## 5. Enumeration, SVP, and CVP

| API | Contract summary | Tags |
|-----|------------------|------|
| `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)` | Enumeration context bound to a GSO object `M`; no `threads` constructor parameter in source signature. | `[ENUM, PD, EUCLID, SRC]` |
| `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)` | Bounded subtree enumeration over basis index window `[first, last)`. | `[ENUM, PD, EUCLID]` |
| `Enumeration.get_nodes(level=None)` | Return node counts globally or at specific level. | `[ENUM, EUCLID]` |
| `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)` | SVP wrapper. `method='proved'` is proof-oriented mode; `method='fast'` is heuristic mode. | `[ENUM, PD, EUCLID]` |
| `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)` | CVP wrapper for target vector `t` with fast/proved modes and flags. | `[ENUM, EUCLID]` |
| `CVP.babai(B, t, *args, **kwargs)` | Babai nearest-plane approximation workflow. | `[ENUM, EUCLID]` |

Practical caveat:

- `CVP.closest_vector`/`CVP.babai` are normally used after LLL preprocessing.

---

## 6. Pruning and Utility Methods

| API | Contract summary | Tags |
|-----|------------------|------|
| `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')` | Static pruning optimizer interface (`run` aliases source method `prune`). | `[ENUM, EUCLID, SRC]` |
| `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)` | Adjust enumeration radius with GH-bound heuristic scaling. | `[ENUM, EUCLID]` |
| `fpylll.util.gaussian_heuristic(r)` | Compute Gaussian heuristic from squared GSO lengths `r`. | `[ENUM, EUCLID]` |

---

## 7. Indefinite Caveat

`fpylll` is a Euclidean lattice stack. It does not provide indefinite arithmetic-form classification contracts (genus/discriminant forms/local-global invariants).

For indefinite workflows, use arithmetic lattice stacks (Hecke/Indefinite.jl/Sage quadratic-form tooling) and treat `fpylll` as a PD reduction/search backend.

---

## 8. Practical Workflow Pattern

1. Build `IntegerMatrix` basis.
2. Construct `GSO.Mat` state.
3. Run `LLL.reduction` preconditioning.
4. Run `BKZ.reduction` with explicit `BKZ.Param` if stronger basis quality is needed.
5. Run `SVP.shortest_vector` / `CVP.closest_vector`.
6. Tune enumeration using `Pruning.run` and GH-bound utilities.

---

## 9. Sources

- fpylll modules index: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll GSO module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.gso`
- fpylll LLL module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.lll`
- fpylll enumeration module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.enumeration`
- fpylll utility module: `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.util`
- fpylll source (`bkz.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz.pyx`
- fpylll source (`bkz_param.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz_param.pyx`
- fpylll source (`svpcvp.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/svpcvp.pyx`
- fpylll source (`pruner.pyx`): `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/pruner.pyx`
- canonical provenance note: `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md`
