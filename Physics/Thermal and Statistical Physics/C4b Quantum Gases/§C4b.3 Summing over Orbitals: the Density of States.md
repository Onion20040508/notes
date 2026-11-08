---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.3
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.2 One Orbital in the Grand Ensemble]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.4 The Grand Partition Function and Polylogarithms]] →

*Sources: Mao, PHY 510 notes, §4.5.4, eqs. (4.109)–(4.119) · PHY 510 Lecture 10/6 · PHY 510 Problem Set 6, part (b), official solution.*

With each orbital solved, the gas follows by combining them. In the grand ensemble the orbitals are statistically independent, so the partition function is a product and its logarithm a sum; for a large box the sum over orbitals becomes an integral over a density of states. The geometric count of orbitals is universal, and the dispersion enters only through a Jacobian. Level B states the density of states for a three-dimensional box ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-2|Def. §B10.1.2]], [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]); here it is done for any dispersion.

**Setup.** Noninteracting orbitals $\ell$ with energies $\epsilon_\ell$, $\hat H = \sum_\ell\epsilon_\ell\hat n_\ell$, $\hat N = \sum_\ell\hat n_\ell$ ([[§C3.5 Many-Particle States#^mod-c3-5-5|Model §C3.5.5]]); the box modes of [[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]] with $g_s$ internal states. Fugacity $z = e^{\beta\mu}$. In grand-canonical formulas $N$ means the mean particle number.

> [!theorem] Theorem §C4b.3.1: The Grand Partition Function Factorizes over Orbitals
> $$
> P(\{n_\ell\}) = \prod_\ell P_\ell(n_\ell), \qquad \Xi = \prod_\ell\Xi_\ell ,
> $$
>
> $$
> \ln\Xi_B = -\sum_\ell\ln\bigl(1 - ze^{-\beta\epsilon_\ell}\bigr), \qquad \ln\Xi_F = \sum_\ell\ln\bigl(1 + ze^{-\beta\epsilon_\ell}\bigr) ,
> $$
>
> $$
> N = \sum_\ell f(\epsilon_\ell), \qquad U = \sum_\ell\epsilon_\ell f(\epsilon_\ell) .
> $$
>
> No factor $1/N!$ appears: each allowed list $\{n_\ell\}$ already is one symmetrized or antisymmetrized state. A prescribed $N$ is imposed by choosing $\mu$ so that the first sum has that value.
>
> *Model:* [[§C3.5 Many-Particle States#^mod-c3-5-5|Model §C3.5.5]] in [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* exact.
>
> *Source: Mao §4.5.4, eqs. (4.110)–(4.114) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-2|Theorem §B10.1.2]]*

^thm-c4b-3-1

> [!derivation]- Derivation
> **Step 1.** The weight of $\{n_\ell\}$ is $e^{-\beta\sum_\ell(\epsilon_\ell - \mu)n_\ell} = \prod_\ell e^{-\beta(\epsilon_\ell - \mu)n_\ell}$.
>
> **Step 2.** In the grand ensemble nothing fixes $\sum_\ell n_\ell$, so each $n_\ell$ is summed over its allowed values independently, and the sum of products is the product of sums: $\Xi = \prod_\ell\Xi_\ell$. Dividing the weight by $\Xi$ gives the product of the $P_\ell$.
>
> **Step 3.** Take the logarithm and use [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]. Means of sums are sums of means.

^der-c4b-3-1

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]

> [!caution] Caution: Why not the canonical ensemble
> Fixing $\sum_\ell n_\ell = N$ in every microstate couples all occupation sums, and the product of [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]] is lost. The grand ensemble trades that exact constraint for a condition on the mean, which is what makes ideal quantum gases solvable.

^cau-c4b-3-1

> [!theorem] Theorem §C4b.3.2: Counting Orbitals; the One-Particle Density of States
> Each allowed $\mathbf k$ occupies a cell of volume $(2\pi)^3/V$, so for a large box
>
> $$
> \sum_\ell(\cdots) \longrightarrow \frac{g_sV}{(2\pi)^3}\int d^3k\,(\cdots), \qquad g(k)\,dk = \frac{g_sV}{2\pi^2}k^2\,dk .
> $$
>
> For an isotropic, increasing dispersion $\epsilon(k)$ the **one-particle density of states** is
>
> $$
> g(\epsilon) = g(k)\frac{dk}{d\epsilon} = \frac{g_sV}{2\pi^2}k^2\frac{dk}{d\epsilon} ,
> $$
>
> with dimensions of inverse energy. The factor $4\pi k^2$ is pure geometry; the dispersion enters only through $dk/d\epsilon$.
>
> *Model:* [[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]]; *applies:* $L$ large compared with the relevant wavelengths; for several branches, sum their densities.
>
> *Source: Mao §4.5.4, eqs. (4.115)–(4.116) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]*

