---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.4 SL(2,C) and the Group Action on Spinor Space]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.6 The Dirac Conjugate and the Bilinears]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors"; Caution "'ξ is the particle, η the antiparticle'"), §8.3 (What each spinor index labels), Ch. 9 §9.6 (Supplement, Definition "The matrix $\gamma^5$", Principle "Properties of $\gamma^5$") · PHY 513 Lecture 7, Part B; Lecture 8, Part A (slide "Transformations with 4-Vectors and 4-Spinors") and Part C · PHY 513, Problem Set 5, Problem 5(a)–(b) (as the user wrote it; submitted) · Peskin & Schroeder, §3.2, pp. 41, 44, §3.4, pp. 49–51, eqs. (3.68)–(3.76) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.32)–(5.40), §5.2, eq. (5.73), Exercise 3.7 · the user's pre-course notes, §5.2 · Sakurai & Napolitano, Modern Quantum Mechanics, §8.2 (the Dirac basis, as recorded in Quantum Mechanics C13★) · Schwartz, Quantum Field Theory and the Standard Model, §10.3, p. 170, eq. (10.74), and §11.3, p. 192 (the Majorana basis; ★ only) · PHY 513, Problem Set 6, Problem 3(b) and comments (Larsen; the user's solution).*

How does spinor space split into a left- and a right-handed half without reference to a basis, and how are the indices of the halves handled? Layers 1–5 ([[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]) gave $V$, the Clifford action, the Dirac form and the Lorentz action, under which the chiral basis shows two invariant halves. This section adds **layer 6**, a grading: the matrix $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is Lorentz invariant, and its eigenspaces $V_L$ ($\gamma^5 = -1$) and $V_R$ ($\gamma^5 = +1$) are the Weyl halves in every basis, with projectors $P_L$, $P_R$. It then gives the index calculus of Weyl spinors (undotted and dotted indices, the invariant $\varepsilon$, the four-vector as a bispinor), what each Dirac index labels, and closes the basis question opened in §C5a.1: which bases are used and why (chiral, Dirac, ★ Majorana).

*Conventions* as in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] and [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]). The "5" of $\gamma^5$ is a label, not a Lorentz index.

## γ⁵ and the Weyl halves

> [!definition] Definition §C5a.5.1: The Matrix γ⁵
>
> $$
> \gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3 ,
> $$
>
> with $\gamma^\mu$ the Dirac matrices of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]. The "5" is a label, not a Lorentz index: there is no $\gamma_5$ obtained by lowering.
>
> *Source: PS §3.4, eq. (3.68) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$", eq. (gamma5)) · PHY 513, Problem Set 5, Problem 5 (statement: "there is no way to lower a '5' index") · Yu §5.1, eq. (5.32)*

^def-c5a-5-1

Yu writes $\gamma_5 \equiv \gamma^5$ for the same matrix. Its totally antisymmetric form $\gamma^5 = -\frac i{4!}\varepsilon_{\mu\nu\rho\sigma}\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma$ (with $\varepsilon^{0123} = +1$) and the duality identities are [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]]–[[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|§C5a.11.7]].

> [!theorem] Theorem §C5a.5.1: Algebraic Properties of γ⁵
>
> $$
> (\gamma^5)^2 = \mathbb 1, \qquad \gamma^{5\dagger} = \gamma^5, \qquad \{\gamma^5, \gamma^\mu\} = 0, \qquad \operatorname{tr}\gamma^5 = 0 ,
> $$
>
> for $\gamma^5$ of [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]] (Hermiticity in a basis with $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]).
>
> *Source: PHY 513, Problem Set 5, Problem 5(a)–(b) (as the user wrote it) · PS §3.4, eqs. (3.69)–(3.71) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$" and its proof) · Yu §5.1, eqs. (5.37)–(5.40)*

^thm-c5a-5-1

> [!derivation]- Derivation
> **1. Anticommutation.** Move $\gamma^\mu$ from the right of $\gamma^0\gamma^1\gamma^2\gamma^3$ to the left, one factor at a time. It passes three factors with index $\ne \mu$, each giving $-1$ (Theorem §C5a.1.5), and the one equal to $\mu$, with which it commutes: $\gamma^5\gamma^\mu = (-1)^3\gamma^\mu\gamma^5$. (The user's Problem Set 5 solution does the same move with $\gamma^a\gamma^\mu = 2g^{a\mu} - \gamma^\mu\gamma^a$ at each step and shows that the four surviving metric terms add up to $-2\gamma^\mu\gamma^5$.)
>
> **2. Hermiticity.** $(ABCD)^\dagger = D^\dagger C^\dagger B^\dagger A^\dagger$ and $\gamma^{0\dagger} = \gamma^0$, $\gamma^{i\dagger} = -\gamma^i$ (Theorem §C5a.1.11): $\gamma^{5\dagger} = -i\gamma^{3\dagger}\gamma^{2\dagger}\gamma^{1\dagger}\gamma^{0\dagger} = -i(-1)^3\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^3\gamma^2\gamma^1\gamma^0$. Reversing four distinct anticommuting factors takes $3 + 2 + 1 = 6$ swaps (three to bring $\gamma^0$ to the front, two for $\gamma^1$, one for $\gamma^2$), so $\gamma^3\gamma^2\gamma^1\gamma^0 = (-1)^6\gamma^0\gamma^1\gamma^2\gamma^3$ and $\gamma^{5\dagger} = \gamma^5$.
>
> **3. Square.** Using the reversed form of step 2 for the second factor, $(\gamma^5)^2 = \gamma^5\gamma^{5\dagger} = i\cdot i\,\gamma^0\gamma^1\gamma^2\gamma^3\gamma^3\gamma^2\gamma^1\gamma^0$. The middle pairs collapse one after another: $(\gamma^3)^2 = -\mathbb 1$, $(\gamma^2)^2 = -\mathbb 1$, $(\gamma^1)^2 = -\mathbb 1$, $(\gamma^0)^2 = \mathbb 1$, giving $i^2(-1)^3 = 1$.
>
> **4. Trace.** $\gamma^5$ is $i$ times the product $\Gamma_{\{0,1,2,3\}}$, traceless by [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], 2.
>
> **What the derivation shows**
> - $\gamma^5$ is a Hermitian involution, so its eigenvalues are $\pm1$; tracelessness makes each occur twice in four dimensions.
> - The factor $i$ in the definition is chosen to make $\gamma^5$ Hermitian with square $+1$.
> - Used next: Theorem §C5a.5.2; the chirality projectors $\frac12(\mathbb 1 \mp \gamma^5)$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]]); traces with $\gamma^5$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-4|Theorem §C5a.11.4]]).

^der-c5a-5-1

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]

Theorem §C5a.5.2 reads its two eigenspaces as irreducible labels and uses that parity exchanges them:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-3]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-9]]

> [!theorem] Theorem §C5a.5.2: γ⁵ Is Lorentz Invariant and Separates the Weyl Halves
> 1. $[\gamma^5, S^{\mu\nu}] = 0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), hence $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$: $\gamma^5$ is a Lorentz scalar.
> 2. In the chiral basis $\gamma^5 = \begin{pmatrix}-\mathbb 1 & 0\\ 0 & \mathbb 1\end{pmatrix}$.
> 3. On the Dirac representation $\gamma^5 = \frac43\bigl(\mathbf J_-^2 - \mathbf J_+^2\bigr)$, with the Casimirs $\mathbf J_\pm^2$ of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3|Theorem §CB.16.3]], equivalently $\mathbf J\cdot\mathbf K = \frac{3i}4\gamma^5$.
> 4. In every basis, the eigenspaces $\gamma^5 = -1$ and $\gamma^5 = +1$ are two-dimensional, invariant under $\Lambda_{1/2}$, and carry $(\frac12, 0)$ and $(0, \frac12)$ (Theorem §C5a.3.4): left-handed spinors ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]) are the $\gamma^5 = -1$ spinors.
>
> *Source: PS §3.4, p. 50 ("$[\gamma^5, S^{\mu\nu}] = 0$. Thus the Dirac representation must be reducible …"; eq. (3.72)) · Yu §5.1, eq. (5.36) ($\gamma^5$ a Lorentz scalar), §5.2, eq. (5.73) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$": "$\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$") · the user's pre-course notes, §5.2 · part 3 written out here*

