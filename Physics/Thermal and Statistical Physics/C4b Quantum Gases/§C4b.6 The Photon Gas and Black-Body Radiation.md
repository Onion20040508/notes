---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.6
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.5 Massive Gases and the Classical Limit]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.7 Bose–Einstein Condensation]] →

*Sources: Mao, PHY 510 notes, §4.5.7, eqs. (4.139)–(4.142), boxes "Why is the chemical potential of black-body photons zero (optional content)?", "The ultraviolet catastrophe and the birth of quantum theory" and Figure 4.5 · PHY 510 Lecture 10/8.*

A cavity in equilibrium with its walls fills with thermal radiation. Its modes are electromagnetic waves, each a quantum oscillator, so black-body radiation is the Bose gas of [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] with a linear dispersion, two polarizations, and one new input: photon number is not conserved, so $\mu = 0$. Everything else, the Stefan–Boltzmann law, the radiation pressure, the photon number, Planck's spectrum, follows from the general formulas. Level B has the full treatment as a ★ section ([[§B11.1★ Blackbody Radiation from Statistical Mechanics#^mod-b11-1-1|Model §B11.1.1]], [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-4|Theorem §B11.1.4]]); in PHY 510 it is core material.

**Setup.** Bose statistics, $\epsilon = \hbar ck$, $g_s = 2$, so $g(\epsilon) = \frac{V}{\pi^2\hbar^3c^3}\epsilon^2$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]) and $\nu = 3$. The vacuum energy of the modes is a temperature-independent constant and is subtracted.

> [!theorem] Theorem §C4b.6.1: Black-Body Photons Have $\mu = 0$
> For radiation in equilibrium with walls that emit and absorb, $\mu = 0$ and $z = 1$ at every temperature. Four ways to see it:
>
> 1. **MaxEnt.** Only the mean energy is constrained, not the photon number, so $\hat\rho \propto e^{-\beta\hat H}$ with no $\hat N_\gamma$ multiplier ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]); comparing with $e^{-\beta(\hat H - \mu\hat N_\gamma)}$ gives $\mu = 0$.
> 2. **Free-energy minimum.** If $N_\gamma$ can relax at fixed $T$, $V$, equilibrium minimizes $F(T, V, N_\gamma)$ over it: $(\partial F/\partial N_\gamma)_{T,V} = \mu_\gamma = 0$.
> 3. **One oscillator.** A mode is a harmonic oscillator whose excitation number varies even canonically: $Z_\ell^{\text{osc}} = 1/(1 - e^{-\beta\hbar\omega_\ell})$ and $\langle n_\ell\rangle = 1/(e^{\beta\hbar\omega_\ell} - 1)$, the Bose occupation at $\mu = 0$.
> 4. **No conservation law.** Photon number has no symmetry protecting it: the fields are real, the $U(1)$ gauge symmetry conserves electric charge, which photons do not carry, and couplings such as $-\hat{\mathbf d}\cdot\hat{\mathbf E}$ create and destroy photons. The free-field Hamiltonian does commute with $\hat N_\gamma$, so it is the number-changing interactions that matter.
>
> *Model:* black-body radiation; *applies:* if photon number is conserved over the equilibration time, a nonzero effective $\mu$ can be appropriate instead.
>
> *Source: Mao §4.5.7, eq. (4.139) and box "Why is the chemical potential of black-body photons zero (optional content)?" · level-B home: [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-2|Theorem §B11.1.2]]*

^thm-c4b-6-1

> [!derivation]- Derivation
> **Part 1.** [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] with the single constraint $\langle\hat H\rangle = U$.
>
> **Part 2.** At fixed $T$, $V$ the equilibrium value of an unconstrained internal variable minimizes $F$ ([[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-5|Theorem §C1.6.5]]), and $\partial F/\partial N$ is the chemical potential ([[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]]).
>
> **Part 3.** $\sum_{n\ge0}e^{-\beta n\hbar\omega}$ is geometric; the mean follows as in [[§C4b.2 One Orbital in the Grand Ensemble#^der-c4b-2-1|Derivation §C4b.2.1]], Step 2, with $\mu = 0$.
>
> **Part 4** is an argument about symmetries, recorded as Mao gives it.

^der-c4b-6-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-5|Theorem §C1.6.5]], [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]

> [!theorem] Theorem §C4b.6.2: Thermodynamics of Black-Body Radiation
> $$
> \ln\Xi = \frac{\pi^2V}{45}\Bigl(\frac{k_BT}{\hbar c}\Bigr)^3, \qquad U = aVT^4, \qquad pV = \tfrac13aVT^4 = \tfrac13U, \qquad C_V = 4aVT^3, \qquad a = \frac{\pi^2k_B^4}{15\hbar^3c^3} ,
> $$
>
> $$
> \frac{N_\gamma}{V} = \frac{2\zeta(3)}{\pi^2}\Bigl(\frac{k_BT}{\hbar c}\Bigr)^3 .
> $$
>
> The photon number falls on cooling: with no conserved excess there is nothing to condense, and since $z = 1$ always, heating never makes the photon gas dilute.
>
> *Model:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]] with the Setup's $g(\epsilon)$; *applies:* large cavity.
>
> *Source: Mao §4.5.7, eqs. (4.140)–(4.141) · level-B homes: [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-3|Theorem §B11.1.3]], [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-5|Theorem §B11.1.5]]*

^thm-c4b-6-2

