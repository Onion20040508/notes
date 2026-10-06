---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 20.7", "MCT"]
tags: [measure-theory, hub]
---
![[§20 The Lebesgue Integral for Simple Functions#^thm-20-7]]

## Treated in
- [[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|Theorem §20.7: Monotone Convergence Theorem (MCT)]], in [[§20 The Lebesgue Integral for Simple Functions]]

## Its proof uses
- [[§15 Measurable Functions#^thm-15-3|Theorem §15.3: Arithmetic Operations Preserve Measurability]]
- [[§16 Limits and Positive Parts of Measurable Functions#^cor-16-3|Corollary §16.3: Pointwise Limits of Measurable Functions]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-1|Proposition §20.1: Linearity]]
- [[§20 The Lebesgue Integral for Simple Functions#^def-20-2|Definition §20.2: Lebesgue Integral of a Non-Negative Measurable Function]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§20 The Lebesgue Integral for Simple Functions#^cor-20-5|Corollary §20.5: Domain Monotonicity]]
- [[§20 The Lebesgue Integral for Simple Functions#^lem-20-6|Lemma §20.6: Integral over Increasing Sets]]

## Its proof uses (other subjects)
- [[Monotone Convergence Theorem]] (Single Variable Analysis)

## Used in (Measure Theory)
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1: Linearity of the Integral]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|Theorem §21.5: MCT II]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-7|Theorem §21.7: Monotone Convergence Theorem — Decreasing Version]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8|Theorem §21.8: Fatou's Lemma]]
- [[§23 The Dominated Convergence Theorem#^thm-23-2|Theorem §23.2: Reverse Fatou's Lemma]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|Theorem §25.1: Translation Invariance]]
- [[§25 Invariance Properties and Fubini's Theorem#^lem-25-5|Lemma §25.5: Closure Properties of 𝓕]]
- [[§26 Applications of Tonelli's Theorem#^thm-26-5|Theorem §26.5: The Subgraph Theorem]]
- [[§35 Lᵖ as a Banach Space#^cor-35-5|Corollary §35.5: Minkowski for Nonnegative Series]]

## Connections
- **Not the 451 theorem.** The MATH 451 [[Monotone Convergence Theorem]] says bounded monotone sequences of reals converge. This theorem exchanges limit and integral for 0 ≤ f_k ↑ f. It uses the 451 result in Step 1, to know that lim ∫f_k exists.
- **Proof idea.** ∫f_k ≤ ∫f by monotonicity. For the reverse, fix a simple h ≤ f and c ∈ (0, 1). The sets {f_k ≥ c·h} increase to E, so [[§20 The Lebesgue Integral for Simple Functions#^lem-20-6|Lemma §20.6]] (from [[Continuity of Measure]]) gives lim ∫f_k ≥ c∫h.
- **Riemann vs Lebesgue.** Riemann integrable functions are not closed under monotone limits: indicators of finite sets of rationals increase to the Dirichlet function ([[§8 Motivation꞉ The Riemann Integral#^rem-8-2|Rem. §8.2]], [[Dirichlet and Thomae functions]]). MATH 451 exchanges limit and integral only under uniform convergence ([[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]).
- **Chain.** MCT → [[Fatou's Lemma]] → [[Dominated Convergence Theorem]]. With the [[Simple Function Approximation Theorem]] it gives [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|linearity]] (§14.8) and the [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-5|series version]] (§14.12), and it gives [[Tonelli's Theorem]] its closure under increasing limits. It is used in [[Measure Theory Problem-Solving Techniques#^rem-19-17|Technique 13]] and [[Measure Theory Problem-Solving Techniques#^rem-19-25|Technique 21]].
