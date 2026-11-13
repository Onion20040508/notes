---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.6 Momentum-Space Feynman Rules]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C8.1 The QED Lagrangian and the Covariant Derivative]] →

*Sources: PHY 513 Lecture 18 (Larsen, 9 Nov 2026), Part C, slides 18–23, 26–29, and transcript · the user's PHY 513 notes, Lecture 18 update, §18.7 "Potentials: Yukawa versus Coulomb" (subsections "The nonrelativistic limit", "The Born approximation", "The Yukawa potential" with Derivation "The Fourier transform (filled in)"; Caution "The correction to $u$ is $O(|\mathbf p|/m)$, not $O(\mathbf p^2)$"; Caution "Slips in the slides and the handwritten notes") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 121–123, eqs. (4.121)–(4.128) (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.4.3, eqs. (8.251)–(8.257), (8.279)–(8.287) · PHY 513 Lecture 17, transcript ("next week we'll do something where we actually care about the sign. We'll try to double check, for example, that two like charges in fact … repel") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The relative sign from antisymmetry" (the pointer to next week).*

What force does the exchange of the Yukawa scalar produce between two fermions? Lecture 18 (Part C) takes it up as the first application of the rules, next to the same question for QED ([[§C8.5 The Coulomb Potential, and Why Like Charges Repel|§C8.5]]); this section keeps PS's route (§4.7, from which it was first written), with the lecture's forms added: the nonrelativistic amplitude $\mathcal M_{\rm NR}$ ([[§C6d.7 The Yukawa Potential#^def-c6d-7-1|Def. §C6d.7.1]]) and the Born comparison $i\mathcal M_{\rm NR} = -i\tilde V(\mathbf q)$ as a statement of its own ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]]). PS answer it by "descending from abstraction to concrete physics": take the $t$-channel amplitude of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] for two *distinguishable* fermions, keep the lowest order in the three-momenta ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], [[§C6d.7 The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]]), and compare with the Born approximation of nonrelativistic scattering ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]]). The result is the attractive Yukawa potential $V(r) = -\frac{g^2}{4\pi r}e^{-m_\phi r}$ ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]]), the same between a fermion and an antifermion and between two antifermions ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-4|Theorem §C6d.7.4]]): scalar exchange is universally attractive. Here the overall sign of the amplitude matters, and it is fixed by the convention $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]]; that the sign so fixed is physical: [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]). The classical-source route to the same potential is [[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]].

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two Dirac species $f_1$, $f_2$ of mass $m$, each coupled to $\phi$ with $g$ (so that only the $t$-channel diagram exists), at order $g^2$, free relativistic states over $|0\rangle$ with bras the adjoints of the kets ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], PS (4.118)); nonrelativistic kinematics, $|\mathbf p| \ll m$, to lowest order in the three-momenta.

*Conventions* ([[Larsen PHY 513]], row "Momentum transfer"): throughout the section the momentum transfer is the course's $\mathbf q = \mathbf p - \mathbf p'$ (incoming minus outgoing momentum of the scattered particle), and $\tilde V(\mathbf q) = \int d^3x\,e^{i\mathbf q\cdot\mathbf x}V(\mathbf x)$, $V(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}\tilde V(\mathbf q)\,e^{-i\mathbf q\cdot\mathbf x}$, as in [[§C8.5 The Coulomb Potential, and Why Like Charges Repel|§C8.5]]; PS's sign of $\mathbf q$ is recorded once, in [[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]] (*Names*).

> [!theorem] Theorem §C6d.7.1: Spinor Products in the Nonrelativistic Limit
> For momenta $|\mathbf p|, |\mathbf p'| \ll m$, with the spinors of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] and [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]] built on orthonormal two-spinors $\xi^s$, $\eta^s$,
>
> $$
> \bar u^{s'}(p')\,u^s(p) = 2m\,\xi^{s'\dagger}\xi^s + O(\mathbf p^2) = 2m\,\delta^{ss'} + O(\mathbf p^2) , \qquad \bar v^s(k)\,v^{s'}(k') = -2m\,\eta^{s\dagger}\eta^{s'} + O(\mathbf k^2) = -2m\,\delta^{ss'} + O(\mathbf k^2) ,
> $$
>
> $O(\mathbf p^2)$ standing for second order in $\mathbf p$, $\mathbf p'$ (resp. $\mathbf k$, $\mathbf k'$) over $m$. The first-order terms cancel. So "the spin of each particle is separately conserved in this nonrelativistic scattering interaction".
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number spinors on shell, $|\mathbf p| \ll m$; at $\mathbf p = \mathbf p'$ exact ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-4|Theorem §C5a.12.4]]).
>
> *Source: PS §4.7, p. 121, eq. (4.122) ($u^s(p) = \sqrt m(\xi^s, \xi^s)$, "etc."), p. 122, eq. (4.128) ($\bar v^s(k)v^{s'}(k') \approx -2m\delta^{ss'}$) · the first-order cancellation written here*

^thm-c6d-7-1

> [!derivation]- Derivation
> **Step 1** (the square roots). $p\cdot\sigma = E_{\mathbf p} - \mathbf p\cdot\boldsymbol\sigma$ and $p\cdot\bar\sigma = E_{\mathbf p} + \mathbf p\cdot\boldsymbol\sigma$, with $E_{\mathbf p} = m + \frac{\mathbf p^2}{2m} + \cdots = m + O(\mathbf p^2)$. The matrix $\mathbf p\cdot\boldsymbol\sigma/m$ has eigenvalues $\pm|\mathbf p|/m$, of modulus $< 1$, so the binomial series $\sqrt{1 + \varepsilon} = 1 + \frac\varepsilon2 + O(\varepsilon^2)$ applies to it:
>
> $$
> \sqrt{p\cdot\sigma} = \sqrt m\Bigl(1 - \frac{\mathbf p\cdot\boldsymbol\sigma}{2m}\Bigr) + O(\mathbf p^2) , \qquad \sqrt{p\cdot\bar\sigma} = \sqrt m\Bigl(1 + \frac{\mathbf p\cdot\boldsymbol\sigma}{2m}\Bigr) + O(\mathbf p^2) .
> $$
>
> **Step 2** ($\bar uu$). With $\bar u^{s'}(p') = (\xi^{s'\dagger}\sqrt{p'\cdot\bar\sigma},\ \xi^{s'\dagger}\sqrt{p'\cdot\sigma})$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]]) and $u^s(p) = (\sqrt{p\cdot\sigma}\,\xi^s,\ \sqrt{p\cdot\bar\sigma}\,\xi^s)$,
>
> $$
> \bar u^{s'}(p')u^s(p) = \xi^{s'\dagger}\bigl[\sqrt{p'\cdot\bar\sigma}\sqrt{p\cdot\sigma} + \sqrt{p'\cdot\sigma}\sqrt{p\cdot\bar\sigma}\bigr]\xi^s .
> $$
>
> Insert Step 1: $m\bigl[(1 + \frac{\mathbf p'\cdot\boldsymbol\sigma}{2m})(1 - \frac{\mathbf p\cdot\boldsymbol\sigma}{2m}) + (1 - \frac{\mathbf p'\cdot\boldsymbol\sigma}{2m})(1 + \frac{\mathbf p\cdot\boldsymbol\sigma}{2m})\bigr] = m\bigl[2 + \frac{\mathbf p'\cdot\boldsymbol\sigma}{2m} - \frac{\mathbf p\cdot\boldsymbol\sigma}{2m} - \frac{\mathbf p'\cdot\boldsymbol\sigma}{2m} + \frac{\mathbf p\cdot\boldsymbol\sigma}{2m}\bigr] + O(\mathbf p^2) = 2m + O(\mathbf p^2)$: the first-order terms cancel in pairs. Hence $\bar u^{s'}(p')u^s(p) = 2m\,\xi^{s'\dagger}\xi^s + O(\mathbf p^2)$, and $\xi^{s'\dagger}\xi^s = \delta^{ss'}$.
>
> **Step 3** ($\bar vv$). With $\bar v^s(k) = (-\eta^{s\dagger}\sqrt{k\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{k\cdot\sigma})$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-4|Theorem §C5a.11.4]]) and $v^{s'}(k') = (\sqrt{k'\cdot\sigma}\,\eta^{s'},\ -\sqrt{k'\cdot\bar\sigma}\,\eta^{s'})$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]):
>
> $$
> \bar v^s(k)v^{s'}(k') = -\eta^{s\dagger}\bigl[\sqrt{k\cdot\bar\sigma}\sqrt{k'\cdot\sigma} + \sqrt{k\cdot\sigma}\sqrt{k'\cdot\bar\sigma}\bigr]\eta^{s'} = -2m\,\eta^{s\dagger}\eta^{s'} + O(\mathbf k^2) ,
> $$
>
> the bracket being that of Step 2 with $p' \to k$, $p \to k'$. At rest this is PS (4.128): $m(\eta^\dagger, -\eta^\dagger)\gamma^0(\eta', -\eta') = m(\eta^\dagger, -\eta^\dagger)(-\eta', \eta') = -2m\,\eta^\dagger\eta'$ (chiral $\gamma^0$, [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]).
>
> **What the derivation shows.**
> - The leading correction is second order; the spin-flip part ($\propto i\boldsymbol\sigma\cdot(\mathbf p'\times\mathbf p)$, from the products $(\mathbf p'\cdot\boldsymbol\sigma)(\mathbf p\cdot\boldsymbol\sigma)$) is suppressed by $\mathbf p^2/m^2$.
> - ⚑ By-product: the factor $2m$ per spinor product is the relativistic normalization $2E \approx 2m$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] → [[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]], Step 2.

