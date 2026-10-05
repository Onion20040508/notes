---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.7 Wick Rotation and the Two-Point Family]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C3.1 Groups, Algebras and Representations of Rotations]] →

*Sources: the user's PHY 513 notes, Ch. 6 §6.13 · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), Part C (on the slides, not reached in class) · Peskin & Schroeder §2.4, pp. 32–33, eqs. (2.61)–(2.66).*

A classical source $j(x)$ acts on the free quantum field for a finite time ([[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]]). Starting from the vacuum, how many particles does it leave behind, with what energy, and in what state? The first physical application of a Green's function: the retarded function of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]] solves the operator equation, the late-time field turns out to be the free field with shifted annihilation operators, and the in-vacuum is then a coherent state of the outgoing particles ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]]). Only the on-shell Fourier components of the source radiate.

*Conventions* ([[Larsen PHY 513]]): $\tilde j(p) = \int d^4y\,e^{ip\cdot y}j(y)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]), evaluated on shell, $p^0 = E_{\mathbf p}$; Heisenberg picture throughout, so the state is the in-vacuum $|0\rangle$ of the free field before the source acts.

> [!theorem] Theorem §C2b.8.1: The Late-Time Field
> With $\phi_0$ the free field ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]) and the field equal to it before the source acts,
>
> $$
> \phi(x) = \phi_0(x) + i\int d^4y\,D_R(x - y)\,j(y) .
> $$
>
> Once $x^0$ is later than the support of $j$,
>
> $$
> \phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(b_{\mathbf p}\,e^{-ip\cdot x} + b_{\mathbf p}^\dagger\,e^{ip\cdot x}\Bigr), \qquad b_{\mathbf p} = a_{\mathbf p} + \frac{i\,\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\Big|_{p^0 = E_{\mathbf p}},
> $$
>
> a free field whose annihilation operators are shifted by on-shell $c$-numbers; $[b_{\mathbf p}, b_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 (Derivation "The late-time field and the particles produced", Steps 1–3) · PHY 513 Lecture 6, "Particle Production by Classical Source I–II" · PS §2.4, eqs. (2.63)–(2.64)*

^thm-c2b-8-1

> [!derivation]- Derivation
> **Step 1** (the retarded solution). $j$ is a $c$-number, so $\phi = \phi_0 + i\int D_R\,j$ solves the operator equation $(\partial^2 + m^2)\phi = j$ (for a test-function source, $i\int D_R\,j = i\,D_R[j(x - \cdot)]$ is smooth and solves it exactly, [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]] with the fundamental solution $D_R$, [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]) ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]], with $(\partial^2 + m^2)\phi_0 = 0$ by [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]). Before the source acts, $D_R(x - y) = 0$ for every $y$ in its support (as a distribution: $\operatorname{supp}D_R \subseteq \{\xi^0 \ge 0\}$, [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]) ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]), so $\phi = \phi_0$ there.
>
> ⚑ By-product: the retarded function is not chosen for convenience; the question fixes the state before the source acts, and that is the retarded boundary condition → [[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-2|Remark: The boundary condition was physics]].
>
> **Step 2** (insert the retarded function in modes; the inner $d^3p$ integral converges for no $y$ by itself, and the formula is read paired with $j$, as made explicit in Step 4). By Theorem §C2b.5.5 and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]],
>
> $$
> \phi(x) = \phi_0(x) + i\int d^4y\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\theta(x^0 - y^0)\Bigl(e^{-ip\cdot(x - y)} - e^{ip\cdot(x - y)}\Bigr)j(y), \qquad p^0 = E_{\mathbf p} .
> $$
>
> **Step 3** (late times). If $x^0$ is later than every $y^0$ in the support of $j$, then $\theta(x^0 - y^0) = 1$ wherever the integrand is nonzero, and the step function drops out.
>
> **Step 4** (exchange and transform). $j$ is smooth with compact support, so $\tilde j$ decreases faster than any power and the $d^4y$ and $d^3p$ integrals may be exchanged ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]). (Sense: with Step 3 the step function is $1$ on the support of $j$, so this is $D_W$ and $D_W(-\cdot)$ acting on the test function $j(x - \cdot)$, $\xi$-integral first, [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 2; the exchange is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]] for a wave packet, and [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]] supplies the decay.) Each $d^4y$ integral is a four-dimensional transform:
>
> $$
> \int d^4y\,e^{-ip\cdot(x - y)}j(y) = e^{-ip\cdot x}\,\tilde j(p), \qquad \int d^4y\,e^{ip\cdot(x - y)}j(y) = e^{ip\cdot x}\int d^4y\,e^{-ip\cdot y}j(y) = e^{ip\cdot x}\,\overline{\tilde j(p)},
> $$
>
> the last because $j$ is real ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4). Both are evaluated at $p^0 = E_{\mathbf p}$.
>
> ⚑ By-product: only the on-shell values $\tilde j(E_{\mathbf p}, \mathbf p)$ enter → [[§C2b.8 Particle Production by a Classical Source#^rem-c2b-8-1|Remark: Only the on-shell part of the source radiates]].
>
> **Step 5** (sort by frequency). With $\frac{i}{2E_{\mathbf p}} = \frac{1}{\sqrt{2E_{\mathbf p}}}\cdot\frac{i}{\sqrt{2E_{\mathbf p}}}$,
>
> $$
> \phi - \phi_0 = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\frac{i\,\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\,e^{-ip\cdot x} + \frac{-i\,\overline{\tilde j(p)}}{\sqrt{2E_{\mathbf p}}}\,e^{ip\cdot x}\Bigr).
> $$
>
> Adding $\phi_0 = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E}}(a_{\mathbf p}e^{-ip\cdot x} + a_{\mathbf p}^\dagger e^{ip\cdot x})$, the coefficient of $e^{-ip\cdot x}$ is $b_{\mathbf p} = a_{\mathbf p} + i\tilde j/\sqrt{2E}$, and that of $e^{ip\cdot x}$ is $a_{\mathbf p}^\dagger - i\overline{\tilde j}/\sqrt{2E} = b_{\mathbf p}^\dagger$.
>
> **Step 6** (the algebra is unchanged). Shifting by $c$-numbers does not change commutators: $[b_{\mathbf p}, b_{\mathbf q}^\dagger] = [a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, an identity of distributions in $(\mathbf p, \mathbf q)$, the shift $i\tilde j(p)/\sqrt{2E_{\mathbf p}}$ being a smooth function ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> **What the derivation shows.**
> - After the source has acted the field is free again, with new ladder operators: the out-particles are the quanta of $b_{\mathbf p}^\dagger$.
> - The expectation value $\langle0|\phi|0\rangle = i\int D_R\,j$ is the classical retarded field of the source ([[§C2b.5 Green's Functions and Contours#^rem-c2b-5-4|§C2b.5, Remark: Measurable response is a retarded commutator]]).
> - Used next: Theorems §C2b.8.2–§C2b.8.3.

^der-c2b-8-1

*Uses:* [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]

> [!theorem] Theorem §C2b.8.2: The Final State Is a Coherent State
> The in-vacuum is an eigenstate of every late-time annihilation operator,
>
> $$
> b_{\mathbf p}|0\rangle = \frac{i\,\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\,|0\rangle ,
> $$
>
> so with respect to the out-particles it is the coherent state of [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]] with $\eta_{\mathbf p} = i\tilde j(E_{\mathbf p}, \mathbf p)$. The number of particles produced is Poisson distributed.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 ("The final state is a coherent state")*

^thm-c2b-8-2

> [!derivation]- Derivation
> **Step 1** (eigenvalue). $a_{\mathbf p}|0\rangle = 0$, so $b_{\mathbf p}|0\rangle = \bigl(a_{\mathbf p} + \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\bigr)|0\rangle = \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}|0\rangle$.
>
> **Step 2** (identify). By Theorem §C2b.8.1, Step 6, the $b$'s obey the vacuum algebra, so the construction of [[§C2a.6 Coherent States and the Classical Field|§C2a.6]] applies with $b$ in place of $a$. A state with $b_{\mathbf p}|\psi\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}|\psi\rangle$ for every $\mathbf p$ is, up to a phase, the coherent state $|\{\eta\}\rangle$ built on the $b$-vacuum ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]); comparing with Step 1, $\eta_{\mathbf p} = i\tilde j(p)$.
>
> **Step 3** (statistics). By [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]] the number of $b$-quanta is Poisson distributed, with mean $\int\frac{d^3p}{(2\pi)^3}\frac{|\eta_{\mathbf p}|^2}{2E_{\mathbf p}}$, which is Theorem §C2b.8.3.
>
> ⚑ By-product: $\bar N < \infty$ is required for the coherent state to be normalizable in the out-Fock space; for a smooth source of finite duration it holds → [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]] (and Example §C2b.8.1).
>
> **What the derivation shows.**
> - A classical source produces classical radiation, in the precise sense of [[§C2a.6 Coherent States and the Classical Field|§C2a.6]]: the out-state has a definite mean field, the classical retarded field, and vacuum-sized fluctuations ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]]).

