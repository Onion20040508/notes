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

*Sources: Axler, Linear Algebra Done Right (the vault's Linear Algebra notes), linked where used (Defs. 2.26, 3.31, 3.73, 3.110, 3.112, 9.71, 9.85, 9.88; Thms. 3.35, 3.43, 3.76, 3.82, 3.84, 3.114, 8.49, 8.50, 9.52, 9.72, 9.73) · Yu Zhao-Huan, 量子场论讲义, §5.2, eqs. (5.55)–(5.56), (5.72) · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness"), §8.3 (Principle "Invariant tensors with mixed slots"; "contracting them is plain matrix multiplication"), Ch. 10 §10.3 · Sakurai §1.5.2 (as recorded in QM C1.4) · PHY 513, Problem Set 6, Problem 3(b) (statement: $U_D$) · the index-by-index derivations and the basis-free formulation written here (first for spinor space in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; moved here in option-1 batch B2, 2026-10-08) · for the real case: the user's PHY 513 notes, Ch. 1 §1.5 ("Vectors, dual vectors, and the metric as an isomorphism"; "Tensors as multilinear maps, and their transformation law", eqs. (covectortransform), (tensortransform)), first written in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] and moved here in option-1 batch B3, 2026-10-08 · restated here in the CB ordering pass (2026-10-08), with their proofs, from their physics homes: the metric and the matrices that preserve it (the user's PHY 513 notes, Ch. 1 §1.4–§1.5; the user's PHY 505 notes and series, Part III, §3.1, §3.8, through REL §B1.2), the Levi-Civita symbol (the user's PHY 513 notes, Ch. 1 §1.5; Yu §1.5), the Pauli matrices (Griffiths §4.4.1, Problem 4.29; Greensite §13.1; PS §3.2, eqs. (3.38), (3.41); Yu Exercise 3.7).*

What do a basis and a change of basis do to the vectors, linear maps, dual vectors and tensors of a finite-dimensional vector space? The physics chapters answer this twice, each in its own notation: for spinor space in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] and for spacetime vectors in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]. Every later section of CB (matrices of representations, invariant tensors, Clifford modules) uses the same rules. This section states them once, for a finite-dimensional $V$ over $\mathbb K = \mathbb R$ or $\mathbb C$, before the Lie theory of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] begins.

*Notation.* The statements below were first written for spinor space $V$, a four-dimensional complex vector space ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]), and keep that wording: "spinor", "spinor tensor", $4\times4$ matrices, indices $a, b = 1, \dots, 4$. They use nothing about $V$ but that it is a finite-dimensional vector space with a basis. For any $V$ of dimension $n$ over $\mathbb K = \mathbb R$ or $\mathbb C$, read $n$ for $4$ and "vector" for "spinor"; over $\mathbb R$ complex conjugation acts trivially. The real case is written separately, in the spacetime notation of [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] where it was first stated: the dual space, tensors as multilinear maps and their transformation law ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], moved here in option-1 batch B3), with upper indices for vector slots and lower ones for covector slots; the index calculus with the metric stays in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]]. The basic facts that the later sections of CB use (the metric of Minkowski space and the matrices that preserve it, the Levi-Civita symbol, the Pauli matrices) are restated in this section with their proofs ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]–[[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]] and the last heading).

## Components, matrices and changes of basis

> [!definition] Definition §CB.0.1: Components of a Spinor in a Basis
> Let $e = (e_1, e_2, e_3, e_4)$ be a basis of spinor space $V$ (a four-dimensional complex vector space, [[§2 Definition of Vector Space#^ladr-1-20|LADR Def. 1.20]]; bases, [[§5 Bases#^ladr-2-26|LADR Def. 2.26]]). The **components** $\psi_a$ of $\psi \in V$ are the unique numbers with
>
> $$
> \psi = \sum_{a=1}^4\psi_a\,e_a ,
> $$
>
> and the column $(\psi_1, \psi_2, \psi_3, \psi_4)^{\mathsf T} \in \mathbb C^4$ is the matrix of $\psi$ in that basis ([[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR Def. 3.73]]). The column is also written $\psi$ when the basis is fixed.
>
> *Source: LADR Def. 3.73 · Yu §5.2, eq. (5.55) · the course's spinor space: [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]*

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
> - Used next: in a new basis the same operator has a new matrix (Theorem §CB.0.5), and the Clifford relation survives in every basis (Theorem §CB.10.15).

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
> - Used next: the Dirac matrices are matrices of operators (Theorem §CB.10.15), so $\gamma'^\mu = U\gamma^\mu U^{-1}$ is this theorem, not an additional rule.

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
> - Used next: trace and eigenvalues (Theorem §CB.0.15); the table in the remark below.

^der-cb-0-10

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8|Def. §CB.0.8]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3|Theorem §CB.0.3]], [[§12 Duality#^ladr-3-114|LADR Thm. 3.114]], [[§38 Tensor Products#^ladr-9-73|LADR Thm. 9.73]]

## The metric of Minkowski space

The real case with a metric. The basic facts below were first stated for spacetime in [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] and in Relativity ([[§B1.1 The Metric and Index Notation|REL §B1.1]], [[§B1.2 Lorentz Transformations and the Lorentz Group|REL §B1.2]]); they are restated here, in the notation of these notes, because the Lie theory of §CB.1–§CB.2 and the invariant tensors of §CB.7 use them (CB ordering pass, 2026-10-08):

> [!definition] Definition §CB.0.11: The Minkowski Metric and Index Positions
> **Minkowski space** $\mathbb R^{1,3}$ is $V = \mathbb R^4$, with standard basis $e_0, \dots, e_3$ and components $x = x^\mu e_\mu$ ($\mu, \nu, \ldots = 0, \dots, 3$; Latin $i, j, \ldots = 1, 2, 3$), together with the **metric** $g(x, y) = g_{\mu\nu}x^\mu y^\nu$, $[g_{\mu\nu}] = \operatorname{diag}(1, -1, -1, -1)$. $g^{\mu\nu}$ is the inverse matrix, $g^{\mu\nu}g_{\nu\rho} = \delta^\mu{}_\rho$. An index that appears once up and once down in a term is summed. Indices are **lowered** with $g_{\mu\nu}$ and **raised** with $g^{\mu\nu}$, $x_\mu = g_{\mu\nu}x^\nu$, $x^\mu = g^{\mu\nu}x_\nu$, so that $g(x, y) = x_\mu y^\mu \equiv x\cdot y$ and $x^2 \equiv x_\mu x^\mu$; on an array with several indices each index is moved separately, e.g. $A_\nu{}^\mu = g_{\nu\rho}A^\rho{}_\sigma g^{\sigma\mu}$ for a matrix $A = [A^\mu{}_\nu]$, and $\omega_{\mu\nu} = g_{\mu\rho}\omega^\rho{}_\nu$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4, eqs. (fourvector), (lowerindex), (pq); §1.5, eq. (metricform) · PHY 513 Lecture 1, Part C ("Index Gymnastics") · Yu §1.3, eqs. (1.18)–(1.23) · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]], the same convention written for $x^\mu = (t, \mathbf x)$, $p^\mu = (E, \mathbf p)$ and $\partial_\mu$ in natural units.*

