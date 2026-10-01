---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 19.18", "Lᵖ is complete"]
tags: [measure-theory, hub]
---
![[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-18]]

## Treated in
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-18|Theorem §19.18: Riesz–Fischer Theorem]], in [[§19 Normed Linear Spaces and Lᵖ Spaces]]

## Its proof uses
- [[§9 Lebesgue Outer Measure#^prop-9-1|Proposition §9.1: Basic Properties of Outer Measure]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9: Integral over Null Sets and A.E. Equal Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-15|Theorem §14.15: Fatou's Lemma]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2: The Essential Supremum is Achieved A.E.]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-8|Definition §19.8: Lᵖ Convergence and Completeness]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|Lemma §19.16: Cauchy Subsequence Lemma]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]
- [[§24 Uniform Convergence#^def-24-2|451 §24.2: Uniform Convergence]]

## Used in (Measure Theory)
- (not cited later in the course)

## Used in (Functional Analysis)
- [[§14 The Function Spaces Lᵖ(Ω)#^rem-14-2|Remark: What “Integrable” Means Here]]
- [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|Theorem §14.3: Lᵖ(Omega) and L^∞(Omega) are Banach Spaces]]
- [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|Proposition §14.8: Lᵖ[a,b] as a Completion]]

## Connections
- **Proof idea.** A Cauchy sequence has a subsequence whose consecutive differences have summable Lᵖ norms. By the absolute series test ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|§19.14]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-16|Lemma §19.16]]), the subsequence converges a.e. to some f. [[Fatou's Lemma]] then bounds the Lᵖ distance from f_k to f by the liminf over j of the distance from f_k to the j-th subsequence term, which is small. For p = ∞, the convergence is uniform off a null set ([[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Cauchy implies convergent]]).
- **Chain.** Hölder → [[Minkowski's Inequality]] → Riesz–Fischer. The engine is “absolutely convergent series converge”, built on the [[Monotone Convergence Theorem (Lebesgue)|MCT]] ([[§15 The General Lebesgue Integral#^cor-15-9|§15.9]] for p = 1). This is the Lᵖ analogue of [[§14 Series#^prop-14-6|451 §14.6]], and in a normed space it is equivalent to completeness.
- **Riemann vs Lebesgue.** Lᵖ is complete like ℝⁿ ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]). The Riemann integrable functions with the L¹ distance are not: min(n, x^(−1/2)) is L¹-Cauchy on (0, 1] with an unbounded limit. For p = 2, L² is a complete inner product space, extending the inner products of [[§19 Inner Products and Norms#^ladr-6-2|LADR 6.2]].
- **Byproduct.** Lᵖ convergence implies a.e. convergence of a subsequence ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-17|§19.17]]). This is used, ahead of its proof, in [[§18 Differentiation Theory#^thm-18-26|Differentiation of the Integral]] (§18.26).
