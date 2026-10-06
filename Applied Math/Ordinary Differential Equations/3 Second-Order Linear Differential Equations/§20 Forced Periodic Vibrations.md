---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 20
bdp: "3.8"
aliases: ["BDP 3.8"]
tags: [ordinary-differential-equations, math331]
---
← [[§19 Mechanical and Electrical Vibrations]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§21 Definition of the Laplace Transform]] →

*Boyce–DiPrima, Section 3.8 · MATH 331 Written HW 4 (Problems 5, 6).*

This section drives the spring–mass system of [[§19 Mechanical and Electrical Vibrations|§19]] with a periodic force $F_0\cos(\omega t)$. With damping, the solution splits into a transient part, which dies out and absorbs the initial conditions, and a steady-state oscillation at the forcing frequency, whose amplitude depends on how close $\omega$ is to the natural frequency $\omega_0$; for small damping it peaks sharply near $\omega_0$ (resonance). Without damping nothing dies out. For $\omega \neq \omega_0$ the motion superposes two frequencies, which for $\omega$ near $\omega_0$ produces beats; for $\omega = \omega_0$ the amplitude grows linearly without bound.

## Forced Vibrations with Damping

> [!example] Example §20.1: Transient and Steady State
> **(a)** Solve
>
> $$
> u'' + u' + \frac54 u = 3\cos t, \qquad u(0) = 2, \quad u'(0) = 3 , \qquad (1),\ (2)
> $$
>
> and describe the solution for large $t$.
>
> **Homogeneous part.** $r^2 + r + \frac54 = 0$ has roots $r = -\frac12 \pm i$, so $u_c(t) = c_1e^{-t/2}\cos t + c_2e^{-t/2}\sin t$.
>
> **Particular solution.** Since $\pm i$ are not roots, try $U = A\cos t + B\sin t$. Then $U' = -A\sin t + B\cos t$, $U'' = -A\cos t - B\sin t$, and
>
> $$
> U'' + U' + \tfrac54 U = \Big(\tfrac14 A + B\Big)\cos t + \Big(-A + \tfrac14 B\Big)\sin t = 3\cos t .
> $$
>
> So $\frac14 A + B = 3$ and $-A + \frac14 B = 0$, i.e. $B = 4A$ and $\frac{17}{4}A = 3$: $A = \frac{12}{17}$, $B = \frac{48}{17}$.
>
> **Initial conditions.** In $u = u_c + U$: $u(0) = c_1 + \frac{12}{17} = 2$ gives $c_1 = \frac{22}{17}$; $u'(0) = -\frac12 c_1 + c_2 + \frac{48}{17} = 3$ gives $c_2 = 3 - \frac{48}{17} + \frac{11}{17} = \frac{14}{17}$. Hence
>
> $$
> u = \underbrace{\frac{22}{17}e^{-t/2}\cos t + \frac{14}{17}e^{-t/2}\sin t}_{\text{transient}} + \underbrace{\frac{12}{17}\cos t + \frac{48}{17}\sin t}_{\text{steady state}} . \qquad (6)
> $$
>
> The first two terms carry $e^{-t/2}$ and rapidly approach $0$; they come from the homogeneous equation and are needed to fit the initial conditions. The last two persist as long as the force acts. After a short time the solution is practically indistinguishable from the steady state $\frac{12}{17}\cos t + \frac{48}{17}\sin t$, an oscillation of amplitude $\frac{12}{17}\sqrt{1 + 16} = \frac{12}{\sqrt{17}} \approx 2.91$.
>
> **(b)** Find the general solution and the steady-state solution of $y'' + 4y' + 29y = 5\sin(3t)$.
>
> $r^2 + 4r + 29 = (r + 2)^2 + 25 = 0$ gives $r = -2 \pm 5i$, so $y_c = c_1e^{-2t}\cos 5t + c_2e^{-2t}\sin 5t$. With $Y = A\sin 3t + B\cos 3t$:
>
> $$
> Y'' + 4Y' + 29Y = (20A - 12B)\sin 3t + (12A + 20B)\cos 3t = 5\sin 3t ,
> $$
>
> so $12A + 20B = 0$ gives $B = -\frac35 A$, and then $20A + \frac{36}{5}A = \frac{136}{5}A = 5$: $A = \frac{25}{136}$, $B = -\frac{15}{136}$. The general solution is
>
> $$
> y = c_1e^{-2t}\cos 5t + c_2e^{-2t}\sin 5t + \frac{25}{136}\sin 3t - \frac{15}{136}\cos 3t .
> $$
>
> As $t \to \infty$ the $c_1, c_2$ terms tend to $0$ whatever $c_1, c_2$ are, so every solution approaches the steady-state solution $\frac{25}{136}\sin 3t - \frac{15}{136}\cos 3t$. (The general solution itself has no limit; "limiting function" means the function it becomes indistinguishable from.)
>
> *BDP: Example 3.8.1*
> *Source: 331 Written HW 4, Problem 6*

