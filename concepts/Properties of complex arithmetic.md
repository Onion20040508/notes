---
subject: math
type: theorem
source: "[[Axler LADR]] 1.3"
ladr: "1.3"
page: 2
aliases: ["LADR 1.3"]
tags: [linear-algebra, ladr/1A]
---
> [!theorem] 1.3 Properties of complex arithmetic
> For all $\alpha,\beta,\lambda\in\C$:
> - **commutativity** $\alpha+\beta=\beta+\alpha$, $\alpha\beta=\beta\alpha$;
> - **associativity** $(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)$, $(\alpha\beta)\lambda=\alpha(\beta\lambda)$;
> - **identities** $\lambda+0=\lambda$, $\lambda 1=\lambda$;
> - **additive inverse** for every $\alpha$ there is a unique $\beta$ with $\alpha+\beta=0$;
> - **multiplicative inverse** for every $\alpha\neq 0$ there is a unique $\beta$ with $\alpha\beta=1$;
> - **distributive property** $\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$.

> [!proof]-
> Everything reduces to the corresponding property of $\R$ via the definitions in [[Complex numbers, C]]. For example,
> $$
> (a+bi)(c+di)=(ac-bd)+(ad+bc)i=(ca-db)+(cb+da)i=(c+di)(a+bi).
> $$
> *(Filled in.)* **Multiplicative inverse.** If $\alpha=a+bi\neq 0$ then $a^2+b^2>0$, and $\beta=\dfrac{a}{a^2+b^2}-\dfrac{b}{a^2+b^2}\,i$ satisfies $\alpha\beta=1$ by direct expansion. If also $\alpha\beta'=1$, then $\beta=\beta(\alpha\beta')=(\beta\alpha)\beta'=\beta'$. The additive inverse $-a-bi$ is unique by the same argument written additively.

## Uses (in the proof)
- [[Complex numbers, C]] (1.1)

## Connections
- These are the field axioms; $\R$ and $\C$ are fields. The vector-space axioms [[Vector space]] copy this list with scalars acting on vectors.
- Uniqueness of inverses is what makes [[−α, subtraction, 1∕α, division]] well defined.
