---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.8 Gamma-Matrix Technology]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5b.1 Canonical Quantization of the Dirac Field]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–42, eqs. (3.22)–(3.30) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)"), §8.3 (What each spinor index labels: table, Principle "Invariant tensors with mixed slots", "The practical test, continued"), Ch. 10 §10.3 (The quantum Dirac field) · PHY 513 Lecture 7 (Larsen), Part B ("There are many realizations of $\gamma^\mu$"); Lecture 8, Part A (slide "Interpretation": "$\gamma^\nu$ are just numbers. They do not transform!") and Part C ("Lorentz generators are block-diagonal (in our basis)") · Yu Zhao-Huan, 量子场论讲义, §5.1–§5.2, eqs. (5.55)–(5.61), (5.72) · the user's pre-course notes, §5.1 (paragraph "Hermiticity"), §5.2 (Note "Four linear spaces tied to Lorentz transformations"; "all representations are related by unitary similarity transformations") · Schwartz, Quantum Field Theory and the Standard Model, §10.3, p. 170, eq. (10.74), and §11.3, p. 192 (the Majorana representation; ★ only) · Axler, Linear Algebra Done Right (the vault's Linear Algebra notes) for every linear-algebra fact, linked where used · much of the basis-free organization is written here.*

What is a Dirac spinor before anyone writes a column of four numbers, and what exactly changes when the $\gamma$ matrices are switched from the chiral basis to another one? §C5a.2 defined the Dirac matrices by their algebra ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), proved that all $4\times4$ solutions are related by $\gamma'^\mu = U\gamma^\mu U^{-1}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]) and gave that $U$ for the Dirac basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^ex-c5a-2-1|Example §C5a.2.1]]), but only for the matrices; §C5a.3 built $\bar\psi = \psi^\dagger\gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) in one fixed basis. This section supplies the missing structure, one layer at a time, each layer a `##` block: (1) a four-dimensional complex vector space $V$ and its bases, where all transformation rules are the change-of-basis formula of linear algebra; (2) the slots of covectors and operators, which decide those rules; (3) the Clifford action $\Gamma^\mu$ on $V$, unique up to equivalence; (4) the Dirac form, the Hermitian form behind $\bar\psi$, basis-free exactly for unitary changes of basis; (5) the Minkowski slot of $\gamma^\mu$, which makes it an invariant tensor for the Lorentz group but not for a change of basis; (6) the Dirac equation and Lagrangian in any basis; (7) why each basis is used.

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; spinor indices are Latin $a, b, c, d \in \{1, 2, 3, 4\}$, never raised or lowered, all written as subscripts, contracted by plain sums; spacetime indices Greek ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]]). Operators on $V$ are written $\Gamma^\mu$, $M$, …, their matrices $\gamma^\mu$, …; $\operatorname{End}(V)$ is the space of linear maps $V \to V$ (Axler's $\mathcal L(V)$). $\psi$ is a c-number spinor or a classical field (no hat); the quantum field is $\hat\psi$.

## Layer 1: The vector space V and its bases

> [!definition] Definition §C5a.9.1: Spinor Space
> **Spinor space** is a complex vector space $V$ of dimension $4$ ([[§2 Definition of Vector Space#^ladr-1-20|LADR Def. 1.20]]). A **Dirac spinor** (at one point) is an element $\psi \in V$.
>
> *Source: Yu §5.2, eq. (5.55) (the spinor as a vector of the representation space) · the user's pre-course notes, §5.2 (Note "Four linear spaces": "the spinor representation space (4-dim, elements $\psi_a$)") · the user's PHY 513 notes, Ch. 8 §8.3 (table: "$\psi_a$: a vector in spinor space $\mathbb C^4$") · the basis-free formulation written here*

^def-c5a-9-1

> [!remark] Remark: What this layer contains, and what it does not
> At this layer $V$ is only a vector space: spinors can be added and multiplied by complex numbers, and nothing else. It has no preferred basis (so no "upper" and "lower" components), no inner product (so no $\psi^\dagger\psi$ that means anything), no Lorentz action and no $\gamma$ matrices. Each later layer adds one structure: the Clifford action $\Gamma^\mu$ (Layer 3), a Hermitian form (Layer 4), the Lorentz action $\Lambda_{1/2}$ and its relation to $\Gamma^\mu$ (Layer 5). The column $\mathbb C^4$ of the lecture appears only after a basis is chosen, and every statement about it has to be checked for independence of that choice.
>
> *Source: written here, organizing PS §3.2, pp. 40–42 and the user's PHY 513 notes, Ch. 8 §8.3*

^rem-c5a-9-1

> [!definition] Definition §C5a.9.2: Components of a Spinor in a Basis
> Let $e = (e_1, e_2, e_3, e_4)$ be a basis of spinor space $V$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-1|Def. §C5a.9.1]]; bases, [[§5 Bases#^ladr-2-26|LADR Def. 2.26]]). The **components** $\psi_a$ of $\psi \in V$ are the unique numbers with
>
> $$
> \psi = \sum_{a=1}^4\psi_a\,e_a ,
> $$
>
> and the column $(\psi_1, \psi_2, \psi_3, \psi_4)^{\mathsf T} \in \mathbb C^4$ is the matrix of $\psi$ in that basis ([[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR Def. 3.73]]). The column is also written $\psi$ when the basis is fixed.
>
> *Source: LADR Def. 3.73 · Yu §5.2, eq. (5.55)*

^def-c5a-9-2

> [!definition] Definition §C5a.9.3: The Matrix of a Linear Map on Spinor Space
> For a linear map $M \in \operatorname{End}(V)$ and a basis $e$ of $V$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-2|Def. §C5a.9.2]]), the **matrix** of $M$ is the $4\times4$ array $(M_{ab})$ with
>
> $$
> M\,e_b = \sum_{a=1}^4 M_{ab}\,e_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the components of $Me_b$ ([[§9 Matrices#^ladr-3-31|LADR Def. 3.31]]). The first index is the row, the second the column.
>
> *Source: LADR Def. 3.31*

^def-c5a-9-3

> [!theorem] Theorem §C5a.9.1: Linear Maps Act by Matrix Multiplication
> In a fixed basis of $V$ (with [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-3|Def. §C5a.9.3]]), for $M, N \in \operatorname{End}(V)$, $\psi \in V$, $\lambda \in \mathbb C$:
>
> $$
> (M\psi)_a = \sum_b M_{ab}\psi_b, \qquad (MN)_{ab} = \sum_c M_{ac}N_{cb}, \qquad (M + \lambda N)_{ab} = M_{ab} + \lambda N_{ab}, \qquad (\mathrm{id})_{ab} = \delta_{ab} .
> $$
>
> So "an operator acting on a spinor" is a matrix times a column, and every algebraic identity among operators holds verbatim among their matrices.
>
> *Source: [[§10 Invertibility and Isomorphisms#^ladr-3-76|LADR Thm. 3.76]], [[§9 Matrices#^ladr-3-43|LADR Thm. 3.43]], [[§9 Matrices#^ladr-3-35|LADR Thm. 3.35]] · Yu §5.2, eq. (5.56) ("the product on the right is a matrix times a column vector")*

^thm-c5a-9-1

> [!derivation]- Derivation
> **1. Action.** $M\psi = M\bigl(\sum_b\psi_be_b\bigr) = \sum_b\psi_b\,Me_b$ (linearity of $M$) $= \sum_b\psi_b\sum_aM_{ab}e_a$ (Def. §C5a.9.3) $= \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a$ (exchange of two finite sums). Components are unique (Def. §C5a.9.2), so $(M\psi)_a = \sum_bM_{ab}\psi_b$.
>
> **2. Product.** $(MN)e_b = M(Ne_b) = M\bigl(\sum_cN_{cb}e_c\bigr) = \sum_cN_{cb}\sum_aM_{ac}e_a = \sum_a\bigl(\sum_cM_{ac}N_{cb}\bigr)e_a$; read off the coefficient of $e_a$.
>
> **3. Sum and identity.** $(M + \lambda N)e_b = \sum_a(M_{ab} + \lambda N_{ab})e_a$; $\mathrm{id}\,e_b = e_b = \sum_a\delta_{ab}e_a$.
>
> **What the derivation shows**
> - Only linearity and the uniqueness of components are used: the matrix calculus of the lecture is the calculus of $\operatorname{End}(V)$ written in one basis.
> - Used next: in a new basis the same operator has a new matrix (Theorem §C5a.9.2), and the Clifford relation survives in every basis (Theorem §C5a.9.5).

^der-c5a-9-1

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-3|Def. §C5a.9.3]]

> [!definition] Definition §C5a.9.4: The Change-of-Basis Matrix
> Let $e$ (old) and $e'$ (new) be two bases of $V$. The **change-of-basis matrix** $U$ is the $4\times4$ matrix with
>
> $$
> e_b = \sum_{a=1}^4U_{ab}\,e'_a \qquad (b = 1, \dots, 4):
> $$
>
> column $b$ lists the new components of the old basis vector $e_b$. In Axler's notation $U = \mathcal M(\mathrm{id}, (e), (e'))$, and it is invertible, with $e'_b = \sum_a(U^{-1})_{ab}\,e_a$ ([[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]).
>
> *Source: LADR Thm. 3.82, Thm. 3.84 (its matrix $C$) · the convention for $U$ fixed here so that $\gamma'^\mu = U\gamma^\mu U^{-1}$, as in Theorem §C5a.2.5 and the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness"); other conventions: Caution below*

^def-c5a-9-4

> [!theorem] Theorem §C5a.9.2: Components Change with U, Matrices with U and U⁻¹
> With the change-of-basis matrix $U$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]), for every $\psi \in V$ and $M \in \operatorname{End}(V)$:
>
> $$
> \psi'_a = \sum_bU_{ab}\,\psi_b, \quad\text{i.e.}\quad \psi' = U\psi ; \qquad M'_{ab} = \sum_{c,d}U_{ac}\,M_{cd}\,(U^{-1})_{db}, \quad\text{i.e.}\quad M' = UMU^{-1} .
> $$
>
> One index, one $U$; a row index gets $U$ from the left, a column index $U^{-1}$ from the right. This is the change-of-basis formula of linear algebra ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], whose $A = C^{-1}BC$ is $M = U^{-1}M'U$).
>
> *Source: LADR Thm. 3.76, Thm. 3.84 · Yu §5.2, eq. (5.72) (the similarity transformation, in the opposite naming of $U$) · the index-by-index derivation written here*

^thm-c5a-9-2

