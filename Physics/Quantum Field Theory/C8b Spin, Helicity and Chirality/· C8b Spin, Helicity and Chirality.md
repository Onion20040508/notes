---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
tags: [chapter, quantum-field-theory]
---
# C8b Spin, Helicity and Chirality
← [[· C8a Quantum Electrodynamics]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (18), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (10), [[· C3 Poincaré Symmetry and Covariant Fields|C3 Poincaré Symmetry and Covariant Fields]] (77), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (89), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (75), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (6), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (8), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (6), [[· C8a Quantum Electrodynamics|C8a Quantum Electrodynamics]] (60), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (16), [[· CA Mathematical Methods|CA Mathematical Methods]] (10), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (18)
**Used by:** [[· C1a Preliminaries|C1a Preliminaries]] (4), [[· C3 Poincaré Symmetry and Covariant Fields|C3 Poincaré Symmetry and Covariant Fields]] (8), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (50), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (14), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (16), [[· C8a Quantum Electrodynamics|C8a Quantum Electrodynamics]] (4), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (4), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (12)

C8b builds the labels of spin for a moving particle, helicity and chirality, and then follows $e^+e^- \to \mu^+\mu^-$ helicity by helicity (Lecture 20, "Helicity Structure", 16 Nov 2026; PS §5.2; the user's notes, Lecture 20 update). Before this chapter no process in the notes followed a spin: scalar particles have none, and for fermions the spins were summed and averaged, or carried unchanged through a nonrelativistic limit ([[§C8b.1 Why Spin Must Now Be Tracked|§C8b.1]]). To fix the spins in a process one needs a label on which all observers agree. The chapter introduces the structures behind such a label formally and in logical order, starting from the new concepts (user decision 2026-11-18): what was done so far, the question "what is the spin of a moving particle?" and the plan (§C8b.1); a particle as an irreducible unitary representation, the standard momentum, the little group and the Wigner rotation, the spin of a massive particle and the Pauli–Lubanski vector (§C8b.2); the little group $ISO(2)$ of a massless particle, the exclusion of continuous spin, helicity with its definition, its invariance for massless and its frame dependence for massive particles, its quantization, the parity pairs, and polarization vectors with the origin of gauge invariance (§C8b.3); chirality, the label of a field component, and the two labels side by side (§C8b.4); the helicity spinors of Problem Set 5 and the massless limit, where helicity becomes chirality (§C8b.5). Then the lecture proper: the projected spinors, the projectors selecting helicity at high energy with the reversal for antiparticles, $\gamma^0\gamma^\mu$ block diagonal and helicity conservation at the QED vertex, $e^-_R$ annihilating only with $e^+_L$ into $J_z = \pm1$, and the chiral fields at high energy (§C8b.6); the projected amplitude, the conjugate and the spin sum with projectors, the traces with $\gamma^5$, $|\mathcal M|^2 = \frac{16e^4}{q^4}(p\cdot k')(p'\cdot k)$, the polarized cross sections $\frac{\alpha^2}{4E_{\rm cm}^2}(1 \pm \cos\theta)^2$ and their average, the zeros from angular momentum, and the amplitude with explicit helicity spinors as the overlap of a circular polarization vector with its rotated image (§C8b.7); the steps are [[P9 Helicity Amplitudes]]. With both masses kept, Yu's sixteen amplitudes, their mass suppressions, angular zeros and sum are ★ §C8b.8. The helicity of photons and of massive vector quanta comes last, because the fermion story does not need it (§C8b.9, draft).

**Lectured and not lectured.** Lectured in PHY 513: the definition of helicity and its dependence on the frame (Lecture 20, slides 9, 11, 24; in §C8b.3); chirality and its projectors (Lectures 7–8 and Problem Set 5; home [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], quoted in §C8b.4, whose comparison answers a question asked in Lecture 20); the helicity spinors (Problem Set 5, Problem 6; Lecture 20, slides 24–25; §C8b.5); the vertex and the polarized cross sections (Lecture 20; §C8b.6, §C8b.7). Not lectured: the little-group construction of §C8b.2 and the proofs of §C8b.3, which are the formal foundation, from Yu §3.3, the supplement of the user's PHY 513 notes (Ch. 7 §7.7) and the user's pre-course notes; they were the starred sections §C3.6★ and §C3.7★ until 2026-11-18 and stand here without a star because the spin-resolved processes rest on them (user decision). ★ §C8b.8 (Yu §8.2.4, masses kept) is beyond the lecture. §C8b.9 is a draft, written ahead of Lecture 25 in Yu's notation; its Proca and Noether-spin boxes are ★. The one fact about stabilizers that earlier chapters use is [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]]; starred boxes of C4 and C5b that rest on the little group point forward to §C8b.2.

## How C8b relates to Yu and PS
Yu treats the one-particle states and the little group in §3.3 (massive particles §3.3.1, massless particles and helicity §3.3.2), the helicity spinors in §5.4.2, the polarized amplitudes of $e^+e^- \to \mu^+\mu^-$ with both masses in §8.2.4 and chirality in §8.3, and the helicity of vector quanta in §4.3–§4.4. PS §5.2 does the projector-and-trace route and the explicit spinors for massless fermions; PS has no little-group construction. The sections were written for C3, C4, C5a and C8 and collected in C8 as §C8.12–§C8.17★ on 2026-11-16; the chapter was formed on 2026-11-18.

| Section | Lecture, slides | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|---|
| §C8b.1 | 20 (the question behind the lecture) | — | — | §5.2, p. 141 |
| §C8b.2 | — (not lectured) | §3.3, (3.87)–(3.109); §3.3.1, (3.110)–(3.177) | one-particle states as representations; standard momentum, little group; massive particles and spin; Pauli–Lubanski vector | — |
| §C8b.3 | 20: slides 9, 11, 24 | §3.3.1, (3.175)–(3.177); §3.3.2, (3.178)–(3.218) | the massless little group $ISO(2)$, continuous spin; helicity of states; invariance and quantization for massless particles; Pauli–Lubanski vector; parity pairs | §5.2, p. 141 |
| §C8b.4 | 20: slides 8, 9, 11, 24; 7–8 (the Weyl halves) | §5.1, (5.36); §8.3, (8.159)–(8.168), (8.174)–(8.189) | $\gamma^5$ a Lorentz scalar; chirality projectors and projected fields; helicity and chirality at high energy | §3.4, pp. 50–51, (3.68)–(3.72) |
| §C8b.5 | 20: slides 24–25 | §5.4.2, (5.158)–(5.199); §8.2.4, (8.100)–(8.107); §8.3, (8.174)–(8.178) | helicity two-spinors and helicity spinors $u_\lambda$, $v_\lambda$; massless limit | §3.3, (3.52)–(3.54) |
| §C8b.6 | 20: slides 3–11, 26–27 | §8.2.4, (8.108), (8.143)–(8.157); §8.3, (8.159)–(8.168), (8.174)–(8.189) | chirality projectors; helicity equals chirality at high energy, reversed for $v$; mass-suppressed helicity amplitudes | §5.2, pp. 141–142, (5.17)–(5.18), p. 145 |
| §C8b.7 | 20: slides 14–20, 23–28 | §8.2.4, (8.99)–(8.142), (8.158) | polarized amplitudes with explicit helicity spinors and both masses; currents (8.118), (8.132)–(8.135); $\mp e^2(1 \pm \cos\theta)$; parity; the sum of sixteen | §5.2, pp. 142–146, (5.17)–(5.32), Figure 5.4 |
| §C8b.8★ | — | §8.2.4, (8.99), (8.108)–(8.158), Figures 8.4–8.6 | massive helicity spinors, currents and all sixteen amplitudes with masses; parity phases; the sum | — |
| §C8b.9 | 18: slides 9, 13; 20: slide 28 | §4.3.1, (4.103)–(4.121); §4.4.4, (4.267)–(4.280) | helicity vectors and states of the Proca field; photon helicity modes, helicity ±1, Noether spin | §9.4, p. 298 |

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
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|§C8b.5.1]] The Helicity Two-Spinors
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|§C8b.5.2]] Helicity Spinors u±
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|§C8b.5.3]] The v Spinors in the Helicity Basis
- [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|§C8b.5.4]] The Massless and High-Energy Limit: Helicity Becomes Chirality
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|§C8b.6.1]] At High Energy the Projectors Select the Helicity of a Particle
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|§C8b.6.2]] For an Antiparticle the Spinor Shows the Opposite Helicity
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|§C8b.6.3]] In the Chiral Basis γ⁰γ^μ Is Block Diagonal
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|§C8b.6.4]] Helicity Conservation at the QED Vertex
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|§C8b.6.5]] An Electron Annihilates Only with a Positron of the Opposite Helicity
- [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-6|§C8b.6.6]] At High Energy ψ_L and ψ_R Are Independent Fields
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