^der-c2b-8-2

*Uses:* [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]]

> [!theorem] Theorem §C2b.8.3: Energy and Number of Particles Produced
> After the source has acted, the energy above the vacuum and the mean number of particles are
>
> $$
> \Delta E = \int\frac{d^3p}{(2\pi)^3}\,\frac12\bigl|\tilde j(p)\bigr|^2, \qquad \bar N = \int\frac{d^3p}{(2\pi)^3}\,\frac{\bigl|\tilde j(p)\bigr|^2}{2E_{\mathbf p}}, \qquad p^0 = E_{\mathbf p}:
> $$
>
> a mean density $|\tilde j(p)|^2/2E_{\mathbf p}$ of particles per $d^3p/(2\pi)^3$, each carrying energy $E_{\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 (Derivation, Step 4) · PHY 513 Lecture 6, "Particle Production by Classical Source: Interpretation" · PS §2.4, eqs. (2.65)–(2.66)*

^thm-c2b-8-3

> [!derivation]- Derivation
> **Step 1** (the late-time Hamiltonian). After the source is off, $H$ has the free form ([[§C2a.2 Mode Expansion and the Mode Algebra#^mod-c2a-2-1|Model §C2a.2.1]]) in the late-time field, whose mode operators are the $b$'s (Theorem §C2b.8.1). The computation of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] uses only the mode expansion and the algebra, both unchanged, so
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,b_{\mathbf p}^\dagger b_{\mathbf p} + E_0 = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\Bigl(a_{\mathbf p}^\dagger - \frac{i\,\overline{\tilde j(p)}}{\sqrt{2E_{\mathbf p}}}\Bigr)\Bigl(a_{\mathbf p} + \frac{i\,\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\Bigr) + E_0 .
> $$
>
> ⚑ By-product: the zero-point constant $E_0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]) is the same before and after and cancels from the energy *added* → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]].
>
> **Step 2** (expand the product, all four terms). $a^\dagger a + a^\dagger\frac{i\tilde j}{\sqrt{2E}} - \frac{i\overline{\tilde j}}{\sqrt{2E}}a + \frac{|\tilde j|^2}{2E}$.
>
> **Step 3** (expectation value in $|0\rangle$). $\langle0|a^\dagger a|0\rangle = 0$ and $\langle0|a|0\rangle = 0$ because $a|0\rangle = 0$; $\langle0|a^\dagger|0\rangle = 0$ because $\langle0|a^\dagger = 0$. Only the product of the two $c$-numbers survives, with no $\delta^3(\mathbf 0)$, since no reordering was needed; the remaining integral is finite because $j$ is a test function ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]]):
>
> $$
> \langle0|H|0\rangle - E_0 = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,\frac{|\tilde j(p)|^2}{2E_{\mathbf p}} = \int\frac{d^3p}{(2\pi)^3}\,\frac12|\tilde j(p)|^2 .
> $$
>
> **Step 4** (number). The out-number operator is $N = \int\frac{d^3p}{(2\pi)^3}b_{\mathbf p}^\dagger b_{\mathbf p}$; Steps 2–3 without the factor $E_{\mathbf p}$ give $\bar N = \int\frac{d^3p}{(2\pi)^3}\frac{|\tilde j(p)|^2}{2E_{\mathbf p}}$.
>
> **What the derivation shows.**
> - The energy and the number are quadratic in the source: the field responds linearly, the energy is the square of the response.
> - PS call $|\tilde j|^2/2E_{\mathbf p}$ a probability density for creating a particle in mode $\mathbf p$; by Theorem §C2b.8.2 it is the mean of a Poisson distribution per mode, which is a probability only when small.

