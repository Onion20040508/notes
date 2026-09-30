---
subject: math
type: definition
source: "[[Axler LADR]] 3.41"
ladr: "3.41"
page: 73
aliases: ["LADR 3.41"]
tags: [linear-algebra, ladr/3C]
---
> [!definition] 3.41 Matrix multiplication
> If $A$ is $m$-by-$n$ and $B$ is $n$-by-$p$, then $AB$ is the $m$-by-$p$ matrix with
> $$
> (AB)_{j,k}=\sum_{r=1}^{n}A_{j,r}B_{r,k}.
> $$

> [!remark] Why this definition
> It is forced by requiring $\mathcal{M}(ST)=\mathcal{M}(S)\mathcal{M}(T)$; see the computation in [[Matrix of product of linear maps (LADR 3.43)]]. The product is defined only when the number of columns of $A$ equals the number of rows of $B$.

## Connections
- Other ways to read the product: [[Entry of matrix product equals row times column]], [[Column of matrix product equals matrix times column]], [[Linear combination of columns]], [[Matrix multiplication as linear combinations of columns]].
