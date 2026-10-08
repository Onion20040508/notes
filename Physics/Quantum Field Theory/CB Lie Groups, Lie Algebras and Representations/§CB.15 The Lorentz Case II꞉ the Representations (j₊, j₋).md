---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.15
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵]] →

*Sources: the user's PHY 513 notes, Ch. 7 §7.4 (the (j₊, j₋) classification) · PHY 513 Lecture 7 (Larsen), Part C · Peskin & Schroeder, §3.1, pp. 38–41 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it; submitted) · Yu Zhao-Huan, 量子场论讲义, §3.2, §4.1, Exercise 3.1 and opening of Ch. 5 · P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here.*

What are the finite-dimensional representations of $SL(2, \mathbb C)$, and which of them are representations of the Lorentz group? With the spin group of [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.14]] and the split $\mathbf J_\pm$ of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms|§CB.4]], this section identifies the finite-dimensional representations of $SL(2, \mathbb C)$ with pairs of commuting $\mathfrak{sl}(2, \mathbb C)$-representations, lists the irreducible ones as the $(j_+, j_-)$, and decides which of them descend to $SO^+(1,3)$. It uses spin $j$ from [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.8]] and the descent criterion of [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.12]]. The course's labels ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]]) and their properties — rotation content, the sign of a $2\pi$ rotation, the tensor/spinor split, products, parity, complex conjugation and non-unitarity — are stated here; the course's descent theorem ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]) is shown as an embed.

<!-- Planned content (OPTION1-PLAN §5, row "CB.11a"): batch B2 moves Thm §C5a.4.8 here (replacing its embed). The C3.3 boxes arrived in B1 (2026-10-08). -->

*Conventions* (the course's, [[Larsen PHY 513]]): $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$, $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]]). From Definition §CB.15.2 on, the boxes are stated for representations of the Lorentz algebra $\mathfrak{so}(1,3)$ on a complex space $V$; by Theorem §CB.15.1 these are the same as the representations of $SL(2, \mathbb C)$.

## The finite-dimensional representations of SL(2,ℂ)

> [!theorem] Theorem §CB.15.1: Representations of SL(2,ℂ) Are Pairs of 𝔰𝔩(2,ℂ)-Representations
> For finite-dimensional representations on complex spaces, the following correspond bijectively, preserving invariant subspaces, irreducibility and intertwiners: continuous representations of $SL(2, \mathbb C)$; representations of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-18|Theorem §CB.2.18]], $SL(2, \mathbb C)$ being simply connected, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); commuting pairs $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]]); complex-linear representations of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]). All of them are completely reducible ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-22|Theorem §CB.5.22]]).
>
> *Source: written here (assembly of the cited theorems)*

^thm-cb-15-1

> [!proof]- Proof
> **1. Group to algebra.** A continuous representation $D : SL(2, \mathbb C) \to GL(W)$ is a Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]); its differential $d = D_\ast$ is a representation of the Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-12|Def. §CB.4.12]]).
>
> **2. Algebra to group, bijectively.** $SL(2, \mathbb C)$ is connected and simply connected ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), so every representation $d$ of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ is $D_\ast$ for exactly one $D$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-18|Theorem §CB.2.18]]). Two representations with the same differential are equal ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-11|Theorem §CB.2.11]]). So $D \mapsto D_\ast$ is a bijection.
>
> **3. Intertwiners agree.** Let $T : W_1 \to W_2$ be linear. If $TD_1(g) = D_2(g)T$ for all $g$, then differentiating $TD_1(e^{sX}) = D_2(e^{sX})T$ at $s = 0$ gives $Td_1(X) = d_2(X)T$ (Theorem §CB.2.3). Conversely, if $Td_1(X) = d_2(X)T$, then $Td_1(X)^n = d_2(X)^nT$ for all $n$, and summing the series $TD_1(e^X) = Te^{d_1(X)} = e^{d_2(X)}T = D_2(e^X)T$; every $g$ is a product of exponentials ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3), so $TD_1(g) = D_2(g)T$. In particular $D_1 \cong D_2$ iff $d_1 \cong d_2$ (invertible intertwiners, [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-3|Def. §CB.5.3]]).
>
> **4. Invariant subspaces agree.** If $W' \subset W$ is invariant under all $D(g)$, then $d(X)w = \lim_{s\to0}\frac1s(D(e^{sX})w - w) \in W'$ for $w \in W'$ ($W'$ is closed, being finite-dimensional). If $W'$ is invariant under all $d(X)$, it is invariant under every power and hence under $e^{d(X)} = D(e^X)$, and so under all products of exponentials, i.e. all of $SL(2, \mathbb C)$ (Theorem §CB.2.10, 3). Hence irreducibility agrees too.
>
> **5. The other two descriptions.** A representation of the real algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on the complex space $W$ is the same as a commuting pair $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]]), and the same as a complex-linear representation of its complexification ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]], 1), with the same invariant subspaces and intertwiners (Theorem §CB.3.8, 2). The complexification is isomorphic to $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]), and pulling back along an isomorphism of Lie algebras changes neither invariant subspaces nor intertwiners. The isomorphism $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ is [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]].
>
> **6. Complete reducibility.** Every finite-dimensional representation of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on a complex space is completely reducible ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-22|Theorem §CB.5.22]]); by step 4 the same decomposition into invariant subspaces works for the group.
>
> **What the proof shows**
> - Simple connectivity of $SL(2, \mathbb C)$ is what makes every algebra representation a group representation; for $SO^+(1,3)$ only those with $D(-\mathbb 1) = \mathbb 1$ survive (Theorem §CB.15.12).
> - Continuity is the only regularity assumed on the group side: differentiability comes from the matrix Lie group theory of §CB.1–§CB.2.

^pf-cb-15-1

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-11|Theorem §CB.2.11]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-18|Theorem §CB.2.18]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-3|Def. §CB.5.3]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-22|Theorem §CB.5.22]]

The course's representations $(j_+, j_-)$ and their irreducibility, and the classification (PHY 513 Lecture 7, Part C; Problem Set 5, Problem 1):

> [!definition] Definition §CB.15.2: The Representation (j₊, j₋)
> For $j_+, j_- \in \{0, \frac12, 1, \frac32, \dots\}$ let $\mathbf J^{(j)}$ be the spin-$j$ matrices on $\mathbb C^{2j+1}$ (with $\mathbf J^{(0)} = 0$ on $\mathbb C$). The representation $(j_+, j_-)$ of the Lorentz algebra is the space $V = \mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1}$ with
>
> $$
> \mathbf J_+ = \mathbf J^{(j_+)}\otimes\mathbb 1, \qquad \mathbf J_- = \mathbb 1\otimes\mathbf J^{(j_-)}, \qquad\text{i.e.}\qquad \mathbf J = \mathbf J^{(j_+)}\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J^{(j_-)}, \quad \mathbf K = -i\bigl(\mathbf J^{(j_+)}\otimes\mathbb 1 - \mathbb 1\otimes\mathbf J^{(j_-)}\bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 (Definition "The representation (j₊, j₋)") · PHY 513, Problem Set 5, Problem 1(b) (statement) · PHY 513 Lecture 7, Part C (HW5 clue)*

^def-cb-15-2

The spin-$j$ matrices are those of Quantum Mechanics in the basis $|j, m\rangle$, $m = j, \dots, -j$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-7|QM Theorem §B6.1.7]] with $\hbar = 1$): $J^{(j)}_3$ diagonal with entries $m$, $J^{(j)}_\pm$ with the real ladder coefficients, so $J^{(j)}_1$ and $J^{(j)}_3$ are real and $J^{(j)}_2$ is imaginary; for $j = \frac12$, $\mathbf J^{(1/2)} = \frac12\boldsymbol\sigma$. The pre-course notes and Weinberg write the labels as $(A, B)$. Each label is a spin chosen for one copy of the rotation algebra; it is not the spin of the field ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-2|Remark: Neither label is the spin]]).

