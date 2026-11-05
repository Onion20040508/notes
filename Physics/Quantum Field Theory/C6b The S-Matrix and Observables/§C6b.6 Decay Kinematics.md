---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.5 Decay Widths]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.7 The Width in the Propagator]] →

<!-- HEADER-6 -->

## Two-body decays

> [!theorem] Theorem §C6b.6.1: Two-Body Decays
> Let $A$ (mass $m_A$, at rest) decay into two particles of masses $m_1$, $m_2$, $m_A > m_1 + m_2$. Then
> 1. $\displaystyle\int d\Pi_2\,F = \int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2m_A}\,F$, with $|\mathbf p_1| = |\mathbf p_2| = \frac{\lambda^{1/2}(m_A^2, m_1^2, m_2^2)}{2m_A}$, $E_1 = \frac{m_A^2 + m_1^2 - m_2^2}{2m_A}$; in particular $\displaystyle\int d\Pi_2 = \frac{|\mathbf p_1|}{4\pi m_A}$;
> 2. if $|\mathcal M|^2$ does not depend on the direction of $\mathbf p_1$,
>
> $$
> \Gamma = \frac{1}{S_{\rm id}}\,\frac{|\mathbf p_1|}{8\pi m_A^2}\,|\mathcal M|^2 ;
> $$
>
> 3. for equal masses $m_1 = m_2 = m$, with $\beta = \sqrt{1 - 4m^2/m_A^2}$,
>
> $$
> |\mathbf p_1| = \frac{m_A}{2}\,\beta, \qquad \int d\Pi_2 = \frac{\beta}{8\pi}, \qquad \Gamma = \frac{1}{S_{\rm id}}\,\frac{|\mathcal M|^2}{16\pi m_A}\,\beta .
> $$
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there: the kinematics exactly, $\Gamma$ at lowest order in the decaying interaction.
>
> *Source: Yu §6.5.5, eqs. (6.379)–(6.385) (page image checked: (6.383) boxed, (6.385) the equal-mass form, "如果两个末态粒子是全同粒子，则 $\mathcal S = 2$") · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Two-body decays (filled in)", citing "Yu's (6.385)": correct) · PHY 513, Problem Set 8, Problem 4 (the user's $\int d\Pi_2 = p_\ast/(4\pi M)$) · PS §4.5, eqs. (4.81)–(4.82) for the phase space*

^thm-c6b-6-1

> [!derivation]- Derivation
> **Step 1** (phase space). The rest frame of $A$ is the centre-of-mass frame of the products, $P = p_A = (m_A, \mathbf 0)$, $E_{\rm cm} = m_A$. [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]] and [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]] with $E_{\rm cm} \to m_A$ give part 1's first two formulas (Yu (6.379)–(6.381)). With $F = 1$ the integrand does not depend on $\Omega$, $\int d\Omega = 4\pi$:
>
> $$
> \int d\Pi_2 = 4\pi\,\frac{|\mathbf p_1|}{16\pi^2m_A} = \frac{|\mathbf p_1|}{4\pi m_A} .
> $$
>
> **Step 2** (the width). By [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] with $n = 2$ and part 1 with $F = |\mathcal M|^2$ constant in $\Omega$:
>
> $$
> \Gamma = \frac{1}{S_{\rm id}}\,\frac{1}{2m_A}\int d\Omega\,\frac{|\mathbf p_1|}{16\pi^2m_A}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{1}{2m_A}\cdot4\pi\cdot\frac{|\mathbf p_1|}{16\pi^2m_A}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathbf p_1|}{8\pi m_A^2}|\mathcal M|^2
> $$
>
> (Yu (6.383)).
>
> **Step 3** (equal masses). $\lambda(m_A^2, m^2, m^2) = m_A^4 + m^4 + m^4 - 2m_A^2m^2 - 2m_A^2m^2 - 2m^4 = m_A^4 - 4m_A^2m^2 = m_A^4\beta^2$, so (Yu (6.384), with $\lambda^{1/2}(1, \frac{m^2}{m_A^2}, \frac{m^2}{m_A^2}) = \beta$)
>
> $$
> |\mathbf p_1| = \frac{m_A^2\beta}{2m_A} = \frac{m_A}{2}\beta, \qquad \int d\Pi_2 = \frac{m_A\beta/2}{4\pi m_A} = \frac{\beta}{8\pi}, \qquad \Gamma = \frac{1}{S_{\rm id}}\,\frac{m_A\beta/2}{8\pi m_A^2}|\mathcal M|^2 = \frac{1}{S_{\rm id}}\,\frac{|\mathcal M|^2}{16\pi m_A}\beta
> $$
>
> (Yu (6.385)). Directly: $E_1 = E_2 = m_A/2$ and $|\mathbf p_1| = \sqrt{m_A^2/4 - m^2}$, the same.
>
> ⚑ By-product: for $1 \to 2$, $[\mathcal M] = 4 - 3 = 1$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]): $\mathcal M$ has the dimension of a mass, and $[\Gamma] = 2 + 1 - 2 = 1$.
>
> **What the derivation shows.**
> - A two-body decay at rest has no free kinematics: the energies and $|\mathbf p_1|$ are fixed numbers, and only the direction is integrated.
> - The phase-space factor vanishes like $\beta$ at threshold $m_A \to m_1 + m_2$.

