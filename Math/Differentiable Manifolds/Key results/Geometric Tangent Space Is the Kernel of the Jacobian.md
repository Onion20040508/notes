---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 20.3", "T geo = ker F′", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3]]

## Treated in
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|Theorem §20.3: The Geometric Tangent Space Is the Kernel of the Jacobian]], in [[§20 Tangent Spaces I꞉ The Geometric Picture]]

## Its proof uses
- [[§7 The Regular Value Theorem#^def-7-2|Definition §7.2: Regular Point and Regular Value]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-1|Lemma §20.1: Locality of the Geometric Tangent Space]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-1|Definition §20.1: Geometric Tangent Space]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|Lemma §20.2: The Geometric Tangent Space of a Graph]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)
- [[§6 Dimension#^ladr-2-39|LADR 2.39 Subspace of full dimension equals the whole space]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-2|Example §20.2: The Orthogonal Group]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-3|Example §20.3: The Unitary Group]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^cor-20-4|Corollary §20.4: Three Descriptions of the Geometric Tangent Space]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|Theorem §20.5: The Classical Groups]]
- [[§21 Transversality#^thm-21-1|Theorem §21.1: Preimages of Transverse Level Sets]]
- [[§21 Transversality#^prop-21-2|Proposition §21.2: Transversality Is the Regular Value Condition]]
- [[§21 Transversality#^cor-21-3|Corollary §21.3: The Regular Value Theorem as a Special Case]]
- [[§21 Transversality#^prop-21-4|Proposition §21.4: Transverse Intersections]]
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|Theorem §24.6: Ambient and Abstract Agree]]
- [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7|Corollary §24.7: Consequences]]
- [[§29 Submanifolds#^thm-29-6|Theorem §29.6: The Regular Value Theorem for Manifolds]]
- [[§29 Submanifolds#^prop-29-8|Proposition §29.8: The Old and New Versions Agree]]

## Connections
- **Used for.** The tangent spaces of the classical groups at I: Skew(n) for O(n), skew-Hermitian matrices for U(n), trace-zero matrices for SL(n,ℝ) ([[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]]). It is the input to the [[Transverse Preimage Theorem]], to transverse intersections ([[§21 Transversality#^prop-21-4|§21.4]]) and to [[Ambient and Abstract Tangent Spaces Agree]], and the [[Regular Value Theorem for Manifolds]] generalizes it to ι_*(T_pS) = ker F_*p.
- **How the proof goes.** Only T^geo_pM ⊆ ker F′(p) is proved directly, by the chain rule. The other inclusion is forced by dimension: the graph lemma ([[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]]) shows T^geo_pM is a subspace of dimension n, and rank–nullity ([[Fundamental theorem of linear maps]]) gives dim ker F′(p) = n ([[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-4|§20, Remark]]).
- **The regular value hypothesis matters.** Take S the x-axis in ℝ², G(x, y) = y and F(t) = (t, t²). The zero set of G ∘ F(t) = t² is the point {0}, whose tangent space is 0, but (G ∘ F)′(0) = 0 has kernel all of ℝ ([[§21 Transversality#^ex-21-2|Ex. §21.2]](b)).
- **Same idea elsewhere.** In 452 this is the geometry of Lagrange multipliers: at a constrained extremum ∇f is orthogonal to the tangent space of the constraint set, so it lies in the span of the constraint gradients ([[Method of Lagrange Multipliers]], [[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 §14.3]]).
