---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: 91
bc: "91"
aliases: ["B&C 91"]
tags: [complex-variables, math342, extension]
---
← [[§90★ An Indentation Around a Branch Point]] · ↑ [[· 7 Applications of Residues]] · [[§92★ Definite Integrals Involving Sines and Cosines]] →

*Brown–Churchill, Section 91.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Here part of the path of integration lies **along** a branch cut. For $\int_0^\infty x^{-a}/(x + 1)\,dx$ one takes the branch of $z^{-a}$ cut along the positive real axis and integrates around a "keyhole": out along the upper edge of the cut, around a large circle, back along the lower edge, and around a small circle. The two edges carry the same real integral with the factors $1$ and $e^{-i2a\pi}$, since $\arg z$ is $0$ on one and $2\pi$ on the other, so the jump of the branch across the cut is what produces the answer. Since the function is not even defined on the cut, the residue theorem cannot be applied to the keyhole literally; B&C's Exercise 6, proved below as a proposition, cuts the region in two and makes the step rigorous. The integral evaluated, $\pi/\sin a\pi$, is the reflection formula of the gamma and beta functions.

## The Keyhole Contour

Let $0 < a < 1$, let $C_\rho$ and $C_R$ be the circles $|z| = \rho$ and $|z| = R$ with $\rho < 1 < R$, $C_R$ counterclockwise and $C_\rho$ clockwise, and consider the branch

$$
f(z) = \frac{z^{-a}}{z + 1} = \frac{\exp(-a\log z)}{z + 1} \qquad (|z| > 0,\ 0 < \arg z < 2\pi) \qquad (2)
$$

of the multiple-valued function $z^{-a}/(z + 1)$, with branch cut $\arg z = 0$. The **keyhole contour** of the figure below is traced by a point moving from $\rho$ to $R$ along the top of the cut, then around $C_R$ back to $R$, then along the bottom of the cut to $\rho$, and finally around $C_\rho$ back to $\rho$. With $z = re^{i\theta}$,

$$
f(z) = \frac{\exp[-a(\ln r + i\theta)]}{re^{i\theta} + 1} ,
$$

and its limiting values on the two edges of the cut annulus, where $\theta = 0$ and $\theta = 2\pi$, are

$$
\frac{\exp[-a(\ln r + i0)]}{r + 1} = \frac{r^{-a}}{r + 1} \quad (\text{upper edge}), \qquad \frac{\exp[-a(\ln r + i2\pi)]}{r + 1} = \frac{r^{-a}e^{-i2a\pi}}{r + 1} \quad (\text{lower edge}) .
$$

On $C_R$ and $C_\rho$ the integrals of $f$ are taken with $0 < \theta < 2\pi$ (the single point $\theta = 0$ does not affect them).

> [!theorem] Proposition §91.1: The Residue Theorem on the Keyhole
> With $f$, $C_\rho$ and $C_R$ as above,
>
> $$
> \int_\rho^R\frac{r^{-a}}{r + 1}\,dr + \int_{C_R} f(z)\,dz - \int_\rho^R\frac{r^{-a}e^{-i2a\pi}}{r + 1}\,dr + \int_{C_\rho} f(z)\,dz = 2\pi i\operatorname*{Res}_{z=-1} f(z) . \qquad (3)
> $$
>
> *B&C: Sec. 91, Exercise 6 (equation (3) of the text, which B&C obtains formally there)*

^prop-91-1