> [!theorem] Theorem §CB.15.3: (j₊, j₋) Is Irreducible
> $(j_+, j_-)$ is a representation of the Lorentz algebra of dimension $(2j_+ + 1)(2j_- + 1)$. It is irreducible, its Casimir operators are the numbers
>
> $$
> \mathbf J_+^2 = j_+(j_+ + 1)\,\mathbb 1, \qquad \mathbf J_-^2 = j_-(j_- + 1)\,\mathbb 1 ,
> $$
>
> and different labels give inequivalent representations.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 (Definition "The representation (j₊, j₋)": "It is irreducible: every vector feels both copies") · PHY 513, Problem Set 5, Problem 1(b) (dimension; statement) · the irreducibility argument written out here*

^thm-cb-15-3

> [!derivation]- Derivation
> **1. It is a representation.** For the $+$ copy, $[J^{(j_+)}_i\otimes\mathbb 1, J^{(j_+)}_j\otimes\mathbb 1] = [J^{(j_+)}_i, J^{(j_+)}_j]\otimes\mathbb 1 = i\varepsilon_{ijk}J^{(j_+)}_k\otimes\mathbb 1$, because the spin-$j$ matrices obey the rotation algebra ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-4|QM Theorem §C5.1.4]]); the same for the $-$ copy. Across copies, $(A\otimes\mathbb 1)(\mathbb 1\otimes B) = A\otimes B = (\mathbb 1\otimes B)(A\otimes\mathbb 1)$, so $[J_{+i}, J_{-j}] = 0$. By Theorem §CB.4.7, 2, the formulas of Def. §CB.15.2 represent the Lorentz algebra.
>
> **2. Dimension.** $\dim(\mathbb C^{a}\otimes\mathbb C^{b}) = ab$, here $(2j_+ + 1)(2j_- + 1)$.
>
> **3. Casimirs.** $\mathbf J_+^2 = (\mathbf J^{(j_+)})^2\otimes\mathbb 1 = j_+(j_+ + 1)\,\mathbb 1$ by the spectrum of angular momentum on a multiplet ([[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-4|QM Theorem §B5.2.4]]); likewise $\mathbf J_-^2$.
>
> **4. A nonzero invariant subspace contains a basis vector.** Let $W \ne \{0\}$ be invariant under all six generators, hence under $J_{\pm3}$ and the ladder operators $J_{\pm,\uparrow} \equiv J_{\pm1} + iJ_{\pm2}$, $J_{\pm,\downarrow} \equiv J_{\pm1} - iJ_{\pm2}$ (linear combinations). The vectors $|m_+\rangle\otimes|m_-\rangle$ form a basis of common eigenvectors of $J_{+3}$ and $J_{-3}$ with eigenvalue pairs $(m_+, m_-)$, each pair occurring once. Take $0 \ne w = \sum c_{m_+m_-}|m_+\rangle\otimes|m_-\rangle \in W$ and a pair $(a, b)$ with $c_{ab} \ne 0$. The polynomial $P = \prod_{m_+ \ne a}(J_{+3} - m_+)\prod_{m_- \ne b}(J_{-3} - m_-)$ in the generators maps $W$ into $W$ and kills every basis vector except $|a\rangle\otimes|b\rangle$, which it multiplies by $\prod_{m_+ \ne a}(a - m_+)\prod_{m_- \ne b}(b - m_-) \ne 0$. So $|a\rangle\otimes|b\rangle \in W$.
>
> **5. The ladders reach every basis vector.** $J_{+,\uparrow}(|m\rangle\otimes|b\rangle) = \sqrt{(j_+ - m)(j_+ + m + 1)}\,|m + 1\rangle\otimes|b\rangle$ ([[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-5|QM Theorem §B5.2.5]]), nonzero for $m < j_+$; $J_{+,\downarrow}(|m\rangle\otimes|b\rangle) = \sqrt{(j_+ + m)(j_+ - m + 1)}\,|m - 1\rangle\otimes|b\rangle$, nonzero for $m > -j_+$; and $J_{-,\uparrow}$, $J_{-,\downarrow}$ act by the same formulas on the second factor, with $j_-$ in place of $j_+$, leaving the first factor alone. Starting from $|a\rangle\otimes|b\rangle$ and stepping in each factor reaches every $|m_+\rangle\otimes|m_-\rangle$ with a nonzero coefficient, so all basis vectors lie in $W$: $W = V$. ⚑ By-product: the precise meaning of "every vector feels both copies": no subspace is closed under one copy's ladders without being closed under the other's.
>
> **6. Inequivalence.** If $D'(X) = UD(X)U^{-1}$ for all generators, then $\mathbf J_\pm'^2 = U\mathbf J_\pm^2U^{-1}$; on $(j_+, j_-)$ these are the numbers $j_\pm(j_\pm + 1)$, which conjugation does not change. Since $j \mapsto j(j+1)$ is injective for $j \ge 0$, equivalent representations have equal labels.
>
> **What the derivation shows**
> - Irreducibility rests only on the nonzero ladder coefficients of each spin-$j$ multiplet: the same reason that a single multiplet is irreducible under rotations ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-1|QM Theorem §C5.3.1]]).
> - The pair of Casimir values is a complete invariant of an irreducible finite-dimensional representation (with Theorem §CB.15.4).
> - Used next: the classification (Theorem §CB.15.4) and every identification of a field's representation by its Casimirs (Theorem §C3.2.2; [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]).

^der-cb-15-3

*Uses:* [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-4|QM Theorem §C5.1.4]], [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-4|QM Theorem §B5.2.4]], [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-5|QM Theorem §B5.2.5]]

