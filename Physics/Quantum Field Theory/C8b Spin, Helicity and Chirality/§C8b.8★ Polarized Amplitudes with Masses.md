---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, extension]
---
← [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.9 Photon Helicity|§C8b.9]] →

★ *Beyond PHY 513: Lecture 20 computed the helicity amplitudes of $e^+e^- \to \mu^+\mu^-$ for massless fermions; this section keeps both masses, following Yu.*

*Sources: Yu Zhao-Huan, 量子场论讲义, §8.2.4, eqs. (8.99), (8.108)–(8.158) and Figures 8.4–8.6 (page images of the current build checked); §8.2.3, eq. (8.92) · PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 26–28 (the massless currents) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.2, pp. 145–146 (massless). Added 2026-11-16 with the helicity move (user decision: "Yu gives a really good lecture on this topic").*

What happens to the sixteen helicity amplitudes of $e^+e^- \to \mu^+\mu^-$ when the masses are kept? At $m = 0$ only the four with opposite helicities in each pair survive, $\mathcal M = \mp e^2(1 \pm \cos\theta)$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]), and the other twelve vanish ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]). With masses Yu computes all sixteen from the explicit helicity spinors: the four survivors keep their values exactly, the other twelve become nonzero but carry a factor $m_e/E_{\rm cm}$, $m_\mu/E_{\rm cm}$ or both, and every amplitude has the angular zeros that angular momentum requires. Their sum reproduces the unpolarized trace result with both masses. The masses are what [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|§C8b.6, Remark: Frame and mass]], item 4, announced; here are the values. Why each suppressed amplitude carries a mass, one factor for each helicity that has to be flipped, is [[§C8b.8★ Polarized Amplitudes with Masses#^rem-c8b-8-1|★ Remark: A mass flips a helicity]], with the mass term of the Lagrangian as the coupling that does it ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]]).

**The mathematical picture.** The amplitude is the contraction of two currents, $\mathcal M = \frac{e^2}{E_{\rm cm}^2}J_e^\mu J_{\mu\,\mu}$, each a four-vector built from one pair of helicity spinors. In the chiral basis $\gamma^0\gamma^\mu$ is block diagonal ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]), so each current is a sum of two two-spinor bilinears $\xi^\dagger\sigma^\mu\xi$, $\xi^\dagger\bar\sigma^\mu\xi$ weighted by products of the factors $\omega_\pm = \sqrt{E \pm |\mathbf p|}$; the products of two $\omega$'s are either of order $E$ or exactly a mass. The angular dependence is that of a spin-one object carried from the beam axis to the muon axis: each amplitude is proportional to a rotation matrix element $d^1_{J_z J_n}(\theta)$.

**Setup.** [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] at order $e^2$, both masses kept, $E_{\rm cm} > 2m_\mu > 2m_e$. Centre-of-mass frame with the labels of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]]: $e^-(p)$, $e^+(p')$ along $\pm\hat{\mathbf z}$ with speed $\beta_e = \sqrt{1 - 4m_e^2/E_{\rm cm}^2}$, $\mu^-(k)$, $\mu^+(k')$ in the $xz$-plane at angle $\theta$ to $\hat{\mathbf z}$ with speed $\beta_\mu$, as in [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]]. Helicity spinors $u_\lambda$, $v_\lambda$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]] and [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]] ($v_\lambda$ for an antiparticle of helicity $\lambda$), built on the two-spinors of Example §C8b.5.1. $\mathcal M(\lambda_1, \lambda_2, \lambda_1', \lambda_2')$ has the helicities of $e^-$, $e^+$, $\mu^-$, $\mu^+$ in this order. The values are exact; their signs depend on the phases of the two-spinors, the moduli do not.

*Conventions* ([[Larsen PHY 513]]): chiral basis, $g = \operatorname{diag}(+, -, -, -)$; $s_\theta \equiv \sin\theta$, $c_\theta \equiv \cos\theta$. Yu writes $k_1, k_2, p_1, p_2$ for the course's $p, p', k, k'$ and $E_{\rm CM}$ for $E_{\rm cm}$; his amplitude (8.99) is the course's $\mathcal M$ of Theorem §C8a.6.2 with $q^2 = E_{\rm cm}^2$.

## The currents

> [!theorem] ★ Theorem §C8b.8.1: The ω-Products of the Four Momenta
> With $\omega_\pm(\mathbf q) \equiv \sqrt{q^0 \pm |\mathbf q|}$,
>
> $$
> \omega_\pm(\mathbf p')\,\omega_\pm(\mathbf p) = \frac{E_{\rm cm}(1 \pm \beta_e)}{2}, \qquad \omega_\mp(\mathbf p')\,\omega_\pm(\mathbf p) = m_e ,
> $$
>
> and the same for the muons with $\mathbf k$, $\mathbf k'$, $\beta_\mu$, $m_\mu$.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] kinematics; *applies:* centre-of-mass frame, exact.
>
> *Source: Yu §8.2.4, eqs. (8.110)–(8.113), (8.123)–(8.124)*

^thm-c8b-8-1

> [!derivation]- Derivation
> **1. The factors.** In the centre-of-mass frame $p^0 = p'^0 = E_{\rm cm}/2$ and $|\mathbf p| = |\mathbf p'| = \beta_eE_{\rm cm}/2$, so $\omega_\pm(\mathbf p) = \omega_\pm(\mathbf p') = \sqrt{\frac{E_{\rm cm}}2(1 \pm \beta_e)}$.
>
> **2. Equal signs.** The product of two equal factors is the square of one: $\frac{E_{\rm cm}}2(1 \pm \beta_e)$.
>
> **3. Opposite signs.** $\omega_+\omega_- = \frac{E_{\rm cm}}2\sqrt{(1 + \beta_e)(1 - \beta_e)} = \frac{E_{\rm cm}}2\sqrt{1 - \beta_e^2}$, and $1 - \beta_e^2 = 4m_e^2/E_{\rm cm}^2$ (8.112), so the product is $m_e$; this is $\omega_\lambda\omega_{-\lambda} = m$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]] for one particle.
>
> **What the derivation shows**
> - An amplitude that needs one $\omega_+$ and one $\omega_-$ from the same pair carries the mass of that pair, exactly.

