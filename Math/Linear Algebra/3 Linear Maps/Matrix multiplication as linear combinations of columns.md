---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.51"
ladr: "3.51"
page: 76
aliases: ["LADR 3.51"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.51 Matrix multiplication as linear combinations of columns
> Let $C$ be $m$-by-$c$ and $R$ be $c$-by-$n$.
> - (a) Column $k$ of $CR$ is a linear combination of the columns of $C$, with coefficients from column $k$ of $R$.
> - (b) Row $j$ of $CR$ is a linear combination of the rows of $R$, with coefficients from row $j$ of $C$.

> [!proof]-
> (a) Column $k$ of $CR$ is $CR_{\cdot,k}$ ([[Column of matrix product equals matrix times column]]), which is $\sum_rR_{r,k}C_{\cdot,r}$ by [[Linear combination of columns]].
>
> (b) *(Filled in; Axler leaves the row versions as exercises.)* The entry of row $j$ of $CR$ in column $k$ is $\sum_rC_{j,r}R_{r,k}$, which is the column-$k$ entry of $\sum_rC_{j,r}R_{r,\cdot}$. Hence $(CR)_{j,\cdot}=\sum_rC_{j,r}R_{r,\cdot}$.

## Uses (in the proof)
- [[Column of matrix product equals matrix times column]] (3.48)
- [[Linear combination of columns]] (3.50)

## Connections
- The tool behind [[Column–row factorization]] and [[Column rank equals row rank (LADR 3.57)]].
