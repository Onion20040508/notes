---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 64
tags: [group-theory, math493]
---
← [[§63 Invariant Inner Products and Maschke over ℝ]] · ↑ [[· 11 Representations and Maschke's Theorem]] · [[§65 Simple Representations]] →

*Source: Lecture (Fri Nov 6); the MATH 420 slides *Complex inner products*, posted for this course. Reference for the linear algebra: Axler, Linear Algebra Done Right, Ch. 6.*

Over $\mathbb{C}$ the averaging argument of [[§63 Invariant Inner Products and Maschke over ℝ|§63]] needs a replacement for the inner product, because no bilinear form on a nonzero complex vector space is positive definite. This section sets up the replacement: sesquilinear and Hermitian forms, their matrices, orthogonal projection, and orthonormal bases by Gram–Schmidt. With a positive definite Hermitian form in place of the inner product, a finite group acts on a finite-dimensional complex representation by unitary matrices in a suitable basis; this is stated in the remark *Why Not Bilinear, and Unitary Matrices*, and its averaging argument is not written out here.

> [!example] Example §64.1: The Dot Product on $\mathbb{C}^2$
> Bilinear forms and symmetric bilinear forms make sense over $\mathbb{C}$, with the same definitions as over $\mathbb{R}$. The dot product $x \cdot y = x_1 y_1 + x_2 y_2$ on $\mathbb{C}^2$ is one. Two facts from the real case fail for it.
>
> 1. *A line without an orthonormal basis.* $(1, i) \cdot (1, i) = 1 + i^2 = 0$, so every vector of the line $\mathbb{C}(1, i)$ has length $0$: $\lambda(1, i) \cdot \lambda(1, i) = \lambda^2 \cdot 0 = 0$. No vector $u$ of this line has $u \cdot u = 1$.
> 2. *A symmetric matrix that is not diagonalizable.* The matrix $A = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ satisfies $A^{\mathsf{T}} = A$, and
>
> $$
> \det(xI - A) = \det\begin{pmatrix} x - 1 & -i \\ -i & x + 1 \end{pmatrix} = (x - 1)(x + 1) - (-i)^2 = x^2 - 1 + 1 = x^2,
> $$
>
> so $0$ is its only eigenvalue. The second row of $A$ is $i$ times the first, $(i, -1) = i\,(1, i)$, so $A$ has rank $1$ and its $0$-eigenspace $\ker A$ is $1$-dimensional; it is spanned by $(-i, 1) = -i\,(1, i)$, the line of item 1. A diagonalizable $2 \times 2$ matrix whose only eigenvalue is $0$ is the zero matrix, so $A$ is not diagonalizable. Over $\mathbb{R}$, by contrast, every symmetric matrix is diagonalizable (the [[Real spectral theorem|real spectral theorem]]; Axler, Ch. 7).
>
> Sesquilinear forms, defined next, repair the first failure: for the standard Hermitian form, $(1, i)$ has $\langle (1, i), (1, i) \rangle = 2$ (Example [[§64 Sesquilinear and Hermitian Forms#^ex-64-3|§64.3]]). For the second, the complex counterparts of symmetric matrices are the Hermitian matrices $Q = Q^\dagger$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-5|§64.5]]), and $A$ is not one: $A^\dagger = \begin{pmatrix} 1 & -i \\ -i & -1 \end{pmatrix} \neq A$. (Hermitian matrices are diagonalizable, by the [[Complex spectral theorem|complex spectral theorem]], Axler, Ch. 7; it is not proved in these notes.)
>
> *Source: MATH 420 slides*

^ex-64-1

> [!definition] Definition §64.1: Sesquilinear Form
> Let $V$ be a complex vector space. A **sesquilinear form** (Latin *sesqui-*, one and a half, as in *sesquicentennial*: linear in one variable and “half linear” in the other) is a map $\langle\ ,\ \rangle: V \times V \to \mathbb{C}$ that is additive in each variable,
>
> $$
> \langle u_1 + u_2, v \rangle = \langle u_1, v \rangle + \langle u_2, v \rangle, \qquad \langle u, v_1 + v_2 \rangle = \langle u, v_1 \rangle + \langle u, v_2 \rangle,
> $$
>
> and satisfies, for $\lambda \in \mathbb{C}$,
>
> $$
> \langle \lambda u, v \rangle = \lambda \langle u, v \rangle, \qquad \langle u, \lambda v \rangle = \bar\lambda \langle u, v \rangle.
> $$
>
> Authors disagree about which variable carries the complex conjugate; here it is the second (the remark *Which Variable Is Conjugate-Linear* at the end of this section compares the two conventions).
>
> *Source: board 11/6; MATH 420 slides*

^def-64-1

> [!definition] Definition §64.2: Hermitian Form
> A sesquilinear form $\langle\ ,\ \rangle$ on a complex vector space $V$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]) is **Hermitian** if $\langle u, v \rangle = \overline{\langle v, u \rangle}$ for all $u, v \in V$. Then $\langle u, u \rangle \in \mathbb{R}$ for every $u$, since $\langle u, u \rangle$ equals its own complex conjugate. Hermitian is the complex counterpart of symmetric.
>
> *Source: board 11/6; MATH 420 slides*

^def-64-2

> [!definition] Definition §64.3: Positive Definite Hermitian Form
> A Hermitian form $\langle\ ,\ \rangle$ on $V$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-2|§64.2]]) is **positive definite** if $\langle u, u \rangle > 0$ for every $u \neq 0$; the inequality makes sense because $\langle u, u \rangle$ is real. A positive definite Hermitian form is the complex counterpart of an inner product (Definition [[§63 Invariant Inner Products and Maschke over ℝ#^def-63-1|§63.1]]).
>
> *Source: board 11/6; MATH 420 slides*

^def-64-3

> [!theorem] Lemma §64.1: No Bilinear Form on a Complex Space Is Positive Definite
> Let $V \neq \{0\}$ be a complex vector space. There is no bilinear form $\langle\ ,\ \rangle$ on $V$ with $\langle v, v \rangle$ a positive real number for every $v \neq 0$.
>
> *Source: lecture 11/6*

^lem-64-1

> [!proof]+ Proof
> *Idea:* scaling by $i$ multiplies $\langle v, v \rangle$ by $i^2 = -1$.
>
> Let $\langle\ ,\ \rangle$ be bilinear and $v \neq 0$. Then $iv \neq 0$ and, by bilinearity, $\langle iv, iv \rangle = i^2 \langle v, v \rangle = -\langle v, v \rangle$. So $\langle v, v \rangle$ and $\langle iv, iv \rangle$ cannot both be positive.

^pf-64-1

> [!remark] Remark: Why Not Bilinear, and Unitary Matrices
> A bilinear form on a complex vector space cannot be positive definite (Lemma [[§64 Sesquilinear and Hermitian Forms#^lem-64-1|§64.1]]). Positive definite Hermitian forms are the complex replacement for inner products. The whole theory carries over, with complex conjugates in the right places: orthonormal bases exist (Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]] below), and the matrices preserving the form are the **unitary** matrices, $\bar M^T M = I$, that is $M^\dagger M = I$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-4|§64.4]]), the analogue of orthogonal matrices (compare the unitary group $U_n(\mathbb{C})$ in the remark *Where the Groups of Lie Type Come From* in [[§56 Simple Groups of Small Order|§56]]). The averaging argument of Propositions [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-4|§63.4]] and [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|§63.5]] works verbatim: a finite group acting on a finite-dimensional complex vector space preserves a positive definite Hermitian form and acts by unitary matrices in a suitable basis, and Maschke's theorem over $\mathbb{C}$ follows in the same way. This is a side topic of the course; the MATH 420 slides on complex inner products, posted on Canvas, are worked out in the rest of this section.
>
> *Source: lecture 11/6*

^rem-64-1

![[m493-61-3.svg]]

*(Not from lecture; figure added.)* Why a bilinear form on a complex vector space cannot be positive definite. Fix $v$ with $B(v, v) = 1$ and multiply $v$ by the unit scalars $e^{i\theta}$. A bilinear $B$ gives $B(e^{i\theta}v, e^{i\theta}v) = e^{2i\theta}$: as $\theta$ goes from $0^\circ$ to $180^\circ$, the value runs once around the unit circle of $\mathbb{C}$, and at $\theta = 90^\circ$, the vector $iv$, it is $-1$. A sesquilinear form gives $\langle e^{i\theta}v, e^{i\theta}v \rangle = e^{i\theta}\,\overline{e^{i\theta}}\,\langle v, v \rangle = 1$ for every $\theta$.

The rest of the section works out the complex theory along the MATH 420 slides on complex inner products: forms on $\mathbb{C}^n$ as matrices, the standard Hermitian form, and orthonormal bases.

> [!definition] Definition §64.4: Conjugate Transpose
> For an $m \times n$ complex matrix $A$, the **conjugate transpose** is the $n \times m$ matrix $A^\dagger = \bar A^{\mathsf{T}}$, obtained by transposing $A$ and replacing each entry by its complex conjugate: $(A^\dagger)_{ij} = \overline{A_{ji}}$. For a column vector $y \in \mathbb{C}^n$, $y^\dagger = (\bar y_1, \ldots, \bar y_n)$ is a row vector.
>
> *Source: MATH 420 slides*

^def-64-4

> [!definition] Definition §64.5: Hermitian Matrix
> A complex $n \times n$ matrix $Q$ is **Hermitian** if $Q = Q^\dagger$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-4|§64.4]]), that is, $Q_{ij} = \overline{Q_{ji}}$ for all $i, j$. Hermitian is the complex counterpart of symmetric; a real matrix is Hermitian exactly when it is symmetric.
>
> *Source: MATH 420 slides*

^def-64-5

> [!theorem] Proposition §64.2: Sesquilinear Forms on $\mathbb{C}^n$ Are Matrices
> Write vectors of $\mathbb{C}^n$ as columns, and let $e_1, \ldots, e_n$ be the standard basis.
>
> 1. For every complex $n \times n$ matrix $Q$, $\langle x, y \rangle = y^\dagger Q x$ is a sesquilinear form on $\mathbb{C}^n$ (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]). Every sesquilinear form on $\mathbb{C}^n$ is of this form for exactly one $Q$, namely $Q_{ij} = \langle e_j, e_i \rangle$.
> 2. The form $\langle x, y \rangle = y^\dagger Q x$ is Hermitian (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-2|§64.2]]) if and only if $Q$ is a Hermitian matrix (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-5|§64.5]]).
>
> *Source: MATH 420 slides, in the convention of Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]*