^der-c8b-8-1

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-1|Theorem §C8a.8.1]]

> [!theorem] ★ Theorem §C8b.8.2: The Beam Currents
> The electron currents $J_e^\mu(\lambda_1, \lambda_2) \equiv \bar v(p', \lambda_2)\gamma^\mu u(p, \lambda_1)$ are
>
> $$
> J_e^\mu(+, -) = E_{\rm cm}(0, -1, -i, 0), \quad J_e^\mu(-, +) = E_{\rm cm}(0, -1, i, 0), \quad J_e^\mu(+, +) = 2m_e(0, 0, 0, -1), \quad J_e^\mu(-, -) = 2m_e(0, 0, 0, 1) .
> $$
>
> The opposite-helicity currents are the circular polarization vectors of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]], independent of the masses; the equal-helicity currents point along the beam and are proportional to $m_e$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (c-number spinors); *applies:* centre-of-mass frame, helicity spinors of Example §C8b.5.1, exact.
>
> *Source: Yu §8.2.4, eqs. (8.108)–(8.121)*

^thm-c8b-8-2

> [!derivation]- Derivation
> **1. The general form.** With $\bar v = v^\dagger\gamma^0$, $v(p', \lambda_2) = (\lambda_2\omega_{\lambda_2}\xi_{-\lambda_2},\ -\lambda_2\omega_{-\lambda_2}\xi_{-\lambda_2})$, $u(p, \lambda_1) = (\omega_{-\lambda_1}\xi_{\lambda_1},\ \omega_{\lambda_1}\xi_{\lambda_1})$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]]) and $\gamma^0\gamma^\mu = \operatorname{diag}(\bar\sigma^\mu, \sigma^\mu)$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]), multiplying the row, the block matrix and the column:
>
> $$
> J_e^\mu = \lambda_2\,\omega_{\lambda_2}(\mathbf p')\,\omega_{-\lambda_1}(\mathbf p)\;\xi^\dagger_{-\lambda_2}(\hat{\mathbf p}')\bar\sigma^\mu\xi_{\lambda_1}(\hat{\mathbf p}) - \lambda_2\,\omega_{-\lambda_2}(\mathbf p')\,\omega_{\lambda_1}(\mathbf p)\;\xi^\dagger_{-\lambda_2}(\hat{\mathbf p}')\sigma^\mu\xi_{\lambda_1}(\hat{\mathbf p})
> $$
>
> (Yu (8.109); the $\omega$'s are real).
>
> **2. The two-spinor bilinears.** With $\xi_+(\hat{\mathbf p}) = (1, 0)$, $\xi_-(\hat{\mathbf p}) = (0, 1)$, $\xi_+(\hat{\mathbf p}') = (0, -1)$, $\xi_-(\hat{\mathbf p}') = (1, 0)$ (Example §C8b.5.1) and $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$, reading off the entries of the Pauli matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]):
> - $\xi_+^\dagger(\hat{\mathbf p}')\sigma^\mu\xi_+(\hat{\mathbf p}) = (0, -1)\,\sigma^\mu(1, 0)^{\mathsf T} = (0, -1, -i, 0) = -\xi_+^\dagger(\hat{\mathbf p}')\bar\sigma^\mu\xi_+(\hat{\mathbf p})$;
> - $\xi_-^\dagger(\hat{\mathbf p}')\sigma^\mu\xi_-(\hat{\mathbf p}) = (1, 0)\,\sigma^\mu(0, 1)^{\mathsf T} = (0, 1, -i, 0) = -\xi_-^\dagger(\hat{\mathbf p}')\bar\sigma^\mu\xi_-(\hat{\mathbf p})$;
> - $\xi_-^\dagger(\hat{\mathbf p}')\sigma^\mu\xi_+(\hat{\mathbf p}) = (1, 0, 0, 1)$, $\xi_-^\dagger(\hat{\mathbf p}')\bar\sigma^\mu\xi_+(\hat{\mathbf p}) = (1, 0, 0, -1)$;
> - $\xi_+^\dagger(\hat{\mathbf p}')\sigma^\mu\xi_-(\hat{\mathbf p}) = (-1, 0, 0, 1)$, $\xi_+^\dagger(\hat{\mathbf p}')\bar\sigma^\mu\xi_-(\hat{\mathbf p}) = (-1, 0, 0, -1)$ (Yu (8.114)–(8.117)).
>
> **3. Opposite helicities.** $(\lambda_1, \lambda_2) = (+, -)$ uses $\xi_+(\hat{\mathbf p}')$ and $\xi_+(\hat{\mathbf p})$, with the factors $-\omega_-\omega_- = -\frac{E_{\rm cm}}2(1 - \beta_e)$ and $+\omega_+\omega_+ = \frac{E_{\rm cm}}2(1 + \beta_e)$ ([[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-1|Theorem §C8b.8.1]]): $J_e = -\frac{E_{\rm cm}(1 - \beta_e)}2(0, 1, i, 0) + \frac{E_{\rm cm}(1 + \beta_e)}2(0, -1, -i, 0) = E_{\rm cm}(0, -1, -i, 0)$: the $\beta_e$ terms cancel. $(-, +)$ likewise gives $E_{\rm cm}(0, -1, i, 0)$ (8.118)–(8.119).
>
> **4. Equal helicities.** $(+, +)$ uses $\xi_-(\hat{\mathbf p}')$, $\xi_+(\hat{\mathbf p})$ and the mixed products $\omega_+(\mathbf p')\omega_-(\mathbf p) = \omega_-(\mathbf p')\omega_+(\mathbf p) = m_e$: $J_e = m_e(1, 0, 0, -1) - m_e(1, 0, 0, 1) = 2m_e(0, 0, 0, -1)$; $(-, -)$ gives $2m_e(0, 0, 0, 1)$ (8.120)–(8.121). All four checked numerically (`qft-C/tools/l20/verify.py`).
>
> **What the derivation shows**
> - In the opposite-helicity currents the two Weyl blocks contribute with weights $(1 \mp \beta_e)/2$ that add to one: the result does not depend on the mass at all.
> - In the equal-helicity currents each term needs one large and one small $\omega$, and the small one is $m_e/\omega_+$: the current is of order $m_e$, not $E_{\rm cm}$.

^der-c8b-8-2

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-1|Theorem §C8b.8.1]]

