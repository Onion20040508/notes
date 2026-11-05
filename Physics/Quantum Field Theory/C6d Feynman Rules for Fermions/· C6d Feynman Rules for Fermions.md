---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
tags: [chapter, quantum-field-theory]
---
# C6d Feynman Rules for Fermions
← [[· C6c Feynman Rules for Amplitudes]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (3), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (6), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (8), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (2), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (23), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (51), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (34), [[· C6b The S-Matrix, Amplitudes and Observables|C6b The S-Matrix, Amplitudes and Observables]] (12), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (29), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (2), [[· CA Mathematical Methods|CA Mathematical Methods]] (25)
**Used by:** [[· C1a Preliminaries|C1a Preliminaries]] (1), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (1), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (4), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (5)

C6d states the **Feynman rules for theories with fermions** (Lecture 17, "Yukawa Theory", PS §4.1 and §4.7; the user's notes, Lecture 17 update): Yukawa theory, the vertex $-ig$, fermion-number arrows and renormalizability (§C6d.1), the four external fermion wave functions $u$, $\bar u$, $\bar v$, $v$ and fermion lines as spinor chains (§C6d.2), Wick's theorem with fermion signs, the sign of a term as a count of crossing contractions, and the $-1$ of a closed fermion loop (§C6d.3), the rules for $i\mathcal M$, the absence of $\frac{1}{3!}$ at the vertex and of symmetry factors, and the decay $\phi \to f\bar f$ (§C6d.4), fermion–fermion scattering with its relative sign from Fermi statistics (§C6d.5), and ★ the nonrelativistic limit, the attractive Yukawa potential (§C6d.6★, PS pp. 121–123, ahead of the lecture). The QED rules of Lecture 18 join this chapter as later sections; processes follow in C8. The logic of the rules is that of [[· C6b The S-Matrix, Amplitudes and Observables]]; the Dirac propagator $S_F$ is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] (derived there from the mode expansion and from $D_F$).

## How C6d relates to Yu and PS
C6d follows the lecture (slides and transcript) and the user's notes. Yu develops Yukawa theory in §7.1 from first-order $T$-matrix elements, with his bras written in the order of the labels ((7.12), an overall sign different from PS (4.118)), and lists the momentum-space rules in §7.2; fermionic Wick contractions are in his §6.3, the Dirac propagator in §6.4.5. PS §4.7 is the lecture's reading.

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6d.1 | §6.1, (6.6)–(6.12); §7.1, (7.1)–(7.5), (7.28), pp. 265–267 | $\mathcal L_Y = -\kappa\phi\bar\psi\psi$; vertex $-i\kappa\int d^4x$; fermion-number flow | §4.1, (4.9), p. 80; §4.7, (4.112), pp. 115, 120 |
| §C6d.2 | §6.3, (6.138)–(6.139); §6.4.5, (6.254)–(6.256); §7.1, (7.8)–(7.20), (7.25)–(7.33) | contractions of fields with initial and final particles; lines written against the arrow | §4.7, (4.114), p. 118 (rule 3), (4.117) |
| §C6d.3 | §6.3, (6.140)–(6.144), §6.3.2; §6.4.5, (6.257)–(6.258); §7.1, p. 268, (7.42), (7.100)–(7.101) | Wick with signs $\epsilon_{ab}$; boxed contraction rule; closed loops $-1$, trace | §4.7, (4.105)–(4.111), (4.118)–(4.120) |
| §C6d.4 | §7.1, (7.23)–(7.24), (7.34), (7.44), p. 272, p. 275; §7.2, rules 1–12 (pp. 287–288) | rules read off first-order $T$-matrix elements; $1/n!$ cancels except for bubbles | §4.7, p. 118 (rules 1–6), pp. 118–120 |
| §C6d.5 | §7.1.2, (7.59), (7.78)–(7.82), Fig. 7.4–7.5 | $\psi\psi \to \psi\psi$, relative sign from antisymmetry | §4.7, (4.113)–(4.119) |
| §C6d.6★ | — | | §4.7, (4.121)–(4.128) |

## Sections
- [[§C6d.1 Yukawa Theory]] — 513 notes Lecture 17 update §17.1–§17.2; PHY 513 Lecture 17, slides 5–8, 26–28; PS §4.1, §4.7
- [[§C6d.2 External Fermions]] — 513 notes Lecture 17 update §17.3; PHY 513 Lecture 17, slides 9–12; PS §4.7, pp. 117–119
- [[§C6d.3 Wick's Theorem with Fermions]] — 513 notes Lecture 17 update §17.4; PHY 513 Lecture 17, slides 15–17, 21–23; PS §4.7, pp. 115–120
- [[§C6d.4 Feynman Rules for Yukawa Theory]] — 513 notes Lecture 17 update §17.5; PHY 513 Lecture 17, slides 16–18; PS §4.7, p. 118; Yu §7.2
- [[§C6d.5 Fermion–Fermion Scattering]] — 513 notes Lecture 17 update §17.6; PHY 513 Lecture 17, slides 19–20; PS §4.7, pp. 116–120
- [[§C6d.6★ The Yukawa Potential]] — PS §4.7, pp. 121–123 (★)

## Theorems
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|§C6d.1.2]] Fermions Enter in Pairs: No New Signs in the Interaction Picture
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|§C6d.1.3]] The Yukawa Vertex
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|§C6d.1.4]] Fermion Number Is Conserved at Every Vertex
- [[§C6d.1 Yukawa Theory#^thm-c6d-1-5|§C6d.1.5]] The Renormalizable Interactions of a Scalar and a Dirac Fermion
- [[§C6d.2 External Fermions#^thm-c6d-2-1|§C6d.2.1]] The Four External Fermion Wave Functions
- [[§C6d.2 External Fermions#^thm-c6d-2-2|§C6d.2.2]] A Fermion Line Is a Spinor Chain
- [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-1|§C6d.3.1]] Wick's Theorem for Two Fermion Fields; the Fermion Contractions
- [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-2|§C6d.3.2]] Wick's Theorem with Fermions
- [[§C6d.3 Wick's Theorem with Fermions#^lem-c6d-3-3|§C6d.3.3]] Vacuum Values of Fermion Operator Strings; Crossing Signs
- [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|§C6d.3.4]] The Sign of a Fully Contracted Term between Particle States
- [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-5|§C6d.3.5]] A Closed Fermion Loop Gives −1 and a Trace
- [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|§C6d.4.1]] Feynman Rules for iℳ in Yukawa Theory
- [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-2|§C6d.4.2]] The Yukawa Vertex Carries No Combinatorial Factor
- [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|§C6d.4.3]] Yukawa Diagrams Have No Symmetry Factors
- [[§C6d.5 Fermion–Fermion Scattering#^thm-c6d-5-1|§C6d.5.1]] The Relative Sign from Fermi Statistics
- [[§C6d.6★ The Yukawa Potential#^thm-c6d-6-1|§C6d.6.1]] Spinor Products in the Nonrelativistic Limit
- [[§C6d.6★ The Yukawa Potential#^thm-c6d-6-2|§C6d.6.2]] The Nonrelativistic Amplitude for Distinguishable Fermions
- [[§C6d.6★ The Yukawa Potential#^thm-c6d-6-3|§C6d.6.3]] The Yukawa Potential
- [[§C6d.6★ The Yukawa Potential#^thm-c6d-6-4|§C6d.6.4]] Scalar Exchange Is Universally Attractive

## Models
- [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|§C6d.1.1]] Yukawa Theory
