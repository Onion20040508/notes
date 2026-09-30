---
subject: math
type: theorem
source: "[[Linear Algebra]] 2.39"
ladr: "2.39"
page: 45
aliases: ["LADR 2.39"]
tags: [linear-algebra, ladr/2C]
---
> [!theorem] 2.39 Subspace of full dimension equals the whole space
> If $V$ is finite-dimensional and $U$ is a subspace with $\dim U=\dim V$, then $U=V$.

> [!proof]-
> A basis $u_1,\dots,u_n$ of $U$ is linearly independent in $V$ and has length $n=\dim V$, so it is a basis of $V$ by [[Linearly independent list of the right length is a basis]]. Thus every $v\in V$ is a combination of the $u_k$, i.e. $v\in U$.

## Uses (in the proof)
- [[Linearly independent list of the right length is a basis]] (2.38)

## Connections
- Typical use: to prove $U=V$, show $U\subseteq V$ and compare dimensions.
