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

*Sources: PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 8, 9, 11 and 24, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1 (Definition "The chiral projectors"; paragraph "Asked in the lecture: is this chirality?"); Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PHY 513 Lecture 7, Part B, and Lecture 8 (the Weyl halves of the Dirac spinor) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.4, pp. 50–51, eqs. (3.68)–(3.72); §5.2, p. 141 · Yu Zhao-Huan, 量子场论讲义, §5.1, eq. (5.36); §8.3, eqs. (8.159)–(8.168), (8.174)–(8.189) · for the general part (2026-11-20): the user's PHY 513 notes, Ch. 7 §7.4.6 and §7.7; Srednicki, Quantum Field Theory, §34, eqs. (34.37)–(34.38); Weinberg, The Quantum Theory of Fields I, §5.9 (by section only).*

Helicity labels a state ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]). What labels a component of a field, and when do the two labels say the same thing? The second label is chirality. Its home is [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], where $\gamma^5$, the projectors $P_L$, $P_R$ and the Weyl halves are built and proved as part of the Dirac representation; this section does not repeat those proofs. It quotes the definition, states in two boxes what kind of label chirality is (the label of an irreducible piece of the representation carried by the spinor index, the same in every frame), and then sets the two labels side by side, with the reading of Lecture 20's slides that the comparison gives. The section is built general first. It opens with what chirality means for any field ([[§C8b.4 Chirality#^def-c8b-4-1|Def. §C8b.4.1]]), then treats the spinor, the case the course teaches. Two starred parts go beyond the course: the rule that ties the two labels together for every massless field ([[§C8b.4 Chirality#^thm-c8b-4-3|★ Theorem §C8b.4.3]]), and the vector field, whose potential has no chirality and whose field strength does ([[§C8b.4 Chirality#^thm-c8b-4-4|★ Theorem §C8b.4.4]]), with the Maxwell Lagrangian and field equations written in the two members ([[§C8b.4 Chirality#^thm-c8b-4-5|★ Theorem §C8b.4.5]]; both used in [[§C8b.9 Photon Helicity|§C8b.9]]). Where the two meet for spinors, for massless and for fast particles, is [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]] and [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]].

**The mathematical picture.** A particle and a field carry different kinds of representation ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]). The states of a particle carry a unitary representation of the Poincaré group, labelled by the mass and by a representation of the little group: spin for $m > 0$ ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-9|Theorem §C8b.2.9]]), helicity for $m = 0$ ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]). The index of a field carries a finite-dimensional representation of the Lorentz group, labelled by $(j_+, j_-)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]]). The Dirac index carries the reducible sum $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]), and chirality says in which of the two summands a component lies. Helicity is therefore a label on the side of states, chirality a label on the side of fields. The same question can be asked of any index: a vector index carries the single type $(\frac12, \frac12)$ and has no chirality, while the antisymmetric tensor $F^{\mu\nu}$ carries $(1, 0)\oplus(0, 1)$ and has one.

**Setup.** Representation facts, as in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]: Theorems §C8b.4.1 and §C8b.4.2 hold for any Dirac spinor (a classical field value, a c-number spinor $u$ or $v$, the spinor index of the quantum Dirac field), for every mass, with no equation of motion and no state involved. The comparison of the two remarks refers, on the helicity side, to one-particle states and spinors of the free Dirac field ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) as in [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]]; each of its entries is proved at the home linked in it. ★ Theorem §C8b.4.3 is about one-particle states of a massless particle and any covariant field, free or interacting; ★ Theorem §C8b.4.4 about any antisymmetric tensor field, with the free plane wave in its part 4; ★ Theorem §C8b.4.5 about the classical Maxwell field with an external current, and the Proca field in its part 5.

*Conventions* ([[Larsen PHY 513]]): $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, equal to $\operatorname{diag}(-\mathbb 1, \mathbb 1)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]); Lorentz transformations of spinors are the matrices $\Lambda_{1/2}$ of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]. A subscript $L$ or $R$ on a field or on a projected spinor ($\psi_L$, $u_R$) is its chirality; on a particle ($e^-_R$) it is its physical helicity. The lecture uses the one pair of letters for both, which is the reason for this section.

## Chirality in general: the type of a field

Chirality is not special to spinors. For any field, the question "which chirality" is the question "which representation $(j_+, j_-)$ does this component carry". The spinor is the case the course teaches. The vector field is the second case this chapter needs ([[§C8b.9 Photon Helicity|§C8b.9]]).

