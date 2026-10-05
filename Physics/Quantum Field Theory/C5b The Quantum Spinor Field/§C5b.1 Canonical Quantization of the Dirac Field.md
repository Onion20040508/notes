---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.7 Gamma-Matrix Technology]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.2 Mode Expansion and the Anticommutator Algebra]] →

*Sources: the user's PHY 513 notes, Ch. 10 §§10.1–10.2 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part A, slides and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 52–58 · Yu Zhao-Huan, 量子场论讲义, §5.4.3, §§5.5.1–5.5.2, §5.5.4 · the user's pre-course notes, §5.5.*

This is the spinor counterpart of [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]: how is the free Dirac field turned into a quantum theory? The classical ingredients are in place: the Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]), the canonical momentum $\pi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]) and the Hamiltonian density ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]). Lecture 10 starts from a puzzle in that momentum: the field is its own conjugate, so the commutators of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]] would make two coordinates fail to commute. This section states the postulate that replaces them, the equal-time anticommutators, and the spin–statistics theorem that says why; the computations that justify the choice run through [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]–[[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]] and [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]], following [[P1 Canonical Quantization]]. Quantum Mechanics met the anticommutators as an algebra chosen per species ([[§C12.2★ Second Quantization|QM §C12.2★]]) and the negative energies as a filled sea ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]); what the field adds is said where each appears.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, chiral basis for the Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), $\bar\psi = \psi^\dagger\gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]), $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ with $p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ whenever $p$ labels a mode, $m > 0$; $\tilde p \equiv (E_{\mathbf p}, -\mathbf p)$ as in [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]; spatial transforms as in [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], with $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$ an identity in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). Spin labels $r, s \in \{1, 2\}$ refer to the spin basis $\xi^s$, $\eta^s$ of [[§C5a.5 Plane-Wave Solutions#^def-c5a-5-3|Def. §C5a.5.3]]. These conventions hold in all of C5b.

> [!caution] Caution: Names for the Dirac field and its mode operators across sources
> Lecture 10 and the user's PHY 513 notes (Ch. 10) put hats on operators, $\hat\psi$, $\hat a^s_{\mathbf p}$, $\hat b^s_{\mathbf p}$, and write $\Pi_\psi$ for the momentum density. These notes drop the hats and write $\pi$, as for the scalar ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|§C2a.1, Caution: Eₚ, not ωₚ; π, not Π]]), and keep Larsen's letters and names otherwise:
>
> | object | Lecture 10, user's Ch. 10 | these notes | PS §3.5 (from eq. (3.99)) | Yu §5.4–§5.5, pre-course notes |
> | --- | --- | --- | --- | --- |
> | fermion annihilator | $\hat a^s_{\mathbf p}$ | $a^s_{\mathbf p}$ | $a^s_{\mathbf p}$ | $a_{\mathbf p,\lambda}$ |
> | antifermion annihilator | $\hat b^s_{\mathbf p}$ | $b^s_{\mathbf p}$ | $b^s_{\mathbf p}$ | $b_{\mathbf p,\lambda}$ |
> | spin label of $u$, $v$ | $s = 1, 2$ | $s = 1, 2$ | $s = 1, 2$ | helicity $\lambda = \pm$ |
> | one-particle states | $\vert\mathbf p, s\rangle$, $\vert\mathbf p, s\rangle^c$ | $\vert\mathbf p, s\rangle$, $\vert\mathbf p, s\rangle^c$ | $\vert\mathbf p, s\rangle$; antifermion unnamed | $\vert\mathbf p^+, \lambda\rangle$, $\vert\mathbf p^-, \lambda\rangle$ |
> | momentum density | $\Pi_\psi = i\psi^\dagger$ | $\pi = i\psi^\dagger$ | $i\psi^\dagger$ | $\pi = i\psi^\dagger$ |
> | kernel of $\mathcal H$ | $H_{\text{s.p.}}$ | $H_{\text{s.p.}}$ ($h_D$ in §C5a.3) | unnamed, eq. (3.85) | — |
>
> The superscript $c$ on the antifermion state is for "conjugate". Peskin–Schroeder's pp. 52–57 use a provisional labelling ($b^s_{-\mathbf p}v^s(-\mathbf p)$ in eq. (3.87), then $\tilde b = b^\dagger$ in eq. (3.98)) that they ask the reader to forget from eq. (3.99) on; only the final one is used here. Other texts write $b$, $d$ (Sakurai, Srednicki) or $b$, $c$.
>
> *Source: Lecture 10, slides 5, 10–12, 16, 20 · the user's PHY 513 notes, Ch. 10 §§10.3, 10.6 and Concordance ("Notation within these notes") · PS §3.5, eqs. (3.87), (3.98)–(3.99), (3.106) · Yu §5.4.3, §5.5.4*

^cau-c5b-1-1

> [!remark] Remark: Lecture 10's route, and how to read Peskin–Schroeder §3.5
> The lecture's logical order is: a puzzle in the canonical momentum → spin and statistics → the mode expansion → anticommutators of fields ⇔ anticommutators of oscillators → the Hamiltonian → particles, antiparticles and the exclusion principle. It copies the scalar construction ([[§C2a.1 Canonical Quantization of Fields|§C2a.1]]–[[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]]) step by step, and the interest is in the two places where the copy must change: the canonical relations become anticommutators, and the negative-frequency solutions turn into positive-energy antiparticles. The lecture did the computation with anticommutators from the start and pointed out where the commutator version would have failed; those checkpoints are [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]] (the antiparticle algebra gets the wrong sign), [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]] (no positive norm with energy bounded below) and [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]] (propagation outside the light cone). Peskin–Schroeder §3.5 does the opposite: pp. 52–56 work through the commutator version, find the problems, and only then switch. The wrong version and the right one stand back to back with nothing marking the wrong pages, so the section has to be read linearly (Lecture 10: "unless you read it linearly, you might get it wrong"). The chapter follows the scalar chapters' order instead: canonical quantization (this section), modes ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]), energy ([[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]]), particles ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]), charge ([[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]]), the spacetime picture ([[§C5b.6 The Heisenberg Dirac Field|§C5b.6]]–[[§C5b.8 Green's Functions and the Dirac Feynman Propagator|§C5b.8]]) and spin and statistics ([[§C5b.9 Spin and Statistics|§C5b.9]]).
>
> *Source: the user's PHY 513 notes, Ch. 10 (introduction) · Lecture 10, slide 6 ("PS tries both: first commutation, then anti-commutation") · Lecture 10 (transcript)*

^rem-c5b-1-1

## The canonical system

> [!definition] Definition §C5b.1.1: Single-Particle Hamiltonian
> The **single-particle Hamiltonian** of the Dirac equation is the $4\times4$ matrix differential operator
>
> $$
> H_{\text{s.p.}} \equiv \gamma^0\bigl(-i\boldsymbol\gamma\cdot\nabla + m\bigr) = -i\boldsymbol\alpha\cdot\nabla + \beta m, \qquad \boldsymbol\gamma\cdot\nabla \equiv \gamma^j\partial_j, \quad \boldsymbol\alpha = \gamma^0\boldsymbol\gamma, \ \beta = \gamma^0 ,
> $$
>
> the kernel of the Hamiltonian density, $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]], where it is written $h_D$). It is Hermitian ($\boldsymbol\alpha$, $\beta$ Hermitian, same theorem), and on $e^{i\mathbf p\cdot\mathbf x}$ it acts as the matrix $h(\mathbf p) = \gamma^0(\gamma^jp^j + m)$. It is the Hamiltonian that relativistic quantum mechanics takes for a four-component wave function ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]).
>
> *Source: Lecture 10, slide 16 · the user's PHY 513 notes, Ch. 10 §10.5 (Definition "The single-particle Hamiltonian"; there $\gamma^0\gamma^i$ is called anti-Hermitian: it is Hermitian, $(\gamma^0\gamma^i)^\dagger = \gamma^{i\dagger}\gamma^0 = -\gamma^i\gamma^0 = \gamma^0\gamma^i$, Step 5 of [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-9|Derivation §C5a.3.9]], which is what makes $\gamma^0\gamma^i(-i\partial_i)$ Hermitian) · PS §3.5, eq. (3.85)*

