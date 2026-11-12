---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.8 From the Question to the Formula]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.2 Contractions with External Fermions]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026, "Yukawa Theory"), slides 2, 5–8 (Part A), 26–28 (Part C), and transcript · the user's PHY 513 notes, Lecture 17 update, §17.1 (paragraph "Why fermions bring nothing new to the derivation"), §17.2 (Definition "Yukawa theory", paragraph "Filled in: $H_I = -L_I$ and the dimension of $g$", Principle "The Yukawa vertex", paragraph "The arrows", Figure "yukvertex") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.1, p. 79, eq. (4.9), p. 80 (renormalizable interactions); §4.7, p. 115 ("Lorentz invariance requires that the interaction Hamiltonian $H_I$ be a product of an even number of spinor fields"), p. 116, eq. (4.112); p. 120 ("the product $(\bar\psi\psi)$, or any other pair of fermions, *commutes* with any operator") · Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.1)–(7.5), (7.28), pp. 265–267 (fermion lines and fermion-number flow).*

Lecture 17 does for a theory with fermions what Lectures 15–16 did for $\phi^4$: Feynman rules for the amplitude. The logic is that of [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]] and [[§C6c.2 Contractions with External Particles|§C6c.2]]–[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] and is not repeated: fermions add nothing new to it, and any question about the logic is settled for the scalars. What is new is bookkeeping: fermions carry spin, come as particles and antiparticles, and anticommute. This section states the theory, Yukawa theory ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]), shows why fermions entering the Hamiltonian in pairs leave the interaction picture and the Dyson series untouched ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]), derives the vertex $-ig$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]), which is $i\mathcal L_{\rm int}$ with the fields stripped ([[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]]), and its fermion-number arrows ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]), and closes with Part C of the lecture, renormalizability ([[§C6d.1 Yukawa Theory#^def-c6d-1-2|Def. §C6d.1.2]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-6|Theorem §C6d.1.6]]). The external fermions are [[§C6d.2 Contractions with External Fermions|§C6d.2]], the signs of Wick's theorem and the contraction rule [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule|§C6d.3]], first and second order [[§C6d.4 First Order|§C6d.4]]–[[§C6d.5 Second Order|§C6d.5]], the rules [[§C6d.6 Momentum-Space Feynman Rules|§C6d.6]]. Yu develops the same theory in §7.1, PS in §4.7.

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], an instance of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with a fermion: a permanent interaction, the interaction picture on the free Fock space, free relativistic states over $|0\rangle$ in place of the in and out states at lowest order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; beyond it $\sqrt Z$, [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). Theorem §C6d.1.2 and Definition §C6d.1.1 are operator and bookkeeping statements, exact.

*Conventions* ([[Larsen PHY 513]]): $\hat\psi \equiv \hat\psi_I$, $\hat{\bar\psi} \equiv \hat{\bar\psi}_I$, $\hat\phi \equiv \hat\phi_I$ are interaction-picture (free) fields ([[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]]); the subscript $I$ is dropped in this chapter as on slides 16–22. The coupling is $g$ (Yu: $\kappa$). The scalar line is dashed, the fermion line solid with an arrow ([[§C6d.6 Momentum-Space Feynman Rules#^rem-c6d-6-2|§C6d.6, Remark: Dashed and solid]]).

## The model

> [!model] Model §C6d.1.1: Yukawa Theory
> A real scalar $\phi$ of mass $m_\phi > 0$ and a Dirac field $\psi$ of mass $m > 0$ with
>
> $$
> \mathcal L = \underbrace{\tfrac12(\partial_\mu\phi)^2 - \tfrac12m_\phi^2\phi^2}_{\mathcal L_\phi} + \underbrace{\bar\psi(i\slashed{\partial} - m)\psi}_{\mathcal L_\psi} \;\underbrace{-\,g\,\bar\psi\psi\,\phi}_{\mathcal L_{\rm int}} , \qquad \hat H = \hat H_{\rm Dirac} + \hat H_{\text{Klein–Gordon}} + \int d^3x\;g\,\hat{\bar\psi}\hat\psi\hat\phi ,
> $$
>
> $g$ a real coupling, $\bar\psi\psi = \bar\psi_a\psi_a$ summed over the spinor index (the scalar bilinear $\mathsf S$ of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).
> 1. *Structure.* The state space is $\mathcal F_\phi \otimes \mathcal F_\psi$, the bosonic Fock space of the free scalar ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], mass $m_\phi$) times the fermionic Fock space of the free Dirac field ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]: particles and antiparticles of mass $m$, two spin states each), with free vacuum $|0\rangle = |0\rangle_\phi \otimes |0\rangle_\psi$. $\hat H_0 = \hat H_{\text{Klein–Gordon}} + \hat H_{\rm Dirac}$ supplies the mode expansions and the propagators; the interaction-picture fields $\hat\phi$, $\hat\psi$, $\hat{\bar\psi}$ are the free fields of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]] (slide 2), scalar and fermion operators commuting.
> 2. *Interaction.* $\mathcal L_{\rm int}$ has no time derivatives, so the conjugate momenta $\pi_\phi = \dot\phi$, $\pi_\psi = i\psi^\dagger$ are those of the free theory and $\mathcal H_{\rm int} = -\mathcal L_{\rm int} = g\,\bar\psi\psi\phi$, as for $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-4|Theorem §C6a.1.4]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]]); in the interaction picture $\hat H_I(t) = \int d^3x\,g\,\hat{\bar\psi}\hat\psi\hat\phi(t, \mathbf x)$.
> 3. *Coupling.* $[g] = 0$: dimensionless, like $\lambda$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|Example §C1b.3.2]]; slide 27).
> 4. *Symmetry.* $\mathcal L$ is invariant under the U(1) $\psi \to e^{i\alpha}\psi$ of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]], $\phi$ neutral, so fermion number is conserved ([[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]); with $\phi$ a scalar (positive intrinsic parity) it is parity invariant; the pseudoscalar coupling $\mathcal L_{\rm int} = -g'\,\bar\psi i\gamma^5\psi\,\phi$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-6|Theorem §C6d.1.6]]) is the alternative for a pseudoscalar $\phi$ ([[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase#^rem-c9-5-2|§C9.5, Remark: Which parity a real field has is decided by its interactions]]).
>
> *Equivalence:* this is [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with a fermion. It is not a polynomial in real or complex scalar fields of [[§C6a.14 Feynman Rules for Polynomial Interactions#^def-c6a-14-1|Def. §C6a.14.1]], but a monomial in the three field symbols $\bar\psi_a$, $\psi_a$, $\phi$, each to the first power; what carries over from §C6a.14: the vertex as $i$ times the coefficient times the leg permutations (here $1$), one propagator per contraction, momentum conservation, one $\int\frac{d^4q}{(2\pi)^4}$ per loop; what changes: the fermion fields anticommute (signs, [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule|§C6d.3]]), carry a spinor index ($4\times4$ matrices along a line), and external fermions carry spinors ([[§C6d.2 Contractions with External Fermions|§C6d.2]]).
>
> *Assumptions:* those of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (unique gapped vacuum $|\Omega\rangle$, stable particles of mass $m_\phi$ and $m$, $g$ small); for decays, $m_\phi > 2m$ makes the scalar unstable ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]), outside assumption 2 as in [[§C6b.5 Decay Widths#^cau-c6b-5-1|§C6b.5, Caution: Free states in a decay amplitude]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* the theory itself; its $S$-matrix by the rules of [[§C6d.6 Momentum-Space Feynman Rules|§C6d.6]] at lowest order exactly, beyond it with $\sqrt Z$ and the physical masses.
>
> *Source: PHY 513 Lecture 17, slide 7 ("$H_{\rm Yukawa} = H_{\rm Dirac} + H_{\text{Klein–Gordon}} + \int d^3x\,g\bar\psi\psi\phi$ … the simplest interacting theory with fermions"), slide 2 (mode expansions), and transcript ("think about the Yukawa theory as simply being like the $\phi^4$ theory with fermions") · the user's PHY 513 notes, Lecture 17 update, §17.2, Definition "Yukawa theory", eq. (yukawaL), paragraph "Filled in: $H_I = -L_I$" · PS §4.1, p. 79, eq. (4.9); §4.7, eq. (4.112) · Yu §6.1, p. 200, eqs. (6.6)–(6.9), (6.12) ($\mathcal L_Y = -\kappa\phi\bar\psi\psi$; the U(1) of $\psi$; $\mathcal H_1 = -\mathcal L_1$); §7.1, eq. (7.1) · item 4 (parity) written here*

^mod-c6d-1-1

## Fermions in pairs

> [!theorem] Theorem §C6d.1.2: Fermions Enter in Pairs: No New Signs in the Interaction Picture
> Call a **package** a product of operators at one time $t$ that contains an even number of fermion fields (any number of scalar fields), e.g. $\hat{\mathcal H}_I(t, \mathbf x) = g\,\hat{\bar\psi}_a\hat\psi_a\hat\phi(t, \mathbf x)$ or $\hat H_I(t)$.
> 1. Moving a product of $2k$ fermion factors past a product of $r$ fermion factors takes $2kr$ exchanges of two fermion factors: an even number, so no sign (scalar factors move freely).
> 2. For packages $B_1, \dots, B_n$ at times $t_1, \dots, t_n$, the fermionic time ordering of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], applied to all fermion fields with the fields of one package kept in their order, is the product of the packages in time order with no sign:
>
> $$
> T\{B_1\cdots B_n\} = B_{\sigma(1)}\cdots B_{\sigma(n)} , \qquad t_{\sigma(1)} \ge t_{\sigma(2)} \ge \cdots \ge t_{\sigma(n)} .
> $$
>
> 3. Hence $T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\}$ is the time-ordered product of [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], and Dyson's formula $U(t, t') = T\{\exp[-i\int_{t'}^tdt''\,\hat H_I(t'')]\}$ ([[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-2|Theorem §C6a.4.2]]), the projection by $T \to \infty(1 - i\varepsilon)$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-2|Theorem §C6a.5.2]]), and $\langle f|\hat S|i\rangle = {}_0\langle f|T\{e^{-i\int\hat H_I}\}|i\rangle_0$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]) hold in Yukawa theory as stated for scalars.
>
> Signs appear only when a package is taken apart: when one of its fermion fields is contracted with a field of another package or with an external particle ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule|§C6d.3]]).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* parts 1–2 any fermion operators (combinatorics of reordering); part 3 any interaction Hamiltonian built of packages, i.e. every Lorentz-invariant, fermion-number-conserving $\mathcal H_{\rm int}$ (Yukawa, QED).
>
> *Source: PHY 513 Lecture 17, slide 6 ("Caution: fermion fields anticommute. Free Hamiltonian $H_0$ and interaction Hamiltonian $H_I$ depend on fermions only in pairs (due to Lorentz invariance) ⇒ introduction of time evolution operator and interaction picture identical to bosonic theory"), and transcript ("You get them in pairs, and once they're in pairs, they behave as a unit as if they were bosons") · the user's PHY 513 notes, Lecture 17 update, §17.1, paragraph "Why fermions bring nothing new to the derivation" (a paragraph there, a theorem here) · PS §4.7, p. 115, p. 120 · proof written here*

^thm-c6d-1-2

> [!derivation]- Derivation
> **Step 1** (part 1: count). Write $A = f_1\cdots f_{2k}$ and $C = h_1\cdots h_r$ (fermion factors only; scalar factors commute with everything fermionic and with each other at the level of this counting). To bring $A$ from the left of $C$ to its right, move $f_{2k}$ past $h_1, \dots, h_r$ ($r$ exchanges), then $f_{2k-1}$ ($r$ more), …, then $f_1$: in total $2k \cdot r$ exchanges, each costing $-1$ in an anticommuting product:
>
> $$
> AC \to (-1)^{2kr}\,CA = CA \quad\text{(as a reordering inside } T \text{ or } :\;: \text{, where fermion factors are treated as anticommuting).}
> $$
>
> **Step 2** (part 2: blocks). By [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], $T\{\cdots\} = (-1)^P\times$(the fields with times decreasing), $P$ the number of fermion exchanges made. The fields of $B_j$ share the time $t_j$ and keep their order, so the reordering moves whole packages. Any permutation $\sigma$ of $n$ blocks is a product of exchanges of two neighbouring blocks; exchanging neighbours $B_j$ ($2k_j$ fermion fields) and $B_{j'}$ ($2k_{j'}$) costs $(2k_j)(2k_{j'})$ fermion exchanges by Step 1, an even number. So $(-1)^P = +1$ and $T\{B_1\cdots B_n\} = B_{\sigma(1)}\cdots B_{\sigma(n)}$.
>
> **Step 3** (part 3: the derivations that use $T$). Dyson's formula ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-2|Theorem §C6a.4.2]]) is derived from $i\partial_tU = \hat H_I(t)U$ by iterating and ordering the factors $\hat H_I(t_k)$ by their times; it uses only that each $\hat H_I(t_k)$ is one operator, and its $T$ orders these operators without sign. By Step 2 that is the same as the fermionic $T$ of all the fermion fields inside them. The projection onto $|\Omega\rangle$ ([[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-2|Theorem §C6a.5.2]]) uses only the spectrum of $\hat H$, and Theorem §C6b.1.1 holds for any $\hat H = \hat H_0 + \hat H_{\rm int}$: neither looks inside $\hat H_I$.
>
> **Step 4** (Lorentz invariance forces pairs). A Lorentz scalar built from spinor fields needs an even number of them: a single $\psi$ transforms in $(\frac12, 0)\oplus(0, \frac12)$, a product of an odd number in a representation of half-integer spin, which contains no invariant ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]). So every Lorentz-invariant $\mathcal H_{\rm int}$ is a sum of packages (PS p. 115; slide 6).
>
> **What the derivation shows.**
> - That fermions give nothing new is the statement that $T$ never splits a package: every question about the Dyson series, the $i\varepsilon$ limit or the in and out states is settled for scalars ([[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]]).
> - ⚑ By-product: fermion signs enter exactly when packages are opened by contractions → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]].