> [!derivation]- Derivation
> **1. The inverse relation.** Claim $e'_b = \sum_a(U^{-1})_{ab}e_a$. Insert $e_a = \sum_dU_{da}e'_d$ (Def. §C5a.9.4) into the right side: $\sum_a(U^{-1})_{ab}\sum_dU_{da}e'_d = \sum_d\bigl(\sum_aU_{da}(U^{-1})_{ab}\bigr)e'_d = \sum_d(UU^{-1})_{db}e'_d = \sum_d\delta_{db}e'_d = e'_b$. ($U$ is invertible because the matrix of the identity from $e'$ back to $e$ is its inverse, LADR Thm. 3.82.)
>
> **2. Components.** $\psi = \sum_b\psi_be_b$ (old components) $= \sum_b\psi_b\sum_aU_{ab}e'_a$ (Def. §C5a.9.4) $= \sum_a\bigl(\sum_bU_{ab}\psi_b\bigr)e'_a$. The new components are unique (Def. §C5a.9.2), so $\psi'_a = \sum_bU_{ab}\psi_b$.
>
> **3. Matrices.** Apply $M$ to a new basis vector and express everything in the new basis:
>
> $$
> Me'_b \overset{(1)}{=} \sum_c(U^{-1})_{cb}\,Me_c \overset{\text{Def. 9.3}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\,e_d \overset{\text{Def. 9.4}}{=} \sum_c(U^{-1})_{cb}\sum_dM_{dc}\sum_aU_{ad}\,e'_a = \sum_a\Bigl(\sum_{d,c}U_{ad}M_{dc}(U^{-1})_{cb}\Bigr)e'_a .
> $$
>
> By Def. §C5a.9.3 in the new basis the bracket is $M'_{ab}$, and it is the $(a, b)$ entry of the triple product $UMU^{-1}$ (Theorem §C5a.9.1, product rule twice).
>
> **4. Consistency check.** $(M\psi)' = U(M\psi) = UMU^{-1}U\psi = M'\psi'$: computing $M\psi$ in either basis gives the same vector of $V$.
>
> **What the derivation shows**
> - The rules are not physics: they are the bookkeeping of one vector and one linear map in two bases. $\psi$ has one $V$-index, hence one factor $U$; $M$ has a row index (a $V$-slot) and a column index (contracted with $\psi$), hence $U$ on the left and $U^{-1}$ on the right. Which kind of index gets which factor is Layer 2 (Theorem §C5a.9.3).
> - Used next: the Dirac matrices are matrices of operators (Theorem §C5a.9.5), so $\gamma'^\mu = U\gamma^\mu U^{-1}$ is this theorem, not an additional rule.

^der-c5a-9-2

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-3|Def. §C5a.9.3]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-1|Theorem §C5a.9.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR Thm. 3.82]]

> [!remark] Remark: Why "UψU⁻¹" means nothing
> $\psi$ is a $4\times1$ column and $U$ a $4\times4$ matrix: $U\psi$ is a column, but $\psi U^{-1}$ is a $4\times1$ times a $4\times4$, which is not defined. The shape reflects the slot count: a spinor has one $V$-slot, so it takes one factor (Theorem §C5a.9.2); only objects with two spinor slots, such as $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$ or $\psi\bar\chi$ (a column times a row, $4\times4$), take the sandwich. A sandwich $U^{-1}\hat\psi U$ does occur in field theory, with the unitary operator $U(\Lambda)$ on the Hilbert space; it acts on the operator nature of $\hat\psi$, not on its spinor index (Caution: Three different transformations, Layer 5).
>
> *Source: written here · the user's PHY 513 notes, Ch. 10 §10.3 ("The operator carries the quantum, particle-like aspect; the column and the plane wave carry the wave aspect and all the Lorentz structure")*

^rem-c5a-9-2

> [!caution] Caution: Which matrix is called U
> Here $U$ converts old components into new ones, $\psi' = U\psi$, $\gamma' = U\gamma U^{-1}$, as in Pauli's theorem ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]), the user's PHY 513 notes and the matrix of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^ex-c5a-2-1|Example §C5a.2.1]] (there old = Dirac basis, new = chiral basis). Yu (5.72) writes $\gamma'^\mu = U^\dagger\gamma^\mu U$ with $U$ unitary, so Yu's $U$ is the inverse of this one; Axler's $C$ in LADR Thm. 3.84 is this $U$; Sakurai's transformation matrix gives (new) $= U^\dagger$(old), again the inverse ([[§C1.4 Change of Basis and Unitary Equivalence#^cau-c1-4-1|QM, Caution: Which matrix is called U]]). Before using a formula, check which basis labels the rows of the source's $U$.
>
> *Source: Yu §5.2, eq. (5.72) · LADR Thm. 3.84 · Sakurai §1.5.2 (as recorded in QM C1.4)*

^cau-c5a-9-1

## Layer 2: Slots — covectors, operators and the index rule

> [!definition] Definition §C5a.9.5: Dual Spinor Space and Dual Basis
> The **dual spinor space** $V'$ is the space of linear functionals $\varphi : V \to \mathbb C$ ([[§12 Duality#^ladr-3-110|LADR Def. 3.110]]). The **dual basis** $(\varepsilon^1, \dots, \varepsilon^4)$ of a basis $e$ is defined by $\varepsilon^a(e_b) = \delta_{ab}$ ([[§12 Duality#^ladr-3-112|LADR Def. 3.112]]). The **components** of $\varphi \in V'$ are $\varphi_a \equiv \varphi(e_a)$, written as a row $(\varphi_1, \dots, \varphi_4)$; then $\varphi = \sum_a\varphi_a\varepsilon^a$ and $\varphi(\psi) = \sum_a\varphi_a\psi_a$, a row times a column.
>
> *Source: LADR Def. 3.110, Def. 3.112, Thm. 3.114 · the row picture: the user's PHY 513 notes, Ch. 8 §8.3 ("contracting them is plain matrix multiplication")*

^def-c5a-9-5

> [!definition] Definition §C5a.9.6: Spinor Tensors and Their Slots
> A **spinor tensor of type $(k, l)$** is an element of $V^{\otimes k}\otimes V'^{\otimes l}$ ([[§38 Tensor Products#^ladr-9-71|LADR Def. 9.71]]; $V'$ of [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-5|Def. §C5a.9.5]]): it has $k$ **$V$-slots** and $l$ **$V'$-slots**. In a basis $e$ with dual basis $\varepsilon$ its **components** $T_{a_1\dots a_k;\,b_1\dots b_l}$ are the coefficients of $e_{a_1}\otimes\dots\otimes e_{a_k}\otimes\varepsilon^{b_1}\otimes\dots\otimes\varepsilon^{b_l}$. A **contraction** sets one $V$-index equal to one $V'$-index and sums. Examples: a spinor $\psi$ is type $(1, 0)$, a row $\varphi$ type $(0, 1)$, a linear map $M \in \operatorname{End}(V)$ type $(1, 1)$ through $M = \sum_{a,b}M_{ab}\,e_a\otimes\varepsilon^b$, a number type $(0, 0)$.
>
> *Source: LADR Def. 9.71, Def. 9.88 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "transforming all of its indices at once, each by the rule of its own slot") · the identification $\operatorname{End}(V) \cong V\otimes V'$ written here (Derivation §C5a.9.3, step 2)*

^def-c5a-9-6

> [!theorem] Theorem §C5a.9.3: The Slot Rule
> Under a change of basis with matrix $U$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]), the components of a spinor tensor ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-6|Def. §C5a.9.6]]) change by one factor per slot:
>
> $$
> T'_{a_1\dots a_k;\,b_1\dots b_l} = \sum U_{a_1c_1}\cdots U_{a_kc_k}\;T_{c_1\dots c_k;\,d_1\dots d_l}\;(U^{-1})_{d_1b_1}\cdots(U^{-1})_{d_lb_l} ,
> $$
>
> $U$ for each $V$-slot, $U^{-1}$ (from the right) for each $V'$-slot. In particular a row transforms as $\varphi' = \varphi U^{-1}$, an operator as $M' = UMU^{-1}$ (agreeing with [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]]), and a contraction of a $V$-slot with a $V'$-slot removes both factors: a fully contracted expression is the same number in every basis.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"; "The practical test, continued") · LADR Thm. 9.73 (multilinearity of ⊗) · the general rule and its derivation written here*

^thm-c5a-9-3

> [!derivation]- Derivation
> **1. The dual basis.** Expand $\varepsilon^b$ in the new dual basis $\varepsilon'$: its coefficients are its values on the new basis vectors (LADR Thm. 3.114 applied in $V'$). By step 1 of Derivation §C5a.9.2, $\varepsilon^b(e'_c) = \varepsilon^b\bigl(\sum_d(U^{-1})_{dc}e_d\bigr) = \sum_d(U^{-1})_{dc}\delta_{bd} = (U^{-1})_{bc}$, so $\varepsilon^b = \sum_c(U^{-1})_{bc}\,\varepsilon'^c$.
>
> **2. Operators as tensors.** The matrix units $E^{(ab)} \equiv e_a\otimes\varepsilon^b$ act as $\psi \mapsto \varepsilon^b(\psi)\,e_a = \psi_b\,e_a$. Then $\sum_{a,b}M_{ab}\,\varepsilon^b(\psi)\,e_a = \sum_a\bigl(\sum_bM_{ab}\psi_b\bigr)e_a = M\psi$ (Theorem §C5a.9.1), so $M = \sum M_{ab}\,e_a\otimes\varepsilon^b$. The sixteen $E^{(ab)}$ span $\operatorname{End}(V)$ by this formula and are independent (apply to $e_c$), and $\dim(V\otimes V') = 16$ ([[§38 Tensor Products#^ladr-9-72|LADR Thm. 9.72]]): $\operatorname{End}(V) \cong V\otimes V'$.
>
> **3. One factor per slot.** Insert $e_{c} = \sum_aU_{ac}e'_{a}$ (Def. §C5a.9.4) into every $V$-slot and $\varepsilon^{d} = \sum_b(U^{-1})_{db}\varepsilon'^{b}$ (step 1) into every $V'$-slot of $T = \sum T_{c_1\dots;\,d_1\dots}\,e_{c_1}\otimes\dots\otimes\varepsilon^{d_1}\otimes\dots$. The tensor product is linear in each factor (LADR Thm. 9.73), so the factors pull out of each slot separately, and the coefficient of $e'_{a_1}\otimes\dots\otimes\varepsilon'^{b_1}\otimes\dots$ is the displayed formula.
>
> **4. The cases.** Type $(0, 1)$: $\varphi'_b = \sum_d\varphi_d(U^{-1})_{db}$, i.e. $\varphi' = \varphi U^{-1}$; also directly, $\varphi'_b = \varphi(e'_b) = \sum_d(U^{-1})_{db}\varphi(e_d)$. Type $(1, 1)$: $M'_{ab} = \sum U_{ac}M_{cd}(U^{-1})_{db}$, Theorem §C5a.9.2 again.
>
> **5. Contraction.** Contract a $V$-index $a$ with a $V'$-index $b$ of $T'$: the two factors become $\sum_aU_{ac}(U^{-1})_{da} = (U^{-1}U)_{dc} = \delta_{dc}$, so the contracted components transform with the remaining slots only. With every slot contracted, nothing remains: $\varphi'\psi' = \varphi U^{-1}U\psi = \varphi\psi$, $\varphi'M'\psi' = \varphi M\psi$.
>
> **What the derivation shows**
> - The "index rule" of the course (one $U$ per index, sandwiches for matrices, invariant scalars) is the transformation law of tensor components, with $V$ and $V'$ as the two kinds of slot. It needs no physics and no metric.
> - ⚑ By-product: $\psi^\dagger$ is *not* a $V'$-slot. Its components $\psi_a^{\ast}$ transform as $(\psi')^{\ast} = U^{\ast}\psi^{\ast}$, i.e. the row $\psi'^\dagger = \psi^\dagger U^\dagger$, which is the $V'$-rule $\psi^\dagger U^{-1}$ only when $U^\dagger = U^{-1}$ → Theorem §C5a.9.11. The row that *is* a $V'$-slot for every $U$ is $\bar\psi$, once defined basis-free (Def. §C5a.9.12).
> - Used next: trace and eigenvalues (Theorem §C5a.9.4); the table in the remark below.

