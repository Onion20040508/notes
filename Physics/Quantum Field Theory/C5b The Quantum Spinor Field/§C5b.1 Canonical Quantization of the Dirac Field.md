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

*Sources: the user's PHY 513 notes, Ch. 10 §§10.1–10.2 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part A, slides 5–7 and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 52–58 · Yu Zhao-Huan, 量子场论讲义, §5.4.3, §§5.5.1–5.5.2, §5.5.4 · the user's pre-course notes, §1.6, §5.4, §5.5.*

This is the spinor counterpart of [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]: how is the free Dirac field turned into a quantum theory? The classical ingredients have their home in Chapter C5a and are recalled first, as embedded boxes: the Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]), the canonical momentum $\pi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]), the Hamiltonian density ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]) and the field momentum ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]]). Lecture 10 starts from a puzzle in that momentum: the field is its own conjugate, so the commutators of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] would make two coordinates fail to commute. The section therefore begins with the conjugate momentum field itself ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]): what $\pi_\psi = i\psi^\dagger$ means for the canonical pairs, why the puzzle is only apparent ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]]), and that Hamilton's equations still give the Dirac equation ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]]); a ★ part shows by Dirac's constraint analysis why $(\psi, i\psi^\dagger)$ may be treated as canonical pairs ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]). It then states the postulate that replaces the commutators, the equal-time anticommutators, and the spin–statistics theorem that says why; the computations that justify the choice run through [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]–[[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]] and [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]], following [[P1 Canonical Quantization]]. Quantum Mechanics met the anticommutators as an algebra chosen per species ([[§C12.2★ Second Quantization|QM §C12.2★]]) and the negative energies as a filled sea ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]); what the field adds is said where each appears.

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
> | kernel of $\mathcal H$ | $H_{\text{s.p.}}$ | $H_{\text{s.p.}}$ (Caution below) | $h_D$, eq. (3.85) | — |
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

## The classical Dirac field, recalled

The classical Dirac field has its home in Chapter C5a; its boxes are shown here as they stand there. The field and its Lagrangian, defined in [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]:

![[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4]]

Lecture 10 opens the quantization (slide 5, "Canonical Quantization") with this Lagrangian written with the time derivative separated, the form the Hamiltonian formalism of [[§C1b.4 Hamiltonian Field Theory|§C1b.4]] needs:

$$
\mathcal L = \bar\psi\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi = \bar\psi\bigl(i\gamma^0\partial_0 + i\gamma^j\partial_j - m\bigr)\psi .
$$

(The slide prints the spatial term without its $i$; the $i$ belongs there, as in Model §C5a.3.4 and the user's Ch. 10 §10.1, and the momentum, which comes from the $\partial_0$ term alone, is not affected.)

Only the $\partial_0$ term contains a velocity. Differentiating it gives the canonical momenta, derived in §C5a.3:

![[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8]]

The Legendre transform with these momenta, in which the velocities cancel identically because $\mathcal L$ is linear in them, gives the Hamiltonian density, derived in §C5a.3 (Lecture 10, slide 16; PS eqs. (3.84)–(3.85); Yu eq. (5.222)):

![[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9]]

The field momentum, the Noether charge of space translations computed from the Dirac energy–momentum tensor $T^{0i} = i\psi^\dagger\partial^i\psi$ in [[§C5a.4 Bilinears, Chirality and the Weyl Equations|§C5a.4]] (PS eq. (3.105)):

![[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12]]

Quantization keeps these formulas and reads $\psi$, $\psi^\dagger$, $H$ and $\mathbf P$ as operators ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]). What it needs from the momenta, the first thing that differs from the scalar, comes next.

## The conjugate momentum field

> [!theorem] Theorem §C5b.1.1: The Conjugate Momentum Field of the Dirac Field
> For the free Dirac field ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) the canonical momenta ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]) are, by [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]] (recalled above),
>
> $$
> \pi_{\psi,a} = \frac{\partial\mathcal L}{\partial\dot\psi_a} = i(\bar\psi\gamma^0)_a = i\psi^\dagger_a, \qquad \pi_{\bar\psi,a} = 0 ,
> $$
>
> with $\bar\psi$ the Dirac conjugate ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]). What quantization needs from this:
> 1. $\pi_\psi$ contains no velocity: $\pi_\psi = i\psi^\dagger$ is a relation between canonical variables, not a new field. After quantization it is an identity of operator-valued distributions ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]); there is no momentum operator besides $i\psi^\dagger$.
> 2. The canonical pairs are $(\psi_a, \pi_{\psi,a})$, $a = 1, \dots, 4$; $\psi^\dagger$ and $\bar\psi = -i\pi_\psi\gamma^0$ are not further coordinates.
> 3. The equal-time relations in momentum form and in field form are equivalent,
>
> $$
> \{\psi_a(\mathbf x), \pi_{\psi,b}(\mathbf y)\} = i\delta_{ab}\delta^3(\mathbf x - \mathbf y),\ \ \{\pi_{\psi,a}, \pi_{\psi,b}\} = 0 \iff \{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y),\ \ \{\psi^\dagger_a, \psi^\dagger_b\} = 0 ,
> $$
>
> with $\{\psi_a, \psi_b\} = 0$ on both sides, and likewise with commutators; the postulate is [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]].
>
> *Scalar analogue:* the momentum of the scalar is its velocity, $\pi = \dot\phi$, a datum independent of $\phi$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]); for the complex scalar $\pi = \dot\phi^\dagger$, still a velocity ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]).
> *Source: Lecture 10, slide 5 ("Canonical Quantization": $\Pi_\psi = \partial\mathcal L/\partial\dot\psi = \bar\psi i\gamma^0 = i\psi^\dagger$) and slide 7 ("$\Pi \sim \psi$ rather than $\Pi \sim \dot\psi$") · the user's PHY 513 notes, Ch. 10 §10.1 (Derivation "The momentum conjugate to ψ", eq. (diracPi)) and §10.4 (Principle "The equal-time anticommutators": "equivalently $\{\hat\psi_a, \hat\Pi_{\psi,b}\} = i\delta_{ab}\delta^3$") · PS §3.5, p. 52 (above eq. (3.84)) · Yu §5.4.3, eqs. (5.219)–(5.220) and the note after (5.220); §5.5.1, eqs. (5.228)–(5.229); §5.5.2, eqs. (5.238)–(5.239) · the user's pre-course notes, §5.4 ("Plane-wave expansion and Hamiltonian")*

^thm-c5b-1-1

> [!derivation]- Derivation
> **1. The momenta (recalled).** [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]] gives $\pi_{\psi,a} = i(\bar\psi\gamma^0)_a = i\psi^\dagger_a$ and $\pi_{\bar\psi} = 0$; the computation is [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-8|Derivation §C5a.3.8]], steps 1–3 (the $\gamma^0$ of $\bar\psi$ cancelled by the $\gamma^0$ of the time component, $(\gamma^0)^2 = \mathbb 1$; no derivative of $\bar\psi$ in $\mathcal L$). Lecture 10 on the same step: "it's a linear function in the time derivative, so there really is no difficulty." ⚑ By-product: slide 5 takes $\psi^\dagger$ instead of $\bar\psi$ as the second field and finds the same structure → [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|Remark: ψ† or ψ̄ as the partner field]].
>
> **2. A relation, not a definition.** For the scalar, $\pi = \dot\phi$ is solved for the velocity, $\dot\phi = \pi$, and $\pi(\mathbf x)$ is a datum on the slice independent of $\phi(\mathbf x)$ ([[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-2|Derivation §C1b.4.2]], step 2). Step 1 contains no $\dot\psi$, so $\pi_{\psi,a} - i\psi^\dagger_a = 0$ holds whatever the velocities are: it restricts the canonical data instead of adding to them (part 1). The independent data on a slice are the four complex values $\psi_a(\mathbf x)$; the momenta are their adjoints times $i$ (part 2). ⚑ By-product: in Dirac's language this relation is a primary constraint, and the justification for treating $(\psi_a, i\psi^\dagger_a)$ as canonical pairs is its Dirac bracket → [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]].
>
> **3. After quantization.** Canonical quantization promotes the canonical variables to operators and keeps the relations among them ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]]). So $\pi_{\psi,a}(\mathbf x)$ is the operator $i\psi^\dagger_a(\mathbf x)$, the adjoint of $\psi_a(\mathbf x)$ times $i$, an identity of operator-valued distributions ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]): paired with a test function $g$, $\int d^3x\,\pi_{\psi,a}(\mathbf x)\,g(\mathbf x) = i\int d^3x\,\psi^\dagger_a(\mathbf x)\,g(\mathbf x)$.
>
> **4. Momentum form ⇒ field form.** Insert $\pi_{\psi,b}(\mathbf y) = i\psi^\dagger_b(\mathbf y)$. The anticommutator is bilinear and $i$ is a number:
>
> $$
> \{\psi_a(\mathbf x), \pi_{\psi,b}(\mathbf y)\} = \{\psi_a(\mathbf x), i\psi^\dagger_b(\mathbf y)\} = i\,\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} .
> $$
>
> So $\{\psi_a, \pi_{\psi,b}\} = i\delta_{ab}\delta^3$ is $i\{\psi_a, \psi^\dagger_b\} = i\delta_{ab}\delta^3$, and dividing by $i \ne 0$ gives $\{\psi_a, \psi^\dagger_b\} = \delta_{ab}\delta^3$; the steps reverse. The factors $i$ cancel, as on slide 5.
>
> **5. Momentum with momentum.** $\{\pi_{\psi,a}(\mathbf x), \pi_{\psi,b}(\mathbf y)\} = \{i\psi^\dagger_a, i\psi^\dagger_b\} = i^2\{\psi^\dagger_a, \psi^\dagger_b\} = -\{\psi^\dagger_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}$, so $\{\pi, \pi\} = 0 \iff \{\psi^\dagger, \psi^\dagger\} = 0$. The relation $\{\psi_a, \psi_b\} = 0$ contains no momentum. Steps 4–5 used only bilinearity, so they hold verbatim for commutators: $[\psi_a, \pi_{\psi,b}] = i\delta_{ab}\delta^3 \iff [\psi_a, \psi^\dagger_b] = \delta_{ab}\delta^3$, the provisional relations of slide 5 ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]]).
>
> **6. ψ̄ needs no relation of its own.** $\bar\psi_b = \sum_c\psi^\dagger_c(\gamma^0)_{cb}$ is a linear combination of momenta, so its anticommutators follow: $\{\psi_a(\mathbf x), \bar\psi_b(\mathbf y)\} = \sum_c\{\psi_a(\mathbf x), \psi^\dagger_c(\mathbf y)\}(\gamma^0)_{cb} = \sum_c\delta_{ac}(\gamma^0)_{cb}\,\delta^3(\mathbf x - \mathbf y) = (\gamma^0)_{ab}\,\delta^3(\mathbf x - \mathbf y)$. ⚑ By-product: this is the equal-time value $iS(0, \boldsymbol\xi) = \gamma^0\delta^3(\boldsymbol\xi)$ of the anticommutator function → [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]].
>
> **What the derivation shows**
> - The momentum of $\psi$ is fixed by the first-order Lagrangian to be $i\psi^\dagger$, a function of the coordinates' adjoints and not of the velocities; this is the whole difference from the scalar, and the source of Larsen's puzzle ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]]).
> - The canonical relations can be stated with $\pi$ (Yu, the user's §10.4) or with $\psi^\dagger$ (slides, PS); the translation uses only $\pi = i\psi^\dagger$ and bilinearity, and is the same for commutators and anticommutators.
> - Assumptions: those of Model §C5a.3.4 ($\psi$ and $\bar\psi$ varied independently, [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-6|Derivation §C5a.3.6]], step 1).
> - Used next: Hamilton's equations ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]]), the constraint analysis ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]) and the postulate ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).

