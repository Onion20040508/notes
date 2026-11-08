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

*Sources: Mao, PHY 510 notes, §4.5.7, eqs. (4.139)–(4.142), boxes "Why is the chemical potential of black-body photons zero (optional content)?", "The ultraviolet catastrophe and the birth of quantum theory" and Figure 4.5 · M. Planck (1900) and A. Einstein (1905), as cited by Mao §4.5.7 through his refs. [25] (Planck, Nobel lecture, 1920) and [26] (R. J. Glauber, "One Hundred Years of Light Quanta", Nobel lecture, 2005) · PHY 510 Lecture 10/8.*

A cavity in equilibrium with its walls fills with thermal radiation. Its modes are electromagnetic waves, each a quantum oscillator, so black-body radiation is the Bose gas of [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] with a linear dispersion, two polarizations, and one new input: photon number is not conserved, so $\mu = 0$. Everything else, the Stefan–Boltzmann law, the radiation pressure, the photon number, Planck's spectrum, follows from the general formulas. Level B has the full treatment as a ★ section ([[§B11.1★ Blackbody Radiation from Statistical Mechanics#^mod-b11-1-1|Model §B11.1.1]], [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-4|Theorem §B11.1.4]]); in PHY 510 it is core material.

**Setup.** Bose statistics, $\epsilon = \hbar ck$, $g_s = 2$, so $g(\epsilon) = \frac{V}{\pi^2\hbar^3c^3}\epsilon^2$ ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]) and $\nu = 3$. The vacuum energy of the modes is a temperature-independent constant and is subtracted.

> [!theorem] Theorem §C4b.6.1: Black-Body Photons Have $\mu = 0$
> For radiation in equilibrium with walls that emit and absorb photons, $\mu_\gamma = 0$ and $z = 1$ at every temperature, and each mode has the Bose occupation $\langle n_\ell\rangle = 1/(e^{\beta\hbar\omega_\ell} - 1)$.
>
> *Model:* black-body radiation; *applies:* photon number relaxes on the equilibration time. If it does not (photons thermalized by number-conserving scattering, as in dye-filled optical microcavities, or the early-universe radiation once photon-creating processes freeze out), a nonzero $\mu_\gamma$ is needed.
>
> *Source: Mao §4.5.7, eq. (4.139) and box "Why is the chemical potential of black-body photons zero (optional content)?" · level-B home: [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-2|Theorem §B11.1.2]]*

^thm-c4b-6-1

> [!derivation]- Derivation
> Three routes, each under its own hypothesis.
>
> **Route 1** (MaxEnt; only $\langle\hat H\rangle = U$ is constrained). [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] gives $\hat\rho \propto e^{-\beta\hat H}$ with no multiplier for $\hat N_\gamma$; comparing with $e^{-\beta(\hat H - \mu\hat N_\gamma)}$, $\mu = 0$.
>
> **Route 2** ($N_\gamma$ an unconstrained internal variable at fixed $T$, $V$). Equilibrium minimizes $F(T, V, N_\gamma)$ over $N_\gamma$ ([[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-5|Theorem §C1.6.5]]), so $(\partial F/\partial N_\gamma)_{T,V} = 0$, and this derivative is $\mu_\gamma$ ([[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]]).
>
> **Route 3** (each mode a canonical oscillator). The levels $n\hbar\omega_\ell$, $n \ge 0$, give $Z_\ell = \sum_ne^{-\beta n\hbar\omega_\ell} = 1/(1 - e^{-\beta\hbar\omega_\ell})$ and $\langle n_\ell\rangle = 1/(e^{\beta\hbar\omega_\ell} - 1)$, as in [[§C4b.2 One Orbital in the Grand Ensemble#^der-c4b-2-1|Derivation §C4b.2.1]], Step 2: the Bose occupation with $\mu = 0$. No particle reservoir enters.

^der-c4b-6-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-5|Theorem §C1.6.5]], [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]], [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]

