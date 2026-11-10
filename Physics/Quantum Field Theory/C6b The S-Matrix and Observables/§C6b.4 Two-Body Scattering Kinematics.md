---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.3 The Cross Section]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.5 Decay Widths]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.3 "两体散射运动学", pp. 247–250, eqs. (6.336)–(6.366), Fig. 6.5 (page images checked, PDF pp. 255–258); Exercise 6.7, eq. (6.424) · the user's PHY 513 notes, Ch. 15 §15.7 (Derivation "Two-body phase space in the CM frame", paragraph "The momentum (filled in)", Principle "$2\to2$ differential cross section in the CM frame", Derivation "The equal-mass case", paragraph "Why $1/E_{\rm cm}^2$") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part C, slides 20–21, 25, and transcript; Lecture 16, slide 19 · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 106–108, eqs. (4.81)–(4.85).*

Two particles in, two out: the simplest final state, and the one the course works out (Lecture 15, Part C, slides 20–21). The cross section of [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]] needs the phase space $d\Pi_2$ explicitly ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]). In the centre-of-mass frame ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]) energy and momentum conservation fix both final energies and the common momentum, written with the Källén function ([[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]), and the phase space reduces to an integral over the direction of one final particle ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]). The results: the $2 \to 2$ differential cross section in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]), its integral and the azimuthal symmetry ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-5|Theorem §C6b.4.5]]), the factor for two identical final particles read as half the sphere ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]]), and the special cases of equal masses in pairs ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]]) and of all masses equal ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-8|Theorem §C6b.4.8]]). Yu §6.5.3, eqs. (6.336)–(6.366), is followed; the same formulas with $E_{\rm cm} \to m_A$ give the two-body decays of [[§C6b.6 Decay Kinematics|§C6b.6]].

**Setup.** Kinematics only: a $2 \to 2$ process $A + B \to 1 + 2$ with on-shell momenta, $p_A + p_B = p_1 + p_2$, and an amplitude $\mathcal M$ supplied from outside (the Feynman rules, [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]). The cross section is the main-line formula of [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]] (box route, [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] with [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]) or, equivalently, the wave-packet formula of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]; both are evaluated in the centre-of-mass frame, beams along $z$, $\mathbf p_B = -\mathbf p_A$. The kinematic formulas are exact; the cross sections inherit the range of validity of $\mathcal M$ (exact if the interaction switches off, lowest order for a permanent interaction: [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]).

*Conventions* ([[Larsen PHY 513]]): collinear beams along $z$; $E_{\rm cm}$ the total energy in the centre-of-mass frame ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]; "c.m.s." on the slides, $E_{\rm CM}$ in Yu); $p_1 \equiv |\mathbf p_1|$; $\theta$ the scattering angle between $\mathbf p_A$ and $\mathbf p_1$ (Yu Fig. 6.5); Yu writes $\lambda^{1/2}(1, m_1^2/E_{\rm CM}^2, m_2^2/E_{\rm CM}^2)$ with dimensionless arguments, these notes mostly $\lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2) = E_{\rm cm}^2\lambda^{1/2}(1, \dots)$.

## Two-body phase space in the centre-of-mass frame

> [!remark] Remark: You must commit
> To make $d\Pi_n$ explicit one must commit to a coordinate system, a number of final particles and the quantities actually observed. With three or four particles in the final state the kinematics is harder, but there is also more data, more quantities that can be measured: correlations and angles, so the theory predicts more. Lecture 15 treats only the simplest case; in practice such kinematics is not worked out every time but looked up.
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7*

^rem-c6b-4-1

> [!definition] Definition §C6b.4.1: The Källén Function
> The **Källén function** is the polynomial
>
> $$
> \lambda(x, y, z) \equiv x^2 + y^2 + z^2 - 2xy - 2xz - 2yz = (x - y - z)^2 - 4yz ,
> $$
>
> symmetric in $x$, $y$, $z$. In two-body kinematics it is evaluated at $x = E_{\rm cm}^2$ and the two squared masses ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]).
>
> *Model:* none (algebra); *applies:* any real arguments.
>
> *Source: Yu §6.5.3, eq. (6.351) (page image checked, boxed; "称为 Källén 函数。$\lambda(x, y, z)$ 关于 $x, y, z$ 对称，是 Gunnar Källén 在其教科书《Elementary Particle Physics》(1964) 中引入的") · the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "The momentum (filled in)")*

^def-c6b-4-1

> [!theorem] Theorem §C6b.4.1: Two-Body Phase Space in the Centre-of-Mass Frame
> For $n = 2$ final particles in the centre-of-mass frame, $P = (E_{\rm cm}, \mathbf 0)$,
>
> $$
> \int d\Pi_2\;F = \int d\Omega\;\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\;F ,
> $$
>
> where $\Omega$ is the direction of $\mathbf p_1$, $\mathbf p_2 = -\mathbf p_1$, and $|\mathbf p_1|$ is fixed by $E_1 + E_2 = E_{\rm cm}$ with $E_1 = \sqrt{p_1^2 + m_1^2}$, $E_2 = \sqrt{p_1^2 + m_2^2}$.
>
> *Model:* any (kinematics); *applies:* two final particles, centre-of-mass frame; independent of the dynamics.
>
> *Source: PHY 513 Lecture 15, slide 20 ("Explicit expression for $n = 2$ final particles in cms: … $= \int d\Omega\frac{|\vec p_1|}{16\pi^2E_{\rm cm}}$"), and transcript · the user's PHY 513 notes, Ch. 15 §15.7, Derivation "Two-body phase space in the CM frame", eq. (dPi2) · PS §4.5, eqs. (4.81)–(4.82) · Yu §6.5.3, eqs. (6.341)–(6.343)*

^thm-c6b-4-1

