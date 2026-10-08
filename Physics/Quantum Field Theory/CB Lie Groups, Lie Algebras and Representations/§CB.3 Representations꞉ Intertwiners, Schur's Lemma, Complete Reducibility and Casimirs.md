---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): K. E. Smith, Groups and their Representations, Ch. 3 (§§1–9: representations, subrepresentations, equivalence, homomorphisms of representations, complete reducibility) and Ch. 4 §1 (Schur's lemma) · the user's PHY 513 notes, Ch. 7 §7.2, §7.4.3 · Yu Zhao-Huan, 量子场论讲义, §3.3.1 · Hall, Quantum Theory for Mathematicians, Ch. 16–17 · P. Woit, Quantum Theory, Groups and Representations, §2.1, Ch. 8 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

Which tools reduce a representation to irreducible pieces, and when does the reduction work? The course defines representations of groups and Lie algebras and their basic vocabulary in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] (decision SPEC-CB 1: those definitions stay there and are shown here as embeds). This section adds the general intertwiner, Schur's lemma and its corollaries, representations of associative algebras (needed for Clifford modules, §CB.8), Casimir elements, the compact-group theorems that make every representation unitary and completely reducible, Weyl's unitary trick that carries complete reducibility to the Lorentz algebra, and the theorem that a noncompact simple algebra has no nontrivial finite-dimensional unitary representation. It builds on [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] and [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]].

<!-- MOVE rows (CB-INVENTORY): Thm §C3.1.3 (Schur), Thm §C3.1.5 (compact groups), Ex §C3.1.1 (boosts as representations of ℝ) and the proof of Thm §C3.3.2 (Weyl's unitary trick) are to be moved here in batch 2; Def §C5a.1.12 (Clifford intertwiners) is to be moved here when this section is written (batch 2; SPEC-CB groups the §C5a.1 moves with batch 6 — settle then). All are embedded for now. -->

## Recalled: representations and their vocabulary

Defined in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] (the Lie algebra version is [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]], shown in §CB.2); for finite groups, [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-7|493 Def. §20.7]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-5]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10]]

## Intertwiners and Schur's lemma

> [!definition] Definition §CB.3.1: Intertwiner
> Let $D_1$, $D_2$ be representations of the same group or Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-5|Def. §C3.1.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]) on complex spaces $W_1$, $W_2$. An **intertwiner** is a linear map $S : W_1 \to W_2$ with $S\,D_1(x) = D_2(x)\,S$ for every element $x$ of the group (resp. algebra). They form a vector space $\operatorname{Hom}_G(W_1, W_2)$. $D_1$ and $D_2$ are equivalent ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]]) iff an invertible intertwiner exists.
>
> *Source (planned): Smith, Groups and their Representations, Ch. 3 §5 (Def. 5.1, "homomorphism of representations") · Woit, §2.1*

^def-cb-3-1

The Clifford version, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (the general version for algebras is Def. §CB.3.7 below):

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-12]]

> [!theorem] Theorem §CB.3.2: Kernel and Image of an Intertwiner Are Invariant
> If $S : W_1 \to W_2$ is an intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]), then $\ker S \subset W_1$ and $\operatorname{im}S \subset W_2$ are invariant subspaces ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]).
>
> *Source (planned): Smith, Groups and their Representations, Ch. 3 §6 (Prop. 6.2)*

^thm-cb-3-2

> [!proof]- Proof
> If $Sw = 0$ then $S\,D_1(x)w = D_2(x)\,Sw = 0$, so $D_1(x)w \in \ker S$. If $w' = Sw$ then $D_2(x)w' = D_2(x)Sw = S\,D_1(x)w \in \operatorname{im}S$.

^pf-cb-3-2

Schur's lemma, stated and proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3]]

> [!theorem] Theorem §CB.3.3: Central Elements Act as Scalars on Irreducible Representations
> Let $D$ be a finite-dimensional irreducible complex representation of a group $G$. If $z$ commutes with every element of $G$, then $D(z) = \lambda\,\mathbb 1$ for some $\lambda \in \mathbb C$. Likewise, any operator commuting with every $D(g)$ (or every $d(X)$, for a Lie algebra) is a multiple of $\mathbb 1$.
>
> *Source (planned): Smith, Groups and their Representations, Ch. 4 §1 · corollary of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], 2*

