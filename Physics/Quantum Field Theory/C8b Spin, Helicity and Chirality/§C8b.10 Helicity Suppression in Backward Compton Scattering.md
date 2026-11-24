---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.9 Photon Helicity|§C8b.9]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]] →

*Sources: PHY 513 Lecture 22 (Larsen, 23 Nov 2026, "Compton Scattering"), slides 28–31 (end of Part C), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, subsection "Helicity suppression" (Derivation "Exactly backward, the helicity-conserving amplitude vanishes", paragraph "The way out", Principle "Inverse Compton scattering"), Caution "Slips in the slides" (items 5–7), paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.5, pp. 165–167, eqs. (5.97)–(5.104), Figure 5.6 (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.6.3, eqs. (8.412)–(8.415), (8.439)–(8.457) (page images of the current build checked).*

Why is the backward peak of Compton scattering not even larger? At high energy the cross section is dominated by photons scattered straight back, because the virtual electron of the $u$-channel diagram is nearly on shell ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^rem-c8a-17-2|§C8a.17, Remark: The physical origin of the backward peak]]). The propagator is of order $1/(1 + \cos\theta)$ in the amplitude, so its square suggests $1/(1 + \cos\theta)^2$ in the cross section; the result has a single power. A single power of $1 + \cos\theta$ is the mark of helicity structure (compare the $(1 \pm \cos\theta)^2$ of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]). The nearly on-shell particle is an electron, whose propagator has a numerator: the denominator is small, and the numerator turns out to be small as well. Exactly backward, conservation of angular momentum forbids the helicity-conserving amplitude ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]]); what survives near the backward direction is suppressed by the angle or by the mass ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]]). The section belongs to this chapter because it uses its tools: the helicity spinors ([[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]]), helicity conservation at the vertex ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]) and the photon helicity vectors ([[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]]).

**The mathematical picture.** At high energy a Dirac spinor of definite helicity lives in one Weyl half ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]), and each $\gamma^\mu$ maps one half into the other, with $\sigma^\mu$ or $\bar\sigma^\mu$ as its block. A chain of three $\gamma$'s between two right-handed spinors is therefore a product of three $2\times2$ matrices between two-spinors ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]]). Along the collision axis the remaining symmetry is the group of rotations about $\hat{\mathbf z}$, and each factor has a definite effect on $s_z$: the photon factors $\sigma^1 \pm i\sigma^2$ raise or lower it by one unit, the spin of the photon, and a diagonal matrix leaves it unchanged. The selection rule is the conservation of $J_z$.

**Setup.** [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]] at order $e^2$, in the centre-of-mass frame of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]] at high energy, $E, \omega \gg m$: the photon comes in along $+\hat{\mathbf z}$, the electron along $-\hat{\mathbf z}$. The external states have definite helicities; spinors in the chiral basis, in their high-energy form ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2: corrections of relative size $m/2E$).

*Conventions* ([[Larsen PHY 513]]): momenta and indices as in [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square|§C8a.15]] ($\nu$ for the incoming photon, $\mu$ for the outgoing one; slide 29 uses the opposite letters). $\chi \equiv \pi - \theta$ is the angle away from the backward direction. R and L denote helicity $+\frac12$, $-\frac12$ for the electron and $+1$, $-1$ for a photon; $h$, $h'$ are the helicities of the incoming and the outgoing photon. $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$; for a four-vector $v$, $\sigma\cdot v \equiv \sigma^\mu v_\mu$ and $\bar\sigma\cdot v \equiv \bar\sigma^\mu v_\mu$; $\sigma_\pm \equiv \frac12(\sigma^1 \pm i\sigma^2)$ are the raising and lowering matrices of $s_z$. Amplitudes are given up to phases that depend on the conventions for the spinors and polarization vectors.

## The denominator near the backward direction

> [!theorem] Theorem §C8b.10.1: The Backward Denominator
> In the centre-of-mass frame, with $\chi = \pi - \theta$, the denominator of the $u$-channel propagator ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]) is
>
> $$
> (p - k')^2 - m^2 = -2\,p\cdot k' = -2\omega\,(E + \omega\cos\theta) \simeq -(\omega^2\chi^2 + m^2) \qquad (m \ll \omega,\ \chi \ll 1) .
> $$
>
> 1. It is small compared with $s \simeq 4\omega^2$ over a whole range of angles, not only at one point.
> 2. For $m/\omega \ll \chi \ll 1$ the propagator contributes $1/\omega^2\chi^2$ to the amplitude; by itself this would give $|\mathcal M|^2 \sim 1/\chi^4$.
> 3. The spin-averaged result is $\frac14\sum|\mathcal M|^2 \simeq \frac{4e^4}{1 + \cos\theta} \simeq \frac{8e^4}{\chi^2}$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]): one power of $\chi^2$ less. The numerator of the propagator, $\slashed p - \slashed k' + m$, must supply a compensating factor of order $\chi$ in the amplitude.
>
> *Model:* kinematics; *applies:* $\gamma e \to \gamma e$ in the centre-of-mass frame; the last form for $m \ll \omega$ and $\chi \ll 1$.
>
> *Source: PHY 513 Lecture 22, slide 28 ("Denominator in propagator small for a range of angles … $\simeq -(\omega^2\chi^2 + m^2)$ [with $\chi = \pi - \theta$]. Puzzle: … expected $|\mathcal M|^2 \sim \frac{1}{\chi^4}$. Clue: $(1 + \cos\theta)$ dependence suggests helicity structure. Nearly on-shell particle is an electron with propagator $S_F = \frac{i(\slashed p - \slashed k' + m)}{(p - k')^2 - m^2}$. Denominator is small, but numerator may also be small"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, subsection "Helicity suppression" · PS §5.5, eq. (5.98) and the paragraph after it*

^thm-c8b-10-1

> [!derivation]- Derivation
> **Step 1** (exact). $(p - k')^2 - m^2 = -2p\cdot k'$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]) and $p\cdot k' = \omega(E + \omega\cos\theta)$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]]). With $\cos\theta = -\cos\chi$: $E + \omega\cos\theta = E - \omega\cos\chi$.
>
> **Step 2** (expand). $E = \sqrt{\omega^2 + m^2} \simeq \omega + \frac{m^2}{2\omega}$ and $\cos\chi \simeq 1 - \frac{\chi^2}{2}$:
>
> $$
> E - \omega\cos\chi \simeq \frac{m^2}{2\omega} + \frac{\omega\chi^2}{2} , \qquad -2\omega\,(E - \omega\cos\chi) \simeq -(m^2 + \omega^2\chi^2) .
> $$
>
> **Step 3** (item 3). $1 + \cos\theta = 1 - \cos\chi \simeq \chi^2/2$.
>
> **What the derivation shows.**
> - The two small quantities, the angle and the mass, enter the denominator on the same footing, as $\omega^2\chi^2 + m^2$; the regulator $2m^2/s$ of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]] is the $m^2$ here.

