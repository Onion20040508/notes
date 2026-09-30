---
subject: math
type: theorem
source: "[[Axler LADR]] 3.18"
ladr: "3.18"
page: 61
aliases: ["LADR 3.18"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.18 The range is a subspace
> If $T\in\Lin(V,W)$, then $\range T$ is a subspace of $W$.

> [!proof]-
> $0=T(0)\in\range T$ by [[Linear maps take 0 to 0]]. If $w_1=Tv_1$, $w_2=Tv_2$, then $w_1+w_2=T(v_1+v_2)\in\range T$. If $w=Tv$ then $\lambda w=T(\lambda v)\in\range T$. Conclude by [[Conditions for a subspace]].

## Uses (in the proof)
- [[Linear maps take 0 to 0]] (3.10)
- [[Conditions for a subspace]] (1.34)

## Connections
- Companion: [[The null space is a subspace]].
