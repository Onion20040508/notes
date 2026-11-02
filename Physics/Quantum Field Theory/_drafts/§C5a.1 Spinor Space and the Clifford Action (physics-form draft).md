---
type: draft
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
> [!warning] Draft for review — physics-form demo, not yet part of the chapter
> Rewrite of [[§C5a.1 Spinor Space and the Clifford Action]] to the physics-form principle (brief `qft-C/PHYSICS-FORM-BRIEF.md`, survey `qft-C/survey/PHYSICS-FORM.md`). Every ID carries the suffix `-d`; the real section is unchanged. Old boxes keep their numbers; the boxes new in this draft are numbered after them (Def. §C5a.1.4, Theorems §C5a.1.3–§C5a.1.7) and so appear out of numerical order.

| | before (real §C5a.1) | after (this draft) |
|---|---|---|
| lines in the file | 216 | 222 (body, without this banner and table) |
| lines as rendered (embeds expanded) | 502 (67 k characters) | 222 (34 k characters) |
| CB embeds (transclusions) | 33 (22 statements, 11 derivations/remarks/cautions) | 0 |
| boxes on screen | 42 (5 own statements, 2 own derivations, 2 remarks + 33 embedded CB boxes, 11 of them proofs) | 16 (11 statements: Def 1.1–1.4, Thm 1.1–1.7; 2 derivations; 2 remarks; 1 caution) |
| judgement tools shown | 10, of which 8 only through CB embeds | the same 10, all as physics boxes (list below) |
| CB/CA items cited | 22, embedded | 22, one line each in the folded *Mathematical background* list |

*What moved where.* The 15 embeds of §CB.0 (components, matrices, change of basis, slot rule, invariance of trace and eigenvalues) → one physics theorem (Thm §C5a.1.4) + one caution. The Dirac matrices and the Dirac maps (Def §CB.11.11, §CB.11.14) → one physics definition (Def §C5a.1.4) that states the algebra and shows the chiral basis. First consequences (Thm §CB.11.12) → Thm §C5a.1.3. Pauli's theorem and its basis-free reading (Thm §CB.13.12–14) → Thm §C5a.1.5. The sixteen products (Thm §CB.12.9) → Thm §C5a.1.6. Eigenvalues (Thm §CB.12.10) → Thm §C5a.1.7. All proofs stay in CB, linked from each box. The σ identities, the chiral basis and its check are unchanged.

*Judgement tools, before → after:* (1) γ algebra rules and $\slashed a\slashed a = a^2$: embed Thm §CB.11.12 → Thm §C5a.1.3; (2) change-of-basis rules $\psi' = U\psi$, $M' = UMU^{-1}$: embed Thm §CB.0.5 → Thm §C5a.1.4, 1–2; (3) one factor per slot, contracted expressions basis-free: embed Thm §CB.0.10 → Thm §C5a.1.4, 3; (4) trace, determinant, eigenvalues basis-free: embed Thm §CB.0.15 → Thm §C5a.1.4, 4; (5) any formula in γ's transforms as $U(\cdot)U^{-1}$: embed Thm §CB.11.15 → Thm §C5a.1.4, 2; (6) Pauli: basis independence of γ results: embeds Thm §CB.13.12–14 → Thm §C5a.1.5; (7) sixteen products, traceless, minimum size 4, Schur: embed Thm §CB.12.9 → Thm §C5a.1.6; (8) eigenvalues of γ⁰, γⁱ: embed Thm §CB.12.10 → Thm §C5a.1.7; (9) σ identities: Thm §C5a.1.1 → unchanged; (10) chiral matrices satisfy the algebra: Thm §C5a.1.2 → unchanged. Lost: none.

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–44, eqs. (3.22)–(3.25), (3.41)–(3.42), §3.4, pp. 49–50 · the user's PHY 513 notes, Ch. 8 §8.1 (The Dirac representation: Definition "The Dirac (Clifford) algebra", paragraphs "Square to ±1, or square root?" and "Uniqueness (Pauli's fundamental theorem)", Derivations "Checking the Dirac algebra in the chiral basis" and "Hermiticity of the Dirac matrices"), §8.2 (Derivation "The double cover made explicit"), §8.3 (What each spinor index labels) · PHY 513 Lecture 7 (Larsen), Part B ("There are many realizations of $\gamma^\mu$"); Lecture 8, Cheat Sheet I and Part C · PHY 513, Problem Set 5, Problem 5 (as the user wrote it; submitted) · PHY 513, Problem Set 6, Problem 3(a) (the user's solution) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.1)–(5.7), (5.45), p. 163, §5.2, eqs. (5.55), (5.68)–(5.75), Table 5.1, Exercise 3.7, eqs. (3.259)–(3.260) · the user's pre-course notes, §5.1–§5.2.*

