---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
tags: [chapter, quantum-field-theory]
---
# C6b The S-Matrix, Amplitudes and Observables
← [[· C6a Interactions and Correlation Functions]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (16), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (53), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (16), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (37), [[· CA Mathematical Methods|CA Mathematical Methods]] (68)
**Used by:** [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (24), [[· CA Mathematical Methods|CA Mathematical Methods]] (1)

C6b computes **$S$-matrix elements and the observables made from them** (Lecture 15 and Problem Set 8; the user's notes, Ch. 15): the $S$-matrix and the invariant amplitude $\mathcal M$ (§C6b.1), the cross section by Yu's box route, the main line (transition probabilities in a box §C6b.2, the cross section §C6b.3, with every factor of $d\sigma$ labelled by its origin), the same cross section from wave packets, the course's careful version (§C6b.4–§C6b.5), Lorentz invariance and two-body phase space (§C6b.6), decay rates and widths (§C6b.7), amplitudes as amputated correlation functions (§C6b.8, [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]), and particle production by a classical source (§C6b.9). The correlation functions, Wick's theorem and the Feynman rules it starts from are in [[· C6a Interactions and Correlation Functions]]. In Yu's book the material of C6b is in §6.2, §6.5, ch. 7 (the $S$-matrix rules), §10.3 and §10.6.

## How C6b relates to Yu
C6b follows the course (Lecture 15) and the user's notes (Ch. 15), except for the cross section: by the user's decision of 2026-10-31 Yu's box route is the main line (§C6b.2–§C6b.3, "from what setup we arrived at the cross section, step by step"), and the course's wave-packet route follows as the careful version (§C6b.4–§C6b.5). Yu uses box normalization and squares the delta function, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, where the course uses wave packets; every section of C6b opens with a Model box or a setup paragraph saying which Hamiltonian, which states and which vacuum it assumes; he derives the width in the propagator from the self-energy (§10.6) and the amputation rule from LSZ (§10.3, §10.5.3). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6b.1 | §6.2, (6.122)–(6.127); §6.5, (6.272)–(6.275) | $S = U(+\infty, -\infty)$ between asymptotic states; $S = \mathbb I + iT$ | §4.5, (4.70)–(4.73) |
| §C6b.2 | §6.5.1, (6.276)–(6.306) | box normalization, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$; transition probability, rate, counting of final states | §4.4, p. 96 |
| §C6b.3 | §6.5.2, (6.307)–(6.331) | beam on a fixed target, flux, $\sigma$, Møller velocity, $d\Pi_n$, $d\sigma$ | §4.5, (4.59)–(4.61), (4.79)–(4.80) |
| §C6b.4 | §6.5.1, (6.276); §6.5.2, (6.308), (6.313), (6.321) | (careful version) cross section as an event rate per flux; no wave packets in Yu | §4.5, (4.59)–(4.61), (4.65)–(4.75) |
| §C6b.5 | §6.5.1–§6.5.2, (6.276)–(6.313), (6.320)–(6.321) | (careful version) box route instead of the packet integrals | §4.5, (4.76)–(4.79) |
| §C6b.6 | §6.5.2–§6.5.3, (6.314)–(6.366) | Møller velocity; Källén function | §4.5, (4.80)–(4.85) |
| §C6b.7 | §6.5.4–§6.5.5, (6.367)–(6.385); §10.6, (10.259)–(10.275) | box route to $\Gamma_f$; width from $\operatorname{Im}\Pi$ | §4.5, (4.62)–(4.64), (4.86) |
| §C6b.8 | §10.3, (10.107), (10.121); §10.5.2–§10.5.3, (10.224)–(10.235) | LSZ; amputated diagrams with $\sqrt Z$ | §4.5, (4.58); §4.6, p. 108 |
| §C6b.9 | — (Yu has no classical-source problem) | | Problem 4.1; §2.4, (2.61)–(2.66) |

## Sections
- [[§C6b.1 The S-Matrix and the Invariant Amplitude]] — 513 notes Ch. 15 §15.1; PS §4.5, pp. 102–104
- [[§C6b.2 Transition Probabilities in a Box]] — Yu §6.5.1, (6.276)–(6.306); 513 notes Ch. 15 §15.10
- [[§C6b.3 The Cross Section]] — Yu §6.5.2, (6.307)–(6.331); 513 notes Ch. 15 §15.2, §15.5–§15.6; PS §4.5, pp. 99–101, 106
- [[§C6b.4 Wave Packets and the Cross Section]] — 513 notes Ch. 15 §15.2–§15.3; PS §4.5, pp. 99–105
- [[§C6b.5 Evaluating the Cross Section]] — 513 notes Ch. 15 §15.4–§15.5; PS §4.5, pp. 104–106, 108
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space]] — 513 notes Ch. 15 §15.6–§15.7; PS §4.5, pp. 106–107
- [[§C6b.7 Decay Rates and Widths]] — 513 notes Ch. 15 §15.8; PS §4.5, pp. 101, 107–108
- [[§C6b.8 Amplitudes from Correlation Functions]] — 513 notes Ch. 15 §15.9–§15.10; PS §4.5, p. 99; §4.6, p. 108
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route]] — PHY 513 Problem Set 8, Problem 3; PS Problem 4.1

