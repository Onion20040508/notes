---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.5 Decay Widths]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.7 The Width in the Propagator]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.5 "衰变运动学", pp. 252–257, eqs. (6.379)–(6.411), Figs. 6.6–6.7 (page images checked, PDF pp. 260–265) · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Two-body decays (filled in)") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), slide 22, and transcript · PHY 513, Problem Set 8, Problem 4 (= PS Problem 4.2; the user's solution) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, eqs. (4.81)–(4.82), (4.86).*

The decay formula of [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] needs the phase space of the products. A particle at rest is the centre-of-mass frame of its decay products, so two-body decays reuse the two-body kinematics of [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]] with $E_{\rm cm} = m_A$: everything but the direction is fixed ([[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]]), the width is one number times $|\mathcal M|^2$ ([[§C6b.6 Decay Kinematics#^thm-c6b-6-2|Theorem §C6b.6.2]]), and for equal masses it vanishes like $\beta$ at threshold ([[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]]). The decay $\Phi \to \phi\phi$ of Problem Set 8 is worked as the user solved it ([[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]]). Three-body decays (★, Yu §6.5.5 (2), beyond the course so far) have a two-dimensional phase space, flat in the energies ([[§C6b.6 Decay Kinematics#^thm-c6b-6-5|Theorem §C6b.6.5]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-6|Theorem §C6b.6.6]]) and in the invariant masses of pairs ([[§C6b.6 Decay Kinematics#^def-c6b-6-1|Def. §C6b.6.1]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-7|Theorem §C6b.6.7]]), over the Dalitz region ([[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]]).

**Setup.** [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]: one particle $A$ at rest, free relativistically normalized states, the width of [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]. The kinematics is exact; every width holds at lowest order in the interaction that makes $A$ decay ([[§C6b.5 Decay Widths#^cau-c6b-5-1|§C6b.5, Caution: Free states in a decay amplitude]]). The three-body formulas assume $|\mathcal M|^2$ independent of the orientation of the decay plane: spin 0, or averaged over the spin of $A$ ([[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]]).

*Conventions* ([[Larsen PHY 513]]): $A$ the decaying particle, mass $m_A$, at rest; $m_1, m_2, m_3$ the masses of the products; $\lambda$ the Källén function ([[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]); $\beta = \sqrt{1 - 4m^2/m_A^2}$ for two equal masses; tildes mark quantities in the centre-of-mass frame of the pair $(1, 2)$ (Yu's notation); $S_{\rm id}$ the identical-particle factor (Yu: $\mathcal S$).

## Two-body decays

> [!theorem] Theorem §C6b.6.1: Two-Body Phase Space at Rest
> Let $A$ (mass $m_A$, at rest) decay into two particles of masses $m_1$, $m_2$, $m_A > m_1 + m_2$ ([[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]). The rest frame of $A$ is the centre-of-mass frame of the products, $E_{\rm cm} = m_A$, and
>
> $$
> \int d\Pi_2\,F = \int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2m_A}\,F , \qquad \int d\Pi_2 = \frac{|\mathbf p_1|}{4\pi m_A} ,
> $$
>
> $$
> |\mathbf p_1| = |\mathbf p_2| = \frac{\lambda^{1/2}(m_A^2, m_1^2, m_2^2)}{2m_A} = \frac{m_A}{2}\,\lambda^{1/2}\Bigl(1, \frac{m_1^2}{m_A^2}, \frac{m_2^2}{m_A^2}\Bigr) , \qquad E_1 = \frac{m_A^2 + m_1^2 - m_2^2}{2m_A} , \qquad E_2 = \frac{m_A^2 + m_2^2 - m_1^2}{2m_A} ,
> $$
>
> with $\lambda$ of [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]. A two-body decay at rest has no free kinematics: the energies and $|\mathbf p_1|$ are fixed numbers, and only the direction $\Omega$ of $\mathbf p_1$ is integrated.
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there: the kinematics exactly.
>
> *Source: Yu §6.5.5, eqs. (6.379)–(6.381) (page image checked: "可见，末态粒子的能量和动量大小都是常数") · PHY 513, Problem Set 8, Problem 4 (the user's $\int d\Pi_2 = p_\ast/(4\pi M)$) · PS §4.5, eqs. (4.81)–(4.82) for the phase space*

^thm-c6b-6-1

> [!derivation]- Derivation
> **Step 1** (phase space). The rest frame of $A$ is the centre-of-mass frame of the products, $P = p_A = (m_A, \mathbf 0)$, $E_{\rm cm} = m_A$. [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]] and [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]] with $E_{\rm cm} \to m_A$ give the formulas for $|\mathbf p_1|$ and $E_1$ (Yu (6.379)–(6.381)). With $F = 1$ the integrand does not depend on $\Omega$, $\int d\Omega = 4\pi$:
>
> $$
> \int d\Pi_2 = 4\pi\,\frac{|\mathbf p_1|}{16\pi^2m_A} = \frac{|\mathbf p_1|}{4\pi m_A} .
> $$
>
> $E_2$ is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], 1, with $E_{\rm cm} \to m_A$ (Yu (6.379)), and the dimensionless form of $|\mathbf p_1|$ its Step 5 (Yu (6.380)).
>
> **What the derivation shows.**
> - A two-body decay at rest has no free kinematics: the energies and $|\mathbf p_1|$ are fixed numbers, and only the direction is integrated (now in the statement).

^der-c6b-6-1

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]

> [!theorem] Theorem §C6b.6.2: The Two-Body Width
> In the setting of [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]], by [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]:
> 1. $\displaystyle\Gamma = \frac{1}{S_{\rm id}}\,\frac{1}{2m_A}\int d\Pi_2\,|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathbf p_1|}{32\pi^2m_A^2}\int d\Omega\,|\mathcal M|^2$;
> 2. if $|\mathcal M|^2$ does not depend on the direction of $\mathbf p_1$ (spin 0, or averaged over the spin of $A$: [[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]]),
>
> $$
> \Gamma = \frac{1}{S_{\rm id}}\,\frac{|\mathbf p_1|}{8\pi m_A^2}\,|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathcal M|^2}{16\pi m_A}\,\lambda^{1/2}\Bigl(1, \frac{m_1^2}{m_A^2}, \frac{m_2^2}{m_A^2}\Bigr) ;
> $$
>
> 3. if $m_1 \ne m_2$ the two products are not identical, and $S_{\rm id} = 1$.
>
> $\mathcal M$ of a $1 \to 2$ decay has the dimension of a mass ([[§C6b.5 Decay Widths#^thm-c6b-5-7|Theorem §C6b.5.7]]).
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there: $\Gamma$ at lowest order in the decaying interaction.
>
> *Source: Yu §6.5.5, eqs. (6.382)–(6.383) (page image checked: (6.383) boxed; "如果 $m_1 \ne m_2$，则两个末态粒子必定不是全同粒子，而 $\mathcal S = 1$") · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Two-body decays (filled in)")*

^thm-c6b-6-2

> [!derivation]- Derivation
> **Step 1** (part 1). [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] with $n = 2$ and [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]] with $F = |\mathcal M|^2$: $\frac{1}{2m_A}\cdot\frac{|\mathbf p_1|}{16\pi^2m_A} = \frac{|\mathbf p_1|}{32\pi^2m_A^2}$ (Yu (6.382)).
>
> **Step 2** (the width; part 2). By [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] with $n = 2$ and [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]] with $F = |\mathcal M|^2$ constant in $\Omega$:
>
> $$
> \Gamma = \frac{1}{S_{\rm id}}\,\frac{1}{2m_A}\int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2m_A}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{1}{2m_A}\cdot4\pi\cdot\frac{|\mathbf p_1|}{16\pi^2m_A}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathbf p_1|}{8\pi m_A^2}|\mathcal M|^2
> $$
>
> (Yu (6.383)).
>
> With $|\mathbf p_1| = \frac{m_A}{2}\lambda^{1/2}(1, \frac{m_1^2}{m_A^2}, \frac{m_2^2}{m_A^2})$ ([[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]]): $\frac{m_A}{2}\cdot\frac{1}{8\pi m_A^2} = \frac{1}{16\pi m_A}$, the second form.
>
> **Step 3** (part 3). Identical particles have equal masses; so $m_1 \ne m_2$ excludes them, and no final state is counted twice.
>
> ⚑ By-product: for $1 \to 2$, $[\mathcal M] = 4 - 3 = 1$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]): $\mathcal M$ has the dimension of a mass, and $[\Gamma] = 2 + 1 - 2 = 1$ → [[§C6b.5 Decay Widths#^thm-c6b-5-7|Theorem §C6b.5.7]].
>
> **What the derivation shows.**
> - For direction-independent $|\mathcal M|^2$ the angular integral is the factor $4\pi$; otherwise part 1 must be integrated.

^der-c6b-6-2

*Uses:* [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]], [[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!theorem] Theorem §C6b.6.3: Two-Body Decay into Equal Masses
> For $m_1 = m_2 = m$ in [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]], with $\beta = \sqrt{1 - 4m^2/m_A^2}$,
>
> $$
> |\mathbf p_1| = \frac{m_A}{2}\,\beta, \qquad \int d\Pi_2 = \frac{\beta}{8\pi}, \qquad \Gamma = \frac{1}{S_{\rm id}}\,\frac{|\mathcal M|^2}{16\pi m_A}\,\beta
> $$
>
> for direction-independent $|\mathcal M|^2$, with $S_{\rm id} = 2$ if the two products are identical. The phase space, and $\Gamma$ at fixed $|\mathcal M|^2$, vanish like $\beta$ at the threshold $m_A \to 2m$.
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there: the kinematics exactly, $\Gamma$ at lowest order in the decaying interaction.
>
> *Source: Yu §6.5.5, eqs. (6.384)–(6.385) (page image checked: (6.385) the equal-mass form, "如果两个末态粒子是全同粒子，则 $\mathcal S = 2$") · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Two-body decays (filled in)", citing "Yu's (6.385)": correct) · PHY 513, Problem Set 8, Problem 4 (the user's $\int d\Pi_2 = p_\ast/(4\pi M)$)*