> [!derivation]- Derivation
> **Step 1** (the spatial delta). With $P = (E_{\rm cm}, \mathbf 0)$, split by components,
>
> $$
> \delta^4(P - p_1 - p_2) = \delta(E_{\rm cm} - E_1 - E_2)\,\delta^3(\mathbf 0 - \mathbf p_1 - \mathbf p_2) = \delta(E_1 + E_2 - E_{\rm cm})\,\delta^3(\mathbf p_2 + \mathbf p_1) ,
> $$
>
> and use the $\delta^3$ to do the $\mathbf p_2$ integral: $\mathbf p_2 = -\mathbf p_1$, so $E_2 = \sqrt{|-\mathbf p_1|^2 + m_2^2} = \sqrt{p_1^2 + m_2^2}$ ("$\delta$-fct set $\vec p_1 + \vec p_2 = 0$ in c.m.s.", slide 20). The factors of $2\pi$: $(2\pi)^4/(2\pi)^6 = (2\pi)^{-2}$, written as $(2\pi)^{-3}\cdot2\pi$:
>
> $$
> \int\frac{d^3p_1}{(2\pi)^3}\frac{1}{2E_1}\frac{d^3p_2}{(2\pi)^3}\frac{1}{2E_2}(2\pi)^4\delta^4(\dots)\,F = \int\frac{d^3p_1}{(2\pi)^3}\frac{1}{2E_12E_2}\cdot2\pi\,\delta(E_1 + E_2 - E_{\rm cm})\,F\Big|_{\mathbf p_2 = -\mathbf p_1} .
> $$
>
> **Step 2** (spherical coordinates). $d^3p_1 = p_1^2\,dp_1\,d\Omega$:
>
> $$
> = \int\frac{d\Omega}{(2\pi)^2}\int_0^\infty dp_1\,\frac{p_1^2}{4E_1E_2}\,\delta(E_1 + E_2 - E_{\rm cm})\,F ,
> $$
>
> with $\frac{(2\pi)^{-3}\cdot2\pi}{2E_1\,2E_2} = \frac{1}{(2\pi)^2\,4E_1E_2}$.
>
> **Step 3** (the energy delta). $E_1 + E_2 - E_{\rm cm}$ is a function of $p_1$ with derivative
>
> $$
> \partial_{p_1}(E_1 + E_2 - E_{\rm cm}) = \frac{p_1}{E_1} + \frac{p_1}{E_2} = \frac{p_1(E_1 + E_2)}{E_1E_2} > 0 ,
> $$
>
> so it has at most one zero $p_1^\ast$, and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2 gives
>
> $$
> \delta(E_1 + E_2 - E_{\rm cm}) = \frac{\delta(p_1 - p_1^\ast)}{|\partial_{p_1}(E_1 + E_2)|_{p_1^\ast}} = \frac{E_1E_2}{p_1(E_1 + E_2)}\bigg|_{p_1^\ast}\,\delta(p_1 - p_1^\ast) .
> $$
>
> (The plus sign, where the longitudinal Jacobian of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] has a minus, is because $\mathbf p_2 = -\mathbf p_1$: $E_2$ also grows with $p_1$. The sign is still a minus as long as $p_2$ is treated as independent; it becomes a plus once $p_2$ is eliminated in favour of $p_1$.)
>
> **Step 4** (collect). Insert Step 3 into Step 2 and do the $p_1$ integral; with $(2\pi)^2\cdot4 = 16\pi^2$ and $E_1 + E_2 = E_{\rm cm}$ at the zero,
>
> $$
> \int d\Pi_2\,F = \int d\Omega\;\frac{1}{(2\pi)^2}\,\frac{p_1^2}{4E_1E_2}\,\frac{E_1E_2}{p_1(E_1 + E_2)}\,F\bigg|_{p_1^\ast} = \int d\Omega\;\frac{p_1}{16\pi^2(E_1 + E_2)}\,F\bigg|_{p_1^\ast} = \int d\Omega\;\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\,F .
> $$
>
> **What the derivation shows.**
> - Two of the six final momentum components remain, the direction $\Omega$ of $\mathbf p_1$; the particles come out "back to back".
> - The zero exists only if $E_{\rm cm} > m_1 + m_2$ (Yu eq. (6.339)): at $p_1 = 0$ the sum $E_1 + E_2$ is $m_1 + m_2$, and it increases with $p_1$ → [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]].
> - Checked by smearing the energy delta function in `qft-C/tools/l15/checks.py` ($E_{\rm cm} = 5$, $m_1 = 1.2$, $m_2 = 0.7$).

^der-c6b-4-1

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!theorem] Theorem §C6b.4.2: The Centre-of-Mass Momentum
> In the setting of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], with the Källén function $\lambda$ of [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]:
> 1. (final state)
>
> $$
> |\mathbf p_1| = |\mathbf p_2| = \frac{\sqrt{\bigl[E_{\rm cm}^2 - (m_1 + m_2)^2\bigr]\bigl[E_{\rm cm}^2 - (m_1 - m_2)^2\bigr]}}{2E_{\rm cm}} = \frac{\lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2)}{2E_{\rm cm}} = \frac{E_{\rm cm}}{2}\,\lambda^{1/2}\Bigl(1, \frac{m_1^2}{E_{\rm cm}^2}, \frac{m_2^2}{E_{\rm cm}^2}\Bigr) ,
> $$
>
> $$
> E_1 = \frac{E_{\rm cm}^2 + m_1^2 - m_2^2}{2E_{\rm cm}} , \qquad E_2 = \frac{E_{\rm cm}^2 + m_2^2 - m_1^2}{2E_{\rm cm}} :
> $$
>
> the heavier particle takes the larger share of the energy, $E_1 - E_2 = (m_1^2 - m_2^2)/E_{\rm cm}$.
> 2. (initial state) The same with $A$, $B$ in place of 1, 2: $E_A = \frac{E_{\rm cm}^2 + m_A^2 - m_B^2}{2E_{\rm cm}}$, $E_B = \frac{E_{\rm cm}^2 + m_B^2 - m_A^2}{2E_{\rm cm}}$, $|\mathbf p_A| = |\mathbf p_B| = \frac{\lambda^{1/2}(E_{\rm cm}^2, m_A^2, m_B^2)}{2E_{\rm cm}}$.
> 3. The formulas of part 1 solve $E_1 + E_2 = E_{\rm cm}$ with $E_1, E_2 > 0$ and $|\mathbf p_1| \ge 0$ exactly for $E_{\rm cm} \ge m_1 + m_2$, the threshold of [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]]. For $E_{\rm cm} \le |m_1 - m_2|$ the square root is real as well (both brackets are negative), but one of the energies of part 1 is negative: a root of the squared equation only.
>
> *Model:* any (kinematics); *applies:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]; part 2 in the centre-of-mass frame of the initial pair.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "The momentum (filled in)") · Yu §6.5.3, eqs. (6.346)–(6.352), (6.354)–(6.355) (page image checked; after (6.349): "质量较大的末态粒子在质心系中分得的能量较多")*

