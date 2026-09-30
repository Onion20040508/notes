---
subject: math
type: theorem
source: "[[Axler LADR]] 5.31"
ladr: "5.31"
page: 148
aliases: ["LADR 5.31"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.31 Minimal polynomial of a restriction operator
> If $V$ is finite-dimensional, $T\in\Lin(V)$, and $U$ is invariant under $T$, then the minimal polynomial of $T$ is a polynomial multiple of the minimal polynomial of $T|_U$.

> [!proof]-
> Let $p$ be the minimal polynomial of $T$. Then $p(T)u=0$ for all $u\in U$, i.e. $p(T|_U)=0$. Apply [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]] to $T|_U$.

## Uses (in the proof)
- [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]] (5.29)

## Connections
- Used in the diagonalizability of restrictions: [[Restriction of diagonalizable operator to invariant subspace]].
