---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.4
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.3 Summing over Orbitals꞉ the Density of States]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.5 Massive Gases and the Classical Limit]] →

*Sources: Mao, PHY 510 notes, §4.5.5, eqs. (4.120)–(4.130), boxes "Three useful functions", "One grand partition function generates the gas thermodynamics" and Figure 4.2 · NIST DLMF §25.12 (cited by Mao) · Kardar, Statistical Physics of Particles, §7.3–§7.6 (Mao's suggested reading) · PHY 510 Lecture 10/6 · PHY 510 Problem Set 6, part (c), official solution.*

$\ln\Xi$ is a function of $(\beta, z, V)$, and $N$, $U$ and $p$ are its three first derivatives. So one integral suffices. For a power-law density of states $g(\epsilon) = A\epsilon^{\nu-1}$ that integral is a polylogarithm of order $\nu + 1$, and each derivative in $z$ lowers the order by one. Level B introduces the same functions ([[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]], [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-1|Theorem §B10.2.1]]); here they come out of $\ln\Xi$ with the endpoint and asymptotic facts the later sections need.

**Setup.** $g(\epsilon) = A\epsilon^{\nu-1}$ with $A \propto V$, which covers $\nu = 3/2$ ($\epsilon \propto k^2$) and $\nu = 3$ ($\epsilon \propto k$) in three dimensions; lowest energy $0$; $x = \beta\epsilon$, $z = e^{\beta\mu}$; physical ranges $0 < z < 1$ (bosons) and $z > 0$ (fermions). Upper signs Bose, lower Fermi.

> [!definition] Definition §C4b.4.1: Gamma Function
> $$
> \Gamma(q) = \int_0^\infty x^{q-1}e^{-x}\,dx, \qquad q > 0 .
> $$
>
> Used below: $\Gamma(q + 1) = q\Gamma(q)$, $\Gamma(n + 1) = n!$, $\Gamma(\tfrac12) = \sqrt\pi$, $\Gamma(\tfrac32) = \tfrac{\sqrt\pi}2$, $\Gamma(\tfrac52) = \tfrac{3\sqrt\pi}4$, proved in [[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-4|Theorem §B4.1.4]].
>
> *Source: Mao §4.5.5, box "Three useful functions: Γ, ζ, and Li" · DLMF §5.2 · level-B home: [[§B4.1 Probability Distributions and the Gaussian#^def-b4-1-5|Def. §B4.1.5]]*

^def-c4b-4-1

> [!definition] Definition §C4b.4.2: Riemann Zeta Function
> $$
> \zeta(q) = \sum_{j\ge1}\frac1{j^q}, \qquad q > 1 .
> $$
>
> *Source: Mao §4.5.5, box "Three useful functions: Γ, ζ, and Li" · DLMF §25.2 · level-B home: [[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]]*

^def-c4b-4-2

> [!definition] Definition §C4b.4.3: Polylogarithm (Integral Form)
> For $q > 0$ and real $w < 1$,
>
> $$
> \operatorname{Li}_q(w) = \frac{1}{\Gamma(q)}\int_0^\infty\frac{w\,x^{q-1}}{e^x - w}\,dx = \frac{1}{\Gamma(q)}\int_0^\infty\frac{x^{q-1}\,dx}{w^{-1}e^x - 1} ,
> $$
>
> with $\Gamma$ of [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]; for $q > 1$ the integral also converges at $w = 1$.
>
> *Source: Mao §4.5.5, eqs. (4.122)–(4.123) · DLMF §25.12 · level-B home (series form): [[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]]*

^def-c4b-4-3

> [!definition] Definition §C4b.4.4: The Bose and Fermi Functions $G_q$
> For both statistics at once,
>
> $$
> G_q(z) \equiv \begin{cases}\operatorname{Li}_q(z), & \text{bosons},\ 0 < z < 1,\\ -\operatorname{Li}_q(-z), & \text{fermions},\ z > 0,\end{cases}
> \qquad\text{so}\qquad
> G_q(z) = \frac1{\Gamma(q)}\int_0^\infty\frac{x^{q-1}\,dx}{z^{-1}e^x \mp 1} ,
> $$
>
> with $\operatorname{Li}_q$ of [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-3|Def. §C4b.4.3]].
>
> *Source: Mao §4.5.5, eq. (4.123) and the display after it · PHY 510 Problem Set 6, part (c)*

^def-c4b-4-4

> [!theorem] Theorem §C4b.4.1: $\ln\Xi$ Is a Polylogarithm
> $$
> \ln\Xi_{\text{cont}} = \mp A\beta^{-\nu}\int_0^\infty x^{\nu-1}\ln(1 \mp ze^{-x})\,dx = A\,\Gamma(\nu)\,\beta^{-\nu}\,G_{\nu+1}(z) .
> $$
>
> *Model:* [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]] with $g = A\epsilon^{\nu-1}$; *applies:* $\nu > 0$, physical $z$; for bosons also $z = 1$, for every $\nu > 0$ (the order $\nu + 1$ exceeds 1).
>
> *Source: Mao §4.5.5, eqs. (4.120)–(4.121) and the display after (4.122)*

