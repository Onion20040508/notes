---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 28
powers: "2.6"
aliases: ["Powers 2.6"]
tags: [fourier-series-and-pdes, math341]
---
← [[§27 Example꞉ Different Boundary Conditions]] · ↑ [[· 2 The Heat Equation]] · [[§29 Sturm–Liouville Problems]] →

*Powers, Section 2.6 · MAT 341 lectures 10.1, 10.10.*

The three previous examples had boundary conditions on $u$ or on $\partial u/\partial x$. This one has a condition of the third kind: a rod with insulated lateral surface, its left end held at a constant temperature and its right end exposed to convective heat transfer. The new feature is the eigenvalue equation $\tan(\lambda a) = -\kappa\lambda/h$, which cannot be solved in closed form; its roots are found graphically or numerically, and for large $n$ they approach $(2n - 1)\pi/2a$. The eigenfunctions $\sin(\lambda_nx)$ are not those of any Fourier series, but they are still orthogonal, and orthogonality alone determines the coefficients of the solution. This is the step from Fourier series to the general eigenfunction expansions of the Sturm–Liouville theory in [[§29 Sturm–Liouville Problems|§29]].

## The Problem

The boundary value–initial value problem satisfied by the temperature in the rod is

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (1) \\
u(0, t) &= T_0, && 0 < t, && (2) \\
-\kappa\frac{\partial u}{\partial x}(a, t) &= h\big(u(a, t) - T_1\big), && 0 < t, && (3) \\
u(x, 0) &= f(x), && 0 < x < a . && (4)
\end{aligned}
$$

