---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 31
bdp: "7.5"
aliases: ["BDP 7.5"]
tags: [ordinary-differential-equations, math331]
---
← [[§30 Basic Theory of Systems of First-Order Linear Equations]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§32 Complex-Valued Eigenvalues]] →

*Boyce–DiPrima, Section 7.5 · MATH 331 Written HW 6, Final Exam (Fall 2021), Final Exam (Fall 2022, alternate).*

For a system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with a constant matrix $\mathbf{A}$, the natural guess $\mathbf{x} = \boldsymbol{\xi}e^{rt}$ works exactly when $r$ is an eigenvalue of $\mathbf{A}$ and $\boldsymbol{\xi}$ an eigenvector, so solving the differential equation becomes the algebra of [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors|§29]]. When the eigenvalues are real and distinct, or $\mathbf{A}$ is symmetric, this gives a fundamental set and the general solution. For $2 \times 2$ systems the solutions are drawn as trajectories in the phase plane, and the signs of the two real eigenvalues decide the picture: a saddle point when they are opposite, a node when they agree. The same material appears in [[§38 Applications to Differential Equations|235 §38]] from the linear-algebra side; this section is the fuller treatment and the basis of the classification completed in [[§32 Complex-Valued Eigenvalues|§32]].

## Equilibrium Solutions and the Phase Plane

For $n = 1$ the system is $x' = ax$, with solutions $x = ce^{at}$. If $a \ne 0$, the only constant solution is $x = 0$. If $a < 0$, every solution approaches $0$ as $t$ increases; if $a > 0$, every solution other than $x = 0$ moves away from it.

> [!definition] Definition §31.1: Equilibrium Solution; Asymptotically Stable, Unstable
> An **equilibrium solution** of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ is a constant solution; the equilibrium solutions are the solutions of $\mathbf{A}\mathbf{x} = \mathbf{0}$. Unless stated otherwise we assume $\det\mathbf{A} \ne 0$, so that $\mathbf{x} = \mathbf{0}$ is the only one ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-1|Theorem §29.1]]). The equilibrium $\mathbf{x} = \mathbf{0}$ is **asymptotically stable** if all other solutions approach it as $t$ increases, and **unstable** if (almost all) other solutions depart from it as $t$ increases.
>
> *BDP: 7.5 (text)*

^def-31-1

> [!definition] Definition §31.2: Phase Plane, Direction Field, Trajectory, Phase Portrait
> For $n = 2$, solutions $\mathbf{x}(t) = (x_1(t), x_2(t))^T$ are visualized in the $x_1x_2$-plane, the **phase plane**. Plotting the vector $\mathbf{A}\mathbf{x}$ at many points $\mathbf{x}$ gives a **direction field** of tangent vectors to solutions. The curve traced by a solution is a **trajectory** (or solution curve), and a plot of a representative sample of trajectories is a **phase portrait**.
>
> *BDP: 7.5 (text)*

^def-31-2

## Exponential Solutions

When $\mathbf{A}$ is diagonal the equations decouple. For instance $\mathbf{x}' = \begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix}\mathbf{x}$ is $x_1' = 2x_1$, $x_2' = -3x_2$, so $x_1 = c_1e^{2t}$, $x_2 = c_2e^{-3t}$, and

$$
\mathbf{x} = c_1\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{2t} + c_2\begin{pmatrix} 0 \\ 1 \end{pmatrix}e^{-3t} .
$$

