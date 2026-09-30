---
subject: math
type: theorem
source: "[[Axler LADR]] 3.22"
ladr: "3.22"
page: 63
aliases: ["LADR 3.22"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.22 Linear map to a lower-dimensional space is not injective
> If $V,W$ are finite-dimensional and $\dim V>\dim W$, then no linear map $V\to W$ is injective.

> [!proof]-
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]] and [[Dimension of a subspace]]:
> $$
> \dim\nullsp T=\dim V-\dim\range T\ \ge\ \dim V-\dim W\ >\ 0 .
> $$
> So $\nullsp T\neq\{0\}$ and $T$ is not injective by [[Injectivity ⟺ null space equals {0}]].

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Dimension of a subspace]] (2.37)
- [[Injectivity ⟺ null space equals {0}]] (3.15)

## Connections
- Linear equations: [[Homogeneous system of linear equations]].
