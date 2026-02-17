# SageMath `QuadraticForm` Reference
## `sage.quadratic_forms.quadratic_form` — the quadratic form as an algebraic object

---

## Overview

A `QuadraticForm` represents a homogeneous degree-2 polynomial Q(x) = Σ a_ij x_i x_j (i ≤ j) over a commutative ring R. It is **not** a lattice or module — it is the form itself. The internal storage is the upper-triangular coefficient list of length n(n+1)/2.

Key relationships:
- **Hessian matrix** A: Q(x) = (1/2) xᵀ A x. Diagonal entries of A are 2·a_ii.
- **Gram matrix** G = (1/2) A: Q(x) = xᵀ G x. Requires 2-divisibility of diagonal Hessian entries (always true for forms constructed from upper-tri coefficients).

---

## 1. Construction

| Signature | Description |
|-----------|-------------|
| `QuadraticForm(R, n, entries)` | From ring R, dimension n, and upper-triangular coefficient list of length n(n+1)/2. Entries are ordered row-by-row: `[a_00, a_01, …, a_0(n-1), a_11, a_12, …]`. |
| `QuadraticForm(p)` | From a homogeneous degree-2 polynomial p in a multivariate polynomial ring. |
| `QuadraticForm(R, M)` | From ring R and symmetric matrix M with even diagonal. M is interpreted as the Hessian matrix. |
| `QuadraticForm(M)` | From symmetric matrix M; ring inferred from base ring of M. |
| `DiagonalQuadraticForm(R, diag)` | Diagonal form a₁x₁² + a₂x₂² + ⋯ over ring R. |
| `quadratic_form_from_invariants(F, rk, det, P, sminus)` | Reconstruct a rational quadratic form from its rational invariants (rank, determinant, finite anisotropic primes, negative signature). |
| `QuadraticForm.from_polynomial(poly)` | Class method; inverse of `polynomial()`. Constructs form from a multivariate polynomial. |

```python
QuadraticForm(ZZ, 2, [1, 3, 2])                # x² + 3xy + 2y²
QuadraticForm(ZZ, 3, [2, 1, 0, 2, 0, 2])       # 2x² + xy + 2y² + 2z²
DiagonalQuadraticForm(ZZ, [1, 1, 1])            # x² + y² + z²

R.<x,y> = QQ[]
QuadraticForm(x^2 + 3*x*y + 2*y^2)             # from polynomial

M = matrix(ZZ, [[2, 1], [1, 4]])
QuadraticForm(ZZ, M)                            # from Hessian matrix (even diagonal)

from sage.quadratic_forms.quadratic_form import quadratic_form_from_invariants
quadratic_form_from_invariants(QQ, 3, -1, [2], 1)
```

---

## 2. Basic Accessors

| Method | Returns | Description |
|--------|---------|-------------|
| `dim()` | `Integer` | Number of variables (= rank of the form). |
| `base_ring()` | `Ring` | Coefficient ring R. |
| `coefficients()` | `list` | Upper-triangular coefficient list [a_00, a_01, …, a_11, …]. |
| `det()` | element of R | Determinant of the Hessian matrix (= 2ⁿ · det(Gram)). |
| `Gram_det()` | element of R | Determinant of the Gram matrix. |
| `gcd()` | element of R | GCD of all coefficients. |

```python
Q = QuadraticForm(ZZ, 2, [1, 3, 2])
Q.dim()              # 2
Q.base_ring()        # Integer Ring
Q.coefficients()     # [1, 3, 2]
Q.det()              # det of Hessian matrix
Q.Gram_det()         # det of Gram matrix
Q.gcd()              # gcd(1, 3, 2) = 1
```

---

## 3. Matrix Representations

| Method | Returns | Description |
|--------|---------|-------------|
| `matrix()` | `Matrix` | Hessian matrix A such that Q(x) = (1/2) xᵀ A x. Synonym: `Hessian_matrix()`. |
| `Hessian_matrix()` | `Matrix` | Same as `matrix()`. |
| `Gram_matrix()` | `Matrix` | Gram matrix G = (1/2) A over the base ring (requires even diagonal in Hessian). |
| `Gram_matrix_rational()` | `Matrix` | Gram matrix over the fraction field of R. Always exists. |
| `has_integral_Gram_matrix()` | `bool` | True if the Gram matrix has entries in the base ring. |