^thm-c5a-5-2

> [!derivation]- Derivation
> **1. γ⁵ commutes with products of two γ's.** $\gamma^5\gamma^\mu\gamma^\nu = -\gamma^\mu\gamma^5\gamma^\nu = \gamma^\mu\gamma^\nu\gamma^5$ (Theorem §C5a.5.1, twice). Hence $\gamma^5$ commutes with $[\gamma^\mu, \gamma^\nu]$ and with $S^{\mu\nu}$, with every power of $A = -\frac i2\omega_{\mu\nu}S^{\mu\nu}$, and with $\Lambda_{1/2} = e^A$: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$.
>
> **2. Chiral form.** From Derivation §C5a.1.10, $\gamma^0\gamma^1 = \operatorname{diag}(-\sigma^1, \sigma^1)$, and $\gamma^2\gamma^3 = \operatorname{diag}(-\sigma^2\sigma^3, -\sigma^2\sigma^3) = \operatorname{diag}(-i\sigma^1, -i\sigma^1)$ ($\sigma^2\sigma^3 = i\sigma^1$, [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). The product is $\operatorname{diag}(-\sigma^1(-i\sigma^1), \sigma^1(-i\sigma^1)) = \operatorname{diag}(i\mathbb 1, -i\mathbb 1)$, and times $i$: $\operatorname{diag}(-\mathbb 1, \mathbb 1)$ (Yu (5.73)).
>
> **3. J·K.** With Theorem §C5a.3.3, $J_kK_k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)\cdot(-\frac i2)\operatorname{diag}(\sigma^k, -\sigma^k) = -\frac i4\operatorname{diag}(\mathbb 1, -\mathbb 1)$ for each $k$ ($(\sigma^k)^2 = \mathbb 1$); summing over $k = 1, 2, 3$: $\mathbf J\cdot\mathbf K = -\frac{3i}4\operatorname{diag}(\mathbb 1, -\mathbb 1) = \frac{3i}4\gamma^5$. Here $J_k$ and $K_k$ commute (both block diagonal with commuting blocks), so $\mathbf J_\pm^2 = \frac14(\mathbf J^2 - \mathbf K^2 \pm 2i\mathbf J\cdot\mathbf K)$ and $\mathbf J_+^2 - \mathbf J_-^2 = i\mathbf J\cdot\mathbf K = -\frac34\gamma^5$. Both sides of part 3 are built from $\gamma$'s by the same formula in every basis, so a change of basis $\gamma \to U\gamma U^{-1}$ (Theorem §C5a.1.12) conjugates both, and the identity holds in every basis. ⚑ By-product: $\gamma^5$ is a function of the two Casimirs of the Lorentz algebra; that alone explains part 1.
>
> **4. Eigenspaces.** In the chiral basis the $\gamma^5 = -1$ eigenspace is the upper half, $(\frac12, 0)$, and $\gamma^5 = +1$ the lower, $(0, \frac12)$ (part 2, Theorem §C5a.3.4). In another basis, $\gamma'^\mu = U\gamma^\mu U^{-1}$ gives $\gamma'^5 = U\gamma^5U^{-1}$, $S' = USU^{-1}$, and the eigenspaces are the images under $U$, with the same generators. They are invariant under $\Lambda_{1/2}$ by part 1: an operator commuting with a representation has invariant eigenspaces (Schur's criterion, PS p. 50).
>
> **What the derivation shows**
> - The split $(\frac12, 0)\oplus(0, \frac12)$ is not an artefact of the chiral basis: it is the eigen-decomposition of the Lorentz-invariant matrix $\gamma^5$, which the chiral basis merely diagonalizes (PS footnote ‡: in another basis "the reducibility would not be manifest").
> - $\gamma^5$ commutes with $S^{\mu\nu}$ but anticommutes with $\gamma^\mu$: the Lorentz transformations preserve handedness, the vector index of $\gamma^\mu$ flips it. Under parity, which exchanges the copies ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]), $\gamma^5$ changes sign (pseudoscalar; [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]).
> - Used next: chirality projectors and Weyl fields ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]).

^der-c5a-5-2

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## Chirality projectors

> [!definition] Definition §C5a.5.2: Chirality Projectors
> $$
> P_L \equiv \tfrac12\bigl(\mathbb 1 - \gamma^5\bigr), \qquad P_R \equiv \tfrac12\bigl(\mathbb 1 + \gamma^5\bigr) .
> $$
>
> With $\gamma^5$ of [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]: a Dirac spinor with $\gamma^5\psi = -\psi$ ($P_L\psi = \psi$) has **left-handed chirality**, one with $\gamma^5\psi = +\psi$ right-handed. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), where $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]), $P_L\psi = (\psi_L, 0)$ and $P_R\psi = (0, \psi_R)$ for $\psi = (\psi_L, \psi_R)$, the Weyl halves of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]].
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PS §3.4, eqs. (3.72), (3.76) · Yu §5.1 ($\gamma^5$), §5.3, eq. (5.112)*

^def-c5a-5-2

The same letters denote the two-component Weyl spinors $\psi_L$, $\psi_R$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]]) and, by abuse, the four-component $P_L\psi$, $P_R\psi$; context decides. Chirality is the eigenvalue of $\gamma^5$, a property of the representation; helicity is the spin along the momentum, a property of a state. They agree only for massless positive-frequency solutions (Theorem §C5a.7.12; [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]]).

> [!theorem] Theorem §C5a.5.3: Properties of the Chirality Projectors
> 1. $P_L^2 = P_L$, $P_R^2 = P_R$, $P_LP_R = P_RP_L = 0$, $P_L + P_R = \mathbb 1$.
> 2. $P_L\gamma^\mu = \gamma^\mu P_R$ and $P_R\gamma^\mu = \gamma^\mu P_L$.
> 3. $[P_{L,R}, S^{\mu\nu}] = 0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), so $P_{L,R}\Lambda_{1/2} = \Lambda_{1/2}P_{L,R}$: chirality is Lorentz invariant, and $P_L\psi$, $P_R\psi$ transform separately.
> 4. $\overline{P_L\psi} = \bar\psi P_R$ and $\overline{P_R\psi} = \bar\psi P_L$.
>
> *Source: PS §3.4, pp. 50–51 (eqs. (3.71)–(3.72), (3.76) and the paragraph on reducibility) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$")*

^thm-c5a-5-3

> [!derivation]- Derivation
> Use $(\gamma^5)^2 = \mathbb 1$, $\gamma^{5\dagger} = \gamma^5$, $\{\gamma^5, \gamma^\mu\} = 0$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]) and $[\gamma^5, S^{\mu\nu}] = 0$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]).
>
> **1. Projectors.** $P_L^2 = \frac14(\mathbb 1 - 2\gamma^5 + (\gamma^5)^2) = \frac14(2\cdot\mathbb 1 - 2\gamma^5) = P_L$; likewise $P_R^2 = P_R$. $P_LP_R = \frac14(\mathbb 1 + \gamma^5 - \gamma^5 - (\gamma^5)^2) = 0$, and $P_RP_L = 0$ the same way. $P_L + P_R = \mathbb 1$ by adding the definitions.
>
> **2. Passing a $\gamma$.** $P_L\gamma^\mu = \frac12(\gamma^\mu - \gamma^5\gamma^\mu) = \frac12(\gamma^\mu + \gamma^\mu\gamma^5) = \gamma^\mu P_R$; with $\gamma^5 \to -\gamma^5$ the other.
>
> **3. Lorentz invariance.** $P_{L,R}$ are polynomials in $\gamma^5$, which commutes with $S^{\mu\nu}$, hence with every power of $\omega_{\mu\nu}S^{\mu\nu}$ and with the exponential series $\Lambda_{1/2}$. So $P_L\psi' = \Lambda_{1/2}(P_L\psi)(\Lambda^{-1}x)$.
>
> **4. Conjugates.** $\overline{P_L\psi} = (P_L\psi)^\dagger\gamma^0 = \psi^\dagger P_L^\dagger\gamma^0 = \psi^\dagger P_L\gamma^0$ ($P_L$ Hermitian since $\gamma^5$ is) $= \psi^\dagger\gamma^0P_R$ (step 2 with $\mu = 0$) $= \bar\psi P_R$.
>
> **What the derivation shows**
> - Step 2 is why every $\gamma$ flips chirality, and why the kinetic term, with one $\gamma$ between $\bar\psi$ and $\psi$, does not mix chiralities while the mass term, with none, does (Theorem §C5a.7.9).
> - ⚑ By-product: the projector on a "left-handed" field appears as $P_R$ next to $\bar\psi$ (step 4): $\overline{\psi_L}\psi_L = \bar\psi P_RP_L\psi = 0$.

