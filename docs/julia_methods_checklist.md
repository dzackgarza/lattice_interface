# Julia Method Test Gap Checklist

Tracks Julia-relevant methods documented in `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (sections 1-4).
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Indefinite.jl

### Methods

- [ ] ``INDEF_FORM_TestEquivalence(Q1, Q2)``
- [ ] ``INDEF_FORM_AutomorphismGroup(Q)``
- [ ] ``INDEF_FORM_GetOrbitRepresentative(Q, C)``
- [ ] ``INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)``
- [ ] ``INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)``
### Definiteness

### References

## 2. Hecke.jl (via Oscar)

### 2.1 Types

### 2.2 Quadratic and hermitian spaces

- [ ] ``quadratic_space(K, n)` / `quadratic_space(K, G)``
- [ ] ``hermitian_space(E, n)` / `hermitian_space(E, G)``
- [ ] ``rank(V)` / `dim(V)``
- [ ] ``gram_matrix(V)` / `gram_matrix(V, M)``
- [ ] ``det(V)` / `discriminant(V)``
- [ ] ``diagonal(V)``
- [ ] ``diagonal_with_transform(V)``
- [ ] ``orthogonal_basis(V)``
- [ ] ``signature_tuple(V)``
- [ ] ``is_regular(V)``
- [ ] ``is_quadratic(V)` / `is_hermitian(V)``
- [ ] ``is_positive_definite(V)` / `is_negative_definite(V)` / `is_definite(V)``
- [ ] ``hasse_invariant(V, p)` / `witt_invariant(V, p)``
- [ ] ``invariants(V)``
- [ ] ``is_isometric(V, W)` / `is_isometric(V, W, p)``
- [ ] ``is_locally_represented_by(U, V, p)``
- [ ] ``is_represented_by(U, V)``
- [ ] ``inner_product(V, v, w)``
- [ ] ``orthogonal_complement(V, M)``
- [ ] ``orthogonal_projection(V, M)``
- [ ] ``is_isotropic(V, p)``
- [ ] ``is_locally_hyperbolic(V, p)``
- [ ] ``restrict_scalars(V, K, α)``
- [ ] ``direct_sum(V, W)` / `direct_product` / `biproduct``
### 2.3 Construction

- [ ] ``integer_lattice(; gram=G)``
- [ ] ``integer_lattice(B; gram=G)``
- [ ] ``lattice(V, B)``
- [ ] ``quadratic_lattice(K, gens; gram=M)``
- [ ] ``hermitian_lattice(E, gens; gram=M)``
- [ ] ``root_lattice(:A, n)` / `(:D, n)` / `(:E, n)` / `(:I, n)``
- [ ] ``hyperbolic_plane_lattice(n)``
- [ ] ``leech_lattice()``
- [ ] ``k3_lattice()``
- [ ] ``mukai_lattice()``
- [ ] ``hyperkaehler_lattice(:K3, n=3)``
- [ ] ``rescale(L, r)``
### 2.4 Intrinsic data

- [ ] ``gram_matrix(L)``
- [ ] ``basis_matrix(L)``
- [ ] ``ambient_space(L)``
- [ ] ``rational_span(L)``
- [ ] ``rank(L)``
- [ ] ``degree(L)``
- [ ] ``signature_tuple(L)``
  - Caveat: in current Hecke docs this returns `(n_positive, n_zero, n_negative)`, not a 2-tuple.
- [ ] ``det(L)``
- [ ] ``discriminant(L)``
- [ ] ``scale(L)``
- [ ] ``norm(L)``
- [ ] ``is_positive_definite(L)``
- [ ] ``is_negative_definite(L)``
- [ ] ``is_definite(L)``
- [ ] ``is_even(L)``
- [ ] ``is_integral(L)``
- [ ] ``is_unimodular(L)``
- [ ] ``is_primary(L, p)``
- [ ] ``is_primary_with_prime(L)``
- [ ] ``is_elementary(L, p)``
- [ ] ``is_elementary_with_prime(L)``
### 2.5 Reduction

- [ ] ``lll(L::ZZLat; same_ambient=true)``
- [ ] `LLLContext(δ, η)`
### 2.6 Vector enumeration

- [ ] ``short_vectors(L, lb, ub)``
- [ ] ``short_vectors_iterator(L, lb, ub)``
- [ ] ``shortest_vectors(L)``
- [ ] ``close_vectors(L, v, ub; lb=0, check=true)``
- [ ] ``short_vectors_affine(S, v, α, d)``
- [ ] ``vectors_of_square_and_divisibility(L, n, d)``
- [ ] ``enumerate_quadratic_triples(L, ...)``
- [ ] ``minimum(L)``
- [ ] ``kissing_number(L)``
- [ ] `rescale(L, -1)`
- [ ] `short_vectors`
- [ ] `shortest_vectors`
- [ ] `short_vectors_affine`
- [ ] `close_vectors`
- [ ] `check=false`
### 2.7 Genus and classification

#### ZZGenus methods

- [ ] ``genus(L::ZZLat)``
- [ ] ``genus(A::MatElem)``
- [ ] ``genus(L, p)``
- [ ] ``integer_genera(sig::Tuple{Int, Int}, det::RationalUnion; even::Bool=true, kwargs...)`` / ``integer_genera(sig::Tuple{Int, Int}, det::QQFieldElem; even::Bool=true, max_scale::Int=Int(det), rank::Int=sum(sig), kwargs...)``
  - Caveat: upstream constrains determinant sign by signature (`det` has sign `(-1)^{s_-}` for `sig=(s_+, s_-)`) and parity (`det ∈ 2ZZ` for `even=true`, `det ∈ ZZ` for `even=false`).
- [ ] ``direct_sum(G1::ZZGenus, G2::ZZGenus)``
- [ ] ``representative(gen)``
- [ ] ``representatives(gen)``
- [ ] ``mass(gen)``
- [ ] ``dim(gen)` / `rank(gen)``
- [ ] ``signature(gen)``
- [ ] ``det(gen)``
- [ ] ``iseven(gen)``
- [ ] ``is_definite(gen)``
- [ ] ``level(gen)``
- [ ] ``scale(gen)` / `norm(gen)``
- [ ] ``primes(gen)``
- [ ] ``is_integral(gen)``
- [ ] ``local_symbol(gen, p)``
- [ ] ``quadratic_space(gen)``
- [ ] ``rational_representative(gen)``
- [ ] ``rescale(gen, a)``
- [ ] ``represents(G1, G2)``
#### ZZLocalGenus methods

- [ ] ``prime(S)``
- [ ] ``iseven(S)``
- [ ] ``symbol(S, scale)``
- [ ] ``hasse_invariant(S)``
- [ ] ``det(S)` / `dim(S)` / `rank(S)``
- [ ] ``excess(S)``
- [ ] ``signature(S)``
- [ ] ``oddity(S)``
- [ ] ``scale(S)` / `norm(S)` / `level(S)``
- [ ] ``representative(S)` / `gram_matrix(S)``
- [ ] ``rescale(S, a)``
- [ ] ``direct_sum(S1, S2)``
- [ ] ``represents(S1, S2)``
#### Discriminant group and classification

- [ ] ``discriminant_group(L)``
- [ ] ``genus_representatives(L)``
- [ ] ``Hecke.quadratic_lattice_database()``
### 2.8 Automorphism and isometry

- [ ] ``automorphism_group_generators(L)``
  - Caveat: upstream documents this for definite lattices (`is_definite(L)` required).
- [ ] ``automorphism_group_order(L)``
  - Caveat: upstream documents this for definite lattices (`is_definite(L)` required).
- [ ] ``is_isometric(L1, L2)``
- [ ] ``is_isometric_with_isometry(L1, L2)``
  - Caveat: upstream documents tuple return `(isometric::Bool, f)` with `(false, zero_matrix(QQ, 0, 0))` on failure, and kwargs `depth=3`, `bacher_depth=5`, `ambient_representation=true`.
- [ ] ``is_locally_isometric(L1, L2, p)``
- [ ] ``is_rationally_isometric(L1, L2)``
- [ ] ``hasse_invariant(L, p)``
- [ ] ``witt_invariant(L, p)``
### 2.9 Module operations and embeddings

- [ ] ``direct_sum(L1, L2)``
- [ ] ``direct_product(L1, L2)``
- [ ] ``biproduct(L1, L2)``
- [ ] ``intersect(L1, L2)``
- [ ] ``+(L1, L2)``
- [ ] ``*(n, L)``
- [ ] ``lattice_in_same_ambient_space(L, B)``
- [ ] ``orthogonal_submodule(L, S)``
- [ ] ``dual(L)``
- [ ] ``is_sublattice(L, S)``
- [ ] ``is_sublattice_with_relations(L, S)``
- [ ] ``is_primitive(L, S)``
- [ ] ``primitive_closure(L, S)``
- [ ] ``divisibility(L, v)``
- [ ] ``in(v, L)``
- [ ] ``irreducible_components(L)``
#### Overlattices and embeddings

- [ ] ``glue_map(L, S, gen_imgs)``
- [ ] ``overlattice(glue_map)``
- [ ] ``primitive_extension(L1, L2, glue_map)``
- [ ] ``local_modification(M, L, p)``
  - Caveat: upstream assumes `M` is `Z_p`-maximal and `L` is isomorphic to `M` over `Q_p`.
- [ ] ``maximal_integral_lattice(L)``
- [ ] ``is_maximal_integral(L)``
- [ ] ``is_maximal(L)``
- [ ] ``embed(L, gen)``
- [ ] ``embed_in_unimodular(L, ...)``
  - Caveat: upstream notes this currently works only for even lattices.
#### Endomorphism-based sublattices

- [ ] ``kernel_lattice(L, f)``
- [ ] ``invariant_lattice(::ZZLat, ::MatGroup)``
- [ ] ``coinvariant_lattice(::ZZLat, ::MatGroup)``
- [ ] ``invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})``
#### Root lattice recognition

- [ ] ``root_lattice_recognition(L)``
- [ ] ``root_lattice_recognition_fundamental(L)``
- [ ] ``ADE_type(L)``
- [ ] ``coxeter_number(L)``
- [ ] ``highest_root(L)``
### 2.10 Vinberg's algorithm

- [ ] ``vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)``
- [ ] ``vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)``
### 2.11 Discriminant groups (`TorQuadModule`)

- [ ] ``torsion_quadratic_module(M, N)``
- [ ] ``torsion_quadratic_module(q::QQMatrix)``
- [ ] ``abelian_group(T)``
- [ ] ``cover(T)` / `relations(T)``
- [ ] ``gram_matrix_bilinear(T)``
- [ ] ``gram_matrix_quadratic(T)``
- [ ] ``value_module(T)``
- [ ] ``value_module_quadratic_form(T)``
- [ ] ``modulus_bilinear_form(T)``
- [ ] ``modulus_quadratic_form(T)``
- [ ] ``quadratic_product(a)``
- [ ] ``inner_product(a, b)``
- [ ] ``lift(a)` / `representative(a)``
- [ ] ``orthogonal_submodule(T, S)``
- [ ] ``is_isometric_with_isometry(T, U)``
  - Caveat: upstream documents tuple return `(Bool, map)` with `(false, 0)` on failure, with preconditions: equal quadratic-form moduli (or prior rescaling) and semiregular decomposition checks.
- [ ] ``is_anti_isometric_with_anti_isometry(T, U)``
  - Caveat: upstream documents tuple return `(Bool, anti_map)` with `(false, 0)` on failure and the same modulus/rescale + semiregular preconditions.
- [ ] ``is_degenerate(T)``
- [ ] ``is_semi_regular(T)``
- [ ] ``radical_bilinear(T)``
- [ ] ``radical_quadratic(T)``
- [ ] ``normal_form(T; partial=false)``
- [ ] ``brown_invariant(T)``
- [ ] ``snf(T)` / `is_snf(T)``
- [ ] ``rescale(T, k)``
- [ ] ``genus(T, sig_pair)``
- [ ] ``is_genus(T, sig_pair)``
- [ ] ``direct_sum(T1, T2)` / `direct_product` / `biproduct``
- [ ] ``submodules(T; ...)``
- [ ] ``stable_submodules(T, act; ...)``
### 2.12 Hermitian lattices (`HermLat` / `QuadLat`)

- [ ] ``base_field(L)` / `base_ring(L)``
- [ ] ``fixed_field(L)` / `fixed_ring(L)``
- [ ] ``involution(L)``
- [ ] ``pseudo_matrix(L)` / `pseudo_basis(L)``
- [ ] ``coefficient_ideals(L)``
- [ ] ``absolute_basis(L)` / `absolute_basis_matrix(L)``
- [ ] ``generators(L)` / `gram_matrix_of_generators(L)``
- [ ] ``local_basis_matrix(L, p)``
- [ ] ``jordan_decomposition(L, p)``
- [ ] ``is_isotropic(L, p)``
- [ ] ``is_modular(L)` / `is_modular(L, p)``
- [ ] ``can_scale_totally_positive(L)``
- [ ] ``volume(L)``
- [ ] ``is_maximal_integral(L)` / `is_maximal(L)``
### 2.13 Quadratic spaces with isometry (`QuadSpaceWithIsom`)

- [ ] ``quadratic_space_with_isometry(V, f; check)``
  - Caveat: current upstream pages contain conflicting default wording for `check`; pass it explicitly when contract fidelity matters.
- [ ] ``quadratic_space_with_isometry(V; neg=false)``
- [ ] ``space(Vf)` / `isometry(Vf)` / `order_of_isometry(Vf)``
  - Caveat: upstream documents `order_of_isometry(Vf) = PosInf` for infinite order; for rank-zero spaces, upstream uses `-1`.
- [ ] ``rank(Vf)` / `dim(Vf)` / `gram_matrix(Vf)` / `det(Vf)` / `discriminant(Vf)``
- [ ] ``diagonal(Vf)` / `signature_tuple(Vf)``
- [ ] ``is_definite(Vf)` / `is_positive_definite(Vf)` / `is_negative_definite(Vf)``
- [ ] ``characteristic_polynomial(Vf)` / `minimal_polynomial(Vf)``
- [ ] ``^(Vf, n)``
- [ ] ``direct_sum(Vf::Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}...)``
- [ ] ``rescale(Vf, a)``
- [ ] ``rational_spinor_norm(Vf; b)``
### 2.14 Lattices with isometry (`ZZLatWithIsom`)

#### Construction

- [ ] ``integer_lattice_with_isometry(L, f; check, ambient_representation)``
  - Caveat: upstream distinguishes matrix representation via `ambient_representation` (ambient-space basis vs fixed basis of `L`).
- [ ] ``integer_lattice_with_isometry(L; neg=false)``
- [ ] ``lattice(Vf::QuadSpaceWithIsom)``
- [ ] ``lattice(Vf::QuadSpaceWithIsom, B)``
- [ ] ``lattice_in_same_ambient_space(Lf, B)``
#### Accessors

- [ ] ``isometry(Lf)``
- [ ] ``ambient_isometry(Lf)``
- [ ] ``ambient_space(Lf)``
- [ ] ``lattice(Lf)``
- [ ] ``basis_matrix(Lf)``
- [ ] ``order_of_isometry(Lf)``
  - Caveat: upstream `latwithisom` defines this as the order of lattice isometry `f`, documented as a divisor of the ambient isometry order; both finite- and infinite-order isometries are supported.
- [ ] ``characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)``
#### Attributes

- [ ] ``rank(Lf)`` / ``degree(Lf)``
- [ ] ``gram_matrix(Lf)`` / ``det(Lf)`` / ``discriminant(Lf)``
- [ ] ``signature_tuple(Lf)``
  - Caveat: this is the lattice signature tuple inherited from the underlying `L`, distinct from eigenspace-signature data returned by `signatures(Lf)`.
- [ ] ``rational_span(Lf)``
- [ ] ``genus(Lf)``
- [ ] ``minimum(Lf)``
  - Caveat: inherits the positive-definite requirement of the underlying lattice minimum routine.
- [ ] ``scale(Lf)`` / ``norm(Lf)``
- [ ] ``is_even(Lf)`` / ``is_integral(Lf)`` / ``is_unimodular(Lf)``
- [ ] ``is_primary(Lf, p)`` / ``is_primary_with_prime(Lf)``
- [ ] ``is_elementary(Lf, p)`` / ``is_elementary_with_prime(Lf)``
- [ ] ``is_positive_definite(Lf)`` / ``is_negative_definite(Lf)`` / ``is_definite(Lf)``

#### Type classification

- [ ] ``type(Lf)``
- [ ] ``is_of_type(Lf, t)``
- [ ] ``is_of_same_type(Lf, Mg)``
- [ ] ``is_of_hermitian_type(Lf)``
- [ ] ``hermitian_structure(Lf)``
- [ ] ``trace_lattice_with_isometry(H)``
- [ ] ``trace_lattice_with_isometry(H, res)``
- [ ] ``is_hermitian(t::Dict)``
#### Operations

- [ ] ``^(Lf, n)``
- [ ] ``direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)``
- [ ] ``dual(Lf)``
- [ ] ``lll(Lf)``
- [ ] ``rescale(Lf, a)``
- [ ] ``orthogonal_submodule(Lf, B)``
#### Kernel sublattices

- [ ] ``kernel_lattice(Lf, p)``
- [ ] ``kernel_lattice(Lf, l)``
- [ ] ``invariant_lattice(Lf)``
- [ ] ``coinvariant_lattice(Lf)``
- [ ] ``invariant_coinvariant_pair(Lf)``
#### Discriminant groups

- [ ] ``discriminant_group(Lf)``
  - Caveat: upstream describes this as discriminant-module plus induced action data `(D, fD)`.
- [ ] ``discriminant_group(TorQuadModuleWithIsom, Lf; ambient_representation=true)``
- [ ] ``image_centralizer_in_Oq(Lf)``
- [ ] ``image_in_Oq(Lf)``
- [ ] ``discriminant_representation(L, G)``
#### Spinor norm

- [ ] ``signatures(Lf)``
- [ ] ``rational_spinor_norm(Lf; b)``
#### Enumeration

- [ ] ``enumerate_classes_of_lattices_with_isometry(::Union{ZZGenus, ZZLat}, ::Int)``
- [ ] ``representatives_of_hermitian_type(::Union{ZZLat, ZZGenus}, ::Union{ZZPolyRingElem, QQPolyRingElem}, ::Int)``
- [ ] ``representatives_of_hermitian_type(::Union{ZZGenus, ZZLat}, ::Int, ::Int)``
- [ ] ``admissible_triples(::ZZGenus, ::Int)``
- [ ] ``is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)``
- [ ] ``splitting(::ZZLatWithIsom, ::Int, ::Int)``
- [ ] ``splitting_of_hermitian_type(::ZZLatWithIsom, ::Int, ::Int)``
- [ ] ``splitting_of_prime_power(::ZZLatWithIsom, ::Int, ::Int)``
- [ ] ``splitting_of_pure_mixed_prime_power(::ZZLatWithIsom, ::Int)``
- [ ] ``splitting_of_mixed_prime_power(::ZZLatWithIsom, ::Int, ::Int)``
### 2.15 Primitive embeddings

- [ ] ``primitive_embeddings(L, M)``
- [ ] ``primitive_embeddings(G::ZZGenus, M)``
- [ ] ``primitive_embeddings(q::TorQuadModule, sig, M)``
- [ ] ``primitive_extensions(M, N)``
- [ ] ``equivariant_primitive_extensions(Mf::ZZLatWithIsom, Nf::ZZLatWithIsom; glue_only=false)``
- [ ] ``admissible_equivariant_primitive_extensions(Mf, Nf, gen, poly, p)``
### 2.16 Hermitian genera

- [ ] ``genus(L::HermLat)``
- [ ] ``genus(L::HermLat, p)``
- [ ] ``hermitian_genera(E::NumField, rank::Int, signatures::Vector{Tuple{Int, Int}}, determinant::Vector{QQFieldElem}; min_scale::Int=(determinant[1] != 0 ? 0 : -3), max_scale::Int=(determinant[1] != 0 ? 0 : 3), kwargs...)``
  - Caveat: upstream requires `E` imaginary quadratic, `rank > 0`, and same-sign determinants (positive for even rank, negative for odd rank).
- [ ] ``hermitian_local_genera(E::NumField, p::AbsNumFieldOrderIdeal, rank::Int, determinant::QQFieldElem, min_scale::Int, max_scale::Int)``
- [ ] ``representative(G)` / `representatives(G)``
- [ ] ``mass(L)``
- [ ] ``rank(G)` / `primes(G)` / `signatures(G)` / `is_integral(G)``
- [ ] ``scale(G)` / `norm(G)` / `local_symbols(G)``
- [ ] ``direct_sum(G1, G2)` / `rescale(G, a)``
- [ ] ``is_ramified(g)` / `is_split(g)` / `is_inert(g)` / `is_dyadic(g)``
### 2.17 Isometry group actions on lattices

- [ ] ``is_isometry(::Hecke.QuadSpace, ::QQMatrix)`` / ``is_isometry(::ZZLat, ::QQMatrix)``
- [ ] ``is_isometry_list(::Hecke.QuadSpace, ::Vector{QQMatrix})`` / ``is_isometry_list(::ZZLat, ::Vector{QQMatrix})``
- [ ] ``is_isometry_group(::Hecke.QuadSpace, ::MatGroup)`` / ``is_isometry_group(::ZZLat, ::MatGroup)``
  - Caveat: upstream `fingrpact` docs describe these check helpers as non-exported utilities for input validation.
- [ ] ``is_stable_isometry(::ZZLatWithIsom)``
- [ ] ``is_special_isometry(::ZZLatWithIsom)``
- [ ] ``special_orthogonal_group(::ZZLat)`` / ``special_subgroup(::ZZLat, ::MatGroup)``
- [ ] ``stable_orthogonal_group(::ZZLat)`` / ``stable_subgroup(::ZZLat, ::MatGroup)``
- [ ] ``stabilizer_discriminant_subgroup(...)``
- [ ] ``stabilizer_in_orthogonal_group(...)``
- [ ] ``pointwise_stabilizer_in_orthogonal_group(...)``
- [ ] ``setwise_stabilizer_in_orthogonal_group(...)``
- [ ] ``pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(...)``
- [ ] ``stabilizer_in_diagonal_action(...)``
  - Caveat: current upstream `fingrpact` docs list these runtime names but do not expose typed dispatch signatures for this stabilizer family.
- [ ] ``maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)``
- [ ] ``saturation(::ZZLat, ::MatGroup, ::MatGroup)``
  - Caveat: upstream presents this explicit saturation computation for finite ambient group input.
- [ ] ``saturation(::ZZLat, ::MatGroup)``
  - Caveat: upstream states this form is available when the coinvariant lattice is definite or rank 2.
- [ ] ``is_saturated_with_saturation(...)``
  - Caveat: upstream states availability when the coinvariant lattice is definite.
- [ ] ``extend_to_ambient_space(::ZZLat, ...)``
  - Caveat: upstream positions this as matrix-representation conversion from lattice-basis coordinates to ambient-space coordinates for collections of isometries.
- [ ] ``restrict_to_lattice(::ZZLat, ...)``
  - Caveat: upstream positions this as the inverse conversion, restricting ambient-space matrix representation back to lattice-basis coordinates.
### 2.18 Torsion quadratic modules with isometry (`TorQuadModuleWithIsom`)

- [ ] ``TorQuadModuleWithIsom``
- [ ] ``underlying_module(Tf)``
- [ ] ``torsion_quadratic_module(Tf)``
- [ ] ``isometry(Tf)``
- [ ] ``order_of_isometry(Tf)``
  - Caveat: upstream states this is finite-order data cached after first computation; order is not precomputed on object construction.
- [ ] ``torsion_quadratic_module_with_isometry(T, f; check=true)``
  - Caveat: upstream documents `check=true` by default and validates compatibility; current method list accepts map/hom/matrix/group-element action data (`TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, `MatGroupElem`).