^der-c2b-8-3

*Uses:* [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^mod-c2a-2-1|Model §C2a.2.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]

> [!theorem] Theorem §C2b.8.4: The Source Is a Test Function; Why $\bar N$ Is Finite
> Let $j \in \mathcal D(\mathbb R^4)$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), smooth and nonzero only in a bounded region of spacetime ([[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]]; $j \in \mathcal S(\mathbb R^4)$ suffices).
> 1. $\tilde j \in \mathcal S(\mathbb R^4)$, so on the shell $|\tilde j(E_{\mathbf p}, \mathbf p)| \le C_N(1 + |\mathbf p|)^{-N}$ for every $N$. Hence $\bar N$ and $\Delta E$ of [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]] are finite, and the out-state of [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]] is a normalizable coherent state.
> 2. The classical field $i\int d^4y\,D_R(x - y)j(y) = i\,D_R[j(x - \cdot)]$ is the distribution $D_R$ acting on a test function: a smooth solution of $(\partial^2 + m^2)\phi = j$ ([[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]]).
> 3. $\bar N = \|\phi_0(j)|0\rangle\|^2$ with $\phi_0(j) = \int d^4x\,j(x)\phi_0(x)$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]): finite exactly when the on-shell restriction of $\tilde j$ is a normalizable one-particle wave function. A source with $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde j|^2 = \infty$, such as an instantaneous point source $g\,\delta^4(x)$, produces infinitely many particles.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 ("$j$ smooth and of finite duration"), Ch. 6 §6.2 (sources as test functions) · PHY 513, Problem Set 4, Problem 0 · stated here as a condition on test functions*

