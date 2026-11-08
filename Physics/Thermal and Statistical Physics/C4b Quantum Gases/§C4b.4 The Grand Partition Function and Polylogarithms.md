---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.4
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.3 Summing over Orbitals: the Density of States]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.5 Massive Gases and the Classical Limit]] →

*Sources: Mao, PHY 510 notes, §4.5.5, eqs. (4.120)–(4.130), boxes "Three useful functions", "One grand partition function generates the gas thermodynamics" and Figure 4.2 · NIST DLMF §25.12 (cited by Mao) · Kardar, Statistical Physics of Particles, §7.3–§7.6 (Mao's suggested reading) · PHY 510 Lecture 10/6 · PHY 510 Problem Set 6, part (c), official solution.*

Instead of three separate integrals for $N$, $U$ and $p$, evaluate one function, $\ln\Xi$, and take derivatives. For a density of states $g(\epsilon) = A\epsilon^{\nu-1}$ the integral is a standard special function, the polylogarithm, and the derivatives only shift its order. Level B introduces the same functions ([[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]], [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-1|Theorem §B10.2.1]]); here they come out of $\ln\Xi$ with the endpoint and asymptotic facts the later sections need.

**Setup.** $g(\epsilon) = A\epsilon^{\nu-1}$ with $A \propto V$, which covers $\nu = 3/2$ ($\epsilon \propto k^2$) and $\nu = 3$ ($\epsilon \propto k$) in three dimensions; lowest energy $0$; $x = \beta\epsilon$, $z = e^{\beta\mu}$; physical ranges $0 < z < 1$ (bosons) and $z > 0$ (fermions). Upper signs Bose, lower Fermi.

> [!definition] Definition §C4b.4.1: Gamma, Zeta and Polylogarithm
> $$
> \Gamma(q) = \int_0^\infty x^{q-1}e^{-x}\,dx, \qquad \zeta(q) = \sum_{j\ge1}\frac1{j^q}\ (q > 1), \qquad \operatorname{Li}_q(w) = \frac{1}{\Gamma(q)}\int_0^\infty\frac{w\,x^{q-1}}{e^x - w}\,dx\ (q > 0,\ w < 1) .
> $$
>
> For $|w| < 1$, $\operatorname{Li}_q(w) = \sum_{j\ge1}w^j/j^q$; $\operatorname{Li}_1(w) = -\ln(1 - w)$; the endpoint $\operatorname{Li}_q(1) = \zeta(q)$ exists for $q > 1$. For both statistics write
>
> $$
> G_q(z) \equiv \begin{cases}\operatorname{Li}_q(z), & \text{bosons},\\ -\operatorname{Li}_q(-z), & \text{fermions}.\end{cases}
> $$
>
> $\Gamma(q + 1) = q\Gamma(q)$, $\Gamma(n + 1) = n!$, $\Gamma(\tfrac12) = \sqrt\pi$, $\Gamma(\tfrac32) = \tfrac{\sqrt\pi}2$, $\Gamma(\tfrac52) = \tfrac{3\sqrt\pi}4$.
>
> *Source: Mao §4.5.5, eqs. (4.122)–(4.123), box "Three useful functions: Γ, ζ, and Li" · DLMF §5.2, §25.2, §25.12 · level-B home: [[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]], Gamma: [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|Def. §B4.1.5]]*

^def-c4b-4-1

> [!theorem] Theorem §C4b.4.1: $\ln\Xi$ Is a Polylogarithm
> $$
> \ln\Xi_{\text{cont}} = \mp A\beta^{-\nu}\int_0^\infty x^{\nu-1}\ln(1 \mp ze^{-x})\,dx = A\,\Gamma(\nu)\,\beta^{-\nu}\,G_{\nu+1}(z) .
> $$
>
> *Model:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]] with $g = A\epsilon^{\nu-1}$; *applies:* $\nu > 0$, physical $z$; at the Bose endpoint $z = 1$ when $\nu + 1 > 1$.
>
> *Source: Mao §4.5.5, eqs. (4.120)–(4.121) and the display after (4.122)*

^thm-c4b-4-1

