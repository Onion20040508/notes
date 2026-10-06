---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 19
bdp: "3.7"
aliases: ["BDP 3.7"]
tags: [ordinary-differential-equations, math331]
---
← [[§18★ Variation of Parameters]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§20 Forced Periodic Vibrations]] →

*Boyce–DiPrima, Section 3.7 · MATH 331 Written HW 4 (Problems 1, 2), Final Exam (Fall 2021, Q2).*

A mass on a spring, with a damper and an external force, obeys $mu'' + \gamma u' + ku = F(t)$, and a series circuit with inductance, resistance and capacitance obeys $LQ'' + RQ' + Q/C = E(t)$: the same constant-coefficient equation with different names for the constants. This section derives the spring–mass equation from Newton's law, then reads off the free motion ($F = 0$) from the root cases of [[§13 Homogeneous Differential Equations with Constant Coefficients|§13]]–[[§16 Repeated Roots; Reduction of Order|§16]]. Without damping the motion is simple harmonic, $u = R\cos(\omega_0 t - \delta)$. With damping every solution dies out, and the sign of $\gamma^2 - 4km$ decides how: as a damped oscillation (underdamped), or without oscillating (critically damped or overdamped).

## The Spring–Mass System

A mass $m$ hangs at rest on a vertical spring of natural length $l$ and stretches it by $L$. Measure the displacement $u(t)$ of the mass from this equilibrium position, **positive downward**.

