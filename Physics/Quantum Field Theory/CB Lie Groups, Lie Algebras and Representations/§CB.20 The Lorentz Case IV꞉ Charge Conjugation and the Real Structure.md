---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.20
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.21 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §9.2.1, eqs. (9.98), (9.102), (9.104)–(9.117) (the charge-conjugation matrix $\mathcal C$, the transpose form) · Peskin & Schroeder, §3.6, eqs. (3.144)–(3.145), pp. 70–71 (the chiral matrix $-i\gamma^2$, unnamed) · PHY 513 Lecture 12, slides 8–10 · the user's PHY 513 notes, Ch. 12 §12.3 · Schwartz, Quantum Field Theory and the Standard Model, §10.3, eq. (10.74) (a Majorana basis) · the basis-free charge-conjugation matrix and map, and the comparison of names, written here.*

Is charge conjugation defined as complex conjugation, or as a general conjugation that becomes complex conjugation in a suitable basis? This section answers it on the Dirac module of [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.19]]: spinor space $S = \mathbb C^4$ with Clifford multiplication ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-19-1|Def. §CB.19.1]]), on which $\mathrm{Spin}(1,3)_0$ acts by the spinor Lorentz matrices $\Lambda_{1/2}$ ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]]) and which $\gamma^5$, the complex volume element of the opposite orientation ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-2|Theorem §CB.19.2]]), splits into the halves $S^\pm$ ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-4|Theorem §CB.19.4]]), complex conjugates of each other ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-6|Theorem §CB.19.6]]). The other tools are Pauli's theorem and Hermitian bases ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^thm-cb-14-12|Theorem §CB.14.12]], [[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-11|Def. §CB.14.11]]). Notation as in [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.19]].

## Charge conjugation: a real structure on the Dirac module

Complex conjugation turns a set of Dirac matrices into another set, and Pauli's theorem ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^thm-cb-14-12|Theorem §CB.14.12]]) relates the two by a matrix $B$. Combined with complex conjugation, $B$ gives an antilinear map of spinor space that commutes with every spinor Lorentz matrix and squares to $\mathbb 1$: a real structure on the Dirac module, whose matrix in the chiral basis is $-i\gamma^2$ (Example §CB.20.5).

> [!definition] Definition §CB.20.1: The Charge-Conjugation Matrix
> Let $\gamma^\mu$ be $4\times4$ Dirac matrices ([[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-12-11|Def. §CB.12.11]]) and $(\gamma^\mu)^{\ast}$ their entrywise complex conjugates. A **charge-conjugation matrix** for them is an invertible $B \in GL(4, \mathbb C)$ with
>
> $$
> B\,(\gamma^\mu)^{\ast}\,B^{-1} = -\gamma^\mu, \qquad \mu = 0, 1, 2, 3 .
> $$
>
> *Source: Yu §9.2.1, eqs. (9.98), (9.112)–(9.113) (the transpose form, Example §CB.20.5, 4) · PS §3.6, eqs. (3.144)–(3.145) (the chiral matrix $-i\gamma^2$, unnamed) · the basis-free definition written here (user's question, 2026-10-12: is charge conjugation defined as complex conjugation, or a general conjugation that becomes it?)*

^def-cb-20-1

> [!theorem] Theorem §CB.20.2: Existence and Uniqueness of the Charge-Conjugation Matrix, and Its Square under Conjugation
> Let $\gamma^\mu$ be $4\times4$ Dirac matrices ([[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-12-11|Def. §CB.12.11]]).
> 1. $(\gamma^\mu)^{\ast}$ and $-\gamma^\mu$ are Dirac matrices too.
> 2. A charge-conjugation matrix $B$ ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^def-cb-20-1|Def. §CB.20.1]]) exists and is unique up to a nonzero factor.
> 3. In a Hermitian basis ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-11|Def. §CB.14.11]]) $B$ can be chosen unitary, and is then unique up to a phase.
> 4. Under a change of basis $\gamma'^\mu = M\gamma^\mu M^{-1}$ ([[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-12-15|Theorem §CB.12.15]]), $B' = MB(M^{\ast})^{-1}$ is a charge-conjugation matrix for the $\gamma'^\mu$; it is unitary if $B$ and $M$ are.
> 5. $BB^{\ast} = \epsilon\,\mathbb 1$ with $\epsilon$ real; the sign of $\epsilon$ is the same for every $B$ and every set of $4\times4$ Dirac matrices; for unitary $B$, $\epsilon = \pm1$. For the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ with $g = (+,-,-,-)$, $\epsilon = +1$: a unitary $B$ has $BB^{\ast} = \mathbb 1$.
>
> *Source: written here from Pauli's theorem (the route of Yu §9.2.1, which verifies the transpose form for the chiral matrix only, eqs. (9.104)–(9.113)) · the sign in part 5 computed here in the chiral basis of [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-12-13|Example §CB.12.13]] and transported to every basis by part 4*

^thm-cb-20-2