^thm-c6b-6-3

> [!derivation]- Derivation
> **Step 1** (equal masses). $\lambda(m_A^2, m^2, m^2) = m_A^4 + m^4 + m^4 - 2m_A^2m^2 - 2m_A^2m^2 - 2m^4 = m_A^4 - 4m_A^2m^2 = m_A^4\beta^2$, so (Yu (6.384), with $\lambda^{1/2}(1, \frac{m^2}{m_A^2}, \frac{m^2}{m_A^2}) = \beta$)
>
> $$
> |\mathbf p_1| = \frac{m_A^2\beta}{2m_A} = \frac{m_A}{2}\beta, \qquad \int d\Pi_2 = \frac{m_A\beta/2}{4\pi m_A} = \frac{\beta}{8\pi}, \qquad \Gamma = \frac{1}{S_{\rm id}}\,\frac{m_A\beta/2}{8\pi m_A^2}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathcal M|^2}{16\pi m_A}\beta
> $$
>
> (Yu (6.385)). Directly: $E_1 = E_2 = m_A/2$ and $|\mathbf p_1| = \sqrt{m_A^2/4 - m^2}$, the same.
>
> **What the derivation shows.**
> - The phase-space factor vanishes like $\beta$ at threshold $m_A \to m_1 + m_2$ (now in the statement; [[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]).

^der-c6b-6-3

*Uses:* [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-2|Theorem §C6b.6.2]], [[§C6b.4 Two-Body Scattering Kinematics#^def-c6b-4-1|Def. §C6b.4.1]]

> [!model] Model §C6b.6.4: Two Scalar Fields with a Φφ² Coupling
> Two real scalar fields, $\Phi$ of mass $M$ and $\phi$ of mass $m$:
>
> $$
> \mathcal L = \tfrac12(\partial_\mu\Phi)^2 - \tfrac12M^2\Phi^2 + \tfrac12(\partial_\mu\phi)^2 - \tfrac12m^2\phi^2 - \mu\,\Phi\phi^2 ,
> $$
>
> each free part the field of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; $[\mu] = 1$; vertex $-2i\mu$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Assumptions:*
> 1. $M > 2m$: $\Phi$ can decay into $\phi\phi$, so it is not a stable asymptotic particle (outside assumption 2 of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]]).
> 2. The potential is not bounded below: at $\Phi = -s$ the coefficient of $\phi^2$ is $\frac{m^2}{2} - \mu s < 0$ for $s > m^2/(2\mu)$ (derived here, not from a source). The model is used at lowest order in $\mu$ only.
> 3. Otherwise as [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], assumptions 2 and 5.
>
> An instance of Model §C6a.0.3, at lowest order; the decay setup is [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]].
>
> *Source: PHY 513, Problem Set 8, Problem 4 (statement: the Lagrangian, "allows a Φ-particle to decay into two ϕ's, provided that M > 2m", "to the lowest order in µ") · PS Problem 4.2*

