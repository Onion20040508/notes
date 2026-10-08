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

Which pairing of two spinors does the Clifford structure single out, and what does it allow one to do with a change of basis? [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] gave spinor space $V$, its bases (layer 1) and the Clifford action $\Gamma^\mu$ with its Hermitian bases and Pauli's theorem (layer 2). This section adds **layer 3**, a Hermitian form on $V$: the Dirac form $h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi$, the form for which every $\Gamma^\mu$ is self-adjoint, unique up to a real factor and of signature $(2, 2)$. Its partial evaluation $h_D(\psi, \cdot\,)$ is the Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$, and requiring that the formula $\psi^\dagger\gamma^0\chi$ keep computing it restricts the allowed changes of basis to unitary ones. The layer needs $\gamma^0$ and the Clifford algebra only; why this form, and not $\psi^\dagger\psi$, is the right one for relativity is the Lorentz invariance proved in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] once the Lorentz action exists ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]).

*Conventions* as in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; Hermitian forms are conjugate-linear in the first slot and linear in the second (the physics order; Axler's is the reverse, [[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]).

## Hermitian forms

> [!definition] Definition §C5a.2.1: Hermitian Form and Its Matrix
> A **Hermitian form** on $V$ is a map $h : V\times V \to \mathbb C$ that is linear in the second argument, conjugate-linear in the first, and satisfies $h(\chi, \psi) = h(\psi, \chi)^{\ast}$. It is **nondegenerate** if $h(\chi, \psi) = 0$ for all $\chi$ implies $\psi = 0$. Its **matrix** in a basis $e$ is $H_{ab} = h(e_a, e_b)$. An inner product is a positive-definite Hermitian form ([[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]], which puts the linear slot first; the physics order is used here).
>
> *Source: LADR Def. 6.2 and its Remark "Convention warning (physics)" · LADR Def. 9.4 (the matrix of a bilinear form, the real analogue) · written here for the indefinite case*

^def-c5a-2-1

> [!theorem] Theorem §C5a.2.1: How a Hermitian Form Changes with the Basis
> For a Hermitian form $h$ with matrix $H$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]):
> 1. $h(\chi, \psi) = \chi^\dagger H\psi = \sum_{a,b}\chi_a^{\ast}H_{ab}\psi_b$, $H^\dagger = H$, and $h$ is nondegenerate iff $\det H \ne 0$;
> 2. under a change of basis with matrix $U$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]),
>
> $$
> H' = (U^{-1})^\dagger\,H\,U^{-1} ;
> $$
>
> 3. this agrees with the operator rule $H \mapsto UHU^{-1}$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]) for every Hermitian $H$ iff $U$ is unitary, $U^\dagger U = \mathbb 1$ ([[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]]).
>
> *Source: the analogue of [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]] ($A = C^{\mathsf t}BC$) and its Remark "Contrast with operators" · the Hermitian version written here*

^thm-c5a-2-1

