---
subject: math
type: definition
source: "[[Linear Algebra]] 1.1"
ladr: "1.1"
page: 2
aliases: ["LADR 1.1"]
tags: [linear-algebra, ladr/1A]
---
> [!definition] 1.1 Complex numbers, C
> A *complex number* is an ordered pair $(a,b)$ with $a,b\in\R$, written $a+bi$. The set of all complex numbers is $\C=\{a+bi : a,b\in\R\}$, with
> $$
> (a+bi)+(c+di)=(a+c)+(b+d)i,\qquad (a+bi)(c+di)=(ac-bd)+(ad+bc)i .
> $$
> We identify $a+0i$ with $a\in\R$ (so $\R\subseteq\C$), write $bi$ for $0+bi$, and $i$ for $0+1i$.

> [!remark] Why this multiplication
> Pretend $i^2=-1$ and expand $(a+bi)(c+di)$ with the usual rules: you get exactly the formula above. Conversely the formula gives $i\cdot i=-1$. So there is nothing to memorize.

## Connections
- Its arithmetic: [[Properties of complex arithmetic]]. Conjugate and absolute value come later in [[Complex conjugate, z, absolute value, ∣z∣]] and [[Properties of complex numbers]].
- Physics: quantum state spaces are complex vector spaces, which is one reason the whole theory is developed over $\F=\R$ or $\C$.