^mod-c6b-6-4

> [!example] Example §C6b.6.1: Φ → φφ, the Lifetime at Lowest Order
> ![[ph-qft-c6b-11-2.svg]]
>
> For $\mathcal L = \frac12(\partial_\mu\Phi)^2 - \frac12M^2\Phi^2 + \frac12(\partial_\mu\phi)^2 - \frac12m^2\phi^2 - \mu\,\Phi\phi^2$ ([[§C6b.6 Decay Kinematics#^mod-c6b-6-4|Model §C6b.6.4]]) with $M > 2m$, to lowest order in $\mu$:
>
> $$
> \mathcal M = -2\mu, \qquad \Gamma = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}}, \qquad \tau = \frac1\Gamma = \frac{8\pi M^2}{\mu^2\sqrt{M^2 - 4m^2}} .
> $$
>
> **Step 1** (the amplitude). No derivatives, so $\hat{\mathcal H}_I = -\mathcal L_I = \mu\hat\Phi\hat\phi^2$ and $-i\int dt\,\hat H_I = -i\mu\int d^4x\,\hat\Phi_I\hat\phi_I^2$. With $\hat b$, $\hat a$ the annihilators of $\hat\Phi$, $\hat\phi$ and relativistically normalized states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $|\mathbf K\rangle_\Phi = \sqrt{2E^\Phi_{\mathbf K}}\,\hat b^\dagger_{\mathbf K}|0\rangle$, $|\mathbf p_1\mathbf p_2\rangle = \sqrt{2E_{\mathbf p_1}}\sqrt{2E_{\mathbf p_2}}\,\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle$ (as needed by [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]):
>
> $$
> \mathcal A = \langle\mathbf p_1\mathbf p_2|\,T\Bigl\{\exp\Bigl[-i\mu\int d^4x\,\hat\Phi_I(x)\hat\phi_I(x)^2\Bigr]\Bigr\}|\mathbf K\rangle_\Phi
> $$
>
> ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]]).
>
> **Step 2** (order zero). $\langle\mathbf p_1\mathbf p_2|\mathbf K\rangle_\Phi \propto \langle0|\hat a_{\mathbf p_1}\hat a_{\mathbf p_2}\hat b^\dagger_{\mathbf K}|0\rangle = \langle0|\hat b^\dagger_{\mathbf K}\hat a_{\mathbf p_1}\hat a_{\mathbf p_2}|0\rangle = 0$: different fields commute, and $\hat a|0\rangle = 0$.
>
> **Step 3** (order one, the $\Phi$ end). One time, so $T$ acts trivially: $\mathcal A^{(1)} = -i\mu\int d^4x\,\langle\mathbf p_1\mathbf p_2|\hat\Phi_I(x)\hat\phi_I(x)^2|\mathbf K\rangle_\Phi$. Split $\hat\Phi_I = \hat\Phi_I^+ + \hat\Phi_I^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]). $\hat\Phi_I^-|\mathbf K\rangle_\Phi$ has two $\Phi$ quanta, which $\hat\phi_I^2$ cannot remove: no overlap with $\langle\mathbf p_1\mathbf p_2|$. With $\hat\Phi_I^+|0\rangle = 0$ and $[\hat b_{\mathbf q}, \hat b^\dagger_{\mathbf K}] = (2\pi)^3\delta^3(\mathbf q - \mathbf K)$,
>
> $$
> \hat\Phi_I^+(x)|\mathbf K\rangle_\Phi = \sqrt{2E^\Phi_{\mathbf K}}\,[\hat\Phi_I^+(x), \hat b^\dagger_{\mathbf K}]|0\rangle = \sqrt{2E^\Phi_{\mathbf K}}\int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E^\Phi_{\mathbf q}}}(2\pi)^3\delta^3(\mathbf q - \mathbf K)|0\rangle = e^{-iK\cdot x}|0\rangle, \quad K^0 = E^\Phi_{\mathbf K} .
> $$
>
> **Step 4** (order one, the $\phi$ end). In $\hat\phi_I\hat\phi_I = (\hat\phi_I^+ + \hat\phi_I^-)(\hat\phi_I^+ + \hat\phi_I^-)$ acting on $|0\rangle$, terms with $\hat\phi_I^+$ on the right vanish, and $\hat\phi_I^+\hat\phi_I^-|0\rangle = [\hat\phi_I^+, \hat\phi_I^-]|0\rangle$ is a number times $|0\rangle$, orthogonal to $\langle\mathbf p_1\mathbf p_2|$. Only $\hat\phi_I^-\hat\phi_I^-$ remains; each of $\hat a_{\mathbf p_1}$, $\hat a_{\mathbf p_2}$ contracts with one of the two fields, in $2$ ways, each giving $\sqrt{2E_{\mathbf p_i}}[\hat a_{\mathbf p_i}, \hat\phi_I^-(x)] = e^{ip_i\cdot x}$ (the one-particle case of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]; general form [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]):
>
> $$
> \langle\mathbf p_1\mathbf p_2|\hat\phi_I^-(x)\hat\phi_I^-(x)|0\rangle = e^{ip_1\cdot x}e^{ip_2\cdot x} + e^{ip_2\cdot x}e^{ip_1\cdot x} = 2\,e^{i(p_1 + p_2)\cdot x}, \qquad p_i^0 = E_{\mathbf p_i} .
> $$
>
> **Step 5** ($\mathcal M$). With [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]],
>
> $$
> \mathcal A^{(1)} = -2i\mu\int d^4x\,e^{i(p_1 + p_2 - K)\cdot x} = -2i\mu\,(2\pi)^4\delta^4(K - p_1 - p_2) ,
> $$
>
> and comparing with $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]): $i\mathcal M = -2i\mu$, $\mathcal M = -2\mu$, momentum independent (no derivatives in the vertex). The $2 = 2!$ is the vertex factor's count of ways to attach two distinct lines to the two $\phi$ legs ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> **Step 6** (identical particles). $|\mathbf p_1\mathbf p_2\rangle = |\mathbf p_2\mathbf p_1\rangle$, so integrating $\mathbf p_1$ and $\mathbf p_2$ independently counts each final state twice: $S_{\rm id} = 2!$ ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]; the $\frac{1}{n!}$ of the $n$-particle measure, [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]]).
>
> **Step 7** ($\int d\Pi_2$ with $\delta(f(p))$, the user's evaluation). At rest, $\mathbf p_2 = -\mathbf p_1$ by the $\delta^3$, $E_{\mathbf p_2} = E_{\mathbf p_1} \equiv E_p$, $p = |\mathbf p_1|$, and $d^3p_1 = p^2\,dp\,d\Omega$:
>
> $$
> \int d\Pi_2 = \int\frac{p^2\,dp\,d\Omega}{(2\pi)^3}\,\frac{1}{4E_p^2}\,2\pi\,\delta(M - 2E_p) .
> $$
>
> With $f(p) = M - 2\sqrt{p^2 + m^2}$ on $p \in [0, \infty)$, the only root is $p_\ast = \sqrt{M^2/4 - m^2} = \frac M2\sqrt{1 - 4m^2/M^2}$ ($E_\ast = M/2$; real for $M > 2m$; $-p_\ast$ is outside the range), and $f'(p) = -2p/E_p$, so ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2)
>
> $$
> \delta(M - 2E_p) = \frac{E_\ast}{2p_\ast}\,\delta(p - p_\ast), \qquad \int d\Pi_2 = 4\pi\cdot\frac{2\pi}{(2\pi)^3}\cdot\frac{p_\ast^2}{4E_\ast^2}\cdot\frac{E_\ast}{2p_\ast} = \frac{p_\ast}{8\pi E_\ast} = \frac{p_\ast}{4\pi M} = \frac{1}{8\pi}\sqrt{1 - \frac{4m^2}{M^2}} ,
> $$
>
> [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]].
>
> **Step 8** (width and lifetime). $|\mathcal M|^2 = 4\mu^2$ is constant:
>
> $$
> \Gamma = \frac12\cdot\frac{1}{2M}\cdot4\mu^2\cdot\frac{1}{8\pi}\sqrt{1 - \frac{4m^2}{M^2}} = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}}, \qquad \tau = \frac{8\pi M}{\mu^2}\Bigl(1 - \frac{4m^2}{M^2}\Bigr)^{-1/2} = \frac{8\pi M^2}{\mu^2\sqrt{M^2 - 4m^2}} ;
> $$
>
> the same from [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]]: $\frac12\frac{4\mu^2}{16\pi M}\beta$. $[\mu] = 1$ ($[\Phi\phi^2] = 3$), $[\Gamma] = 2 - 1 = 1$.
>
> *Source: PHY 513, Problem Set 8, Problem 4 (= PS Problem 4.2; the user's solution, Steps 1–8 as written there) · Yu §6.5.5, eq. (6.385)*

^ex-c6b-6-1

## ★ Three-body decays

> [!theorem]- ★ Theorem §C6b.6.5: Three-Body Phase Space at Rest
> Let $A$ (mass $m_A$, at rest) decay into three particles, and let the integrand depend on the final momenta only through the energies $E_1$, $E_3$ (as $|\mathcal M|^2$ does for spin 0 or spin-averaged decays, [[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]]). The three momenta lie in one plane, $\mathbf p_1 + \mathbf p_2 + \mathbf p_3 = \mathbf 0$, and
>
> $$
> \int d\Pi_3\,F(E_1, E_3) = \frac{1}{4(2\pi)^3}\int dE_1\int dE_3\,F(E_1, E_3) ,
> $$
>
> over the pairs $(E_1, E_3)$ that energy conservation allows ([[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]]): the measure is flat in the two energies.
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* the kinematics exactly; integrands independent of the orientation of the decay plane.
>
> *Source: Yu §6.5.5 (2), eqs. (6.386)–(6.395), Fig. 6.6(a) (page images checked)*

^thm-c6b-6-5

> [!derivation]- Derivation
> **Step 1** (the $\mathbf p_2$ integral). [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]] with $P = (m_A, \mathbf 0)$ (Yu (6.387)); the $\delta^3$ sets $\mathbf p_2 = -\mathbf p_1 - \mathbf p_3$, so the three momenta are coplanar. The constants: $(2\pi)^4/(2\pi)^9 = (2\pi)^{-5}$ and $\frac{1}{2E_1\,2E_2\,2E_3} = \frac{1}{8E_1E_2E_3}$ (Yu (6.388)):
>
> $$
> \int d\Pi_3\,F = \frac{1}{8(2\pi)^5}\int\frac{d^3p_1\,d^3p_3}{E_1E_2E_3}\,\delta(m_A - E_1 - E_2 - E_3)\,F , \qquad E_2 = \sqrt{m_2^2 + |\mathbf p_1 + \mathbf p_3|^2} .
> $$
>
> **Step 2** (spherical coordinates and energies). $d^3p_j = |\mathbf p_j|^2d|\mathbf p_j|\,d\Omega_j$, and differentiating $|\mathbf p_j|^2 + m_j^2 = E_j^2$ gives $|\mathbf p_j|\,d|\mathbf p_j| = E_j\,dE_j$ (Yu (6.389)), so $\frac{|\mathbf p_j|^2d|\mathbf p_j|}{E_j} = |\mathbf p_j|\,dE_j$ for $j = 1, 3$ (Yu (6.390)):
>
> $$
> \int d\Pi_3\,F = \frac{1}{8(2\pi)^5}\int dE_1\int dE_3\int d\Omega_1\int d\Omega_3\,\frac{|\mathbf p_1||\mathbf p_3|}{E_2}\,\delta(m_A - E_1 - E_2 - E_3)\,F .
> $$
>
> **Step 3** (the angle between $\mathbf p_1$ and $\mathbf p_3$). Measure $\Omega_3$ from the direction of $\mathbf p_1$: $d\Omega_3 = \sin\theta_{13}\,d\theta_{13}\,d\varphi_3 = -d\cos\theta_{13}\,d\varphi_3$ (Yu (6.391)). At fixed $E_1$, $E_3$ the magnitudes $|\mathbf p_1| = \sqrt{E_1^2 - m_1^2}$, $|\mathbf p_3| = \sqrt{E_3^2 - m_3^2}$ are fixed, and only $E_2$ depends on $\cos\theta_{13}$ (Yu (6.392)–(6.393)):
>
> $$
> E_2 = \sqrt{m_2^2 + |\mathbf p_1|^2 + |\mathbf p_3|^2 + 2|\mathbf p_1||\mathbf p_3|\cos\theta_{13}} , \qquad \frac{\partial E_2}{\partial\cos\theta_{13}} = \frac{2|\mathbf p_1||\mathbf p_3|}{2E_2} = \frac{|\mathbf p_1||\mathbf p_3|}{E_2} .
> $$
>
> **Step 4** (the energy delta). As a function of $c = \cos\theta_{13}$, $m_A - E_1 - E_2 - E_3$ has derivative $-|\mathbf p_1||\mathbf p_3|/E_2$, of modulus $|\mathbf p_1||\mathbf p_3|/E_2$ (Yu (6.394)); by [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, if its zero $c^\ast$ lies in $[-1, 1]$ (the allowed pairs $(E_1, E_3)$),
>
> $$
> \int_{-1}^1dc\,\frac{|\mathbf p_1||\mathbf p_3|}{E_2}\,\delta(m_A - E_1 - E_2 - E_3) = \frac{|\mathbf p_1||\mathbf p_3|}{E_2}\cdot\frac{E_2}{|\mathbf p_1||\mathbf p_3|} = 1 .
> $$
>
> **Step 5** (the remaining angles). $F$ depends on $E_1$, $E_3$ only: $\int_0^{2\pi}d\varphi_3 = 2\pi$, $\int d\Omega_1 = 4\pi$, and (Yu (6.395))
>
> $$
> \frac{2\pi\cdot4\pi}{8(2\pi)^5} = \frac{8\pi^2}{8\cdot32\pi^5} = \frac{1}{32\pi^3} = \frac{1}{4(2\pi)^3} .
> $$
>
> **What the derivation shows.**
> - Of the nine final momentum components, three orientation angles of the decay plane and the angle $\theta_{13}$ are fixed or integrated trivially; the energies $E_1$, $E_3$ are the two variables that carry the dynamics.

^der-c6b-6-5

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]]

