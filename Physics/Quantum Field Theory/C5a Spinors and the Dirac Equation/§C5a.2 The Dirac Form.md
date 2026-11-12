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

Which pairing of two spinors does the Clifford structure single out, and what does it allow one to do with a change of basis? [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] gave spinor space $V$, its bases (layer 1) and the Clifford action $\Gamma^\mu$ with its Hermitian bases and Pauli's theorem (layer 2). This section adds **layer 3**, a Hermitian form on $V$: the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$, the form for which every $\Gamma^\mu$ is self-adjoint, unique up to a real factor and of signature $(2, 2)$. Its partial evaluation $h_D(\psi, \cdot\,)$ is the Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$, and requiring that the formula $\psi^\dagger\gamma^0\chi$ keep computing it restricts the allowed changes of basis to unitary ones. The layer needs $\gamma^0$ and the Clifford algebra only; why this form, and not $\psi^\dagger\psi$, is the right one for relativity is the Lorentz invariance proved in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] once the Lorentz action exists ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). This section states Hermiticity in the course's chiral basis, the Dirac conjugate $\bar\psi$ with the form behind it, and which changes of basis keep its formula; Hermitian forms and the Dirac form as a form on a Clifford module are mathematics, proved in [[§CB.9 Hermitian Forms, Signature and Pseudo-Unitary Groups|§CB.9]] and [[§CB.13 Complex Clifford Algebras and Clifford Modules|§CB.13]], linked from each box and listed at the end.

**Setup.** As in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]: no field and no dynamics; the Dirac form, the Dirac conjugate and the changes of basis are linear algebra on $V$, exact, and apply to any spinor, classical field values, c-number spinors and the components of the quantum field alike (its conjugate $\hat{\bar\psi} = \hat\psi^\dagger\gamma^0$: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]). The boxes carry no *Model* line.

*Conventions* as in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; Hermitian forms are conjugate-linear in the first slot and linear in the second (the physics order; Axler's is the reverse, [[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]).

## Hermiticity in the chiral basis

> [!theorem] Theorem §C5a.2.1: Hermiticity of the Dirac Matrices
> 1. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$, equivalently $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; each $\gamma^\mu$ is unitary.
> 2. The same holds in any basis in which each $\gamma^\mu$ is a normal matrix, and in particular in any basis reached from the chiral one by a unitary matrix.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", eq. (gammadagger)) · Yu §5.1, eqs. (5.4)–(5.7) · the user's pre-course notes, §5.1 ("Hermiticity"; "hypothesis … arrangeable by a change of basis") · PHY 513, Problem Set 5, Problem 5(b) (the chiral-basis check, as the user wrote it)*

^thm-c5a-2-1

> [!derivation]- Derivation
> **1. Chiral basis.** $\gamma^{0\dagger}$: transposing $\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ and conjugating gives itself. $\gamma^{i\dagger} = \begin{pmatrix}0&(-\sigma^i)^\dagger\\(\sigma^i)^\dagger&0\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix} = -\gamma^i$, the Pauli matrices being Hermitian ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
>
> **2. The compact form.** $\gamma^0\gamma^0\gamma^0 = \gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], 1); $\gamma^0\gamma^i\gamma^0 = -\gamma^i\gamma^0\gamma^0 = -\gamma^i$ (anticommute, then $(\gamma^0)^2 = \mathbb 1$). So $\gamma^0\gamma^\mu\gamma^0$ equals $\gamma^{\mu\dagger}$ for every $\mu$.
>
> **3. Unitarity.** $\gamma^{0\dagger}\gamma^0 = (\gamma^0)^2 = \mathbb 1$, $\gamma^{i\dagger}\gamma^i = -(\gamma^i)^2 = \mathbb 1$.
>
> **4. Normal matrices.** If $\gamma^\mu$ is normal, it is $W\operatorname{diag}(d_1, \dots, d_n)W^\dagger$ with $W$ unitary (spectral theorem). Then $(\gamma^\mu)^2 = W\operatorname{diag}(d_k^2)W^\dagger = g^{\mu\mu}\mathbb 1$ forces $d_k^2 = g^{\mu\mu}$: $d_k = \pm1$ for $\mu = 0$, $d_k = \pm i$ for $\mu = i$. Real eigenvalues make $\gamma^0 = W\operatorname{diag}(d_k)W^\dagger$ Hermitian; imaginary ones make $\gamma^i$ anti-Hermitian, $(W\operatorname{diag}(d_k)W^\dagger)^\dagger = W\operatorname{diag}(d_k^{\ast})W^\dagger = -\gamma^i$. (One $W$ per matrix: the four are not simultaneously diagonalizable, since they anticommute.)
>
> **5. Unitary changes of basis.** If $\gamma'^\mu = U\gamma^\mu U^\dagger$ with $U$ unitary, then $\gamma'^{\mu\dagger} = U\gamma^{\mu\dagger}U^\dagger = U\gamma^0\gamma^\mu\gamma^0U^\dagger = \gamma'^0\gamma'^\mu\gamma'^0$, inserting $U^\dagger U = \mathbb 1$ between the factors.
>
> **What the derivation shows**
> - Hermiticity is not part of the Clifford algebra: a non-unitary change of basis preserves the algebra ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]], 1) but destroys it. It is a choice of basis, assumed from here on; in Yu and the pre-course notes it enters as the hypothesis "normal".
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ is the identity used for every adjoint in Dirac theory: the generators ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 1), $\bar\psi$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]; proof [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]]), the reality of bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]).

