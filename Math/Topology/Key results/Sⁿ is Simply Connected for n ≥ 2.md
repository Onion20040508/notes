---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 27.3", "π₁(Sⁿ) = 0"]
tags: [topology, hub]
---
![[§27 The Fundamental Group of Sⁿ#^thm-27-3]]

## Treated in
- [[§27 The Fundamental Group of Sⁿ#^thm-27-3|Theorem §27.3: Sⁿ is Simply Connected for n ≥ 2]], in [[§27 The Fundamental Group of Sⁿ]]

## Its proof uses
- [[§8 Hausdorff Spaces#^thm-8-1|Theorem §8.1: Finite Point Sets are Closed in Hausdorff Spaces]]
- [[§9 Continuous Functions#^def-9-2|Definition §9.2: Homeomorphism]]
- [[§9 Continuous Functions#^prop-9-3|Proposition §9.3: Homeomorphisms Restrict to Subspaces]]
- [[§14 Connected Subspaces of ℝ#^def-14-new1|Definition §14.3: Path-Connected]]
- [[§23 The Fundamental Group#^ex-23-1|Example §23.1: ℝⁿ is Simply Connected]]
- [[§23 The Fundamental Group#^cor-23-6|Corollary §23.6: π₁ is a Topological Invariant]]
- [[§26 Deformation Retracts and Homotopy Type#^def-26-6|Definition §26.6: Contractible Space]]
- [[§27 The Fundamental Group of Sⁿ#^cor-27-2|Corollary §27.2: Simply Connected from Open Cover]]

## Used in (Topology)
- [[§27 The Fundamental Group of Sⁿ#^ex-27-1|Example §27.1: Wedge of Two Spheres is Simply Connected]]
- [[§28 Fundamental Group of Some Surfaces#^thm-28-2|Theorem §28.2: π₁(P²) ≅ ℤ/2ℤ]]
- [[§28 Fundamental Group of Some Surfaces#^thm-28-3|Theorem §28.3: π₁(Pⁿ) for all n]]
- [[§28 Fundamental Group of Some Surfaces#^cor-28-6|Corollary §28.6: Four Topologically Distinct Surfaces]]

## Connections
- **Proof.** Cover Sⁿ by the complements of the two poles, each ≅ ℝⁿ by stereographic projection. Their overlap is ≅ ℝⁿ ∖ {0}, which is path-connected for n ≥ 2, so [[§27 The Fundamental Group of Sⁿ#^cor-27-2|Simply Connected from Open Cover]] applies. It is recomputed with the [[Seifert–van Kampen Theorem]] in [[§29 The Seifert–van Kampen Theorem#^ex-29-1|Example §29.1]].
- **Why n ≥ 2.** For n = 1 the overlap is disconnected, and indeed [[Fundamental Group of the Circle]] is ℤ ([[§27 The Fundamental Group of Sⁿ#^rem-27-3|Why n ≥ 2 is Essential]]).
- **Applications.** Sⁿ → Pⁿ is then a simply connected cover, giving [[§28 Fundamental Group of Some Surfaces#^thm-28-3|π₁(Pⁿ) ≅ ℤ/2ℤ]] via [[Properties of the Lifting Correspondence]]. It also gives π₁(ℝⁿ⁺¹ ∖ {0}) = 0 ([[§26 Deformation Retracts and Homotopy Type#^ex-26-7|Example §26.7]]), and it separates S² from the other surfaces in [[§28 Fundamental Group of Some Surfaces#^cor-28-6|Four Topologically Distinct Surfaces]].
- **Limits.** Trivial π₁ does not make Sⁿ contractible ([[§27 The Fundamental Group of Sⁿ#^rem-27-2|remark after §27.3]]). Trivial π₁ is also why π₁ cannot prove the [[§25a Retractions and Fixed Points#^thm-26-9|Generalized No-Retraction Theorem]] ([[§25a Retractions and Fixed Points#^rem-26-4|Why Our Proof Does Not Generalize]]).
