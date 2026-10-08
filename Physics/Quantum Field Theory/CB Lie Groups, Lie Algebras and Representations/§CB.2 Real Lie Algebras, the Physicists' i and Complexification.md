---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs]] →

*Sources (proofs written from these, each checked against the text): B. C. Hall, An Elementary Introduction to Groups and Representations, Chs. 3, 5 (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §§5.5, 21.2, 40.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4, Exercise 11.4, Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · the user's PHY 513 notes, Ch. 7 §§7.2, 7.4 (J± and "the algebra decomposes") · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercises 3.1, 3.7 · Peskin & Schroeder, §3.1 · the rest written here.*

The Lie algebra of a matrix Lie group is a *real* Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]). Physics nevertheless writes Hermitian generators $T_a = iX_a$, forms complex combinations such as $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$, and says that the Lorentz algebra "is two copies of the rotation algebra". What are these objects, and in which sense is each statement true? This section answers with three structures: the complexification $\mathfrak g_{\mathbb C}$, which contains $i\mathfrak g$ and all complex combinations; the correspondence between representations of $\mathfrak g$ on *complex* vector spaces and complex-linear representations of $\mathfrak g_{\mathbb C}$; and real forms, the real algebras with the same complexification, told apart by their conjugations. It builds on [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] and on the course's definitions in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]; the representation theory it feeds is [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]].

<!-- MOVE rows (CB-INVENTORY): Def §C3.1.12 and Def §C3.1.13 are embedded below; they are to be moved here in batch 2 (Def §C3.1.12 sharpened to the basis-free definition; Def §C3.1.13 restated as part of Theorem §CB.2.6). -->

## Complexification

> [!definition] Definition §CB.2.1: Complex Lie Algebra
> A **complex Lie algebra** is a complex vector space $\mathfrak h$ with a complex-bilinear, skew-symmetric bracket $[\cdot,\cdot] : \mathfrak h\times\mathfrak h \to \mathfrak h$ satisfying the Jacobi identity (as in [[§49 Lie Bracket and Lie Algebra#^def-49-2|591 Def. §49.2]], with $\mathbb C$ in place of $\mathbb R$). Homomorphisms of complex Lie algebras are complex-linear ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]). Example: $\mathfrak{sl}(2, \mathbb C)$ with the commutator.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §8, Def. 3.27 (real or complex Lie algebra) · Woit, §5.5*

^def-cb-2-1

> [!definition] Definition §CB.2.2: Complexification of a Real Vector Space
> The **complexification** of a real vector space $V$ is $V_{\mathbb C} = V\times V$, with elements written $u + iv$ ($u, v \in V$), real addition componentwise, and multiplication by $a + ib \in \mathbb C$ given by $(a + ib)(u + iv) = (au - bv) + i(bu + av)$. It is a complex vector space with $\dim_{\mathbb C}V_{\mathbb C} = \dim_{\mathbb R}V$ (a real basis of $V$ is a complex basis of $V_{\mathbb C}$), and $V \subset V_{\mathbb C}$ as the vectors $u + i0$. Its **conjugation** is the real-linear map $c(u + iv) = u - iv$; it is conjugate-linear, $c^2 = \mathbb 1$, and its fixed set is $V$.
>
> *Source: Woit, §5.5 (Definition of $V_{\mathbb C}$) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Def. 3.34 · the conjugation written here*

^def-cb-2-2

The course's definition of the complexified Lie algebra, in a basis, is in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12]]

> [!theorem] Theorem §CB.2.3: The Complexification of a Real Lie Algebra
> Let $\mathfrak g$ be a real Lie algebra. On $\mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]]) the bracket
>
> $$
> [X + iY, X' + iY'] = \bigl([X, X'] - [Y, Y']\bigr) + i\bigl([X, Y'] + [Y, X']\bigr)
> $$
>
> is the unique complex-bilinear extension of the bracket of $\mathfrak g$, and makes $\mathfrak g_{\mathbb C}$ a complex Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-1|Def. §CB.2.1]]) with $\dim_{\mathbb C}\mathfrak g_{\mathbb C} = \dim_{\mathbb R}\mathfrak g$; in a basis $\{X_a\}$ of $\mathfrak g$ it is the algebra of [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12|Def. §C3.1.12]], with the same real structure constants. The conjugation $c$ satisfies $c[Z, W] = [cZ, cW]$: it is a conjugate-linear automorphism of $\mathfrak g_{\mathbb C}$ with $c^2 = \mathbb 1$ whose fixed set is $\mathfrak g$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Def. 3.34, Prop. 3.35 · Woit, §5.5*

^thm-cb-2-3

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.35 and its proof (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §5.5 (the bracket formula) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). The statements about the conjugation $c$ are written out here.*
>
> **Step 1** (uniqueness). If a bracket on $\mathfrak g_{\mathbb C}$ is complex-bilinear and extends that of $\mathfrak g$, expanding $[X + iY, X' + iY']$ in each slot gives $[X, X'] + i[X, Y'] + i[Y, X'] + i^2[Y, Y']$, which is the displayed formula. So there is at most one such bracket.
>
> **Step 2** (real bilinear, antisymmetric). The formula is real-bilinear because the bracket of $\mathfrak g$ is. Exchanging the two arguments, $[X' + iY', X + iY] = ([X', X] - [Y', Y]) + i([X', Y] + [Y', X]) = -[X + iY, X' + iY']$ by antisymmetry in $\mathfrak g$.
>
> **Step 3** (complex-linear in the first slot; Hall, eq. (3.19)). Since $i(X + iY) = -Y + iX$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]]),
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
> **Step 4** (Jacobi; Hall's argument). $J(A, B, C) = [A, [B, C]] + [B, [C, A]] + [C, [A, B]]$ is complex-trilinear (Step 3). It vanishes for $A, B, C \in \mathfrak g$ (Jacobi in $\mathfrak g$). Fixing $B, C \in \mathfrak g$, it is complex-linear in $A$ and $\mathfrak g$ spans $\mathfrak g_{\mathbb C}$ over $\mathbb C$, so it vanishes for all $A \in \mathfrak g_{\mathbb C}$; then the same argument in $B$, then in $C$. So $\mathfrak g_{\mathbb C}$ is a complex Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-1|Def. §CB.2.1]]).
>
> **Step 5** (dimension and the basis description). A real basis $\{X_a\}$ of $\mathfrak g$ is a complex basis of $\mathfrak g_{\mathbb C}$ (Def. §CB.2.2), so $\dim_{\mathbb C}\mathfrak g_{\mathbb C} = \dim_{\mathbb R}\mathfrak g$, and by complex bilinearity $[c^aX_a, d^bX_b] = c^ad^bf_{ab}{}^cX_c$ with the real structure constants of $\mathfrak g$: this is the algebra of [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12|Def. §C3.1.12]].
>
> **Step 6** (the conjugation). $c(X + iY) = X - iY$ is real-linear. It is conjugate-linear: $c(i(X + iY)) = c(-Y + iX) = -Y - iX = -i(X - iY) = -i\,c(X + iY)$. $c^2 = \mathbb 1$, and $c(X + iY) = X + iY$ iff $Y = 0$, so the fixed set is $\mathfrak g$. For brackets, put $Z = X + iY$, $W = X' + iY'$; then $cZ = X + i(-Y)$, $cW = X' + i(-Y')$, and the formula gives
>
> $$
> [cZ, cW] = \bigl([X, X'] - [Y, Y']\bigr) - i\bigl([X, Y'] + [Y, X']\bigr) = c[Z, W] .
> $$
>
> **What the proof shows.**
> - The complexification is canonical: no basis is needed, and the basis description of the course is a corollary (Step 5).
> - ⚑ By-product: $c$ is an automorphism of the real Lie algebra underlying $\mathfrak g_{\mathbb C}$ but is conjugate-linear; such maps classify real forms → [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]].

^pf-cb-2-3

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-1|Def. §CB.2.1]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12|Def. §C3.1.12]]

> [!theorem] Theorem §CB.2.4: Complexification Inside the Matrices
> Let $\mathfrak g \subset M_n(\mathbb C)$ be a real Lie algebra of matrices with $\mathfrak g \cap i\mathfrak g = \{0\}$. Then $X + iY \mapsto X + iY$ (the right side a matrix) is an isomorphism of complex Lie algebras from $\mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]) onto $\mathfrak g + i\mathfrak g \subset M_n(\mathbb C)$, under which $c$ becomes $X + iY \mapsto X - iY$. Examples ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]): $\mathfrak u(n)_{\mathbb C} \cong \mathfrak{gl}(n, \mathbb C)$, $\mathfrak{su}(n)_{\mathbb C} \cong \mathfrak{sl}(n, \mathbb C)$, $\mathfrak{so}(n)_{\mathbb C} \cong \mathfrak{so}(n, \mathbb C) = \{X \in M_n(\mathbb C) : X^{\mathsf T} = -X\}$, and
>
> $$
> \mathfrak{so}(1,3)_{\mathbb C} \cong \{X \in M_4(\mathbb C) : X^{\mathsf T}\eta + \eta X = 0\}, \qquad c(X) = \bar X .
> $$
>
> The condition $\mathfrak g \cap i\mathfrak g = \{0\}$ fails for $\mathfrak{sl}(2, \mathbb C)$ regarded as a real Lie algebra; that case is Theorem §CB.2.18.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.36 · Woit, §5.5*

