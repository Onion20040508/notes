---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 33
bdp: "7.7"
aliases: ["BDP 7.7"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§32 Complex-Valued Eigenvalues]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§34★ Repeated Eigenvalues]] →

*Boyce–DiPrima, Section 7.7.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter.*

Placing $n$ independent solutions of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ side by side as columns gives a fundamental matrix $\mathbf{\Psi}(t)$. In terms of it the general solution is $\mathbf{\Psi}(t)\mathbf{c}$, and the initial value problem $\mathbf{x}(t_0) = \mathbf{x}^0$ is solved by $\mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0$. The special fundamental matrix $\mathbf{\Phi}(t)$ with $\mathbf{\Phi}(t_0) = \mathbf{I}$ carries the initial state $\mathbf{x}^0$ to the state $\mathbf{x}(t)$. For a constant matrix $\mathbf{A}$, this $\mathbf{\Phi}(t)$ is the matrix exponential $e^{\mathbf{A}t}$, defined by the same power series as $e^{at}$, so that $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(0) = \mathbf{x}^0$ is solved by $\mathbf{x} = e^{\mathbf{A}t}\mathbf{x}^0$, exactly as in the scalar case. Diagonalizing $\mathbf{A}$ decouples the system and gives $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$; Sections 7.8 and 7.9 build on this, with the Jordan form in place of $\mathbf{D}$ and with a forcing term.

## Fundamental Matrices

> [!definition] Definition §33.1: Fundamental Matrix
> Suppose that $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(n)}(t)$ form a fundamental set of solutions ([[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Definition §30.3]]) of
>
> $$
> \mathbf{x}' = \mathbf{P}(t)\mathbf{x} \qquad (1)
> $$
>
> on some interval $\alpha < t < \beta$. Then the matrix
>
> $$
> \mathbf{\Psi}(t) = \big(\mathbf{x}^{(1)}(t) \,\big|\, \cdots \,\big|\, \mathbf{x}^{(n)}(t)\big) = \begin{pmatrix} x_1^{(1)}(t) & \cdots & x_1^{(n)}(t) \\ \vdots & & \vdots \\ x_n^{(1)}(t) & \cdots & x_n^{(n)}(t) \end{pmatrix},
> $$
>
> whose columns are the vectors $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(n)}(t)$, is a **fundamental matrix** for the system (1). A fundamental matrix is nonsingular at every $t$ in $\alpha < t < \beta$, since its columns are linearly independent vectors there.
>
> *BDP: 7.7 (text)*

^def-33-1

