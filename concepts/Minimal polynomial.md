---
subject: math
type: definition
source: "[[Axler LADR]] 5.24"
ladr: "5.24"
page: 145
aliases: ["LADR 5.24"]
tags: [linear-algebra, ladr/5B]
---
> [!definition] 5.24 Minimal polynomial
> For finite-dimensional $V$ and $T\in\Lin(V)$, the *minimal polynomial* of $T$ is the unique monic polynomial $p$ of smallest degree with $p(T)=0$.

> [!remark] Computing it
> Find the smallest $m$ for which $c_0I+c_1T+\dots+c_{m-1}T^{m-1}=-T^m$ is solvable. Faster in practice: solve $c_0v+\dots+c_{n-1}T^{n-1}v=-T^nv$ for one vector $v$; if the solution is unique, $c_0,\dots,c_{n-1},1$ are the coefficients.

## Connections
- Well defined by [[Existence, uniqueness, and degree of minimal polynomial]]. Eigenvalues are its zeros ([[Eigenvalues are the zeros of the minimal polynomial]]); it divides every annihilating polynomial ([[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]]); diagonalizability criterion: [[Necessary and sufficient condition for diagonalizability]].
