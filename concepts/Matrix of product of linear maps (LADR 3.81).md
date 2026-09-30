---
subject: math
type: theorem
source: "[[Axler LADR]] 3.81"
ladr: "3.81"
page: 91
aliases: ["LADR 3.81"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.81 Matrix of product of linear maps
> Let $T\in\Lin(U,V)$, $S\in\Lin(V,W)$ with bases $u_1,\dots,u_m$ of $U$, $v_1,\dots,v_n$ of $V$, $w_1,\dots,w_p$ of $W$. Then
> $$
> \mathcal{M}\big(ST,(u),(w)\big)=\mathcal{M}\big(S,(v),(w)\big)\,\mathcal{M}\big(T,(u),(v)\big).
> $$

> [!remark] Reading $\mathcal{M}(I,(u),(v))$
> Its column $k$ holds the coordinates of $u_k$ in the basis $v_1,\dots,v_n$: it converts $u$-coordinates into $v$-coordinates.

> [!proof]-
> This is [[Matrix of product of linear maps (LADR 3.43)]] with the bases written out.

## Uses (in the proof)
- [[Matrix of product of linear maps (LADR 3.43)]] (3.43)

## Connections
- Used in [[Matrix of identity operator with respect to two bases]] and [[Change-of-basis formula (LADR 3.84)]].
