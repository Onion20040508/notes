---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 21.5", "L(X,Y) is a Banach space", "dual space is complete", "Lax §15.1, Thms 2–3"]
tags: [functional-analysis, hub]
---
![[§21 Boundedness and Continuity#^thm-21-5]]

## Treated in
- [[§21 Boundedness and Continuity#^thm-21-5|Theorem §21.5: ℒ(X, Y) is a Normed Linear Space]], in [[§21 Boundedness and Continuity]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§8 Normed Linear Spaces#^def-8-1|Definition §8.1: Norm; Normed Linear Space]]
- [[§8 Normed Linear Spaces#^def-8-4|Definition §8.4: Convergence]]
- [[§8 Normed Linear Spaces#^prop-8-5|Proposition §8.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§8 Normed Linear Spaces#^def-8-5|Definition §8.5: Cauchy Sequence]]
- [[§9 Completeness#^def-9-1|Definition §9.1: Complete Metric Space]]
- [[§9 Completeness#^def-9-2|Definition §9.2: Banach Space]]
- [[§21 Boundedness and Continuity#^prop-21-1|Proposition §21.1: The Operator Norm]]
- [[§21 Boundedness and Continuity#^def-21-1|Definition §21.1: Continuous Linear Map]]
- [[§21 Boundedness and Continuity#^def-21-2|Definition §21.2: Bounded Linear Map; Operator Norm]]
- [[§21 Boundedness and Continuity#^def-21-3|Definition §21.3: The Space ℒ(X, Y)]]

## Used in (Functional Analysis)
- [[§22 Dual Spaces#^cor-22-1|Corollary §22.1: The Dual is Always a Banach Space]]

## Connections
- **How.** The proof follows the pattern of [[Continuous Functions with the Sup Norm Form a Banach Space]]. Evaluating a Cauchy sequence T_n at each x gives a Cauchy sequence in Y, which converges because Y is complete. The limit T is linear, and the bound ‖T_n x − T_k x‖ ≤ ε‖x‖ passes to the limit uniformly in x. The point of the [[§21 Boundedness and Continuity#^rem-21-4|Remark §21]] on ε is that N does not depend on x.
- **Only the target matters.** X need not be complete. Lax assumes both spaces are Banach, but his proof uses only that U is complete.
- **Special case.** With Y = 𝔽, the dual X′ is always a Banach space ([[§22 Dual Spaces#^cor-22-1|§22.1]]), even when X is not complete.
- **Finite dimensions.** Every linear map there is bounded ([[§21 Boundedness and Continuity#^prop-21-4|§21.4]]), and LADR's norm of a linear map ([[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]) is the same operator norm.
