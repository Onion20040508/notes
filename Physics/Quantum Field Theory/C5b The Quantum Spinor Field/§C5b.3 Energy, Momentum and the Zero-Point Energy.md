---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.2 Mode Expansion and the Anticommutator Algebra]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.4 Fermions, Fock Space and the Pauli Principle]] →

*Sources: the user's PHY 513 notes, Ch. 10 §10.5 and §10.6 (first derivation) · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part C, slides 16–19 and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 52–58 · Yu Zhao-Huan, 量子场论讲义, §§5.5.1–5.5.2, §5.5.4 · the user's pre-course notes, §5.5.*

This is the spinor counterpart of [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]] (and of the complex field's Hamiltonian, [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]]). Lecture 10 turns here to the spectrum. The single-particle Hamiltonian ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]]) has eigenvalues $-E_{\mathbf p}$ as well as $+E_{\mathbf p}$; the field Hamiltonian in modes inherits a minus sign on the antiparticle oscillators, with the operators in the "wrong" order; and reordering with the anticommutators turns the sign into a plus, at the price of a negative zero-point energy. The second of Lecture 10's checkpoints, where commutators would leave the energy unbounded below, sits between the unreordered and the reordered Hamiltonian. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The single-particle Hamiltonian and its negative energies

> [!theorem] Theorem §C5b.3.1: The Single-Particle Hamiltonian on Plane Waves
> For the plane-wave solutions of the Dirac equation ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-9|Theorem §C5a.5.9]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-10|Theorem §C5a.5.10]]) and $H_{\text{s.p.}}$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]],
>
> $$
> H_{\text{s.p.}}\,u^s(p)\,e^{-ip\cdot x} = +E_{\mathbf p}\,u^s(p)\,e^{-ip\cdot x}, \qquad H_{\text{s.p.}}\,v^s(p)\,e^{ip\cdot x} = -E_{\mathbf p}\,v^s(p)\,e^{ip\cdot x} .
> $$
>
> In momentum space $H_{\text{s.p.}}(\mathbf p)u^s(p) = E_{\mathbf p}u^s(p)$ and $H_{\text{s.p.}}(\mathbf p)v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$: the eigenvalues of $H_{\text{s.p.}}(\mathbf p)$ are $\pm E_{\mathbf p}$, each twice.
>
> *Source: Lecture 10, slides 16–17 · the user's PHY 513 notes, Ch. 10 §10.5 (Derivation "Its eigenstates: energy $+E_{\mathbf p}$ and $-E_{\mathbf p}$") · PS §3.5, p. 53*

^thm-c5b-3-1

> [!derivation]- Derivation
> **1. Split the Dirac equation into time and space parts.** For $\psi = u^s(p)e^{-ip\cdot x}$, the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]; it holds by [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-9|Theorem §C5a.5.9]]) reads $(i\gamma^0\partial_0 + i\gamma^j\partial_j - m)\psi = 0$. Move the space part to the right: $i\gamma^0\partial_0\psi = (-i\gamma^j\partial_j + m)\psi$.
>
> **2. Multiply by $\gamma^0$ on the left.** With $(\gamma^0)^2 = 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]): $i\partial_0\psi = \gamma^0(-i\gamma^j\partial_j + m)\psi = H_{\text{s.p.}}\psi$.
>
> **3. The time derivative of the plane wave.** $e^{-ip\cdot x} = e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x}$, and $i\partial_0e^{-iE_{\mathbf p}t} = E_{\mathbf p}e^{-iE_{\mathbf p}t}$. So $H_{\text{s.p.}}u^s(p)e^{-ip\cdot x} = E_{\mathbf p}u^s(p)e^{-ip\cdot x}$.
>
> **4. The $v$ solutions.** $v^s(p)e^{ip\cdot x}$ solves the same equation ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-10|Theorem §C5a.5.10]]); Steps 1–2 are identical. Now $e^{ip\cdot x} = e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x}$ and $i\partial_0e^{iE_{\mathbf p}t} = -E_{\mathbf p}e^{iE_{\mathbf p}t}$: the eigenvalue is $-E_{\mathbf p}$.
>
> **5. Momentum space.** On $e^{i\mathbf k\cdot\mathbf x}$, $-i\partial_j \to k^j$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]), so $H_{\text{s.p.}} \to H_{\text{s.p.}}(\mathbf k) = \gamma^0(\gamma^jk^j + m)$. In Step 3 the spatial momentum is $\mathbf k = \mathbf p$: $H_{\text{s.p.}}(\mathbf p)u^s(p) = E_{\mathbf p}u^s(p)$. In Step 4 it is $\mathbf k = -\mathbf p$: $H_{\text{s.p.}}(-\mathbf p)v^s(p) = -E_{\mathbf p}v^s(p)$, i.e., renaming $\mathbf p \to -\mathbf p$, $H_{\text{s.p.}}(\mathbf p)v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$. The four vectors $u^{1,2}(p)$, $v^{1,2}(\tilde p)$ are independent (orthogonal, [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]), so these are all four eigenvalues of the $4\times4$ matrix $H_{\text{s.p.}}(\mathbf p)$.
>
> ⚑ By-product: the time derivative was removed from $\mathcal H$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]), but the solutions still satisfy the full equation, so the eigenvalue of $H_{\text{s.p.}}$ is whatever $i\partial_t$ gives — negative for the $v$ solutions → [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|Caution: Negative energies are a problem only if ψ is a wave function]].
>
> **What the derivation shows**
> - The lecture's route uses only the Dirac equation; a second route, by squaring ($H_{\text{s.p.}}(\mathbf p)$ Hermitian with $H_{\text{s.p.}}(\mathbf p)^2 = E_{\mathbf p}^2$), is Steps 2–3 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-1|Derivation §C5b.2.1]] and Step 7 of [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-9|Derivation §C5a.3.9]].
> - Used next: $H_{\text{s.p.}}$ acting inside $H = \int\psi^\dagger H_{\text{s.p.}}\psi$ multiplies the $u$ terms of the field by $E_{\mathbf p}$ and the $v$ terms by $-E_{\mathbf p}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]]).

