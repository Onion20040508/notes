---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.13
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.14★ The Poincaré Group and Induced Representations]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): Quantum Mechanics §C8.1★, §C8.3★ (Sakurai) · Yu Zhao-Huan, 量子场论讲义, §3.3.1 · the user's PHY 513 notes, Ch. 7 §§7.2, 7.6 · the user's pre-course notes (Weinberg vol. 1, §2.2, App. 2.A for Wigner's theorem; §2.7, App. 2.B for Bargmann — via the notes) · Hall, Quantum Theory for Mathematicians, Ch. 16 · P. Woit, Quantum Theory, Groups and Representations, §§7.4–7.5 (projective space) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

Why are the symmetries of quantum mechanics represented by unitary or antiunitary operators, why only up to a phase, and why does that allow, and require, the covering groups SU(2) and SL(2, ℂ)? States are rays, so a symmetry is a map of rays that preserves transition probabilities. Wigner's theorem lifts it to a unitary or antiunitary operator, unique up to a phase (decision SPEC-CB 2: proved here; Quantum Mechanics states it, [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]]). A group of symmetries then becomes a projective representation, which for connected groups is unitary and, in finite dimension, lifts to a genuine representation of the universal cover. Groups containing time reversal need antiunitary elements, whose squares are $\pm1$. The section builds on [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] (universal covers, the Lie correspondence) and the course's projective representations ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-14|Def. §C3.1.14]]).

<!-- MOVE row (CB-INVENTORY): ★ Remark rem-c3-1-9 (Bargmann, infinite dimensions) is embedded below; it is to be moved here in batch 3, next to Theorem §CB.13.7. -->

## Rays and Wigner's theorem

> [!definition] Definition §CB.13.1: Ray Space and Transition Probability
> For a complex Hilbert space $\mathcal H$, the **ray space** $P(\mathcal H)$ is the set of one-dimensional subspaces $[\psi] = \mathbb C\psi$, $\psi \ne 0$. The **transition probability** of two rays is $\bigl|\langle\psi, \phi\rangle\bigr|^2/(\|\psi\|^2\|\phi\|^2)$, independent of the representatives.
>
> *Source (planned): Woit, §7.4 · Quantum Mechanics §C8.1★*

^def-cb-13-1

> [!definition] Definition §CB.13.2: Wigner Symmetry
> A **Wigner symmetry** of $\mathcal H$ is a bijection $T : P(\mathcal H) \to P(\mathcal H)$ that preserves transition probabilities ([[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-13-1|Def. §CB.13.1]]). An operator $U$ **induces** $T$ if $T[\psi] = [U\psi]$ for all $\psi \ne 0$.
>
> *Source (planned): Quantum Mechanics §C8.1★ · written here*

^def-cb-13-2

Antilinear and antiunitary operators and their structure, defined and proved in Quantum Mechanics:

