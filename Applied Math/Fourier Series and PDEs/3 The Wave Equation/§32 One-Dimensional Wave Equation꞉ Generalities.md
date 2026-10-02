---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: 32
powers: "3.4"
aliases: ["Powers 3.4"]
tags: [fourier-series-and-pdes, math341]
---
← [[§31 d'Alembert's Solution]] · ↑ [[· 3 The Wave Equation]] · [[§33★ Estimation of Eigenvalues]] →

*Powers, Section 3.4 · MAT 341 lecture 11.5 · HW 10 · Practice Midterm 2.*

This section does for the wave equation what [[§25 Generalities on the Heat Conduction Problem|§25]] (Powers 2.9) did for heat: it treats a string with nonuniform properties, $(s(x)u_x)_x = p(x)u_{tt}/c^2$, and general boundary conditions of the third kind. The solution is split into an equilibrium solution $v(x)$, which absorbs the nonhomogeneous boundary conditions and is the same as the steady state of the heat problem, plus a part $w$ that is a series of eigenfunctions of a regular Sturm–Liouville problem. Unlike the heat problem, nothing decays: $u$ has no limit as $t \to \infty$, and since the eigenvalues of a nonuniform string are in general not multiples of one another, the motion is not even periodic, and the sound is not musical. The examples add the course's generalizations: nonhomogeneous boundary conditions, a constant external force, and damping.

## The Generalized Problem

> [!definition] Definition §32.1: The Generalized One-Dimensional Wave Problem
> The initial value–boundary value problem for a generalized one-dimensional wave equation, homogeneous and free of $u$, is
>
> $$
> \begin{aligned}
> &\frac{\partial}{\partial x}\Big(s(x)\frac{\partial u}{\partial x}\Big) = \frac{p(x)}{c^2}\frac{\partial^2 u}{\partial t^2}, && l < x < r, \quad 0 < t, && (1) \\
> &\alpha_1u(l, t) - \alpha_2\frac{\partial u}{\partial x}(l, t) = c_1, && 0 < t, && (2) \\
> &\beta_1u(r, t) + \beta_2\frac{\partial u}{\partial x}(r, t) = c_2, && 0 < t, && (3) \\
> &u(x, 0) = f(x), && l < x < r, && (4) \\
> &\frac{\partial u}{\partial t}(x, 0) = g(x), && l < x < r . && (5)
> \end{aligned}
> $$
>
> The functions $s(x)$ and $p(x)$ are positive for $l \le x \le r$ (they represent physical properties), $s$, $s'$ and $p$ are continuous, and $s$ and $p$ have no dimensions. None of the coefficients $\alpha_1, \alpha_2, \beta_1, \beta_2$ is negative.
>
> *Powers: 3.4, Equations (1)–(5)*

^def-32-1

To obtain homogeneous boundary conditions, write $u(x, t) = v(x) + w(x, t)$ as for heat. Neither of the names "steady-state solution" nor "transient solution" is appropriate here: as will be seen, there is no steady state or limiting case, and no part of the solution tends to zero as $t \to \infty$. Nevertheless $v$ represents an equilibrium, and the split is a useful device.

