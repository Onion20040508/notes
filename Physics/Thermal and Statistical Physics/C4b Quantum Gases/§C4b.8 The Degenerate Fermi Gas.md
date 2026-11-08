---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.8
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.7 Bose–Einstein Condensation]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.9★ Low-Temperature Fermi Thermodynamics]] →

*Sources: Mao, PHY 510 notes, §4.6.6–§4.6.7 and §4.6.9, eqs. (4.154)–(4.162), (4.168), Figure 4.8 and the closing comparison table · PHY 510 Lecture 10/8.*

Fermions respond to the same degeneracy scale in the opposite way. Exclusion forces them to fill orbitals one per state up to a Fermi energy, which leaves a gas with large energy and pressure at zero temperature. On heating only a thin shell near the top of the filled sea can change, which is why the electronic heat capacity of a metal is small. Level B covers the degenerate Fermi gas as a ★ section ([[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-2|Theorem §B13.1.2]], [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-4|Theorem §B13.1.4]]).

**Setup.** Uniform three-dimensional gas, $\epsilon = \hbar^2k^2/(2m)$, $g(\epsilon) = A\epsilon^{1/2}$ ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]), fixed $N$ and $V$, Fermi occupation $f(\epsilon) = 1/(e^{(\epsilon - \mu)/k_BT} + 1)$.

> [!caution] Caution: Fixed $\mu$ or fixed $N$
> $f(\mu) = \tfrac12$ at every $T$, so curves of $f$ at one fixed $\mu$ all cross at $\epsilon = \mu$. For a gas of given $N$ the crossing point is $\mu(T) = E_F[1 - \tfrac{\pi^2}{12}(T/T_F)^2 + \cdots]$ ([[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]]), which moves down as $T$ rises; a plot or formula of $f$ against $T$ has to say which of $\mu$, $N$ is held.

^cau-c4b-8-1

> [!definition] Definition §C4b.8.1: Fermi Energy, Wave Number and Temperature
> For a Fermi gas of given $N$, $V$:
>
> $$
> E_F \equiv \mu(T = 0), \qquad k_F \equiv \frac{\sqrt{2mE_F}}{\hbar}\quad\Bigl(\text{so } E_F = \frac{\hbar^2k_F^2}{2m}\Bigr), \qquad T_F \equiv \frac{E_F}{k_B} .
> $$
>
> *Source: Mao §4.6.6, eqs. (4.156), (4.158) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^def-b13-1-1|Def. §B13.1.1]]*

^def-c4b-8-1

> [!definition] Definition §C4b.8.2: Fermi Sea and Fermi Surface
> As $T \to 0$, $f(\epsilon) \to \Theta(E_F - \epsilon)$ for $\epsilon \ne E_F$: the occupied orbitals are those with $|\mathbf k| < k_F$ ([[§C4b.8 The Degenerate Fermi Gas#^def-c4b-8-1|Def. §C4b.8.1]]). This ball in $\mathbf k$-space is the **Fermi sea**; its boundary sphere $|\mathbf k| = k_F$ is the **Fermi surface**.
>
> *Source: Mao §4.6.6 · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^def-b13-1-1|Def. §B13.1.1]]*

^def-c4b-8-2

> [!theorem] Theorem §C4b.8.1: The Fermi Gas at Zero Temperature
> $$
> k_F = \Bigl(\frac{6\pi^2\rho_3}{g_s}\Bigr)^{1/3}, \qquad T_F = \frac{(36\pi)^{1/3}}{4}T_Q \simeq 1.21\,T_Q ,
> $$
>
> $$
> U(0) = \tfrac35NE_F, \qquad p(0)V = \tfrac25NE_F, \qquad B(0) = -V\Bigl(\frac{\partial p}{\partial V}\Bigr)_N = \tfrac53p(0) .
> $$
>
> For spin-$\tfrac12$ electrons ($g_s = 2$), $k_F = (3\pi^2\rho_3)^{1/3}$. Here $p(0) = -(\partial U(0)/\partial V)_N$ is the degeneracy pressure: $U(0) \propto N^{5/3}V^{-2/3}$ by exclusion alone, with no interaction and $T = 0$.
>
> *Model:* the Setup; *applies:* $T = 0$.
>
> *Source: Mao §4.6.6, eqs. (4.157)–(4.161) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-2|Theorem §B13.1.2]]*

^thm-c4b-8-1

