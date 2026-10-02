---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 87
bc: "87"
aliases: ["B&C 87"]
tags: [complex-variables, math342]
---
← [[§86 Example (Evaluation of Improper Integrals)]] · ↑ [[· 7 Applications of Residues]] · [[§88★ Jordan's Lemma]] →

*Brown–Churchill, Section 87 · MAT 342 HW 12, Practice Finals (Spring 2012, Fall 2002, Fall 2009).*

Integrals of the form $\int f(x)\cos ax\,dx$ and $\int f(x)\sin ax\,dx$, with $f = p/q$ rational and $a > 0$, are the Fourier transforms of rational functions; they occur throughout the theory of the Fourier integral. The method of §85 cannot be applied to $f(z)\cos az$ directly, because $\cos az$ grows exponentially away from the real axis. The remedy is to integrate $f(z)e^{iaz}$ instead: on the real axis its real and imaginary parts are the two integrands wanted, and in the upper half plane $|e^{iaz}| = e^{-ay} \le 1$, so the arc integral is no harder than before. One residue computation then gives the cosine and the sine integral together.

## Why e^{iaz}

Let $f(x) = p(x)/q(x)$ with $p$ and $q$ real polynomials without common factors, $q$ with no real zeros and at least one zero above the real axis, and let $a > 0$. We want

$$
\int_{-\infty}^{\infty} f(x)\sin ax\,dx \qquad\text{or}\qquad \int_{-\infty}^{\infty} f(x)\cos ax\,dx . \qquad (1)
$$

By [[§39★ Hyperbolic Functions|§39★]], $|\sin az|^2 = \sin^2 ax + \sinh^2 ay$ and $|\cos az|^2 = \cos^2 ax + \sinh^2 ay$; since $\sinh ay = \frac12(e^{ay} - e^{-ay})$, both moduli grow like $\frac12e^{ay}$ as $y \to \infty$, and no estimate on a large semicircle can succeed. But

$$
\int_{-R}^{R} f(x)\cos ax\,dx + i\int_{-R}^{R} f(x)\sin ax\,dx = \int_{-R}^{R} f(x)e^{iax}\,dx ,
$$

because $f(x)$ is real, and

$$
|e^{iaz}| = |e^{ia(x + iy)}| = |e^{-ay}e^{iax}| = e^{-ay} \le 1 \qquad (y \ge 0) .
$$

> [!theorem] Proposition §87.1: Fourier-Type Integrals of Rational Functions
> Let $f = p/q$ and $a > 0$ be as above, let $z_1, \ldots, z_n$ be the zeros of $q$ above the real axis, and suppose $\deg q \ge \deg p + 2$. Then $\int_{-\infty}^{\infty} f(x)e^{iax}\,dx$ converges absolutely, and
>
> $$
> \int_{-\infty}^{\infty} f(x)e^{iax}\,dx = 2\pi i\sum_{k=1}^{n}\operatorname*{Res}_{z=z_k}\big[f(z)e^{iaz}\big] ,
> $$
>
> $$
> \int_{-\infty}^{\infty} f(x)\cos ax\,dx = \operatorname{Re}\Big(2\pi i\sum_{k=1}^{n}\operatorname*{Res}_{z=z_k}\big[f(z)e^{iaz}\big]\Big), \qquad \int_{-\infty}^{\infty} f(x)\sin ax\,dx = \operatorname{Im}\Big(2\pi i\sum_{k=1}^{n}\operatorname*{Res}_{z=z_k}\big[f(z)e^{iaz}\big]\Big) .
> $$
>
> *B&C: Sec. 87 (text), with the estimate of its Example stated in general*

^prop-87-1

> [!proof]+ Proof
> $f(z)e^{iaz}$ is analytic except at the zeros of $q$, since $e^{iaz}$ is entire and never zero. For $R > \max|z_k|$, the residue theorem on the boundary of the half disk, exactly as in [[§85 Evaluation of Improper Integrals#^thm-85-3|Theorem §85.3]], gives
>
> $$
> \int_{-R}^{R} f(x)e^{iax}\,dx = 2\pi i\sum_{k=1}^{n}\operatorname*{Res}_{z=z_k}\big[f(z)e^{iaz}\big] - \int_{C_R} f(z)e^{iaz}\,dz .
> $$
>
> By [[§85 Evaluation of Improper Integrals#^prop-85-4|Proposition §85.4]], $|f(z)| \le K/|z|^2$ for $|z| \ge R_1$, and $|e^{iaz}| \le 1$ on $C_R$; so $\big|\int_{C_R} f(z)e^{iaz}\,dz\big| \le \pi K/R \to 0$ ([[§47 Upper Bounds for Moduli of Contour Integrals|§47]]). On the real axis $|f(x)e^{iax}| = |f(x)| \le K/x^2$ for $|x| \ge R_1$, so the real and imaginary parts $f(x)\cos ax$ and $f(x)\sin ax$ have absolutely convergent improper integrals (comparison, as in the proof of Proposition §85.4). The integral therefore converges, equals its principal value, and that is the limit of the residue identity. Since $f(x)$ is real, taking real and imaginary parts gives the last two formulas.

^pf-87-1

*Uses:* [[§85 Evaluation of Improper Integrals#^thm-85-3|§85.3]], [[§85 Evaluation of Improper Integrals#^prop-85-4|§85.4]], [[§85 Evaluation of Improper Integrals#^prop-85-1|§85.1]], [[§76 Cauchy's Residue Theorem|§76]] (Theorem), [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (Theorem), [[§30 The Exponential Function|§30]]

> [!remark]- Connections
> - These are the coefficient functions of the Fourier integral: for real $f$, $A(\lambda) = \frac1\pi\int f(x)\cos\lambda x\,dx$ and $B(\lambda) = \frac1\pi\int f(x)\sin\lambda x\,dx$, [[§14 Fourier Integral#^def-14-1|341 Def. §14.1]], or $C(\lambda) = \frac{1}{2\pi}\int f(x)e^{-i\lambda x}\,dx$, [[§15★ Complex Methods#^def-15-2|341 Def. §15.2]]. Proposition §87.1 computes the Fourier transform of any rational function with $\deg q \ge \deg p + 2$ in closed form; Example §87.2 is the case $f = 1/(x^2 + 1)$.

When $\deg q = \deg p + 1$, the bound $|f| \le K/R$ is too weak for this argument, although the integrals may still converge; that case is the subject of Jordan's lemma, [[§88★ Jordan's Lemma|§88★]].

> [!remark] Remark: Method — Integrals of f(x) cos ax and f(x) sin ax
> 1. **Replace** $\cos ax$ or $\sin ax$ by $e^{iaz}$ (with $a > 0$; for $a < 0$ use $\cos ax = \cos|a|x$ and $\sin ax = -\sin|a|x$). Never integrate $f(z)\cos az$ around a semicircle.
> 2. **Residues** of $f(z)e^{iaz}$ at the zeros of $q$ in the upper half plane; $e^{iaz}$ is part of the numerator $\phi$ in the residue formulas.
> 3. **The arc.** If $\deg q \ge \deg p + 2$: $|f(z)e^{iaz}| \le |f(z)| \le M_R$ and $M_R\,\pi R \to 0$. If $\deg q = \deg p + 1$: Jordan's lemma ([[§88★ Jordan's Lemma|§88★]]).
> 4. **Take real or imaginary parts** of $2\pi i\sum\operatorname{Res}$. For an even integrand halve the result to get $\int_0^\infty$: $f(x)\cos ax$ is even when $f$ is, and $f(x)\sin ax$ is even when $f$ is odd.
> 5. **Check:** the cosine integral of an even $f$ comes out real, and the sine integral of an even $f$ is $0$.

^rem-87-1

## Examples

> [!example] Example §87.1: The Integral of cos 2x/(x² + 4)²
> Show that
>
> $$
> \int_0^\infty\frac{\cos 2x}{(x^2 + 4)^2}\,dx = \frac{5\pi}{32e^4} . \qquad (2)
> $$
>
> Let $f(z) = 1/(z^2 + 4)^2$ (3). The product $f(z)e^{i2z}$ is analytic on and above the real axis except at $z = 2i$, which lies inside the half disk for $R > 2$; integrating around its boundary,
>
> $$
> \int_{-R}^{R}\frac{e^{i2x}}{(x^2 + 4)^2}\,dx = 2\pi iB - \int_{C_R} f(z)e^{i2z}\,dz, \qquad B = \operatorname*{Res}_{z=2i}\big[f(z)e^{i2z}\big] . \qquad (4)
> $$
>
> **Residue.** $f(z)e^{i2z} = \phi(z)/(z - 2i)^2$ with $\phi(z) = e^{i2z}/(z + 2i)^2$, analytic and nonzero at $2i$, so $z = 2i$ is a pole of order $2$ and $B = \phi'(2i)$ ([[§80 Residues at Poles|§80]], Theorem). Since
>
> $$
> \phi'(z) = \frac{2ie^{i2z}(z + 2i) - 2e^{i2z}}{(z + 2i)^3}, \qquad B = \phi'(2i) = \frac{e^{-4}(2i\cdot4i - 2)}{(4i)^3} = \frac{-10e^{-4}}{-64i} = \frac{5}{32e^4i} .
> $$
>
> **Real parts.** Equating real parts in (4), $2\pi iB = \frac{5\pi}{16e^4}$ is real, so
>
> $$
> \int_{-R}^{R}\frac{\cos 2x}{(x^2 + 4)^2}\,dx = \frac{5\pi}{16e^4} - \operatorname{Re}\int_{C_R} f(z)e^{i2z}\,dz . \qquad (5)
> $$
>
> **The arc.** On $C_R$, $|f(z)| \le M_R = 1/(R^2 - 4)^2$ and $|e^{i2z}| = e^{-2y} \le 1$; with $|\operatorname{Re} w| \le |w|$,
>
> $$
> \Big|\operatorname{Re}\int_{C_R} f(z)e^{i2z}\,dz\Big| \le \Big|\int_{C_R} f(z)e^{i2z}\,dz\Big| \le M_R\,\pi R = \frac{\pi/R^3}{\big(1 - 4/R^2\big)^2} \to 0 . \qquad (6)
> $$
>
> So $\text{P.V.}\int_{-\infty}^{\infty}\frac{\cos 2x}{(x^2 + 4)^2}\,dx = \frac{5\pi}{16e^4}$, and since the integrand is even this is (2) after halving: $\frac{5\pi}{32e^4} \approx 0.0089907$, as quadrature confirms.
>
> *B&C: Sec. 87, Example*

^ex-87-1

> [!example] Example §87.2: The Integral of cos ax/(x² + 1)
> Show that $\displaystyle\int_0^\infty\frac{\cos ax}{x^2 + 1}\,dx = \frac\pi2e^{-a}$ for $a > 0$.
>
> The only zero of $z^2 + 1$ above the axis is $i$, a simple zero, so
>
> $$
> \operatorname*{Res}_{z=i}\frac{e^{iaz}}{z^2 + 1} = \frac{e^{iaz}}{2z}\Big|_{z=i} = \frac{e^{-a}}{2i}, \qquad 2\pi i\cdot\frac{e^{-a}}{2i} = \pi e^{-a} .
> $$
>
> **The arc.** For $R > 1$ and $z$ on $C_R$: $|e^{iaz}| \le 1$ and $|z^2 + 1| \ge R^2 - 1$, so $\big|\int_{C_R}\frac{e^{iaz}}{z^2 + 1}dz\big| \le \frac{\pi R}{R^2 - 1} \to 0$. (The length factor $\pi R$ matters: $M_R = 1/(R^2 - 1) \to 0$ alone would not suffice for the bound of §47; it suffices only through Jordan's lemma, [[§88★ Jordan's Lemma#^thm-88-2|Theorem §88.2]].)
>
> **Conclusion.** $\int_{-\infty}^{\infty}\frac{\cos ax}{x^2 + 1}\,dx = \operatorname{Re}(\pi e^{-a}) = \pi e^{-a}$, and halving the even integrand, $\int_0^\infty = \frac\pi2e^{-a}$ (for $a = 2$: $0.212584$, as quadrature confirms). The imaginary part gives $\int_{-\infty}^{\infty}\frac{\sin ax}{x^2 + 1}\,dx = 0$, as it must for an odd integrand.
>
> *B&C: Sec. 88, Exercise 2; Source: 342 HW 12*

^ex-87-2

> [!remark]- Connections
> - Read with $a = |x|$ and the integration variable $\lambda$, this is $e^{-|x|} = \frac2\pi\int_0^\infty\frac{\cos\lambda x}{1 + \lambda^2}\,d\lambda$, the Fourier integral representation of [[§14 Fourier Integral#^ex-14-4|341 Ex. §14.4]](a), which 341 obtains from the Fourier integral theorem; here it is verified directly, for every $x$.

> [!example] Example §87.3: A Double Pole
> Prove that for all $a > 0$ and $b > 0$,
>
> $$
> \int_{-\infty}^{\infty}\frac{\cos ax}{(x^2 + b^2)^2}\,dx = \frac{\pi}{2b^3}(1 + ab)e^{-ab} .
> $$
>
> **Residue.** The zeros of $(z^2 + b^2)^2$ are $\pm ib$, each of order $2$; only $ib$ is above the axis. With $\phi(z) = e^{iaz}/(z + ib)^2$,
>
> $$
> \operatorname*{Res}_{z=ib}\frac{e^{iaz}}{(z^2 + b^2)^2} = \phi'(ib) = \frac{iae^{iaz}(z + ib) - 2e^{iaz}}{(z + ib)^3}\Big|_{z=ib} = e^{-ab}\,\frac{ia\cdot2ib - 2}{(2ib)^3} = e^{-ab}\,\frac{-2(1 + ab)}{-8ib^3} = \frac{(1 + ab)e^{-ab}}{4ib^3} .
> $$
>
> **Conclusion.** $\deg q = 4 \ge 0 + 2$, so Proposition §87.1 applies:
>
> $$
> \int_{-\infty}^{\infty}\frac{\cos ax}{(x^2 + b^2)^2}\,dx = \operatorname{Re}\Big(2\pi i\cdot\frac{(1 + ab)e^{-ab}}{4ib^3}\Big) = \frac{\pi(1 + ab)e^{-ab}}{2b^3} .
> $$
>
> Halving gives B&C's form $\int_0^\infty\frac{\cos ax}{(x^2 + b^2)^2}\,dx = \frac{\pi}{4b^3}(1 + ab)e^{-ab}$, and $a = 2$, $b = 2$ recovers Example §87.1: $\frac{\pi}{32}\cdot5e^{-4}$. Quadrature confirms the formula (for instance $1.155727$ at $a = b = 1$). The key reaches the same residue and value; it does not show the estimate of the arc integral.
>
> *B&C: Sec. 88, Exercise 3; Source: 342 practice final (Spring 2012), Q4*

^ex-87-3

> [!example] Example §87.4: A Pole Off the Imaginary Axis
> Find the Cauchy principal value of $\displaystyle\int_{-\infty}^{\infty}\frac{\sin x\,dx}{x^2 + 4x + 5}$.
>
> The integrand is not even, and the pole is not on the imaginary axis, so the residue is genuinely complex. $z^2 + 4z + 5 = (z + 2)^2 + 1$ has the simple zeros $-2 \pm i$; above the axis, $z_1 = -2 + i$:
>
> $$
> \operatorname*{Res}_{z=-2+i}\frac{e^{iz}}{z^2 + 4z + 5} = \frac{e^{iz}}{2z + 4}\Big|_{z=-2+i} = \frac{e^{-1-2i}}{2i}, \qquad 2\pi i\cdot\frac{e^{-1-2i}}{2i} = \frac\pi e\big(\cos 2 - i\sin 2\big) .
> $$
>
> Since $\deg q = 2 \ge 0 + 2$, Proposition §87.1 gives
>
> $$
> \int_{-\infty}^{\infty}\frac{\sin x\,dx}{x^2 + 4x + 5} = \operatorname{Im}\Big(\frac\pi e(\cos 2 - i\sin 2)\Big) = -\frac\pi e\sin 2 \approx -1.05090 ,
> $$
>
> B&C's answer, confirmed by quadrature; the real part gives, at no extra cost, $\int_{-\infty}^{\infty}\frac{\cos x\,dx}{x^2 + 4x + 5} = \frac\pi e\cos 2$.
>
> *B&C: Sec. 88, Exercise 8*

^ex-87-4

> [!example] Example §87.5: The Top Side of a Rectangle
> Let $C_A$ be the segment from $A + iA$ to $-A + iA$, where $A > 1$. Prove that
>
> $$
> \Big|\int_{C_A}\frac{e^{iz}}{z^2 + 1}\,dz\Big| \le \frac{2Ae^{-A}}{A^2 - 1} .
> $$
>
> On $C_A$, $z = x + iA$ with $-A \le x \le A$, so $|e^{iz}| = e^{-A}$, and $|z| \ge A$ gives $|z^2 + 1| \ge |z|^2 - 1 \ge A^2 - 1 > 0$. The length of $C_A$ is $2A$, and by [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (Theorem)
>
> $$
> \Big|\int_{C_A}\frac{e^{iz}}{z^2 + 1}\,dz\Big| \le \frac{e^{-A}}{A^2 - 1}\cdot 2A .
> $$
>
> The bound tends to $0$ as $A \to \infty$, much faster than the semicircle bound: the factor $e^{-A}$ comes from the height of the segment. This is the top side of the rectangle with vertices $\pm A$, $\pm A + iA$, an alternative to the semicircle for Fourier-type integrals; the two vertical sides are handled with $|e^{iz}| = e^{-y}$ and $\int_0^A e^{-y}\,dy \le 1$. The key's estimate is the same.
>
> *Source: 342 practice final (Fall 2002), Q7, 342 practice final (Fall 2009), Q7*

^ex-87-5