> [!theorem] ★ Theorem §C8b.8.3: The Muon Currents
> The muon currents, with a lower index, $J_{\mu\,\mu}(\lambda_1', \lambda_2') \equiv \bar u(k, \lambda_1')\gamma_\mu v(k', \lambda_2')$ are
>
> $$
> J_{\mu\,\mu}(+, -) = E_{\rm cm}(0, c_\theta, -i, -s_\theta), \quad J_{\mu\,\mu}(-, +) = E_{\rm cm}(0, c_\theta, i, -s_\theta), \quad J_{\mu\,\mu}(+, +) = 2m_\mu(0, s_\theta, 0, c_\theta), \quad J_{\mu\,\mu}(-, -) = 2m_\mu(0, -s_\theta, 0, -c_\theta) .
> $$
>
> As functions of the direction they are the beam currents turned by $\theta$ about $\hat{\mathbf y}$: their spatial parts rotate by the full angle $\theta$ while the two-spinors turn by $\theta/2$, the addition of two spins $\frac12$ to spin one.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (c-number spinors); *applies:* centre-of-mass frame, helicity spinors of Example §C8b.5.1, exact.
>
> *Source: Yu §8.2.4, eqs. (8.122)–(8.135) and the sentence after (8.135)*

^thm-c8b-8-3

> [!derivation]- Derivation
> **1. The general form.** $\bar u(k, \lambda_1')\gamma_\mu v(k', \lambda_2') = u^\dagger\gamma^0\gamma_\mu v$ with $\gamma^0\gamma_\mu = \operatorname{diag}(\bar\sigma_\mu, \sigma_\mu)$:
>
> $$
> J_{\mu\,\mu} = \lambda_2'\,\omega_{-\lambda_1'}(\mathbf k)\,\omega_{\lambda_2'}(\mathbf k')\;\xi^\dagger_{\lambda_1'}(\hat{\mathbf k})\bar\sigma_\mu\xi_{-\lambda_2'}(\hat{\mathbf k}') - \lambda_2'\,\omega_{\lambda_1'}(\mathbf k)\,\omega_{-\lambda_2'}(\mathbf k')\;\xi^\dagger_{\lambda_1'}(\hat{\mathbf k})\sigma_\mu\xi_{-\lambda_2'}(\hat{\mathbf k}')
> $$
>
> (Yu (8.122)), with the products of [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-1|Theorem §C8b.8.1]] for the muons.
>
> **2. The bilinears.** With $c = \cos\frac\theta2$, $s = \sin\frac\theta2$, the two-spinors of Example §C8b.5.1, $\sigma_\mu = (\mathbb 1, -\boldsymbol\sigma)$, $\bar\sigma_\mu = (\mathbb 1, \boldsymbol\sigma)$ (lower index), and $c^2 - s^2 = c_\theta$, $2sc = s_\theta$, $c^2 + s^2 = 1$ (8.125):
> - $\xi_+^\dagger(\hat{\mathbf k})\sigma_\mu\xi_+(\hat{\mathbf k}') = (c, s)\,\sigma_\mu\,(s, -c)^{\mathsf T} = (0, c_\theta, -i, -s_\theta) = -\xi_+^\dagger(\hat{\mathbf k})\bar\sigma_\mu\xi_+(\hat{\mathbf k}')$;
> - $\xi_-^\dagger(\hat{\mathbf k})\sigma_\mu\xi_-(\hat{\mathbf k}') = (-s, c)\,\sigma_\mu\,(c, s)^{\mathsf T} = (0, -c_\theta, -i, s_\theta) = -\xi_-^\dagger(\hat{\mathbf k})\bar\sigma_\mu\xi_-(\hat{\mathbf k}')$;
> - $\xi_+^\dagger(\hat{\mathbf k})\sigma_\mu\xi_-(\hat{\mathbf k}') = (1, -s_\theta, 0, -c_\theta)$, $\xi_+^\dagger(\hat{\mathbf k})\bar\sigma_\mu\xi_-(\hat{\mathbf k}') = (1, s_\theta, 0, c_\theta)$;
> - $\xi_-^\dagger(\hat{\mathbf k})\sigma_\mu\xi_+(\hat{\mathbf k}') = (-1, -s_\theta, 0, -c_\theta)$, $\xi_-^\dagger(\hat{\mathbf k})\bar\sigma_\mu\xi_+(\hat{\mathbf k}') = (-1, s_\theta, 0, c_\theta)$ (Yu (8.126)–(8.131)). For the first: the time component is $(c, s)\cdot(s, -c) = cs - sc = 0$; with $\sigma^1(s, -c) = (-c, s)$ the $x$-component is $-(-c^2 + s^2) = c_\theta$; with $\sigma^2(s, -c) = (ic, is)$ it is $-i(c^2 + s^2) = -i$; with $\sigma^3(s, -c) = (s, c)$ it is $-2sc = -s_\theta$.
>
> **3. Opposite helicities.** $(+, -)$: $-\omega_-\omega_-\,(0, -c_\theta, i, s_\theta) + \omega_+\omega_+\,(0, c_\theta, -i, -s_\theta) = \frac{E_{\rm cm}(1 - \beta_\mu)}2(0, c_\theta, -i, -s_\theta) + \frac{E_{\rm cm}(1 + \beta_\mu)}2(0, c_\theta, -i, -s_\theta) = E_{\rm cm}(0, c_\theta, -i, -s_\theta)$; $(-, +)$ likewise (8.132)–(8.133).
>
> **4. Equal helicities.** $(+, +)$: the mixed products are $m_\mu$, $J = m_\mu(1, s_\theta, 0, c_\theta) - m_\mu(1, -s_\theta, 0, -c_\theta) = 2m_\mu(0, s_\theta, 0, c_\theta)$; $(-, -)$ gives $2m_\mu(0, -s_\theta, 0, -c_\theta)$ (8.134)–(8.135). All four checked numerically with massive spinors (`qft-C/tools/l20/verify.py`).
>
> **What the derivation shows**
> - At $\theta = 0$ the muon currents are the beam currents with the lower index (the signs of the spatial components flip) and with $m_\mu$ for $m_e$: the same computation turned by $\theta$.

^der-c8b-8-3

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-1|Theorem §C8b.8.1]]