^prop-64-2

> [!proof]+ Proof
> *Idea:* expand both vectors in the standard basis; the form is determined by its values $\langle e_j, e_i \rangle$.
>
> *(Not from the slides; filled in.)*
>
> (1) *$y^\dagger Q x$ is sesquilinear.* Written out, $y^\dagger Q x = \sum_{i,j} \bar y_i Q_{ij} x_j$. Each term is additive in $x$ and in $y$, and for $\lambda \in \mathbb{C}$
>
> $$
> \bar y_i Q_{ij} (\lambda x_j) = \lambda\, \bar y_i Q_{ij} x_j, \qquad \overline{\lambda y_i}\, Q_{ij} x_j = \bar\lambda\, \bar y_i Q_{ij} x_j;
> $$
>
> so the sum satisfies the conditions of Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]], with $x$ as the first variable and $y$ as the second.
>
> *Every sesquilinear form is of this form.* Let $\langle\ ,\ \rangle$ be sesquilinear and put $Q_{ij} = \langle e_j, e_i \rangle$. For $x = \sum_j x_j e_j$ and $y = \sum_i y_i e_i$, additivity in each variable, linearity in the first and conjugate-linearity in the second give
>
> $$
> \langle x, y \rangle = \Big\langle \sum_j x_j e_j,\ \sum_i y_i e_i \Big\rangle = \sum_{i,j} x_j\, \bar y_i\, \langle e_j, e_i \rangle = \sum_{i,j} \bar y_i Q_{ij} x_j = y^\dagger Q x.
> $$
>
> *Uniqueness.* If also $\langle x, y \rangle = y^\dagger Q' x$ for all $x, y$, then $Q'_{ij} = e_i^\dagger Q' e_j = \langle e_j, e_i \rangle = Q_{ij}$ for all $i, j$, so $Q' = Q$.
>
> (2) By (1), $Q_{ij} = \langle e_j, e_i \rangle$. If the form is Hermitian, then for all $i, j$
>
> $$
> Q_{ij} = \langle e_j, e_i \rangle = \overline{\langle e_i, e_j \rangle} = \overline{Q_{ji}} = (Q^\dagger)_{ij},
> $$
>
> so $Q = Q^\dagger$. Conversely, let $Q = Q^\dagger$, i.e. $\overline{Q_{ij}} = Q_{ji}$. Then for all $x, y$
>
> $$
> \overline{\langle y, x \rangle} = \overline{\sum_{i,j} \bar x_i Q_{ij} y_j} = \sum_{i,j} x_i\, \overline{Q_{ij}}\, \bar y_j = \sum_{i,j} \bar y_j\, Q_{ji}\, x_i = y^\dagger Q x = \langle x, y \rangle,
> $$
>
> where the fourth equality is the formula $y^\dagger Q x = \sum_{a,b} \bar y_a Q_{ab} x_b$ with $a = j$, $b = i$. So the form is Hermitian.

