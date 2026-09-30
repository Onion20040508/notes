---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.16"
ladr: "4.16"
page: 128
aliases: ["LADR 4.16"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.16 Factorization of a polynomial over R
> A nonconstant $p\in\Poly(\R)$ has a factorization, unique up to order,
> $$
> p(x)=c(x-\lambda_1)\cdots(x-\lambda_m)(x^2+b_1x+c_1)\cdots(x^2+b_Mx+c_M)
> $$
> with all constants real and $b_k^2<4c_k$ for each $k$.

> [!proof]-
> **Existence.** View $p$ in $\Poly(\C)$. If all its zeros are real, use [[Fundamental theorem of algebra, second version]]. Otherwise let $\lambda\notin\R$ be a zero; by [[Polynomials with real coefficients have nonreal zeros in pairs]] so is $\bar\lambda$, and
> $$
> p(x)=(x-\lambda)(x-\bar\lambda)q(x)=\big(x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2\big)q(x)
> $$
> with $\deg q=\deg p-2$. For real $x$, $q(x)=p(x)/(x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2)$ is real (the denominator is positive), so the polynomial $\operatorname{Im}q$ vanishes on all of $\R$ and hence has zero coefficients ([[Degree m implies at most m zeros]]). Thus $q\in\Poly(\R)$, and induction on the degree finishes. The quadratic factor has $b^2<4c$ because it has no real zero ([[Factorization of a quadratic polynomial]]).
>
> **Uniqueness.** *(Filled in.)* Each irreducible real quadratic factor splits over $\C$ as $(x-\mu)(x-\bar\mu)$ with $\mu\notin\R$, so any real factorization yields a complex one. By uniqueness in [[Fundamental theorem of algebra, second version]], the multiset of complex zeros is determined; its real elements give the linear factors and its conjugate pairs of nonreal elements give the quadratic factors.

## Uses (in the proof)
- [[Fundamental theorem of algebra, second version]] (4.13)
- [[Polynomials with real coefficients have nonreal zeros in pairs]] (4.14)
- [[Degree m implies at most m zeros]] (4.8)
- [[Factorization of a quadratic polynomial]] (4.15)

## Connections
- Used in [[Operators on odd-dimensional vector spaces have eigenvalues]] to find an irreducible quadratic factor of a real minimal polynomial.
