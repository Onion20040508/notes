---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.7"
ladr: "5.7"
page: 135
aliases: ["LADR 5.7"]
tags: [linear-algebra, ladr/5A]
---
> [!theorem] 5.7 Equivalent conditions to be an eigenvalue
> Let $V$ be finite-dimensional, $T\in\Lin(V)$, $\lambda\in\F$. The following are equivalent:
> - (a) $\lambda$ is an eigenvalue of $T$;
> - (b) $T-\lambda I$ is not injective;
> - (c) $T-\lambda I$ is not surjective;
> - (d) $T-\lambda I$ is not invertible.

> [!remark] Infinite dimensions
> (c) and (d) are then not equivalent to (a): this is why the spectrum of an operator on a Hilbert space can contain points that are not eigenvalues (continuous spectrum).

> [!proof]-
> (a)$\iff$(b): $Tv=\lambda v\iff(T-\lambda I)v=0$, so a nonzero eigenvector is a nonzero element of $\nullsp(T-\lambda I)$ ([[Injectivity ⟺ null space equals {0}]]). (b)$\iff$(c)$\iff$(d) by [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]].

## Uses (in the proof)
- [[Injectivity ⟺ null space equals {0}]] (3.15)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (3.65)

## Connections
- Used in [[T not invertible ⟺ constant term of minimal polynomial of T is 0]]. Determinant version: $\det(T-\lambda I)=0$ ([[Invertible ⟺ nonzero determinant]]).
