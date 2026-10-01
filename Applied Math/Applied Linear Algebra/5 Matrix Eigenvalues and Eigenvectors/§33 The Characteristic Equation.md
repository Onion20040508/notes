---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 33
lay: "5.2"
aliases: ["Lay 5.2"]
tags: [applied-linear-algebra, math235]
---
← [[§32 Eigenvectors and Eigenvalues]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§34 Diagonalization]] →

*Lay, Section 5.2 · MATH 235 lectures L18, L19, L20.*

The equation $A\mathbf{x} = \lambda\mathbf{x}$ has two unknowns, $\lambda$ and $\mathbf{x}$. The determinant removes $\mathbf{x}$: $\lambda$ is an eigenvalue exactly when $A - \lambda I$ is not invertible, that is, when $\det(A - \lambda I) = 0$. This scalar equation, the characteristic equation, is a polynomial equation of degree $n$, and its roots are the eigenvalues, each with a multiplicity. The section also introduces similarity, $B = P^{-1}AP$: similar matrices have the same characteristic polynomial, hence the same eigenvalues. An application shows how the eigenvalues govern the long-term behavior of a Markov chain.

> [!example] Example §33.1: Eigenvalues of a 2 × 2 Matrix
> Find the eigenvalues of $A = \begin{bmatrix} 2 & 3 \\ 3 & -6 \end{bmatrix}$.
>
> We need all scalars $\lambda$ such that $(A - \lambda I)\mathbf{x} = \mathbf{0}$ has a nontrivial solution. By the Invertible Matrix Theorem, this means that the matrix
>
> $$
> A - \lambda I = \begin{bmatrix} 2 & 3 \\ 3 & -6 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix} = \begin{bmatrix} 2 - \lambda & 3 \\ 3 & -6 - \lambda \end{bmatrix}
> $$
>
> is *not* invertible, and a $2 \times 2$ matrix fails to be invertible precisely when its determinant $ad - bc$ is zero ([[§12 The Inverse of a Matrix|§12]], Theorem 4). So the eigenvalues are the solutions of
>
> $$
> \det(A - \lambda I) = (2 - \lambda)(-6 - \lambda) - (3)(3) = -12 + 6\lambda - 2\lambda + \lambda^2 - 9 = \lambda^2 + 4\lambda - 21 = (\lambda - 3)(\lambda + 7) = 0 .
> $$
>
> The eigenvalues of $A$ are $3$ and $-7$.
>
> *Lay: Example 5.2.1*

^ex-33-1

The determinant has turned the matrix equation $(A - \lambda I)\mathbf{x} = \mathbf{0}$, with two unknowns $\lambda$ and $\mathbf{x}$, into the scalar equation $\lambda^2 + 4\lambda - 21 = 0$ with one unknown. The same works for $n \times n$ matrices, using the following facts about determinants.

## Determinants

> [!theorem] Theorem §33.1: Determinant from an Echelon Form
> Let $A$ be an $n \times n$ matrix, let $U$ be any echelon form obtained from $A$ by row replacements and row interchanges (without scaling), and let $r$ be the number of row interchanges. Then $\det A$ is $(-1)^r$ times the product of the diagonal entries $u_{11}, \ldots, u_{nn}$ of $U$. If $A$ is invertible, the $u_{ii}$ are all pivots; otherwise at least $u_{nn}$ is zero. Thus
>
> $$
> \det A = \begin{cases} (-1)^r \cdot \big(\text{product of pivots in } U\big), & \text{when } A \text{ is invertible}, \\ 0, & \text{when } A \text{ is not invertible}. \end{cases} \qquad (1)
> $$
>
> It is a remarkable and nontrivial fact that every such echelon form gives the same value. For example, $A = \begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix}$ reduces with one interchange to $U_1 = \begin{bmatrix} 1 & 5 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -1 \end{bmatrix}$, giving $(-1)^1(1)(-2)(-1) = -2$, and without interchanges (adding $-\tfrac13$ times row 2 to row 3) to $U_2 = \begin{bmatrix} 1 & 5 & 0 \\ 0 & -6 & -1 \\ 0 & 0 & 1/3 \end{bmatrix}$, giving $(-1)^0(1)(-6)(\tfrac13) = -2$.
>
> *Lay: 5.2, Equation (1); Example 5.2.2*