> [!derivation]- Derivation
> **1. Formula.** $h(\chi, \psi) = h\bigl(\sum_a\chi_ae_a, \sum_b\psi_be_b\bigr) = \sum_{a,b}\chi_a^{\ast}\psi_b\,h(e_a, e_b)$: conjugate-linearity pulls out $\chi_a^{\ast}$, linearity pulls out $\psi_b$. $H_{ab} = h(e_a, e_b) = h(e_b, e_a)^{\ast} = H_{ba}^{\ast}$, i.e. $H^\dagger = H$.
>
> **2. Nondegeneracy.** $h(\chi, \psi) = 0$ for all $\chi$ iff $\chi^\dagger(H\psi) = 0$ for all columns $\chi$ iff $H\psi = 0$ (take $\chi = H\psi$). So $h$ is nondegenerate iff $H$ has trivial kernel iff $\det H \ne 0$ ([[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]).
>
> **3. Change of basis.** With $e'_b = \sum_c(U^{-1})_{cb}e_c$ (step 1 of Derivation §C5a.1.2):
>
> $$
> H'_{ab} = h(e'_a, e'_b) = \sum_{c,d}(U^{-1})_{ca}^{\ast}\,(U^{-1})_{db}\,h(e_c, e_d) = \sum_{c,d}\bigl((U^{-1})^\dagger\bigr)_{ac}H_{cd}(U^{-1})_{db} ,
> $$
>
> using $(U^{-1})^{\ast}_{ca} = ((U^{-1})^\dagger)_{ac}$. Check: $\chi'^\dagger H'\psi' = \chi^\dagger U^\dagger(U^{-1})^\dagger HU^{-1}U\psi = \chi^\dagger H\psi$, since $U^\dagger(U^\dagger)^{-1} = \mathbb 1$ and $(U^{-1})^\dagger = (U^\dagger)^{-1}$.
>
> **4. Comparison.** If $U^\dagger U = \mathbb 1$, then $(U^{-1})^\dagger = (U^\dagger)^{-1} = U$, and $H' = UHU^{-1}$ for every $H$. Conversely, if the two rules agree for $H = \mathbb 1$ (a Hermitian matrix), $(U^{-1})^\dagger U^{-1} = UU^{-1} = \mathbb 1$, i.e. $(UU^\dagger)^{-1} = \mathbb 1$, so $UU^\dagger = \mathbb 1$ and $U$ is unitary (LADR Thm. 7.57 (d)).
>
> **What the derivation shows**
> - A $4\times4$ array can be the matrix of an operator (slots $V\otimes V'$) or of a form (two conjugate-and-dual slots); the two transform differently, and only unitary changes of basis hide the difference — the Hermitian counterpart of "operators are $(1,1)$-tensors, bilinear forms $(0,2)$-tensors" in LADR's remark to Thm. 9.7.
> - Used next: $\gamma^0$ is used in both roles (Remark: γ⁰ in two roles).

^der-c5a-2-1

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]]

> [!definition] Definition §C5a.2.2: Signature of a Hermitian Form
> Let $h$ be a nondegenerate Hermitian form on $V$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]). A subspace $W \subseteq V$ is **positive** (**negative**) if $h(\psi, \psi) > 0$ ($< 0$) for every nonzero $\psi \in W$. The **signature** of $h$ is $(p, q)$, with $p$ and $q$ the largest dimensions of a positive and of a negative subspace. It is defined without a basis.
>
> *Source: written here (the real analogue: diagonalization of quadratic forms, [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR Thm. 9.23]])*

^def-c5a-2-2

## The Dirac form and the Dirac conjugate

> [!definition] Definition §C5a.2.3: Hermitian Basis
> A basis of $V$ is **Hermitian** (for the Dirac maps, [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]) if the matrices satisfy $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ for $\mu = 0, \dots, 3$, i.e. $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]). The chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]) is one.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices") · the user's pre-course notes, §5.1 ("Hermiticity": "hypothesis; … arrangeable by a change of basis") · Yu §5.1, eqs. (5.4)–(5.7) · the name written here*

^def-c5a-2-3

> [!definition] Definition §C5a.2.4: The Dirac Form
> In a Hermitian basis ([[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]]) the **Dirac form** is the Hermitian form ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) with matrix $\gamma^0$:
>
> $$
> h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi .
> $$
>
> *Source: PS §3.2, eq. (3.32) · the user's PHY 513 notes, Ch. 8 §8.3 ("$\gamma^0$ for Dirac spinors, giving the invariant $\bar\psi\chi = \psi^\dagger\gamma^0\chi$") · Yu §5.3, eq. (5.90) · the form formulation written here*

^def-c5a-2-4

