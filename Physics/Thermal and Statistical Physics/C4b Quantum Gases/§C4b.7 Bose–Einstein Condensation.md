---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.7
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.6 The Photon Gas and Black-Body Radiation]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.8 The Degenerate Fermi Gas]] →

*Sources: Mao, PHY 510 notes, §4.6.1–§4.6.5, eqs. (4.143)–(4.153), boxes "Why the continuum integral misses the condensate", "What determines whether excited states can saturate?" and Figures 4.6–4.7 · PHY 510 Lecture 10/8.*

Cool a gas of bosons at fixed density. To keep the particle number, $\mu$ must rise toward the lowest orbital energy. In three dimensions the excited orbitals can then hold only a finite number of particles, and below a definite temperature the rest pile into the ground orbital: Bose–Einstein condensation. The degeneracy scale where this happens is the same one that will make a Fermi gas degenerate ([[§C4b.8 The Degenerate Fermi Gas|§C4b.8]]). Level B treats condensation as a ★ section ([[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-4|Theorem §B12.1.4]]); in PHY 510 it is core material.

**Setup.** Uniform three-dimensional gas, $\epsilon_k = \hbar^2k^2/(2m)$, ground energy $0$, fixed $N$ and $V$; $G_q = \operatorname{Li}_q$; $\lambda_T$ and $a_s$ of [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]], [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]].

> [!definition] Definition §C4b.7.1: Degeneracy Temperature
> $T_Q$ is the temperature at which the thermal wavelength equals the spacing, $\lambda_T(T_Q) = a_s$:
>
> $$
> T_Q = \frac{2\pi\hbar^2}{mk_Ba_s^2} = \frac{2\pi\hbar^2}{mk_B}\Bigl(\frac{\rho_3}{g_s}\Bigr)^{2/3}, \qquad \frac{\lambda_T}{a_s} = \sqrt{\frac{T_Q}{T}}, \qquad \frac{\rho_3\lambda_T^3}{g_s} = \Bigl(\frac{T_Q}{T}\Bigr)^{3/2} .
> $$
>
> For $T \gg T_Q$ both statistics are Maxwell–Boltzmann; for $T \lesssim T_Q$ quantum statistics decides. $T_Q$ marks a crossover, not a transition.
>
> *Source: Mao §4.6.1, eq. (4.143)*

^def-c4b-7-1

> [!theorem] Theorem §C4b.7.1: Excited Orbitals Have a Finite Capacity
> The excited-state number
>
> $$
> N_{\text{ex}}(T, \mu) = \int_0^\infty\frac{g(\epsilon)\,d\epsilon}{e^{\beta(\epsilon - \mu)} - 1} = \frac{g_sV}{\lambda_T^3}G_{3/2}(z)
> $$
>
> increases with $\mu$ and is largest as $\mu \to 0^-$:
>
> $$
> N_{\text{ex}}^{\max}(T) = \frac{g_sV}{\lambda_T^3}\zeta(\tfrac32) ,
> $$
>
> finite, although each orbital can hold any number of bosons.
>
> *Model:* the Setup; *applies:* three dimensions; more generally whenever $g(\epsilon) \propto \epsilon^{\alpha-1}$ with $\alpha > 1$ near $\epsilon = 0$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-4|Theorem §C4b.7.4]]).
>
> *Source: Mao §4.6.2, eqs. (4.144)–(4.145)*

^thm-c4b-7-1

> [!derivation]- Derivation
> **Step 1.** Each $f(\epsilon)$ increases with $\mu$, so $N_{\text{ex}}$ does, and $\mu < 0$ is required ([[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]).
>
> **Step 2.** At $\mu \to 0^-$, $G_{3/2}(z) \to \zeta(\tfrac32)$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 3). The integrand $g(\epsilon)/(e^{\beta\epsilon} - 1) \simeq A\epsilon^{1/2}/(\beta\epsilon) \propto \epsilon^{-1/2}$ near $0$ is integrable, and the tail is exponentially small.

