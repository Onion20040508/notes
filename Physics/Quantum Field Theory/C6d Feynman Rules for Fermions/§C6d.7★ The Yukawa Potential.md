---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, extension]
---
← [[§C6d.6 Momentum-Space Feynman Rules]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C9.1 Discrete Lorentz Transformations]] →

★ *Beyond PHY 513 so far: PS §4.7, pp. 121–123, read for Lecture 17 but not covered in it; the nonrelativistic limit was announced in Lecture 17 for the following week. Unstar when a lecture covers it.*

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 121–123, eqs. (4.121)–(4.128) (page images checked) · PHY 513 Lecture 17, transcript ("next week we'll do something where we actually care about the sign. We'll try to double check, for example, that two like charges in fact … repel") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The relative sign from antisymmetry" (the pointer to next week).*

What force does the exchange of the Yukawa scalar produce between two fermions? PS answer it by "descending from abstraction to concrete physics": take the $t$-channel amplitude of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] for two *distinguishable* fermions, keep the lowest order in the three-momenta ([[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]]), and compare with the Born approximation of nonrelativistic scattering ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]]). The result is the attractive Yukawa potential $V(r) = -\frac{g^2}{4\pi r}e^{-m_\phi r}$ ([[§C6d.7★ The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]]), the same between a fermion and an antifermion and between two antifermions ([[§C6d.7★ The Yukawa Potential#^thm-c6d-7-4|Theorem §C6d.7.4]]): scalar exchange is universally attractive. Here the overall sign of the amplitude matters, and it is fixed by the convention $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]). The classical-source route to the same potential is [[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]].

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two Dirac species $f_1$, $f_2$ of mass $m$, each coupled to $\phi$ with $g$ (so that only the $t$-channel diagram exists), at order $g^2$, free relativistic states over $|0\rangle$ with bras the adjoints of the kets ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], PS (4.118)); nonrelativistic kinematics, $|\mathbf p| \ll m$, to lowest order in the three-momenta.

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
> - ⚑ By-product: the factor $2m$ per spinor product is the relativistic normalization $2E \approx 2m$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] → [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]], Step 2.

^der-c6d-7-1

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-4|Theorem §C5a.11.4]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]

> [!theorem] Theorem §C6d.7.2: The Nonrelativistic Amplitude for Distinguishable Fermions
> For $f_1(p) + f_2(k) \to f_1(p') + f_2(k')$ in the setup of this section, with spins $s \to s'$ and $r \to r'$ and $\mathbf q = \mathbf p' - \mathbf p$, to lowest order in the three-momenta
>
> $$
> i\mathcal M = \frac{ig^2}{|\mathbf p' - \mathbf p|^2 + m_\phi^2}\;2m\,\delta^{ss'}\;2m\,\delta^{rr'} .
> $$
>
> Only the $t$-channel diagram of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] contributes, with sign $+$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* order $g^2$ (the lowest), free states with $(|f\rangle)^\dagger = \langle f|$, $|\mathbf p| \ll m$.
>
> *Source: PS §4.7, p. 121, eqs. (4.121)–(4.123) ("If the two interacting particles are distinguishable, only the first diagram in (4.119) contributes")*

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
> **Step 2** (kinematics, PS (4.121)). $p^0 = E_{\mathbf p} = m + O(\mathbf p^2)$, likewise for $p'$, so $(p' - p)^2 = (E_{\mathbf p'} - E_{\mathbf p})^2 - |\mathbf p' - \mathbf p|^2 = -|\mathbf p' - \mathbf p|^2 + O(\mathbf p^4)$.
>
> **Step 3** (assemble). With [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], $(-ig)^2 = -g^2$ and $\frac{i}{-|\mathbf q|^2 - m_\phi^2} = \frac{-i}{|\mathbf q|^2 + m_\phi^2}$:
>
> $$
> i\mathcal M = (-g^2)\cdot\frac{-i}{|\mathbf q|^2 + m_\phi^2}\cdot2m\,\delta^{ss'}\cdot2m\,\delta^{rr'} = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2}\,2m\,\delta^{ss'}\,2m\,\delta^{rr'} .
> $$
>
> **What the derivation shows.**
> - The sign of $i\mathcal M$ comes from $(-ig)^2 = -g^2$ times the $-$ of a spacelike exchange: $+ig^2/(\cdots)$, PS (4.123).

^der-c6d-7-2

*Uses:* [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]]

