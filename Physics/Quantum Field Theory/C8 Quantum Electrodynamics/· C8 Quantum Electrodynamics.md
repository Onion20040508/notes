---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8
tags: [chapter, quantum-field-theory]
---
# C8 Quantum Electrodynamics
← [[· C6d Feynman Rules for Fermions]] · ↑ [[Quantum Field Theory]] · [[· C9 Discrete Symmetries and Majorana Fields]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (13), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (19), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (9), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (12), [[· C3 Poincaré Symmetry and Particle States|C3 Poincaré Symmetry and Particle States]] (1), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (47), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (136), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (20), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (29), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (66), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (27), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (96), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (13), [[· CA Mathematical Methods|CA Mathematical Methods]] (18)
**Used by:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (49), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (7), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (2), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (4), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (9), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (14), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (1)

C8 is **quantum electrodynamics**, started with Lecture 18 and continued with Lecture 19 (Lecture 18: "Quantum Electrodynamics", 9 Nov 2026; PS §4.7 from p. 121 and §4.8; the user's notes, Lecture 18 update; user decision 2026-11-09: a chapter of its own, Yu's chapter 8, while C6d stays Yukawa only). It puts together the ingredients of the earlier chapters, the Dirac field (C5a, C5b), the photon field (C4) and the Feynman rules with fermions (C6d): the Lagrangian with its three terms, the interaction Hamiltonian, the coupling as $e$ times the conserved current, the gauge covariant derivative $D_\mu = \partial_\mu + ieA_\mu$ and its agreement with minimal coupling in nonrelativistic quantum mechanics (§C8.1); the local gauge symmetry, proved through $D_\mu$ and term by term, and what it is for (§C8.2); the photon lines in the course's notation $\hat A_\mu$, $\epsilon^r_\mu(p)$, $\hat a^r_{\mathbf p}$: the field, the four polarizations of which two are physical, the weighted completeness relation, the propagator $-ig_{\mu\nu}/(q^2 + i\varepsilon)$ and its wrong-sign component, each proved in C4 (§C8.3); the Feynman rules: external photons $\epsilon_\mu$, $\epsilon^\ast_\mu$, the vertex $-ie\gamma^\mu$, the rules for $i\mathcal M$ as the Yukawa rules with a new vertex and boson line, and one-photon exchange next to scalar exchange (§C8.4); and the nonrelativistic limit: the Coulomb potential $e^2/4\pi r$ from the $g_{00}$ component, the signs for antiparticles from the spinor products and the contractions, why the sign of $\mathcal M$ relative to the unscattered term is physical, and the table of attraction and repulsion (§C8.5). The Yukawa half of the lecture's Part C, with the Born comparison $i\mathcal M_{\rm NR} = -i\tilde V(\mathbf q)$, is [[§C6d.7 The Yukawa Potential|§C6d.7]]. Lecture 19 ("Electron–Positron Annihilation", 11 Nov 2026; PS §5.1, the slides cite 5.2; the user's notes, Lecture 19 update) computes the first process, $e^+e^- \to \mu^+\mu^-$, completely: QED with a second charged fermion, the one diagram and its amplitude $\frac{ie^2}{q^2}[\bar v\gamma^\mu u][\bar u\gamma_\mu v]$ derived from the rules, the mass shell, on shell and off shell, and the timelike virtual photon (§C8.6); the square of the amplitude, the spin average, each fermion line as a trace, the electron and muon traces by the trace theorems of [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-3|Theorem §C5a.13.3]], and the result in invariants (§C8.7); the centre-of-mass frame with $m_e = 0$, the angular distribution, $d\sigma/d\Omega$ split into kinematics and dynamics, and $\sigma_{\rm tot} = 4\pi\alpha^2/3E_{\rm cm}^2$ (§C8.8); quark–antiquark production, the ratio $R = \sum3Q^2$ and what its measured plateaus confirm (§C8.9). The six steps are the procedure [[P8 Unpolarized Cross Section from Diagrams]]. Problem Set 10, Problems 2 and 3 (PS Problem 4.4 and the first part of Problem 5.1; the user's solution, 2026-11-13) add the electron in a classical external potential: the Dirac field coupled to a given $A_\mu(x)$, the first-order element $-ie\,\bar u(p')\gamma^\mu u(p)\,\tilde A_\mu(p' - p)$ and the rule for the vertex with an external field, the Fourier transform of the Coulomb potential with a cutoff, $Ze/|\mathbf q|^2$, and the Rutherford formula in the nonrelativistic limit (§C8.10; the cross-section formula for a fixed target is [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential|§C6b.10]]); then the same electron at any velocity: the spin sum of the one line as a trace, $\frac12\sum|\bar u'\gamma^0u|^2 = 4E^2(1 - \beta^2\sin^2\frac\theta2)$, Mott's formula, and, beyond the problem set (★), the exact spinor product $\bar u'\gamma^0u$ at equal energies (§C8.11). A starred section, from Appendix B of the user's notes (reference material, not from a lecture; the course has not treated scalar QED), continues [[§C6c.11 Feynman Rules from the Lagrangian|§C6c.11]] to interactions with derivatives: the momentum rule $\partial_\mu \to -ip_\mu$ for a momentum flowing into the vertex, scalar QED with its vertices $-ie(p + p')^\mu$ and $2ie^2g^{\mu\nu}$, the slow-particle limit, and the interaction Hamiltonian, which is not $-\mathcal L_{\rm int}$ there (★ §C8.18). Lecture 20 ("Helicity Structure", 16 Nov 2026; PS §5.2; the user's notes, Lecture 20 update) follows $e^+e^- \to \mu^+\mu^-$ spin by spin: helicity of a particle, the projected spinors, the projectors selecting helicity at high energy with the reversal for antiparticles, $\gamma^0\gamma^\mu$ block diagonal and helicity conservation at the QED vertex, $e^-_R$ annihilating only with $e^+_L$ into $J_z = \pm1$ (§C8.15); the projected amplitude, the conjugate and the spin sum with projectors, the traces with $\gamma^5$, $|\mathcal M|^2 = \frac{16e^4}{q^4}(p\cdot k')(p'\cdot k)$, the polarized cross sections $\frac{\alpha^2}{4E_{\rm cm}^2}(1 \pm \cos\theta)^2$ and their average, the zeros from angular momentum, and the amplitude with explicit helicity spinors as the overlap of a circular polarization vector with its rotated image (§C8.16); the steps are [[P9 Helicity Amplitudes]]. The QED processes of Lectures 21–22 (crossing symmetry, Compton scattering) will continue the chapter; the Ward identity and the careful quantization of the electromagnetic field (Lecture 25) are pending.

