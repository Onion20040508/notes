---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.16
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵]] →

*Sources: the user's PHY 513 notes, Ch. 7 §7.4 (the (j₊, j₋) classification) · PHY 513 Lecture 7 (Larsen), Part C · Peskin & Schroeder, §3.1, pp. 38–41 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it; submitted) · Yu Zhao-Huan, 量子场论讲义, §3.2, §4.1, Exercise 3.1 and opening of Ch. 5 · P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here.*

What are the finite-dimensional representations of $SL(2, \mathbb C)$, and which of them are representations of the Lorentz group? With the spin group of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]] and the split $\mathbf J_\pm$ of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra|§CB.5]], this section identifies the finite-dimensional representations of $SL(2, \mathbb C)$ with pairs of commuting $\mathfrak{sl}(2, \mathbb C)$-representations, lists the irreducible ones as the $(j_+, j_-)$, and decides which of them descend to $SO^+(1,3)$. It uses spin $j$ from [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.9]] and the descent criterion of [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]]. The course's labels ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]) and their properties — rotation content, the sign of a $2\pi$ rotation, the tensor/spinor split, products, parity, complex conjugation and non-unitarity — are stated here; the course's integration and descent theorem ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]), with the explicit polynomial model, follows the rotation content.

*Conventions* (the course's, [[Larsen PHY 513]]): $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$, $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]]). From Definition §CB.16.2 on, the boxes are stated for representations of the Lorentz algebra $\mathfrak{so}(1,3)$ on a complex space $V$; by Theorem §CB.16.1 these are the same as the representations of $SL(2, \mathbb C)$.

## The finite-dimensional representations of SL(2,ℂ)

> [!theorem] Theorem §CB.16.1: Representations of SL(2,ℂ) Are Pairs of 𝔰𝔩(2,ℂ)-Representations
> For finite-dimensional representations on complex spaces, the following correspond bijectively, preserving invariant subspaces, irreducibility and intertwiners: continuous representations of $SL(2, \mathbb C)$; representations of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-21|Theorem §CB.2.21]], $SL(2, \mathbb C)$ being simply connected, [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]]); commuting pairs $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-2|Theorem §CB.15.2]]); complex-linear representations of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]]). All of them are completely reducible ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]).
>
> *Source: written here (assembly of the cited theorems)*

^thm-cb-16-1

> [!proof]- Proof
> **1. Group to algebra.** A continuous representation $D : SL(2, \mathbb C) \to GL(W)$ is a Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]); its differential $d = D_\ast$ is a representation of the Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^def-cb-5-7|Def. §CB.5.7]]).
>
> **2. Algebra to group, bijectively.** $SL(2, \mathbb C)$ is connected and simply connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]]), so every representation $d$ of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ is $D_\ast$ for exactly one $D$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-21|Theorem §CB.2.21]]). Two representations with the same differential are equal ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]]). So $D \mapsto D_\ast$ is a bijection.
>
> **3. Intertwiners agree.** Let $T : W_1 \to W_2$ be linear. If $TD_1(g) = D_2(g)T$ for all $g$, then differentiating $TD_1(e^{sX}) = D_2(e^{sX})T$ at $s = 0$ gives $Td_1(X) = d_2(X)T$ (Theorem §CB.2.3). Conversely, if $Td_1(X) = d_2(X)T$, then $Td_1(X)^n = d_2(X)^nT$ for all $n$, and summing the series $TD_1(e^X) = Te^{d_1(X)} = e^{d_2(X)}T = D_2(e^X)T$; every $g$ is a product of exponentials ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 3), so $TD_1(g) = D_2(g)T$. In particular $D_1 \cong D_2$ iff $d_1 \cong d_2$ (invertible intertwiners, [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]]).
>
> **4. Invariant subspaces agree.** If $W' \subset W$ is invariant under all $D(g)$, then $d(X)w = \lim_{s\to0}\frac1s(D(e^{sX})w - w) \in W'$ for $w \in W'$ ($W'$ is closed, being finite-dimensional). If $W'$ is invariant under all $d(X)$, it is invariant under every power and hence under $e^{d(X)} = D(e^X)$, and so under all products of exponentials, i.e. all of $SL(2, \mathbb C)$ (Theorem §CB.2.10, 3). Hence irreducibility agrees too.
>
> **5. The other two descriptions.** A representation of the real algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on the complex space $W$ is the same as a commuting pair $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-2|Theorem §CB.15.2]]), and the same as a complex-linear representation of its complexification ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], 1), with the same invariant subspaces and intertwiners (Theorem §CB.3.9, 2). The complexification is isomorphic to $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]]), and pulling back along an isomorphism of Lie algebras changes neither invariant subspaces nor intertwiners. The isomorphism $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ is [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]].
>
> **6. Complete reducibility.** Every finite-dimensional representation of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on a complex space is completely reducible ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]); by step 4 the same decomposition into invariant subspaces works for the group.
>
> **What the proof shows**
> - Simple connectivity of $SL(2, \mathbb C)$ is what makes every algebra representation a group representation; for $SO^+(1,3)$ only those with $D(-\mathbb 1) = \mathbb 1$ survive (Theorem §CB.16.15).
> - Continuity is the only regularity assumed on the group side: differentiability comes from the matrix Lie group theory of §CB.1–§CB.2.

^pf-cb-16-1

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-21|Theorem §CB.2.21]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-2|Theorem §CB.15.2]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-2|Def. §CB.6.2]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-21|Theorem §CB.6.21]]

The course's representations $(j_+, j_-)$ and their irreducibility, and the classification (PHY 513 Lecture 7, Part C; Problem Set 5, Problem 1):

> [!definition] Definition §CB.16.2: The Representation (j₊, j₋)
> For $j_+, j_- \in \{0, \frac12, 1, \frac32, \dots\}$ let $\mathbf J^{(j)}$ be the spin-$j$ matrices on $\mathbb C^{2j+1}$ (the matrices of $D^{(j)}$ in the standard basis of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], 3) (with $\mathbf J^{(0)} = 0$ on $\mathbb C$). The representation $(j_+, j_-)$ of the Lorentz algebra is the space $V = \mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1}$ with
>
> $$
> \mathbf J_+ = \mathbf J^{(j_+)}\otimes\mathbb 1, \qquad \mathbf J_- = \mathbb 1\otimes\mathbf J^{(j_-)}, \qquad\text{i.e.}\qquad \mathbf J = \mathbf J^{(j_+)}\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J^{(j_-)}, \quad \mathbf K = -i\bigl(\mathbf J^{(j_+)}\otimes\mathbb 1 - \mathbb 1\otimes\mathbf J^{(j_-)}\bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 (Definition "The representation (j₊, j₋)") · PHY 513, Problem Set 5, Problem 1(b) (statement) · PHY 513 Lecture 7, Part C (HW5 clue)*

^def-cb-16-2

The value of the Lorentz Casimir operator of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] on $(j_+, j_-)$ (the $\mathfrak{so}(1,3)$ example stated there; moved here in the CB ordering pass because it needs the definition above):

> [!theorem] Theorem §CB.16.3: The Lorentz Casimir on (j₊, j₋)
> For $\mathfrak{so}(1,3)$ with the invariant form $B(X, Y) = -\frac12\operatorname{tr}(XY)$ on $4\times4$ matrices, the Casimir operator of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] is $C_d = \mathbf K^2 - \mathbf J^2 = -2(\mathbf J_+^2 + \mathbf J_-^2)$, so $C_d = -2\bigl(j_+(j_+ + 1) + j_-(j_- + 1)\bigr)\mathbb 1$ on $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]; [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]]).
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §18.3 · normalization computed in Theorem §CB.6.15, Step 6 (batch 2) · moved from the Examples of Theorem §CB.6.15 (CB ordering pass, 2026-10-08)*

^thm-cb-16-3

> [!proof]- Proof
> Step 6 of the proof of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]] gives $C_d = -\mathbf J^2 + \mathbf K^2 = -2(\mathbf J_+^2 + \mathbf J_-^2)$, and on $(j_+, j_-)$, where $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]]; [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]), $C_d = -2\bigl(j_+(j_+ + 1) + j_-(j_- + 1)\bigr)\mathbb 1$.

^pf-cb-16-3

*Uses:* [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]

The spin-$j$ matrices are those of Quantum Mechanics in the basis $|j, m\rangle$, $m = j, \dots, -j$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-7|QM Theorem §B6.1.7]] with $\hbar = 1$): $J^{(j)}_3$ diagonal with entries $m$, $J^{(j)}_\pm$ with the real ladder coefficients, so $J^{(j)}_1$ and $J^{(j)}_3$ are real and $J^{(j)}_2$ is imaginary; for $j = \frac12$, $\mathbf J^{(1/2)} = \frac12\boldsymbol\sigma$. The pre-course notes and Weinberg write the labels as $(A, B)$. Each label is a spin chosen for one copy of the rotation algebra; it is not the spin of the field ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-2|Remark: Neither label is the spin]]).

> [!theorem] Theorem §CB.16.4: (j₊, j₋) Is Irreducible
> $(j_+, j_-)$ is a representation of the Lorentz algebra of dimension $(2j_+ + 1)(2j_- + 1)$. It is irreducible, its Casimir operators are the numbers
>
> $$
> \mathbf J_+^2 = j_+(j_+ + 1)\,\mathbb 1, \qquad \mathbf J_-^2 = j_-(j_- + 1)\,\mathbb 1 ,
> $$
>
> and different labels give inequivalent representations.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 (Definition "The representation (j₊, j₋)": "It is irreducible: every vector feels both copies") · PHY 513, Problem Set 5, Problem 1(b) (dimension; statement) · the irreducibility argument written out here*

^thm-cb-16-4

