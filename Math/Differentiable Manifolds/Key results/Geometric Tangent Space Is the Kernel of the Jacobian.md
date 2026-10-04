---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 23.3", "T geo = ker F′", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3]]

## Treated in
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-3|Theorem §23.3: The Geometric Tangent Space Is the Kernel of the Jacobian]], in [[§23 Tangent Spaces I꞉ The Geometric Picture]]

## Its proof uses
- [[§7 The Regular Value Theorem#^def-7-2|Definition §7.2: Regular Point and Regular Value]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-1|Definition §23.1: Geometric Tangent Space]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^lem-23-1|Lemma §23.1: Locality of the Geometric Tangent Space]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^lem-23-2|Lemma §23.2: The Geometric Tangent Space of a Graph]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)
- [[§6 Dimension#^ladr-2-39|LADR 2.39 Subspace of full dimension equals the whole space]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-2|Example §23.2: The Orthogonal Group]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3|Example §23.3: The Unitary Group]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^cor-23-4|Corollary §23.4: Three Descriptions of the Geometric Tangent Space]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|Theorem §23.5: The Classical Groups]]
- [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-7|Theorem §23.7: Dimension of the Geometric Tangent Space]]
- [[§24 Transversality#^thm-24-1|Theorem §24.1: Preimages of Transverse Level Sets]]
- [[§24 Transversality#^prop-24-2|Proposition §24.2: Transversality Is the Regular Value Condition]]
- [[§24 Transversality#^cor-24-3|Corollary §24.3: The Regular Value Theorem as a Special Case]]
- [[§24 Transversality#^prop-24-4|Proposition §24.4: Transverse Intersections]]
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-6|Theorem §27.6: Ambient and Abstract Agree]]
- [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-7|Corollary §27.7: Consequences]]
- [[§33 Submanifolds#^thm-33-6|Theorem §33.6: The Regular Value Theorem for Manifolds]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]

## Connections
- **Used for.** The tangent spaces of the classical groups at I: Skew(n) for O(n), skew-Hermitian matrices for U(n), trace-zero matrices for SL(n,ℝ) ([[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]]). It is the input to the [[Transverse Preimage Theorem]], to transverse intersections ([[§24 Transversality#^prop-24-4|§24.4]]) and to [[Ambient and Abstract Tangent Spaces Agree]], and the [[Regular Value Theorem for Manifolds]] generalizes it to ι_*(T_pS) = ker F_*p.
- **How the proof goes.** Only T^geo_pM ⊆ ker F′(p) is proved directly, by the chain rule. The other inclusion is forced by dimension: the graph lemma ([[§23 Tangent Spaces I꞉ The Geometric Picture#^lem-23-2|§23.2]]) shows T^geo_pM is a subspace of dimension n, and rank–nullity ([[Fundamental theorem of linear maps]]) gives dim ker F′(p) = n ([[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-4|§23, Remark]]).
- **The regular value hypothesis matters.** Take S the x-axis in ℝ², G(x, y) = y and F(t) = (t, t²). The zero set of G ∘ F(t) = t² is the point {0}, whose tangent space is 0, but (G ∘ F)′(0) = 0 has kernel all of ℝ ([[§24 Transversality#^ex-24-2|Ex. §24.2]](b)).
- **Same idea elsewhere.** In 452 this is the geometry of Lagrange multipliers: at a constrained extremum ∇f is orthogonal to the tangent space of the constraint set, so it lies in the span of the constraint gradients ([[Method of Lagrange Multipliers]], [[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 §14.3]]).
