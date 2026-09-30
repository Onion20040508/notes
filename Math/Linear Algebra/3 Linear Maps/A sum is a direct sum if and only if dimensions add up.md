---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.94"
ladr: "3.94"
page: 98
aliases: ["LADR 3.94"]
tags: [linear-algebra, ladr/3E]
---
> [!theorem] 3.94 A sum is a direct sum if and only if dimensions add up
> Suppose $V$ is finite-dimensional and $V_1,\dots,V_m$ are subspaces. Then $V_1+\dots+V_m$ is a direct sum if and only if
> $$
> \dim(V_1+\dots+V_m)=\dim V_1+\dots+\dim V_m .
> $$

> [!remark] Case $m=2$
> Also follows from [[Direct sum of two subspaces]] and [[Dimension of a sum]]: the sum is direct iff $V_1\cap V_2=\{0\}$ iff $\dim(V_1\cap V_2)=0$.

> [!proof]-
> $\Gamma$ in [[Products and direct sums]] is surjective, so by [[Fundamental theorem of linear maps]] it is injective iff $\dim(V_1+\dots+V_m)=\dim(V_1\times\dots\times V_m)$. Combine with [[Products and direct sums]] and [[Dimension of a product is the sum of dimensions]].

## Uses (in the proof)
- [[Products and direct sums]] (3.93)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Dimension of a product is the sum of dimensions]] (3.92)

## Connections
- Used to show eigenspace and generalized-eigenspace decompositions fill $V$: [[Sum of eigenspaces is a direct sum]], [[Generalized eigenspace decomposition]].
