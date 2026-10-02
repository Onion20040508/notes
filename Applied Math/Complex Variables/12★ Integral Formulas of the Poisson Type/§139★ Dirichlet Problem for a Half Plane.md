---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 139
bc: "139"
aliases: ["B&C 139"]
tags: [complex-variables, math342, extension]
---
← [[§138★ Schwarz Integral Formula]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§140★ Neumann Problems]] →

*Brown–Churchill, Section 139.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The Schwarz integral formula of [[§138★ Schwarz Integral Formula|§138★]] was derived for the real part of a decaying analytic function. Here it is turned into a solution method, as the Poisson formula was in [[§135★ Dirichlet Problem for a Disk|§135★]]: for any bounded boundary function with finitely many jumps, the Schwarz integral transform is a bounded harmonic function in the upper half plane that takes the boundary values at every point of continuity. The proof substitutes $t = x + y\tan\tau$, which turns the kernel into the uniform weight $d\tau/\pi$ on $(-\pi/2, \pi/2)$, and then splits the $\tau$ interval as in the disk case. Odd and even extensions give the quarter plane; physically, this covers steady temperatures in a half plane or quadrant, and the potential of a grounded plane with a strip held at a different voltage.

> [!definition] Definition §139.1: Schwarz Integral Transform
> Let $F$ be a real-valued function of $x$, bounded for all $x$ and continuous except for at most a finite number of finite jumps. The **Schwarz integral transform** of $F$ is
>
> $$
> U(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{y\,F(t)}{(t - x)^2 + y^2}\,dt \qquad (y > 0) , \qquad (1)
> $$
>
> suggested by (7) of [[§138★ Schwarz Integral Formula#^thm-138-2|Theorem §138.2]]. Except for the factor $1/\pi$, its kernel $y/|t - z|^2$ is the imaginary component of $1/(t - z)$.
>
> *B&C: Sec. 139, equation (1)*

^def-139-1

> [!theorem] Theorem §139.1: Solution of the Dirichlet Problem for a Half Plane
> The Schwarz integral transform $U$ of such an $F$ is harmonic in the half plane $y > 0$,
>
> $$
> \lim_{\substack{y\to0\\ y > 0}}U(x, y) = F(x) \qquad (2)
> $$
>
> for each fixed $x$ at which $F$ is continuous, and $|U(x, y)| \le M$ in the half plane, where $M$ is an upper bound of $|F|$. In particular, $U(x, y) = F_0$ when $F(x) = F_0$ is constant.
>
> *B&C: Sec. 139 (text)*

^thm-139-1

> [!proof]+ Proof
> **Convergence.** For $y > 0$ the weight $dt/\big((t - x)^2 + y^2\big)$ has finite total mass $\pi/y$, and $F$ is bounded and integrable on bounded intervals, so the integral (1) converges ([[§36 Improper Integrals#^thm-36-2|451 Thm. §36.2]]).
>
> **$U$ is harmonic.** Let $I(x, y) = \int_{-\infty}^\infty F(t)\,dt/\big((t - x)^2 + y^2\big)$, so that $U = \frac y\pi I$. B&C argues: when $y \ge \varepsilon$ and $|x| \le 1/\varepsilon$ ($\varepsilon$ any positive constant), this integral converges uniformly with respect to $x$ and $y$, and so do the integrals of the partial derivatives of the integrand with respect to $x$ and $y$; each is a finite sum of improper or definite integrals over intervals where $F$ is continuous, with integrands continuous in $t$, $x$, $y$. Consequently each partial derivative of $I$ is the integral of the corresponding derivative of the integrand, whenever $y > 0$. (The uniform bound that makes this work: for $y \ge \varepsilon$, $|x| \le 1/\varepsilon$, the integrand and its first and second partial derivatives in $x$ and $y$ are bounded by $C_\varepsilon/(1 + t^2)$, which is integrable, so differentiation under the integral sign is justified by dominated convergence, [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]].) The kernel $y/|t - z|^2 = \operatorname{Im}\frac{1}{t - z}$ is the imaginary part of a function analytic in $z$ for $y > 0$, so it is harmonic and satisfies Laplace's equation in $x$ and $y$ ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]). Since differentiation and integration may be interchanged, $U$ satisfies Laplace's equation too.
>
> **A substitution.** Substitute $t = x + y\tan\tau$, $-\pi/2 < \tau < \pi/2$, so that $dt = y\sec^2\tau\,d\tau$ and $(t - x)^2 + y^2 = y^2\sec^2\tau$:
>
> $$
> U(x, y) = \frac1\pi\int_{-\pi/2}^{\pi/2}F(x + y\tan\tau)\,d\tau \qquad (y > 0) . \qquad (3)
> $$
>
> From (3), $|U| \le \frac1\pi\cdot\pi M = M$: $U$ is bounded; and $U = F_0$ when $F \equiv F_0$.
>
> **The boundary limit.** Fix $x$ where $F$ is continuous, let $G(x, y, \tau) = F(x + y\tan\tau) - F(x)$, and let $\alpha$ be a small positive constant. Then
>
> $$
> \pi\big[U(x, y) - F(x)\big] = \int_{-\pi/2}^{\pi/2}G(x, y, \tau)\,d\tau = I_1(y) + I_2(y) + I_3(y) , \qquad (4)
> $$
>
> where $I_1$, $I_2$, $I_3$ are the integrals over $\big(-\frac\pi2, -\frac\pi2 + \alpha\big)$, $\big(-\frac\pi2 + \alpha, \frac\pi2 - \alpha\big)$ and $\big(\frac\pi2 - \alpha, \frac\pi2\big)$. Since $|G| \le 2M$: given $\varepsilon > 0$, choose $\alpha$ with $6M\alpha < \varepsilon$; then
>
> $$
> |I_1(y)| \le 2M\alpha < \frac\varepsilon3, \qquad |I_3(y)| \le 2M\alpha < \frac\varepsilon3 .
> $$
>
> Since $F$ is continuous at $x$, there is $\gamma > 0$ with $|G(x, y, \tau)| < \frac{\varepsilon}{3\pi}$ whenever $0 < y|\tan\tau| < \gamma$. As $\tau$ ranges from $-\frac\pi2 + \alpha$ to $\frac\pi2 - \alpha$, the maximum of $|\tan\tau|$ is $\tan\big(\frac\pi2 - \alpha\big) = \cot\alpha$. So with $\delta = \gamma\tan\alpha$, $0 < y < \delta$ gives $y|\tan\tau| < \gamma$ throughout the middle interval, and
>
> $$
> |I_2(y)| < \frac{\varepsilon}{3\pi}(\pi - 2\alpha) < \frac\varepsilon3 \qquad\text{whenever}\qquad 0 < y < \delta .
> $$
>
> Hence $|I_1(y)| + |I_2(y)| + |I_3(y)| < \varepsilon$ whenever $0 < y < \delta$, and (2) follows from (4).

^pf-139-1

*Uses:* [[§139★ Dirichlet Problem for a Half Plane#^def-139-1|Def. §139.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§36 Improper Integrals#^thm-36-2|451 Thm. §36.2]] (bounded integrand against a finite weight), [[§15 The General Lebesgue Integral#^thm-15-8|551 Thm. §15.8]] (dominated convergence)

> [!remark]- Connections
> - [[§38 Potential in Unbounded Regions#^rem-38-2|341 Remark: The Half-Plane and Its Poisson Formula]] reaches (1) from a Fourier integral and states it; Theorem §139.1 is the proof that it solves the Dirichlet problem for bounded data with jumps. The disk version is [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]], with the same three-part splitting.

Expression (1) therefore solves the Dirichlet problem for the half plane $y > 0$, with the boundary condition (2).

> [!theorem] Proposition §139.2: The Harmonic Conjugate
> If, in addition, $F$ satisfies an order property $|x^aF(x)| < M$ for some $a > 0$, then
>
> $$
> V(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{(x - t)\,F(t)}{(t - x)^2 + y^2}\,dt \qquad (y > 0) \qquad (5)
> $$
>
> is a harmonic conjugate of the function $U$ of (1).
>
> *B&C: Sec. 139, equation (5)*

^prop-139-2

> [!proof]+ Proof
> B&C says that under these conditions $U$ and $V$ satisfy the Cauchy–Riemann equations when $y > 0$; here is a direct way to see it. Since $y + i(x - t) = i(\overline z - t)$ and $(t - z)(t - \overline z) = |t - z|^2$,
>
> $$
> \frac{y + i(x - t)}{|t - z|^2} = \frac{-i(t - \overline z)}{(t - z)(t - \overline z)} = \frac{-i}{t - z} ,
> $$
>
> so
>
> $$
> U(x, y) + iV(x, y) = \frac{1}{\pi i}\int_{-\infty}^{\infty}\frac{F(t)\,dt}{t - z} =: \Phi(z) .
> $$
>
> The order property makes $F(t)/(t - z) = O(|t|^{-1 - a})$, so the integral converges absolutely, uniformly for $z$ in any closed disk $D$ in the upper half plane. The function $\Phi$ is analytic there: its difference quotient differs from $\frac{1}{\pi i}\int F(t)\,dt/(t - z)^2$ by $\frac{h}{\pi i}\int F(t)\,dt/\big((t - z - h)(t - z)^2\big)$, which tends to $0$ with $h$ (the integrand is bounded by a constant times $|F(t)|/(1 + |t|)^3$ for $z$ in $D$ and small $h$). So $U = \operatorname{Re}\Phi$ and $V = \operatorname{Im}\Phi$ satisfy the Cauchy–Riemann equations, and $V$ is a harmonic conjugate of $U$.

^pf-139-2

*Uses:* [[§139★ Dirichlet Problem for a Half Plane#^def-139-1|Def. §139.1]], [[§138★ Schwarz Integral Formula#^thm-138-2|§138.2]]

> [!remark] Remark: Method — Dirichlet Problem for a Half Plane or Quadrant
> 1. **Half plane $y > 0$.** For bounded data $F$ with finitely many jumps, $U$ is the integral (1). For piecewise constant $F$ integrate with $\int\frac{y\,dt}{(t - x)^2 + y^2} = \arctan\frac{t - x}{y}$; each jump of $F$ contributes an angle subtended at $z$.
> 2. **Quadrant $x > 0$, $y > 0$.** Extend $F$ from $x > 0$ to the whole line, oddly if $U$ must vanish on $x = 0$, evenly if $U_x$ must vanish there, and fold (1) back to an integral over $t > 0$ ([[§139★ Dirichlet Problem for a Half Plane#^ex-139-2|Example §139.2]], [[§139★ Dirichlet Problem for a Half Plane#^ex-139-3|Example §139.3]]).
> 3. **Data on both edges.** Superpose a solution with data on one edge and zero on the other, and one with the roles exchanged.
> 4. **Other half planes.** Interchange or rotate the axes ([[§139★ Dirichlet Problem for a Half Plane#^ex-139-4|Example §139.4]]); for other regions, map conformally onto the half plane.
> 5. **Checks.** $U$ is bounded by $\sup|F|$, and $U \to F$ at points of continuity of $F$.

^rem-139-1

## Examples

> [!example] Example §139.1: Boundary Values with One Jump
> Find the bounded harmonic function in $y > 0$ with $F(x) = 1$ for $x > 0$ and $F(x) = 0$ for $x < 0$.
>
> By (1),
>
> $$
> U(x, y) = \frac1\pi\int_0^\infty\frac{y\,dt}{(t - x)^2 + y^2} = \frac1\pi\Big[\arctan\frac{t - x}{y}\Big]_{t=0}^{t\to\infty} = \frac12 + \frac1\pi\arctan\frac xy .
> $$
>
> With $z = re^{i\theta}$, $\arctan(x/y) = \frac\pi2 - \theta$, so $U = 1 - \theta/\pi$: the harmonic function that is constant on rays from the origin, $1$ on the positive and $0$ on the negative axis. At the jump $x = 0$ the limit along the vertical is $\frac12$. This is the example in [[§38 Potential in Unbounded Regions#^rem-38-2|341 Remark: The Half-Plane and Its Poisson Formula]]; at $(0.7, 0.4)$ quadrature of (1) and the closed form both give $0.834751$.
>
> *B&C: Sec. 139, equation (1)*

^ex-139-1

> [!example] Example §139.2: A Quadrant with One Edge at Zero
> **(a)** Obtain as a special case of (1) the bounded function harmonic in the first quadrant with $U(0, y) = 0$ ($y > 0$) and $\lim_{y\to0^+}U(x, y) = F(x)$ ($x > 0$, $x \ne x_j$), for $F$ bounded on $x > 0$ and continuous except for finite jumps at $x_1, \ldots, x_n$:
>
> $$
> U(x, y) = \frac y\pi\int_0^\infty\Big[\frac{1}{(t - x)^2 + y^2} - \frac{1}{(t + x)^2 + y^2}\Big]F(t)\,dt \qquad (x > 0,\ y > 0) .
> $$
>
> **(b)** For the bounded steady temperatures $T$ in a plate $x > 0$, $y > 0$ with insulated faces, $T \to F_1(x)$ on the $x$ axis and $T \to F_2(y)$ on the $y$ axis ($F_1$, $F_2$ bounded with finitely many jumps), show that with $z = x + iy$, $T = T_1 + T_2$ where
>
> $$
> T_1(x, y) = \frac y\pi\int_0^\infty\Big[\frac{1}{|t - z|^2} - \frac{1}{|t + z|^2}\Big]F_1(t)\,dt, \qquad T_2(x, y) = \frac x\pi\int_0^\infty\Big[\frac{1}{|it - z|^2} - \frac{1}{|it + z|^2}\Big]F_2(t)\,dt .
> $$
>
> **(a)** Extend $F$ to an odd function, $F(-t) = -F(t)$; it is still bounded with finitely many jumps. In (1) split the integral at $0$ and substitute $t \mapsto -t$ in the part over $t < 0$: it becomes $\frac1\pi\int_0^\infty\frac{y\,F(-t)}{(t + x)^2 + y^2}\,dt = -\frac1\pi\int_0^\infty\frac{y\,F(t)}{(t + x)^2 + y^2}\,dt$. Adding the part over $t > 0$ gives the formula. It is harmonic, bounded, and tends to $F(x)$ at points of continuity by Theorem §139.1; and at $x = 0$ the bracket vanishes, so $U(0, y) = 0$.
>
> **(b)** $T_1$ is the function of (a) with $F = F_1$, written with $(t \mp x)^2 + y^2 = |t \mp z|^2$: it is $0$ on the $y$ axis and tends to $F_1$ on the $x$ axis. $T_2$ is the same construction with the axes interchanged: reflecting in the line $y = x$ (which preserves harmonicity) turns the problem "$F_2$ on the $y$ axis, $0$ on the $x$ axis" into (a), and $(t - y)^2 + x^2 = |it - z|^2$, $(t + y)^2 + x^2 = |it + z|^2$. So $T_2$ vanishes on the $x$ axis and tends to $F_2$ on the $y$ axis, and the sum $T$ has both boundary values.
>
> *Check:* for $F = 1$ on $x > 0$, (a) gives $U = \frac1\pi\big[\big(\frac\pi2 + \arctan\frac xy\big) - \big(\frac\pi2 - \arctan\frac xy\big)\big] = \frac2\pi\arctan\frac xy = 1 - \frac{2\theta}{\pi}$, which is $1$ on the positive $x$ axis and $0$ on the positive $y$ axis; at $(0.7, 0.4)$ quadrature gives $0.669501$, the same. With $F_2 = 1$ the $T_2$ formula must give $\frac{2\theta}{\pi} = \frac2\pi\arctan\frac yx$, and $\frac x\pi\int_0^\infty\big[\frac{1}{(t - y)^2 + x^2} - \frac{1}{(t + y)^2 + x^2}\big]dt$ does; the factor $y/\pi$ would not.
>
> *B&C prints the factor in front of the $T_2$ integral as $y/\pi$; the interchange of axes gives $x/\pi$, as the check shows.*
>
> *B&C: Sec. 139, Exercises 1 and 2*

^ex-139-2

> [!example] Example §139.3: A Quadrant with One Edge Insulated
> Obtain the bounded function harmonic in the first quadrant with $U_x(0, y) = 0$ ($y > 0$) and $\lim_{y\to0^+}U(x, y) = F(x)$ ($x > 0$, $x \ne x_j$):
>
> $$
> U(x, y) = \frac y\pi\int_0^\infty\Big[\frac{1}{(t - x)^2 + y^2} + \frac{1}{(t + x)^2 + y^2}\Big]F(t)\,dt \qquad (x > 0,\ y > 0) .
> $$
>
> Extend $F$ evenly, $F(-t) = F(t)$, and fold (1) as in Example §139.2; now the part over $t < 0$ contributes $+\frac1\pi\int_0^\infty\frac{yF(t)}{(t + x)^2 + y^2}dt$. The resulting $U$ is even in $x$, so $U_x(0, y) = 0$: the edge $x = 0$ is insulated. For instance, with $F = 1$ on $0 < x < 1$ and $F = 0$ for $x > 1$,
>
> $$
> U(x, y) = \frac1\pi\Big[\arctan\frac{x + 1}{y} - \arctan\frac{x - 1}{y}\Big] ,
> $$
>
> the half-plane solution for data $1$ on $|x| < 1$, which is even in $x$.
>
> *B&C: Sec. 139, Exercise 3*

^ex-139-3

> [!example] Example §139.4: The Right Half Plane and a Conjugate
> Interchanging the $x$ and $y$ axes in (1) gives the solution of the Dirichlet problem for the half plane $x > 0$:
>
> $$
> U(x, y) = \frac1\pi\int_{-\infty}^{\infty}\frac{x\,F(t)}{(t - y)^2 + x^2}\,dt \qquad (x > 0) .
> $$
>
> Take $F(y) = 1$ for $|y| < 1$ and $F(y) = 0$ for $|y| > 1$. Show that
>
> $$
> U(x, y) = \frac1\pi\Big[\arctan\frac{y + 1}{x} - \arctan\frac{y - 1}{x}\Big] , \qquad V(x, y) = \frac{1}{2\pi}\ln\frac{x^2 + (y + 1)^2}{x^2 + (y - 1)^2}
> $$
>
> ($-\pi/2 \le \arctan t \le \pi/2$), that $-V$ is a harmonic conjugate of $U$, and that $V + iU = \frac1\pi\big[\operatorname{Log}(z + i) - \operatorname{Log}(z - i)\big]$.
>
> **$U$.** $\displaystyle\frac1\pi\int_{-1}^{1}\frac{x\,dt}{(t - y)^2 + x^2} = \frac1\pi\Big[\arctan\frac{t - y}{x}\Big]_{-1}^{1} = \frac1\pi\Big[\arctan\frac{1 - y}{x} + \arctan\frac{1 + y}{x}\Big]$, which is the stated form since $\arctan$ is odd.
>
> **The analytic function.** For $x > 0$ the points $z \pm i$ lie in the right half plane, where $\operatorname{Log}$ is analytic and $\operatorname{Arg}(z \pm i) = \arctan\frac{y \pm 1}{x}$. So
>
> $$
> \frac1\pi\big[\operatorname{Log}(z + i) - \operatorname{Log}(z - i)\big] = \frac1\pi\ln\frac{|z + i|}{|z - i|} + \frac i\pi\Big[\arctan\frac{y + 1}{x} - \arctan\frac{y - 1}{x}\Big] = V + iU ,
> $$
>
> since $\frac1\pi\ln\frac{|z + i|}{|z - i|} = \frac{1}{2\pi}\ln\frac{x^2 + (y + 1)^2}{x^2 + (y - 1)^2}$. As $V + iU$ is analytic, so is $-i(V + iU) = U - iV$: hence $-V$ is a harmonic conjugate of $U$. At $(0.5, 0.3)$, quadrature gives $U = 0.685693$ and the logarithms give $V = 0.153392$, $U = 0.685693$.
>
> *B&C: Sec. 139, Exercise 4*

^ex-139-4

![[m342-139-1.svg]]
*Level curves $U = 0.1, \ldots, 0.9$ of the solution of Example §139.4 in the right half plane, with $U = 1$ on the segment $|y| < 1$ of the $y$ axis (red) and $U = 0$ on the rest (blue). Each is an arc of a circle through $\pm i$: $U$ is $\frac1\pi$ times the angle subtended at $z$ by the segment from $-i$ to $i$.*
