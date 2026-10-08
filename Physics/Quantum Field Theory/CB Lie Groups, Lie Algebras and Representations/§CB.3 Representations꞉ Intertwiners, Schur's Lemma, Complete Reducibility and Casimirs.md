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

*Sources (proofs written from these, each checked against the text): K. E. Smith, Groups and their Representations, Ch. 3 §§5–9, Ch. 4 §1 · B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5 (https://arxiv.org/abs/math-ph/0005032) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §§18.3, 34.4, 35.1, 37.1 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 16.10 · J. H. Shapiro, Burnside's Theorem on Matrix Algebras (2014), after Lomonosov–Rosenthal (2004) (https://joelshapiro.org/Pubvit/Downloads/BurnsideThm/burnside.pdf) · the user's PHY 513 notes, Ch. 7 §§7.2–7.4 · Yu Zhao-Huan, 量子场论讲义, §3.3.1 · P. Woit, Quantum Theory, Groups and Representations, §2.1, Ch. 8 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

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
> *Source: Smith, Groups and their Representations, Ch. 3 §5 (Def. 5.1, "homomorphism of representations") · Woit, §2.1*

^def-cb-3-1

The Clifford version, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (the general version for algebras is Def. §CB.3.7 below):

![[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-12]]

> [!theorem] Theorem §CB.3.2: Kernel and Image of an Intertwiner Are Invariant
> If $S : W_1 \to W_2$ is an intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]), then $\ker S \subset W_1$ and $\operatorname{im}S \subset W_2$ are invariant subspaces ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]).
>
> *Source: Smith, Groups and their Representations, Ch. 3 §6 (Prop. 6.2)*

^thm-cb-3-2

> [!proof]- Proof
> If $Sw = 0$ then $S\,D_1(x)w = D_2(x)\,Sw = 0$, so $D_1(x)w \in \ker S$. If $w' = Sw$ then $D_2(x)w' = D_2(x)Sw = S\,D_1(x)w \in \operatorname{im}S$.

^pf-cb-3-2

Schur's lemma, stated and proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3]]

> [!theorem] Theorem §CB.3.3: Central Elements Act as Scalars on Irreducible Representations
> Let $D$ be a finite-dimensional irreducible complex representation of a group $G$. If $z$ commutes with every element of $G$, then $D(z) = \lambda\,\mathbb 1$ for some $\lambda \in \mathbb C$. Likewise, any operator commuting with every $D(g)$ (or every $d(X)$, for a Lie algebra) is a multiple of $\mathbb 1$.
>
> *Source: Smith, Groups and their Representations, Ch. 4 §1.1 (the argument before Prop. 1.4) · Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Cor. 5.29 · corollary of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], 2*

^thm-cb-3-3

> [!proof]- Proof
> *Source: K. E. Smith, Groups and their Representations, Ch. 4 §1.1: "if $G$ is abelian, or more generally if $g$ is in its center, then the action of $g$ on $V$ is $G$-linear", followed by Schur's lemma (Lemma 1.1) · B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Cor. 5.29 (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** ($D(z)$ is an intertwiner). For every $h \in G$, $zh = hz$ gives $D(z)D(h) = D(zh) = D(hz) = D(h)D(z)$. So $D(z)$ is an intertwiner of $D$ with itself ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]).
>
> **Step 2** (Schur). $D$ is finite-dimensional, irreducible and complex, so by [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], 2, $D(z) = \lambda\mathbb 1$ for some $\lambda \in \mathbb C$.
>
> **Step 3** (the general form). An operator $T$ with $TD(g) = D(g)T$ for all $g$ (or $Td(X) = d(X)T$ for all $X$, for a Lie algebra) is by definition an intertwiner of the representation with itself, and Step 2 applies verbatim: $T = \lambda\mathbb 1$.
>
> **What the proof shows.**
> - Over $\mathbb R$ it fails: a rotation of the plane by $90°$ commutes with the irreducible action of the rotation group of the square and is not a multiple of $\mathbb 1$ (Smith, after Lemma 1.1); the eigenvalue needed in Schur's lemma exists only over $\mathbb C$.
> - Used for Casimirs (Theorem §CB.3.11) and for $D(-\mathbb 1) = \pm\mathbb 1$ on irreducible representations of $SU(2)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]).

^pf-cb-3-3

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]

> [!theorem] Theorem §CB.3.4: Irreducible Representations of Abelian Groups Are One-Dimensional
> Every finite-dimensional irreducible complex representation of an abelian group, or of an abelian Lie algebra, is one-dimensional.
>
> *Source: Smith, Groups and their Representations, Ch. 4 §1.1, Prop. 1.4 · Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Cor. 5.30*

^thm-cb-3-4

> [!proof]- Proof
> *Source: K. E. Smith, Groups and their Representations, Ch. 4 §1.1, Prop. 1.4 and its proof (stated there for groups; the Lie algebra case is the same argument with Theorem §CB.3.3 for algebras) · B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Cor. 5.30 (https://arxiv.org/abs/math-ph/0005032).*
>
> **Step 1** (every element acts as a scalar). In an abelian group every $g$ is central, so on a finite-dimensional irreducible complex representation $D(g) = \lambda(g)\mathbb 1$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]]). For an abelian Lie algebra, $[d(X), d(Y)] = d([X, Y]) = 0$, so each $d(X)$ commutes with all $d(Y)$ and $d(X) = \lambda(X)\mathbb 1$ by the last sentence of Theorem §CB.3.3.
>
> **Step 2** (every line is invariant). A scalar multiple of $\mathbb 1$ maps every subspace into itself; so every one-dimensional subspace of $W$ is invariant ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]). Irreducibility leaves no proper nonzero invariant subspace, so $W$ itself is a line: $\dim W = 1$.
>
> **What the proof shows.**
> - Irreducible representations of an abelian group are characters $\lambda : G \to \mathbb C^\times$; for $U(1)$, $e^{i\phi} \mapsto e^{in\phi}$ — the charges and helicities of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]].
> - Finite dimension and $\mathbb C$ are both used (through Schur); over $\mathbb R$, rotations of the plane are an irreducible two-dimensional representation of the abelian $SO(2)$.

^pf-cb-3-4

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]

## Representations of associative algebras

> [!definition] Definition §CB.3.5: Associative Algebra
> An **associative algebra** over $\mathbb K = \mathbb R$ or $\mathbb C$ is a $\mathbb K$-vector space $A$ with a $\mathbb K$-bilinear associative product and a unit $1_A$. Examples: $M_n(\mathbb C)$, $\operatorname{End}(W)$, the quaternions $\mathbb H$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]) over $\mathbb R$.
>
> *Source: written here*

^def-cb-3-5

> [!definition] Definition §CB.3.6: Algebra Homomorphism
> An **algebra homomorphism** between associative algebras over $\mathbb K$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]) is a $\mathbb K$-linear map $f : A \to B$ with $f(ab) = f(a)f(b)$ and $f(1_A) = 1_B$; a bijective one is an **isomorphism**.
>
> *Source: written here*

