# Nemo/Hecke Lattice Methods Reference
## Comprehensive Julia lattice stack reference (indefinite-aware)

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite setting |
| `[ND]` | Non-degenerate bilinear form required |
| `[INDEF]` | Works in indefinite signatures |
| `[DEG]` | Works with degenerate data |
| `[ZZMOD]` | Matrix/module-level integer lattice operations |
| `[NT]` | Number-theoretic lattice/form workflows |
| `[RED]` | Basis reduction |
| `[FLINT]` | Backed by FLINT |
| `[GAP]` | Uses GAP-backed routines |

---

## 1. Scope

This file documents the lattice-relevant surfaces of:

- `Hecke.jl` (high-level arithmetic lattices, genera, isometries, discriminant forms)
- `Nemo.jl` (matrix-level integer lattice primitives)

For cross-package Julia context (Oscar, Indefinite.jl, LLLplus, etc.), see `julia_lattice_methods_reference.md`.

---

## 2. Hecke.jl (Lattice-Level)

### 2.1 Core types

| Type | Description | Tags |
|------|-------------|------|
| `ZZLat` | Integral quadratic lattice over Z | `[ND, NT]` |
| `QuadLat` | Quadratic lattice over Q or number field | `[ND, NT]` |
| `HermLat` | Hermitian lattice over quadratic extension | `[ND, NT]` |
| `ZZGenus` | Global genus symbol for integer lattices | `[NT]` |
| `ZZLocalGenus` | Local genus symbol at prime `p` | `[NT]` |
| `TorQuadModule` | Finite quadratic module (`L^vee/L`) | `[NT]` |
| `QuadSpace` | Quadratic space over a field | `[NT]` |
| `HermSpace` | Hermitian space over extension field | `[NT]` |
| `ZZLatWithIsom` | Integer lattice with finite-order isometry | `[NT]` |
| `QuadSpaceWithIsom` | Quadratic space with isometry | `[NT]` |