^der-c6d-1-2

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-2|Theorem §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.4 The Time-Evolution Operator Between Two Times#^thm-c6a-4-2|Theorem §C6a.4.2]], [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.5 The Interacting Vacuum and the Two-Point Function#^thm-c6a-5-2|Theorem §C6a.5.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]

## The vertex

> [!theorem] Theorem §C6d.1.3: The Yukawa Vertex
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], at first order in $g$,
>
> $$
> T\Bigl\{e^{-i\int dt\,\hat H_I(t)}\Bigr\} = \mathbb 1 - ig\int d^4x\;\hat{\bar\psi}_a\hat\psi_a\hat\phi(x) + O(g^2) ,
> $$
>
> and each vertex of a diagram, where one dashed and two solid lines meet, is
>
> $$
> -ig\,\delta_{ab} \qquad\bigl(\text{times } \textstyle\int d^4x \text{ in position space; } (2\pi)^4\delta^4(\sum q) \text{ in momentum space}\bigr) ,
> $$
>
> $a$ the spinor index of the $\hat{\bar\psi}$ leg and $b$ that of the $\hat\psi$ leg: the unit $4\times4$ matrix in spinor space, written $-ig$. The $g$ is the strength of $\hat H_I$, the $-i$ comes from $e^{-i\int\hat H_I}$; no factorial appears, since the three legs are of three different kinds (why $-ig$ and not $-ig/3!$: [[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]). At $n$-th order the term is $\frac{1}{n!}T\bigl\{(-ig\int d^4x\,\hat{\bar\psi}\hat\psi\hat\phi)^n\bigr\}$ (slide 16).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* the Dyson series between any states, every order; the vertex factor is exact, the scope of the amplitude is that of [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]].
>
> *Source: PHY 513 Lecture 17, slide 8 ("Time evolution operator at 1st order in perturbation theory: $Te^{-i\int H_Idt} \sim 1 - ig\int d^4x\,\bar\psi_I\psi_I\phi_I$. At each vertex: one boson and two fermions … Vertex $= -ig$"), slide 16 · the user's PHY 513 notes, Lecture 17 update, §17.2, Principle "The Yukawa vertex" (a principle there, a theorem here because it is derived) · PS §4.7, p. 118 (rule 2, "Vertices: $= -ig$") · Yu §7.1, eq. (7.28) ($-i\kappa\int d^4x$); §7.2, rule 9 (p. 288)*

