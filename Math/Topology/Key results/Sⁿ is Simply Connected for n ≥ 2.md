---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 27.3", "π₁(Sⁿ) = 0"]
tags: [topology, hub]
---
![[Topology §27 The Fundamental Group of Sⁿ#^thm-27-3]]

## Treated in
- [[Topology §27 The Fundamental Group of Sⁿ#^thm-27-3|Theorem §27.3: Sⁿ is Simply Connected for n ≥ 2]], in [[Topology §27 The Fundamental Group of Sⁿ]]

## Its proof uses
- [[Topology §8 Hausdorff Spaces#^thm-8-1|Theorem §8.1: Finite Point Sets are Closed in Hausdorff Spaces]]
- [[Topology §9 Continuous Functions#^def-9-2|Definition §9.2: Homeomorphism]]
- [[Topology §9 Continuous Functions#^prop-9-3|Proposition §9.3: Homeomorphisms Restrict to Subspaces]]
- [[Topology §14 Connected Subspaces of ℝ#^def-14-3|Definition §14.3: Path and Path-Connected]]
- [[Topology §23 The Fundamental Group#^ex-23-1|Example §23.1: ℝⁿ is Simply Connected]]
- [[Topology §23 The Fundamental Group#^cor-23-6|Corollary §23.6: π₁ is a Topological Invariant]]
- [[Topology §26 Deformation Retracts and Homotopy Type#^def-26-6|Definition §26.6: Contractible Space]]
- [[Topology §27 The Fundamental Group of Sⁿ#^cor-27-2|Corollary §27.2: Simply Connected from Open Cover]]

## Used in (Topology)
- [[Topology §27 The Fundamental Group of Sⁿ#^ex-27-1|Example §27.1: Wedge of Two Spheres is Simply Connected]]
- [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-2|Theorem §28.2: π₁(P²) ≅ ℤ/2ℤ]]
- [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-3|Theorem §28.3: π₁(Pⁿ) for all n]]
- [[Topology §28 Fundamental Group of Some Surfaces#^cor-28-6|Corollary §28.6: Four Topologically Distinct Surfaces]]

## Connections
- **Proof.** Cover Sⁿ by the complements of the two poles, each ≅ ℝⁿ by stereographic projection. Their overlap is ≅ ℝⁿ ∖ {0}, which is path-connected for n ≥ 2, so [[Topology §27 The Fundamental Group of Sⁿ#^cor-27-2|Simply Connected from Open Cover]] applies. It is recomputed with the [[Seifert–van Kampen Theorem]] in [[Topology §29 The Seifert–van Kampen Theorem#^ex-29-1|Example §29.1]].
- **Why n ≥ 2.** For n = 1 the overlap is disconnected, and indeed [[Fundamental Group of the Circle]] is ℤ ([[Topology §27 The Fundamental Group of Sⁿ#^rem-27-3|Why n ≥ 2 is Essential]]).
- **Applications.** Sⁿ → Pⁿ is then a simply connected cover, giving [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-3|π₁(Pⁿ) ≅ ℤ/2ℤ]] via [[Properties of the Lifting Correspondence]]. It also gives π₁(ℝⁿ⁺¹ ∖ {0}) = 0 ([[Topology §26 Deformation Retracts and Homotopy Type#^ex-26-7|Example §26.7]]), and it separates S² from the other surfaces in [[Topology §28 Fundamental Group of Some Surfaces#^cor-28-6|Four Topologically Distinct Surfaces]].
- **Limits.** Trivial π₁ does not make Sⁿ contractible ([[Topology §27 The Fundamental Group of Sⁿ#^rem-27-2|remark after §27.3]]). Trivial π₁ is also why π₁ cannot prove the [[Topology §26 Deformation Retracts and Homotopy Type#^thm-26-9|Generalized No-Retraction Theorem]] ([[Topology §26 Deformation Retracts and Homotopy Type#^rem-26-4|Why Our Proof Does Not Generalize]]).
