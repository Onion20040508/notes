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

*Sources (planned for the proofs; each to be checked against the text when the proof is written): the user's PHY 513 notes, Ch. 7 §§7.2, 7.4 (J± and "the algebra decomposes") · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercises 3.1, 3.7 · Peskin & Schroeder, §3.1 · Hall, Quantum Theory for Mathematicians, Ch. 16–17 · P. Woit, Quantum Theory, Groups and Representations, §5.5 "Complexification", Ch. 40–41 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

The Lie algebra of a matrix Lie group is a *real* Lie algebra ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]). Physics nevertheless writes Hermitian generators $T_a = iX_a$, forms complex combinations such as $J^\pm = J^1 \pm iJ^2$ and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$, and says that the Lorentz algebra "is two copies of the rotation algebra". What are these objects, and in which sense is each statement true? This section answers with three structures: the complexification $\mathfrak g_{\mathbb C}$, which contains $i\mathfrak g$ and all complex combinations; the correspondence between representations of $\mathfrak g$ on *complex* vector spaces and complex-linear representations of $\mathfrak g_{\mathbb C}$; and real forms, the real algebras with the same complexification, told apart by their conjugations. It builds on [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] and on the course's definitions in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]; the representation theory it feeds is [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]].

<!-- MOVE rows (CB-INVENTORY): Def §C3.1.12 and Def §C3.1.13 are embedded below; they are to be moved here in batch 2 (Def §C3.1.12 sharpened to the basis-free definition; Def §C3.1.13 restated as part of Theorem §CB.2.6). -->

## Complexification

> [!definition] Definition §CB.2.1: Complex Lie Algebra
> A **complex Lie algebra** is a complex vector space $\mathfrak h$ with a complex-bilinear, skew-symmetric bracket $[\cdot,\cdot] : \mathfrak h\times\mathfrak h \to \mathfrak h$ satisfying the Jacobi identity (as in [[§48 Lie Bracket and Lie Algebra#^def-48-2|591 Def. §48.2]], with $\mathbb C$ in place of $\mathbb R$). Homomorphisms of complex Lie algebras are complex-linear ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]]). Example: $\mathfrak{sl}(2, \mathbb C)$ with the commutator.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, §5.5*

^def-cb-2-1

> [!definition] Definition §CB.2.2: Complexification of a Real Vector Space
> The **complexification** of a real vector space $V$ is $V_{\mathbb C} = V\times V$, with elements written $u + iv$ ($u, v \in V$), real addition componentwise, and multiplication by $a + ib \in \mathbb C$ given by $(a + ib)(u + iv) = (au - bv) + i(bu + av)$. It is a complex vector space with $\dim_{\mathbb C}V_{\mathbb C} = \dim_{\mathbb R}V$ (a real basis of $V$ is a complex basis of $V_{\mathbb C}$), and $V \subset V_{\mathbb C}$ as the vectors $u + i0$. Its **conjugation** is the real-linear map $c(u + iv) = u - iv$; it is conjugate-linear, $c^2 = \mathbb 1$, and its fixed set is $V$.
>
> *Source (planned): Woit, §5.5 · Hall, Quantum Theory for Mathematicians, Ch. 16*

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
> *Source (planned): Woit, §5.5 · Hall, Quantum Theory for Mathematicians, Ch. 16*

^thm-cb-2-3

> [!proof]- Proof (to be filled)
> *To be filled (bilinear expansion; Jacobi on basis elements).*

^pf-cb-2-3

> [!theorem] Theorem §CB.2.4: Complexification Inside the Matrices
> Let $\mathfrak g \subset M_n(\mathbb C)$ be a real Lie algebra of matrices with $\mathfrak g \cap i\mathfrak g = \{0\}$. Then $X + iY \mapsto X + iY$ (the right side a matrix) is an isomorphism of complex Lie algebras from $\mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]) onto $\mathfrak g + i\mathfrak g \subset M_n(\mathbb C)$, under which $c$ becomes $X + iY \mapsto X - iY$. Examples ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]): $\mathfrak u(n)_{\mathbb C} \cong \mathfrak{gl}(n, \mathbb C)$, $\mathfrak{su}(n)_{\mathbb C} \cong \mathfrak{sl}(n, \mathbb C)$, $\mathfrak{so}(n)_{\mathbb C} \cong \mathfrak{so}(n, \mathbb C) = \{X \in M_n(\mathbb C) : X^{\mathsf T} = -X\}$, and
>
> $$
> \mathfrak{so}(1,3)_{\mathbb C} \cong \{X \in M_4(\mathbb C) : X^{\mathsf T}\eta + \eta X = 0\}, \qquad c(X) = \bar X .
> $$
>
> The condition $\mathfrak g \cap i\mathfrak g = \{0\}$ fails for $\mathfrak{sl}(2, \mathbb C)$ regarded as a real Lie algebra; that case is Theorem §CB.2.18.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · Woit, §5.5*

