---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
tags: [chapter, quantum-field-theory]
---
# C6c Feynman Rules for Amplitudes
← [[· C6b The S-Matrix and Observables]] · ↑ [[Quantum Field Theory]] · [[· C6d Feynman Rules for Fermions]] →

**Builds on:** [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (26), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (30), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (170), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (50), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (8), [[· CA Mathematical Methods|CA Mathematical Methods]] (49)
**Used by:** [[· C1a Preliminaries|C1a Preliminaries]] (1), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (20), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (17), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (79), [[· C8 Quantum Electrodynamics|C8 Quantum Electrodynamics]] (8), [[· CA Mathematical Methods|CA Mathematical Methods]] (1)

C6c computes **scattering amplitudes from the Dyson series between particle states**, rebuilt after Yu ch. 7 (user decision 2026-11-05) with $\phi^4$ as the running theory, as in Yu §7.3 (Lecture 16, Parts B–C, and Problem Set 8; the user's notes, Lecture 16 update): amplitudes as amputated correlation functions, the course's first statement of the rule (§C6c.1, end of Lecture 15), the contraction of fields with external particles and the $n!$ of identical particles (§C6c.2), Wick's theorem between particle states and Yu's contraction rule, the $\delta$-line, one momentum delta per connected piece (§C6c.3), first order: enumerate the matrix elements, then filter them kinematically, the $4!$ of the vertex, the symmetry factor as the leftover factor, what is not scattering (§C6c.4), second order: every Wick term sorted, the $\frac{1}{n!}$ against the vertex relabellings, amputation, the one-loop $2 \to 2$ amplitude, symmetry factors with the particles held fixed and $S = 1$ for trees (§C6c.5), the collected Feynman rules for $i\mathcal M$ with the $s$-, $t$-, $u$-channels (§C6c.6), particle production by a classical source, the exact case (§C6c.7), and worked translations of questions into formulas (§C6c.8, [[§C6c.8 From the Question to the Formula|From the Question to the Formula]]; procedures [[P5 Symmetry Factor of a Diagram|P5]]–[[P7 From ℳ to σ or Γ|P7]]). The $S$-matrix, cross sections and decay rates are in [[· C6b The S-Matrix and Observables]]; correlation functions and their rules in [[· C6a Interactions and Correlation Functions]]; the same route with fermions, section by section, in [[· C6d Feynman Rules for Fermions]].

## How C6c relates to Yu
C6c follows Yu's ch. 7 method: contractions with initial and final particles, then order by order (first, then second) the Wick terms, the processes they allow and the kinematic filter, with the Feynman rules read off where they first appear and collected last (§7.1–§7.3); every lesson Yu sets apart in a box (the contraction rule p. 268, the $\frac{1}{n!}$ rule p. 275, the $n!$ rule p. 281, the symmetry-factor rule p. 293) is a statement box here. Where Yu checks a rule case by case, the proof is a general theorem of C6a or §CA.7–§CA.8 (orbit–stabilizer). Course order is kept: §C6c.1 is the end of Lecture 15, §C6c.2–§C6c.6 are Lecture 16, Parts B–C. Course conventions throughout (relativistic normalization, the bra order of the course); Yu's differing conventions appear only as cautions.

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6c.1 | §10.3, (10.107), (10.121); §10.5.2–§10.5.3, (10.224)–(10.235) | LSZ; amputated diagrams with $\sqrt Z$ | §4.5, (4.58); §4.6, p. 108 |
| §C6c.2 | §7.1, (7.13)–(7.20); §7.1.2, (7.86)–(7.87), p. 281; §7.4, (7.133)–(7.138) | contractions of fields with initial and final particles; $n$ identical fields on $n$ identical particles | §4.6, (4.93)–(4.94), p. 110 |
| §C6c.3 | §7.1, p. 268; §7.1.2, p. 283, Fig. 7.7 | the boxed contraction rule; disconnected terms do not contribute | §4.6, (4.91), (4.95)–(4.96), pp. 109–111 |
| §C6c.4 | §7.1.1, (7.21)–(7.43), p. 272; §7.3, (7.112)–(7.125), pp. 291–294 | all first-order $T$-matrix elements, then the kinematic filter; the $4!$ of the vertex; the leftover factor is $\frac1S$ | §4.6, (4.92)–(4.98), pp. 109–112 |
| §C6c.5 | §7.1.2, (7.60)–(7.73), p. 275; §7.3, (7.126)–(7.132), p. 294 | second-order terms process by process; the $\frac{1}{n!}$ rule; self-energies $S = 4, 6, 4$; trees $S = 1$ | §4.6, (4.101)–(4.102), pp. 112–114 |
| §C6c.6 | §7.2, rules 1–12 (pp. 287–288); §7.3, p. 292, p. 296; §7.4, rules 1–5 (p. 300); §10.5.3 (amputation with $\sqrt Z$) | momentum-space rules; only the vertex depends on the interaction | §4.6, (4.103)–(4.104), pp. 114–115 |
| §C6c.7 | — (Yu has no classical-source problem) | | Problem 4.1; §2.4, (2.61)–(2.66) |
| §C6c.8 | — (worked translations; uses §6.5, (6.383), (6.385)) | | §4.5, (4.79), (4.84)–(4.86); Problems 4.1–4.2 |

## Sections
- [[§C6c.1 Amplitudes from Correlation Functions]] — 513 notes Ch. 15 §15.9–§15.10; PS §4.5, p. 99; §4.6, p. 108
- [[§C6c.2 Contractions with External Particles]] — PS §4.6, pp. 109–111; Yu §7.1, p. 281, §7.4; PHY 513 Lecture 16, Part B; PHY 513 Problem Set 8, Problem 3
- [[§C6c.3 Wick's Theorem between Particle States]] — PS §4.6, pp. 109–111; Yu §7.1, p. 268, §7.1.2; PHY 513 Lecture 16, Part B
- [[§C6c.4 First Order꞉ Enumerate, then Filter]] — Yu §7.1.1, §7.3, pp. 291–294; PS §4.6, pp. 109–112; PHY 513 Lecture 16, Part B; PHY 513 Problem Set 8, Problem 4
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors]] — Yu §7.1.2, §7.3, pp. 294–296; PS §4.6, pp. 112–114; PHY 513 Lecture 16, Part C; PHY 513 Problem Set 8, Problem 2(c)
- [[§C6c.6 Feynman Rules for Amplitudes]] — PS §4.6, pp. 112–115; Yu §7.2–§7.4; PHY 513 Lecture 16, Part C; PHY 513 Problem Set 8, Problem 2
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route]] — PHY 513 Problem Set 8, Problem 3; PS Problem 4.1
- [[§C6c.8 From the Question to the Formula]] — PHY 513 Problem Set 8, Problems 2–4; PS §4.5, pp. 106–108

