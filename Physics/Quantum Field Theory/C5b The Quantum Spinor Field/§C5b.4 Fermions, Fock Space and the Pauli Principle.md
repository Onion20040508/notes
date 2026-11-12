---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.3 Energy, Momentum and the Zero-Point Energy]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.5 The U(1) Charge, Particles and Antiparticles]] →

*Sources: the user's PHY 513 notes, Ch. 10 §10.6 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part C, slides 20–21 and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 57–61 · Yu Zhao-Huan, 量子场论讲义, §5.5.4; §5.1, eqs. (5.57)–(5.61) (the covariance law of the quantum Dirac field) · the user's pre-course notes, §5.5.*

This is the spinor counterpart of [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]: with the Hamiltonian diagonal and positive ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]) and the ladder relations in hand ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]]), what are the states? The vacuum and the Fock space ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], postulated in §C5b.3 before the zero-point energy) are as for the scalar, with the relativistic normalization unchanged; the spin-specific additions are the two spin states per momentum, the antisymmetry of every multiparticle state, and with it the Pauli exclusion principle, which here is a consequence of the anticommutators and not a postulate ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-6|§C5b.1, Remark: Spin and statistics are an output]]). The Lorentz covariance of the quantized field, $U(\Lambda)\hat\psi(x)U(\Lambda)^{-1} = \Lambda_{1/2}^{-1}\hat\psi(\Lambda x)$, is beyond the lectures and is written out as ★ material ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]]). The charges of the two species are in [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]]. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

**Setup.** The free Dirac field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]) with anticommutators, on the fermionic Fock space over the free vacuum $|0\rangle$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]]); one-particle states relativistically normalized as for the scalar ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); exact. The spin of the antifermion depends on the choice of $\eta^s$, fixed in [[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]].

## The one-particle states

> [!theorem] Theorem §C5b.4.1: Fermions and Antifermions
> The one-particle states
>
> $$
> |\mathbf p, s\rangle \equiv \sqrt{2E_{\mathbf p}}\,\hat a^{s\dagger}_{\mathbf p}|0\rangle, \qquad |\mathbf p, s\rangle^c \equiv \sqrt{2E_{\mathbf p}}\,\hat b^{s\dagger}_{\mathbf p}|0\rangle
> $$
>
> (the vacuum of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], relativistic normalization as in [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) are eigenstates of $:\!\hat H\!:$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]) with eigenvalue $+E_{\mathbf p}$ and carry momentum $\mathbf p$ and spin label $s$ (for the antiparticle the label is its physical spin only with the two-spinors $\eta^s = \xi^{-s}$ of Lecture 12, [[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]: its wave-function spin is opposite, [[§C9.8 Physical Spin versus Wave-Function Spin|§C9.8]]): $\hat a^\dagger$ creates a **particle** (fermion; for the electron field an electron) and $\hat b^\dagger$ an **antiparticle** (antifermion; a positron), the $c$ standing for "conjugate". Both have mass $m$ and two spin states; their charges are opposite ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]). Their overlaps are positive and Lorentz invariant,
>
> $$
> \langle\mathbf p, r|\mathbf q, s\rangle = {}^c\langle\mathbf p, r|\mathbf q, s\rangle^c = 2E_{\mathbf p}(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q), \qquad {}^c\langle\mathbf p, r|\mathbf q, s\rangle = 0 ,
> $$
>
> distributions in $(\mathbf p, \mathbf q)$ as for the scalar ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]); physical states are wave packets ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]).
>
> *Scalar analogue:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]]; complex field [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]].
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact.
>
> *Source: Lecture 10, slide 20 ("a† ∼ particle, b† ∼ anti-particle") · the user's PHY 513 notes, Ch. 10 §10.6 (Principle "One-particle states") · PS §3.5, eqs. (3.106)–(3.107) · Yu §5.5.4, eqs. (5.270)–(5.275) · the user's pre-course notes, §5.5*

^thm-c5b-4-1

> [!derivation]- Derivation
> **1. Eigenvalues.** $:\!\hat H\!:|0\rangle = \hat{\mathbf P}|0\rangle = 0$ (each term ends in an annihilator). By [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], $:\!\hat H\!:\hat a^{s\dagger}_{\mathbf p}|0\rangle = [:\!\hat H\!:, \hat a^{s\dagger}_{\mathbf p}]|0\rangle + \hat a^{s\dagger}_{\mathbf p}:\!\hat H\!:|0\rangle = E_{\mathbf p}\hat a^{s\dagger}_{\mathbf p}|0\rangle$; the same for $\hat{\mathbf P}$ (eigenvalue $\mathbf p$) and for $\hat b^{s\dagger}_{\mathbf p}$. (With the unordered $\hat H$ both energies are shifted by $E_0^{(\rm D)}$, Yu (5.274).) The charges: Step 6 of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-4|Derivation §C5b.5.4]].
>
> **2. Overlaps.** $\langle0|\hat a^r_{\mathbf p}\hat a^{s\dagger}_{\mathbf q}|0\rangle = \langle0|\bigl(\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} - \hat a^{s\dagger}_{\mathbf q}\hat a^r_{\mathbf p}\bigr)|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$; multiplying by $\sqrt{2E_{\mathbf p}2E_{\mathbf q}}$ and evaluating on the support of δ ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], 1) gives $2E_{\mathbf p}$ (in short, $\langle0|\hat a\hat a^\dagger|0\rangle = \langle0|\{\hat a, \hat a^\dagger\}|0\rangle$). The same for $\hat b$. Lorentz invariance of this normalization is the scalar's ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]). Mixed: $\langle0|\hat b^r_{\mathbf p}\hat a^{s\dagger}_{\mathbf q}|0\rangle = -\langle0|\hat a^{s\dagger}_{\mathbf q}\hat b^r_{\mathbf p}|0\rangle = 0$, since $\{\hat b, \hat a^\dagger\} = 0$.
>
> **3. Positivity.** With commutators the $\hat b$-overlap had the opposite sign ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], 1); the anticommutator restores it. Smeared, $\|\hat a^{s\dagger}(g)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3}|g|^2 > 0$.
>
> **What the derivation shows**
> - Both species have the same dispersion $E_{\mathbf p}$ because both sit in one field on one mass shell; opposite charge because they sit in its two frequency parts, as for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]).
> - Particles and antiparticles stand on the same footing: two spin states each and the same energy; nothing but convention decided which is called which ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-2|§C5b.2, Remark: ψ̄ is ψ with particles and antiparticles interchanged]]).

^der-c5b-4-1

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-9|P1, steps 8–9]]

## Many particles: Fermi–Dirac statistics

> [!theorem] Theorem §C5b.4.2: Fermi–Dirac Statistics and the Pauli Exclusion Principle
> In the Fock space of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], with the algebra of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]:
> 1. $\hat a^{r\dagger}_{\mathbf p}\hat a^{s\dagger}_{\mathbf q} = -\hat a^{s\dagger}_{\mathbf q}\hat a^{r\dagger}_{\mathbf p}$ (likewise for $\hat b^\dagger$, and $\hat a^\dagger \hat b^\dagger = -\hat b^\dagger \hat a^\dagger$): a multiparticle state changes sign when two identical quanta are exchanged. The quanta are fermions.
> 2. *(Pauli)* $\hat a^{s\dagger}(g)^2 = \hat b^{s\dagger}(g)^2 = 0$ for every wave packet $g$: no two identical fermions occupy the same one-particle state (spin label and packet); in kernel form, $\hat a^{s\dagger}_{\mathbf p}\hat a^{s\dagger}_{\mathbf p}|0\rangle = 0$.
> 3. For $|\mathbf p_1s_1; \mathbf p_2s_2\rangle \equiv \sqrt{4E_{\mathbf p_1}E_{\mathbf p_2}}\,\hat a^{s_1\dagger}_{\mathbf p_1}\hat a^{s_2\dagger}_{\mathbf p_2}|0\rangle$,
>
> $$
> \langle\mathbf q_1r_1; \mathbf q_2r_2|\mathbf p_1s_1; \mathbf p_2s_2\rangle = 4E_{\mathbf p_1}E_{\mathbf p_2}(2\pi)^6\Bigl[\delta^{r_1s_1}\delta^{r_2s_2}\delta^3(\mathbf p_1 - \mathbf q_1)\delta^3(\mathbf p_2 - \mathbf q_2) - \delta^{r_1s_2}\delta^{r_2s_1}\delta^3(\mathbf p_1 - \mathbf q_2)\delta^3(\mathbf p_2 - \mathbf q_1)\Bigr] ,
> $$
>
> with a minus sign where two bosons have a plus ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, exact.
>
> *Source: Lecture 10, slide 21 and transcript · the user's PHY 513 notes, Ch. 10 §10.6 (Principle "Many-particle states: Fermi–Dirac statistics and the exclusion principle") · PS §3.5, p. 57 · Yu §5.5.4, eqs. (5.289)–(5.295) · the user's pre-course notes, §5.5*