^der-c5a-9-3

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-5|Def. §C5a.9.5]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-6|Def. §C5a.9.6]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-1|Theorem §C5a.9.1]], [[§12 Duality#^ladr-3-114|LADR Thm. 3.114]], [[§38 Tensor Products#^ladr-9-73|LADR Thm. 9.73]]

> [!theorem] Theorem §C5a.9.4: Trace, Determinant and Eigenvalues Do Not Depend on the Basis
> For $M \in \operatorname{End}(V)$ with matrices $M$ and $M' = UMU^{-1}$ in two bases ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]]):
>
> $$
> \operatorname{tr}M' = \operatorname{tr}M, \qquad \det M' = \det M, \qquad \det(z\mathbb 1 - M') = \det(z\mathbb 1 - M) ,
> $$
>
> so the eigenvalues of $M$ with their multiplicities are properties of the operator, not of the basis ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-50|LADR Thm. 8.50]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]], [[§37 Determinants#^ladr-9-63|LADR Def. 9.63]]). The trace is the contraction of the two slots of $M$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-3|Theorem §C5a.9.3]]).
>
> *Source: LADR Thm. 8.49, Thm. 8.50, Thm. 9.52, Def. 9.63*

^thm-c5a-9-4

> [!derivation]- Derivation
> **1. Trace.** $\operatorname{tr}(UMU^{-1}) = \operatorname{tr}\bigl((UM)U^{-1}\bigr) = \operatorname{tr}\bigl(U^{-1}(UM)\bigr) = \operatorname{tr}M$, by $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]). As a contraction: $\operatorname{tr}M = \sum_aM_{aa}$ contracts the $V$-slot with the $V'$-slot (step 5 of Derivation §C5a.9.3).
>
> **2. Determinant.** $\det(UMU^{-1}) = \det M$ (LADR Thm. 9.52 with $S = U^{-1}$).
>
> **3. Characteristic polynomial.** $z\mathbb 1 - UMU^{-1} = U(z\mathbb 1 - M)U^{-1}$, because $U(z\mathbb 1)U^{-1} = z\mathbb 1$. Step 2 gives $\det(z\mathbb 1 - M') = \det(z\mathbb 1 - M)$. Its zeros, with multiplicities, are the eigenvalues (LADR Def. 9.63).
>
> **What the derivation shows**
> - Every statement of the form "$\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$" or "$\gamma^5$ has eigenvalues $\pm1$" is a statement about operators on $V$ and can be checked in any one basis ([[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-3|Theorem §C5a.8.3]]).
> - Statements about individual entries ("$\gamma^0$ is off-diagonal", "the upper two components") are not of this kind.

^der-c5a-9-4

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]], [[§37 Determinants#^ladr-9-52|LADR Thm. 9.52]]

> [!remark] Remark: The index rule as a table
>
> | object | slots (Def. §C5a.9.6) | shape | new components | why |
> |---|---|---|---|---|
> | spinor $\psi$, $u^s(p)$, $v^s(p)$ | $V$ | $4\times1$ | $U\psi$ | Theorem §C5a.9.2 |
> | row $\varphi \in V'$, e.g. $\bar\psi$ (Def. §C5a.9.12) | $V'$ | $1\times4$ | $\varphi U^{-1}$ | Theorem §C5a.9.3 |
> | $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$, $\slashed{p}$, $P_L$, $\psi\bar\chi$ | $V\otimes V'$ | $4\times4$ | $U(\cdot)U^{-1}$ | Theorems §C5a.9.2, §C5a.9.5 |
> | $\psi^\dagger$ | conjugate of $V$ | $1\times4$ | $\psi^\dagger U^\dagger$ ($= \psi^\dagger U^{-1}$ iff $U$ unitary) | Derivation §C5a.9.3 |
> | matrix of the Dirac form, $\gamma^0$ in that role | form on $V$ | $4\times4$ | $(U^{-1})^\dagger(\cdot)U^{-1}$ | Theorem §C5a.9.8 |
> | $\bar\psi\chi$, $\bar\psi\gamma^\mu\chi$, $\operatorname{tr}(\gamma^\mu\gamma^\nu)$, eigenvalues | none (all contracted) | number | unchanged | Theorems §C5a.9.3, §C5a.9.4, §C5a.9.11 |
>
> The spacetime index $\mu$ of $\gamma^\mu$ is not touched by a change of basis of $V$; it belongs to Minkowski space (Layer 5).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (table of what each index labels) · [[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-6|§C5a.2, Remark: What each Dirac index labels]] · the rule column written here*

^rem-c5a-9-3

## Layer 3: The Clifford action

> [!definition] Definition §C5a.9.7: The Dirac Maps
> The **Dirac maps** on spinor space $V$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-1|Def. §C5a.9.1]]) are four linear maps $\Gamma^0, \Gamma^1, \Gamma^2, \Gamma^3 \in \operatorname{End}(V)$ with
>
> $$
> \Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}\,\mathrm{id}_V ,
> $$
>
> $g^{\mu\nu}$ the metric ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]): a representation of the Clifford algebra on $V$. In a basis their matrices ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-3|Def. §C5a.9.3]]) are written $\gamma^\mu$: $\Gamma^\mu e_b = \sum_a(\gamma^\mu)_{ab}e_a$.
>
> *Source: PS §3.2, eq. (3.22), p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent") · PHY 513 Lecture 7, Part B ("There are many realizations of $\gamma^\mu$") · Yu §5.1, eq. (5.1) · the basis-free formulation written here*

^def-c5a-9-7

> [!theorem] Theorem §C5a.9.5: The Matrices of the Dirac Maps in Any Basis
> For the Dirac maps ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-7|Def. §C5a.9.7]]):
> 1. in every basis of $V$ the matrices $\gamma^\mu$ are Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), and under a change of basis $\gamma'^\mu = U\gamma^\mu U^{-1}$;
> 2. the operators $\Gamma^5 = i\Gamma^0\Gamma^1\Gamma^2\Gamma^3$, $S^{\mu\nu} = \frac i4[\Gamma^\mu, \Gamma^\nu]$ and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ have, in each basis, the matrices computed by the formulas of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-7|Def. §C5a.2.7]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]] from that basis's $\gamma$'s, and these transform as $U(\cdot)U^{-1}$;
> 3. $\Gamma^0$ and $\Gamma^5$ have eigenvalues $+1$ and $-1$, each twice, and $\Gamma^i$ has $+i$ and $-i$, each twice; all four are diagonalizable.
>
> *Source: Yu §5.2, eq. (5.72) · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness": "the choice of basis is a convention") · parts 2–3 written here*

^thm-c5a-9-5

> [!derivation]- Derivation
> **1. Clifford relation in a basis.** By Theorem §C5a.9.1 the matrix of $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu$ is $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu$ and that of $2g^{\mu\nu}\mathrm{id}$ is $2g^{\mu\nu}\mathbb 1$; equal operators have equal matrices. The rule $\gamma'^\mu = U\gamma^\mu U^{-1}$ is Theorem §C5a.9.2 with $M = \Gamma^\mu$. (Directly: $\{U\gamma^\mu U^{-1}, U\gamma^\nu U^{-1}\} = U\{\gamma^\mu, \gamma^\nu\}U^{-1} = 2g^{\mu\nu}\mathbb 1$, Yu (5.72).)
>
> **2. Products.** The matrix of $\Gamma^5$ is $i\gamma^0\gamma^1\gamma^2\gamma^3$ (product rule of Theorem §C5a.9.1). In the new basis, inserting $U^{-1}U = \mathbb 1$ between factors: $i\gamma'^0\gamma'^1\gamma'^2\gamma'^3 = iU\gamma^0U^{-1}U\gamma^1U^{-1}U\gamma^2U^{-1}U\gamma^3U^{-1} = U(i\gamma^0\gamma^1\gamma^2\gamma^3)U^{-1}$: computing $\gamma^5$ from the new $\gamma$'s gives the transformed old $\gamma^5$. The same for $[\gamma'^\mu, \gamma'^\nu] = U[\gamma^\mu, \gamma^\nu]U^{-1}$, hence $S'^{\mu\nu} = US^{\mu\nu}U^{-1}$.
>
> **3. Exponentials.** With $A = -\frac i2\omega_{\mu\nu}S^{\mu\nu}$: $(UAU^{-1})^n = UA^nU^{-1}$ (the inner $U^{-1}U$ cancel), so term by term $\exp(UAU^{-1}) = \sum_n\frac1{n!}UA^nU^{-1} = U\,e^A\,U^{-1}$ (the series converges absolutely, and multiplication by fixed matrices is continuous). So $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$.
>
> **4. Eigenvalues of Γ⁰ and Γ⁵.** $(\Gamma^0)^2 = \mathrm{id}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]]), so the minimal polynomial of $\Gamma^0$ divides $z^2 - 1 = (z - 1)(z + 1)$, which has distinct zeros: $\Gamma^0$ is diagonalizable with eigenvalues in $\{1, -1\}$ ([[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]]). Its trace is $0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 2), and the trace is the sum of the eigenvalues with multiplicity ([[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]]): $n_+ - n_- = 0$ with $n_+ + n_- = 4$, so $n_\pm = 2$. The same argument with $(\Gamma^5)^2 = \mathrm{id}$, $\operatorname{tr}\Gamma^5 = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]).
>
> **5. Eigenvalues of Γⁱ.** $(\Gamma^i)^2 = -\mathrm{id}$: minimal polynomial divides $(z - i)(z + i)$; trace $0$ gives $i(n_+ - n_-) = 0$, so $n_\pm = 2$.
>
> **What the derivation shows**
> - Only the Clifford relation and the trace were used, so part 3 holds in every basis: "$\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$" (Dirac basis) and "$\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$" (chiral basis) are each the operator written in its own eigenbasis; the off-diagonal $\gamma^0$ of the chiral basis has the same eigenvalues (Theorem §C5a.9.4).
> - ⚑ By-product: no basis makes $\gamma^0$ and $\gamma^5$ both diagonal. Diagonal matrices commute, but $\gamma^0\gamma^5 = -\gamma^5\gamma^0$, so commuting would force $\gamma^0\gamma^5 = 0$, impossible for invertible matrices. Choosing a basis means choosing which structure to make visible → Remark: Why each basis is used (Layer 7).

^der-c5a-9-5

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-1|Theorem §C5a.9.1]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§17 Diagonalizable Operators#^ladr-5-62|LADR Thm. 5.62]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-52|LADR Thm. 8.52]]

