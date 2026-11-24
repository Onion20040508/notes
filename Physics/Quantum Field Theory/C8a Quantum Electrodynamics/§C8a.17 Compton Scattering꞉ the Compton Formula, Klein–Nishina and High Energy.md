---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.17
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations|§C8a.16]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.18★ Derivative Couplings and Scalar QED|§C8a.18★]] →

*Sources: PHY 513 Lecture 22 (Larsen, 23 Nov 2026, "Compton Scattering"), slides 20–27 (Part C), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3 "Physics of Compton scattering" (subsections "The lab frame: the photon as a particle" with Principle "The Compton formula", "The Klein–Nishina formula" with Derivations "Two-body phase space in the lab frame (filled in)", "The Klein–Nishina formula (filled in)" and Principle "Klein–Nishina and Thomson", "High energy in the center of mass" with paragraphs "The physical origin", "Asked in the lecture: what about the mass?" and Principle "High-energy total cross section"), §22.4 "Summary" (Principle "Compton scattering"), Caution "Slips in the slides", paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.5, pp. 162–164, eqs. (5.88)–(5.96) (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.6, eqs. (8.319)–(8.320); §8.6.2, eqs. (8.384)–(8.401), Figures 8.13–8.14; §8.6.3, eqs. (8.402)–(8.411) (page images and text of the current build checked).*

How much light comes out at each angle? The kinematics of a photon bouncing off an electron fixes the energy of the scattered photon at each angle ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]]), and that needs no quantum electrodynamics. The intensity at each angle does: it is the spin- and polarization-averaged $|\mathcal M|^2$ of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] turned into a cross section. This section does so in two frames:
1. **the lab frame**, electron at rest: the Compton formula, the phase space ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|Theorem §C8a.17.2]]), the Klein–Nishina formula ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|Theorem §C8a.17.4]]) and its low-energy limit, the Thomson cross section ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-5|Theorem §C8a.17.5]]);
2. **the centre-of-mass frame at high energy**: the cross section peaks where the photon is scattered straight back ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]), and the electron mass keeps the total cross section finite, with a logarithm of the energy ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]]).

**Setup.** [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]] at order $e^2$, unpolarized ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^def-c8a-15-1|Def. §C8a.15.1]]), with the cross section of two colliding beams ([[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]). The whole dynamics is the function of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]], which depends on $p\cdot k$ and $p\cdot k'$ only; everything else in this section is kinematics: choosing a frame, expressing the two invariants through an energy and an angle, phase space and flux ([[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]], [[P8 Unpolarized Cross Section from Diagrams#^p8-6|P8, step 6]]).

*Conventions* ([[Larsen PHY 513]]): momenta as in [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square|§C8a.15]]. The photon comes in along $+\hat{\mathbf z}$, and $\theta$ is the angle between $\mathbf k$ and $\mathbf k'$ in both frames. Lab frame: $\omega$, $\omega'$ are the energies of the incoming and the outgoing photon and $E'$ that of the recoiling electron. Centre-of-mass frame: $\omega$ is the energy of each photon and $E$ that of each electron. $\alpha = e^2/4\pi$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^def-c1a-8-1|Def. §C1a.8.1]]), $s = (p + k)^2$, $d\Omega = \sin\theta\,d\theta\,d\varphi$. Yu puts the incoming electron along $+\hat{\mathbf z}$ in the centre-of-mass frame; his $\theta$ is the same angle.

## The lab frame: the photon as a particle

