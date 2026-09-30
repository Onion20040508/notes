---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.35"
ladr: "3.35"
page: 71
aliases: ["LADR 3.35"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.35 Matrix of the sum of linear maps
> If $S,T\in\Lin(V,W)$ (same bases throughout), then $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$.

> [!proof]-
> *(Filled in.)* Let $\mathcal{M}(S)=A$, $\mathcal{M}(T)=C$. Then
> $$
> (S+T)v_k=Sv_k+Tv_k=\sum_j A_{j,k}w_j+\sum_jC_{j,k}w_j=\sum_j(A_{j,k}+C_{j,k})w_j,
> $$
> so column $k$ of $\mathcal{M}(S+T)$ is column $k$ of $A+C$.

## Uses (in the proof)
- (definitions only)

## Connections
- With [[The matrix of a scalar times a linear map]]: $\mathcal{M}$ is linear, one half of [[Dim L(V, W) = (dim V)(dim W)]].
