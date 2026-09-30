---
subject: math
type: theorem
source: "[[Axler LADR]] 5.27"
ladr: "5.27"
page: 146
aliases: ["LADR 5.27"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.27 Eigenvalues are the zeros of the minimal polynomial
> Let $V$ be finite-dimensional and $T\in\Lin(V)$ with minimal polynomial $p$.
> - (a) The zeros of $p$ are exactly the eigenvalues of $T$.
> - (b) If $\F=\C$, then $p(z)=(z-\lambda_1)\cdots(z-\lambda_m)$ where $\lambda_1,\dots,\lambda_m$ lists all eigenvalues of $T$, possibly with repetitions.

> [!proof]-
> (a) If $p(\lambda)=0$, write $p=(z-\lambda)q$ with $q$ monic ([[Each zero of a polynomial corresponds to a degree-one factor]]). Then $0=(T-\lambda I)(q(T)v)$ for all $v$. Since $\deg q<\deg p$, $q(T)\ne0$, so some $q(T)v\ne0$ is an eigenvector for $\lambda$.
>
> Conversely, if $Tv=\lambda v$ with $v\ne0$, then $T^kv=\lambda^kv$, so $0=p(T)v=p(\lambda)v$ and $p(\lambda)=0$.
>
> (b) Combine (a) with the factorization [[Fundamental theorem of algebra, second version]].

## Uses (in the proof)
- [[Each zero of a polynomial corresponds to a degree-one factor]] (4.6)
- [[Fundamental theorem of algebra, second version]] (4.13)

## Connections
- Alternative proof of [[Operator cannot have more eigenvalues than dimension of vector space]] via [[Degree m implies at most m zeros]]. Invertibility test: [[T not invertible ⟺ constant term of minimal polynomial of T is 0]].
