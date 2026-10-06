---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 5
section: 34
lay: "5.3"
aliases: ["Lay 5.3"]
tags: [applied-linear-algebra, math235]
---
← [[§33 The Characteristic Equation]] · ↑ [[· 5 Matrix Eigenvalues and Eigenvectors]] · [[§35 Eigenvectors and Linear Transformations]] →

*Lay, Section 5.3 · MATH 235 lectures L18, L19, L20, L21.*

Powers of a diagonal matrix are trivial to compute, and so are powers of any matrix of the form $A = PDP^{-1}$ with $D$ diagonal: $A^k = PD^kP^{-1}$. Such an $A$ is called diagonalizable. The Diagonalization Theorem says exactly when this happens: when $A$ has $n$ linearly independent eigenvectors, which then form the columns of $P$, with the eigenvalues on the diagonal of $D$. Distinct eigenvalues guarantee this. With repeated eigenvalues it depends on the dimensions of the eigenspaces (the geometric multiplicities), which can be smaller than the algebraic multiplicities. Diagonalization is the main computational tool of the chapter: it gives $A^k$ for large $k$, limits $\lim A^k$, and, in [[§37 Discrete Dynamical Systems|§37]] and [[§38 Applications to Differential Equations|§38]], decouples dynamical systems.

> [!example] Example §34.1: Powers of PDP⁻¹
> **(a) Diagonal matrices.** If $D = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$, then
>
> $$
> D^2 = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 5^2 & 0 \\ 0 & 3^2 \end{bmatrix}, \qquad D^3 = DD^2 = \begin{bmatrix} 5^3 & 0 \\ 0 & 3^3 \end{bmatrix},
> $$
>
> and in general $D^k = \begin{bmatrix} 5^k & 0 \\ 0 & 3^k \end{bmatrix}$ for $k \ge 1$. In the same way, the $k$th power of any diagonal matrix is obtained by raising the diagonal entries to the $k$th power.
>
> **(b)** Let $A = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix}$. Find a formula for $A^k$, given that $A = PDP^{-1}$ with $P = \begin{bmatrix} 1 & 1 \\ -1 & -2 \end{bmatrix}$ and $D$ as in (a).
>
> The formula for the inverse of a $2 \times 2$ matrix gives $P^{-1} = \frac{1}{-2 + 1}\begin{bmatrix} -2 & -1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ -1 & -1 \end{bmatrix}$. By associativity of matrix multiplication,
>
> $$
> A^2 = (PDP^{-1})(PDP^{-1}) = PD\underbrace{(P^{-1}P)}_{I}DP^{-1} = PD^2P^{-1}, \qquad A^3 = (PDP^{-1})A^2 = PD\underbrace{P^{-1}P}_{I}D^2P^{-1} = PD^3P^{-1},
> $$
>
> and in general, by induction, for $k \ge 1$,
>
> $$
> A^k = PD^kP^{-1} = \begin{bmatrix} 1 & 1 \\ -1 & -2 \end{bmatrix}\begin{bmatrix} 5^k & 0 \\ 0 & 3^k \end{bmatrix}\begin{bmatrix} 2 & 1 \\ -1 & -1 \end{bmatrix} = \begin{bmatrix} 5^k & 3^k \\ -5^k & -2\cdot 3^k \end{bmatrix}\begin{bmatrix} 2 & 1 \\ -1 & -1 \end{bmatrix} = \begin{bmatrix} 2\cdot 5^k - 3^k & 5^k - 3^k \\ 2\cdot 3^k - 2\cdot 5^k & 2\cdot 3^k - 5^k \end{bmatrix} .
> $$
>
> Check at $k = 1$: $\begin{bmatrix} 10 - 3 & 5 - 3 \\ 6 - 10 & 6 - 5 \end{bmatrix} = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix} = A$.
>
> *Lay: Examples 5.3.1 and 5.3.2*

^ex-34-1

