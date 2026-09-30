---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.12"
ladr: "4.12"
page: 124
aliases: ["LADR 4.12"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.12 Fundamental theorem of algebra, first version
> Every nonconstant polynomial with complex coefficients has a zero in $\C$.

> [!remark] Analysis inside algebra
> The proof needs a genuinely analytic input: a continuous function on a compact set attains its minimum (the extreme value theorem). There is no purely algebraic proof over $\C$.

> [!proof]-
> **$k$-th roots exist.** By De Moivre, $(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta$. Writing $w=r(\cos\theta+i\sin\theta)$, the number $r^{1/k}\big(\cos\frac{\theta}{k}+i\sin\frac{\theta}{k}\big)$ is a $k$-th root of $w$.
>
> **A minimum exists.** If $p$ has leading term $c_mz^m$, then $|p(z)|/|z|^m\to|c_m|$, so $|p(z)|\to\infty$ as $|z|\to\infty$. Hence the continuous function $|p|$ attains a global minimum at some $\zeta\in\C$ (minimize over a large closed disk, which is compact).
>
> **The minimum is $0$.** Suppose $p(\zeta)\ne0$ and set $q(z)=p(z+\zeta)/p(\zeta)$, so $|q|$ has global minimum $1$ at $0$. Write $q(z)=1+a_kz^k+\dots+a_mz^m$ with $a_k\ne0$ the first nonzero coefficient after the constant, and choose $\beta$ with $\beta^k=-1/a_k$. There is $c>1$ such that for $t\in(0,1)$
> $$
> |q(t\beta)|\le|1+a_kt^k\beta^k|+t^{k+1}c=1-t^k(1-tc).
> $$
> With $t=1/(2c)$ this is $<1$, a contradiction. So $p(\zeta)=0$.

## Uses (in the proof)
- (definitions only)

## Connections
- Second version: [[Fundamental theorem of algebra, second version]]. The reason complex operators have eigenvalues: [[Existence of eigenvalues]].