> [!proof]- Proof
> **1. Conjugate sets are Dirac matrices.** Entrywise conjugation preserves sums and products, and $g^{\mu\nu}$ is real: $(\gamma^\mu)^{\ast}(\gamma^\nu)^{\ast} + (\gamma^\nu)^{\ast}(\gamma^\mu)^{\ast} = (\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu)^{\ast} = (2g^{\mu\nu}\mathbb 1)^{\ast} = 2g^{\mu\nu}\mathbb 1$. For the negatives, $(-\gamma^\mu)(-\gamma^\nu) + (-\gamma^\nu)(-\gamma^\mu) = \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\mathbb 1$.
>
> **2. Existence and uniqueness.** Apply Pauli's theorem ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^thm-cb-14-12|Theorem §CB.14.12]], 1) to the two sets of step 1, with $(\gamma^\mu)^{\ast}$ as the first and $-\gamma^\mu$ as the second: there is an invertible $U$ with $-\gamma^\mu = U(\gamma^\mu)^{\ast}U^{-1}$ for all $\mu$, unique up to a nonzero factor. $B = U$ is a charge-conjugation matrix, and every other one is $\lambda B$, $\lambda \ne 0$.
>
> **3. Unitary choice.** Let $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$. Conjugating entrywise, $\bigl((\gamma^\mu)^{\ast}\bigr)^\dagger = (\gamma^{\mu\dagger})^{\ast} = (\gamma^0)^{\ast}(\gamma^\mu)^{\ast}(\gamma^0)^{\ast}$: the set $(\gamma^\mu)^{\ast}$ satisfies the Hermiticity relation with its own zeroth matrix $(\gamma^0)^{\ast}$. For the negatives, $(-\gamma^\mu)^\dagger = -\gamma^0\gamma^\mu\gamma^0 = (-\gamma^0)(-\gamma^\mu)(-\gamma^0)$. Both sets are Hermitian, so part 2 of Theorem §CB.14.12 makes $U$ unitary. $\lambda B$ is unitary iff $|\lambda| = 1$.
>
> **4. Change of basis.** $\gamma'^\mu = M\gamma^\mu M^{-1}$ gives $(\gamma'^\mu)^{\ast} = M^{\ast}(\gamma^\mu)^{\ast}(M^{\ast})^{-1}$ (conjugation is multiplicative, and $(M^{-1})^{\ast} = (M^{\ast})^{-1}$). With $B' = MB(M^{\ast})^{-1}$, $(B')^{-1} = M^{\ast}B^{-1}M^{-1}$ and
>
> $$
> B'(\gamma'^\mu)^{\ast}(B')^{-1} = MB(M^{\ast})^{-1}\,M^{\ast}(\gamma^\mu)^{\ast}(M^{\ast})^{-1}\,M^{\ast}B^{-1}M^{-1} = M\bigl(B(\gamma^\mu)^{\ast}B^{-1}\bigr)M^{-1} = -M\gamma^\mu M^{-1} = -\gamma'^\mu .
> $$
>
> If $M$ is unitary, so is $M^{\ast}$, and a product of unitary matrices is unitary.
>
> **5. $BB^{\ast}$ commutes with every γ.** Conjugate the defining relation: $B^{\ast}\gamma^\mu(B^{\ast})^{-1} = -(\gamma^\mu)^{\ast}$, i.e. $(\gamma^\mu)^{\ast} = -B^{\ast}\gamma^\mu(B^{\ast})^{-1}$. Insert this into the defining relation:
>
> $$
> -\gamma^\mu = B(\gamma^\mu)^{\ast}B^{-1} = -B B^{\ast}\gamma^\mu(B^{\ast})^{-1}B^{-1} = -(BB^{\ast})\,\gamma^\mu\,(BB^{\ast})^{-1} .
> $$
>
> So $BB^{\ast}$ commutes with all four $\gamma^\mu$, and $BB^{\ast} = \epsilon\mathbb 1$ ([[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-13-9|Theorem §CB.13.9]], 4), $\epsilon \ne 0$ since $B$ is invertible.
>
> **6. ε is real.** Conjugating $BB^{\ast} = \epsilon\mathbb 1$ gives $B^{\ast}B = \epsilon^{\ast}\mathbb 1$. Then $B(B^{\ast}B) = \epsilon^{\ast}B$ and $(BB^{\ast})B = \epsilon B$; the two left sides are equal and $B \ne 0$, so $\epsilon^{\ast} = \epsilon$.
>
> **7. Unitary B: ε = ±1.** $B^{\ast}$ is unitary with $B$, so $BB^{\ast} = \epsilon\mathbb 1$ is unitary: $|\epsilon|^2 = 1$, and with step 6, $\epsilon = \pm1$.
>
> **8. The sign does not depend on the choices.** Another charge-conjugation matrix is $\lambda B$ (step 2), with $(\lambda B)(\lambda B)^{\ast} = |\lambda|^2BB^{\ast} = |\lambda|^2\epsilon\mathbb 1$: same sign. In another basis, step 4 gives $B'(B')^{\ast} = MB(M^{\ast})^{-1}\,M^{\ast}B^{\ast}M^{-1} = M(BB^{\ast})M^{-1} = \epsilon\mathbb 1$: same $\epsilon$. Every set of $4\times4$ Dirac matrices is $M\gamma^\mu M^{-1}$ for some invertible $M$ (Theorem §CB.14.12, 1), so the sign of $\epsilon$ is one number for all of them, and it may be computed in a single basis.
>
> **9. The sign, computed in the chiral basis.** Take the chiral matrices of [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-12-13|Example §CB.12.13]], $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$. The entries of $\sigma^1$, $\sigma^3$ are real and those of $\sigma^2$ are $0$, $\pm i$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]), so $(\gamma^\mu)^{\ast} = \gamma^\mu$ for $\mu = 0, 1, 3$ and $(\gamma^2)^{\ast} = -\gamma^2$. Try $B = -i\gamma^2$. By the Clifford relations ([[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-12-12|Theorem §CB.12.12]], 1), $B^2 = (-i)^2(\gamma^2)^2 = (-1)(-\mathbb 1) = \mathbb 1$, so $B^{-1} = B$.
> - For $\mu = 0, 1, 3$: $B(\gamma^\mu)^{\ast}B^{-1} = (-i)^2\gamma^2\gamma^\mu\gamma^2 = -\gamma^2\gamma^\mu\gamma^2 = -(-\gamma^\mu\gamma^2)\gamma^2 = \gamma^\mu(\gamma^2)^2 = -\gamma^\mu$, moving $\gamma^2$ past $\gamma^\mu \ne \gamma^2$ at the cost of a sign.
> - For $\mu = 2$: $B(\gamma^2)^{\ast}B^{-1} = (-i\gamma^2)(-\gamma^2)(-i\gamma^2) = (-i)(-1)(-i)(\gamma^2)^3 = (\gamma^2)^2\gamma^2 = -\gamma^2$, using $(-i)(-1)(-i) = 1$.
>
> So $B = -i\gamma^2$ is a charge-conjugation matrix. It is unitary: $(\gamma^2)^\dagger = -\gamma^2$ (Example §CB.12.13), so $B^\dagger = i(\gamma^2)^\dagger = -i\gamma^2 = B$ and $B^\dagger B = B^2 = \mathbb 1$. It is real: $B^{\ast} = (-i)^{\ast}(\gamma^2)^{\ast} = i(-\gamma^2) = B$. Hence $BB^{\ast} = B^2 = \mathbb 1$: $\epsilon = +1$, and by step 8 for every set of Dirac matrices.
>
> **What the proof shows**
> - Charge conjugation is not defined as complex conjugation: complex conjugation of the $\gamma$'s produces a second Clifford module, and $B$ is the change of basis that Pauli's theorem supplies between it and the negated original. Only the factor of $B$ is a choice.
> - ⚑ By-product: $\epsilon = +1$ is a property of the Clifford algebra with this signature, not of a basis. It makes $c = B\circ K$ square to $+\mathbb 1$ ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^thm-cb-20-4|Theorem §CB.20.4]], 4), a real structure, so spinors fixed by it exist (Majorana spinors). With $\epsilon = -1$ the map would square to $-\mathbb 1$, a quaternionic structure with no fixed vectors, the situation of the two-spinor flip $\xi \mapsto -i\sigma^2\xi^{\ast}$ on $\mathbb C^2$, which squares to $(-i\sigma^2)(-i\sigma^2)^{\ast} = (-i\sigma^2)^2 = -\mathbb 1$ ($-i\sigma^2$ is real). Consistent with the real classification: $c$ commutes with the $i\gamma^\mu$, which generate $\mathrm{Cl}(3,1) \cong M_4(\mathbb R)$ ([[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^rem-cb-13-1|§CB.13, ★ Remark: The real classification (not used in the course)]]).
> - Used next: the antilinear map $c_B$ (Def. §CB.20.3, Theorem §CB.20.4) and the matrices in three bases (Example §CB.20.5).