> [!theorem] Theorem §CB.15.4: Every Finite-Dimensional Representation Is a Sum of (j₊, j₋)
> Every representation of the Lorentz algebra on a finite-dimensional complex space $V$ is a direct sum of representations $(j_+, j_-)$. The multiplicity of each $(j_+, j_-)$ is fixed by the representation, and $V$ carries an inner product in which all $J_{\pm i}$ are Hermitian.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 ("Every finite-dimensional representation is a direct sum of these"; stated there) · PHY 513, Problem Set 5, Problem 1(b) ("the finite dimensional representations of the Lorentz algebra are therefore labelled by a pair (j₊, j₋)"; statement) · the derivation (Weyl's unitarian trick) written out here, with the two inputs from Lie theory quoted*

^thm-cb-15-4

> [!derivation]- Derivation
> **1. Two commuting angular momenta.** By Theorem §CB.4.7, $V$ carries two commuting triples $J_{+i}$, $J_{-i}$, each obeying the rotation algebra.
>
> **2. A compact group behind them.** The six matrices $-iJ_{+i}$, $-iJ_{-i}$ span, with real coefficients, a real Lie algebra with brackets $[-iJ_{\pm i}, -iJ_{\pm j}] = -[J_{\pm i}, J_{\pm j}] = \varepsilon_{ijk}(-iJ_{\pm k})$ and $[-iJ_{+i}, -iJ_{-j}] = 0$: two commuting copies of the Lie algebra of $SU(2)$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]]). Input from Lie theory, quoted: because $SU(2)\times SU(2)$ is simply connected ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-7|Theorem §CB.8.7]] for each factor), this algebra representation is the derivative of a representation $R$ of the group $G = SU(2)\times SU(2)$ on $V$, with $R(e^{-i\boldsymbol\alpha\cdot\boldsymbol\tau}, e^{-i\boldsymbol\beta\cdot\boldsymbol\tau}) = e^{-i\boldsymbol\alpha\cdot\mathbf J_+ - i\boldsymbol\beta\cdot\mathbf J_-}$, $\boldsymbol\tau = \boldsymbol\sigma/2$.
>
> **3. An invariant inner product.** $G$ is compact. It carries a probability measure $dg$ invariant under translations, $\int f(gh)\,dg = \int f(g)\,dg$ for every $h \in G$: the product of the invariant integral on each $SU(2) = S^3$ constructed in [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^der-cb-5-17|Derivation §CB.5.17]], step 1. Starting from any inner product $(\cdot, \cdot)$ on $V$, define $\langle v, w\rangle = \int(R(g)v, R(g)w)\,dg$. It is positive definite (an average of positive numbers, continuous in $g$) and invariant: $\langle R(h)v, R(h)w\rangle = \int(R(gh)v, R(gh)w)\,dg = \langle v, w\rangle$, using $R(g)R(h) = R(gh)$ and the invariance of $dg$. So every $R(g)$ is unitary for $\langle\cdot, \cdot\rangle$: the argument of [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-17|Theorem §CB.5.17]], run on $SU(2)\times SU(2)$.
>
> **4. The generators are Hermitian.** For each $i$, $t \mapsto e^{-itJ_{+i}} = R(e^{-it\tau_i}, \mathbb 1)$ is unitary for every real $t$. Differentiating $\langle e^{-itJ_{+i}}v, e^{-itJ_{+i}}w\rangle = \langle v, w\rangle$ at $t = 0$ gives $\langle -iJ_{+i}v, w\rangle + \langle v, -iJ_{+i}w\rangle = 0$, i.e. $J_{+i}^\dagger = J_{+i}$. Likewise $J_{-i}^\dagger = J_{-i}$.
>
> **5. Complete reducibility.** Let $W \subset V$ be invariant under all $J_{\pm i}$, and $W^\perp$ its orthogonal complement for $\langle\cdot, \cdot\rangle$. For $u \in W^\perp$, $w \in W$: $\langle J_{\pm i}u, w\rangle = \langle u, J_{\pm i}w\rangle = 0$ (Hermiticity, then $J_{\pm i}w \in W$). So $W^\perp$ is invariant and $V = W\oplus W^\perp$. Repeating inside $W$ and $W^\perp$ (the dimension drops each time) writes $V$ as a direct sum of irreducible invariant subspaces.
>
> **6. One irreducible piece.** Let $U \subset V$ be irreducible. $\mathbf J_+^2$ commutes with all $J_{+i}$ (the angular-momentum Casimir, [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-4|QM Theorem §B5.2.4]]) and with all $J_{-i}$ (different copies commute), and it is Hermitian; its eigenspaces in $U$ are therefore invariant, and irreducibility leaves one eigenvalue (as in [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-14|Theorem §CB.5.14]]): $\mathbf J_+^2 = j_+(j_+ + 1)$ on $U$, and likewise $\mathbf J_-^2 = j_-(j_- + 1)$, by the angular-momentum spectrum for Hermitian generators.
>
> **7. Highest weights of the + copy.** Let $H = \{u \in U : J_{+3}u = j_+u\}$. By the ladder theory of one angular momentum ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-3|Theorem §CB.8.3]], with complete reducibility under the $+$ copy from step 5 applied to that copy alone), $U$ decomposes under the $+$ copy alone into spin-$j_+$ multiplets, each containing exactly one direction in $H$ (its top vector, killed by $J_{+,\uparrow}$); so $\dim U = (2j_+ + 1)\dim H$. Since the $J_{-i}$ commute with $J_{+3}$, they map $H$ into itself: $H$ carries a representation of the $-$ copy.
>
> **8. The isomorphism.** Define $\Phi: \mathbb C^{2j_++1}\otimes H \to U$ by $\Phi(|m\rangle\otimes h) =$ the vector of the $+$ multiplet through $h$ with $J_{+3} = m$, obtained from $h$ by $J_{+,\downarrow}^{\,j_+ - m}$ and normalized with the ladder coefficients. $\Phi$ is onto (every multiplet has its top in $H$) and between spaces of equal dimension (step 7), hence bijective; it turns $\mathbf J^{(j_+)}\otimes\mathbb 1$ into $\mathbf J_+$ (the multiplet's standard matrices) and $\mathbb 1\otimes\mathbf J_-|_H$ into $\mathbf J_-$ (which commutes with the $+$ ladders). If $H$ had a proper invariant subspace $H'$ under the $-$ copy, $\Phi(\mathbb C^{2j_++1}\otimes H')$ would be a proper invariant subspace of $U$; so $H$ is irreducible under one angular momentum with Casimir $j_-(j_- + 1)$, i.e. a single spin-$j_-$ multiplet. Hence $U \cong (j_+, j_-)$.
>
> **9. Multiplicities.** The joint eigenspace of the commuting Hermitian operators $\mathbf J_+^2$, $\mathbf J_-^2$ with eigenvalues $j_\pm(j_\pm + 1)$ is the sum of the pieces labelled $(j_+, j_-)$; its dimension, divided by $(2j_+ + 1)(2j_- + 1)$, is the multiplicity, and it depends only on the operators, not on the chosen decomposition.
>
> **What the derivation shows**
> - One input was quoted, not derived: that a representation of the Lie algebra $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ integrates to the simply connected group $SU(2)\times SU(2)$. Everything else is the invariant integral and the ladder theory of §C3.1 and Quantum Mechanics.
> - The Hermitian inner product of step 4 makes $\mathbf J_\pm$ Hermitian, hence $\mathbf J$ Hermitian and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ anti-Hermitian: the non-unitarity of boosts is built in → [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-11|Theorem §CB.15.11]].
> - The compact group used is not the Lorentz group: $SU(2)\times SU(2)$ is reached by real combinations of $-i\mathbf J_\pm$, which mix $\mathbf J$ with $i\mathbf K$ ("Weyl's unitarian trick"). Only the algebra is shared.
> - Used next: Theorems §C3.2.2, §CB.15.11, and every "which representation is this field" question in [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]].

^der-cb-15-4

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§B5.2 Orbital Angular Momentum and Spherical Harmonics#^thm-b5-2-4|QM Theorem §B5.2.4]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-14|Theorem §CB.5.14]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-17|Theorem §CB.5.17]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-3|Theorem §CB.8.3]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-7|Theorem §CB.8.7]]; quoted: integration of Lie-algebra representations to simply connected groups

> [!theorem] Theorem §CB.15.5: The Irreducible Representations of SL(2,ℂ)
> For $j_+, j_- \in \frac12\mathbb Z_{\ge0}$,
>
> $$
> D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}\bigl((\lambda^\dagger)^{-1}\bigr) \quad\text{on}\quad \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\mathbb C^2
> $$
>
> ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]]; $(\lambda^\dagger)^{-1} \cong \bar\lambda$ by [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]) is an irreducible representation of $SL(2, \mathbb C)$ of dimension $(2j_+ + 1)(2j_- + 1)$, whose generators, read through the course's covering $\pi$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), are those of $(j_+, j_-)$: $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1}$ is equivalent to the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]]; which factor carries $\mathbf J_+$ is fixed by [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]). Every finite-dimensional irreducible continuous representation of $SL(2, \mathbb C)$ is equivalent to exactly one $D^{(j_+, j_-)}$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3, Ch. 8 §8.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]] and [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]] · written here (from Theorems §CB.15.1, §CB.6.5, §CB.8.4)*

^thm-cb-15-5