^der-c8b-10-1

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]

> [!caution] Caution: Two expressions on slide 28
> Slide 28 writes "$(p - k')^2 - m^2 = -2p'\cdot k = \omega(E + \omega\cos\theta) \simeq -(\omega^2\chi^2 + m^2)$". The middle expression lacks a factor $-2$: it is $-2\omega(E + \omega\cos\theta)$ (and $p'\cdot k = p\cdot k'$ by momentum conservation). The approximate form at the end is correct. The same slide says "High energy propagator $\sim \omega^2\chi^2$": this is the size of the denominator; the propagator is of order $1/\omega^2\chi^2$.
>
> *Source: PHY 513 Lecture 22, slide 28 · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", fifth item (checked numerically)*

^cau-c8b-10-1

## The numerator between helicity states

> [!theorem] Theorem §C8b.10.2: The u-Channel Numerator as a Product of 2×2 Matrices
> Let the incoming electron be right-handed at high energy, $u_R(p) = \sqrt{2E}\,(0, \xi_{\rm in})^{\mathsf T}$ with $\xi_{\rm in} = \xi_+(\hat{\mathbf p})$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]), and write the outgoing spinor in halves, $u(p') = (u'_L, u'_R)^{\mathsf T}$. The spinor string of diagram (b) of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]] splits into two parts:
> 1. **the part with $\slashed p - \slashed k'$** reaches only the right-handed half of the outgoing electron,
>
> $$
> \bar u(p')\,\gamma^\nu\epsilon_\nu(k)\,(\slashed p - \slashed k')\,\gamma^\mu\epsilon^\ast_\mu(k')\,u_R(p) = \sqrt{2E}\;u_R'^{\,\dagger}\,\bigl(\sigma\cdot\epsilon(k)\bigr)\,\bigl(\bar\sigma\cdot(p - k')\bigr)\,\bigl(\sigma\cdot\epsilon^\ast(k')\bigr)\,\xi_{\rm in} ,
> $$
>
> which for an outgoing right-handed electron, $u'_R = \sqrt{2E}\,\xi_{\rm out}$, is $2E\;\xi_{\rm out}^\dagger\,(\sigma\cdot\epsilon)\,(\bar\sigma\cdot(p - k'))\,(\sigma\cdot\epsilon^\ast)\,\xi_{\rm in}$: the electron keeps its helicity;
> 2. **the part with $m$** reaches only the left-handed half,
>
> $$
> \bar u(p')\,\gamma^\nu\epsilon_\nu(k)\;m\;\gamma^\mu\epsilon^\ast_\mu(k')\,u_R(p) = m\,\sqrt{2E}\;u_L'^{\,\dagger}\,\bigl(\bar\sigma\cdot\epsilon(k)\bigr)\,\bigl(\sigma\cdot\epsilon^\ast(k')\bigr)\,\xi_{\rm in} :
> $$
>
> the mass in the numerator of the propagator flips the helicity of the electron. Helicity conservation fails by terms proportional to $m$;
> 3. for a left-handed incoming electron the same holds with $\sigma$ and $\bar\sigma$ exchanged.
>
> Item 1 is helicity conservation at the two vertices ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]) carried through the propagator; item 2 is the mass connecting the two chiral blocks ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-2|§C8b.5, Remark: The mass is what connects the two chiral blocks]]). Both are instances of the general rule: between two $u$ spinors at high energy three $\gamma$'s join equal helicities and two $\gamma$'s opposite ones ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]], from [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]]); the sentences of PS pp. 165–166 on the two terms and Yu's (8.451) are in [[§C8b.6 Helicity Conservation at the QED Vertex#^ex-c8b-6-1|Example §C8b.6.1]].
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* the string of diagram (b) with high-energy spinors, corrections of relative order $m/E$; any polarization vectors.
>
> *Source: PHY 513 Lecture 22, slide 29 ("For initial (so also final) electron helicity R amplitude is proportional to: $\bar u_R(\gamma^\mu\epsilon_\mu)(\slashed p - \slashed k')(\gamma^\nu\epsilon^\ast_\nu)u_R = \xi^\dagger_R(\sigma^\mu\epsilon_\mu)\,\bar\sigma^\lambda(p_\lambda - k'_\lambda)\,(\sigma^\nu\epsilon^\ast_\nu)\xi_R$"), slide 30 ("Virtual electron violates helicity conservation (proportional to $m$)"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Derivation "Exactly backward, the helicity-conserving amplitude vanishes", paragraph "The way out" · PS §5.5, eqs. (5.97), (5.99) · the block multiplication written out here (both parts checked numerically)*

^thm-c8b-10-2

> [!derivation]- Derivation
> In the chiral basis $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$: contracted with a vector $v$, it sends a column $(0, x)^{\mathsf T}$ to $\bigl((\sigma\cdot v)x, 0\bigr)^{\mathsf T}$ and a column $(y, 0)^{\mathsf T}$ to $\bigl(0, (\bar\sigma\cdot v)y\bigr)^{\mathsf T}$. The row is $\bar u(p') = u(p')^\dagger\gamma^0 = (u_R'^{\,\dagger}, u_L'^{\,\dagger})$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]).
>
> **Step 1** (first vertex). $\gamma^\mu\epsilon^\ast_\mu(k')\,u_R(p) = \sqrt{2E}\,\bigl((\sigma\cdot\epsilon^\ast)\xi_{\rm in}, 0\bigr)^{\mathsf T}$: the column is now in the upper half.
>
> **Step 2** (the propagator numerator). With $q \equiv p - k'$: $\slashed q$ sends the upper half to the lower one, $\sqrt{2E}\,\bigl(0, (\bar\sigma\cdot q)(\sigma\cdot\epsilon^\ast)\xi_{\rm in}\bigr)^{\mathsf T}$. The term $m$ is a multiple of the unit matrix and leaves the column in the upper half, $m\sqrt{2E}\,\bigl((\sigma\cdot\epsilon^\ast)\xi_{\rm in}, 0\bigr)^{\mathsf T}$.
>
> **Step 3** (second vertex). $\gamma^\nu\epsilon_\nu(k)$ exchanges the halves once more: the $\slashed q$ part becomes $\sqrt{2E}\,\bigl((\sigma\cdot\epsilon)(\bar\sigma\cdot q)(\sigma\cdot\epsilon^\ast)\xi_{\rm in}, 0\bigr)^{\mathsf T}$, the mass part $m\sqrt{2E}\,\bigl(0, (\bar\sigma\cdot\epsilon)(\sigma\cdot\epsilon^\ast)\xi_{\rm in}\bigr)^{\mathsf T}$.
>
> **Step 4** (the row). $\bar u(p')$ multiplies an upper entry by $u_R'^{\,\dagger}$ and a lower entry by $u_L'^{\,\dagger}$: items 1 and 2. For an outgoing electron of helicity $+\frac12$ at high energy $u'_L \to 0$ and $u'_R = \sqrt{2E}\,\xi_+(\hat{\mathbf p}')$; for helicity $-\frac12$, $u'_R \to 0$ and $u'_L = \sqrt{2E}\,\xi_-(\hat{\mathbf p}')$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]).
>
> **Step 5** (item 3). A left-handed spinor is $(x, 0)^{\mathsf T}$; every step exchanges the roles of the halves and of $\sigma$, $\bar\sigma$.
>
> **What the derivation shows.**
> - ⚑ By-product: the two terms of the numerator, $\slashed p - \slashed k'$ and $m$, lead to different final helicities; they do not interfere, and their squares add → [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], 4.
> - The $4\times4$ algebra has become $2\times2$ algebra with a transparent meaning: the outer factors are the photons acting on the spin of the electron.

^der-c8b-10-2

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-7|P9, step 7]]

