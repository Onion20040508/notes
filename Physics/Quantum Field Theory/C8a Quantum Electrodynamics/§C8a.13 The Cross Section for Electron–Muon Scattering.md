---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.13
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution|§C8a.12]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.14 Crossing Symmetry and Mandelstam Variables|§C8a.14]] →

*Sources: PHY 513 Lecture 21 (Larsen, 18 Nov 2026, "Crossing Symmetry"; a recorded lecture in three parts), slides 11–14 (Part B), and recording, part B · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.4, pp. 154–155, the kinematic figure of p. 154 and eqs. (5.62)–(5.66) (page images checked).*

What does electron–muon scattering look like to an experiment? The invariant form of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]] is turned into a cross section in the same way as for annihilation ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production|§C8a.8]]): choose the centre-of-mass frame, write the momenta ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]]) and the invariants ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]), insert them into the squared amplitude ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]]) and into the general cross-section formula ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]]). The kinematic factors are simple; the structure is all in the amplitude. Two limits show what it contains: at high energy the angular dependence $\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]]), and at small angles the growth $1/\theta^4$, which makes the total cross section infinite and comes from a virtual photon that is nearly on its mass shell ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]). The general cross-section formula is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]; nothing about it is rederived here.

**Setup.** [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] at order $e^2$, unpolarized ([[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]]), in the centre-of-mass frame ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]) with the cross section of two colliding beams ([[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]). The electron mass is neglected throughout and the muon mass is kept, as in the lecture; the last two theorems neglect the muon mass as well.

*Conventions* ([[Larsen PHY 513]]): momenta $p_1, p_2 \to p_1', p_2'$ as in [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution|§C8a.12]]; $\hat{\mathbf z}$ along the incoming electron; $\theta$ is the angle between the outgoing and the incoming electron; $E$ is the energy of the muon, before and after; $\alpha = e^2/4\pi$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^def-c1a-8-1|Def. §C1a.8.1]]); $d\Omega = \sin\theta\,d\theta\,d\varphi$ for the direction of the outgoing electron. **The letter $k$ is a number in this section,** the magnitude of the three-momentum of each particle in the centre-of-mass frame and also the energy of the massless electron, as on the slides and in PS; $\mathbf k$ is the three-momentum of the outgoing electron, $|\mathbf k| = k$. In [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon|§C8a.6]]–[[§C8a.8 The Unpolarized Cross Section for Muon Pair Production|§C8a.8]] the same letter was the four-momentum of the outgoing $\mu^-$ of the annihilation process.

## The centre-of-mass frame

> [!theorem] Theorem §C8a.13.1: The Momenta of Electron–Muon Scattering in the Centre-of-Mass Frame
> ![[ph-qft-c8-19-1.svg]]
> *The momenta in the centre-of-mass frame (after PHY 513 Lecture 21, slide 11, and PS p. 154). A sketch of three-momenta in space, not a Feynman diagram.*
>
> In the centre-of-mass frame of $e^-(p_1) + \mu^-(p_2) \to e^-(p_1') + \mu^-(p_2')$ with $m_e = 0$ and the electron along $\hat{\mathbf z}$:
>
> $$
> p_1 = (k, k\hat{\mathbf z}) , \qquad p_2 = (E, -k\hat{\mathbf z}) , \qquad p_1' = (k, \mathbf k) , \qquad p_2' = (E, -\mathbf k) ,
> $$
>
> $$
> |\mathbf k| = k , \qquad \mathbf k\cdot\hat{\mathbf z} = k\cos\theta , \qquad E = \sqrt{k^2 + m_\mu^2} , \qquad E_{\rm cm} = E + k .
> $$
>
> 1. The electron and the muon come in with opposite three-momenta of the same magnitude $k$ and with different energies: $k$ for the massless electron, $E$ for the muon.
> 2. They go out back to back with the same magnitude $k$: the scattering is elastic, and in this frame neither particle changes its energy. Only the directions change, by the angle $\theta$.
> 3. In terms of the total energy, $k = \frac{E_{\rm cm}^2 - m_\mu^2}{2E_{\rm cm}}$ and $E = \frac{E_{\rm cm}^2 + m_\mu^2}{2E_{\rm cm}}$.
>
> *Equivalently,* this is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]] with $m_A = m_1 = 0$ and $m_B = m_2 = m_\mu$: the initial and the final pair have the same two masses, hence the same momentum.
>
> *Model:* any (kinematics); *applies:* on-shell momenta, $m_e = 0$, any $k > 0$.
>
> *Source: PHY 513 Lecture 21, slide 11 ("$p_1 = (k, k\hat z)$, $p_2 = (E, -k\hat z)$, $p_1' = (k, \vec k)$, $p_2' = (E, -\vec k)$. Kinematics in the center of mass system ($m_e$ neglected)"), slide 12 ("Notation: $k \equiv \sqrt{E^2 - m_\mu^2}$, $E_{\rm cm} = E + k$"), and recording, part B · PS §5.4, p. 154 (the figure with "$E^2 = k^2 + m_\mu^2$, $\mathbf k\cdot\hat z = k\cos\theta$, $E + k = E_{\rm cm}$") · item 3 from [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]*

