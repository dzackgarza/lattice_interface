# Julia Lattice Methods Reference
## Lattice = free ℤ-module with symmetric bilinear form

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Requires or only meaningful for **positive definite** forms |
| `[ND]` | Requires **non-degenerate** bilinear form |
| `[INDEF]` | Works correctly for **indefinite** signatures |
| `[DEG]` | Works with **degenerate** forms |
| `[EUCLID]` | Uses ambient Euclidean norm I_n; bilinear form not independently specified |
| `[GAP]` | Delegates to **GAP** |
| `[FLINT]` | Delegates to **FLINT** (via Nemo) |

---

## 1. Indefinite.jl

`[INDEF]` — Integral indefinite quadratic forms. Isometry classification and orbit enumeration under $GL(n,\mathbb{Z})$. ~90% GAP code. Not a registered package (install via GitHub URL).

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `INDEF_FORM_TestEquivalence(Q1, Q2)` | Test $GL(n,\mathbb{Z})$-equivalence of two indefinite forms; returns explicit unimodular transformation if equivalent | `[INDEF, GAP]` |
| `INDEF_FORM_AutomorphismGroup(Q)` | Finite generating set for $\text{Aut}(L)$ of an indefinite form ($O(L)$ often infinite) | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbitRepresentative(Q, C)` | Representatives (mod Aut) of integer solutions to $Q[v]=C$; $C=0$ gives primitive isotropic vectors | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)` | Orbit reps of $k$-dim totally isotropic subspaces, $k \le \min(p,q)$ | `[INDEF, GAP]` |
| `INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)` | Orbit reps of isotropic flags of length $k$ | `[INDEF, GAP]` |

### Definiteness

- Assumes mixed signature (at least one positive and one negative direction)
- Not optimized for PD lattices; use Hecke/Oscar instead
- PD automorphism groups are finite and have no nonzero isotropic vectors — qualitatively different
- Algorithms exploit structure of indefinite forms: reduction to computations on finite quadratic modules, subgroup algorithms in GAP
- For PD lattices, traditional invariants (genus, theta series) and neighbor methods suffice; Indefinite.jl tackles the harder indefinite regime

### References

- Dutour Sikirić et al.; applied to K3 surface lattices and Enriques surfaces moduli
- Sengun–Sikiric (automorphism groups of lattices)

---

## 2. Hecke.jl (via Oscar)

Comprehensive number theory package (part of OSCAR). Builds on Nemo/FLINT and GAP. Handles PD, ND, and indefinite lattices, plus hermitian lattices over number fields.

### 2.1 Types

| Type | Description | Tags |
|------|-------------|------|
| `ZZLat` | Integral quadratic lattice over ℤ | `[INT, ND]` |
| `QuadLat` | Quadratic lattice over ℚ or number field | `[ND]` |
| `HermLat` | Hermitian lattice over quadratic extension | `[ND]` |
| `ZZGenus` | Genus symbol of an integer lattice | |
| `ZZLocalGenus` | Local genus symbol at a prime $p$ | |
| `TorQuadModule` | Torsion quadratic module (finite quadratic form on $L^\vee/L$) | |
| `QuadSpace` | Quadratic space over a field | |
| `HermSpace` | Hermitian space over a quadratic extension | |
| `ZZLatWithIsom` | Integer lattice paired with a finite-order isometry | |
| `QuadSpaceWithIsom` | Quadratic space paired with an isometry | |