## Exactly backward

> [!theorem] Theorem §C8b.10.3: Exactly Backward the Helicity-Conserving Amplitude Vanishes
> ![[ph-qft-c8b-10-1.svg]]
> *ADDED figure (after PS Figure 5.6 and PHY 513 Lecture 22, slide 29): momenta (black) and spins (red, thick) along the axis for $\theta = \pi$, all four particles right-handed. The total $J_z$ before and after differ by one unit.*
>
> At $\theta = \pi$, for an incoming right-handed electron and an outgoing right-handed electron:
> 1. **the spinors.** The incoming electron moves along $-\hat{\mathbf z}$, so $s_z = -\frac12$ and $\xi_{\rm in} = (0, 1)^{\mathsf T}$; the outgoing one moves along $+\hat{\mathbf z}$, $s_z = +\frac12$ and $\xi_{\rm out}^\dagger = (1, 0)$. The electron line must raise $s_z$ by one unit;
> 2. **the photons.** The incoming photon moves along $+\hat{\mathbf z}$; with helicity $h = \pm1$ it has $s_z = \pm1$ and $\sigma\cdot\epsilon(k) = -\sqrt2\,\sigma_\pm$. The outgoing photon moves along $-\hat{\mathbf z}$; with helicity $h' = \pm1$ it has $s_z = \mp1$, and it enters through the complex conjugate vector, $\sigma\cdot\epsilon^\ast(k') = -\sqrt2\,\sigma_\pm$. Absorbing a photon with $s_z = +1$ and emitting one with $s_z = -1$ both raise the $s_z$ of the electron;
> 3. **the propagator.** $p - k' = (E - \omega, 0, 0, 0)$, so $\bar\sigma\cdot(p - k') = (E - \omega)\,\mathbb 1$: diagonal, it does not change $s_z$;
> 4. **the product.** The two photon factors change $s_z$ by $+2$, $0$ or $-2$, never by $+1$:
>
> $$
> \xi_{\rm out}^\dagger\,\bigl(\sigma\cdot\epsilon(k)\bigr)\,\bigl(\bar\sigma\cdot(p - k')\bigr)\,\bigl(\sigma\cdot\epsilon^\ast(k')\bigr)\,\xi_{\rm in} = 0 \qquad\text{for all four choices of } h, h' .
> $$
>
> For both photons right-handed, the case that is enhanced away from the axis: $\sigma_+$ takes $(0, 1)^{\mathsf T}$ to $(1, 0)^{\mathsf T}$, the unit matrix leaves it there, and the second $\sigma_+$ annihilates it. A lowering matrix in the middle would be needed;
> 5. **angular momentum.** Orbital angular momentum has no component along the axis of a collinear configuration. Before, $J_z = h - \frac12$; after, $J_z = \frac12 - h'$. Conservation requires $h + h' = 1$, impossible for $h, h' = \pm1$: the amplitude violates the conservation of angular momentum and vanishes. The same holds with all helicities reversed.
>
> *Equivalently,* this is the argument of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]] for another process: spin flip along the beam is forbidden.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, exactly $\theta = \pi$ in the centre-of-mass frame, electron helicity conserved; items 1–4 for diagram (b) with high-energy spinors, item 5 for the whole amplitude and any energy.
>
> *Source: PHY 513 Lecture 22, slide 29 ("For backwards scattering amplitude vanishes unless initial (and final) γ also have helicity R: $\xi_R({\rm in}) = \binom01$, $s_z = -\frac12$; $\epsilon^\mu\cdot\sigma_\mu({\rm in}) = \frac{1}{\sqrt2}(\sigma_1 + i\sigma_2)$, $s_z = 1$; $\xi^\dagger_R({\rm out}) = (1\ 0)$, $s_z = \frac12$ … $\bar\sigma^\lambda(p_\lambda - k'_\lambda)$ diagonal ⇒ amplitude vanishes due to angular momentum conservation"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Derivation "Exactly backward, the helicity-conserving amplitude vanishes" · PS §5.5, eqs. (5.99)–(5.100), Figure 5.6 and p. 166 ("the total spin angular momentum of the final state is one unit less than that of the initial state") · the matrices and the angular-momentum count checked numerically*

^thm-c8b-10-3

> [!derivation]- Derivation
> **Step 1** (the two-spinors). The helicity two-spinor satisfies $\hat{\mathbf p}\cdot\boldsymbol\sigma\,\xi_\pm = \pm\xi_\pm$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]). For $\hat{\mathbf p} = -\hat{\mathbf z}$ and helicity $+$: $\sigma^3\xi = -\xi$, so $\xi_{\rm in} = (0, 1)^{\mathsf T}$ up to a phase. For $\hat{\mathbf p}' = +\hat{\mathbf z}$: $\xi_{\rm out} = (1, 0)^{\mathsf T}$.
>
> **Step 2** (the incoming photon). Along $+\hat{\mathbf z}$ the helicity vectors are $\epsilon^\mu = \frac{1}{\sqrt2}(0, 1, \pm i, 0)$ ([[§C8b.9 Photon Helicity#^ex-c8b-9-1|Example §C8b.9.1]]). With $\epsilon_\mu = (0, -\boldsymbol\epsilon)$: $\sigma\cdot\epsilon = -\boldsymbol\sigma\cdot\boldsymbol\epsilon = -\frac{1}{\sqrt2}(\sigma^1 \pm i\sigma^2) = -\sqrt2\,\sigma_\pm$.
>
> **Step 3** (the outgoing photon). Along $-\hat{\mathbf z}$ the helicity $\pm1$ vector is the one with $s_z = \mp1$, $\epsilon^\mu(k') = \frac{1}{\sqrt2}(0, 1, \mp i, 0)$ up to a phase (the vectors of Step 2 rotated by $\pi$ about $\hat{\mathbf y}$). The amplitude contains its complex conjugate, $\epsilon^{\ast\mu}(k') = \frac{1}{\sqrt2}(0, 1, \pm i, 0)$, so $\sigma\cdot\epsilon^\ast(k') = -\sqrt2\,\sigma_\pm$: for $h' = +1$ a raising matrix.
>
> **Step 4** (the middle factor). At $\theta = \pi$, $k' = (\omega, 0, 0, -\omega)$ and $p = (E, 0, 0, -\omega)$: the spatial parts cancel in $p - k'$. $\bar\sigma\cdot q = q^0 + \boldsymbol\sigma\cdot\mathbf q = E - \omega$.
>
> **Step 5** (the four products). $\sigma_+(0, 1)^{\mathsf T} = (1, 0)^{\mathsf T}$, $\sigma_-(0, 1)^{\mathsf T} = 0$, $\sigma_+(1, 0)^{\mathsf T} = 0$, $\sigma_-(1, 0)^{\mathsf T} = (0, 1)^{\mathsf T}$. For $h' = -1$ the first factor to act, $\sigma_-$, annihilates $\xi_{\rm in}$. For $h' = +1$ it gives $(1, 0)^{\mathsf T}$; then $h = +1$ gives $\sigma_+(1, 0)^{\mathsf T} = 0$, and $h = -1$ gives $(0, 1)^{\mathsf T}$, orthogonal to $\xi_{\rm out}$.
>
> **Step 6** (angular momentum). A particle moving along $\pm\hat{\mathbf z}$ with helicity $\lambda$ has $s_z = \pm\lambda$. Before: photon $+h$, electron $-\frac12$. After: photon $-h'$, electron $+\frac12$. $\mathbf L = \mathbf x\times\mathbf p$ has no component along $\mathbf p$, so $L_z = 0$ on the axis and $J_z$ is the sum of the $s_z$.
>
> **What the derivation shows.**
> - Exactly on the axis the zero is exact in $J_z$ counting, for any energy; the $2\times2$ computation shows how it comes about in the amplitude.
> - ⚑ By-product: a middle factor that changes $s_z$, or an electron that flips its helicity, evades the rule → [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]].

^der-c8b-10-3

*Uses:* [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]], [[§C8b.9 Photon Helicity#^ex-c8b-9-1|Example §C8b.9.1]], [[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-7|P9, step 7]]

> [!caution] Caution: The matrix of the outgoing photon on slide 29
> Slide 29 writes $\sigma^\nu\cdot\epsilon^\ast_\nu({\rm out}) = \frac{1}{\sqrt2}(\sigma_1 - i\sigma_2)$, a lowering matrix, with the label $s_z = -1$. For an outgoing photon with $s_z = -1$ the complex conjugate vector gives $\sigma^1 + i\sigma^2$, a raising matrix (up to an overall sign): [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]], 2. With the lowering matrix of the slide the product would vanish on $\xi_R({\rm in})$ whatever the propagator is. With the raising matrix it vanishes because $\bar\sigma\cdot(p - k')$ is diagonal, which is the argument that the slide states.
>
> *Source: PHY 513 Lecture 22, slide 29 · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", sixth item (checked numerically)*

^cau-c8b-10-2

## The two ways out

> [!theorem] Theorem §C8b.10.4: Near the Backward Direction the Enhancement Is Reduced by the Angle or by the Mass
> For $\chi \ll 1$ and $m \ll \omega$, two amplitudes with an incoming right-handed electron are enhanced by the small denominator of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-1|Theorem §C8b.10.1]]:
> 1. **not exactly backward.** $\bar\sigma\cdot(p - k')$ acquires an off-diagonal part of order $\omega\chi$, which changes $s_z$ by one unit. With all four particles right-handed,
>
> $$
> \bigl|\mathcal M(e^-_R\gamma_R \to e^-_R\gamma_R)\bigr| \simeq \frac{4e^2\,\omega^2\chi}{\omega^2\chi^2 + m^2} = \frac{4e^2\,\chi}{\chi^2 + m^2/\omega^2} ;
> $$
>
> it vanishes at $\chi = 0$. The final state has one unit of orbital angular momentum;
> 2. **helicity flip.** The mass term of the numerator turns the right-handed electron into a left-handed one ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]], 2):
>
> $$
> \bigl|\mathcal M(e^-_R\gamma_L \to e^-_L\gamma_R)\bigr| \simeq \frac{4e^2\,m\,\omega}{\omega^2\chi^2 + m^2} = \frac{4e^2\,m/\omega}{\chi^2 + m^2/\omega^2} ;
> $$
>
> it does not vanish at $\chi = 0$, and angular momentum then requires the helicity of the photon to flip as well, $h' = -h$;
> 3. the reactions with all four helicities reversed have the same magnitudes;
> 4. **the sum.** The two amplitudes have different final states and add in the square:
>
> $$
> \frac14\sum|\mathcal M|^2 \simeq \frac{8e^4\,\bigl[(\omega\chi)^2 + m^2\bigr]\,\omega^2}{(\omega^2\chi^2 + m^2)^2} = \frac{8e^4\,\omega^2}{\omega^2\chi^2 + m^2} , \qquad \frac{d\sigma}{d\cos\theta} \simeq \frac{4\pi\alpha^2}{s\,(\chi^2 + 4m^2/s)} ,
> $$
>
> which is the unpolarized result of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]] with the regulator of [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]].
>
> Backward scattering is enhanced by the nearly on-shell virtual electron and forbidden by the conservation of angular momentum. The enhancement wins, but by less than the propagator suggests: for $m/\omega \ll \chi \ll 1$, $|\mathcal M|^2 \sim 1/\chi^2$ in place of $1/\chi^4$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, centre-of-mass frame, $m \ll \omega$, $\chi \ll 1$; leading order in both. The lecture gives item 4 as an estimate of orders of magnitude, $|\mathcal M|^2 \sim \frac{(\omega\chi)^2 + m^2}{(\omega^2\chi^2 + m^2)^2} = \frac{1}{\omega^2\chi^2 + m^2}$, up to the power of $\omega$ that makes it dimensionless; the coefficients are those of PS.
>
> *Source: PHY 513 Lecture 22, slide 30 ("Backwards scattering is enhanced by on-shell virtual electron but forbidden by angular momentum conservation. Options: Scattering not exactly backwards: $\slashed p - \slashed k' \sim \sigma_R\,\omega\chi$ (off-diagonal). Virtual electron violates helicity conservation (proportional to $m$). Amplitude after suppressions accounted for is less enhanced: $|\mathcal M|^2 \sim \frac{(\omega\chi)^2 + m^2}{(\omega^2\chi^2 + m^2)^2} = \frac{1}{\omega^2\chi^2 + m^2}$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, paragraph "The way out" · PS §5.5, eqs. (5.101)–(5.103) and p. 166 ("It indicates that the final state is a $p$-wave, as required by angular momentum conservation") · the derivation below is written out here; all three formulas checked numerically against the full amplitude*

^thm-c8b-10-4

> [!derivation]- Derivation
> **Step 1** (the middle factor off the axis). With $\theta = \pi - \chi$: $k' = (\omega, \omega\sin\chi, 0, -\omega\cos\chi)$, so $q = p - k' = (E - \omega, -\omega\sin\chi, 0, -\omega(1 - \cos\chi))$ and
>
> $$
> \bar\sigma\cdot q = q^0 + \boldsymbol\sigma\cdot\mathbf q = (E - \omega)\,\mathbb 1 - \omega\sin\chi\;\sigma^1 - \omega(1 - \cos\chi)\,\sigma^3 \simeq -\omega\chi\,\sigma^1 + \frac{m^2}{2\omega}\,\mathbb 1 - \frac{\omega\chi^2}{2}\,\sigma^3 .
> $$
>
> The off-diagonal part is $-\omega\chi\,\sigma^1$, and $\sigma^1$ exchanges the two components of a two-spinor.
>
> **Step 2** (the product for item 1). To leading order the outer factors are those on the axis ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]]), for both photons right-handed:
>
> $$
> \xi_{\rm out}^\dagger\,(-\sqrt2\,\sigma_+)\,(-\omega\chi\,\sigma^1)\,(-\sqrt2\,\sigma_+)\,\xi_{\rm in} = -2\omega\chi\;(1, 0)\,\sigma_+\,\sigma^1\,\sigma_+\,(0, 1)^{\mathsf T} = -2\omega\chi ,
> $$
>
> since $\sigma_+(0, 1)^{\mathsf T} = (1, 0)^{\mathsf T}$, $\sigma^1(1, 0)^{\mathsf T} = (0, 1)^{\mathsf T}$ and again $\sigma_+(0, 1)^{\mathsf T} = (1, 0)^{\mathsf T}$. The diagonal parts of Step 1 contribute only together with a correction of relative order $\chi$ to an outer factor: terms of order $\chi\,m^2/\omega$ and $\omega\chi^3$, dropped against $\omega\chi$.
>
> **Step 3** (the amplitude of item 1). The string of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]], 1, is $2E\cdot(-2\omega\chi)$. In $i\mathcal M = -ie^2\,\epsilon^\ast_\mu\epsilon_\nu\,\bar u(p')\,\frac{\gamma^\nu(\slashed p - \slashed k' + m)\gamma^\mu}{(p - k')^2 - m^2}\,u(p)$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]]) with the denominator of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-1|Theorem §C8b.10.1]]:
>
> $$
> \mathcal M \simeq -e^2\,\frac{-4E\omega\chi}{-(\omega^2\chi^2 + m^2)} = -\frac{4e^2\,E\omega\chi}{\omega^2\chi^2 + m^2} , \qquad E \simeq \omega .
> $$
>
> The $s$-channel diagram has the large denominator $2p\cdot k \simeq s$ and is not enhanced.
>
> **Step 4** (item 2). In [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]], 2, the outgoing electron is left-handed and moves along $+\hat{\mathbf z}$: $u'_L = \sqrt{2E}\,\xi'$ with $\xi' = (0, 1)^{\mathsf T}$, $s_z = -\frac12$, the same two-spinor as $\xi_{\rm in}$. The product $(0, 1)\,(\bar\sigma\cdot\epsilon(k))\,(\sigma\cdot\epsilon^\ast(k'))\,(0, 1)^{\mathsf T}$ needs a raising matrix followed by a lowering one. $\sigma\cdot\epsilon^\ast(k') = -\sqrt2\,\sigma_+$ is the outgoing photon with $h' = +1$; $\bar\sigma\cdot\epsilon = \epsilon^0 + \boldsymbol\sigma\cdot\boldsymbol\epsilon = +\sqrt2\,\sigma_-$ is the incoming photon with $h = -1$. The product is $-2$, and for the other three pairs of photon helicities it vanishes. So the string is $m\cdot2E\cdot(-2)$ and
>
> $$
> \mathcal M \simeq -e^2\,\frac{-4mE}{-(\omega^2\chi^2 + m^2)} = -\frac{4e^2\,m\,E}{\omega^2\chi^2 + m^2} .
> $$
>
> Angular momentum at $\chi = 0$: before $h - \frac12$, after $-\frac12 - h'$, equal for $h' = -h$; here $h = -1$, $h' = +1$.
>
> **Step 5** (item 3). Parity reverses every helicity and is a symmetry of QED ([[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ: photon, graviton, neutrino]]); in the computation, item 3 of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]].
>
> **Step 6** (item 4). Four enhanced configurations: the two of items 1 and 2 and their mirror images. The average over the four initial states:
>
> $$
> \frac14\cdot2\cdot\frac{16e^4\omega^2\,(\omega^2\chi^2 + m^2)}{(\omega^2\chi^2 + m^2)^2} = \frac{8e^4\,\omega^2}{\omega^2\chi^2 + m^2} .
> $$
>
> Compare [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]: $2e^4\,\frac{p\cdot k}{p\cdot k'}$ with $p\cdot k \simeq 2\omega^2$ and $p\cdot k' \simeq \frac12(\omega^2\chi^2 + m^2)$ is the same. With $\frac{d\sigma}{d\cos\theta} = \frac{2\pi}{64\pi^2s}\cdot\frac14\sum|\mathcal M|^2$, $e^4 = 16\pi^2\alpha^2$ and $s \simeq 4\omega^2$: $\frac{d\sigma}{d\cos\theta} \simeq \frac{4\pi\alpha^2\omega^2}{s(\omega^2\chi^2 + m^2)} = \frac{4\pi\alpha^2}{s(\chi^2 + 4m^2/s)}$ (PS (5.103)).
>
> **What the derivation shows.**
> - ⚑ By-product: the factor $\chi$ in the numerator is the amplitude for converting one unit of spin into orbital angular momentum; it is what turns $1/\chi^4$ into $1/\chi^2$.
> - ⚑ By-product: at the kinematic endpoint $\chi = 0$ only the helicity-flip process is left, with the photon helicity reversed → [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^ex-c8b-10-1|Example §C8b.10.1]].
> - The unpolarized formula of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]] is recovered from two helicity amplitudes; the trace computation hides which configurations carry the peak.