> [!proof]- Proof
> Write $\theta(\lambda) = (\lambda^\dagger)^{-1}$ and $\operatorname{Sym}^k(A)$ for the restriction of $A^{\otimes k}$ to $\operatorname{Sym}^k\mathbb C^2$.
>
> **1. A continuous representation.** $\operatorname{Sym}^k\mathbb C^2$ is invariant under $A^{\otimes k}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], 1), and $(AB)^{\otimes k} = A^{\otimes k}B^{\otimes k}$, so $A \mapsto \operatorname{Sym}^k(A)$ is a homomorphism. $\theta$ is a homomorphism of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 1), and a tensor product of representations is one. The entries of $D^{(j_+, j_-)}(\lambda)$ are polynomials in the entries of $\lambda$ and $\bar\lambda$ ($\lambda^{-1}$ is the adjugate, since $\det\lambda = 1$), so $D^{(j_+, j_-)}$ is continuous. Its dimension is $\dim\operatorname{Sym}^{2j_+}\mathbb C^2\cdot\dim\operatorname{Sym}^{2j_-}\mathbb C^2 = (2j_+ + 1)(2j_- + 1)$ (Theorem §CB.6.13, 1, $\binom{2j+1}{2j} = 2j + 1$).
>
> **2. It is the course's representation.** By [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]], $\operatorname{Sym}^{2j}\mathbb C^2$ with $\operatorname{Sym}^{2j}(\lambda)$ is equivalent to the polynomial realization $P(z) \mapsto P(\lambda^{\mathsf T}z)$ on homogeneous polynomials of degree $2j$. The tensor product of the two equivalences is an equivalence of $D^{(j_+, j_-)}$ with $\tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}(\theta(\lambda))$ of Theorem §C5a.4.8.
>
> **3. Its generators.** Theorem §C5a.4.8, 1: $\tilde D(\Lambda_L(s\omega)) = \exp(-\frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ with $D(\mathcal J^{\mu\nu})$ the generators of $(j_+, j_-)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]]). $s \mapsto \Lambda_L(s\omega) = e^{sA_L(\omega)}$ is a one-parameter subgroup with $\pi_\ast(A_L(\omega)) = -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ (it covers $e^{s\omega}$, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]). Differentiating at $s = 0$: $\tilde D_\ast(A_L(\omega)) = d\bigl(\pi_\ast(A_L(\omega))\bigr)$, where $d$ is the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$, $d(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}) = -\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})$. The $A_L(\omega)$ fill $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, so $\tilde D_\ast = d\circ\pi_\ast$, and by step 2 $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1} \cong d$ (equivalent group representations have equivalent differentials, [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]]).
>
> **4. Irreducible.** $(j_+, j_-)$ is irreducible ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]]), and $\pi_\ast$ is a bijection ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]]), so $D^{(j_+, j_-)}_\ast$ has no invariant subspaces but $0$ and the whole space; by Theorem §CB.15.1 neither has $D^{(j_+, j_-)}$.
>
> **5. Every irreducible representation is one of them.** Let $E$ be a finite-dimensional irreducible continuous representation. $E_\ast\circ\pi_\ast^{-1}$ is an irreducible representation of $\mathfrak{so}(1,3)$ (Theorem §CB.15.1). Its complex-linear extension to $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], 2) is irreducible ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]], 2), hence equivalent to $W_+\boxtimes W_-$ with $W_\pm$ irreducible representations of $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-5|Theorem §CB.6.5]], 2), and each $W_\pm$ is some $V_{j_\pm}$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-4|Theorem §CB.8.4]], 3): $\mathbf J_+$ acts as $\mathbf J^{(j_+)}\otimes\mathbb 1$ and $\mathbf J_-$ as $\mathbb 1\otimes\mathbf J^{(j_-)}$, which is Def. §CB.15.2 (equivalently, [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]] with one summand). By step 3, $E_\ast \cong D^{(j_+, j_-)}_\ast$, so $E \cong D^{(j_+, j_-)}$ (Theorem §CB.15.1).
>
> **6. Exactly one.** If $D^{(j_+, j_-)} \cong D^{(k_+, k_-)}$, their differentials are equivalent, so $(j_+, j_-) \cong (k_+, k_-)$ as $\mathfrak{so}(1,3)$-representations, and the labels coincide (Theorem §CB.15.3, last clause).
>
> **What the proof shows**
> - $(j_+, j_-)$ is $2j_+$ symmetrized slots carrying $\lambda$ and $2j_-$ carrying $(\lambda^\dagger)^{-1}$ — undotted and dotted indices ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]).
> - ⚑ By-product (convention): the labels are tied to $\pi$. Read through $\rho$ and the Clifford identification $\phi$, $x \mapsto D^{(j_+, j_-)}(\phi(x))$ is $D^{(j_+, j_-)}\circ\theta$ in the course's parametrization ($\phi = \theta\circ(\theta\circ\phi)$, Theorem §CB.14.4, 2), which is equivalent to $D^{(j_-, j_+)}$: the two factors exchange roles. This is the group form of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]].

^pf-cb-15-5

*Uses:* [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-5|Theorem §CB.6.5]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-4|Theorem §CB.8.4]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-13|Theorem §CB.4.13]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]]

## Rotation content, products, parity, conjugation

> [!theorem] Theorem §CB.15.6: Rotation Content and the Sign of a 2π Rotation
> 1. Under rotations, $(j_+, j_-)$ is the product $D^{(j_+)}(R)\otimes D^{(j_-)}(R)$ and contains each spin $j = |j_+ - j_-|, |j_+ - j_-| + 1, \dots, j_+ + j_-$ exactly once.
> 2. A rotation by $2\pi$ about any axis acts on $(j_+, j_-)$ as
>
> $$
> e^{-2\pi i\,\hat{\mathbf n}\cdot\mathbf J} = (-1)^{2(j_+ + j_-)} .
> $$
>
> 3. Hence for $j_+ + j_-$ half-integer, $\Lambda \mapsto D(\Lambda)$ is not a representation of $SO^+(1,3)$: the identity $e^{2\pi M^{12}} = \mathbb 1$ is sent to $-\mathbb 1$, and $D(\Lambda)$ is defined only up to sign, a projective representation; for $j_+ + j_-$ an integer the sign is $+1$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4 (Principle "Spin content, and the sign of a 2π rotation", eq. (twopisign)) · PHY 513 Lecture 7, Part B (Weyl spinors are spin ½ under rotations)*

^thm-cb-15-6

