---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 9.1", "complex projective space is a manifold", "Lee Problem 1-9"]
tags: [differentiable-manifolds, hub]
---
![[§9 Complex Projective Space#^prop-9-1]]

## Treated in
- [[§9 Complex Projective Space#^prop-9-1|Proposition §9.1: ℂPⁿ is Hausdorff and Second Countable]], in [[§9 Complex Projective Space]]

## Its proof uses
- [[§1 Point-Set Topology Review#^ex-1-1|Example §1.1: ℝⁿ with the Usual Topology is Second Countable]]
- [[§1 Point-Set Topology Review#^prop-1-6|Proposition §1.6: Metric Spaces]]
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5: Subspaces Inherit Both Conditions]]
- [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10: Universal Property of the Product]]
- [[§4 Quotient Spaces and Open Maps#^def-4-4|Definition §4.4: Open Equivalence Relation]]
- [[§4 Quotient Spaces and Open Maps#^def-4-5|Definition §4.5: Saturation and Saturated Sets]]
- [[§4 Quotient Spaces and Open Maps#^prop-4-5|Proposition §4.5: Openness via Saturations]]
- [[§6 Open Quotients#^def-6-1|Definition §6.1: Graph of a Relation]]
- [[§6 Open Quotients#^thm-6-1|Theorem §6.1: Hausdorff Criterion]]
- [[§6 Open Quotients#^thm-6-3|Theorem §6.3: Second Countability of Open Quotients]]
- [[§9 Complex Projective Space#^def-9-1|Definition §9.1: Complex Projective Space ℂPⁿ]]

## Its proof uses (other subjects)
- [[Compact Subspace of a Hausdorff Space is Closed]] (Topology)
- [[Continuous Image of a Compact Space is Compact]] (Topology)
- [[Heine–Borel Theorem]] (Topology)
- [[§12 Metric Topology#^thm-12-4|590 §12.4: Every Metric Space is Hausdorff]]
- [[§18 Compact Spaces#^thm-18-9|590 §18.9: Finite Product of Compact Spaces]]
- [[§19 Limit Point Compactness#^thm-19-4|590 §19.4: Equivalence for Metrizable Spaces]]

## Used in (Differentiable Manifolds)
- [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Theorem §18.2: The Standard Atlas Is Smooth]]
- [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|Proposition §18.4: ℂP¹ Is the Riemann Sphere]]
- [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|Corollary §18.5: Real Projective Space]]

## Connections
- **Used for.** With the standard charts, ℂPⁿ becomes a compact smooth manifold of dimension 2n, indeed a complex manifold ([[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-3|§18.3]]), and ℂP¹ is homeomorphic to S² ([[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|§18.4]]). The same argument gives ℝPⁿ ([[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]), and S²ⁿ⁺¹ → ℂPⁿ is the Hopf fibration ([[§39 Projective Spaces and the Hopf Fibration#^ex-39-3|Ex. §39.3]]).
- **The pattern, and where it breaks.** The relation is open because S¹ acts by homeomorphisms, and the graph is closed by compactness ([[§9 Complex Projective Space#^rem-9-3|Where This Is Going]]). The origin must be removed: if ℂ^× scales all of ℂⁿ⁺¹, every neighbourhood of the orbit {0} is the whole quotient ([[§9 Complex Projective Space#^ex-9-1|Ex. §9.1]]). The action is by isometries, uniformly over the group, which is what fails for the hyperbola action of ℝ⁺ ([[§9 Complex Projective Space#^rem-9-1|§9, Remark]], [[§13 Group Actions and Orbit Spaces#^ex-13-6|Ex. §13.6]]).
- **Same idea elsewhere.** It is the case of U(1) acting on S²ⁿ⁺¹ ([[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]]) of [[Orbit Spaces of Compact Groups Are Hausdorff]]. The real analogue is 590's projective space Pⁿ = Sⁿ/(x ∼ −x) ([[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2]], [[Projective plane]]), where S² → P² is a 2-sheeted covering map ([[§38 Fundamental Group of Some Surfaces#^thm-38-1|590 §38.1]]).
- **Coming later in the course.** In the Lie group part of the course, ℂPⁿ is the homogeneous space U(n + 1)/(U(1) × U(n)), which so far has only been checked by counting dimensions ([[§25 The Geometric Tangent Space#^rem-25-9|Dimension Checks through Homogeneous Spaces]]).