^thm-33-1

*Proved in [[§21 Properties of Determinants|§21]] (Lay 3.2, formula (1) after Theorem 3). Readers who skip Chapter 3 may take (1) as the definition of $\det A$.*

> [!theorem] Theorem §33.2: The Invertible Matrix Theorem (Continued)
> Let $A$ be an $n \times n$ matrix. Then $A$ is invertible if and only if:
>
> s. The number $0$ is *not* an eigenvalue of $A$.
>
> t. The determinant of $A$ is *not* zero.
>
> These continue the list of equivalent statements (a)–(r) of [[§28 Rank|§28]] (Lay 4.6).
>
> *Lay: 5.2, The Invertible Matrix Theorem (continued)*

^thm-33-2

> [!proof]+ Proof
> (s) is [[§32 Eigenvectors and Eigenvalues#^thm-32-2|Theorem §32.2]]. (t): by formula (1), $\det A \ne 0$ if and only if $A$ is invertible, since for invertible $A$ the pivots are nonzero.

^pf-33-2

*Uses:* [[§32 Eigenvectors and Eigenvalues#^thm-32-2|§32.2]], [[§33 The Characteristic Equation#^thm-33-1|§33.1]]

When $A$ is $3 \times 3$, $|\det A|$ is the volume of the parallelepiped determined by the columns $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ ([[§22 Cramer’s Rule, Volume, and Linear Transformations|§22]]). This volume is nonzero exactly when the columns are linearly independent, in which case $A$ is invertible.

> [!theorem] Theorem §33.3: Properties of Determinants
> Let $A$ and $B$ be $n \times n$ matrices.
>
> a. $A$ is invertible if and only if $\det A \ne 0$.
>
> b. $\det AB = (\det A)(\det B)$.
>
> c. $\det A^T = \det A$.
>
> d. If $A$ is triangular, then $\det A$ is the product of the entries on the main diagonal of $A$.
>
> e. A row replacement operation on $A$ does not change the determinant. A row interchange changes the sign of the determinant. A row scaling also scales the determinant by the same scalar factor.
>
> *Lay: Theorem 3 (5.2)*

^thm-33-3

*Lay collects these from Chapter 3 for reference: (d) is Theorem 2 of [[§20 Introduction to Determinants|§20]] (Lay 3.1), and (e), (a), (c), (b) are Theorems 3–6 of [[§21 Properties of Determinants|§21]] (Lay 3.2), where they are proved.*

## The Characteristic Equation

> [!definition] Definition §33.1: Characteristic Equation and Characteristic Polynomial
> Let $A$ be an $n \times n$ matrix. The scalar equation
>
> $$
> \det(A - \lambda I) = 0
> $$
>
> is called the **characteristic equation** of $A$. Its left side $\det(A - \lambda I)$ is a polynomial in $\lambda$ of degree $n$ (Theorem §33.5), called the **characteristic polynomial** of $A$. The lecture writes $f_A(\lambda) = \det(A - \lambda I_n)$; other common notations are $p_A$ and $\chi_A$.
>
> *Lay: 5.2 (text)*

^def-33-1

> [!theorem] Theorem §33.4: Eigenvalues Are the Roots of the Characteristic Equation
> A scalar $\lambda$ is an eigenvalue of an $n \times n$ matrix $A$ if and only if $\lambda$ satisfies the characteristic equation
>
> $$
> \det(A - \lambda I) = 0 .
> $$
>
> *Lay: 5.2, boxed statement*

^thm-33-4

> [!proof]+ Proof
> $\lambda$ is an eigenvalue of $A$ if and only if $(A - \lambda I)\mathbf{x} = \mathbf{0}$ has a nontrivial solution ([[§32 Eigenvectors and Eigenvalues#^def-32-2|equation (3) of §32]]), if and only if $A - \lambda I$ is not invertible (Invertible Matrix Theorem, (a) $\Leftrightarrow$ (d)), if and only if $\det(A - \lambda I) = 0$ (Theorem §33.3(a)). In the lecture's words: $\lambda$ is an eigenvalue $\Leftrightarrow$ $\operatorname{Nul}(A - \lambda I) \ne \{\mathbf{0}\}$ $\Leftrightarrow$ $\det(A - \lambda I) = 0$.

^pf-33-4

*Uses:* [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]], [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8, the Invertible Matrix Theorem), [[§33 The Characteristic Equation#^thm-33-3|§33.3]]

> [!theorem] Theorem §33.5: The Characteristic Polynomial Has Degree n
> If $A$ is an $n \times n$ matrix, then $\det(A - \lambda I)$ is a polynomial in $\lambda$ of degree $n$. More precisely,
>
> $$
> \det(A - \lambda I) = (-\lambda)^n + (\operatorname{tr} A)(-\lambda)^{n-1} + \cdots + \det A ,
> $$
>
> where $\operatorname{tr} A = a_{11} + a_{22} + \cdots + a_{nn}$ is the **trace** of $A$ (the sum of its diagonal entries). For $n = 2$ this is the whole polynomial:
>
> $$
> \det\begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = (a - \lambda)(d - \lambda) - bc = \lambda^2 - (\operatorname{tr} A)\lambda + \det A .
> $$
>
> *Lay: 5.2 (text, "it can be shown"); the trace form: Source: 235 lecture L19*

^thm-33-5

*Lay omits the proof; see [[§34 Determinants#^ladr-9-65|LADR 9.65]] (characteristic polynomial, trace and determinant). Here is a direct argument by cofactor expansion.*

> [!proof]- Proof
> **A degree bound.** Call a square matrix *linear in $\lambda$* if each entry is a polynomial in $\lambda$ of degree at most $1$. *Claim:* if $M$ is $k \times k$, linear in $\lambda$, and $\lambda$ occurs in at most $m$ of its rows, then $\det M$ is a polynomial of degree at most $m$. Induction on $k$; $k = 1$ is clear. If $m < k$, expand along a row without $\lambda$: $\det M$ is a combination, with constant coefficients, of determinants of $(k-1) \times (k-1)$ submatrices in which $\lambda$ occurs in at most $m$ rows, each of degree $\le m$. If $m = k$, expand along the first row: each term is an entry of degree $\le 1$ times the determinant of a submatrix in which $\lambda$ occurs in at most $k - 1$ rows, so each term has degree $\le k$.
>
> **The leading terms.** Induction on $n$; for $n = 1$, $\det(A - \lambda I) = a_{11} - \lambda$. For $n \ge 2$, expand $\det(A - \lambda I)$ along the first row:
>
> $$
> \det(A - \lambda I) = (a_{11} - \lambda)\det(A_{11} - \lambda I_{n-1}) + \sum_{j=2}^n (-1)^{1+j}a_{1j}\det M_{1j} ,
> $$
>
> where $A_{11}$ is $A$ with row 1 and column 1 deleted and $M_{1j}$ is $A - \lambda I$ with row 1 and column $j$ deleted. In $A - \lambda I$, $\lambda$ occurs only in the diagonal entries. Deleting row $1$ and column $j \ne 1$ removes the two diagonal entries in positions $(1, 1)$ and $(j, j)$, so $\lambda$ occurs in at most $n - 2$ rows of $M_{1j}$, and $\det M_{1j}$ has degree $\le n - 2$ by the claim. By induction, $\det(A_{11} - \lambda I_{n-1}) = (-\lambda)^{n-1} + (a_{22} + \cdots + a_{nn})(-\lambda)^{n-2} + (\text{degree} \le n - 3)$. Multiplying by $a_{11} - \lambda$,
>
> $$
> \det(A - \lambda I) = (-\lambda)^n + (a_{11} + a_{22} + \cdots + a_{nn})(-\lambda)^{n-1} + (\text{degree} \le n - 2) .
> $$
>
> **The constant term** of a polynomial is its value at $0$: $\det(A - 0I) = \det A$.

^pf-33-5

*Uses:* [[§20 Introduction to Determinants|§20]] (Theorem 1: cofactor expansion across any row)

> [!definition] Definition §33.2: Multiplicity of an Eigenvalue
> The **(algebraic) multiplicity** of an eigenvalue $\lambda$ is its multiplicity as a root of the characteristic equation, that is, the number of times the factor $(\lambda - \text{eigenvalue})$ occurs in the characteristic polynomial. The eigenvalues are sometimes listed repeated according to their multiplicities.
>
> *Lay: 5.2 (text)*

^def-33-2

> [!remark]- Connections
> - Rigorous treatment: Axler defines the characteristic polynomial without determinants, as $\prod (z - \lambda_k)^{d_k}$ with $d_k = \dim G(\lambda_k, T)$ the dimension of the generalized eigenspace ([[§29 Generalized Eigenspace Decomposition#^ladr-8-23|LADR 8.23]], [[§29 Generalized Eigenspace Decomposition#^ladr-8-26|LADR 8.26]]), and only later shows it equals $\det(zI - T)$ ([[§34 Determinants#^ladr-9-62|LADR 9.62]]). Note $\det(zI - A) = (-1)^n\det(A - zI)$: Axler's version is monic, Lay's has leading coefficient $(-1)^n$; the roots and multiplicities are the same.

> [!example] Example §33.2: Multiplicities
> **(a)** Find the characteristic equation of $A = \begin{bmatrix} 5 & -2 & 6 & -1 \\ 0 & 3 & -8 & 0 \\ 0 & 0 & 5 & 4 \\ 0 & 0 & 0 & 1 \end{bmatrix}$.
>
> $A - \lambda I$ is upper triangular, so by Theorem §33.3(d)
>
> $$
> \det(A - \lambda I) = \det\begin{bmatrix} 5 - \lambda & -2 & 6 & -1 \\ 0 & 3 - \lambda & -8 & 0 \\ 0 & 0 & 5 - \lambda & 4 \\ 0 & 0 & 0 & 1 - \lambda \end{bmatrix} = (5 - \lambda)(3 - \lambda)(5 - \lambda)(1 - \lambda) .
> $$
>
> The characteristic equation is $(\lambda - 5)^2(\lambda - 3)(\lambda - 1) = 0$, or, expanded, $\lambda^4 - 14\lambda^3 + 68\lambda^2 - 130\lambda + 75 = 0$. The eigenvalue $5$ has multiplicity $2$; $3$ and $1$ have multiplicity $1$. (Check of the expansion: $(\lambda - 5)^2 = \lambda^2 - 10\lambda + 25$ and $(\lambda - 3)(\lambda - 1) = \lambda^2 - 4\lambda + 3$; their product is $\lambda^4 - 14\lambda^3 + (3 + 40 + 25)\lambda^2 - (30 + 100)\lambda + 75$.)
>
> **(b)** The characteristic polynomial of a $6 \times 6$ matrix is $\lambda^6 - 4\lambda^5 - 12\lambda^4$. Find the eigenvalues and their multiplicities.
>
> Factor: $\lambda^6 - 4\lambda^5 - 12\lambda^4 = \lambda^4(\lambda^2 - 4\lambda - 12) = \lambda^4(\lambda - 6)(\lambda + 2)$. The eigenvalues are $0$ (multiplicity $4$), $6$ (multiplicity $1$) and $-2$ (multiplicity $1$), listed with multiplicities as $0, 0, 0, 0, 6, -2$. Since $0$ is an eigenvalue, the matrix is not invertible (Theorem §33.2(s)).
>
> *Lay: Examples 5.2.3 and 5.2.4*

^ex-33-2

> [!remark] Remark: Complex Roots and Numerical Practice
> A polynomial of degree $n$ has at most $n$ roots: if $p(r) = 0$, then $p(\lambda) = (\lambda - r)q(\lambda)$ with $\deg q = n - 1$ (lecture L19). By the **Fundamental Theorem of Algebra**, every polynomial $\lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0$ factors as $(\lambda - r_1)\cdots(\lambda - r_n)$ with $r_1, \ldots, r_n$ possibly complex. So the characteristic equation of an $n \times n$ matrix has exactly $n$ roots, counting multiplicities, provided complex roots are allowed. For $n = 2$ the roots of $\lambda^2 + c_1\lambda + c_0$ are $\frac{-c_1 \pm \sqrt D}{2}$ with $D = c_1^2 - 4c_0$, complex when $D < 0$. Complex eigenvalues are studied in [[§36 Complex Eigenvalues|§36]]; until then, scalars are real.
>
> In practice, eigenvalues of matrices larger than $2 \times 2$ are found by computer, unless the matrix is triangular or otherwise special: a $3 \times 3$ characteristic polynomial is easy to compute but may be hard to factor. There is no formula or finite algorithm for the roots of a general polynomial of degree $n \ge 5$, and good numerical methods avoid the characteristic polynomial altogether (MATLAB computes it *from* the eigenvalues). Several of them, such as the QR algorithm and Jacobi's method $A_{k+1} = P_k^{-1}A_kP_k$, are built on Theorem §33.6 below; others are in [[§39 Iterative Estimates for Eigenvalues|§39]].
>
> *Lay: 5.2 (text); Numerical Notes*

^rem-33-1

> [!example] Example §33.3: A 3 × 3 Characteristic Polynomial
> Find the eigenvalues of $A = \begin{bmatrix} 2 & 2 & 1 \\ 1 & 3 & 1 \\ 1 & 2 & 2 \end{bmatrix}$.
>
> **The polynomial.** By the $3 \times 3$ diagonal rule (or cofactor expansion),
>
> $$
> \begin{aligned}
> \det(A - \lambda I) &= \det\begin{bmatrix} 2 - \lambda & 2 & 1 \\ 1 & 3 - \lambda & 1 \\ 1 & 2 & 2 - \lambda \end{bmatrix} \\
> &= (2 - \lambda)(3 - \lambda)(2 - \lambda) + 2 + 2 - (3 - \lambda) - 2(2 - \lambda) - 2(2 - \lambda) \\
> &= (2 - \lambda)^2(3 - \lambda) - 7 + 5\lambda .
> \end{aligned}
> $$
>
> Since $(2 - \lambda)^2(3 - \lambda) = (4 - 4\lambda + \lambda^2)(3 - \lambda) = -\lambda^3 + 7\lambda^2 - 16\lambda + 12$, the characteristic polynomial is
>
> $$
> -\lambda^3 + 7\lambda^2 - 11\lambda + 5 .
> $$
>
> (Checks: the coefficient of $(-\lambda)^2$ is $7 = \operatorname{tr} A$, and the constant term is $5 = \det A$, as in Theorem §33.5.)
>
> **The roots.** Try small integer divisors of $5$: at $\lambda = 1$, $-1 + 7 - 11 + 5 = 0$. Dividing by $\lambda - 1$,
>
> $$
> -\lambda^3 + 7\lambda^2 - 11\lambda + 5 = (\lambda - 1)(-\lambda^2 + 6\lambda - 5) = -(\lambda - 1)(\lambda - 1)(\lambda - 5) = -(\lambda - 1)^2(\lambda - 5) .
> $$
>
> The eigenvalues are $1$ (multiplicity $2$) and $5$ (multiplicity $1$). The eigenspaces are found in [[§34 Diagonalization#^ex-34-4|Example §34.4]].
>
> *The lecture's expansion of the determinant contains a slip (it reaches $-\lambda^3 + 2\lambda^2 - 6\lambda + 5$, which does not vanish at $5$); its final factorization $(\lambda - 1)(-\lambda + 1)(\lambda - 5)$ is correct.*
>
> *Source: 235 lectures L19, L20 (Lay: Exercise 5.3.5)*

^ex-33-3

## Similarity

> [!definition] Definition §33.3: Similar Matrices
> If $A$ and $B$ are $n \times n$ matrices, then $A$ is **similar to** $B$ if there is an invertible matrix $P$ such that $P^{-1}AP = B$, or, equivalently, $A = PBP^{-1}$. Writing $Q = P^{-1}$, we have $Q^{-1}BQ = A$, so $B$ is also similar to $A$, and we say simply that $A$ and $B$ are **similar**. Changing $A$ into $P^{-1}AP$ is called a **similarity transformation**.
>
> *Lay: 5.2 (text)*

^def-33-3

> [!theorem] Theorem §33.6: Similar Matrices Have the Same Characteristic Polynomial
> If $n \times n$ matrices $A$ and $B$ are similar, then they have the same characteristic polynomial and hence the same eigenvalues (with the same multiplicities).
>
> *Lay: Theorem 4 (5.2)*

^thm-33-6

> [!proof]+ Proof
> If $B = P^{-1}AP$, then, since $P^{-1}P = I$,
>
> $$
> B - \lambda I = P^{-1}AP - \lambda P^{-1}P = P^{-1}(AP - \lambda P) = P^{-1}(A - \lambda I)P .
> $$
>
> Using the multiplicative property, Theorem §33.3(b),
>
> $$
> \det(B - \lambda I) = \det\big[P^{-1}(A - \lambda I)P\big] = \det(P^{-1}) \cdot \det(A - \lambda I) \cdot \det(P) . \qquad (2)
> $$
>
> Since $\det(P^{-1}) \cdot \det(P) = \det(P^{-1}P) = \det I = 1$, equation (2) gives $\det(B - \lambda I) = \det(A - \lambda I)$. Equal polynomials have the same roots with the same multiplicities, so by Theorem §33.4 the eigenvalues agree.

^pf-33-6

*Uses:* [[§33 The Characteristic Equation#^thm-33-3|§33.3]] (b), [[§33 The Characteristic Equation#^thm-33-4|§33.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-52|LADR 9.52]] (determinant is a similarity invariant) and, for the meaning of similarity, [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]] (change-of-basis formula $A = C^{-1}BC$): similar matrices are the matrices of one operator in two bases, as [[§35 Eigenvectors and Linear Transformations|§35]] shows. The trace is also a similarity invariant: [[§31 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR 8.50]].

> [!remark] Remark: Warnings
> 1. **The converse of Theorem §33.6 is false.** $\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$ and $\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ both have characteristic polynomial $(\lambda - 2)^2$, but they are not similar: $P^{-1}(2I)P = 2I$ for every invertible $P$, so $2I$ is similar only to itself.
> 2. **Similarity is not row equivalence.** If $A$ is row equivalent to $B$, then $B = EA$ for some invertible $E$ (a product of elementary matrices), whereas similarity requires $B = P^{-1}AP$. Row operations usually change the eigenvalues. The lecture's extreme case is $n = 1$: a $1 \times 1$ matrix $[a]$ is similar only to itself ($p^{-1}ap = a$), while any two nonzero $1 \times 1$ matrices, such as $[5]$ and $[-7]$, are row equivalent.
>
> *Lay: 5.2, Warnings; Source: 235 lecture L20*

^rem-33-2

> [!theorem] Proposition §33.7: Eigenvectors of Similar Matrices
> If $A = PBP^{-1}$ and $A\mathbf{u} = \lambda\mathbf{u}$ with $\mathbf{u} \ne \mathbf{0}$, then $B(P^{-1}\mathbf{u}) = \lambda(P^{-1}\mathbf{u})$ and $P^{-1}\mathbf{u} \ne \mathbf{0}$. So $P^{-1}$ maps the eigenspace of $A$ for $\lambda$ onto the eigenspace of $B$ for $\lambda$ (with inverse $P$). In particular, if $A$ is similar to $B$ and $A$ is diagonalizable, so is $B$ ([[§34 Diagonalization|§34]]).
>
> *Source: 235 lecture L20*

^prop-33-7

> [!proof]+ Proof
> From $PBP^{-1}\mathbf{u} = \lambda\mathbf{u}$, multiply both sides on the left by $P^{-1}$: $B(P^{-1}\mathbf{u}) = \lambda P^{-1}\mathbf{u}$. Since $P^{-1}$ is invertible and $\mathbf{u} \ne \mathbf{0}$, $P^{-1}\mathbf{u} \ne \mathbf{0}$. Exchanging the roles of $A$ and $B$ (with $B = P^{-1}AP$), $P$ maps eigenvectors of $B$ for $\lambda$ to eigenvectors of $A$ for $\lambda$, so the two linear maps $P^{-1}$ and $P$ are inverse to each other between the two eigenspaces. For the last statement: $A$ diagonalizable means $A = QDQ^{-1}$ with $D$ diagonal; then $B = P^{-1}AP = (P^{-1}Q)D(P^{-1}Q)^{-1}$.

^pf-33-7

*Uses:* [[§33 The Characteristic Equation#^def-33-3|Def. §33.3]], [[§32 Eigenvectors and Eigenvalues#^def-32-2|Def. §32.2]]

## Application to Dynamical Systems

> [!example] Example §33.4: Long-Term Behavior of a Markov Chain
> Let $A = \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix}$. Analyze the long-term behavior of the dynamical system $\mathbf{x}_{k+1} = A\mathbf{x}_k$ ($k = 0, 1, 2, \ldots$) with $\mathbf{x}_0 = \begin{bmatrix} .6 \\ .4 \end{bmatrix}$.
>
> **Eigenvalues.** The characteristic equation is
>
> $$
> 0 = \det\begin{bmatrix} .95 - \lambda & .03 \\ .05 & .97 - \lambda \end{bmatrix} = (.95 - \lambda)(.97 - \lambda) - (.03)(.05) = \lambda^2 - 1.92\lambda + .92 .
> $$
>
> By the quadratic formula,
>
> $$
> \lambda = \frac{1.92 \pm \sqrt{(1.92)^2 - 4(.92)}}{2} = \frac{1.92 \pm \sqrt{.0064}}{2} = \frac{1.92 \pm .08}{2} = 1 \ \text{ or } \ .92 .
> $$
>
> **Eigenvectors.** $A\begin{bmatrix} 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 2.85 + .15 \\ .15 + 4.85 \end{bmatrix} = \begin{bmatrix} 3 \\ 5 \end{bmatrix}$ and $A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} .92 \\ -.92 \end{bmatrix}$, so $\mathbf{v}_1 = (3, 5)$ and $\mathbf{v}_2 = (1, -1)$ are eigenvectors for $\lambda = 1$ and $\lambda = .92$.
>
> **Decompose $\mathbf{x}_0$.** $\{\mathbf{v}_1, \mathbf{v}_2\}$ is a basis for $\mathbb{R}^2$ (two vectors that are not multiples of each other; or by [[§32 Eigenvectors and Eigenvalues#^thm-32-3|Theorem §32.3]]). So $\mathbf{x}_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = [\,\mathbf{v}_1 \;\; \mathbf{v}_2\,]\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$ with
>
> $$
> \begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 5 & -1 \end{bmatrix}^{-1}\begin{bmatrix} .60 \\ .40 \end{bmatrix} = \frac{1}{-8}\begin{bmatrix} -1 & -1 \\ -5 & 3 \end{bmatrix}\begin{bmatrix} .60 \\ .40 \end{bmatrix} = \frac{1}{-8}\begin{bmatrix} -1 \\ -1.8 \end{bmatrix} = \begin{bmatrix} .125 \\ .225 \end{bmatrix} . \qquad (4)
> $$
>
> **Solve.** By linearity and $A\mathbf{v}_1 = \mathbf{v}_1$, $A\mathbf{v}_2 = .92\mathbf{v}_2$: $\mathbf{x}_1 = c_1\mathbf{v}_1 + c_2(.92)\mathbf{v}_2$, $\mathbf{x}_2 = c_1\mathbf{v}_1 + c_2(.92)^2\mathbf{v}_2$, and in general ([[§32 Eigenvectors and Eigenvalues#^thm-32-5|Theorem §32.5]])
>
> $$
> \mathbf{x}_k = .125\begin{bmatrix} 3 \\ 5 \end{bmatrix} + .225(.92)^k\begin{bmatrix} 1 \\ -1 \end{bmatrix} \qquad (k = 0, 1, 2, \ldots) . \qquad (5)
> $$
>
> As $k \to \infty$, $(.92)^k \to 0$, so $\mathbf{x}_k \to .125\mathbf{v}_1 = \begin{bmatrix} .375 \\ .625 \end{bmatrix}$.
>
> $A$ is the city–suburb migration matrix of [[§31 Applications to Markov Chains|§31]], and $\mathbf{x}_k$ is the population distribution after $k$ years. Theorem 18 of that section said that $\mathbf{x}_k$ tends to a steady-state vector; formula (5) shows why: the steady-state vector $.125\mathbf{v}_1$ is an eigenvector for $\lambda = 1$, and the other component dies out like $(.92)^k$.
>
> *Lay: Example 5.2.5*

^ex-33-4
