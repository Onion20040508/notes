---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 46
powers: "5.6"
aliases: ["Powers 5.6"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§45★ Bessel's Equation]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§47★ Vibrations of a Circular Membrane]] →

*Powers, Section 5.6.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section solves the heat equation in a long cylinder whose temperature depends only on the distance $r$ from the axis, the first full use of Bessel functions. A problem that is two-dimensional in rectangular coordinates becomes one-dimensional in polar coordinates, and separation of variables leads to Bessel's equation of order $0$; the eigenfunctions are $J_0(\lambda_n r)$, where $\lambda_n a$ runs through the zeros of $J_0$, and they play the role that $\sin(n\pi x/a)$ played for the rod in [[§19 Example꞉ Fixed End Temperatures#^thm-19-2|Theorem §19.2]]. The new tool is the **Fourier–Bessel series**: the eigenfunctions are orthogonal with weight $r$, which gives the coefficient formula, and a convergence theorem like the one for Fourier series guarantees that the initial condition can be met. Physically this is the cooling of a cylinder (or the diffusion of a substance in one) whose surface is held at temperature zero; the same eigenvalue problem gives the radially symmetric vibrations of a drum in [[§47★ Vibrations of a Circular Membrane#^prop-47-1|Proposition §47.1]].

## The Problem and Separation of Variables

If the unknown function $v(r, \theta, t)$ does not depend on the angle $\theta$ (write $v(r, t)$), the polar form of the two-dimensional Laplacian ([[§44★ Problems in Polar Coordinates#^def-44-1|Definition §44.1]]) loses its $\theta$-term:

$$
\nabla^2 v = \frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) .
$$

Suppose the temperature $v(r, t)$ in a large cylinder of radius $a$ satisfies

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) &= \frac{1}{k}\frac{\partial v}{\partial t}, && 0 < r < a, \quad 0 < t, && (1)\\
v(a, t) &= 0, && 0 < t, && (2)\\
v(r, 0) &= f(r), && 0 < r < a. && (3)
\end{aligned}
$$

The differential equation (1) and the boundary condition (2) are homogeneous, so we try $v(r, t) = \phi(r)T(t)$. Then (1) becomes $\frac{1}{r}(r\phi')'T = \frac{1}{k}\phi T'$, and dividing by $\phi T$,

$$
\frac{(r\phi'(r))'}{r\phi(r)} = \frac{T'(t)}{kT(t)} . \qquad (4)
$$

The left side depends only on $r$ and the right side only on $t$, so both equal a constant, called $-\lambda^2$:

$$
T' + \lambda^2kT = 0, \quad 0 < t, \qquad (5) \qquad\qquad (r\phi')' + \lambda^2r\phi = 0, \quad 0 < r < a . \qquad (6)
$$

The boundary condition (2) becomes $\phi(a)T(t) = 0$ for $t > 0$, which holds if

$$
\phi(a) = 0 . \qquad (7)
$$

Equation (6) is Bessel's equation with $\mu = 0$ ([[§45★ Bessel's Equation#^thm-45-5|Theorem §45.5]], Powers' Summary), whose general solution is $AJ_0(\lambda r) + BY_0(\lambda r)$. Since $Y_0$ becomes infinite as $r \to 0$ and an infinite temperature on the axis is physically unacceptable, we add the **boundedness condition**

$$
|v(r, t)| \ \text{bounded at } r = 0 , \qquad (8)
$$

which will be used again and again: at the singular point $r = 0$ of (6) it takes the place of a boundary condition ([[§4★ Singular Boundary Value Problems#^def-4-2|Definition §4.2]]).

## The Eigenvalue Problem

> [!theorem] Proposition §46.1: Eigenvalues and Eigenfunctions of the Radial Problem
> Let $0 < \alpha_1 < \alpha_2 < \cdots$ be the positive zeros of $J_0$ ($\alpha_1 = 2.405$, $\alpha_2 = 5.520$, $\alpha_3 = 8.654$, $\alpha_4 = 11.792, \ldots$). The singular eigenvalue problem
>
> $$
> (r\phi')' + \lambda^2r\phi = 0, \quad 0 < r < a, \qquad \phi(a) = 0, \qquad |\phi(0)| \text{ bounded}
> $$
>
> has a nonzero solution exactly when $\lambda^2$ is one of the eigenvalues
>
> $$
> \lambda_n^2 = \Big(\frac{\alpha_n}{a}\Big)^2, \qquad n = 1, 2, \ldots , \qquad (9)
> $$
>
> and the corresponding eigenfunctions are the multiples of $\phi_n(r) = J_0(\lambda_n r)$. The eigenfunction $\phi_n$ has $n - 1$ zeros in $0 < r < a$, at $r = (\alpha_k/\alpha_n)a$, $k = 1, \ldots, n - 1$.
>
> *Powers: 5.6, Equation (9)*

^prop-46-1

> [!proof]+ Proof
> **The separation constant is negative.** (Powers names the constant $-\lambda^2$ without discussing the other signs; here is why they give nothing.) If the constant is $0$, then $(r\phi')' = 0$, so $r\phi' = B$ and $\phi = A + B\ln r$; boundedness at $0$ forces $B = 0$, and $\phi(a) = A = 0$. If the constant is positive, $+\mu^2$ with $\mu > 0$, then $(r\phi')' - \mu^2r\phi = 0$ is the modified Bessel equation of order $0$ ([[§45★ Properties of Bessel Functions#^def-45-4|Definition §45.4]]), whose solution bounded at $r = 0$ is $AI_0(\mu r)$ with
>
> $$
> I_0(\mu r) = \sum_{m=0}^{\infty} \frac{1}{(m!)^2}\Big(\frac{\mu r}{2}\Big)^{2m} \ge 1
> $$
>
> ([[§45★ Properties of Bessel Functions#^thm-45-10|Theorem §45.10]]); so $\phi(a) = AI_0(\mu a) = 0$ forces $A = 0$.
>
> **The constant $-\lambda^2$, $\lambda > 0$.** The general solution of (6) is $\phi = AJ_0(\lambda r) + BY_0(\lambda r)$. Since $|Y_0(\lambda r)| \to \infty$ as $r \to 0$ while $J_0(0) = 1$, boundedness at $r = 0$ requires $B = 0$. Then (7) reads $AJ_0(\lambda a) = 0$, and a nonzero solution needs $A \ne 0$, so $J_0(\lambda a) = 0$: $\lambda a$ must be one of the zeros $\alpha_n$, giving (9). Conversely each $\phi_n = J_0(\lambda_n r)$ solves the problem. ($J_0$ is even, so negative values of $\lambda$ give nothing new.)
>
> **Zeros.** $J_0(\lambda_n r) = 0$ for $0 < r < a$ exactly when $\lambda_n r = \alpha_k$ for some $\alpha_k < \alpha_n$, that is, $r = \alpha_k/\lambda_n = (\alpha_k/\alpha_n)a$ with $k < n$.
>
> (The same problem, in Powers' Exercises 5.5.1–5.5.2, is [[§45★ Properties of Bessel Functions#^ex-45-2|Example §45.2]].)

^pf-46-1

*Uses:* [[§45★ Bessel's Equation#^thm-45-5|§45.5]], [[§45★ Properties of Bessel Functions#^thm-45-6|§45.6]] (the zeros $\alpha_n$), [[§45★ Properties of Bessel Functions#^def-45-4|Def. §45.4]], [[§45★ Properties of Bessel Functions#^def-45-new1|Def. §45.4]], [[§45★ Properties of Bessel Functions#^thm-45-10|§45.10]]

![[m341-46-2.svg]]
*The first three eigenfunctions $J_0(\lambda_n r)$, $\lambda_n = \alpha_n/a$, of Proposition §46.1. All equal $1$ on the axis and $0$ at the wall; $J_0(\lambda_n r)$ has $n - 1$ interior zeros, like $\sin(n\pi x/a)$, but its oscillations are not equally spaced and their amplitude decreases away from the axis.*

The time factors are, from (5), $T_n(t) = \exp(-\lambda_n^2kt)$. Every product $J_0(\lambda_n r)\exp(-\lambda_n^2kt)$ satisfies (1), (2) and (8), and so does a linear combination

$$
v(r, t) = \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r)\exp(-\lambda_n^2kt) . \qquad (10)
$$

The initial condition (3) then requires

$$
v(r, 0) = \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r) = f(r), \qquad 0 < r < a . \qquad (11)
$$

## Fourier–Bessel Series

The eigenvalue problem of Proposition §46.1 is not a regular Sturm–Liouville problem ([[§23 Sturm–Liouville Problems#^def-23-1|Definition §23.1]]): in the form $(s\phi')' - q\phi + \lambda^2p\phi = 0$ it has $s(r) = p(r) = r$, which vanish at the endpoint $r = 0$. Its eigenfunctions are nevertheless orthogonal, with the weight $p(r) = r$.

> [!theorem] Proposition §46.2: Orthogonality of the Functions J₀(λₙr)
> If $\lambda_n = \alpha_n/a$ as in Proposition §46.1, then
>
> $$
> \int_0^a \phi_n(r)\phi_m(r)\,r\,dr = \int_0^a J_0(\lambda_n r)J_0(\lambda_m r)\,r\,dr = 0, \qquad n \ne m .
> $$
>
> *Powers: 5.6 (text)*

^prop-46-2

> [!proof]+ Proof
> Powers refers to the Sturm–Liouville argument of [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] and its singular version, Exercise 2.7.6; here it is for this problem. The eigenfunctions satisfy
>
> $$
> (r\phi_n')' = -\lambda_n^2r\phi_n, \qquad (r\phi_m')' = -\lambda_m^2r\phi_m .
> $$
>
> Multiply the first by $\phi_m$, the second by $\phi_n$, and subtract:
>
> $$
> (r\phi_n')'\phi_m - (r\phi_m')'\phi_n = (\lambda_m^2 - \lambda_n^2)\,r\phi_n\phi_m .
> $$
>
> By the product rule the left side is a derivative, $\big[r(\phi_n'\phi_m - \phi_m'\phi_n)\big]'$, because the terms $r\phi_n'\phi_m'$ cancel. Integrate from $0$ to $a$:
>
> $$
> (\lambda_m^2 - \lambda_n^2)\int_0^a \phi_n\phi_m\,r\,dr = \Big[r\big(\phi_n'(r)\phi_m(r) - \phi_m'(r)\phi_n(r)\big)\Big]_0^a .
> $$
>
> At $r = a$ the bracket vanishes because $\phi_n(a) = \phi_m(a) = 0$. At $r = 0$ it vanishes because of the factor $r$: $J_0$ is a power series converging for all arguments, so $\phi_n$, $\phi_m$ and their derivatives are bounded near $r = 0$. (This is where the boundedness condition replaces a boundary condition.) Since $\lambda_m^2 \ne \lambda_n^2$ for $m \ne n$, the integral is $0$.

^pf-46-2

*Uses:* [[§46★ Temperature in a Cylinder#^prop-46-1|§46.1]], [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]] (the same computation)

> [!remark]- Connections
> - Finite-dimensional analogue: eigenvectors of a self-adjoint (indeed of any normal) operator for distinct eigenvalues are orthogonal, [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]]. Here the operator is $\phi \mapsto -\frac{1}{r}(r\phi')'$ on functions with $\phi(a) = 0$, bounded at $0$, and the computation above shows that it is symmetric for the weighted inner product $\langle f, g\rangle = \int_0^a f(r)g(r)\,r\,dr$.
> - In that inner product the functions $J_0(\lambda_n r)$ form an orthogonal set in the sense of [[§24 Orthonormal Sets and Bases#^def-24-1|556 Def. §24.1]]. The weight $r$ is the polar area element: $\int_0^a\!\int_{-\pi}^{\pi} F\,r\,d\theta\,dr$ is the integral over the disk, [[§100 Double Integrals in Polar Coordinates#^thm-100-1|Calc Thm. §100.1]].

The orthogonality relation tells how to choose the coefficients in (11): multiply both sides by $J_0(\lambda_m r)\,r$ and integrate from $0$ to $a$. All terms but the one with $n = m$ vanish, which leaves $\int_0^a f(r)J_0(\lambda_m r)\,r\,dr = a_m\int_0^a J_0^2(\lambda_m r)\,r\,dr$.

> [!definition] Definition §46.1: Fourier–Bessel Series
> Let $f$ be sectionally smooth on $0 < r < a$, and let $\lambda_n = \alpha_n/a$, where $\alpha_n$ are the positive zeros of $J_0$. The **Fourier–Bessel series** (of order $0$) of $f$ is
>
> $$
> \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r), \qquad a_n = \frac{\displaystyle\int_0^a f(r)J_0(\lambda_n r)\,r\,dr}{\displaystyle\int_0^a J_0^2(\lambda_n r)\,r\,dr} . \qquad (12)
> $$
>
> By [[§46★ Temperature in a Cylinder#^prop-46-6|Proposition §46.6]] below, the denominator is $\frac{a^2}{2}J_1^2(\alpha_n)$.
>
> *Powers: 5.6, Equation (12)*

^def-46-1

> [!theorem] Theorem §46.3: Convergence of Fourier–Bessel Series
> If $f(r)$ is sectionally smooth on the interval $0 < r < a$, then at every point $r$ of that interval
>
> $$
> \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r) = \frac{f(r+) + f(r-)}{2}, \qquad 0 < r < a ,
> $$
>
> where the $\lambda_n$ are the solutions of $J_0(\lambda a) = 0$ and the $a_n$ are given by (12).
>
> *Powers: 5.6, Theorem*

^thm-46-3

*Powers omits the proof.* It is the analogue of the Fourier convergence theorem, [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]], and of the eigenfunction expansion theorem, [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]], which Powers states for regular Sturm–Liouville problems only.

> [!remark]- Connections
> - The Hilbert-space counterpart of the theorem is that the normalized functions $J_0(\lambda_n r)/\|J_0(\lambda_n r)\|$ form an orthonormal basis of $L^2\big((0, a), r\,dr\big)$: every function orthogonal to all of them is $0$, equivalently Parseval's equality holds, [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]]. This completeness is not proved in the vault.
> - Used in Electromagnetism: Fourier–Bessel series for a cylinder with the potential given on an end face, and the two-tube electron lens — [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-2|EM Theorem §C6.3.2]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^thm-c6-3-3|EM Theorem §C6.3.3]], [[§C6.3 Separation in Cylindrical and Polar Coordinates#^ex-c6-3-1|EM Example §C6.3.1]].

## Solution of the Heat Problem

> [!theorem] Proposition §46.4: Temperature in a Cylinder
> If $f$ is sectionally smooth on $0 < r < a$, the function
>
> $$
> v(r, t) = \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r)\exp(-\lambda_n^2kt), \qquad \lambda_n = \frac{\alpha_n}{a} , \qquad (13)
> $$
>
> with the coefficients $a_n$ of the Fourier–Bessel series (12) of $f$, satisfies the heat problem (1)–(3) together with the boundedness condition (8).
>
> *Powers: 5.6, Equation (13)*

^prop-46-4

> [!proof]+ Proof
> Each term $J_0(\lambda_n r)\exp(-\lambda_n^2kt)$ is a product $\phi_n(r)T_n(t)$ with $\phi_n$ an eigenfunction of [[§46★ Temperature in a Cylinder#^prop-46-1|Proposition §46.1]] and $T_n$ a solution of (5), so it satisfies (1), (2) and (8) by the separation of variables above; hence so does the sum (10). At $t = 0$ the series is the Fourier–Bessel series of $f$, which by [[§46★ Temperature in a Cylinder#^thm-46-3|Theorem §46.3]] converges to $f(r)$ wherever $f$ is continuous, and to the average of the one-sided limits at jumps: this is (3), as nearly as possible. (As for the rod in [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]], the factors $\exp(-\lambda_n^2kt)$ with $\lambda_n \to \infty$ make the series converge very rapidly for $t > 0$; Powers does not discuss the term-by-term differentiation.)

^pf-46-4

*Uses:* [[§46★ Temperature in a Cylinder#^prop-46-1|§46.1]], [[§46★ Temperature in a Cylinder#^def-46-1|Def. §46.1]], [[§46★ Temperature in a Cylinder#^thm-46-3|§46.3]]

> [!remark] Remark: Method — Radial Problems in a Disk or Cylinder
> To solve a heat or wave problem in a disk or cylinder, $0 < r < a$, whose data do not depend on $\theta$:
> 1. Write the Laplacian as $\frac{1}{r}(rv_r)_r$, separate $v = \phi(r)T(t)$, and call the separation constant $-\lambda^2$. The radial equation is Bessel's equation of order $0$, $(r\phi')' + \lambda^2r\phi = 0$.
> 2. Add the boundedness condition at $r = 0$. It removes $Y_0$ and leaves $\phi = J_0(\lambda r)$.
> 3. Impose the condition at $r = a$. For $\phi(a) = 0$ it gives $\lambda_n = \alpha_n/a$ with $J_0(\alpha_n) = 0$; for $\phi'(a) = 0$, see [[§48★ Some Applications of Bessel Functions#^prop-48-2|Proposition §48.2]].
> 4. Solve for the time factors ($\exp(-\lambda_n^2kt)$ for heat, $\cos$ and $\sin(\lambda_nct)$ for waves) and superpose.
> 5. Find the coefficients from the initial conditions with the weighted orthogonality of Proposition §46.2: formula (12), with the norm of Proposition §46.6.
> 6. Evaluate the integrals with $\frac{d}{dx}\big(xJ_1(x)\big) = xJ_0(x)$ ([[§46★ Temperature in a Cylinder#^lem-46-5|Lemma §46.5]]) and the zeros tabulated in [[§45★ Properties of Bessel Functions#^thm-45-6|Theorem §45.6]].

^rem-46-1

## Example: Uniform Initial Temperature

Two facts about Bessel functions evaluate the integrals in (12) for simple $f$.

> [!theorem] Lemma §46.5: Two Bessel Identities
> For all $x$,
>
> $$
> J_0'(x) = -J_1(x), \qquad \frac{d}{dx}\big(xJ_1(x)\big) = xJ_0(x) . \qquad (14)
> $$
>
> Consequently $\displaystyle\int_0^b xJ_0(x)\,dx = bJ_1(b)$ for every $b$, and $\dfrac{d}{dr}J_0(\lambda r) = -\lambda J_1(\lambda r)$.
>
> *Powers: 5.6, Equation (14); Exercises 5.5.4 and 5.5.6*

^lem-46-5

> [!proof]+ Proof
> Both identities are proved from the series in [[§45★ Properties of Bessel Functions#^thm-45-7|Theorem §45.7]]: $J_0' = -J_1$ is part (b), and $\frac{d}{dx}\big(xJ_1(x)\big) = xJ_0(x)$ is part (d) with $\mu = 1$. Integrating the second identity from $0$ to $b$ gives $\int_0^b xJ_0(x)\,dx = bJ_1(b) - 0\cdot J_1(0) = bJ_1(b)$ ([[§45★ Properties of Bessel Functions#^cor-45-8|Corollary §45.8]] with $\mu = 0$), and the chain rule gives $\frac{d}{dr}J_0(\lambda r) = \lambda J_0'(\lambda r) = -\lambda J_1(\lambda r)$.

^pf-46-5

*Uses:* [[§45★ Properties of Bessel Functions#^thm-45-7|§45.7]], [[§45★ Properties of Bessel Functions#^cor-45-8|§45.8]]

> [!theorem] Proposition §46.6: The Norm of J₀(λₙr)
> If $\phi(r) = J_0(\lambda r)$ and $\lambda$ is chosen so that $\phi(a) = 0$, then
>
> $$
> \int_0^a \phi^2(r)\,r\,dr = \frac{1}{2\lambda^2}\big(a\phi'(a)\big)^2 .
> $$
>
> In particular, for $\lambda_n = \alpha_n/a$,
>
> $$
> \int_0^a J_0^2(\lambda_n r)\,r\,dr = \frac{a^2}{2}J_1^2(\lambda_n a) = \frac{a^2}{2}J_1^2(\alpha_n) . \qquad (16)
> $$
>
> *Powers: 5.6, Equation (16); Exercises 5.6.4–5.6.6*

^prop-46-6

> [!proof]+ Proof
> $\phi$ satisfies Bessel's equation of order $0$, $(r\phi')' + \lambda^2r\phi = 0$. Multiply through by $r\phi'$:
>
> $$
> (r\phi')(r\phi')' + \lambda^2r^2\phi\phi' = 0, \qquad\text{that is,}\qquad \frac{d}{dr}\big[(r\phi')^2\big] + \lambda^2r^2\frac{d}{dr}\big[\phi^2\big] = 0 ,
> $$
>
> because $\frac{d}{dr}[(r\phi')^2] = 2(r\phi')(r\phi')'$ and $\frac{d}{dr}[\phi^2] = 2\phi\phi'$ (Exercise 5.6.4). Integrate over $0 < r < a$, integrating the second term by parts:
>
> $$
> \Big[(r\phi')^2\Big]_0^a + \lambda^2\Big[r^2\phi^2\Big]_0^a - 2\lambda^2\int_0^a \phi^2\,r\,dr = 0 .
> $$
>
> Both brackets vanish at $r = 0$, and $\phi(a) = 0$ kills the second one at $r = a$. What remains is $(a\phi'(a))^2 = 2\lambda^2\int_0^a \phi^2\,r\,dr$, the first formula (Exercise 5.6.5). By [[§46★ Temperature in a Cylinder#^lem-46-5|Lemma §46.5]], $\phi'(a) = -\lambda J_1(\lambda a)$, so $(a\phi'(a))^2/(2\lambda^2) = \frac{a^2}{2}J_1^2(\lambda a)$, which is (16) (Exercise 5.6.6).

^pf-46-6

*Uses:* [[§46★ Temperature in a Cylinder#^lem-46-5|§46.5]]

> [!example] Example §46.1: A Cylinder Initially at Uniform Temperature
> Solve (1)–(3) with (8) when $f(r) = T_0$, $0 < r < a$.
>
> **Numerator of (12).** Substitute $x = \lambda_n r$ and use [[§46★ Temperature in a Cylinder#^lem-46-5|Lemma §46.5]]:
>
> $$
> \int_0^a T_0J_0(\lambda_n r)\,r\,dr = \frac{T_0}{\lambda_n^2}\int_0^{\alpha_n} xJ_0(x)\,dx = \frac{T_0}{\lambda_n^2}\,\alpha_nJ_1(\alpha_n) = T_0\frac{a^2}{\alpha_n}J_1(\alpha_n) . \qquad (15)
> $$
>
> (Equivalently, $\int_0^a J_0(\lambda_n r)\,r\,dr = \frac{1}{\lambda_n}rJ_1(\lambda_n r)\big|_0^a$.)
>
> **Denominator.** By [[§46★ Temperature in a Cylinder#^prop-46-6|Proposition §46.6]] it is $\frac{a^2}{2}J_1^2(\alpha_n)$. Dividing,
>
> $$
> a_n = \frac{2T_0}{\alpha_nJ_1(\alpha_n)} , \qquad (17)
> $$
>
> and by [[§46★ Temperature in a Cylinder#^prop-46-4|Proposition §46.4]] the temperature is
>
> $$
> v(r, t) = T_0\sum_{n=1}^{\infty} \frac{2}{\alpha_nJ_1(\alpha_n)}J_0(\lambda_n r)\exp(-\lambda_n^2kt) . \qquad (18)
> $$
>
> The first coefficients (recomputed):
>
> | $n$ | $\alpha_n$ | $J_1(\alpha_n)$ | $2/(\alpha_nJ_1(\alpha_n))$ |
> |---|---|---|---|
> | 1 | 2.4048 | $+0.5191$ | $+1.6020$ |
> | 2 | 5.5201 | $-0.3403$ | $-1.0648$ |
> | 3 | 8.6537 | $+0.2715$ | $+0.8514$ |
> | 4 | 11.7915 | $-0.2325$ | $-0.7296$ |
>
> The signs of $J_1(\alpha_n)$ alternate because $J_1 = -J_0'$ and $J_0$ alternately crosses zero downward and upward. The coefficients decrease only slowly (roughly like $n^{-1/2}$), as expected for a function that does not vanish at $r = a$, where every $J_0(\lambda_n r)$ does.
>
> *Powers: 5.6, Example, Equations (15)–(18) and Table 2*

^ex-46-1

![[m341-46-1.svg]]
*The temperature (18) of Example §46.1 as a function of $r$ at the dimensionless times $kt/a^2 = 0.01$, $0.05$, $0.2$, $0.5$ (400 terms), with the initial temperature $T_0$ dashed. The wall is held at $0$, so the cylinder cools from the outside in: at first only a boundary layer near $r = a$ has cooled, while later the profile is a multiple of the first eigenfunction $J_0(2.405\,r/a)$ that decays exponentially.*

> [!example] Example §46.2: How Fast the Cylinder Cools
> In Example §46.1, find the temperature on the axis at $kt/a^2 = 0.1$ and $0.5$, and describe the behaviour for large and small times.
>
> At $r = 0$, $J_0(0) = 1$, so by (18)
>
> $$
> \frac{v(0, t)}{T_0} = \sum_{n=1}^{\infty} \frac{2}{\alpha_nJ_1(\alpha_n)}\exp\Big(-\alpha_n^2\frac{kt}{a^2}\Big) , \qquad \alpha_1^2 = 5.7832, \quad \alpha_2^2 = 30.471, \quad \alpha_3^2 = 74.887 .
> $$
>
> **At $kt/a^2 = 0.1$:** the terms are $1.6020\,e^{-0.5783} = 0.8985$, $-1.0648\,e^{-3.0471} = -0.0506$ and $0.8514\,e^{-7.4887} = 0.0005$, so $v(0, t) \approx 0.848\,T_0$.
>
> **At $kt/a^2 = 0.5$:** the first term is $1.6020\,e^{-2.8916} = 0.0889$, and the second is about $-3 \times 10^{-7}$. So $v(0, t) \approx 0.089\,T_0$, and the whole profile is very nearly
>
> $$
> v(r, t) \approx 1.602\,T_0\,J_0\Big(2.405\frac{r}{a}\Big)\exp\Big(-5.783\frac{kt}{a^2}\Big) .
> $$
>
> For large times only the first term matters: the cylinder cools exponentially, with time constant $a^2/(5.783k)$, and the profile keeps the shape of the first eigenfunction. The center temperature has fallen to half its initial value at about $kt/a^2 = 0.2$ (the series gives $0.5015$ there).
>
> **For small times** many terms are needed. At $kt/a^2 = 0.01$ the first two terms give $0.727$, which is wrong; the full series gives $1.0000$, since the axis has not yet felt the cold wall. At $t = 0$ the series becomes $\sum_n 2/(\alpha_nJ_1(\alpha_n))$, the Fourier–Bessel series of the constant $1$ evaluated at $r = 0$. [[§46★ Temperature in a Cylinder#^thm-46-3|Theorem §46.3]] covers only $0 < r < a$, but this alternating series also converges to $1$, very slowly: the partial sums are $0.78$ after $10$ terms and $0.93$ after $100$.
>
> *Powers: 5.6, Table 2 and Figure 8; Exercise 5.6.1*

^ex-46-2

> [!example] Example §46.3: Only the Inner Half Initially Hot
> Solve the heat problem (1)–(3), with (8), if
>
> $$
> f(r) = \begin{cases} T_0, & 0 < r < a/2, \\ 0, & a/2 < r < a. \end{cases}
> $$
>
> **Numerator of (12).** Only $0 < r < a/2$ contributes. Substitute $x = \lambda_n r$, so that $r = a/2$ becomes $x = \alpha_n/2$, and use [[§46★ Temperature in a Cylinder#^lem-46-5|Lemma §46.5]]:
>
> $$
> \int_0^{a/2} T_0J_0(\lambda_n r)\,r\,dr = \frac{T_0}{\lambda_n^2}\int_0^{\alpha_n/2} xJ_0(x)\,dx = \frac{T_0}{\lambda_n^2}\,\frac{\alpha_n}{2}J_1\Big(\frac{\alpha_n}{2}\Big) = T_0\frac{a^2}{2\alpha_n}J_1\Big(\frac{\alpha_n}{2}\Big) .
> $$
>
> **Denominator.** As before, $\frac{a^2}{2}J_1^2(\alpha_n)$ by [[§46★ Temperature in a Cylinder#^prop-46-6|Proposition §46.6]]. Dividing,
>
> $$
> a_n = T_0\,\frac{J_1(\alpha_n/2)}{\alpha_nJ_1^2(\alpha_n)} ,
> \qquad
> v(r, t) = T_0\sum_{n=1}^{\infty} \frac{J_1(\alpha_n/2)}{\alpha_nJ_1^2(\alpha_n)}\,J_0(\lambda_n r)\exp(-\lambda_n^2kt) .
> $$
>
> By [[§46★ Temperature in a Cylinder#^prop-46-4|Proposition §46.4]] this solves the problem. The first coefficients (computed with SciPy, and checked by numerical integration of (12)):
>
> | $n$ | $\alpha_n$ | $J_1(\alpha_n/2)$ | $J_1^2(\alpha_n)$ | $a_n/T_0$ |
> |---|---|---|---|---|
> | 1 | 2.4048 | $+0.4989$ | $0.2695$ | $+0.7698$ |
> | 2 | 5.5201 | $+0.4228$ | $0.1158$ | $+0.6615$ |
> | 3 | 8.6537 | $-0.1804$ | $0.0737$ | $-0.2830$ |
> | 4 | 11.7915 | $-0.2959$ | $0.0540$ | $-0.4643$ |
>
> Unlike Example §46.1, the signs do not simply alternate: they follow the sign of $J_1$ at $\alpha_n/2$, which is wherever the jump of $f$ lands on the graph of $J_1$.
>
> **The jump.** At $r = a/2$, $f$ jumps from $T_0$ to $0$, so by [[§46★ Temperature in a Cylinder#^thm-46-3|Theorem §46.3]] the series at $t = 0$ converges there to $\frac12(T_0 + 0) = T_0/2$. Numerically, $500$ terms give $0.4996\,T_0$ at $r = a/2$, $1.0014\,T_0$ at $r = a/4$ and $-0.0004\,T_0$ at $r = 3a/4$.
>
> **Large times.** Only the first term survives: $v \approx 0.770\,T_0\,J_0(2.405\,r/a)\exp(-5.783\,kt/a^2)$. At $kt/a^2 = 0.2$ this gives $0.242\,T_0$ on the axis (the full series: $0.244\,T_0$). The hot core covers only a quarter of the cross-section, yet the first coefficient is $0.48$ times that of the uniformly hot cylinder ($1.602\,T_0$), not $0.25$ times: the coefficient weighs $f$ against $J_0(\lambda_1 r)$, which is largest near the axis, where the heat sits.
>
> *Powers: Exercise 5.6.3*

^ex-46-3
