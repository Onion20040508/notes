---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.1 Spinor Space and the Clifford Action]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.3 The Lorentz Action on Spinor Space]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices"), §8.3 ("The practical test, continued": "Each spinor slot has its own invariant form in place of $g$"), §8.7 (Definition "The Dirac conjugate") · PHY 513 Lecture 8, Part B · Peskin & Schroeder, §3.2, pp. 41, 43, eq. (3.32) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.4)–(5.7), §5.2, eq. (5.72), §5.3, eq. (5.90) · the user's pre-course notes, §5.1 ("Hermiticity"), §5.2 ("all representations are related by unitary similarity transformations") · Axler (the vault's Linear Algebra notes), linked where used · the form-theoretic formulation written here.*

Which pairing of two spinors does the Clifford structure single out, and what does it allow one to do with a change of basis? [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] gave spinor space $V$, its bases (layer 1) and the Clifford action $\Gamma^\mu$ with its Hermitian bases and Pauli's theorem (layer 2). This section adds **layer 3**, a Hermitian form on $V$: the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$, the form for which every $\Gamma^\mu$ is self-adjoint, unique up to a real factor and of signature $(2, 2)$. Its partial evaluation $h_D(\psi, \cdot\,)$ is the Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$, and requiring that the formula $\psi^\dagger\gamma^0\chi$ keep computing it restricts the allowed changes of basis to unitary ones. The layer needs $\gamma^0$ and the Clifford algebra only; why this form, and not $\psi^\dagger\psi$, is the right one for relativity is the Lorentz invariance proved in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] once the Lorentz action exists ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). Hermitian forms and the Dirac form as a form on a Clifford module are mathematics ([[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups|§CB.8]], [[§CB.12 Complex Clifford Algebras and Clifford Modules|§CB.12]]), shown in the blocks below; this section keeps Hermiticity in the course's chiral basis, the Dirac conjugate $\bar\psi$ and which changes of basis keep its formula.

*Conventions* as in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; Hermitian forms are conjugate-linear in the first slot and linear in the second (the physics order; Axler's is the reverse, [[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]).

## The mathematics used here

Hermiticity below uses the squares and the anticommutation of the Dirac matrices:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-12]]

Layer 3 is a Hermitian form on spinor space: a Hermitian form, its matrix, how it changes with the basis, and its signature:

![[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-8-1]]

![[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-8-2]]

![[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups#^der-cb-8-2]]

![[§CB.8 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-8-3]]

## Hermiticity in the chiral basis

> [!theorem] Theorem §C5a.2.1: Hermiticity of the Dirac Matrices
> 1. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$, equivalently $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; each $\gamma^\mu$ is unitary.
> 2. The same holds in any basis in which each $\gamma^\mu$ is a normal matrix, and in particular in any basis reached from the chiral one by a unitary matrix.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", eq. (gammadagger)) · Yu §5.1, eqs. (5.4)–(5.7) · the user's pre-course notes, §5.1 ("Hermiticity"; "hypothesis … arrangeable by a change of basis") · PHY 513, Problem Set 5, Problem 5(b) (the chiral-basis check, as the user wrote it)*

^thm-c5a-2-1

> [!derivation]- Derivation
> **1. Chiral basis.** $\gamma^{0\dagger}$: transposing $\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ and conjugating gives itself. $\gamma^{i\dagger} = \begin{pmatrix}0&(-\sigma^i)^\dagger\\(\sigma^i)^\dagger&0\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix} = -\gamma^i$, the Pauli matrices being Hermitian ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
>
> **2. The compact form.** $\gamma^0\gamma^0\gamma^0 = \gamma^0$ (Theorem §CB.10.12); $\gamma^0\gamma^i\gamma^0 = -\gamma^i\gamma^0\gamma^0 = -\gamma^i$ (anticommute, then $(\gamma^0)^2 = \mathbb 1$). So $\gamma^0\gamma^\mu\gamma^0$ equals $\gamma^{\mu\dagger}$ for every $\mu$.
>
> **3. Unitarity.** $\gamma^{0\dagger}\gamma^0 = (\gamma^0)^2 = \mathbb 1$, $\gamma^{i\dagger}\gamma^i = -(\gamma^i)^2 = \mathbb 1$.
>
> **4. Normal matrices.** If $\gamma^\mu$ is normal, it is $W\operatorname{diag}(d_1, \dots, d_n)W^\dagger$ with $W$ unitary (spectral theorem). Then $(\gamma^\mu)^2 = W\operatorname{diag}(d_k^2)W^\dagger = g^{\mu\mu}\mathbb 1$ forces $d_k^2 = g^{\mu\mu}$: $d_k = \pm1$ for $\mu = 0$, $d_k = \pm i$ for $\mu = i$. Real eigenvalues make $\gamma^0 = W\operatorname{diag}(d_k)W^\dagger$ Hermitian; imaginary ones make $\gamma^i$ anti-Hermitian, $(W\operatorname{diag}(d_k)W^\dagger)^\dagger = W\operatorname{diag}(d_k^{\ast})W^\dagger = -\gamma^i$. (One $W$ per matrix: the four are not simultaneously diagonalizable, since they anticommute.)
>
> **5. Unitary changes of basis.** If $\gamma'^\mu = U\gamma^\mu U^\dagger$ with $U$ unitary, then $\gamma'^{\mu\dagger} = U\gamma^{\mu\dagger}U^\dagger = U\gamma^0\gamma^\mu\gamma^0U^\dagger = \gamma'^0\gamma'^\mu\gamma'^0$, inserting $U^\dagger U = \mathbb 1$ between the factors.
>
> **What the derivation shows**
> - Hermiticity is not part of the Clifford algebra: a non-unitary change of basis preserves the algebra (Theorem §CB.12.12) but destroys it. It is a choice of basis, assumed from here on; in Yu and the pre-course notes it enters as the hypothesis "normal".
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ is the identity used for every adjoint in Dirac theory: the generators (Theorem §CB.13.22), $\bar\psi$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]]), the reality of bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]).