^def-cb-3-6

> [!definition] Definition §CB.3.7: Representation of an Associative Algebra
> A **representation** (or **module**) of an associative algebra $A$ over $\mathbb K$ on a complex vector space $W$ is an algebra homomorphism $\gamma : A \to \operatorname{End}_{\mathbb C}(W)$ that is $\mathbb K$-linear ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-6|Def. §CB.3.6]], with $\operatorname{End}_{\mathbb C}(W)$ regarded as a $\mathbb K$-algebra). Invariant subspaces, irreducibility, direct sums, intertwiners and equivalence are defined by the words of [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]]–[[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|§C3.1.9]] and [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], with elements of $A$ in place of group elements.
>
> *Source: written here*

^def-cb-3-7

> [!theorem] Theorem §CB.3.8: Schur's Lemma for Representations of an Associative Algebra
> [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]] and [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]] hold verbatim for representations of an associative algebra ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]): an intertwiner between irreducible representations is $0$ or invertible, and one from a finite-dimensional irreducible representation to itself is a multiple of $\mathbb 1$.
>
> *Source: Smith, Groups and their Representations, Ch. 3, Lemma 9.2, Ch. 4, Lemma 1.1 (the same proofs, there for groups) · [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-3|Derivation §C3.1.3]]*

^thm-cb-3-8

> [!proof]- Proof
> *Source: K. E. Smith, Groups and their Representations, Ch. 3, Lemma 9.2 ("a homomorphism of irreducible representations is either zero or an isomorphism") and Ch. 4, Lemma 1.1 (Schur's lemma over $\mathbb C$), whose proofs use only kernels, images and an eigenvalue, never inverses of group elements; and the vault's [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-3|Derivation §C3.1.3]], whose three steps are repeated here with elements $a \in A$ in place of group elements.*
>
> **Step 1** (kernel and image). Let $S : W_1 \to W_2$ intertwine $\gamma_1$, $\gamma_2$: $S\gamma_1(a) = \gamma_2(a)S$ for all $a \in A$. If $Sw = 0$ then $S\gamma_1(a)w = \gamma_2(a)Sw = 0$, so $\ker S$ is invariant; if $w' = Sw$ then $\gamma_2(a)w' = S\gamma_1(a)w \in \operatorname{im}S$. (This is [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-2|Theorem §CB.3.2]] with $a$ in place of $x$.)
>
> **Step 2** (zero or invertible). If $\gamma_1$, $\gamma_2$ are irreducible, $\ker S \in \{0, W_1\}$ and $\operatorname{im}S \in \{0, W_2\}$. If $S \ne 0$, then $\ker S \ne W_1$ and $\operatorname{im}S \ne 0$, so $\ker S = 0$ and $\operatorname{im}S = W_2$: $S$ is bijective.
>
> **Step 3** (scalars). Let $W_1 = W_2 = W$ be finite-dimensional, complex and irreducible, and $S$ an intertwiner of $\gamma$ with itself. $S$ has an eigenvalue $\lambda \in \mathbb C$ ([[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]]). $S - \lambda\mathbb 1$ is again an intertwiner (each $\gamma(a)$ commutes with $\mathbb 1$) and is not invertible, so by Step 2 it is $0$: $S = \lambda\mathbb 1$. In particular, if $z \in A$ commutes with all of $A$, $\gamma(z)$ is an intertwiner and $\gamma(z) = \lambda\mathbb 1$ (the analogue of [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]]).
>
> **What the proof shows.**
> - Nothing about groups was used: only that the represented objects act linearly and that an intertwiner commutes with each of them. So Schur's lemma holds for any set of operators, hence for Clifford modules ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]).
> - Step 3 needs $\mathbb C$ and finite dimension (an eigenvalue); for the real algebra $\mathbb H$ acting on the real space $\mathbb H$ by left multiplication (irreducible, since $\mathbb H$ is a division algebra), multiplication by $i$ from the right commutes with all left multiplications and is not real-scalar.

^pf-cb-3-8

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-2|Theorem §CB.3.2]], [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]]

> [!theorem] Theorem §CB.3.9: Burnside's Theorem
> Let $W$ be a finite-dimensional complex vector space and $A \subset \operatorname{End}(W)$ a complex subalgebra containing $\mathbb 1$. If the only subspaces of $W$ invariant under every element of $A$ are $0$ and $W$, then $A = \operatorname{End}(W)$.
>
> *Source: V. Lomonosov and P. Rosenthal, The simplest proof of Burnside's theorem on matrix algebras, Linear Algebra Appl. 383 (2004) 45–47, as written out in J. H. Shapiro, Burnside's Theorem on Matrix Algebras (2014) · Etingof et al., Introduction to Representation Theory, Thm. 2.5 (the density theorem, a second route)*

^thm-cb-3-9