The Wronskian of the two solutions is $e^{2t}e^{-3t} = e^{-t} \ne 0$, so they form a fundamental set ([[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Definition §30.3]]) and this is the general solution (BDP's Example 1). Each solution is an exponential times a constant vector, which suggests trying the same form for any $\mathbf{A}$.

> [!theorem] Theorem §31.1: Exponential Solutions
> Let $\mathbf{A}$ be a constant $n \times n$ matrix, $r$ a number and $\boldsymbol{\xi} \ne \mathbf{0}$ a constant vector. Then
>
> $$
> \mathbf{x} = \boldsymbol{\xi}e^{rt} \qquad (7)
> $$
>
> is a solution of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ if and only if
>
> $$
> (\mathbf{A} - r\mathbf{I})\boldsymbol{\xi} = \mathbf{0}, \qquad (8)
> $$
>
> that is, if and only if $r$ is an eigenvalue of $\mathbf{A}$ and $\boldsymbol{\xi}$ a corresponding eigenvector.
>
> *BDP: 7.5 (text), Equations (7)–(8)*

^thm-31-1

> [!proof]+ Proof
> Since $\boldsymbol{\xi}$ is constant, $\mathbf{x}' = r\boldsymbol{\xi}e^{rt}$, while $\mathbf{A}\mathbf{x} = \mathbf{A}\boldsymbol{\xi}e^{rt}$. So $\mathbf{x}' = \mathbf{A}\mathbf{x}$ means $r\boldsymbol{\xi}e^{rt} = \mathbf{A}\boldsymbol{\xi}e^{rt}$ for all $t$. Canceling the nonzero scalar factor $e^{rt}$, this holds if and only if $\mathbf{A}\boldsymbol{\xi} = r\boldsymbol{\xi}$, which is (8). Since $\boldsymbol{\xi} \ne \mathbf{0}$, this says $r$ is an eigenvalue with eigenvector $\boldsymbol{\xi}$ ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|Definition §29.4]]). The argument works equally for complex $r$ and $\boldsymbol{\xi}$, using $\frac{d}{dt}e^{rt} = re^{rt}$ for complex $r$ ([[§15 Complex Roots of the Characteristic Equation#^prop-15-1|Proposition §15.1]]).

^pf-31-1

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|Def. §29.4]]

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^thm-38-2|235 Thm. §38.2]] (Lay's "eigenfunctions" $\mathbf{v}e^{\lambda t}$, the same statement and proof).

## Real Eigenvalues of Opposite Signs: Saddle Points

> [!example] Example §31.1: A Saddle Point
> Find the general solution of
>
> $$
> \mathbf{x}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{x} \qquad (9)
> $$
>
> and describe its phase portrait.
>
> **Direction field.** At each point the arrow points along $\mathbf{A}\mathbf{x}$; for example $(1, 4)^T$ at $(1, 0)$ and $(-2, -5)^T$ at $(-1, -1)$. A typical solution in the second or fourth quadrant eventually moves into the first or third quadrant, no solution leaves the first or third quadrant, and far from the origin the trajectories have slope about $2$.
>
> **Eigenvalues.** Substituting $\mathbf{x} = \boldsymbol{\xi}e^{rt}$ gives $\begin{pmatrix} 1 - r & 1 \\ 4 & 1 - r \end{pmatrix}\begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = \mathbf{0}$, which has nonzero solutions only if
>
> $$
> \begin{vmatrix} 1 - r & 1 \\ 4 & 1 - r \end{vmatrix} = (1 - r)^2 - 4 = r^2 - 2r - 3 = (r - 3)(r + 1) = 0 .
> $$
>
> So $r_1 = 3$ and $r_2 = -1$.
>
> **Eigenvectors.** For $r = 3$ both equations reduce to $-2\xi_1 + \xi_2 = 0$, so $\boldsymbol{\xi}^{(1)} = (1, 2)^T$. For $r = -1$ they reduce to $2\xi_1 + \xi_2 = 0$, so $\boldsymbol{\xi}^{(2)} = (1, -2)^T$.
>
> **General solution.** The solutions $\mathbf{x}^{(1)}(t) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t}$ and $\mathbf{x}^{(2)}(t) = \begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t}$ have Wronskian
>
> $$
> W[\mathbf{x}^{(1)}, \mathbf{x}^{(2)}](t) = \begin{vmatrix} e^{3t} & e^{-t} \\ 2e^{3t} & -2e^{-t} \end{vmatrix} = -4e^{2t} \ne 0 ,
> $$
>
> so they form a fundamental set, and the general solution is
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ 2 \end{pmatrix}e^{3t} + c_2\begin{pmatrix} 1 \\ -2 \end{pmatrix}e^{-t} . \qquad (17)
> $$
>
> **Phase portrait** (figure below, panel (a)).
> - $c_2 = 0$: $x_1 = c_1e^{3t}$, $x_2 = 2c_1e^{3t}$. Eliminating $t$, the trajectory lies on the line $x_2 = 2x_1$, the line of $\boldsymbol{\xi}^{(1)}$: in the first quadrant if $c_1 > 0$, the third if $c_1 < 0$, and in both cases it moves away from the origin.
> - $c_1 = 0$: the trajectory lies on the line $x_2 = -2x_1$ of $\boldsymbol{\xi}^{(2)}$, in the fourth quadrant if $c_2 > 0$ and the second if $c_2 < 0$, and it moves toward the origin.
> - In general, for large $t$ the term $c_1\mathbf{x}^{(1)}$ dominates and $c_2\mathbf{x}^{(2)}$ becomes negligible, so every solution with $c_1 \ne 0$ is asymptotic to the line $x_2 = 2x_1$ as $t \to \infty$. Similarly every solution with $c_2 \ne 0$ is asymptotic to $x_2 = -2x_1$ as $t \to -\infty$. The trajectories come in along one eigenvector line and leave along the other.
>
> In terms of components: $x_1 = c_1e^{3t} + c_2e^{-t}$. Only when $c_1 = 0$ does $x_1 \to 0$; otherwise the positive exponential makes $|x_1|$ grow exponentially, and likewise for $x_2$.
>
> *BDP: Example 7.5.2*

