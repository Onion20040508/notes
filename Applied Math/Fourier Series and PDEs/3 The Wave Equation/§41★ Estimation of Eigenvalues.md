---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: "41★"
powers: "3.5"
aliases: ["Powers 3.5"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§40 One-Dimensional Wave Equation꞉ Generalities]] · ↑ [[· 3 The Wave Equation]] · [[§42★ Wave Equation in Unbounded Regions]] →

*Powers, Section 3.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Often one wants not the full solution of a wave problem but only the frequencies at which a structure can vibrate: bridges, airplane wings and other structures must not be driven at them. By [[§40 One-Dimensional Wave Equation꞉ Generalities#^thm-40-2|Theorem §40.2]] these frequencies are $\lambda_nc/2\pi$, so the eigenvalues $\lambda_n^2$ of a Sturm–Liouville problem must be found, and for nonuniform coefficients they usually cannot be found exactly. **Rayleigh's method** gives an upper bound for the lowest eigenvalue from any reasonable guess $y$ of the eigenfunction: $\lambda_1^2$ is the minimum of the **Rayleigh quotient** $N(y)/D(y)$, a ratio of two integrals, and a good guess gives a good estimate. In mechanical terms the quotient compares potential and kinetic energy.

## The Rayleigh Quotient

Consider the Sturm–Liouville problem

$$
(s(x)\phi')' - q(x)\phi + \lambda^2p(x)\phi = 0, \quad l < x < r, \qquad (1) \qquad\qquad \phi(l) = 0, \quad \phi(r) = 0, \qquad (2)
$$

where $s$, $s'$, $q$ and $p$ are continuous and $s$ and $p$ are positive for $l \le x \le r$. (The differential equation is rather general, but the boundary conditions are very special.)

> [!definition] Definition §51.1: Rayleigh Quotient
> For a function $y$ on $l \le x \le r$, let
>
> $$
> N(y) = \int_l^rs(x)\big[y'(x)\big]^2dx + \int_l^rq(x)y^2(x)\,dx, \qquad D(y) = \int_l^rp(x)y^2(x)\,dx .
> $$
>
> The ratio $N(y)/D(y)$ (defined when $y \not\equiv 0$, since then $D(y) > 0$) is the **Rayleigh quotient** of the problem (1)–(2). Estimating the first eigenvalue by $N(y)/D(y)$ for a convenient **trial function** $y$ is **Rayleigh's method**.
>
> *Powers: 3.5, Equation (3) and text*

^def-41-1

> [!theorem] Proposition §51.1: The First Eigenvalue Is the Rayleigh Quotient of Its Eigenfunction
> If $\phi_1$ is the eigenfunction of (1)–(2) corresponding to the smallest eigenvalue $\lambda_1^2$, then
>
> $$
> \lambda_1^2 = \frac{\int_l^rs[\phi_1']^2\,dx + \int_l^rq\phi_1^2\,dx}{\int_l^rp\phi_1^2\,dx} = \frac{N(\phi_1)}{D(\phi_1)} . \qquad (3)
> $$
>
> *Powers: 3.5, Equation (3)*

^prop-41-1

> [!proof]+ Proof
> $\phi_1$ satisfies (1) with $\lambda = \lambda_1$, which can be written
>
> $$
> -(s\phi_1')' + q\phi_1 = \lambda_1^2p\phi_1, \qquad l < x < r .
> $$
>
> Multiply by $\phi_1$ and integrate from $l$ to $r$:
>
> $$
> \int_l^r-(s\phi_1')'\phi_1\,dx + \int_l^rq\phi_1^2\,dx = \lambda_1^2\int_l^rp\phi_1^2\,dx .
> $$
>
> Integrating the first integral by parts,
>
> $$
> \int_l^r-(s\phi_1')'\phi_1\,dx = -s\phi_1'\phi_1\Big|_l^r + \int_l^rs\phi_1'\phi_1'\,dx .
> $$
>
> But $\phi_1(l) = \phi_1(r) = 0$, so the boundary term vanishes, and
>
> $$
> \int_l^rs[\phi_1']^2\,dx + \int_l^rq\phi_1^2\,dx = \lambda_1^2\int_l^rp\phi_1^2\,dx .
> $$
>
> Since $p > 0$ on $[l, r]$ and $\phi_1 \not\equiv 0$, the integral on the right is positive, and dividing by it gives (3). (The same computation shows $\lambda_n^2 = N(\phi_n)/D(\phi_n)$ for every eigenpair.)

^pf-41-1

*Uses:* [[§41★ Estimation of Eigenvalues#^def-41-1|Def. §41.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] (integration by parts)

For instance (Powers' Exercise 3.5.1), if $q \ge 0$ then $N(\phi_1) \ge 0$, so $\lambda_1^2 \ge 0$ by (3).

> [!theorem] Theorem §41.2: Rayleigh's Upper Bound
> If $y(x)$ is any function with two continuous derivatives on $l \le x \le r$, not identically zero, that satisfies $y(l) = y(r) = 0$, then
>
> $$
> \lambda_1^2 \le \frac{N(y)}{D(y)} . \qquad (4)
> $$
>
> *Powers: 3.5, Equation (4)*

^thm-41-2

*Powers omits the proof ("it can be shown").*

> [!remark] Remark: Why It Works
> Expand the trial function in the eigenfunctions, $y = \sum_nc_n\phi_n$ ([[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]]). Integrating by parts as in the proof of Proposition §41.1 (now with $y(l) = y(r) = 0$), $N(y) = \int_l^ry\big(-(sy')' + qy\big)\,dx$, and $-(sy')' + qy = \sum c_n\lambda_n^2p\phi_n$. By the orthogonality $\int\phi_n\phi_mp = 0$ ($n \ne m$), with $I_n = \int_l^r\phi_n^2p\,dx$,
>
> $$
> N(y) = \sum_nc_n^2\lambda_n^2I_n \ \ge\ \lambda_1^2\sum_nc_n^2I_n = \lambda_1^2D(y) ,
> $$
>
> since every $\lambda_n^2 \ge \lambda_1^2$. Equality holds exactly when only $c_1 \ne 0$, that is, when $y$ is a multiple of $\phi_1$. (The term-by-term steps need justification, which Powers does not give.) So the Rayleigh quotient is a weighted average of the eigenvalues, with weights $c_n^2I_n$, and its minimum over all trial functions is $\lambda_1^2$. A trial function close to $\phi_1$ puts little weight on the higher eigenvalues; since the error in $y$ enters the quotient squared, the estimate is usually quite good.

^rem-41-1

> [!remark]- Connections
> - The finite-dimensional version: for a symmetric matrix $A$, the minimum of $\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$ over $\mathbf{x} \ne \mathbf{0}$ is the least eigenvalue, attained at an eigenvector, [[§60★ Constrained Optimization#^thm-60-1|235 Thm. §60.1]], and the proof there is the argument of Remark: Why It Works with a finite orthonormal eigenbasis. The higher eigenvalues as constrained extrema: [[§60★ Constrained Optimization#^thm-60-3|235 Thm. §60.3]].

> [!remark] Remark: Choosing a Trial Function
> By choosing any convenient function $y$ that satisfies the boundary conditions, one gets from $N(y)/D(y)$ an upper bound on $\lambda_1^2$. Keep in mind that the graph of the eigenfunction $\phi_1$ does not cross the $x$-axis between $l$ and $r$, so the graph of $y$ should not cross it either; simple polynomials vanishing at the ends, such as $(x - l)(r - x)$, are the usual first choice. In some mechanical systems the Rayleigh quotient is the ratio of potential energy ($\int s(y')^2$ measures the stretching) to kinetic energy ($\int py^2$ is mass-weighted), and Rayleigh's method says the lowest mode is the shape that vibrates with the least potential energy for its kinetic energy. There are many other methods for estimating eigenvalues and for systematically improving the estimates ([[§41★ Estimation of Eigenvalues#^ex-41-3|Example §41.3]]).

^rem-41-2

> [!example] Example §51.1: A Polynomial Trial Function for the Uniform String
> Estimate the first eigenvalue of $\phi'' + \lambda^2\phi = 0$, $0 < x < 1$, $\phi(0) = \phi(1) = 0$.
>
> Here $s = p = 1$, $q = 0$. Try $y(x) = x(1 - x)$, which satisfies the boundary conditions and does not cross the axis. Then $y'(x) = 1 - 2x$ and
>
> $$
> N(y) = \int_0^1[y'(x)]^2dx = \int_0^1(1 - 2x)^2dx = \frac13, \qquad D(y) = \int_0^1y^2(x)\,dx = \int_0^1x^2(1 - x)^2dx = \frac{1}{30} .
> $$
>
> Therefore $N(y)/D(y) = 10$. The true eigenfunction is $\phi_1(x) = \sin(\pi x)$ ([[§25 Example꞉ Fixed End Temperatures#^thm-25-2|Theorem §25.2]]), and
>
> $$
> N(\phi_1) = \int_0^1\pi^2\cos^2(\pi x)\,dx = \frac{\pi^2}{2}, \qquad D(\phi_1) = \int_0^1\sin^2(\pi x)\,dx = \frac12 ,
> $$
>
> so $N(\phi_1)/D(\phi_1) = \lambda_1^2 = \pi^2 \approx 9.8696 < 10$, confirming (4). The error of the estimate is about $1.3\%$.
>
> *Powers: 3.5, Example 1*

^ex-41-1

> [!example] Example §51.2: A Nonuniform Problem
> Estimate the first eigenvalue of
>
> $$
> (x\phi')' + \lambda^2\frac1x\phi = 0, \quad 1 < x < 2, \qquad \phi(1) = \phi(2) = 0 .
> $$
>
> Here $s(x) = x$, $q = 0$, $p(x) = 1/x$, so the integrals to be calculated are
>
> $$
> N(y) = \int_1^2x(y')^2\,dx, \qquad D(y) = \int_1^2\frac1xy^2\,dx .
> $$
>
> For three trial functions vanishing at $x = 1$ and $x = 2$:
>
> | $y(x)$ | $N(y)$ | $D(y)$ | $N(y)/D(y)$ |
> |---|---|---|---|
> | $\sqrt x\,(2 - x)(x - 1)$ | $\frac{19}{24}$ | $\frac{1}{30}$ | $23.7500$ |
> | $(2 - x)(x - 1)$ | $\frac12$ | $4\ln 2 - \frac{11}{4}$ | $22.1349$ |
> | $\dfrac{(2 - x)(x - 1)}{x}$ | $3 - 4\ln 2$ | $13\ln 2 - 9$ | $20.8379$ |
>
> For example, for $y = (2 - x)(x - 1) = -x^2 + 3x - 2$: $y' = 3 - 2x$, $N = \int_1^2x(3 - 2x)^2\,dx = \int_1^2(4x^3 - 12x^2 + 9x)\,dx = 15 - 28 + \frac{27}{2} = \frac12$, and $D = \int_1^2\frac{(x^2 - 3x + 2)^2}{x}\,dx = \int_1^2\Big(x^3 - 6x^2 + 13x - 12 + \frac4x\Big)dx = \frac{15}{4} - 14 + \frac{39}{2} - 12 + 4\ln 2 = 4\ln 2 - \frac{11}{4}$.
>
> The first eigenvalue and eigenfunction are known ([[§40 One-Dimensional Wave Equation꞉ Generalities#^ex-40-4|Example §40.4]]):
>
> $$
> \lambda_1^2 = \Big(\frac{\pi}{\ln 2}\Big)^2 \approx 20.5423, \qquad \phi_1(x) = \sin\Big(\frac{\pi\ln x}{\ln 2}\Big) .
> $$
>
> All three quotients lie above it, as (4) requires; the error for the best trial function, $(2 - x)(x - 1)/x$, is about $1.44\%$.
>
> *Powers: 3.5, Example 2*

^ex-41-2

> [!example] Example §51.3: Improving the Estimate with a Parameter
> In Example §41.1, use the one-parameter family of trial functions $y_b(x) = x(1 - x)\big(1 + b\,x(1 - x)\big)$ and choose $b$ to make the Rayleigh quotient as small as possible.
>
> Each $y_b$ vanishes at $0$ and $1$. Expanding and integrating,
>
> $$
> N(y_b) = \int_0^1(y_b')^2\,dx = \frac13 + \frac{2b}{15} + \frac{2b^2}{105}, \qquad D(y_b) = \int_0^1y_b^2\,dx = \frac{1}{30} + \frac{b}{70} + \frac{b^2}{630},
> $$
>
> so
>
> $$
> R(b) = \frac{N(y_b)}{D(y_b)} = \frac{6(2b^2 + 14b + 35)}{b^2 + 9b + 21} .
> $$
>
> At $b = 0$ this is the estimate $10$ of Example §41.1. By Theorem §41.2 every $R(b) \ge \pi^2$, so the best estimate in the family is the minimum. By the quotient rule,
>
> $$
> R'(b) = \frac{6(4b^2 + 14b - 21)}{(b^2 + 9b + 21)^2} ,
> $$
>
> which vanishes at $b = \frac{-7 \pm \sqrt{133}}{4}$. The root $b = \frac{-7 + \sqrt{133}}{4} \approx 1.1331$ gives the minimum, and
>
> $$
> R_{\min} = 56 - 4\sqrt{133} \approx 9.86975, \qquad \pi^2 \approx 9.86960 .
> $$
>
> The error has dropped from $1.3\%$ to $0.0015\%$. Minimizing the Rayleigh quotient over a family of trial functions is the idea of the Rayleigh–Ritz method, one of the "methods for systematically improving the estimates".
>
> *Powers: 3.5, Example 1 (the problem); the trial family is added*

^ex-41-3