^thm-cb-2-4

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9, Prop. 3.36 and its proof (written there for $\mathfrak{gl}(n, \mathbb R)$ and $\mathfrak u(n)$, the other cases "left as an exercise", done in Steps 4–6) (https://arxiv.org/abs/math-ph/0005032) · P. Woit, Quantum Theory, Groups and Representations, §5.5: "V ∩ iV = 0, in which case V_ℂ will just be the larger subspace you get by taking complex linear combinations" (https://www.math.columbia.edu/~woit/QM/qmbook.pdf).*
>
> **Step 1** (the map). Define $\iota : \mathfrak g_{\mathbb C} \to M_n(\mathbb C)$, $\iota(X + iY) = X + iY$, the right side computed with matrix operations. It is real-linear, and complex-linear: $\iota(i(X + iY)) = \iota(-Y + iX) = -Y + iX = i(X + iY)$. Its image is $\mathfrak g + i\mathfrak g$.
>
> **Step 2** (injective). If $X + iY = 0$ as matrices, then $X = -iY \in \mathfrak g \cap i\mathfrak g = \{0\}$, so $X = 0$ and then $Y = 0$.
>
> **Step 3** (brackets and conjugation). Expanding the matrix commutator in all four terms, $[X + iY, X' + iY'] = [X, X'] + i[X, Y'] + i[Y, X'] - [Y, Y']$, which is $\iota$ of the bracket of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]. So $\iota$ is an isomorphism of complex Lie algebras onto $\mathfrak g + i\mathfrak g$, and it carries $c(X + iY) = X - iY$ to $X + iY \mapsto X - iY$.
>
> **Step 4** ($\mathfrak u(n)$ and $\mathfrak{su}(n)$; Hall's argument). Every $X \in M_n(\mathbb C)$ is
>
> $$
> X = \frac{X - X^\dagger}2 + i\,\frac{X + X^\dagger}{2i},
> $$
>
> and both fractions are anti-Hermitian: $\bigl(\frac{X - X^\dagger}2\bigr)^\dagger = -\frac{X - X^\dagger}2$ and $\bigl(\frac{X + X^\dagger}{2i}\bigr)^\dagger = \frac{X^\dagger + X}{-2i} = -\frac{X + X^\dagger}{2i}$. A matrix in $\mathfrak u(n) \cap i\mathfrak u(n)$ is anti-Hermitian and Hermitian, hence $0$. So $\mathfrak u(n) + i\mathfrak u(n) = M_n(\mathbb C)$ with $\mathfrak u(n) \cap i\mathfrak u(n) = 0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). If $\operatorname{tr}X = 0$, the two fractions have traces $\frac{\operatorname{tr}X - \overline{\operatorname{tr}X}}2 = 0$ and $\frac{\operatorname{tr}X + \overline{\operatorname{tr}X}}{2i} = 0$; so $\mathfrak{su}(n) + i\mathfrak{su}(n) = \mathfrak{sl}(n, \mathbb C)$.
>
> **Step 5** ($\mathfrak{so}(n)$). A complex antisymmetric $X$ is $\operatorname{Re}X + i\operatorname{Im}X$ (entrywise real and imaginary parts), and $X^{\mathsf T} = -X$ splits into $(\operatorname{Re}X)^{\mathsf T} = -\operatorname{Re}X$, $(\operatorname{Im}X)^{\mathsf T} = -\operatorname{Im}X$. A real matrix that is also $i$ times a real matrix is $0$. So $\mathfrak{so}(n) + i\mathfrak{so}(n) = \mathfrak{so}(n, \mathbb C)$, $\mathfrak{so}(n) \cap i\mathfrak{so}(n) = 0$.
>
> **Step 6** ($\mathfrak{so}(1,3)$). $\eta$ is real, so $X^{\mathsf T}\eta + \eta X = 0$ for complex $X$ splits into the same equation for $\operatorname{Re}X$ and for $\operatorname{Im}X$; as in Step 5, $\{X \in M_4(\mathbb C) : X^{\mathsf T}\eta + \eta X = 0\} = \mathfrak{so}(1,3) + i\mathfrak{so}(1,3)$ with trivial intersection, and $c(\operatorname{Re}X + i\operatorname{Im}X) = \operatorname{Re}X - i\operatorname{Im}X = \bar X$.
>
> **What the proof shows.**
> - For matrix algebras the abstract complexification is just "allow complex coefficients", *provided* $\mathfrak g \cap i\mathfrak g = 0$; for $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ it is not, and the complexification is twice as large → [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]].
> - ⚑ By-product: $\mathfrak u(n)$ and $\mathfrak{gl}(n, \mathbb R)$ have the same complexification $\mathfrak{gl}(n, \mathbb C)$ (Hall, after Prop. 3.36): different real algebras, one complex algebra → real forms, Def. §CB.2.10.

^pf-cb-2-4

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]

## The physicists' i

The course's generators and its remark on the factor $i$, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-3]]

> [!theorem] Theorem §CB.2.5: The Physicists' Generators Rescale the Basis by i; They Do Not Complexify
> Let $\mathfrak g$ be the Lie algebra of a matrix Lie group, $\{X_a\}$ a basis with $[X_a, X_b] = f_{ab}{}^cX_c$ ($f$ real), and $T_a = iX_a$ the physicists' generators ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]]). Then:
> 1. $\mathfrak g = \operatorname{span}_{\mathbb R}\{-iT_a\}$, and the group elements $e^{-i\theta^aT_a} = e^{\theta^aX_a}$ with real $\theta^a$ are the exponentials of $\mathfrak g$;
> 2. each $T_a$ lies in $i\mathfrak g \subset \mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]), and $c(T_a) = -T_a$; $\operatorname{span}_{\mathbb R}\{T_a\} = i\mathfrak g$ and $\operatorname{span}_{\mathbb C}\{T_a\} = \mathfrak g_{\mathbb C}$;
> 3. $[T_a, T_b] = if_{ab}{}^cT_c$;
> 4. $i\mathfrak g$ is closed under the bracket of $\mathfrak g_{\mathbb C}$ if and only if $[\mathfrak g, \mathfrak g] = 0$, because $[iX, iY] = -[X, Y] \in \mathfrak g$ and $\mathfrak g \cap i\mathfrak g = \{0\}$ in $\mathfrak g_{\mathbb C}$. So the real span of Hermitian generators is not a Lie algebra (except for abelian $\mathfrak g$); passing from $X_a$ to $T_a$ rescales the basis by $i$ and is **not** a complexification.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 ("The physicist's i") · Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §5.1 "Physicists' convention" and the remark after Thm. 3.16 · Woit, §5.5 · written here (part 4)*

^thm-cb-2-5

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 3, §5.1 and the remark after Thm. 3.16 ("if you are following the physics convention … condition 3 should be replaced with the condition $-i(XY - YX) \in \mathfrak g$") (https://arxiv.org/abs/math-ph/0005032) · the user's PHY 513 notes, Ch. 7 §7.2 ("The physicist's i"). Part 4 is written here from Theorem §CB.2.3.*
>
> **Step 1** (part 1). $X_a = -iT_a$, so $\mathfrak g = \operatorname{span}_{\mathbb R}\{X_a\} = \operatorname{span}_{\mathbb R}\{-iT_a\}$. For real $\theta^a$, $-i\theta^aT_a = \theta^aX_a \in \mathfrak g$, so $e^{-i\theta^aT_a} = e^{\theta^aX_a}$ is the exponential of an element of $\mathfrak g$, and every element of $\mathfrak g$ is of this form.
>
> **Step 2** (part 2). In $\mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]), $T_a = iX_a = 0 + iX_a \in i\mathfrak g$, and $c(T_a) = 0 - iX_a = -T_a$. Real combinations: $\operatorname{span}_{\mathbb R}\{T_a\} = i\operatorname{span}_{\mathbb R}\{X_a\} = i\mathfrak g$. Complex combinations: $\operatorname{span}_{\mathbb C}\{T_a\} = \operatorname{span}_{\mathbb C}\{X_a\}$ (multiplication by $i$ is invertible), which is $\mathfrak g_{\mathbb C}$ because $\{X_a\}$ is a complex basis of it.
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
> - ⚑ By-product: the $i$ in $[T_a, T_b] = if_{ab}{}^cT_c$ is the price of the rescaling $T_a = iX_a$; the structure constants $f_{ab}{}^c$ are those of the real algebra, unchanged → [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-3|§C3.1, Remark: The physicist's i]].
> - "The algebra of the $T_a$" means $\mathfrak g$ written in a rescaled basis, not a new Lie algebra; complex combinations such as $J^\pm$ are elements of $\mathfrak g_{\mathbb C}$ and act through Theorem §CB.2.6.

^pf-cb-2-5

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]

## Representations on complex vector spaces

The course's definition of a representation of a Lie algebra, a real-linear map into the endomorphisms of a *complex* space, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]], and its complex-linear extension:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-13]]

> [!theorem] Theorem §CB.2.6: Complex Representations of 𝔤 Are Complex-Linear Representations of Its Complexification
> Let $\mathfrak g$ be a real Lie algebra and $W$ a complex vector space.
> 1. Every representation $d : \mathfrak g \to \operatorname{End}_{\mathbb C}(W)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]) extends uniquely to a complex-linear representation $d_{\mathbb C}(X + iY) = d(X) + i\,d(Y)$ of $\mathfrak g_{\mathbb C}$, and every complex-linear representation of $\mathfrak g_{\mathbb C}$ on $W$ restricts to one of $\mathfrak g$; the two operations are inverse bijections.
> 2. Under this bijection, invariant subspaces ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]), irreducibility, direct sums ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]]) and intertwiners (complex-linear maps commuting with the action) are the same for $d$ and $d_{\mathbb C}$.
>
> The statement needs $W$ complex: on a real vector space $i\,d(Y)$ is not defined. The ladder operators $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm$ are values of $d_{\mathbb C}$.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-13|Def. §C3.1.13]]) · Woit, §5.5*

^thm-cb-2-6

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
> which is $d_{\mathbb C}$ of the bracket of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]].
>
> **Step 3** (uniqueness and the inverse bijection). A complex-linear map on $\mathfrak g_{\mathbb C}$ is fixed by its values on $\mathfrak g$, which spans $\mathfrak g_{\mathbb C}$ over $\mathbb C$; so $d_{\mathbb C}$ is the only complex-linear extension. Conversely, if $\rho$ is a complex-linear representation of $\mathfrak g_{\mathbb C}$, its restriction to the real subalgebra $\mathfrak g$ is real-linear and preserves brackets, and by uniqueness its extension is $\rho$ again. Extension and restriction are inverse.
>
> **Step 4** (part 2). Let $U \subset W$ be a complex subspace. If $d(X)U \subset U$ for all $X$, then $d_{\mathbb C}(X + iY)u = d(X)u + i\,d(Y)u \in U$; conversely $d(X) = d_{\mathbb C}(X)$. So $d$ and $d_{\mathbb C}$ have the same invariant subspaces, hence the same irreducibility. The extension of $d_1 \oplus d_2$ acts blockwise as $(d_1)_{\mathbb C}\oplus(d_2)_{\mathbb C}$. For complex-linear $S : W_1 \to W_2$: if $Sd_1(X) = d_2(X)S$ for all $X$, then $S(d_1(X) + i\,d_1(Y)) = d_2(X)S + i\,d_2(Y)S$ (complex linearity of $S$), and the converse is restriction.
>
> **What the proof shows.**
> - The only input is that $W$ is a complex space, so that $i\,d(Y)$ means something; on a real carrier space one must first complexify the space ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]).
> - ⚑ By-product: the ladder operators $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm$ are values of $d_{\mathbb C}$; they are legitimate operators on $W$ even though they are not in the image of $\mathfrak g$, and no group element is their exponential with real parameter.

