---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 15.12", "Heine-Borel Theorem", "Heine–Borel"]
tags: [topology, hub]
---
![[§15 Compact Spaces#^thm-15-12]]

## Treated in
- [[§15 Compact Spaces#^thm-15-12|Theorem §15.12: Heine-Borel Theorem for ℝⁿ]], in [[§15 Compact Spaces]]

## Its proof uses
- [[§6 Closed Sets and Limit Points#^thm-6-2|Theorem §6.2: Closed Sets in Subspaces]]
- [[§11 Metric Topology#^thm-11-4|Theorem §11.4: Every Metric Space is Hausdorff]]
- [[§15 Compact Spaces#^lem-15-1|Lemma §15.1: Compactness in Subspaces]]
- [[§15 Compact Spaces#^thm-15-2|Theorem §15.2: Closed Subspace of Compact is Compact]]
- [[§15 Compact Spaces#^thm-15-4|Theorem §15.4: Compact Subspace of Hausdorff is Closed]]
- [[§15 Compact Spaces#^cor-15-11|Corollary §15.11]]

## Used in (Topology)
- (not cited later in the course)

## Used in (Differentiable Manifolds)
- [[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8: Compactness]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|Proposition §3.29: ℂPⁿ is Hausdorff and Second Countable]]
- [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30|Proposition §3.30: ℂPⁿ Is Compact]]
- [[§7 Homogeneous Spaces#^cor-7-13|Corollary §7.13: Grassmannians as Homogeneous Spaces]]
- [[§8 Differentiable Structures#^prop-8-3|Proposition §8.3: The Circle Needs More Than One Chart]]
- [[§8 Differentiable Structures#^prop-8-9|Proposition §8.9: ℂP¹ Is the Riemann Sphere]]
- [[§10 Vector Spaces and Matrix Groups#^cor-10-13|Corollary §10.13: Consequences]]
- [[§10 Vector Spaces and Matrix Groups#^cor-10-16|Corollary §10.16: U(n) Is Compact]]

## Connections
- **Proof.** Compact ⇒ closed is [[Compact Subspace of a Hausdorff Space is Closed]] (ℝⁿ is a metric space, hence Hausdorff). Closed and bounded ⇒ compact goes through a box [−N, N]ⁿ, which is compact by [[§15 Compact Spaces#^thm-15-10|Closed Intervals are Compact]] and [[§15 Compact Spaces#^thm-15-8|Finite Product of Compact Spaces]] (proved with the [[Tube Lemma]]). The last step is [[Closed Subspace of a Compact Space is Compact]].
- **MATH 451.** With [[Continuous Image of a Compact Space is Compact]] it recovers the [[Extreme Value Theorem]]. In metric spaces, compactness is equivalent to sequential compactness ([[§16 Limit Point Compactness#^thm-16-2|Equivalence for Metrizable Spaces]]), the form met in MATH 451 through [[Bolzano–Weierstrass Theorem]].
- **Failure outside ℝⁿ.** ℤ with the discrete metric is closed and bounded but not compact. Both hypotheses are needed even in ℝ: (0, 1) is bounded but not closed, ℝ is closed but not bounded, and neither is compact ([[§15 Compact Spaces#^rem-15-8|Why Heine-Borel is Fundamental]]). What makes ℝⁿ special is the least upper bound property.
- **Measure Theory.** 551 proves closed and bounded ⇒ compact again without products, through countable subcovers and Cantor's nested set theorem: [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-4|551 Thm. §6.4]] (with [[§6 Open Covers and the Heine–Borel Theorem#^thm-6-1|551 Thm. §6.1]] and [[§5 Topology of ℝⁿ#^thm-5-2|551 Thm. §5.2]]).
- **Functional Analysis.** The theorem fails in every infinite-dimensional normed space, where the closed unit ball is closed and bounded but not compact ([[§15 Compactness and the Unit Ball#^thm-15-5|556 Thm. §15.5]]); in finite dimensions it holds for every norm ([[§15 Compactness and the Unit Ball#^ex-15-1|556 Ex. §15.1]]).
