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

*Sources: Mao, PHY 510 notes, §4.5.4, eqs. (4.109)–(4.119) · PHY 510 Lecture 10/6.*

The whole gas is assembled from the one-orbital results of [[§C4b.2 One Orbital in the Grand Ensemble|§C4b.2]] in two moves. First, the grand partition function is a product over orbitals, so $\ln\Xi$, $N$ and $U$ are sums over orbitals. Second, in a large box those sums become integrals over energy weighted by the number of orbitals per unit energy. Only the second move depends on the dispersion $\epsilon(k)$, and only through $dk/d\epsilon$. Level B states the density of states for a three-dimensional box ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-2|Def. §B10.1.2]], [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-5|Theorem §B10.1.5]]); here it is done for any dispersion.

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
> At fixed $T$, $V$ and given $N$, the chemical potential $\mu(T, V, N)$ is the root of the first sum. The sums run over occupation lists, which label the symmetrized or antisymmetrized states one-to-one ([[§C3.5 Many-Particle States#^def-c3-5-3|Def. §C3.5.3]]), so no $1/N!$ is needed.
>
> *Model:* [[§C3.5 Many-Particle States#^mod-c3-5-5|Model §C3.5.5]] in [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* exact; for bosons $\mu < \epsilon_0$, the lowest orbital energy, so that every $\Xi_\ell$ converges ([[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]).
>
> *Source: Mao §4.5.4, eqs. (4.110)–(4.114) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-2|Theorem §B10.1.2]]*

^thm-c4b-3-1

> [!derivation]- Derivation
> **Step 1.** The weight of $\{n_\ell\}$ is $e^{-\beta\sum_\ell(\epsilon_\ell - \mu)n_\ell} = \prod_\ell e^{-\beta(\epsilon_\ell - \mu)n_\ell}$.
>
> **Step 2.** In the grand ensemble nothing fixes $\sum_\ell n_\ell$, so each $n_\ell$ is summed over its allowed values independently, and the sum of products is the product of sums: $\Xi = \prod_\ell\Xi_\ell$. Dividing the weight by $\Xi$ gives the product of the $P_\ell$.
>
> **Step 3.** Take the logarithm and use [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]. Means of sums are sums of means.
>
> **Step 4** ($\mu$). $N = \sum_\ell f(\epsilon_\ell)$ increases strictly with $\mu$ (each $\partial_\mu f = \beta f(1 \pm f) > 0$, [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-3|Theorem §C4b.2.3]]), so the root is unique.

^der-c4b-3-1

*Uses:* [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-3|Theorem §C4b.2.3]]

> [!caution] Caution: Why not the canonical ensemble
> The canonical sum is the $z^N$ coefficient of the grand one:
>
> $$
> Z_N = \sum_{\{n_\ell\}:\ \sum_\ell n_\ell = N}\ \prod_\ell e^{-\beta n_\ell\epsilon_\ell} = \oint\frac{dz}{2\pi i\,z^{N+1}}\,\Xi(z) .
> $$
>
> The constraint ties every $n_\ell$ to every other, and recovering $Z_N$ from the product $\Xi = \prod_\ell\Xi_\ell$ takes a contour integral; the grand ensemble works with $\Xi$ itself and fixes only the mean $N$.

^cau-c4b-3-1

> [!definition] Definition §C4b.3.1: One-Particle Density of States
> The **one-particle density of states** $g(\epsilon)$ is defined by: $g(\epsilon)\,d\epsilon$ is the number of orbitals with energy in $[\epsilon, \epsilon + d\epsilon]$. Its units are inverse energy.
>
> *Source: Mao §4.5.4, eq. (4.116) · level-B home: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-2|Def. §B10.1.2]]*

^def-c4b-3-1

> [!theorem] Theorem §C4b.3.2: Counting Orbitals; the One-Particle Density of States
> Each allowed $\mathbf k$ occupies a cell of volume $(2\pi)^3/V$, so for a large box
>
> $$
> \sum_\ell(\cdots) \longrightarrow \frac{g_sV}{(2\pi)^3}\int d^3k\,(\cdots), \qquad g(k)\,dk = \frac{g_sV}{2\pi^2}k^2\,dk .
> $$
>
> For an isotropic, increasing dispersion $\epsilon(k)$ the density of states of [[§C4b.3 Summing over Orbitals: the Density of States#^def-c4b-3-1|Def. §C4b.3.1]] is
>
> $$
> g(\epsilon) = g(k)\frac{dk}{d\epsilon} = \frac{g_sV}{2\pi^2}k^2\frac{dk}{d\epsilon} .
> $$
>
> *Model:* [[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]]; *applies:* $L$ large compared with the relevant wavelengths; internal states with a common dispersion ([[§C4b.1 Orbitals and Occupations#^cau-c4b-1-1|§C4b.1, Caution: Do not mix up which orbital with how many]]); with several branches $g$ is a sum of such terms, one per branch.
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

*Uses:* [[§C4b.1 Orbitals and Occupations#^thm-c4b-1-1|Theorem §C4b.1.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^def-c4b-3-1|Def. §C4b.3.1]]

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
> *Model:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]; *applies:* either statistics; part 1 for $p \ll mc$, part 2 for $p \gg mc$ (exact for massless particles).
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
> and $\ln\Xi$ is the integral of $\ln\Xi_\ell$ against $g(\epsilon)$. If one orbital $\ell_0$ carries a finite fraction of the particles, $f(\epsilon_{\ell_0})/N \not\to 0$, it is added by hand: $N = f(\epsilon_{\ell_0}) + N_{\text{cont}}$, the Bose condensate case $N = N_0 + N_{\text{cont}}$ of [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]].
>
> *Model:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]; *applies:* large box, and $\max_\ell f(\epsilon_\ell)/N \to 0$ for the orbitals left in the integral.
>
> *Source: Mao §4.5.4, eq. (4.119)*

^thm-c4b-3-4

> [!derivation]- Derivation
> Group the orbitals of [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]] by energy using [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]: $\sum_\ell F(\epsilon_\ell)$ is a Riemann sum for $\int F(\epsilon)g(\epsilon)\,d\epsilon$, accurate when $F$ changes little over the level spacing near the bottom of the spectrum, $\sim(2\pi\hbar)^2/(2mL^2)$ for massive particles. Any single orbital enters the integral with weight $g(\epsilon)\,d\epsilon \to 0$, so an orbital holding a finite fraction of $N$ is lost and must be added separately.

^der-c4b-3-4

*Uses:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]]

> [!remark]- Connections
> - The same counting in $d$ dimensions, with a sphere area $S_{d-1}$, gives $g(\epsilon) = A\epsilon^{\nu-1}$ with $\nu = d/s$ for $\epsilon \propto k^s$ — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]] (PHY 510 Problem Set 6, part (b)).
> - Contrast: [[§C4b.3 Summing over Orbitals: the Density of States#^def-c4b-3-1|Def. §C4b.3.1]] counts one-particle orbitals per unit energy, while the many-body $g(E)$ of [[§C4a.9★ Density of States, Laplace and Legendre#^def-c4a-9-1|Def. §C4a.9.1]] counts complete microstates of the whole system per unit energy.