```python
Q = QuadraticForm(ZZ, 2, [2, 2, 2])
Q.matrix()                    # [[4, 2], [2, 4]]  (Hessian)
Q.Gram_matrix()               # [[2, 1], [1, 2]]
Q.Gram_matrix_rational()      # [[2, 1], [1, 2]] over QQ
Q.has_integral_Gram_matrix()  # True
```

---

## 4. Polynomial and Evaluation

| Method | Returns | Description |
|--------|---------|-------------|
| `polynomial(names='x')` | `MPolynomial` | Multivariate polynomial representation of Q. Variable names default to `x0, x1, …`. |
| `bilinear_map(v, w)` | element of R | Associated symmetric bilinear form B(v,w) = Q(v+w) − Q(v) − Q(w). |
| `__call__(v)` | element of R or `QuadraticForm` | If v is a vector, evaluates Q(v). If v is a matrix A, returns the form Q∘A (change of variables). |

```python
Q = QuadraticForm(ZZ, 2, [1, 0, 1])   # x² + y²
Q.polynomial()                          # x0^2 + x1^2
Q(vector([3, 4]))                       # 25
Q(matrix(ZZ, 2, 2, [1, 1, 0, 1]))      # change of variables: x² + 2xy + 2y²
```

---

## 5. Local Invariants

| Method | Returns | Description |
|--------|---------|-------------|
| `hasse_invariant(p)` | `±1` | Hasse–Minkowski invariant at prime p (Cassels convention). |
| `hasse_invariant__OMeara(p)` | `±1` | Hasse invariant using O'Meara's convention. |
| `signature()` | `Integer` | Signature = n₊ − n₋ (number of positive minus negative eigenvalues over ℝ). |
| `signature_vector()` | `(n₊, n₋, n₀)` | Full signature vector including nullity. |
| `anisotropic_primes()` | `list` | List of primes where the form is anisotropic. |
| `is_isotropic(p)` | `bool` | True if the form is isotropic at prime p (or over ℝ if p = ∞). |
| `is_anisotropic(p)` | `bool` | True if the form is anisotropic at prime p. |
| `is_hyperbolic(p)` | `bool` | True if the form is hyperbolic at prime p. |
| `rational_diagonal_form()` | `QuadraticForm` | Diagonalization over the fraction field. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
Q.hasse_invariant(2)            # ±1
Q.signature()                   # 3
Q.signature_vector()            # (3, 0, 0)
Q.anisotropic_primes()          # []
Q.rational_diagonal_form()      # <1> + <1> + <1>
```

---

## 6. Definiteness

| Method | Returns | Description |
|--------|---------|-------------|
| `is_positive_definite()` | `bool` | True if Q(x) > 0 for all x ≠ 0. |
| `is_negative_definite()` | `bool` | True if Q(x) < 0 for all x ≠ 0. |
| `is_definite()` | `bool` | True if positive or negative definite. |
| `is_indefinite()` | `bool` | True if neither positive nor negative definite. |
| `compute_definiteness()` | `str` | Computes and caches definiteness; returns string descriptor. |
| `compute_definiteness_string_by_determinants()` | `str` | Determines definiteness by checking signs of leading principal minors. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, -1])
Q.is_positive_definite()    # False
Q.is_indefinite()           # True
```

---

## 7. Level and Primitivity

| Method | Returns | Description |
|--------|---------|-------------|
| `level()` | `Integer` | Level of the quadratic form (smallest N such that N·G⁻¹ is integral with even diagonal). |
| `level_ideal()` | `Ideal` | Level as an ideal of the base ring. |
| `is_primitive()` | `bool` | True if gcd of coefficients is 1. |
| `primitive()` | `QuadraticForm` | Scaled copy with gcd divided out. |
| `adjoint_primitive()` | `QuadraticForm` | Primitive adjoint form. |
| `change_ring(R)` | `QuadraticForm` | Base change to ring R. |

```python
Q = QuadraticForm(ZZ, 2, [2, 4, 6])
Q.is_primitive()     # False (gcd = 2)
Q.primitive()        # QuadraticForm with coefficients [1, 2, 3]
Q.change_ring(QQ)    # same form over QQ
Q.level()            # level of the form
```

---

## 8. Reduction Theory