^der-c6b-6-1

*Uses:* [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]], [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-8|P7, step 8]]

> [!model] Model §C6b.6.4: Two Scalar Fields with a Φφ² Coupling
> Two real scalar fields, $\Phi$ of mass $M$ and $\phi$ of mass $m$:
>
> $$
> \mathcal L = \tfrac12(\partial_\mu\Phi)^2 - \tfrac12M^2\Phi^2 + \tfrac12(\partial_\mu\phi)^2 - \tfrac12m^2\phi^2 - \mu\,\Phi\phi^2 ,
> $$
>
> each free part the field of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; $[\mu] = 1$; vertex $-2i\mu$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Assumptions:*
> 1. $M > 2m$: $\Phi$ can decay into $\phi\phi$, so it is not a stable asymptotic particle (outside assumption 2 of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]]).
> 2. The potential is not bounded below: at $\Phi = -s$ the coefficient of $\phi^2$ is $\frac{m^2}{2} - \mu s < 0$ for $s > m^2/(2\mu)$ (derived here, not from a source). The model is used at lowest order in $\mu$ only.
> 3. Otherwise as [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]], assumptions 2 and 5.
>
> An instance of Model §C6a.0.3, at lowest order; the decay setup is [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]].
>
> *Source: PHY 513, Problem Set 8, Problem 4 (statement: the Lagrangian, "allows a Φ-particle to decay into two ϕ's, provided that M > 2m", "to the lowest order in µ") · PS Problem 4.2*

^mod-c6b-6-4

