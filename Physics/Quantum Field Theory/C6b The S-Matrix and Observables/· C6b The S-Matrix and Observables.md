---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
tags: [chapter, quantum-field-theory]
---
# C6b The S-Matrix and Observables
← [[· C6a Interactions and Correlation Functions]] · ↑ [[Quantum Field Theory]] · [[· C6c Feynman Rules for Amplitudes]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (22), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (54), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (4), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (41), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (17), [[· C8 Quantum Electrodynamics|C8 Quantum Electrodynamics]] (2), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (2), [[· CA Mathematical Methods|CA Mathematical Methods]] (56)
**Used by:** [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (1), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (7), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (50), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (18), [[· C8 Quantum Electrodynamics|C8 Quantum Electrodynamics]] (42), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (19)

C6b computes **the $S$-matrix and the observables made from it** (Lecture 15; the user's notes, Ch. 15), in the order of Yu §6.5 (user decision 2026-11-05): the $S$-matrix, the interacting in and out states and the invariant amplitude $\mathcal M$ (§C6b.1); transition probabilities in a box (§C6b.2) and the cross section (§C6b.3), with every factor of $d\sigma$ labelled by its origin, the flux factor in invariant form, the phase space, the centre-of-mass frame and the threshold of a process; two-body scattering kinematics with the Källén function (§C6b.4); decay widths (§C6b.5) and decay kinematics, two-body and ★ three-body with the Dalitz region (§C6b.6); the width in the propagator and the Breit–Wigner shape (§C6b.7); and the course's careful version of the cross section, with wave packets, ending with the transformation of $\sigma$ as an area (§C6b.8–§C6b.9). The amplitudes themselves — contractions with external particles, Wick's theorem between particle states, first and second order, the Feynman rules for $i\mathcal M$, amplitudes as amputated correlation functions, the classical source and the worked translations — are in [[· C6c Feynman Rules for Amplitudes]]. The correlation functions, Wick's theorem and the Feynman rules it starts from are in [[· C6a Interactions and Correlation Functions]]. In Yu's book the material of C6b is in §6.2, §6.5 and §10.6.

## How C6b relates to Yu
C6b follows Yu §6.5 subsection by subsection (§C6b.2–§C6b.6; the width in the propagator, §C6b.7, is Yu §10.6), and the course's wave-packet route, Lecture 15 Part B, follows as the careful version (§C6b.8–§C6b.9), after the decays (user decisions of 2026-10-31: Yu's box route is the main line, "from what setup we arrived at the cross section, step by step"; 2026-11-05: Yu's order, wave packets after the decays). Yu uses box normalization and squares the delta function, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, where the course uses wave packets; Yu makes $\sigma$ invariant with the Møller velocity, the course shows that the flux factor transforms like an area (§C6b.9). Every section opens with a Model box or a setup paragraph saying which Hamiltonian, which states and which vacuum it assumes. Yu derives the width in the propagator from the self-energy (§10.6) (the amputation rule from LSZ, §10.3, §10.5.3: [[· C6c Feynman Rules for Amplitudes|C6c]]). Each section states its Yu correspondence in its opening and, where the route differs, in a "Remark: Yu's route".

| Section | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|
| §C6b.1 | §6.2, (6.122)–(6.127); §6.5, (6.272)–(6.275) | $S = U(+\infty, -\infty)$ between asymptotic states; $S = \mathbb I + iT$ | §4.5, (4.70)–(4.73) |
| §C6b.2 | §6.5.1, (6.276)–(6.306); Ex. 6.6 | box normalization, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$; transition probability, rate, counting of final states | §4.4, p. 96 |
| §C6b.3 | §6.5.2, (6.307)–(6.335) | beam on a fixed target, flux, $\sigma$, Møller velocity, $d\Pi_n$, $d\sigma$; centre-of-mass frame, threshold | §4.5, (4.59)–(4.61), (4.79)–(4.80) |
| §C6b.4 | §6.5.3, (6.336)–(6.366); Ex. 6.7 | two-body phase space, Källén function, azimuthal symmetry, equal masses | §4.5, (4.81)–(4.85) |
| §C6b.5 | §6.5.4, (6.367)–(6.378) | exponential law, lifetime, branching ratios; box route to $\Gamma_f$; decay threshold | §4.5, (4.62), (4.86) |
| §C6b.6 | §6.5.5, (6.379)–(6.411) | two-body decays; ★ three-body phase space, invariant masses, Dalitz region | §4.5, (4.81)–(4.82) |
| §C6b.7 | §10.6, (10.259)–(10.275) | width from $\operatorname{Im}\Pi$; Breit–Wigner | §4.5, (4.63)–(4.64) |
| §C6b.8 | §6.5.1, (6.276); §6.5.2, (6.308), (6.313), (6.321) | (careful version) cross section as an event rate per flux; no wave packets in Yu | §4.5, (4.59)–(4.61), (4.65)–(4.75) |
| §C6b.9 | §6.5.1–§6.5.2, (6.276)–(6.331) | (careful version) box route instead of the packet integrals; Møller velocity instead of the area law | §4.5, (4.76)–(4.80) |

## Sections
- [[§C6b.1 The S-Matrix and the Invariant Amplitude]] — 513 notes Ch. 15 §15.1; PS §4.5, pp. 102–104
- [[§C6b.2 Transition Probabilities in a Box]] — Yu §6.5.1, (6.276)–(6.306); 513 notes Ch. 15 §15.10
- [[§C6b.3 The Cross Section]] — Yu §6.5.2, (6.307)–(6.335); 513 notes Ch. 15 §15.2, §15.5–§15.7; PS §4.5, pp. 99–101, 106
- [[§C6b.4 Two-Body Scattering Kinematics]] — Yu §6.5.3, (6.336)–(6.366); 513 notes Ch. 15 §15.7; PS §4.5, pp. 106–107
- [[§C6b.5 Decay Widths]] — Yu §6.5.4, (6.367)–(6.378); 513 notes Ch. 15 §15.8; PS §4.5, pp. 101, 107–108
- [[§C6b.6 Decay Kinematics]] — Yu §6.5.5, (6.379)–(6.411); 513 notes Ch. 15 §15.8; Problem Set 8, Problem 4
- [[§C6b.7 The Width in the Propagator]] — Yu §10.6, (10.259)–(10.275); 513 notes Ch. 15 §15.8; PS §4.5, p. 101
- [[§C6b.8 Wave Packets and the Cross Section]] — 513 notes Ch. 15 §15.2–§15.3; PS §4.5, pp. 99–105
- [[§C6b.9 Evaluating the Cross Section]] — 513 notes Ch. 15 §15.4–§15.6; PS §4.5, pp. 104–106, 108

## Principles
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-2|§C6b.1.2]] Cluster Decomposition
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|§C6b.1.3]] Interacting In and Out States