^der-c5a-5-3

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]]

## Spinor indices

> [!definition] Definition §C5a.5.3: Undotted and Dotted Spinor Indices
> - A left-handed spinor carries a lower **undotted** index, $\psi_a$ ($a = 1, 2$), with $\psi_a \to (\Lambda_L)_a{}^b\psi_b$ ($\Lambda_L$, $\Lambda_R$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]); a right-handed one an upper **dotted** index, $\psi^{\dot a}$, with $\psi^{\dot a} \to (\Lambda_R)^{\dot a}{}_{\dot b}\psi^{\dot b}$.
> - $\varepsilon^{12} = -\varepsilon^{21} = +1$, $\varepsilon_{12} = -\varepsilon_{21} = -1$ (zero on the diagonal), so $\varepsilon^{ab}\varepsilon_{bc} = \delta^a{}_c$; indices are raised and lowered by $\psi^a = \varepsilon^{ab}\psi_b$, $\psi_a = \varepsilon_{ab}\psi^b$, and the same numbers $\varepsilon^{\dot a\dot b}$, $\varepsilon_{\dot a\dot b}$ for dotted indices.
> - Complex conjugation turns an undotted index into a dotted one at the same height: $\bar\psi_{\dot a} \equiv (\psi_a)^*$, $\bar\psi^{a} \equiv (\psi^{\dot a})^*$.
> - $\sigma^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]) carries $(\sigma^\mu)_{a\dot b}$ and $\bar\sigma^\mu$ carries $(\bar\sigma^\mu)^{\dot ab}$. A repeated index is summed only as one upper and one lower index of the same kind.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "Give left-handed spinors a lower index … Right-handed indices are conventionally dotted, $\psi_R^{\dot a}$") · the index positions of $\sigma^\mu$, $\bar\sigma^\mu$ derived here (Theorem §C5a.5.6)*

^def-c5a-5-3

As a matrix, $\varepsilon^{ab}$ is $E = \begin{pmatrix}0&1\\-1&0\end{pmatrix} = i\sigma^2$, and $\varepsilon_{ab}$ is $E^{-1} = -E$. The definition is a bookkeeping device: each index position names a transformation law, and the theorems below say which contractions are invariant.

> [!caution] Caution: Conventions for Weyl spinors
> Three choices are made here and differ across texts. (i) Which half is $(\frac12, 0)$ depends on the sign of the boost generator ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]); with $K_i = \mathcal J^{0i}$ it is Peskin–Schroeder's $\psi_L$, with $\boldsymbol\eta\cdot\boldsymbol\sigma/2$ entering with a minus sign. (ii) The index placement (left-handed lower undotted, right-handed upper dotted) is the user's notes' choice; some texts put the left-handed index up. (iii) The sign of $\varepsilon^{12}$; with the opposite sign, every raised spinor index changes sign, and $\chi^a\psi_a$ with it. Peskin–Schroeder use no index notation and write $\sigma^2\psi_L^*$ where the index calculus gives $\varepsilon\psi_L^* = i\sigma^2\psi_L^*$; the factor $i$ is a phase.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6 (Caution "Which one is (½, 0) depends on the sign of K"), Ch. 8 §8.2 · PS eq. (3.38)*

^cau-c5a-5-1

> [!theorem] Theorem §C5a.5.4: ε Is the Invariant Form of a Weyl Slot
> 1. For every $2\times2$ matrix $M$, with $E = (\varepsilon^{ab})$ of [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]], $M^{\mathsf T}EM = (\det M)\,E$. Hence $\varepsilon$ is invariant under $SL(2, \mathbb C)$: $\Lambda_L^{\mathsf T}E\Lambda_L = E$, $\Lambda_R^{\mathsf T}E\Lambda_R = E$.
> 2. An upper undotted index transforms with $(\Lambda_L^{\mathsf T})^{-1}$: $\psi^a \to \psi^b(\Lambda_L^{-1})_b{}^a$.
> 3. $\chi^a\psi_a = \varepsilon^{ab}\chi_b\psi_a$ is invariant; $\chi_a\psi^a = -\chi^a\psi_a$; for commuting components $\psi^a\psi_a = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "$M^{\mathsf T}EM = (\det M)E$ … $E$ is an invariant bilinear form on the left-handed slot … the position of the contracted index matters"; checked numerically there)*

^thm-c5a-5-4

> [!derivation]- Derivation
> **1. The determinant identity.** Write $M = \begin{pmatrix}m_{11}&m_{12}\\m_{21}&m_{22}\end{pmatrix}$. Then $EM = \begin{pmatrix}m_{21}&m_{22}\\-m_{11}&-m_{12}\end{pmatrix}$ and
>
> $$
> M^{\mathsf T}EM = \begin{pmatrix}m_{11}&m_{21}\\m_{12}&m_{22}\end{pmatrix}\begin{pmatrix}m_{21}&m_{22}\\-m_{11}&-m_{12}\end{pmatrix} = \begin{pmatrix}m_{11}m_{21} - m_{21}m_{11} & m_{11}m_{22} - m_{21}m_{12}\\ m_{12}m_{21} - m_{22}m_{11} & m_{12}m_{22} - m_{22}m_{12}\end{pmatrix} = (\det M)\,E .
> $$
>
> With $\det\Lambda_L = \det\Lambda_R = 1$ (Theorem §C5a.4.1) the form is invariant.
>
> **2. Raising an index.** As columns, $\psi^{\uparrow} = E\psi$. Under $\psi \to \Lambda_L\psi$, $\psi^\uparrow \to E\Lambda_L\psi = (E\Lambda_LE^{-1})\psi^\uparrow$. From part 1, $\Lambda_L^{\mathsf T}E\Lambda_L = E$, so $E\Lambda_LE^{-1} = (\Lambda_L^{\mathsf T})^{-1}$ (multiply on the left by $(\Lambda_L^{\mathsf T})^{-1}$ and on the right by $E^{-1}$). In components $(\Lambda_L^{\mathsf T})^{-1}$ acting on $\psi^\uparrow$ is $\psi^b(\Lambda_L^{-1})_b{}^a$.
>
> **3. The invariant.** $\chi^a\psi_a = \sum_a(E\chi)_a\psi_a = (E\chi)^{\mathsf T}\psi = \chi^{\mathsf T}E^{\mathsf T}\psi$. Under the transformation it becomes $\chi^{\mathsf T}\Lambda_L^{\mathsf T}E^{\mathsf T}\Lambda_L\psi = -\chi^{\mathsf T}(\Lambda_L^{\mathsf T}E\Lambda_L)\psi = -\chi^{\mathsf T}E\psi = \chi^{\mathsf T}E^{\mathsf T}\psi$, using $E^{\mathsf T} = -E$ and part 1. Equivalently, an upper index (step 2) against a lower one: $(\Lambda_L^{-1})_b{}^a(\Lambda_L)_a{}^c = \delta_b{}^c$.
>
> **4. The sign.** $\chi_a\psi^a = \chi_a\varepsilon^{ab}\psi_b = -\varepsilon^{ba}\chi_a\psi_b = -\chi^b\psi_b$, by antisymmetry of $\varepsilon$ and relabelling. For commuting numbers $\psi^a\psi_a = \varepsilon^{ab}\psi_b\psi_a$ is an antisymmetric matrix contracted with the symmetric $\psi_b\psi_a$: zero. ⚑ By-product: for anticommuting (Grassmann-valued) components $\psi_b\psi_a = -\psi_a\psi_b$ and $\psi^a\psi_a = \varepsilon^{12}\psi_2\psi_1 + \varepsilon^{21}\psi_1\psi_2 = \psi_2\psi_1 - \psi_1\psi_2 = -2\psi_1\psi_2 \ne 0$: a Lorentz-invariant mass term built from one Weyl field alone exists only for anticommuting fields (Majorana masses, QFT C9, planned; anticommuting fields, [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).
>
> **What the derivation shows**
> - $\varepsilon$ plays for a Weyl slot the role $g$ plays for a vector slot (an invariant bilinear form that raises and lowers), but it is antisymmetric; that is why index positions in a contraction matter and why a single slot's "length squared" vanishes.
> - Invariance of $\varepsilon$ is exactly $\det = 1$: $SL(2, \mathbb C)$ is the group of complex $2\times2$ matrices preserving an antisymmetric form, $Sp(2, \mathbb C)$.

^der-c5a-5-4

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]

