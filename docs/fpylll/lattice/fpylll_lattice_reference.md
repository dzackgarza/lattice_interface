# fpylll Lattice Reference

Local upstream sources:
- `docs/fpylll/upstream/src/integer_matrix.pyx` — IntegerMatrix API
- `docs/fpylll/upstream/src/gso.pyx` — MatGSO (Gram-Schmidt orthogonalization) API
- `docs/fpylll/upstream/src/lll.pyx` — LLL reduction API
- `docs/fpylll/upstream/src/bkz.pyx` — BKZ reduction API
- `docs/fpylll/upstream/src/bkz_param.pyx` — BKZ parameter API
- `docs/fpylll/upstream/src/enumeration.pyx` — Enumeration API
- `docs/fpylll/upstream/src/svpcvp.pyx` — SVP/CVP API
- `docs/fpylll/upstream/src/pruner.pyx` — Pruning API
- `docs/fpylll/upstream/docs/modules.rst` — Module overview

---

## 1. Core Data Structures

### IntegerMatrix

**`IntegerMatrix(arg0, arg1=None, int_type='mpz')`**
- **Signature**: `IntegerMatrix(arg0, arg1=None, int_type='mpz')`
- **Description**: Dense integer matrix constructor. Supports `mpz` (arbitrary precision) and `long` (fixed-size) integer types.
- **Source**: `integer_matrix.pyx:298-361`

**`IntegerMatrix.from_matrix(A, nrows=None, ncols=None, **kwds)`**
- **Signature**: `classmethod IntegerMatrix.from_matrix(A, nrows=None, ncols=None, **kwds)`
- **Description**: Construct from matrix-like object with element access `A[i,j]` or `A[i][j]`.
- **Source**: `integer_matrix.pyx:363-373`

**`IntegerMatrix.from_iterable(nrows, nrows, iterable)`**
- **Signature**: `classmethod IntegerMatrix.from_iterable(nrows, ncols, iterable)`
- **Description**: Construct from iterable of integers.
- **Source**: `integer_matrix.pyx:375-395`

**`IntegerMatrix.randomize(density=1.0, bits=30, distribution='uniform')`**
- **Signature**: `IntegerMatrix.randomize(density=1.0, bits=30, distribution='uniform')`
- **Description**: Randomize matrix entries.
- **Source**: `integer_matrix.pyx:590-680`

### MatGSO (Gram-Schmidt Orthogonalization)

**`MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`**
- **Signature**: `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- **Description**: Provides interface for elementary basis operations, Gram matrix, and Gram-Schmidt orthogonalization. Stores integral basis `B`, μ-coefficients, and r-coefficients.
- **Constraints**: `float_type` must be one of: `'double'`, `'long_double'`, `'dpe'`, `'mpfr'`, `'dd'`, `'qd'` (the latter two require QD library).
- **Source**: `gso.pyx:98-99`

**`MatGSO.update_gso()`**
- **Signature**: `MatGSO.update_gso()`
- **Description**: Compute/update Gram-Schmidt orthogonalization.
- **Source**: `gso.pyx:140-165`

**`MatGSO.get_mu(i, j)`**
- **Signature**: `MatGSO.get_mu(i, j)`
- **Description**: Get Gram-Schmidt coefficient μ_{i,j} = ⟨b_i, b^*_j⟩ / ||b^*_j||^2 for i > j.
- **Source**: `gso.pyx:220-240`

**`MatGSO.get_r(i, j)`**
- **Signature**: `MatGSO.get_r(i, j)`
- **Description**: Get coefficient r_{i,j} = ⟨b_i, b^*_j⟩ for i ≥ j.
- **Source**: `gso.pyx:260-290`

---

## 2. LLL Surface

### LLL Reduction

**`LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`**
- **Signature**: `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- **Description**: Run LLL reduction on integer matrix B. If U is provided, stores transformation matrix.
- **Constraints**: `delta` must satisfy `0.25 < delta ≤ 1`. `eta` must satisfy `0 ≤ eta < sqrt(delta)`.
- **Parameters**:
  - `method`: one of `'wrapper'`, `'proved'`, `'heuristic'`, `'fast'`, or `None`
  - `float_type`: `'double'`, `'long_double'`, `'dpe'`, `'mpfr'`, `'dd'`, `'qd'`
  - `precision`: bit precision for mpfr float type
- **Source**: `lll.pyx:550-622`

**`LLL.is_reduced(M, delta=0.99, eta=0.51)`**
- **Signature**: `LLL.is_reduced(M, delta=0.99, eta=0.51)`
- **Description**: Test if matrix M is LLL-reduced with parameters (delta, eta). May return False for LLL-reduced matrices if precision is too small.
- **Source**: `lll.pyx:624-692`

**`LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`**
- **Signature**: `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`
- **Description**: LLL reduction object constructor. Takes MatGSO object M.
- **Source**: `lll.pyx:46-70`