^thm-c6d-1-3

> [!derivation]- Derivation
> **Step 1** (Dyson). By [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], valid with fermions by [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 3, $T\{e^{-i\int\hat H_I}\} = \sum_n\frac{(-i)^n}{n!}\int dt_1\cdots dt_n\,T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\}$.
>
> **Step 2** (first order). $n = 1$: $-i\int dt\,\hat H_I(t) = -i\int dt\int d^3x\,g\,\hat{\bar\psi}\hat\psi\hat\phi(t, \mathbf x) = -ig\int d^4x\,\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)$, with $d^4x = dt\,d^3x$. Order $n$: $\frac{(-i)^n}{n!}\,g^n\int d^4x_1\cdots d^4x_n\,T\{\cdots\} = \frac{1}{n!}T\{(-ig\int d^4x\,\hat{\bar\psi}\hat\psi\hat\phi)^n\}$.
>
> **Step 3** (the factor per vertex). Each factor $-ig\int d^4x\,\hat{\bar\psi}_a\hat\psi_b\,\delta_{ab}\,\hat\phi$ offers one leg of each kind, $\hat{\bar\psi}_a$, $\hat\psi_b$, $\hat\phi$. In the language of [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]] the vertex factor is $-i$ times the coefficient times $\prod_km_k!$, here $m_{\bar\psi} = m_\psi = m_\phi = 1$, so $\prod_km_k! = 1$: the factor is $-ig$, and the spinor indices of the two fermion legs are joined by $\delta_{ab}$. In momentum space the $\int d^4x$ of the three plane waves at the vertex becomes $(2\pi)^4\delta^4$ of the momenta flowing in ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]).
>
> **What the derivation shows.**
> - The vertex factor is $i\mathcal L_{\rm int}$ with the fields stripped: $i\cdot(-g) = -ig$ (Yu p. 288); in QED the same stripping gives $-ie\gamma^\mu$, a matrix in place of $\delta_{ab}$ ([[§C8.4 Feynman Rules for QED#^thm-c8-4-3|Theorem §C8.4.3]]; PS §4.8). → [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]]
> - The $\frac{1}{n!}$ is still there; it cancels against relabelling the vertices ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]).

^der-c6d-1-3

*Uses:* [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]

> [!theorem] Theorem §C6d.1.4: The Vertex Factor Is iℒ_int with the Fields Stripped
> Let $\mathcal L_{\rm int}$ contain no time derivatives, so that $\mathcal H_{\rm int} = -\mathcal L_{\rm int}$ ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], 2). Then the vertex factor of a term of $\mathcal L_{\rm int}$ is read off without any contraction:
>
> $$
> \text{vertex} = i\times\bigl(\mathcal L_{\rm int}\text{ with the fields stripped off}\bigr)\times\bigl(\text{number of permutations of identical fields}\bigr) .
> $$
>
> 1. Yukawa theory: $\mathcal L_{\rm int} = -g\,\bar\psi_a\psi_a\,\phi$; stripping $\bar\psi_a$, $\psi_b$, $\phi$ leaves $-g\,\delta_{ab}$, no two fields are identical, so the vertex is $i\cdot(-g)\,\delta_{ab} = -ig$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]); $\hat\phi$ gives the dashed leg, $\hat\psi$ the solid leg with the arrow into the vertex, $\hat{\bar\psi}$ the solid leg with the arrow out of it ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]).
> 2. A monomial $\mathcal L_{\rm int} = -g\prod_k\phi_k^{m_k}$ of scalar fields: $i\cdot(-g)\cdot\prod_km_k! = -ig\prod_km_k!$ ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]]); for $\phi^4$, $i\cdot(-\frac{\lambda}{4!})\cdot4! = -i\lambda$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], 2).
> 3. A matrix between the fermion fields stays as a matrix: $\mathcal L_{\rm int} = -e\,\bar\psi\gamma^\mu\psi A_\mu$ gives $-ie\gamma^\mu$ ([[§C8.4 Feynman Rules for QED#^thm-c8-4-3|Theorem §C8.4.3]]; PS §4.8).
>
> Only the vertex depends on $\mathcal L_{\rm int}$; the lines come from the free fields ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]]).
>
> *Proof:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]] (Steps 1–3) for item 1; [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]] for item 2. In both the $-i$ of $e^{-i\int\hat H_I}$ meets the $-$ of $\mathcal H_{\rm int} = -\mathcal L_{\rm int}$: $-i\int d^4x\,\mathcal H_{\rm int} = +i\int d^4x\,\mathcal L_{\rm int}$, and each field of the term is used up by exactly one line ending at the vertex.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], and any interaction without derivatives; *applies:* the vertex factor at every order, exact (the scope of the amplitudes built with it is that of [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]).
>
> *Source: Yu §7.2, p. 288 ("顶点规则与拉氏量中的相互作用项直接对应：将 Yukawa 相互作用项 $\mathcal L_{\rm Y} = -\kappa\phi\bar\psi\psi$ 中的场算符 $\phi$、$\psi$ 和 $\bar\psi$ 剥离，再乘以 i，就得到顶点规则的表达式 $-i\kappa$"); §7.3, p. 296 (the same for $\phi^4$, "multiply by the $4!$ permutations") · PHY 513 Lecture 17, slide 8 ("Vertex $= -ig$") · PS §4.8, p. 123 (the QED vertex) · from the first "What the derivation shows" bullet of [[§C6d.1 Yukawa Theory#^der-c6d-1-3|Derivation §C6d.1.3]]*

^thm-c6d-1-4

> [!definition] Definition §C6d.1.1: Fermion-Number Arrow
> Every solid (fermion) line of a diagram carries an **arrow**, the direction of fermion number ("charge"): it points from the $\hat{\bar\psi}$ end of the line to its $\hat\psi$ end. At a vertex the leg of $\hat\psi$ is the line arriving (arrow into the vertex), the leg of $\hat{\bar\psi}$ the line leaving (arrow out of the vertex). On an internal line from $\hat{\bar\psi}(y)$ to $\hat\psi(x)$ the arrow points from $y$ to $x$; on an external line it points into the diagram for an incoming particle and an outgoing antiparticle, out of it for an outgoing particle and an incoming antiparticle ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). The arrow is not the momentum: for a particle they agree, for an antiparticle they are opposite (slide 12).
>
> *Model:* any theory with a Dirac field and fermion-number conserving interactions; *applies:* bookkeeping on diagrams.
>
> *Source: PHY 513 Lecture 17, slide 12 ("propagator arrow = charge flow (momentum flow opposite)"), and transcript ("what I'm going to use as convention on this kind of lines is that it's the charge direction") · the user's PHY 513 notes, Lecture 17 update, §17.2, paragraph "The arrows" · PS §4.7, p. 119 ("It is conventional to draw arrows on fermion lines … to represent the direction of particle-number flow") · Yu §7.1, pp. 265–266 (费米子数 flow; "$\psi(x)$ corresponds to the line-end pointing into the vertex, $\bar\psi(x)$ to the one pointing away")*

^def-c6d-1-1

> [!theorem] Theorem §C6d.1.5: Fermion Number Is Conserved at Every Vertex
> With the charge $\hat Q$ of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]],
>
> $$
> [\hat Q, \hat{\bar\psi}_a(x)\hat\psi_a(x)\hat\phi(x)] = 0 ,
> $$
>
> so each vertex has **one arrow in and one arrow out** ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]). Hence one vertex describes, as time runs from left to right ("the four readings"):
> 1. $f \to f + \phi$ (and $f + \phi \to f$): a particle enters along the arrow and leaves along it;
> 2. $\bar f \to \bar f + \phi$: an antiparticle, its momentum against the arrow;
> 3. $\phi \to f + \bar f$: both arrows' ends outgoing, the antiparticle's momentum against its arrow;
> 4. $f + \bar f \to \phi$;
>
> and forbids, e.g., $f + f \to \phi$ (two arrows in). Whether a reading is a physical process is decided by kinematics ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* free fields, exact operator identity; with the matrix elements of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] it fixes which external states a vertex connects, at every order.
>
> *Source: PHY 513 Lecture 17, slide 8 ("Each of the three particles are created or annihilated"), slide 12 ("Charge conservation: each vertex has one arrow in, one out"), and transcript ("whatever charge goes into the vertex also comes out"; "you couldn't have this takes care of a particle, and this then took care of another particle. No, no, no. Remember, it must preserve charge") · the user's PHY 513 notes, Lecture 17 update, §17.2, paragraph "The arrows", Figure "yukvertex" · Yu §7.1, Fig. 7.1 (the eight readings with a scalar in or out) · proof written here*

