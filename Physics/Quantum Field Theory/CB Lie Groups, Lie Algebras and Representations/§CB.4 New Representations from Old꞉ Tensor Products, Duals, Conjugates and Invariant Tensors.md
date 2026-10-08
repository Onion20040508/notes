---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): Linear Algebra (LADR) §12 (duality), §36 (alternating forms), §38 (tensor products) · the user's PHY 513 notes, Ch. 1 §1.5, Ch. 7 §7.4.5, Ch. 8 §8.2–§8.3 · Yu Zhao-Huan, 量子场论讲义, §3.2, Exercise 3.7 · Peskin & Schroeder, §3.2, §3.4 · P. Woit, Quantum Theory, Groups and Representations, §§9.4–9.6 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the rest written here.*

How are new representations made from given ones, and what are index slots, dotted indices and invariant symbols in that language? The course has tensors as multilinear maps, index slots and the slot rule ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-4|Def. §C1a.5.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1|Def. §C3.1.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]]); the Math vault has duals and tensor products of vector spaces ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]], [[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]). This section makes each operation on spaces an operation on representations — tensor product, outer tensor product, dual, complex conjugate, $\operatorname{Hom}$, symmetric and exterior powers — and identifies the invariant tensors ($g$, $\varepsilon^{\mu\nu\rho\sigma}$, $\varepsilon_{ab}$) as intertwiners. It builds on [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]] (the conjugation of $\mathfrak g_{\mathbb C}$) and [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]] (Burnside, Schur).

## Recalled: duals, tensors and index slots

The dual space and tensors as multilinear maps, defined in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]; the tensor product of two spaces, defined in LADR:

![[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-3]]

![[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-4]]

![[§38 Tensor Products#^ladr-9-71]]

Index slots, the course's bookkeeping of which representation acts on which index, defined in [[§C3.1 Groups, Algebras and Representations of Rotations|§C3.1]]:

![[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1]]

## Tensor products

> [!definition] Definition §CB.4.1: Tensor Product of Group Representations
> If $D_1$, $D_2$ are representations of a group $G$ on $W_1$, $W_2$, their **tensor product** is the representation of $G$ on $W_1\otimes W_2$ ([[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]) with $(D_1\otimes D_2)(g)(w_1\otimes w_2) = D_1(g)w_1\otimes D_2(g)w_2$.
>
> *Source (planned): Woit, §9.4 · the user's PHY 513 notes, Ch. 7 §7.4.5*

^def-cb-4-1

> [!definition] Definition §CB.4.2: Tensor Product of Lie Algebra Representations
> If $d_1$, $d_2$ are representations of a Lie algebra $\mathfrak g$ on $W_1$, $W_2$, their **tensor product** is $(d_1\otimes d_2)(X) = d_1(X)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X)$ on $W_1\otimes W_2$.
>
> *Source (planned): Woit, §9.4*

^def-cb-4-2

> [!theorem] Theorem §CB.4.3: The Differential of a Tensor Product Is the Leibniz Rule
> 1. Definitions §CB.4.1 and §CB.4.2 give representations.
> 2. If $d_i$ is the differential of $D_i$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]), then $d_1\otimes d_2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-2|Def. §CB.4.2]]) is the differential of $D_1\otimes D_2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]); equivalently $e^{d_1(X)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X)} = e^{d_1(X)}\otimes e^{d_2(X)}$. In physicists' form, generators add: $D(T_a) = D_1(T_a)\otimes\mathbb 1 + \mathbb 1\otimes D_2(T_a)$.
>
> *Source (planned): Woit, §9.4 · the tensor law: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]]*

^thm-cb-4-3

> [!proof]- Proof (to be filled)
> *To be written in batch 4 ($d_1(X)\otimes\mathbb 1$ and $\mathbb 1\otimes d_2(X)$ commute, Theorem §CB.1.2, 3).*

^pf-cb-4-3

> [!definition] Definition §CB.4.4: Outer Tensor Product
> If $D_1$ is a representation of $G_1$ on $W_1$ and $D_2$ one of $G_2$ on $W_2$, their **outer tensor product** $D_1\boxtimes D_2$ is the representation of $G_1\times G_2$ on $W_1\otimes W_2$ with $(g_1, g_2) \mapsto D_1(g_1)\otimes D_2(g_2)$; for Lie algebras, $\mathfrak g_1\oplus\mathfrak g_2$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-8|Def. §CB.2.8]]) acts by $(X_1, X_2) \mapsto d_1(X_1)\otimes\mathbb 1 + \mathbb 1\otimes d_2(X_2)$.
>
> *Source (planned): written here*

