---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 45
bc: "45"
aliases: ["B&C 45"]
tags: [complex-variables, math342]
---
← [[§44 Contour Integrals]] · ↑ [[· 4 Integrals]] · [[§46 Examples Involving Branch Cuts]] →

*Brown–Churchill, Section 45 · MAT 342 HW 5.*

This section evaluates contour integrals straight from the definition $\int_C f(z)\,dz = \int_a^b f[z(t)]z'(t)\,dt$ and draws the lessons. The integral of $1/z$ from $1$ to $-1$ is $\pi i$ along the upper half of the unit circle and $-\pi i$ along the lower half, so around the whole circle it is $2\pi i$; the integral of $z$ from $z_1$ to $z_2$ is $\frac12(z_2^2 - z_1^2)$ along *every* contour; and a non-analytic polynomial in $x$ and $y$ gives different values along two paths with the same endpoints. Which of these behaviors occurs is explained by antiderivatives ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]) and by the Cauchy–Goursat theorem ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]). The integral $\int_C dz/z = 2\pi i$ around a circle, computed here, is the seed of the Cauchy integral formula and of residues.

## Three Examples

> [!example] Example §45.1: The Integral of 1/z Along the Two Halves of the Unit Circle
> Let $C_1$ be the top half $z = e^{i\theta}$ $(0 \le \theta \le \pi)$ of the circle $|z| = 1$, from $z = 1$ to $z = -1$. By definition (2) of [[§44 Contour Integrals#^def-44-1|§44]],
>
> $$
> \int_{C_1}\frac{dz}{z} = \int_0^{\pi}\frac{1}{e^{i\theta}}\,ie^{i\theta}\,d\theta = i\int_0^{\pi}d\theta = \pi i . \qquad (1)
> $$
>
> Let $C_2$ be the *bottom* half of the same circle, also from $z = 1$ to $z = -1$. The representation $z = e^{i\theta}$ $(\pi \le \theta \le 2\pi)$ runs from $-1$ to $1$, so it represents $-C_2$, and by property (6) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]]
>
> $$
> \int_{C_2}\frac{dz}{z} = -\int_{-C_2}\frac{dz}{z} = -\int_{\pi}^{2\pi}\frac{1}{e^{i\theta}}\,ie^{i\theta}\,d\theta = -i\int_{\pi}^{2\pi}d\theta = -\pi i . \qquad (2)
> $$
>
> The values of (1) and (2) are not the same. If $C$ is the closed curve $C = C_1 - C_2$, the whole circle counterclockwise, then
>
> $$
> \int_C\frac{dz}{z} = \int_{C_1}\frac{dz}{z} - \int_{C_2}\frac{dz}{z} = \pi i - (-\pi i) = 2\pi i . \qquad (3)
> $$
>
> *B&C: Sec. 45, Example 1*

^ex-45-1

> [!example] Example §45.2: The Integral of z Depends Only on the Endpoints
> Let $C$ be an arbitrary smooth arc $z = z(t)$ $(a \le t \le b)$ from a fixed point $z_1$ to a fixed point $z_2$. To evaluate
>
> $$
> \int_C z\,dz = \int_a^b z(t)z'(t)\,dt ,
> $$
>
> note that by [[§41 Derivatives of Functions w(t)#^ex-41-1|Example §41.1]], $\frac{d}{dt}\frac{[z(t)]^2}{2} = z(t)z'(t)$. Since $z(a) = z_1$ and $z(b) = z_2$, the fundamental theorem of calculus for $w(t)$ ([[§42 Definite Integrals of Functions w(t)#^thm-42-2|Theorem §42.2]]) gives
>
> $$
> \int_C z\,dz = \frac{[z(t)]^2}{2}\bigg]_a^b = \frac{[z(b)]^2 - [z(a)]^2}{2} = \frac{z_2^2 - z_1^2}{2} .
> $$
>
> Since the value depends only on the endpoints, we may write
>
> $$
> \int_{z_1}^{z_2} z\,dz = \frac{z_2^2 - z_1^2}{2} . \qquad (4)
> $$
>
> Expression (4) is also valid when $C$ is a contour that is not smooth: if $C$ consists of smooth arcs $C_k$ $(k = 1, \ldots, n)$ joined end to end, with $C_k$ from $z_k$ to $z_{k+1}$, then by property (7) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]]
>
> $$
> \int_C z\,dz = \sum_{k=1}^{n}\int_{C_k} z\,dz = \sum_{k=1}^{n}\int_{z_k}^{z_{k+1}} z\,dz = \sum_{k=1}^{n}\frac{z_{k+1}^2 - z_k^2}{2} = \frac{z_{n+1}^2 - z_1^2}{2} , \qquad (5)
> $$
>
> where the sum has telescoped; $z_1$ is the initial point of $C$ and $z_{n+1}$ its final point. In particular $\int_C z\,dz = 0$ around every closed contour.
>
> *B&C: Sec. 45, Example 2*

^ex-45-2

The same argument with the constant function $1$ in place of $z$ gives a fact that the proof in [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49]] relies on.

