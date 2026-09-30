---
subject: math
type: theorem
source: "[[Axler LADR]] 3.103"
ladr: "3.103"
page: 101
aliases: ["LADR 3.103"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.103 Quotient space is a vector space
> If $U$ is a subspace of $V$, then $V/U$ with the operations of [[Addition and scalar multiplication on V∕U]] is a vector space.

> [!proof]-
> **Well defined.** Suppose $v_1+U=v_2+U$ and $w_1+U=w_2+U$. By [[Two translates of a subspace are equal or disjoint]], $v_1-v_2,\ w_1-w_2\in U$, so $(v_1+w_1)-(v_2+w_2)\in U$ and $(v_1+w_1)+U=(v_2+w_2)+U$. Likewise $\lambda v_1-\lambda v_2=\lambda(v_1-v_2)\in U$ gives $(\lambda v_1)+U=(\lambda v_2)+U$.
>
> **Axioms.** *(Filled in.)* Each axiom for $V/U$ follows from the same axiom in $V$ applied to representatives, e.g. $(v+U)+(w+U)=(v+w)+U=(w+v)+U=(w+U)+(v+U)$. The zero is $0+U=U$ and $-(v+U)=(-v)+U$.

## Uses (in the proof)
- [[Two translates of a subspace are equal or disjoint]] (3.101)

## Connections
- Dimension: [[Dimension of quotient space]].
