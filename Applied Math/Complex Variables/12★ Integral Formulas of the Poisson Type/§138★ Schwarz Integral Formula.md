---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 138
bc: "138"
aliases: ["B&C 138"]
tags: [complex-variables, math342, extension]
---
← [[§137★ Related Boundary Value Problems]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§139★ Dirichlet Problem for a Half Plane]] →

*Brown–Churchill, Section 138.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This is the half-plane analog of [[§134★ Poisson Integral Formula|§134★]]. For a function analytic in the closed upper half plane that decays like $|z|^{-a}$, the Cauchy integral formula on large half disks becomes a Cauchy integral formula over the real axis. Because the same integral vanishes at points below the axis, the conjugate point $\overline z$ plays the role of the inverse point: adding or subtracting the integral at $\overline z$ produces real kernels, and taking real and imaginary parts gives the Schwarz integral formula (the Poisson integral formula for the half plane) for $u$, and an integral for its harmonic conjugate $v$, both in terms of the boundary values of $u$ alone.

> [!theorem] Theorem §138.1: Cauchy Integral Formula for the Half Plane
> Let $f$ be analytic throughout the half plane $\operatorname{Im} z \ge 0$, and suppose that for some positive constants $a$ and $M$ the order property
>
> $$
> |z^af(z)| < M \qquad (\operatorname{Im} z \ge 0) \qquad (1)
> $$
>
> holds. Then
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{-\infty}^{\infty}\frac{f(t)\,dt}{t - z} \qquad (\operatorname{Im} z > 0) , \qquad (3)
> $$
>
> the improper integral converging (to the same number as its Cauchy principal value). When $z$ lies below the real axis, the integral in (3) is zero.
>
> *B&C: Sec. 138, equation (3)*

^thm-138-1

> [!proof]+ Proof
> Fix $z$ above the real axis, and let $C_R$ be the upper half of the positively oriented circle of radius $R > |z|$ centered at the origin. By the Cauchy integral formula ([[§54 Cauchy Integral Formula|§54]]) applied to the closed contour formed by $C_R$ and the segment $-R \le t \le R$,
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{C_R}\frac{f(s)\,ds}{s - z} + \frac{1}{2\pi i}\int_{-R}^{R}\frac{f(t)\,dt}{t - z} . \qquad (2)
> $$
>
> On $C_R$, $|f(s)| < M/R^a$ by (1) and $|s - z| \ge R - |z|$, so by the ML-inequality
>
> $$
> \Big|\int_{C_R}\frac{f(s)\,ds}{s - z}\Big| < \frac{M}{R^a(R - |z|)}\pi R = \frac{\pi M}{R^a(1 - |z|/R)} \longrightarrow 0 \qquad (R \to \infty) .
> $$
>
> So the second integral in (2) tends to $f(z)$ as $R \to \infty$. (B&C cites a calculus text for the convergence of the improper integral; here is why.) For $|t| \ge 2|z|$, $|t - z| \ge |t|/2$, so $|f(t)/(t - z)| < 2M/|t|^{1 + a}$, which is integrable at $\pm\infty$ since $a > 0$; so the real and imaginary parts of the integrand are absolutely integrable over the line, the improper integral converges, and its value is the limit of the symmetric integrals, its Cauchy principal value ([[§85 Evaluation of Improper Integrals|§85]]). This gives (3), a **Cauchy integral formula for the half plane** $\operatorname{Im} z > 0$.
>
> If $z$ lies below the real axis, $f(s)/(s - z)$ is analytic inside and on the closed contour of (2), so by the Cauchy–Goursat theorem ([[§50 Cauchy–Goursat Theorem|§50]]) the right side of (2) is zero for every $R$; the same limit shows that the integral in (3) is zero.

^pf-138-1

