---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.19"
ladr: "5.19"
page: 143
aliases: ["LADR 5.19"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.19 Existence of eigenvalues
> Every operator on a finite-dimensional nonzero complex vector space has an eigenvalue.

> [!remark] Both hypotheses are needed
> Over $\R$: rotation by $90^\circ$ on $\R^2$ has no eigenvalue. In infinite dimensions: multiplication by $z$ on $\Poly(\C)$ has no eigenvalue.

> [!proof]-
> Let $\dim V=n>0$, $T\in\Lin(V)$, and $v\ne0$. The $n+1$ vectors $v,Tv,\dots,T^nv$ are linearly dependent, so some nonconstant polynomial $p$ satisfies $p(T)v=0$; take one of smallest degree. By [[Fundamental theorem of algebra, first version]] it has a zero $\lambda\in\C$, and by [[Each zero of a polynomial corresponds to a degree-one factor]] $p(z)=(z-\lambda)q(z)$. Then, using [[Multiplicative properties]],
> $$
> 0=p(T)v=(T-\lambda I)\big(q(T)v\big).
> $$
> Since $\deg q<\deg p$, $q(T)v\ne0$, so $q(T)v$ is an eigenvector with eigenvalue $\lambda$.

## Uses (in the proof)
- [[Fundamental theorem of algebra, first version]] (4.12)
- [[Each zero of a polynomial corresponds to a degree-one factor]] (4.6)
- [[Multiplicative properties]] (5.17)

## Connections
- Consequences: upper-triangular form over $\C$ ([[If F = C, then every operator on V has an upper-triangular matrix]]), Schur's theorem, the complex spectral theorem ([[Complex spectral theorem]]).
- Real substitute: [[Operators on odd-dimensional vector spaces have eigenvalues]] (odd dimensions).