^def-c5b-1-1

> [!model] Model §C5b.1.1: The Free Dirac Field as a Canonical System
> The free Dirac field of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, has the four canonical pairs $(\psi_a, \pi_a)$ with $\pi_a = i\psi_a^\dagger$ and no momentum conjugate to $\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]), and the Hamiltonian
>
> $$
> H = \int d^3x\;\psi^\dagger H_{\text{s.p.}}\psi ,
> $$
>
> with the single-particle Hamiltonian $H_{\text{s.p.}} = -i\boldsymbol\alpha\cdot\nabla + \beta m$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]], the integral of the density of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]; on solutions of the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) $H_{\text{s.p.}}\psi = i\partial_t\psi$.
>
> *Assumptions:* $m > 0$; the field and its derivatives fall off at spatial infinity (classically), or are read against wave packets (quantum). The quantization rule is not part of the model: it is decided below ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]).
> *Scalar analogue:* the free complex scalar, [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]].
> *Source: Lecture 10, slides 5 and 16 · the user's PHY 513 notes, Ch. 10 §10.1 and §10.5 · PS §3.5, eqs. (3.83)–(3.85) · Yu §5.4.3, eqs. (5.219), (5.222) · the user's pre-course notes, §5.5*

^mod-c5b-1-1

> [!remark] Remark: A first-order system: the momentum is ψ† itself
> The Lagrangian is linear in $\dot\psi$, so $\pi = i\psi^\dagger$ does not contain $\dot\psi$ and the Legendre map cannot be inverted; the velocities drop out of $\mathcal H$ by themselves ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]; [[§C1.10 Hamiltonian Field Theory#^rem-c1-10-3|§C1.10, Remark: Constraints and first-order Lagrangians]]). The phase space is therefore $(\psi_a, \psi^\dagger_a)$, four complex coordinates, half as many as four complex scalar fields would have: $\psi^\dagger$ is not a second canonical coordinate as $\phi^\dagger$ was for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]), but the momentum of $\psi$ (Yu, after eq. (5.220)). The complex scalar's crossover $\pi = \dot\phi^\dagger$ is here taken one step further: $\pi$ is $\psi^\dagger$ itself. Lecture 10 derived $\pi$ with the note "treat $\psi$ and $\psi^\dagger$ as independent fields": that is right for varying the action ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]), but the result shows that $\psi^\dagger$ is not an independent canonical coordinate; it *is* the momentum of $\psi$. Lorentz invariance together with a first-order equation forces $\pi \propto \psi^\dagger$ rather than $\pi \propto \dot\psi$, and this is the root of the puzzle below.
>
> *Source: Lecture 10, slide 5 · the user's PHY 513 notes, Ch. 10 §10.1 (Derivation "The momentum conjugate to ψ") · Yu §5.4.3, eqs. (5.219)–(5.220) · PS §3.5, p. 52*

^rem-c5b-1-2

> [!caution] Caution: The provisional commutator quantization, and why it is strange
> Copying the scalar field ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]]) one would impose at equal times $[\psi_a(\mathbf x), \pi_b(\mathbf y)] = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, which with $\pi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]) reads $[\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)] = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, the factors $i$ cancelling (Lecture 10: "Quantization (Provisional)"). This is strange. Canonical coordinates commute with each other, $[q_i, q_j] = 0$, yet here a field–field commutator is required to be a delta function, because the momentum is the field's own conjugate. The root is the linearity of $\mathcal L$ in $\dot\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|Remark: A first-order system: the momentum is ψ† itself]]). Carried through, the commutator version fails twice: the energy is unbounded below or norms are negative ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]), and propagation is not causal ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]). Both failures disappear with anticommutators ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]).
>
> *Source: Lecture 10, slides 5–6 · the user's PHY 513 notes, Ch. 10 §10.1 (Caution "The provisional quantization, and why it is strange") · PS §3.5, pp. 52–56 · Yu §5.5.1*

