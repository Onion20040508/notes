---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.3 Evaluating the Cross Section]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.5 Decay Rates and Widths]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.6 (Derivation "The flux factor as an $\varepsilon$-tensor component", Principle "Same cross section in the CM and target frames", eq. (moller), Caution "$|\vec v_A - \vec v_B|$ is not a relative velocity"), §15.7 (Definition "The $n$-body relativistic phase space", Derivation "Two-body phase space in the CM frame", paragraph "The momentum (filled in)", Principle "$2\to2$ differential cross section in the CM frame", Derivation "The equal-mass case", paragraph "Why $1/E_{\rm cm}^2$") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part C, slides 19–21, 25, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 106–107, eqs. (4.80)–(4.85) · Yu Zhao-Huan, 量子场论讲义, §6.5.2–§6.5.3, eqs. (6.314)–(6.366).*

The cross section of [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] has three factors. $|\mathcal M|^2$ is Lorentz invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]) and so is the final phase space, but the prefactor $E_AE_B|\mathbf v_A - \mathbf v_B|$ "looks highly not relativistically invariant", and $\sigma$ is an area, not a scalar. Part C of the lecture resolves the puzzle with "a trick: undo the velocities": the flux factor is one component of an antisymmetric tensor, invariant under boosts along the beam and rotating like an area ([[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-2|Theorem §C6b.4.2]]). It then makes the phase space explicit in the simplest case, two particles in the centre-of-mass frame, and obtains the $2 \to 2$ differential cross section, which for equal masses is $|\mathcal M|^2/(64\pi^2E_{\rm cm}^2)$. Yu reaches the same results with the Møller velocity (§6.5.2, eqs. (6.314)–(6.331)) and the Källén function (§6.5.3, eqs. (6.336)–(6.366)); Remark: Yu's route, at the end.

*Conventions* ([[Larsen PHY 513]]): $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]; PS have $-1$); $x, y = 1, 2$; collinear beams along $z$; $E_{\rm cm}$ the total energy in the centre-of-mass frame ("c.m.s." on the slides, $E_{\rm CM}$ in Yu); $p_1 \equiv |\mathbf p_1|$.

## Lorentz invariance of the cross section

> [!theorem] Theorem §C6b.4.1: The Flux Factor Is a Component of an Antisymmetric Tensor
> For momenta $p_A$, $p_B$ along the $z$-axis,
>
> $$
> E_AE_B\bigl(v_A^z - v_B^z\bigr) = E_Bp_A^z - E_Ap_B^z = \varepsilon_{xy\mu\nu}\,p_A^\mu p_B^\nu ,
> $$
>
> the $xy$ component of the antisymmetric tensor $F_{\rho\sigma} = \varepsilon_{\rho\sigma\mu\nu}p_A^\mu p_B^\nu$.
>
> *Source: PHY 513 Lecture 15, slide 19 ("$E_AE_B(v_A^z - v_B^z) = E_Bp_A^z - E_Ap_B^z = \epsilon_{xy\mu\nu}p_A^\mu p_B^\nu$ ⇒ prefactor transforms like an area"), and transcript ("as we just learned, momentum divided by $E$ gives velocity. That works the other way around as well") · the user's PHY 513 notes, Ch. 15 §15.6, eq. (fluxeps) · PS §4.5, p. 106 (with $|\epsilon_{\mu xy\nu}p_A^\mu p_B^\nu|$)*

^thm-c6b-4-1

