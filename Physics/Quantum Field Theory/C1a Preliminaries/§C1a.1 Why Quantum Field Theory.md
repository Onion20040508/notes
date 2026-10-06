---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
↑ [[· C1a Preliminaries]] · [[§C1a.2 Natural Units and Dimensional Analysis]] →

*Sources: the user's PHY 513 notes, Ch. 1 §1.1 and §1.8 · PHY 513 Lecture 1 (Larsen, 31 Aug 2026), Part A; Lecture 2 (2 Sep 2026), Part A · Peskin & Schroeder §2.1, pp. 13–14 · Yu §1.1 · the user's pre-course notes, §1.1.*

Why must a theory that is both quantum and relativistic be a theory of fields? Quantum Mechanics C13★ read the Klein–Gordon and Dirac equations as wave equations for one particle and found where that reading fails ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^rem-c13-1-2|QM Remark: What the negative energies could mean]], [[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]); Relativity read the Klein–Gordon equation as a classical field equation ([[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]]); and [[§C12.2★ Second Quantization]] built one Hilbert space for any number of identical particles. This section gives the course's three reasons for fields, adds the failure that is not a defect of any equation but of single-particle mechanics itself (causality, [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]]), maps each failure to the place where the quantum field repairs it, and lays out the plan. What a field is, and how it transforms, is [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-1|Def. §C1b.1.1]].

## Three reasons for fields

> [!law] Law §C1a.1.1: Particle Number Is Not Conserved
> In relativistic processes particles are created and annihilated. Particle–antiparticle pairs appear when enough energy is available ($\gamma \to e^+e^-$ near a nucleus, above $2m_ec^2$) and disappear ($e^+e^- \to \gamma\gamma$); photons are emitted and absorbed one at a time. Additive quantum numbers such as electric charge are conserved in every such process; the number of particles is not.
>
> *Valid when:* energy transfers are comparable to the rest energies involved; for massless quanta, at any energy.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.1 (Motivations 1–2) · PHY 513 Lecture 1, Part A ("Motivation 1: Technical") · PS §2.1, p. 13*

^law-c1a-1-1

> [!remark] Remark: One quantum theory for any number of particles
> Nonrelativistic quantum mechanics has a separate wave function $\psi(\mathbf x_1, \dots, \mathbf x_N)$ for each $N$ and no mechanism that turns one particle into three. [[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1|Law §C1a.1.1]] makes that untenable, and not only above threshold: in second-order perturbation theory multiparticle intermediate states appear at any energy, for times allowed by $\Delta E\,\Delta t \sim \hbar$, and at higher orders arbitrarily many such virtual particles (PS). A relativistic quantum theory must therefore be one theory for any number of particles. That structure is a quantum field: its Hilbert space is the Fock space of all particle numbers ([[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]]), and its amplitude encodes the number: a state of definite particle number has no mean field ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-1|Theorem §C2a.6.1]]), and a classical field is a coherent superposition of all numbers. A classical source coupled to the field does create particles ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3|Theorem §C2b.8.3]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.1 (Motivation 1) · PS §2.1, p. 13*

^rem-c1a-1-1

> [!remark] Remark: Electromagnetism forces relativity and photons
> Someone interested only in a quantum version of electromagnetism meets relativity anyway: electromagnetic waves move at $c$. By [[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1|Law §C1a.1.1]] photons are then created and absorbed freely, so the theory must describe any number of relativistic massless particles, and their interaction with matter. Quantum electrodynamics is the central goal of the course; theories of the other interactions are modelled on it, and it is needed wherever electromagnetism is, in particle, atomic and optical physics.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.1 (Motivation 2) · PHY 513 Lecture 1, Part A ("Motivation 2: 'Practical'")*

^rem-c1a-1-2

> [!remark] Remark: Fields as the long-distance description
> Physical systems may be discrete at the smallest scales, but viewed from far enough away discrete things look continuous: atoms make gases and fluids, and continuum mechanics is field theory. The excitations of a continuous medium are waves, and quantum mechanics reads waves as particles: sound is phonons. The argument looks hand-waving and is in fact general: whatever happens below the scales we can measure, the description at the scales we do measure is a field, with its waves appearing as particles. Dimensional analysis makes this operational: interactions whose couplings have negative mass dimension are suppressed at long distances ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]), so a long-distance theory is fixed by symmetry up to a few terms. This declines to describe the smallest scales; it is not claimed to be the final answer, nor that it is "field theories all the way down" (the theories written here break down at very short distances), but it is the language in which one asks why the world is the way it is.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.1 (Motivation 3 and Discussion) · PHY 513 Lecture 1, Part A ("Motivation 3: Conceptual", "Foundations of Physics")*