^thm-cb-3-3

> [!proof]- Proof (to be filled)
> *To be filled ($D(z)$ is an intertwiner of $D$ with itself; Schur, part 2).*

^pf-cb-3-3

> [!theorem] Theorem §CB.3.4: Irreducible Representations of Abelian Groups Are One-Dimensional
> Every finite-dimensional irreducible complex representation of an abelian group, or of an abelian Lie algebra, is one-dimensional.
>
> *Source (planned): Smith, Groups and their Representations, Ch. 4 §1 (Prop. 1.4)*

^thm-cb-3-4

> [!proof]- Proof (to be filled)
> *To be filled (Theorem §CB.3.3 applied to every element; then every line is invariant).*

^pf-cb-3-4

## Representations of associative algebras

> [!definition] Definition §CB.3.5: Associative Algebra
> An **associative algebra** over $\mathbb K = \mathbb R$ or $\mathbb C$ is a $\mathbb K$-vector space $A$ with a $\mathbb K$-bilinear associative product and a unit $1_A$. Examples: $M_n(\mathbb C)$, $\operatorname{End}(W)$, the quaternions $\mathbb H$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]) over $\mathbb R$.
>
> *Source (planned): written here*

^def-cb-3-5

> [!definition] Definition §CB.3.6: Algebra Homomorphism
> An **algebra homomorphism** between associative algebras over $\mathbb K$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) is a $\mathbb K$-linear map $f : A \to B$ with $f(ab) = f(a)f(b)$ and $f(1_A) = 1_B$; a bijective one is an **isomorphism**.
>
> *Source (planned): written here*

^def-cb-3-6

> [!definition] Definition §CB.3.7: Representation of an Associative Algebra
> A **representation** (or **module**) of an associative algebra $A$ over $\mathbb K$ on a complex vector space $W$ is an algebra homomorphism $\gamma : A \to \operatorname{End}_{\mathbb C}(W)$ that is $\mathbb K$-linear ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]], with $\operatorname{End}_{\mathbb C}(W)$ regarded as a $\mathbb K$-algebra). Invariant subspaces, irreducibility, direct sums, intertwiners and equivalence are defined by the words of [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]]–[[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|§C3.1.9]] and [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], with elements of $A$ in place of group elements.
>
> *Source (planned): written here*

^def-cb-3-7

> [!theorem] Theorem §CB.3.8: Schur's Lemma for Representations of an Associative Algebra
> [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]] and [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]] hold verbatim for representations of an associative algebra ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]): an intertwiner between irreducible representations is $0$ or invertible, and one from a finite-dimensional irreducible representation to itself is a multiple of $\mathbb 1$.
>
> *Source (planned): written here (same proof as Theorem §C3.1.3)*

^thm-cb-3-8

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-3-8

> [!theorem] Theorem §CB.3.9: Burnside's Theorem
> Let $W$ be a finite-dimensional complex vector space and $A \subset \operatorname{End}(W)$ a complex subalgebra containing $\mathbb 1$. If the only subspaces of $W$ invariant under every element of $A$ are $0$ and $W$, then $A = \operatorname{End}(W)$.
>
> *Source (planned): written here (standard); to be checked against a text when proved*

^thm-cb-3-9

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-3-9

## Casimir operators

The course's Casimir operator and its constancy on irreducible representations, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4]]

> [!definition] Definition §CB.3.10: Invariant Bilinear Form on a Lie Algebra
> A bilinear form $B$ on a Lie algebra $\mathfrak g$ is **invariant** if $B([Z, X], Y) + B(X, [Z, Y]) = 0$ for all $X, Y, Z \in \mathfrak g$ (each $\mathrm{ad}_Z$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-19|Def. §CB.1.19]], is skew for $B$).
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 17 · written here*

^def-cb-3-10

