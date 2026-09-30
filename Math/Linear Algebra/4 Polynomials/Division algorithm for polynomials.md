---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.9"
ladr: "4.9"
page: 124
aliases: ["LADR 4.9"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.9 Division algorithm for polynomials
> Let $p,s\in\Poly(\F)$ with $s\neq0$. Then there are unique $q,r\in\Poly(\F)$ with
> $$
> p=sq+r\quad\text{and}\quad\deg r<\deg s .
> $$

> [!remark] A linear-algebra proof
> No long division: existence and uniqueness both come from a basis of $\Poly_n(\F)$.

> [!proof]-
> Let $n=\deg p$, $m=\deg s$. If $n<m$ take $q=0$, $r=p$. Otherwise consider
> $$
> 1,\ z,\ \dots,\ z^{m-1},\ s,\ zs,\ \dots,\ z^{n-m}s\quad\text{in }\Poly_n(\F).
> $$
> These have distinct degrees $0,1,\dots,n$, so they are linearly independent; there are $n+1=\dim\Poly_n(\F)$ of them, so they form a basis ([[Linearly independent list of the right length is a basis]]). Expand
> $$
> p=\underbrace{a_0+a_1z+\dots+a_{m-1}z^{m-1}}_{r}+s\,\underbrace{(b_0+b_1z+\dots+b_{n-m}z^{n-m})}_{q}.
> $$
> Then $\deg r<m$. *(Filled in.)* Uniqueness: any $q,r$ with $p=sq+r$, $\deg r<m$ expand $p$ in this basis, and coordinates are unique ([[Criterion for basis]]).

## Uses (in the proof)
- [[Linearly independent list of the right length is a basis]] (2.38)
- [[Criterion for basis]] (2.28)

## Connections
- Key step in [[Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]]: every annihilating polynomial is a multiple of the minimal polynomial.