^def-cb-0-11

> [!theorem] Theorem §CB.0.12: The Metric Identifies Vectors with Covectors
> The metric of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]] is a symmetric, nondegenerate, indefinite bilinear form. The map $x \mapsto x^\flat = g(x, \cdot\,)$ is an isomorphism $V \to V^{\ast}$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]]), with components and inverse
>
> $$
> (x^\flat)_\mu = g_{\mu\nu}x^\nu \equiv x_\mu, \qquad x^\mu = g^{\mu\nu}x_\nu, \qquad g^{\mu\nu}g_{\nu\rho} = \delta^\mu{}_\rho ,
> $$
>
> and numerically $g^{\mu\nu} = g_{\mu\nu}$. Lowering an index *is* this isomorphism: upper indices are components of vectors, lower ones of covectors, and $x_\mu x^\mu$ is the functional $x^\flat$ evaluated on $x$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5, eqs. (metricform), (flat), (inversemetric); Principle "Why indices go up and down" · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]], the same statement for spacetime vectors.*

^thm-cb-0-12

> [!proof]- Proof
> *Adapted from the derivation of Theorem §C1a.5.2 (the user's PHY 513 notes, Ch. 1 §1.5); the properties of $g$ are checked directly instead of being quoted from Relativity.*
>
> **1. The form.** $g(x, y) = g_{\mu\nu}x^\mu y^\nu$ is linear in each argument, and symmetric because the matrix $\operatorname{diag}(1, -1, -1, -1)$ is. It is nondegenerate: if $g(x, y) = 0$ for all $y$, then $y = e_\nu$ gives $g_{\nu\mu}x^\mu = 0$ for every $\nu$, i.e. $\operatorname{diag}(1, -1, -1, -1)\,x = 0$, so $x = 0$ (the matrix has determinant $-1 \ne 0$, [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]). It is indefinite: $g(e_0, e_0) = 1 > 0$ and $g(e_1, e_1) = -1 < 0$.
>
> **2. $x^\flat$ is a functional.** For fixed $x$, $y \mapsto g(x, y)$ is linear in $y$, so $x^\flat \in V^{\ast}$; its components are its values on the basis, $(x^\flat)_\mu = x^\flat(e_\mu) = g(x, e_\mu) = g_{\nu\mu}x^\nu = g_{\mu\nu}x^\nu$ (symmetry of $g$).
>
> **3. Injective, hence bijective.** The map $x \mapsto x^\flat$ is linear. If $x^\flat = 0$ then $g(x, y) = 0$ for all $y$, and step 1 gives $x = 0$. A linear injection between spaces of equal finite dimension ($\dim V^{\ast} = \dim V$, [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]) is surjective.
>
> **4. The inverse.** The matrix of $x \mapsto x^\flat$ in the bases $e_\mu$, $e^\mu$ is $g_{\mu\nu}$; the inverse map has the inverse matrix $g^{\mu\nu}$, defined by $g^{\mu\nu}g_{\nu\rho} = \delta^\mu{}_\rho$. Numerically $g^{\mu\nu} = g_{\mu\nu}$, because each diagonal entry $\pm1$ is its own inverse, a coincidence of this basis.
>
> **What the proof shows**
> - Only nondegeneracy is used, not positivity: the identification works for any signature, which is why "metric" rather than "inner product".
> - In differential geometry this is the musical isomorphism of a pseudo-Riemannian metric on one tangent space ([[§32 The Cotangent Space#^def-32-1|591 Def. §32.1]]).
> - Equivalence: this is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]] word for word; the physics section keeps the spacetime reading (four-vectors, covectors as gradients).

^pf-cb-0-12

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]], [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]

