---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 32
bdp: "7.6"
aliases: ["BDP 7.6"]
tags: [ordinary-differential-equations, math331]
---
← [[§31 Homogeneous Linear Systems with Constant Coefficients]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§33★ Fundamental Matrices]] →

*Boyce–DiPrima, Section 7.6 · MATH 331 Written HW 6, Final Exam (Fall 2021), Final Exam (Fall 2022, alternate).*

When the real matrix $\mathbf{A}$ has complex eigenvalues, they come in conjugate pairs $\lambda \pm i\mu$ with conjugate eigenvectors, and the exponential solutions $\boldsymbol{\xi}e^{rt}$ of [[§31 Homogeneous Linear Systems with Constant Coefficients|§31]] are complex-valued. Their real and imaginary parts are two independent real solutions, built from $e^{\lambda t}\cos\mu t$ and $e^{\lambda t}\sin\mu t$, exactly as for complex roots of the characteristic equation in [[§15 Complex Roots of the Characteristic Equation|§15]]. In the phase plane the factor $e^{\lambda t}$ makes trajectories spiral in or out while the trigonometric factors rotate them, so the origin is a spiral point, or a center when $\lambda = 0$. With the saddle points and nodes of [[§31 Homogeneous Linear Systems with Constant Coefficients|§31]] this completes the classification of $2 \times 2$ systems, and following the eigenvalues as a parameter varies shows where the phase portrait changes type. The linear-algebra side of complex eigenvalues is [[§36 Complex Eigenvalues|235 §36]].

## Complex Eigenvalues and Real Solutions

Let $\mathbf{A}$ be real. Solutions $\mathbf{x} = \boldsymbol{\xi}e^{rt}$ of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ (1) again require $r$ to be a root of the characteristic equation $\det(\mathbf{A} - r\mathbf{I}) = 0$ (2) and $\boldsymbol{\xi}$ a nonzero solution of $(\mathbf{A} - r\mathbf{I})\boldsymbol{\xi} = \mathbf{0}$ (3) ([[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|Theorem §31.1]]). The polynomial (2) has real coefficients, so its complex roots occur in conjugate pairs: if $r_1 = \lambda + i\mu$ is an eigenvalue, so is $r_2 = \lambda - i\mu$.

> [!example] Example §32.1: A Spiral Point
> Find a fundamental set of real-valued solutions of
>
> $$
> \mathbf{x}' = \begin{pmatrix} -\frac12 & 1 \\ -1 & -\frac12 \end{pmatrix}\mathbf{x} \qquad (4)
> $$
>
> and describe the phase portrait. (The direction field suggests that the trajectories spiral clockwise toward the origin.)
>
> **Eigenvalues.** With $\mathbf{x} = \boldsymbol{\xi}e^{rt}$,
>
> $$
> \begin{vmatrix} -\frac12 - r & 1 \\ -1 & -\frac12 - r \end{vmatrix} = \big(r + \tfrac12\big)^2 + 1 = r^2 + r + \frac54 = 0, \qquad (7)
> $$
>
> so $r_1 = -\frac12 + i$ and $r_2 = -\frac12 - i$.
>
> **Eigenvectors.** For $r_1$ the first row of $\mathbf{A} - r_1\mathbf{I}$ is $(-i, 1)$, so $-i\xi_1 + \xi_2 = 0$ and $\boldsymbol{\xi}^{(1)} = (1, i)^T$. For $r_2$ the same computation gives $\boldsymbol{\xi}^{(2)} = (1, -i)^T$, the complex conjugate of $\boldsymbol{\xi}^{(1)}$. A fundamental set of (complex) solutions is
>
> $$
> \mathbf{x}^{(1)}(t) = \begin{pmatrix} 1 \\ i \end{pmatrix}e^{(-1/2 + i)t}, \qquad \mathbf{x}^{(2)}(t) = \begin{pmatrix} 1 \\ -i \end{pmatrix}e^{(-1/2 - i)t} . \qquad (9)
> $$
>
> **Real solutions.** By [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-5|Theorem §30.5]], the real and imaginary parts of $\mathbf{x}^{(1)}$ are solutions. Using Euler's formula $e^{it} = \cos t + i\sin t$,
>
> $$
> \mathbf{x}^{(1)}(t) = \begin{pmatrix} 1 \\ i \end{pmatrix}e^{-t/2}(\cos t + i\sin t) = \begin{pmatrix} e^{-t/2}\cos t \\ -e^{-t/2}\sin t \end{pmatrix} + i\begin{pmatrix} e^{-t/2}\sin t \\ e^{-t/2}\cos t \end{pmatrix}, \qquad (10)
> $$
>
> so
>
> $$
> \mathbf{u}(t) = e^{-t/2}\begin{pmatrix} \cos t \\ -\sin t \end{pmatrix}, \qquad \mathbf{v}(t) = e^{-t/2}\begin{pmatrix} \sin t \\ \cos t \end{pmatrix} . \qquad (11)
> $$
>
> Their Wronskian is
>
> $$
> W[\mathbf{u}, \mathbf{v}](t) = \begin{vmatrix} e^{-t/2}\cos t & e^{-t/2}\sin t \\ -e^{-t/2}\sin t & e^{-t/2}\cos t \end{vmatrix} = e^{-t}(\cos^2 t + \sin^2 t) = e^{-t} \ne 0,
> $$
>
> so $\mathbf{u}$ and $\mathbf{v}$ form a fundamental set of real-valued solutions.
>
> **Phase portrait** (figure below, panel (a)). $\mathbf{u}(0) = (1, 0)^T$ and $\mathbf{v}(0) = (0, 1)^T$. Every solution $c_1\mathbf{u} + c_2\mathbf{v}$ is a decaying exponential times sines and cosines, so each trajectory approaches the origin along a spiral, making infinitely many circuits; each component is a decaying oscillation in $t$. For the direction of rotation, check one point: at $\mathbf{x} = (0, 1)^T$, $\mathbf{A}\mathbf{x} = (1, -\frac12)^T$ has a positive $x_1$-component, so trajectories cross the positive $x_2$-axis from the second quadrant into the first. The motion is clockwise.
>
> *BDP: Example 7.6.1*

^ex-32-1