### 2.2 Space construction and invariants

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space(K, n)` / `quadratic_space(K, G)` | Build quadratic space from dimension or Gram matrix | `[NT]` |
| `hermitian_space(E, n)` / `hermitian_space(E, G)` | Build hermitian space | `[NT]` |
| `gram_matrix(V)` / `gram_matrix(V, M)` | Gram matrix (optionally on subspace) | `[NT]` |
| `signature_tuple(V)` | Signature `(p, n)` | `[INDEF, NT]` |
| `det(V)` / `discriminant(V)` | Determinant/discriminant | `[NT]` |
| `is_regular(V)` | Non-degeneracy test | `[ND, NT]` |
| `is_isometric(V, W)` / `is_isometric(V, W, p)` | Global/local isometry tests | `[NT]` |
| `is_isotropic(V, p)` | Local isotropy test | `[INDEF, NT]` |
| `orthogonal_complement(V, M)` | Orthogonal complement | `[NT]` |
| `orthogonal_projection(V, M)` | Orthogonal projection | `[NT]` |

### 2.3 Lattice construction

| Method | Description | Tags |
|--------|-------------|------|
| `integer_lattice(; gram=G)` | Integer lattice from Gram matrix | `[NT]` |
| `integer_lattice(B; gram=G)` | Integer lattice from basis + optional Gram | `[NT]` |
| `lattice(V, B)` | Lattice in ambient quadratic space `V` | `[NT]` |
| `quadratic_lattice(K, gens; gram=M)` | Lattice from generators and Gram data | `[INDEF, NT]` |
| `hermitian_lattice(E, gens; gram=M)` | Hermitian lattice from generators | `[NT]` |
| `root_lattice(:A/:D/:E/:I, n)` | Root lattice constructors | `[PD, NT]` |
| `hyperbolic_plane_lattice(n)` | Hyperbolic plane lattice | `[INDEF, NT]` |
| `k3_lattice()` | K3 lattice constructor | `[INDEF, NT]` |
| `mukai_lattice()` | Mukai lattice constructor | `[INDEF, NT]` |
| `hyperkaehler_lattice(:K3, n=3)` | Hyperkahler intersection-form lattice | `[INDEF, NT]` |
| `rescale(L, r)` | Rescaled lattice | `[NT]` |

### 2.4 Intrinsic data and predicates

| Method | Description | Tags |
|--------|-------------|------|
| `gram_matrix(L)` / `basis_matrix(L)` | Core matrix data | `[NT]` |
| `ambient_space(L)` / `rational_span(L)` | Ambient/rational span | `[NT]` |
| `rank(L)` / `degree(L)` | Rank/ambient degree | `[NT]` |
| `signature_tuple(L)` | Signature | `[INDEF, NT]` |
| `det(L)` / `discriminant(L)` | Determinant/discriminant | `[NT]` |
| `scale(L)` / `norm(L)` | Scale and norm ideals | `[NT]` |
| `is_even(L)` / `is_integral(L)` / `is_unimodular(L)` | Arithmetic predicates | `[NT]` |
| `is_positive_definite(L)` / `is_negative_definite(L)` / `is_definite(L)` | Definiteness predicates | `[NT]` |
| `is_primary(L, p)` / `is_elementary(L, p)` | Discriminant-group structure predicates | `[NT]` |

### 2.5 Reduction and vector algorithms

| Method | Description | Tags |
|--------|-------------|------|
| `lll(L::ZZLat; same_ambient=true)` | LLL reduction of integer lattice | `[RED, FLINT, INDEF]` |
| `short_vectors(L, lb, ub)` | Enumerate bounded-norm vectors | `[PD, NT]` |
| `short_vectors_iterator(L, lb, ub)` | Lazy bounded-norm iterator | `[PD, NT]` |
| `shortest_vectors(L)` | Shortest vectors + norm | `[PD, NT]` |
| `minimum(L)` / `kissing_number(L)` | Shortest norm / kissing number | `[PD, NT]` |
| `close_vectors(L, v, ub; lb=0, check=true)` | Bounded close-vector enumeration | `[PD, NT]` |
| `vectors_of_square_and_divisibility(L, n, d)` | Arithmetic vector constraints | `[PD, NT]` |
| `short_vectors_affine(S, v, a, d)` | Affine constrained vector search | `[INDEF, NT]` |

Indefinite caveats:

- `lll` can run on indefinite lattices, but "shortness" is relative to a majorant.
- `short_vectors`/`shortest_vectors` are positive-definite workflows.
- For indefinite reflection workflows use `short_vectors_affine` and Vinberg methods.

### 2.6 Genus and classification

| Method | Description | Tags |
|--------|-------------|------|
| `genus(L::ZZLat)` / `genus(A::MatElem)` | Global genus from lattice or Gram | `[INDEF, NT]` |
| `genus(L, p)` | Local genus at prime `p` | `[NT]` |
| `integer_genera(sig, det; ...)` | Enumerate genera by signature and determinant | `[NT]` |
| `representative(gen)` / `representatives(gen)` | Class representatives in genus | `[NT]` |
| `mass(gen)` | Genus mass | `[NT]` |
| `primes(gen)` / `local_symbol(gen, p)` | Local symbol access | `[NT]` |
| `quadratic_space(gen)` / `rational_representative(gen)` | Rational representatives | `[NT]` |
| `represents(G1, G2)` | Representation relation between genera | `[NT]` |
| `discriminant_group(L)` | `L^vee/L` as finite quadratic module | `[NT]` |
| `genus_representatives(L)` | Representatives of genus of `L` | `[NT]` |

### 2.7 Automorphisms and isometry

| Method | Description | Tags |
|--------|-------------|------|
| `automorphism_group_generators(L)` | Generators for `Aut(L)` | `[PD, GAP, NT]` |
| `automorphism_group_order(L)` | Order of automorphism group | `[PD, NT]` |
| `is_isometric(L1, L2)` | Isometry test | `[PD, NT]` |
| `is_isometric_with_isometry(L1, L2)` | Isometry + explicit map | `[PD, NT]` |
| `is_locally_isometric(L1, L2, p)` | Local p-adic isometry test | `[NT]` |
| `is_rationally_isometric(L1, L2)` | Rational isometry test | `[INDEF, NT]` |
| `hasse_invariant(L, p)` / `witt_invariant(L, p)` | Local invariants | `[NT]` |

Indefinite note: full automorphism groups are often infinite; practical workflows rely on local/rational tests, genus/discriminant forms, and Vinberg/reflection tools.

### 2.8 Module operations, embeddings, overlattices

| Method | Description | Tags |
|--------|-------------|------|
| `direct_sum(L1, L2)` / `direct_product` / `biproduct` | Categorical lattice operations | `[NT]` |
| `intersect(L1, L2)` / `+(L1, L2)` / `*(n, L)` | Basic module operations | `[NT]` |
| `lattice_in_same_ambient_space(L, B)` | Sublattice in same ambient space | `[NT]` |
| `orthogonal_submodule(L, S)` | Orthogonal complement submodule | `[NT]` |
| `dual(L)` | Dual lattice | `[NT]` |
| `is_sublattice(L, S)` / `is_primitive(L, S)` | Inclusion/primitive tests | `[NT]` |
| `primitive_closure(L, S)` / `divisibility(L, v)` | Primitive closure/divisibility | `[NT]` |
| `glue_map(...)` / `overlattice(glue_map)` | Overlattice construction via gluing | `[NT]` |
| `primitive_extension(...)` | Nikulin-style primitive extension | `[NT]` |
| `maximal_integral_lattice(L)` / `is_maximal_integral(L)` | Maximal-integral workflows | `[NT]` |
| `embed(L, gen)` / `embed_in_unimodular(L, ...)` | Embedding algorithms | `[NT]` |
| `kernel_lattice(L, f)` / `invariant_lattice(L, G)` / `coinvariant_lattice(L, G)` | Endomorphism/group-action derived sublattices | `[NT]` |

### 2.9 Vinberg algorithm (indefinite core)

| Method | Description | Tags |
|--------|-------------|------|
| `vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)` | Fundamental roots from Gram matrix | `[INDEF, NT]` |
| `vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)` | Fundamental roots from lattice object | `[INDEF, NT]` |
| `short_vectors_affine(S, v, a, d)` | Affine constrained vectors used by Vinberg | `[INDEF, NT]` |

This targets hyperbolic signatures `(1, n)` and reflection-group chamber computation.

### 2.10 Discriminant finite quadratic modules (`TorQuadModule`)

| Method | Description | Tags |
|--------|-------------|------|
| `torsion_quadratic_module(M, N)` / `torsion_quadratic_module(q::QQMatrix)` | Build finite quadratic module | `[NT]` |
| `abelian_group(T)` / `cover(T)` / `relations(T)` | Structural accessors | `[NT]` |
| `gram_matrix_bilinear(T)` / `gram_matrix_quadratic(T)` | Bilinear/quadratic Gram data | `[NT]` |
| `inner_product(a, b)` / `quadratic_product(a)` | Form evaluation | `[NT]` |
| `lift(a)` / `representative(a)` | Lift to cover lattice | `[NT]` |
| `orthogonal_submodule(T, S)` | Orthogonal complement in module | `[NT]` |
| `is_isometric_with_isometry(T, U)` / `is_anti_isometric_with_anti_isometry(T, U)` | (Anti-)isometry tests with maps | `[NT]` |
| `normal_form(T; partial=false)` / `snf(T)` | Normal forms | `[NT]` |
| `brown_invariant(T)` / `genus(T, sig_pair)` / `is_genus(T, sig_pair)` | Genus-level invariants and feasibility | `[NT]` |

### 2.11 Lattices/spaces with isometry

| Method | Description | Tags |
|--------|-------------|------|
| `quadratic_space_with_isometry(...)` | Construct `QuadSpaceWithIsom` | `[NT]` |
| `integer_lattice_with_isometry(...)` | Construct `ZZLatWithIsom` | `[NT]` |
| `isometry(Lf)` / `ambient_isometry(Lf)` | Isometry accessors | `[NT]` |
| `order_of_isometry(Lf)` | Isometry order | `[NT]` |
| `characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)` | Isometry polynomials | `[NT]` |
| `invariant_lattice(Lf)` / `coinvariant_lattice(Lf)` / `kernel_lattice(Lf, ...)` | Isometry-derived decomposition | `[NT]` |
| `discriminant_group(Lf)` / `discriminant_representation(L, G)` | Induced discriminant action | `[NT]` |
| `enumerate_classes_of_lattices_with_isometry(...)` | Isometry-equivariant class enumeration | `[NT]` |

### 2.12 Hermitian-specific surfaces

| Method | Description | Tags |
|--------|-------------|------|
| `jordan_decomposition(L, p)` | Local Jordan decomposition | `[NT]` |
| `is_isotropic(L, p)` / `is_modular(L)` / `is_modular(L, p)` | Local/global predicates | `[NT]` |
| `volume(L)` | Volume ideal | `[NT]` |
| `genus(L::HermLat)` / `genus(L::HermLat, p)` | Global/local hermitian genus | `[NT]` |
| `hermitian_genera(...)` / `hermitian_local_genera(...)` | Genus enumeration | `[NT]` |
| `mass(L)` | Hermitian genus mass | `[NT]` |

---

## 3. Nemo.jl (Matrix-Level Lattice Primitives)

Nemo provides integer matrix algorithms that underpin many Hecke lattice computations.

### 3.1 Reduction and normal forms

| Method | Description | Tags |
|--------|-------------|------|
| `lll(B::ZZMatrix, ctx::LLLContext)` | LLL reduction with context parameters | `[RED, FLINT, ZZMOD]` |
| `lll_with_transform(B)` | Returns reduced basis and transform matrix | `[RED, FLINT, ZZMOD]` |
| `lll_gram(G)` / `lll_gram_with_transform(G)` | Gram-based LLL variants | `[RED, FLINT, PD]` |
| `hnf(X)` / `hnf_with_transform(X)` | Hermite normal form and transform | `[DEG, ZZMOD]` |
| `snf(X)` / `snf_with_transform(X)` | Smith normal form and transforms | `[DEG, ZZMOD]` |

### 3.2 Practical notes

- `hnf`/`snf` are algebraic and signature-agnostic.
- `lll_gram` is meaningful for positive-definite (or semidefinite) Gram workflows.
- Hecke uses Nemo `ZZMatrix`/`QQMatrix` as the underlying matrix layer.

---

## 4. Indefinite-First Workflow Map

For your stated use case (indefinite lattices):

1. Build lattice/space (`integer_lattice`, `quadratic_lattice`, `hyperbolic_plane_lattice`, K3/Mukai constructors).
2. Use invariants and classification (`signature_tuple`, `genus`, local symbols, `discriminant_group`).
3. Use rational/local isometry tests (`is_rationally_isometric`, `is_locally_isometric`).
4. For reflection-group geometry use `vinberg_algorithm` + `short_vectors_affine`.
5. Use `ZZLatWithIsom` when finite-order isometries are central to classification.

---

## 5. Sources

- Oscar/Hecke docs: https://docs.oscar-system.org/stable/Hecke/
- Hecke integer lattices (DeepWiki): https://deepwiki.com/thofma/Hecke.jl/5.3-integer-lattices
- Hecke general lattices (DeepWiki): https://deepwiki.com/thofma/Hecke.jl/5.4-general-lattices
- Vinberg docs (Oscar legacy path): https://docs.oscar-system.org/v1.2/NumberTheory/vinberg/
- Existing in-repo canonical detail: `julia_lattice_methods_reference.md`
