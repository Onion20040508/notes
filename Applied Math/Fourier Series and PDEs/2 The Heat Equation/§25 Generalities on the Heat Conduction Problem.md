---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 25
powers: "2.9"
aliases: ["Powers 2.9"]
tags: [fourier-series-and-pdes, math341]
---
← [[§24 Expansion in Series of Eigenfunctions]] · ↑ [[· 2 The Heat Equation]] · [[§26 Semi-Infinite Rod]] →

*Powers, Section 2.9 · MAT 341 lectures 10.17, 10.24 · HW 7 · Practice Midterm 2.*

This section assembles the methods of the chapter into one procedure for a fairly general heat conduction problem: a rod with insulated lateral surface whose conductivity, density and specific heat may vary along its length, with any of the three types of boundary condition at either end. The steady state is found from an explicit formula, the transient satisfies homogeneous boundary conditions, separation of variables leads to a regular Sturm–Liouville problem ([[§23 Sturm–Liouville Problems|§23]]), and the initial condition is met by an eigenfunction expansion ([[§24 Expansion in Series of Eigenfunctions|§24]]). From the series one reads off the physics: the temperature tends to the steady state, every discontinuity of the initial temperature is smoothed out instantly, and for large times the deviation from the steady state has the shape of the first eigenfunction, which never changes sign.

## The Problem and Its Steady State

> [!definition] Definition §25.1: The General Heat Conduction Problem
> The temperature $u(x, t)$ in a rod $l < x < r$ whose lateral surface is insulated, in which no heat is generated and whose material properties vary with position, satisfies
>
> $$
> \begin{aligned}
> \frac{\partial}{\partial x}\Big(\kappa(x)\frac{\partial u}{\partial x}\Big) &= \rho(x)c(x)\frac{\partial u}{\partial t}, && l < x < r, \quad 0 < t, && (1) \\
> \alpha_1u(l, t) - \alpha_2\frac{\partial u}{\partial x}(l, t) &= c_1, && t > 0, && (2) \\
> \beta_1u(r, t) + \beta_2\frac{\partial u}{\partial x}(r, t) &= c_2, && t > 0, && (3) \\
> u(x, 0) &= f(x), && l < x < r. && (4)
> \end{aligned}
> $$
>
> Here $\kappa$ is the thermal conductivity, $\rho$ the density and $c$ the specific heat; $\kappa$, $\kappa'$, $\rho$ and $c$ are continuous and positive on $[l, r]$, and $c_1$, $c_2$ are constants. If the temperature at an end is fixed, the coefficient of $\partial u/\partial x$ there is zero; if the end is insulated, the coefficient of $u$ and the right side are zero; if there is convection, both coefficients are positive, with the signs shown. All the $\alpha$'s and $\beta$'s are nonnegative, and **at least one of $\alpha_1$, $\beta_1$ is positive** (the case of two insulated ends is set aside, [[§25 Generalities on the Heat Conduction Problem#^rem-25-1|Remark]] below).
>
> *Powers: 2.9, Eqs. (1)–(4)*

^def-25-1

