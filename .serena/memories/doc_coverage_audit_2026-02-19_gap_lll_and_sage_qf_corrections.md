# Doc Coverage Audit Corrections (2026-02-19, follow-up pass)

## State Summary
- Goal 1: COMPLETE
- Goal 2: COMPLETE (with two corrections applied in this pass)

## Corrections Made

### 1. GAP Core Reference — LLL and Short-Vector Sections

**File**: `docs/gap/lattice/gap_lattice_methods_reference.md`

**Problem**: Sections 1.2 and 1.3 were still in 3-column format (`Function | Description | Tags`) with `LLLReducedBasis(...)` as an uninformative placeholder. Previous completion memories incorrectly claimed GAP sections had typed reference tables.

**Fix**: Converted sections 1.2 and 1.3 to 5-column format (`Function | Argument Types | Return Type | Description | Tags`). Source: `docs/gap/upstream/chap25.html` (GAP Reference Manual §25.5-1, §25.5-2, §25.6-1, §25.6-2).

**`LLLReducedBasis([L, ]vectors[, y][, "linearcomb"][, lllout])`**:
- `L` optional lattice with `ScalarProduct`; `vectors` list of vectors; `y` rational in `(1/4,1]`, default `3/4`; `"linearcomb"` string flag for linear combination data; `lllout` record for incremental calls
- Returns: record with `.basis`, `.mue`, `.B`; if `"linearcomb"`: also `.relations`, `.transformation`

**`LLLReducedGramMat(G[, y])`**:
- `G` square symmetric integer Gram matrix; `y` optional Lovász parameter, default `3/4`
- Returns: record with `.remainder` (reduced Gram), `.mue`, `.B`, `.relations`, `.transformation` (unimodular U s.t. U*G*TransposedMat(U) = .remainder)

**`ShortestVectors(G, m[, "positive"])`**:
- `G` regular symmetric integer bilinear-form matrix; `m` nonneg integer bound
- Returns: record with `.vectors` (one per {x,-x} pair), `.norms`

**`OrthogonalEmbeddings(gram[, "positive"][, maxdim])`**:
- `gram` PD integer matrix; optional string flag and dim bound
- Returns: record with `.vectors` (rows satisfying v*gram^{-1}*v^tr ≤ 1), `.norms`, `.solutions`

**Commit**: `0057674`

---

### 2. SageMath QuadraticForm Reference — local_representation_conditions

**File**: `docs/sage/quadratic_form/sage_quadratic_form_reference.md`

**Problem**: 
- Argument Types was `—` but method actually has `recompute_flag=False, silent_flag=False`
- Return type was `RepresentationConditions` but correct class is `LocalRepresentationConditions`
- Critical constraint missing: only correct for forms in ≥3 variables locally universal at almost all primes

**Fix**: Updated from upstream `docs/sage/quadratic_form/upstream/quadratic_form.html`.

**Commit**: `73ded40`

---

## Remaining Known Gaps (No Source-Backed Fix Available)

1. `is_saturated_with_saturation(...)` in Julia reference (§2.17): "Varies" for argument types — no definitive upstream source for the full signature found
2. Julia reference sections 1, 5, 6 (Indefinite.jl, LLLplus.jl, LatticeAlgorithms.jl): 3-column format — experimental/unregistered packages without formal API docs
3. GAP HyperCells methods: `(...)` placeholders — consistent with playbook guidance for packages where manual doesn't expose compact signatures
4. g6k `SieverParams(...)`, `load_siever_params(...)`: no formal API docs for parameter helpers
