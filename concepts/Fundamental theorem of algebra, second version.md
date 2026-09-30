---
subject: math
type: theorem
source: "[[Axler LADR]] 4.13"
ladr: "4.13"
page: 126
aliases: ["LADR 4.13"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.13 Fundamental theorem of algebra, second version
> A nonconstant $p\in\Poly(\C)$ has a factorization, unique up to the order of the factors,
> $$
> p(z)=c(z-\lambda_1)\cdots(z-\lambda_m),\qquad c,\lambda_1,\dots,\lambda_m\in\C .
> $$

> [!proof]-
> Induction on $m=\deg p$; $m=1$ is clear.
>
> **Existence.** By [[Fundamental theorem of algebra, first version]], $p(\lambda)=0$ for some $\lambda$; by [[Each zero of a polynomial corresponds to a degree-one factor]], $p=(z-\lambda)q$ with $\deg q=m-1$, and $q$ factors by induction.
>
> **Uniqueness.** $c$ is the leading coefficient. If $(z-\lambda_1)\cdots(z-\lambda_m)=(z-\tau_1)\cdots(z-\tau_m)$, setting $z=\lambda_1$ shows some $\tau_j=\lambda_1$; relabel so $\tau_1=\lambda_1$. For $z\ne\lambda_1$ divide by $z-\lambda_1$:
> $$
> (z-\lambda_2)\cdots(z-\lambda_m)=(z-\tau_2)\cdots(z-\tau_m).
> $$
> *(Filled in.)* Both sides are polynomials agreeing at infinitely many points, so they are equal everywhere ([[Degree m implies at most m zeros]] applied to their difference). By induction the $\tau$'s are the $\lambda$'s up to order.

## Uses (in the proof)
- [[Fundamental theorem of algebra, first version]] (4.12)
- [[Each zero of a polynomial corresponds to a degree-one factor]] (4.6)
- [[Degree m implies at most m zeros]] (4.8)

## Connections
- Complex minimal polynomials split: [[Eigenvalues are the zeros of the minimal polynomial]](b). Real version: [[Factorization of a polynomial over R]].
