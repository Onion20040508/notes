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

*Sources: Mao, PHY 510 notes, §4.6.1–§4.6.5, eqs. (4.143)–(4.153), boxes "Why the continuum integral misses the condensate", "What determines whether excited states can saturate?" and Figures 4.6–4.7 · M. H. Anderson, J. R. Ensher, M. R. Matthews, C. E. Wieman and E. A. Cornell, "Observation of Bose–Einstein Condensation in a Dilute Atomic Vapor", Science 269, 198 (1995), as cited by Mao §4.6.5 [27] · PHY 510 Lecture 10/8.*

For bosons at fixed density, every occupation falls as $T$ drops unless $\mu$ moves up toward the bottom of the spectrum, $\epsilon = 0$. In three dimensions the excited orbitals can then hold only a finite number of particles, and below a definite temperature the rest pile into the ground orbital: Bose–Einstein condensation. The degeneracy scale where this happens is the same one that will make a Fermi gas degenerate ([[§C4b.8 The Degenerate Fermi Gas|§C4b.8]]). Level B treats condensation as a ★ section ([[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-4|Theorem §B12.1.4]]); in PHY 510 it is core material.

**Setup.** Uniform three-dimensional gas, $\epsilon_k = \hbar^2k^2/(2m)$, ground energy $0$, fixed $N$ and $V$; $G_q = \operatorname{Li}_q$; $\lambda_T$ and $a_s$ of [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]], [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]].

> [!definition] Definition §C4b.7.1: Degeneracy Temperature
> $T_Q$ is the temperature at which the thermal wavelength equals the spacing, $\lambda_T(T_Q) = a_s$:
>
> $$
> T_Q = \frac{2\pi\hbar^2}{mk_Ba_s^2} = \frac{2\pi\hbar^2}{mk_B}\Bigl(\frac{\rho_3}{g_s}\Bigr)^{2/3}, \qquad \frac{\lambda_T}{a_s} = \sqrt{\frac{T_Q}{T}}, \qquad \frac{\rho_3\lambda_T^3}{g_s} = \Bigl(\frac{T_Q}{T}\Bigr)^{3/2} .
> $$
>
> $T \gg T_Q$ is the classical regime $z \ll 1$ of [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]]. $T_Q$ itself is only a scale: the Bose transition lies at $0.527\,T_Q$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]]) and the Fermi gas has none ([[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]]).
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
> N_{\text{ex}}^{\max}(T) = \frac{g_sV}{\lambda_T^3}\zeta(\tfrac32) < \infty ,
> $$
>
> whereas the occupation of any single orbital, $f(\epsilon_\ell)$, is unbounded as $\mu \to \epsilon_\ell^-$.
>
> *Model:* the Setup; *applies:* three dimensions; more generally whenever $g(\epsilon) \propto \epsilon^{\alpha-1}$ with $\alpha > 1$ near $\epsilon = 0$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-4|Theorem §C4b.7.4]]).
>
> *Source: Mao §4.6.2, eqs. (4.144)–(4.145)*

^thm-c4b-7-1

> [!derivation]- Derivation
> **Step 1.** Each $f(\epsilon)$ increases with $\mu$, so $N_{\text{ex}}$ does, and $\mu < 0$ is required ([[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]).
>
> **Step 2.** At $\mu \to 0^-$, $G_{3/2}(z) \to \zeta(\tfrac32)$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 4). The integrand $g(\epsilon)/(e^{\beta\epsilon} - 1) \simeq A\epsilon^{1/2}/(\beta\epsilon) \propto \epsilon^{-1/2}$ near $0$ is integrable, and the tail is exponentially small.

