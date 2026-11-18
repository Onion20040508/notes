---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.3 Massless Particles and Helicity|§C8b.3]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]] →

*Sources: PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 8, 9, 11 and 24, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1 (Definition "The chiral projectors"; paragraph "Asked in the lecture: is this chirality?"); Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PHY 513 Lecture 7, Part B, and Lecture 8 (the Weyl halves of the Dirac spinor) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.4, pp. 50–51, eqs. (3.68)–(3.72); §5.2, p. 141 · Yu Zhao-Huan, 量子场论讲义, §5.1, eq. (5.36); §8.3, eqs. (8.159)–(8.168), (8.174)–(8.189).*

Helicity labels a state ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]). What labels a component of a field, and when do the two labels say the same thing? The second label is chirality. Its home is [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], where $\gamma^5$, the projectors $P_L$, $P_R$ and the Weyl halves are built and proved as part of the Dirac representation; this section does not repeat those proofs. It quotes the definition, states in two boxes what kind of label chirality is (the label of an irreducible piece of the representation carried by the spinor index, the same in every frame), and then sets the two labels side by side, with the reading of Lecture 20's slides that the comparison gives. Where the two meet, for massless and for fast particles, is [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]] and [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]].

**The mathematical picture.** A particle and a field carry different kinds of representation ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]). The states of a particle carry a unitary representation of the Poincaré group, labelled by the mass and by a representation of the little group: spin for $m > 0$ ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-9|Theorem §C8b.2.9]]), helicity for $m = 0$ ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]). The index of a field carries a finite-dimensional representation of the Lorentz group, labelled by $(j_+, j_-)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]]). The Dirac index carries the reducible sum $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]), and chirality says in which of the two summands a component lies. Helicity is therefore a label on the side of states, chirality a label on the side of fields.

**Setup.** Representation facts, as in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]: Theorems §C8b.4.1 and §C8b.4.2 hold for any Dirac spinor (a classical field value, a c-number spinor $u$ or $v$, the spinor index of the quantum Dirac field), for every mass, with no equation of motion and no state involved. The comparison of the two remarks refers, on the helicity side, to one-particle states and spinors of the free Dirac field ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) as in [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]]; each of its entries is proved at the home linked in it.

*Conventions* ([[Larsen PHY 513]]): $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, equal to $\operatorname{diag}(-\mathbb 1, \mathbb 1)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]); Lorentz transformations of spinors are the matrices $\Lambda_{1/2}$ of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]. A subscript $L$ or $R$ on a field or on a projected spinor ($\psi_L$, $u_R$) is its chirality; on a particle ($e^-_R$) it is its physical helicity. The lecture uses the one pair of letters for both, which is the reason for this section.

## Chirality: the label of a field component

The definition, quoted from its home:

![[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1]]

> [!theorem] Theorem §C8b.4.1: Chirality Labels the Two Irreducible Halves of a Dirac Spinor
> With $\gamma^5$ and the projectors $P_L$, $P_R$ of [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]:
> 1. every Dirac spinor is, in exactly one way, a sum $\psi = \psi_L + \psi_R$ of a left-handed part $\psi_L \equiv P_L\psi$ (chirality $-1$) and a right-handed part $\psi_R \equiv P_R\psi$ (chirality $+1$); the two eigenspaces of $\gamma^5$ are two-dimensional;
> 2. the left-handed spinors carry the representation $(\frac12, 0)$ and the right-handed ones $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]): chirality is the label of the irreducible piece of $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]) in which a component lies;
> 3. in the chiral basis $\psi = (\psi_L, \psi_R)$: the upper two components are the left-handed Weyl spinor, the lower two the right-handed one.
>
> So chirality is defined for a field component: for the classical field, the c-number spinors and the spinor index of the quantum field alike, before any state, momentum or equation of motion is mentioned.
>
> *Model:* none (a representation fact); *applies:* any Dirac spinor, every mass.
>
> *Proof:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], with [[§C5a.5 Chirality and Weyl Spinors#^der-c5a-5-2|its derivation]] (the eigenspaces, their dimension, the representations they carry, the chiral form); the decomposition of part 1 is unique because $P_L + P_R = \mathbb 1$ and $P_LP_R = 0$, which follow from $(\gamma^5)^2 = \mathbb 1$ (PS (3.70)) by adding and by multiplying the two projectors.
>
> *Source: PS §3.4, p. 50 ("the Dirac representation must be reducible"), eq. (3.72) · Yu §8.3, eqs. (8.159)–(8.164) ($P_{L,R}$, $\psi_L \equiv P_L\psi$, $\psi_R \equiv P_R\psi$) · the user's PHY 513 notes, Lecture 20 update, §20.1 (Definition "The chiral projectors")*

^thm-c8b-4-1

> [!theorem] Theorem §C8b.4.2: Chirality Is Lorentz Invariant
> For every proper orthochronous Lorentz transformation, $P_L\Lambda_{1/2} = \Lambda_{1/2}P_L$ and $P_R\Lambda_{1/2} = \Lambda_{1/2}P_R$. Hence, if $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ is the transformed Dirac field ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]),
>
> $$
> (P_L\psi')(x) = \Lambda_{1/2}\,(P_L\psi)(\Lambda^{-1}x), \qquad (P_R\psi')(x) = \Lambda_{1/2}\,(P_R\psi)(\Lambda^{-1}x) :
> $$
>
> a left-handed component is left-handed for every observer related by a rotation or a boost, and likewise a right-handed one. The statement holds for every mass and involves no momentum.
>
> *Model:* none (a representation fact); *applies:* any Dirac spinor or Dirac field, classical or quantum; rotations and boosts only, not parity.
>
> *Proof:* $\gamma^5$ commutes with every $\Lambda_{1/2}$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]), and $P_{L,R} = \frac12(\mathbb 1 \mp \gamma^5)$ are polynomials in $\gamma^5$, so they commute with $\Lambda_{1/2}$ as well; applying $P_L$ to $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ and moving it through $\Lambda_{1/2}$ gives the displayed law.
>
> *Source: PS §3.4, p. 50 ($[\gamma^5, S^{\mu\nu}] = 0$) · Yu §5.1, eq. (5.36) ($\gamma^5$ is a Lorentz scalar matrix)*