^thm-c2b-8-4

> [!derivation]- Derivation
> **Step 1** (the transform of a test function). $\mathcal D \subset \mathcal S$, and the transform maps $\mathcal S$ onto $\mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1): $|\tilde j(k)| \le C_N(1 + |k^0| + |\mathbf k|)^{-N}$. On the shell $|k| \ge |\mathbf p|$, which gives the bound of part 1.
>
> **Step 2** (finite number and energy). With $N = 2$, $\bar N = \int\frac{d^3p}{(2\pi)^3}\frac{|\tilde j(p)|^2}{2E_{\mathbf p}} \le \frac{C_2^2}{2(2\pi)^3}\int d^3p\,\frac{(1 + |\mathbf p|)^{-4}}{E_{\mathbf p}} < \infty$, since $1/E_{\mathbf p} \le 1/|\mathbf p|$ is integrable near $\mathbf p = 0$ in three dimensions; $\Delta E = \int\frac{d^3p}{(2\pi)^3}\frac12|\tilde j(p)|^2 < \infty$ in the same way. The coherent state $e^{-\bar N/2}\exp\{\cdots\}|0\rangle$ of [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]] has norm $1$ precisely when $\bar N < \infty$. Part 1.
>
> **Step 3** (the classical field). $D_R$ is a fundamental solution ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]), $j \in \mathcal D$, so by [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]] $x \mapsto i\,D_R[j(x - \cdot)]$ is smooth, each derivative falling on $j$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), and $(\partial^2 + m^2)$ of it is $i\cdot(-i)\,j = j$. Part 2.
>
> **Step 4** (the one-particle norm). By [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], 1, with $\tilde j(p) = \int d^4x\,j(x)e^{ip\cdot x}$ as in this section's conventions, $\|\phi_0(j)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde j(p)|^2 = \bar N$.
>
> **Step 5** (when it fails). For $j = g\,\delta^4(x)$, $\tilde j = g$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3) and $\bar N = g^2\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \infty$, the divergence of $\phi(x)|0\rangle$ (Step 3 of Derivation §C2b.1.2). The point source of Example §C2b.8.1 is not a test function in space, but its smooth time profile makes $\tilde j = g\,e^{-E_{\mathbf p}^2T^2/2}$ decay on the shell, because there the frequency grows with $|\mathbf p|$; as $T \to 0$ it tends to $g\,\delta^4(x)$ and $\bar N \simeq g^2/8\pi^2T^2 \to \infty$. Part 3.
>
> **What the derivation shows.**
> - Every finite answer of this section rests on $j$ being a test function: the on-shell transform of $j$ must be a normalizable wave packet.
> - Smoothness in time matters most: on the mass shell, decay in energy is decay in momentum.