> [!proof]+ Proof
> $f$ is not analytic, or even defined, on the cut, so (3) is not an instance of the residue theorem. Split the annulus along a ray $\arg z = \theta_0$ with $\pi < \theta_0 < 3\pi/2$, and use on each half a branch that is analytic on all of it.
>
> **(a) The left contour.** $\Gamma_1$ runs from $\rho$ to $R$ along the positive real axis, along $C_R$ counterclockwise from $\theta = 0$ to $\theta = \theta_0$ (call this arc $\Gamma_R$), inward along the ray from $Re^{i\theta_0}$ to $\rho e^{i\theta_0}$ (call this segment $L$), and along $C_\rho$ clockwise from $\theta_0$ back to $0$ (the arc $\Gamma_\rho$). It bounds the region $\rho < |z| < R$, $0 < \arg z < \theta_0$, which contains $-1$ (argument $\pi < \theta_0$). The branch
>
> $$
> f_1(z) = \frac{z^{-a}}{z + 1} \qquad \Big(|z| > 0,\ -\frac\pi2 < \arg z < \frac{3\pi}{2}\Big)
> $$
>
> is analytic on and inside $\Gamma_1$ except at $-1$, since all points there have arguments in $[0, \theta_0] \subset (-\pi/2, 3\pi/2)$. On the positive real axis $f_1(r) = r^{-a}/(r + 1)$. Cauchy's residue theorem gives
>
> $$
> \int_\rho^R\frac{r^{-a}}{r + 1}\,dr + \int_{\Gamma_R} f_1(z)\,dz + \int_L f_1(z)\,dz + \int_{\Gamma_\rho} f_1(z)\,dz = 2\pi i\operatorname*{Res}_{z=-1} f_1(z) .
> $$
>
> **(b) The right contour.** $\Gamma_2$ runs outward along the same ray (that is, along $-L$), along $C_R$ counterclockwise from $\theta_0$ to $2\pi$ (the arc $\gamma_R$), from $R$ to $\rho$ along the positive real axis approached from below, and along $C_\rho$ clockwise from $2\pi$ back to $\theta_0$ (the arc $\gamma_\rho$). It bounds the region $\rho < |z| < R$, $\theta_0 < \arg z < 2\pi$, which contains no singular point. The branch
>
> $$
> f_2(z) = \frac{z^{-a}}{z + 1} \qquad \Big(|z| > 0,\ \frac\pi2 < \arg z < \frac{5\pi}{2}\Big)
> $$
>
> is analytic on and inside $\Gamma_2$, since the arguments there lie in $[\theta_0, 2\pi] \subset (\pi/2, 5\pi/2)$; on the positive real axis it takes $\arg z = 2\pi$, so $f_2(r) = r^{-a}e^{-i2a\pi}/(r + 1)$. The Cauchy–Goursat theorem ([[§50 Cauchy–Goursat Theorem|§50]]) gives
>
> $$
> -\int_\rho^R\frac{r^{-a}e^{-i2a\pi}}{r + 1}\,dr + \int_{\gamma_\rho} f_2(z)\,dz - \int_L f_2(z)\,dz + \int_{\gamma_R} f_2(z)\,dz = 0 .
> $$
>
> **(c) Adding.** The three branches $f$, $f_1$, $f_2$ use the same value of $\arg z$ wherever their ranges overlap: on the closed region of (a) away from the positive real axis, $0 < \arg z \le \theta_0$, so $f_1 = f$ there; on the region of (b) away from the positive real axis, $\theta_0 \le \arg z < 2\pi$, so $f_2 = f$. In particular $f_1 = f_2 = f$ on the ray $L$, so the two integrals over $L$ cancel when the equations are added; $\Gamma_R$ and $\gamma_R$ together make up $C_R$, and $\Gamma_\rho$ and $\gamma_\rho$ make up $C_\rho$, on which $f_1$ or $f_2$ may be replaced by $f$; and $f_1 = f$ near $-1$, so their residues there agree. Adding the two equations gives (3).

^prop-91-1-pf

^pf-91-1