^der-c5b-1-1

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], [[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-2|Derivation §C1b.4.2]], [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-1|P1, step 1]]

> [!remark] Remark: ψ† or ψ̄ as the partner field, one canonical structure
> Slide 5 and the user's Ch. 10 §10.1 vary $\psi$ and $\psi^\dagger$ as independent fields ("Note: treat ψ and ψ† as independent fields"); [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]] and [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]] vary $\psi$ and $\bar\psi$. The two partners are related by $\bar\psi_a = \sum_b\psi^\dagger_b(\gamma^0)_{ba}$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]), a linear change of the partner field that is invertible because $(\gamma^0)^2 = \mathbb 1$ and leaves $\psi$ alone. They give one canonical structure:
> - **The momentum of ψ is the same**, $i(\bar\psi\gamma^0) = i\psi^\dagger$: holding $\bar\psi$ fixed is holding $\psi^\dagger$ fixed, so $\partial\mathcal L/\partial\dot\psi$ is the same derivative of the same function.
> - **The partner momenta are related by the transposed change.** With $\psi^\dagger_b = \sum_a\bar\psi_a(\gamma^0)_{ab}$, the chain rule gives $\pi_{\bar\psi,a} = \sum_b\frac{\partial\mathcal L}{\partial\dot\psi^\dagger_b}\frac{\partial\dot\psi^\dagger_b}{\partial\dot{\bar\psi}_a} = \sum_b\pi_{\psi^\dagger,b}(\gamma^0)_{ab}$, so $\pi_{\bar\psi} = 0 \iff \pi_{\psi^\dagger} = 0$.
> - **The constraints and brackets agree.** [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]] works with $\bar\psi$, [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-5|★ Theorem §C5b.1.5]] with $\psi^\dagger$, and both give the same Dirac bracket $\{\psi_a, \psi^\dagger_b\}_D = -i\delta_{ab}\delta^3$.
>
> "Treat them as independent" is right for varying the action: the Euler–Lagrange equations of the two fields together are equivalent to those of the eight real components ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]; [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-6|Derivation §C5a.3.6]], step 1). The momentum then shows that the partner is not an independent canonical coordinate: $\psi^\dagger$ *is* the momentum of $\psi$, up to the factor $i$ (Yu, after eq. (5.220); the user's Ch. 10 §10.1). Larsen in the lecture: "I might have a different momentum conjugate of ψ̄, but I'm not going to get distracted by that right now."
>
> *Source: Lecture 10, slide 5 and transcript · the user's PHY 513 notes, Ch. 10 §10.1 · Yu §5.4.3, note after eq. (5.220) · the change of variables written out here*

^rem-c5b-1-2

> [!remark] Remark: A first-order system: the momentum is ψ† itself
> The Lagrangian is linear in $\dot\psi$, so $\pi_\psi = i\psi^\dagger$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]) does not contain $\dot\psi$ and the Legendre map cannot be inverted; the velocities drop out of $\mathcal H$ by themselves ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]; [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]]). The complex scalar's crossover $\pi = \dot\phi^\dagger$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]) is here taken one step further: $\pi$ is $\psi^\dagger$ itself, and $\psi^\dagger$ is not a second canonical coordinate as $\phi^\dagger$ was for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]); why both choices of partner field agree is [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|Remark: ψ† or ψ̄ as the partner field]]. Lorentz invariance together with a first-order equation forces $\pi \propto \psi^\dagger$ rather than $\pi \propto \dot\psi$: an invariant term with one derivative is $\bar\psi\gamma^\mu\partial_\mu\psi$, whose time component is $\psi^\dagger\dot\psi$ (Lecture 10: "it was kind of built in that we needed this in order to write something Lorentz invariant and L linear"). Slide 7 names this the key structural point of the spin–statistics theorem: for half-integer spin the equations of motion are linear in time derivatives, so $\Pi \sim \psi$ rather than $\Pi \sim \dot\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]]). What this does to the canonical relations, and the halving of phase space, is [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]].
>
> *Source: Lecture 10, slides 5 and 7, and transcript · the user's PHY 513 notes, Ch. 10 §10.1 (Derivation "The momentum conjugate to ψ") and §10.2 (Principle "The spin–statistics theorem", Status) · Yu §5.4.3, eqs. (5.219)–(5.220) · PS §3.5, p. 52 · the user's pre-course notes, §5.4 ("unlike the complex scalar field, whose Lagrangian is quadratic in time derivatives")*

^rem-c5b-1-3

> [!remark] Remark: Larsen's puzzle, a field–field relation that is canonical
> Slide 5 calls the provisional relation $[\psi(\mathbf x), \psi^\dagger(\mathbf y)] = \delta^3(\mathbf x - \mathbf y)$ "Strange: field-field commutators supposedly vanish", because in canonical quantization any two coordinates commute, $[q_i, q_j] = 0$ (Lecture 10: "this one is also a coordinate with a different coordinate. Sure, it's a complex conjugate coordinate, but this doesn't sound right. For example, when you do this for the corresponding complex scalar field, definitely not"). The resolution is [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], parts 2–3: $\psi$ and $\psi^\dagger$ are not two coordinates. The $\psi_a(\mathbf x)$ are the coordinates and $i\psi^\dagger_a(\mathbf x)$ their momenta, so $\{\psi_a, \psi^\dagger_b\} = \delta_{ab}\delta^3$ is the coordinate–momentum relation $\{\psi_a, \pi_{\psi,b}\} = i\delta_{ab}\delta^3$ with the factor $i$ divided out. The rule $[q_i, q_j] = 0$ is not violated, because $\psi^\dagger$ is not a $q$. Three consequences:
> - **Phase space is half as large.** The data on a slice are the four complex $\psi_a(\mathbf x)$, eight real numbers per point, and these are coordinates and momenta together: for commuting components the real and imaginary parts of each $\psi_a$ form a canonical pair ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]], second route). Four complex scalar fields would carry $\phi_a$ and $\pi_a = \dot\phi^\dagger_a$, sixteen real numbers per point ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]); correspondingly the Dirac equation is first order in time and needs only $\psi$ at $t = 0$, not $\psi$ and $\dot\psi$.
> - **The oscillator does the same with a and a†.** Its annihilator $a = \sqrt{m\omega/2}\,\bigl(x + ip/(m\omega)\bigr)$ mixes coordinate and momentum, and $[a, a^\dagger] = 1$ is $[x, p] = i$ in disguise ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|§C2a.1, Remark: The oscillator, recalled]]). In these variables the oscillator Lagrangian is $i a^{\ast}\dot a - \omega a^{\ast}a$ up to a total time derivative, the same form as $\mathcal L = i\psi^\dagger\dot\psi - \psi^\dagger H_{\text{s.p.}}\psi$ (up to a divergence, [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]). The Dirac field is written from the start in the complex variables into which the oscillator's $x$ and $p$ have to be combined.
> - **The canonical structure does not choose the statistics.** It gives the same $\{\psi, \psi^\dagger\}$ for commuting and for anticommuting components ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]], part 4); the choice is forced by positive energy and causality ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]]).
>
> *Source: Lecture 10, slide 5 ("Strange") and transcript · the user's PHY 513 notes, Ch. 10 §10.1 (Caution "The provisional quantization, and why it is strange") · Yu §5.4.3, note after eq. (5.220) · the oscillator comparison and the counting written here*

^rem-c5b-1-4

> [!caution] Caution: The provisional commutator quantization, and why it is strange
> Copying the scalar field ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]) one would impose at equal times $[\psi_a(\mathbf x), \pi_{\psi,b}(\mathbf y)] = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, which with $\pi_\psi = i\psi^\dagger$ reads $[\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)] = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, the factors $i$ cancelling ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], part 3; Lecture 10: "Quantization (Provisional)"). It looks strange because a field–field commutator is required to be a delta function; why it only looks so is [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]], and the root is the linearity of $\mathcal L$ in $\dot\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-3|Remark: A first-order system: the momentum is ψ† itself]]). Carried through, the commutator version fails twice: the energy is unbounded below or norms are negative ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]), and propagation is not causal ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]). Both failures disappear with anticommutators ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).
>
> *Source: Lecture 10, slides 5–6 · the user's PHY 513 notes, Ch. 10 §10.1 (Caution "The provisional quantization, and why it is strange") · PS §3.5, pp. 52–56 · Yu §5.5.1*

^cau-c5b-1-2

## The canonical system

> [!definition] Definition §C5b.1.1: Single-Particle Hamiltonian
> The **single-particle Hamiltonian** of the Dirac equation is the $4\times4$ matrix differential operator
>
> $$
> H_{\text{s.p.}} \equiv \gamma^0\bigl(-i\boldsymbol\gamma\cdot\nabla + m\bigr) = -i\boldsymbol\alpha\cdot\nabla + \beta m, \qquad \boldsymbol\gamma\cdot\nabla \equiv \gamma^j\partial_j, \quad \boldsymbol\alpha = \gamma^0\boldsymbol\gamma, \ \beta = \gamma^0 ,
> $$
>
> the kernel of the Hamiltonian density, $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]). It is Hermitian ($\boldsymbol\alpha$, $\beta$ Hermitian, same theorem), and on $e^{i\mathbf p\cdot\mathbf x}$ it acts as the matrix $H_{\text{s.p.}}(\mathbf p) = \gamma^0(\gamma^jp^j + m)$ (names in other sources: [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-3|Caution: Names for the single-particle Hamiltonian]]). It is the Hamiltonian that relativistic quantum mechanics takes for a four-component wave function ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]).
>
> *Source: Lecture 10, slide 16 · the user's PHY 513 notes, Ch. 10 §10.5 (Definition "The single-particle Hamiltonian"; there $\gamma^0\gamma^i$ is called anti-Hermitian: it is Hermitian, $(\gamma^0\gamma^i)^\dagger = \gamma^{i\dagger}\gamma^0 = -\gamma^i\gamma^0 = \gamma^0\gamma^i$, Step 5 of [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-9|Derivation §C5a.3.9]], which is what makes $\gamma^0\gamma^i(-i\partial_i)$ Hermitian) · PS §3.5, eq. (3.85)*

