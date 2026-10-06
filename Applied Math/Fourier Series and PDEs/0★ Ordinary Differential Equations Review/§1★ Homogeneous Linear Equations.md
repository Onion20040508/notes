---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: "1★"
powers: "0.1"
aliases: ["Powers 0.1"]
tags: [fourier-series-and-pdes, math341, extension]
---
↑ [[· 0★ Ordinary Differential Equations Review]] · [[§2★ Variable Coefficients and Higher-Order Equations]] →

*Powers, Section 0.1 · MAT 341 lecture 8.27 · HW 1.*
★ *Beyond MAT 341: the course only reviewed parts of this section (lecture 8.27, HW 1 Q1); it is included in full from Powers.*

Separation of variables turns every partial differential equation in this subject into ordinary differential equations, almost always linear, homogeneous and of first or second order. This section collects the ones that will be needed: $u' = ku$, the constant-coefficient equations, above all $u'' + \lambda^2u = 0$ and $u'' - \lambda^2u = 0$, and the Cauchy–Euler equation $t^2u'' + ktu' + pu = 0$, which reappears in polar and spherical coordinates. The general theory (superposition, the Wronskian, reduction of order) is developed and proved in [[Ordinary Differential Equations]], and each item below links to its home there; the Cauchy–Euler equation and equations of order higher than two are not treated there and are worked out here.

## First-Order Equations

> [!definition] Definition §1.1: Linear Equations of First and Second Order; Homogeneous
> The linear differential equations of first and second order are
>
> $$
> \frac{du}{dt} = k(t)u + f(t), \qquad (1)
> $$
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = f(t) . \qquad (2)
> $$
>
> Either equation is **homogeneous** if $f(t)$ is $0$. Equivalently, the equation is homogeneous if the constant function $u(t) \equiv 0$ is a solution.
>
> *Powers: 0.1 (text)*

^def-1-1