> [!definition] Definition §C8b.4.1: Type of a Field Component; Chiral Types and Mirror Pairs
> Let a component of a field carry the irreducible representation $(j_+, j_-)$ of the Lorentz group ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]]). The pair $(j_+, j_-)$ is its **type**.
> 1. The type is **chiral** if $j_+ \ne j_-$ and **non-chiral** if $j_+ = j_-$.
> 2. Parity exchanges $(j_+, j_-)$ and $(j_-, j_+)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-6|Theorem §C3.2.6]]). A chiral type and its image are two different types, a **mirror pair**. A non-chiral type is its own image.
> 3. For a field whose index carries a mirror pair, $(j_+, j_-)\oplus(j_-, j_+)$, the **chirality** of a component says in which of the two summands it lies.
>
> | field | its index carries | chiral? | the two members of the pair |
> |---|---|---|---|
> | scalar $\phi$ | $(0, 0)$ | no | none |
> | Dirac spinor $\psi$ | $(\frac12, 0)\oplus(0, \frac12)$ | a mirror pair | $\psi_L$ and $\psi_R$, the eigenvalues $-1$ and $+1$ of $\gamma^5$ ([[§C8b.4 Chirality#^thm-c8b-4-1\|Theorem §C8b.4.1]]) |
> | vector $A^\mu$ | $(\frac12, \frac12)$ | no | none ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9\|Theorem §C3.2.9]]) |
> | field strength $F^{\mu\nu}$ | $(1, 0)\oplus(0, 1)$ | a mirror pair | $\mathbf E - i\mathbf B$ and $\mathbf E + i\mathbf B$ ([[§C8b.4 Chirality#^thm-c8b-4-4\|★ Theorem §C8b.4.4]]) |
>
> Chirality is a label of field components. It needs no state, no momentum and no equation of motion, and it is the same in every frame, because rotations and boosts act within each summand.
>
> *Model:* none (a representation fact); *applies:* any field with a finite-dimensional index representation, every mass.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 (paragraph "Parity and conjugation exchange the two copies") · PS §3.2, eq. (3.37) (left- and right-handed Weyl spinors) · Srednicki, Quantum Field Theory, §34, eqs. (34.37)–(34.38) (the antisymmetric tensor; his $(3, 1)$ and $(1, 3)$ are $(1, 0)$ and $(0, 1)$) · the general wording and the table written for the user's question of 2026-11-20*

^def-c8b-4-1

## The spinor field: chirality as the eigenvalue of γ⁵

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

## The helicity a massless field carries

Helicity labels states and chirality labels fields. For a massless particle one rule ties the two together. "Helicity equals chirality" for spinors ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]) is its first case; the photon is its second.

> [!theorem] ★ Theorem §C8b.4.3: A Massless Field of Type (j₊, j₋) Carries Helicity j₋ − j₊
> Let $\hat\Phi_a$ be a covariant field ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]]) whose index carries $(j_+, j_-)$, and let $|k, \lambda\rangle$ be a state of a massless particle at the standard momentum $k = \kappa(1, 0, 0, 1)$ ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-1|Def. §C8b.3.1]]) without continuous spin ([[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4|Law §C8b.3.4]]). Suppose the field can annihilate the particle: $u_a \equiv \langle0|\hat\Phi_a(0)|k, \lambda\rangle \ne 0$. Then
> 1. the array $u$ is fixed up to a factor: it is the component with $J_{+3} = -j_+$ and $J_{-3} = +j_-$ (the lowest weight in the first slot, the highest in the second);
> 2. $\lambda = j_- - j_+$;
> 3. if the field can create a particle from the vacuum, $v_a \equiv \langle k, \lambda'|\hat\Phi_a(0)|0\rangle \ne 0$, then $\lambda' = j_+ - j_-$.
>
> | type | annihilates helicity | creates helicity | field |
> |---|---|---|---|
> | $(0, 0)$ | $0$ | $0$ | scalar |
> | $(\frac12, 0)$ | $-\frac12$ | $+\frac12$ | $\psi_L$: left-handed particle, right-handed antiparticle ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-4\|Theorem §C5a.8.4]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4\|Theorem §C8b.5.4]]) |
> | $(0, \frac12)$ | $+\frac12$ | $-\frac12$ | $\psi_R$ |
> | $(\frac12, \frac12)$ | $0$ | $0$ | a true four-vector field, for example the gradient $\partial^\mu\phi$ of a scalar |
> | $(1, 0)$ | $-1$ | $+1$ | $\mathbf E - i\mathbf B$ ([[§C8b.4 Chirality#^thm-c8b-4-4\|★ Theorem §C8b.4.4]]) |
> | $(0, 1)$ | $+1$ | $-1$ | $\mathbf E + i\mathbf B$ |
>
> For spinors the rule is "helicity equals chirality at $m = 0$". For the four-vector it says that a true four-vector field cannot annihilate a particle of helicity $\pm1$.
>
> *Model:* any relativistic quantum theory ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^mod-c3-4-4|Model §C3.4.4]]); *applies:* massless particles without continuous spin, free or interacting fields, an invariant vacuum $U(\Lambda)|0\rangle = |0\rangle$; with $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ and $K^i = \mathcal J^{0i}$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]], [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-2|Theorem §C8b.3.2]]). A source with the other sign of $\mathbf K$ exchanges the two labels and writes the rule as $j_+ - j_-$. For a massive particle there is no such restriction: all $2s + 1$ helicities occur.
>
> *Source: the statement is that of Weinberg, The Quantum Theory of Fields I, §5.9 (massless particle fields; in his labels $(A, B)$ the helicity is $B - A$), cited by section only: no copy is in the course folder and the text was not checked · derived here in the conventions of these notes from Theorem §C8b.3.2 and Law §C8b.3.4, and checked numerically for eleven types (`qft-C/tools/c8b-general/verify_general.py`)*

^thm-c8b-4-3