The definition uses one Hermitian basis; that the result does not depend on which one, up to a factor fixed by convention, is Theorems §C5a.2.2 and §C5a.2.4. $h_D$ is Hermitian because $(\chi^\dagger\gamma^0\psi)^{\ast} = \psi^\dagger\gamma^{0\dagger}\chi = \psi^\dagger\gamma^0\chi$, and nondegenerate because $\det\gamma^0 \ne 0$ ($(\gamma^0)^2 = \mathbb 1$).

> [!definition] Definition §C5a.2.5: The Dirac Conjugate
> The **Dirac conjugate** of a Dirac spinor (or field) $\psi$ is the row
>
> $$
> \bar\psi \equiv \psi^\dagger\gamma^0 .
> $$
>
> It is not the Hermitian conjugate: the extra $\gamma^0$, the matrix of the Dirac form ([[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]), is essential; that this form is Lorentz invariant is [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]] (§C5a.6). Basis-free, $\bar\psi$ is the linear functional $h_D(\psi, \cdot\,) \in V'$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-5|Def. §C5a.1.5]]), and $\psi \mapsto \bar\psi$ is conjugate-linear.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Definition "The Dirac conjugate", eq. (psibar)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.32) · Yu §5.3, eq. (5.90) · the functional reading written here*

^def-c5a-2-5

The components of $\bar\psi$: $\bar\psi(\chi) = h_D(\psi, \chi) = \sum_b(\psi^\dagger\gamma^0)_b\chi_b$, so by Def. §C5a.1.5 its row is $\psi^\dagger\gamma^0$; conjugate-linearity is $(\lambda\psi)^\dagger = \lambda^{\ast}\psi^\dagger$.

> [!theorem] Theorem §C5a.2.2: The Dirac Maps Are Self-Adjoint for the Dirac Form, and Fix It up to a Real Factor
> 1. $h_D(\Gamma^\mu\chi, \psi) = h_D(\chi, \Gamma^\mu\psi)$ for all $\chi, \psi \in V$ and $\mu = 0, \dots, 3$ ($h_D$ of [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]); in components, $\overline{\gamma^\mu\chi} = \bar\chi\gamma^\mu$.
> 2. If $h$ is any nondegenerate Hermitian form on $V$ for which every $\Gamma^\mu$ is self-adjoint in this sense, then $h = c\,h_D$ for a real $c \ne 0$.
>
> So the Dirac form is determined by the Dirac maps alone, up to a real normalization: a basis-free characterization of $\bar\psi$.
>
> *Source: part 1: the identity $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ of the user's PHY 513 notes, Ch. 8 §8.1 and PS §3.2, read as self-adjointness here · part 2 written here*

^thm-c5a-2-2

> [!derivation]- Derivation
> Work in a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$.
>
> **1. Self-adjointness.** $h_D(\Gamma^\mu\chi, \psi) = (\gamma^\mu\chi)^\dagger\gamma^0\psi = \chi^\dagger\gamma^{\mu\dagger}\gamma^0\psi = \chi^\dagger\gamma^0\gamma^\mu\gamma^0\gamma^0\psi = \chi^\dagger\gamma^0\gamma^\mu\psi = h_D(\chi, \Gamma^\mu\psi)$, using $(\gamma^0)^2 = \mathbb 1$. The middle equality reads $\overline{\gamma^\mu\chi} = (\gamma^\mu\chi)^\dagger\gamma^0 = \bar\chi\gamma^\mu$.
>
> **2. The condition on a matrix.** Let $H$ be the matrix of $h$ (Theorem §C5a.2.1, 1). Self-adjointness of $\Gamma^\mu$ means $(\gamma^\mu\chi)^\dagger H\psi = \chi^\dagger H\gamma^\mu\psi$ for all columns, i.e. $\gamma^{\mu\dagger}H = H\gamma^\mu$ (take $\chi$, $\psi$ standard basis columns).
>
> **3. Reduce to a commutant.** Insert $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$: $\gamma^0\gamma^\mu\gamma^0H = H\gamma^\mu$. Multiply on the left by $\gamma^0$: $\gamma^\mu(\gamma^0H) = (\gamma^0H)\gamma^\mu$. So $\gamma^0H$ commutes with all four $\gamma^\mu$, hence $\gamma^0H = c\mathbb 1$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 4), and $H = c\gamma^0$.
>
> **4. The factor.** $H^\dagger = H$ gives $c^{\ast}\gamma^0 = c\gamma^0$, so $c$ is real; nondegeneracy gives $c \ne 0$.
>
> **What the derivation shows**
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, used in §C5a.1 as a matrix identity, says that the Dirac maps are self-adjoint for $h_D$ — not for the positive form $\chi^\dagger\psi$ (for which the $\gamma^i$ are anti-self-adjoint).
> - ⚑ By-product: the normalization of $\bar\psi$ is a convention. Both signs $c = \pm1$ are used in the literature with other metric signatures; with $g = (+,-,-,-)$ the choice $c = 1$ makes $\bar uu = 2m > 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]]).
> - Used next: which changes of basis keep $c = 1$ (Theorem §C5a.2.4).