## The sixteen amplitudes

The amplitudes follow by contracting a beam current with a muon current, $\mathcal M = \frac{e^2}{E_{\rm cm}^2}J_e^\mu J_{\mu\,\mu}$; the polarized cross sections from the two-body formula with unequal masses, $\frac{d\sigma}{d\Omega} = \frac{\beta_\mu}{64\pi^2E_{\rm cm}^2\beta_e}|\mathcal M|^2$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]] with $E_A = E_B = E_{\rm cm}/2$, $|\mathbf v_A - \mathbf v_B| = 2\beta_e$, $|\mathbf p_1| = \beta_\mu E_{\rm cm}/2$; for one helicity configuration, no $\frac14$: [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^cau-c8b-7-2|§C8b.7, Caution: No ¼ for one helicity configuration]]). The four classes are distinguished by whether each pair has opposite or equal helicities.

> [!theorem] ★ Theorem §C8b.8.4: Opposite Helicities in Both Pairs
> $$
> \mathcal M(+, -, +, -) = \mathcal M(-, +, -, +) = -e^2(1 + \cos\theta), \qquad \mathcal M(+, -, -, +) = \mathcal M(-, +, +, -) = e^2(1 - \cos\theta),
> $$
>
> exactly, for all masses, with
>
> $$
> \frac{d\sigma}{d\Omega}\Big|_{\lambda_1 = -\lambda_2 = \lambda_1' = -\lambda_2'} = \frac{\alpha^2\beta_\mu(1 + \cos\theta)^2}{4E_{\rm cm}^2\beta_e}, \qquad \frac{d\sigma}{d\Omega}\Big|_{\lambda_1 = -\lambda_2 = -\lambda_1' = \lambda_2'} = \frac{\alpha^2\beta_\mu(1 - \cos\theta)^2}{4E_{\rm cm}^2\beta_e} .
> $$
>
> The masses enter only through the phase-space factor $\beta_\mu/\beta_e$; at $m = 0$ these are the four amplitudes of Lecture 20 ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]), with the zeros at $\theta = \pi$ and $\theta = 0$ of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]] (Yu's Figure 8.4).
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening.
>
> *Source: Yu §8.2.4, eqs. (8.136)–(8.142), Figure 8.4 and the paragraph after (8.142)*

^thm-c8b-8-4

> [!derivation]- Derivation
> **1. $(+, -, +, -)$.** $J_e^\mu(+, -) = E_{\rm cm}(0, -1, -i, 0)$ (upper index) and $J_{\mu\,\mu}(+, -) = E_{\rm cm}(0, c_\theta, -i, -s_\theta)$ (lower index), so the contraction is the plain sum of products: $J_e^\mu J_{\mu\,\mu} = E_{\rm cm}^2\bigl(0 - c_\theta + (-i)(-i) + 0\bigr) = -E_{\rm cm}^2(1 + c_\theta)$; times $e^2/E_{\rm cm}^2$.
>
> **2. The other three.** $(-, +, -, +)$: $E_{\rm cm}^2(0 - c_\theta + (i)(i) + 0) = -E_{\rm cm}^2(1 + c_\theta)$. $(+, -, -, +)$: $E_{\rm cm}^2(-c_\theta + (-i)(i)) = E_{\rm cm}^2(1 - c_\theta)$. $(-, +, +, -)$: $E_{\rm cm}^2(-c_\theta + (i)(-i)) = E_{\rm cm}^2(1 - c_\theta)$.
>
> **3. Cross sections.** $|\mathcal M|^2 = e^4(1 \pm c_\theta)^2$ and $e^4/(64\pi^2) = \alpha^2/4$ ($\alpha = e^2/4\pi$).
>
> **What the derivation shows**
> - Neither current depends on its mass (Theorems §C8b.8.2–§C8b.8.3), so the massless amplitudes of Lecture 20 are exact; only the flux and the phase space know the masses.

^der-c8b-8-4

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|Theorem §C8b.8.2]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-3|Theorem §C8b.8.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

> [!remark] ★ Remark: A mass flips a helicity
> Yu explains the factors of mass in the twelve suppressed amplitudes as follows.
> 1. *A timelike virtual particle behaves like a real one.* The square root $\sqrt{p^2}$ of its momentum squared plays the role of an effective mass, and its spin is that of the corresponding real particle. The intermediate state of $e^+e^- \to \mu^+\mu^-$ is a timelike virtual photon, of spin one, with angular momentum quantum number $j = 1$. A fermion–antifermion pair of equal helicities has, in Yu's words, angular momentum $j = 0$ in the centre-of-mass frame; the helicity of one of the two particles has to be flipped to reach a state of $j = 1$.
> 2. *The mass of a particle can flip its helicity.* For a massless free particle the helicity is the same in every inertial frame ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]); for a massive free particle it can take different values in different frames, and in the rest frame the momentum vanishes and the helicity is undefined ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-1|§C8b.5, Remark: The helicity of a massive particle depends on the frame]]). The mass may be regarded as a coupling: it couples the two states of opposite helicity, and its effect is to flip the helicity of the particle. In the Lagrangian this coupling is the mass term $-m(\overline{\psi_R}\psi_L + \overline{\psi_L}\psi_R)$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]]).
> 3. *Equal helicities in both pairs* (★ Theorem §C8b.8.5). The mass $m_e$ must flip the helicity of the $e^-$ or the $e^+$, which gives a factor $2m_e/E_{\rm cm}$ in the amplitude, and the mass $m_\mu$ that of the $\mu^-$ or the $\mu^+$, a factor $2m_\mu/E_{\rm cm}$; their product is the $4m_em_\mu/E_{\rm cm}^2$ of the theorem. In the figure of that theorem the helicity of the $e^+$ is flipped by the mass coupling (the cross), the pair turns into the virtual photon, the photon into a muon pair, and the mass coupling flips the helicity of the $\mu^+$. Yu reads the zero at $\theta = \pi/2$ from the same figure: the virtual photon made from the $e^+e^-$ pair has its angular momentum along the $z$-axis and at $\theta = \pi/2$ cannot turn into a $\mu^+\mu^-$ system with angular momentum along the $x$-axis; for $\theta \ne \pi/2$ the amplitude for this shows as the factor $\cos\theta$.
> 4. *Equal helicities in the electron pair only* (★ Theorem §C8b.8.6). One flip, by $m_e$: a factor $2m_e/E_{\rm cm}$. At $\theta = 0$ or $\pi$ the final $\mu^+\mu^-$ system has $J^3 = +1$ or $-1$ while the initial pair has $J^3 = 0$; angular momentum would not be conserved, so the amplitude vanishes. For other angles the muon pair is a superposition of the three eigenstates of $J^3$, which shows as the factor $\sin\theta$.
> 5. *Equal helicities in the muon pair only* (★ Theorem §C8b.8.7). One flip, by $m_\mu$: a factor $2m_\mu/E_{\rm cm}$, negligible if $E_{\rm cm}/2 \gg m_\mu$; the zeros at $\theta = 0$ and $\pi$ for the reason of item 4.
>
> The effect is called **helicity suppression**. Kinematics requires $E_{\rm cm}/2 > m_\mu \gg m_e$, so the eight amplitudes that carry a factor $m_e$ are strongly suppressed and their contribution can be neglected. The general statement, for any bilinear, is [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]] with [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-5|§C8b.6, Remark: Helicity suppression]].
>
> *Source: Yu §8.2.4, p. 328 (the last two paragraphs: "粒子的质量可以翻转螺旋度 … 可以将质量看作一种耦合，它耦合螺旋度相反的两种状态，效果是翻转粒子的螺旋度"), p. 329 (the two paragraphs after Figure 8.5: "这种效应称为螺旋度压低 (helicity suppression)"), p. 330 (the paragraph after Figure 8.6 and the paragraph after (8.157)); Figures 8.5–8.6 (the red crosses labelled $m_e$, $m_\mu$). Added 2026-11-23, after Problem Set 11 was submitted.*

