---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
tags: [chapter, quantum-field-theory]
---
# C6b The S-Matrix, Amplitudes and Observables
← [[· C6a Interactions and Correlation Functions]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (16), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (67), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (21), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (103), [[· CA Mathematical Methods|CA Mathematical Methods]] (73)
**Used by:** [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (1), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (27), [[· CA Mathematical Methods|CA Mathematical Methods]] (1)

C6b computes **$S$-matrix elements and the observables made from them** (Lectures 15–16 and Problem Set 8; the user's notes, Ch. 15 and the Lecture 16 update): the $S$-matrix, the interacting in and out states and the invariant amplitude $\mathcal M$ (§C6b.1), matrix elements between particle states: contractions with external particles, Wick's theorem between particle states, which terms are scattering, the first-order matrix elements (§C6b.2), the Feynman rules for $i\mathcal M$: amputation, the tree-level and all-order rules, the $s$-, $t$-, $u$-channels (§C6b.3), the cross section by Yu's box route, the main line (transition probabilities in a box §C6b.4, the cross section §C6b.5, with every factor of $d\sigma$ labelled by its origin), the same cross section from wave packets, the course's careful version (§C6b.6–§C6b.7), Lorentz invariance and two-body phase space (§C6b.8), decay rates and widths (§C6b.9), amplitudes as amputated correlation functions (§C6b.10, [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]), particle production by a classical source (§C6b.11), and worked translations of questions as asked into the formulas that answer them (§C6b.12, [[§C6b.12 From the Question to the Formula|From the Question to the Formula]]; procedures [[P5 Symmetry Factor of a Diagram|P5]]–[[P7 From ℳ to σ or Γ|P7]]). The correlation functions, Wick's theorem and the Feynman rules it starts from are in [[· C6a Interactions and Correlation Functions]]. In Yu's book the material of C6b is in §6.2, §6.5, ch. 7 (the $S$-matrix rules), §10.3 and §10.6.

## How C6b relates to Yu
C6b follows the course (Lectures 15–16) and the user's notes (Ch. 15, Lecture 16 update), except for the cross section: by the user's decision of 2026-10-31 Yu's box route is the main line (§C6b.4–§C6b.5, "from what setup we arrived at the cross section, step by step"), and the course's wave-packet route follows as the careful version (§C6b.6–§C6b.7). Yu uses box normalization and squares the delta function, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, where the course uses wave packets; every section of C6b opens with a Model box or a setup paragraph saying which Hamiltonian, which states and which vacuum it assumes; he derives the width in the propagator from the self-energy (§10.6) and the amputation rule from LSZ (§10.3, §10.5.3). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6b.1 | §6.2, (6.122)–(6.127); §6.5, (6.272)–(6.275) | $S = U(+\infty, -\infty)$ between asymptotic states; $S = \mathbb I + iT$ | §4.5, (4.70)–(4.73) |
| §C6b.2 | §7.1, (7.13)–(7.24), p. 268, p. 272, (7.86)–(7.87), p. 281; §7.3, (7.115)–(7.121); §7.4, (7.135)–(7.142) | contractions of fields with initial and final particles; all first-order $T$-matrix elements, then the kinematic filter | §4.6, (4.89)–(4.98), pp. 109–113 |
| §C6b.3 | §7.2, rules 6–11 (pp. 287–288); §7.3, p. 294, p. 296; §7.4, rules 1–5 (p. 300); §10.5.3 (amputation with $\sqrt Z$) | rules read off the first-order $T$-matrix elements; tree diagrams $S = 1$ | §4.6, (4.101)–(4.104), pp. 112–115 |
| §C6b.4 | §6.5.1, (6.276)–(6.306) | box normalization, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$; transition probability, rate, counting of final states | §4.4, p. 96 |
| §C6b.5 | §6.5.2, (6.307)–(6.331) | beam on a fixed target, flux, $\sigma$, Møller velocity, $d\Pi_n$, $d\sigma$ | §4.5, (4.59)–(4.61), (4.79)–(4.80) |
| §C6b.6 | §6.5.1, (6.276); §6.5.2, (6.308), (6.313), (6.321) | (careful version) cross section as an event rate per flux; no wave packets in Yu | §4.5, (4.59)–(4.61), (4.65)–(4.75) |
| §C6b.7 | §6.5.1–§6.5.2, (6.276)–(6.313), (6.320)–(6.321) | (careful version) box route instead of the packet integrals | §4.5, (4.76)–(4.79) |
| §C6b.8 | §6.5.2–§6.5.3, (6.314)–(6.366) | Møller velocity; Källén function | §4.5, (4.80)–(4.85) |
| §C6b.9 | §6.5.4–§6.5.5, (6.367)–(6.385); §10.6, (10.259)–(10.275) | box route to $\Gamma_f$; width from $\operatorname{Im}\Pi$ | §4.5, (4.62)–(4.64), (4.86) |
| §C6b.10 | §10.3, (10.107), (10.121); §10.5.2–§10.5.3, (10.224)–(10.235) | LSZ; amputated diagrams with $\sqrt Z$ | §4.5, (4.58); §4.6, p. 108 |
| §C6b.11 | — (Yu has no classical-source problem) | | Problem 4.1; §2.4, (2.61)–(2.66) |
| §C6b.12 | — (worked translations; uses §6.5, (6.383), (6.385)) | | §4.5, (4.79), (4.84)–(4.86); Problems 4.1–4.2 |

## Sections
- [[§C6b.1 The S-Matrix and the Invariant Amplitude]] — 513 notes Ch. 15 §15.1; PS §4.5, pp. 102–104
- [[§C6b.2 Matrix Elements between Particle States]] — PS §4.6, pp. 109–113; Yu §7.1, §7.3; PHY 513 Lecture 16, Part B; PHY 513 Problem Set 8, Problems 3–4
- [[§C6b.3 Feynman Rules for Amplitudes]] — PS §4.6, pp. 112–115; Yu §7.2–§7.4; PHY 513 Lecture 16, Part C; PHY 513 Problem Set 8, Problem 2
- [[§C6b.4 Transition Probabilities in a Box]] — Yu §6.5.1, (6.276)–(6.306); 513 notes Ch. 15 §15.10
- [[§C6b.5 The Cross Section]] — Yu §6.5.2, (6.307)–(6.331); 513 notes Ch. 15 §15.2, §15.5–§15.6; PS §4.5, pp. 99–101, 106
- [[§C6b.6 Wave Packets and the Cross Section]] — 513 notes Ch. 15 §15.2–§15.3; PS §4.5, pp. 99–105
- [[§C6b.7 Evaluating the Cross Section]] — 513 notes Ch. 15 §15.4–§15.5; PS §4.5, pp. 104–106, 108
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space]] — 513 notes Ch. 15 §15.6–§15.7; PS §4.5, pp. 106–107
- [[§C6b.9 Decay Rates and Widths]] — 513 notes Ch. 15 §15.8; PS §4.5, pp. 101, 107–108
- [[§C6b.10 Amplitudes from Correlation Functions]] — 513 notes Ch. 15 §15.9–§15.10; PS §4.5, p. 99; §4.6, p. 108
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route]] — PHY 513 Problem Set 8, Problem 3; PS Problem 4.1
- [[§C6b.12 From the Question to the Formula]] — PHY 513 Problem Set 8, Problems 2–4; PS §4.5, pp. 106–108

