---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 3, 5 (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §§5.5, 21.2, 40.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · the user's PHY 513 notes, Ch. 7 §§7.2, 7.4 (J± and "the algebra decomposes") · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercises 3.1, 3.7 · Peskin & Schroeder, §3.1 · the rest written here.*

The Lie algebra of a matrix Lie group is a *real* Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]]). Physics nevertheless writes Hermitian generators $T_a = iX_a$, forms complex combinations such as $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$, and says that the Lorentz algebra "is two copies of the rotation algebra". What are these objects, and in which sense is each statement true? This section answers with three structures: the complexification $\mathfrak g_{\mathbb C}$, which contains $i\mathfrak g$ and all complex combinations; the correspondence between representations of $\mathfrak g$ on *complex* vector spaces and complex-linear representations of $\mathfrak g_{\mathbb C}$; and real forms, the real algebras with the same complexification, told apart by their conjugations. The Lorentz algebra itself — the split of its complexification and its real forms — is [[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations|§CB.4]]–[[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra|§CB.5]], where $\mathfrak{sl}(2, \mathbb C)$ as a real Lie algebra also begins (continued in [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]]). It builds on [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] and on the course's definitions in [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]]; the representation theory it feeds is [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.6]].

## Complexification

> [!definition] Definition §CB.3.1: Complex Lie Algebra
> A **complex Lie algebra** is a complex vector space $\mathfrak h$ with a complex-bilinear, skew-symmetric bracket $[\cdot,\cdot] : \mathfrak h\times\mathfrak h \to \mathfrak h$ satisfying the Jacobi identity (as in [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], with $\mathbb C$ in place of $\mathbb R$). Homomorphisms of complex Lie algebras are complex-linear ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-2|Def. §CB.2.2]]). Example: $\mathfrak{sl}(2, \mathbb C)$ with the commutator.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.27 (real or complex Lie algebra) · Woit, §5.5*

^def-cb-3-1

> [!definition] Definition §CB.3.2: Complexification of a Real Vector Space
> The **complexification** of a real vector space $V$ is $V_{\mathbb C} = V\times V$, with elements written $u + iv$ ($u, v \in V$), real addition componentwise, and multiplication by $a + ib \in \mathbb C$ given by $(a + ib)(u + iv) = (au - bv) + i(bu + av)$. It is a complex vector space with $\dim_{\mathbb C}V_{\mathbb C} = \dim_{\mathbb R}V$ (a real basis of $V$ is a complex basis of $V_{\mathbb C}$), and $V \subset V_{\mathbb C}$ as the vectors $u + i0$. Its **conjugation** is the real-linear map $c(u + iv) = u - iv$; it is conjugate-linear, $c^2 = \mathbb 1$, and its fixed set is $V$.
>
> *Source: Woit, §5.5 (Definition of $V_{\mathbb C}$) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Def. 3.34 · the conjugation written here*

^def-cb-3-2

The course's definition of the complexified Lie algebra, in a basis (the user's PHY 513 notes, Ch. 7 §7.2):

> [!definition] Definition §CB.3.3: Complexification
> The **complexification** of a real Lie algebra $\mathfrak g$ with basis $\{X_a\}$ is the complex vector space $\mathfrak g_{\mathbb C}$ of all complex combinations $c^aX_a$, with the same bracket extended complex-bilinearly. For rotations $\mathfrak{so}(3)_{\mathbb C} \cong \mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$, spanned by
>
> $$
> J^3, \qquad J^\pm = J^1 \pm iJ^2 \qquad (J^\pm \notin \text{the real span of } J^1, J^2, J^3) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Step 2: $J^\pm \equiv J^1 \pm iJ^2$), §7.4 ($\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$) · Hall §17.4 (the operators $L_\pm = i\pi(F_1) \mp \pi(F_2)$) · Yu §3.3.1, eq. (3.121); the general definition written here*

^def-cb-3-3

> [!theorem] Theorem §CB.3.4: The Complexification of a Real Lie Algebra
> Let $\mathfrak g$ be a real Lie algebra. On $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]]) the bracket
>
> $$
> [X + iY, X' + iY'] = \bigl([X, X'] - [Y, Y']\bigr) + i\bigl([X, Y'] + [Y, X']\bigr)
> $$
>
> is the unique complex-bilinear extension of the bracket of $\mathfrak g$, and makes $\mathfrak g_{\mathbb C}$ a complex Lie algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-1|Def. §CB.3.1]]) with $\dim_{\mathbb C}\mathfrak g_{\mathbb C} = \dim_{\mathbb R}\mathfrak g$; in a basis $\{X_a\}$ of $\mathfrak g$ it is the algebra of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]], with the same real structure constants. The conjugation $c$ satisfies $c[Z, W] = [cZ, cW]$: it is a conjugate-linear automorphism of $\mathfrak g_{\mathbb C}$ with $c^2 = \mathbb 1$ whose fixed set is $\mathfrak g$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Def. 3.34, Prop. 3.35 · Woit, §5.5*

