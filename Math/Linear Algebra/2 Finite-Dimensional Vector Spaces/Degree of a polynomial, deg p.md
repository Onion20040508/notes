---
subject: math
type: definition
source: "[[Linear Algebra]] 2.11"
ladr: "2.11"
page: 31
aliases: ["LADR 2.11"]
tags: [linear-algebra, ladr/2A]
---
> [!definition] 2.11 Degree of a polynomial, deg p
> A polynomial $p$ has *degree $m$* if $p(z)=a_0+a_1z+\dots+a_mz^m$ for all $z$ with $a_m\neq 0$. The zero polynomial has degree $-\infty$. Notation: $\deg p$. With the convention $-\infty<m$, $\Poly_m(\F)$ denotes the polynomials of degree at most $m$ (so $0\in\Poly_m(\F)$).

## Connections
- $\Poly_m(\F)$ is spanned by $1,z,\dots,z^m$, a list that is linearly independent by [[Degree m implies at most m zeros]]; so $\dim\Poly_m(\F)=m+1$ ([[Dimension, dim V]]).