> [!derivation]- Derivation
> **1. Restrict to rotations.** With $\boldsymbol\eta = 0$, Theorem §CB.4.8 gives $D = e^{-i\boldsymbol\theta\cdot\mathbf J_+}e^{-i\boldsymbol\theta\cdot\mathbf J_-} = e^{-i\boldsymbol\theta\cdot\mathbf J^{(j_+)}}\otimes e^{-i\boldsymbol\theta\cdot\mathbf J^{(j_-)}}$ on $(j_+, j_-)$, using $e^{A\otimes\mathbb 1} = e^A\otimes\mathbb 1$ (term by term) and $(A\otimes\mathbb 1)(\mathbb 1\otimes B) = A\otimes B$. This is the rotation of a composite system of two angular momenta $j_+$ and $j_-$, generated by $\mathbf J = \mathbf J_+ + \mathbf J_-$ ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-1|QM Theorem §C7.1.1]]).
>
> **2. Clebsch–Gordan series.** By [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]], $D^{(j_+)}\otimes D^{(j_-)} = \bigoplus_{j = |j_+ - j_-|}^{j_+ + j_-}D^{(j)}$, each once. (Dimension check: $\sum_j(2j + 1) = (2j_+ + 1)(2j_- + 1)$.)
>
> **3. The 2π rotation.** In step 1 with $\boldsymbol\theta = 2\pi\hat{\mathbf n}$, each factor is a $2\pi$ rotation in a single multiplet, $e^{-2\pi i\hat{\mathbf n}\cdot\mathbf J^{(j)}} = (-1)^{2j}$ ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-4|QM Theorem §C5.3.4]]); the tensor product of $(-1)^{2j_+}\mathbb 1$ and $(-1)^{2j_-}\mathbb 1$ is $(-1)^{2j_+ + 2j_-}\mathbb 1$.
>
> **4. Consistency of the sign.** All spins in step 2 differ from $j_+ + j_-$ by integers, so $(-1)^{2j}$ is the same for each: a representation is either wholly "bosonic" or wholly "fermionic" under rotations.
>
> **5. Part 3.** $e^{2\pi M^{12}}$ is the rotation by $2\pi$ about $z$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]), the identity of $SO^+(1,3)$. Its parameters are $\omega_{12} = 2\pi$, i.e. $\boldsymbol\theta = 2\pi\hat{\mathbf z}$, $\boldsymbol\eta = 0$, and step 3 assigns it $(-1)^{2(j_+ + j_-)}\mathbb 1$; a representation must send the identity to $\mathbb 1$. Since also $e^{0} = \mathbb 1$ is assigned $\mathbb 1$, the same group element receives both signs: the matrix is fixed only up to sign, a two-valued representation ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-8-6|Def. §CB.8.6]]; the topology behind it, [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-8-2|§CB.8, Remark: The same pattern for the Lorentz group]]).
>
> **What the derivation shows**
> - The rotation content of a Lorentz representation is ordinary addition of angular momentum; nothing about boosts enters.
> - The half-integer representations are honest representations of the double cover $SL(2, \mathbb C)$ of $SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), as spin $\frac12$ is of $SU(2)$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-8|Theorem §CB.8.8]]; [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]); that the integer ones are honest representations of $SO^+(1,3)$ itself needs that double-cover structure and is not proved here (it is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], 2).
> - Used next: the catalogue ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|Remark: The representations met in the course]]); the sign of spinor fields ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]).

^der-cb-15-6

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-8|Theorem §CB.4.8]], [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-1|QM Theorem §C7.1.1]], [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]], [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-4|QM Theorem §C5.3.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

> [!theorem] Theorem §CB.15.7: Every Finite-Dimensional Representation Splits into a Tensor and a Spinor Part
> 1. The representation $(j_+, j_-)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]]) is a tensor representation ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-20|Def. §CB.12.20]]) if $j_+ + j_-$ is an integer and a spinor representation if $j_+ + j_-$ is half an odd integer; the rotation by $2\pi$ about any axis gives the same sign.
> 2. Every finite-dimensional representation $V$ is uniquely $V = V_{\rm t}\oplus V_{\rm s}$, with $V_{\rm t}$ a tensor and $V_{\rm s}$ a spinor representation, both invariant: $V_{\rm t}$, $V_{\rm s}$ are the eigenspaces of $e^{-2\pi iJ_3}$ for $+1$ and $-1$, and $V_{\rm t}$ ($V_{\rm s}$) is the sum of the pieces $(j_+, j_-)$ of $V$ with $j_+ + j_-$ integer (half-integer).
>
> On $SO^+(1,3)$ a tensor representation integrates to a representation, a spinor representation only to a two-valued one ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]], 3; [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-8-6|Def. §CB.8.6]]); both integrate to representations of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|QFT Theorem §C5a.4.8]], 3).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4 (Principle "Spin content, and the sign of a 2π rotation", eq. (twopisign), and the paragraph "Representations with $j_+ + j_-$ an integer return to themselves after a full turn (bosonic), those with $j_+ + j_-$ half-integer change sign (fermionic)") · Yu, opening of Ch. 5 (p. 157) · the decomposition written out here*

^thm-cb-15-7

> [!derivation]- Derivation
> **1. One piece.** On $(j_+, j_-)$ the rotation by $2\pi$ about the axis $\hat{\mathbf n}$ is $e^{-2\pi i\hat{\mathbf n}\cdot\mathbf J} = (-1)^{2(j_+ + j_-)}\mathbb 1$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]], 2), for every unit vector $\hat{\mathbf n}$. $2(j_+ + j_-)$ is an even integer exactly when $j_+ + j_-$ is an integer, and odd exactly when $j_+ + j_-$ is half an odd integer. This is part 1.
>
> **2. Decompose.** By [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]], $V = W_1\oplus\dots\oplus W_r$ with each $W_k$ invariant and equivalent to some $(j_+^{(k)}, j_-^{(k)})$. Put $V_{\rm t} = \bigoplus\{W_k : j_+^{(k)} + j_-^{(k)}\ \text{integer}\}$ and $V_{\rm s} = \bigoplus\{W_k : j_+^{(k)} + j_-^{(k)}\ \text{half-integer}\}$. A sum of invariant subspaces is invariant, so both are invariant, and $V = V_{\rm t}\oplus V_{\rm s}$.
>
> **3. The 2π rotation on each part.** The generators of $V$ are block diagonal in the decomposition of step 2, hence so is $e^{-2\pi iJ_3}$ (powers of a block-diagonal matrix are block diagonal), with blocks $e^{-2\pi iJ_3}|_{W_k} = (-1)^{2(j_+^{(k)} + j_-^{(k)})}\mathbb 1$ by step 1 (an equivalence $W_k \cong (j_+, j_-)$ conjugates $e^{-2\pi iJ_3}$ and leaves $\pm\mathbb 1$ unchanged). So $e^{-2\pi iJ_3} = +\mathbb 1$ on $V_{\rm t}$ and $-\mathbb 1$ on $V_{\rm s}$: $V_{\rm t}$ is a tensor and $V_{\rm s}$ a spinor representation.
>
> **4. Uniqueness.** By step 3, $V_{\rm t} \subseteq E_+ \equiv \ker(e^{-2\pi iJ_3} - \mathbb 1)$ and $V_{\rm s} \subseteq E_- \equiv \ker(e^{-2\pi iJ_3} + \mathbb 1)$; $E_+\cap E_- = 0$ (a vector with $Rv = v = -v$ vanishes), and $\dim V_{\rm t} + \dim V_{\rm s} = \dim V$, so $V_{\rm t} = E_+$ and $V_{\rm s} = E_-$. These kernels are defined by the representation alone, without choosing the $W_k$. Any other splitting into a tensor and a spinor part $V'_{\rm t}\oplus V'_{\rm s}$ has $V'_{\rm t} \subseteq E_+$, $V'_{\rm s} \subseteq E_-$ by definition, hence equals it by the same dimension count.
>
> **What the derivation shows**
> - "Spinor" is a property decided by one group element, the $2\pi$ rotation, which is the identity of $SO^+(1,3)$ but not of its cover $SL(2, \mathbb C)$; a representation can mix both kinds only as a direct sum, never inside one irreducible piece.
> - The Dirac representation $(\frac12, 0)\oplus(0, \frac12)$ is a spinor representation; the four-vector $(\frac12, \frac12)$ and the field strength $(1, 0)\oplus(0, 1)$ are tensor representations ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]; [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).
> - Used next: the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|QFT Theorem §C5a.3.4]]); spin and statistics ([[§C5b.9 Spin and Statistics|§C5b.9]]).

^der-cb-15-7

*Uses:* [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-20|Def. §CB.12.20]]