^thm-cb-3-4

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.35 and its proof (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §5.5 (the bracket formula) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). The statements about the conjugation $c$ are written out here.*
>
> **Step 1** (uniqueness). If a bracket on $\mathfrak g_{\mathbb C}$ is complex-bilinear and extends that of $\mathfrak g$, expanding $[X + iY, X' + iY']$ in each slot gives $[X, X'] + i[X, Y'] + i[Y, X'] + i^2[Y, Y']$, which is the displayed formula. So there is at most one such bracket.
>
> **Step 2** (real bilinear, antisymmetric). The formula is real-bilinear because the bracket of $\mathfrak g$ is. Exchanging the two arguments, $[X' + iY', X + iY] = ([X', X] - [Y', Y]) + i([X', Y] + [Y', X]) = -[X + iY, X' + iY']$ by antisymmetry in $\mathfrak g$.
>
> **Step 3** (complex-linear in the first slot; Hall, eq. (3.19)). Since $i(X + iY) = -Y + iX$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]]),
>
> $$
> [i(X + iY), X' + iY'] = [-Y + iX, X' + iY'] = \bigl(-[Y, X'] - [X, Y']\bigr) + i\bigl([X, X'] - [Y, Y']\bigr),
> $$
>
> $$
> i\,[X + iY, X' + iY'] = i\bigl([X, X'] - [Y, Y']\bigr) + i^2\bigl([X, Y'] + [Y, X']\bigr) = \bigl(-[X, Y'] - [Y, X']\bigr) + i\bigl([X, X'] - [Y, Y']\bigr),
> $$
>
> and the two agree. With real bilinearity, the bracket is complex-linear in the first slot; by antisymmetry (Step 2) also in the second.
>
> **Step 4** (Jacobi; Hall's argument). $J(A, B, C) = [A, [B, C]] + [B, [C, A]] + [C, [A, B]]$ is complex-trilinear (Step 3). It vanishes for $A, B, C \in \mathfrak g$ (Jacobi in $\mathfrak g$). Fixing $B, C \in \mathfrak g$, it is complex-linear in $A$ and $\mathfrak g$ spans $\mathfrak g_{\mathbb C}$ over $\mathbb C$, so it vanishes for all $A \in \mathfrak g_{\mathbb C}$; then the same argument in $B$, then in $C$. So $\mathfrak g_{\mathbb C}$ is a complex Lie algebra ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-1|Def. §CB.3.1]]).
>
> **Step 5** (dimension and the basis description). A real basis $\{X_a\}$ of $\mathfrak g$ is a complex basis of $\mathfrak g_{\mathbb C}$ (Def. §CB.3.2), so $\dim_{\mathbb C}\mathfrak g_{\mathbb C} = \dim_{\mathbb R}\mathfrak g$, and by complex bilinearity $[c^aX_a, d^bX_b] = c^ad^bf_{ab}{}^cX_c$ with the real structure constants of $\mathfrak g$: this is the algebra of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]].
>
> **Step 6** (the conjugation). $c(X + iY) = X - iY$ is real-linear. It is conjugate-linear: $c(i(X + iY)) = c(-Y + iX) = -Y - iX = -i(X - iY) = -i\,c(X + iY)$. $c^2 = \mathbb 1$, and $c(X + iY) = X + iY$ iff $Y = 0$, so the fixed set is $\mathfrak g$. For brackets, put $Z = X + iY$, $W = X' + iY'$; then $cZ = X + i(-Y)$, $cW = X' + i(-Y')$, and the formula gives
>
> $$
> [cZ, cW] = \bigl([X, X'] - [Y, Y']\bigr) - i\bigl([X, Y'] + [Y, X']\bigr) = c[Z, W] .
> $$
>
> **What the proof shows.**
> - The complexification is canonical: no basis is needed, and the basis description of the course is a corollary (Step 5).
> - ⚑ By-product: $c$ is an automorphism of the real Lie algebra underlying $\mathfrak g_{\mathbb C}$ but is conjugate-linear; such maps classify real forms → [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-13|Theorem §CB.3.13]].

^pf-cb-3-4

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-1|Def. §CB.3.1]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]]

> [!theorem] Theorem §CB.3.5: Complexification Inside the Matrices
> Let $\mathfrak g \subset M_n(\mathbb C)$ be a real Lie algebra of matrices with $\mathfrak g \cap i\mathfrak g = \{0\}$. Then $X + iY \mapsto X + iY$ (the right side a matrix) is an isomorphism of complex Lie algebras from $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]) onto $\mathfrak g + i\mathfrak g \subset M_n(\mathbb C)$, under which $c$ becomes $X + iY \mapsto X - iY$. Examples ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]): $\mathfrak u(n)_{\mathbb C} \cong \mathfrak{gl}(n, \mathbb C)$, $\mathfrak{su}(n)_{\mathbb C} \cong \mathfrak{sl}(n, \mathbb C)$, $\mathfrak{so}(n)_{\mathbb C} \cong \mathfrak{so}(n, \mathbb C) = \{X \in M_n(\mathbb C) : X^{\mathsf T} = -X\}$, and
>
> $$
> \mathfrak{so}(1,3)_{\mathbb C} \cong \{X \in M_4(\mathbb C) : X^{\mathsf T}\eta + \eta X = 0\}, \qquad c(X) = \bar X .
> $$
>
> The condition $\mathfrak g \cap i\mathfrak g = \{0\}$ fails for $\mathfrak{sl}(2, \mathbb C)$ regarded as a real Lie algebra; that case is Theorem §CB.15.1.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.36 · Woit, §5.5*