> [!theorem] Theorem §C6d.7.3: The Yukawa Potential
> Identifying the amplitude of [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]], stripped of the relativistic normalization, with the Born amplitude $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\tilde V(\mathbf q)\,(2\pi)\delta(E_{\mathbf p'} - E_{\mathbf p})$, $\mathbf q = \mathbf p' - \mathbf p$, gives
>
> $$
> \tilde V(\mathbf q) = \frac{-g^2}{|\mathbf q|^2 + m_\phi^2} , \qquad V(\mathbf x) = \int\frac{d^3q}{(2\pi)^3}\,\tilde V(\mathbf q)\,e^{i\mathbf q\cdot\mathbf x} = -\frac{g^2}{4\pi}\,\frac{1}{r}\,e^{-m_\phi r} , \qquad r = |\mathbf x| ,
> $$
>
> an **attractive** potential of range $1/m_\phi$ ($= \hbar/m_\phi c$, the Compton wavelength of the exchanged boson). Its sign is the chain $(-ig)^2 = -g^2$, the spacelike exchange $q^2 = -|\mathbf q|^2$, and $\bar uu = +2m$, with the overall sign of $\mathcal M$ fixed by $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]); for $m_\phi \to 0$ it becomes $-g^2/4\pi r$, an attractive Coulomb-like potential.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* order $g^2$, nonrelativistic limit, the Born approximation of one-particle quantum mechanics ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^mod-c10-1-1|QM Model §C10.1.1]]); the identification is PS's matching, not a derivation of a two-body Schrödinger equation.
>
> *Source: PS §4.7, pp. 121–122, eqs. (4.124)–(4.127) ("an attractive 'Yukawa potential', with range $1/m_\phi = \hbar/m_\phi c$ … Yukawa … worked backwards from the range of the force (about 1 fm) to predict the mass (about 200 MeV) of the required boson, the pion")*

^thm-c6d-7-3

