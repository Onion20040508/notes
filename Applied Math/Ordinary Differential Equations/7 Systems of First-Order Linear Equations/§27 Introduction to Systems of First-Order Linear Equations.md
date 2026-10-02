---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 7
section: 27
bdp: "7.1"
aliases: ["BDP 7.1"]
tags: [ordinary-differential-equations, math331]
---
← [[§26★ The Convolution Integral]] · ↑ [[· 7 Systems of First-Order Linear Equations]] · [[§28 Matrices]] →

*Boyce–DiPrima, Section 7.1 · MATH 331 Written HW 6 (Problem 1).*

Problems with several interacting parts (two masses joined by springs, the voltage and current in a circuit, several tanks or species) lead to *systems* of differential equations for several unknown functions of one variable $t$. Systems of first-order equations are the general form: every equation of order $n$ can be rewritten as a system of $n$ first-order equations, which is also the form that numerical methods require. This section sets up the language (solutions, initial value problems, linear and homogeneous systems) and states the existence and uniqueness theorems, which parallel those of Chapters 2 and 3. As there, the linear case is much stronger: a solution exists on the whole interval where the coefficients are continuous.

## Systems in Applications

We write $x_1, x_2, \ldots$ for the dependent variables, all functions of $t$, and $x_1' = dx_1/dt$.

> [!example] Example §27.1: Two Models That Are Systems
> **(a) Two masses, three springs.** Two masses $m_1$, $m_2$ move on a frictionless surface, attached to each other and to two walls by springs with constants $k_1$, $k_2$, $k_3$ (left wall–$m_1$–$m_2$–right wall), and driven by external forces $F_1(t)$, $F_2(t)$. With displacements $x_1$, $x_2$ from equilibrium (positive to the right), the spring between the masses is stretched by $x_2 - x_1$, and Newton's law as in [[§19 Mechanical and Electrical Vibrations#^prop-19-1|Proposition §19.1]] gives
>
> $$
> \begin{aligned}
> m_1\frac{d^2x_1}{dt^2} &= k_2(x_2 - x_1) - k_1x_1 + F_1(t) = -(k_1 + k_2)x_1 + k_2x_2 + F_1(t), \\
> m_2\frac{d^2x_2}{dt^2} &= -k_3x_2 - k_2(x_2 - x_1) + F_2(t) = k_2x_1 - (k_2 + k_3)x_2 + F_2(t).
> \end{aligned} \qquad (1)
> $$
>
> This is a system of two *second-order* equations. With $y_1 = x_1$, $y_2 = x_2$, $y_3 = x_1'$, $y_4 = x_2'$ it becomes four first-order equations:
>
> $$
> y_1' = y_3, \qquad y_2' = y_4, \qquad y_3' = \frac{-(k_1 + k_2)y_1 + k_2y_2 + F_1(t)}{m_1}, \qquad y_4' = \frac{k_2y_1 - (k_2 + k_3)y_2 + F_2(t)}{m_2} .
> $$
>
> **(b) A parallel LRC circuit.** For a capacitor $C$, resistor $R$ and inductor $L$ in parallel, let $V$ be the voltage drop across the capacitor and $I$ the current through the inductor. Kirchhoff's laws give
>
> $$
> \frac{dI}{dt} = \frac{V}{L}, \qquad \frac{dV}{dt} = -\frac{I}{C} - \frac{V}{RC} , \qquad (2)
> $$
>
> already a system of two first-order equations.
>
> *BDP: 7.1 (text), Equations (1) and (2)*

^ex-27-1

## Higher-Order Equations as Systems