^thm-c5b-4-2

> [!derivation]- Derivation
> **1. Antisymmetry.** $\{\hat a^{r\dagger}_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = 0$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]); similarly for $\hat b^\dagger$ and between $\hat a^\dagger$, $\hat b^\dagger$. In a product of creation operators acting on $|0\rangle$, moving one past another costs $-1$; exchanging the $i$-th and $j$-th takes an odd number of adjacent moves, so the state changes sign (Yu (5.290)–(5.291)).
>
> **2. Pauli.** Smeared, $\{\hat a^{s\dagger}(g), \hat a^{s\dagger}(g)\} = 0$, i.e. $2\hat a^{s\dagger}(g)^2 = 0$. The kernel form is the statement at coinciding labels, which the identity $\{\hat a^{s\dagger}_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = 0$ contains (its right side has no δ, so no valueless constant arises at $\mathbf p = \mathbf q$). ⚑ By-product: exclusion is a consequence of the anticommutators, not an extra input, and it holds for every one-particle state at once → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, ★ Remark: The Dirac sea, read in the field]].
>
> **3. Two-particle overlap: first annihilator.** $\langle\mathbf q_1r_1; \mathbf q_2r_2| = \sqrt{4E_{\mathbf q_1}E_{\mathbf q_2}}\langle0|\hat a^{r_2}_{\mathbf q_2}\hat a^{r_1}_{\mathbf q_1}$. Move $\hat a^{r_1}_{\mathbf q_1}$ to the right:
>
> $$
> \hat a^{r_1}_{\mathbf q_1}\hat a^{s_1\dagger}_{\mathbf p_1}\hat a^{s_2\dagger}_{\mathbf p_2}|0\rangle = (2\pi)^3\delta^{r_1s_1}\delta^3(\mathbf q_1 - \mathbf p_1)\,\hat a^{s_2\dagger}_{\mathbf p_2}|0\rangle - \hat a^{s_1\dagger}_{\mathbf p_1}\,(2\pi)^3\delta^{r_1s_2}\delta^3(\mathbf q_1 - \mathbf p_2)|0\rangle ,
> $$
>
> the minus sign from passing $\hat a^{s_1\dagger}_{\mathbf p_1}$.
>
> **4. Second annihilator.** $\langle0|\hat a^{r_2}_{\mathbf q_2}\hat a^{s\dagger}_{\mathbf p}|0\rangle = (2\pi)^3\delta^{r_2s}\delta^3(\mathbf q_2 - \mathbf p)$ for both terms: direct minus exchanged. The prefactor $\sqrt{16E_{\mathbf q_1}E_{\mathbf q_2}E_{\mathbf p_1}E_{\mathbf p_2}}$ is $4E_{\mathbf p_1}E_{\mathbf p_2}$ on the support of either product of deltas. *Sense:* an identity of distributions in the four momenta; paired with packets it is $\langle g_1, h_1\rangle\langle g_2, h_2\rangle - \langle g_1, h_2\rangle\langle g_2, h_1\rangle$, as in [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-2|Derivation §C2a.4.2]], step 3, with the sign changed.
>
> **What the derivation shows**
> - Fermi statistics comes with the field; Quantum Mechanics had to postulate it per species ([[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]; same algebra, [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]]).

^der-c5b-4-2

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]

