---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.2 The Dirac Form]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–44, eqs. (3.22)–(3.25), (3.41)–(3.42), and §3.4, p. 50 · the user's PHY 513 notes, Ch. 8 §8.1 (The Dirac representation: Definition "The Dirac (Clifford) algebra", paragraphs "Square to ±1, or square root?" and "Uniqueness (Pauli's fundamental theorem)", Derivations "Checking the Dirac algebra in the chiral basis" and "Hermiticity of the Dirac matrices"), §8.2 (Derivation "The double cover made explicit"), §8.3 (What each spinor index labels) · PHY 513 Lecture 7 (Larsen), Part B ("There are many realizations of $\gamma^\mu$"); Lecture 8, Cheat Sheet I and Part C · PHY 513, Problem Set 5, Problem 5 (as the user wrote it; submitted) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.1)–(5.7), (5.45), §5.2, eqs. (5.68)–(5.75), Exercise 3.7, eqs. (3.259)–(3.260) · the user's pre-course notes, §5.1–§5.2 · Axler, Linear Algebra Done Right (the vault's Linear Algebra notes), linked where used · the basis-free organization written here · PHY 513, Problem Set 6, Problem 3(a) (the user's solution).*

What is a Dirac spinor before anyone writes a column of four numbers, and what do the $\gamma$ matrices add to it? A spinor is first of all a vector of a four-dimensional complex vector space $V$; everything else is structure added on top, one layer at a time (the map is [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]]). This section builds the first two layers. **Layer 1** is $V$ itself with its bases: components, matrices of linear maps, and the change-of-basis rules, which are the change-of-basis formula of linear algebra and nothing more ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]]), with the slot rule that decides which factor each index receives. **Layer 2** is the Clifford action: four linear maps $\Gamma^\mu$ on $V$ with $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}$, whose matrices in a basis are the Dirac matrices; their first consequences, the sixteen products, the eigenvalues, the chiral basis as one choice, Hermiticity, and Pauli's theorem, which says that spinor space with its Clifford action is unique and that a choice of $\gamma$ matrices is a choice of basis. The Dirac matrices of Quantum Mechanics enter here as one such choice ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]). The Dirac form, the Lorentz action and chirality are the next layers ([[§C5a.2 The Dirac Form|§C5a.2]]–[[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]).

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis when a basis is fixed; spinor indices are Latin $a, b, c, d \in \{1, 2, 3, 4\}$, never raised or lowered, all written as subscripts, contracted by plain sums; spacetime indices Greek ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]]). Operators on $V$ are written $\Gamma^\mu$, $M$, …, their matrices $\gamma^\mu$, …; $\operatorname{End}(V)$ is the space of linear maps $V \to V$ (Axler's $\mathcal L(V)$). The identity matrix in $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ is usually not written. Pauli matrices $\boldsymbol\sigma = (\sigma^1, \sigma^2, \sigma^3)$, with the product rule of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]. $\psi$ is a c-number spinor or a classical field (no hat); the quantum field is $\hat\psi$.

*Why spinor space and the $\gamma$'s are needed at all, what the Clifford relation induces, the four jobs of the $\gamma$'s, and the layer-by-layer map of the chapter: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]].*

## Spinor space and its bases

