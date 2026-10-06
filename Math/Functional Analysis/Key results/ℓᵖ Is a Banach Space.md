---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 16.5", "completeness of lp", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5]]

## Treated in
- [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|Theorem §18.5: ℓ^p is a Banach Space]], in [[§18 Minkowski's Inequality and the Spaces ℓᵖ]]

## Its proof uses
- [[§11 Normed Linear Spaces#^def-11-5|Definition §11.5: Cauchy Sequence]]
- [[§11 Normed Linear Spaces#^prop-11-5|Proposition §11.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§12 Completeness#^def-12-2|Definition §12.2: Banach Space]]
- [[§14 New Normed Spaces from Old#^cor-14-4|Corollary §14.4: Finite-Dimensional Normed Spaces are Complete]]
- [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-3|Proposition §18.3: ℓ^p is a Normed Linear Space]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 §10.1: Monotone Convergence Theorem]]
- [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** The candidate comes from coordinates: each coordinate is Cauchy in 𝔽, or equivalently the truncations are Cauchy in 𝔽ᵏ, which is complete ([[§14 New Normed Spaces from Old#^cor-14-4|§14.4]]). To close, keep the Cauchy condition with the full infinite sum and N fixed, truncate to k terms, let m → ∞ term by term, and only then let k → ∞ ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]], [[Functional Analysis Problem-Solving Techniques#^rem-t6|Technique 6]]). Choosing n depending on k would fail ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^rem-18-4|Remark §18]]). Membership is bookkeeping, a = a^(N) + (a − a^(N)), unlike for [[Continuous Functions with the Sup Norm Form a Banach Space]].
- **Same idea elsewhere.** The function-space version is the [[Riesz–Fischer Theorem]] (551 §19.18, cited here as [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|§19.3]]). There the candidate must come from an almost-everywhere convergent subsequence. The chain is the same in both courses: Hölder ([[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]]; [[Hölder's Inequality]] in 551), then Minkowski ([[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|§18.1]]; [[Minkowski's Inequality]]), then completeness.
- **Used for.** ℓ² is the first infinite-dimensional Hilbert space ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1|Ex. §23.1]]), with the standard orthonormal basis ([[§27 Orthonormal Sets and Bases#^ex-27-1|Ex. §27.1]]). Its unit ball is not compact, since the eₙ are 2^(1/p) apart ([[§20 Compactness and the Unit Ball#^ex-20-2|Ex. §20.2]]). Completeness does not pass to the subspace c₀₀ of finitely supported sequences, which is not closed ([[§14 New Normed Spaces from Old#^rem-14-3|Remark §14]]).