> [!derivation]- Derivation
> **Step 1** (the Born amplitude). In one-particle quantum mechanics with $\hbar = 1$ and $\langle\mathbf p'|\mathbf p\rangle = (2\pi)^3\delta^3(\mathbf p' - \mathbf p)$, $\hat S = \mathbb 1 - 2\pi i\,\delta(E' - E)\,\hat T_{\rm QM}$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-2|QM Theorem §C10.1.2]], (6.11)) and to first order $\hat T_{\rm QM} \approx \hat V$ ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], 2), with $\langle\mathbf p'|\hat V|\mathbf p\rangle = \int d^3x\,e^{-i\mathbf p'\cdot\mathbf x}V(\mathbf x)e^{i\mathbf p\cdot\mathbf x} = \tilde V(\mathbf q)$, $\tilde V(\mathbf q) \equiv \int d^3x\,V(\mathbf x)e^{-i\mathbf q\cdot\mathbf x}$. In PS's notation $\hat S = \mathbb 1 + i\hat T$: $\langle\mathbf p'|i\hat T|\mathbf p\rangle = -i\tilde V(\mathbf q)(2\pi)\delta(E_{\mathbf p'} - E_{\mathbf p})$, PS (4.124).
>
> **Step 2** (normalizations). The relativistic states carry $\sqrt{2E_{\mathbf p}} \approx \sqrt{2m}$ per particle ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); with four external particles the matrix element is $(\sqrt{2m})^4 = (2m)^2$ times that between nonrelativistically normalized states. These are the two factors $2m$ of [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]]: "the factors of $2m$ … arise from our relativistic normalization conventions, and must be dropped when comparing to (4.124)". The remaining $(2\pi)^4\delta^4(p + k - p' - k')$ contains $\delta^3$ of the target's momentum, which "goes away when we integrate over the momentum of the target", leaving $(2\pi)\delta(E)$ (PS p. 122).
>
> **Step 3** (match). With the spins unchanged ($\delta^{ss'}\delta^{rr'} = 1$), $\frac{i\mathcal M}{(2m)^2} = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2} = -i\tilde V(\mathbf q)$, so $\tilde V(\mathbf q) = -\frac{g^2}{|\mathbf q|^2 + m_\phi^2}$, PS (4.125).
>
> **Step 4** (angular integral). In spherical coordinates for $\mathbf q$ with axis $\mathbf x$, $q = |\mathbf q|$, $c = \cos\theta$: $d^3q = 2\pi q^2\,dq\,dc$, $\int_{-1}^1dc\,e^{iqrc} = \frac{e^{iqr} - e^{-iqr}}{iqr}$, and $\frac{2\pi}{(2\pi)^3} = \frac{1}{4\pi^2}$:
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
> **Step 6** (residue). For $r > 0$ close the contour in the upper half plane: the integrand is $e^{iqr}\cdot\frac{q}{q^2 + m_\phi^2}$ with $\frac{q}{q^2 + m_\phi^2} \to 0$ uniformly as $|q| \to \infty$, so the arc vanishes by Jordan's lemma ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]). The poles are $q = \pm im_\phi$; inside is $q = +im_\phi$, with residue ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]]) $\frac{q\,e^{iqr}}{q + im_\phi}\big|_{q = im_\phi} = \frac{im_\phi e^{-m_\phi r}}{2im_\phi} = \frac12e^{-m_\phi r}$. By the residue theorem ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]) the integral is $2\pi i\cdot\frac12e^{-m_\phi r} = i\pi e^{-m_\phi r}$, and
>
> $$
> V(r) = \frac{-g^2}{4\pi^2ir}\,i\pi\,e^{-m_\phi r} = -\frac{g^2}{4\pi r}\,e^{-m_\phi r} ,
> $$
>
> PS (4.127). Check by the forward transform: $\int d^3x\,\frac{e^{-\mu r}}{r}e^{-i\mathbf q\cdot\mathbf x} = \frac{4\pi}{q^2 + \mu^2}$ ([[§C2.3 Wave Functions in Position and Momentum Space#^ex-c2-3-3|QM Example §C2.3.3]]), so $-\frac{g^2}{4\pi}\cdot\frac{4\pi}{q^2 + m_\phi^2} = \tilde V$.
>
> **What the derivation shows.**
> - Attraction is the sign chain $(-ig)^2 = -g^2$, the spacelike exchange $q^2 = -|\mathbf q|^2$, and $\bar uu = +2m$; with the overall sign of $\mathcal M$ fixed by $(|f\rangle)^\dagger = \langle f|$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]).
> - The range is the inverse mass of the exchanged particle; for $m_\phi \to 0$ the potential becomes $-g^2/4\pi r$, an attractive Coulomb-like force.

^der-c6d-7-3

*Uses:* [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-2|QM Theorem §C10.1.2]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-2|Theorem §C6d.7.2]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§C2.3 Wave Functions in Position and Momentum Space#^ex-c2-3-3|QM Example §C2.3.3]]