^pf-cb-2-6

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]

## Ideals, simple algebras and real forms

> [!definition] Definition §CB.2.7: Ideal
> An **ideal** of a (real or complex) Lie algebra $\mathfrak g$ is a subspace $\mathfrak a$ with $[X, A] \in \mathfrak a$ for all $X \in \mathfrak g$, $A \in \mathfrak a$.
>
> *Source: written here (standard; the term as in Etingof, Lie Groups and Lie Algebras, MIT 18.755)*

^def-cb-2-7

> [!definition] Definition §CB.2.8: Direct Sum of Lie Algebras
> The **direct sum** $\mathfrak g_1 \oplus \mathfrak g_2$ of Lie algebras (both real or both complex) is the vector space $\mathfrak g_1 \oplus \mathfrak g_2$ with $[(X_1, X_2), (Y_1, Y_2)] = ([X_1, Y_1], [X_2, Y_2])$. A Lie algebra is the direct sum of two ideals $\mathfrak a$, $\mathfrak b$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]) if $\mathfrak g = \mathfrak a \oplus \mathfrak b$ as vector spaces; then $[\mathfrak a, \mathfrak b] = 0$ and $\mathfrak g \cong \mathfrak a \oplus \mathfrak b$ as Lie algebras.
>
> *Source: written here*

^def-cb-2-8

> [!definition] Definition §CB.2.9: Simple Lie Algebra
> A (real or complex) Lie algebra $\mathfrak g$ is **simple** if it is not abelian and its only ideals ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]) are $\{0\}$ and $\mathfrak g$.
>
> *Source: written here (standard)*

^def-cb-2-9

> [!definition] Definition §CB.2.10: Real Form
> A **real form** of a complex Lie algebra $\mathfrak h$ is a real Lie subalgebra $\mathfrak g_0 \subset \mathfrak h$ (closed under real combinations and the bracket) with $\mathfrak h = \mathfrak g_0 \oplus i\mathfrak g_0$ as real vector spaces. Then $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_0)_{\mathbb C} \cong \mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]).
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9 (after Prop. 3.36) · written here*

^def-cb-2-10

> [!theorem] Theorem §CB.2.11: Real Forms Are the Fixed Sets of Conjugations
> Let $\mathfrak h$ be a complex Lie algebra. A **conjugation** of $\mathfrak h$ is a conjugate-linear map $\sigma : \mathfrak h \to \mathfrak h$ with $\sigma^2 = \mathbb 1$ and $\sigma[Z, W] = [\sigma Z, \sigma W]$. Then $\sigma \mapsto \mathfrak h^\sigma = \{Z : \sigma Z = Z\}$ is a bijection from conjugations of $\mathfrak h$ onto real forms of $\mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]); the inverse sends $\mathfrak g_0$ to $X + iY \mapsto X - iY$ ($X, Y \in \mathfrak g_0$). Two real forms $\mathfrak g_0$, $\mathfrak g_0'$ are isomorphic as real Lie algebras if and only if there is a complex-linear automorphism $\alpha$ of $\mathfrak h$ with $\alpha\sigma = \sigma'\alpha$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 ("real forms of a complex Lie algebra are in natural bijection with its antilinear involutions") · the isomorphism criterion written here*

^thm-cb-2-11

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 lecture notes (2024), §9.4 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf): Etingof states the bijection and calls the converse "easy to see"; Steps 1–3 write it out. The isomorphism criterion (Step 4) is written here.*
>
> **Step 1** (a conjugation gives a real form). Let $\sigma$ be a conjugation, $\mathfrak g_0 = \mathfrak h^\sigma$. It is a real subspace ($\sigma$ is real-linear) and closed under the bracket: $\sigma[Z, W] = [\sigma Z, \sigma W] = [Z, W]$ for $Z, W \in \mathfrak g_0$. Every $Z \in \mathfrak h$ splits as
>
> $$
> Z = \frac{Z + \sigma Z}2 + i\,\frac{Z - \sigma Z}{2i},
> $$
>
> and both fractions are fixed by $\sigma$: $\sigma\frac{Z + \sigma Z}2 = \frac{\sigma Z + Z}2$, and, $\sigma$ being conjugate-linear ($\sigma(\lambda Z) = \bar\lambda\sigma Z$), $\sigma\frac{Z - \sigma Z}{2i} = \frac{\sigma Z - Z}{-2i} = \frac{Z - \sigma Z}{2i}$. If $Z \in \mathfrak g_0 \cap i\mathfrak g_0$, say $Z = iY$ with $\sigma Y = Y$, then $\sigma Z = -iY = -Z$ and $\sigma Z = Z$, so $Z = 0$. Hence $\mathfrak h = \mathfrak g_0 \oplus i\mathfrak g_0$: $\mathfrak g_0$ is a real form ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]).
>
> **Step 2** (a real form gives a conjugation). Given a real form $\mathfrak g_0$, every $Z \in \mathfrak h$ is uniquely $X + iY$ with $X, Y \in \mathfrak g_0$, so $\sigma(X + iY) = X - iY$ is well defined. Under the isomorphism $(\mathfrak g_0)_{\mathbb C} \cong \mathfrak h$ of Def. §CB.2.10 it is the conjugation $c$ of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]], which is conjugate-linear, squares to $\mathbb 1$ and preserves brackets (Step 6 of that proof). Its fixed set is $\mathfrak g_0$.
>
> **Step 3** (the two maps are inverse). Starting from $\sigma$: for $Z = X + iY$ with $X, Y \in \mathfrak h^\sigma$, $\sigma Z = \sigma X + \sigma(iY) = X - iY$, which is the conjugation built from $\mathfrak h^\sigma$ in Step 2. Starting from $\mathfrak g_0$: the fixed set of the conjugation of Step 2 is $\mathfrak g_0$.
>
> **Step 4** (isomorphic real forms). Let $\sigma$, $\sigma'$ have fixed sets $\mathfrak g_0$, $\mathfrak g_0'$. If $\alpha$ is a complex-linear automorphism of $\mathfrak h$ with $\alpha\sigma = \sigma'\alpha$, then for $Z \in \mathfrak g_0$, $\sigma'(\alpha Z) = \alpha\sigma Z = \alpha Z$, so $\alpha(\mathfrak g_0) \subset \mathfrak g_0'$; likewise $\alpha^{-1}\sigma' = \sigma\alpha^{-1}$ gives $\alpha^{-1}(\mathfrak g_0') \subset \mathfrak g_0$. So $\alpha|_{\mathfrak g_0}$ is a real Lie algebra isomorphism $\mathfrak g_0 \to \mathfrak g_0'$. Conversely, given a real isomorphism $f : \mathfrak g_0 \to \mathfrak g_0'$, set $\alpha(X + iY) = f(X) + if(Y)$ ($X, Y \in \mathfrak g_0$). As in Steps 1–2 of the proof of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]] it is complex-linear and preserves brackets; $f^{-1}$ gives its inverse; and $\alpha\sigma(X + iY) = f(X) - if(Y) = \sigma'\alpha(X + iY)$.
>
> **What the proof shows.**
> - A real form is the same datum as a conjugation; to compare two real forms of one complex algebra, compare their conjugations, as Theorem §CB.2.14 does for $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$.
> - ⚑ By-product: non-isomorphic real algebras can share a complexification (Etingof's example: $\mathfrak u(n)$ and $\mathfrak{gl}(n, \mathbb R)$, both real forms of $\mathfrak{gl}(n, \mathbb C)$; here: Theorems §CB.2.14, §CB.2.15).

^pf-cb-2-11

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]

## The Lorentz algebra: the split J± = ½(J ± iK) and the conjugation picture

> [!theorem] Theorem §CB.2.12: The Split of the Complexified Lorentz Algebra
> Let $J_i$, $K_i$ be the rotation and boost generators of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), so that $-iJ_i$, $-iK_i$ are a basis of $\mathfrak{so}(1,3)$ and $J_i, K_i \in i\,\mathfrak{so}(1,3) \subset \mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-5|Theorem §CB.2.5]]). In $\mathfrak{so}(1,3)_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]) put
>
> $$
> J_{\pm i} = \tfrac12\bigl(J_i \pm iK_i\bigr) .
> $$
>
> 1. **Both directions.** $J_i = J_{+i} + J_{-i}$ and $K_i = -i\bigl(J_{+i} - J_{-i}\bigr)$; so $\{J_{+i}, J_{-i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, while no nonzero complex combination of the $J_{+i}$ alone lies in $\mathfrak{so}(1,3)$ or in $i\,\mathfrak{so}(1,3)$.
> 2. **Two commuting copies of 𝔰𝔩(2,ℂ).** $[J_{+i}, J_{+j}] = i\varepsilon_{ijk}J_{+k}$, $[J_{-i}, J_{-j}] = i\varepsilon_{ijk}J_{-k}$, $[J_{+i}, J_{-j}] = 0$. Hence $\mathfrak a_\pm = \operatorname{span}_{\mathbb C}\{J_{\pm i}\}$ are ideals ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]), $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+ \oplus \mathfrak a_-$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]]), and $J_{\pm i} \mapsto \frac12\sigma^i$ is an isomorphism $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C) \cong \mathfrak{su}(2)_{\mathbb C}$, the complexified rotation algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]).
> 3. **The conjugation exchanges the copies.** The conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ with fixed set $\mathfrak{so}(1,3)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]) satisfies $c(J_{\pm i}) = -J_{\mp i}$, so $c(\mathfrak a_\pm) = \mathfrak a_\mp$, and
>
> $$
> \mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Woit, §40.2 (the split $A_j$, $B_j$ and $\mathfrak{so}(3,1)\otimes\mathbb C = \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$) · Yu, Exercise 3.1 · written here (parts 1 and 3)*

^thm-cb-2-12