> [!theorem] Proposition §45.1: The Integral of 1 Along a Contour
> If $C$ is any contour from a point $z_1$ to a point $z_2$, then
>
> $$
> \int_C dz = z_2 - z_1 .
> $$
>
> *B&C: Sec. 46, Exercise 5*

^prop-45-1

> [!proof]+ Proof
> Let $C$ be $z = z(t)$ $(a \le t \le b)$, made of smooth arcs $C_k$ on $t_{k-1} \le t \le t_k$ $(k = 1, \ldots, n)$, with $a = t_0 < \cdots < t_n = b$. On each piece $z'$ is continuous and $z$ is an antiderivative of $z'$, so by [[§42 Definite Integrals of Functions w(t)#^thm-42-2|Theorem §42.2]]
>
> $$
> \int_{C_k} dz = \int_{t_{k-1}}^{t_k} z'(t)\,dt = z(t_k) - z(t_{k-1}) .
> $$
>
> By property (7) of [[§44 Contour Integrals#^thm-44-2|Theorem §44.2]] the integral over $C$ is the sum of these, which telescopes to $z(b) - z(a) = z_2 - z_1$.

^pf-45-1

*Uses:* [[§44 Contour Integrals#^def-44-1|Def. §44.1]], [[§42 Definite Integrals of Functions w(t)#^thm-42-2|§42.2]], [[§44 Contour Integrals#^thm-44-2|§44.2]]

If $f(z)$ is given as $u(x, y) + iv(x, y)$, it is sometimes convenient to use one of the variables $x$, $y$ as the parameter.

> [!example] Example §45.3: Two Paths, Two Values
> Let $f(z) = y - x - i3x^2$ $(z = x + iy)$. Let $C_1$ be the polygonal line $OAB$ from $O = 0$ up to $A = i$ and then across to $B = 1 + i$, and $C_2$ the segment $OB$ of the line $y = x$. Evaluate $I_1 = \int_{C_1} f(z)\,dz$ and $I_2 = \int_{C_2} f(z)\,dz$.
>
> **Along $C_1$.** By property (7),
>
> $$
> I_1 = \int_{C_1} f(z)\,dz = \int_{OA} f(z)\,dz + \int_{AB} f(z)\,dz . \qquad (6)
> $$
>
> The leg $OA$ is $z = 0 + iy$ $(0 \le y \le 1)$; since $x = 0$ there, $f(z) = y$ and $dz = i\,dy$:
>
> $$
> \int_{OA} f(z)\,dz = \int_0^1 y\,i\,dy = i\int_0^1 y\,dy = \frac i2 .
> $$
>
> On the leg $AB$, $z = x + i$ $(0 \le x \le 1)$; since $y = 1$, $f(z) = 1 - x - i3x^2$ and $dz = dx$:
>
> $$
> \int_{AB} f(z)\,dz = \int_0^1 (1 - x - i3x^2)\,dx = \int_0^1 (1 - x)\,dx - 3i\int_0^1 x^2\,dx = \frac12 - i .
> $$
>
> Hence
>
> $$
> I_1 = \frac{1 - i}{2} . \qquad (7)
> $$
>
> **Along $C_2$.** Here $z = x + ix$ $(0 \le x \le 1)$; since $y = x$, $f(z) = -i3x^2$ and $dz = (1 + i)\,dx$:
>
> $$
> I_2 = \int_0^1 -i3x^2(1 + i)\,dx = 3(1 - i)\int_0^1 x^2\,dx = 1 - i .
> $$
>
> The integrals along $C_1$ and $C_2$ have *different values* although the two paths have the same initial and final points. Consequently the integral of $f$ over the simple closed contour $OABO$, that is $C_1 - C_2$, has the *nonzero* value
>
> $$
> I_1 - I_2 = \frac{-1 + i}{2} .
> $$
>
> [[§50 Cauchy–Goursat Theorem#^ex-50-3|Example §50.3]] recovers this number from Green's theorem ([[§130 Green's Theorem#^thm-130-1|Calc Thm. §130.1]]).
>
> *B&C: Sec. 45, Example 3*

^ex-45-3

> [!remark] Remark: What the Examples Show
> **(a)** The value of a contour integral of a given function from one fixed point to another might be independent of the path taken ([[§45 Some Examples (Contour Integrals)#^ex-45-2|Example §45.2]]), but that is not always the case (Examples §45.1 and §45.3).
>
> **(b)** Contour integrals of a given function around every closed contour might all be zero (Example §45.2), but that is not always the case (Examples §45.1 and §45.3).
>
> When integrals are independent of path, or vanish around closed paths, is the subject of [[§48 Antiderivatives|§48]] (antiderivatives), [[§50 Cauchy–Goursat Theorem|§50]] and [[§52 Simply Connected Domains|§52]]. In Example §45.3, $f$ is analytic nowhere; in Example §45.1, $1/z$ is analytic except at $0$, which is enclosed by the circle; in Example §45.2, $z$ is entire.

^rem-45-1

> [!remark]- Connections
> - The same dichotomy for real vector fields: a line integral is independent of path exactly when it vanishes around every closed path, [[§128 The Fundamental Theorem for Line Integrals#^thm-128-2|Calc Thm. §128.2]]; the complex version is [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]].

> [!remark] Remark: Method — Evaluating a Contour Integral by Parametrization
> 1. **Split** $C$ into smooth pieces (segments, arcs of circles) and parametrize each: a segment from $p$ to $q$ as $z = p + (q - p)t$ $(0 \le t \le 1)$; an arc of the circle $|z - z_0| = R$ as $z = z_0 + Re^{i\theta}$; a graph $y = g(x)$ as $z = x + ig(x)$.
> 2. **Substitute.** Compute $z'(t)$ and $f[z(t)]$, and simplify using the parametrization: on $|z - z_0| = R$, $z - z_0 = Re^{i\theta}$ and $\overline{z - z_0} = R^2/(z - z_0)$; on a horizontal segment $y$ is constant.
> 3. **Integrate** $f[z(t)]z'(t)$ over the parameter interval, either as real part $+ i\,$imaginary part or with an antiderivative of $w(t)$ such as $e^{ik\theta}/(ik)$ ([[§42 Definite Integrals of Functions w(t)#^thm-42-2|Theorem §42.2]]).
> 4. **Orientation.** If a parametrization runs the wrong way, it represents $-C$: change the sign (property (6)). Add the pieces (property (7)).
>
> This works for every piecewise continuous $f$, analytic or not. For analytic integrands, antiderivatives ([[§48 Antiderivatives#^rem-48-1|§48]]) and the Cauchy–Goursat theorem are usually faster.

^rem-45-2

## Course Examples

> [!example] Example §45.4: (z + 2)/z Along Half Circles and the Whole Circle
> Let $f(z) = (z + 2)/z$, and let $C$ be **(a)** the semicircle $z = 2e^{i\theta}$ $(0 \le \theta \le \pi)$; **(b)** the semicircle $z = 2e^{i\theta}$ $(\pi \le \theta \le 2\pi)$; **(c)** the circle $z = 2e^{i\theta}$ $(0 \le \theta \le 2\pi)$.
>
> With $z = 2e^{i\theta}$, $z' = 2ie^{i\theta}$ and
>
> $$
> f[z(\theta)]\,z'(\theta) = \frac{2e^{i\theta} + 2}{2e^{i\theta}}\,2ie^{i\theta} = 2i\big(e^{i\theta} + 1\big) ,
> $$
>
> whose antiderivative is $2e^{i\theta} + 2i\theta$. Hence
>
> $$
> \text{(a)}\ \Big[2e^{i\theta} + 2i\theta\Big]_0^{\pi} = 2(-1 - 1) + 2\pi i = -4 + 2\pi i, \qquad \text{(b)}\ \Big[2e^{i\theta} + 2i\theta\Big]_{\pi}^{2\pi} = 2(1 + 1) + 2\pi i = 4 + 2\pi i ,
> $$
>
> and **(c)** is their sum, $4\pi i$. Reading $f = 1 + 2/z$ explains the numbers: the term $1$ contributes $z_2 - z_1$ ([[§45 Some Examples (Contour Integrals)#^prop-45-1|Proposition §45.1]]), that is $-4$, $4$ and $0$; the term $2/z$ contributes $2\pi i$ along each half circle, as in Example §45.1 (where the radius does not matter).
>
> *B&C: Sec. 46, Exercise 1; Source: 342 HW 5*

^ex-45-4

> [!example] Example §45.5: Powers of z − a Around a Circle
> Let $C$ be the circle of radius $R$ centered at $a$, $z = a + Re^{it}$ $(-\pi \le t \le \pi)$. For every integer $n$,
>
> $$
> \int_C (z - a)^n\,dz = \begin{cases} 0 & \text{when } n \ne -1, \\ 2\pi i & \text{when } n = -1. \end{cases}
> $$
>
> On $C$, $(z - a)^n = R^ne^{int}$ and $z' = iRe^{it}$, so the integrand of (2) is $iR^{n+1}e^{i(n+1)t}$.
>
> **$n \ne -1$.** An antiderivative is $R^{n+1}e^{i(n+1)t}/(n + 1)$, and
>
> $$
> \int_C (z - a)^n\,dz = \frac{R^{n+1}}{n + 1}\Big(e^{i(n+1)\pi} - e^{-i(n+1)\pi}\Big) = \frac{R^{n+1}}{n + 1}\,2i\sin\big((n + 1)\pi\big) = 0 .
> $$
>
> **$n = -1$.** The integrand is the constant $i$, and the integral is $\int_{-\pi}^{\pi} i\,dt = 2\pi i$.
>
> The answer depends neither on $R$ nor on $a$. B&C's Exercise 13 states the same result with $n - 1$ in place of $n$: $\int_C (z - z_0)^{n-1}\,dz$ is $0$ for $n = \pm1, \pm2, \ldots$ and $2\pi i$ for $n = 0$. For contours other than circles, see [[§49 Proof of the Theorem (Antiderivatives)#^ex-49-1|Example §49.1]].
>
> *B&C: Sec. 46, Exercise 13; Source: 342 HW 5, Problem 2(a)*

^ex-45-5