^ex-20-1

Now take a general spring–mass system with the periodic force $F_0\cos(\omega t)$, $F_0, \omega > 0$:
$$
mu'' + \gamma u' + ku = F_0\cos(\omega t) . \qquad (8)
$$

> [!definition] Definition §20.1: Transient and Steady-State Solutions
> For $m, \gamma, k > 0$ the general solution of (8) has the form
>
> $$
> u = c_1u_1(t) + c_2u_2(t) + A\cos(\omega t) + B\sin(\omega t) = u_c(t) + U(t) . \qquad (9)
> $$
>
> The homogeneous part $u_c(t)$, which dies out as $t \to \infty$, is the **transient solution**. The periodic part $U(t) = A\cos(\omega t) + B\sin(\omega t)$, with the same frequency as the force, is the **steady-state solution** or **forced response**.
>
> *BDP: 3.8 (text)*

^def-20-1

The transient lets the solution satisfy any initial conditions. As time goes on, the energy put in by the initial displacement and velocity is dissipated by damping, and the motion becomes the response to the external force. Without damping, the initial conditions would matter forever.

> [!theorem] Theorem §20.1: The Steady-State Response
> Let $m, \gamma, k > 0$ and $\omega_0^2 = k/m$. Every solution of (8) is $u = u_c + U$ with $u_c(t) \to 0$ as $t \to \infty$, and the steady-state solution is
>
> $$
> U(t) = R\cos(\omega t - \delta) , \qquad (10)
> $$
>
> where
>
> $$
> R = \frac{F_0}{\Delta}, \qquad \cos\delta = \frac{m(\omega_0^2 - \omega^2)}{\Delta}, \qquad \sin\delta = \frac{\gamma\omega}{\Delta}, \qquad (11)
> $$
>
> $$
> \Delta = \sqrt{m^2(\omega_0^2 - \omega^2)^2 + \gamma^2\omega^2} . \qquad (12)
> $$
>
> In particular $0 < \delta < \pi$: the response lags behind the force.
>
> *BDP: 3.8, Equations (9)–(12)*

^thm-20-1

