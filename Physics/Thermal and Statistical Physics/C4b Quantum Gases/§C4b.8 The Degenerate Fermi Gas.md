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

**Setup.** Uniform three-dimensional gas, $\epsilon = \hbar^2k^2/(2m)$, $g(\epsilon) = A\epsilon^{1/2}$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]]), fixed $N$ and $V$, Fermi occupation $f(\epsilon) = 1/(e^{(\epsilon - \mu)/k_BT} + 1)$.

> [!caution] Caution: Fixed $\mu$ or fixed $N$
> At fixed $\mu$, all finite-temperature Fermi curves cross at $f(\mu) = \tfrac12$ and sharpen over a width $\sim k_BT$ as $T$ drops. At fixed $N$, $\mu$ itself moves with $T$ to keep $N = \int g f\,d\epsilon$, and the curves no longer share a crossing point. Which is held fixed must be stated.

^cau-c4b-8-1

> [!definition] Definition §C4b.8.1: Fermi Energy, Wave Number and Temperature
> $E_F \equiv \mu(T = 0)$. At $T = 0$, $f(\epsilon) \to \Theta(E_F - \epsilon)$: orbitals fill one particle per state up to $E_F$. The occupied ball $|\mathbf k| < k_F$ is the **Fermi sea**, its surface the **Fermi surface**, and
>
> $$
> E_F = \frac{\hbar^2k_F^2}{2m}, \qquad T_F = \frac{E_F}{k_B} .
> $$
>
> *Source: Mao §4.6.6, eqs. (4.156), (4.158) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^def-b13-1-1|Def. §B13.1.1]]*

^def-c4b-8-1

> [!theorem] Theorem §C4b.8.1: The Fermi Gas at Zero Temperature
> $$
> k_F = \Bigl(\frac{6\pi^2\rho_3}{g_s}\Bigr)^{1/3}, \qquad T_F = \frac{(36\pi)^{1/3}}{4}T_Q \simeq 1.21\,T_Q ,
> $$
>
> $$
> U(0) = \tfrac35NE_F, \qquad p(0)V = \tfrac25NE_F, \qquad C_V(0) = 0 .
> $$
>
> For spin-$\tfrac12$ electrons ($g_s = 2$), $k_F = (3\pi^2\rho_3)^{1/3}$. The **degeneracy pressure** comes from exclusion and the kinetic cost of filling momentum states, with no repulsion and no thermal motion; since $E_F \propto (N/V)^{2/3}$, compression raises the energy even at $T = 0$.
>
> *Model:* the Setup; *applies:* $T = 0$; $C_V(0) = 0$ from [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]].
>
> *Source: Mao §4.6.6, eqs. (4.157)–(4.161) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-2|Theorem §B13.1.2]]*

^thm-c4b-8-1

> [!derivation]- Derivation
> **Step 1** ($k_F$). $N = \int_0^{E_F}g\,d\epsilon$, which in $k$-space is the number of orbitals in the ball: $g_sV\cdot\frac43\pi k_F^3/(2\pi)^3 = g_sVk_F^3/(6\pi^2)$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]).
>
> **Step 2** ($T_F$ vs $T_Q$). $k_BT_F = \frac{\hbar^2}{2m}(6\pi^2\rho_3/g_s)^{2/3}$ and $k_BT_Q = \frac{2\pi\hbar^2}{m}(\rho_3/g_s)^{2/3}$ ([[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]]), ratio $\frac{(6\pi^2)^{2/3}}{4\pi} = \frac{(36\pi^4)^{1/3}}{4\pi} = \frac{(36\pi)^{1/3}}{4} \simeq 1.209$.
>
> **Step 3** ($U$). With $g \propto \epsilon^{1/2}$, $U(0)/N = \int_0^{E_F}\epsilon^{3/2}d\epsilon\big/\int_0^{E_F}\epsilon^{1/2}d\epsilon = \frac{(2/5)E_F^{5/2}}{(2/3)E_F^{3/2}} = \frac35E_F$.
>
> **Step 4** ($p$). $p(0) = -(\partial U(0)/\partial V)_N$ with $U(0) \propto NE_F \propto V^{-2/3}$ gives $p = \frac{2U(0)}{3V}$, the $T = 0$ case of $U = \tfrac32pV$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]).

