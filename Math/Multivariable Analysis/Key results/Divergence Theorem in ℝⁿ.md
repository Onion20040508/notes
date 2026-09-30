---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 17.1", "Gauss theorem in ℝⁿ"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1]]

## Treated in
- [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Theorem §17.1: Divergence Theorem in ℝⁿ]], in [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities]]

## Its proof uses
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|Theorem §15.3: Additivity in the Integrand]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]
- [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-1|Definition §17.1: Divergence in ℝⁿ]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|Theorem §17.2: Green's First Identity]]

## Connections
- **Proof idea.** Prove ∫ u_k n_k dS = ∫ ∂u_k/∂x_k dV for each k. Write D as the region between two graphs in x_k, apply [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Fubini]] and then the [[Fundamental Theorem of Calculus]] in x_k. On the graphs n_k dS = ±dx′, and the lateral sides contribute nothing.
- **Special cases.** n = 1 is the [[Fundamental Theorem of Calculus]], n = 2 is [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Theorem §16.2]] (the flux form of [[Green's Theorem]]), and n = 3 with parametrized surfaces is [[Divergence Theorem in ℝ³]]. In forms language it is the top-degree case (Ω of dimension n) of the [[Generalized Stokes' Theorem]].
- **Where hypotheses matter.** The region must split into finitely many pieces lying between two C¹ graphs in each coordinate direction. The contributions from the internal cuts cancel because the outward normals on the two sides are opposite.
- **Used for.** Applied to w = u∇v it gives [[Green's First Identity]], and from that [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Green's second identity]] and uniqueness for the [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|Dirichlet problem]].
