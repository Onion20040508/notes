---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 19.5", "Hölder"]
tags: [measure-theory, hub]
---
![[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5]]

## Treated in
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5|Theorem §19.5: Hölder's Inequality]], in [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces]]

## Its proof uses
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9: Integral over Null Sets and A.E. Equal Functions]]
- [[Measure Theory §14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2: The Essential Supremum is Achieved A.E.]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|Lemma §19.4: Young's Inequality]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Definition §19.7: Conjugate Exponents]]

## Used in (Measure Theory)
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Corollary §19.6: Lᵖ Inclusion for Finite Measure Spaces]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-7|Proposition §19.7: Interpolation of Lᵖ Norms]]
- [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-9|Theorem §19.9: Minkowski's Inequality]]

## Connections
- **Proof idea.** Normalize both norms to 1 and apply [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|Young's inequality]] a^θ b^(1−θ) ≤ θa + (1 − θ)b pointwise, with θ = 1/p, a = |f|ᵖ and b = |g|^p′, then integrate. For p = 1, p′ = ∞, use |g| ≤ ‖g‖∞ a.e. ([[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]]).
- **Linear algebra.** p = p′ = 2 is the [[Cauchy–Schwarz inequality]] (LADR 6.14) for the L² inner product ⟨f, g⟩ = ∫fg ([[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-1|Rem. §19.1]]). Its Riemann-integral form for continuous functions is [[Linear Algebra 6A Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].
- **Used for.** It proves [[Minkowski's Inequality]], the first step of Hölder → Minkowski → Riesz–Fischer. It also gives the [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Lᵖ inclusions on finite-measure sets]] (§19.6) and [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-7|interpolation of Lᵖ norms]] (§19.7).
- **Sharpness.** For p = 1, p′ = ∞ the converse holds: if fg is integrable for every integrable f, then g ∈ L∞. HW8 P5(b) proves this with a divergent-series counterexample ([[Measure Theory — Problem-Solving Techniques#^rem-19-22|Technique 18]]).