^der-c5b-3-1

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-9|Theorem §C5a.5.9]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-10|Theorem §C5a.5.10]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]

> [!caution] Caution: Negative energies are a problem only if ψ is a wave function
> If $H_{\text{s.p.}}$ were the Hamiltonian, as in relativistic quantum mechanics ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]), the states $v^s(p)e^{ip\cdot x}$ would have energy $-E_{\mathbf p}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]]), the spectrum would be unbounded below, and nothing would stop a particle from cascading down forever: a serious physical problem, and the origin of Dirac's hole theory ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]). In quantum field theory $\psi$ is not a wave function but an operator, and the Hamiltonian is $H = \int d^3x\,\psi^\dagger H_{\text{s.p.}}\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]]). Following the principles of quantum field theory, with the right statistics, makes all energies positive ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]). The scalar analogue is [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|§C2b.1, Remark: Negative frequency is creation, not negative energy]].
>
> *Source: Lecture 10, slide 17 ("Relativistic QM: actual Hamiltonian = H_s.p. … Modern QFT: follow principles ⇒ all energies positive") and transcript · the user's PHY 513 notes, Ch. 10 §10.5 (Caution "Negative-energy states: a problem only if ψ is a wave function") · Yu §1.1 (hole theory)*

^cau-c5b-3-1

## The Hamiltonian, before and after reordering

> [!theorem] Theorem §C5b.3.2: The Hamiltonian in Modes, before Any Algebra
> Substituting the expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] into $H = \int d^3x\,\psi^\dagger H_{\text{s.p.}}\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]]) gives, with the operators in the order in which they arise and no (anti)commutation relation used,
>
> $$
> H = \sum_{s}\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\Bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^s_{\mathbf p}b^{s\dagger}_{\mathbf p}\Bigr) ,
> $$
>
> independent of time. The terms that change the number of quanta ($a^\dagger b^\dagger$, $ba$) vanish identically.
>
> *Scalar analogue:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]; complex field [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]].
> *Source: Lecture 10, slides 18–19 · the user's PHY 513 notes, Ch. 10 §10.5, eq. (diracHwrong) · Yu §5.4.3, eq. (5.223) · PS §3.5, eq. (3.90) (in their provisional labelling) · the user's pre-course notes, §5.5*

^thm-c5b-3-2

> [!derivation]- Derivation
> **1. $H_{\text{s.p.}}$ on the modes.** By Steps 3 and 5 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-1|Derivation §C5b.2.1]], $H_{\text{s.p.}}\bigl(u^r(q)e^{-iq\cdot x}\bigr) = E_{\mathbf q}u^r(q)e^{-iq\cdot x}$ and $H_{\text{s.p.}}\bigl(v^r(q)e^{iq\cdot x}\bigr) = -E_{\mathbf q}v^r(q)e^{iq\cdot x}$ (the spatial momentum of $e^{iq\cdot x}$ is $-\mathbf q$, and $H_{\text{s.p.}}(-\mathbf q)v^r(q) = -E_{\mathbf q}v^r(q)$). So
>
> $$
> H_{\text{s.p.}}\psi = \int\frac{d^3q}{(2\pi)^3}\frac{E_{\mathbf q}}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(a^r_{\mathbf q}u^r(q)e^{-iq\cdot x} - b^{r\dagger}_{\mathbf q}v^r(q)e^{iq\cdot x}\Bigr) .
> $$
>
> **2. Multiply by $\psi^\dagger$, all four terms.** With $\psi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x} + b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x}\bigr)$ (variable $\mathbf p$, label $s$), keeping each operator product in its order:
>
> $$
> \psi^\dagger H_{\text{s.p.}}\psi = \int\frac{d^3p\,d^3q}{(2\pi)^6}\frac{E_{\mathbf q}}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\sum_{s,r}\Bigl[u^{s\dagger}(p)u^r(q)\,a^{s\dagger}_{\mathbf p}a^r_{\mathbf q}e^{i(p-q)\cdot x} - u^{s\dagger}(p)v^r(q)\,a^{s\dagger}_{\mathbf p}b^{r\dagger}_{\mathbf q}e^{i(p+q)\cdot x} + v^{s\dagger}(p)u^r(q)\,b^s_{\mathbf p}a^r_{\mathbf q}e^{-i(p+q)\cdot x} - v^{s\dagger}(p)v^r(q)\,b^s_{\mathbf p}b^{r\dagger}_{\mathbf q}e^{-i(p-q)\cdot x}\Bigr] .
> $$
>
> **3. The $d^3x$ integral.** As in Steps 2–3 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-3|Derivation §C5b.2.3]] (split exponentials, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]; plane-wave delta in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]): the $p - q$ terms give $(2\pi)^3\delta^3(\mathbf p - \mathbf q)e^{\pm i(E_{\mathbf p} - E_{\mathbf q})t}$, the $p + q$ terms $(2\pi)^3\delta^3(\mathbf p + \mathbf q)e^{\pm i(E_{\mathbf p} + E_{\mathbf q})t}$.
>
> **4. Integrate over $\mathbf q$.** In the first and fourth terms $\mathbf q = \mathbf p$, phase $1$, prefactor $E_{\mathbf p}/2E_{\mathbf p} = \frac12$; in the second and third $\mathbf q = -\mathbf p$, $q = \tilde p$, phases $e^{\pm2iE_{\mathbf p}t}$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1):
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,\frac12\sum_{s,r}\Bigl[u^{s\dagger}(p)u^r(p)\,a^{s\dagger}_{\mathbf p}a^r_{\mathbf p} - v^{s\dagger}(p)v^r(p)\,b^s_{\mathbf p}b^{r\dagger}_{\mathbf p} - u^{s\dagger}(p)v^r(\tilde p)\,a^{s\dagger}_{\mathbf p}b^{r\dagger}_{-\mathbf p}e^{2iE_{\mathbf p}t} + v^{s\dagger}(p)u^r(\tilde p)\,b^s_{\mathbf p}a^r_{-\mathbf p}e^{-2iE_{\mathbf p}t}\Bigr] .
> $$
>
> **5. Number-changing terms vanish.** $u^{s\dagger}(p)v^r(\tilde p) = v^{s\dagger}(p)u^r(\tilde p) = 0$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]). Dropped: both time-dependent terms, by spinor orthogonality alone. (For the scalar fields the same terms died by the mass shell, by a mixed commutator, or by cancellation: [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-6|Derivation §C2a.5.6]], What the derivation shows.)
>
> **6. Normalizations.** $u^{s\dagger}(p)u^r(p) = v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]]); with the $\frac12$ this gives $E_{\mathbf p}\bigl(a^{s\dagger}a^s - b^sb^{s\dagger}\bigr)$, summed over $s$. No time dependence is left.
>
> ⚑ By-product: the $b$ term carries a minus sign and the order $bb^\dagger$; for c-number amplitudes the classical energy is indefinite → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]]; for operators, which way it goes depends on the algebra → [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]].
>
> **What the derivation shows**
> - $H$ is diagonal in the modes before any quantization rule is chosen; only the reordering of $bb^\dagger$ remains to be done.
> - Assumptions used: the operator form of $H$ (on solutions), smearing for the exchange of integrals.