^thm-c8a-13-1

> [!derivation]- Derivation
> **Step 1** (the initial state). The frame is defined by $\mathbf p_1 + \mathbf p_2 = \mathbf 0$ ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]): with $\mathbf p_1 = k\hat{\mathbf z}$, $\mathbf p_2 = -k\hat{\mathbf z}$. The electron is massless, so its energy is $|\mathbf p_1| = k$; the muon has $E = \sqrt{k^2 + m_\mu^2}$. The total energy is $E_{\rm cm} = E + k$.
>
> **Step 2** (the final state). Momentum conservation gives $\mathbf p_1' + \mathbf p_2' = \mathbf 0$: $\mathbf p_1' = \mathbf k$, $\mathbf p_2' = -\mathbf k$ for some $\mathbf k$. Energy conservation reads $|\mathbf k| + \sqrt{|\mathbf k|^2 + m_\mu^2} = k + \sqrt{k^2 + m_\mu^2}$. The left side is a strictly increasing function of $|\mathbf k|$ and equals the right side at $|\mathbf k| = k$, so $|\mathbf k| = k$. The outgoing electron then has energy $k$ and the outgoing muon energy $E$.
>
> **Step 3** (the angle). The direction of $\mathbf k$ is not fixed by conservation: $\theta$ is its angle to $\hat{\mathbf z}$, the azimuth $\varphi$ the other free variable. At $\theta = 0$ the electron continues undeflected, $p_1' = p_1$.
>
> **Step 4** (item 3). $E - k = \frac{E^2 - k^2}{E + k} = \frac{m_\mu^2}{E_{\rm cm}}$ and $E + k = E_{\rm cm}$; half the sum and half the difference give $E$ and $k$.
>
> **What the derivation shows.**
> - ⚑ By-product: in the centre-of-mass frame the particles exchange momentum and no energy → [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]], item 2.

^der-c8a-13-1

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]]

> [!theorem] Theorem §C8a.13.2: The Invariants of Electron–Muon Scattering in the Centre-of-Mass Frame
> With the momenta of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]]:
>
> $$
> p_1\cdot p_2 = p_1'\cdot p_2' = k(E + k) , \qquad p_1\cdot p_2' = p_1'\cdot p_2 = k(E + k\cos\theta) , \qquad p_1\cdot p_1' = k^2(1 - \cos\theta) ,
> $$
>
> $$
> q^2 = (p_1 - p_1')^2 = -2p_1\cdot p_1' = -2k^2(1 - \cos\theta) = -4k^2\sin^2\frac\theta2 .
> $$
>
> 1. Only three distinct combinations occur. At $\theta = 0$ the second equals the first, as it must when $p_2' = p_2$.
> 2. The photon momentum is $q = (0, \mathbf q)$ with $\mathbf q = \mathbf p_1 - \mathbf p_1'$, $|\mathbf q| = 2k\sin\frac\theta2$: it has no energy component in this frame, and $q^2 = -|\mathbf q|^2 \le 0$ is spacelike.
> 3. $q^2 \to 0$ for $\theta \to 0$: in the forward direction the photon momentum vanishes, and close to it the photon carries a very small momentum.
>
> *Model:* any (kinematics); *applies:* as [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]].
>
> *Source: PHY 513 Lecture 21, slide 11 ("$p_1\cdot p_2 = k(E + k) = p_1'\cdot p_2'$; $p_1\cdot p_2' = k(E + k\cos\theta) = p_1'\cdot p_2$; $p_1\cdot p_1' = k^2(1 - \cos\theta)$ ⇒ $q^2 = (p_1 - p_1')^2 = -2p_1p_1' = -2k^2(1 - \cos\theta)$"), and recording, part B · PS §5.4, p. 154 ("The combinations we need are …") · item 2 computed here*

