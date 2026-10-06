---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 15
powers: "1.10"
aliases: ["Powers 1.10"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§14 Fourier Integral]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§16★ Applications of Fourier Series and Integrals]] →

*Powers, Section 1.10 · MAT 341 lecture 10.3 · Midterm 1 · Midterm 2.*
★ *Beyond MAT 341: the course did not cover this section, apart from presenting the complex form as a bonus topic in lecture 10.3, which the bonus questions of both midterms used; it is included in full from Powers.*

Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ packs a cosine and a sine of the same frequency into one exponential. Fourier series and integrals then take a single compact form, $f(x) = \sum c_ne^{inx}$ and $f(x) = \int C(\lambda)e^{i\lambda x}\,d\lambda$, with one coefficient formula valid for all frequencies, positive and negative. The complex coefficient function $C(\lambda)$ is the Fourier transform of $f$. This is the form used in physics and electrical engineering: momentum-space wave functions in quantum mechanics, spectra of signals and AC circuits, and the solution of differential equations on the whole line, where differentiation becomes multiplication by $i\lambda$. The lecture of 10.3 presented the complex form as a bonus topic, and the bonus questions of both midterms used the transform.

## Fourier Series

Suppose that a function $f(x)$ equals its Fourier series (period $2\pi$ for simplicity only),

$$
f(x) = a_0 + \sum_{n=1}^{\infty} a_n\cos(nx) + b_n\sin(nx) .
$$

Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, where $i^2 = -1$, gives the exponential forms of the sine and cosine,

$$
\cos\theta = \frac12\big(e^{i\theta} + e^{-i\theta}\big), \qquad \sin\theta = \frac{1}{2i}\big(e^{i\theta} - e^{-i\theta}\big) .
$$

Substituting them into the Fourier series,

$$
f(x) = a_0 + \frac12\sum_{n=1}^{\infty} a_n\big(e^{inx} + e^{-inx}\big) - ib_n\big(e^{inx} - e^{-inx}\big) = a_0 + \frac12\sum_{n=1}^{\infty}(a_n - ib_n)e^{inx} + (a_n + ib_n)e^{-inx} .
$$

> [!definition] Definition §15.1: Complex Fourier Coefficients
> The **complex Fourier coefficients** of $f$ are
>
> $$
> c_0 = a_0, \qquad c_n = \frac12(a_n - ib_n), \qquad c_{-n} = \frac12(a_n + ib_n), \qquad n = 1, 2, 3, \dots ,
> $$
>
> where $a_0, a_n, b_n$ are the Fourier coefficients of $f$. For real $f$, $c_{-n} = \overline{c_n}$.
>
> *Powers: 1.10 (text)*

^def-15-1

> [!theorem] Theorem §15.1: Complex Form of the Fourier Series
> Let $f$ be periodic with period $2\pi$ and sectionally continuous. In terms of the complex coefficients,
>
> $$
> f(x) \sim c_0 + \sum_{n=1}^{\infty}\big(c_ne^{inx} + c_{-n}e^{-inx}\big) = \sum_{n=-\infty}^{\infty} c_ne^{inx} , \qquad (1)
> $$
>
> where the doubly infinite series means the limit of the symmetric partial sums $\sum_{n=-N}^{N}$, and these are exactly the real partial sums $S_N(x)$. The coefficients are given, for all integers $n$, positive, negative or zero, by the universal formula
>
> $$
> c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)e^{-inx}\,dx . \qquad (2)
> $$
>
> For period $2a$ the same holds with $e^{in\pi x/a}$ in place of $e^{inx}$ and $c_n = \frac{1}{2a}\int_{-a}^{a} f(x)e^{-in\pi x/a}\,dx$. In particular, when $f$ is sectionally smooth, the series converges to $\frac12\big(f(x+) + f(x-)\big)$ at every $x$.
>
> *Powers: 1.10, Equations (1) and (2) · Source: 341 lecture 10.3 (period 2a)*

^thm-15-1