^der-c5a-2-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## The Dirac form and the Dirac conjugate

> [!definition] Definition §C5a.2.1: The Dirac Form
> In a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]; as mathematics [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-11|Def. §CB.13.11]]), the **Dirac form** is the Hermitian form on $V$
>
> $$
> h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi ,
> $$
>
> with matrix $\gamma^0$ (as mathematics [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-15|Def. §CB.13.15]]): conjugate-linear in $\chi$ and linear in $\psi$. That this form is Lorentz invariant is [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$: $\gamma^0$ for Dirac spinors") · PS §3.2, p. 43, eq. (3.32) (the pairing $\psi^\dagger\gamma^0\psi$) · the form-theoretic formulation written here*

^def-c5a-2-1

> [!definition] Definition §C5a.2.2: The Dirac Conjugate
> The **Dirac conjugate** of a Dirac spinor (or field) $\psi$ is the row
>
> $$
> \bar\psi \equiv \psi^\dagger\gamma^0 .
> $$
>
> It is not the Hermitian conjugate: the extra $\gamma^0$ is essential. Here $\gamma^0$ is the matrix of the Dirac form $h_D$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]), so $\bar\chi\psi = h_D(\chi, \psi)$. Basis-free, $\bar\psi$ is the linear functional $h_D(\psi, \cdot\,) \in V'$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]]), and $\psi \mapsto \bar\psi$ is conjugate-linear.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Definition "The Dirac conjugate", eq. (psibar)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.32) · Yu §5.3, eq. (5.90) · the functional reading written here*

^def-c5a-2-2

The components of $\bar\psi$: $\bar\psi(\chi) = h_D(\psi, \chi) = \sum_b(\psi^\dagger\gamma^0)_b\chi_b$, so by Def. §CB.0.6 its row is $\psi^\dagger\gamma^0$; conjugate-linearity is $(\lambda\psi)^\dagger = \lambda^{\ast}\psi^\dagger$.

> [!theorem] Theorem §C5a.2.2: The Dirac Form Is Fixed by the γ's up to a Real Factor and Has Signature (2, 2)
> In a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]), let $h_D(\chi, \psi) = \bar\chi\psi = \chi^\dagger\gamma^0\psi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]).
> 1. Every $\gamma^\mu$ is self-adjoint for $h_D$: $h_D(\gamma^\mu\chi, \psi) = h_D(\chi, \gamma^\mu\psi)$, i.e. $\overline{\gamma^\mu\chi} = \bar\chi\gamma^\mu$.
> 2. Conversely, if $h(\chi, \psi) = \chi^\dagger H\psi$ is a nondegenerate Hermitian form for which every $\gamma^\mu$ is self-adjoint, then $H = c\,\gamma^0$ with $c$ real, $c \ne 0$: up to normalization, $\bar\psi = \psi^\dagger\gamma^0$ is the only pairing of two spinors compatible with the $\gamma$'s.
> 3. $h_D$ has signature $(2, 2)$: $\gamma^0$ has eigenvalues $+1, +1, -1, -1$, so $\bar\psi\psi$ takes both signs and is not a norm; in the chiral basis $\bar\psi\psi = \psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L$.
>
> How to read it: the Clifford structure leaves no freedom in how two spinors are paired beyond a real factor (fixed to $1$ by convention), and the pairing it gives is indefinite, a pairing and not a probability.
>
> *Proof:* [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-16|Theorem §CB.13.16]] (parts 1–2), [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-17|Theorem §CB.13.17]] (part 3); the chiral form in part 3 is the block product with $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]).
>
> *Source: PS §3.2, p. 43, eq. (3.32) ($\bar\psi \equiv \psi^\dagger\gamma^0$, introduced because $\psi^\dagger\psi$ is not invariant) · Yu §5.1, eqs. (5.6)–(5.7) ($\gamma^0$ Hermitian, $\gamma^i$ anti-Hermitian, both unitary) · the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$") · the self-adjointness reading and the uniqueness written here*

