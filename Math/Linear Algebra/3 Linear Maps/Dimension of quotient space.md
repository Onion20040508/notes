---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.105"
ladr: "3.105"
page: 102
aliases: ["LADR 3.105"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.105 Dimension of quotient space
> If $V$ is finite-dimensional and $U$ is a subspace of $V$, then
> $$
> \dim V/U=\dim V-\dim U .
> $$

> [!proof]-
> Let $\pi$ be the quotient map ([[Quotient map, π]]). $v+U=0+U\iff v\in U$ by [[Two translates of a subspace are equal or disjoint]], so $\nullsp\pi=U$; and $\range\pi=V/U$ by definition. Apply [[Fundamental theorem of linear maps]]: $\dim V=\dim U+\dim V/U$.

## Uses (in the proof)
- [[Quotient map, π]] (3.104)
- [[Two translates of a subspace are equal or disjoint]] (3.101)
- [[Fundamental theorem of linear maps]] (3.21)

## Connections
- Compare with a complement $W$ ([[Every subspace of V is part of a direct sum equal to V]]): $V/U\cong W$, but the quotient needs no choice.
- Dual counterpart: $\dim U^0=\dim V-\dim U$ ([[Dimension of the annihilator]]).