> [!theorem] Theorem §C8a.17.1: The Compton Formula
> ![[ph-qft-c8a-17-1.svg]]
> *Kinematics, not Feynman diagrams (after PHY 513 Lecture 22, slides 21 and 24, PS pp. 162 and 164, and the figure of the user's notes). (a) Lab frame, electron at rest. (b) Centre-of-mass frame; $\theta$ is the angle between $\mathbf k$ and $\mathbf k'$, and also between $\mathbf p$ and $\mathbf p'$.*
>
> In the lab frame the electron is at rest and is hit by the photon:
>
> $$
> p = (m, \mathbf 0) , \qquad k = (\omega, \omega\hat{\mathbf z}) , \qquad k' = (\omega', \omega'\sin\theta, 0, \omega'\cos\theta) , \qquad p' = p + k - k' = (E', \mathbf p') .
> $$
>
> Then the energy of the scattered photon is fixed by its angle:
>
> $$
> \omega' = \frac{\omega}{1 + \dfrac{\omega}{m}(1 - \cos\theta)} , \qquad\text{equivalently}\qquad \frac{1}{\omega'} - \frac{1}{\omega} = \frac{1 - \cos\theta}{m} .
> $$
>
> 1. **Wavelength form.** With $\lambda = 2\pi/\omega$: $\lambda' - \lambda = \dfrac{2\pi}{m}(1 - \cos\theta)$; with $\hbar$ and $c$ restored ([[§C1a.2 Natural Units and Dimensional Analysis|§C1a.2]]), $\lambda' - \lambda = \dfrac{h}{mc}(1 - \cos\theta)$, where $h/mc = 2\pi\hbar/mc \approx 2.43\ \text{pm}$ is the Compton wavelength of the electron, $2\pi$ times the reduced one of [[§B4.1 The Klein–Gordon Equation#^def-b4-1-2|REL Def. §B4.1.2]].
> 2. **Range.** $\omega' \le \omega$, with equality only at $\theta = 0$; the photon loses most energy when it is scattered straight back, $\omega'(\pi) = \omega/(1 + 2\omega/m)$. For $\omega \ll m$ the loss is negligible, $\omega' \approx \omega$; for $\omega \to \infty$ at fixed $\theta \ne 0$, $\omega' \to m/(1 - \cos\theta)$.
> 3. **Kinematics only.** The formula follows from four-momentum conservation for a massless photon and an electron of mass $m$. No property of QED is used.
>
> *Model:* kinematics; *applies:* $\gamma e \to \gamma e$ on a free electron at rest, any interaction; for an electron bound in an atom, when the photon energy is far above the binding energy.
>
> *Source: PHY 513 Lecture 22, slide 21 ("The 'lab frame': $e^-$ at rest is hit by incoming $\gamma$. Square four-momentum conservation: $p' = p + k - k'$; $0 = p\cdot k - p\cdot k' - k\cdot k' = m\omega - m\omega' - \omega\omega'(1 - \cos\theta)$. Result for final frequency: $\omega' = \frac{\omega}{1 + \frac\omega m(1 - \cos\theta)}$"), slide 22, and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Principle "The Compton formula" (the wavelength form filled in by the user's notes) · PS §5.5, eqs. (5.88)–(5.89) ("Compton's formula for the shift in the photon wavelength") · Yu §8.6, eq. (8.319); §8.6.2, eqs. (8.384)–(8.392) · item 2 written out here (checked numerically)*

^thm-c8a-17-1

> [!derivation]- Derivation
> **Step 1** (square momentum conservation). By [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]], 1: $p'^2 = (p + k - k')^2$ with $p'^2 = p^2 = m^2$ and $k^2 = k'^2 = 0$ leaves the three cross terms, $0 = p\cdot k - p\cdot k' - k\cdot k'$.
>
> **Step 2** (the lab values). $p$ has only a time component: $p\cdot k = m\omega$, $p\cdot k' = m\omega'$. For the photons, $k\cdot k' = \omega\omega' - \mathbf k\cdot\mathbf k' = \omega\omega'(1 - \cos\theta)$. So
>
> $$
> 0 = m\omega - m\omega' - \omega\omega'(1 - \cos\theta) .
> $$
>
> **Step 3** (solve). Dividing by $m\omega\omega'$: $\frac{1}{\omega'} - \frac1\omega = \frac{1 - \cos\theta}{m}$. Solving for $\omega'$: $\omega'\bigl[m + \omega(1 - \cos\theta)\bigr] = m\omega$, the first form.
>
> **Step 4** (items 1 and 2). $\lambda = 2\pi/\omega$ turns the second form into the wavelength form; a length $1/m$ of natural units is $\hbar/mc$ ([[§C1a.2 Natural Units and Dimensional Analysis|§C1a.2]]). The denominator $1 + \frac\omega m(1 - \cos\theta)$ is $1$ at $\theta = 0$ and largest, $1 + 2\omega/m$, at $\theta = \pi$. For $\omega \to \infty$, $\frac{1}{\omega'} \to \frac{1 - \cos\theta}{m}$.
>
> **What the derivation shows.**
> - ⚑ By-product: $m + \omega(1 - \cos\theta) = m\omega/\omega'$, used twice below → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|Theorem §C8a.17.2]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-3|Theorem §C8a.17.3]].
> - The relation is the frame-independent $k\cdot k' = p\cdot k - p\cdot k'$ read in the rest frame of the electron.

^der-c8a-17-1

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]]

> [!remark] Remark: What the kinematics says and what it cannot say
> In the lab frame the photon behaves like a billiard ball that hits a stationary target. It comes out with less energy, and how much less depends on the angle: the colour of the scattered light changes with the angle, a sharp prediction. This was Compton's point: light scatters as a particle, and its kinematics can be done as for any massless particle. Compton's X-ray photons had energies of about 17 keV, far above atomic binding energies, so that the electrons could be treated as free. The prediction needs relativity and just enough quantum mechanics to treat the photon as a massless particle. It says nothing about the intensity: how much light comes out at each angle, and which angles are typical for a given $\omega$. That is what QED adds.
>
> *Source: PHY 513 Lecture 22, slide 3 ("Highlight: the photon scatters as a particle"), slide 22 ("The photon scatters as a particle: energy loss depends on angle, so color of final photon depends on angle"), slide 23 ("QED is not just kinematics: intensity as function of angle"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, subsection "The lab frame: the photon as a particle" · Yu §8.6, first paragraph (the 17 keV X-rays)*

^rem-c8a-17-1

## The Klein–Nishina formula

> [!theorem] Theorem §C8a.17.2: Two-Body Phase Space in the Lab Frame
> For $\gamma e \to \gamma e$ in the lab frame of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]], and a function $F$ that does not depend on the azimuth of $\mathbf k'$,
>
> $$
> \int d\Pi_2\;F = \int d\cos\theta\;\frac{\omega'^2}{8\pi\,\omega\,m}\;F ,
> $$
>
> with $\omega' = \omega'(\theta)$ of the Compton formula.
>
> *Equivalently,* this is the two-body phase space of [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]] in a frame that is not the centre-of-mass frame; the centre-of-mass form is [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]].
>
> *Model:* kinematics; *applies:* a massless particle scattering off a particle of mass $m$ at rest, final masses $0$ and $m$; independent of the dynamics.
>
> *Source: PHY 513 Lecture 22, slide 23 ("Two body phase space (a few lines to compute, not here): $\int d\Pi_2 = \int d\cos\theta\,\frac{(\omega')^2}{8\pi\omega m}$") · the user's PHY 513 notes, Lecture 22 update, §22.3, Derivation "Two-body phase space in the lab frame (filled in)" (filled in by the user's notes; "Checked numerically") · PS §5.5, eq. (5.90) · Yu §8.6.2, eq. (8.395)*

^thm-c8a-17-2