> [!proof]- Proof
> *Source: the user's PHY 513 notes, Ch. 7 §7.4, Derivation "The rotation–boost algebra and its complex split" (the brackets of part 2, as in [[§C3.2 The Lorentz Algebra#^der-c3-2-1c|Derivation §C3.2.1 (the J, K form and the J± split)]], steps 6–8) · P. Woit, Quantum Theory, Groups and Representations, §40.2 (the same split in the real basis $l_j = -iJ_j$, $k_j = -iK_j$; "this construction … requires that we complexify") (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Parts 1 and 3 are written here from Theorems §CB.2.3–§CB.2.5.*
>
> **Step 1** (where $J_i$, $K_i$ live). $-iJ_i$, $-iK_i$ are the generators $M^{jk}$, $M^{0i}$ of the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), a real basis of $\mathfrak{so}(1,3)$, hence a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$, which [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]] realizes inside $M_4(\mathbb C)$. So $J_i = i(-iJ_i)$, $K_i = i(-iK_i)$ lie in $i\,\mathfrak{so}(1,3)$, and $\{J_i, K_i\}$ is also a complex basis. Their brackets, computed as $4\times4$ matrices, are ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]])
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, K_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, J_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, K_j] = -i\varepsilon_{ijk}J_k ,
> $$
>
> the third from the second by antisymmetry and $\varepsilon_{jik} = -\varepsilon_{ijk}$.
>
> **Step 2** (part 1: both directions). Adding and subtracting the definitions, $J_{+i} + J_{-i} = J_i$ and $J_{+i} - J_{-i} = iK_i$, so $K_i = -i(J_{+i} - J_{-i})$. The change of basis $\{J_i, K_i\} \leftrightarrow \{J_{+i}, J_{-i}\}$ is invertible over $\mathbb C$, so $\{J_{\pm i}\}$ is a complex basis of $\mathfrak{so}(1,3)_{\mathbb C}$.
>
> **Step 3** (part 2: the copies commute; user's notes, step 6). By bilinearity, all four terms, and Step 1:
>
> $$
> [J_{+i}, J_{-j}] = \tfrac14\bigl([J_i, J_j] - i[J_i, K_j] + i[K_i, J_j] + [K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k + \varepsilon_{ijk}K_k - \varepsilon_{ijk}K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 4** (part 2: each copy is an angular momentum; user's notes, step 7). With the same sign in both slots, $(\pm i)^2 = -1$:
>
> $$
> [J_{\pm i}, J_{\pm j}] = \tfrac14\bigl([J_i, J_j] \pm i[J_i, K_j] \pm i[K_i, J_j] - [K_i, K_j]\bigr) = \tfrac14\bigl(2i\varepsilon_{ijk}J_k \mp 2\varepsilon_{ijk}K_k\bigr) = i\varepsilon_{ijk}\cdot\tfrac12\bigl(J_k \pm iK_k\bigr) = i\varepsilon_{ijk}J_{\pm k} ,
> $$
>
> using $\mp\varepsilon K_k = i\varepsilon(\pm iK_k)$.
>
> **Step 5** (part 2: ideals and the isomorphism). By Steps 3–4, $[\mathfrak a_\pm, \mathfrak a_\pm] \subset \mathfrak a_\pm$ and $[\mathfrak a_\mp, \mathfrak a_\pm] = 0$, so $[\mathfrak{so}(1,3)_{\mathbb C}, \mathfrak a_\pm] \subset \mathfrak a_\pm$: both are ideals ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]), and with Step 2 the space is their direct sum, a direct sum of Lie algebras ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]]). The matrices $\tau^i = \frac12\sigma^i$ are a complex basis of the traceless $2\times2$ matrices $\mathfrak{sl}(2, \mathbb C)$ (three independent traceless matrices, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]: complex dimension $3$) with $[\tau^i, \tau^j] = i\varepsilon_{ijk}\tau^k$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]). The linear bijection $J_{\pm i} \mapsto \tau^i$ matches the brackets of Step 4 on a basis, hence everywhere: $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, which is $\mathfrak{su}(2)_{\mathbb C}$ by Theorem §CB.2.4.
>
> **Step 6** (part 3: the conjugation). $J_i, K_i \in i\,\mathfrak{so}(1,3)$, so $c(J_i) = -J_i$, $c(K_i) = -K_i$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-5|Theorem §CB.2.5]], 2). $c$ is conjugate-linear, so
>
> $$
> c(J_{\pm i}) = \tfrac12\bigl(c(J_i) \mp i\,c(K_i)\bigr) = \tfrac12\bigl(-J_i \pm iK_i\bigr) = -J_{\mp i},
> $$
>
> and $c$ maps the complex span $\mathfrak a_\pm$ onto $\mathfrak a_\mp$.
>
> **Step 7** (part 3: the real algebra). For $A \in \mathfrak a_+$, $c(A + cA) = cA + A$ ($c^2 = \mathbb 1$), so $A + cA \in \mathfrak{so}(1,3)$, the fixed set of $c$. The real-linear map $A \mapsto A + cA$ is injective: $A + cA = 0$ gives $A = -cA \in \mathfrak a_+ \cap \mathfrak a_- = \{0\}$. Both spaces have real dimension $6$, so it is onto: $\mathfrak{so}(1,3) = \{A + c(A) : A \in \mathfrak a_+\}$.
>
> **Step 8** (the rest of part 1). If $A \in \mathfrak a_+$ lies in $\mathfrak{so}(1,3)$, then $A = cA \in \mathfrak a_-$, so $A = 0$; if it lies in $i\,\mathfrak{so}(1,3)$, then $A = -cA \in \mathfrak a_-$, so again $A = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: the split exists only after complexifying; neither copy contains a nonzero real Lorentz generator (Step 8). Each real generator is a pair $A + c(A)$, one component in each copy, tied together by conjugation: the "complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$, complex conjugates of each other" of the user's notes, Ch. 7 §7.4.
> - The brackets were computed in the vector representation, but by [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]] they hold in every representation; that is [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]].

^pf-cb-2-12

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-5|Theorem §CB.2.5]]

The representation-level statement, a pair of commuting angular momenta on a complex space, proved in [[§C3.2 The Lorentz Algebra|§C3.2]]:

![[§C3.2 The Lorentz Algebra#^thm-c3-2-3]]

> [!theorem] Theorem §CB.2.13: The Euclidean 𝔰𝔬(4) Splits Already over ℝ
> In $\mathfrak{so}(4)$ (real antisymmetric $4\times4$ matrices, coordinates $x^0, \dots, x^3$) let $J_i$ be the physicists' generators of rotations of $x^1, x^2, x^3$ and $\tilde K_i$ those of rotations in the $(x^0, x^i)$ planes, with signs chosen so that
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k .
> $$
>
> Then $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$, with **no** $i$, obey $[A_{\pm i}, A_{\pm j}] = i\varepsilon_{ijk}A_{\pm k}$ and $[A_{+i}, A_{-j}] = 0$, and $-iA_{\pm i} \in \mathfrak{so}(4)$. So $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$ with real ideals $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\} \cong \mathfrak{su}(2)$; and $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C} \oplus (\mathfrak b_-)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, with the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ mapping each summand to itself.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 · Woit, §21.2 (the split $M = \frac12(L + K)$, $N = \frac12(L - K)$ of $\mathfrak{so}(4)$) · [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]] (the same split for the Coulomb problem) · the explicit generators written here*