*Procedure:* [[P1 Canonical Quantization#^p1-8|P1, step 8]]

## Spin and Lorentz covariance of the quanta

> [!theorem] Theorem §C5b.4.3: Dirac Quanta Have Spin One-Half
> With the angular momentum $\hat{\mathbf J} = \int d^3x\,:\!\hat\psi^\dagger\bigl(\mathbf x\times(-i\nabla) + \tfrac12\boldsymbol\Sigma\bigr)\hat\psi\!:$ of [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-8|Theorem §C5a.9.8]] (normal ordered, [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], so $\hat{\mathbf J}|0\rangle = 0$; $\boldsymbol\Sigma = \operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$, [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]) and the spin bases $\xi^s$, $\eta^s$ of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]], the zero-momentum states satisfy
>
> $$
> \hat J_z\,\hat a^{s\dagger}_{\mathbf 0}|0\rangle = \sum_r\Bigl(\xi^{r\dagger}\tfrac{\sigma^3}{2}\xi^s\Bigr)\hat a^{r\dagger}_{\mathbf 0}|0\rangle, \qquad \hat J_z\,\hat b^{s\dagger}_{\mathbf 0}|0\rangle = -\sum_r\Bigl(\eta^{s\dagger}\tfrac{\sigma^3}{2}\eta^r\Bigr)\hat b^{r\dagger}_{\mathbf 0}|0\rangle .
> $$
>
> For $\sigma^3$-eigenvectors $\xi^s, \eta^s \in \{(1, 0)^T, (0, 1)^T\}$: the fermion has $J_z = \pm\frac12$, the antifermion $J_z = \mp\frac12$, opposite to its two-spinor. With the choice $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]) the antifermion created by $\hat b^{s\dagger}_{\mathbf 0}$ has $J_z = \pm\frac12$, like the fermion ([[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact; particles at rest, $\hat{\mathbf J}$ normal ordered.
>
> *Source: PS §3.5, pp. 60–61, eqs. (3.111)–(3.112) (the reading of Lecture 12, where the result is used for the physical spin of the antifermion, [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]])*

^thm-c5b-4-3

> [!derivation]- Derivation
> **1. Reduce to a commutator.** $\hat J_z|0\rangle = 0$, so $\hat J_z\hat a^{s\dagger}_{\mathbf 0}|0\rangle = [\hat J_z, \hat a^{s\dagger}_{\mathbf 0}]|0\rangle$ (PS). With $\hat J_z = \int d^3x\,\hat\psi^\dagger_aM_{ab}\hat\psi_b$, $M = (\mathbf x\times(-i\nabla))_z + \frac12\Sigma^3$, the identity of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]] gives $[\hat\psi^\dagger_aM_{ab}\hat\psi_b, C] = \hat\psi^\dagger_aM_{ab}\{\hat\psi_b, C\} - \{\hat\psi^\dagger_a, C\}M_{ab}\hat\psi_b$ (the normal-ordering constant commutes).
>
> **2. The anticommutators with $\hat a^{s\dagger}_{\mathbf 0}$.** From [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], $\{\hat\psi(x), \hat a^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}u^s(0)e^{-imt}$ (the $\mathbf p$-integral against $(2\pi)^3\delta^3(\mathbf p)$; $E_{\mathbf 0} = m$) and $\{\hat\psi^\dagger(x), \hat a^{s\dagger}_{\mathbf 0}\} = 0$. So $[\hat J_z, \hat a^{s\dagger}_{\mathbf 0}] = \frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,\hat\psi^\dagger(x)\,M\,u^s(0)$.
>
> **3. Orbital part.** $u^s(0)$ is constant in $\mathbf x$, so $(\mathbf x\times(-i\nabla))_zu^s(0) = 0$. Dropped: the orbital term.
>
> **4. Spin part.** $\int d^3x\,\hat\psi^\dagger(x) = \frac{1}{\sqrt{2m}}\sum_r\bigl(\hat a^{r\dagger}_{\mathbf 0}u^{r\dagger}(0)e^{imt} + \hat b^r_{\mathbf 0}v^{r\dagger}(0)e^{-imt}\bigr)$ (the $d^3x$ integral gives $(2\pi)^3\delta^3(\mathbf p)$, [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]). Hence
>
> $$
> [\hat J_z, \hat a^{s\dagger}_{\mathbf 0}] = \frac{1}{2m}\sum_r\Bigl(u^{r\dagger}(0)\tfrac12\Sigma^3u^s(0)\,\hat a^{r\dagger}_{\mathbf 0} + v^{r\dagger}(0)\tfrac12\Sigma^3u^s(0)\,e^{-2imt}\,\hat b^r_{\mathbf 0}\Bigr) .
> $$
>
> **5. Rest-frame spinors.** $u^s(0) = \sqrt m(\xi^s, \xi^s)$, $v^s(0) = \sqrt m(\eta^s, -\eta^s)$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]), and $\Sigma^3 = \operatorname{diag}(\sigma^3, \sigma^3)$: $u^{r\dagger}(0)\Sigma^3u^s(0) = 2m\,\xi^{r\dagger}\sigma^3\xi^s$ and $v^{r\dagger}(0)\Sigma^3u^s(0) = m(\eta^{r\dagger}\sigma^3\xi^s - \eta^{r\dagger}\sigma^3\xi^s) = 0$. Dropped: the $\hat b$ term, identically. This gives the first formula.
>
> **6. Antifermion.** Now $\{\hat\psi(x), \hat b^{s\dagger}_{\mathbf 0}\} = 0$ and $\{\hat\psi^\dagger(x), \hat b^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}v^{s\dagger}(0)e^{-imt}$, so $[\hat J_z, \hat b^{s\dagger}_{\mathbf 0}] = -\frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,v^{s\dagger}(0)M\hat\psi(x)$: the operator now stands on the *right* of the spinor, and the order of the $\hat b$ terms is reversed (PS: "an extra minus sign"). The orbital term is $\int d^3x\,v^{s\dagger}(0)(x\partial_y - y\partial_x)\hat\psi = -\int d^3x\,(\partial_yx - \partial_xy)v^{s\dagger}(0)\hat\psi = 0$ by parts (fall-off; [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]). With $\int d^3x\,\hat\psi = \frac{1}{\sqrt{2m}}\sum_r(\hat a^r_{\mathbf 0}u^r(0)e^{-imt} + \hat b^{r\dagger}_{\mathbf 0}v^r(0)e^{imt})$, the $\hat a$ term annihilates $|0\rangle$ (and has $v^\dagger\Sigma^3u = 0$), and $v^{s\dagger}(0)\Sigma^3v^r(0) = 2m\,\eta^{s\dagger}\sigma^3\eta^r$: the second formula.
>
> **7. Sense.** $\hat a^{s\dagger}_{\mathbf 0}$ is the kernel of $\hat a^{s\dagger}(g)$ at $\mathbf p = 0$, and the formulas are identities of operator-valued distributions evaluated there (PS's computation). For packets $g$ near $\mathbf p = 0$ the orbital part and the $\mathbf p$-dependence of $u^s(p)$ add terms that vanish at $\mathbf p = 0$; the general statement is the little-group spin of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]] (a ★ section, beyond the course); for the Dirac quanta at every momentum it is [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]], 2.
>
> ⚑ By-product: an antifermion built on $\eta^s = (1, 0)^T$ has $J_z = -\frac12$, as a hole in a state of $J_z = +\frac12$ would → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, ★ Remark: The Dirac sea, read in the field]]; with Yu's helicity labelling ($\eta^s = \lambda\xi_{-\lambda}$, [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^cau-c5a-11-1|§C5a.11, Caution: η means two things]] and [[§C5a.13 Helicity Spinors and the Massless Limit#^thm-c5a-13-3|Theorem §C5a.13.3]]) the antiparticle's helicity equals its label (Yu (5.276)–(5.286)).
>
> **What the derivation shows**
> - The spin $\frac12$ is that of the rest-frame two-spinors: the field's quanta are the massive spin-$\frac12$ states of Wigner's classification.

^der-c5b-4-3

*Uses:* [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-8|Theorem §C5a.9.8]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]]

