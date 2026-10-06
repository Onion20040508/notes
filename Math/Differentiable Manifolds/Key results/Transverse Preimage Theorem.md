---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 24.1", "transversality", "Lee Theorem 6.30"]
tags: [differentiable-manifolds, hub]
---
![[§26 Transversality#^thm-26-1]]

## Treated in
- [[§26 Transversality#^thm-26-1|Theorem §26.1: Preimages of Transverse Level Sets]], in [[§26 Transversality]]

## Its proof uses
- [[§7 The Regular Value Theorem#^def-7-4|Definition §7.4: Regular Point and Regular Value]]
- [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3: Regular Value Theorem]]
- [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2: Regular Level Sets Are Smooth Manifolds]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§26 Transversality#^def-26-1|Definition §26.1: Codimension]]
- [[§26 Transversality#^def-26-2|Definition §26.2: Transversality]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§26 Transversality#^prop-26-2|Proposition §26.2: Transversality Is the Regular Value Condition]]
- [[§26 Transversality#^cor-26-3|Corollary §26.3: The Regular Value Theorem as a Special Case]]

## Connections
- **Used for.** Transversality of F to S = G⁻¹(0) is exactly the regular value condition for G ∘ F ([[§26 Transversality#^prop-26-2|§26.2]]), so the conclusion involves only F and S. The [[Regular Value Theorem (Euclidean)]] is the case S = {c} ([[§26 Transversality#^cor-26-3|§26.3]]), and transverse intersections, with codimensions adding, are the companion statement ([[§26 Transversality#^prop-26-4|§26.4]]).
- **Where it fails.** For S the x-axis in ℝ², F(t) = (t, 0) has a preimage of the wrong dimension, and F(t) = (t, t²) the right dimension but the wrong tangent space; lowering the parabola to (t, t² − ε) makes F transverse ([[§26 Transversality#^ex-26-2|Ex. §26.2]]). The unit sphere and the plane z = c fail to meet transversally only at c = ±1, where they meet in a point ([[§26 Transversality#^ex-26-1|Ex. §26.1]]).
- **Same idea elsewhere.** For linear subspaces with U + W = ℝᵏ, codimensions add, by dim(U + W) = dim U + dim W − dim(U ∩ W) ([[§6 Dimension#^ladr-2-43|LADR 2.43]]). The theorem is this count applied to tangent spaces.
- **Coming later in the course.** Transversality on manifolds: the same statement for a map between manifolds and a submanifold, and Thom's theorem that any map can be made transverse by an arbitrarily small perturbation, proved with Sard's theorem.
