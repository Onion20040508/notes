---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 23.5"]
tags: [measure-theory, hub]
---
![[§23 The Dominated Convergence Theorem#^thm-23-5]]

## Treated in
- [[§23 The Dominated Convergence Theorem#^thm-23-5|Theorem §23.5: Riemann Integrability Implies Lebesgue Integrability]], in [[§23 The Dominated Convergence Theorem]]

## Its proof uses
- [[§8 Motivation꞉ The Riemann Integral#^def-8-3|Definition §8.3: Riemann Integrable]]
- [[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|Proposition §16.7: Functions Equal a.e. to Measurable Functions]]
- [[§20 The Lebesgue Integral for Simple Functions#^def-20-1|Definition §20.1: Lebesgue Integral of a Non-Negative Simple Function]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4: Vanishing Integral for Non-Negative Functions]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|Theorem §21.7: Monotone Convergence Theorem — Decreasing Version]]
- [[§22 The General Lebesgue Integral#^ex-22-1|Example §22.1: Bounded Measurable Functions on Finite Measure Sets]]
- [[§23 The Dominated Convergence Theorem#^def-23-1|Definition §23.1: Step Functions]]
- [[§23 The Dominated Convergence Theorem#^thm-23-3|Theorem §23.3: Dominated Convergence Theorem (DCT)]]
- [[§23 The Dominated Convergence Theorem#^rem-23-6|Remark: Riemann Integrability via Step Functions]]

## Its proof uses (other subjects)
- [[§32 The Definition of the Riemann Integral#^lem-32-1|451 §32.1: Refinement Lemma]]

## Used in (Measure Theory)
- [[§26 Applications of Tonelli's Theorem#^thm-26-7|Theorem §26.7: Layer Cake Formula (Cavalieri's Principle)]]

## Connections
- **Proof idea.** On dyadic partitions, the lower and upper step functions φ_k ≤ f ≤ ψ_k are monotone in k (the 451 [[§32 The Definition of the Riemann Integral#^lem-32-1|Refinement Lemma]]), and their integrals tend to the Riemann integral. The decreasing MCT ([[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|§21.7]]) gives ∫(lim ψ_k − lim φ_k) = 0. Then lim φ_k = f = lim ψ_k a.e. ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]]), so f is measurable ([[§16 Limits and Positive Parts of Measurable Functions#^prop-16-7|§16.7]]). The constant sup|f| dominates on [a, b] ([[§22 The General Lebesgue Integral#^ex-22-1|Ex. §22.1]]), so the [[Dominated Convergence Theorem|DCT]] gives ∫ f = lim ∫ φ_k.
- **Converse fails.** The Dirichlet function on [0, 1] is not Riemann integrable ([[§8 Motivation꞉ The Riemann Integral#^ex-8-2|Ex. §8.2]], [[Dirichlet and Thomae functions]]), but it is 0 a.e., so its Lebesgue integral is 0.
- **Where hypotheses matter.** The theorem is for proper integrals of bounded functions. Improper Riemann integrals ([[§36 Improper Integrals|451 §36]]) can converge conditionally, like sin x / x on [1, ∞), while the Lebesgue integral is absolute ([[§22 The General Lebesgue Integral#^rem-22-1|Rem. §15.1]]).
- **Used for.** Riemann tools such as the 451 [[Fundamental Theorem of Calculus]] can then evaluate Lebesgue integrals, as in the [[§26 Applications of Tonelli's Theorem#^thm-26-7|Layer Cake Formula]] (§17.13). The Jordan-content framework of the MATH 452 integral ([[§21 The Definition of the Integral#^def-21-6|452 Def. §21.6]]) is likewise superseded by Lebesgue measure.
