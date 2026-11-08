---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.7
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.6 Massieu Functions and Thermodynamic Potentials]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy]] →

*Sources: Mao, PHY 510 notes, §4.3.8, eqs. (4.53)–(4.61) · PHY 510 Lecture 10/1.*

In [[§C4a.5 The Canonical and Grand-Canonical Ensembles|§C4a.5]] only the $p_i$ moved. A change of volume acts on the Hamiltonian, so now the levels $E_i(V)$ shift as well, and the product rule splits $dU$ into a part from each. The first part is heat, the second work, and $dS = \delta Q_{\text{rev}}/T$ follows; hence $k_BH_{\max}$ is the entropy that Chapter C1 built from Carathéodory's integrating factor ([[§C1.4 Temperature and Entropy#^thm-c1-4-3|Theorem §C1.4.3]]). Level B makes the same split in its statistical identity ([[§B6.2 Temperature, Pressure and Chemical Potential from Entropy#^thm-b6-2-7|Theorem §B6.2.7]]).

**Setup.**
- Levels $E_i(V)$; each state keeps its label $i$ as $V$ changes (quantum: instantaneous eigenstates).
- A reversible path through canonical states $p_i = p_i^\ast(\beta, V)$ at fixed $N$.
- Notation: $p$ is the pressure, $p_i$ a probability.

> [!theorem] Theorem §C4a.7.1: Heat Moves Populations, Work Moves Levels
> $$
> dU = d\Bigl(\sum_ip_iE_i\Bigr) = \underbrace{\sum_iE_i\,dp_i}_{\delta Q_{\text{rev}}} + \underbrace{\sum_ip_i\,dE_i}_{\delta W_{\text{on,rev}}} ,
> $$
>
> and for a simple compressible system
>
> $$
> \delta W_{\text{on,rev}} = \sum_ip_i\frac{\partial E_i}{\partial V}\,dV = -p\,dV, \qquad p = -\sum_ip_i\frac{\partial E_i}{\partial V} .
> $$
>
> *Model:* as in the Setup; *applies:* reversible steps at fixed $N$, with the levels moved slowly enough that a system in level $i$ stays in level $i$ (adiabatic theorem, [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]).
>
> *Source: Mao §4.3.8, eqs. (4.53)–(4.54)*

^thm-c4a-7-1

> [!derivation]- Derivation
> The product rule gives the two sums. By the adiabatic theorem [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]], a slow change of $V$ with no heat contact leaves every $p_i$ fixed, so the energy it delivers is $\sum_ip_i\,dE_i$: this is the work. The first law assigns the remainder $\sum_iE_i\,dp_i$ to heat. With $dE_i = (\partial E_i/\partial V)dV$, comparison with $\delta W_{\text{on,rev}} = -p\,dV$ ([[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-2|Def. §C1.2.2]]) gives $p$.

^der-c4a-7-1

*Uses:* [[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-2|Def. §C1.2.2]], [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]

> [!theorem] Theorem §C4a.7.2: The Clausius Equality from Maximum Entropy
> Along reversible canonical states,
>
> $$
> dS_{\text{eq}} = \frac{\delta Q_{\text{rev}}}{T}, \qquad dU = T\,dS_{\text{eq}} - p\,dV, \qquad dF = -S_{\text{eq}}\,dT - p\,dV\quad(N\ \text{fixed}) ,
> $$
>
> with $d\ln Z = -U\,d\beta + \beta p\,dV$. Consequences:
>
> 1. $1/T$ is an integrating factor: $\delta Q_{\text{rev}}/T = d(k_BH_{\max})$ with $\delta Q_{\text{rev}} = dU + p\,dV$, so $S_{\text{eq}}$ is the entropy of [[§C1.4 Temperature and Entropy#^thm-c1-4-3|Theorem §C1.4.3]], and reversible adiabats are its level sets.
> 2. $S_{\text{eq}} = -(\partial F/\partial T)_{V,N}$ and $p = -(\partial F/\partial V)_{T,N}$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]] with $E_i(V)$; *applies:* quasi-static sequences of canonical states (the irreversible case is [[§C1.5 The Second Law for Irreversible Processes#^thm-c1-5-9|Theorem §C1.5.9]]).
>
> *Source: Mao §4.3.8, eqs. (4.55)–(4.57)*

^thm-c4a-7-2

> [!derivation]- Derivation
> **Step 1.** The instantaneous distribution has $\ln p_i = -\ln Z - \beta E_i$, even as the $E_i$ change. With $\sum_idp_i = 0$,
>
> $$
> dS_{\text{eq}} = -k_B\sum_i(\ln p_i + 1)\,dp_i = k_B\beta\sum_iE_i\,dp_i = \frac{\delta Q_{\text{rev}}}{T}
> $$
>
> by [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]].
>
> **Step 2.** Substitute in $dU = \delta Q_{\text{rev}} + \delta W_{\text{on,rev}}$: $dU = T\,dS_{\text{eq}} - p\,dV$.
>
> **Step 3.** $d\ln Z = -\frac1Z\sum_ie^{-\beta E_i}(E_i\,d\beta + \beta\,dE_i) = -U\,d\beta - \beta\sum_ip_i\frac{\partial E_i}{\partial V}dV = -U\,d\beta + \beta p\,dV$. With $F = -k_BT\ln Z$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]), $dF = -k_B\ln Z\,dT - k_BT\,d\ln Z$; insert $d\beta = -dT/k_BT^2$, so $-k_BT(-U\,d\beta) = -(U/T)\,dT$, and use $S_{\text{eq}} = k_B\ln Z + U/T$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]): $dF = -S_{\text{eq}}\,dT - p\,dV$.