^thm-c4b-4-1

> [!derivation]- Derivation
> **Step 1** (substitute). $\ln\Xi = \mp\int g(\epsilon)\ln(1 \mp ze^{-\beta\epsilon})\,d\epsilon$ ([[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]); with $\epsilon = x/\beta$, $g\,d\epsilon = A\beta^{-\nu}x^{\nu-1}dx$.
>
> **Step 2** (by parts). Take $u = \mp\ln(1 \mp ze^{-x})$, $dv = x^{\nu-1}dx$, so $v = x^\nu/\nu$ and $du = -dx/(z^{-1}e^x \mp 1)$. Then
>
> $$
> \mp\int_0^\infty x^{\nu-1}\ln(1 \mp ze^{-x})\,dx = \Bigl[\mp\frac{x^\nu}\nu\ln(1 \mp ze^{-x})\Bigr]_0^\infty + \frac1\nu\int_0^\infty\frac{x^\nu\,dx}{z^{-1}e^x \mp 1} .
> $$
>
> **Step 3** (boundary). At $\infty$ the logarithm decays like $e^{-x}$. At $0$ it is finite for $z < 1$; at the Bose endpoint it behaves like $\ln x$, and $x^\nu\ln x \to 0$ for $\nu > 0$. So the bracket vanishes.
>
> **Step 4** (identify). $\int_0^\infty\frac{x^\nu\,dx}{z^{-1}e^x \mp 1} = \Gamma(\nu + 1)G_{\nu+1}(z)$ by [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]], and $\Gamma(\nu + 1)/\nu = \Gamma(\nu)$.

^der-c4b-4-1

*Uses:* [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-1|Theorem §C4b.3.1]], [[§C4b.3 Summing over Orbitals꞉ the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]]

> [!theorem] Theorem §C4b.4.2: Four Facts about $G_q$
> 1. **Series:** for $0 < z < 1$, $G_q(z) = \sum_{j\ge1}(\pm1)^{j+1}z^j/j^q$; in particular $\operatorname{Li}_1(w) = -\ln(1 - w)$.
> 2. **Differentiation lowers the order:** $z\,\partial_zG_q(z) = G_{q-1}(z)$ for $q > 1$ and all physical $z$.
> 3. **Dilute gases:** $G_q(z) = z \pm z^2/2^q + O(z^3)$.
> 4. **Bose endpoint:** for $q > 1$, $G_q(1) = \zeta(q)$, with
>
> $$
> \zeta(\tfrac32) \simeq 2.612, \qquad \zeta(\tfrac52) \simeq 1.341, \qquad \zeta(3) \simeq 1.202, \qquad \zeta(4) = \frac{\pi^4}{90} .
> $$
>
> Near it, with $\alpha = -\ln z \to 0^+$:
>
> $$
> G_{3/2}(e^{-\alpha}) = \zeta(\tfrac32) - 2\sqrt\pi\,\alpha^{1/2} + O(\alpha), \qquad G_{1/2}(e^{-\alpha}) = \sqrt{\frac\pi\alpha} + O(1) ,
> $$
>
> so $G_{1/2} = z\partial_zG_{3/2}$ diverges at $z = 1$ although $G_{3/2}(1)$ is finite.
>
> *Model:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-2|Def. §C4b.4.2]]; *applies:* as stated in each part. Used in: part 3 by [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]] and [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-3|Theorem §C4b.5.3]]; part 4 by [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-1|Theorem §C4b.7.1]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] and [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-5|Theorem §C4b.7.5]].
>
> *Source: Mao §4.5.5, eqs. (4.124)–(4.127) · DLMF §25.12 · level-B home of part 4: [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-1|Theorem §B10.2.1]]*

^thm-c4b-4-2

