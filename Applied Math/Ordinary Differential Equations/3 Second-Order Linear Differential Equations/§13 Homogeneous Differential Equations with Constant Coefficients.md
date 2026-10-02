---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 13
bdp: "3.1"
aliases: ["BDP 3.1"]
tags: [ordinary-differential-equations, math331]
---
← [[§12★ First-Order Difference Equations]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§14 Solutions of Linear Homogeneous Equations; the Wronskian]] →

*Boyce–DiPrima, Section 3.1 · MATH 331 Written HW 3, Midterm (Spring 2020).*

A second-order equation is linear when it has the form $y'' + p(t)y' + q(t)y = g(t)$, and it needs two initial conditions, a value and a slope. This section solves the simplest case, the homogeneous equation $ay'' + by' + cy = 0$ with constant coefficients. Trying $y = e^{rt}$ turns the differential equation into the quadratic characteristic equation $ar^2 + br + c = 0$. When its roots $r_1 \ne r_2$ are real, every combination $c_1e^{r_1t} + c_2e^{r_2t}$ is a solution, and the two constants can always be fitted to any initial conditions. Complex and repeated roots follow in [[§15 Complex Roots of the Characteristic Equation|§15]] and [[§16 Repeated Roots; Reduction of Order|§16]]. The theory behind the words "general solution" is in [[§14 Solutions of Linear Homogeneous Equations; the Wronskian|§14]].

## Linear Second-Order Equations

> [!definition] Definition §13.1: Linear Second-Order Equation
> A second-order ordinary differential equation has the form
>
> $$
> \frac{d^2y}{dt^2} = f\Big(t, y, \frac{dy}{dt}\Big), \qquad (1)
> $$
>
> where $f$ is a given function. It is **linear** if $f$ is linear in $y$ and $dy/dt$:
>
> $$
> f\Big(t, y, \frac{dy}{dt}\Big) = g(t) - p(t)\frac{dy}{dt} - q(t)y , \qquad (2)
> $$
>
> with $g$, $p$, $q$ functions of $t$ alone. The equation is then written
>
> $$
> y'' + p(t)y' + q(t)y = g(t) , \qquad (3)
> $$
>
> or, more generally, as
>
> $$
> P(t)y'' + Q(t)y' + R(t)y = G(t) . \qquad (4)
> $$
>
> Where $P(t) \ne 0$, dividing (4) by $P(t)$ gives (3) with
>
> $$
> p(t) = \frac{Q(t)}{P(t)}, \qquad q(t) = \frac{R(t)}{P(t)}, \qquad g(t) = \frac{G(t)}{P(t)} . \qquad (5)
> $$
>
> Equation (3) is studied on intervals where $p$, $q$ and $g$ are continuous. An equation (1) that is not of the form (3) or (4) is **nonlinear**.
>
> *BDP: 3.1 (text)*

^def-13-1

> [!definition] Definition §13.2: Initial Value Problem
> An **initial value problem** for a second-order equation consists of the differential equation, (1), (3) or (4), together with a pair of **initial conditions**
>
> $$
> y(t_0) = y_0, \qquad y'(t_0) = y_0' , \qquad (6)
> $$
>
> where $y_0$ and $y_0'$ are given numbers. The conditions prescribe a point $(t_0, y_0)$ on the graph of the solution and the slope $y_0'$ of the graph there. Two conditions are expected because, roughly speaking, solving a second-order equation takes two integrations, each introducing an arbitrary constant.
>
> *BDP: 3.1 (text)*

^def-13-2

> [!definition] Definition §13.3: Homogeneous and Nonhomogeneous Equations
> The linear equation (3) or (4) is **homogeneous** if $g(t)$, respectively $G(t)$, is zero for all $t$, and **nonhomogeneous** otherwise. The nonhomogeneous term is also called the **forcing function**, since in applications it often describes an externally applied force. A homogeneous equation is written
>
> $$
> P(t)y'' + Q(t)y' + R(t)y = 0 . \qquad (7)
> $$
>
> When $P$, $Q$ and $R$ are constants it becomes the **equation with constant coefficients**
>
> $$
> ay'' + by' + cy = 0 , \qquad (8)
> $$
>
> with given real constants $a \ne 0$, $b$, $c$.
>
> *BDP: 3.1 (text)*

^def-13-3

The homogeneous equation is the fundamental one: once it is solved, the nonhomogeneous equation can always be solved, or at least its solution expressed by an integral ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients|§17]] and [[§18★ Variation of Parameters|§18★]]). Equation (8) can always be solved with elementary functions. With variable coefficients (7) is much harder; BDP treats it in Chapter 5 (series solutions), which MATH 331 did not cover.

