---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 23.3", "T geo = ker F′", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§25 The Geometric Tangent Space#^thm-25-3]]

## Treated in
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]], in [[§25 The Geometric Tangent Space]]

## Its proof uses
- [[§7 The Regular Value Theorem#^def-7-4|Definition §7.4: Regular Point and Regular Value]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1: Geometric Tangent Space]]
- [[§25 The Geometric Tangent Space#^lem-25-1|Lemma §25.1: Locality of the Geometric Tangent Space]]
- [[§25 The Geometric Tangent Space#^lem-25-2|Lemma §25.2: The Geometric Tangent Space of a Graph]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)
- [[§6 Dimension#^ladr-2-39|LADR 2.39 Subspace of full dimension equals the whole space]]
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§25 The Geometric Tangent Space#^cor-25-4|Corollary §25.4: Three Descriptions of the Geometric Tangent Space]]
- [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5: The Classical Groups]]
- [[§25 The Geometric Tangent Space#^thm-25-7|Theorem §25.7: Dimension of the Geometric Tangent Space]]
- [[§26 Transversality#^thm-26-1|Theorem §26.1: Preimages of Transverse Level Sets]]
- [[§26 Transversality#^prop-26-2|Proposition §26.2: Transversality Is the Regular Value Condition]]
- [[§26 Transversality#^cor-26-3|Corollary §26.3: The Regular Value Theorem as a Special Case]]
- [[§26 Transversality#^prop-26-4|Proposition §26.4: Transverse Intersections]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6: Ambient and Abstract Agree]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-7|Corollary §29.7: Consequences]]
- [[§35 Submanifolds#^prop-35-8|Proposition §35.8: The Old and New Versions Agree]]

## Connections
- **Used for.** The tangent spaces of the classical groups at I: Skew(n) for O(n), skew-Hermitian matrices for U(n), trace-zero matrices for SL(n,ℝ) ([[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]). It is the input to the [[Transverse Preimage Theorem]], to transverse intersections ([[§26 Transversality#^prop-26-4|§26.4]]) and to [[Ambient and Abstract Tangent Spaces Agree]], and the [[Regular Value Theorem for Manifolds]] generalizes it to ι_*(T_pS) = ker F_*p.
- **How the proof goes.** Only T^geo_pM ⊆ ker F′(p) is proved directly, by the chain rule. The other inclusion is forced by dimension: the graph lemma ([[§25 The Geometric Tangent Space#^lem-25-2|§25.2]]) shows T^geo_pM is a subspace of dimension n, and rank–nullity ([[Fundamental theorem of linear maps]]) gives dim ker F′(p) = n ([[§25 The Geometric Tangent Space#^rem-25-4|§23, Remark]]).
- **The regular value hypothesis matters.** Take S the x-axis in ℝ², G(x, y) = y and F(t) = (t, t²). The zero set of G ∘ F(t) = t² is the point {0}, whose tangent space is 0, but (G ∘ F)′(0) = 0 has kernel all of ℝ ([[§26 Transversality#^ex-26-2|Ex. §26.2]](b)).
- **Same idea elsewhere.** In 452 this is the geometry of Lagrange multipliers: at a constrained extremum ∇f is orthogonal to the tangent space of the constraint set, so it lies in the span of the constraint gradients ([[Method of Lagrange Multipliers]], [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 §17.3]]).
