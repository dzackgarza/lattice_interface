# SageMath Genus Reference
## `sage.quadratic_forms.genera.genus` — genus symbols for integral quadratic forms

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[INT]` | Defined over **ℤ** (integer-valued bilinear form) |
| `[EVEN]` | Requires or relates to **even** lattices |
| `[P2]` | Specific to the prime **p = 2** |
| `[PODD]` | Specific to **odd primes** |
| `[LOCAL]` | Local (p-adic) computation |
| `[GLOBAL]` | Global genus computation |

---

## Overview

A **genus** of an integral lattice groups lattices that are locally isometric at every prime and at infinity. SageMath represents genera via:

- **`Genus_Symbol_p_adic_ring`** — local genus symbol at a single prime p (Jordan decomposition data).
- **`GenusSymbol_global_ring`** — global genus symbol: a signature pair plus a list of local genus symbols at each relevant prime.

The module provides constructors, enumeration, validation, and representative-computation tools for the Conway–Sloane genus-symbol formalism.

---

## 1. Top-Level Functions — Constructors & Validation

| Function | Description | Tags |
|----------|-------------|------|
| `Genus(A, factored_determinant=None)` | Construct a global genus symbol from a symmetric Gram matrix `A` over ℤ. Optional pre-factored determinant speeds computation. Returns `GenusSymbol_global_ring`. | `[INT, ND, GLOBAL]` |
| `LocalGenusSymbol(A, p)` | Construct the local genus symbol of matrix `A` at prime `p`. Returns `Genus_Symbol_p_adic_ring`. | `[INT, ND, LOCAL]` |
| `genera(sig_pair, determinant, max_scale=None, even=False)` | Enumerate all global genera with given signature pair `(p, n)` and determinant. `max_scale` bounds the highest Jordan-block scale; `even=True` restricts to even lattices. | `[GLOBAL]` |
| `is_GlobalGenus(G)` | Check whether `G` (a `GenusSymbol_global_ring`) satisfies all local-global compatibility conditions (product formula, etc.). Returns `bool`. | `[GLOBAL]` |

---

## 2. Top-Level Functions — p-adic Symbol Computation

| Function | Description | Tags |
|----------|-------------|------|
| `p_adic_symbol(A, p, val)` | Compute the p-adic genus symbol of symmetric matrix `A` at odd prime `p`, using `val` as the p-adic valuation of the determinant. Returns list of triples `[scale, rank, determinant_square_class]`. | `[LOCAL, PODD]` |
| `two_adic_symbol(A, val)` | Compute the 2-adic genus symbol of symmetric matrix `A`, using `val` as the 2-adic valuation of the determinant. Returns list of quintuples `[scale, rank, det, sign, oddity]`. | `[LOCAL, P2]` |
| `is_2_adic_genus(symbol)` | Check whether a list of quintuples is a valid 2-adic genus symbol (rank, determinant, sign, and oddity constraints). Returns `bool`. | `[LOCAL, P2]` |

---

## 3. Top-Level Functions — Matrix Utilities

| Function | Description | Tags |
|----------|-------------|------|
| `signature_pair_of_matrix(A)` | Signature pair `(p, n)` of a symmetric real matrix `A` (number of positive and negative eigenvalues). | `[ND]` |
| `is_even_matrix(A)` | Test whether symmetric integer matrix `A` is even (all diagonal entries divisible by 2). Returns `(bool, int)` tuple: evenness flag and first odd diagonal entry (or 0). | `[INT, EVEN]` |

---

## 4. Helper / Internal Functions

| Function | Description | Tags |
|----------|-------------|------|
| `canonical_2_adic_reduction(symbol)` | Reduce a 2-adic genus symbol to canonical (normal) form in place, applying Conway–Sloane sign-walking rules. | `[LOCAL, P2]` |
| `canonical_2_adic_compartments(symbol)` | Return the list of compartment index-lists for a 2-adic symbol. Compartments are maximal runs of consecutive Jordan blocks with the same scale parity. | `[LOCAL, P2]` |
| `canonical_2_adic_trains(symbol)` | Return the list of train index-lists for a 2-adic symbol. Trains extend compartments by linking adjacent-scale blocks. | `[LOCAL, P2]` |
| `basis_complement(B)` | Given an echelonized matrix `B` with rows forming a subspace, return a matrix whose rows complete it to a full basis of the ambient space. | |
| `split_odd(A)` | Given a symmetric matrix `A` with odd diagonal, split off a 1-dimensional form: returns `(u, B)` where `u` is the odd unit and `B` is the complementary block. | `[P2]` |
| `trace_diag_mod_8(A)` | Trace of the diagonalization of symmetric integer matrix `A`, reduced mod 8. Used in oddity computations. | `[LOCAL, P2]` |

---

## 5. Class `Genus_Symbol_p_adic_ring` — Local Genus at Prime p

Represents the local genus symbol at a single prime p as a list of Jordan-block descriptors.

### 5.1 Structure & Access

| Method | Description | Tags |
|--------|-------------|------|
| `prime()` | Return the underlying prime `p`. | `[LOCAL]` |
| `is_even()` | Whether the represented lattice is even (meaningful mainly at p = 2). | `[LOCAL, EVEN]` |
| `symbol_tuple_list()` | Return the raw list of symbol tuples: triples `(scale, rank, det)` for odd p; quintuples `(scale, rank, det, sign, oddity)` for p = 2. | `[LOCAL]` |
| `canonical_symbol()` | Return the canonical form of the symbol. For p = 2, applies Conway–Sloane sign-walking; for odd p, the symbol is already canonical. | `[LOCAL]` |
| `number_of_blocks()` | Number of Jordan blocks in the decomposition. | `[LOCAL]` |

### 5.2 Invariants

| Method | Description | Tags |
|--------|-------------|------|
| `determinant()` | The p-part of the determinant of the form (product of p^(scale·rank) · det over blocks). | `[LOCAL]` |
| `det()` | Alias for `determinant()`. | `[LOCAL]` |
| `dimension()` | Total dimension (sum of ranks across Jordan blocks). | `[LOCAL]` |
| `dim()` | Alias for `dimension()`. | `[LOCAL]` |
| `rank()` | Alias for `dimension()`. | `[LOCAL]` |
| `excess()` | The p-excess of the symbol. For p = 2 this is the oddity value; for odd p it is computed from determinant and dimension. | `[LOCAL]` |
| `scale()` | Scale ideal of the lattice: the smallest `p^s` such that `p^s` divides all inner products. | `[LOCAL]` |
| `norm()` | Norm ideal of the lattice: the smallest `p^s` such that `p^s` divides all norms `q(x)`. | `[LOCAL]` |
| `level()` | Level of the local genus: maximal scale among Jordan components (as a power of p). | `[LOCAL]` |

### 5.3 Operations

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(other)` | Local genus symbol of the orthogonal direct sum with another `Genus_Symbol_p_adic_ring` at the same prime. | `[LOCAL]` |
| `gram_matrix(check=True)` | A Gram matrix (over ℤ_p) representing this local genus. If `check=True`, verifies the matrix reproduces the symbol. | `[LOCAL]` |
| `mass()` | Local mass factor `m_p` at this prime (the p-adic contribution to the Smith–Minkowski–Siegel mass formula). | `[LOCAL]` |
| `automorphous_numbers()` | Generators of the group of automorphous square classes at this prime (elements represented by the form modulo squares). | `[LOCAL]` |

