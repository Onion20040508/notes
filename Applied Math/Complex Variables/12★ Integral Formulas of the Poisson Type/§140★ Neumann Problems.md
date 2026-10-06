---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 140
bc: "140"
aliases: ["B&C 140"]
tags: [complex-variables, math342, extension]
---
← [[§139★ Dirichlet Problem for a Half Plane]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]]

*Brown–Churchill, Section 140.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

In a Neumann problem the normal derivative of the harmonic function is prescribed on the boundary instead of its values: for steady temperatures, the heat flux through the edge. The kernel is now a logarithm, $Q = -2r_0\ln|s - z|$, whose radial derivative turns out to be $\frac{r_0}{r}(P - 1)$, so the Neumann problem is reduced to the Poisson integral of [[§135★ Dirichlet Problem for a Disk|§135★]]. The data must have mean value zero (no net heat flow into a body in a steady state), and the solution is determined only up to an additive constant, which is its value at the center. The same idea, with the Schwarz integral of [[§139★ Dirichlet Problem for a Half Plane|§139★]], handles the exterior of a circle, a half plane, and a quadrant.

## The Disk

As in [[§134★ Poisson Integral Formula|§134★]], write $s = r_0\exp(i\phi)$ and $z = r\exp(i\theta)$, $r < r_0$.

> [!definition] Definition §140.1: The Neumann Kernel Q
> For $s$ fixed on the circle $|z| = r_0$,
>
> $$
> Q(r_0, r, \phi - \theta) = -2r_0\ln|s - z| = -r_0\ln\big[r_0^2 - 2r_0r\cos(\phi - \theta) + r^2\big] . \qquad (1)
> $$
>
> *B&C: Sec. 140, equation (1)*

^def-140-1