^thm-cb-2-4

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-4

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
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.2 ("The physicist's i") · Woit, §5.1 (the factor i convention), §5.5 · written here*

^thm-cb-2-5

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-5

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
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 17 (cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-13|Def. §C3.1.13]]) · Woit, §5.5*

^thm-cb-2-6

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-6

## Ideals, simple algebras and real forms

> [!definition] Definition §CB.2.7: Ideal
> An **ideal** of a (real or complex) Lie algebra $\mathfrak g$ is a subspace $\mathfrak a$ with $[X, A] \in \mathfrak a$ for all $X \in \mathfrak g$, $A \in \mathfrak a$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-2-7

> [!definition] Definition §CB.2.8: Direct Sum of Lie Algebras
> The **direct sum** $\mathfrak g_1 \oplus \mathfrak g_2$ of Lie algebras (both real or both complex) is the vector space $\mathfrak g_1 \oplus \mathfrak g_2$ with $[(X_1, X_2), (Y_1, Y_2)] = ([X_1, Y_1], [X_2, Y_2])$. A Lie algebra is the direct sum of two ideals $\mathfrak a$, $\mathfrak b$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]) if $\mathfrak g = \mathfrak a \oplus \mathfrak b$ as vector spaces; then $[\mathfrak a, \mathfrak b] = 0$ and $\mathfrak g \cong \mathfrak a \oplus \mathfrak b$ as Lie algebras.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-2-8

> [!definition] Definition §CB.2.9: Simple Lie Algebra
> A (real or complex) Lie algebra $\mathfrak g$ is **simple** if it is not abelian and its only ideals ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]) are $\{0\}$ and $\mathfrak g$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16*

^def-cb-2-9

> [!definition] Definition §CB.2.10: Real Form
> A **real form** of a complex Lie algebra $\mathfrak h$ is a real Lie subalgebra $\mathfrak g_0 \subset \mathfrak h$ (closed under real combinations and the bracket) with $\mathfrak h = \mathfrak g_0 \oplus i\mathfrak g_0$ as real vector spaces. Then $X + iY \mapsto X + iY$ is an isomorphism $(\mathfrak g_0)_{\mathbb C} \cong \mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]).
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · written here*

^def-cb-2-10

> [!theorem] Theorem §CB.2.11: Real Forms Are the Fixed Sets of Conjugations
> Let $\mathfrak h$ be a complex Lie algebra. A **conjugation** of $\mathfrak h$ is a conjugate-linear map $\sigma : \mathfrak h \to \mathfrak h$ with $\sigma^2 = \mathbb 1$ and $\sigma[Z, W] = [\sigma Z, \sigma W]$. Then $\sigma \mapsto \mathfrak h^\sigma = \{Z : \sigma Z = Z\}$ is a bijection from conjugations of $\mathfrak h$ onto real forms of $\mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]); the inverse sends $\mathfrak g_0$ to $X + iY \mapsto X - iY$ ($X, Y \in \mathfrak g_0$). Two real forms $\mathfrak g_0$, $\mathfrak g_0'$ are isomorphic as real Lie algebras if and only if there is a complex-linear automorphism $\alpha$ of $\mathfrak h$ with $\alpha\sigma = \sigma'\alpha$.
>
> *Source (planned): written here (standard); to be checked against a text*