### 5.4 2-adic Structure

| Method | Description | Tags |
|--------|-------------|------|
| `trains()` | Train decomposition indices for the 2-adic symbol (maximal linked runs of Jordan blocks). Raises error for odd p. | `[LOCAL, P2]` |
| `compartments()` | Compartment decomposition indices for the 2-adic symbol. Raises error for odd p. | `[LOCAL, P2]` |

---

## 6. Class `GenusSymbol_global_ring` — Global Genus

Represents a global genus: a signature pair together with local genus symbols at every relevant prime.

### 6.1 Signature & Invariants

| Method | Description | Tags |
|--------|-------------|------|
| `signature_pair()` | Return `(p, n)`: the number of positive and negative eigenvalues. | `[GLOBAL]` |
| `signature()` | Return `p − n` (the signature as a single integer). | `[GLOBAL]` |
| `determinant()` | Determinant of the genus (well-defined up to squares, returned as an integer). | `[GLOBAL]` |
| `det()` | Alias for `determinant()`. | `[GLOBAL]` |
| `dimension()` | Dimension (rank) of the lattice. | `[GLOBAL]` |
| `dim()` | Alias for `dimension()`. | `[GLOBAL]` |
| `rank()` | Alias for `dimension()`. | `[GLOBAL]` |
| `is_even()` | Whether the genus consists of even lattices (determined by the 2-adic symbol). | `[GLOBAL, EVEN]` |