## Theorems
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|§C6b.1.1]] S-Matrix Elements and the Interaction-Picture Evolution Operator
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|§C6b.1.2]] The S-Matrix Conserves Four-Momentum
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-3|§C6b.1.3]] The Mass Dimension of the Amplitude
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|§C6b.1.4]] The Amplitude of Spinless Particles Is Lorentz Invariant
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|§C6b.1.5]] Spinless 2 → 2 Kinematics in Terms of s and t
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|§C6b.2.2]] The Squared Amplitude in a Box
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|§C6b.2.3]] Norms of the Box States
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|§C6b.2.4]] The Transition Probability Grows Linearly in Time; the Rate
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|§C6b.2.5]] Final States in a Periodic Box
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|§C6b.2.6]] The Rate into a Range of Final Momenta
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|§C6b.2.7]] Identical Particles in the Final State
- [[§C6b.3 The Cross Section#^thm-c6b-3-2|§C6b.3.2]] Events per Unit Volume and Time
- [[§C6b.3 The Cross Section#^thm-c6b-3-3|§C6b.3.3]] The Cross Section in the Rest Frame of A
- [[§C6b.3 The Cross Section#^thm-c6b-3-4|§C6b.3.4]] The Lorentz-Invariant Cross Section
- [[§C6b.3 The Cross Section#^thm-c6b-3-5|§C6b.3.5]] The Møller Velocity and the Velocity Difference
- [[§C6b.3 The Cross Section#^thm-c6b-3-6|§C6b.3.6]] The Differential Cross Section
- [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-2|§C6b.4.2]] The Normalization Condition Is the Unit Norm
- [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-3|§C6b.4.3]] The Phase Displaces the Packet by b
- [[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4|§C6b.4.4]] The Quantum Cross Section Is the Event Rate per Unit Flux
- [[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|§C6b.4.5]] Away from the Forward Direction Only iT̂ Contributes
- [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-1|§C6b.5.1]] The Longitudinal Integrals Give the Velocity Difference
- [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|§C6b.5.2]] The Cross Section for 2 → n Scattering
- [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-3|§C6b.5.3]] The Cross Section Is an Area for Every n
- [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4|§C6b.5.4]] Identical Particles in the Final State
- [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-5|§C6b.5.5]] The Scattering Probabilities Add Up to One
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-1|§C6b.6.1]] The Flux Factor Is a Component of an Antisymmetric Tensor
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-2|§C6b.6.2]] The Cross Section Transforms Like an Area
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|§C6b.6.3]] The Flux Factor in Invariant Form
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-4|§C6b.6.4]] The Phase Space Is Lorentz Invariant
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-5|§C6b.6.5]] Two-Body Phase Space in the Centre-of-Mass Frame
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-6|§C6b.6.6]] The Centre-of-Mass Momentum
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-7|§C6b.6.7]] The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
- [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8|§C6b.6.8]] All Masses Equal
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-2|§C6b.7.2]] The Transition Probability of One Particle in a Box
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-3|§C6b.7.3]] The Decay Rate into Fixed Final Momenta
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4|§C6b.7.4]] The Decay Rate Formula
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-5|§C6b.7.5]] Two-Body Decays
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-6|§C6b.7.6]] ★ Partial Widths Add
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-8|§C6b.7.8]] The Propagator Near Its Pole
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-9|§C6b.7.9]] The Width Is Invariant; the Decay Rate Is Time-Dilated
- [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-10|§C6b.7.10]] The Breit–Wigner Shape and Its Width
- [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|§C6b.8.1]] Amplitudes Are Amputated Correlation Functions
- [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-2|§C6b.8.2]] The Disconnected Pieces of the Free Four-Point Function Do Not Scatter
- [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3|§C6b.8.3]] Vertex Factors of a Polynomial Interaction
- [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4|§C6b.8.4]] Vertices Saturated by External Lines Give S = 1
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1|§C6b.9.1]] The Vacuum-Persistence Amplitude of a Source
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-2|§C6b.9.2]] The No-Particle Probability to Order j²
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3|§C6b.9.3]] The Vacuum Series of a Source Exponentiates
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|§C6b.9.4]] Contraction of Fields with Outgoing Particles
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-5|§C6b.9.5]] The One-Particle Amplitude
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-6|§C6b.9.6]] The Measure on n-Particle States
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7|§C6b.9.7]] The Number of Particles Is Poisson Distributed
- [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-8|§C6b.9.8]] Normalization, Mean and Variance

## Models
- [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|§C6b.2.1]] Two Particles in a Box
- [[§C6b.3 The Cross Section#^mod-c6b-3-1|§C6b.3.1]] Beam on a Fixed Target
- [[§C6b.4 Wave Packets and the Cross Section#^mod-c6b-4-1|§C6b.4.1]] Colliding Wave Packets
- [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-1|§C6b.7.1]] A Decaying Particle at Rest
- [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-7|§C6b.7.7]] The Propagator of an Unstable Particle