^der-c4b-7-1

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]], [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!theorem] Theorem §C4b.7.2: The Ground State Must Be Kept Separately
> The exact number equation is the sum $N = \sum_\ell f(\epsilon_\ell)$; the integral of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]] counts the excited orbitals only. With the ground orbital restored,
>
> $$
> N = N_0 + N_{\text{ex}}, \qquad N_0 = \frac{g_s}{e^{-\beta\mu} - 1} = \frac{g_sz}{1 - z}, \qquad \mu = -k_BT\ln\Bigl(1 + \frac{g_s}{N_0}\Bigr) \simeq -\frac{g_sk_BT}{N_0} .
> $$
>
> A macroscopic $N_0$ pins $\mu$ to $0$ in the thermodynamic limit, while $\mu < 0$ in every finite system; that small negative value is what fixes $N_0$.
>
> *Model:* the Setup, with $g_s$ degenerate internal ground states; *applies:* large $N$.
>
> *Source: Mao §4.6.2, eqs. (4.146)–(4.147), box "Why the continuum integral misses the condensate"*

^thm-c4b-7-2

> [!derivation]- Derivation
> **Step 1.** The ground orbital, $\epsilon = 0$, $g_s$ internal states, has total occupation $g_s/(e^{-\beta\mu} - 1)$ ([[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]]). In the integral it has weight zero ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]), which is harmless unless its occupation is of order $V$.
>
> **Step 2.** Solve $N_0(e^{-\beta\mu} - 1) = g_s$ for $\mu$, and expand $\ln(1 + g_s/N_0) \simeq g_s/N_0$ for $N_0 \gg g_s$.

^der-c4b-7-2

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]

> [!theorem] Theorem §C4b.7.3: Transition Temperature and Condensate Fraction
> Condensation sets in when the excited capacity equals $N$:
>
> $$
> \frac{\rho_3\lambda_{T_c}^3}{g_s} = \zeta(\tfrac32), \qquad T_c = \frac{2\pi\hbar^2}{mk_B}\Bigl(\frac{\rho_3}{g_s\zeta(3/2)}\Bigr)^{2/3} = \frac{T_Q}{\zeta(3/2)^{2/3}} \simeq 0.527\,T_Q .
> $$
>
> In the thermodynamic limit,
>
> $$
> \frac{N_0}{N} = \begin{cases}0, & T > T_c,\\ 1 - (T/T_c)^{3/2}, & T < T_c,\end{cases} \qquad \mu\ \begin{cases}< 0, & T > T_c,\\ = 0, & T < T_c.\end{cases}
> $$
>
> The condensate appears continuously at $T_c$ and $N_0/N \to 1$ as $T \to 0$.
>
> *Model:* the Setup; *applies:* thermodynamic limit at fixed density; a finite system rounds the transition.
>
> *Source: Mao §4.6.3, eqs. (4.148)–(4.152) and Figure 4.6 · level-B homes: [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-4|Theorem §B12.1.4]]*

^thm-c4b-7-3

> [!derivation]- Derivation
> **Step 1** ($T_c$). Set $N = N_{\text{ex}}^{\max}(T_c)$ of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]] and solve with $\lambda_T = \sqrt{2\pi\hbar^2/(mk_BT)}$. Comparing with [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]], $(T_Q/T_c)^{3/2} = \zeta(\tfrac32)$, and $2.612^{-2/3} \simeq 0.527$.
>
> **Step 2** (capacity at any $T$). $\lambda_T^{-3} \propto T^{3/2}$, so $N_{\text{ex}}^{\max}(T) = N(T/T_c)^{3/2}$.
>
> **Step 3** (above $T_c$). The capacity exceeds $N$, so $N_{\text{ex}}(T, \mu) = N$ has a solution with $\mu < 0$, and $N_0 = g_sz/(1 - z)$ stays of order one: $N_0/N \to 0$.
>
> **Step 4** (below $T_c$). The capacity is less than $N$; the excited states saturate ($\mu \to 0$) with $N_{\text{ex}} = N(T/T_c)^{3/2}$, and [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]] gives $N_0 = N - N_{\text{ex}}$.

^der-c4b-7-3

*Uses:* [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]], [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]]

![[ph-th-c4b-7-1.svg]]

*Figure: the uniform ideal Bose gas at fixed density. Left: $\mu/k_BT_c$, computed from $\operatorname{Li}_{3/2}(z) = \zeta(\tfrac32)(T_c/T)^{3/2}$ above $T_c$, reaches $0$ at $T_c$ and stays there. Right: the condensate fraction $1 - (T/T_c)^{3/2}$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]]).*

