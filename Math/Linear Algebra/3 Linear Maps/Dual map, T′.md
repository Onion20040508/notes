---
subject: math
type: definition
source: "[[Linear Algebra]] 3.118"
ladr: "3.118"
page: 107
aliases: ["LADR 3.118"]
tags: [linear-algebra, ladr/3F]
---
> [!definition] 3.118 Dual map, $T'$
> For $T\in\Lin(V,W)$, the *dual map* $T'\in\Lin(W',V')$ is
> $$
> T'(\varphi)=\varphi\circ T\qquad(\varphi\in W').
> $$

> [!remark] Why it is linear, and the direction
> $\varphi\circ T$ is a linear functional on $V$, and $T'(\varphi+\psi)=(\varphi+\psi)\circ T=\varphi\circ T+\psi\circ T$, $T'(\lambda\varphi)=\lambda T'(\varphi)$. Note $T'$ goes *backwards*, from $W'$ to $V'$ (pullback).

## Connections
- Algebra: [[Algebraic properties of dual maps]]. Null space and range: [[The null space of T]], [[The range of T]]. Matrix is the transpose: [[Matrix of T (LADR 3.132)]].
- Not the adjoint $T^*$ of Chapter 7 ([[Adjoint, T∗]]), although both are represented by (conjugate) transposes.
