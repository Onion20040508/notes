---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 88
bc: "88"
aliases: ["B&C 88"]
tags: [complex-variables, math342, extension]
---
← [[§87 Improper Integrals from Fourier Analysis]] · ↑ [[· 7 Applications of Residues]] · [[§89★ An Indented Path]] →

*Brown–Churchill, Section 88.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

For a Fourier-type integral $\int f(x)e^{iax}\,dx$ the arc estimate of [[§87 Improper Integrals from Fourier Analysis#^prop-87-1|Proposition §87.1]] needs $|f| \le M_R$ on $C_R$ with $M_R\cdot\pi R \to 0$, that is, $\deg q \ge \deg p + 2$. Jordan's lemma removes the factor $R$: it is enough that $M_R \to 0$. The reason is that $|e^{iaz}| = e^{-aR\sin\theta}$ is exponentially small on the whole semicircle except near its two ends, and Jordan's inequality measures how short those ends are. With the lemma the method covers integrands such as $x\sin 2x/(x^2 + 3)$, which decay only like $1/x$ and converge only conditionally, and the same inequality evaluates the Fresnel integrals of diffraction theory.

## Jordan's Inequality and Jordan's Lemma

> [!theorem] Lemma §88.1: Jordan's Inequality
> For every $R > 0$,
>
> $$
> \int_0^{\pi} e^{-R\sin\theta}\,d\theta < \frac\pi R . \qquad (1)
> $$
>
> Equivalently, by symmetry, $\displaystyle\int_0^{\pi/2} e^{-R\sin\theta}\,d\theta < \frac{\pi}{2R}$ $(R > 0)$. $\qquad (2)$
>
> *B&C: Sec. 88, inequalities (1)–(2)*

^lem-88-1

> [!proof]+ Proof
> **$\sin\theta \ge 2\theta/\pi$ on $[0, \pi/2]$.** B&C reads this off the graphs (figure below); here is why. Let $g(\theta) = \sin\theta - 2\theta/\pi$. Then $g(0) = g(\pi/2) = 0$ and $g''(\theta) = -\sin\theta \le 0$, so $g$ is concave on $[0, \pi/2]$ and lies above the chord joining its endpoint values, which is $0$. Hence $g \ge 0$.
>
> **The estimate.** Since $R > 0$, $e^{-R\sin\theta} \le e^{-2R\theta/\pi}$ for $0 \le \theta \le \pi/2$, and
>
> $$
> \int_0^{\pi/2} e^{-R\sin\theta}\,d\theta \le \int_0^{\pi/2} e^{-2R\theta/\pi}\,d\theta = \frac{\pi}{2R}\big(1 - e^{-R}\big) < \frac{\pi}{2R} .
> $$
>
> This is (2). The substitution $\theta \mapsto \pi - \theta$ leaves $\sin\theta$ unchanged (the graph of $\sin\theta$ on $[0, \pi]$ is symmetric about $\theta = \pi/2$), so $\int_{\pi/2}^{\pi} e^{-R\sin\theta}\,d\theta = \int_0^{\pi/2} e^{-R\sin\theta}\,d\theta$, and adding gives (1).

^pf-88-1

![[m342-88-1.svg]]
*Jordan's inequality: on $0 \le \theta \le \pi/2$ the concave curve $y = \sin\theta$ lies above its chord $y = 2\theta/\pi$, and by symmetry above $y = 2(\pi - \theta)/\pi$ on the other half. So $e^{-R\sin\theta}$ is at most $e^{-2R\theta/\pi}$, whose integral is less than $\pi/(2R)$: the integrand is close to $1$ only on intervals of length about $1/R$ at the two ends.*

> [!theorem] Theorem §88.2: Jordan's Lemma
> Suppose that
> - (a) a function $f(z)$ is analytic at all points in the upper half plane $y \ge 0$ that are exterior to a circle $|z| = R_0$;
> - (b) $C_R$ denotes a semicircle $z = Re^{i\theta}$ $(0 \le \theta \le \pi)$, where $R > R_0$;
> - (c) for all points $z$ on $C_R$, there is a positive constant $M_R$ such that $|f(z)| \le M_R$ and $\lim_{R\to\infty} M_R = 0$.
>
> Then, for every positive constant $a$,
>
> $$
> \lim_{R\to\infty}\int_{C_R} f(z)e^{iaz}\,dz = 0 .
> $$
>
> *B&C: Sec. 88, Theorem*

^thm-88-2

> [!proof]+ Proof
> With the parametrization $z = Re^{i\theta}$, $dz = Rie^{i\theta}\,d\theta$ ([[§44 Contour Integrals|§44]]),
>
> $$
> \int_{C_R} f(z)e^{iaz}\,dz = \int_0^{\pi} f(Re^{i\theta})\exp\big(iaRe^{i\theta}\big)Rie^{i\theta}\,d\theta .
> $$
>
> Here $|f(Re^{i\theta})| \le M_R$ by (c), $|Rie^{i\theta}| = R$, and since $iaRe^{i\theta} = iaR\cos\theta - aR\sin\theta$,
>
> $$
> \big|\exp\big(iaRe^{i\theta}\big)\big| = e^{-aR\sin\theta} .
> $$
>
> The modulus of an integral is at most the integral of the modulus ([[§42 Definite Integrals of Functions w(t)|§42]]), so by Jordan's inequality (1) with $aR$ in place of $R$,
>
> $$
> \Big|\int_{C_R} f(z)e^{iaz}\,dz\Big| \le M_RR\int_0^{\pi} e^{-aR\sin\theta}\,d\theta < M_RR\cdot\frac{\pi}{aR} = \frac{M_R\pi}{a} .
> $$
>
> Since $M_R \to 0$ as $R \to \infty$, the integral tends to $0$.

^pf-88-2

*Uses:* [[§88★ Jordan's Lemma#^lem-88-1|§88.1]], [[§44 Contour Integrals|§44]], [[§42 Definite Integrals of Functions w(t)|§42]], [[§30 The Exponential Function|§30]]

> [!remark]- Connections
> - Jordan's lemma is what makes the Fourier transform of a function decaying only like $1/x$ computable by residues: the Fourier integral of [[§14 Fourier Integral#^def-14-1|341 Def. §14.1]] in its complex form [[§15★ Complex Methods#^thm-15-2|341 Thm. §15.2]], whose outer integral is likewise a symmetric limit $\lim_{L\to\infty}\int_{-L}^{L}$. For example, Example §88.1 below with $3$ replaced by $1$ and $2$ by $x$ gives $\frac2\pi\int_0^\infty\frac{\lambda\sin\lambda x}{1 + \lambda^2}\,d\lambda = e^{-x}$ $(x > 0)$, the representation of [[§14 Fourier Integral#^ex-14-4|341 Ex. §14.4]](b).

> [!remark] Remark: What Jordan's Lemma Adds
> The bound of [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] gives $\big|\int_{C_R} fe^{iaz}\big| \le M_R\,\pi R$, which tends to zero only if $M_R = o(1/R)$; for $f = p/q$ that is $\deg q \ge \deg p + 2$. Jordan's lemma gives $M_R\pi/a$, which tends to zero as soon as $M_R \to 0$, that is, $\deg q \ge \deg p + 1$. So for rational $f$ with $\deg q = \deg p + 1$ and $a > 0$,
>
> $$
> \text{P.V.}\int_{-\infty}^{\infty} f(x)e^{iax}\,dx = 2\pi i\sum_{k}\operatorname{Res}_{z=z_k}\big[f(z)e^{iaz}\big]
> $$
>
> (residues at the zeros of $q$ above the axis), by the argument of [[§87 Improper Integrals from Fourier Analysis#^prop-87-1|Proposition §87.1]]. Only the principal value is asserted: the integrals now converge conditionally, not absolutely. The factor $e^{iaz}$ with $a > 0$ is essential; Jordan's lemma says nothing about $\int_{C_R} f(z)\,dz$ itself, which for $f = 1/z$ is $\pi i$ for every $R$.

^rem-88-1

## Examples

> [!example] Example §88.1: The Integral of x sin 2x/(x² + 3)
> Evaluate $\displaystyle\int_0^\infty\frac{x\sin 2x}{x^2 + 3}\,dx$. (As usual, its existence is established by finding its value.)
>
> **Residue.** With $f(z) = \dfrac{z}{z^2 + 3} = \dfrac{z}{(z - \sqrt3 i)(z + \sqrt3 i)}$ and $R > \sqrt3$, the only singularity of $f(z)e^{i2z}$ inside the half disk is $z = \sqrt3 i$. It is a simple pole: $f(z)e^{i2z} = \phi(z)/(z - \sqrt3 i)$ with
>
> $$
> \phi(z) = \frac{z\exp(i2z)}{z + \sqrt3 i}, \qquad \phi(\sqrt3 i) = \frac12\exp(-2\sqrt3) \ne 0 ,
> $$
>
> so the residue is $B = \frac12\exp(-2\sqrt3)$. The residue theorem gives
>
> $$
> \int_{-R}^{R}\frac{xe^{i2x}}{x^2 + 3}\,dx = i\pi\exp(-2\sqrt3) - \int_{C_R} f(z)e^{i2z}\,dz , \qquad (4)
> $$
>
> and equating imaginary parts,
>
> $$
> \int_{-R}^{R}\frac{x\sin 2x}{x^2 + 3}\,dx = \pi\exp(-2\sqrt3) - \operatorname{Im}\int_{C_R} f(z)e^{i2z}\,dz , \qquad (5)
> $$
>
> with $\big|\operatorname{Im}\int_{C_R} fe^{i2z}\big| \le \big|\int_{C_R} fe^{i2z}\big|$ (6).
>
> **The arc needs Jordan.** On $C_R$, $|f(z)| \le M_R = R/(R^2 - 3)$ and $|e^{i2z}| \le 1$. The bound of §47 is $M_R\pi R = \pi R^2/(R^2 - 3) = \pi/(1 - 3/R^2)$, which tends to $\pi$, not $0$. But $M_R = \dfrac{1/R}{1 - 3/R^2} \to 0$, so Jordan's lemma (Theorem §88.2, $a = 2$) gives $\lim_{R\to\infty}\int_{C_R} f(z)e^{i2z}\,dz = 0$.
>
> **Conclusion.** The integrand in (5) is even, so
>
> $$
> \int_{-\infty}^{\infty}\frac{x\sin 2x}{x^2 + 3}\,dx = \pi\exp(-2\sqrt3), \qquad \int_0^\infty\frac{x\sin 2x}{x^2 + 3}\,dx = \frac\pi2\exp(-2\sqrt3) \approx 0.0491677 ,
> $$
>
> which quadrature (for an oscillatory integral) confirms.
>
> *B&C: Sec. 88, Example*

^ex-88-1

> [!example] Example §88.2: The Integral of x³ sin ax/(x⁴ + 4)
> Show that $\displaystyle\int_{-\infty}^{\infty}\frac{x^3\sin ax}{x^4 + 4}\,dx = \pi e^{-a}\cos a$ for $a > 0$.
>
> **Zeros.** $z^4 = -4 = 4e^{i\pi}$ gives $z = \sqrt2e^{i(\pi/4 + k\pi/2)}$, that is, $\pm1 \pm i$; above the axis, $1 + i$ and $-1 + i$, both simple.
>
> **Residues.** By [[§83 Zeros and Poles|§83]] (Theorem 2), at each such zero $z_k$,
>
> $$
> \operatorname{Res}_{z=z_k}\frac{z^3e^{iaz}}{z^4 + 4} = \frac{z_k^3e^{iaz_k}}{4z_k^3} = \frac{e^{iaz_k}}{4} .
> $$
>
> The sum is $\frac14\big(e^{ia(1+i)} + e^{ia(-1+i)}\big) = \frac{e^{-a}}{4}\big(e^{ia} + e^{-ia}\big) = \frac{e^{-a}\cos a}{2}$, and $2\pi i$ times it is $i\pi e^{-a}\cos a$.
>
> **The arc.** On $C_R$ $(R > \sqrt2)$, $|f(z)| = \big|\frac{z^3}{z^4 + 4}\big| \le M_R = \frac{R^3}{R^4 - 4} \to 0$, while $M_R\,\pi R \to \pi$: here $\deg q = \deg p + 1$, and Jordan's lemma is needed.
>
> **Conclusion.** Taking imaginary parts, $\text{P.V.}\int_{-\infty}^{\infty}\frac{x^3\sin ax}{x^4 + 4}\,dx = \pi e^{-a}\cos a$; since the integrand is even, the two halves converge separately and this is the improper integral. (Quadrature: $0.624442$ at $a = 1$, $-0.206597$ at $a = 2.5$.) The real part gives $\text{P.V.}\int\frac{x^3\cos ax}{x^4 + 4}\,dx = 0$, as for any odd integrand.
>
> *B&C: Sec. 88, Exercise 5*

^ex-88-2

> [!example] Example §88.3: The Fresnel Integrals
> Evaluate the Fresnel integrals, which are important in diffraction theory:
>
> $$
> \int_0^\infty\cos(x^2)\,dx = \int_0^\infty\sin(x^2)\,dx = \frac12\sqrt{\frac\pi2} .
> $$
>
> **(a) A sector.** $\exp(iz^2)$ is entire. Integrate it around the boundary of the sector $0 \le r \le R$, $0 \le \theta \le \pi/4$, positively oriented. On the ray $z = re^{i\pi/4}$, $iz^2 = ir^2e^{i\pi/2} = -r^2$ and $dz = e^{i\pi/4}\,dr$. By the Cauchy–Goursat theorem ([[§50 Cauchy–Goursat Theorem|§50]]),
>
> $$
> \int_0^R e^{ix^2}\,dx + \int_{C_R} e^{iz^2}\,dz - e^{i\pi/4}\int_0^R e^{-r^2}\,dr = 0 ,
> $$
>
> where $C_R$ is the arc $z = Re^{i\theta}$ $(0 \le \theta \le \pi/4)$. Since $e^{i\pi/4} = (1 + i)/\sqrt2$, real and imaginary parts give
>
> $$
> \int_0^R\cos(x^2)\,dx = \frac{1}{\sqrt2}\int_0^R e^{-r^2}\,dr - \operatorname{Re}\int_{C_R} e^{iz^2}\,dz, \qquad \int_0^R\sin(x^2)\,dx = \frac{1}{\sqrt2}\int_0^R e^{-r^2}\,dr - \operatorname{Im}\int_{C_R} e^{iz^2}\,dz .
> $$
>
> **(b) The arc.** On $C_R$, $iz^2 = iR^2e^{i2\theta}$, so $|e^{iz^2}| = e^{-R^2\sin2\theta}$, and with $\phi = 2\theta$,
>
> $$
> \Big|\int_{C_R} e^{iz^2}\,dz\Big| \le R\int_0^{\pi/4} e^{-R^2\sin2\theta}\,d\theta = \frac R2\int_0^{\pi/2} e^{-R^2\sin\phi}\,d\phi < \frac R2\cdot\frac{\pi}{2R^2} = \frac{\pi}{4R} \to 0 ,
> $$
>
> by the form (2) of Jordan's inequality.
>
> **(c) The limit.** With $\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt\pi}{2}$, letting $R \to \infty$ in (a) shows that both Fresnel integrals converge and equal $\frac{1}{\sqrt2}\cdot\frac{\sqrt\pi}{2} = \frac12\sqrt{\frac\pi2} \approx 0.626657$, which quadrature confirms. The integrands do not tend to zero in absolute value at a fixed rate; the integrals converge only because the oscillations of $\cos(x^2)$ and $\sin(x^2)$ speed up.
>
> *B&C: Sec. 88, Exercise 12*

^ex-88-3

> [!remark]- Connections
> - The Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt\pi$ used in (c) is computed in polar coordinates in [[§15 Multivariable Integration#^ex-15-7|452 Ex. §15.7]]. The sector argument rotates the path of integration onto the ray where $e^{iz^2}$ becomes the Gaussian. The related move of shifting the Gaussian integral $\int e^{-(s - ki)^2}\,ds$ off the real axis, by Cauchy–Goursat on a long rectangle, is the "fact from complex analysis" behind the Fourier transform of a Gaussian in [[§15★ Complex Methods#^ex-15-3|341 Ex. §15.3]].
