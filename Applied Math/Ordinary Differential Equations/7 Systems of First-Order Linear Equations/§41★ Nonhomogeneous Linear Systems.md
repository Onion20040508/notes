---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: "41★"
bdp: "7.9"
aliases: ["BDP 7.9"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§40★ Repeated Eigenvalues]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§42 The Matrices (1 1; 4 1) and (0 1 1; 1 0 1; 1 1 0)]] →

*Boyce–DiPrima, Section 7.9.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter.*

For the nonhomogeneous system $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$, the general solution is the general solution of the homogeneous system plus one particular solution, as for a single equation in [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-21-2|Theorem §21.2]]. The section gives four ways to find the particular solution, each carried over from earlier chapters. Diagonalization uncouples a constant-coefficient system into $n$ first-order linear equations. Undetermined coefficients guesses the form for exponential, polynomial and sinusoidal forcing. Variation of parameters works for any $\mathbf{P}(t)$ once a fundamental matrix is known, and for constant $\mathbf{A}$ it becomes $\mathbf{x} = e^{\mathbf{A}t}\mathbf{x}^0 + \int_0^t e^{\mathbf{A}(t-s)}\mathbf{g}(s)\,ds$. Laplace transforms turn the system into algebra through the transfer matrix $(s\mathbf{I} - \mathbf{A})^{-1}$. BDP applies all four to the same system, so the answers can be compared.