> [!proof]- Proof
> *Source: J. H. Shapiro, Burnside's Theorem on Matrix Algebras (note, 2014), §§2.1(c), 3 (https://joelshapiro.org/Pubvit/Downloads/BurnsideThm/burnside.pdf), presenting the proof of V. Lomonosov and P. Rosenthal, Linear Algebra Appl. 383 (2004) 45–47. A second route is the density theorem, P. Etingof et al., Introduction to Representation Theory, Cor. 2.4 and Thm. 2.5 (https://arxiv.org/abs/0901.0827). Fix an inner product on $W$; $v \otimes w$ denotes the rank-one operator $x \mapsto \langle w, x\rangle v$ (inner product antilinear in the first slot, so that this map is linear; Shapiro, with the opposite convention, writes $\langle x, w\rangle v$).*
>
> **Step 1** (the case $\dim W = 1$). Then $\operatorname{End}(W) = \mathbb C\mathbb 1 \subset A$. From now on $n = \dim W \ge 2$.
>
> **Step 2** (irreducible means transitive; Shapiro, §2.1(c)). For $x \ne 0$, $Ax = \{ax : a \in A\}$ is a subspace (A is a vector space), invariant under $A$ ($b(ax) = (ba)x$), and contains $x = \mathbb 1x$. So $Ax = W$ by irreducibility.
>
> **Step 3** (the lemma). *Every subalgebra $B \ne 0$ of $\operatorname{End}(V)$, $V$ a finite-dimensional complex space, with $Bx = V$ for all $x \ne 0$ ("transitive"; $B$ need not contain $\mathbb 1$), contains an operator of rank one.* Induction on $\dim V$; for $\dim V = 1$ every nonzero operator has rank one. Let $\dim V = m > 1$.
> - *A non-invertible nonzero $S \in B$.* $B \not\subset \mathbb C\mathbb 1$: otherwise $Bx \subset \mathbb Cx \ne V$. Take $T \in B$, not a multiple of $\mathbb 1$ (so $T \ne 0$). If $T$ is not invertible, $S = T$. Otherwise $T$ has an eigenvalue $\lambda$ ([[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]]), and $T - \lambda\mathbb 1$ is nonzero and not invertible; $S = T(T - \lambda\mathbb 1) = T^2 - \lambda T \in B$ is not invertible (its second factor is not) and nonzero ($T$ is invertible and $T - \lambda\mathbb 1 \ne 0$).
> - *Compress to $V_0 = S(V)$.* $0 < \dim V_0 < m$. Each $SA$ ($A \in B$) maps $V_0$ into $S(V) = V_0$; let $B_0 = \{SA|_{V_0} : A \in B\}$. It is a subalgebra: linear in $A$, and $(SA)(SA') = S(ASA')$ with $ASA' \in B$. It is transitive: for $0 \ne w \in V_0$, $Bw = V$, so $B_0w = S(Bw) = S(V) = V_0$; in particular $B_0 \ne 0$.
> - *Induction.* $B_0$ contains a rank-one operator: some $A \in B$ with $SA|_{V_0}$ of rank one. Then $SAS \in B$ has image $SA(S(V)) = SA(V_0)$, one-dimensional.
>
> **Step 4** (all rank-one operators lie in $A$). By Step 3 (with $B = A$, $V = W$, transitive by Step 2), $A \ni v \otimes w$ for some $v, w \ne 0$. For $T \in A$: $T(v\otimes w) = (Tv)\otimes w$, and as $T$ runs through $A$, $Tv$ runs through all of $W$ (Step 2); so $v'\otimes w \in A$ for every $v'$. Next, $(v'\otimes w)T : x \mapsto \langle w, Tx\rangle v' = \langle T^\dagger w, x\rangle v'$, i.e. $(v'\otimes w)T = v'\otimes(T^\dagger w) \in A$. The adjoint algebra $A^\dagger = \{T^\dagger : T \in A\}$ contains $\mathbb 1$ and is irreducible: if $M$ is invariant under all $T^\dagger$, then for $y \in M^\perp$, $m \in M$, $\langle m, Ty\rangle = \langle T^\dagger m, y\rangle = 0$, so $M^\perp$ is $A$-invariant, hence $0$ or $W$, and $M = (M^\perp)^\perp$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]]) is $W$ or $0$. By Step 2 for $A^\dagger$, $T^\dagger w$ runs through all of $W$. So $v'\otimes w' \in A$ for all $v', w' \in W$.
>
> **Step 5** (conclusion). In an orthonormal basis $e_1, \dots, e_n$, $e_i\otimes e_j$ has matrix $E_{ij}$ (a $1$ in row $i$, column $j$), and the $E_{ij}$ span all matrices. So $A = \operatorname{End}(W)$.
>
> **What the proof shows.**
> - The only use of $\mathbb C$ is the eigenvalue in Step 3; over $\mathbb R$ the theorem fails ($\mathbb C \subset M_2(\mathbb R)$ acts irreducibly on $\mathbb R^2$).
> - ⚑ By-product: an irreducible family of operators "sees" every matrix; for Clifford modules this forces the matrices of the generators to span $\operatorname{End}(W)$, which is Pauli's theorem's uniqueness argument (§CB.8).

^pf-cb-3-9

*Uses:* [[§15 The Minimal Polynomial#^ladr-5-19|LADR 5.19]], [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-5|Def. §CB.3.5]]

## Casimir operators

The course's Casimir operator and its constancy on irreducible representations, in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11]]

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4]]

> [!definition] Definition §CB.3.10: Invariant Bilinear Form on a Lie Algebra
> A bilinear form $B$ on a Lie algebra $\mathfrak g$ is **invariant** if $B([Z, X], Y) + B(X, [Z, Y]) = 0$ for all $X, Y, Z \in \mathfrak g$ (each $\mathrm{ad}_Z$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-19|Def. §CB.1.19]], is skew for $B$).
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §18.3 ("an invariant inner product on 𝔤") · written here*

^def-cb-3-10

> [!theorem] Theorem §CB.3.11: The Casimir Operator of an Invariant Form
> Let $B$ be a nondegenerate symmetric invariant bilinear form on $\mathfrak g$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]), $\{X_a\}$ a basis and $\{X^a\}$ the dual basis, $B(X_a, X^b) = \delta_a{}^b$. For every representation $d$ of $\mathfrak g$ on $W$, $C_d = \sum_a d(X_a)\,d(X^a)$
> 1. does not depend on the basis;
> 2. commutes with every $d(Y)$, so it is a Casimir operator ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11|Def. §C3.1.11]]);
> 3. is a multiple of $\mathbb 1$ if $d$ is irreducible and finite-dimensional ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]]).
>
> Examples (traces in the defining representations; physicists' generators $D(T_a) = i\,d(X_a)$ as in [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-6|Def. §C3.1.6]]): for $\mathfrak{su}(2)$ with $B(X, Y) = -2\operatorname{tr}(XY)$ on $2\times2$ matrices, $C_d = -\mathbf J^2$, so $C_d = -j(j+1)\mathbb 1$ on spin $j$; for $\mathfrak{so}(1,3)$ with $B(X, Y) = -\frac12\operatorname{tr}(XY)$ on $4\times4$ matrices (equivalently $B = \frac12\omega_{\mu\nu}\omega'^{\mu\nu}$ in the parameters of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]), $C_d = \mathbf K^2 - \mathbf J^2 = -2(\mathbf J_+^2 + \mathbf J_-^2)$, so $C_d = -2\bigl(j_+(j_+ + 1) + j_-(j_- + 1)\bigr)\mathbb 1$ on $(j_+, j_-)$ ([[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]]). (The Poincaré algebra has no nondegenerate invariant form; its Casimirs $P^2$ and $W^2$ are found by hand, [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-6|Theorem §C3.5.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-10|Theorem §C3.6.10]].)
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §18.3 (the quadratic Casimir element: basis independence, centrality) · Meinrenken, Lie Groups and Lie Algebras, Lemma 10.7 · normalizations of the examples computed here and checked against [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] (batch 2)*

