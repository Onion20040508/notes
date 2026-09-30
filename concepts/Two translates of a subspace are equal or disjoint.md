---
subject: math
type: theorem
source: "[[Axler LADR]] 3.101"
ladr: "3.101"
page: 100
aliases: ["LADR 3.101"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.101 Two translates of a subspace are equal or disjoint
> Let $U$ be a subspace of $V$ and $v,w\in V$. Then
> $$
> v-w\in U\iff v+U=w+U\iff (v+U)\cap(w+U)\neq\varnothing .
> $$

> [!remark] Consequence
> Two translates of a subspace are equal or disjoint, so the translates partition $V$; "$v\sim w\iff v-w\in U$" is the corresponding equivalence relation.

> [!proof]-
> If $v-w\in U$ and $u\in U$, then $v+u=w+\big((v-w)+u\big)\in w+U$; so $v+U\subseteq w+U$, and symmetrically, hence equality. Equality trivially gives a nonempty intersection. If $v+u_1=w+u_2$ with $u_1,u_2\in U$, then $v-w=u_2-u_1\in U$.

## Uses (in the proof)
- (definitions only)

## Connections
- The key to well-definedness in [[Quotient space is a vector space]] and to $\nullsp\pi=U$ in [[Dimension of quotient space]].
