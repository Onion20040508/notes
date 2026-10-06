---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 1
powers: "0.1"
aliases: ["Powers 0.1"]
tags: [fourier-series-and-pdes, math341, extension]
---
↑ [[· 0★ Ordinary Differential Equations Review]] · [[§2★ Nonhomogeneous Linear Equations]] →

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

This is [[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-3|331 Def. §13.3]] in Powers' notation: $u$ for the unknown, $k$ and $p$ for the coefficients, $f$ for the inhomogeneity.

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

*Powers derives (4) by separating variables, $\frac1u\frac{du}{dt} = k(t)$, $\ln|u| = \int k\,dt + C$, $u = \pm e^Ce^{\int k\,dt}$. Proved in ODE: [[§5 Separable Differential Equations#^thm-5-1|331 Thm. §5.1]] (separable equations) and [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|331 Thm. §4.2]] (linear equations, which also shows that $u \equiv 0$, lost by dividing by $u$, belongs to the family with $c = 0$).*

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

*Proved in ODE: [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|331 Thm. §14.2]]. Powers calls it a principle because it holds, with only superficial changes, for many other linear homogeneous equations; it is the starting point of every series solution of a PDE in this subject.*

> [!remark]- Connections
> - Superposition says that $L[u] = u'' + ku' + pu$ is a linear map, so the solutions of (6) form its null space, a subspace: [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]].

> [!definition] Definition §1.2: Linear Independence; Wronskian
> Two solutions $u_1$, $u_2$ are **linearly independent** on an interval if the only linear combination of them with constant coefficients that is identically $0$ on the interval is the one with both coefficients $0$. The **Wronskian** of $u_1$ and $u_2$ is
>
> $$
> W(u_1, u_2) = \begin{vmatrix} u_1(t) & u_2(t) \\ u_1'(t) & u_2'(t) \end{vmatrix} = u_1(t)u_2'(t) - u_2(t)u_1'(t) . \qquad (7)
> $$
>
> *Powers: 0.1 (text), Equation (7)*

^def-1-2

The Wronskian is [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-2|331 Def. §14.2]].

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

*Proved in ODE: [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-3|331 Thm. §14.3]] (solving for $c_1$, $c_2$), [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|331 Thm. §14.4]] (every solution is of this form), and [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|331 Thm. §14.8]] (Abel: the Wronskian of two solutions is either never zero or identically zero, which is why "nonzero at one point" and "nonzero on the interval" agree). The equivalence with linear independence is item 4 of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-14-2|331 Remark: The Solution Space Is a Two-Dimensional Vector Space]].*

The first MAT 341 lecture put the contrast this way: the solutions of the first-order equation (3) form a one-dimensional space, fixed by one initial value; those of (6) a two-dimensional space, fixed by $u(0)$ and $u'(0)$; but the heat equation $u_t = u_{xx}$ has an infinite-dimensional space of solutions ($c_1x + c_2$, $e^{-\lambda^2t}\cos\lambda x$, $e^{-\lambda^2t}\sin\lambda x$ for every $\lambda$, $t^{-1/2}e^{-x^2/4t}$, …), so a partial differential equation is always posed together with boundary and initial conditions.

### Constant Coefficients

The most important second-order linear equation that can be solved in closed form is

$$
\frac{d^2u}{dt^2} + k\frac{du}{dt} + pu = 0 \qquad (k, p \text{ constants}) . \qquad (8)
$$

It always has a solution $u(t) = e^{mt}$ for an appropriate constant $m$: substituting gives $m^2e^{mt} + kme^{mt} + pe^{mt} = 0$, and $e^{mt}$ is never $0$.

> [!definition] Definition §1.3: Characteristic Equation
> The **characteristic equation** of the differential equation (8) is
>
> $$
> m^2 + km + p = 0 . \qquad (9)
> $$
>
> $u = e^{mt}$ solves (8) exactly when $m$ is a root of (9).
>
> *Powers: 0.1, Equation (9)*