> [!example] Example §13.1: A First Example
> Solve $y'' - y = 0$, and find the solution with $y(0) = 2$, $y'(0) = -1$.
>
> This is (8) with $a = 1$, $b = 0$, $c = -1$: we want functions equal to their own second derivative. Two come to mind, $y_1(t) = e^t$ and $y_2(t) = e^{-t}$. Constant multiples of them are solutions too, and so is any sum
>
> $$
> y = c_1y_1(t) + c_2y_2(t) = c_1e^t + c_2e^{-t} , \qquad (11)
> $$
>
> since $y' = c_1e^t - c_2e^{-t}$ and $y'' = c_1e^t + c_2e^{-t} = y$. This is a two-parameter family of solutions. To pass through $(0, 2)$ we need $y(0) = c_1 + c_2 = 2$, and to have slope $-1$ there, $y'(0) = c_1 - c_2 = -1$. Adding and subtracting the two equations gives $c_1 = \frac12$ and $c_2 = \frac32$, so
>
> $$
> y = \tfrac12e^t + \tfrac32e^{-t} .
> $$
>
> Two lessons carry over to every equation (8): look for exponential solutions, and fit a linear combination of two of them to the initial conditions.
>
> *BDP: Example 3.1.1*

^ex-13-1

## The Characteristic Equation

> [!definition] Definition §13.4: Characteristic Equation
> The **characteristic equation** of $ay'' + by' + cy = 0$ is the quadratic equation
>
> $$
> ar^2 + br + c = 0 . \qquad (17)
> $$
>
> Since $a$, $b$, $c$ are real, its two roots are real and different, complex conjugates, or real and equal, according as the discriminant $b^2 - 4ac$ is positive, negative or zero.
>
> *BDP: 3.1, Equation (17)*

^def-13-4

> [!theorem] Theorem §13.1: Exponential Solutions
> The function $y = e^{rt}$ is a solution of $ay'' + by' + cy = 0$ if and only if $r$ is a root of the characteristic equation $ar^2 + br + c = 0$.
>
> *BDP: 3.1 (text)*

^thm-13-1

> [!proof]+ Proof
> For $y = e^{rt}$ we have $y' = re^{rt}$ and $y'' = r^2e^{rt}$, so
>
> $$
> ay'' + by' + cy = (ar^2 + br + c)e^{rt} .
> $$
>
> Since $e^{rt} \ne 0$ for every $t$, the right side vanishes identically exactly when $ar^2 + br + c = 0$.

^pf-13-1

*Uses:* [[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-4|Def. §13.4]]

> [!remark]- Connections
> - The same substitution for systems: trying $\mathbf{x} = \mathbf{v}e^{\lambda t}$ in $\mathbf{x}' = A\mathbf{x}$ turns the differential equation into the eigenvalue problem $A\mathbf{v} = \lambda\mathbf{v}$, [[§38 Applications to Differential Equations#^thm-38-2|235 Thm. §38.2]]. In this subject that is [[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-1|Theorem §31.1]] (BDP 7.5), and the second-order equation becomes such a system by [[§27 Introduction to Systems of First-Order Linear Equations#^prop-27-1|Proposition §27.1]] (BDP 7.1).

## Distinct Real Roots

> [!theorem] Theorem §13.2: Distinct Real Roots
> Let the characteristic equation $ar^2 + br + c = 0$ have real roots $r_1 \ne r_2$. Then
>
> $$
> y = c_1y_1(t) + c_2y_2(t) = c_1e^{r_1t} + c_2e^{r_2t} \qquad (18)
> $$
>
> is a solution of $ay'' + by' + cy = 0$ for all constants $c_1$, $c_2$. For any $t_0$, $y_0$, $y_0'$ there is exactly one choice of the constants for which (18) also satisfies $y(t_0) = y_0$, $y'(t_0) = y_0'$, namely
>
> $$
> c_1 = \frac{y_0' - y_0r_2}{r_1 - r_2}\,e^{-r_1t_0}, \qquad c_2 = \frac{y_0r_1 - y_0'}{r_1 - r_2}\,e^{-r_2t_0} , \qquad (24)
> $$
>
> and with these constants (18) solves the initial value problem
>
> $$
> ay'' + by' + cy = 0, \qquad y(t_0) = y_0, \quad y'(t_0) = y_0' . \qquad (25)
> $$
>
> BDP calls (18) the **general solution** of (8). That every solution of (8) is of this form is [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|Theorem §14.4]] together with [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-14-2|Example §14.2]].
>
> *BDP: 3.1, Equations (18) and (24)*