^thm-c6b-4-2

> [!derivation]- Derivation
> **Step 1** ($E_1$). From $E_1 + E_2 = E_{\rm cm}$ and $E_j^2 = p_1^2 + m_j^2$ (so $E_2^2 = E_1^2 - m_1^2 + m_2^2$), square $E_2 = E_{\rm cm} - E_1$ (Yu eqs. (6.346)–(6.348)):
>
> $$
> E_{\rm cm}^2 - 2E_{\rm cm}E_1 + E_1^2 = E_1^2 - m_1^2 + m_2^2 \quad\Rightarrow\quad 2E_{\rm cm}E_1 = E_{\rm cm}^2 + m_1^2 - m_2^2 \quad\Rightarrow\quad E_1 = \frac{E_{\rm cm}^2 + m_1^2 - m_2^2}{2E_{\rm cm}} .
> $$
>
> **Step 2** ($p_1^2$ as a difference of squares). Insert Step 1 into $p_1^2 = E_1^2 - m_1^2$ and factor $a^2 - b^2 = (a - b)(a + b)$ with $a = E_{\rm cm}^2 + m_1^2 - m_2^2$, $b = 2E_{\rm cm}m_1$:
>
> $$
> p_1^2 = \frac{(E_{\rm cm}^2 + m_1^2 - m_2^2)^2 - 4E_{\rm cm}^2m_1^2}{4E_{\rm cm}^2} = \frac{(E_{\rm cm}^2 - 2E_{\rm cm}m_1 + m_1^2 - m_2^2)(E_{\rm cm}^2 + 2E_{\rm cm}m_1 + m_1^2 - m_2^2)}{4E_{\rm cm}^2} = \frac{\bigl[(E_{\rm cm} - m_1)^2 - m_2^2\bigr]\bigl[(E_{\rm cm} + m_1)^2 - m_2^2\bigr]}{4E_{\rm cm}^2} .
> $$
>
> **Step 3** (regroup). Factor each bracket again and pair the first factor with the fourth, the second with the third:
>
> $$
> \begin{aligned}
> \bigl[(E_{\rm cm} - m_1)^2 - m_2^2\bigr]\bigl[(E_{\rm cm} + m_1)^2 - m_2^2\bigr] &= (E_{\rm cm} - m_1 - m_2)(E_{\rm cm} - m_1 + m_2)(E_{\rm cm} + m_1 - m_2)(E_{\rm cm} + m_1 + m_2)\\
> &= \bigl[(E_{\rm cm} - m_1 - m_2)(E_{\rm cm} + m_1 + m_2)\bigr]\bigl[(E_{\rm cm} - m_1 + m_2)(E_{\rm cm} + m_1 - m_2)\bigr]\\
> &= \bigl[E_{\rm cm}^2 - (m_1 + m_2)^2\bigr]\bigl[E_{\rm cm}^2 - (m_1 - m_2)^2\bigr] .
> \end{aligned}
> $$
>
> Taking the square root of Step 2 ($p_1 \ge 0$) gives the first form of the statement.
>
> **Step 4** (Källén). With $x = E_{\rm cm}^2$, expand the product and compare with $\lambda(x, y, z) = x^2 - 2x(y + z) + (y - z)^2$ at $y = m_1^2$, $z = m_2^2$ (Yu eqs. (6.350)–(6.351)):
>
> $$
> \bigl[x - (m_1 + m_2)^2\bigr]\bigl[x - (m_1 - m_2)^2\bigr] = x^2 - x\bigl[(m_1 + m_2)^2 + (m_1 - m_2)^2\bigr] + \bigl[(m_1 + m_2)(m_1 - m_2)\bigr]^2 = x^2 - 2x(m_1^2 + m_2^2) + (m_1^2 - m_2^2)^2 = \lambda(x, m_1^2, m_2^2) ,
> $$
>
> where $x^2 + y^2 + z^2 - 2xy - 2xz - 2yz = x^2 - 2x(y + z) + (y - z)^2$.
>
> **Step 5** (dimensionless form). Every term of $\lambda$ has degree 2, so $\lambda(E^2x, E^2y, E^2z) = E^4\lambda(x, y, z)$; with $E = E_{\rm cm}$, $\lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2)/(2E_{\rm cm}) = \frac{E_{\rm cm}}{2}\lambda^{1/2}(1, m_1^2/E_{\rm cm}^2, m_2^2/E_{\rm cm}^2)$ (Yu (6.352)).
>
> **Step 6** ($E_2$ and the share). Step 1 with the labels 1, 2 exchanged (the equations $E_1 + E_2 = E_{\rm cm}$, $E_j^2 = p_1^2 + m_j^2$ are symmetric) gives $E_2 = \frac{E_{\rm cm}^2 + m_2^2 - m_1^2}{2E_{\rm cm}}$ (Yu (6.349)); subtracting, $E_1 - E_2 = \frac{2(m_1^2 - m_2^2)}{2E_{\rm cm}}$, positive exactly when $m_1 > m_2$.
>
> **Step 7** (initial state; part 2). In the centre-of-mass frame $\mathbf p_B = -\mathbf p_A$ and $E_A + E_B = E_{\rm cm}$: the same two equations with $(m_A, m_B)$ for $(m_1, m_2)$, so Steps 1–6 give part 2 (Yu (6.354)–(6.355)).
>
> **Step 8** (when the root is a solution; part 3). Step 1 squared $E_2 = E_{\rm cm} - E_1$, so its result solves the original equation only if $E_2 = E_{\rm cm} - E_1 \ge 0$, and by symmetry $E_1 \ge 0$, together with $p_1^2 \ge 0$. By Step 3, $p_1^2 \ge 0$ if and only if the two brackets have the same sign: $E_{\rm cm} \ge m_1 + m_2$ (both $\ge 0$) or $E_{\rm cm} \le |m_1 - m_2|$ (both $\le 0$). In the second case, with $m_1 \ge m_2$, part 1 gives $2E_{\rm cm}E_2 = E_{\rm cm}^2 - (m_1^2 - m_2^2) \le (m_1 - m_2)^2 - (m_1 - m_2)(m_1 + m_2) = -2m_2(m_1 - m_2) \le 0$: no solution with positive energies (for example $m_1 = 3$, $m_2 = 1$, $E_{\rm cm} = 1$: $|\mathbf p_1| = \sqrt{45}/2$ but $E_2 = -\frac72$). In the first case $E_{\rm cm}^2 \ge (m_1 + m_2)^2 > |m_1^2 - m_2^2|$, so both energies of part 1 are positive.
>
> **What the derivation shows.**
> - $|\mathbf p_1|$ and both energies are physical exactly above threshold, $E_{\rm cm} \ge m_1 + m_2$ (part 3; [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]]): Step 1 squares $E_2 = E_{\rm cm} - E_1$, which keeps roots with $E_{\rm cm} - E_1 < 0$; for $E_{\rm cm} \le |m_1 - m_2|$ the lighter particle would have the energy $(E_{\rm cm}^2 - |m_1^2 - m_2^2|)/2E_{\rm cm} \le 0$, and between $|m_1 - m_2|$ and $m_1 + m_2$ the radicand is negative. The monotonicity argument of [[§C6b.4 Two-Body Scattering Kinematics#^der-c6b-4-1|Derivation §C6b.4.1]] ("What the derivation shows") gives the same threshold without squaring. The heavier particle takes the larger share of the energy (Yu after eq. (6.349); part 1).

^der-c6b-4-2

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]

> [!theorem]- ★ Theorem §C6b.4.3: The Centre-of-Mass Flux Factor via λ
> In the centre-of-mass frame the flux factor of [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], 2, is
>
> $$
> E_AE_B|\mathbf v_A - \mathbf v_B| = E_{\rm cm}|\mathbf p_A| = \frac12\lambda^{1/2}(E_{\rm cm}^2, m_A^2, m_B^2) = \frac{E_{\rm cm}^2}{2}\,\lambda^{1/2}\Bigl(1, \frac{m_A^2}{E_{\rm cm}^2}, \frac{m_B^2}{E_{\rm cm}^2}\Bigr) ,
> $$
>
> with $\lambda$ of [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]; it agrees with the invariant form $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ of [[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]].
>
> *Model:* any (kinematics); *applies:* centre-of-mass frame, any masses.
>
> *Source: Yu, Exercise 6.7, eq. (6.424) (page image checked; an exercise, worked here)*

^thm-c6b-4-3

> [!derivation]- Derivation
> **Step 1** (velocities in the centre-of-mass frame). $\mathbf p_B = -\mathbf p_A$, so $\mathbf v_A = \mathbf p_A/E_A$ and $\mathbf v_B = -\mathbf p_A/E_B$ point in opposite directions, and with $E_A + E_B = E_{\rm cm}$
>
> $$
> |\mathbf v_A - \mathbf v_B| = |\mathbf p_A|\Bigl(\frac{1}{E_A} + \frac{1}{E_B}\Bigr) = |\mathbf p_A|\,\frac{E_A + E_B}{E_AE_B} = \frac{|\mathbf p_A|\,E_{\rm cm}}{E_AE_B} .
> $$
>
> **Step 2** (multiply). $E_AE_B|\mathbf v_A - \mathbf v_B| = E_{\rm cm}|\mathbf p_A|$.
>
> **Step 3** (insert $|\mathbf p_A|$). By [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], 2, $|\mathbf p_A| = \lambda^{1/2}(E_{\rm cm}^2, m_A^2, m_B^2)/(2E_{\rm cm})$, so $E_{\rm cm}|\mathbf p_A| = \frac12\lambda^{1/2}(E_{\rm cm}^2, m_A^2, m_B^2)$; homogeneity, $\lambda(E^2x, E^2y, E^2z) = E^4\lambda(x, y, z)$ (every term of [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]] is of degree 2), gives the last form.
>
> **Step 4** (check against the invariant form). With $s = E_{\rm cm}^2 = (p_A + p_B)^2 = m_A^2 + m_B^2 + 2p_A\cdot p_B$, $p_A\cdot p_B = (s - m_A^2 - m_B^2)/2$ and
>
> $$
> (p_A\cdot p_B)^2 - m_A^2m_B^2 = \frac{(s - m_A^2 - m_B^2)^2 - 4m_A^2m_B^2}{4} = \frac{\lambda(s, m_A^2, m_B^2)}{4} ,
> $$
>
> by the second form of [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]: the square root is $\frac12\lambda^{1/2}(s, m_A^2, m_B^2)$, the same.
>
> **What the derivation shows.**
> - In the centre-of-mass frame the flux factor is the total energy times the common momentum; Step 4 is the frame-free version, valid for collinear beams in any frame along the axis ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], 1).