> [!theorem] Theorem §CB.0.13: Matrices Preserving the Metric
> Let $\Lambda = [\Lambda^\mu{}_\nu]$ be a real $4\times4$ matrix with $\Lambda^{\mathsf T}g\Lambda = g$, i.e. $g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta}$, with $g$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]. Then:
> 1. $\det\Lambda = \pm1$; products and inverses of such matrices are again such matrices, so they form a subgroup of $GL(4, \mathbb R)$ ([[§4 Subgroups#^def-4-1|493 Def. §4.1]]).
> 2. The inverse needs no inversion: $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, in components $(\Lambda^{-1})^\mu{}_\nu = \Lambda_\nu{}^\mu = g_{\nu\rho}\Lambda^\rho{}_\sigma g^{\sigma\mu}$, the transpose with both indices moved by the metric.
> 3. $\Lambda^{\mathsf T}$ preserves the metric too: $\Lambda g\Lambda^{\mathsf T} = g$ (the "row form").
> 4. $(\Lambda^0{}_0)^2 = 1 + \sum_i(\Lambda^i{}_0)^2 = 1 + \sum_i(\Lambda^0{}_i)^2$; so either $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$.
>
> *Source: the user's PHY 505 notes, §"Relation Between Λ and Λ⁻¹", §"Lorentz Group Structure" · the user's series, Part III, §3.1, §3.8 · PHY 505 typed notes (earlier offering), §5.2.3, §5.3.4–5.3.6 · the course's version: [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 1–3, and [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]], 1–2, the same statements for Lorentz transformations written with $\boldsymbol\eta$ for $g$.*

^thm-cb-0-13

> [!proof]- Proof
> *Adapted from the derivations of REL Theorems §B1.2.3 and §B1.2.4; notation only ($g$ for $\boldsymbol\eta$).*
>
> **1. Determinant and group.** Taking determinants of $\Lambda^{\mathsf T}g\Lambda = g$ gives $\det\Lambda^{\mathsf T}\det g\det\Lambda = \det g$ ([[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]]), and $\det\Lambda^{\mathsf T} = \det\Lambda$ ([[§37 Determinants#^ladr-9-56|LADR Thm. 9.56]]); since $\det g = -1 \ne 0$, $(\det\Lambda)^2 = 1$. So $\Lambda$ is invertible. If $\Lambda_1, \Lambda_2$ preserve $g$, then $(\Lambda_1\Lambda_2)^{\mathsf T}g(\Lambda_1\Lambda_2) = \Lambda_2^{\mathsf T}(\Lambda_1^{\mathsf T}g\Lambda_1)\Lambda_2 = \Lambda_2^{\mathsf T}g\Lambda_2 = g$, and $\mathbb 1$ preserves $g$. That inverses preserve $g$ is step 2; then the subgroup criterion ([[§4 Subgroups#^prop-4-2|493 Prop. §4.2]]) applies.
>
> **2. The inverse.** Multiply $\Lambda^{\mathsf T}g\Lambda = g$ on the left by $g^{-1}$: $(g^{-1}\Lambda^{\mathsf T}g)\Lambda = \mathbb 1$, so $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$ (a left inverse of a square matrix is its inverse). Its entries are $g^{\mu\sigma}(\Lambda^{\mathsf T})_\sigma{}^\rho g_{\rho\nu} = g^{\mu\sigma}\Lambda^\rho{}_\sigma g_{\rho\nu} = \Lambda_\nu{}^\mu$ (both metrics symmetric; index moves of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]). Multiplying $\Lambda^{\mathsf T}g\Lambda = g$ by $(\Lambda^{-1})^{\mathsf T}$ on the left and by $\Lambda^{-1}$ on the right gives $g = (\Lambda^{-1})^{\mathsf T}g\Lambda^{-1}$: the inverse preserves $g$.
>
> **3. The row form.** Invert both sides of $(\Lambda^{-1})^{\mathsf T}g\Lambda^{-1} = g$: $\Lambda g^{-1}\Lambda^{\mathsf T} = g^{-1}$, and $g^{-1} = g$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-12|Theorem §CB.0.12]]).
>
> **4. The time component.** The $00$ entry of $\Lambda^{\mathsf T}g\Lambda = g$ is $g_{\mu\nu}\Lambda^\mu{}_0\Lambda^\nu{}_0 = (\Lambda^0{}_0)^2 - \sum_i(\Lambda^i{}_0)^2 = g_{00} = 1$: the first column is a unit timelike vector. The $00$ entry of $\Lambda g\Lambda^{\mathsf T} = g$ (step 3) gives $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^0{}_i)^2 = 1$ for the first row. Hence $(\Lambda^0{}_0)^2 \ge 1$.
>
> **What the proof shows**
> - Everything follows from the one matrix equation $\Lambda^{\mathsf T}g\Lambda = g$; nothing about spacetime is used. These matrices form the group $O(1,3)$ of the next section.
> - The two discrete labels $\det\Lambda = \pm1$ and $\operatorname{sgn}\Lambda^0{}_0$ come out of parts 1 and 4.
> - Equivalence: parts 1–3 are REL Theorem §B1.2.3, 1–3, and part 4 with $\det\Lambda = \pm1$ is REL Theorem §B1.2.4, 1–2; Relativity reads $\Lambda$ as a change of inertial frame.

^pf-cb-0-13

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-12|Theorem §CB.0.12]], [[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]], [[§37 Determinants#^ladr-9-56|LADR Thm. 9.56]], [[§4 Subgroups#^prop-4-2|493 Prop. §4.2]]

## Tensors moved by a matrix, and basis-independent quantities

The real case again, for a tensor moved by an invertible $\Lambda$ rather than re-expanded in a new basis; the two give the same formula, with $\Lambda$ in place of $U$ (one factor per slot, $\Lambda$ for an upper and $\Lambda^{-1}$ for a lower index):

> [!theorem] Theorem §CB.0.14: The Transformation Law Follows from Multilinearity
> For an invertible $\Lambda$ acting on $V$, the transformed tensor $\Lambda T(\omega_1, \dots, x_1, \dots) = T(\omega_1\circ\Lambda, \dots, \Lambda^{-1}x_1, \dots)$ (for a vector, $\Lambda x$; for a covector, $\omega\circ\Lambda^{-1}$) has components
>
> $$
> (\Lambda T)^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} = \Lambda^{\mu_1}{}_{\rho_1}\cdots\Lambda^{\mu_r}{}_{\rho_r}\,(\Lambda^{-1})^{\sigma_1}{}_{\nu_1}\cdots(\Lambda^{-1})^{\sigma_s}{}_{\nu_s}\,T^{\rho_1\cdots\rho_r}{}_{\sigma_1\cdots\sigma_s} :
> $$
>
> one factor $\Lambda$ per upper index and one $\Lambda^{-1}$ per lower index. For $\Lambda \in O(1,3)$, i.e. $\Lambda^{\mathsf T}g\Lambda = g$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]]), $(\Lambda^{-1})^\sigma{}_\nu = \Lambda_\nu{}^\sigma$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5, eqs. (covectortransform), (tensortransform) · the course's version: [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]] takes the Lorentz form of this law as the definition of a tensor*