^thm-c6d-1-5

> [!derivation]- Derivation
> **Step 1** (charges of the fields). By [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]], $[\hat Q, \hat\psi] = -\hat\psi$, $[\hat Q, \hat{\bar\psi}] = +\hat{\bar\psi}$, and $[\hat Q, \hat\phi] = 0$ ($\hat Q$ contains only fermion operators).
>
> **Step 2** (the product). With $[\hat Q, ABC] = [\hat Q, A]BC + A[\hat Q, B]C + AB[\hat Q, C]$ (commutators obey the product rule, no signs):
>
> $$
> [\hat Q, \hat{\bar\psi}_a\hat\psi_a\hat\phi] = (+1)\,\hat{\bar\psi}_a\hat\psi_a\hat\phi + (-1)\,\hat{\bar\psi}_a\hat\psi_a\hat\phi + 0 = 0 .
> $$
>
> **Step 3** (arrows). $\hat\psi$ lowers $\hat Q$ by one: it annihilates a particle or creates an antiparticle; $\hat{\bar\psi}$ raises it by one: it creates a particle or annihilates an antiparticle ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]). The $\hat\psi$ leg is the arrow into the vertex and the $\hat{\bar\psi}$ leg the arrow out ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]); exactly one of each.
>
> **Step 4** (the readings). Assign each fermion leg its two options from Step 3 and the scalar leg "in" or "out": $\hat\psi$ absorbs $f$ or emits $\bar f$, $\hat{\bar\psi}$ emits $f$ or absorbs $\bar f$. The four combinations are readings 1–4 (each with $\phi$ in or out, Yu's eight cases). $f + f \to \phi$ would need two legs absorbing a particle, i.e. two $\hat\psi$'s: there is one.
>
> **What the derivation shows.**
> - The arrow is redundant given the external spinor and the momentum direction, but it makes every vertex "one in, one out" and so organizes every fermion line into a chain ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]).

