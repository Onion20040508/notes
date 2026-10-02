---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 21
powers: "2.5"
aliases: ["Powers 2.5"]
tags: [fourier-series-and-pdes, math341]
---
← [[§20 Example꞉ Insulated Bar]] · ↑ [[· 2 The Heat Equation]] · [[§22 Example꞉ Convection]] →

*Powers, Section 2.5 · MAT 341 lectures 9.26, 10.1 · HW 5.*

In many important cases the boundary conditions at the two ends are of different kinds. This section solves the problem of a rod with one end held at a constant temperature and the other insulated. The eigenvalue problem now has eigenfunctions $\sin\big((2n - 1)\pi x/2a\big)$, quarter-, three-quarter-, five-quarter-waves on $0 < x < a$, whose frequencies are not the integer multiples of a fundamental. So the initial condition is no longer a routine Fourier series; it is an expansion in these functions, justified by their orthogonality and by an extension trick that reduces it to a sine series on twice the interval. After three examples Powers summarizes the method of separation of variables.

## The Problem and the Eigenvalue Problem

The temperature in a rod with the end $x = 0$ held at the constant temperature $T_0$ and the end $x = a$ insulated satisfies

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (1) \\
u(0, t) &= T_0, && 0 < t, && (2) \\
\frac{\partial u}{\partial x}(a, t) &= 0, && 0 < t, && (3) \\
u(x, 0) &= f(x), && 0 < x < a . && (4)
\end{aligned}
$$

The steady-state problem is $v'' = 0$, $v(0) = T_0$, $v'(a) = 0$; with $v = A + Bx$ the conditions give $A = T_0$, $B = 0$, so $v(x) = T_0$ (Exercise 2.5.1). The transient temperature $w(x, t) = u(x, t) - T_0$ satisfies ([[§18 Steady-State Temperatures#^rem-18-3|Remark: Boundary Conditions of the Transient]])

$$
\begin{aligned}
\frac{\partial^2w}{\partial x^2} &= \frac1k\frac{\partial w}{\partial t}, && 0 < x < a, \quad 0 < t, && (5) \\
w(0, t) &= 0, \quad \frac{\partial w}{\partial x}(a, t) = 0, && 0 < t, && (6) \\
w(x, 0) &= f(x) - T_0 = g(x), && 0 < x < a . && (7)
\end{aligned}
$$

This problem is homogeneous, so separation of variables applies. Assuming $w(x, t) = \phi(x)T(t)$ and inserting into (5) leads, as before, to