> [!definition] Definition §32.1: Spiral Point; Center
> Let the $2 \times 2$ real system $\mathbf{x}' = \mathbf{A}\mathbf{x}$ have complex eigenvalues $\lambda \pm i\mu$, $\mu \ne 0$.
> - If $\lambda \ne 0$, the origin is a **spiral point**. If $\lambda < 0$ the trajectories spiral in toward the origin and it is asymptotically stable; if $\lambda > 0$ they spiral out, become unbounded, and the origin is unstable.
> - If $\lambda = 0$, the trajectories neither approach the origin nor become unbounded, but repeatedly traverse closed curves about it. The origin is then a **center**, and it is said to be **stable, but not asymptotically stable**.
>
> In each case the motion may be clockwise or counterclockwise, depending on the entries of $\mathbf{A}$.
>
> *BDP: 7.6 (text)*

^def-32-1

![[m331-32-1.svg]]
*Trajectories computed from the real solutions. (a) Spiral point of Example §32.1: $\mathbf{u}$ through $(1, 0)$ (red), $\mathbf{v}$ through $(0, 1)$ (green), and other combinations $c_1\mathbf{u} + c_2\mathbf{v}$ (blue), all spiraling clockwise into the origin; each circuit shrinks by the factor $e^{-\pi} \approx 0.04$. (b) Center of Example §32.2(b), $\mathbf{A} = \begin{pmatrix} -4 & 5 \\ -5 & 4 \end{pmatrix}$ with eigenvalues $\pm 3i$: every trajectory is an ellipse traversed clockwise with period $2\pi/3$; the red one passes through $(1.5, 0)$.*

> [!theorem] Theorem §32.1: Conjugate Eigenvalues Have Conjugate Eigenvectors
> Let $\mathbf{A}$ be real, and let $r_1 = \lambda + i\mu$ be an eigenvalue with eigenvector $\boldsymbol{\xi}^{(1)}$. Then $r_2 = \bar r_1 = \lambda - i\mu$ is an eigenvalue with eigenvector $\boldsymbol{\xi}^{(2)} = \overline{\boldsymbol{\xi}^{(1)}}$, and the corresponding solutions
>
> $$
> \mathbf{x}^{(1)}(t) = \boldsymbol{\xi}^{(1)}e^{r_1t}, \qquad \mathbf{x}^{(2)}(t) = \overline{\boldsymbol{\xi}^{(1)}}e^{\bar r_1t} \qquad (14)
> $$
>
> of $\mathbf{x}' = \mathbf{A}\mathbf{x}$ are complex conjugates of each other.
>
> *BDP: 7.6 (text), Equations (12)–(14)*

^thm-32-1

> [!proof]+ Proof
> $r_1$ and $\boldsymbol{\xi}^{(1)}$ satisfy
>
> $$
> (\mathbf{A} - r_1\mathbf{I})\boldsymbol{\xi}^{(1)} = \mathbf{0} . \qquad (12)
> $$
>
> Take complex conjugates. The conjugate of a product is the product of the conjugates, and $\mathbf{A}$ and $\mathbf{I}$ are real, so
>
> $$
> \overline{(\mathbf{A} - r_1\mathbf{I})\boldsymbol{\xi}^{(1)}} = (\mathbf{A} - \bar r_1\mathbf{I})\overline{\boldsymbol{\xi}^{(1)}} = \mathbf{0} . \qquad (13)
> $$
>
> Since $\overline{\boldsymbol{\xi}^{(1)}} \ne \mathbf{0}$, $\bar r_1$ is an eigenvalue with eigenvector $\overline{\boldsymbol{\xi}^{(1)}}$. Finally $\overline{e^{r_1t}} = \overline{e^{\lambda t}(\cos\mu t + i\sin\mu t)} = e^{\lambda t}(\cos\mu t - i\sin\mu t) = e^{\bar r_1t}$ for real $t$, so $\overline{\mathbf{x}^{(1)}(t)} = \overline{\boldsymbol{\xi}^{(1)}}\,e^{\bar r_1t} = \mathbf{x}^{(2)}(t)$.

^pf-32-1