^der-c4b-8-1

*Uses:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]], [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]

> [!theorem] Theorem §C4b.8.2: Only a Thin Shell Is Thermally Active
> For $T \ll T_F$, only orbitals within $\sim k_BT$ of $E_F$ change their occupation. About $g(E_F)k_BT \sim NT/T_F$ particles are excited, each by $\sim k_BT$, so
>
> $$
> U(T) - U(0) \sim N\frac{(k_BT)^2}{E_F}, \qquad C_V \sim Nk_B\frac{T}{T_F} ,
> $$
>
> far below the classical $\tfrac32Nk_B$. The exact coefficient is in [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]].
>
> *Model:* the Setup; *applies:* $T \ll T_F$; an estimate.
>
> *Source: Mao §4.6.7, eq. (4.162) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-4|Theorem §B13.1.4]]*

^thm-c4b-8-2

> [!derivation]- Derivation
> An orbital far below $E_F$ has no empty orbital within $k_BT$ to move to, so it stays full. In a shell of width $k_BT$ there are $g(E_F)k_BT$ orbitals, and $g(E_F) = \frac32N/E_F$ for $g \propto \epsilon^{1/2}$ (from $N = \tfrac23AE_F^{3/2}$). Each excitation costs $\sim k_BT$; multiply, then differentiate in $T$.

^der-c4b-8-2

*Uses:* [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]]

> [!example] Example §C4b.8.1: A Metal's Electrons Are Degenerate at Room Temperature
> For $\rho_3 = 10^{29}\ \text{m}^{-3}$ and $g_s = 2$: $k_F = (3\pi^2\times10^{29})^{1/3} \simeq 1.44\times10^{10}\ \text{m}^{-1}$, $E_F = \hbar^2k_F^2/(2m_e) \simeq 7.9$ eV, $T_F \simeq 9.1\times10^4$ K. At $300$ K, $T/T_F \simeq 0.003$: strongly degenerate. A metal's measured heat capacity also includes the lattice.
>
> *Source: Mao §4.6.7*

^ex-c4b-8-1

> [!example] Example §C4b.8.2: The Same Scale, Two Outcomes
> For uniform ideal gases in three dimensions with quadratic dispersion:
>
> | | bosons | fermions |
> | --- | --- | --- |
> | classical regime | $T \gg T_Q$ | $T \gg T_Q$ |
> | characteristic scale | $T_c \simeq 0.527\,T_Q$ | $T_F \simeq 1.21\,T_Q$ |
> | mechanism | excited states saturate; ground occupation macroscopic | exclusion fills orbitals up to $E_F$ |
> | low-$T$ chemical potential | $\mu \to 0^-$ ($0$ when condensed) | $\mu \to E_F$ |
> | $T = 0$ energy and pressure | zero | $U/N = \tfrac35E_F$, $p = \tfrac25\rho_3E_F$ |
> | low-$T$ heat capacity | $C_V \propto T^{3/2}$ | $C_V \propto T$ |
> | finite-$T$ transition | yes, at $T_c$ | no, a smooth crossover |
>
> Both scales are $k_BT_{\text{deg}} \sim \frac{\hbar^2}m(\rho_3/g_s)^{2/3}$, the point $\rho_3\lambda_T^3/g_s \sim 1$ where exchange matters. Photons, with no fixed $N$, condense neither way. Interactions, traps and other dispersions can change every row.
>
> *Source: Mao §4.6.9, eq. (4.168) and comparison table*

^ex-c4b-8-2

> [!remark]- Connections
> - The exact low-temperature coefficients come from the large-$\ln z$ limit of the polylogarithm — [[§C4b.9★ Low-Temperature Fermi Thermodynamics|§C4b.9]].
> - Degeneracy pressure holds up white dwarfs and neutron stars — [[§B13.3★ White Dwarfs and Neutron Stars#^thm-b13-3-2|Theorem §B13.3.2]].