> [!definition] Definition §C5a.1.1: Spinor Space
> **Spinor space** is a complex vector space $V$ of dimension $4$ ([[§2 Definition of Vector Space#^ladr-1-20|LADR Def. 1.20]]). A **Dirac spinor** (at one point) is an element $\psi \in V$.
>
> *Source: Yu §5.2, eq. (5.55) (the spinor as a vector of the representation space) · the user's pre-course notes, §5.2 (Note "Four linear spaces": "the spinor representation space (4-dim, elements $\psi_a$)") · the user's PHY 513 notes, Ch. 8 §8.3 (table: "$\psi_a$: a vector in spinor space $\mathbb C^4$") · the basis-free formulation written here*

^def-c5a-1-1

> [!remark] Remark: What this layer contains, and what it does not
> At this layer $V$ is only a vector space: spinors can be added and multiplied by complex numbers, and nothing else. It has no preferred basis (so no "upper" and "lower" components), no inner product (so no $\psi^\dagger\psi$ that means anything), no Lorentz action and no $\gamma$ matrices. Each later layer adds one structure: the Clifford action $\Gamma^\mu$ (later in this section), a Hermitian form ([[§C5a.2 The Dirac Form|§C5a.2]]), the Lorentz action and its relation to $\Gamma^\mu$ ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). The column $\mathbb C^4$ of the lecture appears only after a basis is chosen, and every statement about it has to be checked for independence of that choice.
>
> *Source: written here, organizing PS §3.2, pp. 40–42 and the user's PHY 513 notes, Ch. 8 §8.3*

^rem-c5a-1-2

> [!definition] Definition §C5a.1.2: Components of a Spinor in a Basis
> Let $e = (e_1, e_2, e_3, e_4)$ be a basis of spinor space $V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]; bases, [[§5 Bases#^ladr-2-26|LADR Def. 2.26]]). The **components** $\psi_a$ of $\psi \in V$ are the unique numbers with
>
> $$
> \psi = \sum_{a=1}^4\psi_a\,e_a ,
> $$
>
> and the column $(\psi_1, \psi_2, \psi_3, \psi_4)^{\mathsf T} \in \mathbb C^4$ is the matrix of $\psi$ in that basis ([[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR Def. 3.73]]). The column is also written $\psi$ when the basis is fixed.
>
> *Source: LADR Def. 3.73 · Yu §5.2, eq. (5.55)*

^def-c5a-1-2

> [!definition] Definition §C5a.1.3: The Matrix of a Linear Map on Spinor Space
> For a linear map $M \in \operatorname{End}(V)$ and a basis $e$ of $V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]), the **matrix** of $M$ is the $4\times4$ array $(M_{ab})$ with
>
> $$
> M\,e_b = \sum_{a=1}^4 M_{ab}\,e_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the components of $Me_b$ ([[§9 Matrices#^ladr-3-31|LADR Def. 3.31]]). The first index is the row, the second the column.
>
> *Source: LADR Def. 3.31*

^def-c5a-1-3

> [!theorem] Theorem §C5a.1.1: Linear Maps Act by Matrix Multiplication
> In a fixed basis of $V$ (with [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), for $M, N \in \operatorname{End}(V)$, $\psi \in V$, $\lambda \in \mathbb C$:
>
> $$
> (M\psi)_a = \sum_b M_{ab}\psi_b, \qquad (MN)_{ab} = \sum_c M_{ac}N_{cb}, \qquad (M + \lambda N)_{ab} = M_{ab} + \lambda N_{ab}, \qquad (\mathrm{id})_{ab} = \delta_{ab} .
> $$
>
> So "an operator acting on a spinor" is a matrix times a column, and every algebraic identity among operators holds verbatim among their matrices.
>
> *Source: [[§10 Invertibility and Isomorphisms#^ladr-3-76|LADR Thm. 3.76]], [[§9 Matrices#^ladr-3-43|LADR Thm. 3.43]], [[§9 Matrices#^ladr-3-35|LADR Thm. 3.35]] · Yu §5.2, eq. (5.56) ("the product on the right is a matrix times a column vector")*

^thm-c5a-1-1

> [!derivation]- Derivation
> **1. Action.** $M\psi = M\bigl(\sum_b\psi_be_b\bigr) = \sum_b\psi_b\,Me_b$ (linearity of $M$) $= \sum_b\psi_b\sum_aM_{ab}e_a$ (Def. §C5a.1.3) $= \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a$ (exchange of two finite sums). Components are unique (Def. §C5a.1.2), so $(M\psi)_a = \sum_bM_{ab}\psi_b$.
>
> **2. Product.** $(MN)e_b = M(Ne_b) = M\bigl(\sum_cN_{cb}e_c\bigr) = \sum_cN_{cb}\sum_aM_{ac}e_a = \sum_a\bigl(\sum_cM_{ac}N_{cb}\bigr)e_a$; read off the coefficient of $e_a$.
>
> **3. Sum and identity.** $(M + \lambda N)e_b = \sum_a(M_{ab} + \lambda N_{ab})e_a$; $\mathrm{id}\,e_b = e_b = \sum_a\delta_{ab}e_a$.
>
> **What the derivation shows**
> - Only linearity and the uniqueness of components are used: the matrix calculus of the lecture is the calculus of $\operatorname{End}(V)$ written in one basis.
> - Used next: in a new basis the same operator has a new matrix (Theorem §C5a.1.2), and the Clifford relation survives in every basis (Theorem §C5a.1.7).

^der-c5a-1-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]

> [!definition] Definition §C5a.1.4: The Change-of-Basis Matrix
> Let $e$ (old) and $e'$ (new) be two bases of $V$. The **change-of-basis matrix** $U$ is the $4\times4$ matrix with
>
> $$
> e_b = \sum_{a=1}^4U_{ab}\,e'_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the new components of the old basis vector $e_b$. In Axler's notation $U = \mathcal M(\mathrm{id}, (e), (e'))$, and it is invertible, with $e'_b = \sum_a(U^{-1})_{ab}\,e_a$ ([[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]).
>
> *Source: LADR Thm. 3.82, Thm. 3.84 (its matrix $C$) · the convention for $U$ fixed here so that $\gamma'^\mu = U\gamma^\mu U^{-1}$, as in Theorem §C5a.1.12 and the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness"); other conventions: Caution below*

^def-c5a-1-4

> [!theorem] Theorem §C5a.1.2: Components Change with U, Matrices with U and U⁻¹
> With the change-of-basis matrix $U$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), for every $\psi \in V$ and $M \in \operatorname{End}(V)$:
>
> $$
> \psi'_a = \sum_bU_{ab}\,\psi_b, \quad\text{i.e.}\quad \psi' = U\psi ; \qquad M'_{ab} = \sum_{c,d}U_{ac}\,M_{cd}\,(U^{-1})_{db}, \quad\text{i.e.}\quad M' = UMU^{-1} .
> $$
>
> One index, one $U$; a row index gets $U$ from the left, a column index $U^{-1}$ from the right. This is the change-of-basis formula of linear algebra ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], whose $A = C^{-1}BC$ is $M = U^{-1}M'U$).
>
> *Source: LADR Thm. 3.76, Thm. 3.84 · Yu §5.2, eq. (5.72) (the similarity transformation, in the opposite naming of $U$) · the index-by-index derivation written here*

^thm-c5a-1-2

> [!derivation]- Derivation
> **1. The inverse relation.** Claim $e'_b = \sum_a(U^{-1})_{ab}e_a$. Insert $e_a = \sum_dU_{da}e'_d$ (Def. §C5a.1.4) into the right side: $\sum_a(U^{-1})_{ab}\sum_dU_{da}e'_d = \sum_d\bigl(\sum_aU_{da}(U^{-1})_{ab}\bigr)e'_d = \sum_d(UU^{-1})_{db}e'_d = \sum_d\delta_{db}e'_d = e'_b$. ($U$ is invertible because the matrix of the identity from $e'$ back to $e$ is its inverse, LADR Thm. 3.82.)
>
> **2. Components.** $\psi = \sum_b\psi_be_b$ (old components) $= \sum_b\psi_b\sum_aU_{ab}e'_a$ (Def. §C5a.1.4) $= \sum_a\bigl(\sum_bU_{ab}\psi_b\bigr)e'_a$. The new components are unique (Def. §C5a.1.2), so $\psi'_a = \sum_bU_{ab}\psi_b$.
>
> **3. Matrices.** Apply $M$ to a new basis vector and express everything in the new basis:
>
> $$
> Me'_b \overset{(1)}{=} \sum_c(U^{-1})_{cb}\,Me_c \overset{\text{Def. 9.3}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\,e_d \overset{\text{Def. 9.4}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\sum_aU_{ad}\,e'_a = \sum_a\Bigl(\sum_{d,c}U_{ad}M_{dc}(U^{-1})_{cb}\Bigr)e'_a .
> $$
>
> By Def. §C5a.1.3 in the new basis the bracket is $M'_{ab}$, and it is the $(a, b)$ entry of the triple product $UMU^{-1}$ (Theorem §C5a.1.1, product rule twice).
>
> **4. Consistency check.** $(M\psi)' = U(M\psi) = UMU^{-1}U\psi = M'\psi'$: computing $M\psi$ in either basis gives the same vector of $V$.
>
> **What the derivation shows**
> - The rules are not physics: they are the bookkeeping of one vector and one linear map in two bases. $\psi$ has one $V$-index, hence one factor $U$; $M$ has a row index (a $V$-slot) and a column index (contracted with $\psi$), hence $U$ on the left and $U^{-1}$ on the right. Which kind of index gets which factor is the slot rule (Theorem §C5a.1.3).
> - Used next: the Dirac matrices are matrices of operators (Theorem §C5a.1.7), so $\gamma'^\mu = U\gamma^\mu U^{-1}$ is this theorem, not an additional rule.

^der-c5a-1-2

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]

> [!remark] Remark: Why "UψU⁻¹" means nothing
> $\psi$ is a $4\times1$ column and $U$ a $4\times4$ matrix: $U\psi$ is a column, but $\psi U^{-1}$ is a $4\times1$ times a $4\times4$, which is not defined. The shape reflects the slot count: a spinor has one $V$-slot, so it takes one factor (Theorem §C5a.1.2); only objects with two spinor slots, such as $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$ or $\psi\bar\chi$ (a column times a row, $4\times4$), take the sandwich. A sandwich $U^{-1}\hat\psi U$ does occur in field theory, with the unitary operator $U(\Lambda)$ on the Hilbert space; it acts on the operator nature of $\hat\psi$, not on its spinor index (Caution: Three different transformations, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]).
>
> *Source: written here · the user's PHY 513 notes, Ch. 10 §10.3 ("The operator carries the quantum, particle-like aspect; the column and the plane wave carry the wave aspect and all the Lorentz structure")*

^rem-c5a-1-3

> [!caution] Caution: Which matrix is called U
> Here $U$ converts old components into new ones, $\psi' = U\psi$, $\gamma' = U\gamma U^{-1}$, as in Pauli's theorem ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]), the user's PHY 513 notes and the matrix of [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] (there old = Dirac basis, new = chiral basis). Yu (5.72) writes $\gamma'^\mu = U^\dagger\gamma^\mu U$ with $U$ unitary, so Yu's $U$ is the inverse of this one; Axler's $C$ in LADR Thm. 3.84 is this $U$; Sakurai's transformation matrix gives (new) $= U^\dagger$(old), again the inverse ([[§C1.4 Change of Basis and Unitary Equivalence#^cau-c1-4-1|QM, Caution: Which matrix is called U]]). Larsen's $U_D$ (Problem Set 6, Problem 3(b)) converts chiral (old) into Dirac (new) components, $\psi_D = U_D\psi$, $\gamma_D^\mu = U_D\gamma^\mu U_D^\dagger$: it follows this convention, and it is the inverse $U^\dagger$ of the matrix of Example §C5a.5.1, which runs from the Dirac to the chiral basis (the relation is stated there). Before using a formula, check which basis labels the rows of the source's $U$.
>
> *Source: Yu §5.2, eq. (5.72) · LADR Thm. 3.84 · Sakurai §1.5.2 (as recorded in QM C1.4) · PHY 513, Problem Set 6, Problem 3(b) (statement: $U_D$)*

^cau-c5a-1-1

## Slots: covectors, operators and the index rule

> [!definition] Definition §C5a.1.5: Dual Spinor Space and Dual Basis
> The **dual spinor space** $V'$ is the space of linear functionals $\varphi : V \to \mathbb C$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]). The **dual basis** $(\varepsilon^1, \dots, \varepsilon^4)$ of a basis $e$ is defined by $\varepsilon^a(e_b) = \delta_{ab}$ ([[§12 Duality#^ladr-3-112|LADR Def. 3.112]]). The **components** of $\varphi \in V'$ are $\varphi_a \equiv \varphi(e_a)$, written as a row $(\varphi_1, \dots, \varphi_4)$; then $\varphi = \sum_a\varphi_a\varepsilon^a$ and $\varphi(\psi) = \sum_a\varphi_a\psi_a$, a row times a column.
>
> *Source: LADR Def. 3.110, Def. 3.112, Thm. 3.114 · the row picture: the user's PHY 513 notes, Ch. 8 §8.3 ("contracting them is plain matrix multiplication")*

^def-c5a-1-5

> [!definition] Definition §C5a.1.6: Spinor Tensors and Their Slots
> A **spinor tensor of type $(k, l)$** is an element of $V^{\otimes k}\otimes V'^{\otimes l}$ ([[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]; $V'$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-5|Def. §C5a.1.5]]): it has $k$ **$V$-slots** and $l$ **$V'$-slots**. In a basis $e$ with dual basis $\varepsilon$ its **components** $T_{a_1\dots a_k;\,b_1\dots b_l}$ are the coefficients of $e_{a_1}\otimes\dots\otimes e_{a_k}\otimes\varepsilon^{b_1}\otimes\dots\otimes\varepsilon^{b_l}$. A **contraction** sets one $V$-index equal to one $V'$-index and sums. Examples: a spinor $\psi$ is type $(1, 0)$, a row $\varphi$ type $(0, 1)$, a linear map $M \in \operatorname{End}(V)$ type $(1, 1)$ through $M = \sum_{a,b}M_{ab}\,e_a\otimes\varepsilon^b$, a number type $(0, 0)$.
>
> *Source: LADR Def. 9.71, Def. 9.88 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "transforming all of its indices at once, each by the rule of its own slot") · the identification $\operatorname{End}(V) \cong V\otimes V'$ written here (Derivation §C5a.1.3, step 2)*

^def-c5a-1-6

> [!theorem] Theorem §C5a.1.3: The Slot Rule
> Under a change of basis with matrix $U$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), the components of a spinor tensor ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-6|Def. §C5a.1.6]]) change by one factor per slot:
>
> $$
> T'_{a_1\dots a_k;\,b_1\dots b_l} = \sum U_{a_1c_1}\cdots U_{a_kc_k}\;T_{c_1\dots c_k;\,d_1\dots d_l}\;(U^{-1})_{d_1b_1}\cdots(U^{-1})_{d_lb_l} ,
> $$
>
> $U$ for each $V$-slot, $U^{-1}$ (from the right) for each $V'$-slot. In particular a row transforms as $\varphi' = \varphi U^{-1}$, an operator as $M' = UMU^{-1}$ (agreeing with [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]), and a contraction of a $V$-slot with a $V'$-slot removes both factors: a fully contracted expression is the same number in every basis.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"; "The practical test, continued") · LADR Thm. 9.73 (multilinearity of ⊗) · the general rule and its derivation written here*

