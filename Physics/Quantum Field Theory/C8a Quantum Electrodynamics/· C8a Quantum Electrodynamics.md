---
type: chapter
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
tags: [chapter, quantum-field-theory]
---
# C8a Quantum Electrodynamics
← [[· C6d Feynman Rules for Fermions]] · ↑ [[Quantum Field Theory]] · [[· C8b Spin, Helicity and Chirality]] →

**Builds on:** [[· C1a Preliminaries|C1a Preliminaries]] (19), [[· C1b Classical Field Theory|C1b Classical Field Theory]] (19), [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] (13), [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (12), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (53), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (115), [[· C5b The Quantum Spinor Field|C5b The Quantum Spinor Field]] (21), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (31), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (98), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (35), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (119), [[· C8b Spin, Helicity and Chirality|C8b Spin, Helicity and Chirality]] (8), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (3), [[· CA Mathematical Methods|CA Mathematical Methods]] (20)
**Used by:** [[· C1b Classical Field Theory|C1b Classical Field Theory]] (1), [[· C4 The Quantum Vector Field|C4 The Quantum Vector Field]] (50), [[· C5a Spinors and the Dirac Equation|C5a Spinors and the Dirac Equation]] (6), [[· C6a Interactions and Correlation Functions|C6a Interactions and Correlation Functions]] (2), [[· C6b The S-Matrix and Observables|C6b The S-Matrix and Observables]] (4), [[· C6c Feynman Rules for Amplitudes|C6c Feynman Rules for Amplitudes]] (9), [[· C6d Feynman Rules for Fermions|C6d Feynman Rules for Fermions]] (14), [[· C8b Spin, Helicity and Chirality|C8b Spin, Helicity and Chirality]] (92), [[· C9 Discrete Symmetries and Majorana Fields|C9 Discrete Symmetries and Majorana Fields]] (1)

C8a is **quantum electrodynamics**, started with Lecture 18 and continued with Lecture 19 (Lecture 18: "Quantum Electrodynamics", 9 Nov 2026; PS §4.7 from p. 121 and §4.8; the user's notes, Lecture 18 update; user decision 2026-11-09: a chapter of its own, Yu's chapter 8, while C6d stays Yukawa only). It puts together the ingredients of the earlier chapters, the Dirac field (C5a, C5b), the photon field (C4) and the Feynman rules with fermions (C6d): the Lagrangian with its three terms, the interaction Hamiltonian, the coupling as $e$ times the conserved current, the gauge covariant derivative $D_\mu = \partial_\mu + ieA_\mu$ and its agreement with minimal coupling in nonrelativistic quantum mechanics (§C8a.1); the local gauge symmetry, proved through $D_\mu$ and term by term, and what it is for (§C8a.2); the photon lines in the course's notation $\hat A_\mu$, $\epsilon^r_\mu(p)$, $\hat a^r_{\mathbf p}$: the field, the four polarizations of which two are physical, the weighted completeness relation, the propagator $-ig_{\mu\nu}/(q^2 + i\varepsilon)$ and its wrong-sign component, each proved in C4 (§C8a.3); the Feynman rules: external photons $\epsilon_\mu$, $\epsilon^\ast_\mu$, the vertex $-ie\gamma^\mu$, the rules for $i\mathcal M$ as the Yukawa rules with a new vertex and boson line, and one-photon exchange next to scalar exchange (§C8a.4); and the nonrelativistic limit: the Coulomb potential $e^2/4\pi r$ from the $g_{00}$ component, the signs for antiparticles from the spinor products and the contractions, why the sign of $\mathcal M$ relative to the unscattered term is physical, and the table of attraction and repulsion (§C8a.5). The Yukawa half of the lecture's Part C, with the Born comparison $i\mathcal M_{\rm NR} = -i\tilde V(\mathbf q)$, is [[§C6d.7 The Yukawa Potential|§C6d.7]]. Lecture 19 ("Electron–Positron Annihilation", 11 Nov 2026; PS §5.1, the slides cite 5.2; the user's notes, Lecture 19 update) computes the first process, $e^+e^- \to \mu^+\mu^-$, completely: QED with a second charged fermion, the one diagram and its amplitude $\frac{ie^2}{q^2}[\bar v\gamma^\mu u][\bar u\gamma_\mu v]$ derived from the rules, the mass shell, on shell and off shell, and the timelike virtual photon (§C8a.6); the square of the amplitude, the spin average, each fermion line as a trace, the electron and muon traces by the trace theorems of [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-3|Theorem §C5a.13.3]], and the result in invariants (§C8a.7); the centre-of-mass frame with $m_e = 0$, the angular distribution, $d\sigma/d\Omega$ split into kinematics and dynamics, and $\sigma_{\rm tot} = 4\pi\alpha^2/3E_{\rm cm}^2$ (§C8a.8); quark–antiquark production, the ratio $R = \sum3Q^2$ and what its measured plateaus confirm (§C8a.9). The six steps are the procedure [[P8 Unpolarized Cross Section from Diagrams]]. Problem Set 10, Problems 2 and 3 (PS Problem 4.4 and the first part of Problem 5.1; the user's solution, 2026-11-13) add the electron in a classical external potential: the Dirac field coupled to a given $A_\mu(x)$, the first-order element $-ie\,\bar u(p')\gamma^\mu u(p)\,\tilde A_\mu(p' - p)$ and the rule for the vertex with an external field, the Fourier transform of the Coulomb potential with a cutoff, $Ze/|\mathbf q|^2$, and the Rutherford formula in the nonrelativistic limit (§C8a.10; the cross-section formula for a fixed target is [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential|§C6b.10]]); then the same electron at any velocity: the spin sum of the one line as a trace, $\frac12\sum|\bar u'\gamma^0u|^2 = 4E^2(1 - \beta^2\sin^2\frac\theta2)$, Mott's formula, and, beyond the problem set (★), the exact spinor product $\bar u'\gamma^0u$ at equal energies (§C8a.11). A starred section, from Appendix B of the user's notes (reference material, not from a lecture; the course has not treated scalar QED), continues [[§C6c.11 Feynman Rules from the Lagrangian|§C6c.11]] to interactions with derivatives: the momentum rule $\partial_\mu \to -ip_\mu$ for a momentum flowing into the vertex, scalar QED with its vertices $-ie(p + p')^\mu$ and $2ie^2g^{\mu\nu}$, the slow-particle limit, and the interaction Hamiltonian, which is not $-\mathcal L_{\rm int}$ there (★ §C8a.18). Lecture 20 ("Helicity Structure", 16 Nov 2026; PS §5.2; the user's notes, Lecture 20 update), which follows $e^+e^- \to \mu^+\mu^-$ spin by spin, is the subject of the next chapter, [[· C8b Spin, Helicity and Chirality|C8b]]: the helicity sections that stood here as §C8.12–§C8.17★ from 2026-11-16 moved there on 2026-11-18, together with the little-group sections of C3 (user decision), and this chapter was renamed C8a; the steps of a helicity calculation are [[P9 Helicity Amplitudes]]. Lecture 21 ("Crossing Symmetry", 18 Nov 2026, a recorded lecture; PS §5.4; sources: slides and recording) treats a second process, the scattering of an electron off a muon, $e^-\mu^- \to e^-\mu^-$: the one diagram and its amplitude, the spin average as two traces, and the substitution $p \to p_1$, $p' \to -p_1'$, $k \to p_2'$, $k' \to -p_2$ that turns the annihilation result into $\frac{8e^4}{q^4}[(p_1\cdot p_2')(p_1'\cdot p_2) + (p_1\cdot p_2)(p_1'\cdot p_2') - m_\mu^2\,p_1\cdot p_1']$ at $m_e = 0$ (§C8a.12); the centre-of-mass kinematics, the cross section, its high-energy form $\frac{\alpha^2}{2E_{\rm cm}^2}\frac{4 + (1 + \cos\theta)^2}{(1 - \cos\theta)^2}$ and the growth $1/\theta^4$ at small angles from a virtual photon nearly on its mass shell (§C8a.13); crossing symmetry in general with its proof idea, analyticity as the lecture states it, the fermion sign, the Mandelstam variables in the course's form, the two processes as $\frac{2e^4}{s^2}(t^2 + u^2)$ and $\frac{2e^4}{t^2}(s^2 + u^2)$ with $s$ and $t$ exchanged, and the channels (§C8a.14); crossing is a shortcut in [[P8 Unpolarized Cross Section from Diagrams]]. Lecture 22 ("Compton Scattering", 23 Nov 2026; PS §5.5; the user's notes, Lecture 22 update) is the first process with external photons and a virtual electron, $\gamma e^- \to \gamma e^-$: the two diagrams and their relative sign, the simplification $(\slashed p + m)\gamma^\nu u(p) = 2p^\nu u(p)$, and the square as one trace of eight $\gamma$'s for each of four terms, evaluated to $2e^4\bigl[\frac{p\cdot k'}{p\cdot k} + \frac{p\cdot k}{p\cdot k'} + 2m^2\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr) + m^4\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr)^2\bigr]$ (§C8a.15); the Ward identity $k_\mu\mathcal M^\mu(k) = 0$ from current conservation and the replacement $\sum\epsilon^\ast_\mu\epsilon_\nu \to -g_{\mu\nu}$ for external photons (§C8a.16); the Compton formula, the Klein–Nishina and Thomson cross sections, and at high energy the backward peak with $\sigma \simeq \frac{2\pi\alpha^2}{s}\log\frac{s}{m^2}$ (§C8a.17). The helicity suppression of that peak and inverse Compton scattering are in [[· C8b Spin, Helicity and Chirality|C8b]] (§C8b.10). The verification of the Ward identity on the Compton amplitude is Problem Set 12 and is not written yet. The careful quantization of the electromagnetic field (Lecture 25) is pending.