^def-1-3

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

*Proved in ODE: [[§16 Repeated Roots; Reduction of Order#^thm-16-2|331 Thm. §16.2]], which collects [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-2|331 Thm. §13.2]] (distinct roots), [[§16 Repeated Roots; Reduction of Order#^thm-16-1|331 Thm. §16.1]] (double root) and [[§15 Complex Roots of the Characteristic Equation#^thm-15-2|331 Thm. §15.2]] (complex roots; the trade (10) → (11) is [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|331 Thm. §14.6]]).*

> [!definition] Definition §1.4: Hyperbolic Sine and Cosine
> The **hyperbolic sine** and **hyperbolic cosine** are
>
> $$
> \sinh(A) = \tfrac12\big(e^A - e^{-A}\big), \qquad \cosh(A) = \tfrac12\big(e^A + e^{-A}\big) . \qquad (16)
> $$
>
> *Powers: 0.1, Equation (16)*

^def-1-4

This is [[§24 Hyperbolic Functions#^def-24-1|Calc Def. §24.1]]; the derivatives $(\sinh A)' = \cosh A$, $(\cosh A)' = \sinh A$ and the identity $\cosh^2 A - \sinh^2 A = 1$ are [[§24 Hyperbolic Functions#^thm-24-2|Calc Thm. §24.2]] and [[§24 Hyperbolic Functions#^thm-24-1|Calc Thm. §24.1]]. For complex arguments the same formulas define [[§39★ Hyperbolic Functions#^def-39-1|342 Def. §39.1]], used in [[§53★ Partial Differential Equations#^lem-53-2|Lemma §53.2]].

> [!example] Example §1.1: The Two Workhorse Equations
> The equations $u'' + \lambda^2u = 0$ and $u'' - \lambda^2u = 0$, with $\lambda$ a constant, arise in nearly every [[§19 Example꞉ Fixed End Temperatures#^def-19-1|separation of variables]] in this subject.
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
> Which form to use depends on the boundary conditions: see [[§4★ Singular Boundary Value Problems#^rem-4-2|Remark: Method — Choosing the Form of the Solution]].
>
> **$\lambda = 0$.** Both equations become $u'' = 0$, with the double root $m = 0$, and the second case gives $u(t) = c_1 + c_2t$. This case must always be checked separately in eigenvalue problems ([[§3★ Boundary Value Problems#^ex-3-5|Example §3.5]]).
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

The same classification, with the physics of the damping coefficient, is [[§19 Mechanical and Electrical Vibrations#^thm-19-3|331 Thm. §19.3]].

### The Cauchy–Euler Equation

One of the few equations with variable coefficients that can be solved in complete generality is the Cauchy–Euler equation. Its distinguishing feature is that the coefficient of the $n$th derivative is the $n$th power of $t$ times a constant. It is not treated in [[Ordinary Differential Equations]], so its solution is proved here.

> [!definition] Definition §1.5: Cauchy–Euler Equation; Its Characteristic Equation
> The **Cauchy–Euler equation** is
>
> $$
> t^2\frac{d^2u}{dt^2} + kt\frac{du}{dt} + pu = 0 \qquad (k, p \text{ constants}) , \qquad (17)
> $$
>
> and its **characteristic equation** is
>
> $$
> m(m - 1) + km + p = 0 . \qquad (18)
> $$
>
> *Powers: 0.1, Equations (17)–(18)*

^def-1-5

> [!theorem] Theorem §1.5: Solutions of the Cauchy–Euler Equation
> For $t > 0$, the general solution of (17) is determined by the roots $m_1$, $m_2$ of (18):
>
> | Roots of the characteristic equation | General solution |
> |---|---|
> | real, distinct: $m_1 \ne m_2$ | $u(t) = c_1t^{m_1} + c_2t^{m_2}$ |
> | real, double: $m_1 = m_2$ | $u(t) = c_1t^{m_1} + c_2(\ln t)t^{m_1}$ |
> | conjugate complex: $m_{1,2} = \alpha \pm i\beta$ | $u(t) = c_1t^\alpha\cos(\beta\ln t) + c_2t^\alpha\sin(\beta\ln t)$ |
>
> *Powers: 0.1, Table 2*

^thm-1-5

> [!proof]+ Proof
> **Powers' argument: $t^m$ is a solution exactly when $m$ solves (18).** Assume $u(t) = t^m$. Then $u' = mt^{m-1}$, $u'' = m(m - 1)t^{m-2}$, and substituting into (17),
>
> $$
> t^2m(m - 1)t^{m-2} + ktmt^{m-1} + pt^m = \big(m(m - 1) + km + p\big)t^m = 0 .
> $$
>
> Since $t^m \ne 0$ for $t > 0$, this holds if and only if $m$ is a root of (18). For distinct real roots this gives the two solutions $t^{m_1}$, $t^{m_2}$, with Wronskian
>
> $$
> W(t^{m_1}, t^{m_2}) = t^{m_1}\,m_2t^{m_2 - 1} - t^{m_2}\,m_1t^{m_1 - 1} = (m_2 - m_1)\,t^{m_1 + m_2 - 1} \ne 0 ,
> $$
>
> so the first row of the table follows from Theorem §1.3.
>
> **All three rows, by the substitution $x = \ln t$.** (Powers states the other two rows without argument; the substitution is his Exercise 0.1.21.) For $t > 0$ put $x = \ln t$ and $u(t) = v(x)$, that is, $v(x) = u(e^x)$. By the chain rule, with $dx/dt = 1/t$,
>
> $$
> \frac{du}{dt} = \frac1t\,v'(x), \qquad \frac{d^2u}{dt^2} = \frac{d}{dt}\Big(\frac1t\,v'(x)\Big) = -\frac{1}{t^2}\,v'(x) + \frac{1}{t^2}\,v''(x) ,
> $$
>
> so $t\,u' = v'$ and $t^2u'' = v'' - v'$. Equation (17) becomes the constant-coefficient equation
>
> $$
> v'' + (k - 1)v' + pv = 0, \qquad -\infty < x < \infty ,
> $$
>
> whose characteristic equation $m^2 + (k - 1)m + p = 0$ is exactly (18), since $m(m - 1) + km = m^2 + (k - 1)m$. Because $t \mapsto \ln t$ is a one-to-one map of $(0, \infty)$ onto $(-\infty, \infty)$, $u$ solves (17) on $t > 0$ if and only if $v$ solves this equation on the whole line. By Theorem §1.4 its general solution is
>
> $$
> v = c_1e^{m_1x} + c_2e^{m_2x}, \qquad v = c_1e^{m_1x} + c_2xe^{m_1x}, \qquad v = c_1e^{\alpha x}\cos(\beta x) + c_2e^{\alpha x}\sin(\beta x)
> $$
>
> in the three cases. Substituting back $x = \ln t$ and $e^{mx} = t^m$ gives exactly the three rows of the table.

^pf-1-5

*Uses:* [[§1★ Homogeneous Linear Equations#^thm-1-3|§1.3]], [[§1★ Homogeneous Linear Equations#^thm-1-4|§1.4]], [[§1★ Homogeneous Linear Equations#^def-1-5|Def. §1.5]]

For $t < 0$ the same formulas hold with $t$ replaced by $|t|$: the substitution $t = -s$ leaves (17) unchanged in form. In this subject the variable is a radius $r > 0$, so this never matters.

> [!example] Example §1.3: Cauchy–Euler Equations in Polar Coordinates
> Separating variables in polar coordinates ([[§39 Potential in a Disk#^thm-39-2|Theorem §39.2]], Powers 4.5) produces Cauchy–Euler equations in the radius $r$. Solve, for $r > 0$ and a constant $\lambda > 0$:
>
> **(a) $r^2u'' + ru' - \lambda^2u = 0$ (19).** Here $k = 1$, $p = -\lambda^2$, and the characteristic equation is $m(m - 1) + m - \lambda^2 = m^2 - \lambda^2 = 0$, with roots $m = \pm\lambda$. The first row of Theorem §1.5 gives
>
> $$
> u(r) = c_1r^\lambda + c_2r^{-\lambda} . \qquad (20)
> $$
>
> **(b) $r^2u'' + ru' + \lambda^2u = 0$.** Now $m^2 + \lambda^2 = 0$, $m = \pm i\lambda$ ($\alpha = 0$, $\beta = \lambda$), and the third row gives
>
> $$
> u(r) = c_1\cos(\lambda\ln r) + c_2\sin(\lambda\ln r) .
> $$
>
> **(c) $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{du}{dr}\Big) = 0$.** Multiplying out, $u'' + \frac1ru' = 0$, that is $r^2u'' + ru' = 0$: the case $\lambda = 0$ of (a). The characteristic equation $m^2 = 0$ has the double root $0$, and the second row gives
>
> $$
> u(r) = c_1 + c_2\ln r .
> $$
>
> (Directly: $ru' = c_2$, so $u' = c_2/r$.) The solutions $r^{-\lambda}$ and $\ln r$ are unbounded as $r \to 0$; in a disk they are excluded by a boundedness condition ([[§4★ Singular Boundary Value Problems#^def-4-2|Definition §4.2]]).
>
> *Powers: 0.1, Equations (19)–(20); Exercises 0.1.10 and 0.1.11*

^ex-1-3

### Singular Points

> [!definition] Definition §1.6: Singular Point; Regular Singular Point
> For the general linear equation
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 ,
> $$
>
> any point where $k(t)$ or $p(t)$ fails to be continuous is a **singular point** of the differential equation. At such a point solutions may break down in various ways. If $t_0$ is a singular point at which both functions
>
> $$
> (t - t_0)k(t) \qquad\text{and}\qquad (t - t_0)^2p(t) \qquad (21)
> $$
>
> have Taylor series expansions about $t_0$, then $t_0$ is a **regular singular point**.
>
> *Powers: 0.1 (text), Equation (21)*

^def-1-6

The Cauchy–Euler equation is the model: in standard form, $u'' + \frac ktu' + \frac p{t^2}u = 0$, so $tk(t) = k$ and $t^2p(t) = p$ are constants, and $t_0 = 0$ is a regular singular point. Its solutions $t^m$, $(\ln t)t^m$ show the typical behavior near such a point, which provides a model for more general equations (Bessel's equation, [[§45★ Bessel's Equation#^def-45-1|Definition §45.1]]; Legendre's equation, [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-2|Definition §49.2]]). Singular points at the ends of an interval are the subject of [[§4★ Singular Boundary Value Problems|§4★]].

> [!remark]- Remark: Solving by a Change of Variables
> Other second-order equations may be solved by power series, by a change of variables to a kind already solved, or by sheer luck. Powers' example is the equation
>
> $$
> t^4\frac{d^2u}{dt^2} + \lambda^2u = 0 , \qquad (22)
> $$
>
> from the theory of beams, with the change of variables $t = 1/z$, $u(t) = \frac1z\,v(z)$. Since $z = 1/t$, $dz/dt = -1/t^2 = -z^2$, and by the chain rule
>
> $$
> \frac{du}{dt} = \frac{d}{dz}\Big(\frac vz\Big)\frac{dz}{dt} = -z^2\,\frac{zv' - v}{z^2} = -zv' + v, \qquad
> \frac{d^2u}{dt^2} = \frac{d}{dz}(-zv' + v)\,(-z^2) = -z^2(-zv'' - v' + v') = z^3v'' .
> $$
>
> Substituting, $\big(\frac1z\big)^4z^3v'' + \lambda^2\frac vz = 0$, that is $\frac1z(v'' + \lambda^2v) = 0$, so $v'' + \lambda^2v = 0$ and $v = c_1\cos(\lambda z) + c_2\sin(\lambda z)$. Reversing the change of variables,
>
> $$
> u(t) = t\big(c_1\cos(\lambda/t) + c_2\sin(\lambda/t)\big) . \qquad (23)
> $$

^rem-1-1

## A Second Independent Solution

It is not generally possible to solve a second-order linear homogeneous equation with variable coefficients, but a second independent solution can always be found if one solution is known.

> [!theorem] Theorem §1.6: Reduction of Order
> Suppose $u_1(t)$ is a solution of
>
> $$
> \frac{d^2u}{dt^2} + k(t)\frac{du}{dt} + p(t)u = 0 . \qquad (24)
> $$
>
> Then $u_2(t) = v(t)u_1(t)$ is a solution if and only if
>
> $$
> u_1v'' + \big(2u_1' + k(t)u_1\big)v' = 0 , \qquad (25)
> $$
>
> a first-order linear equation for $v'$. A nonconstant solution $v$ (needed for $u_2$ to be independent of $u_1$) can therefore be found, at least in terms of integrals.
>
> *Powers: 0.1 (text), Equation (25)*

^thm-1-6

*Powers substitutes $u_2 = vu_1$: $v''u_1 + 2v'u_1' + vu_1'' + k(v'u_1 + vu_1') + pvu_1 = 0$, and the coefficient $u_1'' + ku_1' + pu_1$ of $v$ is zero. Proved in ODE: [[§16 Repeated Roots; Reduction of Order#^prop-16-3|331 Prop. §16.3]].*

> [!example] Example §1.4: Reduction of Order for a Legendre Equation
> The equation
>
> $$
> (1 - t^2)u'' - 2tu' + 2u = 0, \qquad -1 < t < 1 ,
> $$
>
> has the solution $u_1(t) = t$ (check: $0 - 2t + 2t = 0$). Find a second.
>
> **Substitute** $u_2 = v\cdot t$, so $u_2' = v't + v$, $u_2'' = v''t + 2v'$:
>
> $$
> (1 - t^2)(v''t + 2v') - 2t(v't + v) + 2vt = 0 , \qquad\text{that is}\qquad (1 - t^2)tv'' + (2 - 4t^2)v' = 0 .
> $$
>
> **Solve for $v'$.** Separating, with partial fractions,
>
> $$
> \frac{v''}{v'} = \frac{4t^2 - 2}{t(1 - t^2)} = -\frac2t + \frac{1}{1 - t} - \frac{1}{1 + t} ,
> $$
>
> so $\ln v' = -2\ln t - \ln(1 - t) - \ln(1 + t)$ (on $0 < t < 1$; any constant can be dropped), and
>
> $$
> v' = \frac{1}{t^2(1 - t^2)} = \frac{1}{t^2} + \frac{1/2}{1 - t} + \frac{1/2}{1 + t}, \qquad v = -\frac1t + \frac12\ln\Big|\frac{1 + t}{1 - t}\Big| .
> $$
>
> **The second solution** is
>
> $$
> u_2(t) = t\,v(t) = -1 + \frac t2\ln\frac{1 + t}{1 - t}, \qquad -1 < t < 1 ,
> $$
>
> which is defined and solves the equation on the whole interval (direct substitution checks it). Its Wronskian with $u_1$ is $W(t, u_2) = tu_2' - u_2 = \frac{1}{1 - t^2} \ne 0$, so $u_1$, $u_2$ are independent.
>
> The equation is Legendre's equation $(1 - t^2)u'' - 2tu' + n(n + 1)u = 0$ with $n = 1$ ([[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-2|Definition §49.2]] with $\mu^2 = 2$, Powers 5.9). The polynomial solution $u_1 = t$ is bounded on $[-1, 1]$, while $u_2$ is unbounded as $t \to \pm1$, the regular singular points of the equation.
>
> *Powers: 0.1, Example (reduction of order)*

^ex-1-4

## Higher-Order Equations

Linear homogeneous equations of order higher than two, especially order four, occur frequently in elasticity and fluid mechanics. They are not treated in [[Ordinary Differential Equations]] (which covered only the second-order case and first-order systems).

> [!definition] Definition §1.7: nth-Order Linear Homogeneous Equation; Characteristic Equation
> A general $n$th-order homogeneous linear equation is
>
> $$
> u^{(n)} + k_1(t)u^{(n-1)} + \cdots + k_{n-1}(t)u^{(1)} + k_n(t)u = 0 , \qquad (26)
> $$
>
> with given coefficient functions $k_1(t), \ldots, k_n(t)$. With constant coefficients it reads
>
> $$
> u^{(n)} + k_1u^{(n-1)} + \cdots + k_{n-1}u^{(1)} + k_nu = 0 , \qquad (27)
> $$
>
> and substituting $u = e^{mt}$ and dividing by $e^{mt}$ gives its **characteristic equation**
>
> $$
> m^n + k_1m^{n-1} + \cdots + k_{n-1}m + k_n = 0 . \qquad (28)
> $$
>
> *Powers: 0.1, Equations (26)–(28)*

^def-1-7

> [!theorem] Theorem §1.7: General Solution of the nth-Order Equation
> The Principle of Superposition holds for (26), and its general solution is a linear combination of $n$ independent solutions $u_1(t), \ldots, u_n(t)$ with arbitrary constant coefficients:
>
> $$
> u(t) = c_1u_1(t) + c_2u_2(t) + \cdots + c_nu_n(t) .
> $$
>
> *Powers: 0.1 (text)*

^thm-1-7

*Powers omits the proof. Writing $x_1 = u, x_2 = u', \ldots, x_n = u^{(n-1)}$ turns (26) into a first-order linear system ([[§27 Introduction to Systems of First-Order Linear Equations#^prop-27-1|331 Prop. §27.1]]), for which superposition and the statement are [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-1|331 Thm. §30.1]] and [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]].*

> [!theorem] Theorem §1.8: Solutions of the Constant-Coefficient nth-Order Equation
> Each distinct root of the characteristic equation (28) contributes as many independent solutions of (27) as its multiplicity; complex roots occur in conjugate pairs (the coefficients being real) and are written with real functions:
>
> | Root | Multiplicity | Contribution |
> |---|---|---|
> | $m$ real | $1$ | $ce^{mt}$ |
> | $m$ real | $k$ | $(c_1 + c_2t + \cdots + c_kt^{k-1})e^{mt}$ |
> | $m, \bar m = \alpha \pm i\beta$ | $1$ | $\big(a\cos(\beta t) + b\sin(\beta t)\big)e^{\alpha t}$ |
> | $m, \bar m = \alpha \pm i\beta$ | $k$ | $(a_1 + a_2t + \cdots + a_kt^{k-1})\cos(\beta t)e^{\alpha t} + (b_1 + b_2t + \cdots + b_kt^{k-1})\sin(\beta t)e^{\alpha t}$ |
>
> Since the multiplicities add up to $n$, the contributions together contain $n$ terms, and their sum is the general solution of (27).
>
> *Powers: 0.1, Table 3*

^thm-1-8

*Powers omits the proof ("can be shown to be the general solution"). The case $n = 2$ is [[§16 Repeated Roots; Reduction of Order#^thm-16-2|331 Thm. §16.2]]; the remark below shows why the listed functions are solutions.*

> [!remark]- Remark: Why It Works
> Let $L[u] = u^{(n)} + k_1u^{(n-1)} + \cdots + k_nu$ and let $P(m) = m^n + k_1m^{n-1} + \cdots + k_n$ be the characteristic polynomial. Since $\frac{d^j}{dt^j}e^{mt} = m^je^{mt}$,
>
> $$
> L[e^{mt}] = P(m)\,e^{mt} \qquad\text{for every (complex) } m .
> $$
>
> Differentiate this identity $j$ times with respect to $m$. On the left, $\partial^j_m e^{mt} = t^je^{mt}$, and $\partial_m$ commutes with the $t$-derivatives in $L$ (the function $e^{mt}$ is smooth in both variables). On the right, the Leibniz product rule gives
>
> $$
> L[t^je^{mt}] = \sum_{i=0}^{j}\binom ji P^{(i)}(m)\,t^{j-i}e^{mt} .
> $$
>
> If $m$ is a root of multiplicity $k$, then $P(m) = P'(m) = \cdots = P^{(k-1)}(m) = 0$, so for $j = 0, 1, \ldots, k - 1$ every term vanishes: $e^{mt}, te^{mt}, \ldots, t^{k-1}e^{mt}$ are solutions. For a complex root, the real and imaginary parts of $t^je^{(\alpha + i\beta)t}$ are solutions because the coefficients are real ([[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-5|331 Thm. §30.5]]). That the $n$ functions so obtained are independent is the part that needs more work.

^rem-1-2

> [!example] Example §1.5: Two Fourth-Order Equations
> **(a)** Find the general solution of $u^{(4)} + 3u^{(2)} - 4u = 0$.
>
> The characteristic equation $m^4 + 3m^2 - 4 = 0$ is a quadratic in $m^2$: $(m^2 + 4)(m^2 - 1) = 0$, so $m^2 = -4$ or $1$, and the roots are $m = \pm2i, \pm1$, all simple. By Theorem §1.8 the pair $\pm2i$ ($\alpha = 0$, $\beta = 2$) contributes $a\cos(2t) + b\sin(2t)$, and $m = 1$, $m = -1$ contribute $e^t$, $e^{-t}$:
>
> $$
> u(t) = a\cos(2t) + b\sin(2t) + c_1e^t + c_2e^{-t} .
> $$
>
> **(b)** Find the general solution of $u^{(4)} - 2u^{(2)} + u = 0$.
>
> The characteristic equation $m^4 - 2m^2 + 1 = (m^2 - 1)^2 = (m - 1)^2(m + 1)^2 = 0$ has the roots $\pm1$, each of multiplicity $2$. Each contributes a first-degree polynomial times an exponential:
>
> $$
> u(t) = (c_1 + c_2t)e^t + (c_3 + c_4t)e^{-t} .
> $$
>
> With $e^{\pm t} = \cosh t \pm \sinh t$ the terms can be regrouped into the equivalent form
>
> $$
> u(t) = (C_1 + C_2t)\cosh(t) + (C_3 + C_4t)\sinh(t) ,
> $$
>
> where $C_1 = c_1 + c_3$, $C_2 = c_2 + c_4$, $C_3 = c_1 - c_3$, $C_4 = c_2 - c_4$.
>
> *Powers: 0.1, Examples (fourth-order equations)*

^ex-1-5

> [!remark] Remark: Some Important Equations and Their Solutions
> Powers boxes the four equations that recur throughout the book:
> 1. $\dfrac{du}{dt} = ku$ ($k$ constant): $u(t) = ce^{kt}$ (Theorem §1.1).
> 2. $\dfrac{d^2u}{dt^2} + \lambda^2u = 0$: $u(t) = a\cos(\lambda t) + b\sin(\lambda t)$ (Example §1.1).
> 3. $\dfrac{d^2u}{dt^2} - \lambda^2u = 0$: $u(t) = a\cosh(\lambda t) + b\sinh(\lambda t)$, or $u(t) = c_1e^{\lambda t} + c_2e^{-\lambda t}$ (Example §1.1).
> 4. $t^2u'' + tu' - \lambda^2u = 0$: $u(t) = c_1t^\lambda + c_2t^{-\lambda}$ (Example §1.3).

^rem-1-3