^thm-cb-0-14

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
> **5. Lorentz.** For $\Lambda \in O(1,3)$, $(\Lambda^{-1})^\sigma{}_\nu = g^{\sigma\alpha}\Lambda^\beta{}_\alpha g_{\beta\nu} = \Lambda_\nu{}^\sigma$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]], 2).
>
> **What the derivation shows**
> - The law is not a convention: it is what multilinearity forces once vectors are moved by $\Lambda$; nothing Lorentz-specific was used until step 5.
> - The lecture's definition, "anything that transforms like $p^\mu q^\nu$", is the same law read backwards on products; the coefficient array $\Lambda^\mu{}_\lambda\Lambda^\nu{}_\sigma$ is a $16\times16$ matrix acting on the sixteen components.
> - Contraction, products, and raising and lowering then commute with $\Lambda$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-1|REL Theorem §B2.2.1]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]]), which is the covariance principle's toolkit ([[§B2.2 Tensors and the Covariance Principle#^pr-b2-2-9|REL Principle §B2.2.9]]).

^der-cb-0-14

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-13|Theorem §CB.0.13]]

> [!theorem] Theorem §CB.0.15: Trace, Determinant and Eigenvalues Do Not Depend on the Basis
> For $M \in \operatorname{End}(V)$ with matrices $M$ and $M' = UMU^{-1}$ in two bases ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]):
>
> $$
> \operatorname{tr}M' = \operatorname{tr}M, \qquad \det M' = \det M, \qquad \det(z\mathbb 1 - M') = \det(z\mathbb 1 - M) ,
> $$
>
> so the eigenvalues of $M$ with their multiplicities are properties of the operator, not of the basis ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR Thm. 8.50]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]], [[§37 Determinants#^ladr-9-63|LADR Def. 9.63]]). The trace is the contraction of the two slots of $M$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]).
>
> *Source: LADR Thm. 8.49, Thm. 8.50, Thm. 9.52, Def. 9.63*

^thm-cb-0-15

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

^der-cb-0-15

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]]

## The Levi-Civita symbol and the Pauli matrices

Two families of symbols used throughout CB: the Levi-Civita symbol (invariant tensors, the Lorentz algebra, duality) and the Pauli matrices ($\mathfrak{su}(2)$, $SU(2)$, the Clifford algebra of $\mathbb R^3$, $SL(2, \mathbb C)$). Their homes in the physics chapters are [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]], [[§B2.2 Tensors and the Covariance Principle|REL §B2.2]], [[§B6.1 Spin One-Half and the Pauli Matrices|QM §B6.1]] and [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]; they are restated here with their proofs so that CB rests on CB and the Math vault alone (CB ordering pass, 2026-10-08).

> [!definition] Definition §CB.0.16: The Levi-Civita Symbol
> In $n$ dimensions the **Levi-Civita symbol** $\varepsilon_{i_1\cdots i_n}$ is totally antisymmetric with $\varepsilon_{12\cdots n} = +1$: it equals $\operatorname{sgn}\pi$ if $(i_1, \dots, i_n) = (\pi(1), \dots, \pi(n))$ for a permutation $\pi$ ([[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|493 Def. §21.2]]), and $0$ if two indices coincide. In three Euclidean dimensions indices are raised and lowered with $\delta_{ij}$, so $\varepsilon^{ijk} = \varepsilon_{ijk}$, $\varepsilon_{123} = 1$. On Minkowski space ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]) the symbol is normalized by $\varepsilon^{0123} = +1$ and its indices are lowered with $g$, so $\varepsilon_{0123} = g_{00}g_{11}g_{22}g_{33}\,\varepsilon^{0123} = -1$, and $\varepsilon^{0ijk} = \varepsilon_{ijk}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Definition "The Levi-Civita symbol, and the convention of these notes") · PHY 513, Problem Set 1, Problem 3 · Yu §1.5, eq. (1.104) · the course's version: [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]] (the same normalization); Peskin–Schroeder use $\varepsilon^{0123} = -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]).*

^def-cb-0-16

> [!theorem] Theorem §CB.0.17: Contraction Identities of the Levi-Civita Symbol
> 1. (Minkowski, $\varepsilon^{0123} = +1$, [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]].) The product of two symbols is minus the determinant of deltas,
>
> $$
> \varepsilon_{\mu\nu\rho\sigma}\,\varepsilon^{\alpha\beta\gamma\delta} = -\det\begin{pmatrix} \delta^\alpha_\mu & \delta^\alpha_\nu & \delta^\alpha_\rho & \delta^\alpha_\sigma \\ \delta^\beta_\mu & \delta^\beta_\nu & \delta^\beta_\rho & \delta^\beta_\sigma \\ \delta^\gamma_\mu & \delta^\gamma_\nu & \delta^\gamma_\rho & \delta^\gamma_\sigma \\ \delta^\delta_\mu & \delta^\delta_\nu & \delta^\delta_\rho & \delta^\delta_\sigma \end{pmatrix} \equiv -\delta^{\alpha\beta\gamma\delta}_{\mu\nu\rho\sigma},
> $$
>
> and successive contractions give $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\beta\gamma\delta} = -\delta^{\beta\gamma\delta}_{\nu\rho\sigma}$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\gamma\delta} = -2\bigl(\delta^\gamma_\rho\delta^\delta_\sigma - \delta^\gamma_\sigma\delta^\delta_\rho\bigr)$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\delta} = -6\,\delta^\delta_\sigma$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = -24$.
> 2. (Euclidean three dimensions, $\varepsilon_{123} = 1$, all indices down.) $\varepsilon_{ijk}\varepsilon_{lmn} = \delta^{lmn}_{ijk}$ (no sign), $\ \varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$, $\ \varepsilon_{ijk}\varepsilon_{ijm} = 2\delta_{km}$, $\ \varepsilon_{ijk}\varepsilon_{ijk} = 6$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols"), eqs. (epseps4), (epseps2), (epseps3) · Yu §1.5, eqs. (1.106), (1.118)–(1.119) · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], the same identities.*

