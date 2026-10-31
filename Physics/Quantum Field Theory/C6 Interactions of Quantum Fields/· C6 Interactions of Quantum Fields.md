---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6
tags: [chapter, quantum-field-theory]
---
# C6 Interactions of Quantum Fields
← [[· C5b The Quantum Spinor Field]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (16), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (33), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (63), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (118), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (8), [[· CA Mathematical Methods|CA Mathematical Methods]] (139), [[· CB Lie Groups, Lie Algebras and Representations|CB Lie Groups, Lie Algebras and Representations]] (9)
**Used by:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (2), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (2), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (2), [[· CA Mathematical Methods|CA Mathematical Methods]] (12)

## How C6 relates to Yu
C6 follows the course (Lectures 13–15) and the user's notes (Ch. 13–15), not Yu's chapter split (user decisions, 2026-10-26 and 2026-10-28). Yu treats Wick's theorem in §6.3, the Feynman rules for $S$-matrix elements in ch. 7 (Yukawa first, §7.2; $\phi^4$ and symmetry factors, §7.3), and reaches correlation functions and the cancellation of vacuum bubbles only in ch. 10, through asymptotic in-fields and the LSZ formula; the course reaches them through the $i\varepsilon$ projection onto the interacting vacuum (§C6.4). For the $S$-matrix, cross sections and decay rates (§C6.12–§C6.17, Lecture 15) Yu uses box normalization and squares the delta function, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, where the course uses wave packets; he derives the width in the propagator from the self-energy (§10.6) and the amputation rule from LSZ (§10.3, §10.5.3). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

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
| §C6.12 | §6.2, (6.122)–(6.127); §6.5, (6.272)–(6.275) | $S = U(+\infty, -\infty)$ between asymptotic states; $S = \mathbb I + iT$ | §4.5, (4.70)–(4.73) |
| §C6.13 | §6.5.1, (6.276); §6.5.2, (6.308), (6.313), (6.321) | cross section as an event rate per flux; no wave packets | §4.5, (4.59)–(4.61), (4.65)–(4.75) |
| §C6.14 | §6.5.1–§6.5.2, (6.276)–(6.313), (6.320)–(6.321) | box normalization, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$; beam on a fixed target | §4.5, (4.76)–(4.79) |
| §C6.15 | §6.5.2–§6.5.3, (6.314)–(6.366) | Møller velocity; Källén function | §4.5, (4.80)–(4.85) |
| §C6.16 | §6.5.4–§6.5.5, (6.367)–(6.385); §10.6, (10.259)–(10.275) | box route to $\Gamma_f$; width from $\operatorname{Im}\Pi$ | §4.5, (4.62)–(4.64), (4.86) |
| §C6.17 | §10.3, (10.107), (10.121); §10.5.2–§10.5.3, (10.224)–(10.235) | LSZ; amputated diagrams with $\sqrt Z$ | §4.5, (4.58); §4.6, p. 108 |
| §C6.18 | — (Yu has no classical-source problem) | | Problem 4.1; §2.4, (2.61)–(2.66) |
| §CA.7 (mathematics) | (6.167)–(6.168); (7.114)–(7.125) | | §4.3–§4.4 |
| §CA.8 (mathematics) | §10.5.1, (10.192)–(10.196) | | §4.4, pp. 96–98, (4.50)–(4.52) |

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
- [[§C6.12 The S-Matrix and the Invariant Amplitude]] — 513 notes Ch. 15 §15.1; PS §4.5, pp. 102–104
- [[§C6.13 Wave Packets and the Cross Section]] — 513 notes Ch. 15 §15.2–§15.3; PS §4.5, pp. 99–105
- [[§C6.14 Evaluating the Cross Section]] — 513 notes Ch. 15 §15.4–§15.5; PS §4.5, pp. 104–106, 108
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space]] — 513 notes Ch. 15 §15.6–§15.7; PS §4.5, pp. 106–107
- [[§C6.16 Decay Rates and Widths]] — 513 notes Ch. 15 §15.8; PS §4.5, pp. 101, 107–108
- [[§C6.17 Amplitudes from Correlation Functions]] — 513 notes Ch. 15 §15.9–§15.10; PS §4.5, p. 99; §4.6, p. 108
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route]] — PHY 513 Problem Set 8, Problem 3; PS Problem 4.1

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
- [[§C6.2 The Interaction Picture#^thm-c6-2-5|§C6.2.5]] U(t) Is Not the Exponential of the Interaction
- [[§C6.2 The Interaction Picture#^thm-c6-2-6|§C6.2.6]] The Interaction Hamiltonian Is the Interaction of the Free Field
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-1|§C6.3.1]] The Time-Evolution Operator Is Unitary
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-2|§C6.3.2]] The Equation of Motion of the Time-Evolution Operator
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-3|§C6.3.3]] The Interaction Hamiltonians at Two Times
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-4|§C6.3.4]] The Exponential Solves the Equation Only for Commuting Generators
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-5|§C6.3.5]] Ordered Iterated Integrals Are Time-Ordered Cube Integrals
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-6|§C6.3.6]] Dyson's Formula
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-7|§C6.3.7]] Properties of the Time-Evolution Operator
- [[§C6.3 The Time-Evolution Operator and Time Ordering#^thm-c6-3-8|§C6.3.8]] Dyson's Formula Between Two Times
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
- [[§C6.6 Wick's Theorem#^thm-c6-6-4|§C6.6.4]] ★ Wick's Theorem for Ordinary Products
- [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|§C6.7.1]] The First-Order Numerator
- [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-2|§C6.7.2]] Real-Scalar Lines Are Undirected; Complex-Scalar and Dirac Lines Are Oriented
- [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-3|§C6.7.3]] The Number of Complete Contractions at Order λⁿ
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|§C6.8.1]] The Coefficient of a Diagram Is 1/S
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-2|§C6.8.2]] Feynman Rules for Correlation Functions in Position Space
- [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-3|§C6.8.3]] Correlation Functions of an Odd Number of Fields Vanish in φ⁴ Theory
- [[§C6.9 Symmetry Factors in Practice#^thm-c6-9-1|§C6.9.1]] Symmetry Factors with Oriented Lines
- [[§C6.10 Feynman Rules in Momentum Space#^thm-c6-10-1|§C6.10.1]] Momentum Is Conserved at Every Vertex
- [[§C6.10 Feynman Rules in Momentum Space#^thm-c6-10-2|§C6.10.2]] Feynman Rules for Correlation Functions in Momentum Space
- [[§C6.10 Feynman Rules in Momentum Space#^thm-c6-10-3|§C6.10.3]] The Loop Factor D_F(0) Diverges Quadratically
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-1|§C6.11.1]] The T(1 − iε) Limit Is the Feynman Prescription
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-2|§C6.11.2]] The Denominator Is the Sum of the Vacuum Diagrams
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-3|§C6.11.3]] Every Vacuum Bubble Is Proportional to the Volume of Spacetime
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|§C6.11.4]] The Numerator Factorizes
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-5|§C6.11.5]] Vacuum Bubbles Cancel
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-6|§C6.11.6]] The Denominator Is the Exponential of the Connected Vacuum Bubbles
- [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-7|§C6.11.7]] The Vacuum Energy Density
- [[§C6.12 The S-Matrix and the Invariant Amplitude#^thm-c6-12-1|§C6.12.1]] S-Matrix Elements and the Interaction-Picture Evolution Operator
- [[§C6.12 The S-Matrix and the Invariant Amplitude#^thm-c6-12-2|§C6.12.2]] The S-Matrix Conserves Four-Momentum
- [[§C6.12 The S-Matrix and the Invariant Amplitude#^thm-c6-12-3|§C6.12.3]] The Mass Dimension of the Amplitude
- [[§C6.12 The S-Matrix and the Invariant Amplitude#^thm-c6-12-4|§C6.12.4]] The Amplitude of Spinless Particles Is Lorentz Invariant
- [[§C6.12 The S-Matrix and the Invariant Amplitude#^thm-c6-12-5|§C6.12.5]] Spinless 2 → 2 Kinematics in Terms of s and t
- [[§C6.13 Wave Packets and the Cross Section#^thm-c6-13-1|§C6.13.1]] The Normalization Condition Is the Unit Norm
- [[§C6.13 Wave Packets and the Cross Section#^thm-c6-13-2|§C6.13.2]] The Phase Displaces the Packet by b
- [[§C6.13 Wave Packets and the Cross Section#^thm-c6-13-3|§C6.13.3]] The Quantum Cross Section Is the Event Rate per Unit Flux
- [[§C6.13 Wave Packets and the Cross Section#^lem-c6-13-4|§C6.13.4]] Away from the Forward Direction Only iT̂ Contributes
- [[§C6.14 Evaluating the Cross Section#^thm-c6-14-1|§C6.14.1]] The Longitudinal Integrals Give the Velocity Difference
- [[§C6.14 Evaluating the Cross Section#^thm-c6-14-2|§C6.14.2]] The Cross Section for 2 → n Scattering
- [[§C6.14 Evaluating the Cross Section#^thm-c6-14-3|§C6.14.3]] The Cross Section Is an Area for Every n
- [[§C6.14 Evaluating the Cross Section#^thm-c6-14-4|§C6.14.4]] Identical Particles in the Final State
- [[§C6.14 Evaluating the Cross Section#^thm-c6-14-5|§C6.14.5]] The Scattering Probabilities Add Up to One
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-1|§C6.15.1]] The Flux Factor Is a Component of an Antisymmetric Tensor
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-2|§C6.15.2]] The Cross Section Transforms Like an Area
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-3|§C6.15.3]] The Flux Factor in Invariant Form
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-4|§C6.15.4]] The Phase Space Is Lorentz Invariant
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-5|§C6.15.5]] Two-Body Phase Space in the Centre-of-Mass Frame
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-6|§C6.15.6]] The Centre-of-Mass Momentum
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-7|§C6.15.7]] The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
- [[§C6.15 Lorentz Invariance and Two-Body Phase Space#^thm-c6-15-8|§C6.15.8]] All Masses Equal
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-1|§C6.16.1]] The Decay Rate Formula
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-2|§C6.16.2]] Two-Body Decays
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-3|§C6.16.3]] ★ Partial Widths Add
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-5|§C6.16.5]] The Propagator Near Its Pole
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-6|§C6.16.6]] The Width Is Invariant; the Decay Rate Is Time-Dilated
- [[§C6.16 Decay Rates and Widths#^thm-c6-16-7|§C6.16.7]] The Breit–Wigner Shape and Its Width
- [[§C6.17 Amplitudes from Correlation Functions#^thm-c6-17-1|§C6.17.1]] Amplitudes Are Amputated Correlation Functions
- [[§C6.17 Amplitudes from Correlation Functions#^thm-c6-17-2|§C6.17.2]] The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
- [[§C6.17 Amplitudes from Correlation Functions#^thm-c6-17-3|§C6.17.3]] Vertex Factors of a Polynomial Interaction
- [[§C6.17 Amplitudes from Correlation Functions#^thm-c6-17-4|§C6.17.4]] Vertices Saturated by External Lines Give S = 1
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-1|§C6.18.1]] The Vacuum-Persistence Amplitude of a Source
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-2|§C6.18.2]] The No-Particle Probability to Order j²
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-3|§C6.18.3]] The Vacuum Series of a Source Exponentiates
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6-18-4|§C6.18.4]] Contraction of Fields with Outgoing Particles
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-5|§C6.18.5]] The One-Particle Amplitude
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-6|§C6.18.6]] The Measure on n-Particle States
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-7|§C6.18.7]] The Number of Particles Is Poisson Distributed
- [[§C6.18 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6-18-8|§C6.18.8]] Normalization, Mean and Variance

## Models
- [[§C6.1 From Free to Interacting Fields#^mod-c6-1-1|§C6.1.1]] $\phi^4$ Theory
- [[§C6.16 Decay Rates and Widths#^mod-c6-16-4|§C6.16.4]] The Propagator of an Unstable Particle