^thm-c5a-1-3

> [!derivation]- Derivation
> **1. The dual basis.** Expand $\varepsilon^b$ in the new dual basis $\varepsilon'$: its coefficients are its values on the new basis vectors (LADR Thm. 3.114 applied in $V'$). By step 1 of Derivation §C5a.1.2, $\varepsilon^b(e'_c) = \varepsilon^b\bigl(\sum_d(U^{-1})_{dc}e_d\bigr) = \sum_d(U^{-1})_{dc}\delta_{bd} = (U^{-1})_{bc}$, so $\varepsilon^b = \sum_c(U^{-1})_{bc}\,\varepsilon'^c$.
>
> **2. Operators as tensors.** The matrix units $E^{(ab)} \equiv e_a\otimes\varepsilon^b$ act as $\psi \mapsto \varepsilon^b(\psi)\,e_a = \psi_b\,e_a$. Then $\sum_{a,b}M_{ab}\,\varepsilon^b(\psi)\,e_a = \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a = M\psi$ (Theorem §C5a.1.1), so $M = \sum M_{ab}\,e_a\otimes\varepsilon^b$. The sixteen $E^{(ab)}$ span $\operatorname{End}(V)$ by this formula and are independent (apply to $e_c$), and $\dim(V\otimes V') = 16$ ([[§38 Tensor Products#^ladr-9-72|LADR Thm. 9.72]]): $\operatorname{End}(V) \cong V\otimes V'$.
>
> **3. One factor per slot.** Insert $e_{c} = \sum_aU_{ac}e'_{a}$ (Def. §C5a.1.4) into every $V$-slot and $\varepsilon^{d} = \sum_b(U^{-1})_{db}\varepsilon'^{b}$ (step 1) into every $V'$-slot of $T = \sum T_{c_1\dots;\,d_1\dots}\,e_{c_1}\otimes\dots\otimes\varepsilon^{d_1}\otimes\dots$. The tensor product is linear in each factor (LADR Thm. 9.73), so the factors pull out of each slot separately, and the coefficient of $e'_{a_1}\otimes\dots\otimes\varepsilon'^{b_1}\otimes\dots$ is the displayed formula.
>
> **4. The cases.** Type $(0, 1)$: $\varphi'_b = \sum_d\varphi_d(U^{-1})_{db}$, i.e. $\varphi' = \varphi U^{-1}$; also directly, $\varphi'_b = \varphi(e'_b) = \sum_d(U^{-1})_{db}\varphi(e_d)$. Type $(1, 1)$: $M'_{ab} = \sum U_{ac}M_{cd}(U^{-1})_{db}$, Theorem §C5a.1.2 again.
>
> **5. Contraction.** Contract a $V$-index $a$ with a $V'$-index $b$ of $T'$: the two factors become $\sum_aU_{ac}(U^{-1})_{da} = (U^{-1}U)_{dc} = \delta_{dc}$, so the contracted components transform with the remaining slots only. With every slot contracted, nothing remains: $\varphi'\psi' = \varphi U^{-1}U\psi = \varphi\psi$, $\varphi'M'\psi' = \varphi M\psi$.
>
> **What the derivation shows**
> - The "index rule" of the course (one $U$ per index, sandwiches for matrices, invariant scalars) is the transformation law of tensor components, with $V$ and $V'$ as the two kinds of slot. It needs no physics and no metric.
> - ⚑ By-product: $\psi^\dagger$ is *not* a $V'$-slot. Its components $\psi_a^{\ast}$ transform as $(\psi')^{\ast} = U^{\ast}\psi^{\ast}$, i.e. the row $\psi'^\dagger = \psi^\dagger U^\dagger$, which is the $V'$-rule $\psi^\dagger U^{-1}$ only when $U^\dagger = U^{-1}$ → Theorem §C5a.2.4. The row that *is* a $V'$-slot for every $U$ is $\bar\psi$, once defined basis-free (Def. §C5a.2.5).
> - Used next: trace and eigenvalues (Theorem §C5a.1.4); the table in the remark below.

^der-c5a-1-3

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-5|Def. §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-6|Def. §C5a.1.6]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§12 Duality#^ladr-3-114|LADR Thm. 3.114]], [[§38 Tensor Products#^ladr-9-73|LADR Thm. 9.73]]

> [!theorem] Theorem §C5a.1.4: Trace, Determinant and Eigenvalues Do Not Depend on the Basis
> For $M \in \operatorname{End}(V)$ with matrices $M$ and $M' = UMU^{-1}$ in two bases ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]):
>
> $$
> \operatorname{tr}M' = \operatorname{tr}M, \qquad \det M' = \det M, \qquad \det(z\mathbb 1 - M') = \det(z\mathbb 1 - M) ,
> $$
>
> so the eigenvalues of $M$ with their multiplicities are properties of the operator, not of the basis ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR Thm. 8.50]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]], [[§37 Determinants#^ladr-9-63|LADR Def. 9.63]]). The trace is the contraction of the two slots of $M$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]]).
>
> *Source: LADR Thm. 8.49, Thm. 8.50, Thm. 9.52, Def. 9.63*

^thm-c5a-1-4

> [!derivation]- Derivation
> **1. Trace.** $\operatorname{tr}(UMU^{-1}) = \operatorname{tr}\bigl((UM)U^{-1}\bigr) = \operatorname{tr}\bigl(U^{-1}(UM)\bigr) = \operatorname{tr}M$, by $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]). As a contraction: $\operatorname{tr}M = \sum_aM_{aa}$ contracts the $V$-slot with the $V'$-slot (step 5 of Derivation §C5a.1.3).
>
> **2. Determinant.** $\det(UMU^{-1}) = \det M$ (LADR Thm. 9.52 with $S = U^{-1}$).
>
> **3. Characteristic polynomial.** $z\mathbb 1 - UMU^{-1} = U(z\mathbb 1 - M)U^{-1}$, because $U(z\mathbb 1)U^{-1} = z\mathbb 1$. Step 2 gives $\det(z\mathbb 1 - M') = \det(z\mathbb 1 - M)$. Its zeros, with multiplicities, are the eigenvalues (LADR Def. 9.63).
>
> **What the derivation shows**
> - Every statement of the form "$\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$" or "$\gamma^5$ has eigenvalues $\pm1$" is a statement about operators on $V$ and can be checked in any one basis ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]).
> - Statements about individual entries ("$\gamma^0$ is off-diagonal", "the upper two components") are not of this kind.

^der-c5a-1-4

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]]

## The Clifford algebra

> [!definition] Definition §C5a.1.7: The Dirac Matrices
> **Dirac matrices** ($\gamma$ matrices) are four $n\times n$ complex matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the **Clifford** (Dirac) **algebra**
>
> $$
> \{\gamma^\mu, \gamma^\nu\} \equiv \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\,\mathbb 1_n .
> $$
>
> The label $\mu$ is a spacetime index; the rows and columns are spinor indices (index slots: [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1|Def. §C3.1.1]]). $g^{\mu\nu}$ is the metric and $\gamma_\mu \equiv g_{\mu\nu}\gamma^\nu$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]).
>
> *Source: PS §3.2, eq. (3.22) · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The Dirac (Clifford) algebra", eq. (clifford)) · PHY 513 Lecture 7, Part B ("Warning: 4 × 4 identity matrix on RHS usually not written") · Yu §5.1, eq. (5.1)*

^def-c5a-1-7

> [!theorem] Theorem §C5a.1.5: First Consequences of the Clifford Algebra
> For Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]):
> 1. $(\gamma^0)^2 = \mathbb 1$, $(\gamma^i)^2 = -\mathbb 1$, and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \ne \nu$; each $\gamma^\mu$ is invertible.
> 2. For every four-vector $a$ with commuting components, $(a_\mu\gamma^\mu)^2 = a_\mu a^\mu\,\mathbb 1$.
> 3. *The split.* Every product of two Dirac matrices is its symmetric part plus its antisymmetric part:
>
> $$
> \gamma^\mu\gamma^\nu = \tfrac12\{\gamma^\mu, \gamma^\nu\} + \tfrac12[\gamma^\mu, \gamma^\nu] = g^{\mu\nu}\,\mathbb 1 + \tfrac12[\gamma^\mu, \gamma^\nu] .
> $$
>
> Contracted with a symmetric tensor only $g^{\mu\nu}\mathbb 1$ survives; contracted with an antisymmetric one only the commutator survives.
>
> *Source: Yu §5.1, eqs. (5.2)–(5.4) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?") · PS §3.2, p. 43 (the same step in Dirac ⇒ Klein–Gordon) · item 3: the user's PHY 513 notes use its symmetric half in Ch. 8 (sections "The Dirac representation", "Dirac implies Klein–Gordon", "Plane waves and an eigenvalue problem") and its antisymmetric half for the slash algebra (Ch. 9 §9.6, Problem Set 5)*

^thm-c5a-1-5

