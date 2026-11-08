---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.5
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.4 The Grand Partition Function and Polylogarithms]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.6 The Photon Gas and Black-Body Radiation]] →

*Sources: Mao, PHY 510 notes, §4.5.6, eqs. (4.131)–(4.138), box "Thermal wavelength versus particle spacing" and Figure 4.4 · PHY 510 Lecture 10/8 · PHY 510 Problem Set 6, part (d), official solution.*

When is a gas of atoms classical? Not simply when it is hot: the question is whether the thermal de Broglie wavelength is small compared with the spacing between particles in the same internal state. This section derives that criterion from the number equation, recovers the classical ideal gas, and computes the first correction from exchange alone. Level B has the same quantities ([[§B8.1 The Partition Function of the Ideal Gas#^def-b8-1-1|Def. §B8.1.1]], [[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-1|Def. §B10.2.1]], [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-4|Theorem §B10.2.4]]).

**Setup.** Nonrelativistic particles in three dimensions, $g(\epsilon) = A\epsilon^{1/2}$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]), with the master formulas of [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] at $\nu = \tfrac32$; number density $\rho_3 = N/V$.

> [!definition] Definition §C4b.5.1: Thermal Wavelength
> $$
> \lambda_T = \frac{h}{\sqrt{2\pi mk_BT}} = \sqrt{\frac{2\pi\hbar^2}{mk_BT}} ,
> $$
>
> the matter wavelength of a typical thermal momentum $\sqrt{mk_BT}$: a thermal coherence length, not a particle size. With it the number equation reads
>
> $$
> N = \frac{g_sV}{\lambda_T^3}G_{3/2}(z) .
> $$
>
> *Source: Mao §4.5.6, eqs. (4.131)–(4.132) · level-B home: [[§B8.1 The Partition Function of the Ideal Gas#^def-b8-1-1|Def. §B8.1.1]]*

^def-c4b-5-1

> [!derivation]- Derivation
> [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] with $\nu = \tfrac32$: $N = A\Gamma(\tfrac32)(k_BT)^{3/2}G_{3/2}(z)$, and $A = \frac{g_sV}{4\pi^2}(2m/\hbar^2)^{3/2}$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]), $\Gamma(\tfrac32) = \sqrt\pi/2$. Then $A\Gamma(\tfrac32)(k_BT)^{3/2} = \frac{g_sV\sqrt\pi}{8\pi^2}\bigl(\frac{2mk_BT}{\hbar^2}\bigr)^{3/2} = g_sV\bigl(\frac{mk_BT}{2\pi\hbar^2}\bigr)^{3/2} = g_sV/\lambda_T^3$, using $\frac{\sqrt\pi}{8\pi^2}2^{3/2} = (2\pi)^{-3/2}$.

^der-c4b-5-1

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]

> [!theorem] Theorem §C4b.5.1: The Classical Limit Is $\lambda_T \ll a_s$
> Let $a_s = (g_s/\rho_3)^{1/3}$ be the spacing between particles of one internal state. Then
>
> $$
> \lambda_T \ll a_s \iff z \ll 1 \implies \beta(\epsilon - \mu) \gg 1\ \text{for every}\ \epsilon \ge 0 ,
> $$
>
> and in this limit
>
> $$
> z \simeq \frac{\rho_3\lambda_T^3}{g_s} = \Bigl(\frac{\lambda_T}{a_s}\Bigr)^3, \qquad \mu \simeq k_BT\ln\frac{\rho_3\lambda_T^3}{g_s}, \qquad f(\epsilon) \simeq ze^{-\beta\epsilon} .
> $$
>
> Temperature alone does not decide: compression lowers $a_s$ and pushes a gas toward degeneracy at the same $T$.
>
> *Model:* [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]]; *applies:* nonrelativistic ideal gas; exchange concerns particles in the same internal state, which is why $g_s$ enters.
>
> *Source: Mao §4.5.6, eqs. (4.133)–(4.136) and box "Thermal wavelength versus particle spacing" · level-B home: [[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-1|Def. §B10.2.1]]*

^thm-c4b-5-1