^thm-cb-3-5

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.36 and its proof (written there for $\mathfrak{gl}(n, \mathbb R)$ and $\mathfrak u(n)$, the other cases "left as an exercise", done in Steps 4–6) (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §5.5: "V ∩ iV = 0, in which case V_ℂ will just be the larger subspace you get by taking complex linear combinations" (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*
>
> **Step 1** (the map). Define $\iota : \mathfrak g_{\mathbb C} \to M_n(\mathbb C)$, $\iota(X + iY) = X + iY$, the right side computed with matrix operations. It is real-linear, and complex-linear: $\iota(i(X + iY)) = \iota(-Y + iX) = -Y + iX = i(X + iY)$. Its image is $\mathfrak g + i\mathfrak g$.
>
> **Step 2** (injective). If $X + iY = 0$ as matrices, then $X = -iY \in \mathfrak g \cap i\mathfrak g = \{0\}$, so $X = 0$ and then $Y = 0$.
>
> **Step 3** (brackets and conjugation). Expanding the matrix commutator in all four terms, $[X + iY, X' + iY'] = [X, X'] + i[X, Y'] + i[Y, X'] - [Y, Y']$, which is $\iota$ of the bracket of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]. So $\iota$ is an isomorphism of complex Lie algebras onto $\mathfrak g + i\mathfrak g$, and it carries $c(X + iY) = X - iY$ to $X + iY \mapsto X - iY$.
>
> **Step 4** ($\mathfrak u(n)$ and $\mathfrak{su}(n)$; Hall's argument). Every $X \in M_n(\mathbb C)$ is
>
> $$
> X = \frac{X - X^\dagger}2 + i\,\frac{X + X^\dagger}{2i},
> $$
>
> and both fractions are anti-Hermitian: $\bigl(\frac{X - X^\dagger}2\bigr)^\dagger = -\frac{X - X^\dagger}2$ and $\bigl(\frac{X + X^\dagger}{2i}\bigr)^\dagger = \frac{X^\dagger + X}{-2i} = -\frac{X + X^\dagger}{2i}$. A matrix in $\mathfrak u(n) \cap i\mathfrak u(n)$ is anti-Hermitian and Hermitian, hence $0$. So $\mathfrak u(n) + i\mathfrak u(n) = M_n(\mathbb C)$ with $\mathfrak u(n) \cap i\mathfrak u(n) = 0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]). If $\operatorname{tr}X = 0$, the two fractions have traces $\frac{\operatorname{tr}X - \overline{\operatorname{tr}X}}2 = 0$ and $\frac{\operatorname{tr}X + \overline{\operatorname{tr}X}}{2i} = 0$; so $\mathfrak{su}(n) + i\mathfrak{su}(n) = \mathfrak{sl}(n, \mathbb C)$.
>
> **Step 5** ($\mathfrak{so}(n)$). A complex antisymmetric $X$ is $\operatorname{Re}X + i\operatorname{Im}X$ (entrywise real and imaginary parts), and $X^{\mathsf T} = -X$ splits into $(\operatorname{Re}X)^{\mathsf T} = -\operatorname{Re}X$, $(\operatorname{Im}X)^{\mathsf T} = -\operatorname{Im}X$. A real matrix that is also $i$ times a real matrix is $0$. So $\mathfrak{so}(n) + i\mathfrak{so}(n) = \mathfrak{so}(n, \mathbb C)$, $\mathfrak{so}(n) \cap i\mathfrak{so}(n) = 0$.
>
> **Step 6** ($\mathfrak{so}(1,3)$). $\eta$ is real, so $X^{\mathsf T}\eta + \eta X = 0$ for complex $X$ splits into the same equation for $\operatorname{Re}X$ and for $\operatorname{Im}X$; as in Step 5, $\{X \in M_4(\mathbb C) : X^{\mathsf T}\eta + \eta X = 0\} = \mathfrak{so}(1,3) + i\mathfrak{so}(1,3)$ with trivial intersection, and $c(\operatorname{Re}X + i\operatorname{Im}X) = \operatorname{Re}X - i\operatorname{Im}X = \bar X$.
>
> **What the proof shows.**
> - For matrix algebras the abstract complexification is just "allow complex coefficients", *provided* $\mathfrak g \cap i\mathfrak g = 0$; for $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ it is not, and the complexification is twice as large → [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-1|Theorem §CB.15.1]].
> - ⚑ By-product: $\mathfrak u(n)$ and $\mathfrak{gl}(n, \mathbb R)$ have the same complexification $\mathfrak{gl}(n, \mathbb C)$ (Hall, after Prop. 3.36): different real algebras, one complex algebra → real forms, Def. §CB.3.12.

^pf-cb-3-5

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]

## The physicists' i

The course's generators, stated in [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]], and its remark on the factor $i$:

![[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11]]