> [!derivation]- Derivation
> **Step 1** (the little group on the matrix element). Let $W$ be a Lorentz transformation with $Wk = k$. The covariance law at $x = 0$, with no translation, is $U(W)^{-1}\hat\Phi_a(0)U(W) = D(W)_a{}^b\hat\Phi_b(0)$ (Principle §C3.5.1; $W^{-1}\cdot0 = 0$). Insert $U(W)U(W)^{-1} = \mathbb 1$ and use $\langle0|U(W) = \langle0|$:
>
> $$
> \langle0|\hat\Phi_a(0)\,U(W)|k, \lambda\rangle = \langle0|U(W)\,\bigl[U(W)^{-1}\hat\Phi_a(0)U(W)\bigr]|k, \lambda\rangle = D(W)_a{}^b\,\langle0|\hat\Phi_b(0)|k, \lambda\rangle = \bigl(D(W)u\bigr)_a .
> $$
>
> **Step 2** (rotations about $\hat{\mathbf z}$). For $W = R_z(\theta)$ the state gets a phase, $U(R_z(\theta))|k, \lambda\rangle = e^{-i\theta\lambda}|k, \lambda\rangle$ (Theorem §C8b.3.2, part 1, with $\hat J^3 = \lambda$), so the left side of Step 1 is $e^{-i\theta\lambda}u_a$. On the index, $D(R_z(\theta)) = e^{-i\theta J_3}$. Hence $e^{-i\theta J_3}u = e^{-i\theta\lambda}u$ for every $\theta$; differentiating at $\theta = 0$, $J_3u = \lambda u$.
>
> **Step 3** (the translations of the little group). For $W = S(\alpha, \beta)$, $U(S) = e^{i(\alpha\hat A + \beta\hat B)}$ and $\hat A = \hat B = 0$ on the state (Law §C8b.3.4), so $U(S)|k, \lambda\rangle = |k, \lambda\rangle$ and the left side of Step 1 is $u_a$. On the index, $D(S) = e^{i(\alpha A + \beta B)}$ with the same combinations of the index generators, $A = J_2 - K_1$, $B = -J_1 - K_2$ (the index carries a representation of the same algebra, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]). Hence $e^{i(\alpha A + \beta B)}u = u$ for all $\alpha, \beta$; differentiating, $Au = 0$ and $Bu = 0$.
>
> **Step 4** ($A$ and $B$ in terms of $\mathbf J_\pm$). With $\mathbf J = \mathbf J_+ + \mathbf J_-$ and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ (Theorem §C3.2.2):
>
> $$
> A = J_2 - K_1 = (J_{+2} + J_{-2}) + i(J_{+1} - J_{-1}) = i\,(J_{+1} - iJ_{+2}) - i\,(J_{-1} + iJ_{-2}),
> $$
>
> $$
> B = -J_1 - K_2 = -(J_{+1} + J_{-1}) + i(J_{+2} - J_{-2}) = -(J_{+1} - iJ_{+2}) - (J_{-1} + iJ_{-2}) .
> $$
>
> (Check of the first: $i(J_{+1} - iJ_{+2}) = iJ_{+1} + J_{+2}$ and $-i(J_{-1} + iJ_{-2}) = -iJ_{-1} + J_{-2}$.) Name the lowering operator of the first slot $L \equiv J_{+1} - iJ_{+2}$ and the raising operator of the second $R \equiv J_{-1} + iJ_{-2}$. Then $A = i(L - R)$ and $B = -(L + R)$, so $Au = Bu = 0$ says $(L - R)u = 0$ and $(L + R)u = 0$. Adding and subtracting: $Lu = 0$ and $Ru = 0$.
>
> **Step 5** (only one component survives). In the spin-$j_+$ multiplet of the first slot the lowering operator annihilates only the lowest state, $m_+ = -j_+$, and in the spin-$j_-$ multiplet of the second slot the raising operator annihilates only the highest, $m_- = +j_-$ ([[§C3.1 Index Slots, Rotations and Spin in Field Theory#^thm-c3-1-1|Theorem §C3.1.1]]). So $u$ is a multiple of $|{-j_+}\rangle\otimes|{+j_-}\rangle$: part 1. On it $J_3 = J_{+3} + J_{-3} = -j_+ + j_-$, and by Step 2 this is $\lambda$: part 2.
>
> **Step 6** (creation). For $v_a = \langle k, \lambda'|\hat\Phi_a(0)|0\rangle$ insert the same identity on the other side and use $U(W)|0\rangle = |0\rangle$: $\langle k, \lambda'|U(W)^{-1}\hat\Phi_a(0)U(W)|0\rangle = (D(W)v)_a$, while the left side is $\bigl(U(W)|k, \lambda'\rangle\bigr)^\dagger\hat\Phi_a(0)|0\rangle$, which is $e^{+i\theta\lambda'}v_a$ for a rotation (the complex conjugate of the phase) and $v_a$ for a translation. So $J_3v = -\lambda'v$ and $Av = Bv = 0$. By Steps 4 and 5, $v$ is the same component and $-\lambda' = j_- - j_+$: part 3.
>
> **What the derivation shows**
> - Two inputs fix the helicity: the phase under rotations about the momentum, and the fact that the little-group translations do nothing to a physical massless state.
> - The surviving component has boost weight $m_+ - m_- = -(j_+ + j_-)$: under a boost of rapidity $\eta$ along the motion it grows by $e^{\eta(j_+ + j_-)}$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-11|Theorem §C3.2.11]]), the blue shift of the wave.
> - ⚑ By-product: for the four-vector the only invariant array is the momentum $k^\mu$ itself, of helicity $0$; the polarization vectors of helicity $\pm1$ are not invariant → [[§C8b.4 Chirality#^rem-c8b-4-4|★ Remark: Why photons of helicity ±1 do not contradict the rule]].

^der-c8b-4-3

*Uses:* [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]], [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-1|Def. §C8b.3.1]], [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-2|Theorem §C8b.3.2]], [[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4|Law §C8b.3.4]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]], [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^thm-c3-1-1|Theorem §C3.1.1]]

## The vector field: no chirality in the potential, a mirror pair in the field strength