> [!derivation]- Derivation
> **Step 1** (undo the velocities). $v^z = p^z/E$ ([[§C6b.3 Evaluating the Cross Section#^der-c6b-3-1|Derivation §C6b.3.1]], Step 5), so
>
> $$
> E_AE_B\bigl(v_A^z - v_B^z\bigr) = E_AE_B\frac{p_A^z}{E_A} - E_AE_B\frac{p_B^z}{E_B} = E_Bp_A^z - E_Ap_B^z .
> $$
>
> **Step 2** (which components survive). $\varepsilon_{12\mu\nu}$ vanishes when an index repeats, so $\mu, \nu \in \{0, 3\}$ with $\mu \ne \nu$. Of the 16 terms of the double sum only two remain:
>
> $$
> \varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \sum_{\mu,\nu=0}^3\varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \varepsilon_{1203}\,p_A^0p_B^3 + \varepsilon_{1230}\,p_A^3p_B^0 .
> $$
>
> **Step 3** (the signs). Count transpositions from $(0, 1, 2, 3)$:
>
> $$
> (0, 1, 2, 3) \to (1, 0, 2, 3) \to (1, 2, 0, 3) \to (1, 2, 3, 0) ,
> $$
>
> so $(1, 2, 0, 3)$ is two transpositions away (even) and $(1, 2, 3, 0)$ three (odd): $\varepsilon_{1203} = +\varepsilon_{0123} = -1$, $\varepsilon_{1230} = -\varepsilon_{0123} = +1$.
>
> **Step 4** (assemble). With $p^0 = E$, $p^3 = p^z$:
>
> $$
> \varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \varepsilon_{1203}\,E_A\,p_B^z + \varepsilon_{1230}\,p_A^z\,E_B = -E_Ap_B^z + E_Bp_A^z ,
> $$
>
> which is step 1.
>
> **What the derivation shows.**
> - With PS's $\varepsilon^{0123} = -1$ the middle expression changes sign; inside the absolute value of the flux factor it does not matter.
> - Checked numerically at random collinear momenta in `qft-C/tools/l15/checks.py`.

^der-c6b-4-1

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]

> [!theorem] Theorem §C6b.4.2: The Cross Section Transforms Like an Area
> 1. $E_AE_B|\mathbf v_A - \mathbf v_B|$, and hence $d\sigma$ of [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]], is invariant under boosts along the beam axis $z$.
> 2. Under rotations the flux factor transforms like an area element in the plane transverse to the beam, as $\sigma$ does.
> 3. In particular $d\sigma$ is the same in the centre-of-mass frame ($\mathbf p_{\rm tot} = \mathbf 0$) and in a target frame ($\mathbf p_A = \mathbf 0$ or $\mathbf p_B = \mathbf 0$).
>
> *Source: PHY 513 Lecture 15, slide 19 ("Cross-section $\sigma$ really is an 'area', it transforms like one. Application: $d\sigma$ invariant under boosts in $z$-direction. Same in c.m.s. ($\vec p_{\rm tot} = 0$) and target frame ($\vec p_A = 0$ or $\vec p_B = 0$)."), and transcript ("it's not even exactly invariant. It should transform like an area, and it does") · the user's PHY 513 notes, Ch. 15 §15.6, Principle "Same cross section in the CM and target frames" (a derived result: a theorem here) · PS §4.5, p. 106*

^thm-c6b-4-2

> [!derivation]- Derivation
> **Step 1** (a boost along $z$). Such a boost acts only on the components $0$, $3$, as the matrix of [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], and leaves $x$, $y$ alone. With $c = \cosh\eta$, $s = \sinh\eta$, each momentum becomes
>
> $$
> E' = c\,E + s\,p^z , \qquad p'^z = s\,E + c\,p^z , \qquad \mathbf p'^\perp = \mathbf p^\perp .
> $$
>
> **Step 2** (the component $F_{12}$ is invariant). By [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-1|Theorem §C6b.4.1]], $F_{12} = E_Bp_A^z - E_Ap_B^z$. Insert Step 1 and expand all eight products:
>
> $$
> \begin{aligned}
> F'_{12} = E'_Bp'^z_A - E'_Ap'^z_B ={}& (cE_B + s\,p_B^z)(sE_A + c\,p_A^z) - (cE_A + s\,p_A^z)(sE_B + c\,p_B^z)\\
> ={}& cs\,E_BE_A + c^2E_Bp_A^z + s^2p_B^zE_A + sc\,p_B^zp_A^z - cs\,E_AE_B - c^2E_Ap_B^z - s^2p_A^zE_B - sc\,p_A^zp_B^z\\
> ={}& (c^2 - s^2)\bigl(E_Bp_A^z - E_Ap_B^z\bigr) = F_{12} ,
> \end{aligned}
> $$
>
> since $\cosh^2\eta - \sinh^2\eta = 1$. In index form this is the determinant rule: restricted to $\mu, \nu \in \{0, 3\}$, $\varepsilon_{12\mu\nu} = -\epsilon_{\mu\nu}$ with the two-dimensional symbol $\epsilon_{03} = 1$ (Step 3 of [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^der-c6b-4-1|Derivation §C6b.4.1]]), and $\epsilon_{\mu\nu}L^\mu{}_\alpha L^\nu{}_\beta = \det L\,\epsilon_{\alpha\beta}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] in two dimensions) with $\det L = c^2 - s^2 = 1$. For collinear beams $|\mathbf v_A - \mathbf v_B| = |v_A^z - v_B^z|$, so $E_AE_B|\mathbf v_A - \mathbf v_B| = |F_{12}|$ is invariant; $|\mathcal M|^2$ and the phase space are invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-4|Theorem §C6b.4.4]]): part 1.
>
> **Step 3** (rotations). $F_{\rho\sigma} = \varepsilon_{\rho\sigma\mu\nu}p_A^\mu p_B^\nu$ is an antisymmetric tensor; under a rotation $R$ its spatial components transform as
>
> $$
> F'_{ij} = R_i{}^kR_j{}^l\,F_{kl} , \qquad F_{12} = \tfrac12\,\varepsilon_{3jk}F_{jk} ,
> $$
>
> like the components of an area element $dx^i\wedge dx^j$, equivalently like the $z$ component of the axial vector $\frac12\varepsilon_{ijk}F_{jk}$, the normal to the plane. The flux factor is the component $F_{12}$, the area element in the plane transverse to the beam: part 2. The cross section is defined as an area in that plane ([[§C6b.2 Wave Packets and the Cross Section#^def-c6b-2-6|Def. §C6b.2.6]]: an integral over $d^2b$).
>
> **Step 4** (frames). The centre-of-mass frame and the rest frames of $A$ or of $B$ are reached from one another by boosts along the common beam axis: with $\tanh\eta = v$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]]), $\cosh\eta = \gamma$, $\sinh\eta = \gamma v$ in Step 1 gives $p'^z = \gamma(vE + p^z)$, so the boost with $v = -\frac{p_A^z + p_B^z}{E_A + E_B}$ takes the total momentum to zero and the one with $v = -v_A^z$ takes $A$ to rest. Part 1 applies to each: part 3.
>
> **What the derivation shows.**
> - The flux factor is not a Lorentz scalar; the cross section is not either; they transform alike, which is all that is needed.
> - The same trick, a component transverse to a boost is invariant under it, gave the centre-of-mass momentum in Problem Set 1 — [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]].