> [!remark] Remark: The physicist's i
> Writing $T = iX$ makes generators Hermitian, and through them group elements unitary, whenever the representation is unitary ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-17|Theorem §CB.6.17]]). The $i$ is a convention; it has nothing to do with quantum mechanics. The real Lie algebra is the $\mathbb R$-span of the $-iT_a$; the $T_a$ themselves lie in $i\mathfrak g \subset \mathfrak g_{\mathbb C}$, whose real span is not closed under the bracket, so writing $T = iX$ rescales the basis by $i$ and is not a complexification ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]]; the complexification is [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]]). Asked in Lecture 7 whether ordinary 3-vectors are a representation of this "quantum" algebra: they are, $(J^k)_{lm} = -i\varepsilon^{klm}$ acting on $\mathbf x$ is the defining representation, and the algebra is the same whether the thing rotated is a classical vector or a quantum state. For a non-compact group the same $i$ leaves boost generators anti-Hermitian on finite-dimensional representations ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation", "The physicist's i") · Georgi §2.1, below eq. (2.5)*

^rem-cb-3-1

> [!theorem] Theorem §CB.3.6: The Physicists' Generators Rescale the Basis by i; They Do Not Complexify
> Let $\mathfrak g$ be the Lie algebra of a matrix Lie group, $\{X_a\}$ a basis with $[X_a, X_b] = f_{ab}{}^cX_c$ ($f$ real), and $T_a = iX_a$ the physicists' generators ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]]). Then:
> 1. $\mathfrak g = \operatorname{span}_{\mathbb R}\{-iT_a\}$, and the group elements $e^{-i\theta^aT_a} = e^{\theta^aX_a}$ with real $\theta^a$ are the exponentials of $\mathfrak g$;
> 2. each $T_a$ lies in $i\mathfrak g \subset \mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]), and $c(T_a) = -T_a$; $\operatorname{span}_{\mathbb R}\{T_a\} = i\mathfrak g$ and $\operatorname{span}_{\mathbb C}\{T_a\} = \mathfrak g_{\mathbb C}$;
> 3. $[T_a, T_b] = if_{ab}{}^cT_c$;
> 4. $i\mathfrak g$ is closed under the bracket of $\mathfrak g_{\mathbb C}$ if and only if $[\mathfrak g, \mathfrak g] = 0$, because $[iX, iY] = -[X, Y] \in \mathfrak g$ and $\mathfrak g \cap i\mathfrak g = \{0\}$ in $\mathfrak g_{\mathbb C}$. So the real span of Hermitian generators is not a Lie algebra (except for abelian $\mathfrak g$); passing from $X_a$ to $T_a$ rescales the basis by $i$ and is **not** a complexification.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 ("The physicist's i") · Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §5.1 "Physicists' convention" and the remark after Thm. 3.16 · Woit, §5.5 · written here (part 4)*

^thm-cb-3-6

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §5.1 and the remark after Thm. 3.16 ("if you are following the physics convention … condition 3 should be replaced with the condition $-i(XY - YX) \in \mathfrak g$") (https://arxiv.org/abs/math-ph/0005032) · the user's PHY 513 notes, Ch. 7 §7.2 ("The physicist's i"). Part 4 is written here from Theorem §CB.3.4.*
>
> **Step 1** (part 1). $X_a = -iT_a$, so $\mathfrak g = \operatorname{span}_{\mathbb R}\{X_a\} = \operatorname{span}_{\mathbb R}\{-iT_a\}$. For real $\theta^a$, $-i\theta^aT_a = \theta^aX_a \in \mathfrak g$, so $e^{-i\theta^aT_a} = e^{\theta^aX_a}$ is the exponential of an element of $\mathfrak g$, and every element of $\mathfrak g$ is of this form.
>
> **Step 2** (part 2). In $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]), $T_a = iX_a = 0 + iX_a \in i\mathfrak g$, and $c(T_a) = 0 - iX_a = -T_a$. Real combinations: $\operatorname{span}_{\mathbb R}\{T_a\} = i\operatorname{span}_{\mathbb R}\{X_a\} = i\mathfrak g$. Complex combinations: $\operatorname{span}_{\mathbb C}\{T_a\} = \operatorname{span}_{\mathbb C}\{X_a\}$ (multiplication by $i$ is invertible), which is $\mathfrak g_{\mathbb C}$ because $\{X_a\}$ is a complex basis of it.
>
> **Step 3** (part 3). By complex bilinearity of the bracket of $\mathfrak g_{\mathbb C}$ and $X_c = -iT_c$:
>
> $$
> [T_a, T_b] = [iX_a, iX_b] = i^2[X_a, X_b] = -f_{ab}{}^cX_c = -f_{ab}{}^c(-iT_c) = if_{ab}{}^cT_c .
> $$
>
> **Step 4** (part 4). For $X, Y \in \mathfrak g$, $[iX, iY] = -[X, Y] \in \mathfrak g$. In $\mathfrak g_{\mathbb C}$, $\mathfrak g \cap i\mathfrak g = \{0\}$: an element fixed by $c$ (in $\mathfrak g$) and negated by $c$ (in $i\mathfrak g$) is $0$. If $[\mathfrak g, \mathfrak g] = 0$, all brackets in $i\mathfrak g$ vanish and $i\mathfrak g$ is closed. Conversely, if $i\mathfrak g$ is closed under the bracket, then $-[X, Y] = [iX, iY] \in \mathfrak g \cap i\mathfrak g = \{0\}$ for all $X, Y$, so $\mathfrak g$ is abelian.
>
> **What the proof shows.**
> - ⚑ By-product: the $i$ in $[T_a, T_b] = if_{ab}{}^cT_c$ is the price of the rescaling $T_a = iX_a$; the structure constants $f_{ab}{}^c$ are those of the real algebra, unchanged → [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^rem-cb-3-1|§CB.3, Remark: The physicist's i]].
> - "The algebra of the $T_a$" means $\mathfrak g$ written in a rescaled basis, not a new Lie algebra; complex combinations such as $J^\pm$ are elements of $\mathfrak g_{\mathbb C}$ and act through Theorem §CB.3.8.

^pf-cb-3-6

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]