^def-c5b-1-1

> [!caution] Caution: Names for the single-particle Hamiltonian
> One operator, several names. These notes write $H_{\text{s.p.}}$ everywhere, as Lecture 10 (slide 16) and the user's PHY 513 notes (Ch. 10 §10.5) do; Peskin–Schroeder write the bracket of eq. (3.84), $-i\gamma^0\boldsymbol\gamma\cdot\nabla + m\gamma^0$, and name it $h_D = -i\boldsymbol\alpha\cdot\nabla + m\beta$ in eq. (3.85), "the Dirac Hamiltonian of one-particle quantum mechanics"; earlier drafts of this vault followed them, with $h_D$ for it and $h(\mathbf p)$ for its momentum-space form, now $H_{\text{s.p.}}(\mathbf p)$. Quantum Mechanics (Sakurai) also calls it the Dirac Hamiltonian, $H = c\,\boldsymbol\alpha\cdot\mathbf p + \beta mc^2$, acting on a four-component wave function ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]). In momentum space, with $\hbar = c = 1$, $H_{\text{s.p.}}(\mathbf p) = \boldsymbol\alpha\cdot\mathbf p + \beta m = \gamma^0(\gamma^jp^j + m)$. Not to be confused with the field Hamiltonian $H = \int d^3x\,\psi^\dagger H_{\text{s.p.}}\psi$, an operator on Fock space ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]), or with the density $\mathcal H$.
>
> *Source: Lecture 10, slide 16 · the user's PHY 513 notes, Ch. 10 §10.5 · PS §3.5, eq. (3.85) · Sakurai, eqs. (8.51)–(8.53), as in QM §C13.2★*

^cau-c5b-1-3

> [!model] Model §C5b.1.2: The Free Dirac Field as a Canonical System
> The free Dirac field of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, has the four canonical pairs $(\psi_a, \pi_a)$ with $\pi_a = i\psi_a^\dagger$ and no momentum conjugate to $\bar\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], from [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]), and the Hamiltonian
>
> $$
> H = \int d^3x\;\psi^\dagger H_{\text{s.p.}}\psi , \qquad \mathbf P = \int d^3x\;\psi^\dagger(-i\nabla)\psi = -\int d^3x\;\pi\nabla\psi ,
> $$
>
> with the single-particle Hamiltonian $H_{\text{s.p.}} = -i\boldsymbol\alpha\cdot\nabla + \beta m$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]], the integral of the density of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]], and $\mathbf P$ the Noether momentum of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]] (both recalled above, read as operators in the order written; $H$ is reordered in [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], $\mathbf P$ needs no reordering, [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]]); on solutions of the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) $H_{\text{s.p.}}\psi = i\partial_t\psi$, which is also what Hamilton's equations of the pairs give ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]]).
>
> *Assumptions:* $m > 0$; the field and its derivatives fall off at spatial infinity (classically), or are read against wave packets (quantum). The quantization rule is not part of the model: it is decided below ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).
> *Scalar analogue:* the free complex scalar, [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]].
> *Source: Lecture 10, slides 5 and 16 · the user's PHY 513 notes, Ch. 10 §10.1 and §10.5 · PS §3.5, eqs. (3.83)–(3.85), (3.105) · Yu §5.4.3, eqs. (5.219), (5.222) · the user's pre-course notes, §5.5*

^mod-c5b-1-2

> [!theorem] Theorem §C5b.1.3: Hamilton's Equations of the Dirac Field
> Take the canonical pairs $(\psi_a, \pi_a)$, $\pi_a = i\psi^\dagger_a$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]), with the Hamiltonian of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] as a functional of them, $H[\psi, \pi] = \int d^3x\,(-i\pi)H_{\text{s.p.}}\psi$ ($H_{\text{s.p.}}$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]]). For commuting (classical) components, Hamilton's equations ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]]), equivalently the bracket evolution $\dot F = \{F, H\}$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]]) with $\{\psi_a(\mathbf x), \pi_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, i.e. $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]]; justified as a Dirac bracket in [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]), are
>
> $$
> \dot\psi = -iH_{\text{s.p.}}\psi , \qquad \dot\psi^\dagger = -\partial_j\psi^\dagger\,\alpha^j + im\,\psi^\dagger\beta = \bigl(-iH_{\text{s.p.}}\psi\bigr)^\dagger .
> $$
>
> The first is $i\partial_t\psi = H_{\text{s.p.}}\psi$, the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) multiplied by $\gamma^0$; the second is its adjoint, the conjugate equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], part 2): the two Hamilton equations are one complex equation.
>
> *Scalar analogue:* [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]] ($\dot\phi = \pi$, $\dot\pi = \nabla^2\phi - m^2\phi$, together the Klein–Gordon equation).
> *Source: the user's PHY 513 notes, Ch. 10 §10.5 ("Multiplying the Dirac equation by $\gamma^0$ gives $i\partial_t\psi = H_{\text{s.p.}}\psi$") · PS §3.5, eqs. (3.84)–(3.85) · the user's pre-course notes, §1.6 (canonical field equations) · Hamilton's equations for $\psi$ worked out here*

^thm-c5b-1-3

> [!derivation]- Derivation
> **1. H in the canonical variables.** From $\pi_a = i\psi^\dagger_a$, $\psi^\dagger_a = -i\pi_a$. So $H = \int d^3y\,\sum_{b,c}\psi^\dagger_b(H_{\text{s.p.}})_{bc}\psi_c = \int d^3y\,\sum_b(-i)\pi_b(\mathbf y)\,(H_{\text{s.p.}}\psi)_b(\mathbf y)$, with $H_{\text{s.p.}} = -i\alpha^j\partial_j + \beta m$ acting on $\psi$ only.
>
> **2. Derivative with respect to π.** $H$ is linear in $\pi$ and contains no derivative of $\pi$, so varying $\pi_b \to \pi_b + \varepsilon\zeta_b$ changes $H$ by $\varepsilon\int d^3y\,(-i)\zeta_b(H_{\text{s.p.}}\psi)_b$ and, by [[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-4|Derivation §C1b.4.4]], step 6, $\delta H/\delta\pi_b(\mathbf x) = -i(H_{\text{s.p.}}\psi)_b(\mathbf x)$.
>
> **3. The first Hamilton equation.** $\dot\psi_b = \delta H/\delta\pi_b = -i(H_{\text{s.p.}}\psi)_b$. Multiplied by $i$: $i\partial_t\psi = H_{\text{s.p.}}\psi = \gamma^0(-i\gamma^j\partial_j + m)\psi$. Multiplied on the left by $\gamma^0$, with $(\gamma^0)^2 = \mathbb 1$: $i\gamma^0\partial_0\psi = (-i\gamma^j\partial_j + m)\psi$, i.e. $(i\gamma^\mu\partial_\mu - m)\psi = 0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-9|Derivation §C5a.3.9]], step 6, read backwards).
>
> **4. Derivative with respect to ψ.** Vary $\psi_c \to \psi_c + \varepsilon\eta_c$ with $\eta$ a test function: $\delta H = \varepsilon\int d^3y\,(-i)\sum_{b,c}\pi_b\bigl[-i(\alpha^j)_{bc}\partial_j\eta_c + m\beta_{bc}\eta_c\bigr]$. Move the derivative off $\eta$: $\int d^3y\,\pi_b\,\partial_j\eta_c = -\int d^3y\,(\partial_j\pi_b)\,\eta_c$, the surface term vanishing because $\eta$ has compact support ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]). So
>
> $$
> \delta H = \varepsilon\int d^3y\,(-i)\sum_{b,c}\bigl[i(\partial_j\pi_b)(\alpha^j)_{bc} + m\pi_b\beta_{bc}\bigr]\eta_c , \qquad \frac{\delta H}{\delta\psi_c} = (\partial_j\pi\,\alpha^j)_c - im(\pi\beta)_c .
> $$
>
> **5. The second Hamilton equation.** $\dot\pi_c = -\delta H/\delta\psi_c = -(\partial_j\pi\,\alpha^j)_c + im(\pi\beta)_c$. Insert $\pi = i\psi^\dagger$: $i\dot\psi^\dagger = -i\,\partial_j\psi^\dagger\alpha^j + i\cdot im\,\psi^\dagger\beta$; dividing by $i$, $\dot\psi^\dagger = -\partial_j\psi^\dagger\alpha^j + im\,\psi^\dagger\beta$.
>
> **6. It is the adjoint of step 3.** Step 3 reads $\dot\psi = -i(-i\alpha^j\partial_j\psi + m\beta\psi) = -\alpha^j\partial_j\psi - im\beta\psi$. Its adjoint, with $(M\psi)^\dagger = \psi^\dagger M^\dagger$, $\alpha^{j\dagger} = \alpha^j$, $\beta^\dagger = \beta$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-9|Derivation §C5a.3.9]], step 5), $i \to -i$ and $\partial_j$ real, is $\dot\psi^\dagger = -\partial_j\psi^\dagger\alpha^j + im\,\psi^\dagger\beta$: step 5. The second equation adds nothing; this is part 3 of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]] in Hamiltonian form.
>
> **7. Bracket form.** By [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]], $\dot\psi_a(\mathbf x) = \{\psi_a(\mathbf x), H\}$. With $C_b \equiv (H_{\text{s.p.}}\psi)_b$, the Leibniz rule gives $\{\psi_a(\mathbf x), -i\pi_b(\mathbf y)C_b(\mathbf y)\} = -i\{\psi_a(\mathbf x), \pi_b(\mathbf y)\}C_b(\mathbf y) - i\pi_b(\mathbf y)\{\psi_a(\mathbf x), C_b(\mathbf y)\}$; the second bracket is zero ($C_b$ contains only $\psi$ and its spatial derivatives, and $\{\psi, \psi\} = 0$). Integrating $\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ over $\mathbf y$: $\{\psi_a(\mathbf x), H\} = -iC_a(\mathbf x)$, step 3 again. ⚑ By-product: with operators and the anticommutator in place of the bracket this computation is the Heisenberg equation of the quantum field, and it gives the same Dirac equation with commutators too → [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]], [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|§C5b.6, Remark: The field equation does not choose the statistics]].
>
> **What the derivation shows**
> - The canonical structure ($\psi$, $\pi = i\psi^\dagger$, $H = \int\psi^\dagger H_{\text{s.p.}}\psi$) reproduces the field equation although the Legendre map is not invertible: the velocity $\dot\psi$ is given by Hamilton's first equation, not by solving $\pi(\dot\psi)$.
> - Half the data, half the equations: one first-order equation for $\psi$, whose adjoint is the equation for $\pi$; compare two real equations per scalar component ([[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]]).
> - Assumptions: commuting components; $\psi$, $\pi$ falling off at infinity (step 4). For Grassmann-odd components the same steps hold with the graded bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]], since only $\{\psi, \pi\}$ and $\{\psi, \psi\} = 0$ enter.
> - Used next: the Heisenberg field ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]]).

