---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
tags: [chapter, quantum-field-theory]
---
# C6a Interactions and Correlation Functions
← [[· C5b The Quantum Spinor Field]] · ↑ [[Quantum Field Theory]] · [[· C6b The S-Matrix, Amplitudes and Observables]] →

**Builds on:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (32), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (28), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (102), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (8), [[· C6b The S-Matrix, Amplitudes and Observables|C6b The S-Matrix, Amplitudes and Observables]] (1), [[· CA Mathematical Methods|CA Mathematical Methods]] (88), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (9)
**Used by:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (2), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (2), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (2), [[· C6b The S-Matrix, Amplitudes and Observables|C6b The S-Matrix, Amplitudes and Observables]] (36), [[· CA Mathematical Methods|CA Mathematical Methods]] (11)

C6a computes **correlation functions** $\langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}|\Omega\rangle$ of an interacting theory, with $\phi^4$ theory as the course's first case (Lectures 13–14; the user's notes, Ch. 13–14). The interaction picture and the Dyson series write them through free fields (§C6a.1–§C6a.4, master formula [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]]); Wick's theorem turns the free vacuum values into sums over contractions (§C6a.5–§C6a.6); diagrams and the Feynman rules in position and momentum space, with their symmetry factors, organize the sum, and the $i\varepsilon$ limit cancels the vacuum bubbles (§C6a.7–§C6a.11). Correlation functions are not what an experiment measures: $S$-matrix elements, the invariant amplitude $\mathcal M$, cross sections and decay rates are computed in [[· C6b The S-Matrix, Amplitudes and Observables]], which reads $\mathcal M$ off from the amputated correlation functions of this chapter. In Yu's book the material of C6a is in §6.1–§6.3 and §10.4–§10.5.

## How C6a relates to Yu
C6a follows the course (Lectures 13–14) and the user's notes (Ch. 13–14), not Yu's chapter split (user decisions, 2026-10-26 and 2026-10-28). Yu treats Wick's theorem in §6.3, the Feynman rules for $S$-matrix elements in ch. 7 (Yukawa first, §7.2; $\phi^4$ and symmetry factors, §7.3), and reaches correlation functions and the cancellation of vacuum bubbles only in ch. 10, through asymptotic in-fields and the LSZ formula; the course reaches them through the $i\varepsilon$ projection onto the interacting vacuum (§C6a.4). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6a.1 | Ch. 6 opening, (6.1)–(6.5), (6.13); §6.1.1, (6.39)–(6.46) | | §4.1 |
| §C6a.2 | §6.1, (6.22)–(6.38), (6.44)–(6.50) | $V(t) = e^{iH_0t}e^{-iHt}$ | §4.2 |
| §C6a.3 | §6.2, (6.93)–(6.121) | $U(t, t_0)$, Dyson series; $S = U(\infty, -\infty)$ (6.122)–(6.125) | §4.2 |
| §C6a.4 | §10.4, (10.176)–(10.181) (another route) | in-fields and LSZ; normalization a phase | §4.2 |
| §C6a.5 | §6.3.1, (6.131)–(6.165) | bosons and fermions together | §4.3, (4.32)–(4.37) |
| §C6a.6 | §6.3.1, (6.166)–(6.168); §6.3.2, lemma (6.169)–(6.170), proofs (6.171)–(6.193) | lemma appends an earlier field | §4.3, (4.38)–(4.41) |
| §C6a.7 | §10.5.1, (10.187)–(10.192) | $G^{(2)}$ of in-fields, with a $\delta m^2$ vertex | §4.4, (4.42)–(4.44) |
| §C6a.8 | §7.3, (7.112)–(7.120) | $T$-matrix elements | §4.4, (4.45), p. 94 |
| §C6a.9 | §7.3, (7.124)–(7.125), (7.127)–(7.128), (7.131)–(7.132); p. 293 | self-energies $\langle\mathbf k\rvert iT\lvert\mathbf k\rangle$ | §4.4, pp. 92–93 |
| §C6a.10 | §7.2, rules 8, 10, 11 (pp. 287–288); §7.3, p. 296; §10.5.1, (10.198)–(10.203) | Yukawa $S$-matrix rules; Fourier transform of $G^{(n)}$ | §4.4, (4.46)–(4.47), p. 95 |
| §C6a.11 | §10.4, (10.176)–(10.181); §10.5.1, (10.193)–(10.197) | no $T(1 - i\varepsilon)$; binomial proof | §4.4, (4.48)–(4.57) |
| §CA.7 (mathematics) | (6.167)–(6.168); (7.114)–(7.125) | | §4.3–§4.4 |
| §CA.8 (mathematics) | §10.5.1, (10.192)–(10.196) | | §4.4, pp. 96–98, (4.50)–(4.52) |