## Representations on complex vector spaces

The course's definition of a representation of a Lie algebra, a real-linear map into the endomorphisms of a *complex* space, stated in [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]], and its complex-linear extension:

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5]]

> [!definition] Definition §CB.3.7: Complex-Linear Extension of a Representation
> A representation $d$ of a real Lie algebra $\mathfrak g$ on a complex space $W$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]]) extends uniquely to a complex-linear representation of $\mathfrak g_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]]), $d(X + iY) = d(X) + i\,d(Y)$; the two have the same invariant subspaces.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Step 2: $J^\pm \equiv J^1 \pm iJ^2$), §7.4 ($\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$) · Hall §17.4 (the operators $L_\pm = i\pi(F_1) \mp \pi(F_2)$) · Yu §3.3.1, eq. (3.121); the general definition written here*

^def-cb-3-7

The ladder operators are not generators of rotations: no real angle produces $e^{-i\theta J^+}$ as a rotation, and $J^+$ is not Hermitian even in a unitary representation, $(J^+)^\dagger = J^-$. They live in the complexified algebra, where the problem of finding representations is purely algebraic. The Lorentz algebra is handled the same way: $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ are complex combinations, and $\mathfrak{so}(1,3)_{\mathbb C}$ splits into two commuting copies of $\mathfrak{sl}(2, \mathbb C)$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-2|Theorem §CB.4.2]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-2|Theorem §CB.5.2]]).

> [!theorem] Theorem §CB.3.8: Complex Representations of 𝔤 Are Complex-Linear Representations of Its Complexification
> Let $\mathfrak g$ be a real Lie algebra and $W$ a complex vector space.
> 1. Every representation $d : \mathfrak g \to \operatorname{End}_{\mathbb C}(W)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]]) extends uniquely to a complex-linear representation $d_{\mathbb C}(X + iY) = d(X) + i\,d(Y)$ of $\mathfrak g_{\mathbb C}$, and every complex-linear representation of $\mathfrak g_{\mathbb C}$ on $W$ restricts to one of $\mathfrak g$; the two operations are inverse bijections.
> 2. Under this bijection, invariant subspaces ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-7|Def. §CB.2.7]]), irreducibility, direct sums ([[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-1|Def. §CB.6.1]]) and intertwiners (complex-linear maps commuting with the action) are the same for $d$ and $d_{\mathbb C}$.
>
> The statement needs $W$ complex: on a real vector space $i\,d(Y)$ is not defined. The ladder operators $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm$ are values of $d_{\mathbb C}$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (cited in [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]]) · Woit, §5.5*

^thm-cb-3-8

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (proof referred there to Ch. 3, Exercise 14; written out in Steps 1–4) (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §5.5: "π′(X + iY) = π′(X) + iπ′(Y) … If the original representation was on a complex vector space V, the extended one will act on the same space" (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*
>
> **Step 1** (the extension is complex-linear). $d_{\mathbb C}(X + iY) = d(X) + i\,d(Y)$ makes sense because $\operatorname{End}_{\mathbb C}(W)$ is a complex vector space. It is real-linear, restricts to $d$ on $\mathfrak g$ ($Y = 0$), and with $i(X + iY) = -Y + iX$:
>
> $$
> d_{\mathbb C}(i(X + iY)) = -d(Y) + i\,d(X) = i\bigl(d(X) + i\,d(Y)\bigr) = i\,d_{\mathbb C}(X + iY) .
> $$
>
> **Step 2** (it preserves brackets). Expanding all four terms and using that $d$ preserves brackets,
>
> $$
> [d_{\mathbb C}(X + iY), d_{\mathbb C}(X' + iY')] = [dX, dX'] - [dY, dY'] + i\bigl([dX, dY'] + [dY, dX']\bigr) = d\bigl([X, X'] - [Y, Y']\bigr) + i\,d\bigl([X, Y'] + [Y, X']\bigr),
> $$
>
> which is $d_{\mathbb C}$ of the bracket of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]].
>
> **Step 3** (uniqueness and the inverse bijection). A complex-linear map on $\mathfrak g_{\mathbb C}$ is fixed by its values on $\mathfrak g$, which spans $\mathfrak g_{\mathbb C}$ over $\mathbb C$; so $d_{\mathbb C}$ is the only complex-linear extension. Conversely, if $\rho$ is a complex-linear representation of $\mathfrak g_{\mathbb C}$, its restriction to the real subalgebra $\mathfrak g$ is real-linear and preserves brackets, and by uniqueness its extension is $\rho$ again. Extension and restriction are inverse.
>
> **Step 4** (part 2). Let $U \subset W$ be a complex subspace. If $d(X)U \subset U$ for all $X$, then $d_{\mathbb C}(X + iY)u = d(X)u + i\,d(Y)u \in U$; conversely $d(X) = d_{\mathbb C}(X)$. So $d$ and $d_{\mathbb C}$ have the same invariant subspaces, hence the same irreducibility. The extension of $d_1 \oplus d_2$ acts blockwise as $(d_1)_{\mathbb C}\oplus(d_2)_{\mathbb C}$. For complex-linear $S : W_1 \to W_2$: if $Sd_1(X) = d_2(X)S$ for all $X$, then $S(d_1(X) + i\,d_1(Y)) = d_2(X)S + i\,d_2(Y)S$ (complex linearity of $S$), and the converse is restriction.
>
> **What the proof shows.**
> - The only input is that $W$ is a complex space, so that $i\,d(Y)$ means something; on a real carrier space one must first complexify the space ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-15|Def. §CB.3.15]]).
> - ⚑ By-product: the ladder operators $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm$ are values of $d_{\mathbb C}$; they are legitimate operators on $W$ even though they are not in the image of $\mathfrak g$, and no group element is their exponential with real parameter.

