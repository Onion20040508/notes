---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.15★ Derivative Couplings and Scalar QED|§C8a.15★]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.2 Particle States and the Little Group|§C8b.2]] →

*Sources: PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 9, 11 and 24, and transcript · the user's PHY 513 notes, Lecture 20 update (chapter opening, §20.1); Ch. 7 §7.7 (Supplement "Particles as representations (Wigner's classification)") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.2, p. 141 · Yu Zhao-Huan, 量子场论讲义, §3.3 and §8.2.4–§8.3 (as the sources of the sections listed below) · PHY 513, Problem Set 5, Problem 6.*

Until this chapter no process in these notes followed a spin from the initial state to the final state. Scalar particles have none; for fermions the spins were summed and averaged, or carried unchanged through a nonrelativistic limit, or left as labels on external spinors that were never interpreted. Lecture 20 asks for the cross section of $e^+e^- \to \mu^+\mu^-$ with each of the four spins fixed (PS §5.2, p. 141: "quantize each spin along the direction of the particle's motion"). For that one must be able to say what the spin of a moving particle is, in a way that does not depend on who looks. This section collects how spin was avoided so far, states the question, and lays out how the chapter answers it and which parts of the answer were lectured.

**Setup.** A map of the chapter: it makes no statement of its own. Each fact quoted below holds in the setup of its home, which is linked: one-particle states of a relativistic quantum theory ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^mod-c3-4-4|Model §C3.4.4]]) for the statements about states, the c-number spinors of the free Dirac field for the statements about spinors, the tree-level processes of chapters C6c, C6d and C8a for the table.

*Conventions* ([[Larsen PHY 513]]): a subscript $R$ or $L$ on a particle is its physical helicity ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]); on a field or a projected spinor it is the chirality ([[§C8b.4 Chirality|§C8b.4]]); $s$, $r$ label a spin basis of two-spinors ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3|Def. §C5a.10.3]]).

## How spin was handled so far