> [!definition] Definition §C5a.9.8: Intertwiners of Clifford Representations
> Let $\Gamma^\mu$ on $V$ and $\tilde\Gamma^\mu$ on $\tilde V$ satisfy the Clifford relation ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-7|Def. §C5a.9.7]]). A linear map $T : V \to \tilde V$ is an **intertwiner** if $T\,\Gamma^\mu = \tilde\Gamma^\mu\,T$ for $\mu = 0, \dots, 3$; the two representations are **equivalent** if an invertible intertwiner exists. The same words apply to two sets of $4\times4$ matrices acting on columns $\mathbb C^4$. (Intertwiners for groups and Lie algebras: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]; equivalence: [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]].)
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition, "Equivalence and reducibility": "they differ only by a change of basis") · PS §3.2, p. 41 ("unitarily equivalent") · the Clifford version written here*

^def-c5a-9-8

> [!theorem] Theorem §C5a.9.6: Changes of Basis Are the Invertible Intertwiners
> 1. If $\gamma^\mu$ and $\gamma'^\mu$ are the matrices of the Dirac maps in bases $e$ and $e'$, the change-of-basis matrix $U$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]) is an invertible intertwiner ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-8|Def. §C5a.9.8]]) from $\gamma^\mu$ to $\gamma'^\mu$: $U\gamma^\mu = \gamma'^\mu U$.
> 2. Conversely, if $\gamma^\mu$ are the matrices in a basis $e$ and $U$ is invertible with $U\gamma^\mu U^{-1} = \tilde\gamma^\mu$, then $e'_b \equiv \sum_a(U^{-1})_{ab}e_a$ is a basis in which the Dirac maps have the matrices $\tilde\gamma^\mu$, and $U$ is its change-of-basis matrix.
>
> *Source: Yu §5.2, eq. (5.72) ("all representations are equivalent, related by similarity transformations") · the user's PHY 513 notes, Ch. 7 §7.2 · part 2 written here*

^thm-c5a-9-6

> [!derivation]- Derivation
> **1. Part 1.** Theorem §C5a.9.5, 1 gives $\gamma'^\mu = U\gamma^\mu U^{-1}$; multiply on the right by $U$.
>
> **2. Part 2: e′ is a basis.** The list $e'$ is the image of $e$ under the invertible operator whose matrix in $e$ is $U^{-1}$, so it is a basis.
>
> **3. Part 2: its change-of-basis matrix.** $\sum_aU_{ab}e'_a = \sum_aU_{ab}\sum_c(U^{-1})_{ca}e_c = \sum_c(U^{-1}U)_{cb}e_c = e_b$, which is Def. §C5a.9.4 with matrix $U$.
>
> **4. Part 2: the matrices.** By Theorem §C5a.9.2 the matrices of $\Gamma^\mu$ in $e'$ are $U\gamma^\mu U^{-1} = \tilde\gamma^\mu$.
>
> **What the derivation shows**
> - "Two realizations of the $\gamma$ matrices" and "one set of Dirac maps in two bases" are the same thing. A similarity transformation of the $\gamma$'s alone is a change of basis of $V$ only if the spinors' components are changed with it (Theorem §C5a.9.13).

^der-c5a-9-6

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]

> [!theorem] Theorem §C5a.9.7: Spinor Space Is Unique up to Isomorphism
> 1. If $(V, \Gamma^\mu)$ and $(\tilde V, \tilde\Gamma^\mu)$ are two four-dimensional complex spaces with Dirac maps ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-7|Def. §C5a.9.7]]), there is an invertible intertwiner $T : V \to \tilde V$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-8|Def. §C5a.9.8]]), unique up to a nonzero factor.
> 2. Given $(V, \Gamma^\mu)$, every set of $4\times4$ Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]) — chiral, Dirac, Majorana or any other — is the set of matrices of the $\Gamma^\mu$ in some basis of $V$, and that basis is unique up to multiplying all its vectors by one nonzero number.
>
> This is Pauli's theorem ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]) read without a basis: there is one spinor space, and a choice of $\gamma$ matrices is a choice of basis in it.
>
> *Source: PS §3.2, p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent. We thus need only write one explicit realization") · the user's PHY 513 notes, Ch. 8 §8.1 ("Uniqueness (Pauli's fundamental theorem)") · the basis-free reading written here*

^thm-c5a-9-7

> [!derivation]- Derivation
> **1. Part 1: existence.** Choose bases $e$ of $V$ and $\tilde e$ of $\tilde V$, with matrices $\gamma^\mu$ and $\tilde\gamma^\mu$ (Dirac matrices by Theorem §C5a.9.5). Pauli's theorem gives an invertible $U$ with $\tilde\gamma^\mu = U\gamma^\mu U^{-1}$. Define $T$ by $Te_b = \sum_aU_{ab}\tilde e_a$ (a linear map is fixed by its values on a basis, [[Linear map lemma|LADR Thm. 3.4]]); its matrix is $U$ (Def. §C5a.9.3, from $e$ to $\tilde e$), it is invertible, and the matrices of $T\Gamma^\mu$ and $\tilde\Gamma^\mu T$ are $U\gamma^\mu$ and $\tilde\gamma^\mu U$ ([[§10 Invertibility and Isomorphisms#^ladr-3-81|LADR Thm. 3.81]]), which are equal. Equal matrices, equal maps.
>
> **2. Part 1: uniqueness.** If $T$ and $T'$ are both invertible intertwiners, $T^{-1}T'$ commutes with every $\Gamma^\mu$; its matrix commutes with every $\gamma^\mu$, hence is $c\mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 4), $c \ne 0$: $T' = cT$.
>
> **3. Part 2: existence.** Fix a basis $e$ with matrices $\gamma^\mu$; Pauli's theorem gives $\tilde\gamma^\mu = U\gamma^\mu U^{-1}$, and Theorem §C5a.9.6, 2 produces the basis.
>
> **4. Part 2: uniqueness.** If $f$ and $f'$ both give $\tilde\gamma^\mu$, their change-of-basis matrix $W$ satisfies $W\tilde\gamma^\mu W^{-1} = \tilde\gamma^\mu$, so $W = c\mathbb 1$ (as in step 2), i.e. $f_b = cf'_b$ for all $b$.
>
> **What the derivation shows**
> - ⚑ By-product: the only freedom left once the $\gamma$ matrices are chosen is an overall factor of the basis, which multiplies every spinor's components by $c^{-1}$ and leaves every matrix unchanged. Whether $\bar\psi\psi$ notices it is Theorem §C5a.9.11, 2: it does, by $|c|^{-2}$, unless $|c| = 1$.
> - The averaging construction of $U$ is in Derivation §C5a.2.5; nothing here re-proves it.

^der-c5a-9-7

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-6|Theorem §C5a.9.6]], [[Linear map lemma|LADR Thm. 3.4]], [[§10 Invertibility and Isomorphisms#^ladr-3-81|LADR Thm. 3.81]]

> [!remark]- ★ Remark: The complexified Clifford algebra is the full matrix algebra
> Let $\mathrm{Cl}$ be the complex associative algebra generated by four symbols $\gamma^\mu$ subject only to $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$ (the complexified Clifford algebra of Minkowski space). Step 1 of Derivation §C5a.2.4 used only these relations to rewrite any product as $\pm$ one of the sixteen ordered products $\Gamma_A$, so $\dim\mathrm{Cl} \le 16$. A four-dimensional representation maps $\mathrm{Cl}$ onto $M_4(\mathbb C)$, because the images of the $\Gamma_A$ are a basis of $M_4(\mathbb C)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 4); a surjection onto a 16-dimensional space from a space of dimension at most 16 is an isomorphism ([[Fundamental theorem of linear maps|LADR Thm. 3.21]]): $\mathrm{Cl} \cong M_4(\mathbb C)$. A representation of the Clifford algebra is therefore the same as a module over the matrix algebra $M_4(\mathbb C)$, and by the structure theory of matrix algebras (not proved in the vault) every such module is a direct sum of copies of $\mathbb C^4$. This is the algebraic reason behind Pauli's theorem and behind "at least $4\times4$": the irreducible module is unique and four-dimensional, and every representation has dimension $4k$.
>
> *Source: written here (none of the course sources states the isomorphism); the sixteen-element basis is PS §3.4, p. 50 and Theorem §C5a.2.4*

^rem-c5a-9-4

## Layer 4: The Dirac form

> [!definition] Definition §C5a.9.9: Hermitian Form and Its Matrix
> A **Hermitian form** on $V$ is a map $h : V\times V \to \mathbb C$ that is linear in the second argument, conjugate-linear in the first, and satisfies $h(\chi, \psi) = h(\psi, \chi)^{\ast}$. It is **nondegenerate** if $h(\chi, \psi) = 0$ for all $\chi$ implies $\psi = 0$. Its **matrix** in a basis $e$ is $H_{ab} = h(e_a, e_b)$. An inner product is a positive-definite Hermitian form ([[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]], which puts the linear slot first; the physics order is used here).
>
> *Source: LADR Def. 6.2 and its Remark "Convention warning (physics)" · LADR Def. 9.4 (the matrix of a bilinear form, the real analogue) · written here for the indefinite case*

^def-c5a-9-9

> [!theorem] Theorem §C5a.9.8: How a Hermitian Form Changes with the Basis
> For a Hermitian form $h$ with matrix $H$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-9|Def. §C5a.9.9]]):
> 1. $h(\chi, \psi) = \chi^\dagger H\psi = \sum_{a,b}\chi_a^{\ast}H_{ab}\psi_b$, $H^\dagger = H$, and $h$ is nondegenerate iff $\det H \ne 0$;
> 2. under a change of basis with matrix $U$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]),
>
> $$
> H' = (U^{-1})^\dagger\,H\,U^{-1} ;
> $$
>
> 3. this agrees with the operator rule $H \mapsto UHU^{-1}$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]]) for every Hermitian $H$ iff $U$ is unitary, $U^\dagger U = \mathbb 1$ ([[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]]).
>
> *Source: the analogue of [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]] ($A = C^{\mathsf t}BC$) and its Remark "Contrast with operators" · the Hermitian version written here*

^thm-c5a-9-8

