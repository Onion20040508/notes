---
subject: math
type: theorem
source: "[[Axler LADR]] 3.43"
ladr: "3.43"
page: 74
aliases: ["LADR 3.43"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.43 Matrix of product of linear maps
> If $T\in\Lin(U,V)$ and $S\in\Lin(V,W)$, then $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$ (bases $u_1,\dots,u_p$; $v_1,\dots,v_n$; $w_1,\dots,w_m$).

> [!proof]-
> Let $\mathcal{M}(S)=A$, $\mathcal{M}(T)=B$. For each $k$,
> $$
> (ST)u_k=S\Big(\sum_{r}B_{r,k}v_r\Big)=\sum_rB_{r,k}Sv_r=\sum_rB_{r,k}\sum_jA_{j,r}w_j=\sum_j\Big(\sum_rA_{j,r}B_{r,k}\Big)w_j .
> $$
> So the $(j,k)$ entry of $\mathcal{M}(ST)$ is $\sum_rA_{j,r}B_{r,k}=(AB)_{j,k}$ ([[Matrix multiplication]]).

## Uses (in the proof)
- [[Matrix multiplication]] (3.41)

## Connections
- Restated with explicit bases in [[Matrix of product of linear maps (LADR 3.81)]]; used for change of basis [[Change-of-basis formula (LADR 3.84)]] and [[Matrix of inverse equals inverse of matrix]].