What is a Dirac spinor, and what do the $\gamma$ matrices add to it? A Dirac spinor at a point is four complex numbers $\psi_a$, the components of a vector of a four-dimensional complex space $V$ in a basis; on $V$ act four $4\times4$ matrices $\gamma^\mu$ with $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$, the Dirac matrices. This section states both ingredients in the form the calculations use (Def. §C5a.1.1, Def. §C5a.1.4), the rules for computing with them and for changing the basis (Theorems §C5a.1.3–§C5a.1.4), and the facts that make every result basis independent (Theorems §C5a.1.5–§C5a.1.7); then it writes out the course's basis, the chiral basis, with $\sigma^\mu$ and $\bar\sigma^\mu$. The mathematics behind these statements (linear algebra in components, Clifford modules, Pauli's theorem) is proved in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]] and [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules|§CB.11]]–[[§CB.13 Complex Clifford Algebras and Clifford Modules|§CB.13]], linked from each box and listed at the end. The Dirac matrices of Quantum Mechanics are one such choice ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]). The Dirac form, the Lorentz action and chirality are [[§C5a.2 The Dirac Form|§C5a.2]]–[[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]; the layer-by-layer map of the chapter is [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]].

**Setup.** No field, no Lagrangian and no dynamics yet: every box is a statement about the space $V$, its bases and the matrices $\gamma^\mu$, so it holds for any element of $V$, whether the value of a classical field at a point, a c-number spinor such as $u(p)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates|§C5a.11]]), or the component column of the quantum field $\hat\psi$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]). The boxes are definitions and matrix identities, exact; they carry no *Model* line.

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis when a basis is fixed; spinor indices are Latin $a, b, c, d \in \{1, 2, 3, 4\}$, never raised or lowered, all written as subscripts, contracted by plain sums; spacetime indices Greek ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]]). The identity matrix in $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ is usually not written. Pauli matrices $\boldsymbol\sigma = (\sigma^1, \sigma^2, \sigma^3)$, with the product rule of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]. $\psi$ is a c-number spinor or a classical field (no hat); the quantum field is $\hat\psi$.

## Spinor space and the Dirac matrices