> [!derivation]- Derivation
> **Step 1** ($k_F$). $N = \int_0^{E_F}g\,d\epsilon$, which in $k$-space is the number of orbitals in the Fermi sea ([[§C4b.8 The Degenerate Fermi Gas#^def-c4b-8-2|Def. §C4b.8.2]]): $g_sV\cdot\frac43\pi k_F^3/(2\pi)^3 = g_sVk_F^3/(6\pi^2)$ ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]).
>
> **Step 2** ($T_F$ vs $T_Q$). $k_BT_F = \frac{\hbar^2}{2m}(6\pi^2\rho_3/g_s)^{2/3}$ and $k_BT_Q = \frac{2\pi\hbar^2}{m}(\rho_3/g_s)^{2/3}$ ([[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]]), ratio $\frac{(6\pi^2)^{2/3}}{4\pi} = \frac{(36\pi^4)^{1/3}}{4\pi} = \frac{(36\pi)^{1/3}}{4} \simeq 1.209$.
>
> **Step 3** ($U$). With $g \propto \epsilon^{1/2}$, $U(0)/N = \int_0^{E_F}\epsilon^{3/2}d\epsilon\big/\int_0^{E_F}\epsilon^{1/2}d\epsilon = \frac{(2/5)E_F^{5/2}}{(2/3)E_F^{3/2}} = \frac35E_F$.
>
> **Step 4** ($p$). $p(0) = -(\partial U(0)/\partial V)_N$ with $U(0) \propto NE_F \propto N^{5/3}V^{-2/3}$ gives $p = \frac{2U(0)}{3V}$, the $T = 0$ case of $U = \tfrac32pV$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]).
>
> **Step 5** ($B$). $p(0) \propto V^{-5/3}$ at fixed $N$, so $-V\,\partial_Vp = \tfrac53p$.

^der-c4b-8-1

*Uses:* [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]], [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.8 The Degenerate Fermi Gas#^def-c4b-8-2|Def. §C4b.8.2]]

> [!theorem] Theorem §C4b.8.2: Only a Thin Shell Is Thermally Active
> For $T \ll T_F$, $f$ differs from $\Theta(E_F - \epsilon)$ appreciably only for $|\epsilon - E_F| \lesssim k_BT$. That window holds $g(E_F)k_BT \sim NT/T_F$ particles, each excited by $\sim k_BT$, so
>
> $$
> U(T) - U(0) \sim N\frac{(k_BT)^2}{E_F}, \qquad C_V \sim Nk_B\frac{T}{T_F} \xrightarrow{\ T\to0\ } 0 ,
> $$
>
> linearly in $T$, and $C_V \ll \tfrac32Nk_B$ throughout $T \ll T_F$. The coefficient is fixed in [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]].
>
> *Model:* the Setup; *applies:* $T \ll T_F$; an order-of-magnitude estimate.
>
> *Source: Mao §4.6.7, eq. (4.162) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-4|Theorem §B13.1.4]]*

^thm-c4b-8-2

> [!derivation]- Derivation
> At energy $E_F - \Delta$ with $\Delta \gg k_BT$ the occupation is $1 - e^{-\Delta/k_BT}$: thermal excitation needs an empty orbital within $\sim k_BT$, and there is none so deep in the sea. In the window $|\epsilon - E_F| \lesssim k_BT$ there are $g(E_F)k_BT$ orbitals, and $g(E_F) = \frac32N/E_F$ for $g \propto \epsilon^{1/2}$ (from $N = \tfrac23AE_F^{3/2}$). Each excitation costs $\sim k_BT$; multiply to get $U - U(0)$, then differentiate in $T$: $C_V \sim 2Nk_B^2T/E_F \propto T$.

^der-c4b-8-2

*Uses:* [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]]

> [!example] Example §C4b.8.1: A Metal's Electrons Are Degenerate at Room Temperature
> For $\rho_3 = 10^{29}\ \text{m}^{-3}$ and $g_s = 2$: $k_F = (3\pi^2\times10^{29})^{1/3} \simeq 1.44\times10^{10}\ \text{m}^{-1}$, $E_F = \hbar^2k_F^2/(2m_e) \simeq 7.9$ eV, $T_F \simeq 9.1\times10^4$ K. At $300$ K, $T/T_F \simeq 0.003$: strongly degenerate, and the electronic $C_V/Nk_B = \tfrac{\pi^2}2T/T_F \simeq 0.016$ ([[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]]), against $3$ per atom from the lattice. Per mole of electrons the linear coefficient is $\gamma = \pi^2R/(2T_F) \simeq 0.45\ \text{mJ mol}^{-1}\text{K}^{-2}$, the size of the measured linear term $\gamma T$ of metals, visible only below a few kelvin ([[§B11.2★ Phonons and the Debye Model#^law-b11-2-3|Law §B11.2.3]]).
>
> *Source: Mao §4.6.7; $C_V$ and $\gamma$ computed here · QM home of the free-electron model: [[§A6.2 Crystalline Solids and the Free-Electron Model#^mod-a6-2-2|QM Model §A6.2.2]]*

^ex-c4b-8-1

> [!remark] Remark: The same scale, two outcomes
> Uniform ideal gases in three dimensions, $\epsilon = \hbar^2k^2/2m$; each entry links the box that proves it.
>
> | | bosons | fermions |
> | --- | --- | --- |
> | crossover scale ($\rho_3\lambda_T^3/g_s = 1$) | $T_Q$, [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]] | $T_Q$, [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]] |
> | low-$T$ scale | $T_c = 0.527\,T_Q$, [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] | $T_F = 1.21\,T_Q$, [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]] |
> | $\mu$ as $T \to 0$ | $0^-$, with $\mu \simeq -g_sk_BT/N_0$, [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]] | $E_F[1 - \tfrac{\pi^2}{12}(T/T_F)^2]$, [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]] |
> | $T = 0$ energy, pressure | $0$, $0$, [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-5|Theorem §C4b.7.5]] | $\tfrac35NE_F$, $\tfrac25\rho_3E_F$, [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]] |
> | low-$T$ $C_V/Nk_B$ | $1.926\,(T/T_c)^{3/2}$, [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-5|Theorem §C4b.7.5]] | $\tfrac{\pi^2}2\,T/T_F$, [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]] |
> | sharp transition at $T > 0$ | at $T_c$ ($N_0/N$ nonanalytic), [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] | none: a smooth crossover |
>
> Photons are not in the table: with $\mu = 0$ and no fixed $N$ ([[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]]) there is neither a $T_c$ nor an $E_F$. Every row assumes the Setup; traps change the bosonic column ([[§C4b.7 Bose–Einstein Condensation#^ex-c4b-7-1|Example §C4b.7.1]]).

^rem-c4b-8-1

> [!remark]- Connections
> - The exact low-temperature coefficients come from the large-$\ln z$ limit of the polylogarithm — [[§C4b.9★ Low-Temperature Fermi Thermodynamics|§C4b.9]].
> - Degeneracy pressure holds up white dwarfs and neutron stars — [[§B13.3★ White Dwarfs and Neutron Stars#^thm-b13-3-2|Theorem §B13.3.2]].