^der-c5a-2-2

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]

> [!theorem] Theorem §C5a.2.3: The Dirac Form Has Signature (2, 2)
> The Dirac form $h_D$ ([[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]) has signature $(2, 2)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]]): it is nondegenerate and indefinite, and in a Hermitian basis the eigenspaces $W_\pm$ of $\gamma^0$ (eigenvalues $\pm1$, each twice) are a positive and a negative subspace of maximal dimension.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary)) and [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]] ("indefinite, with eigenvalues $+1, +1, -1, -1$") · the signature argument written here*

^thm-c5a-2-3

> [!derivation]- Derivation
> **1. Eigenspaces.** In a Hermitian basis $\gamma^0$ is Hermitian, hence normal, so $\mathbb C^4$ has an orthonormal (for $\chi^\dagger\psi$) basis of its eigenvectors ([[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]]); its eigenvalues are $\pm1$, each twice ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-8|Theorem §C5a.1.8]]). So $\mathbb C^4 = W_+\oplus W_-$ with $\dim W_\pm = 2$.
>
> **2. Signs on the eigenspaces.** For $\psi \in W_+$, $h_D(\psi, \psi) = \psi^\dagger\gamma^0\psi = \psi^\dagger\psi > 0$ if $\psi \ne 0$; for $\psi \in W_-$, $h_D(\psi, \psi) = -\psi^\dagger\psi < 0$. So $p \ge 2$ and $q \ge 2$.
>
> **3. No larger positive subspace.** Let $P$ be positive with $\dim P \ge 3$. Then $\dim P + \dim W_- \ge 5 > 4$, so $P\cap W_-$ contains some $\psi \ne 0$ (the dimension of a sum is at most $4$, [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]). On it $h_D(\psi, \psi)$ is $> 0$ (in $P$) and $< 0$ (in $W_-$), a contradiction. So $p = 2$; the same argument with $W_+$ gives $q = 2$.
>
> **What the derivation shows**
> - $p$ and $q$ are defined without a basis, so the signature is a property of the Dirac form itself; a real rescaling $c$ (Theorem §C5a.2.2) keeps it $(2, 2)$ (a negative $c$ exchanges $p$ and $q$).
> - ⚑ By-product: there is no positive Lorentz-invariant density built from $\bar\psi$ alone: the invariant form is indefinite, and the positive $\psi^\dagger\psi$ is not invariant ([[§C5a.6 The Dirac Conjugate and the Bilinears#^der-c5a-6-2|Derivation §C5a.6.2]]); the conserved positive density of Quantum Mechanics is the time component of a current ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]).
> - The signature $(2, 2)$ is the spinor counterpart of the Minkowski signature $(1, 3)$ of $g$; both are invariant forms preserved by the corresponding Lorentz matrices ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]).

^der-c5a-2-3

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-8|Theorem §C5a.1.8]], [[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]], [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]

