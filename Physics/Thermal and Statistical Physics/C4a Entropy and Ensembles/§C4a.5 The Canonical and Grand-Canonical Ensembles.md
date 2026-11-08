---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.5
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.4 Why the Maximum Is Thermodynamic Entropy]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.6 Massieu Functions and Thermodynamic Potentials]] →

*Sources: Mao, PHY 510 notes, §4.3.5–§4.3.6, eqs. (4.35)–(4.42) · PHY 510 Lectures 9/29, 10/1 · PHY 510 Problem Set 4, Problem 3, official solution.*

The general MaxEnt solution ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]) carries unnamed multipliers. With $S_{\text{eq}} = k_BH_{\max}$ ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]) they can be named: the energy multiplier is $\beta = 1/k_BT$, and the particle multiplier is $-\beta\mu$. That gives the canonical and grand-canonical ensembles. Level B derived both from a large reservoir ([[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]], [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-1|Theorem §B7.3.1]]); that route is recorded here as a second derivation, after the course's.

**Setup.** Fixed volume $V$; microstates $i$ with energies $E_i$ and, where particles can be exchanged, particle numbers $N_i$; the MaxEnt solution $p_i^\ast$ of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]].

## Canonical

> [!theorem] Theorem §C4a.5.1: The Energy Multiplier Is $\beta$
> When the only prescribed mean is $U = \sum_ip_iE_i$, at fixed $V$ and $N$,
>
> $$
> dH_{\max} = \eta_E\,dU, \qquad \eta_E = \Bigl(\frac{\partial H_{\max}}{\partial U}\Bigr)_{V,N} = \frac1{k_B}\Bigl(\frac{\partial S_{\text{eq}}}{\partial U}\Bigr)_{V,N} = \frac1{k_BT} \equiv \beta ,
> $$
>
> the same inverse temperature that state counting produced ([[§C2.4 Temperature and Entropy from Counting#^def-c2-4-1|Def. §C2.4.1]]).
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] with one constraint; *applies:* neighbouring MaxEnt states with the same energies $E_i$.
>
> *Source: Mao §4.3.5, eq. (4.35)*

^thm-c4a-5-1

> [!derivation]- Derivation
> **Step 1.** For neighbouring maxima at fixed $V$, $N$ the $E_i$ do not change and $\sum_idp_i^\ast = 0$, so
>
> $$
> dH_{\max} = -\sum_i(\ln p_i^\ast + 1)\,dp_i^\ast = -\sum_i\ln p_i^\ast\,dp_i^\ast .
> $$
>
> **Step 2.** $\ln p_i^\ast = -\ln Z - \eta_EE_i$, and the $\ln Z$ term drops by $\sum_idp_i^\ast = 0$: $dH_{\max} = \eta_E\sum_iE_i\,dp_i^\ast = \eta_E\,dU$.
>
> **Step 3.** $S_{\text{eq}} = k_BH_{\max}$ ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]) and $(\partial S/\partial U)_{V,N} = 1/T$ ([[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-2|Theorem §C1.6.2]]).

^der-c4a-5-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]], [[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-2|Theorem §C1.6.2]]

> [!theorem] Theorem §C4a.5.2: The Canonical Ensemble
> At fixed $V$, $N$ with prescribed mean energy, or in contact with a reservoir at $T$,
>
> $$
> p_i^{\text{can}} = \frac{e^{-\beta E_i}}{Z}, \qquad Z(\beta, V, N) = \sum_ie^{-\beta E_i}, \qquad U = \sum_ip_i^{\text{can}}E_i = -\Bigl(\frac{\partial\ln Z}{\partial\beta}\Bigr)_{V,N} .
> $$
>
> The sum runs over all microstates with particle number $N$, whatever their energy. Either $U$ is given and fixes $\beta$, or a reservoir fixes $T$ and the formula predicts $U$; individual microstates have different energies in both readings.
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^def-c4a-3-1|Def. §C4a.3.1]], second row; *applies:* $Z$ convergent.
>
> *Source: Mao §4.3.5, eqs. (4.36)–(4.38) · level-B homes: [[§B7.1 The Boltzmann Factor and the Partition Function#^def-b7-1-2|Def. §B7.1.2]], [[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]]*

^thm-c4a-5-2

> [!derivation]- Derivation
> Put $\eta_E = \beta$ from [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-1|Theorem §C4a.5.1]] into [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] with $A_E(i) = E_i$; the mean formula is the last line of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]].

^der-c4a-5-2

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-1|Theorem §C4a.5.1]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

## Grand canonical

> [!theorem] Theorem §C4a.5.3: The Particle Multiplier Is $-\beta\mu$
> With prescribed $U$ and $\bar N$ at fixed $V$,
>
> $$
> dH_{\max} = \eta_E\,dU + \eta_N\,d\bar N, \qquad \eta_E = \beta = \frac{1}{k_BT}, \qquad \eta_N = -\beta\mu ,
> $$
>
> and the **fugacity** is $z \equiv e^{-\eta_N} = e^{\beta\mu}$, one factor per particle in the weight $e^{-\eta_NN_i} = z^{N_i}$.
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] with two constraints; *applies:* $\mu$ the chemical potential of $dU = T\,dS + \mu\,d\bar N$ at fixed $V$.
>
> *Source: Mao §4.3.6, eqs. (4.39)–(4.41)*