> [!definition] Definition §C5a.1.1: Spinor Space
> **Spinor space** is a complex vector space $V$ of dimension $4$ ([[§2 Definition of Vector Space#^ladr-1-20|LADR Def. 1.20]]). A **Dirac spinor** (at one point) is an element $\psi \in V$. In a basis $(e_1, \dots, e_4)$ it is the column of its four complex **components**, $\psi = \sum_a\psi_a e_a \leftrightarrow (\psi_1, \psi_2, \psi_3, \psi_4)^{\mathsf T} \in \mathbb C^4$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]]); how the column changes with the basis is [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-4-d|Theorem §C5a.1.4]].
>
> *Source: Yu §5.2, eq. (5.55) (the spinor as a vector of the representation space) and Table 5.1 · the user's pre-course notes, §5.2 (Note "Four linear spaces": "the spinor representation space (4-dim, elements $\psi_a$)") · the user's PHY 513 notes, Ch. 8 §8.3 (table: "$\psi_a$: a vector in spinor space $\mathbb C^4$") · the basis-free formulation written here*

^def-c5a-1-1-d

> [!remark] Remark: What this layer contains, and what it does not
> At this layer $V$ is only a vector space: spinors can be added and multiplied by complex numbers, and nothing else. It has no preferred basis (so no "upper" and "lower" components), no inner product (so no $\psi^\dagger\psi$ that means anything), no Lorentz action and no $\gamma$ matrices. Each later layer adds one structure: the Clifford action $\Gamma^\mu$ (Def. §C5a.1.4 below), a Hermitian form ([[§C5a.2 The Dirac Form|§C5a.2]]), the Lorentz action and its relation to $\Gamma^\mu$ ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]). The column $\mathbb C^4$ of the lecture appears only after a basis is chosen, and every statement about it has to be checked for independence of that choice ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-5-d|Theorem §C5a.1.5]]).
>
> *Source: written here, organizing PS §3.2, pp. 40–42 and the user's PHY 513 notes, Ch. 8 §8.3*

^rem-c5a-1-1-d

> [!definition] Definition §C5a.1.4: The Dirac Matrices
> The **Dirac matrices** are four complex $4\times4$ matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ acting on the component columns of Def. §C5a.1.1 and satisfying the **Dirac** (Clifford) **algebra**
>
> $$
> \{\gamma^\mu, \gamma^\nu\} \equiv \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\,\mathbb 1_4 , \qquad \gamma_\mu \equiv g_{\mu\nu}\gamma^\nu .
> $$
>
> $\mu$ is a spacetime index; the rows and columns are spinor indices. They are the matrices, in the chosen basis, of four linear maps $\Gamma^\mu$ on $V$ with $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}$, the **Clifford action** (a Clifford module of $(\mathbb R^{1,3}, g)$: [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-14|Def. §CB.11.14]]). The course's choice is the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-3-d|Def. §C5a.1.3]], with $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ of [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-2-d|Def. §C5a.1.2]]):
>
> $$
> \gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix} .
> $$
>
> Every other basis gives other matrices with the same algebra, and nothing physical depends on the choice ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-5-d|Theorem §C5a.1.5]]).
>
> *Source: PS §3.2, eqs. (3.22), (3.25), (3.42) · Yu §5.1, eq. (5.1); §5.2, eq. (5.75) · PHY 513 Lecture 7, Part B · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The Dirac (Clifford) algebra")*

^def-c5a-1-4-d

> [!theorem] Theorem §C5a.1.3: Computing with the Dirac Matrices
> For Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-4-d|Def. §C5a.1.4]]):
> 1. $(\gamma^0)^2 = \mathbb 1$, $(\gamma^i)^2 = -\mathbb 1$, and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \ne \nu$; each $\gamma^\mu$ is invertible, $(\gamma^\mu)^{-1} = \gamma_\mu$ (no sum).
> 2. For every four-vector $a$ with commuting components, $\slashed a\,\slashed a = a_\mu a^\mu\,\mathbb 1$, where $\slashed a \equiv a_\mu\gamma^\mu$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]); in particular $\slashed p\,\slashed p = p^2$.
> 3. $\gamma^\mu\gamma^\nu = g^{\mu\nu}\,\mathbb 1 + \frac12[\gamma^\mu, \gamma^\nu]$: contracted with a symmetric tensor only $g^{\mu\nu}\mathbb 1$ survives, contracted with an antisymmetric one only the commutator.
>
> *Proof:* [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]] (the same statement for Dirac matrices of any size).
>
> *Source: PS §3.2, p. 43 (the square of the Dirac operator) · Yu §5.1, eqs. (5.2)–(5.4) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?")*

^thm-c5a-1-3-d