^pf-cb-20-2

*Uses:* [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-12-11|Def. §CB.12.11]], [[§CB.14 Complex Clifford Algebras and Clifford Modules#^thm-cb-14-12|Theorem §CB.14.12]], [[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-11|Def. §CB.14.11]], [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-12-15|Theorem §CB.12.15]], [[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-13-9|Theorem §CB.13.9]], [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-12-13|Example §CB.12.13]], [[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-12-12|Theorem §CB.12.12]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]

> [!definition] Definition §CB.20.3: The Charge-Conjugation Map
> For a charge-conjugation matrix $B$ ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^def-cb-20-1|Def. §CB.20.1]]) the **charge-conjugation map** is
>
> $$
> c_B : \mathbb C^4 \to \mathbb C^4, \qquad c_B(\psi) = B\,\psi^{\ast}, \qquad\text{i.e.}\qquad c_B = B\circ K ,
> $$
>
> where $K\psi = \psi^{\ast}$ is the column of complex-conjugate components. Written $c$ when $B$ is fixed.
>
> *Source: written here · the chiral case $-i\gamma^2\psi^{\ast}$: PS §3.6, eq. (3.145), and Yu §9.2.1, eq. (9.102) in transpose form*

^def-cb-20-3

> [!theorem] Theorem §CB.20.4: The Charge-Conjugation Map Is a Real Structure Commuting with the Spinor Lorentz Matrices
> Let $\gamma^\mu$ be the Dirac matrices in a Hermitian basis ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-11|Def. §CB.14.11]]), $B$ a unitary charge-conjugation matrix ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^thm-cb-20-2|Theorem §CB.20.2]], 3) and $c = c_B$ ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^def-cb-20-3|Def. §CB.20.3]]). Then
> 1. $c$ is antilinear, $c(\lambda\psi + \chi) = \lambda^{\ast}c(\psi) + c(\chi)$; it conjugates the standard inner product, $c(\psi)^\dagger c(\chi) = (\psi^\dagger\chi)^{\ast}$, and reverses the Dirac form ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-15|Def. §CB.14.15]]), $h_D(c\psi, c\chi) = -h_D(\psi, \chi)^{\ast}$;
> 2. $c\,\gamma^\mu = -\gamma^\mu\,c$; hence $c\,S^{\mu\nu} = -S^{\mu\nu}\,c$ for the spinor generators ([[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-16|Def. §CB.15.16]]) and $c\,\gamma^5 = -\gamma^5\,c$ ([[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-13-14|Def. §CB.13.14]]), so $c$ maps $S^\pm$ onto $S^\mp$;
> 3. $c\,\Lambda_{1/2}(\omega) = \Lambda_{1/2}(\omega)\,c$ for every real $\omega_{\mu\nu}$ ([[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-19|Def. §CB.15.19]]), hence $c$ commutes with the action of every element of $\mathrm{Spin}(1,3)_0$ ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]]);
> 4. $c^2 = \mathbb 1$;
> 5. under a change of basis $\psi' = M\psi$, $\gamma'^\mu = M\gamma^\mu M^{-1}$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]), the map $c' = c_{B'}$ with $B' = MB(M^{\ast})^{-1}$ satisfies $c'(M\psi) = M\,c(\psi)$.
>
> So $c$ is one antilinear map of spinor space, written in components in each basis, fixed up to a phase: a real structure commuting with $\mathrm{Spin}(1,3)_0$.
>
> *Source: written here · the chiral case of parts 2–3 is the reason the course's $-i\gamma^2\psi^{\ast}$ transforms like $\psi$ (the user's PHY 513 notes, Ch. 12 §12.3) · Yu §9.2.1, eq. (9.112) ($\mathcal C^{-1}\gamma^5\mathcal C = \gamma^5$, the transpose form of $c\gamma^5 = -\gamma^5c$; Example §CB.20.5, 4)*