^pf-64-2

*Uses:* [[§64 Sesquilinear and Hermitian Forms#^def-64-1|Def. §64.1]]

> [!example] Example §64.2: A Hermitian Matrix
> The matrix
>
> $$
> Q = \begin{pmatrix} 3 & 5 + 3i & -2 + 3i \\ 5 - 3i & 7 & -4i \\ -2 - 3i & 4i & 11 \end{pmatrix}
> $$
>
> is Hermitian (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-5|§64.5]]): the diagonal entries $3, 7, 11$ are real, and each entry below the diagonal is the conjugate of its mirror image above it, $\overline{5 + 3i} = 5 - 3i$, $\overline{-2 + 3i} = -2 - 3i$, $\overline{-4i} = 4i$. So $\langle x, y \rangle = y^\dagger Q x$ is a Hermitian form on $\mathbb{C}^3$ (Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-2|§64.2]]). The diagonal of every Hermitian matrix is real, since $Q_{ii} = \overline{Q_{ii}}$.
>
> Hermitian does not imply positive definite. For $x = (5 + 3i, -3, 0)$ only the upper left $2 \times 2$ block of $Q$ contributes, and its two off-diagonal terms $\bar x_1 Q_{12} x_2$ and $\bar x_2 Q_{21} x_1$ are complex conjugates of each other:
>
> $$
> \langle x, x \rangle = x^\dagger Q x = 3\,|5 + 3i|^2 + 7 \cdot |{-3}|^2 + 2 \operatorname{Re}\!\big(\overline{(5 + 3i)}\,(5 + 3i)(-3)\big) = 3 \cdot 34 + 63 - 204 = -39 < 0.
> $$
>
> *Source: MATH 420 slides; the vector $x$ not from the slides*

