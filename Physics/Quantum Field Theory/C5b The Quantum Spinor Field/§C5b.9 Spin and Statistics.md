---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.8 Green's Functions and the Dirac Feynman Propagator]] · ↑ [[· C5b The Quantum Spinor Field]]

*Sources: the user's PHY 513 notes, Ch. 10 §10.2 and §10.7 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), slides 6–7 and 23, transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 52–58 · Yu Zhao-Huan, 量子场论讲义, §§5.4.3–5.5.4 · the user's pre-course notes, §5.5.*

The chapter closes where Lecture 10 began, with spin and statistics. The theorem was stated as a principle in [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]], without proof; the course's two free fields can now be checked against it, the Dirac field for two independent reasons: positivity of energy and norms ([[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]]) and causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]]). The scalar side of the comparison is [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] and [[§C2b.4 Microcausality and the Commutator Function|§C2b.4]]. Two remarks then gather the lecture's summary and the correspondence with Yu and Peskin–Schroeder. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

> [!theorem] Theorem §C5b.9.1: The Free Fields of the Course Obey the Spin–Statistics Theorem
> 1. The free Dirac field (spin ½) admits no quantization with commutators that has positive norms and an energy bounded below ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]), nor one that propagates causally ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]); with anticommutators it has positive energies and norms ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]) and commuting observables at spacelike separation ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]]).
> 2. The free scalar field (spin 0) quantized with commutators has positive energies and norms and is microcausal ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]).
>
> Both therefore obey [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]]; its quanta are fermions and bosons respectively ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]).
>
> *Source: Lecture 10, slides 6–7 · the user's PHY 513 notes, Ch. 10 §§10.1–10.2, 10.4 · PS §3.5, pp. 54–58 · Yu §5.5.1, §5.5.4 · the user's pre-course notes, §5.5*

^thm-c5b-9-1

> [!derivation]- Derivation
> **1. Spin ½, from positivity.** With commutators the Dirac field has negative norms or an energy unbounded below ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]); with anticommutators the energy is positive and norms are positive ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]).
>
> **2. Spin ½, from causality.** Under the assumptions of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]] only the anticommutator can vanish outside the light cone, and with it the observables commute ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]]).
>
> **3. Spin 0.** With commutators the scalar field has positive energy and norms ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]) and is microcausal ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]); there the commutators were an input ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]).
>
> **4. The general theorem.** Not covered by Steps 1–3: see the placeholder under [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]].
>
> **What the derivation shows**
> - The two free instances of the course both obey the theorem, the Dirac field for two independent reasons (energy and causality).
> - Assumptions used: those of Theorem §C5b.7.5 (translation and rotation invariance of the vacuum, positive norms, Lorentz invariance of the two-point functions) and a Fock vacuum for Theorem §C5b.3.3.

^der-c5b-9-1

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]

> [!remark] Remark: Two arguments, one answer
> Peskin–Schroeder reach anticommutators twice: once from causality, by requiring that $\langle0|\psi\bar\psi|0\rangle$ and $\langle0|\bar\psi\psi|0\rangle$ cancel outside the cone ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]), and once from positivity of the energy ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]). That two unrelated requirements select the same quantization is the content of the spin–statistics connection. It changes layer relative to Quantum Mechanics, where Fermi statistics of half-integer-spin particles is a postulate ([[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]): here it is derived for the Dirac field, and the half-integer representations it applies to are exactly those with the sign $-1$ under a $2\pi$ rotation ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations|§C3.2]]; [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]).
>
> *Source: PS §3.5, pp. 56–58 · Yu §5.5.4 ("可以从多个角度证明")*

^rem-c5b-9-1

