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

What is a Dirac spinor before anyone writes a column of four numbers, and what do the $\gamma$ matrices add to it? A spinor is first of all a vector of a four-dimensional complex vector space $V$; everything else is structure added on top, one layer at a time (the map is [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]]). This section builds the first two layers. **Layer 1** is $V$ itself with its bases: components, matrices of linear maps, and the change-of-basis rules, which are the change-of-basis formula of linear algebra and nothing more ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR Thm. 3.84]]), with the slot rule that decides which factor each index receives. **Layer 2** is the Clifford action: four linear maps $\Gamma^\mu$ on $V$ with $\Gamma^\mu\Gamma^\nu + \Gamma^\nu\Gamma^\mu = 2g^{\mu\nu}$, whose matrices in a basis are the Dirac matrices; their first consequences, the sixteen products, the eigenvalues, the chiral basis as one choice, and Pauli's theorem, which says that spinor space with its Clifford action is unique and that a choice of $\gamma$ matrices is a choice of basis. Both layers are mathematics: linear algebra in components ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]]) and the theory of Clifford modules ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules|§CB.10]]–[[§CB.12 Complex Clifford Algebras and Clifford Modules|§CB.12]]), shown in the blocks below; this section keeps spinor space as the carrier of the Dirac field, the matrices $\sigma^\mu$, $\bar\sigma^\mu$ and the chiral basis, and Hermiticity is [[§C5a.2 The Dirac Form|§C5a.2]]. The Dirac matrices of Quantum Mechanics enter here as one such choice ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]). The Dirac form, the Lorentz action and chirality are the next layers ([[§C5a.2 The Dirac Form|§C5a.2]]–[[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]).

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis when a basis is fixed; spinor indices are Latin $a, b, c, d \in \{1, 2, 3, 4\}$, never raised or lowered, all written as subscripts, contracted by plain sums; spacetime indices Greek ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]]). Operators on $V$ are written $\Gamma^\mu$, $M$, …, their matrices $\gamma^\mu$, …; $\operatorname{End}(V)$ is the space of linear maps $V \to V$ (Axler's $\mathcal L(V)$). The identity matrix in $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ is usually not written. Pauli matrices $\boldsymbol\sigma = (\sigma^1, \sigma^2, \sigma^3)$, with the product rule of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]. $\psi$ is a c-number spinor or a classical field (no hat); the quantum field is $\hat\psi$.

*Why spinor space and the $\gamma$'s are needed at all, what the Clifford relation induces, the four jobs of the $\gamma$'s, and the layer-by-layer map of the chapter: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]].*

## The mathematics used here

Layer 1 is linear algebra on a four-dimensional $V$: components and matrices in a basis, and how they change with the basis, stated in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]] for any finite-dimensional $V$:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-1]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-2]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-3]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-3]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-4]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-5]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^rem-cb-0-1]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^cau-cb-0-1]]

The slots of spinor tensors — covectors, operators and the index rule — and the invariance of trace, determinant and eigenvalues:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-6]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-10]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-15]]

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

^rem-c5a-1-1

### The mathematics used here: the Clifford action

Layer 2 is the Clifford action: the Dirac matrices, their first consequences (Remark: A square root of p² below reads part 2), the Dirac maps on $V$ and their matrices in any basis:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-14]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-15]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-15]]

The sixteen products are a basis of $M_4(\mathbb C)$, and the eigenvalues of the Dirac maps follow from the trace:

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-8]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-9]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-9]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-10]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-10]]

## The Clifford algebra