> [!definition] Definition §19.1: Hooke's Law and the Spring Constant
> For a small elongation the spring force is proportional to the elongation and opposes it: an elongation $L$ produces the force $F_s = -kL$ (**Hooke's law**). The constant $k > 0$ is the **spring constant**; it has units of force per length. At equilibrium the weight $w = mg$ balances the spring force,
>
> $$
> w + F_s = mg - kL = 0 , \qquad (2)
> $$
>
> so $k = w/L$ can be measured by hanging a known weight on the spring.
>
> *BDP: 3.7 (text)*

^def-19-1

> [!definition] Definition §19.2: Viscous Damping
> The **damping** (resistive) force $F_d$ acts opposite to the direction of motion. It is modeled as proportional to the speed, $|F_d| = \gamma|u'|$ (**viscous damping**). With the downward-positive convention this is, in both directions of motion,
>
> $$
> F_d(t) = -\gamma u'(t) , \qquad (5)
> $$
>
> where $\gamma > 0$ is the **damping constant** (damping coefficient). If $u' > 0$ the mass moves down and $F_d = -\gamma u'$ points up; if $u' < 0$ it moves up and $F_d = \gamma|u'| = -\gamma u'$ points down.
>
> *BDP: 3.7 (text)*

^def-19-2

> [!theorem] Proposition §19.1: The Equation of Motion
> Under Hooke's law, viscous damping and an applied external force $F(t)$ (positive downward), the displacement $u(t)$ from equilibrium satisfies
>
> $$
> mu''(t) + \gamma u'(t) + ku(t) = F(t) , \qquad (7)
> $$
>
> with $m, \gamma, k > 0$. Together with the initial position and velocity
>
> $$
> u(0) = u_0, \qquad u'(0) = v_0 , \qquad (8)
> $$
>
> it has a unique solution for every $u_0, v_0$ (for $F$ continuous).
>
> *BDP: 3.7, Equations (7) and (8)*

^prop-19-1

> [!proof]+ Proof
> By Newton's law, $mu'' = f$, the net force on the mass. Four forces act:
> 1. the weight $w = mg$, downward;
> 2. the spring force, proportional to the total elongation $L + u$ and restoring: $F_s = -k(L + u)$. This holds also when the spring is compressed: then $L + u < 0$, the force is $k|L + u|$ downward, and $k|L + u| = -k(L + u)$;
> 3. the damping force $F_d = -\gamma u'$ (Definition §19.2);
> 4. the external force $F(t)$.
>
> Hence
>
> $$
> mu''(t) = mg - k\big(L + u(t)\big) - \gamma u'(t) + F(t) . \qquad (6)
> $$
>
> By (2), $mg - kL = 0$, and what remains is (7). Dividing by $m$ puts (7) in the form $u'' + (\gamma/m)u' + (k/m)u = F/m$ with constant (hence continuous) coefficients, so the existence and uniqueness theorem ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]], Theorem 3.2.1) gives exactly one solution with the data (8), for all $t$.
>
> Equation (7) is only approximate: Hooke's law and (5) are approximations for small displacements and moderate speeds, and the mass of the spring has been neglected.

^pf-19-1

*Uses:* [[§19 Mechanical and Electrical Vibrations#^def-19-1|Def. §19.1]], [[§19 Mechanical and Electrical Vibrations#^def-19-2|Def. §19.2]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|§14.1]] (Theorem 3.2.1)

> [!remark] Remark: Method — Setting Up a Spring–Mass Problem
> 1. **Units.** Fix one unit of length (feet *or* inches, metres *or* centimetres) and of time, and convert all data. In English units weights are given in pounds and $g = 32$ ft/s$^2$.
> 2. **Mass:** $m = w/g$ (units lb·s$^2$/ft, or kg).
> 3. **Spring constant:** $k = w/L$ from the equilibrium stretch $L$ (Definition §19.1).
> 4. **Damping constant:** $\gamma = (\text{resisting force})/(\text{speed})$ from the stated resistance at a stated speed.
> 5. **Initial conditions:** $u(0)$ is the initial displacement (positive below equilibrium), $u'(0)$ the initial velocity (positive downward). "Released" means $u'(0) = 0$.
> 6. Write $mu'' + \gamma u' + ku = F(t)$, and solve with the root cases of $mr^2 + \gamma r + k = 0$.

^rem-19-1

## Undamped Free Vibrations

With no external force and no damping ($F = 0$, $\gamma = 0$, an idealization that is reasonable over short times when damping is small), (7) becomes
$$
mu'' + ku = 0 . \qquad (11)
$$
Its characteristic equation $mr^2 + k = 0$ has roots $r = \pm i\sqrt{k/m}$.

> [!theorem] Proposition §19.2: Simple Harmonic Motion
> The general solution of $mu'' + ku = 0$ is
>
> $$
> u = A\cos(\omega_0 t) + B\sin(\omega_0 t), \qquad \omega_0^2 = \frac{k}{m} , \qquad (12),\ (13)
> $$
>
> and it can be written as
>
> $$
> u = R\cos(\omega_0 t - \delta) , \qquad (14)
> $$
>
> where
>
> $$
> A = R\cos\delta, \quad B = R\sin\delta; \qquad R = \sqrt{A^2 + B^2}, \quad \tan\delta = \frac{B}{A} . \qquad (16),\ (17)
> $$
>
> The quadrant of $\delta$ is fixed by the signs of $\cos\delta = A/R$ and $\sin\delta = B/R$, not by $\tan\delta$ alone.
>
> *BDP: 3.7, Equations (12)–(17)*

^prop-19-2

> [!proof]+ Proof
> The roots $r = \pm i\omega_0$ have real part $0$, so (12) is the general solution by the complex-root case ([[§15 Complex Roots of the Characteristic Equation#^thm-15-2|Theorem §15.2]]). If $A = B = 0$ take $R = 0$. Otherwise let $R = \sqrt{A^2 + B^2} > 0$. The point $(A/R, B/R)$ lies on the unit circle, so there is an angle $\delta$ with $\cos\delta = A/R$ and $\sin\delta = B/R$; that is (16), and then $\tan\delta = B/A$ when $A \neq 0$. By the addition formula for cosine,
>
> $$
> R\cos(\omega_0 t - \delta) = R\cos\delta\cos(\omega_0 t) + R\sin\delta\sin(\omega_0 t) = A\cos(\omega_0 t) + B\sin(\omega_0 t) . \qquad (15)
> $$

^pf-19-2

*Uses:* [[§15 Complex Roots of the Characteristic Equation#^thm-15-2|§15.2]] (general solution for complex roots), [[§119 Trigonometry#^thm-119-6|Calc Thm. §119.6]] (addition formulas)

> [!remark]- Connections
> - PDE version: [[§30 Solution of the Vibrating String Problem#^def-30-1|341 Def. §30.1]] (standing waves: each mode of a vibrating string oscillates in time as $a_n\cos(\lambda_nct) + b_n\sin(\lambda_nct)$, a simple harmonic motion with the natural frequencies of [[§30 Solution of the Vibrating String Problem#^def-30-2|341 Def. §30.2]]).
> - Stewart's spring equation $m\,x'' = -kx$ and its sine–cosine solutions, checked by substitution: [[§57 Modeling with Differential Equations#^def-57-4|Calc Def. §57.4]], [[§57 Modeling with Differential Equations#^prop-57-3|Calc Prop. §57.3]].

> [!definition] Definition §19.3: Natural Frequency, Period, Amplitude, Phase
> The motion (14) is **simple harmonic motion**: a displaced cosine wave. Its
> - **natural frequency** is $\omega_0 = \sqrt{k/m}$ (a circular frequency, in radians per unit time);
> - **period** is $T = \dfrac{2\pi}{\omega_0} = 2\pi\Big(\dfrac{m}{k}\Big)^{1/2}$; (18)
> - **amplitude** is $R$, the maximum displacement from equilibrium;
> - **phase** (phase angle) is the dimensionless $\delta$, the shift of the wave from the position $\delta = 0$.
>
> The amplitude never decreases: without damping the energy given by the initial data cannot be dissipated. The frequency $\omega_0$ does not depend on the initial conditions, which only set $R$ and $\delta$. Larger masses vibrate more slowly ($T$ increases with $m$); stiffer springs vibrate faster ($T$ decreases with $k$).
>
> *BDP: 3.7 (text)*

^def-19-3

> [!example] Example §19.1: Setting Up and Solving Spring Problems
> **(a) Formulating.** A mass weighing 4 lb stretches a spring 2 in. It is given an additional 6-in displacement in the positive direction and released. The medium exerts a viscous resistance of 6 lb when the speed is 3 ft/s. Formulate the initial value problem.
>
> Measure $u$ in feet and $t$ in seconds. No external force is mentioned, so $F = 0$. Then
>
> $$
> m = \frac{w}{g} = \frac{4\ \text{lb}}{32\ \text{ft/s}^2} = \frac18\ \frac{\text{lb·s}^2}{\text{ft}}, \qquad
> \gamma = \frac{6\ \text{lb}}{3\ \text{ft/s}} = 2\ \frac{\text{lb·s}}{\text{ft}}, \qquad
> k = \frac{4\ \text{lb}}{\frac16\ \text{ft}} = 24\ \frac{\text{lb}}{\text{ft}} .
> $$
>
> So $\frac18 u'' + 2u' + 24u = 0$, that is, $u'' + 16u' + 192u = 0$, with $u(0) = \frac12$ ft and $u'(0) = 0$ ("released").
>
> **(b) An undamped system.** A mass weighing 10 lb stretches a spring 2 in. It is displaced an additional 2 in and set in motion with an upward velocity of 1 ft/s. Find its position, and the period, amplitude and phase.
>
> Here $k = 10\ \text{lb}/\frac16\ \text{ft} = 60$ lb/ft and $m = 10/32$ lb·s$^2$/ft, so $\omega_0^2 = k/m = 60 \cdot \frac{32}{10} = 192$ and
>
> $$
> u'' + 192u = 0, \qquad u(0) = \tfrac16\ \text{ft}, \quad u'(0) = -1\ \text{ft/s}
> $$
>
> (upward is negative). The general solution is $u = A\cos(8\sqrt3\,t) + B\sin(8\sqrt3\,t)$, since $\sqrt{192} = 8\sqrt3$. Then $A = u(0) = \frac16$ and $8\sqrt3\,B = u'(0) = -1$, so
>
> $$
> u = \frac16\cos(8\sqrt3\,t) - \frac{1}{8\sqrt3}\sin(8\sqrt3\,t) .
> $$
>
> **Frequency and period:** $\omega_0 = 8\sqrt3 \approx 13.856$ rad/s, $T = 2\pi/\omega_0 \approx 0.453$ s.
>
> **Amplitude:** $R^2 = \frac{1}{36} + \frac{1}{192} = \frac{16 + 3}{576} = \frac{19}{576}$, so $R = \frac{\sqrt{19}}{24} \approx 0.182$ ft.
>
> **Phase:** $\tan\delta = B/A = -\frac{6}{8\sqrt3} = -\frac{\sqrt3}{4}$. This has a solution in the second quadrant and one in the fourth. Since $\cos\delta = A/R > 0$ and $\sin\delta = B/R < 0$, $\delta$ is in the fourth quadrant:
>
> $$
> \delta = -\arctan\frac{\sqrt3}{4} \approx -0.40864\ \text{rad}, \qquad u \approx 0.182\cos(8\sqrt3\,t + 0.409) .
> $$
>
> *BDP: Examples 3.7.1 and 3.7.2*

^ex-19-1

## Damped Free Vibrations

With damping and no external force, (7) is
$$
mu'' + \gamma u' + ku = 0 , \qquad (21)
$$
with characteristic equation $mr^2 + \gamma r + k = 0$ and roots
$$
r_1, r_2 = \frac{-\gamma \pm \sqrt{\gamma^2 - 4km}}{2m} = \frac{\gamma}{2m}\left(-1 \pm \sqrt{1 - \frac{4km}{\gamma^2}}\right) . \qquad (22)
$$

> [!theorem] Theorem §19.3: The Three Damping Cases
> Let $m, \gamma, k > 0$. The general solution of $mu'' + \gamma u' + ku = 0$ is
>
> $$
> \begin{aligned}
> \gamma^2 - 4km > 0: &\quad u = Ae^{r_1t} + Be^{r_2t}, \quad r_1, r_2 < 0 \text{ as in (22)}; && (23) \\
> \gamma^2 - 4km = 0: &\quad u = (A + Bt)e^{-\gamma t/(2m)}; && (24) \\
> \gamma^2 - 4km < 0: &\quad u = e^{-\gamma t/(2m)}\big(A\cos(\mu t) + B\sin(\mu t)\big), \quad \mu = \frac{(4km - \gamma^2)^{1/2}}{2m} > 0 . && (25)
> \end{aligned}
> $$
>
> In every case, **every solution tends to $0$ as $t \to \infty$**, whatever the initial conditions. In cases (23) and (24), a solution that is not identically zero passes through the equilibrium $u = 0$ at most once.
>
> In case (25), with $A = R\cos\delta$, $B = R\sin\delta$ as in Proposition §19.2,
>
> $$
> u = Re^{-\gamma t/(2m)}\cos(\mu t - \delta) , \qquad (26)
> $$
>
> which lies between the curves $u = \pm Re^{-\gamma t/(2m)}$.
>
> *BDP: 3.7, Equations (23)–(26) and text*

^thm-19-3

> [!proof]+ Proof
> **The general solutions.** These are the three root cases: distinct real roots ([[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-2|Theorem §13.2]]), the repeated root $-\gamma/(2m)$ ([[§16 Repeated Roots; Reduction of Order#^thm-16-1|Theorem §16.1]]), and complex roots $-\gamma/(2m) \pm i\mu$ ([[§15 Complex Roots of the Characteristic Equation#^thm-15-2|Theorem §15.2]]).
>
> **Decay.** Since $m, \gamma, k > 0$, we have $\gamma^2 - 4km < \gamma^2$. In case (23), $0 < \sqrt{\gamma^2 - 4km} < \gamma$, so both roots $\frac{-\gamma \pm \sqrt{\gamma^2 - 4km}}{2m}$ are negative and $e^{r_1t}, e^{r_2t} \to 0$. In case (24), $te^{-\gamma t/(2m)} \to 0$ because an exponential beats any power of $t$. In case (25), $|A\cos\mu t + B\sin\mu t| \le |A| + |B|$, and the factor $e^{-\gamma t/(2m)} \to 0$.
>
> **At most one zero.** (BDP states this in the text and leaves it as Problem 3.7.13; here is why.) In case (23), $u(t) = 0$ means $Ae^{r_1t} = -Be^{r_2t}$. If one of $A$, $B$ is zero, so is the other (exponentials never vanish), and $u \equiv 0$. Otherwise the condition reads $e^{(r_1 - r_2)t} = -B/A$ with $r_1 \ne r_2$, and $e^{(r_1 - r_2)t}$ is strictly monotone, so it takes the value $-B/A$ at most once. In case (24), $u(t) = 0$ means $A + Bt = 0$, which has at most one root unless $A = B = 0$.
>
> **The form (26)** is Proposition §19.2 applied to $A\cos\mu t + B\sin\mu t$; since $|\cos(\mu t - \delta)| \le 1$, $|u| \le Re^{-\gamma t/(2m)}$.

^pf-19-3

*Uses:* [[§13 Homogeneous Differential Equations with Constant Coefficients#^thm-13-2|§13.2]], [[§15 Complex Roots of the Characteristic Equation#^thm-15-2|§15.2]], [[§16 Repeated Roots; Reduction of Order#^thm-16-1|§16.1]] (the three root cases), [[§19 Mechanical and Electrical Vibrations#^prop-19-2|§19.2]]

> [!remark]- Connections
> - PDE version: [[§32 One-Dimensional Wave Equation꞉ Generalities#^ex-32-3|341 Ex. §32.3]] (a string in a resisting medium: each mode satisfies $T'' + kT' + \omega_n^2T = 0$, and the three damping cases occur mode by mode).

> [!definition] Definition §19.4: Underdamped, Critically Damped, Overdamped
> For $mu'' + \gamma u' + ku = 0$:
> - If $\gamma^2 < 4km$ (small damping), the motion (26) is a **damped oscillation** (damped vibration); the system is **underdamped**. The motion is not periodic, but $\mu$ sets how fast the mass oscillates back and forth: $\mu$ is the **quasi-frequency** and $T_d = 2\pi/\mu$ the **quasi-period**, the time between successive maxima (or minima) of $u$, or between successive passages through equilibrium in the same direction.
> - If $\gamma = 2\sqrt{km}$, the motion is **critically damped**.
> - If $\gamma > 2\sqrt{km}$, the motion is **overdamped**.
>
> In the last two cases the mass does not oscillate: it crosses equilibrium at most once (Theorem §19.3) and creeps back to it. Without damping ($\gamma = 0$) the system is **undamped**.
>
> *BDP: 3.7 (text)*

^def-19-4

> [!theorem] Proposition §19.4: Effect of Small Damping on the Frequency
> In the underdamped case,
>
> $$
> \frac{\mu}{\omega_0} = \left(1 - \frac{\gamma^2}{4km}\right)^{1/2} \cong 1 - \frac{\gamma^2}{8km}, \qquad
> \frac{T_d}{T} = \frac{\omega_0}{\mu} = \left(1 - \frac{\gamma^2}{4km}\right)^{-1/2} \cong 1 + \frac{\gamma^2}{8km} , \qquad (27),\ (28)
> $$
>
> the approximations being valid when $\gamma^2/(4km)$ is small. Small damping slightly lowers the frequency and lengthens the (quasi-)period. As $\gamma \to 2\sqrt{km}$, $\mu \to 0$ and $T_d \to \infty$.
>
> *BDP: 3.7, Equations (27) and (28)*

^prop-19-4

> [!proof]+ Proof
> With $\omega_0 = \sqrt{k/m}$ and $\mu = (4km - \gamma^2)^{1/2}/(2m)$,
>
> $$
> \frac{\mu}{\omega_0} = \frac{(4km - \gamma^2)^{1/2}}{2m}\sqrt{\frac{m}{k}} = \left(\frac{4km - \gamma^2}{4km}\right)^{1/2} = \left(1 - \frac{\gamma^2}{4km}\right)^{1/2} ,
> $$
>
> and $T_d/T = (2\pi/\mu)/(2\pi/\omega_0) = \omega_0/\mu$. For small $x$, $(1 - x)^{1/2} \approx 1 - \frac{x}{2}$ and $(1 - x)^{-1/2} \approx 1 + \frac{x}{2}$ (first-order Taylor approximations), which with $x = \gamma^2/(4km)$ give the approximations. As $\gamma^2 \to 4km$, the factor $(1 - \gamma^2/(4km))^{1/2} \to 0$.

^pf-19-4

*Uses:* [[§19 Mechanical and Electrical Vibrations#^thm-19-3|§19.3]], [[§19 Mechanical and Electrical Vibrations#^def-19-3|Def. §19.3]]

So it is not $\gamma$ alone but the dimensionless ratio $\gamma^2/(4km)$ that decides whether damping is small. Small damping barely changes the quasi-frequency, but over long times it can never be neglected: it is what makes the motion die out.

> [!example] Example §19.2: An Underdamped Spring from Data
> **(a)** A 96 lb weight stretches a spring 3.2 ft in equilibrium. It is subject to friction with damping coefficient $\gamma = 18$ lb·s/ft. The weight is initially displaced 6 inches below equilibrium and given a downward velocity of 10 ft/s. Find its displacement for $t \ge 0$.
>
> **Set up** (Remark: Method above). $m = 96/32 = 3$, $k = 96/3.2 = 30$, $\gamma = 18$; $u(0) = \frac12$ ft (6 in, below is positive), $u'(0) = 10$ ft/s. So
>
> $$
> 3u'' + 18u' + 30u = 0, \quad\text{i.e.}\quad u'' + 6u' + 10u = 0 .
> $$
>
> **Solve.** $\gamma^2 - 4km = 324 - 360 < 0$: underdamped. $r^2 + 6r + 10 = (r + 3)^2 + 1 = 0$ gives $r = -3 \pm i$, so $u = e^{-3t}(c_1\cos t + c_2\sin t)$ and
>
> $$
> u' = e^{-3t}\big((-3c_1 + c_2)\cos t + (-c_1 - 3c_2)\sin t\big) .
> $$
>
> Then $u(0) = c_1 = \frac12$ and $u'(0) = -3c_1 + c_2 = 10$, so $c_2 = 10 + \frac32 = \frac{23}{2}$:
>
> $$
> u(t) = e^{-3t}\Big(\frac12\cos t + \frac{23}{2}\sin t\Big) .
> $$
>
> **(b)** The same with a 64 lb weight, stretch 3.2 ft, $\gamma = 12$ lb·s/ft, initial displacement 2 ft below equilibrium and downward velocity 1 ft/s ($g = 32$ ft/s$^2$).
>
> Now $m = 64/32 = 2$, $k = 64/3.2 = 20$: $2u'' + 12u' + 20u = 0$, $u(0) = 2$, $u'(0) = 1$. Again $r^2 + 6r + 10 = 0$, $r = -3 \pm i$. With the same formula for $u'$: $c_1 = 2$ and $-3c_1 + c_2 = 1$, so $c_2 = 7$:
>
> $$
> u(t) = e^{-3t}\big(2\cos t + 7\sin t\big) .
> $$
>
> In both, the quasi-frequency is $\mu = 1$ (while $\omega_0 = \sqrt{10}$): the damping here is far from small, $\gamma^2/(4km) = 0.9$.
>
> *Source: 331 Written HW 4, Problem 1*
> *Source: 331 Final (Fall 2021), Q2*

^ex-19-2

> [!example] Example §19.3: Classifying by the Damping Coefficient
> Consider the spring–mass system $2\dfrac{d^2y}{dt^2} + \gamma\dfrac{dy}{dt} + 5y = 0$ with $0 \le \gamma < \infty$. Classify it (undamped, underdamped, critically damped, overdamped) according to $\gamma$, and find the values of $\gamma$ at which the type changes (the **bifurcation values**).
>
> Here $m = 2$, $k = 5$, and the roots of $2r^2 + \gamma r + 5 = 0$ are
>
> $$
> r = \frac{-\gamma \pm \sqrt{\gamma^2 - 40}}{4} .
> $$
>
> By Theorem §19.3 and Definition §19.4, with $4km = 40$ and $2\sqrt{km} = \sqrt{40} = 2\sqrt{10} \approx 6.32$:
> - $\gamma = 0$: **undamped**, $y = A\cos\big(\sqrt{5/2}\,t\big) + B\sin\big(\sqrt{5/2}\,t\big)$;
> - $0 < \gamma < 2\sqrt{10}$: **underdamped**, complex roots with real part $-\gamma/4 < 0$;
> - $\gamma = 2\sqrt{10}$: **critically damped**, double root $r = -\sqrt{10}/2$;
> - $\gamma > 2\sqrt{10}$: **overdamped**, two distinct negative roots.
>
> The type changes at $\gamma = 2\sqrt{10}$ (oscillating to non-oscillating) and at $\gamma = 0$ (undamped, where the amplitude is constant, to underdamped). The figure shows one solution of each type, all with $y(0) = 1$, $y'(0) = 0$.
>
> *Source: 331 Written HW 4, Problem 2*

^ex-19-3

![[m331-19-1.svg]]
*Example §19.3 with $y(0) = 1$, $y'(0) = 0$. Undamped ($\gamma = 0$, dashed): $y = \cos(\sqrt{5/2}\,t)$. Underdamped ($\gamma = 2$): $y = e^{-t/2}(\cos\frac32 t + \frac13\sin\frac32 t)$ oscillates with decaying amplitude. Critically damped ($\gamma = 2\sqrt{10}$): $y = (1 + \frac{\sqrt{10}}{2}t)e^{-\sqrt{10}\,t/2}$, the fastest return without crossing. Overdamped ($\gamma = 12$): $y \approx 1.088e^{-0.450t} - 0.088e^{-5.550t}$, slowed by its root closer to $0$.*

> [!example] Example §19.4: Small Damping
> The motion of a spring–mass system is governed by
>
> $$
> u'' + \frac18 u' + u = 0, \qquad u(0) = 2, \quad u'(0) = 0 , \qquad (29)
> $$
>
> with $u$ in feet and $t$ in seconds. Find $u(t)$, the quasi-frequency and quasi-period, the time at which the mass first passes through equilibrium, and the time $\tau$ such that $|u(t)| < 0.1$ for all $t > \tau$.
>
> **Solution.** $r^2 + \frac18 r + 1 = 0$ gives $r = -\frac{1}{16} \pm i\sqrt{1 - \frac{1}{256}} = -\frac{1}{16} \pm i\frac{\sqrt{255}}{16}$, so
>
> $$
> u = e^{-t/16}\Big(A\cos\frac{\sqrt{255}}{16}t + B\sin\frac{\sqrt{255}}{16}t\Big) .
> $$
>
> $u(0) = A = 2$, and $u'(0) = -\frac{A}{16} + \frac{\sqrt{255}}{16}B = 0$ gives $B = 2/\sqrt{255}$. In the form (26), $R = \sqrt{4 + \frac{4}{255}} = 2\sqrt{\frac{256}{255}} = \frac{32}{\sqrt{255}}$, and $\tan\delta = B/A = 1/\sqrt{255}$ with $\delta$ in the first quadrant ($A, B > 0$), $\delta \approx 0.06254$:
>
> $$
> u = \frac{32}{\sqrt{255}}\,e^{-t/16}\cos\Big(\frac{\sqrt{255}}{16}t - \delta\Big) . \qquad (30)
> $$
>
> **Quasi-frequency and quasi-period:** $\mu = \sqrt{255}/16 \approx 0.998$, $T_d = 2\pi/\mu \approx 6.295$ s, against $\omega_0 = 1$, $T = 2\pi$ without damping. Here $\gamma^2/(4km) = \frac{1}{256}$; equivalently $\gamma = \frac18$ is one-sixteenth of the critical value $2\sqrt{km} = 2$.
>
> **First passage through equilibrium.** The cosine in (30) first vanishes when its argument reaches $\pi/2$ (it starts at $-\delta$, just below $0$): $\frac{\sqrt{255}}{16}t - \delta = \frac{\pi}{2}$, so
>
> $$
> t = \frac{16}{\sqrt{255}}\Big(\frac{\pi}{2} + \delta\Big) \approx 1.637\ \text{s} .
> $$
>
> **The time $\tau$.** The envelope $\frac{32}{\sqrt{255}}e^{-t/16}$ drops below $0.1$ at $t = 16\ln(20.04) \approx 48.0$, so $\tau < 48$; but $|u|$ can be below the envelope at that time. Solving $|u(t)| = 0.1$ numerically for the last crossing gives $\tau \approx 47.5149$ s, where $u$ rises back through $-0.1$ just after its minimum $u \approx -0.1046$ at $t \approx 47.22$; every later extremum is smaller than $0.1$ in absolute value.
>
> Although $\gamma$ is small, the amplitude is reduced rather quickly (figure).
>
> *BDP: Example 3.7.3*

^ex-19-4

![[m331-19-2.svg]]
*Example §19.4: the solution (blue) stays between the envelopes $\pm\frac{32}{\sqrt{255}}e^{-t/16}$ (red, dashed). The undamped motion $u = 2\cos t$ with the same initial data (grey, dashed) rises and falls almost together with it at first, since $\mu \approx 0.998$ is close to $\omega_0 = 1$; the damping shows in the amplitude, not in the frequency.*

## Electric Circuits

> [!definition] Definition §19.5: The Series RLC Circuit
> A series circuit contains a resistance $R$ (ohms, $\Omega$), a capacitance $C$ (farads, F) and an inductance $L$ (henrys, H), all positive constants, and an impressed voltage $E(t)$ (volts, V). The current $I(t)$ (amperes, A) and the charge $Q(t)$ on the capacitor (coulombs, C) are related by
>
> $$
> I = \frac{dQ}{dt} . \qquad (31)
> $$
>
> The voltage drops are $RI$ across the resistor, $Q/C$ across the capacitor and $L\,dI/dt$ across the inductor. **Kirchhoff's second law:** in a closed circuit the impressed voltage equals the sum of the voltage drops in the rest of the circuit. The units are related by 1 volt $=$ 1 ohm·1 ampere $=$ 1 coulomb/1 farad $=$ 1 henry·1 ampere/1 second.
>
> *BDP: 3.7 (text)*

^def-19-5

> [!theorem] Proposition §19.5: The Circuit Equations
> The charge satisfies
>
> $$
> LQ'' + RQ' + \frac1C Q = E(t), \qquad Q(t_0) = Q_0, \quad Q'(t_0) = I(t_0) = I_0 , \qquad (33),\ (34)
> $$
>
> and, if $E$ is differentiable, the current satisfies
>
> $$
> LI'' + RI' + \frac1C I = E'(t), \qquad I(t_0) = I_0, \quad I'(t_0) = I_0' = \frac{E(t_0) - RI_0 - Q_0/C}{L} . \qquad (35)\text{–}(37)
> $$
>
> So the charge on the capacitor and the current at one time determine the charge, and the current, at all times.
>
> *BDP: 3.7, Equations (32)–(37)*

^prop-19-5

> [!proof]+ Proof
> Kirchhoff's law (Definition §19.5) says
>
> $$
> L\frac{dI}{dt} + RI + \frac1C Q = E(t) . \qquad (32)
> $$
>
> Substituting $I = Q'$ from (31) gives (33); the initial current is $Q'(t_0) = I(t_0)$. Differentiating (33) and substituting $Q' = I$ gives $LI'' + RI' + I/C = E'(t)$. Finally, evaluating (32) at $t_0$ and solving for $I'(t_0)$ gives (37), which is determined by the measurable quantities $Q_0$, $I_0$ and $E(t_0)$.

^pf-19-5

*Uses:* [[§19 Mechanical and Electrical Vibrations#^def-19-5|Def. §19.5]]

> [!remark] Remark: One Equation, Two Systems
> The circuit equation (33) and the spring equation (7) are the same initial value problem $ay'' + by' + cy = g(t)$ under the dictionary
>
> | spring–mass | $u$ | $m$ | $\gamma$ | $k$ | $F(t)$ |
> |---|---|---|---|---|---|
> | series circuit | $Q$ | $L$ | $R$ | $1/C$ | $E(t)$ |
>
> so every statement of this section transfers. For instance, $LQ'' + RQ' + Q/C = 0$ is critically damped when $R^2 = 4L/C$, underdamped (the charge oscillates with decaying amplitude) when $R^2 < 4L/C$, and every free solution dies out because $L, R, C > 0$. Once a constant-coefficient equation is solved, its solution can be read in whichever physical setting is of interest.

^rem-19-2