^def-cb-4-4

> [!theorem] Theorem §CB.4.5: Irreducible Representations of a Direct Sum Are Outer Tensor Products
> Let $\mathfrak h_1$, $\mathfrak h_2$ be complex Lie algebras and consider finite-dimensional complex-linear representations.
> 1. If $W_1$, $W_2$ are irreducible representations of $\mathfrak h_1$, $\mathfrak h_2$, then $W_1\boxtimes W_2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-4|Def. §CB.4.4]]) is an irreducible representation of $\mathfrak h_1\oplus\mathfrak h_2$.
> 2. Every irreducible representation of $\mathfrak h_1\oplus\mathfrak h_2$ is equivalent to such a $W_1\boxtimes W_2$, with $W_1$, $W_2$ unique up to equivalence.
>
> The same holds for real Lie algebras and their representations on complex spaces, and for groups $G_1\times G_2$.
>
> *Source (planned): written here (via Burnside's theorem, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-9|Theorem §CB.3.9]]) · the Lorentz case: [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]*

^thm-cb-4-5

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-4-5

## Duals and complex conjugates

> [!definition] Definition §CB.4.6: Dual Representation
> The **dual** (contragredient) of a representation $D$ on $W$ is the representation $D^\ast$ on the dual space $W'$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]) with $D^\ast(g) = D(g^{-1})'$, the dual map ([[§12 Duality#^ladr-3-118|LADR Def. 3.118]]) of $D(g^{-1})$: $(D^\ast(g)\varphi)(w) = \varphi(D(g^{-1})w)$. For a Lie algebra, $d^\ast(X) = -d(X)'$. In a basis and its dual basis the matrices are $(D(g)^{-1})^{\mathsf T}$ and $-d(X)^{\mathsf T}$.
>
> *Source (planned): Woit, §4.2, §9.5 · written here*

^def-cb-4-6

> [!definition] Definition §CB.4.7: Complex-Conjugate Representation
> The **complex conjugate** $\bar W$ of a complex vector space $W$ is the set $W$ with the same addition and scalar multiplication $\lambda\cdot_{\bar W}w = \bar\lambda w$. The **complex-conjugate representation** of a representation $D$ on $W$ is $\bar D(g) = D(g)$ regarded as a map of $\bar W$; for a Lie algebra (real, [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]), $\bar d(X) = d(X)$ on $\bar W$. In a basis the matrices are $\overline{D(g)}$ and $\overline{d(X)}$ (entrywise conjugates).
>
> *Source (planned): written here*

^def-cb-4-7

> [!theorem] Theorem §CB.4.8: Conjugation of a Representation Is Conjugation of the Algebra
> Let $d$ be a representation of a real Lie algebra $\mathfrak g$ on $W$, $d_{\mathbb C}$ its complex-linear extension ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]]) and $c$ the conjugation of $\mathfrak g_{\mathbb C}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-3|Theorem §CB.2.3]]). Then the complex-linear extension of $\bar d$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-7|Def. §CB.4.7]]) is
>
> $$
> (\bar d)_{\mathbb C}(Z) = d_{\mathbb C}(cZ) \quad \text{as maps of the set } W, \qquad Z \in \mathfrak g_{\mathbb C} .
> $$
>
> Consequences: for $\mathfrak{so}(1,3)$, whose conjugation exchanges $\mathfrak a_\pm$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], 3), the conjugate representation exchanges the roles of $\mathbf J_+$ and $\mathbf J_-$; for $\mathfrak{su}(2)$ it maps each $\mathfrak{sl}(2, \mathbb C)$-representation to one with the same Casimir.
>
> *Source (planned): written here · the Lorentz case: [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]]*

^thm-cb-4-8

> [!proof]- Proof (to be filled)
> *To be written in batch 4 (on $\bar W$, $i$ acts as $-i$ on $W$: $(\bar d)_{\mathbb C}(X + iY) = d(X) - i\,d(Y) = d_{\mathbb C}(X - iY)$).*

^pf-cb-4-8

## Hom spaces, invariants and powers