> [!example] Example §27.2: A Spring–Mass Equation as a System
> The motion of a certain spring–mass system is described by
>
> $$
> u'' + \frac18 u' + u = 0 . \qquad (3)
> $$
>
> Rewrite it as a system of first-order equations.
>
> Let $x_1 = u$ and $x_2 = u'$. Then $x_1' = x_2$, and $u'' = x_2'$. Substituting for $u$, $u'$ and $u''$ in (3) gives $x_2' + \frac18 x_2 + x_1 = 0$, so
>
> $$
> x_1' = x_2, \qquad x_2' = -x_1 - \frac18 x_2 . \qquad (4)
> $$
>
> In the same way, the general spring–mass equation $mu'' + \gamma u' + ku = F(t)$ (5) becomes, with $x_1 = u$, $x_2 = u'$,
>
> $$
> x_1' = x_2, \qquad x_2' = -\frac{k}{m}x_1 - \frac{\gamma}{m}x_2 + \frac1m F(t) , \qquad (6)
> $$
>
> and the initial conditions $u(0) = u_0$, $u'(0) = u_0'$ become $x_1(0) = u_0$, $x_2(0) = u_0'$. In the matrix notation of [[§28 Matrices#^def-28-2|§28]], (6) reads $\mathbf{x}' = \begin{pmatrix} 0 & 1 \\ -k/m & -\gamma/m \end{pmatrix}\mathbf{x} + \begin{pmatrix} 0 \\ F(t)/m \end{pmatrix}$. The eigenvalues $r$ of this coefficient matrix satisfy $\det\begin{pmatrix} -r & 1 \\ -k/m & -\gamma/m - r \end{pmatrix} = r^2 + \frac{\gamma}{m}r + \frac{k}{m} = 0$, which is the characteristic equation $mr^2 + \gamma r + k = 0$ of (5) ([[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-4|Definition §13.4]]); this is why the eigenvalue methods of [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|§31]] reproduce Chapter 3.
>
> *BDP: Example 7.1.1 and Equations (5)–(6)*

^ex-27-2

> [!theorem] Proposition §27.1: An nth-Order Equation as a First-Order System
> Consider the $n$th order equation
>
> $$
> y^{(n)} = F\big(t, y, y', \ldots, y^{(n-1)}\big) . \qquad (7)
> $$
>
> Define
>
> $$
> x_1 = y, \quad x_2 = y', \quad x_3 = y'', \quad \ldots, \quad x_n = y^{(n-1)} . \qquad (8)
> $$
>
> Then $y$ is a solution of (7) if and only if $(x_1, \ldots, x_n)$ is a solution of the system
>
> $$
> x_1' = x_2, \quad x_2' = x_3, \quad \ldots, \quad x_{n-1}' = x_n, \qquad (9)
> $$
>
> $$
> x_n' = F(t, x_1, x_2, \ldots, x_n) . \qquad (10)
> $$
>
> The initial conditions $y(t_0) = y_0, \ldots, y^{(n-1)}(t_0) = y_0^{(n-1)}$ correspond to $x_k(t_0) = y_0^{(k-1)}$, $k = 1, \ldots, n$.
>
> *BDP: 7.1 (text), Equations (7)–(10)*

^prop-27-1

> [!proof]+ Proof
> If $y$ solves (7), define $x_k = y^{(k-1)}$ as in (8). Then $x_k' = y^{(k)} = x_{k+1}$ for $k = 1, \ldots, n - 1$, which is (9), and $x_n' = y^{(n)} = F(t, y, \ldots, y^{(n-1)}) = F(t, x_1, \ldots, x_n)$, which is (10).
>
> Conversely, let $(x_1, \ldots, x_n)$ solve (9)–(10) and put $y = x_1$. By (9), $y' = x_2$, $y'' = x_2' = x_3$, and inductively $y^{(k-1)} = x_k$ for $k \le n$; in particular $y$ is $n$ times differentiable and $y^{(n)} = x_n'$. Then (10) says $y^{(n)} = F(t, y, y', \ldots, y^{(n-1)})$. The statement about initial conditions is (8) at $t = t_0$.

^pf-27-1

*Uses:* none

> [!remark] Remark: Method — Reducing an Equation of Order n to a System
> 1. Solve the equation for the highest derivative: $y^{(n)} = F(t, y, \ldots, y^{(n-1)})$.
> 2. Name the unknown and its first $n - 1$ derivatives: $x_1 = y$, $x_2 = y'$, …, $x_n = y^{(n-1)}$.
> 3. Write the "chain" $x_1' = x_2, \ldots, x_{n-1}' = x_n$, and the last equation $x_n' = F(t, x_1, \ldots, x_n)$.
> 4. Translate the initial conditions: $x_k(t_0) = y^{(k-1)}(t_0)$.
> 5. For a system of higher-order equations (Example §27.1(a)), do the same for each unknown.

^rem-27-1

## Solutions and Initial Value Problems

