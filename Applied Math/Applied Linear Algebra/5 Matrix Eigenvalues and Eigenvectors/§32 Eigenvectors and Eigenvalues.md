---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 32
lay: "5.1"
aliases: ["Lay 5.1"]
tags: [applied-linear-algebra, math235]
---
← [[§31 Applications to Markov Chains]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§33 The Characteristic Equation]] →

*Lay, Section 5.1 · MATH 235 lectures L18, L19.*

A matrix transformation $\mathbf{x} \mapsto A\mathbf{x}$ may move vectors in all sorts of directions, but usually there are special directions that it only stretches, shrinks or reverses: vectors with $A\mathbf{x} = \lambda\mathbf{x}$. These are the eigenvectors, and the scale factors $\lambda$ are the eigenvalues. Once $\lambda$ is known, the eigenvectors are the nonzero vectors of the null space $\operatorname{Nul}(A - \lambda I)$, found by row reduction. This section proves the two basic facts used throughout Chapter 5: the eigenvalues of a triangular matrix are its diagonal entries, and eigenvectors for distinct eigenvalues are linearly independent. It ends with the reason eigenvectors matter for applications: on an eigenvector the powers $A^k$ act as the numbers $\lambda^k$, which solves difference equations such as the Fibonacci recursion.

## Eigenvectors and Eigenvalues

