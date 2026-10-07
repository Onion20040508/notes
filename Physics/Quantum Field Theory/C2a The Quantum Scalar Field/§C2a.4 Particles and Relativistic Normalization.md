---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.3 Energy, Momentum and the Zero-Point Energy]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.5 The Complex Scalar Field and Its Charge]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.7–4.9 · PHY 513 Lecture 4 (Larsen), Part C and "Details on Normalization"; Problem Set 3, Problem 1, with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.3 · Yu Zhao-Huan, 量子场论讲义, §2.3.4 · the user's pre-course notes, §3.3.*

What do the states of the free real field describe? The ladder relations of [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]] ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]]) and the Fock space of identical particles of Quantum Mechanics ([[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]]) answer: particles, the states of the Fock space generated from the vacuum ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|Principle §C2a.3.3]], postulated in §C2a.3 where the zero-point energy first needs it). What the field adds to second quantization is the continuum and relativity: one-particle states labelled by a continuous momentum, normalized so that the normalization is Lorentz invariant, with the invariant measure $d^3p/(2\pi)^32E_{\mathbf p}$, and created at a point by the field itself. The steps are [[P1 Canonical Quantization#^p1-6|P1, steps 6–7]].

## Particles

> [!theorem] Theorem §C2a.4.1: The Spectrum: Particles
> With $:\!H\!:$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]) and $\mathbf P$:
> 1. $:\!H\!: \ge 0$; $|0\rangle$ is the ground state, $:\!H\!:|0\rangle = \mathbf P|0\rangle = 0$.
> 2. $a^\dagger_{\mathbf p_1}\cdots a^\dagger_{\mathbf p_n}|0\rangle$ has energy $E_{\mathbf p_1} + \dots + E_{\mathbf p_n}$ and momentum $\mathbf p_1 + \dots + \mathbf p_n$: $n$ free particles of mass $m$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$.
> 3. $N = \int\frac{d^3p}{(2\pi)^3}\,a^\dagger_{\mathbf p}a_{\mathbf p}$ counts particles: its eigenvalue on the state of part 2 is $n$, and $[N, H] = [N, \mathbf P] = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Principle "Fields give particles") · PHY 513 Lecture 4, Part C · PS §2.3, p. 22 · Yu §2.3.4, eqs. (2.150)–(2.169)*

^thm-c2a-4-1

> [!derivation]- Derivation
> **1. Positivity.** For any state $|\psi\rangle$, $\langle\psi|a^\dagger_{\mathbf p}a_{\mathbf p}|\psi\rangle = \|a_{\mathbf p}\psi\|^2 \ge 0$, and $E_{\mathbf p} \ge m > 0$ (for a wave-packet state $\psi$, $a_{\mathbf p}\psi$ is a vector for each $\mathbf p$, a Schwartz function of $\mathbf p$, so the integral below converges: [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 2), so
>
> $$
> \langle\psi|:\!H\!:|\psi\rangle = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,\|a_{\mathbf p}\psi\|^2 \ge 0 ,
> $$
>
> with equality iff $a_{\mathbf p}|\psi\rangle = 0$ for (almost) all $\mathbf p$, i.e. $|\psi\rangle \propto |0\rangle$ by the uniqueness in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|Principle §C2a.3.3]].
>
> **2. The vacuum.** Every term of $:\!H\!:$ and of $\mathbf P$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]) ends in an annihilator, so both annihilate $|0\rangle$.
>
> **3. One particle.** $H a^\dagger_{\mathbf p}|0\rangle = [H, a^\dagger_{\mathbf p}]|0\rangle + a^\dagger_{\mathbf p}H|0\rangle = E_{\mathbf p}a^\dagger_{\mathbf p}|0\rangle + 0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]]); likewise $\mathbf P a^\dagger_{\mathbf p}|0\rangle = \mathbf p\,a^\dagger_{\mathbf p}|0\rangle$.
>
> **4. $n$ particles, by induction.** Suppose $H a^\dagger_{\mathbf p_2}\cdots a^\dagger_{\mathbf p_n}|0\rangle = (E_{\mathbf p_2} + \dots + E_{\mathbf p_n})\,a^\dagger_{\mathbf p_2}\cdots a^\dagger_{\mathbf p_n}|0\rangle$. Then
>
> $$
> H a^\dagger_{\mathbf p_1}a^\dagger_{\mathbf p_2}\cdots|0\rangle = \bigl(a^\dagger_{\mathbf p_1}H + E_{\mathbf p_1}a^\dagger_{\mathbf p_1}\bigr)a^\dagger_{\mathbf p_2}\cdots|0\rangle = (E_{\mathbf p_1} + E_{\mathbf p_2} + \dots + E_{\mathbf p_n})\,a^\dagger_{\mathbf p_1}\cdots a^\dagger_{\mathbf p_n}|0\rangle ,
> $$
>
> and the same for $\mathbf P$. ⚑ By-product: $E_{\mathbf p}^2 - \mathbf p^2 = m^2$ for each quantum: the Lagrangian's $m$ is the particle mass → [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-1|Remark: What the spectrum says]].
>
> **5. Counting.** Steps 2–4 of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-7|Derivation §C2a.3.7]] with $1$ in place of $E_{\mathbf q}$ give $[N, a^\dagger_{\mathbf p}] = a^\dagger_{\mathbf p}$, so $N$ has eigenvalue $n$ on the state of part 2. For the commutators, $[a^\dagger_{\mathbf p}a_{\mathbf p}, a^\dagger_{\mathbf q}a_{\mathbf q}] = a^\dagger_{\mathbf p}[a_{\mathbf p}, a^\dagger_{\mathbf q}]a_{\mathbf q} + a^\dagger_{\mathbf q}[a^\dagger_{\mathbf p}, a_{\mathbf q}]a_{\mathbf p} = (2\pi)^3\delta^3(\mathbf p - \mathbf q)\bigl(a^\dagger_{\mathbf p}a_{\mathbf q} - a^\dagger_{\mathbf q}a_{\mathbf p}\bigr)$, which vanishes on the support of the delta (the operator factor vanishes at $\mathbf p = \mathbf q$; multiplication of δ by a smooth function, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1, read in matrix elements between wave packets); $N$, $:\!H\!:$ and $\mathbf P$ are integrals of these number densities with numerical weights, so they commute.
>
> **What the derivation shows**
> - Positivity of $:\!H\!:$ makes $|0\rangle$ the ground state; no negative-energy states exist, although the expansion contains negative frequencies.
> - Energies and momenta of the quanta add: the quanta are free relativistic particles of mass $m$; particle number is conserved in the free theory.
> - Statistics are [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]; the picture is the figure below.

