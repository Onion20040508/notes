---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 26
powers: "2.4"
aliases: ["Powers 2.4"]
tags: [fourier-series-and-pdes, math341]
---
← [[§25 Example꞉ Fixed End Temperatures]] · ↑ [[· 2 The Heat Equation]] · [[§27 Example꞉ Different Boundary Conditions]] →

*Powers, Section 2.4 · MAT 341 lecture 9.26 · HW 5 · Midterm 1.*

The second complete example is a uniform bar whose ends, as well as its lateral surface, are insulated. Now the equation and the boundary conditions are already homogeneous, so separation of variables applies to $u$ directly. The separated problem for $\phi$ is the first one that Powers calls an **eigenvalue problem**; with insulated ends its eigenfunctions are $1, \cos(\pi x/a), \cos(2\pi x/a), \ldots$, and the initial condition becomes a Fourier cosine series. The constant mode never decays: no heat can leave, so the rod tends to the uniform temperature equal to the average of the initial temperature.

## The Problem

The ends of the bar at $x = 0$ and $x = a$ are insulated instead of being held at constant temperatures. The boundary value–initial value problem for the temperature is

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < t, && (1) \\
\frac{\partial u}{\partial x}(0, t) &= 0, \quad \frac{\partial u}{\partial x}(a, t) = 0, && 0 < t, && (2) \\
u(x, 0) &= f(x), && 0 < x < a, && (3)
\end{aligned}
$$