*Uses:* [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-4|Def. §29.4]], [[§15 Complex Roots of the Characteristic Equation#^def-15-1|Def. §15.1]] (Euler's formula)

> [!remark]- Connections
> - See also: [[§36 Complex Eigenvalues#^thm-36-2|235 Thm. §36.2]] (same statement), with the rules for conjugating matrix products in [[§36 Complex Eigenvalues#^prop-36-1|235 Prop. §36.1]].

So the two complex solutions carry the same information, and either one yields two real solutions.

> [!theorem] Theorem §32.2: Real Solutions from a Pair of Complex Eigenvalues
> Let $\mathbf{A}$ be real, with eigenvalue $r_1 = \lambda + i\mu$ ($\mu \ne 0$) and eigenvector $\boldsymbol{\xi}^{(1)} = \mathbf{a} + i\mathbf{b}$, where $\mathbf{a}$ and $\mathbf{b}$ are real vectors. Then
>
> $$
> \mathbf{u}(t) = e^{\lambda t}\big(\mathbf{a}\cos\mu t - \mathbf{b}\sin\mu t\big), \qquad \mathbf{v}(t) = e^{\lambda t}\big(\mathbf{a}\sin\mu t + \mathbf{b}\cos\mu t\big) \qquad (17)
> $$
>
> are linearly independent real-valued solutions of $\mathbf{x}' = \mathbf{A}\mathbf{x}$; they are the real and imaginary parts of $\mathbf{x}^{(1)}(t) = \boldsymbol{\xi}^{(1)}e^{r_1t}$.
>
> If the remaining eigenvalues $r_3, \ldots, r_n$ of the $n \times n$ matrix $\mathbf{A}$ are real and distinct, with eigenvectors $\boldsymbol{\xi}^{(3)}, \ldots, \boldsymbol{\xi}^{(n)}$, the general solution is
>
> $$
> \mathbf{x} = c_1\mathbf{u}(t) + c_2\mathbf{v}(t) + c_3\boldsymbol{\xi}^{(3)}e^{r_3t} + \cdots + c_n\boldsymbol{\xi}^{(n)}e^{r_nt} . \qquad (18)
> $$
>
> This analysis needs $\mathbf{A}$ to be real: only then must complex eigenvalues and eigenvectors occur in conjugate pairs.
>
> *BDP: 7.6 (text), Equations (15)–(18)*

^thm-32-2

> [!proof]+ Proof
> **Real and imaginary parts.** By Euler's formula,
>
> $$
> \mathbf{x}^{(1)}(t) = (\mathbf{a} + i\mathbf{b})e^{(\lambda + i\mu)t} = (\mathbf{a} + i\mathbf{b})e^{\lambda t}\big(\cos\mu t + i\sin\mu t\big) . \qquad (15)
> $$
>
> Multiplying out and collecting the terms without and with $i$,
>
> $$
> \mathbf{x}^{(1)}(t) = e^{\lambda t}\big(\mathbf{a}\cos\mu t - \mathbf{b}\sin\mu t\big) + ie^{\lambda t}\big(\mathbf{a}\sin\mu t + \mathbf{b}\cos\mu t\big) = \mathbf{u}(t) + i\mathbf{v}(t) . \qquad (16)
> $$
>
> $\mathbf{x}^{(1)}$ is a solution ([[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|Theorem §31.1]]) and $\mathbf{A}$ is real, so $\mathbf{u}$ and $\mathbf{v}$ are solutions by [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-5|Theorem §30.5]].
>
> **Independence.** *BDP leaves this to Problem 22, which outlines the following argument.* Since $\mu \ne 0$, $r_1 \ne \bar r_1$, so the eigenvectors $\boldsymbol{\xi}^{(1)}$ and $\overline{\boldsymbol{\xi}^{(1)}}$ (Theorem §32.1) are linearly independent ([[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|Theorem §29.4]]).
>
> *$\mathbf{a}$ and $\mathbf{b}$ are independent.* We have $\mathbf{a} = \frac12(\boldsymbol{\xi}^{(1)} + \overline{\boldsymbol{\xi}^{(1)}})$ and $\mathbf{b} = \frac1{2i}(\boldsymbol{\xi}^{(1)} - \overline{\boldsymbol{\xi}^{(1)}})$. If $c_1\mathbf{a} + c_2\mathbf{b} = \mathbf{0}$, then multiplying by $2$,
>
> $$
> (c_1 - ic_2)\,\boldsymbol{\xi}^{(1)} + (c_1 + ic_2)\,\overline{\boldsymbol{\xi}^{(1)}} = \mathbf{0},
> $$
>
> since $\frac{c_2}{i} = -ic_2$. By independence, $c_1 - ic_2 = 0$ and $c_1 + ic_2 = 0$; adding and subtracting, $c_1 = c_2 = 0$.
>
> *$\mathbf{u}$ and $\mathbf{v}$ are independent at every point.* Fix $t_0$ and suppose $c_1\mathbf{u}(t_0) + c_2\mathbf{v}(t_0) = \mathbf{0}$. Writing $C = \cos\mu t_0$, $S = \sin\mu t_0$ and dividing by $e^{\lambda t_0} \ne 0$,
>
> $$
> (c_1C + c_2S)\,\mathbf{a} + (c_2C - c_1S)\,\mathbf{b} = \mathbf{0} .
> $$
>
> Since $\mathbf{a}$, $\mathbf{b}$ are independent, $c_1C + c_2S = 0$ and $-c_1S + c_2C = 0$. This $2 \times 2$ system for $c_1$, $c_2$ has determinant $C^2 + S^2 = 1 \ne 0$, so $c_1 = c_2 = 0$.
>
> So $W[\mathbf{u}, \mathbf{v}]$ never vanishes in the $2 \times 2$ case, and in general $\mathbf{u}$, $\mathbf{v}$ are independent at every point and on every interval.
>
> **The general solution (18).** (BDP states it; here is why it is general.) At any $t$, $\mathbf{u}(t)$ and $\mathbf{v}(t)$ span the same complex space as $\mathbf{x}^{(1)}(t)$ and $\overline{\mathbf{x}^{(1)}(t)}$ (since $\mathbf{x}^{(1)} = \mathbf{u} + i\mathbf{v}$, $\overline{\mathbf{x}^{(1)}} = \mathbf{u} - i\mathbf{v}$). The $n$ solutions $\mathbf{x}^{(1)}, \overline{\mathbf{x}^{(1)}}, \boldsymbol{\xi}^{(3)}e^{r_3t}, \ldots, \boldsymbol{\xi}^{(n)}e^{r_nt}$ come from $n$ distinct eigenvalues, so their Wronskian is $e^{(r_1 + \cdots + r_n)t}$ times a nonzero determinant, as in (28) of [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|Theorem §31.2]]. Replacing the first two columns by $\mathbf{u} = \frac12(\mathbf{x}^{(1)} + \overline{\mathbf{x}^{(1)}})$ and $\mathbf{v} = \frac1{2i}(\mathbf{x}^{(1)} - \overline{\mathbf{x}^{(1)}})$ multiplies this Wronskian by the nonzero number $\det\begin{pmatrix} 1/2 & 1/(2i) \\ 1/2 & -1/(2i) \end{pmatrix} = \frac{i}{2}$, so the solutions in (18) also form a fundamental set ([[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Definition §30.3]]).

^pf-32-2

*Uses:* [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|§31.1]], [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|§31.2]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-5|§30.5]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-3|Def. §30.3]], [[§32 Complex-Valued Eigenvalues#^thm-32-1|§32.1]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-4|§29.4]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-2|Def. §29.2]], [[§15 Complex Roots of the Characteristic Equation#^def-15-1|Def. §15.1]] (Euler's formula)

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^thm-38-4|235 Thm. §38.4]] (Lay's version, with $\operatorname{Re}\mathbf{v}$ and $\operatorname{Im}\mathbf{v}$ for $\mathbf{a}$ and $\mathbf{b}$), whose independence proof uses the same fact that $\mathbf{a}$, $\mathbf{b}$ are independent, [[§36 Complex Eigenvalues#^thm-36-4|235 Thm. §36.4]] (Step 1); there it also gives $\mathbf{A} = P\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix}P^{-1}$ with $P = [\,\mathbf{a}\ \ \mathbf{b}\,]$, a rotation–scaling matrix.

> [!remark] Remark: Method — The Complex-Eigenvalue Case
> 1. **Eigenvalues.** Solve $\det(\mathbf{A} - r\mathbf{I}) = 0$; for $2 \times 2$ matrices complete the square in $r^2 - (\operatorname{tr}\mathbf{A})r + \det\mathbf{A}$ to get $r = \lambda \pm i\mu$.
> 2. **One eigenvector.** Find an eigenvector $\boldsymbol{\xi}$ for $r_1 = \lambda + i\mu$ only; one row of $\mathbf{A} - r_1\mathbf{I}$ suffices (the other row is a complex multiple of it). Split $\boldsymbol{\xi} = \mathbf{a} + i\mathbf{b}$.
> 3. **Real solutions.** Expand $\boldsymbol{\xi}e^{\lambda t}(\cos\mu t + i\sin\mu t)$ and take real and imaginary parts, or use (17) directly.
> 4. **General solution.** $\mathbf{x} = c_1\mathbf{u}(t) + c_2\mathbf{v}(t)$ (plus terms for the other eigenvalues). For an initial value problem, $\mathbf{x}(0) = c_1\mathbf{a} + c_2\mathbf{b}$.
> 5. **Type and direction.** The sign of $\lambda$ decides spiral in, spiral out or center (Definition §32.1). For the direction of rotation, compute $\mathbf{A}\mathbf{x}$ at one convenient point, such as $(1, 0)^T$ or $(0, 1)^T$, and see which way the tangent vector turns around the origin.

^rem-32-1

## Classification of 2 × 2 Systems

> [!theorem] Theorem §32.3: Classification of the Origin for 2 × 2 Systems
> Let $\mathbf{A}$ be a real $2 \times 2$ matrix with $\det\mathbf{A} \ne 0$ and eigenvalues $r_1$, $r_2$. For $\mathbf{x}' = \mathbf{A}\mathbf{x}$, the equilibrium $\mathbf{x} = \mathbf{0}$ is:
>
> | eigenvalues | the origin is | stability | MATH 331 name |
> |---|---|---|---|
> | real, opposite signs | saddle point | unstable | saddle |
> | real, unequal, both negative | node | asymptotically stable | sink (node) |
> | real, unequal, both positive | node | unstable | source |
> | $\lambda \pm i\mu$, $\lambda < 0$ | spiral point | asymptotically stable | spiral sink |
> | $\lambda \pm i\mu$, $\lambda > 0$ | spiral point | unstable | spiral source |
> | $\pm i\mu$ ($\lambda = 0$) | center | stable, not asymptotically stable | center |
>
> The first three rows and the two spiral rows are BDP's three main cases: real eigenvalues of opposite signs (saddle point), real eigenvalues of the same sign but unequal (node), and complex eigenvalues with nonzero real part (spiral point). Equal real eigenvalues are treated in [[§34★ Repeated Eigenvalues|§34★]].
>
> *BDP: 7.5 (text); 7.6 (text)*
> *Source: 331 Written HW 6, Problems 2 and 4 (the names in the last column)*

^thm-32-3

> [!proof]+ Proof
> *BDP establishes the cases through [[§31 Homogeneous Linear Systems with Constant Coefficients#^ex-31-1|Example §31.1]], [[§31 Homogeneous Linear Systems with Constant Coefficients#^ex-31-2|Example §31.2]] and Example §32.1, each "typical of all $2 \times 2$ systems" of its kind; here is the general argument.* In each case write the general solution in coordinates adapted to $\mathbf{A}$.
>
> **Real eigenvalues** $r_1 \ne r_2$, with eigenvectors $\boldsymbol{\xi}^{(1)}$, $\boldsymbol{\xi}^{(2)}$. By [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|Theorem §31.2]], $\mathbf{x}(t) = c_1e^{r_1t}\boldsymbol{\xi}^{(1)} + c_2e^{r_2t}\boldsymbol{\xi}^{(2)} = \mathbf{T}\mathbf{y}(t)$, where $\mathbf{T}$ has columns $\boldsymbol{\xi}^{(1)}$, $\boldsymbol{\xi}^{(2)}$ (invertible, by [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|Theorem §29.2]]) and $\mathbf{y}(t) = (c_1e^{r_1t}, c_2e^{r_2t})^T$. Since $\mathbf{y} = \mathbf{T}^{-1}\mathbf{x}$, $\mathbf{x}(t) \to \mathbf{0}$ if and only if $\mathbf{y}(t) \to \mathbf{0}$, and $\mathbf{x}$ is unbounded if and only if $\mathbf{y}$ is.
> - Both $r_i < 0$: $\mathbf{y}(t) \to \mathbf{0}$ for all $c_1, c_2$, so every solution tends to $\mathbf{0}$; moreover $|\mathbf{y}(t)| \le |\mathbf{y}(0)|$ for $t \ge 0$, so $|\mathbf{x}(t)| \le \|\mathbf{T}\|\,\|\mathbf{T}^{-1}\|\,|\mathbf{x}(0)|$ and solutions that start near $\mathbf{0}$ stay near it: asymptotically stable.
> - Both $r_i > 0$: if $(c_1, c_2) \ne (0, 0)$, some $|c_ie^{r_it}| \to \infty$: every nonzero solution is unbounded, unstable.
> - $r_1 > 0 > r_2$: the solution tends to $\mathbf{0}$ if $c_1 = 0$ (the line of $\boldsymbol{\xi}^{(2)}$) and is unbounded if $c_1 \ne 0$: almost all trajectories depart, unstable.
>
> *The shape of the trajectories* (the descriptions in [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-3|Definition §31.3]] and [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-4|Definition §31.4]]). Let $c_1 \ne 0$. For a node with $r_2 < r_1 < 0$, $e^{-r_1t}\mathbf{x}(t) = c_1\boldsymbol{\xi}^{(1)} + c_2e^{(r_2 - r_1)t}\boldsymbol{\xi}^{(2)} \to c_1\boldsymbol{\xi}^{(1)}$ as $t \to \infty$, so the direction of $\mathbf{x}(t)$ tends to that of $\pm\boldsymbol{\xi}^{(1)}$: the trajectory enters the origin tangent to the eigenvector of the eigenvalue nearer to $0$. (If $c_1 = 0$ it runs along the line of $\boldsymbol{\xi}^{(2)}$.) For $0 < r_1 < r_2$ the same limit, taken as $t \to -\infty$, shows that trajectories leave the origin tangent to $\boldsymbol{\xi}^{(1)}$. For a saddle with $r_1 > 0 > r_2$ and $c_1c_2 \ne 0$, $e^{-r_1t}\mathbf{x}(t) \to c_1\boldsymbol{\xi}^{(1)}$ as $t \to \infty$ and $e^{-r_2t}\mathbf{x}(t) \to c_2\boldsymbol{\xi}^{(2)}$ as $t \to -\infty$, while $|\mathbf{x}(t)| \to \infty$ at both ends: the trajectory comes in along the line of $\boldsymbol{\xi}^{(2)}$, leaves along that of $\boldsymbol{\xi}^{(1)}$, and never approaches the origin. So the eigenvector lines ($c_1 = 0$ or $c_2 = 0$) are the only trajectories that tend to the origin.
>
> **Complex eigenvalues** $\lambda \pm i\mu$, $\mu \ne 0$, with eigenvector $\mathbf{a} + i\mathbf{b}$. By Theorem §32.2, $\mathbf{x} = c_1\mathbf{u} + c_2\mathbf{v}$, and collecting the coefficients of $\mathbf{a}$ and $\mathbf{b}$ in (17),
>
> $$
> \mathbf{x}(t) = e^{\lambda t}\big[(c_1\cos\mu t + c_2\sin\mu t)\,\mathbf{a} + (-c_1\sin\mu t + c_2\cos\mu t)\,\mathbf{b}\big] = \mathbf{T}\mathbf{y}(t), \qquad
> \mathbf{y}(t) = e^{\lambda t}\begin{pmatrix} \cos\mu t & \sin\mu t \\ -\sin\mu t & \cos\mu t \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix},
> $$
>
> with $\mathbf{T} = [\,\mathbf{a}\ \ \mathbf{b}\,]$ invertible because $\mathbf{a}$, $\mathbf{b}$ are independent (proof of Theorem §32.2). The matrix in $\mathbf{y}(t)$ is a rotation, so $\mathbf{y}(t)$ is the vector $(c_1, c_2)$ rotated by the angle $-\mu t$ and scaled by $e^{\lambda t}$: in the coordinates $\mathbf{y}$ the trajectory is a spiral $|\mathbf{y}(t)| = e^{\lambda t}\sqrt{c_1^2 + c_2^2}$ turning at constant angular speed $|\mu|$.
> - $\lambda < 0$: $\mathbf{y}(t) \to \mathbf{0}$, so $\mathbf{x}(t) \to \mathbf{0}$ while winding around the origin infinitely often (the invertible linear map $\mathbf{T}$ carries a curve winding around $\mathbf{0}$ to one winding around $\mathbf{0}$), and as in the node case $|\mathbf{x}(t)| \le \|\mathbf{T}\|\,\|\mathbf{T}^{-1}\|\,|\mathbf{x}(0)|$ for $t \ge 0$: asymptotically stable spiral point.
> - $\lambda > 0$: $|\mathbf{y}(t)| \to \infty$ for $\mathbf{x} \ne \mathbf{0}$: unstable spiral point.
> - $\lambda = 0$: $\mathbf{y}(t)$ runs around a circle with period $2\pi/|\mu|$, so $\mathbf{x}(t) = \mathbf{T}\mathbf{y}(t)$ runs around an ellipse, the image of the circle under $\mathbf{T}$: a closed curve, periodic in time. Solutions starting near $\mathbf{0}$ stay near it ($|\mathbf{x}(t)| \le \|\mathbf{T}\|\,|\mathbf{y}(0)|$ and $|\mathbf{y}(0)| \le \|\mathbf{T}^{-1}\|\,|\mathbf{x}(0)|$) but do not approach it: stable, not asymptotically stable.

