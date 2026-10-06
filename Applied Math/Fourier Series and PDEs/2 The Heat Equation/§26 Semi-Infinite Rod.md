---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 26
powers: "2.10"
aliases: ["Powers 2.10"]
tags: [fourier-series-and-pdes, math341]
---
← [[§25 Generalities on the Heat Conduction Problem]] · ↑ [[· 2 The Heat Equation]] · [[§27 Infinite Rod]] →

*Powers, Section 2.10 · MAT 341 lectures 10.17, 10.22, 10.24 · HW 9 · Practice Midterm 2.*

A very long rod can be treated as semi-infinite, extending from $0$ to $\infty$; this is also how one suppresses the influence of a far boundary condition that is complicated or unknown. The right-hand boundary condition is then replaced by the requirement that the temperature stay bounded. Separation of variables still works, but it leads to a *singular* eigenvalue problem in which every $\lambda > 0$ is allowed, so the sum over eigenvalues becomes an integral over $\lambda$, and the initial condition is met by the Fourier sine integral ([[§14 Fourier Integral#^def-14-new2|Definition §14.2]]). Physically the model describes a long bar whose end is held at a fixed temperature, or diffusion from a surface into a deep medium; it is a valid approximation for $x$ much smaller than the true length.

## The Singular Eigenvalue Problem

If the rod has uniform properties, no generation, and its end $x = 0$ is held at temperature $0$, the mathematical model is

$$
\begin{aligned}
\frac{\partial^2u}{\partial x^2} &= \frac1k\frac{\partial u}{\partial t}, && 0 < x < \infty, \quad 0 < t, && (1) \\
u(0, t) &= 0, && 0 < t, && (2) \\
u(x, t) &\ \text{bounded as } x \to \infty, && && (3) \\
u(x, 0) &= f(x), && 0 < x. && (4)
\end{aligned}
$$

The heat equation (1) and the boundary condition (2) are homogeneous, and so in effect is the boundedness condition (3): a finite sum of bounded functions is bounded. So (1)–(3) can be attacked by separation of variables. With $u = \phi(x)T(t)$,

$$
\frac{\phi''(x)}{\phi(x)} = \frac{T'(t)}{kT(t)} = \text{const} . \qquad (5)
$$

The boundary condition requires $\phi(0) = 0$, and boundedness requires $\phi(x)$ to remain finite as $x \to \infty$.

> [!definition] Definition §26.1: Singular Eigenvalue Problem
> The problem
>
> $$
> \phi'' + \lambda^2\phi = 0, \quad 0 < x, \qquad \phi(0) = 0, \qquad \phi(x) \ \text{bounded as } x \to \infty \qquad (6)\text{–}(7)
> $$
>
> is a **singular eigenvalue problem**, singular because of the semi-infinite interval. More generally, an eigenvalue problem in which the interval is unbounded, or the coefficient $s$ vanishes at an end ([[§23 Sturm–Liouville Problems#^ex-23-2|Example §23.2]]), and a boundedness condition replaces a boundary condition, is called singular.
>
> *Powers: 2.10 (text)*

^def-26-1

> [!theorem] Proposition §26.1: Solutions of the Singular Eigenvalue Problem
> The equation $\phi'' = \mu\phi$ on $0 < x < \infty$ has a solution $\phi \not\equiv 0$ with $\phi(0) = 0$ and $\phi$ bounded as $x \to \infty$ only if $\mu < 0$. Writing $\mu = -\lambda^2$, *every* $\lambda > 0$ gives such a solution, and up to a constant multiple it is
>
> $$
> \phi(x; \lambda) = \sin(\lambda x), \qquad \lambda > 0 . \qquad (8)
> $$
>
> Negative values of $\lambda$ produce no new solutions. The accompanying factor is $T(t) = \exp(-\lambda^2kt)$.
>
> *Powers: 2.10, Eqs. (6)–(8)*

^prop-26-1

> [!proof]+ Proof
> Consider the sign of the separation constant $\mu$ (Powers leaves the positive case to his Exercise 2.10.8 and does not discuss the zero case; the 10.24 lecture works all three).
> - $\mu = \nu^2 > 0$: $\phi = Ae^{\nu x} + Be^{-\nu x}$. Boundedness as $x \to \infty$ forces $A = 0$, and then $\phi(0) = B = 0$. So any nonzero bounded solution is not $0$ at $x = 0$, and any solution that is $0$ at $x = 0$ is not bounded.
> - $\mu = 0$: $\phi = Ax + B$. Boundedness forces $A = 0$, and $\phi(0) = B = 0$.
> - $\mu = -\lambda^2 < 0$: the general solution $\phi = c_1\cos(\lambda x) + c_2\sin(\lambda x)$ is bounded for any choice of the constants and any $\lambda$, so the boundedness condition contributes nothing further. The boundary condition gives $\phi(0) = c_1 = 0$, leaving $\phi = c_2\sin(\lambda x)$, a nonzero solution for every $\lambda > 0$; take $c_2 = 1$. Since $\sin(-\lambda x) = -\sin(\lambda x)$, negative $\lambda$ give only multiples of the same functions.
>
> Finally $T'/(kT) = -\lambda^2$ gives $T = \exp(-\lambda^2kt)$ up to a constant.

^pf-26-1

In this singular problem there are no "special" values of $\lambda$: the eigenvalues fill the whole half-line $\lambda^2 > 0$, in contrast to the discrete sequence $\lambda_1^2 < \lambda_2^2 < \cdots$ of a regular problem ([[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]]). For any $\lambda$ the function $u(x, t; \lambda) = \sin(\lambda x)\exp(-\lambda^2kt)$ satisfies (1)–(3), and any linear combination of these does too. Since $\lambda$ may take on any positive value, the combination must be an integral, the continuous analogue of a sum.

## Solution by a Fourier Sine Integral

> [!theorem] Theorem §26.2: Solution of the Semi-Infinite Rod Problem
> Let $f$ be sectionally smooth on $0 < x < \infty$ with $\int_0^\infty |f(x)|\,dx < \infty$. Then
>
> $$
> u(x, t) = \int_0^\infty B(\lambda)\sin(\lambda x)\exp(-\lambda^2kt)\,d\lambda , \qquad (9)
> $$
>
> with
>
> $$
> B(\lambda) = \frac2\pi\int_0^\infty f(x)\sin(\lambda x)\,dx , \qquad (10)
> $$
>
> satisfies (1)–(3) for $t > 0$, and at $t = 0$ the integral (9) equals $\frac12\big(f(x+) + f(x-)\big)$ for $x > 0$, which is $f(x)$ wherever $f$ is continuous.
>
> *Powers: 2.10, Eqs. (9) and (10)*

^thm-26-2

> [!proof]+ Proof
> **The coefficient.** Powers chooses $B$ so that the initial condition holds: at $t = 0$, (9) becomes $\int_0^\infty B(\lambda)\sin(\lambda x)\,d\lambda = f(x)$, which is the Fourier sine integral representation of $f$ ([[§14 Fourier Integral#^def-14-new2|Definition §14.2]]), with exactly the coefficient (10). Under the hypotheses on $f$, [[§14 Fourier Integral#^cor-14-2|Corollary §14.2]] gives the value $\frac12(f(x+) + f(x-))$. (Negative values of $\lambda$ need not be included; they give no new solutions.)
>
> **The differential equation.** (Powers asserts that (9) is then the solution; here is why the integral may be differentiated.) The coefficient is bounded: $|B(\lambda)| \le \frac2\pi\int_0^\infty |f|\,dx =: M$. Fix $t_1 > 0$. For $t \ge t_1$ the integrand of (9) and its partial derivatives in $x$ and $t$ are bounded by
>
> $$
> |B\sin(\lambda x)e^{-\lambda^2kt}| \le Me^{-\lambda^2kt_1}, \qquad \Big|\frac{\partial}{\partial x}(\cdots)\Big| \le M\lambda e^{-\lambda^2kt_1}, \qquad \Big|\frac{\partial^2}{\partial x^2}(\cdots)\Big|,\ \frac1k\Big|\frac{\partial}{\partial t}(\cdots)\Big| \le M\lambda^2e^{-\lambda^2kt_1} ,
> $$
>
> and these bounds are integrable over $0 < \lambda < \infty$, independently of $x$ and $t$. So differentiation under the integral sign is legitimate (by the [[Mean Value Theorem|mean value theorem]], the difference quotients are dominated by the same bounds, and dominated convergence applies), and
>
> $$
> \frac{\partial^2u}{\partial x^2} - \frac1k\frac{\partial u}{\partial t} = \int_0^\infty B(\lambda)\big(-\lambda^2 + \lambda^2\big)\sin(\lambda x)e^{-\lambda^2kt}\,d\lambda = 0 .
> $$
>
> **Boundary and boundedness.** $u(0, t) = 0$ because $\sin 0 = 0$. For each $t > 0$,
>
> $$
> |u(x, t)| \le M\int_0^\infty e^{-\lambda^2kt}\,d\lambda = M\sqrt{\frac{\pi}{4kt}} ,
> $$
>
> independently of $x$, so (3) holds. (That $u(x, t) \to f(x)$ as $t \to 0+$, at points of continuity, is a stronger statement than the value of (9) at $t = 0$; it is seen most easily from the kernel form of [[§27 Infinite Rod#^prop-27-4|Proposition §27.4]], and Powers does not discuss it.)

^pf-26-2

*Uses:* [[§26 Semi-Infinite Rod#^prop-26-1|§26.1]], [[§14 Fourier Integral#^def-14-new2|Def. §14.2]], [[§14 Fourier Integral#^cor-14-2|§14.2]], [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]], [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem)

> [!remark]- Connections
> - Differentiation under the integral sign by dominated convergence: [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]. The integrals (9) and (10) are improper Riemann integrals in the sense of [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]]; for $t > 0$ the exponential factor makes (9) converge absolutely and very rapidly.

> [!remark] Remark: Interpreting the Solution
> If $B(\lambda)$ exists, (9) is the solution. When $t > 0$ the factor $\exp(-\lambda^2kt)$ makes the improper integral converge very rapidly, whereas at $t = 0$ it may converge only conditionally (in [[§26 Semi-Infinite Rod#^ex-26-1|Example §26.1]], $B(\lambda)$ decays only like $1/\lambda$). Some care is needed in interpreting the solution: if the rod is really finite, say of length $L$, (9) is meaningless for $x > L$, and a boundary condition at $x = L$ would influence temperatures nearby, so (9) is a valid approximation only for $x \ll L$.

^rem-26-1

> [!remark] Remark: Method — Heat Equation on a Semi-Infinite Rod
> 1. **Nonzero boundary temperature.** If $u(0, t) = T_0$, the bounded steady state is $v(x) = T_0$ ($v = Ax + B$ is bounded only if $A = 0$). Set $w = u - T_0$; then $w(0, t) = 0$ and $w(x, 0) = g(x) = f(x) - T_0$. The sine integral of $g$ needs $\int_0^\infty |g| < \infty$, so this works when $f(x) \to T_0$ as $x \to \infty$ (Powers' Exercise 2.10.7).
> 2. **Separate variables** and discuss the separation constant: positive and zero give no nonzero bounded solution satisfying the condition at $x = 0$; negative, $-\lambda^2$, gives one for every $\lambda > 0$.
> 3. **Superpose with an integral**, $u = \int_0^\infty C(\lambda)\phi(x; \lambda)e^{-\lambda^2kt}\,d\lambda$.
> 4. **Coefficient.** If the basis is $\sin(\lambda x)$ (end held at $0$), $C(\lambda)$ is the Fourier sine integral coefficient $\frac2\pi\int_0^\infty f\sin(\lambda x)\,dx$, i.e. that of the odd extension of $f$. If the end is insulated, $u_x(0, t) = 0$, the basis is $\cos(\lambda x)$ (including the constant, $\lambda = 0$) and $C(\lambda) = \frac2\pi\int_0^\infty f\cos(\lambda x)\,dx$, the coefficient of the even extension ([[§26 Semi-Infinite Rod#^ex-26-3|Example §26.3]]).
> 5. Compute the coefficient explicitly when possible; the remaining integral over $\lambda$ usually cannot be evaluated in closed form, but see [[§28★ The Error Function#^ex-28-1|Example §28.1]].
>
> *Source: 341 lectures 10.17, 10.22, 10.24*

^rem-26-2

## Examples

> [!example] Example §26.1: A Heated Section at the End of the Rod
> Solve (1)–(4) with
>
> $$
> f(x) = \begin{cases} T_0, & 0 < x < b, \\ 0, & b < x . \end{cases}
> $$
>
> A section of length $b$ at the left end of the rod starts out at temperature $T_0 > 0$, different from the temperature of the long right part, which is the same as that of the left boundary. By (10),
>
> $$
> B(\lambda) = \frac2\pi\int_0^\infty f(x)\sin(\lambda x)\,dx = \frac2\pi\int_0^b T_0\sin(\lambda x)\,dx = \frac{2T_0}{\pi\lambda}\big(1 - \cos(\lambda b)\big) .
> $$
>
> Therefore the complete solution is
>
> $$
> u(x, t) = \frac2\pi T_0\int_0^\infty \frac{1 - \cos(\lambda b)}{\lambda}\sin(\lambda x)\exp(-\lambda^2kt)\,d\lambda .
> $$
>
> The integral cannot be evaluated in elementary terms; in terms of the error function it is $T_0\big[\operatorname{erf}\frac{x}{\sqrt{4kt}} - \frac12\operatorname{erf}\frac{x - b}{\sqrt{4kt}} - \frac12\operatorname{erf}\frac{x + b}{\sqrt{4kt}}\big]$ ([[§28★ The Error Function#^ex-28-1|Example §28.1]]), which is how the figure was computed. The heat escapes through the cold end $x = 0$ and spreads to the right; the dimensionless time $kt/b^2$ controls the picture.
>
> *Powers: 2.10, Example*

^ex-26-1

![[m341-26-1.svg]]
*The solution of Example §26.1 as a function of $x/b$ on $0 < x < 3b$, at the dimensionless times $kt/b^2 = 0.001$, $0.01$, $0.1$ and $1$. When $kt/b^2 = 0.01$, the temperature near $x = b/2$ has not changed noticeably from its initial value; the corners are rounded first. Later the heated block both leaks out through $x = 0$, which is held at $0$, and spreads to the right.*

> [!example] Example §26.2: A Half Sine Wave of Initial Temperature
> Solve
>
> $$
> \frac{\partial u}{\partial t} = 2\frac{\partial^2u}{\partial x^2}, \quad x > 0, \qquad u(0, t) = 0, \qquad u \ \text{bounded as } x \to \infty, \qquad u(x, 0) = f(x) = \begin{cases} \sin x, & 0 < x < \pi, \\ 0, & x > \pi . \end{cases}
> $$
>
> **(a)** With $w = \phi(x)T(t)$: $T' = 2\mu T$, $\phi'' = \mu\phi$, $\phi(0) = 0$, $\phi$ bounded as $x \to \infty$.
>
> **(b)** By Proposition §26.1, $\mu > 0$ and $\mu = 0$ give no nonzero solution, and for $\mu = -\lambda^2$, $\phi_\lambda = \sin(\lambda x)$ for all $\lambda > 0$, with $T_\lambda = e^{-2\lambda^2t}$. The basic solutions are $u_\lambda = e^{-2\lambda^2t}\sin(\lambda x)$, $\lambda > 0$.
>
> **(c)** $u = \int_0^\infty B(\lambda)e^{-2\lambda^2t}\sin(\lambda x)\,d\lambda$ with
>
> $$
> B(\lambda) = \frac2\pi\int_0^\pi \sin x\sin(\lambda x)\,dx = \frac1\pi\int_0^\pi \big(\cos((\lambda - 1)x) - \cos((\lambda + 1)x)\big)dx = \frac1\pi\Big(\frac{\sin((\lambda - 1)\pi)}{\lambda - 1} - \frac{\sin((\lambda + 1)\pi)}{\lambda + 1}\Big) .
> $$
>
> Since $\sin((\lambda \mp 1)\pi) = -\sin(\lambda\pi)$, this simplifies to
>
> $$
> B(\lambda) = \frac{2\sin(\lambda\pi)}{\pi(1 - \lambda^2)}, \qquad u(x, t) = \frac2\pi\int_0^\infty \frac{\sin(\lambda\pi)}{1 - \lambda^2}\,e^{-2\lambda^2t}\sin(\lambda x)\,d\lambda .
> $$
>
> The point $\lambda = 1$ is not a singularity: $\sin(\lambda\pi)/(1 - \lambda^2) \to \pi/2$ as $\lambda \to 1$, so $B(1) = 1$ (directly, $\frac2\pi\int_0^\pi \sin^2x\,dx = 1$).
>
> *Source: 341 Practice Midterm 2, Q7*

^ex-26-2

> [!example] Example §26.3: An Insulated End
> Solve
>
> $$
> \frac{\partial u}{\partial t} = k\frac{\partial^2u}{\partial x^2}, \quad x > 0, \qquad \frac{\partial u}{\partial x}(0, t) = 0, \qquad u \ \text{bounded as } x \to \infty, \qquad u(x, 0) = e^{-x} .
> $$
>
> **(a)** With $w = \phi T$ and $T' = k\mu T$: $\phi'' = \mu\phi$, $\phi'(0) = 0$, $\phi$ bounded as $x \to \infty$.
>
> **(b)** Cases:
> - $\mu = \nu^2 > 0$: $\phi = Ae^{-\nu x} + Be^{\nu x}$; boundedness gives $B = 0$, and $\phi'(0) = -\nu A = 0$ gives $A = 0$. No nonzero solution.
> - $\mu = 0$: $\phi = Ax + B$; boundedness gives $A = 0$, and then $\phi'(0) = 0$ holds automatically. So $\phi = B$, a nonzero constant, is a solution.
> - $\mu = -\lambda^2 < 0$: $\phi = A\sin(\lambda x) + B\cos(\lambda x)$, $\phi'(0) = \lambda A = 0$, so $\phi = B\cos(\lambda x)$ for every $\lambda > 0$.
>
> The constant is the case $\lambda = 0$ of $\cos(\lambda x)$.
>
> **(c)** The basic solutions are $w_\lambda = \cos(\lambda x)e^{-k\lambda^2t}$, $\lambda \ge 0$.
>
> **(d)** $u = \int_0^\infty A(\lambda)\cos(\lambda x)e^{-k\lambda^2t}\,d\lambda$, and at $t = 0$, $e^{-x} = \int_0^\infty A(\lambda)\cos(\lambda x)\,d\lambda$ for $x > 0$: the Fourier cosine integral ([[§14 Fourier Integral#^def-14-2|Definition §14.2]], [[§14 Fourier Integral#^cor-14-2|Corollary §14.2]]) of $e^{-x}$, i.e. the Fourier integral of the even extension $e^{-|x|}$. Integrating by parts twice, with $I = \int_0^\infty e^{-x}\cos(\lambda x)\,dx$,
>
> $$
> I = \Big[-e^{-x}\cos(\lambda x)\Big]_0^\infty - \lambda\int_0^\infty e^{-x}\sin(\lambda x)\,dx = 1 - \lambda\Big(\Big[-e^{-x}\sin(\lambda x)\Big]_0^\infty + \lambda I\Big) = 1 - \lambda^2I ,
> $$
>
> so $I = 1/(1 + \lambda^2)$ and
>
> $$
> A(\lambda) = \frac2\pi\int_0^\infty e^{-x}\cos(\lambda x)\,dx = \frac{2}{\pi(1 + \lambda^2)}, \qquad u(x, t) = \frac2\pi\int_0^\infty \frac{\cos(\lambda x)}{1 + \lambda^2}\,e^{-k\lambda^2t}\,d\lambda .
> $$
>
> The constant solution ($\lambda = 0$) is included as the endpoint of the integral; a single value of $\lambda$ contributes nothing to it by itself.
>
> *The key's formula for $A(\lambda)$ has $d\lambda$ in place of $dx$.*
>
> *Source: 341 HW 9, Problem 2*

^ex-26-3