^pf-cb-3-8

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-5|Def. §CB.2.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-7|Def. §CB.2.7]], [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-6-1|Def. §CB.6.1]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]

## Ideals, simple algebras and real forms

> [!definition] Definition §CB.3.9: Ideal
> An **ideal** of a (real or complex) Lie algebra $\mathfrak g$ is a subspace $\mathfrak a$ with $[X, A] \in \mathfrak a$ for all $X \in \mathfrak g$, $A \in \mathfrak a$.
>
> *Source: written here (standard; the term as in Etingof, Lie Groups and Lie Algebras, MIT 18.755)*

^def-cb-3-9

> [!definition] Definition §CB.3.10: Direct Sum of Lie Algebras
> The **direct sum** $\mathfrak g_1 \oplus \mathfrak g_2$ of Lie algebras (both real or both complex) is the vector space $\mathfrak g_1 \oplus \mathfrak g_2$ with $[(X_1, X_2), (Y_1, Y_2)] = ([X_1, Y_1], [X_2, Y_2])$. A Lie algebra is the direct sum of two ideals $\mathfrak a$, $\mathfrak b$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]) if $\mathfrak g = \mathfrak a \oplus \mathfrak b$ as vector spaces; then $[\mathfrak a, \mathfrak b] = 0$ and $\mathfrak g \cong \mathfrak a \oplus \mathfrak b$ as Lie algebras.
>
> *Source: written here*

^def-cb-3-10

> [!definition] Definition §CB.3.11: Simple Lie Algebra
> A (real or complex) Lie algebra $\mathfrak g$ is **simple** if it is not abelian and its only ideals ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-9|Def. §CB.3.9]]) are $\{0\}$ and $\mathfrak g$.
>
> *Source: written here (standard)*

^def-cb-3-11

> [!definition] Definition §CB.3.12: Real Form
> A **real form** of a complex Lie algebra $\mathfrak h$ is a real Lie subalgebra $\mathfrak g_0 \subset \mathfrak h$ (closed under real combinations and the bracket) with $\mathfrak h = \mathfrak g_0 \oplus i\mathfrak g_0$ as real vector spaces. Then $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_0)_{\mathbb C} \cong \mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]]).
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9 (after Prop. 3.36) · written here*

^def-cb-3-12

> [!theorem] Theorem §CB.3.13: Real Forms Are the Fixed Sets of Conjugations
> Let $\mathfrak h$ be a complex Lie algebra. A **conjugation** of $\mathfrak h$ is a conjugate-linear map $\sigma : \mathfrak h \to \mathfrak h$ with $\sigma^2 = \mathbb 1$ and $\sigma[Z, W] = [\sigma Z, \sigma W]$. Then $\sigma \mapsto \mathfrak h^\sigma = \{Z : \sigma Z = Z\}$ is a bijection from conjugations of $\mathfrak h$ onto real forms of $\mathfrak h$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]]); the inverse sends $\mathfrak g_0$ to $X + iY \mapsto X - iY$ ($X, Y \in \mathfrak g_0$). Two real forms $\mathfrak g_0$, $\mathfrak g_0'$ are isomorphic as real Lie algebras if and only if there is a complex-linear automorphism $\alpha$ of $\mathfrak h$ with $\alpha\sigma = \sigma'\alpha$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 ("real forms of a complex Lie algebra are in natural bijection with its antilinear involutions") · the isomorphism criterion written here*