## How C8 relates to Yu and PS
C8 follows the lecture and the user's notes (Parts A, B, C). Yu builds QED the same way in §8.1 and treats the potentials in §8.4.3, with his charge convention $Q_fe$, $e > 0$ ([[§C8.1 The QED Lagrangian and the Covariant Derivative#^cau-c8-1-1|§C8.1, Caution: What e means]]); his photon quantization (§4.4) and propagator (§6.4.4) are the sources of C4, in his notation $e^\mu(p, \sigma)$, $b_{\mathbf p,\sigma}$. PS §4.8 is the lecture's reading. For Lecture 19 the reading is PS §5.1 (the slides cite 5.2, which is Lecture 20); for Lecture 20 PS §5.2, which does the projector-and-trace route and the explicit spinors for massless fermions, while Yu §8.2.4 uses explicit spinors with both masses and §8.3 treats chirality separately; Yu treats the same process in §8.2.1–§8.2.3 with all masses kept, the incoming momenta named $k_1, k_2$ and the outgoing $p_1, p_2$, spins labelled by helicities; he does not discuss $R$.

| Section | Lecture, slides | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|---|
| §C8.1 | 18: slides 5–6 | §8.1, (8.1)–(8.17), (8.35) | free Dirac Lagrangian, covariant derivative $D_\mu = \partial_\mu + iQ_feA_\mu$, $\mathcal L_{\rm QED}$, $J^\mu_{\rm EM}$; Schrödinger–Pauli limit | §4.1, (4.3)–(4.8); §4.8, (4.129) |
| §C8.2 | 18: slide 7 | §8.1, (8.2)–(8.9) | global and local U(1), $A_\mu \to A_\mu - \frac1e\partial_\mu\theta$, covariance of $D_\mu\psi$ | §4.1, (4.6) |
| §C8.3 | 18: slides 8–9, 12–13 | §4.4, (4.184)–(4.193), (4.228)–(4.232), (4.246)–(4.248); §6.4.4, (6.248)–(6.253) | massless polarization basis and weighted completeness; Feynman-gauge expansion; $[b, b^\dagger] \propto -g$; negative-norm temporal state; photon Feynman propagator | §4.8, (4.130)–(4.132), p. 124 |
| §C8.4 | 18: slides 14–15, 19 | §8.1, rules 1–9; §8.4.3, (8.244) | QED Feynman rules, vertex $-iQ_fe\gamma^\mu$ | §4.8, p. 123, (4.133) |
| §C8.5 | 18: slides 24–29 | §8.4.3, (8.238)–(8.278), (8.286)–(8.287) | Coulomb potential (as the Yukawa result at $m_\phi = 0$); Yu's own Fourier transform from $1/\lvert\mathbf q\rvert^2$ to the Coulomb potential, (8.259)–(8.263), by a residue (the direct transform with a cutoff: §C8.10); the absolute sign from contractions; particle–antiparticle | §4.8, pp. 125–126, (4.133)–(4.136) |
| §C8.6 | 19: slides 2–8 | §8.1, (8.10)–(8.11); §8.2.1, (8.37)–(8.39); §7.1, after (7.41) | several charged species $f$; the amplitude with $Q_e = Q_\mu = -1$; $q^2 = E_{\rm CM}^2 > 4m_\mu^2$ and the dropped $i\epsilon$; real and virtual particles | §5.1, pp. 131–132, (5.1) |
| §C8.7 | 19: slides 11–15 | §8.2.1, (8.40)–(8.43); §8.2.2, (8.44)–(8.55); §8.2.3, (8.78)–(8.80) | conjugation, Casimir's trick, $\overline{\lvert\mathcal M\rvert^2}$; trace theorems; the two traces and their contraction, all masses | §5.1, pp. 132–135, (5.2)–(5.5), (5.10) |
| §C8.8 | 19: slides 18–22 | §8.2.3, (8.81)–(8.98) | centre-of-mass kinematics with $\beta_e$, $\beta_\mu$; $d\sigma/d\Omega$ and $\sigma$ with both masses, $m_e \to 0$, high energy; TASSO data | §5.1, pp. 136–138, (5.11)–(5.15) |
| §C8.9 | 19: slides 23–26 | §8.1, (8.10) | quark species with a colour index; no $R$ | §5.1, pp. 138–141, (5.15)–(5.16) |
| §C8.10 | Problem Set 10, Problem 2 | §8.4.3, (8.259)–(8.263) | the Fourier transform between $1/\lvert\mathbf q\rvert^2$ and the Coulomb potential, from momentum to position space; no classical external potential | Problem 4.4, pp. 129–130 |
| §C8.11 | Problem Set 10, Problem 3 | — | — (not cited) | Problem 5.1, first part, p. 169 |
| §C8.15 | 20: slides 3–11, 26–27 | §8.2.4, (8.108), (8.143)–(8.157); §8.3, (8.159)–(8.166), (8.174)–(8.189) | chirality projectors; helicity equals chirality at high energy, reversed for $v$; mass-suppressed helicity amplitudes | §5.2, pp. 141–142, (5.17)–(5.18), p. 145 |
| §C8.16 | 20: slides 14–20, 23–28 | §8.2.4, (8.99)–(8.142), (8.158) | polarized amplitudes with explicit helicity spinors and both masses; currents (8.118), (8.132)–(8.135); $\mp e^2(1 \pm \cos\theta)$; parity; the sum of sixteen | §5.2, pp. 142–146, (5.17)–(5.32), Figure 5.4 |
| §C8.18★ | — (the user's notes, Appendix B) | §11.4.3, (11.482), (11.487)–(11.495) and the closing remark | scalar QED by the path integral; the momentum rule for derivatives; vertices $-iQ_\phi e(p_\mu + q_\mu)$ and $2iQ_\phi^2e^2g_{\mu\nu}$; the non-covariant term of $\mathcal H_I$ | Problem 9.1 (named as reading by the appendix) |

## Sections
- [[§C8.1 The QED Lagrangian and the Covariant Derivative]] — 513 notes Lecture 18 update §18.1–§18.2; PHY 513 Lecture 18, slides 5–6; PS §4.1, §4.8; Yu §8.1
- [[§C8.2 Gauge Invariance]] — 513 notes Lecture 18 update §18.3; PHY 513 Lecture 18, slide 7; Yu §8.1, (8.2)–(8.9)
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator]] — 513 notes Lecture 18 update §18.4–§18.5; PHY 513 Lecture 18, slides 8–9, 12–13; PS §4.8, pp. 123–124; Yu §4.4, §6.4.4
- [[§C8.4 Feynman Rules for QED]] — 513 notes Lecture 18 update §18.6; PHY 513 Lecture 18, slides 14–15, 19; PS §4.8, pp. 123–125; Yu §8.1
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel]] — 513 notes Lecture 18 update §18.7–§18.8; PHY 513 Lecture 18, slides 24–29; PS §4.8, pp. 125–126; Yu §8.4.3
- [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon]] — 513 notes Lecture 19 update §19.1; PHY 513 Lecture 19, slides 2–8; PS §5.1, pp. 131–132; Yu §8.2.1
- [[§C8.7 The Spin-Averaged Squared Amplitude]] — 513 notes Lecture 19 update §19.2–§19.3; PHY 513 Lecture 19, slides 11–15; PS §5.1, pp. 132–135; Yu §8.2.1, §8.2.3
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production]] — 513 notes Lecture 19 update §19.4; PHY 513 Lecture 19, slides 18–22; PS §5.1, pp. 136–138; Yu §8.2.3
- [[§C8.9 Quark–Antiquark Production and the Ratio R]] — 513 notes Lecture 19 update §19.4–§19.6; PHY 513 Lecture 19, slides 23–26; PS §5.1, pp. 139–141
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula]] — PHY 513 Problem Set 10, Problem 2; PS Problem 4.4, pp. 129–130; Yu §8.4.3, (8.259)–(8.263)
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field]] — PHY 513 Problem Set 10, Problem 3; PS Problem 5.1 (first part), p. 169
- [[§C8.15 Chirality, Helicity and the QED Vertex]] — PHY 513 Lecture 20 (16 Nov 2026), slides 3–11; 513 notes Lecture 20 update §20.1–20.2; PS §5.2, pp. 141–142, 145; Yu §8.3
- [[§C8.16 Polarized Cross Sections for Muon Pair Production]] — PHY 513 Lecture 20 (16 Nov 2026), slides 14–28; 513 notes Lecture 20 update §20.3–20.6; PS §5.2, pp. 142–146, (5.17)–(5.32); Yu §8.2.4, (8.99)–(8.158)
- [[§C8.18★ Derivative Couplings and Scalar QED]] — 513 notes Appendix B (2026-11-14), section "Derivative couplings"; Yu §11.4.3, (11.482), (11.487)–(11.495)

