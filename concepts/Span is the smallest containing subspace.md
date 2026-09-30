---
subject: math
type: theorem
source: "[[Axler LADR]] 2.6"
ladr: "2.6"
page: 29
aliases: ["LADR 2.6"]
tags: [linear-algebra, ladr/2A]
---
> [!theorem] 2.6 Span is the smallest containing subspace
> The span of a list of vectors in $V$ is the smallest subspace of $V$ containing all vectors in the list.

> [!proof]-
> $0=0v_1+\dots+0v_m$ is in the span; sums and scalar multiples of linear combinations are linear combinations:
> $$
> \textstyle\sum a_kv_k+\sum c_kv_k=\sum (a_k+c_k)v_k,\qquad \lambda\sum a_kv_k=\sum(\lambda a_k)v_k .
> $$
> So the span is a subspace by [[Conditions for a subspace]]. It contains each $v_k$ (coefficient $1$ on $v_k$, $0$ elsewhere). Any subspace containing all $v_k$ contains all their linear combinations.

## Uses (in the proof)
- [[Conditions for a subspace]] (1.34)

## Connections
- Parallel to [[Sum of subspaces is the smallest containing subspace]]: $\Span(v_1,\dots,v_m)=\Span(v_1)+\dots+\Span(v_m)$.
