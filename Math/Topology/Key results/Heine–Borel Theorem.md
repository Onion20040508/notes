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

## Connections
- **Proof.** Compact ⇒ closed is [[Compact Subspace of a Hausdorff Space is Closed]] (ℝⁿ is a metric space, hence Hausdorff). Closed and bounded ⇒ compact goes through a box [−N, N]ⁿ, which is compact by [[§15 Compact Spaces#^thm-15-10|Closed Intervals are Compact]] and [[§15 Compact Spaces#^thm-15-8|Finite Product of Compact Spaces]] (proved with the [[Tube Lemma]]). The last step is [[Closed Subspace of a Compact Space is Compact]].
- **MATH 451.** With [[Continuous Image of a Compact Space is Compact]] it recovers the [[Extreme Value Theorem]]. In metric spaces, compactness is equivalent to sequential compactness ([[§16 Limit Point Compactness#^thm-16-2|Equivalence for Metrizable Spaces]]), the form met in MATH 451 through [[Bolzano–Weierstrass Theorem]].
- **Failure outside ℝⁿ.** ℤ with the discrete metric is closed and bounded but not compact. Both hypotheses are needed even in ℝ: (0, 1) is bounded but not closed, ℝ is closed but not bounded, and neither is compact ([[§15 Compact Spaces#^rem-15-8|Why Heine-Borel is Fundamental]]). What makes ℝⁿ special is the least upper bound property.