^cau-c5b-1-2

## The postulate, and the theorem behind it

> [!principle] Principle §C5b.1.2: Equal-Time Canonical Anticommutation Relations
> The Dirac field is quantized by promoting the canonical pairs $(\psi_a, \pi_a = i\psi^\dagger_a)$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]] to operators with, at equal times,
>
> $$
> \{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad \{\psi_a(\mathbf x), \psi_b(\mathbf y)\} = \{\psi^\dagger_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = 0 ,
> $$
>
> equivalently $\{\psi_a, \pi_b\} = i\delta_{ab}\delta^3$, and taking as Hamiltonian the $H$ of the model read as an operator. ($\{A, B\} \equiv AB + BA$.) This is **Jordan–Wigner** quantization, in place of the commutators of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]].
>
> *Domain:* fields of half-odd-integer spin (here the Dirac field), Schrödinger-picture operators or Heisenberg operators at a common time; integer-spin fields keep commutators. The relations are identities of operator-valued distributions ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|Theorem §C5b.1.4]]). The operator ordering in $H$ is not fixed by the principle ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]). The choice is forced by positivity ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]) and by causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]).
>
> *Scalar analogue:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]].
> *Source: Lecture 10, slides 6 and 23 · the user's PHY 513 notes, Ch. 10 §10.4 (Principle "The equal-time anticommutators") · PS §3.5, eqs. (3.96), (3.102) · Yu §5.5.2, eqs. (5.238)–(5.239) · the user's pre-course notes, §5.5, eq. (car)*