## How C8a relates to Yu and PS
C8a follows the lecture and the user's notes (Parts A, B, C). Yu builds QED the same way in §8.1 and treats the potentials in §8.4.3, with his charge convention $Q_fe$, $e > 0$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^cau-c8a-1-1|§C8a.1, Caution: What e means]]); his photon quantization (§4.4) and propagator (§6.4.4) are the sources of C4, in his notation $e^\mu(p, \sigma)$, $b_{\mathbf p,\sigma}$. PS §4.8 is the lecture's reading. For Lecture 19 the reading is PS §5.1 (the slides cite 5.2, which is Lecture 20); for Lecture 20 PS §5.2, which does the projector-and-trace route and the explicit spinors for massless fermions, while Yu §8.2.4 uses explicit spinors with both masses and §8.3 treats chirality separately; for Lecture 21 PS §5.4, which the lecture follows closely (electron–muon scattering at $m_e = 0$, then crossing symmetry and the Mandelstam variables), with Yu §8.5 for crossing and the Mandelstam variables; for Lecture 22 PS §5.5, which the lecture follows, with Yu §8.6, who writes out the traces, the phase space and the helicity amplitudes in full; Yu treats the same process in §8.2.1–§8.2.3 with all masses kept, the incoming momenta named $k_1, k_2$ and the outgoing $p_1, p_2$, spins labelled by helicities; he does not discuss $R$.