^thm-cb-2-11

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-11

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
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Yu, Exercise 3.1 · written here (parts 1 and 3)*

^thm-cb-2-12

> [!proof]- Proof (to be filled)
> *To be filled. The brackets of part 2 are computed in any representation, hence in the vector representation, in [[§C3.2 The Lorentz Algebra#^der-c3-2-1c|Derivation §C3.2.1 (the J, K form and the J± split)]], steps 6–7; part 3 from $c(J_i) = -J_i$, $c(K_i) = -K_i$ (Theorem §CB.2.5, 2).*

^pf-cb-2-12

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
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.4.6 · [[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]] (the same split for the Coulomb problem) · written here*

^thm-cb-2-13

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-13

> [!theorem] Theorem §CB.2.14: 𝔰𝔬(1,3) and 𝔰𝔬(4) Are Two Real Forms of One Complex Algebra
> 1. $J_{\pm i} \mapsto A_{\pm i}$ extends to an isomorphism of complex Lie algebras $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C} \cong \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-13|Theorem §CB.2.13]]); under it $\mathfrak{so}(1,3)$ and $\mathfrak{so}(4)$ are real forms ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]) of the same complex algebra.
> 2. Their conjugations differ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-11|Theorem §CB.2.11]]): that of $\mathfrak{so}(4)$ maps each $\mathfrak{sl}(2, \mathbb C)$ summand to itself, that of $\mathfrak{so}(1,3)$ exchanges the two.
> 3. $\mathfrak{so}(1,3)$ is simple as a real Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]]). In particular $\mathfrak{so}(1,3) \not\cong \mathfrak{su}(2)\oplus\mathfrak{su}(2) \cong \mathfrak{so}(4)$: the real Lorentz algebra is **not** two copies of the rotation algebra; only its complexification is two copies of the complexified rotation algebra $\mathfrak{sl}(2, \mathbb C)$.
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §§7.4.1, 7.4.6 ("The accurate statement is that the algebra … decomposes") · written here*

^thm-cb-2-14

> [!proof]- Proof (to be filled)
> *To be filled (part 3: an ideal $\mathfrak a$ of $\mathfrak{so}(1,3)$ gives the $c$-stable ideal $\mathfrak a_{\mathbb C}$ of $\mathfrak a_+\oplus\mathfrak a_-$; the only ideals of $\mathfrak a_+\oplus\mathfrak a_-$ are $0$, $\mathfrak a_+$, $\mathfrak a_-$ and all, because $\mathfrak{sl}(2, \mathbb C)$ is simple, and $c$ exchanges $\mathfrak a_\pm$).*

^pf-cb-2-14

The course's remark on what the split does and does not mean, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]] (see also [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]]):

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4]]

> [!theorem] Theorem §CB.2.15: Two Real Forms of 𝔰𝔩(2,ℂ)
> $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb R)$ are real forms of $\mathfrak{sl}(2, \mathbb C)$, with conjugations $X \mapsto -X^\dagger$ and $X \mapsto \bar X$. They are not isomorphic: $\mathfrak{su}(2)$ has no element $X \ne 0$ for which $\mathrm{ad}_X$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-19|Def. §CB.1.19]]) has a nonzero real eigenvalue, while $H = \operatorname{diag}(1, -1) \in \mathfrak{sl}(2, \mathbb R)$ has $\mathrm{ad}_H$-eigenvalues $0, \pm2$. Moreover $\mathfrak{sl}(2, \mathbb R) \cong \mathfrak{so}(1,2)$ and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16 · written here*

^thm-cb-2-15

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-15

## 𝔰𝔩(2,ℂ) as a real Lie algebra