^thm-c8a-13-2

> [!derivation]- Derivation
> With $a\cdot b = a^0b^0 - \mathbf a\cdot\mathbf b$:
>
> **Step 1.** $p_1\cdot p_2 = k\cdot E - (k\hat{\mathbf z})\cdot(-k\hat{\mathbf z}) = kE + k^2 = k(E + k)$: the three-momenta are opposite, and the minus sign of the metric turns their product into a plus. $p_1'\cdot p_2' = kE - \mathbf k\cdot(-\mathbf k) = kE + k^2$: the same, since only the relative direction of the two momenta enters and both pairs are back to back.
>
> **Step 2.** $p_1\cdot p_2' = kE - (k\hat{\mathbf z})\cdot(-\mathbf k) = kE + k^2\cos\theta = k(E + k\cos\theta)$, and $p_1'\cdot p_2 = kE - \mathbf k\cdot(-k\hat{\mathbf z}) = kE + k^2\cos\theta$: the outgoing momentum has turned by $\theta$ against the incoming one.
>
> **Step 3.** $p_1\cdot p_1' = k\cdot k - (k\hat{\mathbf z})\cdot\mathbf k = k^2 - k^2\cos\theta = k^2(1 - \cos\theta)$: the energy part and the momentum part nearly cancel when the angle is small.
>
> **Step 4.** $q^2 = p_1^2 + p_1'^2 - 2p_1\cdot p_1' = 0 + 0 - 2k^2(1 - \cos\theta)$, both squares being the electron mass squared, which is zero; $1 - \cos\theta = 2\sin^2\frac\theta2$.
>
> **Step 5** (item 2). $q = p_1 - p_1' = (k - k,\ k\hat{\mathbf z} - \mathbf k) = (0, \mathbf q)$, and $|\mathbf q|^2 = k^2 + k^2 - 2k^2\cos\theta = 2k^2(1 - \cos\theta) = -q^2$.
>
> **What the derivation shows.**
> - ⚑ By-product: $q^2 = t$, the momentum transfer of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], part 3, here with a massless electron → [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-1|Def. §C8a.14.1]].

^der-c8a-13-2

*Uses:* [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]]

## The amplitude and the cross section

> [!theorem] Theorem §C8a.13.3: The Spin-Averaged Squared Amplitude of Electron–Muon Scattering in the Centre-of-Mass Frame
> For $e^-\mu^- \to e^-\mu^-$ at order $e^2$ with $m_e = 0$,
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{2e^4}{k^2(1 - \cos\theta)^2}\Bigl[(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)\Bigr] , \qquad E = \sqrt{k^2 + m_\mu^2} .
> $$
>
> 1. The two products of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]] are squares, because the two factors of each are equal in this frame.
> 2. The denominator comes from the photon propagator, $q^4 = 4k^4(1 - \cos\theta)^2$. It vanishes in the forward direction, where the bracket stays finite and nonzero.
> 3. $\mathcal M$ is dimensionless ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]): each term of the bracket is an energy squared, divided by $k^2$.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, centre-of-mass frame, $m_e = 0$, $\theta \ne 0$.
>
> *Source: PHY 513 Lecture 21, slide 12 ("$\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{2e^4}{k^2(1 - \cos\theta)^2}\bigl[(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)\bigr]$"), and recording, part B · PS §5.4, eq. (5.62) · numerical check against the traces: `qft-C/tools/l21/verify.py`*

^thm-c8a-13-3

