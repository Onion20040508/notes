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

*Sources: the user's PHY 513 notes, Ch. 10 §10.6 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part C, slides 20–21 and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 57–61 · Yu Zhao-Huan, 量子场论讲义, §5.5.4 · the user's pre-course notes, §5.5.*

This is the spinor counterpart of [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]: with the Hamiltonian diagonal and positive ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]) and the ladder relations in hand ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]), what are the states? The vacuum and the Fock space are built as for the scalar, with the relativistic normalization unchanged; the spin-specific additions are the two spin states per momentum, the antisymmetry of every multiparticle state, and with it the Pauli exclusion principle, which here is a consequence of the anticommutators and not a postulate ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-3|§C5b.1, Remark: Spin and statistics are an output]]). The charges of the two species are in [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]]. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The vacuum and the one-particle states

> [!principle] Principle §C5b.4.1: The Dirac Vacuum and the Fermionic Fock Space
> There is a normalized state $|0\rangle$, unique up to a phase, with $a^s_{\mathbf p}|0\rangle = b^s_{\mathbf p}|0\rangle = 0$ for all $\mathbf p$, $s$, and the space of states is the Fock space it generates with the creation operators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]],
>
> $$
> \mathcal F = \bigoplus_{n,\bar n\ge0}\Lambda^n\mathcal H_1\otimes\Lambda^{\bar n}\bar{\mathcal H}_1, \qquad \mathcal H_1 \cong \bar{\mathcal H}_1 \cong \mathbb C^2\otimes L^2\Bigl(\mathbb R^3, \frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigr) ,
> $$
>
> antisymmetric powers ($\Lambda^n$) of the one-fermion and one-antifermion spaces, with spin label $s$ and the invariant measure of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]; inner products are computed by moving annihilators to the right with the anticommutators, one sign per exchange.
>
> *Domain:* the free Dirac field. That the annihilators are $b$ and not $b^\dagger$ is fixed by positivity of the energy ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-4|§C5b.3, Remark: Empty and filled are labels]]), not by the expansion; irreducibility is asserted, as for the scalar ([[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]]).
>
> *Scalar analogue:* [[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]].
> *Source: Lecture 10, slides 20–21 · the user's PHY 513 notes, Ch. 10 §10.6 · PS §3.5, eq. (3.103) · Yu §5.5.4, eqs. (5.268)–(5.269) · the user's pre-course notes, §5.5*

^pr-c5b-4-1

> [!theorem] Theorem §C5b.4.2: Fermions and Antifermions
> The one-particle states
>
> $$
> |\mathbf p, s\rangle \equiv \sqrt{2E_{\mathbf p}}\,a^{s\dagger}_{\mathbf p}|0\rangle, \qquad |\mathbf p, s\rangle^c \equiv \sqrt{2E_{\mathbf p}}\,b^{s\dagger}_{\mathbf p}|0\rangle
> $$
>
> (the vacuum of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], relativistic normalization as in [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) are eigenstates of $:\!H\!:$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]) with eigenvalue $+E_{\mathbf p}$ and carry momentum $\mathbf p$ and spin label $s$: $a^\dagger$ creates a **particle** (fermion; for the electron field an electron) and $b^\dagger$ an **antiparticle** (antifermion; a positron), the $c$ standing for "conjugate". Both have mass $m$ and two spin states; their charges are opposite ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]). Their overlaps are positive and Lorentz invariant,
>
> $$
> \langle\mathbf p, r|\mathbf q, s\rangle = {}^c\langle\mathbf p, r|\mathbf q, s\rangle^c = 2E_{\mathbf p}(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q), \qquad {}^c\langle\mathbf p, r|\mathbf q, s\rangle = 0 ,
> $$
>
> distributions in $(\mathbf p, \mathbf q)$ as for the scalar ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]]); physical states are wave packets ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]).
>
> *Scalar analogue:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]; complex field [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]].
> *Source: Lecture 10, slide 20 ("a† ∼ particle, b† ∼ anti-particle") · the user's PHY 513 notes, Ch. 10 §10.6 (Principle "One-particle states") · PS §3.5, eqs. (3.106)–(3.107) · Yu §5.5.4, eqs. (5.270)–(5.275) · the user's pre-course notes, §5.5*

