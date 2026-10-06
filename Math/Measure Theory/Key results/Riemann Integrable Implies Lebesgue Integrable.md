---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 15.10"]
tags: [measure-theory, hub]
---
![[§15 The General Lebesgue Integral#^thm-15-10]]

## Treated in
- [[§15 The General Lebesgue Integral#^thm-15-10|Theorem §15.10: Riemann Integrability Implies Lebesgue Integrability]], in [[§15 The General Lebesgue Integral]]

## Its proof uses
- [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Definition §8.3: Riemann Integrable]]
- [[§12 Measurable Functions#^prop-12-12|Proposition §12.12: Functions Equal a.e. to Measurable Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^def-14-1|Definition §14.1: Lebesgue Integral of a Non-Negative Simple Function]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|Theorem §14.14: Monotone Convergence Theorem — Decreasing Version]]
- [[§15 The General Lebesgue Integral#^ex-15-1|Example §15.1: Bounded Measurable Functions on Finite Measure Sets]]
- [[§15 The General Lebesgue Integral#^def-15-2|Definition §15.2: Step Functions]]
- [[§15 The General Lebesgue Integral#^rem-15-6|Remark: Riemann Integrability via Step Functions]]
- [[§15 The General Lebesgue Integral#^thm-15-8|Theorem §15.8: Dominated Convergence Theorem (DCT)]]

## Its proof uses (other subjects)
- [[§32 The Definition of the Riemann Integral#^lem-32-2|451 §32.2: Refinement Lemma]]

## Used in (Measure Theory)
- [[§17 Invariance Properties and Fubini's Theorem#^thm-17-13|Theorem §17.13: Layer Cake Formula (Cavalieri's Principle)]]

## Connections
- **Proof idea.** On dyadic partitions, the lower and upper step functions φ_k ≤ f ≤ ψ_k are monotone in k (the 451 [[§32 The Definition of the Riemann Integral#^lem-32-2|Refinement Lemma]]), and their integrals tend to the Riemann integral. The decreasing MCT ([[§14 The Lebesgue Integral for Simple Functions#^thm-14-14|§14.14]]) gives ∫(lim ψ_k − lim φ_k) = 0. Then lim φ_k = f = lim ψ_k a.e. ([[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|§14.11]]), so f is measurable ([[§12 Measurable Functions#^prop-12-12|§12.12]]). The constant sup|f| dominates on [a, b] ([[§15 The General Lebesgue Integral#^ex-15-1|Ex. §15.1]]), so the [[Dominated Convergence Theorem|DCT]] gives ∫ f = lim ∫ φ_k.
- **Converse fails.** The Dirichlet function on [0, 1] is not Riemann integrable ([[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[Dirichlet and Thomae functions]]), but it is 0 a.e., so its Lebesgue integral is 0.
- **Where hypotheses matter.** The theorem is for proper integrals of bounded functions. Improper Riemann integrals ([[§36 Improper Integrals|451 §36]]) can converge conditionally, like sin x / x on [1, ∞), while the Lebesgue integral is absolute ([[§15 The General Lebesgue Integral#^rem-15-1|Rem. §15.1]]).
- **Used for.** Riemann tools such as the 451 [[Fundamental Theorem of Calculus]] can then evaluate Lebesgue integrals, as in the [[§17 Invariance Properties and Fubini's Theorem#^thm-17-13|Layer Cake Formula]] (§17.13). The Jordan-content framework of the MATH 452 integral ([[§15 Multivariable Integration#^def-15-10|452 Def. §15.10]]) is likewise superseded by Lebesgue measure.
