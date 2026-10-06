---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: "90★"
bc: "90"
aliases: ["B&C 90"]
tags: [complex-variables, math342, extension]
---
← [[§89★ An Indented Path]] · ↑ [[· 7 Applications of Residues]] · [[§91★ Integration Along a Branch Cut]] →

*Brown–Churchill, Section 90.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

An indentation can also step around a **branch point**. To evaluate $\int_0^\infty x^a\,R(x)\,dx$ with a noninteger power, one integrates a branch of $z^a$ whose branch cut is placed away from the contour, here along the negative imaginary axis. The two legs of the indented semicircle then carry the same real integral, multiplied by $1$ and by $e^{ia\pi}$, because $\arg z$ is $0$ on one and $\pi$ on the other. Unlike the pole of §89, the branch point contributes nothing in the limit: near $0$ the integrand is only as large as $\rho^a$, and the small semicircle has length $\pi\rho$.

> [!example] Example §90.1: The Integral of xᵃ/(x² + 1)²
> Derive the integration formula
>
> $$
> \int_0^\infty\frac{x^a}{(x^2 + 1)^2}\,dx = \frac{(1 - a)\pi}{4\cos(a\pi/2)} \qquad (-1 < a < 3), \qquad (1)
> $$
>
> where $x^a = \exp(a\ln x)$ for $x > 0$. (For $a = 1$ the right side is read as its limit, $\frac12$; see Example §90.3.)
>
> **The branch and the contour.** Use
>
> $$
> f(z) = \frac{z^a}{(z^2 + 1)^2} = \frac{\exp(a\log z)}{(z^2 + 1)^2} \qquad \Big(|z| > 0,\ -\frac\pi2 < \arg z < \frac{3\pi}{2}\Big),
> $$
>
> whose branch cut is the origin together with the negative imaginary axis ([[§33 Branches and Derivatives of Logarithms#^def-33-4|Definition §33.4]]), and the indented contour of the figure below: $L_1$ from $\rho$ to $R$, the semicircle $C_R$ counterclockwise, $L_2$ from $-R$ to $-\rho$, and the semicircle $C_\rho$ clockwise, with $\rho < 1 < R$. The function $f$ is analytic inside and on this contour except at $z = i$. By the [[§76 Cauchy's Residue Theorem#^thm-76-1|residue theorem]],
>
> $$
> \int_{L_1} f(z)\,dz + \int_{L_2} f(z)\,dz = 2\pi i\operatorname{Res}_{z=i} f(z) - \int_{C_\rho} f(z)\,dz - \int_{C_R} f(z)\,dz . \qquad (2)
> $$
>
> **The legs.** $L_1$ and $-L_2$ have the parametrizations $z = re^{i0} = r$ and $z = re^{i\pi} = -r$ $(\rho \le r \le R)$. On $L_1$, $\log z = \ln r + i0$; on $-L_2$, $\log z = \ln r + i\pi$, and $dz = -dr$. Hence
>
> $$
> \int_{L_1} f(z)\,dz - \int_{-L_2} f(z)\,dz = \int_\rho^R\frac{\exp[a(\ln r + i0)]}{(r^2 + 1)^2}\,dr + \int_\rho^R\frac{\exp[a(\ln r + i\pi)]}{(r^2 + 1)^2}\,dr ,
> $$
>
> that is,
>
> $$
> \int_{L_1} f(z)\,dz + \int_{L_2} f(z)\,dz = \big(1 + e^{ia\pi}\big)\int_\rho^R\frac{r^a}{(r^2 + 1)^2}\,dr . \qquad (3)
> $$
>
> **The residue.** $z = i$ is a pole of order $m = 2$: $f(z) = \phi(z)/(z - i)^2$ with $\phi(z) = z^a/(z + i)^2$, analytic and nonzero at $i$, so $\operatorname{Res}_{z=i} f(z) = \phi'(i)$ (4) ([[§80 Residues at Poles#^thm-80-1|Theorem §80.1]]). Straightforward differentiation, using $\frac{d}{dz}z^a = az^{a-1}$ with $z^{a-1} = e^{(a-1)\log z}$ on the same branch ([[§35 The Power Function#^thm-35-2|Theorem §35.2]]), gives
>
> $$
> \phi'(z) = \frac{az^{a-1}}{(z + i)^2} - \frac{2z^a}{(z + i)^3} = e^{(a-1)\log z}\Big[\frac{(a - 2)z + ai}{(z + i)^3}\Big] .
> $$
>
> At $z = i$: $\log i = i\pi/2$, so $e^{(a-1)\log i} = e^{ia\pi/2}e^{-i\pi/2} = -ie^{ia\pi/2}$, and $\frac{(a - 2)i + ai}{(2i)^3} = \frac{(2a - 2)i}{-8i} = \frac{1 - a}{4}$. Therefore
>
> $$
> \operatorname{Res}_{z=i} f(z) = -ie^{ia\pi/2}\Big(\frac{1 - a}{4}\Big) . \qquad (5)
> $$
>
> Substituting (3) and (5) into (2),
>
> $$
> \big(1 + e^{ia\pi}\big)\int_\rho^R\frac{r^a}{(r^2 + 1)^2}\,dr = \frac{\pi(1 - a)}{2}e^{ia\pi/2} - \int_{C_\rho} f(z)\,dz - \int_{C_R} f(z)\,dz . \qquad (6)
> $$
>
> **The two semicircles.** We show
>
> $$
> \lim_{\rho\to0}\int_{C_\rho} f(z)\,dz = 0 \qquad\text{and}\qquad \lim_{R\to\infty}\int_{C_R} f(z)\,dz = 0 . \qquad (7)
> $$
>
> On the whole contour $z = re^{i\theta}$ with $0 \le \theta \le \pi$, and $|z^a| = |e^{a(\ln r + i\theta)}| = r^a$. On $C_\rho$, $|z^2 + 1| \ge \big||z|^2 - 1\big| = 1 - \rho^2$; on $C_R$, $|z^2 + 1| \ge R^2 - 1$. Hence
>
> $$
> \Big|\int_{C_\rho}\frac{z^a}{(z^2 + 1)^2}\,dz\Big| \le \frac{\rho^a}{(1 - \rho^2)^2}\,\pi\rho = \frac{\pi\rho^{a+1}}{(1 - \rho^2)^2} \to 0 \quad (\rho \to 0), \qquad\text{since } a + 1 > 0 ,
> $$
>
> $$
> \Big|\int_{C_R}\frac{z^a}{(z^2 + 1)^2}\,dz\Big| \le \frac{R^a}{(R^2 - 1)^2}\,\pi R = \frac{\pi R^{a+1}}{(R^2 - 1)^2} = \frac{\pi/R^{3-a}}{\big(1 - 1/R^2\big)^2} \to 0 \quad (R \to \infty), \qquad\text{since } 3 - a > 0 .
> $$
>
> *B&C prints the second limit in (7) as a second copy of the first, "$\lim_{\rho\to0}\int_{C_\rho}$" (p. 279); it is the limit over $C_R$ as $R \to \infty$, as the estimate that follows in B&C shows.*
>
> **Conclusion.** For $a \ne 1$ (so that $1 + e^{ia\pi} \ne 0$), letting $\rho \to 0$ and $R \to \infty$ in (6),
>
> $$
> \int_0^\infty\frac{r^a}{(r^2 + 1)^2}\,dr = \frac{\pi(1 - a)}{2}\cdot\frac{e^{ia\pi/2}}{1 + e^{ia\pi}}\cdot\frac{e^{-ia\pi/2}}{e^{-ia\pi/2}} = \frac{\pi(1 - a)}{4}\cdot\frac{2}{e^{ia\pi/2} + e^{-ia\pi/2}} = \frac{(1 - a)\pi}{4\cos(a\pi/2)} ,
> $$
>
> which is (1). The restriction $-1 < a < 3$ is exactly what the two estimates need, and it is also the condition for convergence: the integrand behaves like $x^a$ at $0$ and like $x^{a-4}$ at $\infty$. Quadrature confirms (1), for instance $0.617031$ at $a = 0.3$ and $2.940980$ at $a = 2.7$.
>
> *B&C: Sec. 90, Example*

^ex-90-1

![[m342-90-1.svg]]
*The contour of Example §90.1. The branch of $z^a$ with $-\pi/2 < \arg z < 3\pi/2$ has its cut along the origin and the negative imaginary axis (orange), below the contour; so it is analytic inside and on the contour except at the pole $z = i$ (green). On $L_1$, $\arg z = 0$; on $L_2$, $\arg z = \pi$, which produces the factor $e^{ia\pi}$.*

> [!remark] Remark: Method — Integrals with a Power xᵃ
> To evaluate $\int_0^\infty x^aR(x)\,dx$, with $R$ rational and $R(-x) = R(x)$ (so that both legs carry the same real integral):
> 1. **Choose the branch** of $z^a = e^{a\log z}$ with $-\pi/2 < \arg z < 3\pi/2$: its cut points down, away from the upper half plane and the real axis (except the origin).
> 2. **Indent** around the branch point $0$ with $C_\rho$, and close with $C_R$.
> 3. **Legs:** $\int_{L_1} + \int_{L_2} = (1 + e^{ia\pi})\int_\rho^R r^aR(r)\,dr$, using $\arg z = 0$ on $L_1$ and $\arg z = \pi$ on $L_2$.
> 4. **Residues** at the poles of $R$ in the upper half plane, evaluating $z^a$ on the chosen branch: $i^a = e^{ia\pi/2}$.
> 5. **Semicircles:** $|z^a| = |z|^a$; the small one vanishes if $a + 1 > 0$, the large one if $R(z) = O(|z|^{-k})$ with $a + 1 - k < 0$.
> 6. **Divide** by $1 + e^{ia\pi}$ and simplify with $e^{i\theta} + e^{-i\theta} = 2\cos\theta$.
>
> If $R$ is not even, the legs do not combine; the keyhole of [[§91★ Integration Along a Branch Cut#^prop-91-1|Proposition §91.1]] is then the right contour.

^rem-90-1

> [!example] Example §90.2: The Integral of 1/(√x (x² + 1))
> Derive $\displaystyle\int_0^\infty\frac{dx}{\sqrt x\,(x^2 + 1)} = \frac{\pi}{\sqrt2}$ by integrating
>
> $$
> f(z) = \frac{z^{-1/2}}{z^2 + 1} = \frac{e^{(-1/2)\log z}}{z^2 + 1} \qquad \Big(|z| > 0,\ -\frac\pi2 < \arg z < \frac{3\pi}{2}\Big)
> $$
>
> over the contour of Example §90.1.
>
> **Legs.** On $L_1$, $z^{-1/2} = r^{-1/2}$; on $L_2$, $z^{-1/2} = r^{-1/2}e^{-i\pi/2} = -ir^{-1/2}$. So $\int_{L_1} f + \int_{L_2} f = (1 - i)\int_\rho^R\frac{dr}{\sqrt r\,(r^2 + 1)}$.
>
> **Residue.** $z = i$ is a simple pole, and with $i^{-1/2} = e^{-i\pi/4}$,
>
> $$
> \operatorname{Res}_{z=i} f(z) = \frac{z^{-1/2}}{2z}\Big|_{z=i} = \frac{e^{-i\pi/4}}{2i}, \qquad 2\pi i\operatorname{Res}_{z=i} f(z) = \pi e^{-i\pi/4} = \frac{\pi(1 - i)}{\sqrt2} .
> $$
>
> **Semicircles.** $\big|\int_{C_\rho} f\big| \le \frac{\rho^{-1/2}\pi\rho}{1 - \rho^2} = \frac{\pi\sqrt\rho}{1 - \rho^2} \to 0$ and $\big|\int_{C_R} f\big| \le \frac{R^{-1/2}\pi R}{R^2 - 1} \to 0$.
>
> **Conclusion.** $(1 - i)\int_0^\infty\frac{dx}{\sqrt x\,(x^2 + 1)} = \frac{\pi(1 - i)}{\sqrt2}$, so the integral is $\frac{\pi}{\sqrt2} \approx 2.221441$, as quadrature confirms. [[§91★ Integration Along a Branch Cut#^ex-91-2|Example §91.2]] obtains it again with a keyhole contour.
>
> *B&C: Sec. 91, Exercise 2*

^ex-90-2

> [!example] Example §90.3: Checks on the Formula
> Test formula (1) against integrals known otherwise.
>
> **$a = 0$.** (1) gives $\frac{\pi}{4\cos0} = \frac\pi4$, which is $\int_0^\infty\frac{dx}{(x^2 + 1)^2}$, B&C's Exercise 2 of §86 (residue $\frac{d}{dz}(z + i)^{-2}\big|_{z=i} = \frac{-2}{(2i)^3} = \frac{1}{4i}$, and $\pi i\cdot\frac{1}{4i} = \frac\pi4$).
>
> **$a = 2$.** (1) gives $\frac{-\pi}{4\cos\pi} = \frac\pi4$, so $\int_0^\infty\frac{x^2\,dx}{(x^2 + 1)^2} = \frac\pi4$ as well. This is no accident: the substitution $x = 1/t$ turns $\int_0^\infty\frac{x^a\,dx}{(x^2 + 1)^2}$ into $\int_0^\infty\frac{t^{2-a}\,dt}{(t^2 + 1)^2}$, and the right side of (1) is unchanged under $a \mapsto 2 - a$, since $\frac{(a - 1)}{\cos((2 - a)\pi/2)} = \frac{a - 1}{-\cos(a\pi/2)}$.
>
> **$a = 1$.** Here $1 + e^{ia\pi} = 0$ and the derivation divides by zero; the integral is elementary, $\int_0^\infty\frac{x\,dx}{(x^2 + 1)^2} = \Big[-\frac{1}{2(x^2 + 1)}\Big]_0^\infty = \frac12$. The right side of (1) tends to the same value: as $a \to 1$, $\cos(a\pi/2) = \sin\big((1 - a)\pi/2\big) \sim (1 - a)\pi/2$, so $\frac{(1 - a)\pi}{4\cos(a\pi/2)} \to \frac{\pi}{4\cdot\pi/2} = \frac12$. So (1) holds at $a = 1$ when its right side is read as this limit.
>
> *B&C: Sec. 90, Example (special cases); Sec. 86, Exercise 2*

^ex-90-3
