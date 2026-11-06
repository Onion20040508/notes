---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
tags: [chapter, quantum-field-theory]
---
# C6d Feynman Rules for Fermions
← [[· C6c Feynman Rules for Amplitudes]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (3), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (9), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (8), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (2), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (25), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (62), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (37), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (16), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (79), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (2), [[· CA Mathematical Methods|CA Mathematical Methods]] (27)
**Used by:** [[· C1a Preliminaries|C1a Preliminaries]] (1), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (1), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (4), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (8)

C6d states the **Feynman rules for theories with fermions** (Lecture 17, "Yukawa Theory", PS §4.1 and §4.7; the user's notes, Lecture 17 update), rebuilt on 2026-11-05 after Yu §7.1–§7.2 so that §C6d.2–§C6d.6 mirror C6c §C6c.2–§C6c.6 box by box, each fermion box naming its scalar twin: Yukawa theory, the vertex $-ig$ read off $\mathcal L_{\rm int}$, fermion-number arrows and renormalizability (§C6d.1); the four external fermion wave functions $u$, $\bar u$, $\bar v$, $v$, several fields on one state contracted from the inside out, the $n!$ contractions of identical fermions with the signs of the permutations, and fermion lines as spinor chains (§C6d.2); Wick's theorem with fermion signs, the sign of a term as a count of crossing contractions, and Yu's contraction rule (§C6d.3); first order: the Wick split, ★ the eight three-leg matrix elements, the rules read off them, no $\frac{1}{3!}$ at the vertex, the kinematic filter (two of ten processes), the decay $\phi \to f\bar f$ and ★ its width, internal lines, real and virtual particles, loops, the $-1$ and trace of a closed fermion loop with ★ the tadpoles, and no symmetry factors (§C6d.4); second order: the fourteen Wick terms, the $\frac{1}{2!}$, ★ $f\bar f \to f\bar f$, $ff \to ff$, ★ $f\bar f \to \phi\phi$, the relative-sign rule and the interference term, and ★ disconnected terms, self-energies, closed loops and bubbles (§C6d.5); the momentum-space rules for $i\mathcal M$, with only the vertex theory-specific and relative signs still taken from the contractions (§C6d.6); and ★ the nonrelativistic limit, the attractive Yukawa potential (§C6d.7★, PS pp. 121–123, ahead of the lecture). The QED rules of Lecture 18 join this chapter after §C6d.6; processes follow in C8. The logic of the rules is that of [[· C6c Feynman Rules for Amplitudes]] and §C6b.1; the Dirac propagator $S_F$ is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] (derived there from the mode expansion and from $D_F$).

## How C6d relates to Yu and PS
C6d follows Yu §7.1–§7.2 in its structure (user decision 2026-11-05, as C6c follows Yu ch. 7 for scalars) and the lecture and the user's notes in its taught content; Yu-only material is starred. Yu develops Yukawa theory from first-order $T$-matrix elements, with his bras written in the order of the labels ((7.12), an overall sign different from PS (4.118) and the vault), and lists the momentum-space rules in §7.2; fermionic Wick contractions are in his §6.3, the Dirac propagator in §6.4.5. PS §4.7 is the lecture's reading.

| Section | Mirrors | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|---|
| §C6d.1 | — | §6.1, (6.6)–(6.12); §7.1, (7.1)–(7.5), (7.28), pp. 265–267; §7.2, p. 288 | $\mathcal L_Y = -\kappa\phi\bar\psi\psi$; vertex $-i\kappa\int d^4x$, $i\mathcal L_Y$ with the fields stripped; fermion-number flow | §4.1, (4.9), p. 80; §4.7, (4.112), pp. 115, 120 |
| §C6d.2 | §C6c.2 | §6.3, (6.138)–(6.139); §6.4.5, (6.254)–(6.256); §7.1, (7.8)–(7.20), (7.25)–(7.33); §7.1.2, (7.79)–(7.80) | contractions with initial and final particles, inside out; $n!$ contractions with signs; lines against the arrow | §4.7, (4.114), p. 118 (rule 3), (4.117) |
| §C6d.3 | §C6c.3 | §6.3, (6.140)–(6.144), §6.3.2; §6.4.5, (6.257)–(6.258); §7.1, p. 268, (7.30) | Wick with signs $\epsilon_{ab}$; boxed contraction rule | §4.7, (4.105)–(4.111), (4.118) |
| §C6d.4 | §C6c.4 | §7.1.1, (7.6)–(7.7), (7.21)–(7.58), Fig. 7.1–7.2, pp. 264–273; p. 285 | the ten first-order elements; position-space rules; filter p. 272; width of $\phi \to \psi\bar\psi$; internal lines, real and virtual, loops; tadpoles, closed loop $-1$ | §4.7, p. 118, pp. 119–120, (4.120) |
| §C6d.5 | §C6c.5 | §7.1.2, (7.59)–(7.103), Fig. 7.3–7.11, pp. 273–287 | the 14 second-order terms; $1/n!$ box p. 275; $\psi\bar\psi \to \psi\bar\psi$, $\psi\psi \to \psi\psi$, $\psi\bar\psi \to \phi\phi$; self-energies, loops $n = 2, 3$, bubbles | §4.7, (4.113)–(4.119) |
| §C6d.6 | §C6c.6 | §7.2, rules 1–12 (pp. 287–288), (7.104)–(7.107) | momentum-space rules; only rule 9 theory-specific; relative signs from the contractions | §4.7, p. 118 (rules 1–6), pp. 118–120 |
| §C6d.7★ | — | — | | §4.7, (4.121)–(4.128) |

## Sections
- [[§C6d.1 Yukawa Theory]] — 513 notes Lecture 17 update §17.1–§17.2; PHY 513 Lecture 17, slides 5–8, 26–28; PS §4.1, §4.7
- [[§C6d.2 Contractions with External Fermions]] — 513 notes Lecture 17 update §17.3; PHY 513 Lecture 17, slides 9–12; PS §4.7, pp. 117–119; Yu §7.1, (7.13)–(7.20)
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule]] — 513 notes Lecture 17 update §17.4; PHY 513 Lecture 17, slides 15–17, 21–23; PS §4.7, pp. 115–120; Yu §7.1, p. 268
- [[§C6d.4 First Order]] — Yu §7.1.1, pp. 264–273; PHY 513 Lecture 17, slides 8, 10–12, 16–18; 513 notes Lecture 17 update §17.2, §17.5; PS §4.7, pp. 118–120
- [[§C6d.5 Second Order]] — 513 notes Lecture 17 update §17.6; PHY 513 Lecture 17, slides 19–20, 23; PS §4.7, pp. 116–120; Yu §7.1.2
- [[§C6d.6 Momentum-Space Feynman Rules]] — 513 notes Lecture 17 update §17.5, §17.7; PHY 513 Lecture 17, slides 16–18; PS §4.7, p. 118; Yu §7.2
- [[§C6d.7★ The Yukawa Potential]] — PS §4.7, pp. 121–123 (★)

