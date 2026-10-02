---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 135
bc: "135"
aliases: ["B&C 135"]
tags: [complex-variables, math342, extension]
---
← [[§134★ Poisson Integral Formula]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§136★ Examples (Dirichlet Problem for a Disk)]] →

*Brown–Churchill, Section 135.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

In [[§134★ Poisson Integral Formula|§134★]] the Poisson formula reproduced a function already known to be harmonic up to the circle. This section turns it around: for any piecewise continuous boundary function $F$, the Poisson integral of $F$ is harmonic in the disk and tends to $F(\theta)$ along each radius at every point where $F$ is continuous. So it solves the Dirichlet problem for the disk, with discontinuous boundary data allowed (a cylinder split into two halves at different potentials); the proof uses only three properties of the kernel: it is positive, it has mean value one, and away from $\phi = \theta$ it is small near the circle. Expanding the kernel in a cosine series gives the solution as a Fourier series damped by $(r/r_0)^n$, which is the form found by separation of variables in Fourier Series and PDEs.

## The Poisson Integral Transform

> [!definition] Definition §135.1: Poisson Integral Transform
> Let $F$ be a piecewise continuous function ([[§42 Definite Integrals of Functions w(t)|§42]]) of $\theta$ on $0 \le \theta \le 2\pi$. The **Poisson integral transform** of $F$ is
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,F(\phi)\,d\phi \qquad (r < r_0) , \qquad (1)
> $$
>
> where $P$ is the Poisson kernel of [[§134★ Poisson Integral Formula#^def-134-2|Definition §134.2]].
>
> *B&C: Sec. 135, equation (1)*

^def-135-1

> [!theorem] Theorem §135.1: Solution of the Dirichlet Problem for a Disk
> The Poisson integral transform $U(r, \theta)$ of a piecewise continuous $F$ is harmonic inside the circle $r = r_0$, and
>
> $$
> \lim_{\substack{r\to r_0\\ r < r_0}}U(r, \theta) = F(\theta) \qquad (2)
> $$
>
> for each fixed $\theta$ at which $F$ is continuous. Thus $U$ solves the Dirichlet problem for the disk $r < r_0$ in the sense that $U$ is harmonic and approaches the boundary value $F(\theta)$ as $(r, \theta)$ approaches $(r_0, \theta)$ along a radius, except at the finitely many points where $F$ may be discontinuous.
>
> *B&C: Sec. 135 (text)*

^thm-135-1

> [!proof]+ Proof
> **$U$ is harmonic.** Since $F$ is piecewise continuous, (1) is a sum of finitely many definite integrals, each with an integrand continuous in $r$, $\theta$ and $\phi$, whose partial derivatives with respect to $r$ and $\theta$ are also continuous. So the order of integration and differentiation with respect to $r$ and $\theta$ can be interchanged; and since $P$ satisfies Laplace's equation in polar coordinates ([[§134★ Poisson Integral Formula#^prop-134-2|Proposition §134.2]](c); [[§27★ Harmonic Functions|§27★]], Exercise 1)
>
> $$
> r^2P_{rr} + rP_r + P_{\theta\theta} = 0 ,
> $$
>
> $U$ satisfies it too. (The vault has no separate proof of the rule for differentiating under the integral sign; here is a direct check that avoids it.) By Proposition §134.2(b), $U = \operatorname{Re} G$ with
>
> $$
> G(z) = \frac{1}{2\pi}\int_0^{2\pi}\frac{s + z}{s - z}F(\phi)\,d\phi, \qquad s = r_0e^{i\phi} .
> $$
>
> For $|z| < r_0$ and $0 < |h| < \frac12(r_0 - |z|)$, $\frac{s + z + h}{s - z - h} - \frac{s + z}{s - z} = \frac{2sh}{(s - z - h)(s - z)}$, so
>
> $$
> \frac{G(z + h) - G(z)}{h} - \frac{1}{2\pi}\int_0^{2\pi}\frac{2s\,F(\phi)}{(s - z)^2}\,d\phi = \frac{1}{2\pi}\int_0^{2\pi}\frac{2s\,h\,F(\phi)}{(s - z - h)(s - z)^2}\,d\phi ,
> $$
>
> whose modulus is at most $2r_0|h|\,\max|F|\big/\big(\frac12(r_0 - |z|)^3\big) \to 0$. So $G$ is analytic in the disk and $U = \operatorname{Re} G$ is harmonic ([[§27★ Harmonic Functions|§27★]]).
>
> **The boundary limit.** Let $F$ be continuous at $\theta$, and let $\varepsilon > 0$. We need $\delta > 0$ with
>
> $$
> |U(r, \theta) - F(\theta)| < \varepsilon \qquad\text{whenever}\qquad 0 < r_0 - r < \delta . \qquad (3)
> $$
>
> By property (f) of Proposition §134.2, $F(\theta) = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)F(\theta)\,d\phi$, so
>
> $$
> U(r, \theta) - F(\theta) = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\big[F(\phi) - F(\theta)\big]\,d\phi .
> $$
>
> Extend $F$ periodically with period $2\pi$, so that the integrand is periodic in $\phi$ and any interval of length $2\pi$ may be used; and take $0 < r < r_0$. Since $F$ is continuous at $\theta$, there is a small $\alpha > 0$ ($\alpha < \pi$) with
>
> $$
> |F(\phi) - F(\theta)| < \frac\varepsilon2 \qquad\text{whenever}\qquad |\phi - \theta| \le \alpha . \qquad (4)
> $$
>
> Write
>
> $$
> U(r, \theta) - F(\theta) = I_1(r) + I_2(r) , \qquad (5)
> $$
>
> $$
> I_1(r) = \frac{1}{2\pi}\int_{\theta-\alpha}^{\theta+\alpha}P(r_0, r, \phi - \theta)\big[F(\phi) - F(\theta)\big]\,d\phi, \qquad I_2(r) = \frac{1}{2\pi}\int_{\theta+\alpha}^{\theta-\alpha+2\pi}P(r_0, r, \phi - \theta)\big[F(\phi) - F(\theta)\big]\,d\phi .
> $$
>
> *Near $\phi = \theta$.* Since $P > 0$ (property (a)), by (4) and property (f),
>
> $$
> |I_1(r)| \le \frac{1}{2\pi}\int_{\theta-\alpha}^{\theta+\alpha}P\,|F(\phi) - F(\theta)|\,d\phi < \frac{\varepsilon}{4\pi}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,d\phi = \frac\varepsilon2 .
> $$
>
> *Away from $\phi = \theta$.* B&C notes from the geometry (its Fig. 192) that the denominator $|s - z|^2$ of $P$ in (8) of §134 has a positive minimum $m$ as $\phi$ varies over $\theta + \alpha \le \phi \le \theta - \alpha + 2\pi$. (That minimum must not depend on $r$; here is a bound that does not.) On that interval $\cos(\phi - \theta) \le \cos\alpha$, so
>
> $$
> |s - z|^2 = r_0^2 - 2r_0r\cos(\phi - \theta) + r^2 \ge r_0^2 - 2r_0r\cos\alpha + r^2 = (r - r_0\cos\alpha)^2 + r_0^2\sin^2\alpha \ge r_0^2\sin^2\alpha =: m > 0 .
> $$
>
> Let $M$ be an upper bound of the piecewise continuous function $|F(\phi) - F(\theta)|$ on $0 \le \phi \le 2\pi$ (if $M = 0$ there is nothing to prove). Since $r_0^2 - r^2 = (r_0 + r)(r_0 - r) < 2r_0(r_0 - r)$,
>
> $$
> |I_2(r)| \le \frac{(r_0^2 - r^2)M}{2\pi m}\,2\pi < \frac{2Mr_0}{m}(r_0 - r) < \frac{2Mr_0}{m}\delta = \frac\varepsilon2
> $$
>
> whenever $r_0 - r < \delta$, where
>
> $$
> \delta = \frac{m\varepsilon}{4Mr_0} . \qquad (6)
> $$
>
> *Conclusion.* $|U(r, \theta) - F(\theta)| \le |I_1(r)| + |I_2(r)| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon$ whenever $r_0 - r < \delta$: statement (3) holds with the choice (6).

^pf-135-1

*Uses:* [[§135★ Dirichlet Problem for a Disk#^def-135-1|Def. §135.1]], [[§134★ Poisson Integral Formula#^prop-134-2|§134.2]], [[§27★ Harmonic Functions|§27★]]

> [!remark]- Connections
> - [[§39 Potential in a Disk#^thm-39-2|341 Thm. §39.2]] solves the same problem by separation of variables, and [[§39 Potential in a Disk#^thm-39-3|341 Thm. §39.3]] sums the series into the Poisson integral; it checks the boundary values through uniform convergence of the series, which needs $f$ continuous and sectionally smooth. The proof above needs only piecewise continuity: it uses that the kernel is a positive weight of mass one concentrating at $\phi = \theta$ ([[§39 Potential in a Disk#^rem-39-2|341 Remark: The Poisson Kernel Is a Weight]]).
> - In terms of [[§135★ Dirichlet Problem for a Disk#^prop-135-4|Proposition §135.4]], the theorem says that the Fourier series of a piecewise continuous $F$, with its $n$th term damped by $(r/r_0)^n$, tends to $F(\theta)$ as $r \to r_0$ at every point of continuity (Abel summability). The undamped series converges at such points only under a local condition such as sectional smoothness, [[§12★ Proof of Convergence#^thm-12-4|341 Thm. §12.4]].

> [!theorem] Corollary §135.2: Mean Value at the Center
> According to (1), and since $P(r_0, 0, \phi - \theta) = 1$,
>
> $$
> U(0, \theta) = \frac{1}{2\pi}\int_0^{2\pi}F(\phi)\,d\phi .
> $$
>
> Thus the value of the harmonic function $U$ at the center of the circle $r = r_0$ is the average of its boundary values on the circle.
>
> *B&C: Sec. 135 (text)*

^cor-135-2

> [!proof]+ Proof
> Set $r = 0$ in (1) and use property (e) of [[§134★ Poisson Integral Formula#^prop-134-2|Proposition §134.2]].

^pf-135-2

*Uses:* [[§134★ Poisson Integral Formula#^prop-134-2|§134.2]]

## Series Representations

The kernel and the solution can be expanded in the elementary harmonic functions $r^n\cos n\theta$ and $r^n\sin n\theta$. (B&C leaves the proofs to its Exercises 6 and 7 of Sec. 136, and notes that these results are obtained, for $r_0 = 1$, by separation of variables in its *Fourier Series and Boundary Value Problems*; that derivation is [[§39 Potential in a Disk#^thm-39-2|341 Thm. §39.2]].)

> [!theorem] Proposition §135.3: Series for the Poisson Kernel
> For $r < r_0$,
>
> $$
> P(r_0, r, \phi - \theta) = 1 + 2\sum_{n=1}^{\infty}\Big(\frac{r}{r_0}\Big)^n\cos n(\phi - \theta) , \qquad (7)
> $$
>
> and the series converges uniformly with respect to $\phi$.
>
> *B&C: Sec. 135, equation (7); Sec. 136, Exercises 6 and 7*

^prop-135-3

> [!proof]+ Proof
> Let $-1 < a < 1$. (This is the sum in Exercise 7(b) of B&C's Sec. 68; for $0 \le a < 1$ it is [[§61 Convergence of Series#^ex-61-2|Example §61.2]].) The geometric series $\sum_{n\ge1}(ae^{i\psi})^n$ converges since $|ae^{i\psi}| < 1$, and its real part is
>
> $$
> \sum_{n=1}^{\infty}a^n\cos n\psi = \operatorname{Re}\frac{ae^{i\psi}}{1 - ae^{i\psi}} = \operatorname{Re}\frac{ae^{i\psi}(1 - ae^{-i\psi})}{|1 - ae^{i\psi}|^2} = \frac{a\cos\psi - a^2}{1 - 2a\cos\psi + a^2} .
> $$
>
> Hence
>
> $$
> 1 + 2\sum_{n=1}^{\infty}a^n\cos n\psi = \frac{1 - 2a\cos\psi + a^2 + 2a\cos\psi - 2a^2}{1 - 2a\cos\psi + a^2} = \frac{1 - a^2}{1 - 2a\cos\psi + a^2} .
> $$
>
> With $a = r/r_0$ and $\psi = \phi - \theta$, multiplying numerator and denominator by $r_0^2$ gives (7) of §134, the Poisson kernel. Since $|a^n\cos n\psi| \le |a|^n$ and $\sum|a|^n < \infty$, the Weierstrass M-test shows that the convergence is uniform in $\psi$, hence in $\phi$.

^pf-135-3

*Uses:* [[§134★ Poisson Integral Formula#^def-134-2|Def. §134.2]], [[§61 Convergence of Series#^ex-61-1|Ex. §61.1]] (geometric series), [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]] (M-test)

> [!theorem] Proposition §135.4: Series for the Solution
> The Poisson integral transform (1) of a piecewise continuous $F$ is
>
> $$
> U(r, \theta) = \frac12a_0 + \sum_{n=1}^{\infty}\Big(\frac{r}{r_0}\Big)^n(a_n\cos n\theta + b_n\sin n\theta) \qquad (r < r_0) , \qquad (8)
> $$
>
> where
>
> $$
> a_n = \frac1\pi\int_0^{2\pi}F(\phi)\cos n\phi\,d\phi \quad (n = 0, 1, 2, \ldots), \qquad (9) \qquad\qquad b_n = \frac1\pi\int_0^{2\pi}F(\phi)\sin n\phi\,d\phi \quad (n = 1, 2, \ldots) . \qquad (10)
> $$
>
> *B&C: Sec. 135, equations (8)–(10); Sec. 136, Exercise 7*

^prop-135-4

> [!proof]+ Proof
> Substitute (7) into (1). The series (7) converges uniformly in $\phi$, and $F$ is bounded, so the series obtained by multiplying its terms by $F(\phi)$ also converges uniformly (its tail is at most $\max|F|$ times the tail of (7)). A uniformly convergent series of integrable functions can be integrated term by term, so
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi}F(\phi)\,d\phi + \sum_{n=1}^{\infty}\Big(\frac{r}{r_0}\Big)^n\frac1\pi\int_0^{2\pi}F(\phi)\cos n(\phi - \theta)\,d\phi .
> $$
>
> The first term is $\frac12a_0$. Since $\cos n(\phi - \theta) = \cos n\phi\cos n\theta + \sin n\phi\sin n\theta$, the $n$th integral is $a_n\cos n\theta + b_n\sin n\theta$. This is (8).

^pf-135-4

*Uses:* [[§135★ Dirichlet Problem for a Disk#^prop-135-3|§135.3]], [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]] (integrating a uniformly convergent series)

> [!remark] Remark: Method — Dirichlet Problem in a Disk
> To find the function $U$ harmonic in $r < r_0$ with boundary values $F(\theta)$:
> 1. **Polar form.** Write the boundary data as a function $F(\phi)$ on $0 \le \phi \le 2\pi$; piecewise continuous data (a split cylinder, a heated arc) are allowed.
> 2. **Poisson integral.** If $F$ is piecewise constant, integrate (1) with the antiderivative of the kernel ([[§136★ Examples (Dirichlet Problem for a Disk)#^lem-136-1|Lemma §136.1]]) and simplify $\tan\pi U$; the range $0 < U < 1$ (from $P > 0$ and property (f)) fixes the branch of the arctangent.
> 3. **Series.** If $F$ is a trigonometric polynomial, or its Fourier coefficients are easy, use (8)–(10): multiply the $n$th harmonic by $(r/r_0)^n$. Then $r^n\cos n\theta = \operatorname{Re} z^n$ converts the answer to $x$, $y$.
> 4. **Checks.** $U(0, \theta)$ must be the mean of $F$ (Corollary §135.2), and $U \to F$ along radii at points of continuity.
> 5. **Other regions.** Map the region conformally onto the disk (or use [[§137★ Related Boundary Value Problems|§137★]] for semicircles and exteriors).

^rem-135-1

## Examples

> [!example] Example §135.1: Boundary Values sin² θ
> Find the function harmonic in $r < r_0$ with $U(r_0, \theta) = \sin^2\theta$.
>
> Since $\sin^2\phi = \frac12 - \frac12\cos2\phi$, orthogonality gives in (9)–(10): $a_0 = \frac1\pi\int_0^{2\pi}\sin^2\phi\,d\phi = 1$, $a_2 = \frac1\pi\int_0^{2\pi}\sin^2\phi\cos2\phi\,d\phi = -\frac12$, and all other coefficients are $0$. By (8),
>
> $$
> U(r, \theta) = \frac12 - \frac12\Big(\frac{r}{r_0}\Big)^2\cos2\theta = \frac12 - \frac{x^2 - y^2}{2r_0^2} .
> $$
>
> *Check:* $\nabla^2(x^2 - y^2) = 2 - 2 = 0$; at $r = r_0$ the value is $\frac12 - \frac12\cos2\theta = \sin^2\theta$; and $U(0) = \frac12$, the mean of $\sin^2$.
>
> *B&C: Sec. 135, equations (8)–(10)*

^ex-135-1

> [!example] Example §135.2: At a Jump of the Boundary Values
> Let $F(\phi) = 1$ for $0 < \phi < \pi$ and $F(\phi) = 0$ for $\pi < \phi < 2\pi$. Show that along the radius $\theta = 0$, which ends at a jump of $F$, $U(r, 0) = \frac12$ for every $r < r_0$.
>
> By (1) with $\theta = 0$, $U(r, 0) = \frac{1}{2\pi}\int_0^{\pi}P(r_0, r, \phi)\,d\phi$. Since $P$ is even in $\phi$ (property (d)), $\int_0^\pi P = \frac12\int_{-\pi}^{\pi}P = \frac12\cdot2\pi$ by property (f). So $U(r, 0) = \frac12$, and the radial limit at this jump is the average of the one-sided limits $1$ and $0$. Theorem §135.1 makes no claim at points of discontinuity; at a jump the limit along a radius is this average (the kernel is symmetric about $\phi = \theta$), while along other paths into the jump point $U$ can tend to any value between $0$ and $1$ (by [[§136★ Examples (Dirichlet Problem for a Disk)#^ex-136-1|Example §136.1]], the level curves of $U$ are circular arcs through the jump points).
>
> *B&C: Sec. 135, equation (1)*

^ex-135-2

> [!example] Example §135.3: The Kernel as the Response to a Concentrated Boundary Value
> Let $I$ be the finite unit impulse function
>
> $$
> I(h, \theta - \theta_0) = \begin{cases} 1/h, & \theta_0 \le \theta \le \theta_0 + h, \\ 0, & 0 \le \theta < \theta_0 \ \text{or} \ \theta_0 + h < \theta \le 2\pi, \end{cases}
> $$
>
> with $h > 0$ and $0 \le \theta_0 < \theta_0 + h < 2\pi$, so that $\int_{\theta_0}^{\theta_0+h}I(h, \theta - \theta_0)\,d\theta = 1$. Show that
>
> $$
> \lim_{h\to0^+}\int_0^{2\pi}P(r_0, r, \phi - \theta)\,I(h, \phi - \theta_0)\,d\phi = P(r_0, r, \theta - \theta_0) \qquad (r < r_0) .
> $$
>
> For fixed $r < r_0$ and $\theta$, $P(r_0, r, \phi - \theta)$ is continuous in $\phi$ and $I \ge 0$, so by the mean value theorem for definite integrals there is $c$ with $\theta_0 \le c \le \theta_0 + h$ and
>
> $$
> \int_0^{2\pi}P(r_0, r, \phi - \theta)\,I(h, \phi - \theta_0)\,d\phi = P(r_0, r, c - \theta)\int_{\theta_0}^{\theta_0+h}I(h, \phi - \theta_0)\,d\phi = P(r_0, r, c - \theta) .
> $$
>
> As $h \to 0^+$, $c \to \theta_0$, and by continuity and evenness of $P$ the limit is $P(r_0, r, \theta_0 - \theta) = P(r_0, r, \theta - \theta_0)$. The left side is the Poisson integral (1) of the boundary values $2\pi I(h, \theta - \theta_0)$. So the Poisson kernel $P(r_0, r, \theta - \theta_0)$ is the limit of the harmonic functions in the disk whose boundary values are the impulses $2\pi I(h, \theta - \theta_0)$: the potential produced by a concentrated boundary value at $\theta_0$.
>
> *B&C: Sec. 136, Exercise 5*

^ex-135-3
