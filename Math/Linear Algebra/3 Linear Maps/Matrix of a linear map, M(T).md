---
subject: math
type: definition
source: "[[Linear Algebra]] 3.31"
ladr: "3.31"
page: 69
aliases: ["LADR 3.31"]
tags: [linear-algebra, ladr/3C]
---
> [!definition] 3.31 Matrix of a linear map, M(T)
> Let $T\in\Lin(V,W)$, $v_1,\dots,v_n$ a basis of $V$ and $w_1,\dots,w_m$ a basis of $W$. The *matrix of $T$* with respect to these bases is the $m$-by-$n$ matrix $\mathcal{M}(T)$ with entries defined by
> $$
> Tv_k=A_{1,k}w_1+\dots+A_{m,k}w_m .
> $$
> When the bases need to be shown: $\mathcal{M}\big(T,(v_1,\dots,v_n),(w_1,\dots,w_m)\big)$.

> [!remark] How to remember
> Column $k$ of $\mathcal{M}(T)$ holds the coordinates of $Tv_k$ in the basis $w_1,\dots,w_m$. Write the $v$'s across the top and the $w$'s down the side.

## Connections
- Well defined and bijective in $T$ because of [[Linear map lemma]] and [[Criterion for basis]].
- Compatible with the algebra: [[Matrix of the sum of linear maps]], [[The matrix of a scalar times a linear map]], [[Matrix of product of linear maps (LADR 3.43)]]. Acts on coordinates: [[Linear maps act like matrix multiplication]].
- Depends on the bases: [[Change-of-basis formula (LADR 3.84)]]. Much of Chapters 5–8 is about choosing bases that make $\mathcal{M}(T)$ simple.