^der-c5b-1-3

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]

> [!remark] Remark: What the conjugate momentum is not, for spinors
> The three warnings of [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]], for the Dirac field:
> - **Not a velocity.** $\pi_\psi = i\psi^\dagger$ contains no $\dot\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]). The velocity is what Hamilton's first equation gives, $\dot\psi = -iH_{\text{s.p.}}\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]]), not the inverse of a Legendre map.
> - **Not ψ̄.** The Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) is what makes bilinears covariant; the momentum is $i\psi^\dagger$, without the $\gamma^0$, which the $\gamma^0$ of the time component of $\gamma^\mu\partial_\mu$ cancels ($(\gamma^0)^2 = \mathbb 1$, [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-8|Derivation §C5a.3.8]], step 2). $\bar\psi$ itself has momentum zero.
> - **Not the momentum of the field.** The momentum the field carries is the Noether charge of spatial translations, $\mathbf P = \int d^3x\,\psi^\dagger(-i\nabla)\psi$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]]), a single (operator) quantity built from $\pi_\psi$: $\mathbf P = -\int d^3x\,\pi_\psi\nabla\psi$, the scalar's $P^i = -\int d^3x\,\pi\,\partial_i\phi$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]) with $\pi_\psi$ in place of $\pi$. The canonical momentum is a field, one per point and component, conjugate to $\psi$ in the brackets.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.4 (Caution "What the conjugate momentum is not": "for a Dirac field $\pi = i\psi^\dagger$, no velocity at all") and Ch. 8 §8.8, eq. (diracP) · PS §3.5, eq. (3.105) · the comparison written here*

^rem-c5b-1-5

## ★ Constraints and the Dirac bracket

★ *Beyond PHY 513: none of the course sources (Lecture 10, the user's PHY 513 notes, Peskin–Schroeder §3.5, Yu §5.4–§5.5) analyses the relation $\pi_\psi = i\psi^\dagger$ as a constraint; the statements below are derived here, by Dirac's method, to show why $(\psi_a, i\psi^\dagger_a)$ may be treated as canonical pairs and why the normalization of the canonical relations does not depend on how the Lagrangian is written.*

> [!definition] ★ Definition §C5b.1.2: Primary Constraint
> When the momenta $\pi_A = \partial\mathcal L/\partial\dot q^A$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]) cannot be solved for all the velocities, the canonical data reached by the Legendre map satisfy relations
>
> $$
> \varphi_k(q, \nabla q, \pi) = 0 , \qquad k = 1, \dots, K ,
> $$
>
> that hold whatever the velocities are. These are the **primary constraints**, written $\varphi_k \approx 0$ (**weak equality**): they are imposed only after brackets have been computed, since brackets differentiate in directions off the constraint surface.
>
> *Source: standard (P. A. M. Dirac, Lectures on Quantum Mechanics, 1964, Lecture 1); in-course instances: $\pi^0 = 0$ of the vector field ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]]) and $\pi_\psi = i\psi^\dagger$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]])*

^def-c5b-1-2

> [!definition] ★ Definition §C5b.1.3: Second-Class Constraints
> A set of constraints $\varphi_k \approx 0$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|★ Def. §C5b.1.2]]) is **second class** if the matrix of their Poisson brackets ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]]),
>
> $$
> C_{kl}(\mathbf x, \mathbf y) = \{\varphi_k(\mathbf x), \varphi_l(\mathbf y)\} ,
> $$
>
> is invertible on the constraint surface: there is $C^{-1}$ with $\sum_l\int d^3w\,C_{kl}(\mathbf x, \mathbf w)(C^{-1})^{lm}(\mathbf w, \mathbf y) \approx \delta_k^{\,m}\delta^3(\mathbf x - \mathbf y)$. (A constraint whose bracket with every constraint vanishes weakly is first class instead; first-class constraints generate gauge transformations, [[§C4.2★ The Proca Field#^rem-c4-2-4|§C4.2★, ★ Remark: Second-class constraints, and why Maxwell differs]].)
>
> *Source: standard (Dirac, Lectures on Quantum Mechanics, Lectures 1–2)*

^def-c5b-1-3

> [!definition] ★ Definition §C5b.1.4: Dirac Bracket
> For second-class constraints $\varphi_k \approx 0$ with bracket matrix $C$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-3|★ Def. §C5b.1.3]]), the **Dirac bracket** of two functionals of the canonical data is
>
> $$
> \{F, G\}_D = \{F, G\} - \sum_{k,l}\int d^3z\,d^3w\;\{F, \varphi_k(\mathbf z)\}\,(C^{-1})^{kl}(\mathbf z, \mathbf w)\,\{\varphi_l(\mathbf w), G\} .
> $$
>
> It has $\{\varphi_k, G\}_D \approx 0$ for every $G$, so the constraints may be set to zero before or after it is computed. Dirac's rule quantizes a system with second-class constraints by $\{F, G\}_D \to -i[F, G]$ (an anticommutator for two odd quantities, [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]]).
>
> *Source: standard (Dirac, Lectures on Quantum Mechanics, Lecture 2)*

^def-c5b-1-4

> [!caution] ★ Caution: Which side a Grassmann derivative acts from
> If the components of $\psi$ are taken Grassmann-odd already classically (anticommuting numbers, so that they match the anticommuting operators; the user's PHY 513 notes, Ch. 3 §3.3: "derivatives must be taken consistently from one side"), a derivative with respect to an odd variable depends on the side: for odd $\theta$, $\eta$, the **left derivative** gives $\partial^L(\theta\eta)/\partial\theta = \eta$, while the **right derivative**, which first moves $\theta$ to the right end ($\theta\eta = -\eta\theta$), gives $\partial^R(\theta\eta)/\partial\theta = -\eta$. Applied to the kinetic term $i\psi^\dagger_b\dot\psi_b$, the right derivative gives the course's momentum $\pi_\psi = i\psi^\dagger$, the left derivative $-i\psi^\dagger$. These notes take **momenta as right derivatives** and use the bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]], in which the first slot is differentiated from the right and the second from the left; with commuting components both derivatives agree and nothing changes.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Derivation "The Euler–Lagrange equation for other kinds of field", Spinor) · the sign computation written here*

^cau-c5b-1-4

> [!definition] ★ Definition §C5b.1.5: Graded Poisson Bracket
> Let the canonical variables $(q^A, p_A)$ have parities $\varepsilon_A \in \{0, 1\}$ (0: commuting, 1: Grassmann-odd; $p_A$ has the parity of $q^A$), with momenta $p_A = \partial^R\mathcal L/\partial\dot q^A$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-4|★ Caution: Which side a Grassmann derivative acts from]]). The **graded Poisson bracket** is
>
> $$
> \{F, G\} = \sum_A\int d^3z\,\Bigl[\frac{\delta^RF}{\delta q^A(\mathbf z)}\,\frac{\delta^LG}{\delta p_A(\mathbf z)} - (-1)^{\varepsilon_A}\,\frac{\delta^RF}{\delta p_A(\mathbf z)}\,\frac{\delta^LG}{\delta q^A(\mathbf z)}\Bigr] .
> $$
>
> For $\varepsilon_A = 0$ it is [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]]. For either parity $\{q^A(\mathbf x), p_B(\mathbf y)\} = \delta^A_{\ B}\,\delta^3(\mathbf x - \mathbf y)$, and $\{p_B(\mathbf y), q^A(\mathbf x)\} = -(-1)^{\varepsilon_A}\delta^A_{\ B}\,\delta^3(\mathbf x - \mathbf y)$: antisymmetric for even, symmetric for odd variables. Quantization: $\{F, G\} \to -i[F, G]$, with an anticommutator in place of the commutator when $F$ and $G$ are both odd.
>
> *Source: standard (Henneaux & Teitelboim, Quantization of Gauge Systems, on Grassmann variables); convention fixed here so that $\pi_\psi = i\psi^\dagger$*

^def-c5b-1-5

> [!theorem] ★ Theorem §C5b.1.4: The Dirac Field's Constraints Are Second Class; Its Dirac Bracket
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] with coordinates $\psi_a$, $\bar\psi_a$, momenta $\pi_a \equiv \pi_{\psi,a}$, $\bar\pi_a \equiv \pi_{\bar\psi,a}$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]), and components of parity $\varepsilon = 0$ (commuting) or $\varepsilon = 1$ (Grassmann-odd), with the bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]]:
> 1. The primary constraints ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|★ Def. §C5b.1.2]]) are $\chi_a = \pi_a - i(\bar\psi\gamma^0)_a = \pi_a - i\psi^\dagger_a \approx 0$ and $\bar\chi_a = \bar\pi_a \approx 0$.
> 2. They are second class ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-3|★ Def. §C5b.1.3]]): $\{\chi_a(\mathbf x), \bar\chi_b(\mathbf y)\} = -i(\gamma^0)_{ba}\,\delta^3(\mathbf x - \mathbf y)$, $\{\chi_a, \chi_b\} = \{\bar\chi_a, \bar\chi_b\} = 0$; no further constraints arise.
> 3. The Dirac brackets ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-4|★ Def. §C5b.1.4]]) are, for either parity,
>
> $$
> \{\psi_a(\mathbf x), \bar\psi_b(\mathbf y)\}_D = -i(\gamma^0)_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad \{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}_D = -i\delta_{ab}\,\delta^3(\mathbf x - \mathbf y),
> $$
>
> $\{\psi_a, \psi_b\}_D = \{\psi^\dagger_a, \psi^\dagger_b\}_D = 0$ and $\{\psi_a(\mathbf x), \pi_b(\mathbf y)\}_D = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
> 4. Dirac's rule gives $[\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)] = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ for $\varepsilon = 0$ (the provisional relations, [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]]) and $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ for $\varepsilon = 1$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]): the constraint analysis fixes which fields pair and with what normalization, not the statistics.
>
> *Source: derived here; no course source does the constraint analysis. Method standard (Dirac, Lectures on Quantum Mechanics, 1964; Henneaux & Teitelboim, Quantization of Gauge Systems, for Grassmann variables). Inputs: Theorem §C5a.3.8 (PS §3.5, p. 52; Yu eq. (5.219)); Grassmann fields as in the user's PHY 513 notes, Ch. 3 §3.3*

