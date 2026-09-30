---
subject: math
type: definition
source: "[[Linear Algebra]] 1.20"
ladr: "1.20"
page: 12
aliases: ["LADR 1.20"]
tags: [linear-algebra, ladr/1B]
---
> [!definition] 1.20 Vector space
> A *vector space* is a set $V$ with an addition and a scalar multiplication ([[Addition, scalar multiplication]]) such that:
> - **commutativity** $u+v=v+u$;
> - **associativity** $(u+v)+w=u+(v+w)$ and $(ab)v=a(bv)$;
> - **additive identity** there is $0\in V$ with $v+0=v$ for all $v$;
> - **additive inverse** for every $v$ there is $w$ with $v+w=0$;
> - **multiplicative identity** $1v=v$;
> - **distributive properties** $a(u+v)=au+av$ and $(a+b)v=av+bv$;
>
> for all $u,v,w\in V$ and $a,b\in\F$.

> [!remark] What is not assumed
> Uniqueness of $0$ and of inverses is not an axiom; it is proved in [[Unique additive identity]] and [[Unique additive inverse]]. Likewise $0v=0$ is proved ([[The number 0 times a vector]]), and it must use distributivity, the only axiom linking addition with scalar multiplication.

## Connections
- Examples: $\F^n$ ([[Fⁿ, coordinate]]), and $\F^\infty$, $\F^S$ (examples 1.23–1.25 in [[Linear Algebra]]).
- Real or complex: [[Real vector space, complex vector space]]. Subspaces: [[Subspace]].
- Physics: the superposition principle is the statement that states can be added and scaled, i.e. that they live in a vector space.