Theorem §C5a.5.5 uses that complex conjugation exchanges the two copies:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-10]]

> [!theorem] Theorem §C5a.5.5: Dotted Indices, Conjugation and the Invariant Pairings
> 1. If $\psi_a$ is left-handed, $\bar\psi_{\dot a} = (\psi_a)^*$ transforms with $\Lambda_L^*$, and $\bar\psi^{\dot a} = \varepsilon^{\dot a\dot b}\bar\psi_{\dot b}$, i.e. $E\psi_L^* = i\sigma^2\psi_L^*$, transforms with $\Lambda_R$: it is right-handed (the spin-½ case of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]). Conversely $(\psi^{\dot a})^*$ transforms with $\Lambda_R^* = (\Lambda_L^{\mathsf T})^{-1}$, as an upper undotted index.
> 2. Invariant pairings: $\psi_R^\dagger\chi_L = \bar\psi^a\chi_a$, $\psi_L^\dagger\chi_R = \bar\psi_{\dot a}\chi^{\dot a}$, $\chi^a\psi_a$, $\chi_{\dot a}\psi^{\dot a}$. A dotted index is never contracted with an undotted one: $\chi_R^{\mathsf T}E\psi_L$ is not invariant.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "Right-handed spinors are a different slot … The two slots are paired instead through complex conjugation"; Derivation "The two halves … related by conjugation") · PS eq. (3.38)*

^thm-c5a-5-5

> [!derivation]- Derivation
> **1. Conjugating a left-handed spinor.** $\psi_L \to \Lambda_L\psi_L$ gives $\psi_L^{\ast} \to \Lambda_L^{\ast}\psi_L^{\ast}$. Raise with $E$: $E\psi_L^{\ast} \to E\Lambda_L^{\ast}E^{-1}\,E\psi_L^{\ast}$. By Theorem §C5a.4.1, 3, $\Lambda_L^{\ast} = \sigma^2\Lambda_R\sigma^2$; with $E = i\sigma^2$, $E^{-1} = -i\sigma^2$ and $(\sigma^2)^2 = \mathbb 1$: $E\Lambda_L^{\ast}E^{-1} = (i\sigma^2)\sigma^2\Lambda_R\sigma^2(-i\sigma^2) = \Lambda_R$. So $E\psi_L^{\ast}$ transforms with $\Lambda_R$.
>
> **2. Conjugating a right-handed spinor.** $\Lambda_R = (\Lambda_L^\dagger)^{-1}$ (Theorem §C5a.4.1, 2), so $\Lambda_R^{\ast} = ((\Lambda_L^\dagger)^{\ast})^{-1} = (\Lambda_L^{\mathsf T})^{-1}$, which is the law of an upper undotted index (Theorem §C5a.5.4, 2).
>
> **3. The pairings without ε.** $\psi_R^\dagger\chi_L \to \psi_R^\dagger\Lambda_R^\dagger\Lambda_L\chi_L$, and $\Lambda_R^\dagger = \Lambda_L^{-1}$ (the adjoint of step 2's relation), so it is invariant: an upper undotted index ($\psi_R^{\ast}$, step 2) against a lower undotted one. Likewise $\psi_L^\dagger\chi_R \to \psi_L^\dagger\Lambda_L^\dagger\Lambda_R\chi_R = \psi_L^\dagger\chi_R$, since $\Lambda_L^\dagger\Lambda_R = \Lambda_L^\dagger(\Lambda_L^\dagger)^{-1} = \mathbb 1$.
>
> **4. The pairings with ε.** $\chi^a\psi_a$ is Theorem §C5a.5.4, 3. For dotted indices, $\chi_R^{\mathsf T}E\psi_R \to \chi_R^{\mathsf T}\Lambda_R^{\mathsf T}E\Lambda_R\psi_R = \chi_R^{\mathsf T}E\psi_R$ since $\det\Lambda_R = 1$ (Theorem §C5a.5.4, 1).
>
> **5. A mixed contraction fails.** $\chi_R^{\mathsf T}E\psi_L \to \chi_R^{\mathsf T}\Lambda_R^{\mathsf T}E\Lambda_L\psi_L$. Using $E\Lambda_L = (\Lambda_L^{\mathsf T})^{-1}E$: $\Lambda_R^{\mathsf T}E\Lambda_L = (\Lambda_L^{-1}\Lambda_R)^{\mathsf T}E$. For a pure boost $\Lambda_L^{-1}\Lambda_R = e^{\boldsymbol\eta\cdot\boldsymbol\sigma} \ne \mathbb 1$, so the form changes.
>
> **What the derivation shows**
> - Complex conjugation exchanges the two kinds of index, and $\varepsilon$ moves an index up or down: together they show that the conjugate of $(\frac12, 0)$ is $(0, \frac12)$, the spin-½ case of Theorem §CB.16.10 in index form.
> - The invariants that pair left with right are built with $\dagger$, not with $\varepsilon$; in Dirac form they are $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$, so the Dirac mass term $m\bar\psi\psi$ necessarily couples the two handednesses (QFT §C5a.6–§C5a.7).

^der-c5a-5-5

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]]

Theorem §C5a.5.6 uses the tensor-product rule for the labels:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-8]]

> [!theorem] Theorem §C5a.5.6: A Four-Vector Is a Bispinor
> 1. $X_{a\dot b} = x_\mu(\sigma^\mu)_{a\dot b}$ carries one lower undotted and one lower dotted index ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]]): $x \to \Lambda x$ is $X_{a\dot b} \to (\Lambda_L)_a{}^c(\Lambda_L^*)_{\dot b}{}^{\dot d}X_{c\dot d}$.
> 2. $(\bar\sigma^\mu)^{\dot aa} = \varepsilon^{\dot a\dot b}\varepsilon^{ab}(\sigma^\mu)_{b\dot b}$, and $x^\mu = \frac12(\bar\sigma^\mu)^{\dot aa}X_{a\dot a}$.
> 3. So the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) is equivalent to $(\frac12, 0)\otimes\overline{(\frac12, 0)}$; the conjugate is $(0, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]), and $(\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]), with $x \mapsto X$ the equivalence.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering", paragraph "What (SL2Ccover) says about indices": "a four-vector is an object with one left-handed and one right-handed spinor index") · part 2 written out here*

^thm-c5a-5-6

