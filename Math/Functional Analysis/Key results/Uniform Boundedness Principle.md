---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 42.5", "uniform boundedness", "pointwise bounded implies uniformly bounded", "Lax §10.1, Thms 2–3"]
tags: [functional-analysis, hub]
---
![[§42 Uniform Boundedness and Approximation#^thm-42-6]]

## Treated in
- [[§42 Uniform Boundedness and Approximation#^thm-42-6|Theorem §42.6: Uniform Boundedness Principle]], in [[§42 Uniform Boundedness and Approximation]]

## Its proof uses
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|Theorem §41.3: Equivalent Norm Theorem]]

## Used in (Functional Analysis)
- [[§42 Uniform Boundedness and Approximation#^thm-42-7|Theorem §42.7: Banach–Steinhaus]]
- [[§42 Uniform Boundedness and Approximation#^thm-42-9|Theorem §42.9: Lax Equivalence Theorem]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-10|Theorem §43.10: The Norm of a Weak-ast Limit]]

## Connections
- **How.** In the lecture: $\|x\|_2 = \|x\| + \sup_\alpha \|A_\alpha x\|$ is finite by hypothesis, is a norm, and is complete; it dominates $\|\cdot\|$, so the equivalent norm theorem ([[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]) gives $\sup_\alpha\|A_\alpha x\| \le C\|x\|$ ([[Functional Analysis Problem-Solving Techniques#^rem-t27|Technique 27]]). Lax applies the [[Baire Category Theorem]] directly ([[§42 Uniform Boundedness and Approximation#^rem-42-2|Remark: Other Proofs of the Principle]]).
- **Why complete.** On $c_{00}$ with the maximum norm, $A_n x = n x_n$ is bounded at every $x$ but $\|A_n\| = n$ ([[§42 Uniform Boundedness and Approximation#^ex-42-2|Ex. §42.2]]). Only the domain must be complete; the target is any normed space.
- **Used for.** The [[Banach–Steinhaus Theorem]] and the [[Lax Equivalence Theorem]]. Applied to vectors viewed as functionals on $X'$, it shows that weakly convergent sequences are bounded ([[Criterion for Weak Convergence]], [[Functional Analysis Problem-Solving Techniques#^rem-t29|Technique 29]]); applied on $X$, that weak-$\ast$ convergent sequences are bounded when $X$ is complete ([[§43 Weak and Weak-Star Convergence#^thm-43-10|§43.10]]).
- **Same idea elsewhere.** The QFT notes quote the principle on the space of test functions to see that a pointwise limit of tempered distributions is continuous ([[§CA.2 Generalized Functions#^thm-ca-2-5|QFT Theorem §CA.2.5]]). In finite dimensions the statement is elementary: bound each $A_\alpha$ on a basis.