^ex-31-1

> [!definition] Definition §31.3: Saddle Point
> When the eigenvalues of a $2 \times 2$ system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ are real and of opposite signs, the origin is called a **saddle point**. The pattern of Example §31.1 is typical: the two eigenvector lines are the only trajectories through the origin, one approached and one left, and all other trajectories come in along the first and depart along the second. Saddle points are always unstable, because almost all trajectories depart from them as $t$ increases.
>
> *BDP: 7.5 (text)*

^def-31-3

## Real Eigenvalues of the Same Sign: Nodes

> [!example] Example §31.2: A Node
> Find the general solution of
>
> $$
> \mathbf{x}' = \begin{pmatrix} -3 & \sqrt2 \\ \sqrt2 & -2 \end{pmatrix}\mathbf{x} \qquad (18)
> $$
>
> and describe its phase portrait. (The direction field shows that all solutions approach the origin.)
>
> **Eigenvalues.** $\mathbf{x} = \boldsymbol{\xi}e^{rt}$ leads to $\begin{pmatrix} -3 - r & \sqrt2 \\ \sqrt2 & -2 - r \end{pmatrix}\boldsymbol{\xi} = \mathbf{0}$, and
>
> $$
> (-3 - r)(-2 - r) - 2 = r^2 + 5r + 4 = (r + 1)(r + 4) = 0 ,
> $$
>
> so $r_1 = -1$ and $r_2 = -4$.
>
> **Eigenvectors.** For $r = -1$: $\begin{pmatrix} -2 & \sqrt2 \\ \sqrt2 & -1 \end{pmatrix}\boldsymbol{\xi} = \mathbf{0}$ gives $\xi_2 = \sqrt2\,\xi_1$, so $\boldsymbol{\xi}^{(1)} = (1, \sqrt2)^T$. For $r = -4$: $\begin{pmatrix} 1 & \sqrt2 \\ \sqrt2 & 2 \end{pmatrix}\boldsymbol{\xi} = \mathbf{0}$ gives $\xi_1 = -\sqrt2\,\xi_2$, so $\boldsymbol{\xi}^{(2)} = (-\sqrt2, 1)^T$. (The matrix is symmetric, and the two eigenvectors are orthogonal, as [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|Theorem §29.5]] predicts: $-\sqrt2 + \sqrt2 = 0$.)
>
> **General solution.** The Wronskian of $\boldsymbol{\xi}^{(1)}e^{-t}$ and $\boldsymbol{\xi}^{(2)}e^{-4t}$ is $(1 \cdot 1 - \sqrt2(-\sqrt2))e^{-5t} = 3e^{-5t} \ne 0$, so
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ \sqrt2 \end{pmatrix}e^{-t} + c_2\begin{pmatrix} -\sqrt2 \\ 1 \end{pmatrix}e^{-4t} . \qquad (25)
> $$
>
> **Phase portrait** (figure below, panel (b)). The solution $\mathbf{x}^{(1)}$ approaches the origin along the line $x_2 = \sqrt2\,x_1$, and $\mathbf{x}^{(2)}$ along the line $x_1 = -\sqrt2\,x_2$. As $t \to \infty$, $e^{-4t}$ is much smaller than $e^{-t}$, so $c_2\mathbf{x}^{(2)}$ is negligible compared with $c_1\mathbf{x}^{(1)}$: unless $c_1 = 0$, every solution approaches the origin *tangent to the line* $x_2 = \sqrt2\,x_1$ of the slower eigenvalue. Far from the origin (as $t \to -\infty$) the faster term dominates and trajectories are nearly parallel to $\boldsymbol{\xi}^{(2)}$. Each component $x_1(t)$, $x_2(t)$ tends to $0$.
>
> *BDP: Example 7.5.3*

