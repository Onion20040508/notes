---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 36.2", "norm via the dual", "duality formula for the norm"]
tags: [functional-analysis, hub]
---
![[§36 Duality in Normed Spaces#^thm-36-2]]

## Treated in
- [[§36 Duality in Normed Spaces#^thm-36-2|Theorem §36.2: The Norm as a Maximum over the Dual]], in [[§36 Duality in Normed Spaces]]

## Its proof uses
- [[§36 Duality in Normed Spaces#^thm-36-1|Theorem §36.1: Hahn–Banach for Normed Spaces]]

## Used in (Functional Analysis)
- [[§36 Duality in Normed Spaces#^cor-36-3|Corollary §36.3: Bounded Functionals Separate Points]]
- [[§36 Duality in Normed Spaces#^cor-36-6|Corollary §36.6: Duality Formula for the ℓ^p Norm]]
- [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|Proposition §37.5: The Canonical Embedding X → X'']]
- [[§43 Weak and Weak-Star Convergence#^prop-43-1|Proposition §43.1: Basic Properties of Weak Limits]]
- [[§43 Weak and Weak-Star Convergence#^thm-43-4|Theorem §43.4: The Norm of a Weak Limit]]
- [[§46 The Transpose#^prop-46-4|Proposition §46.4: Properties of the Transpose]]

## Connections
- **How.** $|\ell(y)| \le \|\ell\|\|y\|$ gives $\le$. For equality define $\ell_0(c\,y_0) = c\|y_0\|$ on the line through $y_0$, a functional of norm $1$ there, and extend it by the [[Hahn–Banach Theorem for Normed Spaces]] ([[Functional Analysis Problem-Solving Techniques#^rem-t22|Technique 22]]).
- **Duality.** The norm of a functional is a supremum over the unit ball of $X$, and it need not be attained ([[§36 Duality in Normed Spaces#^ex-36-1|Ex. §36.1]]). The norm of a vector is a supremum over the unit ball of $X'$, and it is always attained ([[§36 Duality in Normed Spaces#^rem-36-2|Remark: Duality]]).
- **Used for.** Bounded functionals separate points ([[§36 Duality in Normed Spaces#^cor-36-3|§36.3]]), so weak limits are unique ([[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]]). The embedding $X \to X''$ is an isometry ([[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]). $\|x_0\| \le \liminf\|x_n\|$ for a weak limit ([[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]). For $\ell^p$ it becomes the duality formula, with an explicit maximizer ([[§36 Duality in Normed Spaces#^cor-36-6|§36.6]], [[§36 Duality in Normed Spaces#^prop-36-7|§36.7]]).
- **With an inner product.** In a Hilbert space the maximizing functional is $(\cdot, y/\|y\|)$, by the equality case of [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]]; no extension theorem is needed. The distance version of the formula is [[Distance to a Subspace via Functionals]].