> [!definition] Definition §CB.2.16: Underlying Real Lie Algebra
> The **underlying real Lie algebra** (realification) $\mathfrak h_{\mathbb R}$ of a complex Lie algebra $\mathfrak h$ is $\mathfrak h$ with scalars restricted to $\mathbb R$; $\dim_{\mathbb R}\mathfrak h_{\mathbb R} = 2\dim_{\mathbb C}\mathfrak h$. The Lie algebra of the matrix Lie group $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]) is $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]).
>
> *Source (planned): written here*

^def-cb-2-16

> [!theorem] Theorem §CB.2.17: The Real Lie Algebra of SL(2,ℂ) Is the Lorentz Algebra
> The differential ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) of the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] is an isomorphism of real Lie algebras $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]); in the conventions of Theorem §C5a.4.7 it sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $-\frac12\sigma^k \mapsto -iK_k$.
>
> *Source (planned): Yu, Exercise 3.7 · the user's PHY 513 notes, Ch. 8 §8.2 · written here*

^thm-cb-2-17

> [!proof]- Proof (to be filled)
> *To be filled (differentiate part 3 of Theorem §C5a.4.7).*

^pf-cb-2-17

> [!theorem] Theorem §CB.2.18: The Complexification of Real 𝔰𝔩(2,ℂ) Is Two Copies of 𝔰𝔩(2,ℂ)
> The map $\Phi : (\mathfrak{sl}(2, \mathbb C)_{\mathbb R})_{\mathbb C} \to \mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$,
>
> $$
> \Phi(X + iY) = \bigl(X + iY,\ \bar X + i\bar Y\bigr) \qquad (X, Y \in \mathfrak{sl}(2, \mathbb C)_{\mathbb R};\ \bar X \text{ the entrywise conjugate}),
> $$
>
> is an isomorphism of complex Lie algebras. So the complexification of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ has complex dimension $6$ and is not $\mathfrak{sl}(2, \mathbb C)$; on the real algebra, $X \mapsto (X, \bar X)$.
>
> *Source (planned): written here*

^thm-cb-2-18

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-18

> [!theorem] Theorem §CB.2.19: Representations of Real 𝔰𝔩(2,ℂ): a Complex-Linear and an Antilinear Part
> Let $\rho : \mathfrak{sl}(2, \mathbb C)_{\mathbb R} \to \operatorname{End}_{\mathbb C}(W)$ be a representation on a complex vector space $W$. There are unique maps $\rho_1$, $\rho_2$ with $\rho = \rho_1 + \rho_2$, $\rho_1$ complex-linear and $\rho_2$ complex-antilinear ($\rho_2(iX) = -i\rho_2(X)$), both Lie algebra homomorphisms, and $[\rho_1(X), \rho_2(Y)] = 0$ for all $X, Y$. Conversely every such commuting pair gives a representation. The defining representation $X \mapsto X$ on $\mathbb C^2$ has $\rho_2 = 0$; its complex conjugate $X \mapsto \bar X$ has $\rho_1 = 0$.
>
> *Source (planned): written here (from Theorem §CB.2.18 and Theorem §CB.2.6)*

^thm-cb-2-19

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-19

> [!theorem] Theorem §CB.2.20: Real Forms Have the Same Representations
> If $\mathfrak g_1$ and $\mathfrak g_2$ are real forms of the same complex Lie algebra $\mathfrak h$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]), then restriction and complex-linear extension ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]) give bijections between the representations of $\mathfrak g_1$ on complex spaces, the complex-linear representations of $\mathfrak h$, and the representations of $\mathfrak g_2$ on complex spaces, preserving invariant subspaces, irreducibility, direct sums and intertwiners. Example: the finite-dimensional complex representations of $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$, $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ correspond to one another (Theorems §CB.2.14, §CB.2.17).
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 17 · written here*

^thm-cb-2-20

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-2-20