^ex-31-2

> [!definition] Definition §31.4: Node
> When the eigenvalues of a $2 \times 2$ system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ are real, different, and of the same sign, the origin is called a **node**. If the eigenvalues are negative, all trajectories approach the origin (tangent to the eigenvector of the eigenvalue nearer to $0$, except the two on the other eigenvector line), and the node is asymptotically stable. If they are positive, the picture is the same with the direction of motion reversed: trajectories leave the origin, and the node is unstable.
>
> *BDP: 7.5 (text)*

^def-31-4

![[m331-31-1.svg]]
*Phase portraits computed from the general solutions (17) and (25). (a) Saddle point of Example §31.1: the trajectory $\mathbf{x}^{(1)}$ (red) leaves the origin along $x_2 = 2x_1$, $\mathbf{x}^{(2)}$ (green) enters it along $x_2 = -2x_1$, and every other trajectory comes in along the green line and leaves along the red one. (b) Asymptotically stable node of Example §31.2: every trajectory enters the origin; except for the green line of the fast eigenvalue $-4$, they arrive tangent to the red line of the slow eigenvalue $-1$.*

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^def-38-2|235 Def. §38.2]], where Lay calls the stable node an *attractor* or *sink* and the unstable one a *repeller* or *source*, and names the eigenvector lines the directions of greatest attraction and repulsion.
> - The discrete analogue $\mathbf{x}_{k+1} = A\mathbf{x}_k$, where the dividing line is $|\lambda| = 1$ instead of $\lambda = 0$: [[§37 Discrete Dynamical Systems#^def-37-1|235 Def. §37.1]], [[§37 Discrete Dynamical Systems#^prop-37-3|235 Prop. §37.3]].

Examples §31.1 and §31.2 cover the two main cases of a $2 \times 2$ system with real, different eigenvalues. The remaining possibility, a zero eigenvalue, means $\det\mathbf{A} = 0$, which was excluded; then a whole line of equilibrium solutions appears (BDP's Problems 5 and 6).

## The General n × n System

For $\mathbf{x}' = \mathbf{A}\mathbf{x}$ with $\mathbf{A}$ real and $n \times n$, the eigenvalues $r_1, \ldots, r_n$ are the roots of $\det(\mathbf{A} - r\mathbf{I}) = 0$, and the nature of the general solution depends on them. There are three possibilities:
1. all eigenvalues are real and different from each other;
2. some eigenvalues occur in complex conjugate pairs;
3. some eigenvalues, real or complex, are repeated.

> [!theorem] Theorem §31.2: Fundamental Set from n Independent Eigenvectors
> Suppose the real $n \times n$ matrix $\mathbf{A}$ has $n$ linearly independent real eigenvectors $\boldsymbol{\xi}^{(1)}, \ldots, \boldsymbol{\xi}^{(n)}$ with eigenvalues $r_1, \ldots, r_n$. This is the case
> - (a) if the eigenvalues are real and all different, and
> - (b) if $\mathbf{A}$ is real and symmetric, even when some eigenvalues are repeated.
>
> Then the solutions
>
> $$
> \mathbf{x}^{(1)}(t) = \boldsymbol{\xi}^{(1)}e^{r_1t}, \quad \ldots, \quad \mathbf{x}^{(n)}(t) = \boldsymbol{\xi}^{(n)}e^{r_nt} \qquad (27)
> $$
>
> form a fundamental set of solutions on $-\infty < t < \infty$, and the general solution of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ is
>
> $$
> \mathbf{x} = c_1\boldsymbol{\xi}^{(1)}e^{r_1t} + \cdots + c_n\boldsymbol{\xi}^{(n)}e^{r_nt} . \qquad (29)
> $$
>
> *BDP: 7.5 (text), Equations (27)–(29)*

^thm-31-2

> [!proof]+ Proof
> **The hypothesis holds in cases (a) and (b).** (a) Each real eigenvalue has a real eigenvector, since $\mathbf{A} - r\mathbf{I}$ is then a real singular matrix and row reduction stays in real numbers. Distinct eigenvalues have linearly independent eigenvectors ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|Theorem §29.4]]). (b) A real symmetric matrix is Hermitian, so all its eigenvalues are real and it has a full set of $n$ linearly independent eigenvectors ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|Theorem §29.5]], parts 1 and 2), which may be taken real by the same remark.
>
> **The conclusion.** Each $\mathbf{x}^{(i)}$ is a solution by Theorem §31.1. Factoring $e^{r_jt}$ out of the $j$th column of the Wronskian,
>
> $$
> W[\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(n)}](t) = \begin{vmatrix} \xi_1^{(1)}e^{r_1t} & \cdots & \xi_1^{(n)}e^{r_nt} \\ \vdots & & \vdots \\ \xi_n^{(1)}e^{r_1t} & \cdots & \xi_n^{(n)}e^{r_nt} \end{vmatrix} = e^{(r_1 + \cdots + r_n)t}\begin{vmatrix} \xi_1^{(1)} & \cdots & \xi_1^{(n)} \\ \vdots & & \vdots \\ \xi_n^{(1)} & \cdots & \xi_n^{(n)} \end{vmatrix} . \qquad (28)
> $$
>
> The exponential is never zero, and the last determinant is nonzero because the eigenvectors are linearly independent ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|Theorem §29.2]]). So the Wronskian never vanishes, the solutions form a fundamental set ([[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Definition §30.3]]), and (29) is the general solution ([[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|Theorem §30.2]]).