> [!remark] Remark: What removes the photon number
> For one mode $\hat N = \hat a^\dagger\hat a$ obeys $[\hat N, \hat a^\dagger] = \hat a^\dagger$, $[\hat N, \hat a] = -\hat a$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|QFT ]]). The free Hamiltonian $\sum\hbar\omega_{\mathbf k\lambda}\hat a^\dagger_{\mathbf k\lambda}\hat a_{\mathbf k\lambda}$ commutes with $\hat N_\gamma$, but $\hat{\mathbf E}$ is linear in the $\hat a$ and $\hat a^\dagger$, so a wall coupling $-\hat{\mathbf d}\cdot\hat{\mathbf E}$ has $[\hat N_\gamma, \hat{\mathbf d}\cdot\hat{\mathbf E}] \ne 0$ and changes $N_\gamma$ by $\pm1$. Nothing else conserves it: the $U(1)$ of electromagnetism protects electric charge, and photons carry none. So the interaction with the walls, not the free field, is what puts Route 1 of [[§C4b.6 The Photon Gas and Black-Body Radiation#^der-c4b-6-1|Derivation §C4b.6.1]] in force.

^rem-c4b-6-1

> [!theorem] Theorem §C4b.6.2: Thermodynamics of Black-Body Radiation
> $$
> \ln\Xi = \frac{\pi^2V}{45}\Bigl(\frac{k_BT}{\hbar c}\Bigr)^3, \qquad U = aVT^4, \qquad pV = \tfrac13aVT^4 = \tfrac13U, \qquad C_V = 4aVT^3, \qquad S = \tfrac43aVT^3, \qquad a = \frac{\pi^2k_B^4}{15\hbar^3c^3} ,
> $$
>
> $$
> \frac{N_\gamma}{V} = \frac{2\zeta(3)}{\pi^2}\Bigl(\frac{k_BT}{\hbar c}\Bigr)^3 \simeq 2.03\times10^{7}\ \text{m}^{-3}\,(T/\text{K})^3 .
> $$
>
> For example $N_\gamma/V \simeq 4.1\times10^8\ \text{m}^{-3} \simeq 410\ \text{cm}^{-3}$ at $2.725$ K; and the mean occupation of a typical mode, $\hbar\omega = k_BT$, is $1/(e - 1) \simeq 0.58$ at every $T$, never $\ll 1$.
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
> **Step 3** ($S$). With $\mu = 0$, $\Phi = U - TS = -pV$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]), so $S = (U + pV)/T = \tfrac43aVT^3$.
>
> **Step 4** ($N_\gamma$). $N_\gamma = A\Gamma(3)(k_BT)^3G_3(1) = \frac{2V(k_BT)^3\zeta(3)}{\pi^2(\hbar c)^3}$, taking the $z$-derivative before setting $z = 1$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], parts 2 and 4). Numerically $2\zeta(3)/\pi^2 = 0.2436$ and $k_B/\hbar c = 436.7\ \text{m}^{-1}\text{K}^{-1}$.

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
> The densities per frequency $\nu$ and per wavelength $\lambda$ are $u_\nu = 2\pi u_\omega$ and $u_\lambda = (2\pi c/\lambda^2)u_\omega$ at $\omega = 2\pi c/\lambda$ ([[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-4|Theorem §B11.1.4]]).
>
> *Model:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]]; *applies:* equilibrium radiation.
>
> *Source: Mao §4.5.7, eq. (4.142) · level-B home: [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-4|Theorem §B11.1.4]] · QM home of the Rayleigh–Jeans limit: [[§A1.1 Blackbody Radiation#^thm-a1-1-3|QM Theorem §A1.1.3]]*

^thm-c4b-6-3

> [!derivation]- Derivation
> **Step 1.** $\langle E\rangle = \hbar\omega\langle n\rangle$ with [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]]; the limits are [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-2|Theorem §C4b.2.2]], part 2, and $e^{x} - 1 \simeq e^x$ for $x \gg 1$.
>
> **Step 2.** $U = \sum_\ell\hbar\omega_\ell\langle n_\ell\rangle$, equal to $-\partial_\beta\ln\Xi$ at $z = 1$. Replace the sum with $\int D(\omega)\,d\omega$ ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]): $D(\omega) = g(\epsilon)\,d\epsilon/d\omega = \hbar g(\hbar\omega)$.
>
> **Step 3.** $u_\omega = D(\omega)\langle E_\omega\rangle/V$; its integral is $U/V$ of [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]]. For the other variables, $u_\nu\,d\nu = u_\omega\,d\omega$ with $d\omega = 2\pi\,d\nu$, and $u_\lambda\,|d\lambda| = u_\omega\,d\omega$ with $|d\omega/d\lambda| = 2\pi c/\lambda^2$.

