---
type: section
subject: "[[Linear Algebra]]"
chapter: 1
section: 1
aliases: ["LADR 1A", "1A Rⁿ and Cⁿ"]
tags: [linear-algebra]
---
↑ [[· 1 Vector Spaces]] · [[§2 Definition of Vector Space]] →

> [!definition] Definition 1.1: Complex numbers, C
> A *complex number* is an ordered pair $(a,b)$ with $a,b\in\R$, written $a+bi$. The set of all complex numbers is $\C=\{a+bi : a,b\in\R\}$, with
> $$
> (a+bi)+(c+di)=(a+c)+(b+d)i,\qquad (a+bi)(c+di)=(ac-bd)+(ad+bc)i .
> $$
> We identify $a+0i$ with $a\in\R$ (so $\R\subseteq\C$), write $bi$ for $0+bi$, and $i$ for $0+1i$.

^ladr-1-1

> [!remark] Remark: Why this multiplication
> Pretend $i^2=-1$ and expand $(a+bi)(c+di)$ with the usual rules: you get exactly the formula above. Conversely the formula gives $i\cdot i=-1$. So there is nothing to memorize.

> [!remark]- Connections
> - Its arithmetic: [[§1 Rⁿ and Cⁿ#^ladr-1-3|Properties of complex arithmetic]]. Conjugate and absolute value come later in [[§13 Polynomials#^ladr-4-2|Complex conjugate, z̄]], [[§13 Polynomials#^ladr-4-2b|absolute value, ∣z∣]] and [[§13 Polynomials#^ladr-4-4|Properties of complex numbers]].
> - Physics: quantum state spaces are complex vector spaces, which is one reason the whole theory is developed over $\F=\R$ or $\C$.
> - Computational version: [[§53 Complex Numbers#^def-53-1|235 Def. §53.1]] (a + bi with i² = −1, real and imaginary parts), with products worked in [[§53 Complex Numbers#^ex-53-1|235 Ex. §53.1]].
> - Computational version: [[§1 Sums and Products#^def-1-1|342 Def. §1.1]] (complex numbers as ordered pairs, the points of the complex plane) and [[§1 Sums and Products#^prop-1-2|342 Prop. §1.2]] (the rectangular form x + iy, with i² = −1).

> [!example] Example 1.2: Complex arithmetic (p. 2)
> Using the distributive and commutative properties of [[§1 Rⁿ and Cⁿ#^ladr-1-3|1.3]]:
> $$
> (2+3i)(4+5i)=8+10i+12i+15i^2=8+22i-15=-7+22i .
> $$
> This is the "pretend $i^2=-1$ and expand" recipe from [[§1 Rⁿ and Cⁿ#^ladr-1-1|1.1]].

^ladr-1-2

> [!theorem] Theorem 1.3: Properties of complex arithmetic
> For all $\alpha,\beta,\lambda\in\C$:
> - **commutativity** $\alpha+\beta=\beta+\alpha$, $\alpha\beta=\beta\alpha$;
> - **associativity** $(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)$, $(\alpha\beta)\lambda=\alpha(\beta\lambda)$;
> - **identities** $\lambda+0=\lambda$, $\lambda 1=\lambda$;
> - **additive inverse** for every $\alpha$ there is a unique $\beta$ with $\alpha+\beta=0$;
> - **multiplicative inverse** for every $\alpha\neq 0$ there is a unique $\beta$ with $\alpha\beta=1$;
> - **distributive property** $\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$.

^ladr-1-3

> [!proof]+ Proof
> Everything reduces to the corresponding property of $\R$ via the definitions in [[§1 Rⁿ and Cⁿ#^ladr-1-1|Complex numbers, C]]. For example,
> $$
> (a+bi)(c+di)=(ac-bd)+(ad+bc)i=(ca-db)+(cb+da)i=(c+di)(a+bi).
> $$
> *(Filled in.)* **Multiplicative inverse.** If $\alpha=a+bi\neq 0$ then $a^2+b^2>0$, and $\beta=\dfrac{a}{a^2+b^2}-\dfrac{b}{a^2+b^2}\,i$ satisfies $\alpha\beta=1$ by direct expansion. If also $\alpha\beta'=1$, then $\beta=\beta(\alpha\beta')=(\beta\alpha)\beta'=\beta'$. The additive inverse $-a-bi$ is unique by the same argument written additively.

*Uses:* [[§1 Rⁿ and Cⁿ#^ladr-1-1|1.1]]

> [!remark]- Connections
> - These are the field axioms ([[§3 The Set ℝ of Real Numbers#^def-3-1|451 Def. §3.1]]); $\R$ and $\C$ are fields. The vector-space axioms [[§2 Definition of Vector Space#^ladr-1-20|Vector space]] copy this list with scalars acting on vectors.
> - Uniqueness of inverses (the group-theory argument of [[§2 First Consequences of the Axioms#^prop-2-3|493 Prop. §2.3]], used in the proof above) is what makes [[§1 Rⁿ and Cⁿ#^ladr-1-5|−α, subtraction]], [[§1 Rⁿ and Cⁿ#^ladr-1-5b|1∕α, division]] well defined.
> - Computational version: [[§53 Complex Numbers#^thm-53-1|235 Thm. §53.1]] (the same laws, stated without proof), with the inverse 1/z = z̄/|z|² in [[§53 Complex Numbers#^prop-53-4|235 Prop. §53.4]].
> - Computational version: [[§2 Basic Algebraic Properties#^thm-2-1|342 Thm. §2.1]] (commutative, associative and distributive laws) and [[§2 Basic Algebraic Properties#^thm-2-4|342 Thm. §2.4]] (multiplicative inverse), proved from the pair definition, with worked examples.

> [!example] Example 1.4: Commutativity of complex multiplication (p. 3)
> For $\alpha=a+bi$, $\beta=c+di$:
> $$
> \alpha\beta=(ac-bd)+(ad+bc)i,\qquad \beta\alpha=(ca-db)+(cb+da)i .
> $$
> The two agree because real multiplication and addition are commutative. Every property in [[§1 Rⁿ and Cⁿ#^ladr-1-3|1.3]] is proved this way: reduce to $\R$.

^ladr-1-4

> [!definition] Definition 1.5: −α, subtraction
> Let $\alpha,\beta\in\C$.
> - $-\alpha$ is the additive inverse of $\alpha$, i.e. the unique number with $\alpha+(-\alpha)=0$.
> - Subtraction: $\beta-\alpha=\beta+(-\alpha)$.

^ladr-1-5

> [!remark]- Connections
> - The same move for vectors: [[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]] makes $-v$ and $w-v$ meaningful.

> [!definition] Definition 1.5b: 1∕α, division
> Let $\alpha,\beta\in\C$.
> - For $\alpha\neq 0$, $1/\alpha$ is the multiplicative inverse, the unique number with $\alpha(1/\alpha)=1$.
> - Division: $\beta/\alpha=\beta(1/\alpha)$ for $\alpha\ne 0$.

^ladr-1-5b

> [!remark]- Connections
> - Well defined because of the uniqueness parts of [[§1 Rⁿ and Cⁿ#^ladr-1-3|Properties of complex arithmetic]].
> - Computational version: [[§53 Complex Numbers#^def-53-2|235 Def. §53.2]] (subtraction) and [[§53 Complex Numbers#^prop-53-4|235 Prop. §53.4]] (reciprocals and quotients, with worked examples).

> [!remark] Notation 1.6: F (p. 4)
> Throughout, $\F$ stands for either $\R$ or $\C$; elements of $\F$ are called *scalars*.

^ladr-1-6

> [!example] Example 1.7: ℝ² and ℝ³ (p. 5)
> $\R^2=\{(x,y):x,y\in\R\}$ (the plane) and $\R^3=\{(x,y,z):x,y,z\in\R\}$ (ordinary space). The goal of the next definitions is to replace $2$ or $3$ by any $n$, and $\R$ by $\F$.

^ladr-1-7

> [!definition] Definition 1.8: List, length
> For an integer $n\ge 0$, a *list of length $n$* is an ordered collection of $n$ elements. Two lists are equal iff they have the same length and the same elements in the same order.

^ladr-1-8

> [!remark] Remark: Lists versus sets
> Order and repetition matter in a list, not in a set. Every list has *finite* length, so $(x_1,x_2,\dots)$ is not a list. The empty list $(\,)$ has length $0$.

> [!remark]- Connections
> - Spanning lists, linearly independent lists and bases ([[§5 Bases#^ladr-2-26|Basis]]) are lists, so repetitions count: a list with a repeated vector is linearly dependent ([[§4 Span and Linear Independence#^ladr-2-17|Linearly dependent]]).
> - Finite length is built into [[§4 Span and Linear Independence#^ladr-2-9|Finite-dimensional vector space]]: finite-dimensional means some *list* spans.

> [!example] Example 1.9: Lists versus sets (p. 5)
> - $(3,5)\ne(5,3)$ as lists, but $\{3,5\}=\{5,3\}$ as sets: **order** matters for lists.
> - $(4,4)\ne(4,4,4)$ (different lengths), but $\{4,4\}=\{4,4,4\}=\{4\}$: **repetition** matters for lists.

^ladr-1-9

> [!remark] Notation 1.10: n (p. 6)
> Fix a positive integer $n$ for the rest of the chapter.

^ladr-1-10

> [!definition] Definition 1.11: Fⁿ, coordinate
> $\F^n=\{(x_1,\dots,x_n) : x_k\in\F \text{ for } k=1,\dots,n\}$, the set of lists of length $n$ with entries in $\F$ ($\F$ denotes $\R$ or $\C$). For $x=(x_1,\dots,x_n)$, $x_k$ is its *$k$-th coordinate*.

^ladr-1-11

> [!remark]- Connections
> - With [[§1 Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] and [[§1 Rⁿ and Cⁿ#^ladr-1-18|Scalar multiplication in Fⁿ]] it is a vector space ([[§2 Definition of Vector Space#^ladr-1-20|Vector space]]).
> - Every $n$-dimensional space over $\F$ is isomorphic to $\F^n$: [[Dimension shows whether vector spaces are isomorphic]].
> - The real case, written as column vectors: [[§3 Vector Equations#^def-3-1|235 Def. §3.1]].

> [!example] Example 1.12: C⁴ (p. 6)
> $\C^4=\{(z_1,z_2,z_3,z_4):z_k\in\C\}$. It cannot be pictured ($\C^4$ is "8 real dimensions"), but its algebra is exactly as easy as that of $\R^2$. That is the point of working with $\F^n$ abstractly.

^ladr-1-12

> [!definition] Definition 1.13: Addition in Fⁿ
> Addition in $\F^n$ is coordinatewise:
> $$
> (x_1,\dots,x_n)+(y_1,\dots,y_n)=(x_1+y_1,\dots,x_n+y_n).
> $$

^ladr-1-13

> [!remark]- Connections
> - Commutative: [[§1 Rⁿ and Cⁿ#^ladr-1-14|Commutativity of addition in Fⁿ]]. Inverses: [[§1 Rⁿ and Cⁿ#^ladr-1-17|Additive inverse in Fⁿ, −x]].
> - In ℝ² and ℝ³: [[§81 Vectors#^thm-81-4|Calc Thm. §81.4]] (with worked examples).
> - In ℝⁿ: [[§3 Vector Equations#^def-3-2|235 Def. §3.2]] (entrywise sum, with examples).

> [!theorem] Theorem 1.14: Commutativity of addition in Fⁿ
> If $x,y\in\F^n$, then $x+y=y+x$.

^ladr-1-14

> [!proof]+ Proof
> Write $x=(x_1,\dots,x_n)$, $y=(y_1,\dots,y_n)$. By [[§1 Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] and commutativity in $\F$,
> $$
> x+y=(x_1+y_1,\dots,x_n+y_n)=(y_1+x_1,\dots,y_n+x_n)=y+x.
> $$

*Uses:* [[§1 Rⁿ and Cⁿ#^ladr-1-13|1.13]]

> [!remark]- Connections
> - Model for checking every axiom of [[§2 Definition of Vector Space#^ladr-1-20|Vector space]] for $\F^n$: reduce to the coordinates.
> - In ℝⁿ: property (i) of [[§3 Vector Equations#^thm-3-2|235 Thm. §3.2]], which lists all the vector-space laws of ℝⁿ.

> [!remark] Notation 1.15: 0 (p. 7)
> $0$ also denotes the list of length $n$ whose coordinates are all $0$: $0=(0,\dots,0)$.

^ladr-1-15

> [!example] Example 1.16: Context determines which 0 is intended (p. 7)
> In "$x+0=x$ for all $x\in\F^n$", the $0$ must be the list $(0,\dots,0)\in\F^n$: adding the *number* $0$ to a list is not defined. Context decides which $0$ is meant.
>
> A vector $v=(a,b)\in\R^2$ can be viewed as a point or as an arrow from the origin; as an arrow it may be moved parallel to itself without change, which is how vector addition is pictured (tip to tail).
>
> Move $y$ so that it starts at the tip of $x$; then $x+y$ (red) runs from $0$ to the new tip. Moving $x$ instead (dashed) gives the same point, so $x+y$ is the diagonal of the parallelogram spanned by $x$ and $y$:
>
> ![[ladr-1.16-tip-to-tail.svg|320]]

^ladr-1-16

> [!remark]- Connections
> - The tip-to-tail picture as a theorem: [[§3 Vector Equations#^thm-3-1|235 Thm. §3.1]] (parallelogram rule for addition in ℝ²).

> [!definition] Definition 1.17: Additive inverse in Fⁿ, −x
> For $x\in\F^n$, the *additive inverse* $-x\in\F^n$ is the vector with $x+(-x)=0$. Explicitly $-(x_1,\dots,x_n)=(-x_1,\dots,-x_n)$.

^ladr-1-17

> [!remark] Remark: Picture
> In $\R^2$, $-x$ has the same length as $x$ and points the opposite way.

> [!remark]- Connections
> - General vector spaces: [[§2 Definition of Vector Space#^ladr-1-27|Unique additive inverse]] and [[§2 Definition of Vector Space#^ladr-1-32|The number −1 times a vector]].

> [!definition] Definition 1.18: Scalar multiplication in Fⁿ
> For $\lambda\in\F$ and $(x_1,\dots,x_n)\in\F^n$,
> $$
> \lambda(x_1,\dots,x_n)=(\lambda x_1,\dots,\lambda x_n).
> $$

^ladr-1-18

> [!remark] Remark: Scalar times vector
> The output is a vector. Contrast the [[§19 Inner Products and Norms#^ladr-6-1|Dot product]], which takes two vectors and returns a scalar; that idea is generalized by the [[§19 Inner Products and Norms#^ladr-6-2|Inner product]] in Chapter 6. In $\R^2$, $\lambda x$ stretches or shrinks $x$ by $|\lambda|$ and reverses it when $\lambda<0$.

> [!remark]- Connections
> - Together with [[§1 Rⁿ and Cⁿ#^ladr-1-13|Addition in Fⁿ]] this makes $\F^n$ a vector space ([[§2 Definition of Vector Space#^ladr-1-20|Vector space]]).
> - In ℝ² and ℝ³: [[§81 Vectors#^thm-81-4|Calc Thm. §81.4]] (with worked examples).
> - In ℝⁿ: [[§3 Vector Equations#^def-3-2|235 Def. §3.2]] (entrywise scalar multiple, with examples).

%% ex:1.18-fig %%
> [!example] Example: Scalar multiples, pictured
> In $\R^2$ every $\lambda x$ lies on the line through $0$ and $x$ (dashed): $2x$ is twice as long as $x$, $\tfrac12x$ half as long, and $-x=(-1)x$ (red, [[§1 Rⁿ and Cⁿ#^ladr-1-17|1.17]]) has the same length as $x$ and points the opposite way.
>
> ![[ladr-1.18-scalar-multiples.svg|380]]