^der-c5b-3-2

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!derivation]- Derivation (second route, Lecture 10: at t = 0 with flipped momenta)
> **1. Evaluate at $t = 0$.** $H$ does not depend on time (first derivation), so evaluate it at $t = 0$ with the relabelled expansions of Step 1 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-4b|Derivation §C5b.2.4, second route]]: $\psi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(a^s_{\mathbf p}u^s(p) + b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\bigr)$, and $\psi^\dagger$ with its own variables $\mathbf p'$, $r$.
>
> **2. $H_{\text{s.p.}}$ on the coefficients.** On $e^{i\mathbf p\cdot\mathbf x}$, $H_{\text{s.p.}}$ acts as $H_{\text{s.p.}}(\mathbf p)$, and $H_{\text{s.p.}}(\mathbf p)u^s(p) = E_{\mathbf p}u^s(p)$, $H_{\text{s.p.}}(\mathbf p)v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]]); it acts on the c-number spinors only:
>
> $$
> H_{\text{s.p.}}\psi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\sum_s\Bigl(E_{\mathbf p}\,a^s_{\mathbf p}u^s(p) - E_{\mathbf p}\,b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\Bigr) .
> $$
>
> **3. Multiply by $\psi^\dagger$ and do the $d^3x$ integral.** $\int d^3x\,e^{-i\mathbf p'\cdot\mathbf x}e^{i\mathbf p\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]) sets the momentum in $\psi^\dagger$ equal to that in $\psi$, cancels one $(2\pi)^3$ and one integral, and turns $1/\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf p'}}$ into $1/2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1):
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\sum_{r,s}\Bigl(a^{r\dagger}_{\mathbf p}u^{r\dagger}(p) + b^r_{-\mathbf p}v^{r\dagger}(\tilde p)\Bigr)\Bigl(E_{\mathbf p}\,a^s_{\mathbf p}u^s(p) - E_{\mathbf p}\,b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\Bigr)
> $$
>
> (slide 18).
>
> **4. Expand into all four terms**, operators in the order they stand:
>
> $$
> \frac{E_{\mathbf p}}{2E_{\mathbf p}}\Bigl[u^{r\dagger}(p)u^s(p)\,a^{r\dagger}_{\mathbf p}a^s_{\mathbf p} - u^{r\dagger}(p)v^s(\tilde p)\,a^{r\dagger}_{\mathbf p}b^{s\dagger}_{-\mathbf p} + v^{r\dagger}(\tilde p)u^s(p)\,b^r_{-\mathbf p}a^s_{\mathbf p} - v^{r\dagger}(\tilde p)v^s(\tilde p)\,b^r_{-\mathbf p}b^{s\dagger}_{-\mathbf p}\Bigr] .
> $$
>
> **5. Orthogonality with flipped momentum.** $u^{r\dagger}(p)u^s(p) = v^{r\dagger}(\tilde p)v^s(\tilde p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]], with $E_{-\mathbf p} = E_{\mathbf p}$) and $u^{r\dagger}(p)v^s(\tilde p) = v^{r\dagger}(\tilde p)u^s(p) = 0$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]). Dropped: the two cross terms, by orthogonality. The $2E_{\mathbf p}$ cancels the $1/2E_{\mathbf p}$ and $\delta^{rs}$ removes one spin sum:
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\sum_s\Bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^s_{-\mathbf p}b^{s\dagger}_{-\mathbf p}\Bigr) .
> $$
>
> **6. Relabel.** In the $b$ term substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian $1$, $E_{\mathbf p}$ unchanged): the statement. (Slide 19 relabels after reordering; the order of the two steps does not matter, since the integral runs over all momenta and nothing says that antiparticles have momentum $-\mathbf p$.)
>
> **What the derivation shows**
> - The products are $u^\dagger u$, not $\bar uu$, because $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi$ carries $\psi^\dagger$; the $\gamma^0$ of $\bar\psi$ was used up turning $i\gamma^0\partial_0$ into $i\partial_0$ (asked in the lecture).
> - This is where the orthogonality of $u(p)$ and $v(\tilde p)$ with flipped momentum is needed: the $d^3x$ integral pairs $\mathbf p$ with $-\mathbf p$, as for the scalar ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]).
> - The "negative energy" term has its oscillators in the "wrong" order (slide 19); reordering is [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]].
>
> *Source: Lecture 10, slides 18–19 and transcript · the user's PHY 513 notes, Ch. 10 §10.5 (Derivation "The Hamiltonian in oscillator form") and Ch. 9 (Derivation "Orthogonality of u and v", the version with flipped momentum)*

