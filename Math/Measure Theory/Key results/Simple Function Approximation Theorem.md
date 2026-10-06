---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 17.2", "approximation by simple functions"]
tags: [measure-theory, hub]
---
![[§17 Simple Functions and Modes of Convergence#^thm-17-2]]

## Treated in
- [[§17 Simple Functions and Modes of Convergence#^thm-17-2|Theorem §17.2: Approximation by Simple Functions: Non-negative Case]], in [[§17 Simple Functions and Modes of Convergence]]

## Its proof uses
- [[§15 Measurable Functions#^prop-15-1|Proposition §15.1: Characteristic Functions of Measurable Sets]]
- [[§15 Measurable Functions#^prop-15-2|Proposition §15.2: Equivalent Conditions for Measurability]]
- [[§15 Measurable Functions#^def-15-3|Definition §15.3: Characteristic Function]]
- [[§15 Measurable Functions#^thm-15-3|Theorem §15.3: Arithmetic Operations Preserve Measurability]]
- [[§17 Simple Functions and Modes of Convergence#^def-17-1|Definition §17.1: Simple Function]]

## Used in (Measure Theory)
- [[§17 Simple Functions and Modes of Convergence#^thm-17-3|Theorem §17.3: Approximation by Simple Functions: General Case]]
- [[§17 Simple Functions and Modes of Convergence#^thm-17-5|Theorem §17.5: Uniform Approximation for Bounded Functions]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1: Linearity of the Integral]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|Theorem §25.1: Translation Invariance]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|Theorem §25.3: Tonelli's Theorem]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-5|Theorem §26.5: The Subgraph Theorem]]

## Connections
- **Proof idea.** Cut the range [0, k) into intervals of length 2^(1−k). Set φ_k = (j − 1)/2^(k−1) where (j − 1)/2^(k−1) ≤ f < j/2^(k−1), and φ_k = k where f ≥ k. Halving the intervals makes φ_k increase, and the shrinking mesh gives φ_k → f. Where f is bounded the convergence is uniform ([[§17 Simple Functions and Modes of Convergence#^thm-17-5|§17.5]]).
- **Riemann vs Lebesgue.** This is Lebesgue's idea of partitioning the range instead of the domain ([[§10 Lebesgue Outer Measure#The Lebesgue Idea|§10]]). Darboux step functions ([[§8 Motivation꞉ The Riemann Integral#^def-8-2|Def. §8.2]], [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]]) need f to vary little on intervals, while the level sets here only need to be measurable.
- **Used for.** With the [[Monotone Convergence Theorem (Lebesgue)]] it gives ∫φ_k → ∫f, which proves [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|linearity]] (§14.8) and [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|translation invariance]] (§17.1). It is the last step of [[Tonelli's Theorem]] and of the [[§26 Applications of Tonelli's Theorem#^thm-26-5|Subgraph Theorem]]. Its signed version ([[§17 Simple Functions and Modes of Convergence#^thm-17-3|§17.3]]) with the DCT gives [[§24 The L¹ Space and Density Theorems#^thm-24-5|density of simple functions in L¹]], and its uniform version feeds [[Lusin's Theorem]].