^thm-cb-2-13

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §21.2 "so(4) symmetry and the Coulomb potential": from $[L_j, L_k] = i\epsilon_{jkl}L_l$, $[L_j, K_k] = i\epsilon_{jkl}K_l$, $[K_j, K_k] = i\epsilon_{jkl}L_l$ "one has" the two commuting copies $M$, $N$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the user's PHY 513 notes, Ch. 7 §7.4.6 ("That happens for $\mathfrak{so}(4)$, the Euclidean case, where the two copies are real"). The explicit choice of $J_i$, $\tilde K_i$ that realizes the hypothesis (Steps 1–3) is written here.*
>
> **Step 1** (a basis of $\mathfrak{so}(4)$). For $0 \le a, b \le 3$ let $E_{ab} = e_ae_b^{\mathsf T} - e_be_a^{\mathsf T}$, real antisymmetric; $\{E_{ab}\}_{a<b}$ is a basis of $\mathfrak{so}(4)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). Multiplying out with $e_b^{\mathsf T}e_c = \delta_{bc}$ (all four products in each of $E_{ab}E_{cd}$ and $E_{cd}E_{ab}$) gives
>
> $$
> [E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{ac}E_{bd} - \delta_{bd}E_{ac} + \delta_{ad}E_{bc} .
> $$
>
> **Step 2** (the generators). Put $J_1 = -iE_{23}$, $J_2 = -iE_{31}$, $J_3 = -iE_{12}$ (i.e. $J_i = -\frac i2\varepsilon_{ijk}E_{jk}$; then $-iJ_3 = -E_{12}$ is the generator $M^{12}$ of the active rotation of $(x^1, x^2)$, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], so on $x^1, x^2, x^3$ these are the rotation generators $(J^k)_{lm} = -i\varepsilon^{klm}$ of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]) and $\tilde K_i = -iE_{0i}$. Then by Step 1:
> - $[J_1, J_2] = (-i)^2[E_{23}, E_{31}] = -E_{21} = E_{12} = iJ_3$;
> - $[\tilde K_1, \tilde K_2] = (-i)^2[E_{01}, E_{02}] = -(-E_{12}) = E_{12} = iJ_3$;
> - $[J_1, \tilde K_2] = -[E_{23}, E_{02}] = -(-E_{03}) = E_{03} = i\tilde K_3$; $[J_2, \tilde K_1] = -[E_{31}, E_{01}] = -E_{03} = -i\tilde K_3$; $[J_1, \tilde K_1] = -[E_{23}, E_{01}] = 0$.
>
> **Step 3** (all index pairs). The cyclic relabelling $\pi$: $0 \mapsto 0$, $1 \mapsto 2$, $2 \mapsto 3$, $3 \mapsto 1$ is realized by the orthogonal permutation matrix $Pe_a = e_{\pi(a)}$, and $PE_{ab}P^{-1} = Pe_ae_b^{\mathsf T}P^{\mathsf T} - \cdots = E_{\pi(a)\pi(b)}$. So $X \mapsto PXP^{-1}$ (a Lie algebra automorphism, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], 4) sends $J_1 \mapsto J_2 \mapsto J_3 \mapsto J_1$ and $\tilde K_1 \mapsto \tilde K_2 \mapsto \tilde K_3 \mapsto \tilde K_1$, while $\varepsilon_{ijk}$ is invariant under cyclic relabelling. Applying it once and twice to the identities of Step 2, and using antisymmetry of the bracket for $[J_j, J_i]$, $[\tilde K_j, \tilde K_i]$, gives for all $i, j$
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, \tilde K_j] = i\varepsilon_{ijk}\tilde K_k, \qquad [\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k ,
> $$
>
> the hypothesis of the theorem. The sign of the last bracket differs from the Lorentz case ($-i\varepsilon_{ijk}J_k$, [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]) because $(E_{0i})^2$ is negative on its plane, $(M^{0i})^2$ positive ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **Step 4** (the split with no $i$; Woit). With $A_{\pm i} = \frac12(J_i \pm \tilde K_i)$ and $[\tilde K_i, J_j] = -[J_j, \tilde K_i] = i\varepsilon_{ijk}\tilde K_k$:
>
> $$
> [A_{\pm i}, A_{\pm j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k \pm i\varepsilon_{ijk}\tilde K_k \pm i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}J_k\bigr) = i\varepsilon_{ijk}A_{\pm k},
> $$
>
> $$
> [A_{+i}, A_{-j}] = \tfrac14\bigl(i\varepsilon_{ijk}J_k - i\varepsilon_{ijk}\tilde K_k + i\varepsilon_{ijk}\tilde K_k - i\varepsilon_{ijk}J_k\bigr) = 0 .
> $$
>
> **Step 5** (real ideals). $-iA_{\pm i} = \frac12(-iJ_i \mp i\tilde K_i) = \frac12\bigl(-\tfrac12\varepsilon_{ijk}E_{jk} \mp E_{0i}\bigr)$ is a real antisymmetric matrix, so $-iA_{\pm i} \in \mathfrak{so}(4)$. By Step 4, $[-iA_{\pm i}, -iA_{\pm j}] = -[A_{\pm i}, A_{\pm j}] = \varepsilon_{ijk}(-iA_{\pm k})$ and $[-iA_{+i}, -iA_{-j}] = 0$: $\mathfrak b_\pm = \operatorname{span}_{\mathbb R}\{-iA_{\pm i}\}$ are commuting subalgebras with the structure constants $\varepsilon_{ijk}$ of $\mathfrak{su}(2)$ in the basis $-i\tau^k$ (Theorem §C3.1.1), so $\mathfrak b_\pm \cong \mathfrak{su}(2)$. Since $J_i = A_{+i} + A_{-i}$ and $\tilde K_i = A_{+i} - A_{-i}$, the six $-iA_{\pm i}$ span the six $-iJ_i$, $-i\tilde K_i$, i.e. all of $\mathfrak{so}(4)$; six vectors spanning a six-dimensional space are a basis, so $\mathfrak{so}(4) = \mathfrak b_+ \oplus \mathfrak b_-$, and each $\mathfrak b_\pm$ is an ideal ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]]).
>
> **Step 6** (complexification and conjugation). Complex combinations of the basis of Step 5 give $\mathfrak{so}(4)_{\mathbb C} = (\mathfrak b_+)_{\mathbb C}\oplus(\mathfrak b_-)_{\mathbb C}$, and $(\mathfrak b_\pm)_{\mathbb C} \cong \mathfrak{su}(2)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]). The conjugation fixes $\mathfrak b_\pm \subset \mathfrak{so}(4)$ and, being conjugate-linear, maps $(\mathfrak b_\pm)_{\mathbb C} = \mathfrak b_\pm + i\mathfrak b_\pm$ to itself.
>
> **What the proof shows.**
> - ⚑ By-product: one sign, $[\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k$ versus $-i\varepsilon_{ijk}J_k$ for boosts, decides whether the split is real (here) or needs complexification (Theorem §CB.2.12).
> - The real split is why $SU(2)\times SU(2)$ covers $SO(4)$ and why the hydrogen spectrum is organized by two angular momenta ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]; Woit §21.2).

^pf-cb-2-13

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]

> [!theorem] Theorem §CB.2.14: 𝔰𝔬(1,3) and 𝔰𝔬(4) Are Two Real Forms of One Complex Algebra
> 1. $J_{\pm i} \mapsto A_{\pm i}$ extends to an isomorphism of complex Lie algebras $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]]); under it $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]) of the same complex algebra.
> 2. Their conjugations differ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]]): that of $\mathfrak{so}(4)$ maps each $\mathfrak{sl}(2, \mathbb C)$ summand to itself, that of $\mathfrak{so}(1,3)$ exchanges the two.
> 3. $\mathfrak{so}(1,3)$ is simple as a real Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]]). In particular $\mathfrak{so}(1,3) \not\cong \mathfrak{su}(2)\oplus\mathfrak{su}(2) \cong \mathfrak{so}(4)$: the real Lorentz algebra is **not** two copies of the rotation algebra; only its complexification is two copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §§7.4.1, 7.4.6 ("The accurate statement is that the algebra … decomposes") · Woit, §§21.2, 40.2 · Etingof, Lie Groups and Lie Algebras, §9.4, Remark 17.3 · written here (the proof)*

^thm-cb-2-14

> [!proof]- Proof
> *Written here, along the route recorded in batch 1 (an ideal of $\mathfrak{so}(1,3)$ complexifies to a $c$-stable ideal of $\mathfrak a_+\oplus\mathfrak a_-$). Context: P. Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (real forms as fixed sets of antilinear involutions) and Remark 17.3 ("if $\mathfrak g$ is a simple complex Lie algebra regarded as a real Lie algebra then $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ is semisimple but not simple") (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §40.2 and §21.2 for the two splits. No source found with this proof for $\mathfrak{so}(1,3)$ itself.*
>
> **Step 1** (part 1). $\{J_{\pm i}\}$ and $\{A_{\pm i}\}$ are complex bases of $\mathfrak{so}(1,3)_{\mathbb C}$ and $\mathfrak{so}(4)_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], 1; Step 5 of the proof of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]]) with identical brackets: $[X_{\pm i}, X_{\pm j}] = i\varepsilon_{ijk}X_{\pm k}$, $[X_{+i}, X_{-j}] = 0$ for $X = J$ and for $X = A$. So the complex-linear bijection $\alpha : J_{\pm i} \mapsto A_{\pm i}$ preserves brackets on a basis, hence everywhere. Each of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$ is a real form of its own complexification (the fixed set of $c$, [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]), and $\alpha^{-1}(\mathfrak{so}(4))$ is a real form of $\mathfrak{so}(1,3)_{\mathbb C}$ isomorphic to $\mathfrak{so}(4)$; with Theorem §CB.2.12, 2, both are real forms of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (part 2). Transported by $\alpha$, the conjugation of $\mathfrak{so}(4)_{\mathbb C}$ becomes $\sigma' = \alpha^{-1}c_{(4)}\alpha$, which maps each $\mathfrak a_\pm = \alpha^{-1}((\mathfrak b_\pm)_{\mathbb C})$ to itself (Theorem §CB.2.13, Step 6 of its proof), while the conjugation $c$ of $\mathfrak{so}(1,3)_{\mathbb C}$ exchanges $\mathfrak a_+$ and $\mathfrak a_-$ (Theorem §CB.2.12, 3). The two conjugations differ, as they must for non-isomorphic real forms ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]]); that the real forms are indeed non-isomorphic is Step 6.
>
> **Step 3** ($\mathfrak{sl}(2, \mathbb C)$ is simple). Basis $H = \operatorname{diag}(1, -1)$, $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$; multiplying out, $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. Let $I \ne 0$ be an ideal and $X = aE + bH + cF \in I$, $X \ne 0$. Then $[E, X] = b[E, H] + c[E, F] = -2bE + cH \in I$ and $[E, [E, X]] = c[E, H] = -2cE \in I$. If $c \ne 0$, $E \in I$. If $c = 0$, $b \ne 0$: $[E, X] = -2bE$, so $E \in I$. If $b = c = 0$: $X = aE$, $a \ne 0$, so $E \in I$. In every case $E \in I$, then $H = [E, F] \in I$ and $F = -\frac12[H, F] \in I$: $I = \mathfrak{sl}(2, \mathbb C)$. It is not abelian, so it is simple ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]]).
>
> **Step 4** (the ideals of $\mathfrak a_+\oplus\mathfrak a_-$). Let $I$ be an ideal of $\mathfrak a_+\oplus\mathfrak a_-$ (each $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$, simple by Step 3, hence with trivial centre, since the centre is an ideal $\ne \mathfrak a_\pm$). If some $(x_+, x_-) \in I$ has $x_+ \ne 0$, pick $y \in \mathfrak a_+$ with $[y, x_+] \ne 0$; then $[(y, 0), (x_+, x_-)] = ([y, x_+], 0) \in I \cap \mathfrak a_+$, a nonzero ideal of $\mathfrak a_+$ (brackets with $\mathfrak a_-$ vanish), so $\mathfrak a_+ \subset I$. Likewise for the minus component. Hence $I \in \{0, \mathfrak a_+, \mathfrak a_-, \mathfrak a_+\oplus\mathfrak a_-\}$.
>
> **Step 5** (part 3: $\mathfrak{so}(1,3)$ is simple). Let $\mathfrak i$ be an ideal of $\mathfrak{so}(1,3)$ and $\mathfrak i_{\mathbb C} = \mathfrak i + i\mathfrak i \subset \mathfrak{so}(1,3)_{\mathbb C}$. It is a complex ideal: for $X, Y \in \mathfrak{so}(1,3)$, $A, B \in \mathfrak i$, $[X + iY, A + iB] = ([X, A] - [Y, B]) + i([X, B] + [Y, A]) \in \mathfrak i + i\mathfrak i$. It is $c$-stable: $c(A + iB) = A - iB$. By Step 4 it is $0$, $\mathfrak a_+$, $\mathfrak a_-$ or everything, and $c(\mathfrak a_\pm) = \mathfrak a_\mp \ne \mathfrak a_\pm$ excludes the middle two. Since $\mathfrak i = \mathfrak i_{\mathbb C} \cap \mathfrak{so}(1,3)$ (the $c$-fixed part of $A + iB$ is $A$), $\mathfrak i = 0$ or $\mathfrak i = \mathfrak{so}(1,3)$. And $\mathfrak{so}(1,3)$ is not abelian ($[-iJ_1, -iJ_2] = -iJ_3 \ne 0$). So it is simple.
>
> **Step 6** (not two rotation algebras). $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ has the ideal $\mathfrak{su}(2)\oplus0$, neither $0$ nor everything, so it is not simple, and by Step 5 it is not isomorphic to $\mathfrak{so}(1,3)$. By Theorem §CB.2.13 it is isomorphic to $\mathfrak{so}(4)$.
>
> **What the proof shows.**
> - ⚑ By-product: "the Lorentz algebra is two copies of the rotation algebra" is true only after complexification; the real algebra is simple, and the two copies are glued by the conjugation → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4|§C3.3, Remark: What the split does and does not mean]].
> - Simplicity of $\mathfrak{so}(1,3)$ is the hypothesis of Theorem §CB.3.16 (no finite-dimensional unitary representations).