^der-c6d-1-5

*Uses:* [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]], [[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]

![[ph-qft-c6d-1-1.svg]]
*[[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]: one vertex, four readings (time runs to the right). Dashed: the scalar; solid with a black arrow: fermion number; orange arrows: momenta, against the fermion arrow for an antiparticle. (a) the vertex, $-ig$, one arrow in and one out; (b) $f \to f\phi$; (c) $\bar f \to \bar f\phi$; (d) $\phi \to f\bar f$; (e) $f\bar f \to \phi$. Added figure.*

> [!remark] Remark: Settle it for the scalars
> The logic comes before the rules: the amplitude is a matrix element of $T\{e^{-i\int\hat H_I}\}$ between free states, $\hat H_I$ plays the role of the potential of ordinary mechanics, and a field in $\hat H_I$ that meets an external particle produces its wave function. With fermions the wave function is $u^s(p)e^{-ip\cdot x}$; stripped of the plane wave in momentum space, the factor is just $u$ — the "$1$" of the scalar rules was always a wave function ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). Anything about where the rules come from (the $i\varepsilon$, the in and out states, which terms belong to $i\hat T$) is answered in [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]] and [[§C6c.2 Contractions with External Particles|§C6c.2]]–[[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]], by [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]].
>
> *Source: PHY 513 Lecture 17, slides 5–6, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.1*