> [!theorem] Theorem §CB.4.9: Hom(V, W) ≅ V* ⊗ W, and Its Invariants Are the Intertwiners
> For representations $D_V$, $D_W$ of $G$, $g\cdot T = D_W(g)\,T\,D_V(g)^{-1}$ is a representation on $\operatorname{Hom}(V, W)$; the linear isomorphism $V'\otimes W \to \operatorname{Hom}(V, W)$, $\varphi\otimes w \mapsto (v \mapsto \varphi(v)w)$, is an equivalence with $D_V^\ast\otimes D_W$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-6|Def. §CB.4.6]]); and $T$ is fixed by every $g$ iff $T$ is an intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]). The Lie algebra version: $X\cdot T = d_W(X)T - T\,d_V(X)$.
>
> *Source (planned): written here · the slot rule: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]]*

^thm-cb-4-9

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-4-9

The course's slot rule, the component form of this theorem, proved in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]:

![[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3]]

> [!definition] Definition §CB.4.10: Invariant Tensor
> An **invariant tensor** of a representation $D$ on a tensor space $\mathcal T$ (a tensor product of copies of $W$, $W'$, $\bar W$, $\bar W'$) is a $t \in \mathcal T$ with $D(g)t = t$ for all $g$; for a Lie algebra, $d(X)t = 0$ for all $X$. By [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-9|Theorem §CB.4.9]], an invariant tensor in $V'\otimes W$ is the same thing as an intertwiner $V \to W$.
>
> *Source (planned): written here*

^def-cb-4-10

> [!definition] Definition §CB.4.11: Symmetric Power
> The **$k$-th symmetric power** $\operatorname{Sym}^kW \subset W^{\otimes k}$ is the subspace of tensors fixed by every permutation of the $k$ factors.
>
> *Source (planned): Woit, §9.6 · written here*

^def-cb-4-11

> [!definition] Definition §CB.4.12: Exterior Power
> The **$k$-th exterior power** $\Lambda^kW \subset W^{\otimes k}$ is the subspace of tensors $t$ with $\pi t = \operatorname{sgn}(\pi)\,t$ for every permutation $\pi$ of the $k$ factors ([[§36 Alternating Multilinear Forms#^ladr-9-32|LADR Def. 9.32]] for the sign); $w_1\wedge\cdots\wedge w_k = \frac1{k!}\sum_\pi\operatorname{sgn}(\pi)\,w_{\pi(1)}\otimes\cdots\otimes w_{\pi(k)}$. The **exterior algebra** is $\Lambda W = \bigoplus_{k=0}^{\dim W}\Lambda^kW$ with the product $\wedge$.
>
> *Source (planned): Woit, §9.6 · LADR §36 (alternating forms, the dual picture) · written here*

^def-cb-4-12

> [!theorem] Theorem §CB.4.13: Symmetric and Exterior Powers Are Subrepresentations
> 1. $\operatorname{Sym}^kW$ and $\Lambda^kW$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-11|Def. §CB.4.11]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]]) are invariant under $D^{\otimes k}$; $\dim\operatorname{Sym}^kW = \binom{n + k - 1}{k}$, $\dim\Lambda^kW = \binom nk$ for $\dim W = n$.
> 2. $W\otimes W = \operatorname{Sym}^2W\oplus\Lambda^2W$ as representations.
> 3. For representations $A$ of $G_1$ and $B$ of $G_2$: $\Lambda^2(A\otimes B) \cong (\operatorname{Sym}^2A\boxtimes\Lambda^2B)\oplus(\Lambda^2A\boxtimes\operatorname{Sym}^2B)$ and $\operatorname{Sym}^2(A\otimes B) \cong (\operatorname{Sym}^2A\boxtimes\operatorname{Sym}^2B)\oplus(\Lambda^2A\boxtimes\Lambda^2B)$ as representations of $G_1\times G_2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-4|Def. §CB.4.4]]).
>
> *Source (planned): written here · the two-index case: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]]*

^thm-cb-4-13

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-4-13

## Invariant tensors of the Lorentz group and of SL(2,ℂ)

