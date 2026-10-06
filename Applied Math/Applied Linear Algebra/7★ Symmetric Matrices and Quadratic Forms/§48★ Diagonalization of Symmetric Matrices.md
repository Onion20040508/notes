---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 7
section: 48
lay: "7.1"
aliases: ["Lay 7.1"]
tags: [applied-linear-algebra, math235, extension]
---
← [[§47 Applications of Inner Product Spaces]] · ↑ [[· 7★ Symmetric Matrices and Quadratic Forms]] · [[§49★ Quadratic Forms]] →

*Lay, Section 7.1.*
★ *Beyond MATH 235: the course ended with inner products (Ch. 6); Chapter 7 is included from Lay as the continuation.*

Chapter 5 left the question of which matrices are diagonalizable without a simple answer. For symmetric matrices the answer is as good as it can be: every symmetric matrix is diagonalizable, its eigenvalues are real, and its eigenvectors can be chosen orthonormal, so that $A = PDP^T$ with $P$ orthogonal. This is the Spectral Theorem. Conversely, only symmetric matrices have such a factorization. Writing $PDP^T$ out column by column expresses $A$ as a weighted sum of projections onto its eigenvector lines, the spectral decomposition. Everything else in Chapter 7 (quadratic forms, constrained optimization, the singular value decomposition, principal component analysis) is built on this section.

## Symmetric Matrices

> [!definition] Definition §48.1: Symmetric Matrix
> A **symmetric** matrix is a matrix $A$ such that $A^T = A$. Such a matrix is necessarily square. Its main diagonal entries are arbitrary, but its other entries occur in pairs, on opposite sides of the main diagonal: $a_{ij} = a_{ji}$.
>
> For example, the first three matrices below are symmetric and the last three are not:
>
> $$
> \begin{bmatrix} 1 & 0 \\ 0 & -3 \end{bmatrix}, \quad
> \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & 8 \\ 0 & 8 & -7 \end{bmatrix}, \quad
> \begin{bmatrix} a & b & c \\ b & d & e \\ c & e & f \end{bmatrix};
> \qquad
> \begin{bmatrix} 1 & -3 \\ 3 & 0 \end{bmatrix}, \quad
> \begin{bmatrix} 1 & -4 & 0 \\ -6 & 1 & -4 \\ 0 & -6 & 1 \end{bmatrix}, \quad
> \begin{bmatrix} 5 & 4 & 3 & 2 \\ 4 & 3 & 2 & 1 \\ 3 & 2 & 1 & 0 \end{bmatrix}.
> $$
>
> The last one is not even square.
>
> *Lay: 7.1, Definition; Example 7.1.1*

^def-48-1