> [!derivation]- Derivation
> **Step 1** (the first product). $p_1\cdot p_2'$ and $p_1'\cdot p_2$ are equal ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]), so $(p_1\cdot p_2')(p_1'\cdot p_2) = k^2(E + k\cos\theta)^2$.
>
> **Step 2** (the second product). Likewise $(p_1\cdot p_2)(p_1'\cdot p_2') = k^2(E + k)^2$.
>
> **Step 3** (the mass term). $-m_\mu^2\,p_1\cdot p_1' = -m_\mu^2k^2(1 - \cos\theta)$.
>
> **Step 4** (the bracket). All three terms carry a factor $k^2$:
>
> $$
> (p_1\cdot p_2')(p_1'\cdot p_2) + (p_1\cdot p_2)(p_1'\cdot p_2') - m_\mu^2\,p_1\cdot p_1' = k^2\Bigl[(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)\Bigr] .
> $$
>
> **Step 5** (the prefactor). $q^4 = \bigl(-2k^2(1 - \cos\theta)\bigr)^2 = 4k^4(1 - \cos\theta)^2$, so $\frac{8e^4}{q^4}\cdot k^2 = \frac{8e^4k^2}{4k^4(1 - \cos\theta)^2} = \frac{2e^4}{k^2(1 - \cos\theta)^2}$: the $4$ of $q^4$ turns the $8$ into a $2$, and two of the four powers of $k$ in the propagator cancel against the $k^2$ of the bracket.
>
> **What the derivation shows.**
> - The key part is the denominator, the square of the photon propagator. In annihilation the corresponding factor was the constant $q^4 = E_{\rm cm}^4$ ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-2|Theorem §C8a.8.2]]).
> - ⚑ By-product: the angle enters twice, through the numerator and through the denominator; the term $(E + k)^2$ carries no angle, the term $(E + k\cos\theta)^2$ does.

^der-c8a-13-3

*Uses:* [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]]