^der-c6d-7-1

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-4|Theorem §C5a.11.4]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]

> [!caution] Caution: The correction to u is first order in the momentum
> Slide 20 writes $u^s(p) = \sqrt m\,(\xi^s, \xi^s)^{\mathsf T} + O(p^2)$. Expanding $\sqrt{p\cdot\sigma} = \sqrt m\bigl(1 - \frac{\mathbf p\cdot\boldsymbol\sigma}{2m} + \cdots\bigr)$ (Step 1 of [[§C6d.7 The Yukawa Potential#^der-c6d-7-1|Derivation §C6d.7.1]]) shows that the first correction to the spinor is linear in $\mathbf p$, of relative order $|\mathbf p|/m$. It drops out of the product: $\bar u^{s'}(p')u^s(p) = 2m\,\delta^{ss'} + O(\mathbf p^2)$ ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]]), and exactly $2m$ at equal momenta. In QED it is what makes $\bar u\gamma^iu$ small rather than zero ([[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-1|Theorem §C8.5.1]]).
>
> *Source: the user's PHY 513 notes, Lecture 18 update, §18.7, Caution "The correction to $u$ is $O(|\mathbf p|/m)$, not $O(\mathbf p^2)$" · PHY 513 Lecture 18, slide 20 · recorded in `qft-C/ERRATA.md`*

^cau-c6d-7-1

> [!theorem] Theorem §C6d.7.2: The Nonrelativistic Amplitude for Distinguishable Fermions
> For $f_1(p) + f_2(k) \to f_1(p') + f_2(k')$ in the setup of this section, with spins $s \to s'$ and $r \to r'$ and momentum transfer $\mathbf q = \mathbf p - \mathbf p'$, to lowest order in the three-momenta
>
> $$
> i\mathcal M = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2}\;2m\,\delta^{ss'}\;2m\,\delta^{rr'} , \qquad |\mathbf q|^2 = |\mathbf p - \mathbf p'|^2 .
> $$
>
> Only the $t$-channel diagram of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] contributes, with sign $+$. The nonrelativistic approximation neglects $O(\mathbf p^2)$: $p \simeq (m, \mathbf p)$, $p' \simeq (m, \mathbf p')$, so $(p' - p)^2 = -|\mathbf p - \mathbf p'|^2 + O(\mathbf p^4)$, and likewise for $k$, $k'$: the propagator depends on the momentum transfer alone (slide 20). The result conserves the spin of each particle (slide 21). The spins $s$, $s'$ are kept different on purpose: orthonormality of the $\xi$'s forces them equal, and a theory that flipped spins here would be a different theory. The potential the amplitude is compared with is spin-independent, and potential scattering by a spin-independent potential does not flip the spin, which is why the factors $\delta^{ss'}$, $\delta^{rr'}$ can be dropped in the comparison ([[§C6d.7 The Yukawa Potential#^def-c6d-7-1|Def. §C6d.7.1]]). With two different masses the factors are $2m_1\delta^{ss'}\,2m_2\delta^{rr'}$ (the lecture and PS write $m$ for both). Only $|\mathbf q|$ enters (PS's $\mathbf q$ has the opposite sign: the *Names* sentence of [[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]]). The QED twin is [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-2|Theorem §C8.5.2]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* order $g^2$ (the lowest), free states with $(|f\rangle)^\dagger = \langle f|$, $|\mathbf p| \ll m$.
>
> *Source: PHY 513 Lecture 18, slide 19 ($i\mathcal M_{\rm Yukawa}$), slide 20 ("The non-relativistic approximation neglects $O(p^2)$: $p = (m, \vec p)$, $p' = (m, \vec p')$ ⇒ $(p' - p)^2 = -|\vec p - \vec p'|^2 + O(\vec p^4)$"), slide 21 ("$i\mathcal M_{\rm Yukawa} = \frac{ig^2}{|\vec p - \vec p'|^2 + m_\phi^2}\,2m\delta^{ss'}\,2m\delta^{rr'}$ … the NR limit conserves spin") · the user's PHY 513 notes, Lecture 18 update, §18.7, "The nonrelativistic limit", eq. (MYukNR) · PS §4.7, p. 121, eqs. (4.121)–(4.123) ("If the two interacting particles are distinguishable, only the first diagram in (4.119) contributes") · Yu §8.4.3, eqs. (8.279)–(8.281)*

