---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: "58★"
powers: "5.7"
aliases: ["Powers 5.7"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§57★ Temperature in a Cylinder]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§59★ Some Applications of Bessel Functions]] →

*Powers, Section 5.7.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

This section solves the wave equation for a circular membrane fixed at its edge: a drumhead. When the initial data do not depend on the angle, the problem uses exactly the eigenfunctions $J_0(\lambda_n r)$ of [[§57★ Temperature in a Cylinder#^prop-57-1|Proposition §57.1]], with $\cos$ and $\sin(\lambda_nct)$ in place of the decaying exponentials. In general, separating $u = R(r)Q(\theta)T(t)$ gives periodic factors $\cos(m\theta)$, $\sin(m\theta)$ and Bessel functions $J_m$ of every integer order, with eigenvalues $\lambda_{mn} = \alpha_{mn}/a$ from the zeros of $J_m$. Physically, these are the standing waves (modes) of a drum: their nodal curves are circles and diameters, and since the $\alpha_{mn}$ are not integer multiples of $\alpha_{01}$, a drum, unlike a string, does not produce a musical tone.

## Symmetric Vibrations

First suppose that the initial conditions are independent of $\theta$. Then the displacement $v(r, t)$ satisfies

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial v}{\partial r}\Big) &= \frac{1}{c^2}\frac{\partial^2v}{\partial t^2}, && 0 < r < a, \quad 0 < t, && (1)\\
v(a, t) &= 0, && 0 < t, && (2)\\
v(r, 0) &= f(r), && 0 < r < a, && (3)\\
\frac{\partial v}{\partial t}(r, 0) &= g(r), && 0 < r < a. && (4)
\end{aligned}
$$