where $f(x)$ is a given function. [[§24 Steady-State Temperatures#^ex-24-3|Example §24.3]] showed that the steady-state problem has infinitely many solutions. But the purpose of the steady state is to make the problem for the transient homogeneous, and here the equation and boundary conditions are homogeneous already. So neither the steady state nor the transient is needed: separate $u$ itself ([[§25 Example꞉ Fixed End Temperatures#^rem-25-1|Remark: Method — The Steady-State/Transient Split]]).

Assume $u(x, t) = \phi(x)T(t)$, neither factor identically $0$. As in [[§25 Example꞉ Fixed End Temperatures#^prop-25-1|Proposition §25.1]], the heat equation becomes $\phi''T = \frac1k\phi T'$, and dividing by $\phi T$,

$$
\frac{\phi''(x)}{\phi(x)} = \frac{T'(t)}{kT(t)}, \qquad 0 < x < a, \quad 0 < t ,
$$

so the two sides equal a constant. If that constant were positive, $T$ would be an increasing exponential function of time, which is unacceptable; also $\phi$ could not satisfy the boundary conditions without being identically zero (proof of Theorem §26.1). Assuming a negative constant, $-\lambda^2$, the equalities separate into

$$
\phi'' + \lambda^2\phi = 0, \quad 0 < x < a , \qquad (4)
$$

$$
T' + \lambda^2kT = 0, \quad 0 < t . \qquad (5)
$$

The boundary conditions are homogeneous, so they translate into conditions on $\phi$: $\frac{\partial u}{\partial x}(0, t) = \phi'(0)T(t) = 0$ and $\frac{\partial u}{\partial x}(a, t) = \phi'(a)T(t) = 0$ for $t > 0$. Either $T(t)$ is always zero (making $u \equiv 0$), or

$$
\phi'(0) = 0, \qquad \phi'(a) = 0 .
$$

## The Eigenvalue Problem

> [!definition] Definition §26.1: Eigenvalue Problem
> A homogeneous differential equation for $\phi$ containing a parameter, together with homogeneous boundary conditions, such as
>
> $$
> \phi'' + \lambda^2\phi = 0, \quad 0 < x < a , \qquad (6)
> $$
>
> $$
> \phi'(0) = 0, \qquad \phi'(a) = 0 , \qquad (7)
> $$
>
> is called an **eigenvalue problem**.
>
> *Powers: 2.4 (text)*

^def-26-1

> [!definition] Definition §26.2: Eigenvalues and Eigenfunctions
> The values of the parameter $\lambda^2$ for which nonzero solutions of an eigenvalue problem such as (6)–(7) ([[§26 Example꞉ Insulated Bar#^def-26-1|Definition §26.1]]) exist are the **eigenvalues**, and the corresponding nonzero solutions are the **eigenfunctions**. The significant parameter is $\lambda^2$, not $\lambda$; the square is used only for convenience. Any constant multiple of an eigenfunction is again an eigenfunction.
>
> *Powers: 2.4 (text)*

^def-26-2

The problem $\phi'' + \lambda^2\phi = 0$, $\phi(0) = \phi(a) = 0$ of [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]] was already an eigenvalue problem (with eigenvalues $(n\pi/a)^2$), and so is the Euler buckling problem of [[§5★ Boundary Value Problems#^ex-5-4|Example §5.4]], whose eigenvalues are those of [[§5★ Boundary Value Problems#^prop-5-3|Proposition §5.3]]. The term itself was introduced in [[§5★ Boundary Value Problems#^def-5-4|Definition §5.4]].

> [!remark]- Connections
> - The analogy is exact: $\phi \mapsto \phi''$ is a linear operator on functions satisfying (7), and (6) says $\phi'' = -\lambda^2\phi$, an eigenvector equation $A\phi = \mu\phi$ with eigenvalue $\mu = -\lambda^2$: [[§40 Eigenvectors and Eigenvalues#^def-40-1|235 Def. §40.1]], [[§14 Invariant Subspaces#^ladr-5-5|LADR 5.5]]. Unlike a matrix it has infinitely many eigenvalues; that the eigenfunctions are orthogonal and complete is the infinite-dimensional analogue of the spectral theorem, [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]] and [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]].

> [!theorem] Theorem §26.1: Eigenvalues for Insulated Ends
> The eigenvalue problem (6)–(7) has the solution
>
> $$
> \begin{cases}
> \lambda_0^2 = 0, & \phi_0(x) = 1, \\[2pt]
> \lambda_n^2 = \Big(\dfrac{n\pi}a\Big)^2, & \phi_n(x) = \cos(\lambda_nx), \quad n = 1, 2, \ldots .
> \end{cases}
> $$
>
> There are no other eigenvalues, and no negative ones: a positive separation constant ($\phi''/\phi = p^2 > 0$) forces $\phi \equiv 0$.
>
> *Powers: 2.4 (text)*

^thm-26-1

> [!proof]+ Proof
> **$\lambda > 0$.** The general solution of (6) is $\phi(x) = c_1\cos(\lambda x) + c_2\sin(\lambda x)$. The boundary condition at $x = 0$ gives $\phi'(0) = c_2\lambda = 0$, so $c_2 = 0$ (as $\lambda \ne 0$) and $\phi(x) = c_1\cos(\lambda x)$. Then the second boundary condition requires $\phi'(a) = -c_1\lambda\sin(\lambda a) = 0$. Once again either $c_1 = 0$, which makes $\phi \equiv 0$, or $\sin(\lambda a) = 0$. So $\lambda$ is restricted to the values $\pi/a, 2\pi/a, 3\pi/a, \ldots$; labeling the eigenvalues with a subscript, $\lambda_n^2 = (n\pi/a)^2$, $\phi_n(x) = \cos(\lambda_nx)$, $n = 1, 2, \ldots$, with $c_1 = 1$ for simplicity.
>
> **$\lambda = 0$.** Equations (6) and (7) become $\phi'' = 0$, $\phi'(0) = 0$, $\phi'(a) = 0$. The solution of the differential equation is $\phi(x) = c_1 + c_2x$, and both boundary conditions say $c_2 = 0$. Therefore $\phi(x)$ is any constant: $0$ is an eigenvalue, $\lambda_0^2 = 0$, $\phi_0(x) = 1$.
>
> **Positive separation constant.** (Powers asserts this; here is why, following his Exercise 2.4.8.) Suppose $\phi''/\phi = p^2$ with $p > 0$. Then $\phi(x) = c_1\cosh(px) + c_2\sinh(px)$, so $\phi'(x) = p\big(c_1\sinh(px) + c_2\cosh(px)\big)$. The condition $\phi'(0) = pc_2 = 0$ gives $c_2 = 0$, and then $\phi'(a) = pc_1\sinh(pa) = 0$ gives $c_1 = 0$, since $\sinh(pa) > 0$. So $\phi \equiv 0$.

^pf-26-1

*Uses:* [[§26 Example꞉ Insulated Bar#^def-26-1|Def. §26.1]], [[§26 Example꞉ Insulated Bar#^def-26-2|Def. §26.2]], [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|331 Thm. §19.2]], [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|331 Thm. §17.2]]

## The Solution

With the numbers $\lambda_n^2$ known, (5) gives $T_0(t) = 1$, $T_n(t) = \exp(-\lambda_n^2kt)$. The products $\phi_n(x)T_n(t)$ solve the partial differential equation (1) and satisfy the boundary conditions (2):

$$
u_0(x, t) = 1, \qquad u_n(x, t) = \cos(\lambda_nx)\exp(-\lambda_n^2kt) . \qquad (8)
$$

> [!theorem] Theorem §26.2: Solution of the Insulated-Bar Problem
> Let $f$ be sectionally smooth on $0 < x < a$ and let
>
> $$
> a_0 = \frac1a\int_0^af(x)\,dx, \qquad a_n = \frac2a\int_0^af(x)\cos\Big(\frac{n\pi x}a\Big)dx . \qquad (10)
> $$
>
> Then the solution of (1)–(3) is
>
> $$
> u(x, t) = a_0 + \sum_{n=1}^\infty a_n\cos(\lambda_nx)\exp(-\lambda_n^2kt), \qquad \lambda_n = \frac{n\pi}a , \qquad (9)
> $$
>
> and as $t \to \infty$ all terms except the first disappear:
>
> $$
> \lim_{t\to\infty}u(x, t) = a_0 = \frac1a\int_0^af(x)\,dx .
> $$
>
> *Powers: 2.4, Equations (8)–(10)*

^thm-26-2

> [!proof]+ Proof
> Because the partial differential equation and the boundary conditions are linear and homogeneous, the principle of superposition ([[§25 Example꞉ Fixed End Temperatures#^thm-25-4|Theorem §25.4]]) applies, and any linear combination of the solutions (8) is a solution; so the solution of the whole system may have the form (9). (The convergence is justified exactly as in the proof of [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|Theorem §25.5]]: for $t \ge t_0 > 0$ the coefficients $A_n(t) = a_n\exp(-\lambda_n^2kt)$ tend to zero so rapidly that the series and its term-by-term derivatives converge uniformly on $0 \le x \le a$; this is Powers' Exercise 2.4.9.)
>
> Only the initial condition (3) remains. For $u$ in the form (9) it reads
>
> $$
> u(x, 0) = a_0 + \sum_{n=1}^\infty a_n\cos(\lambda_nx) = f(x), \qquad 0 < x < a .
> $$
>
> Because $\lambda_n = n\pi/a$, this is a Fourier cosine series problem (the Fourier series of the even periodic extension of $f$, [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-3|Definition §11.3]]), and the coefficients are given by (10). For sectionally smooth $f$ the series converges to $f(x)$ wherever $f$ is continuous ([[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1]]).
>
> Finally, let $M$ bound the $|a_n|$ and fix $t_0 > 0$. For $t \ge t_0$, since $\lambda_n^2 \ge \lambda_1^2$, $e^{-\lambda_n^2kt} \le e^{-\lambda_n^2kt_0}e^{-\lambda_1^2k(t - t_0)}$, so
>
> $$
> \Big|\sum_{n=1}^\infty a_n\cos(\lambda_nx)e^{-\lambda_n^2kt}\Big| \le Me^{-\lambda_1^2k(t - t_0)}\sum_{n=1}^\infty e^{-\lambda_n^2kt_0} \to 0 \qquad (t \to \infty) ,
> $$
>
> uniformly in $x$. So $u(x, t) \to a_0$.

^pf-26-2

*Uses:* [[§26 Example꞉ Insulated Bar#^thm-26-1|§26.1]], [[§25 Example꞉ Fixed End Temperatures#^thm-25-4|§25.4]], [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|§25.5]], [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-3|Def. §11.3]], [[§12 Convergence of Fourier Series#^thm-12-1|§12.1]]

> [!remark] Remark: Why the Limit Is the Average
> The limit $a_0$ is the average of the initial temperature, and the reason is conservation of heat. The total heat in the rod is $\rho cA\int_0^au(x, t)\,dx$, and by the heat equation and the boundary conditions
>
> $$
> \frac{d}{dt}\int_0^au\,dx = \int_0^au_t\,dx = k\int_0^au_{xx}\,dx = k\big(u_x(a, t) - u_x(0, t)\big) = 0 .
> $$
>
> No heat crosses the insulated ends, so the total heat, and with it the average temperature, never changes; heat only redistributes until the temperature is uniform. The same computation explains a remark of the lecture: with prescribed fluxes $u_x(0, t) = A_1$, $u_x(a, t) = A_2$, the total heat changes at the rate $\rho cAk(A_2 - A_1)$, and a steady state, in which nothing changes, is possible only if $A_1 = A_2$ ([[§26 Example꞉ Insulated Bar#^ex-26-2|Example §26.2]]).
>
> *Source: 341 lecture 9.26*

^rem-26-1

## Examples

> [!example] Example §26.1: Initial Temperature a Straight Line
> Find the complete solution of (1)–(3) for the initial temperature distribution $f(x) = T_0 + (T_1 - T_0)x/a$.
>
> No integration is needed for $a_0$: the average of a linear function is the average of its end values, $a_0 = (T_0 + T_1)/2$. The remaining coefficients are
>
> $$
> a_n = \frac2a\int_0^a\Big(T_0 + \frac{(T_1 - T_0)x}a\Big)\cos\Big(\frac{n\pi x}a\Big)dx = 2(T_1 - T_0)\frac{\cos(n\pi) - 1}{n^2\pi^2} .
> $$
>
> (The constant $T_0$ integrates to $0$ against $\cos(n\pi x/a)$; and $\int_0^ax\cos(n\pi x/a)\,dx = \big[\frac{ax}{n\pi}\sin\frac{n\pi x}a\big]_0^a - \frac a{n\pi}\int_0^a\sin\frac{n\pi x}a\,dx = \frac{a^2}{n^2\pi^2}(\cos n\pi - 1)$.) So $a_n = -4(T_1 - T_0)/(n^2\pi^2)$ for odd $n$ and $a_n = 0$ for even $n \ge 2$, and the solution is (9) with these coefficients:
>
> $$
> u(x, t) = \frac{T_0 + T_1}2 - \frac{4(T_1 - T_0)}{\pi^2}\sum_{n\ \text{odd}}\frac1{n^2}\cos\Big(\frac{n\pi x}a\Big)\exp\Big(-\frac{n^2\pi^2kt}{a^2}\Big) .
> $$
>
> For $T_0 = 20$, $T_1 = 100$ Powers tabulates the temperature $u(0, t)$ of the cold end; recomputed from the series (400 terms), it is
>
> | $kt/a^2$ | 0.001 | 0.003 | 0.01 | 0.03 | 0.1 | 0.3 | 1 |
> |---|---|---|---|---|---|---|---|
> | $u(0, t)$ | 22.9 | 24.9 | 29.0 | 35.6 | 47.9 | 58.3 | 60.0 |
>
> The cold end warms quickly at first, then more and more slowly, approaching the average $60$; by $kt/a^2 = 1$ it is indistinguishable from it.
>
> *Powers: 2.4, Example; Exercise 2.4.12*

^ex-26-1

![[m341-20-1.svg]]
*Example §20.1 with $T_0 = 20$, $T_1 = 100$: $u(x, t)$ as a function of $x$ at $kt/a^2 = 0.001$, $0.01$, $0.1$, $1$. The insulated ends force zero slope ($u_x = 0$) at both ends at every $t > 0$, so the profile bends flat there at once; the area under the curve (the total heat) stays fixed while the profile flattens to the average $a_0 = 60$.*

> [!example] Example §26.2: Prescribed Heat Flow at Both Ends
> Consider $u_{xx} = \frac1ku_t$, $0 < x < a$, with $u_x(0, t) = S_0$, $u_x(a, t) = S_1$ and $u(x, 0) = f(x)$.
>
> **The steady-state problem has a solution if and only if $S_0 = S_1$.** It is $v'' = 0$, $v'(0) = S_0$, $v'(a) = S_1$. With $v = Ax + B$, the conditions say $A = S_0$ and $A = S_1$. So if $S_0 \ne S_1$ there is no solution, and if $S_0 = S_1$ then $v(x) = S_0x + B$ with $B$ arbitrary (take $B = 0$). Physical reason: the heat flux $q = -\kappa u_x$ is $-\kappa S_0$ at the left end and $-\kappa S_1$ at the right, so heat enters the rod at the net rate $A\kappa(S_1 - S_0)$ ([[§26 Example꞉ Insulated Bar#^rem-26-1|Remark: Why the Limit Is the Average]]). In a steady state nothing changes, so heat in must equal heat out.
>
> **If $S_0 = S_1$**, the transient $w = u - v$ satisfies $w_{xx} = \frac1kw_t$, $w_x(0, t) = w_x(a, t) = 0$, $w(x, 0) = f(x) - S_0x$: the insulated-bar problem, solved by Theorem §26.2.
>
> **If $S_0 \ne S_1$**, try $u(x, t) = A\big(kt + \frac12x^2\big) + Bx$. Then $u_{xx} = A$ and $\frac1ku_t = \frac1kAk = A$, so $u$ satisfies the heat equation for any $A$ and $B$; and $u_x = Ax + B$, so $u_x(0, t) = B = S_0$, $u_x(a, t) = Aa + B = S_1$ give $B = S_0$, $A = (S_1 - S_0)/a$. This $u$ grows (or falls) linearly in time without bound, at the rate $Ak = k(S_1 - S_0)/a$: heat keeps accumulating. Subtracting it from the solution leaves an insulated-bar problem.
>
> *Source: 341 lecture 9.26; Powers: Exercise 2.4.5*

^ex-26-2

> [!example] Example §26.3: Flux Boundary Conditions on the Midterm
> Solve the heat equation
>
> $$
> u_t = u_{xx}, \quad 0 < x < 1,\ t > 0; \qquad u(x, 0) = 4x; \qquad u_x(0, t) = 1, \quad u_x(1, t) = 1 .
> $$
>
> **(a) Steady state.** $v_{xx} = 0$, $v_x(0) = 1$, $v_x(1) = 1$. Since the fluxes are equal, by Example §26.2 the solutions are $v(x) = x + C$; take $v(x) = x$.
>
> **(b) Transient.** $w = u - v$: $w_t = w_{xx}$; $w(x, 0) = 4x - x = 3x$; $w_x(0, t) = 0$, $w_x(1, t) = 0$.
>
> **(c) Separation.** $w_n = \phi(x)T(t)$ gives $\phi T' = \phi''T$, so $\dfrac{\phi''}\phi = \dfrac{T'}T = p$, a real number: $\phi'' = p\phi$, $T' = pT$, with $\phi'(0) = 0 = \phi'(1)$.
>
> **(d) Basic solutions, three cases.**
> - $p > 0$, $p = \lambda^2$: $\phi = Ae^{\lambda x} + Be^{-\lambda x}$, $\phi' = \lambda(Ae^{\lambda x} - Be^{-\lambda x})$. $\phi'(0) = \lambda(A - B) = 0$ and $\phi'(1) = \lambda(Ae^\lambda - Be^{-\lambda}) = 0$ give $A = B$ and $A(e^\lambda - e^{-\lambda}) = 0$, so $A = B = 0$: no nonzero solution.
> - $p = 0$: $\phi = A + Bx$, $\phi' = B = 0$: nonzero solutions $\phi =$ constant, with $T =$ constant.
> - $p < 0$, $p = -\lambda^2$: $\phi = A\sin\lambda x + B\cos\lambda x$, $\phi' = \lambda A\cos\lambda x - \lambda B\sin\lambda x$. $\phi'(0) = \lambda A = 0$ gives $A = 0$; $\phi'(1) = -\lambda B\sin\lambda = 0$ gives nonzero solutions when $\lambda = n\pi$: $\phi = \cos(n\pi x)$.
>
> In conclusion (Theorem §26.1 with $a = 1$): $p = -(n\pi)^2$, $\phi_n = \cos(n\pi x)$, $T_n = e^{-(n\pi)^2t}$, and the basic solutions are $w_n(x, t) = e^{-(n\pi)^2t}\cos(n\pi x)$, $n = 0, 1, 2, \ldots$.
>
> **(e) Coefficients.** $w = \sum_{n=0}^\infty c_nw_n$, and at $t = 0$, $3x = \sum_{n=0}^\infty c_n\cos(n\pi x)$ on $0 < x < 1$:
>
> $$
> c_0 = \int_0^13x\,dx = \frac32, \qquad c_n = 2\int_0^13x\cos(n\pi x)\,dx = \frac6{(n\pi)^2}\big((-1)^n - 1\big) .
> $$
>
> So
>
> $$
> u(x, t) = x + \frac32 + \sum_{n=1}^\infty\frac6{(n\pi)^2}\big((-1)^n - 1\big)e^{-(n\pi)^2t}\cos(n\pi x) .
> $$
>
> Check with conservation of heat: the fluxes are equal, so the average temperature stays $\int_0^14x\,dx = 2$; and indeed the limit $x + \frac32$ has average $\frac12 + \frac32 = 2$.
>
> **The same problem on $0 < x < a$** with $u(x, 0) = x^2 + x$ and $u_x(0, t) = u_x(a, t) = 1$: $v = x$, $w(x, 0) = x^2$, and the constant term $n = 0$ must be included in $w = \sum a_nw_n$:
>
> $$
> a_0 = \frac1a\int_0^ax^2\,dx = \frac{a^2}3, \qquad a_n = \frac2a\int_0^ax^2\cos\Big(\frac{n\pi x}a\Big)dx = \frac{4a^2(-1)^n}{n^2\pi^2} ,
> $$
>
> (integrating by parts twice), so $u = x + \frac{a^2}3 + \sum_{n=1}^\infty\frac{4a^2(-1)^n}{n^2\pi^2}e^{-(n\pi/a)^2t}\cos\frac{n\pi x}a$.
>
> *In the homework key the transient's initial condition is written $w_x(x, 0) = x^2$; it should be $w(x, 0) = x^2$, which is what the key's coefficients use.*
>
> *Source: 341 Midterm 1, Q2; 341 HW 5, Problem 2*

^ex-26-3