> [!derivation]- Derivation
> **Step 1** (the definition). $\int d\Pi_2 = \int\frac{d^3k'}{(2\pi)^3\,2\omega'}\,\frac{d^3p'}{(2\pi)^3\,2E'}\,(2\pi)^4\delta^4(k' + p' - k - p)$ ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]).
>
> **Step 2** (the momentum delta). The integral over $\mathbf p'$ uses $\delta^3(\mathbf k' + \mathbf p' - \mathbf k)$ (the electron is at rest, $\mathbf p = \mathbf 0$) and eliminates $\mathbf p' = \mathbf k - \mathbf k'$. Then $E'$ is no longer independent:
>
> $$
> E'^2 = m^2 + |\mathbf k - \mathbf k'|^2 = m^2 + \omega^2 + \omega'^2 - 2\omega\omega'\cos\theta .
> $$
>
> What remains is $\int\frac{d^3k'}{(2\pi)^3\,2\omega'\,2E'}\;2\pi\,\delta(\omega' + E' - \omega - m)$.
>
> **Step 3** (spherical coordinates). $d^3k' = \omega'^2\,d\omega'\,d\varphi\,d\cos\theta$. Nothing depends on $\varphi$: its integral gives $2\pi$. The factors combine to $\frac{2\pi\cdot2\pi}{(2\pi)^3\cdot4} = \frac{1}{8\pi}$:
>
> $$
> \int d\Pi_2 = \int d\cos\theta\int d\omega'\;\frac{\omega'}{8\pi\,E'}\;\delta\bigl(f(\omega')\bigr) , \qquad f(\omega') \equiv \omega' + E'(\omega', \theta) - \omega - m .
> $$
>
> **Step 4** (the energy delta). $\delta(f(\omega'))$ contributes $1/|f'|$ at the zero of $f$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]). The zero is the $\omega'$ of the Compton formula, the only solution of energy conservation at fixed $\theta$. With $\frac{\partial E'}{\partial\omega'} = \frac{\omega' - \omega\cos\theta}{E'}$ from Step 2,
>
> $$
> f' = 1 + \frac{\omega' - \omega\cos\theta}{E'} = \frac{E' + \omega' - \omega\cos\theta}{E'} , \qquad \int d\Pi_2 = \int d\cos\theta\;\frac{\omega'}{8\pi\,(E' + \omega' - \omega\cos\theta)} .
> $$
>
> **Step 5** (simplify). Energy conservation, $E' + \omega' = m + \omega$, turns the bracket into $m + \omega(1 - \cos\theta)$, positive, so no absolute value is needed. By the Compton formula it is $m\omega/\omega'$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^der-c8a-17-1|Derivation §C8a.17.1]], Step 3):
>
> $$
> \int d\Pi_2 = \int d\cos\theta\;\frac{\omega'}{8\pi}\cdot\frac{\omega'}{m\omega} = \int d\cos\theta\;\frac{\omega'^2}{8\pi\,\omega\,m} .
> $$
>
> **What the derivation shows.**
> - Away from the centre-of-mass frame the Jacobian of the energy delta function depends on the angle; here the whole dependence is the factor $\omega'^2$.
> - ⚑ By-product: for $\omega \ll m$, $\omega' \to \omega$ and the measure becomes $\frac{\omega}{8\pi m}\,d\cos\theta$, independent of the angle.

^der-c8a-17-2

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!theorem] Theorem §C8a.17.3: The Squared Amplitude in the Lab Frame
> In the lab frame $p\cdot k = m\omega$ and $p\cdot k' = m\omega'$, and the result of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] becomes
>
> $$
> \frac14\sum_{\rm spins,\,pols}|\mathcal M|^2 = 2e^4\left[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\right] ,
> $$
>
> a function of $\theta$ alone once $\omega'/\omega$ is taken from the Compton formula.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized, electron initially at rest.
>
> *Source: the user's PHY 513 notes, Lecture 22 update, §22.3, Derivation "The Klein–Nishina formula (filled in)" (filled in by the user's notes) · PHY 513 Lecture 22, transcript ($p\cdot k = m\omega$, $p\cdot k' = m\omega'$, so that the result is a function of $\omega'/\omega$) · PS §5.5, p. 163 · Yu §8.6.2, eqs. (8.393)–(8.394)*

^thm-c8a-17-3

> [!derivation]- Derivation
> **Step 1** (the ratios). $\frac{p\cdot k'}{p\cdot k} = \frac{\omega'}{\omega}$ and $\frac{p\cdot k}{p\cdot k'} = \frac{\omega}{\omega'}$.
>
> **Step 2** (the mass terms). $m\Bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\Bigr) = \frac1\omega - \frac{1}{\omega'} = -\frac{1 - \cos\theta}{m}$ by the Compton formula. Hence $2m^2\Bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\Bigr) = -2(1 - \cos\theta)$ and $m^4\Bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\Bigr)^2 = (1 - \cos\theta)^2$.
>
> **Step 3** (combine). $-2(1 - \cos\theta) + (1 - \cos\theta)^2 = (1 - \cos\theta)(-1 - \cos\theta) = -(1 - \cos^2\theta) = -\sin^2\theta$.
>
> **What the derivation shows.**
> - The mass has dropped out of the bracket: in the lab frame it enters only through $\omega'(\theta)$.

^der-c8a-17-3

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]]

