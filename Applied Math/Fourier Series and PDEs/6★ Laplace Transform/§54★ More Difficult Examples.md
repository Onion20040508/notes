---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 6
section: 54
powers: "6.4"
aliases: ["Powers 6.4"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§53★ Partial Differential Equations]] · ↑ [[· 6★ Laplace Transform]] · [[§55★ Boundary Value Problems]] →

*Powers, Section 6.4.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Once mastered, separation of variables seems more straightforward than the Laplace transform. The transform has a distinct advantage when the boundary conditions depend on time or the equation is inhomogeneous, and this section gives three examples. In the first, a rod is attached to a well-stirred container of fluid, so the boundary condition contains $u_t$. The eigenfunctions are then not orthogonal, but the transform finds the coefficients anyway. In the second, a semi-infinite solid has a periodically varying surface temperature, and only the **persistent part** of the solution is wanted. It comes from the singular points with $\operatorname{Re}(s) \ge 0$ and describes temperature waves that decay and lag as they move into the solid. In the third, a wire is driven at one of its natural frequencies. $U$ then has a double pole, and the extended Heaviside formula produces a term $t\cos(\pi t)$ whose amplitude grows linearly: resonance.

## A Boundary Condition with a Time Derivative

A uniform insulated rod is attached at one end ($x = 0$) to an insulated container of fluid. The fluid is circulated so well that its temperature is uniform and equal to that at the end of the rod. The other end is kept at a constant temperature. Heat flowing out of the rod at $x = 0$ warms the fluid, so the flux there is proportional to the rate of change of the fluid temperature, $u_t(0, t)$. In dimensionless form the constant $\gamma > 0$ measures the heat capacity of the fluid relative to that of the rod. The problem is

$$
\frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < 1,\ 0 < t; \qquad \frac{\partial u}{\partial x}(0, t) = \gamma\frac{\partial u}{\partial t}(0, t), \quad u(1, t) = 1, \quad 0 < t; \qquad u(x, 0) = 0, \quad 0 < x < 1 .
$$

Its transform has the denominator $s\big(\cosh(\sqrt s) + \sqrt s\,\gamma\sinh(\sqrt s)\big)$, whose zeros are found first.

> [!theorem] Lemma §54.1: Zeros of the Denominator
> Let $\gamma > 0$ and $p(s) = s\big(\cosh(\sqrt s) + \sqrt s\,\gamma\sinh(\sqrt s)\big)$ (an even function of $\sqrt s$, so a function of $s$). The zeros of $p$ are $r_0 = 0$ and
>
> $$
> r_k = (i\eta_k)^2 = -\eta_k^2, \qquad k = 1, 2, \ldots ,
> $$
>
> where $\eta_1 < \eta_2 < \cdots$ are the positive solutions of
>
> $$
> \tan(\eta) = \frac{1}{\eta\gamma} .
> $$
>
> There is exactly one $\eta_k$ in each interval $\big((k - 1)\pi, (k - 1)\pi + \frac\pi2\big)$.
>
> *Powers: 6.4, Example 1 and Equations (1), (2)*

^lem-54-1

