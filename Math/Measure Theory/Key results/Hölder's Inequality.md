---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 19.5", "Hölder"]
tags: [measure-theory, hub]
---
![[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5]]

## Treated in
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5|Theorem §19.5: Hölder's Inequality]], in [[§19 Normed Linear Spaces and Lᵖ Spaces]]

## Its proof uses
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-3|Proposition §14.3: Basic Properties]]
- [[§14 The Lebesgue Integral for Simple Functions#^thm-14-8|Theorem §14.8: Linearity of the Integral]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-9|Proposition §14.9: Integral over Null Sets and A.E. Equal Functions]]
- [[§14 The Lebesgue Integral for Simple Functions#^prop-14-11|Proposition §14.11: Vanishing Integral for Non-Negative Functions]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|Proposition §19.2: The Essential Supremum is Achieved A.E.]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|Lemma §19.4: Young's Inequality]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-7|Definition §19.7: Conjugate Exponents]]

## Used in (Measure Theory)
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Corollary §19.6: Lᵖ Inclusion for Finite Measure Spaces]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-7|Proposition §19.7: Interpolation of Lᵖ Norms]]
- [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-9|Theorem §19.9: Minkowski's Inequality]]

## Used in (Functional Analysis)
- [[§11 Means and Young's Inequality#^prop-11-1|Proposition §11.1: Cauchy–Schwarz in ℝⁿ]]
- [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-1|Theorem §14.1: Hölder's Inequality for Functions]]
- [[§14 The Function Spaces Lᵖ(Ω)#^rem-14-2|Remark: What “Integrable” Means Here]]

## Connections
- **Proof idea.** Normalize both norms to 1 and apply [[§19 Normed Linear Spaces and Lᵖ Spaces#^lem-19-4|Young's inequality]] a^θ b^(1−θ) ≤ θa + (1 − θ)b pointwise, with θ = 1/p, a = |f|ᵖ and b = |g|^p′, then integrate. For p = 1, p′ = ∞, use |g| ≤ ‖g‖∞ a.e. ([[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-2|§19.2]]).
- **Linear algebra.** p = p′ = 2 is the [[Cauchy–Schwarz inequality]] (LADR 6.14) for the L² inner product ⟨f, g⟩ = ∫fg ([[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-1|Rem. §19.1]]). Its Riemann-integral form for continuous functions is [[§19 Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].
- **Used for.** It proves [[Minkowski's Inequality]], the first step of Hölder → Minkowski → Riesz–Fischer. It also gives the [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-6|Lᵖ inclusions on finite-measure sets]] (§19.6) and [[§19 Normed Linear Spaces and Lᵖ Spaces#^prop-19-7|interpolation of Lᵖ norms]] (§19.7).
- **Sharpness.** For p = 1, p′ = ∞ the converse holds: if fg is integrable for every integrable f, then g ∈ L∞. HW8 P5(b) proves this with a divergent-series counterexample ([[Measure Theory Problem-Solving Techniques#^rem-19-22|Technique 18]]).