> [!theorem] Theorem §41.1: Structure of the General Solution
> Let the $n \times n$ matrix $\mathbf{P}(t)$ and the $n \times 1$ vector $\mathbf{g}(t)$ be continuous for $\alpha < t < \beta$. Then the general solution of
>
> $$
> \mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t) \qquad (1)
> $$
>
> can be expressed as
>
> $$
> \mathbf{x} = c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t) + \mathbf{v}(t), \qquad (2)
> $$
>
> where $c_1\mathbf{x}^{(1)}(t) + \cdots + c_n\mathbf{x}^{(n)}(t)$ is the general solution of the homogeneous system $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ ([[§36 Basic Theory of Systems of First-Order Linear Equations#^def-36-4|Definition §36.4]]) and $\mathbf{v}(t)$ is a particular solution of (1).
>
> *BDP: 7.9 (text), Equation (2); Problem 7.9.12*

^thm-41-1

> [!proof]+ Proof
> Let $\mathbf{x} = \boldsymbol{\phi}(t)$ be any solution of (1). Then
>
> $$
> (\boldsymbol{\phi} - \mathbf{v})' = \mathbf{P}\boldsymbol{\phi} + \mathbf{g} - \mathbf{P}\mathbf{v} - \mathbf{g} = \mathbf{P}(\boldsymbol{\phi} - \mathbf{v}),
> $$
>
> so $\mathbf{u} = \boldsymbol{\phi} - \mathbf{v}$ solves the homogeneous system. Since $\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}$ form a fundamental set, [[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-2|Theorem §36.2]] gives $\mathbf{u} = c_1\mathbf{x}^{(1)} + \cdots + c_n\mathbf{x}^{(n)}$ for some constants. Hence $\boldsymbol{\phi}$ has the form (2). Conversely, $\mathbf{u} = c_1\mathbf{x}^{(1)} + \cdots + c_n\mathbf{x}^{(n)}$ solves the homogeneous system by the Principle of Superposition ([[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-1|Theorem §36.1]]), so $(\mathbf{u} + \mathbf{v})' = \mathbf{P}\mathbf{u} + \mathbf{P}\mathbf{v} + \mathbf{g} = \mathbf{P}(\mathbf{u} + \mathbf{v}) + \mathbf{g}$: every expression (2) solves (1).

^pf-41-1

*Uses:* [[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-1|§36.1]], [[§36 Basic Theory of Systems of First-Order Linear Equations#^thm-36-2|§36.2]], [[§36 Basic Theory of Systems of First-Order Linear Equations#^def-36-3|Def. §36.3]], [[§36 Basic Theory of Systems of First-Order Linear Equations#^def-36-4|Def. §36.4]]

> [!remark]- Connections
> - The same structure for linear algebraic systems: [[§6 Solution Sets of Linear Systems#^thm-6-3|235 Thm. §6.3]] (solutions of $A\mathbf{x} = \mathbf{b}$ are a translate of the solutions of $A\mathbf{x} = \mathbf{0}$). In LADR's terms, the solution set of (1) is a translate $\mathbf{v} + U$ of the $n$-dimensional solution space $U$ of the homogeneous system, [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]].

## Diagonalization

Consider first a constant coefficient matrix,
$$
\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{g}(t), \qquad (3)
$$
where $\mathbf{A}$ is an $n \times n$ diagonalizable constant matrix. Diagonalizing $\mathbf{A}$ as in [[§39★ Fundamental Matrices#^thm-39-7|Theorem §39.7]] transforms (3) into a system that is readily solved.

> [!theorem] Theorem §41.2: Uncoupling x′ = Ax + g by Diagonalization
> Let $\mathbf{A}$ have linearly independent eigenvectors $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(n)}$ with eigenvalues $r_1, \ldots, r_n$, let $\mathbf{T}$ be the matrix with these columns and $\mathbf{D} = \operatorname{diag}(r_1, \ldots, r_n)$. Then the substitution
>
> $$
> \mathbf{x} = \mathbf{T}\mathbf{y} \qquad (4)
> $$
>
> transforms (3) into
>
> $$
> \mathbf{y}' = \mathbf{D}\mathbf{y} + \mathbf{h}(t), \qquad \mathbf{h}(t) = \mathbf{T}^{-1}\mathbf{g}(t), \qquad (5)
> $$
>
> that is, into $n$ uncoupled first-order linear equations
>
> $$
> y_j'(t) = r_jy_j(t) + h_j(t), \qquad j = 1, \ldots, n, \qquad (6)
> $$
>
> whose solutions are
>
> $$
> y_j(t) = e^{r_jt}\int_{t_0}^t e^{-r_js}h_j(s)\,ds + c_je^{r_jt}, \qquad j = 1, \ldots, n, \qquad (7)
> $$
>
> with arbitrary constants $c_j$. In $\mathbf{x} = \mathbf{T}\mathbf{y}$, the terms $c_je^{r_jt}$ produce the general solution of $\mathbf{x}' = \mathbf{A}\mathbf{x}$, and the integrals a particular solution of (3).
>
> *BDP: 7.9 (text), Equations (4)–(7)*

^thm-41-2

> [!proof]+ Proof
> Since $\mathbf{T}$ is constant, substituting (4) into (3) gives $\mathbf{T}\mathbf{y}' = \mathbf{A}\mathbf{T}\mathbf{y} + \mathbf{g}(t)$. Multiplying on the left by $\mathbf{T}^{-1}$ and using $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{D}$ ([[§39★ Fundamental Matrices#^thm-39-7|Theorem §39.7]]) gives (5); since $\mathbf{D}$ is diagonal, row $j$ of (5) is (6), in which $h_j$ is a linear combination of $g_1, \ldots, g_n$ with coefficients from row $j$ of $\mathbf{T}^{-1}$.
>
> Each equation (6) is first-order linear with a constant coefficient, as in [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-1|Theorem §5.1]] (BDP 2.1); the same computation works for complex $r_j$. With the integrating factor $e^{-r_jt}$,
>
> $$
> \big(e^{-r_jt}y_j\big)' = e^{-r_jt}\big(y_j' - r_jy_j\big) = e^{-r_jt}h_j(t),
> $$
>
> and integrating from $t_0$ to $t$ gives $e^{-r_jt}y_j(t) = \int_{t_0}^t e^{-r_js}h_j(s)\,ds + c_j$ with $c_j = e^{-r_jt_0}y_j(t_0)$; this is (7). Conversely, every $\mathbf{y}$ of the form (7) solves (5), and then $\mathbf{x} = \mathbf{T}\mathbf{y}$ solves (3), by the same computation read backwards. Finally $\mathbf{T}\,(c_1e^{r_1t}, \ldots, c_ne^{r_nt})^T = \sum_j c_j\boldsymbol{\xi}^{(j)}e^{r_jt} = \mathbf{\Psi}(t)\mathbf{c}$ with the fundamental matrix $\mathbf{\Psi} = \mathbf{T}e^{\mathbf{D}t}$ of [[§39★ Fundamental Matrices#^thm-39-8|Theorem §39.8]](c), so it is the general solution of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ ([[§39★ Fundamental Matrices#^thm-39-1|Theorem §39.1]](a)). The remaining part of $\mathbf{T}\mathbf{y}$ (all $c_j = 0$) is a solution of (3), hence a particular solution, and by [[§41★ Nonhomogeneous Linear Systems#^thm-41-1|Theorem §41.1]] the sum is the general solution of (3).

^pf-41-2

*Uses:* [[§39★ Fundamental Matrices#^thm-39-1|§39.1]], [[§39★ Fundamental Matrices#^thm-39-7|§39.7]], [[§39★ Fundamental Matrices#^thm-39-8|§39.8]], [[§41★ Nonhomogeneous Linear Systems#^thm-41-1|§41.1]], [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-1|§5.1]]

> [!remark]- Connections
> - The homogeneous case is Lay's decoupling, [[§46 Applications to Differential Equations#^thm-46-3|235 Thm. §46.3]]; each equation (6) is solved by [[§70 Linear Equations#^thm-70-1|Calc Thm. §70.1]] (Stewart's treatment of linear equations).

> [!remark] Remark: Method — Diagonalization
> To find the general solution of $\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{g}(t)$ with $\mathbf{A}$ constant and diagonalizable:
> 1. **Find the eigenvalues** $r_j$ and **independent eigenvectors** $\boldsymbol{\xi}^{(j)}$ of $\mathbf{A}$; form $\mathbf{T}$ and $\mathbf{D}$.
> 2. **Find $\mathbf{T}^{-1}$.** If $\mathbf{A}$ is [[§35 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-35-8|Hermitian]] (real symmetric), normalize the eigenvectors so that $(\boldsymbol{\xi}^{(j)}, \boldsymbol{\xi}^{(j)}) = 1$; then $\mathbf{T}^{-1} = \mathbf{T}^{\ast}$ ($= \mathbf{T}^T$ for real $\mathbf{T}$) needs no calculation ([[§39★ Fundamental Matrices#^thm-39-7|Theorem §39.7]](b)).
> 3. **Compute** $\mathbf{h} = \mathbf{T}^{-1}\mathbf{g}$ and solve each scalar equation $y_j' - r_jy_j = h_j$ by an integrating factor.
> 4. **Transform back:** $\mathbf{x} = \mathbf{T}\mathbf{y}$.
>
> If $\mathbf{A}$ is not diagonalizable, use its Jordan form $\mathbf{J}$ ([[§40★ Repeated Eigenvalues#^def-40-3|Definition §40.3]]) and a matrix $\mathbf{T}$ of eigenvectors and generalized eigenvectors. The equations for $y_1, \ldots, y_n$ are then not totally uncoupled, since some rows of $\mathbf{J}$ have two nonzero entries, an eigenvalue on the diagonal and a $1$ to its right. But they can still be solved consecutively, starting with $y_n$, as in [[§40★ Repeated Eigenvalues#^ex-40-3|Example §40.3]].

^rem-41-1

> [!example] Example §41.1: Solution by Diagonalization
> Find the general solution of
>
> $$
> \mathbf{x}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{x} + \begin{pmatrix} 2e^{-t} \\ 3t \end{pmatrix} = \mathbf{A}\mathbf{x} + \mathbf{g}(t) . \qquad (8)
> $$
>
> **Homogeneous system.** $\det(\mathbf{A} - r\mathbf{I}) = (r + 2)^2 - 1 = (r + 1)(r + 3)$, so $r_1 = -3$, $r_2 = -1$. From $\mathbf{A} + 3\mathbf{I} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $\mathbf{A} + \mathbf{I} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$,
>
> $$
> \boldsymbol{\xi}^{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad \boldsymbol{\xi}^{(2)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad (9)
> $$
>
> and the general solution of the homogeneous system is ([[§37 Homogeneous Linear Systems with Constant Coefficients#^thm-37-2|Theorem §37.2]])
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-3t} + c_2\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{-t} . \qquad (10)
> $$
>
> **The transformation.** $\mathbf{A}$ is real and symmetric and its eigenvectors (9) are orthogonal, so normalizing them (both have length $\sqrt2$) makes $\mathbf{T}^{-1} = \mathbf{T}^T$ ([[§39★ Fundamental Matrices#^thm-39-7|Theorem §39.7]](b)):
>
> $$
> \mathbf{T} = \frac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}, \qquad \mathbf{T}^{-1} = \frac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} . \qquad (11)
> $$
>
> With $\mathbf{x} = \mathbf{T}\mathbf{y}$,
>
> $$
> \mathbf{y}' = \mathbf{D}\mathbf{y} + \mathbf{T}^{-1}\mathbf{g}(t) = \begin{pmatrix} -3 & 0 \\ 0 & -1 \end{pmatrix}\mathbf{y} + \frac{1}{\sqrt2}\begin{pmatrix} 2e^{-t} - 3t \\ 2e^{-t} + 3t \end{pmatrix}, \qquad (12)
> $$
>
> that is,
>
> $$
> y_1' + 3y_1 = \sqrt2\,e^{-t} - \frac{3}{\sqrt2}t, \qquad y_2' + y_2 = \sqrt2\,e^{-t} + \frac{3}{\sqrt2}t . \qquad (13)
> $$
>
> **The scalar equations.** For $y_1$, the integrating factor $e^{3t}$ gives $(e^{3t}y_1)' = \sqrt2\,e^{2t} - \frac{3}{\sqrt2}te^{3t}$. Since $\int e^{2t}\,dt = \frac12e^{2t}$ and $\int te^{3t}\,dt = \big(\frac t3 - \frac19\big)e^{3t}$,
>
> $$
> y_1 = \frac{\sqrt2}{2}e^{-t} - \frac{3}{\sqrt2}\Big(\frac t3 - \frac19\Big) + c_1e^{-3t} .
> $$
>
> For $y_2$, the integrating factor $e^t$ gives $(e^ty_2)' = \sqrt2 + \frac{3}{\sqrt2}te^t$, and $\int te^t\,dt = (t - 1)e^t$, so
>
> $$
> y_2 = \sqrt2\,te^{-t} + \frac{3}{\sqrt2}(t - 1) + c_2e^{-t} . \qquad (14)
> $$
>
> **Back to $\mathbf{x}$.** $\mathbf{x} = \mathbf{T}\mathbf{y} = \frac{1}{\sqrt2}\begin{pmatrix} y_1 + y_2 \\ -y_1 + y_2 \end{pmatrix}$. The non-exponential terms combine as $\frac{1}{\sqrt2}\cdot\frac{3}{\sqrt2}\big[\pm\big(-\frac t3 + \frac19\big) + (t - 1)\big]$, which is $t - \frac43$ (sign $+$) and $2t - \frac53$ (sign $-$). So
>
> $$
> \mathbf{x} = \begin{pmatrix} \dfrac{c_1}{\sqrt2}e^{-3t} + \Big(\dfrac{c_2}{\sqrt2} + \dfrac12\Big)e^{-t} + t - \dfrac43 + te^{-t} \\[10pt] -\dfrac{c_1}{\sqrt2}e^{-3t} + \Big(\dfrac{c_2}{\sqrt2} - \dfrac12\Big)e^{-t} + 2t - \dfrac53 + te^{-t} \end{pmatrix}
> $$
>
> $$
> = k_1\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-3t} + k_2\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{-t} + \frac12\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-t} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}te^{-t} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}t - \frac13\begin{pmatrix} 4 \\ 5 \end{pmatrix}, \qquad (15)
> $$
>
> where $k_1 = c_1/\sqrt2$ and $k_2 = c_2/\sqrt2$. The first two terms are the general solution (10) of the homogeneous system; the rest is a particular solution of (8).
>
> *BDP: Example 7.9.1*

^ex-41-1

## Undetermined Coefficients

> [!remark] Remark: Method — Undetermined Coefficients for Systems
> The method of [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^rem-21-2|§21]] (BDP 3.5) carries over to $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$. As a practical matter it applies only when $\mathbf{P} = \mathbf{A}$ is a constant matrix and the components of $\mathbf{g}$ are polynomial, exponential or sinusoidal functions, or sums or products of these.
> 1. **Split $\mathbf{g}$** into terms of the form (constant vector) $\times$ (function), e.g. $\mathbf{g}(t) = \mathbf{u}e^{\lambda t} + \mathbf{w}t$.
> 2. **Assume a solution** of the same form as in BDP 3.5 for a single equation ([[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-21-4|Theorem §21.4]]), but with *vector* coefficients $\mathbf{a}, \mathbf{b}, \ldots$ to be determined.
> 3. **The main difference:** for a term $\mathbf{u}e^{\lambda t}$ where $\lambda$ is a simple root of the characteristic equation (an eigenvalue of $\mathbf{A}$), assume $\mathbf{a}te^{\lambda t} + \mathbf{b}e^{\lambda t}$, not $\mathbf{a}te^{\lambda t}$ alone.
> 4. **Substitute** and equate the coefficients of each function ($te^{\lambda t}$, $e^{\lambda t}$, $t$, $1$, …) to get linear algebraic equations for the vectors; solve them in a convenient order.
> 5. **Add** the general solution of the homogeneous system.

^rem-41-2

> [!example] Example §41.2: Solution by Undetermined Coefficients
> Use the method of undetermined coefficients to find a particular solution of the system (8),
>
> $$
> \mathbf{x}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{x} + \begin{pmatrix} 2e^{-t} \\ 3t \end{pmatrix} = \mathbf{A}\mathbf{x} + \mathbf{g}(t) . \qquad (16)
> $$
>
> **The trial form.** Write
>
> $$
> \mathbf{g}(t) = \begin{pmatrix} 2 \\ 0 \end{pmatrix}e^{-t} + \begin{pmatrix} 0 \\ 3 \end{pmatrix}t . \qquad (17)
> $$
>
> Since $r = -1$ is an eigenvalue of $\mathbf{A}$, both $\mathbf{a}te^{-t}$ and $\mathbf{b}e^{-t}$ must be included:
>
> $$
> \mathbf{x} = \mathbf{v}(t) = \mathbf{a}te^{-t} + \mathbf{b}e^{-t} + \mathbf{c}t + \mathbf{d} . \qquad (18)
> $$
>
> **Equations for the coefficients.** Here $\mathbf{v}' = \mathbf{a}e^{-t} - \mathbf{a}te^{-t} - \mathbf{b}e^{-t} + \mathbf{c}$, while $\mathbf{A}\mathbf{v} + \mathbf{g} = \mathbf{A}\mathbf{a}te^{-t} + \big(\mathbf{A}\mathbf{b} + (2, 0)^T\big)e^{-t} + \big(\mathbf{A}\mathbf{c} + (0, 3)^T\big)t + \mathbf{A}\mathbf{d}$. Equating the coefficients of $te^{-t}$, $e^{-t}$, $t$ and $1$:
>
> $$
> \mathbf{A}\mathbf{a} = -\mathbf{a}, \qquad \mathbf{A}\mathbf{b} = \mathbf{a} - \mathbf{b} - \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \qquad \mathbf{A}\mathbf{c} = -\begin{pmatrix} 0 \\ 3 \end{pmatrix}, \qquad \mathbf{A}\mathbf{d} = \mathbf{c} . \qquad (19)
> $$
>
> **Solving.** The first equation says $\mathbf{a}$ is an eigenvector for $r = -1$ (or zero): $\mathbf{a} = (\alpha, \alpha)^T$. The second is $(\mathbf{A} + \mathbf{I})\mathbf{b} = \mathbf{a} - (2, 0)^T$, i.e.
>
> $$
> -b_1 + b_2 = \alpha - 2, \qquad b_1 - b_2 = \alpha .
> $$
>
> Adding, $0 = 2\alpha - 2$, so it is solvable only if $\alpha = 1$; then $b_1 - b_2 = 1$, and
>
> $$
> \mathbf{b} = k\begin{pmatrix} 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \end{pmatrix} \qquad (20)
> $$
>
> for any constant $k$. The simplest choice is $k = 0$, $\mathbf{b} = (0, -1)^T$. Next, $\mathbf{A}\mathbf{c} = (0, -3)^T$: $-2c_1 + c_2 = 0$ and $c_1 - 2c_2 = -3$ give $\mathbf{c} = (1, 2)^T$. Finally $\mathbf{A}\mathbf{d} = \mathbf{c}$: $-2d_1 + d_2 = 1$ and $d_1 - 2d_2 = 2$ give $\mathbf{d} = -\frac13(4, 5)^T$. Hence
>
> $$
> \mathbf{v}(t) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}te^{-t} - \begin{pmatrix} 0 \\ 1 \end{pmatrix}e^{-t} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}t - \frac13\begin{pmatrix} 4 \\ 5 \end{pmatrix} . \qquad (21)
> $$
>
> **Comparison with [[§41★ Nonhomogeneous Linear Systems#^ex-41-1|Example §41.1]].** The $e^{-t}$ term differs from the particular solution in (15). The two differ by $\frac12(1, 1)^Te^{-t}$, a solution of the homogeneous system. Choosing $k = \frac12$ in (20) gives $\mathbf{b} = (\frac12, -\frac12)^T = \frac12(1, -1)^T$, and then the two particular solutions agree.
>
> *BDP prints this value as $\mathbf{b} = -\frac12(1, 1)^T$, which is not of the form (20); the value from (20) is $\frac12(1, -1)^T$, which matches (15).*
>
> *BDP: Example 7.9.2*

^ex-41-2

## Variation of Parameters

Now let the coefficient matrix be variable, or constant but not diagonalizable:
$$
\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t), \qquad (22)
$$
with $\mathbf{P}$ and $\mathbf{g}$ continuous on $\alpha < t < \beta$, and suppose a fundamental matrix $\mathbf{\Psi}(t)$ of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$ (23) is known. Since the general solution of (23) is $\mathbf{\Psi}(t)\mathbf{c}$ ([[§39★ Fundamental Matrices#^thm-39-1|Theorem §39.1]]), proceed as in [[§22★ Variation of Parameters#^thm-22-1|Theorem §22.1]] (BDP 3.6): replace the constant vector $\mathbf{c}$ by a vector function $\mathbf{u}(t)$.

> [!theorem] Theorem §41.3: Variation of Parameters
> Let $\mathbf{P}(t)$ and $\mathbf{g}(t)$ be continuous on $\alpha < t < \beta$, and let $\mathbf{\Psi}(t)$ be a fundamental matrix of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x}$.
>
> (a) $\mathbf{x} = \mathbf{\Psi}(t)\mathbf{u}(t)$ (24) solves (22) if and only if
>
> $$
> \mathbf{\Psi}(t)\mathbf{u}'(t) = \mathbf{g}(t), \qquad\text{i.e.}\qquad \mathbf{u}'(t) = \mathbf{\Psi}^{-1}(t)\mathbf{g}(t) . \qquad (26),\ (27)
> $$
>
> (b) The general solution of (22) is
>
> $$
> \mathbf{x} = \mathbf{\Psi}(t)\mathbf{c} + \mathbf{\Psi}(t)\int_{t_1}^t \mathbf{\Psi}^{-1}(s)\mathbf{g}(s)\,ds, \qquad (29)
> $$
>
> where $t_1$ is any point in $(\alpha, \beta)$ and $\mathbf{c}$ is an arbitrary constant vector; the first term is the general solution of the homogeneous system and the second a particular solution of (22).
>
> (c) The solution of (22) with $\mathbf{x}(t_0) = \mathbf{x}^0$ (30) is
>
> $$
> \mathbf{x} = \mathbf{\Psi}(t)\mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0 + \mathbf{\Psi}(t)\int_{t_0}^t \mathbf{\Psi}^{-1}(s)\mathbf{g}(s)\,ds, \qquad (33)
> $$
>
> and, with the fundamental matrix $\mathbf{\Phi}$ satisfying $\mathbf{\Phi}(t_0) = \mathbf{I}$,
>
> $$
> \mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0 + \mathbf{\Phi}(t)\int_{t_0}^t \mathbf{\Phi}^{-1}(s)\mathbf{g}(s)\,ds . \qquad (34)
> $$
>
> *BDP: 7.9 (text), Equations (24)–(34)*

^thm-41-3

> [!proof]+ Proof
> **(a)** By the product rule for matrix functions ([[§34 Matrices#^prop-34-4|Proposition §34.4]]), $\mathbf{x}' = \mathbf{\Psi}'\mathbf{u} + \mathbf{\Psi}\mathbf{u}'$, so (22) becomes
>
> $$
> \mathbf{\Psi}'(t)\mathbf{u}(t) + \mathbf{\Psi}(t)\mathbf{u}'(t) = \mathbf{P}(t)\mathbf{\Psi}(t)\mathbf{u}(t) + \mathbf{g}(t) . \qquad (25)
> $$
>
> Since $\mathbf{\Psi}' = \mathbf{P}\mathbf{\Psi}$ ([[§39★ Fundamental Matrices#^thm-39-1|Theorem §39.1]](c)), (25) reduces to (26). $\mathbf{\Psi}(t)$ is nonsingular on $(\alpha, \beta)$ ([[§39★ Fundamental Matrices#^def-39-1|Definition §39.1]]), so (26) is equivalent to (27).
>
> **(b)** The entries of $\mathbf{\Psi}^{-1}(t) = \operatorname{adj}\mathbf{\Psi}(t)/\det\mathbf{\Psi}(t)$ are continuous, since $\det\mathbf{\Psi}(t) \ne 0$ (BDP uses this tacitly), so $\mathbf{\Psi}^{-1}\mathbf{g}$ is continuous and, by the Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus#^thm-41-1|Calc Thm. §41.1]]) applied entry by entry, together with the fact that two antiderivatives on an interval differ by a constant ([[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|Calc Cor. §29.4]]), the solutions of (27) are exactly
>
> $$
> \mathbf{u}(t) = \int_{t_1}^t \mathbf{\Psi}^{-1}(s)\mathbf{g}(s)\,ds + \mathbf{c} . \qquad (28)
> $$
>
> Substituting into (24) gives (29), which solves (22) by (a). Its second term (the case $\mathbf{c} = \mathbf{0}$) is therefore a particular solution, and the first term $\mathbf{\Psi}(t)\mathbf{c}$ is the general solution of the homogeneous system ([[§39★ Fundamental Matrices#^thm-39-1|Theorem §39.1]](a)); by [[§41★ Nonhomogeneous Linear Systems#^thm-41-1|Theorem §41.1]], (29) is the general solution of (22).
>
> **(c)** Take $t_1 = t_0$ in (29) (31). At $t = t_0$ the integral is zero, so the initial condition becomes $\mathbf{\Psi}(t_0)\mathbf{c} = \mathbf{x}^0$, i.e. $\mathbf{c} = \mathbf{\Psi}^{-1}(t_0)\mathbf{x}^0$ (32); this gives (33), the only solution of the initial value problem by the uniqueness part of [[§33 Introduction to Systems of First-Order Linear Equations#^thm-33-3|Theorem §33.3]]. If $\mathbf{\Psi} = \mathbf{\Phi}$, then $\mathbf{\Phi}^{-1}(t_0) = \mathbf{I}$, which gives (34).

^pf-41-3

*Uses:* [[§33 Introduction to Systems of First-Order Linear Equations#^thm-33-3|§33.3]], [[§39★ Fundamental Matrices#^thm-39-1|§39.1]], [[§39★ Fundamental Matrices#^def-39-1|Def. §39.1]], [[§39★ Fundamental Matrices#^def-39-2|Def. §39.2]], [[§41★ Nonhomogeneous Linear Systems#^thm-41-1|§41.1]], [[§34 Matrices#^prop-34-4|§34.4]], [[§41 The Fundamental Theorem of Calculus#^thm-41-1|Calc Thm. §41.1]], [[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|Calc Cor. §29.4]]

> [!remark] Remark: Method — Variation of Parameters for Systems
> To find a particular solution (or the general solution) of $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$:
> 1. **Find a fundamental matrix** $\mathbf{\Psi}(t)$ of the homogeneous system.
> 2. **Solve** $\mathbf{\Psi}(t)\mathbf{u}'(t) = \mathbf{g}(t)$ for $\mathbf{u}'$, by row reduction (or Cramer's rule) rather than by computing $\mathbf{\Psi}^{-1}$.
> 3. **Integrate** each component: $\mathbf{u}(t) = \int\mathbf{u}'(t)\,dt + \mathbf{c}$.
> 4. **Multiply:** $\mathbf{x} = \mathbf{\Psi}(t)\mathbf{u}(t)$. The $\mathbf{c}$ terms give the homogeneous solution; for an initial value problem use (33) or (34), or fit $\mathbf{c}$ at the end.
>
> Unlike the first two methods, this needs neither a constant nor a diagonalizable coefficient matrix.

^rem-41-3

> [!example] Example §41.3: Solution by Variation of Parameters
> Use variation of parameters to find the general solution of the system (8),
>
> $$
> \mathbf{x}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{x} + \begin{pmatrix} 2e^{-t} \\ 3t \end{pmatrix} . \qquad (35)
> $$
>
> **Fundamental matrix.** From (10),
>
> $$
> \mathbf{\Psi}(t) = \begin{pmatrix} e^{-3t} & e^{-t} \\ -e^{-3t} & e^{-t} \end{pmatrix} . \qquad (36)
> $$
>
> **Solving $\mathbf{\Psi}\mathbf{u}' = \mathbf{g}$.**
>
> $$
> \begin{pmatrix} e^{-3t} & e^{-t} \\ -e^{-3t} & e^{-t} \end{pmatrix}\begin{pmatrix} u_1' \\ u_2' \end{pmatrix} = \begin{pmatrix} 2e^{-t} \\ 3t \end{pmatrix} . \qquad (37)
> $$
>
> Adding the two equations, $2e^{-t}u_2' = 2e^{-t} + 3t$; subtracting the second from the first, $2e^{-3t}u_1' = 2e^{-t} - 3t$. So
>
> $$
> u_1' = e^{2t} - \frac32te^{3t}, \qquad u_2' = 1 + \frac32te^t .
> $$
>
> **Integrating**, with $\int te^{3t}\,dt = \big(\frac t3 - \frac19\big)e^{3t}$ and $\int te^t\,dt = (t - 1)e^t$:
>
> $$
> u_1(t) = \frac12e^{2t} - \frac12te^{3t} + \frac16e^{3t} + c_1, \qquad u_2(t) = t + \frac32te^t - \frac32e^t + c_2 .
> $$
>
> **Multiplying.** The first component of $\mathbf{\Psi}\mathbf{u}$ is $e^{-3t}u_1 + e^{-t}u_2 = c_1e^{-3t} + c_2e^{-t} + \frac12e^{-t} + te^{-t} + t - \frac43$, and the second is $-e^{-3t}u_1 + e^{-t}u_2 = -c_1e^{-3t} + c_2e^{-t} - \frac12e^{-t} + te^{-t} + 2t - \frac53$. That is,
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-3t} + c_2\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{-t} + \frac12\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-t} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}te^{-t} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}t - \frac13\begin{pmatrix} 4 \\ 5 \end{pmatrix}, \qquad (38)
> $$
>
> the same as (15) of [[§41★ Nonhomogeneous Linear Systems#^ex-41-1|Example §41.1]], and equivalent to (21) of [[§41★ Nonhomogeneous Linear Systems#^ex-41-2|Example §41.2]].
>
> *BDP: Example 7.9.3*

^ex-41-3

For a constant coefficient matrix, (34) simplifies, because $\mathbf{\Phi}(t)\mathbf{\Phi}^{-1}(s)$ depends only on $t - s$.

> [!theorem] Corollary §41.4: Variation of Parameters with Constant A
> Let $\mathbf{A}$ be a constant $n \times n$ matrix, $\mathbf{g}$ continuous on an interval containing $0$, and $\mathbf{\Phi}$ the fundamental matrix of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with $\mathbf{\Phi}(0) = \mathbf{I}$. The solution of $\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{g}(t)$, $\mathbf{x}(0) = \mathbf{x}^0$ is
>
> $$
> \mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0 + \int_0^t \mathbf{\Phi}(t - s)\mathbf{g}(s)\,ds = e^{\mathbf{A}t}\mathbf{x}^0 + \int_0^t e^{\mathbf{A}(t - s)}\mathbf{g}(s)\,ds .
> $$
>
> *BDP: Problem 7.9.16*

^cor-41-4

> [!proof]+ Proof
> The constant matrix $\mathbf{A}$ is continuous everywhere, so [[§41★ Nonhomogeneous Linear Systems#^thm-41-3|Theorem §41.3]](c) with $t_0 = 0$ gives, by (34),
>
> $$
> \mathbf{x} = \mathbf{\Phi}(t)\mathbf{x}^0 + \mathbf{\Phi}(t)\int_0^t \mathbf{\Phi}^{-1}(s)\mathbf{g}(s)\,ds .
> $$
>
> The matrix $\mathbf{\Phi}(t)$ does not depend on the integration variable $s$, so it can be taken inside the integral: each entry of $\mathbf{\Phi}(t)\int_0^t \mathbf{\Phi}^{-1}(s)\mathbf{g}(s)\,ds$ is a linear combination, with coefficients independent of $s$, of integrals, and the integral is linear. By [[§39★ Fundamental Matrices#^thm-39-4|Theorem §39.4]], $\mathbf{\Phi}(t) = e^{\mathbf{A}t}$, so [[§39★ Fundamental Matrices#^prop-39-6|Proposition §39.6]](c) applies: $\mathbf{\Phi}(t)\mathbf{\Phi}^{-1}(s) = \mathbf{\Phi}(t - s)$. Hence the integral term is $\int_0^t \mathbf{\Phi}(t - s)\mathbf{g}(s)\,ds$, which is the first form; writing $\mathbf{\Phi}(t) = e^{\mathbf{A}t}$ and $\mathbf{\Phi}(t - s) = e^{\mathbf{A}(t - s)}$ gives the second.

^pf-41-4

*Uses:* [[§41★ Nonhomogeneous Linear Systems#^thm-41-3|§41.3]], [[§39★ Fundamental Matrices#^prop-39-6|§39.6]], [[§39★ Fundamental Matrices#^thm-39-4|§39.4]]

The integral is a convolution of $e^{\mathbf{A}t}$ with $\mathbf{g}$, the system form of the convolution formula for a single equation in [[§31★ The Convolution Integral#^thm-31-3|Theorem §31.3]] (BDP 6.6). The analogy with $x' = ax + g(t)$, whose solution is $x = e^{at}x_0 + \int_0^t e^{a(t-s)}g(s)\,ds$, is complete.

## Laplace Transforms

The Laplace transform solves systems in very much the same way as single equations of arbitrary order (BDP Ch. 6). Since the transform is an integral, the transform of a vector is computed component by component: $\mathcal{L}\{\mathbf{x}(t)\} = \mathbf{X}(s)$ is the vector of the transforms of the components of $\mathbf{x}(t)$.

> [!theorem] Proposition §41.5: Transform of the Derivative of a Vector Function
> If each component of $\mathbf{x}(t)$ satisfies the hypotheses of Theorem 6.2.1 ([[§27 Solution of Initial Value Problems#^thm-27-1|Theorem §27.1]]), then
>
> $$
> \mathcal{L}\{\mathbf{x}'(t)\} = s\mathbf{X}(s) - \mathbf{x}(0) . \qquad (39)
> $$
>
> *BDP: 7.9 (text), Equation (39)*

^prop-41-5

> [!proof]+ Proof
> Component $i$ of $\mathcal{L}\{\mathbf{x}'(t)\}$ is $\mathcal{L}\{x_i'(t)\} = sX_i(s) - x_i(0)$ by [[§27 Solution of Initial Value Problems#^thm-27-1|Theorem §27.1]]; these are the components of $s\mathbf{X}(s) - \mathbf{x}(0)$.

^pf-41-5

*Uses:* [[§27 Solution of Initial Value Problems#^thm-27-1|§27.1]]

> [!definition] Definition §41.1: Transfer Matrix
> For the system $\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{g}(t)$ with $\mathbf{x}(0) = \mathbf{0}$, transforming gives $(s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{G}(s)$, so
>
> $$
> \mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{G}(s) . \qquad (44)
> $$
>
> The matrix $(s\mathbf{I} - \mathbf{A})^{-1}$ is called the **transfer matrix**, because multiplying it by the transform of the input vector $\mathbf{g}(t)$ yields the transform of the output vector $\mathbf{x}(t)$.
>
> *BDP: 7.9 (text)*

^def-41-1

> [!remark] Remark: Method — Laplace Transforms for Systems
> To solve $\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{g}(t)$, $\mathbf{x}(0) = \mathbf{x}^0$:
> 1. **Transform** each term, using [[§41★ Nonhomogeneous Linear Systems#^prop-41-5|Proposition §41.5]]: $s\mathbf{X}(s) - \mathbf{x}^0 = \mathbf{A}\mathbf{X}(s) + \mathbf{G}(s)$.
> 2. **Solve the algebraic system:** $\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\big(\mathbf{x}^0 + \mathbf{G}(s)\big)$. For a $2 \times 2$ matrix, $(s\mathbf{I} - \mathbf{A})^{-1}$ is $1/\det(s\mathbf{I} - \mathbf{A})$ times the matrix with the diagonal entries swapped and the off-diagonal entries negated.
> 3. **Expand** each component of $\mathbf{X}(s)$ in partial fractions.
> 4. **Invert** term by term with Table 6.2.1 ([[§27 Solution of Initial Value Problems#^thm-27-6|Theorem §27.6]]).
>
> The method is particularly useful when the forcing involves discontinuous or impulsive terms ([[§29 Differential Equations with Discontinuous Forcing Functions|§29]], [[§30 Impulse Functions|§30]]), and it gives the solution of the initial value problem directly.

^rem-41-4

> [!example] Example §41.4: Solution by Laplace Transforms
> Use the Laplace transform to solve the system (8),
>
> $$
> \mathbf{x}' = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\mathbf{x} + \begin{pmatrix} 2e^{-t} \\ 3t \end{pmatrix} = \mathbf{A}\mathbf{x} + \mathbf{g}(t), \qquad (40)
> $$
>
> with the initial condition $\mathbf{x}(0) = \mathbf{0}$.
>
> **Transforming.** $s\mathbf{X}(s) - \mathbf{x}(0) = \mathbf{A}\mathbf{X}(s) + \mathbf{G}(s)$ (41), where
>
> $$
> \mathbf{G}(s) = \begin{pmatrix} 2/(s + 1) \\ 3/s^2 \end{pmatrix} . \qquad (42)
> $$
>
> With $\mathbf{x}(0) = \mathbf{0}$, $(s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{G}(s)$ (43). Here
>
> $$
> s\mathbf{I} - \mathbf{A} = \begin{pmatrix} s + 2 & -1 \\ -1 & s + 2 \end{pmatrix}, \qquad \det(s\mathbf{I} - \mathbf{A}) = (s + 2)^2 - 1 = (s + 1)(s + 3), \qquad (45)
> $$
>
> so the transfer matrix ([[§41★ Nonhomogeneous Linear Systems#^def-41-1|Definition §41.1]]) is
>
> $$
> (s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(s + 1)(s + 3)}\begin{pmatrix} s + 2 & 1 \\ 1 & s + 2 \end{pmatrix} . \qquad (46)
> $$
>
> **The transform of the solution.**
>
> $$
> \mathbf{X}(s) = \begin{pmatrix} \dfrac{2(s + 2)}{(s + 1)^2(s + 3)} + \dfrac{3}{s^2(s + 1)(s + 3)} \\[12pt] \dfrac{2}{(s + 1)^2(s + 3)} + \dfrac{3(s + 2)}{s^2(s + 1)(s + 3)} \end{pmatrix} . \qquad (47)
> $$
>
> **Partial fractions.**
>
> $$
> \frac{2(s + 2)}{(s + 1)^2(s + 3)} = \frac{1}{(s + 1)^2} + \frac{1/2}{s + 1} - \frac{1/2}{s + 3}, \qquad \frac{3}{s^2(s + 1)(s + 3)} = \frac{1}{s^2} - \frac{4/3}{s} + \frac{3/2}{s + 1} - \frac{1/6}{s + 3},
> $$
>
> $$
> \frac{2}{(s + 1)^2(s + 3)} = \frac{1}{(s + 1)^2} - \frac{1/2}{s + 1} + \frac{1/2}{s + 3}, \qquad \frac{3(s + 2)}{s^2(s + 1)(s + 3)} = \frac{2}{s^2} - \frac{5/3}{s} + \frac{3/2}{s + 1} + \frac{1/6}{s + 3} .
> $$
>
> (For instance, in the second, the cover-up rule gives the coefficients $1$ of $1/s^2$, $\frac32$ of $1/(s + 1)$ and $-\frac16$ of $1/(s + 3)$. Since $s$ times the fraction tends to $0$ as $s \to \infty$, the coefficients of $1/s$, $1/(s + 1)$ and $1/(s + 3)$ add up to $0$, which gives $-\frac32 + \frac16 = -\frac43$ for $1/s$. See [[§54 Integration of Rational Functions by Partial Fractions#^thm-54-3|Calc Thm. §54.3]] for the form of the decomposition.) Adding,
>
> $$
> X_1(s) = \frac{1}{s^2} - \frac{4/3}{s} + \frac{2}{s + 1} + \frac{1}{(s + 1)^2} - \frac{2/3}{s + 3}, \qquad X_2(s) = \frac{2}{s^2} - \frac{5/3}{s} + \frac{1}{s + 1} + \frac{1}{(s + 1)^2} + \frac{2/3}{s + 3} .
> $$
>
> **Inverting** with $\mathcal{L}\{t\} = 1/s^2$, $\mathcal{L}\{1\} = 1/s$, $\mathcal{L}\{e^{at}\} = 1/(s - a)$ and $\mathcal{L}\{te^{at}\} = 1/(s - a)^2$ (Table 6.2.1, [[§27 Solution of Initial Value Problems#^thm-27-6|Theorem §27.6]]):
>
> $$
> \mathbf{x}(t) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}e^{-t} - \frac23\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-3t} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}te^{-t} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}t - \frac13\begin{pmatrix} 4 \\ 5 \end{pmatrix} . \qquad (48)
> $$
>
> Check: at $t = 0$, $\mathbf{x}(0) = (2 - \frac23 - \frac43,\ 1 + \frac23 - \frac53)^T = \mathbf{0}$. This is the particular solution with $\mathbf{x}(0) = \mathbf{0}$, so it differs slightly from those of [[§41★ Nonhomogeneous Linear Systems#^ex-41-1|Examples §41.1]]–[[§41★ Nonhomogeneous Linear Systems#^ex-41-3|§41.3]]: it is (15) with $k_1 = -\frac23$ and $k_2 = \frac32$, since $\frac12(1, -1)^T + \frac32(1, 1)^T = (2, 1)^T$. The general solution is (48) plus the general solution (10) of the homogeneous system.
>
> *BDP: Example 7.9.4*

^ex-41-4

> [!remark] Remark: Choosing a Method
> - **Undetermined coefficients** needs no integration, but it is limited in scope (constant $\mathbf{A}$, special $\mathbf{g}$) and may require solving several sets of algebraic equations.
> - **Diagonalization** needs the inverse of the transformation matrix, the solution of $n$ uncoupled first-order equations, and a matrix multiplication. Its advantage is that for Hermitian coefficient matrices $\mathbf{T}^{-1} = \mathbf{T}^{\ast}$ is written down without calculation, which matters more for large systems.
> - **Laplace transforms** need a matrix inversion (the transfer matrix), a multiplication, and the inverse transform of each term. They are particularly useful for discontinuous or impulsive forcing.
> - **Variation of parameters** is the most general method (variable $\mathbf{P}(t)$, any continuous $\mathbf{g}$), but it involves linear algebraic equations with variable coefficients, an integration and a matrix multiplication, so it can be the most laborious.
>
> For small constant-coefficient systems like the one in [[§41★ Nonhomogeneous Linear Systems#^ex-41-1|Examples §41.1]]–[[§41★ Nonhomogeneous Linear Systems#^ex-41-4|§41.4]], all four work well and there may be little reason to prefer one.

^rem-41-5