> [!definition] Definition §27.1: First-Order System; Solution; Initial Value Problem
> A **system of $n$ first-order differential equations** has the form
>
> $$
> x_1' = F_1(t, x_1, x_2, \ldots, x_n), \quad x_2' = F_2(t, x_1, x_2, \ldots, x_n), \quad \ldots, \quad x_n' = F_n(t, x_1, x_2, \ldots, x_n) . \qquad (11)
> $$
>
> A **solution** of (11) on the interval $I: \alpha < t < \beta$ consists of $n$ functions
>
> $$
> x_1 = \phi_1(t), \quad x_2 = \phi_2(t), \quad \ldots, \quad x_n = \phi_n(t), \qquad (12)
> $$
>
> each differentiable at all points of $I$, that satisfy (11) at all points of $I$. Given $n$ **initial conditions**
>
> $$
> x_1(t_0) = x_1^0, \quad x_2(t_0) = x_2^0, \quad \ldots, \quad x_n(t_0) = x_n^0, \qquad (13)
> $$
>
> with $t_0 \in I$ and prescribed numbers $x_1^0, \ldots, x_n^0$, the equations (11) and (13) together form an **initial value problem**.
>
> A solution (12) is a set of parametric equations in $n$-dimensional space: as $t$ runs through $I$, the point $(\phi_1(t), \ldots, \phi_n(t))$ traces a curve, the **trajectory** or path of a particle moving according to (11). The initial conditions fix its starting point. For $n = 2$ the trajectory lies in the $x_1x_2$-plane, where it is easiest to visualize.
>
> *BDP: 7.1 (text), Equations (11)–(13)*

^def-27-1