> [!theorem] ★ Theorem §C8b.4.4: The Vector Potential Has No Chirality; the Field Strength Is a Mirror Pair
> 1. **The potential.** The index of $A^\mu$ carries the single non-chiral type $(\frac12, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9|Theorem §C3.2.9]]). No matrix other than a multiple of the identity commutes with all Lorentz transformations of a four-vector, so there is no analogue of $P_L$, $P_R$ for $A^\mu$.
> 2. **The field strength.** With $E^i = F^{i0}$ and $B^i = -\frac12\varepsilon_{ijk}F^{jk}$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^def-c1a-8-2|Def. §C1a.8.2]]), put $\mathbf G_\pm \equiv \mathbf E \pm i\mathbf B$. Under an infinitesimal rotation by $\theta$ about $\hat{\mathbf z}$ combined with a boost of rapidity $\eta$ along $\hat{\mathbf z}$, $\delta\mathbf G_\pm = (\theta \pm i\eta)\,\hat{\mathbf z}\times\mathbf G_\pm$: a boost acts on $\mathbf G_\pm$ as a rotation through the imaginary angle $\pm i\eta$, and the two never mix. $\mathbf G_+ = \mathbf E + i\mathbf B$ has type $(0, 1)$ and $\mathbf G_- = \mathbf E - i\mathbf B$ has type $(1, 0)$. The homes of this statement are [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-8|Theorem §C3.3.8]] (with [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]]) and [[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-4|Theorem §C1a.8.4]]; the derivation below is a second route, through the infinitesimal boost.
> 3. **Parity and conjugation.** Parity ($\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$) sends $\mathbf G_\pm \to -\mathbf G_\mp$, and for real fields $\mathbf G_\pm^{\ast} = \mathbf G_\mp$: both exchange the two members, as [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-6|Theorem §C3.2.6]] says they must.
> 4. **Helicity.** For the plane wave $A^\mu = \varepsilon^\mu(k, \lambda)\,e^{-ik\cdot x}$ of a photon of helicity $\lambda$ along $\hat{\mathbf z}$, with $\varepsilon(k, \pm) = (0, 1, \pm i, 0)/\sqrt2$: $\mathbf B = \mp i\mathbf E$, so $\mathbf G_- = 0$ for $\lambda = +1$ and $\mathbf G_+ = 0$ for $\lambda = -1$. The helicity $+1$ wave lies in $(0, 1)$ and the helicity $-1$ wave in $(1, 0)$, as [[§C8b.4 Chirality#^thm-c8b-4-3|★ Theorem §C8b.4.3]] requires.
> 5. **Duality.** With $\tilde F^{\mu\nu} \equiv \frac12\varepsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ ($\varepsilon^{0123} = +1$), the dual has $\mathbf E \to \mathbf B$, $\mathbf B \to -\mathbf E$, so $\tilde F = -iF$ on the $\mathbf G_+$ part and $\tilde F = +iF$ on the $\mathbf G_-$ part. These are the anti-self-dual and self-dual parts of $F$; which is called which depends on the sign conventions of the source ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]], 1; [[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-4|Theorem §C1a.8.4]], 1).
>
> *Model:* none for parts 1–3 and 5 (representation facts); part 4 is the free plane wave of [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]]; *applies:* any antisymmetric tensor field, classical or quantum; for the Hermitian quantum field, $\hat{\mathbf G}_\pm^\dagger = \hat{\mathbf G}_\mp$.
>
> *Source: Srednicki, Quantum Field Theory, §34, eqs. (34.37)–(34.38) (a field of type $(1, 0)$ is a self-dual antisymmetric tensor, in his conventions) · the user's PHY 513 notes, Ch. 7 §7.4 (the types $(j_+, j_-)$) · the computation with $\mathbf E \pm i\mathbf B$ in the conventions of these notes written for the user's question of 2026-11-20 and checked numerically (`qft-C/tools/c8b-general/verify_general.py`)*

^thm-c8b-4-4

