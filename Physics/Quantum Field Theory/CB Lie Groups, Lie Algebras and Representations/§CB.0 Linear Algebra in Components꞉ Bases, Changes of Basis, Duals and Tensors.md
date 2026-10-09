---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.0
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras]] →

*Sources: Axler, Linear Algebra Done Right (the vault's Linear Algebra notes), linked where used (Defs. 2.26, 3.31, 3.73, 3.110, 3.112, 9.71, 9.85, 9.88; Thms. 3.35, 3.43, 3.76, 3.82, 3.84, 3.114, 8.49, 8.50, 9.52, 9.72, 9.73) · Yu Zhao-Huan, 量子场论讲义, §5.2, eqs. (5.55)–(5.56), (5.72) · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness"), §8.3 (Principle "Invariant tensors with mixed slots"; "contracting them is plain matrix multiplication"), Ch. 10 §10.3 · Sakurai §1.5.2 (as recorded in QM C1.4) · PHY 513, Problem Set 6, Problem 3(b) (statement: $U_D$) · the index-by-index derivations and the basis-free formulation written here (first for spinor space in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; moved here in option-1 batch B2, 2026-10-08) · for the real case: the user's PHY 513 notes, Ch. 1 §1.5 ("Vectors, dual vectors, and the metric as an isomorphism"; "Tensors as multilinear maps, and their transformation law", eqs. (covectortransform), (tensortransform)), first written in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] and moved here in option-1 batch B3, 2026-10-08.*

What do a basis and a change of basis do to the vectors, linear maps, dual vectors and tensors of a finite-dimensional vector space? The physics chapters answer this twice, each in its own notation: for spinor space in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] and for spacetime vectors in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]. Every later section of CB (matrices of representations, invariant tensors, Clifford modules) uses the same rules. This section states them once, for a finite-dimensional $V$ over $\mathbb K = \mathbb R$ or $\mathbb C$, before the Lie theory of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] begins.

*Notation.* The statements below were first written for spinor space $V$, a four-dimensional complex vector space ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]), and keep that wording: "spinor", "spinor tensor", $4\times4$ matrices, indices $a, b = 1, \dots, 4$. They use nothing about $V$ but that it is a finite-dimensional vector space with a basis. For any $V$ of dimension $n$ over $\mathbb K = \mathbb R$ or $\mathbb C$, read $n$ for $4$ and "vector" for "spinor"; over $\mathbb R$ complex conjugation acts trivially. The real case is written separately, in the spacetime notation of [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] where it was first stated: the dual space, tensors as multilinear maps and their transformation law ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-11|Theorem §CB.0.11]], moved here in option-1 batch B3), with upper indices for vector slots and lower ones for covector slots; the index calculus with the metric stays in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]].

## Components, matrices and changes of basis

