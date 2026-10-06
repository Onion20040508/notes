---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 30.5", "L(X,Y) is a Banach space", "dual space is complete", "Lax §15.1, Thms 2–3"]
tags: [functional-analysis, hub]
---
![[§30 Boundedness and Continuity#^thm-30-5]]

## Treated in
- [[§30 Boundedness and Continuity#^thm-30-5|Theorem §30.5: ℒ(X, Y) is a Normed Linear Space]], in [[§30 Boundedness and Continuity]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-1|Definition §1.1: Linear Space]]
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§11 Normed Linear Spaces#^def-11-1|Definition §11.1: Norm; Normed Linear Space]]
- [[§11 Normed Linear Spaces#^def-11-4|Definition §11.4: Convergence]]
- [[§11 Normed Linear Spaces#^def-11-5|Definition §11.5: Cauchy Sequence]]
- [[§11 Normed Linear Spaces#^prop-11-5|Proposition §11.5: Limits are Unique; Convergent Sequences are Cauchy]]
- [[§12 Completeness#^def-12-1|Definition §12.1: Complete Metric Space]]
- [[§12 Completeness#^def-12-2|Definition §12.2: Banach Space]]
- [[§30 Boundedness and Continuity#^def-30-1|Definition §30.1: Continuous Linear Map]]
- [[§30 Boundedness and Continuity#^prop-30-1|Proposition §30.1: The Operator Norm]]
- [[§30 Boundedness and Continuity#^def-30-2|Definition §30.2: Bounded Linear Map]]
- [[§30 Boundedness and Continuity#^def-30-3|Definition §30.3: Operator Norm]]
- [[§30 Boundedness and Continuity#^def-30-4|Definition §30.4: The Space ℒ(X, Y)]]

## Used in (Functional Analysis)
- [[§31 Dual Spaces#^cor-31-1|Corollary §31.1: The Dual is Always a Banach Space]]

## Connections
- **How.** The proof follows the pattern of [[Continuous Functions with the Sup Norm Form a Banach Space]]. Evaluating a Cauchy sequence T_n at each x gives a Cauchy sequence in Y, which converges because Y is complete. The limit T is linear, and the bound ‖T_n x − T_k x‖ ≤ ε‖x‖ passes to the limit uniformly in x. The point of the [[§30 Boundedness and Continuity#^rem-30-4|Remark §30]] on ε is that N does not depend on x.
- **Only the target matters.** X need not be complete. Lax assumes both spaces are Banach, but his proof uses only that U is complete.
- **Special case.** With Y = 𝔽, the dual X′ is always a Banach space ([[§31 Dual Spaces#^cor-31-1|§31.1]]), even when X is not complete.
- **Finite dimensions.** Every linear map there is bounded ([[§30 Boundedness and Continuity#^prop-30-4|§30.4]]), and LADR's norm of a linear map ([[§28 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]]) is the same operator norm.