| Section | Lecture, slides | Yu § and eqs. | Yu's setting | PS |
|---|---|---|---|---|
| §C8a.1 | 18: slides 5–6 | §8.1, (8.1)–(8.17), (8.35) | free Dirac Lagrangian, covariant derivative $D_\mu = \partial_\mu + iQ_feA_\mu$, $\mathcal L_{\rm QED}$, $J^\mu_{\rm EM}$; Schrödinger–Pauli limit | §4.1, (4.3)–(4.8); §4.8, (4.129) |
| §C8a.2 | 18: slide 7 | §8.1, (8.2)–(8.9) | global and local U(1), $A_\mu \to A_\mu - \frac1e\partial_\mu\theta$, covariance of $D_\mu\psi$ | §4.1, (4.6) |
| §C8a.3 | 18: slides 8–9, 12–13 | §4.4, (4.184)–(4.193), (4.228)–(4.232), (4.246)–(4.248); §6.4.4, (6.248)–(6.253) | massless polarization basis and weighted completeness; Feynman-gauge expansion; $[b, b^\dagger] \propto -g$; negative-norm temporal state; photon Feynman propagator | §4.8, (4.130)–(4.132), p. 124 |
| §C8a.4 | 18: slides 14–15, 19 | §8.1, rules 1–9; §8.4.3, (8.244) | QED Feynman rules, vertex $-iQ_fe\gamma^\mu$ | §4.8, p. 123, (4.133) |
| §C8a.5 | 18: slides 24–29 | §8.4.3, (8.238)–(8.278), (8.286)–(8.287) | Coulomb potential (as the Yukawa result at $m_\phi = 0$); Yu's own Fourier transform from $1/\lvert\mathbf q\rvert^2$ to the Coulomb potential, (8.259)–(8.263), by a residue (the direct transform with a cutoff: §C8a.10); the absolute sign from contractions; particle–antiparticle | §4.8, pp. 125–126, (4.133)–(4.136) |
| §C8a.6 | 19: slides 2–8 | §8.1, (8.10)–(8.11); §8.2.1, (8.37)–(8.39); §7.1, after (7.41) | several charged species $f$; the amplitude with $Q_e = Q_\mu = -1$; $q^2 = E_{\rm CM}^2 > 4m_\mu^2$ and the dropped $i\epsilon$; real and virtual particles | §5.1, pp. 131–132, (5.1) |
| §C8a.7 | 19: slides 11–15 | §8.2.1, (8.40)–(8.43); §8.2.2, (8.44)–(8.55); §8.2.3, (8.78)–(8.80) | conjugation, Casimir's trick, $\overline{\lvert\mathcal M\rvert^2}$; trace theorems; the two traces and their contraction, all masses | §5.1, pp. 132–135, (5.2)–(5.5), (5.10) |
| §C8a.8 | 19: slides 18–22 | §8.2.3, (8.81)–(8.98) | centre-of-mass kinematics with $\beta_e$, $\beta_\mu$; $d\sigma/d\Omega$ and $\sigma$ with both masses, $m_e \to 0$, high energy; TASSO data | §5.1, pp. 136–138, (5.11)–(5.15) |
| §C8a.9 | 19: slides 23–26 | §8.1, (8.10) | quark species with a colour index; no $R$ | §5.1, pp. 138–141, (5.15)–(5.16) |
| §C8a.10 | Problem Set 10, Problem 2 | §8.4.3, (8.259)–(8.263) | the Fourier transform between $1/\lvert\mathbf q\rvert^2$ and the Coulomb potential, from momentum to position space; no classical external potential | Problem 4.4, pp. 129–130 |
| §C8a.11 | Problem Set 10, Problem 3 | — | — (not cited) | Problem 5.1, first part, p. 169 |
| §C8a.12 | 21: slides 2–8, recording part A | — | — (not cited) | §5.4, pp. 153–154, (5.60)–(5.61) |
| §C8a.13 | 21: slides 11–14, recording part B | — | — (not cited) | §5.4, pp. 154–155, (5.62)–(5.66) |
| §C8a.14 | 21: slides 17–26, recording part C | §8.5, (8.288), (8.290)–(8.296), (8.302)–(8.303), (8.310)–(8.312), (8.315)–(8.318) | crossing symmetry with the fermion sign and a convention for $v$ that removes it; Mandelstam variables for $k_1, k_2 \to p_1, p_2$; the three channels in Yukawa theory; centre-of-mass values for equal masses | §5.4, pp. 155–158, (5.67)–(5.73) |
| §C8a.15 | 22: slides 2–10 | §8.6, (8.321)–(8.324); §8.6.2, (8.348)–(8.349), (8.380)–(8.383) | the two diagrams with the labels $k_1, k_2 \to p_1, p_2$; the simplification with the Dirac equation; the four traces and the unpolarized squared amplitude | §5.5, pp. 158–162, (5.74), (5.81)–(5.82), (5.87) |
| §C8a.16 | 22: slides 3, 9, 12–18 | §8.6.1, (8.325)–(8.337) | the transverse polarization sum with the vector $n$; the current argument and the Ward identity, with its gap noted; the gauge-transformation view; the replacement by $-g_{\mu\nu}$ | §5.5, pp. 159–161, (5.75)–(5.80) |
| §C8a.17 | 22: slides 20–27 | §8.6, (8.319)–(8.320); §8.6.2, (8.384)–(8.401), Figures 8.13–8.14; §8.6.3, (8.402)–(8.411) | Compton's formula, lab kinematics and phase space, Klein–Nishina with a plot for three energies, Thomson; centre-of-mass invariants, the backward divergence and its mass regulator | §5.5, pp. 162–164, (5.88)–(5.96) |
| §C8a.18★ | — (the user's notes, Appendix B) | §11.4.3, (11.482), (11.487)–(11.495) and the closing remark | scalar QED by the path integral; the momentum rule for derivatives; vertices $-iQ_\phi e(p_\mu + q_\mu)$ and $2iQ_\phi^2e^2g_{\mu\nu}$; the non-covariant term of $\mathcal H_I$ | Problem 9.1 (named as reading by the appendix) |

## Sections
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative]] — 513 notes Lecture 18 update §18.1–§18.2; PHY 513 Lecture 18, slides 5–6; PS §4.1, §4.8; Yu §8.1
- [[§C8a.2 Gauge Invariance]] — 513 notes Lecture 18 update §18.3; PHY 513 Lecture 18, slide 7; Yu §8.1, (8.2)–(8.9)
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator]] — 513 notes Lecture 18 update §18.4–§18.5; PHY 513 Lecture 18, slides 8–9, 12–13; PS §4.8, pp. 123–124; Yu §4.4, §6.4.4
- [[§C8a.4 Feynman Rules for QED]] — 513 notes Lecture 18 update §18.6; PHY 513 Lecture 18, slides 14–15, 19; PS §4.8, pp. 123–125; Yu §8.1
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel]] — 513 notes Lecture 18 update §18.7–§18.8; PHY 513 Lecture 18, slides 24–29; PS §4.8, pp. 125–126; Yu §8.4.3
- [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon]] — 513 notes Lecture 19 update §19.1; PHY 513 Lecture 19, slides 2–8; PS §5.1, pp. 131–132; Yu §8.2.1
- [[§C8a.7 The Spin-Averaged Squared Amplitude]] — 513 notes Lecture 19 update §19.2–§19.3; PHY 513 Lecture 19, slides 11–15; PS §5.1, pp. 132–135; Yu §8.2.1, §8.2.3
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production]] — 513 notes Lecture 19 update §19.4; PHY 513 Lecture 19, slides 18–22; PS §5.1, pp. 136–138; Yu §8.2.3
- [[§C8a.9 Quark–Antiquark Production and the Ratio R]] — 513 notes Lecture 19 update §19.4–§19.6; PHY 513 Lecture 19, slides 23–26; PS §5.1, pp. 139–141
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula]] — PHY 513 Problem Set 10, Problem 2; PS Problem 4.4, pp. 129–130; Yu §8.4.3, (8.259)–(8.263)
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field]] — PHY 513 Problem Set 10, Problem 3; PS Problem 5.1 (first part), p. 169
- [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution]] — PHY 513 Lecture 21 (18 Nov 2026, recorded), slides 2–8 and recording part A; PS §5.4, pp. 153–154, (5.60)–(5.61)
- [[§C8a.13 The Cross Section for Electron–Muon Scattering]] — PHY 513 Lecture 21 (18 Nov 2026, recorded), slides 11–14 and recording part B; PS §5.4, pp. 154–155, (5.62)–(5.66)
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables]] — PHY 513 Lecture 21 (18 Nov 2026, recorded), slides 17–26 and recording part C; PS §5.4, pp. 155–158, (5.67)–(5.73); Yu §8.5
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square]] — PHY 513 Lecture 22 (23 Nov 2026), slides 2–10; 513 notes, Lecture 22 update, §22.1; PS §5.5, pp. 158–162, (5.74), (5.81)–(5.82), (5.87); Yu §8.6, (8.321)–(8.324), §8.6.2
- [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations]] — PHY 513 Lecture 22 (23 Nov 2026), slides 3, 9, 12–18; 513 notes, Lecture 22 update, §22.2; PS §5.5, pp. 159–161, (5.75)–(5.80); Yu §8.6.1
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy]] — PHY 513 Lecture 22 (23 Nov 2026), slides 20–27; 513 notes, Lecture 22 update, §22.3–§22.4; PS §5.5, pp. 162–164, (5.88)–(5.96); Yu §8.6.2–§8.6.3
- [[§C8a.18★ Derivative Couplings and Scalar QED]] — 513 notes Appendix B (2026-11-14), section "Derivative couplings"; Yu §11.4.3, (11.482), (11.487)–(11.495)