> [!definition] Definition §CB.0.1: Components of a Spinor in a Basis
> Let $e = (e_1, e_2, e_3, e_4)$ be a basis of spinor space $V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]; bases, [[§5 Bases#^ladr-2-26|LADR Def. 2.26]]). The **components** $\psi_a$ of $\psi \in V$ are the unique numbers with
>
> $$
> \psi = \sum_{a=1}^4\psi_a\,e_a ,
> $$
>
> and the column $(\psi_1, \psi_2, \psi_3, \psi_4)^{\mathsf T} \in \mathbb C^4$ is the matrix of $\psi$ in that basis ([[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR Def. 3.73]]). The column is also written $\psi$ when the basis is fixed.
>
> *Source: LADR Def. 3.73 · Yu §5.2, eq. (5.55)*

^def-cb-0-1

> [!definition] Definition §CB.0.2: The Matrix of a Linear Map on Spinor Space
> For a linear map $M \in \operatorname{End}(V)$ and a basis $e$ of $V$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]]), the **matrix** of $M$ is the $4\times4$ array $(M_{ab})$ with
>
> $$
> M\,e_b = \sum_{a=1}^4 M_{ab}\,e_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the components of $Me_b$ ([[§9 Matrices#^ladr-3-31|LADR Def. 3.31]]). The first index is the row, the second the column.
>
> *Source: LADR Def. 3.31*

^def-cb-0-2

> [!theorem] Theorem §CB.0.3: Linear Maps Act by Matrix Multiplication
> In a fixed basis of $V$ (with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2|Def. §CB.0.2]]), for $M, N \in \operatorname{End}(V)$, $\psi \in V$, $\lambda \in \mathbb C$:
>
> $$
> (M\psi)_a = \sum_b M_{ab}\psi_b, \qquad (MN)_{ab} = \sum_c M_{ac}N_{cb}, \qquad (M + \lambda N)_{ab} = M_{ab} + \lambda N_{ab}, \qquad (\mathrm{id})_{ab} = \delta_{ab} .
> $$
>
> So "an operator acting on a spinor" is a matrix times a column, and every algebraic identity among operators holds verbatim among their matrices.
>
> *Source: [[§10 Invertibility and Isomorphisms#^ladr-3-76|LADR Thm. 3.76]], [[§9 Matrices#^ladr-3-43|LADR Thm. 3.43]], [[§9 Matrices#^ladr-3-35|LADR Thm. 3.35]] · Yu §5.2, eq. (5.56) ("the product on the right is a matrix times a column vector")*

^thm-cb-0-3

> [!derivation]- Derivation
> **1. Action.** $M\psi = M\bigl(\sum_b\psi_be_b\bigr) = \sum_b\psi_b\,Me_b$ (linearity of $M$) $= \sum_b\psi_b\sum_aM_{ab}e_a$ (Def. §CB.0.2) $= \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a$ (exchange of two finite sums). Components are unique (Def. §CB.0.1), so $(M\psi)_a = \sum_bM_{ab}\psi_b$.
>
> **2. Product.** $(MN)e_b = M(Ne_b) = M\bigl(\sum_cN_{cb}e_c\bigr) = \sum_cN_{cb}\sum_aM_{ac}e_a = \sum_a\bigl(\sum_cM_{ac}N_{cb}\bigr)e_a$; read off the coefficient of $e_a$.
>
> **3. Sum and identity.** $(M + \lambda N)e_b = \sum_a(M_{ab} + \lambda N_{ab})e_a$; $\mathrm{id}\,e_b = e_b = \sum_a\delta_{ab}e_a$.
>
> **What the derivation shows**
> - Only linearity and the uniqueness of components are used: the matrix calculus of the lecture is the calculus of $\operatorname{End}(V)$ written in one basis.
> - Used next: in a new basis the same operator has a new matrix (Theorem §CB.0.5), and the Clifford relation survives in every basis (Theorem §CB.10.14).

^der-cb-0-3

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2|Def. §CB.0.2]]

> [!definition] Definition §CB.0.4: The Change-of-Basis Matrix
> Let $e$ (old) and $e'$ (new) be two bases of $V$. The **change-of-basis matrix** $U$ is the $4\times4$ matrix with
>
> $$
> e_b = \sum_{a=1}^4U_{ab}\,e'_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the new components of the old basis vector $e_b$. In Axler's notation $U = \mathcal M(\mathrm{id}, (e), (e'))$, and it is invertible, with $e'_b = \sum_a(U^{-1})_{ab}\,e_a$ ([[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]).
>
> *Source: LADR Thm. 3.82, Thm. 3.84 (its matrix $C$) · the convention for $U$ fixed here so that $\gamma'^\mu = U\gamma^\mu U^{-1}$, as in Theorem §CB.12.12 and the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness"); other conventions: Caution below*

^def-cb-0-4

> [!theorem] Theorem §CB.0.5: Components Change with U, Matrices with U and U⁻¹
> With the change-of-basis matrix $U$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]]), for every $\psi \in V$ and $M \in \operatorname{End}(V)$:
>
> $$
> \psi'_a = \sum_bU_{ab}\,\psi_b, \quad\text{i.e.}\quad \psi' = U\psi ; \qquad M'_{ab} = \sum_{c,d}U_{ac}\,M_{cd}\,(U^{-1})_{db}, \quad\text{i.e.}\quad M' = UMU^{-1} .
> $$
>
> One index, one $U$; a row index gets $U$ from the left, a column index $U^{-1}$ from the right. This is the change-of-basis formula of linear algebra ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], whose $A = C^{-1}BC$ is $M = U^{-1}M'U$).
>
> *Source: LADR Thm. 3.76, Thm. 3.84 · Yu §5.2, eq. (5.72) (the similarity transformation, in the opposite naming of $U$) · the index-by-index derivation written here*