^thm-c5b-4-2

> [!derivation]- Derivation
> **1. Eigenvalues.** $:\!H\!:|0\rangle = \mathbf P|0\rangle = 0$ (each term ends in an annihilator). By [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], $:\!H\!:a^{s\dagger}_{\mathbf p}|0\rangle = [{:}H{:}, a^{s\dagger}_{\mathbf p}]|0\rangle + a^{s\dagger}_{\mathbf p}{:}H{:}|0\rangle = E_{\mathbf p}a^{s\dagger}_{\mathbf p}|0\rangle$; the same for $\mathbf P$ (eigenvalue $\mathbf p$) and for $b^{s\dagger}_{\mathbf p}$. (With the unordered $H$ both energies are shifted by $E_0^{(\rm D)}$, Yu (5.274).) The charges: Step 6 of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-4|Derivation §C5b.5.4]].
>
> **2. Overlaps.** $\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle = \langle0|\bigl(\{a^r_{\mathbf p}, a^{s\dagger}_{\mathbf q}\} - a^{s\dagger}_{\mathbf q}a^r_{\mathbf p}\bigr)|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$; multiplying by $\sqrt{2E_{\mathbf p}2E_{\mathbf q}}$ and evaluating on the support of δ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1) gives $2E_{\mathbf p}$ (Lecture 10: "since $\langle0|aa^\dagger|0\rangle = \langle0|\{a, a^\dagger\}|0\rangle$"). The same for $b$. Lorentz invariance of this normalization is the scalar's ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]). Mixed: $\langle0|b^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle = -\langle0|a^{s\dagger}_{\mathbf q}b^r_{\mathbf p}|0\rangle = 0$, since $\{b, a^\dagger\} = 0$.
>
> **3. Positivity.** With commutators the $b$-overlap had the opposite sign ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], 1); the anticommutator restores it. Smeared, $\|a^{s\dagger}(g)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3}|g|^2 > 0$.
>
> **What the derivation shows**
> - Both species have the same dispersion $E_{\mathbf p}$ because both sit in one field on one mass shell; opposite charge because they sit in its two frequency parts, as for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]).
> - Particles and antiparticles stand on the same footing: two spin states each and the same energy; nothing but convention decided which is called which ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-2|§C5b.2, Remark: ψ̄ is ψ with particles and antiparticles interchanged]]).

^der-c5b-4-2

*Uses:* [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, steps 6–7]]

## Many particles: Fermi–Dirac statistics

> [!theorem] Theorem §C5b.4.3: Fermi–Dirac Statistics and the Pauli Exclusion Principle
> In the Fock space of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], with the algebra of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]:
> 1. $a^{r\dagger}_{\mathbf p}a^{s\dagger}_{\mathbf q} = -a^{s\dagger}_{\mathbf q}a^{r\dagger}_{\mathbf p}$ (likewise for $b^\dagger$, and $a^\dagger b^\dagger = -b^\dagger a^\dagger$): a multiparticle state changes sign when two identical quanta are exchanged. The quanta are fermions.
> 2. *(Pauli)* $a^{s\dagger}(g)^2 = b^{s\dagger}(g)^2 = 0$ for every wave packet $g$: no two identical fermions occupy the same one-particle state (spin label and packet); in kernel form, $a^{s\dagger}_{\mathbf p}a^{s\dagger}_{\mathbf p}|0\rangle = 0$.
> 3. For $|\mathbf p_1s_1; \mathbf p_2s_2\rangle \equiv \sqrt{4E_{\mathbf p_1}E_{\mathbf p_2}}\,a^{s_1\dagger}_{\mathbf p_1}a^{s_2\dagger}_{\mathbf p_2}|0\rangle$,
>
> $$
> \langle\mathbf q_1r_1; \mathbf q_2r_2|\mathbf p_1s_1; \mathbf p_2s_2\rangle = 4E_{\mathbf p_1}E_{\mathbf p_2}(2\pi)^6\Bigl[\delta^{r_1s_1}\delta^{r_2s_2}\delta^3(\mathbf p_1 - \mathbf q_1)\delta^3(\mathbf p_2 - \mathbf q_2) - \delta^{r_1s_2}\delta^{r_2s_1}\delta^3(\mathbf p_1 - \mathbf q_2)\delta^3(\mathbf p_2 - \mathbf q_1)\Bigr] ,
> $$
>
> with a minus sign where two bosons have a plus ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]).
>
> *Source: Lecture 10, slide 21 and transcript · the user's PHY 513 notes, Ch. 10 §10.6 (Principle "Many-particle states: Fermi–Dirac statistics and the exclusion principle") · PS §3.5, p. 57 · Yu §5.5.4, eqs. (5.289)–(5.295) · the user's pre-course notes, §5.5*