> [!theorem]- ★ Lemma §C5b.4.1: The Plane-Wave Spinors under a Lorentz Transformation
> Let $m > 0$, let $\Lambda$ be a proper orthochronous Lorentz transformation with spinor matrix $\Lambda_{1/2}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; either of its two signs, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 2), $p$ a momentum on the mass shell, $\Lambda_{1/2}(p)$ the spinor matrix of the pure boost $L(p)$ from rest to $p$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]), and $u^s$, $v^s$ the spinors of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] and [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]] with spin bases $\xi^s$, $\eta^s$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]), in the chiral basis.
> 1. $\Lambda_{1/2}(\Lambda p)^{-1}\,\Lambda_{1/2}\,\Lambda_{1/2}(p) = \operatorname{diag}(w, w)$ with a matrix $w = w(\Lambda_{1/2}, p) \in SU(2)$; the left side is a spinor matrix of the Wigner element $W(\Lambda, p) = L(\Lambda p)^{-1}\Lambda L(p)$ ([[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]] with $V(p) = L(p)$), a rotation of the rest frame ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]).
> 2. The transformed spinors are the spinors at $\Lambda p$ with rotated spin labels:
>
> $$
> \Lambda_{1/2}\,u^s(p) = \sum_r u^r(\Lambda p)\,\mathcal D_{rs}, \qquad \Lambda_{1/2}\,v^s(p) = \sum_r v^r(\Lambda p)\,\tilde{\mathcal D}_{rs}, \qquad \mathcal D_{rs} \equiv \xi^{r\dagger}w\,\xi^s, \quad \tilde{\mathcal D}_{rs} \equiv \eta^{r\dagger}w\,\eta^s ,
> $$
>
> with $\mathcal D$, $\tilde{\mathcal D}$ unitary $2\times2$ matrices depending on $\Lambda_{1/2}$ and $p$. For $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]), $\tilde{\mathcal D}_{rs} = (\mathcal D_{rs})^{\ast}$.
> 3. For two transformations, $w(\Lambda'_{1/2}\Lambda_{1/2}, p) = w(\Lambda'_{1/2}, \Lambda p)\,w(\Lambda_{1/2}, p)$, and the same for $\mathcal D$ and $\tilde{\mathcal D}$ (the spinor form of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]).
> 4. Take $\Lambda_{1/2}$ to be the exponential of the generators ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]). For a boost along $\pm\hat{\mathbf p}$, and for any pure boost at $\mathbf p = 0$, $w = \mathbb 1$ and $u^s(\Lambda p) = \Lambda_{1/2}u^s(p)$, $v^s(\Lambda p) = \Lambda_{1/2}v^s(p)$ (Peskin–Schroeder's relation). For a rotation by $\theta$ about $\hat{\mathbf n}$, $w = e^{-i\theta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ for every $p$ ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-10|Theorem §C3.6.10]]).
>
> *Model:* none (c-number spinors, a representation fact); *applies:* $m > 0$, on shell $p^0 = E_{\mathbf p}$, any spin bases; exact.
>
> *Source: PS §3.5, p. 59 ($u^s(\Lambda^{-1}\tilde p) = \Lambda_{1/2}^{-1}u^s(\tilde p)$, the case $w = \mathbb 1$) · the general form written out here from [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] and the Wigner element of [[§C3.6★ Particle States and the Little Group|§C3.6★]]; checked numerically*

^lem-c5b-4-1

> [!derivation]- Derivation
> Write $k = (m, \mathbf 0)$, $M \equiv \Lambda_{1/2}(\Lambda p)^{-1}\,\Lambda_{1/2}\,\Lambda_{1/2}(p)$, and $u^s_0 = \sqrt m\,(\xi^s, \xi^s)$, $v^s_0 = \sqrt m\,(\eta^s, -\eta^s)$ for the rest-frame spinors ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]]).
>
> **Step 1** ($M$ commutes with $\gamma^0$). A spinor matrix carries the slash of a momentum to the slash of the transformed momentum, $\Lambda_{1/2}\,\slashed{p}\,\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)}$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-9|Theorem §C5a.12.9]], 1). Apply it three times, to $L(p)$ (which takes $k$ to $p$), to $\Lambda$, and to $L(\Lambda p)^{-1}$ (which takes $\Lambda p$ to $k$):
>
> $$
> M\,\slashed{k}\,M^{-1} = \Lambda_{1/2}(\Lambda p)^{-1}\,\Lambda_{1/2}\,\slashed{p}\,\Lambda_{1/2}^{-1}\,\Lambda_{1/2}(\Lambda p) = \Lambda_{1/2}(\Lambda p)^{-1}\,\slashed{(\Lambda p)}\,\Lambda_{1/2}(\Lambda p) = \slashed{k} .
> $$
>
> Since $\slashed{k} = m\gamma^0$ and $m \ne 0$, $M\gamma^0 = \gamma^0M$.
>
> **Step 2** (block form). In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]) every spinor matrix is block diagonal ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 1; for the pure boost [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]]), and so are products and inverses: $M = \operatorname{diag}(M_L, M_R)$. With $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $M\gamma^0 = \begin{pmatrix}0 & M_L\\ M_R & 0\end{pmatrix}$ and $\gamma^0M = \begin{pmatrix}0 & M_R\\ M_L & 0\end{pmatrix}$. By Step 1 they are equal: $M_L = M_R \equiv w$.
>
> **Step 3** ($w$ is unitary with determinant 1). Each factor $X$ of $M$ satisfies $X^\dagger\gamma^0X = \gamma^0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 2; if $X$ does, so does $X^{-1}$), hence $M^\dagger\gamma^0M = \gamma^0$. With $M = \operatorname{diag}(w, w)$ the left side is $\begin{pmatrix}0 & w^\dagger w\\ w^\dagger w & 0\end{pmatrix}$, so $w^\dagger w = \mathbb 1$. The upper blocks multiply to $w = \bigl(\sqrt{(\Lambda p)\cdot\sigma/m}\bigr)^{-1}\Lambda_L\sqrt{p\cdot\sigma/m}$; $\det\Lambda_L = 1$ (the exponent in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] is traceless) and $\det\sqrt{p\cdot\sigma/m} = \sqrt{(E_{\mathbf p} - |\mathbf p|)(E_{\mathbf p} + |\mathbf p|)}/m = 1$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]), so $\det w = 1$: $w \in SU(2)$.
>
> **Step 4** (it belongs to the Wigner element). Products of spinor matrices are spinor matrices of the products ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 2), so $M$ is a spinor matrix of $L(\Lambda p)^{-1}\Lambda L(p) = W(\Lambda, p)$, which fixes $k$ ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]]) and is therefore a rotation ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]); $\operatorname{diag}(w, w)$ with $w \in SU(2)$ is the form of the spinor matrix of a rotation ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 1, at $\boldsymbol\eta = 0$). This is part 1.
>
> **Step 5** (the $u$ spinors). By [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], 1, $u^s(p) = \Lambda_{1/2}(p)\,u^s_0$. Insert $\mathbb 1 = \Lambda_{1/2}(\Lambda p)\,\Lambda_{1/2}(\Lambda p)^{-1}$:
>
> $$
> \Lambda_{1/2}\,u^s(p) = \Lambda_{1/2}(\Lambda p)\,\bigl[\Lambda_{1/2}(\Lambda p)^{-1}\,\Lambda_{1/2}\,\Lambda_{1/2}(p)\bigr]\,u^s_0 = \Lambda_{1/2}(\Lambda p)\,M\,u^s_0 = \Lambda_{1/2}(\Lambda p)\,\sqrt m\begin{pmatrix}w\,\xi^s\\ w\,\xi^s\end{pmatrix} .
> $$
>
> Expand $w\,\xi^s$ in the spin basis, $w\,\xi^s = \sum_r\xi^r(\xi^{r\dagger}w\,\xi^s) = \sum_r\xi^r\,\mathcal D_{rs}$ (completeness, [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]). Then $M\,u^s_0 = \sum_ru^r_0\,\mathcal D_{rs}$ and $\Lambda_{1/2}\,u^s(p) = \sum_r\Lambda_{1/2}(\Lambda p)\,u^r_0\,\mathcal D_{rs} = \sum_ru^r(\Lambda p)\,\mathcal D_{rs}$.
>
> **Step 6** (the $v$ spinors). The same with $v^s(p) = \Lambda_{1/2}(p)\,v^s_0$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]): $M\,v^s_0 = \sqrt m\,(w\,\eta^s, -w\,\eta^s) = \sum_rv^r_0\,(\eta^{r\dagger}w\,\eta^s)$, so $\Lambda_{1/2}\,v^s(p) = \sum_rv^r(\Lambda p)\,\tilde{\mathcal D}_{rs}$. The relative sign of the two blocks of $v_0$ is untouched because $M$ acts with the same $w$ on both.
>
> **Step 7** ($\mathcal D$ is unitary). $\mathcal D$ is the matrix of the unitary $w$ in the orthonormal basis $\xi^s$: $\sum_t(\mathcal D_{tr})^{\ast}\mathcal D_{ts} = \sum_t(\xi^{r\dagger}w^\dagger\xi^t)(\xi^{t\dagger}w\,\xi^s) = \xi^{r\dagger}w^\dagger w\,\xi^s = \delta_{rs}$, by completeness and orthonormality; the same for $\tilde{\mathcal D}$ in the basis $\eta^s$.
>
> **Step 8** ($\eta^s = \xi^{-s}$). With $J\xi \equiv -i\sigma^2\xi^{\ast}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-3|Theorem §C9.6.3]]), $\eta^s = J\xi^s$. Since $w \in SU(2)$, $w\,J\xi^s = J(w\,\xi^s)$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-3|Theorem §C9.6.3]], 2), and $(J\xi)^\dagger(J\chi) = (\xi^\dagger\chi)^{\ast}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-3|Theorem §C9.6.3]], 1): $\tilde{\mathcal D}_{rs} = (J\xi^r)^\dagger\,J(w\,\xi^s) = (\xi^{r\dagger}w\,\xi^s)^{\ast} = (\mathcal D_{rs})^{\ast}$.
>
> **Step 9** (composition). For $\Lambda'_{1/2}\Lambda_{1/2}$ insert $\mathbb 1 = \Lambda_{1/2}(\Lambda p)\,\Lambda_{1/2}(\Lambda p)^{-1}$ between the two matrices:
>
> $$
> \Lambda_{1/2}(\Lambda'\Lambda p)^{-1}\,\Lambda'_{1/2}\,\Lambda_{1/2}\,\Lambda_{1/2}(p) = \bigl[\Lambda_{1/2}(\Lambda'\Lambda p)^{-1}\,\Lambda'_{1/2}\,\Lambda_{1/2}(\Lambda p)\bigr]\bigl[\Lambda_{1/2}(\Lambda p)^{-1}\,\Lambda_{1/2}\,\Lambda_{1/2}(p)\bigr] ,
> $$
>
> the product of the matrices $M$ for $(\Lambda'_{1/2}, \Lambda p)$ and $(\Lambda_{1/2}, p)$. Their blocks multiply, and so do the matrices of $w$ in a fixed orthonormal basis: part 3.
>
> **Step 10** (special cases). *Boost along $\hat{\mathbf p}$.* The boost matrices along one axis are exponentials of one generator and multiply by adding rapidities, so $\Lambda_{1/2}\,\Lambda_{1/2}(p) = \Lambda_{1/2}(\Lambda p)$ (both are the positive matrix of [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]] for the momentum $\Lambda p$, which lies on the same axis), $M = \mathbb 1$; at $\mathbf p = 0$, $\Lambda_{1/2}(p) = \mathbb 1$ and $\Lambda_{1/2} = \Lambda_{1/2}(\Lambda p)$ for a pure boost. *Rotation $R$.* $\Lambda_{1/2} = \operatorname{diag}(A, A)$ with $A = e^{-i\theta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ unitary ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 1, at $\boldsymbol\eta = 0$, $\boldsymbol\theta = \theta\hat{\mathbf n}$). The upper-right block of $\Lambda_{1/2}\,\slashed{p}\,\Lambda_{1/2}^{-1} = \slashed{(Rp)}$ (Step 1) reads $A\,(p\cdot\sigma)\,A^{-1} = (Rp)\cdot\sigma$; $A\sqrt{p\cdot\sigma}\,A^{-1}$ is positive with this square, so it is $\sqrt{(Rp)\cdot\sigma}$ (uniqueness of the positive root, [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]), and likewise for $\bar\sigma$. Hence $\Lambda_{1/2}\,\Lambda_{1/2}(p)\,\Lambda_{1/2}^{-1} = \Lambda_{1/2}(Rp)$ and $M = \Lambda_{1/2}(Rp)^{-1}\Lambda_{1/2}\,\Lambda_{1/2}(p) = \Lambda_{1/2}$: $w = A$.
>
> **What the derivation shows**
> - Three facts are used: the covariance of $\slashed{p}$, the block form in the chiral basis, and the pseudo-unitarity of $\Lambda_{1/2}$. With $-\Lambda_{1/2}$ in place of $\Lambda_{1/2}$, $w$, $\mathcal D$ and $\tilde{\mathcal D}$ change sign.
> - $\Lambda_{1/2}$ maps the solutions at $p$ onto those at $\Lambda p$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-9|Theorem §C5a.12.9]], 2) but not $u^s(p)$ to $u^s(\Lambda p)$: the label $s$ is defined in the rest frame, and the rest frames reached from $p$ and from $\Lambda p$ by pure boosts differ by the rotation $W(\Lambda, p)$. Spin sums do not notice, $\mathcal D$ being unitary.
> - Used next: [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]], where $\mathcal D$ is cancelled by the transformation of the mode operators.