> [!theorem] Lemma §140.1: Properties of Q
> $Q$ is a harmonic function of $r$ and $\theta$ interior to the circle $|z| = r_0$, and if $r \ne 0$,
>
> $$
> Q_r(r_0, r, \phi - \theta) = -\frac{r_0}{r}\Big(\frac{2r^2 - 2r_0r\cos(\phi - \theta)}{r_0^2 - 2r_0r\cos(\phi - \theta) + r^2}\Big) = \frac{r_0}{r}\big[P(r_0, r, \phi - \theta) - 1\big] , \qquad (2)
> $$
>
> where $P$ is the Poisson kernel (7) of [[§134★ Poisson Integral Formula#^def-134-2|§134★]]. Formula (2) holds for every $r > 0$, $r \ne r_0$.
>
> *B&C: Sec. 140, equation (2)*

^lem-140-1

> [!proof]+ Proof
> **Harmonic.** $Q$ is the real component of $-2r_0\log(z - s)$, where the branch cut of $\log(z - s)$ is an outward ray from the point $s$; that branch is analytic inside the circle, and the real part of an analytic function is harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).
>
> **(2).** Differentiating (1) with respect to $r$,
>
> $$
> Q_r = -r_0\,\frac{2r - 2r_0\cos(\phi - \theta)}{r_0^2 - 2r_0r\cos(\phi - \theta) + r^2} = -\frac{r_0}{r}\cdot\frac{2r^2 - 2r_0r\cos(\phi - \theta)}{r_0^2 - 2r_0r\cos(\phi - \theta) + r^2} .
> $$
>
> On the other hand, writing $D = r_0^2 - 2r_0r\cos(\phi - \theta) + r^2$, $P - 1 = \dfrac{r_0^2 - r^2 - D}{D} = \dfrac{2r_0r\cos(\phi - \theta) - 2r^2}{D}$, which is the same fraction with the opposite sign. This algebra uses nothing about $r < r_0$.

^pf-140-1

*Uses:* [[§140★ Neumann Problems#^def-140-1|Def. §140.1]], [[§134★ Poisson Integral Formula#^def-134-2|Def. §134.2]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]]

These observations suggest that $Q$ may be used to write an integral representation of a harmonic function $U$ whose normal derivative $U_r$ on the circle $r = r_0$ takes prescribed values $G(\theta)$.

> [!theorem] Theorem §140.2: Neumann Problem for a Disk
> Let $G$ be piecewise continuous on $0 \le \phi \le 2\pi$ with mean value zero,
>
> $$
> \int_0^{2\pi}G(\phi)\,d\phi = 0 , \qquad (4)
> $$
>
> and let $U_0$ be an arbitrary constant. Then
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}Q(r_0, r, \phi - \theta)\,G(\phi)\,d\phi + U_0 \qquad (r < r_0) , \qquad (3)
> $$
>
> that is,
>
> $$
> U(r, \theta) = -\frac{r_0}{2\pi}\int_0^{2\pi}\ln\big[r_0^2 - 2r_0r\cos(\phi - \theta) + r^2\big]\,G(\phi)\,d\phi + U_0 \qquad (r < r_0) , \qquad (6)
> $$
>
> is harmonic in $r < r_0$ and
>
> $$
> \lim_{\substack{r\to r_0\\ r < r_0}}U_r(r, \theta) = G(\theta) \qquad (5)
> $$
>
> for each $\theta$ at which $G$ is continuous. So (6) solves the **Neumann problem** for the region interior to the circle, $G(\theta)$ being the normal derivative of $U$ at the boundary in the sense of (5). Moreover $U_0 = U(0, \theta)$ is the value of $U$ at the center.
>
> *B&C: Sec. 140, equations (3)–(6)*

^thm-140-2

> [!proof]+ Proof
> **Harmonic.** B&C: $U$ is harmonic because the integrand is a harmonic function of $r$ and $\theta$ (Lemma §140.1), differentiation under the integral sign being allowed as in [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]]. (In the form used there: since $\ln|s - z| = \ln r_0 + \operatorname{Re}\operatorname{Log}(1 - z/s)$ and $|z/s| < 1$, $U$ is a constant plus the real part of $-\frac{r_0}{\pi}\int_0^{2\pi}\operatorname{Log}(1 - z/s)\,G(\phi)\,d\phi$, whose difference quotients converge uniformly, because $\frac{d}{dz}\operatorname{Log}(1 - z/s) = \frac{-1}{s - z}$ is bounded for $|z| \le \rho < r_0$; so it is analytic, its derivatives may be computed under the integral sign, and $U$ is harmonic.)
>
> **The normal derivative.** By (2) and then (4),
>
> $$
> U_r(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}\frac{r_0}{r}\big[P(r_0, r, \phi - \theta) - 1\big]G(\phi)\,d\phi = \frac{r_0}{r}\cdot\frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,G(\phi)\,d\phi .
> $$
>
> By (1) and (2) of [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]], applied to the piecewise continuous function $G$, the last integral tends to $G(\theta)$ as $r \to r_0$ at each $\theta$ where $G$ is continuous, and $r_0/r \to 1$. This is (5).
>
> **The center.** At $r = 0$ the logarithm in (6) is the constant $\ln r_0^2$, and by (4) its integral against $G$ is zero; so $U(0, \theta) = U_0$.

^pf-140-2