### 2.2 Quadratic and hermitian spaces

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space(K, n)` / `quadratic_space(K, G)` | Quadratic space from dimension or Gram matrix | |
| `hermitian_space(E, n)` / `hermitian_space(E, G)` | Hermitian space from dimension or Gram matrix | |
| `rank(V)` / `dim(V)` | Rank / dimension | |
| `gram_matrix(V)` / `gram_matrix(V, M)` | Gram matrix (optionally on subspace $M$) | |
| `det(V)` / `discriminant(V)` | Determinant / discriminant | |
| `diagonal(V)` | Diagonal entries after diagonalization | |
| `diagonal_with_transform(V)` | Diagonal + transformation matrix | |
| `orthogonal_basis(V)` | Orthogonal basis | |
| `signature_tuple(V)` | $(p, n)$ | `[INDEF ok]` |
| `is_regular(V)` | Non-degeneracy | |
| `is_quadratic(V)` / `is_hermitian(V)` | Type check | |
| `is_positive_definite(V)` / `is_negative_definite(V)` / `is_definite(V)` | Definiteness | |
| `hasse_invariant(V, p)` / `witt_invariant(V, p)` | Local invariants | |
| `invariants(V)` | All rational invariants (dim, det, signatures, Hasse) | |
| `is_isometric(V, W)` / `is_isometric(V, W, p)` | Global / local isometry test | |
| `is_locally_represented_by(U, V, p)` | Whether $U$ is locally represented by $V$ | |
| `is_represented_by(U, V)` | Whether $U$ is globally represented by $V$ | |
| `inner_product(V, v, w)` | Evaluate bilinear form | |
| `orthogonal_complement(V, M)` | Orthogonal complement of subspace $M$ | |
| `orthogonal_projection(V, M)` | Projection onto subspace $M$ | |
| `is_isotropic(V, p)` | Local isotropy test | |
| `is_locally_hyperbolic(V, p)` | Whether $V_p$ is hyperbolic (hermitian spaces) | |
| `restrict_scalars(V, K, α)` | Restriction of scalars | |
| `direct_sum(V, W)` / `direct_product` / `biproduct` | Categorical constructions | |

### 2.3 Construction

| Function | Description | Tags |
|----------|-------------|------|
| `integer_lattice(; gram=G)` | Integer lattice from Gram matrix | |
| `integer_lattice(B; gram=G)` | Integer lattice from basis matrix $B$ and optional Gram | |
| `lattice(V, B)` | Lattice in quadratic space $V$ with basis matrix $B$ | |
| `quadratic_lattice(K, gens; gram=M)` | Lattice from generators + Gram matrix; `K=QQ` → `ZZLat` | `[INDEF ok]` |
| `hermitian_lattice(E, gens; gram=M)` | Hermitian lattice over quadratic extension E | |
| `root_lattice(:A, n)` / `(:D, n)` / `(:E, n)` / `(:I, n)` | Named root lattice | `[PD]` |
| `hyperbolic_plane_lattice(n)` | Hyperbolic plane $U$ scaled by $n$ | `[INDEF]` |
| `leech_lattice()` | Rank-24 Leech lattice | `[PD]` |
| `k3_lattice()` | K3 surface lattice $U^3 \oplus E_8(-1)^2$ | `[INDEF]` |
| `mukai_lattice()` | Rank-24 Mukai lattice (K3 theory); optional extended form | `[INDEF]` |
| `hyperkaehler_lattice(:K3, n=3)` | Hyperkähler intersection form (sig $(3,19)$ or similar) | `[INDEF]` |
| `rescale(L, r)` | New lattice with Gram $r \cdot G$; use `rescale(L, -1)` to flip sign of ND lattice | |

### 2.4 Intrinsic data

| Method | Description | Tags |
|--------|-------------|------|
| `gram_matrix(L)` | Gram matrix | |
| `basis_matrix(L)` | Basis matrix | |
| `ambient_space(L)` | Ambient quadratic space | |
| `rational_span(L)` | Rational span as quadratic space | |
| `rank(L)` | Rank | |
| `degree(L)` | Degree (ambient dimension) | |
| `signature_tuple(L)` | $(n_{+}, n_{0}, n_{-})$ (positive, zero, negative counts) | `[INDEF ok]` |
| `det(L)` | Determinant of Gram | |
| `discriminant(L)` | Discriminant | |
| `scale(L)` | Scale ideal (generated by $b(x,y)$ for all $x,y \in L$) | |
| `norm(L)` | Norm ideal (generated by $q(x)$ for all $x \in L$) | |
| `is_positive_definite(L)` | | `[PD]` |
| `is_negative_definite(L)` | | |
| `is_definite(L)` | PD or ND | |
| `is_even(L)` | All $(x,x) \in 2\mathbb{Z}$ | |
| `is_integral(L)` | All $b(x,y) \in \mathbb{Z}$ | |
| `is_unimodular(L)` | $|\det G| = 1$ | |
| `is_primary(L, p)` | $L^\vee/L$ is a $p$-group | |
| `is_primary_with_prime(L)` | Returns `(true, p)` if primary | |
| `is_elementary(L, p)` | $L^\vee/L \cong (\mathbb{Z}/p)^k$ | |
| `is_elementary_with_prime(L)` | Returns `(true, p)` if elementary | |

### 2.5 Reduction

| Method | Description | Tags |
|--------|-------------|------|
| `lll(L::ZZLat; same_ambient=true)` | LLL-reduced basis; returns new lattice | `[INDEF ok, FLINT]` |

- PD: specify Lovász parameters via `LLLContext(δ, η)`
- INDEF: runs but "shorter" is w.r.t. a majorant, not the indefinite form itself

### 2.6 Vector enumeration

| Method | Description | Tags |
|--------|-------------|------|
| `short_vectors(L, lb, ub)` | Nonzero vectors with $lb \le \|v\|^2 \le ub$ (up to sign) | `[PD]` |
| `short_vectors_iterator(L, lb, ub)` | Lazy iterator version of `short_vectors` | `[PD]` |
| `shortest_vectors(L)` | Shortest vectors and their squared norm | `[PD]` |
| `close_vectors(L, v, ub; lb=0, check=true)` | Lattice points $x$ with $b(v-x, v-x) \le ub$; Fincke–Pohst enumeration | `[PD]` |
| `short_vectors_affine(S, v, α, d)` | Vectors $x \in S$ with $x^2 = d$ and $x \cdot v = \alpha$ (Vinberg) | `[INDEF]` |
| `vectors_of_square_and_divisibility(L, n, d)` | Vectors $v$ with $v^2 = n$ and divisibility $d$ in $L$ | `[PD]` |
| `enumerate_quadratic_triples(L, ...)` | Enumerate quadratic solutions in lattice | `[PD]` |
| `minimum(L)` | Squared length of shortest nonzero vector | `[PD]` |
| `kissing_number(L)` | Number of shortest vectors | `[PD]` |

- ND lattices: use `rescale(L, -1)` then enumerate (no scalar rescaling makes INDEF → PD)
- INDEF: `short_vectors` / `shortest_vectors` refuse; use `short_vectors_affine` or genus methods
- `close_vectors` with `check=false` runs on INDEF but result is ill-posed (distances can be negative/zero)

### 2.7 Genus and classification

#### ZZGenus methods

| Method | Description | Tags |
|--------|-------------|------|
| `genus(L::ZZLat)` | `ZZGenus` — genus symbol (local invariants at all primes) | `[INDEF ok]` |
| `genus(A::MatElem)` | Genus from Gram matrix | `[INDEF ok]` |
| `genus(L, p)` | Local genus `ZZLocalGenus` at prime $p$ | |
| `integer_genera(sig, det; ...)` | Enumerate all genus symbols with given signature and determinant | |
| `direct_sum(G1::ZZGenus, G2::ZZGenus)` | Genus of the orthogonal direct sum | |
| `representative(gen)` | Concrete lattice for a genus class | |
| `representatives(gen)` | All classes in genus | |
| `mass(gen)` | Mass of the genus | |
| `dim(gen)` / `rank(gen)` | Dimension / rank of genus | |
| `signature(gen)` | Signature pair | |
| `det(gen)` | Determinant | |
| `iseven(gen)` | Evenness | |
| `is_definite(gen)` | Definiteness | |
| `level(gen)` | Level | |
| `scale(gen)` / `norm(gen)` | Scale / norm of genus | |
| `primes(gen)` | List of primes appearing in local symbols | |
| `is_integral(gen)` | Integrality | |
| `local_symbol(gen, p)` | Retrieve `ZZLocalGenus` at prime $p$ | |
| `quadratic_space(gen)` | Quadratic space representing the genus | |
| `rational_representative(gen)` | Rational form | |
| `rescale(gen, a)` | Rescaled genus | |
| `represents(G1, G2)` | Whether genus $G_1$ represents $G_2$ | |

#### ZZLocalGenus methods

| Method | Description | Tags |
|--------|-------------|------|
| `prime(S)` | Underlying prime | |
| `iseven(S)` | Evenness at $p$ | |
| `symbol(S, scale)` | Jordan block invariants | |
| `hasse_invariant(S)` | Hasse invariant | |
| `det(S)` / `dim(S)` / `rank(S)` | Determinant / dimension / rank | |
| `excess(S)` | $p$-excess | |
| `signature(S)` | $p$-signature | |
| `oddity(S)` | 2-adic oddity | |
| `scale(S)` / `norm(S)` / `level(S)` | Scale / norm / level | |
| `representative(S)` / `gram_matrix(S)` | Representative lattice / Gram | |
| `rescale(S, a)` | Rescaled local genus | |
| `direct_sum(S1, S2)` | Local genus direct sum | |
| `represents(S1, S2)` | Local representation check | |

#### Discriminant group and classification

| Method | Description | Tags |
|--------|-------------|------|
| `discriminant_group(L)` | $L^\vee / L$ as `TorQuadModule` | |
| `genus_representatives(L)` | All isometry class representatives in the genus of $L$ | |
| `Hecke.quadratic_lattice_database()` | DB of lattices rank ≥ 3 with class number 1 or 2 | `[PD]` |

- Genus relies on local theory (Jordan decomposition, local densities) via MAGMA/GAP
- INDEF genus: can compute discriminant forms and genera even for indefinite lattices
- Handles even unimodular indefinite forms $II_{p,q}$
- Two even INDEF lattices of the same genus are often isometric (Hasse–Minkowski); genus invariants may suffice for equivalence

### 2.8 Automorphism and isometry

| Method | Description | Tags |
|--------|-------------|------|
| `automorphism_group_generators(L)` | Generators of `Aut(L)`; current Hecke docs require `is_definite(L)` | `[PD, GAP]` |
| `automorphism_group_order(L)` | Order of `Aut(L)`; current Hecke docs require `is_definite(L)` | `[PD]` |
| `is_isometric(L1, L2)` | Isometry test | `[PD]` |
| `is_isometric_with_isometry(L1, L2)` | Isometry test + explicit map | `[PD]` |
| `is_locally_isometric(L1, L2, p)` | $p$-adic isometry test | |
| `is_rationally_isometric(L1, L2)` | Rational (ℚ) isometry test | `[INDEF ok]` |
| `hasse_invariant(L, p)` | Hasse invariant at prime $p$ | |
| `witt_invariant(L, p)` | Witt invariant at prime $p$ | |

- PD: finite groups, computed via shortest vectors + symmetries (e.g. $E_8$ Weyl group)
- Oscar also exposes "Lattices with isometry" and "Groups of automorphisms" sections
- INDEF: Aut(L) infinite; use Indefinite.jl or Vinberg's algorithm for reflection subgroups
- Rational/local isometry tests work for all signatures and are key ingredients in genus theory

### 2.9 Module operations and embeddings

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(L1, L2)` | Orthogonal direct sum; returns $(L, i_1, i_2)$ with injection maps | |
| `direct_product(L1, L2)` | Direct product; returns $(L, p_1, p_2)$ with projection maps | |
| `biproduct(L1, L2)` | Biproduct; returns $(L, i_1, i_2, p_1, p_2)$ | |
| `intersect(L1, L2)` | Intersection in common ambient space | |
| `+(L1, L2)` | Sum of lattices in common ambient | |
| `*(n, L)` | Scalar multiple of lattice | |
| `lattice_in_same_ambient_space(L, B)` | Sublattice with basis B in ambient of L | |
| `orthogonal_submodule(L, S)` | Orthogonal complement of S in L | |
| `dual(L)` | Dual lattice $L^\vee$ | |
| `is_sublattice(L, S)` | Whether $S \subseteq L$ | |
| `is_sublattice_with_relations(L, S)` | Sublattice test + inclusion relations | |
| `is_primitive(L, S)` | Whether S is primitive in L ($L/S$ torsion-free) | |
| `primitive_closure(L, S)` | Smallest primitive sublattice of $L$ containing $S$ | |
| `divisibility(L, v)` | Divisibility of vector $v$ in $L$ | |
| `in(v, L)` | Vector membership test | |
| `irreducible_components(L)` | Decompose into orthogonally irreducible components | |