^der-c4a-7-2

*Uses:* [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]

> [!theorem] Theorem §C4a.7.3: With Particle Exchange
> For the grand-canonical distribution,
>
> $$
> T\,dS_{\text{eq}} = \sum_i(E_i - \mu N_i)\,dp_i = dU + p\,dV - \mu\,d\bar N ,
> $$
>
> so
>
> $$
> dU = T\,dS_{\text{eq}} - p\,dV + \mu\,d\bar N, \qquad d\Phi = -S_{\text{eq}}\,dT - p\,dV - \bar N\,d\mu ,
> $$
>
> so $\Phi$ is a function of $(T, V, \mu)$, and homogeneity ([[§C1.8 The Ideal Gas, Extensivity and the Paramagnetic Salt#^ex-c1-8-5|Example §C1.8.5]]) gives
>
> $$
> \Phi = -pV, \qquad p = \frac{k_BT}{V}\ln\Xi .
> $$
>
> With particle exchange the heat is $T\,dS_{\text{eq}} = \sum_i(E_i - \mu N_i)\,dp_i$; the population term $\sum_iE_i\,dp_i$ differs from it by $\mu\,d\bar N$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]] with $E_i(V)$; *applies:* reversible; Euler relation for homogeneous systems ([[§C1.8 The Ideal Gas, Extensivity and the Paramagnetic Salt#^ex-c1-8-5|Example §C1.8.5]]).
>
> *Source: Mao §4.3.8, eqs. (4.58)–(4.61) · level-B home: [[§B3.3 Chemical Potential and Conditions for Equilibrium#^thm-b3-3-2|Theorem §B3.3.2]]*

^thm-c4a-7-3

> [!derivation]- Derivation
> **Step 1.** With $\ln p_i = -\ln\Xi - \beta(E_i - \mu N_i)$ and $\sum_idp_i = 0$: $T\,dS_{\text{eq}} = -k_BT\sum_i\ln p_i\,dp_i = \sum_i(E_i - \mu N_i)\,dp_i$.
>
> **Step 2.** $\sum_iE_i\,dp_i = dU - \sum_ip_i\,dE_i = dU + p\,dV$ ([[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]]) and $\sum_iN_i\,dp_i = d\bar N$ (each $N_i$ is fixed).
>
> **Step 3.** $\Phi = U - TS_{\text{eq}} - \mu\bar N$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-3|Theorem §C4a.6.3]]), so $d\Phi = dU - T\,dS - S\,dT - \mu\,d\bar N - \bar N\,d\mu$; insert Step 2.
>
> **Step 4.** Euler: $U = TS - pV + \mu\bar N$, so $\Phi = -pV$, and $\Phi = -k_BT\ln\Xi$ gives $p$.

^der-c4a-7-3

*Uses:* [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-3|Theorem §C4a.6.3]], [[§C1.8 The Ideal Gas, Extensivity and the Paramagnetic Salt#^ex-c1-8-5|Example §C1.8.5]]

> [!remark] Remark: The route of the chapter so far
> | input | operation | output | box |
> | --- | --- | --- | --- |
> | restrictions and means | maximize $H$ | $p^\ast$, $Z(\eta)$ | [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] |
> | $p^\ast$ | count copies | $S_{\text{eq}} = k_BH_{\max}$ | [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]] |
> | $H_{\max}(\bar A)$ | Legendre transform | $\ln Z$, $F$, $\Phi$ | [[§C4a.6 Massieu Functions and Thermodynamic Potentials|§C4a.6]] |
> | $E_i(V)$ | move $V$ slowly | $\delta W = \sum_ip_i\,dE_i$, $p$ | [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]] |
> | a state out of equilibrium | time evolution | relaxation to $p^\ast$? | not here: Chapter C5 ([[§C5.4 Markov Dynamics and the Apparent Arrow of Time#^thm-c5-4-1|Theorem §C5.4.1]]) |

^rem-c4a-7-1

> [!remark]- Connections
> - Why $\sum_ip_i\,dE_i$ is work: under a slow change of $V$ the occupations stay put — adiabatic theorem [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]; the general evolution of $\hat\rho$ is the von Neumann equation [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-1|QM Theorem §C11.2.1]].
> - Chapter C1's Carathéodory construction and this section produce the same $S$ and $T$ — [[§C1.3 Carathéodory's Principle and the Integrating Factor#^thm-c1-3-4|Theorem §C1.3.4]], [[§C1.4 Temperature and Entropy#^thm-c1-4-2|Theorem §C1.4.2]].
