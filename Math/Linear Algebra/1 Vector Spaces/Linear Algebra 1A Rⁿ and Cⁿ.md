---
type: section
subject: "[[Linear Algebra]]"
chapter: 1
section: "1A"
tags: [linear-algebra]
---
↑ [[Linear Algebra — 1 Vector Spaces]] · [[Linear Algebra 1B Definition of Vector Space]] →

> [!definition] 1.1 Complex numbers, C
> A *complex number* is an ordered pair $(a,b)$ with $a,b\in\R$, written $a+bi$. The set of all complex numbers is $\C=\{a+bi : a,b\in\R\}$, with
> $$
> (a+bi)+(c+di)=(a+c)+(b+d)i,\qquad (a+bi)(c+di)=(ac-bd)+(ad+bc)i .
> $$
> We identify $a+0i$ with $a\in\R$ (so $\R\subseteq\C$), write $bi$ for $0+bi$, and $i$ for $0+1i$.

^ladr-1-1

> [!remark] Why this multiplication
> Pretend $i^2=-1$ and expand $(a+bi)(c+di)$ with the usual rules: you get exactly the formula above. Conversely the formula gives $i\cdot i=-1$. So there is nothing to memorize.

> [!remark]- Connections
> - Its arithmetic: [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-3|Properties of complex arithmetic]]. Conjugate and absolute value come later in [[Linear Algebra 4 Polynomials#^ladr-4-2|Complex conjugate, z, absolute value, ∣z∣]] and [[Linear Algebra 4 Polynomials#^ladr-4-4|Properties of complex numbers]].
> - Physics: quantum state spaces are complex vector spaces, which is one reason the whole theory is developed over $\F=\R$ or $\C$.

> [!example] 1.2 Complex arithmetic (p. 2)

^ladr-1-2

> [!theorem] 1.3 Properties of complex arithmetic
> For all $\alpha,\beta,\lambda\in\C$:
> - **commutativity** $\alpha+\beta=\beta+\alpha$, $\alpha\beta=\beta\alpha$;
> - **associativity** $(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)$, $(\alpha\beta)\lambda=\alpha(\beta\lambda)$;
> - **identities** $\lambda+0=\lambda$, $\lambda 1=\lambda$;
> - **additive inverse** for every $\alpha$ there is a unique $\beta$ with $\alpha+\beta=0$;
> - **multiplicative inverse** for every $\alpha\neq 0$ there is a unique $\beta$ with $\alpha\beta=1$;
> - **distributive property** $\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$.

^ladr-1-3

> [!proof]+
> Everything reduces to the corresponding property of $\R$ via the definitions in [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-1|Complex numbers, C]]. For example,
> $$
> (a+bi)(c+di)=(ac-bd)+(ad+bc)i=(ca-db)+(cb+da)i=(c+di)(a+bi).
> $$
> *(Filled in.)* **Multiplicative inverse.** If $\alpha=a+bi\neq 0$ then $a^2+b^2>0$, and $\beta=\dfrac{a}{a^2+b^2}-\dfrac{b}{a^2+b^2}\,i$ satisfies $\alpha\beta=1$ by direct expansion. If also $\alpha\beta'=1$, then $\beta=\beta(\alpha\beta')=(\beta\alpha)\beta'=\beta'$. The additive inverse $-a-bi$ is unique by the same argument written additively.

*Uses:* [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-1|1.1]]

