---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 9.4", "completion is a Banach space", "Lax §5.1, Thm 3"]
tags: [functional-analysis, hub]
---
![[§9 Completeness#^thm-9-4]]

## Treated in
- [[§9 Completeness#^thm-9-4|Theorem §9.4: The Completion of a Normed Space is a Banach Space]], in [[§9 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^lem-8-3|Lemma §8.3: Reverse Triangle Inequality]]
- [[§8 Normed Linear Spaces#^def-8-5|Definition §8.5: Cauchy Sequence]]
- [[§9 Completeness#^def-9-1|Definition §9.1: Complete Metric Space]]
- [[§9 Completeness#^def-9-3|Definition §9.3: Equivalent Cauchy Sequences]]
- [[§9 Completeness#^def-9-4|Definition §9.4: Completion]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§9 Completeness#^prop-9-5|Proposition §9.5: Identifying a Completion]]
- [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|Proposition §14.8: Lᵖ[a,b] as a Completion]]

## Connections
- **How.** The norm of a class is lim‖x_n‖, which exists because the reverse triangle inequality makes (‖x_n‖) Cauchy in ℝ. For completeness, take a Cauchy sequence of classes and pick the diagonal y_j = x^(M_j)_(N_j) with non-decreasing indices. The argument closes with two three-term triangle inequalities, in which an auxiliary index is sent to infinity last ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]).
- **Same idea elsewhere.** The model is ℝ as equivalence classes of Cauchy sequences of rationals ([[§10 Monotone Sequences and Cauchy Sequences#^rem-10-4|451 Remark §10]]). Density is what pins the completion down. ℂ is complete and contains ℚ but is not its completion ([[§9 Completeness#^rem-9-8|Remark §9]]).
- **Used for.** In practice the completion is identified concretely. If X embeds isometrically and densely in a Banach space Z, then Z is the completion ([[§9 Completeness#^prop-9-5|§9.5]]), unique up to isometry ([[§9 Completeness#^cor-9-6|§9.6]]); the recipe is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]]. This gives (C[a,b], ‖·‖ₚ) → Lᵖ[a,b] ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]], by the [[Riesz–Fischer Theorem]] and [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]]), and C² with a C¹ norm → C¹ ([[§9 Completeness#^prop-9-7|§9.7]]). It also gives C_c → L² ([[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-2|Ex. §17.2]]) and the Sobolev spaces H^k_0 ([[§17 Cauchy–Schwarz and the Induced Norm#^ex-17-3|Ex. §17.3]]). Lax defines Lᵖ outright as a completion.
- **The norm decides.** (C[a,b], ‖·‖∞) is already complete ([[Continuous Functions with the Sup Norm Form a Banach Space]]), so it is its own completion, while the same set with the L¹ norm completes to L¹ ([[§9 Completeness#^rem-9-9|Remark §9]]).
