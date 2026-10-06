---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 23.3", "DCT"]
tags: [measure-theory, hub]
---
![[§23 The Dominated Convergence Theorem#^thm-23-3]]

## Treated in
- [[§23 The Dominated Convergence Theorem#^thm-23-3|Theorem §23.3: Dominated Convergence Theorem (DCT)]], in [[§23 The Dominated Convergence Theorem]]

## Its proof uses
- [[§17 Simple Functions and Modes of Convergence#^rem-17-7|Remark: A.e. Convergence Preserves Measurability]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|Proposition §21.2: Integral over Null Sets and A.E. Equal Functions]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-8|Theorem §21.8: Fatou's Lemma]]
- [[§22 The General Lebesgue Integral#^prop-22-1|Proposition §22.1: Basic Properties]]
- [[§22 The General Lebesgue Integral#^thm-22-2|Theorem §22.2: Linearity]]
- [[§23 The Dominated Convergence Theorem#^thm-23-1|Theorem §23.1: Dominated Fatou's Lemma]]
- [[§23 The Dominated Convergence Theorem#^thm-23-2|Theorem §23.2: Reverse Fatou's Lemma]]

## Its proof uses (other subjects)
- [[Squeeze Theorem]] (Single Variable Analysis)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6: Convergence via Lim Sup and Lim Inf]]
- [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3: Properties of the Absolute Value]]

## Used in (Measure Theory)
- [[§23 The Dominated Convergence Theorem#^cor-23-4|Corollary §23.4: Absolute Convergence in L¹]]
- [[§23 The Dominated Convergence Theorem#^thm-23-5|Theorem §23.5: Riemann Integrability Implies Lebesgue Integrability]]
- [[§24 The L¹ Space and Density Theorems#^lem-24-1|Lemma §24.1]]
- [[§24 The L¹ Space and Density Theorems#^thm-24-3|Theorem §24.3: Tail Decay of the Integral]]
- [[§24 The L¹ Space and Density Theorems#^thm-24-5|Theorem §24.5: Simple Functions are Dense in L¹]]
- [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^cor-32-2|Corollary §32.2: Term-by-Term Differentiation of AC Series]]
- [[§35 Lᵖ as a Banach Space#^thm-35-12|Theorem §35.12: Density in Lᵖ]]

## Used in (Functional Analysis)
- [[§19 The Function Spaces Lᵖ(Ω)#^rem-19-2|Remark: What “Integrable” Means Here]]
- [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|Theorem §19.3: Lᵖ(Omega) and L^∞(Omega) are Banach Spaces]]
- [[§30 Boundedness and Continuity#^ex-30-2|Example §30.2: The Fourier Transform from L¹ to L^∞]]
- [[§33 Sobolev Spaces and Weak Derivatives#^ex-33-3|Example §33.3: sgn x has No Weak Derivative]]
- [[§33 Sobolev Spaces and Weak Derivatives#^rem-33-3|Remark: Hölder, not Dominated Convergence]]
- [[§37 Position Eigenstates and Continuous Resolutions#^prop-37-5|Proposition §37.5: The Spectral Projections of Position]]

## Connections
- **Proof idea.** Fatou applied to F + f_k gives the [[§23 The Dominated Convergence Theorem#^thm-23-1|dominated]] Fatou lemma (§15.6); the [[§23 The Dominated Convergence Theorem#^thm-23-2|reverse]] one (§15.7) is proved in the notes by applying the decreasing and increasing MCT to the positive and negative parts of g_l = sup_{k≥l} f_k (Fatou applied to F − f_k gives it too). Together they give ∫f ≤ liminf ∫f_k ≤ limsup ∫f_k ≤ ∫f, and [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|451 §10.6]] finishes. The alternative proof applies [[Fatou's Lemma]] to 2F − |f_k − f| and gets ∫|f_k − f| → 0 ([[§23 The Dominated Convergence Theorem#^rem-23-4|Rem. §15.4]]). It is the last link of MCT → Fatou → DCT.
- **Riemann vs Lebesgue.** MATH 451 exchanges limit and integral only under uniform convergence ([[§25 More on Uniform Convergence#^thm-25-1|451 §25.1]], [[§33 Properties of the Riemann Integral#^thm-33-12|451 §33.12]]). On [a, b] a uniformly convergent sequence of bounded functions is dominated by a constant, so the DCT contains these results. It also needs only a.e. convergence.
- **Where hypotheses matter.** Without a dominator, mass can escape. f_k = k·χ_(0,1/k) → 0 pointwise but ∫f_k = 1 ([[§21 Consequences of the Monotone Convergence Theorem#^ex-21-1|Ex. §21.1]]). Compare the 451 [[§25 More on Uniform Convergence#^ex-25-1|escaping triangle]].
- **Used for.** [[Riemann Integrable Implies Lebesgue Integrable]] (§15.10), the density theorems ([[§24 The L¹ Space and Density Theorems#^thm-24-5|§24.5]], [[§35 Lᵖ as a Banach Space#^thm-35-12|§35.12]]) and [[§32 The Fundamental Theorem of Calculus for Lebesgue Integrals#^cor-32-2|term-by-term differentiation]] (§32.2). It is also the tool of [[Measure Theory Problem-Solving Techniques#^rem-19-18|Technique 14: DCT for Parameter-Dependent Integrals]].
