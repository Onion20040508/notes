---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 92
bc: "92"
aliases: ["B&C 92"]
tags: [complex-variables, math342, extension]
---
← [[§91★ Integration Along a Branch Cut]] · ↑ [[· 7 Applications of Residues]] · [[§93 Argument Principle]] →

*Brown–Churchill, Section 92 · MAT 342 Practice Finals (Spring 2012, Spring 2005, Fall 2002, Fall 2009, Fall 1999).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A definite integral over a full period, $\int_0^{2\pi} F(\sin\theta, \cos\theta)\,d\theta$, is a contour integral in disguise: with $z = e^{i\theta}$ the point $z$ runs once around the unit circle, $\sin\theta$ and $\cos\theta$ become rational functions of $z$, and $d\theta = dz/(iz)$. When $F$ is rational the new integrand is rational, and the residue theorem evaluates the integral from the poles inside the unit circle; no improper integrals and no estimates at infinity are involved. Although the section was optional in the course, every old final contains one such integral.

## The Substitution z = e^{iθ}

Let $C$ be the positively oriented unit circle

$$
z = e^{i\theta} \qquad (0 \le \theta \le 2\pi) . \qquad (2)
$$

By the differentiation formula of [[§41 Derivatives of Functions w(t)|§41]], $dz/d\theta = ie^{i\theta} = iz$, and ([[§37 The Trigonometric Functions sin z and cos z|§37]]) $\sin\theta = (e^{i\theta} - e^{-i\theta})/2i$, $\cos\theta = (e^{i\theta} + e^{-i\theta})/2$. These suggest the substitutions

$$
\sin\theta = \frac{z - z^{-1}}{2i}, \qquad \cos\theta = \frac{z + z^{-1}}{2}, \qquad d\theta = \frac{dz}{iz} , \qquad (3)
$$

and, for integral multiples of $\theta$, since $e^{in\theta} = z^n$,

$$
\cos n\theta = \frac{z^n + z^{-n}}{2}, \qquad \sin n\theta = \frac{z^n - z^{-n}}{2i} . \qquad (7)
$$

> [!theorem] Proposition §92.1: A Trigonometric Integral as a Contour Integral
> Let $F(s, c)$ be a function for which $\theta \mapsto F(\sin\theta, \cos\theta)$ is continuous on $0 \le \theta \le 2\pi$. Then
>
> $$
> \int_0^{2\pi} F(\sin\theta, \cos\theta)\,d\theta = \int_C F\Big(\frac{z - z^{-1}}{2i}, \frac{z + z^{-1}}{2}\Big)\frac{dz}{iz} , \qquad (1),\ (4)
> $$
>
> where $C$ is the positively oriented unit circle. When the integrand on the right is a rational function of $z$ with no poles on $C$, the integral equals $2\pi i$ times the sum of its residues inside $C$.
>
> *B&C: Sec. 92 (text), equations (1)–(4)*

^prop-92-1

> [!proof]+ Proof
> Write $G(z)$ for the integrand on the right. By the definition of the contour integral with the parametrization (2) ([[§44 Contour Integrals|§44]]), $\int_C G(z)\,dz = \int_0^{2\pi} G(e^{i\theta})\,ie^{i\theta}\,d\theta$. At $z = e^{i\theta}$, $z^{-1} = e^{-i\theta}$, so $\frac{z - z^{-1}}{2i} = \sin\theta$, $\frac{z + z^{-1}}{2} = \cos\theta$, and $\frac{1}{iz}\cdot ie^{i\theta} = 1$; hence $G(e^{i\theta})ie^{i\theta} = F(\sin\theta, \cos\theta)$, which is (1) = (4): the original integral is a parametric form of the contour integral. The last statement is Cauchy's residue theorem ([[§76 Cauchy's Residue Theorem|§76]]), since a rational function has finitely many poles.

^pf-92-1