Assuming $v(r, t) = \phi(r)T(t)$, (1) becomes $\frac{1}{r}(r\phi')'T = \frac{1}{c^2}\phi T''$, and dividing by $\phi T$,

$$
\frac{(r\phi'(r))'}{r\phi(r)} = \frac{T''(t)}{c^2T(t)} = -\lambda^2 ,
$$

so that

$$
T'' + \lambda^2c^2T = 0, \quad 0 < t, \qquad (5) \qquad\qquad (r\phi')' + \lambda^2r\phi = 0, \quad 0 < r < a . \qquad (6)
$$

The boundary condition (2) is satisfied if $\phi(a) = 0$ (7), and because $r = 0$ is a singular point of (6) we add $|\phi(r)|$ bounded at $r = 0$ (8), which is equivalent to $|v(r, t)|$ bounded at $r = 0$. This is exactly the eigenvalue problem of [[§57★ Temperature in a Cylinder#^prop-57-1|Proposition §57.1]]: $\phi_n(r) = J_0(\lambda_n r)$, $\lambda_n = \alpha_n/a$ (9), where $\alpha_n$ are the zeros of $J_0$.

> [!theorem] Proposition §58.1: Symmetric Vibrations of a Circular Membrane
> If $f$ and $g$ are sectionally smooth on $0 < r < a$, the problem (1)–(4), with $|v|$ bounded at $r = 0$, is solved by
>
> $$
> v(r, t) = \sum_{n=1}^{\infty} J_0(\lambda_n r)\big[a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)\big], \qquad \lambda_n = \frac{\alpha_n}{a} , \qquad (10)
> $$
>
> where
>
> $$
> a_n = \frac{1}{D_n}\int_0^a f(r)J_0(\lambda_n r)\,r\,dr, \qquad b_n = \frac{1}{\lambda_ncD_n}\int_0^a g(r)J_0(\lambda_n r)\,r\,dr, \qquad D_n = \int_0^a \big[J_0(\lambda_n r)\big]^2\,r\,dr = \frac{a^2}{2}J_1^2(\alpha_n) .
> $$
>
> *Powers: 5.7, Equation (10) and the formulas after it*

^prop-58-1

> [!proof]+ Proof
> For each $n$, (5) with $\lambda = \lambda_n$ has the solutions $T_n(t) = a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)$, so $v_n(r, t) = \phi_n(r)T_n(t)$ satisfies (1), (2) and (8), and so does the sum (10). The initial conditions require
>
> $$
> v(r, 0) = \sum_{n=1}^{\infty} a_nJ_0(\lambda_n r) = f(r), \qquad \frac{\partial v}{\partial t}(r, 0) = \sum_{n=1}^{\infty} b_n\lambda_ncJ_0(\lambda_n r) = g(r), \qquad 0 < r < a .
> $$
>
> Both are Fourier–Bessel series ([[§57★ Temperature in a Cylinder#^def-57-1|Definition §57.1]]): $a_n$ is the coefficient of $f$ and $b_n\lambda_nc$ the coefficient of $g$, which gives the formulas, and by [[§57★ Temperature in a Cylinder#^thm-57-3|Theorem §57.3]] the series converge to $f$ and $g$. The value of $D_n$ is [[§57★ Temperature in a Cylinder#^prop-57-6|Proposition §57.6]].

^pf-58-1

*Uses:* [[§57★ Temperature in a Cylinder#^prop-57-1|§57.1]], [[§57★ Temperature in a Cylinder#^def-57-1|Def. §57.1]], [[§57★ Temperature in a Cylinder#^thm-57-3|§57.3]], [[§57★ Temperature in a Cylinder#^prop-57-6|§57.6]]

The heat problem of [[§57★ Temperature in a Cylinder#^prop-57-4|Proposition §57.4]] and this wave problem share the equilibrium solution ($0$), the eigenvalue problem and the coefficient formulas; only the time factors differ, as for the rod and the string in [[§38 Solution of the Vibrating String Problem#^thm-38-2|Theorem §38.2]].

## General Vibrations

The full problem for the membrane is

$$
\begin{aligned}
\frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial u}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2u}{\partial\theta^2} &= \frac{1}{c^2}\frac{\partial^2u}{\partial t^2}, && 0 < r < a, \quad 0 < t, && (11)\\
u(a, \theta, t) &= 0, && 0 < t, && (12)\\
|u(0, \theta, t)| &\ \text{bounded}, && 0 < t, && (13)\\
u(r, \theta + 2\pi, t) &= u(r, \theta, t), && 0 < r < a, \quad 0 < t, && (14)\\
u(r, \theta, 0) &= f(r, \theta), && 0 < r < a, && (15)\\
\frac{\partial u}{\partial t}(r, \theta, 0) &= g(r, \theta), && 0 < r < a. && (16)
\end{aligned}
$$

Following [[§54★ Problems in Polar Coordinates#^thm-54-1|Theorem §54.1]], assume $u = \phi(r, \theta)T(t)$. Equation (11) separates into

$$
T'' + \lambda^2c^2T = 0, \quad 0 < t, \qquad (17) \qquad\qquad \frac{1}{r}\frac{\partial}{\partial r}\Big(r\frac{\partial\phi}{\partial r}\Big) + \frac{1}{r^2}\frac{\partial^2\phi}{\partial\theta^2} = -\lambda^2\phi, \quad 0 < r < a . \qquad (18)
$$

Now separate $\phi(r, \theta) = R(r)Q(\theta)$. Then (18) reads $\frac{1}{r}(rR')'Q + \frac{1}{r^2}RQ'' = -\lambda^2RQ$; multiplying by $r^2$ and dividing by $RQ$,

$$
\frac{r(rR')'}{R} + \lambda^2r^2 = -\frac{Q''}{Q} = \mu^2 .
$$

The conditions (12)–(14) pass to $R$ and $Q$, and there are two problems:

$$
Q'' + \mu^2Q = 0, \quad -\pi < \theta \le \pi, \qquad Q(\theta + 2\pi) = Q(\theta) ; \qquad (19)
$$

$$
(rR')' - \frac{\mu^2}{r}R + \lambda^2rR = 0, \quad 0 < r < a, \qquad |R(0)| \text{ bounded}, \qquad R(a) = 0 . \qquad (20)
$$

> [!theorem] Proposition §58.2: Eigenfunctions of the Disk
> Let $\alpha_{mn}$ denote the $n$th positive zero of $J_m$, so that $J_m(\alpha_{mn}) = 0$ (table in [[§56★ Properties of Bessel Functions#^thm-56-1|Theorem §56.1]]), and let
>
> $$
> \lambda_{mn} = \frac{\alpha_{mn}}{a}, \qquad m = 0, 1, 2, \ldots, \quad n = 1, 2, 3, \ldots .
> $$
>
> The product solutions $\phi = R(r)Q(\theta)$ of the eigenvalue problem
>
> $$
> \nabla^2\phi = -\lambda^2\phi \ \ (0 < r < a), \qquad \phi(a, \theta) = 0, \qquad \phi(r, \theta + 2\pi) = \phi(r, \theta), \qquad \phi \text{ bounded at } r = 0
> $$
>
> are, up to constant multiples,
>
> $$
> J_0(\lambda_{0n}r) \quad (m = 0), \qquad J_m(\lambda_{mn}r)\cos(m\theta), \quad J_m(\lambda_{mn}r)\sin(m\theta) \quad (m \ge 1), \qquad (21), (22)
> $$
>
> with eigenvalue $\lambda_{mn}^2$. For $m \ge 1$ there are two independent eigenfunctions for the same eigenvalue.
>
> *Powers: 5.7, Equations (19)–(22)*

^prop-58-2

> [!proof]+ Proof
> **The angular problem (19).** As observed in [[§48 Potential in a Disk#^prop-48-1|Proposition §48.1]] and [[§54★ Problems in Polar Coordinates#^thm-54-2|Theorem §54.2]], the periodic problem has the solutions $\mu_0^2 = 0$, $Q_0 = 1$, and $\mu_m^2 = m^2$, $Q_m = \cos(m\theta)$ and $\sin(m\theta)$, $m = 1, 2, 3, \ldots$; a periodic solution of $Q'' + \mu^2Q = 0$ needs $\mu$ to be an integer.
>
> **The radial problem (20).** With $\mu = m$, (20) is Bessel's equation of order $m$, with general solution $R(r) = CJ_m(\lambda r) + DY_m(\lambda r)$ ([[§55★ Bessel's Equation#^thm-55-5|Theorem §55.5]]). Since $Y_m(\lambda r)$ is unbounded at $r = 0$, boundedness forces $D = 0$, and the constant $C$ can be dropped, since any multiple of a solution is a solution: $R(r) = J_m(\lambda r)$. The boundary condition becomes $R(a) = J_m(\lambda a) = 0$, so $\lambda a$ must be a root of $J_m(\alpha) = 0$: $\lambda = \alpha_{mn}/a$. Multiplying $R$ and $Q$ gives (21) and (22). (As in [[§57★ Temperature in a Cylinder#^prop-57-1|Proposition §57.1]], a separation constant $-\lambda^2 \ge 0$ produces no nonzero solutions: for $\lambda = 0$ the bounded solutions of $(rR')' - \frac{m^2}{r}R = 0$ are the multiples of $r^m$, which do not vanish at $r = a$, and a positive constant leads to the modified Bessel function $I_m$, which has no positive zeros, [[§56★ Properties of Bessel Functions#^thm-56-5|Theorem §56.5]]. See also [[§54★ Problems in Polar Coordinates#^rem-54-2|the remark on positive eigenvalues in §44]].)

^pf-58-2

*Uses:* [[§48 Potential in a Disk#^prop-48-1|§48.1]], [[§55★ Bessel's Equation#^thm-55-5|§55.5]], [[§56★ Properties of Bessel Functions#^thm-56-1|§56.1]], [[§56★ Properties of Bessel Functions#^thm-56-5|§56.5]], [[§54★ Problems in Polar Coordinates#^thm-54-2|§54.2]], [[§57★ Temperature in a Cylinder#^prop-57-1|§57.1]]

> [!definition] Definition §71.1: Standing Waves of the Membrane
> The product solutions of (11)–(14),
>
> $$
> J_m(\lambda_{mn}r)\cos(m\theta)\cos(\lambda_{mn}ct), \quad J_m(\lambda_{mn}r)\sin(m\theta)\cos(\lambda_{mn}ct), \quad J_m(\lambda_{mn}r)\cos(m\theta)\sin(\lambda_{mn}ct), \quad J_m(\lambda_{mn}r)\sin(m\theta)\sin(\lambda_{mn}ct) \qquad (23)
> $$
>
> for $m, n = 1, 2, 3, \ldots$, and, for $m = 0$,
>
> $$
> J_0(\lambda_{0n}r)\cos(\lambda_{0n}ct), \qquad J_0(\lambda_{0n}r)\sin(\lambda_{0n}ct) , \qquad (24)
> $$
>
> are the **standing waves** (normal modes) of the membrane.
>
> *Powers: 5.7, Equations (23)–(24)*

^def-58-1

> [!definition] Definition §71.2: Frequencies of the Membrane
> In the standing waves of [[§58★ Vibrations of a Circular Membrane#^def-58-1|Definition §58.1]], the mode with eigenvalue $\lambda_{mn}^2$ vibrates with **frequency** $\lambda_{mn}c = \alpha_{mn}c/a$ in radians per unit time, as for the string ([[§38 Solution of the Vibrating String Problem#^def-38-2|Definition §38.2]]).
>
> *Powers: 5.7, Equations (23)–(24)*

^def-58-2

> [!definition] Definition §58.3: Nodal Curves
> The **nodal curves** of an eigenfunction $\phi_{mn}(r, \theta)$ are the curves where $\phi_{mn}(r, \theta) = 0$. In the corresponding standing wave these points of the membrane do not move, and adjacent regions bulge up or down according to the sign of $\phi_{mn}$.
>
> *Powers: 5.7, Figure 9*

^def-58-3

The general solution of (11)–(14) is a linear combination of all the standing waves (23), (24); it uses six series:

$$
\begin{aligned}
u(r, \theta, t) = {}& \sum_n a_{0n}J_0(\lambda_{0n}r)\cos(\lambda_{0n}ct) + \sum_{m,n} a_{mn}J_m(\lambda_{mn}r)\cos(m\theta)\cos(\lambda_{mn}ct) + \sum_{m,n} b_{mn}J_m(\lambda_{mn}r)\sin(m\theta)\cos(\lambda_{mn}ct) \\
&+ \sum_n A_{0n}J_0(\lambda_{0n}r)\sin(\lambda_{0n}ct) + \sum_{m,n} A_{mn}J_m(\lambda_{mn}r)\cos(m\theta)\sin(\lambda_{mn}ct) + \sum_{m,n} B_{mn}J_m(\lambda_{mn}r)\sin(m\theta)\sin(\lambda_{mn}ct) . \qquad (25)
\end{aligned}
$$

At $t = 0$ the last three sums disappear and the cosines of $t$ equal $1$, so (15) requires

$$
\sum_n a_{0n}J_0(\lambda_{0n}r) + \sum_{m,n} a_{mn}J_m(\lambda_{mn}r)\cos(m\theta) + \sum_{m,n} b_{mn}J_m(\lambda_{mn}r)\sin(m\theta) = f(r, \theta), \qquad 0 < r < a, \quad -\pi < \theta \le \pi . \qquad (26)
$$

The coefficients come from an orthogonality principle.

> [!theorem] Proposition §58.3: Orthogonality of the Eigenfunctions of the Disk
> Any two different eigenfunctions in (21), (22) are orthogonal over the disk $\mathcal{R}$ ($dA = r\,dr\,d\theta$). For example,
>
> $$
> \iint_{\mathcal{R}} J_0(\lambda_{0n}r)J_m(\lambda_{mn}r)\cos(m\theta)\,dA = \int_0^a J_0(\lambda_{0n}r)J_m(\lambda_{mn}r)\int_{-\pi}^{\pi}\cos(m\theta)\,d\theta\;r\,dr = 0, \quad m \ne 0 , \qquad (27)
> $$
>
> $$
> \int_{-\pi}^{\pi}\!\int_0^a J_m(\lambda_{mn}r)\cos(m\theta)\,J_p(\lambda_{pq}r)\cos(p\theta)\,r\,dr\,d\theta = 0 \quad \text{if } m \ne p \text{ or } n \ne q . \qquad (28)
> $$
>
> In particular, for each fixed $m$,
>
> $$
> \int_0^a J_m(\lambda_{mn}r)J_m(\lambda_{mq}r)\,r\,dr = 0, \qquad n \ne q .
> $$
>
> *Powers: 5.7, Equations (27)–(28); Exercise 5.7.7*

^prop-58-3

> [!proof]+ Proof
> *Powers gives this as a sketch.* In polar coordinates $dA = r\,dr\,d\theta$, and each eigenfunction is a product $R(r)Q(\theta)$, so every integral over the disk splits into a $\theta$-integral times an $r$-integral.
>
> **Different angular factors.** If the angular factors are different members of $1, \cos(m\theta), \sin(m\theta)$ ($m \ge 1$), their $\theta$-integral over $-\pi < \theta \le \pi$ is $0$ by the orthogonality of the trigonometric functions ([[§9 Periodic Functions and Fourier Series#^prop-9-3|Proposition §9.3]]). This covers (27), all pairs from two different series in (25), and (28) when $m \ne p$.
>
> **Same angular factor.** If $m = p$ and the angular factors agree, the $\theta$-integral is $2\pi$ (for $m = 0$) or $\pi$ (for $m \ge 1$), and the integral reduces to $\pi\int_0^a J_m(\lambda_{mn}r)J_m(\lambda_{mq}r)\,r\,dr$ (or $2\pi$ times it). For $n \ne q$ this is $0$ by the usual Sturm–Liouville argument ([[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]]), as in [[§57★ Temperature in a Cylinder#^prop-57-2|Proposition §57.2]]: $R_n = J_m(\lambda_{mn}r)$ and $R_q = J_m(\lambda_{mq}r)$ satisfy
>
> $$
> (rR_n')' - \frac{m^2}{r}R_n = -\lambda_{mn}^2rR_n, \qquad (rR_q')' - \frac{m^2}{r}R_q = -\lambda_{mq}^2rR_q .
> $$
>
> Multiply the first by $R_q$, the second by $R_n$ and subtract; the terms $\frac{m^2}{r}R_nR_q$ cancel, and what remains is
>
> $$
> \big[r(R_n'R_q - R_q'R_n)\big]' = (\lambda_{mq}^2 - \lambda_{mn}^2)\,rR_nR_q .
> $$
>
> Integrating from $0$ to $a$, the bracket vanishes at $a$ (where $R_n = R_q = 0$) and at $0$ (because of the factor $r$; $J_m$ is given by a power series, so $R_n$, $R_q$ and their derivatives are bounded). Since $\lambda_{mn} \ne \lambda_{mq}$ for $n \ne q$, the integral is $0$.

^pf-58-3

*Uses:* [[§58★ Vibrations of a Circular Membrane#^prop-58-2|§58.2]], [[§57★ Temperature in a Cylinder#^prop-57-2|§57.2]], [[§29 Sturm–Liouville Problems#^thm-29-2|§29.2]], [[§9 Periodic Functions and Fourier Series#^prop-9-3|§9.3]], [[§117 Double Integrals in Polar Coordinates#^thm-117-1|Calc Thm. §117.1]] ($dA = r\,dr\,d\theta$)

> [!remark]- Connections
> - All eigenfunctions of $\nabla^2\phi = -\lambda^2\phi$ with $\phi = 0$ on the boundary, for any region, are orthogonal when their eigenvalues differ; that is [[§54★ Problems in Polar Coordinates#^thm-54-3|Theorem §54.3]] (Powers' Exercise 5.4.7), a consequence of Green's second identity, [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]]. The proof above does the disk by hand, and also handles the pairs with the same eigenvalue ($\cos(m\theta)$ against $\sin(m\theta)$), which Green's identity does not separate.
> - Finite-dimensional analogue: [[§23 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]].

> [!theorem] Proposition §58.4: General Vibrations of a Circular Membrane
> If the initial displacement $f(r, \theta)$ has an expansion (26), its coefficients are
>
> $$
> a_{0n} = \frac{\displaystyle\int_{-\pi}^{\pi}\!\int_0^a f(r, \theta)J_0(\lambda_{0n}r)\,r\,dr\,d\theta}{\displaystyle 2\pi\int_0^a J_0^2(\lambda_{0n}r)\,r\,dr}, \qquad (29)
> $$
>
> $$
> a_{mn} = \frac{\displaystyle\int_{-\pi}^{\pi}\!\int_0^a f(r, \theta)J_m(\lambda_{mn}r)\cos(m\theta)\,r\,dr\,d\theta}{\displaystyle \pi\int_0^a J_m^2(\lambda_{mn}r)\,r\,dr}, \qquad b_{mn} = \frac{\displaystyle\int_{-\pi}^{\pi}\!\int_0^a f(r, \theta)J_m(\lambda_{mn}r)\sin(m\theta)\,r\,dr\,d\theta}{\displaystyle \pi\int_0^a J_m^2(\lambda_{mn}r)\,r\,dr} .
> $$
>
> The coefficients $A_{0n}$, $A_{mn}$, $B_{mn}$ are given by the same formulas with $g(r, \theta)$ in place of $f$, divided by $\lambda_{0n}c$, respectively $\lambda_{mn}c$. With these coefficients, (25) is the solution of the membrane problem (11)–(16).
>
> *Powers: 5.7, Equations (25)–(29)*

^prop-58-4

> [!proof]+ Proof
> Multiply (26) by one eigenfunction, say $J_m(\lambda_{mn}r)\cos(m\theta)$, and integrate over the disk with $dA = r\,dr\,d\theta$. By [[§58★ Vibrations of a Circular Membrane#^prop-58-3|Proposition §58.3]] every term but one integrates to $0$, which leaves
>
> $$
> \iint_{\mathcal{R}} f\,J_m(\lambda_{mn}r)\cos(m\theta)\,dA = a_{mn}\int_{-\pi}^{\pi}\cos^2(m\theta)\,d\theta\int_0^a J_m^2(\lambda_{mn}r)\,r\,dr = a_{mn}\,\pi\int_0^a J_m^2(\lambda_{mn}r)\,r\,dr .
> $$
>
> For $m = 0$ the $\theta$-integral of $1^2$ is $2\pi$, which gives (29). Powers calculates only $a_{0n}$ and states that the others follow in the same way. For the $A$'s and $B$'s, differentiate (25) in $t$ and set $t = 0$: the first three sums disappear and the last three become the same kind of series with coefficients $\lambda_{0n}cA_{0n}$, $\lambda_{mn}cA_{mn}$, $\lambda_{mn}cB_{mn}$, which must represent $g$.

^pf-58-4

*Uses:* [[§58★ Vibrations of a Circular Membrane#^prop-58-3|§58.3]]

> [!remark] Remark: What the Solution Tells Us
> Computing the solution (25) is possible in theory but very painful in practice, and the final form does not show clearly what $u$ looks like. Two things can still be read off.
> - **The tone is not musical.** The frequencies $\alpha_{mn}c/a$ are not integer multiples of the lowest one, $\alpha_{01}c/a$, so $u$ is not periodic in $t$ (see Example §58.1).
> - **The shapes of the modes.** The nodal curves of each eigenfunction can be sketched from the zeros of $J_m$ and of $\cos(m\theta)$ (see Example §58.2).
>
> The integral $\int_0^a J_m^2(\lambda_{mn}r)\,r\,dr$ can be evaluated as in [[§57★ Temperature in a Cylinder#^prop-57-6|Proposition §57.6]]: multiplying Bessel's equation of order $m$ by $rR'$ and integrating gives $\frac{a^2}{2}\big(J_m'(\alpha_{mn})\big)^2$, the same computation with the extra term $-m^2RR'$, which integrates to $0$ because $R(0) = R(a) = 0$ for $m \ge 1$.

^rem-58-1

> [!example] Example §71.1: The Overtones of a Drum Are Not Harmonic
> List the lowest frequencies of a circular membrane as multiples of the lowest one, and compare with a string.
>
> The frequencies are $\alpha_{mn}c/a$. From the zeros of $J_0, \ldots, J_5$ (the table in [[§56★ Properties of Bessel Functions#^thm-56-1|Theorem §56.1]], with $\alpha_{41} = 7.588$ and $\alpha_{51} = 8.771$ added), in increasing order:
>
> | mode $(m, n)$ | $(0,1)$ | $(1,1)$ | $(2,1)$ | $(0,2)$ | $(3,1)$ | $(1,2)$ | $(4,1)$ | $(2,2)$ | $(0,3)$ | $(5,1)$ |
> |---|---|---|---|---|---|---|---|---|---|---|
> | $\alpha_{mn}$ | 2.405 | 3.832 | 5.136 | 5.520 | 6.380 | 7.016 | 7.588 | 8.417 | 8.654 | 8.771 |
> | $\alpha_{mn}/\alpha_{01}$ | 1 | 1.593 | 2.136 | 2.295 | 2.653 | 2.917 | 3.155 | 3.500 | 3.598 | 3.647 |
>
> The modes with $m \ge 1$ count twice ($\cos(m\theta)$ and $\sin(m\theta)$). A string fixed at both ends has frequencies $n\pi c/a$, exactly $1, 2, 3, \ldots$ times the fundamental ([[§38 Solution of the Vibrating String Problem#^def-38-2|Definition §38.2]]), so every solution of the string problem is periodic in $t$ and sounds as a musical note. The drum's overtones lie at irrational-looking ratios, and they crowd together as the frequency increases. A superposition of drum modes is in general not periodic in $t$.
>
> *Powers: 5.7 (text), with the zeros of 5.5, Table 1*

^ex-58-1

![[m341-47-2.svg]]
*Frequencies of the lowest modes of a circular membrane (top; label $mn$, blue for the radially symmetric modes $m = 0$, red for the doubly counted modes $m \ge 1$), divided by the fundamental $\alpha_{01}c/a$, against the harmonic frequencies $1, 2, 3, 4$ of a string (bottom).*

> [!example] Example §71.2: Nodal Curves of the Lowest Modes
> Find the nodal curves of the eigenfunctions $\phi_{mn} = J_m(\lambda_{mn}r)\cos(m\theta)$ for $m = 0, 1, 2$ and $n = 1, 2, 3$.
>
> **Circles.** $J_m(\lambda_{mn}r) = 0$ for $0 < r < a$ exactly when $\lambda_{mn}r = \alpha_{mk}$ with $k < n$, that is, on the circles
>
> $$
> r = \frac{\alpha_{mk}}{\alpha_{mn}}\,a, \qquad k = 1, \ldots, n - 1 .
> $$
>
> So $\phi_{m1}$ has no nodal circle inside the disk, $\phi_{m2}$ has one and $\phi_{m3}$ has two. For example, $\phi_{02}$ has a nodal circle at $r = (2.405/5.520)a = 0.436a$; $\phi_{03}$ has two, at $(2.405/8.654)a = 0.278a$ and $(5.520/8.654)a = 0.638a$; $\phi_{12}$ has one at $(3.832/7.016)a = 0.546a$; $\phi_{22}$ one at $(5.136/8.417)a = 0.610a$.
>
> **Diameters.** $\cos(m\theta) = 0$ exactly when $m\theta = \pm\frac{\pi}{2}, \pm\frac{3\pi}{2}, \ldots$, so for $m \ge 1$ there are $m$ nodal diameters, at angles $\theta = \frac{\pi}{2m} + \frac{k\pi}{m}$. Thus $\phi_{1n}$ has the diameter $\theta = \pm\frac{\pi}{2}$ (the $y$-axis) and $\phi_{2n}$ the two diameters $\theta = \pm\frac{\pi}{4}$, $\pm\frac{3\pi}{4}$. Using $\sin(m\theta)$ instead rotates the pattern by $\pi/(2m)$; a combination $A\cos(m\theta) + B\sin(m\theta)$ rotates it by some other angle.
>
> So the nodal curves of $\phi_{mn}$ are $n - 1$ circles and $m$ diameters, which divide the disk into $n \cdot \max(2m, 1)$ regions where the membrane alternately bulges up and down.
>
> *Powers: 5.7, Figure 9*

^ex-58-2

![[m341-47-1.svg]]
*Six eigenfunctions $\phi_{mn} = J_m(\alpha_{mn}r/a)\cos(m\theta)$ of the disk, with their nodal circles and diameters in black; between them $\phi_{mn} > 0$ (blue, $+$) or $\phi_{mn} < 0$ (red, $-$), the shade darker where the largest value of $|\phi_{mn}|$ in the region is larger. Above each, the frequency of the mode relative to the fundamental. Each picture is a snapshot of the corresponding standing wave; half a period later the signs are exchanged.*

> [!example] Example §71.3: Identifying a Mode from Its Nodal Curves
> The nodal curves of an eigenfunction $\phi_{mn}(r, \theta)$ of the disk of radius $a$ are the boundary circle, one interior circle of radius about $0.65a$, and three diameters, at $\theta = 0$, $\pi/3$ and $2\pi/3$ (Powers' Figure 10). (a) Find $m$ and $n$. (b) Find the eigenvalue $\lambda_{mn}$. (c) Find $\phi_{mn}$. (d) Find the frequency of the drumhead vibrating in this mode.
>
> **(a)** By [[§58★ Vibrations of a Circular Membrane#^ex-58-2|Example §58.2]], the nodal curves of $\phi_{mn}$ are $m$ diameters and $n - 1$ interior circles. Three diameters give $m = 3$, and one interior circle gives $n = 2$.
>
> **(b)** $\lambda_{32} = \alpha_{32}/a$, where $\alpha_{32}$ is the second positive zero of $J_3$: $\alpha_{31} = 6.380$, $\alpha_{32} = 9.761$, so $\lambda_{32} = 9.761/a$ and the eigenvalue is $\lambda_{32}^2 = 95.28/a^2$. Check: the interior nodal circle is at $r = (\alpha_{31}/\alpha_{32})a = (6.380/9.761)a = 0.654a$, as in the figure.
>
> **(c)** The eigenfunctions for $\lambda_{32}^2$ are $J_3(\lambda_{32}r)\big(A\cos(3\theta) + B\sin(3\theta)\big)$, by [[§58★ Vibrations of a Circular Membrane#^prop-58-2|Proposition §58.2]]. The angular factor must vanish at $\theta = 0$, $\pi/3$, $2\pi/3$ (and at the opposite ends of these diameters). At $\theta = 0$ this forces $A = 0$, and $\sin(3\theta) = 0$ exactly at $\theta = k\pi/3$. So, up to a constant factor,
>
> $$
> \phi_{32}(r, \theta) = J_3\Big(9.761\,\frac{r}{a}\Big)\sin(3\theta) .
> $$
>
> It changes sign across each nodal curve, so the $12$ regions bulge alternately up and down.
>
> **(d)** By [[§58★ Vibrations of a Circular Membrane#^def-58-2|Definition §58.2]], the displacement $u = \phi_{32}(r, \theta)\big(C\cos(\lambda_{32}ct) + D\sin(\lambda_{32}ct)\big)$ has the frequency
>
> $$
> \lambda_{32}c = 9.761\,\frac{c}{a} \ \text{radians per unit time}, \qquad\text{that is,}\qquad \frac{9.761}{2\pi}\,\frac{c}{a} = 1.554\,\frac{c}{a} \ \text{cycles per unit time},
> $$
>
> $\alpha_{32}/\alpha_{01} = 4.059$ times the fundamental frequency, again not an integer multiple (compare [[§58★ Vibrations of a Circular Membrane#^ex-58-1|Example §58.1]]).
>
> *Powers: Exercise 5.7.10*

^ex-58-3