## Theorems
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|§C6d.1.2]] Fermions Enter in Pairs: No New Signs in the Interaction Picture
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|§C6d.1.3]] The Yukawa Vertex
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|§C6d.1.4]] The Vertex Factor Is iℒ_int with the Fields Stripped
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-5|§C6d.1.5]] Fermion Number Is Conserved at Every Vertex
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-6|§C6d.1.6]] The Renormalizable Interactions of a Scalar and a Dirac Fermion
- [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|§C6d.2.1]] The Four External Fermion Wave Functions
- [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|§C6d.2.2]] Several Fields on One State Contract from the Inside Out
- [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-3|§C6d.2.3]] n Identical Fermion Fields on n Identical Fermions Give the n! Contractions with the Signs of the Permutations
- [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|§C6d.2.4]] A Fermion Line Is a Spinor Chain
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|§C6d.3.1]] Wick's Theorem for Two Fermion Fields; the Fermion Contractions
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|§C6d.3.2]] Wick's Theorem with Fermions
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|§C6d.3.3]] Vacuum Values of Fermion Operator Strings; Crossing Signs
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|§C6d.3.4]] The Sign of a Fully Contracted Term between Particle States
- [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|§C6d.3.5]] The Contraction Rule for T-Matrix Elements with Fermions
- [[§C6d.4 First Order#^thm-c6d-4-1|§C6d.4.1]] The Wick Split of the First-Order Term
- [[§C6d.4 First Order#^thm-c6d-4-2|§C6d.4.2]] ★ The Eight Three-Leg First-Order Matrix Elements
- [[§C6d.4 First Order#^thm-c6d-4-3|§C6d.4.3]] The External-Line and Vertex Rules Read Off at First Order
- [[§C6d.4 First Order#^thm-c6d-4-4|§C6d.4.4]] The Yukawa Vertex Carries No Combinatorial Factor
- [[§C6d.4 First Order#^thm-c6d-4-5|§C6d.4.5]] The Kinematic Filter in Yukawa Theory: Two of Ten
- [[§C6d.4 First Order#^thm-c6d-4-6|§C6d.4.6]] A Closed Fermion Loop Gives −1 and a Trace
- [[§C6d.4 First Order#^thm-c6d-4-7|§C6d.4.7]] Yukawa Diagrams Have No Symmetry Factors
- [[§C6d.5 Second Order#^thm-c6d-5-1|§C6d.5.1]] The Fourteen Second-Order Wick Terms of Yukawa Theory
- [[§C6d.5 Second Order#^thm-c6d-5-2|§C6d.5.2]] The 1/2! Cancels the Exchange x ↔ y; Vertices Move as Even Packages
- [[§C6d.5 Second Order#^thm-c6d-5-3|§C6d.5.3]] The Relative Sign from Fermi Statistics
- [[§C6d.5 Second Order#^thm-c6d-5-4|§C6d.5.4]] The Relative Sign: Minus for Exchanged Fermions, Plus for Exchanged Bosons
- [[§C6d.5 Second Order#^thm-c6d-5-5|§C6d.5.5]] The Relative Sign Fixes the Sign of the Interference Term
- [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|§C6d.6.1]] The Fermion Line Factors Come from the Free Dirac Field; Only the Vertex Is Theory-Specific
- [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|§C6d.6.2]] Feynman Rules for iℳ in Yukawa Theory
- [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-1|§C6d.7.1]] Spinor Products in the Nonrelativistic Limit
- [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-2|§C6d.7.2]] The Nonrelativistic Amplitude for Distinguishable Fermions
- [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-3|§C6d.7.3]] The Yukawa Potential
- [[§C6d.7★ The Yukawa Potential#^thm-c6d-7-4|§C6d.7.4]] Scalar Exchange Is Universally Attractive

## Models
- [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|§C6d.1.1]] Yukawa Theory
