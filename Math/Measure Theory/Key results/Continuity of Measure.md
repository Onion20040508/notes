---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 11.12", "continuity from below"]
tags: [measure-theory, hub]
---
![[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-12]]

## Treated in
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-12|Proposition §11.12: Continuity of Measure from Below]], in [[Measure Theory §11 Borel Sets and Measure Spaces]]

## Its proof uses
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-1|Theorem §10.1: Closure Properties of ℳ]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|Lemma §10.2: Finite Additivity for Disjoint Measurable Sets]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]

## Used in (Measure Theory)
- [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-13|Proposition §11.13: Continuity of Measure from Above]]
- [[Measure Theory §11 Borel Sets and Measure Spaces#^thm-11-14|Theorem §11.14: Continuity of Outer Measure from Below via Measurable Exhaustion]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^lem-14-5|Lemma §14.5: Integral over Increasing Sets]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Theorem §17.11: The Subgraph Theorem]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-21|Theorem §19.21: L^∞ is Not Separable]]

## Connections
- **Proof idea.** Write ⋃Eₙ as the disjoint union of the increments E₁, E₂ ∖ E₁, E₃ ∖ E₂, … . Countable additivity ([[Lebesgue Measurable Sets Form a σ-Algebra]]) turns m(⋃Eₙ) into a limit of partial sums, and [[Measure Theory §10 Lebesgue Measurable Sets#^lem-10-2|finite additivity]] identifies the N-th partial sum with m(E_N).
- **From above.** [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-13|Continuity from above]] (§11.13) follows by taking complements inside E₁, so it needs m(E₁) < ∞. Eₙ = [n, ∞) decreases to ∅ with every m(Eₙ) = ∞ ([[Measure Theory §11 Borel Sets and Measure Spaces#^rem-11-5|Rem. §11.5]]). This form drives [[Egorov's Theorem]].
- **Integral analogues.** It gives [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^lem-14-5|Lemma §14.5]], which is the key step of the [[Monotone Convergence Theorem (Lebesgue)]]. The decreasing [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-14|MCT]] (§14.14) needs ∫f_{k₀} < ∞, just as continuity from above needs m(E₁) < ∞ ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^rem-14-5|Rem. §14.5]]).
- **Techniques.** [[Measure Theory — Problem-Solving Techniques#^rem-19-10|Technique 6: Continuity of Measure and Exhaustion]]. It is also used in [[Measure Theory — Problem-Solving Techniques#^rem-19-15|Technique 11]], where the level sets {|f| < n} increase to {f finite}.