> [!remark]- Connections
> - A nonlinear system of the form (11) with $n = 2$, and its trajectories in the phase plane: the predator–prey equations [[§62 Predator-Prey Systems#^def-62-1|Calc Def. §62.1]], [[§62 Predator-Prey Systems#^def-62-3|Calc Def. §62.3]] (Stewart's treatment).

> [!theorem] Theorem §27.2: Existence and Uniqueness for First-Order Systems
> Let each of the $n$ functions $F_1, \ldots, F_n$ and the $n^2$ first partial derivatives $\partial F_1/\partial x_1, \ldots, \partial F_1/\partial x_n, \ldots, \partial F_n/\partial x_1, \ldots, \partial F_n/\partial x_n$ be continuous in a region $R$ of $tx_1x_2\cdots x_n$-space defined by $\alpha < t < \beta$, $\alpha_1 < x_1 < \beta_1$, …, $\alpha_n < x_n < \beta_n$, and let the point $(t_0, x_1^0, x_2^0, \ldots, x_n^0)$ be in $R$. Then there is an interval $|t - t_0| < h$ in which there exists a unique solution $x_1 = \phi_1(t), \ldots, x_n = \phi_n(t)$ of the system (11) that also satisfies the initial conditions (13).
>
> *BDP: Theorem 7.1.1*

^thm-27-2

*BDP omits the proof ("it can be constructed by generalizing the argument in Section 2.8"): Picard iteration, as in [[§11 The Existence and Uniqueness Theorem|§11]] (Theorem 2.8.1), with absolute values replaced by a norm on $\mathbb{R}^n$. No subject in the vault proves the $n$-dimensional version.*

> [!remark] Remark: Reading Theorem §27.2
> It is the analogue of Theorem 2.4.2 for a single first-order equation (stated in [[§7 Differences Between Linear and Nonlinear Differential Equations|§7]], proved in [[§11 The Existence and Uniqueness Theorem|§11]]). Note that:
> - nothing is assumed about the partial derivatives of the $F_i$ with respect to $t$;
> - the length $2h$ of the interval of existence is not specified, and it may be very short;
> - the hypotheses are sufficient, not necessary: the same conclusion holds under weaker but more complicated hypotheses.

^rem-27-2

> [!definition] Definition §27.2: Linear and Homogeneous Systems
> The system (11) is **linear** if each $F_i$ is a linear function of the dependent variables $x_1, \ldots, x_n$; otherwise it is **nonlinear**. The most general system of $n$ first-order linear equations is
>
> $$
> \begin{aligned}
> x_1' &= p_{11}(t)x_1 + \cdots + p_{1n}(t)x_n + g_1(t), \\
> x_2' &= p_{21}(t)x_1 + \cdots + p_{2n}(t)x_n + g_2(t), \\
> &\ \ \vdots \\
> x_n' &= p_{n1}(t)x_1 + \cdots + p_{nn}(t)x_n + g_n(t).
> \end{aligned} \qquad (14)
> $$
>
> It is **homogeneous** if $g_1(t), \ldots, g_n(t)$ are all zero on $I$, and **nonhomogeneous** otherwise. In matrix notation ([[§28 Matrices#^def-28-2|§28]], [[§30 Basic Theory of Systems of First-Order Linear Equations#^def-30-1|§30]]) it is $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$.
>
> For example, the systems (1) and (2) of Example §27.1 are linear; (1) is nonhomogeneous unless $F_1(t) = F_2(t) = 0$, and (2) is homogeneous.
>
> *BDP: 7.1 (text), Equation (14)*

^def-27-2

> [!remark]- Connections
> - The constant-coefficient homogeneous case $\mathbf{x}' = A\mathbf{x}$ is Lay's starting point, [[§38 Applications to Differential Equations#^def-38-1|235 Def. §38.1]], solved there for diagonalizable $A$ ([[§38 Applications to Differential Equations#^thm-38-3|235 Thm. §38.3]]).

> [!theorem] Theorem §27.3: Existence and Uniqueness for Linear Systems
> If the functions $p_{11}, p_{12}, \ldots, p_{nn}, g_1, \ldots, g_n$ are continuous on an open interval $I: \alpha < t < \beta$, then there exists a unique solution $x_1 = \phi_1(t), \ldots, x_n = \phi_n(t)$ of the system (14) that also satisfies the initial conditions (13), where $t_0$ is any point in $I$ and $x_1^0, \ldots, x_n^0$ are any prescribed numbers. Moreover, the solution exists throughout the interval $I$.
>
> *BDP: Theorem 7.1.2*

^thm-27-3

*BDP omits the proof. It is the system version of Theorem 2.4.1 ([[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]]) and Theorem 3.2.1 ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]]), which is its special case $n = 2$ through Proposition §27.1; no subject in the vault proves it.*

In contrast with the nonlinear case, for a linear system existence and uniqueness hold on the *whole* interval where the hypotheses hold, and the initial values $x_1^0, \ldots, x_n^0$ at $t = t_0$ are completely arbitrary; in Theorem §27.2 the initial point must lie in the region $R$. The rest of Chapter 7 is about linear systems; nonlinear systems are the subject of BDP's Chapters 8 and 9.

> [!example] Example §27.3: Differences of Solutions of a Nonhomogeneous System
> Let $x = x_1(t)$, $y = y_1(t)$ and $x = x_2(t)$, $y = y_2(t)$ be any two solutions of the linear nonhomogeneous system
>
> $$
> x' = p_{11}(t)x + p_{12}(t)y + g_1(t), \qquad y' = p_{21}(t)x + p_{22}(t)y + g_2(t) .
> $$
>
> Show that $x = x_1(t) - x_2(t)$, $y = y_1(t) - y_2(t)$ is a solution of the corresponding homogeneous system.
>
> Both pairs satisfy the system:
>
> $$
> x_1' = p_{11}x_1 + p_{12}y_1 + g_1, \quad y_1' = p_{21}x_1 + p_{22}y_1 + g_2; \qquad
> x_2' = p_{11}x_2 + p_{12}y_2 + g_1, \quad y_2' = p_{21}x_2 + p_{22}y_2 + g_2 .
> $$
>
> Subtract the equations for the second solution from those for the first. The forcing terms $g_1$, $g_2$ cancel, and since differentiation is linear,
>
> $$
> (x_1 - x_2)' = p_{11}(x_1 - x_2) + p_{12}(y_1 - y_2), \qquad (y_1 - y_2)' = p_{21}(x_1 - x_2) + p_{22}(y_1 - y_2) .
> $$
>
> So $x = x_1 - x_2$, $y = y_1 - y_2$ satisfies $x' = p_{11}x + p_{12}y$, $y' = p_{21}x + p_{22}y$, the homogeneous system. As for a single equation ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-1|Theorem §17.1]], BDP Theorem 3.5.1), every solution of the nonhomogeneous system is therefore one particular solution plus a solution of the homogeneous system.
>
> *BDP: Problem 7.1.13*
> *Source: 331 Written HW 6, Problem 1*

^ex-27-3
