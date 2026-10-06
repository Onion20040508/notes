---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 11.4", "completion is a Banach space", "Lax §5.1, Thm 3"]
tags: [functional-analysis, hub]
---
![[§11 Completeness#^thm-11-4]]

## Treated in
- [[§11 Completeness#^thm-11-4|Theorem §11.4: The Completion of a Normed Space is a Banach Space]], in [[§11 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]
- [[§10 Normed Linear Spaces#^lem-10-3|Lemma §10.3: Reverse Triangle Inequality]]
- [[§10 Normed Linear Spaces#^def-10-5|Definition §10.5: Cauchy Sequence]]
- [[§11 Completeness#^def-11-1|Definition §11.1: Complete Metric Space]]
- [[§11 Completeness#^def-11-3|Definition §11.3: Equivalent Cauchy Sequences]]
- [[§11 Completeness#^def-11-4|Definition §11.4: Completion]]

## Its proof uses (other subjects)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§11 Completeness#^prop-11-5|Proposition §11.5: Identifying a Completion]]
- [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|Proposition §17.8: Lᵖ[a,b] as a Completion]]

## Connections
- **How.** The norm of a class is lim‖x_n‖, which exists because the reverse triangle inequality makes (‖x_n‖) Cauchy in ℝ. For completeness, take a Cauchy sequence of classes and pick the diagonal y_j = x^(M_j)_(N_j) with non-decreasing indices. The argument closes with two three-term triangle inequalities, in which an auxiliary index is sent to infinity last ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]).
- **Same idea elsewhere.** The model is ℝ as equivalence classes of Cauchy sequences of rationals ([[§10a Cauchy Sequences#^rem-10-4|451 Remark §10a]], carried out in [[§6★ ℝ from Cauchy Sequences of Rationals|451 §6★]], where ε must stay rational because ℝ is not yet available). Density is what pins the completion down. ℂ is complete and contains ℚ but is not its completion ([[§11 Completeness#^rem-11-8|Remark §11]]).
- **Used for.** In practice the completion is identified concretely. If X embeds isometrically and densely in a Banach space Z, then Z is the completion ([[§11 Completeness#^prop-11-5|§11.5]]), unique up to isometry ([[§11 Completeness#^cor-11-6|§11.6]]); the recipe is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]]. This gives (C[a,b], ‖·‖ₚ) → Lᵖ[a,b] ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|§17.8]], by the [[Riesz–Fischer Theorem]] and [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]]), and C² with a C¹ norm → C¹ ([[§11 Completeness#^prop-11-7|§11.7]]). It also gives C_c → L² ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-2|Ex. §21.2]]) and the Sobolev spaces H^k_0 ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-3|Ex. §21.3]]). Lax defines Lᵖ outright as a completion.
- **The norm decides.** (C[a,b], ‖·‖∞) is already complete ([[Continuous Functions with the Sup Norm Form a Banach Space]]), so it is its own completion, while the same set with the L¹ norm completes to L¹ ([[§11 Completeness#^rem-11-9|Remark §11]]).
