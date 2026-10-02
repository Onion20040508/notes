---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 10.5", "Lee Proposition 21.4", "Lee Corollary 21.6"]
tags: [differentiable-manifolds, hub]
---
![[§10 Group Actions and Orbit Spaces#^thm-10-5]]

## Treated in
- [[§10 Group Actions and Orbit Spaces#^thm-10-5|Theorem §10.5: Compactness of X Is Not Needed]], in [[§10 Group Actions and Orbit Spaces]]

## Its proof uses
- [[§1 Point-Set Topology Review#^def-1-7|Definition §1.7: Hausdorff (T_2)]]
- [[§3 Subspaces and Products#^prop-3-8|Proposition §3.8: Box Characterization of Open Sets]]
- [[§6 Open Quotients and Complex Projective Space#^def-6-1|Definition §6.1: Graph of a Relation]]
- [[§6 Open Quotients and Complex Projective Space#^thm-6-1|Theorem §6.1: Hausdorff Criterion]]
- [[§10 Group Actions and Orbit Spaces#^def-10-2|Definition §10.2: Continuous Action]]
- [[§10 Group Actions and Orbit Spaces#^lem-10-3|Lemma §10.3: Orbit Relations Are Open]]

## Used in (Differentiable Manifolds)
- (not cited later in the course)

## Connections
- **Used for.** Not cited later: the lecture's version with X compact too ([[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]]) covers every application, namely ℂPⁿ = S²ⁿ⁺¹/U(1) ([[ℂPⁿ Is Hausdorff and Second Countable]]), ℝPⁿ⁻¹ = Sⁿ⁻¹/{±I} ([[§12 The Topology of G∕H and Real Grassmannians#^rem-12-3|On the Index]]) and G/H for compact G and H ([[§12 The Topology of G∕H and Real Grassmannians#^cor-12-5|§12.5]]). This version also covers non-compact X, such as SO(3) acting on ℝ³ with orbit space [0, ∞) ([[§10 Group Actions and Orbit Spaces#^ex-10-5|Ex. §10.5]]).
- **Compactness of G is needed.** ℝ⁺ acting on ℝ² ∖ {0} by t·(x, y) = (tx, y/t) satisfies every other hypothesis, yet the orbit space is not Hausdorff: the hyperbola orbits accumulate on the axes ([[§10 Group Actions and Orbit Spaces#^ex-10-6|Ex. §10.6]]). Likewise, if ℂ^× scales all of ℂⁿ⁺¹, every neighbourhood of the orbit {0} is the whole quotient ([[§6 Open Quotients and Complex Projective Space#^ex-6-2|Ex. §6.2]]).
- **Same idea elsewhere.** Orbit relations are always open ([[§10 Group Actions and Orbit Spaces#^lem-10-3|§10.3]]), so by the [[Hausdorff Criterion for Open Quotients]] the content is that the graph of the relation is closed. Compactness of G gives this by the finite-subcover argument of the 590 [[Tube Lemma]], with G as the compact factor. The orbits partition X as in 493 ([[§25 Orbits#^prop-25-1|493 §25.1]]).
- **Coming later in the course.** For Lie groups, properness replaces compactness: if a Lie group acts smoothly, freely and properly on M, then M/G is a smooth manifold (Lee's quotient manifold theorem).
