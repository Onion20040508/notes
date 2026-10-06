---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 14.4", "MCT"]
tags: [measure-theory, hub]
---
![[§14 The Lebesgue Integral for Simple Functions#^thm-14-4]]

## Treated in
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-4|Theorem §14.4: Monotone Convergence Theorem (MCT)]], in [[§14 The Lebesgue Integral for Simple Functions]]

## Its proof uses
- [[§12 Measurable Functions#^thm-12-3|Theorem §12.3: Arithmetic Operations Preserve Measurability]]
- [[§12 Measurable Functions#^cor-12-8|Corollary §12.8: Pointwise Limits of Measurable Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-1|Proposition §14.1: Linearity]]
- [[§14 The Lebesgue Integral for Simple Functions#^def-14-2|Definition §14.2: Lebesgue Integral of a Non-Negative Measurable Function]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[§14 The Lebesgue Integral for Simple Functions#^lem-14-5|Lemma §14.5: Integral over Increasing Sets]]
- [[§14 The Lebesgue Integral for Simple Functions#^cor-14-7|Corollary §14.7: Domain Monotonicity]]

## Its proof uses (other subjects)
- [[Monotone Convergence Theorem]] (Single Variable Analysis)

## Used in (Measure Theory)
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|Theorem §14.12: MCT II]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|Theorem §14.14: Monotone Convergence Theorem — Decreasing Version]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-15|Theorem §14.15: Fatou's Lemma]]
- [[§15 The General Lebesgue Integral#^thm-15-7|Theorem §15.7: Reverse Fatou's Lemma]]
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-1|Theorem §17.1: Translation Invariance]]
- [[§17 Invariance Properties and Fubini's Theorem#^lem-17-5|Lemma §17.5: Closure Properties of 𝓕]]
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|Theorem §17.11: The Subgraph Theorem]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|Corollary §19.12: Minkowski for Nonnegative Series]]

## Connections
- **Not the 451 theorem.** The MATH 451 [[Monotone Convergence Theorem]] says bounded monotone sequences of reals converge. This theorem exchanges limit and integral for 0 ≤ f_k ↑ f. It uses the 451 result in Step 1, to know that lim ∫f_k exists.
- **Proof idea.** ∫f_k ≤ ∫f by monotonicity. For the reverse, fix a simple h ≤ f and c ∈ (0, 1). The sets {f_k ≥ c·h} increase to E, so [[§14 The Lebesgue Integral for Simple Functions#^lem-14-5|Lemma §14.5]] (from [[Continuity of Measure]]) gives lim ∫f_k ≥ c∫h.
- **Riemann vs Lebesgue.** Riemann integrable functions are not closed under monotone limits: indicators of finite sets of rationals increase to the Dirichlet function ([[§8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]], [[Dirichlet and Thomae functions]]). MATH 451 exchanges limit and integral only under uniform convergence ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]).
- **Chain.** MCT → [[Fatou's Lemma]] → [[Dominated Convergence Theorem]]. With the [[Simple Function Approximation Theorem]] it gives [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|linearity]] (§14.8) and the [[§14 The Lebesgue Integral for Simple Functions#^thm-14-12|series version]] (§14.12), and it gives [[Tonelli's Theorem]] its closure under increasing limits. It is used in [[Measure Theory Problem-Solving Techniques#^rem-19-17|Technique 13]] and [[Measure Theory Problem-Solving Techniques#^rem-19-25|Technique 21]].