*Uses:* [[§54 Cauchy Integral Formula|§54]] (Cauchy integral formula), [[§50 Cauchy–Goursat Theorem|§50]], [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (ML-inequality), [[§85 Evaluation of Improper Integrals|§85]] (principal value), [[§36 Improper Integrals#^thm-36-1|451 Thm. §36.1]] (comparison for improper integrals)

> [!theorem] Theorem §138.2: Schwarz Integral Formula
> Let $f = u + iv$ satisfy the hypotheses of Theorem §138.1, and let $z = x + iy$ with $y > 0$. For every complex constant $c$,
>
> $$
> f(z) = \frac{1}{2\pi i}\int_{-\infty}^{\infty}\Big(\frac{1}{t - z} + \frac{c}{t - \overline z}\Big)f(t)\,dt \qquad (\operatorname{Im} z > 0) . \qquad (4)
> $$
>
> In the cases $c = -1$ and $c = 1$ this reduces to
>
> $$
> f(z) = \frac1\pi\int_{-\infty}^{\infty}\frac{y\,f(t)}{|t - z|^2}\,dt \quad (y > 0) \qquad (5) \qquad\text{and}\qquad f(z) = \frac{1}{\pi i}\int_{-\infty}^{\infty}\frac{(t - x)f(t)}{|t - z|^2}\,dt \quad (y > 0) . \qquad (6)
> $$
>
> Consequently the harmonic functions $u$ and $v$ are represented in the half plane $y > 0$ in terms of the boundary values of $u$ by
>
> $$
> u(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{y\,u(t, 0)}{|t - z|^2}\,dt = \frac1\pi\int_{-\infty}^{\infty}\frac{y\,u(t, 0)}{(t - x)^2 + y^2}\,dt \qquad (y > 0) \qquad (7)
> $$
>
> and
>
> $$
> v(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{(x - t)\,u(t, 0)}{(t - x)^2 + y^2}\,dt \qquad (y > 0) . \qquad (8)
> $$
>
> Expression (7) is the **Schwarz integral formula**, or the **Poisson integral formula for the half plane**.
>
> *B&C: Sec. 138, equations (4)–(8)*

^thm-138-2

> [!proof]+ Proof
> **(4).** If $y > 0$, then $\overline z$ lies below the real axis, so by Theorem §138.1 $\int_{-\infty}^\infty f(t)\,dt/(t - \overline z) = 0$. Adding $c$ times this zero to (3) gives (4).
>
> **(5) and (6).** For real $t$, $(t - z)(t - \overline z) = |t - z|^2$. With $c = -1$,
>
> $$
> \frac{1}{t - z} - \frac{1}{t - \overline z} = \frac{z - \overline z}{|t - z|^2} = \frac{2iy}{|t - z|^2} ,
> $$
>
> and dividing by $2\pi i$ gives the kernel $y/(\pi|t - z|^2)$ of (5). With $c = 1$,
>
> $$
> \frac{1}{t - z} + \frac{1}{t - \overline z} = \frac{2t - z - \overline z}{|t - z|^2} = \frac{2(t - x)}{|t - z|^2} ,
> $$
>
> which gives (6).
>
> **(7) and (8).** On the real axis $f(t) = u(t, 0) + iv(t, 0)$. The kernel of (5) is real, so the real part of (5) is (7). In (6), $\frac{1}{\pi i}(t - x)\big(u(t, 0) + iv(t, 0)\big) = \frac1\pi(t - x)\big(v(t, 0) - iu(t, 0)\big)$, whose imaginary part is $-\frac1\pi(t - x)u(t, 0)$; so the imaginary part of (6) is (8). Taking real and imaginary parts under the integral sign is allowed because the improper integrals converge absolutely.

^pf-138-2

*Uses:* [[§138★ Schwarz Integral Formula#^thm-138-1|§138.1]]

> [!remark]- Connections
> - The same half-plane formula (7) is reached in Fourier Series and PDEs by separation of variables: the product solutions $e^{-\lambda y}\cos\lambda x$, $e^{-\lambda y}\sin\lambda x$ are superposed in a Fourier integral, and the $\lambda$-integral is summed under the integral sign; see [[§38 Potential in Unbounded Regions#^rem-38-2|341 Remark: The Half-Plane and Its Poisson Formula]]. Here it comes from the Cauchy integral formula, with $\overline z$ playing the role of the inverse point of [[§134★ Poisson Integral Formula#^def-134-1|Definition §134.1]].

In [[§139★ Dirichlet Problem for a Half Plane|§139★]] the conditions for the validity of (7) and (8) are relaxed.

## Examples

> [!example] Example §138.1: The Formulas for f(z) = i/(z + i)
> Verify (7) and (8) for $f(z) = i/(z + i)$.
>
> **Hypotheses.** $f$ is analytic for $\operatorname{Im} z > -1$, hence throughout $\operatorname{Im} z \ge 0$. There $|z + i| \ge |z|$ and $|z + i| \ge 1$, so $|zf(z)| = |z|/|z + i| \le 1 < 2$: (1) holds with $a = 1$, $M = 2$.
>
> **Boundary values.** $f(t) = \dfrac{i}{t + i} = \dfrac{i(t - i)}{t^2 + 1} = \dfrac{1 + it}{1 + t^2}$, so $u(t, 0) = \dfrac{1}{1 + t^2}$.
>
> **Inside.** $f(z) = \dfrac{i}{x + i(y + 1)} = \dfrac{i\big(x - i(y + 1)\big)}{x^2 + (y + 1)^2} = \dfrac{(y + 1) + ix}{x^2 + (y + 1)^2}$, so
>
> $$
> u(x, y) = \frac{y + 1}{x^2 + (y + 1)^2}, \qquad v(x, y) = \frac{x}{x^2 + (y + 1)^2} .
> $$
>
> Formula (7) therefore asserts
>
> $$
> \frac1\pi\int_{-\infty}^{\infty}\frac{y}{(t - x)^2 + y^2}\cdot\frac{1}{1 + t^2}\,dt = \frac{y + 1}{x^2 + (y + 1)^2} :
> $$
>
> averaging the boundary values $\frac{1}{1 + t^2}$ (which are $\pi$ times the kernel at height $1$ above $0$) with the kernel at height $y$ gives $\pi$ times the kernel at height $y + 1$. At $(x, y) = (0.7, 0.4)$, quadrature of (7) and (8) gives $u = 0.571429 = 1.4/2.45$ and $v = 0.285714 = 0.7/2.45$, as the closed forms require.
>
> *B&C: Sec. 138, equations (7)–(8)*

^ex-138-1

> [!example] Example §138.2: Formula (3) by Residues
> For $f(z) = i/(z + i)$, evaluate the integral in (3) by residues, above and below the axis.
>
> The integrand $\dfrac{i}{(t + i)(t - z)}$ is $O(|t|^{-2})$, so by the method of [[§85 Evaluation of Improper Integrals|§85]] its integral over the real line equals $2\pi i$ times the sum of the residues in the upper half plane ([[§76 Cauchy's Residue Theorem|§76]]); the integral over the large semicircle tends to $0$.
>
> - If $\operatorname{Im} z > 0$, the only pole above the axis is $t = z$, with residue $\dfrac{i}{z + i}$; so $\dfrac{1}{2\pi i}\displaystyle\int_{-\infty}^{\infty}\frac{f(t)\,dt}{t - z} = \frac{i}{z + i} = f(z)$, which is (3).
> - If $\operatorname{Im} z < 0$, both poles $t = -i$ and $t = z$ lie below the axis, so the integral is $0$, as Theorem §138.1 asserts. This vanishing is what makes (4) hold for every $c$.
>
> *B&C: Sec. 138, equations (3)–(4)*

^ex-138-2

> [!example] Example §138.3: Constants and the Order Property
> Test (3), (7) and (8) on the constants $f \equiv 1$ and $f \equiv i$, which do not satisfy (1).
>
> **$f \equiv 1$.** Formula (3) fails: for $y > 0$ the improper integral $\int_{-\infty}^\infty dt/(t - z)$ diverges (its integrand is not $O(|t|^{-1-a})$), and its principal value is $\lim_{R\to\infty}\big[\log(t - z)\big]_{t=-R}^{t=R} = i\pi$ (the argument of $t - z$ runs from $-\pi$ to $0$), so the right side of (3) would be $\frac12$, not $1$. Formula (7), however, gives $u = \frac1\pi\int y\,dt/\big((t - x)^2 + y^2\big) = \frac1\pi\big[\arctan\frac{t - x}{y}\big]_{-\infty}^{\infty} = 1$, correctly.
>
> **$f \equiv i$.** Here $u = 0$ and $v = 1$. Formula (7) gives $0$, correctly, but (8) gives $v = 0$, not $1$: (8) determines the conjugate only up to an additive constant, and the order property is what pins the constant down (it forces $v \to 0$ at infinity).
>
> So (7) holds more generally than its derivation shows, while (3) and (8) need a decay condition; [[§139★ Dirichlet Problem for a Half Plane|§139★]] proves (7) for every bounded, piecewise continuous boundary function, and (8) under an order property.
>
> *B&C: Sec. 138, condition (1)*

^ex-138-3
