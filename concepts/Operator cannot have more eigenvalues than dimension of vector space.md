---
subject: math
type: theorem
source: "[[Axler LADR]] 5.12"
ladr: "5.12"
page: 136
aliases: ["LADR 5.12"]
tags: [linear-algebra, ladr/5A]
---
> [!theorem] 5.12 Operator cannot have more eigenvalues than dimension of vector space
> If $V$ is finite-dimensional, each operator on $V$ has at most $\dim V$ distinct eigenvalues.

> [!proof]-
> Take one eigenvector for each of $m$ distinct eigenvalues. They are linearly independent by [[Linearly independent eigenvectors]], so $m\le\dim V$ by [[Length of linearly independent list ≤ length of spanning list]].

## Uses (in the proof)
- [[Linearly independent eigenvectors]] (5.11)
- [[Length of linearly independent list ≤ length of spanning list]] (2.22)

## Connections
- Alternative proof: zeros of the minimal polynomial ([[Eigenvalues are the zeros of the minimal polynomial]], [[Existence, uniqueness, and degree of minimal polynomial]], [[Degree m implies at most m zeros]]). With exactly $\dim V$ eigenvalues, $T$ is diagonalizable ([[Enough eigenvalues implies diagonalizability]]).