## Principles
- [[§C8a.2 Gauge Invariance#^pr-c8a-2-1|§C8a.2.1]] Gauge Symmetry of QED
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^pr-c8a-5-8|§C8a.5.8]] Attraction and Repulsion by the Spin of the Exchanged Particle
- [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|§C8a.6.4]] Particles Mediating an Interaction Are Off Shell
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|§C8a.14.1]] Crossing Symmetry
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|§C8a.14.2]] The Amplitude Is an Analytic Function of the External Momenta
- [[§C8a.18★ Derivative Couplings and Scalar QED#^pr-c8a-18-1|§C8a.18.1]] Derivatives in the Vertex

## Theorems
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-2|§C8a.1.2]] The Interaction Hamiltonian of QED
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|§C8a.1.3]] The QED Coupling Is e Times the Conserved Current
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-4|§C8a.1.4]] The Condensed Form of the QED Lagrangian
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-5|§C8a.1.5]] The Covariant Derivative Is Minimal Coupling
- [[§C8a.2 Gauge Invariance#^thm-c8a-2-2|§C8a.2.2]] The Covariant Derivative Transforms Covariantly
- [[§C8a.2 Gauge Invariance#^thm-c8a-2-3|§C8a.2.3]] The QED Lagrangian Is Gauge Invariant
- [[§C8a.2 Gauge Invariance#^thm-c8a-2-4|§C8a.2.4]] A Local Phase Needs the Compensating Shift of the Potential
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-1|§C8a.3.1]] The Quantized Photon Field in the Course's Form
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-2|§C8a.3.2]] The Photon Field Is Real: the Photon Is Neutral
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-3|§C8a.3.3]] Why Only Transverse Polarizations Are Physical
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-4|§C8a.3.4]] The Weighted Completeness Relation
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|§C8a.3.5]] The Photon Propagator
- [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-6|§C8a.3.6]] Lorentz Invariance versus Positivity: the Wrong-Sign Component
- [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|§C8a.4.1]] The External Photon Wave Functions
- [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|§C8a.4.2]] Photon Fields Contract in Pairs or with External Photons, without Signs
- [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|§C8a.4.3]] The QED Vertex
- [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|§C8a.4.4]] Feynman Rules for iℳ in QED
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-1|§C8a.5.1]] The Vector Spinor Products in the Nonrelativistic Limit
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-2|§C8a.5.2]] The Nonrelativistic QED Amplitude for Distinguishable Fermions
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-3|§C8a.5.3]] The Coulomb Potential
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-4|§C8a.5.4]] The Antiparticle Spinor Products in the Nonrelativistic Limit
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-5|§C8a.5.5]] The Sign from the Contractions: Plus for Two Particles, Minus for Particle and Antiparticle
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-6|§C8a.5.6]] The Sign of ℳ Relative to the Unscattered Term Is Physical
- [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-7|§C8a.5.7]] In QED Like Charges Repel and Opposite Charges Attract
- [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|§C8a.6.2]] The Amplitude for Electron–Positron Annihilation into a Muon Pair
- [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-3|§C8a.6.3]] The Photon of the Annihilation Diagram Is Timelike and Off Shell
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|§C8a.7.1]] The Complex Conjugate of a Vector Bilinear Reverses It
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-2|§C8a.7.2]] The Squared Amplitude for Fixed Spins
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|§C8a.7.3]] A Spin-Summed Fermion Line Is a Trace
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|§C8a.7.4]] The Spin-Averaged Squared Amplitude as Two Traces
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-5|§C8a.7.5]] The Electron Trace and the Muon Trace
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|§C8a.7.6]] The Spin-Averaged Squared Amplitude in Invariants
- [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|§C8a.7.7]] The Unpolarized Squared Amplitude in General (Casimir's Trick)
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-1|§C8a.8.1]] The Momenta in the Centre-of-Mass Frame
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-2|§C8a.8.2]] The Invariants in the Centre-of-Mass Frame
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|§C8a.8.3]] The Spin-Averaged Squared Amplitude in the Centre-of-Mass Frame
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-4|§C8a.8.4]] The Unpolarized Differential Cross Section
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-5|§C8a.8.5]] The Total Cross Section at High Energy
- [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-6|§C8a.8.6]] The Total Cross Section with the Muon Mass
- [[§C8a.9 Quark–Antiquark Production and the Ratio R#^thm-c8a-9-1|§C8a.9.1]] The Cross Section for Quark–Antiquark Production
- [[§C8a.9 Quark–Antiquark Production and the Ratio R#^thm-c8a-9-2|§C8a.9.2]] R Counts the Quarks, Weighted by Charge Squared
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-2|§C8a.10.2]] The First-Order S-Matrix Element in an External Field
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-3|§C8a.10.3]] Of the Four Terms of the Current, One Scatters and One Is the Unscattered Electron Times a Vacuum Value
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-4|§C8a.10.4]] A Time-Independent Potential Conserves the Energy
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-5|§C8a.10.5]] The Feynman Rule for a Vertex with an External Field
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-6|§C8a.10.6]] The Fourier Transform of the Coulomb Potential
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-7|§C8a.10.7]] The Momentum Transfer at Fixed Energy
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-8|§C8a.10.8]] The Rutherford Formula
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-9|§C8a.10.9]] In the Nonrelativistic Limit the Amplitude Is the Born Amplitude of the Potential Energy eA₀
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^thm-c8a-10-10|§C8a.10.10]] The Total Rutherford Cross Section Is Infinite (ADDED)
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-1|§C8a.11.1]] The Amplitude for an Electron of Any Velocity in the Coulomb Field
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-2|§C8a.11.2]] The Spin-Summed Vector Product in an External Coulomb Field
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-3|§C8a.11.3]] Mott's Formula
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-4|§C8a.11.4]] ★ The Exact Vector Spinor Product at Equal Energies
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-5|§C8a.11.5]] ★ The Spin-Summed Product from the Exact Form, without a Trace of γ Matrices
- [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-6|§C8a.11.6]] ★ The Spin-Dependent Term Points along the Normal of the Scattering Plane
- [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|§C8a.12.1]] The Amplitude for Electron–Muon Scattering
- [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2|§C8a.12.2]] The Spin-Averaged Squared Amplitude as Two Traces
- [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|§C8a.12.3]] The Crossing Substitution Maps Annihilation onto Scattering
- [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|§C8a.12.4]] The Spin-Averaged Squared Amplitude for Electron–Muon Scattering
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-1|§C8a.13.1]] The Momenta of Electron–Muon Scattering in the Centre-of-Mass Frame
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|§C8a.13.2]] The Invariants of Electron–Muon Scattering in the Centre-of-Mass Frame
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|§C8a.13.3]] The Spin-Averaged Squared Amplitude of Electron–Muon Scattering in the Centre-of-Mass Frame
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-4|§C8a.13.4]] The Unpolarized Cross Section for Electron–Muon Scattering
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-5|§C8a.13.5]] Electron–Muon Scattering in the Ultrarelativistic Limit
- [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|§C8a.13.6]] At Small Angles the Cross Section Grows as 1/θ⁴
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|§C8a.14.3]] Crossing a Fermion Changes the Sign of Its Spin Sum
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-4|§C8a.14.4]] Annihilation in the s-Channel
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|§C8a.14.5]] Scattering in the t-Channel
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|§C8a.14.6]] Crossing Exchanges s and t
- [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|§C8a.14.7]] The Mandelstam Variables in the Centre-of-Mass Frame for Equal Masses
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|§C8a.15.1]] The Amplitude for Compton Scattering
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-2|§C8a.15.2]] The Two Compton Diagrams Have the Same Sign
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|§C8a.15.3]] The Denominators of the Two Propagators
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|§C8a.15.4]] The Dirac Equation Simplifies the Numerator
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|§C8a.15.5]] The Simplified Compton Amplitude
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|§C8a.15.6]] The Square Is One Trace of Eight γ's for Each Term
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|§C8a.15.7]] The Spin- and Polarization-Averaged Squared Amplitude of Compton Scattering
- [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|§C8a.15.8]] The Result Depends on Two Invariants
- [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1|§C8a.16.1]] The Physical Sum and the Invariant Sum
- [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|§C8a.16.2]] The Ward Identity
- [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|§C8a.16.3]] The Polarization Sum for External Photons
- [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-4|§C8a.16.4]] The Ward Identity for the Compton Amplitude
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|§C8a.17.1]] The Compton Formula
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-2|§C8a.17.2]] Two-Body Phase Space in the Lab Frame
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-3|§C8a.17.3]] The Squared Amplitude in the Lab Frame
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|§C8a.17.4]] The Klein–Nishina Formula
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-5|§C8a.17.5]] The Thomson Limit
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-6|§C8a.17.6]] The Invariants in the Centre-of-Mass Frame
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|§C8a.17.7]] At High Energy Compton Scattering Peaks in the Backward Direction
- [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|§C8a.17.8]] The Electron Mass Keeps the Total Cross Section Finite
- [[§C8a.18★ Derivative Couplings and Scalar QED#^thm-c8a-18-3|§C8a.18.3]] The Interaction Lagrangian of Scalar QED
- [[§C8a.18★ Derivative Couplings and Scalar QED#^thm-c8a-18-4|§C8a.18.4]] The Three-Point Vertex of Scalar QED
- [[§C8a.18★ Derivative Couplings and Scalar QED#^thm-c8a-18-5|§C8a.18.5]] The Four-Point (Seagull) Vertex of Scalar QED
- [[§C8a.18★ Derivative Couplings and Scalar QED#^thm-c8a-18-6|§C8a.18.6]] For a Slow Particle the Scalar Vertex Is the Dirac Vertex
- [[§C8a.18★ Derivative Couplings and Scalar QED#^thm-c8a-18-7|§C8a.18.7]] The Interaction Hamiltonian of Scalar QED Has a Non-Covariant Term
- [[§C8a.18★ Derivative Couplings and Scalar QED#^lem-c8a-18-8|§C8a.18.8]] The Time-Ordered Product of Two Time Derivatives Has a Contact Term

## Models
- [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|§C8a.1.1]] Quantum Electrodynamics
- [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|§C8a.6.1]] QED with Several Charged Dirac Fields
- [[§C8a.10 Scattering off an External Potential꞉ the Rutherford Formula#^mod-c8a-10-1|§C8a.10.1]] The Dirac Field in a Classical External Potential
- [[§C8a.18★ Derivative Couplings and Scalar QED#^mod-c8a-18-2|§C8a.18.2]] Scalar QED