^thm-cb-3-11

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes (2024), §18.3: "Let $a_i$ be a basis of $\mathfrak g$ and $a^i$ the dual basis under an invariant inner product … $C := \sum_ia_ia^i$. It is easy to show that $C$ is independent on the choice of the basis … Also $C$ is central: $[y, C] = \sum_i([y, a_i]a^i + a_i[y, a^i]) = 0$" (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); Steps 1–2 write out the two "easy" verifications, in a representation instead of the enveloping algebra. The examples (Steps 4–5) are computed here.*
>
> **Step 1** (the dual basis through the inverse matrix). Let $B_{ab} = B(X_a, X_b)$, invertible (nondegenerate) and symmetric, with inverse $B^{ab}$. Then $X^a = B^{ab}X_b$ (sum over $b$), since $B(X_c, B^{ab}X_b) = B^{ab}B_{cb} = \delta_c{}^a$. Hence $C_d = B^{ab}d(X_a)d(X_b)$.
>
> **Step 2** (part 1). Let $Y_i = P^a{}_iX_a$ be another basis, $P$ invertible. Then $B(Y_i, Y_j) = P^a{}_iP^b{}_jB_{ab}$, whose inverse is $(P^{-1})^i{}_c(P^{-1})^j{}_dB^{cd}$. So, by Step 1 for the new basis and linearity of $d$,
>
> $$
> \sum_{i,j}(P^{-1})^i{}_c(P^{-1})^j{}_dB^{cd}\,P^a{}_iP^b{}_j\,d(X_a)d(X_b) = \delta^a{}_c\,\delta^b{}_d\,B^{cd}\,d(X_a)d(X_b) = B^{ab}d(X_a)d(X_b) = C_d .
> $$
>
> **Step 3** (part 2: $C_d$ commutes with $d(Y)$). Every $Z \in \mathfrak g$ expands as $Z = \sum_bB(Z, X^b)X_b = \sum_bB(X_b, Z)X^b$ (pair with $X^c$, resp. $X_c$). Put $c_{ab} = B([Y, X_a], X^b)$, so $[Y, X_a] = \sum_bc_{ab}X_b$. By invariance ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]) $B(X_b, [Y, X^a]) = -B([Y, X_b], X^a) = -c_{ba}$, so $[Y, X^a] = -\sum_bc_{ba}X^b$. Then, with $[d(Y), PQ] = [d(Y), P]Q + P[d(Y), Q]$ and $d$ a homomorphism,
>
> $$
> [d(Y), C_d] = \sum_a\Bigl(d([Y, X_a])\,d(X^a) + d(X_a)\,d([Y, X^a])\Bigr) = \sum_{a,b}c_{ab}\,d(X_b)d(X^a) - \sum_{a,b}c_{ba}\,d(X_a)d(X^b) .
> $$
>
> Renaming $a \leftrightarrow b$ in the second sum turns it into the first: $[d(Y), C_d] = 0$. So $C_d$ is a Casimir operator ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11|Def. §C3.1.11]]).
>
> **Step 4** (part 3). By Step 3, $C_d$ commutes with every $d(Y)$; on a finite-dimensional irreducible representation it is a multiple of $\mathbb 1$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]], last sentence).
>
> **Step 5** (the $\mathfrak{su}(2)$ example). Basis $X_a = -\frac i2\sigma^a$. $B$ is symmetric, invariant (the trace is cyclic: $-2\operatorname{tr}([Z, X]Y + X[Z, Y]) = -2\operatorname{tr}(ZXY - XYZ) = 0$) and $B(X_a, X_b) = -2\operatorname{tr}\bigl(-\frac14\sigma^a\sigma^b\bigr) = \frac12\cdot2\delta_{ab} = \delta_{ab}$, using $\operatorname{tr}(\sigma^a\sigma^b) = 2\delta_{ab}$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). So $X^a = X_a$, and with $d(X_a) = -i\,D(T_a) = -iJ^a$ (physicists' generators, $T_a = \frac12\sigma^a$): $C_d = \sum_a(-iJ^a)^2 = -\mathbf J^2$, which is $-j(j+1)\mathbb 1$ on spin $j$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], 3).
>
> **Step 6** (the Lorentz example). For the generators $M^{\alpha\beta}$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], $(M^{\alpha\beta})^\mu{}_\nu = g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu$, multiplying out the four terms of the trace gives
>
> $$
> \operatorname{tr}(M^{\alpha\beta}M^{\gamma\delta}) = g^{\alpha\delta}g^{\gamma\beta} - g^{\alpha\gamma}g^{\delta\beta} - g^{\beta\delta}g^{\gamma\alpha} + g^{\beta\gamma}g^{\delta\alpha} = 2\bigl(g^{\alpha\delta}g^{\beta\gamma} - g^{\alpha\gamma}g^{\beta\delta}\bigr).
> $$
>
> For index pairs $\alpha < \beta$, $\gamma < \delta$ this vanishes unless $(\alpha, \beta) = (\gamma, \delta)$ ($g$ is diagonal), and then equals $-2g^{\alpha\alpha}g^{\beta\beta}$: $-2$ for a rotation pair ($g^{jj}g^{kk} = 1$), $+2$ for a boost pair ($g^{00}g^{ii} = -1$). With $B = -\frac12\operatorname{tr}$ and the basis $-iJ_i = M^{jk}$, $-iK_i = M^{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]): $B(-iJ_i, -iJ_j) = \delta_{ij}$, $B(-iK_i, -iK_j) = -\delta_{ij}$, mixed values $0$. ($B$ is invariant by the same trace argument as in Step 5, nondegenerate by this table.) Dual basis: $(-iJ_i)^\vee = -iJ_i$, $(-iK_i)^\vee = +iK_i$. So
>
> $$
> C_d = \sum_i\bigl(-iD(J_i)\bigr)^2 + \sum_i\bigl(-iD(K_i)\bigr)\bigl(iD(K_i)\bigr) = -\mathbf J^2 + \mathbf K^2 .
> $$
>
> In terms of $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$: $\mathbf J_+^2 + \mathbf J_-^2 = \frac14\bigl[(\mathbf J^2 + i(\mathbf J\cdot\mathbf K + \mathbf K\cdot\mathbf J) - \mathbf K^2) + (\mathbf J^2 - i(\mathbf J\cdot\mathbf K + \mathbf K\cdot\mathbf J) - \mathbf K^2)\bigr] = \frac12(\mathbf J^2 - \mathbf K^2)$, so $C_d = -2(\mathbf J_+^2 + \mathbf J_-^2)$, and on $(j_+, j_-)$, where $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ ([[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]]; [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]), $C_d = -2\bigl(j_+(j_+ + 1) + j_-(j_- + 1)\bigr)\mathbb 1$.
>
> **What the proof shows.**
> - The Casimir depends on the choice of invariant form; only its multiples are canonical. On $\mathfrak{so}(1,3)$ a second, independent invariant form ($\propto\varepsilon_{\mu\nu\rho\sigma}\omega^{\mu\nu}\omega'^{\rho\sigma}$) gives the second Casimir, proportional to $\mathbf J\cdot\mathbf K$, i.e. to $\mathbf J_+^2 - \mathbf J_-^2 = i\,\mathbf J\cdot\mathbf K$; the two together determine $(j_+, j_-)$.
> - ⚑ By-product (convention check, batch 2): the examples match the register of [[Larsen PHY 513]] ($\mathbf J^2 = j(j+1)$ with $[J^i, J^j] = i\varepsilon^{ijk}J^k$; $K_i = \mathcal J^{0i}$); with $K_i = \mathcal J^{i0}$ the result $\mathbf K^2 - \mathbf J^2$ is unchanged (quadratic in $\mathbf K$).

^pf-cb-3-11

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-3|Theorem §CB.3.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-11|Def. §C3.1.11]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]

## Compact groups: unitarity and complete reducibility

The course's statement for $SU(2)$ and $SO(3)$, proved in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]] by averaging over $S^3$:

![[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5]]