> [!theorem] Theorem §C8a.17.4: The Klein–Nishina Formula
> The unpolarized cross section of Compton scattering off an electron at rest is
>
> $$
> \frac{d\sigma}{d\cos\theta} = \frac{\pi\alpha^2}{m^2}\Bigl(\frac{\omega'}{\omega}\Bigr)^2\left[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\right] , \qquad \frac{\omega'}{\omega} = \frac{1}{1 + \frac\omega m(1 - \cos\theta)} .
> $$
>
> 1. In the forward direction, $\theta = 0$, $\omega' = \omega$ and $\frac{d\sigma}{d\cos\theta} = \frac{2\pi\alpha^2}{m^2}$ at every energy.
> 2. At larger angles the factor $(\omega'/\omega)^2$ suppresses the cross section as $\omega/m$ grows: forward scattering, where $\omega' \approx \omega$, dominates.
> 3. The angular dependence is intricate, through $\omega'(\theta)$. It is a prediction of QED for each $\omega/m$, beyond the kinematics of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]].
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized photon beam on free electrons at rest, any $\omega$; cross section per electron.
>
> *Source: PHY 513 Lecture 22, slide 23 ("Klein-Nishina formula: (more lines to compute, not here): $\frac{d\sigma}{d\cos\theta} = \frac{\pi\alpha^2}{m^2}\bigl(\frac{\omega'}{\omega}\bigr)^2\bigl[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\bigr]$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Derivation "The Klein–Nishina formula (filled in)" and Principle "Klein–Nishina and Thomson" ("checked numerically") · PS §5.5, eq. (5.91) and the display before it (O. Klein and Y. Nishina, Z. Physik 52, 853 (1929), as cited there) · Yu §8.6.2, eqs. (8.396)–(8.398) · items 1 and 2: the figure caption of the user's notes*

^thm-c8a-17-4

> [!derivation]- Derivation
> **Step 1** (the general formula). $d\sigma = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\,\frac14\sum|\mathcal M|^2\,d\Pi_2$ ([[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], 2, with the unpolarized $|\mathcal M|^2$ of [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]).
>
> **Step 2** (the flux factor). The photon has $E_A = \omega$ and speed 1; the electron is at rest, $E_B = m$, $\mathbf v_B = \mathbf 0$. So $\frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|} = \frac{1}{2\omega\cdot2m\cdot1} = \frac{1}{4m\omega}$.
>
> **Step 3** (phase space and amplitude). By [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|Theorem §C8a.17.2]] and [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-3|Theorem §C8a.17.3]], whose $F$ depends on $\theta$ only:
>
> $$
> \frac{d\sigma}{d\cos\theta} = \frac{1}{4m\omega}\cdot\frac{\omega'^2}{8\pi\,\omega\,m}\cdot2e^4\left[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\right] = \frac{e^4}{16\pi\,m^2}\,\frac{\omega'^2}{\omega^2}\left[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\right] .
> $$
>
> **Step 4** ($\alpha$). $e^4 = 16\pi^2\alpha^2$, so $\frac{e^4}{16\pi m^2} = \frac{\pi\alpha^2}{m^2}$.
>
> **Step 5** (item 1). At $\theta = 0$: $\omega'/\omega = 1$ and $\sin\theta = 0$, bracket $= 2$.
>
> **What the derivation shows.**
> - The structure is that of every cross section: flux factor, phase space, squared amplitude. Only the last carries the dynamics ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^rem-c8a-8-2|§C8a.8, Remark: Kinematics and dynamics]]).
> - ⚑ By-product: at $\omega \ll m$ every factor $\omega'/\omega$ is 1 → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-5|Theorem §C8a.17.5]].