*Uses:* [[§140★ Neumann Problems#^lem-140-1|§140.1]], [[§135★ Dirichlet Problem for a Disk#^thm-135-1|§135.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]]

The values $U(r, \theta)$ may represent steady temperatures in a disk $r < r_0$ with insulated faces. Then (5) says that the flux of heat into the disk through its edge is proportional to $G(\theta)$ ([[§118★ Steady Temperatures#^def-118-new1|Definition §118.2]]), and (4) is the natural physical requirement that the total rate of flow of heat into the disk be zero, since the temperatures do not vary with time.

> [!remark] Remark: Why the Data Must Have Mean Zero
> If (4) fails, the integral (3) still defines a harmonic function, but by (2) its normal derivative is
>
> $$
> U_r = \frac{r_0}{r}\Big[\frac{1}{2\pi}\int_0^{2\pi}P\,G\,d\phi - \overline G\Big] \longrightarrow G(\theta) - \overline G, \qquad \overline G = \frac{1}{2\pi}\int_0^{2\pi}G(\phi)\,d\phi :
> $$
>
> it solves the Neumann problem for the data $G - \overline G$, not $G$. And no harmonic function can do better. If $U$ is harmonic in a neighborhood of the closed disk $r \le \rho$, then $\frac{1}{2\pi}\int_0^{2\pi}U(\rho', \theta)\,d\theta = U(0)$ for every $\rho' \le \rho$ (the case $r = 0$ of [[§134★ Poisson Integral Formula#^thm-134-1|Theorem §134.1]]), so its derivative with respect to $\rho'$, $\frac{1}{2\pi}\int_0^{2\pi}U_r(\rho', \theta)\,d\theta$ is zero: the net flux through every circle is zero. So data with nonzero mean are not the normal derivative of any function harmonic up to the circle (nor the limit (5) of $U_r$, when $U_r$ stays bounded near the circle, by letting $\rho' \to r_0$). The constant $U_0$ is free, as it must be, since adding a constant to a solution of a Neumann problem gives another solution.

^rem-140-1

> [!remark]- Connections
> - Neumann's problem and the non-uniqueness up to a constant: [[§35 Potential Equation#^def-35-new3|341 Def. §35.2]] and [[§35 Potential Equation#^prop-35-1|341 Prop. §35.1]]. The compatibility condition $\oint\partial u/\partial n\,ds = 0$ in any region follows from Green's first identity, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|452 Thm. §17.2]]; the remark above proves it for disks.
> - $Q = -2r_0\ln|s - z|$ is $-4\pi r_0$ times the fundamental solution $\frac{1}{2\pi}\ln|z - s|$ of the two-dimensional Laplacian, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|452 Thm. §17.5]]; (6) represents $U$ as a potential of a single layer of density proportional to $G$ on the circle.

## Exterior of a Circle, Half Plane, Quadrant

> [!theorem] Theorem §140.3: Neumann Problem for the Exterior of a Circle
> Let $G$ be piecewise continuous and satisfy (4), and let $H_0$ be a constant. Then
>
> $$
> H(R, \psi) = -\frac{1}{2\pi}\int_0^{2\pi}Q(r_0, R, \phi - \psi)\,G(\phi)\,d\phi + H_0 \qquad (R > r_0) \qquad (7)
> $$
>
> is harmonic in the region exterior to the circle, and
>
> $$
> H_0 = \lim_{R\to\infty}H(R, \psi), \qquad \lim_{\substack{R\to r_0\\ R > r_0}}H_R(R, \psi) = G(\psi) \qquad (8)
> $$
>
> for each $\psi$ at which $G$ is continuous.
>
> *B&C: Sec. 140, equations (7)–(8); Exercise 1*

^thm-140-3

> [!proof]+ Proof
> Write $Z = Re^{i\psi}$, $s = r_0e^{i\phi}$. For $R > r_0$,
>
> $$
> Q(r_0, R, \phi - \psi) = -2r_0\ln|Z - s| = -2r_0\ln R - 2r_0\operatorname{Re}\operatorname{Log}\Big(1 - \frac sZ\Big) ,
> $$
>
> with $|s/Z| < 1$. By (4) the term $-2r_0\ln R$ integrates to zero against $G$, so
>
> $$
> H(R, \psi) = \frac{r_0}{\pi}\int_0^{2\pi}\operatorname{Re}\operatorname{Log}\Big(1 - \frac sZ\Big)G(\phi)\,d\phi + H_0 .
> $$
>
> **Harmonic.** As in Theorem §140.2, the integral is the real part of a function analytic in $|Z| > r_0$ (the derivative of $\operatorname{Log}(1 - s/Z)$ in $Z$ is $\frac{s}{Z(Z - s)}$, bounded for $|Z| \ge \rho > r_0$).
>
> **At infinity.** $\big|\operatorname{Log}(1 - s/Z)\big| \le 2r_0/R$ once $R \ge 2r_0$ (from the Taylor series of $\operatorname{Log}(1 - w)$, $|w| \le \frac12$), uniformly in $\phi$; so $H \to H_0$ as $R \to \infty$.
>
> **The normal derivative.** Formula (2) holds for $R > r_0$, so by (4)
>
> $$
> H_R(R, \psi) = -\frac{1}{2\pi}\int_0^{2\pi}\frac{r_0}{R}\big[P(r_0, R, \phi - \psi) - 1\big]G(\phi)\,d\phi = \frac{r_0}{R}\Big[-\frac{1}{2\pi}\int_0^{2\pi}P(r_0, R, \phi - \psi)\,G(\phi)\,d\phi\Big] .
> $$
>
> The bracket is the solution (4) of [[§137★ Related Boundary Value Problems#^thm-137-4|Theorem §137.4]] of the exterior Dirichlet problem with boundary values $G$, so by (5) there it tends to $G(\psi)$ as $R \to r_0^+$; and $r_0/R \to 1$.

^pf-140-3

*Uses:* [[§140★ Neumann Problems#^lem-140-1|§140.1]], [[§140★ Neumann Problems#^thm-140-2|§140.2]], [[§137★ Related Boundary Value Problems#^thm-137-4|§137.4]]

> [!theorem] Theorem §140.4: Neumann Problem for a Half Plane
> Let $G(x)$ be continuous for all real $x$ except possibly for a finite number of finite jumps, and let it satisfy the order property
>
> $$
> |x^aG(x)| < M \qquad (a > 1) \qquad (9)
> $$
>
> for $-\infty < x < \infty$. For a real constant $U_0$, the function
>
> $$
> U(x, y) = \frac1\pi\int_{-\infty}^{\infty}\ln|z - t|\,G(t)\,dt + U_0 = \frac{1}{2\pi}\int_{-\infty}^{\infty}\ln\big[(t - x)^2 + y^2\big]\,G(t)\,dt + U_0 \qquad (y > 0) \qquad (10)
> $$
>
> is harmonic in the half plane $y > 0$, and
>
> $$
> U_y(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{y\,G(t)}{(t - x)^2 + y^2}\,dt \qquad (y > 0) , \qquad (11)
> $$
>
> so that
>
> $$
> \lim_{\substack{y\to0\\ y > 0}}U_y(x, y) = G(x) \qquad (12)
> $$
>
> at each point $x$ where $G$ is continuous. Expression (10) solves the Neumann problem for the half plane $y > 0$ with boundary condition (12). (No conditions on $G$ are given that ensure $U$ stays bounded as $|z|$ increases.)
>
> *B&C: Sec. 140, equations (9)–(12)*

^thm-140-4

> [!proof]+ Proof
> **Harmonic.** For each fixed real $t$, $\ln|z - t| = \operatorname{Re}\operatorname{Log}(z - t)$ is harmonic in $\operatorname{Im} z > 0$. (B&C states that (10) is then harmonic; here is why the interchange of differentiation and integration is allowed.) $G$ is bounded (continuous with finitely many jumps on any bounded interval, and $|G(t)| < M|t|^{-a}$ for large $|t|$). For $z$ in a closed disk $K$ in the upper half plane there is $C_K$ with $|\ln|z - t|| \le C_K\big(1 + \ln(1 + |t|)\big)$ and with the first and second partial derivatives of $\ln|z - t|$ in $x$ and $y$ bounded by $C_K/(1 + |t|)$. Since $a > 1$, $|G(t)|\big(1 + \ln(1 + |t|)\big)$ is integrable over the line, so the integral (10) converges and may be differentiated twice under the integral sign (dominated convergence, [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]]). Hence $U$ satisfies Laplace's equation.
>
> **(11) and (12).** Differentiating the second form of (10) under the integral sign, $\frac{\partial}{\partial y}\frac{1}{2\pi}\ln\big[(t - x)^2 + y^2\big] = \frac1\pi\cdot\frac{y}{(t - x)^2 + y^2}$, which gives (11). Thus $U_y$ is the Schwarz integral transform of $G$ ([[§139★ Dirichlet Problem for a Half Plane#^def-139-1|Definition §139.1]]), and since $G$ is bounded with finitely many jumps, [[§139★ Dirichlet Problem for a Half Plane#^thm-139-1|Theorem §139.1]] gives (12).

^pf-140-4

*Uses:* [[§139★ Dirichlet Problem for a Half Plane#^def-139-1|Def. §139.1]], [[§139★ Dirichlet Problem for a Half Plane#^thm-139-1|§139.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]] (dominated convergence)

> [!theorem] Corollary §140.5: Neumann Problem for a Quadrant
> When $G$ is an odd function, expression (10) with $U_0 = 0$ can be written
>
> $$
> U(x, y) = \frac{1}{2\pi}\int_0^\infty\ln\Big[\frac{(t - x)^2 + y^2}{(t + x)^2 + y^2}\Big]G(t)\,dt \qquad (x > 0,\ y > 0) . \qquad (13)
> $$
>
> It is harmonic in the first quadrant and satisfies
>
> $$
> U(0, y) = 0 \quad (y > 0), \qquad (14) \qquad\qquad \lim_{\substack{y\to0\\ y > 0}}U_y(x, y) = G(x) \quad (x > 0) \qquad (15)
> $$
>
> at points of continuity of $G$.
>
> *B&C: Sec. 140, equations (13)–(15)*

^cor-140-5

> [!proof]+ Proof
> In (10) split the integral at $t = 0$ and substitute $t \mapsto -t$ in the part over $t < 0$: it becomes $\frac{1}{2\pi}\int_0^\infty\ln\big[(t + x)^2 + y^2\big]G(-t)\,dt = -\frac{1}{2\pi}\int_0^\infty\ln\big[(t + x)^2 + y^2\big]G(t)\,dt$. Adding the part over $t > 0$ gives (13). Harmonicity and (15) come from Theorem §140.4. At $x = 0$ the quotient inside the logarithm is $1$, so $U(0, y) = 0$.

^pf-140-5

*Uses:* [[§140★ Neumann Problems#^thm-140-4|§140.4]]

> [!remark] Remark: Method — Neumann Problems
> 1. **Check the data.** On a closed curve (circle) the prescribed normal derivative must have mean zero, (4); otherwise there is no solution.
> 2. **Disk.** $U = \frac{1}{2\pi}\int Q\,G\,d\phi + U_0$, (6); the constant $U_0$ is $U$ at the center and is not determined by the data. For trigonometric data expand $\ln(1 - 2\rho\cos\psi + \rho^2) = -2\sum_{n\ge1}\rho^n\cos n\psi/n$ ([[§140★ Neumann Problems#^ex-140-1|Example §140.1]]).
> 3. **Exterior, half plane, quadrant.** Use (7), (10) or (13); for a quadrant with zero values on one edge use the odd extension, (13); for a semicircle, extend $G$ oddly or evenly across the diameter ([[§140★ Neumann Problems#^ex-140-3|Example §140.3]]).
> 4. **Fluxes.** In heat problems the normal derivative is $-\Phi/K$ by Fourier's law ([[§118★ Steady Temperatures#^def-118-new1|Definition §118.2]]); to find the flux through another edge, differentiate the integral under the integral sign.

^rem-140-2

## Examples

> [!example] Example §140.1: Normal Derivative cos θ on a Circle
> Solve the Neumann problem in $r < r_0$ with $G(\theta) = \cos\theta$.
>
> The data have mean zero, so Theorem §140.2 applies. For $0 \le \rho < 1$, the real part of $\operatorname{Log}(1 - \rho e^{i\psi}) = -\sum_{n\ge1}\rho^ne^{in\psi}/n$ gives
>
> $$
> \ln\big(1 - 2\rho\cos\psi + \rho^2\big) = 2\ln|1 - \rho e^{i\psi}| = -2\sum_{n=1}^{\infty}\frac{\rho^n}{n}\cos n\psi ,
> $$
>
> uniformly in $\psi$. With $\rho = r/r_0$ and $\psi = \phi - \theta$,
>
> $$
> Q(r_0, r, \phi - \theta) = -r_0\ln r_0^2 - r_0\ln\big(1 - 2\rho\cos\psi + \rho^2\big) = -2r_0\ln r_0 + 2r_0\sum_{n=1}^{\infty}\frac{\rho^n}{n}\cos n(\phi - \theta) .
> $$
>
> Integrating term by term against $\cos\phi$, only $n = 1$ survives, and $\frac{1}{2\pi}\int_0^{2\pi}\cos(\phi - \theta)\cos\phi\,d\phi = \frac12\cos\theta$. So
>
> $$
> U(r, \theta) = 2r_0\cdot\frac{r}{r_0}\cdot\frac12\cos\theta + U_0 = r\cos\theta + U_0 = x + U_0 .
> $$
>
> *Check:* $U$ is harmonic, $U_r = \cos\theta = G$ for every $r$, and $U(0) = U_0$. With $r_0 = 1.5$, $r = 0.8$, $\theta = 0.9$, quadrature of (3) (with $U_0 = 0$) gives $0.497288 = 0.8\cos0.9$; and $Q_r$ computed numerically agrees with $\frac{r_0}{r}(P - 1)$ to all digits shown.
>
> *B&C: Sec. 140, equations (3)–(6)*

^ex-140-1

> [!example] Example §140.2: Heat Flux out of a Quarter Plate
> Let $T(x, y)$ be the steady temperatures in a plate $x \ge 0$, $y \ge 0$ with insulated faces. $T = 0$ on the edge $x = 0$; the flux of heat into the plate along the segment $0 < x < 1$ of the edge $y = 0$ is a constant $A$, and the rest of that edge is insulated. Use (13) to show that the flux out of the plate along the edge $x = 0$ is
>
> $$
> \frac A\pi\ln\Big(1 + \frac{1}{y^2}\Big) .
> $$
>
> **The data.** By Fourier's law $\Phi = -K\,dT/dN$ ([[§118★ Steady Temperatures#^def-118-new1|Definition §118.2]]), with $N$ pointing into the plate ($+y$) on the edge $y = 0$: $-KT_y = A$ on $0 < x < 1$ and $T_y = 0$ for $x > 1$. So $G(x) = -A/K$ on $0 < x < 1$ and $0$ for $x > 1$; extend it oddly. It has compact support, so (9) holds, and (13) gives
>
> $$
> T(x, y) = -\frac{A}{2\pi K}\int_0^1\ln\Big[\frac{(t - x)^2 + y^2}{(t + x)^2 + y^2}\Big]dt ,
> $$
>
> with $T(0, y) = 0$ by (14).
>
> **The flux through $x = 0$.** Differentiating under the integral sign,
>
> $$
> \frac{\partial}{\partial x}\ln\Big[\frac{(t - x)^2 + y^2}{(t + x)^2 + y^2}\Big] = \frac{-2(t - x)}{(t - x)^2 + y^2} - \frac{2(t + x)}{(t + x)^2 + y^2} = \frac{-4t}{t^2 + y^2} \quad\text{at } x = 0 ,
> $$
>
> so
>
> $$
> T_x(0, y) = \frac{2A}{\pi K}\int_0^1\frac{t\,dt}{t^2 + y^2} = \frac{A}{\pi K}\ln\frac{1 + y^2}{y^2} .
> $$
>
> The outward normal on $x = 0$ points in the $-x$ direction, so the flux out of the plate there is $\Phi = -K(-T_x) = KT_x(0, y) = \frac A\pi\ln\big(1 + \frac{1}{y^2}\big)$. It is infinite at the corner and decays like $A/(\pi y^2)$ far up the edge. With $A = K = 1$ and $y = 0.6$, numerical differentiation of the integral gives $0.423077 = \frac1\pi\ln(1 + 1/0.36)$. (As a check on the total: $\int_0^\infty\frac A\pi\ln(1 + y^{-2})\,dy = \frac A\pi\cdot\pi = A$, all the heat that enters through $0 < x < 1$.)
>
> *B&C: Sec. 140, Exercise 4*

^ex-140-2

> [!example] Example §140.3: Semicircular Regions
> Obtain as special cases of (3), for a function harmonic in the half disk $r < r_0$, $0 < \theta < \pi$ with $\lim_{r\to r_0^-}U_r(r, \theta) = G(\theta)$ ($0 < \theta < \pi$) at points of continuity:
>
> **(a)** if $U(r, 0) = U(r, \pi) = 0$,
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^\pi\big[Q(r_0, r, \phi - \theta) - Q(r_0, r, \phi + \theta)\big]G(\phi)\,d\phi ;
> $$
>
> **(b)** if $U_\theta(r, 0) = U_\theta(r, \pi) = 0$, provided $\int_0^\pi G(\phi)\,d\phi = 0$,
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^\pi\big[Q(r_0, r, \phi - \theta) + Q(r_0, r, \phi + \theta)\big]G(\phi)\,d\phi + U_0 .
> $$
>
> Like $P$, the kernel $Q(r_0, r, \cdot)$ is even and $2\pi$-periodic in its last argument. **(a)** Extend $G$ oddly, $G(2\pi - \phi) = -G(\phi)$; then (4) holds automatically, and folding (3) as in [[§137★ Related Boundary Value Problems#^prop-137-1|Proposition §137.1]] gives the formula with $U_0 = 0$. The bracket vanishes at $\theta = 0$ and at $\theta = \pi$, so $U = 0$ on the diameter, and (5) gives the boundary condition on the arc. **(b)** Extend $G$ evenly; now (4) is $2\int_0^\pi G = 0$, which is why the proviso is needed. Folding gives the formula, and as in [[§137★ Related Boundary Value Problems#^prop-137-2|Proposition §137.2]] the $\theta$-derivative of the bracket vanishes at $\theta = 0$ and $\theta = \pi$.
>
> *B&C: Sec. 140, Exercises 2 and 3*

^ex-140-3
