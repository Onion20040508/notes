---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 17.2", "Green's identities"]
tags: [multivariable-analysis, hub]
---
![[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2]]

## Treated in
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|Theorem §17.2: Green's First Identity]], in [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities]]

## Its proof uses
- [[§6 Differentiability#^thm-6-4|Theorem §6.4: Product Rule for Partial Derivatives]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Theorem §17.1: Divergence Theorem in ℝⁿ]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Definition §17.2: Gradient]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-new1|Definition §17.2: Laplacian]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-new2|Definition §17.2: Normal Derivative]]

## Used in (Multivariable Analysis)
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|Example §17.1: Uniqueness for the Dirichlet Problem]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-2|Example §17.2: Uniqueness for the Neumann Problem]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Theorem §17.3: Green's Second Identity]]

## Connections
- **Proof.** Apply the [[Divergence Theorem in ℝⁿ]] to w = u∇v, using the [[§6 Differentiability#^thm-6-4|product rule]] to get div w = ∇u·∇v + uΔv. The boundary term uses ∂v/∂n = ∇v·n̂, a [[Directional Derivative Formula|directional derivative]].
- **Generalizes.** For n = 1 it is [[§34 Fundamental Theorem of Calculus#^thm-34-3|Integration by Parts]] (451 §34.3). In ℝ³ it follows the same way from the [[Divergence Theorem in ℝ³]] ([[§18 Surface Integrals#^rem-18-9|Green's Identities Revisited]]).
- **Uniqueness.** With u = v = w harmonic, ∫|∇w|² = 0 forces ∇w = 0 (the analogue of [[§33 Properties of the Riemann Integral#^thm-33-7|451 §33.7]]). So w is constant on a [[§13 Connected Spaces#^def-13-new1|connected]] domain: zero for the [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|Dirichlet problem]], and a constant for the [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-2|Neumann problem]].
- **Symmetry.** Swapping u and v and subtracting gives [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Green's second identity]]: with vanishing boundary terms, Δ is symmetric for the L² inner product. This is the analogue of a self-adjoint operator ([[§22 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]), which has an orthonormal eigenbasis by the [[Real spectral theorem]].
- **Also in [[Fourier Series and PDEs]]:** [[§44★ Problems in Polar Coordinates#^rem-44-2|341 Remark §44.2]] (the case u = v in the plane, which shows that the Dirichlet eigenvalues of the Laplacian are positive).
- **Also in [[Complex Variables]]:** [[§140★ Neumann Problems#^rem-140-1|342 Remark §140.1]] (the case u = 1 on a disk: Neumann data must have mean zero).