> [!definition] Definition §32.2: Equilibrium Solution
> The **equilibrium solution** of (1)–(3) is the function $v(x)$ satisfying
>
> $$
> (sv')' = 0, \quad l < x < r, \qquad \alpha_1v(l) - \alpha_2v'(l) = c_1, \qquad \beta_1v(r) + \beta_2v'(r) = c_2 .
> $$
>
> It is exactly the steady-state solution of the corresponding heat conduction problem ([[§25 Generalities on the Heat Conduction Problem#^prop-25-1|Proposition §25.1]], Powers 2.9; Powers' Exercise 3.4.2): setting $u_{tt} = 0$ in (1) or $u_t = 0$ in the heat equation $(su_x)_x = pu_t/k$ gives the same problem.
>
> *Powers: 3.4 (text)*

^def-32-2

> [!theorem] Proposition §32.1: The Problem for w
> If $v$ is the equilibrium solution, then $w(x, t) = u(x, t) - v(x)$ satisfies
>
> $$
> \begin{aligned}
> &\frac{\partial}{\partial x}\Big(s(x)\frac{\partial w}{\partial x}\Big) = \frac{p(x)}{c^2}\frac{\partial^2 w}{\partial t^2}, && l < x < r, \quad 0 < t, && (6) \\
> &\alpha_1w(l, t) - \alpha_2\frac{\partial w}{\partial x}(l, t) = 0, \qquad \beta_1w(r, t) + \beta_2\frac{\partial w}{\partial x}(r, t) = 0, && 0 < t, && (7), (8) \\
> &w(x, 0) = f(x) - v(x), \qquad \frac{\partial w}{\partial t}(x, 0) = g(x), && l < x < r . && (9), (10)
> \end{aligned}
> $$
>
> *Powers: 3.4, Equations (6)–(10)*

^prop-32-1

> [!proof]+ Proof
> Since $v$ does not depend on $t$, $w_{tt} = u_{tt}$ and $w_t = u_t$, while $(sw_x)_x = (su_x)_x - (sv')' = (su_x)_x$. So (1) becomes (6). In the boundary conditions, $\alpha_1w(l, t) - \alpha_2w_x(l, t) = [\alpha_1u(l, t) - \alpha_2u_x(l, t)] - [\alpha_1v(l) - \alpha_2v'(l)] = c_1 - c_1 = 0$, and likewise at $r$. Finally $w(x, 0) = f(x) - v(x)$ and $w_t(x, 0) = u_t(x, 0) = g(x)$.

^pf-32-1

*Uses:* [[§32 One-Dimensional Wave Equation꞉ Generalities#^def-32-1|Def. §32.1]], [[§32 One-Dimensional Wave Equation꞉ Generalities#^def-32-2|Def. §32.2]]

## Separation of Variables

The equation and boundary conditions for $w$ are homogeneous and linear, so try $w(x, t) = \phi(x)T(t)$. In the usual way ($\frac{(s\phi')'}{p\phi} = \frac{T''}{c^2T} = -\lambda^2$) the factors must satisfy

$$
T'' + c^2\lambda^2T = 0, \quad 0 < t, \qquad (11) \qquad\qquad (s(x)\phi')' + \lambda^2p(x)\phi = 0, \quad l < x < r, \qquad (12)
$$

$$
\alpha_1\phi(l) - \alpha_2\phi'(l) = 0, \qquad (13) \qquad\qquad \beta_1\phi(r) + \beta_2\phi'(r) = 0 . \qquad (14)
$$

The eigenvalue problem (12)–(14) is a regular Sturm–Liouville problem, because of the assumptions on $s$, $p$ and the coefficients. By [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] and [[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]] it has infinitely many nonnegative eigenvalues $\lambda_1^2 < \lambda_2^2 < \cdots$ and eigenfunctions $\phi_1, \phi_2, \ldots$ with the orthogonality property

$$
\int_l^r\phi_n(x)\phi_m(x)p(x)\,dx = 0, \qquad n \ne m .
$$

The solution of (11) is $T_n(t) = a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)$. So the frequencies of vibration that occur are $\lambda_nc/2\pi$ cycles per unit time: it is the eigenvalues of (12)–(14) that determine them.

> [!theorem] Theorem §32.2: Solution of the Generalized Wave Problem
> The solution of (1)–(5) is $u(x, t) = v(x) + w(x, t)$, where $v$ is the equilibrium solution and
>
> $$
> w(x, t) = \sum_{n=1}^\infty\phi_n(x)\big(a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big), \qquad (15)
> $$
>
> with $\lambda_n^2$, $\phi_n$ the eigenvalues and eigenfunctions of (12)–(14) and
>
> $$
> a_n = \frac{1}{I_n}\int_l^r\big[f(x) - v(x)\big]\phi_n(x)p(x)\,dx, \qquad (16) \qquad\qquad
> b_n = \frac{1}{I_n\lambda_nc}\int_l^rg(x)\phi_n(x)p(x)\,dx, \qquad (17)
> $$
>
> $$
> I_n = \int_l^r\phi_n^2(x)p(x)\,dx . \qquad (18)
> $$
>
> *Powers: 3.4, Equations (15)–(18)*

^thm-32-2

> [!proof]+ Proof
> *Powers assembles the solution formally, as in [[§30 Solution of the Vibrating String Problem#^thm-30-2|Theorem §30.2]].* Each product $\phi_n(x)T_n(t)$ satisfies (6)–(8), and so does the series (15) by superposition. Its two initial conditions, yet to be satisfied, are (differentiating term by term)
>
> $$
> w(x, 0) = \sum_{n=1}^\infty a_n\phi_n(x) = f(x) - v(x), \qquad \frac{\partial w}{\partial t}(x, 0) = \sum_{n=1}^\infty b_n\lambda_nc\,\phi_n(x) = g(x), \qquad l < x < r .
> $$
>
> Multiply the first equation by $\phi_m(x)p(x)$ and integrate from $l$ to $r$. Integrating term by term, every term with $n \ne m$ vanishes by orthogonality, and the term $n = m$ gives $a_mI_m$:
>
> $$
> a_mI_m = \int_l^r\big[f(x) - v(x)\big]\phi_m(x)p(x)\,dx ,
> $$
>
> which is (16), since $I_m > 0$ ($p > 0$ and $\phi_m \not\equiv 0$). The same computation with the second equation gives $b_m\lambda_mcI_m = \int_l^rg\phi_mp\,dx$, which is (17) (Powers' Exercise 3.4.1). That these expansions converge to $f - v$ and $g$ is the eigenfunction expansion theorem, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]]: for sectionally smooth $f$ and $g$, at every point of continuity in $l < x < r$. (Powers divides by $\lambda_n$, so he assumes $\lambda_n > 0$. The eigenvalue $0$ occurs only when $\alpha_1 = \beta_1 = 0$, both ends free; its time factor is $a_0 + b_0t$, as in [[§30 Solution of the Vibrating String Problem#^ex-30-4|Example §30.4]].)

^pf-32-2

*Uses:* [[§32 One-Dimensional Wave Equation꞉ Generalities#^prop-32-1|§32.1]], [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]], [[§23 Sturm–Liouville Problems#^thm-23-5|§23.5]], [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|§24.2]]

> [!remark]- Connections
> - The formulas (16)–(18) are the coefficients of an orthogonal expansion in the inner product $\langle\phi, \chi\rangle = \int_l^r\phi\chi p\,dx$, exactly as $c_j = \frac{\mathbf{y}\cdot\mathbf{u}_j}{\mathbf{u}_j\cdot\mathbf{u}_j}$ for an orthogonal basis of $\mathbb{R}^n$, [[§41 Orthogonal Sets#^thm-41-2|235 Thm. §41.2]]. The underlying reason the $\phi_n$ are orthogonal is that the Sturm–Liouville operator is self-adjoint in this inner product, the infinite-dimensional analogue of a symmetric matrix, [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]].

> [!remark] Remark: What the Solution Does as t → ∞
> From the form of $w$:
> 1. **$u(x, t)$ has no limit as $t \to \infty$.** Each term of the series for $w$ is periodic in time and does not die away. What survives is an average: the time average $\frac1T\int_0^Tu(x, t)\,dt$ tends to $v(x)$ as $T \to \infty$ (Powers' Exercise 3.4.4), because $\frac1T\int_0^T\cos(\lambda_nct)\,dt$ and $\frac1T\int_0^T\sin(\lambda_nct)\,dt$ are at most $\frac{2}{\lambda_ncT}$ in absolute value and tend to $0$ (term by term). So the equilibrium solution is the average position of the string.
> 2. **In general the sound is not musical.** Except in very special cases, the eigenvalues $\lambda_n^2$ are not closely related to each other. A sound is musical if, for instance, $\lambda_n = n\lambda_1$, as for the uniform string ([[§30 Solution of the Vibrating String Problem#^prop-30-4|Proposition §30.4]]).
> 3. **In general $u$ is not even periodic in time.** Each term is periodic, but the terms have no common period except in special cases, so the sum is not periodic. One such special case (Powers' Exercise 3.4.7): if $\lambda_n = \alpha(n + \beta)$ with $\beta = j/k$ rational, then every $\lambda_nc$ is a multiple of $\alpha c/k$, and all terms have the common period $2\pi k/(\alpha c)$.

^rem-32-1

> [!remark] Remark: Method — Solving a Wave Problem with Nonhomogeneous Conditions
> To solve a problem of the form (1)–(5), or a uniform string with nonhomogeneous boundary conditions or a constant external force:
> 1. **Equilibrium problem.** Set $u_{tt} = 0$ and solve for $v(x)$ with the original boundary conditions (and the external force, if any).
> 2. **Problem for $w = u - v$.** Write down the equation, the now homogeneous boundary conditions, and the initial conditions $w(x, 0) = f - v$, $w_t(x, 0) = g$.
> 3. **Separate variables** in the $w$ problem and solve the Sturm–Liouville problem (12)–(14) for $\lambda_n$, $\phi_n$; write down the basic solutions $\phi_n(x)T_n(t)$.
> 4. **Coefficients** from (16)–(17), with the weight $p$. For the uniform string ($s = p = 1$, fixed ends) the $w$ problem can instead be solved by d'Alembert's method, [[§31 d'Alembert's Solution#^rem-31-3|Remark: Method — d'Alembert's Method]].
> 5. **Answer** $u = v + w$.

^rem-32-2

> [!example] Example §32.1: A Moving End Held at a New Position
> Solve
>
> $$
> u_{tt} = u_{xx}, \quad 0 < x < \pi; \qquad u(0, t) = 0, \quad u(\pi, t) = \pi; \qquad u(x, 0) = \sin x + x, \quad u_t(x, 0) = \sin x .
> $$
>
> **(a) Equilibrium.** $v'' = 0$, $v(0) = 0$, $v(\pi) = \pi$, so $v(x) = x$.
>
> **(b) Problem for $w = u - v$.** $w_{tt} = w_{xx}$, $w(0, t) = 0$, $w(\pi, t) = 0$, $w(x, 0) = \sin x + x - x = \sin x$, $w_t(x, 0) = \sin x$.
>
> **(c) Basic solutions.** As in [[§30 Solution of the Vibrating String Problem#^ex-30-2|Example §30.2]] (with $c = 1$), $\phi_n = \sin(nx)$ and $w_n = \sin(nx)\big[a_n\cos(nt) + b_n\sin(nt)\big]$.
>
> **(d) Coefficients.** $a_n = \frac2\pi\int_0^\pi\sin x\sin(nx)\,dx$ is $1$ for $n = 1$ and $0$ otherwise; $b_n = \frac{2}{n\pi}\int_0^\pi\sin x\sin(nx)\,dx$ is also $1$ for $n = 1$ and $0$ otherwise. So
>
> $$
> w(x, t) = \sin x\,(\cos t + \sin t), \qquad u(x, t) = x + \sin x\,(\cos t + \sin t) .
> $$
>
> **(e) d'Alembert's form.** $G(x) = \int_0^x\sin y\,dy = 1 - \cos x$, which is already even and $2\pi$-periodic, and $\bar f_o(x) = \sin x$. With $A = -1$, $\bar G_e + A = -\cos x$, so $\psi(x) = \frac12(\sin x - \cos x)$ and $\phi(x) = \frac12(\sin x + \cos x)$, and
>
> $$
> w = \psi(x + t) + \phi(x - t) = \frac12\big[\sin(x + t) + \sin(x - t)\big] + \frac12\big[\cos(x - t) - \cos(x + t)\big] = \sin x\cos t + \sin x\sin t ,
> $$
>
> the same as (d) by the sum-to-product identities. The string oscillates forever about its equilibrium position $v(x) = x$, the straight line to the raised end, with period $2\pi$; it never settles there.
>
> *Source: 341 Practice Midterm 2, Q4*

^ex-32-1

> [!example] Example §32.2: A String under a Constant Force
> Solve
>
> $$
> u_{tt} = u_{xx} - F, \quad 0 < x < a; \qquad u(0, t) = u(a, t) = 0; \qquad u(x, 0) = \frac F2x^2, \quad u_t(x, 0) = 0,
> $$
>
> with $F$ a constant (a uniform downward force, as gravity in [[§29 The Vibrating String#^thm-29-1|Theorem §29.1]] with $c = 1$, $F = g$).
>
> **(a) Equilibrium.** $0 = v'' - F$, $v(0) = v(a) = 0$: by [[§29 The Vibrating String#^ex-29-2|Example §29.2]], $v(x) = \frac F2(x^2 - ax)$.
>
> **(b) Problem for $w = u - v$.** Since $v'' = F$, $w_{tt} = u_{tt} = u_{xx} - F = w_{xx} + v'' - F = w_{xx}$; the force has been absorbed. The conditions are $w(0, t) = w(a, t) = 0$, $w(x, 0) = \frac F2x^2 - \frac F2(x^2 - ax) = \frac{aF}{2}x$, $w_t(x, 0) = 0$.
>
> **(c) d'Alembert's method** ($c = 1$). With $g \equiv 0$, $G \equiv 0$ and $A = 0$: $\psi = \phi = \frac12\bar f_o$, where $\bar f_o$ is the odd $2a$-periodic extension of $f(x) = \frac{aF}{2}x$. Its sine coefficients are
>
> $$
> a_n = \frac2a\cdot\frac{aF}{2}\int_0^ax\sin\frac{n\pi x}{a}\,dx = F\Big[-\frac{ax}{n\pi}\cos\frac{n\pi x}{a}\Big]_0^a = \frac{(-1)^{n+1}Fa^2}{n\pi}
> $$
>
> (the remaining integral $\frac{a}{n\pi}\int_0^a\cos\frac{n\pi x}{a}\,dx$ vanishes). So
>
> $$
> \psi(x) = \phi(x) = \sum_{n=1}^\infty\frac{(-1)^{n+1}Fa^2}{2n\pi}\sin\frac{n\pi x}{a}, \qquad
> w(x, t) = \sum_{n=1}^\infty\frac{(-1)^{n+1}Fa^2}{2n\pi}\Big[\sin\frac{n\pi(x + t)}{a} + \sin\frac{n\pi(x - t)}{a}\Big] .
> $$
>
> **(d)** $u(x, t) = \frac F2(x^2 - ax) + w(x, t)$.
>
> The initial shape $\frac F2x^2$ does not vanish at $x = a$, so $\bar f_o$ is a sawtooth with jumps at odd multiples of $a$, and its coefficients decay only like $1/n$. Again $u$ oscillates about the sagging equilibrium $v$ and does not approach it.
>
> *Source: 341 HW 10, Problem 3*

^ex-32-2

> [!example] Example §32.3: The Damped String
> Solve the string in a resisting medium ([[§29 The Vibrating String#^prop-29-3|Proposition §29.3]])
>
> $$
> u_{tt} = c^2u_{xx} - ku_t, \quad 0 < x < a; \qquad u(0, t) = u(a, t) = 0; \qquad u(x, 0) = f(x), \quad u_t(x, 0) = g(x),
> $$
>
> with $k > 0$. This equation is not of the form (1), but separation of variables still works.
>
> **Separation.** $u_n = \phi(x)T(t)$ gives $\phi(T'' + kT') = c^2\phi''T$, so $\dfrac{\phi''}{\phi} = \dfrac{T'' + kT'}{c^2T} = p$. The problem $\phi'' = p\phi$, $\phi(0) = \phi(a) = 0$ is the familiar one: $p = -(n\pi/a)^2$, $\phi_n = \sin(n\pi x/a)$. Then
>
> $$
> T'' + kT' + \omega_n^2T = 0, \qquad \omega_n = \frac{cn\pi}{a} ,
> $$
>
> the equation of a damped oscillator. Trying $T = e^{zt}$ gives $z^2 + kz + \omega_n^2 = 0$, $z = -\frac k2 \pm \sqrt{\frac{k^2}{4} - \omega_n^2}$, and three cases ([[§19 Mechanical and Electrical Vibrations#^thm-19-3|331 Thm. §19.3]]):
> - $\frac k2 > \omega_n$ (overdamped): $T_n = e^{-kt/2}\big(A\cosh(\mu_nt) + B\sinh(\mu_nt)\big)$, $\mu_n = \sqrt{k^2/4 - \omega_n^2}$; no vibration, only decay.
> - $\frac k2 = \omega_n$ (critically damped): $T_n = e^{-kt/2}(A + Bt)$; no vibration.
> - $\frac k2 < \omega_n$ (underdamped): $T_n = e^{-kt/2}\big(A\cos(\mu_nt) + B\sin(\mu_nt)\big)$, $\mu_n = \sqrt{\omega_n^2 - k^2/4}$; vibrating decay.
>
> **General solution for small $k$.** If $\frac k2 < \frac{c\pi}{a}$, every mode is underdamped and
>
> $$
> u(x, t) = \sum_{n=1}^\infty\sin\frac{n\pi x}{a}\,e^{-kt/2}\big(A_n\cos(\mu_nt) + B_n\sin(\mu_nt)\big),
> \qquad A_n = \frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,dx, \qquad -\frac k2A_n + \mu_nB_n = \frac2a\int_0^ag(x)\sin\frac{n\pi x}{a}\,dx .
> $$
>
> The frequencies $\mu_n/2\pi = \frac{1}{2\pi}\sqrt{(cn\pi/a)^2 - k^2/4}$ are not an arithmetic sequence, so $u$ is not periodic, and $u \to 0$ as $t \to \infty$ (Powers' Exercise 3.2.10). For larger $k$ the lowest modes are overdamped while the high modes still vibrate.
>
> **A single mode.** For $c = 1$, $a = \pi$, $u(x, 0) = \sin(nx)$, $u_t(x, 0) = 0$, only the $n$th mode is present: $u = T(t)\sin(nx)$ with $T(0) = 1$, $T'(0) = 0$. Let $\Delta_n = \sqrt{|k^2/4 - n^2|}$.
> - $\frac k2 < n$: $T = e^{-kt/2}(A\cos\Delta_nt + B\sin\Delta_nt)$ with $A = 1$ and $T'(0) = -\frac k2A + \Delta_nB = 0$, so $u = e^{-kt/2}\Big(\cos(\Delta_nt) + \dfrac{k}{2\Delta_n}\sin(\Delta_nt)\Big)\sin(nx)$.
> - $\frac k2 = n$: $T = e^{-kt/2}(A + Bt)$ with $A = 1$, $-\frac k2 + B = 0$: $u = e^{-kt/2}\big(1 + \frac k2t\big)\sin(nx)$.
> - $\frac k2 > n$: $T = e^{-kt/2}(A\cosh\Delta_nt + B\sinh\Delta_nt)$ with $A = 1$, $B = \frac{k}{2\Delta_n}$: $u = e^{-kt/2}\Big(\cosh(\Delta_nt) + \dfrac{k}{2\Delta_n}\sinh(\Delta_nt)\Big)\sin(nx)$.
>
> In every case the shape $\sin(nx)$ is kept and only the amplitude changes, as for a standing wave.
>
> *Source: 341 lecture 11.5; 341 Practice Midterm 2, Q9*

^ex-32-3

> [!example] Example §32.4: A Nonuniform String That Is Musical
> Solve $\dfrac{\partial}{\partial x}\Big(x\dfrac{\partial u}{\partial x}\Big) = \dfrac{1}{c^2x}\dfrac{\partial^2u}{\partial t^2}$, $1 < x < 2$, with $u(1, t) = u(2, t) = 0$, $u(x, 0) = f(x)$, $u_t(x, 0) = g(x)$. Here $s(x) = x$ and $p(x) = 1/x$, both positive on $[1, 2]$.
>
> **Eigenvalue problem.** By (12)–(14), $(x\phi')' + \lambda^2\frac1x\phi = 0$, $\phi(1) = \phi(2) = 0$. Substitute $\xi = \ln x$, so that $x\frac{d}{dx} = \frac{d}{d\xi}$: then $x\phi' = \frac{d\phi}{d\xi}$ and $(x\phi')' = \frac1x\frac{d^2\phi}{d\xi^2}$, and the equation becomes
>
> $$
> \frac{d^2\phi}{d\xi^2} + \lambda^2\phi = 0, \qquad 0 < \xi < \ln 2, \qquad \phi = 0 \text{ at } \xi = 0 \text{ and } \xi = \ln 2 .
> $$
>
> Its eigenvalues and eigenfunctions are those of the uniform string of length $\ln 2$:
>
> $$
> \lambda_n = \frac{n\pi}{\ln 2}, \qquad \phi_n(x) = \sin\Big(\frac{n\pi\ln x}{\ln 2}\Big), \qquad n = 1, 2, \ldots ;
> $$
>
> in particular $\lambda_1^2 = (\pi/\ln 2)^2 \approx 20.5423$.
>
> **Coefficients.** The weight is $p(x) = 1/x$, and with $\xi = \ln x$, $d\xi = dx/x$,
>
> $$
> I_n = \int_1^2\sin^2\Big(\frac{n\pi\ln x}{\ln 2}\Big)\frac{dx}{x} = \int_0^{\ln 2}\sin^2\Big(\frac{n\pi\xi}{\ln 2}\Big)d\xi = \frac{\ln 2}{2} .
> $$
>
> The equilibrium solution is $v \equiv 0$, so by (16)–(17)
>
> $$
> u(x, t) = \sum_{n=1}^\infty\phi_n(x)\big(a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big), \qquad
> a_n = \frac{2}{\ln 2}\int_1^2f(x)\phi_n(x)\frac{dx}{x}, \qquad b_n = \frac{2}{\ln 2\,\lambda_nc}\int_1^2g(x)\phi_n(x)\frac{dx}{x} .
> $$
>
> **Musical.** Here $\lambda_n = n\lambda_1$, so the frequencies $\lambda_nc/2\pi = nc/(2\ln 2)$ are multiples of the fundamental, and $u$ is periodic with period $2\ln 2/c$: one of the "very special cases" of Remark: What the Solution Does. The reason is visible in the substitution: in the variable $\xi = \ln x$ the equation is $u_{\xi\xi} = u_{tt}/c^2$, a uniform string in disguise. The first eigenvalue of this problem is estimated by Rayleigh's method in [[§33★ Estimation of Eigenvalues#^ex-33-2|Example §33.2]].
>
> *Powers: 3.5, Example 2 (the eigenvalue problem); the wave problem is added*

^ex-32-4