*Uses:* [[§44 Contour Integrals|§44]], [[§76 Cauchy's Residue Theorem|§76]] (Theorem), [[§37 The Trigonometric Functions sin z and cos z|§37]]

> [!remark] Remark: Method — Integrals over a Period
> To evaluate $\int_0^{2\pi} F(\sin\theta, \cos\theta)\,d\theta$ with $F$ rational:
> 1. **Substitute** (3), and (7) for multiples of $\theta$; multiply out to a single rational function of $z$, clearing $z^{-1}$ by multiplying numerator and denominator by a power of $z$.
> 2. **Find the poles** (zeros of the denominator), and check that none lies on $|z| = 1$. For a quadratic $z^2 + bz + c$ the product of the roots is $c$: if $|c| = 1$ and one root is outside the circle, the other is inside.
> 3. **Residues** at the poles inside $|z| < 1$ only, including $z = 0$ if a power of $z$ is left in the denominator.
> 4. **Multiply** by $2\pi i$. The result must be real for a real integrand.
>
> For $\int_0^{\pi}$ or $\int_{-\pi}^{\pi}$, first use symmetry or periodicity to pass to a full period $[0, 2\pi]$.

^rem-92-1

## Examples

> [!example] Example §92.1: The Integral of 1/(1 + a sin θ)
> Show that
>
> $$
> \int_0^{2\pi}\frac{d\theta}{1 + a\sin\theta} = \frac{2\pi}{\sqrt{1 - a^2}} \qquad (-1 < a < 1) . \qquad (5)
> $$
>
> For $a = 0$ this is clear; let $a \ne 0$. With (3),
>
> $$
> \frac{1}{1 + a\,\frac{z - z^{-1}}{2i}}\cdot\frac{1}{iz} = \frac{2iz}{az^2 + 2iz - a}\cdot\frac{1}{iz} = \frac{2}{az^2 + 2iz - a} = \frac{2/a}{z^2 + (2i/a)z - 1} ,
> $$
>
> so the integral is $\int_C\frac{2/a}{z^2 + (2i/a)z - 1}\,dz$ (6). By the quadratic formula the denominator has the pure imaginary zeros
>
> $$
> z_1 = \Big(\frac{-1 + \sqrt{1 - a^2}}{a}\Big)i, \qquad z_2 = \Big(\frac{-1 - \sqrt{1 - a^2}}{a}\Big)i .
> $$
>
> Because $|a| < 1$, $|z_2| = \frac{1 + \sqrt{1 - a^2}}{|a|} > 1$; and $|z_1z_2| = 1$ (the constant term), so $|z_1| < 1$. There are no singular points on $C$, and only $z_1$ is inside. With $f(z) = \frac{2/a}{(z - z_1)(z - z_2)} = \frac{\phi(z)}{z - z_1}$, $\phi(z) = \frac{2/a}{z - z_2}$, the point $z_1$ is a simple pole and
>
> $$
> B_1 = \phi(z_1) = \frac{2/a}{z_1 - z_2} = \frac{2/a}{2i\sqrt{1 - a^2}/a} = \frac{1}{i\sqrt{1 - a^2}} .
> $$
>
> Hence $\int_C f(z)\,dz = 2\pi iB_1 = \frac{2\pi}{\sqrt{1 - a^2}}$, which is (5). (For $a = \frac12$: $7.255197$, as quadrature confirms.) B&C's Exercise 4, $\int_0^{2\pi}\frac{d\theta}{1 + a\cos\theta} = \frac{2\pi}{\sqrt{1 - a^2}}$, follows the same way, or from (5) by the substitution $\theta \mapsto \theta + \pi/2$, which turns $\cos\theta$ into $-\sin\theta$ and does not change an integral over a full period.
>
> *B&C: Sec. 92, Example 1*

^ex-92-1

> [!example] Example §92.2: A Cosine of a Multiple Angle
> Show that
>
> $$
> \int_0^{\pi}\frac{\cos2\theta\,d\theta}{1 - 2a\cos\theta + a^2} = \frac{a^2\pi}{1 - a^2} \qquad (-1 < a < 1) . \qquad (8)
> $$
>
> For $a = 0$ both sides are $0$; let $a \ne 0$. Since $\cos(2\pi - \theta) = \cos\theta$ and $\cos2(2\pi - \theta) = \cos2\theta$, the graph of the integrand on $[0, 2\pi]$ is symmetric about $\theta = \pi$, and the integral over $[0, \pi]$ is half the integral over $[0, 2\pi]$. With (3) and (7),
>
> $$
> 1 - 2a\cos\theta + a^2 = 1 - a(z + z^{-1}) + a^2 = \frac{(z - a)(1 - az)}{z} = -\frac{(z - a)(az - 1)}{z}, \qquad \cos2\theta = \frac{z^4 + 1}{2z^2} ,
> $$
>
> so
>
> $$
> \int_0^{\pi}\frac{\cos2\theta\,d\theta}{1 - 2a\cos\theta + a^2} = \frac12\int_C\frac{z^4 + 1}{2z^2}\cdot\frac{-z}{(z - a)(az - 1)}\cdot\frac{dz}{iz} = \frac i4\int_C\frac{z^4 + 1}{(z - a)(az - 1)z^2}\,dz ,
> $$
>
> using $-\frac{1}{4i} = \frac i4$. The singular points inside $C$ are $a$ and $0$; the point $1/a$ is outside since $|a| < 1$. So
>
> $$
> \int_0^{\pi}\frac{\cos2\theta\,d\theta}{1 - 2a\cos\theta + a^2} = \frac i4\cdot2\pi i(B_1 + B_2) , \qquad (9)
> $$
>
> with $B_1$, $B_2$ the residues of $f(z) = \frac{z^4 + 1}{(z - a)(az - 1)z^2}$ at $a$ and $0$.
>
> **At $a$** (simple pole), $f = \phi/(z - a)$ with $\phi(z) = \frac{z^4 + 1}{(az - 1)z^2}$:
>
> $$
> B_1 = \phi(a) = \frac{a^4 + 1}{(a^2 - 1)a^2} . \qquad (10)
> $$
>
> **At $0$** (pole of order $2$), $f = \phi/z^2$ with $\phi(z) = \frac{z^4 + 1}{(z - a)(az - 1)}$, and $B_2 = \phi'(0)$. Since $(z - a)(az - 1) = az^2 - (1 + a^2)z + a$ equals $a$ at $0$ with derivative $-(1 + a^2)$ there, and the numerator $z^4 + 1$ has derivative $0$ at $0$,
>
> $$
> B_2 = \phi'(0) = \frac{0\cdot a - 1\cdot\big(-(1 + a^2)\big)}{a^2} = \frac{a^2 + 1}{a^2} . \qquad (11)
> $$
>
> **Sum.** $B_1 + B_2 = \frac{a^4 + 1 + (a^2 + 1)(a^2 - 1)}{(a^2 - 1)a^2} = \frac{2a^4}{(a^2 - 1)a^2} = \frac{2a^2}{a^2 - 1}$, and (9) gives $\frac i4\cdot2\pi i\cdot\frac{2a^2}{a^2 - 1} = -\pi\,\frac{a^2}{a^2 - 1} = \frac{a^2\pi}{1 - a^2}$, which is (8). (For $a = \frac12$: $\frac\pi3$, as quadrature confirms.)
>
> *B&C: Sec. 92, Example 2*

^ex-92-2

> [!remark]- Connections
> - The denominator $1 - 2a\cos\theta + a^2$ is that of the Poisson kernel, [[§39 Potential in a Disk#^thm-39-3|341 Thm. §39.3]] with $a = r/c$. In 341 the kernel is $\frac{1 - a^2}{1 - 2a\cos\psi + a^2} = 1 + 2\sum_{n\ge1}a^n\cos n\psi$, and (8) reads off its Fourier coefficient: $\frac1\pi\int_{-\pi}^{\pi}\frac{1 - a^2}{1 - 2a\cos\theta + a^2}\cos2\theta\,d\theta = 2a^2$. With $\cos2\theta$ replaced by $1$, the same computation gives $\int_0^{2\pi}\frac{d\theta}{1 - 2a\cos\theta + a^2} = \frac{2\pi}{1 - a^2}$, the statement that the Poisson kernel has average $1$, [[§39 Potential in a Disk#^rem-39-2|341 Remark: The Poisson Kernel Is a Weight]].

> [!example] Example §92.3: The Integral of 1/(5 + 4 sin θ)
> Evaluate $\displaystyle\int_0^{2\pi}\frac{d\theta}{5 + 4\sin\theta}$.
>
> With (3), $5 + 4\cdot\frac{z - z^{-1}}{2i} = \frac{10iz + 4z^2 - 4}{2iz}$, so
>
> $$
> \int_0^{2\pi}\frac{d\theta}{5 + 4\sin\theta} = \int_C\frac{2iz}{4z^2 + 10iz - 4}\cdot\frac{dz}{iz} = \int_C\frac{dz}{2z^2 + 5iz - 2} .
> $$
>
> The zeros of $2z^2 + 5iz - 2$ are $\frac{-5i \pm \sqrt{-25 + 16}}{4} = \frac{-5i \pm 3i}{4}$, that is $-\frac i2$ and $-2i$; only $-\frac i2$ is inside $C$. Its residue is $\frac{1}{4z + 5i}\big|_{z=-i/2} = \frac{1}{3i}$, and the integral is $2\pi i\cdot\frac{1}{3i} = \frac{2\pi}{3}$. This is (5) with $a = \frac45$: $\frac15\cdot\frac{2\pi}{\sqrt{1 - 16/25}} = \frac15\cdot\frac{2\pi}{3/5}$. The Fall 2002 key is the same computation.
>
> *B&C: Sec. 92, Exercise 1; Source: 342 practice final (Fall 2002), Q6, 342 practice final (Fall 2009), Q6*

^ex-92-3

> [!example] Example §92.4: The Integral of 1/(2 + cos θ)
> Evaluate $\displaystyle\int_0^{2\pi}\frac{d\theta}{2 + \cos\theta}$.
>
> With (3), $2 + \frac{z + z^{-1}}{2} = \frac{z^2 + 4z + 1}{2z}$, so the integral is $\int_C\frac{2z}{z^2 + 4z + 1}\cdot\frac{dz}{iz} = -2i\int_C\frac{dz}{z^2 + 4z + 1}$. The zeros are $-2 \pm \sqrt3$; their product is $1$, and $-2 - \sqrt3$ is outside the circle, so $-2 + \sqrt3$ is inside. Its residue is $\frac{1}{2z + 4}\big|_{z=-2+\sqrt3} = \frac{1}{2\sqrt3}$, and
>
> $$
> \int_0^{2\pi}\frac{d\theta}{2 + \cos\theta} = -2i\cdot2\pi i\cdot\frac{1}{2\sqrt3} = \frac{2\pi}{\sqrt3} \approx 3.627599 ,
> $$
>
> in agreement with B&C's Exercise 4 ($a = \frac12$: $\frac12\cdot\frac{2\pi}{\sqrt{3/4}}$) and with quadrature. The Spring 2005 key reaches the same value by the same route.
>
> *B&C: Sec. 92, Exercise 4; Source: 342 practice final (Spring 2005), Q6, 342 practice final (Fall 1999), Q4*

^ex-92-4

> [!example] Example §92.5: The Integral of 1/(1 + sin²θ)
> Prove that, with $C$ the unit circle oriented counterclockwise,
>
> $$
> \int_{-\pi}^{\pi}\frac{d\theta}{1 + \sin^2\theta} = \int_C\frac{4iz}{z^4 - 6z^2 + 1}\,dz = \sqrt2\,\pi .
> $$
>
> **The first equality.** The integrand has period $2\pi$, so the integral over $[-\pi, \pi]$ equals that over $[0, 2\pi]$. With (3), $\sin^2\theta = \frac{(z - z^{-1})^2}{-4} = -\frac{(z^2 - 1)^2}{4z^2}$, so
>
> $$
> \frac{1}{1 + \sin^2\theta}\cdot\frac{1}{iz} = \frac{4z^2}{4z^2 - (z^2 - 1)^2}\cdot\frac{1}{iz} = \frac{4z}{i(-z^4 + 6z^2 - 1)} = \frac{4iz}{z^4 - 6z^2 + 1} .
> $$
>
> **Poles.** With $w = z^2$, $w^2 - 6w + 1 = 0$ gives $w = 3 \pm \sqrt8$. Since $3 - \sqrt8 = (\sqrt2 - 1)^2 < 1$ and $3 + \sqrt8 > 1$, the zeros inside $C$ are $z = \pm\sqrt{3 - \sqrt8} = \pm(\sqrt2 - 1)$, both simple.
>
> **Residues.** At each of them, by [[§83 Zeros and Poles|§83]] (Theorem 2),
>
> $$
> \operatorname{Res}\frac{4iz}{z^4 - 6z^2 + 1} = \frac{4iz}{4z^3 - 12z} = \frac{i}{z^2 - 3} = \frac{i}{(3 - \sqrt8) - 3} = -\frac{i}{2\sqrt2} .
> $$
>
> **Conclusion.** $2\pi i\cdot\Big(-\frac{2i}{2\sqrt2}\Big) = \frac{2\pi}{\sqrt2} = \sqrt2\,\pi \approx 4.442883$, as quadrature confirms. The key is the same computation.
>
> *B&C: Sec. 92, Exercise 2; Source: 342 practice final (Spring 2012), Q3*

^ex-92-5