#### Overlattices and embeddings

| Method | Description | Tags |
|--------|-------------|------|
| `glue_map(L, S, gen_imgs)` | Construct glue map for primitive extension | |
| `overlattice(glue_map)` | Build overlattice from a glue map | |
| `primitive_extension(L1, L2, glue_map)` | Nikulin gluing: lattice from isometric discriminant subquotients | |
| `local_modification(M, L, p)` | Local modification at prime $p$; docs assume `M` is $\mathbf{Z}_p$-maximal and `L` is isomorphic to `M` over $\mathbf{Q}_p$ | |
| `maximal_integral_lattice(L)` | Maximal integral overlattice | |
| `is_maximal_integral(L)` | Whether $L$ is already maximal integral | |
| `is_maximal(L)` | Whether $L$ is maximal | |
| `embed(L, gen)` | Embed lattice into a genus | |
| `embed_in_unimodular(L, ...)` | Embed into a unimodular lattice; current Hecke docs note this presently works only for even lattices | |

#### Endomorphism-based sublattices

| Method | Description | Tags |
|--------|-------------|------|
| `kernel_lattice(L, f)` | Kernel of endomorphism $f$ on $L$ | |
| `invariant_lattice(L, G)` | Fixed-point sublattice $L^G$ under group action | |
| `coinvariant_lattice(L, G)` | Orthogonal complement of $L^G$ in $L$ | |

#### Root lattice recognition

| Method | Description | Tags |
|--------|-------------|------|
| `root_lattice_recognition(L)` | Identify ADE type of root sublattice | `[PD]` |
| `root_lattice_recognition_fundamental(L)` | Find fundamental root system | `[PD]` |
| `ADE_type(L)` | Determine root lattice type | `[PD]` |
| `coxeter_number(L)` | Coxeter number | `[PD]` |
| `highest_root(L)` | Highest root coordinates | `[PD]` |