^pf-32-3

*Uses:* [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|§31.2]], [[§32 Complex-Valued Eigenvalues#^thm-32-2|§32.2]], [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^thm-29-2|§29.2]], [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-1|Def. §31.1]], [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-3|Def. §31.3]], [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-4|Def. §31.4]], [[§32 Complex-Valued Eigenvalues#^def-32-1|Def. §32.1]]

> [!remark]- Connections
> - See also: [[§38 Applications to Differential Equations#^def-38-2|235 Def. §38.2]] (attractor, repeller, saddle point for $\mathbf{x}' = A\mathbf{x}$) and [[§38 Applications to Differential Equations#^ex-38-3|235 Ex. §38.3]] (a spiral point in an RLC circuit). The discrete-time classification, with $|\lambda|$ compared to $1$ and spirals from complex eigenvalues: [[§37 Discrete Dynamical Systems#^prop-37-3|235 Prop. §37.3]] and [[§37 Discrete Dynamical Systems#^ex-37-4|235 Ex. §37.4]]. The coordinates $\mathbf{y}$ in the complex case are those of [[§36 Complex Eigenvalues#^thm-36-4|235 Thm. §36.4]].
> - A nonlinear system drawn in the same phase plane: the predator–prey equations of [[§62 Predator-Prey Systems#^def-62-1|Calc Def. §62.1]], whose trajectories around the coexistence equilibrium are closed cycles ([[§62 Predator-Prey Systems#^ex-62-2|Calc Ex. §62.2]]), as around a center.

> [!remark] Remark: Transitions Between the Cases
> Other possibilities occur as transitions between the main cases and are less likely in applications:
> - a **zero eigenvalue** occurs in the transition between a saddle point and a node;
> - **purely imaginary eigenvalues** (a center) occur in the transition between asymptotically stable and unstable spiral points;
> - **real and equal eigenvalues** occur in the transition between nodes and spiral points.
>
> A value of a parameter in $\mathbf{A}$ at which the qualitative behavior of the trajectories changes in this way is a **bifurcation value**. For $2 \times 2$ matrices the eigenvalues are $r = \frac12\big(\operatorname{tr}\mathbf{A} \pm \sqrt{(\operatorname{tr}\mathbf{A})^2 - 4\det\mathbf{A}}\big)$, so the transitions happen where $\det\mathbf{A} = 0$, where $\operatorname{tr}\mathbf{A} = 0$ with $\det\mathbf{A} > 0$, and where $(\operatorname{tr}\mathbf{A})^2 = 4\det\mathbf{A}$.

^rem-32-2

> [!example] Example §32.2: Classifying Complex-Eigenvalue Systems
> For each matrix, find the eigenvalues and an eigenvector, the type of the origin for $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$, and (in (c)) the general solution.
>
> **(a)** $\mathbf{A} = \begin{pmatrix} 6 & -2 \\ 4 & 2 \end{pmatrix}$. $(6 - r)(2 - r) + 8 = r^2 - 8r + 20 = (r - 4)^2 + 4$, so $r = 4 \pm 2i$. For $r = 4 + 2i$, the first row of $\mathbf{A} - r\mathbf{I}$ is $(2 - 2i, -2)$, so $(2 - 2i)a = 2b$, $b = (1 - i)a$, and $\boldsymbol{\xi}^{(1)} = (1, 1 - i)^T$; then $\boldsymbol{\xi}^{(2)} = \overline{\boldsymbol{\xi}^{(1)}} = (1, 1 + i)^T$ for $4 - 2i$. Real part $4 > 0$: a **spiral source** (unstable spiral point). With $\mathbf{a} = (1, 1)^T$, $\mathbf{b} = (0, -1)^T$, (17) gives the real solutions $e^{4t}(\cos 2t,\ \cos 2t + \sin 2t)^T$ and $e^{4t}(\sin 2t,\ \sin 2t - \cos 2t)^T$.
>
> **(b)** $\mathbf{A} = \begin{pmatrix} -4 & 5 \\ -5 & 4 \end{pmatrix}$. $(-4 - r)(4 - r) + 25 = r^2 + 9$, so $r = \pm 3i$: a **center**. For $r = 3i$, the first row of $\mathbf{A} - 3i\mathbf{I}$ gives $(-4 - 3i)a + 5b = 0$, so $\boldsymbol{\xi}^{(1)} = (5, 4 + 3i)^T$ and $\boldsymbol{\xi}^{(2)} = (5, 4 - 3i)^T$. With $\mathbf{a} = (5, 4)^T$, $\mathbf{b} = (0, 3)^T$, $\lambda = 0$, $\mu = 3$:
>
> $$
> \mathbf{u}(t) = \begin{pmatrix} 5\cos 3t \\ 4\cos 3t - 3\sin 3t \end{pmatrix}, \qquad \mathbf{v}(t) = \begin{pmatrix} 5\sin 3t \\ 4\sin 3t + 3\cos 3t \end{pmatrix},
> $$
>
> periodic with period $2\pi/3$: the trajectories are ellipses (panel (b) of the figure above). At $(1, 0)^T$, $\mathbf{A}\mathbf{x} = (-4, -5)^T$ points down, so the motion is clockwise.
>
> **(c)** $\mathbf{A} = \begin{pmatrix} -1 & 4 \\ -5 & -5 \end{pmatrix}$. $(-1 - r)(-5 - r) + 20 = r^2 + 6r + 25 = (r + 3)^2 + 16$, so $r = -3 \pm 4i$: a **spiral sink** (asymptotically stable spiral point). Direction: at $(1, 0)^T$, $\mathbf{A}\mathbf{x} = (-1, -5)^T$ points down, so clockwise.
>
> **Eigenvector.** For $r = -3 + 4i$, the first row of $\mathbf{A} - r\mathbf{I}$ is $(2 - 4i, 4)$: $(2 - 4i)\xi_1 + 4\xi_2 = 0$, so $4\xi_2 = (-2 + 4i)\xi_1$ and $\boldsymbol{\xi}^{(1)} = (2, -1 + 2i)^T = \mathbf{a} + i\mathbf{b}$ with $\mathbf{a} = (2, -1)^T$, $\mathbf{b} = (0, 2)^T$.
>
> **General solution.** By (17) with $\lambda = -3$, $\mu = 4$,
>
> $$
> \mathbf{Y}(t) = c_1e^{-3t}\begin{pmatrix} 2\cos 4t \\ -\cos 4t - 2\sin 4t \end{pmatrix} + c_2e^{-3t}\begin{pmatrix} 2\sin 4t \\ -\sin 4t + 2\cos 4t \end{pmatrix} .
> $$
>
> Check with Abel's formula: the Wronskian of the two solutions is $4e^{-6t}$, and indeed $\operatorname{tr}\mathbf{A} = -6$.
>
> *Source: 331 Written HW 6, Problems 2(b), 2(c) and 4*

^ex-32-2

> [!example] Example §32.3: Two Spiral Sinks from Final Exams
> **(a)** For $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$ with $\mathbf{A} = \begin{pmatrix} -2 & 5 \\ -2 & 0 \end{pmatrix}$, find the eigenvalues and an eigenvector for one of them, sketch the phase portrait, and classify the origin.
>
> **Eigenvalues.** $\det(\mathbf{A} - r\mathbf{I}) = (-2 - r)(-r) + 10 = r^2 + 2r + 10 = (r + 1)^2 + 9$, so $r_{1,2} = -1 \pm 3i$.
>
> **Eigenvector.** $\mathbf{A}(a, b)^T = (-1 + 3i)(a, b)^T$ reads $-2a + 5b = (-1 + 3i)a$ and $-2a = (-1 + 3i)b$. The second (simpler) equation is satisfied by $b = -2$, $a = -1 + 3i$:
>
> $$
> \boldsymbol{\xi}^{(1)} = \begin{pmatrix} -1 + 3i \\ -2 \end{pmatrix} .
> $$
>
> (Check with the first equation: $-2(-1 + 3i) - 10 = -8 - 6i = (-1 + 3i)^2$.)
>
> **Classification and sketch.** The real part $-1$ is negative: a **spiral sink**. For the direction, at $(1, 0)^T$ the tangent vector is $\mathbf{A}(1, 0)^T = (-2, -2)^T$, pointing down and to the left, so the trajectories spiral into the origin **clockwise**. (With $\mathbf{a} = (-1, -2)^T$, $\mathbf{b} = (3, 0)^T$, the real solutions are $e^{-t}(-\cos 3t - 3\sin 3t,\ -2\cos 3t)^T$ and $e^{-t}(3\cos 3t - \sin 3t,\ -2\sin 3t)^T$.)
>
> **(b)** Find the general solution of $\mathbf{Y}' = \mathbf{A}\mathbf{Y}$ with $\mathbf{A} = \begin{pmatrix} -3 & 4 \\ -2 & 1 \end{pmatrix}$, sketch the phase portrait, and classify the origin.
>
> **Eigenvalues.** $(-3 - r)(1 - r) + 8 = r^2 + 2r + 5 = (r + 1)^2 + 4$, so $r = -1 \pm 2i$.
>
> **Eigenvector.** For $r = -1 + 2i$ the second row of $\mathbf{A} - r\mathbf{I}$ is $(-2, 2 - 2i)$: $-2a + (2 - 2i)b = 0$, so $a = (1 - i)b$ and
>
> $$
> \boldsymbol{\xi}^{(1)} = \begin{pmatrix} 1 - i \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} + i\begin{pmatrix} -1 \\ 0 \end{pmatrix} .
> $$
>
> **General solution.** By (17) with $\mathbf{a} = (1, 1)^T$, $\mathbf{b} = (-1, 0)^T$, $\lambda = -1$, $\mu = 2$:
>
> $$
> \mathbf{Y}(t) = c_1e^{-t}\begin{pmatrix} \cos 2t + \sin 2t \\ \cos 2t \end{pmatrix} + c_2e^{-t}\begin{pmatrix} \sin 2t - \cos 2t \\ \sin 2t \end{pmatrix} .
> $$
>
> (The Wronskian is $e^{-2t}$, matching $\operatorname{tr}\mathbf{A} = -2$.)
>
> **Classification and sketch.** Real part $-1 < 0$: a **spiral sink**. At $(1, 0)^T$, $\mathbf{A}\mathbf{x} = (-3, -2)^T$ points down and to the left, so the spirals turn **clockwise** as they close in on the origin.
>
> *Source: 331 Final (Fall 2021), Q7; 331 Final (Fall 2022, alternate), Q6*

^ex-32-3

> [!example] Example §32.4: Bifurcation Values of a Parameter
> **(a)** For
>
> $$
> \mathbf{x}' = \begin{pmatrix} \alpha & 2 \\ -2 & 0 \end{pmatrix}\mathbf{x}, \qquad (19)
> $$
>
> describe how the solutions depend qualitatively on $\alpha$, and find the bifurcation values.
>
> The characteristic equation is $(\alpha - r)(-r) + 4 = r^2 - \alpha r + 4 = 0$ (20), so
>
> $$
> r = \frac{\alpha \pm \sqrt{\alpha^2 - 16}}{2} . \qquad (21)
> $$
>
> - $-4 < \alpha < 4$: the eigenvalues are complex conjugates, $\frac{\alpha}{2} \pm \frac{i}{2}\sqrt{16 - \alpha^2}$, and the trajectories are spirals: directed inward (asymptotically stable spiral point) for $-4 < \alpha < 0$ and outward (unstable) for $0 < \alpha < 4$. At $\alpha = 0$ the eigenvalues are $\pm 2i$, the origin is a center and the solutions are periodic.
> - $\alpha < -4$: two negative real eigenvalues (their product is $4 > 0$ and their sum $\alpha < 0$): an asymptotically stable node.
> - $\alpha > 4$: two positive eigenvalues: an unstable node, all trajectories except $\mathbf{x} = \mathbf{0}$ unbounded.
>
> So there are three bifurcation values: $\alpha = -4$ and $\alpha = 4$, where the eigenvalues change between real and complex (at which they are real and equal, a node of the kind treated in [[§34★ Repeated Eigenvalues|§34★]]), and $\alpha = 0$, where the spirals change from inward to outward. At $(1, 0)^T$ the tangent vector is $(\alpha, -2)^T$, so the rotation is clockwise for every $\alpha$ with complex eigenvalues.
>
> **(b)** For $\mathbf{x}' = \begin{pmatrix} \alpha & -2 \\ 8 & \alpha \end{pmatrix}\mathbf{x}$: (a) determine the eigenvalues in terms of $\alpha$, (b) find the bifurcation values, (c) describe the phase portraits just below and above each.
>
> $\det(\mathbf{A} - \lambda\mathbf{I}) = (\alpha - \lambda)^2 + 16 = 0$ gives $\lambda = \alpha \pm 4i$. The eigenvalues are complex for every $\alpha$, so nodes and saddles never occur; only the sign of the real part $\alpha$ matters. For $\alpha < 0$ the origin is a spiral sink, for $\alpha = 0$ a center, for $\alpha > 0$ a spiral source: the only bifurcation value is $\alpha = 0$. At $(1, 0)^T$ the tangent vector is $(\alpha, 8)^T$, pointing up, so the rotation is counterclockwise: for $\alpha = -1$ the trajectories spiral counterclockwise into the origin, for $\alpha = 1$ counterclockwise outward.
>
> *BDP: Example 7.6.2*
> *Source: 331 Written HW 6, Problem 3*

^ex-32-4

![[m331-32-2.svg]]
*The phase portraits of system (19) as $\alpha$ increases through the bifurcation values $-4$, $0$, $4$, computed from the exact solutions. At $\alpha = \pm 5$ the eigenvalues are $-1, -4$ and $4, 1$ (red: the slow eigenvector line, along which trajectories meet the origin; green: the fast one). At $\alpha = \pm 2$ they are $\pm 1 \pm i\sqrt3$, and at $\alpha = 0$, $\pm 2i$: the matrix is then a rotation and the trajectories are circles. All rotation is clockwise.*

## A Multiple Spring–Mass System

Two masses $m_1$, $m_2$ connected by three springs with constants $k_1$, $k_2$, $k_3$ (the system of [[§27 Introduction to Systems of First-Order Linear Equations#^ex-27-1|Example §27.1]](a)) satisfy, without external forces,

$$
m_1\frac{d^2x_1}{dt^2} = -(k_1 + k_2)x_1 + k_2x_2, \qquad m_2\frac{d^2x_2}{dt^2} = k_2x_1 - (k_2 + k_3)x_2 . \qquad (22)
$$

With $y_1 = x_1$, $y_2 = x_2$, $y_3 = x_1'$, $y_4 = x_2'$ this becomes the first-order system $y_1' = y_3$, $y_2' = y_4$ (23), $m_1y_3' = -(k_1 + k_2)y_1 + k_2y_2$, $m_2y_4' = k_2y_1 - (k_2 + k_3)y_2$ (24).

> [!example] Example §32.5: Fundamental Modes of Two Masses and Three Springs
> Let $m_1 = 2$, $m_2 = \frac94$, $k_1 = 1$, $k_2 = 3$, $k_3 = \frac{15}{4}$. Then (23)–(24) become
>
> $$
> \mathbf{y}' = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -2 & \frac32 & 0 & 0 \\ \frac43 & -3 & 0 & 0 \end{pmatrix}\mathbf{y} = \mathbf{A}\mathbf{y} . \qquad (26)
> $$
>
> Analyze the possible motions.
>
> **Eigenvalues.** The characteristic polynomial is
>
> $$
> r^4 + 5r^2 + 4 = (r^2 + 1)(r^2 + 4), \qquad (27)
> $$
>
> so the eigenvalues are $r_1 = i$, $r_2 = -i$, $r_3 = 2i$, $r_4 = -2i$. (Writing $\mathbf{y} = (\boldsymbol{\eta}, r\boldsymbol{\eta})$ reduces $\mathbf{A}\mathbf{y} = r\mathbf{y}$ to $\begin{pmatrix} -2 & 3/2 \\ 4/3 & -3 \end{pmatrix}\boldsymbol{\eta} = r^2\boldsymbol{\eta}$, whose characteristic equation is $(r^2 + 2)(r^2 + 3) - 2 = r^4 + 5r^2 + 4$.)
>
> **Eigenvectors.**
>
> $$
> \boldsymbol{\xi}^{(1)} = \begin{pmatrix} 3 \\ 2 \\ 3i \\ 2i \end{pmatrix}, \quad \boldsymbol{\xi}^{(2)} = \overline{\boldsymbol{\xi}^{(1)}}, \quad \boldsymbol{\xi}^{(3)} = \begin{pmatrix} 3 \\ -4 \\ 6i \\ -8i \end{pmatrix}, \quad \boldsymbol{\xi}^{(4)} = \overline{\boldsymbol{\xi}^{(3)}} . \qquad (28)
> $$
>
> Check for $\boldsymbol{\xi}^{(1)}$: $\mathbf{A}\boldsymbol{\xi}^{(1)} = (3i,\ 2i,\ -6 + 3,\ 4 - 6)^T = (3i, 2i, -3, -2)^T = i\,\boldsymbol{\xi}^{(1)}$.
>
> **Real solutions.** By Theorem §32.2 with $\lambda = 0$,
>
> $$
> \boldsymbol{\xi}^{(1)}e^{it} = \begin{pmatrix} 3\cos t \\ 2\cos t \\ -3\sin t \\ -2\sin t \end{pmatrix} + i\begin{pmatrix} 3\sin t \\ 2\sin t \\ 3\cos t \\ 2\cos t \end{pmatrix} = \mathbf{u}^{(1)}(t) + i\mathbf{v}^{(1)}(t), \qquad (29)
> $$
>
> $$
> \boldsymbol{\xi}^{(3)}e^{2it} = \begin{pmatrix} 3\cos 2t \\ -4\cos 2t \\ -6\sin 2t \\ 8\sin 2t \end{pmatrix} + i\begin{pmatrix} 3\sin 2t \\ -4\sin 2t \\ 6\cos 2t \\ -8\cos 2t \end{pmatrix} = \mathbf{u}^{(2)}(t) + i\mathbf{v}^{(2)}(t) . \qquad (30)
> $$
>
> These four solutions are linearly independent (BDP leaves the check to the reader): at $t = 0$ they are $(3, 2, 0, 0)$, $(0, 0, 3, 2)$, $(3, -4, 0, 0)$, $(0, 0, 6, -8)$, and their determinant is $\pm\begin{vmatrix} 3 & 3 \\ 2 & -4 \end{vmatrix}\begin{vmatrix} 3 & 6 \\ 2 & -8 \end{vmatrix} = \pm(-18)(-36) \ne 0$. So the general solution is
>
> $$
> \mathbf{y} = c_1\mathbf{u}^{(1)}(t) + c_2\mathbf{v}^{(1)}(t) + c_3\mathbf{u}^{(2)}(t) + c_4\mathbf{v}^{(2)}(t) . \qquad (31)
> $$
>
> **The motion.** Every solution is periodic with period $2\pi$, so each trajectory in the four-dimensional phase space is a closed curve.
> - The terms with $c_1$, $c_2$ have frequency $1$ and period $2\pi$, with $y_2 = \frac23y_1$ and $y_4 = \frac23y_3$: the masses move back and forth together, in the same direction, the second moving two-thirds as far and as fast as the first. For $\mathbf{u}^{(1)}$, the projections onto the $y_1y_3$- and $y_2y_4$-planes are circles of radius $3$ and $2$, both traversed clockwise: the origin is a center in each plane.
> - The terms with $c_3$, $c_4$ have frequency $2$ and period $\pi$, with $y_2 = -\frac43y_1$ and $y_4 = -\frac43y_3$: the masses always move in opposite directions, the second four-thirds as far and as fast as the first (a phase difference of $\pi$). The projections of $\mathbf{u}^{(2)}$ are the ellipses $4y_1^2 + y_3^2 = 36$ and $4y_2^2 + y_4^2 = 64$.
>
> These two motions are the **fundamental modes** of the system. The first occurs only when $c_3 = c_4 = 0$, that is, for initial conditions with $3y_2(0) = 2y_1(0)$ and $3y_4(0) = 2y_3(0)$; the second only when $c_1 = c_2 = 0$, that is, $3y_2(0) = -4y_1(0)$ and $3y_4(0) = -4y_3(0)$. Any other solution is a superposition of the two modes. Its projection onto the $y_1y_3$-plane may cross itself, but the trajectory in four dimensions cannot, by the uniqueness theorem.
>
> *BDP: Example 7.6.3*

^ex-32-5