^der-c2a-4-1

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-3|Principle §C2a.3.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!theorem] Theorem §C2a.4.2: Bose Symmetry and Multiple Occupation
> 1. Multiparticle states are symmetric: $a^\dagger_{\mathbf p_1}a^\dagger_{\mathbf p_2}|0\rangle = a^\dagger_{\mathbf p_2}a^\dagger_{\mathbf p_1}|0\rangle$, and
>
> $$
> \langle0|a_{\mathbf q_2}a_{\mathbf q_1}a^\dagger_{\mathbf p_1}a^\dagger_{\mathbf p_2}|0\rangle = (2\pi)^6\bigl[\delta^3(\mathbf q_1 - \mathbf p_1)\delta^3(\mathbf q_2 - \mathbf p_2) + \delta^3(\mathbf q_1 - \mathbf p_2)\delta^3(\mathbf q_2 - \mathbf p_1)\bigr] :
> $$
>
> the quanta obey Bose–Einstein statistics.
> 2. One mode holds any number of quanta: for a normalized wave packet, $c^\dagger = \int\frac{d^3p}{(2\pi)^3}\psi(\mathbf p)a^\dagger_{\mathbf p}$ with $\int\frac{d^3p}{(2\pi)^3}|\psi|^2 = 1$, $[c, c^\dagger] = 1$ and $(c^\dagger)^N|0\rangle/\sqrt{N!}$ is a normalized state of $N$ particles all in the same one-particle state.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 ("Bose statistics"; "Macroscopic occupation") · PS §2.3, p. 22 · Yu §2.3.4, eqs. (2.170)–(2.172); the packet form written here*

^thm-c2a-4-2

> [!derivation]- Derivation
> **1. Symmetry.** $[a^\dagger_{\mathbf p_1}, a^\dagger_{\mathbf p_2}] = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); apply to $|0\rangle$. ⚑ By-product: Bose statistics is inherited from $[\phi(\mathbf x), \phi(\mathbf y)] = 0$, not imposed; anticommutators would give fermions → [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-1|Remark: What the spectrum says]].
>
> **2. Move $a_{\mathbf q_1}$ to the right.** $a_{\mathbf q_1}a^\dagger_{\mathbf p_1} = a^\dagger_{\mathbf p_1}a_{\mathbf q_1} + (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_1)$, then $a_{\mathbf q_1}a^\dagger_{\mathbf p_2}|0\rangle = (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_2)|0\rangle$:
>
> $$
> a_{\mathbf q_1}a^\dagger_{\mathbf p_1}a^\dagger_{\mathbf p_2}|0\rangle = (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_2)\,a^\dagger_{\mathbf p_1}|0\rangle + (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_1)\,a^\dagger_{\mathbf p_2}|0\rangle .
> $$
>
> **3. Then $a_{\mathbf q_2}$.** $\langle0|a_{\mathbf q_2}a^\dagger_{\mathbf p}|0\rangle = (2\pi)^3\delta^3(\mathbf q_2 - \mathbf p)$ for $\mathbf p = \mathbf p_1, \mathbf p_2$ gives the two terms of the statement: direct and exchanged. *Sense:* an identity of distributions in the four momenta; paired with wave packets ($a^\dagger(h_i)$, $a(g_i)$ of [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]) it reads $\langle0|a(g_2)a(g_1)a^\dagger(h_1)a^\dagger(h_2)|0\rangle = \langle g_1, h_1\rangle\langle g_2, h_2\rangle + \langle g_1, h_2\rangle\langle g_2, h_1\rangle$ with $\langle g, h\rangle = \int\frac{d^3p}{(2\pi)^3}\overline gh$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 1).
>
> **4. One packet mode.** $[c, c^\dagger] = \int\frac{d^3p\,d^3q}{(2\pi)^6}\psi^{\ast}(\mathbf p)\psi(\mathbf q)[a_{\mathbf p}, a^\dagger_{\mathbf q}] = \int\frac{d^3p}{(2\pi)^3}|\psi(\mathbf p)|^2 = 1$, the delta eliminating $\mathbf q$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 1, with $g = h = \psi$). So $c$, $c^\dagger$ obey the single-oscillator algebra, and $\|(c^\dagger)^N|0\rangle\|^2 = N!$ ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], 4). ⚑ By-product: with a sharp momentum, $(a^\dagger_{\mathbf p})^N|0\rangle$ has norm proportional to $\delta^3(\mathbf 0)^N$ → [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]].
>
> **What the derivation shows**
> - The exchanged term in step 3 is Bose symmetry seen in an overlap.
> - Any normalized packet is a single oscillator of the field; this is the mode a coherent state occupies ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]]).
> - Used next: macroscopic occupation and the classical limit ([[§C2a.6 Coherent States and the Classical Field|§C2a.6]]).

^der-c2a-4-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]

![[ph-qft-c2-2-1.svg]]
*The spectrum of the free field in the plane of total momentum and energy (Theorem §C2a.4.1). The vacuum is a point; one-particle states lie on the mass hyperbola, one state per $\mathbf P$; $n$-particle states fill the region above $E = \sqrt{\mathbf P^2 + n^2m^2}$, reached when all $n$ particles move together with $\mathbf P/n$ each. Adapted from the user's PHY 513 notes, Ch. 4.*