^thm-cb-0-17

> [!proof]- Proof
> *The derivation of Theorem §C1a.5.3, unchanged except for the citations.*
>
> **1. Both sides vanish together.** The left side vanishes if two of $\mu\nu\rho\sigma$ coincide, or two of $\alpha\beta\gamma\delta$. The determinant then has two equal columns, or two equal rows, and vanishes too ([[§37 Determinants#^ladr-9-45|LADR Thm. 9.45]]).
>
> **2. Distinct indices.** Otherwise $(\mu\nu\rho\sigma) = \tau(0123)$ and $(\alpha\beta\gamma\delta) = \pi(0123)$ for permutations $\tau$, $\pi$. The left side is $\operatorname{sgn}\tau\,\varepsilon_{0123}\cdot\operatorname{sgn}\pi\,\varepsilon^{0123} = -\operatorname{sgn}\tau\operatorname{sgn}\pi$, using $\varepsilon_{0123} = -1$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]). The matrix of deltas has exactly one entry $1$ in each row and column: it is a permutation matrix, of determinant $\operatorname{sgn}(\tau^{-1}\pi) = \operatorname{sgn}\tau\operatorname{sgn}\pi$ ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]). So the two sides agree, with the minus sign. ⚑ By-product: the overall sign is $\varepsilon_{0123}\varepsilon^{0123} = \det g = -1$, the Minkowski signature; in Euclidean signature it is $+1$ → part 2.
>
> **3. One contraction of a $k\times k$ delta in $n$ dimensions.** Expand $\delta^{\alpha\cdots}_{\mu\cdots}$ (first upper index $\alpha$, first lower $\mu$) along its first row: $\sum_j(-1)^{1+j}\delta^\alpha_{\lambda_j}M_{1j}$, where $\lambda_j$ is the $j$-th lower index and $M_{1j}$ the minor. Set $\alpha = \mu$ and sum. The term $j = 1$ gives $\delta^\mu_\mu M_{11} = n\,M_{11}$. For $j \ge 2$, $\delta^\mu_{\lambda_j}$ replaces $\mu$ by $\lambda_j$ in the first column of $M_{1j}$; moving that column from position 1 to position $j - 1$ takes $j - 2$ transpositions and turns $M_{1j}$ into $(-1)^{j-2}M_{11}$; with the sign $(-1)^{1+j}$ each such term is $-M_{11}$. There are $k - 1$ of them:
>
> $$
> \delta^{\mu\beta\cdots}_{\mu\nu\cdots} = (n - k + 1)\,\delta^{\beta\cdots}_{\nu\cdots} .
> $$
>
> **4. Successive contractions, $n = 4$.** $k = 4$: factor $1$, so $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\beta\gamma\delta} = -\delta^{\beta\gamma\delta}_{\nu\rho\sigma}$. $k = 3$: factor $2$, giving $-2\delta^{\gamma\delta}_{\rho\sigma} = -2(\delta^\gamma_\rho\delta^\delta_\sigma - \delta^\gamma_\sigma\delta^\delta_\rho)$. $k = 2$: factor $3$, giving $-6\delta^\delta_\sigma$. $k = 1$: $\delta^\sigma_\sigma = 4$, giving $-24 = -4!$. (Check of the last: $4!$ nonzero terms, each $(\pm1)(\mp1) = -1$.)
>
> **5. Three Euclidean dimensions.** Steps 1–3 with $n = 3$, $\varepsilon_{123}\varepsilon_{123} = +1$ (indices raised and lowered by $\delta_{ij}$, no signs): $\varepsilon_{ijk}\varepsilon_{lmn} = +\delta^{lmn}_{ijk}$; contracting $i = l$ gives factor $3 - 3 + 1 = 1$, i.e. $\delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ after renaming; then factor $2$, giving $2\delta_{km}$; then $\delta_{kk} = 3$, giving $6$.
>
> **What the proof shows**
> - Every Minkowski $\varepsilon\varepsilon$ identity is its Euclidean twin times $\det g = -1$.
> - Working rule: fix the convention for $\varepsilon_{0123}$ first; bring the contracted indices to the leading slots of both symbols by antisymmetry (one sign per transposition) before applying the identity.
> - Equivalence: this is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]] with its derivation; the physics section keeps the applications (the field tensor, three-vector notation).

^pf-cb-0-17

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]], [[§37 Determinants#^ladr-9-45|LADR Thm. 9.45]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]

> [!theorem] Theorem §CB.0.18: The Levi-Civita Symbol and the Determinant
> For every $4\times4$ matrix $A^\mu{}_\nu$, with $\varepsilon$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]:
> 1. $\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$;
> 2. $\det A = -\dfrac{1}{4!}\,\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta$;
> 3. if $\det A \ne 0$, $\ (A^{-1})^\nu{}_\mu = -\dfrac{1}{3!\,\det A}\,\varepsilon_{\mu\mu_2\mu_3\mu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4}A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4}$;
> 4. for four vectors, $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = -\det[a|b|c|d]$ (the matrix with columns $a^\mu, \dots, d^\mu$), which vanishes if and only if $a, b, c, d$ are linearly dependent.
>
> In Euclidean signature the minus signs in 2–4 are absent.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Levi-Civita and determinants"), eq. (epsdet) · Yu §1.5, eqs. (1.107)–(1.110) · the course's version: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], the same statement.*