^der-c5a-2-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12|Theorem §CB.10.12]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

### The mathematics used here: the Dirac form

In a Hermitian basis, which Theorem §C5a.2.1 shows the chiral basis to be, the Dirac form is defined; the Dirac maps fix it up to a real factor, and it has signature (2, 2):

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-11]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-15]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-16]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-16]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-17]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-17]]

The Dirac conjugate below is the partial evaluation of the form, a dual spinor:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6]]

## The Dirac conjugate

> [!definition] Definition §C5a.2.1: The Dirac Conjugate
> The **Dirac conjugate** of a Dirac spinor (or field) $\psi$ is the row
>
> $$
> \bar\psi \equiv \psi^\dagger\gamma^0 .
> $$
>
> It is not the Hermitian conjugate: the extra $\gamma^0$, the matrix of the Dirac form ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-15|Def. §CB.12.15]]), is essential; that this form is Lorentz invariant is [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]] (§C5a.6). Basis-free, $\bar\psi$ is the linear functional $h_D(\psi, \cdot\,) \in V'$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]]), and $\psi \mapsto \bar\psi$ is conjugate-linear.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Definition "The Dirac conjugate", eq. (psibar)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.32) · Yu §5.3, eq. (5.90) · the functional reading written here*

^def-c5a-2-1

The components of $\bar\psi$: $\bar\psi(\chi) = h_D(\psi, \chi) = \sum_b(\psi^\dagger\gamma^0)_b\chi_b$, so by Def. §CB.0.6 its row is $\psi^\dagger\gamma^0$; conjugate-linearity is $(\lambda\psi)^\dagger = \lambda^{\ast}\psi^\dagger$.

### The mathematics used here: changes of basis

Theorem §C5a.2.2 combines the change-of-basis rules, Pauli's theorem (part 2: Hermitian bases are related by unitary matrices) and the theorem on the Dirac form under a change of basis:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-5]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-18]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-18]]

## Which changes of basis preserve the Dirac conjugate

