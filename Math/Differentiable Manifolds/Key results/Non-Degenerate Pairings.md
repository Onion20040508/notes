---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 20.5", "pairing theorem"]
tags: [differentiable-manifolds, hub]
---
![[§20 Linear Algebra Toolkit#^thm-20-5]]

## Treated in
- [[§20 Linear Algebra Toolkit#^thm-20-5|Theorem §20.5: Non-Degenerate Pairings]], in [[§20 Linear Algebra Toolkit]]

## Its proof uses
- [[§20 Linear Algebra Toolkit#^prop-20-1|Proposition §20.1: Standing Facts from Linear Algebra]]
- [[§20 Linear Algebra Toolkit#^prop-20-2|Proposition §20.2: The Dual Basis]]
- [[§20 Linear Algebra Toolkit#^def-20-3|Definition §20.3: Bilinear Pairing]]

## Its proof uses (other subjects)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§30 Tangent Spaces III꞉ The Cotangent Space#^thm-30-7|Theorem §30.7: The Cotangent Space from Germs]]

## Connections
- **Used for.** [[Cotangent Space from Germs]]: the pairing of T_pM with I_p/I_p², (D, class of f) ↦ D[f], is non-degenerate ([[§30 Tangent Spaces III꞉ The Cotangent Space#^prop-30-6|§30.6]]), so the theorem gives T_pM ≅ (I_p/I_p²)* and I_p/I_p² ≅ T*_pM at once.
- **Both hypotheses are needed.** Each half of non-degeneracy gives one inequality of dimensions, and only together do they force the isomorphisms. Finite dimension cannot be dropped: for infinite-dimensional V the evaluation pairing of V with V* is non-degenerate, but V → V** is not onto ([[§20 Linear Algebra Toolkit#^rem-20-2|§20, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's duality: dim V′ = dim V ([[§12 Duality#^ladr-3-111|LADR 3.111]]), and V ≅ V** canonically ([[§20 Linear Algebra Toolkit#^prop-20-3|§20.3]]). A real inner product is a non-degenerate pairing of V with itself, and then B^♭ is the isomorphism of the [[Riesz representation theorem]].
- **Coming later in the course.** In de Rham cohomology, (α, β) ↦ ∫ α ∧ β pairs Hᵏ with Hⁿ⁻ᵏ on a compact oriented n-manifold, and Poincaré duality says this pairing is non-degenerate.