> [!remark] Remark: What the spectrum says
> - **The Lagrangian's $m$ is the particle's mass.** $a^\dagger_{\mathbf p}|0\rangle$ has exactly the energy and momentum of a relativistic particle of mass $m$ ([[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-3|REL Theorem §B2.1.3]]), and the label $\mathbf p$, introduced as a Fourier variable, is the eigenvalue of $\mathbf P$. The isolated hyperbola in the figure is how a particle is recognized in a spectrum; with interactions it returns as an isolated pole of the two-point function ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-7|★ Remark: With interactions, the Källén–Lehmann representation]]; QFT C10, planned).
> - **Statistics were not imposed.** Bose symmetry ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]) comes from $[\phi(\mathbf x), \phi(\mathbf y)] = 0$, inherited by the $a^\dagger$'s; fermions need anticommutators, a different quantization ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]). Many quanta in one mode, $(a^\dagger_{\mathbf p})^N|0\rangle$, is the beginning of the laser; whether such a state is a classical wave is [[§C2a.6 Coherent States and the Classical Field|§C2a.6]].
> - **One field, any number of particles.** This is the reason for field theory: particle number is not conserved in relativistic processes, and one field operator creates and destroys any number of quanta. In $\phi$ the plane wave $e^{-ip\cdot x}$ (the wave) multiplies $a_{\mathbf p}$ (the particle): wave–particle duality in one expression.
> - **Not a density.** $\mathbf x$ is a label on the field operator, not an eigenvalue; there is a momentum operator and a Hamiltonian but no position or time operator.
>
> *Source: the user's PHY 513 notes, Ch. 4 §§4.7–4.9 · PHY 513 Lecture 4, Part C ("Comments") · PS §2.3, p. 22*

^rem-c2a-4-1

> [!remark] Remark: Why |0⟩ is the vacuum
> - **Ground state.** By Theorem §C2a.4.1, 1, no state has lower energy; $H|0\rangle = 0$ is the normal-ordering choice of zero, not a physical statement.
> - **Poincaré invariant.** $P^\mu|0\rangle = 0$ and $J^{\mu\nu}|0\rangle = 0$, since every generator is normal ordered and bilinear, with an annihilator on the right. This is what makes $\langle0|\phi(x)\phi(y)|0\rangle$ a function of $x - y$ alone ([[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]).
> - **Unique, given the $a$'s.** Any state annihilated by all $a_{\mathbf p}$ is a multiple of $|0\rangle$ (irreducibility). What is not unique is the choice of the $a$'s ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-5|★ Remark: Other mode functions]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Principle "Why |0⟩ is the vacuum")*

^rem-c2a-4-2

> [!caution] Caution: Plane-wave states are not normalizable
> $\langle\mathbf p|\mathbf p\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0)$ is infinite: like $|x'\rangle$ and $|p'\rangle$ in quantum mechanics ([[§C2.1 Continuous Spectra and Position Eigenkets#^pr-c2-1-2|QM Principle §C2.1.2]], [[§37 Position Eigenstates and Continuous Resolutions#^prop-37-4|556 Prop. §37.4]]), $|\mathbf p\rangle$ is not in $\mathcal F$. Genuine one-particle states are wave packets $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\psi(\mathbf p)\,|\mathbf p\rangle$ with $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\psi(\mathbf p)|^2 < \infty$ (Yu, Exercise 2.3). Correspondingly $a^\dagger_{\mathbf p}$ and $\phi(\mathbf x)$ are operator-valued distributions, meaningful after smearing with test functions; that is why products of fields at one point need normal ordering and why $\delta^3(\mathbf 0)$ appeared in $H$. The precise statements: [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]] (and [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points") · Yu §2.3.4, after eq. (2.163)*

^cau-c2a-4-1

Quantum Mechanics constructed the Fock space from a given one-particle space and defined $a$, $a^\dagger$ on occupation-number kets ([[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]], [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]]). Here the order is reversed: the $a^\dagger$ come from the field, and the one-particle space $\mathcal H_1$ is whatever $a^\dagger_{\mathbf p}|0\rangle$ spans, with a continuous label. Yu §2.3.4 builds the same space constructively (one-particle, multiparticle and occupation-number states, each property checked from the commutators), and Weinberg's *Quantum Theory of Fields* §4.2 goes the other way, defining the Fock space first and the operators on it afterwards, as Quantum Mechanics does. What is new is how to normalize it.

## Relativistic normalization

> [!definition] Definition §C2a.4.1: Relativistic Normalization
> The relativistically normalized states are
>
> $$
> |\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,a^\dagger_{\mathbf p}|0\rangle, \qquad \langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}\,(2\pi)^3\delta^3(\mathbf p - \mathbf q), \qquad |\mathbf p_1, \dots, \mathbf p_n\rangle = \sqrt{2E_{\mathbf p_1}}\cdots\sqrt{2E_{\mathbf p_n}}\;a^\dagger_{\mathbf p_1}\cdots a^\dagger_{\mathbf p_n}|0\rangle  .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9, eq. (relnorm) · PHY 513 Lecture 4, Part C · PS §2.3, eqs. (2.35)–(2.36) · Yu §2.3.4, eqs. (2.152), (2.157)*

^def-c2a-4-1

> [!definition] Definition §C2a.4.2: Invariant Measure and One-Particle Completeness
> The **invariant measure** on the mass shell, and the resolution of the identity on one-particle states that it gives with the states of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]:
>
> $$
> \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \int\frac{d^4p}{(2\pi)^4}\,2\pi\,\delta(p^2 - m^2)\,\theta(p^0), \qquad \mathbb 1_{1\text{-particle}} = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,|\mathbf p\rangle\langle\mathbf p| .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9, eq. (invmeasure) · PS §2.3, eqs. (2.39)–(2.40) · Yu §2.3.4, eqs. (2.161), (2.167)*