^der-c5b-3-2b

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-4b|Derivation §C5b.2.4, second route]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

The second checkpoint: with commutators the minus sign of Theorem §C5b.3.2 cannot be removed.

> [!theorem] Theorem §C5b.3.3: Commutators Allow No Positive Norm with Positive Energy
> Quantize with the commutators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]]; $H$ is that of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]].
> 1. If a normalized $|0\rangle$ is annihilated by every $a^s_{\mathbf p}$ and $b^s_{\mathbf p}$, then $\|b^{s\dagger}(g)|0\rangle\|^2 = -\int\frac{d^3p}{(2\pi)^3}|g|^2 < 0$ for every $g \ne 0$ in $\mathcal S$: the antiparticle states have negative norm, although $[H, b^{s\dagger}_{\mathbf p}] = +E_{\mathbf p}b^{s\dagger}_{\mathbf p}$ still raises the energy.
> 2. If instead $d^s_{\mathbf p} \equiv b^{s\dagger}_{\mathbf p}$ annihilates $|0\rangle$, then $[d, d^\dagger] = +(2\pi)^3\delta^{rs}\delta^3$, norms are positive, and $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(a^{s\dagger}a^s - d^{s\dagger}d^s\bigr)$: the normalized $n$-quantum states $(n!)^{-1/2}d^{s\dagger}(g)^n|0\rangle$, $\int\frac{d^3p}{(2\pi)^3}|g|^2 = 1$, have energy expectation $-n\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}|g|^2$, unbounded below.
>
> Either way there is no Hilbert space with positive norm on which $H$ is bounded below: the Dirac field cannot be quantized with commutators.
>
> *Source: Lecture 10, slide 6 ("Hamiltonian not positive definite") and transcript · the user's PHY 513 notes, Ch. 10 §10.1 (Caution "The provisional quantization …") and after eq. (diracH) · PS §3.5, p. 54 (after eq. (3.90)) · Yu §5.5.1, after eq. (5.237), and Exercise 5.10 as worked in the user's pre-course notes, §5.5 · the user's pre-course notes, §5.5 ("The disease is sharper than a naive reading suggests")*

^thm-c5b-3-3

> [!derivation]- Derivation
> **1. Smeared operators.** $b^s(g) = \int\frac{d^3p}{(2\pi)^3}\overline{g(\mathbf p)}b^s_{\mathbf p}$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]); by Step 6 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-5|Derivation §C5b.2.5]], $[b^s(g), b^{s\dagger}(g)] = -\int\frac{d^3p}{(2\pi)^3}|g|^2$.
>
> **2. Part 1, the norm.** Since $b^s(g)|0\rangle = 0$, $\|b^{s\dagger}(g)|0\rangle\|^2 = \langle0|b^s(g)b^{s\dagger}(g)|0\rangle = \langle0|[b^s(g), b^{s\dagger}(g)]|0\rangle + \langle0|b^{s\dagger}(g)b^s(g)|0\rangle = -\int\frac{d^3p}{(2\pi)^3}|g|^2 + 0$. A vector of negative squared norm does not exist in a Hilbert space. (Unsmeared, $\langle\mathbf p^-|\mathbf p^-\rangle = -2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0)$, the user's pre-course notes; the smeared form avoids the valueless $\delta^3(\mathbf 0)$, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].)
>
> **3. Part 1, the spectrum.** $[-E_{\mathbf q}b^r_{\mathbf q}b^{r\dagger}_{\mathbf q}, b^{s\dagger}_{\mathbf p}] = -E_{\mathbf q}[b^r_{\mathbf q}, b^{s\dagger}_{\mathbf p}]b^{r\dagger}_{\mathbf q}$ (the other term has $[b^{r\dagger}, b^{s\dagger}] = 0$) $= +E_{\mathbf q}(2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)b^{r\dagger}_{\mathbf q}$; integrating, $[H, b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}b^{s\dagger}_{\mathbf p}$. The $a$ part commutes with $b^\dagger$. So $b^\dagger$ raises the eigenvalue: the failure is in the metric, not in the spectrum (the user's pre-course notes). The diagonal matrix element $\langle0|b^s(g)\,H\,b^{s\dagger}(g)|0\rangle$ is then the (positive) energy times the negative squared norm of Step 2, hence negative: the negative energy expectation values recorded in the user's pre-course notes come from the indefinite metric.
>
> **4. Part 2, relabel.** With $d \equiv b^\dagger$, $d^\dagger = b$: $[d^r_{\mathbf p}, d^{s\dagger}_{\mathbf q}] = [b^{r\dagger}_{\mathbf p}, b^s_{\mathbf q}] = -[b^s_{\mathbf q}, b^{r\dagger}_{\mathbf p}] = +(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$: a bosonic oscillator algebra with positive norms, as for the scalar ([[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]]). In $H$, $-b^sb^{s\dagger} = -d^{s\dagger}d^s$ with no reordering, hence no constant.
>
> **5. Part 2, the energy.** As for the scalar, $[-\int E\,d^\dagger d, d^{s\dagger}(g)] = -d^{s\dagger}(E_{\mathbf p}g)$, so $d^{s\dagger}(g)$ lowers the energy by the packet's mean energy; $n$ quanta may occupy one packet because the $d^\dagger$ commute ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]), and pushing $H$ through the $n$ creation operators one at a time (as in [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-2|Derivation §C2a.4.2]], step 4) gives $\langle H\rangle = -n\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}|g|^2$, with norm $1$ for the stated normalization. As $n \to \infty$ the energy goes to $-\infty$ (PS: "by creating more and more particles with $b^\dagger$, we can lower the energy indefinitely").
>
> **6. No third option.** The canonical relations fix $[b, b^\dagger] < 0$ (Theorem §C5b.2.5); a vacuum must be annihilated by one of $b$, $b^\dagger$ in each mode for a Fock space to be built; Steps 2 and 5 exhaust the two choices.
>
> **What the derivation shows**
> - The two textbook diagnoses are the two horns of one dilemma: Yu keeps $b$ as annihilator and finds negative norms; Peskin–Schroeder keep positive norms and find energy unbounded below.
> - Assumptions used: a Fock vacuum, and $H$ as computed before any reordering.
> - Used next: the cure ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]); the causality version of the same failure is [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]].