> [!example] Example §48.1: Diagonalizing a Symmetric Matrix with Distinct Eigenvalues
> If possible, diagonalize $A = \begin{bmatrix} 6 & -2 & -1 \\ -2 & 6 & -1 \\ -1 & -1 & 5 \end{bmatrix}$.
>
> **Eigenvalues.** Expanding $\det(A - \lambda I)$ gives the characteristic equation
>
> $$
> 0 = -\lambda^3 + 17\lambda^2 - 90\lambda + 144 = -(\lambda - 8)(\lambda - 6)(\lambda - 3) .
> $$
>
> **Eigenvectors.** Row reduce $A - \lambda I$ for each eigenvalue:
>
> $$
> A - 8I = \begin{bmatrix} -2 & -2 & -1 \\ -2 & -2 & -1 \\ -1 & -1 & -3 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \mathbf{v}_1 = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix};
> \qquad
> A - 6I = \begin{bmatrix} 0 & -2 & -1 \\ -2 & 0 & -1 \\ -1 & -1 & -1 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 1/2 \\ 0 & 1 & 1/2 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \mathbf{v}_2 = \begin{bmatrix} -1 \\ -1 \\ 2 \end{bmatrix};
> $$
>
> $$
> A - 3I = \begin{bmatrix} 3 & -2 & -1 \\ -2 & 3 & -1 \\ -1 & -1 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}.
> $$
>
> (For $\lambda = 6$ the free variable $x_3 = 2$ was chosen to clear fractions.) Three eigenvectors for distinct eigenvalues form a basis of $\mathbb{R}^3$, so $A$ is diagonalizable. But more is true: $\mathbf{v}_1 \cdot \mathbf{v}_2 = 1 - 1 + 0 = 0$, $\mathbf{v}_1 \cdot \mathbf{v}_3 = -1 + 1 + 0 = 0$, $\mathbf{v}_2 \cdot \mathbf{v}_3 = -1 - 1 + 2 = 0$, so $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is an *orthogonal* basis of $\mathbb{R}^3$. Normalize:
>
> $$
> \mathbf{u}_1 = \begin{bmatrix} -1/\sqrt2 \\ 1/\sqrt2 \\ 0 \end{bmatrix}, \quad
> \mathbf{u}_2 = \begin{bmatrix} -1/\sqrt6 \\ -1/\sqrt6 \\ 2/\sqrt6 \end{bmatrix}, \quad
> \mathbf{u}_3 = \begin{bmatrix} 1/\sqrt3 \\ 1/\sqrt3 \\ 1/\sqrt3 \end{bmatrix},
> \qquad
> P = \begin{bmatrix} -1/\sqrt2 & -1/\sqrt6 & 1/\sqrt3 \\ 1/\sqrt2 & -1/\sqrt6 & 1/\sqrt3 \\ 0 & 2/\sqrt6 & 1/\sqrt3 \end{bmatrix}, \quad
> D = \begin{bmatrix} 8 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 3 \end{bmatrix}.
> $$
>
> Then $A = PDP^{-1}$ as in the Diagonalization Theorem ([[§34 Diagonalization#^thm-34-1|Theorem §34.1]]). This time $P$ is square with orthonormal columns, so $P$ is an orthogonal matrix and $P^{-1}$ is simply $P^T$ ([[§41 Orthogonal Sets#^thm-41-4|Theorem §41.4]]). Thus $A = PDP^T$.
>
> *Lay: Example 7.1.2*

^ex-48-1

The orthogonality of the eigenvectors in Example §48.1 is no accident: they belong to distinct eigenvalues of a symmetric matrix.

> [!theorem] Theorem §48.1: Eigenvectors of a Symmetric Matrix Are Orthogonal
> If $A$ is symmetric, then any two eigenvectors from different eigenspaces are orthogonal.
>
> *Lay: Theorem 1 (7.1)*

^thm-48-1

> [!proof]+ Proof
> Let $\mathbf{v}_1$ and $\mathbf{v}_2$ be eigenvectors that correspond to distinct eigenvalues $\lambda_1 \ne \lambda_2$. To show $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$, write the dot product as a matrix product, $\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^T \mathbf{y}$, and compute
>
> $$
> \begin{aligned}
> \lambda_1 \mathbf{v}_1 \cdot \mathbf{v}_2 &= (\lambda_1 \mathbf{v}_1)^T \mathbf{v}_2 = (A\mathbf{v}_1)^T \mathbf{v}_2 && \text{since } \mathbf{v}_1 \text{ is an eigenvector} \\
> &= (\mathbf{v}_1^T A^T) \mathbf{v}_2 = \mathbf{v}_1^T (A \mathbf{v}_2) && \text{since } A^T = A \\
> &= \mathbf{v}_1^T (\lambda_2 \mathbf{v}_2) && \text{since } \mathbf{v}_2 \text{ is an eigenvector} \\
> &= \lambda_2 \mathbf{v}_1^T \mathbf{v}_2 = \lambda_2 \mathbf{v}_1 \cdot \mathbf{v}_2 .
> \end{aligned}
> $$
>
> Hence $(\lambda_1 - \lambda_2)\, \mathbf{v}_1 \cdot \mathbf{v}_2 = 0$. But $\lambda_1 - \lambda_2 \ne 0$, so $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$.

^pf-48-1

*Uses:* [[§48★ Diagonalization of Symmetric Matrices#^def-48-1|Def. §48.1]], [[§11 Matrix Operations#^thm-11-7|§11.7]] ($(AB)^T = B^T A^T$), [[§40 Inner Product, Length, and Orthogonality#^def-40-1|Def. §40.1]] (the inner product $\mathbf{u}^T \mathbf{v}$)

> [!remark]- Connections
> - Rigorous treatment: [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]] proves the same for eigenvectors of any normal operator ($T^*T = TT^*$) on a real or complex inner product space; symmetric matrices are the self-adjoint operators on $\mathbb{R}^n$ ([[§22 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]), and the one-line computation above is $\langle T v_1, v_2 \rangle = \langle v_1, T v_2 \rangle$.
> - PDE version: [[§23 Sturm–Liouville Problems#^thm-23-2|341 Thm. §23.2]] (eigenfunctions of a Sturm–Liouville problem for different eigenvalues are orthogonal with weight $p$); the self-adjoint differential operator plays the part of the symmetric matrix, [[§23 Sturm–Liouville Problems#^rem-23-3|341 Remark: Self-Adjointness]].

> [!definition] Definition §48.2: Orthogonally Diagonalizable
> An $n \times n$ matrix $A$ is **orthogonally diagonalizable** if there are an orthogonal matrix $P$ (with $P^{-1} = P^T$) and a diagonal matrix $D$ such that
>
> $$
> A = PDP^T = PDP^{-1} . \qquad (1)
> $$
>
> Such a diagonalization requires $n$ linearly independent and orthonormal eigenvectors (the columns of $P$).
>
> *Lay: 7.1, Definition and Equation (1)*

^def-48-2

> [!theorem] Theorem §48.2: Orthogonally Diagonalizable Means Symmetric
> An $n \times n$ matrix $A$ is orthogonally diagonalizable if and only if $A$ is a symmetric matrix.
>
> *Lay: Theorem 2 (7.1)*

^thm-48-2

> [!proof]+ Proof
> **Orthogonally diagonalizable ⟹ symmetric.** If $A = PDP^T$ as in (1), then, since $D^T = D$ for a diagonal matrix and $(P^T)^T = P$,
>
> $$
> A^T = (PDP^T)^T = P^{TT} D^T P^T = PDP^T = A .
> $$
>
> **Symmetric ⟹ orthogonally diagonalizable.** This is the hard direction. Lay omits its proof here ("much harder"); it is part (d) of the Spectral Theorem, [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|Theorem §48.3]], proved below from Lay's hints.

^pf-48-2

*Uses:* [[§48★ Diagonalization of Symmetric Matrices#^def-48-2|Def. §48.2]], [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|§48.3]] (d), [[§11 Matrix Operations#^thm-11-7|§11.7]] (transpose of a product)

This is a remarkable statement: in Chapter 5 there was no way to tell at a glance whether a matrix is diagonalizable, but for symmetric matrices one look suffices.

> [!example] Example §48.2: A Repeated Eigenvalue
> Orthogonally diagonalize $A = \begin{bmatrix} 3 & -2 & 4 \\ -2 & 6 & 2 \\ 4 & 2 & 3 \end{bmatrix}$, whose characteristic equation is
>
> $$
> 0 = -\lambda^3 + 12\lambda^2 - 21\lambda - 98 = -(\lambda - 7)^2(\lambda + 2) .
> $$
>
> **Eigenspaces.** For $\lambda = 7$:
>
> $$
> A - 7I = \begin{bmatrix} -4 & -2 & 4 \\ -2 & -1 & 2 \\ 4 & 2 & -4 \end{bmatrix} \sim \begin{bmatrix} 1 & 1/2 & -1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix},
> \qquad x_1 = -\tfrac12 x_2 + x_3 ,
> $$
>
> with two free variables, giving the basis $\mathbf{v}_1 = (1, 0, 1)$ ($x_2 = 0$, $x_3 = 1$) and $\mathbf{v}_2 = (-1/2, 1, 0)$ ($x_2 = 1$, $x_3 = 0$). For $\lambda = -2$:
>
> $$
> A + 2I = \begin{bmatrix} 5 & -2 & 4 \\ -2 & 8 & 2 \\ 4 & 2 & 5 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1/2 \\ 0 & 0 & 0 \end{bmatrix}
> \ \Rightarrow\ \mathbf{v}_3 = \begin{bmatrix} -1 \\ -1/2 \\ 1 \end{bmatrix}.
> $$
>
> **Orthogonalize inside the eigenspace.** $\mathbf{v}_1$ and $\mathbf{v}_2$ are linearly independent but not orthogonal ($\mathbf{v}_2 \cdot \mathbf{v}_1 = -1/2$). Replace $\mathbf{v}_2$ by its component orthogonal to $\mathbf{v}_1$ ([[§41 Orthogonal Sets#^def-41-3|Definition §41.3]], orthogonal projection onto a line):
>
> $$
> \mathbf{z}_2 = \mathbf{v}_2 - \frac{\mathbf{v}_2 \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1} \mathbf{v}_1 = \begin{bmatrix} -1/2 \\ 1 \\ 0 \end{bmatrix} - \frac{-1/2}{2} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -1/4 \\ 1 \\ 1/4 \end{bmatrix}.
> $$
>
> $\mathbf{z}_2$ is a linear combination of the eigenvectors $\mathbf{v}_1, \mathbf{v}_2$, so it lies in the eigenspace for $\lambda = 7$. (This is one step of the Gram–Schmidt process, [[§43 The Gram–Schmidt Process#^thm-43-1|Theorem §43.1]].) The eigenspace is two-dimensional, so the orthogonal set $\{\mathbf{v}_1, \mathbf{z}_2\}$ is an orthogonal basis for it, by the Basis Theorem ([[§27 The Dimension of a Vector Space#^thm-27-5|Theorem §27.5]]). Normalizing ($\|\mathbf{v}_1\| = \sqrt2$, $\|\mathbf{z}_2\| = \sqrt{18}/4$, so $\mathbf{z}_2 / \|\mathbf{z}_2\| = 4\mathbf{z}_2/\sqrt{18}$):
>
> $$
> \mathbf{u}_1 = \begin{bmatrix} 1/\sqrt2 \\ 0 \\ 1/\sqrt2 \end{bmatrix}, \qquad
> \mathbf{u}_2 = \begin{bmatrix} -1/\sqrt{18} \\ 4/\sqrt{18} \\ 1/\sqrt{18} \end{bmatrix}.
> $$
>
> For $\lambda = -2$, rescale $\mathbf{v}_3$ to clear the fraction: $2\mathbf{v}_3 = (-2, -1, 2)$ has length $3$, so
>
> $$
> \mathbf{u}_3 = \frac{1}{\|2\mathbf{v}_3\|} 2\mathbf{v}_3 = \frac13 \begin{bmatrix} -2 \\ -1 \\ 2 \end{bmatrix} = \begin{bmatrix} -2/3 \\ -1/3 \\ 2/3 \end{bmatrix}.
> $$
>
> **Assemble.** By Theorem §48.1, $\mathbf{u}_3$ is orthogonal to $\mathbf{u}_1$ and $\mathbf{u}_2$ automatically (check: $\mathbf{u}_3 \cdot \mathbf{u}_1 = \frac{1}{3\sqrt2}(-2 + 2) = 0$). So $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ is orthonormal, and with
>
> $$
> P = [\,\mathbf{u}_1\ \ \mathbf{u}_2\ \ \mathbf{u}_3\,] = \begin{bmatrix} 1/\sqrt2 & -1/\sqrt{18} & -2/3 \\ 0 & 4/\sqrt{18} & -1/3 \\ 1/\sqrt2 & 1/\sqrt{18} & 2/3 \end{bmatrix}, \qquad
> D = \begin{bmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & -2 \end{bmatrix},
> $$
>
> $P$ orthogonally diagonalizes $A$: $A = PDP^{-1} = PDP^T$.
>
> The eigenvalue $7$ has multiplicity two and its eigenspace is two-dimensional. Part (b) of the Spectral Theorem says this always happens for symmetric matrices.
>
> *Lay: Example 7.1.3*

^ex-48-2

> [!remark] Remark: Method — Orthogonal Diagonalization
> To orthogonally diagonalize a symmetric $n \times n$ matrix $A$:
> 1. Find the eigenvalues: the roots of $\det(A - \lambda I) = 0$. All are real (Theorem §48.3(a)).
> 2. For each eigenvalue $\lambda$, find a basis of the eigenspace $\operatorname{Nul}(A - \lambda I)$ by row reduction.
> 3. If an eigenspace has dimension $\ge 2$, apply Gram–Schmidt to its basis to get an orthogonal basis of that eigenspace. Eigenvectors from *different* eigenspaces are already orthogonal (Theorem §48.1); never mix eigenvectors of different eigenvalues in Gram–Schmidt.
> 4. Normalize every vector. Together they form an orthonormal basis $\mathbf{u}_1, \dots, \mathbf{u}_n$ of $\mathbb{R}^n$ (Theorem §48.3(b) guarantees there are $n$ of them).
> 5. Set $P = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_n\,]$ and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, listing each eigenvalue in the column position of its eigenvector. Then $A = PDP^T$.

^rem-48-1

## The Spectral Theorem

> [!definition] Definition §48.3: Spectrum
> The set of eigenvalues of a matrix $A$ is sometimes called the **spectrum** of $A$. A description of the eigenvalues and eigenvectors of a class of matrices, such as Theorem §48.3, is called a **spectral theorem**.
>
> *Lay: 7.1 (text)*

^def-48-3

> [!theorem] Theorem §48.3: The Spectral Theorem for Symmetric Matrices
> An $n \times n$ symmetric matrix $A$ has the following properties:
> - (a) $A$ has $n$ real eigenvalues, counting multiplicities.
> - (b) The dimension of the eigenspace for each eigenvalue $\lambda$ equals the multiplicity of $\lambda$ as a root of the characteristic equation.
> - (c) The eigenspaces are mutually orthogonal, in the sense that eigenvectors corresponding to different eigenvalues are orthogonal.
> - (d) $A$ is orthogonally diagonalizable.
>
> *Lay: Theorem 3 (7.1)*

^thm-48-3

> [!proof]+ Proof
> *Lay gives this as a sketch:* (a) from Exercise 24 of Section 5.5, (b) from (d) via Exercise 31, (c) is Theorem 1, and (d) from the Schur factorization (Supplementary Exercise 16 of Chapter 6) and Exercise 32, "details omitted". Here are the details along that route.
>
> **(a) The eigenvalues are real.** The characteristic polynomial has degree $n$, so it has $n$ roots in $\mathbb{C}$, counting multiplicities (fundamental theorem of algebra, [[§13 Polynomials#^ladr-4-13|LADR 4.13]]). Let $\lambda$ be one of them. Then $A - \lambda I$ is not invertible as a complex matrix, so there is a nonzero $\mathbf{x} \in \mathbb{C}^n$ with $A\mathbf{x} = \lambda \mathbf{x}$ ([[§36 Complex Eigenvalues#^def-36-1|Definition §36.1]]). Let $\bar{\mathbf{x}}$ be the vector of complex conjugates of the entries of $\mathbf{x}$, and put $q = \bar{\mathbf{x}}^T A \mathbf{x}$, a complex number. Since $A$ has real entries, $\bar A = A$, and
>
> $$
> \bar q = \overline{\bar{\mathbf{x}}^T A \mathbf{x}} = \mathbf{x}^T A \bar{\mathbf{x}} = (\mathbf{x}^T A \bar{\mathbf{x}})^T = \bar{\mathbf{x}}^T A^T \mathbf{x} = \bar{\mathbf{x}}^T A \mathbf{x} = q ,
> $$
>
> using that a $1 \times 1$ matrix equals its transpose and $A^T = A$. So $q$ is real. On the other hand $q = \bar{\mathbf{x}}^T (\lambda \mathbf{x}) = \lambda\, \bar{\mathbf{x}}^T \mathbf{x}$, and $\bar{\mathbf{x}}^T \mathbf{x} = |x_1|^2 + \cdots + |x_n|^2$ is real and positive. Hence $\lambda = q / (\bar{\mathbf{x}}^T \mathbf{x})$ is real. Since $A - \lambda I$ is then a real singular matrix, $\lambda$ also has a *real* eigenvector.
>
> **(c)** is Theorem §48.1.
>
> **(d) Step 1: Schur factorization.** *Claim: an $n \times n$ real matrix $A$ whose $n$ eigenvalues (with multiplicity) are all real can be written $A = URU^T$ with $U$ orthogonal and $R$ upper triangular.* Induction on $n$; for $n = 1$ take $U = [1]$. For $n > 1$, let $\lambda_1$ be an eigenvalue and $\mathbf{u}_1$ a real unit eigenvector (it exists because $A - \lambda_1 I$ is a real singular matrix, as at the end of (a)). Extend $\{\mathbf{u}_1\}$ to a basis of $\mathbb{R}^n$ and apply Gram–Schmidt ([[§43 The Gram–Schmidt Process#^thm-43-1|Theorem §43.1]]), which keeps $\mathbf{u}_1$ first: this gives an orthonormal basis $\mathbf{u}_1, \mathbf{w}_2, \dots, \mathbf{w}_n$. Let $W = [\,\mathbf{w}_2\ \cdots\ \mathbf{w}_n\,]$ and $U_1 = [\,\mathbf{u}_1\ \ W\,]$, an orthogonal matrix. By block multiplication,
>
> $$
> U_1^T A U_1 = \begin{bmatrix} \mathbf{u}_1^T A \mathbf{u}_1 & \mathbf{u}_1^T A W \\ W^T A \mathbf{u}_1 & W^T A W \end{bmatrix} = \begin{bmatrix} \lambda_1 & \ast \\ \mathbf{0} & A_1 \end{bmatrix},
> $$
>
> since $\mathbf{u}_1^T A \mathbf{u}_1 = \lambda_1 \mathbf{u}_1^T \mathbf{u}_1 = \lambda_1$ and $W^T A \mathbf{u}_1 = \lambda_1 W^T \mathbf{u}_1 = \mathbf{0}$. The matrices $A$ and $U_1^T A U_1 = U_1^{-1} A U_1$ are similar, so they have the same characteristic polynomial ([[§33 The Characteristic Equation#^thm-33-6|Theorem §33.6]]); expanding $\det(U_1^T A U_1 - \lambda I)$ down the first column gives $(\lambda_1 - \lambda) \det(A_1 - \lambda I)$. So the eigenvalues of the $(n-1) \times (n-1)$ matrix $A_1$ are the remaining $n - 1$ eigenvalues of $A$, all real. By induction $A_1 = U_2 R_1 U_2^T$ with $U_2$ orthogonal and $R_1$ upper triangular. Then
>
> $$
> U = U_1 \begin{bmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & U_2 \end{bmatrix}
> \quad\text{is orthogonal, and}\quad
> U^T A U = \begin{bmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & U_2^T \end{bmatrix} \begin{bmatrix} \lambda_1 & \ast \\ \mathbf{0} & A_1 \end{bmatrix} \begin{bmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & U_2 \end{bmatrix} = \begin{bmatrix} \lambda_1 & \ast\, U_2 \\ \mathbf{0} & R_1 \end{bmatrix} = R
> $$
>
> is upper triangular. ($U$ is orthogonal because a product of orthogonal matrices is: $(U_1 V)^T (U_1 V) = V^T U_1^T U_1 V = I$.)
>
> **(d) Step 2: symmetric and triangular means diagonal** (Exercise 32). Now let $A$ be symmetric. By (a) all its eigenvalues are real, so Step 1 gives $A = URU^T$, that is, $R = U^T A U$. Then $R^T = U^T A^T U = U^T A U = R$: $R$ is symmetric. An upper triangular matrix has zeros below the diagonal; if it is symmetric it also has zeros above the diagonal, so $R$ is diagonal. Thus $A = URU^T$ is an orthogonal diagonalization.
>
> **(b) from (d)** (Exercise 31). Write $A = PDP^T$ with $P$ orthogonal and $D = \operatorname{diag}(d_1, \dots, d_n)$. $A$ and $D$ are similar, so
>
> $$
> \det(A - \lambda I) = \det(D - \lambda I) = (d_1 - \lambda)(d_2 - \lambda) \cdots (d_n - \lambda) ,
> $$
>
> and the multiplicity $k$ of an eigenvalue $\lambda$ is the number of indices $i$ with $d_i = \lambda$. On the other hand,
>
> $$
> A\mathbf{x} = \lambda \mathbf{x} \iff PDP^T \mathbf{x} = \lambda \mathbf{x} \iff D(P^T \mathbf{x}) = \lambda (P^T \mathbf{x}) ,
> $$
>
> so $\mathbf{x} \mapsto P^T \mathbf{x}$ maps the eigenspace $\operatorname{Nul}(A - \lambda I)$ onto $\operatorname{Nul}(D - \lambda I) = \operatorname{Span}\{\mathbf{e}_i : d_i = \lambda\}$, and it is one-to-one because $P^T$ is invertible. An invertible linear map preserves dimension ([[§27 The Dimension of a Vector Space#^prop-27-7|Proposition §27.7]]), so the eigenspace of $A$ for $\lambda$ has dimension $k$.

^pf-48-3

*Uses:* [[§48★ Diagonalization of Symmetric Matrices#^thm-48-1|§48.1]], [[§33 The Characteristic Equation#^thm-33-5|§33.5]] (degree $n$), [[§36 Complex Eigenvalues#^def-36-1|Def. §36.1]] (complex eigenvectors), [[§36 Complex Eigenvalues#^prop-36-1|§36.1]] (conjugates of products), [[§53 Complex Numbers#^prop-53-2|§53.2]] ($\bar z z = \lvert z \rvert^2$), [[§43 The Gram–Schmidt Process#^thm-43-1|§43.1]] (Gram–Schmidt), [[§41 Orthogonal Sets#^thm-41-4|§41.4]], [[§41 Orthogonal Sets#^def-41-5|Def. §41.5]] (orthogonal matrices), [[§33 The Characteristic Equation#^thm-33-6|§33.6]] (similar matrices), [[§20 Introduction to Determinants#^thm-20-1|§20.1]] (cofactor expansion), [[§14 Partitioned Matrices#^prop-14-2|§14.2]] (block multiplication), [[§27 The Dimension of a Vector Space#^prop-27-7|§27.7]] (isomorphisms preserve dimension), [[§13 Polynomials#^ladr-4-13|LADR 4.13]] (fundamental theorem of algebra)

> [!remark]- Connections
> - Rigorous treatment: the real spectral theorem, [[§23 Spectral Theorem#^ladr-7-29|LADR 7.29]] (hub [[Real spectral theorem]]), for self-adjoint operators on a finite-dimensional real inner product space. Axler's proof follows the same route as above: Schur's theorem ([[§20 Orthonormal Bases#^ladr-6-37|LADR 6.37]]) gives an upper-triangular matrix in an orthonormal basis, and self-adjointness forces it to be diagonal. To get real eigenvalues he avoids $\mathbb{C}$ and determinants altogether, showing instead that the minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-24|LADR 5.24]]) of a self-adjoint operator has only real roots ([[§23 Spectral Theorem#^ladr-7-27|LADR 7.27]]); the complex argument of part (a) is [[§22 Self-Adjoint and Normal Operators#^ladr-7-12|LADR 7.12]].
> - Over $\mathbb{C}$ the condition becomes "normal" ([[§23 Spectral Theorem#^ladr-7-31|LADR 7.31]], [[Complex spectral theorem]]); the symmetric-bilinear-form version, which is the Principal Axes Theorem, [[§49★ Quadratic Forms#^thm-49-2|Theorem §49.2]], is [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-13|LADR 9.13]].
> - See also: BDP's statement for Hermitian matrices, [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|331 Thm. §29.5]] (real eigenvalues and orthogonality proved there). For $\mathbf{x}' = A\mathbf{x}$ with $A$ real symmetric it guarantees a fundamental set of eigenvector solutions even when eigenvalues repeat, [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|331 Thm. §31.2]](b), worked for a double eigenvalue in [[§31 Homogeneous Linear Systems with Constant Coefficients#^ex-31-3|331 Ex. §31.3]].
> - PDE version, in infinite dimensions: a regular Sturm–Liouville problem has real eigenvalues, [[§23 Sturm–Liouville Problems#^prop-23-3|341 Prop. §23.3]], infinitely many of them with $\lambda_n^2 \to \infty$, [[§23 Sturm–Liouville Problems#^thm-23-5|341 Thm. §23.5]], and its eigenfunctions serve as an orthogonal basis for expanding functions, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|341 Thm. §24.2]].

## Spectral Decomposition

> [!theorem] Theorem §48.4: Spectral Decomposition
> Suppose $A = PDP^{-1}$, where the columns of $P$ are orthonormal eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_n$ of $A$ and the corresponding eigenvalues $\lambda_1, \dots, \lambda_n$ are in the diagonal matrix $D$. Then
>
> $$
> A = \lambda_1 \mathbf{u}_1 \mathbf{u}_1^T + \lambda_2 \mathbf{u}_2 \mathbf{u}_2^T + \cdots + \lambda_n \mathbf{u}_n \mathbf{u}_n^T . \qquad (2)
> $$
>
> Each term $\lambda_j \mathbf{u}_j \mathbf{u}_j^T$ is an $n \times n$ matrix of rank at most $1$ (rank $1$ when $\lambda_j \ne 0$): every column of $\lambda_j \mathbf{u}_j \mathbf{u}_j^T$ is a multiple of $\mathbf{u}_j$. Moreover, for each $\mathbf{x}$ in $\mathbb{R}^n$, the vector $(\mathbf{u}_j \mathbf{u}_j^T)\mathbf{x}$ is the orthogonal projection of $\mathbf{x}$ onto $\operatorname{Span}\{\mathbf{u}_j\}$.
>
> *Lay: 7.1, Equation (2) and text*

^thm-48-4

> [!proof]+ Proof
> Since $P$ has orthonormal columns and is square, $P^{-1} = P^T$. By column-times-diagonal multiplication, $PD = [\,\lambda_1 \mathbf{u}_1\ \cdots\ \lambda_n \mathbf{u}_n\,]$, so
>
> $$
> A = PDP^T = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_n\,] \begin{bmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{bmatrix} \begin{bmatrix} \mathbf{u}_1^T \\ \vdots \\ \mathbf{u}_n^T \end{bmatrix}
> = [\,\lambda_1 \mathbf{u}_1\ \cdots\ \lambda_n \mathbf{u}_n\,] \begin{bmatrix} \mathbf{u}_1^T \\ \vdots \\ \mathbf{u}_n^T \end{bmatrix}.
> $$
>
> The column–row expansion of a product ([[§14 Partitioned Matrices#^thm-14-3|Theorem §14.3]]: $AB$ is the sum of (column $k$ of $A$)(row $k$ of $B$)) turns this into (2).
>
> The $i$th column of $\mathbf{u}_j \mathbf{u}_j^T$ is $\mathbf{u}_j$ times the $i$th entry of $\mathbf{u}_j$, so all columns are multiples of $\mathbf{u}_j$ and the rank is at most $1$ (exactly $1$ since $\mathbf{u}_j \ne \mathbf{0}$). Finally (Exercise 35), by associativity,
>
> $$
> (\mathbf{u}_j \mathbf{u}_j^T)\mathbf{x} = \mathbf{u}_j (\mathbf{u}_j^T \mathbf{x}) = (\mathbf{x} \cdot \mathbf{u}_j)\, \mathbf{u}_j = \frac{\mathbf{x} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j} \mathbf{u}_j ,
> $$
>
> because $\mathbf{u}_j \cdot \mathbf{u}_j = 1$. This is the orthogonal projection of $\mathbf{x}$ onto $\operatorname{Span}\{\mathbf{u}_j\}$ ([[§41 Orthogonal Sets#^def-41-3|Definition §41.3]]).

^pf-48-4

*Uses:* [[§14 Partitioned Matrices#^thm-14-3|§14.3]] (column–row expansion), [[§41 Orthogonal Sets#^def-41-3|Def. §41.3]] (orthogonal projection onto a line), [[§41 Orthogonal Sets#^thm-41-4|§41.4]]

> [!definition] Definition §48.4: Spectral Decomposition; Projection Matrix
> The representation (2) of a symmetric matrix $A$ is called a **spectral decomposition** of $A$, because it breaks up $A$ into pieces determined by the spectrum (eigenvalues) of $A$. Each matrix $\mathbf{u}_j \mathbf{u}_j^T$ ($\mathbf{u}_j$ a unit vector) is a **projection matrix**, in the sense of Theorem §48.4: it sends $\mathbf{x}$ to its orthogonal projection onto $\operatorname{Span}\{\mathbf{u}_j\}$.
>
> *Lay: 7.1 (text)*

^def-48-4

> [!example] Example §48.3: A Spectral Decomposition
> Construct a spectral decomposition of the matrix $A$ that has the orthogonal diagonalization
>
> $$
> A = \begin{bmatrix} 7 & 2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 2/\sqrt5 & -1/\sqrt5 \\ 1/\sqrt5 & 2/\sqrt5 \end{bmatrix} \begin{bmatrix} 8 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 2/\sqrt5 & 1/\sqrt5 \\ -1/\sqrt5 & 2/\sqrt5 \end{bmatrix}.
> $$
>
> Denote the columns of $P$ by $\mathbf{u}_1$ and $\mathbf{u}_2$. By (2), $A = 8\mathbf{u}_1 \mathbf{u}_1^T + 3\mathbf{u}_2 \mathbf{u}_2^T$. To verify, compute
>
> $$
> \mathbf{u}_1 \mathbf{u}_1^T = \begin{bmatrix} 2/\sqrt5 \\ 1/\sqrt5 \end{bmatrix} \begin{bmatrix} 2/\sqrt5 & 1/\sqrt5 \end{bmatrix} = \begin{bmatrix} 4/5 & 2/5 \\ 2/5 & 1/5 \end{bmatrix}, \qquad
> \mathbf{u}_2 \mathbf{u}_2^T = \begin{bmatrix} -1/\sqrt5 \\ 2/\sqrt5 \end{bmatrix} \begin{bmatrix} -1/\sqrt5 & 2/\sqrt5 \end{bmatrix} = \begin{bmatrix} 1/5 & -2/5 \\ -2/5 & 4/5 \end{bmatrix},
> $$
>
> and
>
> $$
> 8\mathbf{u}_1 \mathbf{u}_1^T + 3\mathbf{u}_2 \mathbf{u}_2^T = \begin{bmatrix} 32/5 & 16/5 \\ 16/5 & 8/5 \end{bmatrix} + \begin{bmatrix} 3/5 & -6/5 \\ -6/5 & 12/5 \end{bmatrix} = \begin{bmatrix} 7 & 2 \\ 2 & 4 \end{bmatrix} = A .
> $$
>
> Note that $\mathbf{u}_1 \mathbf{u}_1^T + \mathbf{u}_2 \mathbf{u}_2^T = I$: the two projections onto perpendicular lines add up to the identity. Geometrically, $A\mathbf{x}$ is found by splitting $\mathbf{x}$ into its components along $\mathbf{u}_1$ and $\mathbf{u}_2$ and stretching them by $8$ and $3$ (figure below).
>
> *Lay: Example 7.1.4*

^ex-48-3

![[m235-48-1.svg]]
*The symmetric matrix $A = \begin{bmatrix} 7 & 2 \\ 2 & 4 \end{bmatrix}$ of Example §48.3 maps the unit circle onto an ellipse. Its orthonormal eigenvectors $\mathbf{u}_1, \mathbf{u}_2$ (red) lie along perpendicular lines (green), and $A$ just stretches them by the eigenvalues $8$ and $3$: these images are the semi-axes of the ellipse. A non-symmetric diagonalizable matrix also stretches along eigenvector lines, but those lines are not perpendicular.*

> [!remark]- Connections
> - Rigorous treatment: in the language of [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]] (orthogonal projection $P_U$), (2) reads $T = \sum_\lambda \lambda P_{E(\lambda, T)}$, a sum over the distinct eigenvalues of projections onto the mutually orthogonal eigenspaces; this is how the spectral theorem is stated for self-adjoint operators in infinite dimensions.

> [!remark]- Remark: Numerical Note
> For a symmetric matrix that is not too large, modern algorithms compute eigenvalues and eigenvectors with great precision. They apply a sequence of similarity transformations by orthogonal matrices; the diagonal entries of the transformed matrices converge rapidly to the eigenvalues, and the orthogonal matrices combine into one whose columns are eigenvectors. Orthogonal matrices preserve lengths, so numerical errors do not accumulate. A nonsymmetric matrix cannot have a full set of orthogonal eigenvectors; the algorithm still produces fairly accurate eigenvalues, but its eigenvectors need nonorthogonal techniques.

^rem-48-2

> [!remark]- Remark: Powers of Symmetric Matrices
> If $A$ is symmetric, so is $A^2$: $(A^2)^T = (AA)^T = A^T A^T = AA = A^2$. Hence, by Theorem §48.2, if $A$ is orthogonally diagonalizable, so is $A^2$; explicitly, $A^2 = PDP^T PDP^T = PD^2P^T$, with the same eigenvectors and squared eigenvalues. (Lay's Practice Problems 1–2.)

^rem-48-3
