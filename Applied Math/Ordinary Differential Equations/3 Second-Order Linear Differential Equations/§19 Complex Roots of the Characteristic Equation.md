---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 19
bdp: "3.3"
aliases: ["BDP 3.3"]
tags: [ordinary-differential-equations, math331]
---
← [[§18 Solutions of Linear Homogeneous Equations; the Wronskian]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§20 Repeated Roots; Reduction of Order]] →

*Boyce–DiPrima, Section 3.3 · MATH 331 Written HW 3, Midterm (Fall 2021).*

When the discriminant $b^2 - 4ac$ is negative, the characteristic equation of $ay'' + by' + cy = 0$ has complex conjugate roots $\lambda \pm i\mu$, and the exponential solutions $e^{(\lambda \pm i\mu)t}$ have complex exponents. Euler's formula $e^{it} = \cos t + i\sin t$ gives them a meaning: $e^{(\lambda + i\mu)t} = e^{\lambda t}(\cos\mu t + i\sin\mu t)$. Since the equation has real coefficients, the real and imaginary parts $e^{\lambda t}\cos\mu t$ and $e^{\lambda t}\sin\mu t$ are real solutions ([[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-6|Theorem §18.6]]), and they form a fundamental set. The solutions oscillate with period $2\pi/\mu$; the factor $e^{\lambda t}$ makes the oscillation decay, grow or keep a constant amplitude according to the sign of $\lambda$.

## Complex Roots

Suppose that $b^2 - 4ac < 0$. Then the roots of the characteristic equation $ar^2 + br + c = 0$ are conjugate complex numbers

$$
r_1 = \lambda + i\mu, \qquad r_2 = \lambda - i\mu , \qquad (4)
$$

with $\lambda$, $\mu$ real, and [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-1|Theorem §17.1]] suggests the solutions

$$
y_1(t) = \exp((\lambda + i\mu)t), \qquad y_2(t) = \exp((\lambda - i\mu)t) . \qquad (5)
$$

With $\lambda = -1$, $\mu = 2$ and $t = 3$, for instance, $y_1(3) = e^{-3 + 6i}$. What does it mean to raise $e$ to a complex power?

## Euler's Formula

