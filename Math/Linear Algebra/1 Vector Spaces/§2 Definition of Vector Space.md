---
type: section
subject: "[[Linear Algebra]]"
chapter: 1
section: 2
aliases: ["LADR 1B", "1B Definition of Vector Space"]
tags: [linear-algebra]
---
← [[§1 Rⁿ and Cⁿ]] · ↑ [[· 1 Vector Spaces]] · [[§3 Subspaces]] →

> [!definition] Definition 1.19: Addition, scalar multiplication
> - An *addition* on a set $V$ is a function assigning an element $u+v\in V$ to each pair $u,v\in V$.
> - A *scalar multiplication* on $V$ is a function assigning an element $\lambda v\in V$ to each $\lambda\in\F$ and $v\in V$.

^ladr-1-19

> [!remark]- Connections
> - The two operations in [[§2 Definition of Vector Space#^ladr-1-20|Vector space]]. Note the closure is built in: results land in $V$.

> [!definition] Definition 1.20: Vector space
> A *vector space* is a set $V$ with an addition and a scalar multiplication ([[§2 Definition of Vector Space#^ladr-1-19|Addition, scalar multiplication]]) such that:
> - **commutativity** $u+v=v+u$;
> - **associativity** $(u+v)+w=u+(v+w)$ and $(ab)v=a(bv)$;
> - **additive identity** there is $0\in V$ with $v+0=v$ for all $v$;
> - **additive inverse** for every $v$ there is $w$ with $v+w=0$;
> - **multiplicative identity** $1v=v$;
> - **distributive properties** $a(u+v)=au+av$ and $(a+b)v=av+bv$;
>
> for all $u,v,w\in V$ and $a,b\in\F$.

^ladr-1-20

> [!remark] Remark: What is not assumed
> Uniqueness of $0$ and of inverses is not an axiom; it is proved in [[§2 Definition of Vector Space#^ladr-1-26|Unique additive identity]] and [[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]]. Likewise $0v=0$ is proved ([[§2 Definition of Vector Space#^ladr-1-30|The number 0 times a vector]]), and it must use distributivity, the only axiom linking addition with scalar multiplication.

> [!remark]- Connections
> - Examples: $\F^n$ ([[§1 Rⁿ and Cⁿ#^ladr-1-11|Fⁿ, coordinate]]), and $\F^\infty$, $\F^S$ (examples 1.23–1.25 in [[Linear Algebra]]).
> - Real or complex: [[§2 Definition of Vector Space#^ladr-1-22|Real vector space, complex vector space]]. Subspaces: [[§3 Subspaces#^ladr-1-33|Subspace]].
> - Physics: the superposition principle is the statement that states can be added and scaled, i.e. that they live in a vector space.
> - Forgetting scalar multiplication, (V, +) is an abelian group: [[§1 The Definition of a Group#^def-1-2|493 Def. §1.2]].
> - Same definition in 556, as a linear space: [[§1 Linear Spaces#^def-1-1|556 Def. §1.1]].
> - The axioms checked for ℝⁿ in Stewart: [[§81 Vectors#^thm-81-5|Calc Thm. §81.5]].
> - Computational version: [[§23 Vector Spaces and Subspaces#^def-23-1|235 Def. §23.1]] (real scalars, ten axioms), with the catalogue ℝⁿ, signals, ℙₙ, functions and matrices in [[§23 Vector Spaces and Subspaces#^ex-23-1|235 Ex. §23.1]].

> [!definition] Definition 1.21: Vector, point
> Elements of a vector space are called *vectors* or *points*. When the field matters we say $V$ is a vector space *over* $\F$.

^ladr-1-21

> [!remark]- Connections
> - See [[§2 Definition of Vector Space#^ladr-1-20|Vector space]], [[§2 Definition of Vector Space#^ladr-1-22|Real vector space, complex vector space]].

> [!definition] Definition 1.22: Real vector space, complex vector space
> A vector space over $\R$ is a *real vector space*; a vector space over $\C$ is a *complex vector space*.

^ladr-1-22

> [!remark] Remark: The field matters
> As sets $\C$ and $\R^2$ can be identified, but $\C$ has dimension $1$ over $\C$ and dimension $2$ over $\R$ (see [[§6 Dimension#^ladr-2-35|Dimension, dim V]], [[§6 Dimension#^ladr-2-37|Dimension of a subspace]]).

> [!remark]- Connections
> - Complex scalars are what guarantee eigenvalues: [[Existence of eigenvalues]], versus [[§15 The Minimal Polynomial#^ladr-5-34|Operators on odd-dimensional vector spaces have eigenvalues]] over $\R$.

> [!example] Example 1.23: F^∞ (p. 13)
> $\F^\infty$ is the set of all sequences $(x_1,x_2,\dots)$ with entries in $\F$, with termwise operations
> $$
> (x_1,x_2,\dots)+(y_1,y_2,\dots)=(x_1+y_1,x_2+y_2,\dots),\qquad \lambda(x_1,x_2,\dots)=(\lambda x_1,\lambda x_2,\dots).
> $$
> It is a vector space ([[§2 Definition of Vector Space#^ladr-1-20|1.20]]) with zero the all-$0$ sequence. It is the standard home of infinite-dimensional phenomena, e.g. the shift operators (see [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|3.65]]).

^ladr-1-23

> [!remark] Notation 1.24: F^S (p. 13)

^ladr-1-24

> [!example] Example 1.25: $\F^S$ is a vector space (p. 14)
> For a nonempty set $S$, $\F^S$ (functions $S\to\F$) with pointwise operations $(f+g)(x)=f(x)+g(x)$, $(\lambda f)(x)=\lambda f(x)$ is a vector space. Its zero is the function $0(x)=0$ and $(-f)(x)=-f(x)$.
>
> **Everything is a function space.** $\F^n=\F^{\{1,\dots,n\}}$ (write $x(k)$ for $x_k$) and $\F^\infty=\F^{\{1,2,\dots\}}$. Elements of a vector space may be lists, functions, or stranger objects; the axioms are all that matter.
>
> Physics: a wave function $\psi:\R^3\to\C$ is an element of such a function space (before any square-integrability condition is imposed).

^ladr-1-25

> [!remark]- Connections
> - Computational version: [[§23 Vector Spaces and Subspaces#^ex-23-1|235 Ex. §23.1]](e) (real-valued functions on a set, with pointwise operations).

> [!theorem] Theorem 1.26: Unique additive identity
> A vector space has a unique additive identity.

^ladr-1-26

> [!proof]+ Proof
> If $0$ and $0'$ are both additive identities, then
> $$
> 0'=0'+0=0+0'=0,
> $$
> using that $0$ is an identity, commutativity, and that $0'$ is an identity.

> [!remark]- Connections
> - Justifies speaking of *the* $0$ in [[§2 Definition of Vector Space#^ladr-1-20|Vector space]].
> - Same argument for the identity of any group: [[§2 First Consequences of the Axioms#^prop-2-2|493 Prop. §2.2]].
> - Computational version: [[§23 Vector Spaces and Subspaces#^prop-23-1|235 Prop. §23.1]] (the zero vector and negatives are unique).

> [!theorem] Theorem 1.27: Unique additive inverse
> Every element of a vector space has a unique additive inverse.

^ladr-1-27

> [!proof]+ Proof
> Let $v\in V$ and let $w,w'$ both be additive inverses of $v$. Then
> $$
> w=w+0=w+(v+w')=(w+v)+w'=0+w'=w'.
> $$

> [!remark]- Connections
> - Makes the notation $-v$ and $w-v:=w+(-v)$ legitimate (notation 1.28).
> - Computed concretely in [[§2 Definition of Vector Space#^ladr-1-32|The number −1 times a vector]]: $-v=(-1)v$.
> - Same argument for inverses in any group: [[§2 First Consequences of the Axioms#^prop-2-3|493 Prop. §2.3]].
> - Computational version: [[§23 Vector Spaces and Subspaces#^prop-23-1|235 Prop. §23.1]] (uniqueness of the negative −u).

> [!remark] Notation 1.28: −v, w − v (p. 15)

^ladr-1-28

> [!remark] Notation 1.29: V (p. 15)

^ladr-1-29

> [!theorem] Theorem 1.30: The number 0 times a vector
> $0v=0$ for every $v\in V$ (scalar $0$ on the left, vector $0$ on the right).

^ladr-1-30

> [!remark] Remark: Why distributivity
> The statement mixes scalar multiplication with the additive identity, and distributivity is the only axiom of [[§2 Definition of Vector Space#^ladr-1-20|Vector space]] relating the two operations.

> [!proof]+ Proof
> $0v=(0+0)v=0v+0v$. Add the additive inverse of $0v$ to both sides to get $0=0v$.

> [!remark]- Connections
> - Companion: [[§2 Definition of Vector Space#^ladr-1-31|A number times the vector 0]] ($a0=0$). Used in [[§2 Definition of Vector Space#^ladr-1-32|The number −1 times a vector]].
> - Computational version: [[§23 Vector Spaces and Subspaces#^prop-23-2|235 Prop. §23.2]], equation (1).

> [!theorem] Theorem 1.31: A number times the vector 0
> $a0=0$ for every $a\in\F$ (vector $0$ on both sides).

^ladr-1-31

> [!proof]+ Proof
> $a0=a(0+0)=a0+a0$. Add the additive inverse of $a0$ to both sides to get $0=a0$.

> [!remark]- Connections
> - Not the same statement as [[§2 Definition of Vector Space#^ladr-1-30|The number 0 times a vector]]: there the scalar is $0$, here the vector is $0$.
> - Computational version: [[§23 Vector Spaces and Subspaces#^prop-23-2|235 Prop. §23.2]], equation (2).

> [!theorem] Theorem 1.32: The number −1 times a vector
> $(-1)v=-v$ for every $v\in V$.

^ladr-1-32

> [!proof]+ Proof
> $v+(-1)v=1v+(-1)v=(1+(-1))v=0v=0$ by [[§2 Definition of Vector Space#^ladr-1-30|The number 0 times a vector]]. So $(-1)v$ is an additive inverse of $v$, hence equals $-v$ by uniqueness ([[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]]).

*Uses:* [[§2 Definition of Vector Space#^ladr-1-30|1.30]], [[§2 Definition of Vector Space#^ladr-1-27|1.27]]

> [!remark]- Connections
> - Used in [[§3 Subspaces#^ladr-1-34|Conditions for a subspace]] to see that subspaces contain additive inverses.
> - Computational version: [[§23 Vector Spaces and Subspaces#^prop-23-2|235 Prop. §23.2]], equation (3).
