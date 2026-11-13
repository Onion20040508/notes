---
type: subject
discipline: physics
courses: ["PHY 513 (UMich, F. Larsen, Fall 2026)"]
textbooks: ["Peskin & Schroeder, An Introduction to Quantum Field Theory", "Yu Zhao-Huan (余钊焕), Lecture Notes on Quantum Field Theory (量子场论讲义)", "Schwartz, Quantum Field Theory and the Standard Model (further reading)"]
conventions: "[[Larsen PHY 513]]"
status: "level C — C1a, C1b, C2a, C2b, C3, C4, C5a, C5b (§C5b.1–§C5b.9 taught: Lectures 10 and 17, Problem Sets 6 and 9; ★ items of §C5b.5 beyond the lectures), C6a (§C6a.1–§C6a.5, Lecture 13: φ⁴ theory, interaction picture, Dyson series, interacting vacuum, master formula; §C6a.6–§C6a.12, Lecture 14; §C6a.13, the vacuum bubbles exponentiate (PS p. 98, Problem Set 8); §C6a.14, rules for polynomial interactions), C6b (§C6b.1–§C6b.9, Lecture 15, after Yu §6.5: S-matrix, box route, cross section, two-body kinematics, decay widths and kinematics with ★ three-body decays, the width in the propagator, wave packets), C6c (§C6c.1–§C6c.8, Lecture 16 and Problem Set 8, Feynman rules for amplitudes after Yu ch. 7), C6d (§C6d.1–§C6d.6, Lecture 17 rebuilt after Yu §7.1–§7.2: Yukawa theory, contractions with external fermions, Wick and the contraction rule, first and second order, the rules for fermions; §C6d.7 Yukawa potential and the Born comparison, Lecture 18), C8 (§C8.1–§C8.5, Lecture 18, quantum electrodynamics, the Lagrangian and the covariant derivative, gauge invariance, photon lines, Feynman rules, the Coulomb potential and attraction against repulsion; §C8.6–§C8.9, Lecture 19, electron–positron annihilation into muons, the amplitude and the virtual photon, the spin-averaged square by traces, the unpolarized cross section, quark pairs and the ratio R; QED processes of Lectures 20–22 pending), C9 (§C9.1–§C9.5 parity incl. the scalar field, §C9.6–§C9.11 charge conjugation, physical spin, time reversal and CPT, taught; §C9.12 C, T, CPT of the complex scalar field, Problem Set 7; §C9.13 time reversal of the S-matrix and detailed balance, Problem Set 9), CA written, CB written (proofs complete except the placeholders listed under Planned)"
tags: [subject, quantum-field-theory]
---
# Quantum Field Theory

Relativistic quantum field theory at the graduate level (**C**, PHY 513, Larsen, Fall 2026; textbook Peskin & Schroeder). Chapters follow Yu Zhao-Huan's lecture notes (余钊焕《量子场论讲义》), whose chapter numbers they keep: fields are organized by spin after the Poincaré group, and interactions are treated once for all fields. Each concept has one home: statements are short boxes, derivations are folded under them, explanations are titled remarks, and hidden connections are collected in each note's Connections. Multi-step procedures have their own notes in Procedures/, linked from every place they are carried out. Statements are marked by layer: *principles* (postulated), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealized systems). ★ marks material beyond the PHY 513 syllabus; a *draft* banner marks syllabus topics written ahead of the lectures. Relativity is in [[Relativity]], one-particle quantum mechanics in [[Quantum Mechanics]]. Procedures: [[P1 Canonical Quantization]], [[P2 Green's Functions by Contour Integration]], [[P3 Noether's Procedure]], [[P4 Restoring ħ and c]], [[P5 Symmetry Factor of a Diagram]], [[P6 Tree Amplitude from a Lagrangian]], [[P7 From ℳ to σ or Γ]]. Reference cards: [[Scalar Field Card]], [[Vector Field Card]], [[Spinor Field Card]]. Two mathematics chapters collect the tools the physics uses: [[· CA Mathematical Methods]] (limits, generalized functions, Fourier transforms, contours, Gaussian and Bessel integrals, iε boundary values, pairings and symmetry factors, the exponential formula) and [[· CB Lie Groups, Lie Algebras and Representations]] (Lie groups and algebras, complexification, representations, Clifford algebras and the spin groups). The course order, lecture by lecture, is in [[PHY 513 Course Log]], the annotated midterm sheet in [[PHY 513 Midterm Cheatsheet]], the midterm review in [[PHY 513 Midterm Review]] with its drills [[PHY 513 PS Drill]] and [[PHY 513 Notes Drill]]; conventions in [[Larsen PHY 513]].