> [!derivation]- Derivation
> **1. It is a representation.** For the $+$ copy, $[J^{(j_+)}_i\otimes\mathbb 1, J^{(j_+)}_j\otimes\mathbb 1] = [J^{(j_+)}_i, J^{(j_+)}_j]\otimes\mathbb 1 = i\varepsilon_{ijk}J^{(j_+)}_k\otimes\mathbb 1$, because the spin-$j$ matrices obey the rotation algebra ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]); the same for the $-$ copy. Across copies, $(A\otimes\mathbb 1)(\mathbb 1\otimes B) = A\otimes B = (\mathbb 1\otimes B)(A\otimes\mathbb 1)$, so $[J_{+i}, J_{-j}] = 0$. By Theorem §CB.5.2, 2, the formulas of Def. §CB.16.2 represent the Lorentz algebra.
>
> **2. Dimension.** $\dim(\mathbb C^{a}\otimes\mathbb C^{b}) = ab$, here $(2j_+ + 1)(2j_- + 1)$.
>
> **3. Casimirs.** $\mathbf J_+^2 = (\mathbf J^{(j_+)})^2\otimes\mathbb 1 = j_+(j_+ + 1)\,\mathbb 1$ by the spectrum of angular momentum on a multiplet ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]); likewise $\mathbf J_-^2$.
>
> **4. A nonzero invariant subspace contains a basis vector.** Let $W \ne \{0\}$ be invariant under all six generators, hence under $J_{\pm3}$ and the ladder operators $J_{\pm,\uparrow} \equiv J_{\pm1} + iJ_{\pm2}$, $J_{\pm,\downarrow} \equiv J_{\pm1} - iJ_{\pm2}$ (linear combinations). The vectors $|m_+\rangle\otimes|m_-\rangle$ form a basis of common eigenvectors of $J_{+3}$ and $J_{-3}$ with eigenvalue pairs $(m_+, m_-)$, each pair occurring once. Take $0 \ne w = \sum c_{m_+m_-}|m_+\rangle\otimes|m_-\rangle \in W$ and a pair $(a, b)$ with $c_{ab} \ne 0$. The polynomial $P = \prod_{m_+ \ne a}(J_{+3} - m_+)\prod_{m_- \ne b}(J_{-3} - m_-)$ in the generators maps $W$ into $W$ and kills every basis vector except $|a\rangle\otimes|b\rangle$, which it multiplies by $\prod_{m_+ \ne a}(a - m_+)\prod_{m_- \ne b}(b - m_-) \ne 0$. So $|a\rangle\otimes|b\rangle \in W$.
>
> **5. The ladders reach every basis vector.** $J_{+,\uparrow}(|m\rangle\otimes|b\rangle) = \sqrt{(j_+ - m)(j_+ + m + 1)}\,|m + 1\rangle\otimes|b\rangle$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]), nonzero for $m < j_+$; $J_{+,\downarrow}(|m\rangle\otimes|b\rangle) = \sqrt{(j_+ + m)(j_+ - m + 1)}\,|m - 1\rangle\otimes|b\rangle$, nonzero for $m > -j_+$; and $J_{-,\uparrow}$, $J_{-,\downarrow}$ act by the same formulas on the second factor, with $j_-$ in place of $j_+$, leaving the first factor alone. Starting from $|a\rangle\otimes|b\rangle$ and stepping in each factor reaches every $|m_+\rangle\otimes|m_-\rangle$ with a nonzero coefficient, so all basis vectors lie in $W$: $W = V$. ⚑ By-product: the precise meaning of "every vector feels both copies": no subspace is closed under one copy's ladders without being closed under the other's.
>
> **6. Inequivalence.** If $D'(X) = UD(X)U^{-1}$ for all generators, then $\mathbf J_\pm'^2 = U\mathbf J_\pm^2U^{-1}$; on $(j_+, j_-)$ these are the numbers $j_\pm(j_\pm + 1)$, which conjugation does not change. Since $j \mapsto j(j+1)$ is injective for $j \ge 0$, equivalent representations have equal labels.
>
> **What the derivation shows**
> - Irreducibility rests only on the nonzero ladder coefficients of each spin-$j$ multiplet: the same reason that a single multiplet is irreducible under rotations ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-1|QM Theorem §C5.3.1]]).
> - The pair of Casimir values is a complete invariant of an irreducible finite-dimensional representation (with Theorem §CB.16.5).
> - Used next: the classification (Theorem §CB.16.5) and every identification of a field's representation by its Casimirs (Theorem §C3.2.2; [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]).

^der-cb-16-4

*Uses:* [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]

> [!theorem] Theorem §CB.16.5: Every Finite-Dimensional Representation Is a Sum of (j₊, j₋)
> Every representation of the Lorentz algebra on a finite-dimensional complex space $V$ is a direct sum of representations $(j_+, j_-)$. The multiplicity of each $(j_+, j_-)$ is fixed by the representation, and $V$ carries an inner product in which all $J_{\pm i}$ are Hermitian.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3 ("Every finite-dimensional representation is a direct sum of these"; stated there) · PHY 513, Problem Set 5, Problem 1(b) ("the finite dimensional representations of the Lorentz algebra are therefore labelled by a pair (j₊, j₋)"; statement) · the derivation (Weyl's unitarian trick) written out here, with the two inputs from Lie theory quoted*

^thm-cb-16-5

> [!derivation]- Derivation
> **1. Two commuting angular momenta.** By Theorem §CB.5.2, $V$ carries two commuting triples $J_{+i}$, $J_{-i}$, each obeying the rotation algebra.
>
> **2. A compact group behind them.** The six matrices $-iJ_{+i}$, $-iJ_{-i}$ span, with real coefficients, a real Lie algebra with brackets $[-iJ_{\pm i}, -iJ_{\pm j}] = -[J_{\pm i}, J_{\pm j}] = \varepsilon_{ijk}(-iJ_{\pm k})$ and $[-iJ_{+i}, -iJ_{-j}] = 0$: two commuting copies of the Lie algebra of $SU(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]). Input from Lie theory, quoted: because $SU(2)\times SU(2)$ is simply connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]] for each factor), this algebra representation is the derivative of a representation $R$ of the group $G = SU(2)\times SU(2)$ on $V$, with $R(e^{-i\boldsymbol\alpha\cdot\boldsymbol\tau}, e^{-i\boldsymbol\beta\cdot\boldsymbol\tau}) = e^{-i\boldsymbol\alpha\cdot\mathbf J_+ - i\boldsymbol\beta\cdot\mathbf J_-}$, $\boldsymbol\tau = \boldsymbol\sigma/2$.
>
> **3. An invariant inner product.** $G$ is compact. It carries a probability measure $dg$ invariant under translations, $\int f(gh)\,dg = \int f(g)\,dg$ for every $h \in G$: the product of the invariant integral on each $SU(2) = S^3$ constructed in [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^der-cb-6-16|Derivation §CB.6.16]], step 1. Starting from any inner product $(\cdot, \cdot)$ on $V$, define $\langle v, w\rangle = \int(R(g)v, R(g)w)\,dg$. It is positive definite (an average of positive numbers, continuous in $g$) and invariant: $\langle R(h)v, R(h)w\rangle = \int(R(gh)v, R(gh)w)\,dg = \langle v, w\rangle$, using $R(g)R(h) = R(gh)$ and the invariance of $dg$. So every $R(g)$ is unitary for $\langle\cdot, \cdot\rangle$: the argument of [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-16|Theorem §CB.6.16]], run on $SU(2)\times SU(2)$.
>
> **4. The generators are Hermitian.** For each $i$, $t \mapsto e^{-itJ_{+i}} = R(e^{-it\tau_i}, \mathbb 1)$ is unitary for every real $t$. Differentiating $\langle e^{-itJ_{+i}}v, e^{-itJ_{+i}}w\rangle = \langle v, w\rangle$ at $t = 0$ gives $\langle -iJ_{+i}v, w\rangle + \langle v, -iJ_{+i}w\rangle = 0$, i.e. $J_{+i}^\dagger = J_{+i}$. Likewise $J_{-i}^\dagger = J_{-i}$.
>
> **5. Complete reducibility.** Let $W \subset V$ be invariant under all $J_{\pm i}$, and $W^\perp$ its orthogonal complement for $\langle\cdot, \cdot\rangle$. For $u \in W^\perp$, $w \in W$: $\langle J_{\pm i}u, w\rangle = \langle u, J_{\pm i}w\rangle = 0$ (Hermiticity, then $J_{\pm i}w \in W$). So $W^\perp$ is invariant and $V = W\oplus W^\perp$. Repeating inside $W$ and $W^\perp$ (the dimension drops each time) writes $V$ as a direct sum of irreducible invariant subspaces.
>
> **6. One irreducible piece.** Let $U \subset V$ be irreducible. $\mathbf J_+^2$ commutes with all $J_{+i}$ (the angular-momentum Casimir, [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]) and with all $J_{-i}$ (different copies commute), and it is Hermitian; its eigenspaces in $U$ are therefore invariant, and irreducibility leaves one eigenvalue (as in [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-13|Theorem §CB.6.13]]): $\mathbf J_+^2 = j_+(j_+ + 1)$ on $U$, and likewise $\mathbf J_-^2 = j_-(j_- + 1)$, by the angular-momentum spectrum for Hermitian generators.
>
> **7. Highest weights of the + copy.** Let $H = \{u \in U : J_{+3}u = j_+u\}$. By the ladder theory of one angular momentum ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], with complete reducibility under the $+$ copy from step 5 applied to that copy alone), $U$ decomposes under the $+$ copy alone into spin-$j_+$ multiplets, each containing exactly one direction in $H$ (its top vector, killed by $J_{+,\uparrow}$); so $\dim U = (2j_+ + 1)\dim H$. Since the $J_{-i}$ commute with $J_{+3}$, they map $H$ into itself: $H$ carries a representation of the $-$ copy.
>
> **8. The isomorphism.** Define $\Phi: \mathbb C^{2j_++1}\otimes H \to U$ by $\Phi(|m\rangle\otimes h) =$ the vector of the $+$ multiplet through $h$ with $J_{+3} = m$, obtained from $h$ by $J_{+,\downarrow}^{\,j_+ - m}$ and normalized with the ladder coefficients. $\Phi$ is onto (every multiplet has its top in $H$) and between spaces of equal dimension (step 7), hence bijective; it turns $\mathbf J^{(j_+)}\otimes\mathbb 1$ into $\mathbf J_+$ (the multiplet's standard matrices) and $\mathbb 1\otimes\mathbf J_-|_H$ into $\mathbf J_-$ (which commutes with the $+$ ladders). If $H$ had a proper invariant subspace $H'$ under the $-$ copy, $\Phi(\mathbb C^{2j_++1}\otimes H')$ would be a proper invariant subspace of $U$; so $H$ is irreducible under one angular momentum with Casimir $j_-(j_- + 1)$, i.e. a single spin-$j_-$ multiplet. Hence $U \cong (j_+, j_-)$.
>
> **9. Multiplicities.** The joint eigenspace of the commuting Hermitian operators $\mathbf J_+^2$, $\mathbf J_-^2$ with eigenvalues $j_\pm(j_\pm + 1)$ is the sum of the pieces labelled $(j_+, j_-)$; its dimension, divided by $(2j_+ + 1)(2j_- + 1)$, is the multiplicity, and it depends only on the operators, not on the chosen decomposition.
>
> **What the derivation shows**
> - One input was quoted, not derived: that a representation of the Lie algebra $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ integrates to the simply connected group $SU(2)\times SU(2)$. Everything else is the invariant integral and the ladder theory of §C3.1 and Quantum Mechanics.
> - The Hermitian inner product of step 4 makes $\mathbf J_\pm$ Hermitian, hence $\mathbf J$ Hermitian and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ anti-Hermitian: the non-unitarity of boosts is built in → [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]].
> - The compact group used is not the Lorentz group: $SU(2)\times SU(2)$ is reached by real combinations of $-i\mathbf J_\pm$, which mix $\mathbf J$ with $i\mathbf K$ ("Weyl's unitarian trick"). Only the algebra is shared.
> - Used next: Theorems §C3.2.2, §CB.16.14, and every "which representation is this field" question in [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]].