> [!theorem] Theorem §CB.3.12: Haar Measure on a Compact Group
> On every compact matrix Lie group $G$ there is a unique Borel probability measure $\mu$ invariant under left and right translations: $\int_Gf(hg)\,d\mu(g) = \int_Gf(gh)\,d\mu(g) = \int_Gf(g)\,d\mu(g)$ for every continuous $f$ and $h \in G$. For $SU(2) \cong S^3$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-5|591 Prop. §41.5]]) it is the normalized round measure of $S^3$.
>
> *Source: Lee, Introduction to Smooth Manifolds, Prop. 16.10 (existence of a left-invariant volume form) · Etingof, Lie Groups and Lie Algebras (MIT 18.755), §34.4, Prop. 34.8 (compact groups are unimodular), Thm. 37.1 (uniqueness) · cited in [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]] · Measure Theory (551) for the measure-theoretic background*

^thm-cb-3-12

> [!proof]- Proof
> *Source: J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Prop. 16.10 and its proof (the Haar volume form) for Steps 1–3 · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes (2024), §34.4 and Prop. 34.8 (right invariance: "the representation of G on $|\wedge^n\mathfrak g^\ast|$ defines a continuous homomorphism $\rho : G \to \mathbb R_+$. Since G is compact, the image … is a compact subgroup of $\mathbb R_+$ … the trivial group") for Step 4, and the last paragraph of the proof of Thm. 37.1 (a left-invariant and a right-invariant normalized integral agree) for Step 5 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf). Step 6 is the vault's [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-5|Derivation §C3.1.5]], step 1.*
>
> **Step 1** (a left-invariant volume form; Lee). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], $G$ is a Lie group of dimension $n = \dim\mathfrak g$. If $n = 0$, $G$ is discrete and compact, hence finite, and $\mu = \frac1{|G|}\times$counting measure works; let $n \ge 1$. Choose a basis $X_1, \dots, X_n$ of $\mathfrak g = T_{\mathbb 1}G$ and let $E_i$ be the left-invariant vector fields with $E_i(\mathbb 1) = X_i$ ([[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-3|591 Def. §50.3]]); they form a global frame. Let $\varepsilon^1, \dots, \varepsilon^n$ be the dual coframe. Then $(L_g^\ast\varepsilon^i)(E_j) = \varepsilon^i(L_{g\ast}E_j) = \varepsilon^i(E_j) = \delta^i{}_j$, so each $\varepsilon^i$, and hence $\omega = \varepsilon^1\wedge\cdots\wedge\varepsilon^n$, is left-invariant: $L_g^\ast\omega = \omega$. $\omega$ vanishes nowhere ($\omega(E_1, \dots, E_n) = 1$); orient $G$ so that $\omega$ is positive.
>
> **Step 2** (left-invariant forms are multiples of $\omega$; Lee). A left-invariant $n$-form $\tilde\omega$ satisfies $\tilde\omega_g = L_{g^{-1}}^\ast\tilde\omega_{\mathbb 1}$, and $\tilde\omega_{\mathbb 1} = c\,\omega_{\mathbb 1}$ for a real $c$ (the top exterior power of $T_{\mathbb 1}^\ast G$ is one-dimensional); so $\tilde\omega = c\,\omega$.
>
> **Step 3** (the measure and left invariance). $G$ is compact and oriented, so $\int_G\omega > 0$; put $\omega_G = \omega/\int_G\omega$ and $I(f) = \int_Gf\,\omega_G$ for continuous $f$. $I$ is linear, positive ($f \ge 0 \Rightarrow I(f) \ge 0$) and $I(1) = 1$; by the Riesz–Markov–Kakutani theorem (as recalled in Etingof, §37.1) it is integration against a unique Borel probability measure $\mu$. Left invariance: $L_h$ is a diffeomorphism with $L_h^\ast\omega_G = \omega_G$, hence orientation-preserving, so $\int_G(f\circ L_h)\,\omega_G = \int_GL_h^\ast(f\,\omega_G) = \int_Gf\,\omega_G$ (diffeomorphism invariance of the integral, Lee, Prop. 16.6).
>
> **Step 4** (right invariance; Etingof, Prop. 34.8). Left and right translations commute, $L_gR_h = R_hL_g$, so $R_h^\ast\omega_G$ is left-invariant and by Step 2 $R_h^\ast\omega_G = \chi(h)\,\omega_G$ with $\chi(h) \ne 0$ ($R_h$ is a diffeomorphism). From $R_{hk} = R_k\circ R_h$, $R_{hk}^\ast = R_h^\ast R_k^\ast$ and $\chi(hk) = \chi(h)\chi(k)$. $\chi$ is continuous ($\chi(h) = (R_h^\ast\omega_G)_{\mathbb 1}(X_1, \dots, X_n)/(\omega_G)_{\mathbb 1}(X_1, \dots, X_n)$, and $(R_h^\ast\omega_G)_{\mathbb 1}(X_1, \dots, X_n) = (\omega_G)_h(X_1h, \dots, X_nh)$ depends continuously on $h$). So $|\chi| : G \to (\mathbb R_{>0}, \cdot)$ is a continuous homomorphism and $|\chi|(G)$ is a compact subgroup of $\mathbb R_{>0}$. If it contained $t \ne 1$, it would contain $t^k$ for all $k \in \mathbb Z$, which is unbounded or accumulates at $0$: not compact. So $|\chi| = 1$, $\chi(h) = \pm1$. If $\chi(h) = 1$, $R_h$ preserves orientation and $\int(f\circ R_h)\,\omega_G = \int R_h^\ast(f\,\omega_G) = \int f\,\omega_G$. If $\chi(h) = -1$, $R_h$ reverses it and $\int R_h^\ast(f\,\omega_G) = -\int f\,\omega_G$, i.e. $-\int(f\circ R_h)\,\omega_G = -\int f\,\omega_G$. Either way $\int f(gh)\,d\mu(g) = \int f\,d\mu$.
>
> **Step 5** (uniqueness; Etingof, Thm. 37.1). Let $\mu'$ be another Borel probability measure that is left-invariant. For continuous $f$, $(g, h) \mapsto f(gh)$ is continuous and bounded on $G\times G$, so Fubini's theorem for the product of the two finite measures applies (the $\mathbb R^n$ case is [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]]):
>
> $$
> \int f\,d\mu = \int\Bigl(\int f(gh)\,d\mu(g)\Bigr)d\mu'(h) = \int\Bigl(\int f(gh)\,d\mu'(h)\Bigr)d\mu(g) = \int\Bigl(\int f\,d\mu'\Bigr)d\mu(g) = \int f\,d\mu',
> $$
>
> using right invariance of $\mu$ (Step 4) in the first equality and left invariance of $\mu'$ in the third. Integrals of all continuous functions determine a finite Borel measure on the compact metrizable $G$ (the uniqueness part of Riesz–Markov–Kakutani), so $\mu' = \mu$. In particular the measure is unique even among merely left-invariant ones.
>
> **Step 6** ($SU(2)$). The normalized round measure on $S^3 \cong SU(2)$ is invariant under left and right multiplication, which act on $\mathbb R^4$ by orthogonal maps ([[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-5|Derivation §C3.1.5]], step 1), and has total mass $1$; by Step 5 it is the Haar measure.
>
> **What the proof shows.**
> - ⚑ By-product: compactness enters twice: the total volume $\int_G\omega$ is finite (normalization), and the modular character $|\chi|$ must be trivial (right invariance). For a non-compact group such as $SO^+(1,3)$ an invariant measure exists but has infinite volume, so averaging (Theorem §CB.3.13) is impossible → [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-1|Example §C3.1.1]].
> - Used next: the averaged inner product (Theorem §CB.3.13), and the invariant integral on $SU(2)\times SU(2)$ in Weyl's trick (Theorem §CB.3.15).

