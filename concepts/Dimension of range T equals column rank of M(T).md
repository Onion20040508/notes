---
subject: math
type: theorem
source: "[[Axler LADR]] 3.78"
ladr: "3.78"
page: 90
aliases: ["LADR 3.78"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.78 Dimension of range T equals column rank of M(T)
> If $V,W$ are finite-dimensional and $T\in\Lin(V,W)$, then $\dim\range T$ equals the column rank of $\mathcal{M}(T)$.

> [!proof]-
> $w\mapsto\mathcal{M}(w)$ is an isomorphism $W\to\F^{m,1}$. *(Filled in.)* $\range T=\Span(Tv_1,\dots,Tv_n)$, since $T(\sum c_kv_k)=\sum c_kTv_k$. The isomorphism restricts to an isomorphism from $\range T$ onto $\Span(\mathcal{M}(Tv_1),\dots,\mathcal{M}(Tv_n))$, and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$. Isomorphic spaces have equal dimension ([[Dimension shows whether vector spaces are isomorphic]]).

## Uses (in the proof)
- [[Dimension shows whether vector spaces are isomorphic]] (3.70)

## Connections
- With [[Fundamental theorem of linear maps]]: $\dim V=\dim\nullsp T+\operatorname{rank}\mathcal{M}(T)$, the matrix rank–nullity theorem.