^thm-c4a-5-3

> [!derivation]- Derivation
> **Step 1.** As in [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^der-c4a-5-1|Derivation §C4a.5.1]], with $\ln p_i^\ast = -\ln\Xi - \eta_EE_i - \eta_NN_i$ and $\sum_iN_i\,dp_i^\ast = d\bar N$: $dH_{\max} = \eta_E\,dU + \eta_N\,d\bar N$.
>
> **Step 2.** Thermodynamics at fixed $V$: $dS_{\text{eq}} = (dU - \mu\,d\bar N)/T$. With $dS_{\text{eq}} = k_B\,dH_{\max}$ ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]), comparing coefficients gives $k_B\eta_E = 1/T$ and $k_B\eta_N = -\mu/T$.

^der-c4a-5-3

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-1|Theorem §C4a.5.1]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]

> [!theorem] Theorem §C4a.5.4: The Grand-Canonical Ensemble
> $$
> p_i^{\text{gc}} = \frac{e^{-\beta(E_i - \mu N_i)}}{\Xi} = \frac{z^{N_i}e^{-\beta E_i}}{\Xi}, \qquad \Xi(\beta, \mu, V) = \sum_ie^{-\beta(E_i - \mu N_i)} ,
> $$
>
> the sum running over all energies and all particle numbers. Either the means $U$, $\bar N$ fix $T$, $\mu$, or reservoirs fix $T$, $\mu$ and the distribution predicts $U$, $\bar N$.
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^def-c4a-3-1|Def. §C4a.3.1]], third row; *applies:* $\Xi$ convergent.
>
> *Source: Mao §4.3.6, eq. (4.42) · level-B homes: [[§B7.3 The Grand Canonical Ensemble#^def-b7-3-2|Def. §B7.3.2]], [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-1|Theorem §B7.3.1]]*

^thm-c4a-5-4

> [!derivation]- Derivation
> Put the multipliers of [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-3|Theorem §C4a.5.3]] into [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] with $A_E(i) = E_i$, $A_N(i) = N_i$.

^der-c4a-5-4

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-3|Theorem §C4a.5.3]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

## The same ensembles from a reservoir

> [!theorem] Theorem §C4a.5.5: Canonical and Grand-Canonical Weights from a Reservoir
> Let a small system be weakly coupled to a large reservoir, the pair isolated and microcanonical. Then for a system microstate $i$
>
> $$
> p_i = \frac{\Omega_R(E_{\text{tot}} - E_i, N_R)}{\sum_j\Omega_R(E_{\text{tot}} - E_j, N_R)} \simeq \frac{e^{-\beta E_i}}{Z}
> $$
>
> with energy exchange, and $p_i \simeq e^{-\beta(E_i - \mu N_i)}/\Xi$ when particles are exchanged as well. The system's states are unequally likely, though the pair's are equal, because different system states leave different numbers of reservoir states. The probability of an energy level is $P(E) = g(E)e^{-\beta E}/Z$, with $g(E)$ its degeneracy.
>
> *Model:* [[§C2.4 Temperature and Entropy from Counting#^mod-c2-4-1|Model §C2.4.1]] with $B$ a reservoir; *applies:* the reservoir so large that the exchanges do not change its $T$ and $\mu$, so its entropy is linear over the relevant range.
>
> *Source: PHY 510 Problem Set 4, Problem 3, official solution · level-B home: [[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]]*

^thm-c4a-5-5

> [!derivation]- Derivation
> **Step 1** (counting). Fixing the system in $i$ fixes the reservoir energy $E_{\text{tot}} - E_i$ (and $N_{\text{tot}} - N_i$). Every compatible pair state is equally likely ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]]), so $p_i \propto \Omega_R$ of the reservoir.
>
> **Step 2** (expand). With $S_R = k_B\ln\Omega_R$, $\partial S_R/\partial E_R = 1/T$ and $\partial S_R/\partial N_R = -\mu/T$,
>
> $$
> S_R(E_{\text{tot}} - E_i, N_{\text{tot}} - N_i) \simeq S_R(E_{\text{tot}}, N_{\text{tot}}) - \frac{E_i}{T} + \frac{\mu N_i}{T} .
> $$
>
> The sign of the last term is $(-N_i)(-\mu/T)$. Higher terms involve derivatives of $1/T$ and $\mu/T$ with respect to the reservoir's variables, which vanish for a large reservoir.
>
> **Step 3** (normalize). Exponentiate $S_R/k_B$; the common factor cancels in the ratio.
>
> **Step 4** (levels). All $g(E)$ states of energy $E$ have the same weight, so their probabilities add.

^der-c4a-5-5

*Uses:* [[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]], [[§C2.4 Temperature and Entropy from Counting#^mod-c2-4-1|Model §C2.4.1]], [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]

> [!remark]- Connections
> - The canonical ensemble at fixed $N$ and the grand-canonical one are related by $\Xi = \sum_Nz^NZ(\beta; N)$ — [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]].
> - The partition functions generate the thermodynamic potentials — [[§C4a.6 Massieu Functions and Thermodynamic Potentials|§C4a.6]].
> - Adsorption on independent sites is the simplest grand-canonical system — [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-4|Example §C4a.11.4]]; level B: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-5|Theorem §B7.3.5]].