^def-c2a-4-2

> [!theorem] Theorem §C2a.4.3: The Invariant Measure
> Under proper orthochronous Lorentz transformations, for $m > 0$:
> 1. $\theta(p^0)$ is invariant on the mass shell $p^2 = m^2$;
> 2. for every scalar $F$, $\displaystyle\int\frac{d^3p}{2E_{\mathbf p}}\,F(E_{\mathbf p}, \mathbf p) = \int d^4p\;\delta(p^2 - m^2)\,\theta(p^0)\,F(p)$, so $d^3p/2E_{\mathbf p}$ is an invariant measure.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 · PHY 513 Lecture 4 ("Details on Normalization"); Problem Set 3, Problem 1, with the course solution · PS §2.3, eq. (2.40) · Yu §2.3.4, eqs. (2.158)–(2.161)*

^thm-c2a-4-3

> [!derivation]- Derivation
> **1. On the shell, $p$ is timelike.** $p^2 = m^2 > 0$ means $(p^0)^2 = \mathbf p^2 + m^2 > \mathbf p^2$, so $|\mathbf p| < |p^0|$.
>
> **2. Rotations** act on $\mathbf p$ only and leave $p^0$, hence $\theta(p^0)$, unchanged.
>
> **3. Boosts, and every proper orthochronous Λ.** By step 1 the shell vector is timelike, and proper orthochronous transformations preserve the sign of the time component of timelike vectors; this is proved once, by Cauchy–Schwarz for a boost and for $\Lambda^{-1}$, together with the decomposition into a boost times a rotation, in [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]], 3. Hence $\theta(p'^0) = \theta(p^0)$ on the shell. ⚑ By-product: off the shell, for spacelike $p$, the sign of $p^0$ is frame dependent; the restriction to the shell is what makes "positive energy" invariant, the momentum-space form of [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]] → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], 1. ⚑ By-product: time reversal ($\Lambda^0{}_0 < 0$) is excluded; the measure is invariant only under the orthochronous group → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]] (its hypothesis).
>
> **4. The four-dimensional measure.** Under $p \to p' = \Lambda p$, $d^4p' = |\det\Lambda|\,d^4p$, and $\Lambda^{\mathsf T}g\Lambda = g$ gives $(\det\Lambda)^2 = 1$; so $d^4p$ is invariant ([[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]]). $p^2$ is a scalar, so $\delta(p^2 - m^2)$ is invariant (as a distribution: δ composed with the invariant function $p^2 - m^2$, whose gradient $2p$ does not vanish on the shell, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3, with invariance in the sense of [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
>
> **5. Do the $p^0$ integral.** With $f(p^0) = (p^0)^2 - E_{\mathbf p}^2$, roots $p^0 = \pm E_{\mathbf p}$, $|f'(\pm E_{\mathbf p})| = 2E_{\mathbf p}$, the composition rule ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]]; as an identity in $\mathcal S'$, the limit of nascent deltas, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2) gives
>
> $$
> \delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}, \qquad \int dp^0\,\delta(p^2 - m^2)\,\theta(p^0)\,F(p) = \frac{F(E_{\mathbf p}, \mathbf p)}{2E_{\mathbf p}} ,
> $$
>
> $\theta$ removing the root $-E_{\mathbf p}$. *Sense:* $\theta(p^0)\delta(p^2 - m^2)$ is a tempered distribution on $\mathbb R^4$, acting as $F \mapsto \int d^3p\,F(E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1); the product $\theta\cdot\delta$ is defined because $\theta(p^0)$ is smooth near the shell for $m > 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2).
>
> **6. Conclude.** Integrating step 5 over $\mathbf p$ gives part 2 (for $F$ a test function on $\mathbb R^4$, or any $F$ integrable against the shell measure); its right side is invariant by steps 3–4, so the left side is. Restoring the conventional factors, $\int\frac{d^4p}{(2\pi)^4}2\pi\,\delta(p^2 - m^2)\theta(p^0) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}$.
>
> **What the derivation shows**
> - The invariant measure is the volume element of the upper mass hyperboloid; $1/2E_{\mathbf p}$ is the Jacobian of the delta.
> - Assumptions used: $m > 0$ (timelike shell), proper orthochronous transformations.
> - Used next: the invariance of $\langle\mathbf p|\mathbf q\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]) and every mode integral of [[§C2b.2 The Wightman Function|§C2b.2]]–[[§C2b.4 Microcausality and the Commutator Function|§C2b.4]].

^der-c2a-4-3

*Uses:* [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, step 7]]