^thm-cb-20-4

> [!proof]- Proof
> **1. Antilinearity.** $c(\lambda\psi + \chi) = B(\lambda\psi + \chi)^{\ast} = B(\lambda^{\ast}\psi^{\ast} + \chi^{\ast}) = \lambda^{\ast}B\psi^{\ast} + B\chi^{\ast}$.
>
> **2. Inner products.** $(B\psi^{\ast})^\dagger = (\psi^{\ast})^\dagger B^\dagger = \psi^{\mathsf T}B^\dagger$, so $c(\psi)^\dagger c(\chi) = \psi^{\mathsf T}B^\dagger B\chi^{\ast} = \psi^{\mathsf T}\chi^{\ast} = \sum_a\psi_a\chi_a^{\ast} = (\psi^\dagger\chi)^{\ast}$ ($B$ unitary). For the Dirac form, the defining relation at $\mu = 0$, $B(\gamma^0)^{\ast} = -\gamma^0B$, gives $B^\dagger\gamma^0B = -B^\dagger B(\gamma^0)^{\ast} = -(\gamma^0)^{\ast}$; hence $h_D(c\psi, c\chi) = \psi^{\mathsf T}B^\dagger\gamma^0B\chi^{\ast} = -\psi^{\mathsf T}(\gamma^0)^{\ast}\chi^{\ast} = -\bigl(\psi^\dagger\gamma^0\chi\bigr)^{\ast} = -h_D(\psi, \chi)^{\ast}$.
>
> **3. $\gamma^\mu$.** $c(\gamma^\mu\psi) = B(\gamma^\mu)^{\ast}\psi^{\ast} = B(\gamma^\mu)^{\ast}B^{-1}\,B\psi^{\ast} = -\gamma^\mu c(\psi)$, inserting $B^{-1}B = \mathbb 1$.
>
> **4. $S^{\mu\nu}$: two signs.** $(S^{\mu\nu})^{\ast} = \bigl(\frac i4[\gamma^\mu, \gamma^\nu]\bigr)^{\ast} = -\frac i4[(\gamma^\mu)^{\ast}, (\gamma^\nu)^{\ast}]$: conjugation flips the $i$. Conjugating by $B$ (which preserves products, $BXYB^{-1} = BXB^{-1}\,BYB^{-1}$):
>
> $$
> B(S^{\mu\nu})^{\ast}B^{-1} = -\tfrac i4\bigl[B(\gamma^\mu)^{\ast}B^{-1}, B(\gamma^\nu)^{\ast}B^{-1}\bigr] = -\tfrac i4[-\gamma^\mu, -\gamma^\nu] = -\tfrac i4[\gamma^\mu, \gamma^\nu] = -S^{\mu\nu} .
> $$
>
> The two minus signs of the $\gamma$'s cancel in the commutator; the sign of the $i$ survives. As in step 3, $c(S^{\mu\nu}\psi) = B(S^{\mu\nu})^{\ast}B^{-1}c(\psi) = -S^{\mu\nu}c(\psi)$.
>
> **5. γ⁵.** $(\gamma^5)^{\ast} = (i\gamma^0\gamma^1\gamma^2\gamma^3)^{\ast} = -i(\gamma^0)^{\ast}(\gamma^1)^{\ast}(\gamma^2)^{\ast}(\gamma^3)^{\ast}$, so $B(\gamma^5)^{\ast}B^{-1} = -i(-\gamma^0)(-\gamma^1)(-\gamma^2)(-\gamma^3) = -i\gamma^0\gamma^1\gamma^2\gamma^3 = -\gamma^5$, and $c\gamma^5 = -\gamma^5c$ as in step 3. If $\gamma^5\psi = \pm\psi$, then $\gamma^5c(\psi) = -c(\gamma^5\psi) = -c(\pm\psi) = \mp c(\psi)$ (the factor $\pm1$ is real, so antilinearity does not change it): $c(S^\pm) \subseteq S^\mp$, with equality since $c^2 = \mathbb 1$ (step 8).
>
> **6. Λ½: the two signs cancel.** Let $X = \omega_{\mu\nu}S^{\mu\nu}$ with real $\omega_{\mu\nu}$; then $X^{\ast} = \omega_{\mu\nu}(S^{\mu\nu})^{\ast}$ and, by step 4, $BX^{\ast}B^{-1} = -X$; inserting $B^{-1}B$ between factors, $B(X^{\ast})^nB^{-1} = (BX^{\ast}B^{-1})^n = (-X)^n$. Entrywise conjugation is continuous and multiplicative, so it passes through the exponential series ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]]):
>
> $$
> B\,\Lambda_{1/2}(\omega)^{\ast}B^{-1} = \sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^nB(X^{\ast})^nB^{-1} = \sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^n(-X)^n = \sum_{n=0}^\infty\frac1{n!}\Bigl(-\frac i2\Bigr)^nX^n = \Lambda_{1/2}(\omega) .
> $$
>
> ⚑ By-product: two sign flips cancel, $i \to -i$ from the conjugation of the exponent and $X \to -X$ from $B$ (step 4). Then $c(\Lambda_{1/2}\psi) = B\Lambda_{1/2}^{\ast}B^{-1}\,B\psi^{\ast} = \Lambda_{1/2}c(\psi)$.
>
> **7. The whole group.** Every $x \in \mathrm{Spin}(1,3)_0$ is a finite product of exponentials of elements of its Lie algebra ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-5|Theorem §CB.3.5]], 3), each acting as some $\Lambda_{1/2}(\omega)$ (Theorem §CB.19.3). A map commuting with each factor commutes with the product.
>
> **8. c².** $c(c(\psi)) = B(B\psi^{\ast})^{\ast} = BB^{\ast}\psi = \psi$, since $BB^{\ast} = \mathbb 1$ for unitary $B$ (Theorem §CB.20.2, 5).
>
> **9. Change of basis.** $B'$ is a charge-conjugation matrix for the $\gamma'^\mu$ (Theorem §CB.20.2, 4), and $c'(M\psi) = MB(M^{\ast})^{-1}(M\psi)^{\ast} = MB(M^{\ast})^{-1}M^{\ast}\psi^{\ast} = MB\psi^{\ast} = M\,c(\psi)$: the new components of $c(\psi)$ are $c'$ of the new components of $\psi$, which is the transformation of a map between vectors (Theorem §CB.0.5). $B$ is fixed up to a phase $\lambda$ (Theorem §CB.20.2, 3), and $c_{\lambda B} = \lambda c_B$: the map is fixed up to the same phase.
>
> **What the proof shows**
> - Part 3 is why $c(\psi)$ transforms like $\psi$ although $\psi^{\ast}$ alone does not ($\Lambda_{1/2}^{\ast} \ne \Lambda_{1/2}$ for boosts): $B$ undoes the effect of the conjugation on the generators.
> - The fixed vectors $c(\psi) = \psi$ form a real four-dimensional subspace $S_{\mathbb R}$ with $S = S_{\mathbb R}\oplus iS_{\mathbb R}$ ($\psi = \frac12(\psi + c\psi) + i\cdot\frac1{2i}(\psi - c\psi)$, both parts fixed), invariant under $\mathrm{Spin}(1,3)_0$ by part 3; it is not invariant under $\gamma^5$ (part 2). In a basis with $B = \mathbb 1$ it is the real columns (Example §CB.20.5, 3).
> - Used next: the matrices in three bases and the transpose form (Example §CB.20.5).