> [!theorem] Theorem §C8a.13.4: The Unpolarized Cross Section for Electron–Muon Scattering
> For $e^-\mu^- \to e^-\mu^-$ at order $e^2$ in the centre-of-mass frame with $m_e = 0$, with $\Omega = (\theta, \varphi)$ the direction of the outgoing electron:
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2k^2(E + k)^2(1 - \cos\theta)^2}\Bigl[(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)\Bigr] .
> $$
>
> It is reached in three lines. Let $A$, $B$ be the incoming particles and $\mathbf p_f$ the three-momentum of one outgoing particle.
> 1. *The general $2 \to 2$ formula* in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]), which has three factors, one for the initial state, one for the final state and the dynamics:
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\cdot\frac{|\mathbf p_f|}{16\pi^2E_{\rm cm}}\cdot\frac14\sum_{\rm spins}|\mathcal M|^2 .
> $$
>
> 2. *The velocity difference in that frame,* for any four masses, is $|\mathbf v_A - \mathbf v_B| = \frac{|\mathbf p_A|E_{\rm cm}}{E_AE_B}$, and
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2E_{\rm cm}^2}\cdot\frac{|\mathbf p_f|}{|\mathbf p_A|}\cdot\frac14\sum_{\rm spins}|\mathcal M|^2 :
> $$
>
> a universal factor, and a ratio of final to initial momentum that alone remembers which particles are involved.
> 3. *For this process* $|\mathbf p_f| = |\mathbf p_A| = k$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]], 2), so $\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2E_{\rm cm}^2}\cdot\frac14\sum|\mathcal M|^2$ with $E_{\rm cm} = E + k$.
>
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] with [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] for the cross section, [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] for $\mathcal M$; *applies:* order $\alpha^2$, unpolarized beams and undetected final spins ([[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]), $m_e = 0$, $\theta \ne 0$.
>
> *Source: PHY 513 Lecture 21, slide 13 ("$\frac{d\sigma}{d\Omega} = \frac{1}{2E_A\cdot2E_B\cdot|\vec v_A - \vec v_B|}\cdot\frac{|\vec p_1|}{16\pi^2E_{\rm cm}}\cdot\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{1}{64\pi^2E_{\rm cm}^2}\cdot\frac{|\vec p_1|}{|\vec p_A|}\cdot\frac14\sum_{\rm spin}|\mathcal M|^2 = \alpha^2\cdot\frac{(E + k\cos\theta)^2 + (E + k)^2 - m_\mu^2(1 - \cos\theta)}{2k^2(E + k)^2(1 - \cos\theta)^2}$. 1st line: general $2 \to 2$ scattering formula. 2nd line: simplification in the center of mass system: $|\vec v_A - \vec v_B| = \bigl|\frac{\vec p_A}{E_A} - \frac{\vec p_B}{E_B}\bigr| = |\vec p_A|\bigl|\frac{1}{E_A} + \frac{1}{E_B}\bigr| = \frac{|\vec p_A|E_{\rm cm}}{E_AE_B}$"; the third line: Caution below), and recording, part B · PS §5.4, eqs. (5.63)–(5.64) · numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-13-4

> [!derivation]- Derivation
> **Step 1** (the general formula). [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], item 1, with $|\mathcal M|^2$ replaced by the spin average ([[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]). Here $A$ is the incoming electron ($p_1$), $B$ the incoming muon ($p_2$), and $\mathbf p_f = \mathbf p_1' = \mathbf k$. The formula is that of the centre-of-mass frame, its second factor being the two-body phase space there ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]); nothing has been assumed about the masses.
>
> **Step 2** (the velocities). The velocity of a relativistic particle is its momentum divided by its energy, $\mathbf v = \mathbf p/E$: with $E = \gamma m$ and $\mathbf p = \gamma m\mathbf v$ the factors $\gamma m$ cancel in the ratio. In the centre-of-mass frame $\mathbf p_B = -\mathbf p_A$, so
>
> $$
> |\mathbf v_A - \mathbf v_B| = \Bigl|\frac{\mathbf p_A}{E_A} - \frac{\mathbf p_B}{E_B}\Bigr| = |\mathbf p_A|\Bigl(\frac{1}{E_A} + \frac{1}{E_B}\Bigr) = \frac{|\mathbf p_A|\,(E_A + E_B)}{E_AE_B} = \frac{|\mathbf p_A|\,E_{\rm cm}}{E_AE_B} ,
> $$
>
> a velocity difference, not a relative velocity ([[§C6b.3 The Cross Section#^cau-c6b-3-2|§C6b.3, Caution: The velocity difference is not a relative velocity]]). Here it is $1 + \frac kE$.
>
> **Step 3** (the initial-state factor). The energies $E_AE_B$ cancel: $2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B| = 4|\mathbf p_A|E_{\rm cm}$.
>
> **Step 4** (line 2). $\frac{1}{4|\mathbf p_A|E_{\rm cm}}\cdot\frac{|\mathbf p_f|}{16\pi^2E_{\rm cm}} = \frac{1}{64\pi^2E_{\rm cm}^2}\cdot\frac{|\mathbf p_f|}{|\mathbf p_A|}$. Only $\mathbf p_B = -\mathbf p_A$ has been used.
>
> **Step 5** (line 3). $|\mathbf p_f| = |\mathbf k| = k = |\mathbf p_A|$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]]): the ratio is 1.
>
> **Step 6** (the amplitude). [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]], copied, with $e^4 = (4\pi\alpha)^2 = 16\pi^2\alpha^2$ and $E_{\rm cm} = E + k$:
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2(E + k)^2}\cdot\frac{2\cdot16\pi^2\alpha^2}{k^2(1 - \cos\theta)^2}\Bigl[\cdots\Bigr] = \frac{\alpha^2}{2k^2(E + k)^2(1 - \cos\theta)^2}\Bigl[\cdots\Bigr] ,
> $$
>
> since $\frac{2\cdot16\pi^2}{64\pi^2} = \frac12$.
>
> **What the derivation shows.**
> - ⚑ By-product: line 2 holds for every $2 \to 2$ process in the centre-of-mass frame; for equal initial and final momenta it is the formula of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]].
> - The kinematic factors contributed only $\frac{1}{64\pi^2E_{\rm cm}^2}$; every feature of the result is copied from the amplitude → [[§C8a.13 The Cross Section for Electron–Muon Scattering#^rem-c8a-13-1|Remark: Where the structure comes from]].

^der-c8a-13-4

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|Theorem §C8a.13.1]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-6|P8, step 6]]; [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!caution] Caution: The momenta on slide 13
> Three points on the slide of the cross section.
> 1. Its $|\vec p_1|$ is the momentum of a final particle, in the labels $A + B \to 1 + 2$ of the general formula. It is $|\mathbf p_1'| = k$ in the labels of this lecture, not the momentum of the incoming electron $p_1$; this section writes $|\mathbf p_f|$.
> 2. The first line is already a formula of the centre-of-mass frame: its factor $\frac{|\vec p_1|}{16\pi^2E_{\rm cm}}$ is the two-body phase space in that frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]). The "simplification in the center of mass system" of the second line is the evaluation of the velocity difference.
> 3. The slide gives as the reason for the third line "$|\vec p_1| = |\vec p_A|$ when one particle is massless", and the recording and PS (before (5.63)) say the same. The equality rests on the scattering being elastic: the two outgoing particles have the same masses as the two incoming ones, so their common momentum in the centre-of-mass frame is the same ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]; Step 2 of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^der-c8a-13-1|Derivation §C8a.13.1]]). The massless electron enters the formulas of this section through $E_A = |\mathbf p_A| = k$.
>
> *Source: PHY 513 Lecture 21, slide 13, and recording, part B · PS §5.4, p. 154 ("which in the case where one particle is massless takes the simple form", eq. (5.63)) · recorded in `qft-C/ERRATA.md`*