## Which changes of basis preserve the Dirac conjugate

> [!theorem] Theorem §C5a.2.4: Which Changes of Basis Preserve ψ̄
> Let $e$ be a Hermitian basis ([[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]]), $U$ any invertible change-of-basis matrix ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), $\psi' = U\psi$, $\gamma'^\mu = U\gamma^\mu U^{-1}$.
> 1. The Dirac-conjugate formula applied in the new basis gives $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger(U^\dagger U)\gamma^0\chi$. It equals $h_D(\psi, \chi) = \bar\psi\chi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]) for all $\psi, \chi$ iff $U$ is unitary.
> 2. The new basis is Hermitian iff $U^\dagger U = c\,\mathbb 1$ with $c > 0$, i.e. $U = \sqrt c\,W$ with $W$ unitary; then $\psi'^\dagger\gamma'^0\chi' = c\,\bar\psi\chi$.
> 3. For unitary $U$: $\psi'^\dagger = \psi^\dagger U^{-1}$, $\bar\psi' = \bar\psi\,U^{-1}$, and every bilinear $\bar\psi M\chi$ with $M \in \operatorname{End}(V)$ ($M' = UMU^{-1}$) is unchanged.
>
> So $\bar\psi = \psi^\dagger\gamma^0$ defines the same object in all Hermitian bases related by unitary matrices, and not otherwise. Part 2 for $c = 1$ is [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], 2; Pauli's theorem guarantees that two Hermitian bases are related by a unitary $U$ up to this factor ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], 2).
>
> *Source: PS §3.2, p. 41 ("unitarily equivalent") · Yu §5.2, eq. (5.72) (unitary $U$) · the user's pre-course notes, §5.2 ("all representations are related by unitary similarity transformations") · parts 1–2 and the converses written here*

^thm-c5a-2-4

> [!derivation]- Derivation
> **1. Part 1.** $\psi'^\dagger = (U\psi)^\dagger = \psi^\dagger U^\dagger$ and $\gamma'^0\chi' = U\gamma^0U^{-1}U\chi = U\gamma^0\chi$, so $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger U^\dagger U\gamma^0\chi$. This equals $\psi^\dagger\gamma^0\chi$ for all columns iff $U^\dagger U\gamma^0 = \gamma^0$ (take $\psi$, $\chi$ standard basis columns to read off each entry), iff $U^\dagger U = \mathbb 1$ (multiply on the right by $(\gamma^0)^{-1} = \gamma^0$).
>
> **2. Part 2: the condition.** The new basis is Hermitian iff $\gamma'^{\mu\dagger} = \gamma'^0\gamma'^\mu\gamma'^0$. Left side: $(U\gamma^\mu U^{-1})^\dagger = (U^\dagger)^{-1}\gamma^{\mu\dagger}U^\dagger = (U^\dagger)^{-1}\gamma^0\gamma^\mu\gamma^0U^\dagger$. Right side: $U\gamma^0U^{-1}U\gamma^\mu U^{-1}U\gamma^0U^{-1} = U\gamma^0\gamma^\mu\gamma^0U^{-1}$. Multiply both on the left by $U^\dagger$ and on the right by $U$: the condition is $\gamma^0\gamma^\mu\gamma^0\,(U^\dagger U) = (U^\dagger U)\,\gamma^0\gamma^\mu\gamma^0$ for every $\mu$.
>
> **3. Part 2: solve it.** For $\mu = 0$ it says $P \equiv U^\dagger U$ commutes with $\gamma^0$ ($(\gamma^0)^3 = \gamma^0$). Then $\gamma^\mu = \gamma^0(\gamma^0\gamma^\mu\gamma^0)\gamma^0$ is a product of matrices commuting with $P$, so $P$ commutes with every $\gamma^\mu$ and $P = c\mathbb 1$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 4). $c > 0$: $v^\dagger Pv = |Uv|^2 > 0$ for $v \ne 0$. Conversely $P = c\mathbb 1$ satisfies the condition. Then $W = U/\sqrt c$ has $W^\dagger W = \mathbb 1$, and part 1's computation gives $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger(c\mathbb 1)\gamma^0\chi = c\,\bar\psi\chi$.
>
> **4. Part 3.** With $U^\dagger = U^{-1}$: $\psi'^\dagger = \psi^\dagger U^{-1}$; $\bar\psi' = \psi'^\dagger\gamma'^0 = \psi^\dagger U^{-1}U\gamma^0U^{-1} = \bar\psi U^{-1}$; $\bar\psi'M'\chi' = \bar\psi U^{-1}UMU^{-1}U\chi = \bar\psi M\chi$.
>
> **What the derivation shows**
> - ⚑ By-product: the class of Hermitian bases is closed under $U = \sqrt c\,W$, but $\bar\psi$ is only closed under $c = 1$. Example: $U = 2\cdot\mathbb 1$ leaves every $\gamma$ matrix unchanged (so the new basis is Hermitian), doubles every component, and multiplies $\bar\psi\psi$ by $4$. The $\gamma$'s fix the Dirac form only up to a factor (Theorem §C5a.2.2); demanding unitary changes of basis — equivalently, keeping $\psi^\dagger\psi$ of the standard columns as the reference inner product — fixes it. This is the normalization implicit in "$\bar\psi = \psi^\dagger\gamma^0$ in every basis".
> - In the language of the slot rule (Theorem §C5a.1.3): a unitary $U$ makes the conjugate slot of $\psi^\dagger$ transform like a $V'$-slot, and the two roles of $\gamma^0$ (operator and form, Theorem §C5a.2.1) transform alike.
> - Used next: the Dirac Lagrangian is basis independent exactly for unitary $U$ (Theorem §C5a.7.5).