## Principles
- [[§C8.2 Gauge Invariance#^pr-c8-2-1|§C8.2.1]] Gauge Symmetry of QED
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^pr-c8-5-8|§C8.5.8]] Attraction and Repulsion by the Spin of the Exchanged Particle
- [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8-6-4|§C8.6.4]] Particles Mediating an Interaction Are Off Shell
- [[§C8.18★ Derivative Couplings and Scalar QED#^pr-c8-18-1|§C8.18.1]] Derivatives in the Vertex

## Theorems
- [[§C8.1 The QED Lagrangian and the Covariant Derivative#^thm-c8-1-2|§C8.1.2]] The Interaction Hamiltonian of QED
- [[§C8.1 The QED Lagrangian and the Covariant Derivative#^thm-c8-1-3|§C8.1.3]] The QED Coupling Is e Times the Conserved Current
- [[§C8.1 The QED Lagrangian and the Covariant Derivative#^thm-c8-1-4|§C8.1.4]] The Condensed Form of the QED Lagrangian
- [[§C8.1 The QED Lagrangian and the Covariant Derivative#^thm-c8-1-5|§C8.1.5]] The Covariant Derivative Is Minimal Coupling
- [[§C8.2 Gauge Invariance#^thm-c8-2-2|§C8.2.2]] The Covariant Derivative Transforms Covariantly
- [[§C8.2 Gauge Invariance#^thm-c8-2-3|§C8.2.3]] The QED Lagrangian Is Gauge Invariant
- [[§C8.2 Gauge Invariance#^thm-c8-2-4|§C8.2.4]] A Local Phase Needs the Compensating Shift of the Potential
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-1|§C8.3.1]] The Quantized Photon Field in the Course's Form
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-2|§C8.3.2]] The Photon Field Is Real: the Photon Is Neutral
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-3|§C8.3.3]] Why Only Transverse Polarizations Are Physical
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-4|§C8.3.4]] The Weighted Completeness Relation
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-5|§C8.3.5]] The Photon Propagator
- [[§C8.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8-3-6|§C8.3.6]] Lorentz Invariance versus Positivity: the Wrong-Sign Component
- [[§C8.4 Feynman Rules for QED#^thm-c8-4-1|§C8.4.1]] The External Photon Wave Functions
- [[§C8.4 Feynman Rules for QED#^thm-c8-4-2|§C8.4.2]] Photon Fields Contract in Pairs or with External Photons, without Signs
- [[§C8.4 Feynman Rules for QED#^thm-c8-4-3|§C8.4.3]] The QED Vertex
- [[§C8.4 Feynman Rules for QED#^thm-c8-4-4|§C8.4.4]] Feynman Rules for iℳ in QED
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-1|§C8.5.1]] The Vector Spinor Products in the Nonrelativistic Limit
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-2|§C8.5.2]] The Nonrelativistic QED Amplitude for Distinguishable Fermions
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-3|§C8.5.3]] The Coulomb Potential
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-4|§C8.5.4]] The Antiparticle Spinor Products in the Nonrelativistic Limit
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-5|§C8.5.5]] The Sign from the Contractions: Plus for Two Particles, Minus for Particle and Antiparticle
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-6|§C8.5.6]] The Sign of ℳ Relative to the Unscattered Term Is Physical
- [[§C8.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8-5-7|§C8.5.7]] In QED Like Charges Repel and Opposite Charges Attract
- [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8-6-2|§C8.6.2]] The Amplitude for Electron–Positron Annihilation into a Muon Pair
- [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8-6-3|§C8.6.3]] The Photon of the Annihilation Diagram Is Timelike and Off Shell
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-1|§C8.7.1]] The Complex Conjugate of a Vector Bilinear Reverses It
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-2|§C8.7.2]] The Squared Amplitude for Fixed Spins
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-3|§C8.7.3]] A Spin-Summed Fermion Line Is a Trace
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-4|§C8.7.4]] The Spin-Averaged Squared Amplitude as Two Traces
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-5|§C8.7.5]] The Electron Trace and the Muon Trace
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-6|§C8.7.6]] The Spin-Averaged Squared Amplitude in Invariants
- [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-7|§C8.7.7]] The Unpolarized Squared Amplitude in General (Casimir's Trick)
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-1|§C8.8.1]] The Momenta in the Centre-of-Mass Frame
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-2|§C8.8.2]] The Invariants in the Centre-of-Mass Frame
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-3|§C8.8.3]] The Spin-Averaged Squared Amplitude in the Centre-of-Mass Frame
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-4|§C8.8.4]] The Unpolarized Differential Cross Section
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-5|§C8.8.5]] The Total Cross Section at High Energy
- [[§C8.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8-8-6|§C8.8.6]] The Total Cross Section with the Muon Mass
- [[§C8.9 Quark–Antiquark Production and the Ratio R#^thm-c8-9-1|§C8.9.1]] The Cross Section for Quark–Antiquark Production
- [[§C8.9 Quark–Antiquark Production and the Ratio R#^thm-c8-9-2|§C8.9.2]] R Counts the Quarks, Weighted by Charge Squared
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-2|§C8.10.2]] The First-Order S-Matrix Element in an External Field
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-3|§C8.10.3]] Of the Four Terms of the Current, One Scatters and One Is the Unscattered Electron Times a Vacuum Value
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-4|§C8.10.4]] A Time-Independent Potential Conserves the Energy
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-5|§C8.10.5]] The Feynman Rule for a Vertex with an External Field
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-6|§C8.10.6]] The Fourier Transform of the Coulomb Potential
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-7|§C8.10.7]] The Momentum Transfer at Fixed Energy
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-8|§C8.10.8]] The Rutherford Formula
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-9|§C8.10.9]] In the Nonrelativistic Limit the Amplitude Is the Born Amplitude of the Potential Energy eA₀
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8-10-10|§C8.10.10]] The Total Rutherford Cross Section Is Infinite (ADDED)
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-1|§C8.11.1]] The Amplitude for an Electron of Any Velocity in the Coulomb Field
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-2|§C8.11.2]] The Spin-Summed Vector Product in an External Coulomb Field
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-3|§C8.11.3]] Mott's Formula
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-4|§C8.11.4]] ★ The Exact Vector Spinor Product at Equal Energies
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-5|§C8.11.5]] ★ The Spin-Summed Product from the Exact Form, without a Trace of γ Matrices
- [[§C8.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8-11-6|§C8.11.6]] ★ The Spin-Dependent Term Points along the Normal of the Scattering Plane
- [[§C8.15 Chirality, Helicity and the QED Vertex#^thm-c8-15-1|§C8.15.1]] At High Energy the Projectors Select the Helicity of a Particle
- [[§C8.15 Chirality, Helicity and the QED Vertex#^thm-c8-15-2|§C8.15.2]] For an Antiparticle the Spinor Shows the Opposite Helicity
- [[§C8.15 Chirality, Helicity and the QED Vertex#^thm-c8-15-3|§C8.15.3]] In the Chiral Basis γ⁰γ^μ Is Block Diagonal
- [[§C8.15 Chirality, Helicity and the QED Vertex#^thm-c8-15-4|§C8.15.4]] Helicity Conservation at the QED Vertex
- [[§C8.15 Chirality, Helicity and the QED Vertex#^thm-c8-15-5|§C8.15.5]] An Electron Annihilates Only with a Positron of the Opposite Helicity
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-1|§C8.16.1]] The Projected Amplitude
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-2|§C8.16.2]] The Conjugate Keeps the Projector on the Right
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-3|§C8.16.3]] With Projectors the Spin Sum Is Still a Trace
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-4|§C8.16.4]] The Projected Traces
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-5|§C8.16.5]] The Polarized Squared Amplitudes in Invariants
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-6|§C8.16.6]] The Polarized Cross Sections in the Centre-of-Mass Frame
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-7|§C8.16.7]] The Average over Helicities Is the Unpolarized Result
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-8|§C8.16.8]] Angular Momentum along the Beam Fixes the Zeros
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-9|§C8.16.9]] Spinors in the Ultrarelativistic Limit
- [[§C8.16 Polarized Cross Sections for Muon Pair Production#^thm-c8-16-10|§C8.16.10]] The Vertex Is a Circular Polarization Vector
- [[§C8.18★ Derivative Couplings and Scalar QED#^thm-c8-18-3|§C8.18.3]] The Interaction Lagrangian of Scalar QED
- [[§C8.18★ Derivative Couplings and Scalar QED#^thm-c8-18-4|§C8.18.4]] The Three-Point Vertex of Scalar QED
- [[§C8.18★ Derivative Couplings and Scalar QED#^thm-c8-18-5|§C8.18.5]] The Four-Point (Seagull) Vertex of Scalar QED
- [[§C8.18★ Derivative Couplings and Scalar QED#^thm-c8-18-6|§C8.18.6]] For a Slow Particle the Scalar Vertex Is the Dirac Vertex
- [[§C8.18★ Derivative Couplings and Scalar QED#^thm-c8-18-7|§C8.18.7]] The Interaction Hamiltonian of Scalar QED Has a Non-Covariant Term
- [[§C8.18★ Derivative Couplings and Scalar QED#^lem-c8-18-8|§C8.18.8]] The Time-Ordered Product of Two Time Derivatives Has a Contact Term

## Models
- [[§C8.1 The QED Lagrangian and the Covariant Derivative#^mod-c8-1-1|§C8.1.1]] Quantum Electrodynamics
- [[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8-6-1|§C8.6.1]] QED with Several Charged Dirac Fields
- [[§C8.10 Scattering off an External Potential꞉ the Rutherford Formula#^mod-c8-10-1|§C8.10.1]] The Dirac Field in a Classical External Potential
- [[§C8.18★ Derivative Couplings and Scalar QED#^mod-c8-18-2|§C8.18.2]] Scalar QED
