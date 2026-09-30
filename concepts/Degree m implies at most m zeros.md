---
subject: math
type: theorem
source: "[[Axler LADR]] 4.8"
ladr: "4.8"
page: 122
aliases: ["LADR 4.8"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.8 Degree m implies at most m zeros
> A polynomial $p\in\Poly(\F)$ of degree $m\ge1$ has at most $m$ zeros in $\F$.

> [!remark] Coefficients are unique
> If a polynomial function had two coefficient lists, their difference would be a nonzero-coefficient polynomial with infinitely many zeros (all of $\F$), contradicting this result. So coefficients and degree are well defined (used in [[Polynomial, P(F)]], [[Degree of a polynomial, deg p]]), and $1,z,\dots,z^m$ is linearly independent.

> [!proof]-
> Induction on $m$. For $m=1$, $a_0+a_1z$ with $a_1\ne0$ has exactly one zero $-a_0/a_1$. For $m>1$: if $p$ has no zero we are done; otherwise let $p(\lambda)=0$ and write $p=(z-\lambda)q$ with $\deg q=m-1$ ([[Each zero of a polynomial corresponds to a degree-one factor]]). The zeros of $p$ are $\lambda$ together with the zeros of $q$, of which there are at most $m-1$.

## Uses (in the proof)
- [[Each zero of a polynomial corresponds to a degree-one factor]] (4.6)

## Connections
- Alternative bound on the number of eigenvalues: via [[Eigenvalues are the zeros of the minimal polynomial]] and [[Existence, uniqueness, and degree of minimal polynomial]] (compare [[Operator cannot have more eigenvalues than dimension of vector space]]).