^thm-13-2

> [!proof]+ Proof
> **(18) is a solution.** Differentiating,
>
> $$
> y' = c_1r_1e^{r_1t} + c_2r_2e^{r_2t}, \qquad (19) \qquad\qquad y'' = c_1r_1^2e^{r_1t} + c_2r_2^2e^{r_2t} . \qquad (20)
> $$
>
> Substituting and collecting the terms with $c_1$ and with $c_2$,
>
> $$
> ay'' + by' + cy = c_1\big(ar_1^2 + br_1 + c\big)e^{r_1t} + c_2\big(ar_2^2 + br_2 + c\big)e^{r_2t} . \qquad (21)
> $$
>
> Both brackets are $0$ because $r_1$ and $r_2$ are roots of (17), so $y$ is a solution.
>
> **The initial conditions.** Write $E_1 = e^{r_1t_0}$ and $E_2 = e^{r_2t_0}$. Setting $t = t_0$ in (18) and (19), the conditions become
>
> $$
> c_1E_1 + c_2E_2 = y_0, \qquad (22) \qquad\qquad c_1r_1E_1 + c_2r_2E_2 = y_0' . \qquad (23)
> $$
>
> Multiply (22) by $r_2$ and subtract (23): $c_1E_1(r_2 - r_1) = r_2y_0 - y_0'$. Multiply (22) by $r_1$ and subtract it from (23): $c_2E_2(r_2 - r_1) = y_0' - r_1y_0$. Since $r_1 - r_2 \ne 0$ and $E_1, E_2 \ne 0$, these give (24). Conversely, the constants (24) satisfy (22) and (23), as substitution shows. So for every choice of $t_0$, $y_0$, $y_0'$ the system has exactly one solution $(c_1, c_2)$ (its determinant is $(r_2 - r_1)E_1E_2 \ne 0$), and with it (18) solves (25).

^pf-13-2

*Uses:* [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-1|§13.1]], [[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-2|Def. §13.2]]

> [!remark] Remark: Behavior as t → ∞
> With distinct real roots the solution is a sum of two exponentials, so its long-run behavior is simple. If both roots are negative, every solution tends to $0$. If at least one root is positive, the solutions are in general unbounded; whether a growing solution tends to $+\infty$ or $-\infty$ is decided by the sign of the coefficient of $e^{rt}$ for the larger root $r$. In the less common case that one root is $0$ and the other negative, every solution tends to a constant (the coefficient of $e^{0t} = 1$).

^rem-13-1

> [!example] Example §13.2: Two Decaying Exponentials
> **(a)** Find the general solution of $y'' + 5y' + 6y = 0$.
>
> With $y = e^{rt}$, $r$ must satisfy $r^2 + 5r + 6 = (r + 2)(r + 3) = 0$, so $r_1 = -2$, $r_2 = -3$, and by Theorem §13.2
>
> $$
> y = c_1e^{-2t} + c_2e^{-3t} . \qquad (27)
> $$
>
> **(b)** Solve the initial value problem $y'' + 5y' + 6y = 0$, $y(0) = 2$, $y'(0) = 3$.
>
> From (27), $y(0) = c_1 + c_2 = 2$, and from $y' = -2c_1e^{-2t} - 3c_2e^{-3t}$, $y'(0) = -2c_1 - 3c_2 = 3$. Twice the first equation plus the second gives $-c_2 = 7$, so $c_2 = -7$ and $c_1 = 9$. (Formula (24) with $t_0 = 0$ agrees: $c_1 = \frac{3 - 2(-3)}{-2 - (-3)} = 9$, $c_2 = \frac{2(-2) - 3}{1} = -7$.) The solution is
>
> $$
> y = 9e^{-2t} - 7e^{-3t} . \qquad (31)
> $$
>
> **(c)** The solution starts upward (slope $3$) but both exponents are negative, so $y \to 0$: there is a maximum point. Locate it.
>
> $y' = -18e^{-2t} + 21e^{-3t} = 0$ gives, after multiplying by $e^{3t}$, $e^t = \frac{21}{18} = \frac76$, so
>
> $$
> t_m = \ln\tfrac76 \approx 0.15415, \qquad y_m = 9\Big(\tfrac67\Big)^2 - 7\Big(\tfrac67\Big)^3 = \tfrac{324}{49} - \tfrac{216}{49} = \tfrac{108}{49} \approx 2.20408 .
> $$
>
> *BDP: Examples 3.1.2, 3.1.3 and 3.1.5*