> [!theorem] Theorem §C2a.4.4: Invariance of the Relativistic Normalization
> $2E_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q)$ is Lorentz invariant, hence so are $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and the one-particle resolution of the identity of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]; $\delta^3(\mathbf p - \mathbf q)$ alone is not: $\delta^3(\mathbf p - \mathbf q) = (E_{\mathbf p'}/E_{\mathbf p})\,\delta^3(\mathbf p' - \mathbf q')$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 · PS §2.3, eqs. (2.34)–(2.36), (2.39) · Yu §2.3.4, eqs. (2.155)–(2.157), (2.162)–(2.163)*

^thm-c2a-4-4

> [!derivation]- Derivation
> **1. A reproducing kernel.** For a scalar test function $g$ on the shell ($g \in \mathcal S$, so that $\delta^3$ acts on it, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]), insert $1 = 2E_{\mathbf p}/2E_{\mathbf p}$:
>
> $$
> g(\mathbf q) = \int d^3p\,\delta^3(\mathbf p - \mathbf q)\,g(\mathbf p) = \int\frac{d^3p}{2E_{\mathbf p}}\,\bigl[2E_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q)\bigr]\,g(\mathbf p) .
> $$
>
> **2. Invariance.** The left side is a scalar and $d^3p/2E_{\mathbf p}$ is invariant ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]); the kernel that reproduces every $g$ against an invariant measure is unique (a distribution is fixed by its action on test functions, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]), so $2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ is invariant in the sense of [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]].
>
> **3. The overlap.** By [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] and [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]],
>
> $$
> \langle\mathbf p|\mathbf q\rangle = \sqrt{4E_{\mathbf p}E_{\mathbf q}}\,\langle0|a_{\mathbf p}a^\dagger_{\mathbf q}|0\rangle = \sqrt{4E_{\mathbf p}E_{\mathbf q}}\,\langle0|\bigl(a^\dagger_{\mathbf q}a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf p - \mathbf q)\bigr)|0\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q) ,
> $$
>
> the first term vanishing because $a_{\mathbf p}|0\rangle = 0$ and $\sqrt{4E_{\mathbf p}E_{\mathbf q}} = 2E_{\mathbf p}$ on the support (a smooth factor times δ, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1).
>
> **4. Completeness on one-particle states.** $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\mathbf p\rangle\langle\mathbf p|\mathbf q\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\mathbf p\rangle\,2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q) = |\mathbf q\rangle$: the measure and the normalization cancel exactly. Both factors are invariant, so the resolution of the identity is. *Sense:* $|\mathbf q\rangle$ is not a vector, so this is shorthand for the identity $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\langle h|\mathbf p\rangle\langle\mathbf p|g\rangle = \langle h|g\rangle$ between wave packets → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 3.
>
> **5. The bare delta.** Write $\delta^3(\mathbf p - \mathbf q) = \frac{1}{2E_{\mathbf p}}\bigl[2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)\bigr]$; the bracket is invariant, so in the transformed frame $\delta^3(\mathbf p - \mathbf q) = \frac{2E_{\mathbf p'}}{2E_{\mathbf p}}\delta^3(\mathbf p' - \mathbf q')$. ⚑ By-product: the normalization $\langle\mathbf p|\mathbf q\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ of $a^\dagger_{\mathbf p}|0\rangle$ is frame dependent → [[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-3|Remark: why √(2E_p)]].
>
> **What the derivation shows**
> - The factor $2E_{\mathbf p}$ in the normalization is the inverse of the Jacobian in the measure; together they are invariant.
> - Used next: the Lorentz action $U(\Lambda)|\mathbf p\rangle = |\Lambda\mathbf p\rangle$ ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11|Theorem §C3.5.11]]) and every amplitude built from $|\mathbf p\rangle$.

^der-c2a-4-4

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

> [!derivation]- Derivation (second route: boosting the delta function directly)
> **1. The boost.** Along $z$ with velocity $\beta$: $p_3' = \gamma(p_3 + \beta E)$, $E' = \gamma(E + \beta p_3)$, $p_1' = p_1$, $p_2' = p_2$, with $E = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ on the shell.
>
> **2. Derivative.** On the shell $dE/dp_3 = p_3/E$, so
>
> $$
> \frac{dp_3'}{dp_3} = \gamma\Bigl(1 + \beta\frac{dE}{dp_3}\Bigr) = \gamma\,\frac{E + \beta p_3}{E} = \frac{E'}{E} .
> $$
>
> **3. Delta of a function.** The transverse deltas are unchanged; for the third, $\delta(p_3 - q_3) = \delta(p_3' - q_3')\,|dp_3'/dp_3|$ (composition rule, [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], with the single root $p_3 = q_3$; in $\mathcal S'$, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2, since $p_3'$ is a smooth function of $p_3$ with nonzero derivative $E'/E$). Hence $\delta^3(\mathbf p - \mathbf q) = \delta^3(\mathbf p' - \mathbf q')\,E'/E$, i.e. $E\,\delta^3(\mathbf p - \mathbf q) = E'\,\delta^3(\mathbf p' - \mathbf q')$.
>
> **What the derivation shows**
> - The physical reason: a box of volume $V$ at rest has volume $V/\gamma$ in a boosted frame, so a density per unit volume cannot be invariant, and $E$ compensates.
> - A general Lorentz transformation is a boost times a rotation, and rotations leave $E\,\delta^3$ manifestly invariant.

^der-c2a-4-4b

*Uses:* [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-3|WO Theorem §B4.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, step 7]]

> [!definition] Definition §C2a.4.3: One-Particle Wave Packet
> For $g \in \mathcal S(\mathbb R^3)$, the **wave packet** with momentum profile $g$ is
>
> $$
> |g\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,g(\mathbf p)\,|\mathbf p\rangle = a^\dagger\bigl(g/\sqrt{2E}\bigr)|0\rangle ,
> $$
>
> with $a^\dagger(\cdot)$ as in [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]] and $(g/\sqrt{2E})(\mathbf p) = g(\mathbf p)/\sqrt{2E_{\mathbf p}}$. The physical one-particle states are wave packets and their limits in norm; $|\mathbf p\rangle$ is the kernel of the map $g \mapsto |g\rangle$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": genuine states are wave packets) · Yu, Exercise 2.3*

^def-c2a-4-3

> [!theorem] Theorem §C2a.4.5: The Overlap of Momentum States Is a Distribution
> For $g, h \in \mathcal S(\mathbb R^3)$:
> 1. $\langle g|h\rangle = \displaystyle\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\overline{g(\mathbf p)}\,h(\mathbf p)$, finite; $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is the kernel of this pairing, a Lorentz-invariant tempered distribution in $(\mathbf p, \mathbf q)$.
> 2. $\langle\mathbf p|\mathbf p\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0)$ has no value: $|\mathbf p\rangle$ is not a vector, and the norms of wave packets narrowing to $|\mathbf p\rangle$ diverge.
> 3. $\langle\mathbf p|g\rangle = g(\mathbf p)$, and $\displaystyle\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\langle h|\mathbf p\rangle\langle\mathbf p|g\rangle = \langle h|g\rangle$: the resolution of the identity of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] holds between wave packets (weakly), and the one-particle space is $L^2(\mathbb R^3, d^3p/(2\pi)^32E_{\mathbf p})$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": $|\mathbf p\rangle$ is a distribution) and §4.9 · Yu, Exercise 2.3 · stated and derived here as distributions*

