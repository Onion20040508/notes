---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 6.5", "Lee Proposition 21.4", "Lee Corollary 21.6"]
tags: [differentiable-manifolds, hub]
---
![[§6 Group Actions and Orbit Spaces#^thm-6-5]]

## Treated in
- [[§6 Group Actions and Orbit Spaces#^thm-6-5|Theorem §6.5: Compactness of X Is Not Needed]], in [[§6 Group Actions and Orbit Spaces]]

## Its proof uses
- [[§1 Point-Set Topology Review#^def-1-7|Definition §1.7: Hausdorff (T_2)]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-8|Proposition §3.8: Box Characterization of Open Sets]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Definition §3.10: Graph of a Relation]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|Theorem §3.26: Hausdorff Criterion]]
- [[§6 Group Actions and Orbit Spaces#^def-6-2|Definition §6.2: Continuous Action]]
- [[§6 Group Actions and Orbit Spaces#^lem-6-3|Lemma §6.3: Orbit Relations Are Open]]

## Used in (Differentiable Manifolds)
- (not cited later in the course)

## Connections
- **Used for.** Not cited later: the lecture's version with X compact too ([[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]]) covers every application, namely ℂPⁿ = S²ⁿ⁺¹/U(1) ([[ℂPⁿ Is Hausdorff and Second Countable]]), ℝPⁿ⁻¹ = Sⁿ⁻¹/{±I} ([[§7 Homogeneous Spaces#^rem-7-8|On the Index]]) and G/H for compact G and H ([[§7 Homogeneous Spaces#^cor-7-10|§7.10]]). This version also covers non-compact X, such as SO(3) acting on ℝ³ with orbit space [0, ∞) ([[§6 Group Actions and Orbit Spaces#^ex-6-5|Ex. §6.5]]).
- **Compactness of G is needed.** ℝ⁺ acting on ℝ² ∖ {0} by t·(x, y) = (tx, y/t) satisfies every other hypothesis, yet the orbit space is not Hausdorff: the hyperbola orbits accumulate on the axes ([[§6 Group Actions and Orbit Spaces#^ex-6-6|Ex. §6.6]]). Likewise, if ℂ^× scales all of ℂⁿ⁺¹, every neighbourhood of the orbit {0} is the whole quotient ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-8|Ex. §3.8]]).
- **Same idea elsewhere.** Orbit relations are always open ([[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]]), so by the [[Hausdorff Criterion for Open Quotients]] the content is that the graph of the relation is closed. Compactness of G gives this by the finite-subcover argument of the 590 [[Tube Lemma]], with G as the compact factor. The orbits partition X as in 493 ([[§25 Orbits#^prop-25-1|493 §25.1]]).
- **Coming later in the course.** For Lie groups, properness replaces compactness: if a Lie group acts smoothly, freely and properly on M, then M/G is a smooth manifold (Lee's quotient manifold theorem).