> [!remark] Remark: A square root of p²
> The handwritten question "square to $\pm1$, or square root?" has a precise answer: for a momentum $p$, $p_\mu\gamma^\mu$ is a matrix square root of the number $p^2$ ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-3-d|Theorem §C5a.1.3]], 2). This is what Dirac was after: a first-order operator whose square is the Klein–Gordon operator, $(i\gamma^\mu\partial_\mu)^2 = -\partial^2$, so that a first-order equation implies $(\partial^2 + m^2)\psi = 0$ ([[§C13.2★ The Dirac Equation#^rem-c13-2-1|QM, Remark: The square root of the Klein–Gordon operator]]; [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]). No number squares to $p^2$ as a linear function of $p$; anticommuting matrices do, because the cross terms cancel in pairs. Run backwards, the requirement forces the algebra: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]] (the equivalence), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]] (no commuting coefficients), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]] (even size, at least four).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?")*

^rem-c5a-1-2-d

## Changing the basis, and why the choice does not matter

> [!theorem] Theorem §C5a.1.4: How Spinors and Spinor Matrices Change with the Basis
> Let $U$ be the change-of-basis matrix from an old to a new basis of $V$: column $b$ of $U$ lists the new components of the old basis vector $e_b$, $e_b = \sum_a U_{ab}e'_a$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]]). Then:
> 1. a spinor's column changes as $\psi' = U\psi$;
> 2. every $4\times4$ matrix acting on spinors changes as $M' = UMU^{-1}$; in particular $\gamma'^\mu = U\gamma^\mu U^{-1}$ are again Dirac matrices, and every expression built from the $\gamma$'s (sums, products, numbers, convergent power series such as $e^{-\frac i2\omega_{\mu\nu}S^{\mu\nu}}$) is given in the new basis by the same formula in the $\gamma'^\mu$;
> 3. one factor per spinor slot: a column (one $V$-slot) takes $U$ from the left, a row (one dual slot) takes $U^{-1}$ from the right, $\varphi' = \varphi U^{-1}$, a matrix takes both; a fully contracted expression ($\varphi\psi$, $\varphi M\psi$) is the same number in every basis;
> 4. $\operatorname{tr}M' = \operatorname{tr}M$, $\det M' = \det M$, and the eigenvalues of $M$ with their multiplicities do not depend on the basis.
>
> *Proof:* parts 1–2 [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]] and [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-15|Theorem §CB.11.15]]; part 3 [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]; part 4 [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]]. This is the change-of-basis formula of linear algebra ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (What each spinor index labels) · PHY 513, Problem Set 6, Problem 3(b) (statement: $\psi_D = U_D\psi$, $\gamma_D^\mu = U_D\gamma^\mu U_D^\dagger$) · Yu §5.2, eq. (5.72) · the slot formulation written here*

^thm-c5a-1-4-d

> [!caution] Caution: Which matrix is called U, and why a spinor takes one factor
> Here $U$ converts old components into new ones, $\psi' = U\psi$, $\gamma' = U\gamma U^{-1}$. Yu (5.72) writes $\gamma'^\mu = U^\dagger\gamma^\mu U$ with $U$ unitary, so Yu's $U$ is the inverse of this one; Larsen's $U_D$ (Problem Set 6, Problem 3(b)) converts chiral into Dirac components and follows this convention; the matrix of [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] runs the other way. Before using a formula, check which basis labels the rows of the source's $U$ (the full comparison, with Axler and Sakurai: [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^cau-cb-0-1|§CB.0, Caution: Which matrix is called U]]). A "sandwich" $U\psi U^{-1}$ is not defined ($\psi$ is a $4\times1$ column): only objects with two spinor slots ($\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$, $\psi\bar\chi$) take it. The sandwich $U(\Lambda)^{-1}\hat\psi\,U(\Lambda)$ of field theory uses the unitary operator on the Hilbert space and acts on the operator nature of $\hat\psi$, not on its spinor index ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 · PHY 513, Problem Set 6, Problem 3(b) · Yu eq. (5.72) · condensed from [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^rem-cb-0-1|§CB.0, Remark: Why "UψU⁻¹" means nothing]] and the caution linked above*

^cau-c5a-1-1-d

