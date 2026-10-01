---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 3.26", "Hausdorff criterion"]
tags: [differentiable-manifolds, hub]
---
![[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26]]

## Treated in
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|Theorem §3.26: Hausdorff Criterion]], in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients]]

## Its proof uses
- [[§1 Point-Set Topology Review#^def-1-7|Definition §1.7: Hausdorff (T_2)]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Definition §3.3: Product Topology]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Definition §3.4: Quotient Space and Quotient Topology]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-6|Definition §3.6: Open Equivalence Relation]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-8|Proposition §3.8: Box Characterization of Open Sets]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Definition §3.10: Graph of a Relation]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|Theorem §3.28: Second Countability of Open Quotients]]

## Used in (Differentiable Manifolds)
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-7|Example §3.7: The Line with Two Origins — via the Criterion]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-27|Corollary §3.27: The Diagonal Criterion]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|Proposition §3.29: ℂPⁿ is Hausdorff and Second Countable]]
- [[§6 Group Actions and Orbit Spaces#^cor-6-4|Corollary §6.4: Compact Group and Compact Hausdorff Space]]
- [[§6 Group Actions and Orbit Spaces#^thm-6-5|Theorem §6.5: Compactness of X Is Not Needed]]

## Connections
- **Used for.** The diagonal criterion ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-27|§3.27]]) and [[ℂPⁿ Is Hausdorff and Second Countable]]. Orbit relations of continuous actions are always open ([[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]]), so the criterion applies to every orbit space: [[Orbit Spaces of Compact Groups Are Hausdorff]], hence G/H for compact G and H ([[§7 Homogeneous Spaces#^cor-7-10|§7.10]]) and the Grassmannians.
- **Where it says no.** For the line with two origins the relation is open, but the graph is not closed: ((1/n, 1), (1/n, 2)) lies in it and converges to the pair of origins ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-7|Ex. §3.7]]). For ℝ⁺ acting on ℝ² ∖ {0} by t·(x, y) = (tx, y/t), openness comes free and the closed-graph half fails, because the hyperbola orbits accumulate on the axes ([[§6 Group Actions and Orbit Spaces#^ex-6-6|Ex. §6.6]], [[§6 Group Actions and Orbit Spaces#^rem-6-7|What the Example Shows]]). Openness is used only for ⇐, and X itself need not be Hausdorff ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^rem-3-15|§3, Remark]]).
- **Same idea elsewhere.** In 590, the quotient by the fibres of a continuous surjection onto a Hausdorff space is Hausdorff ([[§12 Quotient Topology#^cor-12-4|590 §12.4]](2)), and a quotient of ℝ can fail to be Hausdorff ([[§12 Quotient Topology#^ex-12-5|590 Ex. §12.5]]). The criterion replaces such case-by-case checks; Lee checks ℝPⁿ and ℂPⁿ one example at a time.
- **Coming later in the course.** For a closed subgroup H of a Lie group G, the coset space G/H is Hausdorff with no compactness assumption (Lee Theorem 21.17).