> [!derivation]- Derivation
> **Step 1** (substitute). $\ln\Xi = \mp\int g(\epsilon)\ln(1 \mp ze^{-\beta\epsilon})\,d\epsilon$ ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]); with $\epsilon = x/\beta$, $g\,d\epsilon = A\beta^{-\nu}x^{\nu-1}dx$.
>
> **Step 2** (by parts). Take $u = \mp\ln(1 \mp ze^{-x})$, $dv = x^{\nu-1}dx$, so $v = x^\nu/\nu$ and $du = -dx/(z^{-1}e^x \mp 1)$. Then
>
> $$
> \mp\int_0^\infty x^{\nu-1}\ln(1 \mp ze^{-x})\,dx = \Bigl[\mp\frac{x^\nu}\nu\ln(1 \mp ze^{-x})\Bigr]_0^\infty + \frac1\nu\int_0^\infty\frac{x^\nu\,dx}{z^{-1}e^x \mp 1} .
> $$
>
> **Step 3** (boundary). At $\infty$ the logarithm decays like $e^{-x}$. At $0$ it is finite for $z < 1$; at the Bose endpoint it behaves like $\ln x$, and $x^\nu\ln x \to 0$ for $\nu > 0$. So the bracket vanishes.
>
> **Step 4** (identify). $\int_0^\infty\frac{x^\nu\,dx}{z^{-1}e^x \mp 1} = \Gamma(\nu + 1)G_{\nu+1}(z)$ by [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]] (for fermions, $w = -z$ and an overall sign), and $\Gamma(\nu + 1)/\nu = \Gamma(\nu)$.

^der-c4b-4-1

*Uses:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]

> [!theorem] Theorem §C4b.4.2: Three Facts about $G_q$
> 1. **Differentiation lowers the order:** $z\,\partial_zG_q(z) = G_{q-1}(z)$, in the physical domains (a derivative can diverge at the Bose endpoint while the function is finite).
> 2. **Dilute gases:** $G_q(z) = z \pm z^2/2^q + O(z^3)$. The common first term is Maxwell–Boltzmann; the second is the first exchange correction.
> 3. **Bose endpoint:** for $q > 1$, $G_q(1) = \zeta(q)$, with
>
> $$
> \zeta(\tfrac32) \simeq 2.612, \qquad \zeta(\tfrac52) \simeq 1.341, \qquad \zeta(3) \simeq 1.202, \qquad \zeta(4) = \frac{\pi^4}{90} .
> $$
>
> Near it, with $\alpha = -\ln z \to 0^+$: $G_{3/2}(e^{-\alpha}) = \zeta(\tfrac32) - 2\sqrt\pi\,\alpha^{1/2} + O(\alpha)$ and $G_{1/2}(e^{-\alpha}) \sim \sqrt{\pi/\alpha}$. The $\alpha^{1/2}$ term means there is no Taylor expansion about $z = 1$.
>
> For bosons $z$ never exceeds $1$: once the excited states are saturated the excess goes into the condensate.
>
> *Model:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]; *applies:* as stated.
>
> *Source: Mao §4.5.5, eqs. (4.124)–(4.127) · DLMF §25.12 · level-B home of part 3: [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-1|Theorem §B10.2.1]]*

^thm-c4b-4-2

> [!derivation]- Derivation
> **Part 1.** Termwise on the series, $z\partial_z\sum_jz^j/j^q = \sum_jz^j/j^{q-1}$; analytic continuation carries it to the whole physical domain. For fermions, $z\partial_z[-\operatorname{Li}_q(-z)] = -\operatorname{Li}_{q-1}(-z)$ in the same way.
>
> **Part 2.** The first two terms of the series, $w + w^2/2^q$, with $w = z$ for bosons and $-[(-z) + z^2/2^q] = z - z^2/2^q$ for fermions.
>
> **Part 3.** $\operatorname{Li}_q(1) = \sum_jj^{-q} = \zeta(q)$, convergent for $q > 1$. The endpoint forms are DLMF §25.12 (as cited by Mao): the $\alpha^{1/2}$ comes from the small-$x$ region of the integral, where $1/(e^{x+\alpha} - 1) \simeq 1/(x + \alpha)$ and $\int_0^\infty x^{1/2}[\frac1{x+\alpha} - \frac1x]dx = -\pi\sqrt\alpha$, divided by $\Gamma(\tfrac32) = \sqrt\pi/2$.

^der-c4b-4-2

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]