> [!definition] Definition §34.1: Diagonalizable Matrix
> A square matrix $A$ is said to be **diagonalizable** if $A$ is similar to a diagonal matrix ([[§33 The Characteristic Equation#^def-33-3|Definition §33.3]]), that is, if $A = PDP^{-1}$ for some invertible matrix $P$ and some diagonal matrix $D$. (Equivalently, $P^{-1}AP = D$; the lecture writes $M^{-1}AM = D$ or $B^{-1}AB = D$.)
>
> *Lay: 5.3 (text)*

^def-34-1

> [!definition] Definition §34.2: Eigenvector Basis
> A basis of $\mathbb{R}^n$ consisting of eigenvectors of an $n \times n$ matrix $A$ is called an **eigenvector basis** of $\mathbb{R}^n$ (the lecture says *eigenbasis of $A$*).
>
> *Lay: 5.3 (text)*

^def-34-2

> [!theorem] Theorem §34.1: The Diagonalization Theorem
> An $n \times n$ matrix $A$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors.
>
> In fact, $A = PDP^{-1}$, with $D$ a diagonal matrix, if and only if the columns of $P$ are $n$ linearly independent eigenvectors of $A$. In this case, the diagonal entries of $D$ are eigenvalues of $A$ that correspond, respectively, to the eigenvectors in $P$.
>
> In other words, $A$ is diagonalizable if and only if there are enough eigenvectors to form a basis of $\mathbb{R}^n$, an eigenvector basis.
>
> *Lay: Theorem 5 (5.3)*

^thm-34-1

> [!proof]+ Proof
> First, observe that if $P$ is any $n \times n$ matrix with columns $\mathbf{v}_1, \ldots, \mathbf{v}_n$, and if $D$ is any diagonal matrix with diagonal entries $\lambda_1, \ldots, \lambda_n$, then by the column definition of matrix multiplication
>
> $$
> AP = A[\,\mathbf{v}_1 \;\; \mathbf{v}_2 \;\; \cdots \;\; \mathbf{v}_n\,] = [\,A\mathbf{v}_1 \;\; A\mathbf{v}_2 \;\; \cdots \;\; A\mathbf{v}_n\,] \qquad (1)
> $$
>
> while
>
> $$
> PD = P\begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{bmatrix} = [\,\lambda_1\mathbf{v}_1 \;\; \lambda_2\mathbf{v}_2 \;\; \cdots \;\; \lambda_n\mathbf{v}_n\,] , \qquad (2)
> $$
>
> since column $j$ of $PD$ is $P$ times column $j$ of $D$, which is $P(\lambda_j\mathbf{e}_j) = \lambda_j\mathbf{v}_j$.
>
> **"Only if".** Suppose $A$ is diagonalizable and $A = PDP^{-1}$. Right-multiplying by $P$ gives $AP = PD$. By (1) and (2),
>
> $$
> [\,A\mathbf{v}_1 \;\; A\mathbf{v}_2 \;\; \cdots \;\; A\mathbf{v}_n\,] = [\,\lambda_1\mathbf{v}_1 \;\; \lambda_2\mathbf{v}_2 \;\; \cdots \;\; \lambda_n\mathbf{v}_n\,] . \qquad (3)
> $$
>
> Equating columns,
>
> $$
> A\mathbf{v}_1 = \lambda_1\mathbf{v}_1, \quad A\mathbf{v}_2 = \lambda_2\mathbf{v}_2, \quad \ldots, \quad A\mathbf{v}_n = \lambda_n\mathbf{v}_n . \qquad (4)
> $$
>
> Since $P$ is invertible, its columns $\mathbf{v}_1, \ldots, \mathbf{v}_n$ are linearly independent (Invertible Matrix Theorem); in particular they are nonzero. So the equations (4) show that $\lambda_1, \ldots, \lambda_n$ are eigenvalues and $\mathbf{v}_1, \ldots, \mathbf{v}_n$ corresponding eigenvectors. This proves the "only if" parts of the first and second statements, and the third statement.
>
> **"If".** Given any $n$ eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$, use them as the columns of $P$, and use the corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$ to construct $D$. By (1)–(3), $AP = PD$; this is true without any condition on the eigenvectors. If, in fact, the eigenvectors are linearly independent, then $P$ is invertible (Invertible Matrix Theorem), and right-multiplying $AP = PD$ by $P^{-1}$ gives $A = PDP^{-1}$.

^pf-34-1

*Uses:* [[§34 Diagonalization#^def-34-1|Def. §34.1]], [[§32 Eigenvectors and Eigenvalues#^def-32-1|Def. §32.1]], [[§11 Matrix Operations#^def-11-3|Def. §11.3]] (the product $AB$ column by column), [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]] (the Invertible Matrix Theorem)

> [!remark]- Connections
> - Rigorous treatment: [[§17 Diagonalizable Operators#^ladr-5-50|LADR 5.50]] (an operator is diagonalizable if it has a diagonal matrix in *some* basis) and [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]] (equivalent: a basis of eigenvectors; $V$ is the direct sum of the eigenspaces; the eigenspace dimensions add up to $\dim V$). Axler's (a) $\Leftrightarrow$ (b) is the operator form of $AP = PD$; that $D = P^{-1}AP$ is the matrix of $\mathbf{x} \mapsto A\mathbf{x}$ in the basis of columns of $P$ is [[§35 Eigenvectors and Linear Transformations#^thm-35-2|Theorem §35.2]].
> - A further criterion with no counterpart in Lay: diagonalizable $\Leftrightarrow$ the minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-24|LADR 5.24]]) has distinct linear factors, [[§17 Diagonalizable Operators#^ladr-5-62|LADR 5.62]].
> - ODE version: [[§33★ Fundamental Matrices#^thm-33-7|331 Thm. §33.7]] (the same theorem, $\mathbf{T}^{-1}A\mathbf{T} = D$ with the eigenvectors as columns of $\mathbf{T}$). For $\mathbf{x}' = A\mathbf{x}$ it gives a fundamental set of eigenvector solutions, [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|331 Thm. §31.2]], and the matrix exponential $e^{At} = \mathbf{T}e^{Dt}\mathbf{T}^{-1}$, the continuous analogue of $A^k = PD^kP^{-1}$, [[§33★ Fundamental Matrices#^thm-33-8|331 Thm. §33.8]].

## Diagonalizing Matrices

> [!remark] Remark: Method — Diagonalizing a Matrix
> To diagonalize an $n \times n$ matrix $A$, that is, to find an invertible $P$ and a diagonal $D$ with $A = PDP^{-1}$:
> 1. **Find the eigenvalues of $A$**, the roots of $\det(A - \lambda I) = 0$ ([[§33 The Characteristic Equation#^thm-33-4|Theorem §33.4]]). If there are $n$ distinct ones, $A$ is diagonalizable ([[§34 Diagonalization#^thm-34-2|Theorem §34.2]] below).
> 2. **Find $n$ linearly independent eigenvectors of $A$**: a basis of each eigenspace $\operatorname{Nul}(A - \lambda I)$ ([[§32 Eigenvectors and Eigenvalues#^rem-32-4|Remark: Method]]). This is the critical step. If the eigenspace dimensions add up to less than $n$, then $A$ cannot be diagonalized ([[§34 Diagonalization#^thm-34-3|Theorem §34.3]]).
> 3. **Construct $P$** from the vectors of step 2, as columns, in any order.
> 4. **Construct $D$** from the corresponding eigenvalues, *in the same order* as the columns of $P$, each eigenvalue repeated once for each of its basis vectors.
> 5. **Check** $AP = PD$, which avoids computing $P^{-1}$ (but make sure $P$ is invertible).
>
> *Lay: Example 5.3.3 (Steps 1–4); Source: 235 lecture L20 ("diagonalization algorithm")*

^rem-34-1

> [!example] Example §34.2: Diagonalizing a 3 × 3 Matrix
> Diagonalize $A = \begin{bmatrix} 1 & 3 & 3 \\ -3 & -5 & -3 \\ 3 & 3 & 1 \end{bmatrix}$, if possible.
>
> **Step 1.** The characteristic equation turns out to be a cubic that can be factored:
>
> $$
> 0 = \det(A - \lambda I) = -\lambda^3 - 3\lambda^2 + 4 = -(\lambda - 1)(\lambda + 2)^2 .
> $$
>
> (Check: $-(\lambda - 1)(\lambda^2 + 4\lambda + 4) = -(\lambda^3 + 3\lambda^2 - 4)$; the trace is $1 - 5 + 1 = -3 = 1 + (-2) + (-2)$.) The eigenvalues are $\lambda = 1$ and $\lambda = -2$.
>
> **Step 2.** Row reduce $A - \lambda I$:
>
> $$
> A - I = \begin{bmatrix} 0 & 3 & 3 \\ -3 & -6 & -3 \\ 3 & 3 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}, \qquad
> A + 2I = \begin{bmatrix} 3 & 3 & 3 \\ -3 & -3 & -3 \\ 3 & 3 & 3 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> For $\lambda = 1$: $x_1 = x_3$, $x_2 = -x_3$, basis $\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix}$. For $\lambda = -2$: $x_1 = -x_2 - x_3$, basis $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$. The set $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is linearly independent ([[§34 Diagonalization#^thm-34-3|Theorem §34.3]](c)).
>
> **Steps 3–4.**
>
> $$
> P = [\,\mathbf{v}_1 \;\; \mathbf{v}_2 \;\; \mathbf{v}_3\,] = \begin{bmatrix} 1 & -1 & -1 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}, \qquad D = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{bmatrix} .
> $$
>
> **Check.**
>
> $$
> AP = \begin{bmatrix} 1 & 3 & 3 \\ -3 & -5 & -3 \\ 3 & 3 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 & -1 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ -1 & -2 & 0 \\ 1 & 0 & -2 \end{bmatrix}, \qquad
> PD = \begin{bmatrix} 1 & -1 & -1 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 \\ -1 & -2 & 0 \\ 1 & 0 & -2 \end{bmatrix} .
> $$
>
> So $A = PDP^{-1}$: $A$ is diagonalizable, although it has only two distinct eigenvalues.
>
> *Lay: Example 5.3.3*

^ex-34-2

> [!theorem] Theorem §34.2: Distinct Eigenvalues Imply Diagonalizable
> An $n \times n$ matrix with $n$ distinct eigenvalues is diagonalizable.
>
> *Lay: Theorem 6 (5.3)*

^thm-34-2

> [!proof]+ Proof
> Let $\mathbf{v}_1, \ldots, \mathbf{v}_n$ be eigenvectors corresponding to the $n$ distinct eigenvalues of a matrix $A$. Then $\{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$ is linearly independent, by [[§32 Eigenvectors and Eigenvalues#^thm-32-3|Theorem §32.3]]. Hence $A$ is diagonalizable, by the Diagonalization [[§34 Diagonalization#^thm-34-1|Theorem §34.1]].

^pf-34-2

*Uses:* [[§32 Eigenvectors and Eigenvalues#^thm-32-3|§32.3]], [[§34 Diagonalization#^thm-34-1|§34.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§17 Diagonalizable Operators#^ladr-5-58|LADR 5.58]] (an operator on $V$ with $\dim V$ distinct eigenvalues is diagonalizable), by the same argument from [[§14 Invariant Subspaces#^ladr-5-11|LADR 5.11]].

For example, $A = \begin{bmatrix} 5 & -8 & 1 \\ 0 & 0 & 7 \\ 0 & 0 & -2 \end{bmatrix}$ is triangular, so its eigenvalues are $5$, $0$ and $-2$ ([[§32 Eigenvectors and Eigenvalues#^thm-32-1|Theorem §32.1]]); three distinct eigenvalues, so $A$ is diagonalizable (Lay, Example 5.3.5). The lecture's $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$ has eigenvalues $5 \ne -1$, with eigenvectors $(1, 2)$ and $(1, -1)$ ([[§32 Eigenvectors and Eigenvalues#^ex-32-5|Example §32.5]]); with $M = \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix}$ (these eigenvectors as columns), $AM = \begin{bmatrix} 5 & -1 \\ 10 & 1 \end{bmatrix} = M\begin{bmatrix} 5 & 0 \\ 0 & -1 \end{bmatrix}$, so $M^{-1}AM = \operatorname{diag}(5, -1)$.

The condition is sufficient but not *necessary*: the matrix of [[§34 Diagonalization#^ex-34-2|Example §34.2]] is diagonalizable with only two distinct eigenvalues. Nor is every matrix diagonalizable.

> [!example] Example §34.3: Matrices That Are Not Diagonalizable
> **(a)** (Lecture.) $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ is not diagonalizable. Two reasons:
> - *By powers.* $A^2 = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$. If $M^{-1}AM = D$ were diagonal, then $D^2 = M^{-1}AMM^{-1}AM = M^{-1}A^2M = 0$. A diagonal matrix with $D^2 = 0$ has all diagonal entries $d_{ii}$ with $d_{ii}^2 = 0$, so $D = 0$ and $A = MDM^{-1} = 0$, a contradiction.
> - *By eigenvectors.* $\det(A - \lambda I) = \det\begin{bmatrix} -\lambda & 1 \\ 0 & -\lambda \end{bmatrix} = \lambda^2$, so the only eigenvalue is $0$, with algebraic multiplicity $2$. Its eigenspace is $\operatorname{Nul} A = \operatorname{Span}\{(1, 0)\}$, one-dimensional. Every eigenvector is a multiple of $(1, 0)$, so there are not two linearly independent eigenvectors, and [[§34 Diagonalization#^thm-34-1|Theorem §34.1]] says $A$ is not diagonalizable.
>
> By contrast, $\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$, $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ and $\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ are diagonal, hence diagonalizable, even though two of them have a repeated eigenvalue.
>
> **(b)** (Lay.) $A = \begin{bmatrix} 2 & 4 & 3 \\ -4 & -6 & -3 \\ 3 & 3 & 1 \end{bmatrix}$ has the same characteristic equation as the matrix of [[§34 Diagonalization#^ex-34-2|Example §34.2]], $-(\lambda - 1)(\lambda + 2)^2 = 0$. But each eigenspace is only one-dimensional:
>
> $$
> A - I = \begin{bmatrix} 1 & 4 & 3 \\ -4 & -7 & -3 \\ 3 & 3 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}, \qquad
> A + 2I = \begin{bmatrix} 4 & 4 & 3 \\ -4 & -4 & -3 \\ 3 & 3 & 3 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix},
> $$
>
> with bases $\mathbf{v}_1 = (1, -1, 1)$ for $\lambda = 1$ and $\mathbf{v}_2 = (-1, 1, 0)$ for $\lambda = -2$. There are no other eigenvalues, and every eigenvector of $A$ is a multiple of $\mathbf{v}_1$ or $\mathbf{v}_2$. So no basis of $\mathbb{R}^3$ consists of eigenvectors of $A$, and $A$ is *not* diagonalizable.
>
> *Lay: Example 5.3.4; Source: 235 lectures L19, L20*

^ex-34-3

## Matrices Whose Eigenvalues Are Not Distinct

If $A$ has $n$ distinct eigenvalues, any choice of eigenvectors gives an invertible $P$. When $A$ is diagonalizable with fewer distinct eigenvalues, $P$ can still be built so that it is automatically invertible, by taking bases of the eigenspaces. Whether there are enough of them is measured by comparing two multiplicities.

> [!definition] Definition §34.3: Geometric Multiplicity
> Let $\lambda$ be an eigenvalue of an $n \times n$ matrix $A$. The dimension of the eigenspace $\operatorname{Nul}(A - \lambda I)$ is called the **geometric multiplicity** of $\lambda$. The multiplicity of $\lambda$ as a root of the characteristic polynomial ([[§33 The Characteristic Equation#^def-33-2|Definition §33.2]]) is its **algebraic multiplicity**.
>
> *Source: 235 lecture L20 (Lay speaks of "the dimension of the eigenspace" and "the multiplicity")*

^def-34-3

> [!theorem] Theorem §34.3: Diagonalizability and Multiplicities
> Let $A$ be an $n \times n$ matrix whose distinct eigenvalues are $\lambda_1, \ldots, \lambda_p$.
>
> a. For $1 \le k \le p$, the dimension of the eigenspace for $\lambda_k$ is less than or equal to the multiplicity of the eigenvalue $\lambda_k$. (Geometric multiplicity $\le$ algebraic multiplicity; and the geometric multiplicity is $\ge 1$.)
>
> b. The matrix $A$ is diagonalizable if and only if the sum of the dimensions of the eigenspaces equals $n$, and this happens if and only if (i) the characteristic polynomial factors completely into linear factors and (ii) the dimension of the eigenspace for each $\lambda_k$ equals the multiplicity of $\lambda_k$.
>
> c. If $A$ is diagonalizable and $\mathcal{B}_k$ is a basis for the eigenspace corresponding to $\lambda_k$ for each $k$, then the total collection of vectors in the sets $\mathcal{B}_1, \ldots, \mathcal{B}_p$ forms an eigenvector basis for $\mathbb{R}^n$.
>
> *Lay: Theorem 7 (5.3)*

^thm-34-3

*Lay omits the proof ("somewhat lengthy but not difficult"; he cites Friedberg–Insel–Spence, Section 5.2); see [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]] for (b) and (c), and, for (a), Axler's multiplicity $\dim G(\lambda, T) \ge \dim E(\lambda, T)$, [[§29 Generalized Eigenspace Decomposition#^ladr-8-23|LADR 8.23]]. The lecture states (a) and (b)(ii) without proof. Here is a proof with the tools of this course.*

> [!proof]- Proof
> **Step 0: bases of eigenspaces combine to an independent set.** Let $\mathcal{B}_k$ be a basis of the eigenspace $E_k$ for $\lambda_k$, $k = 1, \ldots, p$. Suppose a linear combination of all the vectors of $\mathcal{B}_1 \cup \cdots \cup \mathcal{B}_p$ is $\mathbf{0}$. Group the terms by eigenspace: $\mathbf{w}_1 + \cdots + \mathbf{w}_p = \mathbf{0}$, where $\mathbf{w}_k \in E_k$ is the part of the combination using $\mathcal{B}_k$. Each nonzero $\mathbf{w}_k$ is an eigenvector for $\lambda_k$. If some $\mathbf{w}_k$ were nonzero, the nonzero ones would be eigenvectors for distinct eigenvalues with sum $\mathbf{0}$, a linear dependence contradicting [[§32 Eigenvectors and Eigenvalues#^thm-32-3|Theorem §32.3]]. So every $\mathbf{w}_k = \mathbf{0}$, and since $\mathcal{B}_k$ is linearly independent, all the weights in $\mathbf{w}_k$ are zero. Hence $\mathcal{B}_1 \cup \cdots \cup \mathcal{B}_p$ is linearly independent. (This is Lay's Practice Problem 5.1.3 in general.) In particular $\dim E_1 + \cdots + \dim E_p \le n$, since a linearly independent set in $\mathbb{R}^n$ has at most $n$ vectors ([[§7 Linear Independence#^thm-7-6|Theorem §7.6]]).
>
> **(c) and the first part of (b).** If $\dim E_1 + \cdots + \dim E_p = n$, Step 0 gives $n$ linearly independent eigenvectors, a basis of $\mathbb{R}^n$ ([[§27 The Dimension of a Vector Space#^thm-27-5|Theorem §27.5]], the Basis Theorem), so $A$ is diagonalizable by [[§34 Diagonalization#^thm-34-1|Theorem §34.1]]. Conversely, if $A$ is diagonalizable, it has $n$ linearly independent eigenvectors ([[§34 Diagonalization#^thm-34-1|Theorem §34.1]]). Those belonging to $\lambda_k$ are a linearly independent subset of $E_k$, so there are at most $\dim E_k$ of them; adding over $k$, $n \le \dim E_1 + \cdots + \dim E_p$. With Step 0, the sum equals $n$, and then the union of the $\mathcal{B}_k$ is $n$ independent vectors, an eigenvector basis: this is (c).
>
> **(a).** Fix $\lambda = \lambda_k$, let $d = \dim E_k \ge 1$ and let $\mathbf{v}_1, \ldots, \mathbf{v}_d$ be a basis of $E_k$. Extend it to a basis $\mathbf{v}_1, \ldots, \mathbf{v}_n$ of $\mathbb{R}^n$ and let $P = [\,\mathbf{v}_1 \; \cdots \; \mathbf{v}_n\,]$. Since $A\mathbf{v}_j = \lambda\mathbf{v}_j$ for $j \le d$, the first $d$ columns of $P^{-1}AP$ are $P^{-1}(\lambda\mathbf{v}_j) = \lambda\mathbf{e}_j$, so
>
> $$
> P^{-1}AP = \begin{bmatrix} \lambda I_d & B \\ 0 & C \end{bmatrix}, \qquad P^{-1}AP - tI = \begin{bmatrix} (\lambda - t)I_d & B \\ 0 & C - tI_{n-d} \end{bmatrix}
> $$
>
> for some blocks $B$, $C$. Expanding the determinant down the first column $d$ times (each time the only nonzero entry is $\lambda - t$ at the top), $\det(P^{-1}AP - tI) = (\lambda - t)^d\det(C - tI)$. By [[§33 The Characteristic Equation#^thm-33-6|Theorem §33.6]] this is the characteristic polynomial of $A$, so $(\lambda - t)^d$ divides it, and the multiplicity of $\lambda$ is at least $d$.
>
> **The second part of (b).** Let $m_k$ be the multiplicity of $\lambda_k$, and write the characteristic polynomial as $f(t) = (\lambda_1 - t)^{m_1}\cdots(\lambda_p - t)^{m_p}\,g(t)$ (divide out the factors one root at a time), where $g$ has no real root, because the real roots of $f$ are exactly the eigenvalues $\lambda_1, \ldots, \lambda_p$ ([[§33 The Characteristic Equation#^thm-33-4|Theorem §33.4]]). Since $f$ has degree $n$ ([[§33 The Characteristic Equation#^thm-33-5|Theorem §33.5]]), $m_1 + \cdots + m_p \le n$, with equality if and only if $g$ is a constant, that is, if and only if $f$ factors completely into linear factors (i): a factorization into linear factors $c(r_1 - t)\cdots(r_n - t)$ has real roots $r_i$, so each $r_i$ is one of the $\lambda_k$. By (a),
>
> $$
> \dim E_1 + \cdots + \dim E_p \le m_1 + \cdots + m_p \le n .
> $$
>
> So the sum of the dimensions equals $n$ if and only if both inequalities are equalities: the second is (i), and, given $\dim E_k \le m_k$ for each $k$, the first is equality $\dim E_k = m_k$ for every $k$, which is (ii).

^pf-34-3

*Uses:* [[§32 Eigenvectors and Eigenvalues#^thm-32-3|§32.3]], [[§34 Diagonalization#^thm-34-1|§34.1]], [[§33 The Characteristic Equation#^thm-33-6|§33.6]], [[§27 The Dimension of a Vector Space#^thm-27-5|§27.5]] (the Basis Theorem), [[§27 The Dimension of a Vector Space#^thm-27-3|§27.3]] (a linearly independent set extends to a basis), [[§20 Introduction to Determinants#^thm-20-1|§20.1]] (cofactor expansion), [[§33 The Characteristic Equation#^thm-33-4|§33.4]], [[§33 The Characteristic Equation#^thm-33-5|§33.5]], [[§7 Linear Independence#^thm-7-6|§7.6]]

> [!remark]- Connections
> - See also, for $\mathbf{x}' = A\mathbf{x}$: a repeated eigenvalue whose geometric multiplicity equals its algebraic multiplicity still gives independent eigenvector solutions, [[§34★ Repeated Eigenvalues#^prop-34-1|331 Prop. §34.1]]; when the geometric multiplicity is smaller, a generalized eigenvector supplies the missing solution, [[§34★ Repeated Eigenvalues#^thm-34-2|331 Thm. §34.2]].

> [!remark] Remark: Reading Theorem §34.3
> - Since the geometric multiplicity of an eigenvalue of algebraic multiplicity $1$ is squeezed between $1$ and $1$, an eigenvalue with algebraic multiplicity $1$ never causes trouble. This gives a second proof of [[§34 Diagonalization#^thm-34-2|Theorem §34.2]] (lecture L20): $n$ distinct eigenvalues means all algebraic multiplicities are $1$, so all geometric multiplicities are $1$ and they add up to $n$.
> - Condition (i) fails when there are complex roots, as for the rotation matrix $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ (characteristic polynomial $\lambda^2 + 1$). Such a matrix is not diagonalizable with real $P$ and $D$, although it may be with complex ones ([[§36 Complex Eigenvalues|§36]]).
> - Condition (ii) is what fails in [[§34 Diagonalization#^ex-34-3|Example §34.3]]: there, $\lambda = 0$ (or $\lambda = -2$) has algebraic multiplicity $2$ and geometric multiplicity $1$.
>
> *Source: 235 lecture L20*

^rem-34-2

> [!example] Example §34.4: Multiplicities in Diagonalizable Matrices
> **(a)** Diagonalize $A = \begin{bmatrix} 2 & 2 & 1 \\ 1 & 3 & 1 \\ 1 & 2 & 2 \end{bmatrix}$, whose characteristic polynomial is $-(\lambda - 1)^2(\lambda - 5)$ ([[§33 The Characteristic Equation#^ex-33-3|Example §33.3]]).
>
> **$\lambda = 1$.** $A - I = \begin{bmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \\ 1 & 2 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$, so $x_1 = -2x_2 - x_3$ with $x_2, x_3$ free:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_2\begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} .
> $$
>
> The eigenspace is two-dimensional, with basis $\mathbf{v}_1 = (-2, 1, 0)$, $\mathbf{v}_2 = (-1, 0, 1)$.
>
> **$\lambda = 5$.** Interchange rows 1 and 3, then add $-1$ times row 1 to row 2 and $3$ times row 1 to row 3:
>
> $$
> A - 5I = \begin{bmatrix} -3 & 2 & 1 \\ 1 & -2 & 1 \\ 1 & 2 & -3 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & -3 \\ 1 & -2 & 1 \\ -3 & 2 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & -3 \\ 0 & -4 & 4 \\ 0 & 8 & -8 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & -3 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $x_1 = x_3$, $x_2 = x_3$: the eigenspace is one-dimensional, with basis $\mathbf{v}_3 = (1, 1, 1)$. Check: $A\mathbf{v}_3 = (2 + 2 + 1, 1 + 3 + 1, 1 + 2 + 2) = (5, 5, 5)$.
>
> **Multiplicities.**
>
> | eigenvalue | $1$ | $5$ |
> |---|---|---|
> | algebraic multiplicity | $2$ | $1$ |
> | geometric multiplicity | $2$ | $1$ |
>
> They agree for each eigenvalue, so $A$ is diagonalizable by [[§34 Diagonalization#^thm-34-3|Theorem §34.3]](b), and by (c) the three vectors form an eigenvector basis:
>
> $$
> A = PDP^{-1}, \qquad P = \begin{bmatrix} -2 & -1 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}, \qquad D = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5 \end{bmatrix} .
> $$
>
> *In the lecture the reduction of $A - 5I$ turns the entry $-3$ into $3$ in one step and arrives at $(-5, 1, 1)$, which is not an eigenvector ($A(-5, 1, 1) = (-7, -1, -1)$); the correct row reduction gives $(1, 1, 1)$.*
>
> **(b) Only the repeated eigenvalue needs checking.** Is $A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & -1 & -1 & 1 \end{bmatrix}$ diagonalizable?
>
> In $A - \lambda I$, subtract row 4 from rows 2 and 3: they become $(0,\ 2 - \lambda,\ 0,\ \lambda - 2) = (2 - \lambda)(0, 1, 0, -1)$ and $(0,\ 0,\ 2 - \lambda,\ \lambda - 2) = (2 - \lambda)(0, 0, 1, -1)$. Take out the two factors $2 - \lambda$, then add columns 2 and 3 to column 4 and expand along rows 2 and 3 (each now $\mathbf{e}_2^T$, $\mathbf{e}_3^T$):
>
> $$
> \det(A - \lambda I) = (2 - \lambda)^2\det\begin{bmatrix} 1 - \lambda & 1 & 1 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & -1 & -1 & -1 - \lambda \end{bmatrix} = (2 - \lambda)^2\det\begin{bmatrix} 1 - \lambda & 3 \\ 1 & -1 - \lambda \end{bmatrix} = (2 - \lambda)^2(\lambda^2 - 4) = (\lambda - 2)^3(\lambda + 2) .
> $$
>
> So $2$ has algebraic multiplicity $3$ and $-2$ has algebraic multiplicity $1$. For $\lambda = 2$, every row of $A - 2I$ is $\pm(-1, 1, 1, 1)$, so $A - 2I \sim \begin{bmatrix} -1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$: $x_2, x_3, x_4$ are free and the geometric multiplicity is $3$, with basis $(1, 1, 0, 0)$, $(1, 0, 1, 0)$, $(1, 0, 0, 1)$. For $\lambda = -2$ nothing needs computing: $1 \le$ geometric multiplicity $\le$ algebraic multiplicity $= 1$ ([[§34 Diagonalization#^thm-34-3|Theorem §34.3]](a)). The multiplicities agree, so $A$ is diagonalizable. (An eigenvector for $-2$ is $(-1, 1, 1, 1)$: $A(-1, 1, 1, 1) = (2, -2, -2, -2)$.)
>
> *Source: 235 lectures L19, L20 (Lay: Exercise 5.3.5)*

^ex-34-4

> [!example] Example §34.5: The Limit of the Powers of a Stochastic Matrix
> A walker moves between two spots. From spot 1 she stays with probability $\frac12$ and moves with probability $\frac12$; from spot 2 she moves to spot 1 with probability $\frac34$ and stays with probability $\frac14$. The transition matrix is
>
> $$
> A = \begin{bmatrix} 1/2 & 3/4 \\ 1/2 & 1/4 \end{bmatrix}
> $$
>
> (column $j$ lists the probabilities of going from spot $j$ to spots 1 and 2; the columns sum to $1$). Find $\lim_{N\to\infty} A^N$.
>
> **Eigenvalues.** $\det(A - \lambda I) = (\tfrac12 - \lambda)(\tfrac14 - \lambda) - \tfrac38 = \lambda^2 - \tfrac34\lambda + \tfrac18 - \tfrac38 = \lambda^2 - \tfrac34\lambda - \tfrac14 = (\lambda - 1)(\lambda + \tfrac14)$. The eigenvalues are $1$ and $-\frac14$.
>
> **Eigenvectors.** $A - I = \begin{bmatrix} -1/2 & 3/4 \\ 1/2 & -3/4 \end{bmatrix}$ gives $-\frac12x_1 + \frac34x_2 = 0$, so $\mathbf{u} = (3, 2)$. $A + \frac14I = \begin{bmatrix} 3/4 & 3/4 \\ 1/2 & 1/2 \end{bmatrix}$ gives $x_1 + x_2 = 0$, so $\mathbf{v} = (1, -1)$.
>
> **Diagonalize.** With $P = \begin{bmatrix} 3 & 1 \\ 2 & -1 \end{bmatrix}$, $\det P = -5$ and $P^{-1} = \frac{1}{-5}\begin{bmatrix} -1 & -1 \\ -2 & 3 \end{bmatrix} = \frac15\begin{bmatrix} 1 & 1 \\ 2 & -3 \end{bmatrix}$, so $A = PDP^{-1}$ with $D = \operatorname{diag}(1, -\frac14)$, and
>
> $$
> A^N = PD^NP^{-1} = \frac15\begin{bmatrix} 3 & 1 \\ 2 & -1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & (-1/4)^N \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 2 & -3 \end{bmatrix} = \frac15\begin{bmatrix} 3 + 2r & 3 - 3r \\ 2 - 2r & 2 + 3r \end{bmatrix}, \qquad r = \Big(-\frac14\Big)^N .
> $$
>
> (At $N = 1$, $r = -\frac14$ gives $\frac15\begin{bmatrix} 5/2 & 15/4 \\ 5/2 & 5/4 \end{bmatrix} = A$.)
>
> **The limit.** $r \to 0$, so $D^N \to \operatorname{diag}(1, 0)$ and
>
> $$
> \lim_{N\to\infty} A^N = \frac15\begin{bmatrix} 3 & 0 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 2 & -3 \end{bmatrix} = \frac15\begin{bmatrix} 3 & 3 \\ 2 & 2 \end{bmatrix} = \begin{bmatrix} 0.6 & 0.6 \\ 0.4 & 0.4 \end{bmatrix} .
> $$
>
> Both columns equal the steady-state vector $\frac15\mathbf{u} = (0.6, 0.4)$: whatever the starting spot, in the long run the walker is at spot 1 with probability $0.6$ and at spot 2 with probability $0.4$ (the fractions of time spent there). This is the behavior predicted by the Perron–Frobenius theorem ([[§32 Eigenvectors and Eigenvalues#^rem-32-2|Remark: The Perron–Frobenius Theorem]]) and by [[§31 Applications to Markov Chains#^thm-31-3|Theorem §31.3]] (Lay's Theorem 18).
>
> *The lecture writes the intermediate product as $\begin{bmatrix} 3 & 3 \\ 4 & -6 \end{bmatrix}\frac15$; the final matrix $\begin{bmatrix} 0.6 & 0.6 \\ 0.4 & 0.4 \end{bmatrix}$ is correct.*
>
> *Source: 235 lectures L20, L21*

^ex-34-5
