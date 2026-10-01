---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 23
lay: "4.1"
aliases: ["Lay 4.1"]
tags: [applied-linear-algebra, math235]
---
← [[§22 Cramer’s Rule, Volume, and Linear Transformations]] · ↑ [[· 4 Vector Spaces]] · [[§24 Null Spaces, Column Spaces, and Linear Transformations]] →

*Lay, Section 4.1 · MATH 235 lectures L10, L13, L14.*

Much of Chapters 1 and 2 used only a few algebraic properties of $\mathbb{R}^n$: vectors can be added and multiplied by scalars, and these operations obey the usual rules. A vector space is any set with two such operations obeying those rules (ten axioms). Polynomials, functions, discrete-time signals and matrices all form vector spaces, so everything proved from the axioms applies to them at once. Inside a vector space, a subspace is a subset closed under the two operations; it is then a vector space itself. The most common way to produce a subspace is as the span of finitely many vectors, which turns questions about infinitely many vectors into computations with a few.

## Vector Spaces

> [!definition] Definition §23.1: Vector Space
> A **vector space** is a nonempty set $V$ of objects, called *vectors*, on which are defined two operations, called *addition* and *multiplication by scalars* (real numbers), subject to the ten axioms below. The axioms must hold for all vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ in $V$ and all scalars $c$ and $d$.
> 1. The sum of $\mathbf{u}$ and $\mathbf{v}$, denoted by $\mathbf{u} + \mathbf{v}$, is in $V$.
> 2. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.
> 3. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$.
> 4. There is a **zero vector** $\mathbf{0}$ in $V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$.
> 5. For each $\mathbf{u}$ in $V$, there is a vector $-\mathbf{u}$ in $V$ such that $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$.
> 6. The scalar multiple of $\mathbf{u}$ by $c$, denoted by $c\mathbf{u}$, is in $V$.
> 7. $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$.
> 8. $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$.
> 9. $c(d\mathbf{u}) = (cd)\mathbf{u}$.
> 10. $1\mathbf{u} = \mathbf{u}$.
>
> Technically $V$ is a *real* vector space. All the theory of this chapter also holds for a *complex* vector space, in which the scalars are complex numbers ([[§36 Complex Eigenvalues|§36]], 5.5); until then all scalars are real.
>
> *Lay: 4.1, Definition*

^def-23-1

> [!remark]- Connections
> - Rigorous treatment: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]], over $\mathbf{F} = \mathbb{R}$ or $\mathbb{C}$ from the start; Axler packs Lay's axioms 1 and 6 into "addition and scalar multiplication are functions $V \times V \to V$, $\mathbf{F} \times V \to V$". The same definition over $\mathbb{R}$ or $\mathbb{C}$: [[§1 Linear Spaces#^def-1-1|556 Def. §1.1]].

> [!theorem] Proposition §23.1: The Zero Vector and Negatives Are Unique
> In a vector space $V$, the zero vector of Axiom 4 is unique, and for each $\mathbf{u}$ in $V$ the vector $-\mathbf{u}$ of Axiom 5, called the **negative** of $\mathbf{u}$, is unique.
>
> *Lay: 4.1 (text); Exercises 25 and 26*

^prop-23-1

> [!proof]+ Proof
> Because of Axiom 2, Axioms 4 and 5 also give $\mathbf{0} + \mathbf{u} = \mathbf{u}$ and $-\mathbf{u} + \mathbf{u} = \mathbf{0}$.
>
> **Zero.** Suppose $\mathbf{w}$ in $V$ also has the property $\mathbf{u} + \mathbf{w} = \mathbf{w} + \mathbf{u} = \mathbf{u}$ for all $\mathbf{u}$. Taking $\mathbf{u} = \mathbf{0}$ gives $\mathbf{0} + \mathbf{w} = \mathbf{0}$. But $\mathbf{0} + \mathbf{w} = \mathbf{w}$ by Axiom 4 (with Axiom 2). Hence $\mathbf{w} = \mathbf{0} + \mathbf{w} = \mathbf{0}$.
>
> **Negatives.** Suppose $\mathbf{w}$ satisfies $\mathbf{u} + \mathbf{w} = \mathbf{0}$. Adding $-\mathbf{u}$ to both sides,
>
> $$
> \begin{aligned}
> (-\mathbf{u}) + [\mathbf{u} + \mathbf{w}] &= (-\mathbf{u}) + \mathbf{0} \\
> [(-\mathbf{u}) + \mathbf{u}] + \mathbf{w} &= (-\mathbf{u}) + \mathbf{0} && \text{by Axiom 3} \\
> \mathbf{0} + \mathbf{w} &= (-\mathbf{u}) + \mathbf{0} && \text{by Axioms 2 and 5} \\
> \mathbf{w} &= -\mathbf{u} && \text{by Axioms 2 and 4.}
> \end{aligned}
> $$

