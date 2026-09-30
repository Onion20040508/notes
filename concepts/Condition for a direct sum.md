---
subject: math
type: theorem
source: "[[Axler LADR]] 1.45"
ladr: "1.45"
page: 23
aliases: ["LADR 1.45"]
tags: [linear-algebra, ladr/1C]
---
> [!theorem] 1.45 Condition for a direct sum
> Let $V_1,\dots,V_m$ be subspaces of $V$. Then $V_1+\dots+V_m$ is a direct sum if and only if the only way to write $0=v_1+\dots+v_m$ with $v_k\in V_k$ is $v_1=\dots=v_m=0$.

> [!proof]-
> ($\Rightarrow$) Uniqueness of representation applied to $0=0+\dots+0$.
>
> ($\Leftarrow$) Suppose $v=v_1+\dots+v_m=u_1+\dots+u_m$ with $v_k,u_k\in V_k$. Subtracting,
> $$
> 0=(v_1-u_1)+\dots+(v_m-u_m),\qquad v_k-u_k\in V_k,
> $$
> so every $v_k-u_k=0$ by hypothesis, i.e. the representation is unique.

## Uses (in the proof)
- (definitions only)

## Connections
- Same idea as linear independence ([[Linearly independent]]): uniqueness everywhere follows from uniqueness at $0$.
- Used in [[Direct sum of two subspaces]], [[Sum of eigenspaces is a direct sum]], [[A sum is a direct sum if and only if dimensions add up]].