^thm-c5b-1-4

> [!derivation]- Derivation
> **1. Momenta and constraints.** The time-derivative part of $\mathcal L$ is $\sum_{b,c}i\bar\psi_b(\gamma^0)_{bc}\dot\psi_c$. In the right derivative with respect to $\dot\psi_a$ the velocity already stands at the right end, so no sign arises: $\pi_a = \sum_bi\bar\psi_b(\gamma^0)_{ba} = i(\bar\psi\gamma^0)_a = i\psi^\dagger_a$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-8|Derivation §C5a.3.8]], step 2, where the order of factors did not matter). $\mathcal L$ contains no $\dot{\bar\psi}$: $\bar\pi_a = 0$. Both relations hold for all velocities: part 1. The constraints have the parity $\varepsilon$ of the fields.
>
> **2. Fundamental brackets.** By [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]]: $\{\psi_a(\mathbf x), \pi_b(\mathbf y)\} = \{\bar\psi_a(\mathbf x), \bar\pi_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$; reversed, $\{\pi_b(\mathbf y), \psi_a(\mathbf x)\} = \{\bar\pi_b(\mathbf y), \bar\psi_a(\mathbf x)\} = -(-1)^\varepsilon\delta_{ab}\delta^3(\mathbf x - \mathbf y)$. Every other pair has bracket zero: two coordinates, two momenta, $\psi$ with $\bar\pi$, $\bar\psi$ with $\pi$. Numerical factors ($i$, entries of $\gamma^0$) are even and pass through brackets without signs.
>
> **3. χ with χ.** Expand into all four terms: $\{\chi_a, \chi_b\} = \{\pi_a, \pi_b\} - i\sum_c(\gamma^0)_{cb}\{\pi_a, \bar\psi_c\} - i\sum_c(\gamma^0)_{ca}\{\bar\psi_c, \pi_b\} - \sum_{c,d}(\gamma^0)_{ca}(\gamma^0)_{db}\{\bar\psi_c, \bar\psi_d\}$. Each bracket is zero by step 2 ($\pi$ is the momentum of $\psi$, not of $\bar\psi$). So $\{\chi_a, \chi_b\} = 0$; likewise $\{\bar\chi_a, \bar\chi_b\} = \{\bar\pi_a, \bar\pi_b\} = 0$.
>
> **4. χ with χ̄, both orders.** $\{\chi_a(\mathbf x), \bar\chi_b(\mathbf y)\} = \{\pi_a, \bar\pi_b\} - i\sum_c(\gamma^0)_{ca}\{\bar\psi_c(\mathbf x), \bar\pi_b(\mathbf y)\} = 0 - i(\gamma^0)_{ba}\delta^3(\mathbf x - \mathbf y)$, the sum over $c$ eliminating $c$ against $\delta_{cb}$. In the other order, $\{\bar\chi_b(\mathbf y), \chi_a(\mathbf x)\} = -i\sum_c(\gamma^0)_{ca}\{\bar\pi_b(\mathbf y), \bar\psi_c(\mathbf x)\} = -i(\gamma^0)_{ba}\cdot\bigl(-(-1)^\varepsilon\bigr)\delta^3 = i(-1)^\varepsilon(\gamma^0)_{ba}\delta^3(\mathbf x - \mathbf y)$.
>
> **5. The matrix and its inverse.** Order the constraints $(\chi_a, \bar\chi_a)$. Then $C = \begin{pmatrix}0 & X\\ Y & 0\end{pmatrix}\delta^3(\mathbf x - \mathbf y)$ with $X_{ab} = -i(\gamma^0)_{ba}$, i.e. $X = -i(\gamma^0)^{\mathsf T}$ (row $\chi_a$, column $\bar\chi_b$), and $Y_{ba} = i(-1)^\varepsilon(\gamma^0)_{ba}$, i.e. $Y = i(-1)^\varepsilon\gamma^0$ (row $\bar\chi_b$, column $\chi_a$). Since $(\gamma^0)^2 = \mathbb 1$, also $((\gamma^0)^{\mathsf T})^2 = \mathbb 1$, so $X^{-1} = i(\gamma^0)^{\mathsf T}$ and $Y^{-1} = -i(-1)^\varepsilon\gamma^0$ (check: $YY^{-1} = i\cdot(-i)\,(-1)^{2\varepsilon}(\gamma^0)^2 = \mathbb 1$). The inverse is $C^{-1} = \begin{pmatrix}0 & Y^{-1}\\ X^{-1} & 0\end{pmatrix}\delta^3$: indeed $CC^{-1} = \begin{pmatrix}XX^{-1} & 0\\ 0 & YY^{-1}\end{pmatrix} = \mathbb 1$, the spatial kernels composing as $\int d^3w\,\delta^3(\mathbf x - \mathbf w)\delta^3(\mathbf w - \mathbf y) = \delta^3(\mathbf x - \mathbf y)$, a convolution of deltas ([[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-5|Derivation §C1b.4.5]], step 4). In components: $(C^{-1})^{\chi_a\bar\chi_b} = -i(-1)^\varepsilon(\gamma^0)_{ab}\delta^3$, $(C^{-1})^{\bar\chi_b\chi_a} = i(\gamma^0)_{ab}\delta^3$. $C$ is invertible: part 2's second-class statement.
>
> **6. No secondary constraints.** Add the constraints to the Hamiltonian with arbitrary multipliers, $H_T = H + \int d^3z\,\sum_B\varphi_B(\mathbf z)u_B(\mathbf z)$, $\varphi_B$ running over $\chi_a$, $\bar\chi_a$. Preserving the constraints in time, $\{\varphi_A, H_T\} \approx 0$, reads $\{\varphi_A, H\} + \sum_B\int C_{AB}u_B \approx 0$: the multipliers are not canonical variables, so $\{\varphi_A, u_B\} = 0$, and the term $\varphi_B\{\varphi_A, u_B\}$ vanishes. $C$ is invertible, so this fixes $u = -C^{-1}\{\varphi, H\}$ and imposes no new relation on the data: part 2's last clause. (Contrast the vector field, where $\pi_0 \approx 0$ needs a secondary constraint, Gauss's law, before a second-class pair appears: [[§C4.2★ The Proca Field#^rem-c4-2-4|§C4.2★, ★ Remark: Second-class constraints, and why Maxwell differs]].)
>
> **7. The ψ–ψ̄ Dirac bracket.** The Poisson bracket $\{\psi_a, \bar\psi_b\}$ is zero (two coordinates). The brackets with the constraints, by step 2: $\{\psi_a(\mathbf x), \chi_c(\mathbf z)\} = \{\psi_a(\mathbf x), \pi_c(\mathbf z)\} = \delta_{ac}\delta^3(\mathbf x - \mathbf z)$; $\{\psi_a, \bar\chi_d\} = \{\psi_a, \bar\pi_d\} = 0$; $\{\chi_c(\mathbf w), \bar\psi_b(\mathbf y)\} = 0$; $\{\bar\chi_d(\mathbf w), \bar\psi_b(\mathbf y)\} = \{\bar\pi_d(\mathbf w), \bar\psi_b(\mathbf y)\} = -(-1)^\varepsilon\delta_{db}\delta^3(\mathbf w - \mathbf y)$. Only the block $(C^{-1})^{\chi_c\bar\chi_d}$ meets two nonzero factors:
>
> $$
> \{\psi_a(\mathbf x), \bar\psi_b(\mathbf y)\}_D = 0 - \sum_{c,d}\int d^3z\,d^3w\;\delta_{ac}\delta^3(\mathbf x - \mathbf z)\,\bigl[-i(-1)^\varepsilon(\gamma^0)_{cd}\delta^3(\mathbf z - \mathbf w)\bigr]\,\bigl[-(-1)^\varepsilon\delta_{db}\delta^3(\mathbf w - \mathbf y)\bigr] .
> $$
>
> The $\mathbf z$ integral sets $\mathbf z = \mathbf x$ and $c = a$; the $\mathbf w$ integral sets $\mathbf w = \mathbf y$ and $d = b$. The signs multiply to $-\cdot(-i)\cdot(-1) = -i$ and the parity factors to $(-1)^{2\varepsilon} = 1$: $\{\psi_a(\mathbf x), \bar\psi_b(\mathbf y)\}_D = -i(\gamma^0)_{ab}\delta^3(\mathbf x - \mathbf y)$. ⚑ By-product: the parity $\varepsilon$ cancels; commuting and Grassmann fields have the same Dirac bracket → part 4.
>
> **8. The ψ–ψ† Dirac bracket.** $\psi^\dagger_b = \sum_c\bar\psi_c(\gamma^0)_{cb}$ (multiply $\bar\psi = \psi^\dagger\gamma^0$ by $\gamma^0$ on the right). The bracket is linear in its second slot with even coefficients, so $\{\psi_a, \psi^\dagger_b\}_D = \sum_c\{\psi_a, \bar\psi_c\}_D(\gamma^0)_{cb} = -i\sum_c(\gamma^0)_{ac}(\gamma^0)_{cb}\,\delta^3 = -i\bigl((\gamma^0)^2\bigr)_{ab}\delta^3 = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **9. The remaining brackets.** $\{\psi_a, \psi_b\}_D$: the Poisson bracket is zero, and every correction term contains $\{\psi_a, \bar\chi_d\} = 0$ or $\{\bar\chi_d, \psi_b\} = \{\bar\pi_d, \psi_b\} = 0$, so it is zero. $\{\bar\psi_a, \bar\psi_b\}_D$: zero Poisson bracket; the corrections contain $\{\bar\psi_a, \chi_c\} = 0$ or $\{\chi_c, \bar\psi_b\} = 0$; so zero, and hence $\{\psi^\dagger_a, \psi^\dagger_b\}_D = 0$ by the linear relation of step 8. $\{\psi_a, \pi_b\}_D$: the Poisson bracket is $\delta_{ab}\delta^3$ and the only candidate correction contains $\{\bar\chi_d, \pi_b\} = \{\bar\pi_d, \pi_b\} = 0$. Consistency check: with $\pi \approx i\psi^\dagger$, $i\{\psi_a, \psi^\dagger_b\}_D = i(-i)\delta_{ab}\delta^3 = \delta_{ab}\delta^3$, as it must be, since Dirac brackets with $\chi$ vanish ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-4|★ Def. §C5b.1.4]]).
>
> **10. Quantization.** Dirac's rule $\{F, G\}_D \to -i[F, G]$ (anticommutator for two odd quantities) is $[F, G] = i\{F, G\}_D$. For $\varepsilon = 0$: $[\psi_a, \psi^\dagger_b] = i(-i)\delta_{ab}\delta^3 = \delta_{ab}\delta^3$. For $\varepsilon = 1$: $\{\psi_a, \psi^\dagger_b\} = \delta_{ab}\delta^3$, and $\{\psi_a, \psi_b\} = \{\psi^\dagger_a, \psi^\dagger_b\} = 0$ from step 9: part 4. ⚑ By-product: the canonical analysis delivers the coefficient $1$ and the pairing of $\psi$ with $\psi^\dagger$ for either statistics; the statistics is chosen by positivity and causality → [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]], [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|§C5b.6, Remark: The field equation does not choose the statistics]].
>
> **What the derivation shows**
> - $\pi_\psi = i\psi^\dagger$ and $\pi_{\bar\psi} = 0$ are a second-class set; the Dirac bracket eliminates $(\pi, \bar\pi)$ and leaves $\psi$, $\psi^\dagger$ with $\{\psi, \psi^\dagger\}_D = -i\delta$, i.e. $\{\psi, \pi\}_D = \delta$. This is what licenses treating $(\psi_a, i\psi^\dagger_a)$ as canonical pairs in [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]] and [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]].
> - Counting: $\psi_a$, $\bar\psi_a$ and their momenta are sixteen complex variables per point, the eight second-class constraints remove eight, and the eight left are $\psi_a$ and $\psi^\dagger_a$: half the phase space of four complex scalars ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]]).
> - Assumptions: right-derivative momenta; spatial kernels composed as convolutions of deltas.
> - Used next: the symmetric Lagrangian ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-5|★ Theorem §C5b.1.5]]); the postulate ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).