^der-c4b-7-1

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]], [[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!theorem] Theorem §C4b.7.2: The Ground State Must Be Kept Separately
> The exact number equation is the sum $N = \sum_\ell f(\epsilon_\ell)$; the integral of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]] counts the excited orbitals only. With the ground orbital restored,
>
> $$
> N = N_0 + N_{\text{ex}}, \qquad N_0 = \frac{g_s}{e^{-\beta\mu} - 1} = \frac{g_sz}{1 - z}, \qquad \mu = -k_BT\ln\Bigl(1 + \frac{g_s}{N_0}\Bigr) \simeq -\frac{g_sk_BT}{N_0} .
> $$
>
> If $N_0 = O(N)$, then $\mu = O(k_BT/N) = O(1/V) \to 0^-$; $N_0$ is fixed by this small negative $\mu$, not by $\mu = 0$, where the formula is singular.
>
> *Model:* the Setup, with $g_s$ degenerate internal ground states; *applies:* large $N$. For $g_s > 1$ only the total $N_0$ of the ground manifold is fixed; how it is shared among the $g_s$ states needs physics beyond the ideal gas.
>
> *Source: Mao §4.6.2, eqs. (4.146)–(4.147), box "Why the continuum integral misses the condensate"*

^thm-c4b-7-2

> [!derivation]- Derivation
> **Step 1.** The ground orbital, $\epsilon = 0$, $g_s$ internal states, has total occupation $g_s/(e^{-\beta\mu} - 1)$ ([[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]]). In the integral it has weight zero ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]); dropping it costs nothing when $N_0/V \to 0$ and everything when $N_0 = O(V)$.
>
> **Step 2.** Solve $N_0(e^{-\beta\mu} - 1) = g_s$ for $\mu$, and expand $\ln(1 + g_s/N_0) \simeq g_s/N_0$ for $N_0 \gg g_s$.

^der-c4b-7-2

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]], [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]

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
> *Model:* the Setup; *applies:* thermodynamic limit at fixed density.
>
> *Source: Mao §4.6.3, eqs. (4.148)–(4.152) and Figure 4.6 · level-B homes: [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-4|Theorem §B12.1.4]]*

^thm-c4b-7-3

> [!derivation]- Derivation
> **Step 1** ($T_c$). Set $N = N_{\text{ex}}^{\max}(T_c)$ of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]] and solve with $\lambda_T = \sqrt{2\pi\hbar^2/(mk_BT)}$. Comparing with [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]], $(T_Q/T_c)^{3/2} = \zeta(\tfrac32)$, and $2.612^{-2/3} \simeq 0.527$.
>
> **Step 2** (capacity at any $T$). $\lambda_T^{-3} \propto T^{3/2}$, so $N_{\text{ex}}^{\max}(T) = N(T/T_c)^{3/2}$.
>
> **Step 3** (above $T_c$). The capacity exceeds $N$, so $G_{3/2}(z) = \zeta(\tfrac32)(T_c/T)^{3/2} < \zeta(\tfrac32)$ has a root $z < 1$ that depends on $T/T_c$ only, not on $V$. Then $N_0 = g_sz/(1 - z)$ stays bounded as $V \to \infty$, and $N_0/N \to 0$.
>
> **Step 4** (below $T_c$). The capacity is less than $N$; the excited states saturate ($\mu \to 0$) with $N_{\text{ex}} = N(T/T_c)^{3/2}$, and [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]] gives $N_0 = N - N_{\text{ex}}$.

^der-c4b-7-3

*Uses:* [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]], [[§C4b.7 Bose–Einstein Condensation#^def-c4b-7-1|Def. §C4b.7.1]]

![[ph-th-c4b-7-1.svg]]

*Figure: the uniform ideal Bose gas at fixed density. Left: $\mu/k_BT_c$, computed from $\operatorname{Li}_{3/2}(z) = \zeta(\tfrac32)(T_c/T)^{3/2}$ above $T_c$, reaches $0$ at $T_c$ and stays there. Right: the condensate fraction $1 - (T/T_c)^{3/2}$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]]).*

