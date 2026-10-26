---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6
tags: [chapter, quantum-field-theory]
---
# C6 Interactions of Quantum Fields
← [[· C5b The Quantum Spinor Field]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (32), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (16), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (69), [[· CA Mathematical Methods|CA Mathematical Methods]] (63), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (4)
**Used by:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (2), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (2), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (1), [[· CA Mathematical Methods|CA Mathematical Methods]] (7)

## How C6 relates to Yu
C6 follows the course (Lectures 13–14) and the user's notes (Ch. 13–14), not Yu's chapter split (user decision, 2026-10-26). Yu treats Wick's theorem in §6.3, the Feynman rules for $S$-matrix elements in ch. 7 (Yukawa first, §7.2; $\phi^4$ and symmetry factors, §7.3), and reaches correlation functions and the cancellation of vacuum bubbles only in ch. 10, through asymptotic in-fields and the LSZ formula; the course reaches them through the $i\varepsilon$ projection onto the interacting vacuum (§C6.4). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6.1 | Ch. 6 opening, (6.1)–(6.5), (6.13); §6.1.1, (6.39)–(6.46) | | §4.1 |
| §C6.2 | §6.1, (6.22)–(6.38), (6.44)–(6.50) | $V(t) = e^{iH_0t}e^{-iHt}$ | §4.2 |
| §C6.3 | §6.2, (6.93)–(6.121) | $U(t, t_0)$, Dyson series; $S = U(\infty, -\infty)$ (6.122)–(6.125) | §4.2 |
| §C6.4 | §10.4, (10.176)–(10.181) (another route) | in-fields and LSZ; normalization a phase | §4.2 |
| §C6.5 | §6.3.1, (6.131)–(6.165) | bosons and fermions together | §4.3, (4.32)–(4.37) |
| §C6.6 | §6.3.1, (6.166)–(6.168); §6.3.2, lemma (6.169)–(6.170), proofs (6.171)–(6.193) | lemma appends an earlier field | §4.3, (4.38)–(4.41) |
| §C6.7 | §10.5.1, (10.187)–(10.192) | $G^{(2)}$ of in-fields, with a $\delta m^2$ vertex | §4.4, (4.42)–(4.44) |
| §C6.8 | §7.3, (7.112)–(7.120) | $T$-matrix elements | §4.4, (4.45), p. 94 |
| §C6.9 | §7.3, (7.124)–(7.125), (7.127)–(7.128), (7.131)–(7.132); p. 293 | self-energies $\langle\mathbf k\rvert iT\lvert\mathbf k\rangle$ | §4.4, pp. 92–93 |
| §C6.10 | §7.2, rules 8, 10, 11 (pp. 287–288); §7.3, p. 296; §10.5.1, (10.198)–(10.203) | Yukawa $S$-matrix rules; Fourier transform of $G^{(n)}$ | §4.4, (4.46)–(4.47), p. 95 |
| §C6.11 | §10.4, (10.176)–(10.181); §10.5.1, (10.193)–(10.197) | no $T(1 - i\varepsilon)$; binomial proof | §4.4, (4.48)–(4.57) |
| §CA.7 (mathematics) | (6.167)–(6.168); (7.114)–(7.125); (10.194)–(10.196) | | §4.3–§4.4 |

## Sections
- [[§C6.1 From Free to Interacting Fields]] — 513 notes Ch. 13 §13.1; PS §4.1
- [[§C6.2 The Interaction Picture]] — 513 notes Ch. 13 §13.2; PS §4.2, pp. 83–84
- [[§C6.3 The Time-Evolution Operator and Time Ordering]] — 513 notes Ch. 13 §13.3; PS §4.2, pp. 84–86
- [[§C6.4 The Interacting Vacuum and the Two-Point Function]] — 513 notes Ch. 13 §§13.4–13.6; PS §4.2, pp. 86–87
- [[§C6.5 Normal Ordering and Contractions]] — 513 notes Ch. 14 §14.1–§14.2; PS §4.3, pp. 88–89
- [[§C6.6 Wick's Theorem]] — 513 notes Ch. 14 §14.2; PS §4.3, pp. 89–90
- [[§C6.7 Feynman Diagrams for Correlation Functions]] — 513 notes Ch. 14 §14.3; PS §4.4, pp. 90–92
- [[§C6.8 Position-Space Feynman Rules]] — 513 notes Ch. 14 §14.4–§14.5; PS §4.4, pp. 92–94
- [[§C6.9 Symmetry Factors in Practice]] — 513 notes Ch. 14 §14.5; PS §4.4, pp. 92–93
- [[§C6.10 Feynman Rules in Momentum Space]] — 513 notes Ch. 14 §14.6; PS §4.4, pp. 94–95
- [[§C6.11 The iε Limit and Vacuum Bubbles]] — 513 notes Ch. 14 §14.7–§14.8; PS §4.4, pp. 95–99

## Principles
- [[§C6.1 From Free to Interacting Fields#^pr-c6-1-6|§C6.1.6]] Canonical Quantization of $\phi^4$ Theory at a Reference Time

## Theorems
- [[§C6.1 From Free to Interacting Fields#^thm-c6-1-2|§C6.1.2]] The Coupling of $\phi^4$ Theory Is Dimensionless
- [[§C6.1 From Free to Interacting Fields#^thm-c6-1-3|§C6.1.3]] The Field Equation of $\phi^4$ Theory
- [[§C6.1 From Free to Interacting Fields#^thm-c6-1-4|§C6.1.4]] The Conjugate Momentum Is Unchanged by the Interaction
- [[§C6.1 From Free to Interacting Fields#^thm-c6-1-5|§C6.1.5]] The Hamiltonian of $\phi^4$ Theory and Its Split
- [[§C6.1 From Free to Interacting Fields#^thm-c6-1-7|§C6.1.7]] The Ladder Operators Diagonalize the Free Hamiltonian, Not the Full One
- [[§C6.2 The Interaction Picture#^thm-c6-2-1|§C6.2.1]] The Interaction-Picture Field Is the Free Mode Expansion
- [[§C6.2 The Interaction Picture#^thm-c6-2-2|§C6.2.2]] The Interaction-Picture Field Obeys the Free Field Equations
- [[§C6.2 The Interaction Picture#^thm-c6-2-3|§C6.2.3]] Free-Vacuum Correlators of the Interaction-Picture Field Are the Free Ones
- [[§C6.2 The Interaction Picture#^thm-c6-2-4|§C6.2.4]] The Heisenberg Field in Terms of the Interaction-Picture Field
- [[§C6.2 The Interaction Picture#^thm-c6-2-5|§C6.2.5]] The Interaction Hamiltonian Is the Interaction of the Free Field
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-1|§C6.3.1]] The Time-Evolution Operator Is Unitary
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-2|§C6.3.2]] The Equation of Motion of the Time-Evolution Operator
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-3|§C6.3.3]] The Exponential Solves the Equation Only for Commuting Generators
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-4|§C6.3.4]] Ordered Iterated Integrals Are Time-Ordered Cube Integrals
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-5|§C6.3.5]] Dyson's Formula
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-6|§C6.3.6]] Properties of the Time-Evolution Operator
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-7|§C6.3.7]] Dyson's Formula Between Two Times
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-1|§C6.4.1]] Projection onto the Ground State
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-2|§C6.4.2]] The Interacting Vacuum Evolved from the Far Past
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-3|§C6.4.3]] The Conjugate Vacuum Evolved into the Far Future
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-4|§C6.4.4]] The Normalization Is the Vacuum-to-Vacuum Amplitude
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-5|§C6.4.5]] The Two-Point Function as a Chain of Free Evolutions
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-6|§C6.4.6]] The Master Formula
- [[§C6.4 The Interacting Vacuum and the Two-Point Function#^thm-c6-4-7|§C6.4.7]] The n-Point Functions
- [[§C6.5 Normal Ordering and Contractions#^thm-c6-5-1|§C6.5.1]] The Normal-Ordered Product of n Free Fields
- [[§C6.5 Normal Ordering and Contractions#^thm-c6-5-2|§C6.5.2]] The Price of Reordering Is the Wightman Function
- [[§C6.6 Wick's Theorem#^lem-c6-6-1|§C6.6.1]] Appending a Field of Earlier Time
- [[§C6.6 Wick's Theorem#^thm-c6-6-2|§C6.6.2]] Wick's Theorem
- [[§C6.6 Wick's Theorem#^thm-c6-6-3|§C6.6.3]] Free Vacuum Values Are Sums over Pairings
- [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|§C6.7.1]] The First-Order Numerator
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|§C6.8.1]] The Coefficient of a Diagram Is 1/S
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-2|§C6.8.2]] Feynman Rules for Correlation Functions in Position Space
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-3|§C6.8.3]] Correlation Functions of an Odd Number of Fields Vanish in φ⁴ Theory
- [[§C6.10 Feynman Rules in Momentum Space#^thm-c6-10-1|§C6.10.1]] Momentum Is Conserved at Every Vertex
- [[§C6.10 Feynman Rules in Momentum Space#^thm-c6-10-2|§C6.10.2]] Feynman Rules for Correlation Functions in Momentum Space
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-1|§C6.11.1]] The T(1 − iε) Limit Is the Feynman Prescription
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-2|§C6.11.2]] The Denominator Is the Sum of the Vacuum Diagrams
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-3|§C6.11.3]] Every Vacuum Bubble Is Proportional to the Volume of Spacetime
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|§C6.11.4]] The Numerator Factorizes
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-5|§C6.11.5]] Vacuum Bubbles Cancel

## Models
- [[§C6.1 From Free to Interacting Fields#^mod-c6-1-1|§C6.1.1]] $\phi^4$ Theory