By [[§24 Steady-State Temperatures#^ex-24-2|Example §24.2]] the steady-state solution is

$$
v(x) = T_0 + \frac{xh(T_1 - T_0)}{\kappa + ha} . \qquad (5)
$$

Since the original boundary conditions are nonhomogeneous, form the problem for the transient solution $w(x, t) = u(x, t) - v(x)$. By direct substitution (as in [[§24 Steady-State Temperatures#^rem-24-3|Remark: Boundary Conditions of the Transient]]),

$$
\begin{aligned}
\frac{\partial^2w}{\partial x^2} &= \frac1k\frac{\partial w}{\partial t}, && 0 < x < a, \quad 0 < t, && (6) \\
w(0, t) &= 0, \quad hw(a, t) + \kappa\frac{\partial w}{\partial x}(a, t) = 0, && 0 < t, && (7) \\
w(x, 0) &= f(x) - v(x) \equiv g(x), && 0 < x < a . && (8)
\end{aligned}
$$

Assuming $w = \phi(x)T(t)$, the variables separate exactly as before, giving two ordinary differential equations linked by a common parameter $\lambda^2$: $\phi'' + \lambda^2\phi = 0$, $0 < x < a$, and $T' + \lambda^2kT = 0$, $0 < t$. Since the boundary conditions are linear and homogeneous, they translate directly into conditions on $\phi$:

$$
w(0, t) = \phi(0)T(t) = 0, \qquad \kappa\frac{\partial w}{\partial x}(a, t) + hw(a, t) = \big[\kappa\phi'(a) + h\phi(a)\big]T(t) = 0 .
$$

Either $T(t) \equiv 0$ (which would make $w \equiv 0$) or $\phi(0) = 0$ and $\kappa\phi'(a) + h\phi(a) = 0$.

## The Eigenvalue Problem

> [!theorem] Theorem §34.1: Eigenvalues for Convection at One End
> The eigenvalue problem
>
> $$
> \phi'' + \lambda^2\phi = 0, \quad 0 < x < a , \qquad (9)
> $$
>
> $$
> \phi(0) = 0, \qquad \kappa\phi'(a) + h\phi(a) = 0 , \qquad (10)
> $$
>
> with $\kappa, h > 0$, has infinitely many eigenvalues $\lambda_1^2 < \lambda_2^2 < \cdots$. The numbers $\lambda_n > 0$ are the positive solutions of
>
> $$
> \kappa\lambda\cos(\lambda a) + h\sin(\lambda a) = 0, \qquad\text{or}\qquad \tan(\lambda a) = -\frac\kappa h\lambda , \qquad (11)
> $$
>
> one in each interval $\frac{(2n - 1)\pi}{2a} < \lambda_n < \frac{n\pi}a$, and the eigenfunctions are $\phi_n(x) = \sin(\lambda_nx)$. For very large $n$, $\lambda_n$ is given approximately by
>
> $$
> \lambda_n \cong \frac{2n - 1}2\,\frac\pi a .
> $$
>
> The time factors are $T_n(t) = \exp(-\lambda_n^2kt)$.
>
> *Powers: 2.6, Equations (9)–(11)*

^thm-28-1

> [!proof]+ Proof
> **Reduction to (11).** The general solution of the differential equation is $\phi(x) = c_1\cos(\lambda x) + c_2\sin(\lambda x)$. The boundary condition at $x = 0$ requires $\phi(0) = c_1 = 0$, leaving $\phi(x) = c_2\sin(\lambda x)$. At the other boundary,
>
> $$
> \kappa\phi'(a) + h\phi(a) = c_2\big(\kappa\lambda\cos(\lambda a) + h\sin(\lambda a)\big) = 0 .
> $$
>
> Discarding the possibilities $c_2 = 0$ and $\lambda = 0$, which both lead to the trivial solution, leaves the equation (11). (For $\lambda = 0$, Powers asserts this; here is why: the general solution is then $\phi = c_1 + c_2x$, not the form above; $\phi(0) = 0$ gives $c_1 = 0$, and $\kappa\phi'(a) + h\phi(a) = c_2(\kappa + ha) = 0$ gives $c_2 = 0$.) (Dividing by $h\cos(\lambda a)$ is allowed: if $\cos(\lambda a) = 0$, then (11) would force $\sin(\lambda a) = 0$ as well, which is impossible.)
>
> **Positive separation constant.** (Powers does not treat it; here is the check.) If $\phi'' = p^2\phi$ with $p > 0$, then $\phi(0) = 0$ gives $\phi = c_2\sinh(px)$, and $\kappa\phi'(a) + h\phi(a) = c_2\big(\kappa p\cosh(pa) + h\sinh(pa)\big)$. Both terms in the parentheses are positive, so $c_2 = 0$.
>
> **The roots of (11).** From sketches of the graphs of $\tan(\lambda a)$ and $-\kappa\lambda/h$ (figure below) there is an infinite number of solutions. (Powers argues from the graphs; here is the count.) Put $z = \lambda a > 0$ and $A = \kappa/ha > 0$, so (11) reads $\tan z = -Az$. The right side is negative for $z > 0$, so there is no root where $\tan z \ge 0$, that is, in $0 < z < \frac\pi2$ or in $n\pi \le z < n\pi + \frac\pi2$. On each interval $\frac{(2n - 1)\pi}2 < z < n\pi$ the function $F(z) = \tan z + Az$ is continuous and strictly increasing ($F' = \sec^2z + A > 0$), tends to $-\infty$ as $z \to \frac{(2n - 1)\pi}2$ from the right, and $F(n\pi) = An\pi > 0$. So $F$ has exactly one zero $z_n$ there, and $\lambda_n = z_n/a$. Finally, writing $z_n = \frac{(2n - 1)\pi}2 + \varepsilon_n$ with $0 < \varepsilon_n < \frac\pi2$, $\tan z_n = -\cot\varepsilon_n$, so (11) says $\cot\varepsilon_n = Az_n \to \infty$; hence $\varepsilon_n \to 0$ and $\lambda_n \cong \frac{(2n - 1)\pi}{2a}$ for large $n$.

^pf-28-1

*Uses:* [[§26 Example꞉ Insulated Bar#^def-26-1|Def. §26.1]], [[§26 Example꞉ Insulated Bar#^def-26-2|Def. §26.2]], [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|331 Thm. §19.2]]

![[m341-22-1.svg]]
*The graphs of $\tan(\lambda a)$ (blue) and $-\kappa\lambda/h$ (red), here for $\kappa/ha = 0.5$, against $\lambda a$. The intersections (dots) are the eigenvalues: $\lambda_na \approx 2.289$, $5.087$, $8.096$, $11.173$, each just to the right of $(2n - 1)\pi/2$ (dashed) and closer to it as $n$ grows. The intersection at $\lambda = 0$ corresponds to the trivial solution.*

> [!remark] Remark: Negative Roots
> The equation (11) also has negative solutions $-\lambda_n$ (the left side is odd in $\lambda$, and so is the right). They are ignored because they give nothing new: $\sin(-\lambda_nx) = -\sin(\lambda_nx)$ is a multiple of the same eigenfunction, and the eigenvalue $\lambda^2$ is the same.

^rem-28-1

> [!example] Example §34.1: The First Five Eigenvalues Numerically
> The roots of (11) depend on the single dimensionless parameter $\kappa/ha$: in terms of $z = \lambda a$ the equation is $\tan z = -Az$ with $A = \kappa/ha$. Solving it on each interval $\big(\frac{(2n - 1)\pi}2, n\pi\big)$ by bisection gives the first five positive solutions $z_n = \lambda_na$:
>
> | $n$ | $A = 0.25$ | $0.5$ | $1$ | $2$ | $4$ |
> |---|---|---|---|---|---|
> | 1 | 2.5704 | 2.2889 | 2.0288 | 1.8366 | 1.7155 |
> | 2 | 5.3540 | 5.0870 | 4.9132 | 4.8158 | 4.7648 |
> | 3 | 8.3029 | 8.0962 | 7.9787 | 7.9171 | 7.8857 |
> | 4 | 11.3348 | 11.1727 | 11.0855 | 11.0408 | 11.0183 |
> | 5 | 14.4080 | 14.2764 | 14.2074 | 14.1724 | 14.1548 |
>
> The values agree with Powers' Table 2 to all four decimals. Two trends are visible. Down a column, $z_n - (2n - 1)\frac\pi2$ shrinks ($\frac\pi2 = 1.5708$, $\frac{3\pi}2 = 4.7124$, $\frac{5\pi}2 = 7.8540$, $\frac{7\pi}2 = 10.9956$, $\frac{9\pi}2 = 14.1372$), as Theorem §28.1 says. Across a row, as $A = \kappa/ha$ grows (weak convection compared with conduction), $z_n$ moves down toward $(2n - 1)\frac\pi2$, the insulated-end values of [[§27 Example꞉ Different Boundary Conditions#^thm-27-1|Theorem §27.1]]; as $A \to 0$ (strong convection) it moves up toward $n\pi$, the fixed-end values of [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]]. For instance, with $\kappa/h = 0.5$ and $a = 1$: $\lambda_1 = 2.29$, $\lambda_2 = 5.09$.
>
> *Powers: 2.6, Table 2*

^ex-28-1

## Orthogonality and the Coefficients

For each $n = 1, 2, \ldots$ there are an eigenvalue $\lambda_n^2$ and an eigenfunction $\phi_n(x)$, and $w_n(x, t) = \phi_n(x)T_n(t)$ is a solution of (6) and (7). Since (6) and (7) are linear and homogeneous, the transient solution will have the form

$$
w(x, t) = \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt) ,
$$

and the remaining condition, the initial condition (8), is

$$
w(x, 0) = \sum_{n=1}^\infty b_n\sin(\lambda_nx) = g(x), \qquad 0 < x < a . \qquad (12)
$$

Although (12) looks like a Fourier series problem, it is not, because $\lambda_2, \lambda_3, \ldots$ are not integer multiples of $\lambda_1$. But the idea of orthogonality still works.

> [!theorem] Proposition §34.2: Orthogonality and Norms of the Eigenfunctions
> Let $\lambda_n$ be the positive roots of (11). Then
>
> $$
> \int_0^a\sin(\lambda_nx)\sin(\lambda_mx)\,dx = 0, \qquad n \ne m , \qquad (13)
> $$
>
> and
>
> $$
> \int_0^a\sin^2(\lambda_mx)\,dx = \frac a2 + \frac\kappa h\,\frac{\cos^2(\lambda_ma)}2 .
> $$
>
> In general this is not $a/2$.
>
> *Powers: 2.6, Equation (13); Exercises 2.6.6 and 2.6.10*

^prop-28-2

> [!proof]+ Proof
> (Powers states (13) "by direct computation" and leaves the computations to Exercises 2.6.10 and 2.6.6; here they are. The general reason, valid for every problem of this type, is [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]]; the same direct computation is [[§29 Sturm–Liouville Problems#^ex-29-3|Example §29.3]].) Write $s_n = \sin(\lambda_na)$, $c_n = \cos(\lambda_na)$. The defining equation (11) says $hs_n = -\kappa\lambda_nc_n$.
>
> **Orthogonality.** For $n \ne m$ we have $\lambda_n \ne \lambda_m$, both positive. By the product-to-sum identity,
>
> $$
> \int_0^a\sin(\lambda_nx)\sin(\lambda_mx)\,dx = \frac12\Big[\frac{\sin((\lambda_n - \lambda_m)a)}{\lambda_n - \lambda_m} - \frac{\sin((\lambda_n + \lambda_m)a)}{\lambda_n + \lambda_m}\Big] = \frac{\lambda_ms_nc_m - \lambda_nc_ns_m}{\lambda_n^2 - \lambda_m^2} ,
> $$
>
> where the last step expands $\sin((\lambda_n \mp \lambda_m)a) = s_nc_m \mp c_ns_m$ and puts both fractions over $\lambda_n^2 - \lambda_m^2$. Substituting $s_n = -\kappa\lambda_nc_n/h$ and $s_m = -\kappa\lambda_mc_m/h$, the numerator is
>
> $$
> \lambda_m\Big(-\frac\kappa h\lambda_nc_n\Big)c_m - \lambda_nc_n\Big(-\frac\kappa h\lambda_mc_m\Big) = 0 .
> $$
>
> **Norm.** $\int_0^a\sin^2(\lambda_mx)\,dx = \frac a2 - \frac{\sin(2\lambda_ma)}{4\lambda_m} = \frac a2 - \frac{s_mc_m}{2\lambda_m}$, and $-s_mc_m/\lambda_m = \frac\kappa hc_m^2$ by (11).

^pf-28-2

*Uses:* [[§28 Example꞉ Convection#^thm-28-1|§28.1]]

> [!theorem] Theorem §34.3: Coefficients and Solution
> If the expansion (12) holds and may be integrated term by term after multiplication by $\sin(\lambda_mx)$, then
>
> $$
> b_m = \frac{\int_0^ag(x)\sin(\lambda_mx)\,dx}{\int_0^a\sin^2(\lambda_mx)\,dx} . \qquad (14)
> $$
>
> With these coefficients the solution of (1)–(4) is
>
> $$
> u(x, t) = v(x) + w(x, t) = T_0 + \frac{xh(T_1 - T_0)}{\kappa + ha} + \sum_{n=1}^\infty b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt) .
> $$
>
> *Powers: 2.6, Equation (14)*

^thm-28-3

> [!proof]+ Proof
> Multiply both sides of (12) by $\sin(\lambda_mx)$, with $m$ fixed, and integrate from $0$ to $a$; integrating term by term,
>
> $$
> \int_0^ag(x)\sin(\lambda_mx)\,dx = \sum_{n=1}^\infty b_n\int_0^a\sin(\lambda_nx)\sin(\lambda_mx)\,dx .
> $$
>
> By (13) all the terms of the series disappear except the one with $n = m$, which gives $\int_0^ag\sin(\lambda_mx)\,dx = b_m\int_0^a\sin^2(\lambda_mx)\,dx$, and the integral on the right is positive. This is (14). With the $b_m$ so calculated, $w$ satisfies (6)–(8) (superposition, [[§25 Example꞉ Fixed End Temperatures#^thm-25-4|Theorem §25.4]]; convergence for $t > 0$ as in [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|Theorem §25.5]], since $|b_m| \le \int_0^a|g| \big/ \frac a2$ by the norm formula of Proposition §28.2, and $\frac{(2n - 1)\pi}{2a} < \lambda_n < \frac{n\pi}a$ gives $\sum\lambda_n^2e^{-\lambda_n^2kt_0} < \infty$), and $u = v + w$ satisfies (1)–(4).

^pf-28-3

*Uses:* [[§28 Example꞉ Convection#^prop-28-2|§28.2]], [[§25 Example꞉ Fixed End Temperatures#^thm-25-4|§25.4]], [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|§25.5]], [[§24 Steady-State Temperatures#^ex-24-2|Ex. §24.2]]

*That every sectionally smooth $g$ does have an expansion (12), so that the hypothesis of Theorem §28.3 is met, is not shown here; it is the expansion theorem for Sturm–Liouville eigenfunctions, [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]].*

> [!remark]- Connections
> - (14) is the coordinate formula $b_m = \langle g, \phi_m\rangle/\langle\phi_m, \phi_m\rangle$ for an orthogonal set in the inner product $\int_0^af g\,dx$: [[§56 Inner Product Spaces#^thm-56-2|235 Thm. §56.2]]. In finite dimensions orthogonality and a basis suffice; here "basis" means completeness, the property that the expansion reconstructs $g$: [[§24 Orthonormal Sets and Bases#^def-24-2|556 Def. §24.2]], [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]].

> [!remark] Remark: A Generalized Fourier Basis
> The lectures name the property used here. A sequence of functions $\phi_1, \phi_2, \ldots$ on an interval $I$ is a **generalized Fourier basis** if (i) it is orthogonal, $\int_I\phi_i\phi_j\,dx = 0$ for $i \ne j$, and (ii) it is complete: every sectionally continuous $f$ has an expansion $f(x) \sim \sum c_n\phi_n(x)$, with $c_n = \int_If\phi_n\,dx\big/\int_I\phi_n^2\,dx$. The eigenfunctions $\sin(\lambda_nx)$ of (9)–(10) are such a basis, as are those of [[§25 Example꞉ Fixed End Temperatures|§25]]–[[§27 Example꞉ Different Boundary Conditions|§27]]. The eigenvalue problems of this chapter, $\phi'' = p\phi$ with conditions $\alpha_1\phi(0) - \alpha_2\phi'(0) = 0$ and $\beta_1\phi(a) + \beta_2\phi'(a) = 0$, are special cases of the Sturm–Liouville problem, whose theorems guarantee both properties: [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]], [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]].
>
> *Source: 341 lectures 10.1, 10.10*

^rem-28-2

## Examples

> [!example] Example §34.2: Starting from Zero Temperature
> Solve (1)–(4) with $f(x) = 0$, and find the coefficients for $g(x) = 1$.
>
> **Coefficients.** Here $g = -v = -T_0 - Bx$ with $B = h(T_1 - T_0)/(\kappa + ha)$. Two integrals are needed:
>
> $$
> \int_0^a\sin(\lambda x)\,dx = \frac{1 - \cos(\lambda a)}\lambda, \qquad \int_0^ax\sin(\lambda x)\,dx = -\frac{a\cos(\lambda a)}\lambda + \frac{\sin(\lambda a)}{\lambda^2} = -\frac{\cos(\lambda a)}\lambda\Big(a + \frac\kappa h\Big) ,
> $$
>
> the last step by (11), $\sin(\lambda a) = -\frac\kappa h\lambda\cos(\lambda a)$, for $\lambda = \lambda_m$. Since $B\big(a + \frac\kappa h\big) = \frac{h(T_1 - T_0)}{\kappa + ha}\cdot\frac{ha + \kappa}h = T_1 - T_0$,
>
> $$
> \int_0^ag\sin(\lambda_mx)\,dx = -T_0\frac{1 - \cos(\lambda_ma)}{\lambda_m} + (T_1 - T_0)\frac{\cos(\lambda_ma)}{\lambda_m} = \frac{T_1\cos(\lambda_ma) - T_0}{\lambda_m} .
> $$
>
> Dividing by the norm from Proposition §28.2,
>
> $$
> b_m = \frac{T_1\cos(\lambda_ma) - T_0}{\lambda_m\Big(\dfrac a2 + \dfrac\kappa h\,\dfrac{\cos^2(\lambda_ma)}2\Big)} = \frac{2h\big(T_1\cos(\lambda_ma) - T_0\big)}{\lambda_m\big(ha + \kappa\cos^2(\lambda_ma)\big)} ,
> $$
>
> and $u(x, t) = T_0 + \dfrac{xh(T_1 - T_0)}{\kappa + ha} + \sum b_n\sin(\lambda_nx)\exp(-\lambda_n^2kt)$.
>
> **For $g(x) = 1$** only the first integral is needed: $b_m = \dfrac{1 - \cos(\lambda_ma)}{\lambda_m\big(\frac a2 + \frac\kappa h\frac{\cos^2(\lambda_ma)}2\big)}$.
>
> For instance, with $T_0 = 20$, $T_1 = 100$, $a = 1$, $\kappa/ha = 1$: $\lambda_1 = 2.0288$, $\cos\lambda_1 = -0.4421$, and $b_1 = (100(-0.4421) - 20)/(2.0288 \cdot 0.5977) \approx -53.0$. The figure below sums 400 terms.
>
> *Powers: 2.6, Figure 7; Exercise 2.6.7*

^ex-28-2

![[m341-22-2.svg]]
*Example §22.2 with $T_0 = 20$, $T_1 = 100$, $f(x) = 0$, at $kt/a^2 = 0.001$, $0.01$, $0.1$, $1$; dashed: the steady state (5). (a) $\kappa/ha = 0.1$ (strong convection): the right end quickly approaches the fluid temperature and $v(a) = 20 + 80/1.1 \approx 92.7$. (b) $\kappa/ha = 1$: the end stays well below $T_1$, $v(a) = 60$. Both the temperature and the slope at $x = a$ change with time, in the ratio required by the boundary condition (3).*

> [!example] Example §34.3: A General Robin Condition
> Solve $u_{xx} = \frac1ku_t$, $0 < x < a$, with $u(0, t) = T_1$, $hu(a, t) + \kappa u_x(a, t) = r$ (a constant), $u(x, 0) = f(x)$.
>
> **Steady state.** $v'' = 0$, $v(0) = T_1$, $hv(a) + \kappa v'(a) = r$. With $v = Bx + T_1$: $h(Ba + T_1) + \kappa B = r$, so
>
> $$
> v(x) = T_1 + \frac{r - hT_1}{\kappa + ha}\,x .
> $$
>
> (For convection into a fluid at $T_f$, $r = hT_f$ and the slope is $h(T_f - T_1)/(\kappa + ha)$, which is (5) with the roles of the temperatures renamed.)
>
> **Transient.** $w = u - v$: $w_{xx} = \frac1kw_t$, $w(0, t) = 0$, $hw(a, t) + \kappa w_x(a, t) = 0$, $w(x, 0) = f(x) - v(x) = g(x)$: the problem (6)–(8).
>
> **Basic solutions.** $\phi'' = p\phi$, $\phi(0) = 0$, $h\phi(a) + \kappa\phi'(a) = 0$. For $p \ge 0$ all solutions are zero; for $p = -\lambda^2$, $\phi = A\sin(\lambda x)$ with $hA\sin(\lambda a) + \kappa A\lambda\cos(\lambda a) = 0$, that is $\tan(\lambda a) = -\frac\kappa h\lambda$. "Unfortunately $\lambda$ cannot be written explicitly": the roots $\lambda_n$ are read off the graph (Theorem §28.1), and $w_n(x, t) = \sin(\lambda_nx)e^{-\lambda_n^2kt}$.
>
> **Coefficients.** $w = \sum c_nw_n$, and since $\{\sin\lambda_nx\}$ is a generalized Fourier basis (orthogonal by Proposition §28.2),
>
> $$
> c_m = \frac{\int_0^ag(x)\sin(\lambda_mx)\,dx}{\int_0^a\sin^2(\lambda_mx)\,dx} ,
> $$
>
> where in general $\int_0^a\sin^2(\lambda_mx)\,dx \ne a/2$.
>
> *Lecture 10.10 writes the steady-state slope as $(r - T_1)/(a + \kappa)$; imposing $hv(a) + \kappa v'(a) = r$ on $v = Bx + T_1$ gives $(r - hT_1)/(\kappa + ha)$, which reduces to the lecture's expression when $h = 1$.*
>
> *Source: 341 lectures 10.1, 10.10*

^ex-28-3