## Level C — graduate
- [[· C1a Preliminaries]]
- [[· C1b Classical Field Theory]]
- [[· C2a The Quantum Scalar Field]]
- [[· C2b Two-Point Functions, Causality and Propagators]]
- [[· C3 Poincaré Symmetry and Particle States]] (★ §C3.6, §C3.7)
- [[· C4 The Quantum Vector Field]] (★ §C4.2, §C4.3, §C4.4, §C4.5)
- [[· C5a Spinors and the Dirac Equation]]
- [[· C5b The Quantum Spinor Field]]
- [[· C6a Interactions and Correlation Functions]]
- [[· C6b The S-Matrix and Observables]]
- [[· C6c Feynman Rules for Amplitudes]]
- [[· C6d Feynman Rules for Fermions]]
- [[· C8 Quantum Electrodynamics]]
- [[· C9 Discrete Symmetries and Majorana Fields]]
- [[· CA Mathematical Methods]]
- [[· CB Lie Groups, Lie Algebras and Representations]] (★ §CB.22)

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  C1a["C1a Preliminaries"]
  C1b["C1b Classical Field Theory"]
  C2a["C2a The Quantum Scalar Field"]
  C2b["C2b Two-Point Functions, Causality and Propagators"]
  C3["C3 Poincaré Symmetry and Particle States"]
  C4["C4 The Quantum Vector Field"]
  C5a["C5a Spinors and the Dirac Equation"]
  C5b["C5b The Quantum Spinor Field"]
  C6a["C6a Interactions and Correlation Functions"]
  C6b["C6b The S-Matrix and Observables"]
  C6c["C6c Feynman Rules for Amplitudes"]
  C6d["C6d Feynman Rules for Fermions"]
  C8["C8 Quantum Electrodynamics"]
  C9["C9 Discrete Symmetries and Majorana Fields"]
  CA["CA Mathematical Methods"]
  CB["CB Lie Groups, Lie Algebras and Representations"]
  C1a -->|31| C1b
  C1a -->|3| C2a
  C1b -->|13| C2a
  C1a -->|32| C2b
  C1b -->|3| C2b
  C2a -->|149| C2b
  C1a -->|58| C3
  C1b -->|27| C3
  C2a -->|41| C3
  C2b -->|15| C3
  C1a -->|40| C4
  C1b -->|110| C4
  C2a -->|94| C4
  C2b -->|61| C4
  C3 -->|72| C4
  C1a -->|43| C5a
  C1b -->|94| C5a
  C2a -->|2| C5a
  C3 -->|54| C5a
  C1a -->|4| C5b
  C1b -->|26| C5b
  C2a -->|95| C5b
  C2b -->|142| C5b
  C3 -->|38| C5b
  C4 -->|2| C5b
  C5a -->|215| C5b
  C1b -->|32| C6a
  C2a -->|62| C6a
  C2b -->|118| C6a
  C3 -->|1| C6a
  C5b -->|9| C6a
  C1a -->|23| C6b
  C1b -->|1| C6b
  C2a -->|54| C6b
  C2b -->|4| C6b
  C3 -->|6| C6b
  C6a -->|41| C6b
  C2a -->|32| C6c
  C2b -->|31| C6c
  C6a -->|171| C6c
  C6b -->|51| C6c
  C1b -->|3| C6d
  C2a -->|9| C6d
  C2b -->|8| C6d
  C3 -->|2| C6d
  C5a -->|25| C6d
  C5b -->|62| C6d
  C6a -->|39| C6d
  C6b -->|18| C6d
  C6c -->|79| C6d
  C1a -->|10| C8
  C1b -->|7| C8
  C2a -->|3| C8
  C2b -->|1| C8
  C4 -->|46| C8
  C5a -->|58| C8
  C5b -->|5| C8
  C6a -->|16| C8
  C6b -->|43| C8
  C6c -->|8| C8
  C6d -->|83| C8
  C1a -->|12| C9
  C1b -->|9| C9
  C2a -->|74| C9
  C2b -->|9| C9
  C3 -->|8| C9
  C5a -->|157| C9
  C5b -->|121| C9
  C6a -->|9| C9
  C6b -->|19| C9
  C1a -->|2| CA
  C1b -->|3| CA
  C2a -->|6| CA
  C2b -->|44| CA
  C6a -->|12| CA
  C6c -->|1| CA
  C1a -->|23| CB
  C1b -->|1| CB
  C3 -->|48| CB
  C5a -->|55| CB
  C5b -->|1| CB
  C9 -->|4| CB
  CA -->|2| CB
  C1b -.->|24| C1a
  C2a -.->|5| C1a
  C2b -.->|24| C1a
  C3 -.->|10| C1a
  C4 -.->|2| C1a
  C5a -.->|8| C1a
  C6c -.->|1| C1a
  C6d -.->|1| C1a
  CA -.->|52| C1a
  CB -.->|21| C1a
  C2a -.->|35| C1b
  C2b -.->|4| C1b
  C3 -.->|14| C1b
  C4 -.->|4| C1b
  C5a -.->|3| C1b
  C5b -.->|2| C1b
  C6a -.->|4| C1b
  C8 -.->|1| C1b
  C9 -.->|5| C1b
  CA -.->|34| C1b
  CB -.->|3| C1b
  C2b -.->|29| C2a
  C3 -.->|4| C2a
  C5b -.->|2| C2a
  C6a -.->|11| C2a
  C6b -.->|1| C2a
  CA -.->|220| C2a
  C6a -.->|17| C2b
  CA -.->|484| C2b
  C4 -.->|5| C3
  C5a -.->|8| C3
  C5b -.->|5| C3
  C6a -.->|9| C3
  C6c -.->|6| C3
  C9 -.->|12| C3
  CA -.->|13| C3
  CB -.->|93| C3
  C5a -.->|1| C4
  C5b -.->|9| C4
  C8 -.->|49| C4
  CA -.->|152| C4
  C5b -.->|46| C5a
  C8 -.->|3| C5a
  C9 -.->|10| C5a
  CA -.->|7| C5a
  CB -.->|71| C5a
  C6a -.->|1| C5b
  C6d -.->|1| C5b
  C9 -.->|13| C5b
  CA -.->|133| C5b
  CB -.->|1| C5b
  C6b -.->|7| C6a
  C6c -.->|20| C6a
  C6d -.->|4| C6a
  CA -.->|113| C6a
  CB -.->|10| C6a
  C6c -.->|18| C6b
  C8 -.->|2| C6b
  C9 -.->|2| C6b
  CA -.->|56| C6b
  C6d -.->|8| C6c
  C8 -.->|1| C6c
  CA -.->|49| C6c
  C8 -.->|13| C6d
  C9 -.->|2| C6d
  CA -.->|31| C6d
  CA -.->|10| C8
  CA -.->|42| C9
  CB -.->|38| C9