### 2.10 Vinberg's algorithm

`[INDEF]` — For hyperbolic lattices (signature $(1,n)$). Enumerates simple roots defining the Weyl chamber of the reflection group.

| Method | Description | Tags |
|--------|-------------|------|
| `vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)` | Fundamental roots of hyperbolic reflection lattice from Gram matrix | `[INDEF]` |
| `vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)` | Same, from `ZZLat` of signature $(1,0,n)$ | `[INDEF]` |
| `short_vectors_affine(S, v, α, d)` | Vectors $x$ with $x^2 = d$, $x \cdot v = \alpha$ (used internally by Vinberg) | `[INDEF]` |

Computes Coxeter diagram of reflecting hyperplanes. Applicable to even hyperbolic lattices ($U \oplus E_8(-1)$, etc.). Implementation follows Algorithm 2.2 of Jingyu Shi 2015.

### 2.11 Discriminant groups (`TorQuadModule`)

| Method | Description | Tags |
|--------|-------------|------|
| `torsion_quadratic_module(M, N)` | Torsion quadratic module $M/N$ | |
| `torsion_quadratic_module(q::QQMatrix)` | From rational Gram matrix | |
| `discriminant_group(L)` | $L^\vee / L$ as `TorQuadModule` | |
| `abelian_group(T)` | Underlying abelian group | |
| `cover(T)` / `relations(T)` | Cover lattice / relation lattice | |
| `gram_matrix_bilinear(T)` | Bilinear Gram matrix over $\mathbb{Q}/\mathbb{Z}$ | |
| `gram_matrix_quadratic(T)` | Quadratic Gram matrix over $\mathbb{Q}/2\mathbb{Z}$ | |
| `value_module(T)` | Value module of bilinear form | |
| `value_module_quadratic_form(T)` | Value module of quadratic form | |
| `modulus_bilinear_form(T)` | Modulus of bilinear form | |
| `modulus_quadratic_form(T)` | Modulus of quadratic form | |
| `quadratic_product(a)` | $q(a)$ for element $a \in T$ | |
| `inner_product(a, b)` | $b(a,b)$ for elements $a,b \in T$ | |
| `lift(a)` / `representative(a)` | Lift element to cover lattice | |
| `orthogonal_submodule(T, S)` | Orthogonal complement of submodule $S$ in $T$ | |
| `is_isometric_with_isometry(T, U)` | Isometry test + explicit map | |
| `is_anti_isometric_with_anti_isometry(T, U)` | Anti-isometry test + map | |
| `is_degenerate(T)` | Degeneracy test | |
| `is_semi_regular(T)` | Semi-regularity test | |
| `radical_bilinear(T)` | Radical of bilinear form | |
| `radical_quadratic(T)` | Radical of quadratic form | |
| `normal_form(T; partial=false)` | Normal form of torsion quadratic module | |
| `brown_invariant(T)` | Brown invariant (mod 8) | |
| `snf(T)` / `is_snf(T)` | Smith normal form / test | |
| `rescale(T, k)` | Rescaled module | |
| `genus(T, sig_pair)` | Genus from discriminant form + signature | |
| `is_genus(T, sig_pair)` | Check if a genus with this discriminant form exists | |
| `direct_sum(T1, T2)` / `direct_product` / `biproduct` | Categorical constructions | |
| `submodules(T; ...)` | Enumerate submodules | |
| `stable_submodules(T, act; ...)` | Submodules stable under isometries | |

### 2.12 Hermitian lattices (`HermLat` / `QuadLat`)

Methods shared with `ZZLat` (construction, rank, det, etc.) are listed in §2.2–2.8. Additional methods specific to lattices over number fields:

| Method | Description | Tags |
|--------|-------------|------|
| `base_field(L)` / `base_ring(L)` | Base field $K$ / ring of integers $\mathcal{O}_K$ | |
| `fixed_field(L)` / `fixed_ring(L)` | Fixed field under involution / its ring | |
| `involution(L)` | Involution of the hermitian form | |
| `pseudo_matrix(L)` / `pseudo_basis(L)` | Pseudo-matrix / pseudo-basis (fractional ideals + vectors) | |
| `coefficient_ideals(L)` | Coefficient ideals of pseudo-basis | |
| `absolute_basis(L)` / `absolute_basis_matrix(L)` | Absolute $\mathbb{Z}$-basis | |
| `generators(L)` / `gram_matrix_of_generators(L)` | Generators and their Gram matrix | |
| `local_basis_matrix(L, p)` | Basis matrix of $L_p$ | |
| `jordan_decomposition(L, p)` | Jordan decomposition at prime $p$ | |
| `is_isotropic(L, p)` | Whether $L_p$ is isotropic | |
| `is_modular(L)` / `is_modular(L, p)` | Modular lattice test (global / local) | |
| `can_scale_totally_positive(L)` | Whether the form can be rescaled to totally positive | |
| `volume(L)` | Volume ideal | |
| `is_maximal_integral(L)` / `is_maximal(L)` | Maximality tests | |
| `maximal_integral_lattice(L)` | Maximal integral overlattice | |