^pf-cb-20-4

*Uses:* [[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^def-cb-20-3|Def. §CB.20.3]], [[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^thm-cb-20-2|Theorem §CB.20.2]], [[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-15|Def. §CB.14.15]], [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-16|Def. §CB.15.16]], [[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-13-14|Def. §CB.13.14]], [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-19|Def. §CB.15.19]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-5|Theorem §CB.3.5]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]

> [!example] Example §CB.20.5: The Charge-Conjugation Matrix in Three Bases, and the Transpose Form
> 1. *Chiral basis* ([[§CB.12 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-12-13|Example §CB.12.13]]): $B = -i\gamma^2 = \begin{pmatrix}0 & -i\sigma^2\\ i\sigma^2 & 0\end{pmatrix}$, up to a phase; real, symmetric and unitary, with $B^2 = BB^{\ast} = \mathbb 1$.
> 2. *Dirac basis* $\gamma_D^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, $\gamma_D^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$ (the chiral $\gamma^i$): again $B_D = -i\gamma_D^2 = -i\gamma^2$.
> 3. *A Majorana basis*, all four matrices purely imaginary: $\gamma_M^0 = \begin{pmatrix}0 & \sigma^2\\ \sigma^2 & 0\end{pmatrix}$, $\gamma_M^1 = \begin{pmatrix}i\sigma^3 & 0\\ 0 & i\sigma^3\end{pmatrix}$, $\gamma_M^2 = \begin{pmatrix}0 & -\sigma^2\\ \sigma^2 & 0\end{pmatrix}$, $\gamma_M^3 = \begin{pmatrix}-i\sigma^1 & 0\\ 0 & -i\sigma^1\end{pmatrix}$: $B_M = \mathbb 1$ up to a phase, and $c$ is plain complex conjugation, $c(\psi) = \psi^{\ast}$.
> 4. *Transpose form.* In any Hermitian basis ([[§CB.14 Complex Clifford Algebras and Clifford Modules#^def-cb-14-11|Def. §CB.14.11]]) put $\tilde B \equiv B(\gamma^0)^{\mathsf T}$. Then $\tilde B^{-1}\gamma^\mu\tilde B = -(\gamma^\mu)^{\mathsf T}$ for all $\mu$, $B = \tilde B(\gamma^0)^{\mathsf T}$, and $c(\psi) = B\psi^{\ast} = \tilde B\,(\psi^\dagger\gamma^0)^{\mathsf T}$. In the chiral basis $\tilde B = i\gamma^0\gamma^2$.
>
> In all three bases $BB^{\ast} = +\mathbb 1$, as [[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^thm-cb-20-2|Theorem §CB.20.2]], 5 requires.
>
> *Computation.* **1. Chiral.** Step 9 of the proof of Theorem §CB.20.2. In blocks, $-i\gamma^2 = -i\begin{pmatrix}0 & \sigma^2\\ -\sigma^2 & 0\end{pmatrix}$ with $-i\sigma^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ real. Symmetric: $(\sigma^2)^{\mathsf T} = -\sigma^2$, so $\begin{pmatrix}0 & \sigma^2\\ -\sigma^2 & 0\end{pmatrix}^{\mathsf T} = \begin{pmatrix}0 & -(\sigma^2)^{\mathsf T}\\ (\sigma^2)^{\mathsf T} & 0\end{pmatrix} = \gamma^2$. **2. Dirac.** $\gamma_D^0$ is real, Hermitian, squares to $\mathbb 1$ and anticommutes with each $\gamma^i$: $\operatorname{diag}(\mathbb 1, -\mathbb 1)\gamma^i = \begin{pmatrix}0 & \sigma^i\\ \sigma^i & 0\end{pmatrix} = -\gamma^i\operatorname{diag}(\mathbb 1, -\mathbb 1)$ by block multiplication; with the chiral $\gamma^i$ these are Dirac matrices in a Hermitian basis. Step 9 used only that $\gamma^0$, $\gamma^1$, $\gamma^3$ are real, $\gamma^2$ is imaginary and anti-Hermitian, and the Clifford relations; all hold here, so $-i\gamma_D^2$ works. Cross-check with Theorem §CB.20.2, 4: the real orthogonal $M = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1 & \mathbb 1\\ -\mathbb 1 & \mathbb 1\end{pmatrix}$, $M^{-1} = M^{\mathsf T}$, carries the chiral matrices to these (block multiplication: $M\gamma^0M^{\mathsf T} = \frac12\begin{pmatrix}\mathbb 1 & \mathbb 1\\ \mathbb 1 & -\mathbb 1\end{pmatrix}\begin{pmatrix}\mathbb 1 & -\mathbb 1\\ \mathbb 1 & \mathbb 1\end{pmatrix} = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ and $M\gamma^iM^{\mathsf T} = \frac12\begin{pmatrix}-\sigma^i & \sigma^i\\ -\sigma^i & -\sigma^i\end{pmatrix}\begin{pmatrix}\mathbb 1 & -\mathbb 1\\ \mathbb 1 & \mathbb 1\end{pmatrix} = \gamma^i$); $M^{\ast} = M$, so $B_D = MBM^{-1} = M(-i\gamma^2)M^{-1} = -i\gamma_D^2$. **3. Majorana.** In the block notation $A\otimes C = \begin{pmatrix}a_{11}C & a_{12}C\\ a_{21}C & a_{22}C\end{pmatrix}$, for which block multiplication gives $(A\otimes C)(A'\otimes C') = AA'\otimes CC'$: $\gamma_M^0 = \sigma^1\otimes\sigma^2$, $\gamma_M^1 = \mathbb 1\otimes i\sigma^3$, $\gamma_M^2 = (-i\sigma^2)\otimes\sigma^2$, $\gamma_M^3 = \mathbb 1\otimes(-i\sigma^1)$. Squares: $(\sigma^1)^2\otimes(\sigma^2)^2 = \mathbb 1$; $\mathbb 1\otimes(i\sigma^3)^2 = -\mathbb 1$; $(-i\sigma^2)^2\otimes(\sigma^2)^2 = -\mathbb 1$; $\mathbb 1\otimes(-i\sigma^1)^2 = -\mathbb 1$. Anticommutators: in each of the six pairs exactly one tensor factor holds two distinct, hence anticommuting, Pauli matrices and the other factor holds equal or commuting ones ($\gamma_M^0, \gamma_M^1$: $\sigma^2$ vs $\sigma^3$ in the second factor; $\gamma_M^0, \gamma_M^2$: $\sigma^1$ vs $\sigma^2$ in the first; $\gamma_M^0, \gamma_M^3$: $\sigma^2$ vs $\sigma^1$; $\gamma_M^1, \gamma_M^2$: $\sigma^3$ vs $\sigma^2$; $\gamma_M^1, \gamma_M^3$: $\sigma^3$ vs $\sigma^1$; $\gamma_M^2, \gamma_M^3$: $\sigma^2$ vs $\sigma^1$), so each pair anticommutes ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-22|Theorem §CB.0.22]]). Imaginary: $\sigma^1\otimes\sigma^2$ (real times imaginary), $i\sigma^3$, $(-i\sigma^2)\otimes\sigma^2$ (real times imaginary), $-i\sigma^1$. Hermitian basis: $\gamma_M^0$ is Hermitian and the $\gamma_M^i$ anti-Hermitian (each factor Hermitian or anti-Hermitian; $(A\otimes C)^\dagger = A^\dagger\otimes C^\dagger$). Then $(\gamma_M^\mu)^{\ast} = -\gamma_M^\mu$, so $B_M = \mathbb 1$ satisfies $B_M(\gamma_M^\mu)^{\ast}B_M^{-1} = -\gamma_M^\mu$, and $B_MB_M^{\ast} = \mathbb 1$. **4. Transpose form.** In a Hermitian basis $(\gamma^\mu)^{\ast} = (\gamma^{\mu\dagger})^{\mathsf T} = (\gamma^0\gamma^\mu\gamma^0)^{\mathsf T} = (\gamma^0)^{\mathsf T}(\gamma^\mu)^{\mathsf T}(\gamma^0)^{\mathsf T}$, and $\bigl((\gamma^0)^{\mathsf T}\bigr)^2 = \bigl((\gamma^0)^2\bigr)^{\mathsf T} = \mathbb 1$. So $\tilde B(\gamma^\mu)^{\mathsf T}\tilde B^{-1} = B(\gamma^0)^{\mathsf T}(\gamma^\mu)^{\mathsf T}(\gamma^0)^{\mathsf T}B^{-1} = B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$; multiplying by $\tilde B^{-1}$ on the left and $\tilde B$ on the right, $(\gamma^\mu)^{\mathsf T} = -\tilde B^{-1}\gamma^\mu\tilde B$. Next $\tilde B(\gamma^0)^{\mathsf T} = B\bigl((\gamma^0)^{\mathsf T}\bigr)^2 = B$, and $(\psi^\dagger\gamma^0)^{\mathsf T} = (\gamma^0)^{\mathsf T}\psi^{\ast}$, so $\tilde B(\psi^\dagger\gamma^0)^{\mathsf T} = B\psi^{\ast}$. In the chiral basis $\gamma^0$ is real and symmetric, $(\gamma^0)^{\mathsf T} = \gamma^0$, and $\tilde B = -i\gamma^2\gamma^0 = i\gamma^0\gamma^2$ by anticommutation. (All four parts checked numerically here, including a random unitary change of the chiral basis.)
>
> *Source: chiral and Dirac bases: Example §CB.12.13 and the course's equivalence [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] (the same $M$, called $U_D$ there after PHY 513, Problem Set 6, Problem 3(b)) · the Majorana basis: Schwartz, Quantum Field Theory and the Standard Model, §10.3, eq. (10.74) (p. 170: "In this basis the γ-matrices are purely imaginary"), the course's restatement [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]] · the transpose form: Yu §9.2.1, eqs. (9.98) ($\mathcal C \equiv i\gamma^0\gamma^2$), (9.112), (9.117) · PS §3.6, eq. (3.145) ($-i\gamma^2\psi^{\ast} = -i(\bar\psi\gamma^0\gamma^2)^{\mathsf T}$) · the general relation $B = \tilde B(\gamma^0)^{\mathsf T}$ written here*