> [!theorem] Theorem §CB.15.8: Tensor Products Add Each Copy Separately
> If $D$, $D'$ are representations on $V$, $V'$, then $D\otimes D'$ has generators $D(\mathcal J^{\mu\nu})\otimes\mathbb 1 + \mathbb 1\otimes D'(\mathcal J^{\mu\nu})$, so $\mathbf J_\pm^{\rm tot} = \mathbf J_\pm\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J'_\pm$, and
>
> $$
> (j_+, j_-)\otimes(j'_+, j'_-) = \bigoplus_{J_+ = |j_+ - j'_+|}^{j_+ + j'_+}\ \bigoplus_{J_- = |j_- - j'_-|}^{j_- + j'_-}(J_+, J_-) .
> $$
>
> In particular $(\frac12, \frac12)\otimes(\frac12, \frac12) = (1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, $16 = 9 + 3 + 3 + 1$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (Derivation "Products: two-index tensors are (1,1)⊕(1,0)⊕(0,1)⊕(0,0)")*

^thm-cb-15-8

> [!derivation]- Derivation
> **1. Generators of a product.** $(D\otimes D')(\Lambda) = D(\Lambda)\otimes D'(\Lambda)$ is a representation, since $(A\otimes B)(A'\otimes B') = AA'\otimes BB'$. For $\Lambda = e^{s\omega}$, expand both factors to first order and multiply out the four terms:
>
> $$
> \Bigl(\mathbb 1 - \tfrac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})\Bigr)\otimes\Bigl(\mathbb 1 - \tfrac{is}2\omega_{\mu\nu}D'(\mathcal J^{\mu\nu})\Bigr) = \mathbb 1\otimes\mathbb 1 - \tfrac{is}2\omega_{\mu\nu}\bigl(D(\mathcal J^{\mu\nu})\otimes\mathbb 1 + \mathbb 1\otimes D'(\mathcal J^{\mu\nu})\bigr) + O(s^2) ,
> $$
>
> the product of the two first-order terms being $O(s^2)$. By Def. §CB.4.1 the bracket is the generator. $\mathbf J_\pm$ are linear in the generators, so they add in the same way.
>
> **2. Regroup the factors.** On $V\otimes V' = (\mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1})\otimes(\mathbb C^{2j'_++1}\otimes\mathbb C^{2j'_-+1})$ reorder the factors to $(\mathbb C^{2j_++1}\otimes\mathbb C^{2j'_++1})\otimes(\mathbb C^{2j_-+1}\otimes\mathbb C^{2j'_-+1})$ (a fixed basis permutation, an equivalence). Then $\mathbf J_+^{\rm tot} = (\mathbf J^{(j_+)}\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J^{(j'_+)})\otimes\mathbb 1$ acts on the first pair only and $\mathbf J_-^{\rm tot}$ on the second pair only.
>
> **3. Add angular momenta in each copy.** In the first pair, $\mathbf J^{(j_+)}\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J^{(j'_+)}$ is the total angular momentum of two spins; in the coupled basis it is block diagonal with one spin-$J_+$ block for each $J_+$ from $|j_+ - j'_+|$ to $j_+ + j'_+$ ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). The same in the second pair with $J_-$.
>
> **4. Distribute.** $(\bigoplus_{J_+}W_{J_+})\otimes(\bigoplus_{J_-}W_{J_-}) = \bigoplus_{J_+, J_-}W_{J_+}\otimes W_{J_-}$, and on each summand $\mathbf J_+^{\rm tot}$ acts as spin-$J_+$ matrices on the first factor and $\mathbf J_-^{\rm tot}$ as spin-$J_-$ matrices on the second: that summand is $(J_+, J_-)$ (Def. §CB.15.2).
>
> **5. Two vectors.** $j_\pm = j'_\pm = \frac12$: in each copy $\frac12\otimes\frac12 = 0\oplus1$, so the four combinations $(J_+, J_-) \in \{0, 1\}^2$ appear once each, with dimensions $9, 3, 3, 1$.
>
> **What the derivation shows**
> - The two copies never mix: angular momenta are added *separately* in the $+$ and the $-$ copy. Rotations, which see $\mathbf J_+ + \mathbf J_-$, add all four spins at once (Theorem §CB.15.6).
> - Which pieces of a two-index tensor $T^{\mu\nu}$ are which (trace, antisymmetric, symmetric traceless) is [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-7|Theorem §CB.16.7]].

^der-cb-15-8

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]

> [!remark] Remark: Sums versus products
> $(\frac12, 0)\oplus(0, \frac12)$ (dimension $2 + 2$) and $(\frac12, \frac12)$ (dimension $2\times2$) are both four-dimensional and must not be confused. Two tests separate them. The Casimirs: on $(\frac12, \frac12)$, $\mathbf J_+^2 = \mathbf J_-^2 = \frac34$ on every vector (Theorem §C3.2.2); on the sum, $\mathbf J_+^2$ is $\frac34$ on one half and $0$ on the other. The $2\pi$ rotation (Theorem §CB.15.6): $+1$ on $(\frac12, \frac12)$, $-1$ on $(\frac12, 0)\oplus(0, \frac12)$. In a sum no vector feels both copies; in an irreducible $(j_+, j_-)$ with $j_\pm \ne 0$ every vector does. The Dirac spinor is the sum, the four-vector the product ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-10|Theorem §C5a.4.10]] applies both tests to the Dirac matrices).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (paragraph "Sums versus products")*

^rem-cb-15-1

> [!theorem] Theorem §CB.15.9: The Parity Automorphism Exchanges the Two Copies
> 1. The map $\pi$: $\mathbf J \mapsto \mathbf J$, $\mathbf K \mapsto -\mathbf K$ preserves the Lorentz algebra.
> 2. $\pi$ exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$; composed with $\pi$, the representation $(j_+, j_-)$ becomes equivalent to $(j_-, j_+)$.
> 3. If an invertible $Q$ on $V$ satisfies $Q\mathbf JQ^{-1} = \mathbf J$, $Q\mathbf KQ^{-1} = -\mathbf K$, then $(j_+, j_-)$ and $(j_-, j_+)$ occur in $V$ with equal multiplicity.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 (paragraph "Parity and conjugation exchange the two copies") · the parts written out here*

^thm-cb-15-9

> [!derivation]- Derivation
> **1. π preserves the algebra.** Check the three relations of Theorem §CB.4.2 with $\mathbf K$ replaced by $-\mathbf K$: $[J_i, J_j] = i\varepsilon_{ijk}J_k$ does not involve $\mathbf K$; $[J_i, -K_j] = -i\varepsilon_{ijk}K_k = i\varepsilon_{ijk}(-K_k)$; $[-K_i, -K_j] = [K_i, K_j] = -i\varepsilon_{ijk}J_k$. All three hold.
>
> **2. J± are exchanged.** $\pi(\mathbf J_\pm) = \frac12(\mathbf J \pm i(-\mathbf K)) = \frac12(\mathbf J \mp i\mathbf K) = \mathbf J_\mp$.
>
> **3. The labels.** In $(j_+, j_-)$ composed with $\pi$, the new $\mathbf J_+$ is the old $\mathbf J_- = \mathbb 1\otimes\mathbf J^{(j_-)}$ and vice versa. The swap of tensor factors $\mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1} \to \mathbb C^{2j_-+1}\otimes\mathbb C^{2j_++1}$, $a\otimes b \mapsto b\otimes a$, turns this into $\mathbf J^{(j_-)}\otimes\mathbb 1$ and $\mathbb 1\otimes\mathbf J^{(j_+)}$: the representation $(j_-, j_+)$.
>
> **4. Part 3.** From $Q\mathbf JQ^{-1} = \mathbf J$ and $Q\mathbf KQ^{-1} = -\mathbf K$, as in step 2, $Q\mathbf J_\pmQ^{-1} = \mathbf J_\mp$, hence $Q\mathbf J_\pm^2Q^{-1} = \mathbf J_\mp^2$. If $\mathbf J_+^2v = av$ and $\mathbf J_-^2v = bv$, then $\mathbf J_-^2(Qv) = Q\mathbf J_+^2v = a\,Qv$ and $\mathbf J_+^2(Qv) = b\,Qv$. So the invertible $Q$ maps the joint eigenspace for $(a, b)$ into that for $(b, a)$, and $Q^{-1}$ maps back: the two have equal dimension, and by Theorem §CB.15.4, step 9, equal multiplicities.
>
> **What the derivation shows**
> - Statement 1 is the parity of the vector representation read on the algebra; the physical reading — parity on four-vectors and on the indices of fields, and why a parity-invariant theory carries both copies — is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]] (physics; steps 2 and the consequences of the original derivation are kept there).

