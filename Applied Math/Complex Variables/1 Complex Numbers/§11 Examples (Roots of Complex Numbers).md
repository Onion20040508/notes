---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 11
bc: "11"
aliases: ["B&C 11"]
tags: [complex-variables, math342]
---
← [[§10 Roots of Complex Numbers]] · ↑ [[· 1 Complex Numbers]] · [[§12★ Regions in the Complex Plane]] →

*Brown–Churchill, Section 11.*

This section works the [[§10 Roots of Complex Numbers#^rem-10-1|method of §10]] on the standard cases: the roots of a negative real number, the $n$th roots of unity, and the square roots of a number $a + i$, where half-angle formulas turn the exponential answer into a closed formula in radicals. The roots of unity are the building blocks: every set of $n$th roots is one root times the $n$th roots of unity, and their sum is zero. Two exercises then put roots to work: the quadratic formula holds verbatim over $\mathbb{C}$, and the roots of $z^4 + 4$ factor it into real quadratics.

> [!example] Example §11.1: The Fourth Roots of −16
> Find all four values of $(-16)^{1/4}$.
>
> Write $-16 = 16\exp[i(\pi + 2k\pi)]$ $(k = 0, \pm1, \ldots)$. Since $\sqrt[4]{16} = 2$, the roots are
>
> $$
> c_k = 2\exp\Big[i\Big(\frac\pi4 + \frac{k\pi}{2}\Big)\Big] \qquad (k = 0, 1, 2, 3) . \qquad (1)
> $$
>
> They lie at the vertices of a square inscribed in the circle $|z| = 2$, equally spaced around it starting with the principal root
>
> $$
> c_0 = 2\exp\Big[i\Big(\frac\pi4\Big)\Big] = 2\Big(\cos\frac\pi4 + i\sin\frac\pi4\Big) = 2\Big(\frac{1}{\sqrt2} + \frac{i}{\sqrt2}\Big) = \sqrt2(1 + i) .
> $$
>
> Without any further calculation, rotating by quarter turns,
>
> $$
> c_1 = \sqrt2(-1 + i), \qquad c_2 = \sqrt2(-1 - i), \qquad c_3 = \sqrt2(1 - i) .
> $$
>
> By (2) and (4) of [[§10 Roots of Complex Numbers#^prop-10-3|Proposition §10.3]] these are $c_0$, $c_0\omega_4$, $c_0\omega_4^2$, $c_0\omega_4^3$, where $\omega_4 = \exp(i\frac\pi2) = i$: multiplying by $i$ is the quarter turn. Check: $c_0^2 = 2(1 + i)^2 = 4i$ and $c_0^4 = (4i)^2 = -16$.
>
> *B&C: Sec. 11, Example 1*

^ex-11-1

> [!example] Example §11.2: The nth Roots of Unity
> Determine the $n$th roots of unity, and show that if $c$ is any $n$th root of unity other than $1$, then $1 + c + c^2 + \cdots + c^{n-1} = 0$.
>
> **The roots.** Starting with $1 = 1\exp[i(0 + 2k\pi)]$ $(k = 0, \pm1, \ldots)$,
>
> $$
> c_k = \sqrt[n]{1}\exp\Big[i\Big(\frac0n + \frac{2k\pi}{n}\Big)\Big] = \exp\Big(i\frac{2k\pi}{n}\Big) \qquad (k = 0, 1, 2, \ldots, n - 1) . \qquad (2)
> $$
>
> When $n = 2$ these are $\pm1$. When $n \ge 3$ they lie at the vertices of a regular polygon inscribed in the unit circle $|z| = 1$, with one vertex at the principal root $z = 1$ ($k = 0$). By (3) of [[§10 Roots of Complex Numbers#^prop-10-3|Proposition §10.3]] they are simply
>
> $$
> 1, \ \omega_n, \ \omega_n^2, \ \ldots, \ \omega_n^{n-1} \qquad\text{where } \omega_n = \exp\Big(i\frac{2\pi}{n}\Big) ,
> $$
>
> and $\omega_n^n = 1$. For $n = 3$: $1$, $\frac{-1 \pm \sqrt3\,i}{2}$; for $n = 4$: $\pm1$, $\pm i$; for $n = 6$: $\pm1$, $\pm\frac12 \pm \frac{\sqrt3}{2}i$ (an equilateral triangle, a square and a regular hexagon, B&C Fig. 13).
>
> **The sum vanishes** (Exercise 7). For any $c \ne 1$, let $S = 1 + c + c^2 + \cdots + c^{n-1}$. Then $cS = c + c^2 + \cdots + c^n$, and subtracting, $S - cS = 1 - c^n$, so
>
> $$
> 1 + c + c^2 + \cdots + c^{n-1} = \frac{1 - c^n}{1 - c} \qquad (c \ne 1)
> $$
>
> (the identity of B&C's Exercise 9, Sec. 9, with $n - 1$ in place of $n$). If $c$ is an $n$th root of unity, $c^n = 1$ and the sum is $0$. With $c = \omega_n$: the $n$ vertices of the regular polygon, viewed as vectors from its center, add up to zero.
>
> *B&C: Sec. 11, Example 2 and Exercise 7*

^ex-11-2

> [!example] Example §11.3: The Square Roots of a + i
> Let $a$ be any positive real number. Find the two square roots of $a + i$ in rectangular form.
>
> **Exponential form.** Write $A = |a + i| = \sqrt{a^2 + 1}$ and $\alpha = \operatorname{Arg}(a + i)$. Since $a + i = A\exp[i(\alpha + 2k\pi)]$ $(k = 0, \pm1, \ldots)$, the square roots are
>
> $$
> c_k = \sqrt A\exp\Big[i\Big(\frac\alpha2 + k\pi\Big)\Big] \qquad (k = 0, 1) . \qquad (3)
> $$
>
> Because $e^{i\pi} = -1$, the two values of $(a + i)^{1/2}$ reduce to
>
> $$
> c_0 = \sqrt A\,e^{i\alpha/2} \qquad\text{and}\qquad c_1 = -c_0 . \qquad (4)
> $$
>
> **Half angles.** By Euler's formula,
>
> $$
> c_0 = \sqrt A\Big(\cos\frac\alpha2 + i\sin\frac\alpha2\Big) . \qquad (5)
> $$
>
> Because $a + i$ lies above the real axis, $0 < \alpha < \pi$, so $\cos\frac\alpha2 > 0$ and $\sin\frac\alpha2 > 0$. Hence, by the identities $\cos^2\frac\alpha2 = \frac{1 + \cos\alpha}{2}$ and $\sin^2\frac\alpha2 = \frac{1 - \cos\alpha}{2}$ (taking positive square roots),
>
> $$
> c_0 = \sqrt A\bigg(\sqrt{\frac{1 + \cos\alpha}{2}} + i\sqrt{\frac{1 - \cos\alpha}{2}}\bigg) . \qquad (6)
> $$
>
> **Eliminate $\alpha$.** But $\cos\alpha = a/A$, and so
>
> $$
> \sqrt{\frac{1 \pm \cos\alpha}{2}} = \sqrt{\frac{1 \pm (a/A)}{2}} = \sqrt{\frac{A \pm a}{2A}} . \qquad (7)
> $$
>
> Consequently, from (6), (7) and $c_1 = -c_0$, the two square roots of $a + i$ $(a > 0)$ are
>
> $$
> \pm\frac{1}{\sqrt2}\Big(\sqrt{A + a} + i\sqrt{A - a}\Big) . \qquad (8)
> $$
>
> **Check.** Since $(A + a)(A - a) = A^2 - a^2 = 1$,
>
> $$
> \Big[\frac{1}{\sqrt2}\Big(\sqrt{A + a} + i\sqrt{A - a}\Big)\Big]^2 = \frac12\Big[(A + a) - (A - a) + 2i\sqrt{(A + a)(A - a)}\Big] = a + i .
> $$
>
> The derivation used only $0 < \alpha < \pi$, so (8) holds for every real $a$. For $a = 0$ it gives the square roots of $i$: $\pm\frac{1}{\sqrt2}(1 + i)$.
>
> *B&C: Sec. 11, Example 3*

^ex-11-3

> [!example] Example §11.4: The Quadratic Formula
> **(a)** Prove that the usual formula solves $az^2 + bz + c = 0$ $(a \ne 0)$ when $a$, $b$, $c$ are complex: by completing the square, derive
>
> $$
> z = \frac{-b + (b^2 - 4ac)^{1/2}}{2a} ,
> $$
>
> where both square roots are to be considered when $b^2 - 4ac \ne 0$. **(b)** Find the roots of $z^2 + 2z + (1 - i) = 0$.
>
> **(a)** Dividing by $a$ and completing the square (all steps use only the field laws of [[§2 Basic Algebraic Properties|§2]]–[[§3 Further Algebraic Properties|§3]]),
>
> $$
> az^2 + bz + c = 0 \iff z^2 + \frac{b}{a}z + \frac{c}{a} = 0 \iff \Big(z + \frac{b}{2a}\Big)^2 = \frac{b^2 - 4ac}{4a^2} \iff \big(2az + b\big)^2 = b^2 - 4ac ,
> $$
>
> the last step multiplying by $4a^2 \ne 0$. So $z$ is a root exactly when $2az + b$ is a square root of $b^2 - 4ac$, that is, $z = \dfrac{-b + w}{2a}$ with $w \in (b^2 - 4ac)^{1/2}$. By [[§10 Roots of Complex Numbers#^thm-10-2|Theorem §10.2]], if $b^2 - 4ac \ne 0$ it has two square roots $\pm w_0$, giving two roots $z$; if $b^2 - 4ac = 0$ the only root is $z = -b/(2a)$.
>
> **(b)** Here $a = 1$, $b = 2$, $c = 1 - i$, and $b^2 - 4ac = 4 - 4(1 - i) = 4i$. Since $4i = 4\exp[i(\frac\pi2 + 2k\pi)]$, its square roots are $\pm 2e^{i\pi/4} = \pm\sqrt2(1 + i)$. So
>
> $$
> z = \frac{-2 \pm \sqrt2(1 + i)}{2} = -1 \pm \frac{1 + i}{\sqrt2} : \qquad \Big(-1 + \frac{1}{\sqrt2}\Big) + \frac{i}{\sqrt2}, \qquad \Big(-1 - \frac{1}{\sqrt2}\Big) - \frac{i}{\sqrt2} .
> $$
>
> *B&C: Sec. 11, Exercise 8*

^ex-11-4

> [!example] Example §11.5: Factoring z⁴ + 4
> Find the four zeros of $z^4 + 4$, one of them being $z_0 = \sqrt2\,e^{i\pi/4} = 1 + i$, and use them to factor $z^4 + 4$ into quadratic factors with real coefficients.
>
> **Zeros.** $z^4 = -4 = 4\exp[i(\pi + 2k\pi)]$, so the zeros are the fourth roots $\sqrt2\exp\big[i\big(\frac\pi4 + \frac{k\pi}{2}\big)\big]$, $k = 0, 1, 2, 3$, exactly as in Example §11.1 with $\sqrt2$ in place of $2$:
>
> $$
> 1 + i, \qquad -1 + i, \qquad -1 - i, \qquad 1 - i .
> $$
>
> **Factor.** Group each zero with its conjugate:
>
> $$
> \big(z - (1 + i)\big)\big(z - (1 - i)\big) = (z - 1)^2 + 1 = z^2 - 2z + 2, \qquad \big(z - (-1 + i)\big)\big(z - (-1 - i)\big) = (z + 1)^2 + 1 = z^2 + 2z + 2 .
> $$
>
> So $z^4 + 4 = (z^2 + 2z + 2)(z^2 - 2z + 2)$. Check: the product is $(z^2 + 2)^2 - (2z)^2 = z^4 + 4z^2 + 4 - 4z^2 = z^4 + 4$.
>
> *B&C: Sec. 11, Exercise 6*

^ex-11-5

> [!remark]- Connections
> - Example §11.5 is an instance of two Linear Algebra facts: the non-real zeros of a real polynomial come in conjugate pairs, [[§13 Polynomials#^ladr-4-14|LADR 4.14]], and every real polynomial factors into real linear and quadratic factors, [[§13 Polynomials#^ladr-4-16|LADR 4.16]]. When a real quadratic has real roots is [[§13 Polynomials#^ladr-4-15|LADR 4.15]]; over $\mathbb{C}$, Example §11.4 shows, every quadratic has roots.
