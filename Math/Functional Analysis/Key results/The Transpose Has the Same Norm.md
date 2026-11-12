---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 46.4", "norm of the transpose", "Lax §15.1, Thm 5"]
tags: [functional-analysis, hub]
---
![[§46 The Transpose#^prop-46-4]]

## Treated in
- [[§46 The Transpose#^prop-46-4|Proposition §46.4: Properties of the Transpose]], in [[§46 The Transpose]]

## Its proof uses
- [[§30 Boundedness and Continuity#^prop-30-1|Proposition §30.1: The Operator Norm]]
- [[§36 Duality in Normed Spaces#^thm-36-2|Theorem §36.2: The Norm as a Maximum over the Dual]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** $\|M'\| \le \|M\|$ is one line: $|(M'\ell)(x)| = |\ell(Mx)| \le \|\ell\|\,\|M\|\,\|x\|$. The reverse writes $\|Mx\|$ as a maximum over functionals of norm $1$ ([[The Norm as a Maximum over the Dual]], a consequence of Hahn–Banach) and exchanges the two suprema. Technique: [[Functional Analysis Problem-Solving Techniques#^rem-t33|T33]].
- **What it says.** $M \mapsto M'$ is a linear isometry of $\mathcal{L}(X, Y)$ into $\mathcal{L}(Y', X')$.
- **Finite dimensions.** For a matrix with the Euclidean norms, $\|A^T\| = \|A\|$ (both are the largest singular value): [[§28 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]].
- **In Lax.** §15.1, Thm 5(i).