> [!proof]+ Proof
> **The series.** The computation before Definition §15.1, done for a partial sum, shows
>
> $$
> a_0 + \sum_{n=1}^{N}\big(a_n\cos nx + b_n\sin nx\big) = c_0 + \sum_{n=1}^{N}\big(c_ne^{inx} + c_{-n}e^{-inx}\big) = \sum_{n=-N}^{N} c_ne^{inx} ,
> $$
>
> because $b_n\cdot\frac{1}{2i} = -\frac{i}{2}b_n$. So the symmetric partial sums of (1) are the partial sums $S_N(x)$ of the real series, and they converge exactly when $S_N(x)$ does, to the same limit; for sectionally smooth $f$ this is [[§12★ Proof of Convergence#^thm-12-4|Theorem §12.4]].
>
> **The coefficients** ("easy to derive", says Powers). For $n \ge 1$, by the real coefficient formulas,
>
> $$
> c_n = \frac12(a_n - ib_n) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\big(\cos nx - i\sin nx\big)\,dx = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)e^{-inx}\,dx .
> $$
>
> For $n = 0$, $c_0 = a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\,dx$, which is (2) with $e^{0} = 1$. For $n = -m$ with $m \ge 1$,
>
> $$
> c_{-m} = \frac12(a_m + ib_m) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\big(\cos mx + i\sin mx\big)\,dx = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)e^{imx}\,dx ,
> $$
>
> which is (2) for $n = -m$. (Equivalently, Powers' Exercise 1.10.6: $\int_{-\pi}^{\pi} e^{inx}e^{-imx}\,dx = 0$ for $n \ne m$ and $2\pi$ for $n = m$, since $\int_{-\pi}^{\pi} e^{ikx}\,dx = \big[e^{ikx}/(ik)\big]_{-\pi}^{\pi} = 0$ for $k \ne 0$; multiplying (1) by $e^{-imx}$ and integrating term by term picks out $2\pi c_m$.) For period $2a$, apply the above to $g(s) = f(as/\pi)$ and substitute $x = as/\pi$, as in [[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]].

^pf-15-1

*Uses:* [[§15★ Complex Methods#^def-15-1|Def. §15.1]], [[§12★ Proof of Convergence#^thm-12-4|§12.4]], [[§12★ Proof of Convergence#^cor-12-5|§12.5]], [[§6 Periodic Functions and Fourier Series#^def-6-2|Def. §6.2]], [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]] (the complex exponential and Euler's formula)

> [!remark]- Connections
> - The normalized exponentials $e^{inx}/\sqrt{2\pi}$, $n \in \mathbb{Z}$, form an orthonormal basis of the complex space $L^2[0, 2\pi]$, [[§24 Orthonormal Sets and Bases#^thm-24-11|556 Thm. §24.11]]: (2) says $c_n\sqrt{2\pi}$ is the inner product of $f$ with the $n$th basis vector, and Parseval's equality reads $\frac{1}{2\pi}\int|f|^2 = \sum|c_n|^2$ ([[§24 Orthonormal Sets and Bases#^rem-24-9|556 Rem. §24.9]]). In quantum mechanics they are the momentum eigenstates of a particle on a ring.
> - Complex-variables version: [[§42 Definite Integrals of Functions w(t)#^ex-42-4|342 Ex. §42.4]] (orthogonality of the $e^{in\theta}$) and [[§66 Laurent Series#^ex-66-3|342 Ex. §66.3]] (for boundary values of a function analytic in an annulus, this series is the Laurent series [[§66 Laurent Series#^def-66-1|342 Def. §66.1]] on the unit circle).

The complex form is used especially in physics and electrical engineering. Sometimes the function corresponding to a Fourier series can be recognized by use of the complex form.

> [!example] Example §15.1: Summing a Cosine Series with the Logarithm
> The series $\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\cos(nx)$ may be considered the real part of
>
> $$
> \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}e^{inx} = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\big(e^{ix}\big)^n , \qquad (3)
> $$
>
> because the real part of $e^{i\theta}$ is $\cos\theta$. The series on the right is recognized as a Taylor series, $\sum_{n\ge1}\frac{(-1)^{n+1}}{n}z^n = \ln(1 + z)$ with $z = e^{ix}$:
>
> $$
> \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\big(e^{ix}\big)^n = \ln\big(1 + e^{ix}\big) .
> $$
>
> (Powers asserts this; here is why it holds on $|z| = 1$. For $|z| < 1$ the series is the Taylor series of the principal logarithm $\operatorname{Log}(1 + z)$. On $|z| = 1$, $z \ne -1$, it still converges, by Dirichlet's test, and Abel's theorem on power series lets $|z| \to 1$; so the identity holds for $z = e^{ix}$, $-\pi < x < \pi$.) Some manipulations yield
>
> $$
> 1 + e^{ix} = e^{ix/2}\big(e^{ix/2} + e^{-ix/2}\big) = 2e^{ix/2}\cos\big(\tfrac x2\big), \qquad \ln\big(1 + e^{ix}\big) = \frac{ix}{2} + \ln\Big(2\cos\big(\tfrac x2\big)\Big) ,
> $$
>
> since $2\cos(x/2) > 0$ for $-\pi < x < \pi$. The real part of $\ln(1 + e^{ix})$ is $\ln\big(2\cos(x/2)\big)$, and we derive the relation
>
> $$
> \ln\Big(2\cos\big(\tfrac x2\big)\Big) \sim \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\cos(nx), \qquad -\pi < x < \pi . \qquad (4)
> $$
>
> The series actually converges except at $x = \pm\pi, \pm3\pi, \dots$, where the function tends to $-\infty$. The imaginary parts give a check: $\sum_{n\ge1}\frac{(-1)^{n+1}}{n}\sin(nx) = \frac x2$ for $-\pi < x < \pi$, which is the Fourier series of $\frac x2$ (its coefficients are $\frac1\pi\int_{-\pi}^{\pi}\frac x2\sin nx\,dx = \frac{(-1)^{n+1}}{n}$).
>
> *Powers: 1.10, Example (Fourier series)*

^ex-15-1

## Fourier Integral

The Fourier integral of a function $f(x)$ defined on the entire line $-\infty < x < \infty$ can also be cast in complex form.

> [!definition] Definition §15.2: Complex Fourier Integral; Fourier Transform
> Let $\int_{-\infty}^{\infty}|f(x)|\,dx < \infty$. The **complex Fourier integral coefficient function** of $f$ is
>
> $$
> C(\lambda) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i\lambda x}\,dx , \qquad (6)
> $$
>
> and the **complex Fourier integral** of $f$ is
>
> $$
> \int_{-\infty}^{\infty} C(\lambda)e^{i\lambda x}\,d\lambda . \qquad (5)
> $$
>
> $C(\lambda)$ is often called the **Fourier transform** of $f$, and (5), read as a formula producing $f$ from $C$, the **inverse Fourier transform**.
>
> *Powers: 1.10, Equations (5) and (6) · Source: 341 lecture 10.3*

^def-15-2

> [!remark]- Connections
> - Normalizations differ between books. Powers puts $\frac{1}{2\pi}$ in the transform; Lax's (and 556's) $\mathcal{F}(f)(x) = \int e^{-ix\cdot\xi}f(\xi)\,d\xi$ is $2\pi C$, and many physics texts split the factor as $\frac{1}{\sqrt{2\pi}}$ in both directions. In any normalization, $|C(\lambda)| \le \frac{1}{2\pi}\int|f|$: the transform is a bounded linear map from $L^1$ to $L^\infty$, [[§26 Boundedness and Continuity#^ex-26-2|556 Ex. §26.2]].
> - For a rational function $f$ the transform can be computed by residues: [[§87 Improper Integrals from Fourier Analysis#^prop-87-1|342 Prop. §87.1]].

The lecture reached (5) and (6) as Powers reached (7) of §14 ([[§14 Fourier Integral#^rem-14-1|Remark: Why It Works]]): on $-a < x < a$ the complex series of Theorem §15.1 reads $f(x) = \sum_n \frac\pi a C_a\big(\frac{n\pi}a\big)e^{in\pi x/a}$ with $C_a(\lambda) = \frac{1}{2\pi}\int_{-a}^{a} f(x)e^{-i\lambda x}\,dx$, a Riemann sum with spacing $\Delta\lambda = \pi/a$, which suggests (5) as $a \to \infty$. The real theorem makes this precise.

> [!theorem] Theorem §15.2: Complex Form of the Fourier Integral
> Let $f$ satisfy the hypotheses of [[§14 Fourier Integral#^thm-14-1|Theorem §14.1]], with Fourier integral coefficient functions $A(\lambda)$, $B(\lambda)$.
> 1. The complex coefficient function is
>
> $$
> C(\lambda) = \frac12\big(A(\lambda) - iB(\lambda)\big) . \qquad (7)
> $$
>
> 2. At every point $x$,
>
> $$
> \lim_{L\to\infty}\int_{-L}^{L} C(\lambda)e^{i\lambda x}\,d\lambda = \frac12\big(f(x+) + f(x-)\big) .
> $$
>
> 3. If $f$ is even, $C(\lambda) = \frac12A(\lambda)$ is real; if $f$ is odd, $C(\lambda) = -\frac i2B(\lambda)$ is imaginary.
>
> *Powers: 1.10, Equation (7) and text*

^thm-15-2

> [!proof]+ Proof
> **1** ("simple to show", says Powers). By Euler's formula $e^{-i\lambda x} = \cos\lambda x - i\sin\lambda x$, so
>
> $$
> C(\lambda) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)\cos(\lambda x)\,dx - \frac{i}{2\pi}\int_{-\infty}^{\infty} f(x)\sin(\lambda x)\,dx = \frac12A(\lambda) - \frac i2B(\lambda) .
> $$
>
> **2.** Powers writes the integral (5) over $-\infty < \lambda < \infty$; it is to be read as the limit of $\int_{-L}^{L}$ (here is why: the imaginary part of the integrand below is odd in $\lambda$, so its integral over $[-L, L]$ vanishes, while $\int_0^{L}$ of it need not converge). By part 1 and Euler's formula,
>
> $$
> C(\lambda)e^{i\lambda x} = \frac12\big(A\cos\lambda x + B\sin\lambda x\big) + \frac i2\big(A\sin\lambda x - B\cos\lambda x\big) .
> $$
>
> $A$ is even and $B$ is odd in $\lambda$, so the real part is even in $\lambda$ and the imaginary part is odd. Hence
>
> $$
> \int_{-L}^{L} C(\lambda)e^{i\lambda x}\,d\lambda = \int_0^{L}\big(A(\lambda)\cos\lambda x + B(\lambda)\sin\lambda x\big)\,d\lambda + 0 ,
> $$
>
> and as $L \to \infty$ this tends to $\frac12\big(f(x+) + f(x-)\big)$ by [[§14 Fourier Integral#^thm-14-1|Theorem §14.1]].
>
> **3.** If $f$ is even then $B = 0$, and if $f$ is odd then $A = 0$ (Remark: Reading the Theorem in [[§14 Fourier Integral#^rem-14-2|§14]]); part 1 gives the rest.

^pf-15-2

*Uses:* [[§15★ Complex Methods#^def-15-2|Def. §15.2]], [[§14 Fourier Integral#^thm-14-1|§14.1]], [[§14 Fourier Integral#^def-14-1|Def. §14.1]], [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]] (Euler's formula)

> [!remark]- Connections
> - See also: [[§95★ Inverse Laplace Transforms#^thm-95-4|342 Thm. §95.4]] (the Bromwich inversion formula for the Laplace transform, derived from this theorem).

> [!example] Example §15.2: The Rectangular Pulse in Complex Form
> Find the complex Fourier integral representation of
>
> $$
> f(x) = \begin{cases} 1, & -a < x < a, \\ 0, & |x| > a . \end{cases}
> $$
>
> The coefficient function (or transform) of $f$ is
>
> $$
> C(\lambda) = \frac{1}{2\pi}\int_{-a}^{a} e^{-i\lambda x}\,dx = \frac{1}{2\pi}\Big[\frac{e^{-i\lambda x}}{-i\lambda}\Big]_{-a}^{a} = \frac{1}{2\pi}\cdot\frac{e^{i\lambda a} - e^{-i\lambda a}}{i\lambda} = \frac{\sin(\lambda a)}{\pi\lambda} .
> $$
>
> The representation of $f$ is
>
> $$
> f(x) = \int_{-\infty}^{\infty}\frac{\sin(\lambda a)}{\pi\lambda}e^{i\lambda x}\,d\lambda, \qquad -\infty < x < \infty .
> $$
>
> Of course, at $x = \pm a$ the integral converges to $\frac12$. The function is even and $C$ is real, as Theorem §15.2(3) says; for $a = 1$, $C = \frac12A$ with $A(\lambda) = \frac{2\sin\lambda}{\pi\lambda}$ from [[§14 Fourier Integral#^ex-14-2|Example §14.2]].
>
> *Powers prints the second case of $f$ as $x < |a|$ (p. 115); it should be $|x| > a$.*
>
> *Powers: 1.10, Example (Fourier integral)*

^ex-15-2

> [!example] Example §15.3: The Gaussian and the Uncertainty Relation
> The Gaussian distribution is $f_\sigma(x) = \dfrac{1}{\sqrt{2\pi\sigma^2}}e^{-x^2/(2\sigma^2)}$, with $\int_{-\infty}^{\infty} f_\sigma = 1$.
>
> **(a) Its transform is again a Gaussian.** Complete the square in the exponent:
>
> $$
> -\frac{x^2}{2\sigma^2} - i\lambda x = -\frac{(x + i\sigma^2\lambda)^2}{2\sigma^2} - \frac{\sigma^2\lambda^2}{2} .
> $$
>
> With $x = \sqrt2\,\sigma s$ and the Gaussian integral $\int_{-\infty}^{\infty} e^{-(s - ki)^2}\,ds = \sqrt\pi$ (here $k = -\sigma\lambda/\sqrt2$),
>
> $$
> C(\lambda) = \frac{1}{2\pi}\cdot\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\sigma^2\lambda^2/2}\int_{-\infty}^{\infty} e^{-(x + i\sigma^2\lambda)^2/(2\sigma^2)}\,dx = \frac{1}{2\pi}\cdot\frac{\sqrt2\,\sigma\sqrt\pi}{\sqrt{2\pi\sigma^2}}\,e^{-\sigma^2\lambda^2/2} = \frac{1}{2\pi}e^{-\sigma^2\lambda^2/2} .
> $$
>
> (The shifted Gaussian integral is a fact from complex analysis, a shift of the path of integration. A real-variable check: $I(\lambda) = \int e^{-x^2}\cos\lambda x\,dx$ satisfies $I'(\lambda) = -\int xe^{-x^2}\sin\lambda x\,dx = -\frac\lambda2 I(\lambda)$, differentiating under the integral sign and integrating by parts, and $I(0) = \sqrt\pi$ ([[§28★ The Error Function#^prop-28-1|Proposition §28.1]](d)); so $I(\lambda) = \sqrt\pi e^{-\lambda^2/4}$, which is the case $\sigma^2 = \frac12$ after scaling.) In particular, for $f(x) = e^{-x^2} = \sqrt\pi f_{1/\sqrt2}(x)$, $C(\lambda) = \sqrt\pi\cdot\frac{1}{2\pi}e^{-\lambda^2/4} = \dfrac{e^{-\lambda^2/4}}{2\sqrt\pi}$ (Powers' Exercise 1.10.8). By Theorem §15.2, the real coefficient functions are $A(\lambda) = 2C(\lambda) = \frac1\pi e^{-\sigma^2\lambda^2/2}$ and $B = 0$.
>
> **(b) A heat flow (Midterm 2).** Let $u_t = u_{xx}$ on $-\infty < x < \infty$, $u$ bounded, $u(x, 0) = f_2(x)$ (the Gaussian with $\sigma = 2$). Separation of variables gives the basic solutions $e^{-\lambda^2 t}\big(A(\lambda)\cos\lambda x + B(\lambda)\sin\lambda x\big)$ ([[§27 Infinite Rod#^prop-27-1|Proposition §27.1]]), and by (a) $B = 0$, $A(\lambda) = \frac1\pi e^{-2\lambda^2}$. So
>
> $$
> u(x, t) = \frac1\pi\int_0^{\infty} e^{-\lambda^2 t}e^{-2\lambda^2}\cos\lambda x\,d\lambda = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-(t + 2)\lambda^2 + i\lambda x}\,d\lambda = \frac{1}{2\pi}\sqrt{\frac{\pi}{t + 2}}\,e^{-x^2/(4(t + 2))} = \frac{1}{\sqrt{2\pi(2t + 4)}}\,e^{-x^2/(2(2t + 4))} ,
> $$
>
> completing the square as in (a). The solution is the Gaussian $f_\sigma$ with $\sigma^2 = 2t + 4$: it spreads as time goes on.
>
> **(c) Fourier integral at a fixed time.** At $t = t_0$, $u(x, t_0) = \int_0^{\infty} A_{t_0}(\lambda)\cos(\lambda x)\,d\lambda$ with $A_{t_0}(\lambda) = \frac1\pi\int_{-\infty}^{\infty} u(x, t_0)\cos(\lambda x)\,dx = \frac1\pi e^{-\lambda^2(t_0 + 2)}$, by (a) with $\sigma^2 = 2t_0 + 4$, or simply by reading off the integral in (b).
>
> **(d) Widths.** Let $U_t(x) = u(x, t)$, and let $\Delta x(t)$, $\Delta\lambda(t)$ be the positive values where $U_t$ and $A_t$ drop to half their maxima (at $x = 0$, $\lambda = 0$):
>
> $$
> \frac{U_t(\Delta x)}{U_t(0)} = e^{-\Delta x^2/(4t + 8)} = \frac12 \ \Rightarrow\ \Delta x = \sqrt{(4t + 8)\ln 2}, \qquad \frac{A_t(\Delta\lambda)}{A_t(0)} = e^{-\Delta\lambda^2(t + 2)} = \frac12 \ \Rightarrow\ \Delta\lambda = \sqrt{\frac{\ln 2}{t + 2}} .
> $$
>
> So $\Delta x(t)\cdot\Delta\lambda(t) = \sqrt{4(\ln 2)^2} = 2\ln 2$, a constant. More generally, for any $f_\sigma$, $\Delta x = \sigma\sqrt{2\ln 2}$ and $\Delta\lambda = \sqrt{2\ln 2}/\sigma$: a function narrow in $x$ has a transform wide in $\lambda$, and conversely. This is the mathematical core of the uncertainty principle of quantum mechanics, where $\lambda$ is a wave number and $\hbar\lambda$ a momentum.
>
> The same midterm problem, worked with the real Fourier integral, is [[§27 Infinite Rod#^ex-27-4|Example §27.4]].
>
> *Powers: Exercise 1.10.8 · Source: 341 Midterm 2, Q3 (bonus)*

^ex-15-3

![[m341-15-1.svg]]
*Example §15.3: the temperature $U_t(x)$ (left) and its Fourier cosine coefficient function $A_t(\lambda)$ (right) at $t = 0$ (blue) and $t = 6$ (red). As heat spreads, $U_t$ widens and flattens while $A_t$ narrows (the high frequencies die first, like $e^{-\lambda^2 t}$). The dashed lines mark the half-widths $\Delta x$ and $\Delta\lambda$; their product stays $2\ln 2$.*

> [!remark]- Connections
> - Complex-variables version: [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^ex-51-3|342 Ex. §51.3]] (the shift of the path of integration done by the Cauchy–Goursat theorem on a rectangle, giving $\int_0^\infty e^{-x^2}\cos 2bx\,dx = \frac{\sqrt\pi}{2}e^{-b^2}$); a rotation of the path in the same spirit is [[§88★ Jordan's Lemma#^ex-88-3|342 Ex. §88.3]].

The Fourier integral or transform may be used to solve differential equations on the interval $-\infty < x < \infty$, in much the same way that the Laplace transform is used: it turns derivatives in $x$ into multiplication by $i\lambda$.

> [!example] Example §15.4: Solving the Heat Equation by Fourier Transform
> With Powers' normalization, write $\hat f(\xi) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i\xi x}\,dx$ (that is, $\hat f = C$) and $\check g(x) = \int_{-\infty}^{\infty} g(\xi)e^{ix\xi}\,d\xi$. Use the transform to solve
>
> $$
> u_t = u_{xx}, \quad -\infty < x < \infty, \ t > 0; \qquad u(x, 0) = f(x); \qquad u \text{ bounded as } |x| \to \infty ,
> $$
>
> where $\int|f| < \infty$ and $f(x), f'(x) \to 0$ as $|x| \to \infty$.
>
> **(a) Transform of a derivative.** Integrating by parts,
>
> $$
> \widehat{f'}(\xi) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f'(x)e^{-i\xi x}\,dx = \frac{1}{2\pi}\Big[f(x)e^{-i\xi x}\Big]_{-\infty}^{\infty} + \frac{i\xi}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i\xi x}\,dx = i\xi\hat f(\xi) ,
> $$
>
> since $|f(x)e^{-i\xi x}| = |f(x)| \to 0$ at $\pm\infty$. (In real form: the coefficients of $f'$ are $\lambda B(\lambda)$ and $-\lambda A(\lambda)$, which is [[§14 Fourier Integral#^thm-14-3|Theorem §14.3]].)
>
> **(b) Second derivative.** Applying (a) to $f'$: $\widehat{f''}(\xi) = i\xi\,\widehat{f'}(\xi) = -\xi^2\hat f(\xi)$.
>
> **(c) The transformed problem.** Assume $u$ is smooth with $\int|u(x, t)|\,dx < \infty$ and $u, u_x \to 0$ as $|x| \to \infty$. Transforming $u_t = u_{xx}$ in $x$ (and differentiating under the integral sign in $t$), $\hat u(\xi, t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} u(x, t)e^{-ix\xi}\,dx$ satisfies, for each fixed $\xi$, an ordinary differential equation in $t$:
>
> $$
> \frac{\partial\hat u}{\partial t}(\xi, t) = -\xi^2\hat u(\xi, t), \qquad \hat u(\xi, 0) = \hat f(\xi) .
> $$
>
> **(d) Solve and invert.** Hence $\hat u(\xi, t) = \hat f(\xi)e^{-\xi^2 t}$. By Example §15.3(a) with $\sigma^2 = 2t$, the function $g_t(x) = 2\pi f_{\sqrt{2t}}(x) = \sqrt{\pi/t}\,e^{-x^2/(4t)}$ has $\hat g_t(\xi) = e^{-\xi^2 t}$, so $\hat u = \hat f\,\hat g_t$. In this normalization the convolution theorem reads $\widehat{g_1 \ast  g_2} = 2\pi\,\hat g_1\hat g_2$, where $(g_1 \ast  g_2)(x) = \int g_1(x - y)g_2(y)\,dy$; by Fubini's theorem ([[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]]; the double integral converges absolutely to $\int|g_1|\int|g_2|$),
>
> $$
> \widehat{g_1 * g_2}(\xi) = \frac{1}{2\pi}\int g_2(y)e^{-i\xi y}\Big(\int g_1(x - y)e^{-i\xi(x - y)}\,dx\Big)dy = \frac{1}{2\pi}\cdot 2\pi\hat g_1(\xi)\cdot 2\pi\hat g_2(\xi) .
> $$
>
> So $\hat u = \frac{1}{2\pi}\widehat{f * g_t}$, and inverting (Theorem §15.2),
>
> $$
> u(x, t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x - y)\sqrt{\frac\pi t}\,e^{-y^2/(4t)}\,dy = \int_{-\infty}^{\infty} f(x - y)\,\frac{e^{-y^2/(4t)}}{\sqrt{4\pi t}}\,dy .
> $$
>
> The kernel $e^{-y^2/(4t)}/\sqrt{4\pi t}$ has integral $1$ and concentrates at $y = 0$ as $t \to 0+$, so $u(x, t) \to f(x)$; this is the heat kernel of [[§27 Infinite Rod#^thm-27-3|Theorem §27.3]].
>
> *The exam states the convolution fact as $(\hat g_1\hat g_2)^\vee = g_1 \ast  g_2$, without the factor $\frac{1}{2\pi}$ that this normalization requires; the key follows the exam's statement, so its final answer $\int f(x - y)\sqrt{\pi/t}\,e^{-y^2/(4t)}\,dy$ is $2\pi$ times the solution above and tends to $2\pi f(x)$, not $f(x)$, as $t \to 0+$.*
>
> *Source: 341 Midterm 1, Q3 (bonus)*

^ex-15-4