## Laws
- [[§C6b.5 Decay Widths#^law-c6b-5-2|§C6b.5.2]] The Exponential Decay Law

## Theorems
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|§C6b.1.1]] S-Matrix Elements and the Interaction-Picture Evolution Operator
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|§C6b.1.4]] The S-Matrix Conserves Four-Momentum
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|§C6b.1.5]] The Mass Dimension of the Amplitude
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|§C6b.1.6]] The Amplitude of Spinless Particles Is Lorentz Invariant
- [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|§C6b.1.7]] Spinless 2 → 2 Kinematics in Terms of s and t
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2|§C6b.2.2]] The Box Dictionary
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|§C6b.2.3]] The Squared Amplitude in a Box
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|§C6b.2.4]] Norms of the Box States
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|§C6b.2.5]] The Transition Probability Grows Linearly in Time; the Rate
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|§C6b.2.6]] Final States in a Periodic Box
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|§C6b.2.7]] The Rate into a Range of Final Momenta
- [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|§C6b.2.8]] Identical Particles in the Final State
- [[§C6b.3 The Cross Section#^thm-c6b-3-2|§C6b.3.2]] Events per Unit Volume and Time
- [[§C6b.3 The Cross Section#^thm-c6b-3-3|§C6b.3.3]] One Particle of Each Kind in the Box
- [[§C6b.3 The Cross Section#^thm-c6b-3-4|§C6b.3.4]] The Cross Section in the Rest Frame of A
- [[§C6b.3 The Cross Section#^thm-c6b-3-5|§C6b.3.5]] The Lorentz-Invariant Cross Section
- [[§C6b.3 The Cross Section#^thm-c6b-3-6|§C6b.3.6]] The Møller Velocity and the Velocity Difference
- [[§C6b.3 The Cross Section#^thm-c6b-3-7|§C6b.3.7]] The Flux Factor in Invariant Form
- [[§C6b.3 The Cross Section#^thm-c6b-3-8|§C6b.3.8]] The Phase Space Is Lorentz Invariant
- [[§C6b.3 The Cross Section#^thm-c6b-3-9|§C6b.3.9]] The Differential Cross Section
- [[§C6b.3 The Cross Section#^thm-c6b-3-10|§C6b.3.10]] Spin Sums Are Traces: Independent of the Spin Basis
- [[§C6b.3 The Cross Section#^thm-c6b-3-11|§C6b.3.11]] The Cross Section Is an Area for Every n
- [[§C6b.3 The Cross Section#^thm-c6b-3-12|§C6b.3.12]] The Threshold of a 2 → n Process
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|§C6b.4.1]] Two-Body Phase Space in the Centre-of-Mass Frame
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|§C6b.4.2]] The Centre-of-Mass Momentum
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-3|§C6b.4.3]] ★ The Centre-of-Mass Flux Factor via λ
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|§C6b.4.4]] The 2 → 2 Differential Cross Section in the Centre-of-Mass Frame
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-5|§C6b.4.5]] The Total 2 → 2 Cross Section; Azimuthal Symmetry
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|§C6b.4.6]] Two Identical Final Particles: Half the Sphere
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|§C6b.4.7]] Equal Masses in Pairs
- [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-8|§C6b.4.8]] All Masses Equal
- [[§C6b.5 Decay Widths#^thm-c6b-5-3|§C6b.5.3]] The Lifetime Is the Mean Decay Time
- [[§C6b.5 Decay Widths#^thm-c6b-5-4|§C6b.5.4]] The Transition Probability of One Particle in a Box
- [[§C6b.5 Decay Widths#^thm-c6b-5-5|§C6b.5.5]] The Decay Rate into Fixed Final Momenta
- [[§C6b.5 Decay Widths#^thm-c6b-5-6|§C6b.5.6]] The Decay Rate Formula
- [[§C6b.5 Decay Widths#^thm-c6b-5-7|§C6b.5.7]] The Width Is an Energy for Every n
- [[§C6b.5 Decay Widths#^thm-c6b-5-8|§C6b.5.8]] The Decay Threshold
- [[§C6b.5 Decay Widths#^thm-c6b-5-9|§C6b.5.9]] The Width Is Frame-Independent; a Moving Particle Decays at Γ/γ
- [[§C6b.5 Decay Widths#^thm-c6b-5-10|§C6b.5.10]] Isotropic Decays
- [[§C6b.5 Decay Widths#^thm-c6b-5-11|§C6b.5.11]] ★ Partial Widths Add
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-1|§C6b.6.1]] Two-Body Phase Space at Rest
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-2|§C6b.6.2]] The Two-Body Width
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-3|§C6b.6.3]] Two-Body Decay into Equal Masses
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-5|§C6b.6.5]] ★ Three-Body Phase Space at Rest
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-6|§C6b.6.6]] ★ The Three-Body Width in the Energies
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-7|§C6b.6.7]] ★ The Three-Body Width in the Invariant Masses
- [[§C6b.6 Decay Kinematics#^thm-c6b-6-8|§C6b.6.8]] ★ The Dalitz Region
- [[§C6b.7 The Width in the Propagator#^thm-c6b-7-2|§C6b.7.2]] The Propagator Near Its Pole
- [[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|§C6b.7.3]] The Width Is Invariant; the Decay Rate Is Time-Dilated
- [[§C6b.7 The Width in the Propagator#^thm-c6b-7-4|§C6b.7.4]] The Breit–Wigner Shape and Its Width
- [[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-2|§C6b.8.2]] The Normalization Condition Is the Unit Norm
- [[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|§C6b.8.3]] The Phase Displaces the Packet by b
- [[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-4|§C6b.8.4]] The Quantum Cross Section Is the Event Rate per Unit Flux
- [[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|§C6b.8.5]] Away from the Forward Direction Only iT̂ Contributes
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|§C6b.9.1]] The Longitudinal Integrals Give the Velocity Difference
- [[§C6b.9 Evaluating the Cross Section#^lem-c6b-9-2|§C6b.9.2]] The Reflected Root Does Not Contribute
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|§C6b.9.3]] The Cross Section for 2 → n Scattering
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|§C6b.9.4]] Identical Particles in the Final State
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-5|§C6b.9.5]] The Scattering Probabilities Add Up to One
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|§C6b.9.6]] The Flux Factor Is a Component of an Antisymmetric Tensor
- [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|§C6b.9.7]] The Cross Section Transforms Like an Area

## Models
- [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|§C6b.2.1]] Two Particles in a Box
- [[§C6b.3 The Cross Section#^mod-c6b-3-1|§C6b.3.1]] Beam on a Fixed Target
- [[§C6b.5 Decay Widths#^mod-c6b-5-1|§C6b.5.1]] A Decaying Particle at Rest
- [[§C6b.6 Decay Kinematics#^mod-c6b-6-4|§C6b.6.4]] Two Scalar Fields with a Φφ² Coupling
- [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|§C6b.7.1]] The Propagator of an Unstable Particle
- [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|§C6b.8.1]] Colliding Wave Packets
