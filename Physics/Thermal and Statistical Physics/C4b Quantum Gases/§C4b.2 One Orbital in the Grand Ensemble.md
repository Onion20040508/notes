---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.2
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.1 Orbitals and Occupations]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.3 Summing over Orbitals: the Density of States]] →

*Sources: Mao, PHY 510 notes, §4.5.3, eqs. (4.100)–(4.108) and Figure 4.1 · PHY 510 Lecture 10/6.*

The grand-canonical weight ([[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]) of a noninteracting occupation list is a product of one factor per orbital. So the occupation of a single orbital has its own distribution, obtained by summing out all the others, and that distribution depends only on $\epsilon_\ell$, $T$ and $\mu$. Its mean is the Bose–Einstein or Fermi–Dirac occupation. Level B derives the same distributions ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-3|Theorem §B10.1.3]]); here they come with their limits and their fluctuations.

**Setup.** Noninteracting orbitals with energies $\epsilon_\ell$; an occupation list $\{n_\ell\}$ has energy $\sum_\ell n_\ell\epsilon_\ell$ and particle number $\sum_\ell n_\ell$; grand ensemble at $T$, $\mu$. Fix one orbital $\ell$ and write $n$ for its occupation.

> [!theorem] Theorem §C4b.2.1: Grand-Canonical Statistics of One Orbital
> The probability that orbital $\ell$ holds $n$ particles is
>
> $$
> P_\ell(n) = \frac{e^{-\beta n(\epsilon_\ell - \mu)}}{\Xi_\ell}, \qquad \Xi_\ell = \sum_{n\ \text{allowed}}e^{-\beta n(\epsilon_\ell - \mu)}, \qquad \langle n_\ell\rangle = \frac1\beta\frac{\partial\ln\Xi_\ell}{\partial\mu} .
> $$
>
> 1. **Bosons**, $n = 0, 1, 2, \dots$: $\Xi_\ell^B = \dfrac{1}{1 - e^{-\beta(\epsilon_\ell - \mu)}}$ and $\langle n_\ell\rangle_B = \dfrac{1}{e^{\beta(\epsilon_\ell - \mu)} - 1}$, provided $\mu < \epsilon_\ell$.
> 2. **Fermions**, $n = 0, 1$: $\Xi_\ell^F = 1 + e^{-\beta(\epsilon_\ell - \mu)}$ and $\langle n_\ell\rangle_F = \dfrac{1}{e^{\beta(\epsilon_\ell - \mu)} + 1}$, for any $\mu$.
>
> For bosons the condition must hold for every orbital, so $\mu < \epsilon_0$, the lowest one-particle energy.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]] for the Setup; *applies:* noninteracting particles, for which $P_\ell$ is a marginal of a product distribution (Step 1; the full product is [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]]).
>
> *Source: Mao §4.5.3, eqs. (4.100)–(4.105) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-3|Theorem §B10.1.3]]*

^thm-c4b-2-1

> [!derivation]- Derivation
> **Step 1** (marginal). [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]] weights the list $\{n_k\}$ by $e^{-\beta\sum_k n_k(\epsilon_k - \mu)} = \prod_k e^{-\beta n_k(\epsilon_k - \mu)}$. Summing over all $n_k$ with $k \ne \ell$, each over its own allowed values, gives the same constant factor $\prod_{k\ne\ell}\Xi_k$ for every value of $n_\ell = n$. Hence $P_\ell(n) \propto e^{-\beta n(\epsilon_\ell - \mu)}$, and normalizing over $n$ gives $\Xi_\ell$.
>
> **Step 2** (bosons). With $u = e^{-\beta(\epsilon_\ell - \mu)}$, $\Xi^B = \sum_{n\ge0}u^n = 1/(1 - u)$ for $u < 1$, that is $\mu < \epsilon_\ell$. Then $\langle n\rangle = u\,\partial_u\ln\Xi^B = u/(1 - u) = 1/(u^{-1} - 1)$. ($\partial_\mu$ at fixed $T$ acts as $\beta u\,\partial_u$.)
>
> **Step 3** (fermions). $\Xi^F = 1 + u$, finite for all $u$, and $\langle n\rangle = u/(1 + u) = 1/(u^{-1} + 1)$.

^der-c4b-2-1

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]

