---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): the user's PHY 513 notes, Ch. 7 §7.2 · PHY 513 Lecture 7 · Yu Zhao-Huan, 量子场论讲义, §§3.2–3.3.1 · Quantum Mechanics §C5.2, §C5.3, §C7.1 · Differentiable Manifolds (591) §§40–41 · Group Theory (493) §§38–41 · P. Woit, Quantum Theory, Groups and Representations, Ch. 8 (§8.1 classification, §8.2 construction), §9.4 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

What are all finite-dimensional representations of SU(2) and SO(3), how are they built from spin ½, and how do they multiply? The course classifies the irreducible representations of the rotation algebra by highest weight and integrates them to SU(2) and SO(3) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]); Quantum Mechanics adds angular momenta ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). This section puts these in the language of §CB.2–§CB.4: $\mathfrak{sl}(2, \mathbb C)$ and weights, complete reducibility, spin $j$ as the symmetric power $\operatorname{Sym}^{2j}\mathbb C^2$, the Clebsch–Gordan series as a statement about tensor products, and the descent lemma that decides which representations of a covering group are representations of the quotient. The three-dimensional Clifford picture of the same objects is [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]].

<!-- MOVE row (CB-INVENTORY): Remark "Spin j is 2j symmetrized spin-½ slots" (rem-c3-1-6) is embedded below; it is to be moved here in batch 4 and upgraded to Theorem §CB.6.5 with proof. -->

## 𝔰𝔩(2,ℂ) and weights

> [!definition] Definition §CB.6.1: The Standard Basis of 𝔰𝔩(2,ℂ)
> The **standard basis** of $\mathfrak{sl}(2, \mathbb C)$ is
>
> $$
> H = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}, \quad E = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \quad F = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix}, \qquad [H, E] = 2E, \quad [H, F] = -2F, \quad [E, F] = H .
> $$
>
> Under $\mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]) and complex-linear extension of a representation ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]): $H = 2J^3$, $E = J^+$, $F = J^-$ in the physicists' generators of the defining representation.
>
> *Source (planned): Woit, §8.1 · written here*

^def-cb-6-1

> [!definition] Definition §CB.6.2: Weight and Weight Space
> For a representation of $\mathfrak{sl}(2, \mathbb C)$ (equivalently of $\mathfrak{su}(2)$) on $W$, the **weight space** of weight $m \in \mathbb C$ is $W_m = \{w : J^3w = mw\}$, $J^3 = \frac12H$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-1|Def. §CB.6.1]]); $m$ is a **weight** if $W_m \ne 0$, and $\dim W_m$ is its **multiplicity**.
>
> *Source (planned): Woit, §8.1 · written here*

^def-cb-6-2

> [!theorem] Theorem §CB.6.3: Finite-Dimensional Representations of 𝔰𝔩(2,ℂ)
> Let $W$ be a finite-dimensional complex-linear representation of $\mathfrak{sl}(2, \mathbb C)$. Then:
> 1. $W$ is completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]) and $J^3$ is diagonalizable: $W = \bigoplus_mW_m$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-6-2|Def. §CB.6.2]]);
> 2. every weight lies in $\frac12\mathbb Z$, and $J^\pm W_m \subset W_{m\pm1}$;
> 3. the irreducible ones are the $V_j$ of the course's classification ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]), with weights $j, j-1, \dots, -j$, each of multiplicity one.
>
> *Source (planned): Woit, §8.1 · the user's PHY 513 notes, Ch. 7 §7.2*

^thm-cb-6-3

> [!proof]- Proof (to be filled)
> *To be filled (part 1 from Theorem §CB.3.15 with $K = SU(2)$, and $J^3$ Hermitian in an invariant inner product, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-13|Theorem §CB.3.13]]; parts 2–3 from the highest-weight theorem below).*

^pf-cb-6-3

The highest-weight classification, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] (two routes):

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6]]

> [!theorem] Theorem §CB.6.4: Weight Multiplicities Determine a Representation
> Two finite-dimensional representations of $\mathfrak{sl}(2, \mathbb C)$ are equivalent iff their weight multiplicities agree. With $n_m = \dim W_m$, the number of summands $V_j$ in $W$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]]) is $n_j - n_{j+1}$.
>
> *Source (planned): Woit, §8.1 · written here*

^thm-cb-6-4

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-6-4

## Spin j as a symmetric power

The course realizes spin $j$ on polynomials of degree $2j$, and integrates to SU(2) and SO(3), in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6]]

> [!theorem] Theorem §CB.6.5: Spin j Is the Symmetric Power Sym²ʲℂ²
> For $j \in \frac12\mathbb Z_{\ge0}$, the restriction of $D^{\otimes2j}$ ($D$ the defining representation of $SU(2)$ or $SL(2, \mathbb C)$ on $\mathbb C^2$, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]) to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-11|Def. §CB.4.11]]) is irreducible and equivalent to $V_j$. The identification with homogeneous polynomials of degree $2j$, $P(z) = \psi_{a_1\cdots a_{2j}}z_{a_1}\cdots z_{a_{2j}}$, is an equivalence with the polynomial realization of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]; and $-\mathbb 1$ acts as $(-1)^{2j}$.
>
> *Source (planned): Woit, §8.2 · the user's PHY 513 notes, Ch. 7 §7.2 · written here*

^thm-cb-6-5

