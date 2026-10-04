---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 44
bc: "44"
aliases: ["B&C 44"]
tags: [complex-variables, math342]
---
← [[§43 Contours]] · ↑ [[· 4 Integrals]] · [[§45 Some Examples (Contour Integrals)]] →

*Brown–Churchill, Section 44 · MAT 342 HW 5, Practice Finals (Fall 2002, Spring 2005).*

The integral of $f(z)$ along a contour $C$ is defined by pulling it back along a parametrization $z = z(t)$ to an integral of the kind studied in [[§42 Definite Integrals of Functions w(t)#^def-42-1|§42]]: $\int_C f(z)\,dz = \int_a^b f[z(t)]\,z'(t)\,dt$. It is a line integral, and its value depends on $f$ and, in general, on $C$, but not on the parametrization chosen for $C$. This section proves that invariance and the four properties (constant multiples, sums, reversing a contour, joining contours) on which every later computation rests. Unlike a real integral, a contour integral has no ready interpretation as an area; its meaning emerges from the theorems of the following sections.

## The Definition

> [!definition] Definition §44.1: Contour Integral
> Let
>
> $$
> z = z(t) \qquad (a \le t \le b) \qquad (1)
> $$
>
> represent a contour $C$ extending from $z_1 = z(a)$ to $z_2 = z(b)$, and suppose that $f[z(t)]$ is piecewise continuous on $a \le t \le b$; we then say that $f(z)$ is **piecewise continuous on $C$**. The **contour integral**, or line integral, of $f$ along $C$ is
>
> $$
> \int_C f(z)\,dz = \int_a^b f[z(t)]\,z'(t)\,dt . \qquad (2)
> $$
>
> Since $C$ is a contour, $z'(t)$ is piecewise continuous too, so the integrand on the right is piecewise continuous and the integral exists ([[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]]). When the value is independent of the contour taken between two fixed points, it is also written $\int_{z_1}^{z_2} f(z)\,dz$.
>
> *B&C: Sec. 44 (text)*

^def-44-1

> [!remark]- Connections
> - With $f = u + iv$ and $z = x + iy$, (2) splits into two real line integrals with respect to $x$ and $y$, [[§108 Line Integrals#^def-108-4|Calc Def. §108.4]]: $\int_C f\,dz = \int_C u\,dx - v\,dy + i\int_C v\,dx + u\,dy$. This is made precise in [[§50 Cauchy–Goursat Theorem#^prop-50-1|Proposition §50.1]], where it is the bridge to Green's theorem.

The value does not depend on the parametrization used, for the changes of parameter of [[§43 Contours#^def-43-2|§43]].

> [!theorem] Proposition §44.1: Invariance Under a Change of Parameter
> Let $C$ be the contour (1), let $f$ be piecewise continuous on $C$, and let $\phi$ be a change of parameter ([[§43 Contours#^def-43-2|Definition §43.2]]), with $Z(\tau) = z[\phi(\tau)]$. Then
>
> $$
> \int_a^b f[z(t)]\,z'(t)\,dt = \int_\alpha^\beta f[Z(\tau)]\,Z'(\tau)\,d\tau .
> $$
>
> *B&C: Sec. 44 (text); Sec. 46, Exercise 12*

^prop-44-1

> [!proof]+ Proof
> B&C says this "can be seen by following the same general procedure" as for arc length; here it is.
>
> **Smooth arc, continuous $f$.** Then $w(t) = f[z(t)]z'(t)$ is continuous on $[a, b]$, and by [[§43 Contours#^lem-43-1|Lemma §43.1]](b) and the chain rule (14) of [[§43 Contours#^lem-43-2|Lemma §43.2]],
>
> $$
> \int_a^b f[z(t)]\,z'(t)\,dt = \int_\alpha^\beta f\big[z(\phi(\tau))\big]\,z'[\phi(\tau)]\,\phi'(\tau)\,d\tau = \int_\alpha^\beta f[Z(\tau)]\,Z'(\tau)\,d\tau .
> $$
>
> **General case.** Let $a = t_0 < t_1 < \cdots < t_n = b$ include the points where the smooth arcs of $C$ meet and the points where $f[z(t)]$ is discontinuous, and let $\tau_k = \phi^{-1}(t_k)$; $\phi$ is a strictly increasing bijection, so $\alpha = \tau_0 < \cdots < \tau_n = \beta$, and $\phi$ maps $[\tau_{k-1}, \tau_k]$ onto $[t_{k-1}, t_k]$. On each such piece, after $f[z(t)]$ is redefined at the endpoints by its one-sided limits (which changes no integral), the smooth case applies. Adding over $k$ ([[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]](d)) gives the result.

^pf-44-1

*Uses:* [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§43 Contours#^def-43-2|Def. §43.2]], [[§43 Contours#^lem-43-1|§43.1]], [[§43 Contours#^lem-43-2|§43.2]], [[§42 Definite Integrals of Functions w(t)#^prop-42-1|§42.1]]

## Properties

> [!definition] Definition §44.2: Opposite, Sum and Difference of Contours
> If $C$ is a contour, $-C$ denotes the same set of points with the order reversed: if $C$ has the representation (1), a representation of $-C$ is
>
> $$
> z = z(-t) \qquad (-b \le t \le -a) . \qquad (3)
> $$
>
> If $C_1$ is a contour from $z_1$ to $z_2$ and $C_2$ is a contour from $z_2$ to $z_3$, the contour $C$ consisting of $C_1$ followed by $C_2$ is their **sum**, $C = C_1 + C_2$. When $C_1$ and $C_2$ have the same final point, $C_1 - C_2$ denotes the sum $C_1 + (-C_2)$.
>
> *B&C: Sec. 44 (text)*

^def-44-2

(A single parametrization of $C_1 + C_2$ is obtained by shifting the parameter interval of $C_2$ linearly so that it starts where that of $C_1$ ends; by Proposition §44.1 it does not matter how.)

> [!theorem] Theorem §44.2: Properties of Contour Integrals
> Let $f$ and $g$ be piecewise continuous on the contours involved, and let $z_0$ be a complex constant. Then
>
> $$
> \int_C z_0f(z)\,dz = z_0\int_C f(z)\,dz , \qquad (4)
> $$
>
> $$
> \int_C \big[f(z) + g(z)\big]\,dz = \int_C f(z)\,dz + \int_C g(z)\,dz , \qquad (5)
> $$
>
> $$
> \int_{-C} f(z)\,dz = -\int_C f(z)\,dz , \qquad (6)
> $$
>
> $$
> \int_{C_1 + C_2} f(z)\,dz = \int_{C_1} f(z)\,dz + \int_{C_2} f(z)\,dz . \qquad (7)
> $$
>
> *B&C: Sec. 44 (text)*

^thm-44-2

> [!proof]+ Proof
> **(4), (5).** By definition (2) the integrands are $z_0f[z(t)]z'(t)$ and $f[z(t)]z'(t) + g[z(t)]z'(t)$; apply [[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]](b).
>
> **(6).** Use representation (3) for $-C$. By [[§41 Derivatives of Functions w(t)#^prop-41-1|Proposition §41.1]](d), $\frac{d}{dt}z(-t) = -z'(-t)$, where $z'(-t)$ is the derivative of $z(t)$ with respect to $t$, evaluated at $-t$. So
>
> $$
> \int_{-C} f(z)\,dz = \int_{-b}^{-a} f[z(-t)]\,\frac{d}{dt}z(-t)\,dt = -\int_{-b}^{-a} f[z(-t)]\,z'(-t)\,dt .
> $$
>
> The substitution $\tau = -t$ ([[§43 Contours#^lem-43-1|Lemma §43.1]](a), applied to $w(t) = f[z(t)]z'(t)$) turns the last integral into $\int_a^b f[z(\tau)]\,z'(\tau)\,d\tau = \int_C f(z)\,dz$, which proves (6).
>
> **(7).** Let $C$, with representation (1), consist of a contour $C_1$ from $z_1$ to $z_2$ followed by a contour $C_2$ from $z_2$ to $z_3$. There is a value $c$ of $t$, $a < c < b$, with $z(c) = z_2$, and $C_1$ and $C_2$ are represented by $z = z(t)$ on $a \le t \le c$ and on $c \le t \le b$. By [[§42 Definite Integrals of Functions w(t)#^prop-42-1|Proposition §42.1]](d),
>
> $$
> \int_a^b f[z(t)]\,z'(t)\,dt = \int_a^c f[z(t)]\,z'(t)\,dt + \int_c^b f[z(t)]\,z'(t)\,dt ,
> $$
>
> which is (7). If $C_1$ and $C_2$ come with their own parametrizations, Proposition §44.1 shows that the integrals do not change when they are combined into one, as described above.

^pf-44-2

*Uses:* [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§44 Contour Integrals#^def-44-2|Def. §44.2]], [[§44 Contour Integrals#^prop-44-1|§44.1]], [[§42 Definite Integrals of Functions w(t)#^prop-42-1|§42.1]], [[§41 Derivatives of Functions w(t)#^prop-41-1|§41.1]], [[§43 Contours#^lem-43-1|§43.1]]

> [!remark]- Connections
> - Property (6) is [[§108 Line Integrals#^thm-108-4|Calc Thm. §108.4]] (reversing the orientation of a line integral with respect to $x$ or $y$), and (7) is the additivity over pieces used there for piecewise-smooth curves.

## Examples from the Definition

> [!example] Example §44.1: The Integral of z̄ Along a Half Circle, Two Ways
> Let $C$ be the right half of the circle $|z| = 2$ from $-2i$ to $2i$ ([[§43 Contours#^ex-43-4|Example §43.4]]). Evaluate $\int_C \bar z\,dz$ using each representation.
>
> **(a) $z = 2e^{i\theta}$, $-\frac\pi2 \le \theta \le \frac\pi2$.** Here $\bar z = 2e^{-i\theta}$ and $z'(\theta) = 2ie^{i\theta}$, so the integrand of (2) is the constant $4i$ and
>
> $$
> \int_C \bar z\,dz = \int_{-\pi/2}^{\pi/2} 4i\,d\theta = 4\pi i .
> $$
>
> **(b) $z = \sqrt{4 - y^2} + iy$, $-2 \le y \le 2$.** Here $Z'(y) = -\dfrac{y}{\sqrt{4 - y^2}} + i$ for $-2 < y < 2$, and
>
> $$
> \overline{Z(y)}\,Z'(y) = \big(\sqrt{4 - y^2} - iy\big)\Big(-\frac{y}{\sqrt{4 - y^2}} + i\Big) = -y + i\sqrt{4 - y^2} + \frac{iy^2}{\sqrt{4 - y^2}} + y = \frac{4i}{\sqrt{4 - y^2}} .
> $$
>
> So
>
> $$
> \int_C \bar z\,dz = \int_{-2}^{2}\frac{4i\,dy}{\sqrt{4 - y^2}} = 4i\Big[\arcsin\frac y2\Big]_{-2}^{2} = 4i\Big(\frac\pi2 + \frac\pi2\Big) = 4\pi i .
> $$
>
> The integrand is unbounded at $y = \pm2$, so this is a convergent improper integral: as noted in [[§43 Contours#^ex-43-4|Example §43.4]], this representation is not smooth at the endpoints, and Proposition §44.1 applies only on $[-2 + \delta, 2 - \delta]$; letting $\delta \to 0$ recovers the same value $4\pi i$.
>
> *B&C: Sec. 46, Exercise 11*

^ex-44-1

> [!example] Example §44.2: zᵐ z̄ⁿ Around the Unit Circle
> Let $m$ and $n$ be integers and $C$ the unit circle $|z| = 1$, counterclockwise. With $z = e^{i\theta}$ $(0 \le \theta \le 2\pi)$, $\bar z = e^{-i\theta}$ and $z' = ie^{i\theta}$, so
>
> $$
> \int_C z^m\bar z^n\,dz = \int_0^{2\pi} e^{im\theta}e^{-in\theta}\,ie^{i\theta}\,d\theta = i\int_0^{2\pi} e^{i(m+1)\theta}e^{-in\theta}\,d\theta = \begin{cases} 2\pi i & \text{when } n = m + 1, \\ 0 & \text{otherwise,} \end{cases}
> $$
>
> by the orthogonality relation of [[§42 Definite Integrals of Functions w(t)#^ex-42-4|Example §42.4]] with $m + 1$ in place of $m$. For instance $\int_C \bar z\,dz = 2\pi i$ $(m = 0, n = 1)$ and $\int_C dz/z = 2\pi i$ $(m = -1, n = 0)$; on $C$ the two integrands agree, since $\bar z = 1/z$ when $|z| = 1$.
>
> *B&C: Sec. 46, Exercise 10*

^ex-44-2

> [!example] Example §44.3: A Piecewise Continuous Integrand
> Let
>
> $$
> f(z) = \begin{cases} 1 & \text{when } y < 0, \\ 4y & \text{when } y > 0, \end{cases}
> $$
>
> and let $C$ be the arc from $z = -1 - i$ to $z = 1 + i$ along the curve $y = x^3$. Use $x$ as the parameter: $z = x + ix^3$ $(-1 \le x \le 1)$, $z'(x) = 1 + 3ix^2$. The function $f$ is not defined at the point $z = 0$ of $C$ (where $y = 0$), but $f[z(x)]$ is $1$ for $x < 0$ and $4x^3$ for $x > 0$, which has one-sided limits at $0$; so $f$ is piecewise continuous on $C$, and
>
> $$
> \int_C f(z)\,dz = \int_{-1}^{0} 1\cdot(1 + 3ix^2)\,dx + \int_0^1 4x^3(1 + 3ix^2)\,dx = \big[x + ix^3\big]_{-1}^{0} + \big[x^4 + 2ix^6\big]_0^1 = (1 + i) + (1 + 2i) = 2 + 3i .
> $$
>
> *B&C: Sec. 46, Exercise 4; Source: 342 HW 5*

^ex-44-3

> [!example] Example §44.4: Integrands That Agree on the Contour
> **(a)** Use the definition of contour integrals to prove
>
> $$
> \int_C e^{\bar z}\,dz = \int_C e^{4/z}\,dz , \qquad C: |z| = 2 \text{ counterclockwise.}
> $$
>
> With $z = 2e^{i\theta}$ $(0 \le \theta \le 2\pi)$ we have $\bar z = 2e^{-i\theta}$ and $4/z = 4/(2e^{i\theta}) = 2e^{-i\theta}$: the two exponents agree at every point of $C$. By (2) both integrals equal
>
> $$
> \int_0^{2\pi} e^{2e^{-i\theta}}\,2ie^{i\theta}\,d\theta .
> $$
>
> **(b)** In the same way, $\int_C \sin(\bar z)\,dz = \int_C \sin(1/z)\,dz$ when $C$ is $|z| = 1$ counterclockwise, since $\bar z = e^{-i\theta} = 1/z$ on $C$; both equal $\int_0^{2\pi}\sin(e^{-i\theta})\,ie^{i\theta}\,d\theta$.
>
> A contour integral sees only the values of the integrand on $C$. The functions $e^{\bar z}$ and $\sin\bar z$ are nowhere analytic, but on $C$ they coincide with $e^{4/z}$ and $\sin(1/z)$, which are analytic except at $0$; that is why the exams then evaluate the integrals by residues ([[§76 Cauchy's Residue Theorem#^thm-76-1|Theorem §76.1]]), as $2\pi i\operatorname{Res}_{z=0}e^{4/z} = 8\pi i$ and $2\pi i\operatorname{Res}_{z=0}\sin(1/z) = 2\pi i$; the Laurent series and residues asked for in the remaining parts of these problems are worked in [[§68 Examples (Proof of Laurent's Theorem)#^ex-68-4|Example §68.4]](c).
>
> **(c)** The values also follow from the definition directly. With the series $e^w = \sum_{n \ge 0} w^n/n!$ ([[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]]),
>
> $$
> e^{2e^{-i\theta}}\,2ie^{i\theta} = \sum_{n=0}^{\infty}\frac{2^{n+1}i}{n!}\,e^{i\theta}e^{-in\theta} .
> $$
>
> The $n$th term has modulus $2^{n+1}/n!$, and $\sum 2^{n+1}/n!$ converges, so by the M-test the series converges uniformly in $\theta$ and may be integrated term by term (real and imaginary parts separately). By [[§42 Definite Integrals of Functions w(t)#^ex-42-4|Example §42.4]] only the term $n = 1$ survives:
>
> $$
> \int_C e^{\bar z}\,dz = \frac{2^2i}{1!}\cdot2\pi = 8\pi i .
> $$
>
> Likewise $\sin(e^{-i\theta})\,ie^{i\theta} = \sum_{k \ge 0}\frac{(-1)^k i}{(2k+1)!}e^{i\theta}e^{-i(2k+1)\theta}$, and only $k = 0$ survives: $\int_C \sin\bar z\,dz = 2\pi i$. (Numerical quadrature: $25.1327i = 8\pi i$ and $6.2832i = 2\pi i$.)
>
> *Source: 342 practice final (Fall 2002), Q5; 342 practice final (Spring 2005), Q5*

^ex-44-4

> [!remark]- Connections
> - The term-by-term integration in (c) uses the M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], and the integration of uniform limits, [[§33 Properties of the Riemann Integral#^thm-33-12|451 Thm. §33.12]]; in complex form it is computing the $n = 1$ Fourier coefficient of $\theta \mapsto e^{2e^{-i\theta}}$, as in [[§15★ Complex Methods#^thm-15-1|341 Thm. §15.1]].