^der-c5a-2-4

*Uses:* [[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]

> [!remark] Remark: γ⁰ in two roles
> The matrix $\gamma^0$ appears in two different jobs. As the matrix of the Dirac map $\Gamma^0$ it is an operator, slots $V\otimes V'$, and transforms as $U\gamma^0U^{-1}$; it enters the Dirac equation $i\gamma^0\partial_0\psi + \dots$. As the matrix of the Dirac form it pairs two spinors, $\bar\chi\psi = \chi^\dagger\gamma^0\psi$, and transforms as $(U^{-1})^\dagger\gamma^0U^{-1}$ (Theorem §C5a.2.1). In a Hermitian basis the two arrays coincide; after a non-unitary change of basis they differ, and the formula $\bar\psi = \psi^\dagger\gamma^0$, which silently identifies them, stops computing the Dirac form (Theorem §C5a.2.4, 1). The same double role is played by $g_{\mu\nu}$ for vectors in an orthonormal frame, and the same caution applies to non-orthonormal frames. Under Lorentz transformations the form role is the one preserved: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]).
>
> *Source: written here · the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$: $\gamma^0$ for Dirac spinors")*

^rem-c5a-2-1

> [!remark]- Connections
> - The Dirac form is the invariant form of the spinor slot as $g$ is that of the vector slot and $\varepsilon$ that of a Weyl slot; its indefiniteness, signature $(2, 2)$, is the spinor face of the non-unitarity of finite-dimensional Lorentz representations — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-11|Theorem §CB.15.11]].
> - The reality of bilinears and the self-adjointness of the Dirac maps for the Dirac form are one identity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]].
> - Unitary changes of basis are those that keep the reference inner product $\psi^\dagger\chi$ of the columns; the Dirac form needs them although it is not itself an inner product, as Quantum Mechanics needs them to keep probabilities — [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-1|QM Theorem §C1.4.1]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]].
> - The Dirac conjugate defined here is what the Lagrangian, every bilinear and the canonical momentum $\pi = i\psi^\dagger$ are built from — [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|Theorem §C5a.8.1]].