> [!theorem] Theorem §C5a.1.5: Any Two Sets of Dirac Matrices Are Related by a Change of Basis (Pauli)
> 1. If $\gamma^\mu$ and $\gamma'^\mu$ are two sets of $4\times4$ Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-4-d|Def. §C5a.1.4]]), there is an invertible $U$ with $\gamma'^\mu = U\gamma^\mu U^{-1}$ for all $\mu$, unique up to a nonzero factor. Conversely $U\gamma^\mu U^{-1}$ is a set of Dirac matrices for every invertible $U$.
> 2. If both sets satisfy $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ (Hermitian bases, [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]), $U$ can be chosen unitary.
> 3. Hence a choice of $\gamma$ matrices (chiral, Dirac, Majorana, …) is a choice of basis of the one spinor space $V$, unique up to an overall factor; a result written with $\gamma$'s and transformed by [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-4-d|Theorem §C5a.1.4]] holds in every basis, so anything proved in the chiral basis holds in all.
>
> *Proof:* [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|Theorem §CB.13.12]] (parts 1–2); part 3 is [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-13|Theorem §CB.13.13]] with [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-14|Theorem §CB.13.14]].
>
> *Source: PS §3.2, p. 41 ("all 4×4 representations of the Dirac algebra are unitarily equivalent", footnote to Problem 3.1) · Yu §5.2, eq. (5.72) (the converse direction) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)") · PHY 513 Lecture 7, Part B ("There are many realizations of $\gamma^\mu$")*

^thm-c5a-1-5-d

> [!theorem] Theorem §C5a.1.6: The Sixteen Products of γ Matrices
> For $A = \{\mu_1 < \dots < \mu_k\} \subseteq \{0, 1, 2, 3\}$ let $\Gamma_A = \gamma^{\mu_1}\cdots\gamma^{\mu_k}$, $\Gamma_\varnothing = \mathbb 1$: the sixteen matrices $\mathbb 1$, $\gamma^\mu$, $\gamma^\mu\gamma^\nu$ $(\mu < \nu)$, $\gamma^\mu\gamma^\nu\gamma^\rho$ $(\mu < \nu < \rho)$, $\gamma^0\gamma^1\gamma^2\gamma^3$ (up to sign the antisymmetrized products $\gamma^{[\mu_1\cdots\mu_k]}$ of [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-8|Def. §CB.12.8]]). For Dirac matrices of any size $n$:
> 1. $\Gamma_A\Gamma_B = \pm\Gamma_{A\triangle B}$ (symmetric difference), the sign fixed by the algebra alone; in particular $\Gamma_A^2 = \pm\mathbb 1$;
> 2. $\operatorname{tr}\Gamma_A = 0$ for $A \ne \varnothing$;
> 3. the sixteen $\Gamma_A$ are linearly independent, so $n \ge 4$;
> 4. for $n = 4$ they are a basis of all $4\times4$ complex matrices: $M = \sum_A c_A\Gamma_A$ with $c_A = \frac14\operatorname{tr}(\Gamma_A^{-1}M)$ (since $\operatorname{tr}(\Gamma_A^{-1}\Gamma_B) = 4\delta_{AB}$ by parts 1–2); only multiples of $\mathbb 1$ commute with all $\gamma^\mu$, and no subspace of $\mathbb C^4$ other than $0$ and $\mathbb C^4$ is mapped into itself by all $\gamma^\mu$.
>
> *Proof:* [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|Theorem §CB.12.9]]; the coefficient formula of part 4 follows from parts 1–2 as indicated.
>
> *Source: PS §3.4, p. 49 (the table "16 total") · Yu §5.1, eq. (5.45) and p. 163 (linear independence from the different transformation laws; $N \ge 4$, footnote 1) · PS §3.2, p. 41 ("these matrices must be at least 4 × 4")*

^thm-c5a-1-6-d