> [!derivation]- Derivation
> **1. Part 1.** By Theorem §C5a.4.6, 1, $x \to \Lambda x$ corresponds to $X \to \Lambda_LX\Lambda_L^\dagger$. In components, $(\Lambda_LX\Lambda_L^\dagger)_{a\dot b} = (\Lambda_L)_a{}^cX_{c\dot d}(\Lambda_L^\dagger)^{\dot d}{}_{\dot b} = (\Lambda_L)_a{}^c(\Lambda_L^{\ast})_{\dot b}{}^{\dot d}X_{c\dot d}$, since $(\Lambda_L^\dagger)_{dk} = (\Lambda_L^{\ast})_{kd}$. The first index transforms with $\Lambda_L$ (lower undotted), the second with $\Lambda_L^{\ast}$ (lower dotted, Theorem §C5a.5.5, 1).
>
> **2. ε on σ.** As matrices, $\varepsilon^{\dot a\dot b}\varepsilon^{ab}(\sigma^\mu)_{b\dot b} = (E(\sigma^\mu)^{\mathsf T}E^{\mathsf T})_{\dot aa}$. Since $\sigma^\mu$ is Hermitian, $(\sigma^\mu)^{\mathsf T} = (\sigma^\mu)^{\ast}$; with $E = i\sigma^2$ and $E^{\mathsf T} = -i\sigma^2$ ($\sigma^2$ is antisymmetric): $E(\sigma^\mu)^{\ast}E^{\mathsf T} = \sigma^2(\sigma^\mu)^{\ast}\sigma^2 = \bar\sigma^\mu$ (Theorem §C5a.1.9, 3).
>
> **3. The inverse.** $\frac12(\bar\sigma^\mu)^{\dot aa}X_{a\dot a} = \frac12\operatorname{tr}(X\bar\sigma^\mu) = x^\mu$ (Theorem §C5a.4.2).
>
> **4. Part 3.** By part 1 the four-vector space, via the bijection $x \mapsto X$ (Theorem §C5a.4.2, extended complex-linearly to $\mathbb C^4 \to M_2(\mathbb C)$), is the tensor product of the left-handed representation and its complex conjugate. The conjugate is equivalent to $(0, \frac12)$ by $E$ (Theorem §C5a.5.5, 1), and $(\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]).
>
> **What the derivation shows**
> - Theorem §C3.2.2 identified the vector as $(\frac12, \frac12)$ by Casimirs; here the identification is an explicit map, and the two "spins ½" of the label are the two indices of $X_{a\dot b}$.
> - $\sigma^\mu_{a\dot b}$ is the invariant tensor that converts a vector index into an undotted–dotted pair; the Dirac matrices are built from it ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]).

^der-c5a-5-6

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]

> [!remark] Remark: What each Weyl index labels
>
> | symbol | transforms with | index type |
> |---|---|---|
> | $\psi_a$ (left-handed, $(\frac12, 0)$) | $\Lambda_L$ | lower undotted |
> | $\psi^a = \varepsilon^{ab}\psi_b$ | $(\Lambda_L^{\mathsf T})^{-1}$ | upper undotted |
> | $\bar\psi_{\dot a} = (\psi_a)^*$ | $\Lambda_L^*$ | lower dotted |
> | $\psi^{\dot a}$ (right-handed, $(0, \frac12)$) | $\Lambda_R = (\Lambda_L^\dagger)^{-1}$ | upper dotted |
> | $\varepsilon^{ab}$, $\varepsilon^{\dot a\dot b}$ | invariant | the two invariant forms |
> | $(\sigma^\mu)_{a\dot b}$, $(\bar\sigma^\mu)^{\dot aa}$ | invariant | one vector slot, one slot of each kind |
>
> Three rules: contract an upper with a lower index of the same kind; conjugation dots or undots an index and keeps its height; $\varepsilon$ raises and lowers, with a sign that depends on which position is contracted. Spinor indices are never moved with $g$. The Dirac index is an undotted and a dotted index stacked ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (table and "The practical test, continued"), §8.2*

^rem-c5a-5-1

> [!remark] Remark: Kinematics allows one handedness, a mass needs both
> Lorentz transformations never mix $\psi_L$ and $\psi_R$ (their matrices are separate), so kinematics allows a theory of one Weyl field alone. Dynamics decides: the only invariants pairing a spinor with a conjugate spinor are $\psi_R^\dagger\chi_L$ and $\psi_L^\dagger\chi_R$ (Theorem §C5a.5.5), so a Dirac mass term couples left to right, and a single Weyl field describes a massless particle (Lecture 7: "Weyl spinors are massless particles. Mass couples $\xi$ and $\eta$"). The equations are [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; that one-handed fields describe neutrinos in the Standard Model is beyond the course.
>
> *Source: PHY 513 Lecture 7, Part B (slide "Spinors and Boosts") · the user's PHY 513 notes, Ch. 8 §8.2 (paragraph "Physics of the split")*

^rem-c5a-5-2

> [!remark]- ★ Remark: Null vectors, spinors and the celestial sphere
> A future null vector has $\det X = 0$ and $\operatorname{tr}X > 0$, so $X$ is positive semidefinite of rank one (Theorem §C5a.4.2, 3): $X = \xi\xi^\dagger$ for a column $\xi \in \mathbb C^2$, unique up to a phase. Then $\lambda X\lambda^\dagger = (\lambda\xi)(\lambda\xi)^\dagger$: the Lorentz group acts on null vectors through a left-handed spinor, $\xi \to \lambda\xi$. Null rays (null vectors up to positive scale) are spinors up to complex scale, the points $z = \xi_1/\xi_2$ of the Riemann sphere $\mathbb{CP}^1$ — the sky seen by an observer — and $\lambda = \begin{pmatrix}a&b\\c&d\end{pmatrix}$ acts on it by the Möbius transformation $z \mapsto (az + b)/(cz + d)$. Boosts thus act on the celestial sphere as conformal maps (aberration). The phase of $\xi$, invisible in $X$, is the spinor's extra datum, the "flag" of Penrose's flagpole picture.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering", parenthetical "the celestial sphere")*

^rem-c5a-5-3

> [!remark] Remark: What each Dirac index labels
>
> | symbol | what it is | indices |
> |---|---|---|
> | $\psi_a$ | a vector of spinor space $\mathbb C^4$ | $a$: Dirac spinor |
> | $(\gamma^\mu)_{ab}$ | a spacetime vector whose components are $4\times4$ matrices | $\mu$: spacetime; $a, b$: spinor |
> | $(S^{\mu\nu})_{ab}$ | a generator as a matrix on $\mathbb C^4$ | $\mu\nu$: generator label; $a, b$: spinor |
> | $(\Lambda_{1/2})_{ab}$ | the transformation of spinor space | $a, b$: spinor |
> | $(\gamma^0)_{ab}$ | the invariant form of the Dirac slot ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1\|Theorem §C5a.6.1]]) | $a, b$: spinor |
>
> Spinor indices are contracted by plain matrix multiplication and never moved with $g$; since $\Lambda_{1/2}$ is not unitary, not even $\psi^\dagger\psi$ is invariant. In the chiral basis the Dirac index is a pair of Weyl indices, $\psi = (\psi_a, \psi^{\dot a})$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-3|Def. §C5a.5.3]]; index positions of $\sigma^\mu$, $\bar\sigma^\mu$: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6|Theorem §C5a.5.6]]), and
>
> $$
> \gamma^\mu = \begin{pmatrix}0 & (\sigma^\mu)_{a\dot b}\\ (\bar\sigma^\mu)^{\dot ab} & 0\end{pmatrix}, \qquad \gamma^\mu\psi = \bigl((\sigma^\mu)_{a\dot b}\psi^{\dot b},\ (\bar\sigma^\mu)^{\dot ab}\psi_b\bigr) :
> $$
>
> $\gamma^\mu$ converts a dotted index into an undotted one and back, so it flips handedness, while $S^{\mu\nu}$, $\Lambda_{1/2}$ and $\gamma^5 = \operatorname{diag}(-1, +1)$ keep each half (figure below). That the Dirac spinor has as many components as a four-vector is a coincidence of four dimensions: in $d$ spacetime dimensions a Dirac spinor has $2^{\lfloor d/2\rfloor}$ components (32 against 10 in $d = 10$).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (table, Principle "Invariant tensors with mixed slots", paragraphs "The practical test, continued", "A coincidence of dimension") · PHY 513 Lecture 8, Part A (slide "Transformations with 4-Vectors and 4-Spinors")*

