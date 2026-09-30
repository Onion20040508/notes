---
subject: math
type: theorem
source: "[[Axler LADR]] 1.34"
ladr: "1.34"
page: 18
aliases: ["LADR 1.34"]
tags: [linear-algebra, ladr/1C]
---
> [!theorem] 1.34 Conditions for a subspace
> A subset $U\subseteq V$ is a subspace of $V$ if and only if
> - **additive identity** $0\in U$;
> - **closed under addition** $u,w\in U \implies u+w\in U$;
> - **closed under scalar multiplication** $a\in\F,\ u\in U \implies au\in U$.

> [!remark] Variant
> "$0\in U$" can be replaced by "$U\neq\varnothing$": take $u\in U$, then $0=0u\in U$ by [[The number 0 times a vector]].

> [!proof]-
> If $U$ is a subspace, the three conditions hold by the definition of vector space.
>
> Conversely, assume the three conditions. The first puts the identity of $V$ in $U$; the second and third make addition and scalar multiplication operations on $U$. For $u\in U$, $-u=(-1)u\in U$ by [[The number −1 times a vector]] and closure, so inverses exist in $U$. *(Filled in.)* The remaining axioms (commutativity, associativity, multiplicative identity, distributivity) are identities that hold for all vectors of $V$, hence in particular for those of $U$.

## Uses (in the proof)
- [[The number −1 times a vector]] (1.32)

## Connections
- The workhorse for every 'is a subspace' claim: [[Sum of subspaces is the smallest containing subspace]], [[Span is the smallest containing subspace]], [[Null space, null T]], [[Range]].
