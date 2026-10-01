---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 19.9", "Minkowski"]
tags: [measure-theory, hub]
---
![[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-9]]

## Treated in
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-9|Theorem §19.9: Minkowski's Inequality]], in [[§19 Normed Linear Spaces and Lᵖ Spaces]]

## Its proof uses
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[§15 The General Lebesgue Integral#^prop-15-3|Proposition §15.3: Triangle Inequality]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2: The Essential Supremum is Achieved A.E.]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5|Theorem §19.5: Hölder's Inequality]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Definition §19.7: Conjugate Exponents]]

## Used in (Measure Theory)
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|Theorem §19.10: Lᵖ is a Normed Linear Space]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-11|Corollary §19.11: Minkowski for Finite Sums]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-15|Proposition §19.15: Basic Properties of Lᵖ Convergence]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-17|Corollary §19.17: Lᵖ Convergence Implies A.E. Convergent Subsequence]]

## Used in (Functional Analysis)
- [[§14 The Function Spaces Lᵖ(Ω)#^rem-14-2|Remark: What “Integrable” Means Here]]
- [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-2|Theorem §14.2: Minkowski's Inequality for Functions]]
- [[§20 Orthonormal Sets and Bases#^prop-20-15|Proposition §20.15: Lᵖ(E) is Separable for 1 ≤ p < ∞]]

## Connections
- **Proof idea.** For 1 < p < ∞, write |f + g|ᵖ ≤ |f|·|f + g|^(p−1) + |g|·|f + g|^(p−1). Apply [[Hölder's Inequality]] with exponents p and p′ = p/(p − 1) to each term, then divide by the Lᵖ norm of f + g raised to the power p − 1. p = 1 is [[§15 The General Lebesgue Integral#^prop-15-3|Proposition §15.3]], and p = ∞ is pointwise.
- **Linear algebra.** It is the triangle inequality that makes the Lᵖ norm a norm ([[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-2|Def. §19.2]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-10|§19.10]]). For p = 2 the norm comes from ⟨f, g⟩ = ∫fg, and Minkowski is the inner-product [[Triangle inequality]] (LADR 6.17), just as Hölder is [[Cauchy–Schwarz inequality|Cauchy–Schwarz]]. Among the Lᵖ norms only p = 2 satisfies the [[§19 Inner Products and Norms#^ladr-6-21|parallelogram equality]].
- **Chain.** Hölder → Minkowski → series bounds ([[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-12|§19.12]], via the [[Monotone Convergence Theorem (Lebesgue)]], and [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|§19.14]]) → [[Riesz–Fischer Theorem]]. It also gives [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-15|uniqueness of Lᵖ limits and continuity of the norm]] (§19.15).
