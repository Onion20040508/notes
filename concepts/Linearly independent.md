---
subject: math
type: definition
source: "[[Axler LADR]] 2.15"
ladr: "2.15"
page: 32
aliases: ["LADR 2.15"]
tags: [linear-algebra, ladr/2A]
---
> [!definition] 2.15 Linearly independent
> A list $v_1,\dots,v_m$ in $V$ is *linearly independent* if the only choice of $a_1,\dots,a_m\in\F$ with $a_1v_1+\dots+a_mv_m=0$ is $a_1=\dots=a_m=0$. The empty list is declared linearly independent.

> [!remark] Equivalent form
> $v_1,\dots,v_m$ is linearly independent iff every vector of $\Span(v_1,\dots,v_m)$ has exactly one representation as a linear combination of the list (subtract two representations).

## Connections
- Negation: [[Linearly dependent]]. Same 'uniqueness at $0$' pattern as [[Condition for a direct sum]]. Half of [[Basis]].