^pf-cb-3-12

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-3|591 Def. §50.3]], [[§25 Invariance Properties and Fubini's Theorem#^thm-25-6|551 Thm. §25.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-5|Derivation §C3.1.5]]

> [!theorem] Theorem §CB.3.13: Representations of Compact Groups Are Unitary
> Every finite-dimensional representation $D$ of a compact matrix Lie group $G$ on $W$ is unitary ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]): if $\langle\cdot,\cdot\rangle_0$ is any inner product on $W$, then $\langle v, w\rangle = \int_G\langle D(g)v, D(g)w\rangle_0\,d\mu(g)$ (Haar, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-12|Theorem §CB.3.12]]) is an inner product for which every $D(g)$ is unitary, and the physicists' generators are Hermitian.
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Props. 5.16–5.17 and Exercise 3 · Etingof, Lie Groups and Lie Algebras (MIT 18.755), Prop. 35.1 · Smith, Groups and their Representations, Ch. 3 §8 (the finite-group averaging)*

^thm-cb-3-13

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5, Prop. 5.17 and its proof (averaging an inner product with Haar measure; Prop. 5.16 is the finite-group sum, as in K. E. Smith, Groups and their Representations, Ch. 3 §8) (https://arxiv.org/abs/math-ph/0005032) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Prop. 35.1 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf). The Hermitian generators (Step 4) are Hall's Exercise 3 of Ch. 5, done as in [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-5|Derivation §C3.1.5]], step 4.*
>
> **Step 1** (well defined). $D$ is continuous, so $g \mapsto \langle D(g)v, D(g)w\rangle_0$ is a continuous function on the compact $G$, and its integral against the probability measure $\mu$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-12|Theorem §CB.3.12]]) exists. ⚑ By-product: this is the only place compactness is used (a finite invariant measure).
>
> **Step 2** (an inner product). $\langle v, w\rangle$ is sesquilinear and Hermitian-symmetric because $\langle\cdot,\cdot\rangle_0$ is and the integral is linear. For $v \ne 0$, $g \mapsto \|D(g)v\|_0^2$ is continuous and positive ($D(g)$ is invertible), so it has a positive minimum $m$ on the compact $G$, and $\langle v, v\rangle \ge m\,\mu(G) = m > 0$.
>
> **Step 3** (invariance). For $h \in G$, using $D(g)D(h) = D(gh)$ and then right invariance of $\mu$ (Theorem §CB.3.12) with $F(g) = \langle D(g)v, D(g)w\rangle_0$:
>
> $$
> \langle D(h)v, D(h)w\rangle = \int_G\langle D(gh)v, D(gh)w\rangle_0\,d\mu(g) = \int_GF(gh)\,d\mu(g) = \int_GF(g)\,d\mu(g) = \langle v, w\rangle .
> $$
>
> So every $D(h)$ is unitary for $\langle\cdot,\cdot\rangle$, and $D$ is unitary ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]).
>
> **Step 4** (Hermitian generators). For $X \in \mathfrak g$, $D(e^{sX}) = e^{s\,d(X)}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]] with $H = GL(W)$) is unitary for every real $s$: $\langle e^{s\,d(X)}v, e^{s\,d(X)}w\rangle = \langle v, w\rangle$. Differentiating at $s = 0$ (product rule) gives $\langle d(X)v, w\rangle + \langle v, d(X)w\rangle = 0$: $d(X)^\dagger = -d(X)$. Hence $D(T_a) = i\,d(X_a)$ satisfies $D(T_a)^\dagger = -i\,d(X_a)^\dagger = i\,d(X_a) = D(T_a)$.
>
> **What the proof shows.**
> - Unitarity of a finite-dimensional representation of a compact group is a theorem, not an assumption; the generators of rotations are Hermitian for this reason.
> - The new inner product depends on the starting $\langle\cdot,\cdot\rangle_0$; on an irreducible representation it is unique up to a positive factor (two invariant inner products differ by an intertwiner, Theorem §CB.3.3).

^pf-cb-3-13

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-12|Theorem §CB.3.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]

> [!theorem] Theorem §CB.3.14: Unitary Representations Are Completely Reducible
> If a finite-dimensional representation (of a group, a Lie algebra or an associative algebra closed under adjoints) is unitary for an inner product, then the orthogonal complement of an invariant subspace is invariant, and the representation is an orthogonal direct sum of irreducible ones: completely reducible ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]]). Hence every finite-dimensional representation of a compact matrix Lie group is completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-13|Theorem §CB.3.13]]).
>
> *Source: Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §5, Props. 5.14, 5.15, 5.17 · Smith, Groups and their Representations, Ch. 3 §8 (Thms. 8.1, 8.2) · Etingof, Lie Groups and Lie Algebras (MIT 18.755), Cor. 35.2*

^thm-cb-3-14

> [!proof]- Proof
> *Source: B. C. Hall, An Elementary Introduction to Groups and Representations, Ch. 5 §5, Prop. 5.15 (the complement $U^\perp$ is invariant) and Prop. 5.14 (induction on dimension), with proofs (https://arxiv.org/abs/math-ph/0005032) · K. E. Smith, Groups and their Representations, Ch. 3 §8, Thms. 8.1–8.2 (the same induction, with an averaged projection instead of an inner product) · P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, Cor. 35.2 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf). The Lie-algebra and associative-algebra cases of Step 1 are the same computation with the adjoint in place of the inverse.*
>
> **Step 1** (the orthogonal complement is invariant; Hall, Prop. 5.15). Let $U \subset W$ be invariant and $w \in U^\perp$, $u \in U$.
> - *Group*, $D(g)$ unitary: $\langle u, D(g)w\rangle = \langle D(g)^\dagger u, w\rangle = \langle D(g^{-1})u, w\rangle = 0$, since $D(g)^\dagger = D(g)^{-1} = D(g^{-1})$ and $D(g^{-1})u \in U$.
> - *Lie algebra*, $D(T_a)$ Hermitian, i.e. $d(X)^\dagger = -d(X)$: $\langle u, d(X)w\rangle = \langle d(X)^\dagger u, w\rangle = -\langle d(X)u, w\rangle = 0$.
> - *Associative algebra* with $\gamma(a)^\dagger = \gamma(a')$ for some $a' \in A$: $\langle u, \gamma(a)w\rangle = \langle\gamma(a')u, w\rangle = 0$.
>
> In each case $U^\perp$ is invariant.
>
> **Step 2** (splitting). $W = U \oplus U^\perp$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]), both summands invariant (Step 1), and each with the restricted inner product is again unitary. In a basis adapted to $U \oplus U^\perp$ every represented operator is block diagonal: the representation is equivalent to the direct sum of its restrictions ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]]).
>
> **Step 3** (induction on dimension; Hall, Prop. 5.14). If $\dim W = 1$, $W$ is irreducible. Suppose the claim holds below dimension $n$ and $\dim W = n$. If $W$ is irreducible, it is a direct sum with one summand. Otherwise there is an invariant $U$ with $0 \ne U \ne W$; by Step 2, $W = U \oplus U^\perp$ with $\dim U, \dim U^\perp < n$, both unitary, so each is an orthogonal direct sum of irreducible invariant subspaces, and so is $W$.
>
> **Step 4** (compact groups). By [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-13|Theorem §CB.3.13]] every finite-dimensional representation of a compact matrix Lie group is unitary for some inner product; Steps 1–3 apply.
>
> **What the proof shows.**
> - An invariant inner product is a machine for producing invariant complements; without it complements may not exist (the Galilean boosts of [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-1|Example §C3.1.1]]).
> - The pieces are orthogonal; for the Lorentz algebra the complete reducibility comes instead from the compact real form (Theorem §CB.3.15), and the pieces are orthogonal only for an inner product that makes boosts non-unitary.

