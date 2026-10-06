---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 54
bc: "54"
aliases: ["B&C 54"]
tags: [complex-variables, math342]
---
← [[§53 Multiply Connected Domains]] · ↑ [[· 4 Integrals]] · [[§55 An Extension of the Cauchy Integral Formula]] →

*Brown–Churchill, Section 54 (with Exercises 1, 2, 7 of Section 57) · MAT 342 HW 7.*

The Cauchy integral formula expresses the value of an analytic function at any point inside a simple closed contour as an integral of its values on the contour. So the values of $f$ on $C$ completely determine its values inside, a rigidity with no counterpart for differentiable functions of a real variable. The proof deforms $C$ into a small circle about the point and lets the circle shrink, using only the continuity of $f$ there. Read backwards, the formula evaluates contour integrals of the form $\int_C f(z)\,dz/(z - z_0)$ without any parametrization, and it is the source of everything in the following sections: derivatives of all orders, Liouville's theorem, the maximum modulus principle, Taylor series.

> [!theorem] Theorem §54.1: Cauchy Integral Formula
> Let $f$ be analytic everywhere inside and on a simple closed contour $C$, taken in the positive sense. If $z_0$ is any point interior to $C$, then
>
> $$
> f(z_0) = \frac{1}{2\pi i}\int_C \frac{f(z)\,dz}{z - z_0} . \qquad (1)
> $$
>
> Written as
>
> $$
> \int_C \frac{f(z)\,dz}{z - z_0} = 2\pi i\,f(z_0) , \qquad (5)
> $$
>
> it can be used to evaluate certain integrals along simple closed contours.
>
> *B&C: Sec. 54, Theorem and equation (5)*

^thm-54-1

