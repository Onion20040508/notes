---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 21.8", "Fatou"]
tags: [measure-theory, hub]
---
![[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8]]

## Treated in
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8|Theorem §21.8: Fatou's Lemma]], in [[§21 Consequences of the Monotone Convergence Theorem]]

## Its proof uses
- [[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|Theorem §16.1: Measurability of Suprema and Infima]]
- [[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|Remark: Recalling Limsup and Liminf for Sequences]]
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|Theorem §20.7: Monotone Convergence Theorem (MCT)]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^def-10-3|451 §10.3: Lim Sup and Lim Inf]]

## Used in (Measure Theory)
- [[§23 The Dominated Convergence Theorem#^thm-23-1|Theorem §23.1: Dominated Fatou's Lemma]]
- [[§23 The Dominated Convergence Theorem#^thm-23-3|Theorem §23.3: Dominated Convergence Theorem (DCT)]]
- [[§29 Lebesgue's Differentiation Theorem#^thm-29-1|Theorem §29.1: Lebesgue's Differentiation Theorem for Monotone Functions]]
- [[§35 Lᵖ as a Banach Space#^thm-35-11|Theorem §35.11: Riesz–Fischer Theorem]]

## Used in (Functional Analysis)
- [[§19 The Function Spaces Lᵖ(Ω)#^rem-19-2|Remark: What “Integrable” Means Here]]

## Connections
- **Proof idea.** g_k = inf_{j≥k} f_j is measurable ([[§16 Limits and Positive Parts of Measurable Functions#^thm-16-1|§16.1]]), increases to liminf f_k ([[§16 Limits and Positive Parts of Measurable Functions#^rem-16-4|Rem. §12.4]]) and satisfies g_k ≤ f_k. The [[Monotone Convergence Theorem (Lebesgue)]] then gives ∫liminf f_k = lim ∫g_k ≤ liminf ∫f_k. It is the middle link of MCT → Fatou → DCT.
- **Where hypotheses matter.** The inequality can be strict: for f_k = k·χ_(0,1/k) the two sides are 0 and 1 ([[§21 Consequences of the Monotone Convergence Theorem#^ex-21-1|Ex. §21.1]]), with mass escaping as in the 451 [[§25 More on Uniform Convergence#^ex-25-1|escaping triangle]]. Nonnegativity is needed. For signed functions a dominator replaces it ([[§23 The Dominated Convergence Theorem#^thm-23-1|§23.1]]).
- **Used for.** The [[Dominated Convergence Theorem]], via the dominated and [[§23 The Dominated Convergence Theorem#^thm-23-2|reverse]] Fatou lemmas. In [[Riesz–Fischer Theorem|Riesz–Fischer]] it passes from an a.e. convergent subsequence to Lᵖ convergence. In [[Lebesgue's Differentiation Theorem for Monotone Functions]] it bounds ∫f′ through the difference quotients n(f(x + 1/n) − f(x)).
- **Technique.** [[Measure Theory Problem-Solving Techniques#^rem-19-20|Technique 16: Fatou Squeeze on Complementary Sets]].