> [!theorem] Theorem §C4b.7.4: When Can Excited States Saturate?
> If $g(\epsilon) \propto \epsilon^{\alpha-1}$ near $\epsilon = 0$, the excited capacity at $\mu \to 0^-$ is finite exactly when $\alpha > 1$. For a uniform gas with $\epsilon \propto k^2$ in $d$ dimensions $\alpha = d/2$: condensation at $T > 0$ for $d = 3, 4$, none for $d = 1, 2$.
>
> *Model:* ideal Bose gas; *applies:* thermodynamic limit; $\alpha$ is that of the actual one-particle spectrum, which a trap changes ([[§C4b.7 Bose–Einstein Condensation#^ex-c4b-7-1|Example §C4b.7.1]]).
>
> *Source: Mao §4.6.3, box "What determines whether excited states can saturate?"*

^thm-c4b-7-4

> [!derivation]- Derivation
> Near $0$, $g(\epsilon)/(e^{\beta\epsilon} - 1) \simeq \epsilon^{\alpha-1}/(\beta\epsilon) \propto \epsilon^{\alpha-2}$, integrable at $0$ iff $\alpha - 2 > -1$; at $\alpha = 1$ the integral diverges logarithmically, for $\alpha < 1$ as a power. For $d$ dimensions and $\epsilon \propto k^2$, $g \propto k^{d-1}dk/d\epsilon \propto \epsilon^{d/2-1}$, so $\alpha = d/2$ ([[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]]).

^der-c4b-7-4

> [!example] ★ Example §C4b.7.1: A Harmonic Trap Condenses in Two and Three Dimensions
> In $V(\mathbf r) = \tfrac12m(\omega_x^2x^2 + \omega_y^2y^2 + \omega_z^2z^2)$ the orbitals are $\epsilon = \hbar(\omega_xn_x + \omega_yn_y + \omega_zn_z)$, $n_i \ge 0$ (zero-point energy dropped).
>
> 1. **Count.** For $\epsilon \gg \hbar\omega_i$ the orbitals below $\epsilon$ fill the simplex $\sum_i\hbar\omega_in_i \le \epsilon$, of volume $\epsilon^3/(6\hbar^3\omega_x\omega_y\omega_z)$, so $g(\epsilon) = \dfrac{\epsilon^2}{2(\hbar\bar\omega)^3}$ with $\bar\omega^3 = \omega_x\omega_y\omega_z$: $\alpha = 3$. In two dimensions the same count gives $g = \epsilon/(\hbar\bar\omega)^2$, $\alpha = 2$.
> 2. **$T_c$.** By [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-4|Theorem §C4b.7.4]] both condense. In 3D, $N = \int_0^\infty\frac{g\,d\epsilon}{e^{\beta_c\epsilon} - 1} = \frac{(k_BT_c)^3}{2(\hbar\bar\omega)^3}\Gamma(3)\zeta(3)$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]] part 4), so
>
> $$
> k_BT_c = \hbar\bar\omega\Bigl(\frac{N}{\zeta(3)}\Bigr)^{1/3}, \qquad \frac{N_0}{N} = 1 - \Bigl(\frac{T}{T_c}\Bigr)^3 .
> $$
>
> 3. **Contrast.** The uniform 2D gas ($\alpha = 1$) does not condense, the 2D trap ($\alpha = 2$) does: the confinement, not the dimension, sets $\alpha$.
>
> *Source: added (standard trapped-gas count; Mao §4.6.3 notes that confinement changes the density of states)*

^ex-c4b-7-1