^ex-13-2

> [!example] Example §13.3: An Exam Initial Value Problem
> Find the solution of $y'' + 3y' - 10y = 0$ with $y(0) = 3$ and $y'(0) = 5$.
>
> The characteristic equation $r^2 + 3r - 10 = (r + 5)(r - 2) = 0$ has roots $2$ and $-5$, so $y = c_1e^{2t} + c_2e^{-5t}$ and $y' = 2c_1e^{2t} - 5c_2e^{-5t}$. The initial conditions give
>
> $$
> c_1 + c_2 = 3, \qquad 2c_1 - 5c_2 = 5 .
> $$
>
> Substituting $c_1 = 3 - c_2$ into the second, $6 - 7c_2 = 5$, so $c_2 = \frac17$ and $c_1 = \frac{20}{7}$:
>
> $$
> y = \tfrac{20}{7}e^{2t} + \tfrac17e^{-5t} .
> $$
>
> The larger root $2$ has a positive coefficient, so $y \to +\infty$ ([[§13 Homogeneous Differential Equations with Constant Coefficients#^rem-13-1|Remark: Behavior as t → ∞]]).
>
> *Source: 331 Midterm (Spring 2020), Q3*

^ex-13-3

> [!example] Example §13.4: Choosing the Initial Slope
> Consider $y'' + y' - 2y = 0$, $y(0) = 2$, $y'(0) = \beta$.
>
> **(a)** For which $\beta$ does $\lim_{t\to\infty} y(t) = 0$?
>
> **(b)** For which $\beta$ is $y(t) \ne 0$ for all $-\infty < t < \infty$, so that the graph never touches the $t$-axis?
>
> **The solution.** $r^2 + r - 2 = (r + 2)(r - 1)$, so $y = c_1e^{-2t} + c_2e^t$ and $y' = -2c_1e^{-2t} + c_2e^t$. The initial conditions are $c_1 + c_2 = 2$ and $-2c_1 + c_2 = \beta$. Subtracting, $3c_1 = 2 - \beta$, so
>
> $$
> c_1 = \frac{2 - \beta}{3}, \qquad c_2 = \frac{\beta + 4}{3}, \qquad y = \frac{2 - \beta}{3}e^{-2t} + \frac{\beta + 4}{3}e^{t} .
> $$
>
> **(a)** $e^{-2t} \to 0$, while $c_2e^t$ is unbounded unless $c_2 = 0$. So $y \to 0$ exactly when $c_2 = 0$, that is, $\beta = -4$; then $y = 2e^{-2t}$.
>
> **(b)** $y(t) = 0$ means $c_1e^{-2t} = -c_2e^t$. If $c_1$ and $c_2$ are both nonzero, this is $e^{3t} = -c_1/c_2$, which has the solution $t = \frac13\ln(-c_1/c_2)$ exactly when $c_1$ and $c_2$ have opposite signs. If one of them is $0$, the other is $2$ (since $c_1 + c_2 = 2$), and $y$ is $2e^{-2t}$ or $2e^t$, never $0$. Both cannot be negative, because $c_1 + c_2 = 2$. So $y$ never vanishes exactly when $c_1 \ge 0$ and $c_2 \ge 0$:
>
> $$
> 2 - \beta \ge 0 \ \text{ and } \ \beta + 4 \ge 0 \quad\Longleftrightarrow\quad -4 \le \beta \le 2 .
> $$
>
> The endpoints are included: $\beta = -4$ gives $2e^{-2t}$ and $\beta = 2$ gives $2e^t$. For $\beta < -4$ the solution crosses the axis at $t = \frac13\ln\frac{2 - \beta}{-(\beta + 4)} > 0$; for $\beta > 2$ it crosses at a negative $t$.
>
> *Source: 331 Written HW 3, Problem 4*

^ex-13-4

![[m331-13-1.svg]]
*Example §13.4: the solutions with $y(0) = 2$ and slopes $\beta = -6, -4, -1, 2, 4$. Every solution is $c_1e^{-2t} + c_2e^t$, dominated by $e^t$ as $t \to \infty$ and by $e^{-2t}$ as $t \to -\infty$. For $-4 \le \beta \le 2$ both coefficients are $\ge 0$ and the curve stays above the axis (the green boundary cases are pure exponentials, and only $\beta = -4$ decays). For $\beta = -6$ the $e^t$ term is negative and the curve crosses at $t = \frac13\ln 4 \approx 0.46$; for $\beta = 4$ the $e^{-2t}$ term is negative and it crosses at $t \approx -0.46$ (red dots).*
