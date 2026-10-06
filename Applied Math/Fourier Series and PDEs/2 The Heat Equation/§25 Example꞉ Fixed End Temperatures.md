---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 25
powers: "2.3"
aliases: ["Powers 2.3"]
tags: [fourier-series-and-pdes, math341]
---
← [[§24 Steady-State Temperatures]] · ↑ [[· 2 The Heat Equation]] · [[§26 Example꞉ Insulated Bar]] →

*Powers, Section 2.3 · MAT 341 lectures 9.19, 9.24, 9.26 · HW 3, HW 4, HW 5 · Practice Midterm 1.*

This section solves a complete heat conduction problem for the first time: a rod with insulated lateral surface, ends held at fixed temperatures $T_0$ and $T_1$, and initial temperature $f(x)$. The steady state $v$ of [[§24 Steady-State Temperatures|§24]] takes care of the end temperatures; the transient $w = u - v$ satisfies a homogeneous problem, which is solved by **separation of variables** (Fourier's method). Assuming a product $w = \phi(x)T(t)$ splits the heat equation into two ordinary differential equations; the boundary conditions single out the eigenfunctions $\sin(n\pi x/a)$; superposition of the product solutions gives a series, and the initial condition becomes a Fourier sine series problem. Physically, the solution is a sum of modes, each decaying like $\exp(-n^2\pi^2kt/a^2)$, so higher modes die first and the temperature relaxes to the straight-line steady state.

## The Problem and Its Transient

The temperature $u(x, t)$ in a uniform rod with insulated lateral surface, ends held at fixed temperatures and initial temperature distribution $f(x)$ satisfies

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (1) \\
u(0, t) &= T_0, && 0 < t, && (2) \\
u(a, t) &= T_1, && 0 < t, && (3) \\
u(x, 0) &= f(x), && 0 < x < a . && (4)
\end{aligned}
$$

By [[§24 Steady-State Temperatures#^ex-24-1|Example §24.1]] the steady state $v(x) = \lim_{t\to\infty} u(x, t)$ satisfies $v'' = 0$, $v(0) = T_0$, $v(a) = T_1$ ((5)–(6)) and is

$$
v(x) = T_0 + (T_1 - T_0)\frac xa , \qquad (7)
$$

and by [[§24 Steady-State Temperatures#^prop-24-1|Proposition §24.1]] the transient $w(x, t) = u(x, t) - v(x)$ satisfies

$$
\begin{aligned}
\frac{\partial^2w}{\partial x^2} &= \frac1k\frac{\partial w}{\partial t}, && 0 < x < a, \quad 0 < t, && (8) \\
w(0, t) &= 0, && 0 < t, && (9) \\
w(a, t) &= 0, && 0 < t, && (10) \\
w(x, 0) &= f(x) - v(x) \equiv g(x), && 0 < x < a . && (11)
\end{aligned}
$$

Once $w$ is found, the unknown temperature is

$$
u(x, t) = v(x) + w(x, t) . \qquad (12)
$$

> [!remark] Remark: Method — The Steady-State/Transient Split
> For a heat problem whose partial differential equation or boundary conditions are nonhomogeneous, with data independent of $t$:
> 1. **Steady state.** Set up and solve the steady-state problem for $v(x)$ ([[§24 Steady-State Temperatures#^rem-24-1|method of §24]]): drop the initial condition, replace $u$ by $v$ and $\partial u/\partial t$ by $0$, and solve the two-point boundary value problem.
> 2. **Transient problem.** Put $w(x, t) = u(x, t) - v(x)$. The equation and boundary conditions for $w$ are those for $u$ with the nonhomogeneous terms deleted ([[§24 Steady-State Temperatures#^rem-24-3|Remark: Boundary Conditions of the Transient]]); the initial condition becomes $w(x, 0) = f(x) - v(x) = g(x)$. Check that $w \equiv 0$ satisfies the equation and the boundary conditions.
> 3. **Solve for $w$** by separation of variables (below).
> 4. **Reassemble** $u(x, t) = v(x) + w(x, t)$.
>
> If the problem is already homogeneous (as for the insulated bar of [[§26 Example꞉ Insulated Bar|§26]]), skip steps 1, 2 and 4 and separate $u$ directly. The split cannot be skipped otherwise: separation of variables may be applied to $w$ but **not** to the original $u$, because a product $\phi(x)T(t)$ cannot satisfy $u(0, t) = T_0 \ne 0$ for all $t$ unless $T(t)$ is constant.

^rem-25-1

## Separation of Variables

> [!definition] Definition §31.1: Trivial Solution
> Since the partial differential equation (8) and the boundary conditions (9), (10) are homogeneous, the function $w \equiv 0$ satisfies them. Because it is obvious and of no help in satisfying the initial condition, it is called the **trivial solution**.
>
> *Powers: 2.3 (text)*

^def-25-1

> [!definition] Definition §31.3: Separation of Variables; Product Solution
> The **product method**, **separation of variables**, or **Fourier's method** seeks nontrivial solutions of the homogeneous equation and boundary conditions in the form of a **product**
>
> $$
> w(x, t) = \phi(x)T(t) ,
> $$
>
> where neither factor $\phi(x)$ nor $T(t)$ is identically $0$ (that would lead back to the trivial solution). For the method to work it is essential to have a homogeneous partial differential equation and homogeneous boundary conditions.
>
> *Powers: 2.3 (text)*

^def-25-2

> [!theorem] Proposition §31.1: The Separated Equations
> A product $w(x, t) = \phi(x)T(t)$, with neither factor identically zero, satisfies the heat equation (8) and the boundary conditions (9), (10) if and only if there is a constant $p$ (the **separation constant**) such that
>
> $$
> \phi'' - p\phi = 0, \qquad T' - pkT = 0 , \qquad (13)
> $$
>
> $$
> \phi(0) = 0, \qquad \phi(a) = 0 . \qquad (14)
> $$
>
> *Powers: 2.3, Equations (13)–(14)*

^prop-25-1

> [!proof]+ Proof
> Each factor depends on one variable only, so
>
> $$
> \frac{\partial^2w}{\partial x^2} = \phi''(x)T(t), \qquad \frac{\partial w}{\partial t} = \phi(x)T'(t) ,
> $$
>
> and the partial differential equation becomes $\phi''(x)T(t) = \frac1k\phi(x)T'(t)$. Dividing through by $\phi T$ (at points where it is not zero),
>
> $$
> \frac{\phi''(x)}{\phi(x)} = \frac{T'(t)}{kT(t)}, \qquad 0 < x < a, \quad 0 < t .
> $$
>
> *Here is the key argument.* The ratio on the left contains functions of $x$ alone and cannot vary with $t$. The ratio on the right contains functions of $t$ alone and cannot vary with $x$. Since the equality holds for all $x$ in $0 < x < a$ and all $t > 0$, the common value of the two sides varies neither with $x$ nor with $t$: it is a constant $p$,
>
> $$
> \frac{\phi''(x)}{\phi(x)} = p, \qquad \frac{T'(t)}{kT(t)} = p ,
> $$
>
> which is (13). The boundary conditions in product form are
>
> $$
> w(0, t) = \phi(0)T(t) = 0, \qquad w(a, t) = \phi(a)T(t) = 0 .
> $$
>
> These hold for all $t > 0$ either if $T(t) \equiv 0$, which is forbidden, or if the other factors are zero: (14).
>
> Conversely, if (13) and (14) hold, then $\phi''T = p\phi T = \frac1k\phi T'$, which is (8), and $w(0, t) = \phi(0)T(t) = 0$, $w(a, t) = 0$.

^pf-25-1

*Uses:* [[§25 Example꞉ Fixed End Temperatures#^def-25-1|Def. §25.1]], [[§25 Example꞉ Fixed End Temperatures#^def-25-2|Def. §25.2]]

The task now is to solve (13) and satisfy the boundary conditions (14) while avoiding the trivial solution. Problems of this kind are called eigenvalue problems ([[§26 Example꞉ Insulated Bar#^def-26-1|Definition §26.1]]).

> [!theorem] Theorem §31.2: The Eigenvalue Problem with Fixed Ends
> The problem
>
> $$
> \phi'' - p\phi = 0, \quad 0 < x < a; \qquad \phi(0) = 0, \qquad \phi(a) = 0
> $$
>
> has a solution $\phi \not\equiv 0$ if and only if $p = -\lambda_n^2$ with
>
> $$
> \lambda_n = \frac{n\pi}a, \qquad n = 1, 2, 3, \ldots ,
> $$
>
> and then $\phi$ is a constant multiple of
>
> $$
> \phi_n(x) = \sin(\lambda_nx) = \sin\Big(\frac{n\pi x}a\Big) .
> $$
>
> The corresponding solutions of $T' - pkT = 0$ are the constant multiples of $T_n(t) = \exp(-\lambda_n^2kt)$.
>
> *Powers: 2.3 (text)*

^thm-25-2

> [!proof]+ Proof
> Consider the sign of $p$.
>
> **Case 1: $p > 0$.** The solutions of (13) are
>
> $$
> \phi(x) = c_1\cosh(\sqrt p\,x) + c_2\sinh(\sqrt p\,x), \qquad T(t) = ce^{pkt} .
> $$
>
> (The characteristic roots of $\phi'' - p\phi = 0$ are $\pm\sqrt p$, and $\cosh$, $\sinh$ are combinations of $e^{\pm\sqrt p\,x}$.) The boundary conditions give $\phi(0) = c_1 = 0$ and $\phi(a) = c_2\sinh(\sqrt p\,a) = 0$. The sinh function is $0$ only when its argument is $0$, which is not true of $\sqrt p\,a$; so $c_1 = c_2 = 0$ and $\phi \equiv 0$, which is not acceptable.
>
> **Case 2: $p = 0$.** The solutions of (13) are $\phi(x) = c_1 + c_2x$, $T(t) = c$. The boundary conditions require $\phi(0) = c_1 = 0$ and $\phi(a) = c_2a = 0$. Again $\phi \equiv 0$.
>
> **Case 3: $p < 0$.** Replace $p$ by $-\lambda^2$ with $\lambda > 0$. Equations (13) become
>
> $$
> \phi'' + \lambda^2\phi = 0, \qquad T' + \lambda^2kT = 0 ,
> $$
>
> whose solutions are
>
> $$
> \phi(x) = c_1\cos(\lambda x) + c_2\sin(\lambda x), \qquad T(t) = c\exp(-\lambda^2kt) .
> $$
>
> The boundary conditions require $\phi(0) = c_1 = 0$, leaving $\phi(x) = c_2\sin(\lambda x)$, and then $\phi(a) = c_2\sin(\lambda a) = 0$. Either $c_2 = 0$, making $\phi \equiv 0$ (rejected, since it leads to the trivial solution $w \equiv 0$), or $\sin(\lambda a) = 0$. The latter requires $\lambda = n\pi/a$ with $n = \pm1, \pm2, \pm3, \ldots$. Negative $n$ give no new functions, because $\sin(-\theta) = -\sin(\theta)$, so $n = 1, 2, 3, \ldots$ suffice: $\lambda_n = n\pi/a$.
>
> Because the differential equations (13) and the boundary conditions (14) are homogeneous, any constant multiple of a solution is a solution; so the constant $c_2$ in $\phi$ and $c$ in $T$ may be dropped, which gives $\phi_n$ and $T_n$.

^pf-25-2

*Uses:* [[§25 Example꞉ Fixed End Temperatures#^prop-25-1|§25.1]], [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|331 Thm. §17.2]], [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|331 Thm. §19.2]]

> [!theorem] Proposition §31.3: The Product Solutions
> For each $n = 1, 2, 3, \ldots$ the product
>
> $$
> w_n(x, t) = \sin(\lambda_nx)\exp(-\lambda_n^2kt), \qquad \lambda_n = \frac{n\pi}a ,
> $$
>
> has these properties:
> 1. $\dfrac{\partial^2w_n}{\partial x^2} = -\lambda_n^2w_n$ and $\dfrac{\partial w_n}{\partial t} = -\lambda_n^2kw_n$; therefore $w_n$ satisfies the heat equation (8).
> 2. $w_n(0, t) = \sin(0)e^{-\lambda_n^2kt} = 0$ for every $n$ and $t$; therefore $w_n$ satisfies the boundary condition at $x = 0$.
> 3. $w_n(a, t) = \sin(\lambda_na)e^{-\lambda_n^2kt} = 0$ for every $n$ and $t$, because $\lambda_na = n\pi$ and $\sin(n\pi) = 0$; therefore $w_n$ satisfies the boundary condition at $x = a$.
>
> *Powers: 2.3 (text)*

^prop-25-3

> [!proof]+ Proof
> Differentiate: $\partial_x^2\sin(\lambda_nx) = -\lambda_n^2\sin(\lambda_nx)$ and $\partial_t\exp(-\lambda_n^2kt) = -\lambda_n^2k\exp(-\lambda_n^2kt)$, so $\partial_x^2w_n = -\lambda_n^2w_n$ and $\frac1k\partial_tw_n = -\lambda_n^2w_n$, and (8) holds. Properties 2 and 3 are the evaluations shown.

^pf-25-3

> [!theorem] Theorem §31.4: Principle of Superposition
> If $u_1, u_2, \ldots$ are solutions of the same linear, homogeneous equations, then so is
>
> $$
> u = c_1u_1 + c_2u_2 + \cdots .
> $$
>
> *Powers: 2.3, Principle of Superposition*

^thm-25-4

*Powers omits the proof. For finitely many terms it is the computation of [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-2|331 Thm. §18.2]], with the linear operations $w \mapsto w_{xx} - \frac1kw_t$, $w \mapsto w(0, t)$, $w \mapsto w(a, t)$ in place of $L$; for an infinite series the convergence of the series and of its differentiated series must be checked, as in the proof of Theorem §25.5.*

## The Solution

There are infinitely many product solutions, so an infinite series is needed to combine them all.

> [!theorem] Theorem §25.5: Solution of the Fixed-End Problem
> Let $g = f - v$ be sectionally smooth on $0 < x < a$, and let
>
> $$
> b_n = \frac2a\int_0^a g(x)\sin\Big(\frac{n\pi x}a\Big)\,dx . \qquad (17)
> $$
>
> Then
>
> $$
> w(x, t) = \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt), \qquad \lambda_n = \frac{n\pi}a , \qquad (15)
> $$
>
> satisfies the heat equation (8) for $t > 0$ and the boundary conditions (9), (10), and at $t = 0$
>
> $$
> w(x, 0) = \sum_{n=1}^\infty b_n\sin\Big(\frac{n\pi x}a\Big) = g(x), \qquad 0 < x < a , \qquad (16)
> $$
>
> at every point where $g$ is continuous (at a jump, the series gives the average of the one-sided limits). The solution of (1)–(4) is
>
> $$
> u(x, t) = v(x) + w(x, t) = T_0 + (T_1 - T_0)\frac xa + \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt) .
> $$
>
> *Powers: 2.3, Equations (15)–(17)*

^thm-25-5

> [!proof]+ Proof
> **Boundary conditions.** At $x = 0$ and at $x = a$ each term of (15) is $0$ ([[§25 Example꞉ Fixed End Temperatures#^prop-25-3|Proposition §25.3]]), so the sum is $0$ as well.
>
> **Heat equation.** Differentiate (15) term by term; by Proposition §25.3 each term satisfies (8), so the differentiated series satisfy $w_{xx} = \frac1kw_t$. Note that the choice of the $b_n$ does not enter into this check, so (15) plays the role of a general solution of (8)–(10).
>
> (Powers sets aside the convergence questions; here is why term-by-term differentiation is valid for $t > 0$. The coefficients are bounded ([[§14 Operations on Fourier Series#^prop-14-8|Proposition §14.8]]): $|b_n| \le \frac2a\int_0^a|g|\,dx =: M$. Fix $t_0 > 0$. For $t \ge t_0$ and all $x$, the terms of the series for $w$, $w_x$, $w_{xx}$ and $w_t$ are bounded by $M$, $M\lambda_n$, $M\lambda_n^2$ and $Mk\lambda_n^2$ times $\exp(-\lambda_n^2kt_0)$, and $\sum_n n^2\exp(-n^2\pi^2kt_0/a^2)$ converges ([[Ratio Test|ratio test]]). By the Weierstrass M-test all four series converge uniformly on $0 \le x \le a$, $t \ge t_0$. In $x$: for fixed $t$ the sine coefficients $B_n(t) = b_ne^{-\lambda_n^2kt}$ satisfy $\sum n^2|B_n(t)| < \infty$, so $w(\cdot, t)$ has continuous derivatives $w_x$, $w_{xx}$ given by the differentiated series ([[§14 Operations on Fourier Series#^thm-14-7|Theorem §14.7]]). In $t$: for fixed $x$ let $G(t) = \sum_n b_n\sin(\lambda_nx)(-\lambda_n^2k)e^{-\lambda_n^2kt}$, a uniformly convergent series of continuous functions on $t \ge t_0$, hence continuous. Integrating term by term from $t_0$ to $t$ gives $\int_{t_0}^tG = w(x, t) - w(x, t_0)$, so $w_t = G$ by the fundamental theorem of calculus. This is 341 HW 3, Problem 3, with $a = \pi$, $k = 1$.)
>
> **Initial condition.** Of the four parts of the original problem, only the initial condition remains. At $t = 0$ the exponentials in (15) are all $1$, and the condition takes the form (16). This is a problem in Fourier series: (16) is the Fourier sine series of $g$ on $0 < x < a$ (the Fourier series of its odd periodic extension of period $2a$, [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Definition §11.4]]), whose coefficients are (17). If $g$ is sectionally smooth, this series converges to $g(x)$ at each point of $0 < x < a$ where $g$ is continuous and to $\frac12(g(x+) + g(x-))$ at a jump ([[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]]). So the $w$ found satisfies all requirements set on it. (Even if $g$ does not satisfy these conditions, Powers notes that the solution arrived at is the best that can be done.)
>
> **The original problem.** By [[§24 Steady-State Temperatures#^prop-24-1|Proposition §24.1]], $u = v + w$ satisfies (1)–(4).

^pf-25-5

*Uses:* [[§25 Example꞉ Fixed End Temperatures#^prop-25-3|§25.3]], [[§25 Example꞉ Fixed End Temperatures#^thm-25-4|§25.4]], [[§24 Steady-State Temperatures#^prop-24-1|§24.1]], [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Def. §11.4]], [[§12 Convergence of Fourier Series#^thm-12-1|§12.1]], [[§14 Operations on Fourier Series#^prop-14-8|§14.8]], [[§14 Operations on Fourier Series#^thm-14-7|§14.7]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]], [[§86 The Ratio and Root Tests#^thm-86-1|Calc Thm. §86.1]] (ratio test)

> [!remark]- Connections
> - The M-test and term-by-term integration of a uniformly convergent series: [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]].
> - The coefficient formula (17) is the coordinate formula for an orthogonal basis, $b_n = \langle g, \phi_n\rangle/\langle\phi_n, \phi_n\rangle$ with $\langle\phi_n, \phi_n\rangle = a/2$, in the inner product $\int_0^a fg\,dx$: [[§56 Inner Product Spaces#^thm-56-2|235 Thm. §56.2]], [[§57 Applications of Inner Product Spaces#^thm-57-3|235 Thm. §57.3]].

> [!remark] Remark: Method — Separation of Variables, Step by Step
> To solve a homogeneous problem such as (8)–(11):
> 1. **Assume a product** $w(x, t) = \phi(x)T(t)$ and substitute into the partial differential equation. Divide by $\phi T$ so that each side depends on one variable only; both sides then equal a constant $p$. This gives one ordinary differential equation for $\phi$ and one for $T$.
> 2. **Transfer the boundary conditions to $\phi$.** Since they are homogeneous, $w(0, t) = \phi(0)T(t) = 0$ for all $t$ forces $\phi(0) = 0$ (as $T \not\equiv 0$); similarly at $x = a$, and similarly for $w_x$ or $hw + \kappa w_x$.
> 3. **Solve the eigenvalue problem for $\phi$** by cases: $p > 0$, $p = 0$, $p < 0$ (write $p = -\lambda^2$). Keep the values of $p$ for which a nonzero $\phi$ exists; label them $p_n = -\lambda_n^2$ with eigenfunctions $\phi_n$.
> 4. **Solve for $T$:** $T_n(t) = \exp(-\lambda_n^2kt)$. The **basic solutions** are $w_n = \phi_n(x)T_n(t)$.
> 5. **Superpose:** $w = \sum c_nw_n$ satisfies the equation and the boundary conditions for any coefficients.
> 6. **Impose the initial condition:** $\sum c_n\phi_n(x) = g(x)$. Here this is a Fourier sine series (odd periodic extension of $g$), so $c_n = \frac2a\int_0^ag(x)\sin(n\pi x/a)\,dx$; in later problems it is a cosine series ([[§26 Example꞉ Insulated Bar#^thm-26-2|Theorem §26.2]]) or an expansion in other orthogonal functions ([[§27 Example꞉ Different Boundary Conditions#^thm-27-3|Theorem §27.3]], [[§28 Example꞉ Convection#^thm-28-3|Theorem §28.3]]).
>
> Powers' own summary of the whole procedure, after three examples, is [[§27 Example꞉ Different Boundary Conditions#^rem-27-1|Remark: Method — Summary of Separation of Variables]] in §21.

^rem-25-2

## Examples

> [!example] Example §31.1: Initial Temperature Zero
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac1k\frac{\partial u}{\partial t}, \quad 0 < x < a,\ 0 < t; \qquad u(0, t) = T_0, \quad u(a, t) = T_1, \quad 0 < t; \qquad u(x, 0) = 0, \quad 0 < x < a .
> $$
>
> The steady-state solution is $v(x) = T_0 + (T_1 - T_0)x/a$. The transient $w = u - v$ satisfies (8)–(10) and
>
> $$
> w(x, 0) = -T_0 - (T_1 - T_0)\frac xa \equiv g(x), \qquad 0 < x < a .
> $$
>
> By Theorem §25.5, $w(x, t) = \sum b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt)$ (18) with
>
> $$
> \begin{aligned}
> b_n &= \frac2a\int_0^a\Big[-T_0 - (T_1 - T_0)\frac xa\Big]\sin\Big(\frac{n\pi x}a\Big)dx \\
> &= \frac{2T_0}a\,\frac{\cos(n\pi x/a)}{n\pi/a}\bigg|_0^a - \frac2{a^2}(T_1 - T_0)\,\frac{\sin(n\pi x/a) - (n\pi x/a)\cos(n\pi x/a)}{(n\pi/a)^2}\bigg|_0^a \\
> &= -\frac{2T_0}{n\pi}\big(1 - (-1)^n\big) + \frac{2(T_1 - T_0)}{n\pi}(-1)^n \\
> &= -\frac2{n\pi}\big(T_0 - T_1(-1)^n\big) .
> \end{aligned}
> $$
>
> (For the second line: $\int x\sin(bx)\,dx = \big(\sin(bx) - bx\cos(bx)\big)/b^2$.) The complete solution is $u(x, t) = w(x, t) + T_0 + (T_1 - T_0)x/a$, where
>
> $$
> w(x, t) = -\frac2\pi\sum_{n=1}^\infty\frac{T_0 - T_1(-1)^n}n\sin(\lambda_nx)\exp(-\lambda_n^2kt) . \qquad (19)
> $$
>
> **Features of the solution.**
> - $u(x, 0)$ really is $0$ for $0 < x < a$, because at $t = 0$ the Fourier series converges to $-v(x)$.
> - When $t$ is positive but very small, the series for $w(x, t)$ almost equals $-T_0 - (T_1 - T_0)x/a$. But at $x = 0$ and $x = a$ it adds up to zero, and $w$ is a continuous function of $x$ for $t > 0$, so $u$ satisfies the boundary conditions: the end temperatures spread into the cold rod from both ends.
> - When $t$ is large, $\exp(-\lambda_1^2kt)$ is small and the other exponentials are still smaller. Then $w(x, t)$ is well approximated by the first term (or first few terms) of the series.
> - As $t \to \infty$, $w(x, t)$ disappears completely and $u \to v$.
>
> *Powers: 2.3, Example*

^ex-25-1

![[m341-19-1.svg]]
*Example §19.1 with $T_0 = 20$, $T_1 = 100$ ($a = 1$, 400 terms): $u(x, t)$ as a function of $x$ at the dimensionless times $kt/a^2 = 0.001$, $0.01$, $0.1$, $1$. The heat enters from both ends of the initially cold rod; by $kt/a^2 = 1$ the first mode has decayed by $e^{-\pi^2} \approx 5 \times 10^{-5}$ and the profile is indistinguishable from the steady state $v(x) = 20 + 80x/a$ (dashed).*

The dimensionless combinations $x/a$ and $kt/a^2$ are the only way $x$ and $t$ enter (19): a rod twice as long takes four times as long to reach the same stage.

> [!example] Example §31.2: A Homework Problem from Start to Finish
> Solve
>
> $$
> \frac{\partial u}{\partial t} = \frac{\partial^2u}{\partial x^2}, \quad 0 < x < a,\ t > 0; \qquad u(x, 0) = \frac xa; \qquad u(0, t) = 0, \quad u(a, t) = 2 .
> $$
>
> **(a) Steady state.** $v'' = 0$, $v(0) = 0$, $v(a) = 2$, so $v = Ax + B$ with $B = 0$, $A = 2/a$: $v(x) = \dfrac{2x}a$.
>
> **(b) Transient.** $w = u - v$ satisfies $w_t = w_{xx}$, $w(0, t) = w(a, t) = 0$, and $w(x, 0) = \dfrac xa - \dfrac{2x}a = -\dfrac xa$.
>
> **(c) Separation.** If $w_n = \phi_n(x)T_n(t)$ satisfies the equation and boundary conditions and $T_n'/T_n = p_n$, then $\phi_nT_n' = \phi_n''T_n$ gives $\phi_n'' = p_n\phi_n$, with $\phi_n(0) = \phi_n(a) = 0$ (as $T_n \not\equiv 0$).
>
> **(d) Basic solutions.** By Theorem §25.2 (the three cases $p > 0$, $p = 0$, $p < 0$ are exactly its proof): $p_n = -(n\pi/a)^2$, $\phi_n = \sin(n\pi x/a)$, $T_n = e^{-(n\pi/a)^2t}$, and
>
> $$
> w_n(x, t) = e^{-(n\pi/a)^2t}\sin\Big(\frac{n\pi x}a\Big), \qquad n = 1, 2, \ldots .
> $$
>
> **(e) Coefficients.** $w = \sum a_nw_n$ with $\sum a_n\sin(n\pi x/a) = -x/a$, so
>
> $$
> a_n = \frac2a\int_0^a\Big(-\frac xa\Big)\sin\Big(\frac{n\pi x}a\Big)dx = -\frac2{a^2}\cdot\Big(-\frac{a^2(-1)^n}{n\pi}\Big) = \frac{2(-1)^n}{n\pi} ,
> $$
>
> using $\int_0^ax\sin(n\pi x/a)\,dx = \Big[-\frac{ax}{n\pi}\cos\frac{n\pi x}a\Big]_0^a + \frac a{n\pi}\int_0^a\cos\frac{n\pi x}a\,dx = -\frac{a^2(-1)^n}{n\pi}$. Therefore
>
> $$
> u(x, t) = \frac{2x}a + \sum_{n=1}^\infty\frac{2(-1)^n}{n\pi}\,e^{-(n\pi/a)^2t}\sin\Big(\frac{n\pi x}a\Big) .
> $$
>
> Check at $t = 0$: the sine series of $x/a$ on $(0, a)$ is $\sum\frac{2(-1)^{n+1}}{n\pi}\sin\frac{n\pi x}a$, so the series is $-x/a$ and $u(x, 0) = 2x/a - x/a = x/a$.
>
> *The answer key gives $a_n = 2(-1)^n/(n\pi a)$, with an extra factor $1/a$, and writes the exponentials as $e^{-(n\pi/a)^2x}$ for $e^{-(n\pi/a)^2t}$; the computation above gives $2(-1)^n/(n\pi)$.*
>
> *Source: 341 HW 4, Problems 2–3*

^ex-25-2

> [!example] Example §31.3: A Different Diffusivity
> Solve $u_t = 2u_{xx}$, $0 < x < 1$, $t > 0$; $u(x, 0) = 4x$; $u(0, t) = 0$, $u(1, t) = 3$.
>
> **Steady state.** $0 = 2v''$, $v(0) = 0$, $v(1) = 3$: $v(x) = 3x$ ([[§24 Steady-State Temperatures#^ex-24-1|Example §24.1]]).
>
> **Transient.** $w_t = 2w_{xx}$, $w(0, t) = w(1, t) = 0$, $w(x, 0) = 4x - 3x = x$.
>
> **Separation.** $\phi T' = 2\phi''T$, so $\dfrac{\phi''}\phi = \dfrac{T'}{2T} = p$: $\phi'' = p\phi$, $\phi(0) = \phi(1) = 0$, and $T' = 2pT$. This is (13) with $k = 2$, $a = 1$; by Theorem §25.2, $p = -(n\pi)^2$, $\phi_n = \sin(n\pi x)$, $T_n = e^{-2n^2\pi^2t}$, and $w_n = \sin(n\pi x)e^{-2n^2\pi^2t}$.
>
> **Coefficients.** $c_n = 2\int_0^1x\sin(n\pi x)\,dx = 2\cdot\dfrac{(-1)^{n+1}}{n\pi} = \dfrac{2(-1)^{n+1}}{n\pi}$. So
>
> $$
> u(x, t) = 3x + \sum_{n=1}^\infty\frac{2(-1)^{n+1}}{n\pi}\sin(n\pi x)\,e^{-2n^2\pi^2t} .
> $$
>
> Compared with $k = 1$, every mode decays twice as fast: $k$ sets the time scale $a^2/k$.
>
> *Source: 341 Practice Midterm 1, Q7*

^ex-25-3

> [!example] Example §25.4: Lateral Convection Adds a Uniform Decay
> Continue [[§24 Steady-State Temperatures#^ex-24-5|Example §24.5]]: solve $w_t = w_{xx} - \gamma^2w$, $w(0, t) = w(a, t) = 0$, $w(x, 0) = f(x) - T$.
>
> **(c) Separation.** With $w_n = \phi_n(x)T_n(t)$: $\phi_nT_n' = \phi_n''T_n - \gamma^2\phi_nT_n$, so
>
> $$
> p_n = \frac{T_n'}{T_n} = \frac{\phi_n''}{\phi_n} - \gamma^2, \qquad\text{that is}\qquad \phi_n'' = (p_n + \gamma^2)\phi_n, \quad \phi_n(0) = \phi_n(a) = 0 .
> $$
>
> **(d) Basic solutions.** This is Theorem §25.2 with $p_n + \gamma^2$ in place of $p$: nonzero solutions exist exactly when $p_n + \gamma^2 = -(n\pi/a)^2$, so
>
> $$
> \phi_n(x) = \sin\Big(\frac{n\pi x}a\Big), \qquad p_n = -\gamma^2 - \Big(\frac{n\pi}a\Big)^2, \qquad w_n(x, t) = e^{-[\gamma^2 + (n\pi/a)^2]t}\sin\Big(\frac{n\pi x}a\Big) .
> $$
>
> **(e) Coefficients.** $w = \sum c_nw_n$ and $w(x, 0) = \sum c_n\sin(n\pi x/a) = f(x) - T$, so
>
> $$
> c_n = \frac2a\int_0^a\big(f(x) - T\big)\sin\Big(\frac{n\pi x}a\Big)dx .
> $$
>
> So $w(x, t) = e^{-\gamma^2t}\,\tilde w(x, t)$, where $\tilde w$ is the solution of the plain heat equation $\tilde w_t = \tilde w_{xx}$ with the same boundary and initial data: the lateral heat loss multiplies every mode by the same factor $e^{-\gamma^2t}$. (Direct check: if $\tilde w_t = \tilde w_{xx}$, then $(e^{-\gamma^2t}\tilde w)_t = e^{-\gamma^2t}(\tilde w_{xx} - \gamma^2\tilde w)$.)
>
> *Source: 341 HW 5, Problem 1(c)–(e)*

^ex-25-4