^pr-c5b-1-2

> [!principle] Principle §C5b.1.3: The Spin–Statistics Theorem
> *Ingredients:* fields in a representation of spin $s$; a local quantum field theory (a Lagrangian with finitely many derivatives, fields multiplied only at the same point); Lorentz invariance, positive energies and positive norms; causal propagation (the commutator or anticommutator of the fields vanishes outside the light cone).
> *Claim:* a physical field of integer spin (a representation $(j_+, j_-)$ of [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations|§C3.2]] with $j_+ + j_-$ an integer) must be quantized with commutation relations ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]]) and describes bosons; a physical field of half-odd-integer spin must be quantized with anticommutation relations ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]) and describes fermions ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]). Causality is microcausality of observables ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
>
> *Layer:* stated, not proved, in this course (Lecture 10: "The proof is complicated"); the free fields of the course are checked in [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]].
> *Source: Lecture 10, slide 7 · the user's PHY 513 notes, Ch. 10 §10.2 (Principle "The spin–statistics theorem") · Yu §5.5.4 (boxed statement, after eq. (5.293)) · PS §3.5, pp. 57–58 (Pauli 1940; Streater & Wightman, cited there) · the user's pre-course notes, §5.5, Theorem "Spin–statistics theorem"*

^pr-c5b-1-3

> [!derivation]+ Derivation (to be filled: every spin)
> *Status:* the proof for every spin (that integer-spin fields *cannot* be quantized with anticommutators, and the general half-integer case) rests on the Lorentz invariance of the two-point functions and causality at spacelike separation. It is not given in the sources used here (Yu points to further reading for proofs via exchange paths, Lorentz invariance of the S-matrix and causality; PS cite Pauli 1940 and Streater–Wightman). To be filled. The key structural point, as Lecture 10 gave it: for half-integer spin the equations of motion are linear in time derivatives, not second order, so the canonical momentum is proportional to the field itself, $\pi \sim \psi^\dagger$, rather than to its time derivative, $\pi \sim \dot\phi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|Remark: A first-order system: the momentum is ψ† itself]]). Higher spins follow the same pattern: integer spins are quantized like scalars with indices, half-integer spins ($\frac12$, $\frac32$, …) with anticommutators.