^thm-cb-3-13

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 lecture notes (2024), §9.4 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf): Etingof states the bijection and calls the converse "easy to see"; Steps 1–3 write it out. The isomorphism criterion (Step 4) is written here.*
>
> **Step 1** (a conjugation gives a real form). Let $\sigma$ be a conjugation, $\mathfrak g_0 = \mathfrak h^\sigma$. It is a real subspace ($\sigma$ is real-linear) and closed under the bracket: $\sigma[Z, W] = [\sigma Z, \sigma W] = [Z, W]$ for $Z, W \in \mathfrak g_0$. Every $Z \in \mathfrak h$ splits as
>
> $$
> Z = \frac{Z + \sigma Z}2 + i\,\frac{Z - \sigma Z}{2i},
> $$
>
> and both fractions are fixed by $\sigma$: $\sigma\frac{Z + \sigma Z}2 = \frac{\sigma Z + Z}2$, and, $\sigma$ being conjugate-linear ($\sigma(\lambda Z) = \bar\lambda\sigma Z$), $\sigma\frac{Z - \sigma Z}{2i} = \frac{\sigma Z - Z}{-2i} = \frac{Z - \sigma Z}{2i}$. If $Z \in \mathfrak g_0 \cap i\mathfrak g_0$, say $Z = iY$ with $\sigma Y = Y$, then $\sigma Z = -iY = -Z$ and $\sigma Z = Z$, so $Z = 0$. Hence $\mathfrak h = \mathfrak g_0 \oplus i\mathfrak g_0$: $\mathfrak g_0$ is a real form ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]]).
>
> **Step 2** (a real form gives a conjugation). Given a real form $\mathfrak g_0$, every $Z \in \mathfrak h$ is uniquely $X + iY$ with $X, Y \in \mathfrak g_0$, so $\sigma(X + iY) = X - iY$ is well defined. Under the isomorphism $(\mathfrak g_0)_{\mathbb C} \cong \mathfrak h$ of Def. §CB.3.12 it is the conjugation $c$ of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], which is conjugate-linear, squares to $\mathbb 1$ and preserves brackets (Step 6 of that proof). Its fixed set is $\mathfrak g_0$.
>
> **Step 3** (the two maps are inverse). Starting from $\sigma$: for $Z = X + iY$ with $X, Y \in \mathfrak h^\sigma$, $\sigma Z = \sigma X + \sigma(iY) = X - iY$, which is the conjugation built from $\mathfrak h^\sigma$ in Step 2. Starting from $\mathfrak g_0$: the fixed set of the conjugation of Step 2 is $\mathfrak g_0$.
>
> **Step 4** (isomorphic real forms). Let $\sigma$, $\sigma'$ have fixed sets $\mathfrak g_0$, $\mathfrak g_0'$. If $\alpha$ is a complex-linear automorphism of $\mathfrak h$ with $\alpha\sigma = \sigma'\alpha$, then for $Z \in \mathfrak g_0$, $\sigma'(\alpha Z) = \alpha\sigma Z = \alpha Z$, so $\alpha(\mathfrak g_0) \subset \mathfrak g_0'$; likewise $\alpha^{-1}\sigma' = \sigma\alpha^{-1}$ gives $\alpha^{-1}(\mathfrak g_0') \subset \mathfrak g_0$. So $\alpha|_{\mathfrak g_0}$ is a real Lie algebra isomorphism $\mathfrak g_0 \to \mathfrak g_0'$. Conversely, given a real isomorphism $f : \mathfrak g_0 \to \mathfrak g_0'$, set $\alpha(X + iY) = f(X) + if(Y)$ ($X, Y \in \mathfrak g_0$). As in Steps 1–2 of the proof of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]] it is complex-linear and preserves brackets; $f^{-1}$ gives its inverse; and $\alpha\sigma(X + iY) = f(X) - if(Y) = \sigma'\alpha(X + iY)$.
>
> **What the proof shows.**
> - A real form is the same datum as a conjugation; to compare two real forms of one complex algebra, compare their conjugations, as Theorem §CB.5.5 does for $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$.
> - ⚑ By-product: non-isomorphic real algebras can share a complexification (Etingof's example: $\mathfrak u(n)$ and $\mathfrak{gl}(n, \mathbb R)$, both real forms of $\mathfrak{gl}(n, \mathbb C)$; here: Theorems §CB.5.5, §CB.5.6).

^pf-cb-3-13

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-12|Def. §CB.3.12]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-4|Theorem §CB.3.4]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-8|Theorem §CB.3.8]]

## Real representations and their complexification

> [!definition] Definition §CB.3.14: Real Representation
> A **real representation** of a matrix Lie group $G$ is a continuous homomorphism $D : G \to GL(U)$ with $U$ a *real* finite-dimensional vector space; of a Lie algebra, a Lie algebra homomorphism $\mathfrak g \to \operatorname{End}_{\mathbb R}(U)$. Example: the vector representation of $SO^+(1,3)$ on $\mathbb R^{1,3}$, and the real two-index tensors $F^{\mu\nu}$.
>
> *Source: written here (Hall, An Elementary Introduction to Groups and Representations, Def. 5.1, real representations)*

^def-cb-3-14

> [!definition] Definition §CB.3.15: Complexification of a Real Representation
> The **complexification** of a real representation $D$ on $U$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-14|Def. §CB.3.14]]) is the representation $D_{\mathbb C}$ on $U_{\mathbb C}$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]]) given by $D_{\mathbb C}(g)(u + iv) = D(g)u + iD(g)v$; it is complex-linear and commutes with the conjugation $c$.
>
> *Source: written here*

^def-cb-3-15