^der-c6b-4-2

*Uses:* [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-4|Theorem §C6b.4.4]]

> [!theorem] Theorem §C6b.4.3: The Flux Factor in Invariant Form
> For collinear beams,
>
> $$
> E_AE_B\,|\mathbf v_A - \mathbf v_B| = \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} ,
> $$
>
> which is manifestly invariant. In general $\frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2}$, Yu's Møller velocity $v_{\rm Møl}$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6, eq. (moller) (filled in) · Yu §6.5.2, eqs. (6.315), (6.322)–(6.329)*

^thm-c6b-4-3

> [!derivation]- Derivation
> **Step 1** (the invariant). With $p^\mu = (E, \mathbf p) = E(1, \mathbf v)$ (Yu eqs. (6.325)–(6.326)),
>
> $$
> p_A\cdot p_B = E_AE_B - \mathbf p_A\cdot\mathbf p_B = E_AE_B - E_AE_B\,\mathbf v_A\cdot\mathbf v_B = E_AE_B(1 - \mathbf v_A\cdot\mathbf v_B) .
> $$
>
> **Step 2** (square). Three identities: the binomial square, Lagrange's identity ($\cos^2 = 1 - \sin^2$), and the expansion of $|\mathbf v_A - \mathbf v_B|^2$:
>
> $$
> (1 - \mathbf v_A\cdot\mathbf v_B)^2 = 1 - 2\mathbf v_A\cdot\mathbf v_B + (\mathbf v_A\cdot\mathbf v_B)^2 , \qquad (\mathbf v_A\cdot\mathbf v_B)^2 = |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 , \qquad -2\mathbf v_A\cdot\mathbf v_B = |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2 .
> $$
>
> Substituting the second and third into the first and regrouping $1 - |\mathbf v_A|^2 - |\mathbf v_B|^2 + |\mathbf v_A|^2|\mathbf v_B|^2 = (1 - |\mathbf v_A|^2)(1 - |\mathbf v_B|^2)$:
>
> $$
> \begin{aligned}
> (1 - \mathbf v_A\cdot\mathbf v_B)^2 &= 1 + |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2 + |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\\
> &= |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 + (1 - |\mathbf v_A|^2)(1 - |\mathbf v_B|^2) .
> \end{aligned}
> $$
>
> **Step 3** (the masses cancel). $E^2(1 - |\mathbf v|^2) = E^2 - |\mathbf p|^2 = m^2$ for each particle, so, multiplying Step 2 by $E_A^2E_B^2$ and using Step 1,
>
> $$
> (p_A\cdot p_B)^2 = E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) + m_A^2m_B^2 \quad\Rightarrow\quad (p_A\cdot p_B)^2 - m_A^2m_B^2 = E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) .
> $$
>
> **Step 4** (collinear). For collinear beams $\mathbf v_A\times\mathbf v_B = 0$; take the square root ($E_AE_B > 0$):
>
> $$
> \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = E_AE_B\,|\mathbf v_A - \mathbf v_B| .
> $$
>
> **Step 5** (check in the rest frame of $A$). $p_A = (m_A, \mathbf 0)$, $E_B^2 - m_B^2 = |\mathbf p_B|^2$:
>
> $$
> \sqrt{(m_AE_B)^2 - m_A^2m_B^2} = m_A\sqrt{E_B^2 - m_B^2} = m_A|\mathbf p_B| , \qquad E_AE_B|\mathbf v_A - \mathbf v_B| = m_AE_B\,\frac{|\mathbf p_B|}{E_B} = m_A|\mathbf p_B| .
> $$
>
> **What the derivation shows.**
> - For collinear beams the flux factor is a function of the invariant $p_A\cdot p_B$ alone, the algebraic reason behind [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-2|Theorem §C6b.4.2]], 1. (For collinear beams $F_{12}^2 = \frac12F_{\rho\sigma}F^{\rho\sigma} = (p_A\cdot p_B)^2 - m_A^2m_B^2$, by the contraction identity $\varepsilon_{\rho\sigma\mu\nu}\varepsilon^{\rho\sigma\alpha\beta} = -2(\delta^\alpha_\mu\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\mu)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]]) and because the other components of $F$ vanish.)
> - Checked numerically in `qft-C/tools/l15/checks.py`.