^rem-c5a-5-4

![[ph-qft-c5-2-1.svg]]
*The Dirac spinor in the chiral basis as two Weyl slots. Lorentz transformations ($S^{\mu\nu}$, $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$) and $\gamma^5$ act within each slot, so the representation is $(\frac12, 0)\oplus(0, \frac12)$ (Theorems §C5a.3.4, §C5a.5.2); $\gamma^\mu$ maps each slot to the other through $\sigma^\mu$ and $\bar\sigma^\mu$, so products of two $\gamma$'s (such as $S^{\mu\nu}$) keep the slots, and $\bar\psi = \psi^\dagger\gamma^0$ pairs each slot with the other, which is why a mass term couples them.*

## Choosing a basis

> [!caution] Caution: Bases and conventions across the sources
> Peskin–Schroeder, the lecture, the user's notes and Yu use the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), in which $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$. Quantum Mechanics C13★ follows Sakurai's **Dirac basis**, $\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ with the same $\gamma^i$ and $\gamma^5$ off-diagonal ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]); the two are related by a fixed unitary matrix (Example §C5a.5.1), so every basis-independent statement holds in both, but statements about "upper and lower components" do not transfer. Peskin–Schroeder warn that books using a chiral basis often differ in signs (e.g. $\gamma^0$ and $\gamma^5$ of opposite sign), and texts with the metric $(-,+,+,+)$ have $\{\gamma^\mu, \gamma^\nu\} = \pm2\eta^{\mu\nu}$ with other factors of $i$.
>
> How spinors, $\gamma$'s, $\bar\psi$ and the equations change between such bases: [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]]; what does not change: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-8|§C5a.7, Remark: What depends on the basis and what does not]].
>
> *Source: PS §3.2, p. 41 · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)") · Sakurai & Napolitano §8.2 (the Dirac basis)*

^cau-c5a-5-2

> [!example] Example §C5a.5.1: The Dirac Basis Is Equivalent to the Chiral Basis
> The Dirac basis of Quantum Mechanics ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]), $\gamma_D^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, $\gamma_D^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$, is carried to the chiral basis by the unitary
>
> $$
> U = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1 & -\mathbb 1 \\ \mathbb 1 & \mathbb 1\end{pmatrix}, \qquad \gamma^\mu = U\gamma_D^\mu U^\dagger, \qquad \gamma^5 = U\gamma_D^5U^\dagger, \quad \gamma_D^5 = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix} .
> $$
>
> *Computation.* $UU^\dagger = \frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \mathbb 1$ (blockwise). $U\gamma_D^0U^\dagger = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \frac12\begin{pmatrix}0&2\\2&0\end{pmatrix} = \gamma^0$. $U\gamma_D^iU^\dagger = \frac12\begin{pmatrix}\sigma^i&\sigma^i\\-\sigma^i&\sigma^i\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \frac12\begin{pmatrix}0&2\sigma^i\\-2\sigma^i&0\end{pmatrix} = \gamma^i$. $U\gamma_D^5U^\dagger = \frac12\begin{pmatrix}-1&1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ (checked numerically). The Dirac basis diagonalizes $\gamma^0$, the energy sign at rest, and suits the nonrelativistic limit ([[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]); the chiral basis diagonalizes $\gamma^5$, the Lorentz structure.
>
> *Larsen's matrix, the other direction.* Problem Set 6, Problem 3(b) starts from the chiral basis and defines the Dirac basis by
>
> $$
> U_D = \frac1{\sqrt2}\bigl(\mathbb 1 - \gamma^5\gamma^0\bigr) = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1 & \mathbb 1 \\ -\mathbb 1 & \mathbb 1\end{pmatrix} = U^\dagger = U^{-1}, \qquad \gamma_D^\mu = U_D\gamma^\mu U_D^\dagger, \qquad \psi_D = U_D\psi ,
> $$
>
> with $\gamma^5$, $\gamma^0$ the chiral matrices ($\gamma^5\gamma^0 = \operatorname{diag}(-\mathbb 1, \mathbb 1)\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix} = \begin{pmatrix}0&-\mathbb 1\\\mathbb 1&0\end{pmatrix}$). $U$ and $U_D$ are one change of basis read in the two directions ([[§C5a.1 Spinor Space and the Clifford Action#^cau-c5a-1-1|§C5a.1, Caution: Which matrix is called U]]); these notes use $U_D$ whenever spinors are carried into the Dirac basis ([[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]]).
>
> The matrix $U$ converts the $\gamma$'s only; the spinors change with the same $U$ by [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]] (one factor $U$ per spinor index), $\bar\psi$ keeps its form because $U$ is unitary ([[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]]), and the plane-wave spinors in the Dirac basis are [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]].
>
> *Source: Sakurai & Napolitano, Modern Quantum Mechanics, §8.2, eqs. (8.52)–(8.55), Problem 8.9 (the Dirac basis, as recorded in Quantum Mechanics C13★) · PS §3.2, p. 41 ("a different representation, in which $\gamma^0$ is diagonal") · the matrix $U$ computed here · PHY 513, Problem Set 6, Problem 3(b) (statement, Larsen: $U_D$ and the name "Dirac representation", "also sometimes called the standard representation but that is misleading"; solution as the user wrote it, derivation below)*

^ex-c5a-5-1

> [!derivation]- Derivation (second route: from the chiral basis with U_D, the user's solution of Problem Set 6, Problem 3(b))
> **1. $U_D$ in blocks.** $\mathbb 1 - \gamma^5\gamma^0 = \begin{pmatrix}\mathbb 1&0\\0&\mathbb 1\end{pmatrix} - \begin{pmatrix}0&-\mathbb 1\\\mathbb 1&0\end{pmatrix} = \begin{pmatrix}\mathbb 1&\mathbb 1\\-\mathbb 1&\mathbb 1\end{pmatrix}$, with $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]) and $\gamma^0$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]. Comparing with $U$ above, $U_D = U^\dagger$ (transpose of a real block matrix).
>
> **2. Unitarity, both products.** $U_D^\dagger = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1&-\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix}$ and
>
> $$
> U_D^\dagger U_D = \frac12\begin{pmatrix}\mathbb 1 + \mathbb 1 & \mathbb 1 - \mathbb 1\\ \mathbb 1 - \mathbb 1 & \mathbb 1 + \mathbb 1\end{pmatrix} = \mathbb 1_4, \qquad U_DU_D^\dagger = \frac12\begin{pmatrix}\mathbb 1 + \mathbb 1 & -\mathbb 1 + \mathbb 1\\ -\mathbb 1 + \mathbb 1 & \mathbb 1 + \mathbb 1\end{pmatrix} = \mathbb 1_4 .
> $$
>
> **3. All four γ's at once.** With $\gamma^\mu = \begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]), first $U_D\gamma^\mu = \frac1{\sqrt2}\begin{pmatrix}\bar\sigma^\mu & \sigma^\mu\\ \bar\sigma^\mu & -\sigma^\mu\end{pmatrix}$, then
>
> $$
> \gamma_D^\mu = U_D\gamma^\mu U_D^\dagger = \frac12\begin{pmatrix}\bar\sigma^\mu & \sigma^\mu\\ \bar\sigma^\mu & -\sigma^\mu\end{pmatrix}\begin{pmatrix}\mathbb 1&-\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix} = \frac12\begin{pmatrix}\bar\sigma^\mu + \sigma^\mu & -\bar\sigma^\mu + \sigma^\mu\\ \bar\sigma^\mu - \sigma^\mu & -\bar\sigma^\mu - \sigma^\mu\end{pmatrix} .
> $$
>
> **4. μ = 0 and μ = i.** $\sigma^0 = \bar\sigma^0 = \mathbb 1$ gives $\gamma_D^0 = \frac12\begin{pmatrix}2\cdot\mathbb 1&0\\0&-2\cdot\mathbb 1\end{pmatrix} = \operatorname{diag}(\mathbb 1, -\mathbb 1)$; $\sigma^i = -\bar\sigma^i$ gives $\gamma_D^i = \frac12\begin{pmatrix}0&2\sigma^i\\-2\sigma^i&0\end{pmatrix} = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$: the Dirac matrices displayed above.
>
> **What the derivation shows**
> - Writing $\gamma^\mu$ through $\sigma^\mu$, $\bar\sigma^\mu$ does all four matrices in one product; the Dirac basis is the sum and difference of the Weyl halves, $\psi_D = \frac1{\sqrt2}(\psi_L + \psi_R,\ \psi_R - \psi_L)$, and $\gamma_D^0$ is diagonal because $\gamma^0$ swaps the halves ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-7|Theorem §C5a.5.7]] explains why $\gamma^5$ then cannot stay diagonal).
> - That the new matrices satisfy the Clifford algebra needs no check: conjugation by any invertible matrix preserves it (Problem Set 6, Problem 3(a); step 1 of [[§C5a.1 Spinor Space and the Clifford Action#^der-c5a-1-12|Derivation §C5a.1.12]]).
> - Used next: the plane-wave spinors in the Dirac basis, $u_D(p) = U_Du(p)$ ([[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]]).

^der-ex-c5a-5-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]

> [!caution] Caution: The upper components are not the particle
> The Lecture 7 slides preview the four components as "spin up/down for particle/anti-particle" (and the handwritten notes attach "particle" to $\xi$, "antiparticle" to $\eta$). As a count this is right: a Dirac field describes two spin states of a particle and two of its antiparticle. As an assignment of components it is wrong in the chiral basis: the halves are the left- and right-handed Weyl spinors, and a particle at rest has *equal* halves, $u \propto (\xi, \xi)$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]]; PS (3.47)). The heuristic belongs to the Dirac basis (Example §C5a.5.1), where nonrelativistic particles live mostly in the upper components.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Caution "'$\xi$ is the particle, $\eta$ the antiparticle'") · PHY 513 Lecture 7, Part B*