^rem-c8b-8-1

> [!caution] ★ Caution: Yu's picture and the exact currents
> The picture of a flipped helicity accounts for the factors $2m_e/E_{\rm cm}$ and $2m_\mu/E_{\rm cm}$ and for the vanishing of the twelve amplitudes at $m = 0$. The angular factors are read more safely from the currents themselves. The current of an equal-helicity pair is $2m_e(0, 0, 0, \mp1)$, a vector along the axis of the pair (★ [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|Theorem §C8b.8.2]]): it is the component $0$ of spin one along that axis, not the component $\pm1$. The amplitudes are the rotation matrix elements between such components (★ [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-8|Theorem §C8b.8.8]]): $d^1_{00}(\theta) = \cos\theta$ for equal helicities in both pairs, which vanishes at $\theta = \pi/2$, and $d^1_{0,\pm1}(\theta) \propto \sin\theta$ when one pair has opposite helicities. A spin-one state with component $+1$ along $\hat{\mathbf z}$ has the amplitude $d^1_{11}(\pi/2) = \frac12$, not zero, to have component $+1$ along $\hat{\mathbf x}$.
>
> *Source: Yu §8.2.4, pp. 328–330, compared with ★ Theorems §C8b.8.2, §C8b.8.3 and §C8b.8.8 · recorded in `qft-C/ERRATA.md`*

^cau-c8b-8-1

