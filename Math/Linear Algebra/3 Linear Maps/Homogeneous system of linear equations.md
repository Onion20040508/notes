---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.26"
ladr: "3.26"
page: 65
aliases: ["LADR 3.26"]
tags: [linear-algebra, ladr/3B]
---
> [!theorem] 3.26 Homogeneous system of linear equations
> A homogeneous system of linear equations with more variables than equations has nonzero solutions.

> [!proof]-
> Write the system $\sum_{k=1}^n A_{j,k}x_k=0$ ($j=1,\dots,m$) as $T(x)=0$, where $T:\F^n\to\F^m$,
> $$
> T(x_1,\dots,x_n)=\Big(\sum_{k}A_{1,k}x_k,\ \dots,\ \sum_{k}A_{m,k}x_k\Big).
> $$
> $T$ is linear and nonzero solutions are nonzero elements of $\nullsp T$. If $n>m$, $T$ is not injective by [[Linear map to a lower-dimensional space is not injective]], so $\nullsp T\neq\{0\}$ ([[Injectivity ⟺ null space equals {0}]]).

## Uses (in the proof)
- [[Linear map to a lower-dimensional space is not injective]] (3.22)
- [[Injectivity ⟺ null space equals {0}]] (3.15)

## Connections
- Also provable by Gaussian elimination; here it is pure dimension counting. Companion: [[Inhomogeneous system of linear equations]].
