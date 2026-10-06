---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 25
lay: "4.3"
aliases: ["Lay 4.3"]
tags: [applied-linear-algebra, math235]
---
← [[§24 Null Spaces, Column Spaces, and Linear Transformations]] · ↑ [[· 4 Vector Spaces]] · [[§26 Coordinate Systems]] →

*Lay, Section 4.3 · MATH 235 lectures L10, L14, L15.*

This section identifies the subsets that span a vector space $V$ (or a subspace $H$) as efficiently as possible. Linear independence is defined exactly as in $\mathbb{R}^n$, and a basis is a linearly independent spanning set. A basis can always be cut out of a finite spanning set by discarding vectors that depend on the others (the Spanning Set Theorem). For a matrix this gives concrete algorithms: the vectors produced by solving $A\mathbf{x} = \mathbf{0}$ form a basis of $\operatorname{Nul} A$, and the pivot columns of $A$ form a basis of $\operatorname{Col} A$. A basis is at the same time a spanning set that is as small as possible and an independent set that is as large as possible.

## Linear Independence

> [!definition] Definition §25.1: Linearly Independent and Dependent Sets
> An indexed set of vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in a vector space $V$ is **linearly independent** if the vector equation
>
> $$
> c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_p\mathbf{v}_p = \mathbf{0} \qquad (1)
> $$
>
> has *only* the trivial solution $c_1 = 0, \ldots, c_p = 0$. The set is **linearly dependent** if (1) has a nontrivial solution, that is, if there are weights $c_1, \ldots, c_p$, *not all zero*, such that (1) holds; then (1) is called a **linear dependence relation** among $\mathbf{v}_1, \ldots, \mathbf{v}_p$.
>
> Just as in $\mathbb{R}^n$ ([[§7 Linear Independence#^prop-7-2|Proposition §7.2]], [[§7 Linear Independence#^prop-7-3|Proposition §7.3]], [[§7 Linear Independence#^thm-7-7|Theorem §7.7]]): a set $\{\mathbf{v}\}$ of one vector is linearly independent if and only if $\mathbf{v} \ne \mathbf{0}$; a set of two vectors is linearly dependent if and only if one of them is a multiple of the other; and any set containing the zero vector is linearly dependent.
>
> *Lay: 4.3 (text)*

^def-25-1

> [!theorem] Theorem §25.1: Characterization of Linearly Dependent Sets
> An indexed set $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ of two or more vectors, with $\mathbf{v}_1 \ne \mathbf{0}$, is linearly dependent if and only if some $\mathbf{v}_j$ (with $j > 1$) is a linear combination of the preceding vectors $\mathbf{v}_1, \ldots, \mathbf{v}_{j-1}$.
>
> *Lay: Theorem 4 (4.3)*

^thm-25-1

> [!proof]+ Proof
> *Lay: "the same proof as Theorem 7 in Section 1.7".* If $\mathbf{v}_j = c_1\mathbf{v}_1 + \cdots + c_{j-1}\mathbf{v}_{j-1}$, then
>
> $$
> c_1\mathbf{v}_1 + \cdots + c_{j-1}\mathbf{v}_{j-1} + (-1)\mathbf{v}_j + 0\mathbf{v}_{j+1} + \cdots + 0\mathbf{v}_p = \mathbf{0}
> $$
>
> is a linear dependence relation (the weight of $\mathbf{v}_j$ is $-1 \ne 0$).
>
> Conversely, let $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p = \mathbf{0}$ with weights not all zero, and let $j$ be the largest subscript with $c_j \ne 0$. If $j = 1$, then $c_1\mathbf{v}_1 = \mathbf{0}$ with $c_1 \ne 0$, so $\mathbf{v}_1 = c_1^{-1}(c_1\mathbf{v}_1) = c_1^{-1}\mathbf{0} = \mathbf{0}$, which is impossible. So $j > 1$, and $c_1\mathbf{v}_1 + \cdots + c_j\mathbf{v}_j = \mathbf{0}$ can be solved for $\mathbf{v}_j$:
>
> $$
> \mathbf{v}_j = \left(-\frac{c_1}{c_j}\right)\mathbf{v}_1 + \cdots + \left(-\frac{c_{j-1}}{c_j}\right)\mathbf{v}_{j-1} .
> $$

^pf-25-1

*Uses:* [[§25 Linearly Independent Sets; Bases#^def-25-1|Def. §25.1]], [[§23 Vector Spaces and Subspaces#^prop-23-2|§23.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§4 Span and Linear Independence#^ladr-2-15|LADR 2.15]] (linearly independent lists) and the linear dependence lemma [[§4 Span and Linear Independence#^ladr-2-19|LADR 2.19]], which adds that removing such a $\mathbf{v}_j$ does not change the span (part (a) of Theorem §25.2 below). Axler works with lists, Lay with indexed sets; the difference is only that a list may repeat a vector.

The main difference from $\mathbb{R}^n$: when the vectors are not $n$-tuples, equation (1) usually cannot be written as a system of $n$ linear equations, so the vectors cannot be made the columns of a matrix $A$ and studied through $A\mathbf{x} = \mathbf{0}$. One must rely on the definition and on Theorem §25.1, until coordinates ([[§26 Coordinate Systems#^cor-26-4|Corollary §26.4]]) translate the problem back to $\mathbb{R}^n$.

> [!example] Example §25.1: Dependence and Independence Among Functions
> **(a)** Let $\mathbf{p}_1(t) = 1$, $\mathbf{p}_2(t) = t$, $\mathbf{p}_3(t) = 4 - t$. Then $\{\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3\}$ is linearly dependent in $\mathbb{P}$, because $\mathbf{p}_3 = 4\mathbf{p}_1 - \mathbf{p}_2$.
>
> **(b)** $\{\sin t, \cos t\}$ is linearly independent in $C[0, 1]$, the space of continuous functions on $0 \le t \le 1$: as *vectors in $C[0,1]$* neither is a multiple of the other, since there is no scalar $c$ with $\cos t = c \cdot \sin t$ for all $t \in [0, 1]$ (at $t = 0$ the left side is $1$ and the right side $0$), nor one with $\sin t = c\cos t$ for all $t$ ($\sin t / \cos t = \tan t$ is not constant). However, $\{\sin t\cos t, \sin 2t\}$ is linearly dependent, because of the identity $\sin 2t = 2\sin t\cos t$ for all $t$.
>
> *Lay: Examples 4.3.1 and 4.3.2*

^ex-25-1

## Bases

> [!definition] Definition §25.2: Basis
> Let $H$ be a subspace of a vector space $V$. An indexed set of vectors $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ in $V$ is a **basis** for $H$ if
>
> (i) $\mathcal{B}$ is a linearly independent set, and
>
> (ii) the subspace spanned by $\mathcal{B}$ coincides with $H$; that is, $H = \operatorname{Span}\{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$.
>
> Since every vector space is a subspace of itself, this covers $H = V$: a basis of $V$ is a linearly independent set that spans $V$. When $H \ne V$, condition (ii) includes the requirement that each $\mathbf{b}_j$ belongs to $H$.
>
> *Lay: 4.3, Definition*

^def-25-2

> [!remark]- Connections
> - Rigorous treatment: [[§5 Bases#^ladr-2-26|LADR 2.26]], and the criterion [[§5 Bases#^ladr-2-28|LADR 2.28]] (a list is a basis iff every vector is a unique linear combination of it), which is Lay's Unique Representation Theorem ([[§26 Coordinate Systems#^thm-26-1|Theorem §26.1]], Theorem 7 of 4.4).

> [!example] Example §25.2: Standard Bases and Bases of ℝⁿ
> **(a) Columns of an invertible matrix.** If $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ is an invertible $n \times n$ matrix, its columns form a basis for $\mathbb{R}^n$: by the Invertible Matrix Theorem ([[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]]) they are linearly independent and span $\mathbb{R}^n$. For instance, $\mathbf{v}_1 = (3, 0, -6)$, $\mathbf{v}_2 = (-4, 1, 7)$, $\mathbf{v}_3 = (-2, 1, 5)$ form a basis of $\mathbb{R}^3$: two row replacements ($R_3 + 2R_1$, then $R_3 + R_2$) give
>
> $$
> \begin{bmatrix} 3 & -4 & -2 \\ 0 & 1 & 1 \\ -6 & 7 & 5 \end{bmatrix} \sim \begin{bmatrix} 3 & -4 & -2 \\ 0 & 1 & 1 \\ 0 & -1 & 1 \end{bmatrix} \sim \begin{bmatrix} 3 & -4 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix},
> $$
>
> three pivot positions, so $A = [\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3]$ is invertible.
>
> **(b) The standard basis of $\mathbb{R}^n$.** The columns $\mathbf{e}_1, \ldots, \mathbf{e}_n$ of $I_n$ form the **standard basis** for $\mathbb{R}^n$. Directly (the lecture, for $n = 3$): $a_1\mathbf{e}_1 + a_2\mathbf{e}_2 + a_3\mathbf{e}_3 = (a_1, a_2, a_3)$ is $\mathbf{0}$ only if $a_1 = a_2 = a_3 = 0$, and every $\mathbf{v} = (v_1, v_2, v_3)$ equals $v_1\mathbf{e}_1 + v_2\mathbf{e}_2 + v_3\mathbf{e}_3$.
>
> **(c) The standard basis of $\mathbb{P}_n$** is $S = \{1, t, t^2, \ldots, t^n\}$. Certainly $S$ spans $\mathbb{P}_n$. If
>
> $$
> c_0 \cdot 1 + c_1t + c_2t^2 + \cdots + c_nt^n = \mathbf{0}(t) \qquad (2)
> $$
>
> as functions, the polynomial on the left has the same values as the zero polynomial, so every real number is a zero of it. A polynomial of degree at most $n$ with more than $n$ zeros is the zero polynomial (a basic fact of algebra, [[§13 Polynomials#^ladr-4-8|LADR 4.8]]), so $c_0 = \cdots = c_n = 0$. Thus $S$ is linearly independent, hence a basis. The lecture calls it the **monomial basis**.
>
> **(d) The standard basis of $M_{2 \times 2}$** consists of
>
> $$
> E_{11} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad E_{12} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \quad E_{21} = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, \quad E_{22} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix},
> $$
>
> since $\begin{bmatrix} a & b \\ c & d \end{bmatrix} = aE_{11} + bE_{12} + cE_{21} + dE_{22}$, and this is the zero matrix only when $a = b = c = d = 0$. Likewise the $mn$ matrices with a single entry $1$ form a basis of $M_{m \times n}$.
>
> *Lay: Examples 4.3.3–4.3.6*
> *Source: 235 lecture L14; 235 checklist (4.3)*

^ex-25-2

## The Spanning Set Theorem

> [!theorem] Theorem §25.2: The Spanning Set Theorem
> Let $S = \{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ be a set in a vector space $V$, and let $H = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$.
>
> a. If one of the vectors in $S$, say $\mathbf{v}_k$, is a linear combination of the remaining vectors in $S$, then the set formed from $S$ by removing $\mathbf{v}_k$ still spans $H$.
>
> b. If $H \ne \{\mathbf{0}\}$, some subset of $S$ is a basis for $H$.
>
> *Lay: Theorem 5 (4.3)*

^thm-25-2

> [!proof]+ Proof
> **a.** By rearranging the list of vectors in $S$ if necessary, we may suppose that $\mathbf{v}_p$ is a linear combination of $\mathbf{v}_1, \ldots, \mathbf{v}_{p-1}$, say
>
> $$
> \mathbf{v}_p = a_1\mathbf{v}_1 + \cdots + a_{p-1}\mathbf{v}_{p-1} . \qquad (3)
> $$
>
> Any $\mathbf{x}$ in $H$ can be written as
>
> $$
> \mathbf{x} = c_1\mathbf{v}_1 + \cdots + c_{p-1}\mathbf{v}_{p-1} + c_p\mathbf{v}_p \qquad (4)
> $$
>
> for suitable scalars $c_1, \ldots, c_p$. Substituting (3) into (4),
>
> $$
> \mathbf{x} = (c_1 + c_pa_1)\mathbf{v}_1 + \cdots + (c_{p-1} + c_pa_{p-1})\mathbf{v}_{p-1},
> $$
>
> a linear combination of $\mathbf{v}_1, \ldots, \mathbf{v}_{p-1}$. Since $\mathbf{x}$ was arbitrary in $H$, $\{\mathbf{v}_1, \ldots, \mathbf{v}_{p-1}\}$ spans $H$ (and its span is contained in $H$, so it equals $H$).
>
> **b.** If the original spanning set $S$ is linearly independent, it is already a basis for $H$. Otherwise one of the vectors in $S$ depends on the others and can be deleted, by part (a). As long as there are two or more vectors in the spanning set, this can be repeated until the spanning set is linearly independent, and hence a basis for $H$. If the spanning set is eventually reduced to one vector, that vector is nonzero (hence linearly independent) because $H \ne \{\mathbf{0}\}$. The process stops after at most $p - 1$ deletions.

^pf-25-2

*Uses:* [[§25 Linearly Independent Sets; Bases#^def-25-1|Def. §25.1]], [[§25 Linearly Independent Sets; Bases#^def-25-2|Def. §25.2]], [[§23 Vector Spaces and Subspaces#^def-23-3|Def. §23.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§5 Bases#^ladr-2-30|LADR 2.30]] ([[Every spanning list contains a basis]]), proved by the same deletion process; the companion result [[§5 Bases#^ladr-2-32|LADR 2.32]] ([[Every linearly independent list extends to a basis]]) is Lay's Theorem 11 of 4.5 ([[§27 The Dimension of a Vector Space#^thm-27-3|Theorem §27.3]]).

> [!example] Example §25.3: Discarding a Dependent Vector
> Let
>
> $$
> \mathbf{v}_1 = \begin{bmatrix} 0 \\ 2 \\ -1 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 2 \\ 2 \\ 0 \end{bmatrix}, \quad \mathbf{v}_3 = \begin{bmatrix} 6 \\ 16 \\ -5 \end{bmatrix}, \qquad H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\} .
> $$
>
> Note that $\mathbf{v}_3 = 5\mathbf{v}_1 + 3\mathbf{v}_2$ (check: $(0 + 6,\ 10 + 6,\ -5 + 0) = (6, 16, -5)$). Every vector in $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ is in $H$, because $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + 0\mathbf{v}_3$. Conversely, if $\mathbf{x} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$ is in $H$, substituting for $\mathbf{v}_3$,
>
> $$
> \mathbf{x} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3(5\mathbf{v}_1 + 3\mathbf{v}_2) = (c_1 + 5c_3)\mathbf{v}_1 + (c_2 + 3c_3)\mathbf{v}_2 .
> $$
>
> So $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$. Since $\mathbf{v}_1$ and $\mathbf{v}_2$ are not multiples of each other, $\{\mathbf{v}_1, \mathbf{v}_2\}$ is linearly independent, and it is a basis of the plane $H$.
>
> *Lay: Example 4.3.7*

^ex-25-3

## Bases for Nul A, Col A and Row A

**Nul A.** The method of [[§24 Null Spaces, Column Spaces, and Linear Transformations#^rem-24-1|§24, Remark: Method — A Spanning Set for Nul A]] produces a linearly independent spanning set when $\operatorname{Nul} A \ne \{\mathbf{0}\}$ ([[§24 Null Spaces, Column Spaces, and Linear Transformations#^prop-24-2|Proposition §24.2]]), that is, a *basis* for $\operatorname{Nul} A$, with one vector for each free variable.

**Col A.** The key observation: if $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ is row reduced to $B = [\mathbf{b}_1 \ \cdots \ \mathbf{b}_n]$, the columns of $B$ are often totally different from those of $A$, but the equations $A\mathbf{x} = \mathbf{0}$ and $B\mathbf{x} = \mathbf{0}$ have exactly the same solutions. So

$$
x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{0} \quad\text{and}\quad x_1\mathbf{b}_1 + \cdots + x_n\mathbf{b}_n = \mathbf{0}
$$

have the same solutions: **the columns of $A$ have exactly the same linear dependence relationships as the columns of $B$.**

> [!theorem] Theorem §25.3: The Pivot Columns Form a Basis for Col A
> The pivot columns of a matrix $A$ form a basis for $\operatorname{Col} A$.
>
> *Lay: Theorem 6 (4.3)*

^thm-25-3

> [!proof]+ Proof
> Let $B$ be the reduced echelon form of $A$. The pivot columns of $B$ are distinct columns $\mathbf{e}_1, \mathbf{e}_2, \ldots$ of the identity (padded with zeros), so no one of them is a linear combination of the ones before it, and they are linearly independent ([[§25 Linearly Independent Sets; Bases#^thm-25-1|Theorem §25.1]]). Since $A$ is row equivalent to $B$, the pivot columns of $A$ are linearly independent as well, because any linear dependence relation among the columns of $A$ corresponds to one among the columns of $B$. For the same reason, every nonpivot column of $A$ is a linear combination of the pivot columns of $A$ (in $B$, a nonpivot column is a combination of the pivot columns to its left, with weights read off from its entries). So the nonpivot columns of $A$ may be discarded from the spanning set for $\operatorname{Col} A$, by the Spanning Set Theorem. This leaves the pivot columns of $A$ as a basis for $\operatorname{Col} A$.

^pf-25-3

*Uses:* [[§25 Linearly Independent Sets; Bases#^thm-25-1|§25.1]], [[§25 Linearly Independent Sets; Bases#^thm-25-2|§25.2]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-2|Def. §24.2]], [[§1 Systems of Linear Equations#^thm-1-2|§1.2]] (row equivalent systems have the same solutions)

> [!remark] Remark: Warning — Use the Pivot Columns of A Itself
> The pivot columns are evident once $A$ is reduced only to *echelon* form. But the basis for $\operatorname{Col} A$ consists of the pivot columns *of $A$*, not of the echelon form: row operations can change the column space. In Example §25.4(b), every column of the echelon form $B$ has last entry $0$, so the columns of $B$ cannot span $\operatorname{Col} A$, which contains $\mathbf{a}_1 = (1, 3, 2, 5)$.

^rem-25-1

**Row A** ([[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-3|Definition §24.3]]). Row operations do not change the row space, and the nonzero rows of an echelon form of $A$ form a basis of $\operatorname{Row} A$; this is Theorem 13 of 4.6, proved as [[§28 Rank#^thm-28-1|Theorem §28.1]]. Here, unlike for $\operatorname{Col} A$, the rows of the *echelon form* are the ones to use.

> [!remark] Remark: Method — Bases for Nul A, Col A and Row A
> 1. Row reduce $A$ to an echelon form $B$ (to reduced echelon form if $\operatorname{Nul} A$ is wanted). Locate the pivot columns.
> 2. **Col A:** the pivot columns *of $A$*.
> 3. **Nul A:** solve $A\mathbf{x} = \mathbf{0}$ in parametric form; the vectors multiplying the free variables. (No free variables: $\operatorname{Nul} A = \{\mathbf{0}\}$, whose basis is empty.)
> 4. **Row A:** the nonzero rows *of the echelon form $B$*.

^rem-25-2

> [!example] Example §25.4: Bases for the Fundamental Subspaces
> **(a) A matrix in reduced echelon form.** Let
>
> $$
> B = [\mathbf{b}_1 \ \cdots \ \mathbf{b}_5] = \begin{bmatrix} 1 & 4 & 0 & 2 & 0 \\ 0 & 0 & 1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> Each nonpivot column is a combination of the pivot columns: $\mathbf{b}_2 = 4\mathbf{b}_1$ and $\mathbf{b}_4 = 2\mathbf{b}_1 - \mathbf{b}_3$. By the Spanning Set Theorem we may discard $\mathbf{b}_2$ and $\mathbf{b}_4$, and $S = \{\mathbf{b}_1, \mathbf{b}_3, \mathbf{b}_5\} = \{\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3\}$ (in $\mathbb{R}^4$) still spans $\operatorname{Col} B$. Since $\mathbf{b}_1 \ne \mathbf{0}$ and no vector in $S$ is a combination of those before it, $S$ is linearly independent (Theorem §25.1), so $S$ is a basis for $\operatorname{Col} B$.
>
> **(b) The same pattern before reduction.** The matrix
>
> $$
> A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_5] = \begin{bmatrix} 1 & 4 & 0 & 2 & -1 \\ 3 & 12 & 1 & 5 & 5 \\ 2 & 8 & 1 & 3 & 2 \\ 5 & 20 & 2 & 8 & 8 \end{bmatrix}
> $$
>
> is row equivalent to $B$. So its columns satisfy the same relations: $\mathbf{a}_2 = 4\mathbf{a}_1 = (4, 12, 8, 20)$ and $\mathbf{a}_4 = 2\mathbf{a}_1 - \mathbf{a}_3 = (2 - 0,\ 6 - 1,\ 4 - 1,\ 10 - 2) = (2, 5, 3, 8)$, as one checks. Discard $\mathbf{a}_2$ and $\mathbf{a}_4$. Any dependence relation among $\mathbf{a}_1, \mathbf{a}_3, \mathbf{a}_5$ would be one among $\mathbf{b}_1, \mathbf{b}_3, \mathbf{b}_5$, so $\{\mathbf{a}_1, \mathbf{a}_3, \mathbf{a}_5\}$, the pivot columns of $A$, is a basis for $\operatorname{Col} A$.
>
> **(c) All three spaces at once** (the lecture). Let $A = \begin{bmatrix} 1 & 0 & -3 & 2 \\ 0 & 1 & -5 & 4 \\ 3 & -2 & 1 & -2 \end{bmatrix}$. With $R_3 - 3R_1$, then $R_3 + 2R_2$:
>
> $$
> A \sim \begin{bmatrix} 1 & 0 & -3 & 2 \\ 0 & 1 & -5 & 4 \\ 0 & -2 & 10 & -8 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -3 & 2 \\ 0 & 1 & -5 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} ,
> $$
>
> already in reduced echelon form, with pivot columns 1 and 2.
> - $\operatorname{Col} A$: basis $\{(1, 0, 3), (0, 1, -2)\}$, the first two columns of $A$. So $\dim \operatorname{Col} A = 2$, and every basis of $\operatorname{Col} A$ has exactly two vectors ([[§27 The Dimension of a Vector Space#^thm-27-2|Theorem §27.2]]).
> - $\operatorname{Nul} A$: $x_1 = 3x_3 - 2x_4$, $x_2 = 5x_3 - 4x_4$, with $x_3$, $x_4$ free, so
>
> $$
> \mathbf{x} = x_3\begin{bmatrix} 3 \\ 5 \\ 1 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} -2 \\ -4 \\ 0 \\ 1 \end{bmatrix}, \qquad \text{basis } \{(3, 5, 1, 0),\ (-2, -4, 0, 1)\} .
> $$
>
> Check: $A(-2, -4, 0, 1) = (-2 + 0 - 0 + 2,\ -4 + 4,\ -6 + 8 + 0 - 2) = \mathbf{0}$.
> - $\operatorname{Row} A$: basis $\{(1, 0, -3, 2), (0, 1, -5, 4)\}$, the nonzero rows of the echelon form.
>
> *The lecture writes $x_1 = 3x_3 + 2x_4$ and the second basis vector as $(2, -4, 0, 1)$; the first row $x_1 - 3x_3 + 2x_4 = 0$ gives $x_1 = 3x_3 - 2x_4$, hence $(-2, -4, 0, 1)$.*
>
> *Lay: Examples 4.3.8 and 4.3.9*
> *Source: 235 lecture L15*

^ex-25-4

## Two Views of a Basis

> [!remark] Remark: A Basis Is a Minimal Spanning Set and a Maximal Independent Set
> When the Spanning Set Theorem is used, deletion of vectors must stop when the set becomes linearly independent: if one more vector were deleted, it would not be a linear combination of the remaining ones (Theorem §25.1), so the smaller set would no longer span $V$. Thus **a basis is a spanning set that is as small as possible.**
>
> A basis is also **a linearly independent set that is as large as possible**: if $S$ is a basis for $V$ and $S$ is enlarged by one vector $\mathbf{w}$ from $V$, the new set cannot be linearly independent, because $S$ spans $V$, so $\mathbf{w}$ is a linear combination of the elements of $S$.

^rem-25-3

> [!example] Example §25.5: Enlarging and Shrinking
> **(a)** In $\mathbb{R}^3$:
>
> $$
> \underbrace{\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 3 \\ 0 \end{bmatrix} \right\}}_{\text{independent, does not span } \mathbb{R}^3}
> \qquad
> \underbrace{\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 3 \\ 0 \end{bmatrix}, \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} \right\}}_{\text{a basis for } \mathbb{R}^3}
> \qquad
> \underbrace{\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 3 \\ 0 \end{bmatrix}, \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}, \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix} \right\}}_{\text{spans } \mathbb{R}^3, \text{ dependent}}
> $$
>
> The first set lies in the $x_1x_2$-plane. The second is upper triangular with nonzero diagonal $1, 3, 6$, so it is invertible as a matrix and its columns form a basis. Any fourth vector in $\mathbb{R}^3$ is a combination of those three. The lecture's version: $\{\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf{v}\}$ with $\mathbf{v} = (2, -1, 3)$ is not a basis, because $\mathbf{v} - 2\mathbf{e}_1 + \mathbf{e}_2 - 3\mathbf{e}_3 = \mathbf{0}$; and $\{\mathbf{e}_1, \mathbf{e}_2\}$ is not a basis, because $(1, 2, -3)$ is not in its span (every $a\mathbf{e}_1 + b\mathbf{e}_2$ has third entry $0$).
>
> **(b) A basis for a plane, checked from the definition.** Let $W = \{(x, y, z) : x + y + z = 0\}$, a plane through the origin in $\mathbb{R}^3$, and $\mathbf{v}_1 = (1, -1, 0)$, $\mathbf{v}_2 = (1, 0, -1)$, both in $W$.
> - *Independent:* $[\mathbf{v}_1 \ \mathbf{v}_2] = \begin{bmatrix} 1 & 1 \\ -1 & 0 \\ 0 & -1 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & -1 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$ ($R_2 + R_1$, then $R_3 + R_2$) has no free variables.
> - *Spanning:* for $\mathbf{w} = (w_1, w_2, w_3)$ the same operations give
>
> $$
> [\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{w}] \sim \begin{bmatrix} 1 & 1 & w_1 \\ 0 & 1 & w_1 + w_2 \\ 0 & 0 & w_1 + w_2 + w_3 \end{bmatrix} .
> $$
>
> The only potentially bad row is the last one, and for $\mathbf{w} \in W$ its last entry $w_1 + w_2 + w_3$ is $0$. So $a\mathbf{v}_1 + b\mathbf{v}_2 = \mathbf{w}$ is solvable for every $\mathbf{w}$ in $W$.
>
> So $\{\mathbf{v}_1, \mathbf{v}_2\}$ is a basis of $W$. (Equivalently, $W = \operatorname{Nul}\,[1 \ 1 \ 1]$, and the method of [[§25 Linearly Independent Sets; Bases#^rem-25-2|Remark: Method — Bases for Nul A, Col A and Row A]] with free variables $y$, $z$ gives the basis $\{(-1, 1, 0), (-1, 0, 1)\}$.)
>
> *Lay: Example 4.3.10*
> *Source: 235 lecture L14*

^ex-25-5

> [!remark]- Remark: Bases with Infinitely Many Elements
> The lecture points out that a basis need not be finite. In Lay's sense (finite linear combinations), the polynomials $\{1, t, t^2, t^3, \ldots\}$ form a basis of $\mathbb{P}$: every polynomial is a *finite* combination of them, and they are independent by the argument of Example §25.2(c). The lecture also calls the harmonics $\sin 2\pi nx$, $\cos 2\pi nx$ ($n = 0, 1, 2, \ldots$) a basis of $C^\infty([0, 1])$, citing Fourier's theorem $f = \sum_n (a_n \sin 2\pi nx + b_n \cos 2\pi nx)$. That is a statement about *infinite series*, which converge only in a suitable sense (for instance in the mean, [[§47 Applications of Inner Product Spaces#^thm-47-4|Theorem §47.4]]; Fourier series: [[§47 Applications of Inner Product Spaces#^def-47-6|Definition §47.6]]); the harmonics are not a basis in the sense of Definition §25.2, since most smooth functions are not finite combinations of them. The right framework is an orthonormal basis of a Hilbert space ([[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]]); as the lecture says, such bases are a subject of real analysis.
>
> *Source: 235 lectures L14, L15*

^rem-25-4