^der-cb-16-5

*Uses:* [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-13|Theorem §CB.6.13]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-16|Theorem §CB.6.16]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]; quoted: integration of Lie-algebra representations to simply connected groups

The first instance of the classification, by the Casimirs alone (first written in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]], restated here with its derivation in the CB ordering pass, 2026-10-08):

> [!theorem] Theorem §CB.16.6: The Vector Representation Is (½, ½)
> For the $4\times4$ generators $\mathcal J^{\mu\nu}$ of the vector representation ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]]) $J_i$, $K_i$ of [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]] and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]]), in the basis $(v^0, v^1, v^2, v^3)$,
>
> $$
> (J_i)^l{}_m = -i\varepsilon_{ilm}, \quad \mathbf J^2 = \operatorname{diag}(0, 2, 2, 2), \quad \mathbf K^2 = -\operatorname{diag}(3, 1, 1, 1), \quad \mathbf J\cdot\mathbf K = \mathbf K\cdot\mathbf J = 0, \quad \mathbf J_+^2 = \mathbf J_-^2 = \tfrac34\,\mathbb 1 ,
> $$
>
> ($J_i$ acting only on the spatial components). Hence the vector representation is equivalent to $(\frac12, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Derivation "The spin content of a four-vector": $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$), §7.4.3 ("both $\mathbf J_+^2$ and $\mathbf J_-^2$ equal $\frac34$ … checked numerically") · Yu §4.2.2, eqs. (4.38)–(4.42) · the course's version: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]], the same statement and computation.*

^thm-cb-16-6

> [!proof]- Proof
> *The derivation of Theorem §C3.2.2, with the citations replaced by their CB homes.* Write $E_{ab}$ for the $4\times4$ matrix with $1$ in row $a$, column $b$ ($a, b = 0, \dots, 3$) and $0$ elsewhere, so $E_{ab}E_{cd} = \delta_{bc}E_{ad}$.
>
> **1. The boost generators.** $(K_i)^\mu{}_\nu = (\mathcal J^{0i})^\mu{}_\nu = i(g^{0\mu}\delta^i{}_\nu - g^{i\mu}\delta^0{}_\nu)$. Nonzero entries: $(\mu, \nu) = (0, i)$ gives $ig^{00} = i$; $(\mu, \nu) = (i, 0)$ gives $-ig^{ii} = +i$. So $K_i = i(E_{0i} + E_{i0})$.
>
> **2. The rotation generators.** For spatial $j, k$, $(\mathcal J^{jk})^\mu{}_\nu = i(g^{j\mu}\delta^k{}_\nu - g^{k\mu}\delta^j{}_\nu)$ vanishes unless $\mu$ is spatial, and then $g^{jl} = -\delta_{jl}$: $(\mathcal J^{jk})^l{}_m = -i(\delta_{jl}\delta_{km} - \delta_{kl}\delta_{jm})$. Contract with $\frac12\varepsilon_{ijk}$: $(J_i)^l{}_m = -\frac i2(\varepsilon_{ilm} - \varepsilon_{iml}) = -i\varepsilon_{ilm}$. So $J_i = -i\varepsilon_{ilm}E_{lm}$ (sum over spatial $l, m$): on the spatial components these are the matrices $J^k$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]].
>
> **3. J².** $(J_iJ_i)^l{}_n = \sum_{i,m}(-i\varepsilon_{ilm})(-i\varepsilon_{imn}) = -\sum_{i,m}\varepsilon_{ilm}\varepsilon_{imn}$. With $\varepsilon_{imn} = -\varepsilon_{inm}$ and $\sum_{i,m}\varepsilon_{ilm}\varepsilon_{inm} = 2\delta_{ln}$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], 2), this is $+2\delta_{ln}$; the time row and column are zero. So $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$.
>
> **4. K².** $K_i^2 = i^2(E_{0i} + E_{i0})^2 = -(E_{0i}E_{0i} + E_{0i}E_{i0} + E_{i0}E_{0i} + E_{i0}E_{i0}) = -(0 + E_{00} + E_{ii} + 0)$, since $i \ne 0$. Summing over $i = 1, 2, 3$: $\mathbf K^2 = -(3E_{00} + E_{11} + E_{22} + E_{33}) = -\operatorname{diag}(3, 1, 1, 1)$.
>
> **5. J·K and K·J.** $J_iK_i = (-i\varepsilon_{ilm}E_{lm})\,i(E_{0i} + E_{i0}) = \varepsilon_{ilm}(E_{lm}E_{0i} + E_{lm}E_{i0}) = \varepsilon_{ilm}(0 + \delta_{mi}E_{l0}) = \varepsilon_{ili}E_{l0} = 0$ ($m$ is spatial, so $E_{lm}E_{0i} = 0$). $K_iJ_i = i(E_{0i} + E_{i0})(-i\varepsilon_{ilm}E_{lm}) = \varepsilon_{ilm}(\delta_{il}E_{0m} + 0) = \varepsilon_{iim}E_{0m} = 0$.
>
> **6. The Casimirs.** Expand $\mathbf J_\pm^2 = \frac14(\mathbf J \pm i\mathbf K)\cdot(\mathbf J \pm i\mathbf K)$ into its four terms: $\frac14\bigl(\mathbf J^2 \pm i\mathbf J\cdot\mathbf K \pm i\mathbf K\cdot\mathbf J - \mathbf K^2\bigr) = \frac14\bigl(\operatorname{diag}(0, 2, 2, 2) + \operatorname{diag}(3, 1, 1, 1)\bigr) = \frac34\,\mathbb 1$, by steps 3–5.
>
> **7. Identify.** By [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]] the vector representation is a sum of pieces $(j_+, j_-)$, and on each piece $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]]). Step 6 forces $j_\pm(j_\pm + 1) = \frac34$ on every piece, i.e. $j_+ = j_- = \frac12$; each such piece has dimension $2\cdot2 = 4 = \dim\mathbb C^4$, so there is exactly one. ⚑ By-product: step 3 is the rotation content directly: $s(s+1) = 0$ on $v^0$ and $2$ on $\mathbf v$, so a four-vector is spin $0 \oplus 1$ under rotations, as Theorem §CB.16.8 predicts for $\frac12\otimes\frac12$.
>
> **What the proof shows**
> - The four-vector is irreducible under the Lorentz group (a single $(\frac12, \frac12)$) although it is reducible under rotations (time plus space): boosts mix $v^0$ with $\mathbf v$.
> - Time and space are not $\mathbf J_+$ and $\mathbf J_-$: every vector of $\mathbb C^4$ has $\mathbf J_+^2 = \mathbf J_-^2 = \frac34$; the split into two spins $\frac12$ is a tensor product $\mathbb C^2\otimes\mathbb C^2$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-10|Theorem §CB.17.10]]).
> - Equivalence: this is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]; the course computes the spatial matrices as in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]] and uses the result for vector fields.

^pf-cb-16-6

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-2|Def. §CB.4.2]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-4|Def. §CB.4.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-21|Theorem §CB.1.21]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]]

