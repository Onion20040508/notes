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

So far the means were varied with the energy levels fixed. Changing the volume is different: it changes the Hamiltonian, so it moves the levels themselves. Splitting $dU$ into "probabilities change" and "levels move" separates heat from work, and the statistical entropy then satisfies $dS = \delta Q_{\text{rev}}/T$. This closes the loop with Chapter C1: $k_BH_{\max}$ is the entropy that Carathéodory's integrating factor produces ([[§C1.4 Temperature and Entropy#^thm-c1-4-3|Theorem §C1.4.3]]). Level B makes the same split in its statistical identity ([[§B6.2 Temperature, Pressure and Chemical Potential from Entropy#^thm-b6-2-7|Theorem §B6.2.7]]).

**Setup.** A system with energy levels $E_i(V)$ that depend on the volume, followed by label $i$ as $V$ changes (instantaneous eigenstates in a quantum description), along a reversible sequence of canonical states $p_i = p_i^\ast$ at fixed $N$. The pressure is $p$; probabilities are $p_i$.

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
> *Model:* as in the Setup; *applies:* reversible steps at fixed $N$, with the levels moved slowly enough that a system in level $i$ stays in level $i$.
>
> *Source: Mao §4.3.8, eqs. (4.53)–(4.54)*

^thm-c4a-7-1

> [!derivation]- Derivation
> The product rule splits $dU$. Work is the energy change from moving the levels at fixed occupations, which is $\sum_ip_i\,dE_i$; heat is the rest. With $E_i = E_i(V)$, $dE_i = (\partial E_i/\partial V)dV$, and comparing with $\delta W_{\text{on,rev}} = -p\,dV$ ([[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-2|Def. §C1.2.2]]) defines $p$.

^der-c4a-7-1

*Uses:* [[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-2|Def. §C1.2.2]]

> [!theorem] Theorem §C4a.7.2: The Clausius Equality from Maximum Entropy
> Along reversible canonical states,
>
> $$
> dS_{\text{eq}} = \frac{\delta Q_{\text{rev}}}{T}, \qquad dU = T\,dS_{\text{eq}} - p\,dV, \qquad dF = -S_{\text{eq}}\,dT - p\,dV\quad(N\ \text{fixed}) ,
> $$
>
> with $d\ln Z = -U\,d\beta + \beta p\,dV$. So $S_{\text{eq}} = k_BH_{\max}$ is the entropy state function of Chapter C1, and $1/T$ is the integrating factor of $\delta Q_{\text{rev}} = dU + p\,dV$; reversible adiabats are the surfaces $S_{\text{eq}} = \text{const}$. Derivatives of $F(T, V, N)$ give $S_{\text{eq}} = -(\partial F/\partial T)_{V,N}$ and $p = -(\partial F/\partial V)_{T,N}$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]] with $E_i(V)$; *applies:* reversible paths only; irreversible processes obey [[§C1.5 The Second Law for Irreversible Processes#^thm-c1-5-9|Theorem §C1.5.9]].
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
> **Step 3.** $d\ln Z = -\frac1Z\sum_ie^{-\beta E_i}(E_i\,d\beta + \beta\,dE_i) = -U\,d\beta - \beta\sum_ip_i\frac{\partial E_i}{\partial V}dV = -U\,d\beta + \beta p\,dV$. With $F = -k_BT\ln Z$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]), $dF = -S_{\text{eq}}\,dT - p\,dV$.

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
> and $\Phi$ has natural variables $(T, V, \mu)$. For a homogeneous extensive system the Euler relation gives
>
> $$
> \Phi = -pV, \qquad p = \frac{k_BT}{V}\ln\Xi .
> $$
>
> When particles cross the boundary, $\sum_iE_i\,dp_i$ includes the energy they carry and is no longer heat alone.
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
> Constraints select the equilibrium probabilities ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]); $k_BH_{\max}$ is their entropy ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]); Legendre transforms give the potentials ([[§C4a.6 Massieu Functions and Thermodynamic Potentials|§C4a.6]]); moving the external parameters gives work ([[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|Theorem §C4a.7.1]]). Whether a given evolving state approaches one of these ensembles is a separate, dynamical question (Mao Ch. 5, level C to come).

^rem-c4a-7-1

> [!remark]- Connections
> - The same split appears in quantum adiabatic processes: slowly moved levels keep their occupations, which is why $\sum p_i\,dE_i$ is work — [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-1|QM Theorem §C11.2.1]] for the dynamics of $\hat\rho$.
> - Chapter C1's Carathéodory construction and this section produce the same $S$ and $T$ — [[§C1.3 Carathéodory's Principle and the Integrating Factor#^thm-c1-3-4|Theorem §C1.3.4]], [[§C1.4 Temperature and Entropy#^thm-c1-4-2|Theorem §C1.4.2]].
