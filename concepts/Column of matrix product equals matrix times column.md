---
subject: math
type: theorem
source: "[[Axler LADR]] 3.48"
ladr: "3.48"
page: 75
aliases: ["LADR 3.48"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.48 Column of matrix product equals matrix times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{\cdot,k}=A\,B_{\cdot,k}$: column $k$ of $AB$ is $A$ times column $k$ of $B$.

> [!proof]-
> Both are $m$-by-$1$, and the entry in row $j$ of each is $\sum_rA_{j,r}B_{r,k}$.

## Uses (in the proof)
- (definitions only)

## Connections
- Combined with [[Linear combination of columns]] gives [[Matrix multiplication as linear combinations of columns]].
