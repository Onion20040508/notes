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

*Sources: the user's PHY 513 notes, Ch. 15 §15.6 (Derivation "The flux factor as an $\varepsilon$-tensor component", Principle "Same cross section in the CM and target frames", eq. (moller), Caution "$|\vec v_A - \vec v_B|$ is not a relative velocity"), §15.7 (Definition "The $n$-body relativistic phase space", Derivation "Two-body phase space in the CM frame", paragraph "The momentum (filled in)", Principle "$2\to2$ differential cross section in the CM frame", Derivation "The equal-mass case", paragraph "Why $1/E_{\rm cm}^2$") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part C, slides 19–21, 25, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 106–107, eqs. (4.80)–(4.85) · Yu Zhao-Huan, 量子场论讲义, §6.5.2–§6.5.3, eqs. (6.314)–(6.366).*

<!-- HEADER-4 -->

*Conventions* ([[Larsen PHY 513]]): $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]; PS have $-1$); $x, y = 1, 2$; collinear beams along $z$; $E_{\rm cm}$ the total energy in the centre-of-mass frame ("c.m.s." on the slides, $E_{\rm CM}$ in Yu); $p_1 \equiv |\mathbf p_1|$.

## Two-body phase space in the centre-of-mass frame

> [!remark] Remark: You must commit
> To make $d\Pi_n$ explicit, "you must commit. … What coordinate system are you in? How many [particles] do you have? What are you actually observing?" With three or four particles in the final state the kinematics is harder, "but also a lot more data. There's literally more things you can measure": correlations and angles, so the theory predicts more. The lecture did only the simplest case; "in practice, this is not the sort of thing … you're going to work out" every time, but "the sort of thing like let me just look it up."
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7*

^rem-c6b-4-1

<!-- NEW def-c6b-4-1 -->

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
> *Source: PHY 513 Lecture 15, slide 20 ("Explicit expression for $n = 2$ final particles in cms: … $= \int d\Omega\frac{|\vec p_1|}{16\pi^2E_{\rm cm}}$"), and transcript ("Not that bad") · the user's PHY 513 notes, Ch. 15 §15.7, Derivation "Two-body phase space in the CM frame", eq. (dPi2) · PS §4.5, eqs. (4.81)–(4.82) · Yu §6.5.3, eqs. (6.341)–(6.343)*

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
> (The plus sign, where [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] had a minus, is because $\mathbf p_2 = -\mathbf p_1$: $E_2$ also grows with $p_1$. In the lecture, "Still was a minus, but then I've gotten rid of $p_2$ when $p_2$ is minus $p_1$.")
>
> **Step 4** (collect). Insert Step 3 into Step 2 and do the $p_1$ integral; with $(2\pi)^2\cdot4 = 16\pi^2$ and $E_1 + E_2 = E_{\rm cm}$ at the zero,
>
> $$
> \int d\Pi_2\,F = \int d\Omega\;\frac{1}{(2\pi)^2}\,\frac{p_1^2}{4E_1E_2}\,\frac{E_1E_2}{p_1(E_1 + E_2)}\,F\bigg|_{p_1^\ast} = \int d\Omega\;\frac{p_1}{16\pi^2(E_1 + E_2)}\,F\bigg|_{p_1^\ast} = \int d\Omega\;\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\,F .
> $$
>
> **What the derivation shows.**
> - Two of the six final momentum components remain, the direction $\Omega$ of $\mathbf p_1$; the particles come out "back to back".
> - The zero exists only if $E_{\rm cm} > m_1 + m_2$ (Yu eq. (6.339)): at $p_1 = 0$ the sum $E_1 + E_2$ is $m_1 + m_2$, and it increases with $p_1$.
> - Checked by smearing the energy delta function in `qft-C/tools/l15/checks.py` ($E_{\rm cm} = 5$, $m_1 = 1.2$, $m_2 = 0.7$).

^der-c6b-4-1

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!theorem] Theorem §C6b.4.2: The Centre-of-Mass Momentum
> In the setting of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]],
>
> $$
> |\mathbf p_1| = |\mathbf p_2| = \frac{\sqrt{\bigl[E_{\rm cm}^2 - (m_1 + m_2)^2\bigr]\bigl[E_{\rm cm}^2 - (m_1 - m_2)^2\bigr]}}{2E_{\rm cm}} = \frac{\lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2)}{2E_{\rm cm}} ,
> $$
>
> with the Källén function $\lambda(x, y, z) = x^2 + y^2 + z^2 - 2xy - 2xz - 2yz$, and $E_1 = \frac{E_{\rm cm}^2 + m_1^2 - m_2^2}{2E_{\rm cm}}$.
>
> *Model:* any (kinematics); *applies:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]].
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "The momentum (filled in)") · Yu §6.5.3, eqs. (6.346)–(6.352)*

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
> **What the derivation shows.**
> - $|\mathbf p_1|$ is real exactly above threshold, $E_{\rm cm} \ge m_1 + m_2$; the heavier particle takes the larger share of the energy (Yu after eq. (6.349)).