^thm-c6d-7-2

> [!derivation]- Derivation
> **Step 1** (one diagram). With $|\mathbf p, \mathbf k\rangle = \sqrt{\cdots}\,\hat a^\dagger_{1\mathbf p}\hat a^\dagger_{2\mathbf k}|0\rangle$ and $\langle\mathbf p', \mathbf k'| = \sqrt{\cdots}\,\langle0|\hat a_{2\mathbf k'}\hat a_{1\mathbf p'}$, the $f_1$ fields can only contract with $f_1$ particles. Each vertex is $\hat{\bar\psi}_j\hat\psi_j\hat\phi$ of one species $j$, so the vertex at $x$ (say) carries $f_1$: $p \to p'$, and the one at $y$ carries $f_2$: $k \to k'$. The exchange pattern C of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] would need $p \to k'$, an $f_1$ turning into an $f_2$: absent. The string and its arcs are those of pattern A: two crossings, sign $+$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]). So
>
> $$
> i\mathcal M = (-ig)^2\,\bar u^{s'}(p')u^s(p)\,\frac{i}{(p' - p)^2 - m_\phi^2}\,\bar u^{r'}(k')u^r(k)
> $$
>
> ($i\varepsilon$ dropped: the denominator does not vanish, Step 2).
>
> **Step 2** (kinematics, PS (4.121)). $p^0 = E_{\mathbf p} = m + O(\mathbf p^2)$, likewise for $p'$, so $(p' - p)^2 = (E_{\mathbf p'} - E_{\mathbf p})^2 - |\mathbf p' - \mathbf p|^2 = -|\mathbf p - \mathbf p'|^2 + O(\mathbf p^4) = -|\mathbf q|^2 + O(\mathbf p^4)$, with $\mathbf q = \mathbf p - \mathbf p'$ and $E_{\mathbf p'} - E_{\mathbf p} = O(\mathbf p^2)$.
>
> **Step 3** (assemble). With [[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], $(-ig)^2 = -g^2$ and $\frac{i}{-|\mathbf q|^2 - m_\phi^2} = \frac{-i}{|\mathbf q|^2 + m_\phi^2}$:
>
> $$
> i\mathcal M = (-g^2)\cdot\frac{-i}{|\mathbf q|^2 + m_\phi^2}\cdot2m\,\delta^{ss'}\cdot2m\,\delta^{rr'} = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2}\,2m\,\delta^{ss'}\,2m\,\delta^{rr'} .
> $$
>
> **What the derivation shows.**
> - The sign of $i\mathcal M$ comes from $(-ig)^2 = -g^2$ times the $-$ of a spacelike exchange: $+ig^2/(\cdots)$, PS (4.123).

^der-c6d-7-2

*Uses:* [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]]

> [!theorem] Theorem §C6d.7.3: The Yukawa Potential
> Identifying the amplitude of [[§C6d.7 The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]], stripped of the relativistic normalization, with the Born amplitude $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\tilde V(\mathbf q)\,(2\pi)\delta(E_{\mathbf p'} - E_{\mathbf p})$, $\mathbf q = \mathbf p - \mathbf p'$, $\tilde V(\mathbf q) = \int d^3x\,e^{i\mathbf q\cdot\mathbf x}V(\mathbf x)$ ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]], 1), gives
>
> $$
> \tilde V(\mathbf q) = \frac{-g^2}{|\mathbf q|^2 + m_\phi^2} , \qquad V(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}\,\tilde V(\mathbf q)\,e^{-i\mathbf q\cdot\mathbf x} = -\frac{g^2}{4\pi}\,\frac{1}{r}\,e^{-m_\phi r} , \qquad r = |\mathbf x| ,
> $$
>
> an **attractive** potential of range $1/m_\phi$ ($= \hbar/m_\phi c$, the Compton wavelength of the exchanged boson). Its sign is the chain $(-ig)^2 = -g^2$, the spacelike exchange $q^2 = -|\mathbf q|^2$, and $\bar uu = +2m$, with the overall sign of $\mathcal M$ fixed by $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]]); for $m_\phi \to 0$ it becomes $-g^2/4\pi r$, an attractive Coulomb-like potential. In the lecture's words the potential is *attractive* (the minus sign) and *exponentially damped*: a screened Coulomb potential, screened because the exchanged particle has a mass; a massless scalar would give an attractive $1/r$ potential, like Coulomb's but without spin (the exchanged particle is a scalar); unlike Coulomb's it attracts whatever the charges ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-4|Theorem §C6d.7.4]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-3|Theorem §C8.5.3]]). The matching used here is stated on its own, in the lecture's form $i\mathcal M_{\rm NR} = -i\tilde V(\mathbf q)$, in [[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]], in the same conventions. *Names:* PS write the momentum transfer $\mathbf q = \mathbf p' - \mathbf p$ and $\tilde V(\mathbf q) = \int d^3x\,V(\mathbf x)\,e^{-i\mathbf q\cdot\mathbf x}$, $V(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}\tilde V(\mathbf q)\,e^{i\mathbf q\cdot\mathbf x}$ (eqs. (4.124)–(4.126)), the formulas above with $\mathbf q \to -\mathbf q$; they give the same $\tilde V$ and the same $V$, since only $|\mathbf q|$ enters (a central potential).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* order $g^2$, nonrelativistic limit, the Born approximation of one-particle quantum mechanics ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^mod-c10-1-1|QM Model §C10.1.1]]); the identification is PS's matching, not a derivation of a two-body Schrödinger equation.
>
> *Source: PHY 513 Lecture 18, slide 23 ("$\tilde V(\vec q) = \frac{-g^2}{|\vec q|^2 + m_\phi^2}$ … $V(\vec x) = \int\frac{d^3q}{(2\pi)^3}\frac{-g^2}{|\vec q|^2 + m_\phi^2}e^{-i\vec q\cdot\vec x} = -\frac{g^2}{4\pi r}e^{-m_\phi r}$. Attractive Yukawa potential = screened Coulomb potential") · the user's PHY 513 notes, Lecture 18 update, §18.7, "The Yukawa potential", eq. (yukawaV), Derivation "The Fourier transform (filled in)" · Yu §8.4.3, eqs. (8.282)–(8.285) · PS §4.7, pp. 121–122, eqs. (4.124)–(4.127) ("an attractive 'Yukawa potential', with range $1/m_\phi = \hbar/m_\phi c$ … Yukawa … worked backwards from the range of the force (about 1 fm) to predict the mass (about 200 MeV) of the required boson, the pion")*