^thm-cb-0-5

> [!derivation]- Derivation
> **1. The inverse relation.** Claim $e'_b = \sum_a(U^{-1})_{ab}e_a$. Insert $e_a = \sum_dU_{da}e'_d$ (Def. §CB.0.4) into the right side: $\sum_a(U^{-1})_{ab}\sum_dU_{da}e'_d = \sum_d\bigl(\sum_aU_{da}(U^{-1})_{ab}\bigr)e'_d = \sum_d(UU^{-1})_{db}e'_d = \sum_d\delta_{db}e'_d = e'_b$. ($U$ is invertible because the matrix of the identity from $e'$ back to $e$ is its inverse, LADR Thm. 3.82.)
>
> **2. Components.** $\psi = \sum_b\psi_be_b$ (old components) $= \sum_b\psi_b\sum_aU_{ab}e'_a$ (Def. §CB.0.4) $= \sum_a\bigl(\sum_bU_{ab}\psi_b\bigr)e'_a$. The new components are unique (Def. §CB.0.1), so $\psi'_a = \sum_bU_{ab}\psi_b$.
>
> **3. Matrices.** Apply $M$ to a new basis vector and express everything in the new basis:
>
> $$
> Me'_b \overset{(1)}{=} \sum_c(U^{-1})_{cb}\,Me_c \overset{\text{Def. 9.3}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\,e_d \overset{\text{Def. 9.4}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\sum_aU_{ad}\,e'_a = \sum_a\Bigl(\sum_{d,c}U_{ad}M_{dc}(U^{-1})_{cb}\Bigr)e'_a .
> $$
>
> By Def. §CB.0.2 in the new basis the bracket is $M'_{ab}$, and it is the $(a, b)$ entry of the triple product $UMU^{-1}$ (Theorem §CB.0.3, product rule twice).
>
> **4. Consistency check.** $(M\psi)' = U(M\psi) = UMU^{-1}U\psi = M'\psi'$: computing $M\psi$ in either basis gives the same vector of $V$.
>
> **What the derivation shows**
> - The rules are not physics: they are the bookkeeping of one vector and one linear map in two bases. $\psi$ has one $V$-index, hence one factor $U$; $M$ has a row index (a $V$-slot) and a column index (contracted with $\psi$), hence $U$ on the left and $U^{-1}$ on the right. Which kind of index gets which factor is the slot rule (Theorem §CB.0.10).
> - Used next: the Dirac matrices are matrices of operators (Theorem §CB.10.14), so $\gamma'^\mu = U\gamma^\mu U^{-1}$ is this theorem, not an additional rule.

^der-cb-0-5

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2|Def. §CB.0.2]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3|Theorem §CB.0.3]], [[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]

> [!remark] Remark: Why "UψU⁻¹" means nothing
> $\psi$ is a $4\times1$ column and $U$ a $4\times4$ matrix: $U\psi$ is a column, but $\psi U^{-1}$ is a $4\times1$ times a $4\times4$, which is not defined. The shape reflects the slot count: a spinor has one $V$-slot, so it takes one factor (Theorem §CB.0.5); only objects with two spinor slots, such as $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$ or $\psi\bar\chi$ (a column times a row, $4\times4$), take the sandwich. A sandwich $U^{-1}\hat\psi U$ does occur in field theory, with the unitary operator $U(\Lambda)$ on the Hilbert space; it acts on the operator nature of $\hat\psi$, not on its spinor index (Caution: Three different transformations, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]).
>
> *Source: written here · the user's PHY 513 notes, Ch. 10 §10.3 ("The operator carries the quantum, particle-like aspect; the column and the plane wave carry the wave aspect and all the Lorentz structure")*

