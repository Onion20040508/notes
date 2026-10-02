---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 13.5", "completeness of lp", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5]]

## Treated in
- [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-5|Theorem §13.5: ℓ^p is a Banach Space]], in [[§13 Minkowski's Inequality and the Spaces ℓᵖ]]

## Its proof uses
- [[§8 Normed Linear Spaces#^prop-8-5|Proposition §8.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§8 Normed Linear Spaces#^def-8-5|Definition §8.5: Cauchy Sequence]]
- [[§9 Completeness#^def-9-2|Definition §9.2: Banach Space]]
- [[§10 New Normed Spaces from Old#^cor-10-4|Corollary §10.4: Finite-Dimensional Normed Spaces are Complete]]
- [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^prop-13-3|Proposition §13.3: ℓ^p is a Normed Linear Space]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 §10.1: Monotone Convergence Theorem]]
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|Theorem §14.3: Lᵖ(Omega) and L^∞(Omega) are Banach Spaces]]
- [[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-1|Example §17.1: Hilbert Spaces]]

## Connections
- **How.** The candidate comes from coordinates: each coordinate is Cauchy in 𝔽, or equivalently the truncations are Cauchy in 𝔽ᵏ, which is complete ([[§10 New Normed Spaces from Old#^cor-10-4|§10.4]]). To close, keep the Cauchy condition with the full infinite sum and N fixed, truncate to k terms, let m → ∞ term by term, and only then let k → ∞ ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]], [[Functional Analysis Problem-Solving Techniques#^rem-t6|Technique 6]]). Choosing n depending on k would fail ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^rem-13-4|Remark §13]]). Membership is bookkeeping, a = a^(N) + (a − a^(N)), unlike for [[Continuous Functions with the Sup Norm Form a Banach Space]].
- **Same idea elsewhere.** The function-space version is the [[Riesz–Fischer Theorem]] (551 §19.18, cited here as [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-3|§14.3]]). There the candidate must come from an almost-everywhere convergent subsequence. The chain is the same in both courses: Hölder ([[§12 Hölder's Inequality for Sequences#^thm-12-1|§12.1]]; [[Hölder's Inequality]] in 551), then Minkowski ([[§13 Minkowski's Inequality and the Spaces ℓᵖ#^thm-13-1|§13.1]]; [[Minkowski's Inequality]]), then completeness.
- **Used for.** ℓ² is the first infinite-dimensional Hilbert space ([[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-1|Ex. §17.1]]), with the standard orthonormal basis ([[§20 Orthonormal Sets and Bases#^ex-20-1|Ex. §20.1]]). Its unit ball is not compact, since the eₙ are 2^(1/p) apart ([[§15 Compactness and the Unit Ball#^ex-15-2|Ex. §15.2]]). Completeness does not pass to the subspace c₀₀ of finitely supported sequences, which is not closed ([[§10 New Normed Spaces from Old#^rem-10-3|Remark §10]]).