^thm-c6d-7-3

> [!derivation]- Derivation
> **Step 1** (the Born amplitude). In one-particle quantum mechanics with $\hbar = 1$ and $\langle\mathbf p'|\mathbf p\rangle = (2\pi)^3\delta^3(\mathbf p' - \mathbf p)$, $\hat S = \mathbb 1 - 2\pi i\,\delta(E' - E)\,\hat T_{\rm QM}$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-2|QM Theorem §C10.1.2]], (6.11)) and to first order $\hat T_{\rm QM} \approx \hat V$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], 2), with $\langle\mathbf p'|\hat V|\mathbf p\rangle = \int d^3x\,e^{-i\mathbf p'\cdot\mathbf x}V(\mathbf x)e^{i\mathbf p\cdot\mathbf x} = \int d^3x\,e^{i(\mathbf p - \mathbf p')\cdot\mathbf x}V(\mathbf x) = \tilde V(\mathbf q)$, $\mathbf q = \mathbf p - \mathbf p'$, $\tilde V(\mathbf q) \equiv \int d^3x\,e^{i\mathbf q\cdot\mathbf x}V(\mathbf x)$ (Step 2 of [[§C6d.7 The Yukawa Potential#^der-c6d-7-5|Derivation §C6d.7.5]] is the same computation). In PS's notation $\hat S = \mathbb 1 + i\hat T$: $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\tilde V(\mathbf q)(2\pi)\delta(E_{\mathbf p'} - E_{\mathbf p})$, PS (4.124).
>
> **Step 2** (normalizations). The relativistic states carry $\sqrt{2E_{\mathbf p}} \approx \sqrt{2m}$ per particle ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); with four external particles the matrix element is $(\sqrt{2m})^4 = (2m)^2$ times that between nonrelativistically normalized states. These are the two factors $2m$ of [[§C6d.7 The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]]: "the factors of $2m$ … arise from our relativistic normalization conventions, and must be dropped when comparing to (4.124)". The remaining $(2\pi)^4\delta^4(p + k - p' - k')$ contains $\delta^3$ of the target's momentum, which "goes away when we integrate over the momentum of the target", leaving $(2\pi)\delta(E)$ (PS p. 122).
>
> **Step 3** (match). With the spins unchanged ($\delta^{ss'}\delta^{rr'} = 1$), $\frac{i\mathcal M}{(2m)^2} = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2} = -i\tilde V(\mathbf q)$, so $\tilde V(\mathbf q) = -\frac{g^2}{|\mathbf q|^2 + m_\phi^2}$, PS (4.125).
>
> **Step 4** (angular integral). $V(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}\,\frac{-g^2}{|\mathbf q|^2 + m_\phi^2}\,e^{-i\mathbf q\cdot\mathbf x}$ (the inverse of the transform of Step 1: $\int\frac{d^3q}{(2\pi)^3}e^{-i\mathbf q\cdot\mathbf x}\int d^3y\,e^{i\mathbf q\cdot\mathbf y}V(\mathbf y) = \int d^3y\,\delta^3(\mathbf y - \mathbf x)V(\mathbf y) = V(\mathbf x)$, [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]). In spherical coordinates for $\mathbf q$ with axis $\mathbf x$, $q = |\mathbf q|$, $c = \cos\theta$, $\mathbf q\cdot\mathbf x = qrc$: $d^3q = 2\pi q^2\,dq\,dc$, $\int_{-1}^1dc\,e^{-iqrc} = \frac{e^{-iqr} - e^{iqr}}{-iqr} = \frac{e^{iqr} - e^{-iqr}}{iqr}$ (the same value as with $e^{+iqrc}$: the integral is even in $\mathbf q$), and $\frac{2\pi}{(2\pi)^3} = \frac{1}{4\pi^2}$:
>
> $$
> V(\mathbf x) = \frac{-g^2}{4\pi^2}\int_0^\infty dq\,q^2\,\frac{e^{iqr} - e^{-iqr}}{iqr}\,\frac{1}{q^2 + m_\phi^2} = \frac{-g^2}{4\pi^2ir}\int_0^\infty dq\,\frac{q\,(e^{iqr} - e^{-iqr})}{q^2 + m_\phi^2} .
> $$
>
> **Step 5** (extend to the whole line). In the $e^{-iqr}$ term substitute $q = -q'$ ($dq = -dq'$; limits $0, \infty \to 0, -\infty$): $-\int_0^\infty dq\,\frac{qe^{-iqr}}{q^2 + m_\phi^2} = -\int_0^{-\infty}(-dq')\frac{(-q')e^{iq'r}}{q'^2 + m_\phi^2} = \int_{-\infty}^0dq'\,\frac{q'e^{iq'r}}{q'^2 + m_\phi^2}$. Hence, PS (4.126),
>
> $$
> V(\mathbf x) = \frac{-g^2}{4\pi^2ir}\int_{-\infty}^{\infty}dq\,\frac{q\,e^{iqr}}{q^2 + m_\phi^2} ,
> $$
>
> an improper integral converging at $\pm\infty$ by the oscillation of $e^{iqr}$, $r > 0$.
>
> **Step 6** (residue). For $r > 0$ close the contour in the upper half plane: the integrand is $e^{iqr}\cdot\frac{q}{q^2 + m_\phi^2}$ with $\frac{q}{q^2 + m_\phi^2} \to 0$ uniformly as $|q| \to \infty$, so the arc vanishes by Jordan's lemma ([[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]]). The poles are $q = \pm im_\phi$; inside is $q = +im_\phi$, with residue ([[§CA.5 Contour Integration#^thm-ca-5-4|Theorem §CA.5.4]]) $\frac{q\,e^{iqr}}{q + im_\phi}\big|_{q = im_\phi} = \frac{im_\phi e^{-m_\phi r}}{2im_\phi} = \frac12e^{-m_\phi r}$. By the residue theorem ([[§CA.5 Contour Integration#^thm-ca-5-5|Theorem §CA.5.5]]) the integral is $2\pi i\cdot\frac12e^{-m_\phi r} = i\pi e^{-m_\phi r}$, and
>
> $$
> V(r) = \frac{-g^2}{4\pi^2ir}\,i\pi\,e^{-m_\phi r} = -\frac{g^2}{4\pi r}\,e^{-m_\phi r} ,
> $$
>
> PS (4.127). Check by the forward transform: $\int d^3x\,e^{i\mathbf q\cdot\mathbf x}\,\frac{e^{-\mu r}}{r} = \frac{4\pi}{q^2 + \mu^2}$ ([[§C2.3 Wave Functions in Position and Momentum Space#^ex-c2-3-3|QM Example §C2.3.3]], there with $e^{-i\mathbf q\cdot\mathbf x}$; the integral depends on $|\mathbf q|$ only), so $-\frac{g^2}{4\pi}\cdot\frac{4\pi}{q^2 + m_\phi^2} = \tilde V$. The user's Lecture 18 update fills in the same transform (Derivation "The Fourier transform (filled in)"; the lecture stated the result without the computation) by the same three moves as Steps 4–6: the angular integral, written there as $\int_{-1}^1d\cos\theta\,e^{-iqr\cos\theta} = 2\sin(qr)/(qr)$, giving $\frac{1}{2\pi^2r}\int_0^\infty dq\,\frac{q\sin qr}{q^2 + m_\phi^2}$; the extension to $\frac{1}{4\pi^2ir}\int_{-\infty}^\infty dq\,\frac{q\,e^{iqr}}{q^2 + m_\phi^2}$; and the residue at $q = im_\phi$, with the result $\frac{e^{-m_\phi r}}{4\pi r}$. It is one computation, not a second route; Yu's is (8.283)–(8.284).
>
> **What the derivation shows.**
> - Attraction is the sign chain $(-ig)^2 = -g^2$, the spacelike exchange $q^2 = -|\mathbf q|^2$, and $\bar uu = +2m$; with the overall sign of $\mathcal M$ fixed by $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]]).
> - The range is the inverse mass of the exchanged particle; for $m_\phi \to 0$ the potential becomes $-g^2/4\pi r$, an attractive Coulomb-like force.
> - At zero mass the forward transform $\int d^3x\,e^{-i\mathbf q\cdot\mathbf x}\frac{1}{4\pi r}$ does not converge; with a cutoff $e^{-\varepsilon r}$ it is $\frac{1}{|\mathbf q|^2 + \varepsilon^2}$, the Yukawa form with $m_\phi = \varepsilon$, and the limit is $\frac{1}{|\mathbf q|^2}$ → [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-6|Theorem §C8.10.6]] (PHY 513, Problem Set 10, Problem 2(c)).

