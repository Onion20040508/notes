---
type: section
subject: "[[Complex Variables]]"
chapter: 7
section: "89★"
bc: "89"
aliases: ["B&C 89"]
tags: [complex-variables, math342, extension]
---
← [[§88★ Jordan's Lemma]] · ↑ [[· 7 Applications of Residues]] · [[§90★ An Indentation Around a Branch Point]] →

*Brown–Churchill, Section 89.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

When the integrand has a singular point on the real axis, the contour of §85 must avoid it, and the standard way is an **indentation**: a small semicircle $C_\rho$ around the point. The key fact is a limit: as $\rho \to 0$, the integral over a half circle around a simple pole tends to $\mp\pi i$ times the residue, half of what a full circle gives. With it B&C evaluates Dirichlet's integral $\int_0^\infty \sin x/x\,dx = \pi/2$, where the pole of $e^{iz}/z$ sits at the origin and the arc at infinity needs Jordan's lemma; the same contour gives the integral of $\sin^2 x/x^2$.

> [!theorem] Theorem §89.1: Half Circle Around a Simple Pole
> Suppose that
> - (a) a function $f(z)$ has a simple pole at a point $z = x_0$ on the real axis, with a Laurent series representation in a punctured disk $0 < |z - x_0| < R_2$ and with residue $B_0$;
> - (b) $C_\rho$ denotes the upper half of a circle $|z - x_0| = \rho$, where $\rho < R_2$ and the clockwise direction is taken.
>
> Then
>
> $$
> \lim_{\rho\to0}\int_{C_\rho} f(z)\,dz = -B_0\pi i .
> $$
>
> *B&C: Sec. 89, Theorem*

^thm-89-1

> [!proof]+ Proof
> Since the pole is simple, the Laurent series in (a) has the form
>
> $$
> f(z) = g(z) + \frac{B_0}{z - x_0} \quad (0 < |z - x_0| < R_2), \qquad\text{where}\qquad g(z) = \sum_{n=0}^{\infty} a_n(z - x_0)^n \quad (|z - x_0| < R_2) .
> $$
>
> Thus
>
> $$
> \int_{C_\rho} f(z)\,dz = \int_{C_\rho} g(z)\,dz + B_0\int_{C_\rho}\frac{dz}{z - x_0} . \qquad (1)
> $$
>
> **The regular part.** The power series $g$ is continuous in its disk of convergence $|z - x_0| < R_2$ ([[§70★ Continuity of Sums of Power Series#^thm-70-1|Theorem §70.1]]). Choose $\rho_0$ with $\rho < \rho_0 < R_2$; then $g$ is continuous on the closed disk $|z - x_0| \le \rho_0$, hence bounded there ([[§18 Continuity#^thm-18-6|Theorem §18.6]]): $|g(z)| \le M$. (One $\rho_0$ serves for all $\rho < \rho_0$, so $M$ does not depend on $\rho$.) The length of $C_\rho$ is $\pi\rho$, so ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]])
>
> $$
> \Big|\int_{C_\rho} g(z)\,dz\Big| \le M\pi\rho, \qquad\text{and}\qquad \lim_{\rho\to0}\int_{C_\rho} g(z)\,dz = 0 . \qquad (2)
> $$
>
> **The principal part.** The reversed semicircle $-C_\rho$ has the parametric representation $z = x_0 + \rho e^{i\theta}$ $(0 \le \theta \le \pi)$, so
>
> $$
> \int_{C_\rho}\frac{dz}{z - x_0} = -\int_{-C_\rho}\frac{dz}{z - x_0} = -\int_0^{\pi}\frac{1}{\rho e^{i\theta}}\,\rho ie^{i\theta}\,d\theta = -i\int_0^{\pi} d\theta = -i\pi , \qquad (3)
> $$
>
> for every $\rho$. Letting $\rho \to 0$ in (1) and using (2) and (3) gives the limit $-B_0\pi i$.

^pf-89-1

*Uses:* [[§70★ Continuity of Sums of Power Series#^thm-70-1|§70.1]], [[§18 Continuity#^thm-18-6|§18.6]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]], [[§67 Proof of Laurent's Theorem#^thm-67-1|§67.1]], [[§44 Contour Integrals#^def-44-1|Def. §44.1]]

> [!remark] Remark: Other Arcs
> The proof uses only that $g$ is bounded near $x_0$ and that $\int\frac{dz}{z - x_0}$ over an arc is $i$ times the angle swept. So the counterclockwise upper half circle gives $+B_0\pi i$; this is an old-final problem, worked out in [[§84 Behavior of Functions Near Isolated Singular Points#^ex-84-3|Example §84.3]] (its first part, for analytic $g$, is [[§47 Upper Bounds for Moduli of Contour Integrals#^ex-47-5|Example §47.5]](d)). An arc of angle $\alpha$ around a simple pole gives $\pm i\alpha B_0$; for $\alpha = 2\pi$ this is the [[§76 Cauchy's Residue Theorem#^thm-76-1|residue theorem]] for one simple pole. For a pole of order $2$ or more the limit does not exist in general: $\int_{C_\rho} dz/z^2 = -2/\rho$ for the clockwise upper half circle about $0$.

^rem-89-1

## Dirichlet's Integral

> [!example] Example §89.1: Dirichlet's Integral
> Show that
>
> $$
> \int_0^\infty\frac{\sin x}{x}\,dx = \frac\pi2 \qquad (4)
> $$
>
> by integrating $e^{iz}/z$ around the indented contour of the figure below: $L_1$ is the interval $\rho \le x \le R$, then the semicircle $C_R$ counterclockwise, then $L_2$, the interval $-R \le x \le -\rho$, and the semicircle $C_\rho$ clockwise, with $0 < \rho < R$. The semicircle $C_\rho$ avoids the singularity of $e^{iz}/z$ at the origin.
>
> **Cauchy–Goursat.** $e^{iz}/z$ is analytic inside and on the contour ([[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|Theorem §51.3]]), so
>
> $$
> \int_{L_1}\frac{e^{iz}}{z}\,dz + \int_{L_2}\frac{e^{iz}}{z}\,dz = -\int_{C_\rho}\frac{e^{iz}}{z}\,dz - \int_{C_R}\frac{e^{iz}}{z}\,dz . \qquad (5)
> $$
>
> **The legs.** $L_1$ and $-L_2$ have the parametrizations $z = re^{i0} = r$ and $z = re^{i\pi} = -r$ $(\rho \le r \le R)$ (6), so the left side of (5) is
>
> $$
> \int_{L_1}\frac{e^{iz}}{z}\,dz - \int_{-L_2}\frac{e^{iz}}{z}\,dz = \int_\rho^R\frac{e^{ir}}{r}\,dr - \int_\rho^R\frac{e^{-ir}}{r}\,dr = 2i\int_\rho^R\frac{e^{ir} - e^{-ir}}{2ir}\,dr = 2i\int_\rho^R\frac{\sin r}{r}\,dr .
> $$
>
> (On $-L_2$, $z = -r$ and $dz = -dr$, so $\int_{-L_2}\frac{e^{iz}}{z}dz = \int_\rho^R\frac{e^{-ir}}{-r}(-dr)$.) Hence
>
> $$
> 2i\int_\rho^R\frac{\sin r}{r}\,dr = -\int_{C_\rho}\frac{e^{iz}}{z}\,dz - \int_{C_R}\frac{e^{iz}}{z}\,dz . \qquad (7)
> $$
>
> **The small semicircle.** From the Laurent series
>
> $$
> \frac{e^{iz}}{z} = \frac1z\Big(1 + \frac{iz}{1!} + \frac{(iz)^2}{2!} + \frac{(iz)^3}{3!} + \cdots\Big) = \frac1z + \frac{i}{1!} + \frac{i^2}{2!}z + \frac{i^3}{3!}z^2 + \cdots \qquad (0 < |z| < \infty),
> $$
>
> $e^{iz}/z$ has a simple pole at the origin with residue $1$, and Theorem §89.1 gives $\lim_{\rho\to0}\int_{C_\rho}\frac{e^{iz}}{z}\,dz = -\pi i$.
>
> **The large semicircle.** On $C_R$, $|1/z| = 1/R \to 0$, so by Jordan's lemma ([[§88★ Jordan's Lemma#^thm-88-2|Theorem §88.2]], $a = 1$) $\lim_{R\to\infty}\int_{C_R}\frac{e^{iz}}{z}\,dz = 0$. (The bound of [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]], $\frac1R\cdot\pi R = \pi$, would not do.)
>
> **Conclusion.** Letting $\rho \to 0$ in (7) and then $R \to \infty$: $2i\int_0^\infty\frac{\sin r}{r}\,dr = \pi i$, which is (4). The integral at $0$ is proper ($\sin r/r \to 1$), and the limits show that the improper integral at $\infty$ converges (conditionally: $\int_0^\infty|\sin x|/x\,dx = \infty$).
>
> *B&C: Sec. 89, Example*

^ex-89-1

![[m342-89-1.svg]]
*The indented contour of Example §89.1: the legs $L_1$, $L_2$ on the real axis, the large semicircle $C_R$ counterclockwise and the small semicircle $C_\rho$ clockwise around the pole of $e^{iz}/z$ at the origin. The pole is outside the contour, so the integral around it is $0$; in the limit $C_\rho$ contributes $-\pi i$ times the residue, half of a full clockwise circle.*

> [!remark]- Connections
> - Dirichlet's integral is the value at $x = 0$ of the Fourier integral of the rectangular pulse, [[§18 Fourier Integral#^ex-18-2|341 Ex. §18.2]], and it governs the Gibbs overshoot shown there; Powers evaluates it by real methods (Exercise 1.9.6).

## Further Examples

> [!example] Example §89.2: The Integrals of (cos ax − cos bx)/x² and sin²x/x²
> Use $f(z) = (e^{iaz} - e^{ibz})/z^2$ and the indented contour of Example §89.1 to show that
>
> $$
> \int_0^\infty\frac{\cos(ax) - \cos(bx)}{x^2}\,dx = \frac\pi2(b - a) \qquad (a \ge 0,\ b \ge 0),
> $$
>
> and deduce $\displaystyle\int_0^\infty\frac{\sin^2x}{x^2}\,dx = \frac\pi2$.
>
> **The pole.** From $e^{iaz} - e^{ibz} = i(a - b)z + \frac{(ia)^2 - (ib)^2}{2}z^2 + \cdots$, $f(z) = \frac{i(a - b)}{z} + (\text{a power series})$: a simple pole at $0$ (if $a \ne b$; for $a = b$ both sides are $0$) with residue $B_0 = i(a - b)$. Theorem §89.1 gives $\lim_{\rho\to0}\int_{C_\rho} f = -\pi i\cdot i(a - b) = \pi(a - b)$.
>
> **The legs.** As in Example §89.1, $\int_{L_1} f + \int_{L_2} f = \int_\rho^R\big(f(r) + f(-r)\big)\,dr$, and
>
> $$
> f(r) + f(-r) = \frac{e^{iar} - e^{ibr} + e^{-iar} - e^{-ibr}}{r^2} = \frac{2\big(\cos ar - \cos br\big)}{r^2} .
> $$
>
> **The large semicircle.** For $a, b \ge 0$ and $y \ge 0$, $|e^{iaz}|, |e^{ibz}| \le 1$, so $|f| \le 2/R^2$ on $C_R$ and $\big|\int_{C_R} f\big| \le 2\pi/R \to 0$.
>
> **Conclusion.** By Cauchy–Goursat, $2\int_\rho^R\frac{\cos ar - \cos br}{r^2}\,dr = -\int_{C_\rho} f - \int_{C_R} f \to -\pi(a - b)$, so $\int_0^\infty\frac{\cos ax - \cos bx}{x^2}\,dx = \frac\pi2(b - a)$. (The integrand is continuous at $0$, with limit $(b^2 - a^2)/2$.) With $a = 0$, $b = 2$ and $1 - \cos 2x = 2\sin^2x$: $2\int_0^\infty\frac{\sin^2x}{x^2}\,dx = \pi$, so $\int_0^\infty\frac{\sin^2x}{x^2}\,dx = \frac\pi2$. Quadrature confirms ($\pi$ for $a = 1$, $b = 3$).
>
> *B&C: Sec. 91, Exercise 1*

^ex-89-2

> [!remark]- Connections
> - With $a = 0$, $b = 1$ this is $\int_0^\infty\frac{1 - \cos\lambda}{\lambda^2}\,d\lambda = \frac\pi2$, the value used at $x = 0$ for the triangular pulse in [[§18 Fourier Integral#^ex-18-3|341 Ex. §18.3]].
