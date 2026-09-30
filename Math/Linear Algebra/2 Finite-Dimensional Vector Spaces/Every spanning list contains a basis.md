---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.30"
ladr: "2.30"
page: 40
aliases: ["LADR 2.30"]
tags: [linear-algebra, ladr/2B]
---
> [!theorem] 2.30 Every spanning list contains a basis
> Every spanning list in a vector space can be reduced to a basis of the vector space.

> [!proof]-
> Let $v_1,\dots,v_n$ span $V$ and start with $B=v_1,\dots,v_n$. For $k=1,\dots,n$: if $v_k\in\Span(v_1,\dots,v_{k-1})$, delete $v_k$ from $B$; otherwise keep it (for $k=1$ this means: delete $v_1$ iff $v_1=0$).
>
> Only vectors already in the span of earlier ones are discarded, so $B$ still spans $V$. No vector of $B$ lies in the span of the earlier ones in $B$, so $B$ is linearly independent by [[Linear dependence lemma]]. Hence $B$ is a basis.

## Uses (in the proof)
- [[Linear dependence lemma]] (2.19)

## Connections
- Dual statement: [[Every linearly independent list extends to a basis]]. Consequences: [[Basis of finite-dimensional vector space]], [[Spanning list of the right length is a basis]].