^pf-cb-3-14

*Uses:* [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-13|Theorem §CB.3.13]], [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]

What fails without compactness, worked out in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-1]]

## Weyl's unitary trick

> [!theorem] Theorem §CB.3.15: Weyl's Unitary Trick
> Let $\mathfrak g$ be a real Lie algebra and $K$ a compact, simply connected matrix Lie group whose Lie algebra $\mathfrak k$ and $\mathfrak g$ are real forms of the same complex Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-10|Def. §CB.2.10]]). Then every finite-dimensional representation of $\mathfrak g$ on a complex space is completely reducible. In particular this holds for $\mathfrak g = \mathfrak{so}(1,3)$ and for $\mathfrak g = \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, with $K = SU(2)\times SU(2)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]), and for $\mathfrak{su}(2)$ and $\mathfrak{sl}(2, \mathbb C)$ with $K = SU(2)$.
>
> *Source: Etingof, Lie Groups and Lie Algebras (MIT 18.755), §35.1 after Cor. 35.2 ("Weyl's unitary trick", for $\mathfrak{sl}_n$ via $SU(n)$) · the Lorentz case written in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], Derivation, steps 1–5*

^thm-cb-3-15

> [!proof]- Proof
> *Source: P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, §35.1, the paragraph after Cor. 35.2: representations of the simply connected compact $SU(n)$ are the same as representations of $\mathfrak{su}(n)$ or of its complexification $\mathfrak{sl}_n$, so the compact-group theorem gives complete reducibility for $\mathfrak{sl}_n$ ("Weyl's unitary trick") (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf) · the vault's [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^der-c3-3-2|Derivation §C3.3.2]], steps 1–5, for the Lorentz case, generalized here. Step 2 uses the Lie correspondence, Theorem §CB.1.24, whose proof is still a placeholder (SPEC-CB decision 7); this proof is complete relative to it.*
>
> **Step 1** (move the representation to $\mathfrak k$). Let $d$ be a representation of $\mathfrak g$ on a finite-dimensional complex $W$. $\mathfrak g$ and $\mathfrak k$ are real forms of one complex algebra $\mathfrak h$, so by [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-20|Theorem §CB.2.20]] there is a representation $d_{\mathfrak k}$ of $\mathfrak k$ on the same $W$ (extend $d$ complex-linearly to $\mathfrak h$, restrict to $\mathfrak k$) with exactly the same invariant subspaces.
>
> **Step 2** (integrate to $K$). $K$ is simply connected, so by [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]] (with $H = GL(W)$) there is a representation $D$ of $K$ on $W$ with $D_\ast = d_{\mathfrak k}$, i.e. $D(e^X) = e^{d_{\mathfrak k}(X)}$.
>
> **Step 3** (complete reducibility for $K$). $K$ is compact, so $W = W_1\oplus\cdots\oplus W_r$ with each $W_i$ invariant and irreducible under $D$ ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-14|Theorem §CB.3.14]]).
>
> **Step 4** (back to $\mathfrak k$). $K$ is connected (simply connected includes connected), so a subspace is invariant under all $D(k)$ iff it is invariant under all $d_{\mathfrak k}(X)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 2). So the $W_i$ are invariant and irreducible under $d_{\mathfrak k}$.
>
> **Step 5** (back to $\mathfrak g$). By Step 1, the $W_i$ are invariant and irreducible under $d$: $d$ is completely reducible ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-9|Def. §C3.1.9]]).
>
> **Step 6** (the instances). $K = SU(2)\times SU(2)$, realized as block-diagonal matrices in $GL(4, \mathbb C)$, is closed, compact (a product of compact sets) and simply connected ($SU(2) \cong S^3$ is, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], and $\pi_1$ of a product is the product, [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]). Its Lie algebra is $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ (block-diagonal exponentials $e^{s(X\oplus Y)} = e^{sX}\oplus e^{sY}$, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]), a real form of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ (componentwise [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-15|Theorem §CB.2.15]]: the fixed set of $(X, Y) \mapsto (-X^\dagger, -Y^\dagger)$). $\mathfrak{so}(1,3)$ is a real form of the same algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], 1), and $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]), an isomorphism carrying representations and their invariant subspaces along. For $\mathfrak{su}(2)$ take $K = SU(2)$ itself ($\mathfrak g = \mathfrak k$); complex-linear representations of $\mathfrak{sl}(2, \mathbb C) = \mathfrak{su}(2)_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]]) are those of $\mathfrak{su}(2)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]).
>
> **What the proof shows.**
> - ⚑ By-product: complete reducibility of non-unitary representations (Lorentz) is borrowed from a compact group with the same complexified algebra; unitarity is *not* borrowed: the boosts stay non-unitary ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-16|Theorem §CB.3.16]]).
> - The single input not proved in CB is the Lie correspondence (Step 2), quoted in the same way in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^der-c3-3-2|Derivation §C3.3.2]], step 2.

^pf-cb-3-15

*Uses:* [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-20|Theorem §CB.2.20]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-14|Theorem §CB.3.14]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-15|Theorem §CB.2.15]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]

The Lorentz case, stated in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]; its proof is the trick above:

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2]]

## Noncompact simple algebras have no finite-dimensional unitary representations

> [!theorem] Theorem §CB.3.16: No Nontrivial Finite-Dimensional Unitary Representation of a Noncompact Simple Algebra
> Let $\mathfrak g$ be a real simple Lie algebra ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-9|Def. §CB.2.9]]) that has no positive-definite invariant inner product ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]). Then every finite-dimensional unitary representation of $\mathfrak g$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]) is zero. $\mathfrak{so}(1,3)$ satisfies the hypothesis: $\mathrm{ad}$ of a boost generator has nonzero real eigenvalues, impossible for an operator that is skew for an inner product.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Principle "Hermitian generators do not make boosts unitary", citing Weinberg vol. 1 ch. 2; statement) · the trace-form argument written here (cf. Etingof, Lie Groups and Lie Algebras, MIT 18.755, Lemma 18.6, which uses the same form $\operatorname{Tr}_V(xy)$)*