^thm-c8b-4-2

> [!remark] Remark: What parity does
> Parity is not a proper orthochronous transformation, and Theorem §C8b.4.2 does not cover it. What it does to the two chiralities is [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-7|Theorem §C9.4.7]] (fields and currents), with [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-6|Theorem §C3.2.6]] for the representations; it is not restated here.

^rem-c8b-4-1

## Helicity versus chirality

> [!remark] Remark: Helicity versus chirality
> The two labels side by side:
>
> | | helicity | chirality |
> |---|---|---|
> | what it is | the eigenvalue $\pm\frac12$ of $h = \hat{\mathbf p}\cdot\mathbf S$, the spin along the motion: a property of a state of momentum $\mathbf p$ | the eigenvalue $\pm1$ of $\gamma^5$, selected by $P_{L,R}$: a label of a field component, independent of $\mathbf p$ |
> | Lorentz invariant? | only for $m = 0$; for $m > 0$ a frame that overtakes the particle reverses it ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-1\|§C8b.5, Remark: The helicity of a massive particle depends on the frame]]) | yes, under proper orthochronous transformations ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2\|Theorem §C5a.5.2]]) |
> | constant in free motion? | yes, for every mass: $h$ commutes with the free Dirac Hamiltonian | only for $m = 0$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3\|§C8b.6, Remark: Frame and mass]], item 3) |
> | antiparticles | the physical helicity is opposite to what the two-spinor in $v$ shows ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2\|Theorem §C8b.6.2]]) | $P_Rv$ has chirality $+1$ and describes a physically left-handed antiparticle at $m = 0$ |
>
> The two agree where the columns agree: for massless particles, and for fast ones up to corrections of relative size $m/E$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]; [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]).
>
> *Source: PHY 513 Lecture 20, slides 8, 9, 11, 24, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1, paragraph "Asked in the lecture: is this chirality?" · Yu §8.3, eqs. (8.174)–(8.189) · the table written for the user's question of 2026-11-18; moved here from §C8b.6, Remark: Chirality and helicity*

^rem-c8b-4-2

> [!remark] Remark: Reading the slides of Lecture 20 with the table
> Lecture 20 says "helicity" throughout and works at $m = 0$, where the two agree. Read with the table:
> 1. slide 8, "Helicity is conserved in QED": the identity is conservation of chirality at the vector vertex, exact for every mass ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]); it is a statement about helicity at $m = 0$;
> 2. slide 9, "Helicity depends on time (not conserved by the equation of motion) except for massless particles": true of chirality; helicity is constant in free motion for every mass;
> 3. slide 11, "Particle wave functions $u_{R,L}$ = physical helicity": the projections $u_{R,L}$ are chirality components, equal to helicity states at $m = 0$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]]);
> 4. slide 24, "helicity is not Lorentz-invariant except in the UR limit": true of helicity proper.
>
> *Source: PHY 513 Lecture 20, slides 8, 9, 11, 24 · the reading written for the user's question of 2026-11-18; moved here from §C8b.6, Remark: Chirality and helicity*

^rem-c8b-4-3

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> $\gamma^5$ commutes with the spinor representation, and its eigenspaces are the two half-spin representations (Theorems §C8b.4.1, §C8b.4.2):
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-4|Theorem §CB.19.4]] — the volume element commutes with the even part of the Clifford algebra, so its eigenspaces are invariant under the spin group; physics form: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]].
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-18-3|Def. §CB.18.3]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]] — the representations $(j_+, j_-)$ of the Lorentz algebra, and the Dirac module as $(\frac12, 0)\oplus(0, \frac12)$; physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]].

> [!remark]- Connections
> - Chirality and its calculus (the projectors, undotted and dotted indices, the bases) are developed in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]; the Weyl fields, each of one chirality, are [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]].
> - Helicity, the label on the side of states, is built in [[§C8b.2 Particle States and the Little Group|§C8b.2]]–[[§C8b.3 Massless Particles and Helicity|§C8b.3]]; that a field of given $(j_+, j_-)$ can create a particle only if its rotation content contains the particle's spin is [[§C8b.2 Particle States and the Little Group#^rem-c8b-2-5|§C8b.2, Remark: What a field must contain]].
> - The two labels are tied together by the plane-wave solutions: the helicity spinors and their massless limit — [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]; Lecture 20 then uses the chirality projectors as helicity projectors at $m = 0$ — [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[P9 Helicity Amplitudes|P9]].
> - The same double use of "left" and "right" occurs for the Weyl plane waves — [[§C5a.8 The Weyl Form and the Weyl Equations#^rem-c5a-8-1|§C5a.8, Remark: Why "left-handed"]].
