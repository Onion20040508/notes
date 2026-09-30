---
subject: math
type: theorem
source: "[[Topology]]"
aliases: ["Topology 15.12", "Heine-Borel Theorem", "Heine–Borel"]
tags: [topology, hub]
---
![[Topology §15 Compact Spaces#^thm-15-12]]

## Treated in
- [[Topology §15 Compact Spaces#^thm-15-12|Theorem §15.12: Heine-Borel Theorem for ℝⁿ]], in [[Topology §15 Compact Spaces]]

## Its proof uses
- [[Topology §6 Closed Sets and Limit Points#^thm-6-2|Theorem §6.2: Closed Sets in Subspaces]]
- [[Topology §11 Metric Topology#^thm-11-4|Theorem §11.4: Every Metric Space is Hausdorff]]
- [[Topology §15 Compact Spaces#^lem-15-1|Lemma §15.1: Compactness in Subspaces]]
- [[Topology §15 Compact Spaces#^thm-15-2|Theorem §15.2: Closed Subspace of Compact is Compact]]
- [[Topology §15 Compact Spaces#^thm-15-4|Theorem §15.4: Compact Subspace of Hausdorff is Closed]]
- [[Topology §15 Compact Spaces#^cor-15-11|Corollary §15.11]]

## Used in (Topology)
- (not cited later in the course)

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^rem-14-10|Remark: The Logical Flow: Necessary to Sufficient]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-8|Theorem §15.8: Fubini's Theorem — Rectangle Case]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Theorem §15.9: Fubini for Type I Regions]]
- [[Multivariable Analysis §15 Multivariable Integration#^prop-15-16|Proposition §15.16: C¹ Diffeomorphisms Preserve Jordan Measurability]]

## Connections
- **Proof.** Compact ⇒ closed is [[Compact Subspace of a Hausdorff Space is Closed]] (ℝⁿ is a metric space, hence Hausdorff). Closed and bounded ⇒ compact goes through a box [−N, N]ⁿ, which is compact by [[Topology §15 Compact Spaces#^thm-15-10|Closed Intervals are Compact]] and [[Topology §15 Compact Spaces#^thm-15-8|Finite Product of Compact Spaces]] (proved with the [[Tube Lemma]]). The last step is [[Closed Subspace of a Compact Space is Compact]].
- **MATH 451.** With [[Continuous Image of a Compact Space is Compact]] it recovers the [[Extreme Value Theorem]]. In metric spaces, compactness is equivalent to sequential compactness ([[Topology §16 Limit Point Compactness#^thm-16-2|Equivalence for Metrizable Spaces]]), the form met in MATH 451 through [[Bolzano–Weierstrass Theorem]].
- **Failure outside ℝⁿ.** ℤ with the discrete metric is closed and bounded but not compact. Both hypotheses are needed even in ℝ: (0, 1) is bounded but not closed, ℝ is closed but not bounded, and neither is compact ([[Topology §15 Compact Spaces#^rem-15-8|Why Heine-Borel is Fundamental]]). What makes ℝⁿ special is the least upper bound property.