^cau-c8a-13-1

> [!remark] Remark: Where the structure comes from
> The cross section has a great deal of structure, and none of it could have been guessed: it has to be computed. It is worth seeing where it comes from. The three kinematic factors of the general formula combine to the universal $\frac{1}{64\pi^2E_{\rm cm}^2}$ and are essentially trivial. The complicated part is entirely the dynamics: the square bracket and the squared propagator are copied from the amplitude ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]]). This is the split into kinematics and dynamics of the annihilation process ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^rem-c8a-8-2|§C8a.8, Remark: Kinematics and dynamics]]), with a more complicated dynamical factor.
>
> *Source: PHY 513 Lecture 21, recording, part B*

^rem-c8a-13-1

## Two limits

![[ph-qft-c8-19-2.svg]]
*ADDED figure (not from the lecture): the two processes at high energy on a logarithmic scale, in units of $\frac{\alpha^2}{4E_{\rm cm}^2}$. Red: electron–muon scattering, [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]]; blue: annihilation into muons, $1 + \cos^2\theta$ ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-5|Theorem §C8a.8.5]]); dashed: the small-angle form $64/\theta^4$ of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]. Annihilation varies by a factor of 2 over all angles; scattering rises without bound in the forward direction. The two agree at $\theta = \pi$ (computed here).*

> [!theorem] Theorem §C8a.13.5: Electron–Muon Scattering in the Ultrarelativistic Limit
> For $m_\mu \ll E$, where $E \simeq k$ and $E_{\rm cm} \simeq 2k$,
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2E_{\rm cm}^2}\cdot\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2} .
> $$
>
> 1. The energy dependence is $1/E_{\rm cm}^2$, all it can be by dimensional analysis when no mass is left ([[§C6b.4 Two-Body Scattering Kinematics#^rem-c6b-4-3|§C6b.4, Remark: Why 1/E²: dimensional analysis]]).
> 2. The angular dependence stays nontrivial in this limit. The $4$ comes from the term $(E + k)^2$, which has no angular dependence; the $(1 + \cos\theta)^2$ from $(E + k\cos\theta)^2$; the denominator from the propagator. How they add up is not obvious beforehand.
> 3. The corresponding amplitude is $\frac14\sum|\mathcal M|^2 = 2e^4\,\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$, which is $\frac{2e^4}{t^2}(s^2 + u^2)$ in the Mandelstam variables ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]]).
>
> *Model:* as [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]]; *applies:* as there, with both masses neglected against $E_{\rm cm}$; $\theta \ne 0$.
>
> *Source: PHY 513 Lecture 21, slide 14 ("Angular dependence quite nontrivial even in the ultrarelativistic limit ($m_\mu \ll E \simeq k$): $\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2E_{\rm cm}^2}\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$"), and recording, part B · PS §5.4, eq. (5.65)*

^thm-c8a-13-5