![[§C8.3★ Time Reversal#^def-c8-3-1]]

![[§C8.3★ Time Reversal#^thm-c8-3-1]]

> [!theorem] Theorem §CB.13.3: Wigner's Theorem
> Every Wigner symmetry $T$ of a complex Hilbert space $\mathcal H$ ([[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-13-2|Def. §CB.13.2]]) is induced by an operator $U$ that is either unitary or antiunitary ([[§C8.3★ Time Reversal#^def-c8-3-1|QM Def. §C8.3.1]]). $U$ is unique up to a phase $e^{i\alpha}$, and if $\dim\mathcal H \ge 2$ the alternative (unitary or antiunitary) is determined by $T$.
>
> *Source (planned): Weinberg vol. 1, App. 2.A (via the user's pre-course notes) · Hall, Quantum Theory for Mathematicians (to be checked) · stated without proof in [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]]*

^thm-cb-13-3

> [!proof]- Proof (to be filled)
> *Decision SPEC-CB 2: the proof is to be written here (planned route: Weinberg's or Bargmann's construction on an orthonormal basis; Quantum Mechanics will link it).*

^pf-cb-13-3

The statement in Quantum Mechanics:

![[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1]]

## Projective representations

The course's definition, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-14]]

> [!theorem] Theorem §CB.13.4: Connected Groups of Symmetries Act by Unitaries
> Let $G$ be a connected matrix Lie group and $g \mapsto T(g)$ a homomorphism into the group of Wigner symmetries of $\mathcal H$. Then every $T(g)$ is induced by a unitary operator. So a group of symmetries containing an antiunitary one (time reversal) is not connected.
>
> *Source (planned): written here*

^thm-cb-13-4

> [!proof]- Proof
> **1. Squares are unitary.** If $U$ is unitary or antiunitary, $U^2$ is unitary: a product of two antiunitary operators is linear and preserves inner products, since $\langle U^2\psi, U^2\phi\rangle = \overline{\langle U\psi, U\phi\rangle} = \overline{\overline{\langle\psi, \phi\rangle}} = \langle\psi, \phi\rangle$.
>
> **2. Every element is a product of squares.** By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 3, $g = e^{X_1}\cdots e^{X_k}$ with $X_i \in \mathfrak g$, and $e^{X_i} = (e^{X_i/2})^2$ (Theorem §CB.1.2, 3).
>
> **3. Conclusion.** Choose for each $e^{X_i/2}$ an inducing operator $U_i$ (Theorem §CB.13.3). Then $T(e^{X_i}) = T(e^{X_i/2})^2$ is induced by $U_i^2$, unitary by step 1, and $T(g)$ by the product $U_1^2\cdots U_k^2$, unitary. If $T(g)$ is induced by a unitary, it is not induced by an antiunitary (uniqueness in Theorem §CB.13.3, $\dim\mathcal H \ge 2$).

^pf-cb-13-4

> [!definition] Definition §CB.13.5: Lift of a Projective Representation
> Let $p : \tilde G \to G$ be a covering homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]) and $U$ a projective representation of $G$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-14|Def. §C3.1.14]]). A **lift** of $U$ to $\tilde G$ is a genuine continuous representation $\Sigma$ of $\tilde G$ with $U(p(x)) = c(x)\Sigma(x)$, $|c(x)| = 1$, for all $x \in \tilde G$.
>
> *Source (planned): written here*

^def-cb-13-5

> [!theorem] Theorem §CB.13.6: Finite-Dimensional Projective Representations Lift to the Universal Cover
> Let $G$ be a connected matrix Lie group with universal covering group $p : \tilde G \to G$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]), and $W$ finite-dimensional. Every continuous homomorphism $G \to PGL(W) = GL(W)/\mathbb C^\times\mathbb 1$ has a lift ([[§CB.13 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-13-5|Def. §CB.13.5]]) to a continuous representation $\Sigma : \tilde G \to SL(W)$, and the lift into $SL(W)$ is unique (two lifts differ by a continuous homomorphism $\tilde G \to \{\zeta : \zeta^{\dim W} = 1\}$, constant on the connected $\tilde G$); if the projective representation is unitary, so is $\Sigma$. Instances: $SO(3)$ with $\tilde G = SU(2)$, $SO^+(1,3)$ with $\tilde G = SL(2, \mathbb C)$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · the rotation case: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-9|Theorem §C3.1.9]]*

^thm-cb-13-6

> [!proof]- Proof (to be filled)
> *To be filled (normalize to determinant $1$ locally, differentiate to a representation of $\mathfrak g$ in $\mathfrak{sl}(W)$, integrate on the simply connected $\tilde G$ by Theorem §CB.1.24, compare with $U\circ p$ by Theorem §CB.1.17).*

^pf-cb-13-6

The rotation case, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-9]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-9]]

> [!theorem] Theorem §CB.13.7: Bargmann's Theorem
> Let $\tilde G$ be a connected and simply connected Lie group whose Lie algebra $\mathfrak g$ has the property that every real skew-symmetric bilinear form $\beta$ on $\mathfrak g$ with $\beta([X, Y], Z) + \beta([Y, Z], X) + \beta([Z, X], Y) = 0$ is of the form $\beta(X, Y) = f([X, Y])$ for a linear $f : \mathfrak g \to \mathbb R$ (vanishing second cohomology). Then every continuous projective unitary representation of $\tilde G$ on a separable Hilbert space is induced by a continuous unitary representation of $\tilde G$. This holds for $SU(2)$, $SL(2, \mathbb C)$ and the universal cover $\mathbb R^{1,3}\rtimes SL(2, \mathbb C)$ of the Poincaré group (§CB.14★).
>
> *Source (planned): Bargmann (1954), via Weinberg vol. 1, §2.7 and App. 2.B, as cited in the user's pre-course notes · Hall, Quantum Theory for Mathematicians, Ch. 16 (to be checked)*

^thm-cb-13-7

