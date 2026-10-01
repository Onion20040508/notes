---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 15.8", "DCT"]
tags: [measure-theory, hub]
---
![[§15 The General Lebesgue Integral#^thm-15-8]]

## Treated in
- [[§15 The General Lebesgue Integral#^thm-15-8|Theorem §15.8: Dominated Convergence Theorem (DCT)]], in [[§15 The General Lebesgue Integral]]

## Its proof uses
- [[§12 Measurable Functions#^rem-12-7|Remark: A.e. Convergence Preserves Measurability]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9: Integral over Null Sets and A.E. Equal Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-15|Theorem §14.15: Fatou's Lemma]]
- [[§15 The General Lebesgue Integral#^prop-15-1|Proposition §15.1: Basic Properties]]
- [[§15 The General Lebesgue Integral#^thm-15-2|Theorem §15.2: Linearity]]
- [[§15 The General Lebesgue Integral#^thm-15-6|Theorem §15.6: Dominated Fatou's Lemma]]
- [[§15 The General Lebesgue Integral#^thm-15-7|Theorem §15.7: Reverse Fatou's Lemma]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6: Convergence via Lim Sup and Lim Inf]]
- [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]
- [[Squeeze Theorem]] (Single Variable Analysis)

## Used in (Measure Theory)
- [[§15 The General Lebesgue Integral#^cor-15-9|Corollary §15.9: Absolute Convergence in L¹]]
- [[§15 The General Lebesgue Integral#^thm-15-10|Theorem §15.10: Riemann Integrability Implies Lebesgue Integrability]]
- [[§16 The L¹ Space and Density Theorems#^lem-16-2|Lemma §16.2]]
- [[§16 The L¹ Space and Density Theorems#^thm-16-3|Theorem §16.3: Tail Decay of the Integral]]
- [[§16 The L¹ Space and Density Theorems#^thm-16-5|Theorem §16.5: Simple Functions are Dense in L¹]]
- [[§18 Differentiation Theory#^cor-18-14|Corollary §18.14: Term-by-Term Differentiation of AC Series]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|Theorem §19.19: Density in Lᵖ]]

## Used in (Functional Analysis)
- [[§14 The Function Spaces Lᵖ(Ω)#^rem-14-2|Remark: What “Integrable” Means Here]]
- [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|Theorem §14.3: Lᵖ(Omega) and L^∞(Omega) are Banach Spaces]]
- [[§26 Position Eigenstates and Continuous Resolutions#^prop-26-5|Proposition §26.5: The Spectral Projections of Position]]

## Connections
- **Proof idea.** Fatou applied to F + f_k and F − f_k gives the [[§15 The General Lebesgue Integral#^thm-15-6|dominated]] (§15.6) and [[§15 The General Lebesgue Integral#^thm-15-7|reverse]] (§15.7) Fatou lemmas. Together they give ∫f ≤ liminf ∫f_k ≤ limsup ∫f_k ≤ ∫f, and [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]] finishes. The alternative proof applies [[Fatou's Lemma]] to 2F − |f_k − f| and gets ∫|f_k − f| → 0 ([[§15 The General Lebesgue Integral#^rem-15-4|Rem. §15.4]]). It is the last link of MCT → Fatou → DCT.
- **Riemann vs Lebesgue.** MATH 451 exchanges limit and integral only under uniform convergence ([[§25 More on Uniform Convergence#^thm-25-1|451 §25.1]], [[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]). On [a, b] a uniformly convergent sequence of bounded functions is dominated by a constant, so the DCT contains these results. It also needs only a.e. convergence.
- **Where hypotheses matter.** Without a dominator, mass can escape. f_k = k·χ_(0,1/k) → 0 pointwise but ∫f_k = 1 ([[§14 The Lebesgue Integral for Simple Functions#^ex-14-1|Ex. §14.1]]). Compare the 451 [[§25 More on Uniform Convergence#^ex-25-1|escaping triangle]].
- **Used for.** [[Riemann Integrable Implies Lebesgue Integrable]] (§15.10), the density theorems ([[§16 The L¹ Space and Density Theorems#^thm-16-5|§16.5]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|§19.19]]) and [[§18 Differentiation Theory#^cor-18-14|term-by-term differentiation]] (§18.14). It is also the tool of [[Measure Theory Problem-Solving Techniques#^rem-19-18|Technique 14: DCT for Parameter-Dependent Integrals]].