This is [[§17 Homogeneous Differential Equations with Constant Coefficients#^def-17-3|331 Def. §17.3]] in Powers' notation: $u$ for the unknown, $k$ and $p$ for the coefficients, $f$ for the inhomogeneity.

> [!theorem] Theorem §1.1: The First-Order Homogeneous Equation
> The general solution of
>
> $$
> \frac{du}{dt} = k(t)u \qquad (3)
> $$
>
> is
>
> $$
> u(t) = c\,e^{\int k(t)\,dt} , \qquad (4)
> $$
>
> with $c$ an arbitrary constant, which can be used to satisfy an initial condition. In the most common case $k(t) = k$ is constant:
>
> $$
> \frac{du}{dt} = ku, \qquad u(t) = ce^{kt} . \qquad (5)
> $$
>
> If $k < 0$, $u(t) \to 0$ as $t$ increases; if $k > 0$, $|u(t)|$ grows rapidly, which in physical problems usually signals that something cannot go on indefinitely.
>
> *Powers: 0.1, Equations (3)–(5)*

^thm-1-1

*Powers derives (4) by separating variables, $\frac1u\frac{du}{dt} = k(t)$, $\ln|u| = \int k\,dt + C$, $u = \pm e^Ce^{\int k\,dt}$. Proved in ODE: [[§6 Separable Differential Equations#^thm-6-1|331 Thm. §6.1]] (separable equations) and [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-2|331 Thm. §5.2]] (linear equations, which also shows that $u \equiv 0$, lost by dividing by $u$, belongs to the family with $c = 0$).*

For example, $du/dt = -tu$ has the general solution $u(t) = ce^{-t^2/2}$, and the initial condition $u(0) = 5$ forces $c = 5$ (Powers' example). MAT 341's HW 1, Problem 1(a), asked for $du/dt = tu$: the same steps give $u(t) = ce^{t^2/2}$.

## Second-Order Equations

There is no solution method for the general second-order linear homogeneous equation

$$
\frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 , \qquad (6)
$$

but its solutions have a simple structure.

> [!theorem] Theorem §1.2: Principle of Superposition
> If $u_1(t)$ and $u_2(t)$ are solutions of the same linear homogeneous equation (6), then so is any linear combination of them: $u(t) = c_1u_1(t) + c_2u_2(t)$.
>
> *Powers: 0.1, Principle of Superposition*

^thm-1-2

*Proved in ODE: [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-2|331 Thm. §18.2]]. Powers calls it a principle because it holds, with only superficial changes, for many other linear homogeneous equations; it is the starting point of every series solution of a PDE in this subject.*

> [!remark]- Connections
> - Superposition says that $L[u] = u'' + ku' + pu$ is a linear map, so the solutions of (6) form its null space, a subspace: [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]], [[§30 Null Spaces, Column Spaces, and Linear Transformations#^thm-30-5|235 Thm. §30.5]].

> [!definition] Definition §1.3: Linear Independence
> Two solutions $u_1$, $u_2$ are **linearly independent** on an interval if the only linear combination of them with constant coefficients that is identically $0$ on the interval is the one with both coefficients $0$.
>
> *Powers: 0.1 (text), Equation (7)*

^def-1-2

> [!definition] Definition §1.4: Wronskian
> The **Wronskian** of two solutions $u_1$ and $u_2$ is
>
> $$
> W(u_1, u_2) = \begin{vmatrix} u_1(t) & u_2(t) \\ u_1'(t) & u_2'(t) \end{vmatrix} = u_1(t)u_2'(t) - u_2(t)u_1'(t) . \qquad (7)
> $$
>
> *Powers: 0.1 (text), Equation (7)*

^def-1-3

The Wronskian is [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^def-18-2|331 Def. §18.2]].

> [!theorem] Theorem §1.3: The Wronskian Test and the General Solution
> Two solutions of the same linear homogeneous equation (6) are independent on an interval if and only if their Wronskian is nonzero on that interval. If $u_1(t)$, $u_2(t)$ are independent solutions, then
>
> $$
> u(t) = c_1u_1(t) + c_2u_2(t)
> $$
>
> is a **general solution** of (6): given any initial conditions, $c_1$ and $c_2$ can be chosen so that $u$ satisfies them. To satisfy an unrestricted initial condition, two independent solutions are needed.
>
> *Powers: 0.1 (text)*

^thm-1-3

*Proved in ODE: [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-3|331 Thm. §18.3]] (solving for $c_1$, $c_2$), [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|331 Thm. §18.4]] (every solution is of this form), and [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-8|331 Thm. §18.8]] (Abel: the Wronskian of two solutions is either never zero or identically zero, which is why "nonzero at one point" and "nonzero on the interval" agree). The equivalence with linear independence is item 4 of [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-18-2|331 Remark: The Solution Space Is a Two-Dimensional Vector Space]].*

The first MAT 341 lecture put the contrast this way: the solutions of the first-order equation (3) form a one-dimensional space, fixed by one initial value; those of (6) a two-dimensional space, fixed by $u(0)$ and $u'(0)$; but the heat equation $u_t = u_{xx}$ has an infinite-dimensional space of solutions ($c_1x + c_2$, $e^{-\lambda^2t}\cos\lambda x$, $e^{-\lambda^2t}\sin\lambda x$ for every $\lambda$, $t^{-1/2}e^{-x^2/4t}$, …), so a partial differential equation is always posed together with boundary and initial conditions.

### Constant Coefficients

The most important second-order linear equation that can be solved in closed form is

$$
\frac{d^2u}{dt^2} + k\frac{du}{dt} + pu = 0 \qquad (k, p \text{ constants}) . \qquad (8)
$$

It always has a solution $u(t) = e^{mt}$ for an appropriate constant $m$: substituting gives $m^2e^{mt} + kme^{mt} + pe^{mt} = 0$, and $e^{mt}$ is never $0$.

> [!definition] Definition §1.5: Characteristic Equation
> The **characteristic equation** of the differential equation (8) is
>
> $$
> m^2 + km + p = 0 . \qquad (9)
> $$
>
> $u = e^{mt}$ solves (8) exactly when $m$ is a root of (9).
>
> *Powers: 0.1, Equation (9)*