^rem-cb-0-1

> [!caution] Caution: Which matrix is called U
> Here $U$ converts old components into new ones, $\psi' = U\psi$, $\gamma' = U\gamma U^{-1}$, as in Pauli's theorem ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12|Theorem §CB.12.12]]), the user's PHY 513 notes and the matrix of [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] (there old = Dirac basis, new = chiral basis). Yu (5.72) writes $\gamma'^\mu = U^\dagger\gamma^\mu U$ with $U$ unitary, so Yu's $U$ is the inverse of this one; Axler's $C$ in LADR Thm. 3.84 is this $U$; Sakurai's transformation matrix gives (new) $= U^\dagger$(old), again the inverse ([[§C1.4 Change of Basis and Unitary Equivalence#^cau-c1-4-1|QM, Caution: Which matrix is called U]]). Larsen's $U_D$ (Problem Set 6, Problem 3(b)) converts chiral (old) into Dirac (new) components, $\psi_D = U_D\psi$, $\gamma_D^\mu = U_D\gamma^\mu U_D^\dagger$: it follows this convention, and it is the inverse $U^\dagger$ of the matrix of Example §C5a.5.1, which runs from the Dirac to the chiral basis (the relation is stated there). Before using a formula, check which basis labels the rows of the source's $U$.
>
> *Source: Yu §5.2, eq. (5.72) · LADR Thm. 3.84 · Sakurai §1.5.2 (as recorded in QM C1.4) · PHY 513, Problem Set 6, Problem 3(b) (statement: $U_D$)*

^cau-cb-0-1

## Slots: covectors, operators and the index rule

> [!definition] Definition §CB.0.6: Dual Spinor Space and Dual Basis
> The **dual spinor space** $V'$ is the space of linear functionals $\varphi : V \to \mathbb C$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]). The **dual basis** $(\varepsilon^1, \dots, \varepsilon^4)$ of a basis $e$ is defined by $\varepsilon^a(e_b) = \delta_{ab}$ ([[§12 Duality#^ladr-3-112|LADR Def. 3.112]]). The **components** of $\varphi \in V'$ are $\varphi_a \equiv \varphi(e_a)$, written as a row $(\varphi_1, \dots, \varphi_4)$; then $\varphi = \sum_a\varphi_a\varepsilon^a$ and $\varphi(\psi) = \sum_a\varphi_a\psi_a$, a row times a column.
>
> *Source: LADR Def. 3.110, Def. 3.112, Thm. 3.114 · the row picture: the user's PHY 513 notes, Ch. 8 §8.3 ("contracting them is plain matrix multiplication")*

^def-cb-0-6

The real case in the spacetime notation of [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]: $V = \mathbb R^4$ with basis $e_\mu$, vector components with upper indices, covector components with lower ones, and the dual written $V^\ast$ (the complex box above writes $V'$, rows and Latin indices):

> [!definition] Definition §CB.0.7: Dual Space
> Let $V = \mathbb R^4$ with basis $e_\mu$, so $x = x^\mu e_\mu$. Its **dual space** $V^{\ast}$ is the space of linear functionals $\omega: V \to \mathbb R$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]), with dual basis $e^\mu(e_\nu) = \delta^\mu{}_\nu$ ([[§12 Duality#^ladr-3-112|LADR Def. 3.112]]); $\omega = \omega_\mu e^\mu$ and $\omega(x) = \omega_\mu x^\mu$, with no metric.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Vectors, dual vectors, and the metric as an isomorphism")*

^def-cb-0-7

> [!definition] Definition §CB.0.8: Spinor Tensors and Their Slots
> A **spinor tensor of type $(k, l)$** is an element of $V^{\otimes k}\otimes V'^{\otimes l}$ ([[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]; $V'$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]]): it has $k$ **$V$-slots** and $l$ **$V'$-slots**. In a basis $e$ with dual basis $\varepsilon$ its **components** $T_{a_1\dots a_k;\,b_1\dots b_l}$ are the coefficients of $e_{a_1}\otimes\dots\otimes e_{a_k}\otimes\varepsilon^{b_1}\otimes\dots\otimes\varepsilon^{b_l}$. A **contraction** sets one $V$-index equal to one $V'$-index and sums. Examples: a spinor $\psi$ is type $(1, 0)$, a row $\varphi$ type $(0, 1)$, a linear map $M \in \operatorname{End}(V)$ type $(1, 1)$ through $M = \sum_{a,b}M_{ab}\,e_a\otimes\varepsilon^b$, a number type $(0, 0)$.
>
> *Source: LADR Def. 9.71, Def. 9.88 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "transforming all of its indices at once, each by the rule of its own slot") · the identification $\operatorname{End}(V) \cong V\otimes V'$ written here (Derivation §CB.0.10, step 2)*

^def-cb-0-8

> [!definition] Definition §CB.0.9: Tensor as a Multilinear Map
> With $V$, $V^{\ast}$ and the dual basis of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], a **tensor of type $(r, s)$** is a multilinear map ([[§38 Tensor Products#^ladr-9-85|LADR Def. 9.85]])
>
> $$
> T: \underbrace{V^*\times\cdots\times V^*}_{r}\times\underbrace{V\times\cdots\times V}_{s} \to \mathbb R, \qquad T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} = T(e^{\mu_1}, \dots, e^{\mu_r}, e_{\nu_1}, \dots, e_{\nu_s}) .
> $$
>
> A vector is a $(1,0)$ tensor ($x(\omega) = \omega(x)$), a covector a $(0,1)$ tensor, a number a $(0,0)$ tensor.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Tensors as multilinear maps, and their transformation law")*

^def-cb-0-9

> [!theorem] Theorem §CB.0.10: The Slot Rule
> Under a change of basis with matrix $U$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]]), the components of a spinor tensor ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8|Def. §CB.0.8]]) change by one factor per slot:
>
> $$
> T'_{a_1\dots a_k;\,b_1\dots b_l} = \sum U_{a_1c_1}\cdots U_{a_kc_k}\;T_{c_1\dots c_k;\,d_1\dots d_l}\;(U^{-1})_{d_1b_1}\cdots(U^{-1})_{d_lb_l} ,
> $$
>
> $U$ for each $V$-slot, $U^{-1}$ (from the right) for each $V'$-slot. In particular a row transforms as $\varphi' = \varphi U^{-1}$, an operator as $M' = UMU^{-1}$ (agreeing with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]), and a contraction of a $V$-slot with a $V'$-slot removes both factors: a fully contracted expression is the same number in every basis.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"; "The practical test, continued") · LADR Thm. 9.73 (multilinearity of ⊗) · the general rule and its derivation written here*