^ex-cb-20-5

> [!caution] Caution: Names for the charge-conjugation matrix
> Two matrices go by this name. These notes call **$B$** the matrix acting on $\psi^{\ast}$, $B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$ (Def. §CB.20.1); the course and Peskin–Schroeder use its chiral form $-i\gamma^2$ without a name (Lecture 12, slides 8–9; PS eqs. (3.144)–(3.145)). Yu's **charge-conjugation matrix** $\mathcal C \equiv i\gamma^0\gamma^2$ (eq. (9.98)) is the transpose form $\tilde B = B(\gamma^0)^{\mathsf T}$ of [[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^ex-cb-20-5|Example §CB.20.5]], 4, acting on $\bar\psi^{\mathsf T}$, with $\mathcal C^{-1}\gamma^\mu\mathcal C = -(\gamma^\mu)^{\mathsf T}$ (eq. (9.112)); the course's $-i(\bar\psi\gamma^0\gamma^2)^{\mathsf T}$ is the same $\mathcal C\bar\psi^{\mathsf T}$, since $-i(\gamma^0\gamma^2)^{\mathsf T} = -i\gamma^2\gamma^0 = i\gamma^0\gamma^2$. Yu's $\mathcal C$ is not the $\mathcal C$ of the Hilbert-space operator $U(\mathcal C)$, which names the transformation. The relation $B = \tilde B(\gamma^0)^{\mathsf T}$ holds in Hermitian bases.
>
> *Source: Yu §9.2.1, eqs. (9.98), (9.112), (9.117) · PS §3.6, pp. 70–71 (no name given) · Lecture 12, slides 8–10 · written here*