^der-c2b-8-4

*Uses:* [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]

> [!remark] Remark: Only the on-shell part of the source radiates
> $\tilde j$ enters only at $p^0 = E_{\mathbf p} \ge m$: a source must have Fourier components at frequencies that real particles can carry, "in resonance with on-mass-shell waves" (PS). A static source, whose transform is concentrated at $p^0 = 0 < m$, produces no particles at all; it surrounds itself with a field, the Yukawa cloud of range $1/m$ ([[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]]), but emits nothing. A slowly switched source is nearly static and produces exponentially few particles (Example §C2b.8.1).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 (first remark) · PS §2.4, p. 33*

^rem-c2b-8-1

> [!remark] Remark: The boundary condition was physics
> The retarded function was forced by the question, which specifies the state before the source acts. The same calculation with $D_F$ would answer a different question, one with conditions imposed in both the past and the future. This is the concrete instance of [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: Which Green's function when]]. The calculation is exact because the coupling is linear in $\phi$ and the source is classical; with a quantum source, a field of its own, the same structure becomes the first interaction (QFT C6, planned), and PS return to it in their Problem 4.1 and, for photons, in bremsstrahlung.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 (third remark, "Where the course goes next") · PS §2.4, p. 33*

^rem-c2b-8-2

> [!example] Example §C2b.8.1: A Point Source Switched On and Off
> Let $j(x) = g\,\delta^3(\mathbf x)\,\frac{e^{-t^2/2T^2}}{\sqrt{2\pi}\,T}$: a point source of total strength $g$ (dimension $1/\text{mass}$), switched on and off over a time $T$. Find the mean number of particles produced, and its limits $mT \ll 1$ and $mT \gg 1$.
>
> **Step 1** (the transform). $\tilde j(p) = \int dt\,e^{iEt}\frac{e^{-t^2/2T^2}}{\sqrt{2\pi}T}\int d^3y\,e^{-i\mathbf p\cdot\mathbf y}g\,\delta^3(\mathbf y) = g\,e^{-E^2T^2/2}$, by the Gaussian transform ([[§C4.1 Propagators#^thm-c4-1-3|QM Theorem §C4.1.3]] with $a = 1/2T^2$, $b = iE$), at $E = E_{\mathbf p}$; the spatial integral is δ acting on the smooth function $e^{-i\mathbf p\cdot\mathbf y}$ ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]), which is why a source that is not a test function in space still has a transform here.
>
> **Step 2** (the number). By Theorem §C2b.8.3, with $d^3p = 4\pi p^2dp$ and $p\,dp = E\,dE$, so $\frac{p^2dp}{E} = \sqrt{E^2 - m^2}\,dE$:
>
> $$
> \bar N = \int\frac{d^3p}{(2\pi)^3}\frac{g^2e^{-E^2T^2}}{2E} = \frac{g^2}{4\pi^2}\int_m^\infty dE\,\sqrt{E^2 - m^2}\,e^{-E^2T^2} .
> $$
>
> **Step 3** (a Bessel function again). Substitute $E = m\cosh u$: $\sqrt{E^2 - m^2}\,dE = m^2\sinh^2u\,du$. With $\cosh^2u = \frac12(1 + \cosh2u)$, $\sinh^2u = \frac12(\cosh2u - 1)$ and $v = 2u$, and $z \equiv \frac12m^2T^2$,
>
> $$
> \int_m^\infty\sqrt{E^2 - m^2}\,e^{-E^2T^2}dE = m^2e^{-z}\int_0^\infty\frac{\cosh v - 1}{2}\,e^{-z\cosh v}\,\frac{dv}{2} = \frac{m^2}{4}e^{-z}\bigl[K_1(z) - K_0(z)\bigr]
> $$
>
> ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]). So $\bar N = \frac{g^2m^2}{16\pi^2}\,e^{-z}\bigl[K_1(z) - K_0(z)\bigr]$.
>
> **Step 4** (sudden switching, $mT \ll 1$). $K_1(z) \simeq 1/z$ dominates ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3): $\bar N \simeq \frac{g^2m^2}{16\pi^2}\cdot\frac{2}{m^2T^2} = \frac{g^2}{8\pi^2T^2}$, independent of $m$ and growing without bound as $T \to 0$.
>
> **Step 5** (adiabatic switching, $mT \gg 1$). $K_1 - K_0 \simeq \sqrt{\pi/2z}\,e^{-z}\bigl[(1 + \frac{3}{8z}) - (1 - \frac{1}{8z})\bigr] = \sqrt{\pi/2z}\,e^{-z}/2z$ (Theorem §CA.5.3, 2), so $\bar N \simeq \frac{g^2}{16\pi^2}\cdot\frac{\sqrt\pi}{mT^3}\,e^{-m^2T^2}$: exponentially small.
>
> The source's frequency spectrum $e^{-\omega^2T^2/2}$ must reach $\omega \ge m$ to make a particle; a source switched on slowly compared with $1/m$ leaves the field in its vacuum, the field-theory form of the adiabatic theorem ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-6|QM Theorem §C9.4.6]]), while a sudden one excites every mode ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-5|QM Theorem §C9.4.5]]).
>
> *Source: worked here, applying the user's PHY 513 notes, Ch. 6 §6.13 (the remark that a static source produces nothing) and PS eq. (2.66); checked numerically*

^ex-c2b-8-1

![[ph-qft-c2-7-1.svg]]
*Mean number of particles produced by the point source of Example §C2b.8.1, in units of $g^2m^2/16\pi^2$, against the switching time $T$ in units of the Compton time $1/m$. Fast switching follows $2/(mT)^2$; slow switching is exponentially suppressed, $\sqrt\pi\,e^{-(mT)^2}/(mT)^3$, because the source then has no Fourier components on the mass shell.*

> [!remark]- Connections
> - The out-state is the field version of a driven oscillator: a classical force on a quantum oscillator displaces its ground state into a coherent state, mode by mode ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]]); here one such displacement $i\tilde j(p)/\sqrt{2E_{\mathbf p}}$ per $\mathbf p$, with the forced classical response being the retarded field ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]]).
> - Only Fourier components at the natural frequencies are absorbed: the field-theory form of resonance, and the reason a static charge does not radiate while an accelerated one does (radiation: [[§B11.4★ Radiation from a Point Charge|EM §B11.4★]]; photons from a classical current, PS Problem 4.1, and bremsstrahlung, QFT C8, planned).
> - The sudden/adiabatic dichotomy of Example §C2b.8.1 is the time-dependent perturbation theory of [[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits|QM §C9.4]] applied to infinitely many oscillators; Fermi's golden rule is the small-$\bar N$, long-time limit of the same $|\tilde j(E_{\mathbf p})|^2$.
> - The Poisson statistics of the produced particles is that of a laser or a radio transmitter, classical sources of coherent radiation ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]]; [[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]]).
> - The Bessel function $K_1 - K_0$ of Example §C2b.8.1 comes from the same integral representation as the two-point function ([[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^def-ca-5-1|Def. §CA.5.1]]), because both integrate over the mass shell with hyperbolic variables.
> - [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]] (test functions) is the class the classical source belongs to; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]] (the transform preserves $\mathcal S$) turns that into the on-shell decay of $\tilde j$ that makes $\bar N$, $\Delta E$ and the coherent out-state finite (Theorem §C2b.8.4).
> - [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]] (convolution with a fundamental solution) is the statement that the retarded field $i\int D_R\,j$ is smooth and solves the sourced equation.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]] and [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]] (exchanging the $y$- and $p$-integrals) turn $D_R$ acting on $j$ into the on-shell transform $\tilde j(E_{\mathbf p}, \mathbf p)$.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]] (reality, $\tilde j(-p) = \overline{\tilde j(p)}$) pairs the creation and annihilation shifts; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]] ($\tilde\delta = 1$) shows the instantaneous point source is outside the class.