> [!theorem] Theorem §CB.3.11: The Casimir Operator of an Invariant Form
> Let $B$ be a nondegenerate symmetric invariant bilinear form on $\mathfrak g$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]), $\{X_a\}$ a basis and $\{X^a\}$ the dual basis, $B(X_a, X^b) = \delta_a{}^b$. For every representation $d$ of $\mathfrak g$ on $W$, $C_d = \sum_a d(X_a)\,d(X^a)$
> 1. does not depend on the basis;
> 2. commutes with every $d(Y)$, so it is a Casimir operator ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11|Def. §C3.1.11]]);
> 3. is a multiple of $\mathbb 1$ if $d$ is irreducible and finite-dimensional ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]]).
>
> Examples: for $\mathfrak{su}(2)$ with $B(X, Y) = -2\operatorname{tr}(XY)$, $C_d = -\mathbf J^2$ in the physicists' generators; for the Lorentz algebra with $B$ built from $g$, $C_d$ is a multiple of $\mathbf J^2 - \mathbf K^2$. (The Poincaré algebra has no nondegenerate invariant form; its Casimirs $P^2$ and $W^2$ are found by hand, [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-6|Theorem §C3.5.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-10|Theorem §C3.6.10]].)
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 17 · written here (the normalizations of the examples to be checked in batch 2)*

^thm-cb-3-11

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-3-11

## Compact groups: unitarity and complete reducibility

The course's statement for $SU(2)$ and $SO(3)$, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] by averaging over $S^3$:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5]]

> [!theorem] Theorem §CB.3.12: Haar Measure on a Compact Group
> On every compact matrix Lie group $G$ there is a unique Borel probability measure $\mu$ invariant under left and right translations: $\int_Gf(hg)\,d\mu(g) = \int_Gf(gh)\,d\mu(g) = \int_Gf(g)\,d\mu(g)$ for every continuous $f$ and $h \in G$. For $SU(2) \cong S^3$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-5|591 Prop. §41.5]]) it is the normalized round measure of $S^3$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 16–17 (cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]]) · Measure Theory (551) for the measure-theoretic background*

^thm-cb-3-12

> [!proof]- Proof (to be filled)
> *To be filled for SU(2) (the $S^3$ measure, as in Derivation §C3.1.5); the general existence (via a left-invariant volume form) is to be filled.*

^pf-cb-3-12

> [!theorem] Theorem §CB.3.13: Representations of Compact Groups Are Unitary
> Every finite-dimensional representation $D$ of a compact matrix Lie group $G$ on $W$ is unitary ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]): if $\langle\cdot,\cdot\rangle_0$ is any inner product on $W$, then $\langle v, w\rangle = \int_G\langle D(g)v, D(g)w\rangle_0\,d\mu(g)$ (Haar, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-12|Theorem §CB.3.12]]) is an inner product for which every $D(g)$ is unitary, and the physicists' generators are Hermitian.
>
> *Source (planned): Smith, Groups and their Representations, Ch. 3 §8 (the finite-group averaging) · Hall, Quantum Theory for Mathematicians, Ch. 17*

^thm-cb-3-13

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-3-13

> [!theorem] Theorem §CB.3.14: Unitary Representations Are Completely Reducible
> If a finite-dimensional representation (of a group, a Lie algebra or an associative algebra closed under adjoints) is unitary for an inner product, then the orthogonal complement of an invariant subspace is invariant, and the representation is an orthogonal direct sum of irreducible ones: completely reducible ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]]). Hence every finite-dimensional representation of a compact matrix Lie group is completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-13|Theorem §CB.3.13]]).
>
> *Source (planned): Smith, Groups and their Representations, Ch. 3 §8 (Thms. 8.1, 8.2, 8.4) · Hall, Quantum Theory for Mathematicians, Ch. 17*

^thm-cb-3-14

> [!proof]- Proof (to be filled)
> *To be filled (induction on dimension).*

^pf-cb-3-14

What fails without compactness, worked out in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-1]]

## Weyl's unitary trick

> [!theorem] Theorem §CB.3.15: Weyl's Unitary Trick
> Let $\mathfrak g$ be a real Lie algebra and $K$ a compact, simply connected matrix Lie group whose Lie algebra $\mathfrak k$ and $\mathfrak g$ are real forms of the same complex Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]). Then every finite-dimensional representation of $\mathfrak g$ on a complex space is completely reducible. In particular this holds for $\mathfrak g = \mathfrak{so}(1,3)$ and for $\mathfrak g = \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, with $K = SU(2)\times SU(2)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]), and for $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)$ with $K = SU(2)$.
>
> *Source (planned): Hall, Quantum Theory for Mathematicians, Ch. 17 · the Lorentz case written here in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], Derivation*