> [!derivation]- Derivation
> **Step 1** (the potential). The vector representation is irreducible, equivalent to $(\frac12, \frac12)$ (Theorem §C3.2.9). By Schur's lemma ([[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|Theorem §CB.7.4]]) a matrix that commutes with an irreducible representation is a multiple of the identity. A projector onto a proper invariant part would be such a matrix and is not a multiple of the identity. Part 1.
>
> **Step 2** (an infinitesimal boost of $F$). The boost along $\hat{\mathbf z}$ is $\Lambda = \mathbb 1 - i\eta\,\mathcal K^3$ with $\mathcal K^3 = \mathcal J^{03}$ and $(\mathcal J^{03})^\mu{}_\nu = i(g^{0\mu}\delta^3{}_\nu - g^{3\mu}\delta^0{}_\nu)$ ([[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-1|Def. §C1a.7.1]]). Its nonzero entries are $(\mathcal J^{03})^0{}_3 = i$ and $(\mathcal J^{03})^3{}_0 = -ig^{33} = i$, so $-i\eta\mathcal K^3$ is $\eta\,b$ with $b^0{}_3 = b^3{}_0 = 1$: $\delta x^0 = \eta x^3$, $\delta x^3 = \eta x^0$. A tensor with two upper indices changes by $\delta F^{\mu\nu} = \eta\,(b^\mu{}_\alpha F^{\alpha\nu} + b^\nu{}_\beta F^{\mu\beta})$. Component by component, with $F^{i0} = E^i$, $F^{12} = -B^3$, $F^{23} = -B^1$, $F^{31} = -B^2$:
>
> $$
> \delta F^{10} = \eta F^{13} = \eta B^2, \qquad \delta F^{20} = \eta F^{23} = -\eta B^1, \qquad \delta F^{30} = \eta\,(F^{00} + F^{33}) = 0,
> $$
>
> $$
> \delta F^{23} = \eta F^{20} = \eta E^2, \qquad \delta F^{31} = \eta F^{01} = -\eta E^1, \qquad \delta F^{12} = 0 .
> $$
>
> So $\delta\mathbf E = \eta\,(B^2, -B^1, 0)$ and, from $B^1 = -F^{23}$, $B^2 = -F^{31}$, $\delta\mathbf B = \eta\,(-E^2, E^1, 0)$. With $\hat{\mathbf z}\times\mathbf V = (-V^2, V^1, 0)$ these are
>
> $$
> \delta\mathbf E = -\eta\,\hat{\mathbf z}\times\mathbf B, \qquad \delta\mathbf B = +\eta\,\hat{\mathbf z}\times\mathbf E .
> $$
>
> **Step 3** (the combinations). $\delta\mathbf G_\pm = \delta\mathbf E \pm i\,\delta\mathbf B = -\eta\,\hat{\mathbf z}\times\mathbf B \pm i\eta\,\hat{\mathbf z}\times\mathbf E$. Compare with $\pm i\eta\,\hat{\mathbf z}\times(\mathbf E \pm i\mathbf B) = \pm i\eta\,\hat{\mathbf z}\times\mathbf E + (\pm i)(\pm i)\,\eta\,\hat{\mathbf z}\times\mathbf B = \pm i\eta\,\hat{\mathbf z}\times\mathbf E - \eta\,\hat{\mathbf z}\times\mathbf B$: the same. So $\delta\mathbf G_\pm = \pm i\eta\,\hat{\mathbf z}\times\mathbf G_\pm$ under the boost. Under a rotation by $\theta$ about $\hat{\mathbf z}$ every vector changes by $\theta\,\hat{\mathbf z}\times\mathbf V$, and $\mathbf E$, $\mathbf B$ are vectors under rotations. Adding the two gives the formula of part 2.
>
> **Step 4** (the types). On three-vectors the rotation is $-i\theta J_3\mathbf V = \theta\,\hat{\mathbf z}\times\mathbf V$, with $J_3$ a spin-1 matrix. The boost is $-i\eta K_3\mathbf G_\pm = \pm i\eta\,\hat{\mathbf z}\times\mathbf G_\pm = \pm i\eta\,(-iJ_3)\mathbf G_\pm = \pm\eta J_3\mathbf G_\pm$, so $K_3 = \pm iJ_3$ on $\mathbf G_\pm$; the other axes follow by rotating the axis. In [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]], $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$: the type $(1, 0)$ has $\mathbf K = -i\mathbf J$ and the type $(0, 1)$ has $\mathbf K = +i\mathbf J$. Hence $\mathbf G_+$ is $(0, 1)$ and $\mathbf G_-$ is $(1, 0)$. Part 2.
>
> **Step 5** (parity, conjugation). $\mathbf G_\pm = \mathbf E \pm i\mathbf B \to -\mathbf E \pm i\mathbf B = -(\mathbf E \mp i\mathbf B) = -\mathbf G_\mp$. For real $\mathbf E$, $\mathbf B$: $(\mathbf E \pm i\mathbf B)^{\ast} = \mathbf E \mp i\mathbf B$. Part 3.
>
> **Step 6** (the plane wave). $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ and $\partial^\mu e^{-ik\cdot x} = -ik^\mu e^{-ik\cdot x}$ give $F^{\mu\nu} = -i(k^\mu\varepsilon^\nu - k^\nu\varepsilon^\mu)\,e^{-ik\cdot x}$. With $\varepsilon^0 = 0$, $k^0 = \kappa$: $E^i = F^{i0} = -i(k^i\varepsilon^0 - k^0\varepsilon^i) = i\kappa\,\varepsilon^i$. And $B^i = -\frac12\varepsilon_{ijk}F^{jk} = \frac i2\varepsilon_{ijk}(k^j\varepsilon^k - k^k\varepsilon^j) = i\,(\mathbf k\times\boldsymbol\varepsilon)^i$ (the plane-wave factor is left out). For $\mathbf k = \kappa\hat{\mathbf z}$ and $\boldsymbol\varepsilon = (1, \pm i, 0)/\sqrt2$: $\hat{\mathbf z}\times(1, \pm i, 0) = (\mp i, 1, 0) = \mp i\,(1, \pm i, 0)$, so $\mathbf k\times\boldsymbol\varepsilon = \mp i\kappa\,\boldsymbol\varepsilon$ and $\mathbf B = i(\mp i\kappa)\boldsymbol\varepsilon = \pm\kappa\,\boldsymbol\varepsilon = \mp i\,\mathbf E$. For $\lambda = +1$: $\mathbf G_- = \mathbf E - i(-i\mathbf E) = 0$ and $\mathbf G_+ = 2\mathbf E$. For $\lambda = -1$: $\mathbf G_+ = \mathbf E + i(i\mathbf E) = 0$. Part 4.
>
> **Step 7** (the dual). $\tilde F^{0i} = \frac12\varepsilon^{0ijk}F_{jk} = \frac12\varepsilon_{ijk}(-\varepsilon_{jkl}B^l) = -B^i$, using $F_{jk} = -\varepsilon_{jkl}B^l$ and $\varepsilon_{ijk}\varepsilon_{jkl} = 2\delta_{il}$. Since $F^{0i} = -E^i$, the dual has $\mathbf B$ in the place of $\mathbf E$; the second rule, $\mathbf B \to -\mathbf E$, was checked numerically. Then $\mathbf G_+ \to \mathbf B - i\mathbf E = -i\,\mathbf G_+$ and $\mathbf G_- \to \mathbf B + i\mathbf E = +i\,\mathbf G_-$. Part 5.
>
> **What the derivation shows**
> - $\mathbf E$ and $\mathbf B$ mix under boosts, but the complex combinations $\mathbf E \pm i\mathbf B$ do not mix with each other. They are to $F^{\mu\nu}$ what $\psi_L$, $\psi_R$ are to the Dirac spinor.
> - In the plane wave $F$ the momentum $k$ enters antisymmetrically with $\varepsilon$, so a shift $\varepsilon \to \varepsilon + c\,k$ drops out: $F$ is a true tensor although $\varepsilon$ is not a true vector.

^der-c8b-4-4