^der-lem-c5b-4-1

*Uses:* [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-9|Theorem §C5a.12.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C3.6★ Particle States and the Little Group#^def-c3-6-2|Def. §C3.6.2]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-4|Theorem §C3.6.4]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-10|Theorem §C3.6.10]], [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-3|Theorem §C9.6.3]], [[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]

> [!theorem]- ★ Theorem §C5b.4.4: Lorentz Covariance of the Quantized Dirac Field
> Let $m > 0$. For each spinor matrix $\Lambda_{1/2}$ of a proper orthochronous Lorentz transformation $\Lambda$ let $U(\Lambda)$ be the linear operator on the fermionic Fock space ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]]) with $U(\Lambda)|0\rangle = |0\rangle$ that acts on the one-particle states of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]] by the spin-$\frac12$ law of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]], with the matrices $\mathcal D = \mathcal D(\Lambda_{1/2}, p)$, $\tilde{\mathcal D}$ of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]],
>
> $$
> U(\Lambda)\,|\mathbf p, s\rangle = \sum_r\mathcal D_{rs}\,|\Lambda\mathbf p, r\rangle, \qquad U(\Lambda)\,|\mathbf p, s\rangle^c = \sum_r(\tilde{\mathcal D}_{rs})^{\ast}\,|\Lambda\mathbf p, r\rangle^c ,
> $$
>
> and on multiparticle states factor by factor ($\Lambda\mathbf p$ is the spatial part of $\Lambda p$, $p^0 = E_{\mathbf p}$). Then:
> 1. $U(\Lambda)$ is unitary and $U(\Lambda')\,U(\Lambda) = U(\Lambda'\Lambda)$ for the product $\Lambda'_{1/2}\Lambda_{1/2}$: a unitary representation of the covering group $SL(2, \mathbb C)$, as [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]] requires for half-integer spin ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-3|Theorem §C3.4.3]]). The two matrices $\pm\Lambda_{1/2}$ of one $\Lambda$ give operators that differ by $(-1)^F$, $F$ the number of fermions plus antifermions.
> 2. The mode operators transform as
>
> $$
> U(\Lambda)\,\hat a^{s\dagger}_{\mathbf p}\,U(\Lambda)^{-1} = \sqrt{\frac{E_{\Lambda\mathbf p}}{E_{\mathbf p}}}\,\sum_r\mathcal D_{rs}\,\hat a^{r\dagger}_{\Lambda\mathbf p}, \qquad U(\Lambda)\,\hat b^{s\dagger}_{\mathbf p}\,U(\Lambda)^{-1} = \sqrt{\frac{E_{\Lambda\mathbf p}}{E_{\mathbf p}}}\,\sum_r(\tilde{\mathcal D}_{rs})^{\ast}\,\hat b^{r\dagger}_{\Lambda\mathbf p} ,
> $$
>
> and, taking adjoints, $U\hat a^s_{\mathbf p}U^{-1} = \sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}\,\sum_r(\mathcal D_{rs})^{\ast}\,\hat a^r_{\Lambda\mathbf p}$, $U\hat b^s_{\mathbf p}U^{-1} = \sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}\,\sum_r\tilde{\mathcal D}_{rs}\,\hat b^r_{\Lambda\mathbf p}$.
> 3. The Heisenberg field ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]]) transforms as
>
> $$
> U(\Lambda)\,\hat\psi(x)\,U(\Lambda)^{-1} = \Lambda_{1/2}^{-1}\,\hat\psi(\Lambda x), \qquad\text{equivalently}\qquad U(\Lambda)^{-1}\,\hat\psi(x)\,U(\Lambda) = \Lambda_{1/2}\,\hat\psi(\Lambda^{-1}x) ,
> $$
>
> and $U(\Lambda)\,\hat{\bar\psi}(x)\,U(\Lambda)^{-1} = \hat{\bar\psi}(\Lambda x)\,\Lambda_{1/2}$, as operator-valued distributions. So [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]] holds for the free Dirac field with $D = \Lambda_{1/2}$.
>
> With $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]), $(\tilde{\mathcal D}_{rs})^{\ast} = \mathcal D_{rs}$: antifermion states transform exactly as fermion states. Where the Wigner rotation is trivial, $\mathcal D = \mathbb 1$ (a boost along $\pm\hat{\mathbf p}$), part 2 is Peskin–Schroeder's $U(\Lambda)\,\hat a^s_{\mathbf p}\,U^{-1}(\Lambda) = \sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}\;\hat a^s_{\Lambda\mathbf p}$, eq. (3.109) ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^cau-c5b-4-1|★ Caution: When Peskin–Schroeder's eq. (3.109) holds as printed]]).
>
> *Scalar analogue:* [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]] (the representation and the mode operators), [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]] (the field).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, $m > 0$, relativistic normalization; exact; Lorentz transformations only (translations act by $e^{i\hat P\cdot a}$, [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|Theorem §C3.4.6]], 3).
>
> *Source: PS §3.5, pp. 59–60, eqs. (3.106)–(3.110) (the computation, for the particle term and $\mathcal D = \mathbb 1$) · Yu §5.1, eqs. (5.57)–(5.61) (the law in the form $U^{-1}(\Lambda)\psi(x)U(\Lambda) = D(\Lambda)\psi(\Lambda^{-1}x)$, stated as the covariance of the quantum Dirac field) · the Wigner matrices, unitarity, composition and the antifermion term written out here on the pattern of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]] and [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]]*