> [!theorem] Theorem §C5a.1.7: The Eigenvalues of γ⁰ and γⁱ
> In every basis, $\gamma^0$ is diagonalizable with eigenvalues $+1$ and $-1$, each twice, and each $\gamma^i$ ($i = 1, 2, 3$) is diagonalizable with eigenvalues $+i$ and $-i$, each twice.
>
> *Proof:* [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-10|Theorem §CB.12.10]] (for the maps $\Gamma^\mu$; the matrices have the same eigenvalues in every basis by [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-4-d|Theorem §C5a.1.4]], 4).
>
> *Source: Yu §5.1, eqs. (5.4)–(5.7) (squares $\pm\mathbb 1$; Hermitian $\gamma^0$, anti-Hermitian $\gamma^i$ for normal matrices) · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices")*

^thm-c5a-1-7-d

## The chiral basis

> [!definition] Definition §C5a.1.2: The Matrices σ^μ and σ̄^μ
> With $\mathbb 1$ the $2\times2$ identity and the Pauli matrices $\boldsymbol\sigma$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]]),
>
> $$
> \sigma^\mu = (\mathbb 1, \boldsymbol\sigma), \qquad \bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma), \qquad \sigma_\mu = g_{\mu\nu}\sigma^\nu = (\mathbb 1, -\boldsymbol\sigma) .
> $$
>
> For a four-vector $x$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]) write $X \equiv x_\mu\sigma^\mu = x^0\mathbb 1 - \mathbf x\cdot\boldsymbol\sigma$ and $\bar X \equiv x_\mu\bar\sigma^\mu = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$.
>
> *Source: PS §3.2, eq. (3.41) · Yu §5.2, eq. (5.74); Exercise 3.7, eq. (3.259) · PHY 513 Lecture 8, Part C ("Notation $\sigma^\mu = (1, \vec\sigma)$, $\bar\sigma^\mu = (1, -\vec\sigma)$") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit")*

^def-c5a-1-2-d

The bar on $\bar\sigma$ has nothing to do with the bar of the Dirac conjugate $\bar\psi$ (PS p. 44). Note that $\sigma_\mu$ and $\bar\sigma^\mu$ have the same entries: lowering the index of $\sigma$ and replacing $\sigma$ by $\bar\sigma$ both flip the sign of the spatial part.

> [!theorem] Theorem §C5a.1.1: Identities of σ^μ and σ̄^μ
> For $\sigma^\mu$, $\bar\sigma^\mu$, $X$, $\bar X$ of [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-2-d|Def. §C5a.1.2]]:
> 1. $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$.
> 2. $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1$ and $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu = 2g^{\mu\nu}\mathbb 1$; in particular $X\bar X = \bar XX = x^2\,\mathbb 1$.
> 3. $\sigma^2(\sigma^\mu)^*\sigma^2 = \bar\sigma^\mu$ and $\sigma^2(\bar\sigma^\mu)^*\sigma^2 = \sigma^\mu$.
>
> *Source: Yu Exercise 3.7, eq. (3.260) (the inverse $x^\mu = \frac12\operatorname{tr}(X\bar\sigma^\mu)$, which is part 1) · the user's PHY 513 notes, Ch. 8 §8.2 ("from $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$ the inverse is …") · PS eq. (3.38) (part 3 for $\boldsymbol\sigma$) · the case-by-case computation written out here*

^thm-c5a-1-1-d

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
> - Part 2 is a "Clifford algebra" for the pair $(\sigma, \bar\sigma)$: neither set alone squares to $g$, but $\sigma$ followed by $\bar\sigma$ does. Stacking them into a $4\times4$ matrix is exactly the chiral Dirac matrix → [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-3-d|Def. §C5a.1.3]].
> - $X\bar X = x^2$ makes $\det X = x^2$ plausible ($\det X\cdot\det\bar X = (x^2)^2$, and the two determinants are equal): the next theorems use it.
> - Part 3 is the matrix form of "complex conjugation exchanges the two Weyl representations" → Theorem §C5a.4.1, part 3.

