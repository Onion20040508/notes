---
subject: math
type: theorem
source: "[[Axler LADR]] 5.32"
ladr: "5.32"
page: 149
aliases: ["LADR 5.32"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.32 T not invertible ⟺ constant term of minimal polynomial of T is 0
> For finite-dimensional $V$ and $T\in\Lin(V)$: $T$ is not invertible $\iff$ the constant term of the minimal polynomial of $T$ is $0$.

> [!remark] Inverse as a polynomial
> *(Filled in.)* If $p(z)=c_0+c_1z+\dots+z^m$ with $c_0\ne0$, then $T\big(c_1I+\dots+T^{m-1}\big)=-c_0I$, so $T^{-1}=-\tfrac1{c_0}\big(c_1I+c_2T+\dots+T^{m-1}\big)$ is a polynomial in $T$.

> [!proof]-
> $T$ not invertible $\iff0$ is an eigenvalue ([[Equivalent conditions to be an eigenvalue]]) $\iff0$ is a zero of $p$ ([[Eigenvalues are the zeros of the minimal polynomial]](a)) $\iff p(0)=0$, and $p(0)$ is the constant term.

## Uses (in the proof)
- [[Equivalent conditions to be an eigenvalue]] (5.7)
- [[Eigenvalues are the zeros of the minimal polynomial]] (5.27)

## Connections
- Determinant analogue: [[Invertible ⟺ nonzero determinant]].
