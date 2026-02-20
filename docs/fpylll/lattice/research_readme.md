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

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `IntegerMatrix(arg0, arg1=None, int_type='mpz')` | `arg0`: int or `IntegerMatrix`; `arg1`: int or None (optional, default `None`); `int_type`: str (optional, default `'mpz'`, accepts `'mpz'` or `'long'`) | `IntegerMatrix` | Integer matrix container for lattice basis/Gram workflows. When `arg0`, `arg1` are integers, creates an `arg0 × arg1` zero matrix; when `arg0` is an `IntegerMatrix` and `arg1` is `None`, creates a copy. Source: `integer_matrix.pyx` | `[ZZMOD, EUCLID, SRC]` |
| `GSO.Mat(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional, default `None`); `UinvT`: `IntegerMatrix` (optional, default `None`); `flags`: int (optional, default `GSO_DEFAULT`); `float_type`: str (optional, default `'double'`); `gram`: bool (optional, default `False`); `update`: bool (optional, default `False`) | `MatGSO` | Build GSO state from basis matrix `B`; optional transform tracking (`U`, `UinvT`); `flags` controls INT_GRAM, ROW_EXPO, OP_FORCE_LONG; `gram=True` treats `B` as a Gram matrix; `update=True` calls `update_gso()`. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` (optional); `UinvT`: `IntegerMatrix` (optional); `flags`: int (optional); `float_type`: str (optional); `gram`: bool (optional); `update`: bool (optional) | `MatGSO` | Alias for `GSO.Mat`; same constructor surface. Source: `gso.pyx` | `[EUCLID, SRC]` |
| `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)` | `M`: `MatGSO`; `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `flags`: int (optional, default `LLL_DEFAULT`; valid flags: `LLL.DEFAULT`, `LLL.VERBOSE`, `LLL.EARLY_RED`, `LLL.SIEGEL`) | `LLL.Reduction` | Stateful LLL reducer over GSO object `M`; validates `0.25 < delta <= 1.0` and `0.5 <= eta < sqrt(delta)` before reduction. Calling the object (`__call__`) supports partial-range reduction: `LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)` where `kappa_end=-1` defaults to `M.d`. `.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)` performs only size reduction on the given row range. Properties: `.delta`, `.eta`, `.final_kappa`, `.last_early_red`, `.zeros`, `.nswaps`. Source: `lll.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` | `block_size`: int; `strategies`: str (optional, default `BKZ_DEFAULT_STRATEGY`); `delta`: float (optional); `flags`: int (optional); `max_loops`: int (optional); `max_time`: int (optional); `auto_abort`: object (optional); `gh_factor`: float (optional); `min_success_probability`: float (optional); `rerandomization_density`: float (optional); `dump_gso_filename`: str (optional); `**kwds`: dict | `BKZ.Param` | BKZ parameter object specifying block size, strategy file, abort conditions, and pruning controls. Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Reduction(M, lll_obj, param)` | `M`: `MatGSO`; `lll_obj`: `LLL.Reduction`; `param`: `BKZ.Param` | `BKZ.Reduction` | Stateful BKZ reducer over GSO object `M` with LLL helper and BKZ parameter object. Source: `bkz.pyx` | `[RED, EUCLID, SRC]` |

---

## 3. LLL Surface

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` or `None` (optional, default `None`); `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `method`: str or `None` (optional, default `None`; one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, `None`); `float_type`: str or `None` (optional, default `None`); `precision`: int (optional, default `0`); `flags`: int (optional, default `LLL_DEFAULT`) | `IntegerMatrix` | Reduces basis matrix `B` in place; returns `B`. Optional transform matrix `U` tracks unimodular transformation. **Method/float_type constraints**: `method='wrapper'` requires `float_type=None`; `method='fast'` requires `float_type` in `('double', 'long double', 'dd', 'qd')`; `method=None` defaults to `'wrapper'`. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix`; `U`: `IntegerMatrix` or `None` (optional); `delta`: float (optional); `eta`: float (optional); `method`: str or `None` (optional; one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, `None`); `float_type`: str or `None` (optional); `precision`: int (optional); `flags`: int (optional) | `IntegerMatrix` | Module-level alias with the same contract as `LLL.reduction`; reduces `B` in place and returns `B`. Same method/float_type constraints apply. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `LLL.is_reduced(M, delta=0.99, eta=0.51)` | `M`: `IntegerMatrix` or `MatGSO`; `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`) | `bool` | Predicate for LLL-reducedness under given Lovász/size-reduction parameters. Accepts either an `IntegerMatrix` (GSO is recomputed internally) or a `MatGSO` object (existing GSO state is reused). **Caution**: may return `False` for a genuinely LLL-reduced matrix if the internal floating-point precision is too low. Source: `lll.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |

Additional LLL surface (from `wrapper.pyx` / `lll.pyx`):

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `LLL.Wrapper(B, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)` | `B`: `IntegerMatrix` (must have `int_type='mpz'`; raises `NotImplementedError` for non-mpz types); `delta`: float (optional, default `0.99`); `eta`: float (optional, default `0.51`); `flags`: int (optional, default `LLL_DEFAULT`) | `LLL.Wrapper` | Stateful LLL wrapper object. Calls `__call__()` to run LLL on `B` in place. **Single-use**: `__call__()` may only be called once; raises `ValueError` on repeated invocation. Internally wraps the C++ `Wrapper` class. **mpz-only restriction**: unlike `LLL.Reduction`, only accepts `IntegerMatrix` with `int_type='mpz'`. Source: `wrapper.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |

Parameter constraints from docs/source:

- `delta` must satisfy `0.25 < delta <= 1.0`,
- `eta` must satisfy `0.5 <= eta < sqrt(delta)`,
- invalid parameter ranges raise errors before running reduction.

---

## 4. BKZ Surface

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `BKZ.reduction(B, param, U=None, float_type=None, precision=0)` | `B`: `IntegerMatrix`; `param`: `BKZ.Param`; `U`: `IntegerMatrix` or `None` (optional, default `None`); `float_type`: str or `None` (optional, default `None`); `precision`: int (optional, default `0`) | `IntegerMatrix` | Reduces basis `B` in place using BKZ parameter object `param`; returns `B`. Source: `bkz.pyx` | `[RED, EUCLID, ZZMOD, SRC]` |
| `BKZ.Reduction(M, lll_obj, param)` | `M`: `MatGSO`; `lll_obj`: `LLL.Reduction`; `param`: `BKZ.Param` | `BKZ.Reduction` | Stateful BKZ for repeated tours over the same GSO object. Source: `bkz.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` | `block_size`: int; `strategies`: str (optional); `delta`: float (optional); `flags`: int (optional); `max_loops`: int (optional); `max_time`: int (optional); `auto_abort`: object (optional); `gh_factor`: float (optional); `min_success_probability`: float (optional); `rerandomization_density`: float (optional); `dump_gso_filename`: str (optional); `**kwds`: dict | `BKZ.Param` | Full BKZ tuning surface (block size, strategies, abort/loop/time controls, GH/pruning controls). Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |
| `BKZ.EasyParam(block_size, **kwds)` | `block_size`: int; `**kwds`: dict | `BKZ.EasyParam` | Convenience parameter builder with default strategy file and keyword passthrough. Source: `bkz_param.pyx` | `[RED, EUCLID, SRC]` |

Documentation caveat:

- Current `modules.html` exposes BKZ section headers but not the full member signatures.
- BKZ signatures above are source-anchored to upstream `bkz.pyx` / `bkz_param.pyx`.

---

## 5. Enumeration, SVP, and CVP

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)` | `M`: `MatGSO`; `nr_solutions`: int (optional, default `1`); `strategy`: `EvaluatorStrategy` (optional, default `BEST_N_SOLUTIONS`); `sub_solutions`: bool (optional, default `False`) | `Enumeration` | Enumeration context bound to a GSO object `M`; no `threads` constructor parameter in source signature. Source: `enumeration.pyx` | `[ENUM, PD, EUCLID, SRC]` |
| `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)` | `first`: int; `last`: int; `max_dist`: float; `max_dist_expo`: int; `target`: list (optional, default `None`); `subtree`: object (optional, default `None`); `pruning`: object (optional, default `None`); `dual`: bool (optional, default `False`); `subtree_reset`: bool (optional, default `False`) | `list` of tuples `(vector, norm)` | Bounded subtree enumeration over basis index window `[first, last)`. Source: `enumeration.pyx` | `[ENUM, PD, EUCLID, SRC]` |
| `Enumeration.get_nodes(level=None)` | `level`: int (optional, default `None`) | `int` or `dict` | Return node counts globally (`level=None`) or at specific level. Source: `enumeration.pyx` | `[ENUM, EUCLID, SRC]` |
| `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)` | `B`: `IntegerMatrix`; `method`: str (optional, default `'fast'`); `flags`: int (optional, default `SVP_DEFAULT`); `pruning`: bool (optional, default `True`); `preprocess`: bool (optional, default `True`); `max_aux_solutions`: int (optional, default `0`) | `tuple` `(vector, norm)` | SVP wrapper. `method='proved'` is proof-oriented mode; `method='fast'` is heuristic mode. Source: `svpcvp.pyx` | `[ENUM, PD, EUCLID, SRC]` |
| `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)` | `B`: `IntegerMatrix`; `t`: list (target vector); `method`: str (optional, default `'fast'`); `flags`: int (optional, default `CVP_DEFAULT`) | `list` (vector) | CVP wrapper for target vector `t` with fast/proved modes and flags. Source: `svpcvp.pyx` | `[ENUM, EUCLID, SRC]` |
| `CVP.babai(B, t, *args, **kwargs)` | `B`: `IntegerMatrix`; `t`: list (target vector); `*args`: tuple; `**kwargs`: dict | `list` (vector) | Babai nearest-plane approximation workflow. Source: `svpcvp.pyx` | `[ENUM, EUCLID, SRC]` |

Practical caveat:

- `CVP.closest_vector`/`CVP.babai` are normally used after LLL preprocessing.

---

## 6. Pruning and Utility Methods

| API | Argument Types | Return Type | Description | Tags |
|-----|----------------|-------------|-------------|------|
| `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')` | `radius`: float; `cost`: float; `gso_r`: list; `target`: float; `metric`: str (optional, default `'probability'`); `flags`: int (optional, default `Pruning.GRADIENT`); `pruning`: object (optional, default `None`); `float_type`: str (optional, default `'double'`) | `tuple` `(pruning_vector, probability)` | Static pruning optimizer interface (`run` aliases source method `prune`). Source: `pruner.pyx` | `[ENUM, EUCLID, SRC]` |
| `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)` | `dist`: float; `dist_expo`: int; `block_size`: int; `root_det`: float; `gh_factor`: float | `tuple` `(adjusted_dist, adjusted_expo)` | Adjust enumeration radius with GH-bound heuristic scaling. Source: `util` module | `[ENUM, EUCLID, SRC]` |
| `fpylll.util.gaussian_heuristic(r)` | `r`: list (squared GSO lengths) | `float` | Compute Gaussian heuristic from squared GSO lengths `r`. Source: `util` module | `[ENUM, EUCLID, SRC]` |

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