^rem-c6d-1-1

## Renormalizability (Lecture 17, Part C)

Part C of the lecture (slides 26–28) explains why the theories of the course have the interactions they have. The counting of mass dimensions is [[§C1b.3 Mass Dimension, Locality and Power Counting|§C1b.3]] ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]: $[\phi] = 1$, $[\psi] = \frac32$; [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]]: $[g_{\mathcal O}] = 4 - [\mathcal O]$; [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|Example §C1b.3.2]]: $[g] = 0$); the lecture adds the name and the fermion case.

> [!definition] Definition §C6d.1.2: Renormalizable Interaction
> An interaction term $g_{\mathcal O}\,\mathcal O$ of a Lagrangian density in four dimensions is **renormalizable** if its coupling has zero or positive mass dimension,
>
> $$
> [g_{\mathcal O}] = 4 - [\mathcal O] \ge 0 ,
> $$
>
> and **nonrenormalizable** if $[g_{\mathcal O}] < 0$. In the words of [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]: renormalizable = relevant or marginal, nonrenormalizable = irrelevant. Examples: $\lambda\phi^4$ and $g\bar\psi\psi\phi$ ($[\lambda] = [g] = 0$); $f\phi^6$ and $h(\bar\psi\psi)^2$ ($[f] = [h] = -2$, $f, h \sim M^{-2}$).
>
> What the name means (cutoff independence of loop amplitudes) is renormalization theory, second semester (PS p. 80; slide 26: "a deep principle: much more in 2nd semester"); here it is the dimension criterion the slides state.
>
> *Model:* any local $\mathcal L$ in four dimensions; *applies:* classical dimension counting, as [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]].
>
> *Source: PHY 513 Lecture 17, slide 27 ("Renormalizable interactions: Coupling has zero or positive mass-dimension ($[g] \ge 0$)"), slide 28 ("$f\phi^6$ or $h\bar\psi\psi\bar\psi\psi$ ⇒ $f, h \sim M^{-2}$") · PS §4.1, pp. 79–80 ("any theory containing a coupling constant with negative mass dimension is not renormalizable")*