| Method | Returns | Description |
|--------|---------|-------------|
| `lll()` | `QuadraticForm` | LLL-reduced equivalent form (ternary: uses Tornaria's method). |
| `minkowski_reduction()` | `QuadraticForm` | Minkowski-reduced form (small dimensions). |
| `minkowski_reduction_for_4vars__SP()` | `QuadraticForm` | Minkowski reduction specialized for 4-variable forms (Schiemann–Pall). |
| `reduced_binary_form()` | `QuadraticForm` | Classical reduced form for binary (dim 2) quadratic forms. |
| `reduced_binary_form1()` | `QuadraticForm` | Alternate binary reduction algorithm. |
| `reduced_ternary_form__Dickson()` | `QuadraticForm` | Ternary reduction following Dickson's algorithm. |

```python
Q = QuadraticForm(ZZ, 3, [5, 4, 3, 5, 2, 5])
Q_red = Q.lll()                       # LLL-reduced form
Q_red.Gram_matrix()                   # smaller entries

Q2 = QuadraticForm(ZZ, 2, [10, 6, 5])
Q2.reduced_binary_form()              # classically reduced binary form
```

---

## 9. Theta Series

| Method | Returns | Description |
|--------|---------|-------------|
| `theta_series(var, prec)` | power series | Theta series Θ_Q(q) = Σ q^{Q(x)} via PARI. `var` is the variable name, `prec` is precision. |
| `theta_by_cholesky(q_prec)` | `list` | Representation numbers via Cholesky decomposition, up to precision `q_prec`. |
| `theta_by_pari(prec)` | power series | Theta series computed directly via PARI's `qfrep`. |
| `theta_series_degree_2(prec)` | dict | Degree-2 Siegel theta series coefficients up to given precision. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
Q.theta_series(var='q', prec=20)       # 1 + 8*q + 24*q^2 + ...
Q.theta_by_cholesky(10)                # [1, 8, 24, 32, 24, ...]
Q.theta_by_pari(20)                    # via PARI
```

---

## 10. Enumeration and Automorphisms

| Method | Returns | Description |
|--------|---------|-------------|
| `short_vector_list_up_to_length(n)` | `list[list]` | Lists of short vectors grouped by norm, for norms 0, 1, …, n−1. Uses PARI. |
| `short_primitive_vector_list_up_to_length(n)` | `list[list]` | Same, but restricted to primitive vectors (gcd of entries = 1). |
| `automorphism_group()` | `MatrixGroup` | Full automorphism group Aut(Q) as a matrix group. |
| `automorphisms()` | `list[Matrix]` | List of automorphism matrices. |
| `number_of_automorphisms()` | `Integer` | \|Aut(Q)\|. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1])
Q.short_vector_list_up_to_length(5)     # vectors with Q(x) < 5
Q.number_of_automorphisms()             # 8 (dihedral group of square)
Q.automorphism_group()                  # matrix group of order 8
```

---

## 11. Equivalence Testing

### Global, Local, and Rational Isometry

| Method | Returns | Description |
|--------|---------|-------------|
| `is_globally_equivalent_to(other)` | `bool` or `Matrix` | Tests GL_n(ℤ) equivalence. Returns transformation matrix if equivalent. |
| `is_locally_equivalent_to(other, p)` | `bool` | Tests equivalence over ℤ_p (p-adic integers). |
| `is_rationally_isometric(other)` | `bool` | Tests equivalence over ℚ (Hasse–Minkowski). |

```python
Q1 = DiagonalQuadraticForm(ZZ, [1, 1])
Q2 = QuadraticForm(ZZ, 2, [1, 0, 1])
Q1.is_globally_equivalent_to(Q2)       # True (same form)
Q1.is_rationally_isometric(Q2)         # True
```

### Local Jordan Decomposition Helpers

| Method | Returns | Description |
|--------|---------|-------------|
| `local_normal_form(p)` | `QuadraticForm` | Returns a locally equivalent Jordan-normal form over ℤ_p; upstream warning: currently only for forms over `ZZ`. |
| `jordan_blocks_by_scale_and_unimodular(p, safe_flag=True)` | `list[tuple[int, QuadraticForm]]` | Returns Jordan components grouped by scale exponent with unimodular block forms; decomposition into smaller blocks is not unique. |
| `jordan_blocks_in_unimodular_list_by_scale_power(p)` | `list[QuadraticForm]` | Returns a scale-indexed list of p-unimodular Jordan components; upstream caveat: defined for integer-valued forms, and for `p=2` indexing is guaranteed only with integer Gram matrix. |
| `has_equivalent_Jordan_decomposition_at_prime(other, p)` | `bool` | Tests whether Q and `other` have equivalent Jordan decompositions at prime `p`. |

```python
Q = QuadraticForm(ZZ, 2, [10, 4, 1])
Q.local_normal_form(5)
Q.jordan_blocks_by_scale_and_unimodular(5)
```

---

## 12. Genus and Mass

| Method | Returns | Description |
|--------|---------|-------------|
| `global_genus_symbol()` | `GenusSymbol_global_ring` | Complete genus symbol over ℤ. |
| `local_genus_symbol(p)` | `Genus_Symbol_p_adic_ring` | Local genus symbol at prime p. |
| `CS_genus_symbol_list()` | `list` | Conway–Sloane genus symbol list. |
| `genera(sig_pair, det, ...)` | `list` | (Static/module-level) Enumerate all genera with given signature pair and determinant. |
| `mass__by_Siegel_densities()` | `Rational` | Mass of the genus computed via Siegel's density formula. |
| `conway_mass()` | `Rational` | Mass via Conway–Sloane tables. |
| `conway_standard_mass()` | `Rational` | Conway–Sloane "standard" mass. |
| `siegel_product()` | `Rational` | Siegel product (product of local densities). |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
Q.global_genus_symbol()
Q.local_genus_symbol(2)
Q.mass__by_Siegel_densities()
```

---

## 13. Local Densities and Congruence Helpers

| Method | Returns | Description |
|--------|---------|-------------|
| `local_density(p, m)` | `Rational` | Local density of representing m at prime p; upstream notes this wrapper enforces a local-normal-form precondition internally before density computation. |
| `local_primitive_density(p, m)` | `Rational` | Local primitive density of representing m at prime p; upstream notes this wrapper enforces a local-normal-form precondition internally before primitive-density computation. |
| `local_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Local density with congruence filters; upstream assumes a block-diagonal, `p`-integral form and uses `Zvec`/`NZvec` as non-repeating index lists in `range(self.dim())` (or `None`). |
| `local_primitive_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Primitive local density with congruence filters; same block-diagonal and `p`-integral assumptions, and upstream notes this routine is included for consistency rather than internal use. |
| `local_good_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Good-type contribution to congruence density decomposition; upstream assumes a block-diagonal, `p`-integral form and `Zvec`/`NZvec` index-list semantics as above. |
| `local_bad_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Bad-type contribution to congruence density decomposition; upstream assumes a block-diagonal, `p`-integral form and `Zvec`/`NZvec` index-list semantics as above. |
| `local_badI_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Type-I bad contribution used in congruence-density decompositions; upstream assumes a block-diagonal, `p`-integral form and `Zvec`/`NZvec` index-list semantics. |
| `local_badII_density_congruence(p, m, Zvec=None, NZvec=None)` | `Rational` | Type-II bad contribution used in congruence-density decompositions; upstream assumes a block-diagonal, `p`-integral form and `Zvec`/`NZvec` index-list semantics. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
Q.local_density(2, 1)             # local density of representing 1 at p=2
Q.local_primitive_density(3, 6)   # primitive local density at p=3
Q.local_density_congruence(2, 1, None, None)
Q.local_primitive_density_congruence(3, 1, None, None)
```

Source note: contracts above were reconciled against `docs/sage/quadratic_form/upstream/quadratic_form.html` and the current upstream page `https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/quadratic_form.html` (accessed 2026-02-17).

---

## 14. Representability

| Method | Returns | Description |
|--------|---------|-------------|
| `local_representation_conditions(...)` | `RepresentationConditions` | Computes local conditions for representability of integers by Q. |
| `is_locally_universal_at_prime(p)` | `bool` | True if Q locally represents all p-adic integers. |
| `is_locally_universal_at_all_primes()` | `bool` | True if Q is locally universal at every finite prime. |
| `is_locally_universal_at_all_places()` | `bool` | True if Q is locally universal at all places (including ∞). |
| `is_locally_represented_number(m)` | `bool` | True if m is locally represented by Q at all places. |
| `is_locally_represented_number_at_place(m, p)` | `bool` | True if m is locally represented by Q at place p. |
| `solve(n)` | `vector` or `None` | Find x such that Q(x) = n, or None if no solution exists. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
Q.is_locally_universal_at_all_primes()
Q.is_locally_represented_number(7)       # True
Q.solve(14)                              # e.g., (1, 2, 3)
```

---

## 15. Neighbors

| Method | Returns | Description |
|--------|---------|-------------|
| `find_p_neighbor_from_vec(p, v)` | `QuadraticForm` | Compute the p-neighbor of Q determined by isotropic vector v mod p. |
| `neighbor_iteration(p, ...)` | `list[QuadraticForm]` | Iterate over all p-neighbors; used to enumerate genus representatives. |

```python
Q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
v = vector([1, 0, 0, 0])
Q.find_p_neighbor_from_vec(2, v)
```

---

## 16. Ternary-Specific Methods (Tornaria)

Specialized methods for ternary (dim = 3) quadratic forms, following Tornaria's algorithms.

| Method | Returns | Description |
|--------|---------|-------------|
| `disc()` | `Integer` | Discriminant of the ternary form. |
| `content()` | `Integer` | Content (gcd of the "matrix entries" in ternary sense). |
| `adjoint()` | `QuadraticForm` | Adjoint (classical adjoint / adjugate form). |
| `antiadjoint()` | `QuadraticForm` | Inverse of the adjoint operation (when it exists). |
| `reciprocal()` | `QuadraticForm` | Reciprocal form (related to adjoint by scaling). |
| `omega()` | `Integer` | Omega invariant. |
| `delta()` | `Integer` | Delta invariant. |
| `xi()` | `Integer` | Xi invariant (Tornaria). |
| `xi_rec()` | `Integer` | Xi of the reciprocal form. |
| `clifford_invariant()` | element | Clifford invariant (quaternion algebra class). |
| `clifford_conductor()` | `Integer` | Conductor of the Clifford invariant. |
| `hasse_conductor()` | `Integer` | Hasse conductor of the ternary form. |
| `representation_number_list(B)` | `list` | List of representation numbers r_Q(n) for n = 0, 1, …, B−1. |
| `representation_vector_list(B)` | `list[list]` | List of representation vectors for n = 0, 1, …, B−1. |

```python
Q = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 1])   # x² + y² + z²
Q.disc()                      # 4
Q.adjoint()                   # adjoint ternary form
Q.clifford_invariant()
Q.representation_number_list(20)   # [1, 6, 12, 8, 6, 24, ...]
```

---

## 17. Variable Substitutions

| Method | Returns | Description |
|--------|---------|-------------|
| `swap_variables(i, j)` | `QuadraticForm` | Swap variables x_i and x_j. |
| `multiply_variable(i, s)` | `QuadraticForm` | Replace x_i → s·x_i. |
| `divide_variable(i, s)` | `QuadraticForm` | Replace x_i → x_i/s (requires divisibility). |
| `add_symmetric(i, j, s)` | `QuadraticForm` | Replace x_i → x_i + s·x_j (and symmetrically). |
| `extract_variables(v)` | `QuadraticForm` | Extract a sub-form using only the variables indexed by list v. |
| `scale_by_factor(s)` | `QuadraticForm` | Multiply the entire form by scalar s. |

```python
Q = QuadraticForm(ZZ, 3, [1, 2, 3, 4, 5, 6])
Q.swap_variables(0, 2)            # swap x₀ and x₂
Q.multiply_variable(1, 3)         # x₁ → 3x₁
Q.extract_variables([0, 2])       # sub-form in x₀, x₂
Q.scale_by_factor(2)              # 2·Q
```

---

## Cross-References

- **`IntegralLattice`** wraps a Gram matrix as a lattice module; to convert: `IntegralLattice(Q.Gram_matrix())` (requires integral Gram matrix).
- **`BinaryQF(a,b,c)`** — specialized binary form class with class group methods; related but separate hierarchy.
- **`TernaryQF(coeffs)`** — specialized ternary form class; overlaps with ternary methods above.
- **Full lattice reference**: see [`sagemath_lattice_reference.md`](sagemath_lattice_reference.md).