^ex-64-2

> [!example] Example §64.3: The Standard Hermitian Form on $\mathbb{C}^n$
> The standard positive definite Hermitian form on $\mathbb{C}^n$ is
>
> $$
> \langle p, q \rangle = p_1 \bar q_1 + p_2 \bar q_2 + \cdots + p_n \bar q_n = q^\dagger p,
> $$
>
> the form of Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-2|§64.2]] with $Q = I$; it is Hermitian since $I^\dagger = I$. Writing $p_k = x_k + y_k i$ with $x_k, y_k \in \mathbb{R}$,
>
> $$
> \langle p, p \rangle = (x_1 + y_1 i)(x_1 - y_1 i) + \cdots + (x_n + y_n i)(x_n - y_n i) = x_1^2 + y_1^2 + \cdots + x_n^2 + y_n^2 \geq 0,
> $$
>
> with equality only if every $x_k$ and $y_k$ is $0$, i.e. $p = 0$. So the form is positive definite, and $\langle p, p \rangle$ is the squared Euclidean length of $p$ read as the vector $(x_1, y_1, \ldots, x_n, y_n) \in \mathbb{R}^{2n}$. The standard basis is orthonormal. The vector $(1, i)$ of Example [[§64 Sesquilinear and Hermitian Forms#^ex-64-1|§64.1]], of length $0$ for the dot product, has
>
> $$
> \langle (1, i), (1, i) \rangle = 1 \cdot \bar 1 + i \cdot \bar i = 1 + i(-i) = 2,
> $$
>
> so $\tfrac{1}{\sqrt2}(1, i)$ is an orthonormal basis of the line $\mathbb{C}(1, i)$.
>
> *Source: MATH 420 slides, there written $\bar p_1 q_1 + \cdots + \bar p_n q_n$ (see the remark *Which Variable Is Conjugate-Linear* below)*

^ex-64-3

> [!theorem] Proposition §64.3: Orthogonal Projection for a Positive Definite Hermitian Form
> Let $V$ be a complex vector space with a positive definite Hermitian form $\langle\ ,\ \rangle$, and let $u_1, \ldots, u_k$ be an orthogonal basis of a subspace $L$: the $u_i$ are nonzero and $\langle u_i, u_j \rangle = 0$ for $i \neq j$. Define
>
> $$
> P_L(v) = \sum_{i=1}^k \frac{\langle v, u_i \rangle}{\langle u_i, u_i \rangle}\, u_i \qquad (v \in V).
> $$
>
> 1. $P_L: V \to V$ is linear, its image lies in $L$, and $P_L(v) = v$ for $v \in L$.
> 2. $v - P_L(v)$ is orthogonal to $L$: $\langle v - P_L(v), u \rangle = 0$ for every $u \in L$.
>
> This is the formula of the real case (proof of Proposition [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-1|§63.1]]), written for an orthogonal rather than an orthonormal basis.
>
> *Source: MATH 420 slides, in the convention of Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]*

