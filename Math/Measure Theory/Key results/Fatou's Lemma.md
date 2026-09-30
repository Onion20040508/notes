---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 14.15", "Fatou"]
tags: [measure-theory, hub]
---
![[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-15]]

## Treated in
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-15|Theorem §14.15: Fatou's Lemma]], in [[Measure Theory §14 The Lebesgue Integral for Simple Functions]]

## Its proof uses
- [[Measure Theory §12 Measurable Functions#^rem-12-4|Remark: Recalling Limsup and Liminf for Sequences]]
- [[Measure Theory §12 Measurable Functions#^thm-12-6|Theorem §12.6: Measurability of Suprema and Infima]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-4|Theorem §14.4: Monotone Convergence Theorem (MCT)]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 §10.3: Lim Sup and Lim Inf]]

## Used in (Measure Theory)
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-6|Theorem §15.6: Dominated Fatou's Lemma]]
- [[Measure Theory §15 The General Lebesgue Integral#^thm-15-8|Theorem §15.8: Dominated Convergence Theorem (DCT)]]
- [[Measure Theory §18 Differentiation Theory#^thm-18-9|Theorem §18.9: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-18|Theorem §19.18: Riesz–Fischer Theorem]]

## Connections
- **Proof idea.** g_k = inf_{j≥k} f_j is measurable ([[Measure Theory §12 Measurable Functions#^thm-12-6|§12.6]]), increases to liminf f_k ([[Measure Theory §12 Measurable Functions#^rem-12-4|Rem. §12.4]]) and satisfies g_k ≤ f_k. The [[Monotone Convergence Theorem (Lebesgue)]] then gives ∫liminf f_k = lim ∫g_k ≤ liminf ∫f_k. It is the middle link of MCT → Fatou → DCT.
- **Where hypotheses matter.** The inequality can be strict: for f_k = k·χ_(0,1/k) the two sides are 0 and 1 ([[Measure Theory §14 The Lebesgue Integral for Simple Functions#^ex-14-1|Ex. §14.1]]), with mass escaping as in the 451 [[Single Variable Analysis §25 More on Uniform Convergence#^ex-25-1|escaping triangle]]. Nonnegativity is needed. For signed functions a dominator replaces it ([[Measure Theory §15 The General Lebesgue Integral#^thm-15-6|§15.6]]).
- **Used for.** The [[Dominated Convergence Theorem]], via the dominated and [[Measure Theory §15 The General Lebesgue Integral#^thm-15-7|reverse]] Fatou lemmas. In [[Riesz–Fischer Theorem|Riesz–Fischer]] it passes from an a.e. convergent subsequence to Lᵖ convergence. In [[Lebesgue's Differentiation Theorem for Monotone Functions]] it bounds ∫f′ through the difference quotients n(f(x + 1/n) − f(x)).
- **Technique.** [[Measure Theory — Problem-Solving Techniques#^rem-19-20|Technique 16: Fatou Squeeze on Complementary Sets]].
