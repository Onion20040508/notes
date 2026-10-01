---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 10.5", "pairing theorem"]
tags: [differentiable-manifolds, hub]
---
![[§10 Vector Spaces and Matrix Groups#^thm-10-5]]

## Treated in
- [[§10 Vector Spaces and Matrix Groups#^thm-10-5|Theorem §10.5: Non-Degenerate Pairings]], in [[§10 Vector Spaces and Matrix Groups]]

## Its proof uses
- [[§10 Vector Spaces and Matrix Groups#^prop-10-1|Proposition §10.1: Standing Facts from Linear Algebra]]
- [[§10 Vector Spaces and Matrix Groups#^prop-10-2|Proposition §10.2: The Dual Basis]]
- [[§10 Vector Spaces and Matrix Groups#^def-10-3|Definition §10.3: Bilinear Pairing]]

## Its proof uses (other subjects)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|Theorem §13.7: The Cotangent Space from Germs]]

## Connections
- **Used for.** [[Cotangent Space from Germs]]: the pairing of T_pM with I_p/I_p², (D, class of f) ↦ D[f], is non-degenerate ([[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-6|§13.6]]), so the theorem gives T_pM ≅ (I_p/I_p²)* and I_p/I_p² ≅ T*_pM at once.
- **Both hypotheses are needed.** Each half of non-degeneracy gives one inequality of dimensions, and only together do they force the isomorphisms. Finite dimension cannot be dropped: for infinite-dimensional V the evaluation pairing of V with V* is non-degenerate, but V → V** is not onto ([[§10 Vector Spaces and Matrix Groups#^rem-10-2|§10, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's duality: dim V′ = dim V ([[§12 Duality#^ladr-3-111|LADR 3.111]]), and V ≅ V** canonically ([[§10 Vector Spaces and Matrix Groups#^prop-10-3|§10.3]]). A real inner product is a non-degenerate pairing of V with itself, and then B^♭ is the isomorphism of the [[Riesz representation theorem]].
- **Coming later in the course.** In de Rham cohomology, (α, β) ↦ ∫ α ∧ β pairs Hᵏ with Hⁿ⁻ᵏ on a compact oriented n-manifold, and Poincaré duality says this pairing is non-degenerate.