> [!theorem] Theorem §C5a.2.2: Which Changes of Basis Preserve ψ̄
> Let $e$ be a Hermitian basis ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-11|Def. §CB.12.11]]), $U$ any invertible change-of-basis matrix ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]]), $\psi' = U\psi$, $\gamma'^\mu = U\gamma^\mu U^{-1}$, and $\bar\psi = \psi^\dagger\gamma^0$ the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]).
> 1. The Dirac-conjugate formula applied in the new basis computes the same $\bar\psi\chi$, $\psi'^\dagger\gamma'^0\chi' = \bar\psi\chi$ for all $\psi, \chi$, iff $U$ is unitary; a new Hermitian basis with $U^\dagger U = c\,\mathbb 1$ multiplies it by $c$ ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-18|Theorem §CB.12.18]]).
> 2. For unitary $U$: $\psi'^\dagger = \psi^\dagger U^{-1}$, $\bar\psi' = \bar\psi\,U^{-1}$, and every bilinear $\bar\psi M\chi$ with $M \in \operatorname{End}(V)$ ($M' = UMU^{-1}$) is unchanged.
>
> So $\bar\psi = \psi^\dagger\gamma^0$ defines the same object in all Hermitian bases related by unitary matrices, and not otherwise.
>
> *Source: PS §3.2, p. 41 ("unitarily equivalent") · Yu §5.2, eq. (5.72) (unitary $U$) · the user's pre-course notes, §5.2 ("all representations are related by unitary similarity transformations") · parts 1–2 and the converses written here*

^thm-c5a-2-2

> [!derivation]- Derivation
> **1. Part 1** is Theorem §CB.12.18 read for $\bar\psi = \psi^\dagger\gamma^0$: the number $\psi'^\dagger\gamma'^0\chi'$ is the Dirac conjugate formula in the new basis.
>
> **2. Part 2.** With $U^\dagger = U^{-1}$: $\psi'^\dagger = \psi^\dagger U^{-1}$; $\bar\psi' = \psi'^\dagger\gamma'^0 = \psi^\dagger U^{-1}U\gamma^0U^{-1} = \bar\psi U^{-1}$; $\bar\psi'M'\chi' = \bar\psi U^{-1}UMU^{-1}U\chi = \bar\psi M\chi$.
>
> **What the derivation shows**
> - In the language of the slot rule (Theorem §CB.0.10): a unitary $U$ makes the conjugate slot of $\psi^\dagger$ transform like a $V'$-slot, and the two roles of $\gamma^0$ (operator and form, Theorem §CB.8.2) transform alike.
> - Used next: the Dirac Lagrangian is basis independent exactly for unitary $U$ (Theorem §C5a.7.5).

^der-c5a-2-2

*Uses:* [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-18|Theorem §CB.12.18]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]

> [!remark] Remark: γ⁰ in two roles
> The matrix $\gamma^0$ appears in two different jobs. As the matrix of the Dirac map $\Gamma^0$ it is an operator, slots $V\otimes V'$, and transforms as $U\gamma^0U^{-1}$; it enters the Dirac equation $i\gamma^0\partial_0\psi + \dots$. As the matrix of the Dirac form it pairs two spinors, $\bar\chi\psi = \chi^\dagger\gamma^0\psi$, and transforms as $(U^{-1})^\dagger\gamma^0U^{-1}$ (Theorem §CB.8.2). In a Hermitian basis the two arrays coincide; after a non-unitary change of basis they differ, and the formula $\bar\psi = \psi^\dagger\gamma^0$, which silently identifies them, stops computing the Dirac form (Theorem §C5a.2.2, 1). The same double role is played by $g_{\mu\nu}$ for vectors in an orthonormal frame, and the same caution applies to non-orthonormal frames. Under Lorentz transformations the form role is the one preserved: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]]).
>
> *Source: written here · the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$: $\gamma^0$ for Dirac spinors")*

^rem-c5a-2-1

> [!remark]- Connections
> - The Dirac form is the invariant form of the spinor slot as $g$ is that of the vector slot and $\varepsilon$ that of a Weyl slot; its indefiniteness, signature $(2, 2)$, is the spinor face of the non-unitarity of finite-dimensional Lorentz representations — [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]].
> - The reality of bilinears and the self-adjointness of the Dirac maps for the Dirac form are one identity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]].
> - Unitary changes of basis are those that keep the reference inner product $\psi^\dagger\chi$ of the columns; the Dirac form needs them although it is not itself an inner product, as Quantum Mechanics needs them to keep probabilities — [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-1|QM Theorem §C1.4.1]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]].
> - The Dirac conjugate defined here is what the Lagrangian, every bilinear and the canonical momentum $\pi = i\psi^\dagger$ are built from — [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|Theorem §C5a.8.1]].