> [!remark] Remark: Spin and statistics are an output
> In nonrelativistic quantum mechanics the exclusion principle is an extra postulate: one is told, or shown by spectroscopy, that two electrons cannot occupy the same state ([[§A5.3 The Exclusion Principle and the Periodic Table#^pr-a5-3-2|QM Principle §A5.3.2]]; for identical particles in general, [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]). In relativistic quantum field theory it is not negotiable. A spin-½ field cannot be quantized consistently, with a bounded Hamiltonian and causal propagation, without anticommutators ([[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]]), and anticommutators give the exclusion principle ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]). Without any knowledge of atomic spectra one would have to invent it (Lecture 10: "It's an output, not an input"). Photons, by contrast, are bosons, which is why many of them can occupy one mode, as in a laser.
>
> *Source: Lecture 10 (transcript, end of the lecture) · the user's PHY 513 notes, Ch. 10 §10.2 ("Spin and statistics are an output")*

^rem-c5b-1-3

## Smeared Dirac fields

> [!definition] Definition §C5b.1.2: Smeared Dirac Field on a Time Slice
> For $f \in \mathcal S(\mathbb R^3, \mathbb C^4)$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], componentwise), the **smeared Dirac field** and its adjoint on a time slice are
>
> $$
> \psi(f) = \int d^3x\;f(\mathbf x)^\dagger\psi(\mathbf x) = \sum_a\int d^3x\;\overline{f_a(\mathbf x)}\,\psi_a(\mathbf x), \qquad \psi^\dagger(f) \equiv \psi(f)^\dagger = \int d^3x\;\psi^\dagger(\mathbf x)f(\mathbf x) ;
> $$
>
> $\psi(f)$ is antilinear and $\psi^\dagger(f)$ linear in $f$, and $\langle f, g\rangle \equiv \int d^3x\,f^\dagger g$ is the $L^2(\mathbb R^3, \mathbb C^4)$ product. As for the scalar ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]), $\psi(\mathbf x)$ is the kernel of these operators, an operator-valued distribution ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 and App. A §A.4 (smeared operators, for the scalar) · written here for the Dirac field*

^def-c5b-1-2

> [!theorem] Theorem §C5b.1.4: The Anticommutators Are Identities after Smearing; Smeared Fermi Fields Are Bounded
> For $f, g \in \mathcal S(\mathbb R^3, \mathbb C^4)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|Def. §C5b.1.2]]):
> 1. [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]] means $\{\psi(f), \psi^\dagger(g)\} = \langle f, g\rangle$ and $\{\psi(f), \psi(g)\} = 0$.
> 2. $\psi(f)^2 = 0$, and $\|\psi(f)\| = \|\psi^\dagger(f)\| = \|f\|_{L^2}$: the smeared field is a **bounded** operator, and extends by continuity to every $f \in L^2(\mathbb R^3, \mathbb C^4)$.
> 3. The field at a point is still not an operator: it would need $\|f\|_{L^2} = \infty$ ($f \to \delta$), and $\{\psi_a(\mathbf x), \psi^\dagger_a(\mathbf x)\} = \delta^3(\mathbf 0)$ has no value.
>
> Bosonic smeared fields are unbounded ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]], Step 4: each pair with $\int fg = 1$ is a canonical pair $[Q, P] = i$, which has no bounded solutions).
>
> *Source: stated and derived here (standard: Bratteli & Robinson, Operator Algebras and Quantum Statistical Mechanics 2, §5.2.2) · the user's PHY 513 notes, App. A §A.4 (smeared operators)*

^thm-c5b-1-4