^der-c5b-1-4

> [!derivation]- Derivation (second route: real and imaginary parts, commuting components)
> **1. Split ψ.** For commuting components write $\psi_a = (q_a + ip_a)/\sqrt2$ with real fields $q_a$, $p_a$. The time-derivative part of $\mathcal L$ is $i\psi^\dagger_a\dot\psi_a$ (summed over $a$), and expanding all four terms of the product,
>
> $$
> i\psi^{\ast}_a\dot\psi_a = \frac i2(q_a - ip_a)(\dot q_a + i\dot p_a) = \frac i2\bigl(q_a\dot q_a + p_a\dot p_a\bigr) + \frac12\bigl(p_a\dot q_a - q_a\dot p_a\bigr) .
> $$
>
> **2. Drop total time derivatives.** $\frac i2(q_a\dot q_a + p_a\dot p_a) = \frac i4\frac{d}{dt}(q_a^2 + p_a^2)$ and $\frac12(p_a\dot q_a - q_a\dot p_a) = p_a\dot q_a - \frac12\frac{d}{dt}(q_ap_a)$. Total time derivatives in $L$ change neither the equations of motion ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]) nor anything else here, so the kinetic term is $\sum_ap_a\dot q_a$.
>
> **3. A phase-space action.** The rest of $\mathcal L$ is $-\psi^\dagger H_{\text{s.p.}}\psi$ up to a divergence ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]), a function of $q$, $p$ and their spatial derivatives. So $S = \int d^4x\,\bigl(\sum_ap_a\dot q_a - \mathcal H(q, p)\bigr)$ is a phase-space action of the form of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], with $(q_a, p_a)$ the canonical pairs and $\{q_a(\mathbf x), p_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]]).
>
> **4. Back to ψ.** By bilinearity, with $\{p_a, q_b\} = -\delta_{ab}\delta^3$ and $\{q, q\} = \{p, p\} = 0$: $\{\psi_a, \psi^{\ast}_b\} = \frac12\{q_a + ip_a, q_b - ip_b\} = \frac12\bigl(-i\{q_a, p_b\} + i\{p_a, q_b\}\bigr) = \frac12(-i - i)\delta_{ab}\delta^3 = -i\delta_{ab}\delta^3$, and $\{\psi_a, \psi_b\} = \frac12\bigl(i\{q_a, p_b\} + i\{p_a, q_b\}\bigr) = 0$. Part 3 again.
>
> **What this route shows**
> - The real and imaginary parts of each $\psi_a$ are a coordinate and its momentum: the Dirac field's phase space is $(\operatorname{Re}\psi, \operatorname{Im}\psi)$, and no constraint machinery is needed once $\mathcal L$ is written in these variables.
> - It needs commuting components (the split into real fields); the first route covers both parities.

^der-c5b-1-4b

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|★ Def. §C5b.1.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-3|★ Def. §C5b.1.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-4|★ Def. §C5b.1.4]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]], [[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-5|Derivation §C1b.4.5]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]

> [!theorem] ★ Theorem §C5b.1.5: The Symmetric Lagrangian Gives the Same Bracket
> Take the real symmetric density $\mathcal L_{\rm sym} = \mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$ of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-7|Theorem §C5a.3.7]], with $\psi$ and $\psi^\dagger$ as coordinates (as on slide 5; [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-2|Remark: ψ† or ψ̄ as the partner field]]), components of parity $\varepsilon$ and the bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]]:
> 1. The momenta are $\pi_{\psi,a} = \frac i2\psi^\dagger_a$ and $\pi_{\psi^\dagger,a} = -\frac i2(-1)^\varepsilon\psi_a$ ($-\frac i2\psi_a$ for commuting components).
> 2. The naive rule, $\{\psi_a, \pi_{\psi,b}\} = i\delta_{ab}\delta^3$ with this momentum, would give $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = 2\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, twice the value from $\mathcal L$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]).
> 3. The constraints $\phi_a = \pi_{\psi,a} - \frac i2\psi^\dagger_a \approx 0$, $\tilde\phi_a = \pi_{\psi^\dagger,a} + \frac i2(-1)^\varepsilon\psi_a \approx 0$ are second class with $\{\phi_a(\mathbf x), \tilde\phi_b(\mathbf y)\} = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, the same matrix as for $\mathcal L$ in these coordinates, and the Dirac bracket is again $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}_D = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]).
>
> The normalization of the canonical relations is fixed by the constraint analysis, not by reading $\pi$ off a particular $\mathcal L$: a total derivative in $\mathcal L$ moves the momenta but not the brackets.
>
> *Source: derived here; no course source computes the momenta of $\mathcal L_{\rm sym}$ (stated without derivation as a by-product in [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-8|Derivation §C5a.3.8]]). The symmetric density: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "Two further properties of the Dirac Lagrangian"); Yu §5.3, eqs. (5.97)–(5.99)*

^thm-c5b-1-5

> [!derivation]- Derivation
> **1. The velocity terms.** In $\mathcal L_{\rm sym} = \frac i2\bigl(\bar\psi\gamma^\mu\partial_\mu\psi - \partial_\mu\bar\psi\,\gamma^\mu\psi\bigr) - m\bar\psi\psi$ only the $\mu = 0$ terms contain velocities: $\frac i2\bigl(\bar\psi\gamma^0\dot\psi - \dot{\bar\psi}\gamma^0\psi\bigr)$. With $\bar\psi\gamma^0 = \psi^\dagger$ and $\dot{\bar\psi}\gamma^0 = \dot\psi^\dagger(\gamma^0)^2 = \dot\psi^\dagger$ this is $\frac i2\sum_a\bigl(\psi^\dagger_a\dot\psi_a - \dot\psi^\dagger_a\psi_a\bigr)$.
>
> **2. Momentum of ψ.** In $\psi^\dagger_a\dot\psi_a$ the velocity stands at the right end; the right derivative removes it: $\pi_{\psi,a} = \frac i2\psi^\dagger_a$.
>
> **3. Momentum of ψ†.** In $-\frac i2\dot\psi^\dagger_a\psi_a$ the velocity stands on the left. Moving it to the right end exchanges two factors of parity $\varepsilon$, a sign $(-1)^{\varepsilon\cdot\varepsilon} = (-1)^\varepsilon$: $-\frac i2\dot\psi^\dagger_a\psi_a = -\frac i2(-1)^\varepsilon\psi_a\dot\psi^\dagger_a$, so $\pi_{\psi^\dagger,a} = -\frac i2(-1)^\varepsilon\psi_a$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-4|★ Caution: Which side a Grassmann derivative acts from]]). For commuting components this is the $-\frac i2\psi$ of the by-product in Derivation §C5a.3.8. Part 1.
>
> **4. The naive normalization.** Insert $\pi_{\psi,b} = \frac i2\psi^\dagger_b$ into $\{\psi_a, \pi_{\psi,b}\} = i\delta_{ab}\delta^3$ by bilinearity, as in step 4 of [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-1|Derivation §C5b.1.1]]: $\frac i2\{\psi_a, \psi^\dagger_b\} = i\delta_{ab}\delta^3$, so $\{\psi_a, \psi^\dagger_b\} = 2\delta_{ab}\delta^3$: part 2. $\mathcal L$ and $\mathcal L_{\rm sym}$ have the same field equations (Theorem §C5a.3.7), so a rule whose answer depends on the choice between them cannot be the right one.
>
> **5. The constraint brackets.** Fundamental brackets as in step 2 of [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-4|Derivation §C5b.1.4]], with $\psi^\dagger$ in place of $\bar\psi$ and $\tilde\pi_a \equiv \pi_{\psi^\dagger,a}$: $\{\psi_a, \pi_b\} = \{\psi^\dagger_a, \tilde\pi_b\} = \delta_{ab}\delta^3$, $\{\pi_b, \psi_a\} = \{\tilde\pi_b, \psi^\dagger_a\} = -(-1)^\varepsilon\delta_{ab}\delta^3$, all others zero. Expanding into all four terms,
>
> $$
> \{\phi_a, \tilde\phi_b\} = \{\pi_a, \tilde\pi_b\} + \tfrac i2(-1)^\varepsilon\{\pi_a, \psi_b\} - \tfrac i2\{\psi^\dagger_a, \tilde\pi_b\} - \tfrac i2\cdot\tfrac i2(-1)^\varepsilon\{\psi^\dagger_a, \psi_b\} = 0 + \tfrac i2(-1)^\varepsilon\bigl(-(-1)^\varepsilon\bigr)\delta_{ab}\delta^3 - \tfrac i2\delta_{ab}\delta^3 - 0 = -i\delta_{ab}\delta^3 .
> $$
>
> The two halves, $-\frac i2$ each, come one from each momentum. In the other order, $\{\tilde\phi_b, \phi_a\} = -\frac i2\{\tilde\pi_b, \psi^\dagger_a\} + \frac i2(-1)^\varepsilon\{\psi_b, \pi_a\} = \frac i2(-1)^\varepsilon\delta_{ab}\delta^3 + \frac i2(-1)^\varepsilon\delta_{ab}\delta^3 = i(-1)^\varepsilon\delta_{ab}\delta^3$. And $\{\phi_a, \phi_b\} = 0$ ($\pi$ with $\pi$, $\pi$ with $\psi^\dagger$, $\psi^\dagger$ with $\psi^\dagger$: all zero), likewise $\{\tilde\phi_a, \tilde\phi_b\} = 0$. For $\mathcal L$ itself in the same coordinates, $\chi_a = \pi_a - i\psi^\dagger_a$, $\tilde\chi_a = \tilde\pi_a$, and $\{\chi_a, \tilde\chi_b\} = -i\{\psi^\dagger_a, \tilde\pi_b\} = -i\delta_{ab}\delta^3$: the same matrix.
>
> **6. Inverse.** As in step 5 of Derivation §C5b.1.4 with $X = -i\mathbb 1$, $Y = i(-1)^\varepsilon\mathbb 1$: $(C^{-1})^{\phi_a\tilde\phi_b} = -i(-1)^\varepsilon\delta_{ab}\delta^3$, $(C^{-1})^{\tilde\phi_b\phi_a} = i\delta_{ab}\delta^3$. Invertible: second class.
>
> **7. The Dirac bracket.** $\{\psi_a, \psi^\dagger_b\} = 0$ (two coordinates). $\{\psi_a, \phi_c\} = \{\psi_a, \pi_c\} = \delta_{ac}\delta^3$; $\{\psi_a, \tilde\phi_d\} = \{\psi_a, \tilde\pi_d\} + \frac i2(-1)^\varepsilon\{\psi_a, \psi_d\} = 0$; $\{\tilde\phi_d, \psi^\dagger_b\} = \{\tilde\pi_d, \psi^\dagger_b\} = -(-1)^\varepsilon\delta_{db}\delta^3$; $\{\phi_c, \psi^\dagger_b\} = \{\pi_c, \psi^\dagger_b\} - \frac i2\{\psi^\dagger_c, \psi^\dagger_b\} = 0$. Only the $(\phi_c, \tilde\phi_d)$ block contributes, and after the two delta integrations (as in step 7 of Derivation §C5b.1.4)
>
> $$
> \{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}_D = -\,\delta_{ac}\cdot\bigl(-i(-1)^\varepsilon\delta_{cd}\bigr)\cdot\bigl(-(-1)^\varepsilon\delta_{db}\bigr)\,\delta^3(\mathbf x - \mathbf y) = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y) :
> $$
>
> part 3, with the same parity cancellation $(-1)^{2\varepsilon} = 1$.
>
> **8. Why the bracket did not move.** $\mathcal L_{\rm sym} - \mathcal L = -\frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$; after $\int d^3x$ the spatial part is a surface term (zero for fields falling off at infinity) and the time part is $\frac{d}{dt}F$ with $F = -\frac i2\int d^3x\,\psi^\dagger\psi$. Adding $\dot F$ to $L$ shifts each momentum by the derivative of $F$ ($\partial F/\partial\psi_a = -\frac i2\psi^\dagger_a$: $i\psi^\dagger_a \to \frac i2\psi^\dagger_a$, step 2; $\partial^RF/\partial\psi^\dagger_a = -\frac i2(-1)^\varepsilon\psi_a$: $0 \to -\frac i2(-1)^\varepsilon\psi_a$, step 3) and moves the constraint surface accordingly, but leaves the constraint matrix (step 5) and therefore the Dirac bracket unchanged. ⚑ By-product: the canonical momentum depends on the total derivative chosen in $\mathcal L$, as the canonical $T^{\mu\nu}$ does ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-7|Derivation §C5a.3.7]], step 6); the bracket does not.
>
> **What the derivation shows**
> - Reading $\pi$ off a Lagrangian and imposing $\{\psi, \pi\} = i\delta$ is only safe when the momentum is an independent variable; for a first-order Lagrangian the coefficient depends on how $\mathcal L$ is written, and the Dirac bracket removes the dependence.
> - The course's $\mathcal L$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) happens to give the right coefficient directly, because its partner momentum vanishes: the naive rule and the Dirac bracket agree for it ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]], step 9).
> - Assumptions: fall-off at spatial infinity (step 8); right-derivative momenta.
> - Used next: [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]].