^der-c6b-4-3

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]]

## 2 → 2 scattering in the centre-of-mass frame

> [!theorem] Theorem §C6b.4.4: The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
> For $A + B \to 1 + 2$ in the centre-of-mass frame, with $\Omega$ the direction of $\mathbf p_1$:
> 1. with $|\mathbf p_1|$ of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]],
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\cdot\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\cdot|\mathcal M|^2 ;
> $$
>
> 2. with the $\lambda$ form of $|\mathbf p_1|$,
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{128\pi^2E_AE_B|\mathbf v_A - \mathbf v_B|}\,\lambda^{1/2}\Bigl(1, \frac{m_1^2}{E_{\rm cm}^2}, \frac{m_2^2}{E_{\rm cm}^2}\Bigr)\,|\mathcal M|^2 .
> $$
>
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] with [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] (or [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]); *applies:* as there; $\mathcal M$ from free states and the Feynman rules is exact in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] and lowest order in [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]].
>
> *Source: PHY 513 Lecture 15, slide 21 (boxed formula) · the user's PHY 513 notes, Ch. 15 §15.7, Principle "$2\to2$ differential cross section in the CM frame", eq. (dsdOgen) (a derived result: a theorem here) · PS §4.5, eq. (4.84) · Yu §6.5.3, eqs. (6.345), (6.353) (page image checked; (6.353) boxed)*