> [!theorem] Theorem §CB.3.16: The Complexification of an Irreducible Real Representation
> Let $D$ be a real representation on $U$ and $D_{\mathbb C}$ its complexification ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-15|Def. §CB.3.15]]).
> 1. $U' \mapsto U'_{\mathbb C}$ is a bijection from the invariant subspaces of $U$ onto the invariant subspaces of $U_{\mathbb C}$ that are mapped to themselves by $c$.
> 2. If $D$ is irreducible, then either $D_{\mathbb C}$ is irreducible, or $U_{\mathbb C} = W \oplus c(W)$ for an irreducible invariant subspace $W$, with $c(W)$ irreducible too.
>
> *Source: written here (the case of two-index tensors: [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], Derivation, step 4)*

^thm-cb-3-16

> [!proof]- Proof
> *Written here, along the route recorded in batch 1; no source with this proof was found in the texts used for CB (Hall's notes, Woit, Meinrenken, Etingof, Smith treat complexification of algebras and of representations but not this dichotomy). The two-index case is worked in [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], Derivation, step 4.*
>
> **Step 1** (invariance commutes with $c$). For $g$ in the group (or $X$ in the algebra), $D_{\mathbb C}(g)c(u + iv) = D(g)u - iD(g)v = c\,D_{\mathbb C}(g)(u + iv)$ ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-15|Def. §CB.3.15]]). So if $W \subset U_{\mathbb C}$ is invariant, so is $c(W)$, a complex subspace because $c$ is conjugate-linear; and intersections and sums of invariant subspaces are invariant.
>
> **Step 2** (part 1: $c$-stable subspaces come from $U$). If $U' \subset U$ is invariant, then $U'_{\mathbb C} = U' + iU'$ is a complex subspace, invariant (Def. §CB.3.15) and $c$-stable. Conversely, let $W \subset U_{\mathbb C}$ be a complex subspace with $c(W) = W$, and put $U' = W \cap U$. For $w = u + iv \in W$ ($u, v \in U$): $u = \frac12(w + cw) \in W$ and $v = \frac1{2i}(w - cw) \in W$, so $u, v \in U'$ and $W = U' + iU' = U'_{\mathbb C}$. If $W$ is invariant, $U'$ is invariant (intersection of invariant $W$ with $U$, which $D_{\mathbb C}$ preserves). The maps $U' \mapsto U'_{\mathbb C}$ and $W \mapsto W \cap U$ are inverse: $U'_{\mathbb C} \cap U = U'$ (the real part of $u + iv$ with $u, v \in U'$).
>
> **Step 3** (part 2: a minimal invariant subspace). Let $D$ be irreducible and suppose $D_{\mathbb C}$ is not. Choose a nonzero invariant $W \subsetneq U_{\mathbb C}$ of smallest dimension; it is irreducible (a smaller nonzero invariant subspace inside it would contradict minimality). $c(W)$ is invariant (Step 1), of the same dimension, and irreducible ($c$ maps invariant subspaces of $c(W)$ bijectively to invariant subspaces of $W$).
>
> **Step 4** ($W \cap c(W) = 0$). $W \cap c(W)$ is invariant and $c$-stable, so by Step 2 it is $U'_{\mathbb C}$ for an invariant $U' \subset U$, which is $0$ or $U$ by irreducibility of $D$. If it were $U_{\mathbb C}$, then $W = U_{\mathbb C}$, excluded. So $W \cap c(W) = 0$.
>
> **Step 5** ($W + c(W) = U_{\mathbb C}$). $W + c(W)$ is invariant, $c$-stable ($c^2 = \mathbb 1$) and nonzero, so by Step 2 it is $U'_{\mathbb C}$ with $U' \ne 0$ invariant, hence $U' = U$ and $W + c(W) = U_{\mathbb C}$. With Step 4, $U_{\mathbb C} = W \oplus c(W)$.
>
> **What the proof shows.**
> - Either complexification keeps an irreducible real representation irreducible, or it splits it into two pieces exchanged by complex conjugation; for real two-forms $F^{\mu\nu}$ the pieces are the self-dual and anti-self-dual parts, $\mathbf E \pm i\mathbf B$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - ⚑ By-product: in the split case $\dim U = 2\dim W$, and the real representation is the complex representation $W$ "regarded as real"; the conjugate piece $c(W)$ carries the conjugate representation (§CB.7).

^pf-cb-3-16

*Uses:* [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-2|Def. §CB.3.2]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-14|Def. §CB.3.14]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-15|Def. §CB.3.15]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-7|Def. §CB.2.7]]

> [!remark]- Connections
> - The duality operator on two-forms has eigenvalues $\pm i$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]): the real representation of $SO^+(1,3)$ on $F^{\mu\nu}$ is irreducible, and its complexification is $W \oplus c(W)$ with $W$ = the self-dual part — the second alternative of Theorem §CB.3.16, and the field-strength picture of Theorem §CB.5.1, 3 ($\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$ are exchanged by conjugation, [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - **Used in**: Theorem §CB.3.4–Theorem §CB.3.8 — the complexified rotation algebra and the ladder operators ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-3|Def. §CB.3.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-3-7|Def. §CB.3.7]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-3|Theorem §CB.9.3]]); Theorem §CB.3.6 — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^rem-cb-3-1|§CB.3, Remark: The physicist's i]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]; Theorem §CB.3.16 — [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]; Definition §CB.3.3 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); Definition §CB.3.7 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded); §CB.3, Remark: The physicist's i — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded).