> [!theorem] Theorem §CB.16.7: The Irreducible Representations of SL(2,ℂ)
> For $j_+, j_- \in \frac12\mathbb Z_{\ge0}$,
>
> $$
> D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}\bigl((\lambda^\dagger)^{-1}\bigr) \quad\text{on}\quad \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\mathbb C^2
> $$
>
> ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]]; $(\lambda^\dagger)^{-1} \cong \bar\lambda$ by [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-16|Theorem §CB.7.16]]) is an irreducible representation of $SL(2, \mathbb C)$ of dimension $(2j_+ + 1)(2j_- + 1)$, whose generators, read through the course's covering $\pi$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]), are those of $(j_+, j_-)$: $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1}$ is equivalent to the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]). Every finite-dimensional irreducible continuous representation of $SL(2, \mathbb C)$ is equivalent to exactly one $D^{(j_+, j_-)}$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3, Ch. 8 §8.2, through [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]] and [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]] · written here (from Theorems §CB.16.1, §CB.7.5, §CB.9.5) · which factor carries $\mathbf J_+$ is fixed by the sign convention of $\mathbf K$: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]] (moved here from the statement, CB ordering pass)*

^thm-cb-16-7

> [!proof]- Proof
> Write $\theta(\lambda) = (\lambda^\dagger)^{-1}$ and $\operatorname{Sym}^k(A)$ for the restriction of $A^{\otimes k}$ to $\operatorname{Sym}^k\mathbb C^2$.
>
> **1. A continuous representation.** $\operatorname{Sym}^k\mathbb C^2$ is invariant under $A^{\otimes k}$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], 1), and $(AB)^{\otimes k} = A^{\otimes k}B^{\otimes k}$, so $A \mapsto \operatorname{Sym}^k(A)$ is a homomorphism. $\theta$ is a homomorphism of $SL(2, \mathbb C)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], 2), and a tensor product of representations is one. The entries of $D^{(j_+, j_-)}(\lambda)$ are polynomials in the entries of $\lambda$ and $\bar\lambda$ ($\lambda^{-1}$ is the adjugate, since $\det\lambda = 1$), so $D^{(j_+, j_-)}$ is continuous. Its dimension is $\dim\operatorname{Sym}^{2j_+}\mathbb C^2\cdot\dim\operatorname{Sym}^{2j_-}\mathbb C^2 = (2j_+ + 1)(2j_- + 1)$ (Theorem §CB.7.13, 1, $\binom{2j+1}{2j} = 2j + 1$).
>
> **2. It is the course's representation.** By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], $\operatorname{Sym}^{2j}\mathbb C^2$ with $\operatorname{Sym}^{2j}(\lambda)$ is equivalent to the polynomial realization $P(z) \mapsto P(\lambda^{\mathsf T}z)$ on homogeneous polynomials of degree $2j$. The tensor product of the two equivalences is an equivalence of $D^{(j_+, j_-)}$ with $\tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}(\theta(\lambda))$ of Theorem §CB.16.9.
>
> **3. Its generators.** Theorem §CB.16.9, 1: $\tilde D(\Lambda_L(s\omega)) = \exp(-\frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ with $D(\mathcal J^{\mu\nu})$ the generators of $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]). $s \mapsto \Lambda_L(s\omega) = e^{sA_L(\omega)}$ is a one-parameter subgroup with $\pi_\ast(A_L(\omega)) = -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ (it covers $e^{s\omega}$, [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]]). Differentiating at $s = 0$: $\tilde D_\ast(A_L(\omega)) = d\bigl(\pi_\ast(A_L(\omega))\bigr)$, where $d$ is the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$, $d(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}) = -\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})$. The $A_L(\omega)$ fill $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, so $\tilde D_\ast = d\circ\pi_\ast$, and by step 2 $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1} \cong d$ (equivalent group representations have equivalent differentials, [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-1|Theorem §CB.16.1]]).
>
> **4. Irreducible.** $(j_+, j_-)$ is irreducible ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]]), and $\pi_\ast$ is a bijection ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]]), so $D^{(j_+, j_-)}_\ast$ has no invariant subspaces but $0$ and the whole space; by Theorem §CB.16.1 neither has $D^{(j_+, j_-)}$.
>
> **5. Every irreducible representation is one of them.** Let $E$ be a finite-dimensional irreducible continuous representation. $E_\ast\circ\pi_\ast^{-1}$ is an irreducible representation of $\mathfrak{so}(1,3)$ (Theorem §CB.16.1). Its complex-linear extension to $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]], 2) is irreducible ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], 2), hence equivalent to $W_+\boxtimes W_-$ with $W_\pm$ irreducible representations of $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-5|Theorem §CB.7.5]], 2), and each $W_\pm$ is some $V_{j_\pm}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]], 3): $\mathbf J_+$ acts as $\mathbf J^{(j_+)}\otimes\mathbb 1$ and $\mathbf J_-$ as $\mathbb 1\otimes\mathbf J^{(j_-)}$, which is Def. §CB.16.2 (equivalently, [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]] with one summand). By step 3, $E_\ast \cong D^{(j_+, j_-)}_\ast$, so $E \cong D^{(j_+, j_-)}$ (Theorem §CB.16.1).
>
> **6. Exactly one.** If $D^{(j_+, j_-)} \cong D^{(k_+, k_-)}$, their differentials are equivalent, so $(j_+, j_-) \cong (k_+, k_-)$ as $\mathfrak{so}(1,3)$-representations, and the labels coincide (Theorem §CB.16.4, last clause).
>
> **What the proof shows**
> - $(j_+, j_-)$ is $2j_+$ symmetrized slots carrying $\lambda$ and $2j_-$ carrying $(\lambda^\dagger)^{-1}$ — undotted and dotted indices ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-16|Theorem §CB.7.16]]).
> - ⚑ By-product (convention): the labels are tied to $\pi$. Read through $\rho$ and the Clifford identification $\phi$, $x \mapsto D^{(j_+, j_-)}(\phi(x))$ is $D^{(j_+, j_-)}\circ\theta$ in the course's parametrization ($\phi = \theta\circ(\theta\circ\phi)$, Theorem §CB.15.12, 2), which is equivalent to $D^{(j_-, j_+)}$: the two factors exchange roles. This is the group form of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]].

^pf-cb-16-7

*Uses:* [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-5|Theorem §CB.7.5]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-5|Theorem §CB.9.5]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-9|Theorem §CB.3.9]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-8|Theorem §CB.5.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-1|Theorem §CB.16.1]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]]

## Rotation content, products, parity, conjugation

> [!theorem] Theorem §CB.16.8: Rotation Content and the Sign of a 2π Rotation
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

^thm-cb-16-8

> [!derivation]- Derivation
> **1. Restrict to rotations.** With $\boldsymbol\eta = 0$, Theorem §CB.5.3 gives $D = e^{-i\boldsymbol\theta\cdot\mathbf J_+}e^{-i\boldsymbol\theta\cdot\mathbf J_-} = e^{-i\boldsymbol\theta\cdot\mathbf J^{(j_+)}}\otimes e^{-i\boldsymbol\theta\cdot\mathbf J^{(j_-)}}$ on $(j_+, j_-)$, using $e^{A\otimes\mathbb 1} = e^A\otimes\mathbb 1$ (term by term) and $(A\otimes\mathbb 1)(\mathbb 1\otimes B) = A\otimes B$. This is the rotation of a composite system of two angular momenta $j_+$ and $j_-$, generated by $\mathbf J = \mathbf J_+ + \mathbf J_-$ ([[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-3|Theorem §CB.7.3]]).
>
> **2. Clebsch–Gordan series.** By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-14|Theorem §CB.9.14]], $D^{(j_+)}\otimes D^{(j_-)} = \bigoplus_{j = |j_+ - j_-|}^{j_+ + j_-}D^{(j)}$, each once. (Dimension check: $\sum_j(2j + 1) = (2j_+ + 1)(2j_- + 1)$.)
>
> **3. The 2π rotation.** In step 1 with $\boldsymbol\theta = 2\pi\hat{\mathbf n}$, each factor is a $2\pi$ rotation in a single multiplet, $e^{-2\pi i\hat{\mathbf n}\cdot\mathbf J^{(j)}} = (-1)^{2j}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]); the tensor product of $(-1)^{2j_+}\mathbb 1$ and $(-1)^{2j_-}\mathbb 1$ is $(-1)^{2j_+ + 2j_-}\mathbb 1$.
>
> **4. Consistency of the sign.** All spins in step 2 differ from $j_+ + j_-$ by integers, so $(-1)^{2j}$ is the same for each: a representation is either wholly "bosonic" or wholly "fermionic" under rotations.
>
> **5. Part 3.** $e^{2\pi M^{12}}$ is the rotation by $2\pi$ about $z$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]), the identity of $SO^+(1,3)$. Its parameters are $\omega_{12} = 2\pi$, i.e. $\boldsymbol\theta = 2\pi\hat{\mathbf z}$, $\boldsymbol\eta = 0$, and step 3 assigns it $(-1)^{2(j_+ + j_-)}\mathbb 1$; a representation must send the identity to $\mathbb 1$. Since also $e^{0} = \mathbb 1$ is assigned $\mathbb 1$, the same group element receives both signs: the matrix is fixed only up to sign, a two-valued representation ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-7|Def. §CB.9.7]]; the topology behind it, [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|§CB.9, Remark: The same pattern for the Lorentz group]]).
>
> **What the derivation shows**
> - The rotation content of a Lorentz representation is ordinary addition of angular momentum; nothing about boosts enters.
> - The half-integer representations are honest representations of the double cover $SL(2, \mathbb C)$ of $SO^+(1,3)$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]), as spin $\frac12$ is of $SU(2)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]; [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]); that the integer ones are honest representations of $SO^+(1,3)$ itself needs that double-cover structure and is not proved here (it is [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], 2).
> - Used next: the catalogue ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|Remark: The representations met in the course]]); the sign of spinor fields ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]).

^der-cb-16-8

*Uses:* [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-3|Theorem §CB.7.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-14|Theorem §CB.9.14]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]

