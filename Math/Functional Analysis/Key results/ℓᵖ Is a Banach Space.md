---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 16.5", "completeness of lp", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-5]]

## Treated in
- [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-5|Theorem §16.5: ℓ^p is a Banach Space]], in [[§16 Minkowski's Inequality and the Spaces ℓᵖ]]

## Its proof uses
- [[§10 Normed Linear Spaces#^def-10-5|Definition §10.5: Cauchy Sequence]]
- [[§10 Normed Linear Spaces#^prop-10-5|Proposition §10.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§11 Completeness#^def-11-2|Definition §11.2: Banach Space]]
- [[§12 New Normed Spaces from Old#^cor-12-4|Corollary §12.4: Finite-Dimensional Normed Spaces are Complete]]
- [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-3|Proposition §16.3: ℓ^p is a Normed Linear Space]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 §10.1: Monotone Convergence Theorem]]
- [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** The candidate comes from coordinates: each coordinate is Cauchy in 𝔽, or equivalently the truncations are Cauchy in 𝔽ᵏ, which is complete ([[§12 New Normed Spaces from Old#^cor-12-4|§12.4]]). To close, keep the Cauchy condition with the full infinite sum and N fixed, truncate to k terms, let m → ∞ term by term, and only then let k → ∞ ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]], [[Functional Analysis Problem-Solving Techniques#^rem-t6|Technique 6]]). Choosing n depending on k would fail ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^rem-16-4|Remark §16]]). Membership is bookkeeping, a = a^(N) + (a − a^(N)), unlike for [[Continuous Functions with the Sup Norm Form a Banach Space]].
- **Same idea elsewhere.** The function-space version is the [[Riesz–Fischer Theorem]] (551 §19.18, cited here as [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-3|§17.3]]). There the candidate must come from an almost-everywhere convergent subsequence. The chain is the same in both courses: Hölder ([[§15 Hölder's Inequality for Sequences#^thm-15-1|§15.1]]; [[Hölder's Inequality]] in 551), then Minkowski ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-1|§16.1]]; [[Minkowski's Inequality]]), then completeness.
- **Used for.** ℓ² is the first infinite-dimensional Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1|Ex. §21.1]]), with the standard orthonormal basis ([[§24 Orthonormal Sets and Bases#^ex-24-1|Ex. §24.1]]). Its unit ball is not compact, since the eₙ are 2^(1/p) apart ([[§18 Compactness and the Unit Ball#^ex-18-2|Ex. §18.2]]). Completeness does not pass to the subspace c₀₀ of finitely supported sequences, which is not closed ([[§12 New Normed Spaces from Old#^rem-12-3|Remark §12]]).