^der-c8a-17-4

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|Theorem §C8a.17.2]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-3|Theorem §C8a.17.3]], [[§C1a.8 Relativistic Electrodynamics in Index Form#^def-c1a-8-1|Def. §C1a.8.1]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-6|P8, step 6]]

> [!theorem] Theorem §C8a.17.5: The Thomson Limit
> At low energy, $\omega \ll m$, $\omega' \to \omega$ and the Klein–Nishina formula becomes
>
> $$
> \frac{d\sigma}{d\cos\theta} = \frac{\pi\alpha^2}{m^2}\,(1 + \cos^2\theta) , \qquad \sigma_{\rm tot} = \frac{\pi\alpha^2}{m^2}\int_{-1}^{1}(1 + \cos^2\theta)\,d\cos\theta = \frac{8\pi\alpha^2}{3m^2} .
> $$
>
> 1. This is the Thomson cross section of classical electrodynamics, for the scattering of electromagnetic radiation by a free electron: $\sigma_{\rm tot} = \frac{8\pi}{3}r_e^2$ with the classical electron radius $r_e = \alpha/m$ ($\approx 2.82$ fm, so $\sigma_{\rm tot} \approx 0.665$ barn).
> 2. It does not depend on $\omega$, and the distribution is symmetric between forward and backward.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, $\omega \ll m$; the Klein–Nishina formula is its correction at higher energy.
>
> *Source: PHY 513 Lecture 22, slide 23 ("Thomson cross-section in classical EM: (low energy $\omega \to 0$ ⇒ $\omega = \omega'$, then integrate over $\theta$) $\sigma_{\rm tot} = \frac{8\pi\alpha^2}{3m^2}$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Principle "Klein–Nishina and Thomson" ($r_e$ filled in by the user's notes; "checked numerically") · PS §5.5, eq. (5.92) ("the familiar Thomson cross section for scattering of classical electromagnetic radiation by a free electron") · Yu §8.6, eq. (8.320) ($r_e \equiv \alpha/m_e$); §8.6.2, eqs. (8.399)–(8.401) · the numbers in item 1 evaluated here*

^thm-c8a-17-5

> [!derivation]- Derivation
> **Step 1** (the limit). For $\omega/m \to 0$ at any $\theta$, $\omega'/\omega = 1/(1 + \frac\omega m(1 - \cos\theta)) \to 1$. The bracket becomes $1 + 1 - \sin^2\theta = 1 + \cos^2\theta$ and the prefactor $(\omega'/\omega)^2 \to 1$.
>
> **Step 2** (the integral). $\int_{-1}^{1}(1 + c^2)\,dc = 2 + \frac23 = \frac83$.
>
> **Step 3** (units). $r_e = \alpha\hbar/mc$ with $\hbar c = 197.327$ MeV fm, $mc^2 = 0.510999$ MeV, $\alpha = 1/137.036$: $r_e = 2.818$ fm; $\frac{8\pi}{3}r_e^2 = 66.5\ \text{fm}^2 = 0.665$ barn ($1\ \text{barn} = 100\ \text{fm}^2$; [[P4 Restoring ħ and c|P4]]).
>
> **What the derivation shows.**
> - The quantum of light does not enter: at $\omega \ll m$ the photon's recoil is negligible and the result is the classical one.

^der-c8a-17-5

*Uses:* [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|Theorem §C8a.17.4]]

![[ph-qft-c8a-17-2.svg]]
*ADDED figure (after the figure of the user's notes, §22.3, and Yu's Figure 8.14): the Klein–Nishina distribution of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|Theorem §C8a.17.4]] in the lab frame for four photon energies. At low energy it is the symmetric Thomson distribution $1 + \cos^2\theta$. All curves start at the same forward value; as $\omega/m$ grows, scattering at large angles is suppressed by the factor $(\omega'/\omega)^2$.*

![[ph-qft-c8a-17-a1.gif|520]]
*Animation: the Klein–Nishina distribution (blue) leaving the Thomson one (black) as $\omega/m$ grows from 0 to 5. Lower panel: the Compton formula $\omega'/\omega$ against $\theta$; the red dot marks the backward value $1/(1 + 2\omega/m)$. The suppression at large angles follows the energy loss of the photon. (Not from the sources; animation added, vault only.)*

## High energy in the centre-of-mass frame

> [!theorem] Theorem §C8a.17.6: The Invariants in the Centre-of-Mass Frame
> In the centre-of-mass frame (figure of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]], panel (b)),
>
> $$
> k = (\omega, \omega\hat{\mathbf z}) , \quad p = (E, -\omega\hat{\mathbf z}) , \quad k' = (\omega, \omega\sin\theta, 0, \omega\cos\theta) , \quad p' = (E, -\omega\sin\theta, 0, -\omega\cos\theta) , \qquad E^2 = \omega^2 + m^2 ,
> $$
>
> and the two invariants of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]] are
>
> $$
> p\cdot k = \omega\,(E + \omega) , \qquad p\cdot k' = \omega\,(E + \omega\cos\theta) .
> $$
>
> 1. The scattering is elastic: all four three-momenta have the magnitude $\omega$, and each particle keeps its energy, because the final masses are the initial ones and the centre-of-mass momentum is fixed by $E_{\rm cm}$ and the two masses ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]).
> 2. $s = (p + k)^2 = (E + \omega)^2 = m^2 + 2\,p\cdot k$.
>
> *Model:* kinematics; *applies:* $\gamma e \to \gamma e$ in the centre-of-mass frame, any energy.
>
> *Source: PHY 513 Lecture 22, slide 24 ("Invariants computed in the cms: $p\cdot k = \omega(E + \omega)$, $p\cdot k' = \omega(E + \omega\cos\theta)$ where $E^2 = \omega^2 + m^2$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, subsection "High energy in the center of mass" · PS §5.5, p. 164 · Yu §8.6.3, eqs. (8.402)–(8.404)*

^thm-c8a-17-6

> [!derivation]- Derivation
> **Step 1** (the momenta). The total three-momentum vanishes, so the electron comes in along $-\hat{\mathbf z}$ with $|\mathbf p| = |\mathbf k| = \omega$, and $E = \sqrt{\omega^2 + m^2}$. In the final state the same two masses share the same total energy with opposite momenta, so the magnitude is again $\omega$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]); the outgoing photon is turned by $\theta$ in the $xz$-plane, the electron goes the opposite way.
>
> **Step 2** (the products). $p\cdot k = E\omega - (-\omega\hat{\mathbf z})\cdot(\omega\hat{\mathbf z}) = E\omega + \omega^2$. $p\cdot k' = E\omega - (-\omega\hat{\mathbf z})\cdot(\omega\sin\theta, 0, \omega\cos\theta) = E\omega + \omega^2\cos\theta$.
>
> **Step 3** ($s$). $p + k = (E + \omega, \mathbf 0)$; and $(p + k)^2 = m^2 + 2p\cdot k$ by [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]].

^der-c8a-17-6

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-5|P8, step 5]]

