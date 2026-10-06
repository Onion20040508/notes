---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 6.1", "Hausdorff criterion"]
tags: [differentiable-manifolds, hub]
---
![[§6 Open Quotients#^thm-6-1]]

## Treated in
- [[§6 Open Quotients#^thm-6-1|Theorem §6.1: Hausdorff Criterion]], in [[§6 Open Quotients]]

## Its proof uses
- [[§1 Point-Set Topology Review#^def-1-8|Definition §1.8: Hausdorff (T_2)]]
- [[§3 Subspaces and Products#^def-3-3|Definition §3.3: Product Topology]]
- [[§3 Subspaces and Products#^prop-3-8|Proposition §3.8: Box Characterization of Open Sets]]
- [[§4 Quotient Spaces and Open Maps#^def-4-1|Definition §4.1: Quotient Space and Quotient Topology]]
- [[§4 Quotient Spaces and Open Maps#^prop-4-1|Proposition §4.1: The Quotient Topology Is the Finest Making π Continuous]]
- [[§4 Quotient Spaces and Open Maps#^def-4-4|Definition §4.4: Open Equivalence Relation]]
- [[§6 Open Quotients#^def-6-1|Definition §6.1: Graph of a Relation]]

## Used in (Differentiable Manifolds)
- [[§10 The Line with Two Origins#^ex-10-1|Example §10.1: The Line with Two Origins — via the Criterion]]
- [[§6 Open Quotients#^cor-6-2|Corollary §6.2: The Diagonal Criterion]]
- [[§9 Complex Projective Space#^prop-9-1|Proposition §9.1: ℂPⁿ is Hausdorff and Second Countable]]
- [[§13 Group Actions and Orbit Spaces#^cor-13-4|Corollary §13.4: Compact Group and Compact Hausdorff Space]]
- [[§13 Group Actions and Orbit Spaces#^thm-13-5|Theorem §13.5: Compactness of X Is Not Needed]]

## Connections
- **Used for.** The diagonal criterion ([[§6 Open Quotients#^cor-6-2|§6.2]]) and [[ℂPⁿ Is Hausdorff and Second Countable]]. Orbit relations of continuous actions are always open ([[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]]), so the criterion applies to every orbit space: [[Orbit Spaces of Compact Groups Are Hausdorff]], hence G/H for compact G and H ([[§15 The Topology of G∕H and Real Grassmannians#^cor-15-5|§15.5]]) and the Grassmannians.
- **Where it says no.** For the line with two origins the relation is open, but the graph is not closed: ((1/n, 1), (1/n, 2)) lies in it and converges to the pair of origins ([[§10 The Line with Two Origins#^ex-10-1|Ex. §10.1]]). For ℝ⁺ acting on ℝ² ∖ {0} by t·(x, y) = (tx, y/t), openness comes free and the closed-graph half fails, because the hyperbola orbits accumulate on the axes ([[§13 Group Actions and Orbit Spaces#^ex-13-6|Ex. §13.6]], [[§13 Group Actions and Orbit Spaces#^rem-13-7|What the Example Shows]]). Openness is used only for ⇐, and X itself need not be Hausdorff ([[§6 Open Quotients#^rem-6-1|§6, Remark]]).
- **Same idea elsewhere.** In 590, the quotient by the fibres of a continuous surjection onto a Hausdorff space is Hausdorff ([[§13 Quotient Topology#^cor-13-4|590 §13.4]](2)), and a quotient of ℝ can fail to be Hausdorff ([[§13 Quotient Topology#^ex-13-5|590 Ex. §13.5]]). The criterion replaces such case-by-case checks; Lee checks ℝPⁿ and ℂPⁿ one example at a time.
- **Coming later in the course.** For a closed subgroup H of a Lie group G, the coset space G/H is Hausdorff with no compactness assumption (Lee Theorem 21.17).
