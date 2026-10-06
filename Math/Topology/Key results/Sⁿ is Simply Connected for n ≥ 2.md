---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 37.3", "π₁(Sⁿ) = 0"]
tags: [topology, hub]
---
![[§37 The Fundamental Group of Sⁿ#^thm-37-3]]

## Treated in
- [[§37 The Fundamental Group of Sⁿ#^thm-37-3|Theorem §37.3: Sⁿ is Simply Connected for n ≥ 2]], in [[§37 The Fundamental Group of Sⁿ]]

## Its proof uses
- [[§9 Hausdorff Spaces#^thm-9-1|Theorem §9.1: Finite Point Sets are Closed in Hausdorff Spaces]]
- [[§10 Continuous Functions#^def-10-2|Definition §10.2: Homeomorphism]]
- [[§10 Continuous Functions#^prop-10-3|Proposition §10.3: Homeomorphisms Restrict to Subspaces]]
- [[§16 Connected Subspaces of ℝ#^def-16-4|Definition §16.4: Path-Connected]]
- [[§29 The Fundamental Group#^ex-29-1|Example §29.1: ℝⁿ is Simply Connected]]
- [[§29 The Fundamental Group#^cor-29-6|Corollary §29.6: π₁ is a Topological Invariant]]
- [[§35 Deformation Retracts and Homotopy Type#^def-35-4|Definition §35.4: Contractible Space]]
- [[§37 The Fundamental Group of Sⁿ#^cor-37-2|Corollary §37.2: Simply Connected from Open Cover]]

## Used in (Topology)
- [[§37 The Fundamental Group of Sⁿ#^ex-37-1|Example §37.1: Wedge of Two Spheres is Simply Connected]]
- [[§38 Fundamental Group of Some Surfaces#^thm-38-2|Theorem §38.2: π₁(P²) ≅ ℤ/2ℤ]]
- [[§38 Fundamental Group of Some Surfaces#^thm-38-3|Theorem §38.3: π₁(Pⁿ) for all n]]
- [[§38 Fundamental Group of Some Surfaces#^cor-38-6|Corollary §38.6: Four Topologically Distinct Surfaces]]

## Connections
- **Proof.** Cover Sⁿ by the complements of the two poles, each ≅ ℝⁿ by stereographic projection. Their overlap is ≅ ℝⁿ ∖ {0}, which is path-connected for n ≥ 2, so [[§37 The Fundamental Group of Sⁿ#^cor-37-2|Simply Connected from Open Cover]] applies. It is recomputed with the [[Seifert–van Kampen Theorem]] in [[§39 The Seifert–van Kampen Theorem#^ex-39-1|Example §39.1]].
- **Why n ≥ 2.** For n = 1 the overlap is disconnected, and indeed [[Fundamental Group of the Circle]] is ℤ ([[§37 The Fundamental Group of Sⁿ#^rem-37-3|Why n ≥ 2 is Essential]]).
- **Applications.** Sⁿ → Pⁿ is then a simply connected cover, giving [[§38 Fundamental Group of Some Surfaces#^thm-38-3|π₁(Pⁿ) ≅ ℤ/2ℤ]] via [[Properties of the Lifting Correspondence]]. It also gives π₁(ℝⁿ⁺¹ ∖ {0}) = 0 ([[§35 Deformation Retracts and Homotopy Type#^ex-35-6|Example §35.6]]), and it separates S² from the other surfaces in [[§38 Fundamental Group of Some Surfaces#^cor-38-6|Four Topologically Distinct Surfaces]].
- **Limits.** Trivial π₁ does not make Sⁿ contractible ([[§37 The Fundamental Group of Sⁿ#^rem-37-2|remark after §27.3]]). Trivial π₁ is also why π₁ cannot prove the [[§34 Retractions and Fixed Points#^thm-34-9|Generalized No-Retraction Theorem]] ([[§34 Retractions and Fixed Points#^rem-34-4|Why Our Proof Does Not Generalize]]).
