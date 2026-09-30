---
subject: math
type: theorem
source: "[[Axler LADR]] 3.72"
ladr: "3.72"
page: 87
aliases: ["LADR 3.72"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.72 Dim L(V, W) = (dim V)(dim W)
> If $V,W$ are finite-dimensional, then $\Lin(V,W)$ is finite-dimensional and $\dim\Lin(V,W)=(\dim V)(\dim W)$.

> [!proof]-
> *(Filled in: Axler 3.71.)* Fix bases, $\dim V=n$, $\dim W=m$. The map $\mathcal{M}:\Lin(V,W)\to\F^{m,n}$ is linear by [[Matrix of the sum of linear maps]] and [[The matrix of a scalar times a linear map]]. It is injective: $\mathcal{M}(T)=0$ means $Tv_k=0$ for all $k$, so $T=0$. It is surjective: given $A$, [[Linear map lemma]] gives $T$ with $Tv_k=\sum_jA_{j,k}w_j$. So $\Lin(V,W)\cong\F^{m,n}$, and $\dim\Lin(V,W)=mn$ by [[Dimension shows whether vector spaces are isomorphic]] and [[Dim Fᵐ’ⁿ = mn]].

## Uses (in the proof)
- [[Matrix of the sum of linear maps]] (3.35)
- [[The matrix of a scalar times a linear map]] (3.38)
- [[Linear map lemma]] (3.4)
- [[Dimension shows whether vector spaces are isomorphic]] (3.70)
- [[Dim Fᵐ’ⁿ = mn]] (3.40)

## Connections
- Special case $W=\F$: $\dim V'=\dim V$ ([[Dim V′ = dim V]]).