^prop-64-3

> [!proof]+ Proof
> *Idea:* the coefficient of $u_i$ is chosen so that $v - P_L(v)$ has no $u_i$-component; the other $u_j$ do not interfere, being orthogonal to $u_i$.
>
> *(Not from the slides; filled in.)* The denominators $\langle u_i, u_i \rangle$ are positive real numbers, since $u_i \neq 0$ and the form is positive definite (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-3|§64.3]]).
>
> (1) Each coefficient $v \mapsto \langle v, u_i \rangle / \langle u_i, u_i \rangle$ is linear in $v$, because the form is linear in its first variable (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]); hence $P_L$ is linear, and $P_L(v)$, a linear combination of $u_1, \ldots, u_k$, lies in $L$. If $v = \sum_j a_j u_j \in L$, then by orthogonality $\langle v, u_i \rangle = \sum_j a_j \langle u_j, u_i \rangle = a_i \langle u_i, u_i \rangle$, so the coefficient of $u_i$ in $P_L(v)$ is $a_i$, and $P_L(v) = v$.
>
> (2) For each $j$, by linearity in the first variable and $\langle u_i, u_j \rangle = 0$ for $i \neq j$,
>
> $$
> \langle v - P_L(v), u_j \rangle = \langle v, u_j \rangle - \sum_{i=1}^k \frac{\langle v, u_i \rangle}{\langle u_i, u_i \rangle} \langle u_i, u_j \rangle = \langle v, u_j \rangle - \frac{\langle v, u_j \rangle}{\langle u_j, u_j \rangle} \langle u_j, u_j \rangle = 0.
> $$
>
> A general $u \in L$ is $u = \sum_j c_j u_j$, and by conjugate-linearity in the second variable $\langle v - P_L(v), u \rangle = \sum_j \bar c_j \langle v - P_L(v), u_j \rangle = 0$.