*Uses:* [[§76 Cauchy's Residue Theorem|§76]] (Theorem), [[§50 Cauchy–Goursat Theorem|§50]] (Theorem), [[§33 Branches and Derivatives of Logarithms|§33]], [[§35 The Power Function|§35]]

![[m342-91-1.svg]]
*The keyhole contour of §91. The branch $z^{-a}$ with $0 < \arg z < 2\pi$ is cut along the positive real axis (orange); the contour runs out along the upper edge ($\theta = 0$), around $C_R$, back along the lower edge ($\theta = 2\pi$) and around $C_\rho$ clockwise. It encloses the pole $-1$ (green). Proposition §91.1 justifies the residue theorem on it by splitting along a ray in the third quadrant.*

> [!remark] Remark: Method — Integration Along a Branch Cut
> To evaluate $\int_0^\infty x^{-a}R(x)\,dx$ (or with $x^{a}$, $\sqrt x$, $\sqrt[3]x$), $R$ rational with no poles on $[0, \infty)$:
> 1. **Take the branch with $0 < \arg z < 2\pi$**, cut along the positive real axis, and the keyhole contour.
> 2. **Edges:** the upper edge gives $\int_\rho^R r^{-a}R(r)\,dr$, the lower edge $-e^{-i2a\pi}\int_\rho^R r^{-a}R(r)\,dr$; together $(1 - e^{-i2a\pi})\int_\rho^R$. (Proposition §91.1, whose proof works for any such $R$.)
> 3. **Residues** at all poles of $R$ in the plane (not only the upper half), with $\arg$ taken in $(0, 2\pi)$: for instance $(-1)^{-a} = e^{-ia\pi}$ and $i^{-a} = e^{-ia\pi/2}$, but $(-i)^{-a} = e^{-i3a\pi/2}$.
> 4. **Circles:** $|z^{-a}| = |z|^{-a}$; $\int_{C_\rho} \to 0$ and $\int_{C_R} \to 0$ under the convergence conditions at $0$ and $\infty$.
> 5. **Divide** by $1 - e^{-i2a\pi}$.
>
> Compared with [[§90★ An Indentation Around a Branch Point#^rem-90-1|the indented semicircle]], the keyhole does not need $R$ to be even, at the price of residues in the lower half plane.

^rem-91-1

## Examples

> [!example] Example §91.1: The Integral of x⁻ᵃ/(x + 1)
> Let $x^{-a}$, where $x > 0$ and $0 < a < 1$, denote the principal value $\exp(-a\ln x)$. Evaluate
>
> $$
> \int_0^\infty\frac{x^{-a}}{x + 1}\,dx \qquad (0 < a < 1), \qquad (1)
> $$
>
> an integral that is improper at both ends: the integrand behaves like $x^{-a}$ near $0$ and like $x^{-a-1}$ at $\infty$, so it converges when $0 < a < 1$ (convergence also follows from the evaluation).
>
> **The residue.** $\phi(z) = z^{-a} = \exp[-a(\ln r + i\theta)]$ $(r > 0,\ 0 < \theta < 2\pi)$ is analytic at $z = -1$ with $\phi(-1) = \exp[-a(\ln1 + i\pi)] = e^{-ia\pi} \ne 0$. So $z = -1$ is a simple pole of $f = \phi/(z + 1)$ and $\operatorname{Res}_{z=-1} f(z) = e^{-ia\pi}$. By Proposition §91.1,
>
> $$
> \big(1 - e^{-i2a\pi}\big)\int_\rho^R\frac{r^{-a}}{r + 1}\,dr = 2\pi ie^{-ia\pi} - \int_{C_\rho} f(z)\,dz - \int_{C_R} f(z)\,dz . \qquad (4)
> $$
>
> **The circles.** On $C_\rho$, $|z^{-a}| = \rho^{-a}$ and $|z + 1| \ge 1 - \rho$; on $C_R$, $|z^{-a}| = R^{-a}$ and $|z + 1| \ge R - 1$. So
>
> $$
> \Big|\int_{C_\rho} f(z)\,dz\Big| \le \frac{\rho^{-a}}{1 - \rho}\,2\pi\rho = \frac{2\pi}{1 - \rho}\,\rho^{1-a}, \qquad \Big|\int_{C_R} f(z)\,dz\Big| \le \frac{R^{-a}}{R - 1}\,2\pi R = \frac{2\pi R}{R - 1}\cdot\frac{1}{R^a} ,
> $$
>
> and since $0 < a < 1$ these tend to $0$ as $\rho \to 0$ and $R \to \infty$.
>
> **Conclusion.** Letting $\rho \to 0$ and then $R \to \infty$ in (4),
>
> $$
> \big(1 - e^{-i2a\pi}\big)\int_0^\infty\frac{r^{-a}}{r + 1}\,dr = 2\pi ie^{-ia\pi}, \qquad \int_0^\infty\frac{r^{-a}}{r + 1}\,dr = 2\pi i\,\frac{e^{-ia\pi}}{1 - e^{-i2a\pi}}\cdot\frac{e^{ia\pi}}{e^{ia\pi}} = \frac{\pi}{\big(e^{ia\pi} - e^{-ia\pi}\big)/2i} ,
> $$
>
> and with $\sin a\pi = (e^{ia\pi} - e^{-ia\pi})/2i$,
>
> $$
> \int_0^\infty\frac{x^{-a}}{x + 1}\,dx = \frac{\pi}{\sin a\pi} \qquad (0 < a < 1) . \qquad (5)
> $$
>
> For $a = \frac12$ this is $\pi$, which the substitution $x = u^2$ confirms: $\int_0^\infty\frac{2\,du}{u^2 + 1} = \pi$. Quadrature confirms other values ($4.44288$ at $a = \frac14$).
>
> *B&C: Sec. 91, Example*

^ex-91-1

> [!example] Example §91.2: The Integral of 1/(√x (x² + 1)) Again
> Derive $\displaystyle\int_0^\infty\frac{dx}{\sqrt x\,(x^2 + 1)} = \frac{\pi}{\sqrt2}$ by integrating the branch
>
> $$
> f(z) = \frac{z^{-1/2}}{z^2 + 1} = \frac{e^{(-1/2)\log z}}{z^2 + 1} \qquad (|z| > 0,\ 0 < \arg z < 2\pi)
> $$
>
> around the keyhole contour.
>
> **Edges.** By Proposition §91.1 (its proof applies verbatim with $z^2 + 1$ in place of $z + 1$; the splitting ray may be taken with $3\pi/2 < \theta_0 < 2\pi$, so that $\pm i$ both lie in the left part), the edges give $\big(1 - e^{-i\pi}\big)\int_\rho^R\frac{dr}{\sqrt r\,(r^2 + 1)} = 2\int_\rho^R\frac{dr}{\sqrt r\,(r^2 + 1)}$.
>
> **Residues.** Both $i = e^{i\pi/2}$ and $-i = e^{i3\pi/2}$ lie inside, and with arguments in $(0, 2\pi)$, $i^{-1/2} = e^{-i\pi/4}$ and $(-i)^{-1/2} = e^{-i3\pi/4}$:
>
> $$
> \operatorname*{Res}_{z=i} f = \frac{e^{-i\pi/4}}{2i}, \qquad \operatorname*{Res}_{z=-i} f = \frac{e^{-i3\pi/4}}{-2i}, \qquad 2\pi i\big(\operatorname{Res} + \operatorname{Res}\big) = \pi\big(e^{-i\pi/4} - e^{-i3\pi/4}\big) = \pi\Big(\frac{1 - i}{\sqrt2} - \frac{-1 - i}{\sqrt2}\Big) = \pi\sqrt2 .
> $$
>
> **Circles.** $\big|\int_{C_\rho}\big| \le \frac{\rho^{-1/2}2\pi\rho}{1 - \rho^2} \to 0$, $\big|\int_{C_R}\big| \le \frac{R^{-1/2}2\pi R}{R^2 - 1} \to 0$.
>
> **Conclusion.** $2\int_0^\infty\frac{dx}{\sqrt x\,(x^2 + 1)} = \pi\sqrt2$, so the integral is $\frac{\pi}{\sqrt2}$, as found in [[§90★ An Indentation Around a Branch Point#^ex-90-2|Example §90.2]] with the indented semicircle.
>
> *B&C: Sec. 91, Exercise 3*

^ex-91-2

> [!example] Example §91.3: A Cube Root and Two Poles
> Derive, for $a > b > 0$,
>
> $$
> \int_0^\infty\frac{\sqrt[3]{x}}{(x + a)(x + b)}\,dx = \frac{2\pi}{\sqrt3}\cdot\frac{\sqrt[3]{a} - \sqrt[3]{b}}{a - b} ,
> $$
>
> using $f(z) = \dfrac{z^{1/3}}{(z + a)(z + b)} = \dfrac{e^{(1/3)\log z}}{(z + a)(z + b)}$ $(|z| > 0,\ 0 < \arg z < 2\pi)$ and a keyhole contour with $\rho < b < a < R$.
>
> **Edges.** Here the exponent is $+\frac13$, so the lower edge carries $e^{i2\pi/3}$: $\int_{\text{edges}} = \big(1 - e^{i2\pi/3}\big)\int_\rho^R\frac{r^{1/3}\,dr}{(r + a)(r + b)}$.
>
> **Residues.** Both poles $-a$, $-b$ have argument $\pi$, so $(-a)^{1/3} = \sqrt[3]{a}\,e^{i\pi/3}$ and $(-b)^{1/3} = \sqrt[3]{b}\,e^{i\pi/3}$:
>
> $$
> \operatorname*{Res}_{z=-a} f + \operatorname*{Res}_{z=-b} f = \frac{\sqrt[3]{a}\,e^{i\pi/3}}{b - a} + \frac{\sqrt[3]{b}\,e^{i\pi/3}}{a - b} = -e^{i\pi/3}\,\frac{\sqrt[3]{a} - \sqrt[3]{b}}{a - b} .
> $$
>
> **Circles.** $|f| \le \rho^{1/3}/((a - \rho)(b - \rho))$ on $C_\rho$ and $\le R^{1/3}/((R - a)(R - b))$ on $C_R$; times the lengths $2\pi\rho$, $2\pi R$, both tend to $0$.
>
> **Conclusion.** $1 - e^{i2\pi/3} = -i\sqrt3\,e^{i\pi/3}$ (as in [[§86 Example (Evaluation of Improper Integrals)#^ex-86-5|Example §86.5]]), so
>
> $$
> \int_0^\infty\frac{\sqrt[3]{x}\,dx}{(x + a)(x + b)} = \frac{2\pi i\cdot\big(-e^{i\pi/3}\big)}{-i\sqrt3\,e^{i\pi/3}}\cdot\frac{\sqrt[3]{a} - \sqrt[3]{b}}{a - b} = \frac{2\pi}{\sqrt3}\cdot\frac{\sqrt[3]{a} - \sqrt[3]{b}}{a - b} .
> $$
>
> Quadrature confirms it ($0.802152$ for $a = 3$, $b = 1$).
>
> *B&C: Sec. 91, Exercise 4*

^ex-91-3

> [!example] Example §91.4: The Beta Function B(p, 1 − p)
> The **beta function** is $B(p, q) = \int_0^1 t^{p-1}(1 - t)^{q-1}\,dt$ $(p > 0,\ q > 0)$. Show that
>
> $$
> B(p, 1 - p) = \frac{\pi}{\sin(p\pi)} \qquad (0 < p < 1) .
> $$
>
> Substitute $t = 1/(x + 1)$: as $x$ runs from $\infty$ to $0$, $t$ runs from $0$ to $1$; $1 - t = x/(x + 1)$ and $dt = -dx/(x + 1)^2$. Hence
>
> $$
> B(p, 1 - p) = \int_0^1 t^{p-1}(1 - t)^{-p}\,dt = \int_0^\infty (x + 1)^{1-p}\Big(\frac{x}{x + 1}\Big)^{-p}\frac{dx}{(x + 1)^2} = \int_0^\infty\frac{x^{-p}}{x + 1}\,dx ,
> $$
>
> since the powers of $x + 1$ combine to $(x + 1)^{1 - p + p - 2} = (x + 1)^{-1}$. By (5) with $a = p$ this is $\pi/\sin(p\pi)$. In terms of the gamma function, $B(p, 1 - p) = \Gamma(p)\Gamma(1 - p)$, so this is Euler's reflection formula $\Gamma(p)\Gamma(1 - p) = \pi/\sin p\pi$ (B&C's reason for calling (1) important in the study of the gamma function); at $p = \frac12$ it gives $\Gamma(\frac12) = \sqrt\pi$.
>
> *B&C: Sec. 91, Exercise 5*

^ex-91-4