> [!derivation]- Derivation
> **1. Squares.** Put $\nu = \mu$: $2(\gamma^\mu)^2 = 2g^{\mu\mu}\mathbb 1$ (no sum), so $(\gamma^0)^2 = g^{00} = 1$ and $(\gamma^i)^2 = g^{ii} = -1$. Hence $(\gamma^0)^{-1} = \gamma^0$ and $(\gamma^i)^{-1} = -\gamma^i$.
>
> **2. Distinct indices.** For $\mu \ne \nu$, $g^{\mu\nu} = 0$, so $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 0$.
>
> **3. Square root.** $(a_\mu\gamma^\mu)^2 = a_\mu a_\nu\gamma^\mu\gamma^\nu$. The coefficient $a_\mu a_\nu$ is symmetric in $\mu\nu$, so only the symmetric part of $\gamma^\mu\gamma^\nu$ contributes: $a_\mu a_\nu\gamma^\mu\gamma^\nu = \frac12a_\mu a_\nu(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) = a_\mu a_\nu g^{\mu\nu}\mathbb 1 = a^2\mathbb 1$.
>
> **4. The split.** Add and subtract $\frac12\gamma^\nu\gamma^\mu$: $\gamma^\mu\gamma^\nu = \frac12(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) + \frac12(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)$. The first bracket is $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]). For a symmetric $S_{\mu\nu}$, $S_{\mu\nu}[\gamma^\mu, \gamma^\nu] = 0$: renaming the dummy indices $\mu \leftrightarrow \nu$ turns it into its own negative. For an antisymmetric $A_{\mu\nu}$, $A_{\mu\nu}g^{\mu\nu} = 0$ for the same reason. Step 3 is the case $S_{\mu\nu} = a_\mu a_\nu$.
>
> **What the derivation shows**
> - The algebra says exactly "the $\gamma$'s square to the metric and anticommute"; part 2 is the same statement for every direction at once.
> - Used next: Hermiticity (Theorem §C5a.1.11), the sixteen products (Theorem §C5a.1.6), Dirac ⇒ Klein–Gordon ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]), the slash algebra ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]).
> - The split is the working trick for products of two γ's. With $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ it reads $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]); it gives the second form of the spinor generators (Def. §C5a.3.1 in §C5a.3), $\slashed a\slashed b = a\cdot b - i\sigma^{\mu\nu}a_\mu b_\nu$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]), and, iterated, the reduction of any product of γ's to antisymmetrized products ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]]).

^der-c5a-1-5

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]

> [!remark] Remark: A square root of p²
> The handwritten question "square to $\pm1$, or square root?" has a precise answer: for a momentum $p$, $p_\mu\gamma^\mu$ is a matrix square root of the number $p^2$ (Theorem §C5a.1.5, 2). This is what Dirac was after: a first-order operator whose square is the Klein–Gordon operator, $(i\gamma^\mu\partial_\mu)^2 = -\partial^2$, so that a first-order equation implies $(\partial^2 + m^2)\psi = 0$ ([[§C13.2★ The Dirac Equation#^rem-c13-2-1|QM, Remark: The square root of the Klein–Gordon operator]]; [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]). No number squares to $p^2$ as a linear function of $p$; anticommuting matrices do, because the cross terms cancel in pairs. Run backwards, the requirement forces the algebra: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]] (the equivalence), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]] (no commuting coefficients), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]] (even size, at least four).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?")*

^rem-c5a-1-4

> [!definition] Definition §C5a.1.8: Antisymmetrized Products of γ Matrices
> For indices $\mu_1, \dots, \mu_n$,
>
> $$
> \gamma^{[\mu_1}\gamma^{\mu_2}\cdots\gamma^{\mu_n]} \equiv \gamma^{[\mu_1\cdots\mu_n]} \equiv \frac1{n!}\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\,\gamma^{\mu_{\pi(1)}}\cdots\gamma^{\mu_{\pi(n)}} ,
> $$
>
> of the Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]): the totally antisymmetric part, with weight $1/n!$. Thus $\gamma^{[\mu\nu]} = \frac12[\gamma^\mu, \gamma^\nu]$, which is $-2iS^{\mu\nu}$ with the spinor generators of §C5a.3 ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) and $-i\sigma^{\mu\nu}$ with $\sigma^{\mu\nu}$ of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]; for distinct indices it is the ordered product of Theorem §C5a.1.6 up to sign.
>
> *Source: PHY 513, Problem Set 5, Problem 5(c) statement (notation) · PS §3.4, p. 49 · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$")*

^def-c5a-1-8

> [!theorem] Theorem §C5a.1.6: The Sixteen Products Are a Basis
> For $A = \{\mu_1 < \dots < \mu_k\} \subseteq \{0, 1, 2, 3\}$ let $\Gamma_A = \gamma^{\mu_1}\cdots\gamma^{\mu_k}$ ($\Gamma_\varnothing = \mathbb 1$). For Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) of any size $n$:
> 1. $\Gamma_A\Gamma_B = \pm\Gamma_{A\triangle B}$ (symmetric difference), with a sign fixed by the algebra alone; in particular $\Gamma_A^2 = \pm\mathbb 1$;
> 2. $\operatorname{tr}\Gamma_A = 0$ for $A \ne \varnothing$;
> 3. the sixteen $\Gamma_A$ are linearly independent, so $n \ge 4$;
> 4. for $n = 4$ they are a basis of $M_4(\mathbb C)$: only multiples of $\mathbb 1$ commute with all $\gamma^\mu$, and no subspace of $\mathbb C^4$ other than $0$ and $\mathbb C^4$ is invariant under all $\gamma^\mu$ (irreducibility, [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-8|Def. §C3.1.8]]).
>
> *Source: PS §3.2, p. 41 ("these matrices must be at least 4 × 4") and §3.4, p. 50 (the sixteen matrices) · the user's PHY 513 notes, Ch. 8, paragraph after the bilinears ("the sixteen matrices … are a basis of all 4 × 4 matrices") · the user's pre-course notes, §5.1 ("Dimension of the spinor representation": independence "stated") · Yu §5.1, eq. (5.45) · the trace proof written out here*

^thm-c5a-1-6

> [!derivation]- Derivation
> **1. Products.** Write $\Gamma_A\Gamma_B$ as one string of $\gamma$'s. For each $\mu \in A\cap B$, move the copy of $\gamma^\mu$ from the $B$ part leftwards until it stands next to its partner from $A$; each step past a different $\gamma^\nu$ gives a factor $-1$ (Theorem §C5a.1.5). The pair becomes $(\gamma^\mu)^2 = g^{\mu\mu}\mathbb 1 = \pm\mathbb 1$. What is left is a product of the $\gamma^\mu$ with $\mu \in A\triangle B$, each once, in some order; reordering it increasingly costs one $-1$ per transposition. So $\Gamma_A\Gamma_B = c_{AB}\Gamma_{A\triangle B}$ with $c_{AB} = \pm1$ computed from the anticommutation signs and $g^{\mu\mu}$ only. With $B = A$, $A\triangle A = \varnothing$: $\Gamma_A^2 = c_{AA}\mathbb 1$, and $\Gamma_A^{-1} = c_{AA}\Gamma_A$.
>
> **2. Passing one γ through Γ_A.** If $|A| = k$: for $\mu \in A$, $\gamma^\mu$ anticommutes with the $k - 1$ other factors and commutes with itself, so $\gamma^\mu\Gamma_A = (-1)^{k-1}\Gamma_A\gamma^\mu$; for $\nu \notin A$, $\gamma^\nu\Gamma_A = (-1)^k\Gamma_A\gamma^\nu$.
>
> **3. Traces.** Let $A \ne \varnothing$. If $k$ is even, pick $\mu \in A$: by step 2, $\Gamma_A = -(\gamma^\mu)^{-1}\Gamma_A\gamma^\mu$, and cyclicity of the trace ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]) gives $\operatorname{tr}\Gamma_A = -\operatorname{tr}\Gamma_A = 0$. If $k$ is odd ($k = 1$ or $3$), there is $\nu \notin A$, and $\Gamma_A = -(\gamma^\nu)^{-1}\Gamma_A\gamma^\nu$ gives the same.
>
> **4. Independence.** Suppose $\sum_Ac_A\Gamma_A = 0$. Multiply by $\Gamma_B^{-1}$ and take the trace: $\Gamma_B^{-1}\Gamma_A = c_{BB}\Gamma_B\Gamma_A = \pm\Gamma_{A\triangle B}$ is traceless unless $A = B$ (step 3), when it is $\mathbb 1$ with trace $n$. So $nc_B = 0$, $c_B = 0$ for every $B$. Sixteen independent elements of the $n^2$-dimensional space $M_n(\mathbb C)$ need $n^2 \ge 16$: $n \ge 4$.
>
> **5. n = 4.** $\dim M_4(\mathbb C) = 16$, so the sixteen independent $\Gamma_A$ span it. A matrix commuting with every $\gamma^\mu$ commutes with every product $\Gamma_A$, hence with every $4\times4$ matrix, in particular with the matrix units $E_{ij}$; $E_{ij}M = ME_{ij}$ for all $i, j$ forces $M = c\mathbb 1$. A subspace invariant under all $\gamma^\mu$ is invariant under all $\Gamma_A$, hence under all matrices, and only $0$ and $\mathbb C^4$ are.
>
> **What the derivation shows**
> - Everything follows from the anticommutation signs; no explicit matrices were used. The chiral basis is one $4\times4$ solution, so $n = 4$ is attained. That $n$ must be even is [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]] (also [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]]), by another trace argument; here the bound comes from independence of all sixteen products at once.
> - Up to factors $\pm1, \pm i$ the sixteen are $\mathbb 1$, $\gamma^\mu$, $\gamma^\mu\gamma^\nu$ ($\mu < \nu$), $\gamma^\mu\gamma^\nu\gamma^\rho$ ($\propto\gamma_\kappa\gamma^5$) and $\gamma^0\gamma^1\gamma^2\gamma^3$ ($\propto\gamma^5$, Def. §C5a.5.1): the scalar, vector, tensor, axial vector and pseudoscalar of the bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]); reducing any product to them is [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]].
> - ⚑ By-product (step 3): every $\gamma^\mu$ and every product of distinct $\gamma$'s is traceless, the start of trace technology ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]).
> - Used next: Pauli's theorem (Theorem §C5a.1.12), which needs part 4.