> [!example] Example §33.1: A Fundamental Matrix
> Find a fundamental matrix for the system
>
> $$
> \mathbf{x}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{x} .
> $$
>
> The eigenvalues of the coefficient matrix are $r_1 = 3$ and $r_2 = -1$, with eigenvectors $(1, 2)^T$ and $(1, -2)^T$ ([[§31 Homogeneous Linear Systems with Constant Coefficients#^ex-31-1|Example §31.1]]). So
>
> $$
> \mathbf{x}^{(1)}(t) = \begin{pmatrix} e^{3t} \\ 2e^{3t} \end{pmatrix}, \qquad \mathbf{x}^{(2)}(t) = \begin{pmatrix} e^{-t} \\ -2e^{-t} \end{pmatrix}
> $$
>
> are solutions, and they are linearly independent at every $t$: $W[\mathbf{x}^{(1)}, \mathbf{x}^{(2)}](t) = e^{3t}(-2e^{-t}) - e^{-t}(2e^{3t}) = -4e^{2t} \ne 0$. A fundamental matrix is
>
> $$
> \mathbf{\Psi}(t) = \begin{pmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{pmatrix} .
> $$
>
> *BDP: Example 7.7.1*

^ex-33-1

> [!theorem] Theorem §33.1: Solving with a Fundamental Matrix
> Let $\mathbf{\Psi}(t)$ be a fundamental matrix for $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ on $\alpha < t < \beta$. Then:
>
> (a) the general solution is
>
> $$
> \mathbf{x} = \mathbf{\Psi}(t)\mathbf{c}, \qquad (6)
> $$
>
> where $\mathbf{c}$ is a constant vector with arbitrary components $c_1, \ldots, c_n$;
>
> (b) for $t_0$ in $\alpha < t < \beta$, the solution of the initial value problem $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$, $\mathbf{x}(t_0) = \mathbf{x}^0$, is
>
> $$
> \mathbf{x} = \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0 ; \qquad (10)
> $$
>
> (c) $\mathbf{\Psi}$ satisfies the matrix differential equation
>
> $$
> \mathbf{\Psi}' = \mathbf{P}(t)\mathbf{\Psi} . \qquad (11)
> $$
>
> *BDP: 7.7 (text), Equations (6), (10) and (11)*

^thm-33-1

> [!proof]+ Proof
> **(a)** Multiplying a matrix by a vector forms a linear combination of its columns:
>
> $$
> \mathbf{\Psi}(t)\mathbf{c} = c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t) . \qquad (5)
> $$
>
> By [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|Theorem §30.2]] (BDP Theorem 7.4.2) and [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|Theorem §30.1]], the expressions (5) with arbitrary constants are exactly the solutions of (1).
>
> **(b)** By (a), $\mathbf{x} = \mathbf{\Psi}(t)\mathbf{c}$ satisfies the initial condition if and only if
>
> $$
> \mathbf{\Psi}(t_0)\mathbf{c} = \mathbf{x}^0 . \qquad (8)
> $$
>
> Since $\mathbf{\Psi}(t_0)$ is nonsingular ([[§33★ Fundamental Matrices#^def-33-1|Definition §33.1]]), (8) has the unique solution $\mathbf{c} = \mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0$. Substituting it into (6) gives (10). By the uniqueness part of [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (BDP Theorem 7.1.2), this is the only solution of the initial value problem.
>
> **(c)** A matrix function is differentiated entry by entry ([[§28 Matrices#^def-28-5|Definition §28.5]]), so column $j$ of $\mathbf{\Psi}'$ is $\mathbf{x}^{(j)\prime}$. Column $j$ of $\mathbf{P}(t)\mathbf{\Psi}$ is $\mathbf{P}(t)\mathbf{x}^{(j)}$. These agree for every $j$ because each $\mathbf{x}^{(j)}$ solves (1).

^pf-33-1

*Uses:* [[§33★ Fundamental Matrices#^def-33-1|Def. §33.1]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|§30.1]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|§30.2]], [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (uniqueness), [[§28 Matrices#^def-28-5|Def. §28.5]] (derivatives of matrix functions)

In practice one solves (8) by row reduction and substitutes $\mathbf{c}$ into (6), rather than computing $\mathbf{\Psi}^{-1}(t_0)$ and using (10).

> [!definition] Definition §33.2: The Fundamental Matrix Φ
> Let $\mathbf{x}^{(1)}(t), \ldots, \mathbf{x}^{(n)}(t)$ be the solutions of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ of [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-4|Theorem §30.4]] (BDP Theorem 7.4.4), which satisfy the initial conditions
>
> $$
> \mathbf{x}^{(j)}(t_0) = \mathbf{e}^{(j)}, \qquad j = 1, \ldots, n, \qquad (12)
> $$
>
> where $\mathbf{e}^{(j)}$ has a $1$ in the $j$th position and zeros elsewhere. The fundamental matrix with these columns is denoted $\mathbf{\Phi}(t)$. It is characterized by
>
> $$
> \mathbf{\Phi}(t_0) = \mathbf{I} . \qquad (13)
> $$
>
> The symbol $\mathbf{\Phi}$ is always reserved for the fundamental matrix satisfying (13); $\mathbf{\Psi}$ denotes an arbitrary fundamental matrix.
>
> *BDP: 7.7 (text)*

^def-33-2

> [!theorem] Theorem §33.2: Solving with Φ
> (a) The solution of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$, $\mathbf{x}(t_0) = \mathbf{x}^0$, is
>
> $$
> \mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0 . \qquad (14)
> $$
>
> (b) For any fundamental matrix $\mathbf{\Psi}$,
>
> $$
> \mathbf{\Phi}(t) = \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0) .
> $$
>
> *BDP: 7.7 (text), Equation (14)*

^thm-33-2

> [!proof]+ Proof
> **(a)** Apply [[§33★ Fundamental Matrices#^thm-33-1|Theorem §33.1]](b) with $\mathbf{\Psi} = \mathbf{\Phi}$: since $\mathbf{\Phi}^{-1}(t_0) = \mathbf{I}^{-1} = \mathbf{I}$, (10) becomes (14).
>
> **(b)** By Theorem §33.1(b) and part (a), $\mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0$ and $\mathbf{\Phi}(t)\mathbf{x}^0$ both solve the same initial value problem, so they are equal for every $t$ (uniqueness, [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]]). Taking $\mathbf{x}^0 = \mathbf{e}^{(j)}$ shows that column $j$ of $\mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)$ equals column $j$ of $\mathbf{\Phi}(t)$, for each $j$.

^pf-33-2

*Uses:* [[§33★ Fundamental Matrices#^thm-33-1|§33.1]], [[§33★ Fundamental Matrices#^def-33-2|Def. §33.2]], [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (uniqueness)

$\mathbf{\Phi}(t)$ is often more complicated than a convenient $\mathbf{\Psi}(t)$, but it pays off when the same system is to be solved for many initial conditions, as for a physical system started from many initial states: each solution is then one matrix multiplication (14). $\mathbf{\Phi}(t)$ is the transformation that carries the initial state $\mathbf{x}^0$ to the state $\mathbf{x}(t)$ at time $t$.

> [!example] Example §33.2: The Fundamental Matrix with Φ(0) = I
> For the system $\mathbf{x}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{x}$ of [[§33★ Fundamental Matrices#^ex-33-1|Example §33.1]], find the fundamental matrix $\mathbf{\Phi}$ such that $\mathbf{\Phi}(0) = \mathbf{I}$.
>
> The columns of $\mathbf{\Phi}$ are the solutions with
>
> $$
> \mathbf{x}^{(1)}(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \mathbf{x}^{(2)}(0) = \begin{pmatrix} 0 \\ 1 \end{pmatrix} . \qquad (15)
> $$
>
> The general solution is $\mathbf{x} = c_1\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t} + c_2\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}$, so $\mathbf{x}(0) = (c_1 + c_2,\ 2c_1 - 2c_2)^T$.
> - For $\mathbf{x}(0) = (1, 0)^T$: $c_1 + c_2 = 1$ and $c_1 = c_2$, so $c_1 = c_2 = \frac12$.
> - For $\mathbf{x}(0) = (0, 1)^T$: $c_1 + c_2 = 0$ and $2c_1 - 2c_2 = 1$, so $c_1 = \frac14$, $c_2 = -\frac14$.
>
> Hence
>
> $$
> \mathbf{\Phi}(t) = \begin{pmatrix} \frac12 e^{3t} + \frac12 e^{-t} & \frac14 e^{3t} - \frac14 e^{-t} \\[4pt] e^{3t} - e^{-t} & \frac12 e^{3t} + \frac12 e^{-t} \end{pmatrix} . \qquad (16)
> $$
>
> **Check by [[§33★ Fundamental Matrices#^thm-33-2|Theorem §33.2]](b).** With $\mathbf{\Psi}$ from Example §33.1, $\mathbf{\Psi}(0) = \begin{pmatrix} 1 & 1 \\ 2 & -2 \end{pmatrix}$ has determinant $-4$, so $\mathbf{\Psi}^{-1}(0) = \frac{1}{-4}\begin{pmatrix} -2 & -1 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} \frac12 & \frac14 \\ \frac12 & -\frac14 \end{pmatrix}$ and
>
> $$
> \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(0) = \begin{pmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{pmatrix}\begin{pmatrix} \frac12 & \frac14 \\ \frac12 & -\frac14 \end{pmatrix} = \begin{pmatrix} \frac12 e^{3t} + \frac12 e^{-t} & \frac14 e^{3t} - \frac14 e^{-t} \\[4pt] e^{3t} - e^{-t} & \frac12 e^{3t} + \frac12 e^{-t} \end{pmatrix} .
> $$
>
> The entries of $\mathbf{\Phi}(t)$ are more complicated than those of $\mathbf{\Psi}(t)$, but now the solution for any initial condition is $\mathbf{\Phi}(t)\mathbf{x}^0$.
>
> *BDP: Example 7.7.2*

^ex-33-2

> [!remark] Remark: Method — Fundamental Matrices
> To solve $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ with a fundamental matrix:
> 1. **Find $n$ linearly independent solutions** (for constant $\mathbf{P} = \mathbf{A}$: eigenvectors as in [[§31 Homogeneous Linear Systems with Constant Coefficients#^rem-31-1|§31]], complex eigenvalues as in [[§32 Complex-Valued Eigenvalues#^rem-32-1|§32]], generalized eigenvectors as in [[§34★ Repeated Eigenvalues|§34★]]) and put them in the columns of $\mathbf{\Psi}(t)$.
> 2. **General solution:** $\mathbf{x} = \mathbf{\Psi}(t)\mathbf{c}$.
> 3. **Initial value problem:** solve $\mathbf{\Psi}(t_0)\mathbf{c} = \mathbf{x}^0$ by row reduction and substitute.
> 4. **If many initial conditions are needed**, compute $\mathbf{\Phi}(t)$ once, either column by column from the initial conditions $\mathbf{e}^{(j)}$ or as $\mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)$; then $\mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0$.

^rem-33-1

## The Matrix exp(At)

The scalar initial value problem $x' = ax$, $x(0) = x_0$ has the solution $x = x_0\exp(at)$. The corresponding problem for an $n \times n$ system,
$$
\mathbf{x}' = \mathbf{A}\mathbf{x}, \qquad \mathbf{x}(0) = \mathbf{x}^0 , \qquad (19)
$$
with $\mathbf{A}$ a constant matrix, has the solution $\mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0$ with $\mathbf{\Phi}(0) = \mathbf{I}$ ([[§33★ Fundamental Matrices#^thm-33-2|Theorem §33.2]]). This suggests that $\mathbf{\Phi}(t)$ might have an exponential character. The scalar exponential is the power series $\exp(at) = 1 + \sum_{k=1}^\infty a^kt^k/k!$, which converges for all $t$ ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]); replace $a$ by $\mathbf{A}$ and $1$ by $\mathbf{I}$.

> [!definition] Definition §33.3: The Matrix Exponential
> Let $\mathbf{A}$ be a constant $n \times n$ matrix. The **matrix exponential** $\exp(\mathbf{A}t) = e^{\mathbf{A}t}$ is the sum of the series
>
> $$
> e^{\mathbf{A}t} = \mathbf{I} + \sum_{k=1}^\infty \frac{\mathbf{A}^kt^k}{k!} = \mathbf{I} + \mathbf{A}t + \frac{\mathbf{A}^2t^2}{2!} + \cdots + \frac{\mathbf{A}^kt^k}{k!} + \cdots , \qquad (23)
> $$
>
> taken entry by entry: the $(i, j)$ entry of $e^{\mathbf{A}t}$ is the sum of the $(i, j)$ entries of the terms. (Each of these $n^2$ series converges for every real $t$, by [[§33★ Fundamental Matrices#^thm-33-3|Theorem §33.3]].)
>
> *BDP: 7.7 (text), Equation (23)*

^def-33-3

> [!theorem] Theorem §33.3: The Matrix Exponential Satisfies Φ′ = AΦ, Φ(0) = I
> Let $\mathbf{A}$ be a constant $n \times n$ matrix. Then:
>
> (a) for every real $t$, each entry of the series (23) converges (absolutely);
>
> (b) $e^{\mathbf{A}t}$ is differentiable, and
>
> $$
> \frac{d}{dt}e^{\mathbf{A}t} = \sum_{k=1}^\infty \frac{\mathbf{A}^kt^{k-1}}{(k-1)!} = \mathbf{A}e^{\mathbf{A}t} ; \qquad (24),\ (25)
> $$
>
> (c) $e^{\mathbf{A}t}\big|_{t=0} = \mathbf{I}$.
>
> *BDP: 7.7 (text), Equations (23)–(26)*

^thm-33-3

> [!proof]+ Proof
> Let $K = \max_{i,j} |a_{ij}|$. First, for $k \ge 1$ and all $i, j$,
>
> $$
> \big|(\mathbf{A}^k)_{ij}\big| \le n^{k-1}K^k . \qquad (\ast)
> $$
>
> For $k = 1$ this is the definition of $K$. If it holds for $k$, then $(\mathbf{A}^{k+1})_{ij} = \sum_{l=1}^n (\mathbf{A}^k)_{il}\,a_{lj}$ is a sum of $n$ terms, each of absolute value at most $n^{k-1}K^k \cdot K$, so $|(\mathbf{A}^{k+1})_{ij}| \le n^kK^{k+1}$.
>
> **(a)** (BDP asserts this: "it is possible to show that each element of this matrix sum converges for all $t$". Here is why.) Fix $i, j$. The $(i, j)$ entry of (23) is the power series $\sum_{k=0}^\infty c_kt^k$ with $c_k = (\mathbf{A}^k)_{ij}/k!$, where $\mathbf{A}^0 = \mathbf{I}$. By $(\ast)$, for $k \ge 1$,
>
> $$
> |c_kt^k| \le \frac{n^{k-1}K^k|t|^k}{k!} \le \frac{(nK|t|)^k}{k!} ,
> $$
>
> and $\sum_k (nK|t|)^k/k!$ converges (its sum is $e^{nK|t|}$, [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]). By the Comparison Test ([[§14 Series#^thm-14-7|451 Thm. §14.7]]) the entry series converges absolutely, for every real $t$. So each entry of $e^{\mathbf{A}t}$ is a power series in $t$ with infinite radius of convergence.
>
> **(b)** (BDP differentiates term by term; here is why that is allowed.) A power series may be differentiated term by term inside its interval of convergence ([[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]), here all of $\mathbb{R}$. Doing this in every entry gives the first equality in (24). Shifting the index ($k = m + 1$),
>
> $$
> \sum_{k=1}^\infty \frac{\mathbf{A}^kt^{k-1}}{(k-1)!} = \sum_{m=0}^\infty \frac{\mathbf{A}^{m+1}t^m}{m!} = \lim_{N\to\infty} \mathbf{A}\mathbf{S}_N(t), \qquad \mathbf{S}_N(t) = \sum_{m=0}^N \frac{\mathbf{A}^mt^m}{m!} .
> $$
>
> Each entry of $\mathbf{A}\mathbf{S}_N(t)$ is the fixed linear combination $\sum_l a_{il}(\mathbf{S}_N(t))_{lj}$ of entries of $\mathbf{S}_N(t)$, and $\mathbf{S}_N(t) \to e^{\mathbf{A}t}$ entrywise by (a). By the limit laws, $\mathbf{A}\mathbf{S}_N(t) \to \mathbf{A}e^{\mathbf{A}t}$, which is (25). (In the same way $\mathbf{S}_N(t)\mathbf{A} \to e^{\mathbf{A}t}\mathbf{A}$; since $\mathbf{S}_N\mathbf{A} = \mathbf{A}\mathbf{S}_N$, the matrices $\mathbf{A}$ and $e^{\mathbf{A}t}$ commute.)
>
> **(c)** At $t = 0$ every term with $k \ge 1$ vanishes, leaving $\mathbf{I}$.

^pf-33-3

*Uses:* [[§33★ Fundamental Matrices#^def-33-3|Def. §33.3]], [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]], [[§14 Series#^thm-14-7|451 Thm. §14.7]], [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]

> [!remark]- Connections
> - Rigorous treatment of the two steps: comparison, [[§14 Series#^thm-14-7|451 Thm. §14.7]], and term-by-term differentiation of a power series, [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]. The scalar series is [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]].
> - Norm viewpoint: with the operator norm ([[§27 Consequences of Singular Value Decomposition#^ladr-7-86|LADR 7.86]], [[§26 Boundedness and Continuity#^def-26-2|556 Def. §26.2]]) one has $\|\mathbf{A}^k\| \le \|\mathbf{A}\|^k$, so (23) converges absolutely in the Banach space ([[§11 Completeness#^def-11-2|556 Def. §11.2]]) of $n \times n$ matrices ([[§26 Boundedness and Continuity#^thm-26-5|556 Thm. §26.5]](2), [[§12 New Normed Spaces from Old#^cor-12-4|556 Cor. §12.4]]). No other subject in the vault defines the exponential of a matrix or operator; this note is its home.

> [!theorem] Theorem §33.4: The Exponential Is the Fundamental Matrix Φ
> Let $\mathbf{A}$ be a constant matrix and $\mathbf{\Phi}(t)$ the fundamental matrix of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with $\mathbf{\Phi}(0) = \mathbf{I}$. Then
>
> $$
> \mathbf{\Phi}(t) = e^{\mathbf{A}t} \quad\text{for all } t,
> $$
>
> and the solution of the initial value problem $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(0) = \mathbf{x}^0$ is
>
> $$
> \mathbf{x} = e^{\mathbf{A}t}\mathbf{x}^0 , \qquad (28)
> $$
>
> the analogue of $x = x_0e^{at}$.
>
> *BDP: 7.7 (text), Equations (27)–(28)*

^thm-33-4

> [!proof]+ Proof
> Both $\mathbf{\Phi}$ and $e^{\mathbf{A}t}$ satisfy the matrix initial value problem
>
> $$
> \mathbf{Z}' = \mathbf{A}\mathbf{Z}, \qquad \mathbf{Z}(0) = \mathbf{I} \qquad (27)
> $$
>
> ($\mathbf{\Phi}$ by [[§33★ Fundamental Matrices#^thm-33-1|Theorem §33.1]](c) and [[§33★ Fundamental Matrices#^def-33-2|Definition §33.2]], $e^{\mathbf{A}t}$ by [[§33★ Fundamental Matrices#^thm-33-3|Theorem §33.3]]). Read column by column, (27) says that column $j$ of $\mathbf{Z}$ solves $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(0) = \mathbf{e}^{(j)}$. The entries of $\mathbf{A}$ are constants, continuous for all $t$, so by the uniqueness part of [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]] (BDP Theorem 7.1.2) this problem has only one solution: column $j$ of $\mathbf{\Phi}(t)$ equals column $j$ of $e^{\mathbf{A}t}$ for each $j$. (BDP calls this "the uniqueness part of Theorem 7.1.2 (extended to matrix differential equations)"; the extension is just this column-by-column reading.) Then (28) is [[§33★ Fundamental Matrices#^thm-33-2|Theorem §33.2]](a).

^pf-33-4

*Uses:* [[§33★ Fundamental Matrices#^thm-33-1|§33.1]], [[§33★ Fundamental Matrices#^def-33-2|Def. §33.2]], [[§33★ Fundamental Matrices#^thm-33-2|§33.2]], [[§33★ Fundamental Matrices#^thm-33-3|§33.3]], [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (uniqueness)

To justify the name, $e^{\mathbf{A}t}$ should also have the algebraic properties of the exponential function. BDP outlines this in Problem 12, and uses the diagonal case of Problem 13 in the text.

> [!theorem] Proposition §33.5: Exponential of a Diagonal Matrix
> If $\mathbf{D}$ is a diagonal matrix with diagonal elements $a_1, a_2, \ldots, a_n$, then $e^{\mathbf{D}t}$ is the diagonal matrix with diagonal elements $e^{a_1t}, e^{a_2t}, \ldots, e^{a_nt}$.
>
> *BDP: Problem 7.7.13*

^prop-33-5

> [!proof]+ Proof
> A product of diagonal matrices is diagonal, with the products of the diagonal entries on its diagonal; by induction, $\mathbf{D}^k$ is diagonal with entries $a_1^k, \ldots, a_n^k$. So in the series (23) every off-diagonal entry is $0 + 0 + \cdots = 0$, and the $(i, i)$ entry is $1 + \sum_{k\ge1} a_i^kt^k/k! = e^{a_it}$ ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]).

^pf-33-5

*Uses:* [[§33★ Fundamental Matrices#^def-33-3|Def. §33.3]], [[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]

> [!theorem] Proposition §33.6: The Exponential Law
> Let $\mathbf{A}$ be a constant matrix and $\mathbf{\Phi}(t) = e^{\mathbf{A}t}$. For all real $t$ and $s$:
>
> (a) $\mathbf{\Phi}(t)\mathbf{\Phi}(s) = \mathbf{\Phi}(t + s)$, that is, $e^{\mathbf{A}t}e^{\mathbf{A}s} = e^{\mathbf{A}(t+s)}$;
>
> (b) $\mathbf{\Phi}(t)\mathbf{\Phi}(-t) = \mathbf{I}$, that is, $e^{\mathbf{A}t}e^{-\mathbf{A}t} = \mathbf{I}$, so $\mathbf{\Phi}(-t) = \mathbf{\Phi}^{-1}(t)$;
>
> (c) $\mathbf{\Phi}(t - s) = \mathbf{\Phi}(t)\mathbf{\Phi}^{-1}(s)$.
>
> *BDP: Problem 7.7.12*

^prop-33-6

> [!proof]+ Proof
> **(a)** Fix $s$ and regard $t$ as the variable. Let $\mathbf{Z}_1(t) = \mathbf{\Phi}(t)\mathbf{\Phi}(s)$ and $\mathbf{Z}_2(t) = \mathbf{\Phi}(t + s)$. Since $\mathbf{\Phi}(s)$ is a constant matrix, $\mathbf{Z}_1' = \mathbf{\Phi}'(t)\mathbf{\Phi}(s) = \mathbf{A}\mathbf{\Phi}(t)\mathbf{\Phi}(s) = \mathbf{A}\mathbf{Z}_1$, and $\mathbf{Z}_1(0) = \mathbf{I}\,\mathbf{\Phi}(s) = \mathbf{\Phi}(s)$. By the chain rule, $\mathbf{Z}_2'(t) = \mathbf{\Phi}'(t + s) = \mathbf{A}\mathbf{\Phi}(t + s) = \mathbf{A}\mathbf{Z}_2$, and $\mathbf{Z}_2(0) = \mathbf{\Phi}(s)$. So column $j$ of $\mathbf{Z}_1$ and column $j$ of $\mathbf{Z}_2$ solve the same initial value problem $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(0) =$ column $j$ of $\mathbf{\Phi}(s)$; by uniqueness ([[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|Theorem §27.3]]) they are equal. Hence $\mathbf{Z}_1 = \mathbf{Z}_2$.
>
> **(b)** Put $s = -t$ in (a): $\mathbf{\Phi}(t)\mathbf{\Phi}(-t) = \mathbf{\Phi}(0) = \mathbf{I}$. A square matrix with a one-sided inverse is invertible with that inverse, so $\mathbf{\Phi}(-t) = \mathbf{\Phi}^{-1}(t)$.
>
> **(c)** By (a) and (b), $\mathbf{\Phi}(t - s) = \mathbf{\Phi}(t)\mathbf{\Phi}(-s) = \mathbf{\Phi}(t)\mathbf{\Phi}^{-1}(s)$.

^pf-33-6

*Uses:* [[§33★ Fundamental Matrices#^thm-33-3|§33.3]], [[§33★ Fundamental Matrices#^thm-33-4|§33.4]], [[§27 Introduction to Systems of First-Order Linear Equations#^thm-27-3|§27.3]] (uniqueness)

> [!remark] Remark: Starting at t₀ ≠ 0; Sums in the Exponent
> - **Initial time $t_0$.** For constant $\mathbf{A}$, the fundamental matrix with $\mathbf{\Phi}(t_0) = \mathbf{I}$ is $e^{\mathbf{A}(t - t_0)}$: by [[§33★ Fundamental Matrices#^thm-33-2|Theorem §33.2]](b) with $\mathbf{\Psi} = e^{\mathbf{A}t}$ and [[§33★ Fundamental Matrices#^prop-33-6|Proposition §33.6]](c), it is $e^{\mathbf{A}t}(e^{\mathbf{A}t_0})^{-1} = e^{\mathbf{A}(t - t_0)}$. So $\mathbf{x}' = \mathbf{A}\mathbf{x}$, $\mathbf{x}(t_0) = \mathbf{x}^0$ has the solution $\mathbf{x} = e^{\mathbf{A}(t - t_0)}\mathbf{x}^0$.
> - **What the law does not say.** Proposition §33.6 multiplies exponentials of the *same* matrix. For two matrices $\mathbf{B}$, $\mathbf{C}$ that do not commute, $e^{\mathbf{B}}e^{\mathbf{C}}$ (the series (23) at $t = 1$) is in general not $e^{\mathbf{B} + \mathbf{C}}$. For $\mathbf{B} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\mathbf{C} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $\mathbf{B}^2 = \mathbf{C}^2 = \mathbf{0}$, so $e^{\mathbf{B}}e^{\mathbf{C}} = (\mathbf{I} + \mathbf{B})(\mathbf{I} + \mathbf{C}) = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$; but $(\mathbf{B} + \mathbf{C})^2 = \mathbf{I}$, so $e^{\mathbf{B} + \mathbf{C}} = \cosh 1\,\mathbf{I} + \sinh 1\,(\mathbf{B} + \mathbf{C})$, whose diagonal entries are $\cosh 1 \approx 1.543$.

^rem-33-2

> [!remark]- Remark: Picard Iteration Builds the Series
> The method of successive approximations of [[§11 The Existence and Uniqueness Theorem|§11]] (BDP 2.8) applies to (19) and produces exactly the partial sums of (23) (BDP, Problem 15). A solution $\mathbf{x} = \boldsymbol{\phi}(t)$ satisfies the integral equation $\boldsymbol{\phi}(t) = \mathbf{x}^0 + \int_0^t \mathbf{A}\boldsymbol{\phi}(s)\,ds$. Starting from $\boldsymbol{\phi}^{(0)}(t) = \mathbf{x}^0$ and setting $\boldsymbol{\phi}^{(k+1)}(t) = \mathbf{x}^0 + \int_0^t \mathbf{A}\boldsymbol{\phi}^{(k)}(s)\,ds$, induction gives
>
> $$
> \boldsymbol{\phi}^{(k)}(t) = \Big(\mathbf{I} + \mathbf{A}t + \mathbf{A}^2\frac{t^2}{2!} + \cdots + \mathbf{A}^k\frac{t^k}{k!}\Big)\mathbf{x}^0 ,
> $$
>
> because $\int_0^t \mathbf{A}\,\mathbf{A}^m\frac{s^m}{m!}\mathbf{x}^0\,ds = \mathbf{A}^{m+1}\frac{t^{m+1}}{(m+1)!}\mathbf{x}^0$. Letting $k \to \infty$ gives $\boldsymbol{\phi}(t) = e^{\mathbf{A}t}\mathbf{x}^0$, in agreement with (28).

^rem-33-3

## Diagonalizable Matrices

A system of linear equations, algebraic or differential, is hard mainly because it is *coupled*: some equations involve more than one unknown, so all must be solved simultaneously. If each equation involves only one unknown, each can be solved by itself. So one tries to transform the system into an equivalent *uncoupled* one, which means transforming the coefficient matrix $\mathbf{A}$ into a *diagonal* matrix. Eigenvectors do this.

> [!definition] Definition §33.4: Similar Matrices; Diagonalizable Matrix
> Let $\mathbf{T}$ be a nonsingular matrix. Passing from $\mathbf{A}$ to $\mathbf{T}^{-1}\mathbf{A}\mathbf{T}$ is a **similarity transformation**, and $\mathbf{A}$ is said to be **similar** to $\mathbf{T}^{-1}\mathbf{A}\mathbf{T}$. If $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D}$ is a diagonal matrix for some nonsingular $\mathbf{T}$, then $\mathbf{A}$ is **diagonalizable**.
>
> *BDP: 7.7 (text)*

^def-33-4

> [!theorem] Theorem §33.7: Diagonalization by Eigenvectors
> Let $\mathbf{A}$ be an $n \times n$ matrix.
>
> (a) Suppose $\mathbf{A}$ has a full set of $n$ linearly independent eigenvectors $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(n)}$, with corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$. (This is certainly the case if the eigenvalues are all different, or if $\mathbf{A}$ is Hermitian.) Form the matrix $\mathbf{T}$ whose columns are the eigenvectors:
>
> $$
> \mathbf{T} = \begin{pmatrix} \xi_1^{(1)} & \cdots & \xi_1^{(n)} \\ \vdots & & \vdots \\ \xi_n^{(1)} & \cdots & \xi_n^{(n)} \end{pmatrix} . \qquad (29)
> $$
>
> Then $\mathbf{T}$ is nonsingular and
>
> $$
> \mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D} = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix} . \qquad (31),\ (32)
> $$
>
> The similarity transformation leaves the eigenvalues of $\mathbf{A}$ unchanged and transforms its eigenvectors into the coordinate vectors $\mathbf{e}^{(1)}, \ldots, \mathbf{e}^{(n)}$.
>
> (b) If $\mathbf{A}$ is Hermitian and its eigenvectors are chosen mutually orthogonal and normalized, $(\boldsymbol{\xi}^{(i)}, \boldsymbol{\xi}^{(i)}) = 1$, then $\mathbf{T}^{-1} = \mathbf{T}^*$: the inverse of $\mathbf{T}$ is its adjoint (the transpose of its complex conjugate).
>
> (c) If $\mathbf{A}$ has fewer than $n$ linearly independent eigenvectors, there is no matrix $\mathbf{T}$ such that $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D}$ is diagonal: $\mathbf{A}$ is not diagonalizable.
>
> *BDP: 7.7 (text), Equations (29)–(32)*

^thm-33-7

> [!proof]+ Proof
> **(a)** The parenthetical cases are results of BDP 7.3: eigenvectors for different eigenvalues are linearly independent ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|Theorem §29.4]]), and a Hermitian matrix has a full set of $n$ (mutually orthogonal) eigenvectors ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|Theorem §29.5]]). Since the columns of $\mathbf{T}$ are linearly independent, $\det\mathbf{T} \ne 0$ ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|Theorem §29.2]]), so $\mathbf{T}^{-1}$ exists. Column $k$ of $\mathbf{A}\mathbf{T}$ is $\mathbf{A}\boldsymbol{\xi}^{(k)} = \lambda_k\boldsymbol{\xi}^{(k)}$, and column $k$ of $\mathbf{T}\mathbf{D}$ is $\mathbf{T}(\lambda_k\mathbf{e}^{(k)}) = \lambda_k\boldsymbol{\xi}^{(k)}$. Hence
>
> $$
> \mathbf{A}\mathbf{T} = \begin{pmatrix} \lambda_1\xi_1^{(1)} & \cdots & \lambda_n\xi_1^{(n)} \\ \vdots & & \vdots \\ \lambda_1\xi_n^{(1)} & \cdots & \lambda_n\xi_n^{(n)} \end{pmatrix} = \mathbf{T}\mathbf{D}, \qquad (30)
> $$
>
> and multiplying on the left by $\mathbf{T}^{-1}$ gives (32). The eigenvalues of $\mathbf{D}$ are its diagonal entries $\lambda_1, \ldots, \lambda_n$, those of $\mathbf{A}$. Finally $\mathbf{T}\mathbf{e}^{(k)} = \boldsymbol{\xi}^{(k)}$, so $\mathbf{T}^{-1}\boldsymbol{\xi}^{(k)} = \mathbf{e}^{(k)}$.
>
> **(b)** (BDP: "it is easy to verify"; here is the verification.) With the inner product $(\mathbf{x}, \mathbf{y}) = \sum_k x_k\overline{y_k}$ of [[§28 Matrices#^def-28-new2|Definition §28.3]],
>
> $$
> (\mathbf{T}^*\mathbf{T})_{ij} = \sum_{k=1}^n \overline{T_{ki}}\,T_{kj} = \sum_{k=1}^n \xi_k^{(j)}\,\overline{\xi_k^{(i)}} = (\boldsymbol{\xi}^{(j)}, \boldsymbol{\xi}^{(i)}) = \begin{cases} 1, & i = j, \\ 0, & i \ne j. \end{cases}
> $$
>
> So $\mathbf{T}^*\mathbf{T} = \mathbf{I}$, and since $\mathbf{T}$ is square, $\mathbf{T}^{-1} = \mathbf{T}^*$.
>
> **(c)** (BDP states this without argument.) Suppose $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D}$ with $\mathbf{D}$ diagonal, entries $d_1, \ldots, d_n$. Then $\mathbf{A}\mathbf{T} = \mathbf{T}\mathbf{D}$, and comparing columns as in (a), $\mathbf{A}\mathbf{t}^{(k)} = d_k\mathbf{t}^{(k)}$ for each column $\mathbf{t}^{(k)}$ of $\mathbf{T}$. The columns of the nonsingular matrix $\mathbf{T}$ are nonzero and linearly independent, so they are $n$ linearly independent eigenvectors of $\mathbf{A}$.

^pf-33-7

*Uses:* [[§33★ Fundamental Matrices#^def-33-4|Def. §33.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|§29.2]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|§29.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|§29.5]], [[§28 Matrices#^def-28-new2|Def. §28.3]] (inner product)

> [!remark]- Connections
> - The same theorem in Lay: [[§34 Diagonalization#^thm-34-1|235 Thm. §34.1]] (written $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$, with $\mathbf{P} = \mathbf{T}$); rigorous operator form, [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]].
> - Part (b) is the spectral theorem: [[§23 Spectral Theorem#^ladr-7-31|LADR 7.31]] (complex; normal operators, which include the Hermitian ones), and for real symmetric matrices, where $\mathbf{T}^{-1} = \mathbf{T}^T$, [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]].

Now return to $\mathbf{x}' = \mathbf{A}\mathbf{x}$. Sections 7.5 and 7.6 started from the trial solution $\mathbf{x} = \boldsymbol{\xi}e^{rt}$; diagonalization gives another viewpoint, based on the coefficient matrix.

> [!theorem] Theorem §33.8: Fundamental Matrix by Diagonalization
> Let $\mathbf{A}$ have $n$ linearly independent eigenvectors $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(n)}$ with eigenvalues $r_1, \ldots, r_n$, and let $\mathbf{T}$ and $\mathbf{D}$ be as in [[§33★ Fundamental Matrices#^thm-33-7|Theorem §33.7]]. Then:
>
> (a) the substitution $\mathbf{x} = \mathbf{T}\mathbf{y}$ (38) transforms $\mathbf{x}' = \mathbf{A}\mathbf{x}$ (37) into the uncoupled system
>
> $$
> \mathbf{y}' = \mathbf{D}\mathbf{y} ; \qquad (41)
> $$
>
> (b) $\mathbf{Q}(t) = e^{\mathbf{D}t} = \operatorname{diag}(e^{r_1t}, \ldots, e^{r_nt})$ is a fundamental matrix for (41);
>
> (c) $\mathbf{\Psi}(t) = \mathbf{T}\mathbf{Q}(t)$ is a fundamental matrix for (37), namely
>
> $$
> \mathbf{\Psi}(t) = \begin{pmatrix} \xi_1^{(1)}e^{r_1t} & \cdots & \xi_1^{(n)}e^{r_nt} \\ \vdots & & \vdots \\ \xi_n^{(1)}e^{r_1t} & \cdots & \xi_n^{(n)}e^{r_nt} \end{pmatrix} ; \qquad (43),\ (44)
> $$
>
> (d) $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$.
>
> *BDP: 7.7 (text), Equations (37)–(44)*

^thm-33-8

> [!proof]+ Proof
> **(a)** $\mathbf{T}$ is constant, so $\mathbf{x}' = \mathbf{T}\mathbf{y}'$, and (37) becomes $\mathbf{T}\mathbf{y}' = \mathbf{A}\mathbf{T}\mathbf{y}$ (39). Multiplying by $\mathbf{T}^{-1}$ gives $\mathbf{y}' = (\mathbf{T}^{-1}\mathbf{A}\mathbf{T})\mathbf{y}$ (40), which is (41) by [[§33★ Fundamental Matrices#^thm-33-7|Theorem §33.7]].
>
> **(b)** By [[§33★ Fundamental Matrices#^prop-33-5|Proposition §33.5]], $e^{\mathbf{D}t}$ is the diagonal matrix with entries $e^{r_kt}$. By [[§33★ Fundamental Matrices#^thm-33-3|Theorem §33.3]], $\mathbf{Q}' = \mathbf{D}\mathbf{Q}$, so each column of $\mathbf{Q}$ solves (41), and $\det\mathbf{Q}(t) = e^{(r_1 + \cdots + r_n)t} \ne 0$, so the columns are linearly independent at every $t$.
>
> **(c)** $\mathbf{\Psi}' = \mathbf{T}\mathbf{Q}' = \mathbf{T}\mathbf{D}\mathbf{Q} = \mathbf{A}\mathbf{T}\mathbf{Q} = \mathbf{A}\mathbf{\Psi}$, using $\mathbf{T}\mathbf{D} = \mathbf{A}\mathbf{T}$ (30). So the columns of $\mathbf{\Psi}$ solve (37), and $\det\mathbf{\Psi}(t) = \det\mathbf{T}\,\det\mathbf{Q}(t) \ne 0$. Column $k$ of $\mathbf{T}\mathbf{Q}$ is $\mathbf{T}(e^{r_kt}\mathbf{e}^{(k)}) = e^{r_kt}\boldsymbol{\xi}^{(k)}$, which gives (44).
>
> **(d)** $\mathbf{\Psi}(0) = \mathbf{T}\mathbf{Q}(0) = \mathbf{T}$. By Theorems [[§33★ Fundamental Matrices#^thm-33-4|§33.4]] and [[§33★ Fundamental Matrices#^thm-33-2|§33.2]](b), $e^{\mathbf{A}t} = \mathbf{\Phi}(t) = \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(0) = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$.

^pf-33-8

*Uses:* [[§33★ Fundamental Matrices#^thm-33-7|§33.7]], [[§33★ Fundamental Matrices#^prop-33-5|§33.5]], [[§33★ Fundamental Matrices#^thm-33-3|§33.3]], [[§33★ Fundamental Matrices#^thm-33-4|§33.4]], [[§33★ Fundamental Matrices#^thm-33-2|§33.2]], [[§33★ Fundamental Matrices#^def-33-1|Def. §33.1]]

> [!remark]- Connections
> - Lay decouples $\mathbf{x}' = A\mathbf{x}$ by the same change of variable: [[§38 Applications to Differential Equations#^thm-38-3|235 Thm. §38.3]].

The columns of $\mathbf{\Psi}(t)$ in (44) are the solutions $\boldsymbol{\xi}^{(k)}e^{r_kt}$ of [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|Theorem §31.2]] (BDP 7.5). So diagonalization offers no computational advantage over the method of Section 7.5: either way one must find the eigenvalues and eigenvectors of $\mathbf{A}$. What it adds is the formula $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$ and the idea of decoupling, which carries over to Jordan forms ([[§34★ Repeated Eigenvalues|§34★]]) and to nonhomogeneous systems ([[§35★ Nonhomogeneous Linear Systems|§35★]]).

> [!example] Example §33.3: Diagonalizing A and Recovering Ψ and Φ
> Let $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}$ (33). Find the similarity transformation matrix $\mathbf{T}$, show that $\mathbf{A}$ can be diagonalized, and use the diagonal system to obtain a fundamental matrix for $\mathbf{x}' = \mathbf{A}\mathbf{x}$.
>
> **Diagonalizing.** The eigenvalues and eigenvectors are $r_1 = 3$, $\boldsymbol{\xi}^{(1)} = (1, 2)^T$ and $r_2 = -1$, $\boldsymbol{\xi}^{(2)} = (1, -2)^T$ ([[§33★ Fundamental Matrices#^ex-33-1|Example §33.1]]). So
>
> $$
> \mathbf{T} = \begin{pmatrix} 1 & 1 \\ 2 & -2 \end{pmatrix}, \qquad \det\mathbf{T} = -4, \qquad \mathbf{T}^{-1} = \frac{1}{-4}\begin{pmatrix} -2 & -1 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} \frac12 & \frac14 \\[2pt] \frac12 & -\frac14 \end{pmatrix} . \qquad (35)
> $$
>
> Then $\mathbf{A}\mathbf{T} = \begin{pmatrix} 3 & -1 \\ 6 & 2 \end{pmatrix}$ and
>
> $$
> \mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \begin{pmatrix} \frac12 & \frac14 \\[2pt] \frac12 & -\frac14 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ 6 & 2 \end{pmatrix} = \begin{pmatrix} \frac32 + \frac32 & -\frac12 + \frac12 \\[2pt] \frac32 - \frac32 & -\frac12 - \frac12 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} = \mathbf{D} . \qquad (36)
> $$
>
> **The uncoupled system.** $\mathbf{x} = \mathbf{T}\mathbf{y}$ turns $\mathbf{x}' = \mathbf{A}\mathbf{x}$ into $\mathbf{y}' = \mathbf{D}\mathbf{y}$, i.e. $y_1' = 3y_1$, $y_2' = -y_2$ (46). Multiplying $\mathbf{D}$ by itself,
>
> $$
> \mathbf{D}^2 = \begin{pmatrix} 9 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \mathbf{D}^3 = \begin{pmatrix} 27 & 0 \\ 0 & -1 \end{pmatrix}, \qquad \ldots, \qquad \mathbf{D}^k = \begin{pmatrix} 3^k & 0 \\ 0 & (-1)^k \end{pmatrix},
> $$
>
> so by the series (23) ([[§33★ Fundamental Matrices#^prop-33-5|Proposition §33.5]]), $e^{\mathbf{D}t} = \begin{pmatrix} e^{3t} & 0 \\ 0 & e^{-t} \end{pmatrix}$ (48).
>
> **Back to $\mathbf{x}$.**
>
> $$
> \mathbf{\Psi}(t) = \mathbf{T}e^{\mathbf{D}t} = \begin{pmatrix} 1 & 1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} e^{3t} & 0 \\ 0 & e^{-t} \end{pmatrix} = \begin{pmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{pmatrix}, \qquad (49)
> $$
>
> the fundamental matrix of Example §33.1. Going one step further ([[§33★ Fundamental Matrices#^thm-33-8|Theorem §33.8]](d)),
>
> $$
> e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1} = \begin{pmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{pmatrix}\begin{pmatrix} \frac12 & \frac14 \\[2pt] \frac12 & -\frac14 \end{pmatrix} = \begin{pmatrix} \frac12 e^{3t} + \frac12 e^{-t} & \frac14 e^{3t} - \frac14 e^{-t} \\[4pt] e^{3t} - e^{-t} & \frac12 e^{3t} + \frac12 e^{-t} \end{pmatrix},
> $$
>
> which is the matrix $\mathbf{\Phi}(t)$ of [[§33★ Fundamental Matrices#^ex-33-2|Example §33.2]], as [[§33★ Fundamental Matrices#^thm-33-4|Theorem §33.4]] predicts.
>
> *BDP: Examples 7.7.3 and 7.7.4*

^ex-33-3

> [!remark] Remark: Method — Solving x′ = Ax with the Matrix Exponential
> For a constant matrix $\mathbf{A}$ with $n$ linearly independent eigenvectors:
> 1. **Find the eigenvalues** $r_1, \ldots, r_n$ and **independent eigenvectors** $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(n)}$. If there are fewer than $n$, use generalized eigenvectors and the Jordan form instead ([[§34★ Repeated Eigenvalues|§34★]]).
> 2. **Form** $\mathbf{T} = (\boldsymbol{\xi}^{(1)} | \cdots | \boldsymbol{\xi}^{(n)})$ and $e^{\mathbf{D}t} = \operatorname{diag}(e^{r_1t}, \ldots, e^{r_nt})$. If $\mathbf{A}$ is Hermitian (real symmetric), normalize orthogonal eigenvectors so that $\mathbf{T}^{-1} = \mathbf{T}^{\ast}$.
> 3. **Compute** $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$.
> 4. **Solve:** $\mathbf{x} = e^{\mathbf{A}t}\mathbf{x}^0$ for $\mathbf{x}(0) = \mathbf{x}^0$, or $\mathbf{x} = e^{\mathbf{A}(t - t_0)}\mathbf{x}^0$ for $\mathbf{x}(t_0) = \mathbf{x}^0$ ([[§33★ Fundamental Matrices#^rem-33-2|Remark: Starting at t₀]]).
>
> For complex eigenvalues the same formulas hold with complex $\mathbf{T}$ and $\mathbf{D}$; the product $\mathbf{T}e^{\mathbf{D}t}\mathbf{T}^{-1}$ is real when $\mathbf{A}$ is real, since it equals the real series (23).

^rem-33-4
