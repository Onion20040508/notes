---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.15"
ladr: "4.15"
page: 126
aliases: ["LADR 4.15"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.15 Factorization of a quadratic polynomial
> For $b,c\in\R$: $x^2+bx+c=(x-\lambda_1)(x-\lambda_2)$ with $\lambda_1,\lambda_2\in\R$ if and only if $b^2\ge4c$.

> [!proof]-
> Complete the square: $x^2+bx+c=\big(x+\tfrac b2\big)^2+\big(c-\tfrac{b^2}{4}\big)$.
>
> If $b^2<4c$, the right side is positive for every real $x$, so there is no real zero and no such factorization.
>
> If $b^2\ge4c$, pick $d\in\R$ with $d^2=\tfrac{b^2}{4}-c$; then $x^2+bx+c=\big(x+\tfrac b2+d\big)\big(x+\tfrac b2-d\big)$.

## Uses (in the proof)
- (definitions only)

## Connections
- The irreducible quadratics ($b^2<4c$) appear in [[Factorization of a polynomial over R]], [[Even-dimensional null space]], [[Operators on odd-dimensional vector spaces have eigenvalues]].
