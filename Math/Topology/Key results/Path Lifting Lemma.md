---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 24.6"]
tags: [topology, hub]
---
![[§24 Covering Spaces#^lem-24-6]]

## Treated in
- [[§24 Covering Spaces#^lem-24-6|Lemma §24.6: Path Lifting Lemma]], in [[§24 Covering Spaces]]

## Its proof uses
- [[§9 Continuous Functions#^thm-9-5|Theorem §9.5: Pasting Lemma]]
- [[§13 Connected Spaces#^thm-13-3|Theorem §13.3: Continuous Image of Connected Space]]
- [[§13 Connected Spaces#^lem-13-4|Lemma §13.4: Connected Subspace and Separation]]
- [[§14 Connected Subspaces of ℝ#^cor-14-2|Corollary §14.2]]
- [[§15 Compact Spaces#^thm-15-10|Theorem §15.10: Closed Intervals are Compact]]
- [[§16 Limit Point Compactness#^lem-16-3|Lemma §16.3: Lebesgue Number Lemma]]

## Used in (Topology)
- [[§24 Covering Spaces#^lem-24-7|Lemma §24.7: Homotopy Lifting Lemma]]
- [[§24 Covering Spaces#^thm-24-8|Theorem §24.8: Lifts of Path-Homotopic Paths]]
- [[§24 Covering Spaces#^thm-24-9|Theorem §24.9: Properties of the Lifting Correspondence]]
- [[§24 Covering Spaces#^thm-24-10|Theorem §24.10: π₁(S¹) ≅ ℤ]]
- [[§28 Fundamental Group of Some Surfaces#^thm-28-4|Theorem §28.4: π₁ of the Figure Eight is Non-Abelian]]

## Connections
- **Proof.** The [[Lebesgue Number Lemma]] subdivides I into pieces mapping into evenly covered sets. Each piece is lifted by a local inverse of p and the pieces are glued with the [[Pasting Lemma]]. Uniqueness holds because a connected image cannot jump between disjoint slices ([[§24 Covering Spaces#^rem-24-5|Role of Each Map]]).
- **Covering hypothesis is needed.** p : ℝ₊ → S¹ is a surjective local homeomorphism but not a covering map, and a clockwise loop from (1, 0) has no lift starting at 1 ([[§24 Covering Spaces#^ex-24-2|Example §24.2]]).
- **Builds.** It leads to the [[Homotopy Lifting Lemma]], the [[§24 Covering Spaces#^def-24-7|lifting correspondence]] and [[Properties of the Lifting Correspondence]], hence [[Fundamental Group of the Circle]]. Explicit lifts also show that the figure eight has non-abelian π₁ ([[§28 Fundamental Group of Some Surfaces#^thm-28-4|Theorem §28.4]]).
- **Also in [[Complex Variables]]:** [[§93 Argument Principle#^lem-93-1|342 Lemma §93.1]] (a continuous argument along a contour: the lift through θ ↦ eⁱᶿ, given by an integral of w′/w; complex-variables version).