The course's integration theorem, with the explicit polynomial model of $(j_+, j_-)$; its proof uses the Weyl matrices and their properties ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-15-6|Def. §CB.15.6]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]]) (first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]); it is placed here because the theorems below use it:

> [!theorem] Theorem §CB.16.9: Integer (j₊, j₋) Are Representations of SO⁺(1,3)
> 1. On $V_{j_+}\otimes V_{j_-}$, $V_j$ the homogeneous polynomials of degree $2j$ in $z \in \mathbb C^2$ (the spin-$j$ space of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]), the matrices
>
> $$
> \tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}\bigl((\lambda^\dagger)^{-1}\bigr), \qquad \bigl(D^{(j)}(M)P\bigr)(z) = P(M^{\mathsf T}z),
> $$
>
> form a representation ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-4|Def. §CB.2.4]]) of $SL(2, \mathbb C)$ with $\tilde D(\Lambda_L(\omega)) = \exp\bigl(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})\bigr)$, $D(\mathcal J^{\mu\nu})$ the generators ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]]) of the representation $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]), and $\tilde D(-\mathbb 1) = (-1)^{2(j_+ + j_-)}$. It is the only one with these generators.
> 2. If $j_+ + j_-$ is an integer, $D(\Lambda) \equiv \tilde D(\lambda)$ for any $\lambda$ with $\pi(\lambda) = \Lambda$ is a well-defined representation of $SO^+(1,3)$. If $j_+ + j_-$ is half an odd integer, $D(\Lambda)$ is defined only up to sign, a two-valued representation ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-7|Def. §CB.9.7]]), as [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]] found.
> 3. Hence a finite-dimensional representation of the Lorentz algebra (a sum of pieces $(j_+, j_-)$, [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]]) integrates to $SO^+(1,3)$ iff every piece $(j_+, j_-)$ in it has $j_+ + j_-$ an integer; every one integrates to $SL(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (spin $j$ on polynomials), §7.4.4 (the sign rule) and Ch. 8 §8.1 ("the Dirac representation is a representation of the double cover") · the proof written out here*

^thm-cb-16-9

> [!derivation]- Derivation
> **1. A representation of SL(2, C).** $D^{(j)}$ is a representation of $GL(2, \mathbb C)$, and $\lambda \mapsto (\lambda^\dagger)^{-1}$ a homomorphism ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^lem-cb-9-11|Lemma §CB.9.11]]: the computation of this step, extracted there in the CB ordering pass). A tensor product of representations is one, $(A\otimes B)(A'\otimes B') = AA'\otimes BB'$. So $\tilde D(\lambda_1\lambda_2) = \tilde D(\lambda_1)\tilde D(\lambda_2)$.
>
> **2. On the Weyl matrices.** With $\boldsymbol\alpha = \boldsymbol\theta - i\boldsymbol\eta \in \mathbb C^3$: $\Lambda_L(\omega) = e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2}$ and $(\Lambda_L(\omega)^\dagger)^{-1} = \Lambda_R(\omega) = e^{-i\bar{\boldsymbol\alpha}\cdot\boldsymbol\sigma/2}$, $\bar{\boldsymbol\alpha} = \boldsymbol\theta + i\boldsymbol\eta$ (Theorem §CB.15.7, 2). So $\tilde D(\Lambda_L(\omega)) = f_{j_+}(\boldsymbol\alpha)\otimes f_{j_-}(\bar{\boldsymbol\alpha})$ with $f_j(\boldsymbol\alpha) \equiv D^{(j)}(e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2})$.
>
> **3. Real angles.** For real $\boldsymbol\alpha = s\hat{\mathbf n}$, $s \mapsto e^{-is\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ is a one-parameter subgroup of $SU(2)$, so $s \mapsto f_j(s\hat{\mathbf n})$ is a one-parameter group of matrices whose derivative at $0$ is $-i\hat{\mathbf n}\cdot\mathbf J^{(j)}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], 1: $D^{(j)}$ on $SU(2)$ has the spin-$j$ matrices as generators). A one-parameter group is fixed by its derivative at $0$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]), so $f_j(\boldsymbol\alpha) = g_j(\boldsymbol\alpha) \equiv e^{-i\boldsymbol\alpha\cdot\mathbf J^{(j)}}$ for all $\boldsymbol\alpha \in \mathbb R^3$.
>
> **4. Complex angles: analytic continuation.** Each entry of $f_j$ is a polynomial in the entries of $e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2}$, each of which is an entire function of $(\alpha_1, \alpha_2, \alpha_3) \in \mathbb C^3$ (an everywhere convergent power series); each entry of $g_j$ is entire for the same reason. An entire function $F$ on $\mathbb C^3$ vanishing on $\mathbb R^3$ vanishes identically: for fixed real $\alpha_2, \alpha_3$, $\alpha_1 \mapsto F$ is entire and vanishes on $\mathbb R$, so it vanishes on $\mathbb C$ (identity theorem); then for fixed $\alpha_1 \in \mathbb C$, real $\alpha_3$, the same in $\alpha_2$; then in $\alpha_3$. Applied to the entries of $f_j - g_j$: $f_j(\boldsymbol\alpha) = e^{-i\boldsymbol\alpha\cdot\mathbf J^{(j)}}$ for all complex $\boldsymbol\alpha$.
>
> **5. The generators.** By steps 2 and 4, $\tilde D(\Lambda_L(\omega)) = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J^{(j_+)}}\otimes e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J^{(j_-)}}$. Using $e^{A}\otimes e^{B} = (e^A\otimes\mathbb 1)(\mathbb 1\otimes e^B) = e^{A\otimes\mathbb 1}e^{\mathbb 1\otimes B}$ (as in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-8|Derivation §CB.16.8]], step 1), this is $e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+}e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-}$ with $\mathbf J_\pm$ of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], which is $\exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ by [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3|Theorem §CB.5.3]]. Differentiating at $\omega = 0$: the generators of $\tilde D$ are those of $(j_+, j_-)$.
>
> **6. The element −1.** $P$ is homogeneous of degree $2j$, so $(D^{(j)}(-\mathbb 1)P)(z) = P(-z) = (-1)^{2j}P(z)$; and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. Hence $\tilde D(-\mathbb 1) = (-1)^{2j_+}(-1)^{2j_-} = (-1)^{2(j_+ + j_-)}$.
>
> **7. Uniqueness.** Every $\lambda$ is $\pm\Lambda_L(\omega_1)\Lambda_L(\omega_2)$: $\pi(\lambda) = e^{\omega_1}e^{\omega_2}$ (step 1 of Derivation §CB.15.9) $= \pi(\Lambda_L(\omega_1)\Lambda_L(\omega_2))$, and Theorem §CB.15.5; and $-\mathbb 1 = \Lambda_L(2\pi\hat{\mathbf z})$. So the Weyl matrices generate $SL(2, \mathbb C)$, and a continuous representation is fixed by its values on them. On each one-parameter group $s \mapsto \Lambda_L(s\omega)$ these values form a one-parameter group of matrices, fixed by its derivative at $s = 0$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]]), i.e. by the generators, which step 5 identified.
>
> **8. Descending to SO⁺(1,3).** Let $j_+ + j_-$ be an integer. Then $\tilde D(-\lambda) = \tilde D(-\mathbb 1)\tilde D(\lambda) = \tilde D(\lambda)$. For $\Lambda \in SO^+(1,3)$ there is $\lambda$ with $\pi(\lambda) = \Lambda$ (Theorem §CB.15.9), and the only other is $-\lambda$ (Theorem §CB.15.5), so $D(\Lambda) = \tilde D(\lambda)$ is well defined. If $\pi(\lambda_k) = \Lambda_k$ then $\pi(\lambda_1\lambda_2) = \Lambda_1\Lambda_2$, so $D(\Lambda_1\Lambda_2) = \tilde D(\lambda_1\lambda_2) = D(\Lambda_1)D(\Lambda_2)$: a representation. Its value on $e^\omega = \pi(\Lambda_L(\omega))$ is $\exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ by step 5, so it is *the* representation that §C3.2 wrote down on exponentials. For $j_+ + j_-$ half an odd integer, $\tilde D(-\lambda) = -\tilde D(\lambda)$, so the two lifts of $\Lambda$ give opposite matrices, and no choice of signs gives a representation ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], 3).
>
> **9. Part 3.** By [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]] every finite-dimensional representation of the algebra is a direct sum of pieces $(j_+, j_-)$; integrate each by steps 1–5 and add. The sum descends to $SO^+(1,3)$ iff $\tilde D(-\mathbb 1) = \mathbb 1$, i.e. iff every piece has $(-1)^{2(j_+ + j_-)} = 1$.
>
> **What the derivation shows**
> - $(j_+, j_-)$ is literally $2j_+$ symmetrized left-handed slots and $2j_-$ symmetrized right-handed slots: $D^{(j)}(\lambda)$ acts by one $\lambda$ per variable $z$, as spin $j$ acts by one $U$ per slot in the rotation case.
> - The sign $(-1)^{2(j_+ + j_-)}$ of §CB.16 is the parity of the total number of spinor slots, the value of $\tilde D$ on the kernel of the covering.
> - The only analytic input is the identity theorem: the complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$ of the factorization (§C3.2) are honest complex arguments of entire functions.
> - Used next: the Dirac representation as the case $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); fields of every spin ([[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]).

^der-cb-16-9

*Uses:* [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-7|Theorem §CB.15.7]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-8|Theorem §CB.2.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-8|Derivation §CB.16.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]; the identity theorem for entire functions

