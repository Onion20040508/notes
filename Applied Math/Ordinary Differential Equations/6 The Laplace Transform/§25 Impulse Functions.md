---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 25
bdp: "6.5"
aliases: ["BDP 6.5"]
tags: [ordinary-differential-equations, math331]
---
← [[§24 Differential Equations with Discontinuous Forcing Functions]] · ↑ [[· 6 The Laplace Transform]] · [[§26★ The Convolution Integral]] →

*Boyce–DiPrima, Section 6.5 · MATH 331 Written HW 5 (Problems 5–7); Final (Fall 2021), Q5.*

A hammer blow or a voltage spike is a large force acting for a very short time. What matters is its total effect, the impulse $\int g\,dt$, not its exact shape. Idealizing such a force as acting at a single instant leads to the Dirac delta $\delta(t - t_0)$: zero away from $t_0$, with total integral $1$. No ordinary function behaves like this, so $\delta$ is defined through limits of narrow pulses $d_\tau$ of area $1$. Its Laplace transform is simply $e^{-st_0}$, so impulsive forcing is as easy to handle with the Laplace transform as step forcing, and the solution is again continuous while its derivative jumps.

## Impulses and the Delta Function

Consider equations

$$
ay'' + by' + cy = g(t), \qquad (1)
$$

where $g(t)$ is large during a short interval $t_0 - \tau < t < t_0 + \tau$, $\tau > 0$, and zero otherwise.

> [!definition] Definition §25.1: Impulse
> If $g(t) = 0$ outside the interval $(t_0 - \tau, t_0 + \tau)$, the **impulse** of $g$ is
>
> $$
> I(\tau) = \int_{t_0 - \tau}^{t_0 + \tau} g(t)\,dt = \int_{-\infty}^{\infty} g(t)\,dt . \qquad (2), (3)
> $$
>
> It measures the strength of the forcing. If $g$ is a force, $I(\tau)$ is the total impulse of the force over the interval (the change in momentum it produces). If $y$ is the current in a circuit and $g$ is the time derivative of the voltage, $I(\tau)$ is the total voltage impressed on the circuit during the interval.
>
> *BDP: 6.5 (text), Equations (2) and (3)*

^def-25-1

> [!definition] Definition §25.2: The Unit Pulses $d_\tau$
> For $\tau > 0$ let
>
> $$
> d_\tau(t) = \begin{cases} \dfrac{1}{2\tau}, & -\tau < t < \tau, \\[4pt] 0, & t \le -\tau \text{ or } t \ge \tau. \end{cases} \qquad (4)
> $$
>
> This pulse has height $\frac{1}{2\tau}$ on an interval of length $2\tau$, so its impulse is $I(\tau) = 1$ for every $\tau > 0$. As $\tau \to 0^+$ the pulses get narrower and taller, and
>
> $$
> \lim_{\tau \to 0^+} d_\tau(t) = 0 \quad (t \ne 0), \qquad \lim_{\tau \to 0^+} I(\tau) = 1 . \qquad (5), (6)
> $$
>
> *BDP: 6.5 (text), Equations (4)–(6)*

^def-25-2