- [ ] ``torsion_quadratic_module_with_isometry(q::QQMatrix, f::ZZMatrix; check=true)``
  - Caveat: upstream documents `check=true` by default and validates the matrix data as a torsion quadratic module with isometry.
- [ ] ``sub(Tf, gens)``
  - Caveat: upstream requires the generated submodule to be stable under the fixed isometry.
- [ ] ``primary_part(Tf, m)``
- [ ] ``orthogonal_submodule(Tf, S; check=true)``
  - Caveat: upstream requires `S` to be stable under the fixed isometry, and `check=true` enforces this precondition.
- [ ] ``submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])``
  - Caveat: current upstream docs expose `quotype` filtering on this surface; accepted selector values are restricted to `0,1,2,3`.
- [ ] ``automorphism_group_with_inclusion(Tf)``
  - Caveat: upstream identifies this with automorphisms in `O(T)` commuting with the fixed isometry.
- [ ] ``automorphism_group(Tf)``
  - Caveat: upstream method list currently typesets `TorQuadModuleWithMap` in one signature location; surrounding page context is `TorQuadModuleWithIsom`.
- [ ] ``is_isomorphic_with_map(Tf, Sg)``
  - Caveat: upstream return contract is `(true, map)` on success and `(false, 0)` on failure.
