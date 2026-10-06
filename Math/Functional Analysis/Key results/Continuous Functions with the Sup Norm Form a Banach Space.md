---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 11.1", "sup norm complete", "C[a,b] is a Banach space", "Lax §5.1, examples"]
tags: [functional-analysis, hub]
---
![[§12 Completeness#^thm-12-1]]

## Treated in
- [[§11 Completeness#^thm-11-1|Theorem §11.1: C[a,b] with the Supremum Norm is a Banach Space]], in [[§12 Completeness]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§11 Normed Linear Spaces#^def-11-5|Definition §11.5: Cauchy Sequence]]
- [[§12 Completeness#^def-12-2|Definition §12.2: Banach Space]]

## Its proof uses (other subjects)
- [[Extreme Value Theorem]] (Single Variable Analysis)
- [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3: Cauchy Implies Convergent]]

## Used in (Functional Analysis)
- [[§11 Completeness#^prop-11-7|Proposition §11.7: (C²[a,b], ∣·∣_X) is Not Complete]]
- [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5|Proposition §19.5: Continuous Functions are Not Dense in L^∞]]
- [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-8|Proposition §17.8: Lᵖ[a,b] as a Completion]]
- [[§20 Compactness and the Unit Ball#^prop-20-4|Proposition §20.4: The Constant theta = 1 Cannot Be Attained]]

## Connections
- **How.** The proof finds a candidate, then closes ([[Functional Analysis Problem-Solving Techniques#^rem-t5|Technique 5]]). A sup-norm Cauchy sequence is pointwise Cauchy, so it has a pointwise limit f, by completeness of the scalars ([[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]]). Keeping N independent of t upgrades this to uniform convergence, and a 3ε argument makes f continuous. These two steps re-prove [[§24 Uniform Convergence#^thm-24-1|451 §24.1]] and [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]. Unlike for ℓᵖ, showing that the candidate lies in the space is a genuine theorem ([[§12 Completeness#^rem-12-1|Remark §11]]).
- **The norm decides.** On the same set with the Lᵖ norm (1 ≤ p < ∞), C[a,b] is not complete, and its completion is Lᵖ[a,b] ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]]): ramps form a Cauchy sequence converging to a step. C²[a,b] with max|f| + max|f′| is also incomplete, with completion C¹ ([[§13 The Completion of a Normed Space#^prop-13-4|§13.4]]). With the full C² norm it is complete, by the same argument applied to f, f′, f″ ([[§13 The Completion of a Normed Space#^ex-13-1|Ex. §13.1]]). The pattern is [[Functional Analysis Problem-Solving Techniques#^rem-t9|Technique 9]].
- **Used for.** Closed subspaces inherit completeness. {f ∈ C[0,1] : f(0) = 0} is the Banach space in which Riesz's constant 1 is not attained ([[§20 Compactness and the Unit Ball#^prop-20-4|§20.4]]). Being complete, C[0,1] is closed in L^∞[0,1]; as a proper closed subspace it is not dense there ([[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5|§19.5]]), matching the place where 551's approximation chain breaks ([[§35 Lᵖ as a Banach Space#^rem-35-4|551 Remark §35]]).
