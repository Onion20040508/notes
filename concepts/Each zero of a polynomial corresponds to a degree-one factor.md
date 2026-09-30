---
subject: math
type: theorem
source: "[[Axler LADR]] 4.6"
ladr: "4.6"
page: 122
aliases: ["LADR 4.6"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.6 Each zero of a polynomial corresponds to a degree-one factor
> Let $p\in\Poly(\F)$ have degree $m\ge1$ and $\lambda\in\F$. Then $p(\lambda)=0$ iff there is $q\in\Poly(\F)$ of degree $m-1$ with
> $$
> p(z)=(z-\lambda)q(z)\quad\text{for all }z\in\F .
> $$

> [!proof]-
> ($\Rightarrow$) Write $p(z)=\sum_{k=0}^ma_kz^k$. Since $p(\lambda)=0$,
> $$
> p(z)=p(z)-p(\lambda)=\sum_{k=1}^m a_k(z^k-\lambda^k),\qquad z^k-\lambda^k=(z-\lambda)\sum_{j=1}^{k}\lambda^{j-1}z^{k-j}.
> $$
> So $p(z)=(z-\lambda)q(z)$ where $q$ has degree $m-1$ (its $z^{m-1}$ coefficient is $a_m\neq0$).
>
> ($\Leftarrow$) $p(\lambda)=(\lambda-\lambda)q(\lambda)=0$.

## Uses (in the proof)
- (definitions only)

## Connections
- Gives [[Degree m implies at most m zeros]], and the step $p(z)=(z-\lambda)q(z)$ in [[Existence of eigenvalues]] and [[Eigenvalues are the zeros of the minimal polynomial]].
