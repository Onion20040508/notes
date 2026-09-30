---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.11"
ladr: "5.11"
page: 136
aliases: ["LADR 5.11"]
tags: [linear-algebra, ladr/5A]
---
> [!theorem] 5.11 Linearly independent eigenvectors
> Every list of eigenvectors of $T\in\Lin(V)$ corresponding to distinct eigenvalues is linearly independent.

> [!proof]-
> Suppose not, and let $m$ be the smallest length of a linearly dependent list $v_1,\dots,v_m$ of eigenvectors with distinct eigenvalues $\lambda_1,\dots,\lambda_m$ ($m\ge2$, since eigenvectors are nonzero). Then $a_1v_1+\dots+a_mv_m=0$ with all $a_k\ne0$ (by minimality). Apply $T-\lambda_mI$:
> $$
> a_1(\lambda_1-\lambda_m)v_1+\dots+a_{m-1}(\lambda_{m-1}-\lambda_m)v_{m-1}=0 ,
> $$
> with all coefficients nonzero. This is a shorter dependent list, a contradiction.

## Uses (in the proof)
- (definitions only)

## Connections
- Gives [[Operator cannot have more eigenvalues than dimension of vector space]], and that eigenspaces form a direct sum ([[Sum of eigenspaces is a direct sum]]).
- Physics: states with different energies are independent (and orthogonal for self-adjoint $H$, [[Eigenvalues of self-adjoint operators]]).