^thm-c5b-4-4

> [!derivation]- Derivation
> Write $d\mu(p) \equiv \frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}$ for the invariant measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and $\hat\alpha^{s\dagger}_{\mathbf p} \equiv \sqrt{2E_{\mathbf p}}\,\hat a^{s\dagger}_{\mathbf p}$, $\hat\beta^{s\dagger}_{\mathbf p} \equiv \sqrt{2E_{\mathbf p}}\,\hat b^{s\dagger}_{\mathbf p}$ for the creation operators of the relativistically normalized states, $|\mathbf p, s\rangle = \hat\alpha^{s\dagger}_{\mathbf p}|0\rangle$, $|\mathbf p, s\rangle^c = \hat\beta^{s\dagger}_{\mathbf p}|0\rangle$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]). The steps follow those of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-4|Derivation §C3.5.4]] and [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-5|Derivation §C3.5.5]]; what is new is the matrix $\mathcal D$.
>
> **Step 1** (wave packets). A one-fermion state is $|g\rangle = \sum_s\int d\mu(p)\,g_s(\mathbf p)\,|\mathbf p, s\rangle$. By the overlap $\langle\mathbf p, r|\mathbf q, s\rangle = 2E_{\mathbf p}(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]) the $\mathbf q$-integral against the delta cancels one measure: $\langle g|h\rangle = \sum_s\int d\mu(p)\,\overline{g_s(\mathbf p)}\,h_s(\mathbf p)$, the space $\mathbb C^2\otimes L^2(d\mu)$ of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]].
>
> **Step 2** ($U$ on wave packets). Apply the definition under the integral and substitute $q = \Lambda p$ on the mass shell. The substitution maps the shell onto itself (an orbit of $SO^+(1,3)$, [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]), the measure is invariant, $d\mu(p) = d\mu(q)$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], 2), and $p = \Lambda^{-1}q$:
>
> $$
> U(\Lambda)|g\rangle = \sum_{s,r}\int d\mu(p)\,g_s(\mathbf p)\,\mathcal D_{rs}(\Lambda_{1/2}, p)\,|\Lambda\mathbf p, r\rangle = \sum_r\int d\mu(q)\,\Bigl[\sum_s\mathcal D_{rs}(\Lambda_{1/2}, \Lambda^{-1}q)\,g_s(\Lambda^{-1}\mathbf q)\Bigr]\,|\mathbf q, r\rangle .
> $$
>
> So $(Ug)_r(\mathbf q) = \sum_s\mathcal D_{rs}(\Lambda_{1/2}, \Lambda^{-1}q)\,g_s(\Lambda^{-1}\mathbf q)$: the scalar's $g(\Lambda^{-1}\mathbf q)$ with a unitary matrix acting on the spin label.
>
> **Step 3** ($U$ preserves the norm). $\mathcal D$ is unitary at each momentum ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], 2), so $\sum_r|(Ug)_r(\mathbf q)|^2 = \sum_s|g_s(\Lambda^{-1}\mathbf q)|^2$, and by the invariance of the measure (substituting back $p = \Lambda^{-1}q$)
>
> $$
> \|U(\Lambda)g\|^2 = \int d\mu(q)\,\sum_s|g_s(\Lambda^{-1}\mathbf q)|^2 = \int d\mu(p)\,\sum_s|g_s(\mathbf p)|^2 = \|g\|^2 .
> $$
>
> The same holds for antifermion packets, $(\tilde{\mathcal D})^{\ast}$ being unitary as well.
>
> **Step 4** (composition, and $U$ is onto). Apply $U(\Lambda)$ and then $U(\Lambda')$ to a kernel state:
>
> $$
> U(\Lambda')\,U(\Lambda)\,|\mathbf p, s\rangle = \sum_r\mathcal D_{rs}(\Lambda_{1/2}, p)\,U(\Lambda')\,|\Lambda\mathbf p, r\rangle = \sum_t\Bigl[\sum_r\mathcal D_{tr}(\Lambda'_{1/2}, \Lambda p)\,\mathcal D_{rs}(\Lambda_{1/2}, p)\Bigr]\,|\Lambda'\Lambda\mathbf p, t\rangle = \sum_t\mathcal D_{ts}(\Lambda'_{1/2}\Lambda_{1/2}, p)\,|\Lambda'\Lambda\mathbf p, t\rangle ,
> $$
>
> by [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], 3: the law for $\Lambda'_{1/2}\Lambda_{1/2}$. For antifermions the complex conjugate of a product of matrices is the product of the conjugates, so $(\tilde{\mathcal D})^{\ast}$ composes in the same way. Continuity in $\Lambda_{1/2}$ holds as for the scalar (Step 4 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-4|Derivation §C3.5.4]]), $w$ depending continuously on $\Lambda_{1/2}$ and $p$. With $\Lambda'_{1/2} = \Lambda_{1/2}^{-1}$ the product is $\mathbb 1$, for which $w = \mathbb 1$ and $U = \mathbb 1$: $U(\Lambda^{-1})$, taken with $\Lambda_{1/2}^{-1}$, undoes $U(\Lambda)$, so $U(\Lambda)$ is onto. An onto isometry is unitary ([[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-51|LADR Def. 7.51]]).
>
> **Step 5** (Fock space). On a state of $n$ fermions and $\bar n$ antifermions $U$ acts on each momentum and spin label as in Step 2. Steps 2–4 go through factor by factor with the product measure, because the multiparticle overlaps are sums over permutations, with signs, of products of the invariant one-particle kernels ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], 3); antisymmetric wave functions go to antisymmetric ones, the same matrix acting in every slot. With $U|0\rangle = |0\rangle$ this is part 1. Changing the sign of $\Lambda_{1/2}$ changes the sign of $w$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]]), hence of $\mathcal D$ and $\tilde{\mathcal D}$, once for every particle: the factor $(-1)^F$.
>
> **Step 6** (the mode operators). $\hat\alpha^{s\dagger}_{\mathbf p}$ adds a fermion to a product state, $\hat\alpha^{s\dagger}_{\mathbf p}|\mathbf q_1r_1; \dots\rangle = |\mathbf p s; \mathbf q_1r_1; \dots\rangle$. Apply $U$ and use Step 5 for the first slot and for the rest:
>
> $$
> U\,\hat\alpha^{s\dagger}_{\mathbf p}\,|\mathbf q_1r_1; \dots\rangle = \sum_r\mathcal D_{rs}\,\hat\alpha^{r\dagger}_{\Lambda\mathbf p}\;U|\mathbf q_1r_1; \dots\rangle .
> $$
>
> The states $U|\mathbf q_1r_1; \dots\rangle$ span Fock space ($U$ is onto), so $U\hat\alpha^{s\dagger}_{\mathbf p}U^{-1} = \sum_r\mathcal D_{rs}\,\hat\alpha^{r\dagger}_{\Lambda\mathbf p}$, an identity of operator-valued distributions in $\mathbf p$ (smeared with a packet as in Step 2). Dividing by $\sqrt{2E_{\mathbf p}}$ and writing $\hat\alpha^{r\dagger}_{\Lambda\mathbf p} = \sqrt{2E_{\Lambda\mathbf p}}\,\hat a^{r\dagger}_{\Lambda\mathbf p}$ gives the first formula of part 2; the same with $\hat\beta^\dagger$ and $(\tilde{\mathcal D})^{\ast}$ gives the second. The adjoints follow from $(UXU^{-1})^\dagger = UX^\dagger U^{-1}$ for unitary $U$: $U\hat\alpha^s_{\mathbf p}U^{-1} = \sum_r(\mathcal D_{rs})^{\ast}\,\hat\alpha^r_{\Lambda\mathbf p}$ and $U\hat\beta^{s\dagger}_{\mathbf p}U^{-1} = \sum_r(\tilde{\mathcal D}_{rs})^{\ast}\,\hat\beta^{r\dagger}_{\Lambda\mathbf p}$ are the two that the field contains.
>
> **Step 7** (the field over the invariant measure). Since $\frac{1}{\sqrt{2E_{\mathbf p}}} = \frac{\sqrt{2E_{\mathbf p}}}{2E_{\mathbf p}}$, the expansion of [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], 2, reads
>
> $$
> \hat\psi(x) = \int d\mu(p)\,\sum_s\Bigl(\hat\alpha^s_{\mathbf p}\,u^s(p)\,e^{-ip\cdot x} + \hat\beta^{s\dagger}_{\mathbf p}\,v^s(p)\,e^{ip\cdot x}\Bigr), \qquad p^0 = E_{\mathbf p} ,
> $$
>
> PS's rewriting before eq. (3.110): an invariant integral times operators that transform without a factor.
>
> **Step 8** (conjugate term by term). $U$ passes through the c-number spinors, the exponentials and the integral (*sense:* as for the scalar, Step 2 of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^der-c3-5-5|Derivation §C3.5.5]]: after smearing in $x$ with a Schwartz function the coefficients are Schwartz functions of $\mathbf p$, and the mode operators smeared with them are bounded, [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]). By Step 6,
>
> $$
> U\,\hat\psi(x)\,U^{-1} = \int d\mu(p)\,\sum_r\Bigl(\hat\alpha^r_{\Lambda\mathbf p}\,\Bigl[\sum_s(\mathcal D_{rs})^{\ast}\,u^s(p)\Bigr]\,e^{-ip\cdot x} + \hat\beta^{r\dagger}_{\Lambda\mathbf p}\,\Bigl[\sum_s(\tilde{\mathcal D}_{rs})^{\ast}\,v^s(p)\Bigr]\,e^{ip\cdot x}\Bigr) .
> $$
>
> **Step 9** (the spinor relation). Multiply $\Lambda_{1/2}\,u^s(p) = \sum_tu^t(\Lambda p)\,\mathcal D_{ts}$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], 2) by $(\mathcal D_{rs})^{\ast}$ and sum over $s$; $\sum_s\mathcal D_{ts}(\mathcal D_{rs})^{\ast} = \delta_{tr}$ by unitarity:
>
> $$
> \Lambda_{1/2}\sum_s(\mathcal D_{rs})^{\ast}\,u^s(p) = u^r(\Lambda p), \qquad\text{so}\qquad \sum_s(\mathcal D_{rs})^{\ast}\,u^s(p) = \Lambda_{1/2}^{-1}\,u^r(\Lambda p), \qquad \sum_s(\tilde{\mathcal D}_{rs})^{\ast}\,v^s(p) = \Lambda_{1/2}^{-1}\,v^r(\Lambda p) ,
> $$
>
> the last in the same way from the $v$ relation. For $\mathcal D = \mathbb 1$ the first is PS's $u^s(\Lambda^{-1}\tilde p) = \Lambda_{1/2}^{-1}u^s(\tilde p)$ with $\tilde p = \Lambda p$. The Wigner matrix of the mode operators and that of the spinors have cancelled; the constant matrix $\Lambda_{1/2}^{-1}$ comes out of the integral:
>
> $$
> U\,\hat\psi(x)\,U^{-1} = \Lambda_{1/2}^{-1}\int d\mu(p)\,\sum_r\Bigl(\hat\alpha^r_{\Lambda\mathbf p}\,u^r(\Lambda p)\,e^{-ip\cdot x} + \hat\beta^{r\dagger}_{\Lambda\mathbf p}\,v^r(\Lambda p)\,e^{ip\cdot x}\Bigr) .
> $$
>
> **Step 10** (change variables on the shell). Substitute $q = \Lambda p$ as in Step 2: $d\mu(p) = d\mu(q)$, the shell is mapped onto itself (the change of variables of an invariant distribution, [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]), and in the exponent $p\cdot x = (\Lambda^{-1}q)\cdot x = q\cdot(\Lambda x)$ by the invariance of the Minkowski product:
>
> $$
> U\,\hat\psi(x)\,U^{-1} = \Lambda_{1/2}^{-1}\int d\mu(q)\,\sum_r\Bigl(\hat\alpha^r_{\mathbf q}\,u^r(q)\,e^{-iq\cdot(\Lambda x)} + \hat\beta^{r\dagger}_{\mathbf q}\,v^r(q)\,e^{iq\cdot(\Lambda x)}\Bigr) = \Lambda_{1/2}^{-1}\,\hat\psi(\Lambda x) ,
> $$
>
> PS (3.110).
>
> **Step 11** (the inverse form). Apply Step 10 to $\Lambda_{1/2}^{-1}$, whose operator is $U(\Lambda)^{-1}$ (Step 4): $U^{-1}\hat\psi(x)\,U = \Lambda_{1/2}\,\hat\psi(\Lambda^{-1}x)$, the law of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]] and Yu (5.61), and the classical law of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]] for the operator.
>
> **Step 12** (the conjugate field). Take the adjoint of Step 10, $U\hat\psi^\dagger(x)U^{-1} = \hat\psi^\dagger(\Lambda x)\,(\Lambda_{1/2}^{-1})^\dagger$, and multiply by $\gamma^0$ from the right. From $\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 2) written for $\Lambda_{1/2}^{-1}$, $(\Lambda_{1/2}^{-1})^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}$, so $U\hat{\bar\psi}(x)U^{-1} = \hat\psi^\dagger(\Lambda x)\,\gamma^0\,\Lambda_{1/2} = \hat{\bar\psi}(\Lambda x)\,\Lambda_{1/2}$.
>
> **Step 13** (smeared form). For Schwartz functions $f_a$, $a = 1, \dots, 4$, $U\Bigl[\int d^4x\,f_a(x)\hat\psi_a(x)\Bigr]U^{-1} = \int d^4x\,f_a(x)\,(\Lambda_{1/2}^{-1})_{ab}\,\hat\psi_b(\Lambda x) = \int d^4y\,f_a(\Lambda^{-1}y)\,(\Lambda_{1/2}^{-1})_{ab}\,\hat\psi_b(y)$, with $y = \Lambda x$, $d^4y = |\det\Lambda|\,d^4x = d^4x$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]]): the field smeared with the moved test function.
>
> **What the derivation shows**
> - The same two ingredients as for the scalar, the invariant measure and the relativistic normalization, plus one new cancellation: the rotation of the spin labels of the mode operators against that of the spinors. This is why the field can transform with the finite, non-unitary matrix $\Lambda_{1/2}$ while $U(\Lambda)$ is unitary: the states carry the unitary rest-frame rotation $w$, the spinors $u$, $v$ convert it into $\Lambda_{1/2}$.
> - ⚑ By-product: the antifermion law is not a choice. With any matrix other than $(\tilde{\mathcal D})^{\ast}$ on the antifermion states, the second term of Step 9 would not give $\Lambda_{1/2}^{-1}v^r(\Lambda p)$. For $\eta^s = \xi^{-s}$ it equals $\mathcal D$, the statement that $s$ is the physical spin of the antiparticle ([[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]]).
> - ⚑ By-product: the sign of $\Lambda_{1/2}$ appears on both sides of part 3, in $U$ as $(-1)^F$ and in $\Lambda_{1/2}^{-1}$, and drops out of every bilinear: $U\,\hat{\bar\psi}\hat\psi(x)\,U^{-1} = \hat{\bar\psi}\hat\psi(\Lambda x)$ and $U\,\hat{\bar\psi}\gamma^\mu\hat\psi(x)\,U^{-1} = (\Lambda^{-1})^\mu{}_\nu\,\hat{\bar\psi}\gamma^\nu\hat\psi(\Lambda x)$, using $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], 3, for $\Lambda^{-1}$).
> - Check against [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]: for a rotation by $\theta$ about $z$, $w = e^{-i\theta\sigma^3/2}$, and with $U = e^{-i\theta\hat J_z}$ ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|Theorem §C3.4.6]], 4) the first order in $\theta$ of part 2 at $\mathbf p = 0$ is $\hat J_z\,\hat a^{s\dagger}_{\mathbf 0}|0\rangle = \sum_r(\xi^{r\dagger}\frac{\sigma^3}{2}\xi^s)\,\hat a^{r\dagger}_{\mathbf 0}|0\rangle$ and $\hat J_z\,\hat b^{s\dagger}_{\mathbf 0}|0\rangle = -\sum_r(\eta^{s\dagger}\frac{\sigma^3}{2}\eta^r)\,\hat b^{r\dagger}_{\mathbf 0}|0\rangle$, the two formulas found there from the Noether charge. That the operators $U(\Lambda)$ constructed here are generated by the Noether charges for all six generators (for the scalar: [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]]) is not derived in these notes.