> [!theorem]- ★ Theorem §C6b.6.6: The Three-Body Width in the Energies
> For $A$ at rest decaying into three particles with direction-independent $|\mathcal M|^2$,
>
> $$
> \Gamma_f = \frac{1}{S_{\rm id}}\,\frac{1}{(2\pi)^3}\,\frac{1}{8m_A}\int_{E_1^{\min}}^{E_1^{\max}}dE_1\int_{E_3^{\min}}^{E_3^{\max}}dE_3\,|\mathcal M(E_1, E_3)|^2 ,
> $$
>
> with $|\mathcal M|^2$ written as a function of $E_1$, $E_3$ and the limits of the allowed region ([[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]], with [[§C6b.6 Decay Kinematics#^thm-c6b-6-7|Theorem §C6b.6.7]], 1).
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there: lowest order in the decaying interaction.
>
> *Source: Yu §6.5.5 (2), eq. (6.396) (page image checked: "需要把不变振幅 $\mathcal M$ 表达为 $E_1$ 和 $E_3$ 的函数，而且要仔细考虑 $E_1$ 和 $E_3$ 的积分上下限")*

^thm-c6b-6-6

> [!derivation]- Derivation
> **Step 1** (the width). [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] with $n = 3$ (Yu (6.386)): $\Gamma_f = \frac{1}{S_{\rm id}}\frac{1}{2m_A}\int d\Pi_3\,|\mathcal M|^2$.
>
> **Step 2** ($|\mathcal M|^2$ as a function of $E_1$, $E_3$). For spinless particles $|\mathcal M|^2$ depends on the scalar products ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]); with $p_A = p_1 + p_2 + p_3$ and $p_A = (m_A, \mathbf 0)$,
>
> $$
> p_A\cdot p_j = m_AE_j , \quad E_2 = m_A - E_1 - E_3 , \quad 2p_1\cdot p_2 = (p_A - p_3)^2 - m_1^2 - m_2^2 = m_A^2 + m_3^2 - 2m_AE_3 - m_1^2 - m_2^2 ,
> $$
>
> and likewise $2p_2\cdot p_3$ (with $E_1$) and $2p_1\cdot p_3$ (with $E_2$): every scalar product is a function of $E_1$, $E_3$.
>
> **Step 3** (insert the phase space). [[§C6b.6 Decay Kinematics#^thm-c6b-6-5|Theorem §C6b.6.5]] with $F = |\mathcal M|^2$: $\frac{1}{2m_A}\cdot\frac{1}{4(2\pi)^3} = \frac{1}{(2\pi)^3}\frac{1}{8m_A}$.
>
> **What the derivation shows.**
> - A three-body width is a two-dimensional integral; the energies are inconvenient variables, and the invariant masses of [[§C6b.6 Decay Kinematics#^def-c6b-6-1|Def. §C6b.6.1]] replace them.

^der-c6b-6-6

*Uses:* [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-5|Theorem §C6b.6.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]

> [!definition]- ★ Definition §C6b.6.1: Invariant Masses of a Pair
> For a decay $A \to 1 + 2 + 3$ the **invariant mass** of the pair $(1, 2)$ is $\sqrt{s_{12}}$, with
>
> $$
> s_{12} \equiv (p_1 + p_2)^2 , \qquad \text{likewise } s_{23} \equiv (p_2 + p_3)^2 :
> $$
>
> the mass of the "effective particle" of four-momentum $p_1 + p_2$, equal to the centre-of-mass energy ([[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]) of the pair. Both are Lorentz invariants.
>
> *Model:* any (kinematics); *applies:* any three-body final state.
>
> *Source: Yu §6.5.5 (2), eqs. (6.397)–(6.398) (page image checked: "$\sqrt{s_{12}}$ 相当于这个等效粒子的质量，称为粒子 1 和 2 的不变质量 (invariant mass)，它也是粒子 1 和 2 组成的系统的质心能")*

^def-c6b-6-1

> [!theorem]- ★ Theorem §C6b.6.7: The Three-Body Width in the Invariant Masses
> 1. In the rest frame of $A$,
>
> $$
> s_{12} = m_A^2 + m_3^2 - 2m_AE_3 , \qquad s_{23} = m_A^2 + m_1^2 - 2m_AE_1 , \qquad ds_{12} = -2m_A\,dE_3 , \qquad ds_{23} = -2m_A\,dE_1 .
> $$
>
> 2. The width of ★ [[§C6b.6 Decay Kinematics#^thm-c6b-6-6|Theorem §C6b.6.6]] becomes
>
> $$
> \Gamma_f = \frac{1}{S_{\rm id}}\,\frac{1}{256\pi^3m_A^3}\int_{s_{12}^{\min}}^{s_{12}^{\max}}ds_{12}\int_{s_{23}^{\min}}^{s_{23}^{\max}}ds_{23}\,|\mathcal M(s_{12}, s_{23})|^2 ,
> $$
>
> over the Dalitz region ([[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]]), with $|\mathcal M|^2$ written as a function of the invariant masses ([[§C6b.6 Decay Kinematics#^def-c6b-6-1|Def. §C6b.6.1]]).
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there.
>
> *Source: Yu §6.5.5 (2), eqs. (6.397)–(6.400) (page image checked; (6.400) boxed)*

^thm-c6b-6-7

> [!derivation]- Derivation
> **Step 1** (part 1). Momentum conservation $p_1 + p_2 = p_A - p_3$; square, with $p_A^2 = m_A^2$, $p_3^2 = m_3^2$ and $p_A\cdot p_3 = m_AE_3$ at rest (Yu (6.397)):
>
> $$
> s_{12} = (p_A - p_3)^2 = m_A^2 + m_3^2 - 2p_A\cdot p_3 = m_A^2 + m_3^2 - 2m_AE_3 ,
> $$
>
> and the same with $1 \leftrightarrow 3$ for $s_{23} = (p_A - p_1)^2$ (Yu (6.398)); differentiating at fixed masses gives (Yu (6.399)) $ds_{12} = -2m_A\,dE_3$, $ds_{23} = -2m_A\,dE_1$.
>
> **Step 2** (change of variables; part 2). $(E_1, E_3) \mapsto (s_{23}, s_{12})$ is linear with Jacobian $|\partial(s_{23}, s_{12})/\partial(E_1, E_3)| = (2m_A)^2$, so $dE_1\,dE_3 = \frac{ds_{12}\,ds_{23}}{4m_A^2}$ (the minus signs reverse the limits, which the absolute value absorbs). In [[§C6b.6 Decay Kinematics#^thm-c6b-6-6|Theorem §C6b.6.6]]:
>
> $$
> \frac{1}{(2\pi)^3}\,\frac{1}{8m_A}\cdot\frac{1}{4m_A^2} = \frac{1}{8\pi^3\cdot32m_A^3} = \frac{1}{256\pi^3m_A^3} .
> $$
>
> **What the derivation shows.**
> - Uniform density in $(E_1, E_3)$ means uniform density in $(s_{12}, s_{23})$: a plot of decay events in these variables (a Dalitz plot) is flat where $|\mathcal M|^2$ is constant, and its structure shows $|\mathcal M|^2$ directly.

^der-c6b-6-7

*Uses:* [[§C6b.6 Decay Kinematics#^thm-c6b-6-6|Theorem §C6b.6.6]], [[§C6b.6 Decay Kinematics#^def-c6b-6-1|Def. §C6b.6.1]]

> [!theorem]- ★ Theorem §C6b.6.8: The Dalitz Region
> The allowed values of $(s_{12}, s_{23})$ in $A \to 1 + 2 + 3$ are
>
> $$
> (m_1 + m_2)^2 \le s_{12} \le (m_A - m_3)^2 , \qquad s_{23}^{\min}(s_{12}) \le s_{23} \le s_{23}^{\max}(s_{12}) ,
> $$
>
> $$
> s_{23}^{\max,\min} = (\tilde E_2 + \tilde E_3)^2 - \Bigl(\sqrt{\tilde E_2^2 - m_2^2} \mp \sqrt{\tilde E_3^2 - m_3^2}\Bigr)^2 , \qquad \tilde E_2 = \frac{s_{12} + m_2^2 - m_1^2}{2\sqrt{s_{12}}} , \qquad \tilde E_3 = \frac{m_A^2 - s_{12} - m_3^2}{2\sqrt{s_{12}}} ,
> $$
>
> where $\tilde E_2$, $\tilde E_3$ are the energies of particles 2 and 3 in the centre-of-mass frame of the pair $(1, 2)$. All limits are Lorentz invariant. The region for $m_A = 4m_1 = 5m_2 = 8m_3$ is drawn below.
>
> *Model:* any (kinematics); *applies:* any three-body decay.
>
> *Source: Yu §6.5.5 (2), eqs. (6.401)–(6.411), Fig. 6.6(b), Fig. 6.7 (page images checked)*

^thm-c6b-6-8

> [!derivation]- Derivation
> **Step 1** (energies in the rest frame of a four-momentum). For a timelike $P$, in its rest frame $P = (\sqrt{P^2}, \mathbf 0)$, so the energy of a particle of momentum $p$ there is $\frac{p\cdot P}{\sqrt{P^2}}$, an invariant expression.
>
> **Step 2** ($\tilde E_2$, $\tilde E_3$). Take $P = p_1 + p_2$, $P^2 = s_{12}$, and use $2p_1\cdot p_2 = s_{12} - m_1^2 - m_2^2$ and $2p_A\cdot p_3 = m_A^2 + m_3^2 - s_{12}$ (square $p_1 + p_2 = p_A - p_3$):
>
> $$
> \tilde E_2 = \frac{p_2\cdot(p_1 + p_2)}{\sqrt{s_{12}}} = \frac{p_1\cdot p_2 + m_2^2}{\sqrt{s_{12}}} = \frac{s_{12} + m_2^2 - m_1^2}{2\sqrt{s_{12}}} , \qquad \tilde E_3 = \frac{p_3\cdot(p_A - p_3)}{\sqrt{s_{12}}} = \frac{p_A\cdot p_3 - m_3^2}{\sqrt{s_{12}}} = \frac{m_A^2 - s_{12} - m_3^2}{2\sqrt{s_{12}}} .
> $$
>
> The first is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], 1, with $E_{\rm cm} \to \sqrt{s_{12}}$ (Yu (6.401)); Yu obtains the second by squaring an equation for $\tilde E_3$ in the pair frame, where $\tilde{\mathbf p}_3 = \tilde{\mathbf p}_A$ (Yu (6.402)–(6.404)).
>
> **Step 3** ($s_{23}$ at fixed $s_{12}$). In the pair frame (Yu (6.405)–(6.406)),
>
> $$
> s_{23} = (\tilde E_2 + \tilde E_3)^2 - |\tilde{\mathbf p}_2 + \tilde{\mathbf p}_3|^2 , \qquad |\tilde{\mathbf p}_2 + \tilde{\mathbf p}_3|^2 = |\tilde{\mathbf p}_2|^2 + |\tilde{\mathbf p}_3|^2 + 2|\tilde{\mathbf p}_2||\tilde{\mathbf p}_3|\cos\tilde\theta_{23} ,
> $$
>
> with $|\tilde{\mathbf p}_j| = \sqrt{\tilde E_j^2 - m_j^2}$ fixed by $s_{12}$. Every angle $\tilde\theta_{23} \in [0, \pi]$ occurs: at fixed $s_{12}$ the direction of $\tilde{\mathbf p}_2 = -\tilde{\mathbf p}_1$ relative to $\tilde{\mathbf p}_3$ is free, as the direction of $\mathbf p_1$ in [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]; so $s_{23}$ fills the interval between $\cos\tilde\theta_{23} = 1$, where $|\tilde{\mathbf p}_2 + \tilde{\mathbf p}_3| = |\tilde{\mathbf p}_2| + |\tilde{\mathbf p}_3|$ and $s_{23}$ is smallest (Yu (6.407)), and $\cos\tilde\theta_{23} = -1$, where it is largest (Yu (6.408)).
>
> **Step 4** (the range of $s_{12}$). In the pair frame $s_{12} = (\tilde E_1 + \tilde E_2)^2 \ge (m_1 + m_2)^2$, with equality when both are at rest there (Yu (6.409)–(6.410)). In the rest frame of $A$, $s_{12} = m_A^2 + m_3^2 - 2m_AE_3$ ([[§C6b.6 Decay Kinematics#^thm-c6b-6-7|Theorem §C6b.6.7]], 1) is largest at the smallest $E_3 = m_3$: $s_{12}^{\max} = (m_A - m_3)^2$ (Yu (6.411)).
>
> **Step 5** (invariance). Every limit is a function of $s_{12}$ and the masses only.
>
> **What the derivation shows.**
> - The boundary touches the lines $s_{23} = (m_2 + m_3)^2$ and $s_{23} = (m_A - m_1)^2$, the ranges of $s_{23}$ obtained by exchanging the roles of the particles (dash-dotted in the figure).

^der-c6b-6-8

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.6 Decay Kinematics#^thm-c6b-6-7|Theorem §C6b.6.7]], [[§C6b.6 Decay Kinematics#^def-c6b-6-1|Def. §C6b.6.1]]

![[ph-qft-c6b-6-1.svg]]
*The Dalitz region of a three-body decay for $m_A = 4m_1 = 5m_2 = 8m_3$ (as Yu Fig. 6.7), in units of $m_A^2$: for each $s_{12}$ between $(m_1 + m_2)^2$ and $(m_A - m_3)^2$, $s_{23}$ runs from $s_{23}^{\min}$ (blue) to $s_{23}^{\max}$ (red) of Theorem §C6b.6.8; the dash-dotted lines are the extreme values of $s_{12}$ and $s_{23}$. With constant $|\mathcal M|^2$ the decay events fill the shaded region uniformly (Theorem §C6b.6.7). Added figure, computed from the limits (tools/yu-phaseB/figs/dalitz.py).*

> [!remark]- Connections
> - Two-body decay kinematics is two-body scattering kinematics with $E_{\rm cm} = m_A$; the energies of a pair in its own rest frame (Dalitz limits) are the same formula with $E_{\rm cm} = \sqrt{s_{12}}$ — [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]].
> - The first-order decay amplitudes of the Feynman rules that feed these widths: the kinematic filter at first order is the decay threshold — [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]], [[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]; the fermion decay $\phi \to f\bar f$ — [[§C6d.4 First Order|§C6d.4]].
> - The flat Dalitz density is the three-body analogue of the isotropic two-body decay: the phase space carries no dynamics, so any structure in a Dalitz plot is $|\mathcal M|^2$ — [[§C6b.5 Decay Widths#^thm-c6b-5-10|Theorem §C6b.5.10]].