^pf-31-2

*Uses:* [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|§31.1]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|§29.2]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|§29.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|§29.5]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-2|Def. §30.2]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Def. §30.3]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|§30.2]]

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^thm-38-3|235 Thm. §38.3]], the same general solution for diagonalizable $A$ obtained by decoupling: $\mathbf{x} = P\mathbf{y}$ with the eigenvectors as columns of $P$ turns the system into $y_k' = r_ky_k$. Having $n$ independent eigenvectors is exactly diagonalizability, [[§34 Diagonalization#^thm-34-1|235 Thm. §34.1]].

> [!remark] Remark: Method — Eigenvector Solutions of x′ = Ax
> 1. **Eigenvalues.** Solve the characteristic equation $\det(\mathbf{A} - r\mathbf{I}) = 0$. For $2 \times 2$ matrices, $\det(\mathbf{A} - r\mathbf{I}) = r^2 - (\operatorname{tr}\mathbf{A})\,r + \det\mathbf{A}$.
> 2. **Eigenvectors.** For each eigenvalue, solve $(\mathbf{A} - r\mathbf{I})\boldsymbol{\xi} = \mathbf{0}$. In the $2 \times 2$ case one row suffices: the row $(a, b)$ gives $\boldsymbol{\xi} = (b, -a)^T$ (if not both zero).
> 3. **General solution.** If there are $n$ independent eigenvectors (Theorem §31.2), $\mathbf{x} = c_1\boldsymbol{\xi}^{(1)}e^{r_1t} + \cdots + c_n\boldsymbol{\xi}^{(n)}e^{r_nt}$. Otherwise see [[§32 Complex-Valued Eigenvalues|§32]] (complex eigenvalues) or [[§34★ Repeated Eigenvalues|§34★]] (too few eigenvectors).
> 4. **Initial value problem.** Setting $t = 0$ gives the linear system $c_1\boldsymbol{\xi}^{(1)} + \cdots + c_n\boldsymbol{\xi}^{(n)} = \mathbf{x}(0)$ for the constants. Check the answer by substituting $t = 0$.
> 5. **Phase portrait** ($2 \times 2$, by hand). Draw the two eigenvector lines; on each, the motion is outward if its eigenvalue is positive and inward if negative. Then fill in curves using dominance: as $t \to \infty$ trajectories follow the line of the larger eigenvalue, and as $t \to -\infty$ the line of the smaller one. Opposite signs give a saddle, equal signs a node.