^def-1-4

> [!theorem] Theorem §1.4: Solutions of the Constant-Coefficient Equation
> The general solution of $u'' + ku' + pu = 0$ is determined by the roots $m_1$, $m_2$ of the characteristic equation (9):
>
> | Roots of the characteristic equation | General solution |
> |---|---|
> | real, distinct: $m_1 \ne m_2$ | $u(t) = c_1e^{m_1t} + c_2e^{m_2t}$ |
> | real, double: $m_1 = m_2$ | $u(t) = c_1e^{m_1t} + c_2te^{m_1t}$ |
> | conjugate complex: $m_{1,2} = \alpha \pm i\beta$ | $u(t) = c_1e^{\alpha t}\cos(\beta t) + c_2e^{\alpha t}\sin(\beta t)$ |
>
> In the complex case, the pair of complex solutions
>
> $$
> e^{\alpha t}e^{i\beta t}, \qquad e^{\alpha t}e^{-i\beta t} \qquad (10)
> $$
>
> is traded for the pair of real solutions
>
> $$
> e^{\alpha t}\cos(\beta t), \qquad e^{\alpha t}\sin(\beta t) . \qquad (11)
> $$
>
> *Powers: 0.1, Table 1; Equations (10)–(11)*

^thm-1-4

*Proved in ODE: [[§20 Repeated Roots; Reduction of Order#^thm-20-2|331 Thm. §20.2]], which collects [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|331 Thm. §17.2]] (distinct roots), [[§20 Repeated Roots; Reduction of Order#^thm-20-1|331 Thm. §20.1]] (double root) and [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|331 Thm. §19.2]] (complex roots; the trade (10) → (11) is [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-6|331 Thm. §18.6]]).*

> [!definition] Definition §2.2: Hyperbolic Sine and Cosine
> The **hyperbolic sine** and **hyperbolic cosine** are
>
> $$
> \sinh(A) = \tfrac12\big(e^A - e^{-A}\big), \qquad \cosh(A) = \tfrac12\big(e^A + e^{-A}\big) . \qquad (16)
> $$
>
> *Powers: 0.1, Equation (16)*

^def-1-5

This is [[§27 Hyperbolic Functions#^def-27-1|Calc Def. §27.1]]; the derivatives $(\sinh A)' = \cosh A$, $(\cosh A)' = \sinh A$ and the identity $\cosh^2 A - \sinh^2 A = 1$ are [[§27 Hyperbolic Functions#^thm-27-2|Calc Thm. §27.2]] and [[§27 Hyperbolic Functions#^thm-27-1|Calc Thm. §27.1]]. For complex arguments the same formulas define [[§39★ Hyperbolic Functions#^def-39-1|342 Def. §39.1]], used in [[§66★ Partial Differential Equations#^lem-66-2|Lemma §66.2]].

> [!example] Example §1.1: The Two Workhorse Equations
> The equations $u'' + \lambda^2u = 0$ and $u'' - \lambda^2u = 0$, with $\lambda$ a constant, arise in nearly every [[§25 Example꞉ Fixed End Temperatures#^def-25-2|separation of variables]] in this subject.
>
> **$u'' + \lambda^2u = 0$ (12).** The characteristic equation $m^2 + \lambda^2 = 0$ has roots $m = \pm i\lambda$. If $\lambda \ne 0$, the third case of Theorem §1.4 applies with $\alpha = 0$, $\beta = \lambda$:
>
> $$
> u(t) = c_1\cos(\lambda t) + c_2\sin(\lambda t) . \qquad (13)
> $$
>
> **$u'' - \lambda^2u = 0$ (14).** The characteristic equation $m^2 - \lambda^2 = 0$ has roots $m = \pm\lambda$. If $\lambda \ne 0$, the first case applies:
>
> $$
> u(t) = c_1e^{\lambda t} + c_2e^{-\lambda t} . \qquad (15)
> $$
>
> By (16), $\sinh(\lambda t)$ and $\cosh(\lambda t)$ are linear combinations of $e^{\lambda t}$ and $e^{-\lambda t}$, so by the Principle of Superposition (Theorem §1.2) they are solutions too. Their Wronskian is
>
> $$
> W(\cosh\lambda t, \sinh\lambda t) = \cosh(\lambda t)\cdot\lambda\cosh(\lambda t) - \sinh(\lambda t)\cdot\lambda\sinh(\lambda t) = \lambda \ne 0 ,
> $$
>
> so they are independent (Theorem §1.3), and the general solution may equally well be written
>
> $$
> u(t) = c_1'\cosh(\lambda t) + c_2'\sinh(\lambda t) .
> $$
>
> Which form to use depends on the boundary conditions: see [[§6★ Singular Boundary Value Problems#^rem-6-2|Remark: Method — Choosing the Form of the Solution]].
>
> **$\lambda = 0$.** Both equations become $u'' = 0$, with the double root $m = 0$, and the second case gives $u(t) = c_1 + c_2t$. This case must always be checked separately in eigenvalue problems ([[§5★ Boundary Value Problems#^ex-5-5|Example §5.5]]).
>
> *Powers: 0.1, Equations (12)–(16)*

^ex-1-1

> [!example] Example §1.2: The Mass–Spring–Damper System
> The displacement of a mass in a mass–spring–damper system is described by the initial value problem
>
> $$
> \frac{d^2u}{dt^2} + b\frac{du}{dt} + \omega^2u = 0, \qquad u(0) = u_0, \quad \frac{du}{dt}(0) = v_0 ,
> $$
>
> derived from Newton's second law; $b \ge 0$ and $\omega^2$ are proportional to characteristic constants of the damper and the spring. The characteristic equation $m^2 + bm + \omega^2 = 0$ has the roots
>
> $$
> m = \frac{-b \pm \sqrt{b^2 - 4\omega^2}}{2} = -\frac b2 \pm \sqrt{\Big(\frac b2\Big)^2 - \omega^2} ,
> $$
>
> so the motion is decided by comparing $b/2$ with $\omega$.
> - **$b = 0$: undamped.** The roots are $\pm i\omega$, and $u(t) = c_1\cos(\omega t) + c_2\sin(\omega t)$. The mass oscillates forever.
> - **$0 < b/2 < \omega$: underdamped.** The roots are $\alpha \pm i\beta$ with $\alpha = -b/2$, $\beta = \sqrt{\omega^2 - (b/2)^2}$, and $u(t) = e^{-bt/2}\big(c_1\cos(\beta t) + c_2\sin(\beta t)\big)$. The mass oscillates, but approaches equilibrium as $t$ increases.
> - **$b/2 = \omega$: critically damped.** The double root is $-b/2$, and $u(t) = e^{-bt/2}(c_1 + c_2t)$. The mass approaches equilibrium and passes through it ($u$ changes sign) at most once, since $c_1 + c_2t$ has at most one zero.
> - **$b/2 > \omega$: overdamped.** Both roots $m_1$, $m_2$ are real, and negative because $\sqrt{(b/2)^2 - \omega^2} < b/2$; $u(t) = c_1e^{m_1t} + c_2e^{m_2t}$. The mass approaches equilibrium and $u$ changes sign at most once, since $c_1e^{m_1t} + c_2e^{m_2t} = 0$ means $e^{(m_1 - m_2)t} = -c_2/c_1$, which has at most one solution.
>
> In each case $c_1$, $c_2$ are fixed by $u_0$ and $v_0$. (Powers writes the double root as $b/2$; it is $-b/2$, as the solution formula shows.)
>
> *Powers: 0.1, Example (Mass–Spring–Damper System)*

^ex-1-2

The same classification, with the physics of the damping coefficient, is [[§23 Mechanical and Electrical Vibrations#^thm-23-3|331 Thm. §23.3]].

*Continued in [[§2★ Variable Coefficients and Higher-Order Equations]]: the Cauchy–Euler equation, singular points, reduction of order and equations of higher order.*