^thm-c5b-4-3

> [!derivation]- Derivation
> **1. Antisymmetry.** $\{a^{r\dagger}_{\mathbf p}, a^{s\dagger}_{\mathbf q}\} = 0$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]); similarly for $b^\dagger$ and between $a^\dagger$, $b^\dagger$. In a product of creation operators acting on $|0\rangle$, moving one past another costs $-1$; exchanging the $i$-th and $j$-th takes an odd number of adjacent moves, so the state changes sign (Yu (5.290)–(5.291)).
>
> **2. Pauli.** Smeared, $\{a^{s\dagger}(g), a^{s\dagger}(g)\} = 0$, i.e. $2a^{s\dagger}(g)^2 = 0$. The kernel form is the statement at coinciding labels, which the identity $\{a^{s\dagger}_{\mathbf p}, a^{s\dagger}_{\mathbf q}\} = 0$ contains (its right side has no δ, so no valueless constant arises at $\mathbf p = \mathbf q$). ⚑ By-product: exclusion is a consequence of the anticommutators, not an extra input, and it holds for every one-particle state at once → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].
>
> **3. Two-particle overlap: first annihilator.** $\langle\mathbf q_1r_1; \mathbf q_2r_2| = \sqrt{4E_{\mathbf q_1}E_{\mathbf q_2}}\langle0|a^{r_2}_{\mathbf q_2}a^{r_1}_{\mathbf q_1}$. Move $a^{r_1}_{\mathbf q_1}$ to the right:
>
> $$
> a^{r_1}_{\mathbf q_1}a^{s_1\dagger}_{\mathbf p_1}a^{s_2\dagger}_{\mathbf p_2}|0\rangle = (2\pi)^3\delta^{r_1s_1}\delta^3(\mathbf q_1 - \mathbf p_1)\,a^{s_2\dagger}_{\mathbf p_2}|0\rangle - a^{s_1\dagger}_{\mathbf p_1}\,(2\pi)^3\delta^{r_1s_2}\delta^3(\mathbf q_1 - \mathbf p_2)|0\rangle ,
> $$
>
> the minus sign from passing $a^{s_1\dagger}_{\mathbf p_1}$.
>
> **4. Second annihilator.** $\langle0|a^{r_2}_{\mathbf q_2}a^{s\dagger}_{\mathbf p}|0\rangle = (2\pi)^3\delta^{r_2s}\delta^3(\mathbf q_2 - \mathbf p)$ for both terms: direct minus exchanged. The prefactor $\sqrt{16E_{\mathbf q_1}E_{\mathbf q_2}E_{\mathbf p_1}E_{\mathbf p_2}}$ is $4E_{\mathbf p_1}E_{\mathbf p_2}$ on the support of either product of deltas. *Sense:* an identity of distributions in the four momenta; paired with packets it is $\langle g_1, h_1\rangle\langle g_2, h_2\rangle - \langle g_1, h_2\rangle\langle g_2, h_1\rangle$, as in [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-3|Derivation §C2a.4.3]], step 3, with the sign changed.
>
> **What the derivation shows**
> - Fermi statistics comes with the field; Quantum Mechanics had to postulate it per species ([[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]; same algebra, [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]]).