> [!theorem] ★ Theorem §C8b.8.5: Equal Helicities in Both Pairs
> $$
> \mathcal M(+, +, +, +) = \mathcal M(-, -, -, -) = -\frac{4e^2m_em_\mu\cos\theta}{E_{\rm cm}^2}, \qquad \mathcal M(+, +, -, -) = \mathcal M(-, -, +, +) = \frac{4e^2m_em_\mu\cos\theta}{E_{\rm cm}^2},
> $$
>
> $$
> \frac{d\sigma}{d\Omega}\Big|_{\lambda_1 = \lambda_2,\ \lambda_1' = \lambda_2'} = \frac{4\alpha^2m_e^2m_\mu^2\beta_\mu\cos^2\theta}{E_{\rm cm}^6\beta_e} .
> $$
>
> They are suppressed by $m_em_\mu/E_{\rm cm}^2$ and vanish at $\theta = \pi/2$ for any masses. Each mass enters once: a factor $2m_e/E_{\rm cm}$ for the helicity that the electron mass has to flip in the equal-helicity $e^+e^-$ pair, and a factor $2m_\mu/E_{\rm cm}$ for the muon pair ([[§C8b.8★ Polarized Amplitudes with Masses#^rem-c8b-8-1|★ Remark: A mass flips a helicity]]). Since $E_{\rm cm}/2 > m_\mu \gg m_e$, these four amplitudes are strongly suppressed.
>
> ![[ph-qft-c8-17-1.svg]]
> *Yu's Figure 8.5 redrawn: $(+, +, +, +)$ at $\theta = \pi/2$, spins (thick) and momenta (thin). A red cross marks where a mass flips a helicity; the faint arrow is the spin on the side of the collision. The equal-helicity $e^+e^-$ pair has $J_z = 0$ along the beam, the equal-helicity muon pair $J_x = 0$ along its own axis; a single spin-one photon connects them with the factor $d^1_{00}(\theta) = \cos\theta$, which is zero at $\theta = \pi/2$ (★ Theorem §C8b.8.8).*
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening.
>
> *Source: Yu §8.2.4, eqs. (8.143)–(8.147), Figure 8.5 (redrawn; drawn without its marks on the lines until Problem Set 11 was submitted, the red crosses added 2026-11-23) and the two paragraphs after it, p. 329; the proportionality $m_em_\mu\cos\theta/E_{\rm cm}^2$ as on Yu's pages (`qft-C/ERRATA.md`, "Lecture 20 update")*

^thm-c8b-8-5

> [!derivation]- Derivation
> **1. Contraction.** $J_e^\mu(+, +) = 2m_e(0, 0, 0, -1)$ and $J_{\mu\,\mu}(+, +) = 2m_\mu(0, s_\theta, 0, c_\theta)$: only the $z$-components meet, $J_e^\mu J_{\mu\,\mu} = 4m_em_\mu(-1)(c_\theta) = -4m_em_\mu c_\theta$.
>
> **2. Signs.** Each of $J_e(-, -)$, $J_\mu(-, -)$ is minus its $(+, +)$ partner (Theorems §C8b.8.2–§C8b.8.3): $(-, -, -, -)$ has two sign changes, $(+, +, -, -)$ and $(-, -, +, +)$ one.
>
> **3. Cross section.** $|\mathcal M|^2 = 16e^4m_e^2m_\mu^2c_\theta^2/E_{\rm cm}^4$, and $\frac{\beta_\mu}{64\pi^2E_{\rm cm}^2\beta_e}\cdot16e^4 = \frac{4\alpha^2\beta_\mu}{E_{\rm cm}^2\beta_e}$.
>
> **What the derivation shows**
> - The beam current points along $\hat{\mathbf z}$ and the muon current along $\hat{\mathbf k}$; their contraction is $\hat{\mathbf z}\cdot\hat{\mathbf k} = \cos\theta$ up to the sign of the metric.

^der-c8b-8-5

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|Theorem §C8b.8.2]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-3|Theorem §C8b.8.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

> [!theorem] ★ Theorem §C8b.8.6: Equal Helicities in the Electron Pair Only
> $$
> \mathcal M(+, +, +, -) = \mathcal M(+, +, -, +) = \frac{2e^2m_e\sin\theta}{E_{\rm cm}}, \qquad \mathcal M(-, -, -, +) = \mathcal M(-, -, +, -) = -\frac{2e^2m_e\sin\theta}{E_{\rm cm}},
> $$
>
> $$
> \frac{d\sigma}{d\Omega}\Big|_{\lambda_1 = \lambda_2,\ \lambda_1' = -\lambda_2'} = \frac{\alpha^2m_e^2\beta_\mu\sin^2\theta}{E_{\rm cm}^4\beta_e} .
> $$
>
> They are suppressed by $m_e/E_{\rm cm}$ and vanish at $\theta = 0$ and $\theta = \pi$. The factor is $2m_e/E_{\rm cm}$: the electron mass has to flip one helicity of the equal-helicity $e^+e^-$ pair ([[§C8b.8★ Polarized Amplitudes with Masses#^rem-c8b-8-1|★ Remark: A mass flips a helicity]]); with $E_{\rm cm}/2 > m_\mu \gg m_e$ their contribution is negligible.
>
> ![[ph-qft-c8-17-2.svg]]
> *Yu's Figure 8.6 redrawn: $(+, +, +, -)$, spins (thick) and momenta (thin). A red cross marks where the electron mass flips a helicity; the faint arrow is the spin on the side of the collision. The equal-helicity $e^+e^-$ pair has $J_z = 0$; an opposite-helicity muon pair has $J = \pm1$ along its axis, which at $\theta = 0$ or $\pi$ is $J_z = \pm1 \ne 0$: the amplitude vanishes there, $\propto d^1_{0,\pm1}(\theta) \propto \sin\theta$ (★ Theorem §C8b.8.8).*
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening.
>
> *Source: Yu §8.2.4, eqs. (8.148)–(8.152), Figure 8.6 (redrawn; drawn without its marks on the lines until Problem Set 11 was submitted, the red cross added 2026-11-23) and the paragraph after it, p. 330*

^thm-c8b-8-6

> [!derivation]- Derivation
> **1. Contraction.** $J_e^\mu(+, +) = 2m_e(0, 0, 0, -1)$ with $J_{\mu\,\mu}(+, -) = E_{\rm cm}(0, c_\theta, -i, -s_\theta)$: only the $z$-components, $2m_eE_{\rm cm}(-1)(-s_\theta) = 2m_eE_{\rm cm}s_\theta$; times $e^2/E_{\rm cm}^2$. With $J_\mu(-, +) = E_{\rm cm}(0, c_\theta, i, -s_\theta)$ the $z$-component is the same: $(+, +, -, +)$ has the same value.
>
> **2. $(-, -)$ beam.** $J_e(-, -) = -J_e(+, +)$ changes the sign of both.
>
> **3. Cross section.** $|\mathcal M|^2 = 4e^4m_e^2s_\theta^2/E_{\rm cm}^2$, times $\frac{\beta_\mu}{64\pi^2E_{\rm cm}^2\beta_e}$, with $4e^4/64\pi^2 = \alpha^2$.

^der-c8b-8-6

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|Theorem §C8b.8.2]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-3|Theorem §C8b.8.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

> [!theorem] ★ Theorem §C8b.8.7: Equal Helicities in the Muon Pair Only
> $$
> \mathcal M(+, -, +, +) = \mathcal M(-, +, +, +) = -\frac{2e^2m_\mu\sin\theta}{E_{\rm cm}}, \qquad \mathcal M(-, +, -, -) = \mathcal M(+, -, -, -) = \frac{2e^2m_\mu\sin\theta}{E_{\rm cm}},
> $$
>
> $$
> \frac{d\sigma}{d\Omega}\Big|_{\lambda_1 = -\lambda_2,\ \lambda_1' = \lambda_2'} = \frac{\alpha^2m_\mu^2\beta_\mu\sin^2\theta}{E_{\rm cm}^4\beta_e} .
> $$
>
> They are suppressed by $m_\mu/E_{\rm cm}$, negligible when $E_{\rm cm}/2 \gg m_\mu$, and vanish at $\theta = 0$ and $\theta = \pi$ (the mirror image of the figure of ★ Theorem §C8b.8.6: here $J_z = \pm1$ initially and $J = 0$ along the muon axis). The factor is $2m_\mu/E_{\rm cm}$: here the muon mass has to flip one helicity of the equal-helicity $\mu^+\mu^-$ pair ([[§C8b.8★ Polarized Amplitudes with Masses#^rem-c8b-8-1|★ Remark: A mass flips a helicity]]).
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening.
>
> *Source: Yu §8.2.4, eqs. (8.153)–(8.157) and the paragraph after (8.157)*

^thm-c8b-8-7

> [!derivation]- Derivation
> **1. Contraction.** $J_e^\mu(+, -) = E_{\rm cm}(0, -1, -i, 0)$ with $J_{\mu\,\mu}(+, +) = 2m_\mu(0, s_\theta, 0, c_\theta)$: only the $x$-components, $E_{\rm cm}\cdot2m_\mu\cdot(-1)(s_\theta)$; times $e^2/E_{\rm cm}^2$. $J_e(-, +)$ has the same $x$-component, so $(-, +, +, +)$ has the same value.
>
> **2. $(-, -)$ muons.** $J_\mu(-, -) = -J_\mu(+, +)$ changes the sign of both.
>
> **3. Cross section.** As in Derivation §C8b.8.6, step 3, with $m_\mu$ for $m_e$.

^der-c8b-8-7

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|Theorem §C8b.8.2]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-3|Theorem §C8b.8.3]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]

## Angular momentum, parity and the sum

> [!theorem] ★ Theorem §C8b.8.8: Each Amplitude Is a Spin-One Rotation Matrix Element
> With $J_z \equiv \frac12(\lambda_1 - \lambda_2)$, the angular momentum of the beam pair along $\hat{\mathbf z}$, and $J_n \equiv \frac12(\lambda_1' - \lambda_2')$, that of the muon pair along $\hat{\mathbf k}$,
>
> $$
> |\mathcal M(\lambda_1, \lambda_2, \lambda_1', \lambda_2')| = C\,\bigl|d^1_{J_zJ_n}(\theta)\bigr| ,
> $$
>
> with $C$ independent of $\theta$: $C = 2e^2$ for opposite helicities in both pairs, $4e^2m_em_\mu/E_{\rm cm}^2$ for equal ones in both, $2\sqrt2e^2m_e/E_{\rm cm}$ and $2\sqrt2e^2m_\mu/E_{\rm cm}$ for an equal-helicity electron or muon pair. Hence the zeros: $d^1_{\pm1,\pm1}$ vanishes at $\theta = \pi$ and $d^1_{\pm1,\mp1}$ at $\theta = 0$ ([[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|Theorem §C8b.8.4]]), $d^1_{00}$ at $\theta = \pi/2$ (Theorem §C8b.8.5), $d^1_{0,\pm1}$ and $d^1_{\pm1,0}$ at $\theta = 0$ and $\pi$ (Theorems §C8b.8.6–§C8b.8.7).
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening.
>
> *Source: the reading of Yu §8.2.4, Figures 8.4–8.6 and the angular-momentum paragraphs after (8.142), (8.147), (8.152), (8.157) (their values of $J$), written as rotation matrices here; the massless case: [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^rem-c8b-7-3|§C8b.7, ★ Remark: In between, the amplitudes are spin-one rotation matrices]]*

^thm-c8b-8-8

> [!derivation]- Derivation
> **1. The spin-one rotation matrices.** $d^1_{11} = d^1_{-1,-1} = \frac12(1 + \cos\theta)$, $d^1_{1,-1} = d^1_{-1,1} = \frac12(1 - \cos\theta)$, $d^1_{00} = \cos\theta$, $d^1_{\pm1,0} = \mp\frac{\sin\theta}{\sqrt2}$, $d^1_{0,\pm1} = \pm\frac{\sin\theta}{\sqrt2}$ ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]]).
>
> **2. The pairs.** An $e^-$ along $+\hat{\mathbf z}$ with helicity $\lambda_1$ has spin $\frac{\lambda_1}2$ along $\hat{\mathbf z}$; an $e^+$ along $-\hat{\mathbf z}$ with helicity $\lambda_2$ has spin $-\frac{\lambda_2}2$ along $\hat{\mathbf z}$; orbital angular momentum along the line of motion is zero. So $J_z = \frac12(\lambda_1 - \lambda_2)$, and likewise $J_n$ along $\hat{\mathbf k}$ for the muons.
>
> **3. Compare.** Theorem §C8b.8.4: $(1 \pm \cos\theta) = 2d^1_{\pm1,\pm1}$ or $2d^1_{\pm1,\mp1}$ with $J_z = \lambda_1$, $J_n = \lambda_1'$; Theorem §C8b.8.5: $J_z = J_n = 0$ and $\cos\theta = d^1_{00}$; Theorem §C8b.8.6: $J_z = 0$, $J_n = \pm1$, $\sin\theta = \sqrt2|d^1_{0,\pm1}|$; Theorem §C8b.8.7: $J_z = \pm1$, $J_n = 0$, $\sin\theta = \sqrt2|d^1_{\pm1,0}|$. Checked numerically for all sixteen at two angles (`qft-C/tools/l20/verify.py`).
>
> **What the derivation shows**
> - The angular dependence of every amplitude is fixed by the spin $j = 1$ of the photon and by the two angular-momentum projections; the dynamics and the masses only set the constant $C$.
> - A zero at $\theta = 0$ or $\pi$ appears exactly when $J_z \ne \pm J_n$ there, the forward argument of Lecture 20 ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]) applied to all sixteen.