> [!derivation]- Derivation
> **Part 1.** For $0 < w < 1$ and $x > 0$, $\frac{w}{e^x - w} = \sum_{j\ge1}w^je^{-jx}$, a series of positive terms, so it may be integrated termwise against $x^{q-1}$ (monotone convergence): $\int_0^\infty x^{q-1}e^{-jx}dx = \Gamma(q)/j^q$, hence $\operatorname{Li}_q(w) = \sum_jw^j/j^q$. For fermions, $w = -z$ with $0 < z < 1$; the partial sums are dominated by $\sum_jz^je^{-jx}$, so termwise integration still holds, and $-\operatorname{Li}_q(-z) = \sum_j(-1)^{j+1}z^j/j^q$. At $q = 1$, $\sum_jw^j/j = -\ln(1 - w)$.
>
> **Part 2.** Put $h(x) = 1/(z^{-1}e^x \mp 1)$. Then $z\partial_zh = z^{-1}e^x/(z^{-1}e^x \mp 1)^2 = -\partial_xh$. In the integral of [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]] integrate by parts:
>
> $$
> z\partial_zG_q = -\frac1{\Gamma(q)}\int_0^\infty x^{q-1}\partial_xh\,dx = \frac{q - 1}{\Gamma(q)}\int_0^\infty x^{q-2}h\,dx = G_{q-1}(z) ,
> $$
>
> the boundary term $x^{q-1}h$ vanishing at $0$ (for $q > 1$, and $h$ finite for $z < 1$) and at $\infty$; $(q - 1)/\Gamma(q) = 1/\Gamma(q - 1)$. No series or continuation is needed, so this holds for every physical $z$, fermions with $z > 1$ included.
>
> **Part 3.** The first two terms of part 1: $z + z^2/2^q$ for bosons and $z - z^2/2^q$ for fermions.
>
> **Part 4.** $G_q(1) = \sum_jj^{-q} = \zeta(q)$ by part 1 and monotone convergence as $z \to 1^-$, finite for $q > 1$. For the endpoint forms write $\frac1{e^y - 1} = \frac1y + r(y)$, with $r$ smooth on $[0, \infty)$, $r(0) = -\tfrac12$ and $r'(y) = O((1 + y)^{-2})$.
>
> - $q = \tfrac32$: $\Gamma(\tfrac32)[G_{3/2}(e^{-\alpha}) - \zeta(\tfrac32)] = \int_0^\infty x^{1/2}\bigl[\frac1{x+\alpha} - \frac1x\bigr]dx + \int_0^\infty x^{1/2}[r(x + \alpha) - r(x)]\,dx$. The first integral is $-\alpha\int_0^\infty\frac{x^{-1/2}dx}{x + \alpha} = -\alpha\cdot\frac{\pi}{\sqrt\alpha} = -\pi\sqrt\alpha$ (substitute $x = \alpha u$, $\int_0^\infty\frac{u^{-1/2}du}{1 + u} = \pi$). The second is at most $\alpha\int_0^\infty x^{1/2}\sup_{[x, x+\alpha]}|r'|\,dx = O(\alpha)$, the integrand falling like $x^{-3/2}$. Divide by $\Gamma(\tfrac32) = \sqrt\pi/2$: $-2\sqrt\pi\,\alpha^{1/2}$.
> - $q = \tfrac12$: $\Gamma(\tfrac12)G_{1/2}(e^{-\alpha}) = \int_0^\infty\frac{x^{-1/2}dx}{x + \alpha} + \int_0^\infty x^{-1/2}r(x + \alpha)\,dx = \frac{\pi}{\sqrt\alpha} + O(1)$, since $r$ is bounded near $0$ and $O(1/y)$ at infinity. Divide by $\sqrt\pi$.

^der-c4b-4-2

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-3|Def. §C4b.4.3]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-2|Def. §C4b.4.2]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]

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
> **Step 2.** Apply to $\ln\Xi = A\Gamma(\nu)\beta^{-\nu}G_{\nu+1}(z)$: $z\partial_z$ lowers the order ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 2); $-\partial_\beta\beta^{-\nu} = \nu\beta^{-\nu-1}$; $\partial_VA = A/V$.
>
> **Step 3.** Comparing, $U = \nu\cdot(pV)$ and $\ln\Xi = \beta pV$, so $\Phi = -pV$.

^der-c4b-4-3

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-1|Theorem §C4b.4.1]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|Theorem §C4a.7.3]]

> [!remark] Remark: Which regime, which expansion
> Every thermodynamic quantity is a $G_q(z)$, so a regime is a range of $z$. At fixed density, lowest energy $0$:
>
> | gas and temperature | $z$ | tool | proved in |
> | --- | --- | --- | --- |
> | any statistics, $T \gg T_Q$ | $z \simeq \rho_3\lambda_T^3/g_s \ll 1$ | series, [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]] part 3 | [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]], [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-3|Theorem §C4b.5.3]] |
> | bosons in 3D, $T \le T_c$ | $z = 1$ in the bulk, $1 - z = O(1/N_0)$ | endpoint, part 4 | [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]], [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] |
> | fermions, $T \ll T_F$ | $\ln z \simeq T_F/T \gg 1$ | Sommerfeld, [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]] | [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-2|Theorem §C4b.9.2]] |
> | black-body photons, any $T$ | $z = 1$ | endpoint, part 4 | [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-1|Theorem §C4b.6.1]], [[§C4b.6 The Photon Gas and Black-Body Radiation#^thm-c4b-6-2|Theorem §C4b.6.2]] |
>
> At other temperatures $z$ is the root of the number equation of [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], unique because $N$ increases with $z$ (part 2: $z\partial_zG_\nu = G_{\nu-1} > 0$). The limit must be taken at fixed density: at fixed $\mu > 0$, $T \to \infty$ sends $z = e^{\mu/k_BT} \to 1$, not to the dilute $z \to 0$.

^rem-c4b-4-1

> [!remark]- Connections
> - The orders and the relation $U = \nu pV$ in any dimension and for any power-law dispersion — [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]].
> - $U = \tfrac32pV$ for nonrelativistic and $U = 3pV$ for ultrarelativistic gases, whatever the statistics — [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-3|Theorem §B10.2.3]].
