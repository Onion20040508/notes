---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 34.5", "Hölder"]
tags: [measure-theory, hub]
---
![[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5]]

## Treated in
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|Theorem §34.5: Hölder's Inequality]], in [[§34 Normed Linear Spaces and Lᵖ Spaces]]

## Its proof uses
- [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|Proposition §20.3: Basic Properties]]
- [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|Theorem §21.1: Linearity of the Integral]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|Proposition §21.2: Integral over Null Sets and A.E. Equal Functions]]
- [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4: Vanishing Integral for Non-Negative Functions]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2: The Essential Supremum is Achieved A.E.]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|Lemma §34.4: Young's Inequality]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Definition §34.10: Conjugate Exponents]]

## Used in (Measure Theory)
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|Corollary §34.6: Lᵖ Inclusion for Finite Measure Spaces]]
- [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-7|Proposition §34.7: Interpolation of Lᵖ Norms]]
- [[§35 Lᵖ as a Banach Space#^thm-35-2|Theorem §35.2: Minkowski's Inequality]]

## Used in (Functional Analysis)
- [[§16 Means and Young's Inequality#^prop-16-1|Proposition §16.1: Cauchy–Schwarz in ℝⁿ]]
- [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Theorem §19.1: Hölder's Inequality for Functions]]
- [[§19 The Function Spaces Lᵖ(Ω)#^rem-19-2|Remark: What “Integrable” Means Here]]

## Connections
- **Proof idea.** Normalize both norms to 1 and apply [[§34 Normed Linear Spaces and Lᵖ Spaces#^lem-34-4|Young's inequality]] a^θ b^(1−θ) ≤ θa + (1 − θ)b pointwise, with θ = 1/p, a = |f|ᵖ and b = |g|^p′, then integrate. For p = 1, p′ = ∞, use |g| ≤ ‖g‖∞ a.e. ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]]).
- **Linear algebra.** p = p′ = 2 is the [[Cauchy–Schwarz inequality]] (LADR 6.14) for the L² inner product ⟨f, g⟩ = ∫fg ([[§34 Normed Linear Spaces and Lᵖ Spaces#^rem-34-1|Rem. §19.1]]). Its Riemann-integral form for continuous functions is [[§20 Inner Products and Norms#^ladr-6-16|LADR 6.16(b)]].
- **Used for.** It proves [[Minkowski's Inequality]], the first step of Hölder → Minkowski → Riesz–Fischer. It also gives the [[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|Lᵖ inclusions on finite-measure sets]] (§34.6) and [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-7|interpolation of Lᵖ norms]] (§34.7).
- **Sharpness.** For p = 1, p′ = ∞ the converse holds: if fg is integrable for every integrable f, then g ∈ L∞. HW8 P5(b) proves this with a divergent-series counterexample ([[Measure Theory Problem-Solving Techniques#^rem-19-22|Technique 18]]).