^der-c8b-8-8

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|Theorem §C8b.8.4]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-5|Theorem §C8b.8.5]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-6|Theorem §C8b.8.6]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-7|Theorem §C8b.8.7]], [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]]

> [!theorem] ★ Theorem §C8b.8.9: Reversing All Helicities Changes at Most the Sign
> $$
> \mathcal M(-\lambda_1, -\lambda_2, -\lambda_1', -\lambda_2') = \eta\,\mathcal M(\lambda_1, \lambda_2, \lambda_1', \lambda_2'),
> $$
>
> with $\eta = +1$ when both pairs have opposite or both have equal helicities (Theorems §C8b.8.4–§C8b.8.5) and $\eta = -1$ when exactly one pair has equal helicities (Theorems §C8b.8.6–§C8b.8.7). So $|\mathcal M|$ and the polarized cross sections are unchanged when every helicity is reversed, as parity invariance of QED requires.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening; the phase $\eta$ refers to the phases of Example §C8b.5.1.
>
> *Source: Yu §8.2.4, eq. (8.140) and the sentences after (8.139), (8.146), (8.151), (8.156) on the phase factors $1$ and $-1$*

^thm-c8b-8-9

> [!derivation]- Derivation
> **1. Read off.** Theorem §C8b.8.4: $\mathcal M(-, +, -, +) = \mathcal M(+, -, +, -)$ and $\mathcal M(-, +, +, -) = \mathcal M(+, -, -, +)$; Theorem §C8b.8.5: $\mathcal M(-, -, -, -) = \mathcal M(+, +, +, +)$, $\mathcal M(-, -, +, +) = \mathcal M(+, +, -, -)$; Theorem §C8b.8.6: $\mathcal M(-, -, -, +) = -\mathcal M(+, +, +, -)$, $\mathcal M(-, -, +, -) = -\mathcal M(+, +, -, +)$; Theorem §C8b.8.7: $\mathcal M(-, +, -, -) = -\mathcal M(+, -, +, +)$, $\mathcal M(+, -, -, -) = -\mathcal M(-, +, +, +)$. Checked numerically (`qft-C/tools/l20/verify.py`).
>
> **2. Why it must be a phase.** Parity reverses every momentum and keeps every spin, so it reverses every helicity; a rotation by $\pi$ about $\hat{\mathbf y}$ then brings the momenta back. QED is parity invariant ([[§C9.4 Fermion Bilinears under Parity|§C9.4]]), so the two amplitudes describe physically equivalent processes and can differ only by a phase ([[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ]]); the value of the phase depends on the phase conventions of the spinors.

