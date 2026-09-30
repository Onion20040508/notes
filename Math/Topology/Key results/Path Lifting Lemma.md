---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 24.6"]
tags: [topology, hub]
---
![[Topology §24 Covering Spaces#^lem-24-6]]

## Treated in
- [[Topology §24 Covering Spaces#^lem-24-6|Lemma §24.6: Path Lifting Lemma]], in [[Topology §24 Covering Spaces]]

## Its proof uses
- [[Topology §9 Continuous Functions#^thm-9-5|Theorem §9.5: Pasting Lemma]]
- [[Topology §13 Connected Spaces#^thm-13-3|Theorem §13.3: Continuous Image of Connected Space]]
- [[Topology §13 Connected Spaces#^lem-13-4|Lemma §13.4: Connected Subspace and Separation]]
- [[Topology §14 Connected Subspaces of ℝ#^cor-14-2|Corollary §14.2]]
- [[Topology §15 Compact Spaces#^thm-15-10|Theorem §15.10: Closed Intervals are Compact]]
- [[Topology §16 Limit Point Compactness#^lem-16-3|Lemma §16.3: Lebesgue Number Lemma]]

## Used in (Topology)
- [[Topology §24 Covering Spaces#^lem-24-7|Lemma §24.7: Homotopy Lifting Lemma]]
- [[Topology §24 Covering Spaces#^thm-24-8|Theorem §24.8: Lifts of Path-Homotopic Paths]]
- [[Topology §24 Covering Spaces#^thm-24-9|Theorem §24.9: Properties of the Lifting Correspondence]]
- [[Topology §24 Covering Spaces#^thm-24-10|Theorem §24.10: π₁(S¹) ≅ ℤ]]
- [[Topology §28 Fundamental Group of Some Surfaces#^thm-28-4|Theorem §28.4: π₁ of the Figure Eight is Non-Abelian]]

## Connections
- **Proof.** The [[Lebesgue Number Lemma]] subdivides I into pieces mapping into evenly covered sets. Each piece is lifted by a local inverse of p and the pieces are glued with the [[Pasting Lemma]]. Uniqueness holds because a connected image cannot jump between disjoint slices ([[Topology §24 Covering Spaces#^rem-24-5|Role of Each Map]]).
- **Covering hypothesis is needed.** p : ℝ₊ → S¹ is a surjective local homeomorphism but not a covering map, and a clockwise loop from (1, 0) has no lift starting at 1 ([[Topology §24 Covering Spaces#^ex-24-2|Example §24.2]]).
- **Builds.** It leads to the [[Homotopy Lifting Lemma]], the [[Topology §24 Covering Spaces#^def-24-7|lifting correspondence]] and [[Properties of the Lifting Correspondence]], hence [[Fundamental Group of the Circle]]. Explicit lifts also show that the figure eight has non-abelian π₁ ([[Topology §28 Fundamental Group of Some Surfaces#^thm-28-4|Theorem §28.4]]).
