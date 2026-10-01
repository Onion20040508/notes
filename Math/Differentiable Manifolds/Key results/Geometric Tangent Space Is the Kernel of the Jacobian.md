---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 11.3", "T geo = ker F′", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3]]

## Treated in
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]], in [[§11 Tangent Spaces I꞉ The Geometric Picture]]

## Its proof uses
- [[§4 The Regular Value Theorem#^def-4-2|Definition §4.2: Regular Point and Regular Value]]
- [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3: Regular Value Theorem]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1: Geometric Tangent Space]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|Lemma §11.1: Locality of the Geometric Tangent Space]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|Lemma §11.2: The Geometric Tangent Space of a Graph]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)
- [[§6 Dimension#^ladr-2-39|LADR 2.39 Subspace of full dimension equals the whole space]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Example §11.2: The Orthogonal Group]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|Example §11.3: The Unitary Group]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-4|Corollary §11.4: Three Descriptions of the Geometric Tangent Space]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5: The Classical Groups]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7: Preimages of Transverse Level Sets]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-8|Proposition §11.8: Transversality Is the Regular Value Condition]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-9|Corollary §11.9: The Regular Value Theorem as a Special Case]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-10|Proposition §11.10: Transverse Intersections]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Theorem §12.8: Ambient and Abstract Agree]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20|Corollary §12.20: Consequences]]
- [[§15 Submanifolds#^thm-15-6|Theorem §15.6: The Regular Value Theorem for Manifolds]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** The tangent spaces of the classical groups at I: Skew(n) for O(n), skew-Hermitian matrices for U(n), trace-zero matrices for SL(n,ℝ) ([[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]]). It is the input to the [[Transverse Preimage Theorem]], to transverse intersections ([[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-10|§11.10]]) and to [[Ambient and Abstract Tangent Spaces Agree]], and the [[Regular Value Theorem for Manifolds]] generalizes it to ι_*(T_pS) = ker F_*p.
- **How the proof goes.** Only T^geo_pM ⊆ ker F′(p) is proved directly, by the chain rule. The other inclusion is forced by dimension: the graph lemma ([[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]]) shows T^geo_pM is a subspace of dimension n, and rank–nullity ([[Fundamental theorem of linear maps]]) gives dim ker F′(p) = n ([[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-4|§11, Remark]]).
- **The regular value hypothesis matters.** Take S the x-axis in ℝ², G(x, y) = y and F(t) = (t, t²). The zero set of G ∘ F(t) = t² is the point {0}, whose tangent space is 0, but (G ∘ F)′(0) = 0 has kernel all of ℝ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-6|Ex. §11.6]](b)).
- **Same idea elsewhere.** In 452 this is the geometry of Lagrange multipliers: at a constrained extremum ∇f is orthogonal to the tangent space of the constraint set, so it lies in the span of the constraint gradients ([[Method of Lagrange Multipliers]], [[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 §14.3]]).