- [ ] ``is_anti_isomorphic_with_map(Tf, Sg)``
  - Caveat: upstream return contract is `(true, anti_map)` on success and `(false, 0)` on failure.
### References

### Definiteness summary

## 3. Oscar.jl

### Integration points

- [ ] ``Oscar.ZZLat``
- [ ] ``Oscar.to_oscar(obj)``
- [ ] `Lattice databases`
- [ ] ``lll`, `short_vectors`, `close_vectors``
- [ ] `Discriminant groups`
- [ ] `Intersection forms`
- [ ] `Polyhedral integration`
### References

- [ ] `using Oscar`
## 4. Nemo.jl

### 4.1 LLL reduction

- [ ] ``lll(B::ZZMatrix, ctx::LLLContext)``
- [ ] ``lll_with_transform(B)``
- [ ] ``lll_gram(G)``
- [ ] ``lll_gram_with_transform(G)``
- [ ] `lll(B)`
### 4.2 Hermite Normal Form

- [ ] ``hnf(X)` / `AbstractAlgebra.hnf(X)``
- [ ] ``hnf_with_transform(X)``
### 4.3 Smith Normal Form

- [ ] ``snf(X)` / `AbstractAlgebra.snf(X)``
- [ ] ``snf_with_transform(X)``
### 4.4 Other