> [!theorem] Theorem §C4b.7.4: When Can Excited States Saturate?
> If $g(\epsilon) \propto \epsilon^{\alpha-1}$ near $\epsilon = 0$, the excited capacity at $\mu \to 0^-$ is finite exactly when $\alpha > 1$. A uniform gas with quadratic dispersion in $d$ dimensions has $\alpha = d/2$, so this mechanism gives condensation at $T > 0$ only for $d > 2$. A trap changes $g(\epsilon)$ and can change the answer.
>
> *Model:* ideal Bose gas; *applies:* thermodynamic limit; apply to the actual spectrum.
>
> *Source: Mao §4.6.3, box "What determines whether excited states can saturate?"*

^thm-c4b-7-4

> [!derivation]- Derivation
> Near $0$, $g(\epsilon)/(e^{\beta\epsilon} - 1) \simeq \epsilon^{\alpha-1}/(\beta\epsilon) \propto \epsilon^{\alpha-2}$, integrable at $0$ iff $\alpha - 2 > -1$. For $d$ dimensions and $\epsilon \propto k^2$, $g \propto k^{d-1}dk/d\epsilon \propto \epsilon^{d/2-1}$, so $\alpha = d/2$ ([[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]]).

^der-c4b-7-4

> [!theorem] Theorem §C4b.7.5: Energy and Heat Capacity below $T_c$
> The condensate has zero energy and carries no pressure; energy and pressure come from the excited particles. Below $T_c$,
>
> $$
> U \propto T^{5/2}, \qquad C_V \propto T^{3/2}, \qquad pV = \tfrac23U ,
> $$
>
> both $U$ and $C_V$ vanishing as $T \to 0$. $U$ is smooth through $T_c$ while $C_V$ has a finite cusp there; for $T \gg T_c$ the classical values $\tfrac32Nk_BT$, $\tfrac32Nk_B$ return. At fixed $T$, $V$, particles added to a condensed gas join the condensate and leave the pressure unchanged.
>
> *Model:* the Setup; *applies:* ideal gas.
>
> *Source: Mao §4.6.4, eq. (4.153) and Figure 4.7 · PHY 510 Problem Set 6, part (f), official solution · level-B home: [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-5|Theorem §B12.1.5]]*

^thm-c4b-7-5

> [!derivation]- Derivation
> Below $T_c$, $z = 1$ in [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] for the excited states: $U = \tfrac32A\Gamma(\tfrac32)(k_BT)^{5/2}\zeta(\tfrac52) \propto T^{5/2}$, so $C_V \propto T^{3/2}$; $pV = U/\nu$ with $\nu = \tfrac32$. None of this involves $N$, which is why adding particles at fixed $T$, $V$ changes nothing but $N_0$.

^der-c4b-7-5

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]

> [!remark] Remark: What a condensate is
> A condensate is not a clump in one place. In the uniform gas it is a macroscopic number of bosons in the $\mathbf k = 0$ orbital, which fills the whole box: the density stays uniform, the momentum distribution gets a sharp peak at $\mathbf k = 0$, and the occupied orbital gives long-range coherence visible in interference. At $T > 0$ it coexists with a thermal cloud. Superfluidity is a further property, of the response to flow, and needs interactions.

^rem-c4b-7-1

> [!law] Law §C4b.7.6: Bose–Einstein Condensation in Helium and in Atomic Gases
> 1. Liquid $^4$He becomes superfluid at its lambda transition near $2.17$ K at saturated vapour pressure (discovered 1938; London linked it to Bose condensation). It is a strongly interacting liquid, and the ideal-gas fraction and cusp do not describe it quantitatively.
> 2. Magnetically trapped $^{87}$Rb condensed near $170$ nK in 1995: a narrow low-momentum component grew inside the broad thermal cloud. The low temperature fits $T_Q \propto \rho_3^{2/3}/m$ for a dilute, heavy gas; the trap changes $g(\epsilon)$, so uniform-box formulas should not be fitted directly.
>
> *Valid when:* as stated; weak interactions for part 2.
>
> *Source: Mao §4.6.5 · level-B homes: [[§B12.1★ Bose–Einstein Condensation#^law-b12-1-6|Law §B12.1.6]], [[§B12.1★ Bose–Einstein Condensation#^law-b12-1-7|Law §B12.1.7]]*

^law-c4b-7-6

> [!remark]- Connections
> - The same scale $T_Q$ sets the Fermi temperature, $T_F \simeq 1.21\,T_Q$ — [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]].
> - Black-body photons do not condense because their number is not conserved — [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]].
> - Condensation in any dimension for any power-law dispersion — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]].