^der-c6d-7-3

*Uses:* [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-2|QM Theorem §C10.1.2]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C6d.7 The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.5 Contour Integration#^thm-ca-5-4|Theorem §CA.5.4]], [[§CA.5 Contour Integration#^thm-ca-5-5|Theorem §CA.5.5]], [[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]], [[§C2.3 Wave Functions in Position and Momentum Space#^ex-c2-3-3|QM Example §C2.3.3]]

> [!theorem] Theorem §C6d.7.4: Scalar Exchange Is Universally Attractive
> In the same limit the potential between a fermion and an antifermion, $f_1(p)\bar f_2(k) \to f_1(p')\bar f_2(k')$, and between two antifermions is again $V(r) = -\frac{g^2}{4\pi r}e^{-m_\phi r}$: attractive and of the same strength. In each case one diagram contributes, and the sign changes of the spinor products ($\bar vv = -2m$) and of the contraction pattern cancel:
>
> | process | chains | crossings | product |
> |---|---|---|---|
> | $f_1f_2 \to f_1f_2$ | $\bar u(p')u(p)$, $\bar u(k')u(k)$ | 2 ($+$) | $+(2m)(2m)$ |
> | $f_1\bar f_2 \to f_1\bar f_2$ | $\bar u(p')u(p)$, $\bar v(k)v(k')$ | 3 ($-$) | $-(2m)(-2m) = +(2m)^2$ |
> | $\bar f_1\bar f_2 \to \bar f_1\bar f_2$ | $\bar v(p)v(p')$, $\bar v(k)v(k')$ | 4 ($+$) | $+(-2m)(-2m) = +(2m)^2$ |
>
> The QED twin, in which the same two signs do not cancel, is [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-7|Theorem §C8.5.7]]; the crossing counts, as a statement for both theories, are [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-5|Theorem §C8.5.5]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* as [[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]]; for $f\bar f$ of one species the annihilation ($s$-channel) diagram is added, not treated here.
>
> *Source: PHY 513 Lecture 18, slides 26–29 (slide 29: "Yukawa: $f\bar f$ same sign as $ff/\bar f\bar f$"; the table row "Scalar (Yukawa): attract, attract") · the user's PHY 513 notes, Lecture 18 update, §18.7, "Antiparticles", Derivation "Particle–particle versus particle–antiparticle" and the sign table · Yu §8.4.3, eqs. (8.286)–(8.287) · PS §4.7, p. 122, eq. (4.128) and the contraction with $|\mathbf p, \mathbf k\rangle = a^\dagger_{\mathbf p}b^\dagger_{\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \langle0|b_{\mathbf k'}a_{\mathbf p'}$ ("three operator interchanges, so there is an overall factor of $-1$. This cancels the extra minus sign in (4.128)"), p. 123 ("the Yukawa potential is *universally attractive*") · the crossing counts written here*

^thm-c6d-7-4

> [!derivation]- Derivation
> **Step 1** ($f_1\bar f_2$). $|\mathbf p, \mathbf k\rangle = \sqrt{\cdots}\,\hat a^\dagger_{1\mathbf p}\hat b^\dagger_{2\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \sqrt{\cdots}\,\langle0|\hat b_{2\mathbf k'}\hat a_{1\mathbf p'}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). The $f_1$ line at $x$: $\hat{\bar\psi}_x$ emits $p'$ ($\bar u(p')$), $\hat\psi_x$ absorbs $p$ ($u(p)$). The $\bar f_2$ line at $y$: $\hat{\bar\psi}_y$ absorbs the incoming antifermion $k$ ($\bar v(k)$), $\hat\psi_y$ emits the outgoing one $k'$ ($v(k')$) ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]); read against the arrow the chain is $\bar v(k)v(k')$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). String: $\hat b_{\mathbf k'}(1)\,\hat a_{\mathbf p'}(2)\,\hat{\bar\psi}_x(3)\,\hat\psi_x(4)\,\hat{\bar\psi}_y(5)\,\hat\psi_y(6)\,\hat a^\dagger_{\mathbf p}(7)\,\hat b^\dagger_{\mathbf k}(8)$; pairs $(2, 3)$, $(4, 7)$, $(5, 8)$, $(1, 6)$; crossings $(4, 7)$–$(5, 8)$, $(4, 7)$–$(1, 6)$, $(5, 8)$–$(1, 6)$: three, sign $-$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]; PS: "three operator interchanges"). With [[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], $\bar v(k)v(k') \approx -2m$, and Steps 2–3 of [[§C6d.7 The Yukawa Potential#^der-c6d-7-2|Derivation §C6d.7.2]]: $i\mathcal M = (-1)\cdot\frac{ig^2}{|\mathbf q|^2 + m_\phi^2}\cdot2m\cdot(-2m) = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2}(2m)^2$, the same as for $f_1f_2$.
>
> **Step 2** ($\bar f_1\bar f_2$). $|\mathbf p, \mathbf k\rangle = \sqrt{\cdots}\,\hat b^\dagger_{1\mathbf p}\hat b^\dagger_{2\mathbf k}|0\rangle$, bra $\langle0|\hat b_{2\mathbf k'}\hat b_{1\mathbf p'}$. At $x$: $\hat{\bar\psi}_x$ absorbs $p$, $\hat\psi_x$ emits $p'$, chain $\bar v(p)v(p')$; at $y$: $\bar v(k)v(k')$. String $\hat b_{\mathbf k'}(1)\,\hat b_{\mathbf p'}(2)\,\hat{\bar\psi}_x(3)\,\hat\psi_x(4)\,\hat{\bar\psi}_y(5)\,\hat\psi_y(6)\,\hat b^\dagger_{\mathbf p}(7)\,\hat b^\dagger_{\mathbf k}(8)$; pairs $(3, 7)$, $(2, 4)$, $(5, 8)$, $(1, 6)$; crossings $(3, 7)$–$(2, 4)$, $(3, 7)$–$(5, 8)$, $(3, 7)$–$(1, 6)$, $(5, 8)$–$(1, 6)$: four, sign $+$. Product $(-2m)(-2m) = (2m)^2$: the same amplitude. PS: "there is an additional minus sign from changing the other $\bar uu$ into $\bar vv$, and the number of interchanges necessary to untangle the contractions is even".
>
> **Step 3** (potential). The amplitudes being equal, Steps 2–6 of [[§C6d.7 The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]] give the same $V(r)$.
>
> **What the derivation shows.**
> - Scalar exchange attracts everything: particles and antiparticles carry the same "scalar charge" $g$. Vector exchange (QED) repels like charges and attracts opposite ones, which is the sign check announced in Lecture 17 and carried out in Lecture 18: [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-7|Theorem §C8.5.7]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^pr-c8-5-8|Principle §C8.5.8]] (PS §4.8, p. 125).