^der-c5b-4-3

*Uses:* [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

## Spin and Lorentz covariance of the quanta

> [!theorem] Theorem §C5b.4.4: Dirac Quanta Have Spin One-Half
> With the angular momentum $\mathbf J = \int d^3x\,:\!\psi^\dagger\bigl(\mathbf x\times(-i\nabla) + \tfrac12\boldsymbol\Sigma\bigr)\psi\!:$ of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-13|Theorem §C5a.4.13]] (normal ordered, [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], so $\mathbf J|0\rangle = 0$; $\boldsymbol\Sigma = \operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]) and the spin bases $\xi^s$, $\eta^s$ of [[§C5a.5 Plane-Wave Solutions#^def-c5a-5-3|Def. §C5a.5.3]], the zero-momentum states satisfy
>
> $$
> J_z\,a^{s\dagger}_{\mathbf 0}|0\rangle = \sum_r\Bigl(\xi^{r\dagger}\tfrac{\sigma^3}{2}\xi^s\Bigr)a^{r\dagger}_{\mathbf 0}|0\rangle, \qquad J_z\,b^{s\dagger}_{\mathbf 0}|0\rangle = -\sum_r\Bigl(\eta^{s\dagger}\tfrac{\sigma^3}{2}\eta^r\Bigr)b^{r\dagger}_{\mathbf 0}|0\rangle .
> $$
>
> For $\sigma^3$-eigenvectors $\xi^s, \eta^s \in \{(1, 0)^T, (0, 1)^T\}$: the fermion has $J_z = \pm\frac12$, the antifermion $J_z = \mp\frac12$, opposite to its two-spinor.
>
> *Source: PS §3.5, pp. 60–61, eqs. (3.111)–(3.112)*

^thm-c5b-4-4

> [!derivation]- Derivation
> **1. Reduce to a commutator.** $J_z|0\rangle = 0$, so $J_za^{s\dagger}_{\mathbf 0}|0\rangle = [J_z, a^{s\dagger}_{\mathbf 0}]|0\rangle$ (PS). With $J_z = \int d^3x\,\psi^\dagger_aM_{ab}\psi_b$, $M = (\mathbf x\times(-i\nabla))_z + \frac12\Sigma^3$, the identity of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]] gives $[\psi^\dagger_aM_{ab}\psi_b, C] = \psi^\dagger_aM_{ab}\{\psi_b, C\} - \{\psi^\dagger_a, C\}M_{ab}\psi_b$ (the normal-ordering constant commutes).
>
> **2. The anticommutators with $a^{s\dagger}_{\mathbf 0}$.** From [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], $\{\psi(x), a^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}u^s(0)e^{-imt}$ (the $\mathbf p$-integral against $(2\pi)^3\delta^3(\mathbf p)$; $E_{\mathbf 0} = m$) and $\{\psi^\dagger(x), a^{s\dagger}_{\mathbf 0}\} = 0$. So $[J_z, a^{s\dagger}_{\mathbf 0}] = \frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,\psi^\dagger(x)\,M\,u^s(0)$.
>
> **3. Orbital part.** $u^s(0)$ is constant in $\mathbf x$, so $(\mathbf x\times(-i\nabla))_zu^s(0) = 0$. Dropped: the orbital term.
>
> **4. Spin part.** $\int d^3x\,\psi^\dagger(x) = \frac{1}{\sqrt{2m}}\sum_r\bigl(a^{r\dagger}_{\mathbf 0}u^{r\dagger}(0)e^{imt} + b^r_{\mathbf 0}v^{r\dagger}(0)e^{-imt}\bigr)$ (the $d^3x$ integral gives $(2\pi)^3\delta^3(\mathbf p)$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). Hence
>
> $$
> [J_z, a^{s\dagger}_{\mathbf 0}] = \frac{1}{2m}\sum_r\Bigl(u^{r\dagger}(0)\tfrac12\Sigma^3u^s(0)\,a^{r\dagger}_{\mathbf 0} + v^{r\dagger}(0)\tfrac12\Sigma^3u^s(0)\,e^{-2imt}\,b^r_{\mathbf 0}\Bigr) .
> $$
>
> **5. Rest-frame spinors.** $u^s(0) = \sqrt m(\xi^s, \xi^s)$, $v^s(0) = \sqrt m(\eta^s, -\eta^s)$ ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-3|Theorem §C5a.5.3]]), and $\Sigma^3 = \operatorname{diag}(\sigma^3, \sigma^3)$: $u^{r\dagger}(0)\Sigma^3u^s(0) = 2m\,\xi^{r\dagger}\sigma^3\xi^s$ and $v^{r\dagger}(0)\Sigma^3u^s(0) = m(\eta^{r\dagger}\sigma^3\xi^s - \eta^{r\dagger}\sigma^3\xi^s) = 0$. Dropped: the $b$ term, identically. This gives the first formula.
>
> **6. Antifermion.** Now $\{\psi(x), b^{s\dagger}_{\mathbf 0}\} = 0$ and $\{\psi^\dagger(x), b^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}v^{s\dagger}(0)e^{-imt}$, so $[J_z, b^{s\dagger}_{\mathbf 0}] = -\frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,v^{s\dagger}(0)M\psi(x)$: the operator now stands on the *right* of the spinor, and the order of the $b$ terms is reversed (PS: "an extra minus sign"). The orbital term is $\int d^3x\,v^{s\dagger}(0)(x\partial_y - y\partial_x)\psi = -\int d^3x\,(\partial_yx - \partial_xy)v^{s\dagger}(0)\psi = 0$ by parts (fall-off; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]). With $\int d^3x\,\psi = \frac{1}{\sqrt{2m}}\sum_r(a^r_{\mathbf 0}u^r(0)e^{-imt} + b^{r\dagger}_{\mathbf 0}v^r(0)e^{imt})$, the $a$ term annihilates $|0\rangle$ (and has $v^\dagger\Sigma^3u = 0$), and $v^{s\dagger}(0)\Sigma^3v^r(0) = 2m\,\eta^{s\dagger}\sigma^3\eta^r$: the second formula.
>
> **7. Sense.** $a^{s\dagger}_{\mathbf 0}$ is the kernel of $a^{s\dagger}(g)$ at $\mathbf p = 0$, and the formulas are identities of operator-valued distributions evaluated there (PS's computation). For packets $g$ near $\mathbf p = 0$ the orbital part and the $\mathbf p$-dependence of $u^s(p)$ add terms that vanish at $\mathbf p = 0$; the general statement is the little-group spin of [[§C3.5★ Particle States and the Little Group#^thm-c3-5-8|Theorem §C3.5.8]] (draft: to be revisited after Lecture 10).
>
> ⚑ By-product: an antifermion built on $\eta^s = (1, 0)^T$ has $J_z = -\frac12$, as a hole in a state of $J_z = +\frac12$ would → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]]; with Yu's helicity labelling ($\eta^s = \lambda\xi_{-\lambda}$, [[§C5a.5 Plane-Wave Solutions#^cau-c5a-5-2|§C5a.5, Caution: η means two things]] and [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-13|Theorem §C5a.6.13]]) the antiparticle's helicity equals its label (Yu (5.276)–(5.286)).
>
> **What the derivation shows**
> - The spin $\frac12$ is that of the rest-frame two-spinors: the field's quanta are the massive spin-$\frac12$ states of Wigner's classification.