```

## Planned
Yu's chapter 6, Interactions of quantum fields, and his chapter 7, Feynman diagrams, are written as four chapters (through Lecture 18 and Problem Set 9): C6a Interactions and Correlation Functions (§C6a.0: setups and observables; §C6a.1–§C6a.5: φ⁴ theory, the interaction picture, the Dyson series, the interacting vacuum and the master formula; §C6a.6–§C6a.12: normal ordering, Wick's theorem, Feynman diagrams and rules for correlation functions in position and momentum space, symmetry factors, the iε limit and the cancellation of vacuum bubbles, with the combinatorics in §CA.8–§CA.9; §C6a.13: the exponential of the connected vacuum bubbles and the vacuum energy density; §C6a.14: the rules for any polynomial interaction); C6b The S-Matrix and Observables (§C6b.1–§C6b.9 in Yu §6.5's order: the S-matrix and the invariant amplitude, transition probabilities in a box, the cross section, two-body scattering kinematics, decay widths, decay kinematics (★ three-body), the width in the propagator, and the cross section from wave packets); C6c Feynman Rules for Amplitudes (§C6c.1–§C6c.8: amplitudes as amputated correlation functions, matrix elements between particle states and the Feynman rules for amplitudes, particle production by a classical source); C6d Feynman Rules for Fermions (Lecture 17, after Yu §7.1–§7.2, mirroring C6c: Yukawa theory, contractions with external fermions, Wick's theorem with signs and the contraction rule, first and second order, the momentum-space rules, and the Yukawa potential, §C6d.7, taught in Lecture 18). The Feynman propagators of the other fields (Yu §6.4) are with their fields: complex scalar [[§C6a.8 Feynman Diagrams for Correlation Functions#^thm-c6a-8-2|Theorem §C6a.8.2]], vector fields [[§C4.11 Vector-Field Propagators|§C4.11]] and [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-5|Theorem §C8.3.5]], Dirac field [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]. The planned C7 Feynman diagrams is dissolved (user decision 2026-11-04: S-matrix rules in C6b and C6c, fermion rules in C6d). C8 Quantum Electrodynamics is started (user decision 2026-11-09): written §C8.1–§C8.5 (Lecture 18), the Lagrangian and the covariant derivative, gauge invariance, photon lines, the QED Feynman rules, the Coulomb potential and why like charges repel, and §C8.6–§C8.9 (Lecture 19), the first process $e^+e^- \to \mu^+\mu^-$: the amplitude and the virtual photon, the spin-averaged square by traces, the unpolarized cross section, quark–antiquark production and the ratio $R$; the QED processes of Lectures 20–22 (helicity structure, crossing symmetry, Compton scattering), the Ward identity and the quantization of the electromagnetic field in the course (Lecture 25) are pending.

**Level C — PHY 513 (Larsen, Fall 2026; Peskin & Schroeder; Yu)**
Chapters without notes yet, or with parts pending (Yu's numbering): C8 Quantum electrodynamics (written: §C8.1–§C8.9, Lectures 18–19; QED processes of Lectures 20–22 pending) · C9 Discrete symmetries and Majorana fields (written: parity §C9.1–§C9.5, charge conjugation §C9.6–§C9.7, physical spin §C9.8, time reversal §C9.9–§C9.10, CPT §C9.11, C, T and CPT of the complex scalar field §C9.12, time reversal of the S-matrix and detailed balance §C9.13; Majorana fields pending) · C10 The S-matrix and correlation functions (LSZ; the S-matrix, cross sections and decay rates themselves are in C6b §C6b.1–§C6b.9) · C11 Path-integral quantization · *Second semester* (PHY 513 Lecture 17, slide 26: renormalization, "a deep principle: much more in 2nd semester"): loop integrals, regularization (dimensional regularization), renormalization, Cutkosky cuts; the dimension count that sorts couplings into renormalizable and nonrenormalizable is already in [[§C1b.3 Mass Dimension, Locality and Power Counting|§C1b.3]] and [[§C6d.1 Yukawa Theory|§C6d.1]]

**Mathematics chapter CB**: [[· CB Lie Groups, Lie Algebras and Representations]] (§CB.0–§CB.23) has its full logical chain, every definition and theorem in reading order, and proofs, except those still marked *Proof (to be filled)* (the Lie correspondence in §CB.3, Bargmann's theorem in §CB.21, Mackey and Wigner–Mackey in §CB.22★). The layout is "physics refers to mathematics" (option 1, 2026-10-08; physics form since the rollout of 2026-11-02, user-approved demos §C5a.1 and §C3.2): the mathematical statements of C1a, C3, C5a and C9 have their homes in CB (the matrix groups, the components of the Lorentz group and the identity component, the discrete element of O(3), the dual space, multilinear tensors and their transformation law; §CB.0, linear algebra in components, holds the statements of spinor-space layer 1; the SU(2)/SO(3) part is §CB.2, the Lorentz algebra §CB.5–§CB.6), and CB rests only on CB, CA and the Math notes, with two exceptions embedded from the physics chapters: the orbit theorem of §C1a.4 in §CB.22★ and the ★ Grassmann boxes of §C5b.1 in §CB.23. Physics sections do not embed CB or CA statements: each structure is stated in the Model or Definition that uses it with a link to its CB/CA home, each judgement tool is a physics statement box whose *Proof:* links CB, and the CB/CA items a section relies on are listed, with what each guarantees there, in a folded *Mathematical background* block at the end of the section, before Connections. §CB.23 Grassmann algebras is completed with C11 (the two ★ Grassmann boxes of §C5b.1 move then).
