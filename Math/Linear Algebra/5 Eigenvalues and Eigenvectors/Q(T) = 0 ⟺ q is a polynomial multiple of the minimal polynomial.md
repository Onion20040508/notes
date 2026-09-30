---
subject: math
type: theorem
source: "[[Linear Algebra]] 5.29"
ladr: "5.29"
page: 148
aliases: ["LADR 5.29"]
tags: [linear-algebra, ladr/5B]
---
> [!theorem] 5.29 Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial
> Let $V$ be finite-dimensional, $T\in\Lin(V)$, $q\in\Poly(\F)$. Then $q(T)=0$ iff $q$ is a polynomial multiple of the minimal polynomial $p$ of $T$.

> [!proof]-
> ($\Rightarrow$) By [[Division algorithm for polynomials]], $q=ps+r$ with $\deg r<\deg p$. Then $0=q(T)=p(T)s(T)+r(T)=r(T)$. If $r\ne0$, dividing by its leading coefficient gives a monic annihilator of degree $<\deg p$, impossible. So $r=0$ and $q=ps$.
>
> ($\Leftarrow$) If $q=ps$ then $q(T)=p(T)s(T)=0$ ([[Multiplicative properties]]).

## Uses (in the proof)
- [[Division algorithm for polynomials]] (4.9)
- [[Multiplicative properties]] (5.17)

## Connections
- Minimal polynomial of a restriction divides: [[Minimal polynomial of a restriction operator]]. With Cayley–Hamilton: minimal polynomial divides the characteristic polynomial ([[Characteristic polynomial is a multiple of minimal polynomial]]).