> [!theorem] Theorem §CB.16.10: Every Finite-Dimensional Representation Splits into a Tensor and a Spinor Part
> 1. The representation $(j_+, j_-)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]) is a tensor representation ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-26|Def. §CB.13.26]]) if $j_+ + j_-$ is an integer and a spinor representation if $j_+ + j_-$ is half an odd integer; the rotation by $2\pi$ about any axis gives the same sign.
> 2. Every finite-dimensional representation $V$ is uniquely $V = V_{\rm t}\oplus V_{\rm s}$, with $V_{\rm t}$ a tensor and $V_{\rm s}$ a spinor representation, both invariant: $V_{\rm t}$, $V_{\rm s}$ are the eigenspaces of $e^{-2\pi iJ_3}$ for $+1$ and $-1$, and $V_{\rm t}$ ($V_{\rm s}$) is the sum of the pieces $(j_+, j_-)$ of $V$ with $j_+ + j_-$ integer (half-integer).
>
> On $SO^+(1,3)$ a tensor representation integrates to a representation, a spinor representation only to a two-valued one ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], 3; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-7|Def. §CB.9.7]]); both integrate to representations of $SL(2, \mathbb C)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|QFT Theorem §CB.16.9]], 3).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4 (Principle "Spin content, and the sign of a 2π rotation", eq. (twopisign), and the paragraph "Representations with $j_+ + j_-$ an integer return to themselves after a full turn (bosonic), those with $j_+ + j_-$ half-integer change sign (fermionic)") · Yu, opening of Ch. 5 (p. 157) · the decomposition written out here*

^thm-cb-16-10

> [!derivation]- Derivation
> **1. One piece.** On $(j_+, j_-)$ the rotation by $2\pi$ about the axis $\hat{\mathbf n}$ is $e^{-2\pi i\hat{\mathbf n}\cdot\mathbf J} = (-1)^{2(j_+ + j_-)}\mathbb 1$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], 2), for every unit vector $\hat{\mathbf n}$. $2(j_+ + j_-)$ is an even integer exactly when $j_+ + j_-$ is an integer, and odd exactly when $j_+ + j_-$ is half an odd integer. This is part 1.
>
> **2. Decompose.** By [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]], $V = W_1\oplus\dots\oplus W_r$ with each $W_k$ invariant and equivalent to some $(j_+^{(k)}, j_-^{(k)})$. Put $V_{\rm t} = \bigoplus\{W_k : j_+^{(k)} + j_-^{(k)}\ \text{integer}\}$ and $V_{\rm s} = \bigoplus\{W_k : j_+^{(k)} + j_-^{(k)}\ \text{half-integer}\}$. A sum of invariant subspaces is invariant, so both are invariant, and $V = V_{\rm t}\oplus V_{\rm s}$.
>
> **3. The 2π rotation on each part.** The generators of $V$ are block diagonal in the decomposition of step 2, hence so is $e^{-2\pi iJ_3}$ (powers of a block-diagonal matrix are block diagonal), with blocks $e^{-2\pi iJ_3}|_{W_k} = (-1)^{2(j_+^{(k)} + j_-^{(k)})}\mathbb 1$ by step 1 (an equivalence $W_k \cong (j_+, j_-)$ conjugates $e^{-2\pi iJ_3}$ and leaves $\pm\mathbb 1$ unchanged). So $e^{-2\pi iJ_3} = +\mathbb 1$ on $V_{\rm t}$ and $-\mathbb 1$ on $V_{\rm s}$: $V_{\rm t}$ is a tensor and $V_{\rm s}$ a spinor representation.
>
> **4. Uniqueness.** By step 3, $V_{\rm t} \subseteq E_+ \equiv \ker(e^{-2\pi iJ_3} - \mathbb 1)$ and $V_{\rm s} \subseteq E_- \equiv \ker(e^{-2\pi iJ_3} + \mathbb 1)$; $E_+\cap E_- = 0$ (a vector with $Rv = v = -v$ vanishes), and $\dim V_{\rm t} + \dim V_{\rm s} = \dim V$, so $V_{\rm t} = E_+$ and $V_{\rm s} = E_-$. These kernels are defined by the representation alone, without choosing the $W_k$. Any other splitting into a tensor and a spinor part $V'_{\rm t}\oplus V'_{\rm s}$ has $V'_{\rm t} \subseteq E_+$, $V'_{\rm s} \subseteq E_-$ by definition, hence equals it by the same dimension count.
>
> **What the derivation shows**
> - "Spinor" is a property decided by one group element, the $2\pi$ rotation, which is the identity of $SO^+(1,3)$ but not of its cover $SL(2, \mathbb C)$; a representation can mix both kinds only as a direct sum, never inside one irreducible piece.
> - The Dirac representation $(\frac12, 0)\oplus(0, \frac12)$ is a spinor representation; the four-vector $(\frac12, \frac12)$ and the field strength $(1, 0)\oplus(0, 1)$ are tensor representations ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]; [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).
> - Used next: the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|QFT Theorem §C5a.3.2]]); spin and statistics ([[§C5b.9 Spin and Statistics|§C5b.9]]).

^der-cb-16-10

*Uses:* [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-26|Def. §CB.13.26]]

> [!theorem] Theorem §CB.16.11: Tensor Products Add Each Copy Separately
> If $D$, $D'$ are representations on $V$, $V'$, then $D\otimes D'$ has generators $D(\mathcal J^{\mu\nu})\otimes\mathbb 1 + \mathbb 1\otimes D'(\mathcal J^{\mu\nu})$, so $\mathbf J_\pm^{\rm tot} = \mathbf J_\pm\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J'_\pm$, and
>
> $$
> (j_+, j_-)\otimes(j'_+, j'_-) = \bigoplus_{J_+ = |j_+ - j'_+|}^{j_+ + j'_+}\ \bigoplus_{J_- = |j_- - j'_-|}^{j_- + j'_-}(J_+, J_-) .
> $$
>
> In particular $(\frac12, \frac12)\otimes(\frac12, \frac12) = (1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, $16 = 9 + 3 + 3 + 1$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (Derivation "Products: two-index tensors are (1,1)⊕(1,0)⊕(0,1)⊕(0,0)")*

^thm-cb-16-11

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
> **3. Add angular momenta in each copy.** In the first pair, $\mathbf J^{(j_+)}\otimes\mathbb 1 + \mathbb 1\otimes\mathbf J^{(j'_+)}$ is the total angular momentum of two spins; in the coupled basis it is block diagonal with one spin-$J_+$ block for each $J_+$ from $|j_+ - j'_+|$ to $j_+ + j'_+$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-14|Theorem §CB.9.14]]). The same in the second pair with $J_-$.
>
> **4. Distribute.** $(\bigoplus_{J_+}W_{J_+})\otimes(\bigoplus_{J_-}W_{J_-}) = \bigoplus_{J_+, J_-}W_{J_+}\otimes W_{J_-}$, and on each summand $\mathbf J_+^{\rm tot}$ acts as spin-$J_+$ matrices on the first factor and $\mathbf J_-^{\rm tot}$ as spin-$J_-$ matrices on the second: that summand is $(J_+, J_-)$ (Def. §CB.16.2).
>
> **5. Two vectors.** $j_\pm = j'_\pm = \frac12$: in each copy $\frac12\otimes\frac12 = 0\oplus1$, so the four combinations $(J_+, J_-) \in \{0, 1\}^2$ appear once each, with dimensions $9, 3, 3, 1$.
>
> **What the derivation shows**
> - The two copies never mix: angular momenta are added *separately* in the $+$ and the $-$ copy. Rotations, which see $\mathbf J_+ + \mathbf J_-$, add all four spins at once (Theorem §CB.16.8).
> - Which pieces of a two-index tensor $T^{\mu\nu}$ are which (trace, antisymmetric, symmetric traceless) is [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-12|Theorem §CB.17.12]].

^der-cb-16-11

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-14|Theorem §CB.9.14]]

> [!remark] Remark: Sums versus products
> $(\frac12, 0)\oplus(0, \frac12)$ (dimension $2 + 2$) and $(\frac12, \frac12)$ (dimension $2\times2$) are both four-dimensional and must not be confused. Two tests separate them. The Casimirs: on $(\frac12, \frac12)$, $\mathbf J_+^2 = \mathbf J_-^2 = \frac34$ on every vector (Theorem §C3.2.2); on the sum, $\mathbf J_+^2$ is $\frac34$ on one half and $0$ on the other. The $2\pi$ rotation (Theorem §CB.16.8): $+1$ on $(\frac12, \frac12)$, $-1$ on $(\frac12, 0)\oplus(0, \frac12)$. In a sum no vector feels both copies; in an irreducible $(j_+, j_-)$ with $j_\pm \ne 0$ every vector does. The Dirac spinor is the sum, the four-vector the product ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-5|Theorem §CB.17.5]] applies both tests to the Dirac matrices).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (paragraph "Sums versus products")*

^rem-cb-16-1

> [!theorem] Theorem §CB.16.12: The Parity Automorphism Exchanges the Two Copies
> 1. The map $\pi$: $\mathbf J \mapsto \mathbf J$, $\mathbf K \mapsto -\mathbf K$ preserves the Lorentz algebra.
> 2. $\pi$ exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$; composed with $\pi$, the representation $(j_+, j_-)$ becomes equivalent to $(j_-, j_+)$.
> 3. If an invertible $Q$ on $V$ satisfies $Q\mathbf JQ^{-1} = \mathbf J$, $Q\mathbf KQ^{-1} = -\mathbf K$, then $(j_+, j_-)$ and $(j_-, j_+)$ occur in $V$ with equal multiplicity.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 (paragraph "Parity and conjugation exchange the two copies") · the parts written out here*

^thm-cb-16-12