^thm-cb-3-16

> [!proof]- Proof
> *Written here, along the route recorded in batch 1. The form $B_V(x, y) = \operatorname{Tr}|_V(xy)$ of a representation and the fact that its kernel is an ideal are used the same way in P. Etingof, Lie Groups and Lie Algebras, MIT 18.755 notes, proof of Lemma 18.6 (https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf); the user's notes (Ch. 7 §7.3) state the result and cite Weinberg. The Lorentz group version, by eigenvalues, is [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]].*
>
> **Step 1** (unitary means anti-Hermitian). A unitary representation has $D(T_a) = i\,d(X_a)$ Hermitian ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]]), i.e. $d(X_a)^\dagger = -d(X_a)$, and by real linearity $d(X)^\dagger = -d(X)$ for all $X \in \mathfrak g$.
>
> **Step 2** (the kernel is an ideal). If $d(A) = 0$, then $d([X, A]) = [d(X), d(A)] = 0$ for every $X$: $\ker d$ is an ideal ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]]). $\mathfrak g$ is simple, so $\ker d = \mathfrak g$ (then $d = 0$, the claim) or $\ker d = 0$.
>
> **Step 3** (a faithful unitary representation gives an invariant inner product). Suppose $\ker d = 0$ and put $B(X, Y) = -\operatorname{tr}(d(X)d(Y))$. It is real: $\overline{\operatorname{tr}(d(X)d(Y))} = \operatorname{tr}\bigl((d(X)d(Y))^\dagger\bigr) = \operatorname{tr}(d(Y)^\dagger d(X)^\dagger) = \operatorname{tr}(d(Y)d(X)) = \operatorname{tr}(d(X)d(Y))$. It is symmetric (cyclicity of the trace) and bilinear. It is positive definite: $B(X, X) = -\operatorname{tr}(d(X)^2) = \operatorname{tr}(d(X)^\dagger d(X)) = \sum_{ij}|d(X)_{ij}|^2 > 0$ for $X \ne 0$, since $d$ is injective. It is invariant ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]]): with $d([Z, X]) = [d(Z), d(X)]$,
>
> $$
> B([Z, X], Y) + B(X, [Z, Y]) = -\operatorname{tr}\bigl(d(Z)d(X)d(Y) - d(X)d(Z)d(Y) + d(X)d(Z)d(Y) - d(X)d(Y)d(Z)\bigr) = -\operatorname{tr}\bigl(d(Z)d(X)d(Y)\bigr) + \operatorname{tr}\bigl(d(X)d(Y)d(Z)\bigr) = 0 .
> $$
>
> This contradicts the hypothesis, so $\ker d = \mathfrak g$ and $d = 0$.
>
> **Step 4** ($\mathfrak{so}(1,3)$ is simple). [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]], 3.
>
> **Step 5** (a skew operator has no nonzero real eigenvalue). If $B$ is a positive-definite invariant form and $\mathrm{ad}_ZX = \lambda X$ with $\lambda$ real, $X \ne 0$, then $\lambda B(X, X) = B([Z, X], X) = -B(X, [Z, X]) = -\lambda B(X, X)$, so $\lambda = 0$.
>
> **Step 6** (a boost has real eigenvalues $\pm1$). With $u = -iK_1$, $v = -iJ_2$, $Z = -iK_3$ in $\mathfrak{so}(1,3)$ and the brackets $[K_i, K_j] = -i\varepsilon_{ijk}J_k$, $[K_i, J_j] = i\varepsilon_{ijk}K_k$ (Step 1 of the proof of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]]):
>
> $$
> \mathrm{ad}_Zu = -[K_3, K_1] = -(-i\varepsilon_{312}J_2) = iJ_2 = -v, \qquad \mathrm{ad}_Zv = -[K_3, J_2] = -i\varepsilon_{321}K_1 = iK_1 = -u .
> $$
>
> So $\mathrm{ad}_Z(u - v) = u - v$ and $\mathrm{ad}_Z(u + v) = -(u + v)$: real eigenvalues $\pm1$. By Step 5, $\mathfrak{so}(1,3)$ has no positive-definite invariant inner product, and Steps 1–3 apply.
>
> **What the proof shows.**
> - ⚑ By-product: for the Lorentz algebra every finite-dimensional representation in which all six generators are Hermitian is zero; physically, field-index representations are never unitary, and unitary representations on states are infinite-dimensional → [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]].
> - Simplicity is used only in Step 2, to exclude a kernel that is a proper nonzero ideal; for a non-simple algebra a unitary representation can be nonzero on one ideal and vanish on another.

^pf-cb-3-16

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-10|Def. §C3.1.10]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-7|Def. §CB.2.7]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-10|Def. §CB.3.10]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-14|Theorem §CB.2.14]]

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
> *Source: written here · the field laws: [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]*

^thm-cb-3-17

> [!proof]- Proof
> Each $D(g)$ is linear in $f$. For $g, h \in G$ and every $x$: $(D(g)D(h)f)(x) = S(g)\,(D(h)f)(g^{-1}x) = S(g)S(h)\,f(h^{-1}g^{-1}x) = S(gh)\,f((gh)^{-1}x) = (D(gh)f)(x)$, using $(gh)^{-1} = h^{-1}g^{-1}$ and that $S$ is a homomorphism. $D(\mathbb 1) = \mathbb 1$ because $\mathbb 1x = x$ and $S(\mathbb 1) = \mathbb 1$. The inverse $g^{-1}$ in the argument is what makes the order come out right; $f(gx)$ would give an anti-homomorphism. The first formula is the case $S \equiv \mathbb 1$.

^pf-cb-3-17

> [!remark]- Connections
> - Theorem §CB.3.16 and Theorem §CB.3.13 are the two halves of [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]]: field indices carry finite-dimensional, non-unitary representations; states carry unitary, infinite-dimensional ones.
> - Theorem §CB.3.9 (Burnside) is what makes Clifford modules rigid: an irreducible Clifford module sees all of $\operatorname{End}(W)$, which is Pauli's theorem in disguise (§CB.8).
> - **Used in**: Definition §CB.3.1 — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-13|Theorem §C5a.1.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]]; Theorem §CB.3.3 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4|Theorem §C3.1.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-6|Theorem §C3.5.6]]; Theorem §CB.3.4 — [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]; Theorems §CB.3.8–§CB.3.9 — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]; Theorem §CB.3.11 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-4|Theorem §C3.1.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]; Theorems §CB.3.12–§CB.3.14 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]; Theorem §CB.3.15 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]; Theorem §CB.3.16 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]; Theorem §CB.3.17 — [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-3|Theorem §C3.4.3]].
