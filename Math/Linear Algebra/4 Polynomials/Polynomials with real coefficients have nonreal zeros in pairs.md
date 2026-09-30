---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.14"
ladr: "4.14"
page: 126
aliases: ["LADR 4.14"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.14 Polynomials with real coefficients have nonreal zeros in pairs
> If $p\in\Poly(\C)$ has real coefficients and $\lambda\in\C$ is a zero of $p$, then so is $\bar\lambda$.

> [!proof]-
> From $a_0+a_1\lambda+\dots+a_m\lambda^m=0$ with all $a_k\in\R$, conjugate both sides using [[Properties of complex numbers]]: $a_0+a_1\bar\lambda+\dots+a_m\bar\lambda^m=0$.

## Uses (in the proof)
- [[Properties of complex numbers]] (4.4)

## Connections
- Pairs $(z-\lambda)(z-\bar\lambda)=z^2-2(\operatorname{Re}\lambda)z+|\lambda|^2$: the real quadratic factors of [[Factorization of a polynomial over R]].
- Physics: for real (e.g. time-reversal symmetric) problems, complex eigenvalues come in conjugate pairs.