^der-c6b-4-3

*Uses:* [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-1|Theorem §C6b.4.1]]

> [!caution] Caution: The velocity difference is not a relative velocity
> $|\mathbf v_A - \mathbf v_B|$ is the difference of two velocities measured in the same frame, not the speed of one particle in the rest frame of the other. It is not bounded by 1: for a head-on collision of ultrarelativistic particles in the centre-of-mass frame it approaches 2. Nothing is wrong: it is the rate at which the two flux tubes sweep through each other. Names: PS call it "the relative velocity of the beams as viewed from the laboratory frame" (p. 106); Yu defines $v_{\rm rel} \equiv |\mathbf v_{\mathcal A} - \mathbf v_{\mathcal B}|$, "相对速度" (eq. (6.314)), and notes that for head-on ultrarelativistic beams $v_{\rm rel} = 2$, "no longer a relative velocity in the traditional sense" (p. 246); the true relative speed is the Møller-type invariant $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}/(p_A\cdot p_B)$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6, Caution "$|\vec v_A - \vec v_B|$ is not a relative velocity" · PS §4.5, p. 106 · Yu §6.5.2, eq. (6.314), p. 246*

^cau-c6b-4-1

## Phase space

> [!definition] Definition §C6b.4.1: The n-Particle Relativistic Phase Space
> The **$n$-particle phase-space factor** of a final state of $n$ particles with total four-momentum $P$ is
>
> $$
> d\Pi_n = \Bigl(\prod_{i=1}^n\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\Bigr)\cdot(2\pi)^4\delta^4\Bigl(P - \sum_ip_i\Bigr) ,
> $$
>
> with $P = p_A + p_B$ for scattering and $P = p_A$ for a decay ([[§C6b.5 Decay Rates and Widths|§C6b.5]]): the kinematics of the $n$ final particles. An explicit $d\Pi_n$ requires a specific final state and coordinate system.
>
> *Source: PHY 513 Lecture 15, slide 20 ("The $n$-particle phase space factor $d\Pi_n = (\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i})\cdot(2\pi)^4\delta^{(4)}(p_A + p_B - \sum_ip_i)$"), slide 25 ("The phase space factor is kinematics of $n$ final particles … Explicit $d\Pi_n$: specific final state and coordinate system"), slide 22 (with $p_A$), and transcript ("this whole thing here is sometimes called the $n$ particle relativistic phase space") · the user's PHY 513 notes, Ch. 15 §15.7, eq. (dPin) · PS §4.5, eq. (4.80) ("relativistically invariant $n$-body phase space") · Yu §6.5.2, eq. (6.318) ($n$ 体不变相空间)*