> [!derivation]- Derivation
> **1. Formula.** $h(\chi, \psi) = h\bigl(\sum_a\chi_ae_a, \sum_b\psi_be_b\bigr) = \sum_{a,b}\chi_a^{\ast}\psi_b\,h(e_a, e_b)$: conjugate-linearity pulls out $\chi_a^{\ast}$, linearity pulls out $\psi_b$. $H_{ab} = h(e_a, e_b) = h(e_b, e_a)^{\ast} = H_{ba}^{\ast}$, i.e. $H^\dagger = H$.
>
> **2. Nondegeneracy.** $h(\chi, \psi) = 0$ for all $\chi$ iff $\chi^\dagger(H\psi) = 0$ for all columns $\chi$ iff $H\psi = 0$ (take $\chi = H\psi$). So $h$ is nondegenerate iff $H$ has trivial kernel iff $\det H \ne 0$ ([[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]).
>
> **3. Change of basis.** With $e'_b = \sum_c(U^{-1})_{cb}e_c$ (step 1 of Derivation §C5a.9.2):
>
> $$
> H'_{ab} = h(e'_a, e'_b) = \sum_{c,d}(U^{-1})_{ca}^{\ast}\,(U^{-1})_{db}\,h(e_c, e_d) = \sum_{c,d}\bigl((U^{-1})^\dagger\bigr)_{ac}H_{cd}(U^{-1})_{db} ,
> $$
>
> using $(U^{-1})^{\ast}_{ca} = ((U^{-1})^\dagger)_{ac}$. Check: $\chi'^\dagger H'\psi' = \chi^\dagger U^\dagger(U^{-1})^\dagger HU^{-1}U\psi = \chi^\dagger H\psi$, since $U^\dagger(U^\dagger)^{-1} = \mathbb 1$ and $(U^{-1})^\dagger = (U^\dagger)^{-1}$.
>
> **4. Comparison.** If $U^\dagger U = \mathbb 1$, then $(U^{-1})^\dagger = (U^\dagger)^{-1} = U$, and $H' = UHU^{-1}$ for every $H$. Conversely, if the two rules agree for $H = \mathbb 1$ (a Hermitian matrix), $(U^{-1})^\dagger U^{-1} = UU^{-1} = \mathbb 1$, i.e. $(UU^\dagger)^{-1} = \mathbb 1$, so $UU^\dagger = \mathbb 1$ and $U$ is unitary (LADR Thm. 7.57 (d)).
>
> **What the derivation shows**
> - A $4\times4$ array can be the matrix of an operator (slots $V\otimes V'$) or of a form (two conjugate-and-dual slots); the two transform differently, and only unitary changes of basis hide the difference — the Hermitian counterpart of "operators are $(1,1)$-tensors, bilinear forms $(0,2)$-tensors" in LADR's remark to Thm. 9.7.
> - Used next: $\gamma^0$ is used in both roles (Remark: γ⁰ in two roles).

^der-c5a-9-8

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-9|Def. §C5a.9.9]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]]

> [!definition] Definition §C5a.9.10: Signature of a Hermitian Form
> Let $h$ be a nondegenerate Hermitian form on $V$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-9|Def. §C5a.9.9]]). A subspace $W \subseteq V$ is **positive** (**negative**) if $h(\psi, \psi) > 0$ ($< 0$) for every nonzero $\psi \in W$. The **signature** of $h$ is $(p, q)$, with $p$ and $q$ the largest dimensions of a positive and of a negative subspace. It is defined without a basis.
>
> *Source: written here (the real analogue: diagonalization of quadratic forms, [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR Thm. 9.23]])*

^def-c5a-9-10

> [!definition] Definition §C5a.9.11: Hermitian Basis
> A basis of $V$ is **Hermitian** (for the Dirac maps, [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-7|Def. §C5a.9.7]]) if the matrices satisfy $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ for $\mu = 0, \dots, 3$, i.e. $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]). The chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]) is one.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices") · the user's pre-course notes, §5.1 ("Hermiticity": "hypothesis; … arrangeable by a change of basis") · Yu §5.1, eqs. (5.4)–(5.7) · the name written here*

^def-c5a-9-11

> [!definition] Definition §C5a.9.12: The Dirac Form and the Dirac Adjoint
> In a Hermitian basis ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-11|Def. §C5a.9.11]]) the **Dirac form** is the Hermitian form ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-9|Def. §C5a.9.9]]) with matrix $\gamma^0$:
>
> $$
> h_D(\chi, \psi) = \chi^\dagger\gamma^0\psi .
> $$
>
> The **Dirac adjoint** of $\psi \in V$ is the functional $\bar\psi \equiv h_D(\psi, \cdot\,) \in V'$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-5|Def. §C5a.9.5]]); its row of components is $\psi^\dagger\gamma^0$, the Dirac conjugate of [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]. The map $\psi \mapsto \bar\psi$, $V \to V'$, is conjugate-linear.
>
> *Source: PS §3.2, eq. (3.32) · the user's PHY 513 notes, Ch. 8 §8.3 ("$\gamma^0$ for Dirac spinors, giving the invariant $\bar\psi\chi = \psi^\dagger\gamma^0\chi$") · Yu §5.3, eq. (5.90) · the form-and-functional formulation written here*

^def-c5a-9-12

The definition uses one Hermitian basis; that the result does not depend on which one, up to a factor fixed by convention, is Theorems §C5a.9.9 and §C5a.9.11. $h_D$ is Hermitian because $(\chi^\dagger\gamma^0\psi)^{\ast} = \psi^\dagger\gamma^{0\dagger}\chi = \psi^\dagger\gamma^0\chi$, and nondegenerate because $\det\gamma^0 \ne 0$ ($(\gamma^0)^2 = \mathbb 1$). The components of $\bar\psi$: $\bar\psi(\chi) = \sum_b(\psi^\dagger\gamma^0)_b\chi_b$, so by Def. §C5a.9.5 its row is $\psi^\dagger\gamma^0$; conjugate-linearity is $(\lambda\psi)^\dagger = \lambda^{\ast}\psi^\dagger$.

> [!theorem] Theorem §C5a.9.9: The Dirac Maps Are Self-Adjoint for the Dirac Form, and Fix It up to a Real Factor
> 1. $h_D(\Gamma^\mu\chi, \psi) = h_D(\chi, \Gamma^\mu\psi)$ for all $\chi, \psi \in V$ and $\mu = 0, \dots, 3$ ($h_D$ of [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]]); in components, $\overline{\gamma^\mu\chi} = \bar\chi\gamma^\mu$.
> 2. If $h$ is any nondegenerate Hermitian form on $V$ for which every $\Gamma^\mu$ is self-adjoint in this sense, then $h = c\,h_D$ for a real $c \ne 0$.
>
> So the Dirac form is determined by the Dirac maps alone, up to a real normalization: a basis-free characterization of $\bar\psi$.
>
> *Source: part 1: the identity $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ of the user's PHY 513 notes, Ch. 8 §8.1 and PS §3.2, read as self-adjointness here · part 2 written here*

^thm-c5a-9-9

> [!derivation]- Derivation
> Work in a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$.
>
> **1. Self-adjointness.** $h_D(\Gamma^\mu\chi, \psi) = (\gamma^\mu\chi)^\dagger\gamma^0\psi = \chi^\dagger\gamma^{\mu\dagger}\gamma^0\psi = \chi^\dagger\gamma^0\gamma^\mu\gamma^0\gamma^0\psi = \chi^\dagger\gamma^0\gamma^\mu\psi = h_D(\chi, \Gamma^\mu\psi)$, using $(\gamma^0)^2 = \mathbb 1$. The middle equality reads $\overline{\gamma^\mu\chi} = (\gamma^\mu\chi)^\dagger\gamma^0 = \bar\chi\gamma^\mu$.
>
> **2. The condition on a matrix.** Let $H$ be the matrix of $h$ (Theorem §C5a.9.8, 1). Self-adjointness of $\Gamma^\mu$ means $(\gamma^\mu\chi)^\dagger H\psi = \chi^\dagger H\gamma^\mu\psi$ for all columns, i.e. $\gamma^{\mu\dagger}H = H\gamma^\mu$ (take $\chi$, $\psi$ standard basis columns).
>
> **3. Reduce to a commutant.** Insert $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$: $\gamma^0\gamma^\mu\gamma^0H = H\gamma^\mu$. Multiply on the left by $\gamma^0$: $\gamma^\mu(\gamma^0H) = (\gamma^0H)\gamma^\mu$. So $\gamma^0H$ commutes with all four $\gamma^\mu$, hence $\gamma^0H = c\mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 4), and $H = c\gamma^0$.
>
> **4. The factor.** $H^\dagger = H$ gives $c^{\ast}\gamma^0 = c\gamma^0$, so $c$ is real; nondegeneracy gives $c \ne 0$.
>
> **What the derivation shows**
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, used in §C5a.2 as a matrix identity, says that the Dirac maps are self-adjoint for $h_D$ — not for the positive form $\chi^\dagger\psi$ (for which the $\gamma^i$ are anti-self-adjoint).
> - ⚑ By-product: the normalization of $\bar\psi$ is a convention. Both signs $c = \pm1$ are used in the literature with other metric signatures; with $g = (+,-,-,-)$ the choice $c = 1$ makes $\bar uu = 2m > 0$ ([[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-2|Theorem §C5a.7.2]]).
> - Used next: which changes of basis keep $c = 1$ (Theorem §C5a.9.11).

^der-c5a-9-9

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-11|Def. §C5a.9.11]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-8|Theorem §C5a.9.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]

> [!theorem] Theorem §C5a.9.10: The Dirac Form Has Signature (2, 2)
> The Dirac form $h_D$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]]) has signature $(2, 2)$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-10|Def. §C5a.9.10]]): it is nondegenerate and indefinite, and in a Hermitian basis the eigenspaces $W_\pm$ of $\gamma^0$ (eigenvalues $\pm1$, each twice) are a positive and a negative subspace of maximal dimension.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary)) and [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]] ("indefinite, with eigenvalues $+1, +1, -1, -1$") · the signature argument written here*

^thm-c5a-9-10

> [!derivation]- Derivation
> **1. Eigenspaces.** In a Hermitian basis $\gamma^0$ is Hermitian, hence normal, so $\mathbb C^4$ has an orthonormal (for $\chi^\dagger\psi$) basis of its eigenvectors ([[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]]); its eigenvalues are $\pm1$, each twice (Theorem §C5a.9.5, 3). So $\mathbb C^4 = W_+\oplus W_-$ with $\dim W_\pm = 2$.
>
> **2. Signs on the eigenspaces.** For $\psi \in W_+$, $h_D(\psi, \psi) = \psi^\dagger\gamma^0\psi = \psi^\dagger\psi > 0$ if $\psi \ne 0$; for $\psi \in W_-$, $h_D(\psi, \psi) = -\psi^\dagger\psi < 0$. So $p \ge 2$ and $q \ge 2$.
>
> **3. No larger positive subspace.** Let $P$ be positive with $\dim P \ge 3$. Then $\dim P + \dim W_- \ge 5 > 4$, so $P\cap W_-$ contains some $\psi \ne 0$ (the dimension of a sum is at most $4$, [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]). On it $h_D(\psi, \psi)$ is $> 0$ (in $P$) and $< 0$ (in $W_-$), a contradiction. So $p = 2$; the same argument with $W_+$ gives $q = 2$.
>
> **What the derivation shows**
> - $p$ and $q$ are defined without a basis, so the signature is a property of the Dirac form itself; a real rescaling $c$ (Theorem §C5a.9.9) keeps it $(2, 2)$ (a negative $c$ exchanges $p$ and $q$).
> - ⚑ By-product: there is no positive Lorentz-invariant density built from $\bar\psi$ alone: the invariant form is indefinite, and the positive $\psi^\dagger\psi$ is not invariant ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-3|Derivation §C5a.3.3]]); the conserved positive density of Quantum Mechanics is the time component of a current ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]).
> - The signature $(2, 2)$ is the spinor counterpart of the Minkowski signature $(1, 3)$ of $g$; both are invariant forms preserved by the corresponding Lorentz matrices ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]).

^der-c5a-9-10

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-10|Def. §C5a.9.10]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]], [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]