*Uses:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9|Theorem §C3.2.9]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]], [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-1|Def. §C1a.7.1]], [[§C1a.8 Relativistic Electrodynamics in Index Form#^def-c1a-8-2|Def. §C1a.8.2]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|Theorem §CB.7.4]]

## The Lagrangian in the two members

Theorem §C8b.4.4 is about the index of the field alone. The dynamics is in the Lagrangian, and for the spinor the Lagrangian is where the two chiralities are seen to separate: the kinetic term acts within each Weyl block ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]). The same analysis for the vector field:

> [!theorem] ★ Theorem §C8b.4.5: The Maxwell Lagrangian and Field Equations in E ± iB
> For the Maxwell field with a current $J^\mu = (\rho, \mathbf J)$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^mod-c1a-8-1|Model §C1a.8.1]]) and $\mathbf G_\pm = \mathbf E \pm i\mathbf B$ ([[§C8b.4 Chirality#^thm-c8b-4-4|★ Theorem §C8b.4.4]]):
> 1. **The Lagrangian separates.** $-\frac14F_{\mu\nu}F^{\mu\nu} = \frac12(\mathbf E^2 - \mathbf B^2) = \frac14\bigl(\mathbf G_+\cdot\mathbf G_+ + \mathbf G_-\cdot\mathbf G_-\bigr)$: one term for each member and no product of $\mathbf G_+$ with $\mathbf G_-$.
> 2. **Each member has its own field equation.** Maxwell's equations ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-2|Theorem §C1a.8.2]]) are equivalent to $\nabla\cdot\mathbf G_\pm = \rho$ and $i\,\partial_t\mathbf G_\pm = \pm\nabla\times\mathbf G_\pm - i\mathbf J$. The current enters both in the same way.
> 3. **Without a current these are Weyl equations for spin one.** With the spin-one matrices $(S_j)_{kl} = -i\varepsilon_{jkl}$ and $\hat{\mathbf p} = -i\nabla$, $\nabla\times\mathbf G = (\mathbf S\cdot\hat{\mathbf p})\,\mathbf G$, so $i\,\partial_t\mathbf G_\pm = \pm(\mathbf S\cdot\hat{\mathbf p})\,\mathbf G_\pm$. For a wave of positive frequency, $\mathbf G_\pm \propto e^{-i(\omega t - \mathbf k\cdot\mathbf x)}$ with $\omega = |\mathbf k|$, this reads $(\mathbf S\cdot\mathbf k/|\mathbf k|)\,\mathbf G_\pm = \pm\mathbf G_\pm$: $\mathbf G_+$ carries helicity $+1$ and $\mathbf G_-$ helicity $-1$. The spinor twin is $i\,\partial_t\psi_{R,L} = \pm(\boldsymbol\sigma\cdot\hat{\mathbf p})\,\psi_{R,L}$ at $m = 0$ ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-4|Theorem §C5a.8.4]]).
> 4. **The two members are not independent fields.** For a real potential $\mathbf G_- = \mathbf G_+^{\ast}$ (for the quantum field $\hat{\mathbf G}_- = \hat{\mathbf G}_+^\dagger$): one potential contains both helicities. The energy density and the momentum density contain both members together, $\frac12(\mathbf E^2 + \mathbf B^2) = \frac12\,\mathbf G_+\cdot\mathbf G_-$ and $\mathbf E\times\mathbf B = \frac1{2i}\,\mathbf G_-\times\mathbf G_+$ ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]]).
> 5. **A mass.** The Proca Lagrangian adds $\frac12m^2A_\mu A^\mu$ ([[§C4.2★ The Proca Field#^mod-c4-2-1|Model §C4.2.1]]), a term written with the potential and not with $\mathbf G_\pm$. The equations become $\nabla\cdot\mathbf G_\pm = \rho - m^2A^0$ and $i\,\partial_t\mathbf G_\pm = \pm\nabla\times\mathbf G_\pm - i(\mathbf J - m^2\mathbf A)$: both members are tied to the one potential $A^\mu$, of type $(\frac12, \frac12)$, and with it the third state, helicity $0$, appears ([[§C8b.9 Photon Helicity#^thm-c8b-9-2|★ Theorem §C8b.9.2]]).
>
> *Model:* [[§C1a.8 Relativistic Electrodynamics in Index Form#^mod-c1a-8-1|Model §C1a.8.1]] (classical Maxwell field with an external current; parts 3 and 4 with $J = 0$ where stated), and [[§C4.2★ The Proca Field#^mod-c4-2-1|Model §C4.2.1]] with a current added for part 5; *applies:* Heaviside–Lorentz units, $c = 1$; identities of the classical fields, which hold for the free quantum field operator by operator.
>
> *Source: the Maxwell equations in the variables $\mathbf E \pm i\mathbf B$ are standard (the Riemann–Silberstein vector); no typed source in the course folder states them, so they are derived here from Theorem §C1a.8.2 and checked symbolically (`qft-C/tools/c8b-general/verify_lagr.py`) · the user's PHY 513 notes, Ch. 1 §1.5 ("Irreducible pieces of a two-tensor") · written for the user's question of 2026-11-20*

^thm-c8b-4-5

> [!derivation]- Derivation
> **Step 1** (the Lagrangian). $\mathbf G_\pm\cdot\mathbf G_\pm = (\mathbf E \pm i\mathbf B)\cdot(\mathbf E \pm i\mathbf B) = \mathbf E^2 - \mathbf B^2 \pm 2i\,\mathbf E\cdot\mathbf B$. Adding the two signs, the $\mathbf E\cdot\mathbf B$ terms cancel: $\mathbf G_+\cdot\mathbf G_+ + \mathbf G_-\cdot\mathbf G_- = 2(\mathbf E^2 - \mathbf B^2)$. With $-\frac14F_{\mu\nu}F^{\mu\nu} = \frac12(\mathbf E^2 - \mathbf B^2)$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]], 2) this is part 1. (Subtracting instead gives the pseudoscalar: $\mathbf E\cdot\mathbf B = \frac1{4i}(\mathbf G_+\cdot\mathbf G_+ - \mathbf G_-\cdot\mathbf G_-)$.)
>
> **Step 2** (the field equations). In three-vector form Maxwell's equations are $\nabla\cdot\mathbf E = \rho$, $\nabla\times\mathbf B - \partial_t\mathbf E = \mathbf J$, $\nabla\cdot\mathbf B = 0$, $\nabla\times\mathbf E + \partial_t\mathbf B = 0$ (Theorem §C1a.8.2). The divergences: $\nabla\cdot\mathbf G_\pm = \nabla\cdot\mathbf E \pm i\,\nabla\cdot\mathbf B = \rho$. The time derivatives: $\partial_t\mathbf E = \nabla\times\mathbf B - \mathbf J$ and $\partial_t\mathbf B = -\nabla\times\mathbf E$, so
>
> $$
> \partial_t\mathbf G_\pm = \nabla\times\mathbf B - \mathbf J \mp i\,\nabla\times\mathbf E = \mp i\,\nabla\times(\mathbf E \pm i\mathbf B) - \mathbf J ,
> $$
>
> where $\mp i\,\nabla\times(\mathbf E \pm i\mathbf B) = \mp i\,\nabla\times\mathbf E + (\mp i)(\pm i)\,\nabla\times\mathbf B = \mp i\,\nabla\times\mathbf E + \nabla\times\mathbf B$. Multiplying by $i$: $i\,\partial_t\mathbf G_\pm = \pm\nabla\times\mathbf G_\pm - i\mathbf J$. Conversely the real and imaginary parts of these two complex equations are the four Maxwell equations. Part 2.
>
> **Step 3** (the curl as a spin matrix). $\bigl((\mathbf S\cdot\hat{\mathbf p})\mathbf G\bigr)_k = (S_j)_{kl}\,(-i\partial_j)\,G_l = (-i\varepsilon_{jkl})(-i\partial_j)G_l = -\varepsilon_{jkl}\partial_jG_l = \varepsilon_{kjl}\partial_jG_l = (\nabla\times\mathbf G)_k$, moving $k$ to the first slot of $\varepsilon$ with one transposition. So without a current $i\,\partial_t\mathbf G_\pm = \pm(\mathbf S\cdot\hat{\mathbf p})\mathbf G_\pm$. On $e^{-i(\omega t - \mathbf k\cdot\mathbf x)}$: $i\partial_t \to \omega$ and $\hat{\mathbf p} \to \mathbf k$, so $\omega\,\mathbf G_\pm = \pm(\mathbf S\cdot\mathbf k)\mathbf G_\pm$; with $\omega = |\mathbf k| > 0$ divide by $|\mathbf k|$. Part 3. (For the spinor: Theorem §C5a.8.2 at $m = 0$ is $i(\partial_0 \mp \boldsymbol\sigma\cdot\nabla)\psi_{L,R} = 0$, i.e. $i\partial_t\psi_{R,L} = \pm\boldsymbol\sigma\cdot(-i\nabla)\psi_{R,L}$.)
>
> **Step 4** (reality, energy, momentum). $\mathbf E$ and $\mathbf B$ are real, so $(\mathbf E + i\mathbf B)^{\ast} = \mathbf E - i\mathbf B$. $\mathbf G_+\cdot\mathbf G_- = (\mathbf E + i\mathbf B)\cdot(\mathbf E - i\mathbf B) = \mathbf E^2 + \mathbf B^2$. $\mathbf G_-\times\mathbf G_+ = (\mathbf E - i\mathbf B)\times(\mathbf E + i\mathbf B) = i\,\mathbf E\times\mathbf B - i\,\mathbf B\times\mathbf E = 2i\,\mathbf E\times\mathbf B$. Part 4.
>
> **Step 5** (the mass term). The Proca equation is $\partial_\mu F^{\mu\nu} + m^2A^\nu = 0$ ([[§C4.2★ The Proca Field#^thm-c4-2-3|Theorem §C4.2.3]]); with a current, $\partial_\mu F^{\mu\nu} = J^\nu - m^2A^\nu$. This is Maxwell's inhomogeneous equation with $J^\nu$ replaced by $J^\nu - m^2A^\nu$, and the homogeneous equations are unchanged, so Step 2 applies with $\rho \to \rho - m^2A^0$ and $\mathbf J \to \mathbf J - m^2\mathbf A$. Part 5.
>
> **What the derivation shows**
> - The free Maxwell Lagrangian does not couple the two members, and each obeys a first-order equation that fixes its helicity: the same structure as the massless Dirac Lagrangian in Weyl components.
> - A current couples to both members equally, as the vector coupling of QED couples to both chiralities equally ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]).
> - ⚑ By-product: the difference from the spinor is part 4. $\psi_L$ and $\psi_R$ are independent fields at $m = 0$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-6|Theorem §C8b.6.6]]), and a theory may keep only one of them ([[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]]). $\mathbf G_+$ and $\mathbf G_-$ are complex conjugates of each other, so a real potential always describes both helicities: the photon is its own antiparticle, and the field that annihilates helicity $+1$ creates helicity $-1$ ([[§C8b.4 Chirality#^thm-c8b-4-3|★ Theorem §C8b.4.3]]).
> - The mass acts differently in the two cases. For the spinor see [[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-2|§C8b.5, Remark: The mass is what connects the two chiral blocks]] and [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]]: $-m\bar\psi\psi = -m(\overline{\psi_R}\psi_L + \overline{\psi_L}\psi_R)$, the term of the Dirac Lagrangian that joins the two members. For the vector the mass term cannot be written with $\mathbf G_\pm$ at all: it needs the potential.

^der-c8b-4-5

*Uses:* [[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-2|Theorem §C1a.8.2]], [[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]], [[§C8b.4 Chirality#^thm-c8b-4-4|★ Theorem §C8b.4.4]], [[§C4.2★ The Proca Field#^thm-c4-2-3|Theorem §C4.2.3]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]

> [!remark] ★ Remark: The duality rotation is the vector twin of the chiral rotation
> Multiplying the two members by opposite phases, $\mathbf G_\pm \to e^{\mp i\alpha}\mathbf G_\pm$, is the rotation $\mathbf E \to \mathbf E\cos\alpha + \mathbf B\sin\alpha$, $\mathbf B \to -\mathbf E\sin\alpha + \mathbf B\cos\alpha$. It leaves the equations of [[§C8b.4 Chirality#^thm-c8b-4-5|★ Theorem §C8b.4.5]], part 2, unchanged when there is no current, and it leaves the energy density $\frac12\mathbf G_+\cdot\mathbf G_-$ unchanged ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-4|Theorem §C1a.8.4]], last item of its derivation). The Lagrangian of part 1 is not unchanged: it becomes $\frac12(\mathbf E^2 - \mathbf B^2)\cos2\alpha + \mathbf E\cdot\mathbf B\,\sin2\alpha$. A current or a mass spoils the rotation, because $\rho$, $\mathbf J$ and $A^\mu$ are real and do not rotate with it. For the spinor the corresponding rotation gives the two chiralities opposite phases; it is a symmetry of the massless Dirac Lagrangian, and its current is the axial current, which the mass stops being conserved ([[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-4|Theorem §C5a.9.4]]).
>
> *Source: Theorem §C1a.8.4 (duality rotations) · the rotated Lagrangian computed here and checked symbolically (`qft-C/tools/c8b-general/verify_lagr.py`)*

^rem-c8b-4-5

> [!remark] ★ Remark: Why photons of helicity ±1 do not contradict the rule
> [[§C8b.4 Chirality#^thm-c8b-4-3|★ Theorem §C8b.4.3]] allows a true four-vector field only helicity $0$, and photons have helicity $\pm1$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-5|Theorem §C8b.9.5]]). Both statements hold, because the potential of a massless spin-one particle is not a true four-vector field. Under a Lorentz transformation its polarization vector comes back with a multiple of the momentum added ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]], part 3): the field transforms as a vector only up to a gauge transformation. In the derivation above this is Step 3 failing: the little-group translations do not leave $\varepsilon(k, \pm)$ alone, they add a multiple of $k$. The object that is a true tensor is $F^{\mu\nu}$, in which the added multiple of $k$ cancels, and its types $(1, 0)\oplus(0, 1)$ are the ones the rule requires for helicity $\mp1$. Gauge invariance is the price of describing helicity $\pm1$ with a vector potential ([[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^rem-c4-6-3|§C4.6, Remark: Why a massless vector field must be a gauge field]]; on states, the null states of [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]]).
>
> *Source: the reading is that of the user's pre-course notes, §2.3 ("the origin of gauge invariance for the photon") and of Weinberg, The Quantum Theory of Fields I, §5.9 (cited by section only, not checked against the text)*

^rem-c8b-4-4

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
> | at a vertex | at high energy the vector vertex of QED keeps it ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4\|Theorem §C8b.6.4]]) and a scalar vertex flips it ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10\|Theorem §C8b.6.10]]) | a bilinear with an odd number of $\gamma$'s between $\bar\psi$ and $\psi$ joins equal chiralities, one with an even number opposite ones ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7\|Theorem §C8b.6.7]]); the mass term joins $\psi_L$ and $\psi_R$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8\|Theorem §C8b.6.8]]) |
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
> - [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-4|Theorem §CB.7.4]] — Schur's lemma: nothing but multiples of the identity commutes with an irreducible representation, so the vector index has no chirality projector (★ Theorem §C8b.4.4).
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-18-3|Def. §CB.18.3]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]] — the representations $(j_+, j_-)$ of the Lorentz algebra, and the Dirac module as $(\frac12, 0)\oplus(0, \frac12)$; physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]].