^thm-cb-0-18

> [!proof]- Proof
> *The derivation of Theorem §C1a.5.4, unchanged except for the citations.*
>
> **1. Part 1.** Call the left side $L_{\alpha\beta\gamma\delta}$. Exchanging two of its free indices, say $\alpha \leftrightarrow \beta$, and renaming the dummies $\mu \leftrightarrow \nu$ gives back $L$ with $\varepsilon_{\nu\mu\rho\sigma} = -\varepsilon_{\mu\nu\rho\sigma}$: $L$ is totally antisymmetric, hence $L_{\alpha\beta\gamma\delta} = L_{0123}\,\varepsilon_{\alpha\beta\gamma\delta}/\varepsilon_{0123}$. And $L_{0123} = \varepsilon_{\mu\nu\rho\sigma}A^\mu{}_0A^\nu{}_1A^\rho{}_2A^\sigma{}_3 = \varepsilon_{0123}\sum_\pi\operatorname{sgn}\pi\,A^{\pi(0)}{}_0\cdots A^{\pi(3)}{}_3 = \varepsilon_{0123}\det A$ by the Leibniz formula ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]). So $L_{\alpha\beta\gamma\delta} = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$.
>
> **2. Part 2.** Contract part 1 with $\varepsilon^{\alpha\beta\gamma\delta}$ and use $\varepsilon_{\alpha\beta\gamma\delta}\varepsilon^{\alpha\beta\gamma\delta} = -24$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]]): $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha\cdots = -24\det A$.
>
> **3. Part 3.** Call the right side $B^\nu{}_\mu$ and compute $B^\nu{}_\mu A^\mu{}_\lambda$. By part 1 with the first slot filled by $A^\mu{}_\lambda$: $\varepsilon_{\mu\mu_2\mu_3\mu_4}A^\mu{}_\lambda A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4} = \det A\,\varepsilon_{\lambda\nu_2\nu_3\nu_4}$. Then $B^\nu{}_\mu A^\mu{}_\lambda = -\frac{1}{3!}\varepsilon_{\lambda\nu_2\nu_3\nu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4} = -\frac{1}{6}(-6\,\delta^\nu_\lambda) = \delta^\nu_\lambda$ by Theorem §CB.0.17. A left inverse of a square matrix is the inverse.
>
> **4. Part 4.** Put $A = [a|b|c|d]$, $A^\mu{}_0 = a^\mu$ etc., and $(\alpha\beta\gamma\delta) = (0123)$ in part 1: $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = \varepsilon_{0123}\det A = -\det A$. It vanishes iff $\det A = 0$ iff the columns are dependent ([[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]). ⚑ By-product: with all indices raised on $\varepsilon$ and lowered on the vectors the same number results, $\varepsilon^{\mu\nu\rho\sigma}a_\mu b_\nu c_\rho d_\sigma = \det[a_\mu|\cdots] = \det g\,\det[a|\cdots] = -\det[a|b|c|d]$: the signed four-volume of the parallelepiped spanned by $a, b, c, d$ is $-\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma$ in this convention. (The user's PHY 513 notes, Ch. 1 §1.5, item 3, write it without the minus sign; checked numerically.)
>
> **What the proof shows**
> - $\varepsilon$ is the antisymmetrizer, and the determinant is what antisymmetrizing a product of rows produces; the Minkowski minus signs are all $\varepsilon_{0123} = \det g$.
> - For $A = \Lambda$ preserving the metric, part 1 is the pseudotensor law of the Levi-Civita symbol (the course's version: [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]]; in CB: [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-14|Theorem §CB.7.14]]).
> - Equivalence: this is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] with its derivation.

^pf-cb-0-18

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]

> [!definition] Definition §CB.0.19: The Pauli Matrices
> The **Pauli matrices** are
>
> $$
> \sigma^1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma^2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma^3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
> $$
>
> $\boldsymbol\sigma = (\sigma^1, \sigma^2, \sigma^3)$, and for $\mathbf a \in \mathbb C^3$, $\mathbf a\cdot\boldsymbol\sigma = a_1\sigma^1 + a_2\sigma^2 + a_3\sigma^3$. The index is Euclidean: $\sigma_i = \sigma^i$.
>
> *Source: Griffiths §4.4.1, eq. (4.148) · PS §3.2, eq. (3.41) · Greensite §13.1, eqs. (13.46)–(13.47) · the course's version: [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], the same matrices written $\sigma_x, \sigma_y, \sigma_z$ (with $\mathbf S = \frac\hbar2\boldsymbol\sigma$ for spin ½).*

^def-cb-0-19

> [!definition] Definition §CB.0.20: The Matrices σ^μ and σ̄^μ
> With $\mathbb 1$ the $2\times2$ identity and the Pauli matrices $\boldsymbol\sigma$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]]),
>
> $$
> \sigma^\mu = (\mathbb 1, \boldsymbol\sigma), \qquad \bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma), \qquad \sigma_\mu = g_{\mu\nu}\sigma^\nu = (\mathbb 1, -\boldsymbol\sigma) .
> $$
>
> For $x \in \mathbb R^{1,3}$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]) write $X \equiv x_\mu\sigma^\mu = x^0\mathbb 1 - \mathbf x\cdot\boldsymbol\sigma$ and $\bar X \equiv x_\mu\bar\sigma^\mu = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$.
>
> *Source: PS §3.2, eq. (3.41) · Yu §5.2, eq. (5.74); Exercise 3.7, eq. (3.259) · PHY 513 Lecture 8, Part C ("Notation $\sigma^\mu = (1, \vec\sigma)$, $\bar\sigma^\mu = (1, -\vec\sigma)$") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit") · the course's version: [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], the same definition.*