^pf-64-3

*Uses:* [[§64 Sesquilinear and Hermitian Forms#^def-64-3|Def. §64.3]], [[§64 Sesquilinear and Hermitian Forms#^def-64-1|Def. §64.1]]

> [!theorem] Proposition §64.4: Orthonormal Bases for a Positive Definite Hermitian Form
> Let $V$ be a finite-dimensional complex vector space with a positive definite Hermitian form $\langle\ ,\ \rangle$. Then $V$ has an orthonormal basis, i.e. a basis $w_1, \ldots, w_n$ with $\langle w_i, w_j \rangle = 1$ if $i = j$ and $0$ otherwise. It is obtained from any basis by the Gram–Schmidt algorithm, exactly as over $\mathbb{R}$.
>
> *Source: MATH 420 slides*

^prop-64-4

> [!proof]+ Proof
> *Idea:* subtract from each basis vector its projection onto the span of the previous ones, then scale to length $1$.
>
> *(Not from the slides; filled in.)* If $V = \{0\}$, the empty basis is orthonormal. Otherwise let $v_1, \ldots, v_n$ be a basis of $V$ and define recursively
>
> $$
> u_1 = v_1, \qquad u_k = v_k - P_{L_{k-1}}(v_k) \quad (2 \leq k \leq n), \qquad \text{where } L_{k-1} = \operatorname{span}(u_1, \ldots, u_{k-1})
> $$
>
> and $P_{L_{k-1}}$ is the projection of Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-3|§64.3]]. We show by induction on $k$ that $u_1, \ldots, u_k$ are nonzero and pairwise orthogonal, with $\operatorname{span}(u_1, \ldots, u_k) = \operatorname{span}(v_1, \ldots, v_k)$. (The statement for $k - 1$ makes $u_1, \ldots, u_{k-1}$ an orthogonal basis of $L_{k-1}$, so $P_{L_{k-1}}$ is defined.)
>
> *$k = 1$.* $u_1 = v_1 \neq 0$, since $v_1$ belongs to a basis.
>
> *From $k - 1$ to $k$.* By Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-3|§64.3]](2), $u_k = v_k - P_{L_{k-1}}(v_k)$ is orthogonal to $L_{k-1}$, so $\langle u_k, u_i \rangle = 0$ for $i < k$, and $\langle u_i, u_k \rangle = \overline{\langle u_k, u_i \rangle} = 0$ by the Hermitian property. Next, $P_{L_{k-1}}(v_k)$ lies in $L_{k-1}$, which equals $\operatorname{span}(v_1, \ldots, v_{k-1})$ by the induction hypothesis; so $u_k \in \operatorname{span}(v_1, \ldots, v_k)$ and $v_k = u_k + P_{L_{k-1}}(v_k) \in \operatorname{span}(u_1, \ldots, u_k)$, which gives $\operatorname{span}(u_1, \ldots, u_k) = \operatorname{span}(v_1, \ldots, v_k)$. Finally, if $u_k = 0$, then $v_k = P_{L_{k-1}}(v_k)$ would lie in $\operatorname{span}(v_1, \ldots, v_{k-1})$, contradicting the linear independence of $v_1, \ldots, v_k$; so $u_k \neq 0$.
>
> *Normalizing.* Each $\langle u_k, u_k \rangle$ is a positive real number (positive definiteness), so $w_k = u_k / \sqrt{\langle u_k, u_k \rangle}$ is defined. For a real scalar $r$, $\langle r u, r u \rangle = r \bar r \langle u, u \rangle = r^2 \langle u, u \rangle$, so $\langle w_k, w_k \rangle = 1$; scaling keeps $\langle w_i, w_j \rangle = 0$ for $i \neq j$. The $w_1, \ldots, w_n$ span $\operatorname{span}(v_1, \ldots, v_n) = V$, and $n$ vectors spanning the $n$-dimensional space $V$ form a basis.