> [!theorem] Theorem §C8a.17.7: At High Energy Compton Scattering Peaks in the Backward Direction
> For $E, \omega \gg m$, in the centre-of-mass frame:
> 1. the terms proportional to $m^2$ and $m^4$ in [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] are negligible, $p\cdot k \simeq 2\omega^2$, and $p\cdot k' \simeq \omega^2(1 + \cos\theta)$, which vanishes at $\theta = \pi$;
> 2. hence
>
> $$
> \frac14\sum_{\rm spins,\,pols}|\mathcal M|^2 \simeq 2e^4\left[\frac{1 + \cos\theta}{2} + \frac{2}{1 + \cos\theta}\right] \simeq \frac{4e^4}{1 + \cos\theta} \quad (\theta \text{ near } \pi) ;
> $$
>
> the term $p\cdot k/p\cdot k'$ dominates where the photon is scattered straight back;
> 3. the cross section from the dominant term is
>
> $$
> \frac{d\sigma}{d\Omega}\bigg|_{\text{high energy}} = \frac{1}{64\pi^2 s}\cdot\frac14\sum|\mathcal M|^2 \simeq \frac{e^4}{16\pi^2 s}\,\frac{1}{1 + \cos\theta} = \frac{\alpha^2}{s}\,\frac{1}{1 + \cos\theta} ;
> $$
>
> 4. the total cross section computed from it, $\sigma_{\rm tot} = \dfrac{2\pi\alpha^2}{s}\displaystyle\int\frac{d\cos\theta}{1 + \cos\theta}$, diverges logarithmically at $\theta \to \pi$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized, $s \gg m^2$; items 2–4 with $m$ set to zero, which fails within an angle of order $m/\omega$ of the backward direction ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]]). The prefactor $\frac{1}{64\pi^2s}$ of item 3 is exact at every energy.
>
> *Source: PHY 513 Lecture 22, slide 25 ("High Energy: $E, \omega \gg m$: terms proportional to $m^2$ and $m^4$ negligible. $p\cdot k = \omega(E + \omega) \simeq 2\omega^2$, $p\cdot k' = \omega(E + \omega\cos\theta) \simeq \omega^2(1 + \cos\theta)$, $= 0$ for $\theta = \pi$. Dominant contribution: photon scatters straight backwards. $\frac14\sum_{\rm spin}|\mathcal M|^2 = 2e^4\frac{p\cdot k}{p\cdot k'} = 2e^4\cdot\frac{2}{1 + \cos\theta}$"), slide 26 ("$= \frac{e^4}{16\pi^2s}\frac{1}{1 + \cos\theta} = \frac{\alpha^2}{s}\frac{1}{1 + \cos\theta}$. Total cross-section diverges in backward direction $\theta \sim \pi$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, subsection "High energy in the center of mass" · PS §5.5, eq. (5.93) · Yu §8.6.3, eqs. (8.405)–(8.407)*

^thm-c8a-17-7

> [!derivation]- Derivation
> **Step 1** (the invariants). For $\omega \gg m$, $E = \sqrt{\omega^2 + m^2} \simeq \omega$. In [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]]: $p\cdot k \simeq 2\omega^2$ and $p\cdot k' \simeq \omega^2(1 + \cos\theta)$.
>
> **Step 2** (the amplitude). The ratios: $\frac{p\cdot k'}{p\cdot k} \simeq \frac{1 + \cos\theta}{2}$, at most 1, and $\frac{p\cdot k}{p\cdot k'} \simeq \frac{2}{1 + \cos\theta}$, unbounded as $\theta \to \pi$. The mass terms are dropped: $m^2\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr)$ is of order $m^2/\omega^2$ away from the backward direction. Near $\theta = \pi$ the second ratio alone remains: $2e^4\cdot\frac{2}{1 + \cos\theta}$.
>
> **Step 3** (the cross-section formula). [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], 1, with $E_A = E$, $E_B = \omega$, $|\mathbf v_A - \mathbf v_B| = \frac\omega E + 1 = \frac{E + \omega}{E}$ (the particles move towards each other), $|\mathbf p_1| = \omega$ and $E_{\rm cm} = E + \omega$:
>
> $$
> \frac{1}{2E\cdot2\omega\cdot\frac{E + \omega}{E}}\cdot\frac{\omega}{16\pi^2(E + \omega)} = \frac{1}{64\pi^2(E + \omega)^2} = \frac{1}{64\pi^2 s} .
> $$
>
> No approximation is made in this step. The number is that of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]: what matters there is that the final momentum of the phase space cancels the initial momentum of the flux factor, and here both equal $\omega$.
>
> **Step 4** (insert). $\frac{1}{64\pi^2s}\cdot\frac{4e^4}{1 + \cos\theta} = \frac{e^4}{16\pi^2s}\frac{1}{1 + \cos\theta}$, and $e^4 = 16\pi^2\alpha^2$.
>
> **Step 5** (the total). $\int d\Omega = 2\pi\int d\cos\theta$; near $\cos\theta = -1$, $\int\frac{d\cos\theta}{1 + \cos\theta} = \log(1 + \cos\theta)$ diverges at the lower limit.
>
> **What the derivation shows.**
> - ⚑ By-product: the dominant term $p\cdot k/p\cdot k'$ is the square of diagram (b) alone, and at $m = 0$ there is no interference ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^der-c8a-15-7|Derivation §C8a.15.7]], closing remarks): the backward peak belongs to the $u$-channel diagram.
> - ⚑ By-product: the divergence came from dropping $m$ in a quantity that becomes small → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]].
> - ⚑ By-product: the peak is $1/(1 + \cos\theta)$ and not the square of the propagator, $1/(1 + \cos\theta)^2$ → [[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]].

^der-c8a-17-7

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-6|P8, step 6]]

> [!caution] Caution: The prefactor on slide 26
> Slide 26 writes the first line as $\frac{d\sigma}{d\Omega} = \frac{1}{64\pi E_{\rm cm}^2}\cdot\frac14\sum|\mathcal M|^2$. The prefactor is $\frac{1}{64\pi^2E_{\rm cm}^2}$, with $\pi^2$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^der-c8a-17-7|Derivation §C8a.17.7]], Step 3; [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]). The next line of the slide, $\frac{e^4}{16\pi^2s}\frac{1}{1 + \cos\theta}$, has it right.
>
> *Source: PHY 513 Lecture 22, slide 26 · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", fourth item*

^cau-c8a-17-1

