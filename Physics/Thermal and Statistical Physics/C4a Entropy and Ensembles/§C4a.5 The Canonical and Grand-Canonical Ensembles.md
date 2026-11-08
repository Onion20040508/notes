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
> which coincides with the microcanonical $\beta = \partial\ln\Omega/\partial E$ of [[§C2.4 Temperature and Entropy from Counting#^def-c2-4-1|Def. §C2.4.1]].
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
> At fixed $V$, $N$ with prescribed mean energy, or in contact with a reservoir at $T$ ([[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-5|Theorem §C4a.5.5]]),
>
> $$
> p_i^{\text{can}} = \frac{e^{-\beta E_i}}{Z}, \qquad Z(\beta, V, N) = \sum_ie^{-\beta E_i}, \qquad U = \sum_ip_i^{\text{can}}E_i = -\Bigl(\frac{\partial\ln Z}{\partial\beta}\Bigr)_{V,N} .
> $$
>
> - Index set: every microstate with particle number $N$, at every energy.
> - Two readings of the same formula: (1) $U$ given: solve $U = -\partial_\beta\ln Z$ for $\beta$; (2) $T$ given: $U$ follows.
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
> and the **fugacity** is $z \equiv e^{-\eta_N} = e^{\beta\mu}$, so that $e^{-\eta_NN_i} = z^{N_i}$.
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

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-1|Theorem §C4a.5.1]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]], [[§C1.6 Thermodynamic Potentials and Variational Principles#^thm-c1-6-2|Theorem §C1.6.2]]

> [!theorem] Theorem §C4a.5.4: The Grand-Canonical Ensemble
> $$
> p_i^{\text{gc}} = \frac{e^{-\beta(E_i - \mu N_i)}}{\Xi} = \frac{z^{N_i}e^{-\beta E_i}}{\Xi}, \qquad \Xi(\beta, \mu, V) = \sum_ie^{-\beta(E_i - \mu N_i)} ,
> $$
>
> - Index set: every microstate at every energy and every particle number.
> - Two readings: (1) $U$, $\bar N$ given: solve for $T$, $\mu$; (2) $T$, $\mu$ given by a reservoir ([[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-5|Theorem §C4a.5.5]]): $U$, $\bar N$ follow.
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
> System and reservoir $R$, weakly coupled, together isolated with uniform weights on pair states. For a system microstate $i$:
>
> 1. Exactly (energy exchange only),
>
> $$
> p_i = \frac{\Omega_R(E_{\text{tot}} - E_i, N_R)}{\sum_j\Omega_R(E_{\text{tot}} - E_j, N_R)} ;
> $$
>
> all the $i$-dependence sits in $\Omega_R$.
> 2. For a large reservoir, $p_i \simeq e^{-\beta E_i}/Z$, and with particle exchange $p_i \simeq e^{-\beta(E_i - \mu N_i)}/\Xi$, where $T$, $\mu$ are the reservoir's.
> 3. Per energy level, $P(E) = g(E)e^{-\beta E}/Z$, with $g(E)$ the degeneracy.
>
> *Model:* [[§C2.4 Temperature and Entropy from Counting#^mod-c2-4-1|Model §C2.4.1]] with $B$ a reservoir, exchanging energy, and for the grand case also particles; *applies:* $E_i^2 \ll k_BT^2C_R$ for the relevant $E_i$, with $C_R$ the reservoir's heat capacity (likewise for $N_i$), which holds as $C_R \to \infty$ at fixed $E_i$.
>
> *Source: PHY 510 Problem Set 4, Problem 3, official solution · level-B home: [[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]]*

^thm-c4a-5-5

> [!derivation]- Derivation
> **Step 1** (item 1). The pair states with the system in $i$ are $i$ combined with any reservoir state of energy $E_{\text{tot}} - E_i$ (and particle number $N_{\text{tot}} - N_i$). Uniform pair weights ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]]) make $p_i$ proportional to their number $\Omega_R$.
>
> **Step 2** (second-order expansion, energy). Write $\ln\Omega_R = S_R/k_B$, so $\partial_{E_R}\ln\Omega_R = \beta$ and $\partial_{E_R}\beta = -1/(k_BT^2C_R)$. Then
>
> $$
> \ln\Omega_R(E_{\text{tot}} - E_i) = \ln\Omega_R(E_{\text{tot}}) - \beta E_i - \frac{E_i^2}{2k_BT^2C_R} + \dots
> $$
>
> The quadratic term is negligible exactly under the *applies* condition; dropping it, $\Omega_R(E_{\text{tot}} - E_i) \simeq \Omega_R(E_{\text{tot}})\,e^{-\beta E_i}$, and the $i$-independent factor $\Omega_R(E_{\text{tot}})$ drops out of item 1's ratio: $p_i = e^{-\beta E_i}/Z$.
>
> **Step 3** (particles). Now $\partial_{N_R}\ln\Omega_R = -\beta\mu$ and $N_R = N_{\text{tot}} - N_i$, so the linear term in $N_i$ is $(-N_i)(-\beta\mu) = +\beta\mu N_i$:
>
> $$
> \ln\Omega_R(E_{\text{tot}} - E_i, N_{\text{tot}} - N_i) \simeq \ln\Omega_R(E_{\text{tot}}, N_{\text{tot}}) - \beta(E_i - \mu N_i) ,
> $$
>
> with second-order terms again suppressed by the reservoir's size. Normalizing gives $e^{-\beta(E_i - \mu N_i)}/\Xi$.
>
> **Step 4** (item 3). The $g(E)$ states at energy $E$ share one weight; add them.

^der-c4a-5-5

*Uses:* [[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]], [[§C2.4 Temperature and Entropy from Counting#^mod-c2-4-1|Model §C2.4.1]], [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]

> [!remark]- Connections
> - The canonical ensemble at fixed $N$ and the grand-canonical one are related by $\Xi = \sum_Nz^NZ(\beta; N)$ — [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]].
> - The partition functions generate the thermodynamic potentials — [[§C4a.6 Massieu Functions and Thermodynamic Potentials|§C4a.6]].
> - Adsorption on independent sites is the simplest grand-canonical system — [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-4|Example §C4a.11.4]]; level B: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-5|Theorem §B7.3.5]].