^thm-c6b-4-4

> [!derivation]- Derivation
> **Step 1** (insert the phase space). By [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], 2 (equivalently [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]) and [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2\,d\Pi_2$. For a smooth acceptance $g$ of the final states, [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]] with $F = |\mathcal M|^2g$ gives
>
> $$
> \int g\,d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\int d\Pi_2\,|\mathcal M|^2g = \int d\Omega\;g(\Omega)\;\frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\,|\mathcal M(\Omega)|^2 ,
> $$
>
> with $\mathcal M$ evaluated at $\mathbf p_2 = -\mathbf p_1$ and the $|\mathbf p_1|$ of the energy constraint; it depends on $\Omega$.
>
> **Step 2** (read off). The initial-state factor does not depend on $\Omega$; what multiplies $g(\Omega)\,d\Omega$ under the integral is $(d\sigma/d\Omega)_{\rm cm}$, part 1.
>
> **Step 3** (the $\lambda$ form; part 2). Insert $|\mathbf p_1| = \frac{E_{\rm cm}}{2}\lambda^{1/2}(1, m_1^2/E_{\rm cm}^2, m_2^2/E_{\rm cm}^2)$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], 1): $\frac{1}{4E_AE_B|\mathbf v_A - \mathbf v_B|}\cdot\frac{E_{\rm cm}\lambda^{1/2}}{2\cdot16\pi^2E_{\rm cm}} = \frac{\lambda^{1/2}}{128\pi^2E_AE_B|\mathbf v_A - \mathbf v_B|}$ (Yu (6.353)).
>
> **What the derivation shows.**
> - The initial-state factor has not been simplified; it may allow simplifications of its own. For unequal masses the kinematics of the particular situation must be worked out (or looked up) → the $\lambda$ form (part 2), ★ [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-3|Theorem §C6b.4.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]].

^der-c6b-4-4

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]

> [!theorem] Theorem §C6b.4.5: The Total 2 → 2 Cross Section; Azimuthal Symmetry
> Let $\Omega = (\theta, \varphi)$ be the direction of $\mathbf p_1$ in the centre-of-mass frame, with polar axis along $\mathbf p_A$ ($\theta$ the scattering angle), $d\Omega = \sin\theta\,d\theta\,d\varphi$, $\theta \in [0, \pi]$, $\varphi \in [0, 2\pi)$.
> 1. $\displaystyle\sigma = \frac{1}{S_{\rm id}}\int d\Omega\,\Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm}$, with $(d\sigma/d\Omega)_{\rm cm}$ of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]] and $S_{\rm id}$ of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]].
> 2. If $|\mathcal M|^2$ does not depend on $\varphi$ (rotational symmetry about the beam axis; for spinless particles always, since $|\mathcal M|^2$ is a function of $s$ and $t$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]) and $t$ depends on $\theta$ only),
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\,\frac{1}{64\pi E_AE_B|\mathbf v_A - \mathbf v_B|}\,\lambda^{1/2}\Bigl(1, \frac{m_1^2}{E_{\rm cm}^2}, \frac{m_2^2}{E_{\rm cm}^2}\Bigr)\int_0^\pi d\theta\,\sin\theta\,|\mathcal M(\theta)|^2 .
> $$
>
> 3. If $|\mathcal M|^2$ is constant, $\sigma = \frac{4\pi}{S_{\rm id}}\bigl(\frac{d\sigma}{d\Omega}\bigr)_{\rm cm}$.
>
> *Model:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]; *applies:* as there; part 2 for azimuthally symmetric $|\mathcal M|^2$.
>
> *Source: Yu §6.5.3, eqs. (6.342), (6.344), (6.356)–(6.357) (page image checked) · PHY 513 Lecture 16, slide 19 ($\sigma_{\rm tot} = \lambda^2/(32\pi E_{\rm cm}^2)$, "note: identical particles")*

^thm-c6b-4-5

> [!derivation]- Derivation
> **Step 1** (part 1). [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], 1: $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$, and in the centre-of-mass frame $d\sigma = (d\sigma/d\Omega)_{\rm cm}\,d\Omega$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]).
>
> **Step 2** ($\varphi$-independence for spinless particles). In the centre-of-mass frame, with $\theta$ the angle between $\mathbf p_A$ and $\mathbf p_1$,
>
> $$
> t = (p_A - p_1)^2 = m_A^2 + m_1^2 - 2(E_AE_1 - |\mathbf p_A||\mathbf p_1|\cos\theta) ,
> $$
>
> where $E_A$, $E_1$, $|\mathbf p_A|$, $|\mathbf p_1|$ are fixed by $E_{\rm cm}$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]); so $t$ depends on $\theta$ alone, and so does $|\mathcal M|^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]).
>
> **Step 3** (the $\varphi$ integral). For $|\mathcal M|^2 = |\mathcal M(\theta)|^2$ (Yu (6.356)):
>
> $$
> \int d\Omega\,|\mathcal M(\theta)|^2 = \int_0^{2\pi}d\varphi\int_0^\pi d\theta\,\sin\theta\,|\mathcal M(\theta)|^2 = 2\pi\int_0^\pi d\theta\,\sin\theta\,|\mathcal M(\theta)|^2 .
> $$
>
> **Step 4** (part 2). Insert into part 1 with the $\lambda$ form of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], 2: $\frac{2\pi}{128\pi^2} = \frac{1}{64\pi}$ (Yu (6.357)).
>
> **Step 5** (part 3). For constant $|\mathcal M|^2$ the integrand of part 1 is constant and $\int d\Omega = 4\pi$.
>
> **What the derivation shows.**
> - Only the polar integral is left for an azimuthally symmetric process; it carries all the angular information of $|\mathcal M|^2$.