> [!theorem] Theorem §C5a.9.11: Which Changes of Basis Preserve ψ̄
> Let $e$ be a Hermitian basis ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-11|Def. §C5a.9.11]]), $U$ any invertible change-of-basis matrix ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-4|Def. §C5a.9.4]]), $\psi' = U\psi$, $\gamma'^\mu = U\gamma^\mu U^{-1}$.
> 1. The Dirac-conjugate formula applied in the new basis gives $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger(U^\dagger U)\gamma^0\chi$. It equals $h_D(\psi, \chi) = \bar\psi\chi$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]]) for all $\psi, \chi$ iff $U$ is unitary.
> 2. The new basis is Hermitian iff $U^\dagger U = c\,\mathbb 1$ with $c > 0$, i.e. $U = \sqrt c\,W$ with $W$ unitary; then $\psi'^\dagger\gamma'^0\chi' = c\,\bar\psi\chi$.
> 3. For unitary $U$: $\psi'^\dagger = \psi^\dagger U^{-1}$, $\bar\psi' = \bar\psi\,U^{-1}$, and every bilinear $\bar\psi M\chi$ with $M \in \operatorname{End}(V)$ ($M' = UMU^{-1}$) is unchanged.
>
> So $\bar\psi = \psi^\dagger\gamma^0$ defines the same object in all Hermitian bases related by unitary matrices, and not otherwise. Part 2 for $c = 1$ is [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], 2; Pauli's theorem guarantees that two Hermitian bases are related by a unitary $U$ up to this factor ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]], 2).
>
> *Source: PS §3.2, p. 41 ("unitarily equivalent") · Yu §5.2, eq. (5.72) (unitary $U$) · the user's pre-course notes, §5.2 ("all representations are related by unitary similarity transformations") · parts 1–2 and the converses written here*

^thm-c5a-9-11

> [!derivation]- Derivation
> **1. Part 1.** $\psi'^\dagger = (U\psi)^\dagger = \psi^\dagger U^\dagger$ and $\gamma'^0\chi' = U\gamma^0U^{-1}U\chi = U\gamma^0\chi$, so $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger U^\dagger U\gamma^0\chi$. This equals $\psi^\dagger\gamma^0\chi$ for all columns iff $U^\dagger U\gamma^0 = \gamma^0$ (take $\psi$, $\chi$ standard basis columns to read off each entry), iff $U^\dagger U = \mathbb 1$ (multiply on the right by $(\gamma^0)^{-1} = \gamma^0$).
>
> **2. Part 2: the condition.** The new basis is Hermitian iff $\gamma'^{\mu\dagger} = \gamma'^0\gamma'^\mu\gamma'^0$. Left side: $(U\gamma^\mu U^{-1})^\dagger = (U^\dagger)^{-1}\gamma^{\mu\dagger}U^\dagger = (U^\dagger)^{-1}\gamma^0\gamma^\mu\gamma^0U^\dagger$. Right side: $U\gamma^0U^{-1}U\gamma^\mu U^{-1}U\gamma^0U^{-1} = U\gamma^0\gamma^\mu\gamma^0U^{-1}$. Multiply both on the left by $U^\dagger$ and on the right by $U$: the condition is $\gamma^0\gamma^\mu\gamma^0\,(U^\dagger U) = (U^\dagger U)\,\gamma^0\gamma^\mu\gamma^0$ for every $\mu$.
>
> **3. Part 2: solve it.** For $\mu = 0$ it says $P \equiv U^\dagger U$ commutes with $\gamma^0$ ($(\gamma^0)^3 = \gamma^0$). Then $\gamma^\mu = \gamma^0(\gamma^0\gamma^\mu\gamma^0)\gamma^0$ is a product of matrices commuting with $P$, so $P$ commutes with every $\gamma^\mu$ and $P = c\mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 4). $c > 0$: $v^\dagger Pv = |Uv|^2 > 0$ for $v \ne 0$. Conversely $P = c\mathbb 1$ satisfies the condition. Then $W = U/\sqrt c$ has $W^\dagger W = \mathbb 1$, and part 1's computation gives $\psi'^\dagger\gamma'^0\chi' = \psi^\dagger(c\mathbb 1)\gamma^0\chi = c\,\bar\psi\chi$.
>
> **4. Part 3.** With $U^\dagger = U^{-1}$: $\psi'^\dagger = \psi^\dagger U^{-1}$; $\bar\psi' = \psi'^\dagger\gamma'^0 = \psi^\dagger U^{-1}U\gamma^0U^{-1} = \bar\psi U^{-1}$; $\bar\psi'M'\chi' = \bar\psi U^{-1}UMU^{-1}U\chi = \bar\psi M\chi$.
>
> **What the derivation shows**
> - ⚑ By-product: the class of Hermitian bases is closed under $U = \sqrt c\,W$, but $\bar\psi$ is only closed under $c = 1$. Example: $U = 2\cdot\mathbb 1$ leaves every $\gamma$ matrix unchanged (so the new basis is Hermitian), doubles every component, and multiplies $\bar\psi\psi$ by $4$. The $\gamma$'s fix the Dirac form only up to a factor (Theorem §C5a.9.9); demanding unitary changes of basis — equivalently, keeping $\psi^\dagger\psi$ of the standard columns as the reference inner product — fixes it. This is the normalization implicit in "$\bar\psi = \psi^\dagger\gamma^0$ in every basis".
> - In the language of Layer 2: a unitary $U$ makes the conjugate slot of $\psi^\dagger$ transform like a $V'$-slot, and the two roles of $\gamma^0$ (operator and form, Theorem §C5a.9.8) transform alike.
> - Used next: the Dirac Lagrangian is basis independent exactly for unitary $U$ (Theorem §C5a.9.14).

^der-c5a-9-11

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-11|Def. §C5a.9.11]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-12|Def. §C5a.9.12]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-8|Theorem §C5a.9.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]

> [!remark] Remark: γ⁰ in two roles
> The matrix $\gamma^0$ appears in two different jobs. As the matrix of the Dirac map $\Gamma^0$ it is an operator, slots $V\otimes V'$, and transforms as $U\gamma^0U^{-1}$; it enters the Dirac equation $i\gamma^0\partial_0\psi + \dots$. As the matrix of the Dirac form it pairs two spinors, $\bar\chi\psi = \chi^\dagger\gamma^0\psi$, and transforms as $(U^{-1})^\dagger\gamma^0U^{-1}$ (Theorem §C5a.9.8). In a Hermitian basis the two arrays coincide; after a non-unitary change of basis they differ, and the formula $\bar\psi = \psi^\dagger\gamma^0$, which silently identifies them, stops computing the Dirac form (Theorem §C5a.9.11, 1). The same double role is played by $g_{\mu\nu}$ for vectors in an orthonormal frame, and the same caution applies to non-orthonormal frames. Under Lorentz transformations the form role is the one preserved: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]).
>
> *Source: written here · the user's PHY 513 notes, Ch. 8 §8.3 ("Each spinor slot has its own invariant form in place of $g$: $\gamma^0$ for Dirac spinors")*

^rem-c5a-9-5

## Layer 5: The Minkowski slot of γ

> [!definition] Definition §C5a.9.13: Clifford Multiplication
> Let $M = \mathbb R^{1,3}$ be Minkowski space with metric $g$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]). **Clifford multiplication** is the map
>
> $$
> M\times V \to V, \qquad (a, \psi) \mapsto \slashed{a}\,\psi \equiv a_\mu\Gamma^\mu\psi, \qquad a_\mu = g_{\mu\nu}a^\nu ,
> $$
>
> with the Dirac maps $\Gamma^\mu$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-7|Def. §C5a.9.7]]; slash, [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]). It is linear in $a$ and in $\psi$, and $\slashed{a}\,\slashed{a}\,\psi = (a\cdot a)\,\psi$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], 2). As a tensor, $\Gamma = (\Gamma^\mu) \in M\otimes\operatorname{End}(V) \cong M\otimes V\otimes V'$, with components $(\gamma^\mu)_{ab}$: one Minkowski slot $\mu$, one $V$-slot $a$, one $V'$-slot $b$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-6|Def. §C5a.9.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "$\gamma^\mu$ is an invariant tensor with one spacetime slot and two spinor slots") · PS §3.2, p. 42 · the name and the map formulation written here*

^def-c5a-9-13

> [!theorem] Theorem §C5a.9.12: Clifford Multiplication Is Lorentz Equivariant
> Let $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ be built from the same $\omega$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]). Then, for Clifford multiplication ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-13|Def. §C5a.9.13]]):
> 1. $\Lambda_{1/2}\bigl(\slashed{a}\,\psi\bigr) = \slashed{(\Lambda a)}\,\bigl(\Lambda_{1/2}\psi\bigr)$ for all $a \in M$, $\psi \in V$: moving the vector and the spinor together moves their product;
> 2. equivalently, transforming all three slots of $\gamma^\mu$ returns it: $\Lambda^\mu{}_\nu\,\Lambda_{1/2}\,\gamma^\nu\,\Lambda_{1/2}^{-1} = \gamma^\mu$.
>
> Both are the covariance of $\gamma^\mu$, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]), read as a statement about an intertwiner $M\otimes V \to V$ for the Lorentz group.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots") · the equivariance form written here*

^thm-c5a-9-12

> [!derivation]- Derivation
> **1. Conjugate the slash.** $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = (\Lambda a)_\mu\,\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}$ (the numbers $(\Lambda a)_\mu$ pull out) $= (\Lambda a)_\mu\,\Lambda^\mu{}_\nu\gamma^\nu$ (Theorem §C5a.2.12, 1).
>
> **2. Lower the index explicitly.** $(\Lambda a)_\mu = g_{\mu\rho}\Lambda^\rho{}_\sigma a^\sigma$, so the coefficient of $\gamma^\nu$ is $g_{\mu\rho}\Lambda^\rho{}_\sigma\Lambda^\mu{}_\nu\,a^\sigma = g_{\sigma\nu}a^\sigma = a_\nu$, by the defining property $g_{\mu\rho}\Lambda^\mu{}_\nu\Lambda^\rho{}_\sigma = g_{\nu\sigma}$ of a Lorentz transformation ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]). Hence $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = a_\nu\gamma^\nu = \slashed{a}$.
>
> **3. Part 1.** Multiply step 2 on the left by $\Lambda_{1/2}$ and apply to $\psi$: $\slashed{(\Lambda a)}\,\Lambda_{1/2}\psi = \Lambda_{1/2}\,\slashed{a}\,\psi$.
>
> **4. Part 2.** From Theorem §C5a.2.12, 1, multiply on the left by $\Lambda_{1/2}$ and on the right by $\Lambda_{1/2}^{-1}$: $\gamma^\mu = \Lambda_{1/2}\,\Lambda^\mu{}_\nu\gamma^\nu\,\Lambda_{1/2}^{-1} = \Lambda^\mu{}_\nu\,\Lambda_{1/2}\gamma^\nu\Lambda_{1/2}^{-1}$. The three factors are the slot rules: $\Lambda$ on the Minkowski index, $\Lambda_{1/2}$ on the $V$-index (left), $\Lambda_{1/2}^{-1}$ on the $V'$-index (right) — the slot rule of Theorem §C5a.9.3 with the Lorentz matrices in place of $U$. This is the lecture's form $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-5|§C5a.2, Remark: The lecture's form of the covariance]]).
>
> **What the derivation shows**
> - Clifford multiplication is a map between representations of the Lorentz group (vector ⊗ Dirac → Dirac) that commutes with the group action; such a map is an intertwiner, and its components $(\gamma^\mu)_{ab}$ are an invariant tensor. This is why a $\gamma$ matrix never acquires a transformation of its own under a Lorentz transformation.
> - Assumption used: $\Lambda$ and $\Lambda_{1/2}$ come from the same $\omega$, i.e. $\Lambda$ is the image of $\Lambda_{1/2}$ under the covering map $SL(2, \mathbb C) \to SO^+(1,3)$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-8|Theorem §C5a.1.8]]); for a mismatched pair the identity fails ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-3|§C5a.2, Remark: One transformation, two matrices]]).
> - Used next: covariance of the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]]) is part 1 applied to $a = \partial$.