> [!theorem] Theorem §CB.4.14: The Metric and the Levi-Civita Symbol Are Invariant Tensors
> 1. $g_{\mu\nu} \in (V')^{\otimes2}$ and $g^{\mu\nu} \in V^{\otimes2}$ ($V = \mathbb R^{1,3}$) are invariant tensors ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-10|Def. §CB.4.10]]) of $O(1,3)$; equivalently $g : V \to V'$ is an intertwiner, so $V \cong V^\ast$ as representations.
> 2. $\varepsilon^{\mu\nu\rho\sigma} \in \Lambda^4V$ satisfies $\Lambda\cdot\varepsilon = (\det\Lambda)\,\varepsilon$: it is invariant under $SO(1,3)$ and changes sign under $\mathcal P$ and $\mathcal T$.
>
> *Source (planned): the user's PHY 513 notes, Ch. 1 §1.5 · [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]]*

^thm-cb-4-14

> [!proof]- Proof (to be filled)
> *To be written in batch 4 (part 1 is the definition of $O(1,3)$; part 2 from [[§37 Determinants|LADR §37]] via Theorem §C1a.5.5).*

^pf-cb-4-14

> [!theorem] Theorem §CB.4.15: ε on ℂ² and SL(2,ℂ) = Sp(2,ℂ)
> Let $\varepsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$, the alternating form $\varepsilon(u, v) = u^{\mathsf T}\varepsilon v$ on $\mathbb C^2$.
> 1. $A^{\mathsf T}\varepsilon A = (\det A)\,\varepsilon$ for every $A \in M_2(\mathbb C)$; so $SL(2, \mathbb C) = \{A : A^{\mathsf T}\varepsilon A = \varepsilon\} = Sp(2, \mathbb C)$, and $\Lambda^2\mathbb C^2$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-12|Def. §CB.4.12]]) is the representation $A \mapsto \det A$, trivial on $SL(2, \mathbb C)$.
> 2. $\varepsilon : \mathbb C^2 \to (\mathbb C^2)'$ is an intertwiner from the defining representation of $SL(2, \mathbb C)$ to its dual ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-6|Def. §CB.4.6]]): $(A^{-1})^{\mathsf T} = \varepsilon A\varepsilon^{-1}$.
> 3. For $A \in SU(2)$, $\bar A = (A^{-1})^{\mathsf T} = \varepsilon A\varepsilon^{-1}$: the defining representation of $SU(2)$ is equivalent to its dual and to its conjugate ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-7|Def. §CB.4.7]]).
>
> *Source (planned): the user's PHY 513 notes, Ch. 8 §8.2 · Yu, Exercise 3.7 · written here*

^thm-cb-4-15

> [!proof]- Proof (to be filled)
> *To be written in batch 4 (part 1: both sides are alternating in the columns of $A$, so proportional, compare at $A = \mathbb 1$; [[§37 Determinants|LADR §37]]).*

^pf-cb-4-15

> [!theorem] Theorem §CB.4.16: The Four Two-Dimensional Representations of SL(2,ℂ)
> On $\mathbb C^2$ the matrices $A$, $(A^{-1})^{\mathsf T}$, $\bar A$ and $(A^\dagger)^{-1}$ ($A \in SL(2, \mathbb C)$) give the defining representation, its dual, its conjugate and the dual of the conjugate. They fall into exactly two equivalence classes: $A \cong (A^{-1})^{\mathsf T}$ and $\bar A \cong (A^\dagger)^{-1}$, both via $\varepsilon$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]]); $A \not\cong \bar A$, since $\operatorname{tr}A \ne \operatorname{tr}\bar A$ for $A = \operatorname{diag}(2i, -\frac i2)$. In index language: undotted indices carry $A$, dotted indices carry $\bar A$, and $\varepsilon$ raises and lowers each kind without mixing them.
>
> *Source (planned): the user's PHY 513 notes, Ch. 8 §8.2 · Peskin & Schroeder, §3.2 · written here*

^thm-cb-4-16

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-4-16

The course's dotted and undotted indices and the invariant pairings, in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], are the component form of Theorems §CB.4.15–§CB.4.16:

![[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5]]

> [!remark]- Connections
> - Theorem §CB.4.8 is why complex conjugation and parity both exchange $(j_+, j_-) \leftrightarrow (j_-, j_+)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-8|Theorem §C3.3.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]]): conjugation acts on the algebra through $c$, parity through an automorphism; both swap $\mathfrak a_+$ and $\mathfrak a_-$.
> - Theorem §CB.4.13, 3 with $A = S^+$, $B = S^-$ is the decomposition of two-forms into self-dual and anti-self-dual parts (§CB.12; [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]]).
> - **Used in**: Definitions §CB.4.1–Theorem §CB.4.3 — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]]; Theorem §CB.4.5 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]; Definitions §CB.4.6–Theorem §CB.4.8 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-5|Def. §C5a.1.5]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]; Theorem §CB.4.9 — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]]; Theorem §CB.4.13 — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]]; Theorem §CB.4.14 — [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]]; Theorems §CB.4.15–§CB.4.16 — [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]].