^pf-64-4

*Uses:* [[§64 Sesquilinear and Hermitian Forms#^prop-64-3|§64.3]]

![[m493-61-4.svg]]

*(Not from lecture; figure added.)* One step of the Gram–Schmidt algorithm in the proof of Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]]: $u_2$ is $v_2$ minus its projection onto the span of $u_1$, so it is orthogonal to $u_1$, and $u_1, u_2$ span the same subspace as $v_1, v_2$. The picture is drawn in a real plane; over $\mathbb{C}$ the coefficient $\langle v_2, u_1 \rangle / \langle u_1, u_1 \rangle$ is a complex number, and $\operatorname{span}(u_1)$ is a complex line.

> [!remark] Remark: Which Variable Is Conjugate-Linear
> These notes follow the board of 11/6: $\langle\ ,\ \rangle$ is linear in the first variable and conjugate-linear in the second (Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]]). The MATH 420 slides on complex inner products, posted for this course, use the opposite convention: a form $B$ with $B(v, cw) = c\,B(v, w)$ and $B(cv, w) = \bar c\,B(v, w)$. The two are related by $B(v, w) = \langle w, v \rangle$, and the translation changes nothing else:
> - $B$ is Hermitian, or positive definite, exactly when $\langle\ ,\ \rangle$ is, and for Hermitian forms $B(v, w) = 0$ exactly when $\langle v, w \rangle = 0$, so orthogonality means the same;
> - on $\mathbb{C}^n$ the two use the same matrix $Q$: $B(x, y) = x^\dagger Q y$ and $\langle x, y \rangle = y^\dagger Q x$ (Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-2|§64.2]]);
> - the standard form of Example [[§64 Sesquilinear and Hermitian Forms#^ex-64-3|§64.3]] is $B(p, q) = \bar p_1 q_1 + \cdots + \bar p_n q_n$;
> - the coefficient $\langle v, u_i \rangle$ in the projection of Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-3|§64.3]] is $B(u_i, v)$.
>
> Both conventions are common. Linear in the first variable (as here, and in Axler) is more usual in pure mathematics; linear in the second is more usual in applied mathematics, physics and engineering. Many texts write $A^\ast$ for $A^\dagger$, and $\ast$ also denotes the dual space $V^\ast$, so the meaning of $\ast$ has to be read from the context.
>
> *Source: MATH 420 slides*

^rem-64-2

> [!remark]- Connections
> - Linear Algebra: Axler's inner product ([[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]]) is a positive definite Hermitian form in the convention of Definition [[§64 Sesquilinear and Hermitian Forms#^def-64-1|§64.1]] (linear in the first slot). The Gram–Schmidt procedure ([[§21 Orthonormal Bases#^ladr-6-32|LADR 6.32]]) and the existence of orthonormal bases ([[§21 Orthonormal Bases#^ladr-6-35|LADR 6.35]]) are Proposition [[§64 Sesquilinear and Hermitian Forms#^prop-64-4|§64.4]].
> - Spectral theorems quoted in Example [[§64 Sesquilinear and Hermitian Forms#^ex-64-1|§64.1]]: real symmetric matrices ([[§24 Spectral Theorem#^ladr-7-29|LADR 7.29]]) and complex normal, in particular Hermitian, matrices ([[§24 Spectral Theorem#^ladr-7-31|LADR 7.31]]) are diagonalizable in an orthonormal basis.