## Principles
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|§C6b.1.3]] Interacting In and Out States

## Theorems
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|§C6b.1.1]] S-Matrix Elements and the Interaction-Picture Evolution Operator
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|§C6b.1.4]] The S-Matrix Conserves Four-Momentum
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|§C6b.1.5]] The Mass Dimension of the Amplitude
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|§C6b.1.6]] The Amplitude of Spinless Particles Is Lorentz Invariant
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|§C6b.1.7]] Spinless 2 → 2 Kinematics in Terms of s and t
- [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|§C6b.2.1]] Contraction of Fields with Outgoing Particles
- [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|§C6b.2.2]] Contraction of Fields with Incoming Particles
- [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|§C6b.2.3]] Wick's Theorem between Particle States
- [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|§C6b.2.5]] The First-Order Matrix Elements of a Monomial
- [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|§C6b.2.6]] The Kinematic Filter
- [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|§C6b.3.1]] Vertices Saturated by External Lines Give S = 1
- [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|§C6b.3.2]] Tree-Level Feynman Rules for iℳ
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-2|§C6b.4.2]] The Squared Amplitude in a Box
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-3|§C6b.4.3]] Norms of the Box States
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-4|§C6b.4.4]] The Transition Probability Grows Linearly in Time; the Rate
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-5|§C6b.4.5]] Final States in a Periodic Box
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-6|§C6b.4.6]] The Rate into a Range of Final Momenta
- [[§C6b.4 Transition Probabilities in a Box#^thm-c6b-4-7|§C6b.4.7]] Identical Particles in the Final State
- [[§C6b.5 The Cross Section#^thm-c6b-5-2|§C6b.5.2]] Events per Unit Volume and Time
- [[§C6b.5 The Cross Section#^thm-c6b-5-3|§C6b.5.3]] The Cross Section in the Rest Frame of A
- [[§C6b.5 The Cross Section#^thm-c6b-5-4|§C6b.5.4]] The Lorentz-Invariant Cross Section
- [[§C6b.5 The Cross Section#^thm-c6b-5-5|§C6b.5.5]] The Møller Velocity and the Velocity Difference
- [[§C6b.5 The Cross Section#^thm-c6b-5-6|§C6b.5.6]] The Differential Cross Section
- [[§C6b.6 Wave Packets and the Cross Section#^thm-c6b-6-2|§C6b.6.2]] The Normalization Condition Is the Unit Norm
- [[§C6b.6 Wave Packets and the Cross Section#^thm-c6b-6-3|§C6b.6.3]] The Phase Displaces the Packet by b
- [[§C6b.6 Wave Packets and the Cross Section#^thm-c6b-6-4|§C6b.6.4]] The Quantum Cross Section Is the Event Rate per Unit Flux
- [[§C6b.6 Wave Packets and the Cross Section#^lem-c6b-6-5|§C6b.6.5]] Away from the Forward Direction Only iT̂ Contributes
- [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-1|§C6b.7.1]] The Longitudinal Integrals Give the Velocity Difference
- [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-2|§C6b.7.2]] The Cross Section for 2 → n Scattering
- [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-3|§C6b.7.3]] The Cross Section Is an Area for Every n
- [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|§C6b.7.4]] Identical Particles in the Final State
- [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-5|§C6b.7.5]] The Scattering Probabilities Add Up to One
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-1|§C6b.8.1]] The Flux Factor Is a Component of an Antisymmetric Tensor
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-2|§C6b.8.2]] The Cross Section Transforms Like an Area
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-3|§C6b.8.3]] The Flux Factor in Invariant Form
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-4|§C6b.8.4]] The Phase Space Is Lorentz Invariant
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-5|§C6b.8.5]] Two-Body Phase Space in the Centre-of-Mass Frame
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-6|§C6b.8.6]] The Centre-of-Mass Momentum
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-7|§C6b.8.7]] The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
- [[§C6b.8 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-8-8|§C6b.8.8]] All Masses Equal
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-2|§C6b.9.2]] The Transition Probability of One Particle in a Box
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-3|§C6b.9.3]] The Decay Rate into Fixed Final Momenta
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-4|§C6b.9.4]] The Decay Rate Formula
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-5|§C6b.9.5]] Two-Body Decays
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-7|§C6b.9.7]] ★ Partial Widths Add
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-9|§C6b.9.9]] The Propagator Near Its Pole
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-10|§C6b.9.10]] The Width Is Invariant; the Decay Rate Is Time-Dilated
- [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-11|§C6b.9.11]] The Breit–Wigner Shape and Its Width
- [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|§C6b.10.1]] Amplitudes Are Amputated Correlation Functions
- [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|§C6b.10.2]] The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-1|§C6b.11.1]] The Vacuum-Persistence Amplitude of a Source
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-2|§C6b.11.2]] The No-Particle Probability to Order j²
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-3|§C6b.11.3]] The Vacuum Series of a Source Exponentiates
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-4|§C6b.11.4]] The One-Particle Amplitude
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-5|§C6b.11.5]] The Measure on n-Particle States
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-6|§C6b.11.6]] The Number of Particles Is Poisson Distributed
- [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-7|§C6b.11.7]] Normalization, Mean and Variance

## Models
- [[§C6b.4 Transition Probabilities in a Box#^mod-c6b-4-1|§C6b.4.1]] Two Particles in a Box
- [[§C6b.5 The Cross Section#^mod-c6b-5-1|§C6b.5.1]] Beam on a Fixed Target
- [[§C6b.6 Wave Packets and the Cross Section#^mod-c6b-6-1|§C6b.6.1]] Colliding Wave Packets
- [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-1|§C6b.9.1]] A Decaying Particle at Rest
- [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-6|§C6b.9.6]] Two Scalar Fields with a Φφ² Coupling
- [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-8|§C6b.9.8]] The Propagator of an Unstable Particle