^der-c8b-10-4

*Uses:* [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-1|Theorem §C8b.10.1]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-7|P9, step 7]], [[P9 Helicity Amplitudes#^p9-6|P9, step 6]]

> [!theorem] ★ Theorem §C8b.10.5: The Helicity Amplitudes of Compton Scattering at High Energy
> ★ *Beyond the lecture: Yu's explicit helicity amplitudes, quoted.* For $m \to 0$ in the centre-of-mass frame, with helicities in the order (incoming electron, incoming photon, outgoing electron, outgoing photon) and $\mathcal M = \mathcal M_s + \mathcal M_u$ the contributions of diagrams (a) and (b):
> 1. all four helicities equal:
>
> $$
> \mathcal M_s(\pm, \pm, \pm, \pm) \simeq -2e^2\cos\frac\theta2 , \qquad \mathcal M_u(\pm, \pm, \pm, \pm) \simeq -\frac{2e^2\sin^2\frac\theta2}{\cos\frac\theta2} , \qquad \mathcal M(\pm, \pm, \pm, \pm) \simeq -\frac{2e^2}{\cos\frac\theta2} ;
> $$
>
> 2. electron and photon helicities opposite, each conserved: $\mathcal M_u(\pm, \mp, \pm, \mp) \simeq -2e^2\cos\frac\theta2$, with no $s$-channel contribution;
> 3. the other twelve amplitudes vanish in this limit;
> 4. the singularity at $\theta = \pi$ comes from the $u$-channel amplitude with all helicities equal. Its spinor string contains a factor $\cos\frac\theta2$, which weakens the $\cos^{-2}\frac\theta2$ of the propagator to $\cos^{-1}\frac\theta2$: the helicity suppression of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], since $\cos\frac\theta2 = \sin\frac\chi2 \simeq \frac\chi2$;
> 5. the squares add up to the unpolarized result: $\frac14\sum|\mathcal M|^2 = \frac14\Bigl[2\cdot\frac{4e^4}{\cos^2\frac\theta2} + 2\cdot4e^4\cos^2\frac\theta2\Bigr] = 2e^4\Bigl[\frac{2}{1 + \cos\theta} + \frac{1 + \cos\theta}{2}\Bigr]$ ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], 2).
>
> *Proof:* Yu §8.6.3, by explicit spinors and polarization vectors; not reproduced. The signs are those of Yu's phase conventions. The magnitudes of items 1–2, the zeros of item 3 and the sum of item 5 were checked numerically.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, $m = 0$ (leading order in $m/\omega$ away from $\theta = \pi$); near $\theta = \pi$ with the mass kept: [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]].
>
> *Source: Yu §8.6.3, eqs. (8.412)–(8.415) (the two channels), (8.441) ($\mathcal M_s$), (8.451) (opposite electron helicities do not contribute), (8.456)–(8.457) ($\mathcal M_u$) and the closing sentence of the page · the user's PHY 513 notes, Lecture 22 update, paragraph "Correspondence with Yu" · item 5 computed here*