^thm-c2a-4-5

> [!derivation]- Derivation
> **1. Wave packets in operator form.** By [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}a^\dagger_{\mathbf p}|0\rangle$, so $|g\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{g(\mathbf p)}{\sqrt{2E_{\mathbf p}}}a^\dagger_{\mathbf p}|0\rangle = a^\dagger(g/\sqrt{2E})|0\rangle$. For $m > 0$, $g/\sqrt{2E} \in \mathcal S$ (as in [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-7|Derivation §C2a.2.7]], step 7).
>
> **2. The overlap of two packets.** Since $a(\cdot)|0\rangle = 0$, $\langle g|h\rangle = \langle0|a(g/\sqrt{2E})\,a^\dagger(h/\sqrt{2E})|0\rangle = [a(g/\sqrt{2E}), a^\dagger(h/\sqrt{2E})]$, and by [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 1, this is $\int\frac{d^3p}{(2\pi)^3}\overline gh/2E_{\mathbf p}$: finite, because $g, h \in \mathcal S$ and $1/2E_{\mathbf p} \le 1/2m$.
>
> **3. The kernel.** $\langle g|h\rangle$ is antilinear in $g$, linear in $h$ and continuous, so by [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]] it is $\int\frac{d^3p\,d^3q}{(2\pi)^6\,2E_{\mathbf p}2E_{\mathbf q}}\overline{g(\mathbf p)}h(\mathbf q)\,K(\mathbf p, \mathbf q)$ for exactly one tempered distribution $K$. Inserting $K = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]) and pairing the delta with the test function $\overline g(\mathbf p)h(\mathbf q)/(2E_{\mathbf p}2E_{\mathbf q})$ (variables $\mathbf u = \mathbf p - \mathbf q$, $\mathbf v = \mathbf q$, as in [[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-3|Derivation §C2a.1.3]], step 2) gives $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\overline gh$, the result of step 2: so $K = \langle\mathbf p|\mathbf q\rangle$. It is tempered because $\delta^3 \in \mathcal S'$ ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 3) and $2E_{\mathbf p}$ is smooth and polynomially bounded with its derivatives ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1); it is Lorentz invariant as a distribution ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]) by [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]].
>
> **4. No value on the diagonal.** At $\mathbf q = \mathbf p$ the kernel is $2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0)$, δ at its singular point ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). Concretely, the packets $g_\varepsilon(\mathbf p) = (2\pi)^3\,2E_{\mathbf p}\,\rho_\varepsilon(\mathbf p - \mathbf p_0)$, with $\rho_\varepsilon$ a nascent delta ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3), give $|g_\varepsilon\rangle = \int d^3p\,\rho_\varepsilon(\mathbf p - \mathbf p_0)|\mathbf p\rangle \to |\mathbf p_0\rangle$ against every wave packet, while
>
> $$
> \langle g_\varepsilon|g_\varepsilon\rangle = \int d^3p\,(2\pi)^3\,2E_{\mathbf p}\,\rho_\varepsilon(\mathbf p - \mathbf p_0)^2 = \varepsilon^{-3}\,(2\pi)^3\,2E_{\mathbf p_0}\int\rho^2 + o(\varepsilon^{-3}) \to \infty ,
> $$
>
> the divergence of $\rho_\varepsilon^2$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 2). ⚑ By-product: $|\mathbf p\rangle$ is the limit of states only weakly, as $|x'\rangle$ is in quantum mechanics → [[§37 Position Eigenstates and Continuous Resolutions#^prop-37-4|556 Prop. §37.4]].
>
> **5. Components and completeness.** $\langle\mathbf p|g\rangle = \int\frac{d^3q}{(2\pi)^3\,2E_{\mathbf q}}g(\mathbf q)\,2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q) = g(\mathbf p)$, δ acting on the test function $g$. Hence $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\langle h|\mathbf p\rangle\langle\mathbf p|g\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\overline hg = \langle h|g\rangle$ by step 2: an equality of numbers for every pair of packets, which is what the operator identity of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] asserts. The map $g \mapsto |g\rangle$ preserves inner products from $L^2(d^3p/(2\pi)^32E_{\mathbf p})$, and $\mathcal S$ is dense in that $L^2$, so it extends to all of $\mathcal H_1$.
>
> **What the derivation shows**
> - $\langle\mathbf p|\mathbf q\rangle$ is a distribution, defined by its pairings with wave packets; its "value" on the diagonal is δ at its singular point.
> - The profile $g(\mathbf p) = \langle\mathbf p|g\rangle$ is the one-particle wave function in momentum space, square integrable with the invariant measure.
> - Completeness is a statement about matrix elements between states, which is how every use of it in later sections should be read.

^der-c2a-4-5

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, step 7]]

> [!caution] Caution: The slides' normalization drops the (2π)³
> Lecture 4's slides write $\langle\mathbf p|\mathbf q\rangle = 2\omega_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q)$. With $[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, as on the same slides, the factor $(2\pi)^3$ is required ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]; PS eq. (2.36)).

^cau-c2a-4-2