^thm-cb-0-10

> [!derivation]- Derivation
> **1. The dual basis.** Expand $\varepsilon^b$ in the new dual basis $\varepsilon'$: its coefficients are its values on the new basis vectors (LADR Thm. 3.114 applied in $V'$). By step 1 of Derivation §CB.0.5, $\varepsilon^b(e'_c) = \varepsilon^b\bigl(\sum_d(U^{-1})_{dc}e_d\bigr) = \sum_d(U^{-1})_{dc}\delta_{bd} = (U^{-1})_{bc}$, so $\varepsilon^b = \sum_c(U^{-1})_{bc}\,\varepsilon'^c$.
>
> **2. Operators as tensors.** The matrix units $E^{(ab)} \equiv e_a\otimes\varepsilon^b$ act as $\psi \mapsto \varepsilon^b(\psi)\,e_a = \psi_b\,e_a$. Then $\sum_{a,b}M_{ab}\,\varepsilon^b(\psi)\,e_a = \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a = M\psi$ (Theorem §CB.0.3), so $M = \sum M_{ab}\,e_a\otimes\varepsilon^b$. The sixteen $E^{(ab)}$ span $\operatorname{End}(V)$ by this formula and are independent (apply to $e_c$), and $\dim(V\otimes V') = 16$ ([[§38 Tensor Products#^ladr-9-72|LADR Thm. 9.72]]): $\operatorname{End}(V) \cong V\otimes V'$.
>
> **3. One factor per slot.** Insert $e_{c} = \sum_aU_{ac}e'_{a}$ (Def. §CB.0.4) into every $V$-slot and $\varepsilon^{d} = \sum_b(U^{-1})_{db}\varepsilon'^{b}$ (step 1) into every $V'$-slot of $T = \sum T_{c_1\dots;\,d_1\dots}\,e_{c_1}\otimes\dots\otimes\varepsilon^{d_1}\otimes\dots$. The tensor product is linear in each factor (LADR Thm. 9.73), so the factors pull out of each slot separately, and the coefficient of $e'_{a_1}\otimes\dots\otimes\varepsilon'^{b_1}\otimes\dots$ is the displayed formula.
>
> **4. The cases.** Type $(0, 1)$: $\varphi'_b = \sum_d\varphi_d(U^{-1})_{db}$, i.e. $\varphi' = \varphi U^{-1}$; also directly, $\varphi'_b = \varphi(e'_b) = \sum_d(U^{-1})_{db}\varphi(e_d)$. Type $(1, 1)$: $M'_{ab} = \sum U_{ac}M_{cd}(U^{-1})_{db}$, Theorem §CB.0.5 again.
>
> **5. Contraction.** Contract a $V$-index $a$ with a $V'$-index $b$ of $T'$: the two factors become $\sum_aU_{ac}(U^{-1})_{da} = (U^{-1}U)_{dc} = \delta_{dc}$, so the contracted components transform with the remaining slots only. With every slot contracted, nothing remains: $\varphi'\psi' = \varphi U^{-1}U\psi = \varphi\psi$, $\varphi'M'\psi' = \varphi M\psi$.
>
> **What the derivation shows**
> - The "index rule" of the course (one $U$ per index, sandwiches for matrices, invariant scalars) is the transformation law of tensor components, with $V$ and $V'$ as the two kinds of slot. It needs no physics and no metric.
> - ⚑ By-product: $\psi^\dagger$ is *not* a $V'$-slot. Its components $\psi_a^{\ast}$ transform as $(\psi')^{\ast} = U^{\ast}\psi^{\ast}$, i.e. the row $\psi'^\dagger = \psi^\dagger U^\dagger$, which is the $V'$-rule $\psi^\dagger U^{-1}$ only when $U^\dagger = U^{-1}$ → Theorem §C5a.2.2. The row that *is* a $V'$-slot for every $U$ is $\bar\psi$, once defined basis-free (Def. §C5a.2.1).
> - Used next: trace and eigenvalues (Theorem §CB.0.12); the table in the remark below.