> [!proof]- Proof (to be filled)
> *To be filled, or stated only with a precise reference (infinite-dimensional; beyond the course's finite-dimensional tools).*

^pf-cb-13-7

## Antiunitary symmetries

> [!definition] Definition §CB.13.8: Unitary–Antiunitary Representation
> Let $G_0 \subset G$ be a subgroup of index $2$. A **unitary–antiunitary representation** (corepresentation) of $(G, G_0)$ on $\mathcal H$ assigns to each $g \in G$ an operator $U(g)$, unitary for $g \in G_0$ and antiunitary for $g \notin G_0$, with $U(g)U(h) = e^{i\varphi(g, h)}U(gh)$. Example: the Lorentz group with $\mathcal T$, $G_0$ the subgroup without time reversal, $U(\mathcal T)$ antiunitary.
>
> *Source (planned): written here · Quantum Mechanics §C8.3★*

^def-cb-13-8

> [!theorem] Theorem §CB.13.9: The Square of an Antiunitary Involution Is ±1
> If $\Theta$ is antiunitary and $\Theta^2 = c\mathbb 1$ for a number $c$, then $c = \pm1$. If $c = -1$, then $\Theta\psi$ is orthogonal to $\psi$ for every $\psi$.
>
> *Source (planned): written here · [[§C8.3★ Time Reversal#^thm-c8-3-7|QM Theorem §C8.3.7]] (Kramers)*

^thm-cb-13-9

> [!proof]- Proof
> **1. c is real.** $\Theta^3 = \Theta\Theta^2 = \Theta(c\mathbb 1) = \bar c\,\Theta$ because $\Theta$ is antilinear, and $\Theta^3 = \Theta^2\Theta = c\,\Theta$. Since $\Theta \ne 0$, $\bar c = c$.
>
> **2. |c| = 1.** $\Theta^2$ is unitary (step 1 of Theorem §CB.13.4), so $\|c\psi\| = \|\psi\|$ and $|c| = 1$. With step 1, $c = \pm1$.
>
> **3. c = −1.** For antiunitary $\Theta$, $\langle\Theta\phi, \Theta\chi\rangle = \overline{\langle\phi, \chi\rangle} = \langle\chi, \phi\rangle$. With $\phi = \Theta\psi$, $\chi = \psi$: $\langle\Theta^2\psi, \Theta\psi\rangle = \langle\psi, \Theta\psi\rangle$, i.e. $-\langle\psi, \Theta\psi\rangle = \langle\psi, \Theta\psi\rangle$, so $\langle\psi, \Theta\psi\rangle = 0$.

^pf-cb-13-9

> [!theorem] Theorem §CB.13.10: An Antiunitary Operator Reversing Spin Squares to (−1)²ʲ
> Let $\Theta$ be antiunitary on the spin-$j$ representation $V_j$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]) with $\Theta J^a\Theta^{-1} = -J^a$ for $a = 1, 2, 3$. Then $\Theta^2 = (-1)^{2j}\mathbb 1$. In particular an antiunitary time reversal acts on spinors with $\Theta^2 = -1$ and on tensors with $\Theta^2 = +1$.
>
> *Source (planned): [[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]] · written here*

^thm-cb-13-10

> [!proof]- Proof (to be filled)
> *To be filled ($\Theta^2$ is linear and commutes with every $J^a$, so it is a scalar by [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]], $\pm1$ by Theorem §CB.13.9; evaluate on the standard basis with $\Theta = \eta\,e^{-i\pi J^2}K$).*

^pf-cb-13-10

The course's remark on why states carry unitary representations of the covering group, in [[§C3.5 Quantum Poincaré Transformations|§C3.5]]:

![[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-1]]

> [!remark]- Connections
> - Theorem §CB.13.4 is why continuous symmetries (rotations, boosts, translations) are unitary and only discrete ones can be antiunitary: time reversal is antiunitary ([[§C8.3★ Time Reversal#^thm-c8-3-3|QM Theorem §C8.3.3]]), parity unitary ([[§C9.3 Parity on States, Spinors and the Dirac Field|§C9.3]]); C, T, CPT follow after Lecture 12 (QFT C9, planned).
> - Theorem §CB.13.6 and Theorem §CB.13.7 are the precise forms of "spin ½ is a representation of SU(2), not SO(3)": the two-valuedness of §C3.1 and §C5a.4 is the projective representation, and its lift is the genuine representation of the covering group (§CB.9).
> - **Used in**: Definitions §CB.13.1–Theorem §CB.13.3 — [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-1|QM Theorem §C8.1.1]], [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-1|§C3.5, Remark: Why unitary, why the covering group]]; Theorem §CB.13.4 — [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-2|Theorem §C3.5.2]]; Theorem §CB.13.6 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-9|Theorem §C3.1.9]], [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-8|§C3.1, Remark: The same pattern for the Lorentz group]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.13.7 — [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]]; Theorems §CB.13.9–§CB.13.10 — [[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]], [[§C8.3★ Time Reversal#^thm-c8-3-7|QM Theorem §C8.3.7]], time reversal in QFT C9 (planned).