^pf-23-1

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-1|Def. §23.1]]

> [!theorem] Proposition §23.2: Arithmetic with Zero and Negatives
> For each $\mathbf{u}$ in $V$ and scalar $c$,
>
> $$
> 0\mathbf{u} = \mathbf{0}, \qquad (1)
> \qquad\qquad
> c\mathbf{0} = \mathbf{0}, \qquad (2)
> \qquad\qquad
> -\mathbf{u} = (-1)\mathbf{u} . \qquad (3)
> $$
>
> *Lay: 4.1, Equations (1)–(3); Exercises 27–29*

^prop-23-2

> [!proof]+ Proof
> **(1)** By Axiom 8, $0\mathbf{u} = (0 + 0)\mathbf{u} = 0\mathbf{u} + 0\mathbf{u}$. Add $-0\mathbf{u}$ to both sides:
>
> $$
> \begin{aligned}
> 0\mathbf{u} + (-0\mathbf{u}) &= [0\mathbf{u} + 0\mathbf{u}] + (-0\mathbf{u}) \\
> 0\mathbf{u} + (-0\mathbf{u}) &= 0\mathbf{u} + [0\mathbf{u} + (-0\mathbf{u})] && \text{by Axiom 3} \\
> \mathbf{0} &= 0\mathbf{u} + \mathbf{0} && \text{by Axiom 5} \\
> \mathbf{0} &= 0\mathbf{u} && \text{by Axiom 4.}
> \end{aligned}
> $$
>
> **(2)** By Axioms 4 and 7, $c\mathbf{0} = c(\mathbf{0} + \mathbf{0}) = c\mathbf{0} + c\mathbf{0}$; adding $-c\mathbf{0}$ to both sides exactly as in (1) gives $\mathbf{0} = c\mathbf{0}$.
>
> **(3)** By Axioms 10 and 8 and equation (1),
>
> $$
> \mathbf{u} + (-1)\mathbf{u} = 1\mathbf{u} + (-1)\mathbf{u} = (1 + (-1))\mathbf{u} = 0\mathbf{u} = \mathbf{0} .
> $$
>
> So $(-1)\mathbf{u}$ has the property that defines $-\mathbf{u}$, and by the uniqueness of negatives (Proposition §23.1), $(-1)\mathbf{u} = -\mathbf{u}$.

