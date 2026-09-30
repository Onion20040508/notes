---
subject: math
type: theorem
source: "[[Linear Algebra]] 3.68"
ladr: "3.68"
page: 85
aliases: ["LADR 3.68"]
tags: [linear-algebra, ladr/3D]
---
> [!theorem] 3.68 ST = I ⟺ TS = I (on vector spaces of the same dimension)
> Let $V,W$ be finite-dimensional of the same dimension, $S\in\Lin(V,W)$, $T\in\Lin(W,V)$. Then $ST=I\iff TS=I$.

> [!proof]-
> Suppose $ST=I$. If $Tv=0$ then $v=STv=S0=0$, so $T$ is injective ([[Injectivity ⟺ null space equals {0}]]) and hence invertible ([[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]]). Multiplying $ST=I$ on the right by $T^{-1}$ gives $S=T^{-1}$, so $TS=I$. The converse follows by swapping roles.

## Uses (in the proof)
- [[Injectivity ⟺ null space equals {0}]] (3.15)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (3.65)

## Connections
- For square matrices: a one-sided inverse is automatically two-sided. Fails in infinite dimensions (shift operators).
