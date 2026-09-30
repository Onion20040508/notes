---
subject: math
type: theorem
source: "[[Axler LADR]] 5.34"
ladr: "5.34"
page: 150
aliases: ["LADR 5.34"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.34 Operators on odd-dimensional vector spaces have eigenvalues
> Every operator on an odd-dimensional vector space has an eigenvalue.

> [!remark] Sharp
> In every even dimension there are real operators without eigenvalues (block-diagonal rotations).

> [!proof]-
> Over $\C$ this is [[Existence of eigenvalues]], so let $\F=\R$, $n=\dim V$ odd, and induct on $n$ in steps of $2$ ($n=1$ is trivial). Let $p$ be the minimal polynomial of $T$. If $x-\lambda$ divides $p$ for some real $\lambda$, then $\lambda$ is an eigenvalue ([[Eigenvalues are the zeros of the minimal polynomial]](a)). Otherwise, by [[Factorization of a polynomial over R]], $p(x)=q(x)(x^2+bx+c)$ with $b^2<4c$ and $q$ monic. Then $q(T)$ vanishes on $\range(T^2+bT+cI)$; since $\deg q<\deg p$, this range is not all of $V$.
>
> By [[Fundamental theorem of linear maps]], $\dim V=\dim\nullsp(T^2+bT+cI)+\dim\range(T^2+bT+cI)$. The null space has even dimension ([[Even-dimensional null space]]), so the range has odd dimension $<n$. It is invariant ([[Null space and range of p(T) are invariant under T]]), so by induction $T$ restricted to it has an eigenvalue, which is an eigenvalue of $T$.

## Uses (in the proof)
- [[Existence of eigenvalues]] (5.19)
- [[Eigenvalues are the zeros of the minimal polynomial]] (5.27)
- [[Factorization of a polynomial over R]] (4.16)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Even-dimensional null space]] (5.33)
- [[Null space and range of p(T) are invariant under T]] (5.18)

## Connections
- Physics: a rotation of $\R^3$ has a real eigenvalue by this result, necessarily $\pm1$ (norm-preserving; cf. [[Eigenvalues of unitary operators have absolute value 1]]). For a proper rotation ($\det=1$), since the eigenvalues have modulus $1$, nonreal ones come in conjugate pairs with product $1$, and their product is $1$, the eigenvalue $1$ must occur: the rotation axis.
