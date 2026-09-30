---
subject: math
type: theorem
source: "[[Axler LADR]] 3.127"
ladr: "3.127"
page: 111
aliases: ["LADR 3.127"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.127 Condition for the annihilator to equal {0} or the whole space
> If $V$ is finite-dimensional and $U$ is a subspace, then
> - (a) $U^0=\{0\}\iff U=V$;
> - (b) $U^0=V'\iff U=\{0\}$.

> [!remark] How to use it
> (a) shows a subspace is everything by showing no nonzero functional kills it; (b) shows it is trivial by showing every functional kills it.

> [!proof]-
> (a) $U^0=\{0\}\iff\dim U^0=0\iff\dim U=\dim V\iff U=V$, by [[Dimension of the annihilator]] and [[Subspace of full dimension equals the whole space]].
>
> (b) $U^0=V'\iff\dim U^0=\dim V'$ (one direction by [[Subspace of full dimension equals the whole space]]) $\iff\dim U^0=\dim V$ ([[Dim V′ = dim V]]) $\iff\dim U=0$ ([[Dimension of the annihilator]]) $\iff U=\{0\}$.

## Uses (in the proof)
- [[Dimension of the annihilator]] (3.125)
- [[Subspace of full dimension equals the whole space]] (2.39)
- [[Dim V′ = dim V]] (3.111)

## Connections
- Gives the surjective/injective dualities in [[The null space of T]] and [[The range of T]].