^der-c5b-1-5

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-7|Theorem §C5a.3.7]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|★ Def. §C5b.1.5]], [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-4|★ Caution: Which side a Grassmann derivative acts from]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]

## The postulate, and the theorem behind it

> [!principle] Principle §C5b.1.6: Equal-Time Canonical Anticommutation Relations
> The Dirac field is quantized by promoting the canonical pairs $(\psi_a, \pi_a = i\psi^\dagger_a)$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] to operators with, at equal times,
>
> $$
> \{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad \{\psi_a(\mathbf x), \psi_b(\mathbf y)\} = \{\psi^\dagger_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = 0 ,
> $$
>
> equivalently $\{\psi_a, \pi_b\} = i\delta_{ab}\delta^3$, and taking as Hamiltonian the $H$ of the model read as an operator. ($\{A, B\} \equiv AB + BA$.) This is **Jordan–Wigner** quantization, in place of the commutators of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]].
>
> *Domain:* fields of half-odd-integer spin (here the Dirac field), Schrödinger-picture operators or Heisenberg operators at a common time; integer-spin fields keep commutators. The relations are identities of operator-valued distributions ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]]). The operator ordering in $H$ is not fixed by the principle ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]). The choice is forced by positivity ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]) and by causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]).
>
> *Scalar analogue:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]].
> *Source: Lecture 10, slides 6 and 23 · the user's PHY 513 notes, Ch. 10 §10.4 (Principle "The equal-time anticommutators") · PS §3.5, eqs. (3.96), (3.102) · Yu §5.5.2, eqs. (5.238)–(5.239) · the user's pre-course notes, §5.5, eq. (car)*

^pr-c5b-1-6

> [!principle] Principle §C5b.1.7: The Spin–Statistics Theorem
> *Ingredients:* fields in a representation of spin $s$; a local quantum field theory (a Lagrangian with finitely many derivatives, fields multiplied only at the same point); Lorentz invariance, positive energies and positive norms; causal propagation (the commutator or anticommutator of the fields vanishes outside the light cone).
> *Claim:* a physical field of integer spin (a representation $(j_+, j_-)$ of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]] with $j_+ + j_-$ an integer) must be quantized with commutation relations ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]) and describes bosons; a physical field of half-odd-integer spin must be quantized with anticommutation relations ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]) and describes fermions ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]). Causality is microcausality of observables ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
>
> *Layer:* stated, not proved, in this course (Lecture 10: "The proof is complicated"); the free fields of the course are checked in [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]].
> *Source: Lecture 10, slide 7 · the user's PHY 513 notes, Ch. 10 §10.2 (Principle "The spin–statistics theorem") · Yu §5.5.4 (boxed statement, after eq. (5.293)) · PS §3.5, pp. 57–58 (Pauli 1940; Streater & Wightman, cited there) · the user's pre-course notes, §5.5, Theorem "Spin–statistics theorem"*

^pr-c5b-1-7

> [!derivation]+ Derivation (to be filled: every spin)
> *Status:* the proof for every spin (that integer-spin fields *cannot* be quantized with anticommutators, and the general half-integer case) rests on the Lorentz invariance of the two-point functions and causality at spacelike separation. It is not given in the sources used here (Yu points to further reading for proofs via exchange paths, Lorentz invariance of the S-matrix and causality; PS cite Pauli 1940 and Streater–Wightman). To be filled. The key structural point, as Lecture 10 gave it: for half-integer spin the equations of motion are linear in time derivatives, not second order, so the canonical momentum is proportional to the field itself, $\pi \sim \psi^\dagger$, rather than to its time derivative, $\pi \sim \dot\phi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-3|Remark: A first-order system: the momentum is ψ† itself]]). Higher spins follow the same pattern: integer spins are quantized like scalars with indices, half-integer spins ($\frac12$, $\frac32$, …) with anticommutators.

> [!remark] Remark: Spin and statistics are an output
> In nonrelativistic quantum mechanics the exclusion principle is an extra postulate: one is told, or shown by spectroscopy, that two electrons cannot occupy the same state ([[§A5.3 The Exclusion Principle and the Periodic Table#^pr-a5-3-2|QM Principle §A5.3.2]]; for identical particles in general, [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]). In relativistic quantum field theory it is not negotiable. A spin-½ field cannot be quantized consistently, with a bounded Hamiltonian and causal propagation, without anticommutators ([[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]]), and anticommutators give the exclusion principle ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]). Without any knowledge of atomic spectra one would have to invent it (Lecture 10: "It's an output, not an input"). Photons, by contrast, are bosons, which is why many of them can occupy one mode, as in a laser.
>
> *Source: Lecture 10 (transcript, end of the lecture) · the user's PHY 513 notes, Ch. 10 §10.2 ("Spin and statistics are an output")*

^rem-c5b-1-6

## Smeared Dirac fields

> [!definition] Definition §C5b.1.6: Smeared Dirac Field on a Time Slice
> For $f \in \mathcal S(\mathbb R^3, \mathbb C^4)$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], componentwise), the **smeared Dirac field** and its adjoint on a time slice are
>
> $$
> \psi(f) = \int d^3x\;f(\mathbf x)^\dagger\psi(\mathbf x) = \sum_a\int d^3x\;\overline{f_a(\mathbf x)}\,\psi_a(\mathbf x), \qquad \psi^\dagger(f) \equiv \psi(f)^\dagger = \int d^3x\;\psi^\dagger(\mathbf x)f(\mathbf x) ;
> $$
>
> $\psi(f)$ is antilinear and $\psi^\dagger(f)$ linear in $f$, and $\langle f, g\rangle \equiv \int d^3x\,f^\dagger g$ is the $L^2(\mathbb R^3, \mathbb C^4)$ product. As for the scalar ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]), $\psi(\mathbf x)$ is the kernel of these operators, an operator-valued distribution ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 and App. A §A.4 (smeared operators, for the scalar) · written here for the Dirac field*

^def-c5b-1-6

> [!theorem] Theorem §C5b.1.8: The Anticommutators Are Identities after Smearing; Smeared Fermi Fields Are Bounded
> For $f, g \in \mathcal S(\mathbb R^3, \mathbb C^4)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-6|Def. §C5b.1.6]]):
> 1. [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] means $\{\psi(f), \psi^\dagger(g)\} = \langle f, g\rangle$ and $\{\psi(f), \psi(g)\} = 0$.
> 2. $\psi(f)^2 = 0$, and $\|\psi(f)\| = \|\psi^\dagger(f)\| = \|f\|_{L^2}$: the smeared field is a **bounded** operator, and extends by continuity to every $f \in L^2(\mathbb R^3, \mathbb C^4)$.
> 3. The field at a point is still not an operator: it would need $\|f\|_{L^2} = \infty$ ($f \to \delta$), and $\{\psi_a(\mathbf x), \psi^\dagger_a(\mathbf x)\} = \delta^3(\mathbf 0)$ has no value.
>
> Bosonic smeared fields are unbounded ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], Step 4: each pair with $\int fg = 1$ is a canonical pair $[Q, P] = i$, which has no bounded solutions).
>
> *Source: stated and derived here (standard: Bratteli & Robinson, Operator Algebras and Quantum Statistical Mechanics 2, §5.2.2) · the user's PHY 513 notes, App. A §A.4 (smeared operators)*

