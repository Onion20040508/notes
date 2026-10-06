---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 11.4", "completion is a Banach space", "Lax §5.1, Thm 3"]
tags: [functional-analysis, hub]
---
![[§13 The Completion of a Normed Space#^thm-13-1]]

## Treated in
- [[§13 The Completion of a Normed Space#^thm-13-1|Theorem §13.1: The Completion of a Normed Space is a Banach Space]], in [[§12 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§11 Normed Linear Spaces#^lem-11-3|Lemma §11.3: Reverse Triangle Inequality]]
- [[§11 Normed Linear Spaces#^def-11-5|Definition §11.5: Cauchy Sequence]]
- [[§12 Completeness#^def-12-1|Definition §12.1: Complete Metric Space]]
- [[§12 Completeness#^def-12-3|Definition §12.3: Equivalent Cauchy Sequences]]
- [[§12 Completeness#^def-12-4|Definition §12.4: Completion]]

## Its proof uses (other subjects)
- [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§13 The Completion of a Normed Space#^prop-13-2|Proposition §13.2: Identifying a Completion]]
- [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|Proposition §17.8: Lᵖ[a,b] as a Completion]]

## Connections
- **How.** The norm of a class is lim‖x_n‖, which exists because the reverse triangle inequality makes (‖x_n‖) Cauchy in ℝ. For completeness, take a Cauchy sequence of classes and pick the diagonal y_j = x^(M_j)_(N_j) with non-decreasing indices. The argument closes with two three-term triangle inequalities, in which an auxiliary index is sent to infinity last ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]).
- **Same idea elsewhere.** The model is ℝ as equivalence classes of Cauchy sequences of rationals ([[§10a Cauchy Sequences#^rem-10a-4|451 Remark §10a]], carried out in [[§6★ ℝ from Cauchy Sequences of Rationals|451 §6★]], where ε must stay rational because ℝ is not yet available). Density is what pins the completion down. ℂ is complete and contains ℚ but is not its completion ([[§13 The Completion of a Normed Space#^rem-13-5|Remark §11]]).
- **Used for.** In practice the completion is identified concretely. If X embeds isometrically and densely in a Banach space Z, then Z is the completion ([[§13 The Completion of a Normed Space#^prop-13-2|§13.2]]), unique up to isometry ([[§13 The Completion of a Normed Space#^cor-13-3|§13.3]]); the recipe is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]]. This gives (C[a,b], ‖·‖ₚ) → Lᵖ[a,b] ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]], by the [[Riesz–Fischer Theorem]] and [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]]), and C² with a C¹ norm → C¹ ([[§13 The Completion of a Normed Space#^prop-13-4|§13.4]]). It also gives C_c → L² ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-2|Ex. §23.2]]) and the Sobolev spaces H^k_0 ([[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-3|Ex. §23.3]]). Lax defines Lᵖ outright as a completion.
- **The norm decides.** (C[a,b], ‖·‖∞) is already complete ([[Continuous Functions with the Sup Norm Form a Banach Space]]), so it is its own completion, while the same set with the L¹ norm completes to L¹ ([[§13 The Completion of a Normed Space#^rem-13-6|Remark §11]]).
