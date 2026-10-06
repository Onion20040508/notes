---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 32.1"]
tags: [topology, hub]
---
![[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1]]

## Treated in
- [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|Lemma §32.1: Path Lifting Lemma]], in [[§31 Covering Spaces]]

## Its proof uses
- [[§10 Continuous Functions#^thm-10-5|Theorem §10.5: Pasting Lemma]]
- [[§15 Connected Spaces#^thm-15-3|Theorem §15.3: Continuous Image of Connected Space]]
- [[§15 Connected Spaces#^lem-15-4|Lemma §15.4: Connected Subspace and Separation]]
- [[§16 Connected Subspaces of ℝ#^cor-16-2|Corollary §16.2]]
- [[§18 Compact Spaces#^thm-18-10|Theorem §18.10: Closed Intervals are Compact]]
- [[§19 Limit Point Compactness#^lem-19-2|Lemma §19.2: Lebesgue Number Lemma]]

## Used in (Topology)
- [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-2|Lemma §32.2: Homotopy Lifting Lemma]]
- [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-3|Theorem §32.3: Lifts of Path-Homotopic Paths]]
- [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|Theorem §32.4: Properties of the Lifting Correspondence]]
- [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-5|Theorem §32.5: π₁(S¹) ≅ ℤ]]
- [[§38 Fundamental Group of Some Surfaces#^thm-38-4|Theorem §38.4: π₁ of the Figure Eight is Non-Abelian]]

## Connections
- **Proof.** The [[Lebesgue Number Lemma]] subdivides I into pieces mapping into evenly covered sets. Each piece is lifted by a local inverse of p and the pieces are glued with the [[Pasting Lemma]]. Uniqueness holds because a connected image cannot jump between disjoint slices ([[§32 Lifting and the Fundamental Group of the Circle#^rem-32-5|Role of Each Map]]).
- **Covering hypothesis is needed.** p : ℝ₊ → S¹ is a surjective local homeomorphism but not a covering map, and a clockwise loop from (1, 0) has no lift starting at 1 ([[§31 Covering Spaces#^ex-31-2|Example §31.2]]).
- **Builds.** It leads to the [[Homotopy Lifting Lemma]], the [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|lifting correspondence]] and [[Properties of the Lifting Correspondence]], hence [[Fundamental Group of the Circle]]. Explicit lifts also show that the figure eight has non-abelian π₁ ([[§38 Fundamental Group of Some Surfaces#^thm-38-4|Theorem §38.4]]).
- **Also in [[Complex Variables]]:** [[§93 Argument Principle#^lem-93-1|342 Lemma §93.1]] (a continuous argument along a contour: the lift through θ ↦ eⁱᶿ, given by an integral of w′/w; complex-variables version).