^pf-cb-2-14

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]]

The course's remark on what the split does and does not mean, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]] (see also [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]):

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4]]

> [!theorem] Theorem §CB.2.15: Two Real Forms of 𝔰𝔩(2,ℂ)
> $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb R)$ are real forms of $\mathfrak{sl}(2, \mathbb C)$, with conjugations $X \mapsto -X^\dagger$ and $X \mapsto \bar X$. They are not isomorphic: $\mathfrak{su}(2)$ has no element $X \ne 0$ for which $\mathrm{ad}_X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-19|Def. §CB.1.19]]) has a nonzero real eigenvalue, while $H = \operatorname{diag}(1, -1) \in \mathfrak{sl}(2, \mathbb R)$ has $\mathrm{ad}_H$-eigenvalues $0, \pm2$. Moreover $\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$ and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §9.4 (the same argument for $\mathfrak u(n) \not\cong \mathfrak{gl}(n, \mathbb R)$, via $\mathrm{ad}$) · Hall, An Elementary Introduction to Groups and Representations, Ch. 3 §9 (real forms, Exercise 11) · written here (the details)*

^thm-cb-2-15

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §9.4: "$\mathfrak u(n) \not\cong \mathfrak{gl}_n(\mathbb R)$, since in the first algebra any element $x$ with nilpotent $\mathrm{ad}\,x$ must be zero, while in the second one it does not have to" (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); Steps 2–3 run this argument with real eigenvalues of $\mathrm{ad}$ in place of nilpotency. The conjugations and the isomorphism with $\mathfrak{so}(1,2)$ are written here.*
>
> **Step 1** (the two conjugations). On $\mathfrak{sl}(2, \mathbb C)$ put $\sigma_1(X) = -X^\dagger$ and $\sigma_2(X) = \bar X$. Both map traceless matrices to traceless ones ($\operatorname{tr}X^\dagger = \operatorname{tr}\bar X = \overline{\operatorname{tr}X}$), are conjugate-linear and square to $\mathbb 1$. Brackets: $[\sigma_1X, \sigma_1Y] = X^\dagger Y^\dagger - Y^\dagger X^\dagger = (YX - XY)^\dagger = -[X, Y]^\dagger = \sigma_1[X, Y]$, and $\overline{XY - YX} = \bar X\bar Y - \bar Y\bar X$. Fixed sets: $-X^\dagger = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{su}(2)$; $\bar X = X$ with $\operatorname{tr}X = 0$ is $\mathfrak{sl}(2, \mathbb R)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). By [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]] both are real forms of $\mathfrak{sl}(2, \mathbb C)$.
>
> **Step 2** (in $\mathfrak{su}(2)$, $\mathrm{ad}$ has no nonzero real eigenvalue). On $\mathfrak{su}(2)$ let $B(X, Y) = -\operatorname{tr}(XY)$. It is real: $\overline{\operatorname{tr}(XY)} = \operatorname{tr}((XY)^\dagger) = \operatorname{tr}(Y^\dagger X^\dagger) = \operatorname{tr}(YX) = \operatorname{tr}(XY)$ for anti-Hermitian $X$, $Y$. It is positive definite: $B(X, X) = -\operatorname{tr}(X^2) = \operatorname{tr}(X^\dagger X) = \sum_{ij}|X_{ij}|^2$. It is invariant: $B([Z, X], Y) + B(X, [Z, Y]) = -\operatorname{tr}(ZXY - XZY + XZY - XYZ) = -\operatorname{tr}(ZXY) + \operatorname{tr}(XYZ) = 0$ by cyclicity of the trace. So for $Z \in \mathfrak{su}(2)$, if $\mathrm{ad}_ZX = \lambda X$ with $\lambda \in \mathbb R$, $X \ne 0$ in $\mathfrak{su}(2)$:
>
> $$
> \lambda B(X, X) = B([Z, X], X) = -B(X, [Z, X]) = -\lambda B(X, X) \quad\Longrightarrow\quad \lambda = 0 .
> $$
>
> **Step 3** (in $\mathfrak{sl}(2, \mathbb R)$ it has). With $E$, $F$ as in Step 3 of the proof of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]] (real matrices), $\mathrm{ad}_HE = 2E$, $\mathrm{ad}_HF = -2F$, $\mathrm{ad}_HH = 0$: eigenvalues $0, \pm2$. A Lie algebra isomorphism $f : \mathfrak{sl}(2, \mathbb R) \to \mathfrak{su}(2)$ would satisfy $\mathrm{ad}_{f(H)}f(E) = f([H, E]) = 2f(E)$ with $f(E) \ne 0$, contradicting Step 2. So $\mathfrak{su}(2) \not\cong \mathfrak{sl}(2, \mathbb R)$.
>
> **Step 4** ($\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$). In $\mathfrak{so}(1,2)$, $\eta = \operatorname{diag}(1, -1, -1)$, the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] (same formula, three dimensions) are $M^{01} = e_0e_1^{\mathsf T} + e_1e_0^{\mathsf T}$, $M^{02} = e_0e_2^{\mathsf T} + e_2e_0^{\mathsf T}$, $M^{12} = e_2e_1^{\mathsf T} - e_1e_2^{\mathsf T}$, and multiplying out (with $e_a^{\mathsf T}e_b = \delta_{ab}$)
>
> $$
> [M^{01}, M^{02}] = -M^{12}, \qquad [M^{12}, M^{01}] = M^{02}, \qquad [M^{12}, M^{02}] = -M^{01} .
> $$
>
> In $\mathfrak{sl}(2, \mathbb R)$ put $B_1 = \frac12H$, $B_2 = \frac12(E + F)$, $R = \frac12(F - E)$. With $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$: $[B_1, B_2] = \frac14(2E - 2F) = -R$; $[R, B_1] = \frac14([F, H] - [E, H]) = \frac14(2F + 2E) = B_2$; $[R, B_2] = \frac14([F, E] - [E, F]) = -\frac12H = -B_1$. The linear bijection $B_1 \mapsto M^{01}$, $B_2 \mapsto M^{02}$, $R \mapsto M^{12}$ matches all brackets on a basis: an isomorphism.
>
> **Step 5** ($\mathfrak{su}(2) \cong \mathfrak{so}(3)$). This is [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]].
>
> **What the proof shows.**
> - Compactness is visible in the algebra: an invariant positive-definite form (Step 2) forbids real $\mathrm{ad}$-eigenvalues; a "boost" ($H$, or $M^{01}$) has them. The same test shows $\mathfrak{so}(1,3)$ has no invariant inner product → Theorem §CB.3.16.
> - ⚑ By-product: one complex algebra $\mathfrak{sl}(2, \mathbb C)$, two real forms: rotations of $\mathbb R^3$ and Lorentz transformations of $\mathbb R^{1,2}$.

^pf-cb-2-15

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]] (Step 3 of its proof), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]]

## 𝔰𝔩(2,ℂ) as a real Lie algebra

> [!definition] Definition §CB.2.16: Underlying Real Lie Algebra
> The **underlying real Lie algebra** (realification) $\mathfrak h_{\mathbb R}$ of a complex Lie algebra $\mathfrak h$ is $\mathfrak h$ with scalars restricted to $\mathbb R$; $\dim_{\mathbb R}\mathfrak h_{\mathbb R} = 2\dim_{\mathbb C}\mathfrak h$. The Lie algebra of the matrix Lie group $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]) is $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]).
>
> *Source: written here*

^def-cb-2-16

> [!theorem] Theorem §CB.2.17: The Real Lie Algebra of SL(2,ℂ) Is the Lorentz Algebra
> The differential ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]); in the conventions of Theorem §C5a.4.7 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$.
>
> *Source: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], 3, differentiated · Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · conventions checked against [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]] (batch 2)*

^thm-cb-2-17

