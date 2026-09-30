---
subject: math
type: theorem
source: "[[Axler LADR]] 3.46"
ladr: "3.46"
page: 75
aliases: ["LADR 3.46"]
tags: [linear-algebra, ladr/3C]
---
> [!theorem] 3.46 Entry of matrix product equals row times column
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $(AB)_{j,k}=A_{j,\cdot}\,B_{\cdot,k}$: the $(j,k)$ entry of $AB$ is row $j$ of $A$ times column $k$ of $B$.

> [!proof]-
> Both sides equal $A_{j,1}B_{1,k}+\dots+A_{j,n}B_{n,k}$ by [[Matrix multiplication]], the right side being a $1$-by-$n$ times $n$-by-$1$ product.

## Uses (in the proof)
- [[Matrix multiplication]] (3.41)

## Connections
- Column version: [[Column of matrix product equals matrix times column]].