^thm-c4b-3-2

> [!derivation]- Derivation
> **Step 1.** The allowed $\mathbf k$ form a cubic lattice of spacing $2\pi/L$ ([[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]]), one point per volume $(2\pi/L)^3 = (2\pi)^3/V$, times $g_s$ internal states.
>
> **Step 2.** A spherical shell $[k, k + dk]$ has volume $4\pi k^2dk$, so it holds $g_sV\,4\pi k^2dk/(2\pi)^3 = g_sVk^2dk/(2\pi^2)$ orbitals.
>
> **Step 3.** Orbitals in $[\epsilon, \epsilon + d\epsilon]$ are those in the corresponding shell: $g(\epsilon)\,d\epsilon = g(k)\,dk$.

^der-c4b-3-2

*Uses:* [[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]]

> [!theorem] Theorem §C4b.3.3: Two Dispersions
> 1. **Nonrelativistic**, $\epsilon = \hbar^2k^2/(2m)$:
>
> $$
> g(\epsilon) = \frac{g_sV}{4\pi^2}\Bigl(\frac{2m}{\hbar^2}\Bigr)^{3/2}\epsilon^{1/2} .
> $$
>
> 2. **Ultrarelativistic or massless**, $\epsilon = \hbar ck$:
>
> $$
> g(\epsilon) = \frac{g_sV}{2\pi^2\hbar^3c^3}\epsilon^2 .
> $$
>
> The change from $\sqrt\epsilon$ to $\epsilon^2$ comes from the dispersion alone, not from the statistics.
>
> *Model:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]; *applies:* part 1 for $p \ll mc$, part 2 for $p \gg mc$ (exact for massless particles).
>
> *Source: Mao §4.5.4, eqs. (4.117)–(4.118)*

^thm-c4b-3-3

> [!derivation]- Derivation
> **Part 1.** $k = \sqrt{2m\epsilon}/\hbar$ and $dk/d\epsilon = m/(\hbar^2k)$, so $k^2\,dk/d\epsilon = mk/\hbar^2 = \frac{m}{\hbar^2}\frac{\sqrt{2m\epsilon}}{\hbar} = \frac12\bigl(\frac{2m}{\hbar^2}\bigr)^{3/2}\epsilon^{1/2}$. Multiply by $g_sV/(2\pi^2)$.
>
> **Part 2.** $k = \epsilon/(\hbar c)$ and $dk/d\epsilon = 1/(\hbar c)$, so $k^2\,dk/d\epsilon = \epsilon^2/(\hbar c)^3$.

^der-c4b-3-3

*Uses:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

> [!theorem] Theorem §C4b.3.4: Continuum Formulas, with the Ground State Kept Aside
> $$
> N_{\text{cont}} = \int_0^\infty g(\epsilon)f(\epsilon)\,d\epsilon, \qquad U_{\text{cont}} = \int_0^\infty\epsilon\,g(\epsilon)f(\epsilon)\,d\epsilon ,
> $$
>
> and $\ln\Xi$ is the integral of $\ln\Xi_\ell$ against $g(\epsilon)$. These describe the dense set of excited orbitals. An isolated orbital whose occupation becomes macroscopic must be kept separately: for a Bose condensate in a zero-energy ground state, $N = N_0 + N_{\text{cont}}$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]]).
>
> *Model:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]; *applies:* large box; the continuum gives no weight to a single orbital.
>
> *Source: Mao §4.5.4, eq. (4.119)*

^thm-c4b-3-4

> [!derivation]- Derivation
> Group the orbitals of [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]] by energy using [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]: a smooth function $F(\epsilon_\ell)$ summed over orbitals becomes $\int F(\epsilon)g(\epsilon)\,d\epsilon$ when $F$ varies little between neighbouring levels. A single orbital carries weight $g(\epsilon)\,d\epsilon \to 0$ in the integral, so a macroscopic $f(\epsilon_0)$ at the lowest level is lost and must be added by hand.

^der-c4b-3-4

*Uses:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

> [!remark]- Connections
> - The same counting in $d$ dimensions, with a sphere area $S_{d-1}$, gives $g(\epsilon) = A\epsilon^{\nu-1}$ with $\nu = d/s$ for $\epsilon \propto k^s$ — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]].
> - The density of states here counts one-particle orbitals; the many-body $g(E)$ of [[§C4a.9★ Density of States, Laplace and Legendre#^def-c4a-9-1|Def. §C4a.9.1]] counts whole microstates.