- [ ] `Echelon form`
- [ ] `Saturation`
### Interaction with Hecke

### References

## 5. LLLplus.jl

### 5.1 Reduction and search

- [ ] ``lll(B)``
- [ ] ``seysen(B)``
- [ ] ``hkz(B)``
- [ ] ``brun(B)``
- [ ] ``cvp(Q, R, y)``
  - Caveat: upstream examples use Euclidean/QR workflows on real matrices; no indefinite-form contract is documented.

### 5.2 Utility workflows

- [ ] ``subsetsum(...)``
- [ ] ``integerfeasibility(...)``
- [ ] ``rationalapprox(...)``

### Definiteness summary

- LLLplus algorithms are documented for Euclidean (positive-definite) workflows; indefinite arithmetic-form classification is out of scope.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 5)
- `https://github.com/chrisvwx/LLLplus.jl`
- `https://chrisvwx.github.io/LLLplus.jl/dev/`

## 6. LatticeAlgorithms.jl

### 6.1 Core methods

- [ ] ``lll(M)``
- [ ] ``islllreduced(B)``
- [ ] ``kz(M)``
- [ ] ``closest_point(x, M)``
- [ ] ``closest_point_Dn(x)``
- [ ] ``Dn(n)``
- [ ] ``distance(M)``
- [ ] ``distances(M)``
  - Caveat: upstream positions these routines in GKP/CVP Euclidean settings; no indefinite-form classification API is documented.