> [!remark]- Connections
> - Chirality and its calculus (the projectors, undotted and dotted indices, the bases) are developed in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]; the Weyl fields, each of one chirality, are [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]].
> - Helicity, the label on the side of states, is built in [[§C8b.2 Particle States and the Little Group|§C8b.2]]–[[§C8b.3 Massless Particles and Helicity|§C8b.3]]; that a field of given $(j_+, j_-)$ can create a particle only if its rotation content contains the particle's spin is [[§C8b.2 Particle States and the Little Group#^rem-c8b-2-5|§C8b.2, Remark: What a field must contain]].
> - The two labels are tied together by the plane-wave solutions: the helicity spinors and their massless limit — [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]; Lecture 20 then uses the chirality projectors as helicity projectors at $m = 0$ — [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[P9 Helicity Amplitudes|P9]].
> - The vector field, set beside the spinor row by row: [[§C8b.9 Photon Helicity#^rem-c8b-9-1|§C8b.9, Remark: Helicity and chirality for the spinor field and the vector field]]; the two polarization bases: [[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]].
> - The little-group translations that fix the helicity of a field (★ Theorem §C8b.4.3) are the ones that shift a polarization vector by the momentum — [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-2|Theorem §C8b.3.2]], [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]].
> - The same double use of "left" and "right" occurs for the Weyl plane waves — [[§C5a.8 The Weyl Form and the Weyl Equations#^rem-c5a-8-1|§C5a.8, Remark: Why "left-handed"]].