## Sections
- [[§C6a.1 From Free to Interacting Fields]] — 513 notes Ch. 13 §13.1; PS §4.1
- [[§C6a.2 The Interaction Picture]] — 513 notes Ch. 13 §13.2; PS §4.2, pp. 83–84
- [[§C6a.3 The Time-Evolution Operator and Time Ordering]] — 513 notes Ch. 13 §13.3; PS §4.2, pp. 84–86
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function]] — 513 notes Ch. 13 §§13.4–13.6; PS §4.2, pp. 86–87
- [[§C6a.5 Normal Ordering and Contractions]] — 513 notes Ch. 14 §14.1–§14.2; PS §4.3, pp. 88–89
- [[§C6a.6 Wick's Theorem]] — 513 notes Ch. 14 §14.2; PS §4.3, pp. 89–90
- [[§C6a.7 Feynman Diagrams for Correlation Functions]] — 513 notes Ch. 14 §14.3; PS §4.4, pp. 90–92
- [[§C6a.8 Position-Space Feynman Rules]] — 513 notes Ch. 14 §14.4–§14.5; PS §4.4, pp. 92–94
- [[§C6a.9 Symmetry Factors in Practice]] — 513 notes Ch. 14 §14.5; PS §4.4, pp. 92–93
- [[§C6a.10 Feynman Rules in Momentum Space]] — 513 notes Ch. 14 §14.6; PS §4.4, pp. 94–95
- [[§C6a.11 The iε Limit and Vacuum Bubbles]] — 513 notes Ch. 14 §14.7–§14.8; PS §4.4, pp. 95–99

## Principles
- [[§C6a.1 From Free to Interacting Fields#^pr-c6a-1-6|§C6a.1.6]] Canonical Quantization of $\phi^4$ Theory at a Reference Time

## Theorems
- [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-2|§C6a.1.2]] The Coupling of $\phi^4$ Theory Is Dimensionless
- [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-3|§C6a.1.3]] The Field Equation of $\phi^4$ Theory
- [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-4|§C6a.1.4]] The Conjugate Momentum Is Unchanged by the Interaction
- [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|§C6a.1.5]] The Hamiltonian of $\phi^4$ Theory and Its Split
- [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-7|§C6a.1.7]] The Ladder Operators Diagonalize the Free Hamiltonian, Not the Full One
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-1|§C6a.2.1]] The Interaction-Picture Field Is the Free Mode Expansion
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-2|§C6a.2.2]] The Interaction-Picture Field Obeys the Free Field Equations
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-3|§C6a.2.3]] Free-Vacuum Correlators of the Interaction-Picture Field Are the Free Ones
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-4|§C6a.2.4]] The Heisenberg Field in Terms of the Interaction-Picture Field
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-5|§C6a.2.5]] U(t) Is Not the Exponential of the Interaction
- [[§C6a.2 The Interaction Picture#^thm-c6a-2-6|§C6a.2.6]] The Interaction Hamiltonian Is the Interaction of the Free Field
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-1|§C6a.3.1]] The Time-Evolution Operator Is Unitary
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|§C6a.3.2]] The Equation of Motion of the Time-Evolution Operator
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-3|§C6a.3.3]] The Interaction Hamiltonians at Two Times
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-4|§C6a.3.4]] The Exponential Solves the Equation Only for Commuting Generators
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-5|§C6a.3.5]] Ordered Iterated Integrals Are Time-Ordered Cube Integrals
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|§C6a.3.6]] Dyson's Formula
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|§C6a.3.7]] Properties of the Time-Evolution Operator
- [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|§C6a.3.8]] Dyson's Formula Between Two Times
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|§C6a.4.1]] Projection onto the Ground State
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-2|§C6a.4.2]] The Interacting Vacuum Evolved from the Far Past
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-3|§C6a.4.3]] The Conjugate Vacuum Evolved into the Far Future
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|§C6a.4.4]] The Normalization Is the Vacuum-to-Vacuum Amplitude
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-5|§C6a.4.5]] The Two-Point Function as a Chain of Free Evolutions
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|§C6a.4.6]] The Master Formula
- [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|§C6a.4.7]] The n-Point Functions
- [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|§C6a.5.1]] The Normal-Ordered Product of n Free Fields
- [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-2|§C6a.5.2]] The Price of Reordering Is the Wightman Function
- [[§C6a.6 Wick's Theorem#^lem-c6a-6-1|§C6a.6.1]] Appending a Field of Earlier Time
- [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|§C6a.6.2]] Wick's Theorem
- [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|§C6a.6.3]] Free Vacuum Values Are Sums over Pairings
- [[§C6a.6 Wick's Theorem#^thm-c6a-6-4|§C6a.6.4]] ★ Wick's Theorem for Ordinary Products
- [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-1|§C6a.7.1]] The First-Order Numerator
- [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|§C6a.7.2]] Real-Scalar Lines Are Undirected; Complex-Scalar and Dirac Lines Are Oriented
- [[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-3|§C6a.7.3]] The Number of Complete Contractions at Order λⁿ
- [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|§C6a.8.1]] The Coefficient of a Diagram Is 1/S
- [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|§C6a.8.2]] Feynman Rules for Correlation Functions in Position Space
- [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-3|§C6a.8.3]] Correlation Functions of an Odd Number of Fields Vanish in φ⁴ Theory
- [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1|§C6a.9.1]] Symmetry Factors with Oriented Lines
- [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-1|§C6a.10.1]] Momentum Is Conserved at Every Vertex
- [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|§C6a.10.2]] Feynman Rules for Correlation Functions in Momentum Space
- [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-3|§C6a.10.3]] The Loop Factor D_F(0) Diverges Quadratically
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-1|§C6a.11.1]] The T(1 − iε) Limit Is the Feynman Prescription
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|§C6a.11.2]] The Denominator Is the Sum of the Vacuum Diagrams
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|§C6a.11.3]] Every Vacuum Bubble Is Proportional to the Volume of Spacetime
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|§C6a.11.4]] The Numerator Factorizes
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|§C6a.11.5]] Vacuum Bubbles Cancel
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6|§C6a.11.6]] The Denominator Is the Exponential of the Connected Vacuum Bubbles
- [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-7|§C6a.11.7]] The Vacuum Energy Density

## Models
- [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|§C6a.1.1]] $\phi^4$ Theory