> [!derivation]- Derivation
> **Step 1** (the energies). For $m_\mu \to 0$, $E = \sqrt{k^2 + m_\mu^2} \to k$ and $E_{\rm cm} = E + k \to 2k$, so $k = \frac12E_{\rm cm}$.
>
> **Step 2** (the bracket). $(E + k\cos\theta)^2 \to k^2(1 + \cos\theta)^2$, $(E + k)^2 \to 4k^2$, and $m_\mu^2(1 - \cos\theta) \to 0$: the bracket of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]] tends to $k^2\bigl[4 + (1 + \cos\theta)^2\bigr]$.
>
> **Step 3** (the prefactor). $\frac{\alpha^2}{2k^2(E + k)^2(1 - \cos\theta)^2} \to \frac{\alpha^2}{2k^2\cdot4k^2(1 - \cos\theta)^2}$. With the $k^2$ of Step 2: $\frac{\alpha^2}{8k^2}\cdot\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$, and $8k^2 = 2E_{\rm cm}^2$.
>
> **Step 4** (item 3). The same limit in [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]]: $\frac{2e^4}{k^2(1 - \cos\theta)^2}\cdot k^2\bigl[4 + (1 + \cos\theta)^2\bigr]$.
>
> **What the derivation shows.**
> - Compare annihilation at the same energies, $\frac{\alpha^2}{4E_{\rm cm}^2}(1 + \cos^2\theta)$ ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-5|Theorem §C8a.8.5]]): the same order in $\alpha$, the same $1/E_{\rm cm}^2$, a different function of the angle.

^der-c8a-13-5

*Uses:* [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]]

> [!theorem] Theorem §C8a.13.6: At Small Angles the Cross Section Grows as 1/θ⁴
> 1. For $\theta \to 0$ the cross section of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]] grows as
>
> $$
> \frac{d\sigma}{d\Omega} \propto \frac{1}{\theta^4} ,
> $$
>
> for any muon mass: the bracket stays finite and nonzero while $(1 - \cos\theta)^2 \simeq \frac{\theta^4}{4}$. In the ultrarelativistic limit of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]] the coefficient is $\frac{d\sigma}{d\Omega} \simeq \frac{16\alpha^2}{E_{\rm cm}^2\,\theta^4}$.
> 2. *The mechanism in the amplitude:* the factor is the squared photon propagator, $\frac{1}{q^4}$ with $q^2 = -2k^2(1 - \cos\theta) \simeq -k^2\theta^2$. As $\theta \to 0$, $q^2 \to 0$: the virtual photon is nearly on its mass shell ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]), and the amplitude is large because it is divided by something small.
> 3. *The total cross section is infinite.* In the ultrarelativistic limit the cross section for scattering by more than $\theta_0$ is $\sigma(\theta > \theta_0) \simeq \frac{16\pi\alpha^2}{E_{\rm cm}^2\,\theta_0^2}$ for small $\theta_0$, which grows without bound as $\theta_0 \to 0$.
>
> The same $1/\theta^4$ is the small-angle behaviour of Rutherford scattering, in classical mechanics as well (see [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-8|Theorem §C8a.10.8]]).
>
> *Model:* as [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]]; *applies:* order $\alpha^2$; items 1 (the coefficient) and 3 with both masses neglected; the first-order formula used at all angles down to $\theta_0$.
>
> *Source: PHY 513 Lecture 21, slide 14 ("Small-angle scattering $\theta \sim 0$ has huge cross-section: $\frac{d\sigma}{d\Omega} \sim \frac{1}{\theta^4}$. Particles barely hit one another, as in Rutherford scattering. Mechanism in amplitude: virtual photon nearly on-shell"), and recording, part B · PS §5.4, eq. (5.66) and p. 155 ("This singularity is the same as in the Rutherford formula … it arises from the nearly on-shell (that is, $q^2 \approx 0$) virtual photon") · the coefficient $16$ and item 3 derived here from the lecture's formula; numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-13-6

