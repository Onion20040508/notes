---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.32"
ladr: "2.32"
page: 41
aliases: ["LADR 2.32"]
tags: [linear-algebra, ladr/2B]
---
> [!theorem] 2.32 Every linearly independent list extends to a basis
> Every linearly independent list in a finite-dimensional vector space can be extended to a basis.

> [!proof]-
> Let $u_1,\dots,u_m$ be linearly independent in $V$ and let $w_1,\dots,w_n$ span $V$. Then $u_1,\dots,u_m,w_1,\dots,w_n$ spans $V$. Run the reduction procedure of [[Every spanning list contains a basis]] on this list. No $u_k$ is deleted, because $u_k\notin\Span(u_1,\dots,u_{k-1})$ by independence. The result is a basis consisting of $u_1,\dots,u_m$ and some $w$'s.

## Uses (in the proof)
- [[Every spanning list contains a basis]] (2.30)

## Connections
- The key step of [[Fundamental theorem of linear maps]], [[Every subspace of V is part of a direct sum equal to V]], [[Dimension of a sum]], [[Linearly independent list of the right length is a basis]].
- Inner-product version: [[Every orthonormal list extends to an orthonormal basis]] (via [[Gram–Schmidt procedure]]).
