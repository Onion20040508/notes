---
subject: math
type: theorem
source: "[[Axler LADR]] 3.125"
ladr: "3.125"
page: 110
aliases: ["LADR 3.125"]
tags: [linear-algebra, ladr/3F]
---
> [!theorem] 3.125 Dimension of the annihilator
> If $V$ is finite-dimensional and $U$ is a subspace, then $\dim U^0=\dim V-\dim U$.

> [!remark] The hands-on proof
> Alternatively: with the extended basis and its dual basis $\varphi_1,\dots,\varphi_n$, the functionals dual to the $w$'s form a basis of $U^0$.

> [!proof]-
> Let $i\in\Lin(U,V)$ be the inclusion; then $i'\in\Lin(V',U')$ and $i'(\varphi)=\varphi|_U$. So $\nullsp i'=U^0$. By [[Fundamental theorem of linear maps]] and [[Dim V′ = dim V]],
> $$
> \dim\range i'+\dim U^0=\dim V'=\dim V .
> $$
> *(Filled in: Axler cites an exercise.)* $i'$ is surjective: given $\varphi\in U'$, extend a basis $u_1,\dots,u_m$ of $U$ to a basis $u_1,\dots,u_m,w_1,\dots,w_k$ of $V$ ([[Every linearly independent list extends to a basis]]) and let $\psi\in V'$ agree with $\varphi$ on the $u$'s and vanish on the $w$'s ([[Linear map lemma]]); then $i'(\psi)=\varphi$. Hence $\dim\range i'=\dim U'=\dim U$, giving $\dim U+\dim U^0=\dim V$.

## Uses (in the proof)
- [[Fundamental theorem of linear maps]] (3.21)
- [[Dim V′ = dim V]] (3.111)
- [[Every linearly independent list extends to a basis]] (2.32)
- [[Linear map lemma]] (3.4)

## Connections
- Same count as [[Dimension of quotient space]]; indeed $U^0\cong(V/U)'$.
- Inner-product analogue: [[Dimension of orthogonal complement]].