^def-cb-0-20

> [!theorem] Theorem §CB.0.21: Algebra of the Pauli Matrices
> With $j, k, l \in \{1, 2, 3\}$, the Pauli matrices of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]] and the symbol $\varepsilon^{jkl}$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]:
> 1. **Product rule:** $\sigma^j\sigma^k = \delta^{jk}\,\mathbb 1 + i\varepsilon^{jkl}\sigma^l$. In particular $(\sigma^j)^2 = \mathbb 1$, $\sigma^1\sigma^2 = i\sigma^3$ (and cyclically), and $\sigma^j\sigma^k + \sigma^k\sigma^j = 2\delta^{jk}\mathbb 1$.
> 2. **Commutators:** $[\sigma^j, \sigma^k] = 2i\varepsilon^{jkl}\sigma^l$.
> 3. **Vector form:** $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)\,\mathbb 1 + i\,(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$ for vectors with commuting components; for a unit vector $\hat{\mathbf n}$, $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \mathbb 1$.
> 4. **Basis:** each $\sigma^j$ is Hermitian with trace $0$ and eigenvalues $\pm1$; $\mathbb 1, \sigma^1, \sigma^2, \sigma^3$ form a basis of the complex $2\times2$ matrices; a $2\times2$ matrix is Hermitian iff it is $a_0\mathbb 1 + \mathbf a\cdot\boldsymbol\sigma$ with $a_0, \mathbf a$ real, and traceless Hermitian iff $a_0 = 0$.
> 5. **Traces:** $\operatorname{tr}(\sigma^j\sigma^k) = 2\delta^{jk}$.
>
> *Source: Griffiths Problem 4.29, eq. (4.153) · Greensite §13.1 · the course's version: [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], parts 1–4 the same (with $\mathbf S = \frac\hbar2\boldsymbol\sigma$ there); part 5 added here.*

^thm-cb-0-21

> [!proof]- Proof
> *Adapted from the derivation of QM Theorem §B6.1.4 (indices $1, 2, 3$ for $x, y, z$); part 5 added.*
>
> **1. Product rule.** Multiply the matrices: $(\sigma^1)^2 = (\sigma^2)^2 = (\sigma^3)^2 = \mathbb 1$ by inspection, and
>
> $$
> \sigma^1\sigma^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i\sigma^3, \qquad
> \sigma^2\sigma^1 = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = -i\sigma^3 ;
> $$
>
> the products $\sigma^2\sigma^3 = i\sigma^1$, $\sigma^3\sigma^1 = i\sigma^2$ and their reverses follow the same way. These nine products are the product rule. Adding $\sigma^j\sigma^k$ and $\sigma^k\sigma^j$, the $\varepsilon$ terms cancel ($\varepsilon^{kjl} = -\varepsilon^{jkl}$) and the $\delta$ terms double.
>
> **2. Commutators.** Subtract $\sigma^k\sigma^j$ from $\sigma^j\sigma^k$: the $\delta^{jk}$ terms cancel and the $\varepsilon$ terms double, since $\varepsilon^{kjl} = -\varepsilon^{jkl}$.
>
> **3. Vector form.** $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = \sum_{j,k}a_jb_k\sigma^j\sigma^k = \sum_ja_jb_j\,\mathbb 1 + i\sum_l\bigl(\sum_{j,k}\varepsilon^{jkl}a_jb_k\bigr)\sigma^l$, and the bracket is $(\mathbf a\times\mathbf b)_l$. With $\mathbf a = \mathbf b = \hat{\mathbf n}$ the cross product vanishes and $\hat{\mathbf n}\cdot\hat{\mathbf n} = 1$.
>
> **4. Basis.** Hermiticity and the trace are read off. $(\sigma^j)^2 = \mathbb 1$ forces eigenvalues $\pm1$, and trace $0$ forces one of each. A general matrix $\begin{pmatrix} p & q \\ r & t\end{pmatrix}$ equals $\tfrac{p+t}2\mathbb 1 + \tfrac{q+r}2\sigma^1 + \tfrac{i(q-r)}2\sigma^2 + \tfrac{p-t}2\sigma^3$, uniquely, so the four matrices are a basis; the coefficients are real exactly when $p, t$ are real and $r = \bar q$, that is, when the matrix is Hermitian ([[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR Def. 7.10]]); its trace is $2a_0$.
>
> **5. Traces.** By part 1, $\operatorname{tr}(\sigma^j\sigma^k) = \delta^{jk}\operatorname{tr}\mathbb 1 + i\varepsilon^{jkl}\operatorname{tr}\sigma^l = 2\delta^{jk}$, using $\operatorname{tr}\sigma^l = 0$ (part 4).
>
> **What the proof shows**
> - Part 1 is the Clifford relation of $\mathbb R^3$ for the $\sigma^j$ together with their products; the Clifford reading is [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.14]].
> - Part 4 says that $\mathbf x \mapsto \mathbf x\cdot\boldsymbol\sigma$ identifies $\mathbb R^3$ with the traceless Hermitian $2\times2$ matrices, the dictionary of $SU(2) \to SO(3)$ (§CB.1).
> - Equivalence: parts 1–4 are [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 1–4, where part 2 is read as the spin commutation relations.

^pf-cb-0-21

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR Def. 7.10]]

> [!theorem] Theorem §CB.0.22: Identities of σ^μ and σ̄^μ
> For $\sigma^\mu$, $\bar\sigma^\mu$, $X$, $\bar X$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]:
> 1. $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$.
> 2. $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1$ and $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu = 2g^{\mu\nu}\mathbb 1$; in particular $X\bar X = \bar XX = x^2\,\mathbb 1$.
> 3. $\sigma^2(\sigma^\mu)^*\sigma^2 = \bar\sigma^\mu$ and $\sigma^2(\bar\sigma^\mu)^*\sigma^2 = \sigma^\mu$; equivalently $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$.
>
> *Source: Yu Exercise 3.7, eq. (3.260) (the inverse $x^\mu = \frac12\operatorname{tr}(X\bar\sigma^\mu)$, which is part 1) · the user's PHY 513 notes, Ch. 8 §8.2 ("from $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$ the inverse is …") · PS eq. (3.38) (part 3 for $\boldsymbol\sigma$) · the course's version: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], the same statement.*