^thm-c5b-1-8

> [!derivation]- Derivation
> **1. Part 1.** Exactly Steps 1–3 of [[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-3|Derivation §C2a.1.3]] with the anticommutator in place of the commutator (it is bilinear too): pairing $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}$ with $\overline{f_a(\mathbf x)}g_b(\mathbf y)$ gives $\{\psi(f), \psi^\dagger(g)\}$ on the left and $\sum_a\int d^3x\,\overline{f_a}g_a = \langle f, g\rangle$ on the right, the kernel $\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ acting as in Step 2 there ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], change of variables with Jacobian $1$). The other relation has kernel $0$.
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

^der-c5b-1-8

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-6|Def. §C5b.1.6]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-2|P1, step 2]]

## The field momentum as the generator of translations

> [!theorem] Theorem §C5b.1.9: The Field Momentum Generates Translations of ψ
> Let $\mathbf P = \int d^3y\,\psi^\dagger(-i\nabla)\psi$ be the field momentum of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] (classically [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]]), read as an operator in the order written. The equal-time anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] give
>
> $$
> [\psi_a(\mathbf x), \mathbf P] = -i\nabla\psi_a(\mathbf x), \qquad [\psi^\dagger_a(\mathbf x), \mathbf P] = -i\nabla\psi^\dagger_a(\mathbf x),
> $$
>
> commutators although the fields anticommute, because $\mathbf P$ is bilinear. These are the space components of the translation law $[\Phi_a(x), P^\mu] = i\partial^\mu\Phi_a(x)$ of [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]]: the Noether momentum of the Dirac field is the generator of space translations. The time component is the Heisenberg equation, [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]].
>
> *Scalar analogue:* [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]], Steps 1 and 3.
> *Source: the general law: the user's PHY 513 notes, Ch. 7 §7.6, eq. (PPhi); Yu §3.2, eqs. (3.80)–(3.86) · for the Dirac field computed here, as Theorem §C3.5.13 does for the scalar*

^thm-c5b-1-9

> [!derivation]- Derivation
> All fields at one time $t$; unprimed fields at $\mathbf x$, primed at $\mathbf y$; $P^k = -i\int d^3y\,\psi'^\dagger_b\,\partial'_k\psi'_b$ (summed over $b$), with $\partial'_k = \partial/\partial y^k$.
>
> **1. Commutator with a bilinear.** For any operators, $[A, BC] = \{A, B\}C - B\{A, C\}$: expanding the right side, $ABC + BAC - BAC - BCA = ABC - BCA$ ([[§C5b.6 The Heisenberg Dirac Field#^der-c5b-6-2|Derivation §C5b.6.2]], step 1).
>
> **2. ψ with the density.** With $A = \psi_a$, $B = \psi'^\dagger_b$, $C = \partial'_k\psi'_b$: $\{\psi_a, \psi'^\dagger_b\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, and $\{\psi_a, \partial'_k\psi'_b\} = \partial'_k\{\psi_a, \psi'_b\} = 0$, since $\{\psi_a(\mathbf x), \psi_b(\mathbf y)\} = 0$ for all $\mathbf y$ and so has zero $\mathbf y$-derivative. So $[\psi_a, \psi'^\dagger_b\partial'_k\psi'_b] = \delta_{ab}\delta^3(\mathbf x - \mathbf y)\,\partial'_k\psi'_b$.
>
> **3. Integrate.** Multiply by $-i$, sum over $b$ and integrate over $\mathbf y$; the delta sets $\mathbf y = \mathbf x$ and $b = a$ (*sense:* after smearing in $\mathbf x$, the pairing of $\delta^3$ with the operator-valued distribution $\partial_k\psi_a$, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]): $[\psi_a(\mathbf x), P^k] = -i\,\partial_k\psi_a(\mathbf x)$, i.e. $[\psi_a, \mathbf P] = -i\nabla\psi_a$.
>
> **4. ψ† with the density.** Now $A = \psi^\dagger_a$: $\{\psi^\dagger_a, \psi'^\dagger_b\} = 0$, and $\{\psi^\dagger_a(\mathbf x), \partial'_k\psi'_b(\mathbf y)\} = \partial'_k\bigl(\delta_{ab}\delta^3(\mathbf x - \mathbf y)\bigr)$. So $[\psi^\dagger_a, P^k] = -i\int d^3y\,\bigl(0 - \psi'^\dagger_b\,\partial'_k\delta_{ab}\delta^3(\mathbf x - \mathbf y)\bigr) = i\int d^3y\,\psi^\dagger_a(\mathbf y)\,\partial'_k\delta^3(\mathbf x - \mathbf y)$. Integrate by parts in $\mathbf y$, the distributional derivative ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]; no boundary term after smearing): $= -i\int d^3y\,\partial'_k\psi^\dagger_a(\mathbf y)\,\delta^3(\mathbf x - \mathbf y) = -i\,\partial_k\psi^\dagger_a(\mathbf x)$. It is also the adjoint of step 3: $[\psi_a, P^k]^\dagger = [P^k, \psi^\dagger_a]$ for Hermitian $P^k$, and $(-i\partial_k\psi_a)^\dagger = i\partial_k\psi^\dagger_a$.
>
> **5. The translation law.** $\partial^k = -\partial_k$, so step 3 reads $[\psi_a, P^k] = i\partial^k\psi_a$: the $\mu = k$ components of [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]] with the index of $\psi$ untouched ($D = \mathbb 1$ for translations). To first order in $\mathbf a$, $e^{i\mathbf a\cdot\mathbf P}\psi(\mathbf x)e^{-i\mathbf a\cdot\mathbf P} = \psi + i a^k[P^k, \psi] = \psi - a^k\partial_k\psi = \psi(\mathbf x - \mathbf a)$.
>
> ⚑ By-product: with commutators, $[A, BC] = [A, B]C + B[A, C]$ and the provisional relations ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]]) give the same result; like the field equation, the translation law does not choose the statistics → [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|§C5b.6, Remark: The field equation does not choose the statistics]]. ⚑ By-product: reordering $\mathbf P$ changes it by at most a c-number, which drops out of every commutator; the mode form needs no reordering at all ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]]).
>
> **What the derivation shows**
> - The classical Noether momentum, quantized with anticommutators, is the generator of space translations of the quantum field, as [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]] requires of a relativistic field theory; the statistics enter only through a sign that cancels in a bilinear.
> - Assumptions: equal times; smearing in $\mathbf x$ to evaluate the delta and its derivative.
> - Used next: the momentum of one-particle states ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], the mode form of the same statement).

^der-c5b-1-9

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.6 The Heisenberg Dirac Field#^der-c5b-6-2|Derivation §C5b.6.2]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!remark]- Connections
> - The classical Dirac field is not re-derived here: its Lagrangian, momenta, Hamiltonian density and Noether momentum live in Chapter C5a and are embedded at the top; quantization adds operators, an ordering and the anticommutators, and the Noether momentum becomes the generator of translations, as the scalar's does — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]].
> - The puzzle of [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|Caution: The provisional commutator quantization]] is the quantum face of a classical fact: a Lagrangian of first order in time has momenta that are functions of the coordinates, so phase space is half as large and the canonical pairs are $(\psi, \psi^\dagger)$ — [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]].
> - The scalar's conjugate momentum is a velocity, an independent field next to $\phi$; the Dirac field's is $i\psi^\dagger$, so the spinor version of the canonical postulate pairs a field with its own adjoint, and the three warnings about what a conjugate momentum is apply with a fourth (it is not $\bar\psi$) — [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]], [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-5|Remark: What the conjugate momentum is not, for spinors]].
> - Hamilton's equations for fields (one pair per component, the bracket generating time evolution) carry over to the first-order Dirac Lagrangian once the momentum is read as $i\psi^\dagger$; they return the Dirac equation and its adjoint, and their operator form is the Heisenberg equation — [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]].
> - The Lagrangian and its momenta are classical results of Chapter C5a; the real symmetric form $\mathcal L_{\rm sym}$ differs by a divergence, changes the momenta to $\pm\frac i2$ times the fields, and leaves the Dirac bracket unchanged — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-7|Theorem §C5a.3.7]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-5|★ Theorem §C5b.1.5]].
> - The vector field meets constraints too: $\pi^0 = 0$ is a primary constraint that needs Gauss's law as a secondary one, second class for the Proca field and first class (gauge) for Maxwell; the Dirac field's constraints are second class at once, with no secondary constraint and no gauge freedom — [[§C4.2★ The Proca Field#^rem-c4-2-4|§C4.2★, ★ Remark: Second-class constraints, and why Maxwell differs]], [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]; the Proca field's Dirac bracket shows up as $[A^0, A^j] \ne 0$ — [[§C4.4★ Quantizing the Massive Vector Field#^thm-c4-4-2|Theorem §C4.4.2]].
> - $\psi$ is to the Dirac field what $a$ is to the oscillator, a complex combination of a coordinate and its momentum, which is why a relation between $\psi$ and $\psi^\dagger$ can be canonical — [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|§C2a.1, Remark: The oscillator, recalled]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-4|Remark: Larsen's puzzle]].
> - The anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] have the form of the fermionic field relations of nonrelativistic second quantization; the relativistic field adds two species in one local field, spinors, and a statistics that is forced rather than chosen — [[§C12.2★ Second Quantization#^thm-c12-2-3|QM Theorem §C12.2.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-6|§C5b.2, Remark: What the field adds to the anticommutators of second quantization]].
> - Microcausality for fermions is an anticommutator statement, and the Feynman propagator of the Dirac field carries the fermionic sign of time ordering — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]; the spin–statistics theorem ties the anticommutators of this section to spin ½, the representations with the sign $-1$ under a $2\pi$ rotation — [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - The anticommutators make smeared fermion fields bounded ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]]), so the distributional care needed in this chapter is only for point values and coincident labels: the plane-wave delta in $\mathcal S'$, the split exponentials for wave packets, relabelling with Jacobian 1, evaluation of smooth prefactors on the support of δ, the box for δ³(0), integration by parts with fall-off — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]; for the scalar the smeared fields are unbounded and the canonical relations are identities of unbounded operators — [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]].
> - Quantum Mechanics lists the proof of the spin–statistics connection as deferred to field theory; this course states the theorem and checks it on its two free fields — [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]], [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]].