> [!proof]- Proof
> *Source: the vault's [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], part 3 (from the user's PHY 513 notes, Ch. 8 §8.2, and Yu, Exercise 3.7), differentiated with [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]. Convention check (batch 2): Larsen's register, $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$ with $-iJ_i = M^{jk}$ ($ijk$ cyclic) and $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]); the statement's two assignments are confirmed in Steps 2–3, so the statement stands unchanged.*
>
> **Step 1** (a real basis). $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ consists of the traceless complex $2\times2$ matrices ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]); $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them, so the six matrices $-\frac i2\sigma^k$, $-\frac12\sigma^k$ are a real basis. Likewise $-iJ_k$, $-iK_k$ are a real basis of $\mathfrak{so}(1,3)$.
>
> **Step 2** (rotations). By Theorem §C5a.4.7, 3, $\pi(U) = \operatorname{diag}(1, R(U))$ for $U \in SU(2)$, and $R(e^{-is\sigma^k/2})$ is the rotation by $s$ about $x^k$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 2), which in the vector representation is $e^{-isJ_k} = e^{sM^{ij}}$ ($ijk$ cyclic; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 3). By the formula of Theorem §CB.1.14,
>
> $$
> \pi_\ast\bigl(-\tfrac i2\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-is\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isJ_k}\Big|_{s=0} = -iJ_k .
> $$
>
> **Step 3** (boosts). By Theorem §C5a.4.7, 3, $\pi(e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2})$ is the pure boost $e^\omega$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$; for $\boldsymbol\eta = s\,\mathbf e_k$ this is $e^{sM^{0k}} = e^{-isK_k}$ (Def. §C1a.6.2: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\boldsymbol\eta\cdot\mathbf K$). Hence
>
> $$
> \pi_\ast\bigl(-\tfrac12\sigma^k\bigr) = \frac{d}{ds}\pi\bigl(e^{-s\sigma^k/2}\bigr)\Big|_{s=0} = \frac{d}{ds}e^{-isK_k}\Big|_{s=0} = -iK_k .
> $$
>
> **Step 4** (isomorphism). $\pi_\ast$ is real-linear and preserves brackets (Theorem §CB.1.14) and maps the real basis of Step 1 onto the real basis of Step 1: it is bijective, hence an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]).
>
> **Step 5** (a check on brackets). $[-\frac i2\sigma^1, -\frac i2\sigma^2] = -\frac14[\sigma^1, \sigma^2] = -\frac14\cdot2i\sigma^3 = -\frac i2\sigma^3$, matching $[-iJ_1, -iJ_2] = -[J_1, J_2] = -iJ_3$; and $[-\frac12\sigma^1, -\frac12\sigma^2] = \frac14\cdot2i\sigma^3 = -(-\frac i2\sigma^3)$, matching $[-iK_1, -iK_2] = -[K_1, K_2] = iJ_3 = -(-iJ_3)$ ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]).
>
> **What the proof shows.**
> - ⚑ By-product: in $\mathfrak{sl}(2, \mathbb C)$ a boost generator is a complex multiple of a rotation generator, $-\frac12\sigma^k = -i\bigl(-\frac i2\sigma^k\bigr)$. So multiplication by $i$ on $\mathfrak{sl}(2, \mathbb C)$ becomes, on $\mathfrak{so}(1,3)$, the real-linear map $-iJ_k \mapsto iK_k$, $-iK_k \mapsto -iJ_k$ (it squares to $-\mathbb 1$) — a complex structure on $\mathfrak{so}(1,3)$ that is invisible from its definition → Theorem §CB.2.18.
> - The opposite sign convention for $\mathbf K$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]], after Def. §C1a.6.2: some sources use $K^i = \mathcal J^{i0}$) would flip the second assignment.

^pf-cb-2-17

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]

> [!theorem] Theorem §CB.2.18: The Complexification of Real 𝔰𝔩(2,ℂ) Is Two Copies of 𝔰𝔩(2,ℂ)
> The map $\Phi : (\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} \to \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$,
>
> $$
> \Phi(X + iY) = \bigl(X + iY,\ \bar X + i\bar Y\bigr) \qquad (X, Y \in \mathfrak{sl}(2, \mathbb C)_{\mathbb R};\ \bar X \text{ the entrywise conjugate}),
> $$
>
> is an isomorphism of complex Lie algebras. So the complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$; on the real algebra, $X \mapsto (X, \bar X)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 and Remark 17.3 ($\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$ for a complex $\mathfrak g$ regarded as real) · Woit, §5.5 ($\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ is "built out of two copies") · the explicit map written here*

^thm-cb-2-18

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4 ("Let $\mathfrak g$ be a complex Lie algebra. Show that $\mathfrak g_{\mathbb C} \cong \mathfrak g\oplus\mathfrak g$") and Remark 17.3 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); P. Woit, §5.5, on $\mathfrak{gl}(n, \mathbb C)_{\mathbb C}$ (https://www.math.columbia.edu/~woit/QM/qmbook.pdf). Etingof's statement is an exercise; the solution with the explicit map of the theorem (the second copy written with the conjugate matrix) is written here.*
>
> **Step 1** (what the symbols mean). An element of $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ is a formal $X + iY$ with $X, Y$ traceless complex matrices ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]]); the $i$ here is the new one, not the matrix scalar. In each component of $\Phi(X + iY)$, "$X + iY$" and "$\bar X + i\bar Y$" are computed with matrix operations, and both are traceless.
>
> **Step 2** (complex-linear). $\Phi$ is real-linear, and with $i(X + iY) = -Y + iX$:
>
> $$
> \Phi(-Y + iX) = \bigl(-Y + iX,\ -\bar Y + i\bar X\bigr) = i\bigl(X + iY,\ \bar X + i\bar Y\bigr) .
> $$
>
> **Step 3** (brackets). On the real algebra, $\Phi(X) = (X, \bar X)$ preserves brackets: $[X, X'] \mapsto ([X, X'], \overline{[X, X']}) = ([X, X'], [\bar X, \bar X'])$, entrywise conjugation being multiplicative. $\Phi$ is the complex-linear extension of this real Lie algebra homomorphism into the complex Lie algebra $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$, and such an extension preserves brackets by the four-term expansion of Step 2 of the proof of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]] (with $d$ replaced by $X \mapsto (X, \bar X)$).
>
> **Step 4** (injective). If $\Phi(X + iY) = 0$, then $X + iY = 0$ and $\bar X + i\bar Y = 0$ as matrices. Conjugating the second entrywise, $X - iY = 0$. Adding and subtracting: $X = 0$, $Y = 0$.
>
> **Step 5** (bijective). $\dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} = \dim_{\mathbb R}\mathfrak{sl}(2, \mathbb C)_{\mathbb R} = 6$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]; [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]) $= \dim_{\mathbb C}(\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C))$, so the injective linear $\Phi$ is bijective: an isomorphism of complex Lie algebras. In particular the complexification has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$ (dimension $3$).
>
> **What the proof shows.**
> - ⚑ By-product: "complexify by allowing complex coefficients" fails for an algebra already closed under $i$; the abstract $i$ and the matrix $i$ are different, and the second copy carries the conjugate matrices. This is the algebraic origin of the conjugate representation $\Lambda \mapsto \bar\Lambda$ of $SL(2, \mathbb C)$ (Theorem §CB.2.19).
> - Composed with Theorem §CB.2.17, this gives $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ once more, consistently with Theorem §CB.2.12.

^pf-cb-2-18

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]

> [!theorem] Theorem §CB.2.19: Representations of Real 𝔰𝔩(2,ℂ): a Complex-Linear and an Antilinear Part
> Let $\rho : \mathfrak{sl}(2, \mathbb C)_{\mathbb R} \to \operatorname{End}_{\mathbb C}(W)$ be a representation on a complex vector space $W$. There are unique maps $\rho_1$, $\rho_2$ with $\rho = \rho_1 + \rho_2$, $\rho_1$ complex-linear and $\rho_2$ complex-antilinear ($\rho_2(iX) = -i\rho_2(X)$), both Lie algebra homomorphisms, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$. Conversely every such commuting pair gives a representation. The defining representation $X \mapsto X$ on $\mathbb C^2$ has $\rho_2 = 0$; its complex conjugate $X \mapsto \bar X$ has $\rho_1 = 0$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), Exercise 11.4 ("$\mathrm{Rep}_{\mathbb R}G \cong \mathrm{Rep}(\mathfrak g\oplus\mathfrak g)$" for a complex $G$ regarded as real) · written here (from Theorem §CB.2.18 and Theorem §CB.2.6)*

^thm-cb-2-19

> [!proof]- Proof
> *Written here from Theorems §CB.2.6 and §CB.2.18; it is the Lie-algebra half of P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Exercise 11.4, second sentence (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), which is stated there without proof.*
>
> **Step 1** (pass to two copies). Extend $\rho$ complex-linearly to $\rho_{\mathbb C}$ on $(\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]) and set $\sigma = \rho_{\mathbb C}\circ\Phi^{-1}$ with $\Phi$ of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]]: a complex-linear representation of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ on $W$. Put $\sigma_1(A) = \sigma(A, 0)$, $\sigma_2(B) = \sigma(0, B)$. Both are complex-linear representations of $\mathfrak{sl}(2, \mathbb C)$, and they commute: $[\sigma_1(A), \sigma_2(B)] = \sigma([(A, 0), (0, B)]) = \sigma(0) = 0$.
>
> **Step 2** (existence). For $X$ in the real algebra, $\Phi(X) = (X, \bar X) = (X, 0) + (0, \bar X)$, so $\rho(X) = \rho_{\mathbb C}(X) = \sigma_1(X) + \sigma_2(\bar X)$. Put $\rho_1(X) = \sigma_1(X)$ and $\rho_2(X) = \sigma_2(\bar X)$. Then $\rho_1$ is complex-linear; $\rho_2(iX) = \sigma_2(\overline{iX}) = \sigma_2(-i\bar X) = -i\rho_2(X)$ is antilinear; both preserve brackets (for $\rho_2$ because $\overline{[X, Y]} = [\bar X, \bar Y]$); and they commute by Step 1.
>
> **Step 3** (uniqueness). If $\rho = \rho_1 + \rho_2$ with $\rho_1$ complex-linear and $\rho_2$ antilinear, then $\rho(iX) = i\rho_1(X) - i\rho_2(X)$, so $-i\rho(iX) = \rho_1(X) - \rho_2(X)$ and
>
> $$
> \rho_1(X) = \tfrac12\bigl(\rho(X) - i\rho(iX)\bigr), \qquad \rho_2(X) = \tfrac12\bigl(\rho(X) + i\rho(iX)\bigr):
> $$
>
> both are determined by $\rho$.
>
> **Step 4** (converse). If $\rho_1$, $\rho_2$ are bracket-preserving, complex-linear resp. antilinear, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$, then $\rho = \rho_1 + \rho_2$ is real-linear and, expanding all four terms and dropping the two mixed ones,
>
> $$
> [\rho(X), \rho(Y)] = [\rho_1X, \rho_1Y] + [\rho_1X, \rho_2Y] + [\rho_2X, \rho_1Y] + [\rho_2X, \rho_2Y] = \rho_1[X, Y] + \rho_2[X, Y] = \rho([X, Y]) .
> $$
>
> **Step 5** (the two examples). For $\rho(X) = X$: $\rho(iX) = iX$, so Step 3 gives $\rho_2(X) = \frac12(X + i\cdot iX) = 0$. For $\rho(X) = \bar X$: $\rho(iX) = -i\bar X$, so $\rho_1(X) = \frac12(\bar X - i(-i\bar X)) = \frac12(\bar X - \bar X) = 0$.
>
> **What the proof shows.**
> - ⚑ By-product: a representation of $SL(2, \mathbb C)$ regarded as a real group is labelled by two complex-linear pieces, one "holomorphic", one "antiholomorphic"; through Theorem §CB.2.17 these become the two commuting angular momenta behind the labels $(j_+, j_-)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; which of the defining representation and its conjugate is called $(\frac12, 0)$ is a convention fixed there).
> - The decomposition needs $W$ complex; antilinearity of $\rho_2$ is relative to the complex structure of $\mathfrak{sl}(2, \mathbb C)$, not of $W$.