^der-c5b-3-3

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]

> [!definition] Definition §C5b.3.1: Normal Ordering of Fermion Operators
> The **normal-ordered** product $:\!X\!:$ of creation and annihilation operators places all creation operators to the left of all annihilation operators, with a factor $-1$ for every exchange of two fermion operators made in the rearrangement; bosonic operators are moved without sign as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]. For example $:\!b^r_{\mathbf p}b^{s\dagger}_{\mathbf q}\!: = -b^{s\dagger}_{\mathbf q}b^r_{\mathbf p}$ and $:\!\psi^\dagger_a\psi_b\!:$ is extended linearly through the mode expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]. Then $\langle0|{:}X{:}|0\rangle = 0$ for the vacuum of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]].
>
> *Source: the user's PHY 513 notes, Ch. 10 §10.5 ("Normal ordering of fermion operators puts annihilators to the right *with* the sign of the reordering") · Lecture 10 (transcript: "so that is the normal ordering part") · PS §3.5, after eq. (3.104) ("the infinite constant term that comes from anticommuting $b$ and $b^\dagger$"), §4.7 (sign rule, cited) · Yu §6.3 (fermionic normal products, cited)*

^def-c5b-3-1

> [!theorem] Theorem §C5b.3.4: The Hamiltonian of the Dirac Field
> With the anticommutators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], the $H$ of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]] is
>
> $$
> H = \sum_s\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} + b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}\bigr) + E_0^{(\rm D)}, \qquad :\!H\!: = \sum_s\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} + b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}\bigr) \ge 0 ,
> $$
>
> with the normal ordering of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]] and the constant $E_0^{(\rm D)}$ of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]. Both species contribute positive energy $E_{\mathbf p}$ per quantum; $:\!H\!:|0\rangle = 0$.
>
> *Scalar analogue:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] with [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]].
> *Source: Lecture 10, slides 19 and 23 · the user's PHY 513 notes, Ch. 10 §10.5, eq. (diracH), and §10.7 · PS §3.5, eq. (3.104) · Yu §5.5.2, eq. (5.247) · the user's pre-course notes, §5.5, eq. (dirac-H)*

^thm-c5b-3-4

> [!derivation]- Derivation
> **1. Start from the unreordered form.** $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^s_{\mathbf p}b^{s\dagger}_{\mathbf p})$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]]), valid for any algebra.
>
> **2. Reorder with the anticommutator.** $b^s_{\mathbf p}b^{s\dagger}_{\mathbf p} = -b^{s\dagger}_{\mathbf p}b^s_{\mathbf p} + \{b^s_{\mathbf p}, b^{s\dagger}_{\mathbf p}\} = -b^{s\dagger}_{\mathbf p}b^s_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]] at coincident labels). Hence $-b^sb^{s\dagger} = +b^{s\dagger}b^s - (2\pi)^3\delta^3(\mathbf 0)$: the minus sign of Theorem §C5b.3.2 is turned into a plus by the anticommutator ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|Remark: Two minus signs make a plus]]). (Slide 19 passes from $-b_{-\mathbf p}b^\dagger_{-\mathbf p}$ to $+b^\dagger_{\mathbf p}b_{\mathbf p}$ without the constant; in the lecture it was raised by a question, "that should output a delta of zero", and removed by normal ordering, Step 4.)
>
> **3. Collect.** $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(a^{s\dagger}a^s + b^{s\dagger}b^s) - \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0)$. ⚑ By-product: the constant is negative → [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]. *Sense:* $\delta^3(\mathbf 0)$ has no value; the constant is defined in the box of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
>
> **4. Normal order.** By [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], $:\!a^\dagger a\!: = a^\dagger a$ and $:\!-bb^\dagger\!: = +b^\dagger b$, so $:\!H\!:$ is the operator part; every term ends in an annihilator, so $:\!H\!:|0\rangle = 0$, and $\langle\Psi|{:}H{:}|\Psi\rangle = \sum_s\int E_{\mathbf p}(\|a^s_{\mathbf p}\Psi\|^2 + \|b^s_{\mathbf p}\Psi\|^2) \ge 0$ (read with wave packets, as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).
>
> **What the derivation shows**
> - Positivity of the energy is produced by the reordering sign, and the ordering constant is where the sign of the algebra shows.
> - Assumptions used: the algebra of Theorem §C5b.2.4; the box for $\delta^3(\mathbf 0)$.