> [!theorem] Theorem §C2a.4.6: The Field Creates a Particle at a Point
> Acting on the vacuum, the field at $t = 0$ is a superposition of one-particle states with invariant weight:
>
> $$
> \phi(\mathbf x)|0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,e^{-i\mathbf p\cdot\mathbf x}\,|\mathbf p\rangle, \qquad \langle\mathbf p|\phi(\mathbf x)|0\rangle = e^{-i\mathbf p\cdot\mathbf x}, \qquad \langle0|\phi(\mathbf x)|\mathbf p\rangle = e^{i\mathbf p\cdot\mathbf x} ,
> $$
>
> the field-theory analogue of $\langle\mathbf x|\mathbf p\rangle \propto e^{i\mathbf p\cdot\mathbf x}$. With the time dependence of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], $\langle0|\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 · PS §2.3, eqs. (2.41)–(2.42) · Yu §2.3.4, eqs. (2.164)–(2.165)*

^thm-c2a-4-6

> [!derivation]- Derivation
> **1. Act on the vacuum.** In $\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} + a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x}\bigr)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], before folding) the annihilators give $0$ on $|0\rangle$. ⚑ By-product: what remains weights every momentum alike (up to $1/2E_{\mathbf p}$), so the result has infinite norm; it is a vector only after smearing in $\mathbf x$ → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]].
>
> **2. Normalize.** $a^\dagger_{\mathbf p}|0\rangle = |\mathbf p\rangle/\sqrt{2E_{\mathbf p}}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); the two factors $1/\sqrt{2E_{\mathbf p}}$ combine into the invariant weight $1/2E_{\mathbf p}$, giving the first formula.
>
> **3. Project.** $\langle\mathbf q|\phi(\mathbf x)|0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-i\mathbf p\cdot\mathbf x}\,2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf q - \mathbf p) = e^{-i\mathbf q\cdot\mathbf x}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]), the delta eliminating $\mathbf p$: an identity of distributions in $\mathbf q$, whose result $e^{-i\mathbf q\cdot\mathbf x}$ happens to be a smooth function; against a wave packet, $\langle g|\phi(\mathbf x)|0\rangle = \int\frac{d^3q}{(2\pi)^3\,2E_{\mathbf q}}\overline{g(\mathbf q)}e^{-i\mathbf q\cdot\mathbf x}$, a convergent integral ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 3).
>
> **4. Conjugate.** $\phi$ is Hermitian, so $\langle0|\phi(\mathbf x)|\mathbf q\rangle = \langle\mathbf q|\phi(\mathbf x)|0\rangle^{\ast} = e^{i\mathbf q\cdot\mathbf x}$.
>
> **What the derivation shows**
> - The weight $1/2E_{\mathbf p}$ is the invariant measure: this is where the choice $1/\sqrt{2E_{\mathbf p}}$ of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2]], step 2, pays off.
> - Used next: the two-point function $\langle0|\phi(x)\phi(y)|0\rangle$ as an overlap of two such states ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]).

^der-c2a-4-6

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]

> [!theorem] Theorem §C2a.4.7: The Smeared Field Creates a State; the Field at a Point Does Not
> For real $f \in \mathcal S(\mathbb R^3)$,
>
> $$
> \phi(f)|0\rangle = |\tilde f\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\tilde f(\mathbf p)\,|\mathbf p\rangle, \qquad \|\phi(f)|0\rangle\|^2 = \langle0|\phi(f)^2|0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,|\tilde f(\mathbf p)|^2 < \infty :
> $$
>
> a one-particle wave packet ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]). As $f$ narrows to $\delta^3(\cdot - \mathbf x)$ the norm diverges, like $\Lambda^2/8\pi^2$ with a momentum cutoff $\Lambda$: $\phi(\mathbf x)|0\rangle$ is not a vector, only its pairings $\langle g|\phi(\mathbf x)|0\rangle$ with wave packets are numbers.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": $\phi(\mathbf x)$ is an operator-valued distribution) and §4.9 · stated and derived here*

^thm-c2a-4-7

> [!derivation]- Derivation
> **1. The smeared field on the vacuum.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 3, $\phi(f) = a(g_f) + a^\dagger(g_f)$ with $g_f = \tilde f/\sqrt{2E}$; $a(g_f)|0\rangle = 0$, so $\phi(f)|0\rangle = a^\dagger(\tilde f/\sqrt{2E})|0\rangle = |\tilde f\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]).
>
> **2. Its norm.** By [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 1, $\langle\tilde f|\tilde f\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde f|^2$, finite because $\tilde f \in \mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1). Since $\phi(f)$ is Hermitian it equals $\langle0|\phi(f)^2|0\rangle$: the vacuum fluctuation of the field averaged with $f$.
>
> **3. Narrow the smearing.** Let $f_\varepsilon(\mathbf y) = \rho_\varepsilon(\mathbf y - \mathbf x)$ with $\rho \ge 0$ a real test function, $\int\rho = 1$, so $f_\varepsilon \to \delta^3(\cdot - \mathbf x)$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3). By the translation and rescaling rules ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 1; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 3), $\tilde f_\varepsilon(\mathbf p) = e^{-i\mathbf p\cdot\mathbf x}\tilde\rho(\varepsilon\mathbf p)$, with $|\tilde\rho| \le \int\rho = 1$ and $\tilde\rho(\mathbf 0) = 1$.
>
> **4. The norm diverges.** For each $\Lambda$, on the ball $|\mathbf p| < \Lambda$ the integrand $|\tilde\rho(\varepsilon\mathbf p)|^2/2E_{\mathbf p}$ converges to $1/2E_{\mathbf p}$, dominated by $1/2m$, so by dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 1)
>
> $$
> \liminf_{\varepsilon\to0^+}\|\phi(f_\varepsilon)|0\rangle\|^2 \ge \int_{|\mathbf p| < \Lambda}\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \frac{1}{4\pi^2}\int_0^\Lambda\frac{p^2\,dp}{\sqrt{p^2 + m^2}} = \frac{\Lambda^2}{8\pi^2} + O\Bigl(m^2\ln\frac\Lambda m\Bigr) ,
> $$
>
> using $d^3p = 4\pi p^2dp$ and $p^2/\sqrt{p^2 + m^2} = p - m^2/2p + \dots$ at large $p$. $\Lambda$ is arbitrary, so the norm has no finite limit. ⚑ By-product: the divergent number is $\langle0|\phi(\mathbf x)^2|0\rangle$, the two-point function at coincident points, the same coincident product as the zero-point energy → [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
>
> **5. What survives at a point.** The components $\langle\mathbf p|\phi(\mathbf x)|0\rangle = e^{-i\mathbf p\cdot\mathbf x}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]]) are bounded, so against a wave packet $\langle g|\phi(\mathbf x)|0\rangle$ is a convergent integral. $\phi(\mathbf x)|0\rangle$ is a "ket" in the sense of $|x'\rangle$: defined by its pairings, not normalizable.
>
> **What the derivation shows**
> - A field averaged over a region creates a genuine one-particle state, whose momentum profile is the transform $\tilde f$ of the averaging function.
> - The field at a point creates no state: the obstruction is ultraviolet (large momenta), not infrared.
> - Used next: fluctuations of a coherent state are meaningful when smeared ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]]); the smeared vacuum fluctuation is the Wightman function smeared with $f\otimes f$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]).