> [!remark] Remark: Motivation — Iterating a Matrix
> The lecture starts with the question of what the powers $A, A^2, A^3, \ldots$ of a matrix do. For $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$,
>
> $$
> A^2 = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix} = \begin{bmatrix} 1 + 8 & 2 + 6 \\ 4 + 12 & 8 + 9 \end{bmatrix} = \begin{bmatrix} 9 & 8 \\ 16 & 17 \end{bmatrix} .
> $$
>
> Since all entries are positive, $A$ maps the closed first quadrant $\mathbb{R}^2_+$ into itself, onto the narrower wedge between the rays through its columns $A\mathbf{e}_1 = (1, 4)$ and $A\mathbf{e}_2 = (2, 3)$. Then $A^2(\mathbb{R}^2_+)$ is the still narrower wedge between $(9, 16)$ and $(8, 17)$, and so on: the wedges $A^N(\mathbb{R}^2_+)$ close down onto a single ray. A vector $\mathbf{u}$ on that ray is mapped to a vector on the same ray, $A\mathbf{u} = \lambda\mathbf{u}$. (Here the ray is spanned by $(1, 2)$, with $\lambda = 5$: see [[§32 Eigenvectors and Eigenvalues#^ex-32-5|Example §32.5]].)
>
> *Source: 235 lecture L18*

^rem-32-1

> [!remark]- Remark: The Perron–Frobenius Theorem
> The lecture states the general fact behind the shrinking wedges, without proof: if $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ with $a, b, c, d > 0$, then there are a vector $\mathbf{u} = (u_1, u_2)$ with $u_1, u_2 > 0$ and a number $\lambda > 0$ such that $A\mathbf{u} = \lambda\mathbf{u}$. In L21 a sharper form is stated for matrices with positive entries whose columns sum to $1$: the eigenvalue $1$ has a one-dimensional eigenspace spanned by a vector with positive entries, and every other eigenvalue has absolute value less than $1$. This explains the convergence of regular Markov chains ([[§31 Applications to Markov Chains|§31]], Theorem 18); see [[§34 Diagonalization#^ex-34-5|Example §34.5]].
>
> *Source: 235 lectures L18, L21*

^rem-32-2

> [!definition] Definition §32.1: Eigenvector and Eigenvalue
> An **eigenvector** of an $n \times n$ matrix $A$ is a nonzero vector $\mathbf{x}$ such that $A\mathbf{x} = \lambda\mathbf{x}$ for some scalar $\lambda$. A scalar $\lambda$ is called an **eigenvalue** of $A$ if there is a nontrivial solution $\mathbf{x}$ of $A\mathbf{x} = \lambda\mathbf{x}$; such an $\mathbf{x}$ is called an *eigenvector corresponding to $\lambda$*.
>
> An eigenvector must be nonzero, by definition, but an eigenvalue may be zero ([[§32 Eigenvectors and Eigenvalues#^thm-32-2|Theorem §32.2]]).
>
> *Lay: 5.1, Definition*

^def-32-1

> [!remark]- Connections
> - Rigorous treatment: [[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]] (eigenvalue), [[§14 Invariant Subspaces#^ladr-5-8|LADR 5.8]] (eigenvector) and [[§14 Invariant Subspaces#^ladr-5-7|LADR 5.7]] ($\lambda$ is an eigenvalue $\Leftrightarrow$ $T - \lambda I$ is not injective $\Leftrightarrow$ not invertible); there for an operator $T$ on any finite-dimensional $V$, where an eigenvector spans a one-dimensional invariant subspace.

> [!example] Example §32.1: Checking Eigenvectors and Eigenvalues
> Let $A = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}$, $\mathbf{u} = \begin{bmatrix} 6 \\ -5 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$.
>
> **(a) Are $\mathbf{u}$ and $\mathbf{v}$ eigenvectors of $A$?** Multiply:
>
> $$
> A\mathbf{u} = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}\begin{bmatrix} 6 \\ -5 \end{bmatrix} = \begin{bmatrix} 6 - 30 \\ 30 - 10 \end{bmatrix} = \begin{bmatrix} -24 \\ 20 \end{bmatrix} = -4\begin{bmatrix} 6 \\ -5 \end{bmatrix} = -4\mathbf{u}, \qquad
> A\mathbf{v} = \begin{bmatrix} 3 - 12 \\ 15 - 4 \end{bmatrix} = \begin{bmatrix} -9 \\ 11 \end{bmatrix} .
> $$
>
> So $\mathbf{u}$ is an eigenvector corresponding to the eigenvalue $-4$. But $(-9, 11)$ is not a multiple of $(3, -2)$ (a multiple $c(3, -2)$ with $3c = -9$ has $c = -3$, and then $-2c = 6 \ne 11$), so $\mathbf{v}$ is not an eigenvector.
>
> **(b) Show that $7$ is an eigenvalue of $A$, and find the corresponding eigenvectors.** $7$ is an eigenvalue if and only if $A\mathbf{x} = 7\mathbf{x}$ has a nontrivial solution. This equation is equivalent to $A\mathbf{x} - 7\mathbf{x} = \mathbf{0}$, that is,
>
> $$
> (A - 7I)\mathbf{x} = \mathbf{0}, \qquad A - 7I = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix} - \begin{bmatrix} 7 & 0 \\ 0 & 7 \end{bmatrix} = \begin{bmatrix} -6 & 6 \\ 5 & -5 \end{bmatrix} .
> $$
>
> The columns of $A - 7I$ are obviously linearly dependent, so this homogeneous system has nontrivial solutions, and $7$ *is* an eigenvalue. Row reduce:
>
> $$
> \begin{bmatrix} -6 & 6 & 0 \\ 5 & -5 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & -1 & 0 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The general solution is $x_1 = x_2$, $x_2$ free, that is, $\mathbf{x} = x_2\begin{bmatrix} 1 \\ 1 \end{bmatrix}$. Each such vector with $x_2 \ne 0$ is an eigenvector corresponding to $\lambda = 7$.
>
> *Lay: Examples 5.1.2 and 5.1.3*

^ex-32-1

> [!remark] Remark: Warning — Row Reduction Does Not Find Eigenvalues
> Row reduction was used in Example §32.1 to find eigen*vectors*, once the eigenvalue was known. It cannot be used to find eigen*values*: an echelon form of $A$ usually does not display the eigenvalues of $A$, because row operations change them. (The tool for eigenvalues is the characteristic equation, [[§33 The Characteristic Equation#^thm-33-4|Theorem §33.4]].)
>
> *Lay: 5.1 (text)*

^rem-32-3

The equivalence of $A\mathbf{x} = 7\mathbf{x}$ and $(A - 7I)\mathbf{x} = \mathbf{0}$ in Example §32.1 holds for any $\lambda$ in place of $7$: $\lambda$ is an eigenvalue of $A$ if and only if

$$
(A - \lambda I)\mathbf{x} = \mathbf{0} \qquad (3)
$$

has a nontrivial solution.

> [!definition] Definition §32.2: Eigenspace
> Let $\lambda$ be an eigenvalue of the $n \times n$ matrix $A$. The set of all solutions of $(A - \lambda I)\mathbf{x} = \mathbf{0}$ is the null space $\operatorname{Nul}(A - \lambda I)$, so it is a subspace of $\mathbb{R}^n$ ([[§24 Null Spaces, Column Spaces, and Linear Transformations|§24]], Theorem 2). It is called the **eigenspace** of $A$ corresponding to $\lambda$. The eigenspace consists of the zero vector and all the eigenvectors corresponding to $\lambda$.
>
> *Lay: 5.1 (text)*

^def-32-2

For the matrix of Example §32.1, the eigenspace for $\lambda = 7$ consists of all multiples of $(1, 1)$, the line through $(1, 1)$ and the origin. From part (a), the eigenspace for $\lambda = -4$ is the line through $(6, -5)$.

![[m235-32-1.svg]]
*The two eigenspaces of $A = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}$. On the line through $(1, 1)$ (blue) the transformation $\mathbf{x} \mapsto A\mathbf{x}$ is multiplication by $7$; on the line through $(6, -5)$ (red) it is multiplication by $-4$, which reverses direction. Every other vector, such as $\mathbf{v} = (3, -2)$ (gray), is moved off its own line: $A\mathbf{v} = (-9, 11)$.*

> [!example] Example §32.2: A Two-Dimensional Eigenspace
> Let $A = \begin{bmatrix} 4 & -1 & 6 \\ 2 & 1 & 6 \\ 2 & -1 & 8 \end{bmatrix}$. An eigenvalue of $A$ is $2$. Find a basis for the corresponding eigenspace.
>
> Form
>
> $$
> A - 2I = \begin{bmatrix} 4 & -1 & 6 \\ 2 & 1 & 6 \\ 2 & -1 & 8 \end{bmatrix} - \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix} = \begin{bmatrix} 2 & -1 & 6 \\ 2 & -1 & 6 \\ 2 & -1 & 6 \end{bmatrix}
> $$
>
> and row reduce the augmented matrix for $(A - 2I)\mathbf{x} = \mathbf{0}$ (subtract row 1 from rows 2 and 3):
>
> $$
> \begin{bmatrix} 2 & -1 & 6 & 0 \\ 2 & -1 & 6 & 0 \\ 2 & -1 & 6 & 0 \end{bmatrix} \sim \begin{bmatrix} 2 & -1 & 6 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The system has free variables, which confirms that $2$ is an eigenvalue. The single equation $2x_1 - x_2 + 6x_3 = 0$ gives $x_1 = \tfrac12 x_2 - 3x_3$, so
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_2\begin{bmatrix} 1/2 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}, \qquad x_2, x_3 \text{ free.}
> $$
>
> The eigenspace is a two-dimensional subspace of $\mathbb{R}^3$ (a plane through the origin, on which $A$ acts as the dilation $\mathbf{x} \mapsto 2\mathbf{x}$). Scaling the first vector by $2$, a basis is
>
> $$
> \left\{ \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}, \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix} \right\} .
> $$
>
> Check: $A(1, 2, 0) = (4 - 2, 2 + 2, 2 - 2) = (2, 4, 0)$ and $A(-3, 0, 1) = (-12 + 6, -6 + 6, -6 + 8) = (-6, 0, 2)$.
>
> *Lay: Example 5.1.4*

^ex-32-2

> [!remark] Remark: Method — The Eigenspace for a Known Eigenvalue
> 1. Form $A - \lambda I$: subtract $\lambda$ from each diagonal entry of $A$.
> 2. Row reduce the augmented matrix $[\,A - \lambda I \;\; \mathbf{0}\,]$. If there is no free variable, $\lambda$ is *not* an eigenvalue.
> 3. Write the general solution in parametric vector form; the vectors multiplying the free variables form a basis of the eigenspace $\operatorname{Nul}(A - \lambda I)$ ([[§24 Null Spaces, Column Spaces, and Linear Transformations|§24]]).
> 4. Check one vector $\mathbf{v}$ of the basis: $A\mathbf{v} = \lambda\mathbf{v}$.
>
> This is a good method by hand. With a matrix program it usually works too but is not entirely reliable: roundoff error can produce an echelon form with the wrong number of pivots. The best programs compute approximate eigenvalues and eigenvectors simultaneously (see [[§39 Iterative Estimates for Eigenvalues|§39]]).
>
> *Lay: 5.1, Numerical Note*

^rem-32-4

> [!theorem] Theorem §32.1: Eigenvalues of a Triangular Matrix
> The eigenvalues of a triangular matrix are the entries on its main diagonal.
>
> *Lay: Theorem 1 (5.1)*

^thm-32-1

> [!proof]+ Proof
> **Upper triangular.** (Lay writes the $3 \times 3$ case.) Let $A = [a_{ij}]$ be upper triangular, $n \times n$. Then
>
> $$
> A - \lambda I = \begin{bmatrix} a_{11} - \lambda & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} - \lambda & \cdots & a_{2n} \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} - \lambda \end{bmatrix}
> $$
>
> is upper triangular too. The scalar $\lambda$ is an eigenvalue of $A$ if and only if $(A - \lambda I)\mathbf{x} = \mathbf{0}$ has a nontrivial solution, that is, a free variable. Because of the zero entries, this happens if and only if at least one diagonal entry of $A - \lambda I$ is zero (Lay: "it is easy to see"; here is why).
> - If all diagonal entries $a_{kk} - \lambda$ are nonzero, $A - \lambda I$ is already an echelon form with a pivot in every column, so there is no free variable.
> - If $a_{kk} - \lambda = 0$ for some $k$, look at the first $k$ columns of $A - \lambda I$. Column $j$ has zeros below row $j$, and column $k$ also has a zero in row $k$. So all of the first $k$ columns have zeros in rows $k, \ldots, n$. Deleting those rows leaves $k$ vectors in $\mathbb{R}^{k-1}$, which are linearly dependent ([[§7 Linear Independence|§7]], Theorem 8); the same weights give a linear dependence among the first $k$ columns of $A - \lambda I$. So the columns of $A - \lambda I$ are linearly dependent, and $(A - \lambda I)\mathbf{x} = \mathbf{0}$ has a nontrivial solution.
>
> So $\lambda$ is an eigenvalue exactly when $\lambda$ equals one of $a_{11}, \ldots, a_{nn}$.
>
> **Lower triangular** (Lay's Exercises 27–28). Since $(A - \lambda I)^T = A^T - \lambda I$ and a square matrix is invertible if and only if its transpose is (Invertible Matrix Theorem), $A - \lambda I$ fails to be invertible exactly when $A^T - \lambda I$ does. So $A$ and $A^T$ have the same eigenvalues. If $A$ is lower triangular, $A^T$ is upper triangular with the same diagonal, and the first part applies.

^pf-32-1

*Uses:* [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]], [[§7 Linear Independence|§7]] (Theorem 8: more vectors than entries are dependent), [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8, the Invertible Matrix Theorem: (c), (d), (l))

> [!example] Example §32.3: Eigenvalues by Inspection
> Let $A = \begin{bmatrix} 3 & 6 & -8 \\ 0 & 0 & 6 \\ 0 & 0 & 2 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 0 & 0 \\ -2 & 1 & 0 \\ 5 & 3 & 4 \end{bmatrix}$. By Theorem §32.1, the eigenvalues of the upper triangular $A$ are $3$, $0$ and $2$, and the eigenvalues of the lower triangular $B$ are $4$ and $1$ (the diagonal entry $4$ occurs twice, but it is one eigenvalue).
>
> Since $0$ is an eigenvalue of $A$, $A\mathbf{x} = \mathbf{0}$ has a nontrivial solution, and $A$ is not invertible (Theorem §32.2 below). Indeed, its second column is $2$ times its first.
>
> *Lay: Example 5.1.5*

^ex-32-3

> [!theorem] Theorem §32.2: Zero as an Eigenvalue
> An $n \times n$ matrix $A$ has $0$ as an eigenvalue if and only if $A$ is not invertible.
>
> *Lay: 5.1 (text)*

^thm-32-2

> [!proof]+ Proof
> $0$ is an eigenvalue if and only if $A\mathbf{x} = 0\mathbf{x}$ has a nontrivial solution. But $A\mathbf{x} = 0\mathbf{x}$ is the equation $A\mathbf{x} = \mathbf{0}$, which has a nontrivial solution if and only if $A$ is not invertible, by the Invertible Matrix Theorem (statements (a) and (d)).

^pf-32-2

*Uses:* [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8, the Invertible Matrix Theorem)

This fact is added to the Invertible Matrix Theorem in [[§33 The Characteristic Equation#^thm-33-2|Theorem §33.2]].

The next theorem is needed throughout the chapter. Its proof is a typical calculation with eigenvectors, and it proves "If $P$ then $Q$" by showing that $P$ together with the negation of $Q$ leads to a contradiction.

> [!theorem] Theorem §32.3: Eigenvectors for Distinct Eigenvalues Are Independent
> If $\mathbf{v}_1, \ldots, \mathbf{v}_r$ are eigenvectors that correspond to distinct eigenvalues $\lambda_1, \ldots, \lambda_r$ of an $n \times n$ matrix $A$, then the set $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ is linearly independent.
>
> *Lay: Theorem 2 (5.1)*

^thm-32-3

> [!proof]+ Proof
> Suppose $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ is linearly dependent. Since $\mathbf{v}_1$ is nonzero, one of the vectors in the set is a linear combination of the preceding vectors ([[§7 Linear Independence|§7]], Theorem 7). Let $p$ be the least index such that $\mathbf{v}_{p+1}$ is a linear combination of the preceding vectors; by the minimality of $p$, the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_p$ are linearly independent (otherwise Theorem 7 would apply to them and give a smaller index). Then there are scalars $c_1, \ldots, c_p$ with
>
> $$
> c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p = \mathbf{v}_{p+1} . \qquad (5)
> $$
>
> Multiply both sides of (5) by $A$ and use $A\mathbf{v}_k = \lambda_k\mathbf{v}_k$ for each $k$:
>
> $$
> c_1\lambda_1\mathbf{v}_1 + \cdots + c_p\lambda_p\mathbf{v}_p = \lambda_{p+1}\mathbf{v}_{p+1} . \qquad (6)
> $$
>
> Multiply both sides of (5) by $\lambda_{p+1}$ and subtract the result from (6):
>
> $$
> c_1(\lambda_1 - \lambda_{p+1})\mathbf{v}_1 + \cdots + c_p(\lambda_p - \lambda_{p+1})\mathbf{v}_p = \mathbf{0} . \qquad (7)
> $$
>
> Since $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is linearly independent, the weights in (7) are all zero. None of the factors $\lambda_i - \lambda_{p+1}$ is zero, because the eigenvalues are distinct. Hence $c_i = 0$ for $i = 1, \ldots, p$. But then (5) says that $\mathbf{v}_{p+1} = \mathbf{0}$, which is impossible for an eigenvector. Hence $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ cannot be linearly dependent, and therefore it is linearly independent.

^pf-32-3

*Uses:* [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]], [[§7 Linear Independence|§7]] (Theorem 7: characterization of linearly dependent sets)

> [!remark]- Remark: A Second Proof (Vandermonde)
> The lecture proves the case $r = 3$ differently. Suppose $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$ (1). Applying $A$ once and twice gives
>
> $$
> \lambda_1c_1\mathbf{v}_1 + \lambda_2c_2\mathbf{v}_2 + \lambda_3c_3\mathbf{v}_3 = \mathbf{0} \quad (2), \qquad \lambda_1^2c_1\mathbf{v}_1 + \lambda_2^2c_2\mathbf{v}_2 + \lambda_3^2c_3\mathbf{v}_3 = \mathbf{0} \quad (3).
> $$
>
> Equations (1)–(3) say, row by row, that
>
> $$
> \begin{bmatrix} c_1\mathbf{v}_1 & c_2\mathbf{v}_2 & c_3\mathbf{v}_3 \end{bmatrix} V^T = 0, \qquad V = \begin{bmatrix} 1 & 1 & 1 \\ \lambda_1 & \lambda_2 & \lambda_3 \\ \lambda_1^2 & \lambda_2^2 & \lambda_3^2 \end{bmatrix} ,
> $$
>
> where $V$ is the **Vandermonde matrix**, with $\det V = (\lambda_2 - \lambda_1)(\lambda_3 - \lambda_1)(\lambda_3 - \lambda_2) \ne 0$ (the Vandermonde determinant; for $3 \times 3$ it can be checked by row reduction). Multiplying on the right by $(V^T)^{-1}$ gives $c_1\mathbf{v}_1 = c_2\mathbf{v}_2 = c_3\mathbf{v}_3 = \mathbf{0}$, and since the $\mathbf{v}_i$ are nonzero, $c_1 = c_2 = c_3 = 0$. The same works for any $r$, with the $r \times r$ Vandermonde matrix. (The lecture writes the matrix of the $c_i\mathbf{v}_i$ on the right of $V$; the product is formed with the columns of $V$ as weights, which is the transposed arrangement above.)
>
> *Source: 235 lecture L19*

^rem-32-5

> [!theorem] Corollary §32.4: At Most n Eigenvalues
> An $n \times n$ matrix has at most $n$ distinct eigenvalues.
>
> *Source: 235 lecture L19 (Lay: Exercise 5.1.23)*

^cor-32-4

> [!proof]+ Proof
> If $\lambda_1, \ldots, \lambda_r$ are distinct eigenvalues of $A$, choose an eigenvector $\mathbf{v}_i$ for each. By Theorem §32.3, $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ is a linearly independent set in $\mathbb{R}^n$, so $r \le n$ ([[§7 Linear Independence|§7]], Theorem 8). (The lecture gives a second reason: the eigenvalues are the roots of a polynomial of degree $n$, [[§33 The Characteristic Equation#^thm-33-5|Theorem §33.5]], and such a polynomial has at most $n$ roots.)

^pf-32-4

*Uses:* [[§32 Eigenvectors and Eigenvalues#^thm-32-3|§32.3]], [[§7 Linear Independence|§7]] (Theorem 8)

> [!remark]- Connections
> - Rigorous treatment: [[§14 Invariant Subspaces#^ladr-5-11|LADR 5.11]] (eigenvectors for distinct eigenvalues are linearly independent; Axler's proof is the same minimal-counterexample argument) and [[§14 Invariant Subspaces#^ladr-5-12|LADR 5.12]] (at most $\dim V$ eigenvalues). In Axler's terms the eigenspaces form a direct sum, [[§17 Diagonalizable Operators#^ladr-5-54|LADR 5.54]].
> - The Vandermonde determinant of the second proof: [[§34 Determinants#^ladr-9-67|LADR 9.67]].

## Eigenvectors and Difference Equations

Let $A$ be $n \times n$. The **first-order difference equation**

$$
\mathbf{x}_{k+1} = A\mathbf{x}_k \qquad (k = 0, 1, 2, \ldots) \qquad (8)
$$

is a recursive description of a sequence $\{\mathbf{x}_k\}$ in $\mathbb{R}^n$. A **solution** of (8) is an explicit description of $\{\mathbf{x}_k\}$ whose formula for each $\mathbf{x}_k$ does not depend directly on $A$ or on the preceding terms other than the initial term $\mathbf{x}_0$. (Iterating (8) gives $\mathbf{x}_k = A^k\mathbf{x}_0$, but this is not yet a solution: it still requires computing $A^k$.)

> [!theorem] Theorem §32.5: Eigenvector Solutions of a Difference Equation
> If $\mathbf{x}_0$ is an eigenvector of $A$ with eigenvalue $\lambda$, then
>
> $$
> \mathbf{x}_k = \lambda^k\mathbf{x}_0 \qquad (k = 0, 1, 2, \ldots) \qquad (9)
> $$
>
> is a solution of $\mathbf{x}_{k+1} = A\mathbf{x}_k$; equivalently, $A^k\mathbf{x}_0 = \lambda^k\mathbf{x}_0$ for all $k$. More generally, if $\mathbf{u}$ and $\mathbf{v}$ are eigenvectors with eigenvalues $\lambda$ and $\mu$, and $c_1, c_2$ are scalars, then
>
> $$
> \mathbf{x}_k = c_1\lambda^k\mathbf{u} + c_2\mu^k\mathbf{v}
> $$
>
> is a solution, with $\mathbf{x}_0 = c_1\mathbf{u} + c_2\mathbf{v}$. The same holds for linear combinations of any number of eigenvectors.
>
> *Lay: 5.1, Equation (9); Exercise 5.1.33; Practice Problem 5.1.2*

^thm-32-5

> [!proof]+ Proof
> For (9): $A\mathbf{x}_k = A(\lambda^k\mathbf{x}_0) = \lambda^k(A\mathbf{x}_0) = \lambda^k(\lambda\mathbf{x}_0) = \lambda^{k+1}\mathbf{x}_0 = \mathbf{x}_{k+1}$. Since $\mathbf{x}_0 = \lambda^0\mathbf{x}_0$ is the given initial term, induction on $k$ gives $A^k\mathbf{x}_0 = \mathbf{x}_k = \lambda^k\mathbf{x}_0$.
>
> For the combination: by linearity of $\mathbf{x} \mapsto A\mathbf{x}$,
>
> $$
> A\mathbf{x}_k = c_1\lambda^kA\mathbf{u} + c_2\mu^kA\mathbf{v} = c_1\lambda^{k+1}\mathbf{u} + c_2\mu^{k+1}\mathbf{v} = \mathbf{x}_{k+1} ,
> $$
>
> and the same computation works with more terms.

^pf-32-5

*Uses:* [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]]

So if $\mathbf{x}_0$ can be written as a combination of eigenvectors, the difference equation is solved. This is the idea of the rest of the chapter ([[§34 Diagonalization|§34]], [[§37 Discrete Dynamical Systems|§37]]). The lecture uses it to find a formula for the Fibonacci numbers. Finding the eigenvalues uses the characteristic equation $\det(A - \lambda I) = 0$ of the next section: $A - \lambda I$ has a nonzero null space exactly when it is not invertible, that is, when its determinant is $0$ ([[§33 The Characteristic Equation#^thm-33-4|Theorem §33.4]]).

> [!example] Example §32.4: The Fibonacci Numbers and the Golden Ratio
> The Fibonacci numbers are $F_0 = 0$, $F_1 = 1$ and $F_n = F_{n-1} + F_{n-2}$: $0, 1, 1, 2, 3, 5, 8, 13, 21, \ldots$. The ratios $\frac{2}{1}, \frac{3}{2}, \frac{5}{3}, \frac{8}{5}, \frac{13}{8}, \frac{21}{13}, \ldots$ seem to approach the **golden ratio** $\varphi = \frac{1 + \sqrt5}{2} \approx 1.618$ (the ratio $a/b$ of a segment cut into $a > b$ with $\frac{a}{b} = \frac{a + b}{a}$). We find a formula for $F_n$ and prove $\lim_{n\to\infty} F_{n+1}/F_n = \varphi$.
>
> **A difference equation.** Let $\mathbf{v}_n = \begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix}$, so $\mathbf{v}_0 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Then
>
> $$
> \mathbf{v}_n = \begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix} = \begin{bmatrix} F_n \\ F_{n-1} + F_n \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} F_{n-1} \\ F_n \end{bmatrix} = A\mathbf{v}_{n-1}, \qquad A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix},
> $$
>
> so $\mathbf{v}_n = A^n\mathbf{v}_0$, and we need $A^n\mathbf{v}_0$.
>
> **Eigenvalues.** $\det(A - \lambda I) = \det\begin{bmatrix} -\lambda & 1 \\ 1 & 1 - \lambda \end{bmatrix} = -\lambda(1 - \lambda) - 1 = \lambda^2 - \lambda - 1$, whose roots are
>
> $$
> \lambda = \frac{1 \pm \sqrt5}{2} : \qquad \varphi = \frac{1 + \sqrt5}{2}, \qquad \psi = \frac{1 - \sqrt5}{2} .
> $$
>
> Note $\varphi + \psi = 1$, $\varphi\psi = -1$, $\varphi - \psi = \sqrt5$, and $\varphi^2 = \varphi + 1$, $\psi^2 = \psi + 1$.
>
> **Eigenvectors.** $A - \varphi I = \begin{bmatrix} -\varphi & 1 \\ 1 & 1 - \varphi \end{bmatrix}$. Its second row times $\varphi$ is $(\varphi, \varphi - \varphi^2) = (\varphi, -1)$, the negative of the first row, so the rows are proportional, as they must be, and the system reduces to $-\varphi u_1 + u_2 = 0$. Taking $u_1 = 1$: $\mathbf{u} = \begin{bmatrix} 1 \\ \varphi \end{bmatrix}$. In the same way $\mathbf{v} = \begin{bmatrix} 1 \\ \psi \end{bmatrix}$ is an eigenvector for $\psi$.
>
> **Decompose $\mathbf{v}_0$.** $\mathbf{u} - \mathbf{v} = \begin{bmatrix} 0 \\ \varphi - \psi \end{bmatrix} = \sqrt5\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \sqrt5\,\mathbf{v}_0$, so $\mathbf{v}_0 = \frac{1}{\sqrt5}(\mathbf{u} - \mathbf{v})$. By Theorem §32.5,
>
> $$
> \mathbf{v}_n = A^n\mathbf{v}_0 = \frac{1}{\sqrt5}\big(\varphi^n\mathbf{u} - \psi^n\mathbf{v}\big) = \frac{1}{\sqrt5}\begin{bmatrix} \varphi^n - \psi^n \\ \varphi^{n+1} - \psi^{n+1} \end{bmatrix} .
> $$
>
> The first entry is **Binet's formula**
>
> $$
> F_n = \frac{\varphi^n - \psi^n}{\sqrt5} = \frac{1}{\sqrt5}\left[\Big(\frac{1 + \sqrt5}{2}\Big)^n - \Big(\frac{1 - \sqrt5}{2}\Big)^n\right] .
> $$
>
> Check: $F_0 = \frac{1 - 1}{\sqrt5} = 0$, $F_1 = \frac{\varphi - \psi}{\sqrt5} = \frac{\sqrt5}{\sqrt5} = 1$, and since $\varphi^2 = \frac{6 + 2\sqrt5}{4}$, $\psi^2 = \frac{6 - 2\sqrt5}{4}$, $F_2 = \frac{1}{\sqrt5}\cdot\frac{4\sqrt5}{4} = 1$.
>
> **The ratio.** $\varphi > 1$ and $|\psi| = \frac{\sqrt5 - 1}{2} \approx 0.618 < 1$, so $\psi^n \to 0$ and $F_n \approx \varphi^n/\sqrt5$ for large $n$ (in fact $F_n$ is the integer nearest to $\varphi^n/\sqrt5$, since $|\psi^n/\sqrt5| < \frac12$). Precisely,
>
> $$
> \frac{F_{n+1}}{F_n} = \frac{\varphi^{n+1} - \psi^{n+1}}{\varphi^n - \psi^n} = \frac{\varphi - \psi(\psi/\varphi)^n}{1 - (\psi/\varphi)^n} \to \varphi \qquad (n \to \infty),
> $$
>
> because $|\psi/\varphi| < 1$.
>
> *The lecture writes $F_0 = 1$ at one point and lists $\mathbf{v}_2, \mathbf{v}_3$ with their entries in reverse order; with $\mathbf{v}_0 = (0, 1)$, as used for the formula, the indexing is $F_0 = 0$, $F_1 = F_2 = 1$.*
>
> *Source: 235 lecture L18*

^ex-32-4

> [!example] Example §32.5: A Power Applied to a Vector
> Let $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$. Find $A^{10}\begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
>
> **Eigenvalues.** $\det(A - \lambda I) = (1 - \lambda)(3 - \lambda) - 8 = \lambda^2 - 4\lambda - 5 = (\lambda - 5)(\lambda + 1)$, so the eigenvalues are $5$ and $-1$.
>
> **Eigenvectors.** For $\lambda = 5$: $A - 5I = \begin{bmatrix} -4 & 2 \\ 4 & -2 \end{bmatrix}$, and $-4u_1 + 2u_2 = 0$ gives $\mathbf{u} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$. For $\lambda = -1$: $A + I = \begin{bmatrix} 2 & 2 \\ 4 & 4 \end{bmatrix}$, and $2v_1 + 2v_2 = 0$ gives $\mathbf{v} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
>
> **Decompose.** $\mathbf{u} + 2\mathbf{v} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}$, so $\mathbf{e}_1 = \frac13(\mathbf{u} + 2\mathbf{v})$. By Theorem §32.5, $A^{10}\mathbf{u} = 5^{10}\mathbf{u}$ and $A^{10}\mathbf{v} = (-1)^{10}\mathbf{v} = \mathbf{v}$, so
>
> $$
> A^{10}\mathbf{e}_1 = \frac13\big(5^{10}\mathbf{u} + 2\mathbf{v}\big) = \frac13\left(5^{10}\begin{bmatrix} 1 \\ 2 \end{bmatrix} + 2\begin{bmatrix} 1 \\ -1 \end{bmatrix}\right) = \begin{bmatrix} (5^{10} + 2)/3 \\ (2\cdot 5^{10} - 2)/3 \end{bmatrix} = \begin{bmatrix} 3\,255\,209 \\ 6\,510\,416 \end{bmatrix} .
> $$
>
> The second entry is almost exactly twice the first: $A^{10}\mathbf{e}_1$ lies almost on the eigenvector line through $(1, 2)$, as the shrinking wedges of [[§32 Eigenvectors and Eigenvalues#^rem-32-1|Remark: Motivation]] predict.
>
> *The lecture writes $A\mathbf{u} = 5^{10}\mathbf{u}$ for $A^{10}\mathbf{u} = 5^{10}\mathbf{u}$.*
>
> *Source: 235 lecture L18*

^ex-32-5