^der-c6b-4-5

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]

> [!theorem] Theorem §C6b.4.6: Two Identical Final Particles: Half the Sphere
> If the two final particles of a $2 \to 2$ process are identical, then in the centre-of-mass frame the directions $(\theta, \varphi)$ and $(\pi - \theta, \varphi + \pi)$ of $\mathbf p_1$ describe the same final state, $(d\sigma/d\Omega)_{\rm cm}$ takes the same value at both, and
>
> $$
> \sigma = \frac12\int_{4\pi}d\Omega\,\Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \int_{\theta < \pi/2}d\Omega\,\Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} :
> $$
>
> the factor $1/S_{\rm id} = 1/2$ of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-5|Theorem §C6b.4.5]], 1, is the same as integrating over half the sphere.
>
> *Model:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]; *applies:* two identical final particles, centre-of-mass frame; every order.
>
> *Source: Yu §6.5.3, after eq. (6.358) ("如果末态 2 个粒子是全同的，那么末态对称性因子 $\mathcal S = 2$") · PS §4.5, p. 108 · PHY 513 Lecture 16, slide 19 ("note: identical particles")*

^thm-c6b-4-6

> [!derivation]- Derivation
> **Step 1** (opposite directions). With $\hat{\mathbf n}(\theta, \varphi) = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, $\sin(\pi - \theta) = \sin\theta$, $\cos(\pi - \theta) = -\cos\theta$, $\cos(\varphi + \pi) = -\cos\varphi$, $\sin(\varphi + \pi) = -\sin\varphi$:
>
> $$
> \hat{\mathbf n}(\pi - \theta, \varphi + \pi) = (-\sin\theta\cos\varphi, -\sin\theta\sin\varphi, -\cos\theta) = -\hat{\mathbf n}(\theta, \varphi) .
> $$
>
> **Step 2** (one state). In the centre-of-mass frame $\mathbf p_2 = -\mathbf p_1$. For $\mathbf p_1 = p\,\hat{\mathbf n}(\theta, \varphi)$ the final state is $|p\hat{\mathbf n}, -p\hat{\mathbf n}\rangle$; for $\mathbf p_1 = p\,\hat{\mathbf n}(\pi - \theta, \varphi + \pi) = -p\hat{\mathbf n}$ it is $|-p\hat{\mathbf n}, p\hat{\mathbf n}\rangle$. For identical particles the creation operators commute ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], 1), so the two kets are equal, and so are the amplitudes and $(d\sigma/d\Omega)_{\rm cm}$ at the two points.
>
> **Step 3** (the two hemispheres). The map $(\theta, \varphi) \mapsto (\theta', \varphi') = (\pi - \theta, \varphi + \pi)$ sends $\theta < \pi/2$ to $\theta' > \pi/2$, with $|d\theta'/d\theta| = 1$, $d\varphi' = d\varphi$ and $\sin\theta' = \sin\theta$, so $d\Omega' = d\Omega$. With Step 2,
>
> $$
> \int_{4\pi}d\Omega\,\frac{d\sigma}{d\Omega} = \int_{\theta < \pi/2}d\Omega\,\frac{d\sigma}{d\Omega} + \int_{\theta' > \pi/2}d\Omega'\,\frac{d\sigma}{d\Omega'} = 2\int_{\theta < \pi/2}d\Omega\,\frac{d\sigma}{d\Omega} .
> $$
>
> Multiplying by $1/S_{\rm id} = 1/2$ gives the statement.
>
> **What the derivation shows.**
> - Integrating over the full sphere counts each state twice; the $\frac12$ is a counting of states, not a property of the amplitude ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]; [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]).

^der-c6b-4-6

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-5|Theorem §C6b.4.5]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]