^der-cb-15-9

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-2|Theorem §CB.4.2]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]]

> [!theorem] Theorem §CB.15.10: Complex Conjugation Exchanges the Two Copies
> If $D$ is a representation, so is its complex conjugate $\bar D(\Lambda) = D(\Lambda)^*$, with generators $\bar D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\mu\nu})^*$. The conjugate of $(j_+, j_-)$ is equivalent to $(j_-, j_+)$; for spin $j$ the equivalence is $-\mathbf J^{(j)*} = R\,\mathbf J^{(j)}R^{-1}$ with $R = e^{-i\pi J^{(j)}_2}$, the rotation by $\pi$ about the $2$-axis.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 ("Complex conjugation turns θ − iη into θ + iη and does the same exchange") · the derivation written out here*

^thm-cb-15-10

> [!derivation]- Derivation
> **1. The conjugate is a representation.** Entrywise conjugation respects products, $(AB)^{\ast} = A^{\ast}B^{\ast}$, so $D(\Lambda_1)^{\ast}D(\Lambda_2)^{\ast} = D(\Lambda_1\Lambda_2)^{\ast}$.
>
> **2. Its generators.** The parameters $\omega$ are real, so conjugating $D(e^{s\omega}) = \mathbb 1 - \frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}) + O(s^2)$ gives $\mathbb 1 + \frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})^{\ast} + O(s^2) = \mathbb 1 - \frac{is}2\omega_{\mu\nu}\bigl(-D(\mathcal J^{\mu\nu})^{\ast}\bigr) + O(s^2)$. So $\bar{\mathbf J} = -\mathbf J^{\ast}$, $\bar{\mathbf K} = -\mathbf K^{\ast}$.
>
> **3. The copies are exchanged.** $\bar{\mathbf J}_\pm = \frac12(\bar{\mathbf J} \pm i\bar{\mathbf K}) = -\frac12(\mathbf J^{\ast} \pm i\mathbf K^{\ast}) = -\bigl(\frac12(\mathbf J \mp i\mathbf K)\bigr)^{\ast} = -(\mathbf J_\mp)^{\ast}$, using $(\mp i\mathbf K)^{\ast} = \pm i\mathbf K^{\ast}$.
>
> **4. On (j₊, j₋).** $\bar{\mathbf J}_+ = -(\mathbb 1\otimes\mathbf J^{(j_-)})^{\ast} = \mathbb 1\otimes(-\mathbf J^{(j_-)\ast})$ and $\bar{\mathbf J}_- = (-\mathbf J^{(j_+)\ast})\otimes\mathbb 1$.
>
> **5. −J* is equivalent to J.** In the standard basis $J^{(j)}_1$, $J^{(j)}_3$ are real and $J^{(j)}_2$ is imaginary (Def. §CB.15.2, text), so $-\mathbf J^{(j)\ast} = (-J_1, J_2, -J_3)$. Angular momentum is a vector operator, $D(R)^\dagger J_iD(R) = R_{ik}J_k$ ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-5|QM Theorem §C5.1.5]]); for the rotation by $\pi$ about the $2$-axis, $R = \operatorname{diag}(-1, 1, -1) = R^{-1}$, and $D = e^{-i\pi J_2}$ gives $e^{-i\pi J_2}J_ie^{i\pi J_2} = (R^{-1})_{ik}J_k$, i.e. $(-J_1, J_2, -J_3)$. So $-\mathbf J^{(j)\ast} = e^{-i\pi J_2}\mathbf J^{(j)}e^{i\pi J_2}$.
>
> **6. Assemble.** Conjugating step 4 by $e^{-i\pi J^{(j_+)}_2}\otimes e^{-i\pi J^{(j_-)}_2}$ turns it into $\bar{\mathbf J}_+ = \mathbb 1\otimes\mathbf J^{(j_-)}$, $\bar{\mathbf J}_- = \mathbf J^{(j_+)}\otimes\mathbb 1$; the swap of the two factors (as in Theorem §CB.15.9, step 3) gives $(j_-, j_+)$. ⚑ By-product: for $j = \frac12$, $e^{-i\pi\sigma_2/2} = -i\sigma_2$, so $\sigma_2\psi^{\ast}$ transforms like the other Weyl spinor: Peskin–Schroeder's $\sigma^2\psi_L^{\ast}$ (eq. (3.38); [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]; QFT C9, planned).
>
> **What the derivation shows**
> - In the factorization of Theorem §CB.4.8, conjugation turns the angle $\boldsymbol\theta - i\boldsymbol\eta$ into $\boldsymbol\theta + i\boldsymbol\eta$: it exchanges the copies because the two angles are conjugates.
> - The operator $e^{-i\pi J_2}$ is the one that, followed by complex conjugation, is time reversal in Quantum Mechanics ([[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]]): both use that only $J_2$ is imaginary in the standard basis.
> - A real field (a real four-vector, a real $F^{\mu\nu}$) must contain, with $(j_+, j_-)$, also $(j_-, j_+)$ or be of the form $(j, j)$.

^der-cb-15-10

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-1|Def. §CB.4.1]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-5|QM Theorem §C5.1.5]]

> [!remark] Remark: What the labels (j₊, j₋) mean
> Each statement below is proved in this section; together they say why "$(\frac12, 0)$" and "$(0, \frac12)$" are meaningful names.
> - **Two angular momenta.** The complexified Lorentz algebra is two commuting copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$, spanned by $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-7|Theorem §CB.4.7]]; [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]); the real algebra is not split ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-10|Theorem §CB.4.10]]). A finite-dimensional representation chooses a spin for each copy; $(j_+, j_-)$ records the two choices, read off from the Casimirs $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]]), and the dimension is $(2j_+ + 1)(2j_- + 1)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]]).
> - **Rotations see the sum.** Adding and subtracting the definitions of $\mathbf J_\pm$ gives $\mathbf J = \mathbf J_+ + \mathbf J_-$ and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$. So under rotations $(j_+, j_-)$ is the addition of two angular momenta, with spins $|j_+ - j_-|, \dots, j_+ + j_-$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]]): $(\frac12, 0)$ and $(0, \frac12)$ are both spin $\frac12$, $(\frac12, \frac12)$ is $0\oplus1$, the four-vector ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]). Neither label alone is the spin ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-2|Remark: Neither label is the spin]]).
> - **Boosts see the difference.** $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ is $-\frac i2\boldsymbol\sigma$ on $(\frac12, 0)$ and $+\frac i2\boldsymbol\sigma$ on $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]; the sign convention $K_i = \mathcal J^{0i}$: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|Caution: Which one is (½, 0) depends on the sign of K]]). Same rotations, opposite boosts: that is the whole difference between left- and right-handed.
> - **The 2π rotation sees the parity of 2(j₊ + j₋).** It is $(-1)^{2(j_+ + j_-)}$, which sorts every representation into tensor and spinor parts ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-7|Theorem §CB.15.7]]); $(\frac12, 0)$ and $(0, \frac12)$ are the smallest spinor representations.
> - **Parity and conjugation swap the copies.** Parity keeps $\mathbf J$ and reverses $\mathbf K$, so it exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$ and $(j_+, j_-) \leftrightarrow (j_-, j_+)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-9|Theorem §CB.15.9]]); complex conjugation does the same ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-10|Theorem §CB.15.10]]). A spinor field on which parity acts must therefore contain $(\frac12, 0)$ and $(0, \frac12)$ together: the Dirac field is $(\frac12, 0)\oplus(0, \frac12)$ (the user's PHY 513 notes, Ch. 7 §7.4.6, paragraph "Parity and conjugation exchange the two copies"; how parity acts on Dirac fields is QFT C9, planned).
>
> *Source: PS §3.1–§3.2, pp. 38–44 · the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "What a label (j₊, j₋) means, worked out"; §7.4.4; §7.4.6) · PHY 513 Lecture 7, Parts B–C · Yu §3.2 · the summary written here*