^def-c6b-4-1

With it, [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] reads $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\,|\mathcal M|^2\,d\Pi_n$ (slide 24).

> [!theorem] Theorem §C6b.4.4: The Phase Space Is Lorentz Invariant
> For every scalar function $F$ of the momenta and every $\Lambda \in SO^+(1, 3)$, $\int d\Pi_n\,F(p_1, \dots, p_n)$ with total momentum $\Lambda P$ equals the same integral of $F(\Lambda p_1, \dots, \Lambda p_n)$ with total momentum $P$: $d\Pi_n$ is an invariant measure on the final states.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6 (first paragraph) and §15.7 (Definition "The $n$-body relativistic phase space": "It is Lorentz invariant") · PS §4.5, p. 106 ("manifestly Lorentz invariant") · Yu §6.5.1, eq. (6.304)*

^thm-c6b-4-4

> [!derivation]- Derivation
> **Step 1** (each one-particle factor). By [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] and [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], substituting $p = \Lambda p'$:
>
> $$
> \int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}\,G(p) = \int\frac{d^4p}{(2\pi)^4}\,2\pi\delta(p^2 - m^2)\theta(p^0)\,G(p) = \int\frac{d^4p'}{(2\pi)^4}\,|\det\Lambda|\,2\pi\delta\bigl((\Lambda p')^2 - m^2\bigr)\theta\bigl((\Lambda p')^0\bigr)\,G(\Lambda p') = \int\frac{d^3p'}{(2\pi)^32E_{\mathbf p'}}\,G(\Lambda p') ,
> $$
>
> using $|\det\Lambda| = 1$, $(\Lambda p')^2 = p'^2$, and $\theta((\Lambda p')^0) = \theta(p'^0)$ on the mass shell.
>
> **Step 2** (the delta function). By linearity and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1,
>
> $$
> \delta^4\Bigl(\Lambda P - \sum_i\Lambda p_i'\Bigr) = \delta^4\Bigl(\Lambda\bigl(P - \textstyle\sum_ip_i'\bigr)\Bigr) = |\det\Lambda|^{-1}\,\delta^4\Bigl(P - \sum_ip_i'\Bigr) = \delta^4\Bigl(P - \sum_ip_i'\Bigr) .
> $$
>
> **Step 3** (combine). Substitute $p_i = \Lambda p_i'$ in every factor of the integral with total momentum $\Lambda P$; by Step 1 each measure is unchanged, by Step 2 the delta function loses its $\Lambda$:
>
> $$
> \int\prod_i\frac{d^3p_i}{(2\pi)^32E_i}\,(2\pi)^4\delta^4\Bigl(\Lambda P - \sum_ip_i\Bigr)F(p_1, \dots, p_n) = \int\prod_i\frac{d^3p_i'}{(2\pi)^32E_i'}\,(2\pi)^4\delta^4\Bigl(P - \sum_ip_i'\Bigr)F(\Lambda p_1', \dots, \Lambda p_n') .
> $$
>
> **What the derivation shows.**
> - "It is built up from invariant 3-momentum integrals constrained by a 4-momentum delta function" (PS p. 106); the invariance holds for the measure as a whole, not for its explicit form in a chosen frame.

^der-c6b-4-4

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!remark] Remark: You must commit
> To make $d\Pi_n$ explicit, "you must commit. … What coordinate system are you in? How many [particles] do you have? What are you actually observing?" With three or four particles in the final state the kinematics is harder, "but also a lot more data. There's literally more things you can measure": correlations and angles, so the theory predicts more. The lecture did only the simplest case; "in practice, this is not the sort of thing … you're going to work out" every time, but "the sort of thing like let me just look it up."
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7*

^rem-c6b-4-1

> [!theorem] Theorem §C6b.4.5: Two-Body Phase Space in the Centre-of-Mass Frame
> For $n = 2$ final particles in the centre-of-mass frame, $P = (E_{\rm cm}, \mathbf 0)$,
>
> $$
> \int d\Pi_2\;F = \int d\Omega\;\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\;F ,
> $$
>
> where $\Omega$ is the direction of $\mathbf p_1$, $\mathbf p_2 = -\mathbf p_1$, and $|\mathbf p_1|$ is fixed by $E_1 + E_2 = E_{\rm cm}$ with $E_1 = \sqrt{p_1^2 + m_1^2}$, $E_2 = \sqrt{p_1^2 + m_2^2}$.
>
> *Source: PHY 513 Lecture 15, slide 20 ("Explicit expression for $n = 2$ final particles in cms: … $= \int d\Omega\frac{|\vec p_1|}{16\pi^2E_{\rm cm}}$"), and transcript ("Not that bad") · the user's PHY 513 notes, Ch. 15 §15.7, Derivation "Two-body phase space in the CM frame", eq. (dPi2) · PS §4.5, eqs. (4.81)–(4.82) · Yu §6.5.3, eqs. (6.341)–(6.343)*

^thm-c6b-4-5

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
> (The plus sign, where [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-1|Theorem §C6b.3.1]] had a minus, is because $\mathbf p_2 = -\mathbf p_1$: $E_2$ also grows with $p_1$. In the lecture, "Still was a minus, but then I've gotten rid of $p_2$ when $p_2$ is minus $p_1$.")
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

^der-c6b-4-5

*Uses:* [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^def-c6b-4-1|Def. §C6b.4.1]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Theorem §C6b.4.6: The Centre-of-Mass Momentum
> In the setting of [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-5|Theorem §C6b.4.5]],
>
> $$
> |\mathbf p_1| = |\mathbf p_2| = \frac{\sqrt{\bigl[E_{\rm cm}^2 - (m_1 + m_2)^2\bigr]\bigl[E_{\rm cm}^2 - (m_1 - m_2)^2\bigr]}}{2E_{\rm cm}} = \frac{\lambda^{1/2}(E_{\rm cm}^2, m_1^2, m_2^2)}{2E_{\rm cm}} ,
> $$
>
> with the Källén function $\lambda(x, y, z) = x^2 + y^2 + z^2 - 2xy - 2xz - 2yz$, and $E_1 = \frac{E_{\rm cm}^2 + m_1^2 - m_2^2}{2E_{\rm cm}}$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "The momentum (filled in)") · Yu §6.5.3, eqs. (6.346)–(6.352)*