### Definiteness summary

- LatticeAlgorithms.jl routines are used in positive-definite Euclidean decoding/reduction workflows.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 6)
- `https://github.com/QuantumSavory/LatticeAlgorithms.jl`
- `https://github.com/amazon-science/lattice-algorithms`

## 7. Minor Julia Lattice Packages

### 7.1 LatticeBasisReduction.jl

- [ ] ``lll(B::AbstractMatrix{<:Integer}; delta=0.99, eta=0.51)``
- [ ] ``lll!(B::Matrix{BigFloat}; delta=0.99, eta=0.51)``
- [ ] ``islllreduced(B::AbstractMatrix{BigFloat}; delta=0.99, eta=0.51)``
  - Caveat: package exports `lll`; `lll!` and `islllreduced` are documented API surfaces but non-exported.

### 7.2 MinkowskiReduction.jl

- [ ] ``minkReduce(B::AbstractMatrix{<:Integer}; stable=true)``
- [ ] ``deviousMat(n::Int64, m::Int64)``
  - Caveat: upstream documents testing only for low ranks (`n <= 7`) and Euclidean workflows.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 7)
- `https://github.com/MGBoom/LatticeBasisReduction.jl`
- `https://mgboom.github.io/LatticeBasisReduction.jl/stable/API/`
- `https://github.com/glwhart/MinkowskiReduction.jl`
- `https://github.com/glwhart/MinkowskiReduction.jl/blob/master/README.md`

Last updated: 2026-02-18