^der-c5a-1-6

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]

## The Clifford action on spinor space

> [!definition] Definition §C5a.1.9: The Dirac Maps
> The **Dirac maps** on spinor space $V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]) are four linear maps $\Gamma^0, \Gamma^1, \Gamma^2, \Gamma^3 \in \operatorname{End}(V)$ with
>
> $$
> \Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}\,\mathrm{id}_V ,
> $$
>
> $g^{\mu\nu}$ the metric ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]): a representation of the Clifford algebra on $V$. In a basis their matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]) are written $\gamma^\mu$: $\Gamma^\mu e_b = \sum_a(\gamma^\mu)_{ab}e_a$.
>
> *Source: PS §3.2, eq. (3.22), p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent") · PHY 513 Lecture 7, Part B ("There are many realizations of $\gamma^\mu$") · Yu §5.1, eq. (5.1) · the basis-free formulation written here*

^def-c5a-1-9

> [!theorem] Theorem §C5a.1.7: The Matrices of the Dirac Maps in Any Basis
> For the Dirac maps ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]):
> 1. in every basis of $V$ the matrices $\gamma^\mu$ are Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]), and under a change of basis $\gamma'^\mu = U\gamma^\mu U^{-1}$;
> 2. every operator built from the $\Gamma^\mu$ by sums, products, multiplication by numbers and convergent power series has, in each basis, the matrix given by the same formula in that basis's $\gamma$'s, and these matrices transform as $U(\cdot)U^{-1}$.
>
> *Source: Yu §5.2, eq. (5.72) · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness": "the choice of basis is a convention") · part 2 written here*

^thm-c5a-1-7

> [!derivation]- Derivation
> **1. Clifford relation in a basis.** By Theorem §C5a.1.1 the matrix of $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu$ is $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu$ and that of $2g^{\mu\nu}\mathrm{id}$ is $2g^{\mu\nu}\mathbb 1$; equal operators have equal matrices. The rule $\gamma'^\mu = U\gamma^\mu U^{-1}$ is Theorem §C5a.1.2 with $M = \Gamma^\mu$. (Directly: $\{U\gamma^\mu U^{-1}, U\gamma^\nu U^{-1}\} = U\{\gamma^\mu, \gamma^\nu\}U^{-1} = 2g^{\mu\nu}\mathbb 1$, Yu (5.72).)
>
> **2. Products.** If operators $A$, $B$ have matrices $a$, $b$ in the old basis, $AB$ has the matrix $ab$ (Theorem §C5a.1.1), and in the new basis, inserting $U^{-1}U = \mathbb 1$ between the factors, $a'b' = UaU^{-1}UbU^{-1} = U(ab)U^{-1}$; sums and multiples go the same way. By induction on the number of factors, every polynomial in the $\Gamma^\mu$ has matrix "the same polynomial in the $\gamma$'s", and computing it from the new $\gamma$'s gives $U(\cdot)U^{-1}$ of the old one. For example $i\gamma'^0\gamma'^1\gamma'^2\gamma'^3 = iU\gamma^0U^{-1}U\gamma^1U^{-1}U\gamma^2U^{-1}U\gamma^3U^{-1} = U(i\gamma^0\gamma^1\gamma^2\gamma^3)U^{-1}$, and $[\gamma'^\mu, \gamma'^\nu] = U[\gamma^\mu, \gamma^\nu]U^{-1}$.
>
> **3. Power series.** For a matrix $A$: $(UAU^{-1})^n = UA^nU^{-1}$ (the inner $U^{-1}U$ cancel), so term by term $\sum_nc_n(UAU^{-1})^n = U\bigl(\sum_nc_nA^n\bigr)U^{-1}$ wherever the series converges absolutely (multiplication by fixed matrices is continuous). In particular $\exp(UAU^{-1}) = U\,e^A\,U^{-1}$.
>
> **What the derivation shows**
> - Only Theorem §C5a.1.1 (operators ↔ matrices) and the cancellation $U^{-1}U = \mathbb 1$ are used.
> - Instances defined later: $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]), $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]): computed from the new $\gamma$'s, each is the transformed old one, $\gamma'^5 = U\gamma^5U^{-1}$, $S'^{\mu\nu} = US^{\mu\nu}U^{-1}$, $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$ (steps 2–3).
> - Used next: the eigenvalues ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-8|Theorem §C5a.1.8]]) and changes of basis as intertwiners (Theorem §C5a.1.13).

^der-c5a-1-7

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]]

> [!theorem] Theorem §C5a.1.8: The Eigenvalues of Γ⁰ and Γⁱ
> For the Dirac maps ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]), $\Gamma^0$ is diagonalizable with eigenvalues $+1$ and $-1$, each twice, and each $\Gamma^i$ ($i = 1, 2, 3$) is diagonalizable with eigenvalues $+i$ and $-i$, each twice. Hence the matrix $\gamma^0$ has eigenvalues $\pm1$ (each twice) in every basis ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-4|Theorem §C5a.1.4]]).
>
> *Source: the argument written here, from the Clifford algebra and the trace ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]); the same argument for $\gamma^5$ is in the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$")*

^thm-c5a-1-8

> [!derivation]- Derivation
> **1. Eigenvalues of Γ⁰.** $(\Gamma^0)^2 = \mathrm{id}$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]]), so the minimal polynomial of $\Gamma^0$ divides $z^2 - 1 = (z - 1)(z + 1)$, which has distinct zeros: $\Gamma^0$ is diagonalizable with eigenvalues in $\{1, -1\}$ ([[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]]). Its trace is $0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 2), and the trace is the sum of the eigenvalues with multiplicity ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]]): $n_+ - n_- = 0$ with $n_+ + n_- = 4$, so $n_\pm = 2$.
>
> **2. Eigenvalues of Γⁱ.** $(\Gamma^i)^2 = -\mathrm{id}$: the minimal polynomial divides $(z - i)(z + i)$, again with distinct zeros; trace $0$ gives $i(n_+ - n_-) = 0$, so $n_\pm = 2$.
>
> **What the derivation shows**
> - Only the Clifford relation and the trace were used, so the result holds in every basis: "$\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$" of the Dirac basis ([[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]) is the operator written in its own eigenbasis; the off-diagonal $\gamma^0$ of the chiral basis has the same eigenvalues (Theorem §C5a.1.4).
> - ⚑ By-product: no basis makes $\gamma^0$ and $\gamma^5$ both diagonal → [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-7|Theorem §C5a.5.7]].
> - Used next: the signature of the Dirac form ([[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]]).

^der-c5a-1-8

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]]

## The chiral basis and Hermiticity

> [!definition] Definition §C5a.1.10: The Matrices σ^μ and σ̄^μ
> With $\mathbb 1$ the $2\times2$ identity and the Pauli matrices $\boldsymbol\sigma$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]]),
>
> $$
> \sigma^\mu = (\mathbb 1, \boldsymbol\sigma), \qquad \bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma), \qquad \sigma_\mu = g_{\mu\nu}\sigma^\nu = (\mathbb 1, -\boldsymbol\sigma) .
> $$
>
> For a four-vector $x$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]) write $X \equiv x_\mu\sigma^\mu = x^0\mathbb 1 - \mathbf x\cdot\boldsymbol\sigma$ and $\bar X \equiv x_\mu\bar\sigma^\mu = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$.
>
> *Source: PS §3.2, eq. (3.41) · Yu §5.2, eq. (5.74); Exercise 3.7, eq. (3.259) · PHY 513 Lecture 8, Part C ("Notation $\sigma^\mu = (1, \vec\sigma)$, $\bar\sigma^\mu = (1, -\vec\sigma)$") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit")*

^def-c5a-1-10

The bar on $\bar\sigma$ has nothing to do with the bar of the Dirac conjugate $\bar\psi$ (PS p. 44). Note that $\sigma_\mu$ and $\bar\sigma^\mu$ have the same entries: lowering the index of $\sigma$ and replacing $\sigma$ by $\bar\sigma$ both flip the sign of the spatial part.

> [!theorem] Theorem §C5a.1.9: Identities of σ^μ and σ̄^μ
> For $\sigma^\mu$, $\bar\sigma^\mu$, $X$, $\bar X$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]:
> 1. $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$.
> 2. $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1$ and $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu = 2g^{\mu\nu}\mathbb 1$; in particular $X\bar X = \bar XX = x^2\,\mathbb 1$.
> 3. $\sigma^2(\sigma^\mu)^*\sigma^2 = \bar\sigma^\mu$ and $\sigma^2(\bar\sigma^\mu)^*\sigma^2 = \sigma^\mu$.
>
> *Source: Yu Exercise 3.7, eq. (3.260) (the inverse $x^\mu = \frac12\operatorname{tr}(X\bar\sigma^\mu)$, which is part 1) · the user's PHY 513 notes, Ch. 8 §8.2 ("from $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$ the inverse is …") · PS eq. (3.38) (part 3 for $\boldsymbol\sigma$) · the case-by-case computation written out here*

