---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.76"
ladr: "3.76"
page: 89
aliases: ["LADR 3.76"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.76 Linear maps act like matrix multiplication
> Let $T\in\Lin(V,W)$, $v\in V$, with bases $v_1,\dots,v_n$ of $V$ and $w_1,\dots,w_m$ of $W$. Then
> $$
> \mathcal{M}(Tv)=\mathcal{M}(T)\,\mathcal{M}(v).
> $$

> [!remark] Every map is a matrix, after relabeling
> Identifying $v$ with $\mathcal{M}(v)$, $T$ becomes multiplication by $\mathcal{M}(T)$ on $\F^{n,1}$. The matrix depends on the bases, and choosing bases to simplify it is a central theme later.

> [!proof]-
> Write $v=b_1v_1+\dots+b_nv_n$, so $Tv=\sum b_kTv_k$. Since $\mathcal{M}$ is linear on $W$ and $\mathcal{M}(Tv_k)$ is column $k$ of $\mathcal{M}(T)$,
> $$
> \mathcal{M}(Tv)=\sum_kb_k\,\mathcal{M}(T)_{\cdot,k}=\mathcal{M}(T)\mathcal{M}(v)
> $$
> by [[Linear combination of columns]].

## Uses (in the proof)
- [[Linear combination of columns]] (3.50)

## Connections
- Used in [[Dimension of range T equals column rank of M(T)]] and in the change-of-basis story [[Change-of-basis formula (LADR 3.84)]].