> [!theorem] Theorem §C6b.4.7: Equal Masses in Pairs
> Let $m_A = m_B = m_i$ and $m_1 = m_2 = m_f$, and in the centre-of-mass frame let
>
> $$
> \beta_i \equiv \sqrt{1 - \frac{4m_i^2}{E_{\rm cm}^2}} = \frac{|\mathbf p_A|}{E_A} , \qquad \beta_f \equiv \sqrt{1 - \frac{4m_f^2}{E_{\rm cm}^2}} = \frac{|\mathbf p_1|}{E_1} ,
> $$
>
> the speeds of each initial and each final particle. Then
> 1. $E_A = E_B = E_1 = E_2 = E_{\rm cm}/2$, and $\lambda^{1/2}(1, m^2/E_{\rm cm}^2, m^2/E_{\rm cm}^2) = \sqrt{1 - 4m^2/E_{\rm cm}^2}$ for equal arguments ([[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]);
> 2. $|\mathbf p_A| = |\mathbf p_B| = E_{\rm cm}\beta_i/2$, $|\mathbf p_1| = |\mathbf p_2| = E_{\rm cm}\beta_f/2$;
> 3. $|\mathbf v_A - \mathbf v_B| = 2\beta_i$, the flux factor is $E_AE_B|\mathbf v_A - \mathbf v_B| = E_{\rm cm}^2\beta_i/2$, and
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{\beta_f\,|\mathcal M|^2}{64\pi^2E_{\rm cm}^2\,\beta_i} ;
> $$
>
> 4. if the two final particles are identical, $S_{\rm id} = 2$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]]); otherwise $S_{\rm id} = 1$;
> 5. the momentum transfers are spacelike or zero: with $t = (p_A - p_1)^2$, $u = (p_A - p_2)^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]),
>
> $$
> t = -|\mathbf p_A - \mathbf p_1|^2 \le 0 , \qquad u = -|\mathbf p_A - \mathbf p_2|^2 \le 0 ,
> $$
>
> a Lorentz-invariant statement, true in every frame although read off in the centre-of-mass frame, and true for $m_i \ne m_f$. Hence a particle of mass $m_3 > 0$ exchanged in the $t$- or $u$-channel has $t - m_3^2 \le -m_3^2 < 0$, $u - m_3^2 < 0$: its propagator never goes on shell in the physical region, and the $i\varepsilon$ may be dropped ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-3|Example §C6c.6.3]]).
>
> *Model:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]; *applies:* as there, masses equal in pairs; part 5 is kinematics only, any theory.
>
> *Source: Yu §6.5.3, eqs. (6.358)–(6.365) (page image checked) · PHY 513, Problem Set 9, Problem 3(b)–(c) (the user's solution: "in the center of mass frame both $\phi_1$'s and both $\phi_2$'s have energy $E_{\text{cms}}/2$ … $(p_A - p_{1,2})^2 = -|\mathbf p_A - \mathbf p_{1,2}|^2 \le 0$, a Lorentz-invariant statement"; taught through the problem set, hence unstarred)*

^thm-c6b-4-7

> [!derivation]- Derivation
> **Step 1** (energies; part 1). [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], parts 1–2, with $m_1 = m_2$ and $m_A = m_B$: $E_1 = E_2 = \frac{E_{\rm cm}^2 + m_f^2 - m_f^2}{2E_{\rm cm}} = \frac{E_{\rm cm}}{2}$ and the same for $E_A$, $E_B$ (Yu (6.358)).
>
> **Step 2** ($\lambda$ at two equal arguments; part 1). From [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]] (Yu (6.359)),
>
> $$
> \lambda(x, y, y) = x^2 + y^2 + y^2 - 2xy - 2xy - 2y^2 = x^2 - 4xy = x(x - 4y) ,
> $$
>
> so $\lambda(1, y, y) = 1 - 4y$ and $\lambda^{1/2}(1, m^2/E_{\rm cm}^2, m^2/E_{\rm cm}^2) = \sqrt{1 - 4m^2/E_{\rm cm}^2}$ (Yu (6.360)).
>
> **Step 3** (momenta; part 2). [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]: $|\mathbf p_1| = \frac{E_{\rm cm}}{2}\lambda^{1/2}(1, \frac{m_f^2}{E_{\rm cm}^2}, \frac{m_f^2}{E_{\rm cm}^2}) = \frac{E_{\rm cm}\beta_f}{2}$, likewise $|\mathbf p_A| = \frac{E_{\rm cm}\beta_i}{2}$ (Yu (6.361)); dividing by $E_1 = E_A = E_{\rm cm}/2$ gives $\beta_f = |\mathbf p_1|/E_1$, $\beta_i = |\mathbf p_A|/E_A$, the speeds $|\mathbf p|/E$ (Yu (6.362)).
>
> **Step 4** (flux; part 3). $\mathbf p_B = -\mathbf p_A$ and $E_B = E_A$: $|\mathbf v_A - \mathbf v_B| = \bigl|\frac{\mathbf p_A}{E_A} + \frac{\mathbf p_A}{E_A}\bigr| = \frac{2|\mathbf p_A|}{E_A} = 2\beta_i$, and $E_AE_B\cdot2\beta_i = \frac{E_{\rm cm}^2}{4}\cdot2\beta_i = \frac{E_{\rm cm}^2\beta_i}{2}$ (Yu (6.363)–(6.364)).
>
> **Step 5** (cross section; part 3). [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], 2, with Steps 3–4: $\frac{1}{128\pi^2}\cdot\frac{2}{E_{\rm cm}^2\beta_i}\cdot\beta_f|\mathcal M|^2 = \frac{\beta_f|\mathcal M|^2}{64\pi^2E_{\rm cm}^2\beta_i}$ (Yu (6.365)).
>
> **Step 6** (part 4). Two identical final particles: [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]]. Particles of different species are never counted twice.
>
> **Step 7** (part 5). By Step 1, $E_A = E_1 = E_2 = E_{\rm cm}/2$ also when $m_i \ne m_f$. So $t = (p_A - p_1)^2 = (E_A - E_1)^2 - |\mathbf p_A - \mathbf p_1|^2 = -|\mathbf p_A - \mathbf p_1|^2 \le 0$, and the same for $u$ with $p_2$. $t$ and $u$ are Lorentz scalars ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]), so their sign is the same in every frame; with $m_3^2 > 0$, $t - m_3^2 \le -m_3^2 < 0$: the denominator $t - m_3^2 + i\varepsilon$ has a nonzero limit, and $\varepsilon \to 0$ may be taken inside it.
>
> **What the derivation shows.**
> - All masses equal is $\beta_i = \beta_f$: [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-8|Theorem §C6b.4.8]].

^der-c6b-4-7

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]]

> [!theorem] Theorem §C6b.4.8: All Masses Equal
> If the four particles of a $2 \to 2$ process have the same mass,
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2} .
> $$
>
> It applies to elastic scattering of identical particles (two in, the same two out) and to any $2 \to 2$ process at energies $E \gg m_i$, where all masses effectively vanish. The final momentum $|\mathbf p_1|$ of the phase space cancels the $|\mathbf p_A|$ of the flux factor ($\beta_i = \beta_f$ in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]]).
>
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] with [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] (or [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]); *applies:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], all four masses equal.
>
> *Source: PHY 513 Lecture 15, slide 21 ("If all masses are identical: … $(\frac{d\sigma}{d\Omega})_{\rm c.m.s.} = \frac{1}{64\pi^2E_{\rm c.m.}^2}\cdot|\mathcal M|^2$. Applies in important special cases: 2 particles in, 2 particles out (all identical). High energy $E \gg m_i$ ⇒ all masses effectively vanish."), slide 25, and transcript · the user's PHY 513 notes, Ch. 15 §15.7, eq. (dsdO64), Derivation "The equal-mass case" · PS §4.5, eq. (4.85) · Yu §6.5.3, eq. (6.366)*