^cau-c5a-5-3

> [!theorem] Theorem §C5a.5.7: γ⁰ and γ⁵ Cannot Be Diagonal in the Same Basis
> Each of $\gamma^0$ and $\gamma^5$ is diagonal, with eigenvalues $+1$ and $-1$ each twice, in a basis of its own eigenvectors ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-8|Theorem §C5a.1.8]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]); no basis of $V$ makes both diagonal.
>
> *Source: the argument written here*

^thm-c5a-5-7

> [!derivation]- Derivation
> **1. Each alone.** For $\Gamma^0$ this is Theorem §C5a.1.8. For $\Gamma^5$ the same argument applies with $(\Gamma^5)^2 = \mathrm{id}$ and $\operatorname{tr}\Gamma^5 = 0$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]): the minimal polynomial divides $(z - 1)(z + 1)$, and the trace forces each eigenvalue twice (also part 4 of Theorem §C5a.5.2).
>
> **2. Diagonal matrices commute.** If, in some basis, $\gamma^0 = \operatorname{diag}(a_1, \dots, a_4)$ and $\gamma^5 = \operatorname{diag}(b_1, \dots, b_4)$, then $\gamma^0\gamma^5 = \operatorname{diag}(a_kb_k) = \gamma^5\gamma^0$.
>
> **3. They anticommute.** $\gamma^5\gamma^0 = -\gamma^0\gamma^5$ (Theorem §C5a.5.1). With step 2, $\gamma^0\gamma^5 = -\gamma^0\gamma^5$, so $\gamma^0\gamma^5 = 0$. But $\gamma^0$ and $\gamma^5$ are invertible ($(\gamma^0)^2 = (\gamma^5)^2 = \mathbb 1$), so their product is invertible and not $0$: contradiction.
>
> **What the derivation shows**
> - Choosing a basis means choosing which structure to make visible: the chiral basis diagonalizes $\gamma^5$, the Dirac basis $\gamma^0$ (Remark: Why each basis is used, below).

^der-c5a-5-7

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-8|Theorem §C5a.1.8]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]

> [!remark] Remark: Why each basis is used
> A basis can diagonalize $\gamma^0$ or $\gamma^5$, never both ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-7|Theorem §C5a.5.7]]); each choice makes one structure visible.
> - **Chiral (Weyl) basis**, the course's ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]): $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, so the basis is adapted to the Weyl halves $\psi = (\psi_L, \psi_R)$; $S^{\mu\nu}$ and $\Lambda_{1/2}$ are block diagonal ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]; Lecture 8: "block-diagonal (in our basis)"), so the reduction $(\frac12, 0)\oplus(0, \frac12)$ is manifest; the Dirac equation splits into two-component equations coupled only by $m$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]), which decouple for $m = 0$ into the Weyl fields ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]); at high energy chirality becomes helicity ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]]). Peskin–Schroeder use it "exclusively" as "especially convenient" (PS p. 41); Larsen calls it "the better one for relativistic processes" and for "understanding how the Lorentz group acts on the spinors", "best for pedagogical purposes" (Problem Set 6, comments after Problem 3).
> - **Dirac (standard) basis**, Sakurai's ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]): $\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, adapted to the rest frame, where the time evolution is generated by $m\gamma^0$, and to the nonrelativistic limit, in which two components dominate and obey the Pauli equation ([[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]; Sakurai's free solutions, [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]]). Sakurai's treatment of the discrete symmetries is written in this basis ([[§C13.2★ The Dirac Equation#^thm-c13-2-7|QM Theorem §C13.2.7]]; field theory: QFT C9, planned). It is also the basis behind the heuristic "upper = particle, lower = antiparticle" ([[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-3|§C5a.5, Caution: The upper components are not the particle]]). Larsen's reason (Problem Set 6, comments after Problem 3; he calls it the **Dirac representation**, "standard" being "misleading"): the plane-wave spinor $u_D(p)$ has vanishing lower components at rest, for small momentum the two "large" upper components are the two-component Schrödinger wave function of a spin-½ particle, so the basis is "useful for low energy processes, e.g. for computing relativistic corrections to non-relativistic quantum mechanics" ([[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]]); the matrix that takes the chiral basis there is $U_D$ of [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]].
> - **Majorana basis** (★, next remark): all $\gamma^\mu$ imaginary, adapted to reality; Larsen: "convenient in situations where particles and anti-particles are identified" (Problem Set 6; on his "all the Dirac-matrices are real", see the next remark).
>
> *Source: PS §3.2, p. 41 ("many field theory textbooks choose a different representation, in which $\gamma^0$ is diagonal") · PHY 513 Lecture 8, Part C · the user's PHY 513 notes, Ch. 8 §8.2 · Sakurai §8.2–§8.3 (as recorded in QM C13★) · PHY 513, Problem Set 6, comments after Problem 3 (Larsen) · the comparison written here*

^rem-c5a-5-5