> [!remark] Remark: How spin was handled before this chapter
> | Process | Home | What was done with the spins |
> |---|---|---|
> | scalar particles: $\phi\phi \to \phi\phi$, the cubic–quartic and three-scalar theories, $\Phi \to \phi\phi$, the linear sigma model | [[§C6c.4 First Order꞉ Enumerate, then Filter\|§C6c.4]], [[§C6c.6 Feynman Rules for Amplitudes\|§C6c.6]], [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index\|§C6c.8]]–[[§C6c.9 The Linear Sigma Model꞉ the Broken Phase\|§C6c.9]] | no spin: an external line carries a momentum and nothing else |
> | Yukawa theory at order $g^2$: fermion–fermion, fermion–antifermion scattering, pair annihilation into scalars | [[§C6d.5 Second Order\|§C6d.5]] ([[§C6d.5 Second Order#^ex-c6d-5-1\|Examples §C6d.5.1]]–[[§C6d.5 Second Order#^ex-c6d-5-3\|§C6d.5.3]]), rules [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2\|Theorem §C6d.6.2]] | external spinors $u^s(p)$, $v^s(p)$ written with fixed labels $s$; the amplitudes were left in that form and the labels were never read as a direction of the spin |
> | the Yukawa potential | [[§C6d.7 The Yukawa Potential\|§C6d.7]] ([[§C6d.7 The Yukawa Potential#^thm-c6d-7-1\|Theorem §C6d.7.1]]) | nonrelativistic limit: each fermion keeps its spin label, and the label drops out of the potential |
> | the Coulomb potential | [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel\|§C8a.5]] ([[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-1\|Theorem §C8a.5.1]]) | the same nonrelativistic limit |
> | $e^+e^- \to \mu^+\mu^-$, unpolarized | [[§C8a.7 The Spin-Averaged Squared Amplitude\|§C8a.7]] ([[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1\|Def. §C8a.7.1]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3\|Theorem §C8a.7.3]]), [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production\|§C8a.8]] | summed over the final spins and averaged over the initial ones; the sums are traces |
> | $e^+e^- \to q\bar q$ and the ratio $R$ | [[§C8a.9 Quark–Antiquark Production and the Ratio R\|§C8a.9]] | the same average |
> | an electron in a Coulomb field: Rutherford, Mott | [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula\|§C8a.10]], [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field\|§C8a.11]] ([[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-2\|Theorem §C8a.11.2]]) | Rutherford: nonrelativistic limit, the spin does not flip; Mott: sum over the final spin and average over the initial one |
> | $e^-\mu^- \to e^-\mu^-$ | [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution\|§C8a.12]] ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2\|Theorem §C8a.12.2]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4\|Theorem §C8a.12.4]]), [[§C8a.13 The Cross Section for Electron–Muon Scattering\|§C8a.13]] | spin average, obtained from the annihilation result by crossing |
> | helicity two-spinors (Problem Set 5, Problem 6) | [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1\|Theorem §C8b.5.1]] | a choice of basis for the two-spinors $\xi$, computed once and not followed through a process |
>
> In every row the result either does not involve spin at all, or is a sum over a complete set of spin states, which does not depend on the basis chosen for them ([[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]], [[§C6b.3 The Cross Section#^thm-c6b-3-10|Theorem §C6b.3.10]]). None of these results needed to say which way a spin points.

^rem-c8b-1-1

## The question

> [!remark] Remark: What is the spin of a moving particle?
> For a particle at rest the answer is that of Quantum Mechanics: its states carry a representation of the rotation group, and "spin up along $\hat{\mathbf z}$" is the eigenvalue of $\hat J^3$ (for the Dirac particle: [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-4|Theorem §C5a.10.4]], with the physical spin of [[§C9.8 Physical Spin versus Wave-Function Spin#^def-c9-8-3|Def. §C9.8.3]]). For a moving particle three labels are in use, and they behave differently under a change of frame:
> 1. **The spin along a fixed axis**, the label $s$ of $u^s(p)$: it is defined by boosting the rest-frame state. Rotations act on it as on a particle at rest, but a boost that is not along $\mathbf p$ acts through a rotation that depends on the momentum, the Wigner rotation ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-10|Theorem §C8b.2.10]]; [[§C8b.2 Particle States and the Little Group#^rem-c8b-2-3|§C8b.2, Remark: The Wigner rotation and Thomas precession]]). "Spin up along $\hat{\mathbf z}$" is not a boost-invariant statement.
> 2. **Helicity**, the spin along the direction of motion ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]): it refers to no external axis, so it is invariant under rotations. For $m > 0$ an observer who overtakes the particle sees the momentum reversed and the spin unchanged, so the helicity changes sign ([[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-2|§C8b.3, Remark: Helicity of a massive particle]]); for $m = 0$ no observer can overtake it, and the helicity is the same in every frame ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]).
> 3. **Chirality**, the eigenvalue of $\gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]): it is the same in every frame for every mass ([[§C8b.4 Chirality#^thm-c8b-4-2|Theorem §C8b.4.2]]), but it labels a component of the field, not a state. For $m = 0$, and for fast particles up to corrections of relative size $m/E$, it coincides with the helicity ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]), with a reversal for antiparticles ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]).
>
> The label of a state that every observer agrees on is therefore the helicity of a massless particle. This is why Lecture 20 works at high energy, with the masses set to zero (slide 24: "helicity is not Lorentz-invariant except in the UR limit").

^rem-c8b-1-2

## Why the formal structure enters here

All three statements of the remark rest on one construction, due to Wigner. A Lorentz transformation moves the momentum of a state; the transformations that leave a given momentum fixed form a group, the *little group* of that momentum ([[§C8b.2 Particle States and the Little Group#^def-c8b-2-2|Def. §C8b.2.2]]), and the states at that momentum carry a representation of it ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-5|Theorem §C8b.2.5]]). For $m > 0$ the little group is the rotation group of the rest frame ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-8|Theorem §C8b.2.8]]), and its representations are the spins ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-9|Theorem §C8b.2.9]]); for $m = 0$ it is the Euclidean group of a plane ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-1|Theorem §C8b.3.1]]), and the label left over is the helicity. Until now the notes needed only the simplest consequence, that a massive particle of spin $s$ has $2s + 1$ states at each momentum, and mentioned the construction as a pointer. With spins fixed in a process, the labels themselves are needed, so the construction is built here, formally and in order, before it is used.

## The plan of the chapter

1. §C8b.1 (this section): what was done so far, the question, the plan.
2. [[§C8b.2 Particle States and the Little Group|§C8b.2]] Particle States and the Little Group: what a particle is for the Poincaré group; the standard momentum, the stabilizer of a momentum (its little group), the Wigner rotation; for $m > 0$ the little group is the rotation group and its label is the spin. *Status:* foundation: Yu §3.3–§3.3.1, the supplement of the user's PHY 513 notes (Ch. 7 §7.7), the pre-course notes §2.3; not lectured.
3. [[§C8b.3 Massless Particles and Helicity|§C8b.3]] Massless Particles and Helicity: for $m = 0$ the little group is $ISO(2)$; helicity is defined, shown to be the same in every frame for $m = 0$ and frame dependent for $m > 0$, quantized, and tied to the Pauli–Lubanski vector; polarization vectors and gauge invariance. *Status:* the definition and the frame dependence are Lecture 20 (slides 9, 11, 24); the proofs are foundation (Yu §3.3.2), not lectured.
4. [[§C8b.4 Chirality|§C8b.4]] Chirality: the label of a field component, and the comparison of the two labels. *Status:* chirality is taught material of [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (Lectures 7–8, Problem Set 5); the comparison answers a question asked in Lecture 20.
5. [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]] Helicity Spinors and the Massless Limit: the spinors $u$, $v$ of definite helicity; at $m = 0$ and at high energy helicity becomes chirality. *Status:* Problem Set 5, Problem 6; Lecture 20, slides 24–25; Yu §5.4.2.
6. [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]] Helicity Conservation at the QED Vertex: the projectors select helicities of fast particles, and both fermions at a QED vertex carry the same projection. *Status:* Lecture 20; PS §5.2; Yu §8.3.
7. [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]] Polarized Cross Sections for Muon Pair Production: $e^+e^- \to \mu^+\mu^-$ helicity by helicity. *Status:* Lecture 20; PS §5.2.
8. [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]] Polarized Amplitudes with Masses: the sixteen helicity amplitudes with both masses kept. *Status:* ★ beyond the lecture: Yu §8.2.4.
9. [[§C8b.9 Photon Helicity|§C8b.9]] Photon Helicity: the two helicities of the photon and the helicity of massive vector quanta; last, because the fermion story does not need it. *Status:* draft, written ahead of Lecture 25 in Yu's notation (Yu §4.3–§4.4); its Proca and Noether-spin boxes are ★.

> [!abstract]- Mathematical background
> Proved in CB; nothing in this section relies on it directly. The sections that follow use:
> - [[§CB.22★ The Poincaré Group and Induced Representations#^thm-cb-22-13|Theorem §CB.22.13]] — the induced representation of a semidirect product is unitary; physics form: [[§C8b.2 Particle States and the Little Group#^thm-c8b-2-5|Theorem §C8b.2.5]].
> - [[§CB.10 SU(2) and SO(3)꞉ Spin j, Topology and Symmetric Powers#^thm-cb-10-3|Theorem §CB.10.3]] — the irreducible representations of the rotation algebra, one for each spin; physics form: [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^thm-c3-1-1|Theorem §C3.1.1]].
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-4|Theorem §CB.19.4]] — $\gamma^5$ commutes with the spinor generators; physics form: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]].

> [!remark]- Connections
> - The unpolarized cross section is defined by the sum and average that made spin labels unnecessary — [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]; the helicity-resolved cross sections of [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]] add up to it ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|Theorem §C8b.7.7]]).
> - The elementary fact behind the massive little group, that the Lorentz transformations fixing a timelike vector are the rotations of its rest frame, is already available in C1a — [[§C1a.4 The Lorentz Group#^thm-c1a-4-5|Theorem §C1a.4.5]]; it is what the split of a four-vector by a momentum uses ([[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-2|Theorem §C4.1.2]]).
> - For an antiparticle the spin shown by the spinor $v$ (the wave-function spin, [[§C9.8 Physical Spin versus Wave-Function Spin#^def-c9-8-1|Def. §C9.8.1]]) and the physical spin of the state ([[§C9.8 Physical Spin versus Wave-Function Spin#^def-c9-8-3|Def. §C9.8.3]]) are different notions; how they are related is [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]].
> - The steps of a helicity-amplitude calculation are collected in [[P9 Helicity Amplitudes|P9]].