^thm-c5a-1-9

> [!derivation]- Derivation
> The only input is the Pauli product rule $\sigma^i\sigma^j = \delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k$, with $\operatorname{tr}\sigma^i = 0$ and $\operatorname{tr}\mathbb 1 = 2$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). Latin indices run over $1, 2, 3$.
>
> **1. Trace, by cases.** $(\mu, \nu) = (0, 0)$: $\operatorname{tr}(\mathbb 1\cdot\mathbb 1) = 2 = 2g^{00}$. $(0, j)$: $\operatorname{tr}(\mathbb 1\cdot(-\sigma^j)) = 0 = 2g^{0j}$. $(i, 0)$: $\operatorname{tr}(\sigma^i\cdot\mathbb 1) = 0$. $(i, j)$: $\operatorname{tr}(\sigma^i(-\sigma^j)) = -\operatorname{tr}(\delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k) = -2\delta^{ij} = 2g^{ij}$.
>
> **2. Anticommutators, by cases.** For $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu$: $(0, 0)$ gives $\mathbb 1 + \mathbb 1 = 2g^{00}\mathbb 1$; $(0, j)$ gives $\mathbb 1(-\sigma^j) + \sigma^j\mathbb 1 = 0$; $(i, j)$ gives $-\sigma^i\sigma^j - \sigma^j\sigma^i = -2\delta^{ij}\mathbb 1 = 2g^{ij}\mathbb 1$, because the $i\varepsilon^{ijk}\sigma^k$ terms of the two products are opposite ($\varepsilon^{jik} = -\varepsilon^{ijk}$). For $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu$ the same three cases give $2\mathbb 1$, $(-\sigma^j) + \sigma^j = 0$ and $-2\delta^{ij}\mathbb 1$.
>
> **3. X X̄.** $X\bar X = x_\mu x_\nu\sigma^\mu\bar\sigma^\nu$. The coefficient $x_\mu x_\nu$ is symmetric in $\mu\nu$, so only the symmetric part of $\sigma^\mu\bar\sigma^\nu$ survives: $x_\mu x_\nu\sigma^\mu\bar\sigma^\nu = \frac12x_\mu x_\nu(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu) = x_\mu x_\nu g^{\mu\nu}\mathbb 1 = x^2\mathbb 1$ by step 2. The same for $\bar XX$.
>
> **4. Conjugation by σ².** $\sigma^1$ and $\sigma^3$ are real and $\sigma^2$ is imaginary, so $(\sigma^1)^{\ast} = \sigma^1$, $(\sigma^2)^{\ast} = -\sigma^2$, $(\sigma^3)^{\ast} = \sigma^3$. Since $(\sigma^2)^2 = \mathbb 1$ and $\sigma^2$ anticommutes with $\sigma^1, \sigma^3$: $\sigma^2\sigma^1\sigma^2 = -\sigma^1(\sigma^2)^2 = -\sigma^1$, $\sigma^2(-\sigma^2)\sigma^2 = -\sigma^2$, $\sigma^2\sigma^3\sigma^2 = -\sigma^3$. So $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$ for each $i$ (PS (3.38)), while $\sigma^2\mathbb 1^{\ast}\sigma^2 = \mathbb 1$. Hence $\sigma^2(\sigma^\mu)^{\ast}\sigma^2 = (\mathbb 1, -\boldsymbol\sigma) = \bar\sigma^\mu$, and conjugating $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ the same way gives $(\mathbb 1, \boldsymbol\sigma) = \sigma^\mu$.
>
> **What the derivation shows**
> - Part 2 is a "Clifford algebra" for the pair $(\sigma, \bar\sigma)$: neither set alone squares to $g$, but $\sigma$ followed by $\bar\sigma$ does. Stacking them into a $4\times4$ matrix is exactly the chiral Dirac matrix → [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]].
> - $X\bar X = x^2$ makes $\det X = x^2$ plausible ($\det X\cdot\det\bar X = (x^2)^2$, and the two determinants are equal): the next theorems use it.
> - Part 3 is the matrix form of "complex conjugation exchanges the two Weyl representations" → Theorem §C5a.4.1, part 3.

^der-c5a-1-9

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!definition] Definition §C5a.1.11: The Chiral Basis
> The **chiral** (**Weyl**) **basis** is, in $2\times2$ blocks, with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]],
>
> $$
> \gamma^0 = \begin{pmatrix} 0 & \mathbb 1 \\ \mathbb 1 & 0 \end{pmatrix}, \qquad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}, \qquad\text{i.e.}\qquad \gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix} .
> $$
>
> A Dirac spinor in this basis is written $\psi = \binom{\psi_L}{\psi_R}$, with two-component upper and lower halves (their Lorentz transformation, as left- and right-handed Weyl spinors, is derived in §C5a.3–§C5a.4: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-2|Def. §C5a.4.2]]).
>
> *Source: PS §3.2, eqs. (3.25), (3.36), (3.42) · PHY 513 Lecture 7, Part B (slide "Explicit Form of Dirac Matrices"); Lecture 8, Cheat Sheet I and Part C ("Economical form of all 4 $\gamma$-matrices") · the user's PHY 513 notes, Ch. 8 §8.1, eq. (chiralbasis), §8.2, eq. (weylsplit) · Yu §5.2, eqs. (5.68), (5.75)*

^def-c5a-1-11

> [!theorem] Theorem §C5a.1.10: The Chiral Matrices Satisfy the Clifford Algebra
> The matrices of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]] satisfy $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_4$, and $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis") · PHY 513 Lecture 7, Part B (sample check $\{\gamma^0, \gamma^i\} = 0$) · Yu §5.2, eqs. (5.69)–(5.71) · PHY 513, Problem Set 6, Problem 3(a) (the block-by-block check of step 3, as the user wrote it)*

^thm-c5a-1-10

> [!derivation]- Derivation
> **1. The block product.** $\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}\begin{pmatrix}0&\sigma^\nu\\\bar\sigma^\nu&0\end{pmatrix} = \begin{pmatrix}0\cdot0 + \sigma^\mu\bar\sigma^\nu & 0\cdot\sigma^\nu + \sigma^\mu\cdot0\\ \bar\sigma^\mu\cdot0 + 0\cdot\bar\sigma^\nu & \bar\sigma^\mu\sigma^\nu + 0\cdot0\end{pmatrix} = \begin{pmatrix}\sigma^\mu\bar\sigma^\nu & 0\\ 0 & \bar\sigma^\mu\sigma^\nu\end{pmatrix}$.
>
> **2. The anticommutator.** Adding the same with $\mu \leftrightarrow \nu$: $\{\gamma^\mu, \gamma^\nu\} = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu,\ \bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu) = \operatorname{diag}(2g^{\mu\nu}\mathbb 1, 2g^{\mu\nu}\mathbb 1)$ by [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], 2.
>
> **3. Explicitly (the lecture's check).** $(\gamma^0)^2 = \operatorname{diag}(\mathbb 1, \mathbb 1)$; $\gamma^0\gamma^i = \operatorname{diag}(-\sigma^i, \sigma^i)$ and $\gamma^i\gamma^0 = \operatorname{diag}(\sigma^i, -\sigma^i)$, so $\{\gamma^0, \gamma^i\} = 0$; $\gamma^i\gamma^j = \operatorname{diag}(-\sigma^i\sigma^j, -\sigma^i\sigma^j)$, so $\{\gamma^i, \gamma^j\} = -\operatorname{diag}(\{\sigma^i, \sigma^j\}, \{\sigma^i, \sigma^j\}) = -2\delta^{ij}\mathbb 1_4 = 2g^{ij}\mathbb 1_4$. All ten conditions hold.
>
> **What the derivation shows**
> - The Clifford algebra of $\gamma$ is the pair identity of $\sigma$, $\bar\sigma$ stacked off-diagonally; every product of two $\gamma$'s is block diagonal, every product of an odd number off-diagonal. That is why the generators (products of two) will not mix the halves (Theorem §C5a.3.3).

^der-c5a-1-10

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]]

> [!theorem] Theorem §C5a.1.11: Hermiticity of the Dirac Matrices
> 1. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$, equivalently $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; each $\gamma^\mu$ is unitary.
> 2. The same holds in any basis in which each $\gamma^\mu$ is a normal matrix, and in particular in any basis reached from the chiral one by a unitary matrix.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", eq. (gammadagger)) · Yu §5.1, eqs. (5.4)–(5.7) · the user's pre-course notes, §5.1 ("Hermiticity"; "hypothesis … arrangeable by a change of basis") · PHY 513, Problem Set 5, Problem 5(b) (the chiral-basis check, as the user wrote it)*

^thm-c5a-1-11