^thm-c6b-4-8

> [!derivation]- Derivation
> **Step 1** (initial energies). In the centre-of-mass frame $\mathbf p_B = -\mathbf p_A$, and with $m_A = m_B = m$,
>
> $$
> E_B = \sqrt{|-\mathbf p_A|^2 + m^2} = \sqrt{|\mathbf p_A|^2 + m^2} = E_A , \qquad E_A + E_B = E_{\rm cm} \;\Rightarrow\; 2E_A = 2E_B = E_{\rm cm} .
> $$
>
> **Step 2** (final momentum). The same for the final pair, $\mathbf p_2 = -\mathbf p_1$ and $m_1 = m_2 = m$: $E_1 = E_2 = E_{\rm cm}/2 = E_A$, hence
>
> $$
> |\mathbf p_1|^2 = E_1^2 - m^2 = E_A^2 - m^2 = |\mathbf p_A|^2 \;\Rightarrow\; |\mathbf p_1| = |\mathbf p_A| .
> $$
>
> **Step 3** (velocities). The velocities are back to back, $\mathbf v_B = \mathbf p_B/E_B = -\mathbf p_A/E_A = -\mathbf v_A$, so with Steps 1–2
>
> $$
> |\mathbf v_A - \mathbf v_B| = 2|\mathbf v_A| = \frac{2|\mathbf p_A|}{E_A} = \frac{2|\mathbf p_1|}{E_{\rm cm}/2} = \frac{4|\mathbf p_1|}{E_{\rm cm}} .
> $$
>
> **Step 4** (insert in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]). With $2E_A\,2E_B = E_{\rm cm}\cdot E_{\rm cm}$ (Step 1) and Step 3, the prefactor of $|\mathcal M|^2$ is
>
> $$
> \frac{1}{E_{\rm cm}\cdot E_{\rm cm}\cdot4|\mathbf p_1|/E_{\rm cm}}\cdot\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}} = \frac{1}{4|\mathbf p_1|E_{\rm cm}}\cdot\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}} = \frac{1}{64\pi^2E_{\rm cm}^2} .
> $$
>
> **Step 5** (high energy). For $E \gg m_i$,
>
> $$
> |\mathbf p_i| = \sqrt{E_i^2 - m_i^2} = E_i\Bigl(1 - \frac{m_i^2}{2E_i^2} + \cdots\Bigr) \to E_i , \qquad |\mathbf v_i| = \frac{|\mathbf p_i|}{E_i} \to 1 ;
> $$
>
> the masses drop out of Steps 1–4, which hold with $|\mathbf p_1| = |\mathbf p_A| = E_{\rm cm}/2$ whatever the masses were.
>
> **What the derivation shows.**
> - The $|\mathbf p_1|$ of the final phase space cancels the one of the initial velocity, so the initial-state and final-state factors combine.

^der-c6b-4-8

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!remark] Remark: Why 1/E²: dimensional analysis
> The result could have been guessed. $d\sigma/d\Omega$ is an area and $\mathcal M$ is dimensionless for $2 \to 2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]), so the prefactor has dimension $(\text{energy})^{-2}$. If the particles are kinematically indistinguishable, the total energy is the only scale, so the prefactor has to be one over the energy squared; only the number $64\pi^2$ is not fixed by this argument. A total cross section with an energy-independent $|\mathcal M|^2$ therefore falls like $1/E_{\rm cm}^2$ ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]]).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "Why $1/E_{\rm cm}^2$") · PHY 513 Lecture 16, slide 19 ("No angular dependence (feature of spin-less particles). Simple energy dependence (follows by dimensional analysis). Special to $\phi^4$-theory at leading order"; $\sigma_{\rm tot} = \lambda^2/(32\pi E_{\rm cm}^2)$, "note: identical particles")*

^rem-c6b-4-2

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2 — δ of a function with a simple zero, $\delta(f(p_1)) = \delta(p_1 - p_1^\ast)/|f'(p_1^\ast)|$: the energy delta function of $d\Pi_2$ becomes the Jacobian $\frac{E_1E_2}{p_1(E_1 + E_2)}$, which gives $\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}$ (Derivation §C6b.4.1, Step 3).

> [!remark]- Connections
> - $E_{\rm cm}^2 = s$, the first Mandelstam variable; the scattering angle $\theta$ of $d\Omega$ fixes $t$ — [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]].
> - The classical cross section transforms between the laboratory and centre-of-mass frames with an explicit Jacobian of the angles; here the transformation is built into the invariance of $d\Pi_2$ — [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^thm-b4-2-6|CM Theorem §B4.2.6]].
> - The same two-body formulas with $E_{\rm cm} \to m_A$ give the decay kinematics: a particle at rest is the centre-of-mass frame of its decay products — [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]], [[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]].
> - With unequal masses, $2 \to 2$ and its reverse at the same $E_{\rm cm}$ have flux factors $4|\mathbf k|E_{\rm cm}$ and $4|\mathbf k'|E_{\rm cm}$; with time-reversal invariance their unpolarized cross sections differ only by $\mathbf k'^2$ against $\mathbf k^2$ and the spin multiplicities — [[§C9.13 Time Reversal of the S-Matrix and Detailed Balance#^thm-c9-13-6|Theorem §C9.13.6]].
> - The Källén function also writes the invariant flux factor, $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = \frac12\lambda^{1/2}(s, m_A^2, m_B^2)$, and the invariant masses of three-body decays reuse the two-body energies in the rest frame of a pair — ★ [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-3|Theorem §C6b.4.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]], ★ [[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]].
> - The identical-particle factor as half the sphere is the counting of final states of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]] and [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]] made geometric.