^der-c5b-4-4

*Uses:* [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]]

> [!caution]- ★ Caution: When Peskin–Schroeder's eq. (3.109) holds as printed
> Peskin–Schroeder write $U(\Lambda)\,\hat a^s_{\mathbf p}\,U^{-1}(\Lambda) = \sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}\;\hat a^s_{\Lambda\mathbf p}$ and $u^s(\Lambda^{-1}\tilde p) = \Lambda_{1/2}^{-1}u^s(\tilde p)$, "assuming that the axis of spin quantization is parallel to the boost or rotation axis". With the spinors of [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]] both hold as printed where $w = \mathbb 1$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]], 4): a boost along $\pm\hat{\mathbf p}$. For a boost along the spin axis of a particle moving in another direction, $w$ is a rotation about the axis perpendicular to both and mixes the two labels. For a rotation by $\theta$ about the spin axis each relation acquires a phase, $\Lambda_{1/2}u^s(p) = e^{\mp i\theta/2}u^s(Rp)$ and $U\hat a^s_{\mathbf p}U^{-1} = e^{\pm i\theta/2}\,\hat a^s_{R\mathbf p}$ (upper signs for spin up along the axis). In every case the two matrices cancel in the product of mode operator and spinor, so eq. (3.110) holds for every $\Lambda$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]], 3).
>
> *Source: PS §3.5, p. 59 · checked numerically for the chiral-basis spinors (boost along $z$ with $\mathbf p$ along $x$; rotation about $z$)*

