---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 11.1", "sup norm complete", "C[a,b] is a Banach space", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§11 Completeness#^thm-11-1]]

## Treated in
- [[§11 Completeness#^thm-11-1|Theorem §11.1: C[a,b] with the Supremum Norm is a Banach Space]], in [[§11 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-5|Definition §10.5: Cauchy Sequence]]
- [[§11 Completeness#^def-11-2|Definition §11.2: Banach Space]]

## Its proof uses (other subjects)
- [[Extreme Value Theorem]] (Single Variable Analysis)
- [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§11 Completeness#^ex-11-2|Example §11.2: C²[a,b] with a C¹ Norm]]
- [[§11 Completeness#^prop-11-7|Proposition §11.7: (C²[a,b], ∣·∣_X) is Not Complete]]
- [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-5|Proposition §17.5: Continuous Functions are Not Dense in L^∞]]
- [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|Proposition §17.8: Lᵖ[a,b] as a Completion]]
- [[§18 Compactness and the Unit Ball#^prop-18-4|Proposition §18.4: The Constant theta = 1 Cannot Be Attained]]

## Connections
- **How.** The proof finds a candidate, then closes ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]). A sup-norm Cauchy sequence is pointwise Cauchy, so it has a pointwise limit f, by completeness of the scalars ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|451 §10.8]]). Keeping N independent of t upgrades this to uniform convergence, and a 3ε argument makes f continuous. These two steps re-prove [[§24 Uniform Convergence#^thm-24-1|451 §24.1]] and [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]. Unlike for ℓᵖ, showing that the candidate lies in the space is a genuine theorem ([[§11 Completeness#^rem-11-1|Remark §11]]).
- **The norm decides.** On the same set with the Lᵖ norm (1 ≤ p < ∞), C[a,b] is not complete, and its completion is Lᵖ[a,b] ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|§17.8]]): ramps form a Cauchy sequence converging to a step. C²[a,b] with max|f| + max|f′| is also incomplete, with completion C¹ ([[§11 Completeness#^prop-11-7|§11.7]]). With the full C² norm it is complete, by the same argument applied to f, f′, f″ ([[§11 Completeness#^ex-11-2|Ex. §11.2]]). The pattern is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]].
- **Used for.** Closed subspaces inherit completeness. {f ∈ C[0,1] : f(0) = 0} is the Banach space in which Riesz's constant 1 is not attained ([[§18 Compactness and the Unit Ball#^prop-18-4|§18.4]]). Being complete, C[0,1] is closed in L^∞[0,1]; as a proper closed subspace it is not dense there ([[§17 The Function Spaces Lᵖ(Ω)#^prop-17-5|§17.5]]), matching the place where 551's approximation chain breaks ([[§19 Normed Linear Spaces and Lᵖ Spaces#^rem-19-4|551 Remark §19]]).