> [!definition] Definition §25.3: The Dirac Delta Function
> The **unit impulse function** $\delta$ is the idealized forcing that imparts an impulse of magnitude one at $t = 0$ and is zero for all other $t$. It is defined by the properties (5) and (6) of the limit of $d_\tau$:
>
> $$
> \delta(t) = 0, \quad t \ne 0; \qquad \int_{-\infty}^{\infty} \delta(t)\,dt = 1 . \qquad (7), (8)
> $$
>
> A unit impulse at $t = t_0$ is $\delta(t - t_0)$:
>
> $$
> \delta(t - t_0) = 0, \quad t \ne t_0; \qquad \int_{-\infty}^{\infty} \delta(t - t_0)\,dt = 1 . \qquad (9), (10)
> $$
>
> No ordinary function satisfies both (7) and (8): a function that vanishes except at one point has integral $0$. $\delta$ is an example of a **generalized function**, usually called the **Dirac delta function**. All statements about it are understood through the pulses $d_\tau$, as in [[§25 Impulse Functions#^def-25-4|Definition §25.4]].
>
> *BDP: 6.5 (text), Equations (7)–(10)*

^def-25-3

> [!remark]- Connections
> - The rigorous object behind (9)–(10) is a measure, not a function: the Dirac measure $\mu_{t_0}$ ([[§11 Borel Sets and Measure Spaces#^ex-11-2|551 Ex. §11.2]]), with $\mu_{t_0}(E) = 1$ if $t_0 \in E$ and $0$ otherwise. Integrating against it gives $\int f\,d\mu_{t_0} = f(t_0)$, which is [[§25 Impulse Functions#^thm-25-3|Theorem §25.3]], and $\mathcal{L}\{\delta(t - t_0)\} = \int e^{-st}\,d\mu_{t_0} = e^{-st_0}$, which is [[§25 Impulse Functions#^thm-25-2|Theorem §25.2]].
> - That no function, even in $L^2$, can do the job of $\delta$: point evaluation $\varphi \mapsto \varphi(x_0)$ is not given by an inner product with any $\psi \in L^2(\mathbb{R})$, [[§32 Position Eigenstates and Continuous Resolutions#^prop-32-4|556 Prop. §32.4]]; the "wavefunction" $\delta(x - x_0)$ of a position eigenstate is the same idealization.

> [!definition] Definition §25.4: Transform and Integrals of δ
> For $t_0 > 0$, the Laplace transform of $\delta(t - t_0)$ is defined as the limit of the transforms of the pulses:
>
> $$
> \mathcal{L}\{\delta(t - t_0)\} = \lim_{\tau \to 0^+} \mathcal{L}\{d_\tau(t - t_0)\} . \qquad (11)
> $$
>
> In the same way, for a continuous function $f$,
>
> $$
> \int_{-\infty}^{\infty} \delta(t - t_0)\,f(t)\,dt = \lim_{\tau \to 0^+} \int_{-\infty}^{\infty} d_\tau(t - t_0)\,f(t)\,dt . \qquad (15)
> $$
>
> (The Dirac delta does not satisfy the hypotheses of the existence theorem for Laplace transforms, [[§21 Definition of the Laplace Transform#^thm-21-2|Theorem §21.2]] (BDP Theorem 6.1.2), so its transform has to be defined.)
>
> *BDP: 6.5 (text), Equations (11) and (15)*

^def-25-4

## The Laplace Transform of δ

> [!theorem] Theorem §25.1: Transform of a Shifted Pulse
> If $0 < \tau < t_0$, then, for $s \ne 0$,
>
> $$
> \mathcal{L}\{d_\tau(t - t_0)\} = \frac{\sinh(s\tau)}{s\tau}\,e^{-st_0} . \qquad (12)
> $$
>
> *BDP: 6.5 (text), Equation (12)*

^thm-25-1

> [!proof]+ Proof
> Since $\tau < t_0$, the interval $(t_0 - \tau, t_0 + \tau)$ where $d_\tau(t - t_0)$ is nonzero lies in $t > 0$. (This must eventually be the case as $\tau \to 0^+$.) There $d_\tau(t - t_0) = \frac{1}{2\tau}$, so
>
> $$
> \mathcal{L}\{d_\tau(t - t_0)\} = \int_{t_0 - \tau}^{t_0 + \tau} e^{-st}\,\frac{1}{2\tau}\,dt = -\frac{1}{2s\tau}\,e^{-st}\Big|_{t = t_0 - \tau}^{t = t_0 + \tau} = \frac{1}{2s\tau}\,e^{-st_0}\big(e^{s\tau} - e^{-s\tau}\big) = \frac{\sinh(s\tau)}{s\tau}\,e^{-st_0},
> $$
>
> using $\sinh x = \frac12(e^x - e^{-x})$. (For $s = 0$ the integral is just the impulse $1$ of the pulse.)

^pf-25-1

*Uses:* [[§25 Impulse Functions#^def-25-2|Def. §25.2]], [[§21 Definition of the Laplace Transform#^def-21-4|Def. §21.4]]

> [!theorem] Theorem §25.2: Transform of the Delta Function
> For $t_0 > 0$,
>
> $$
> \mathcal{L}\{\delta(t - t_0)\} = e^{-st_0}, \qquad (13)
> $$
>
> and, extending to $t_0 = 0$ by letting $t_0 \to 0^+$,
>
> $$
> \mathcal{L}\{\delta(t)\} = \lim_{t_0 \to 0^+} e^{-st_0} = 1 . \qquad (14)
> $$
>
> *BDP: 6.5 (text), Equations (13) and (14)*

^thm-25-2

> [!proof]+ Proof
> By [[§25 Impulse Functions#^def-25-4|Definition §25.4]] and [[§25 Impulse Functions#^thm-25-1|Theorem §25.1]], $\mathcal{L}\{\delta(t - t_0)\} = e^{-st_0}\lim_{\tau \to 0^+} \dfrac{\sinh(s\tau)}{s\tau}$. The quotient is of the form $\frac00$ as $\tau \to 0^+$; by l'Hôpital's rule (differentiating in $\tau$, with $s$ fixed),
>
> $$
> \lim_{\tau \to 0^+} \frac{\sinh(s\tau)}{s\tau} = \lim_{\tau \to 0^+} \frac{s\cosh(s\tau)}{s} = \cosh 0 = 1 .
> $$
>
> This gives (13) for $s \ne 0$; for $s = 0$ both sides of (13) equal $1$, since each pulse has impulse $1$. Equation (14) is BDP's definition of $\mathcal{L}\{\delta(t)\}$ as the limit of (13) as $t_0 \to 0^+$.

^pf-25-2

*Uses:* [[§25 Impulse Functions#^def-25-4|Def. §25.4]], [[§25 Impulse Functions#^thm-25-1|§25.1]], [[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-2|Calc Thm. §28.2]] (l'Hôpital's rule)

The formulas agree with the shift rule of [[§23 Step Functions#^thm-23-2|Theorem §23.2]]: $\delta(t - t_0)$ is the translation of $\delta(t)$ by $t_0$, and $\mathcal{L}\{\delta(t - t_0)\} = e^{-st_0}\mathcal{L}\{\delta(t)\} = e^{-st_0}$.

> [!theorem] Theorem §25.3: The Sifting Property
> If $f$ is continuous, then
>
> $$
> \int_{-\infty}^{\infty} \delta(t - t_0)\,f(t)\,dt = f(t_0) . \qquad (16)
> $$
>
> The same holds for an integral over any interval $[\alpha, \beta]$ that contains $t_0$ in its interior, and here it suffices that $f$ be continuous on $[\alpha, \beta]$; the integral is $0$ over an interval that does not contain $t_0$.
>
> *BDP: 6.5 (text), Equation (16)*

^thm-25-3

> [!proof]+ Proof
> By (4), $d_\tau(t - t_0) = \frac{1}{2\tau}$ on $(t_0 - \tau, t_0 + \tau)$ and $0$ elsewhere, so
>
> $$
> \int_{-\infty}^{\infty} d_\tau(t - t_0)\,f(t)\,dt = \frac{1}{2\tau}\int_{t_0 - \tau}^{t_0 + \tau} f(t)\,dt = \frac{1}{2\tau}\cdot 2\tau\cdot f(t^*) = f(t^*)
> $$
>
> for some $t^*$ with $t_0 - \tau \le t^* \le t_0 + \tau$, by the mean value theorem for integrals applied to the continuous $f$ on $[t_0 - \tau, t_0 + \tau]$. As $\tau \to 0^+$, $t^* \to t_0$, so $f(t^*) \to f(t_0)$ by continuity of $f$ at $t_0$. By (15) the left side of (16) is this limit, $f(t_0)$.
>
> For an interval $[\alpha, \beta]$ with $\alpha < t_0 < \beta$, once $\tau$ is small enough that $(t_0 - \tau, t_0 + \tau) \subseteq (\alpha, \beta)$, the integral of $d_\tau(t - t_0)f(t)$ over $[\alpha, \beta]$ is again $\frac{1}{2\tau}\int_{t_0 - \tau}^{t_0 + \tau} f(t)\,dt$. The argument above uses $f$ only on $[t_0 - \tau, t_0 + \tau]$, so the limit is again $f(t_0)$. If $t_0 \notin [\alpha, \beta]$, then for small $\tau$ the pulse vanishes on $[\alpha, \beta]$ and the integral is $0$.

^pf-25-3

*Uses:* [[§25 Impulse Functions#^def-25-2|Def. §25.2]], [[§25 Impulse Functions#^def-25-4|Def. §25.4]], [[§43 Average Value of a Function#^thm-43-1|Calc Thm. §43.1]] (mean value theorem for integrals)

> [!remark]- Connections
> - The mean value theorem for integrals used in the proof: [[§43 Average Value of a Function#^thm-43-1|Calc Thm. §43.1]]; rigorous version [[§33 Properties of the Riemann Integral#^thm-33-9|451 Thm. §33.9]].

> [!example] Example §25.1: Integrals Against δ
> Evaluate:
>
> **(a)** $\displaystyle\int_1^7 \delta(t + 3)\,dt$. The impulse is at $t = -3$, outside $[1, 7]$, so the integral is $0$.
>
> **(b)** $\displaystyle\int_1^7 \delta(t - 6)\,dt$. The impulse is at $t = 6 \in (1, 7)$; by [[§25 Impulse Functions#^thm-25-3|Theorem §25.3]] with $f = 1$, the integral is $1$.
>
> **(c)** $\displaystyle\int_1^7 (2t^4 - 5t^3 - 7t^2 - 1)\,\delta(t - 8)\,dt$. The impulse is at $t = 8$, outside $[1, 7]$, so the integral is $0$, whatever the polynomial.
>
> **(d)** $\displaystyle\int_1^7 \ln(t^2)\,\delta(t - e)\,dt$. Here $e \approx 2.718 \in (1, 7)$ and $\ln(t^2)$ is continuous there, so the integral is $\ln(e^2) = 2$.
>
> *Source: 331 Written HW 5, Problem 5*

^ex-25-1

## Impulsive Forcing

With [[§25 Impulse Functions#^thm-25-2|Theorem §25.2]], an impulse in the forcing term is handled exactly like a step ([[§24 Differential Equations with Discontinuous Forcing Functions#^rem-24-1|Method of §24]]): $k\delta(t - c)$ contributes $ke^{-cs}$ to the transformed equation.

> [!example] Example §25.2: A Unit Impulse at t = 5
> Solve $2y'' + y' + 2y = \delta(t - 5)$, $y(0) = 0$, $y'(0) = 0$. This is the circuit or oscillator of [[§24 Differential Equations with Discontinuous Forcing Functions#^ex-24-1|Example §24.1]], now struck by a unit impulse at $t = 5$.
>
> **Transform.** $(2s^2 + s + 2)Y(s) = e^{-5s}$, so
>
> $$
> Y(s) = \frac{e^{-5s}}{2s^2 + s + 2} = \frac{e^{-5s}}{2}\cdot\frac{1}{(s + \frac14)^2 + \frac{15}{16}} .
> $$
>
> **Invert.** By [[§23 Step Functions#^thm-23-3|Theorem §23.3]],
>
> $$
> \mathcal{L}^{-1}\Big\{\frac{1}{(s + \frac14)^2 + \frac{15}{16}}\Big\} = \frac{4}{\sqrt{15}}\,e^{-t/4}\sin\frac{\sqrt{15}}{4}t ,
> $$
>
> and by [[§23 Step Functions#^thm-23-2|Theorem §23.2]]
>
> $$
> y(t) = \frac{2}{\sqrt{15}}\,u_5(t)\,e^{-(t - 5)/4}\sin\Big(\frac{\sqrt{15}}{4}(t - 5)\Big)
> = \begin{cases} 0, & t < 5, \\[2pt] \dfrac{2}{\sqrt{15}}\,e^{-(t - 5)/4}\sin\Big(\dfrac{\sqrt{15}}{4}(t - 5)\Big), & t \ge 5. \end{cases}
> $$
>
> **Behavior.** There is no response before $t = 5$; the impulse then starts a decaying oscillation that persists indefinitely (maximum $\approx 0.356$ at $t \approx 6.36$). The response is continuous at $t = 5$ despite the singular forcing. Its derivative jumps there, from $0$ to $y'(5^+) = \frac{2}{\sqrt{15}}\cdot\frac{\sqrt{15}}{4} = \frac12$, and $y''$ has an infinite discontinuity: a singularity on one side of the equation must be balanced by one on the other side.
>
> *BDP: Example 6.5.1*

^ex-25-2

![[m331-25-1.svg]]
*(a) The pulses $d_\tau$ of [[§25 Impulse Functions#^def-25-2|Definition §25.2]] for $\tau = 1, \frac12, \frac14$: narrower and taller, always with area $1$. (b) The responses of the system of [[§25 Impulse Functions#^ex-25-2|Example §25.2]] to the shifted pulses $d_\tau(t - 5)$ (computed with [[§23 Step Functions#^thm-23-2|Theorem §23.2]] from the step response of [[§24 Differential Equations with Discontinuous Forcing Functions#^ex-24-1|Example §24.1]]) approach its response to $\delta(t - 5)$ (blue) as $\tau \to 0^+$. This is the content of [[§25 Impulse Functions#^def-25-4|Definition §25.4]]: the impulse is the limit of short pulses of unit area.*

> [!remark] Remark: What an Impulse Does to y′
> In [[§25 Impulse Functions#^ex-25-2|Example §25.2]] the derivative jumps by $\frac12 = \frac{1}{a}$, where $a = 2$ is the leading coefficient. In general, for $ay'' + by' + cy = k\delta(t - t_0)$ the solution $y$ is continuous at $t_0$ and
>
> $$
> y'(t_0^+) - y'(t_0^-) = \frac{k}{a} .
> $$
>
> Integrate the equation over $[t_0 - \varepsilon, t_0 + \varepsilon]$: the right side gives $k$ ([[§25 Impulse Functions#^thm-25-3|Theorem §25.3]]), the left side gives $a\big[y'(t_0 + \varepsilon) - y'(t_0 - \varepsilon)\big] + b\big[y(t_0 + \varepsilon) - y(t_0 - \varepsilon)\big] + c\int y$, and as $\varepsilon \to 0$ only the first bracket survives because $y$ is continuous. Mechanically: the impulse $k$ changes the momentum $a\,y'$ by $k$ instantaneously, while the position has no time to change. So an impulse at $t_0$ is equivalent to restarting the free motion at $t_0$ with the velocity changed by $k/a$.

^rem-25-1

> [!example] Example §25.3: An Impulse After a Kick-Start
> Solve $y'' + 4y' + 20y = \delta(t - 3)$, $y(0) = 0$, $y'(0) = 12$.
>
> **Transform.** $s^2Y - 12 + 4sY + 20Y = e^{-3s}$, so
>
> $$
> Y(s) = \frac{12}{s^2 + 4s + 20} + \frac{e^{-3s}}{s^2 + 4s + 20}, \qquad s^2 + 4s + 20 = (s + 2)^2 + 4^2 .
> $$
>
> **Invert.** $\mathcal{L}^{-1}\Big\{\dfrac{1}{(s + 2)^2 + 4^2}\Big\} = \dfrac14 e^{-2t}\sin 4t$ by [[§23 Step Functions#^thm-23-3|Theorem §23.3]], so
>
> $$
> y(t) = 3e^{-2t}\sin 4t + \frac14\,u_3(t)\,e^{-2(t - 3)}\sin\big(4(t - 3)\big) .
> $$
>
> The first term is the free response to the initial velocity $12$; the second is the response to the unit impulse, which adds $1$ to $y'$ at $t = 3$ ([[§25 Impulse Functions#^rem-25-1|Remark: What an Impulse Does to y′]], $a = 1$).
>
> *Source: 331 Final (Fall 2021), Q5*

^ex-25-3

> [!example] Example §25.4: An Impulse Times a Continuous Function
> Solve $y'' + y = \delta(t - \pi)\cos t$, $y(0) = 0$, $y'(0) = 1$, and sketch the solution.
>
> **The forcing.** By the sifting property, $\delta(t - \pi)\cos t$ acts as $\cos\pi\,\delta(t - \pi) = -\delta(t - \pi)$:
>
> $$
> \mathcal{L}\{\delta(t - \pi)\cos t\} = \int_0^\infty e^{-st}\cos t\,\delta(t - \pi)\,dt = e^{-\pi s}\cos\pi = -e^{-\pi s} .
> $$
>
> **Transform.** $s^2Y - 1 + Y = -e^{-\pi s}$, so $Y(s) = \dfrac{1 - e^{-\pi s}}{s^2 + 1}$ and
>
> $$
> y(t) = \sin t - u_\pi(t)\sin(t - \pi) = \sin t + u_\pi(t)\sin t = \begin{cases} \sin t, & 0 \le t < \pi, \\ 2\sin t, & t \ge \pi, \end{cases}
> $$
>
> using $\sin(t - \pi) = -\sin t$.
>
> **Sketch.** The mass oscillates as $\sin t$ until $t = \pi$, when it passes through equilibrium with velocity $\cos\pi = -1$. The impulse $-1$ changes the velocity to $-2$ ([[§25 Impulse Functions#^rem-25-1|Remark: What an Impulse Does to y′]]), so from then on the motion is $2\sin t$: the same phase, twice the amplitude. The graph is the arch of $\sin t$ on $[0, \pi]$ followed by $2\sin t$, with a corner at $t = \pi$.
>
> *Source: 331 Written HW 5, Problem 6*

^ex-25-4

> [!example] Example §25.5: Choosing the Strength of an Impulse
> Consider $y'' + 2y' + y = k\delta(t - 3)$, $y(0) = 0$, $y'(0) = 0$, with $k$ a constant. (a) Solve. (b) Find $k$ such that the peak value of the solution is $7$.
>
> **(a)** $(s^2 + 2s + 1)Y = ke^{-3s}$, so $Y(s) = ke^{-3s}\dfrac{1}{(s + 1)^2}$. Since $\mathcal{L}^{-1}\{1/(s + 1)^2\} = te^{-t}$ ([[§23 Step Functions#^thm-23-3|Theorem §23.3]] with $\mathcal{L}\{t\} = 1/s^2$),
>
> $$
> y(t) = k\,u_3(t)\,(t - 3)\,e^{-(t - 3)} .
> $$
>
> The system is critically damped (repeated root $-1$), so after the impulse it rises once and decays without oscillating.
>
> **(b)** For $t > 3$, $y'(t) = k\,e^{-(t - 3)}\big(1 - (t - 3)\big)$, which is zero only at $t = 4$; $y' > 0$ before and $y' < 0$ after (for $k > 0$). So the peak is $y(4) = k\,e^{-1}$. Setting $k/e = 7$ gives $k = 7e$.
>
> *Source: 331 Written HW 5, Problem 7*

^ex-25-5