^der-c6b-4-2

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]

<!-- NEW thm-c6b-4-3 -->

## 2 → 2 scattering in the centre-of-mass frame

> [!theorem] Theorem §C6b.4.4: The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\cdot\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\cdot|\mathcal M|^2 ,
> $$
>
> with $\Omega$ the direction of $\mathbf p_1$ and $|\mathbf p_1|$ of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]].
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]] (or [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]); *applies:* as there; $\mathcal M$ from free states and the Feynman rules is exact in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] and lowest order in [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]].
>
> *Source: PHY 513 Lecture 15, slide 21 (boxed formula) · the user's PHY 513 notes, Ch. 15 §15.7, Principle "$2\to2$ differential cross section in the CM frame", eq. (dsdOgen) (a derived result: a theorem here) · PS §4.5, eq. (4.84) · Yu §6.5.3, eq. (6.345)*

^thm-c6b-4-4

> [!derivation]- Derivation
> **Step 1** (insert the phase space). By [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]] and [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2\,d\Pi_2$. For a smooth acceptance $g$ of the final states, [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]] with $F = |\mathcal M|^2g$ gives
>
> $$
> \int g\,d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\int d\Pi_2\,|\mathcal M|^2g = \int d\Omega\;g(\Omega)\;\frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\,|\mathcal M(\Omega)|^2 ,
> $$
>
> with $\mathcal M$ evaluated at $\mathbf p_2 = -\mathbf p_1$ and the $|\mathbf p_1|$ of the energy constraint; it depends on $\Omega$.
>
> **Step 2** (read off). The initial-state factor does not depend on $\Omega$; what multiplies $g(\Omega)\,d\Omega$ under the integral is $(d\sigma/d\Omega)_{\rm cm}$, the statement.
>
> **What the derivation shows.**
> - The initial-state factor has not been simplified: "I still have all the initial stuff, which has its own simplifications, perhaps." For unequal masses the kinematics of the particular situation must be worked out ("you just look it up").

^der-c6b-4-4

*Uses:* [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]

<!-- NEW thm-c6b-4-5 -->

<!-- NEW thm-c6b-4-6 -->

<!-- NEW thm-c6b-4-7 -->

> [!theorem] Theorem §C6b.4.8: All Masses Equal
> If the four particles of a $2 \to 2$ process have the same mass,
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2} .
> $$
>
> It applies to elastic scattering of identical particles (two in, the same two out) and to any $2 \to 2$ process at energies $E \gg m_i$, where all masses effectively vanish.
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* as in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], all four masses equal.
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
> - The $|\mathbf p_1|$ of the final phase space cancels the one of the initial velocity: "the initial state stuff and the final state stuff nicely sort of combine."

^der-c6b-4-8

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!remark] Remark: Why 1/E²: dimensional analysis
> The result could have been guessed. $d\sigma/d\Omega$ is an area and $\mathcal M$ is dimensionless for $2 \to 2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]), so the prefactor has dimension $(\text{energy})^{-2}$. "If particles do not sort of distinguish each other, kinematically speaking, total energy is [the] only [scale]. So it had to be basically one over the energy squared. All we can discuss is did I get the $64\pi^2$." A total cross section with an energy-independent $|\mathcal M|^2$ therefore falls like $1/E_{\rm cm}^2$ ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]]).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "Why $1/E_{\rm cm}^2$") · PHY 513 Lecture 16, slide 19 ("No angular dependence (feature of spin-less particles). Simple energy dependence (follows by dimensional analysis). Special to $\phi^4$-theory at leading order"; $\sigma_{\rm tot} = \lambda^2/(32\pi E_{\rm cm}^2)$, "note: identical particles")*

^rem-c6b-4-2

> [!remark]- Connections
> - $E_{\rm cm}^2 = s$, the first Mandelstam variable; the scattering angle $\theta$ of $d\Omega$ fixes $t$ — [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]].
> - The classical cross section transforms between the laboratory and centre-of-mass frames with an explicit Jacobian of the angles; here the transformation is built into the invariance of $d\Pi_2$ — [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^thm-b4-2-6|CM Theorem §B4.2.6]].
<!-- CONN-4 -->