> [!remark]- Connections
> - These are the field axioms; $\R$ and $\C$ are fields. The vector-space axioms [[Linear Algebra 1B Definition of Vector Space#^ladr-1-20|Vector space]] copy this list with scalars acting on vectors.
> - Uniqueness of inverses is what makes [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-5|−α, subtraction, 1∕α, division]] well defined.

> [!example] 1.4 Commutativity of complex multiplication (p. 2)

^ladr-1-4

> [!definition] 1.5 −α, subtraction, 1∕α, division
> Let $\alpha,\beta\in\C$.
> - $-\alpha$ is the additive inverse of $\alpha$, i.e. the unique number with $\alpha+(-\alpha)=0$.
> - Subtraction: $\beta-\alpha=\beta+(-\alpha)$.
> - For $\alpha\neq 0$, $1/\alpha$ is the multiplicative inverse, the unique number with $\alpha(1/\alpha)=1$.
> - Division: $\beta/\alpha=\beta(1/\alpha)$ for $\alpha\ne 0$.

^ladr-1-5

> [!remark]- Connections
> - Well defined because of the uniqueness parts of [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-3|Properties of complex arithmetic]].
> - The same move for vectors: [[Linear Algebra 1B Definition of Vector Space#^ladr-1-27|Unique additive inverse]] makes $-v$ and $w-v$ meaningful.

> [!remark] 1.6 Notation: F (p. 4)

^ladr-1-6

> [!example] 1.7 R (p. 4)

^ladr-1-7

> [!definition] 1.8 List, length
> For an integer $n\ge 0$, a *list of length $n$* is an ordered collection of $n$ elements. Two lists are equal iff they have the same length and the same elements in the same order.

^ladr-1-8

> [!remark] Lists versus sets
> Order and repetition matter in a list, not in a set. Every list has *finite* length, so $(x_1,x_2,\dots)$ is not a list. The empty list $(\,)$ has length $0$.

> [!remark]- Connections
> - Spanning lists, linearly independent lists and bases ([[Linear Algebra 2B Bases#^ladr-2-26|Basis]]) are lists, so repetitions count: a list with a repeated vector is linearly dependent ([[Linear Algebra 2A Span and Linear Independence#^ladr-2-17|Linearly dependent]]).
> - Finite length is built into [[Linear Algebra 2A Span and Linear Independence#^ladr-2-9|Finite-dimensional vector space]]: finite-dimensional means some *list* spans.

> [!example] 1.9 Lists versus sets (p. 4)

^ladr-1-9

> [!remark] 1.10 Notation: N (p. 6)

^ladr-1-10

> [!definition] 1.11 Fⁿ, coordinate
> $\F^n=\{(x_1,\dots,x_n) : x_k\in\F \text{ for } k=1,\dots,n\}$, the set of lists of length $n$ with entries in $\F$ ($\F$ denotes $\R$ or $\C$). For $x=(x_1,\dots,x_n)$, $x_k$ is its *$k$-th coordinate*.

^ladr-1-11

> [!remark]- Connections
> - With [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] and [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-18|Scalar multiplication in Fⁿ]] it is a vector space ([[Linear Algebra 1B Definition of Vector Space#^ladr-1-20|Vector space]]).
> - Every $n$-dimensional space over $\F$ is isomorphic to $\F^n$: [[Dimension shows whether vector spaces are isomorphic]].

> [!example] 1.12 C⁴ (p. 6)

^ladr-1-12

> [!definition] 1.13 Addition in Fⁿ
> Addition in $\F^n$ is coordinatewise:
> $$
> (x_1,\dots,x_n)+(y_1,\dots,y_n)=(x_1+y_1,\dots,x_n+y_n).
> $$

^ladr-1-13

> [!remark]- Connections
> - Commutative: [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-14|Commutativity of addition in F]]. Inverses: [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-17|Additive inverse in Fⁿ, −x]].

> [!theorem] 1.14 Commutativity of addition in F
> If $x,y\in\F^n$, then $x+y=y+x$.

^ladr-1-14

> [!proof]+
> Write $x=(x_1,\dots,x_n)$, $y=(y_1,\dots,y_n)$. By [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] and commutativity in $\F$,
> $$
> x+y=(x_1+y_1,\dots,x_n+y_n)=(y_1+x_1,\dots,y_n+x_n)=y+x.
> $$

*Uses:* [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-13|1.13]]

> [!remark]- Connections
> - Model for checking every axiom of [[Linear Algebra 1B Definition of Vector Space#^ladr-1-20|Vector space]] for $\F^n$: reduce to the coordinates.

> [!remark] 1.15 Notation: 0 (p. 6)

^ladr-1-15

> [!example] 1.16 Context determines which 0 is intended (p. 6)

^ladr-1-16

> [!definition] 1.17 Additive inverse in Fⁿ, −x
> For $x\in\F^n$, the *additive inverse* $-x\in\F^n$ is the vector with $x+(-x)=0$. Explicitly $-(x_1,\dots,x_n)=(-x_1,\dots,-x_n)$.

^ladr-1-17

> [!remark] Picture
> In $\R^2$, $-x$ has the same length as $x$ and points the opposite way.

> [!remark]- Connections
> - General vector spaces: [[Linear Algebra 1B Definition of Vector Space#^ladr-1-27|Unique additive inverse]] and [[Linear Algebra 1B Definition of Vector Space#^ladr-1-32|The number −1 times a vector]].

> [!definition] 1.18 Scalar multiplication in Fⁿ
> For $\lambda\in\F$ and $(x_1,\dots,x_n)\in\F^n$,
> $$
> \lambda(x_1,\dots,x_n)=(\lambda x_1,\dots,\lambda x_n).
> $$

^ladr-1-18

> [!remark] Scalar times vector
> The output is a vector. Contrast the [[Linear Algebra 6A Inner Products and Norms#^ladr-6-1|Dot product]], which takes two vectors and returns a scalar; that idea is generalized by the [[Linear Algebra 6A Inner Products and Norms#^ladr-6-2|Inner product]] in Chapter 6. In $\R^2$, $\lambda x$ stretches or shrinks $x$ by $|\lambda|$ and reverses it when $\lambda<0$.

> [!remark]- Connections
> - Together with [[Linear Algebra 1A Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] this makes $\F^n$ a vector space ([[Linear Algebra 1B Definition of Vector Space#^ladr-1-20|Vector space]]).