^thm-c5a-2-2

## Which changes of basis preserve the Dirac conjugate

> [!theorem] Theorem §C5a.2.3: Which Changes of Basis Preserve ψ̄
> Let $e$ be a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]; [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-11|Def. §CB.13.11]]), $U$ any invertible change-of-basis matrix ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]]), $\psi' = U\psi$, $\gamma'^\mu = U\gamma^\mu U^{-1}$, and $\bar\psi = \psi^\dagger\gamma^0$ the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]]).
> 1. The Dirac-conjugate formula applied in the new basis computes the same $\bar\psi\chi$, $\psi'^\dagger\gamma'^0\chi' = \bar\psi\chi$ for all $\psi, \chi$, iff $U$ is unitary; a new Hermitian basis with $U^\dagger U = c\,\mathbb 1$ multiplies it by $c$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-18|Theorem §CB.13.18]]).
> 2. For unitary $U$: $\psi'^\dagger = \psi^\dagger U^{-1}$, $\bar\psi' = \bar\psi\,U^{-1}$, and every bilinear $\bar\psi M\chi$ with $M \in \operatorname{End}(V)$ ($M' = UMU^{-1}$) is unchanged.
>
> So $\bar\psi = \psi^\dagger\gamma^0$ defines the same object in all Hermitian bases related by unitary matrices, and not otherwise.
>
> *Source: PS §3.2, p. 41 ("unitarily equivalent") · Yu §5.2, eq. (5.72) (unitary $U$) · the user's pre-course notes, §5.2 ("all representations are related by unitary similarity transformations") · parts 1–2 and the converses written here*

^thm-c5a-2-3

> [!derivation]- Derivation
> **1. Part 1** is Theorem §CB.13.18 read for $\bar\psi = \psi^\dagger\gamma^0$: the number $\psi'^\dagger\gamma'^0\chi'$ is the Dirac conjugate formula in the new basis.
>
> **2. Part 2.** With $U^\dagger = U^{-1}$: $\psi'^\dagger = \psi^\dagger U^{-1}$; $\bar\psi' = \psi'^\dagger\gamma'^0 = \psi^\dagger U^{-1}U\gamma^0U^{-1} = \bar\psi U^{-1}$; $\bar\psi'M'\chi' = \bar\psi U^{-1}UMU^{-1}U\chi = \bar\psi M\chi$.
>
> **What the derivation shows**
> - In the language of the slot rule ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], 3): a unitary $U$ makes the conjugate slot of $\psi^\dagger$ transform like a $V'$-slot, and the two roles of $\gamma^0$ (operator and form, Theorem §CB.9.2) transform alike.
> - Used next: the Dirac Lagrangian is basis independent exactly for unitary $U$ (Theorem §C5a.7.5).

^der-c5a-2-3