> [!remark] Remark: A square root of p²
> The handwritten question "square to $\pm1$, or square root?" has a precise answer: for a momentum $p$, $p_\mu\gamma^\mu$ is a matrix square root of the number $p^2$ (Theorem §CB.10.12, 2). This is what Dirac was after: a first-order operator whose square is the Klein–Gordon operator, $(i\gamma^\mu\partial_\mu)^2 = -\partial^2$, so that a first-order equation implies $(\partial^2 + m^2)\psi = 0$ ([[§C13.2★ The Dirac Equation#^rem-c13-2-1|QM, Remark: The square root of the Klein–Gordon operator]]; [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]). No number squares to $p^2$ as a linear function of $p$; anticommuting matrices do, because the cross terms cancel in pairs. Run backwards, the requirement forces the algebra: [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]] (the equivalence), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-2|Theorem §C5a.0.2]] (no commuting coefficients), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]] (even size, at least four).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?")*

^rem-c5a-1-2

### The mathematics used here: Pauli's theorem

The chiral basis below is one choice among all bases, because spinor space with its Clifford action is unique and a choice of $\gamma$ matrices is a choice of basis:

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-7]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-13]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-13]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-14]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-14]]

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

^def-c5a-1-2

The bar on $\bar\sigma$ has nothing to do with the bar of the Dirac conjugate $\bar\psi$ (PS p. 44). Note that $\sigma_\mu$ and $\bar\sigma^\mu$ have the same entries: lowering the index of $\sigma$ and replacing $\sigma$ by $\bar\sigma$ both flip the sign of the spatial part.

> [!theorem] Theorem §C5a.1.1: Identities of σ^μ and σ̄^μ
> For $\sigma^\mu$, $\bar\sigma^\mu$, $X$, $\bar X$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]:
> 1. $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$.
> 2. $\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu = 2g^{\mu\nu}\mathbb 1$ and $\bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu = 2g^{\mu\nu}\mathbb 1$; in particular $X\bar X = \bar XX = x^2\,\mathbb 1$.
> 3. $\sigma^2(\sigma^\mu)^*\sigma^2 = \bar\sigma^\mu$ and $\sigma^2(\bar\sigma^\mu)^*\sigma^2 = \sigma^\mu$.
>
> *Source: Yu Exercise 3.7, eq. (3.260) (the inverse $x^\mu = \frac12\operatorname{tr}(X\bar\sigma^\mu)$, which is part 1) · the user's PHY 513 notes, Ch. 8 §8.2 ("from $\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2g^{\mu\nu}$ the inverse is …") · PS eq. (3.38) (part 3 for $\boldsymbol\sigma$) · the case-by-case computation written out here*

^thm-c5a-1-1

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
> - Part 2 is a "Clifford algebra" for the pair $(\sigma, \bar\sigma)$: neither set alone squares to $g$, but $\sigma$ followed by $\bar\sigma$ does. Stacking them into a $4\times4$ matrix is exactly the chiral Dirac matrix → [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]].
> - $X\bar X = x^2$ makes $\det X = x^2$ plausible ($\det X\cdot\det\bar X = (x^2)^2$, and the two determinants are equal): the next theorems use it.
> - Part 3 is the matrix form of "complex conjugation exchanges the two Weyl representations" → Theorem §C5a.4.1, part 3.

^der-c5a-1-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!definition] Definition §C5a.1.3: The Chiral Basis
> The **chiral** (**Weyl**) **basis** is, in $2\times2$ blocks, with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]],
>
> $$
> \gamma^0 = \begin{pmatrix} 0 & \mathbb 1 \\ \mathbb 1 & 0 \end{pmatrix}, \qquad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}, \qquad\text{i.e.}\qquad \gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix} .
> $$
>
> A Dirac spinor in this basis is written $\psi = \binom{\psi_L}{\psi_R}$, with two-component upper and lower halves (their Lorentz transformation, as left- and right-handed Weyl spinors, is derived in §C5a.3–§C5a.4: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-2|Def. §C5a.4.2]]).
>
> *Source: PS §3.2, eqs. (3.25), (3.36), (3.42) · PHY 513 Lecture 7, Part B (slide "Explicit Form of Dirac Matrices"); Lecture 8, Cheat Sheet I and Part C ("Economical form of all 4 $\gamma$-matrices") · the user's PHY 513 notes, Ch. 8 §8.1, eq. (chiralbasis), §8.2, eq. (weylsplit) · Yu §5.2, eqs. (5.68), (5.75)*

