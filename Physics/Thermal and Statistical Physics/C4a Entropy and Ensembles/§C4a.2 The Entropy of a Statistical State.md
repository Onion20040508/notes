---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.2
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.1 Shannon Entropy]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.3 Maximum Entropy and Lagrange Multipliers]] →

*Sources: Mao, PHY 510 notes, §4.2, eqs. (4.8)–(4.15) · Jaynes, Information Theory and Statistical Mechanics II (1957), §7 · PHY 510 Lecture 9/24.*

Shannon's measure applies to any list of alternatives. Statistical mechanics applies it to the microstates of Chapter C3: the uncertainty about which complete microscopic state the system is in, given what is known macroscopically. This section fixes the units (nats), the meaning of the alternatives, and the classical and quantum forms. Level B introduced the Gibbs entropy $-k_B\sum p\ln p$ ([[§B6.3 Entropy, Information and the Gibbs Paradox#^def-b6-3-1|Def. §B6.3.1]]); here it starts as an information measure, and its identification with thermodynamic entropy is derived in [[§C4a.4 Why the Maximum Is Thermodynamic Entropy|§C4a.4]].

**Setup.** A system whose microstates are labelled by $i$ ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^def-c2-1-1|Def. §C2.1.1]]), with probabilities $p_i$; or a classical density $\rho_{\text{cl}}$ on phase space; or a density operator $\hat\rho$ ([[§C3.1 Microstates and Statistical States in Parallel|§C3.1]], [[§C3.2 The Density Operator as an Ensemble|§C3.2]]).

> [!definition] Definition §C4a.2.1: Entropy in Nats
> From here on,
>
> $$
> H[p] \equiv -\sum_ip_i\ln p_i = (\ln2)\,H_{\text{bits}}[p] .
> $$
>
> Since $\ln 2 > 0$, switching units cannot change which of two distributions has more entropy, nor which one maximizes it.
>
> *Source: Mao §4.2, eq. (4.8)*

^def-c4a-2-1

> [!definition] Definition §C4a.2.2: Microstates as Alternatives
> The outcomes of Shannon's problem are taken to be the complete microstates $i$, with probabilities $p_i$:
>
> $$
> H[p] = -\sum_ip_i\ln p_i .
> $$
>
> - $p_i$ encodes what the macroscopic data leave undecided; no measurement is implied.
> - Uniform weights on $\Omega$ microstates give $H = \ln\Omega$. For any $p$, the **effective number of microstates**
>
> $$
> \Omega_{\text{eff}} = e^{H[p]}
> $$
>
> is the size of the uniform distribution with the same entropy.
>
> *Model:* [[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^def-c2-1-1|Def. §C2.1.1]]; *applies:* uncertainty about the microstate given macroscopic information; knowing the microstate exactly leaves $H = 0$.
>
> *Source: Mao §4.2.1, eqs. (4.9)–(4.11) · Jaynes (1957 II), p. 171*

^def-c4a-2-2

> [!example] Example §C4a.2.1: Uncertainty of $L$ Spins
> If all $2^L$ configurations of $L$ classical Ising spins are equally likely, $H = L\ln2$ nats, or $L$ bits: one bit per spin.
>
> *Source: Mao §4.2.1*

^ex-c4a-2-1

> [!definition] Definition §C4a.2.3: Entropy of a Classical Density
> For a classical density on phase space with the measure $d\Gamma$ of [[§C3.1 Microstates and Statistical States in Parallel#^def-c3-1-3|Def. §C3.1.3]],
>
> $$
> H_{\text{cl}}[\rho_{\text{cl}}] = -\int_\Gamma d\Gamma(X)\,\rho_{\text{cl}}(X)\ln\rho_{\text{cl}}(X) ,
> $$
>
> the continuum form of $\sum_i \to \int d\Gamma$, $p_i \to \rho_{\text{cl}}$.
>
> *Source: Mao §4.2.2, eqs. (4.12)–(4.13)*

^def-c4a-2-3

> [!caution] Caution: The reference measure must be fixed
> Only $\rho_{\text{cl}}\,d\Gamma$ is a probability. Under $d\Gamma \to c\,d\Gamma$ the same probabilities require the density $\rho_{\text{cl}}/c$, and
>
> $$
> H_{\text{cl}} \to H_{\text{cl}} + \ln c ,
> $$
>
> so a value of $H_{\text{cl}}$, or a comparison of two values, means something only once $d\Gamma$ is chosen once and for all. Choosing the cell $h^f$ of [[§C3.1 Microstates and Statistical States in Parallel#^thm-c3-1-1|Theorem §C3.1.1]] makes the classical value match quantum state counting.

^cau-c4a-2-1

> [!definition] Definition §C4a.2.4: Von Neumann Entropy
> For a density operator with eigen-decomposition $\hat\rho = \sum_ip_i|i\rangle\langle i|$,
>
> $$
> H_{\text{vN}}[\hat\rho] = -\operatorname{Tr}(\hat\rho\ln\hat\rho) = -\sum_ip_i\ln p_i .
> $$
>
> The trace of a function of $\hat\rho$ is basis-free, so the second form can be evaluated in any eigenbasis, also one chosen inside a degenerate eigenspace. Full treatment in QM: [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^def-c11-2-1|QM Def. §C11.2.1]].
>
> *Source: Mao §4.2.2, eqs. (4.14)–(4.15) · QM home: [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^def-c11-2-1|QM Def. §C11.2.1]]*

^def-c4a-2-4

> [!caution] Caution: Eigenvalues, not preparation weights
> An ensemble prepared as $\sum_np_n|\psi_n\rangle\langle\psi_n|$ with non-orthogonal $|\psi_n\rangle$ has $H_{\text{vN}}$ computed from the eigenvalues of $\hat\rho$, not from the $p_n$. The two differ: for $|{\uparrow}\rangle$ and $|+\rangle$ with weights $\tfrac12, \tfrac12$, the weights give $\ln2$, while $\hat\rho$ has eigenvalues $\tfrac12(1 \pm 1/\sqrt2)$ and smaller entropy, because the two states overlap. Different preparations with the same $\hat\rho$ ([[§C3.2 The Density Operator as an Ensemble#^thm-c3-2-5|Theorem §C3.2.5]]) have the same $H_{\text{vN}}$, as they must.
>
> *Source: Jaynes (1957 II), eqs. (7.14)–(7.16), cited in Mao §4.2.2*

^cau-c4a-2-2

> [!remark]- Connections
> - Properties of $H_{\text{vN}}$ (invariance under unitaries, additivity, maximum $\ln N$) — [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-4|QM Theorem §C11.2.4]].
> - The entropy of a reduced state measures entanglement — [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^thm-c4a-8-2|Theorem §C4a.8.2]].
> - Unitary evolution keeps $H_{\text{vN}}$ fixed, because it keeps the eigenvalues ([[§C3.3 Liouville Theorems and Stationary Ensembles#^thm-c3-3-5|Theorem §C3.3.5]]); level B's coarse-graining discussion is the classical counterpart — [[§B6.3 Entropy, Information and the Gibbs Paradox#^rem-b6-3-3|Remark: Fine-grained entropy does not grow; coarse-grained entropy does]].