^cau-c5b-4-1

> [!remark]- ★ Remark: Lorentz covariance of the quantized field
> With $U(\Lambda)\hat a^s_{\mathbf p}U^{-1}(\Lambda) = \sqrt{E_{\Lambda p}/E_{\mathbf p}}\,\hat a^s_{\Lambda\mathbf p}$ (spin axis along the boost or rotation axis) and the covariance of the spinors, Peskin–Schroeder obtain $U(\Lambda)\hat\psi(x)U^{-1}(\Lambda) = \Lambda_{1/2}^{-1}\hat\psi(\Lambda x)$, eqs. (3.108)–(3.110): the spinor instance ($D = \Lambda_{1/2}$, [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]], which for the free scalar was a theorem ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]]). For general spin axes the mode operators transform with the Wigner rotation of [[§C3.6★ Particle States and the Little Group#^thm-c3-6-5|Theorem §C3.6.5]] ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^lem-c5b-4-1|★ Lemma §C5b.4.1]]). Derived, with the Wigner rotation kept, in [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]] (Peskin–Schroeder, pp. 59–60); $\langle\mathbf p, r|\mathbf q, s\rangle$ is Lorentz invariant ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]), which is what makes $U(\Lambda)$ unitary although $\Lambda_{1/2}$ is not.
>
> *Source: PS §3.5, pp. 59–60, eqs. (3.106)–(3.110)*

^rem-c5b-4-1

> [!remark] Remark: Why the Dirac field has no coherent states
> The scalar field becomes classical in coherent states, eigenstates of every annihilator with c-number eigenvalues ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]); C5b has no section corresponding to [[§C2a.6 Coherent States and the Classical Field|§C2a.6]], for two reasons. (1) A smeared fermion annihilator is nilpotent, $\hat a^s(g)^2 = 0$ (the adjoint of part 2 of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]). If $\hat a^s(g)\Psi = \alpha\Psi$ with $\Psi \ne 0$, then $0 = \hat a^s(g)^2\Psi = \alpha^2\Psi$, so $\alpha = 0$: no c-number eigenvalue other than zero exists. (2) The field changes the charge by one unit, $[\hat Q, \hat\psi] = -\hat\psi$ ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]), so in every eigenstate of $\hat Q$ the mean field $\langle\Psi|\hat\psi(x)|\Psi\rangle$ vanishes: $\hat\psi\Psi$ has charge one unit lower than $\Psi$ and is orthogonal to it. Physically, the Pauli principle forbids the macroscopic occupation of one mode that makes the scalar field classical ([[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|§C2a.6, Remark: Why a definite field needs an indefinite particle number]]); a classical Dirac field is not the expectation value of the quantum one. Fermionic coherent states need anticommuting (Grassmann) eigenvalues and appear with the path integral for fermions (PHY 513 Lecture 26; QFT C11, planned).
>
> *Source: argued here from Theorem §C5b.4.2 and Theorem §C5b.5.4 (none of the course sources treats fermionic coherent states before the path integral)*

^rem-c5b-4-2

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], part 1 — a smooth prefactor is evaluated on the support of δ: $\sqrt{2E_{\mathbf p}2E_{\mathbf q}}\,\delta^3(\mathbf p - \mathbf q) = 2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ in the norms of the one-particle states (Derivation §C5b.4.1).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — $\int d^3x\,e^{i\mathbf p\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p)$ in $\mathcal S'$: the space integral of the field keeps only the zero-momentum modes (Derivation §C5b.4.3).
> - [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]] — integration by parts with fall-off: the orbital term of $\hat J_z$ drops out on the zero-momentum states (Derivation §C5b.4.3).
> - [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]] — linear change of variables in a distribution: the substitution $q = \Lambda p$ on the mass shell, with the invariant measure of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] (Derivation §C5b.4.4, ★).

> [!remark]- Connections
> - The fermionic Fock space is the antisymmetric Fock space of nonrelativistic second quantization, built twice (fermions and antifermions) with the invariant measure; the field fixes which operators annihilate the vacuum by positivity of the energy — [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-4|§C5b.3, Remark: Empty and filled are labels]].
> - The minus sign in the two-fermion overlap is the field-theory origin of the antisymmetric wave functions of identical fermions and of the Pauli principle used for atoms — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]], [[§B7.1 Two-Particle Systems, Bosons and Fermions|QM §B7.1]], [[§A5.3 The Exclusion Principle and the Periodic Table#^pr-a5-3-2|QM Principle §A5.3.2]].
> - At most one fermion per state is what gives the Fermi–Dirac occupation numbers of statistical mechanics, $\bar n = 1/(e^{\beta(E-\mu)} + 1)$, as Bose symmetry gives the Bose–Einstein ones — [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions|TH §B10.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]].
> - The one-particle states are the massive spin-½ representations of the Poincaré group, with the spin read off from the rest-frame two-spinors — [[§C3.6★ Particle States and the Little Group|§C3.6★]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|★ Theorem §C5b.4.4]].
> - The one-particle wave functions of these states are $u^s(p)e^{-ip\cdot x}$ and $\bar v^s(p)e^{-ip\cdot x}$, the external-line factors of fermion Feynman rules — [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|§C6d.2, Theorem §C6d.2.1]].
