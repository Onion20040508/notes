---
subject: math
type: theorem
source: "[[Axler LADR]] 1.46"
ladr: "1.46"
page: 23
aliases: ["LADR 1.46"]
tags: [linear-algebra, ladr/1C]
---
> [!theorem] 1.46 Direct sum of two subspaces
> If $U,W$ are subspaces of $V$, then $U+W$ is a direct sum $\iff U\cap W=\{0\}$.

> [!remark] Only for two subspaces
> Pairwise trivial intersections do not make a sum of three subspaces direct. In $\R^2$ take the lines spanned by $(1,0)$, $(0,1)$, $(1,1)$: all pairwise intersections are $\{0\}$, yet $(1,0)+(0,1)+(-1,-1)=0$.

> [!proof]-
> ($\Rightarrow$) If $v\in U\cap W$, then $0=v+(-v)$ with $v\in U$, $-v\in W$. Uniqueness of the representation of $0$ gives $v=0$.
>
> ($\Leftarrow$) By [[Condition for a direct sum]] it suffices to show: $0=u+w$ with $u\in U$, $w\in W$ forces $u=w=0$. From $u=-w\in W$ we get $u\in U\cap W=\{0\}$, so $u=0$ and then $w=0$.

## Uses (in the proof)
- [[Condition for a direct sum]] (1.45)

## Connections
- Used to build complements in [[Every subspace of V is part of a direct sum equal to V]]. Dimension version: [[A sum is a direct sum if and only if dimensions add up]].