### 2.13 Quadratic spaces with isometry (`QuadSpaceWithIsom`)

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space_with_isometry(V, f; check)` | Pair space $V$ with isometry matrix $f$ | |
| `quadratic_space_with_isometry(V; neg=false)` | Pair with identity (or negation) | |
| `space(Vf)` / `isometry(Vf)` / `order_of_isometry(Vf)` | Accessors | |
| `rank(Vf)` / `dim(Vf)` / `gram_matrix(Vf)` / `det(Vf)` / `discriminant(Vf)` | Space attributes | |
| `diagonal(Vf)` / `signature_tuple(Vf)` | Diagonal / signature | |
| `is_definite(Vf)` / `is_positive_definite(Vf)` / `is_negative_definite(Vf)` | Definiteness | |
| `characteristic_polynomial(Vf)` / `minimal_polynomial(Vf)` | Polynomials of isometry | |
| `^(Vf, n)` | Raise isometry to power | |
| `direct_sum(Vf, Wg, ...)` | Equivariant direct sum | |
| `rescale(Vf, a)` | Rescale preserving isometry | |
| `rational_spinor_norm(Vf; b)` | Rational spinor norm | |

### 2.14 Lattices with isometry (`ZZLatWithIsom`)

Pairs an integer lattice with a finite-order isometry. Used for equivariant classification and K3/hyperkähler applications.

#### Construction

| Method | Description | Tags |
|--------|-------------|------|
| `integer_lattice_with_isometry(L, f; check, ambient_representation)` | Pair lattice $L$ with isometry matrix $f$ | |
| `integer_lattice_with_isometry(L; neg=false)` | Pair with identity (or negation if `neg=true`) | |
| `lattice(Vf::QuadSpaceWithIsom)` | Extract lattice from space-with-isometry | |
| `lattice_in_same_ambient_space(Lf, B)` | Sublattice preserving ambient isometry | |

#### Accessors

| Method | Description | Tags |
|--------|-------------|------|
| `isometry(Lf)` | Isometry matrix | |
| `ambient_isometry(Lf)` | Isometry on ambient space | |
| `ambient_space(Lf)` | Ambient quadratic space carrying the isometry | |
| `lattice(Lf)` | Underlying `ZZLat` | |
| `basis_matrix(Lf)` | Basis matrix of underlying lattice | |
| `order_of_isometry(Lf)` | Order of isometry (or `-1` if infinite) | |
| `characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)` | Polynomials of the isometry | |

#### Attributes

Upstream docs explicitly expose many `ZZLat` attributes on `ZZLatWithIsom`; these methods report invariants of the underlying lattice `L` in the pair `(L, f)` unless stated otherwise.

| Method | Description | Tags |
|--------|-------------|------|
| `rank(Lf)` / `degree(Lf)` | Rank and ambient degree inherited from the underlying lattice | |
| `gram_matrix(Lf)` / `det(Lf)` / `discriminant(Lf)` | Gram/determinant/discriminant invariants forwarded from `L` | |
| `signature_tuple(Lf)` | Lattice signature tuple `(n_{+}, n_{0}, n_{-})`; distinct from eigenspace signatures returned by `signatures(Lf)` | `[INDEF]` |
| `rational_span(Lf)` | Rational span accessor for the lattice-with-isometry object | `[INDEF]` |
| `genus(Lf)` | Genus of the underlying lattice `L` | `[INDEF]` |
| `minimum(Lf)` | Minimum of the underlying lattice; same positive-definite precondition as `minimum(L)` | `[PD]` |
| `scale(Lf)` / `norm(Lf)` | Scale and norm ideals forwarded from `L` | |
| `is_even(Lf)` / `is_integral(Lf)` / `is_unimodular(Lf)` | Arithmetic predicates of the underlying lattice | |
| `is_primary(Lf, p)` / `is_primary_with_prime(Lf)` | `p`-primary discriminant-group predicates forwarded from `L` | |
| `is_elementary(Lf, p)` / `is_elementary_with_prime(Lf)` | Elementary discriminant-group predicates forwarded from `L` | |
| `is_positive_definite(Lf)` / `is_negative_definite(Lf)` / `is_definite(Lf)` | Definiteness predicates inherited from `L` | |

#### Type classification

| Method | Description | Tags |
|--------|-------------|------|
| `type(Lf)` | Type of lattice-with-isometry (dictionary of invariants) | |
| `is_of_type(Lf, t)` | Test against a type | |
| `is_of_same_type(Lf, Mg)` | Whether two lattices-with-isometry share the same type | |
| `is_of_hermitian_type(Lf)` | Whether the isometry gives a hermitian structure | |
| `hermitian_structure(Lf)` | Extract hermitian lattice from hermitian-type isometry | |
| `trace_lattice_with_isometry(H)` | Recover `ZZLatWithIsom` from hermitian lattice via trace form | |
| `is_hermitian(t::Dict)` | Whether a type dictionary corresponds to hermitian type | |

#### Operations

| Method | Description | Tags |
|--------|-------------|------|
| `^(Lf, n)` | Raise isometry to power $n$ | |
| `direct_sum(Lf, Mg, ...)` | Equivariant direct sum | |
| `dual(Lf)` | Dual with induced isometry | |
| `lll(Lf)` | LLL with isometry carried along | |
| `rescale(Lf, a)` | Rescale with isometry preserved | |
| `orthogonal_submodule(Lf, B)` | Orthogonal complement with induced isometry | |

#### Kernel sublattices

| Method | Description | Tags |
|--------|-------------|------|
| `kernel_lattice(Lf, p)` | Kernel of polynomial $p$ in isometry (with induced isometry) | |
| `kernel_lattice(Lf, l)` | Kernel of $f^l - 1$ | |
| `invariant_lattice(Lf)` | Fixed sublattice $L^f$ | |
| `coinvariant_lattice(Lf)` | Orthogonal complement of $L^f$ | |
| `invariant_coinvariant_pair(Lf)` | Both at once | |

#### Discriminant groups

| Method | Description | Tags |
|--------|-------------|------|
| `discriminant_group(Lf)` | `TorQuadModule` with induced isometry | |
| `image_centralizer_in_Oq(Lf)` | Image of centralizer of $\bar{f}$ in $O(q_L)$ | |
| `discriminant_representation(L, G)` | Action of matrix group on discriminant group | |

#### Spinor norm

| Method | Description | Tags |
|--------|-------------|------|
| `signatures(Lf)` | Signatures of eigenspaces | |
| `rational_spinor_norm(Lf; b)` | Rational spinor norm | |

#### Enumeration

| Method | Description | Tags |
|--------|-------------|------|
| `enumerate_classes_of_lattices_with_isometry(gen, poly, ...)` | Representatives of isomorphism classes in a genus | |
| `representatives_of_hermitian_type(gen, poly, ...)` | Representatives of hermitian type | |
| `admissible_triples(gen, p, ...)` | Tuples of genera satisfying admissibility conditions | |
| `is_admissible_triple(gen_triple, p)` | Validate admissibility | |
| `splitting(Lf)` | Generic splitting of `ZZLatWithIsom` into irreducible components | |
| `splitting_of_hermitian_type(Lf)` | Split hermitian-type lattice-with-isometry into hermitian sublattices | |
| `splitting_of_prime_power(Lf, p)` | Split lattice-with-isometry at a prime power | |
| `splitting_of_pure_mixed_prime_power(Lf, p)` | Split pure/mixed part at prime power | |
| `splitting_of_mixed_prime_power(Lf, p)` | Split mixed part at prime power | |

### 2.15 Primitive embeddings

| Method | Description | Tags |
|--------|-------------|------|
| `primitive_embeddings(L, M)` | Primitive embeddings of $M$ into $L$ | |
| `primitive_embeddings(G::ZZGenus, M)` | Primitive embeddings into lattices of genus $G$ | |
| `primitive_embeddings(q::TorQuadModule, sig, M)` | Via discriminant form + signature | |
| `primitive_extensions(M, N)` | Isomorphism classes of primitive extensions of $M \oplus N$ | |
| `equivariant_primitive_extensions(Mf::ZZLatWithIsom, Nf::ZZLatWithIsom; glue_only=false)` | Equivariant primitive extensions (with isometries); returns `Vector{ZZLatWithIsom}` | |
| `admissible_equivariant_primitive_extensions(Mf, Nf, gen, poly, p)` | Admissible equivariant extensions satisfying type conditions for a target genus | |

### 2.16 Hermitian genera

| Method | Description | Tags |
|--------|-------------|------|
| `genus(L::HermLat)` | Global genus of hermitian lattice | |
| `genus(L::HermLat, p)` | Local genus at prime $p$ | |
| `hermitian_genera(E, rank, sigs, det; ...)` | Enumerate hermitian genera | |
| `hermitian_local_genera(E, p, rank, det_val, min_scale, max_scale)` | Enumerate local hermitian genera | |
| `representative(G)` / `representatives(G)` | Representatives of genus classes | |
| `genus_representatives(L)` | All representatives in genus of $L$ | |
| `mass(L)` | Mass of hermitian lattice | |
| `rank(G)` / `primes(G)` / `signatures(G)` / `is_integral(G)` | Genus attributes | |
| `scale(G)` / `norm(G)` / `local_symbols(G)` | Scale, norm, local data | |
| `direct_sum(G1, G2)` / `rescale(G, a)` | Operations on genera | |
| `is_ramified(g)` / `is_split(g)` / `is_inert(g)` / `is_dyadic(g)` | Local genus splitting behavior | |

### 2.17 Isometry group actions on lattices

| Method | Description | Tags |
|--------|-------------|------|
| `is_isometry(L, f)` | Whether $f$ is an isometry of $L$ | |
| `is_isometry_list(L, fs)` | Test list of matrices | |
| `is_isometry_group(L, G)` | Test matrix group | |
| `is_stable_isometry(L, S, f)` | Whether $f$ stabilizes sublattice $S$ | |
| `is_special_isometry(L, f)` | Whether $f \in SO(L)$ (det = +1) | |
| `special_orthogonal_group(L)` / `special_subgroup(G)` | $SO(L)$ / $SO$ subgroup of isometry group | |
| `stable_orthogonal_group(L, S)` / `stable_subgroup(G, S)` | Isometries stabilizing $S$ | |
| `stabilizer_discriminant_subgroup(G, T)` | Stabilizer of discriminant subgroup | |
| `stabilizer_in_orthogonal_group(L, S)` | Stabilizer of sublattice in $O(L)$ | |
| `pointwise_stabilizer_in_orthogonal_group(L, S)` | Pointwise stabilizer | |
| `setwise_stabilizer_in_orthogonal_group(L, S)` | Setwise stabilizer | |
| `pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(L, S)` | Pointwise stabilizer of $S^\perp$ | |
| `stabilizer_in_diagonal_action(L1, L2, ...)` | Stabilizer under diagonal action | |
| `maximal_extension(G, ...)` | Maximal extension of isometry group | |
| `saturation(L, S)` | Saturation of sublattice (primitive closure in $L$) | |
| `is_saturated_with_saturation(L, S)` | Test + compute saturation | |
| `extend_to_ambient_space(L, f)` | Extend isometry to ambient space | |
| `restrict_to_lattice(L, f)` | Restrict ambient isometry to lattice | |

### 2.18 Torsion quadratic modules with isometry (`TorQuadModuleWithIsom`)

Finite quadratic module workflows with a distinguished isometry action. This is the discriminant-form analogue of lattice-with-isometry surfaces and is central for equivariant gluing/classification contracts.

| Method | Description | Tags |
|--------|-------------|------|
| `TorQuadModuleWithIsom` | Type for a torsion quadratic module paired with an isometry | `[NT]` |
| `underlying_module(Tf)` / `torsion_quadratic_module(Tf)` | Access underlying finite quadratic module | `[NT]` |
| `isometry(Tf)` / `order_of_isometry(Tf)` | Access isometry and its order; upstream notes order is finite-order data computed lazily and cached | `[NT]` |
| `torsion_quadratic_module_with_isometry(T, f; check=true)` | Constructor from a `TorQuadModule` and module map; `check=true` validates compatibility | `[NT]` |
| `torsion_quadratic_module_with_isometry(q::QQMatrix, f::ZZMatrix; check=true)` | Constructor from quadratic-form matrix data and action matrix; `check=true` validates constraints | `[NT]` |
| `sub(Tf, gens)` | Construct an isometry-stable submodule from generators | `[NT]` |
| `primary_part(Tf, m)` | Primary part with induced isometry action | `[NT]` |
| `orthogonal_submodule(Tf, S; check=true)` | Orthogonal complement in the finite quadratic module with induced action; upstream requires `S` stable under isometry (enforced when `check=true`) | `[NT]` |
| `submodules(Tf; quotype=...)` | Enumerate isometry-stable submodules (optionally filtered by quadratic type) | `[NT]` |
| `automorphism_group_with_inclusion(Tf)` | Automorphism group with inclusion map, identified upstream as the subgroup of `O(T)` commuting with the fixed isometry | `[NT]` |
| `automorphism_group(Tf)` | Automorphism group of the pair `(T, f)` | `[NT]` |
| `is_isomorphic_with_map(Tf, Sg)` | Isomorphism test between pairs, with explicit map when successful | `[NT]` |
| `is_anti_isomorphic_with_map(Tf, Sg)` | Anti-isomorphism test between pairs, with explicit map when successful | `[NT]` |

Source note: contracts in this subsection were reconciled against `docs/julia/oscar_jl/number_theory/quad_form_and_isom/torquadmodwithisom.md`, the OSCAR stable `QuadFormAndIsom` introduction (`https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/intro/`), and the OSCAR dev `torquadmodwithisom` method page (`https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/`) (accessed 2026-02-17).

### References

- Oscar manual and Hecke GitHub documentation
- Hofmann & Fieker (2025)
- Nebe–Pless–Sloane (lattices), Conway–Sloane (theta series, classification)
- Kirschmer–Voight (forms over number fields)
- GAP Quadratic Forms package

### Definiteness summary

| Regime | Available methods |
|--------|------------------|
| **PD** | All: LLL, SVP/CVP, kissing number, genus, automorphisms, root recognition, theta series ingredients |
| **ND** | Use `rescale(L, -1)` to reduce to PD |
| **INDEF** | `lll` (runs, limited meaning); genus/discriminant forms; rational/local isometry; Vinberg's algorithm (sig $(1,n)$); discriminant group operations; no SVP/CVP |

---

## 3. Oscar.jl

Metapackage combining Nemo, Hecke, Polymake, Singular, GAP. Does not add distinct lattice algorithms — provides unified interface to Hecke's methods.

### Integration points

| Capability | Notes |
|------------|-------|
| `Oscar.ZZLat` | High-level type wrapping Hecke's `ZZLat` |
| `Oscar.to_oscar(obj)` | Emit reproducible Julia code to reconstruct `obj` (useful for `ZZLatWithIsom` examples and bug reports) |
| Lattice databases | Markus Kirschmer's databases accessible directly |
| `lll`, `short_vectors`, `close_vectors` | Dispatch to Hecke/Nemo |
| Discriminant groups | Finite quadratic module type; computes isometries of discriminant form (Nikulin theory) |
| `rescale(L, r)` | Documented with warnings about INDEF limitations |
| Intersection forms | Verify primitive embeddings for Néron–Severi / K3 lattices (Nikulin theory) |
| Polyhedral integration | Use lattice in polyhedral context via Polymake; compute Aut(L) as abstract group |

Same definiteness constraints as Hecke. Oscar v1.6 includes Hecke v0.39.

### References

- Oscar manual, Quadratic Forms section
- OSCAR homepage and reference paper (2023)
- `using Oscar` provides unified namespace for Nemo LLL + Hecke genus functions

---

## 4. Nemo.jl

Computer algebra over ℤ, ℚ, ℤ/n. Built on FLINT/Antic. Lattice = `ZZMatrix` (`fmpz_mat` — FLINT integer matrix) whose rows (or columns) form a basis in $\mathbb{Z}^n$. Provides matrix-level reduction, not high-level lattice classification.

### 4.1 LLL reduction

| Function | Description | Tags |
|----------|-------------|------|
| `lll(B::ZZMatrix, ctx::LLLContext)` | LLL-reduced basis; default δ=0.99, η=0.51 | `[PD, FLINT]` |
| `lll_with_transform(B)` | Returns $(L, T)$ with $L = T \cdot B$ | `[PD, FLINT]` |
| `lll_gram(G)` | LLL on Gram matrix $G = B B^T$; requires symmetric PSD | `[PD, FLINT]` |
| `lll_gram_with_transform(G)` | Gram-based LLL + transformation | `[PD, FLINT]` |

- `lll(B)` without explicit Gram uses standard Euclidean dot product
- Gram-based variant requires symmetric, non-singular (or semi-definite) G
- INDEF Gram: algorithm executes but "reduced" is meaningless — LLL criteria assume PD; supply a PD Gram majorant instead (as in BKZ contexts)

### 4.2 Hermite Normal Form

| Function | Description | Tags |
|----------|-------------|------|
| `hnf(X)` / `AbstractAlgebra.hnf(X)` | Hermite normal form (triangular, divisibility) | `[DEG, INDEF ok]` |
| `hnf_with_transform(X)` | Returns $(H, U)$ with $H = U \cdot X$ | `[DEG, INDEF ok]` |

No definiteness assumptions. Purely algebraic. Canonical representative of lattice basis. Used in ideal arithmetic and linear Diophantine equations. Fast modular HNF via FLINT. Does not prefer short vectors.

### 4.3 Smith Normal Form

| Function | Description | Tags |
|----------|-------------|------|
| `snf(X)` / `AbstractAlgebra.snf(X)` | Smith normal form; diagonal $D = UXV$ with invariant factors | `[DEG, INDEF ok]` |
| `snf_with_transform(X)` | Returns $(D, U, V)$ | `[DEG, INDEF ok]` |

Reveals $\mathbb{Z}^n / L \cong \mathbb{Z}/d_1 \times \cdots \times \mathbb{Z}/d_n$. Discriminant = $\prod d_i$ (up to sign). No definiteness assumptions.

### 4.4 Other

| Function | Description | Tags |
|----------|-------------|------|
| Echelon form | Via FLINT | `[DEG]` |
| Saturation | No high-level `saturate` function; achieve via HNF/SNF (invariant factors reveal if sublattice has index > 1 in rational span) | `[DEG]` |

### Interaction with Hecke

Nemo `ZZMatrix` / `QQMatrix` are the underlying matrix types in Hecke/Oscar lattice objects. One can extract basis/Gram and apply Nemo functions directly.

### References

- Fieker et al., ISSAC 2017
- FLINT documentation (floating-point LLL, Gram-Schmidt)
- Cohen, *A Course in Computational Algebraic Number Theory* (HNF/SNF)
- Nguyen–Vallée, *The LLL Algorithm*

---

## 5. LLLplus.jl

`[PD, EUCLID]` — Experimental lattice reduction toolkit by Christian Peel. Pure Julia. Not registered. Pedagogical / prototyping focus. Applications: cryptography, communications, integer programming.

### Methods

| Function | Description | Tags |
|----------|-------------|------|
| `lll(B)` | LLL reduction | `[PD, EUCLID]` |
| `seysen(B)` | Seysen's reduction (minimizes pairwise dot products; more orthogonal than LLL) | `[PD, EUCLID]` |
| `hkz(B)` | Hermite-Korkine-Zolotarev reduction (exact SVP in projected lattices; exponential cost) | `[PD, EUCLID]` |
| `brun(B)` | Brun's algorithm (integer relations / Diophantine approximation; precursor to PSLQ) | `[PD, EUCLID]` |
| `cvp(Q, R, y)` | Closest vector problem via sphere decoder (QR factorization input) | `[PD, EUCLID]` |

### Utility functions

| Function | Description |
|----------|-------------|
| `subsetsum(...)` | Subset sum via lattice formulation |
| `integerfeasibility(...)` | Integer linear feasibility |
| `rationalapprox(...)` | Rational approximation via short vectors |
| BBP π digits | Spigot algorithm demo |

### Definiteness

All algorithms assume Euclidean norm. Input is a real matrix (accepts `randn` floating-point); form is the standard inner product or implicit via QR. INDEF forms not supported. Brun's algorithm internally constructs a PD lattice in extended dimension. For serious/large-scale use, consider fplll (C++) or Nemo.

### References

- Wübben et al. (lattice reduction in communications)
- Bremner, *Lattice Basis Reduction*
- Simons Institute Lattice Algorithms workshop (2020)
- Chris Peel, JuliaCon 2021: "Lattice Reduction using LLLplus.jl"

---

## 6. LatticeAlgorithms.jl (Amazon Science)

`[PD, EUCLID]` — Lattice algorithms for GKP quantum error-correcting codes. Accompanied PRX Quantum 4, 040334 (2023).

### Methods

| Function / capability | Description | Tags |
|----------------------|-------------|------|
| LLL reduction | Standard LLL | `[PD]` |
| KZ (HKZ) reduction | Korkine-Zolotarev; exact SVP in small dimensions | `[PD]` |
| SVP solver | Shortest vector problem (Fincke-Pohst enumeration) | `[PD]` |
| CVP solver | Closest vector problem (sphere decoding / A* search) | `[PD]` |
| Predefined lattices | $D_n$ root lattice, repetition-GKP lattices | `[PD]` |
| MLD for surface-square GKP | Maximum likelihood decoding using CVP as component | `[PD]` |

### Definiteness

All algorithms require PD (Euclidean distance minimization). GKP symplectic form is INDEF but the decoding problem reduces to CVP in a PD lattice of errors.

### References

- "Closest Lattice Point Decoding for Multimode GKP Codes", PRX Quantum 4, 040334 (2023)
- Subsequent arXiv papers on tensor-network / matching decoders with lattice methods
- Search algorithm reference: Chalmers University publication (lattice point enumeration)
- Algorithms efficient in moderate dimensions ($n \sim 8$–$10$ for multimode GKP)

---

## 7. Minor Packages

### 7.1 LatticeBasisReduction.jl

`[PD, EUCLID]` — Lattice reduction algorithms. Provides LLL and related reductions. Minimal package; use LLLplus or Nemo for more features.

### 7.2 MinkowskiReduction.jl

`[PD, EUCLID]` — Minkowski reduction of lattice bases. Computes Minkowski-reduced bases (all basis vectors are successive minima). Exact but exponential cost; practical only in low dimensions.

---

## 8. Other Considerations

### Theta series

No Julia package automates theta series computation. Use `short_vectors(L, 0, N)` in Hecke to count vectors by norm and assemble $\Theta_L(q) = \sum_{v \in L} q^{|v|^2}$ manually. No `theta_series(L, precision)` function yet. No package for Eisenstein series or Siegel theta constants; use PARI/GP via Nemo for deeper analysis. `[PD]`

### GAP packages (via GAP.jl / Oscar)

`OrthogonalForms`, `AutomorphismGroups`, etc. Not Julia packages per se. Complement Oscar for exact isometry tests via Hasse invariants.

### Performance notes

| Package | Backend | Speed |
|---------|---------|-------|
| Nemo.jl | FLINT (C) | Fast (LLL, HNF) |
| Hecke.jl | Nemo + GAP + optional PARI/MAGMA (genus computations) | Moderate–fast |
| Indefinite.jl | GAP | Moderate |
| LLLplus.jl | Pure Julia | Moderate; use fplll for large-scale |
| LatticeAlgorithms.jl | Pure Julia | Moderate (designed for dim ~8–10) |

---

## 9. Definiteness Constraints Summary

### Positive-definite

All reduction (LLL, BKZ, HKZ, Seysen), enumeration (SVP, CVP, `short_vectors`), and packing invariants (`kissing_number`, theta series) apply. Algorithms treat the lattice as a metric space.

### Indefinite

No SVP/CVP (infinitely many vectors in any bounded norm range due to null directions). Use:
- Genus symbols and discriminant forms for classification
- Orbits of isotropic vectors (Indefinite.jl)
- Vinberg's algorithm for sig $(1,n)$ reflection groups
- Functions enforce via `check::Bool=true`; throws if form is not definite

### Semi-definite / degenerate

Most functions demand non-degenerate forms ("nondegenerate $\mathbb{Z}$-lattice"). Preprocess by quotienting out the null space. HNF/SNF (Nemo) handle rank-deficient matrices. Hecke/Oscar error out and guide toward `rescale`, `scale(L)`, or orthogonal complement to remove null directions. Nemo/LLLplus simply assume away degenerate cases or rely on generic linear algebra for rank deficiency.

---

## Sources

- Indefinite.jl README (Dutour Sikirić et al.)
- Oscar/Hecke stable manual (lattices): https://docs.oscar-system.org/stable/Hecke/manual/lattices/integrelattices/ (accessed 2026-02-17)
- Oscar/Hecke stable manual (lattices with isometry): https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/ (accessed 2026-02-17)
- In-repo localized provenance for `ZZLatWithIsom` attribute-forwarding survey: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom_online_provenance_2026-02-17.md`
- Nemo.jl documentation — LLL, HNF
- LLLplus.jl README
- LatticeAlgorithms.jl README (Amazon Science)
