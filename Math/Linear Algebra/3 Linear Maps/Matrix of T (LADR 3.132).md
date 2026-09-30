---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.132"
ladr: "3.132"
page: 113
aliases: ["LADR 3.132", "matrix of the dual map"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.132 Matrix of $T'$ is the transpose of the matrix of $T$
> Let $V,W$ be finite-dimensional, $T\in\Lin(V,W)$, with bases $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_m$ of $W$ and the dual bases $\varphi_1,\dots,\varphi_n$, $\psi_1,\dots,\psi_m$. Then
> $$
> \mathcal{M}(T')=\big(\mathcal{M}(T)\big)^t .
> $$

> [!proof]-
> Let $A=\mathcal{M}(T)$, $C=\mathcal{M}(T')$. By definition $T'(\psi_j)=\sum_rC_{r,j}\varphi_r$; evaluating at $v_k$ gives $(\psi_j\circ T)(v_k)=C_{k,j}$. On the other hand
> $$
> (\psi_j\circ T)(v_k)=\psi_j\Big(\sum_rA_{r,k}w_r\Big)=A_{j,k}.
> $$
> So $C_{k,j}=A_{j,k}$, i.e. $C=A^t$.

## Uses (in the proof)
- (definitions only)

## Connections
- Explains [[Algebraic properties of dual maps]](c) as $(AB)^t=B^tA^t$. Used in [[Column rank equals row rank (LADR 3.133)]].
- With respect to orthonormal bases the adjoint has the conjugate transpose: [[Matrix of T (LADR 7.9)]].