> [!proof]+ Proof
> The factor $s$ gives $r_0 = 0$, and the bracket is $1$ at $s = 0$. For the bracket, Powers notes that aside from $s = 0$ there are no real zeros. He means no real $\sqrt s$: for $s > 0$ both terms are positive. (The zeros found below are negative real values of $s$.) So put $\sqrt s = \xi + i\eta$ with $\xi$, $\eta$ real. By the addition formulas of [[§53★ Partial Differential Equations#^lem-53-2|Lemma §53.2]],
>
> $$
> \cosh(\xi + i\eta) = \cosh\xi\cos\eta + i\sinh\xi\sin\eta, \qquad \sqrt s\,\gamma\sinh(\sqrt s) = \gamma(\xi + i\eta)(\sinh\xi\cos\eta + i\cosh\xi\sin\eta) .
> $$
>
> Collecting real and imaginary parts, the bracket vanishes exactly when
>
> $$
> \big(\cosh(\xi) + \xi\gamma\sinh(\xi)\big)\cos(\eta) - \eta\gamma\cosh(\xi)\sin(\eta) = 0, \qquad (1)
> $$
>
> $$
> \eta\gamma\sinh(\xi)\cos(\eta) + \big(\sinh(\xi) + \xi\gamma\cosh(\xi)\big)\sin(\eta) = 0 . \qquad (2)
> $$
>
> Regard these as linear equations for $\cos\eta$ and $\sin\eta$. Since $\sin^2\eta + \cos^2\eta = 1$, the unknowns are not both zero, so the determinant must vanish:
>
> $$
> \big(\cosh\xi + \xi\gamma\sinh\xi\big)\big(\sinh\xi + \xi\gamma\cosh\xi\big) + \eta^2\gamma^2\sinh\xi\cosh\xi = 0 .
> $$
>
> Multiplying out (the "some algebra" of Powers), $(\cosh\xi + \xi\gamma\sinh\xi)(\sinh\xi + \xi\gamma\cosh\xi) = (1 + \xi^2\gamma^2)\sinh\xi\cosh\xi + \xi\gamma(\cosh^2\xi + \sinh^2\xi)$, so the condition is
>
> $$
> \big(1 + \xi^2\gamma^2 + \eta^2\gamma^2\big)\sinh(\xi)\cosh(\xi) + \xi\gamma\big(\sinh^2(\xi) + \cosh^2(\xi)\big) = 0 .
> $$
>
> If $\xi \ne 0$, both terms have the sign of $\xi$ ($\sinh\xi$ has the sign of $\xi$, $\cosh\xi > 0$, $\gamma > 0$), so their sum is not zero. The only solutions have $\xi = 0$. Then (2) holds automatically, and (1) reduces to $\cos\eta - \eta\gamma\sin\eta = 0$. Here $\cos\eta \ne 0$, since otherwise $\sin\eta = 0$ as well, so this is $\tan(\eta) = 1/(\eta\gamma)$; $\eta = 0$ is not a solution. Since $\eta$ and $-\eta$ give the same $s = (i\eta)^2 = -\eta^2$, only positive $\eta$ are needed.
>
> **Counting.** On $\big((k - 1)\pi, (k - 1)\pi + \frac\pi2\big)$, $\tan\eta$ increases continuously from $0$ to $+\infty$ while $1/(\eta\gamma)$ is positive and decreasing (from $+\infty$ when $k = 1$). So the two graphs cross exactly once. On $\big((k - 1)\pi + \frac\pi2, k\pi\big)$, $\tan\eta < 0 < 1/(\eta\gamma)$, and there is no solution.

^pf-54-1

*Uses:* [[§53★ Partial Differential Equations#^lem-53-2|§53.2]]

> [!example] Example §54.1: A Rod Attached to a Stirred Container
> Solve the problem above.
>
> **Transform and solve.** Since $u(0, 0) = 0$, $\mathcal{L}(\gamma u_t(0, t)) = s\gamma U(0, s)$, and the transformed problem is
>
> $$
> \frac{d^2U}{dx^2} = sU, \quad 0 < x < 1; \qquad \frac{dU}{dx}(0, s) = s\gamma U(0, s), \quad U(1, s) = \frac1s .
> $$
>
> $U = C\big(\cosh(\sqrt s\,x) + \sqrt s\,\gamma\sinh(\sqrt s\,x)\big)$ satisfies the equation and the condition at $x = 0$ ($U'(0) = C\gamma s = s\gamma U(0)$). Then $U(1) = 1/s$ fixes $C$:
>
> $$
> U(x, s) = \frac{\cosh(\sqrt s\,x) + \sqrt s\,\gamma\sinh(\sqrt s\,x)}{s\big(\cosh(\sqrt s) + \sqrt s\,\gamma\sinh(\sqrt s)\big)} = \frac{q(s)}{p(s)} .
> $$
>
> By Lemma §54.1 the singular points are $r_0 = 0$ and $r_k = -\eta_k^2$.
>
> **Part a ($r_0 = 0$).** The limit of $sU(x, s)$ as $s \to 0$ is $(1 + 0)/(1 + 0) = 1$, so this root contributes $1\cdot e^{0t} = 1$, the steady state.
>
> **Part b ($r_k = -\eta_k^2$).** First,
>
> $$
> p'(s) = \cosh\big(\sqrt s\big) + \sqrt s\,\gamma\sinh\big(\sqrt s\big) + \tfrac12\sqrt s(1 + \gamma)\sinh\big(\sqrt s\big) + \tfrac12\gamma s\cosh\big(\sqrt s\big) .
> $$
>
> At $r_k$ the first two terms cancel, since $\cosh(\sqrt{r_k}) + \sqrt{r_k}\,\gamma\sinh(\sqrt{r_k}) = 0$. With $\sqrt{r_k} = i\eta_k$, $\sinh(i\eta) = i\sin\eta$ and $\cosh(i\eta) = \cos\eta$, the rest is $-\frac12\eta_k(1 + \gamma)\sin\eta_k - \frac12\gamma\eta_k^2\cos\eta_k$. Using $\sin\eta_k = \cos\eta_k/(\eta_k\gamma)$ from the root condition,
>
> $$
> p'(r_k) = -\frac{1}{2\gamma}\big(1 + \gamma + \eta_k^2\gamma^2\big)\cos(\eta_k) .
> $$
>
> Also $q(r_k) = \cosh(i\eta_kx) + i\eta_k\gamma\sinh(i\eta_kx) = \cos(\eta_kx) - \eta_k\gamma\sin(\eta_kx)$. Hence the contribution of $r_k$ to $u(x, t)$ is
>
> $$
> \frac{q(r_k)}{p'(r_k)}\exp(r_kt) = -2\gamma\,\frac{\cos(\eta_kx) - \eta_k\gamma\sin(\eta_kx)}{\big(1 + \gamma + \eta_k^2\gamma^2\big)\cos(\eta_k)}\exp\big(-\eta_k^2t\big) .
> $$
>
> **Part c (assembly; left to the reader by Powers).**
>
> $$
> u(x, t) = 1 - 2\gamma\sum_{k=1}^\infty \frac{\cos(\eta_kx) - \eta_k\gamma\sin(\eta_kx)}{\big(1 + \gamma + \eta_k^2\gamma^2\big)\cos(\eta_k)}\exp\big(-\eta_k^2t\big) .
> $$
>
> **Check.**
> - *Equation.* Each term has the form $X_k(x)e^{-\eta_k^2t}$ with $X_k'' = -\eta_k^2X_k$, so it solves the heat equation; for $t > 0$ the factors $e^{-\eta_k^2t}$, with $\eta_k > (k - 1)\pi$, make the series and its derivatives converge uniformly.
> - *At $x = 1$.* $X_k(1) = \cos\eta_k - \eta_k\gamma\sin\eta_k = 0$ by the root condition, so $u(1, t) = 1$.
> - *At $x = 0$.* Term by term, with $D_k = (1 + \gamma + \eta_k^2\gamma^2)\cos\eta_k$: $u_x(0, t) = -2\gamma\sum(-\eta_k^2\gamma)e^{-\eta_k^2t}/D_k$ and $\gamma u_t(0, t) = -2\gamma^2\sum(-\eta_k^2)e^{-\eta_k^2t}/D_k$, which agree.
> - *At $t = 0$.* For $\gamma = 1$ the roots are $\eta_1 \approx 0.8603$, $\eta_2 \approx 3.4256$, $\eta_3 \approx 6.4373$, and the partial sums of $u(x, 0)$ tend to $0$, slowly, as for a Fourier series whose sum jumps at an endpoint (with $4000$ terms they are below $2\times10^{-4}$ at $x = 0, \frac14, \frac12, \frac34$).
>
> For $\gamma = 1$ the slowest mode decays like $e^{-0.74t}$. At $t = 1$ the fluid has reached $u(0, 1) \approx 0.47$.
>
> *Powers: 6.4, Example 1*

^ex-54-1

> [!remark] Remark: Eigenfunctions That Are Not Orthogonal
> Powers notes that separation of variables would find difficulties here, because the eigenfunctions are not orthogonal. With $u = X(x)T(t)$, $T' = -\lambda T$, the boundary condition at $x = 0$ becomes $X'(0) = -\lambda\gamma X(0)$. The eigenvalue appears in the boundary condition, so this is not a regular Sturm–Liouville problem ([[§23 Sturm–Liouville Problems|§23]]). The eigenfunctions $X_k = \cos(\eta_kx) - \eta_k\gamma\sin(\eta_kx)$, $\lambda_k = \eta_k^2$, are not orthogonal on $0 < x < 1$, and the usual coefficient formula fails. The transform gives the coefficients directly.
>
> Orthogonality is in fact only hidden. Integrating $X_j''X_k - X_jX_k''$ over $(0, 1)$ and using $X(1) = 0$ and the condition at $0$ gives
>
> $$
> (\lambda_k - \lambda_j)\Big[\int_0^1 X_jX_k\,dx + \gamma X_j(0)X_k(0)\Big] = 0 .
> $$
>
> So the $X_k$ are orthogonal for the inner product $\int_0^1 fg\,dx + \gamma f(0)g(0)$. The extra term is the fluid: a heat capacity $\gamma$ concentrated at the point $x = 0$.
>
> **Limiting cases.** As $\gamma \to 0$ the container disappears, the condition becomes $u_x(0, t) = 0$ (insulated end), and $\eta_k \to (2k - 1)\pi/2$, the eigenvalues of [[§21 Example꞉ Different Boundary Conditions|§21]]. As $\gamma \to \infty$ the fluid cannot change temperature quickly. Then $\eta_k \to (k - 1)\pi$ for $k \ge 2$, as for a rod with both ends fixed, while $\eta_1 \approx 1/\sqrt\gamma \to 0$: a very slow mode in which rod and fluid together creep up to $u = 1$.

^rem-54-1

## The Persistent Part of a Solution

Sometimes only part of the solution is of interest. For heat conduction in a semi-infinite solid with a time-varying surface temperature, one may want only the part that persists after a long time.

> [!definition] Definition §54.1: Persistent Part
> The **persistent part** of a solution $u(x, t)$ is the part that remains after a long time: in the extended Heaviside formula, the sum of the contributions $A_ne^{r_nt}$ from singular points $r_n$ with *nonnegative* real part. A singular point with *negative* real part contributes a decaying exponential, a **transient**. The persistent part may or may not be a steady state: it may oscillate.
>
> *Powers: 6.4 (text)*

^def-54-1

> [!example] Example §54.2: Temperature Waves in a Semi-Infinite Solid
> Any initial condition that is bounded in $x$ gives rise only to transient temperatures, so take a zero initial temperature:
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial u}{\partial t}, \quad 0 < x < \infty,\ 0 < t; \qquad u(0, t) = f(t), \quad 0 < t; \qquad u(x, 0) = 0, \quad 0 < x < \infty .
> $$
>
> **Transform and solve.** The transformed equation and its general solution are
>
> $$
> \frac{d^2U}{dx^2} = sU, \quad 0 < x; \qquad U(0, s) = F(s); \qquad U(x, s) = A\exp\big(-\sqrt s\,x\big) + B\exp\big(\sqrt s\,x\big) .
> $$
>
> Assume that $u(x, t)$ is bounded as $x \to \infty$, and that $\sqrt s$ is the square root with nonnegative real part. Then $B = 0$ and $A = F(s)$:
>
> $$
> U(x, s) = F(s)\exp\big(-\sqrt s\,x\big) .
> $$
>
> **A particular boundary temperature.** Take
>
> $$
> f(t) = 1 - e^{-\beta t} + \alpha\sin(\omega t), \qquad F(s) = \frac1s - \frac{1}{s + \beta} + \frac{\alpha\omega}{s^2 + \omega^2} ,
> $$
>
> with $\beta > 0$. $U = F(s)\exp(-\sqrt s\,x)$ becomes infinite at $s = 0, \pm i\omega, -\beta$. The last is discarded, being negative. So the persistent part is
>
> $$
> A_0e^{0t} + A_1e^{i\omega t} + A_2e^{-i\omega t} ,
> $$
>
> with
>
> $$
> A_0 = \lim_{s\to0}\big[sF(s)\exp(-\sqrt s\,x)\big] = 1, \qquad
> A_1 = \lim_{s\to i\omega}\big[(s - i\omega)F(s)\exp(-\sqrt s\,x)\big] = \frac{\alpha}{2i}\exp\big(-\sqrt{i\omega}\,x\big),
> $$
>
> $$
> A_2 = \lim_{s\to-i\omega}\big[(s + i\omega)F(s)\exp(-\sqrt s\,x)\big] = -\frac{\alpha}{2i}\exp\big(-\sqrt{-i\omega}\,x\big) ,
> $$
>
> since $(s - i\omega)\frac{\alpha\omega}{s^2 + \omega^2} = \frac{\alpha\omega}{s + i\omega} \to \frac{\alpha}{2i}$. The roots of $\pm i$ with positive real part are $\sqrt i = \frac{1}{\sqrt2}(1 + i)$ and $\sqrt{-i} = \frac{1}{\sqrt2}(1 - i)$. So the persistent part is
>
> $$
> 1 + \frac{\alpha}{2i}\exp\Big[i\omega t - \sqrt{\tfrac\omega2}(1 + i)x\Big] - \frac{\alpha}{2i}\exp\Big[-i\omega t - \sqrt{\tfrac\omega2}(1 - i)x\Big] = 1 + \alpha\exp\Big(-\sqrt{\tfrac\omega2}\,x\Big)\sin\Big(\omega t - \sqrt{\tfrac\omega2}\,x\Big) .
> $$
>
> **Check.** With $\kappa = \sqrt{\omega/2}$ and $v = e^{-\kappa x}\sin(\omega t - \kappa x)$: $v_t = \omega e^{-\kappa x}\cos(\omega t - \kappa x)$, and differentiating twice in $x$, $v_{xx} = 2\kappa^2e^{-\kappa x}\cos(\omega t - \kappa x) = v_t$. So the persistent part solves the heat equation. At $x = 0$ it equals $1 + \alpha\sin(\omega t)$, the boundary temperature without its transient $-e^{-\beta t}$.
>
> **Meaning.** The surface oscillation travels into the solid as a damped wave. Its amplitude decreases by a factor $e$ every $\sqrt{2/\omega}$ units of depth, and its phase lags by $\sqrt{\omega/2}\,x$, so the wave moves inward with speed $\omega/\kappa = \sqrt{2\omega}$. With a diffusivity $k$ restored ($u_t = ku_{xx}$), the depth scale is $\sqrt{2k/\omega}$. Slow oscillations penetrate deeper: the annual temperature wave in the ground reaches $\sqrt{365} \approx 19$ times as deep as the daily one. At a depth of $\pi\sqrt{2/\omega}$ the temperature is half a period out of phase with the surface.
>
> *Powers: 6.4, Example 2*

^ex-54-2

![[m341-54-1.svg]]
*The persistent part $u = 1 + \alpha e^{-\sqrt{\omega/2}\,x}\sin(\omega t - \sqrt{\omega/2}\,x)$ of Example §54.2, for $\alpha = \frac12$ and $\omega = 2\pi$, at four instants of one period. Each profile is a wave squeezed into the envelope $1 \pm \alpha e^{-\sqrt{\omega/2}\,x}$ (dashed): the surface oscillation dies out within a few depth units $\sqrt{2/\omega} \approx 0.56$, and deeper points reach their maxima later.*

> [!remark]- Remark: The Branch Point at the Origin
> Unlike the transforms of [[§53★ Partial Differential Equations|§53★]], $U = F(s)e^{-\sqrt s\,x}$ is not an even function of $\sqrt s$, and $s = 0$ is a branch point, not a pole. $A_0 = \lim_{s\to0}sU = 1$ still gives the correct long-time value, but the rest of the solution need not decay exponentially. For $f(t) = 1$, the solution is $u = \operatorname{erfc}\big(x/(2\sqrt t)\big)$ ([[§28★ The Error Function|§28★]]). It approaches the persistent value $1$ only like $1 - x/\sqrt{\pi t}$. The persistent part computed above is correct, but "transient" here can mean a slow algebraic decay. The points $\pm i\omega$ are ordinary simple poles, where the residue computation is valid.

^rem-54-2

## Resonance: A Double Pole

> [!theorem] Proposition §54.2: Heaviside's Formula at a Double Root
> Suppose that near $s = r$ the transform has the form
>
> $$
> U(s) = \frac{A(s - r) + B}{(s - r)^2} + V(s) = \frac{A}{s - r} + \frac{B}{(s - r)^2} + V(s) ,
> $$
>
> with $V$ bounded near $r$. Then
>
> $$
> B = \lim_{s\to r}\big[(s - r)^2U(s)\big], \qquad A = \lim_{s\to r}\Big\{(s - r)\Big[U(s) - \frac{B}{(s - r)^2}\Big]\Big\} ,
> $$
>
> and the contribution of $r$ to the inverse transform is
>
> $$
> Ae^{rt} + Bte^{rt} .
> $$
>
> *Powers: 6.4, Example 3 (text)*

^prop-54-2

> [!proof]+ Proof
> **Coefficients.** Multiply by $(s - r)^2$: $(s - r)^2U = B + A(s - r) + (s - r)^2V(s) \to B$ as $s \to r$, since $V$ is bounded. Then $(s - r)\big[U - B/(s - r)^2\big] = A + (s - r)V(s) \to A$.
>
> **Inverse transform.** $\mathcal{L}(t) = 1/s^2$ ([[§51★ Definition and Elementary Properties#^ex-51-3|Example §51.3]]), so by the shifting theorem ([[§51★ Definition and Elementary Properties#^thm-51-3|Theorem §51.3]]) with $b = r$, also for complex $r$, $\mathcal{L}(te^{rt}) = 1/(s - r)^2$; and $\mathcal{L}(e^{rt}) = 1/(s - r)$. By linearity ([[§52★ Partial Fractions and Convolutions#^thm-52-1|Theorem §52.1]]) the two singular terms invert to $Ae^{rt} + Bte^{rt}$.

^pf-54-2

*Uses:* [[§51★ Definition and Elementary Properties#^ex-51-3|Ex. §51.3]], [[§51★ Definition and Elementary Properties#^thm-51-3|§51.3]], [[§52★ Partial Fractions and Convolutions#^thm-52-1|§52.1]]

*When $(s - r)^2U$ is differentiable at $r$, the second limit is also $A = \frac{d}{ds}\big[(s - r)^2U(s)\big]_{s=r}$. This is the form behind Powers' remark that $A$ "may be computed by L'Hôpital's rule".*

> [!remark]- Connections
> - For rational transforms with repeated roots, the same terms $t^ne^{rt}$ come from partial fractions and table entry 11, $\mathcal{L}(t^ne^{at}) = n!/(s - a)^{n+1}$: [[§22 Solution of Initial Value Problems#^thm-22-6|331 Thm. §22.6]], [[§22 Solution of Initial Value Problems#^rem-22-4|331 §22]] (Method — Inverting a Rational Transform). The ODE version of resonance, $mu'' + ku = F_0\cos(\omega_0t)$ with its growing term $\frac{F_0}{2m\omega_0}t\sin(\omega_0t)$, is [[§20 Forced Periodic Vibrations#^prop-20-4|331 Prop. §20.4]].

> [!example] Example §54.3: A Wire Driven at a Natural Frequency
> A steel wire exposed to a sinusoidal magnetic field is displaced according to
>
> $$
> \frac{\partial^2u}{\partial x^2} = \frac{\partial^2u}{\partial t^2} - \sin(\omega t), \quad 0 < x < 1,\ 0 < t; \qquad u(0, t) = 0,\quad u(1, t) = 0; \qquad u(x, 0) = 0,\quad \frac{\partial u}{\partial t}(x, 0) = 0 .
> $$
>
> The nonhomogeneous term is the force due to the field.
>
> **Transform and solve.**
>
> $$
> \frac{d^2U}{dx^2} = s^2U - \frac{\omega}{s^2 + \omega^2}, \quad 0 < x < 1; \qquad U(0, s) = 0, \quad U(1, s) = 0 .
> $$
>
> The constant $\omega/(s^2(s^2 + \omega^2))$ is a particular solution. Subtracting the multiple of $\cosh(s(\frac12 - x))$, which is symmetric about $x = \frac12$, that cancels it at both ends gives
>
> $$
> U(x, s) = \frac{\omega}{s^2(s^2 + \omega^2)}\cdot\frac{\cosh(\frac12 s) - \cosh\big(s(\frac12 - x)\big)}{\cosh(\frac12 s)} .
> $$
>
> **Inversion in general.** One way is by convolution, [[§52★ Partial Fractions and Convolutions#^thm-52-3|Theorem §52.3]]. Since $\omega/(s^2 + \omega^2) = \mathcal{L}(\sin\omega t)$,
>
> $$
> u(x, t) = \int_0^t \sin\big(\omega(t - t')\big)v(x, t')\,dt', \qquad v(x, t) = \mathcal{L}^{-1}\Big(\frac{\cosh(\frac12 s) - \cosh\big(s(\frac12 - x)\big)}{s^2\cosh(\frac12 s)}\Big)
> $$
>
> (Powers leaves the details as an exercise). The Heaviside formula is routine when all singular points are simple. They are $s = \pm i\omega$ and the zeros $s = \pm(2n - 1)i\pi$ of $\cosh(\frac12 s)$ (Lemma §53.2(b)). The point $s = 0$ is removable, because $\cosh(\frac12 s) - \cosh(s(\frac12 - x)) \approx \frac{s^2}{2}x(1 - x)$ cancels the $s^2$. The interesting case is $\cosh(i\omega/2) = 0$, that is, $\omega = (2n - 1)\pi$, one of the natural frequencies of the wire.
>
> **The resonant case $\omega = \pi$.** Now
>
> $$
> U(x, s) = \frac{\pi}{s^2(s^2 + \pi^2)}\cdot\frac{\cosh(\frac12 s) - \cosh\big(s(\frac12 - x)\big)}{\cosh(\frac12 s)} ,
> $$
>
> and $U$ is undefined at $s = 0$ (removable), $s = \pm i\pi$ and $s = \pm(2n - 1)i\pi$, $n = 2, 3, \ldots$ At $\pm i\pi$ both $s^2 + \pi^2$ and $\cosh(\frac12 s)$ vanish, so these are double poles. Instead of $\frac{A_{-1}}{s + i\pi} + \frac{A_1}{s - i\pi}$, the decomposition must contain
>
> $$
> \frac{A_{-1}(s + i\pi) + B_{-1}}{(s + i\pi)^2} + \frac{A_1(s - i\pi) + B_1}{(s - i\pi)^2} ,
> $$
>
> contributing $A_{-1}e^{-i\pi t} + B_{-1}te^{-i\pi t} + A_1e^{i\pi t} + B_1te^{i\pi t}$ (Proposition §54.2).
>
> **The coefficient $B_1$.** Write $(s - i\pi)^2U$ as a product in which each factor has a finite limit; $(s - i\pi)/\cosh(\frac12 s) \to 1/(\frac12\sinh(\frac12 i\pi)) = 1/(\frac12 i)$ by L'Hôpital's rule:
>
> $$
> B_1 = \lim_{s\to i\pi}\Big\{\frac{\pi}{s^2(s + i\pi)}\cdot\frac{\cosh(\frac12 s) - \cosh\big(s(\frac12 - x)\big)}{\cosh(\frac12 s)/(s - i\pi)}\Big\}
> = \frac{\pi}{-\pi^2(2i\pi)}\cdot\frac{\cosh(\frac12 i\pi) - \cosh\big(i\pi(\frac12 - x)\big)}{\frac12\sinh(\frac12 i\pi)} .
> $$
>
> With $\cosh(\frac12 i\pi) = \cos\frac\pi2 = 0$, $\cosh(i\pi(\frac12 - x)) = \cos(\pi(\frac12 - x)) = \sin(\pi x)$ and $\frac12\sinh(\frac12 i\pi) = \frac i2$:
>
> $$
> B_1 = \frac{1}{-2i\pi^2}\cdot\frac{-\sin(\pi x)}{i/2} = -\frac{1}{\pi^2}\cos\Big(\pi\Big(\frac12 - x\Big)\Big) = -\frac{1}{\pi^2}\sin(\pi x) .
> $$
>
> **Resonance.** $U$ is real for real $s$, so its coefficients at conjugate points are conjugate: $B_{-1} = \bar B_1 = B_1$. Therefore $u(x, t)$ contains the term
>
> $$
> B_1te^{i\pi t} + B_{-1}te^{-i\pi t} = -\frac{2t}{\pi^2}\sin(\pi x)\cos(\pi t) ,
> $$
>
> whose amplitude increases with time. This is the expected resonance phenomenon.
>
> **Completing the solution.** The coefficient $A_1$ is more complicated. Expanding $(s - i\pi)^2U$ to first order about $i\pi$ (by L'Hôpital's rule, or with a computer algebra system) gives
>
> $$
> A_1 = \frac{i}{2\pi^3}\Big[\pi\big(1 - (1 - 2x)\cos(\pi x)\big) - 5\sin(\pi x)\Big], \qquad A_{-1} = \bar A_1 ,
> $$
>
> so $A_1e^{i\pi t} + A_{-1}e^{-i\pi t} = g(x)\sin(\pi t)$ with
>
> $$
> g(x) = \frac{(1 - 2x)\cos(\pi x) - 1}{\pi^2} + \frac{5\sin(\pi x)}{\pi^3} .
> $$
>
> At the simple poles $\pm i\mu_n$, $\mu_n = (2n - 1)\pi$, $n \ge 2$, Heaviside's formula with $\cos(\frac12\mu_n) = 0$ and $\cos(\mu_n(\frac12 - x)) = \sin(\frac12\mu_n)\sin(\mu_nx)$ gives $q/p' = 2\pi i\sin(\mu_nx)/(\mu_n^2(\mu_n^2 - \pi^2))$, and the pair contributes $-4\pi\sin(\mu_nx)\sin(\mu_nt)/(\mu_n^2(\mu_n^2 - \pi^2))$. Altogether,
>
> $$
> u(x, t) = -\frac{2t}{\pi^2}\sin(\pi x)\cos(\pi t) + g(x)\sin(\pi t) - 4\pi\sum_{n=2}^\infty \frac{\sin(\mu_nx)\sin(\mu_nt)}{\mu_n^2\big(\mu_n^2 - \pi^2\big)} .
> $$
>
> **Check.**
> - *Initial position and boundary values.* $u(x, 0) = 0$ term by term; $g(0) = g(1) = 0$, so $u(0, t) = u(1, t) = 0$.
> - *Equation.* The series solves the homogeneous wave equation. For the first two terms, with $h = (1 - 2x)\cos(\pi x)$ one finds $h'' + \pi^2h = 4\pi\sin(\pi x)$, so $g'' + \pi^2g = \frac4\pi\sin(\pi x) - 1$. Substituting, the first two terms give exactly $u_{tt} - u_{xx} = \sin(\pi t)$.
> - *Initial velocity.* $u_t(x, 0) = 0$ says that the series $4\pi\sum_{n\ge2}\sin(\mu_nx)/(\mu_n(\mu_n^2 - \pi^2))$ is the sine series of $\pi g(x) - \frac{2}{\pi^2}\sin(\pi x)$. For instance, the $\sin(\pi x)$ coefficient of the latter is $2\int_0^1\big(\pi g - \frac{2}{\pi^2}\sin\pi x\big)\sin(\pi x)\,dx = 2\big(\pi(-\frac{3}{2\pi^3} + \frac{5}{2\pi^3}) - \frac{1}{\pi^2}\big) = 0$. The coefficient of $5$ in $g$ is exactly what makes this vanish.
>
> **Why only odd frequencies resonate.** In eigenfunction form the forcing is $\sin(\omega t)\cdot 1$ with $1 = \sum_{n\ \text{odd}}\frac{4}{n\pi}\sin(n\pi x)$ on $(0, 1)$. The uniform force has no component along the even modes $\sin(2m\pi x)$, which are antisymmetric about $x = \frac12$. So driving at $\omega = 2m\pi$ produces no resonance: there $\cosh(i\omega/2) = \cos(m\pi) \ne 0$ and the poles stay simple.
>
> *Powers: 6.4, Example 3*

^ex-54-3

![[m341-54-2.svg]]
*Midpoint displacement $u(\frac12, t)$ of the wire of Example §54.3, driven at its fundamental frequency $\omega = \pi$, from the complete solution (300 terms). The oscillation grows between the lines $\pm 2t/\pi^2$ (dashed), the envelope of the resonance term $-\frac{2t}{\pi^2}\sin(\pi x)\cos(\pi t)$ that comes from the double poles at $s = \pm i\pi$; the bounded terms only distort the first few cycles.*