^der-c5a-1-1-d

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-2-d|Def. §C5a.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!definition] Definition §C5a.1.3: The Chiral Basis
> The **chiral** (**Weyl**) **basis** is, in $2\times2$ blocks, with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-2-d|Def. §C5a.1.2]],
>
> $$
> \gamma^0 = \begin{pmatrix} 0 & \mathbb 1 \\ \mathbb 1 & 0 \end{pmatrix}, \qquad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}, \qquad\text{i.e.}\qquad \gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix} .
> $$
>
> A Dirac spinor in this basis is written $\psi = \binom{\psi_L}{\psi_R}$, with two-component upper and lower halves (their Lorentz transformation, as left- and right-handed Weyl spinors, is derived in §C5a.3–§C5a.4: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-2|Def. §C5a.4.2]]).
>
> *Source: PS §3.2, eqs. (3.25), (3.36), (3.42) · PHY 513 Lecture 7, Part B (slide "Explicit Form of Dirac Matrices"); Lecture 8, Cheat Sheet I and Part C ("Economical form of all 4 $\gamma$-matrices") · the user's PHY 513 notes, Ch. 8 §8.1, eq. (chiralbasis), §8.2, eq. (weylsplit) · Yu §5.2, eqs. (5.68), (5.75)*

^def-c5a-1-3-d

> [!theorem] Theorem §C5a.1.2: The Chiral Matrices Satisfy the Clifford Algebra
> The matrices of [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-3-d|Def. §C5a.1.3]] satisfy $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_4$, and $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis") · PHY 513 Lecture 7, Part B (sample check $\{\gamma^0, \gamma^i\} = 0$) · Yu §5.2, eqs. (5.69)–(5.71) · PHY 513, Problem Set 6, Problem 3(a) (the block-by-block check of step 3, as the user wrote it)*

^thm-c5a-1-2-d

> [!derivation]- Derivation
> **1. The block product.** $\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}\begin{pmatrix}0&\sigma^\nu\\\bar\sigma^\nu&0\end{pmatrix} = \begin{pmatrix}0\cdot0 + \sigma^\mu\bar\sigma^\nu & 0\cdot\sigma^\nu + \sigma^\mu\cdot0\\ \bar\sigma^\mu\cdot0 + 0\cdot\bar\sigma^\nu & \bar\sigma^\mu\sigma^\nu + 0\cdot0\end{pmatrix} = \begin{pmatrix}\sigma^\mu\bar\sigma^\nu & 0\\ 0 & \bar\sigma^\mu\sigma^\nu\end{pmatrix}$.
>
> **2. The anticommutator.** Adding the same with $\mu \leftrightarrow \nu$: $\{\gamma^\mu, \gamma^\nu\} = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu,\ \bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu) = \operatorname{diag}(2g^{\mu\nu}\mathbb 1, 2g^{\mu\nu}\mathbb 1)$ by [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-1-d|Theorem §C5a.1.1]], 2.
>
> **3. Explicitly (the lecture's check).** $(\gamma^0)^2 = \operatorname{diag}(\mathbb 1, \mathbb 1)$; $\gamma^0\gamma^i = \operatorname{diag}(-\sigma^i, \sigma^i)$ and $\gamma^i\gamma^0 = \operatorname{diag}(\sigma^i, -\sigma^i)$, so $\{\gamma^0, \gamma^i\} = 0$; $\gamma^i\gamma^j = \operatorname{diag}(-\sigma^i\sigma^j, -\sigma^i\sigma^j)$, so $\{\gamma^i, \gamma^j\} = -\operatorname{diag}(\{\sigma^i, \sigma^j\}, \{\sigma^i, \sigma^j\}) = -2\delta^{ij}\mathbb 1_4 = 2g^{ij}\mathbb 1_4$. All ten conditions hold.
>
> **What the derivation shows**
> - The Clifford algebra of $\gamma$ is the pair identity of $\sigma$, $\bar\sigma$ stacked off-diagonally; every product of two $\gamma$'s is block diagonal, every product of an odd number off-diagonal. That is why the generators (products of two) will not mix the halves (Theorem §C5a.3.1).

^der-c5a-1-2-d

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-3-d|Def. §C5a.1.3]], [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^thm-c5a-1-1-d|Theorem §C5a.1.1]]