> [!derivation]- Derivation
> **1. Chiral basis.** $\gamma^{0\dagger}$: transposing $\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ and conjugating gives itself. $\gamma^{i\dagger} = \begin{pmatrix}0&(-\sigma^i)^\dagger\\(\sigma^i)^\dagger&0\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix} = -\gamma^i$, the Pauli matrices being Hermitian ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
>
> **2. The compact form.** $\gamma^0\gamma^0\gamma^0 = \gamma^0$ (Theorem §C5a.1.5); $\gamma^0\gamma^i\gamma^0 = -\gamma^i\gamma^0\gamma^0 = -\gamma^i$ (anticommute, then $(\gamma^0)^2 = \mathbb 1$). So $\gamma^0\gamma^\mu\gamma^0$ equals $\gamma^{\mu\dagger}$ for every $\mu$.
>
> **3. Unitarity.** $\gamma^{0\dagger}\gamma^0 = (\gamma^0)^2 = \mathbb 1$, $\gamma^{i\dagger}\gamma^i = -(\gamma^i)^2 = \mathbb 1$.
>
> **4. Normal matrices.** If $\gamma^\mu$ is normal, it is $W\operatorname{diag}(d_1, \dots, d_n)W^\dagger$ with $W$ unitary (spectral theorem). Then $(\gamma^\mu)^2 = W\operatorname{diag}(d_k^2)W^\dagger = g^{\mu\mu}\mathbb 1$ forces $d_k^2 = g^{\mu\mu}$: $d_k = \pm1$ for $\mu = 0$, $d_k = \pm i$ for $\mu = i$. Real eigenvalues make $\gamma^0 = W\operatorname{diag}(d_k)W^\dagger$ Hermitian; imaginary ones make $\gamma^i$ anti-Hermitian, $(W\operatorname{diag}(d_k)W^\dagger)^\dagger = W\operatorname{diag}(d_k^{\ast})W^\dagger = -\gamma^i$. (One $W$ per matrix: the four are not simultaneously diagonalizable, since they anticommute.)
>
> **5. Unitary changes of basis.** If $\gamma'^\mu = U\gamma^\mu U^\dagger$ with $U$ unitary, then $\gamma'^{\mu\dagger} = U\gamma^{\mu\dagger}U^\dagger = U\gamma^0\gamma^\mu\gamma^0U^\dagger = \gamma'^0\gamma'^\mu\gamma'^0$, inserting $U^\dagger U = \mathbb 1$ between the factors.
>
> **What the derivation shows**
> - Hermiticity is not part of the Clifford algebra: a non-unitary change of basis preserves the algebra (Theorem §C5a.1.12) but destroys it. It is a choice of basis, assumed from here on; in Yu and the pre-course notes it enters as the hypothesis "normal".
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ is the identity used for every adjoint in Dirac theory: the generators (Theorem §C5a.3.5), $\bar\psi$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]), the reality of bilinears ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]]).

^der-c5a-1-11

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## Uniqueness: Pauli's theorem

> [!theorem] Theorem §C5a.1.12: Pauli's Fundamental Theorem
> 1. If $\gamma^\mu$ and $\gamma'^\mu$ are two sets of $4\times4$ Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]), there is an invertible $U$ with $\gamma'^\mu = U\gamma^\mu U^{-1}$ for all $\mu$, unique up to a nonzero factor. Conversely, $U\gamma^\mu U^{-1}$ is a set of Dirac matrices for every invertible $U$.
> 2. If both sets satisfy $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]), $U$ can be chosen unitary.
>
> *Source: PS §3.2, p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent", stated) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)", stated) · Yu §5.2, eq. (5.72) (the converse) · PHY 513, Problem Set 6, Problem 3(a) (the converse for unitary $U$, $\gamma^\mu = U\gamma^\mu_WU^\dagger$, as the user wrote it: step 1 below with $U^{-1} = U^\dagger$; the statement adds "it can be shown that all possible realizations of the Dirac algebra are unitarily equivalent") · the proof (averaging over the sixteen products) written out here*

^thm-c5a-1-12

> [!derivation]- Derivation
> **1. Converse.** $\{U\gamma^\mu U^{-1}, U\gamma^\nu U^{-1}\} = U\{\gamma^\mu, \gamma^\nu\}U^{-1} = 2g^{\mu\nu}U\mathbb 1U^{-1} = 2g^{\mu\nu}\mathbb 1$.
>
> **2. The same signs.** Form $\Gamma_A$ and $\Gamma'_A$ from the two sets. By Theorem §C5a.1.6, 1, $\Gamma_A\Gamma_B = c_{AB}\Gamma_{A\triangle B}$ and $\Gamma'_A\Gamma'_B = c_{AB}\Gamma'_{A\triangle B}$ with the *same* $c_{AB}$, which depends only on the algebra.
>
> **3. An averaged intertwiner.** For any $F \in M_4(\mathbb C)$ set $S_F = \sum_A\Gamma'_AF\Gamma_A^{-1}$ (sixteen terms). For each $B$,
>
> $$
> \Gamma'_BS_F\Gamma_B^{-1} = \sum_A(\Gamma'_B\Gamma'_A)F(\Gamma_B\Gamma_A)^{-1} = \sum_Ac_{BA}\Gamma'_{B\triangle A}\,F\,c_{BA}^{-1}\Gamma_{B\triangle A}^{-1} = \sum_C\Gamma'_CF\Gamma_C^{-1} = S_F ,
> $$
>
> using step 2, $(XY)^{-1} = Y^{-1}X^{-1}$, $c_{BA} = \pm1$, and the change of summation variable $C = B\triangle A$, which runs over all sixteen subsets exactly once as $A$ does ($A = B\triangle C$). So $\Gamma'_BS_F = S_F\Gamma_B$ for all $B$, in particular $\gamma'^\mu S_F = S_F\gamma^\mu$.
>
> **4. Some S_F is nonzero.** The entries of $S_{E_{ij}}$ ($E_{ij}$ the matrix units) are $(S_{E_{ij}})_{ab} = \sum_A(\Gamma'_A)_{ai}(\Gamma_A^{-1})_{jb}$. Put $a = i$, $b = j$ and sum over $i, j$: $\sum_{i,j}(S_{E_{ij}})_{ij} = \sum_A\operatorname{tr}\Gamma'_A\operatorname{tr}\Gamma_A^{-1}$. Every term with $A \ne \varnothing$ vanishes ($\Gamma_A^{-1} = \pm\Gamma_A$ is traceless, Theorem §C5a.1.6, 2), and $A = \varnothing$ gives $4\cdot4 = 16$. So some $S \equiv S_{E_{ij}} \ne 0$.
>
> **5. S is invertible.** If $Sv = 0$, then $S\gamma^\mu v = \gamma'^\mu Sv = 0$: $\ker S$ is invariant under all $\gamma^\mu$, so it is $0$ or $\mathbb C^4$ (Theorem §C5a.1.6, 4); it is not $\mathbb C^4$ since $S \ne 0$. (Schur's argument, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]].) Take $U = S$: $\gamma'^\mu = U\gamma^\mu U^{-1}$.
>
> **6. Uniqueness.** If also $\gamma'^\mu = V\gamma^\mu V^{-1}$, then $V^{-1}U$ commutes with every $\gamma^\mu$, so $V^{-1}U = c\mathbb 1$ (Theorem §C5a.1.6, 4), $c \ne 0$.
>
> **7. Unitary choice.** If both sets obey $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, all $\gamma^\mu$, $\gamma'^\mu$ are unitary (Theorem §C5a.1.11, whose step 3 used only this relation and the algebra), hence so are all products $\Gamma_A$, $\Gamma'_A$. Take the adjoint of $\Gamma'_AU = U\Gamma_A$: $U^\dagger\Gamma'^{-1}_A = \Gamma_A^{-1}U^\dagger$, i.e. $\Gamma_AU^\dagger = U^\dagger\Gamma'_A$. Then $U^\dagger U\Gamma_A = U^\dagger\Gamma'_AU = \Gamma_AU^\dagger U$: $U^\dagger U$ commutes with every $\Gamma_A$, so $U^\dagger U = c\mathbb 1$; it is positive definite ($v^\dagger U^\dagger Uv = |Uv|^2 > 0$), so $c > 0$, and $U/\sqrt c$ is unitary and still intertwines.
>
> **What the derivation shows**
> - "There are many realizations of $\gamma^\mu$" (Lecture 7) means one realization in many bases, exactly as spin $\frac12$ has one set of Pauli matrices up to a change of basis. Every basis-independent statement may be proved in the chiral basis and holds everywhere.
> - The trick of step 3, averaging over a finite group ($\pm\Gamma_A$, $32$ elements), is the finite version of the invariant averaging behind complete reducibility ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]]).
> - Used next: Example §C5a.5.1; the basis independence of $\gamma^5$'s eigenspaces (Theorem §C5a.5.2).
> - Read without a basis ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-13|Theorem §C5a.1.13]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-14|Theorem §C5a.1.14]]), Pauli's theorem says that a choice of $\gamma$ matrices is a choice of basis of one spinor space; what then happens to spinor components, to $\bar\psi$ and to the Dirac equation is [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]] and [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]].

^der-c5a-1-12

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]

> [!definition] Definition §C5a.1.12: Intertwiners of Clifford Representations
> Let $\Gamma^\mu$ on $V$ and $\tilde\Gamma^\mu$ on $\tilde V$ satisfy the Clifford relation ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]). A linear map $T : V \to \tilde V$ is an **intertwiner** if $T\,\Gamma^\mu = \tilde\Gamma^\mu\,T$ for $\mu = 0, \dots, 3$; the two representations are **equivalent** if an invertible intertwiner exists. The same words apply to two sets of $4\times4$ matrices acting on columns $\mathbb C^4$. (Intertwiners for groups and Lie algebras: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]; equivalence: [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]].)
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition, "Equivalence and reducibility": "they differ only by a change of basis") · PS §3.2, p. 41 ("unitarily equivalent") · the Clifford version written here*