> [!remark] Remark: The physical origin of the backward peak
> $p\cdot k'$ is, up to the factor $-2$, the denominator of the propagator of diagram (b) ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]). When it is small, the momentum squared of the virtual electron is close to $m^2$: the virtual electron is nearly on shell ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]). An amplitude becomes very large when the virtual particle that mediates the process gets close to its mass shell.
>
> *Source: PHY 513 Lecture 22, slide 27 ("Physical origin: virtual fermion nearly on-shell. $p\cdot k' = \omega(E + \omega\cos\theta) \sim 0$ for $\theta \sim \pi$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, paragraph "The physical origin"*

^rem-c8a-17-2

> [!theorem] Theorem §C8a.17.8: The Electron Mass Keeps the Total Cross Section Finite
> Keeping the mass in the quantity that becomes small,
>
> $$
> \frac{p\cdot k'}{\omega^2} = \frac E\omega + \cos\theta \simeq 1 + \cos\theta + \frac{2m^2}{s} ,
> $$
>
> which cannot go to zero. With this regulator at small backward angles,
>
> $$
> \sigma_{\rm tot} \simeq \frac{2\pi\alpha^2}{s}\int_{-1}^{1}\frac{d\cos\theta}{1 + \cos\theta + 2m^2/s} = \frac{2\pi\alpha^2}{s}\,\log\Bigl(1 + \frac{s}{m^2}\Bigr) \simeq \frac{2\pi\alpha^2}{s}\,\log\frac{s}{m^2} .
> $$
>
> 1. The total cross section at high energy is large, logarithmically in $s/m^2$, and finite. It would diverge only for a massless electron.
> 2. The main dependence, $\alpha^2/s$, follows from dimensional analysis; the nearly on-shell electron adds the logarithm.
> 3. The terms with $m^2$ and $m^4$ of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] stay of order one even at $\theta = \pi$, negligible next to $p\cdot k/p\cdot k' \sim s/m^2$.
> 4. Refinement (filled in by the user's notes): keeping the subleading term $\frac{1 + \cos\theta}{2}$ of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], 2, as well gives $\sigma_{\rm tot} \simeq \dfrac{2\pi\alpha^2}{s}\Bigl[\log\dfrac{s}{m^2} + \dfrac12\Bigr]$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized, $s \gg m^2$; items 1–2 at leading logarithmic accuracy; item 4 includes the constant next to the logarithm.
>
> *Source: PHY 513 Lecture 22, slide 27 ("Effective small angle regulator $\frac{2m^2}{s}$ from improved estimate: $\frac E\omega + \cos\theta \sim \sqrt{1 + \frac{m^2}{\omega^2}} + \cos\theta \sim 1 + \cos\theta + \frac{2m^2}{s}$. Large (but finite) total cross-section at high energy $s$: $\sigma_{\rm tot} = \frac{2\pi\alpha^2}{s}\int_{\theta\sim\pi}\frac{1}{1 + \cos\theta + \frac{2m^2}{s}}d\cos\theta = \frac{2\pi\alpha^2}{s}\log\frac{s}{m^2}$"), and transcript (the answer to the question about the mass) · the user's PHY 513 notes, Lecture 22 update, §22.3, paragraph "Asked in the lecture: what about the mass?" and Principle "High-energy total cross section" (item 4 filled in by the user's notes, "checked numerically against the full [formula] for $s/m^2$ up to $10^{10}$"; checked here up to $4\cdot10^8$) · PS §5.5, eqs. (5.94)–(5.96) and p. 164 ("The main dependence $\alpha^2/s$ follows from dimensional analysis. But the singularity associated with backward scattering of photons leads to an enhancement by an extra logarithm of the energy") · Yu §8.6.3, eqs. (8.408)–(8.411)*

^thm-c8a-17-8

> [!derivation]- Derivation
> **Step 1** (keep the mass). Exactly, $\frac{p\cdot k'}{\omega^2} = \frac{E}{\omega} + \cos\theta$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]]). Expand $\frac E\omega = \sqrt{1 + \frac{m^2}{\omega^2}} \simeq 1 + \frac{m^2}{2\omega^2}$, and $s = (E + \omega)^2 \simeq 4\omega^2$, so $\frac{m^2}{2\omega^2} \simeq \frac{2m^2}{s}$.
>
> **Step 2** (the regulated cross section). In [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]] replace $1 + \cos\theta$ by $1 + \cos\theta + \frac{2m^2}{s}$ in the dominant term: $\frac{d\sigma}{d\Omega} \simeq \frac{\alpha^2}{s}\,\frac{1}{1 + \cos\theta + 2m^2/s}$, i.e. $\frac{d\sigma}{d\cos\theta} \simeq \frac{2\pi\alpha^2}{2m^2 + s(1 + \cos\theta)}$ (PS (5.94)).
>
> **Step 3** (integrate). With $\varepsilon_m \equiv 2m^2/s$: $\int_{-1}^{1}\frac{dc}{1 + c + \varepsilon_m} = \log\frac{2 + \varepsilon_m}{\varepsilon_m} = \log\Bigl(1 + \frac{2}{\varepsilon_m}\Bigr) = \log\Bigl(1 + \frac{s}{m^2}\Bigr)$.
>
> **Step 4** (item 3). At $\theta = \pi$: $p\cdot k' \simeq \frac{m^2}{2}$ and $p\cdot k \simeq \frac s2$, so $2m^2\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr) \simeq -4$ and $m^4\bigl(\cdots\bigr)^2 \simeq 4$, of order one, while $\frac{p\cdot k}{p\cdot k'} \simeq \frac{s}{m^2}$.
>
> **Step 5** (item 4). With both terms, $\frac{d\sigma}{d\Omega} \simeq \frac{\alpha^2}{s}\bigl[\frac{1 + c}{4} + \frac{1}{1 + c + \varepsilon_m}\bigr]$, and $2\pi\int_{-1}^{1}\frac{1 + c}{4}\,dc = \pi$: $\sigma_{\rm tot} \simeq \frac{\pi\alpha^2}{s}\bigl[1 + 2\log\bigl(1 + \frac{s}{m^2}\bigr)\bigr]$.
>
> **What the derivation shows.**
> - A quantity that vanishes in the massless approximation must be computed to the next order before it is put in a denominator.
> - The regulator acts within an angle $\chi = \pi - \theta$ of order $m/\omega$ of the backward direction: there $1 + \cos\theta \simeq \chi^2/2$ is comparable to $2m^2/s \simeq m^2/2\omega^2$ → [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-1|Theorem §C8b.10.1]].

^der-c8a-17-8

*Uses:* [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]]

![[ph-qft-c8a-17-3.svg]]
*ADDED figure (not in the sources): the high-energy cross section in the centre-of-mass frame, on a logarithmic scale. Dashed: the massless form $1/(1 + \cos\theta)$ of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], which diverges at $\theta = \pi$. Solid: both terms with the regulator $2m^2/s$ of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]], for $s/m^2 = 10^2$ and $10^4$; the peak value is about $s/2m^2$.*

One point remains puzzling. The propagator of diagram (b) is of order $1/(1 + \cos\theta)$ in the amplitude, so its square would give $1/(1 + \cos\theta)^2$; yet the cross section has a single power. The backward peak is large, but less large than the propagator alone suggests. The reason is the helicity structure of the amplitude: [[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]].