^der-c2a-4-7

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

> [!remark] Remark: Sharp momentum or sharp position; why √(2E_p)
> - **Fourier conjugates.** $a^\dagger_{\mathbf p}|0\rangle$ has sharp momentum and is not localized (its "wave function" is a plane wave); $\phi(\mathbf x)|0\rangle$ is localized at $\mathbf x$ and contains all momenta. The two are related as $|\mathbf p\rangle$ and $|\mathbf x\rangle$ are in quantum mechanics ([[§C2.3 Wave Functions in Position and Momentum Space#^thm-c2-3-3|QM Theorem §C2.3.3]]), with the difference that $\mathbf x$ labels an operator. The localization is approximate: compared with $|\mathbf x\rangle$, the weight carries an extra $1/2E_{\mathbf p}$, nearly constant only for $|\mathbf p| \ll m$ (PS p. 24).
> - **Why the factor.** The $1/\sqrt{2E_{\mathbf p}}$ placed in the mode expansion and the $\sqrt{2E_{\mathbf p}}$ in $|\mathbf p\rangle$ are the same choice: they make $\langle\mathbf p|\mathbf q\rangle$, $\langle\mathbf p|\phi|0\rangle$ and the completeness relation invariant, at the price of dividing by $2E_{\mathbf p}$ elsewhere. With it a Lorentz transformation acts on states without extra factors, $U(\Lambda)|\mathbf p\rangle = |\Lambda\mathbf p\rangle$ (PS eq. (2.37)); that, and the spin-0 particle as a representation of the Poincaré group, is [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11|Theorem §C3.5.11]]; for a particle of any spin the relativistic normalization is again the one that keeps the transformation law free of factors ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.9 ("Two complementary statements, not a contradiction"; "Discussion") · PS §2.3, pp. 23–24*

^rem-c2a-4-3

> [!remark]- Connections
> - The Fock space and the algebra of creation operators of nonrelativistic many-body theory are the same structure; what the field adds is that the one-particle space is generated by the field, labelled by a continuous momentum and normalized invariantly — [[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]], [[§C12.2★ Second Quantization#^rem-c12-2-1|QM Remark: One mode is one oscillator; what changes]].
> - The invariant measure is the mass hyperboloid's volume element, and the invariance of $\operatorname{sgn}p^0$ on it is the momentum-space form of the invariance of past and future — [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]].
> - The two-point function $\langle0|\phi(x)\phi(y)|0\rangle$ is $\langle0|\phi(x)$ times $\phi(y)|0\rangle$, two superpositions of the states of Theorem §C2a.4.6, integrated with the invariant measure; the zero-point constant is its coincident limit — [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]; single-particle position states $|\mathbf x\rangle$ carry weight $1$ instead of $1/2E_{\mathbf p}$, which makes the single-particle amplitude a time derivative of $D_W$ — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-7|Theorem §C2b.3.7]].
> - $|\mathbf p\rangle$ is to the Fock space what a tempered distribution is to the test functions: known through its pairings $\langle\mathbf p|g\rangle = g(\mathbf p)$, with $\langle\mathbf p|\mathbf q\rangle$ the kernel of the inner product ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]) — [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]; its infinite norm is δ at its singular point, and the narrowing packets that approach it are nascent deltas — [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]].
> - The invariant measure is a distribution on spacetime momenta, $\theta(p^0)\delta(p^2 - m^2)$, defined through composition with $p^2 - m^2$; θ·δ is a legitimate product here because θ is smooth near the shell — [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]; Lorentz invariance of $\langle\mathbf p|\mathbf q\rangle$ is invariance of a distribution — [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]].
> - The divergence of $\|\phi(\mathbf x)|0\rangle\|^2$ is the large-momentum tail of the transform of a narrowing test function; translation and rescaling turn the narrowing into $\tilde\rho(\varepsilon\mathbf p)$, and dominated convergence on balls gives the bound ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]]) — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]].
> - A charged field has two such Fock towers, particles and antiparticles — [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]]; a vector field is, roughly, one scalar per polarization — [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-5|Theorem §C4.4.5]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]], and for the photon [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-9|Theorem §C4.7.9]]; the full recipe — [[P1 Canonical Quantization]].
> - For $N$ coupled scalars the spectrum of Theorem §C2a.4.1 holds for each mass eigenfield, with masses the square roots of the eigenvalues of the mass matrix ([[§R1.3 Diagonalization into N Free Klein–Gordon Fields#^thm-r1-3-4|Thesis Thm. §R1.3.4]]); when exactly one of those particles is light is the question of the honors-thesis scalar-mass notes ([[§R5.1 What One Light State Means#^def-r5-1-1|Thesis Def. §R5.1.1]]).