^def-c5a-1-12

> [!theorem] Theorem §C5a.1.13: Changes of Basis Are the Invertible Intertwiners
> 1. If $\gamma^\mu$ and $\gamma'^\mu$ are the matrices of the Dirac maps in bases $e$ and $e'$, the change-of-basis matrix $U$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]) is an invertible intertwiner ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-12|Def. §C5a.1.12]]) from $\gamma^\mu$ to $\gamma'^\mu$: $U\gamma^\mu = \gamma'^\mu U$.
> 2. Conversely, if $\gamma^\mu$ are the matrices in a basis $e$ and $U$ is invertible with $U\gamma^\mu U^{-1} = \tilde\gamma^\mu$, then $e'_b \equiv \sum_a(U^{-1})_{ab}e_a$ is a basis in which the Dirac maps have the matrices $\tilde\gamma^\mu$, and $U$ is its change-of-basis matrix.
>
> *Source: Yu §5.2, eq. (5.72) ("all representations are equivalent, related by similarity transformations") · the user's PHY 513 notes, Ch. 7 §7.2 · part 2 written here*

^thm-c5a-1-13

> [!derivation]- Derivation
> **1. Part 1.** Theorem §C5a.1.7, 1 gives $\gamma'^\mu = U\gamma^\mu U^{-1}$; multiply on the right by $U$.
>
> **2. Part 2: e′ is a basis.** The list $e'$ is the image of $e$ under the invertible operator whose matrix in $e$ is $U^{-1}$, so it is a basis.
>
> **3. Part 2: its change-of-basis matrix.** $\sum_aU_{ab}e'_a = \sum_aU_{ab}\sum_c(U^{-1})_{ca}e_c = \sum_c(U^{-1}U)_{cb}e_c = e_b$, which is Def. §C5a.1.4 with matrix $U$.
>
> **4. Part 2: the matrices.** By Theorem §C5a.1.2 the matrices of $\Gamma^\mu$ in $e'$ are $U\gamma^\mu U^{-1} = \tilde\gamma^\mu$.
>
> **What the derivation shows**
> - "Two realizations of the $\gamma$ matrices" and "one set of Dirac maps in two bases" are the same thing. A similarity transformation of the $\gamma$'s alone is a change of basis of $V$ only if the spinors' components are changed with it (Theorem §C5a.7.2).

^der-c5a-1-13

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]

> [!theorem] Theorem §C5a.1.14: Spinor Space Is Unique up to Isomorphism
> 1. If $(V, \Gamma^\mu)$ and $(\tilde V, \tilde\Gamma^\mu)$ are two four-dimensional complex spaces with Dirac maps ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]), there is an invertible intertwiner $T : V \to \tilde V$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-12|Def. §C5a.1.12]]), unique up to a nonzero factor.
> 2. Given $(V, \Gamma^\mu)$, every set of $4\times4$ Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) — chiral, Dirac, Majorana or any other — is the set of matrices of the $\Gamma^\mu$ in some basis of $V$, and that basis is unique up to multiplying all its vectors by one nonzero number.
>
> This is Pauli's theorem ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]) read without a basis: there is one spinor space, and a choice of $\gamma$ matrices is a choice of basis in it.
>
> *Source: PS §3.2, p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent. We thus need only write one explicit realization") · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness (Pauli's fundamental theorem)") · the basis-free reading written here*

^thm-c5a-1-14

> [!derivation]- Derivation
> **1. Part 1: existence.** Choose bases $e$ of $V$ and $\tilde e$ of $\tilde V$, with matrices $\gamma^\mu$ and $\tilde\gamma^\mu$ (Dirac matrices by Theorem §C5a.1.7). Pauli's theorem gives an invertible $U$ with $\tilde\gamma^\mu = U\gamma^\mu U^{-1}$. Define $T$ by $Te_b = \sum_aU_{ab}\tilde e_a$ (a linear map is fixed by its values on a basis, [[Linear map lemma|LADR Thm. 3.4]]); its matrix is $U$ (Def. §C5a.1.3, from $e$ to $\tilde e$), it is invertible, and the matrices of $T\Gamma^\mu$ and $\tilde\Gamma^\mu T$ are $U\gamma^\mu$ and $\tilde\gamma^\mu U$ ([[§10 Invertibility and Isomorphisms#^ladr-3-81|LADR Thm. 3.81]]), which are equal. Equal matrices, equal maps.
>
> **2. Part 1: uniqueness.** If $T$ and $T'$ are both invertible intertwiners, $T^{-1}T'$ commutes with every $\Gamma^\mu$; its matrix commutes with every $\gamma^\mu$, hence is $c\mathbb 1$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 4), $c \ne 0$: $T' = cT$.
>
> **3. Part 2: existence.** Fix a basis $e$ with matrices $\gamma^\mu$; Pauli's theorem gives $\tilde\gamma^\mu = U\gamma^\mu U^{-1}$, and Theorem §C5a.1.13, 2 produces the basis.
>
> **4. Part 2: uniqueness.** If $f$ and $f'$ both give $\tilde\gamma^\mu$, their change-of-basis matrix $W$ satisfies $W\tilde\gamma^\mu W^{-1} = \tilde\gamma^\mu$, so $W = c\mathbb 1$ (as in step 2), i.e. $f_b = cf'_b$ for all $b$.
>
> **What the derivation shows**
> - ⚑ By-product: the only freedom left once the $\gamma$ matrices are chosen is an overall factor of the basis, which multiplies every spinor's components by $c^{-1}$ and leaves every matrix unchanged. Whether $\bar\psi\psi$ notices it is Theorem §C5a.2.4, 2: it does, by $|c|^{-2}$, unless $|c| = 1$.
> - The averaging construction of $U$ is in Derivation §C5a.1.12; nothing here re-proves it.

^der-c5a-1-14

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-13|Theorem §C5a.1.13]], [[Linear map lemma|LADR Thm. 3.4]], [[§10 Invertibility and Isomorphisms#^ladr-3-81|LADR Thm. 3.81]]

> [!remark]- ★ Remark: The complexified Clifford algebra is the full matrix algebra
> Let $\mathrm{Cl}$ be the complex associative algebra generated by four symbols $\gamma^\mu$ subject only to $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$ (the complexified Clifford algebra of Minkowski space). Step 1 of Derivation §C5a.1.6 used only these relations to rewrite any product as $\pm$ one of the sixteen ordered products $\Gamma_A$, so $\dim\mathrm{Cl} \le 16$. A four-dimensional representation maps $\mathrm{Cl}$ onto $M_4(\mathbb C)$, because the images of the $\Gamma_A$ are a basis of $M_4(\mathbb C)$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 4); a surjection onto a 16-dimensional space from a space of dimension at most 16 is an isomorphism ([[Fundamental theorem of linear maps|LADR Thm. 3.21]]): $\mathrm{Cl} \cong M_4(\mathbb C)$. A representation of the Clifford algebra is therefore the same as a module over the matrix algebra $M_4(\mathbb C)$, and by the structure theory of matrix algebras (not proved in the vault) every such module is a direct sum of copies of $\mathbb C^4$. This is the algebraic reason behind Pauli's theorem and behind "at least $4\times4$": the irreducible module is unique and four-dimensional, and every representation has dimension $4k$.
>
> *Source: written here (none of the course sources states the isomorphism); the sixteen-element basis is PS §3.4, p. 50 and Theorem §C5a.1.6*

^rem-c5a-1-5

> [!remark]- Connections
> - The transformation rules of spinors and $\gamma$ matrices are the change-of-basis formula of linear algebra, $A = C^{-1}BC$ for operators and its dual and conjugate versions for covectors and forms; nothing specific to physics enters until the Clifford action — [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], [[§12 Duality#^ladr-3-112|LADR Def. 3.112]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]].
> - The index rule for spinors is the same slot rule as for spacetime tensors, with $U$ in place of $\Lambda$ and no metric to raise or lower; spinor indices are matrix indices of the third kind in the index-slot classification — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1|Def. §C3.1.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
> - Pauli's theorem is the Clifford-algebra analogue of "spin ½ is unique up to basis": both follow because the generated matrix algebra is all of $M_n(\mathbb C)$, so the representation is irreducible and Schur's lemma pins the intertwiner — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]].
> - Spinor space is unique up to isomorphism for the same reason spin ½ is: the generated matrix algebra is all of $M_n(\mathbb C)$, so the representation is irreducible and Schur's lemma pins the intertwiner; the ★ remark identifies the whole Clifford algebra with $M_4(\mathbb C)$ — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]].
> - $\sigma^\mu$ and $\bar\sigma^\mu$ are to Weyl spinors what $\gamma^\mu$ is to Dirac spinors, and $\gamma^\mu$ is literally built from them in the chiral basis — [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]].
> - The sixteen products are the matrices of the fermion bilinears (scalar, pseudoscalar, vector, axial vector, tensor) and of every trace identity used in scattering amplitudes — [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]].
> - Component by component, the quantum field is four operators $\hat\psi_a$ with c-number coefficients $u^s_a(p)$; a change of basis acts on the index $a$ of both, never on the mode operators — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-3|§C5b.2, Remark: A spinor-valued operator, component by component]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]].
> - The layers of spinor space mirror those of Minkowski space: a vector space, then an algebraic structure (the Clifford product here, the metric there), then a group that preserves it; for spinors the Clifford action comes before any group, and the Lorentz algebra is built from it — [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