> [!proof]- Proof (to be filled)
> *To be filled (weights of $\operatorname{Sym}^{2j}\mathbb C^2$: $z_1^az_2^b$, $a + b = 2j$, has weight $\frac12(a - b)$, each once; Theorem §CB.6.4).*

^pf-cb-6-5

## The Clebsch–Gordan series

> [!theorem] Theorem §CB.6.6: Clebsch–Gordan Series
> For $j_1, j_2 \in \frac12\mathbb Z_{\ge0}$, as representations of $\mathfrak{sl}(2, \mathbb C)$, $SU(2)$ or $SL(2, \mathbb C)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]),
>
> $$
> V_{j_1}\otimes V_{j_2} \cong \bigoplus_{j = |j_1 - j_2|}^{j_1 + j_2}V_j \qquad (j \text{ in integer steps}) .
> $$
>
> *Source (planned): [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]] · Woit, §9.4*

^thm-cb-6-6

> [!proof]- Proof (to be filled)
> *To be filled (weights add under $\otimes$, Theorem §CB.4.3; count multiplicities and apply Theorem §CB.6.4). Quantum Mechanics proves the same series with explicit Clebsch–Gordan coefficients:*

^pf-cb-6-6

![[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2]]

## Descent to a quotient group

> [!theorem] Theorem §CB.6.7: Descent Lemma
> Let $p : \tilde G \to G$ be a surjective Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]) that is a covering map (e.g. Theorem §CB.1.23), with kernel $N$. A representation $\tilde D$ of $\tilde G$ is of the form $\tilde D = D\circ p$ for a representation $D$ of $G$ iff $\tilde D(n) = \mathbb 1$ for all $n \in N$; then $D$ is unique, and $D$ is irreducible iff $\tilde D$ is. Instances: $SU(2) \to SO(3)$ and $SL(2, \mathbb C) \to SO^+(1,3)$, $N = \{\pm\mathbb 1\}$, where the condition is $\tilde D(-\mathbb 1) = \mathbb 1$.
>
> *Source (planned): [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]] (the group part) · written here*

^thm-cb-6-7

> [!proof]- Proof
> **1. Necessity.** If $\tilde D = D\circ p$ and $n \in N$, then $\tilde D(n) = D(p(n)) = D(\mathbb 1) = \mathbb 1$.
>
> **2. Definition of D.** Suppose $\tilde D(N) = \{\mathbb 1\}$. For $g \in G$ pick $\tilde g$ with $p(\tilde g) = g$ ($p$ is onto) and put $D(g) = \tilde D(\tilde g)$. Another choice is $\tilde gn$ with $n \in N$ ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]]: $p(\tilde g') = p(\tilde g)$ iff $\tilde g^{-1}\tilde g' \in N$), and $\tilde D(\tilde gn) = \tilde D(\tilde g)\tilde D(n) = \tilde D(\tilde g)$; so $D$ is well defined. This is the first isomorphism theorem applied to $\tilde D$, whose kernel contains $N$ ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).
>
> **3. Homomorphism.** $p(\tilde g\tilde h) = gh$, so $D(gh) = \tilde D(\tilde g\tilde h) = \tilde D(\tilde g)\tilde D(\tilde h) = D(g)D(h)$, and $D(\mathbb 1) = \tilde D(\mathbb 1) = \mathbb 1$.
>
> **4. Continuity.** Near any $g \in G$ a covering map has a continuous local inverse $s$ (an evenly covered neighbourhood, [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]), and $D = \tilde D\circ s$ there, a composition of continuous maps.
>
> **5. Uniqueness and irreducibility.** $D(g)$ is forced to be $\tilde D(\tilde g)$, so $D$ is unique; and $D(G) = \tilde D(\tilde G)$ as sets of operators, so the invariant subspaces of $D$ and $\tilde D$ coincide.

^pf-cb-6-7

> [!theorem] Theorem §CB.6.8: Integer Spin Is Built from Vectors
> 1. $V_1$ is equivalent to the complexified vector representation of $SO(3)$ on $\mathbb C^3$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]).
> 2. For every integer $l \ge 0$, $V_l$ is equivalent to the space of traceless symmetric tensors in $\operatorname{Sym}^l\mathbb C^3$, a subrepresentation of $(\mathbb C^3)^{\otimes l}$. So every representation of $SO(3)$ is contained in a sum of tensor powers of the vector representation.
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.2 (four-vector example) · Woit, §8.3 · written here*

^thm-cb-6-8

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-6-8

The topology behind the descent, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8]]

> [!remark]- Connections
> - Theorem §CB.6.7 is the single mechanism behind three course theorems: integer spin integrates to SO(3) ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]), integer $(j_+, j_-)$ to $SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]), and the general tensor/spinor split ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]).
> - The Clebsch–Gordan series of Theorem §CB.6.6 is used copy by copy for the Lorentz group ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]]) and in the 3D and 4D versions of the TA's theorem (Theorem §CB.10.6, Theorem §CB.12.9).
> - **Used in**: Definitions §CB.6.1–§CB.6.2, Theorem §CB.6.3 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]] (step 4); Theorem §CB.6.5 — [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6|§C3.1, Remark: Spin j is 2j symmetrized spin-½ slots]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; Theorem §CB.6.6 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]]; Theorem §CB.6.7 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]; Theorem §CB.6.8 — [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]].
