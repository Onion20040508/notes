---
subject: math
type: theorem
source: "[[Axler LADR]] 5.33"
ladr: "5.33"
page: 149
aliases: ["LADR 5.33"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.33 Even-dimensional null space
> Let $\F=\R$, $V$ finite-dimensional, $T\in\Lin(V)$, and $b,c\in\R$ with $b^2<4c$. Then $\dim\nullsp(T^2+bT+cI)$ is even.

> [!proof]-
> $\nullsp(T^2+bT+cI)$ is invariant ([[Null space and range of p(T) are invariant under T]]); restricting to it, we may assume $T^2+bT+cI=0$ and must show $\dim V$ is even.
>
> $T$ has no eigenvectors: if $Tv=\lambda v$ then $0=(\lambda^2+b\lambda+c)v=\big((\lambda+\tfrac b2)^2+c-\tfrac{b^2}4\big)v$ and the scalar is positive, so $v=0$.
>
> Let $U$ be an invariant subspace of largest possible even dimension. If $U\ne V$, pick $w\notin U$ and let $W=\Span(w,Tw)$. $W$ is invariant since $T(Tw)=-bTw-cw$, and $\dim W=2$ (else $w$ is an eigenvector). $U\cap W=\{0\}$: it is invariant and properly contained in $W$ (as $w\notin U$), so if nonzero it would be a $1$-dimensional invariant subspace, i.e. an eigenvector line. By [[Dimension of a sum]], $\dim(U+W)=\dim U+2$, and $U+W$ is invariant and even-dimensional, contradicting maximality. So $U=V$.

## Uses (in the proof)
- [[Null space and range of p(T) are invariant under T]] (5.18)
- [[Dimension of a sum]] (2.43)

## Connections
- Key lemma for [[Operators on odd-dimensional vector spaces have eigenvalues]]. Complex-conjugate eigenvalue pairs of a real operator show up as such 2-dimensional invariant blocks.
