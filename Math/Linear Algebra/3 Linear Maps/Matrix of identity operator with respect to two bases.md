---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.82"
ladr: "3.82"
page: 92
aliases: ["LADR 3.82"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.82 Matrix of identity operator with respect to two bases
> If $u_1,\dots,u_n$ and $v_1,\dots,v_n$ are bases of $V$, then $\mathcal{M}(I,(u),(v))$ and $\mathcal{M}(I,(v),(u))$ are invertible and inverse to each other.

> [!proof]-
> Apply [[Matrix of product of linear maps (LADR 3.81)]] with $S=T=I$ and $w=u$:
> $$
> I=\mathcal{M}(I,(v),(u))\,\mathcal{M}(I,(u),(v)).
> $$
> Swapping the roles of $u$ and $v$ gives the product in the other order.

## Uses (in the proof)
- [[Matrix of product of linear maps (LADR 3.81)]] (3.81)

## Connections
- The change-of-basis matrix $C$ in [[Change-of-basis formula (LADR 3.84)]].