^thm-c8b-10-5

## Inverse Compton scattering

> [!example] Example §C8b.10.1: Inverse Compton Scattering
> *Question.* A beam of low-energy photons, an intense laser beam, is shone against a beam of high-energy electrons. What photons come out, and with what polarization?
>
> *Answer.* In the centre-of-mass frame this is Compton scattering at high energy, provided $s \gg m^2$.
> 1. **Energy.** The strongest scattering is backward in the centre-of-mass frame ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]). In the frame of the experiment such photons carry nearly all of the electron's energy:
>
> $$
> \omega'_{\rm lab} \simeq \Bigl(1 - \frac{\chi^2}{4}\Bigr)E_{\rm lab} ,
> $$
>
> where $E_{\rm lab}$ is the energy of the electron in the frame of the experiment and $\chi$ the backward angle in the centre-of-mass frame. Low-energy photons are turned into high-energy photons.
> 2. **Polarization.** Let the laser photons be right-handed and the electrons unpolarized. The enhanced amplitude is the one with all helicities equal ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], 1), so most scattered photons are right-handed.
> 3. **The endpoint.** Exactly backward, $\chi = 0$, that amplitude vanishes. Only the helicity-flip amplitude survives, and it reverses the helicity of the photon ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], 2, with all helicities reversed): the photons of the very highest energy, $\omega'_{\rm lab} = E_{\rm lab}$, are left-handed.
> 4. **The spectrum.** With $y \equiv \omega'_{\rm lab}/E_{\rm lab} \simeq 1 - \chi^2/4$, the cross section of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], 4, becomes
>
> $$
> \frac{d\sigma}{dy} \simeq \frac{2\pi\alpha^2}{s\,\bigl[(1 - y) + m^2/s\bigr]^2}\,\Bigl[(1 - y) + \frac{m^2}{s}\Bigr] ,
> $$
>
> where the first term in the last bracket is the helicity-conserving process and the second the helicity-flip process.
>
> The scattering selects a polarization, by means of enhancements that are large without being infinite. It can be used to measure the polarization of an electron beam, or as a source of high-energy photons with adjustable energy distribution and polarization.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$; head-on beams with $s = 4E_{\rm lab}\,\omega_{\rm lab} \gg m^2$ ($\omega_{\rm lab}$ the energy of the laser photons); items 1 and 4 near the endpoint, $\chi \ll 1$.
>
> *Source: PHY 513 Lecture 22, slide 31 ("High energy electrons scattering off low energy photons (a laser beam) give high energy photons. Strongest scattering is backwards. Such photons acquire nearly all electron energy $\omega' = (1 - \frac14\chi^2)E$. Suppose initial photons are polarized (R only), electrons not ⇒ most scattered photons R. But exactly backscattered ($\chi = 0$) must flip spin so very highest energy γ's ($\omega' = E$) are L"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.3, Principle "Inverse Compton scattering" (the meaning of $E$ and $\chi$ filled in by the user's notes; "Checked numerically") · PS §5.5, p. 167, eq. (5.104) and the display before it ($y \approx \frac12(1 - \cos\theta) \approx 1 - \frac{\chi^2}{4}$; "This effect can be used experimentally to measure the polarization of an electron beam or to create high-energy photon sources with adjustable energy distribution and polarization")*

^ex-c8b-10-1

> [!derivation]- Derivation
> **Step 1** (the boost). In the centre-of-mass frame the scattered photon has energy $\omega$ and moves at the angle $\theta = \pi - \chi$ to $+\hat{\mathbf z}$; the electron comes in along $-\hat{\mathbf z}$ with energy $E$. The frame of the experiment moves along $+\hat{\mathbf z}$ with a velocity $\beta$ close to 1, so that the electron is very energetic there: $E_{\rm lab} = \gamma(E + \beta\omega)$ and $\omega'_{\rm lab} = \gamma\omega\,(1 - \beta\cos\theta) = \gamma\omega\,(1 + \beta\cos\chi)$.
>
> **Step 2** (the ratio). For $\beta \to 1$: $y = \frac{\omega'_{\rm lab}}{E_{\rm lab}} \to \frac{\omega\,(1 + \cos\chi)}{E + \omega}$. For $s \gg m^2$, $E \simeq \omega$: $y \simeq \frac12(1 + \cos\chi) = \frac12(1 - \cos\theta) \simeq 1 - \frac{\chi^2}{4}$.
>
> **Step 3** ($s$ in the frame of the experiment). The beams are head-on: $s = m^2 + 2p\cdot k = m^2 + 2(E_{\rm lab}\omega_{\rm lab} + |\mathbf p_{\rm lab}|\omega_{\rm lab}) \simeq 4E_{\rm lab}\,\omega_{\rm lab}$.
>
> **Step 4** (item 4). $y = \frac12(1 - \cos\theta)$ gives $dy = -\frac12\,d\cos\theta$ and $\chi^2 \simeq 4(1 - y)$. So $\frac{d\sigma}{dy} = 2\,\frac{d\sigma}{d\cos\theta} \simeq \frac{8\pi\alpha^2}{s\,(4(1 - y) + 4m^2/s)} = \frac{2\pi\alpha^2}{s\,((1 - y) + m^2/s)}$, written in the statement with numerator and denominator multiplied by $(1 - y) + m^2/s$ so that the two helicity contributions of [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^der-c8b-10-4|Derivation §C8b.10.4]], Step 6, $\propto \chi^2$ and $\propto 4m^2/s$, are visible.
>
> **What the derivation shows.**
> - The photon energy in the experiment is fixed by the centre-of-mass angle: the endpoint of the spectrum is the backward direction, where the helicity structure changes.

^der-c8b-10-6

*Uses:* [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|Theorem §C8a.17.6]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]

> [!caution] Caution: Which E and which χ on slide 31
> In "$\omega' = (1 - \frac14\chi^2)E$" on slide 31, $E$ is the energy of the electron in the frame of the experiment and $\omega'$ the energy of the scattered photon in that frame, while $\chi$ is the backward angle in the centre-of-mass frame. On the preceding slides $E$ and $\omega$ are centre-of-mass energies, where the photon energy does not change at all, $\omega' = \omega$.
>
> *Source: PHY 513 Lecture 22, slide 31 · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", seventh item · PS §5.5, p. 167*

^cau-c8b-10-3

> [!remark]- Connections
> - The puzzle and the unpolarized formulas that this section explains — [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]]; the amplitude and its two diagrams — [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]].
> - The same angular-momentum argument fixed the zeros of the polarized cross sections of $e^+e^- \to \mu^+\mu^-$ — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]; there both initial particles were fermions and the allowed $J_z$ was $\pm1$, here a photon and an electron give $J_z = \pm\frac12, \pm\frac32$.
> - Helicity conservation at the QED vertex, exact for projections and a statement about helicities at $m = 0$ — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|§C8b.6, Remark: Frame and mass]]; the suppressed amplitudes of $e^+e^- \to \mu^+\mu^-$ with masses — [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]].
> - The photon factors $\sigma^1 \pm i\sigma^2$ are the helicity vectors contracted with $\sigma^\mu$; in Lecture 20 the same circular vector appeared as the current of an $e^-_Re^+_L$ pair — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]], [[§C8b.9 Photon Helicity#^ex-c8b-9-1|Example §C8b.9.1]].
> - A nearly on-shell exchanged photon gives the full $1/\theta^4$ in $e^-\mu^-$ scattering: no selection rule protects the forward direction there — [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]].
> - The recipe for helicity amplitudes — [[P9 Helicity Amplitudes|P9]].
> - The general rule behind the two terms of the propagator numerator, an odd number of $\gamma$'s joining equal chiralities and an even number opposite ones, and helicity suppression as the name of the effect — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]], [[§C8b.6 Helicity Conservation at the QED Vertex#^ex-c8b-6-1|Example §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-5|§C8b.6, Remark: Helicity suppression]].