> [!derivation]- Derivation
> **Step 1.** $G_{3/2}(z)$ increases with $z$ and is $\simeq z$ for small $z$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 2). So [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]] gives $\rho_3\lambda_T^3/g_s = G_{3/2}(z)$, small exactly when $z$ is small, and then $z \simeq \rho_3\lambda_T^3/g_s$.
>
> **Step 2.** $\beta(\epsilon - \mu) = \beta\epsilon - \ln z \ge -\ln z \gg 1$.
>
> **Step 3.** Then $ze^{-\beta\epsilon} \ll 1$ in $f = ze^{-\beta\epsilon}/(1 \mp ze^{-\beta\epsilon})$, so the $\mp$ is negligible. This is the step that drops quantum statistics; the continuum approximation of [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]] did not.

^der-c4b-5-2

*Uses:* [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!example] Example §C4b.5.1: Classical and Degenerate Gases
> Air at room conditions has $\lambda_T \ll a_s$: nondegenerate. Dilute atomic gases become degenerate only after cooling to ultralow temperatures. Conduction electrons in a metal are degenerate already at room temperature, because their mass is small and their density high. Lighter particles become degenerate at higher $T$ for the same density, since $\lambda_T \propto (mT)^{-1/2}$.
>
> *Source: Mao §4.5.6, box "Thermal wavelength versus particle spacing" · level B: [[§B8.1 The Partition Function of the Ideal Gas#^ex-b8-1-1|Example §B8.1.1]]*

^ex-c4b-5-1

> [!theorem] Theorem §C4b.5.2: Classical Ideal-Gas Thermodynamics
> For $z \ll 1$, $\ln\Xi \simeq N$ and
>
> $$
> U = \tfrac32Nk_BT, \qquad pV = Nk_BT, \qquad C_V = \tfrac32Nk_B .
> $$
>
> *Model:* [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]]; *applies:* $\lambda_T \ll a_s$.
>
> *Source: Mao §4.5.6, eq. (4.137) · level-B home: [[§B8.1 The Partition Function of the Ideal Gas#^thm-b8-1-4|Theorem §B8.1.4]]*

^thm-c4b-5-2

> [!derivation]- Derivation
> With $G_{3/2} \simeq G_{5/2} \simeq z$, [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] gives $\ln\Xi = A\Gamma(\tfrac32)\beta^{-3/2}z = N$, $U = \tfrac32k_BT\ln\Xi$ and $pV = k_BT\ln\Xi$. Substitute $\ln\Xi = N$ and differentiate $U$ at fixed $V$, $N$.

^der-c4b-5-3

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]]

> [!theorem] Theorem §C4b.5.3: The First Exchange Correction
> To next order in $\rho_3\lambda_T^3/g_s$,
>
> $$
> \frac{p}{\rho_3k_BT} = 1 \mp \frac{\rho_3\lambda_T^3/g_s}{2^{5/2}} + O\bigl[(\rho_3\lambda_T^3/g_s)^2\bigr] ,
> $$
>
> upper sign bosons. At the same $\rho_3$ and $T$, Bose statistics lowers the pressure and Fermi statistics raises it, with no interaction at all.
>
> *Model:* ideal quantum gas near the classical limit; *applies:* $\rho_3\lambda_T^3/g_s \ll 1$.
>
> *Source: Mao §4.5.6, eq. (4.138) · level-B home: [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-4|Theorem §B10.2.4]]*

^thm-c4b-5-3

> [!derivation]- Derivation
> **Step 1.** Write $\delta = \rho_3\lambda_T^3/g_s$. From [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] and [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 2:
>
> $$
> \delta = z \pm \frac{z^2}{2^{3/2}} + \cdots, \qquad \frac{p\lambda_T^3}{g_sk_BT} = z \pm \frac{z^2}{2^{5/2}} + \cdots .
> $$
>
> **Step 2.** Invert the first to second order: $z = \delta \mp \delta^2/2^{3/2} + \cdots$.
>
> **Step 3.** Substitute: $\frac{p\lambda_T^3}{g_sk_BT} = \delta \mp \frac{\delta^2}{2^{3/2}} \pm \frac{\delta^2}{2^{5/2}} + \cdots = \delta \mp \frac{\delta^2}{2^{5/2}}$, since $\frac1{2^{3/2}} - \frac1{2^{5/2}} = \frac1{2^{5/2}}$. Divide by $\delta = \rho_3\lambda_T^3/g_s$.

^der-c4b-5-4

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!remark]- Connections
> - The degeneracy scale where $\lambda_T = a_s$ sets both the Bose condensation temperature and the Fermi temperature — [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]].
> - The classical chemical potential $\mu = k_BT\ln(\rho\lambda_T^3/g_s)$ — [[§B8.1 The Partition Function of the Ideal Gas#^thm-b8-1-6|Theorem §B8.1.6]].