> [!theorem] Theorem §C6d.7.4: Scalar Exchange Is Universally Attractive
> In the same limit the potential between a fermion and an antifermion, $f_1(p)\bar f_2(k) \to f_1(p')\bar f_2(k')$, and between two antifermions is again $V(r) = -\frac{g^2}{4\pi r}e^{-m_\phi r}$: attractive and of the same strength. In each case one diagram contributes, and the sign changes of the spinor products ($\bar vv = -2m$) and of the contraction pattern cancel:
>
> | process | chains | crossings | product |
> |---|---|---|---|
> | $f_1f_2 \to f_1f_2$ | $\bar u(p')u(p)$, $\bar u(k')u(k)$ | 2 ($+$) | $+(2m)(2m)$ |
> | $f_1\bar f_2 \to f_1\bar f_2$ | $\bar u(p')u(p)$, $\bar v(k)v(k')$ | 3 ($-$) | $-(2m)(-2m) = +(2m)^2$ |
> | $\bar f_1\bar f_2 \to \bar f_1\bar f_2$ | $\bar v(p)v(p')$, $\bar v(k)v(k')$ | 4 ($+$) | $+(-2m)(-2m) = +(2m)^2$ |
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with two species; *applies:* as [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-3|Theorem §C6d.7.3]]; for $f\bar f$ of one species the annihilation ($s$-channel) diagram is added, not treated here.
>
> *Source: PS §4.7, p. 122, eq. (4.128) and the contraction with $|\mathbf p, \mathbf k\rangle = a^\dagger_{\mathbf p}b^\dagger_{\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \langle0|b_{\mathbf k'}a_{\mathbf p'}$ ("three operator interchanges, so there is an overall factor of $-1$. This cancels the extra minus sign in (4.128)"), p. 123 ("the Yukawa potential is *universally attractive*") · the crossing counts written here*

^thm-c6d-7-4

> [!derivation]- Derivation
> **Step 1** ($f_1\bar f_2$). $|\mathbf p, \mathbf k\rangle = \sqrt{\cdots}\,\hat a^\dagger_{1\mathbf p}\hat b^\dagger_{2\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \sqrt{\cdots}\,\langle0|\hat b_{2\mathbf k'}\hat a_{1\mathbf p'}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). The $f_1$ line at $x$: $\hat{\bar\psi}_x$ emits $p'$ ($\bar u(p')$), $\hat\psi_x$ absorbs $p$ ($u(p)$). The $\bar f_2$ line at $y$: $\hat{\bar\psi}_y$ absorbs the incoming antifermion $k$ ($\bar v(k)$), $\hat\psi_y$ emits the outgoing one $k'$ ($v(k')$) ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]); read against the arrow the chain is $\bar v(k)v(k')$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). String: $\hat b_{\mathbf k'}(1)\,\hat a_{\mathbf p'}(2)\,\hat{\bar\psi}_x(3)\,\hat\psi_x(4)\,\hat{\bar\psi}_y(5)\,\hat\psi_y(6)\,\hat a^\dagger_{\mathbf p}(7)\,\hat b^\dagger_{\mathbf k}(8)$; pairs $(2, 3)$, $(4, 7)$, $(5, 8)$, $(1, 6)$; crossings $(4, 7)$–$(5, 8)$, $(4, 7)$–$(1, 6)$, $(5, 8)$–$(1, 6)$: three, sign $-$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]; PS: "three operator interchanges"). With [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], $\bar v(k)v(k') \approx -2m$, and Steps 2–3 of [[§C6d.7★ The Yukawa Potential#^der-c6d-7-2|Derivation §C6d.7.2]]: $i\mathcal M = (-1)\cdot\frac{ig^2}{|\mathbf q|^2 + m_\phi^2}\cdot2m\cdot(-2m) = \frac{ig^2}{|\mathbf q|^2 + m_\phi^2}(2m)^2$, the same as for $f_1f_2$.
>
> **Step 2** ($\bar f_1\bar f_2$). $|\mathbf p, \mathbf k\rangle = \sqrt{\cdots}\,\hat b^\dagger_{1\mathbf p}\hat b^\dagger_{2\mathbf k}|0\rangle$, bra $\langle0|\hat b_{2\mathbf k'}\hat b_{1\mathbf p'}$. At $x$: $\hat{\bar\psi}_x$ absorbs $p$, $\hat\psi_x$ emits $p'$, chain $\bar v(p)v(p')$; at $y$: $\bar v(k)v(k')$. String $\hat b_{\mathbf k'}(1)\,\hat b_{\mathbf p'}(2)\,\hat{\bar\psi}_x(3)\,\hat\psi_x(4)\,\hat{\bar\psi}_y(5)\,\hat\psi_y(6)\,\hat b^\dagger_{\mathbf p}(7)\,\hat b^\dagger_{\mathbf k}(8)$; pairs $(3, 7)$, $(2, 4)$, $(5, 8)$, $(1, 6)$; crossings $(3, 7)$–$(2, 4)$, $(3, 7)$–$(5, 8)$, $(3, 7)$–$(1, 6)$, $(5, 8)$–$(1, 6)$: four, sign $+$. Product $(-2m)(-2m) = (2m)^2$: the same amplitude. PS: "there is an additional minus sign from changing the other $\bar uu$ into $\bar vv$, and the number of interchanges necessary to untangle the contractions is even".
>
> **Step 3** (potential). The amplitudes being equal, Steps 2–6 of [[§C6d.7★ The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]] give the same $V(r)$.
>
> **What the derivation shows.**
> - Scalar exchange attracts everything: particles and antiparticles carry the same "scalar charge" $g$. Vector exchange (QED) repels like charges and attracts opposite ones, which is the sign check announced in Lecture 17 for the following week (C6d, QED rules, and C8 Quantum electrodynamics, planned; PS §4.8, p. 125).

^der-c6d-7-4

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|Theorem §C6d.7.1]], [[§C6d.7★ The Yukawa Potential#^der-c6d-7-2|Derivation §C6d.7.2]], [[§C6d.7★ The Yukawa Potential#^der-c6d-7-3|Derivation §C6d.7.3]]

> [!remark] Remark: The same potential from a classical source
> Two static point sources $j = g[\delta^3(\mathbf x - \mathbf y_1) + \delta^3(\mathbf x - \mathbf y_2)]$ coupled to a free scalar lower the vacuum energy by $V(r) = -\frac{g^2}{4\pi r}e^{-mr}$ ([[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]], Coleman's "mesostatics"): the same function with the same sign. In the nonrelativistic limit a fermion at rest is such a source: $\bar\psi\psi \approx \psi^\dagger\psi$, the number density, so $g\bar\psi\psi\phi$ couples $\phi$ to a point charge $g$ for each particle; and $\bar vv = -2m$ together with the extra contraction sign make the antifermion's effective charge also $+g$ ([[§C6d.7★ The Yukawa Potential#^thm-c6d-7-4|Theorem §C6d.7.4]]). The static field of one such source is the Yukawa profile of [[§C2b.5 Green's Functions and Contours|§C2b.5]] (Connections there).
>
> *Source: Coleman pp. 95–96, as cited in [[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]] · PS §4.7, p. 122 · the identification written here*

^rem-c6d-7-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]] — the residue at $q = im_\phi$ and Jordan's lemma for closing above give $V(r)$ from $\tilde V(\mathbf q)$.

> [!remark]- Connections
> - The Born approximation of quantum mechanics is the first-order $\hat S$-matrix between plane waves; QFT supplies the potential, QM the scattering theory built on it — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-6|QM Theorem §C10.1.6]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^ex-c10-1-1|QM Example §C10.1.1]] (the Born cross section of a Yukawa potential).
> - The range $1/m_\phi$ is the decay length $e^{-mr}$ of the spacelike Wightman function: the same Bessel-function tail at spacelike separation — [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]].
> - Yukawa's 1935 argument ran the other way, from the range of the nuclear force (about 1 fm) to the mass of the exchanged particle (about 200 MeV), the pion — [[§A7.1 Properties of Nuclei and Binding Energy|QM §A7.1]], [[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase|§C9.5]] (the pion is a pseudoscalar, coupled by $\bar\psi i\gamma^5\psi\phi$).
> - Exchange of a spin-1 particle gives a force that depends on the sign of the charges (Coulomb's law from QED) — C6d, QED rules (planned); PS §4.8.