> [!proof]+ Proof
> (BDP calls (11) "straightforward but somewhat lengthy" and leaves it as Problem 3.8.9; here it is.)
>
> **Transient.** $u_c$ solves $mu'' + \gamma u' + ku = 0$, so $u_c \to 0$ by [[§19 Mechanical and Electrical Vibrations#^thm-19-3|Theorem §19.3]]. The roots of $mr^2 + \gamma r + k = 0$ have nonzero real part $-\gamma/(2m)$ (complex case) or are negative, so $\pm i\omega$ are not roots and the trial form $U = A\cos\omega t + B\sin\omega t$ needs no factor $t$ ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|Theorem §17.4]]).
>
> **Coefficients.** Write $a = k - m\omega^2 = m(\omega_0^2 - \omega^2)$ and $b = \gamma\omega > 0$. Since $U'' = -\omega^2U$ and $U' = \omega(-A\sin\omega t + B\cos\omega t)$,
>
> $$
> mU'' + \gamma U' + kU = (aA + bB)\cos\omega t + (aB - bA)\sin\omega t .
> $$
>
> This equals $F_0\cos\omega t$ exactly when $aA + bB = F_0$ and $-bA + aB = 0$. The determinant of this system is $a^2 + b^2 = \Delta^2 > 0$ (as $b > 0$), and Cramer's rule ([[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-1|235 Thm. §22.1]]) gives
>
> $$
> A = \frac{aF_0}{\Delta^2}, \qquad B = \frac{bF_0}{\Delta^2} .
> $$
>
> **Amplitude and phase.** By [[§19 Mechanical and Electrical Vibrations#^prop-19-2|Proposition §19.2]], $U = R\cos(\omega t - \delta)$ with $R = \sqrt{A^2 + B^2} = \dfrac{F_0}{\Delta^2}\sqrt{a^2 + b^2} = \dfrac{F_0}{\Delta}$, $\cos\delta = A/R = a/\Delta$ and $\sin\delta = B/R = b/\Delta$. These are (11). Since $\sin\delta > 0$, $\delta \in (0, \pi)$.

^pf-20-1

*Uses:* [[§19 Mechanical and Electrical Vibrations#^thm-19-3|§19.3]], [[§19 Mechanical and Electrical Vibrations#^prop-19-2|§19.2]], [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|§17.4]] (undetermined coefficients), [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-1|235 Thm. §22.1]] (Cramer's rule)

> [!remark]- Connections
> - See also: [[§16★ Applications of Fourier Series and Integrals#^thm-16-1|341 Thm. §16.1]] (the periodic response to any periodic forcing, found term by term from the Fourier series of the force), with a damped oscillator driven by a square wave in [[§16★ Applications of Fourier Series and Integrals#^ex-16-1|341 Ex. §16.1]].

> [!theorem] Proposition §20.2: Amplitude of the Forced Response
> In the notation of [[§20 Forced Periodic Vibrations#^thm-20-1|Theorem §20.1]], with $\Gamma = \dfrac{\gamma^2}{mk}$,
>
> $$
> \frac{Rk}{F_0} = \left[\Big(1 - \frac{\omega^2}{\omega_0^2}\Big)^2 + \Gamma\,\frac{\omega^2}{\omega_0^2}\right]^{-1/2} . \qquad (13)
> $$
>
> 1. $R \to F_0/k$ as $\omega \to 0$, and $R \to 0$ as $\omega \to \infty$.
> 2. If $\gamma^2 < 2mk$, $R$ has its maximum at $\omega = \omega_{\max}$, where
>
> $$
> \omega_{\max}^2 = \omega_0^2 - \frac{\gamma^2}{2m^2} = \omega_0^2\Big(1 - \frac{\gamma^2}{2mk}\Big), \qquad (14)
> $$
>
> $$
> R_{\max} = \frac{F_0}{\gamma\omega_0\sqrt{1 - \gamma^2/(4mk)}} \cong \frac{F_0}{\gamma\omega_0}\Big(1 + \frac{\gamma^2}{8mk}\Big) , \qquad (15)
> $$
>
> the approximation being valid for small $\gamma$. So $\omega_{\max} < \omega_0$, and $\omega_{\max}$ is close to $\omega_0$ when $\gamma$ is small.
> 3. If $\gamma^2 \ge 2mk$ (i.e. $\Gamma \ge 2$), $R$ is a decreasing function of $\omega$, with its maximum $F_0/k$ at $\omega = 0$.
> 4. As $\gamma \to 0$, $R \to \dfrac{F_0}{m|\omega_0^2 - \omega^2|}$, so the graph of $Rk/F_0$ approaches the vertical line $\omega = \omega_0$.
>
> *BDP: 3.8, Equations (13)–(15) and text*

^prop-20-2

> [!proof]+ Proof
> (BDP gives the outcome of these computations; they are Problem 3.8.9.)
>
> **Equation (13).** $R = F_0/\Delta$ and $k = m\omega_0^2$, so $Rk/F_0 = k/\Delta$ and
>
> $$
> \frac{\Delta^2}{k^2} = \frac{m^2(\omega_0^2 - \omega^2)^2}{m^2\omega_0^4} + \frac{\gamma^2\omega^2}{k^2}
> = \Big(1 - \frac{\omega^2}{\omega_0^2}\Big)^2 + \frac{\gamma^2}{mk}\cdot\frac{m\,\omega^2}{k} ,
> $$
>
> and $m\omega^2/k = \omega^2/\omega_0^2$.
>
> **1.** As $\omega \to 0$, $\Delta \to m\omega_0^2 = k$; as $\omega \to \infty$, $\Delta \ge m|\omega_0^2 - \omega^2| \to \infty$.
>
> **2 and 3.** $R$ is largest where $\Delta^2$ is smallest. As a function of $z = \omega^2 \ge 0$,
>
> $$
> D(z) = m^2(\omega_0^2 - z)^2 + \gamma^2 z, \qquad D'(z) = -2m^2(\omega_0^2 - z) + \gamma^2, \qquad D''(z) = 2m^2 > 0 .
> $$
>
> So $D$ is convex with its only critical point at $z^* = \omega_0^2 - \gamma^2/(2m^2)$. Since $\omega_0^2 = k/m$, $z^* > 0$ exactly when $\gamma^2 < 2mk$; then $D$ is smallest at $z^*$, which is (14). If $\gamma^2 \ge 2mk$, then $z^* \le 0$, $D' > 0$ on $z > 0$, $D$ is increasing, and $R$ decreases in $\omega$ from its value $F_0/k$ at $\omega = 0$. At $z^*$, $\omega_0^2 - z^* = \gamma^2/(2m^2)$, so
>
> $$
> D(z^*) = \frac{\gamma^4}{4m^2} + \gamma^2\omega_0^2 - \frac{\gamma^4}{2m^2} = \gamma^2\omega_0^2 - \frac{\gamma^4}{4m^2} = \gamma^2\omega_0^2\Big(1 - \frac{\gamma^2}{4m^2\omega_0^2}\Big) = \gamma^2\omega_0^2\Big(1 - \frac{\gamma^2}{4mk}\Big) ,
> $$
>
> and $R_{\max} = F_0/\sqrt{D(z^*)}$ is (15). The approximation is $(1 - x)^{-1/2} \approx 1 + \frac{x}{2}$ with $x = \gamma^2/(4mk)$.
>
> **4.** As $\gamma \to 0$, $\Delta \to m|\omega_0^2 - \omega^2|$ for each $\omega \ne \omega_0$, and at $\omega = \omega_0$, $R = F_0/(\gamma\omega_0) \to \infty$.

^pf-20-2

*Uses:* [[§20 Forced Periodic Vibrations#^thm-20-1|§20.1]]

![[m331-20-2.svg]]
*The amplitude response (13) against $\omega/\omega_0$ for several damping parameters $\Gamma = \gamma^2/(mk)$. Every curve starts at $1$ (the static displacement $F_0/k$) and tends to $0$. For $\Gamma = 1/64$ ([[§20 Forced Periodic Vibrations#^ex-20-2|Example §20.2]]) the peak is $\approx 8.02$, just below $\omega/\omega_0 = 1$; for $\Gamma = 2$ there is no peak. The dashed curve $1/|1 - \omega^2/\omega_0^2|$ is the undamped limit $\Gamma \to 0$.*

> [!definition] Definition §20.2: Resonance
> For a lightly damped system, the amplitude $R$ of the forced response is large when $\omega$ is near $\omega_0$, even for small forces: by (15), $R_{\max} \approx F_0/(\gamma\omega_0)$, and the smaller $\gamma$, the more pronounced the peak. This phenomenon is called **resonance**.
>
> *BDP: 3.8 (text)*

^def-20-2

Resonance can be harmful (structures such as buildings and bridges can fail catastrophically) or useful (instruments such as seismographs are designed to resonate with weak incoming signals). The three quantities $Rk/F_0$, $\omega/\omega_0$ and $\Gamma$ are dimensionless (BDP, Problem 3.8.9d), so (13) reduces the five parameters $m, \gamma, k, F_0, \omega$ of (8) to three, and one family of curves describes the response of every system (8). The value $\Gamma = 2$ separates the curves with a peak from the monotone ones; critical damping is $\Gamma = 4$.

> [!remark] Remark: The Phase of the Response
> By (11), the phase $\delta$ also depends on $\omega$. For $\omega$ near $0$, $\cos\delta \approx 1$ and $\sin\delta \approx 0$: $\delta \approx 0$, and the response is nearly in phase with the force (their maxima and minima occur nearly together). At $\omega = \omega_0$, $\cos\delta = 0$ and $\sin\delta = 1$: $\delta = \pi/2$, so the peaks of the response come a quarter period after the peaks of the force. For $\omega$ very large, $\cos\delta \approx -1$, $\sin\delta \approx 0$: $\delta \approx \pi$, and the response is nearly out of phase (minimal when the force is maximal). For small damping the transition from $\delta \approx 0$ to $\delta \approx \pi$ is abrupt near $\omega_0$; for larger damping it is gradual.

^rem-20-1

> [!example] Example §20.2: Low, Resonant and High Forcing Frequencies
> Consider
>
> $$
> u'' + \frac18 u' + u = 3\cos(\omega t), \qquad u(0) = 2, \quad u'(0) = 0 , \qquad (16)
> $$
>
> the system of [[§19 Mechanical and Electrical Vibrations#^ex-19-4|Example §19.4]] driven by a periodic force, and compare the steady-state responses for $\omega = 0.3$, $1$ and $2$.
>
> Here $m = k = 1$, $\gamma = \frac18$, so $\omega_0 = 1$, $\Gamma = \frac{1}{64} = 0.015625$, and the static displacement is $F_0/k = 3$. By (11)–(12), $\Delta = \sqrt{(1 - \omega^2)^2 + \omega^2/64}$, $R = 3/\Delta$, and $\delta$ is the angle with $\cos\delta = (1 - \omega^2)/\Delta$, $\sin\delta = (\omega/8)/\Delta$.
> - **$\omega = 0.3$ (low).** $\Delta = \sqrt{0.91^2 + 0.0375^2} = \sqrt{0.82950625} \approx 0.91077$, so $R \approx 3.2939$, slightly larger than the static displacement, and $\delta = \arctan(0.0375/0.91) \approx 0.041185$: essentially in phase with the force.
> - **$\omega = 1$ (resonant).** $\Delta = \frac18$, so $R = 24$, eight times the static displacement, and $\delta = \pi/2$: the predicted quarter-period lag.
> - **$\omega = 2$ (high).** $\Delta = \sqrt{9 + \frac{1}{16}} \approx 3.01040$, so $R \approx 0.99655$, about one third of the static displacement, and $\delta = \pi - \arctan\frac{0.25}{3} \approx 3.0585$: nearly opposite in phase.
>
> In each case the full solution of (16) is the transient of Example §19.4's type, decaying like $e^{-t/16}$, plus $R\cos(\omega t - \delta)$; once the transient has died out, the motion is the steady state with these amplitudes and phases.
>
> *BDP: Example 3.8.2*

^ex-20-2

## Forced Vibrations Without Damping

With $\gamma = 0$ the equation is that of an **undamped forced oscillator**,
$$
mu'' + ku = F_0\cos(\omega t) . \qquad (17)
$$
The form of its general solution depends on whether $\omega$ equals the natural frequency $\omega_0 = \sqrt{k/m}$.

> [!theorem] Proposition §20.3: Undamped Forcing off Resonance; Beats
> If $\omega \ne \omega_0$, the general solution of (17) is
>
> $$
> u = c_1\cos(\omega_0 t) + c_2\sin(\omega_0 t) + \frac{F_0}{m(\omega_0^2 - \omega^2)}\cos(\omega t) . \qquad (18)
> $$
>
> If the mass starts at rest, $u(0) = 0$, $u'(0) = 0$, then $c_1 = -\dfrac{F_0}{m(\omega_0^2 - \omega^2)}$, $c_2 = 0$ (19), and
>
> $$
> u = \frac{F_0}{m(\omega_0^2 - \omega^2)}\big(\cos(\omega t) - \cos(\omega_0 t)\big)
> = \frac{2F_0}{m(\omega_0^2 - \omega^2)}\sin\Big(\frac12(\omega_0 - \omega)t\Big)\sin\Big(\frac12(\omega_0 + \omega)t\Big) . \qquad (20),\ (21)
> $$
>
> *BDP: 3.8, Equations (18)–(21)*

^prop-20-3

> [!proof]+ Proof
> Since $\omega \ne \omega_0$, $\cos\omega t$ is not a solution of $mu'' + ku = 0$, so try $U = A\cos\omega t$: $mU'' + kU = (k - m\omega^2)A\cos\omega t = m(\omega_0^2 - \omega^2)A\cos\omega t$, which equals $F_0\cos\omega t$ for $A = F_0/\big(m(\omega_0^2 - \omega^2)\big)$. Adding the homogeneous solution of [[§19 Mechanical and Electrical Vibrations#^prop-19-2|Proposition §19.2]] gives (18).
>
> At rest: $u(0) = c_1 + A = 0$ gives $c_1 = -A$, and $u'(0) = \omega_0c_2 = 0$ gives $c_2 = 0$; this is (20). For (21), let $\alpha = \frac12(\omega_0 + \omega)t$ and $\beta = \frac12(\omega_0 - \omega)t$, so that $\alpha - \beta = \omega t$ and $\alpha + \beta = \omega_0 t$. By the addition formulas,
>
> $$
> \cos(\omega t) - \cos(\omega_0 t) = \cos(\alpha - \beta) - \cos(\alpha + \beta) = 2\sin\alpha\sin\beta .
> $$
>
> *(BDP prints (21) with the factor $\frac{2F_0}{m}(\omega_0^2 - \omega^2)$; the factor $\omega_0^2 - \omega^2$ belongs in the denominator, as in (20) and in BDP's amplitude formula that follows.)*

^pf-20-3

*Uses:* [[§19 Mechanical and Electrical Vibrations#^prop-19-2|§19.2]], [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|§17.4]] (undetermined coefficients), [[§119 Trigonometry#^thm-119-6|Calc Thm. §119.6]] (addition formulas)

> [!definition] Definition §20.3: Beat
> If $|\omega_0 - \omega|$ is small, then $\omega_0 + \omega \gg |\omega_0 - \omega|$, and (21) is a rapid oscillation with frequency $\frac12(\omega_0 + \omega)$ whose amplitude
>
> $$
> \frac{2F_0}{m|\omega_0^2 - \omega^2|}\,\Big|\sin\Big(\frac12(\omega_0 - \omega)t\Big)\Big|
> $$
>
> varies slowly and periodically. Motion with such a periodic variation of amplitude exhibits a **beat**. (In acoustics: two tuning forks of nearly equal frequency sounding together. In electronics the variation of amplitude with time is called **amplitude modulation**.)
>
> *BDP: 3.8 (text)*

^def-20-3

> [!example] Example §20.3: A Beat
> Solve $u'' + u = \frac12\cos(0.8t)$, $u(0) = 0$, $u'(0) = 0$, and describe the solution.
>
> Here $m = 1$, $\omega_0 = 1$, $\omega = 0.8$, $F_0 = \frac12$, so $\frac{F_0}{m(\omega_0^2 - \omega^2)} = \frac{0.5}{0.36} = \frac{25}{18}$ and by (21)
>
> $$
> u = \frac{25}{9}\sin(0.1t)\sin(0.9t) \approx 2.778\sin(0.1t)\sin(0.9t) . \qquad (23)
> $$
>
> The amplitude $2.778|\sin(0.1t)|$ has slow frequency $0.1$ and period $2\pi/0.1 = 20\pi$; a half-period $10\pi \approx 31.4$ is one cycle of growing and then shrinking amplitude. Inside it the mass oscillates with the fast frequency $0.9$, slightly less than $\omega_0$.
>
> If $\omega$ is increased to $0.9$, the slow frequency halves to $0.05$ (slow half-period $20\pi$), the multiplier grows to $\frac{1}{1 - 0.81} \approx 5.263$, and the fast frequency rises only to $0.95$. As $\omega \to \omega_0$ the beats become longer and taller: the limit is the resonance below.
>
> *BDP: Example 3.8.3*

^ex-20-3

> [!theorem] Proposition §20.4: Undamped Resonance
> If $\omega = \omega_0$, the general solution of $mu'' + ku = F_0\cos(\omega_0 t)$ is
>
> $$
> u = c_1\cos(\omega_0 t) + c_2\sin(\omega_0 t) + \frac{F_0}{2m\omega_0}\,t\sin(\omega_0 t) . \qquad (24)
> $$
>
> Every solution is unbounded as $t \to \infty$.
>
> *BDP: 3.8, Equation (24)*

^prop-20-4

> [!proof]+ Proof
> Now $F_0\cos\omega_0 t$ solves the homogeneous equation, so the trial form needs the factor $t$ ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|Theorem §17.4]]): $U = t(A\cos\omega_0 t + B\sin\omega_0 t)$. Write $V = A\cos\omega_0 t + B\sin\omega_0 t$, so $V'' = -\omega_0^2V$. Then $U = tV$, $U'' = 2V' + tV'' = 2V' - \omega_0^2 tV$, and
>
> $$
> U'' + \omega_0^2U = 2V' = 2\omega_0(-A\sin\omega_0 t + B\cos\omega_0 t) .
> $$
>
> Dividing (17) by $m$, we need $U'' + \omega_0^2 U = (F_0/m)\cos\omega_0 t$, so $A = 0$ and $B = F_0/(2m\omega_0)$. With the homogeneous solution this is (24). The first two terms of (24) are bounded, while $t\sin(\omega_0 t)$ takes the values $\pm t$ at $t = (n + \frac12)\pi/\omega_0$, so $u$ is unbounded whatever $c_1$ and $c_2$ are.

^pf-20-4

*Uses:* [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|§17.4]] (undetermined coefficients, the factor $t$), [[§19 Mechanical and Electrical Vibrations#^prop-19-2|§19.2]]

> [!remark]- Connections
> - PDE version: [[§54★ More Difficult Examples#^ex-54-3|341 Ex. §54.3]] (a wire driven at one of its natural frequencies, solved by Laplace transform: the resonant mode grows like $t\cos(\pi t)$).

> [!example] Example §20.4: Resonance
> **(a)** Solve $u'' + u = \frac12\cos t$, $u(0) = 0$, $u'(0) = 0$.
>
> Here $\omega = \omega_0 = 1$, $m = 1$, $F_0 = \frac12$, so by (24) $u = c_1\cos t + c_2\sin t + \frac{t}{4}\sin t$. Then $u(0) = c_1 = 0$, and $u'(0) = c_2 + \big[\frac14\sin t + \frac{t}{4}\cos t\big]_{t=0} = c_2 = 0$:
>
> $$
> u = \frac{t}{4}\sin t . \qquad (26)
> $$
>
> It oscillates between the lines $u = \pm t/4$ and grows without bound (figure (b)).
>
> **(b)** For the forced system $\dfrac{d^2y}{dt^2} + 3y = 7\sin(\alpha t)$ (parameter $\alpha > 0$): for which $\alpha$ does it exhibit resonance? Find the general solution for that $\alpha$.
>
> The natural frequency is $\omega_0 = \sqrt3$ ($r^2 + 3 = 0$, $r = \pm\sqrt3\,i$), so resonance occurs for $\alpha = \sqrt3$, when the forcing $\sin(\sqrt3\,t)$ solves the homogeneous equation. Try $Y = t(A\cos\sqrt3\,t + B\sin\sqrt3\,t)$; as in the proof of [[§20 Forced Periodic Vibrations#^prop-20-4|Proposition §20.4]],
>
> $$
> Y'' + 3Y = 2\sqrt3\,(-A\sin\sqrt3\,t + B\cos\sqrt3\,t) = 7\sin\sqrt3\,t ,
> $$
>
> so $B = 0$ and $A = -\frac{7}{2\sqrt3} = -\frac{7\sqrt3}{6}$:
>
> $$
> y = c_1\cos(\sqrt3\,t) + c_2\sin(\sqrt3\,t) - \frac{7\sqrt3}{6}\,t\cos(\sqrt3\,t) .
> $$
>
> *BDP: Example 3.8.4*
> *Source: 331 Written HW 4, Problem 5*

^ex-20-4

![[m331-20-1.svg]]
*(a) The beat of [[§20 Forced Periodic Vibrations#^ex-20-3|Example §20.3]]: $u = 2.778\sin(0.1t)\sin(0.9t)$ (blue) inside the slowly varying amplitude $\pm 2.778\sin(0.1t)$ (red, dashed); one beat lasts $10\pi$. (b) Resonance, [[§20 Forced Periodic Vibrations#^ex-20-4|Example §20.4]](a): $u = \frac{t}{4}\sin t$ between the lines $u = \pm t/4$. As $\omega \to \omega_0$ in (a), the length $2\pi/|\omega_0 - \omega|$ of a beat grows and the first half of each beat approaches the linear growth in (b).*

> [!remark] Remark: Unbounded Growth Is a Limit of the Model
> Because of the term $t\sin(\omega_0 t)$, (24) predicts unbounded motion whatever the initial conditions. In reality the spring cannot stretch infinitely far, and as soon as $u$ becomes large the model itself fails, since Hooke's law assumes $u$ small. With damping, the response stays bounded ([[§20 Forced Periodic Vibrations#^thm-20-1|Theorem §20.1]]), but by (15) it can still be very large when $\gamma$ is small and $\omega$ is close to $\omega_0$.

^rem-20-2