Equation (1) is the heat equation of [[§17 Derivation and Boundary Conditions#^thm-17-2|Theorem §17.2]] (Eq. (3) there, without generation) before the coefficients are assumed constant.

> [!theorem] Proposition §25.1: The Steady-State Temperature
> Assume $c_1$ and $c_2$ are constants. The steady-state solution $v(x) = \lim_{t \to \infty}u(x, t)$ satisfies the boundary value problem
>
> $$
> \frac{d}{dx}\Big(\kappa(x)\frac{dv}{dx}\Big) = 0, \quad l < x < r, \qquad \alpha_1v(l) - \alpha_2v'(l) = c_1, \qquad \beta_1v(r) + \beta_2v'(r) = c_2 . \qquad (5)\text{–}(7)
> $$
>
> With
>
> $$
> I(x) = \int_l^x \frac{d\xi}{\kappa(\xi)} , \qquad (8)
> $$
>
> this problem has the unique solution $v(x) = A + BI(x)$, where
>
> $$
> \Delta = \alpha_1\Big(\beta_1I(r) + \frac{\beta_2}{\kappa(r)}\Big) + \frac{\alpha_2\beta_1}{\kappa(l)} > 0, \qquad A = \frac{c_1\big(\beta_1I(r) + \beta_2/\kappa(r)\big) + \alpha_2c_2/\kappa(l)}{\Delta}, \qquad B = \frac{\alpha_1c_2 - \beta_1c_1}{\Delta} .
> $$
>
> *Powers: 2.9, Eqs. (5)–(8) and Exercise 2.9.1*

^prop-25-1

> [!proof]+ Proof
> Integrating $(\kappa v')' = 0$ once gives $\kappa v' = B$, a constant, so $v' = B/\kappa$ and, integrating again from $l$, $v = A + BI(x)$ with $A = v(l)$, since $I(l) = 0$. Conversely every such function solves the differential equation. Since $v'(l) = B/\kappa(l)$ and $v'(r) = B/\kappa(r)$, the boundary conditions become the linear system
>
> $$
> \alpha_1A - \frac{\alpha_2}{\kappa(l)}B = c_1, \qquad \beta_1A + \Big(\beta_1I(r) + \frac{\beta_2}{\kappa(r)}\Big)B = c_2 ,
> $$
>
> whose determinant is $\Delta$. (Powers asserts that the problem can be solved when $\alpha_1$ or $\beta_1$ is positive; here is why.) All terms of $\Delta$ are nonnegative, and $I(r) > 0$ because $\kappa > 0$. If $\alpha_1 > 0$: either $\beta_1 > 0$, and then $\alpha_1\beta_1I(r) > 0$, or $\beta_1 = 0$, and then $\beta_2 > 0$ and $\alpha_1\beta_2/\kappa(r) > 0$. If $\alpha_1 = 0$: then $\alpha_2 > 0$ and $\beta_1 > 0$ by assumption, and $\alpha_2\beta_1/\kappa(l) > 0$. So $\Delta > 0$, the system has exactly one solution, and Cramer's rule gives the stated $A$ and $B$. (Substituting them back confirms both equations.)

^pf-25-1

*Uses:* [[§25 Generalities on the Heat Conduction Problem#^def-25-1|Def. §25.1]]

> [!remark] Remark: Two Insulated Ends
> If $\alpha_1 = \beta_1 = 0$, then $\Delta = 0$. With $c_1 = c_2 = 0$ every constant solves (5)–(7), so the boundary value problem does not determine $v$; the right constant comes from conservation of heat, $v = \int_l^r \rho cf\,dx \big/ \int_l^r \rho c\,dx$, the heat-capacity-weighted average of the initial temperature (as for the uniform bar of [[§20 Example꞉ Insulated Bar#^thm-20-2|Theorem §20.2]]). In the eigenvalue problem below, $\lambda^2 = 0$ is then an eigenvalue with eigenfunction $1$, and the solution has the form $u = a_0 + \sum a_n\phi_ne^{-\lambda_n^2kt}$ with $a_0$ that average (Powers' Exercise 2.9.3). If instead nonzero fluxes are prescribed, $-\alpha_2u_x(l, t) = c_1$ and $\beta_2u_x(r, t) = c_2$, a steady state needs $\kappa v' = B$ with $B = -c_1\kappa(l)/\alpha_2 = c_2\kappa(r)/\beta_2$: the heat flowing in at one end must equal the heat flowing out at the other. Otherwise no steady state exists, and the heat content of the rod grows or decreases without bound.

^rem-25-1

## The Transient Problem

> [!definition] Definition §25.2: Dimensionless Coefficients; Transient Temperature
> Let $\bar\kappa$, $\bar\rho$ and $\bar c$ be average values of $\kappa(x)$, $\rho(x)$ and $c(x)$. The dimensionless functions $s(x)$ and $p(x)$ are defined by
>
> $$
> \kappa(x) = \bar\kappa s(x), \qquad \rho(x)c(x) = \bar\rho\bar cp(x) ,
> $$
>
> and $k = \bar\kappa/\bar\rho\bar c$. The **transient temperature** is $w(x, t) = u(x, t) - v(x)$.
>
> *Powers: 2.9 (text)*

^def-25-2

> [!theorem] Proposition §25.2: The Transient Problem
> $w(x, t)$ satisfies the initial value–boundary value problem
>
> $$
> \begin{aligned}
> \frac{\partial}{\partial x}\Big(s(x)\frac{\partial w}{\partial x}\Big) &= \frac1kp(x)\frac{\partial w}{\partial t}, && l < x < r, \quad 0 < t, && (9) \\
> \alpha_1w(l, t) - \alpha_2\frac{\partial w}{\partial x}(l, t) &= 0, && 0 < t, && (10) \\
> \beta_1w(r, t) + \beta_2\frac{\partial w}{\partial x}(r, t) &= 0, && 0 < t, && (11) \\
> w(x, 0) &= f(x) - v(x) = g(x), && l < x < r, && (12)
> \end{aligned}
> $$
>
> which has homogeneous boundary conditions.
>
> *Powers: 2.9, Eqs. (9)–(12)*

^prop-25-2

> [!proof]+ Proof
> By direct computation. Since $v$ does not depend on $t$, $w_t = u_t$, and since $(\kappa v')' = 0$,
>
> $$
> \frac{\partial}{\partial x}\Big(\kappa\frac{\partial w}{\partial x}\Big) = \frac{\partial}{\partial x}\Big(\kappa\frac{\partial u}{\partial x}\Big) - (\kappa v')' = \rho c\frac{\partial u}{\partial t} = \rho c\frac{\partial w}{\partial t} .
> $$
>
> Divide by $\bar\kappa$: the left side becomes $(sw_x)_x$, and the right side $(\bar\rho\bar c/\bar\kappa)\,p\,w_t = \frac1kp\,w_t$. This is (9). At $x = l$, $\alpha_1w - \alpha_2w_x = (\alpha_1u - \alpha_2u_x) - (\alpha_1v - \alpha_2v') = c_1 - c_1 = 0$, which is (10); (11) is the same at $x = r$. Finally $w(x, 0) = u(x, 0) - v(x) = f(x) - v(x)$.

^pf-25-2

*Uses:* [[§25 Generalities on the Heat Conduction Problem#^prop-25-1|§25.1]], [[§25 Generalities on the Heat Conduction Problem#^def-25-2|Def. §25.2]]

## Separation of Variables and the Solution

> [!theorem] Theorem §25.3: Solution of the General Heat Conduction Problem
> Assume $s$, $s'$ and $p$ are continuous on $[l, r]$, $s$ and $p$ are positive there (with $\alpha_1$ or $\beta_1$ positive, as in Definition §25.1), and $f$ is sectionally smooth. Then:
> 1. The eigenvalue problem
>
> $$
> (s\phi')' + \lambda^2p\phi = 0, \quad l < x < r, \qquad \alpha_1\phi(l) - \alpha_2\phi'(l) = 0, \qquad \beta_1\phi(r) + \beta_2\phi'(r) = 0 \qquad (13)\text{–}(15)
> $$
>
> is a regular Sturm–Liouville problem with an infinite number of eigenvalues $0 < \lambda_1^2 < \lambda_2^2 < \cdots$; to each corresponds just one eigenfunction $\phi_n$ (give or take a constant multiplier), and the eigenfunctions are orthogonal with weight $p$.
> 2. The solution of (1)–(4) is
>
> $$
> u(x, t) = v(x) + \sum_{n=1}^\infty a_n\phi_n(x)\exp(-\lambda_n^2kt), \qquad a_n = \frac{\int_l^r g(x)\phi_n(x)p(x)\,dx}{\int_l^r \phi_n^2(x)p(x)\,dx} , \qquad (16)
> $$
>
> with $v$ from Proposition §25.1 and $g = f - v$.
>
> *Powers: 2.9, Eqs. (13)–(16)*

^thm-25-3

> [!proof]+ Proof
> **Separation.** If $w = \phi(x)T(t)$, then (9) becomes $T(s\phi')' = \frac1kp\phi T'$, and dividing by $p\phi T$,
>
> $$
> \frac{(s\phi')'}{p\phi} = \frac{T'}{kT}, \qquad l < x < r, \quad 0 < t .
> $$
>
> A function of $x$ equals a function of $t$ only if both are constant; call the constant $-\lambda^2$ (part 1 shows that it is negative). This separates into $T' + \lambda^2kT = 0$ and $(s\phi')' + \lambda^2p\phi = 0$. The boundary conditions are linear and homogeneous; for instance (10) becomes $[\alpha_1\phi(l) - \alpha_2\phi'(l)]T(t) = 0$, and since $T \equiv 0$ would make $w \equiv 0$, the other factor must be zero. This gives (13)–(15).
>
> **Part 1.** The problem (13)–(15) is (5)–(7) of [[§23 Sturm–Liouville Problems#^def-23-1|Definition §23.1]] with $q = 0$, and $s$, $s'$, $p$ continuous with $s$, $p > 0$, $\alpha$'s and $\beta$'s nonnegative: it is a regular Sturm–Liouville problem. By [[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]] it has infinitely many eigenvalues, all nonnegative ($q = 0$), increasing to $\infty$; by [[§23 Sturm–Liouville Problems#^prop-23-4|Proposition §23.4]] each has one eigenfunction up to a multiple, and by [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] the eigenfunctions are orthogonal with weight $p$. (Powers states that the eigenvalues are positive; here is why $0$ is excluded.) For $\lambda = 0$, $(s\phi')' = 0$ gives $\phi = A + BJ(x)$ with $J(x) = \int_l^x d\xi/s(\xi)$, and the boundary conditions give the system of [[§25 Generalities on the Heat Conduction Problem#^prop-25-1|Proposition §25.1]] with $\kappa$ replaced by $s$ and $c_1 = c_2 = 0$. Its determinant is positive when $\alpha_1$ or $\beta_1$ is positive, so $A = B = 0$, and $0$ is not an eigenvalue.
>
> **Part 2.** For each $n$, $T_n(t) = \exp(-\lambda_n^2kt)$ solves $T' + \lambda_n^2kT = 0$, and $w_n = \phi_n(x)T_n(t)$ satisfies (9)–(11). These are linear homogeneous equations, so any linear combination of solutions is again a solution, and the transient has the form
>
> $$
> w(x, t) = \sum_{n=1}^\infty a_n\phi_n(x)\exp(-\lambda_n^2kt) .
> $$
>
> (Powers takes for granted that the infinite series may be differentiated term by term; here is why it may, for $t \ge t_1 > 0$. The proof of [[§25 Generalities on the Heat Conduction Problem#^thm-25-4|Theorem §25.4]] gives $|a_n\phi_n(x)| \le MG$ and $\lambda_n^2 \ge \gamma n^2$. By the mean value theorem there is a point $\xi_n$ with $|\phi_n'(\xi_n)| = |\phi_n(r) - \phi_n(l)|/(r - l)$, and integrating $(s\phi_n')' = -\lambda_n^2p\phi_n$ from $\xi_n$ gives $|a_ns\phi_n'(x)| \le C(1 + \lambda_n^2)$ on $[l, r]$, with $C$ independent of $n$. Together with $T_n' = -\lambda_n^2kT_n$, the terms of the series for $w$, $w_x$, $(sw_x)_x$ and $w_t$ are all bounded by a constant times $(1 + \lambda_n^2)e^{-\lambda_n^2kt_1}$, which is summable. So all four series converge uniformly by the M-test, and, integrating the differentiated series term by term and using the fundamental theorem of calculus as in the proof of [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]], they are the derivatives of $w$.) The initial condition (12) requires $\sum a_n\phi_n(x) = g(x)$ on $l < x < r$. If $f$, and therefore $g = f - v$, is sectionally smooth, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]] says that this equality holds (except possibly at the finitely many jumps, where the series gives the average) when $a_n$ are the generalized Fourier coefficients of $g$. Finally $u = v + w$.

^pf-25-3

*Uses:* [[§25 Generalities on the Heat Conduction Problem#^prop-25-1|§25.1]], [[§25 Generalities on the Heat Conduction Problem#^prop-25-2|§25.2]], [[§23 Sturm–Liouville Problems#^def-23-1|Def. §23.1]], [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]], [[§23 Sturm–Liouville Problems#^prop-23-4|§23.4]], [[§23 Sturm–Liouville Problems#^thm-23-5|§23.5]], [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|§24.2]], [[§25 Generalities on the Heat Conduction Problem#^thm-25-4|§25.4]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|§19.5]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]

> [!remark]- Connections
> - Finite-dimensional analogue: the system $\mathbf{x}' = -kA\mathbf{x}$ with $A$ real symmetric is solved by expanding in an orthonormal basis of eigenvectors, $\mathbf{x}(t) = \sum c_ie^{-k\mu_it}\mathbf{v}_i$ with $c_i = \mathbf{x}(0)\cdot\mathbf{v}_i$ ([[§31 Homogeneous Linear Systems with Constant Coefficients#^thm-31-2|331 Thm. §31.2]], [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]]). Formula (16) is the same with $A$ replaced by the self-adjoint operator $-\frac1p\frac{d}{dx}s\frac{d}{dx}$ and the boundary conditions ([[§23 Sturm–Liouville Problems#^rem-23-3|Remark in §23]]).

Working from the representation (16), Powers draws three conclusions about the solution.

> [!theorem] Theorem §25.4: Behavior of the Solution
> Let $u$ be given by (16), with $f$ sectionally smooth.
> 1. Since all the $\lambda_n^2$ are positive, $u(x, t)$ tends to $v(x)$ as $t \to \infty$.
> 2. For any $t_1 > 0$, the series for $u(x, t_1)$ converges uniformly in $l \le x \le r$ because of the exponential factors; therefore $u(x, t_1)$ is a continuous function of $x$. Any discontinuity in the initial condition is immediately eliminated.
> 3. For large enough values of $t$,
>
> $$
> u(x, t) \approx v(x) + a_1\phi_1(x)\exp(-\lambda_1^2kt) .
> $$
>
> Because $\phi_1(x)$ is of one sign on $l < x < r$, the graph of this approximation lies either above or below the graph of $v(x)$ but does not cross it (provided $a_1 \ne 0$).
>
> *Powers: 2.9 (text)*

^thm-25-4

> [!proof]- Proof
> *Powers gives this as a sketch* (his Exercise 2.9.2 asks the reader to justify the conclusions). The estimates below use, besides the results cited, two standard facts about regular Sturm–Liouville problems that Powers does not state: the eigenvalues grow at least like $n^2$, $\lambda_n^2 \ge \gamma n^2$ for some $\gamma > 0$ and all large $n$; and the normalized eigenfunctions are uniformly bounded, $|\phi_n(x)| \le MN_n^{1/2}$ with $N_n = \int_l^r \phi_n^2p\,dx$ and $M$ independent of $n$ and $x$. (Both are visible in the examples: for $\sin(n\pi x/a)$, $\lambda_n^2 = n^2\pi^2/a^2$ and $|\phi_n| \le 1 = \sqrt{2/a}\,N_n^{1/2}$.)
>
> **A bound on the coefficients (Bessel).** For each $N$, by orthogonality,
>
> $$
> 0 \le \int_l^r p\Big(g - \sum_{n=1}^N a_n\phi_n\Big)^2dx = \int_l^r pg^2\,dx - 2\sum_{n=1}^N a_n\int_l^r pg\phi_n\,dx + \sum_{n=1}^N a_n^2N_n = \int_l^r pg^2\,dx - \sum_{n=1}^N a_n^2N_n ,
> $$
>
> since $\int pg\phi_n = a_nN_n$. Hence $a_n^2N_n \le G^2 := \int_l^r pg^2\,dx$ for every $n$, and $|a_n\phi_n(x)| \le |a_n|MN_n^{1/2} \le MG$.
>
> **2.** For $t \ge t_1 > 0$ and all $x \in [l, r]$,
>
> $$
> \big|a_n\phi_n(x)e^{-\lambda_n^2kt}\big| \le MG\,e^{-\lambda_n^2kt_1} =: M_n ,
> $$
>
> and $\sum M_n < \infty$ because $e^{-\lambda_n^2kt_1} \le e^{-\gamma kt_1n^2}$ for large $n$. By the Weierstrass M-test ([[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]]) the series converges uniformly on $l \le x \le r$, $t \ge t_1$; each term is continuous, so the sum is continuous ([[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]). In particular $u(\cdot, t_1)$ is continuous even if $f$ jumps.
>
> **1.** Since $\lambda_n^2 \ge \lambda_1^2 > 0$ ([[§25 Generalities on the Heat Conduction Problem#^thm-25-3|Theorem §25.3]]), for $t \ge t_1$, $e^{-\lambda_n^2kt} = e^{-\lambda_n^2kt_1}e^{-\lambda_n^2k(t - t_1)} \le e^{-\lambda_n^2kt_1}e^{-\lambda_1^2k(t - t_1)}$, so
>
> $$
> |u(x, t) - v(x)| \le e^{-\lambda_1^2k(t - t_1)}\sum_{n=1}^\infty M_n \longrightarrow 0 \qquad (t \to \infty) ,
> $$
>
> uniformly in $x$.
>
> **3.** In the same way, using $\lambda_n^2 \ge \lambda_2^2$ for $n \ge 2$,
>
> $$
> \big|u(x, t) - v(x) - a_1\phi_1(x)e^{-\lambda_1^2kt}\big| \le e^{-\lambda_2^2k(t - t_1)}\sum_{n=2}^\infty M_n ,
> $$
>
> which is small compared with the first term, of size $e^{-\lambda_1^2kt}$, because $\lambda_2^2 > \lambda_1^2$ (the eigenvalues are distinct): the ratio is $O(e^{-(\lambda_2^2 - \lambda_1^2)kt})$. (How large $t$ must be depends on the $a_n$ and $\lambda_n$.) By [[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]](b) with $n = 1$, $\phi_1$ has no zeros in $l < x < r$; being continuous, it is of one sign there. So $a_1\phi_1(x)e^{-\lambda_1^2kt}$ has the sign of $a_1\phi_1$ for all $x$, and the approximation stays on one side of $v$.

^pf-25-4

*Uses:* [[§25 Generalities on the Heat Conduction Problem#^thm-25-3|§25.3]], [[§23 Sturm–Liouville Problems#^thm-23-5|§23.5]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], [[§24 Uniform Convergence#^thm-24-2|451 Thm. §24.2]]

> [!remark]- Connections
> - The Bessel step is the finite Bessel inequality for the orthonormal set $\phi_n/N_n^{1/2}$ in the weighted inner product, [[§24 Orthonormal Sets and Bases#^lem-24-2|556 Lem. §24.2]].

> [!remark] Remark: Method — Solving a Heat Problem with Variable Coefficients
> 1. **Steady state.** Solve $(\kappa v')' = 0$ with the boundary conditions (Proposition §25.1); this reduces the problem to one with homogeneous boundary conditions. If the boundary conditions are already homogeneous, $v = 0$.
> 2. **Transient problem.** Write down the problem for $w = u - v$: same equation, homogeneous boundary conditions, initial value $g = f - v$.
> 3. **Basic solutions.** Separate variables, $w = \phi(x)T(t)$, and put the eigenvalue problem for $\phi$ in Sturm–Liouville form ([[§23 Sturm–Liouville Problems#^rem-23-2|Method in §23]]); check that it is regular.
> 4. **Solve the eigenvalue problem**, discussing the separation constant positive, zero and negative; when $sp = 1$, use the substitution $y = \int dx/s$ ([[§23 Sturm–Liouville Problems#^rem-23-5|Method in §23]]). If the eigenvalue equation is transcendental, keep $\lambda_n$ in the answer and locate the roots graphically.
> 5. **Superpose and expand.** $w = \sum a_n\phi_n(x)T_n(t)$; find $a_n$ from $g$ by the generalized Fourier coefficient formula with weight $p$, computing the normalizing integrals $\int p\phi_n^2$. Then $u = v + w$.
>
> When everything is constant and the boundary conditions are of Dirichlet or Neumann type, the solution can be written out explicitly; with Robin conditions or variable coefficients, the $\lambda_n$ and the normalizing integrals generally have to be left in the answer.
>
> *Source: 341 lecture 10.24*

^rem-25-2

## Examples

> [!example] Example §25.1: Neumann and Robin Conditions
> Solve
>
> $$
> \frac{\partial u}{\partial t} = 2\frac{\partial^2u}{\partial x^2}, \quad 0 < x < 2, \qquad \frac{\partial u}{\partial x}(0, t) = 1, \qquad -\frac{\partial u}{\partial x}(2, t) = u(2, t) - 2, \qquad u(x, 0) = x^2 + x - 1 .
> $$
>
> Physically, heat is drawn out through the left end at a constant rate (the flux $-u_x$ there is $-1$, directed out of the rod), and the right end exchanges heat by convection with a medium at temperature $2$, from which heat flows in. In the notation of Definition §25.1, $\alpha_1 = 0$, $\alpha_2 = 1$, $c_1 = -1$, $\beta_1 = \beta_2 = 1$, $c_2 = 2$, and $s = p = 1$, $k = 2$.
>
> **(a) Steady state.** $0 = 2v''$, $v'(0) = 1$, $-v'(2) = v(2) - 2$. So $v = ax + b$ with $a = 1$, and $-1 = 2 + b - 2$ gives $b = -1$:
>
> $$
> v(x) = x - 1 .
> $$
>
> (Proposition §25.1 with $I(x) = x$ gives $\Delta = 1$, $A = -1$, $B = 1$.)
>
> **(b) Transient.** $w = u - v$ satisfies $w_t = 2w_{xx}$, $w_x(0, t) = 1 - 1 = 0$, $w_x(2, t) + w(2, t) = 0$, and $w(x, 0) = x^2 + x - 1 - (x - 1) = x^2$.
>
> **(c)–(f) Basic solutions and coefficients.** With $w = \phi(x)T(t)$ and $T'/(2T) = \phi''/\phi = \mu$, the eigenvalue problem is $\phi'' = \mu\phi$, $\phi'(0) = 0$, $\phi'(2) + \phi(2) = 0$, solved in [[§24 Expansion in Series of Eigenfunctions#^ex-24-3|Example §24.3]]: $\mu_n = -\lambda_n^2$ with $\cot 2\lambda_n = \lambda_n$, $\phi_n = \cos(\lambda_nx)$, and $T_n = e^{-2\lambda_n^2t}$. The basic solutions are $w_n = \cos(\lambda_nx)e^{-2\lambda_n^2t}$, and $x^2 = \sum c_n\cos(\lambda_nx)$ with
>
> $$
> c_n = \frac{\int_0^2 x^2\cos(\lambda_nx)\,dx}{\int_0^2 \cos^2(\lambda_nx)\,dx} = \frac{4(4\lambda_n^2 - 1)\sin 2\lambda_n}{\lambda_n^3(2 + \sin^2 2\lambda_n)} .
> $$
>
> **(g) Solution.**
>
> $$
> u(x, t) = x - 1 + \sum_{n=1}^\infty c_n\cos(\lambda_nx)e^{-2\lambda_n^2t} .
> $$
>
> **Theorem §25.4 in this example.** Here $\lambda_1 \approx 0.5384$, $\lambda_1^2 \approx 0.2899$ and $c_1 \approx 1.298$, so for large $t$
>
> $$
> u(x, t) \approx x - 1 + 1.298\cos(0.538x)\,e^{-0.580t} .
> $$
>
> Since $2\lambda_1 < \pi/2$, $\phi_1 = \cos(\lambda_1x)$ is positive on $[0, 2]$, and the temperature approaches the steady line $v = x - 1$ from above (figure). The next term decays like $e^{-2\lambda_2^2t} \approx e^{-6.64t}$, so the one-term approximation is good once $t$ is about $1$.
>
> *Source: 341 HW 7, Problem 2*

^ex-25-1

![[m341-25-1.svg]]
*The solution of Example §25.1 at several times, computed from 80 terms of the series. The initial profile $x^2 + x - 1$ (black dashed) relaxes toward the steady state $v(x) = x - 1$ (gray dashed). The slope at $x = 0$ is $1$ at all times (the prescribed flux), and the profile soon takes the shape $v + c_1\cos(\lambda_1x)e^{-2\lambda_1^2t}$, which stays above $v$.*

> [!example] Example §25.2: A Rod with Exponentially Varying Properties
> Solve
>
> $$
> e^{-x}\frac{\partial u}{\partial t} = \frac{\partial}{\partial x}\Big(e^x\frac{\partial u}{\partial x}\Big), \quad 0 < x < 1, \qquad u(0, t) = 0, \quad u(1, t) = 0, \qquad u(x, 0) = f(x) .
> $$
>
> This is (1) with conductivity $\kappa = e^x$ and heat capacity $\rho c = e^{-x}$; take $s = e^x$, $p = e^{-x}$, $k = 1$ (rescaling by averages, as in Definition §25.2, only changes $k$ and the constants in $s$, $p$). The boundary conditions are homogeneous, so there is no need to subtract a steady state ($v = 0$).
>
> **Basic solutions.** With $w = \phi(x)T(t)$: $e^{-x}\phi T' = (e^x\phi')'T$, so $T'/T = e^x(e^x\phi')'/\phi = \mu$, and
>
> $$
> T' = \mu T, \qquad e^x(e^x\phi')' = \mu\phi, \quad \phi(0) = 0, \quad \phi(1) = 0 .
> $$
>
> Here $sp = 1$, so substitute $y = \int_0^x e^{-\xi}\,d\xi = 1 - e^{-x}$, $\phi(x) = \psi(1 - e^{-x})$ ([[§23 Sturm–Liouville Problems#^rem-23-5|Method in §23]]). Then $e^x\phi' = \psi'$, $(e^x\phi')' = e^{-x}\psi''$, and the problem becomes
>
> $$
> \psi''(y) = \mu\psi(y), \quad 0 < y < 1 - e^{-1}, \qquad \psi(0) = 0, \quad \psi(1 - e^{-1}) = 0 .
> $$
>
> As in [[§23 Sturm–Liouville Problems#^ex-23-4|Example §23.4]], $\mu \ge 0$ gives only $\psi \equiv 0$, and $\mu = -\lambda^2$ gives $\psi = A\sin(\lambda y)$ with $\lambda(1 - e^{-1}) = n\pi$. So
>
> $$
> \lambda_n = \frac{n\pi}{1 - e^{-1}}, \qquad \phi_n(x) = \sin\Big(n\pi\,\frac{1 - e^{-x}}{1 - e^{-1}}\Big), \qquad w_n(x, t) = e^{-\lambda_n^2t}\phi_n(x) ,
> $$
>
> with $\lambda_1 \approx 4.970$, $\lambda_1^2 \approx 24.70$.
>
> **Coefficients.** By [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]], $\int_0^1 e^{-x}\phi_n\phi_m\,dx = 0$ for $n \ne m$, and with $dy = e^{-x}dx$, $\int_0^1 e^{-x}\phi_n^2\,dx = \int_0^{1 - e^{-1}}\sin^2\frac{n\pi y}{1 - e^{-1}}\,dy = \frac{1 - e^{-1}}{2}$. So
>
> $$
> u(x, t) = \sum_{n=1}^\infty b_ne^{-\lambda_n^2t}\sin\Big(n\pi\,\frac{1 - e^{-x}}{1 - e^{-1}}\Big), \qquad b_n = \frac{2}{1 - e^{-1}}\int_0^1 e^{-x}f(x)\sin\Big(n\pi\,\frac{1 - e^{-x}}{1 - e^{-1}}\Big)dx .
> $$
>
> *Source: 341 lecture 10.17*

^ex-25-2

> [!example] Example §25.3: Variable Coefficients and Fixed End Temperatures
> Consider
>
> $$
> \frac{\partial u}{\partial t} = e^{2x}\frac{\partial}{\partial x}\Big(e^{2x}\frac{\partial u}{\partial x}\Big), \quad 0 < x < a, \qquad u(0, t) = T_0, \quad u(a, t) = T_1, \qquad u(x, 0) = f(x) .
> $$
>
> Dividing by $e^{2x}$ puts it in the form (1) with $\kappa = e^{2x}$, $\rho c = e^{-2x}$, $k = 1$.
>
> **(a) Steady state.** $0 = e^{2x}(e^{2x}v')'$, $v(0) = T_0$, $v(a) = T_1$. Then $e^{2x}v' = B$, $v = A + BI(x)$ with $I(x) = \int_0^xe^{-2\xi}\,d\xi = \frac12(1 - e^{-2x})$, and the boundary conditions give
>
> $$
> v(x) = T_0 + (T_1 - T_0)\frac{1 - e^{-2x}}{1 - e^{-2a}} = \frac{T_0 - T_1}{1 - e^{-2a}}\,e^{-2x} + \frac{T_1 - e^{-2a}T_0}{1 - e^{-2a}} .
> $$
>
> **(b) Transient.** $w = u - v$: $w_t = e^{2x}(e^{2x}w_x)_x$, $w(0, t) = w(a, t) = 0$, $w(x, 0) = f(x) - v(x) = g(x)$.
>
> **(c) Eigenvalue problem.** With $w = \phi T$ and $T' = \mu T$: $e^{2x}(e^{2x}\phi')' = \mu\phi$, $\phi(0) = \phi(a) = 0$; in Sturm–Liouville form $(e^{2x}\phi')' - \mu e^{-2x}\phi = 0$, so $s = e^{2x}$, $p = e^{-2x}$.
>
> **(d) Solving it.** Since $sp = 1$, substitute $y = 1 - e^{-2x}$ (twice $\int_0^x e^{-2\xi}d\xi$; the hint's variable $e^{-2x}$ works equally well), $\phi(x) = \psi(1 - e^{-2x})$. Then $\phi' = 2e^{-2x}\psi'$, $e^{2x}\phi' = 2\psi'$, $(e^{2x}\phi')' = 4e^{-2x}\psi''$, and
>
> $$
> \psi''(y) = \frac\mu4\psi(y), \quad 0 < y < 1 - e^{-2a}, \qquad \psi(0) = 0, \quad \psi(1 - e^{-2a}) = 0 .
> $$
>
> As before, $\mu \ge 0$ gives no nonzero solution, and $\mu/4 = -\lambda^2$ gives $\psi = A\sin(\lambda y)$ with $\lambda(1 - e^{-2a}) = n\pi$. So
>
> $$
> \mu_n = -\frac{4n^2\pi^2}{(1 - e^{-2a})^2}, \qquad \phi_n(x) = \sin\Big(\frac{n\pi(1 - e^{-2x})}{1 - e^{-2a}}\Big) .
> $$
>
> **(e) Basic solutions.** $T_n = e^{\mu_nt}$, $w_n(x, t) = \exp\Big(-\frac{4n^2\pi^2t}{(1 - e^{-2a})^2}\Big)\sin\Big(\frac{n\pi(1 - e^{-2x})}{1 - e^{-2a}}\Big)$.
>
> **(f) Solution.** The weight is $e^{-2x}$, and with $dy = 2e^{-2x}dx$, $\int_0^a e^{-2x}\phi_n^2\,dx = \frac12\int_0^{1 - e^{-2a}}\sin^2\frac{n\pi y}{1 - e^{-2a}}\,dy = \frac{1 - e^{-2a}}{4}$. Hence
>
> $$
> u(x, t) = v(x) + \sum_{n=1}^\infty b_nw_n(x, t), \qquad b_n = \frac{\int_0^a e^{-2x}g(x)\phi_n(x)\,dx}{\int_0^a e^{-2x}\phi_n^2(x)\,dx} = \frac{4}{1 - e^{-2a}}\int_0^a e^{-2x}g(x)\sin\Big(\frac{n\pi(1 - e^{-2x})}{1 - e^{-2a}}\Big)dx .
> $$
>
> *The key's formula for $T_n(t)$ omits the factor $4$ in the exponent; its basic solutions $w_n$ have it.*
>
> *Source: 341 Practice Midterm 2, Q6*

^ex-25-3