> [!theorem] Theorem §C4b.7.5: Energy and Heat Capacity below $T_c$
> Below $T_c$ the $N_0$ particles at $\epsilon = 0$ contribute nothing to $U$ or $p$, and
>
> $$
> U = \frac32\frac{\zeta(5/2)}{\zeta(3/2)}Nk_BT\Bigl(\frac{T}{T_c}\Bigr)^{3/2} \simeq 0.770\,Nk_BT_c\Bigl(\frac{T}{T_c}\Bigr)^{5/2}, \qquad C_V = \frac{15}4\frac{\zeta(5/2)}{\zeta(3/2)}Nk_B\Bigl(\frac{T}{T_c}\Bigr)^{3/2}, \qquad pV = \tfrac23U ,
> $$
>
> so $U \propto T^{5/2}$ and $C_V \propto T^{3/2}$ both vanish as $T \to 0$, and $C_V \to 1.926\,Nk_B$ as $T \to T_c^-$. At fixed $T$, $V$, $U$ and $p$ do not depend on $N$: added particles go into $N_0$.
>
> *Model:* the Setup; *applies:* ideal gas, $T < T_c$.
>
> *Source: Mao §4.6.4, eq. (4.153) · PHY 510 Problem Set 6, part (f), official solution · level-B home: [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-5|Theorem §B12.1.5]]*

^thm-c4b-7-5

> [!derivation]- Derivation
> **Step 1.** Below $T_c$, $z = 1$ in [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] for the excited states: $U = \tfrac32A\Gamma(\tfrac32)(k_BT)^{5/2}\zeta(\tfrac52)$, and $pV = U/\nu$ with $\nu = \tfrac32$. With $A \propto V$, neither involves $N$.
>
> **Step 2.** At $T_c$, $N = A\Gamma(\tfrac32)(k_BT_c)^{3/2}\zeta(\tfrac32)$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]]). Dividing, $U/N = \tfrac32k_BT\,(T/T_c)^{3/2}\zeta(\tfrac52)/\zeta(\tfrac32)$; numerically $\tfrac32\cdot1.341/2.612 = 0.770$.
>
> **Step 3.** $U \propto T^{5/2}$ at fixed $N$, $V$ gives $C_V = \tfrac52U/T$, i.e. $\tfrac{15}4\cdot0.5135 = 1.926$ at $T = T_c$.

^der-c4b-7-5

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]]

> [!remark] Remark: Through the transition and above
> Mao's numerical curves (§4.6.4, Figure 4.7) show $U(T)$ smooth through $T_c$, $C_V$ peaking at $T_c$ with a finite cusp (a jump in $dC_V/dT$, not in $C_V$), and $U \to \tfrac32Nk_BT$, $C_V \to \tfrac32Nk_B$ for $T \gg T_c$. Above $T_c$ the closed form $C_V/Nk_B = \tfrac{15}4G_{5/2}/G_{3/2} - \tfrac94G_{3/2}/G_{1/2}$ ([[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-5|Theorem §B12.1.5]]) meets the value of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-5|Theorem §C4b.7.5]] at $T_c$ because $G_{1/2}(1) = \infty$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 4).

^rem-c4b-7-1