^der-cb-0-10

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8|Def. §CB.0.8]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3|Theorem §CB.0.3]], [[§12 Duality#^ladr-3-114|LADR Thm. 3.114]], [[§38 Tensor Products#^ladr-9-73|LADR Thm. 9.73]]

The real case again, for a tensor moved by an invertible $\Lambda$ rather than re-expanded in a new basis; the two give the same formula, with $\Lambda$ in place of $U$ (one factor per slot, $\Lambda$ for an upper and $\Lambda^{-1}$ for a lower index):

> [!theorem] Theorem §CB.0.11: The Transformation Law Follows from Multilinearity
> For an invertible $\Lambda$ acting on $V$, the transformed tensor $\Lambda T(\omega_1, \dots, x_1, \dots) = T(\omega_1\circ\Lambda, \dots, \Lambda^{-1}x_1, \dots)$ (for a vector, $\Lambda x$; for a covector, $\omega\circ\Lambda^{-1}$) has components
>
> $$
> (\Lambda T)^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} = \Lambda^{\mu_1}{}_{\rho_1}\cdots\Lambda^{\mu_r}{}_{\rho_r}\,(\Lambda^{-1})^{\sigma_1}{}_{\nu_1}\cdots(\Lambda^{-1})^{\sigma_s}{}_{\nu_s}\,T^{\rho_1\cdots\rho_r}{}_{\sigma_1\cdots\sigma_s} :
> $$
>
> one factor $\Lambda$ per upper index and one $\Lambda^{-1}$ per lower index. For $\Lambda \in O(1,3)$, $(\Lambda^{-1})^\sigma{}_\nu = \Lambda_\nu{}^\sigma$, and this is the law that [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]] takes as the definition.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5, eqs. (covectortransform), (tensortransform)*

