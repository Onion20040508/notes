---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 9.1", "sup norm complete", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§9 Completeness#^thm-9-1]]

## Treated in
- [[§9 Completeness#^thm-9-1|Theorem §9.1: C[a,b] with the Supremum Norm is a Banach Space]], in [[§9 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^def-8-5|Definition §8.5: Cauchy Sequence]]
- [[§9 Completeness#^def-9-2|Definition §9.2: Banach Space]]

## Its proof uses (other subjects)
- [[Extreme Value Theorem]] (Single Variable Analysis)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§9 Completeness#^ex-9-2|Example §9.2: C²[a,b] with a C¹ Norm]]
- [[§9 Completeness#^prop-9-6|Proposition §9.6: (C²[a,b], ∣·∣_X) is Not Complete]]
- [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-5|Proposition §14.5: Continuous Functions are Not Dense in L^∞]]
- [[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|Proposition §14.8: Lᵖ[a,b] as a Completion]]
- [[§15 Compactness and the Unit Ball#^prop-15-4|Proposition §15.4: The Constant theta = 1 Cannot Be Attained]]

## Connections
- **How.** The proof finds a candidate, then closes ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]). A sup-norm Cauchy sequence is pointwise Cauchy, so it has a pointwise limit f, by completeness of the scalars ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8]]). Keeping N independent of t upgrades this to uniform convergence, and a 3ε argument makes f continuous. These two steps re-prove [[§24 Uniform Convergence#^thm-24-1|451 §24.1]] and [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]. Unlike for ℓᵖ, showing that the candidate lies in the space is a genuine theorem ([[§9 Completeness#^rem-9-1|Remark §9]]).
- **The norm decides.** On the same set with the Lᵖ norm (1 ≤ p < ∞), C[a,b] is not complete, and its completion is Lᵖ[a,b] ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-8|§14.8]]): ramps form a Cauchy sequence converging to a step. C²[a,b] with max|f| + max|f′| is also incomplete, with completion C¹ ([[§9 Completeness#^prop-9-6|§9.6]]). With the full C² norm it is complete, by the same argument applied to f, f′, f″ ([[§9 Completeness#^ex-9-2|Ex. §9.2]]). The pattern is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]].
- **Used for.** Closed subspaces inherit completeness. {f ∈ C[0,1] : f(0) = 0} is the Banach space in which Riesz's constant 1 is not attained ([[§15 Compactness and the Unit Ball#^prop-15-4|§15.4]]). Being complete, C[0,1] is closed in L^∞[0,1]; as a proper closed subspace it is not dense there ([[§14 The Function Spaces Lᵖ(Ω)#^prop-14-5|§14.5]]), matching the place where 551's approximation chain breaks ([[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|551 Remark §19]]).
