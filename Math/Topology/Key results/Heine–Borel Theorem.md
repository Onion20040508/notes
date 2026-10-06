---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 18.12", "Heine-Borel Theorem", "Heine–Borel"]
tags: [topology, hub]
---
![[§18 Compact Spaces#^thm-18-12]]

## Treated in
- [[§18 Compact Spaces#^thm-18-12|Theorem §18.12: Heine-Borel Theorem for ℝⁿ]], in [[§18 Compact Spaces]]

## Its proof uses
- [[§7 Closed Sets and Limit Points#^thm-7-2|Theorem §7.2: Closed Sets in Subspaces]]
- [[§12 Metric Topology#^thm-12-4|Theorem §12.4: Every Metric Space is Hausdorff]]
- [[§18 Compact Spaces#^lem-18-1|Lemma §18.1: Compactness in Subspaces]]
- [[§18 Compact Spaces#^thm-18-2|Theorem §18.2: Closed Subspace of Compact is Compact]]
- [[§18 Compact Spaces#^thm-18-4|Theorem §18.4: Compact Subspace of Hausdorff is Closed]]
- [[§18 Compact Spaces#^cor-18-11|Corollary §18.11]]

## Used in (Topology)
- (not cited later in the course)

## Used in (Differentiable Manifolds)
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§2 Topological Manifolds#^prop-2-12|Proposition §2.12: Manifolds Are Locally Compact]]
- [[§9 Complex Projective Space#^prop-9-1|Proposition §9.1: ℂPⁿ is Hausdorff and Second Countable]]
- [[§9 Complex Projective Space#^prop-9-2|Proposition §9.2: ℂPⁿ Is Compact]]
- [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Corollary §15.8: Grassmannians as Homogeneous Spaces]]
- [[§17 Differentiable Structures#^prop-17-3|Proposition §17.3: The Circle Needs More Than One Chart]]
- [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|Proposition §18.4: ℂP¹ Is the Riemann Sphere]]
- [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|Corollary §23.2: Consequences]]
- [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-5|Corollary §23.5: U(n) Is Compact]]
- [[§34 Submersions#^cor-34-8|Corollary §34.8: No Submersions from Compact Manifolds to Euclidean Space]]

## Used in (Multivariable Analysis)
- [[§25 Change of Variables on General Domains#^prop-25-2|Proposition §25.2: C¹ Diffeomorphisms Preserve Jordan Measurability]]
- [[§23 Fubini's Theorem#^thm-23-1|Theorem §23.1: Fubini's Theorem — Rectangle Case]]
- [[§23 Fubini's Theorem#^thm-23-2|Theorem §23.2: Fubini for Type I Regions]]

## Used in (Measure Theory)
- [[§30 Differentiating the Integral#^thm-30-1|Theorem §30.1: Continuous Maps Preserve Bounded Closed Sets]]

## Connections
- **Proof.** Compact ⇒ closed is [[Compact Subspace of a Hausdorff Space is Closed]] (ℝⁿ is a metric space, hence Hausdorff). Closed and bounded ⇒ compact goes through a box [−N, N]ⁿ, which is compact by [[§18 Compact Spaces#^thm-18-10|Closed Intervals are Compact]] and [[§18 Compact Spaces#^thm-18-9|Finite Product of Compact Spaces]] (proved with the [[Tube Lemma]]). The last step is [[Closed Subspace of a Compact Space is Compact]].
- **MATH 451.** With [[Continuous Image of a Compact Space is Compact]] it recovers the [[Extreme Value Theorem]]. In metric spaces, compactness is equivalent to sequential compactness ([[§19 Limit Point Compactness#^thm-19-4|Equivalence for Metrizable Spaces]]), the form met in MATH 451 through [[Bolzano–Weierstrass Theorem]].
- **Failure outside ℝⁿ.** ℤ with the discrete metric is closed and bounded but not compact. Both hypotheses are needed even in ℝ: (0, 1) is bounded but not closed, ℝ is closed but not bounded, and neither is compact ([[§18 Compact Spaces#^rem-18-8|Why Heine-Borel is Fundamental]]). What makes ℝⁿ special is the [[§16 Connected Subspaces of ℝ#^def-16-1|least upper bound property]].
- **Measure Theory.** 551 proves closed and bounded ⇒ compact again without products, through countable subcovers and Cantor's nested set theorem: [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|551 Thm. §6.4]] (with [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-3|551 Thm. §6.3]] and [[§5 Topology of ℝⁿ#^thm-5-2|551 Thm. §5.2]]).
- **Functional Analysis.** The theorem fails in every infinite-dimensional normed space, where the closed unit ball is closed and bounded but not compact ([[§20 Compactness and the Unit Ball#^thm-20-5|556 Thm. §20.5]]); in finite dimensions it holds for every norm ([[§20 Compactness and the Unit Ball#^ex-20-1|556 Ex. §20.1]]).
- **Also in [[Complex Variables]]:** [[§18 Continuity#^thm-18-6|342 Thm. §18.6]] (closed bounded regions of ℂ: continuous functions on them are bounded; complex-variables version).
