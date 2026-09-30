---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 18.9", "monotone functions are differentiable a.e."]
tags: [measure-theory, hub]
---
![[Measure Theory §18 Differentiation Theory#^thm-18-9]]

## Treated in
- [[Measure Theory §18 Differentiation Theory#^thm-18-9|Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions]], in [[Measure Theory §18 Differentiation Theory]]

## Its proof uses
- [[Measure Theory §3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2: ℚ is countable]]
- [[Measure Theory §9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[Measure Theory §9 Lebesgue Outer Measure#^def-9-4|Definition §9.4: Outer Measure]]
- [[Measure Theory §10 Lebesgue Measurable Sets#^thm-10-3|Theorem §10.3: ℳ is a σ-Algebra with Countable Additivity]]
- [[Measure Theory §12 Measurable Functions#^ex-12-1|Example §12.1: Monotone Functions are Measurable]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-10|Proposition §14.10: Integrability Implies A.E. Finiteness]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-15|Theorem §14.15: Fatou's Lemma]]
- [[Measure Theory §15 The General Lebesgue Integral#^def-15-1|Definition §15.1: Lebesgue Integral of a General Measurable Function]]
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2: Linearity]]
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-4|Theorem §15.4: Countable Additivity of the General Integral]]
- [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-1|Theorem §17.1: Translation Invariance]]
- [[Measure Theory §18 Differentiation Theory#^def-18-1|Definition §18.1: Vitali Covering]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-2|Theorem §18.2: Vitali Covering Theorem]]
- [[Measure Theory §18 Differentiation Theory#^rem-18-3|Remark: Relationship to Differentiability]]
- [[Measure Theory §18 Differentiation Theory#^def-18-3|Definition §18.3: Dini Derivatives]]

## Used in (Measure Theory)
- [[Measure Theory §18 Differentiation Theory#^cor-18-10|Corollary §18.10: BV Functions are Differentiable A.E.]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-15|Theorem §18.15: Lebesgue Decomposition of Increasing Functions]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-26|Theorem §18.26: Differentiation of the Integral]]

## Connections
- **Proof idea.** f fails to be differentiable where D⁺f > D₋f or D⁻f > D₊f ([[Measure Theory §18 Differentiation Theory#^rem-18-3|Rem. §18.3]]). Each bad set is a countable union, over rationals r > s, of sets A_{r,s} = {D⁺f > r > s > D₋f}. Two applications of the [[Vitali Covering Theorem]] give r·m*(A) ≤ s·m*(A), so these sets are null. For (ii)–(iii), f′ is the a.e. limit of n(f(x + 1/n) − f(x)), and [[Fatou's Lemma]] with [[Measure Theory §17 Invariance Properties and Fubini's Theorem#^thm-17-1|translation invariance]] bounds ∫f′ by f(b) − f(a).
- **Where hypotheses matter.** (iii) is only an inequality. The [[Measure Theory §18 Differentiation Theory#^ex-18-4|Cantor function]] has φ′ = 0 a.e. but φ(1) − φ(0) = 1. In the MATH 451 [[Fundamental Theorem of Calculus]] (FTC I), f′ exists everywhere and is Riemann integrable, and equality holds.
- **Chain.** Vitali covering → this theorem → [[Measure Theory §18 Differentiation Theory#^cor-18-10|BV functions are differentiable a.e.]] (via [[Jordan Decomposition Theorem|Jordan decomposition]]) → [[Measure Theory §18 Differentiation Theory#^thm-18-26|F′ = f a.e.]] (§18.26) → [[Fundamental Theorem of Calculus for Lebesgue Integrals]]. It also gives [[Measure Theory §18 Differentiation Theory#^thm-18-15|Lebesgue Decomposition]] (§18.15).
- **Used for.** [[Measure Theory — Problem-Solving Techniques#^rem-19-23|Technique 19: Pointwise Bounds via Lebesgue Differentiation]] (HW12 P4). MATH 451 knew that monotone functions are Riemann integrable ([[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-1|451 §33.1]]); a.e. differentiability is new.