^cau-cb-20-1

> [!remark]- ★ Remark: Majorana spinors as a real structure
> $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ has no real four-dimensional module ([[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^rem-cb-13-1|§CB.13, ★ Remark: The real classification]]), but the Dirac module carries a conjugate-linear map commuting with $\mathrm{Spin}(1,3)_0$ and squaring to $\mathbb 1$: the charge-conjugation map $c = B\circ K$ of [[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^def-cb-20-3|Def. §CB.20.3]], with $c^2 = \mathbb 1$, commuting with every $\Lambda_{1/2}$ and exchanging $S^+$ with $S^-$ ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^thm-cb-20-4|Theorem §CB.20.4]]; that the two halves are complex conjugates of each other is [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-6|Theorem §CB.19.6]]). Its fixed vectors, $c\psi = \psi$, are the Majorana spinors: a real form $S_{\mathbb R}$ of $S$ for the group (proof of Theorem §CB.20.4, last bullet). In the Majorana basis $B = \mathbb 1$ and $c$ is plain complex conjugation ([[§CB.20 The Lorentz Case IV꞉ Charge Conjugation and the Real Structure#^ex-cb-20-5|Example §CB.20.5]]; [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]]). The Majorana field itself is not yet in the vault (chapter C9; a section on the field is planned).

^rem-cb-20-1

> [!remark]- Connections
> - The course's $-i\gamma^2\psi^{\ast}$ is the chiral-basis form of one basis-free antilinear map $c = B\circ K$ of the Dirac module (Theorems §CB.20.2, §CB.20.4); that $c^2 = +\mathbb 1$ rather than $-\mathbb 1$ is what allows Majorana spinors, the fixed points of $c$ (★ Remark above).
> - **Used in**: Definition §CB.20.1 — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (restated in physics form as [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (physics form: [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background); Theorem §CB.20.2 — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (restated in physics form as [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (physics form: [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background; Connections); Definition §CB.20.3 — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (restated in physics form as [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (physics form: [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background); Theorem §CB.20.4 — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (restated in physics form as [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (cited in [[§C9.7 Charge Conjugation on the Field and Bilinears#^der-c9-7-1|Derivation §C9.7.1]]; physics form: [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background; Connections); Example §CB.20.5 — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (restated in physics form as [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (cited in [[§C9.7 Charge Conjugation on the Field and Bilinears#^thm-c9-7-7|Theorem §C9.7.7]]; physics form: [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background); §CB.20, Caution: Names for the charge-conjugation matrix — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]] (cited in [[§C9.6 Charge Conjugation on Oscillators and Spinors#^thm-c9-6-7|Theorem §C9.6.7]]; Mathematical background), [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]] (cited in [[§C9.7 Charge Conjugation on the Field and Bilinears#^thm-c9-7-1|Theorem §C9.7.1]], [[§C9.7 Charge Conjugation on the Field and Bilinears#^thm-c9-7-7|Theorem §C9.7.7]]; Mathematical background).
