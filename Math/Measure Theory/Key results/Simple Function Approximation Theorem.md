---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 12.14", "approximation by simple functions"]
tags: [measure-theory, hub]
---
![[Measure Theory §12 Measurable Functions#^thm-12-14]]

## Treated in
- [[Measure Theory §12 Measurable Functions#^thm-12-14|Theorem §12.14: Approximation by Simple Functions: Non-negative Case]], in [[Measure Theory §12 Measurable Functions]]

## Its proof uses
- [[Measure Theory §12 Measurable Functions#^prop-12-1|Proposition §12.1: Characteristic Functions of Measurable Sets]]
- [[Measure Theory §12 Measurable Functions#^prop-12-2|Proposition §12.2: Equivalent Conditions for Measurability]]
- [[Measure Theory §12 Measurable Functions#^thm-12-3|Theorem §12.3: Arithmetic Operations Preserve Measurability]]
- [[Measure Theory §12 Measurable Functions#^def-12-3|Definition §12.3: Characteristic Function]]
- [[Measure Theory §12 Measurable Functions#^def-12-6|Definition §12.6: Simple Function]]

## Used in (Measure Theory)
- [[Measure Theory §12 Measurable Functions#^thm-12-15|Theorem §12.15: Approximation by Simple Functions: General Case]]
- [[Measure Theory §12 Measurable Functions#^thm-12-17|Theorem §12.17: Uniform Approximation for Bounded Functions]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-1|Theorem §17.1: Translation Invariance]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-3|Theorem §17.3: Tonelli's Theorem]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Theorem §17.11: The Subgraph Theorem]]

## Connections
- **Proof idea.** Cut the range [0, k) into intervals of length 2^(1−k). Set φ_k = (j − 1)/2^(k−1) where (j − 1)/2^(k−1) ≤ f < j/2^(k−1), and φ_k = k where f ≥ k. Halving the intervals makes φ_k increase, and the shrinking mesh gives φ_k → f. Where f is bounded the convergence is uniform ([[Measure Theory §12 Measurable Functions#^thm-12-17|§12.17]]).
- **Riemann vs Lebesgue.** This is Lebesgue's idea of partitioning the range instead of the domain ([[Measure Theory §9 Lebesgue Outer Measure#The Lebesgue Idea|§9]]). Darboux step functions ([[Measure Theory §8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-1|451 Def. §32.1]]) need f to vary little on intervals, while the level sets here only need to be measurable.
- **Used for.** With the [[Monotone Convergence Theorem (Lebesgue)]] it gives ∫φ_k → ∫f, which proves [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity]] (§14.8) and [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]] (§17.1). It is the last step of [[Tonelli's Theorem]] and of the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-11|Subgraph Theorem]]. Its signed version ([[Measure Theory §12 Measurable Functions#^thm-12-15|§12.15]]) with the DCT gives [[Measure Theory §16 The L¹ Space and Density Theorems#^thm-16-5|density of simple functions in L¹]], and its uniform version feeds [[Lusin's Theorem]].