> [!remark] Remark: What the correspondence does not transport
> Theorem §CB.2.20 transports the algebra of the representations, not unitarity and not the group: a representation of $\mathfrak{so}(4)$ that is unitary for $SU(2)\times SU(2)$ becomes a representation of $\mathfrak{so}(1,3)$ whose boosts are not unitary ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]). Complete reducibility does survive, which is Weyl's unitary trick ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]]): it needs the compact-group theorem of §CB.3, so it is stated there, after that theorem, and not here.

^rem-cb-2-1

## Real representations and their complexification

> [!definition] Definition §CB.2.21: Real Representation
> A **real representation** of a matrix Lie group $G$ is a continuous homomorphism $D : G \to GL(U)$ with $U$ a *real* finite-dimensional vector space; of a Lie algebra, a Lie algebra homomorphism $\mathfrak g \to \operatorname{End}_{\mathbb R}(U)$. Example: the vector representation of $SO^+(1,3)$ on $\mathbb R^{1,3}$, and the real two-index tensors $F^{\mu\nu}$.
>
> *Source (planned): written here*

^def-cb-2-21

> [!definition] Definition §CB.2.22: Complexification of a Real Representation
> The **complexification** of a real representation $D$ on $U$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-21|Def. §CB.2.21]]) is the representation $D_{\mathbb C}$ on $U_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-2|Def. §CB.2.2]]) given by $D_{\mathbb C}(g)(u + iv) = D(g)u + iD(g)v$; it is complex-linear and commutes with the conjugation $c$.
>
> *Source (planned): written here*

^def-cb-2-22

> [!theorem] Theorem §CB.2.23: The Complexification of an Irreducible Real Representation
> Let $D$ be a real representation on $U$ and $D_{\mathbb C}$ its complexification ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-22|Def. §CB.2.22]]).
> 1. $U' \mapsto U'_{\mathbb C}$ is a bijection from the invariant subspaces of $U$ onto the invariant subspaces of $U_{\mathbb C}$ that are mapped to themselves by $c$.
> 2. If $D$ is irreducible, then either $D_{\mathbb C}$ is irreducible, or $U_{\mathbb C} = W \oplus c(W)$ for an irreducible invariant subspace $W$, with $c(W)$ irreducible too.
>
> *Source (planned): written here (the case of two-index tensors: [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], Derivation, step 5)*

^thm-cb-2-23

> [!proof]- Proof (to be filled)
> *To be filled (part 2: for a minimal invariant $W \subset U_{\mathbb C}$, $W\cap c(W)$ and $W + c(W)$ are $c$-stable and invariant).*

^pf-cb-2-23

> [!remark]- Connections
> - The duality operator on two-forms has eigenvalues $\pm i$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]): the real representation of $SO^+(1,3)$ on $F^{\mu\nu}$ is irreducible, and its complexification is $W \oplus c(W)$ with $W$ = the self-dual part — the second alternative of Theorem §CB.2.23, and the field-strength picture of Theorem §CB.2.12, 3 ($\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$ are exchanged by conjugation, [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]).
> - The same algebra, $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ over $\mathbb R$, is the hidden symmetry of the hydrogen atom ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-5|QM Theorem §C8.1.5]]): there the split needs no $i$ (Theorem §CB.2.13), for the Lorentz algebra it does (Theorem §CB.2.14).
> - **Used in**: Theorem §CB.2.3–Theorem §CB.2.6 — the complexified rotation algebra and the ladder operators ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-12|Def. §C3.1.12]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-13|Def. §C3.1.13]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]); Theorem §CB.2.5 — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-3|§C3.1, Remark: The physicist's i]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]; Theorem §CB.2.12 — [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-3|§C3.3, Remark: What the labels (j₊, j₋) mean]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorems §CB.2.13–§CB.2.14 — [[§C3.2 The Lorentz Algebra#^cau-c3-2-1|§C3.2, Caution: The algebra decomposes; it is not "reducible"]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-4|§C3.3, Remark: What the split does and does not mean]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]; Theorems §CB.2.17–§CB.2.19 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.2.23 — [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]].
