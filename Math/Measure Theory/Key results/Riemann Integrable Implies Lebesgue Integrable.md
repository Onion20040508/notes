---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 15.10"]
tags: [measure-theory, hub]
---
![[Measure Theory §15 The General Lebesgue Integral#^thm-15-10]]

## Treated in
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-10|Theorem §15.10: Riemann Integrability Implies Lebesgue Integrability]], in [[Measure Theory §15 The General Lebesgue Integral]]

## Its proof uses
- [[Measure Theory §8 Motivation꞉ The Riemann Integral#^def-8-3|Definition §8.3: Riemann Integrable]]
- [[Measure Theory §12 Measurable Functions#^prop-12-12|Proposition §12.12: Functions Equal a.e. to Measurable Functions]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^def-14-1|Definition §14.1: Lebesgue Integral of a Non-Negative Simple Function]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-14|Theorem §14.14: Monotone Convergence Theorem — Decreasing Version]]
- [[Measure Theory §15 The General Lebesgue Integral#^ex-15-1|Example §15.1: Bounded Measurable Functions on Finite Measure Sets]]
- [[Measure Theory §15 The General Lebesgue Integral#^def-15-2|Definition §15.2: Step Functions]]
- [[Measure Theory §15 The General Lebesgue Integral#^rem-15-6|Remark: Riemann Integrability via Step Functions]]
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-8|Theorem §15.8: Dominated Convergence Theorem (DCT)]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §32 The Definition of the Riemann Integral#^lem-32-2|451 §32.2: Refinement Lemma]]

## Used in (Measure Theory)
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-13|Theorem §17.13: Layer Cake Formula (Cavalieri's Principle)]]

## Connections
- **Proof idea.** On dyadic partitions, the lower and upper step functions φ_k ≤ f ≤ ψ_k are monotone in k (the 451 [[Single Variable Analysis §32 The Definition of the Riemann Integral#^lem-32-2|Refinement Lemma]]), and their integrals tend to the Riemann integral. The decreasing MCT ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-14|§14.14]]) gives ∫(lim ψ_k − lim φ_k) = 0. Then lim φ_k = f = lim ψ_k a.e. ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]]), so f is measurable ([[Measure Theory §12 Measurable Functions#^prop-12-12|§12.12]]). The constant sup|f| dominates on [a, b] ([[Measure Theory §15 The General Lebesgue Integral#^ex-15-1|Ex. §15.1]]), so the [[Dominated Convergence Theorem|DCT]] gives ∫ f = lim ∫ φ_k.
- **Converse fails.** The Dirichlet function on [0, 1] is not Riemann integrable ([[Measure Theory §8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[Dirichlet and Thomae functions]]), but it is 0 a.e., so its Lebesgue integral is 0.
- **Where hypotheses matter.** The theorem is for proper integrals of bounded functions. Improper Riemann integrals ([[Single Variable Analysis §36 Improper Integrals|451 §36]]) can converge conditionally, like sin x / x on [1, ∞), while the Lebesgue integral is absolute ([[Measure Theory §15 The General Lebesgue Integral#^rem-15-1|Rem. §15.1]]).
- **Used for.** Riemann tools such as the 451 [[Fundamental Theorem of Calculus]] can then evaluate Lebesgue integrals, as in the [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-13|Layer Cake Formula]] (§17.13). The Jordan-content framework of the MATH 452 integral ([[Multivariable Analysis §15 Multivariable Integration#^def-15-10|452 Def. §15.10]]) is likewise superseded by Lebesgue measure.