^thm-cb-3-15

> [!proof]- Proof (to be filled)
> *To be moved here from the derivation of Theorem §C3.3.2 in batch 2 and generalized: transfer the representation to $\mathfrak k$ (Theorem §CB.2.20), integrate it to $K$ (Theorem §CB.1.24), apply Theorem §CB.3.14, and transfer the invariant complements back (Theorem §CB.2.20).*

^pf-cb-3-15

The Lorentz case, stated in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]; its proof is the trick above:

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2]]

## Noncompact simple algebras have no finite-dimensional unitary representations

> [!theorem] Theorem §CB.3.16: No Nontrivial Finite-Dimensional Unitary Representation of a Noncompact Simple Algebra
> Let $\mathfrak g$ be a real simple Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]]) that has no positive-definite invariant inner product ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]). Then every finite-dimensional unitary representation of $\mathfrak g$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]) is zero. $\mathfrak{so}(1,3)$ satisfies the hypothesis: $\mathrm{ad}$ of a boost generator has nonzero real eigenvalues, impossible for an operator that is skew for an inner product.
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.3 (Principle "Hermitian generators do not make boosts unitary", citing Weinberg vol. 1 ch. 2) · written here*

^thm-cb-3-16

> [!proof]- Proof (to be filled)
> *To be filled (the kernel is an ideal; if it is $0$, $B(X, Y) = -\operatorname{tr}(d(X)d(Y))$ is a positive-definite invariant inner product). The Lorentz group version, by eigenvalues, is [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]].*

^pf-cb-3-16

## Representations on spaces of functions

> [!theorem] Theorem §CB.3.17: A Group Action Gives a Representation on Functions
> Let a group $G$ act on a set $X$ ([[§25 Actions#^def-25-1|493 Def. §25.1]]) and let $W$ be a complex vector space. On the vector space of maps $f : X \to W$,
>
> $$
> (D(g)f)(x) = f(g^{-1}x)
> $$
>
> is a representation of $G$ (a homomorphism into the invertible linear maps). With an additional representation $S$ of $G$ on $W$, $(D(g)f)(x) = S(g)f(g^{-1}x)$ is again one.
>
> *Source (planned): written here · the field laws: [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]*

^thm-cb-3-17

> [!proof]- Proof
> Each $D(g)$ is linear in $f$. For $g, h \in G$ and every $x$: $(D(g)D(h)f)(x) = S(g)\,(D(h)f)(g^{-1}x) = S(g)S(h)\,f(h^{-1}g^{-1}x) = S(gh)\,f((gh)^{-1}x) = (D(gh)f)(x)$, using $(gh)^{-1} = h^{-1}g^{-1}$ and that $S$ is a homomorphism. $D(\mathbb 1) = \mathbb 1$ because $\mathbb 1x = x$ and $S(\mathbb 1) = \mathbb 1$. The inverse $g^{-1}$ in the argument is what makes the order come out right; $f(gx)$ would give an anti-homomorphism. The first formula is the case $S \equiv \mathbb 1$.

^pf-cb-3-17

> [!remark]- Connections
> - Theorem §CB.3.16 and Theorem §CB.3.13 are the two halves of [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]]: field indices carry finite-dimensional, non-unitary representations; states carry unitary, infinite-dimensional ones.
> - Theorem §CB.3.9 (Burnside) is what makes Clifford modules rigid: an irreducible Clifford module sees all of $\operatorname{End}(W)$, which is Pauli's theorem in disguise (§CB.8).
> - **Used in**: Definition §CB.3.1 — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-13|Theorem §C5a.1.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]]; Theorem §CB.3.3 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4|Theorem §C3.1.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-6|Theorem §C3.5.6]]; Theorem §CB.3.4 — [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]; Theorems §CB.3.8–§CB.3.9 — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]; Theorem §CB.3.11 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4|Theorem §C3.1.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]; Theorems §CB.3.12–§CB.3.14 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]; Theorem §CB.3.15 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; Theorem §CB.3.16 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]; Theorem §CB.3.17 — [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-3|Theorem §C3.4.3]].
