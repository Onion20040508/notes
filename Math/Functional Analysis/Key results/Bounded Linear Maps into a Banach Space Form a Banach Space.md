---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 26.5", "L(X,Y) is a Banach space", "dual space is complete", "Lax §15.1, Thms 2–3"]
tags: [functional-analysis, hub]
---
![[§26 Boundedness and Continuity#^thm-26-5]]

## Treated in
- [[§26 Boundedness and Continuity#^thm-26-5|Theorem §26.5: ℒ(X, Y) is a Normed Linear Space]], in [[§26 Boundedness and Continuity]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§10 Normed Linear Spaces#^def-10-1|Definition §10.1: Norm; Normed Linear Space]]
- [[§10 Normed Linear Spaces#^def-10-4|Definition §10.4: Convergence]]
- [[§10 Normed Linear Spaces#^prop-10-5|Proposition §10.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§10 Normed Linear Spaces#^def-10-5|Definition §10.5: Cauchy Sequence]]
- [[§11 Completeness#^def-11-1|Definition §11.1: Complete Metric Space]]
- [[§11 Completeness#^def-11-2|Definition §11.2: Banach Space]]
- [[§26 Boundedness and Continuity#^prop-26-1|Proposition §26.1: The Operator Norm]]
- [[§26 Boundedness and Continuity#^def-26-1|Definition §26.1: Continuous Linear Map]]
- [[§26 Boundedness and Continuity#^def-26-2|Definition §26.2: Bounded Linear Map; Operator Norm]]
- [[§26 Boundedness and Continuity#^def-26-3|Definition §26.3: The Space ℒ(X, Y)]]

## Used in (Functional Analysis)
- [[§27 Dual Spaces#^cor-27-1|Corollary §27.1: The Dual is Always a Banach Space]]

## Connections
- **How.** The proof follows the pattern of [[Continuous Functions with the Sup Norm Form a Banach Space]]. Evaluating a Cauchy sequence T_n at each x gives a Cauchy sequence in Y, which converges because Y is complete. The limit T is linear, and the bound ‖T_n x − T_k x‖ ≤ ε‖x‖ passes to the limit uniformly in x. The point of the [[§26 Boundedness and Continuity#^rem-26-4|Remark §26]] on ε is that N does not depend on x.
- **Only the target matters.** X need not be complete. Lax assumes both spaces are Banach, but his proof uses only that U is complete.
- **Special case.** With Y = 𝔽, the dual X′ is always a Banach space ([[§27 Dual Spaces#^cor-27-1|§27.1]]), even when X is not complete.
- **Finite dimensions.** Every linear map there is bounded ([[§26 Boundedness and Continuity#^prop-26-4|§26.4]]), and LADR's norm of a linear map ([[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]) is the same operator norm.