> [!theorem] Theorem §C4b.4.3: One Function Gives $N$, $U$ and $p$
> With $\beta$, $z$, $V$ independent and $A \propto V$,
>
> $$
> N_{\text{cont}} = z\Bigl(\frac{\partial\ln\Xi}{\partial z}\Bigr)_{\beta,V} = A\Gamma(\nu)\beta^{-\nu}G_\nu(z), \qquad U = -\Bigl(\frac{\partial\ln\Xi}{\partial\beta}\Bigr)_{z,V} = \nu A\Gamma(\nu)\beta^{-(\nu+1)}G_{\nu+1}(z),
> $$
>
> $$
> p = \frac1\beta\Bigl(\frac{\partial\ln\Xi}{\partial V}\Bigr)_{\beta,z} = \frac AV\Gamma(\nu)\beta^{-(\nu+1)}G_{\nu+1}(z) ,
> $$
>
> hence, at any degeneracy,
>
> $$
> U = \nu\,pV, \qquad \Phi = -k_BT\ln\Xi = -pV .
> $$
>
> In three dimensions: $\nu = \tfrac32$ (orders $\tfrac32$ for $N$, $\tfrac52$ for $\ln\Xi$, $U$, $p$) for $\epsilon \propto k^2$; $\nu = 3$ (orders $3$ and $4$) for $\epsilon \propto k$. A Bose condensate adds $N_0$ to $N$ and nothing to $U$ or $p$.
>
> *Model:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-1|Theorem §C4b.4.1]]; *applies:* bulk continuum thermodynamics.
>
> *Source: Mao §4.5.5, eqs. (4.128)–(4.130), box "One grand partition function generates the gas thermodynamics" · PHY 510 Problem Set 6, part (c), official solution · level-B home: [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-3|Theorem §B10.2.3]]*

^thm-c4b-4-3

> [!derivation]- Derivation
> **Step 1** (why these derivatives). In $\Xi = \sum_iz^{N_i}e^{-\beta E_i(V)}$, $z\partial_z$ brings down $N_i$ and $-\partial_\beta$ at fixed $z$ brings down $E_i$; dividing by $\Xi$ gives means. The pressure is $p = -(\partial\Phi/\partial V)_{T,\mu}$ ([[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]]), and fixed $T$, $\mu$ is fixed $\beta$, $z$.
>
> **Step 2.** Apply to $\ln\Xi = A\Gamma(\nu)\beta^{-\nu}G_{\nu+1}(z)$: $z\partial_z$ lowers the order ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 1); $-\partial_\beta\beta^{-\nu} = \nu\beta^{-\nu-1}$; $\partial_VA = A/V$.
>
> **Step 3.** Comparing, $U = \nu\cdot(pV)$ and $\ln\Xi = \beta pV$, so $\Phi = -pV$.

^der-c4b-4-3

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-1|Theorem §C4b.4.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]]

> [!example] Example §C4b.4.1: Which Regime, Which Expansion
> At fixed density, with the lowest energy at $0$:
>
> | regime | $\mu$ | $z$ and method |
> | --- | --- | --- |
> | high-$T$ dilute gas | $\mu/k_BT \ll -1$ | $z \ll 1$: small-$z$ series ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 2) |
> | low-$T$ Bose gas in 3D | $\mu \to 0^-$, pinned at $0$ when condensed | $z \to 1^-$: endpoint ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 3) |
> | low-$T$ Fermi gas | $\mu \to E_F > 0$ | $\ln z = \mu/k_BT \gg 1$: Sommerfeld ([[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]]) |
> | black-body photons | $\mu = 0$ always | $z = 1$ at every $T$ |
>
> In between, solve the number equation for $z$ numerically ($N$ increases with $z$) and insert it in the other formulas. Taking $T \to \infty$ at fixed $\mu$ is not the fixed-density classical limit.
>
> *Source: Mao §4.5.5, Figure 4.2 and the table of limits*

^ex-c4b-4-1

> [!remark]- Connections
> - The orders and the relation $U = \nu pV$ in any dimension and for any power-law dispersion — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]].
> - $U = \tfrac32pV$ for nonrelativistic and $U = 3pV$ for ultrarelativistic gases, whatever the statistics — [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-3|Theorem §B10.2.3]].
