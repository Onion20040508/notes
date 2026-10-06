---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.5", "Lee Proposition 21.4", "Lee Corollary 21.6"]
tags: [differentiable-manifolds, hub]
---
![[§13 Group Actions and Orbit Spaces#^thm-13-5]]

## Treated in
- [[§13 Group Actions and Orbit Spaces#^thm-13-5|Theorem §13.5: Compactness of X Is Not Needed]], in [[§13 Group Actions and Orbit Spaces]]

## Its proof uses
- [[§1 Point-Set Topology Review#^def-1-8|Definition §1.8: Hausdorff (T_2)]]
- [[§3 Subspaces and Products#^prop-3-8|Proposition §3.8: Box Characterization of Open Sets]]
- [[§6 Open Quotients#^def-6-1|Definition §6.1: Graph of a Relation]]
- [[§6 Open Quotients#^thm-6-1|Theorem §6.1: Hausdorff Criterion]]
- [[§13 Group Actions and Orbit Spaces#^def-13-2|Definition §13.2: Continuous Action]]
- [[§13 Group Actions and Orbit Spaces#^lem-13-3|Lemma §13.3: Orbit Relations Are Open]]

## Used in (Differentiable Manifolds)
- (not cited later in the course)

## Connections
- **Used for.** Not cited later: the lecture's version with X compact too ([[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]]) covers every application, namely ℂPⁿ = S²ⁿ⁺¹/U(1) ([[ℂPⁿ Is Hausdorff and Second Countable]]), ℝPⁿ⁻¹ = Sⁿ⁻¹/{±I} ([[§15 The Topology of G∕H and Real Grassmannians#^rem-15-3|On the Index]]) and G/H for compact G and H ([[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]]). This version also covers non-compact X, such as SO(3) acting on ℝ³ with orbit space [0, ∞) ([[§13 Group Actions and Orbit Spaces#^ex-13-5|Ex. §13.5]]).
- **Compactness of G is needed.** ℝ⁺ acting on ℝ² ∖ {0} by t·(x, y) = (tx, y/t) satisfies every other hypothesis, yet the orbit space is not Hausdorff: the hyperbola orbits accumulate on the axes ([[§13 Group Actions and Orbit Spaces#^ex-13-6|Ex. §13.6]]). Likewise, if ℂ^× scales all of ℂⁿ⁺¹, every neighbourhood of the orbit {0} is the whole quotient ([[§9 Complex Projective Space#^ex-9-1|Ex. §9.1]]).
- **Same idea elsewhere.** Orbit relations are always open ([[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]), so by the [[Hausdorff Criterion for Open Quotients]] the content is that the graph of the relation is closed. Compactness of G gives this by the finite-subcover argument of the 590 [[Tube Lemma]], with G as the compact factor. The orbits partition X as in 493 ([[§27 Orbits#^prop-27-1|493 §27.1]]).
- **Coming later in the course.** For Lie groups, properness replaces compactness: if a Lie group acts smoothly, freely and properly on M, then M/G is a smooth manifold (Lee's quotient manifold theorem).