> [!derivation]- Derivation
> **Step 1.** $A = V/(\pi^2\hbar^3c^3)$, $\nu = 3$, $\Gamma(3) = 2$, $z = 1$: [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-1|Theorem §C4b.4.1]] gives $\ln\Xi = 2A(k_BT)^3\zeta(4) = \frac{2V(k_BT)^3}{\pi^2\hbar^3c^3}\cdot\frac{\pi^4}{90} = \frac{\pi^2V}{45}\bigl(\frac{k_BT}{\hbar c}\bigr)^3$.
>
> **Step 2.** [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] with $\nu = 3$: $U = 3k_BT\ln\Xi = \frac{\pi^2V(k_BT)^4}{15(\hbar c)^3} = aVT^4$, and $pV = k_BT\ln\Xi = U/3$. Then $C_V = \partial_TU = 4aVT^3$; here $N_\gamma$ adjusts freely.
>
> **Step 3.** $N_\gamma = A\Gamma(3)(k_BT)^3G_3(1) = \frac{2V(k_BT)^3\zeta(3)}{\pi^2(\hbar c)^3}$, taking the $z$-derivative before setting $z = 1$.

^der-c4b-6-2

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-1|Theorem §C4b.4.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!theorem] Theorem §C4b.6.3: Planck's Spectrum and Its Two Limits
> One mode of frequency $\omega$ has mean thermal energy
>
> $$
> \langle E_\omega\rangle = \frac{\hbar\omega}{e^{\beta\hbar\omega} - 1} \simeq \begin{cases}k_BT, & \hbar\omega \ll k_BT\quad\text{(Rayleigh–Jeans)},\\ \hbar\omega\,e^{-\hbar\omega/k_BT}, & \hbar\omega \gg k_BT\quad\text{(Wien tail)}.\end{cases}
> $$
>
> With $D(\omega) = \hbar g(\hbar\omega) = V\omega^2/(\pi^2c^3)$ modes per unit angular frequency, the energy per volume per $d\omega$ is
>
> $$
> u_\omega(T) = \frac{\hbar\omega^3}{\pi^2c^3}\frac{1}{e^{\hbar\omega/k_BT} - 1}, \qquad \frac UV = \int_0^\infty u_\omega\,d\omega = aT^4 .
> $$
>
> Spectra per ordinary frequency or per wavelength need the corresponding Jacobian.
>
> *Model:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]]; *applies:* equilibrium radiation.
>
> *Source: Mao §4.5.7, eq. (4.142) · level-B home: [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-4|Theorem §B11.1.4]]*

^thm-c4b-6-3

> [!derivation]- Derivation
> **Step 1.** $\langle E\rangle = \hbar\omega\langle n\rangle$ with [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]], part 3; the limits are [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-2|Theorem §C4b.2.2]], part 2, and $e^{x} - 1 \simeq e^x$ for $x \gg 1$.
>
> **Step 2.** $U = \sum_\ell\hbar\omega_\ell\langle n_\ell\rangle$, equal to $-\partial_\beta\ln\Xi$ at $z = 1$. Replace the sum with $\int D(\omega)\,d\omega$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]): $D(\omega) = g(\epsilon)\,d\epsilon/d\omega = \hbar g(\hbar\omega)$.
>
> **Step 3.** $u_\omega = D(\omega)\langle E_\omega\rangle/V$; its integral is $U/V$ of [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]].

^der-c4b-6-3

*Uses:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]], [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-2|Theorem §C4b.2.2]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

![[ph-th-c4b-6-1.svg]]

*Figure: Planck's spectrum against the classical Rayleigh–Jeans form, in the scaled variable $x = \hbar\omega/k_BT$ (spectral density in units of $(k_BT)^3/(\pi^2\hbar^2c^3)$). They agree at small $x$; quantization cuts off the high-frequency tail that the classical form lets grow without bound ([[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-4|Theorem §C4b.6.4]]).*

> [!theorem] Theorem §C4b.6.4: The Ultraviolet Catastrophe
> Classical equipartition gives every mode $k_BT$ ([[§B8.2 Equipartition and the Heat Capacities of Molecules#^thm-b8-2-1|Theorem §B8.2.1]]), so
>
> $$
> u^{\text{cl}}_\omega = \frac{k_BT\omega^2}{\pi^2c^3}, \qquad \frac{U_{\text{cl}}}{V} = \frac{k_BT}{\pi^2c^3}\int_0^\infty\omega^2\,d\omega = \infty .
> $$
>
> The mode count is right; the classical thermal energy per mode is wrong at high frequency. With quanta $\hbar\omega$ ([[§C4b.1 Orbitals and Occupations#^pr-c4b-1-2|Principle §C4b.1.2]]), a mode with $\hbar\omega \gg k_BT$ is rarely excited even once, its mean energy is exponentially small, and $U$ is finite.
>
> *Model:* classical electromagnetic modes in a cavity; *applies:* contrasted with [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]].
>
> *Source: Mao §4.5.7, box "The ultraviolet catastrophe and the birth of quantum theory"*

^thm-c4b-6-4

> [!derivation]- Derivation
> A classical mode is an oscillator with two quadratic terms, mean energy $k_BT$ for every $\omega$. Multiply by $D(\omega)/V = \omega^2/(\pi^2c^3)$ and integrate: the integrand grows as $\omega^2$.

^der-c4b-6-4

*Uses:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]]

> [!remark] Remark: The historical step
> Planck reproduced the measured spectrum in 1900 by counting the energies of material resonators in elements proportional to frequency. Einstein's light-quantum hypothesis of 1905 gave light itself quanta of energy $h\nu = \hbar\omega$. The derivation here, from a quantized field, is the later unified account and is not Planck's original resonator argument.

^rem-c4b-6-1

> [!remark]- Connections
> - Radiation pressure $p = U/3V$ and Stefan's law follow from thermodynamics alone once $p = u/3$ is known — [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-3|Theorem §B11.1.3]].
> - Phonons in a solid are the same calculation with a cutoff and three branches — [[§B11.2★ Phonons and the Debye Model#^mod-b11-2-2|Model §B11.2.2]].