^der-c4b-6-3

*Uses:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]], [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-2|Theorem §C4b.2.2]], [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

![[ph-th-c4b-6-1.svg]]

*Figure: Planck's spectrum against the classical Rayleigh–Jeans form, in the scaled variable $x = \hbar\omega/k_BT$ (spectral density in units of $(k_BT)^3/(\pi^2\hbar^2c^3)$). They agree at small $x$; quantization cuts off the high-frequency tail that the classical form lets grow without bound ([[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-4|Theorem §C4b.6.4]]).*

> [!theorem] Theorem §C4b.6.4: The Ultraviolet Catastrophe
> Classical equipartition gives every mode $k_BT$ ([[§B8.2 Equipartition and the Heat Capacities of Molecules#^thm-b8-2-1|Theorem §B8.2.1]]), so with modes up to a cutoff $\omega_c$
>
> $$
> u^{\text{cl}}_\omega = \frac{k_BT\omega^2}{\pi^2c^3}, \qquad \frac{U_{\text{cl}}}{V} = \frac{k_BT}{\pi^2c^3}\int_0^{\omega_c}\omega^2\,d\omega = \frac{k_BT\,\omega_c^3}{3\pi^2c^3} \xrightarrow{\ \omega_c\to\infty\ } \infty ,
> $$
>
> whereas the same $D(\omega)$ with $\langle E_\omega\rangle$ of [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]] gives the finite $aT^4$.
>
> *Model:* classical electromagnetic modes in a cavity; *applies:* contrasted with [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]].
>
> *Source: Mao §4.5.7, box "The ultraviolet catastrophe and the birth of quantum theory" · QM home: [[§A1.1 Blackbody Radiation#^thm-a1-1-3|QM Theorem §A1.1.3]]*

^thm-c4b-6-4

> [!derivation]- Derivation
> A classical mode is an oscillator with two quadratic terms, mean energy $k_BT$ for every $\omega$. Multiply by $D(\omega)/V = \omega^2/(\pi^2c^3)$ and integrate to $\omega_c$.

^der-c4b-6-4

*Uses:* [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]]

> [!remark] Remark: The historical step
> The quantized $\langle E_\omega\rangle$ entered physics through Planck's wall oscillators (1900) and Einstein's light quanta (1905), told at the QM level ([[§A1.1 Blackbody Radiation#^pr-a1-1-4|QM Principle §A1.1.4]], [[§A1.2 The Photoelectric Effect#^pr-a1-2-3|QM Principle §A1.2.3]]); the mode-by-mode field derivation used here came later.

^rem-c4b-6-2

> [!remark]- Connections
> - Radiation pressure $p = U/3V$ and Stefan's law follow from thermodynamics alone once $p = u/3$ is known — [[§B11.1★ Blackbody Radiation from Statistical Mechanics#^thm-b11-1-3|Theorem §B11.1.3]].
> - Phonons in a solid are the same calculation with a cutoff and three branches — [[§B11.2★ Phonons and the Debye Model#^mod-b11-2-2|Model §B11.2.2]].
