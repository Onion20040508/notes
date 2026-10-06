---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 29.1", "monotone functions are differentiable a.e."]
tags: [measure-theory, hub]
---
![[§29 Lebesgue's Differentiation Theorem#^thm-29-1]]

## Treated in
- [[§29 Lebesgue's Differentiation Theorem#^thm-29-1|Theorem §29.1: Lebesgue's Differentiation Theorem for Monotone Functions]], in [[§29 Lebesgue's Differentiation Theorem]]

## Its proof uses
- [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2: ℚ is countable]]
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§10 Lebesgue Outer Measure#^def-10-4|Definition §10.4: Outer Measure]]
- [[§11 Lebesgue Measurable Sets#^thm-11-3|Theorem §11.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[§15 Measurable Functions#^ex-15-1|Example §15.1: Monotone Functions are Measurable]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|Proposition §21.3: Integrability Implies A.E. Finiteness]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8|Theorem §21.8: Fatou's Lemma]]
- [[§22 The General Lebesgue Integral#^def-22-1|Definition §22.1: Lebesgue Integral of a General Measurable Function]]
- [[§22 The General Lebesgue Integral#^thm-22-2|Theorem §22.2: Linearity]]
- [[§22 The General Lebesgue Integral#^thm-22-4|Theorem §22.4: Countable Additivity of the General Integral]]
- [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|Theorem §25.1: Translation Invariance]]
- [[§28 Differentiation Theory#^def-28-1|Definition §28.1: Vitali Covering]]
- [[§28 Differentiation Theory#^thm-28-2|Theorem §28.2: Vitali Covering Theorem]]
- [[§29 Lebesgue's Differentiation Theorem#^def-29-1|Definition §29.1: Dini Derivatives]]

## Used in (Measure Theory)
- [[§29 Lebesgue's Differentiation Theorem#^cor-29-2|Corollary §29.2: BV Functions are Differentiable A.E.]]
- [[§30 Differentiating the Integral#^thm-30-7|Theorem §30.7: Differentiation of the Integral]]
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-3|Theorem §32.3: Lebesgue Decomposition of Increasing Functions]]

## Connections
- **Proof idea.** f fails to be differentiable where D⁺f > D₋f or D⁻f > D₊f ([[§29 Lebesgue's Differentiation Theorem#^rem-29-3|Rem. §18.3]]). Each bad set is a countable union, over rationals r > s, of sets A_{r,s} = {D⁺f > r > s > D₋f}. Two applications of the [[Vitali Covering Theorem]] give r·m*(A) ≤ s·m*(A), so these sets are null. For (ii)–(iii), f′ is the a.e. limit of n(f(x + 1/n) − f(x)), and [[Fatou's Lemma]] with [[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|translation invariance]] bounds ∫f′ by f(b) − f(a).
- **Where hypotheses matter.** (iii) is only an inequality. The [[§31 Absolute Continuity#^ex-31-1|Cantor function]] has φ′ = 0 a.e. but φ(1) − φ(0) = 1. In the MATH 451 [[Fundamental Theorem of Calculus]] (FTC I), f′ exists everywhere and is Riemann integrable, and equality holds.
- **Chain.** Vitali covering → this theorem → [[§29 Lebesgue's Differentiation Theorem#^cor-29-2|BV functions are differentiable a.e.]] (via [[Jordan Decomposition Theorem|Jordan decomposition]]) → [[§30 Differentiating the Integral#^thm-30-7|F′ = f a.e.]] (§18.26) → [[Fundamental Theorem of Calculus for Lebesgue Integrals]]. It also gives [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^thm-32-3|Lebesgue Decomposition]] (§18.15).
- **Used for.** [[Measure Theory Problem-Solving Techniques#^rem-19-23|Technique 19: Pointwise Bounds via Lebesgue Differentiation]] (HW12 P4). MATH 451 knew that monotone functions are Riemann integrable ([[§33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]); a.e. differentiability is new.