^rem-c1a-1-3

> [!remark] Remark: Where quantum field theory is used
> In particle physics it unifies matter (electrons, quarks) and interactions (photons, gluons); this is the course's emphasis. In atomic, molecular and optical physics it supplies the quantum theory of the photon and the radiative corrections, such as the Lamb shift. In condensed matter, quantum many-body physics is nonrelativistic field theory: the fields are emergent, particle number is not conserved, and the same principles hold with less symmetry. Quasiparticles are the condensed-matter route to the same structure: start from many electrons with no small parameter, take a continuum description, and its quantized waves are the quasiparticles, phonons being the simplest. This is also why free-particle approximations work far better than naive estimates suggest.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.1 ("Applications", Discussion) · PHY 513 Lecture 1, Part A ("Applications of Quantum Field Theory")*

^rem-c1a-1-4

## Why single-particle relativistic quantum mechanics fails

> [!remark] Remark: Five failures and where each is repaired
> | Failure of the single-particle reading | Shown in | What the quantum field does | Where |
> | --- | --- | --- | --- |
> | Energy unbounded below: $E = -E_{\mathbf p}$ solves the Klein–Gordon equation, so there is no stable ground state | [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2\|QM Theorem §C13.1.2]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^rem-c13-1-2\|QM Remark: What the negative energies could mean]] | negative frequencies multiply creation operators; $H = \int E_{\mathbf p}a^\dagger a$ is positive | [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4\|Theorem §C2b.1.4]], [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4\|Remark: Negative frequency is creation, not negative energy]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1\|Theorem §C2a.3.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2\|Theorem §C2a.4.2]] |
> | The conserved density is not positive, $\rho \propto E$ | [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1\|QM Theorem §C13.1.1]] | it is a charge density: particles minus antiparticles | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6\|Theorem §C2a.5.6]], [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-3\|Remark: Charge, not probability]] |
> | The particle number is fixed | [[§C1a.1 Why Quantum Field Theory#^law-c1a-1-1\|Law §C1a.1.1]] | one Fock space for all numbers | [[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1\|Principle §C2a.4.1]] |
> | Propagation outside the light cone | [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6\|Theorem §C1a.3.6]] | the commutator of fields vanishes at spacelike separation | [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5\|Theorem §C2b.4.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7\|Theorem §C2b.4.7]] |
> | Dirac's sea: infinite charge, a one-body equation read as a many-body state, no help for bosons | [[§C13.2★ The Dirac Equation#^rem-c13-2-7\|QM Remark: The Dirac sea, the positron, and CPT]] | an anticommuting field that annihilates electrons and creates positrons | [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1\|Theorem §C5b.2.1]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3\|§C5b.5, Remark: The Dirac sea, read in the field]] |
>
> The first two are one defect seen twice: for a plane wave the Klein–Gordon density is $E/mc^2$ times $|N|^2$, so the negative energies are the negative densities. PS skip them ("this discussion usually takes place near the end of a graduate-level quantum mechanics course") and make the third and fourth the reasons for fields.
>
> *Source: the user's pre-course notes, §1.1 (Key points "Two difficulties of the Klein–Gordon equation", "How field theory resolves the difficulties") · Yu §1.1 · PS §2.1, pp. 13–14 · the user's PHY 513 notes, Ch. 2 §2.2*

^rem-c1a-1-5

> [!remark] Remark: Hole theory, and why it is not enough
> Dirac's first-order equation removes the negative densities but not the negative energies. His remedy fills every negative-energy state; the Pauli principle then keeps positive-energy electrons out of them, and a missing electron of charge $-e$ and energy $-|E|$ behaves as a particle of charge $+e$ and energy $+|E|$, the positron, observed by Anderson in 1932 ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]). Three problems remain: the infinite charge density of the sea produces no observed field; an equation introduced for one particle is interpreted through infinitely many; and bosons, which obey no exclusion principle, cannot be helped this way. That a relativistic wave equation for one particle runs into so many difficulties suggests that the framework itself must change.
>
> *Source: Yu §1.1 · the user's pre-course notes, §1.1 (Key point "Problems with hole theory")*

^rem-c1a-1-6