^rem-31-1

> [!example] Example §31.3: A 3 × 3 Symmetric System with a Double Eigenvalue
> Find the general solution of
>
> $$
> \mathbf{x}' = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}\mathbf{x} . \qquad (30)
> $$
>
> The matrix is real and symmetric; its eigenvalues and eigenvectors were found in [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^ex-29-4|Example §29.4]]:
>
> $$
> r_1 = 2,\ \boldsymbol{\xi}^{(1)} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}; \qquad r_2 = r_3 = -1,\ \boldsymbol{\xi}^{(2)} = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix},\ \boldsymbol{\xi}^{(3)} = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} .
> $$
>
> The three eigenvectors are independent (the determinant of the matrix with these columns is $3$), so by Theorem §31.2(b) the general solution is
>
> $$
> \mathbf{x} = c_1\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}e^{2t} + c_2\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}e^{-t} + c_3\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}e^{-t} . \qquad (34)
> $$
>
> Even though $r = -1$ has algebraic multiplicity $2$, it has two independent eigenvectors, which is all that is needed. (Check with Abel's formula: $\operatorname{tr}\mathbf{A} = 0$, so the Wronskian is constant, $e^{(2 - 1 - 1)t} \cdot 3 = 3$.)
>
> **Behavior.** If $c_1 \ne 0$, the term with $e^{2t}$ dominates and all components of $\mathbf{x}$ become unbounded as $t \to \infty$. If $c_1 = 0$, only the decaying terms remain and $\mathbf{x} \to \mathbf{0}$. Since $\boldsymbol{\xi}^{(1)}$ is orthogonal to $\boldsymbol{\xi}^{(2)}$ and $\boldsymbol{\xi}^{(3)}$, $c_1 = (\mathbf{x}(0), \boldsymbol{\xi}^{(1)})/3$, so the initial points with $c_1 = 0$ are exactly those in the plane $x_1 + x_2 + x_3 = 0$ spanned by $\boldsymbol{\xi}^{(2)}$ and $\boldsymbol{\xi}^{(3)}$. Solutions that start in this plane approach the origin; all others become unbounded.
>
> *BDP: Example 7.5.4*

^ex-31-3

> [!remark] Remark: The Remaining Cases
> - **Complex eigenvalues** (possibility 2). If all eigenvalues are different there are still $n$ independent solutions of the form (27), but some are complex-valued. As in Chapter 3, real solutions can be extracted from them; this is [[§32 Complex-Valued Eigenvalues|§32]].
> - **Repeated eigenvalues** (possibility 3). An eigenvalue of algebraic multiplicity $m$ may have fewer than $m$ independent eigenvectors ($q < m$, [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-3|Theorem §29.3]]). Then there are fewer than $n$ solutions of the form $\boldsymbol{\xi}e^{rt}$, and solutions of another form are needed, much as a repeated root of the characteristic equation of an $n$th-order equation gives $e^{rt}, te^{rt}, \ldots$ ([[§16 Repeated Roots; Reduction of Order#^thm-16-1|Theorem §16.1]]). This is [[§34★ Repeated Eigenvalues|§34★]].
> - **Complex matrices.** If $\mathbf{A}$ itself is complex, the eigenvalues need not come in conjugate pairs and the eigenvectors are usually complex; (29) still holds when there are $n$ independent eigenvectors, but the solutions are complex-valued.

^rem-31-2

## Initial Value Problems and Classification

> [!example] Example §31.4: Two Initial Value Problems
> **(a)** Solve $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$ with $\mathbf{A} = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}$ and $\mathbf{Y}(0) = \begin{pmatrix} -9 \\ 7 \end{pmatrix}$.
>
> **Eigenvalues.** $\det(\mathbf{A} - \lambda\mathbf{I}) = (1 - \lambda)^2 - 9 = \lambda^2 - 2\lambda - 8 = (\lambda - 4)(\lambda + 2)$, so $\lambda_1 = 4$, $\lambda_2 = -2$.
>
> **Eigenvectors.** For $\lambda = 4$, the first row of $\mathbf{A}\mathbf{v} = 4\mathbf{v}$ reads $a + 3b = 4a$, so $a = b$ and $\mathbf{v}_1 = (1, 1)^T$. For $\lambda = -2$, $a + 3b = -2a$ gives $b = -a$, so $\mathbf{v}_2 = (1, -1)^T$.
>
> **General solution and initial condition.**
>
> $$
> \mathbf{Y}(t) = c_1e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2e^{-2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad \mathbf{Y}(0) = \begin{pmatrix} c_1 + c_2 \\ c_1 - c_2 \end{pmatrix} = \begin{pmatrix} -9 \\ 7 \end{pmatrix} .
> $$
>
> Adding and subtracting, $c_1 = -1$ and $c_2 = -8$:
>
> $$
> \mathbf{Y}(t) = -e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} - 8e^{-2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} -e^{4t} - 8e^{-2t} \\ -e^{4t} + 8e^{-2t} \end{pmatrix} .
> $$
>
> Check: $\mathbf{Y}(0) = (-1 - 8, -1 + 8)^T = (-9, 7)^T$. The eigenvalues have opposite signs, so the origin is a saddle point; this solution starts near the incoming line of $\mathbf{v}_2$ and leaves along the direction $-\mathbf{v}_1 = (-1, -1)^T$.
>
> **(b)** Solve $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$ with $\mathbf{A} = \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix}$ and $\mathbf{Y}(0) = \begin{pmatrix} 9 \\ 5 \end{pmatrix}$.
>
> $\det(\mathbf{A} - \lambda\mathbf{I}) = (4 - \lambda)^2 - 1 = \lambda^2 - 8\lambda + 15 = (\lambda - 5)(\lambda - 3)$. For $\lambda = 5$, $4a + b = 5a$ gives $\mathbf{v}_1 = (1, 1)^T$; for $\lambda = 3$, $4a + b = 3a$ gives $\mathbf{v}_2 = (1, -1)^T$. Then $\mathbf{Y}(0) = (c_1 + c_2, c_1 - c_2)^T = (9, 5)^T$ gives $c_1 = 7$, $c_2 = 2$:
>
> $$
> \mathbf{Y}(t) = 7e^{5t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + 2e^{3t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 7e^{5t} + 2e^{3t} \\ 7e^{5t} - 2e^{3t} \end{pmatrix} .
> $$
>
> Both eigenvalues are positive: the origin is an unstable node (a source), and the solution grows without bound in the direction of $\mathbf{v}_1$.
>
> In both parts $\mathbf{A}$ is symmetric, so the eigenvectors are orthogonal ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-5|Theorem §29.5]]) and the constants can be read off without solving a system: $c_i = (\mathbf{Y}(0), \mathbf{v}_i)/(\mathbf{v}_i, \mathbf{v}_i)$, for instance $c_1 = (9 + 5)/2 = 7$ in (b).
>
> *Source: 331 Final (Fall 2021), Q6; 331 Final (Fall 2022, alternate), Q5*

