---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 86
bc: "86"
aliases: ["B&C 86"]
tags: [complex-variables, math342]
---
← [[§85 Evaluation of Improper Integrals]] · ↑ [[· 7 Applications of Residues]] · [[§87 Improper Integrals from Fourier Analysis]] →

*Brown–Churchill, Section 86 · MAT 342 HW 12, Practice Finals (Spring 2005, Fall 2002, Fall 2009, Fall 1999).*

B&C devotes this section to one worked instance of the method of [[§85 Evaluation of Improper Integrals#^thm-85-3|Theorem §85.3]], the integral $\int_0^\infty dx/(x^6 + 1) = \pi/3$. The same three steps recur in the course homework and on every old final: locate the zeros of $q$ above the real axis as roots of complex numbers, compute the residues there by $p/q'$, and show that the integral over the arc $C_R$ disappears. B&C's Exercise 10 does all integrals $\int_0^\infty x^{2m}/(x^{2n} + 1)\,dx$ at once, and the last example replaces the semicircle by a sector, which uses the rotational symmetry of the integrand to need only one residue.

> [!example] Example §86.1: The Integral of 1/(x⁶ + 1)
> Evaluate $\displaystyle\int_0^\infty\frac{dx}{x^6 + 1}$.
>
> **Singular points.** $f(z) = 1/(z^6 + 1)$ is analytic except at the zeros of $z^6 + 1$, the sixth roots of $-1$ ([[§10 Roots of Complex Numbers|§10]]):
>
> $$
> c_k = \exp\Big[i\Big(\frac\pi6 + \frac{2k\pi}{6}\Big)\Big] \qquad (k = 0, 1, 2, \ldots, 5) .
> $$
>
> None is real. The first three, $c_0 = e^{i\pi/6}$, $c_1 = i$, $c_2 = e^{i5\pi/6}$, lie in the upper half plane, the other three in the lower one. For $R > 1$, integrating around the boundary of the half disk gives
>
> $$
> \int_{-R}^{R} f(x)\,dx + \int_{C_R} f(z)\,dz = 2\pi i(B_0 + B_1 + B_2), \qquad (1)
> $$
>
> where $B_k$ is the residue of $f$ at $c_k$.
>
> **Residues.** By [[§83 Zeros and Poles|§83]] (Theorem 2) each $c_k$ is a simple pole, and since $c_k^6 = -1$,
>
> $$
> B_k = \frac{1}{6c_k^5} = \frac{c_k}{6c_k^6} = -\frac{c_k}{6} \qquad (k = 0, 1, 2), \qquad\text{so}\qquad B_0 + B_1 + B_2 = -\frac16(c_0 + c_1 + c_2) . \qquad (2)
> $$
>
> On the unit circle $c_2 = e^{i5\pi/6} = -e^{-i\pi/6}$, and $e^{i\pi/6} - e^{-i\pi/6} = 2i\sin\frac\pi6 = i$ ([[§37 The Trigonometric Functions sin z and cos z|§37]]). Hence
>
> $$
> B_0 + B_1 + B_2 = -\frac16\big(e^{i\pi/6} + i - e^{-i\pi/6}\big) = -\frac i3, \qquad \int_{-R}^{R} f(x)\,dx = \frac{2\pi}{3} - \int_{C_R} f(z)\,dz \qquad (3)
> $$
>
> for all $R > 1$.
>
> **The arc.** For $R > 1$ and $z$ on $C_R$, $|z^6 + 1| \ge \big||z|^6 - 1\big| = R^6 - 1$, so $|f(z)| \le M_R = 1/(R^6 - 1)$ and ([[§47 Upper Bounds for Moduli of Contour Integrals|§47]])
>
> $$
> \Big|\int_{C_R} f(z)\,dz\Big| \le M_R\,\pi R = \frac{\pi R}{R^6 - 1} = \frac{\pi/R^5}{1 - 1/R^6} \longrightarrow 0 . \qquad (4)
> $$
>
> **Conclusion.** Letting $R \to \infty$ in (3), $\int_{-\infty}^{\infty} dx/(x^6 + 1) = 2\pi/3$ (the principal value, which is the integral since the integrand is even), and by (7) of §85
>
> $$
> \int_0^\infty\frac{dx}{x^6 + 1} = \frac\pi3 . \qquad (5)
> $$
>
> *B&C prints the intermediate limit as "P.V. $\int_{-R}^{R}$" (p. 264); it is $\text{P.V.}\int_{-\infty}^{\infty}$.*
>
> *B&C: Sec. 86, Example*

^ex-86-1

> [!example] Example §86.2: The Integral of 1/(x⁴ + 1)
> Show that $\displaystyle\int_0^\infty\frac{dx}{x^4 + 1} = \frac{\pi}{2\sqrt2}$.
>
> **Zeros.** $z^4 = -1 = e^{i\pi}$ gives $z = e^{i(\pi/4 + k\pi/2)}$, $k = 0, 1, 2, 3$; the two above the axis are $z_1 = e^{i\pi/4}$ and $z_2 = e^{i3\pi/4}$, and none is real.
>
> **Residues.** At each simple zero, with $z_k^4 = -1$,
>
> $$
> \operatorname{Res}_{z=z_k}\frac{1}{z^4 + 1} = \frac{1}{4z_k^3} = \frac{z_k}{4z_k^4} = -\frac{z_k}{4} .
> $$
>
> Since $e^{i\pi/4} + e^{i3\pi/4} = \frac{1 + i}{\sqrt2} + \frac{-1 + i}{\sqrt2} = i\sqrt2$, the sum of the residues is $-\frac{i\sqrt2}{4}$.
>
> **Arc and conclusion.** $\deg(z^4 + 1) = 4 \ge 0 + 2$, so the arc integral tends to zero ([[§85 Evaluation of Improper Integrals#^prop-85-4|Proposition §85.4]]; directly, $|\int_{C_R}| \le \pi R/(R^4 - 1) \to 0$). The integrand is even, so by (12) of §85
>
> $$
> \int_0^\infty\frac{dx}{x^4 + 1} = \pi i\Big(-\frac{i\sqrt2}{4}\Big) = \frac{\pi\sqrt2}{4} = \frac{\pi}{2\sqrt2} \approx 1.11072 ,
> $$
>
> in agreement with numerical quadrature. The Fall 2002 key computes the same two residues as $\frac14e^{-i3\pi/4}$ and $\frac14e^{-i9\pi/4}$ and reaches the same value.
>
> *B&C: Sec. 86, Exercise 3; Source: 342 HW 12, 342 practice final (Fall 2002), Q9, 342 practice final (Fall 2009), Q8*

^ex-86-2

> [!example] Example §86.3: Two Quadratic Factors
> Show that $\displaystyle\int_0^\infty\frac{x^2\,dx}{(x^2 + 1)(x^2 + 4)} = \frac\pi6$.
>
> **Zeros.** $q(z) = (z^2 + 1)(z^2 + 4) = z^4 + 5z^2 + 4$ has the zeros $\pm i$, $\pm2i$; above the axis, $i$ and $2i$, both simple. $q'(z) = 4z^3 + 10z$.
>
> **Residues.** With $p(z) = z^2$,
>
> $$
> \operatorname{Res}_{z=i}\frac{p}{q} = \frac{p(i)}{q'(i)} = \frac{-1}{-4i + 10i} = \frac{-1}{6i} = \frac i6, \qquad \operatorname{Res}_{z=2i}\frac{p}{q} = \frac{-4}{-32i + 20i} = \frac{-4}{-12i} = -\frac i3 .
> $$
>
> The sum is $-\frac i6$, and $2\pi i\cdot(-\frac i6) = \frac\pi3$.
>
> **Arc.** For $R > 2$ and $|z| = R$: $|z^2 + 1| \ge R^2 - 1$ and $|z^2 + 4| \ge R^2 - 4$, so
>
> $$
> \Big|\int_{C_R}\frac{z^2\,dz}{(z^2 + 1)(z^2 + 4)}\Big| \le \frac{\pi R^3}{(R^2 - 1)(R^2 - 4)} = \frac{\pi/R}{(1 - R^{-2})(1 - 4R^{-2})} \to 0 .
> $$
>
> **Conclusion.** $\int_{-\infty}^{\infty} = \frac\pi3$, and since the integrand is even, $\int_0^\infty = \frac\pi6 \approx 0.523599$, as quadrature confirms.
>
> *B&C: Sec. 86, Exercise 5; Source: 342 HW 12*

^ex-86-3

> [!example] Example §86.4: All Integrals of x²ᵐ/(x²ⁿ + 1)
> Let $m$ and $n$ be integers with $0 \le m < n$. Derive
>
> $$
> \int_0^\infty\frac{x^{2m}}{x^{2n} + 1}\,dx = \frac{\pi}{2n}\csc\Big(\frac{2m + 1}{2n}\pi\Big) .
> $$
>
> **(a) Zeros.** $z^{2n} = -1 = e^{i\pi}$ has the $2n$ roots $\exp\big(i(2k + 1)\pi/(2n)\big)$, $k = 0, \ldots, 2n - 1$. Their arguments $(2k + 1)\pi/(2n)$ are never multiples of $\pi$ (an odd number over an even one is not an integer), so none is real; those in $0 < \arg z < \pi$ are
>
> $$
> c_k = \exp\Big(i\,\frac{(2k + 1)\pi}{2n}\Big) \qquad (k = 0, 1, \ldots, n - 1) .
> $$
>
> **(b) Residues.** Each $c_k$ is a simple zero of $q = z^{2n} + 1$ ($q'(c_k) = 2nc_k^{2n-1} \ne 0$), and $c_k^{2m} \ne 0$, so by [[§83 Zeros and Poles|§83]] (Theorem 2), with $c_k^{2n} = -1$ and $\alpha = \frac{2m + 1}{2n}\pi$,
>
> $$
> \operatorname{Res}_{z=c_k}\frac{z^{2m}}{z^{2n} + 1} = \frac{c_k^{2m}}{2nc_k^{2n-1}} = \frac{c_k^{2m+1}}{2nc_k^{2n}} = -\frac{1}{2n}e^{i(2k+1)\alpha} .
> $$
>
> The sum is geometric with ratio $e^{i2\alpha} \ne 1$ ([[§9 Arguments of Products and Quotients|§9]], Exercise 9), and $e^{i2n\alpha} = e^{i(2m+1)\pi} = -1$:
>
> $$
> \sum_{k=0}^{n-1} e^{i(2k+1)\alpha} = e^{i\alpha}\,\frac{1 - e^{i2n\alpha}}{1 - e^{i2\alpha}} = \frac{2e^{i\alpha}}{1 - e^{i2\alpha}} = \frac{2}{e^{-i\alpha} - e^{i\alpha}} = \frac{2}{-2i\sin\alpha} = \frac{i}{\sin\alpha} .
> $$
>
> Hence $2\pi i\sum_k\operatorname{Res} = 2\pi i\cdot\big(-\frac{1}{2n}\big)\cdot\frac{i}{\sin\alpha} = \frac{\pi}{n\sin\alpha}$.
>
> **(c) Conclusion.** Since $m < n$, $\deg q = 2n \ge 2m + 2$, so the arc integral vanishes (Proposition §85.4), and the integrand is even:
>
> $$
> \int_0^\infty\frac{x^{2m}}{x^{2n} + 1}\,dx = \frac{\pi}{2n\sin\alpha} = \frac{\pi}{2n}\csc\Big(\frac{2m + 1}{2n}\pi\Big) .
> $$
>
> **Special cases.** $m = 0$, $n = 3$: $\frac\pi6\csc\frac\pi6 = \frac\pi3$ (Example §86.1). $m = 0$, $n = 2$: $\frac\pi4\csc\frac\pi4 = \frac{\pi}{2\sqrt2}$ (Example §86.2). $m = 1$, $n = 2$: $\int_0^\infty\frac{x^2\,dx}{x^4 + 1} = \frac\pi4\csc\frac{3\pi}{4} = \frac{\pi}{2\sqrt2}$, the Spring 2005 problem; its key finds the residues $\frac14e^{-i\pi/4}$, $\frac14e^{-i3\pi/4}$ at $e^{i\pi/4}$, $e^{i3\pi/4}$ and the same value. $m = 1$, $n = 3$: $\int_0^\infty\frac{x^2\,dx}{1 + x^6} = \frac\pi6\csc\frac\pi2 = \frac\pi6$ (B&C's Exercise 4, the Fall 1999 problem). Quadrature confirms all four (and, for instance, $m = 2$, $n = 5$: $\frac{\pi}{10}$).
>
> *B&C: Sec. 86, Exercise 10; Source: 342 practice final (Spring 2005), Q9, 342 practice final (Fall 1999), Q5*

^ex-86-4

> [!example] Example §86.5: A Sector Instead of a Semicircle
> Use a residue and the boundary of the sector $0 \le |z| \le R$, $0 \le \arg z \le 2\pi/3$ $(R > 1)$ to show that
>
> $$
> \int_0^\infty\frac{dx}{x^3 + 1} = \frac{2\pi}{3\sqrt3} .
> $$
>
> The integrand is not even, so the semicircle of §85 would produce $\int_{-\infty}^{\infty}$, which diverges at $x = -1$. The sector uses instead the symmetry $z^3 = r^3$ on the ray $z = re^{i2\pi/3}$.
>
> **The pole inside.** The zeros of $z^3 + 1$ are $-1$ and $e^{\pm i\pi/3}$. Only $e^{i\pi/3}$ has its argument in $(0, 2\pi/3)$; $-1$ (argument $\pi$) and $e^{-i\pi/3}$ are outside the sector. With $c = e^{i\pi/3}$, $c^3 = -1$:
>
> $$
> \operatorname{Res}_{z=c}\frac{1}{z^3 + 1} = \frac{1}{3c^2} = \frac{c}{3c^3} = -\frac{e^{i\pi/3}}{3} .
> $$
>
> **The three sides.** On the segment $z = x$ $(0 \le x \le R)$ the integral is $\int_0^R dx/(x^3 + 1)$. On the returning ray, $z = re^{i2\pi/3}$ with $r$ from $R$ to $0$, $z^3 = r^3e^{i2\pi} = r^3$ and $dz = e^{i2\pi/3}\,dr$, so its integral is $-e^{i2\pi/3}\int_0^R dr/(r^3 + 1)$. By the residue theorem,
>
> $$
> \big(1 - e^{i2\pi/3}\big)\int_0^R\frac{dx}{x^3 + 1} = 2\pi i\Big(-\frac{e^{i\pi/3}}{3}\Big) - \int_{C_R}\frac{dz}{z^3 + 1} ,
> $$
>
> where $C_R$ is the arc $z = Re^{i\theta}$, $0 \le \theta \le 2\pi/3$.
>
> **The arc.** $|z^3 + 1| \ge R^3 - 1$ on $C_R$, whose length is $2\pi R/3$, so $\big|\int_{C_R}\big| \le \frac{2\pi R}{3(R^3 - 1)} \to 0$.
>
> **Conclusion.** $1 - e^{i2\pi/3} = e^{i\pi/3}\big(e^{-i\pi/3} - e^{i\pi/3}\big) = -2i\sin\frac\pi3\,e^{i\pi/3} = -i\sqrt3\,e^{i\pi/3}$. Letting $R \to \infty$ (the integral converges by comparison with $1/x^3$),
>
> $$
> \int_0^\infty\frac{dx}{x^3 + 1} = \frac{-2\pi i\,e^{i\pi/3}/3}{-i\sqrt3\,e^{i\pi/3}} = \frac{2\pi}{3\sqrt3} \approx 1.20920 ,
> $$
>
> which quadrature confirms.
>
> *B&C: Sec. 86, Exercise 9*

^ex-86-5

![[m342-86-1.svg]]
*The sector contour of Example §86.5. On the ray at angle $2\pi/3$ the integrand $1/(z^3 + 1)$ takes the same values as on the positive real axis, so the two straight sides combine into $(1 - e^{i2\pi/3})\int_0^R$. Of the three zeros of $z^3 + 1$ on the unit circle (dashed), only $e^{i\pi/3}$ (red) is enclosed.*