> [!derivation]- Derivation
> **1. π preserves the algebra.** Check the three relations of Theorem §CB.4.6 with $\mathbf K$ replaced by $-\mathbf K$: $[J_i, J_j] = i\varepsilon_{ijk}J_k$ does not involve $\mathbf K$; $[J_i, -K_j] = -i\varepsilon_{ijk}K_k = i\varepsilon_{ijk}(-K_k)$; $[-K_i, -K_j] = [K_i, K_j] = -i\varepsilon_{ijk}J_k$. All three hold.
>
> **2. J± are exchanged.** $\pi(\mathbf J_\pm) = \frac12(\mathbf J \pm i(-\mathbf K)) = \frac12(\mathbf J \mp i\mathbf K) = \mathbf J_\mp$.
>
> **3. The labels.** In $(j_+, j_-)$ composed with $\pi$, the new $\mathbf J_+$ is the old $\mathbf J_- = \mathbb 1\otimes\mathbf J^{(j_-)}$ and vice versa. The swap of tensor factors $\mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1} \to \mathbb C^{2j_-+1}\otimes\mathbb C^{2j_++1}$, $a\otimes b \mapsto b\otimes a$, turns this into $\mathbf J^{(j_-)}\otimes\mathbb 1$ and $\mathbb 1\otimes\mathbf J^{(j_+)}$: the representation $(j_-, j_+)$.
>
> **4. Part 3.** From $Q\mathbf JQ^{-1} = \mathbf J$ and $Q\mathbf KQ^{-1} = -\mathbf K$, as in step 2, $Q\mathbf J_\pmQ^{-1} = \mathbf J_\mp$, hence $Q\mathbf J_\pm^2Q^{-1} = \mathbf J_\mp^2$. If $\mathbf J_+^2v = av$ and $\mathbf J_-^2v = bv$, then $\mathbf J_-^2(Qv) = Q\mathbf J_+^2v = a\,Qv$ and $\mathbf J_+^2(Qv) = b\,Qv$. So the invertible $Q$ maps the joint eigenspace for $(a, b)$ into that for $(b, a)$, and $Q^{-1}$ maps back: the two have equal dimension, and by Theorem §CB.16.5, step 9, equal multiplicities.
>
> **What the derivation shows**
> - Statement 1 is the parity of the vector representation read on the algebra; the physical reading — parity on four-vectors and on the indices of fields, and why a parity-invariant theory carries both copies — is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]] (physics; steps 2 and the consequences of the original derivation are kept there).

^der-cb-16-12

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]]

> [!theorem] Theorem §CB.16.13: Complex Conjugation Exchanges the Two Copies
> If $D$ is a representation, so is its complex conjugate $\bar D(\Lambda) = D(\Lambda)^*$, with generators $\bar D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\mu\nu})^*$. The conjugate of $(j_+, j_-)$ is equivalent to $(j_-, j_+)$; for spin $j$ the equivalence is $-\mathbf J^{(j)*} = R\,\mathbf J^{(j)}R^{-1}$ with $R = e^{-i\pi J^{(j)}_2}$, the rotation by $\pi$ about the $2$-axis.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 ("Complex conjugation turns θ − iη into θ + iη and does the same exchange") · the derivation written out here*

^thm-cb-16-13

> [!derivation]- Derivation
> **1. The conjugate is a representation.** Entrywise conjugation respects products, $(AB)^{\ast} = A^{\ast}B^{\ast}$, so $D(\Lambda_1)^{\ast}D(\Lambda_2)^{\ast} = D(\Lambda_1\Lambda_2)^{\ast}$.
>
> **2. Its generators.** The parameters $\omega$ are real, so conjugating $D(e^{s\omega}) = \mathbb 1 - \frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}) + O(s^2)$ gives $\mathbb 1 + \frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})^{\ast} + O(s^2) = \mathbb 1 - \frac{is}2\omega_{\mu\nu}\bigl(-D(\mathcal J^{\mu\nu})^{\ast}\bigr) + O(s^2)$. So $\bar{\mathbf J} = -\mathbf J^{\ast}$, $\bar{\mathbf K} = -\mathbf K^{\ast}$.
>
> **3. The copies are exchanged.** $\bar{\mathbf J}_\pm = \frac12(\bar{\mathbf J} \pm i\bar{\mathbf K}) = -\frac12(\mathbf J^{\ast} \pm i\mathbf K^{\ast}) = -\bigl(\frac12(\mathbf J \mp i\mathbf K)\bigr)^{\ast} = -(\mathbf J_\mp)^{\ast}$, using $(\mp i\mathbf K)^{\ast} = \pm i\mathbf K^{\ast}$.
>
> **4. On (j₊, j₋).** $\bar{\mathbf J}_+ = -(\mathbb 1\otimes\mathbf J^{(j_-)})^{\ast} = \mathbb 1\otimes(-\mathbf J^{(j_-)\ast})$ and $\bar{\mathbf J}_- = (-\mathbf J^{(j_+)\ast})\otimes\mathbb 1$.
>
> **5. −J* is equivalent to J.** In the standard basis $J^{(j)}_1$, $J^{(j)}_3$ are real and $J^{(j)}_2$ is imaginary (Def. §CB.16.2, text), so $-\mathbf J^{(j)\ast} = (-J_1, J_2, -J_3)$. Angular momentum is a vector operator, $D(R)^\dagger J_iD(R) = R_{ik}J_k$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-8|Theorem §CB.4.8]]); for the rotation by $\pi$ about the $2$-axis, $R = \operatorname{diag}(-1, 1, -1) = R^{-1}$, and $D = e^{-i\pi J_2}$ gives $e^{-i\pi J_2}J_ie^{i\pi J_2} = (R^{-1})_{ik}J_k$, i.e. $(-J_1, J_2, -J_3)$. So $-\mathbf J^{(j)\ast} = e^{-i\pi J_2}\mathbf J^{(j)}e^{i\pi J_2}$.
>
> **6. Assemble.** Conjugating step 4 by $e^{-i\pi J^{(j_+)}_2}\otimes e^{-i\pi J^{(j_-)}_2}$ turns it into $\bar{\mathbf J}_+ = \mathbb 1\otimes\mathbf J^{(j_-)}$, $\bar{\mathbf J}_- = \mathbf J^{(j_+)}\otimes\mathbb 1$; the swap of the two factors (as in Theorem §CB.16.12, step 3) gives $(j_-, j_+)$. ⚑ By-product: for $j = \frac12$, $e^{-i\pi\sigma_2/2} = -i\sigma_2$, so $\sigma_2\psi^{\ast}$ transforms like the other Weyl spinor.
>
> **What the derivation shows**
> - In the course: Peskin–Schroeder's $\sigma^2\psi_L^{\ast}$ (eq. (3.38); [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]]; QFT C9, planned) (moved here from the By-product of step 6, CB ordering pass).
> - In the factorization of Theorem §CB.5.3, conjugation turns the angle $\boldsymbol\theta - i\boldsymbol\eta$ into $\boldsymbol\theta + i\boldsymbol\eta$: it exchanges the copies because the two angles are conjugates.
> - The operator $e^{-i\pi J_2}$ is the one that, followed by complex conjugation, is time reversal in Quantum Mechanics ([[§C8.3★ Time Reversal#^thm-c8-3-6|QM Theorem §C8.3.6]]): both use that only $J_2$ is imaginary in the standard basis.
> - A real field (a real four-vector, a real $F^{\mu\nu}$) must contain, with $(j_+, j_-)$, also $(j_-, j_+)$ or be of the form $(j, j)$.

^der-cb-16-13

*Uses:* [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-8|Theorem §CB.4.8]]

> [!remark] Remark: What the labels (j₊, j₋) mean
> Each statement below is proved in this section; together they say why "$(\frac12, 0)$" and "$(0, \frac12)$" are meaningful names.
> - **Two angular momenta.** The complexified Lorentz algebra is two commuting copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$, spanned by $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]]; [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]]); the real algebra is not split ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-5|Theorem §CB.5.5]]). A finite-dimensional representation chooses a spin for each copy; $(j_+, j_-)$ records the two choices, read off from the Casimirs $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]]), and the dimension is $(2j_+ + 1)(2j_- + 1)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]).
> - **Rotations see the sum.** Adding and subtracting the definitions of $\mathbf J_\pm$ gives $\mathbf J = \mathbf J_+ + \mathbf J_-$ and $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$. So under rotations $(j_+, j_-)$ is the addition of two angular momenta, with spins $|j_+ - j_-|, \dots, j_+ + j_-$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]): $(\frac12, 0)$ and $(0, \frac12)$ are both spin $\frac12$, $(\frac12, \frac12)$ is $0\oplus1$, the four-vector ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]). Neither label alone is the spin ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-2|Remark: Neither label is the spin]]).
> - **Boosts see the difference.** $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ is $-\frac i2\boldsymbol\sigma$ on $(\frac12, 0)$ and $+\frac i2\boldsymbol\sigma$ on $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]; the sign convention $K_i = \mathcal J^{0i}$: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|Caution: Which one is (½, 0) depends on the sign of K]]). Same rotations, opposite boosts: that is the whole difference between left- and right-handed.
> - **The 2π rotation sees the parity of 2(j₊ + j₋).** It is $(-1)^{2(j_+ + j_-)}$, which sorts every representation into tensor and spinor parts ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]); $(\frac12, 0)$ and $(0, \frac12)$ are the smallest spinor representations.
> - **Parity and conjugation swap the copies.** Parity keeps $\mathbf J$ and reverses $\mathbf K$, so it exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$ and $(j_+, j_-) \leftrightarrow (j_-, j_+)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]]); complex conjugation does the same ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13|Theorem §CB.16.13]]). A spinor field on which parity acts must therefore contain $(\frac12, 0)$ and $(0, \frac12)$ together: the Dirac field is $(\frac12, 0)\oplus(0, \frac12)$ (the user's PHY 513 notes, Ch. 7 §7.4.6, paragraph "Parity and conjugation exchange the two copies"; how parity acts on Dirac fields is QFT C9, planned).
>
> *Source: PS §3.1–§3.2, pp. 38–44 · the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "What a label (j₊, j₋) means, worked out"; §7.4.4; §7.4.6) · PHY 513 Lecture 7, Parts B–C · Yu §3.2 · the summary written here*