> [!example] Example §C6b.6.1: Φ → φφ, the Lifetime at Lowest Order
> ![[ph-qft-c6b-11-2.svg]]
>
> For $\mathcal L = \frac12(\partial_\mu\Phi)^2 - \frac12M^2\Phi^2 + \frac12(\partial_\mu\phi)^2 - \frac12m^2\phi^2 - \mu\,\Phi\phi^2$ ([[§C6b.6 Decay Kinematics#^mod-c6b-6-4|Model §C6b.6.4]]) with $M > 2m$, to lowest order in $\mu$:
>
> $$
> \mathcal M = -2\mu, \qquad \Gamma = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}}, \qquad \tau = \frac1\Gamma = \frac{8\pi M^2}{\mu^2\sqrt{M^2 - 4m^2}} .
> $$
>
> **Step 1** (the amplitude). No derivatives, so $\hat{\mathcal H}_I = -\mathcal L_I = \mu\hat\Phi\hat\phi^2$ and $-i\int dt\,\hat H_I = -i\mu\int d^4x\,\hat\Phi_I\hat\phi_I^2$. With $\hat b$, $\hat a$ the annihilators of $\hat\Phi$, $\hat\phi$ and relativistically normalized states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $|\mathbf K\rangle_\Phi = \sqrt{2E^\Phi_{\mathbf K}}\,\hat b^\dagger_{\mathbf K}|0\rangle$, $|\mathbf p_1\mathbf p_2\rangle = \sqrt{2E_{\mathbf p_1}}\sqrt{2E_{\mathbf p_2}}\,\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle$ (as needed by [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]):
>
> $$
> \mathcal A = \langle\mathbf p_1\mathbf p_2|\,T\Bigl\{\exp\Bigl[-i\mu\int d^4x\,\hat\Phi_I(x)\hat\phi_I(x)^2\Bigr]\Bigr\}|\mathbf K\rangle_\Phi
> $$
>
> ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]]).
>
> **Step 2** (order zero). $\langle\mathbf p_1\mathbf p_2|\mathbf K\rangle_\Phi \propto \langle0|\hat a_{\mathbf p_1}\hat a_{\mathbf p_2}\hat b^\dagger_{\mathbf K}|0\rangle = \langle0|\hat b^\dagger_{\mathbf K}\hat a_{\mathbf p_1}\hat a_{\mathbf p_2}|0\rangle = 0$: different fields commute, and $\hat a|0\rangle = 0$.
>
> **Step 3** (order one, the $\Phi$ end). One time, so $T$ acts trivially: $\mathcal A^{(1)} = -i\mu\int d^4x\,\langle\mathbf p_1\mathbf p_2|\hat\Phi_I(x)\hat\phi_I(x)^2|\mathbf K\rangle_\Phi$. Split $\hat\Phi_I = \hat\Phi_I^+ + \hat\Phi_I^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]). $\hat\Phi_I^-|\mathbf K\rangle_\Phi$ has two $\Phi$ quanta, which $\hat\phi_I^2$ cannot remove: no overlap with $\langle\mathbf p_1\mathbf p_2|$. With $\hat\Phi_I^+|0\rangle = 0$ and $[\hat b_{\mathbf q}, \hat b^\dagger_{\mathbf K}] = (2\pi)^3\delta^3(\mathbf q - \mathbf K)$,
>
> $$
> \hat\Phi_I^+(x)|\mathbf K\rangle_\Phi = \sqrt{2E^\Phi_{\mathbf K}}\,[\hat\Phi_I^+(x), \hat b^\dagger_{\mathbf K}]|0\rangle = \sqrt{2E^\Phi_{\mathbf K}}\int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E^\Phi_{\mathbf q}}}(2\pi)^3\delta^3(\mathbf q - \mathbf K)|0\rangle = e^{-iK\cdot x}|0\rangle, \quad K^0 = E^\Phi_{\mathbf K} .
> $$
>
> **Step 4** (order one, the $\phi$ end). In $\hat\phi_I\hat\phi_I = (\hat\phi_I^+ + \hat\phi_I^-)(\hat\phi_I^+ + \hat\phi_I^-)$ acting on $|0\rangle$, terms with $\hat\phi_I^+$ on the right vanish, and $\hat\phi_I^+\hat\phi_I^-|0\rangle = [\hat\phi_I^+, \hat\phi_I^-]|0\rangle$ is a number times $|0\rangle$, orthogonal to $\langle\mathbf p_1\mathbf p_2|$. Only $\hat\phi_I^-\hat\phi_I^-$ remains; each of $\hat a_{\mathbf p_1}$, $\hat a_{\mathbf p_2}$ contracts with one of the two fields, in $2$ ways, each giving $\sqrt{2E_{\mathbf p_i}}[\hat a_{\mathbf p_i}, \hat\phi_I^-(x)] = e^{ip_i\cdot x}$ (the one-particle case of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]; general form [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]):
>
> $$
> \langle\mathbf p_1\mathbf p_2|\hat\phi_I^-(x)\hat\phi_I^-(x)|0\rangle = e^{ip_1\cdot x}e^{ip_2\cdot x} + e^{ip_2\cdot x}e^{ip_1\cdot x} = 2\,e^{i(p_1 + p_2)\cdot x}, \qquad p_i^0 = E_{\mathbf p_i} .
> $$
>
> **Step 5** ($\mathcal M$). With [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]],
>
> $$
> \mathcal A^{(1)} = -2i\mu\int d^4x\,e^{i(p_1 + p_2 - K)\cdot x} = -2i\mu\,(2\pi)^4\delta^4(K - p_1 - p_2) ,
> $$
>
> and comparing with $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]): $i\mathcal M = -2i\mu$, $\mathcal M = -2\mu$, momentum independent (no derivatives in the vertex). The $2 = 2!$ is the vertex factor's count of ways to attach two distinct lines to the two $\phi$ legs ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> **Step 6** (identical particles). $|\mathbf p_1\mathbf p_2\rangle = |\mathbf p_2\mathbf p_1\rangle$, so integrating $\mathbf p_1$ and $\mathbf p_2$ independently counts each final state twice: $S_{\rm id} = 2!$ ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]; the $\frac{1}{n!}$ of the $n$-particle measure, [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]]).
>
> **Step 7** ($\int d\Pi_2$ with $\delta(f(p))$, the user's evaluation). At rest, $\mathbf p_2 = -\mathbf p_1$ by the $\delta^3$, $E_{\mathbf p_2} = E_{\mathbf p_1} \equiv E_p$, $p = |\mathbf p_1|$, and $d^3p_1 = p^2\,dp\,d\Omega$:
>
> $$
> \int d\Pi_2 = \int\frac{p^2\,dp\,d\Omega}{(2\pi)^3}\,\frac{1}{4E_p^2}\,2\pi\,\delta(M - 2E_p) .
> $$
>
> With $f(p) = M - 2\sqrt{p^2 + m^2}$ on $p \in [0, \infty)$, the only root is $p_\ast = \sqrt{M^2/4 - m^2} = \frac M2\sqrt{1 - 4m^2/M^2}$ ($E_\ast = M/2$; real for $M > 2m$; $-p_\ast$ is outside the range), and $f'(p) = -2p/E_p$, so ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2)
>
> $$
> \delta(M - 2E_p) = \frac{E_\ast}{2p_\ast}\,\delta(p - p_\ast), \qquad \int d\Pi_2 = 4\pi\cdot\frac{2\pi}{(2\pi)^3}\cdot\frac{p_\ast^2}{4E_\ast^2}\cdot\frac{E_\ast}{2p_\ast} = \frac{p_\ast}{8\pi E_\ast} = \frac{p_\ast}{4\pi M} = \frac{1}{8\pi}\sqrt{1 - \frac{4m^2}{M^2}} ,
> $$
>
> [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]].
>
> **Step 8** (width and lifetime). $|\mathcal M|^2 = 4\mu^2$ is constant:
>
> $$
> \Gamma = \frac12\cdot\frac{1}{2M}\cdot4\mu^2\cdot\frac{1}{8\pi}\sqrt{1 - \frac{4m^2}{M^2}} = \frac{\mu^2}{8\pi M}\sqrt{1 - \frac{4m^2}{M^2}}, \qquad \tau = \frac{8\pi M}{\mu^2}\Bigl(1 - \frac{4m^2}{M^2}\Bigr)^{-1/2} = \frac{8\pi M^2}{\mu^2\sqrt{M^2 - 4m^2}} ;
> $$
>
> the same from [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|Theorem §C6b.6.3]]: $\frac12\frac{4\mu^2}{16\pi M}\beta$. $[\mu] = 1$ ($[\Phi\phi^2] = 3$), $[\Gamma] = 2 - 1 = 1$.
>
> *Source: PHY 513, Problem Set 8, Problem 4 (= PS Problem 4.2; the user's solution, Steps 1–8 as written there) · Yu §6.5.5, eq. (6.385)*

^ex-c6b-6-1

## ★ Three-body decays

<!-- NEW thm-c6b-6-5 -->

<!-- NEW thm-c6b-6-6 -->

<!-- NEW def-c6b-6-1 -->

<!-- NEW thm-c6b-6-7 -->

<!-- NEW thm-c6b-6-8 -->

> [!remark]- Connections
<!-- CONN-6 -->
