---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
tags: [chapter, quantum-field-theory]
---
# C8b Spin, Helicity and Chirality
← [[· C8a Quantum Electrodynamics]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (31), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (10), [[· C3 Poincaré Symmetry and Covariant Fields|C3 Poincaré Symmetry and Covariant Fields]] (94), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (98), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (120), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (6), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (10), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (6), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (23), [[· C8a Quantum Electrodynamics|C8a Quantum Electrodynamics]] (105), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (18), [[· CA Mathematical Methods|CA Mathematical Methods]] (10), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (20)
**Used by:** [[· C1a Preliminaries|C1a Preliminaries]] (4), [[· C3 Poincaré Symmetry and Covariant Fields|C3 Poincaré Symmetry and Covariant Fields]] (8), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (50), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (14), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (16), [[· C8a Quantum Electrodynamics|C8a Quantum Electrodynamics]] (8), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (4), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (12)

C8b builds the labels of spin for a moving particle, helicity and chirality, and then follows $e^+e^- \to \mu^+\mu^-$ helicity by helicity (Lecture 20, "Helicity Structure", 16 Nov 2026; PS §5.2; the user's notes, Lecture 20 update). Before this chapter no process in the notes followed a spin: scalar particles have none, and for fermions the spins were summed and averaged, or carried unchanged through a nonrelativistic limit ([[§C8b.1 Why Spin Must Now Be Tracked|§C8b.1]]). To fix the spins in a process one needs a label on which all observers agree. The chapter introduces the structures behind such a label formally and in logical order, starting from the new concepts (user decision 2026-11-18): what was done so far, the question "what is the spin of a moving particle?" and the plan (§C8b.1); a particle as an irreducible unitary representation, the standard momentum, the little group and the Wigner rotation, the spin of a massive particle and the Pauli–Lubanski vector (§C8b.2); the little group $ISO(2)$ of a massless particle, the exclusion of continuous spin, helicity with its definition, its invariance for massless and its frame dependence for massive particles, its quantization, the parity pairs, and polarization vectors with the origin of gauge invariance (§C8b.3); chirality, the label of a field component, and the two labels side by side (§C8b.4); the helicity spinors of Problem Set 5 and the massless limit, where helicity becomes chirality (§C8b.5). Then the lecture proper: the projected spinors, the projectors selecting helicity at high energy with the reversal for antiparticles, $\gamma^0\gamma^\mu$ block diagonal and helicity conservation at the QED vertex, $e^-_R$ annihilating only with $e^+_L$ into $J_z = \pm1$, the chiral fields at high energy, and, added after Problem Set 11 was submitted, the rule for any vertex: a bilinear with an even number of $\gamma$'s joins opposite chiralities and one with an odd number equal ones, so that the mass term $-m(\overline{\psi_R}\psi_L + \overline{\psi_L}\psi_R)$ couples the two chiralities and a scalar vertex flips the helicity, with the selection rules for $u$ and $v$ spinors at high energy (§C8b.6); the projected amplitude, the conjugate and the spin sum with projectors, the traces with $\gamma^5$, $|\mathcal M|^2 = \frac{16e^4}{q^4}(p\cdot k')(p'\cdot k)$, the polarized cross sections $\frac{\alpha^2}{4E_{\rm cm}^2}(1 \pm \cos\theta)^2$ and their average, the zeros from angular momentum, and the amplitude with explicit helicity spinors as the overlap of a circular polarization vector with its rotated image (§C8b.7); the steps are [[P9 Helicity Amplitudes]]. With both masses kept, Yu's sixteen amplitudes, their mass suppressions, angular zeros and sum are ★ §C8b.8. The helicity of photons and of massive vector quanta follows, because the fermion story does not need it (§C8b.9, draft). The chapter closes with the one process of the course in which the helicities of an electron and of photons act together, backward Compton scattering at high energy (Lecture 22): angular momentum forbids the helicity-conserving amplitude exactly backward, which weakens the peak of the cross section from $1/\chi^4$ to $1/\chi^2$ and fixes the polarization of the photons of inverse Compton scattering (§C8b.10). Two sections from Problem Set 11, in the user's solution, apply the tools to fermion–fermion scattering: with a scalar exchanged every vertex flips the helicity, six of the sixteen helicity amplitudes survive at high energy and they are the constants $2g^2$ and $-g^2$, with spin average $3g^4$ (§C8b.11); with a photon exchanged the vertex at equal momenta is $2p^\mu\delta_{\lambda\lambda'}$, and the amplitudes in which each electron keeps its helicity dominate near the forward and the backward direction (§C8b.12).

**Lectured and not lectured.** Lectured in PHY 513: the definition of helicity and its dependence on the frame (Lecture 20, slides 9, 11, 24; in §C8b.3); chirality and its projectors (Lectures 7–8 and Problem Set 5; home [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], quoted in §C8b.4, whose comparison answers a question asked in Lecture 20); the helicity spinors (Problem Set 5, Problem 6; Lecture 20, slides 24–25; §C8b.5); the vertex and the polarized cross sections (Lecture 20; §C8b.6, §C8b.7). Not lectured, and starred box by box: the general layer of §C8b.4 added on 2026-11-20 at the user's request (chirality of any field, the helicity $j_- - j_+$ a massless field carries, the field strength as a mirror pair), with the comparison of the polarization bases and the spinor-against-vector table in §C8b.9. Not lectured: the little-group construction of §C8b.2 and the proofs of §C8b.3, which are the formal foundation, from Yu §3.3, the supplement of the user's PHY 513 notes (Ch. 7 §7.7) and the user's pre-course notes; they were the starred sections §C3.6★ and §C3.7★ until 2026-11-18 and stand here without a star because the spin-resolved processes rest on them (user decision). ★ §C8b.8 (Yu §8.2.4, masses kept) is beyond the lecture. §C8b.9 is a draft, written ahead of Lecture 25 in Yu's notation; its Proca and Noether-spin boxes are ★. §C8b.10 is lectured (Lecture 22, slides 28–31), except its ★ theorem, which quotes Yu's helicity amplitudes. The closing part of §C8b.6 was held back until Problem Set 11 was submitted and is unstarred: Lecture 20 states that without the $\gamma$ of the vertex the helicity flip is mandatory, the user's notes add the rule for an even or odd number of $\gamma$'s, and Problem 1(a) derives the selection rule; Yu's selection rules for the bilinears are quoted with it. §C8b.11 and §C8b.12 are Problem Set 11, Problems 1 and 2, as the user solved them. The remark in ★ §C8b.8 on a mass flipping a helicity is Yu's. The one fact about stabilizers that earlier chapters use is [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]]; starred boxes of C4 and C5b that rest on the little group point forward to §C8b.2.

## How C8b relates to Yu and PS
Yu treats the one-particle states and the little group in §3.3 (massive particles §3.3.1, massless particles and helicity §3.3.2), the helicity spinors in §5.4.2, the polarized amplitudes of $e^+e^- \to \mu^+\mu^-$ with both masses in §8.2.4 and chirality in §8.3, and the helicity of vector quanta in §4.3–§4.4. PS §5.2 does the projector-and-trace route and the explicit spinors for massless fermions; PS has no little-group construction. The sections were written for C3, C4, C5a and C8 and collected in C8 as §C8.12–§C8.17★ on 2026-11-16; the chapter was formed on 2026-11-18.

| Section | Lecture, slides | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|---|
| §C8b.1 | 20 (the question behind the lecture) | — | — | §5.2, p. 141 |
| §C8b.2 | — (not lectured) | §3.3, (3.87)–(3.109); §3.3.1, (3.110)–(3.177) | one-particle states as representations; standard momentum, little group; massive particles and spin; Pauli–Lubanski vector | — |
| §C8b.3 | 20: slides 9, 11, 24 | §3.3.1, (3.175)–(3.177); §3.3.2, (3.178)–(3.218) | the massless little group $ISO(2)$, continuous spin; helicity of states; invariance and quantization for massless particles; Pauli–Lubanski vector; parity pairs | §5.2, p. 141 |
| §C8b.4 | 20: slides 8, 9, 11, 24; 7–8 (the Weyl halves) | §5.1, (5.36); §8.3, (8.159)–(8.168), (8.174)–(8.189) | $\gamma^5$ a Lorentz scalar; chirality projectors and projected fields; helicity and chirality at high energy; (beyond Yu) chirality of any field, the rule helicity $= j_- - j_+$ for massless fields, the vector potential and $\mathbf E \pm i\mathbf B$, the Maxwell Lagrangian in these variables | §3.4, pp. 50–51, (3.68)–(3.72) |
| §C8b.5 | 20: slides 24–25 | §5.4.2, (5.158)–(5.199); §8.2.4, (8.100)–(8.107); §8.3, (8.174)–(8.178) | helicity two-spinors and helicity spinors $u_\lambda$, $v_\lambda$; massless limit; comparison with the fixed-axis basis | §3.3, (3.52)–(3.54) |
| §C8b.6 | 20: slides 3–11, 26–27; Problem Set 11, Problem 1(a) | §8.2.4, (8.108), (8.143)–(8.157); §8.3, (8.159)–(8.199) | chirality projectors; chiral decomposition of the bilinears with zero to three $\gamma$'s and the mass term; helicity equals chirality at high energy, reversed for $v$; selection rules for the bilinears at high energy; mass-suppressed helicity amplitudes | §5.2, pp. 141–142, (5.17)–(5.18), p. 145 |
| §C8b.7 | 20: slides 14–20, 23–28 | §8.2.4, (8.99)–(8.142), (8.158) | polarized amplitudes with explicit helicity spinors and both masses; currents (8.118), (8.132)–(8.135); $\mp e^2(1 \pm \cos\theta)$; parity; the sum of sixteen | §5.2, pp. 142–146, (5.17)–(5.32), Figure 5.4 |
| §C8b.8★ | — | §8.2.4, (8.99), (8.108)–(8.158), Figures 8.4–8.6 | massive helicity spinors, currents and all sixteen amplitudes with masses; a mass flipping a helicity as the reason for the suppression; parity phases; the sum | — |
| §C8b.9 | 18: slides 9, 13; 20: slide 28 | §4.3.1, (4.103)–(4.121); §4.4.4, (4.267)–(4.280) | helicity vectors and states of the Proca field; photon helicity modes, helicity ±1, Noether spin; linear against helicity polarization vectors; spinor and vector side by side | §9.4, p. 298 |
| §C8b.10 | 22: slides 28–31 | §8.6.3, (8.412)–(8.415), (8.439)–(8.457) | the two channels with explicit helicity spinors; $\mathcal M_s$ and $\mathcal M_u$ for the helicity configurations; the factor $\cos\frac\theta2$ that weakens the singularity at $\theta = \pi$ | §5.5, pp. 165–167, (5.97)–(5.104), Figure 5.6 |
| §C8b.11 | Problem Set 11, Problem 1(b)–(g) | — (the amplitude: §7.1.2, (7.82); the bilinears without a $\gamma$: §8.3, (8.190)–(8.192)) | — | §4.7, (4.118)–(4.119) |
| §C8b.12 | Problem Set 11, Problem 2 | — | — | — (the Gordon identity: Problem 3.2) |

## Sections
- [[§C8b.1 Why Spin Must Now Be Tracked]] — PHY 513 Lecture 20; PS 5.2, p. 141; 513 notes, Lecture 20 update
- [[§C8b.2 Particle States and the Little Group]] — Yu 3.3, 3.3.1; 513 notes Ch. 7
- [[§C8b.3 Massless Particles and Helicity]] — PHY 513 Lecture 20, slides 9, 11, 24; Yu 3.3.1–3.3.2; 513 notes Ch. 7 §7.7
- [[§C8b.4 Chirality]] — PHY 513 Lecture 20, slides 8, 9, 11, 24; PS 3.4; Yu 5.1, 8.3
- [[§C8b.5 Helicity Spinors and the Massless Limit]] — PS 3.3; Yu 5.4.2, 8.2.4, 8.3; 513 notes Ch. 9; PS5 P6; Lecture 20 (moved from §C5a.13, 2026-11-16)
- [[§C8b.6 Helicity Conservation at the QED Vertex]] — PHY 513 Lecture 20 (16 Nov 2026), slides 3–11; 513 notes Lecture 20 update §20.1–20.2; PS §5.2, pp. 141–142, 145; Yu §8.3, (8.159)–(8.168), (8.174)–(8.189)
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production]] — PHY 513 Lecture 20 (16 Nov 2026), slides 14–28; 513 notes Lecture 20 update §20.3–20.6; PS §5.2, pp. 142–146, (5.17)–(5.32); Yu §8.2.4
- [[§C8b.8★ Polarized Amplitudes with Masses]] — Yu §8.2.4, (8.99), (8.108)–(8.158), Figures 8.4–8.6
- [[§C8b.9 Photon Helicity]] — Yu §4.3.1, §4.4.4; PS §9.4; Lecture 18 (moved from §C4.3★/§C4.5★/§C4.10, 2026-11-16)
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering]] — PHY 513 Lecture 22 (23 Nov 2026), slides 28–31; 513 notes, Lecture 22 update, §22.3 (Helicity suppression); PS §5.5, pp. 165–167, (5.97)–(5.104); Yu §8.6.3
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory]] — PHY 513 Problem Set 11, Problem 1(b)–(g) (the user's solution, submitted Nov 2026); PS §4.7, (4.119); Problem Set 5, Problem 6
- [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering]] — PHY 513 Problem Set 11, Problem 2 (the user's solution, submitted Nov 2026); the Gordon identity (Problem Set 5, Problem 3)

## Principles
- [[§C8b.2 Particle States and the Little Group#^pr-c8b-2-1|§C8b.2.1]] Particles Are Irreducible Unitary Representations

## Laws
- [[§C8b.2 Particle States and the Little Group#^law-c8b-2-2|§C8b.2.2]] Physical Particles Have p² ≥ 0 and p⁰ > 0
- [[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4|§C8b.3.4]] Massless Particles Have No Continuous Spin

## Theorems
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-3|§C8b.2.3]] One Particle, One Orbit
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-4|§C8b.2.4]] The Wigner Element Lies in the Little Group
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-5|§C8b.2.5]] The Induced Representation
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-6|§C8b.2.6]] The Induced States Are Relativistically Normalized
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-7|§C8b.2.7]] The Little Groups of the Physical Orbits
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-8|§C8b.2.8]] The Massive Little Group Is SO(3)
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-9|§C8b.2.9]] Massive Particles Carry Spin
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-10|§C8b.2.10]] Rotations Act by the Rotation Itself
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-11|§C8b.2.11]] The Pauli–Lubanski Vector and the Second Casimir
- [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-12|§C8b.2.12]] The Casimirs of a Massive Particle
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-1|§C8b.3.1]] The Massless Little Group Is ISO(2)
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-2|§C8b.3.2]] Generators of the Massless Little Group
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-3|§C8b.3.3]] Nonzero Translation Eigenvalues Come in Circles
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|§C8b.3.5]] Helicity Is Lorentz Invariant
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-6|§C8b.3.6]] Helicity Is Quantized
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-7|§C8b.3.7]] The Pauli–Lubanski Vector of a Massless Particle
- [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|§C8b.3.8]] Little-Group Translations Shift a Polarization Vector by the Momentum
- [[§C8b.4 Chirality#^thm-c8b-4-1|§C8b.4.1]] Chirality Labels the Two Irreducible Halves of a Dirac Spinor
- [[§C8b.4 Chirality#^thm-c8b-4-2|§C8b.4.2]] Chirality Is Lorentz Invariant
- [[§C8b.4 Chirality#^thm-c8b-4-3|§C8b.4.3]] ★ A Massless Field of Type (j₊, j₋) Carries Helicity j₋ − j₊
- [[§C8b.4 Chirality#^thm-c8b-4-4|§C8b.4.4]] ★ The Vector Potential Has No Chirality; the Field Strength Is a Mirror Pair
- [[§C8b.4 Chirality#^thm-c8b-4-5|§C8b.4.5]] ★ The Maxwell Lagrangian and Field Equations in E ± iB
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|§C8b.5.1]] The Helicity Two-Spinors
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|§C8b.5.2]] Helicity Spinors u±
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|§C8b.5.3]] The v Spinors in the Helicity Basis
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|§C8b.5.4]] The Massless and High-Energy Limit: Helicity Becomes Chirality
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-5|§C8b.5.5]] The Helicity Basis Is the Fixed-Axis Basis Rotated onto the Momentum
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|§C8b.6.1]] At High Energy the Projectors Select the Helicity of a Particle
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|§C8b.6.2]] For an Antiparticle the Spinor Shows the Opposite Helicity
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|§C8b.6.3]] In the Chiral Basis γ⁰γ^μ Is Block Diagonal
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|§C8b.6.4]] Helicity Conservation at the QED Vertex
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|§C8b.6.5]] An Electron Annihilates Only with a Positron of the Opposite Helicity
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-6|§C8b.6.6]] At High Energy ψ_L and ψ_R Are Independent Fields
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|§C8b.6.7]] An Even Number of γ's Joins Opposite Chiralities, an Odd Number Equal Ones
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|§C8b.6.8]] The Mass Term Couples ψ_L and ψ_R
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-9|§C8b.6.9]] Chirality and Helicity of a Solution of the Dirac Equation
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|§C8b.6.10]] The Scalar Vertex Flips the Helicity
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|§C8b.6.11]] Selection Rules for Spinor Bilinears at High Energy
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-1|§C8b.7.1]] The Projected Amplitude
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-2|§C8b.7.2]] The Conjugate Keeps the Projector on the Right
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-3|§C8b.7.3]] With Projectors the Spin Sum Is Still a Trace
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-4|§C8b.7.4]] The Projected Traces
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-5|§C8b.7.5]] The Polarized Squared Amplitudes in Invariants
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|§C8b.7.6]] The Polarized Cross Sections in the Centre-of-Mass Frame
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|§C8b.7.7]] The Average over Helicities Is the Unpolarized Result
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|§C8b.7.8]] Angular Momentum along the Beam Fixes the Zeros
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-9|§C8b.7.9]] Spinors in the Ultrarelativistic Limit
- [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|§C8b.7.10]] The Vertex Is a Circular Polarization Vector
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-1|§C8b.8.1]] ★ The ω-Products of the Four Momenta
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-2|§C8b.8.2]] ★ The Beam Currents
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-3|§C8b.8.3]] ★ The Muon Currents
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|§C8b.8.4]] ★ Opposite Helicities in Both Pairs
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-5|§C8b.8.5]] ★ Equal Helicities in Both Pairs
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-6|§C8b.8.6]] ★ Equal Helicities in the Electron Pair Only
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-7|§C8b.8.7]] ★ Equal Helicities in the Muon Pair Only
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-8|§C8b.8.8]] ★ Each Amplitude Is a Spin-One Rotation Matrix Element
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-9|§C8b.8.9]] ★ Reversing All Helicities Changes at Most the Sign
- [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-10|§C8b.8.10]] ★ The Sum of the Sixteen Is the Unpolarized Result
- [[§C8b.9 Photon Helicity#^thm-c8b-9-1|§C8b.9.1]] ★ The Helicity Vectors Are Helicity Eigenvectors
- [[§C8b.9 Photon Helicity#^thm-c8b-9-2|§C8b.9.2]] ★ The One-Particle States Are Helicity Eigenstates
- [[§C8b.9 Photon Helicity#^thm-c8b-9-3|§C8b.9.3]] ★ Helicity and Transverse Spin from the Noether Spin
- [[§C8b.9 Photon Helicity#^thm-c8b-9-4|§C8b.9.4]] Helicity Mode Algebra and Expansion
- [[§C8b.9 Photon Helicity#^thm-c8b-9-5|§C8b.9.5]] Photons Have Helicity ±1
- [[§C8b.9 Photon Helicity#^thm-c8b-9-6|§C8b.9.6]] Energy and Momentum of Physical States in Helicity Form
- [[§C8b.9 Photon Helicity#^thm-c8b-9-7|§C8b.9.7]] ★ The Spin of Transverse Photons
- [[§C8b.9 Photon Helicity#^thm-c8b-9-8|§C8b.9.8]] ★ Photon Helicity from the Noether Spin
- [[§C8b.9 Photon Helicity#^thm-c8b-9-9|§C8b.9.9]] ★ Null States Change the Transverse Spin, Not the Helicity
- [[§C8b.9 Photon Helicity#^thm-c8b-9-10|§C8b.9.10]] The Helicity Vectors Are the Linear Vectors in Circular Combination
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-1|§C8b.10.1]] The Backward Denominator
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|§C8b.10.2]] The u-Channel Numerator as a Product of 2×2 Matrices
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|§C8b.10.3]] Exactly Backward the Helicity-Conserving Amplitude Vanishes
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|§C8b.10.4]] Near the Backward Direction the Enhancement Is Reduced by the Angle or by the Mass
- [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-5|§C8b.10.5]] ★ The Helicity Amplitudes of Compton Scattering at High Energy
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|§C8b.11.1]] Six of the Sixteen Helicity Amplitudes May Be Nonzero
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-2|§C8b.11.2]] The Helicity Spinors at Very High Energy
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|§C8b.11.3]] The Selection Rule from the Explicit Spinors
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|§C8b.11.4]] The Four Momenta in the Centre-of-Mass Frame and Their Two-Spinors
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|§C8b.11.5]] The Four Inner Products
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|§C8b.11.6]] The Relative Sign of the Two Diagrams, by Counting Exchanges
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-7|§C8b.11.7]] The Scalar Propagators at High Energy
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8|§C8b.11.8]] The Amplitudes ℳ_RR;LL and ℳ_LR;LR
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|§C8b.11.9]] The Six Helicity Amplitudes of ff → ff in Yukawa Theory
- [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-10|§C8b.11.10]] The Spin Average of the Squared Amplitude, by Explicit Averaging
- [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|§C8b.12.1]] The Amplitude of e⁻e⁻ → e⁻e⁻ at Order e²
- [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|§C8b.12.2]] In the Forward Direction the Vector Coupling Conserves Helicity
- [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|§C8b.12.3]] Near the Forward Direction the Helicity-Conserving Amplitudes Are Largest
- [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4|§C8b.12.4]] Near the Backward Direction the Helicities Follow the Directions