^def-c5a-1-3

> [!theorem] Theorem §C5a.1.2: The Chiral Matrices Satisfy the Clifford Algebra
> The matrices of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]] satisfy $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_4$, and $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis") · PHY 513 Lecture 7, Part B (sample check $\{\gamma^0, \gamma^i\} = 0$) · Yu §5.2, eqs. (5.69)–(5.71) · PHY 513, Problem Set 6, Problem 3(a) (the block-by-block check of step 3, as the user wrote it)*

^thm-c5a-1-2

> [!derivation]- Derivation
> **1. The block product.** $\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}\begin{pmatrix}0&\sigma^\nu\\\bar\sigma^\nu&0\end{pmatrix} = \begin{pmatrix}0\cdot0 + \sigma^\mu\bar\sigma^\nu & 0\cdot\sigma^\nu + \sigma^\mu\cdot0\\ \bar\sigma^\mu\cdot0 + 0\cdot\bar\sigma^\nu & \bar\sigma^\mu\sigma^\nu + 0\cdot0\end{pmatrix} = \begin{pmatrix}\sigma^\mu\bar\sigma^\nu & 0\\ 0 & \bar\sigma^\mu\sigma^\nu\end{pmatrix}$.
>
> **2. The anticommutator.** Adding the same with $\mu \leftrightarrow \nu$: $\{\gamma^\mu, \gamma^\nu\} = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu,\ \bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu) = \operatorname{diag}(2g^{\mu\nu}\mathbb 1, 2g^{\mu\nu}\mathbb 1)$ by [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], 2.
>
> **3. Explicitly (the lecture's check).** $(\gamma^0)^2 = \operatorname{diag}(\mathbb 1, \mathbb 1)$; $\gamma^0\gamma^i = \operatorname{diag}(-\sigma^i, \sigma^i)$ and $\gamma^i\gamma^0 = \operatorname{diag}(\sigma^i, -\sigma^i)$, so $\{\gamma^0, \gamma^i\} = 0$; $\gamma^i\gamma^j = \operatorname{diag}(-\sigma^i\sigma^j, -\sigma^i\sigma^j)$, so $\{\gamma^i, \gamma^j\} = -\operatorname{diag}(\{\sigma^i, \sigma^j\}, \{\sigma^i, \sigma^j\}) = -2\delta^{ij}\mathbb 1_4 = 2g^{ij}\mathbb 1_4$. All ten conditions hold.
>
> **What the derivation shows**
> - The Clifford algebra of $\gamma$ is the pair identity of $\sigma$, $\bar\sigma$ stacked off-diagonally; every product of two $\gamma$'s is block diagonal, every product of an odd number off-diagonal. That is why the generators (products of two) will not mix the halves (Theorem §C5a.3.1).

^der-c5a-1-2

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]

> [!remark]- Connections
> - The index rule for spinors is the same slot rule as for spacetime tensors, with $U$ in place of $\Lambda$ and no metric to raise or lower; spinor indices are matrix indices of the third kind in the index-slot classification — [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
> - $\sigma^\mu$ and $\bar\sigma^\mu$ are to Weyl spinors what $\gamma^\mu$ is to Dirac spinors, and $\gamma^\mu$ is literally built from them in the chiral basis — [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]].
> - The sixteen products are the matrices of the fermion bilinears (scalar, pseudoscalar, vector, axial vector, tensor) and of every trace identity used in scattering amplitudes — [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]].
> - Component by component, the quantum field is four operators $\hat\psi_a$ with c-number coefficients $u^s_a(p)$; a change of basis acts on the index $a$ of both, never on the mode operators — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-3|§C5b.2, Remark: A spinor-valued operator, component by component]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]].
> - The layers of spinor space mirror those of Minkowski space: a vector space, then an algebraic structure (the Clifford product here, the metric there), then a group that preserves it; for spinors the Clifford action comes before any group, and the Lorentz algebra is built from it — [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]].