> [!remark] Remark: Where Euler's Formula Comes From
> Recall the Taylor series
>
> $$
> e^t = 1 + t + \frac{t^2}{2} + \cdots + \frac{t^n}{n!} + \cdots = \sum_{n=0}^{\infty}\frac{t^n}{n!}, \qquad -\infty < t < \infty . \qquad (7)
> $$
>
> Assume that $it$ may be substituted for $t$:
>
> $$
> e^{it} = \sum_{n=0}^{\infty}\frac{(it)^n}{n!} . \qquad (8)
> $$
>
> Write $(it)^n = i^nt^n$ and use $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, and so on: for even $n = 2k$, $i^n = (i^2)^k = (-1)^k$, and for odd $n = 2k + 1$, $i^n = i(-1)^k$. Separating the real and imaginary terms (allowed because the series converges absolutely for every $t$),
>
> $$
> e^{it} = \sum_{k=0}^{\infty}\frac{(-1)^kt^{2k}}{(2k)!} + i\sum_{k=0}^{\infty}\frac{(-1)^kt^{2k+1}}{(2k+1)!} . \qquad (9)
> $$
>
> The first series is the Taylor series of $\cos t$ about $t = 0$ and the second that of $\sin t$, so $e^{it} = \cos t + i\sin t$. The argument rests on the unverified assumption that (7) holds for complex values, so it only makes the formula plausible. BDP therefore takes the formula as the *definition* of $e^{it}$ ([[§19 Complex Roots of the Characteristic Equation#^def-19-1|Definition §19.1]]). (BDP Problem 3.3.20 outlines a second derivation, from the differential equation $y'' + y = 0$.)

^rem-19-1

> [!definition] Definition §23.1: The Complex Exponential
> **Euler's formula** defines, for real $t$,
>
> $$
> e^{it} = \cos t + i\sin t . \qquad (10)
> $$
>
> Replacing $t$ by $-t$ and by $\mu t$ gives
>
> $$
> e^{-it} = \cos t - i\sin t, \qquad (11) \qquad\qquad e^{i\mu t} = \cos(\mu t) + i\sin(\mu t) . \qquad (12)
> $$
>
> For a complex exponent $(\lambda + i\mu)t$, requiring the law of exponents $e^{(\lambda + i\mu)t} = e^{\lambda t}e^{i\mu t}$ (13) leads to the definition
>
> $$
> e^{(\lambda + i\mu)t} = e^{\lambda t}\big(\cos(\mu t) + i\sin(\mu t)\big) = e^{\lambda t}\cos(\mu t) + ie^{\lambda t}\sin(\mu t) . \qquad (14)
> $$
>
> The real and imaginary parts of $e^{(\lambda + i\mu)t}$ are thus elementary real functions. For example, $e^{-3 + 6i} = e^{-3}\cos 6 + ie^{-3}\sin 6 \approx 0.0478041 - 0.0139113i$.
>
> *BDP: 3.3, Equations (10) and (14)*

^def-19-1

> [!remark]- Connections
> - The series argument of [[§19 Complex Roots of the Characteristic Equation#^rem-19-1|Remark: Where Euler's Formula Comes From]], with its series: [[§90 Taylor and Maclaurin Series#^thm-90-6|Calc Thm. §90.6]] ($e^x$), [[§91 Taylor Series of Important Functions#^thm-91-1|Calc Thm. §91.1]] ($\sin x$), [[§91 Taylor Series of Important Functions#^thm-91-2|Calc Thm. §91.2]] ($\cos x$); the same derivation from the complex-numbers side: [[§64 Complex Numbers#^rem-64-1|235 Remark: Euler's Formula]], where $e^{i\varphi}$ gives the polar form of a complex number.
> - Lay defines $e^{(a+bi)t}$ by the power series and arrives at the same formula (14), used for complex eigenvalues of $\mathbf{x}' = A\mathbf{x}$: [[§46 Applications to Differential Equations#^def-46-3|235 Def. §46.3]].
> - Complex-variables version: [[§7 Exponential Form#^def-7-4|342 Def. §7.4]] (Euler's formula), [[§7 Exponential Form#^def-7-5|342 Def. §7.5]] (the exponential form $z = re^{i\theta}$) and [[§30 The Exponential Function#^def-30-1|342 Def. §30.1]] ($e^z = e^xe^{iy}$ for every complex $z$, whose Maclaurin series is proved in [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]]).

> [!theorem] Proposition §23.1: Rules for the Complex Exponential
> For complex numbers $r$, $r_1$, $r_2$ and real $t$:
>
> $$
> e^{(r_1 + r_2)t} = e^{r_1t}e^{r_2t}, \qquad \frac{d}{dt}\big(e^{rt}\big) = re^{rt} . \qquad (15)
> $$
>
> So the usual laws of exponents and the differentiation formula hold for complex exponents.
>
> *BDP: 3.3 (text), Equation (15)*

^prop-19-1

> [!proof]+ Proof
> *BDP leaves both rules as verifications from (10) and (14) (the first is Problem 3.3.22); here they are.*
>
> **Law of exponents.** Let $r_1 = \lambda_1 + i\mu_1$ and $r_2 = \lambda_2 + i\mu_2$. By (14) and complex multiplication,
>
> $$
> e^{r_1t}e^{r_2t} = e^{\lambda_1t}e^{\lambda_2t}\big[(\cos\mu_1t\cos\mu_2t - \sin\mu_1t\sin\mu_2t) + i(\sin\mu_1t\cos\mu_2t + \cos\mu_1t\sin\mu_2t)\big] .
> $$
>
> By the addition formulas the bracket is $\cos(\mu_1 + \mu_2)t + i\sin(\mu_1 + \mu_2)t$, and $e^{\lambda_1t}e^{\lambda_2t} = e^{(\lambda_1 + \lambda_2)t}$, so the product is $e^{(\lambda_1 + \lambda_2)t}\big(\cos(\mu_1 + \mu_2)t + i\sin(\mu_1 + \mu_2)t\big) = e^{(r_1 + r_2)t}$ by (14).
>
> **Derivative.** Let $r = \lambda + i\mu$. Differentiating the real and imaginary parts in (14) with the product rule,
>
> $$
> \frac{d}{dt}e^{rt} = e^{\lambda t}(\lambda\cos\mu t - \mu\sin\mu t) + ie^{\lambda t}(\lambda\sin\mu t + \mu\cos\mu t) .
> $$
>
> On the other hand, $re^{rt} = (\lambda + i\mu)e^{\lambda t}(\cos\mu t + i\sin\mu t) = e^{\lambda t}\big[(\lambda\cos\mu t - \mu\sin\mu t) + i(\lambda\sin\mu t + \mu\cos\mu t)\big]$, the same.

^pf-19-1

*Uses:* [[§19 Complex Roots of the Characteristic Equation#^def-19-1|Def. §19.1]]

> [!remark]- Connections
> - Complex-variables version: [[§30 The Exponential Function#^thm-30-2|342 Thm. §30.2]] (the law of exponents for all complex exponents) and [[§41 Derivatives of Functions w(t)#^ex-41-2|342 Ex. §41.2]] (the derivative rule, proved the same way).

## The General Solution

> [!example] Example §23.1: Complex Solutions and Their Real Parts
> Find the general solution of
>
> $$
> y'' + y' + 9.25y = 0 , \qquad (16)
> $$
>
> and the solution with $y(0) = 2$, $y'(0) = 8$ (17).
>
> **Complex solutions.** The characteristic equation $r^2 + r + 9.25 = 0$ has roots $r = \frac{-1 \pm \sqrt{1 - 37}}{2}$, that is,
>
> $$
> r_1 = -\tfrac12 + 3i, \qquad r_2 = -\tfrac12 - 3i .
> $$
>
> By [[§19 Complex Roots of the Characteristic Equation#^prop-19-1|Proposition §19.1]] the computation of [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-1|Theorem §17.1]] works for complex $r$, so two solutions are
>
> $$
> y_1(t) = \exp\Big(\Big(-\tfrac12 + 3i\Big)t\Big) = e^{-t/2}\big(\cos 3t + i\sin 3t\big), \qquad y_2(t) = e^{-t/2}\big(\cos 3t - i\sin 3t\big) . \qquad (18), (19)
> $$
>
> Their Wronskian is $W[y_1, y_2](t) = -6ie^{-t}$, which is not zero, so the general solution of (16) can be written as a combination of $y_1$ and $y_2$ with arbitrary (complex) coefficients.
>
> **Real solutions.** The problem has real coefficients, and a real form is preferable. By [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-6|Theorem §18.6]] the real and imaginary parts of $y_1$,
>
> $$
> u(t) = e^{-t/2}\cos 3t, \qquad v(t) = e^{-t/2}\sin 3t , \qquad (20)
> $$
>
> are real-valued solutions. Their Wronskian is $W[u, v](t) = 3e^{-t}$ (formula (24) below with $\lambda = -\frac12$, $\mu = 3$), which is not zero, so they form a fundamental set and the general solution is
>
> $$
> y = c_1u(t) + c_2v(t) = e^{-t/2}\big(c_1\cos 3t + c_2\sin 3t\big) . \qquad (21)
> $$
>
> **The initial value problem.** Setting $t = 0$ and $y = 2$ in (21) gives $c_1 = 2$. Differentiating, $y' = e^{-t/2}\big[(-\frac12c_1 + 3c_2)\cos 3t + (-3c_1 - \frac12c_2)\sin 3t\big]$, so $y'(0) = -\frac12c_1 + 3c_2 = 8$ and $c_2 = 3$:
>
> $$
> y = e^{-t/2}\big(2\cos 3t + 3\sin 3t\big) . \qquad (22)
> $$
>
> The solution oscillates with period $2\pi/3$, and the factor $e^{-t/2}$ makes the amplitude decay to zero (Figure (a) below).
>
> *BDP: Example 3.3.1*

^ex-19-1

> [!theorem] Theorem §23.2: General Solution for Complex Roots
> If the roots of the characteristic equation $ar^2 + br + c = 0$ are the complex numbers $\lambda \pm i\mu$ with $\mu \ne 0$, then
>
> $$
> u(t) = e^{\lambda t}\cos(\mu t), \qquad v(t) = e^{\lambda t}\sin(\mu t) \qquad (23)
> $$
>
> are real solutions of $ay'' + by' + cy = 0$ with Wronskian
>
> $$
> W[u, v](t) = \mu e^{2\lambda t} , \qquad (24)
> $$
>
> so they form a fundamental set, and the general solution is
>
> $$
> y = c_1e^{\lambda t}\cos(\mu t) + c_2e^{\lambda t}\sin(\mu t) , \qquad (25)
> $$
>
> where $c_1$ and $c_2$ are arbitrary constants.
>
> *BDP: 3.3 (text), Equations (23)–(25)*

^thm-19-2

> [!proof]+ Proof
> **Complex solutions.** Let $r = \lambda + i\mu$. By [[§19 Complex Roots of the Characteristic Equation#^prop-19-1|Proposition §19.1]], $\frac{d}{dt}e^{rt} = re^{rt}$ and $\frac{d^2}{dt^2}e^{rt} = r^2e^{rt}$, so, exactly as in the proof of [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-1|Theorem §17.1]],
>
> $$
> a\big(e^{rt}\big)'' + b\big(e^{rt}\big)' + ce^{rt} = (ar^2 + br + c)e^{rt} = 0 .
> $$
>
> So $y_1 = e^{(\lambda + i\mu)t}$ is a complex-valued solution.
>
> **Real solutions.** By (14), $y_1 = e^{\lambda t}\cos\mu t + ie^{\lambda t}\sin\mu t = u + iv$. The equation (divided by $a$) has real constant coefficients, so $u$ and $v$ are solutions by [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-6|Theorem §18.6]]. (Using $y_2 = e^{(\lambda - i\mu)t}$ instead gives $u$ and $-v$, nothing new.)
>
> **The Wronskian.** BDP leaves (24) as Problem 3.3.19. With $u' = e^{\lambda t}(\lambda\cos\mu t - \mu\sin\mu t)$ and $v' = e^{\lambda t}(\lambda\sin\mu t + \mu\cos\mu t)$,
>
> $$
> W[u, v] = uv' - u'v = e^{2\lambda t}\big[\cos\mu t\,(\lambda\sin\mu t + \mu\cos\mu t) - \sin\mu t\,(\lambda\cos\mu t - \mu\sin\mu t)\big] = \mu e^{2\lambda t}\big(\cos^2\mu t + \sin^2\mu t\big) = \mu e^{2\lambda t} .
> $$
>
> Since $\mu \ne 0$, $W \ne 0$, so $u$, $v$ form a fundamental set and (25) is the general solution by [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|Theorem §18.4]]. (If $\mu = 0$, the roots are real and equal, the case of [[§20 Repeated Roots; Reduction of Order#^thm-20-1|Theorem §20.1]].)

^pf-19-2

*Uses:* [[§19 Complex Roots of the Characteristic Equation#^prop-19-1|§19.1]], [[§19 Complex Roots of the Characteristic Equation#^def-19-1|Def. §19.1]], [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-1|§17.1]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-6|§18.6]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|§18.4]]

> [!remark]- Connections
> - The systems version: for a real matrix with complex eigenvalue $a + bi$ and eigenvector $\mathbf{v}$, the real and imaginary parts of $\mathbf{v}e^{(a+bi)t}$ are two real solutions of $\mathbf{x}' = A\mathbf{x}$, [[§46 Applications to Differential Equations#^thm-46-4|235 Thm. §46.4]]; in this subject [[§38 Complex-Valued Eigenvalues#^thm-38-2|Theorem §38.2]] (BDP 7.6).

The solution (25) can be written down as soon as $\lambda$ and $\mu$ are known; by the quadratic formula (with $a > 0$), $\lambda = -\frac{b}{2a}$ and $\mu = \frac{\sqrt{4ac - b^2}}{2a}$.

> [!remark] Remark: The Sign of λ
> Every solution (25) oscillates, with period $2\pi/\mu$ in the trigonometric factors. The factor $e^{\lambda t}$ controls the amplitude: for $\lambda < 0$ the oscillations decay to zero, for $\lambda > 0$ they grow without bound, and for $\lambda = 0$ (that is, $b = 0$) there is no exponential factor and the solution is a pure oscillation of constant amplitude, whose amplitude and phase are set by the initial conditions.

^rem-19-2

> [!example] Example §23.2: Two Course Initial Value Problems
> **(a)** Solve $y'' + 6y' + 13y = 0$, $y(0) = 2$, $y'(0) = -1$.
>
> Completing the square in $r^2 + 6r + 13 = 0$: $(r + 3)^2 = -4$, so $r + 3 = \pm 2i$ and $r = -3 \pm 2i$, with $\lambda = -3$, $\mu = 2$. By [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|Theorem §19.2]],
>
> $$
> y = c_1e^{-3t}\cos 2t + c_2e^{-3t}\sin 2t, \qquad y' = e^{-3t}\big[(-3c_1 + 2c_2)\cos 2t + (-2c_1 - 3c_2)\sin 2t\big] .
> $$
>
> $y(0) = c_1 = 2$ and $y'(0) = -3c_1 + 2c_2 = -6 + 2c_2 = -1$, so $c_2 = \frac52$:
>
> $$
> y = 2e^{-3t}\cos 2t + \tfrac52e^{-3t}\sin 2t .
> $$
>
> **(b)** Solve $y'' + 6y' + 10y = 0$, $y(0) = 2$, $y'(0) = -7$.
>
> Now $(r + 3)^2 = -1$, so $r = -3 \pm i$: $\lambda = -3$, $\mu = 1$, and $y = e^{-3t}(c_1\cos t + c_2\sin t)$. From $y(0) = c_1 = 2$ and $y'(0) = -3c_1 + c_2 = -7$ we get $c_2 = -1$:
>
> $$
> y = e^{-3t}\big(2\cos t - \sin t\big) .
> $$
>
> Both solutions decay in an oscillating way, since $\lambda = -3 < 0$.
>
> *Source: 331 Written HW 3, Problem 2; 331 Midterm (Fall 2021), Q4*

^ex-19-2

> [!example] Example §23.3: Growing and Pure Oscillations
> **(a)** Solve $16y'' - 8y' + 145y = 0$, $y(0) = -2$, $y'(0) = 1$. (26)
>
> The characteristic equation $16r^2 - 8r + 145 = 0$ has roots $r = \frac{8 \pm \sqrt{64 - 9280}}{32} = \frac{8 \pm 96i}{32} = \frac14 \pm 3i$. So
>
> $$
> y(t) = c_1e^{t/4}\cos 3t + c_2e^{t/4}\sin 3t . \qquad (27)
> $$
>
> $y(0) = c_1 = -2$, and differentiating before setting $t = 0$, $y'(0) = \frac14c_1 + 3c_2 = 1$, so $c_2 = \frac12$:
>
> $$
> y = -2e^{t/4}\cos 3t + \tfrac12e^{t/4}\sin 3t . \qquad (28)
> $$
>
> This is a growing oscillation: the trigonometric factors again have period $2\pi/3$, and the factor $e^{t/4}$, with positive exponent, makes the amplitude increase.
>
> **(b)** Find the general solution of $y'' + 9y = 0$. (29)
>
> The characteristic equation $r^2 + 9 = 0$ has roots $r = \pm 3i$, so $\lambda = 0$, $\mu = 3$, and
>
> $$
> y = c_1\cos 3t + c_2\sin 3t . \qquad (30)
> $$
>
> With no exponential factor, every solution is a pure oscillation with period $2\pi/3$ and constant amplitude; the initial conditions determine the amplitude and the phase. For instance $y(0) = 2$, $y'(0) = 8$ gives $c_1 = 2$, $3c_2 = 8$, so $y = 2\cos 3t + \frac83\sin 3t$, of amplitude $\sqrt{4 + 64/9} = \frac{10}{3}$.
>
> *BDP: Examples 3.3.2 and 3.3.3*

^ex-19-3

![[m331-15-1.svg]]
*The three possibilities of [[§19 Complex Roots of the Characteristic Equation#^rem-19-2|Remark: The Sign of λ]], each with $\mu = 3$ and so period $2\pi/3$. (a) $y = e^{-t/2}(2\cos 3t + 3\sin 3t)$ from [[§19 Complex Roots of the Characteristic Equation#^ex-19-1|Example §19.1]], inside the decaying envelope $\pm\sqrt{13}\,e^{-t/2}$ (dashed). (b) $y = e^{t/4}(-2\cos 3t + \frac12\sin 3t)$ from [[§19 Complex Roots of the Characteristic Equation#^ex-19-3|Example §19.3]](a), inside the growing envelope $\pm\sqrt{17/4}\,e^{t/4}$. (c) $y = 2\cos 3t + \frac83\sin 3t$ from [[§19 Complex Roots of the Characteristic Equation#^ex-19-3|Example §19.3]](b), with constant amplitude $\frac{10}{3}$. In each case the envelope is $\pm\sqrt{c_1^2 + c_2^2}\,e^{\lambda t}$.*