^der-c8b-8-9

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|Theorem §C8b.8.4]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-5|Theorem §C8b.8.5]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-6|Theorem §C8b.8.6]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-7|Theorem §C8b.8.7]]

> [!theorem] ★ Theorem §C8b.8.10: The Sum of the Sixteen Is the Unpolarized Result
> $$
> \frac14\sum_{\lambda_1\lambda_2\lambda_1'\lambda_2'}|\mathcal M(\lambda_1, \lambda_2, \lambda_1', \lambda_2')|^2 = e^4\Bigl[1 + \beta_e^2\beta_\mu^2\cos^2\theta + \frac{4(m_e^2 + m_\mu^2)}{E_{\rm cm}^2}\Bigr] = 16\pi^2\alpha^2\Bigl[1 + \beta_e^2\beta_\mu^2\cos^2\theta + \frac{4(m_e^2 + m_\mu^2)}{E_{\rm cm}^2}\Bigr] ,
> $$
>
> the trace result of [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] in the centre-of-mass frame with both masses (Yu (8.92)); at $m_e = 0$ it is [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]].
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as in the opening; unpolarized beams, final spins summed.
>
> *Source: Yu §8.2.4, eq. (8.158) and the sentence after it*

^thm-c8b-8-10

> [!derivation]- Derivation
> **1. Add the squares.** From Theorems §C8b.8.4–§C8b.8.7, with $E \equiv E_{\rm cm}$: $2e^4(1 + c_\theta)^2 + 2e^4(1 - c_\theta)^2 + 4\cdot\frac{16e^4m_e^2m_\mu^2c_\theta^2}{E^4} + 4\cdot\frac{4e^4m_e^2s_\theta^2}{E^2} + 4\cdot\frac{4e^4m_\mu^2s_\theta^2}{E^2}$.
>
> **2. Divide by 4 and collect.** $2(1 + c_\theta)^2 + 2(1 - c_\theta)^2 = 4(1 + c_\theta^2)$, so $\frac14\sum = e^4\bigl[1 + c_\theta^2 + \frac{16m_e^2m_\mu^2c_\theta^2}{E^4} + \frac{4(m_e^2 + m_\mu^2)(1 - c_\theta^2)}{E^2}\bigr]$.
>
> **3. Factor.** The $c_\theta^2$ terms are $c_\theta^2\bigl(1 - \frac{4m_e^2}{E^2}\bigr)\bigl(1 - \frac{4m_\mu^2}{E^2}\bigr) = \beta_e^2\beta_\mu^2c_\theta^2$ (expand the product: $1 - \frac{4(m_e^2 + m_\mu^2)}{E^2} + \frac{16m_e^2m_\mu^2}{E^4}$), leaving $1 + \frac{4(m_e^2 + m_\mu^2)}{E^2}$. With $e^4 = 16\pi^2\alpha^2$ this is the statement (Yu (8.158)).
>
> **4. Compare with the traces.** In [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] put $p\cdot k = p'\cdot k' = \frac{E^2}4(1 - \beta_e\beta_\mu c_\theta)$, $p\cdot k' = p'\cdot k = \frac{E^2}4(1 + \beta_e\beta_\mu c_\theta)$, $p\cdot p' = \frac{E^2}4(1 + \beta_e^2)$, $k\cdot k' = \frac{E^2}4(1 + \beta_\mu^2)$, $q^2 = E^2$: the bracket times $8e^4/E^4$ gives the same expression (checked numerically, `qft-C/tools/l20/verify.py`). At $m_e = 0$: $\beta_e = 1$ and $\beta_\mu^2 = 1 - 4m_\mu^2/E^2$, Theorem §C8a.8.3 with $E = 2E_{\rm beam}$.
>
> **What the derivation shows**
> - The twelve mass-suppressed configurations supply exactly the mass terms of the trace result: $4(m_e^2 + m_\mu^2)/E_{\rm cm}^2$ and the $\beta$'s in front of $\cos^2\theta$.

^der-c8b-8-10

*Uses:* [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|Theorem §C8b.8.4]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-5|Theorem §C8b.8.5]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-6|Theorem §C8b.8.6]], [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-7|Theorem §C8b.8.7]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]], [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]]

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> - [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-3|Theorem §CB.10.3]] — the spin-$j$ representations whose $j = 1$ matrix elements $d^1_{mm'}$ are used in ★ Theorem §C8b.8.8 (physics form: [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]]).

> [!remark]- Connections
> - The massless limit of this section is Lecture 20: the four surviving amplitudes, their cross sections and the forward argument — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]–[[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]; the vanishing of the other twelve at $m = 0$ — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]].
> - The size $m/E$ of the suppressed amplitudes is the size of the small Weyl block of a fast helicity spinor — [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2.
> - Yu's angular-momentum pictures, Figures 8.4–8.6: Figure 8.4 is [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]'s figure; Figures 8.5–8.6 are redrawn above.
> - The polarized amplitudes add up to the trace computation of Lecture 19 — [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]], [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production|§C8a.8]].
> - The rule that decides which bilinears vanish at high energy, and the mass term as the coupling between the two chiralities — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]]; helicity suppression in another process, backward Compton scattering — [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]].
