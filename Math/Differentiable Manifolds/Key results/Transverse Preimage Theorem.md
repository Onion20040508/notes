---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 11.7", "transversality", "Lee Theorem 6.30"]
tags: [differentiable-manifolds, hub]
---
![[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7]]

## Treated in
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7: Preimages of Transverse Level Sets]], in [[§11 Tangent Spaces I꞉ The Geometric Picture]]

## Its proof uses
- [[§4 The Regular Value Theorem#^def-4-2|Definition §4.2: Regular Point and Regular Value]]
- [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3: Regular Value Theorem]]
- [[§9 Manifolds in Euclidean Space#^prop-9-2|Proposition §9.2: Regular Level Sets Are Smooth Manifolds]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-4|Definition §11.4: Codimension]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-5|Definition §11.5: Transversality]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-8|Proposition §11.8: Transversality Is the Regular Value Condition]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-9|Corollary §11.9: The Regular Value Theorem as a Special Case]]

## Connections
- **Used for.** Transversality of F to S = G⁻¹(0) is exactly the regular value condition for G ∘ F ([[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-8|§11.8]]), so the conclusion involves only F and S. The [[Regular Value Theorem (Euclidean)]] is the case S = {c} ([[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-9|§11.9]]), and transverse intersections, with codimensions adding, are the companion statement ([[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-10|§11.10]]).
- **Where it fails.** For S the x-axis in ℝ², F(t) = (t, 0) has a preimage of the wrong dimension, and F(t) = (t, t²) the right dimension but the wrong tangent space; lowering the parabola to (t, t² − ε) makes F transverse ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-6|Ex. §11.6]]). The unit sphere and the plane z = c fail to meet transversally only at c = ±1, where they meet in a point ([[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-5|Ex. §11.5]]).
- **Same idea elsewhere.** For linear subspaces with U + W = ℝᵏ, codimensions add, by dim(U + W) = dim U + dim W − dim(U ∩ W) ([[§6 Dimension#^ladr-2-43|LADR 2.43]]). The theorem is this count applied to tangent spaces.
- **Coming later in the course.** Transversality on manifolds: the same statement for a map between manifolds and a submanifold, and Thom's theorem that any map can be made transverse by an arbitrarily small perturbation, proved with Sard's theorem.