> [!remark]- ★ Remark: The Majorana basis
> Schwartz gives a basis in which every Dirac matrix is purely imaginary,
>
> $$
> \gamma^0 = \begin{pmatrix}0 & \sigma^2\\ \sigma^2 & 0\end{pmatrix}, \quad \gamma^1 = \begin{pmatrix}i\sigma^3 & 0\\ 0 & i\sigma^3\end{pmatrix}, \quad \gamma^2 = \begin{pmatrix}0 & -\sigma^2\\ \sigma^2 & 0\end{pmatrix}, \quad \gamma^3 = \begin{pmatrix}-i\sigma^1 & 0\\ 0 & -i\sigma^1\end{pmatrix}
> $$
>
> (Schwartz (10.74); with $g = (+,-,-,-)$ and $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$, checked numerically here, as are $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, so the basis is Hermitian, and $\gamma^5$ imaginary). By Theorem §C5a.1.14 it is the chiral basis after a change of basis, unitary by Theorem §C5a.2.4, 2 up to a factor. In it $i\gamma^\mu$ is real, so the Dirac operator $i\gamma^\mu\partial_\mu - m$ has real coefficients: with $\psi$ also $\psi^{\ast}$ is a solution, and the condition $\psi^{\ast} = \psi$ is compatible with the equation (written here). Real solutions describe a field equal to its own conjugate; quantized, a fermion that is its own antiparticle, a **Majorana fermion** (Schwartz §11.3; Yu §9.6; QFT C9, planned; the two-component form of the Majorana mass: [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-7|§C5a.7, ★ Remark: A Majorana mass needs no second field]]). The Majorana basis is to reality what the chiral basis is to chirality. Problem Set 6 (comments after Problem 3) describes it as the representation in which "all the Dirac-matrices are real"; with the course's $g = (+,-,-,-)$ and $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ it is the matrices $i\gamma^\mu$ that are real (as above), while the $\gamma^\mu$ themselves are purely imaginary; the two statements agree up to this factor $i$ (equivalently, up to the overall sign of the metric).
>
> *Source: Schwartz, Quantum Field Theory and the Standard Model, §10.3, p. 170, eq. (10.74) ("In this basis the γ-matrices are purely imaginary"), §11.3, p. 192 ("Majorana fermions are their own antiparticles") · PHY 513, Problem Set 6, comments after Problem 3 · the reality argument written here*

^rem-c5a-5-6

> [!remark] Remark: The spin-½ analogy
> For spin $\frac12$, $S_x$ is the off-diagonal $\frac\hbar2\sigma_x$ in the $S_z$ basis and $\operatorname{diag}(\frac\hbar2, -\frac\hbar2)$ in its own eigenbasis; the unitary $U = (\sigma_x + \sigma_z)/\sqrt2$ relates the two and both matrices have eigenvalues $\pm\frac\hbar2$ ([[§C1.4 Change of Basis and Unitary Equivalence#^ex-c1-4-2|QM Example §C1.4.2]], [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-4|QM Theorem §C1.4.4]]). The Dirac case is the same pattern: $\gamma^0$ is off-diagonal in the chiral basis and diagonal in the Dirac basis, $\gamma^5$ the reverse, with eigenvalues $\pm1$ twice either way (Theorems §C5a.1.8, §C5a.5.7). As $S_x$ and $S_z$ cannot be diagonal together because they do not commute, $\gamma^0$ and $\gamma^5$ cannot because they anticommute. And as changing the basis of the spin space changes the components of a spin state but not the state ([[§C1.4 Change of Basis and Unitary Equivalence#^rem-c1-4-1|QM, Remark: Changing the basis is not changing the state]]), changing the basis of $V$ changes $\psi_a$ but not $\psi$. One difference: the spin basis is changed by a unitary to keep probabilities, the spinor basis to keep $\bar\psi$ (Theorem §C5a.2.4) — the Dirac form, not an inner product, is what must be preserved.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 ("like the choice of basis for spin-½") · Sakurai §1.5.4 (as recorded in QM C1.4) · the comparison written here*

^rem-c5a-5-7

> [!remark] Remark: The index rule as a table
>
> | object | slots (Def. §C5a.1.6) | shape | new components | why |
> |---|---|---|---|---|
> | spinor $\psi$, $u^s(p)$, $v^s(p)$ | $V$ | $4\times1$ | $U\psi$ | Theorem §C5a.1.2 |
> | row $\varphi \in V'$, e.g. $\bar\psi$ (Def. §C5a.2.5) | $V'$ | $1\times4$ | $\varphi U^{-1}$ | Theorem §C5a.1.3 |
> | $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$, $\slashed{p}$, $P_L$, $\psi\bar\chi$ | $V\otimes V'$ | $4\times4$ | $U(\cdot)U^{-1}$ | Theorems §C5a.1.2, §C5a.1.7 |
> | $\psi^\dagger$ | conjugate of $V$ | $1\times4$ | $\psi^\dagger U^\dagger$ ($= \psi^\dagger U^{-1}$ iff $U$ unitary) | Derivation §C5a.1.3 |
> | matrix of the Dirac form, $\gamma^0$ in that role | form on $V$ | $4\times4$ | $(U^{-1})^\dagger(\cdot)U^{-1}$ | Theorem §C5a.2.1 |
> | $\bar\psi\chi$, $\bar\psi\gamma^\mu\chi$, $\operatorname{tr}(\gamma^\mu\gamma^\nu)$, eigenvalues | none (all contracted) | number | unchanged | Theorems §C5a.1.3, §C5a.1.4, §C5a.2.4 |
>
> The spacetime index $\mu$ of $\gamma^\mu$ is not touched by a change of basis of $V$; it belongs to Minkowski space ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (table of what each index labels) · [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]] · the rule column written here*

^rem-c5a-5-8

> [!remark] Remark: What the Lorentz group adds to the Dirac matrices of Quantum Mechanics
> Quantum Mechanics C13★ reaches the same algebra from the requirement that a first-order wave equation imply Klein–Gordon ([[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]]), and records the transformation $S^{-1}\gamma^\mu S = \Lambda^\mu{}_\nu\gamma^\nu$ as a checked result ([[§C13.2★ The Dirac Equation#^rem-c13-2-4|QM, Remark: Lorentz covariance and the rapidity]]; its rotation matrix $e^{+i\theta\hat{\mathbf n}\cdot\boldsymbol\Sigma/2}$ is passive, the $\Lambda_{1/2}$ here active). Field theory adds, in this order: the algebra has one $4\times4$ solution up to basis (Pauli's theorem); the generators $\frac i4[\gamma^\mu, \gamma^\nu]$ obey the Lorentz algebra *because of* the Clifford algebra (Theorem §C5a.3.2), so the Dirac spinor is a Lorentz representation before any equation is written; that representation is $(\frac12, 0)\oplus(0, \frac12)$, a reducible sum whose halves are separated by $\gamma^5$; and the covariance of $\gamma^\mu$ is derived, which then makes the Dirac equation covariant ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]). The object is also different: $\psi$ will be a field, not a wave function, quantized with anticommutators ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).
>
> *Source: PS §3.2, pp. 40–42 (the order of the construction) · the user's PHY 513 notes, Ch. 8 §8.1 (the logic (i)–(v) of the section)*

^rem-c5a-5-9

> [!remark]- Connections
> - $\gamma^5 = \frac43(\mathbf J_-^2 - \mathbf J_+^2)$ ties chirality to the two Casimirs of the Lorentz algebra, the spinor counterpart of the invariant $\mathbf E\cdot\mathbf B$ that separates the self-dual and anti-self-dual halves of the field strength — [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]].
> - The Dirac basis of Quantum Mechanics and the chiral basis here are one unitary matrix apart; the former diagonalizes the energy sign at rest and suits the nonrelativistic limit and $g = 2$, the latter diagonalizes $\gamma^5$ and suits the Lorentz structure and massless limits — [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]], [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]].
> - The Dirac basis of Quantum Mechanics is one point of the same orbit of bases; its nonrelativistic structure is why Sakurai uses it — [[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]], [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]].
> - $\varepsilon$ for spinors parallels $g$ for vectors and the symplectic form of Hamiltonian mechanics: $SL(2, \mathbb C) = Sp(2, \mathbb C)$ preserves an antisymmetric form, as canonical transformations preserve $\{q, p\}$ — [[§C1b.4 Hamiltonian Field Theory|§C1b.4]].
> - Chirality is the eigenvalue of a Lorentz-invariant operator on $V$, helicity the spin along a momentum; they meet for massless solutions — [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]], [[§C3.7★ Massless Particles and Helicity|§C3.7★]].
> - $\gamma^5$ generates the chiral transformation $e^{i\alpha\gamma^5}$, which rotates the Weyl halves by opposite phases, $(\psi_L, \psi_R) \to (e^{-i\alpha}\psi_L, e^{i\alpha}\psi_R)$; the projectors $P_{L,R}$ split its current into separately conserved left and right currents when $m = 0$, and the mass, which pairs the halves, breaks it — [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]] (Problem Set 6, Problem 5), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|Theorem §C5a.8.4]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]].