## Theorems
- [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|§C6c.1.1]] Amplitudes Are Amputated Correlation Functions
- [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|§C6c.1.2]] The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
- [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|§C6c.2.1]] Contraction of Fields with Outgoing Particles
- [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|§C6c.2.2]] Contraction of Fields with Incoming Particles
- [[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|§C6c.2.3]] n Identical Fields on n Identical Particles Give the n! Contractions
- [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|§C6c.2.4]] In and Out Are One Contraction Read Both Ways; a Vertex Collects the Momenta
- [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|§C6c.3.1]] Wick's Theorem between Particle States
- [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-2|§C6c.3.2]] The Contraction Rule for S-Matrix Elements
- [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|§C6c.3.3]] Every Connected Piece Carries Its Own Momentum Delta
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|§C6c.4.1]] The First-Order Matrix Elements of a Monomial
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|§C6c.4.2]] The Kinematic Filter
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-3|§C6c.4.3]] The Interaction Decides Which Processes Have a Matrix Element; Kinematics Decides Which Happen
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|§C6c.4.4]] The φ⁴ Vertex Carries No Combinatorial Factor
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|§C6c.4.5]] The Factor Left Over in a Matrix Element Is 1/S
- [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|§C6c.4.6]] δ-Lines, Forward Pieces and Vacuum Bubbles Are Not Scattering
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-1|§C6c.5.1]] The Second-Order Terms of φ⁴ Theory
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|§C6c.5.2]] The 1/n! Cancels the Relabellings of the Vertices
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|§C6c.5.3]] External-Leg Corrections Are Removed by Amputation; the Rest Is the T-Matrix Element
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|§C6c.5.4]] With the Particles Held Fixed, S Comes Only from Self-Loops, Parallel Lines and Vertices without Particles
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|§C6c.5.5]] Vertices Saturated by External Lines Give S = 1
- [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|§C6c.5.6]] Tree Diagrams of a Process Have S = 1
- [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|§C6c.6.1]] The Line Factors Come from the Free Fields; the Interaction Fixes Only the Vertex
- [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|§C6c.6.2]] Tree-Level Feynman Rules for iℳ
- [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|§C6c.6.3]] Feynman Rules for iℳ, All Orders
- [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|§C6c.6.4]] Tree Diagrams of a Process; the s-, t-, u-Channels
- [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|§C6c.6.6]] The Vertex Content Decides Which Channels Exist
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-1|§C6c.7.1]] The Vacuum-Persistence Amplitude of a Source
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-2|§C6c.7.2]] The No-Particle Probability to Order j²
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-3|§C6c.7.3]] The Vacuum Series of a Source Exponentiates
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-4|§C6c.7.4]] The One-Particle Amplitude
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|§C6c.7.5]] The Measure on n-Particle States
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-6|§C6c.7.6]] The Number of Particles Is Poisson Distributed
- [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-7|§C6c.7.7]] Normalization, Mean and Variance

## Models
- [[§C6c.6 Feynman Rules for Amplitudes#^mod-c6c-6-5|§C6c.6.5]] The Three-Scalar Theory
