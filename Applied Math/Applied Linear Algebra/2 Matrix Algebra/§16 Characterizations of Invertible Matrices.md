---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 16
lay: "2.3"
aliases: ["Lay 2.3"]
tags: [applied-linear-algebra, math235]
---
← [[§15 Elementary Matrices and the Inversion Algorithm]] · ↑ [[· 2 Matrix Algebra]] · [[§17 Partitioned Matrices]] →

*Lay, Section 2.3 · MATH 235 lectures L6, L7, L8, L9.*

For a *square* matrix, almost every concept of Chapter 1 turns out to be equivalent to invertibility. This is the Invertible Matrix Theorem: twelve statements about an $n \times n$ matrix $A$ (pivots, solutions of $A\mathbf{x} = \mathbf{0}$ and $A\mathbf{x} = \mathbf{b}$, independence and spanning of the columns, one-to-one and onto, one-sided inverses, invertibility of $A^T$) are either all true or all false. One consequence is that a one-sided inverse of a square matrix is automatically two-sided. The theorem is then read for linear transformations: $T : \mathbb{R}^n \to \mathbb{R}^n$ has an inverse function exactly when its standard matrix is invertible, and the inverse is again linear. The theorem grows in later sections: (m)–(r) in [[§22 Dimension and Rank#^thm-22-3|Theorem §22.3]], $\det A \ne 0$ in [[§25 Properties of Determinants#^thm-25-4|Theorem §25.4]], (m)–(r) restated in Lay 4.6 form in [[§34 Rank#^thm-34-5|Theorem §34.5]], (s)–(t) in [[§41 The Characteristic Equation#^thm-41-2|Theorem §41.2]], and (u)–(x) in [[§62★ The Singular Value Decomposition in Applications#^thm-62-2|Theorem §62.2]].

## The Invertible Matrix Theorem

> [!theorem] Theorem §19.2: The Invertible Matrix Theorem
> Let $A$ be a square $n \times n$ matrix. Then the following statements are equivalent. That is, for a given $A$, the statements are either all true or all false.
>
> a. $A$ is an invertible matrix.
> b. $A$ is row equivalent to the $n \times n$ identity matrix.
> c. $A$ has $n$ pivot positions.
> d. The equation $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.
> e. The columns of $A$ form a linearly independent set.
> f. The linear transformation $\mathbf{x} \mapsto A\mathbf{x}$ is one-to-one.
> g. The equation $A\mathbf{x} = \mathbf{b}$ has at least one solution for each $\mathbf{b}$ in $\mathbb{R}^n$.
> h. The columns of $A$ span $\mathbb{R}^n$.
> i. The linear transformation $\mathbf{x} \mapsto A\mathbf{x}$ maps $\mathbb{R}^n$ onto $\mathbb{R}^n$.
> j. There is an $n \times n$ matrix $C$ such that $CA = I$.
> k. There is an $n \times n$ matrix $D$ such that $AD = I$.
> l. $A^T$ is an invertible matrix.
>
> Continued with statements (m)–(r) in [[§22 Dimension and Rank#^thm-22-3|Theorem §22.3]].
>
> *Lay: Theorem 8 (2.3)*

^thm-16-1

> [!proof]+ Proof
> "(a) $\Rightarrow$ (j)" means that whenever (a) is true, so is (j). The proof establishes the circle of implications
>
> $$
> \text{(a)} \Rightarrow \text{(j)} \Rightarrow \text{(d)} \Rightarrow \text{(c)} \Rightarrow \text{(b)} \Rightarrow \text{(a)},
> $$
>
> so these five statements are equivalent, and then links each remaining statement to the circle (figure below).
>
> **(a) $\Rightarrow$ (j).** $C = A^{-1}$ works.
>
> **(j) $\Rightarrow$ (d).** (Lay's Exercise 23 in Section 2.1.) If $CA = I$ and $A\mathbf{x} = \mathbf{0}$, then $\mathbf{x} = I\mathbf{x} = CA\mathbf{x} = C\mathbf{0} = \mathbf{0}$.
>
> **(d) $\Rightarrow$ (c).** (Exercise 23 in Section 2.2.) If $A\mathbf{x} = \mathbf{0}$ has only the trivial solution, this consistent system has a unique solution, so it has no free variables ([[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]]). Every one of the $n$ variables is then a basic variable, so every one of the $n$ columns of $A$ is a pivot column: $A$ has $n$ pivot positions.
>
> **(c) $\Rightarrow$ (b).** Each row and each column contains at most one pivot position. $A$ is square, so $n$ pivot positions means exactly one in each of the $n$ rows and each of the $n$ columns. In an echelon form the pivot of row $i + 1$ lies strictly to the right of the pivot of row $i$, so the pivot of row $i$ is in column $i$: the pivots lie on the main diagonal. In the reduced echelon form each pivot is $1$ and is the only nonzero entry in its column, and every column is a pivot column, so the reduced echelon form of $A$ is $I_n$. Thus $A$ is row equivalent to $I_n$.
>
> **(b) $\Rightarrow$ (a).** [[§15 Elementary Matrices and the Inversion Algorithm#^thm-15-3|Theorem §15.3]]. This completes the circle.
>
> **(a) $\Rightarrow$ (k).** $D = A^{-1}$ works.
>
> **(k) $\Rightarrow$ (g).** (Exercise 24 in Section 2.1.) If $AD = I$, then for each $\mathbf{b}$ the vector $\mathbf{x} = D\mathbf{b}$ satisfies $A\mathbf{x} = (AD)\mathbf{b} = I\mathbf{b} = \mathbf{b}$.
>
> **(g) $\Rightarrow$ (a).** (Exercise 24 in Section 2.2.) If $A\mathbf{x} = \mathbf{b}$ is consistent for every $\mathbf{b}$, then $A$ has a pivot position in every row ([[§5 The Matrix Equation Ax = b#^thm-5-3|Theorem §5.3]], (a) $\Rightarrow$ (d)). There are $n$ rows, so (c) holds, and (c) implies (a) through the circle. So (k) and (g) are linked to the circle.
>
> **(g) $\Leftrightarrow$ (h) $\Leftrightarrow$ (i).** These are equivalent for *any* matrix: (g) $\Leftrightarrow$ (h) is [[§5 The Matrix Equation Ax = b#^thm-5-3|Theorem §5.3]] ((a) $\Leftrightarrow$ (c) there), and (h) $\Leftrightarrow$ (i) is [[§10 The Matrix of a Linear Transformation#^thm-10-3|Theorem §10.3]](a) ($\mathbf{x} \mapsto A\mathbf{x}$, whose standard matrix is $A$, is onto exactly when the columns of $A$ span $\mathbb{R}^n$). So (h) and (i) are linked through (g).
>
> **(d) $\Leftrightarrow$ (e) $\Leftrightarrow$ (f).** Also equivalent for any matrix: (d) $\Leftrightarrow$ (e) is [[§8 Linear Independence#^prop-8-1|Proposition §8.1]] (the columns of $A$ are independent exactly when $A\mathbf{x} = \mathbf{0}$ has only the trivial solution), and (e) $\Leftrightarrow$ (f) is [[§10 The Matrix of a Linear Transformation#^thm-10-3|Theorem §10.3]](b).
>
> **(a) $\Leftrightarrow$ (l).** (a) $\Rightarrow$ (l) is [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](c). Applying the same theorem to $A^T$, and using $(A^T)^T = A$ ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]](a)), gives (l) $\Rightarrow$ (a).

^pf-16-1

*Uses:* [[§15 Elementary Matrices and the Inversion Algorithm#^thm-15-3|§15.3]], [[§14 The Inverse of a Matrix#^thm-14-4|§14.4]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|§13.2]], [[§5 The Matrix Equation Ax = b#^thm-5-3|§5.3]], [[§8 Linear Independence#^prop-8-1|§8.1]], [[§10 The Matrix of a Linear Transformation#^thm-10-3|§10.3]], [[§3 Solutions of Linear Systems#^thm-3-1|§3.1]], [[§2 Row Reduction and Echelon Forms#^def-2-3|Def. §2.3]], [[§3 Solutions of Linear Systems#^def-3-1|Def. §3.1]]

![[m235-13-1.svg]]
*How the proof of the Invertible Matrix Theorem is organized. The five statements on the circle imply one another in turn; (k) and (g) attach to it through (a); the statements (g), (h), (i) about spanning and onto, and (d), (e), (f) about independence and one-to-one, are equivalent for every matrix, square or not; and (l) is equivalent to (a) by the inverse of a transpose. Squareness is used only in (c) ⇒ (b) and (g) ⇒ (a), where $n$ pivots must fill both the $n$ rows and the $n$ columns.*

> [!remark]- Connections
> - Rigorous treatment: for a linear operator on a finite-dimensional space, injective $\Leftrightarrow$ surjective $\Leftrightarrow$ invertible, [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]] (hub [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]]), proved there from the [[Fundamental theorem of linear maps|fundamental theorem of linear maps]] instead of pivot counting; one-sided inverses are two-sided, [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68]].
> - The same phenomenon for functions between finite sets of equal size: injective iff surjective, [[§11 Properties of Finite Sets#^thm-11-7|250 Thm. §11.7]].

> [!remark] Remark: Using the Theorem
> - By [[§14 The Inverse of a Matrix#^thm-14-3|Theorem §14.3]], (g) may be strengthened to "$A\mathbf{x} = \mathbf{b}$ has a *unique* solution for each $\mathbf{b}$ in $\mathbb{R}^n$". That statement certainly implies (b), so it is also equivalent to invertibility.
> - The theorem divides the $n \times n$ matrices into two disjoint classes, invertible (nonsingular) and singular. The *negation* of each statement describes every singular matrix: an $n \times n$ singular matrix is not row equivalent to $I_n$, has fewer than $n$ pivot positions, has linearly dependent columns, and so on.
> - The theorem applies **only to square matrices**. If the columns of a $4 \times 3$ matrix are linearly independent, nothing follows about the existence of solutions of $A\mathbf{x} = \mathbf{b}$.
> - In practice the quickest test is (c): row reduce to an echelon form and count pivots. The lecture calls a pivot in every row the most practical criterion for invertibility.
> - The lecture (L9) defines an $n \times n$ matrix $A$ to be invertible when $AB = I$ for some $n \times n$ matrix $B$, without also asking for $BA = I$. By (k) $\Rightarrow$ (a) this describes the same matrices as Lay's two-sided definition, and [[§16 Characterizations of Invertible Matrices#^cor-16-2|Corollary §16.2]] below shows that such a $B$ is $A^{-1}$.

^rem-16-1

> [!theorem] Corollary §19.1: A One-Sided Inverse Is an Inverse
> Let $A$ and $B$ be square matrices. If $AB = I$, then $A$ and $B$ are both invertible, with $B = A^{-1}$ and $A = B^{-1}$.
>
> *Lay: 2.3 (text)*

^cor-16-2

> [!proof]+ Proof
> $AB = I$ is statement (k) for $A$ (with $D = B$), so $A$ is invertible by [[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]. Multiplying $AB = I$ on the left by $A^{-1}$ gives $B = A^{-1}(AB) = A^{-1}I = A^{-1}$ (Lay's Exercise 8 in Section 2.2). Then $B$ is invertible with $B^{-1} = (A^{-1})^{-1} = A$ by [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](a).

^pf-16-2

*Uses:* [[§16 Characterizations of Invertible Matrices#^thm-16-1|§16.1]], [[§14 The Inverse of a Matrix#^thm-14-4|§14.4]]

> [!example] Example §19.1: Deciding Invertibility
> **(a)** Is $A = \begin{bmatrix} 1 & 0 & -2 \\ 3 & 1 & -2 \\ -5 & -1 & 9 \end{bmatrix}$ invertible?
>
> $$
> A \xrightarrow[R_3 + 5R_1]{R_2 - 3R_1} \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 4 \\ 0 & -1 & -1 \end{bmatrix} \xrightarrow{R_3 + R_2} \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 4 \\ 0 & 0 & 3 \end{bmatrix} .
> $$
>
> $A$ has three pivot positions, so it is invertible by statement (c). There is no need to compute $A^{-1}$.
>
> **(b)** Is $A = \begin{bmatrix} 2 & 3 & 4 \\ 2 & 3 & 4 \\ 2 & 3 & 4 \end{bmatrix}$ invertible? Column 2 is $\tfrac32$ times column 1, so the columns are linearly dependent; statement (e) fails, so $A$ is not invertible. (Equally: $R_2 - R_1$ and $R_3 - R_1$ leave one nonzero row, one pivot.)
>
> **(c)** If $A$ and $B$ are $n \times n$ and $AB\mathbf{x} = \mathbf{0}$ has a nontrivial solution, then statement (d) fails for the square matrix $AB$, so $AB$ is not invertible.
>
> **(d)** If for some $n \times n$ matrix $A$ statement (g) is false, then $A\mathbf{x} = \mathbf{b}$ is inconsistent for at least one $\mathbf{b}$ in $\mathbb{R}^n$, and also, by (d), $A\mathbf{x} = \mathbf{0}$ has nontrivial solutions.
>
> *Lay: Example 2.3.1; 2.3, Practice Problems 1–3*

^ex-16-1

## Invertible Linear Transformations

Matrix multiplication corresponds to composition of linear transformations ([[§12 Matrix Operations#^thm-12-2|Theorem §12.2]]), so the equation $A^{-1}A\mathbf{x} = \mathbf{x}$ says that multiplication by $A^{-1}$ transforms $A\mathbf{x}$ back into $\mathbf{x}$.

> [!definition] Definition §19.1: Invertible Linear Transformation
> A linear transformation $T : \mathbb{R}^n \to \mathbb{R}^n$ is **invertible** if there exists a function $S : \mathbb{R}^n \to \mathbb{R}^n$ such that
>
> $$
> \begin{aligned}
> S(T(\mathbf{x})) &= \mathbf{x} \quad \text{for all } \mathbf{x} \text{ in } \mathbb{R}^n, && (1) \\
> T(S(\mathbf{x})) &= \mathbf{x} \quad \text{for all } \mathbf{x} \text{ in } \mathbb{R}^n . && (2)
> \end{aligned}
> $$
>
> By [[§16 Characterizations of Invertible Matrices#^thm-16-3|Theorem §16.3]] such an $S$ is unique and linear. It is called the **inverse** of $T$ and written $T^{-1}$.
>
> *Lay: 2.3 (text)*

^def-16-1

> [!remark] Remark: Invertible Means One-to-One and Onto
> In the lecture, a function $R : S \to T$ between any two sets is invertible exactly when it is **one-to-one** ($R(s_1) = R(s_2) \Rightarrow s_1 = s_2$) and **onto** (every $t \in T$ is $R(s)$ for some $s$): such a map, called **bijective**, just reshuffles the elements. A map from a 2-element set into a 3-element set cannot be inverted, since some element of the target is not hit and no inverse can send it anywhere consistent; for finite sets, an invertible map forces the two sets to have the same size. For $\mathbf{x} \mapsto A\mathbf{x}$ with $A$ an $m \times n$ matrix:
> - one-to-one means $A\mathbf{x} = A\mathbf{y} \Rightarrow \mathbf{x} = \mathbf{y}$, i.e. $A(\mathbf{x} - \mathbf{y}) = \mathbf{0} \Rightarrow \mathbf{x} - \mathbf{y} = \mathbf{0}$, i.e. $A\mathbf{z} = \mathbf{0}$ only for $\mathbf{z} = \mathbf{0}$: a pivot in every column;
> - onto means $A\mathbf{x} = \mathbf{b}$ is consistent for every $\mathbf{b}$: a pivot in every row.
>
> Both together force $m = n$, and for square $A$ either one alone suffices ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]). (Sets: [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]], invertible means bijective. The lecture's aside on infinite sets, a bijection between $\mathbb{Z}$ and $\mathbb{Q}$ but none between $\mathbb{Z}$ and $\mathbb{R}$, and the Bernstein–Cantor theorem: [[§14 Counting Infinite Sets#^thm-14-10|250 Thm. §14.10]], [[§14a Uncountable Sets#^thm-14a-2|250 Thm. §14a.2]], [[§14a Uncountable Sets#^thm-14a-4|250 Thm. §14a.4]].)
>
> *Source: 235 lectures L6, L8*

^rem-16-2

> [!theorem] Theorem §16.3: Invertible Linear Transformations
> Let $T : \mathbb{R}^n \to \mathbb{R}^n$ be a linear transformation and let $A$ be the standard matrix for $T$. Then $T$ is invertible if and only if $A$ is an invertible matrix. In that case, the linear transformation $S$ given by $S(\mathbf{x}) = A^{-1}\mathbf{x}$ is the unique function satisfying equations (1) and (2).
>
> *Lay: Theorem 9 (2.3)*

^thm-16-3

> [!proof]+ Proof
> **$T$ invertible $\Rightarrow$ $A$ invertible.** Equation (2) shows that $T$ maps $\mathbb{R}^n$ onto $\mathbb{R}^n$: if $\mathbf{b}$ is in $\mathbb{R}^n$ and $\mathbf{x} = S(\mathbf{b})$, then $T(\mathbf{x}) = T(S(\mathbf{b})) = \mathbf{b}$, so each $\mathbf{b}$ is in the range of $T$. Thus $A$ is invertible, by statement (i) of the Invertible Matrix Theorem.
>
> **$A$ invertible $\Rightarrow$ $T$ invertible.** Let $S(\mathbf{x}) = A^{-1}\mathbf{x}$. Then $S$ is a linear transformation (a matrix transformation), and it satisfies (1) and (2):
>
> $$
> S(T(\mathbf{x})) = A^{-1}(A\mathbf{x}) = (A^{-1}A)\mathbf{x} = \mathbf{x}, \qquad T(S(\mathbf{x})) = A(A^{-1}\mathbf{x}) = (AA^{-1})\mathbf{x} = \mathbf{x} .
> $$
>
> **Uniqueness.** (Lay outlines this in Exercise 39.) Suppose $U : \mathbb{R}^n \to \mathbb{R}^n$ also satisfies (1) and (2). Let $\mathbf{v}$ be in $\mathbb{R}^n$. By (2) for $U$, $T(U(\mathbf{v})) = \mathbf{v}$; applying $S$ and using (1) for $S$ at the point $U(\mathbf{v})$,
>
> $$
> U(\mathbf{v}) = S\big(T(U(\mathbf{v}))\big) = S(\mathbf{v}) .
> $$
>
> So $U = S$.

^pf-16-3

*Uses:* [[§16 Characterizations of Invertible Matrices#^def-16-1|Def. §16.1]], [[§16 Characterizations of Invertible Matrices#^thm-16-1|§16.1]], [[§12 Matrix Operations#^thm-12-2|§12.2]], [[§9 Introduction to Linear Transformations#^prop-9-2|§9.2]]

> [!remark]- Connections
> - Rigorous treatment: a linear map is invertible iff it is injective and surjective, and its inverse is then linear, [[§10 Invertibility and Isomorphisms#^ladr-3-63|LADR 3.63]]; for maps between arbitrary sets, [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]] and the uniqueness of the inverse function, [[§9 Injections, Surjections and Bijections#^def-9-5|250 Def. §9.5]].

> [!example] Example §19.2: A One-to-One Transformation of ℝⁿ Is Invertible
> What can be said about a one-to-one linear transformation $T$ from $\mathbb{R}^n$ into $\mathbb{R}^n$?
>
> The columns of the standard matrix $A$ of $T$ are linearly independent ([[§10 The Matrix of a Linear Transformation#^thm-10-3|Theorem §10.3]](b)). So $A$ is invertible by the Invertible Matrix Theorem, statement (e), and then by statement (i) $T$ maps $\mathbb{R}^n$ onto $\mathbb{R}^n$. Also $T$ is invertible, by [[§16 Characterizations of Invertible Matrices#^thm-16-3|Theorem §16.3]].
>
> *Lay: Example 2.3.2*

^ex-16-2

> [!example] Example §19.3: Inverting Geometric Transformations of the Plane
> **Rotation.** The counterclockwise rotation $R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ has $\det R_\theta = \cos^2\theta + \sin^2\theta = 1 \ne 0$, and by [[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]]
>
> $$
> R_\theta^{-1} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} = \begin{bmatrix} \cos(-\theta) & -\sin(-\theta) \\ \sin(-\theta) & \cos(-\theta) \end{bmatrix} = R_{-\theta} .
> $$
>
> This agrees with $R_{-\theta}R_\theta = R_0 = I$ ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|Example §13.1]](b)): the inverse transformation rotates back.
>
> **Shear.** The horizontal shear with matrix $S = \begin{bmatrix} 1 & s \\ 0 & 1 \end{bmatrix}$ moves each point horizontally by $s$ times its height. (The lecture's standard shear, with $s = 1$, sends $(2, 5)$ to $(7, 5)$.) Here $\det S = 1$, and
>
> $$
> S^{-1} = \begin{bmatrix} 1 & -s \\ 0 & 1 \end{bmatrix},
> $$
>
> the shear by $-s$, which slides each point back.
>
> **Dilation.** $rI$ stretches every vector by the factor $r$. For $r \ne 0$ its inverse is $\frac1r I$; for $r = 0$ it is not invertible.
>
> **Projection.** The projection $P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ onto the $x_1$-axis is not one-to-one ($P\mathbf{e}_2 = \mathbf{0} = P\mathbf{0}$) and not onto (its range is the $x_1$-axis), so it is not invertible: $\det P = 0$, and the whole vertical line through a point is flattened to a single point, which cannot be undone.
>
> *Source: 235 lectures L6, L7*

^ex-16-3

> [!remark]- Remark: Numerical Note — Ill-Conditioned Matrices
> In practice one may meet a "nearly singular" or **ill-conditioned** matrix: an invertible matrix that becomes singular if some entries are changed ever so slightly. Row reduction may then produce fewer than $n$ pivots because of roundoff error, and roundoff can also make a singular matrix appear invertible. Matrix programs compute a **condition number** for a square matrix: the larger it is, the closer the matrix is to being singular. The identity matrix has condition number $1$, and a singular matrix has infinite condition number. (Lay defines a condition number through singular values in [[§62★ The Singular Value Decomposition in Applications#^def-62-1|Definition §62.1]].)

^rem-16-3
