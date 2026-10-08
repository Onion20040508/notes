---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 28.1", "Gauss theorem in ℝⁿ"]
tags: [multivariable-analysis, hub]
---
![[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1]]

## Treated in
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|Theorem §28.1: Divergence Theorem in ℝⁿ]], in [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities]]

## Its proof uses
- [[§22 Properties of the Integral#^thm-22-2|Theorem §22.2: Additivity in the Integrand]]
- [[§22 Properties of the Integral#^thm-22-3|Theorem §22.3: Additivity over Domains]]
- [[§23 Fubini's Theorem#^thm-23-2|Theorem §23.2: Fubini for Type I Regions]]
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-1|Definition §28.1: Divergence in ℝⁿ]]
- [[§31 Surface Integrals#^thm-31-1|Theorem §31.1: Surface Area via the Gram Matrix]]

## Its proof uses (other subjects)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-2|Theorem §28.2: Green's First Identity]]

## Used in (Functional Analysis)
- [[§33 Sobolev Spaces and Weak Derivatives#^lem-33-2|Lemma §33.2: Integration by Parts against a Test Function]]

## Connections
- **Proof idea.** Prove ∫ u_k n_k dS = ∫ ∂u_k/∂x_k dV for each k. Write D as the region between two graphs in x_k, apply [[§23 Fubini's Theorem#^thm-23-2|Fubini]] and then the [[Fundamental Theorem of Calculus]] in x_k. On the graphs n_k dS = ±dx′, using the graph area element of [[Surface Area via the Gram Matrix]] (§18.1, cited ahead of its section), and the lateral sides contribute nothing.
- **Special cases.** n = 1 is the [[Fundamental Theorem of Calculus]], n = 2 is [[§27 Line Integrals and Green's Theorem#^thm-27-2|Theorem §27.2]] (the flux form of [[Green's Theorem]]), and n = 3 with parametrized surfaces is [[Divergence Theorem in ℝ³]]. In forms language it is the top-degree case (Ω of dimension n) of the [[Generalized Stokes' Theorem]].
- **Where hypotheses matter.** The region must split into finitely many pieces lying between two C¹ graphs in each coordinate direction. The contributions from the internal cuts cancel because the outward normals on the two sides are opposite.
- **Used for.** Applied to w = u∇v it gives [[Green's First Identity]], and from that [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|Green's second identity]] and uniqueness for the [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|Dirichlet problem]].
