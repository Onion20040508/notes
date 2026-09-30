---
subject: math
type: theorem
source: "[[Axler LADR]] 3.24"
ladr: "3.24"
page: 64
aliases: ["LADR 3.24"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.24 Linear map to a higher-dimensional space is not surjective
> If $V,W$ are finite-dimensional and $\dim V<\dim W$, then no linear map $V\to W$ is surjective.

> [!proof]-
> For $T\in\Lin(V,W)$, by [[Fundamental theorem of linear maps]],
> $$
> \dim\range T=\dim V-\dim\nullsp T\ \le\ \dim V\ <\ \dim W,
> $$
> so $\range T\neq W$.

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)

## Connections
- Linear equations: [[Inhomogeneous system of linear equations]].
