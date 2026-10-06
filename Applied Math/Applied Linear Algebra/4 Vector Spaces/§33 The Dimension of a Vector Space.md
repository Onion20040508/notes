---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 33
lay: "4.5"
aliases: ["Lay 4.5"]
tags: [applied-linear-algebra, math235]
---
← [[§32 Coordinate Systems]] · ↑ [[· 4 Vector Spaces]] · [[§34 Rank]] →

*Lay, Section 4.5 · MATH 235 lecture L16.*

A vector space with a basis of $n$ vectors is isomorphic to $\mathbb{R}^n$ through the coordinate mapping ([[§32 Coordinate Systems#^thm-32-3|Theorem §32.3]]). This section shows that the number $n$ does not depend on the basis chosen, so it is a property of the space itself: its dimension. Dimension controls the size of linearly independent sets (at most $n$ vectors) and of spanning sets (at least $n$ vectors), and when a set has exactly $n$ vectors, one of the two properties gives the other for free (the Basis Theorem). For a matrix, $\dim \operatorname{Nul} A$ and $\dim \operatorname{Col} A$ are read off an echelon form. (The instructor's checklist for "Section 4.5" follows the 6th edition, where this section also contains the row space, the Rank Theorem and the Invertible Matrix Theorem; in the 5th edition those are in Section 4.6, [[§34 Rank|§34]].)

## Dimension

> [!theorem] Theorem §41.1: More Vectors Than the Basis Means Dependence
> If a vector space $V$ has a basis $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$, then any set in $V$ containing more than $n$ vectors must be linearly dependent.
>
> Equivalently: every linearly independent set in $V$ has at most $n$ vectors. The theorem also holds for infinite sets $S$ (an infinite set is called linearly dependent if some finite subset is): any $p > n$ vectors of $S$ form a dependent subset.
>
> *Lay: Theorem 9 (4.5)*

^thm-33-1

> [!proof]+ Proof
> Let $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ be a set in $V$ with $p > n$. The coordinate vectors $[\mathbf{u}_1]_{\mathcal B}, \ldots, [\mathbf{u}_p]_{\mathcal B}$ are $p$ vectors in $\mathbb{R}^n$, more vectors than entries, so they are linearly dependent ([[§8 Linear Independence#^thm-8-6|Theorem §8.6]]). So there are scalars $c_1, \ldots, c_p$, not all zero, with
>
> $$
> c_1 [\mathbf{u}_1]_{\mathcal B} + \cdots + c_p [\mathbf{u}_p]_{\mathcal B} = \mathbf{0} \in \mathbb{R}^n .
> $$
>
> The coordinate mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ is linear ([[§32 Coordinate Systems#^thm-32-3|Theorem §32.3]]), so the left side is $[c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p]_{\mathcal B}$. A vector whose $\mathcal{B}$-coordinates are all $0$ is $0 \cdot \mathbf{b}_1 + \cdots + 0 \cdot \mathbf{b}_n = \mathbf{0}$. Hence
>
> $$
> c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p = \mathbf{0}
> $$
>
> with the $c_i$ not all zero, and $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is linearly dependent.

^pf-33-1

*Uses:* [[§8 Linear Independence#^thm-8-6|§8.6]], [[§32 Coordinate Systems#^thm-32-3|§32.3]]

> [!theorem] Theorem §41.2: All Bases Have the Same Size
> If a vector space $V$ has a basis of $n$ vectors, then every basis of $V$ must consist of exactly $n$ vectors.
>
> *Lay: Theorem 10 (4.5)*

^thm-33-2

> [!proof]+ Proof
> Let $\mathcal{B}_1$ be a basis of $n$ vectors and $\mathcal{B}_2$ any other basis of $V$. Since $\mathcal{B}_1$ is a basis and $\mathcal{B}_2$ is linearly independent, $\mathcal{B}_2$ has no more than $n$ vectors, by [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]]. Since $\mathcal{B}_2$ is a basis and $\mathcal{B}_1$ is linearly independent, [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]] applied with the roles exchanged shows that $\mathcal{B}_1$ has no more vectors than $\mathcal{B}_2$, so $\mathcal{B}_2$ has at least $n$ vectors. Thus $\mathcal{B}_2$ has exactly $n$ vectors.

^pf-33-2

*Uses:* [[§33 The Dimension of a Vector Space#^thm-33-1|§33.1]]

If a nonzero vector space $V$ is spanned by a finite set $S$, then some subset of $S$ is a basis of $V$, by the Spanning Set Theorem ([[§31 Linearly Independent Sets; Bases#^thm-31-2|Theorem §31.2]]). By [[§33 The Dimension of a Vector Space#^thm-33-2|Theorem §33.2]] all such bases have the same size, so the following definition makes sense.

> [!definition] Definition §41.1: Finite-Dimensional; Dimension
> If $V$ is spanned by a finite set, then $V$ is **finite-dimensional**, and the **dimension** of $V$, written $\dim V$, is the number of vectors in a basis for $V$. The dimension of the zero vector space $\{\mathbf{0}\}$ is defined to be $0$. If $V$ is not spanned by a finite set, then $V$ is **infinite-dimensional**.
>
> *Lay: 4.5, Definition*

^def-33-1

> [!remark]- Connections
> - Rigorous treatment: [[§6 Dimension#^ladr-2-34|LADR 2.34]] (basis length does not depend on basis) and [[§6 Dimension#^ladr-2-35|LADR 2.35]]. Axler proves [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]] without coordinates, from [[§4 Span and Linear Independence#^ladr-2-22|LADR 2.22]] (a linearly independent list is never longer than a spanning list), by trading spanning vectors for independent ones; infinite-dimensional spaces: [[§4 Span and Linear Independence#^ladr-2-13|LADR 2.13]].

> [!example] Example §41.1: Dimensions of the Standard Spaces
> **$\mathbb{R}^n$.** The standard basis $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ has $n$ vectors, so $\dim \mathbb{R}^n = n$. (L16: "any basis of $\mathbb{R}^4$ has exactly $4$ vectors.")
>
> **$\mathbb{P}_n$.** The standard basis $\{1, t, \ldots, t^n\}$ has $n + 1$ vectors, so $\dim \mathbb{P}_n = n + 1$; for instance $\dim \mathbb{P}_2 = 3$.
>
> **$\mathbb{P}$, all polynomials, is infinite-dimensional.** Suppose $\mathbb{P}$ were spanned by finitely many polynomials $p_1, \ldots, p_k$, and let $d$ be the largest of their degrees. Every linear combination of $p_1, \ldots, p_k$ has degree at most $d$, so $t^{d+1}$ is not in their span, a contradiction. (Lay leaves this as Exercise 27.)
>
> **A plane in $\mathbb{R}^3$.** For $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ with $\mathbf{v}_1 = (3, 6, 2)$ and $\mathbf{v}_2 = (-1, 0, 1)$, the two vectors are not multiples of each other, hence linearly independent, so they form a basis of $H$ and $\dim H = 2$.
>
> *Lay: Examples 4.5.1 and 4.5.2*
> *Source: 235 lecture L16*

^ex-33-1

> [!example] Example §41.2: Finding the Dimension of a Subspace
> Find the dimension of
>
> $$
> H = \left\{ \begin{bmatrix} a - 3b + 6c \\ 5a + 4d \\ b - 2c - d \\ 5d \end{bmatrix} : a, b, c, d \text{ in } \mathbb{R} \right\} .
> $$
>
> **A spanning set.** Splitting the vector by parameters, $H$ is the set of all linear combinations $a\mathbf{v}_1 + b\mathbf{v}_2 + c\mathbf{v}_3 + d\mathbf{v}_4$ of
>
> $$
> \mathbf{v}_1 = \begin{bmatrix} 1 \\ 5 \\ 0 \\ 0 \end{bmatrix}, \quad
> \mathbf{v}_2 = \begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \quad
> \mathbf{v}_3 = \begin{bmatrix} 6 \\ 0 \\ -2 \\ 0 \end{bmatrix}, \quad
> \mathbf{v}_4 = \begin{bmatrix} 0 \\ 4 \\ -1 \\ 5 \end{bmatrix} .
> $$
>
> **Shrink it to a basis.** $\mathbf{v}_1 \ne \mathbf{0}$; $\mathbf{v}_2$ is not a multiple of $\mathbf{v}_1$ (its first two entries $-3, 0$ are not proportional to $1, 5$); but $\mathbf{v}_3 = -2\mathbf{v}_2$. By the Spanning Set Theorem we may discard $\mathbf{v}_3$, and $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_4\}$ still spans $H$. Finally, $\mathbf{v}_4$ is not a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$, since its fourth entry is $5$ while theirs are $0$. No vector of $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_4\}$ is a linear combination of the ones before it, so the set is linearly independent ([[§31 Linearly Independent Sets; Bases#^thm-31-1|Theorem §31.1]]) and is a basis for $H$. Thus $\dim H = 3$.
>
> (Check by row reduction: the matrix $[\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3\ \mathbf{v}_4]$ has reduced echelon form with pivots in columns $1, 2, 4$.)
>
> *Lay: Example 4.5.3*

^ex-33-2

> [!example] Example §41.3: The Subspaces of ℝ³ by Dimension
> By [[§33 The Dimension of a Vector Space#^thm-33-3|Theorem §33.3]] below, a subspace $H$ of $\mathbb{R}^3$ has $\dim H \in \{0, 1, 2, 3\}$.
> - **0-dimensional:** only the zero subspace $\{\mathbf{0}\}$.
> - **1-dimensional:** a basis is one nonzero vector $\mathbf{v}$, so $H = \operatorname{Span}\{\mathbf{v}\}$, a line through the origin.
> - **2-dimensional:** $H = \operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$ with $\mathbf{u}, \mathbf{v}$ linearly independent: a plane through the origin.
> - **3-dimensional:** only $\mathbb{R}^3$ itself. Three linearly independent vectors in $\mathbb{R}^3$ span $\mathbb{R}^3$, by the Invertible Matrix Theorem ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]); see also [[§33 The Dimension of a Vector Space#^cor-33-6|Corollary §33.6]].
>
> *Lay: Example 4.5.4*

^ex-33-3

![[m235-27-1.svg]]
*The subspaces of $\mathbb{R}^3$, sorted by dimension: the origin (dimension $0$), lines through the origin (dimension $1$, red), planes through the origin (dimension $2$, blue), and $\mathbb{R}^3$ itself (dimension $3$). A line or plane that misses the origin is not a subspace.*

## Subspaces of a Finite-Dimensional Space

The next theorem is the counterpart of the Spanning Set Theorem: a spanning set can be shrunk to a basis, and a linearly independent set can be enlarged to one.

> [!theorem] Theorem §41.3: Extending to a Basis; Dimension of a Subspace
> Let $H$ be a subspace of a finite-dimensional vector space $V$. Any linearly independent set in $H$ can be expanded, if necessary, to a basis for $H$. Also, $H$ is finite-dimensional and
>
> $$
> \dim H \le \dim V .
> $$
>
> *Lay: Theorem 11 (4.5)*

^thm-33-3

> [!proof]+ Proof
> If $H = \{\mathbf{0}\}$, then $\dim H = 0 \le \dim V$. Otherwise let $S = \{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ be any linearly independent set in $H$ (for instance one nonzero vector of $H$). If $S$ spans $H$, then $S$ is a basis for $H$.
>
> Otherwise there is some $\mathbf{u}_{k+1}$ in $H$ that is not in $\operatorname{Span} S$. Then $\{\mathbf{u}_1, \ldots, \mathbf{u}_k, \mathbf{u}_{k+1}\}$ is linearly independent: no vector in it is a linear combination of the vectors before it ([[§31 Linearly Independent Sets; Bases#^thm-31-1|Theorem §31.1]]), since $\mathbf{u}_1, \ldots, \mathbf{u}_k$ are independent and $\mathbf{u}_{k+1} \notin \operatorname{Span} S$. (Lecture L16 checks this directly. Suppose $c_1\mathbf{u}_1 + \cdots + c_{k+1}\mathbf{u}_{k+1} = \mathbf{0}$. If $c_{k+1} \ne 0$, then $\mathbf{u}_{k+1} = -\frac{c_1}{c_{k+1}}\mathbf{u}_1 - \cdots - \frac{c_k}{c_{k+1}}\mathbf{u}_k$ lies in $\operatorname{Span} S$, a contradiction. So $c_{k+1} = 0$, and then $c_1\mathbf{u}_1 + \cdots + c_k\mathbf{u}_k = \mathbf{0}$ forces $c_1 = \cdots = c_k = 0$.)
>
> So long as the new set does not span $H$, repeat: each step produces a larger linearly independent set in $H \subseteq V$. By [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]] a linearly independent set in $V$ has at most $\dim V$ vectors, so the process stops after at most $\dim V - k$ steps. When it stops, the expanded set spans $H$, hence is a basis for $H$ with at most $\dim V$ vectors: $H$ is finite-dimensional and $\dim H \le \dim V$.

^pf-33-3

*Uses:* [[§33 The Dimension of a Vector Space#^thm-33-1|§33.1]], [[§31 Linearly Independent Sets; Bases#^thm-31-1|§31.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§5 Bases#^ladr-2-32|LADR 2.32]] (every linearly independent list extends to a basis; Axler adjoins vectors of a spanning list of $V$, so the process visibly stops) and [[§6 Dimension#^ladr-2-37|LADR 2.37]] (dimension of a subspace).

> [!theorem] Corollary §41.4: Independent Sets and Spanning Sets in an n-Dimensional Space
> Let $\dim V = n$.
> 1. A linearly independent set in $V$ has at most $n$ vectors.
> 2. A set that spans $V$ has at least $n$ vectors.
>
> So a set with fewer than $n$ vectors cannot span $V$, and a set with more than $n$ vectors is linearly dependent.
>
> *Lay: 4.5 (text after Theorem 9); Practice Problem 1 and Exercise 25*

^cor-33-4

> [!proof]+ Proof
> 1 is [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]]. For 2, let $S$ span $V$. If $V = \{\mathbf{0}\}$ there is nothing to prove ($n = 0$). Otherwise, by the Spanning Set Theorem ([[§31 Linearly Independent Sets; Bases#^thm-31-2|Theorem §31.2]]) some subset $S'$ of $S$ is a basis of $V$, and $S'$ has exactly $n$ vectors by [[§33 The Dimension of a Vector Space#^thm-33-2|Theorem §33.2]]. So $S$ has at least $n$ vectors.

^pf-33-4

*Uses:* [[§33 The Dimension of a Vector Space#^thm-33-1|§33.1]], [[§33 The Dimension of a Vector Space#^thm-33-2|§33.2]], [[§31 Linearly Independent Sets; Bases#^thm-31-2|§31.2]]

When the dimension is known, the search for a basis is simplified: with the right number of vectors, it is enough to check *either* independence *or* spanning. This matters in applications (difference equations, [[§37 Solution Sets of Linear Difference Equations#^ex-37-1|Example §37.1]]; differential equations) where independence is much easier to verify than spanning.

> [!theorem] Theorem §41.5: The Basis Theorem
> Let $V$ be a $p$-dimensional vector space, $p \ge 1$. Any linearly independent set of exactly $p$ elements in $V$ is automatically a basis for $V$. Any set of exactly $p$ elements that spans $V$ is automatically a basis for $V$.
>
> *Lay: Theorem 12 (4.5)*

^thm-33-5

> [!proof]+ Proof
> **Independent sets.** By [[§33 The Dimension of a Vector Space#^thm-33-3|Theorem §33.3]] (with $H = V$), a linearly independent set $S$ of $p$ elements can be extended to a basis for $V$. That basis must contain exactly $p$ elements, since $\dim V = p$ ([[§33 The Dimension of a Vector Space#^thm-33-2|Theorem §33.2]]). So nothing was added: $S$ is already a basis for $V$.
>
> **Spanning sets.** Suppose $S$ has $p$ elements and spans $V$. Since $V$ is nonzero, the Spanning Set Theorem gives a subset $S'$ of $S$ that is a basis of $V$. Since $\dim V = p$, $S'$ contains $p$ vectors, so $S' = S$ and $S$ is a basis.

^pf-33-5

*Uses:* [[§33 The Dimension of a Vector Space#^thm-33-3|§33.3]], [[§33 The Dimension of a Vector Space#^thm-33-2|§33.2]], [[§31 Linearly Independent Sets; Bases#^thm-31-2|§31.2]]

Lay states the Basis Theorem for subspaces of $\mathbb{R}^n$ already in Section 2.9 ([[§22 Dimension and Rank|§22]], Theorem 15) and defers its proof to this section; the proof above covers that case, with $V = H$.

> [!remark]- Connections
> - Rigorous treatment: [[§6 Dimension#^ladr-2-38|LADR 2.38]] (linearly independent list of the right length is a basis) and [[§6 Dimension#^ladr-2-42|LADR 2.42]] (spanning list of the right length is a basis), the same two arguments.

> [!example] Example §41.4: Three Vectors That Form a Basis of ℝ³
> Show that $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 3 \\ 4 \\ 0 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 5 \\ 6 \\ 7 \end{bmatrix}$ form a basis of $\mathbb{R}^3$.
>
> Since $\dim \mathbb{R}^3 = 3$, by the Basis Theorem it is enough to show that the three vectors are linearly independent; spanning then comes for free. Let $A = [\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3]$. Expanding along the third row (two zeros),
>
> $$
> \det A = \begin{vmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \\ 0 & 0 & 7 \end{vmatrix} = 7 \begin{vmatrix} 1 & 3 \\ 2 & 4 \end{vmatrix} = 7(4 - 6) = -14 \ne 0 .
> $$
>
> So $A$ is invertible and its columns are linearly independent (Invertible Matrix Theorem with determinants, [[§25 Properties of Determinants#^thm-25-4|Theorem §25.4]]). Hence $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is a basis of $\mathbb{R}^3$. (The same three vectors, checked by row reduction instead: [[§22 Dimension and Rank#^ex-22-4|Example §22.4]](a).)
>
> *Source: 235 lecture L16*

^ex-33-4

> [!theorem] Corollary §41.6: A Subspace of Full Dimension Is the Whole Space
> Let $H$ be a subspace of a finite-dimensional vector space $V$. If $\dim H = \dim V$, then $H = V$. In particular, the possible dimensions of subspaces of $\mathbb{R}^n$ are $0, 1, \ldots, n$, and the only $n$-dimensional subspace of $\mathbb{R}^n$ is $\mathbb{R}^n$ itself.
>
> *Lay: 4.5, Exercise 26*

^cor-33-6

> [!proof]+ Proof
> Let $n = \dim H = \dim V$. If $n = 0$, then $H = V = \{\mathbf{0}\}$. Otherwise a basis of $H$ is a linearly independent set of exactly $n$ vectors in $V$, hence a basis of $V$ by the Basis Theorem. So $V = \operatorname{Span}(\text{basis}) = H$. The statement about $\mathbb{R}^n$ follows with [[§33 The Dimension of a Vector Space#^thm-33-3|Theorem §33.3]].

^pf-33-6

*Uses:* [[§33 The Dimension of a Vector Space#^thm-33-5|§33.5]], [[§33 The Dimension of a Vector Space#^thm-33-3|§33.3]]

> [!theorem] Proposition §41.7: Linear Maps and Dimension
> Let $V$ and $W$ be vector spaces, $V$ finite-dimensional, and $T : V \to W$ a linear transformation.
> 1. For a subspace $H$ of $V$, the image $T(H)$ is a subspace of $W$ and $\dim T(H) \le \dim H$.
> 2. If $T$ is one-to-one, then $\dim T(H) = \dim H$. In particular, if $T$ is one-to-one and onto (an isomorphism), then $\dim W = \dim V$: isomorphic finite-dimensional vector spaces have the same dimension.
>
> *Lay: 4.5, Exercises 31 and 32*

^prop-33-7

> [!proof]+ Proof
> $T(H)$ is a subspace: it is the range of the restriction of $T$ to $H$, a linear map $H \to W$, so [[§30 Null Spaces, Column Spaces, and Linear Transformations#^thm-30-5|Theorem §30.5]] applies (this is Lay's Exercise 35 in Section 4.2). Let $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ be a basis of $H$ (if $H = \{\mathbf{0}\}$, then $T(H) = \{\mathbf{0}\}$ and both dimensions are $0$). Every vector of $T(H)$ is $T(c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p) = c_1 T(\mathbf{v}_1) + \cdots + c_p T(\mathbf{v}_p)$, so $T(\mathbf{v}_1), \ldots, T(\mathbf{v}_p)$ span $T(H)$, and $\dim T(H) \le p$ by [[§33 The Dimension of a Vector Space#^cor-33-4|Corollary §33.4]]. This is 1.
>
> For 2, suppose also $c_1 T(\mathbf{v}_1) + \cdots + c_p T(\mathbf{v}_p) = \mathbf{0}$. Then $T(c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p) = \mathbf{0} = T(\mathbf{0})$, and since $T$ is one-to-one, $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p = \mathbf{0}$, so all $c_i = 0$. Thus $T(\mathbf{v}_1), \ldots, T(\mathbf{v}_p)$ is a basis of $T(H)$ and $\dim T(H) = p = \dim H$. With $H = V$ and $T$ onto, $T(V) = W$, so $\dim W = \dim V$.

^pf-33-7

*Uses:* [[§33 The Dimension of a Vector Space#^cor-33-4|§33.4]], [[§30 Null Spaces, Column Spaces, and Linear Transformations#^thm-30-5|§30.5]]


## The Dimensions of Nul A and Col A

The pivot columns of $A$ form a basis for $\operatorname{Col} A$ ([[§31 Linearly Independent Sets; Bases#^thm-31-3|Theorem §31.3]]), so $\dim \operatorname{Col} A$ is known as soon as the pivot columns are. A basis of $\operatorname{Nul} A$ usually takes more work, but its size is just as easy to find.

> [!theorem] Theorem §33.8: Dimensions of Nul A and Col A
> Let $A$ be an $m \times n$ matrix. The dimension of $\operatorname{Nul} A$ is the number of free variables in the equation $A\mathbf{x} = \mathbf{0}$, and the dimension of $\operatorname{Col} A$ is the number of pivot columns in $A$.
>
> *Lay: 4.5 (boxed statement)*

^thm-33-8

> [!proof]+ Proof
> **Col A.** The pivot columns of $A$ form a basis for $\operatorname{Col} A$, so their number is $\dim \operatorname{Col} A$.
>
> **Nul A.** Suppose $A\mathbf{x} = \mathbf{0}$ has $k$ free variables. If $k = 0$, then $\operatorname{Nul} A = \{\mathbf{0}\}$ has dimension $0$. Otherwise, the standard method of Section 4.2 ([[§30 Null Spaces, Column Spaces, and Linear Transformations#^rem-30-1|Remark: Method — A Spanning Set for Nul A]]; see also [[§30 Null Spaces, Column Spaces, and Linear Transformations#^prop-30-2|Proposition §30.2]]) writes the general solution in parametric vector form $\mathbf{x} = x_{j_1}\mathbf{u}_1 + \cdots + x_{j_k}\mathbf{u}_k$, one vector $\mathbf{u}_i$ for each free variable $x_{j_i}$, so $\mathbf{u}_1, \ldots, \mathbf{u}_k$ span $\operatorname{Nul} A$. They are linearly independent: in entry $j_i$, the vector $\mathbf{u}_i$ has a $1$ and every other $\mathbf{u}_l$ has a $0$, so if $c_1\mathbf{u}_1 + \cdots + c_k\mathbf{u}_k = \mathbf{0}$, then entry $j_i$ gives $c_i = 0$. So $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ is a basis for $\operatorname{Nul} A$, and $\dim \operatorname{Nul} A = k$.

^pf-33-8

*Uses:* [[§31 Linearly Independent Sets; Bases#^thm-31-3|§31.3]], [[§30 Null Spaces, Column Spaces, and Linear Transformations#^prop-30-2|§30.2]]

> [!example] Example §33.5: Dimensions of the Null Space and the Column Space
> Find $\dim \operatorname{Nul} A$ and $\dim \operatorname{Col} A$ for
>
> $$
> A = \begin{bmatrix} -3 & 6 & -1 & 1 & -7 \\ 1 & -2 & 2 & 3 & -1 \\ 2 & -4 & 5 & 8 & -4 \end{bmatrix} .
> $$
>
> Row reduce $[A\ \ \mathbf{0}]$. Interchange rows 1 and 2, then add $3 \cdot$(row 1) to row 2 and $-2 \cdot$(row 1) to row 3:
>
> $$
> \begin{bmatrix} 1 & -2 & 2 & 3 & -1 & 0 \\ 0 & 0 & 5 & 10 & -10 & 0 \\ 0 & 0 & 1 & 2 & -2 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -2 & 2 & 3 & -1 & 0 \\ 0 & 0 & 1 & 2 & -2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
> $$
>
> (divide row 2 by $5$, then subtract it from row 3). The pivots are in columns $1$ and $3$, so $x_2, x_4, x_5$ are free. Hence $\dim \operatorname{Nul} A = 3$ and $\dim \operatorname{Col} A = 2$. Note that $3 + 2 = 5$, the number of columns: this is the Rank Theorem of [[§34 Rank#^thm-34-3|§34]].
>
> *Lay: Example 4.5.5*

^ex-33-5
