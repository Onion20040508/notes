---
subject: math
type: theorem
source: "[[Axler LADR]] 3.57"
ladr: "3.57"
page: 78
aliases: ["LADR 3.57"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.57 Column rank equals row rank
> For every $A\in\F^{m,n}$, the column rank of $A$ equals the row rank of $A$.

> [!proof]-
> Let $c$ be the column rank and $A=CR$ as in [[Column–row factorization]]. By [[Matrix multiplication as linear combinations of columns]](b) every row of $A$ is a linear combination of the $c$ rows of $R$, so row rank $\le c=$ column rank. Applying this to $A^t$:
> $$
> \text{col rank}(A)=\text{row rank}(A^t)\le\text{col rank}(A^t)=\text{row rank}(A).
> $$

## Uses (in the proof)
- [[Column–row factorization]] (3.56)
- [[Matrix multiplication as linear combinations of columns]] (3.51)

## Connections
- Allows [[Rank]]. Alternative proof via duality: [[Column rank equals row rank (LADR 3.133)]].