^der-c5b-3-4

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!remark] Remark: Two minus signs make a plus
> In [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]] the antiparticle term carries two signs: one from the wave function, the eigenvalue $-E_{\mathbf p}$ of $H_{\text{s.p.}}$ on $v^s(p)e^{ip\cdot x}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]]), and one from reordering anticommuting operators, $bb^\dagger = -b^\dagger b + \{b, b^\dagger\}$. Their product is $+E_{\mathbf p}$ (slide 19: "Fermion statistics cancels sign in 'negative energy'"). Had the oscillators been quantized with commutators, reordering would have given $-bb^\dagger = -b^\dagger b - (2\pi)^3\delta^3(\mathbf 0)$ and the antiparticle energies would have stayed negative (Yu, eq. (5.237); [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]). The negative-energy solutions are harmless because they enter as part of a complete basis of the quantum field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-1|§C5b.2, Remark: Reading the expansion]]), not as wave functions of particles ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|Caution: Negative energies are a problem only if ψ is a wave function]]): the field has a wave aspect and an operator aspect, and the wrong sign of the first is cancelled by the wrong order of the second.
>
> *Source: Lecture 10, slide 19 and transcript · the user's PHY 513 notes, Ch. 10 §10.5 (after eq. (diracH))*

^rem-c5b-3-1

## The zero-point energy

> [!theorem] Theorem §C5b.3.5: The Fermionic Zero-Point Energy Is Negative
> The ordering constant of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]] is
>
> $$
> E_0^{(\rm D)} = -2V\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p} = -4E_0, \qquad V = (2\pi)^3\delta^3(\mathbf 0) ,
> $$
>
> with $E_0$ the real scalar's zero-point energy of the same mass ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]): $-\frac12E_{\mathbf p}$ for each of the four modes per momentum (two spins, two species), where each bosonic mode gave $+\frac12E_{\mathbf p}$. In a box with cutoff, $E_0^{(\rm D)}(V, \Lambda) = -2\sum_{|\mathbf k|<\Lambda}E_{\mathbf k}$, energy density $\approx -\Lambda^4/4\pi^2$ for $\Lambda \gg m$.
>
> *Scalar analogue:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]].
> *Source: the user's PHY 513 notes, Ch. 10 §10.5 ("The constant": "$-\frac12E_{\mathbf p}$ for each of the four fermionic oscillators per momentum") · Lecture 10 (transcript) · the user's pre-course notes, §5.5 (Remark "The fermionic zero-point energy is negative") · Yu §5.5.2, eq. (5.247), §5.5.4, eq. (5.269) · PS §3.5, after eq. (3.104)*

^thm-c5b-3-5

> [!derivation]- Derivation
> **1. The constant.** From Step 3 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-4|Derivation §C5b.3.4]], $E_0^{(\rm D)} = -\sum_{s=1,2}\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0) = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}$, with the dictionary $(2\pi)^3\delta^3(\mathbf 0) \leftrightarrow V$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], 2. Since $E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, $E_0^{(\rm D)} = -4E_0$.
>
> **2. Mode by mode.** For each fermionic mode $c$ ($c = a^s_{\mathbf p}$ or $b^s_{\mathbf p}$; in the box $\{c, c^\dagger\} = 1$ per mode after rescaling by $V$), $c^\dagger c = \frac12[c^\dagger, c] + \frac12\{c, c^\dagger\} = \frac12[c^\dagger, c] + \frac12$. In the box $H = \sum_{\mathbf k,s}E_{\mathbf k}(a^\dagger a - bb^\dagger)$ becomes, with $-bb^\dagger = b^\dagger b - 1$, $\sum E_{\mathbf k}\bigl[(a^\dagger a - \tfrac12) + (b^\dagger b - \tfrac12)\bigr]$ plus $\sum E(\frac12 + \frac12 - 1) = 0$: each of the four modes per momentum is a fermionic oscillator $E(c^\dagger c - \frac12) = \frac E2[c^\dagger, c]$, with ground-state energy $-\frac E2$. The bosonic oscillator is $\omega(a^\dagger a + \frac12) = \frac\omega2\{a^\dagger, a\}$ ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|§C2a.1, Remark: The oscillator, recalled]]): the sign of the zero-point energy is the sign that turns $\{\cdot,\cdot\}$ into $[\cdot,\cdot]$.
>
> **3. Box with cutoff.** As in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-2|Derivation §C2a.3.2]]: two spins times $-\sum_{|\mathbf k|<\Lambda}E_{\mathbf k}$; per volume $-2\int_{|\mathbf p|<\Lambda}\frac{d^3p}{(2\pi)^3}E_{\mathbf p} \approx -2\cdot\frac{4\pi}{(2\pi)^3}\frac{\Lambda^4}{4} = -\frac{\Lambda^4}{4\pi^2}$ for $\Lambda \gg m$, four times the scalar's $\Lambda^4/16\pi^2$ with the opposite sign.
>
> **What the derivation shows**
> - A negative infinite constant, removed by normal ordering exactly as the scalar's; for energy differences it is harmless ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]]).
> - It is the energy of Dirac's filled sea → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].