^thm-c6b-4-6

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

^der-c6b-4-6

*Uses:* [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-5|Theorem §C6b.4.5]]

## 2 → 2 scattering in the centre-of-mass frame

> [!theorem] Theorem §C6b.4.7: The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\cdot\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\cdot|\mathcal M|^2 ,
> $$
>
> with $\Omega$ the direction of $\mathbf p_1$ and $|\mathbf p_1|$ of [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-6|Theorem §C6b.4.6]].
>
> *Source: PHY 513 Lecture 15, slide 21 (boxed formula) · the user's PHY 513 notes, Ch. 15 §15.7, Principle "$2\to2$ differential cross section in the CM frame", eq. (dsdOgen) (a derived result: a theorem here) · PS §4.5, eq. (4.84) · Yu §6.5.3, eq. (6.345)*

^thm-c6b-4-7

> [!derivation]- Derivation
> **Step 1** (insert the phase space). By [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] and [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^def-c6b-4-1|Def. §C6b.4.1]], $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}|\mathcal M|^2\,d\Pi_2$. For a smooth acceptance $g$ of the final states, [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-5|Theorem §C6b.4.5]] with $F = |\mathcal M|^2g$ gives
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

^der-c6b-4-7

*Uses:* [[§C6b.3 Evaluating the Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-5|Theorem §C6b.4.5]], [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^def-c6b-4-1|Def. §C6b.4.1]]