^der-c5b-4-4

*Uses:* [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], [[§C3.5★ Particle States and the Little Group#^thm-c3-5-8|Theorem §C3.5.8]]

> [!remark] Remark: Lorentz covariance of the quantized field
> With $U(\Lambda)a^s_{\mathbf p}U^{-1}(\Lambda) = \sqrt{E_{\Lambda p}/E_{\mathbf p}}\,a^s_{\Lambda\mathbf p}$ (spin axis along the boost or rotation axis) and the covariance of the spinors, Peskin–Schroeder obtain $U(\Lambda)\psi(x)U^{-1}(\Lambda) = \Lambda_{1/2}^{-1}\psi(\Lambda x)$, eqs. (3.108)–(3.110): the spinor instance ($D = \Lambda_{1/2}$, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]) of [[§C3.4 Quantum Poincaré Transformations#^pr-c3-4-8|Principle §C3.4.8]], which for the free scalar was a theorem ([[§C3.4 Quantum Poincaré Transformations#^thm-c3-4-12|Theorem §C3.4.12]]). For general spin axes the mode operators transform with the Wigner rotation of [[§C3.5★ Particle States and the Little Group#^thm-c3-5-4|Theorem §C3.5.4]]. Not derived here (draft); $\langle\mathbf p, r|\mathbf q, s\rangle$ is Lorentz invariant ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]), which is what makes $U(\Lambda)$ unitary although $\Lambda_{1/2}$ is not.
>
> *Source: PS §3.5, pp. 59–60, eqs. (3.106)–(3.110)*

^rem-c5b-4-1

> [!remark] Remark: Why the Dirac field has no coherent states
> The scalar field becomes classical in coherent states, eigenstates of every annihilator with c-number eigenvalues ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]); C5b has no section corresponding to [[§C2a.6 Coherent States and the Classical Field|§C2a.6]], for two reasons. (1) A smeared fermion annihilator is nilpotent, $a^s(g)^2 = 0$ (the adjoint of part 2 of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]). If $a^s(g)\Psi = \alpha\Psi$ with $\Psi \ne 0$, then $0 = a^s(g)^2\Psi = \alpha^2\Psi$, so $\alpha = 0$: no c-number eigenvalue other than zero exists. (2) The field changes the charge by one unit, $[Q, \psi] = -\psi$ ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]), so in every eigenstate of $Q$ the mean field $\langle\Psi|\psi(x)|\Psi\rangle$ vanishes: $\psi\Psi$ has charge one unit lower than $\Psi$ and is orthogonal to it. Physically, the Pauli principle forbids the macroscopic occupation of one mode that makes the scalar field classical ([[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|§C2a.6, Remark: Why a definite field needs an indefinite particle number]]); a classical Dirac field is not the expectation value of the quantum one. Fermionic coherent states need anticommuting (Grassmann) eigenvalues and appear with the path integral for fermions (PHY 513 Lecture 26; QFT C11, planned).
>
> *Source: argued here from Theorem §C5b.4.3 and Theorem §C5b.5.4 (none of the course sources treats fermionic coherent states before the path integral)*

