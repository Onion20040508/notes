---
subject: math
type: theorem
source: "[[Axler LADR]] 5.22"
ladr: "5.22"
page: 144
aliases: ["LADR 5.22"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.22 Existence, uniqueness, and degree of minimal polynomial
> If $V$ is finite-dimensional and $T\in\Lin(V)$, there is a unique monic $p\in\Poly(\F)$ of smallest degree with $p(T)=0$. Moreover $\deg p\le\dim V$.

> [!remark] Crude bound versus sharp bound
> $\dim\Lin(V)=(\dim V)^2$ ([[Dim L(V, W) = (dim V)(dim W)]]) gives an annihilating polynomial of degree $\le(\dim V)^2$ for free; this result sharpens it to $\dim V$ without determinants.

> [!proof]-
> **Existence with the bound**, by induction on $\dim V$ (for all operators on all spaces over $\F$ of smaller dimension). If $\dim V=0$, take $p=1$. Otherwise pick $v\ne0$. The list $v,Tv,\dots,T^{\dim V}v$ is dependent, so by [[Linear dependence lemma]] there is a smallest $m\le\dim V$ with
> $$
> c_0v+c_1Tv+\dots+c_{m-1}T^{m-1}v+T^mv=0 .
> $$
> Let $q(z)=c_0+\dots+c_{m-1}z^{m-1}+z^m$. Then $q(T)(T^kv)=T^k(q(T)v)=0$ for all $k$, and $v,\dots,T^{m-1}v$ is independent (minimality of $m$), so $\dim\nullsp q(T)\ge m$ and $\dim\range q(T)\le\dim V-m$ ([[Fundamental theorem of linear maps]]). $\range q(T)$ is invariant ([[Null space and range of p(T) are invariant under T]]), so by induction there is a monic $s$ with $\deg s\le\dim V-m$ and $s(T|_{\range q(T)})=0$. Then $(sq)(T)v'=s(T)(q(T)v')=0$ for every $v'\in V$, and $sq$ is monic of degree $\le\dim V$.
>
> **Smallest degree and uniqueness.** *(Filled in.)* Among monic polynomials annihilating $T$ take one of smallest degree. If $p_1,p_2$ both qualify, $p_1-p_2$ has smaller degree and annihilates $T$; if it were nonzero, dividing by its leading coefficient would give a monic annihilator of smaller degree. So $p_1=p_2$.

## Uses (in the proof)
- [[Linear dependence lemma]] (2.19)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Null space and range of p(T) are invariant under T]] (5.18)

## Connections
- Defines [[Minimal polynomial]]. Divisibility: [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]]. Cayley–Hamilton ([[Cayley–Hamilton theorem (LADR 8.29)]]) gives another annihilator of degree $\dim V$.