> [!remark] Remark: Lecture 10 in one statement
> The lecture's summary slide: the mode expansion ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]), with oscillators obeying $\{a^r_{\mathbf p}, a^{s\dagger}_{\mathbf q}\} = \{b^r_{\mathbf p}, b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^3(\mathbf p - \mathbf q)\delta^{rs}$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]), satisfies the equal-time anticommutation relation $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]), is causal ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]]), and diagonalizes the Hamiltonian with all energies positive after normal ordering, $:\!H\!: = \int\frac{d^3p}{(2\pi)^3}\sum_sE_{\mathbf p}(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} + b^{s\dagger}_{\mathbf p}b^s_{\mathbf p})$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]). Its quanta are spin-½ particles and antiparticles ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|Theorem §C5b.4.4]]) obeying Fermi–Dirac statistics ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]).
>
> *Source: Lecture 10, slide 23 · the user's PHY 513 notes, Ch. 10 §10.7 (Principle "The quantum Dirac field")*

^rem-c5b-9-2

> [!remark] Remark: The same steps in Yu and Peskin–Schroeder
> Yu §5.4.3–§5.5 covers the ground of this chapter with the helicity basis in place of $s = 1, 2$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-1|§C5b.1, Caution: Names for the Dirac field and its mode operators across sources]]). His mode expansion and conjugates are eqs. (5.216)–(5.218) ([[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]), the momentum (5.219), with the remark (5.220) that $\psi^\dagger$ is not an extra canonical variable. His §5.5.1 is the commutator attempt that Peskin–Schroeder also make: the commutators (5.228) give $[b, b^\dagger] = -(2\pi)^3\delta^3$ (5.236) and a Hamiltonian with negative antiparticle energies (5.237) ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]). §5.5.2 switches to the anticommutators (5.238)–(5.239), derives the oscillator algebra (5.240)–(5.246) in the direction fields ⇒ oscillators (the first derivation under [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]; the lecture went the other way), and finds the Hamiltonian as (5.247), with the same negative zero-point term ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]). The ladder relations are (5.248)–(5.251) ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]), the many-particle states and the exclusion principle (5.289)–(5.295) ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]), and the spin–statistics theorem is stated after (5.293), with the remark that it can be proved from positivity of the energy (as here), from the path dependence of exchanging identical particles, from Lorentz invariance of the S-matrix, or from causality. Peskin–Schroeder §3.5 does the commutator attempt on pp. 52–56 (eqs. (3.86)–(3.96)) and gives the cleaned-up results from eq. (3.99) on ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-1|§C5b.1, Remark: Lecture 10's route, and how to read Peskin–Schroeder §3.5]]). Recommended reading in the user's notes: PS §3.5, read linearly; Yu §5.5; Tong, Chapter 5.
>
> *Source: the user's PHY 513 notes, Ch. 10 §10.7 ("Correspondence with Yu") and Concordance ("Where Yu's results appear")*

^rem-c5b-9-3

> [!remark]- Connections
> - The principle that QM had to postulate per species becomes, for the free Dirac field, a consequence of positivity and causality; the half-integer representations it applies to are exactly those with the sign $-1$ under a $2\pi$ rotation — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations|§C3.2]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - The two failures of commutators are the two halves of one structure: the antiparticle term of every bilinear carries the sign of $\sum v\bar v = \slashed{p} - m$, which shows up in the energy as $-E_{\mathbf p}$ and in the two-point function as $-(i\slashed{\partial} + m)D_W(-\xi)$ — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|§C5b.3, Remark: Two minus signs make a plus]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]].
> - Fermi–Dirac statistics of the quanta is what gives degenerate Fermi gases, the periodic table and the stability of matter their structure — [[§A5.3 The Exclusion Principle and the Periodic Table#^pr-a5-3-2|QM Principle §A5.3.2]], [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions|TH §B10.1]].
> - The vector field (spin 1) must take commutators, and its covariant quantization meets negative norms of a different origin, removed by a gauge condition rather than by statistics — [[§C4.6 Covariant Quantization and the Indefinite Metric|§C4.6]], [[§C4.7 The Gupta–Bleuler Condition and Physical Photons|§C4.7]].
> - The path integral for fermions reproduces the anticommutators with Grassmann variables (PHY 513 Lecture 26) — QFT C11 (planned).
