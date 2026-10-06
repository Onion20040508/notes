---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 28.2", "Green's identities"]
tags: [multivariable-analysis, hub]
---
![[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2]]

## Treated in
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|Theorem §28.2: Green's First Identity]], in [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities]]

## Its proof uses
- [[§8 Algebra of Differentiable Functions#^thm-8-2|Theorem §8.2: Product Rule for Partial Derivatives]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|Theorem §28.1: Divergence Theorem in ℝⁿ]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-2|Definition §28.2: Gradient]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-3|Definition §28.3: Laplacian]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-4|Definition §28.4: Normal Derivative]]

## Used in (Multivariable Analysis)
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|Example §28.1: Uniqueness for the Dirichlet Problem]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-2|Example §28.2: Uniqueness for the Neumann Problem]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|Theorem §28.3: Green's Second Identity]]

## Connections
- **Proof.** Apply the [[Divergence Theorem in ℝⁿ]] to w = u∇v, using the [[§8 Algebra of Differentiable Functions#^thm-8-2|product rule]] to get div w = ∇u·∇v + uΔv. The boundary term uses ∂v/∂n = ∇v·n̂, a [[Directional Derivative Formula|directional derivative]].
- **Generalizes.** For n = 1 it is [[§34 Fundamental Theorem of Calculus#^thm-34-3|Integration by Parts]] (451 §34.3). In ℝ³ it follows the same way from the [[Divergence Theorem in ℝ³]] ([[§32 Flux Integrals and the Divergence Theorem in ℝ³#^rem-32-9|Green's Identities Revisited]]).
- **Uniqueness.** With u = v = w harmonic, ∫|∇w|² = 0 forces ∇w = 0 (the analogue of [[§33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]]). So w is constant on a [[§15 Connected Spaces#^def-15-2|connected]] domain: zero for the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|Dirichlet problem]], and a constant for the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-2|Neumann problem]].
- **Symmetry.** Swapping u and v and subtracting gives [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|Green's second identity]]: with vanishing boundary terms, Δ is symmetric for the L² inner product. This is the analogue of a self-adjoint operator ([[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]), which has an orthonormal eigenbasis by the [[Real spectral theorem]].
- **Also in [[Fourier Series and PDEs]]:** [[§54★ Problems in Polar Coordinates#^rem-54-2|341 Remark §44.2]] (the case u = v in the plane, which shows that the Dirichlet eigenvalues of the Laplacian are positive).
- **Also in [[Complex Variables]]:** [[§140★ Neumann Problems#^rem-140-1|342 Remark §140.1]] (the case u = 1 on a disk: Neumann data must have mean zero).