> [!definition] Definition §C4b.2.1: Mean Occupation Function
> $$
> f(\epsilon) = \frac{1}{e^{\beta(\epsilon - \mu)} \mp 1} ,
> $$
>
> upper sign bosons, lower sign fermions, so that $f(\epsilon_\ell) = \langle n_\ell\rangle$ ([[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]). Then:
>
> - $\sum_\ell f(\epsilon_\ell) = \bar N$, not $1$;
> - fermions: $f_F(\epsilon_\ell) = P_\ell(1) \in (0, 1)$, with $f_F(\mu) = \tfrac12$;
> - bosons: $f_B \in (0, \infty)$ for $\epsilon > \mu$.
>
> *Source: Mao §4.5.3, eq. (4.106)*

^def-c4b-2-1

> [!theorem] Theorem §C4b.2.2: Two Different Classical Limits
> With $y = \beta(\epsilon - \mu)$:
>
> 1. **Dilute particles**, $y \gg 1$: $f_B \simeq f_F \simeq e^{-y} \ll 1$, the Maxwell–Boltzmann form; double occupation has relative weight $P_\ell(2)/P_\ell(1) = e^{-y}$ for bosons and is forbidden for fermions.
> 2. **Classical waves** (bosons with $\mu = 0$), $0 < y \ll 1$: $f_B \simeq 1/y \gg 1$, so $\epsilon f_B \simeq k_BT$, the mean thermal energy of one mode (the Rayleigh–Jeans input of [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-3|Theorem §C4b.6.3]]).
>
> Part 1 describes classical particles, part 2 classical fields.
>
> *Model:* [[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]]; *applies:* part 1 for the whole spectrum needs $y \gg 1$ already at the lowest orbital, i.e. $z \ll 1$ ([[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]]).
>
> *Source: Mao §4.5.3, eq. (4.107) · level-B home of part 1: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-4|Theorem §B10.1.4]]*

^thm-c4b-2-2

> [!derivation]- Derivation
> **Part 1.** For $y \gg 1$, $e^y \mp 1 = e^y(1 \mp e^{-y}) \simeq e^y$. The ratio $P_\ell(2)/P_\ell(1) = e^{-y}$ is read off [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]].
>
> **Part 2.** For $y \ll 1$, $e^y - 1 = y + O(y^2)$, so $f_B = 1/y + O(1)$; with $\mu = 0$, $y = \beta\epsilon$ and $\epsilon f_B \simeq \epsilon/(\beta\epsilon) = k_BT$.

^der-c4b-2-2

> [!theorem] Theorem §C4b.2.3: Occupation Fluctuations
> $$
> \operatorname{Var}(n_\ell) = k_BT\frac{\partial\langle n_\ell\rangle}{\partial\mu} = \begin{cases}\langle n_\ell\rangle(1 + \langle n_\ell\rangle), & \text{bosons},\\ \langle n_\ell\rangle(1 - \langle n_\ell\rangle), & \text{fermions},\end{cases}
> $$
>
> so $\operatorname{Var}(n_\ell)/\langle n_\ell\rangle = 1 \pm \langle n_\ell\rangle$, against the Poisson value $1$.
>
> *Model:* [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]; *applies:* exact.
>
> *Source: Mao §4.5.3, eq. (4.108) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-3|Theorem §B10.1.3]]*

^thm-c4b-2-3

> [!derivation]- Derivation
> **Step 1.** [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-3|Theorem §C4a.10.3]] for one orbital: $\operatorname{Var}(n) = k_BT\,\partial_\mu\langle n\rangle$.
>
> **Step 2.** With $f = (e^y \mp 1)^{-1}$ and $\partial_\mu y = -\beta$, $\partial_\mu f = \beta e^y/(e^y \mp 1)^2$. Since $e^y = 1/f \pm 1$, this is $\beta f^2(1/f \pm 1) = \beta f(1 \pm f)$.

^der-c4b-2-3

*Uses:* [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-3|Theorem §C4a.10.3]], [[§C4b.2 One Orbital in the Grand Ensemble#^def-c4b-2-1|Def. §C4b.2.1]]

![[ph-th-c4b-2-1.svg]]

*Figure: Bose–Einstein and Fermi–Dirac occupations against $(\epsilon - \mu)/k_BT$, with the Maxwell–Boltzmann form $e^{-(\epsilon - \mu)/k_BT}$ dashed. The Bose curve diverges as $\epsilon \to \mu^+$, the Fermi curve passes through $\tfrac12$ at $\epsilon = \mu$, and all three meet in the tail ([[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-2|Theorem §C4b.2.2]]).*

> [!remark]- Connections
> - The Fermi–Dirac form already appeared for adsorption sites, each a single orbital that holds at most one particle — [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-4|Example §C4a.11.4]].
> - Large bosonic fluctuations, $\operatorname{Var}(n) \simeq n^2$, are the photon bunching of thermal light (QM level, not in these notes).