^pf-23-2

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-1|Def. §23.1]], [[§23 Vector Spaces and Subspaces#^prop-23-1|§23.1]]

> [!example] Example §23.1: A Catalogue of Vector Spaces
> **(a) $\mathbb{R}^n$**, $n \ge 1$: the premier example; geometric intuition from $\mathbb{R}^3$ guides the whole chapter. It is **finite dimensional** (lecture L14).
>
> **(b) Arrows.** The set of all arrows (directed line segments) in three-dimensional space, two arrows being equal if they have the same length and point in the same direction. Add by the parallelogram rule; $c\mathbf{v}$ is the arrow $|c|$ times as long as $\mathbf{v}$, in the same direction if $c \ge 0$ and the opposite one otherwise. An arrow of length zero (a point) is the zero vector, and the negative of $\mathbf{v}$ is $(-1)\mathbf{v}$. Axioms 1, 4, 5, 6 and 10 are evident; the others are verified by geometry (for instance, Axiom 2 is the parallelogram, and Axiom 3 is the two ways of adding three arrows head to tail). No coordinate system is involved. This is the common model for forces in physics.
>
> **(c) Signals.** $\mathbb{S}$ is the space of all doubly infinite sequences of numbers $\{y_k\} = (\ldots, y_{-2}, y_{-1}, y_0, y_1, y_2, \ldots)$, added and scaled term by term: $\{y_k\} + \{z_k\} = \{y_k + z_k\}$, $c\{y_k\} = \{cy_k\}$. The axioms are verified as for $\mathbb{R}^n$. A signal measured (sampled) at discrete times is such a sequence; Lay calls $\mathbb{S}$ the space of discrete-time **signals**. The lecture uses the one-sided version $\mathbb{R}^\infty$ of sequences $(a_1, a_2, a_3, \ldots)$.
>
> **(d) $\mathbb{P}_n$**, $n \ge 0$: the polynomials of degree at most $n$,
>
> $$
> \mathbf{p}(t) = a_0 + a_1t + a_2t^2 + \cdots + a_nt^n , \qquad (4)
> $$
>
> with real coefficients $a_0, \ldots, a_n$ and real variable $t$. The **degree** of $\mathbf{p}$ is the highest power of $t$ with nonzero coefficient; if $\mathbf{p}(t) = a_0 \ne 0$ the degree is $0$; if all coefficients are zero, $\mathbf{p}$ is the **zero polynomial**, which belongs to $\mathbb{P}_n$ although its degree is not defined. If $\mathbf{q}(t) = b_0 + b_1t + \cdots + b_nt^n$, then
>
> $$
> (\mathbf{p} + \mathbf{q})(t) = \mathbf{p}(t) + \mathbf{q}(t) = (a_0 + b_0) + (a_1 + b_1)t + \cdots + (a_n + b_n)t^n, \qquad (c\mathbf{p})(t) = ca_0 + (ca_1)t + \cdots + (ca_n)t^n .
> $$
>
> Both have degree at most $n$, so Axioms 1 and 6 hold. Axioms 2, 3 and 7–10 follow from properties of the real numbers, the zero polynomial is the zero vector (Axiom 4), and $(-1)\mathbf{p}$ is the negative of $\mathbf{p}$ (Axiom 5). So $\mathbb{P}_n$ is a vector space. The set $\mathbb{P}$ of *all* polynomials is one too.
>
> **(e) Functions.** The set $V$ of all real-valued functions on a set $\mathbb{D}$ (typically $\mathbb{R}$ or an interval), with $(\mathbf{f} + \mathbf{g})(t) = \mathbf{f}(t) + \mathbf{g}(t)$ and $(c\mathbf{f})(t) = c\,\mathbf{f}(t)$. For instance, if $\mathbf{f}(t) = 1 + \sin 2t$ and $\mathbf{g}(t) = 2 + .5t$, then $(\mathbf{f} + \mathbf{g})(t) = 3 + \sin 2t + .5t$ and $(2\mathbf{g})(t) = 4 + t$. Two functions are equal when their values agree for every $t$ in $\mathbb{D}$; the zero vector is the function that is identically zero, and the negative of $\mathbf{f}$ is $(-1)\mathbf{f}$. Inside it the lecture singles out $C(\mathbb{R})$, the continuous functions on $\mathbb{R}$ (such as $|x|$, $x^3$, $\sin x \cdot e^{x+3}$), and $C^\infty(\mathbb{R})$, the functions with derivatives of all orders (such as $(\sin x)^3 + e^{x^3}(\sin x)^4$; but not $|x|$).
>
> **(f) Matrices.** For fixed $m$ and $n$, the set $M_{m \times n}$ of all $m \times n$ matrices with the usual addition and scalar multiplication ([[§11 Matrix Operations#^def-11-2|Definition §11.2]]); its zero vector is the zero matrix.
>
> *Lay: Examples 4.1.1–4.1.5; 4.1 (text before Exercise 21)*
> *Source: 235 lectures L13, L14*

^ex-23-1

> [!remark] Remark: A Function Is One Vector
> In the space of functions, each function is a single object, one "point" of the space; the sum $\mathbf{f} + \mathbf{g}$ can be pictured as the fourth vertex of a parallelogram with vertices $\mathbf{0}$, $\mathbf{f}$, $\mathbf{g}$, as in $\mathbb{R}^2$. Thinking this way carries the geometric intuition of $\mathbb{R}^n$ over to any vector space.

^rem-23-1

## Subspaces

> [!definition] Definition §23.2: Subspace
> A **subspace** of a vector space $V$ is a subset $H$ of $V$ that has three properties:
>
> a. The zero vector of $V$ is in $H$.
>
> b. $H$ is closed under vector addition: for each $\mathbf{u}$ and $\mathbf{v}$ in $H$, the sum $\mathbf{u} + \mathbf{v}$ is in $H$.
>
> c. $H$ is closed under multiplication by scalars: for each $\mathbf{u}$ in $H$ and each scalar $c$, the vector $c\mathbf{u}$ is in $H$.
>
> Some texts (and the lectures) replace (a) by the assumption that $H$ is nonempty; then (a) follows from (c) and $0\mathbf{u} = \mathbf{0}$. But the best way to test for a subspace is to look first for the zero vector: if $\mathbf{0}$ is not in $H$, then $H$ is not a subspace and nothing else needs checking.
>
> *Lay: 4.1, Definition and footnote 2*

^def-23-2

> [!remark]- Connections
> - Rigorous treatment: [[§3 Subspaces#^ladr-1-34|LADR 1.34]] (the same three conditions, with Axiom-by-Axiom proof that they suffice); [[§1 Linear Spaces#^def-1-2|556 Def. §1.2]]. For subspaces of $\mathbb{R}^n$ this is [[§18 Subspaces of ℝⁿ#^def-18-1|Definition §18.1]] (2.8).

> [!theorem] Proposition §23.3: A Subspace Is a Vector Space
> Every subspace $H$ of a vector space $V$ is itself a vector space, under the vector space operations already defined in $V$. Conversely, every vector space is a subspace of itself (and possibly of other, larger spaces).
>
> *Lay: 4.1 (text)*

^prop-23-3

> [!proof]+ Proof
> Properties (a), (b), (c) of Definition §23.2 are Axioms 4, 1 and 6 for $H$. Axioms 2, 3 and 7–10 hold in $H$ automatically, because they hold for all elements of $V$, including those in $H$. Axiom 5 also holds in $H$: if $\mathbf{u}$ is in $H$, then $(-1)\mathbf{u}$ is in $H$ by property (c), and $(-1)\mathbf{u} = -\mathbf{u}$ by equation (3) of Proposition §23.2. For the converse, $V$ contains $\mathbf{0}$ and is closed under its own operations by Axioms 1, 4, 6.

^pf-23-3

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-1|Def. §23.1]], [[§23 Vector Spaces and Subspaces#^def-23-2|Def. §23.2]], [[§23 Vector Spaces and Subspaces#^prop-23-2|§23.2]]

The term *subspace* is used when at least two vector spaces are in mind, one inside the other; "subspace of $V$" identifies $V$ as the larger space.

> [!example] Example §23.2: Subspaces
> **(a) The zero subspace.** The set $\{\mathbf{0}\}$ consisting only of the zero vector of $V$ is a subspace: $\mathbf{0} + \mathbf{0} = \mathbf{0}$ and $c\mathbf{0} = \mathbf{0}$ (Proposition §23.2). It is written $\{\mathbf{0}\}$. At the other extreme, $V$ is a subspace of itself.
>
> **(b) Polynomials and smooth functions.** $\mathbb{P}$ is a subspace of the space of all real-valued functions on $\mathbb{R}$, and for each $n \ge 0$, $\mathbb{P}_n$ is a subspace of $\mathbb{P}$: it contains the zero polynomial, and sums and scalar multiples of polynomials of degree at most $n$ again have degree at most $n$. The lecture's chain is
>
> $$
> \mathbb{P}_n \subset \mathbb{P} \subset C^\infty(\mathbb{R}) \subset C(\mathbb{R}) ,
> $$
>
> each a subspace of the next (sums and multiples of differentiable, or continuous, functions are differentiable, or continuous).
>
> **(c) A copy of $\mathbb{R}^2$ inside $\mathbb{R}^3$.** $\mathbb{R}^2$ is *not* a subspace of $\mathbb{R}^3$: it is not even a subset, since vectors in $\mathbb{R}^3$ have three entries. But
>
> $$
> H = \left\{ \begin{bmatrix} s \\ t \\ 0 \end{bmatrix} : s, t \in \mathbb{R} \right\}
> $$
>
> (the $x_1x_2$-plane) is a subspace of $\mathbb{R}^3$ that "looks" and "acts" like $\mathbb{R}^2$: the zero vector is in $H$, and sums and scalar multiples of vectors with third entry $0$ have third entry $0$.
>
> **(d) Symmetric matrices.** A square matrix is symmetric if $A^T = A$. The set $S$ of symmetric $3 \times 3$ matrices is a subspace of $M_{3 \times 3}$: $\mathbf{0}^T = \mathbf{0}$; if $A^T = A$ and $B^T = B$ then $(A + B)^T = A^T + B^T = A + B$; and $(cA)^T = cA^T = cA$.
>
> **(e) Sequences.** In the space $\mathbb{R}^\infty$ of sequences, the convergent sequences form a subspace, since $\lim(a_n + b_n) = \lim a_n + \lim b_n$ and $\lim ca_n = c\lim a_n$ when the limits exist. So do the "Fibonacci-type" sequences, those with
>
> $$
> x_{n+1} = x_n + x_{n-1} \quad \text{for all } n \ge 2 :
> $$
>
> the zero sequence satisfies the recursion, and if $(x_n)$ and $(y_n)$ do, then $x_{n+1} + y_{n+1} = (x_n + y_n) + (x_{n-1} + y_{n-1})$ and $cx_{n+1} = cx_n + cx_{n-1}$. The Fibonacci sequence $1, 1, 2, 3, 5, 8, \ldots$ is one element. The lecture asks which geometric sequences $(\lambda, \lambda^2, \lambda^3, \ldots)$ belong to this subspace: the recursion becomes $\lambda^{n-1}(\lambda^2 - \lambda - 1) = 0$, so for $\lambda \ne 0$ exactly the two roots $\lambda = (1 \pm \sqrt5)/2$ of $\lambda^2 = \lambda + 1$ work. ([[§26 Coordinate Systems#^ex-26-3|Example §26.3]](c) identifies this subspace with $\mathbb{R}^2$, and [[§30 Applications to Difference Equations#^ex-30-4|Example §30.4]] writes every Fibonacci-type sequence as a combination of these two geometric sequences, which gives the closed formula for the Fibonacci numbers.)
>
> *Lay: Examples 4.1.6–4.1.8; Practice Problem 3 (4.1)*
> *Source: 235 lectures L13, L14*

^ex-23-2

> [!example] Example §23.3: Sets That Are Not Subspaces
> **(a) Missing the origin.** A plane in $\mathbb{R}^3$ not through the origin is not a subspace of $\mathbb{R}^3$, because it does not contain the zero vector; likewise a line in $\mathbb{R}^2$ not through the origin is not a subspace of $\mathbb{R}^2$. For instance, $H = \{(3s, 2 + 5s) : s \in \mathbb{R}\}$ is such a line. It also fails (c): $\mathbf{u} = (3, 7)$ is in $H$ ($s = 1$), but $2\mathbf{u} = (6, 14)$ would need $3s = 6$ and $2 + 5s = 14$, that is, $s = 2$ and $s = 12/5$, which is impossible.
>
> **(b) The first quadrant** $V = \{(x, y) : x \ge 0,\ y \ge 0\}$ contains $\mathbf{0}$ and is closed under addition, but not under scalar multiplication: if $\mathbf{v} = (x, y) \ne \mathbf{0}$ is in $V$, then $-\mathbf{v} = (-1)\mathbf{v}$ is not.
>
> **(c) The two axes** $V = \{(x, y) : xy = 0\}$ contain $\mathbf{0}$ and are closed under scalar multiplication ($c(x, 0) = (cx, 0)$), but not under addition: $(2, 0)$ and $(0, 3)$ are in $V$, while $(2, 0) + (0, 3) = (2, 3)$ is not.
>
> **(d) A parabola** $V = \{(x, y) : y^2 = x\}$ contains $\mathbf{0}$ but is not closed under scaling: $(1, 1)$ is in $V$ but $2(1, 1) = (2, 2)$ is not ($4 \ne 2$).
>
> The lecture's moral: subspaces are cut out by *linear* (homogeneous) conditions. Inequalities or nonlinear conditions in the description of a set are a reason to suspect it is not a subspace.
>
> *Lay: Example 4.1.9; Practice Problem 1 (4.1)*
> *Source: 235 lecture L10*

^ex-23-3

## A Subspace Spanned by a Set

As in Chapter 1, a **linear combination** of $\mathbf{v}_1, \ldots, \mathbf{v}_p$ is any sum of scalar multiples $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$, and $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is the set of all such linear combinations ([[§3 Vector Equations#^def-3-3|Definition §3.3]], [[§3 Vector Equations#^def-3-4|Definition §3.4]]).

> [!theorem] Theorem §23.4: A Span Is a Subspace
> If $\mathbf{v}_1, \ldots, \mathbf{v}_p$ are in a vector space $V$, then $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is a subspace of $V$. It is the smallest subspace containing $\mathbf{v}_1, \ldots, \mathbf{v}_p$: every subspace of $V$ that contains $\mathbf{v}_1, \ldots, \mathbf{v}_p$ also contains their span.
>
> *Lay: Theorem 1 (4.1); Exercise 31*

^thm-23-4

> [!proof]+ Proof
> *Lay proves the case $p = 2$ (Example 4.1.10) and says it "can easily be generalized".* Let $H = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$.
>
> **(a)** $\mathbf{0} = 0\mathbf{v}_1 + \cdots + 0\mathbf{v}_p$ (Proposition §23.2(1) and Axiom 4), so $\mathbf{0}$ is in $H$.
>
> **(b)** Take two vectors of $H$, $\mathbf{u} = s_1\mathbf{v}_1 + \cdots + s_p\mathbf{v}_p$ and $\mathbf{w} = t_1\mathbf{v}_1 + \cdots + t_p\mathbf{v}_p$. By Axioms 2, 3 and 8,
>
> $$
> \mathbf{u} + \mathbf{w} = (s_1\mathbf{v}_1 + \cdots + s_p\mathbf{v}_p) + (t_1\mathbf{v}_1 + \cdots + t_p\mathbf{v}_p) = (s_1 + t_1)\mathbf{v}_1 + \cdots + (s_p + t_p)\mathbf{v}_p ,
> $$
>
> so $\mathbf{u} + \mathbf{w}$ is in $H$.
>
> **(c)** For a scalar $c$, by Axioms 7 and 9,
>
> $$
> c\mathbf{u} = c(s_1\mathbf{v}_1 + \cdots + s_p\mathbf{v}_p) = (cs_1)\mathbf{v}_1 + \cdots + (cs_p)\mathbf{v}_p ,
> $$
>
> so $c\mathbf{u}$ is in $H$. Thus $H$ is a subspace of $V$.
>
> **Smallest.** If a subspace $K$ contains $\mathbf{v}_1, \ldots, \mathbf{v}_p$, it contains each $c_i\mathbf{v}_i$ by closure under scalar multiplication, and then the sum $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$ by closure under addition (applied $p - 1$ times). So $H \subseteq K$.

^pf-23-4

*Uses:* [[§23 Vector Spaces and Subspaces#^def-23-1|Def. §23.1]], [[§23 Vector Spaces and Subspaces#^def-23-2|Def. §23.2]], [[§23 Vector Spaces and Subspaces#^prop-23-2|§23.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§4 Span and Linear Independence#^ladr-2-6|LADR 2.6]] (the span is the smallest subspace containing the list); [[§1 Linear Spaces#^prop-1-4|556 Prop. §1.4]], [[§1 Linear Spaces#^prop-1-5|556 Prop. §1.5]], where spans of infinite sets are taken as well, still with finite linear combinations.

> [!definition] Definition §23.3: Subspace Spanned by a Set; Spanning Set
> $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is called **the subspace spanned** (or **generated**) by $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$. Given any subspace $H$ of $V$, a **spanning** (or **generating**) **set** for $H$ is a set $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in $H$ such that $H = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$.
>
> Each $\mathbf{v}_k$ belongs to $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$, since $\mathbf{v}_k = 0\mathbf{v}_1 + \cdots + 1\mathbf{v}_k + \cdots + 0\mathbf{v}_p$ (Practice Problem 2). The vectors of a spanning set are "handles" on $H$: computations with the infinitely many vectors of $H$ reduce to computations with finitely many.
>
> *Lay: 4.1 (text)*

^def-23-3

In $\mathbb{R}^3$, every nonzero subspace other than $\mathbb{R}^3$ itself is either $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ for linearly independent $\mathbf{v}_1, \mathbf{v}_2$ (a plane through the origin) or $\operatorname{Span}\{\mathbf{v}\}$ for $\mathbf{v} \ne \mathbf{0}$ (a line through the origin); this is proved in [[§27 The Dimension of a Vector Space#^ex-27-3|Example §27.3]] (4.5). The lecture's list: the subspaces of $\mathbb{R}^2$ are $\{\mathbf{0}\}$, the lines through the origin, and $\mathbb{R}^2$; those of $\mathbb{R}^3$ are $\{\mathbf{0}\}$, lines and planes through the origin, and $\mathbb{R}^3$.

> [!example] Example §23.4: Finding a Spanning Set
> **(a)** Let $H = \{(a - 3b,\ b - a,\ a,\ b) : a, b \in \mathbb{R}\}$. Show that $H$ is a subspace of $\mathbb{R}^4$.
>
> Write the vectors of $H$ as columns and split by the parameters:
>
> $$
> \begin{bmatrix} a - 3b \\ b - a \\ a \\ b \end{bmatrix} = a\begin{bmatrix} 1 \\ -1 \\ 1 \\ 0 \end{bmatrix} + b\begin{bmatrix} -3 \\ 1 \\ 0 \\ 1 \end{bmatrix} = a\mathbf{v}_1 + b\mathbf{v}_2 .
> $$
>
> So $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$, a subspace of $\mathbb{R}^4$ by Theorem §23.4, with spanning set $\{\mathbf{v}_1, \mathbf{v}_2\}$.
>
> **(b)** For what values of $h$ is $\mathbf{y} = (-4, 3, h)$ in the subspace of $\mathbb{R}^3$ spanned by $\mathbf{v}_1 = (1, -1, -2)$, $\mathbf{v}_2 = (5, -4, -7)$, $\mathbf{v}_3 = (-3, 1, 0)$?
>
> This asks whether $x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + x_3\mathbf{v}_3 = \mathbf{y}$ is consistent. Row reduce ($R_2 + R_1$, $R_3 + 2R_1$, then $R_3 - 3R_2$):
>
> $$
> \begin{bmatrix} 1 & 5 & -3 & -4 \\ -1 & -4 & 1 & 3 \\ -2 & -7 & 0 & h \end{bmatrix} \sim \begin{bmatrix} 1 & 5 & -3 & -4 \\ 0 & 1 & -2 & -1 \\ 0 & 3 & -6 & h - 8 \end{bmatrix} \sim \begin{bmatrix} 1 & 5 & -3 & -4 \\ 0 & 1 & -2 & -1 \\ 0 & 0 & 0 & h - 5 \end{bmatrix} .
> $$
>
> The system is consistent if and only if $h = 5$, so $\mathbf{y}$ is in $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ exactly when $h = 5$.
>
> *Lay: Examples 4.1.11 and 4.1.12*

^ex-23-4

> [!remark] Remark: Method — Is H a Subspace?
> 1. **Zero vector.** Check whether $\mathbf{0} \in H$. If not, $H$ is not a subspace; stop.
> 2. **Parametric description.** If $H$ is given by parameters, $H = \{a\mathbf{v}_1 + b\mathbf{v}_2 + \cdots\}$, then $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \ldots\}$ is a subspace (Theorem §23.4), and the $\mathbf{v}_i$ form a spanning set (Example §23.4(a)).
> 3. **Homogeneous equations.** If $H$ is the set of solutions of homogeneous linear equations, then $H = \operatorname{Nul} A$ is a subspace ([[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-1|Theorem §24.1]]); solving the equations gives a spanning set.
> 4. **Directly.** Otherwise check closure under addition and scalar multiplication from Definition §23.2.
> 5. **To disprove**, give one specific counterexample: two vectors of $H$ whose sum is not in $H$, or one vector and one scalar (Example §23.3).

^rem-23-2