^rem-c5b-4-2

> [!remark]- Connections
> - The fermionic Fock space is the antisymmetric Fock space of nonrelativistic second quantization, built twice (fermions and antifermions) with the invariant measure; the field fixes which operators annihilate the vacuum by positivity of the energy — [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-4|§C5b.3, Remark: Empty and filled are labels]].
> - The minus sign in the two-fermion overlap is the field-theory origin of the antisymmetric wave functions of identical fermions and of the Pauli principle used for atoms — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]], [[§B7.1 Two-Particle Systems, Bosons and Fermions|QM §B7.1]], [[§A5.3 The Exclusion Principle and the Periodic Table#^pr-a5-3-2|QM Principle §A5.3.2]].
> - At most one fermion per state is what gives the Fermi–Dirac occupation numbers of statistical mechanics, $\bar n = 1/(e^{\beta(E-\mu)} + 1)$, as Bose symmetry gives the Bose–Einstein ones — [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions|TH §B10.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]].
> - The one-particle states are the massive spin-½ representations of the Poincaré group, with the spin read off from the rest-frame two-spinors — [[§C3.5★ Particle States and the Little Group|§C3.5★]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|Theorem §C5b.4.4]].
> - The one-particle wave functions of these states are $u^s(p)e^{-ip\cdot x}$ and $\bar v^s(p)e^{-ip\cdot x}$, the external-line factors of fermion Feynman rules — [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]], QFT C7 (planned).