> [!derivation]- Derivation
> **1. Part 1.** Exactly Steps 1–3 of [[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-2|Derivation §C2a.1.2]] with the anticommutator in place of the commutator (it is bilinear too): pairing $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}$ with $\overline{f_a(\mathbf x)}g_b(\mathbf y)$ gives $\{\psi(f), \psi^\dagger(g)\}$ on the left and $\sum_a\int d^3x\,\overline{f_a}g_a = \langle f, g\rangle$ on the right, the kernel $\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ acting as in Step 2 there ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], change of variables with Jacobian $1$). The other relation has kernel $0$.
>
> **2. Nilpotency.** $A \equiv \psi(f)$ satisfies $2A^2 = \{A, A\} = 0$ by part 1.
>
> **3. A projection.** Let $c = \|f\|^2_{L^2} > 0$ and $P \equiv A^\dagger A/c$. Then $P^\dagger = P$ and, using $AA^\dagger = c - A^\dagger A$ (part 1 with $g = f$) and $A^2 = 0$,
>
> $$
> P^2 = \frac{A^\dagger(AA^\dagger)A}{c^2} = \frac{A^\dagger(c - A^\dagger A)A}{c^2} = \frac{A^\dagger A}{c} - \frac{(A^\dagger)^2A^2}{c^2} = P .
> $$
>
> **4. The norm.** For any state $\Psi$, $\|A\Psi\|^2 = \langle\Psi, A^\dagger A\Psi\rangle = c\,\langle\Psi, P\Psi\rangle \le c\|\Psi\|^2$, with equality on the range of $P$. That range is not $\{0\}$: $P = 0$ would give $A = 0$, hence $AA^\dagger + A^\dagger A = 0 \ne c$. So $\|A\| = \sqrt c = \|f\|_{L^2}$, and $\|A^\dagger\| = \|A\|$. A bounded operator depending continuously on $f$ in the $L^2$ norm extends to the closure of $\mathcal S$ in $L^2$, which is $L^2$.
>
> **5. Part 3.** For a nascent delta $f_\varepsilon = \rho_\varepsilon e_a$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3), $\|f_\varepsilon\|^2_{L^2} = \int\rho_\varepsilon^2 = \varepsilon^{-3}\int\rho^2 \to \infty$: no limit operator. The coincident anticommutator is δ at its singular point ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3).
>
> ⚑ By-product: $\psi(f)^2 = 0$ is the Pauli principle at the level of the field: a smeared Fermi field is a two-level system for every $f$ → [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]], [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]], 3.
>
> **What the derivation shows**
> - Anticommutators make the smeared fields bounded, so domain questions that the scalar field raises do not arise for fermions; the singularity is only in the point limit.
> - Used next: the mode algebra ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]).

^der-c5b-1-4

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|Def. §C5b.1.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-2|P1, step 2]]

> [!remark]- Connections
> - The puzzle of [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]] is the quantum face of a classical fact: a Lagrangian of first order in time has momenta that are functions of the coordinates, so phase space is half as large and the canonical pairs are $(\psi, \psi^\dagger)$ — [[§C1.10 Hamiltonian Field Theory#^rem-c1-10-3|§C1.10, Remark: Constraints and first-order Lagrangians]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]].
> - The anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]] have the form of the fermionic field relations of nonrelativistic second quantization; the relativistic field adds two species in one local field, spinors, and a statistics that is forced rather than chosen — [[§C12.2★ Second Quantization#^thm-c12-2-3|QM Theorem §C12.2.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-6|§C5b.2, Remark: What the field adds to the anticommutators of second quantization]].
> - Microcausality for fermions is an anticommutator statement, and the Feynman propagator of the Dirac field carries the fermionic sign of time ordering — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]; the spin–statistics theorem ties the anticommutators of this section to spin ½, the representations with the sign $-1$ under a $2\pi$ rotation — [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-3|Principle §C5b.1.3]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations|§C3.2]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - The anticommutators make smeared fermion fields bounded ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|Theorem §C5b.1.4]]), so the distributional care needed in this chapter is only for point values and coincident labels: the plane-wave delta in $\mathcal S'$, the split exponentials for wave packets, relabelling with Jacobian 1, evaluation of smooth prefactors on the support of δ, the box for δ³(0), integration by parts with fall-off — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]; for the scalar the smeared fields are unbounded and the canonical relations are identities of unbounded operators — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]].
> - Quantum Mechanics lists the proof of the spin–statistics connection as deferred to field theory; this course states the theorem and checks it on its two free fields — [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-3|Principle §C5b.1.3]], [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]].