^def-c6d-1-2

> [!theorem] Theorem §C6d.1.6: The Renormalizable Interactions of a Scalar and a Dirac Fermion
> For one real scalar $\phi$ and one Dirac field $\psi$, the Lorentz-invariant, fermion-number-conserving, renormalizable ([[§C6d.1 Yukawa Theory#^def-c6d-1-2|Def. §C6d.1.2]]) interaction terms that contain the fermion are exactly
>
> $$
> g\,\bar\psi\psi\,\phi \qquad\text{and}\qquad g'\,\bar\psi i\gamma^5\psi\,\phi ,
> $$
>
> the scalar and the pseudoscalar Yukawa couplings ($g, g'$ real, dimensionless). Fermion self-interactions such as $(\bar\psi\psi)^2$ are nonrenormalizable.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] and its pseudoscalar variant; *applies:* classical dimension counting of local terms; terms with more fermion species or a Majorana field are not counted.
>
> *Source: PHY 513 Lecture 17, slide 27 ("Yukawa coupling only Lorentz invariant interaction between scalars and fermions that is renormalizable"; [[§C6d.1 Yukawa Theory#^cau-c6d-1-1|Caution: "Only" includes the pseudoscalar coupling]]) · PS §4.1, p. 80 ("the only allowable new interaction is the Yukawa term, $g\bar\psi\psi\phi$, although similar interactions can also be constructed out of Weyl and Majorana spinors") · the dimension count written here*

^thm-c6d-1-6

> [!derivation]- Derivation
> **Step 1** (dimensions). $[\psi] = [\bar\psi] = \frac32$, $[\phi] = 1$, $[\partial_\mu] = 1$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]). Renormalizable means $[\mathcal O] \le 4$ ([[§C6d.1 Yukawa Theory#^def-c6d-1-2|Def. §C6d.1.2]]).
>
> **Step 2** (fermions in pairs $\bar\psi\Gamma\psi$). Fermion number conservation ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]]) requires as many $\bar\psi$ as $\psi$, and Lorentz invariance an even number of spinor fields (Step 4 of [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]]). Two pairs have $[\mathcal O] \ge 6 > 4$: nonrenormalizable, e.g. $[(\bar\psi\psi)^2] = 6$, $[h] = -2$. So exactly one pair, $[\bar\psi\Gamma\psi] = 3$, leaving dimension $\le 1$ for the rest.
>
> **Step 3** (what may multiply the pair). Dimension $0$: nothing, $\bar\psi\Gamma\psi$ is quadratic (a mass term, $\Gamma = 1$ or $i\gamma^5$), not an interaction. Dimension $1$: one $\phi$, or one derivative $\partial_\mu$; a derivative alone gives $\bar\psi\gamma^\mu\partial_\mu\psi$-type terms, again quadratic (kinetic). So an interaction is $\bar\psi\Gamma\psi\,\phi$ with no free index on $\Gamma$.
>
> **Step 4** (Lorentz scalars among the bilinears). Of the sixteen bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-3|Def. §C5a.6.3]]) only $\mathsf S = \bar\psi\psi$ and $\mathsf P = \bar\psi i\gamma^5\psi$ carry no Lorentz index ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]); $\mathsf V^\mu$, $\mathsf A^\mu$, $\mathsf T^{\mu\nu}$ need a vector, and the only one available, $\partial_\mu\phi$, costs dimension $5$. Both $\mathsf S$ and $\mathsf P$ are real ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]), so $g$, $g'$ real make the terms Hermitian.
>
> **What the derivation shows.**
> - The list is short because $[\psi] = \frac32$: a fermion pair already uses $3$ of the $4$ units.
> - Parity distinguishes the two terms: $\mathsf S\phi$ for a scalar, $\mathsf P\phi$ for a pseudoscalar ([[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase|§C9.5]]).

