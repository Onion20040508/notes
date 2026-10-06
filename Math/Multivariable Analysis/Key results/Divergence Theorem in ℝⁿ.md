---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 17.1", "Gauss theorem in ℝⁿ"]
tags: [multivariable-analysis, hub]
---
![[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1]]

## Treated in
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Theorem §17.1: Divergence Theorem in ℝⁿ]], in [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities]]

## Its proof uses
- [[§15 Multivariable Integration#^thm-15-3|Theorem §15.3: Additivity in the Integrand]]
- [[§15 Multivariable Integration#^thm-15-4|Theorem §15.4: Additivity over Domains]]
- [[§15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-1|Definition §17.1: Divergence in ℝⁿ]]
- [[§18 Surface Integrals#^thm-18-1|Theorem §18.1: Surface Area via the Gram Matrix]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|Theorem §17.2: Green's First Identity]]

## Connections
- **Proof idea.** Prove ∫ u_k n_k dS = ∫ ∂u_k/∂x_k dV for each k. Write D as the region between two graphs in x_k, apply [[§15 Multivariable Integration#^thm-15-9|Fubini]] and then the [[Fundamental Theorem of Calculus]] in x_k. On the graphs n_k dS = ±dx′, using the graph area element of [[Surface Area via the Gram Matrix]] (§18.1, cited ahead of its section), and the lateral sides contribute nothing.
- **Special cases.** n = 1 is the [[Fundamental Theorem of Calculus]], n = 2 is [[§16 Line Integrals and Green's Theorem#^thm-16-2|Theorem §16.2]] (the flux form of [[Green's Theorem]]), and n = 3 with parametrized surfaces is [[Divergence Theorem in ℝ³]]. In forms language it is the top-degree case (Ω of dimension n) of the [[Generalized Stokes' Theorem]].
- **Where hypotheses matter.** The region must split into finitely many pieces lying between two C¹ graphs in each coordinate direction. The contributions from the internal cuts cancel because the outward normals on the two sides are opposite.
- **Used for.** Applied to w = u∇v it gives [[Green's First Identity]], and from that [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Green's second identity]] and uniqueness for the [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|Dirichlet problem]].