^thm-cb-0-22

> [!proof]- Proof
> *The derivation of Theorem §C5a.1.1, unchanged except for the citations.* The only input is the Pauli product rule $\sigma^i\sigma^j = \delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k$, with $\operatorname{tr}\sigma^i = 0$ and $\operatorname{tr}\mathbb 1 = 2$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]). Latin indices run over $1, 2, 3$.
>
> **1. Trace, by cases.** $(\mu, \nu) = (0, 0)$: $\operatorname{tr}(\mathbb 1\cdot\mathbb 1) = 2 = 2g^{00}$. $(0, j)$: $\operatorname{tr}(\mathbb 1\cdot(-\sigma^j)) = 0 = 2g^{0j}$. $(i, 0)$: $\operatorname{tr}(\sigma^i\cdot\mathbb 1) = 0$. $(i, j)$: $\operatorname{tr}(\sigma^i(-\sigma^j)) = -\operatorname{tr}(\delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k) = -2\delta^{ij} = 2g^{ij}$.
>
> **2. Anticommutators, by cases.** For $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu$: $(0, 0)$ gives $\mathbb 1 + \mathbb 1 = 2g^{00}\mathbb 1$; $(0, j)$ gives $\mathbb 1(-\sigma^j) + \sigma^j\mathbb 1 = 0$; $(i, j)$ gives $-\sigma^i\sigma^j - \sigma^j\sigma^i = -2\delta^{ij}\mathbb 1 = 2g^{ij}\mathbb 1$, because the $i\varepsilon^{ijk}\sigma^k$ terms of the two products are opposite ($\varepsilon^{jik} = -\varepsilon^{ijk}$). For $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu$ the same three cases give $2\mathbb 1$, $(-\sigma^j) + \sigma^j = 0$ and $-2\delta^{ij}\mathbb 1$.
>
> **3. X X̄.** $X\bar X = x_\mu x_\nu\sigma^\mu\bar\sigma^\nu$. The coefficient $x_\mu x_\nu$ is symmetric in $\mu\nu$, so only the symmetric part of $\sigma^\mu\bar\sigma^\nu$ survives: $x_\mu x_\nu\sigma^\mu\bar\sigma^\nu = \frac12x_\mu x_\nu(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu) = x_\mu x_\nu g^{\mu\nu}\mathbb 1 = x^2\mathbb 1$ by step 2. The same for $\bar XX$.
>
> **4. Conjugation by σ².** $\sigma^1$ and $\sigma^3$ are real and $\sigma^2$ is imaginary, so $(\sigma^1)^{\ast} = \sigma^1$, $(\sigma^2)^{\ast} = -\sigma^2$, $(\sigma^3)^{\ast} = \sigma^3$. Since $(\sigma^2)^2 = \mathbb 1$ and $\sigma^2$ anticommutes with $\sigma^1, \sigma^3$: $\sigma^2\sigma^1\sigma^2 = -\sigma^1(\sigma^2)^2 = -\sigma^1$, $\sigma^2(-\sigma^2)\sigma^2 = -\sigma^2$, $\sigma^2\sigma^3\sigma^2 = -\sigma^3$. So $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$ for each $i$ (PS (3.38)), while $\sigma^2\mathbb 1^{\ast}\sigma^2 = \mathbb 1$. Hence $\sigma^2(\sigma^\mu)^{\ast}\sigma^2 = (\mathbb 1, -\boldsymbol\sigma) = \bar\sigma^\mu$, and conjugating $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ the same way gives $(\mathbb 1, \boldsymbol\sigma) = \sigma^\mu$.
>
> **What the proof shows**
> - Part 2 is a "Clifford algebra" for the pair $(\sigma, \bar\sigma)$: neither set alone squares to $g$, but $\sigma$ followed by $\bar\sigma$ does; stacking them into a $4\times4$ matrix gives the chiral Dirac matrices (the course's [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]).
> - Part 3 is the matrix form of "complex conjugation exchanges the two Weyl representations" ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13|Theorem §CB.16.13]]).
> - Equivalence: this is [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]] with its derivation.

^pf-cb-0-22

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]

> [!remark]- Connections
> - The transformation rules of spinors and $\gamma$ matrices are the change-of-basis formula of linear algebra, $A = C^{-1}BC$ for operators and its dual and conjugate versions for covectors and forms; nothing specific to physics enters until the Clifford action — [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], [[§12 Duality#^ladr-3-112|LADR Def. 3.112]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]].
> - The real case with a metric, where an index is raised and lowered instead of being a separate slot, is the spacetime index calculus — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]], [[§CB.7 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-7-9|Theorem §CB.7.9]].
> - **Used in**: Definition §CB.0.1 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.2 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Theorem §CB.0.3 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.4 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]); Theorem §CB.0.5 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-2|§C5a.5, Caution: Bases and conventions across the sources]], [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]]); §CB.0, Remark: Why "UψU⁻¹" means nothing — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); §CB.0, Caution: Which matrix is called U — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]); Definition §CB.0.6 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.2 The Dirac Form|§C5a.2]] (embedded; cited in [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]); Definition §CB.0.7 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded; cited in [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]]); Definition §CB.0.8 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Definition §CB.0.9 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded); Theorem §CB.0.10 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded); Theorem §CB.0.14 — [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded; cited in [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]), [[§C1a.7 Relativistic Electrodynamics in Index Form|§C1a.7]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]); Theorem §CB.0.15 — [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] (embedded), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]).