$$
\frac{\phi''(x)}{\phi(x)} = \frac{T'(t)}{kT(t)} = \text{constant} . \qquad (8)
$$

The boundary conditions take the form $\phi(0)T(t) = 0$ (9) and $\phi'(a)T(t) = 0$ (10) for $0 < t$, so

$$
\phi(0) = 0, \qquad \phi'(a) = 0 . \qquad (11)
$$

> [!theorem] Theorem §21.1: Eigenvalues for a Fixed and an Insulated End
> The eigenvalue problem
>
> $$
> \phi'' + \lambda^2\phi = 0, \quad 0 < x < a , \qquad (12)
> $$
>
> with the boundary conditions (11) has the solution
>
> $$
> \lambda_n = \frac{(2n - 1)\pi}{2a}, \qquad \phi_n(x) = \sin(\lambda_nx), \qquad n = 1, 2, 3, \ldots . \qquad (15)
> $$
>
> A positive or zero separation constant in (8) forces $\phi \equiv 0$; so $0$ is not an eigenvalue. The corresponding time factors, from $T' + \lambda^2kT = 0$ (13), are $T_n(t) = \exp(-\lambda_n^2kt)$.
>
> *Powers: 2.5, Equations (11)–(15)*

^thm-21-1

> [!proof]+ Proof
> **Negative constant $-\lambda^2$, $\lambda > 0$.** The general solution of (12) is $\phi(x) = c_1\cos(\lambda x) + c_2\sin(\lambda x)$. The condition $\phi(0) = 0$ requires $c_1 = 0$, leaving $\phi(x) = c_2\sin(\lambda x)$. The condition at $x = a$ now takes the form
>
> $$
> \phi'(a) = c_2\lambda\cos(\lambda a) = 0 .
> $$
>
> The three choices are: $c_2 = 0$, which gives the trivial solution; $\lambda = 0$, excluded here and treated below; and $\cos(\lambda a) = 0$. The third alternative, the only acceptable one, requires that $\lambda a$ be an odd multiple of $\pi/2$:
>
> $$
> \lambda_n = \frac{(2n - 1)\pi}{2a}, \qquad n = 1, 2, \ldots . \qquad (14)
> $$
>
> **Zero and positive constants.** (Powers says "by trial and error", leaving the zero case to Exercise 2.5.2; here is the check.) If the constant is $0$, $\phi = c_1 + c_2x$; $\phi(0) = c_1 = 0$ and $\phi'(a) = c_2 = 0$, so $\phi \equiv 0$ and $0$ is not an eigenvalue. If it is $p^2 > 0$, $\phi = c_1\cosh(px) + c_2\sinh(px)$; $\phi(0) = c_1 = 0$, and $\phi'(a) = c_2p\cosh(pa) = 0$ forces $c_2 = 0$, since $\cosh > 0$.

^pf-21-1

*Uses:* [[§20 Example꞉ Insulated Bar#^def-20-1|Def. §20.1]], [[§15 Complex Roots of the Characteristic Equation#^thm-15-2|331 Thm. §15.2]]

## Expanding in the New Eigenfunctions

As in previous cases, the general solution of the homogeneous problem (5)–(6) is a general linear combination of the product solutions,

$$
w(x, t) = \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt) , \qquad (16)
$$

and the coefficients must be chosen to satisfy the initial condition (7):

$$
w(x, 0) = \sum_{n=1}^\infty b_n\sin\Big(\frac{(2n - 1)\pi x}{2a}\Big) = g(x), \qquad 0 < x < a . \qquad (17)
$$

A routine Fourier sine series on $0 < x < a$ would involve the functions $\sin(n\pi x/a)$, not the functions here.

> [!theorem] Proposition §21.2: Orthogonality of the Eigenfunctions
> With $\lambda_n = (2n - 1)\pi/2a$,
>
> $$
> \int_0^a\sin(\lambda_nx)\sin(\lambda_mx)\,dx = \begin{cases} 0, & m \ne n, \\ \dfrac a2, & m = n . \end{cases}
> $$
>
> *Powers: Exercise 2.5.10*

^prop-21-2

> [!proof]+ Proof
> By the product-to-sum identity $\sin A\sin B = \frac12\big(\cos(A - B) - \cos(A + B)\big)$,
>
> $$
> \int_0^a\sin(\lambda_nx)\sin(\lambda_mx)\,dx = \frac12\int_0^a\cos\big((\lambda_n - \lambda_m)x\big)\,dx - \frac12\int_0^a\cos\big((\lambda_n + \lambda_m)x\big)\,dx .
> $$
>
> Here $(\lambda_n - \lambda_m)a = (n - m)\pi$ and $(\lambda_n + \lambda_m)a = (n + m - 1)\pi$ are integer multiples of $\pi$. If $m \ne n$, both frequencies are nonzero, and $\int_0^a\cos(\mu x)\,dx = \sin(\mu a)/\mu = 0$ for $\mu a \in \pi\mathbb{Z}\setminus\{0\}$; so the integral is $0$. If $m = n$, the first integral is $\frac12\int_0^a1\,dx = \frac a2$ and the second is $0$ (since $n + m - 1 = 2n - 1 \ne 0$).

^pf-21-2

> [!theorem] Theorem §21.3: Expansion in the Quarter-Wave Sines
> If $g$ is sectionally smooth on $0 < x < a$ and
>
> $$
> b_n = \frac2a\int_0^ag(x)\sin\Big(\frac{(2n - 1)\pi x}{2a}\Big)dx , \qquad (18)
> $$
>
> then the series (17) represents $g$: it converges to $g(x)$ at each point $0 < x < a$ where $g$ is continuous, and to $\frac12\big(g(x+) + g(x-)\big)$ at a jump. Conversely, if (17) holds with a series that may be integrated term by term, its coefficients must be (18).
>
> *Powers: 2.5, Equation (18); Exercises 2.5.10–12*

^thm-21-3

> [!proof]+ Proof
> *Powers gives this as a sketch, in Exercises 2.5.10–12.*
>
> **The coefficients are forced (Exercise 10b).** Multiply (17) by $\sin(\lambda_mx)$ and integrate from $0$ to $a$ term by term. By [[§21 Example꞉ Different Boundary Conditions#^prop-21-2|Proposition §21.2]] every term vanishes except $n = m$, which gives $b_m\cdot\frac a2$. So $b_m = \frac2a\int_0^ag(x)\sin(\lambda_mx)\,dx$.
>
> **The series converges to $g$ (Exercises 11–12).** Extend $g$ to $0 < x < 2a$ by reflection about $x = a$:
>
> $$
> G(x) = g(x), \quad 0 < x < a; \qquad G(x) = g(2a - x), \quad a < x < 2a .
> $$
>
> $G$ is sectionally smooth on $0 < x < 2a$, so its Fourier sine series on that interval, with period $4a$ and half-period $2a$ ([[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Definition §7.4]]),
>
> $$
> G(x) \sim \sum_{N=1}^\infty B_N\sin\Big(\frac{N\pi x}{2a}\Big), \qquad B_N = \frac2{2a}\int_0^{2a}G(x)\sin\Big(\frac{N\pi x}{2a}\Big)dx ,
> $$
>
> converges to $G(x)$ at each continuity point and to the midpoint of the jump otherwise ([[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]]). Split the integral at $a$ and substitute $x = 2a - y$ in the second half. Since $\sin\big(N\pi - \frac{N\pi y}{2a}\big) = -(-1)^N\sin\frac{N\pi y}{2a}$,
>
> $$
> \int_a^{2a}g(2a - x)\sin\Big(\frac{N\pi x}{2a}\Big)dx = -(-1)^N\int_0^ag(y)\sin\Big(\frac{N\pi y}{2a}\Big)dy ,
> $$
>
> and therefore
>
> $$
> B_N = \frac1a\big(1 - (-1)^N\big)\int_0^ag(x)\sin\Big(\frac{N\pi x}{2a}\Big)dx = \begin{cases} 0, & N \text{ even}, \\ \dfrac2a\displaystyle\int_0^ag(x)\sin\Big(\frac{N\pi x}{2a}\Big)dx, & N \text{ odd} . \end{cases}
> $$
>
> Only odd $N = 2n - 1$ survive, and for them $B_{2n-1} = b_n$ and $\frac{N\pi x}{2a} = \lambda_nx$. So for $0 < x < a$, where $G = g$, the convergent sine series of $G$ is exactly the series (17), and its sum is $g(x)$ (or the average at a jump).

^pf-21-3

*Uses:* [[§21 Example꞉ Different Boundary Conditions#^prop-21-2|§21.2]], [[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Def. §7.4]], [[§8 Convergence of Fourier Series#^thm-8-1|§8.1]]

> [!remark]- Connections
> - Proposition §21.2 and formula (18) say that $\{\sin\lambda_nx\}$ is an orthogonal set in the inner product $\langle f, g\rangle = \int_0^af g\,dx$ and that $b_n = \langle g, \phi_n\rangle/\langle\phi_n, \phi_n\rangle$ is the coordinate of $g$ along $\phi_n$: [[§46 Inner Product Spaces#^thm-46-2|235 Thm. §46.2]]. Theorem §21.3 adds that these coordinates reconstruct $g$, a completeness statement; the general version for Sturm–Liouville eigenfunctions is [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]].

> [!theorem] Theorem §21.4: Solution of the Fixed–Insulated Problem
> If $f$ is sectionally smooth, the solution of (1)–(4) is
>
> $$
> u(x, t) = T_0 + \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt), \qquad \lambda_n = \frac{(2n - 1)\pi}{2a} , \qquad (19)
> $$
>
> with $b_n$ given by (18) for $g(x) = f(x) - T_0$. The term $T_0$ is the steady-state solution; it is not part of the separation-of-variables solution.
>
> *Powers: 2.5, Equations (16)–(19)*

^thm-21-4

> [!proof]+ Proof
> By [[§21 Example꞉ Different Boundary Conditions#^thm-21-1|Theorem §21.1]] and superposition ([[§19 Example꞉ Fixed End Temperatures#^thm-19-4|Theorem §19.4]]), (16) satisfies (5)–(6) for any coefficients; the convergence for $t > 0$ and term-by-term differentiation are justified as in [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]], since again $|b_n| \le \frac2a\int_0^a|g|$ and $\sum\lambda_n^2e^{-\lambda_n^2kt_0} < \infty$. By [[§21 Example꞉ Different Boundary Conditions#^thm-21-3|Theorem §21.3]] the coefficients (18) make $w(x, 0) = g(x)$. Then $u = T_0 + w$ satisfies (1)–(4), because $T_0$ satisfies (1)–(3) and $w$ absorbs the initial condition.

^pf-21-4

*Uses:* [[§21 Example꞉ Different Boundary Conditions#^thm-21-1|§21.1]], [[§21 Example꞉ Different Boundary Conditions#^thm-21-3|§21.3]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-4|§19.4]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|§19.5]]

> [!example] Example §21.1: Initial Temperature Constant
> Find the solution of (1)–(4) with the initial condition $u(x, 0) = T_1$, $0 < x < a$.
>
> Then $g(x) = T_1 - T_0$ on $0 < x < a$, and by (18), using $\cos(\lambda_na) = \cos\big((2n - 1)\frac\pi2\big) = 0$,
>
> $$
> b_n = \frac2a(T_1 - T_0)\int_0^a\sin(\lambda_nx)\,dx = \frac2a(T_1 - T_0)\,\frac{1 - \cos(\lambda_na)}{\lambda_n} = \frac2a(T_1 - T_0)\,\frac{2a}{(2n - 1)\pi} = (T_1 - T_0)\frac4{\pi(2n - 1)} .
> $$
>
> Therefore the complete solution with initial condition $u(x, 0) = T_1$ is
>
> $$
> u(x, t) = T_0 + (T_1 - T_0)\frac4\pi\sum_{n=1}^\infty\frac1{2n - 1}\sin(\lambda_nx)\exp(-\lambda_n^2kt) . \qquad (20)
> $$
>
> The rod, initially at $T_1$ throughout, cools (or warms) through its left end toward $T_0$. For large $t$ the first term dominates: $u - T_0 \approx (T_1 - T_0)\frac4\pi\sin\frac{\pi x}{2a}e^{-\pi^2kt/4a^2}$, which decays more slowly than the slowest mode $e^{-\pi^2kt/a^2}$ of [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]]: with only one end open to the reservoir, heat has twice as far to travel.
>
> *Powers: 2.5, Example*

^ex-21-1

![[m341-21-1.svg]]
*Example §21.1 with $T_0 = 0$, $T_1 = 100$: $u(x, t)$ at $kt/a^2 = 0.001$, $0.01$, $0.1$, $1$. The fixed end $x = 0$ pulls the temperature down at once, while at the insulated end $x = a$ every profile meets the wall with zero slope; at $kt/a^2 = 1$ only the first mode is left, $u(a, t) \approx \frac{400}\pi e^{-\pi^2/4} \approx 10.8$.*

## Summary of Separation of Variables

After three major examples the method used to solve linear boundary value–initial value problems can be outlined. So far only homogeneous partial differential equations have appeared, but a nonhomogeneity that is independent of $t$ can be treated by the same technique.

> [!remark] Remark: Method — Summary of Separation of Variables
> 1. **Prepare.** If the partial differential equation or a boundary condition or both are not homogeneous, first find a function $v(x)$, independent of $t$, that satisfies the partial differential equation and the boundary conditions. Since $v$ does not depend on $t$, the partial differential equation applied to $v$ becomes an ordinary differential equation, and finding $v$ is a two-point boundary value problem. Determine the initial value–boundary value problem satisfied by the "transient solution" $w(x, t) = u(x, t) - v(x)$. It must be a **homogeneous problem**: the partial differential equation and the boundary conditions (but not usually the initial condition) are satisfied by the constant function $0$.
> 2. **Separate.** Assuming that $w(x, t) = \phi(x)T(t)$, with neither factor $0$, separate the partial differential equation into two ordinary differential equations, one for $\phi(x)$ and one for $T(t)$, linked by the separation constant $-\lambda^2$. Reduce the boundary conditions to conditions on $\phi$ alone.
> 3. **Solve.** Solve the eigenvalue problem for $\phi$: find the values of $\lambda^2$ for which it has nonzero solutions, and label the eigenfunctions and eigenvalues $\phi_n(x)$ and $\lambda_n^2$. Solve the ordinary differential equation for the time factors $T_n(t)$.
> 4. **Combine and satisfy the remaining condition.** Form the general solution of the homogeneous problem as a sum of constant multiples of the product solutions, $w(x, t) = \sum c_n\phi_n(x)T_n(t)$. Choose the $c_n$ so that the initial condition is satisfied. This may or may not be a routine Fourier series problem; if not, an orthogonality principle must be used to determine the coefficients ([[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]], [[§24 Expansion in Series of Eigenfunctions#^prop-24-1|Proposition §24.1]]).
> 5. **Check.** Form the solution of the original problem, $u(x, t) = v(x) + w(x, t)$, and check that all conditions are satisfied.
>
> The same steps, with more detail on each, are [[§19 Example꞉ Fixed End Temperatures#^rem-19-1|Remark: Method — The Steady-State/Transient Split]] and [[§19 Example꞉ Fixed End Temperatures#^rem-19-2|Remark: Method — Separation of Variables, Step by Step]].

^rem-21-1

## Course Examples

> [!example] Example §21.2: A Prescribed Flux at the Insulated End
> Solve $u_{xx} = \frac1ku_t$, $0 < x < a$, $t > 0$, with $u(0, t) = T$, $u_x(a, t) = A$, $u(x, 0) = f(x)$.
>
> **Step 1, steady state.** $v'' = 0$, $v(0) = T$, $v'(a) = A$: $v(x) = Ax + T$.
>
> **Step 2, transient.** $w = u - v$ satisfies $w_{xx} = \frac1kw_t$, $w(0, t) = 0$, $w_x(a, t) = 0$, $w(x, 0) = f(x) - Ax - T = g(x)$: the problem (5)–(7) again. (The flux $A$ is absorbed by the sloped steady state; for $A > 0$, heat flows steadily in at $x = a$ and out at $x = 0$.)
>
> **Step 3, separation.** $w = \phi(x)T(t)$ gives $\frac{\phi''}\phi = \frac{T'}{kT} = p$, with $\phi(0) = 0$, $\phi'(a) = 0$. By Theorem §21.1, $p_n = -\lambda_n^2$, $\lambda_n = (2n - 1)\pi/2a$, $\phi_n = \sin(\lambda_nx)$, and $w_n(x, t) = \sin(\lambda_nx)e^{-\lambda_n^2kt}$.
>
> **Step 4, coefficients.** $w = \sum c_nw_n$ and $g(x) = w(x, 0) = \sum c_n\sin(\lambda_nx)$. "It looks like a Fourier series", but the frequencies are odd multiples of $\pi/2a$; by the calculation lemma (Proposition §21.2: orthogonality, and $\int_0^a\sin^2(\lambda_nx)\,dx = a/2$),
>
> $$
> c_n = \frac2a\int_0^ag(x)\sin\Big(\frac{(2n - 1)\pi x}{2a}\Big)dx .
> $$
>
> **Step 5.** $u(x, t) = Ax + T + \sum_{n=1}^\infty c_n\sin(\lambda_nx)e^{-\lambda_n^2kt}$.
>
> *Source: 341 lectures 9.26, 10.1*

^ex-21-2

> [!example] Example §21.3: A Heat Source with Fixed and Insulated Ends
> Solve
>
> $$
> \frac{\partial^2u}{\partial x^2} + K = \frac{\partial u}{\partial t}, \quad 0 < x < a,\ t > 0; \qquad u(x, 0) = -\frac K2x^2; \qquad u(0, t) = T, \quad \frac{\partial u}{\partial x}(a, t) = 0 .
> $$
>
> **(a)** By [[§18 Steady-State Temperatures#^ex-18-4|Example §18.4]], $v(x) = -\frac12Kx^2 + Kax + T$, and $w = u - v$ satisfies
>
> $$
> w_{xx} = w_t; \qquad w(x, 0) = -\tfrac K2x^2 - v(x) = -Kax - T; \qquad w(0, t) = 0, \quad w_x(a, t) = 0 .
> $$
>
> **(b) Basic solutions.** $\frac{\phi''}\phi = \frac{T'}T = p$, $\phi(0) = 0$, $\phi'(a) = 0$. By Theorem §21.1 (with $k = 1$): $\phi_n = \sin(\lambda_nx)$, $p = -\lambda_n^2$, $\lambda_n = (2n - 1)\pi/2a$, $T_n = e^{-\lambda_n^2t}$, and
>
> $$
> w_n(x, t) = e^{-[(2n - 1)\pi/2a]^2t}\sin\Big(\frac{(2n - 1)\pi x}{2a}\Big) .
> $$
>
> **(c) Coefficients.** $w = \sum a_nw_n$ with $a_n = \frac2a\int_0^a(-Kax - T)\sin(\lambda_nx)\,dx$. Using $\cos(\lambda_na) = 0$ and $\sin(\lambda_na) = \sin\big((2n - 1)\frac\pi2\big) = (-1)^{n+1}$:
>
> $$
> \int_0^a\sin(\lambda_nx)\,dx = \frac{1 - \cos(\lambda_na)}{\lambda_n} = \frac1{\lambda_n}, \qquad \int_0^ax\sin(\lambda_nx)\,dx = \Big[-\frac{x\cos(\lambda_nx)}{\lambda_n}\Big]_0^a + \frac{\sin(\lambda_na)}{\lambda_n^2} = \frac{(-1)^{n+1}}{\lambda_n^2} .
> $$
>
> So
>
> $$
> a_n = \frac2a\Big(-Ka\frac{(-1)^{n+1}}{\lambda_n^2} - \frac T{\lambda_n}\Big) = \frac{8a^2K(-1)^n}{(2n - 1)^2\pi^2} - \frac{4T}{(2n - 1)\pi} ,
> $$
>
> and
>
> $$
> u(x, t) = -\frac12Kx^2 + Kax + T + \sum_{n=1}^\infty\Big(\frac{8a^2K(-1)^n}{(2n - 1)^2\pi^2} - \frac{4T}{(2n - 1)\pi}\Big)e^{-\lambda_n^2t}\sin(\lambda_nx) .
> $$
>
> *Source: 341 HW 5, Problem 3*

^ex-21-3