> [!remark] Remark: Lecture 22 at a glance
> - Two diagrams, $s$- and $u$-channel, with a virtual electron between the photon vertices; external photons contribute $\epsilon_\nu(k)$ in and $\epsilon^\ast_\mu(k')$ out ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]]).
> - The Dirac equation simplifies the numerators, $(\slashed p + m)\gamma^\nu u(p) = 2p^\nu u(p)$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|Lemma §C8a.15.4]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]]); the square is one trace of eight $\gamma$'s for each term ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]]), with the result of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]].
> - The Ward identity $k_\mu\mathcal M^\mu = 0$ follows from current conservation, holds order by order but not diagram by diagram, and makes the timelike and longitudinal polarizations cancel, so that $\sum\epsilon^\ast_\mu\epsilon_\nu \to -g_{\mu\nu}$ ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]], [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]]).
> - Kinematics alone gives $\omega'(\theta)$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]]); QED gives the intensity, the Klein–Nishina formula ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|Theorem §C8a.17.4]]), with the Thomson limit $8\pi\alpha^2/3m^2$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-5|Theorem §C8a.17.5]]).
> - At high energy backward scattering dominates because the virtual electron is nearly on shell, and $\sigma \simeq (2\pi\alpha^2/s)\log(s/m^2)$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]]); angular momentum forbids helicity-conserving scattering exactly backward, which weakens the enhancement from $1/\chi^4$ to $1/(\omega^2\chi^2 + m^2)$ and controls the polarization of inverse-Compton photons ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^ex-c8b-10-1|Example §C8b.10.1]]).
>
> *Source: the user's PHY 513 notes, Lecture 22 update, §22.4, Principle "Compton scattering" · PHY 513 Lecture 22, slide 3 (outline)*

^rem-c8a-17-3

> [!remark] Remark: Correspondence with Yu and Peskin–Schroeder
> Yu §8.6 covers the lecture with his own labels: $k_1$, $k_2$ for the incoming electron and photon, $p_1$, $p_2$ for the outgoing ones; his $\theta$ is the angle used here in both frames.
>
> | topic | here | PS §5.5 | Yu §8.6 |
> |---|---|---|---|
> | diagrams, amplitude, denominators, simplified amplitude | [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1\|Theorem §C8a.15.1]]–[[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5\|Theorem §C8a.15.5]] | pp. 158–159, (5.74) | (8.321)–(8.324) |
> | physical sum, current argument, Ward identity, gauge view, replacement by $-g_{\mu\nu}$ | [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1\|Theorem §C8a.16.1]]–[[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3\|Theorem §C8a.16.3]] | (5.75)–(5.80) | (8.325)–(8.337) |
> | traces and the averaged $\lvert\mathcal M\rvert^2$ | [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6\|Theorem §C8a.15.6]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7\|Theorem §C8a.15.7]] | (5.81)–(5.82), (5.87) | (8.348)–(8.349), (8.380)–(8.383) |
> | Compton formula, lab kinematics | [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1\|Theorem §C8a.17.1]] | (5.88)–(5.89) | (8.319), (8.384)–(8.392) |
> | phase space, Klein–Nishina, Thomson | [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2\|Theorem §C8a.17.2]]–[[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-5\|Theorem §C8a.17.5]] | (5.90)–(5.92) | (8.320), (8.393)–(8.401), Fig. 8.14 |
> | centre-of-mass invariants, backward peak, the mass regulator | [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6\|Theorem §C8a.17.6]]–[[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8\|Theorem §C8a.17.8]] | (5.93)–(5.96) | (8.402)–(8.411) |
> | helicity amplitudes and helicity suppression | [[§C8b.10 Helicity Suppression in Backward Compton Scattering\|§C8b.10]] | (5.97)–(5.104) | (8.412)–(8.457) |
>
> Yu's centre-of-mass frame has the incoming electron along $+\hat{\mathbf z}$; the course's has the incoming photon there. PS and Yu evaluate the traces through intermediate forms in other variables; [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] writes them in $p\cdot k$ and $p\cdot k'$ throughout.
>
> *Source: the user's PHY 513 notes, Lecture 22 update, paragraph "Correspondence with Yu" · PS and Yu pages as listed in the Sources line (equation numbers checked on the page images of the current build)*

^rem-c8a-17-4

> [!abstract]- Mathematical background
> Proved in CA; the line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] — a delta function of a function with a simple zero, $\delta(f(x)) = \delta(x - x_0)/|f'(x_0)|$: the factor $1/|f'|$ of the energy delta function in the lab-frame phase space ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|Theorem §C8a.17.2]], Step 4 of its derivation).

> [!remark]- Connections
> - The other QED cross sections of the course, built with the same three factors: $e^+e^- \to \mu^+\mu^-$ ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-4|Theorem §C8a.8.4]]) and $e^-\mu^- \to e^-\mu^-$ ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|Theorem §C8a.13.4]]), both in the centre-of-mass frame; Klein–Nishina is the first in the rest frame of a target that recoils. The formulas of [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential|§C6b.10]] are for a fixed target described by an external potential, which does not recoil, and do not apply here.
> - A second peak caused by a virtual particle close to its mass shell: the photon of $e^-\mu^-$ scattering in the forward direction, $1/\theta^4$ — [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]]; there the exchanged particle is a photon and the peak is the full square of the propagator, here it is an electron and the peak is weaker ([[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]]).
> - The Thomson cross section is the classical scattering of light by a free charge; the dimensionless measure of the photon energy that decides between the two regimes is $\omega/m$, the ratio of the Compton wavelength to the wavelength of the light ([[§C1a.2 Natural Units and Dimensional Analysis|§C1a.2]], [[§B4.1 The Klein–Gordon Equation#^def-b4-1-2|REL Def. §B4.1.2]]).
> - Helicity suppression of the backward peak, and inverse Compton scattering — [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^ex-c8b-10-1|Example §C8b.10.1]].
