---
subject: math
type: theorem
source: "[[Axler LADR]] 3.28"
ladr: "3.28"
page: 65
aliases: ["LADR 3.28"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.28 Inhomogeneous system of linear equations
> An inhomogeneous system of linear equations with more equations than variables has no solution for some choice of the constant terms.

> [!proof]-
> With $T:\F^n\to\F^m$ as in [[Homogeneous system of linear equations]], the system $\sum_kA_{j,k}x_k=c_j$ is solvable exactly when $(c_1,\dots,c_m)\in\range T$. If $n<m$, $T$ is not surjective by [[Linear map to a higher-dimensional space is not surjective]], so some $(c_1,\dots,c_m)$ is not in the range.

## Uses (in the proof)
- [[Homogeneous system of linear equations]] (3.26)
- [[Linear map to a higher-dimensional space is not surjective]] (3.24)

## Connections
- Companion: [[Homogeneous system of linear equations]].