> [!remark] Remark: Time is a parameter, position an operator
> In quantum mechanics position is an observable, the operator $\hat{\mathbf x}$, while time is a parameter on which the state depends, the eigenvalue of no Hermitian operator ([[§C3.3 The Schrödinger and Heisenberg Pictures#^def-c3-3-1|QM Def. §C3.3.1]]). Relativity mixes the two, so a relativistic quantum theory cannot treat them this differently. Two ways out: promote time to an operator, which is very hard to carry through, or demote position to a label. Quantum field theory takes the second: at every point $\mathbf x$ there is an operator $\phi(\mathbf x)$, and in the Heisenberg picture $\phi(t, \mathbf x) = e^{iHt}\phi(\mathbf x)e^{-iHt}$ carries $t$ and $\mathbf x$ on an equal footing, both as labels ([[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]]). The demotion has a classical precedent: in the continuum limit of a chain of masses the index of each mass becomes the coordinate $x$ of a displacement field ([[§B3.2 The Continuum Limit and the Wave Equation#^def-b3-2-1|WO Def. §B3.2.1]]). It also removes an awkwardness: the position operator has no eigenvectors ([[§37 Position Eigenstates and Continuous Resolutions#^prop-37-3|556 Prop. §37.3]]), whereas a label needs none. The price is that $\phi(\mathbf x)$ at a point is not an operator either, only after smearing ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]).
>
> *Source: Yu §1.1, eq. (1.4) · the user's PHY 513 notes, Ch. 1 §1.1 ("A fourth view") · the user's pre-course notes, §1.1 ("The asymmetry between time and space", Remark "Precedent in the classical continuum limit")*

^rem-c1a-1-7

## The plan

> [!remark] Remark: The plan of the course and of these notes
> The course has three blocks: Lectures 1–12 treat classical fields and relativity, then free relativistic quantum fields of spin $0$ and spin $\frac12$; Lectures 13–22 treat interactions and Feynman diagrams, applied to quantum electrodynamics; Lectures 23–26 review and add path integrals ([[PHY 513 Course Log]]). These notes follow Yu's chapters instead: C1a preliminaries (this chapter: units, causality, the Lorentz group and tensors) and C1b classical field theory (the scalar field, the action, the Hamiltonian formalism, Noether's theorem), C2a the scalar field and C2b its two-point functions and propagators, then the Poincaré group and particle states, vector and spinor fields, interactions, Feynman diagrams, QED, discrete symmetries, the S-matrix and path integrals ([[· C3 Poincaré Symmetry and Particle States|C3]], [[· C4 The Quantum Vector Field|C4]], [[· C5a Spinors and the Dirac Equation|C5a]], [[· C5b The Quantum Spinor Field|C5b]]; C6–C11, planned). A theory of particles is built by one workflow:
> 1. specify the particle content, one field per species;
> 2. write a Lorentz-invariant Lagrangian of those fields ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|Def. §C1b.2.1]]);
> 3. derive Feynman rules from it and draw the diagrams of a process (QFT C6–C7, planned);
> 4. compute the invariant amplitude, and from it cross sections and decay rates (QFT C8, C10, planned).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.8 · the user's pre-course notes, §1.1 ("Interactions of quantum fields") · Yu §1.1*

^rem-c1a-1-8

> [!remark]- Connections
> - The Klein–Gordon density of [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]] and the U(1) Noether charge density of the complex field ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]) are the same expression; read as a charge it counts particles minus antiparticles ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]]), and its indefinite sign stops being a defect.
> - Pair creation has a threshold fixed by four-momentum conservation ([[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]]); the annihilation photons of [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|Example §C1a.2.1]] are the reverse process.
> - The Lamb shift, the discrepancy between the Dirac levels and measurement ([[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^ex-c13-3-1|QM Example §C13.3.1]]), is a radiative correction of quantum electrodynamics (QFT C8, planned): the AMO reason for fields.
> - Phonons ([[§B11.2★ Phonons and the Debye Model#^def-b11-2-1|TH Def. §B11.2.1]]) are the quanta of the displacement field of a crystal, the textbook case of "waves of a continuum read as particles"; photons in a cavity ([[§B11.1★ Blackbody Radiation from Statistical Mechanics|TH §B11.1★]]) are the relativistic case.
> - Second quantization ([[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]], [[§C12.2★ Second Quantization#^def-c12-2-3|QM Def. §C12.2.3]]) is nonrelativistic field theory with fixed particle number per sector; the relativistic field adds the invariant normalization and measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and mixes the sectors once interactions are present.
> - Locality, causality and symmetry, the three principles the course names ([[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-1|Remark: The three principles of quantum field theory]]), answer the three motivations: locality makes the long-distance description a field theory, causality forces antiparticles and many particles ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|Remark: Two orderings that cancel; why antiparticles must exist]]), and symmetry fixes the Lagrangian up to a few terms.