### 6.2 Local Data

| Method | Description | Tags |
|--------|-------------|------|
| `local_symbols()` | List of `Genus_Symbol_p_adic_ring` objects, one per relevant prime. | `[GLOBAL]` |
| `local_symbol(p)` | The local genus symbol at prime `p`. If `p` does not divide the level, returns the trivial unimodular symbol. | `[GLOBAL, LOCAL]` |

### 6.3 Operations

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(other)` | Global genus of the orthogonal direct sum with another `GenusSymbol_global_ring`. | `[GLOBAL]` |
| `discriminant_form()` | The discriminant form (discriminant group with induced ℚ/ℤ-valued quadratic form) as a `TorsionQuadraticModule`. | `[GLOBAL, ND]` |
| `rational_representative()` | A diagonal matrix over ℚ in the rational equivalence class of this genus. | `[GLOBAL]` |

### 6.4 Representatives & Mass

| Method | Description | Tags |
|--------|-------------|------|
| `representative()` | An integral Gram matrix representing a lattice in this genus (typically the first computed class representative). | `[GLOBAL, INT]` |
| `representatives(backend=None, algorithm=None)` | All class representatives (Gram matrices) in the genus. `backend` and `algorithm` select the enumeration engine (e.g., `"Plesken"`, `"default"`). | `[GLOBAL, INT]` |
| `mass()` | The mass of the genus (Smith–Minkowski–Siegel mass: sum of 1/|Aut(L)| over isometry classes). | `[GLOBAL]` |
| `spinor_generators(proper)` | Generators of the spinor kernel at each relevant prime. `proper=True` uses SO, `proper=False` uses O. Returns a dict mapping primes to lists of generators. | `[GLOBAL]` |

---

## 7. Typical Workflow

```python
from sage.all import *

# 1. Build a genus from a Gram matrix
G = Matrix(ZZ, [[2, 1], [1, 2]])       # A2 root lattice
gen = Genus(G)

# 2. Inspect global invariants
gen.signature_pair()                     # (2, 0)
gen.determinant()                        # 3
gen.is_even()                            # True

# 3. Inspect local data
gen.local_symbols()                      # local symbols at p=2, p=3
gen.local_symbol(3).symbol_tuple_list()  # Jordan block data at 3

# 4. Enumerate all genera with same invariants
all_genera = genera((2, 0), 3, even=True)

# 5. Recover lattice representatives
gen.representative()                     # a Gram matrix in this genus
gen.representatives()                    # all class reps (one class for A2)
gen.mass()                               # mass = 1/|Aut(A2)| = 1/12

# 6. Discriminant form
gen.discriminant_form()                  # TorsionQuadraticModule ≅ ℤ/3ℤ
```

---

## 8. Key Mathematical Facts

- **Genus = local-global equivalence class.** Two integral lattices are in the same genus iff they are isometric over ℤ_p for every prime p and over ℝ.
- **Mass formula.** The Smith–Minkowski–Siegel mass is a product of local factors `m_p` times a gamma-factor contribution from the real place.
- **Even vs. odd.** A lattice is even iff all diagonal entries of its Gram matrix are even. The 2-adic symbol encodes evenness via the oddity component.
- **Spinor genus.** The spinor genus refines the genus; `spinor_generators()` computes the spinor kernel to distinguish spinor genera within a genus.
- **Conway–Sloane symbols.** The 2-adic genus symbol uses quintuples `(scale, rank, det, sign, oddity)` with sign-walking rules for canonicalization. Odd-prime symbols use triples `(scale, rank, det_square_class)`.