> [!theorem] Theorem §C6b.4.8: All Masses Equal
> If the four particles of a $2 \to 2$ process have the same mass,
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2} .
> $$
>
> It applies to elastic scattering of identical particles (two in, the same two out) and to any $2 \to 2$ process at energies $E \gg m_i$, where all masses effectively vanish.
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
> **Step 4** (insert in [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-7|Theorem §C6b.4.7]]). With $2E_A\,2E_B = E_{\rm cm}\cdot E_{\rm cm}$ (Step 1) and Step 3, the prefactor of $|\mathcal M|^2$ is
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

*Uses:* [[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-7|Theorem §C6b.4.7]]

> [!remark] Remark: Why 1/E²: dimensional analysis
> The result could have been guessed. $d\sigma/d\Omega$ is an area and $\mathcal M$ is dimensionless for $2 \to 2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-3|Theorem §C6b.1.3]]), so the prefactor has dimension $(\text{energy})^{-2}$. "If particles do not sort of distinguish each other, kinematically speaking, total energy is [the] only [scale]. So it had to be basically one over the energy squared. All we can discuss is did I get the $64\pi^2$." A total cross section with an energy-independent $|\mathcal M|^2$ therefore falls like $1/E_{\rm cm}^2$ ([[§C6b.6 Amplitudes from Correlation Functions#^ex-c6b-6-2|Example §C6b.6.2]]).
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.7 (paragraph "Why $1/E_{\rm cm}^2$")*

^rem-c6b-4-2

> [!remark] Remark: Yu's route
> Yu writes the cross section first for a fixed target and then replaces $|\mathbf v_{\mathcal B}|$ by the **Møller velocity** $v_{\rm Møl} = \frac{1}{E_{\mathcal A}E_{\mathcal B}}\sqrt{(p_{\mathcal A}\cdot p_{\mathcal B})^2 - m_{\mathcal A}^2m_{\mathcal B}^2}$ (eq. (6.315)), which makes the incident flux $E_{\mathcal A}E_{\mathcal B}v_{\rm Møl}$ and $\sigma$ Lorentz invariant *by definition* (eq. (6.316)); $d\Pi_n$ is eq. (6.318), $d\sigma$ eq. (6.320). He shows $v_{\rm Møl} = \sqrt{|\mathbf v_{\mathcal A} - \mathbf v_{\mathcal B}|^2 - |\mathbf v_{\mathcal A}\times\mathbf v_{\mathcal B}|^2}$ (eqs. (6.322)–(6.329)), so for collinear beams the two definitions agree ([[§C6b.4 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-4-3|Theorem §C6b.4.3]]); the course instead derives the transformation law of the flux factor (an area). His $2 \to 2$ kinematics in the centre-of-mass frame: eqs. (6.336)–(6.345) (two-body phase space (6.341)–(6.343), $d\sigma/d\Omega$ (6.345)), the Källén function (6.351) with $d\sigma/d\Omega$ in terms of it (6.353), special cases (6.356)–(6.366), all four masses equal (6.366).
>
> *Source: Yu §6.5.2–§6.5.3, pp. 244–250, eqs. (6.314)–(6.366)*

^rem-c6b-4-3

> [!remark]- Connections
> - "A component transverse to a boost is invariant under that boost": the same observation gave the centre-of-mass momentum from one tensor component in two frames — [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]].
> - The invariant measure of the phase space is the one that makes $\langle\mathbf p|\mathbf q\rangle$ invariant and that appears in every mode expansion — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]].
> - $E_{\rm cm}^2 = s$, the first Mandelstam variable; the scattering angle $\theta$ of $d\Omega$ fixes $t$ — [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]].
> - The classical cross section transforms between the laboratory and centre-of-mass frames with an explicit Jacobian of the angles; here the transformation is built into the invariance of $d\Pi_2$ — [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^thm-b4-2-6|CM Theorem §B4.2.6]].
> - The flux factor $F_{12}$ is the dual, in the transverse plane, of the antisymmetric tensor built from the two momenta, as $\mathbf B$ is the dual of $F_{ij}$ in electrodynamics — [[§C1a.7 Relativistic Electrodynamics in Index Form|§C1a.7]].