**`LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`**
- **Signature**: `LLL.Reduction.__call__(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`
- **Description**: Execute LLL reduction with given parameters.
- **Source**: `lll.pyx:215-305`

**`LLL.Reduction.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)`**
- **Signature**: `LLL.Reduction.size_reduction(kappa_min=0, kappa_end=-1, size_reduction_start=0)`
- **Description**: Perform size reduction only.
- **Source**: `lll.pyx:307-379`

**`LLL.Reduction.final_kappa`**
- **Signature**: `property LLL.Reduction.final_kappa`
- **Description**: Final kappa index after reduction.
- **Source**: `lll.pyx:381-419`

**`LLL.Reduction.zeros`**
- **Signature**: `property LLL.Reduction.zeros`
- **Description**: Number of zero vectors encountered.
- **Source**: `lll.pyx:461-499`

**`LLL.Reduction.nswaps`**
- **Signature**: `property LLL.Reduction.nswaps`
- **Description**: Number of swaps performed.
- **Source**: `lll.pyx:501-539`

---

## 3. BKZ Surface

### BKZ Reduction

**`BKZ.reduction(B, param, U=None, float_type=None, precision=0)`**
- **Signature**: `BKZ.reduction(B, param, U=None, float_type=None, precision=0)`
- **Description**: Run BKZ reduction on integer matrix B. `param` must be a `BKZ.Param` object.
- **Constraints**: Euclidean lattice reduction workflow; not an indefinite genus/isometry classifier.
- **Source**: `bkz.pyx` (main reduction function)

**`BKZ.Reduction(M, lll_obj, param)`**
- **Signature**: `BKZ.Reduction(M, lll_obj, param)`
- **Description**: BKZ reduction object constructor. Takes MatGSO object M, LLL object, and BKZ param.
- **Source**: `bkz.pyx:200-280`

**`BKZ.AutoAbort(M, num_rows, start_row=0)`**
- **Signature**: `BKZ.AutoAbort(M, num_rows, start_row=0)`
- **Description**: Utility class for aborting BKZ when slope no longer improves.
- **Source**: `bkz.pyx:51-165`

**`BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`**
- **Signature**: `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`
- **Description**: BKZ parameter object. `block_size` is the required parameter (2 ≤ block_size ≤ 500).
- **Constraints**: `delta` must satisfy `0.25 < delta ≤ 1`.
- **Source**: `bkz_param.pyx`

---

## 4. Enumeration / SVP / CVP

### Enumeration

**`Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`**
- **Signature**: `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`
- **Description**: Create enumeration object for SVP/CVP.
- **Source**: `enumeration.pyx`

**`Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`**
- **Signature**: `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`
- **Description**: Perform enumeration. Returns list of solutions.
- **Source**: `enumeration.pyx`

**`Enumeration.get_nodes(level=None)`**
- **Signature**: `Enumeration.get_nodes(level=None)`
- **Description**: Get enumeration node counts.
- **Source**: `enumeration.pyx`

### SVP

**`SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`**
- **Signature**: `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`
- **Description**: Find shortest non-zero vector in lattice.
- **Caveat**: `method='fast'` is heuristic; `method='proved'` is proof-oriented mode.
- **Source**: `svpcvp.pyx`

### CVP

**`CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`**
- **Signature**: `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`
- **Description**: Find closest vector to target t in lattice.
- **Caveat**: Practical CVP workflows assume LLL-preconditioned basis input.
- **Source**: `svpcvp.pyx`

**`CVP.babai(B, t, *args, **kwargs)`**
- **Signature**: `CVP.babai(B, t, *args, **kwargs)`
- **Description**: Babai's nearest plane algorithm for CVP.
- **Caveat**: Practical CVP workflows assume LLL-preconditioned basis input.
- **Source**: `svpcvp.pyx`

---

## 5. Pruning and Utilities

### Pruning

**`Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`**
- **Signature**: `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`
- **Description**: Compute pruning parameters.
- **Source**: `pruner.pyx`

### Utilities

**`fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`**
- **Signature**: `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`
- **Description**: Adjust enumeration radius to Gaussian heuristic bound.
- **Source**: `fpylll.util` module

**`fpylll.util.gaussian_heuristic(r)`**
- **Signature**: `fpylll.util.gaussian_heuristic(r)`
- **Description**: Compute Gaussian heuristic for radius r.
- **Source**: `fpylll.util` module

---

## Definiteness and Domain Caveat

fpylll is a Euclidean lattice reduction library. It does not expose indefinite arithmetic-form classification semantics (genus, spinor genus, signature-based classification). The methods operate on lattices as free modules with symmetric positive-definite bilinear forms (inner products), not on the broader class of indefinite bilinear-form lattices.

---

## References

- fpylll modules: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll repository: `https://github.com/fplll/fpylll`
- fpylll docs home: `https://fpylll.readthedocs.io/`