^der-c5b-3-5

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|§C2a.1, Remark: The oscillator, recalled]]

> [!remark] Remark: Energies are measured from the vacuum
> After normal ordering, $H$ measures energy relative to the vacuum. What the theory has to get right is how much energy each particle carries: $a^\dagger$ and $b^\dagger$ each add $E_{\mathbf p}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]). The energy assigned to the zero-particle state is a different question, which nothing but gravity would detect (Lecture 10: "it's never going to matter until quantum gravity"). The same choice was made for the scalar ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]]); for the Dirac field the dropped constant is negative ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]).
>
> *Source: Lecture 10 (transcript, answer to "that should output a delta of zero — do we just ignore that?") · the user's PHY 513 notes, Ch. 10 §10.5 ("The constant")*

^rem-c5b-3-2

> [!remark]- ★ Remark: Bose and Fermi zero-point energies have opposite signs
> Each bosonic mode contributes $+\frac12E$ and each fermionic mode $-\frac12E$. A theory with equal numbers of bosonic and fermionic modes of equal masses has cancelling zero-point energies; supersymmetric theories are built this way (stated in the user's pre-course notes, outside the course).
>
> *Source: the user's pre-course notes, §5.5 (Remark "The fermionic zero-point energy is negative")*

^rem-c5b-3-3

> [!remark] Remark: Empty and filled are labels
> Take one pair $b$, $b^\dagger$ with $\{b, b^\dagger\} = 1$, $b^2 = 0$. If $b|0\rangle = 0$, then $|1\rangle = b^\dagger|0\rangle$, $b|1\rangle = |0\rangle$, $b^\dagger|1\rangle = 0$: a two-state space ([[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]], 3). One could equally call $|1\rangle$ empty and $\tilde b = b^\dagger$ its annihilator: $\{\tilde b, \tilde b^\dagger\} = 1$ again, because the anticommutator is symmetric. The two descriptions are the same until an observable, here the energy, says which state is lower; the lower one is called empty, and the dagger goes on the operator that creates positive energy. With commutators the relabelling changes the sign of the algebra ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], 2), which is why the trick is available only for fermions; and $(\tilde b^\dagger)^2 = 0$ means a mode cannot be filled twice.
>
> *Source: PS §3.5, pp. 57 (the single pair $b$, $b^\dagger$; eq. (3.98))*

^rem-c5b-3-4

## Momentum and the ladder relations

> [!theorem] Theorem §C5b.3.6: Momentum of the Dirac Field
> The field momentum $\mathbf P = -\int d^3x\,\pi\nabla\psi = \int d^3x\,\psi^\dagger(-i\nabla)\psi$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]]; general form [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-6|Theorem §C1.12.6]]) is, under the anticommutators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]],
>
> $$
> \mathbf P = \sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} + b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}\bigr) ,
> $$
>
> with no constant and no ordering choice: fermions and antifermions of label $\mathbf p$ both carry momentum $\mathbf p$.
>
> *Scalar analogue:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]].
> *Source: PS §3.5, eq. (3.105) · Yu §5.5.2, eqs. (5.257)–(5.258) · not computed in Lecture 10 (slide 20 states that the one-particle states carry momentum $\mathbf p$)*

^thm-c5b-3-6

> [!derivation]- Derivation
> **1. $-i\nabla$ on the modes.** $-i\nabla e^{-iq\cdot x} = -i(i\mathbf q)e^{-iq\cdot x} = \mathbf q\,e^{-iq\cdot x}$ and $-i\nabla e^{iq\cdot x} = -\mathbf q\,e^{iq\cdot x}$, since $\pm q\cdot x$ contains $\mp\mathbf q\cdot\mathbf x$. So $(-i\nabla)\psi$ is Step 1 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2|Derivation §C5b.3.2]] with $E_{\mathbf q}$ replaced by $\mathbf q$ (and the same relative minus sign).
>
> **2. Steps 2–5 of Derivation §C5b.3.2 unchanged.** The cross terms vanish by [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]; in the diagonal terms $\mathbf q = \mathbf p$ and the prefactor is $\mathbf p/2E_{\mathbf p}$, times $2E_{\mathbf p}\delta^{rs}$:
>
> $$
> \mathbf P = \sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^s_{\mathbf p}b^{s\dagger}_{\mathbf p}\bigr) .
> $$
>
> **3. Reorder.** As in [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-4|Derivation §C5b.3.4]], Step 2: $-b^sb^{s\dagger} = b^{s\dagger}b^s - (2\pi)^3\delta^3(\mathbf 0)$. The constant is $-2V\int\frac{d^3p}{(2\pi)^3}\mathbf p$, an odd integrand: zero for any rotation-invariant cutoff (in the box, $\mathbf k$ and $-\mathbf k$ pair off), as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-4|Derivation §C2a.3.4]], step 7.
>
> **What the derivation shows**
> - The relabelling $\mathbf p \to -\mathbf p$ in [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-1|Derivation §C5b.2.1]], Step 5, is why the antifermion of label $\mathbf p$ has momentum $+\mathbf p$.

^der-c5b-3-6