^rem-cb-16-2

## Not unitary

> [!theorem] Theorem §CB.16.14: No Finite-Dimensional Representation Is Unitary
> 1. In an inner product with $\mathbf J_\pm$ Hermitian (Theorem §CB.16.5), $\mathbf J$ is Hermitian and $\mathbf K$ anti-Hermitian; a boost $D = e^{-i\boldsymbol\eta\cdot\mathbf K} = e^{-\boldsymbol\eta\cdot(\mathbf J_+ - \mathbf J_-)}$ is Hermitian and positive, and unitary only if $\boldsymbol\eta\cdot\mathbf K = 0$.
> 2. If a finite-dimensional representation of $SO^+(1,3)$ is unitary for some inner product, it is trivial: $D(\Lambda) = \mathbb 1$ for every $\Lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Principle "Hermitian generators do not make boosts unitary", citing Weinberg vol. 1 ch. 2 for the general theorem), §7.4.6 ("$\vec J$ can be taken Hermitian and $\vec K$ is then anti-Hermitian") · the proof for the Lorentz group written out here*

^thm-cb-16-14

> [!derivation]- Derivation
> **1. Part 1, Hermiticity.** $\mathbf J = \mathbf J_+ + \mathbf J_-$ is a sum of Hermitian matrices. $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ and $(-iX)^\dagger = iX^\dagger = iX$ for Hermitian $X$, so $\mathbf K^\dagger = -\mathbf K$.
>
> **2. Part 1, the boost.** $-i\boldsymbol\eta\cdot\mathbf K = -i\boldsymbol\eta\cdot(-i)(\mathbf J_+ - \mathbf J_-) = -\boldsymbol\eta\cdot(\mathbf J_+ - \mathbf J_-) \equiv -H$ with $H$ Hermitian. In an eigenbasis of $H$ (real eigenvalues $h_k$), $e^{-H} = \operatorname{diag}(e^{-h_k})$: Hermitian with positive eigenvalues. It is unitary only if every $|e^{-h_k}| = 1$, i.e. every $h_k = 0$, i.e. $H = 0$.
>
> **3. Part 2: unitary means Hermitian generators.** Suppose $\langle\cdot, \cdot\rangle$ makes every $D(\Lambda)$ unitary. For each generator $X$, $t \mapsto D(e^{t\omega}) = e^{-itX}$ (with $\omega$ the corresponding parameter) is unitary for all real $t$; differentiating $\langle e^{-itX}v, e^{-itX}w\rangle = \langle v, w\rangle$ at $t = 0$ gives $X^\dagger = X$. In particular $K_3$ is Hermitian, so its eigenvalues are real.
>
> **4. Part 2: the eigenvalues of K₃ are imaginary.** By Theorem §CB.16.5, $V$ is a sum of pieces $(j_+, j_-)$; on each, $K_3 = -i(J^{(j_+)}_3\otimes\mathbb 1 - \mathbb 1\otimes J^{(j_-)}_3)$ is diagonal on $|m_+\rangle\otimes|m_-\rangle$ with eigenvalue $-i(m_+ - m_-)$. Eigenvalues do not depend on the inner product or basis. Being both real (step 3) and imaginary, all are $0$; the pair $m_+ = j_+$, $m_- = -j_-$ then gives $j_+ + j_- = 0$, so every piece is $(0, 0)$.
>
> **5. Part 2: trivial.** On $(0, 0)$ all generators vanish, so $D(e^\omega) = e^0 = \mathbb 1$ for every $\omega$. Every element of $SO^+(1,3)$ is a product of exponentials (a boost times a rotation, [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], each an exponential by [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]), so $D(\Lambda) = \mathbb 1$.
>
> **What the derivation shows**
> - The finite-dimensional representations, which act on the indices of fields, are never unitary (except the trivial one). Unitarity is required of the operators on quantum states, which therefore must be infinite-dimensional: the one-particle spaces of [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]], with $U(\Lambda)$ of [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]] ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]).
> - Rotations are unitary in these inner products ($\mathbf J$ Hermitian); boosts are not. This is the precise form of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]], proved here for the Lorentz group without the general theorem on noncompact groups.
> - Used next: the spinor conjugate $\bar\psi$, which exists because $\psi^\dagger$ does not transform with $D^{-1}$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]).

^der-cb-16-14

*Uses:* [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-5|Theorem §CB.4.5]]

## Descent to SO⁺(1,3)

> [!theorem] Theorem §CB.16.15: Which (j₊, j₋) Descend to SO⁺(1,3)
> $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2(j_+ + j_-)}\mathbb 1$. Hence $D^{(j_+, j_-)}$ is tensorial ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-23|Def. §CB.13.23]]), i.e. a representation of $SO^+(1,3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-15|Theorem §CB.9.15]]), iff $j_+ + j_- \in \mathbb Z$, and spinorial iff $j_+ + j_- \in \frac12 + \mathbb Z$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4, through [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], Derivation, step 6 · written here*

^thm-cb-16-15

> [!proof]- Proof
> **1. The value on −1.** $\operatorname{Sym}^{2j}(-\mathbb 1)$ is $(-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$ restricted to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]]), and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. So $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2j_+}\mathbb 1\otimes(-1)^{2j_-}\mathbb 1 = (-1)^{2(j_+ + j_-)}\mathbb 1$.
>
> **2. Tensorial or spinorial.** Under $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ the element $-1$ goes to $-\mathbb 1$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-12|Theorem §CB.15.12]], 1, for either identification $\phi$ or $\theta\circ\phi$). $2(j_+ + j_-)$ is an integer; $(-1)^{2(j_+ + j_-)} = 1$ iff it is even, i.e. $j_+ + j_- \in \mathbb Z$ (tensorial, [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-23|Def. §CB.13.23]]), and $= -1$ iff $j_+ + j_- \in \frac12 + \mathbb Z$ (spinorial).
>
> **3. Descent.** $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ is a surjective covering homomorphism with kernel $\{\pm\mathbb 1\}$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]), as is $\rho$ on $\mathrm{Spin}(1,3)_0$ (Theorem §CB.15.12, 2). By the descent lemma ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-15|Theorem §CB.9.15]]) $D^{(j_+, j_-)}$ is $D\circ\pi$ for a representation $D$ of $SO^+(1,3)$ iff $D^{(j_+, j_-)}(-\mathbb 1) = \mathbb 1$, i.e. iff $j_+ + j_- \in \mathbb Z$, and then $D$ is irreducible.
>
> **What the proof shows**
> - The sign is the parity of the total number $2j_+ + 2j_-$ of spinor slots, each slot contributing one factor $-1$.

^pf-cb-16-15

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-15|Theorem §CB.9.15]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-23|Def. §CB.13.23]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-12|Theorem §CB.15.12]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]

> [!remark]- Connections
> - The conjugation that exchanges the two $\mathfrak{sl}(2, \mathbb C)$ summands ([[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-1|Theorem §CB.5.1]], 3) is, on the group, $\lambda \mapsto (\lambda^\dagger)^{-1}$, the same map that relates the two factors of $D^{(j_+, j_-)}$ and the two Weyl matrices $\Lambda_L$, $\Lambda_R$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]).
> - The sign $(-1)^{2(j_+ + j_-)}$ of a $2\pi$ rotation is the value of a representation on the kernel $\{\pm\mathbb 1\}$ of the covering map, and the endpoint of the lift of the $2\pi$ loop: algebra (§C3.2), topology (§C3.1) and the explicit group meet here — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]].
> - **Used in**: Theorems §CB.16.1–§CB.16.7 — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3|Theorem §CB.5.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]; Theorem §CB.16.9 — [[§C1b.1 Fields and Their Transformation Laws|§C1b.1]] (embedded; cited in [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]), [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation|§C3.5]] (embedded; cited in [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); Theorem §CB.16.15 — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]; Theorem §CB.16.12 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (embedded; cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-4|§C5a.0, Remark: Why not two-component spinors?]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]), [[§C9.2★ Parity of the Scalar Field|§C9.2★]] (cited in [[§C9.2★ Parity of the Scalar Field#^rem-c9-2-9|§C9.2, Remark: Correspondence with Yu §9.1.1]]); Theorem §CB.16.13 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, Remark: A Majorana mass needs no second field]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]); Definition §CB.16.2 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded; cited in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]), [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§C1b.1 Fields and Their Transformation Laws|§C1b.1]] (cited in [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-2|§C1b.1, Remark: Two representations at once]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (cited in [[§C3.6★ Particle States and the Little Group#^rem-c3-6-5|§C3.6, Remark: What a field must contain]]); Theorem §CB.16.4 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded; cited in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]); Theorem §CB.16.5 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded); Theorem §CB.16.8 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-4|Theorem §C5a.9.4]]), [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^ex-c3-1-1|Example §C3.1.1]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (cited in [[§C3.6★ Particle States and the Little Group#^rem-c3-6-5|§C3.6, Remark: What a field must contain]]), [[§C3.3 Primitive and Traceless Moments|EM §C3.3]] (cited in [[§C3.3 Primitive and Traceless Moments#^thm-c3-3-4|EM Theorem §C3.3.4]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (cited in the text); Theorem §CB.16.10 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded; cited in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]); §CB.16, Remark: What the labels (j₊, j₋) mean — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded); Theorem §CB.16.14 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded; cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]] (embedded; cited in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded), [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-22|Theorem §CB.13.22]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]), [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^rem-cb-15-1|§CB.15, Remark: The rotation story, one level up]], [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded; cited in [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-1|§C3.3, Remark: Three realizations of one algebra]], [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]); Theorem §CB.16.11 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]).