> [!derivation]- Derivation
> **Step 1** (the expansion). $1 - \cos\theta = \frac{\theta^2}{2} - \frac{\theta^4}{24} + \cdots$, so $(1 - \cos\theta)^2 = \frac{\theta^4}{4}\bigl(1 + O(\theta^2)\bigr)$.
>
> **Step 2** (the bracket at $\theta = 0$). In [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]] the bracket is continuous at $\theta = 0$, where its last term vanishes and the first two are equal: its value there is $2(E + k)^2 > 0$. The cross section therefore behaves as a constant times $(1 - \cos\theta)^{-2}$, that is as $1/\theta^4$.
>
> **Step 3** (the coefficient at high energy). In [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]] the numerator at $\theta = 0$ is $4 + 2^2 = 8$: $\frac{d\sigma}{d\Omega} \simeq \frac{\alpha^2}{2E_{\rm cm}^2}\cdot\frac{8}{\theta^4/4} = \frac{16\alpha^2}{E_{\rm cm}^2\theta^4}$.
>
> **Step 4** (the photon). $q^2 = -2k^2(1 - \cos\theta) = -k^2\theta^2\bigl(1 + O(\theta^2)\bigr)$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]), and $\frac14\sum|\mathcal M|^2 \propto \frac{1}{q^4}$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]]): the $\theta^{-4}$ is the square of the propagator $\frac{1}{q^2}$ of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]]. The photon's mass shell is $q^2 = 0$.
>
> **Step 5** (the integral). With $x = 1 - \cos\theta$, $d\Omega = 2\pi\,dx$ after the integral over $\varphi$, and $1 + \cos\theta = 2 - x$, the integrand of [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]] is $\frac{4 + (2 - x)^2}{x^2} = \frac{8}{x^2} - \frac4x + 1$. Integrating from $x_0 = 1 - \cos\theta_0$ to $2$:
>
> $$
> \sigma(\theta > \theta_0) = \frac{\pi\alpha^2}{E_{\rm cm}^2}\int_{x_0}^{2}dx\,\Bigl(\frac{8}{x^2} - \frac4x + 1\Bigr) = \frac{\pi\alpha^2}{E_{\rm cm}^2}\Bigl[\frac{8}{x_0} - 2 - x_0 - 4\ln\frac{2}{x_0}\Bigr] .
> $$
>
> For small $\theta_0$, $x_0 \simeq \frac{\theta_0^2}{2}$ and the first term dominates: $\frac{16\pi\alpha^2}{E_{\rm cm}^2\theta_0^2}$.
>
> **What the derivation shows.**
> - ⚑ By-product: the divergence is a statement about the forward direction only; at any fixed angle away from it the cross section is finite and of order $\alpha^2/E_{\rm cm}^2$.
> - The pole of the propagator at $q^2 = 0$, which the annihilation process can never reach ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-3|Theorem §C8a.6.3]]), lies at the edge of the physical region of the scattering process → [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]].

^der-c8a-13-6

*Uses:* [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|Theorem §C8a.13.5]], [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-6|P8, step 6]]

> [!remark] Remark: Barely hitting
> Why is a small deflection so probable? Small angles belong to large impact parameters: the particles nearly miss each other, and it is easy to nearly miss. Wherever the electron passes, as long as it is not near the centre, some scattering happens. Very little happens in each such event, but the cross section measures how probable it is that something happens, and that probability is very large.
>
> In the amplitude the same fact appears as a photon that is nearly on shell, which means nearly real. The process is then close to a two-step one: one particle, the muon, creates an electromagnetic field, almost an electrostatic one, and the other particle feels that field. A field that is nearly real makes the process essentially classical. This is the opposite of annihilation, where the two initial particles disappear and the photon is as far from its shell as the energy allows ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-3|Theorem §C8a.6.3]]).
>
> *Source: PHY 513 Lecture 21, recording, part B; slide 14*

^rem-c8a-13-2

> [!remark]- Connections
> - The route from the invariant form to the cross section is that of the annihilation process, with the same general formula — [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-4|Theorem §C8a.8.4]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]; as a procedure — [[P8 Unpolarized Cross Section from Diagrams|P8]], [[P7 From ℳ to σ or Γ|P7]].
> - That the momentum transfer of an exchange is spacelike, with the forward direction as the only place where the photon reaches its shell, was stated with the definition of the terms — [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]].
> - The initial and final momenta of an elastic process agree in the centre-of-mass frame because they depend only on $E_{\rm cm}$ and the two masses — [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]].
> - Forward: the two high-energy results as one function of $s$, $t$, $u$, and the forward peak as the pole at $t = 0$ — [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]].
> - A second peak from a virtual particle close to its mass shell: the electron of Compton scattering in the backward direction at high energy, weaker than the square of its propagator — [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]].