*Uses:* [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2|Derivation §C5b.3.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!theorem] Theorem §C5b.3.7: Ladder Relations
> For any operators, $[AB, C] = A\{B, C\} - \{A, C\}B$. With [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]] and $H$, $\mathbf P$ of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]] (normal ordered),
>
> $$
> [H, a^{s\dagger}_{\mathbf p}] = E_{\mathbf p}a^{s\dagger}_{\mathbf p}, \quad [H, b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}b^{s\dagger}_{\mathbf p}, \quad [\mathbf P, a^{s\dagger}_{\mathbf p}] = \mathbf p\,a^{s\dagger}_{\mathbf p}, \quad [\mathbf P, b^{s\dagger}_{\mathbf p}] = \mathbf p\,b^{s\dagger}_{\mathbf p} ,
> $$
>
> and the adjoint relations for $a$, $b$ with the opposite signs: Hamiltonian and momentum are bilinear, so commutators with them are ordinary commutators although the fields anticommute. Exactly as for bosons, $a^\dagger$ and $b^\dagger$ add energy $E_{\mathbf p}$ and $a$, $b$ remove it. The charge: [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]].
>
> *Scalar analogue:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]].
> *Source: the user's PHY 513 notes, Ch. 10 §10.6 (Derivation "The oscillators raise and lower the energy") · Yu §5.5.2, eqs. (5.248)–(5.251) · the user's pre-course notes, §5.5 ("the mixed identity converts the anticommutators into the needed commutators")*

^thm-c5b-3-7

> [!derivation]- Derivation
> **1. The identity.** $A\{B, C\} - \{A, C\}B = ABC + ACB - ACB - CAB = ABC - CAB = [AB, C]$.
>
> **2. $H$ and $a^\dagger$.** With $A = a^{r\dagger}_{\mathbf q}$, $B = a^r_{\mathbf q}$, $C = a^{s\dagger}_{\mathbf p}$: $[a^{r\dagger}_{\mathbf q}a^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}] = a^{r\dagger}_{\mathbf q}\{a^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}\} - \{a^{r\dagger}_{\mathbf q}, a^{s\dagger}_{\mathbf p}\}a^r_{\mathbf q} = a^{r\dagger}_{\mathbf q}(2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p) - 0$. The $b^\dagger b$ terms give $b^{r\dagger}_{\mathbf q}\{b^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}\} - \{b^{r\dagger}_{\mathbf q}, a^{s\dagger}_{\mathbf p}\}b^r_{\mathbf q} = 0$. Multiplying by $E_{\mathbf q}$ and integrating $\int\frac{d^3q}{(2\pi)^3}\sum_r$: $E_{\mathbf p}a^{s\dagger}_{\mathbf p}$.
>
> **3. $H$ and $b^\dagger$.** The same with the species exchanged: $E_{\mathbf p}b^{s\dagger}_{\mathbf p}$; the sign is $+$ because $:\!H\!:$ contains $+b^\dagger b$.
>
> **4. $H$ and the annihilators.** $[a^{r\dagger}_{\mathbf q}a^r_{\mathbf q}, a^s_{\mathbf p}] = a^{r\dagger}_{\mathbf q}\{a^r_{\mathbf q}, a^s_{\mathbf p}\} - \{a^{r\dagger}_{\mathbf q}, a^s_{\mathbf p}\}a^r_{\mathbf q} = -(2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)a^r_{\mathbf q}$, so $[H, a^s_{\mathbf p}] = -E_{\mathbf p}a^s_{\mathbf p}$; likewise for $b$ (Yu (5.249), (5.251)).
>
> **5. $\mathbf P$.** Replace the weight $E_{\mathbf q}$ by $\mathbf q$. Constants commute with everything, so the unordered forms give the same relations.
>
> **What the derivation shows**
> - $a^\dagger$ and $b^\dagger$ both raise the energy by $E_{\mathbf p}$ and the momentum by $\mathbf p$: the commutator of a bilinear with a single fermion operator is computed with anticommutators, and the signs work out to the bosonic ones.
> - The same identity with weights $\pm1$ gives the charges of the quanta ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]).

^der-c5b-3-7

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark]- Connections
> - The free Dirac Hamiltonian is the second-quantized form of the single-particle Hamiltonian, $H = \int\psi^\dagger H_{\text{s.p.}}\psi$, exactly the one-body operator of nonrelativistic second quantization; what is new is that half of the modes of $H_{\text{s.p.}}$ are written with creation operators in front — [[§C12.2★ Second Quantization#^thm-c12-2-4|QM Theorem §C12.2.4]], [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].
> - The sign of the zero-point energy, $+\frac12\omega$ for $\{a^\dagger, a\}/2$ and $-\frac12\omega$ for $[c^\dagger, c]/2$, is the oscillator form of the boson–fermion difference; both are the same singular coincident product, δ³(0) in modes or a two-point function at zero separation — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|§C2b.6, Remark: The zero-point energy is the Wightman function at coincident points]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]].
> - The Hamiltonian in modes needs the orthogonality of $u(p)$ and $v(\tilde p)$ at flipped momentum for the same reason the scalar Hamiltonian needed $E_{-\mathbf p} = E_{\mathbf p}$: the $d^3x$ integral pairs $\mathbf p$ with $-\mathbf p$ in the number-changing terms — [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]].
> - The ladder relations generate the time dependence of the mode operators, which makes the expansion of §C5b.2 the Heisenberg field — [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]].
> - Momentum and energy together form the four-momentum $P^\mu$ of the Noether procedure applied to the Dirac Lagrangian — [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]], [[P3 Noether's Procedure|P3]].