^ex-31-4

> [!example] Example §31.5: Classifying Real-Eigenvalue Systems
> For each matrix, find the eigenvalues and eigenvectors, the type of the origin for $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$, and the general solution.
>
> **(a)** $\mathbf{A} = \begin{pmatrix} -9 & 8 \\ -3 & 1 \end{pmatrix}$. $(-9 - \lambda)(1 - \lambda) + 24 = \lambda^2 + 8\lambda + 15 = (\lambda + 3)(\lambda + 5)$, so $\lambda_1 = -3$, $\lambda_2 = -5$. For $\lambda = -3$, the second row of $\mathbf{A} + 3\mathbf{I} = \begin{pmatrix} -6 & 8 \\ -3 & 4 \end{pmatrix}$ gives $3a = 4b$, $\mathbf{v}_1 = (4, 3)^T$. For $\lambda = -5$, $\mathbf{A} + 5\mathbf{I} = \begin{pmatrix} -4 & 8 \\ -3 & 6 \end{pmatrix}$ gives $a = 2b$, $\mathbf{v}_2 = (2, 1)^T$. Both eigenvalues are negative: an asymptotically stable **node** (a **sink**). Trajectories enter the origin tangent to the line of $\mathbf{v}_1$, the slower eigenvalue $-3$.
>
> $$
> \mathbf{Y}(t) = c_1e^{-3t}\begin{pmatrix} 4 \\ 3 \end{pmatrix} + c_2e^{-5t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} .
> $$
>
> **(b)** $\mathbf{A} = \begin{pmatrix} 2 & 2 \\ -1 & 5 \end{pmatrix}$. $(2 - \lambda)(5 - \lambda) + 2 = \lambda^2 - 7\lambda + 12 = (\lambda - 3)(\lambda - 4)$. For $\lambda = 3$, $\mathbf{A} - 3\mathbf{I} = \begin{pmatrix} -1 & 2 \\ -1 & 2 \end{pmatrix}$ gives $\mathbf{v}_1 = (2, 1)^T$; for $\lambda = 4$, $\mathbf{A} - 4\mathbf{I} = \begin{pmatrix} -2 & 2 \\ -1 & 1 \end{pmatrix}$ gives $\mathbf{v}_2 = (1, 1)^T$. Both positive: an unstable **node** (a **source**). Trajectories leave the origin tangent to the line of $\mathbf{v}_1$ (as $t \to -\infty$ the term $e^{3t}$ dominates) and far out become parallel to $\mathbf{v}_2$.
>
> $$
> \mathbf{Y}(t) = c_1e^{3t}\begin{pmatrix} 2 \\ 1 \end{pmatrix} + c_2e^{4t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} .
> $$
>
> **(c)** $\mathbf{A} = \begin{pmatrix} 2 & 4 \\ 3 & 1 \end{pmatrix}$. $(2 - \lambda)(1 - \lambda) - 12 = \lambda^2 - 3\lambda - 10 = (\lambda - 5)(\lambda + 2)$. For $\lambda = 5$, $\mathbf{A} - 5\mathbf{I} = \begin{pmatrix} -3 & 4 \\ 3 & -4 \end{pmatrix}$ gives $3a = 4b$, $\mathbf{v}_1 = (4, 3)^T$; for $\lambda = -2$, $\mathbf{A} + 2\mathbf{I} = \begin{pmatrix} 4 & 4 \\ 3 & 3 \end{pmatrix}$ gives $\mathbf{v}_2 = (1, -1)^T$. Opposite signs: a **saddle point**, with outgoing line along $\mathbf{v}_1$ and incoming line along $\mathbf{v}_2$.
>
> $$
> \mathbf{Y}(t) = c_1e^{5t}\begin{pmatrix} 4 \\ 3 \end{pmatrix} + c_2e^{-2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} .
> $$
>
> *Source: 331 Written HW 6, Problems 2(a), 5 and 6*

^ex-31-5