*Uses:* [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-18|Theorem §CB.13.18]], [[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]

> [!remark] Remark: γ⁰ in two roles
> The matrix $\gamma^0$ appears in two different jobs. As the matrix of the Dirac map $\Gamma^0$ it is an operator, slots $V\otimes V'$, and transforms as $U\gamma^0U^{-1}$; it enters the Dirac equation $i\gamma^0\partial_0\psi + \dots$. As the matrix of the Dirac form it pairs two spinors, $\bar\chi\psi = \chi^\dagger\gamma^0\psi$, and transforms as $(U^{-1})^\dagger\gamma^0U^{-1}$ (Theorem §CB.9.2). In a Hermitian basis the two arrays coincide; after a non-unitary change of basis they differ, and the formula $\bar\psi = \psi^\dagger\gamma^0$, which silently identifies them, stops computing the Dirac form (Theorem §C5a.2.3, 1). The same double role is played by $g_{\mu\nu}$ for vectors in an orthonormal frame, and the same caution applies to non-orthonormal frames. Under Lorentz transformations the form role is the one preserved: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]; [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], 2).
>
> *Source: written here · the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$: $\gamma^0$ for Dirac spinors")*

^rem-c5a-2-1

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> Hermiticity below uses the squares and the anticommutation of the Dirac matrices:
> - [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]] with [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-11-12|Derivation]] — squares and anticommutation ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]).
>
> Layer 3 is a Hermitian form on spinor space: a Hermitian form, its matrix, how it changes with the basis, and its signature:
> - [[§CB.9 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-9-1|Def. §CB.9.1]] — Hermitian form and its matrix (the Dirac form of Def. §C5a.2.1 is one).
> - [[§CB.9 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-9-2|Theorem §CB.9.2]] with [[§CB.9 Hermitian Forms, Signature and Pseudo-Unitary Groups#^der-cb-9-2|Derivation]] — $H' = (U^{-1})^\dagger HU^{-1}$, which agrees with the operator rule iff $U$ is unitary (Remark: γ⁰ in two roles).
> - [[§CB.9 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-9-3|Def. §CB.9.3]] — signature of a Hermitian form.
>
> In a Hermitian basis, which Theorem §C5a.2.1 shows the chiral basis to be, the Dirac form is defined; the Dirac maps fix it up to a real factor, and it has signature (2, 2):
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-11|Def. §CB.13.11]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-15|Def. §CB.13.15]] — Hermitian basis; the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$ (Def. §C5a.2.1).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-16|Theorem §CB.13.16]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^der-cb-13-16|Derivation]] — the Dirac maps are self-adjoint for $h_D$ and fix it up to a real factor; physics form: [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]].
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-17|Theorem §CB.13.17]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^der-cb-13-17|Derivation]] — $h_D$ has signature $(2, 2)$: $\bar\psi\psi$ is indefinite; physics form: [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]].
>
> The Dirac conjugate below is the partial evaluation of the form, a dual spinor:
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]] — dual spinor space and dual basis ($\bar\psi \in V'$, Def. §C5a.2.2).
>
> Theorem §C5a.2.3 combines the change-of-basis rules, Pauli's theorem (part 2: Hermitian bases are related by unitary matrices) and the theorem on the Dirac form under a change of basis:
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]] with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-5|Derivation]] — the change-of-basis matrix; $\psi' = U\psi$, $M' = UMU^{-1}$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|Theorem §CB.13.12]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^der-cb-13-12|Derivation]] — Pauli's theorem; two Hermitian bases are related by a unitary matrix ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]], 2).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-18|Theorem §CB.13.18]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^der-cb-13-18|Derivation]] — which changes of basis preserve the Dirac form (Theorem §C5a.2.3, 1).
>
> Used next (Derivation §C5a.2.1, last bullet, and the Connections): the Lorentz invariance of the form defined here:
> - [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]] — $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$: the Dirac form is Lorentz invariant ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]].

> [!remark]- Connections
> - The Dirac form is the invariant form of the spinor slot as $g$ is that of the vector slot and $\varepsilon$ that of a Weyl slot; its indefiniteness, signature $(2, 2)$, is the spinor face of the non-unitarity of finite-dimensional Lorentz representations — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-7|Theorem §C3.2.7]].
> - The reality of bilinears and the self-adjointness of the Dirac maps for the Dirac form are one identity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]].
> - Unitary changes of basis are those that keep the reference inner product $\psi^\dagger\chi$ of the columns; the Dirac form needs them although it is not itself an inner product, as Quantum Mechanics needs them to keep probabilities — [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-1|QM Theorem §C1.4.1]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]].
> - The Dirac conjugate defined here is what the Lagrangian, every bilinear and the canonical momentum $\pi = i\psi^\dagger$ are built from — [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]], [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-1|Theorem §C5a.9.1]].