^rem-cb-15-2

## Not unitary

> [!theorem] Theorem §CB.15.11: No Finite-Dimensional Representation Is Unitary
> 1. In an inner product with $\mathbf J_\pm$ Hermitian (Theorem §CB.15.4), $\mathbf J$ is Hermitian and $\mathbf K$ anti-Hermitian; a boost $D = e^{-i\boldsymbol\eta\cdot\mathbf K} = e^{-\boldsymbol\eta\cdot(\mathbf J_+ - \mathbf J_-)}$ is Hermitian and positive, and unitary only if $\boldsymbol\eta\cdot\mathbf K = 0$.
> 2. If a finite-dimensional representation of $SO^+(1,3)$ is unitary for some inner product, it is trivial: $D(\Lambda) = \mathbb 1$ for every $\Lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Principle "Hermitian generators do not make boosts unitary", citing Weinberg vol. 1 ch. 2 for the general theorem), §7.4.6 ("$\vec J$ can be taken Hermitian and $\vec K$ is then anti-Hermitian") · the proof for the Lorentz group written out here*

^thm-cb-15-11

> [!derivation]- Derivation
> **1. Part 1, Hermiticity.** $\mathbf J = \mathbf J_+ + \mathbf J_-$ is a sum of Hermitian matrices. $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ and $(-iX)^\dagger = iX^\dagger = iX$ for Hermitian $X$, so $\mathbf K^\dagger = -\mathbf K$.
>
> **2. Part 1, the boost.** $-i\boldsymbol\eta\cdot\mathbf K = -i\boldsymbol\eta\cdot(-i)(\mathbf J_+ - \mathbf J_-) = -\boldsymbol\eta\cdot(\mathbf J_+ - \mathbf J_-) \equiv -H$ with $H$ Hermitian. In an eigenbasis of $H$ (real eigenvalues $h_k$), $e^{-H} = \operatorname{diag}(e^{-h_k})$: Hermitian with positive eigenvalues. It is unitary only if every $|e^{-h_k}| = 1$, i.e. every $h_k = 0$, i.e. $H = 0$.
>
> **3. Part 2: unitary means Hermitian generators.** Suppose $\langle\cdot, \cdot\rangle$ makes every $D(\Lambda)$ unitary. For each generator $X$, $t \mapsto D(e^{t\omega}) = e^{-itX}$ (with $\omega$ the corresponding parameter) is unitary for all real $t$; differentiating $\langle e^{-itX}v, e^{-itX}w\rangle = \langle v, w\rangle$ at $t = 0$ gives $X^\dagger = X$. In particular $K_3$ is Hermitian, so its eigenvalues are real.
>
> **4. Part 2: the eigenvalues of K₃ are imaginary.** By Theorem §CB.15.4, $V$ is a sum of pieces $(j_+, j_-)$; on each, $K_3 = -i(J^{(j_+)}_3\otimes\mathbb 1 - \mathbb 1\otimes J^{(j_-)}_3)$ is diagonal on $|m_+\rangle\otimes|m_-\rangle$ with eigenvalue $-i(m_+ - m_-)$. Eigenvalues do not depend on the inner product or basis. Being both real (step 3) and imaginary, all are $0$; the pair $m_+ = j_+$, $m_- = -j_-$ then gives $j_+ + j_- = 0$, so every piece is $(0, 0)$.
>
> **5. Part 2: trivial.** On $(0, 0)$ all generators vanish, so $D(e^\omega) = e^0 = \mathbb 1$ for every $\omega$. Every element of $SO^+(1,3)$ is a product of exponentials (a boost times a rotation, [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], each an exponential by [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]), so $D(\Lambda) = \mathbb 1$.
>
> **What the derivation shows**
> - The finite-dimensional representations, which act on the indices of fields, are never unitary (except the trivial one). Unitarity is required of the operators on quantum states, which therefore must be infinite-dimensional: the one-particle spaces of [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], with $U(\Lambda)$ of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]] ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]).
> - Rotations are unitary in these inner products ($\mathbf J$ Hermitian); boosts are not. This is the precise form of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]], proved here for the Lorentz group without the general theorem on noncompact groups.
> - Used next: the spinor conjugate $\bar\psi$, which exists because $\psi^\dagger$ does not transform with $D^{-1}$ ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).

^der-cb-15-11

*Uses:* [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

## Descent to SO⁺(1,3)

> [!theorem] Theorem §CB.15.12: Which (j₊, j₋) Descend to SO⁺(1,3)
> $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2(j_+ + j_-)}\mathbb 1$. Hence $D^{(j_+, j_-)}$ is tensorial ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]]), i.e. a representation of $SO^+(1,3)$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-11|Theorem §CB.8.11]]), iff $j_+ + j_- \in \mathbb Z$, and spinorial iff $j_+ + j_- \in \frac12 + \mathbb Z$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 6 · written here*

^thm-cb-15-12

> [!proof]- Proof
> **1. The value on −1.** $\operatorname{Sym}^{2j}(-\mathbb 1)$ is $(-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$ restricted to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]]), and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. So $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2j_+}\mathbb 1\otimes(-1)^{2j_-}\mathbb 1 = (-1)^{2(j_+ + j_-)}\mathbb 1$.
>
> **2. Tensorial or spinorial.** Under $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ the element $-1$ goes to $-\mathbb 1$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], 1, for either identification $\phi$ or $\theta\circ\phi$). $2(j_+ + j_-)$ is an integer; $(-1)^{2(j_+ + j_-)} = 1$ iff it is even, i.e. $j_+ + j_- \in \mathbb Z$ (tensorial, [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]]), and $= -1$ iff $j_+ + j_- \in \frac12 + \mathbb Z$ (spinorial).
>
> **3. Descent.** $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ is a surjective covering homomorphism with kernel $\{\pm\mathbb 1\}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), as is $\rho$ on $\mathrm{Spin}(1,3)_0$ (Theorem §CB.14.4, 2). By the descent lemma ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-11|Theorem §CB.8.11]]) $D^{(j_+, j_-)}$ is $D\circ\pi$ for a representation $D$ of $SO^+(1,3)$ iff $D^{(j_+, j_-)}(-\mathbb 1) = \mathbb 1$, i.e. iff $j_+ + j_- \in \mathbb Z$, and then $D$ is irreducible.
>
> **What the proof shows**
> - The sign is the parity of the total number $2j_+ + 2j_-$ of spinor slots, each slot contributing one factor $-1$.

^pf-cb-15-12

*Uses:* [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-11|Theorem §CB.8.11]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]

The course's descent theorem, proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8]]

> [!remark]- Connections
> - The conjugation that exchanges the two $\mathfrak{sl}(2, \mathbb C)$ summands ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], 3) is, on the group, $\lambda \mapsto (\lambda^\dagger)^{-1}$, the same map that relates the two factors of $D^{(j_+, j_-)}$ and the two Weyl matrices $\Lambda_L$, $\Lambda_R$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]).
> - **Used in**: Theorems §CB.15.1–§CB.15.5 — [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-15-2|Def. §CB.15.2]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-8|Theorem §CB.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.15.12 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-6|Theorem §CB.15.6]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-7|Theorem §CB.15.7]].