> [!proof]+ Proof
> **Deformation to a small circle.** Let $C_\rho$ denote a positively oriented circle $|z - z_0| = \rho$, where $\rho$ is small enough that $C_\rho$ is interior to $C$ (possible because $z_0$ is interior to $C$, so some disk about $z_0$ lies inside $C$). The quotient $f(z)/(z - z_0)$ is analytic at every point of the closed region between and on the contours $C_\rho$ and $C$, since $f$ is analytic there and $z - z_0 \ne 0$. By the principle of deformation of paths,
>
> $$
> \int_C \frac{f(z)\,dz}{z - z_0} = \int_{C_\rho}\frac{f(z)\,dz}{z - z_0} .
> $$
>
> This enables us to write
>
> $$
> \int_C \frac{f(z)\,dz}{z - z_0} - f(z_0)\int_{C_\rho}\frac{dz}{z - z_0} = \int_{C_\rho}\frac{f(z) - f(z_0)}{z - z_0}\,dz . \qquad (2)
> $$
>
> But $\int_{C_\rho} dz/(z - z_0) = 2\pi i$ ([[§45 Some Examples (Contour Integrals)#^ex-45-5|Example §45.5]]), and so equation (2) becomes
>
> $$
> \int_C \frac{f(z)\,dz}{z - z_0} - 2\pi i\,f(z_0) = \int_{C_\rho}\frac{f(z) - f(z_0)}{z - z_0}\,dz . \qquad (3)
> $$
>
> **Shrinking the circle.** The left side of (3) does not depend on $\rho$. Now the fact that $f$ is analytic, and therefore continuous, at $z_0$ ensures that corresponding to each positive number $\varepsilon$, however small, there is a positive number $\delta$ such that
>
> $$
> |f(z) - f(z_0)| < \varepsilon \qquad\text{whenever}\qquad |z - z_0| < \delta . \qquad (4)
> $$
>
> Let the radius $\rho$ of $C_\rho$ be smaller than $\delta$. Since $|z - z_0| = \rho < \delta$ when $z$ is on $C_\rho$, the first of inequalities (4) holds there, and the integrand on the right of (3) has modulus less than $\varepsilon/\rho$. The upper bound for moduli of contour integrals ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]), with $C_\rho$ of length $2\pi\rho$, gives
>
> $$
> \left| \int_{C_\rho}\frac{f(z) - f(z_0)}{z - z_0}\,dz \right| < \frac{\varepsilon}{\rho}\,2\pi\rho = 2\pi\varepsilon .
> $$
>
> In view of equation (3), then,
>
> $$
> \left| \int_C \frac{f(z)\,dz}{z - z_0} - 2\pi i\,f(z_0) \right| < 2\pi\varepsilon .
> $$
>
> The left side is a nonnegative constant that is less than an arbitrarily small positive number, so it is $0$. Hence equation (1) is valid.

^pf-54-1

*Uses:* [[§53 Multiply Connected Domains#^cor-53-2|§53.2]], [[§45 Some Examples (Contour Integrals)#^ex-45-5|Ex. §45.5]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]], [[§19 Derivatives#^thm-19-1|§19.1]]

![[m342-54-1.svg]]
*The proof. The integrand $f(z)/(z - z_0)$ is analytic in the shaded region between $C$ and the small circle $C_\rho$, so the two integrals are equal. On $C_\rho$, $f(z)$ is within $\varepsilon$ of $f(z_0)$ once $\rho$ is small; what remains is $f(z_0)\int_{C_\rho}dz/(z - z_0) = 2\pi i\,f(z_0)$.*

> [!remark]- Connections
> - For a circle $C$ centered at $z_0$, formula (1) says that $f(z_0)$ is the average of $f$ over the circle: Gauss's mean value theorem, [[§59 Maximum Modulus Principle#^thm-59-1|§59.1]]. Its real part is the mean value property of harmonic functions, [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-2|341 Thm. §49.2]], and the Poisson integral formula [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-1|341 Thm. §49.1]] is the corresponding statement that a harmonic function in a disk is determined by its boundary values.

> [!remark] Remark: Method — Evaluating Contour Integrals by Cauchy's Formula
> For $\int_C g(z)\,dz$, $C$ a simple closed contour:
> 1. **Find the singular points** of $g$ (factor the denominator) and decide which lie inside $C$. None inside: the integral is $0$ (Cauchy–Goursat).
> 2. **One singular point $z_0$ inside, a simple factor:** write $g(z) = \dfrac{f(z)}{z - z_0}$, putting into $f$ everything except $z - z_0$, and check that $f$ is analytic inside and on $C$ (its own singular points lie outside $C$). Then $\int_C g(z)\,dz = 2\pi i\,f(z_0)$.
> 3. **A repeated factor $(z - z_0)^{n+1}$:** write $g(z) = f(z)/(z - z_0)^{n+1}$ and use the extension, $\int_C g(z)\,dz = \dfrac{2\pi i}{n!}f^{(n)}(z_0)$ ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]], stated in [[§55 An Extension of the Cauchy Integral Formula|§55]]).
> 4. **Several singular points inside:** surround them by small disjoint circles and add the contributions ([[§53 Multiply Connected Domains#^rem-53-1|Remark: Method — Deforming a Contour]]), or split $g$ by partial fractions.
> 5. **Orientation:** the formulas are for $C$ in the positive sense; for the clockwise direction change the sign.

^rem-54-1

> [!example] Example §54.1: A Factor of z Inside the Unit Circle
> Let $C$ be the positively oriented circle $|z| = 1$ about the origin. Since the function
>
> $$
> f(z) = \frac{\cos z}{z^2 + 9}
> $$
>
> is analytic inside and on $C$ (its singular points $\pm 3i$ are outside), and since the origin $z_0 = 0$ is interior to $C$, equation (5) tells us that
>
> $$
> \int_C \frac{\cos z}{z(z^2 + 9)}\,dz = \int_C \frac{(\cos z)/(z^2 + 9)}{z - 0}\,dz = 2\pi i\,f(0) = \frac{2\pi i}{9} .
> $$
>
> (Quadrature: $0.6981317\ldots i = 2\pi i/9$.)
>
> *B&C: Sec. 54, Example*

^ex-54-1

> [!example] Example §54.2: Two Integrals Around a Square
> Let $C$ denote the positively oriented boundary of the square whose sides lie along the lines $x = \pm2$ and $y = \pm2$. Evaluate (a) $\displaystyle\int_C \frac{e^{-z}\,dz}{z - (\pi i/2)}$ and (c) $\displaystyle\int_C \frac{z\,dz}{2z + 1}$.
>
> **(a)** The point $z_0 = \pi i/2 \approx 1.57i$ lies inside the square, and $f(z) = e^{-z}$ is entire. By (5),
>
> $$
> \int_C \frac{e^{-z}\,dz}{z - (\pi i/2)} = 2\pi i\,e^{-\pi i/2} = 2\pi i\,(-i) = 2\pi .
> $$
>
> **(c)** First make the coefficient of $z$ in the denominator equal to $1$: $\dfrac{z}{2z + 1} = \dfrac{z/2}{z - (-\frac12)}$. The point $-\frac12$ lies inside the square and $f(z) = z/2$ is entire, so
>
> $$
> \int_C \frac{z\,dz}{2z + 1} = 2\pi i\,f\big(-\tfrac12\big) = 2\pi i\Big(-\frac14\Big) = -\frac{\pi i}{2} .
> $$
>
> (B&C's answers: (a) $2\pi$, (c) $-\pi i/2$; quadrature along the four sides agrees.)
>
> *B&C: Sec. 57, Exercise 1(a), (c); Source: 342 HW 7*

^ex-54-2

> [!example] Example §54.3: One Singular Point Inside, One Outside
> Find the value of the integral of $g(z) = \dfrac{1}{z^2 + 4}$ around the circle $|z - i| = 2$ in the positive sense.
>
> The singular points are the zeros of $z^2 + 4 = (z - 2i)(z + 2i)$. Since $|2i - i| = 1 < 2$, the point $2i$ is inside the circle; since $|-2i - i| = 3 > 2$, the point $-2i$ is outside. So write
>
> $$
> g(z) = \frac{f(z)}{z - 2i}, \qquad f(z) = \frac{1}{z + 2i} ,
> $$
>
> where $f$ is analytic inside and on the circle. By (5),
>
> $$
> \int_C \frac{dz}{z^2 + 4} = 2\pi i\,f(2i) = \frac{2\pi i}{4i} = \frac{\pi}{2} .
> $$
>
> (B&C's answer: $\pi/2$; quadrature over the circle gives $1.5707963\ldots$)
>
> *B&C: Sec. 57, Exercise 2(a); Source: 342 HW 7*

^ex-54-3

> [!example] Example §54.4: A Real Integral from the Cauchy Formula
> Let $C$ be the unit circle $z = e^{i\theta}$ ($-\pi \le \theta \le \pi$). First show that for any real constant $a$,
>
> $$
> \int_C \frac{e^{az}}{z}\,dz = 2\pi i .
> $$
>
> Then write this integral in terms of $\theta$ to derive the integration formula
>
> $$
> \int_0^\pi e^{a\cos\theta}\cos(a\sin\theta)\,d\theta = \pi .
> $$
>
> **The contour integral.** $f(z) = e^{az}$ is entire and $0$ is inside $C$, so by (5) the integral is $2\pi i\,e^{a \cdot 0} = 2\pi i$.
>
> **In terms of $\theta$.** With $z = e^{i\theta}$, $dz = ie^{i\theta}\,d\theta$, and $az = a\cos\theta + ia\sin\theta$,
>
> $$
> \int_C \frac{e^{az}}{z}\,dz = \int_{-\pi}^{\pi}\frac{e^{ae^{i\theta}}}{e^{i\theta}}\,ie^{i\theta}\,d\theta = i\int_{-\pi}^{\pi}e^{a\cos\theta}\big[\cos(a\sin\theta) + i\sin(a\sin\theta)\big]\,d\theta .
> $$
>
> Setting this equal to $2\pi i$ and dividing by $i$,
>
> $$
> \int_{-\pi}^{\pi}e^{a\cos\theta}\cos(a\sin\theta)\,d\theta + i\int_{-\pi}^{\pi}e^{a\cos\theta}\sin(a\sin\theta)\,d\theta = 2\pi .
> $$
>
> Both integrals are real, so comparing real parts, $\int_{-\pi}^{\pi}e^{a\cos\theta}\cos(a\sin\theta)\,d\theta = 2\pi$ (and comparing imaginary parts, the second integral is $0$, as it must be since its integrand is odd). The integrand $e^{a\cos\theta}\cos(a\sin\theta)$ is even in $\theta$, because $\cos(-\theta) = \cos\theta$ and $\cos(a\sin(-\theta)) = \cos(-a\sin\theta) = \cos(a\sin\theta)$. Hence the integral over $0 \le \theta \le \pi$ is half of $2\pi$, which is $\pi$. (Quadrature for $a = 0.7$ and $a = 2.5$: $3.14159265\ldots$)
>
> *B&C: Sec. 57, Exercise 7; Source: 342 HW 7*

^ex-54-4