^thm-cb-0-11

> [!derivation]- Derivation
> **1. The transformed basis functionals.** For the dual basis, $(e^\mu\circ\Lambda)(e_\rho) = e^\mu(\Lambda e_\rho) = e^\mu(\Lambda^\sigma{}_\rho e_\sigma) = \Lambda^\mu{}_\rho$, so $e^\mu\circ\Lambda = \Lambda^\mu{}_\rho e^\rho$.
>
> **2. The transformed basis vectors.** $\Lambda^{-1}e_\nu = (\Lambda^{-1})^\sigma{}_\nu e_\sigma$, the $\nu$-th column of $\Lambda^{-1}$.
>
> **3. Multilinearity.** Insert steps 1–2 into the definition of $\Lambda T$ and pull each sum out of its slot, one slot at a time:
>
> $$
> (\Lambda T)^{\mu_1\cdots}{}_{\nu_1\cdots} = T\bigl(\Lambda^{\mu_1}{}_{\rho_1}e^{\rho_1}, \dots, (\Lambda^{-1})^{\sigma_1}{}_{\nu_1}e_{\sigma_1}, \dots\bigr) = \Lambda^{\mu_1}{}_{\rho_1}\cdots(\Lambda^{-1})^{\sigma_1}{}_{\nu_1}\cdots T(e^{\rho_1}, \dots, e_{\sigma_1}, \dots) .
> $$
>
> **4. Consistency for vectors and covectors.** For a vector regarded as $x(\omega) = \omega(x)$: $(\Lambda x)(\omega) = x(\omega\circ\Lambda) = \omega(\Lambda x)$, so the $(1,0)$ case is $x'^\mu = \Lambda^\mu{}_\nu x^\nu$. For a covector, $\omega'_\nu = (\Lambda^{-1})^\sigma{}_\nu\omega_\sigma$, and $\omega'(x') = \omega'_\nu x'^\nu = \omega_\sigma(\Lambda^{-1})^\sigma{}_\nu\Lambda^\nu{}_\rho x^\rho = \omega_\sigma\delta^\sigma{}_\rho x^\rho = \omega(x)$: a number does not change.
>
> **5. Lorentz.** For $\Lambda \in O(1,3)$, $(\Lambda^{-1})^\sigma{}_\nu = g^{\sigma\alpha}\Lambda^\beta{}_\alpha g_{\beta\nu} = \Lambda_\nu{}^\sigma$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2).
>
> **What the derivation shows**
> - The law is not a convention: it is what multilinearity forces once vectors are moved by $\Lambda$; nothing Lorentz-specific was used until step 5.
> - The lecture's definition, "anything that transforms like $p^\mu q^\nu$", is the same law read backwards on products; the coefficient array $\Lambda^\mu{}_\lambda\Lambda^\nu{}_\sigma$ is a $16\times16$ matrix acting on the sixteen components.
> - Contraction, products, and raising and lowering then commute with $\Lambda$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-1|REL Theorem §B2.2.1]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]]), which is the covariance principle's toolkit ([[§B2.2 Tensors and the Covariance Principle#^pr-b2-2-9|REL Principle §B2.2.9]]).

