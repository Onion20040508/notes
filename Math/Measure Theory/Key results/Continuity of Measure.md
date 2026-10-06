---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 13.4", "continuity from below"]
tags: [measure-theory, hub]
---
![[§13 Approximation and Continuity of Measure#^prop-13-4]]

## Treated in
- [[§13 Approximation and Continuity of Measure#^prop-13-4|Proposition §13.4: Continuity of Measure from Below]], in [[§13 Approximation and Continuity of Measure]]

## Its proof uses
- [[§11 Lebesgue Measurable Sets#^thm-11-1|Theorem §11.1: Closure Properties of ℳ]]
- [[§11 Lebesgue Measurable Sets#^lem-11-2|Lemma §11.2: Finite Additivity for Disjoint Measurable Sets]]
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]]

## Used in (Measure Theory)
- [[§13 Approximation and Continuity of Measure#^prop-13-5|Proposition §13.5: Continuity of Measure from Above]]
- [[§13 Approximation and Continuity of Measure#^thm-13-7|Theorem §13.7: Continuity of Outer Measure from Below via Measurable Exhaustion]]
- [[§20 The Lebesgue Integral for Simple Functions#^lem-20-6|Lemma §20.6: Integral over Increasing Sets]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-5|Theorem §26.5: The Subgraph Theorem]]
- [[§35 Lᵖ as a Banach Space#^thm-35-14|Theorem §35.14: L^∞ is Not Separable]]

## Connections
- **Proof idea.** Write ⋃Eₙ as the disjoint union of the increments E₁, E₂ ∖ E₁, E₃ ∖ E₂, … . Countable additivity ([[Lebesgue Measurable Sets Form a σ-Algebra]]) turns m(⋃Eₙ) into a limit of partial sums, and [[§11 Lebesgue Measurable Sets#^lem-11-2|finite additivity]] identifies the N-th partial sum with m(E_N).
- **From above.** [[§13 Approximation and Continuity of Measure#^prop-13-5|Continuity from above]] (§11.13) follows by taking complements inside E₁, so it needs m(E₁) < ∞. Eₙ = [n, ∞) decreases to ∅ with every m(Eₙ) = ∞ ([[§13 Approximation and Continuity of Measure#^rem-13-5|Rem. §11.5]]). This form drives [[Egorov's Theorem]].
- **Integral analogues.** It gives [[§20 The Lebesgue Integral for Simple Functions#^lem-20-6|Lemma §20.6]], which is the key step of the [[Monotone Convergence Theorem (Lebesgue)]]. The decreasing [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|MCT]] (§14.14) needs ∫f_{k₀} < ∞, just as continuity from above needs m(E₁) < ∞ ([[§21 Consequences of the Monotone Convergence Theorem#^rem-21-5|Rem. §14.5]]).
- **Techniques.** [[Measure Theory Problem-Solving Techniques#^rem-19-10|Technique 6: Continuity of Measure and Exhaustion]]. It is also used in [[Measure Theory Problem-Solving Techniques#^rem-19-15|Technique 11]], where the level sets {|f| < n} increase to {f finite}.