^der-c6d-7-4

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.7 The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], [[§C6d.7 The Yukawa Potential#^der-c6d-7-2|Derivation §C6d.7.2]], [[§C6d.7 The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]]

## The lecture's form: the nonrelativistic amplitude and the Born comparison

> [!definition] Definition §C6d.7.1: Nonrelativistic Amplitude
> For a $2 \to 2$ amplitude in the nonrelativistic limit that conserves the spins, $i\mathcal M = i\mathcal M_{\rm NR}\cdot(2m_1\delta^{ss'})(2m_2\delta^{rr'})$, the **nonrelativistic amplitude** $\mathcal M_{\rm NR}$ is the amplitude with the relativistic wave-function factors $2m\,\delta$ omitted. The factors come from the relativistic normalization, in which $\bar uu = 2m$ rather than $1$: a nonrelativistic wave function is $e^{-ip\cdot x}$, not $\sqrt{2m}\,e^{-ip\cdot x}$. Equivalently, $\mathcal M_{\rm NR}$ is the amplitude between the states $|\mathbf p, s\rangle_{\rm NR} = \frac{1}{\sqrt{2E_{\mathbf p}}}|\mathbf p, s\rangle = \hat a^{s\dagger}_{\mathbf p}|0\rangle$ with $E_{\mathbf p} \approx m$, normalized as in one-particle quantum mechanics, $\langle\mathbf p'|\mathbf p\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$ ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]).
>
> *Model:* any theory with the relativistic normalization of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]; *applies:* nonrelativistic limit, lowest order in the momenta; a convention for comparing with nonrelativistic quantum mechanics.
>
> *Source: PHY 513 Lecture 18, slide 21 ("Convention: in NR QM $\psi \sim e^{-ipx}$ and not $\psi \sim \sqrt{2m}\,e^{-ipx}$. For comparisons with NR QM: Omit relativistic wavefunction factors $2m\delta^{ss'}$") · the user's PHY 513 notes, Lecture 18 update, §18.7 (after eq. (MYukNR); "$\mathcal M_{\rm NR}$ the amplitude without the $2m\,\delta$ factors") · PS §4.7, p. 122 ("must be dropped when comparing to (4.124)") · Yu §8.4.3, eqs. (8.251)–(8.254) ($\mathcal M_{\rm NR}$)*

^def-c6d-7-1

> [!theorem] Theorem §C6d.7.5: The Born Comparison: the Nonrelativistic Amplitude Is Minus the Fourier Transform of the Potential
> 1. *Quantum mechanics.* For one nonrelativistic particle in a potential $V(\mathbf x)$, the interaction-picture evolution operator to first order between plane waves (the Born approximation) is
>
> $$
> \langle\mathbf p'|i\hat T|\mathbf p\rangle = \langle\mathbf p'|\,T\bigl\{e^{-i\int dt\,\hat H_I}\bigr\}\,|\mathbf p\rangle\Big|_{\text{first order}} = -i\int d^3x\,dt\;e^{i(E_{\mathbf p'} - E_{\mathbf p})t + i(\mathbf p - \mathbf p')\cdot\mathbf x}\,V(\mathbf x) = -i\,\tilde V(\mathbf q)\;2\pi\delta(E_{\mathbf p'} - E_{\mathbf p}) ,
> $$
>
> with $\mathbf q = \mathbf p - \mathbf p'$ and $\tilde V(\mathbf q) = \int d^3x\,e^{i\mathbf q\cdot\mathbf x}V(\mathbf x)$: the $dt$ integral gives energy conservation, the $d^3x$ integral the Fourier transform of the potential at the momentum transfer.
> 2. *Field theory.* $\langle\mathbf p', \mathbf k'|i\hat T|\mathbf p, \mathbf k\rangle = i\mathcal M\,(2\pi)^4\delta^4(p + k - p' - k')$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). The energy part of $\delta^4$ plays the role of $2\pi\delta(E_{\mathbf p'} - E_{\mathbf p})$; the three-momentum part, $\mathbf p - \mathbf p' = \mathbf k' - \mathbf k$, is the recoil of the target, which potential scattering does not enforce: a fixed potential absorbs any momentum.
> 3. *Matching* what remains, with the nonrelativistic normalization of [[§C6d.7 The Yukawa Potential#^def-c6d-7-1|Def. §C6d.7.1]]:
>
> $$
> i\mathcal M_{\rm NR} = -i\,\tilde V(\mathbf q) .
> $$
>
> The amplitude is the potential in Fourier space, with a minus sign; this says what the tree diagram computes. The comparison is between amplitudes, not their squares, so the overall sign of $\mathcal M$ matters ([[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]]).
>
> *Equivalently,* this is the matching of [[§C6d.7 The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]] (Steps 1–3 of its derivation, PS (4.124)–(4.125), in the same conventions for $\mathbf q$ and $\tilde V$), stated on its own because Yukawa theory and QED both use it.
>
> *Model:* item 1: potential scattering, [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^mod-c10-1-1|QM Model §C10.1.1]], $\hbar = 1$, plane waves $\langle\mathbf x|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x}$; items 2–3: any theory of two distinguishable particles at lowest order, nonrelativistic limit; *applies:* first order in $V$ (the first Born approximation, [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]]); an identification of amplitudes, not a derivation of a two-body Schrödinger equation.
>
> *Source: PHY 513 Lecture 18, slide 22 ("Scattering in nonrelativistic QM (the Born Approximation): $\langle\vec p'|i\mathcal T|\vec p\rangle = \langle\vec p'|Te^{-i\int H_Idt}|\vec p\rangle = \ldots = -i\tilde V(\vec q)\,2\pi\delta(E_{\vec p'} - E_{\vec p})$ … Compare with scattering in QFT: $\langle\vec p', \vec k'|i\mathcal T|\vec p, \vec k\rangle = i\mathcal M(2\pi)^4\delta^4(p + k - p' - k')$, includes target recoil ⇒ $i\mathcal M = -i\tilde V(\vec q)$"), and transcript · the user's PHY 513 notes, Lecture 18 update, §18.7, "The Born approximation", eqs. (born), (MV) · PS §4.7, p. 121, eq. (4.124), p. 122 · Yu §8.4.3, eqs. (8.255)–(8.258) (his $\tilde V(\mathbf q) = \int d^3x\,V e^{-i\mathbf q\cdot\mathbf x}$ with $\mathbf q$ the incoming minus the outgoing momentum; the same for a central potential)*

^thm-c6d-7-5

> [!derivation]- Derivation
> **Step 1** (first order). In quantum mechanics with $\hat H = \hat H_0 + \hat V$, $\hat H_0 = \hat{\mathbf p}^2/2m$, the interaction-picture potential is $\hat H_I(t) = e^{i\hat H_0t}\hat Ve^{-i\hat H_0t}$ and $T\{e^{-i\int dt\,\hat H_I}\} = \mathbb 1 - i\int dt\,\hat H_I(t) + \cdots$, the same Dyson series as in field theory ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) with a potential in place of field operators. The term $\mathbb 1$ is the unscattered wave, $\langle\mathbf p'|\mathbf p\rangle$; the first-order term is $i\hat T$.
>
> **Step 2** (plane waves). $\hat H_0|\mathbf p\rangle = E_{\mathbf p}|\mathbf p\rangle$, so
>
> $$
> \langle\mathbf p'|\hat H_I(t)|\mathbf p\rangle = e^{iE_{\mathbf p'}t}\,\langle\mathbf p'|\hat V|\mathbf p\rangle\,e^{-iE_{\mathbf p}t} , \qquad \langle\mathbf p'|\hat V|\mathbf p\rangle = \int d^3x\;e^{-i\mathbf p'\cdot\mathbf x}\,V(\mathbf x)\,e^{i\mathbf p\cdot\mathbf x} = \int d^3x\;e^{i(\mathbf p - \mathbf p')\cdot\mathbf x}\,V(\mathbf x) = \tilde V(\mathbf p - \mathbf p') .
> $$
>
> **Step 3** (the time integral). $\int dt\,e^{i(E_{\mathbf p'} - E_{\mathbf p})t} = 2\pi\delta(E_{\mathbf p'} - E_{\mathbf p})$, an identity in $\mathcal S'$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]). Hence $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\,\tilde V(\mathbf q)\,2\pi\delta(E_{\mathbf p'} - E_{\mathbf p})$, item 1.
>
> **Step 4** (matching). Between nonrelativistically normalized states the field-theory element is $i\mathcal M_{\rm NR}(2\pi)^4\delta^4(p + k - p' - k')$ ([[§C6d.7 The Yukawa Potential#^def-c6d-7-1|Def. §C6d.7.1]]; Yu (8.255)). Its $(2\pi)^3\delta^3(\mathbf p + \mathbf k - \mathbf p' - \mathbf k')$ fixes the final momentum of the target and disappears when that momentum is integrated over (Step 2 of [[§C6d.7 The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]]; PS p. 122); what remains is $i\mathcal M_{\rm NR}\,2\pi\delta(E)$, to be compared with Step 3: $i\mathcal M_{\rm NR} = -i\tilde V(\mathbf q)$.
>
> **What the derivation shows.**
> - The decomposition $\hat S = \mathbb 1 + i\hat T$ is the same on both sides; the matching fixes the sign of $\mathcal M$ relative to the $\mathbb 1$ → [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|Theorem §C8.5.6]].
> - The same matching with the photon in place of the scalar gives the Coulomb potential → [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-3|Theorem §C8.5.3]].

^der-c6d-7-5

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6d.7 The Yukawa Potential#^def-c6d-7-1|Def. §C6d.7.1]], [[§C6d.7 The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]]

> [!caution] Caution: Slips on the Born-approximation slide
> Slide 22 writes the exponent $e^{-i(E_{\vec p} - E_{\vec p})t}$; the energies are those of $\mathbf p'$ and $\mathbf p$, $e^{i(E_{\mathbf p'} - E_{\mathbf p})t}$, as in [[§C6d.7 The Yukawa Potential#^thm-c6d-7-5|Theorem §C6d.7.5]]. The user's update records in addition that the handwritten notes exchange the bra and the ket, $\langle\mathbf p|i\hat T|\mathbf p'\rangle$, and label the operator $e^{i\int H_Idt}$; it is $\langle\mathbf p'|i\hat T|\mathbf p\rangle$ from $T\{e^{-i\int H_Idt}\}$.
>
> *Source: the user's PHY 513 notes, Lecture 18 update, §18.7, Caution "Slips in the slides and the handwritten notes" (second item) · PHY 513 Lecture 18, slide 22 · recorded in `qft-C/ERRATA.md`*

^cau-c6d-7-2

> [!remark] Remark: The same potential from a classical source
> Two static point sources $j = g[\delta^3(\mathbf x - \mathbf y_1) + \delta^3(\mathbf x - \mathbf y_2)]$ coupled to a free scalar lower the vacuum energy by $V(r) = -\frac{g^2}{4\pi r}e^{-mr}$ ([[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]], Coleman's "mesostatics"): the same function with the same sign. In the nonrelativistic limit a fermion at rest is such a source: $\bar\psi\psi \approx \psi^\dagger\psi$, the number density, so $g\bar\psi\psi\phi$ couples $\phi$ to a point charge $g$ for each particle; and $\bar vv = -2m$ together with the extra contraction sign make the antifermion's effective charge also $+g$ ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-4|Theorem §C6d.7.4]]). The static field of one such source is the Yukawa profile of [[§C2b.6 Green's Functions and Contours|§C2b.6]] (Connections there).
>
> *Source: Coleman pp. 95–96, as cited in [[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]] · PS §4.7, p. 122 · the identification written here*

^rem-c6d-7-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.5 Contour Integration#^thm-ca-5-4|Theorem §CA.5.4]], [[§CA.5 Contour Integration#^thm-ca-5-5|Theorem §CA.5.5]], [[§CA.5 Contour Integration#^thm-ca-5-6|Theorem §CA.5.6]] — the residue at $q = im_\phi$ and Jordan's lemma for closing above give $V(r)$ from $\tilde V(\mathbf q)$.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — $\int dt\,e^{i\omega t} = 2\pi\delta(\omega)$ in $\mathcal S'$: the energy delta of the Born amplitude; the same identity in three dimensions inverts $\tilde V(\mathbf q) = \int d^3x\,e^{i\mathbf q\cdot\mathbf x}V(\mathbf x)$.

> [!remark]- Connections
> - The Born approximation of quantum mechanics is the first-order $\hat S$-matrix between plane waves; QFT supplies the potential, QM the scattering theory built on it — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^ex-c10-1-1|QM Example §C10.1.1]] (the Born cross section of a Yukawa potential).
> - The range $1/m_\phi$ is the decay length $e^{-mr}$ of the spacelike Wightman function: the same Bessel-function tail at spacelike separation — [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]].
> - Yukawa's 1935 argument ran the other way, from the range of the nuclear force (about 1 fm) to the mass of the exchanged particle (about 200 MeV), the pion — [[§A7.1 Properties of Nuclei and Binding Energy|QM §A7.1]], [[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase|§C9.5]] (the pion is a pseudoscalar, coupled by $\bar\psi i\gamma^5\psi\phi$).
> - Exchange of a spin-1 particle gives a force that depends on the sign of the charges (Coulomb's law from QED) — [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-3|Theorem §C8.5.3]], [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-7|Theorem §C8.5.7]]; the table by the spin of the exchanged particle — [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^pr-c8-5-8|Principle §C8.5.8]]; PS §4.8.