> [!law] Law §C4b.7.6: Bose–Einstein Condensation in Helium and in Atomic Gases
> 1. **Liquid $^4$He** turns superfluid at the lambda point, $T_\lambda = 2.17$ K under its saturated vapour (discovered 1938; London proposed the link to Bose condensation). The ideal-gas formula of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] at the liquid's density, $\rho_3 = 2.18\times10^{28}\ \text{m}^{-3}$, gives $T_c = 3.1$ K: the right scale, but the liquid is strongly interacting and its lambda anomaly is far sharper than the cusp of [[§C4b.7 Bose–Einstein Condensation#^rem-c4b-7-1|§C4b.7, Remark: Through the transition and above]].
> 2. **Dilute alkali vapours.** Anderson et al. (1995) observed a condensate in magnetically trapped $^{87}$Rb near $170$ nK: a narrow low-momentum peak appeared on top of the broad thermal distribution. For $\rho_3 = 10^{19}$–$10^{20}\ \text{m}^{-3}$ the uniform formula gives $T_c \simeq 0.09$–$0.4\ \mu$K, the same range, the large $m$ and low $\rho_3$ of $T_c \propto \rho_3^{2/3}/m$ explaining the nanokelvin scale; a quantitative comparison uses the trap's $g(\epsilon)$ ([[§C4b.7 Bose–Einstein Condensation#^ex-c4b-7-1|Example §C4b.7.1]]).
>
> *Valid when:* part 1 as a statement of scale only (interactions are strong); part 2 for a dilute, weakly interacting gas.
>
> *Source: Mao §4.6.5 · Anderson et al., Science 269, 198 (1995), as cited by Mao [27] · level-B homes: [[§B12.1★ Bose–Einstein Condensation#^law-b12-1-6|Law §B12.1.6]], [[§B12.1★ Bose–Einstein Condensation#^law-b12-1-7|Law §B12.1.7]]*

^law-c4b-7-6

> [!theorem] Theorem §C4b.7.7: The Condensate Is One Extended Orbital
> For $g_s = 1$ below $T_c$, with field operator $\hat\psi(\mathbf r) = V^{-1/2}\sum_{\mathbf k}e^{i\mathbf k\cdot\mathbf r}\hat a_{\mathbf k}$:
>
> 1. the momentum distribution is $\langle\hat n_{\mathbf k}\rangle = N_0\,\delta_{\mathbf k,0} + f(\epsilon_k)\,(1 - \delta_{\mathbf k,0})$, a macroscopic spike at $\mathbf k = 0$ on a smooth thermal background;
> 2. the density $\langle\hat\psi^\dagger(\mathbf r)\hat\psi(\mathbf r)\rangle = N/V$ is uniform;
> 3. the one-body density matrix keeps a finite value at large separation:
>
> $$
> \rho_1(\mathbf r, \mathbf r') = \langle\hat\psi^\dagger(\mathbf r)\hat\psi(\mathbf r')\rangle = \frac{N_0}{V} + \int\frac{d^3k}{(2\pi)^3}f(\epsilon_k)\,e^{i\mathbf k\cdot(\mathbf r' - \mathbf r)} \xrightarrow{|\mathbf r - \mathbf r'|\to\infty} \frac{N_0}{V} \ne 0
> $$
>
> (off-diagonal long-range order), while above $T_c$ it decays to $0$.
>
> *Model:* the Setup, thermodynamic limit; *applies:* ideal gas. Superfluidity, the response to flow, needs interactions and is not part of this result ([[§B12.1★ Bose–Einstein Condensation#^law-b12-1-6|Law §B12.1.6]]).
>
> *Source: Mao §4.6.4 (qualitative description) · formulas added here, standard (Penrose–Onsager criterion)*

^thm-c4b-7-7

> [!derivation]- Derivation
> **Step 1.** In the grand ensemble of [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], $\langle\hat a^\dagger_{\mathbf k}\hat a_{\mathbf k'}\rangle = \delta_{\mathbf k\mathbf k'}\langle\hat n_{\mathbf k}\rangle$, since the states are diagonal in the occupations. With [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]] and [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] this gives part 1.
>
> **Step 2.** Then $\rho_1(\mathbf r, \mathbf r') = V^{-1}\sum_{\mathbf k}\langle\hat n_{\mathbf k}\rangle e^{i\mathbf k\cdot(\mathbf r' - \mathbf r)}$. At $\mathbf r = \mathbf r'$ the sum is $N/V$ (part 2). Keep the $\mathbf k = 0$ term and replace the rest by an integral ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]).
>
> **Step 3.** $f(\epsilon_k) \propto k^{-2}$ near $k = 0$ (at $\mu = 0$) and decays exponentially at large $k$, so it is integrable over $d^3k$; by the Riemann–Lebesgue lemma its Fourier transform tends to $0$ at large separation, leaving $N_0/V$. Above $T_c$, $N_0/V \to 0$ and $\mu < 0$, so only the decaying integral remains.

^der-c4b-7-6

*Uses:* [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]], [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

> [!remark]- Connections
> - The same scale $T_Q$ sets the Fermi temperature, $T_F \simeq 1.21\,T_Q$ — [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]].
> - Black-body photons do not condense because their number is not conserved — [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]].
> - Condensation in any dimension for any power-law dispersion — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]].