^der-c6d-1-6

*Uses:* [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]], [[§C6d.1 Yukawa Theory#^def-c6d-1-2|Def. §C6d.1.2]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]], [[§C6d.1 Yukawa Theory#^der-c6d-1-2|Derivation §C6d.1.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-3|Def. §C5a.6.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]

> [!caution] Caution: "Only" includes the pseudoscalar coupling
> Slide 27 calls the Yukawa coupling "only Lorentz invariant interaction between scalars and fermions that is renormalizable", and PS p. 80 lists $g\bar\psi\psi\phi$ alone. The dimension count admits also $g'\bar\psi i\gamma^5\psi\phi$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-6|Theorem §C6d.1.6]]); both are called Yukawa couplings, and which one appears is decided by the parity of $\phi$ ([[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase|§C9.5]]). Fermion-number-violating terms of Majorana type are excluded by the U(1) of [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (PS: "similar interactions can also be constructed out of Weyl and Majorana spinors").
>
> *Source: PHY 513 Lecture 17, slide 27 · PS §4.1, p. 80 · written here*

^cau-c6d-1-1

> [!remark] Remark: Nonrenormalizable couplings fade at low energy
> A nonrenormalizable coupling has negative dimension, $f, h \sim M^{-2}$ for $f\phi^6$, $h(\bar\psi\psi)^2$. With external momenta $p \ll M$ the only way to make its contribution dimensionless relative to a marginal one is $hp^2 \sim (p/M)^2$, so "amplitudes where external particles have momentum $\sim p \ll M$ are suppressed by $\sim(p/M)^2$ (or more)" and "renormalizable couplings dominate processes at low energy" (slide 28). Hence "QFT interactions are heavily constrained. Unlike QM where the potential $V(x)$ is largely arbitrary." The same estimate is [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-3|§C1b.3, Remark: Why irrelevant terms die at low energy]]; Fermi's $G_F$ is the example there ([[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-5|§C1b.3, Remark: What the counting leaves out]]).
>
> *Source: PHY 513 Lecture 17, slide 28 · the transcript does not reach Part C; the slides are the source*

^rem-c6d-1-2

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the vertex integral $\int d^4x$ of three plane waves is the momentum delta of the vertex.

> [!remark]- Connections
> - The vertex $-ig$ with three distinct legs is the case $\prod_km_k! = 1$ of the polynomial vertex rule; what is new is the spinor index carried through the vertex by $\delta_{ab}$ — [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-2|Theorem §C6a.14.2]].
> - The arrow of a fermion line is the arrow of a complex scalar line: both mark the U(1) charge, and both make particle and antiparticle lines distinguishable — [[§C6a.8 Feynman Diagrams for Correlation Functions#^thm-c6a-8-2|Theorem §C6a.8.2]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]].
> - Exchanging the scalar between two fermions gives an attractive Yukawa potential, the force Yukawa built the theory for (nucleons and pions) — [[§C6d.7 The Yukawa Potential|§C6d.7]]; the same $e^{-m_\phi r}/r$ arises from a classical source — [[§C6a.0 Setups and Observables#^mod-c6a-0-2|★ Model §C6a.0.2]].
> - In the Standard Model the Yukawa couplings of the Higgs to quarks and leptons are most of its free parameters (PS p. 79); the pseudoscalar version describes pions coupled to nucleons — [[§C9.5 Intrinsic Parity, Pseudoscalars and the Parity Phase|§C9.5]].
> - Renormalizability is the dimension count of [[§C1b.3 Mass Dimension, Locality and Power Counting|§C1b.3]] given a name; its meaning, independence of the cutoff in loop integrals, is second-semester renormalization (PS §4.1, p. 80).