^der-cb-0-11

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]]

> [!theorem] Theorem §CB.0.12: Trace, Determinant and Eigenvalues Do Not Depend on the Basis
> For $M \in \operatorname{End}(V)$ with matrices $M$ and $M' = UMU^{-1}$ in two bases ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]):
>
> $$
> \operatorname{tr}M' = \operatorname{tr}M, \qquad \det M' = \det M, \qquad \det(z\mathbb 1 - M') = \det(z\mathbb 1 - M) ,
> $$
>
> so the eigenvalues of $M$ with their multiplicities are properties of the operator, not of the basis ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR Thm. 8.50]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]], [[§37 Determinants#^ladr-9-63|LADR Def. 9.63]]). The trace is the contraction of the two slots of $M$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]).
>
> *Source: LADR Thm. 8.49, Thm. 8.50, Thm. 9.52, Def. 9.63*

^thm-cb-0-12

> [!derivation]- Derivation
> **1. Trace.** $\operatorname{tr}(UMU^{-1}) = \operatorname{tr}\bigl((UM)U^{-1}\bigr) = \operatorname{tr}\bigl(U^{-1}(UM)\bigr) = \operatorname{tr}M$, by $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]). As a contraction: $\operatorname{tr}M = \sum_aM_{aa}$ contracts the $V$-slot with the $V'$-slot (step 5 of Derivation §CB.0.10).
>
> **2. Determinant.** $\det(UMU^{-1}) = \det M$ (LADR Thm. 9.52 with $S = U^{-1}$).
>
> **3. Characteristic polynomial.** $z\mathbb 1 - UMU^{-1} = U(z\mathbb 1 - M)U^{-1}$, because $U(z\mathbb 1)U^{-1} = z\mathbb 1$. Step 2 gives $\det(z\mathbb 1 - M') = \det(z\mathbb 1 - M)$. Its zeros, with multiplicities, are the eigenvalues (LADR Def. 9.63).
>
> **What the derivation shows**
> - Every statement of the form "$\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$" or "$\gamma^5$ has eigenvalues $\pm1$" is a statement about operators on $V$ and can be checked in any one basis ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]).
> - Statements about individual entries ("$\gamma^0$ is off-diagonal", "the upper two components") are not of this kind.

^der-cb-0-12

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]]

> [!remark]- Connections
> - The transformation rules of spinors and $\gamma$ matrices are the change-of-basis formula of linear algebra, $A = C^{-1}BC$ for operators and its dual and conjugate versions for covectors and forms; nothing specific to physics enters until the Clifford action — [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], [[§12 Duality#^ladr-3-112|LADR Def. 3.112]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]].
> - The real case with a metric, where an index is raised and lowered instead of being a separate slot, is the spacetime index calculus — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-9|Theorem §CB.7.9]].
> - **Used in**: Definition §CB.0.1 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.2 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Theorem §CB.0.3 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.4 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]); Theorem §CB.0.5 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-2|§C5a.5, Caution: Bases and conventions across the sources]], [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]]); §CB.0, Remark: Why "UψU⁻¹" means nothing — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); §CB.0, Caution: Which matrix is called U — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]); Definition §CB.0.6 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]); Definition §CB.0.7 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded; cited in [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]]); Definition §CB.0.8 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.9 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded); Theorem §CB.0.10 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Theorem §CB.0.11 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded; cited in [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]), [[§C1a.7 Relativistic Electrodynamics in Index Form|§C1a.7]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]); Theorem §CB.0.12 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]).