^pf-cb-2-19

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]]

> [!theorem] Theorem §CB.2.20: Real Forms Have the Same Representations
> If $\mathfrak g_1$ and $\mathfrak g_2$ are real forms of the same complex Lie algebra $\mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]), then restriction and complex-linear extension ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]) give bijections between the representations of $\mathfrak g_1$ on complex spaces, the complex-linear representations of $\mathfrak h$, and the representations of $\mathfrak g_2$ on complex spaces, preserving invariant subspaces, irreducibility, direct sums and intertwiners. Example: the finite-dimensional complex representations of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ correspond to one another (Theorems §CB.2.14, §CB.2.17).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §1, Prop. 5.5 (each correspondence) · Woit, §5.5 · written here (the composition)*

^thm-cb-2-20

> [!proof]- Proof
> *Written here as a composition of two instances of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]] (B. C. Hall, An Elementary Introduction to Groups and Representations, Prop. 5.5, https://arxiv.org/abs/math-ph/0005032; P. Woit, §5.5, whose example is exactly this use: representations of $\mathfrak{su}(2)$ through $\mathfrak{sl}(2, \mathbb C)$).*
>
> **Step 1** (from $\mathfrak g_1$ to $\mathfrak h$). $\mathfrak g_1$ is a real form of $\mathfrak h$, so $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_1)_{\mathbb C} \cong \mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]). Composing with it, Theorem §CB.2.6 says: a representation $d$ of $\mathfrak g_1$ on a complex space $W$ extends uniquely to the complex-linear representation $\tilde d(X + iY) = d(X) + i\,d(Y)$ of $\mathfrak h$ ($X, Y \in \mathfrak g_1$), and every complex-linear representation of $\mathfrak h$ arises so, by restriction to $\mathfrak g_1 \subset \mathfrak h$.
>
> **Step 2** (from $\mathfrak h$ to $\mathfrak g_2$). The same for $\mathfrak g_2$: restriction of complex-linear representations of $\mathfrak h$ to $\mathfrak g_2$ is a bijection onto the representations of $\mathfrak g_2$ on complex spaces, with inverse the complex-linear extension.
>
> **Step 3** (composition). $d \mapsto \tilde d|_{\mathfrak g_2}$ is a bijection from representations of $\mathfrak g_1$ to representations of $\mathfrak g_2$ on the same space $W$, inverse to the analogous map in the other direction. Invariant subspaces, irreducibility, direct sums and intertwiners are preserved at each of the two steps (Theorem §CB.2.6, 2), hence by the composition.
>
> **Step 4** (the example). $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms of one complex algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], 1). A Lie algebra isomorphism $f : \mathfrak g \to \mathfrak g'$ turns representations of $\mathfrak g'$ into those of $\mathfrak g$ by $d' \mapsto d'\circ f$, bijectively and preserving all four structures; apply it to $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]]) and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]).
>
> **What the proof shows.**
> - Only the complex-linear algebra structure is transported; unitarity and integrability to a group are not (Remark below; [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]] uses this theorem together with the compact group to recover complete reducibility).
> - ⚑ By-product: the finite-dimensional representations of the Lorentz algebra are classified by those of $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, i.e. by pairs of spins → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]].

^pf-cb-2-20

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]

> [!remark] Remark: What the correspondence does not transport
> Theorem §CB.2.20 transports the algebra of the representations, not unitarity and not the group: a representation of $\mathfrak{so}(4)$ that is unitary for $SU(2)\times SU(2)$ becomes a representation of $\mathfrak{so}(1,3)$ whose boosts are not unitary ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]). Complete reducibility does survive, which is Weyl's unitary trick ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]]): it needs the compact-group theorem of §CB.3, so it is stated there, after that theorem, and not here.

^rem-cb-2-1

## Real representations and their complexification

> [!definition] Definition §CB.2.21: Real Representation
> A **real representation** of a matrix Lie group $G$ is a continuous homomorphism $D : G \to GL(U)$ with $U$ a *real* finite-dimensional vector space; of a Lie algebra, a Lie algebra homomorphism $\mathfrak g \to \operatorname{End}_{\mathbb R}(U)$. Example: the vector representation of $SO^+(1,3)$ on $\mathbb R^{1,3}$, and the real two-index tensors $F^{\mu\nu}$.
>
> *Source: written here (Hall, An Elementary Introduction to Groups and Representations, Def. 5.1, real representations)*

^def-cb-2-21

> [!definition] Definition §CB.2.22: Complexification of a Real Representation
> The **complexification** of a real representation $D$ on $U$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-21|Def. §CB.2.21]]) is the representation $D_{\mathbb C}$ on $U_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]]) given by $D_{\mathbb C}(g)(u + iv) = D(g)u + iD(g)v$; it is complex-linear and commutes with the conjugation $c$.
>
> *Source: written here*

^def-cb-2-22

> [!theorem] Theorem §CB.2.23: The Complexification of an Irreducible Real Representation
> Let $D$ be a real representation on $U$ and $D_{\mathbb C}$ its complexification ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]).
> 1. $U' \mapsto U'_{\mathbb C}$ is a bijection from the invariant subspaces of $U$ onto the invariant subspaces of $U_{\mathbb C}$ that are mapped to themselves by $c$.
> 2. If $D$ is irreducible, then either $D_{\mathbb C}$ is irreducible, or $U_{\mathbb C} = W \oplus c(W)$ for an irreducible invariant subspace $W$, with $c(W)$ irreducible too.
>
> *Source: written here (the case of two-index tensors: [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], Derivation, step 5)*

^thm-cb-2-23

> [!proof]- Proof
> *Written here, along the route recorded in batch 1; no source with this proof was found in the texts used for CB (Hall's notes, Woit, Meinrenken, Etingof, Smith treat complexification of algebras and of representations but not this dichotomy). The two-index case is worked in [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], Derivation, step 5.*
>
> **Step 1** (invariance commutes with $c$). For $g$ in the group (or $X$ in the algebra), $D_{\mathbb C}(g)c(u + iv) = D(g)u - iD(g)v = c\,D_{\mathbb C}(g)(u + iv)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]). So if $W \subset U_{\mathbb C}$ is invariant, so is $c(W)$, a complex subspace because $c$ is conjugate-linear; and intersections and sums of invariant subspaces are invariant.
>
> **Step 2** (part 1: $c$-stable subspaces come from $U$). If $U' \subset U$ is invariant, then $U'_{\mathbb C} = U' + iU'$ is a complex subspace, invariant (Def. §CB.2.22) and $c$-stable. Conversely, let $W \subset U_{\mathbb C}$ be a complex subspace with $c(W) = W$, and put $U' = W \cap U$. For $w = u + iv \in W$ ($u, v \in U$): $u = \frac12(w + cw) \in W$ and $v = \frac1{2i}(w - cw) \in W$, so $u, v \in U'$ and $W = U' + iU' = U'_{\mathbb C}$. If $W$ is invariant, $U'$ is invariant (intersection of invariant $W$ with $U$, which $D_{\mathbb C}$ preserves). The maps $U' \mapsto U'_{\mathbb C}$ and $W \mapsto W \cap U$ are inverse: $U'_{\mathbb C} \cap U = U'$ (the real part of $u + iv$ with $u, v \in U'$).
>
> **Step 3** (part 2: a minimal invariant subspace). Let $D$ be irreducible and suppose $D_{\mathbb C}$ is not. Choose a nonzero invariant $W \subsetneq U_{\mathbb C}$ of smallest dimension; it is irreducible (a smaller nonzero invariant subspace inside it would contradict minimality). $c(W)$ is invariant (Step 1), of the same dimension, and irreducible ($c$ maps invariant subspaces of $c(W)$ bijectively to invariant subspaces of $W$).
>
> **Step 4** ($W \cap c(W) = 0$). $W \cap c(W)$ is invariant and $c$-stable, so by Step 2 it is $U'_{\mathbb C}$ for an invariant $U' \subset U$, which is $0$ or $U$ by irreducibility of $D$. If it were $U_{\mathbb C}$, then $W = U_{\mathbb C}$, excluded. So $W \cap c(W) = 0$.
>
> **Step 5** ($W + c(W) = U_{\mathbb C}$). $W + c(W)$ is invariant, $c$-stable ($c^2 = \mathbb 1$) and nonzero, so by Step 2 it is $U'_{\mathbb C}$ with $U' \ne 0$ invariant, hence $U' = U$ and $W + c(W) = U_{\mathbb C}$. With Step 4, $U_{\mathbb C} = W \oplus c(W)$.
>
> **What the proof shows.**
> - Either complexification keeps an irreducible real representation irreducible, or it splits it into two pieces exchanged by complex conjugation; for real two-forms $F^{\mu\nu}$ the pieces are the self-dual and anti-self-dual parts, $\mathbf E \pm i\mathbf B$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - ⚑ By-product: in the split case $\dim U = 2\dim W$, and the real representation is the complex representation $W$ "regarded as real"; the conjugate piece $c(W)$ carries the conjugate representation (§CB.4).

^pf-cb-2-23

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-21|Def. §CB.2.21]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]

> [!remark]- Connections
> - The duality operator on two-forms has eigenvalues $\pm i$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]): the real representation of $SO^+(1,3)$ on $F^{\mu\nu}$ is irreducible, and its complexification is $W \oplus c(W)$ with $W$ = the self-dual part — the second alternative of Theorem §CB.2.23, and the field-strength picture of Theorem §CB.2.12, 3 ($\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$ are exchanged by conjugation, [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - The same algebra, $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ over $\mathbb R$, is the hidden symmetry of the hydrogen atom ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]): there the split needs no $i$ (Theorem §CB.2.13), for the Lorentz algebra it does (Theorem §CB.2.14).
> - **Used in**: Theorem §CB.2.3–Theorem §CB.2.6 — the complexified rotation algebra and the ladder operators ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12|Def. §C3.1.12]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-13|Def. §C3.1.13]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]); Theorem §CB.2.5 — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-3|§C3.1, Remark: The physicist's i]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]; Theorem §CB.2.12 — [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-3|§C3.3, Remark: What the labels (j₊, j₋) mean]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorems §CB.2.13–§CB.2.14 — [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4|§C3.3, Remark: What the split does and does not mean]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]; Theorems §CB.2.17–§CB.2.19 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.2.23 — [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]].