^der-c5a-9-12

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-13|Def. §C5a.9.13]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-3|Theorem §C5a.9.3]]

> [!remark] Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis
> $\gamma^\mu$ has three slots: Minkowski, $V$, $V'$. A **Lorentz transformation** acts on all of them at once — $\Lambda$ on the Minkowski slot, $\Lambda_{1/2}$ and $\Lambda_{1/2}^{-1}$ on the spinor slots — and returns the same array (Theorem §C5a.9.12, 2): "$\gamma^\nu$ are just numbers. They do not transform!" (Lecture 8). What transforms is $\psi$, and $\partial_\mu$ with it, and the equation keeps its form. A **change of basis of $V$** acts only on the spinor slots, with one $U$ and its inverse; the Minkowski slot is untouched because no basis of spacetime changes. Nothing compensates, so the array changes: $\gamma' = U\gamma U^{-1}$ (Theorem §C5a.9.5). In short, the Lorentz group acts on spacetime *and* spinor space and $\gamma$ is invariant under the combined action; $GL(V)$ acts on spinor space alone and $\gamma$ is merely covariant under it.
>
> *Source: PHY 513 Lecture 8, Part A (slide "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 · the comparison written here*

^rem-c5a-9-6

> [!caution] Caution: Three different transformations
> Three operations look alike on paper — a matrix multiplying $\psi$, sometimes a sandwich — and are unrelated:
>
> | | change of basis of $V$ | Lorentz transformation of a classical field | Lorentz transformation of the quantum field |
> |---|---|---|---|
> | what changes | the description (basis $e \to e'$) | the configuration (moved by $\Lambda$) | the state of the system, by $U(\Lambda)$ |
> | group | $GL(V)$, unitary for $\bar\psi$ to keep its form (Theorem §C5a.9.11) | $SL(2, \mathbb C)$ on $V$ together with $SO^+(1,3)$ on $M$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-8\|Theorem §C5a.1.8]]) | unitary operators on the Hilbert space ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1\|Principle §C3.5.1]]) |
> | $\psi$ | $\psi'(x) = U\psi(x)$, same point | $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5\|Def. §C5a.2.5]]) | $U(\Lambda)^{-1}\hat\psi(x)U(\Lambda) = \Lambda_{1/2}\hat\psi(\Lambda^{-1}x)$ ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8\|Principle §C3.5.8]]) |
> | $\gamma^\mu$ | $U\gamma^\mu U^{-1}$ | unchanged (Theorem §C5a.9.12) | unchanged |
> | $\partial_\mu$ | unchanged | $\Lambda_\mu{}^\nu\partial_\nu$ (chain rule) | as for the classical field |
> | acts on | spinor index only | spinor index and argument | operator nature (sandwich) and, through the law, spinor index and argument |
> | predictions | unchanged (Remark: What depends on the basis) | those of the moved system | those of the moved system |
>
> In the third column the sandwich $U(\Lambda)^{-1}\cdots U(\Lambda)$ acts on the Hilbert-space side of $\hat\psi$, while the single matrix $\Lambda_{1/2}$ acts on its spinor index (Yu (5.61); Peskin–Schroeder's equivalent form $U\hat\psi U^{-1} = \Lambda_{1/2}^{-1}\hat\psi(\Lambda x)$: [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-1|§C5b.4, Remark: Lorentz covariance of the quantized field]]; the two kinds of representation: [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]]). The letter $U$ is overloaded: the change-of-basis matrix $U$ is a constant $4\times4$ matrix, $U(\Lambda)$ an infinite-dimensional unitary operator. The operations are compatible: in a new basis the Lorentz law reads $\psi'(x) \mapsto \Lambda'_{1/2}\psi'(\Lambda^{-1}x)$ with $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$ (Theorem §C5a.9.5, 2), since $U\Lambda_{1/2}\psi = (U\Lambda_{1/2}U^{-1})(U\psi)$.
>
> *Source: Yu §5.2, eqs. (5.55)–(5.61) · the user's pre-course notes, §5.2 (Note "Four linear spaces tied to Lorentz transformations": spinor space with $D(\Lambda)$, Hilbert space with $U(\Lambda)$, "a field carries several of these actions at once") · the user's PHY 513 notes, Ch. 10 §10.3 · PS §3.5, eqs. (3.108)–(3.110) · the table written here*

^cau-c5a-9-2

## Layer 6: The Dirac equation and Lagrangian in any basis

> [!theorem] Theorem §C5a.9.13: The Dirac Equation Keeps Its Form When ψ and γ Change Together
> Let $\psi(x)$ be a $C^1$ field with values in $V$, with columns $\psi(x)$ and $\psi'(x) = U\psi(x)$ in two bases and Dirac matrices $\gamma^\mu$, $\gamma'^\mu = U\gamma^\mu U^{-1}$ ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-5|Theorem §C5a.9.5]]). Then
>
> $$
> \bigl(i\gamma'^\mu\partial_\mu - m\bigr)\psi'(x) = U\,\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi(x) ,
> $$
>
> so $\psi'$ solves the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) with $\gamma'$ iff $\psi$ solves it with $\gamma$: the equation is the basis-free statement $(i\Gamma^\mu\partial_\mu - m)\psi = 0$ about a $V$-valued field.
>
> *Source: Yu §5.2, eq. (5.72) (the similarity transformation of the $\gamma$'s) · PS §3.2, p. 41 · the derivation written here*

^thm-c5a-9-13

> [!derivation]- Derivation
> **1. The derivative passes through U.** $U$ is a constant matrix, so $\partial_\mu\psi'(x) = \partial_\mu(U\psi(x)) = U\partial_\mu\psi(x)$, component by component: $\partial_\mu\sum_bU_{ab}\psi_b = \sum_bU_{ab}\partial_\mu\psi_b$.
>
> **2. The kinetic term.** $\gamma'^\mu\partial_\mu\psi' = U\gamma^\mu U^{-1}U\partial_\mu\psi = U\gamma^\mu\partial_\mu\psi$ (insert step 1, cancel $U^{-1}U = \mathbb 1$).
>
> **3. The mass term.** $m\psi' = mU\psi = U(m\psi)$ ($m$ is a number times $\mathbb 1$, which commutes with $U$).
>
> **4. Combine.** $(i\gamma'^\mu\partial_\mu - m)\psi' = U(i\gamma^\mu\partial_\mu - m)\psi$. $U$ is invertible, so one side vanishes iff the other does.
>
> **5. ⚑ By-product: changing γ without ψ breaks solutions.** Take $U = \gamma^5$, which is unitary and its own inverse with $\gamma^5\gamma^\mu\gamma^5 = -\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]): the new matrices $\gamma'^\mu = -\gamma^\mu$ are a legitimate set of Dirac matrices. If $\psi$ solves the old equation, $i\gamma^\mu\partial_\mu\psi = m\psi$, and its columns are kept unchanged while only the $\gamma$'s are replaced, then $(i\gamma'^\mu\partial_\mu - m)\psi = -i\gamma^\mu\partial_\mu\psi - m\psi = -2m\psi \ne 0$ for $m \ne 0$, $\psi \ne 0$. The correctly transformed spinor $\psi' = \gamma^5\psi$ does solve it, by step 4. A solution is a pair (matrices, columns) in one basis.
>
> **What the derivation shows**
> - The form invariance needs only that $U$ is constant and invertible; unitarity is not used. (A position-dependent $U(x)$ would produce an extra term $i\gamma'^\mu(\partial_\mu U)U^{-1}\psi'$, the seed of a connection — not needed in flat spacetime with a global basis.)
> - Used next: Lagrangian (Theorem §C5a.9.14), which does need unitarity.

^der-c5a-9-13

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]

> [!theorem] Theorem §C5a.9.14: The Dirac Lagrangian under a Change of Basis
> With the hypotheses of [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-13|Theorem §C5a.9.13]], the old basis Hermitian ([[§C5a.9 Spinor Space, Bases and Transformation Rules#^def-c5a-9-11|Def. §C5a.9.11]]) and $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]):
>
> $$
> \mathcal L' \equiv \psi'^\dagger\gamma'^0\bigl(i\gamma'^\mu\partial_\mu - m\bigr)\psi' = \psi^\dagger\,(U^\dagger U)\,\gamma^0\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi .
> $$
>
> For $m \ne 0$, $\mathcal L' = \mathcal L$ for every field iff $U$ is unitary; for $U = \sqrt c\,W$ ($W$ unitary), $\mathcal L' = c\,\mathcal L$.
>
> *Source: the derivation written here, from Theorems §C5a.9.11 and §C5a.9.13 · PS §3.2, p. 41 (unitary equivalence)*

^thm-c5a-9-14

> [!derivation]- Derivation
> **1. The left factor.** $\psi'^\dagger\gamma'^0 = \psi^\dagger U^\dagger\,U\gamma^0U^{-1}$ (Theorem §C5a.9.11, step 1).
>
> **2. The right factor.** $(i\gamma'^\mu\partial_\mu - m)\psi' = U(i\gamma^\mu\partial_\mu - m)\psi$ (Theorem §C5a.9.13).
>
> **3. Multiply.** $\mathcal L' = \psi^\dagger U^\dagger U\gamma^0U^{-1}U(i\gamma^\mu\partial_\mu - m)\psi = \psi^\dagger(U^\dagger U)\gamma^0(i\gamma^\mu\partial_\mu - m)\psi$.
>
> **4. When equal.** If $U^\dagger U = \mathbb 1$, $\mathcal L' = \psi^\dagger\gamma^0(\cdots)\psi = \mathcal L$. Conversely, let $m \ne 0$ and $\mathcal L' = \mathcal L$ for all fields. Take constant fields ($\partial_\mu\psi = 0$): $-m\,\psi^\dagger A\psi = 0$ for every column $\psi$, with $A = (U^\dagger U - \mathbb 1)\gamma^0$. Over $\mathbb C$ a matrix with $\psi^\dagger A\psi = 0$ for all $\psi$ is zero (polarization, [[§23 Self-Adjoint and Normal Operators#^ladr-7-13|LADR Thm. 7.13]]), so $(U^\dagger U - \mathbb 1)\gamma^0 = 0$, and multiplying by $\gamma^0$ on the right, $U^\dagger U = \mathbb 1$. If $U^\dagger U = c\mathbb 1$, step 3 gives $c\mathcal L$.
>
> **What the derivation shows**
> - The field equation is basis independent for every invertible $U$ (Theorem §C5a.9.13), the Lagrangian only for unitary $U$. A factor $c$ rescales the action, which changes the normalization of the field (the canonical anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] would acquire $1/c$), not the dynamics.
> - The Lorentz scalar property of $\mathcal L$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-5|Theorem §C5a.3.5]]) is a different statement: there the basis is fixed and the field is moved (Caution: Three different transformations).

^der-c5a-9-14

*Uses:* [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.9 Spinor Space, Bases and Transformation Rules#^thm-c5a-9-13|Theorem §C5a.9.13]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-13|LADR Thm. 7.13]]

> [!example] Example §C5a.9.1: The Plane-Wave Spinors in the Dirac Basis
> *To be filled after Problem Set 6 is submitted (Oct 13).*

^ex-c5a-9-1

> [!remark] Remark: What depends on the basis and what does not
>
> | depends on the basis of $V$ | does not depend on it |
> |---|---|
> | the entries of $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$ | the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ (Theorem §C5a.9.5) |
> | the components $\psi_a$ of a spinor, $u^s_a(p)$, $v^s_a(p)$ | the spinor $\psi \in V$ itself; the solution space of the Dirac equation (Theorem §C5a.9.13) |
> | "upper and lower components" and what they mean | the eigenspaces of $\Gamma^5$ (the Weyl halves, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14\|Theorem §C5a.2.14]], 4) and of $\Gamma^0$ |
> | "$\gamma^0$ is off-diagonal", "$\gamma^5$ is diagonal", "$S^{\mu\nu}$ is block diagonal" | traces such as $\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$, determinants, eigenvalues: $\pm1$ twice for $\gamma^0$ and $\gamma^5$, $\pm i$ twice for $\gamma^i$ (Theorems §C5a.9.4, §C5a.9.5) |
> | whether $\psi^\dagger\gamma^0\chi$ is the Dirac form (fails for non-unitary $U$) | the Dirac form $\bar\psi\chi$ and every bilinear $\bar\psi\Gamma\chi$, under unitary $U$ (Theorem §C5a.9.11) |
> | the matrix form of the Lagrangian | $\mathcal L$, the action and the field equations, under unitary $U$ (Theorem §C5a.9.14) |
> | — | every physical prediction: cross sections, energies, charges are built from traces and bilinears |
>
> Pauli's theorem ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]) puts every possible set of Dirac matrices in the left column of a single row: each is the chiral set after a change of basis (Theorem §C5a.9.7), so a basis-independent statement proved in the chiral basis holds in all of them. The Dirac basis of Quantum Mechanics is such a basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^ex-c5a-2-1|Example §C5a.2.1]]; [[§C5a.2 The Clifford Algebra and the Dirac Representation#^cau-c5a-2-1|§C5a.2, Caution: Bases and conventions across the sources]]).
>
> *Source: PS §3.2, p. 41 · the user's PHY 513 notes, Ch. 8 §8.1 ("the choice of basis is a convention, like the choice of basis for spin-½"), §8.2 (Caution on "particle" and "antiparticle" components) · the table written here*

^rem-c5a-9-7

## Layer 7: Choosing a basis

> [!remark] Remark: Why each basis is used
> A basis can diagonalize $\gamma^0$ or $\gamma^5$, never both (⚑ in Derivation §C5a.9.5); each choice makes one structure visible.
> - **Chiral (Weyl) basis**, the course's ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]): $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, so the basis is adapted to the Weyl halves $\psi = (\psi_L, \psi_R)$; $S^{\mu\nu}$ and $\Lambda_{1/2}$ are block diagonal ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]; Lecture 8: "block-diagonal (in our basis)"), so the reduction $(\frac12, 0)\oplus(0, \frac12)$ is manifest; the Dirac equation splits into two-component equations coupled only by $m$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]]), which decouple for $m = 0$ into the Weyl fields ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]]); at high energy chirality becomes helicity ([[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-14|Theorem §C5a.7.14]]). Peskin–Schroeder use it "exclusively" as "especially convenient" (PS p. 41).
> - **Dirac (standard) basis**, Sakurai's ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]): $\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, adapted to the rest frame, where the time evolution is generated by $m\gamma^0$, and to the nonrelativistic limit, in which two components dominate and obey the Pauli equation ([[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]; Sakurai's free solutions, [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]]). Parity acts through $\gamma^0$ ($\Psi_P = \beta\Psi(-\mathbf x)$, [[§C13.2★ The Dirac Equation#^thm-c13-2-7|QM Theorem §C13.2.7]]), so here the upper and lower halves have intrinsic parity $+1$ and $-1$; in the chiral basis the same $\gamma^0$ exchanges the Weyl halves ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]]). This is the basis behind the heuristic "upper = particle, lower = antiparticle" ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^cau-c5a-2-2|§C5a.2, Caution: The upper components are not the particle]]).
> - **Majorana basis** (★, next remark): all $\gamma^\mu$ imaginary, adapted to reality.
>
> *Source: PS §3.2, p. 41 ("many field theory textbooks choose a different representation, in which $\gamma^0$ is diagonal") · PHY 513 Lecture 8, Part C · the user's PHY 513 notes, Ch. 8 §8.2 · Sakurai §8.2–§8.3 (as recorded in QM C13★) · the comparison written here*

^rem-c5a-9-8

> [!remark]- ★ Remark: The Majorana basis
> Schwartz gives a basis in which every Dirac matrix is purely imaginary,
>
> $$
> \gamma^0 = \begin{pmatrix}0 & \sigma^2\\ \sigma^2 & 0\end{pmatrix}, \quad \gamma^1 = \begin{pmatrix}i\sigma^3 & 0\\ 0 & i\sigma^3\end{pmatrix}, \quad \gamma^2 = \begin{pmatrix}0 & -\sigma^2\\ \sigma^2 & 0\end{pmatrix}, \quad \gamma^3 = \begin{pmatrix}-i\sigma^1 & 0\\ 0 & -i\sigma^1\end{pmatrix}
> $$
>
> (Schwartz (10.74); with $g = (+,-,-,-)$ and $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$, checked numerically here, as are $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, so the basis is Hermitian, and $\gamma^5$ imaginary). By Theorem §C5a.9.7 it is the chiral basis after a change of basis, unitary by Theorem §C5a.9.11, 2 up to a factor. In it $i\gamma^\mu$ is real, so the Dirac operator $i\gamma^\mu\partial_\mu - m$ has real coefficients: with $\psi$ also $\psi^{\ast}$ is a solution, and the condition $\psi^{\ast} = \psi$ is compatible with the equation (written here). Real solutions describe a field equal to its own conjugate; quantized, a fermion that is its own antiparticle, a **Majorana fermion** (Schwartz §11.3; Yu §9.6; QFT C9, planned; the two-component form of the Majorana mass: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^rem-c5a-4-3|§C5a.4, ★ Remark: A Majorana mass needs no second field]]). The Majorana basis is to reality what the chiral basis is to chirality.
>
> *Source: Schwartz, Quantum Field Theory and the Standard Model, §10.3, p. 170, eq. (10.74) ("In this basis the γ-matrices are purely imaginary"), §11.3, p. 192 ("Majorana fermions are their own antiparticles") · the reality argument written here*

^rem-c5a-9-9

> [!remark] Remark: The spin-½ analogy
> For spin $\frac12$, $S_x$ is the off-diagonal $\frac\hbar2\sigma_x$ in the $S_z$ basis and $\operatorname{diag}(\frac\hbar2, -\frac\hbar2)$ in its own eigenbasis; the unitary $U = (\sigma_x + \sigma_z)/\sqrt2$ relates the two and both matrices have eigenvalues $\pm\frac\hbar2$ ([[§C1.4 Change of Basis and Unitary Equivalence#^ex-c1-4-2|QM Example §C1.4.2]], [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-4|QM Theorem §C1.4.4]]). The Dirac case is the same pattern: $\gamma^0$ is off-diagonal in the chiral basis and diagonal in the Dirac basis, $\gamma^5$ the reverse, with eigenvalues $\pm1$ twice either way (Theorem §C5a.9.5). As $S_x$ and $S_z$ cannot be diagonal together because they do not commute, $\gamma^0$ and $\gamma^5$ cannot because they anticommute. And as changing the basis of the spin space changes the components of a spin state but not the state ([[§C1.4 Change of Basis and Unitary Equivalence#^rem-c1-4-1|QM, Remark: Changing the basis is not changing the state]]), changing the basis of $V$ changes $\psi_a$ but not $\psi$. One difference: the spin basis is changed by a unitary to keep probabilities, the spinor basis to keep $\bar\psi$ (Theorem §C5a.9.11) — the Dirac form, not an inner product, is what must be preserved.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 ("like the choice of basis for spin-½") · Sakurai §1.5.4 (as recorded in QM C1.4) · the comparison written here*

^rem-c5a-9-10

> [!remark]- Connections
> - The transformation rules of spinors and $\gamma$ matrices are the change-of-basis formula of linear algebra, $A = C^{-1}BC$ for operators and its dual and conjugate versions for covectors and forms; nothing specific to physics enters until Layer 3 — [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]], [[§12 Duality#^ladr-3-112|LADR Def. 3.112]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]].
> - The index rule for spinors is the same slot rule as for spacetime tensors, with $U$ in place of $\Lambda$ and no metric to raise or lower; spinor indices are matrix indices of the third kind in the index-slot classification — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1|Def. §C3.1.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
> - Spinor space is unique up to isomorphism for the same reason spin ½ is: the generated matrix algebra is all of $M_n(\mathbb C)$, so the representation is irreducible and Schur's lemma pins the intertwiner; the ★ remark identifies the whole Clifford algebra with $M_4(\mathbb C)$ — [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]].
> - The Dirac form is the invariant form of the spinor slot as $g$ is that of the vector slot and $\varepsilon$ that of a Weyl slot; its indefiniteness, signature $(2, 2)$, is the spinor face of the non-unitarity of finite-dimensional Lorentz representations — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-10|Theorem §C5a.1.10]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]].
> - The reality of bilinears and the self-adjointness of the Dirac maps for the Dirac form are one identity, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ — [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]].
> - Clifford multiplication being Lorentz equivariant is what makes $\slashed{\partial}\psi$ transform like $\psi$, hence the Dirac equation covariant and $\mathcal L$ a scalar; the same "invariant tensor" idea makes the Pauli matrices an invariant vector of $SU(2)$ — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-1|§C5a.3, Remark: What covariance shows and what it does not]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
> - A change of basis of $V$ and a Lorentz transformation act on the same spinor index but belong to different groups, and the Hilbert-space $U(\Lambda)$ acts on yet another space; the three are kept apart in the field transformation laws of C3 — [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]], [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]], [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]].
> - Component by component, the quantum field is four operators $\hat\psi_a$ with c-number coefficients $u^s_a(p)$; a change of basis acts on the index $a$ of both, never on the mode operators — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-3|§C5b.2, Remark: A spinor-valued operator, component by component]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]].
> - The Dirac basis of Quantum Mechanics is one point of the same orbit of bases; its parity and nonrelativistic structure are why Sakurai uses it — [[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^ex-c5a-2-1|Example §C5a.2.1]].
> - A basis of $V$ chosen independently at each point, $U = U(x)$, would spoil the form invariance by a term $(\partial_\mu U)U^{-1}$ (Derivation §C5a.9.13); compensating it needs a connection — the spin connection of field theory in curved spacetime, outside this course.