> [!remark]- Connections
> - The index rule for spinors is the same slot rule as for spacetime tensors, with $U$ in place of $\Lambda$ and no metric to raise or lower; spinor indices are matrix indices of the third kind in the index-slot classification — [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
> - $\sigma^\mu$ and $\bar\sigma^\mu$ are to Weyl spinors what $\gamma^\mu$ is to Dirac spinors, and $\gamma^\mu$ is literally built from them in the chiral basis — [[§C5a.1 Spinor Space and the Clifford Action (physics-form draft)#^def-c5a-1-3-d|Def. §C5a.1.3]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]].
> - The sixteen products are the matrices of the fermion bilinears (scalar, pseudoscalar, vector, axial vector, tensor) and of every trace identity used in scattering amplitudes — [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-8|Theorem §C5a.14.8]].
> - Component by component, the quantum field is four operators $\hat\psi_a$ with c-number coefficients $u^s_a(p)$; a change of basis acts on the index $a$ of both, never on the mode operators — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-3|§C5b.2, Remark: A spinor-valued operator, component by component]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]].
> - The layers of spinor space mirror those of Minkowski space: a vector space, then an algebraic structure (the Clifford product here, the metric there), then a group that preserves it; for spinors the Clifford action comes before any group, and the Lorentz algebra is built from it — [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
> - Yu's Table 5.1 (p. 165) puts the four spaces of the subject side by side: vector-representation space, spinor space (this section), the Hilbert space of states and the space of fields, each with its own generators of the Lorentz group — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]].

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1|Def. §CB.0.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2|Def. §CB.0.2]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3|Theorem §CB.0.3]] — components and matrices in a basis; operator identities hold verbatim among matrices.
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4|Def. §CB.0.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]] — the change-of-basis matrix; ψ′ = Uψ, M′ = UMU⁻¹ (Theorem §C5a.1.4, 1–2).
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^rem-cb-0-1|§CB.0, Remark: Why "UψU⁻¹" means nothing]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^cau-cb-0-1|§CB.0, Caution: Which matrix is called U]] — the full comparison of conventions condensed in the caution above.
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6|Def. §CB.0.6]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8|Def. §CB.0.8]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]] — dual spinors and spinor tensors; one factor per slot, contractions are basis free (Theorem §C5a.1.4, 3).
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]] — trace, determinant and eigenvalues are basis free (Theorem §C5a.1.4, 4).
> - [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-14|Def. §CB.11.14]] — Dirac matrices of any size and the Dirac maps on V (Def. §C5a.1.4).
> - [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]] — squares, anticommutation, the square root of a² (Theorem §C5a.1.3).
> - [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-15|Theorem §CB.11.15]] — the matrices of the Dirac maps in any basis are Dirac matrices, and formulas in them transform by conjugation (Theorem §C5a.1.4, 2).
> - [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-8|Def. §CB.12.8]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|Theorem §CB.12.9]] — antisymmetrized products; the sixteen products are a basis, traceless, and force size ≥ 4 (Theorem §C5a.1.6).
> - [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-10|Theorem §CB.12.10]] — eigenvalues ±1 of Γ⁰ and ±i of Γⁱ (Theorem §C5a.1.7).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-7|Def. §CB.13.7]] — intertwiners and equivalence of two sets of Dirac matrices (the U of Theorem §C5a.1.5).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|Theorem §CB.13.12]] — Pauli's fundamental theorem (Theorem §C5a.1.5, 1–2).
> - [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-13|Theorem §CB.13.13]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-14|Theorem §CB.13.14]] — changes of basis are exactly the invertible intertwiners; spinor space is unique (Theorem §C5a.1.5, 3).
