---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.33"
ladr: "2.33"
page: 42
aliases: ["LADR 2.33"]
tags: [linear-algebra, ladr/2B]
---
> [!theorem] 2.33 Every subspace of V is part of a direct sum equal to V
> Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. Then there is a subspace $W$ of $V$ with $V=U\oplus W$.

> [!remark] Not unique
> $W$ depends on the choice of extension: in $\R^2$ with $U$ the $x$-axis, every other line through $0$ is a complement. An inner product picks a canonical one, $U^\perp$ ([[Direct sum of a subspace and its orthogonal complement]]).

> [!proof]-
> $U$ is finite-dimensional ([[Finite-dimensional subspaces]]), so it has a basis $u_1,\dots,u_m$ ([[Basis of finite-dimensional vector space]]). As a linearly independent list in $V$ it extends to a basis $u_1,\dots,u_m,w_1,\dots,w_n$ of $V$ ([[Every linearly independent list extends to a basis]]). Let $W=\Span(w_1,\dots,w_n)$. By [[Direct sum of two subspaces]] it suffices to show $V=U+W$ and $U\cap W=\{0\}$.
>
> - Any $v\in V$ is $\underbrace{a_1u_1+\dots+a_mu_m}_{\in U}+\underbrace{b_1w_1+\dots+b_nw_n}_{\in W}$.
> - If $v\in U\cap W$, then $v=\sum a_ku_k=\sum b_jw_j$, so $\sum a_ku_k-\sum b_jw_j=0$ and all coefficients vanish by independence; hence $v=0$.

## Uses (in the proof)
- [[Finite-dimensional subspaces]] (2.25)
- [[Basis of finite-dimensional vector space]] (2.31)
- [[Every linearly independent list extends to a basis]] (2.32)
- [[Direct sum of two subspaces]] (1.46)

## Connections
- Dimension count: $\dim W=\dim V-\dim U$, cf. [[Dimension of quotient space]] for $V/U$.
