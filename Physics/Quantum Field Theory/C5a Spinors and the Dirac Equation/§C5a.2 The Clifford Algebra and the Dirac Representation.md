---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.1 Weyl Spinors and SL(2,C)]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.3 The Dirac Equation and Its Lagrangian]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.1 (The Dirac representation), §8.2 (Derivations "How the two halves transform", "The two halves are irreducible, inequivalent, and related by conjugation"), §8.3 (What each spinor index labels), "Lecture 8's starting point", and Ch. 9 §9.6 (Supplement, Definition "The matrix $\gamma^5$", Principle "Properties of $\gamma^5$") · PHY 513 Lecture 7 (Larsen), Part B · PHY 513 Lecture 8, Cheat Sheets I–II and Part A · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 40–43, eqs. (3.22)–(3.30), and §3.4, p. 50, eqs. (3.68)–(3.72) · PHY 513, Problem Set 4, Problem 5(b)–(c) and Problem Set 5, Problem 5(a)–(b) (as the user wrote them; submitted) · Yu Zhao-Huan, 量子场论讲义, §5.1, eqs. (5.1)–(5.40), §5.2, eqs. (5.68)–(5.77) · the user's pre-course notes, §5.1–§5.2.*

Is there a four-dimensional representation of the Lorentz group built from a "square root" of the metric, and what is it? The Lorentz algebra and the list $(j_+, j_-)$ of its finite-dimensional representations are [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] and [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations|§C3.2]]; the Weyl matrices, $\sigma^\mu$, $\bar\sigma^\mu$ and the group $SL(2, \mathbb C)$ are [[§C5a.1 Weyl Spinors and SL(2,C)|§C5a.1]]; Dirac's matrices as a device for a first-order wave equation are [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]. This section defines the Dirac matrices by their algebra alone, proves that the algebra has essentially one $4\times4$ solution (Pauli's theorem), builds from it six generators $S^{\mu\nu}$ that obey the Lorentz algebra, identifies the resulting Dirac representation as $(\frac12, 0)\oplus(0, \frac12)$, proves that $\gamma^\mu$ carries a vector index ($\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$), and introduces $\gamma^5$, whose eigenspaces are the two Weyl halves. The Dirac equation, $\bar\psi$ and the Lagrangian come next ([[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]).

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Hermitian convention, the $D(\mathcal J^{\mu\nu})$ of §C3.2; [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]); $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with the same $\omega_{\mu\nu}$ as $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$, $K_i = \mathcal J^{0i}$. The identity matrix in $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ is usually not written.

## The Clifford algebra

> [!definition] Definition §C5a.2.1: The Dirac Matrices
> **Dirac matrices** ($\gamma$ matrices) are four $n\times n$ complex matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the **Clifford** (Dirac) **algebra**
>
> $$
> \{\gamma^\mu, \gamma^\nu\} \equiv \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\,\mathbb 1_n .
> $$
>
> The label $\mu$ is a spacetime index; the rows and columns are spinor indices (index slots: [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-1|Def. §C3.1.1]]). $g^{\mu\nu}$ is the metric and $\gamma_\mu \equiv g_{\mu\nu}\gamma^\nu$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]).
>
> *Source: PS §3.2, eq. (3.22) · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The Dirac (Clifford) algebra", eq. (clifford)) · PHY 513 Lecture 7, Part B ("Warning: 4 × 4 identity matrix on RHS usually not written") · Yu §5.1, eq. (5.1)*

^def-c5a-2-1

> [!theorem] Theorem §C5a.2.1: First Consequences of the Clifford Algebra
> For Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]):
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

^thm-c5a-2-1

> [!derivation]- Derivation
> **1. Squares.** Put $\nu = \mu$: $2(\gamma^\mu)^2 = 2g^{\mu\mu}\mathbb 1$ (no sum), so $(\gamma^0)^2 = g^{00} = 1$ and $(\gamma^i)^2 = g^{ii} = -1$. Hence $(\gamma^0)^{-1} = \gamma^0$ and $(\gamma^i)^{-1} = -\gamma^i$.
>
> **2. Distinct indices.** For $\mu \ne \nu$, $g^{\mu\nu} = 0$, so $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 0$.
>
> **3. Square root.** $(a_\mu\gamma^\mu)^2 = a_\mu a_\nu\gamma^\mu\gamma^\nu$. The coefficient $a_\mu a_\nu$ is symmetric in $\mu\nu$, so only the symmetric part of $\gamma^\mu\gamma^\nu$ contributes: $a_\mu a_\nu\gamma^\mu\gamma^\nu = \frac12a_\mu a_\nu(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) = a_\mu a_\nu g^{\mu\nu}\mathbb 1 = a^2\mathbb 1$.
>
> **4. The split.** Add and subtract $\frac12\gamma^\nu\gamma^\mu$: $\gamma^\mu\gamma^\nu = \frac12(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu) + \frac12(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)$. The first bracket is $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]). For a symmetric $S_{\mu\nu}$, $S_{\mu\nu}[\gamma^\mu, \gamma^\nu] = 0$: renaming the dummy indices $\mu \leftrightarrow \nu$ turns it into its own negative. For an antisymmetric $A_{\mu\nu}$, $A_{\mu\nu}g^{\mu\nu} = 0$ for the same reason. Step 3 is the case $S_{\mu\nu} = a_\mu a_\nu$.
>
> **What the derivation shows**
> - The algebra says exactly "the $\gamma$'s square to the metric and anticommute"; part 2 is the same statement for every direction at once.
> - Used next: Hermiticity (Theorem §C5a.2.3), the sixteen products (Theorem §C5a.2.4), Dirac ⇒ Klein–Gordon ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]]), the slash algebra ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]).
> - The split is the working trick for products of two γ's. With $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$ it reads $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]); it gives the second form of the spinor generators (Def. §C5a.2.3 below), $\slashed a\slashed b = a\cdot b - i\sigma^{\mu\nu}a_\mu b_\nu$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]), and, iterated, the reduction of any product of γ's to antisymmetrized products ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-8|Theorem §C5a.7.8]]).

^der-c5a-2-1

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]

> [!remark] Remark: A square root of p²
> The handwritten question "square to $\pm1$, or square root?" has a precise answer: for a momentum $p$, $p_\mu\gamma^\mu$ is a matrix square root of the number $p^2$ (Theorem §C5a.2.1, 2). This is what Dirac was after: a first-order operator whose square is the Klein–Gordon operator, $(i\gamma^\mu\partial_\mu)^2 = -\partial^2$, so that a first-order equation implies $(\partial^2 + m^2)\psi = 0$ ([[§C13.2★ The Dirac Equation#^rem-c13-2-1|QM, Remark: The square root of the Klein–Gordon operator]]; [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]]). No number squares to $p^2$ as a linear function of $p$; anticommuting matrices do, because the cross terms cancel in pairs.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Square to ±1, or square root?")*

^rem-c5a-2-1

> [!definition] Definition §C5a.2.2: The Chiral Basis
> The **chiral** (**Weyl**) **basis** is, in $2\times2$ blocks, with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]],
>
> $$
> \gamma^0 = \begin{pmatrix} 0 & \mathbb 1 \\ \mathbb 1 & 0 \end{pmatrix}, \qquad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}, \qquad\text{i.e.}\qquad \gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix} .
> $$
>
> A Dirac spinor in this basis is written $\psi = \binom{\psi_L}{\psi_R}$, with two-component upper and lower halves (the Weyl spinors of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]], Theorem §C5a.2.9).
>
> *Source: PS §3.2, eqs. (3.25), (3.36), (3.42) · PHY 513 Lecture 7, Part B (slide "Explicit Form of Dirac Matrices"); Lecture 8, Cheat Sheet I and Part C ("Economical form of all 4 $\gamma$-matrices") · the user's PHY 513 notes, Ch. 8 §8.1, eq. (chiralbasis), §8.2, eq. (weylsplit) · Yu §5.2, eqs. (5.68), (5.75)*

^def-c5a-2-2

> [!theorem] Theorem §C5a.2.2: The Chiral Matrices Satisfy the Clifford Algebra
> The matrices of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]] satisfy $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\mathbb 1_4$, and $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Checking the Dirac algebra in the chiral basis") · PHY 513 Lecture 7, Part B (sample check $\{\gamma^0, \gamma^i\} = 0$) · Yu §5.2, eqs. (5.69)–(5.71)*

^thm-c5a-2-2

> [!derivation]- Derivation
> **1. The block product.** $\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}\begin{pmatrix}0&\sigma^\nu\\\bar\sigma^\nu&0\end{pmatrix} = \begin{pmatrix}0\cdot0 + \sigma^\mu\bar\sigma^\nu & 0\cdot\sigma^\nu + \sigma^\mu\cdot0\\ \bar\sigma^\mu\cdot0 + 0\cdot\bar\sigma^\nu & \bar\sigma^\mu\sigma^\nu + 0\cdot0\end{pmatrix} = \begin{pmatrix}\sigma^\mu\bar\sigma^\nu & 0\\ 0 & \bar\sigma^\mu\sigma^\nu\end{pmatrix}$.
>
> **2. The anticommutator.** Adding the same with $\mu \leftrightarrow \nu$: $\{\gamma^\mu, \gamma^\nu\} = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu + \sigma^\nu\bar\sigma^\mu,\ \bar\sigma^\mu\sigma^\nu + \bar\sigma^\nu\sigma^\mu) = \operatorname{diag}(2g^{\mu\nu}\mathbb 1, 2g^{\mu\nu}\mathbb 1)$ by [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-1|Theorem §C5a.1.1]], 2.
>
> **3. Explicitly (the lecture's check).** $(\gamma^0)^2 = \operatorname{diag}(\mathbb 1, \mathbb 1)$; $\gamma^0\gamma^i = \operatorname{diag}(-\sigma^i, \sigma^i)$ and $\gamma^i\gamma^0 = \operatorname{diag}(\sigma^i, -\sigma^i)$, so $\{\gamma^0, \gamma^i\} = 0$; $\gamma^i\gamma^j = \operatorname{diag}(-\sigma^i\sigma^j, -\sigma^i\sigma^j)$, so $\{\gamma^i, \gamma^j\} = -\operatorname{diag}(\{\sigma^i, \sigma^j\}, \{\sigma^i, \sigma^j\}) = -2\delta^{ij}\mathbb 1_4 = 2g^{ij}\mathbb 1_4$. All ten conditions hold.
>
> **What the derivation shows**
> - The Clifford algebra of $\gamma$ is the pair identity of $\sigma$, $\bar\sigma$ stacked off-diagonally; every product of two $\gamma$'s is block diagonal, every product of an odd number off-diagonal. That is why the generators (products of two) will not mix the halves (Theorem §C5a.2.8).

^der-c5a-2-2

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-1|Theorem §C5a.1.1]]

> [!caution] Caution: Bases and conventions across the sources
> Peskin–Schroeder, the lecture, the user's notes and Yu use the chiral basis above, in which $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$. Quantum Mechanics C13★ follows Sakurai's **Dirac basis**, $\gamma^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ with the same $\gamma^i$ and $\gamma^5$ off-diagonal ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]); the two are related by a fixed unitary matrix (Example §C5a.2.1), so every basis-independent statement holds in both, but statements about "upper and lower components" do not transfer. Peskin–Schroeder warn that books using a chiral basis often differ in signs (e.g. $\gamma^0$ and $\gamma^5$ of opposite sign), and texts with the metric $(-,+,+,+)$ have $\{\gamma^\mu, \gamma^\nu\} = \pm2\eta^{\mu\nu}$ with other factors of $i$.
>
> *Source: PS §3.2, p. 41 · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)") · Sakurai & Napolitano §8.2 (the Dirac basis)*

^cau-c5a-2-1

> [!theorem] Theorem §C5a.2.3: Hermiticity of the Dirac Matrices
> 1. In the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), $\gamma^{0\dagger} = \gamma^0$ and $\gamma^{i\dagger} = -\gamma^i$, equivalently $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; each $\gamma^\mu$ is unitary.
> 2. The same holds in any basis in which each $\gamma^\mu$ is a normal matrix, and in particular in any basis reached from the chiral one by a unitary matrix.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", eq. (gammadagger)) · Yu §5.1, eqs. (5.4)–(5.7) · the user's pre-course notes, §5.1 ("Hermiticity"; "hypothesis … arrangeable by a change of basis") · PHY 513, Problem Set 5, Problem 5(b) (the chiral-basis check, as the user wrote it)*

^thm-c5a-2-3

> [!derivation]- Derivation
> **1. Chiral basis.** $\gamma^{0\dagger}$: transposing $\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ and conjugating gives itself. $\gamma^{i\dagger} = \begin{pmatrix}0&(-\sigma^i)^\dagger\\(\sigma^i)^\dagger&0\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix} = -\gamma^i$, the Pauli matrices being Hermitian ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]).
>
> **2. The compact form.** $\gamma^0\gamma^0\gamma^0 = \gamma^0$ (Theorem §C5a.2.1); $\gamma^0\gamma^i\gamma^0 = -\gamma^i\gamma^0\gamma^0 = -\gamma^i$ (anticommute, then $(\gamma^0)^2 = \mathbb 1$). So $\gamma^0\gamma^\mu\gamma^0$ equals $\gamma^{\mu\dagger}$ for every $\mu$.
>
> **3. Unitarity.** $\gamma^{0\dagger}\gamma^0 = (\gamma^0)^2 = \mathbb 1$, $\gamma^{i\dagger}\gamma^i = -(\gamma^i)^2 = \mathbb 1$.
>
> **4. Normal matrices.** If $\gamma^\mu$ is normal, it is $W\operatorname{diag}(d_1, \dots, d_n)W^\dagger$ with $W$ unitary (spectral theorem). Then $(\gamma^\mu)^2 = W\operatorname{diag}(d_k^2)W^\dagger = g^{\mu\mu}\mathbb 1$ forces $d_k^2 = g^{\mu\mu}$: $d_k = \pm1$ for $\mu = 0$, $d_k = \pm i$ for $\mu = i$. Real eigenvalues make $\gamma^0 = W\operatorname{diag}(d_k)W^\dagger$ Hermitian; imaginary ones make $\gamma^i$ anti-Hermitian, $(W\operatorname{diag}(d_k)W^\dagger)^\dagger = W\operatorname{diag}(d_k^{\ast})W^\dagger = -\gamma^i$. (One $W$ per matrix: the four are not simultaneously diagonalizable, since they anticommute.)
>
> **5. Unitary changes of basis.** If $\gamma'^\mu = U\gamma^\mu U^\dagger$ with $U$ unitary, then $\gamma'^{\mu\dagger} = U\gamma^{\mu\dagger}U^\dagger = U\gamma^0\gamma^\mu\gamma^0U^\dagger = \gamma'^0\gamma'^\mu\gamma'^0$, inserting $U^\dagger U = \mathbb 1$ between the factors.
>
> **What the derivation shows**
> - Hermiticity is not part of the Clifford algebra: a non-unitary change of basis preserves the algebra (Theorem §C5a.2.5) but destroys it. It is a choice of basis, assumed from here on; in Yu and the pre-course notes it enters as the hypothesis "normal".
> - $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ is the identity used for every adjoint in Dirac theory: the generators (Theorem §C5a.2.11), $\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]), the reality of bilinears ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]]).

^der-c5a-2-3

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!theorem] Theorem §C5a.2.4: The Sixteen Products Are a Basis
> For $A = \{\mu_1 < \dots < \mu_k\} \subseteq \{0, 1, 2, 3\}$ let $\Gamma_A = \gamma^{\mu_1}\cdots\gamma^{\mu_k}$ ($\Gamma_\varnothing = \mathbb 1$). For Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]) of any size $n$:
> 1. $\Gamma_A\Gamma_B = \pm\Gamma_{A\triangle B}$ (symmetric difference), with a sign fixed by the algebra alone; in particular $\Gamma_A^2 = \pm\mathbb 1$;
> 2. $\operatorname{tr}\Gamma_A = 0$ for $A \ne \varnothing$;
> 3. the sixteen $\Gamma_A$ are linearly independent, so $n \ge 4$;
> 4. for $n = 4$ they are a basis of $M_4(\mathbb C)$: only multiples of $\mathbb 1$ commute with all $\gamma^\mu$, and no subspace of $\mathbb C^4$ other than $0$ and $\mathbb C^4$ is invariant under all $\gamma^\mu$ (irreducibility, [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]]).
>
> *Source: PS §3.2, p. 41 ("these matrices must be at least 4 × 4") and §3.4, p. 50 (the sixteen matrices) · the user's PHY 513 notes, Ch. 8, paragraph after the bilinears ("the sixteen matrices … are a basis of all 4 × 4 matrices") · the user's pre-course notes, §5.1 ("Dimension of the spinor representation": independence "stated") · Yu §5.1, eq. (5.45) · the trace proof written out here*

^thm-c5a-2-4

> [!derivation]- Derivation
> **1. Products.** Write $\Gamma_A\Gamma_B$ as one string of $\gamma$'s. For each $\mu \in A\cap B$, move the copy of $\gamma^\mu$ from the $B$ part leftwards until it stands next to its partner from $A$; each step past a different $\gamma^\nu$ gives a factor $-1$ (Theorem §C5a.2.1). The pair becomes $(\gamma^\mu)^2 = g^{\mu\mu}\mathbb 1 = \pm\mathbb 1$. What is left is a product of the $\gamma^\mu$ with $\mu \in A\triangle B$, each once, in some order; reordering it increasingly costs one $-1$ per transposition. So $\Gamma_A\Gamma_B = c_{AB}\Gamma_{A\triangle B}$ with $c_{AB} = \pm1$ computed from the anticommutation signs and $g^{\mu\mu}$ only. With $B = A$, $A\triangle A = \varnothing$: $\Gamma_A^2 = c_{AA}\mathbb 1$, and $\Gamma_A^{-1} = c_{AA}\Gamma_A$.
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
> - Everything follows from the anticommutation signs; no explicit matrices were used. The chiral basis is one $4\times4$ solution, so $n = 4$ is attained. That $n$ must be even is [[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], by another trace argument; here the bound comes from independence of all sixteen products at once.
> - Up to factors $\pm1, \pm i$ the sixteen are $\mathbb 1$, $\gamma^\mu$, $\gamma^\mu\gamma^\nu$ ($\mu < \nu$), $\gamma^\mu\gamma^\nu\gamma^\rho$ ($\propto\gamma_\kappa\gamma^5$) and $\gamma^0\gamma^1\gamma^2\gamma^3$ ($\propto\gamma^5$, Def. §C5a.2.5): the scalar, vector, tensor, axial vector and pseudoscalar of the bilinears ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]); reducing any product to them is [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-8|Theorem §C5a.7.8]].
> - ⚑ By-product (step 3): every $\gamma^\mu$ and every product of distinct $\gamma$'s is traceless, the start of trace technology ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]).
> - Used next: Pauli's theorem (Theorem §C5a.2.5), which needs part 4.

^der-c5a-2-4

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR Thm. 8.49]]

> [!theorem] Theorem §C5a.2.5: Pauli's Fundamental Theorem
> 1. If $\gamma^\mu$ and $\gamma'^\mu$ are two sets of $4\times4$ Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), there is an invertible $U$ with $\gamma'^\mu = U\gamma^\mu U^{-1}$ for all $\mu$, unique up to a nonzero factor. Conversely, $U\gamma^\mu U^{-1}$ is a set of Dirac matrices for every invertible $U$.
> 2. If both sets satisfy $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]), $U$ can be chosen unitary.
>
> *Source: PS §3.2, p. 41 ("all 4 × 4 representations of the Dirac algebra are unitarily equivalent", stated) · the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Uniqueness (Pauli's fundamental theorem)", stated) · Yu §5.2, eq. (5.72) (the converse) · the proof (averaging over the sixteen products) written out here*

^thm-c5a-2-5

> [!derivation]- Derivation
> **1. Converse.** $\{U\gamma^\mu U^{-1}, U\gamma^\nu U^{-1}\} = U\{\gamma^\mu, \gamma^\nu\}U^{-1} = 2g^{\mu\nu}U\mathbb 1U^{-1} = 2g^{\mu\nu}\mathbb 1$.
>
> **2. The same signs.** Form $\Gamma_A$ and $\Gamma'_A$ from the two sets. By Theorem §C5a.2.4, 1, $\Gamma_A\Gamma_B = c_{AB}\Gamma_{A\triangle B}$ and $\Gamma'_A\Gamma'_B = c_{AB}\Gamma'_{A\triangle B}$ with the *same* $c_{AB}$, which depends only on the algebra.
>
> **3. An averaged intertwiner.** For any $F \in M_4(\mathbb C)$ set $S_F = \sum_A\Gamma'_AF\Gamma_A^{-1}$ (sixteen terms). For each $B$,
>
> $$
> \Gamma'_BS_F\Gamma_B^{-1} = \sum_A(\Gamma'_B\Gamma'_A)F(\Gamma_B\Gamma_A)^{-1} = \sum_Ac_{BA}\Gamma'_{B\triangle A}\,F\,c_{BA}^{-1}\Gamma_{B\triangle A}^{-1} = \sum_C\Gamma'_CF\Gamma_C^{-1} = S_F ,
> $$
>
> using step 2, $(XY)^{-1} = Y^{-1}X^{-1}$, $c_{BA} = \pm1$, and the change of summation variable $C = B\triangle A$, which runs over all sixteen subsets exactly once as $A$ does ($A = B\triangle C$). So $\Gamma'_BS_F = S_F\Gamma_B$ for all $B$, in particular $\gamma'^\mu S_F = S_F\gamma^\mu$.
>
> **4. Some S_F is nonzero.** The entries of $S_{E_{ij}}$ ($E_{ij}$ the matrix units) are $(S_{E_{ij}})_{ab} = \sum_A(\Gamma'_A)_{ai}(\Gamma_A^{-1})_{jb}$. Put $a = i$, $b = j$ and sum over $i, j$: $\sum_{i,j}(S_{E_{ij}})_{ij} = \sum_A\operatorname{tr}\Gamma'_A\operatorname{tr}\Gamma_A^{-1}$. Every term with $A \ne \varnothing$ vanishes ($\Gamma_A^{-1} = \pm\Gamma_A$ is traceless, Theorem §C5a.2.4, 2), and $A = \varnothing$ gives $4\cdot4 = 16$. So some $S \equiv S_{E_{ij}} \ne 0$.
>
> **5. S is invertible.** If $Sv = 0$, then $S\gamma^\mu v = \gamma'^\mu Sv = 0$: $\ker S$ is invariant under all $\gamma^\mu$, so it is $0$ or $\mathbb C^4$ (Theorem §C5a.2.4, 4); it is not $\mathbb C^4$ since $S \ne 0$. (Schur's argument, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]].) Take $U = S$: $\gamma'^\mu = U\gamma^\mu U^{-1}$.
>
> **6. Uniqueness.** If also $\gamma'^\mu = V\gamma^\mu V^{-1}$, then $V^{-1}U$ commutes with every $\gamma^\mu$, so $V^{-1}U = c\mathbb 1$ (Theorem §C5a.2.4, 4), $c \ne 0$.
>
> **7. Unitary choice.** If both sets obey $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, all $\gamma^\mu$, $\gamma'^\mu$ are unitary (Theorem §C5a.2.3, whose step 3 used only this relation and the algebra), hence so are all products $\Gamma_A$, $\Gamma'_A$. Take the adjoint of $\Gamma'_AU = U\Gamma_A$: $U^\dagger\Gamma'^{-1}_A = \Gamma_A^{-1}U^\dagger$, i.e. $\Gamma_AU^\dagger = U^\dagger\Gamma'_A$. Then $U^\dagger U\Gamma_A = U^\dagger\Gamma'_AU = \Gamma_AU^\dagger U$: $U^\dagger U$ commutes with every $\Gamma_A$, so $U^\dagger U = c\mathbb 1$; it is positive definite ($v^\dagger U^\dagger Uv = |Uv|^2 > 0$), so $c > 0$, and $U/\sqrt c$ is unitary and still intertwines.
>
> **What the derivation shows**
> - "There are many realizations of $\gamma^\mu$" (Lecture 7) means one realization in many bases, exactly as spin $\frac12$ has one set of Pauli matrices up to a change of basis. Every basis-independent statement may be proved in the chiral basis and holds everywhere.
> - The trick of step 3, averaging over a finite group ($\pm\Gamma_A$, $32$ elements), is the finite version of the invariant averaging behind complete reducibility ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]]).
> - Used next: Example §C5a.2.1; the basis independence of $\gamma^5$'s eigenspaces (Theorem §C5a.2.14).

^der-c5a-2-5

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]

> [!example] Example §C5a.2.1: The Dirac Basis Is Equivalent to the Chiral Basis
> The Dirac basis of Quantum Mechanics ([[§C13.2★ The Dirac Equation#^cau-c13-2-1|QM, Caution: Dirac matrices]]), $\gamma_D^0 = \operatorname{diag}(\mathbb 1, -\mathbb 1)$, $\gamma_D^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$, is carried to the chiral basis by the unitary
>
> $$
> U = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1 & -\mathbb 1 \\ \mathbb 1 & \mathbb 1\end{pmatrix}, \qquad \gamma^\mu = U\gamma_D^\mu U^\dagger, \qquad \gamma^5 = U\gamma_D^5U^\dagger, \quad \gamma_D^5 = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix} .
> $$
>
> *Computation.* $UU^\dagger = \frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \mathbb 1$ (blockwise). $U\gamma_D^0U^\dagger = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \frac12\begin{pmatrix}0&2\\2&0\end{pmatrix} = \gamma^0$. $U\gamma_D^iU^\dagger = \frac12\begin{pmatrix}\sigma^i&\sigma^i\\-\sigma^i&\sigma^i\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \frac12\begin{pmatrix}0&2\sigma^i\\-2\sigma^i&0\end{pmatrix} = \gamma^i$. $U\gamma_D^5U^\dagger = \frac12\begin{pmatrix}-1&1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix} = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ (checked numerically). The Dirac basis diagonalizes $\gamma^0$, the energy sign at rest, and suits the nonrelativistic limit ([[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]]); the chiral basis diagonalizes $\gamma^5$, the Lorentz structure.
>
> *Source: Sakurai & Napolitano, Modern Quantum Mechanics, §8.2, eqs. (8.52)–(8.55), Problem 8.9 (the Dirac basis, as recorded in Quantum Mechanics C13★) · PS §3.2, p. 41 ("a different representation, in which $\gamma^0$ is diagonal") · the matrix $U$ computed here*

^ex-c5a-2-1

> [!remark] Remark: What the Lorentz group adds to the Dirac matrices of Quantum Mechanics
> Quantum Mechanics C13★ reaches the same algebra from the requirement that a first-order wave equation imply Klein–Gordon ([[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]]), and records the transformation $S^{-1}\gamma^\mu S = \Lambda^\mu{}_\nu\gamma^\nu$ as a checked result ([[§C13.2★ The Dirac Equation#^rem-c13-2-4|QM, Remark: Lorentz covariance and the rapidity]]; its rotation matrix $e^{+i\theta\hat{\mathbf n}\cdot\boldsymbol\Sigma/2}$ is passive, the $\Lambda_{1/2}$ here active). Field theory adds, in this order: the algebra has one $4\times4$ solution up to basis (Pauli's theorem); the generators $\frac i4[\gamma^\mu, \gamma^\nu]$ obey the Lorentz algebra *because of* the Clifford algebra (Theorem §C5a.2.7), so the Dirac spinor is a Lorentz representation before any equation is written; that representation is $(\frac12, 0)\oplus(0, \frac12)$, a reducible sum whose halves are separated by $\gamma^5$; and the covariance of $\gamma^\mu$ is derived, which then makes the Dirac equation covariant ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]]). The object is also different: $\psi$ will be a field, not a wave function, quantized with anticommutators ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).
>
> *Source: PS §3.2, pp. 40–42 (the order of the construction) · the user's PHY 513 notes, Ch. 8 §8.1 (the logic (i)–(v) of the section)*

^rem-c5a-2-2

## The spinor generators

> [!definition] Definition §C5a.2.3: The Spinor Generators
> Given Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), the six **spinor generators** are
>
> $$
> S^{\mu\nu} = \frac i4\,[\gamma^\mu, \gamma^\nu] = -S^{\nu\mu}, \qquad\text{equivalently}\qquad S^{\mu\nu} = \frac i2\bigl(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbb 1\bigr) .
> $$
>
> *Source: PS §3.2, eq. (3.23) · PHY 513 Lecture 7, Part B ("Given such $\gamma^\mu$, form a $4\times4$ matrix for each $(\mu\nu)$ pair") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor generators", eq. (Sdef)) · Yu §5.1, eqs. (5.8)–(5.9) · the user's pre-course notes, §5.1, eq. (spinor-generators)*

^def-c5a-2-3

The second form follows from $\gamma^\nu\gamma^\mu = 2g^{\mu\nu} - \gamma^\mu\gamma^\nu$: $[\gamma^\mu, \gamma^\nu] = 2\gamma^\mu\gamma^\nu - 2g^{\mu\nu}$. For $\mu \ne \nu$, $S^{\mu\nu} = \frac i2\gamma^\mu\gamma^\nu$; $S^{\mu\mu} = 0$. Yu and Peskin–Schroeder also use $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu}$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]]).

> [!theorem] Theorem §C5a.2.6: The Dirac Matrices Rotate as a Vector
> With the vector generators $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]],
>
> $$
> [\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\,\gamma^\nu = i\bigl(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho\bigr) .
> $$
>
> *Source: PHY 513, Problem Set 4, Problem 5(b) (as the user wrote it) · PS §3.2, p. 42 (stated, "with a short computation") · PHY 513 Lecture 8, Part A ("Compute (using Dirac algebra)") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 1, eq. (gammaS)) · Yu §5.1, eqs. (5.11), (5.24)*

^thm-c5a-2-6

> [!derivation]- Derivation
> (The user's solution of Problem Set 4, Problem 5(b).)
>
> **1. Pull out the factor.** By linearity of the commutator, $[\gamma^\mu, S^{\rho\sigma}] = \frac i4[\gamma^\mu, [\gamma^\rho, \gamma^\sigma]]$, and $[\gamma^\mu, [\gamma^\rho, \gamma^\sigma]] = [\gamma^\mu, \gamma^\rho\gamma^\sigma] - [\gamma^\mu, \gamma^\sigma\gamma^\rho]$.
>
> **2. The reordering identity.** For any matrices, $[A, BC] = \{A, B\}C - B\{A, C\}$: the right side is $ABC + BAC - BAC - BCA = ABC - BCA$. Applied to both terms:
>
> $$
> [\gamma^\mu, [\gamma^\rho, \gamma^\sigma]] = \{\gamma^\mu, \gamma^\rho\}\gamma^\sigma - \gamma^\rho\{\gamma^\mu, \gamma^\sigma\} - \{\gamma^\mu, \gamma^\sigma\}\gamma^\rho + \gamma^\sigma\{\gamma^\mu, \gamma^\rho\} .
> $$
>
> **3. Insert the algebra.** Each anticommutator is $2g\,\mathbb 1$, a number times the identity, which commutes with every $\gamma$ and may be moved freely: the four terms are $2g^{\mu\rho}\gamma^\sigma - 2g^{\mu\sigma}\gamma^\rho - 2g^{\mu\sigma}\gamma^\rho + 2g^{\mu\rho}\gamma^\sigma = 4(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$.
>
> **4. Restore the factor and read off J.** $[\gamma^\mu, S^{\rho\sigma}] = \frac i4\cdot4(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho) = i(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$. Write $\gamma^\sigma = \delta^\sigma{}_\nu\gamma^\nu$, $\gamma^\rho = \delta^\rho{}_\nu\gamma^\nu$ and use $g^{\mu\rho} = g^{\rho\mu}$: $i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)\gamma^\nu = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$.
>
> **What the derivation shows**
> - The commutator with a spinor generator acts on the *label* $\mu$ of $\gamma^\mu$ exactly as the vector generator acts on a four-vector: the infinitesimal form of "$\gamma^\mu$ is a vector" (finite form, Theorem §C5a.2.12).
> - Only the Clifford algebra was used; the result holds in every basis and every dimension $n$.
> - Used next: the Lorentz algebra for $S^{\mu\nu}$ (Theorem §C5a.2.7).

^der-c5a-2-6

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]

> [!theorem] Theorem §C5a.2.7: The Spinor Generators Obey the Lorentz Algebra
>
> $$
> [S^{\mu\nu}, S^{\rho\sigma}] = i\bigl(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho}\bigr) ,
> $$
>
> the relations of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] with $\mathcal J \to S$. Hence the $S^{\mu\nu}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]) are the generators of a representation of the Lorentz algebra on $\mathbb C^n$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-1|Def. §C3.2.1]]).
>
> *Source: PHY 513, Problem Set 4, Problem 5(c) (as the user wrote it) · PS §3.2, p. 40 ("By repeated use of (3.22), it is easy to verify") · PHY 513 Lecture 7, Part B ("Claim: $S^{\mu\nu}$ satisfy Lorentz algebra") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 2) · Yu §5.1, eq. (5.12)*

^thm-c5a-2-7

> [!derivation]- Derivation
> (The user's solution of Problem Set 4, Problem 5(c).)
>
> **1. Pull out the factor.** $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4X$ with $X \equiv [[\gamma^\mu, \gamma^\nu], S^{\rho\sigma}] = [\gamma^\mu\gamma^\nu, S^{\rho\sigma}] - [\gamma^\nu\gamma^\mu, S^{\rho\sigma}]$.
>
> **2. Product rule.** With $[AB, C] = A[B, C] + [A, C]B$ (expand: $ABC - ACB + ACB - CAB$):
>
> $$
> X = \gamma^\mu[\gamma^\nu, S^{\rho\sigma}] + [\gamma^\mu, S^{\rho\sigma}]\gamma^\nu - \gamma^\nu[\gamma^\mu, S^{\rho\sigma}] - [\gamma^\nu, S^{\rho\sigma}]\gamma^\mu .
> $$
>
> **3. Insert Theorem §C5a.2.6.** $[\gamma^\mu, S^{\rho\sigma}] = i(g^{\rho\mu}\gamma^\sigma - g^{\sigma\mu}\gamma^\rho)$ and $[\gamma^\nu, S^{\rho\sigma}] = i(g^{\rho\nu}\gamma^\sigma - g^{\sigma\nu}\gamma^\rho)$. Expanding all four products into eight terms:
>
> $$
> X = i\bigl[g^{\rho\nu}\gamma^\mu\gamma^\sigma - g^{\sigma\nu}\gamma^\mu\gamma^\rho + g^{\rho\mu}\gamma^\sigma\gamma^\nu - g^{\sigma\mu}\gamma^\rho\gamma^\nu - g^{\rho\mu}\gamma^\nu\gamma^\sigma + g^{\sigma\mu}\gamma^\nu\gamma^\rho - g^{\rho\nu}\gamma^\sigma\gamma^\mu + g^{\sigma\nu}\gamma^\rho\gamma^\mu\bigr] .
> $$
>
> **4. Pair into commutators.** First with seventh, second with eighth, third with fifth, fourth with sixth:
>
> $$
> X = i\bigl[g^{\rho\nu}[\gamma^\mu, \gamma^\sigma] - g^{\sigma\nu}[\gamma^\mu, \gamma^\rho] + g^{\rho\mu}[\gamma^\sigma, \gamma^\nu] - g^{\sigma\mu}[\gamma^\rho, \gamma^\nu]\bigr] .
> $$
>
> **5. Back to S.** From Def. §C5a.2.3, $[\gamma^a, \gamma^b] = -4iS^{ab}$, so $X = i(-4i)[g^{\rho\nu}S^{\mu\sigma} - g^{\sigma\nu}S^{\mu\rho} + g^{\rho\mu}S^{\sigma\nu} - g^{\sigma\mu}S^{\rho\nu}] = 4[\dots]$.
>
> **6. Restore the factor and reorder.** $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4X = i(g^{\nu\rho}S^{\mu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\rho}S^{\sigma\nu} - g^{\mu\sigma}S^{\rho\nu})$; with $S^{\sigma\nu} = -S^{\nu\sigma}$, $S^{\rho\nu} = -S^{\nu\rho}$ and the symmetry of $g$ this is $i(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho})$.
>
> **What the derivation shows**
> - The Lorentz algebra of the $S$'s is a consequence of the Clifford algebra alone, through Theorem §C5a.2.6: in any dimension and signature, $\frac i4[\gamma, \gamma]$ represents the corresponding orthogonal algebra (PS: in three Euclidean dimensions $\gamma^j = i\sigma^j$ gives $S^{ij} = \frac12\varepsilon^{ijk}\sigma^k$, spin ½, PS (3.24)).
> - This is "the step that makes everything after it legitimate" (the user's notes): exponentiating six matrices gives a representation of the group, up to the global sign of [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-9|Theorem §C5a.1.9]], only if they obey its algebra. Yu's route (5.11)–(5.12) is the same computation, with $[S^{\mu\nu}, \gamma^\rho]$ in place of $[\gamma^\mu, S^{\rho\sigma}]$.
> - Used next: the Dirac representation (Def. §C5a.2.4).

^der-c5a-2-7

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-6|Theorem §C5a.2.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]]

## The Dirac representation

> [!definition] Definition §C5a.2.4: The Dirac Representation
> The **Dirac representation** is the representation of the Lorentz algebra on $\mathbb C^4$ whose generators ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-1|Def. §C3.2.1]]) are $D(\mathcal J^{\mu\nu}) = S^{\mu\nu}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-7|Theorem §C5a.2.7]]). For parameters $\omega_{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]),
>
> $$
> \Lambda_{1/2}(\omega) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}S^{\mu\nu}\Bigr), \qquad \psi \to \Lambda_{1/2}\,\psi ,
> $$
>
> and a **Dirac spinor** is a column $\psi \in \mathbb C^4$ transforming so. A **Dirac field** transforms as $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ ([[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]).
>
> *Source: PS §3.2, eq. (3.30) · PHY 513 Lecture 7, Part B ("Finite Lorentz Transformations in Dirac Representation"), Part C ("Dirac 4-Spinor") · PHY 513 Lecture 8, Cheat Sheet II · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation $\Lambda_{1/2}$", eq. (Lhalf)) · Yu §5.1, eq. (5.14)*

^def-c5a-2-4

The exponent $\omega_{\mu\nu}S^{\mu\nu}$ is linear in the six parameters; $\Lambda_{1/2}$ depends on them nonlinearly (Lecture 7). $\Lambda_{1/2}^{-1}(\omega) = \Lambda_{1/2}(-\omega)$ (Yu (5.16)). As a function of the group element $\Lambda = e^\omega$ rather than of $\omega$, $\Lambda_{1/2}$ is fixed only up to sign (Theorem §C5a.2.9). A quantum Dirac field is an operator-valued distribution; the law then holds after smearing, as for every field ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]]).

> [!theorem] Theorem §C5a.2.8: The Generators in the Chiral Basis
> In the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), with $\Sigma^k = \operatorname{diag}(\sigma^k, \sigma^k)$,
>
> $$
> S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k = \frac12\varepsilon^{ijk}\begin{pmatrix}\sigma^k&0\\0&\sigma^k\end{pmatrix}, \qquad S^{0i} = -\frac i2\begin{pmatrix}\sigma^i&0\\0&-\sigma^i\end{pmatrix}, \qquad S^{\mu\nu} = \frac i4\begin{pmatrix}\sigma^\mu\bar\sigma^\nu - \sigma^\nu\bar\sigma^\mu & 0\\0 & \bar\sigma^\mu\sigma^\nu - \bar\sigma^\nu\sigma^\mu\end{pmatrix} ,
> $$
>
> so the rotation and boost generators ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]) are $\mathbf J = \frac12\boldsymbol\Sigma$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$. All six are block diagonal.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) · PHY 513 Lecture 7, Part B; Lecture 8, Cheat Sheet I · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis", eq. (Sexplicit)) · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-2-8

> [!derivation]- Derivation
> **1. General block form.** By Theorem §C5a.2.2, $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$; subtracting the same with $\mu \leftrightarrow \nu$ and multiplying by $\frac i4$ gives the third formula.
>
> **2. Rotations.** For spatial $i, j$: $\sigma^i\bar\sigma^j - \sigma^j\bar\sigma^i = -\sigma^i\sigma^j + \sigma^j\sigma^i = -[\sigma^i, \sigma^j] = -2i\varepsilon^{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 2), and the lower block $\bar\sigma^i\sigma^j - \bar\sigma^j\sigma^i = -[\sigma^i, \sigma^j]$ is the same. Times $\frac i4$: $\frac i4(-2i)\varepsilon^{ijk}\sigma^k = \frac12\varepsilon^{ijk}\sigma^k$ in both blocks.
>
> **3. Boosts.** Upper block of $S^{0i}$: $\sigma^0\bar\sigma^i - \sigma^i\bar\sigma^0 = -\sigma^i - \sigma^i = -2\sigma^i$, times $\frac i4$: $-\frac i2\sigma^i$. Lower block: $\bar\sigma^0\sigma^i - \bar\sigma^i\sigma^0 = \sigma^i + \sigma^i = 2\sigma^i$, times $\frac i4$: $+\frac i2\sigma^i = -\frac i2(-\sigma^i)$.
>
> **4. J and K.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], $J_k = \frac12\varepsilon_{kij}S^{ij} = \frac12\varepsilon_{kij}\cdot\frac12\varepsilon_{ijl}\Sigma^l = \frac14\cdot2\delta_{kl}\Sigma^l = \frac12\Sigma^k$, using $\varepsilon_{kij}\varepsilon_{lij} = 2\delta_{kl}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and $\varepsilon_{ijl} = \varepsilon_{lij}$; and $K_i = S^{0i}$.
>
> **What the derivation shows**
> - The rotation generators are spin ½ twice over, $\frac12\boldsymbol\sigma$ in each block; the boost generators are $\mp\frac i2\boldsymbol\sigma$, opposite in the two blocks: exactly the two rows of [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-6|Theorem §C3.2.6]], stacked.
> - The factor $\frac12$ in $S^{ij}$ is what makes a $2\pi$ rotation $-1$ (Theorem §C5a.2.9; [[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-4|Remark: Why half the angle]]).

^der-c5a-2-8

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-2|Theorem §C5a.2.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

> [!theorem] Theorem §C5a.2.9: The Dirac Representation Is (½, 0) ⊕ (0, ½)
> 1. In the chiral basis $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-1|Def. §C3.2.1]]) are $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, $\mathbf J_- = \frac12\operatorname{diag}(0, \boldsymbol\sigma)$: the upper half is the representation $(\frac12, 0)$, the lower $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-2|Def. §C3.2.2]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-6|Theorem §C3.2.6]]), and with the Weyl matrices of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]]
>
> $$
> \Lambda_{1/2}(\omega) = \begin{pmatrix}\Lambda_L(\omega) & 0\\ 0 & \Lambda_R(\omega)\end{pmatrix} = \begin{pmatrix} e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma} & 0\\ 0 & e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}\end{pmatrix} .
> $$
>
> 2. $\lambda \mapsto \operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ is a representation of $SL(2, \mathbb C)$ with $\Lambda_{1/2}(\omega)$ the image of $\Lambda_L(\omega)$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-9|Theorem §C5a.1.9]]); on $SO^+(1,3)$, $\Lambda_{1/2}$ is defined up to sign, a two-valued representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]]), and a rotation by $2\pi$ gives $-\mathbb 1_4$.
> 3. Rotation by $\theta$ about $z$: $\Lambda_{1/2} = \operatorname{diag}(e^{-i\theta\sigma^3/2}, e^{-i\theta\sigma^3/2})$. Boost of rapidity $\eta$ along $x$: $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\sigma^1/2}, e^{+\eta\sigma^1/2})$, $e^{\mp\eta\sigma^1/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\sigma^1$.
>
> *Source: PS §3.2, eqs. (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts": "4 dim. Dirac spinor representation is reducible") · PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$ …") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation", Examples 1–2, eq. (spinorboost); checked numerically there), §8.2 (Derivations "How the two halves transform", "… related by conjugation": "Their labels") · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit")*

^thm-c5a-2-9

> [!derivation]- Derivation
> **1. The labels.** From Theorem §C5a.2.8, $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K) = \frac12\bigl(\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm i(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr) = \frac14\bigl(\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm \operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr)$, which is $\frac12\operatorname{diag}(\boldsymbol\sigma, 0)$ for the upper sign and $\frac12\operatorname{diag}(0, \boldsymbol\sigma)$ for the lower. On the upper half $\mathbf J_+ = \frac12\boldsymbol\sigma$, $\mathbf J_- = 0$: by [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-2|Def. §C3.2.2]] this is $(\frac12, 0)$; the lower half is $(0, \frac12)$.
>
> **2. The exponent.** $-\frac i2\omega_{\mu\nu}S^{\mu\nu} = -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$ (the regrouping of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], linear in the generators). Inserting Theorem §C5a.2.8: $-i\boldsymbol\theta\cdot\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) - i\boldsymbol\eta\cdot(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma) = \operatorname{diag}\bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma,\ -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\bigr)$, since $-i\cdot(-\frac i2) = -\frac12$.
>
> **3. Exponentiate.** Powers of a block-diagonal matrix are block diagonal with the powers of the blocks, so $\exp\operatorname{diag}(A, B) = \operatorname{diag}(e^A, e^B)$. The blocks are $\Lambda_L(\omega)$ and $\Lambda_R(\omega)$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]]).
>
> **4. SL(2, C).** $\lambda \mapsto \lambda$ and $\lambda \mapsto (\lambda^\dagger)^{-1}$ are representations (Derivation §C5a.1.9, step 1), hence so is their direct sum; at $\lambda = \Lambda_L(\omega)$ it gives $\operatorname{diag}(\Lambda_L, (\Lambda_L^\dagger)^{-1}) = \operatorname{diag}(\Lambda_L, \Lambda_R) = \Lambda_{1/2}(\omega)$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-2|Theorem §C5a.1.2]], 2). This is [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-9|Theorem §C5a.1.9]] for $(\frac12, 0)\oplus(0, \frac12)$; $j_+ + j_- = \frac12$, so the image of $-\mathbb 1$ is $-\mathbb 1_4$ and $\Lambda_{1/2}$ is two-valued on $SO^+(1,3)$.
>
> **5. Rotation about z.** $\omega_{12} = -\omega_{21} = \theta$ gives $\boldsymbol\theta = \theta\hat{\mathbf z}$, $\boldsymbol\eta = 0$ (the two terms $\frac12(\omega_{12}S^{12} + \omega_{21}S^{21}) = \theta S^{12}$), so both blocks are $e^{-i\theta\sigma^3/2} = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$. At $\theta = 2\pi$ each is $-\mathbb 1$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]), while the vector-representation matrix of the same $\omega$ is $\exp(-2\pi i\,\mathcal J^{12}) = \mathbb 1$ (the eigenvalues of $\mathcal J^{12}$ are $0, 0, \pm1$). ⚑ By-product: the same physical rotation multiplies the four spinor components by $e^{-i\theta/2}, e^{i\theta/2}, e^{-i\theta/2}, e^{i\theta/2}$: no component is left alone, unlike $V^0$, $V^3$ of a vector.
>
> **6. Boost along x.** $\omega_{01} = -\omega_{10} = \eta$ gives $\boldsymbol\eta = \eta\hat{\mathbf x}$, $\boldsymbol\theta = 0$, so the blocks are $e^{\mp\eta\sigma^1/2}$. Since $(\sigma^1)^2 = \mathbb 1$, the even terms of the series sum to $\cosh\frac\eta2\,\mathbb 1$ and the odd ones to $\mp\sinh\frac\eta2\,\sigma^1$. No $i$ appears: the blocks are Hermitian, not unitary, and stretched in opposite senses. The same $\omega$ gives in the vector representation $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\eta$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\eta$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **What the derivation shows**
> - The Dirac representation is reducible: the halves never mix under rotations or boosts. If the lower half vanishes in one frame, it vanishes in all, which could never happen for a four-vector.
> - Each half is irreducible and the two are inequivalent ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-4|Theorem §C3.2.4]]; the user's notes argue directly: an intertwiner commutes with $\frac12\boldsymbol\sigma$, so is $c\mathbb 1$ by Schur, and cannot turn $-\frac i2\boldsymbol\sigma$ into $+\frac i2\boldsymbol\sigma$); they are complex conjugates of each other up to basis ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-11|Theorem §C5a.1.11]]).
> - Half the angle and half the rapidity appear in every spinor matrix ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-4|Remark: Why half the angle]]).
> - Used next: boosting rest-frame spinors ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-5|Theorem §C5a.5.5]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-8|Theorem §C5a.5.8]]); the Weyl form of the Dirac equation ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]]).

^der-c5a-2-9

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^def-c3-2-2|Def. §C3.2.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

> [!remark] Remark: One transformation, two matrices
> One Lorentz transformation is six numbers $\omega_{\mu\nu}$; the vector and the Dirac representation exponentiate them with different generators:
>
> | | four-vector $A^\mu$ | Dirac spinor $\psi_a$ |
> |---|---|---|
> | components label | a direction, $\mu = 0, \dots, 3$ | a component of $\mathbb C^4$; no direction |
> | generators | $(\mathcal J^{\mu\nu})^\alpha{}_\beta$ | $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, same algebra |
> | matrix | $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, real | $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$, complex |
> | rotation by $\theta$ about $z$ | $\cos\theta$, $\sin\theta$ in the $(1, 2)$ block | phases $e^{\mp i\theta/2}$: half the angle |
> | boost by $\eta$ along $x$ | $\cosh\eta$, $\sinh\eta$ | $\cosh\frac\eta2 \mp \sigma^1\sinh\frac\eta2$, opposite in the halves |
> | invariant form | $g$: $\Lambda^{\mathsf T}g\Lambda = g$ | $\gamma^0$: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]) |
> | rotation by $2\pi$ | $+\mathbb 1$ | $-\mathbb 1$ |
> | fixed by $\Lambda$? | yes | up to sign: a representation of $SL(2, \mathbb C)$ |
>
> Both matrices are $4\times4$ for unrelated reasons: $\Lambda$ because spacetime has four dimensions, $\Lambda_{1/2}$ because the Clifford algebra needs four components (Theorem §C5a.2.4). Relations such as $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ hold only for a matched pair built from the same $\omega$ (checked numerically in the user's notes, matched and mismatched). This is why the lecture calls $\psi$ a four-component *column*, not a four-vector.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation": "One transformation, two representations"; Derivation "From six numbers to two matrices"; Principle "Transforming as a vector and as a spinor, side by side"; paragraph "Same dimension, different representation")*

^rem-c5a-2-3

> [!remark] Remark: Why half the angle
> The rotation generator $\mathcal J^{12}$ of the vector representation has eigenvalues $\pm1$ (on $x \pm iy$) and $0$ twice (on $t$, $z$); the spinor generator $S^{12} = \frac12\Sigma^3$ has $\pm\frac12$. For boosts, $\mathcal J^{01}$ has $\pm i$ and $S^{01}$ has $\pm\frac i2$. Exponentiating $\theta$ times an eigenvalue $s$ gives the phase $e^{-is\theta}$: spin $1$ turns with the full angle, spin $\frac12$ with half of it, and the $2\pi$ sign is $e^{-i\pi} = -1$. The factor $\frac12$ in $S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k$ is therefore essential; the user's notes record that the handwritten lecture notes omit it, while the Lecture 8 slides have it.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Why 'half'"), Caution "A missing ½ in the handwritten notes" · PHY 513 Lecture 8, Cheat Sheet I*

^rem-c5a-2-4

> [!caution] Caution: The upper components are not the particle
> The Lecture 7 slides preview the four components as "spin up/down for particle/anti-particle" (and the handwritten notes attach "particle" to $\xi$, "antiparticle" to $\eta$). As a count this is right: a Dirac field describes two spin states of a particle and two of its antiparticle. As an assignment of components it is wrong in the chiral basis: the halves are the left- and right-handed Weyl spinors, and a particle at rest has *equal* halves, $u \propto (\xi, \xi)$ ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-3|Theorem §C5a.5.3]]; PS (3.47)). The heuristic belongs to the Dirac basis (Example §C5a.2.1), where nonrelativistic particles live mostly in the upper components.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Caution "'$\xi$ is the particle, $\eta$ the antiparticle'") · PHY 513 Lecture 7, Part B*

^cau-c5a-2-2

> [!theorem] Theorem §C5a.2.10: The Dirac Representation Is Not the Vector Representation
> The Dirac representation ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]) and the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) are both four-dimensional, but they are inequivalent ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-4|Def. §C3.1.4]]); these are the two tests of [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^rem-c3-2-3|§C3.2, Remark: Sums versus products]]:
> 1. on the Dirac representation the Casimirs ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-4|Theorem §C3.2.4]]) are $\mathbf J_+^2 = \operatorname{diag}(\frac34, \frac34, 0, 0)$ and $\mathbf J_-^2 = \operatorname{diag}(0, 0, \frac34, \frac34)$, on the vector representation $\mathbf J_\pm^2 = \frac34\mathbb 1$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-7|Theorem §C3.2.7]]);
> 2. a rotation by $2\pi$ is $-\mathbb 1$ on Dirac spinors and $+\mathbb 1$ on four-vectors;
> 3. under rotations the Dirac spinor is spin $\frac12\oplus\frac12$, the vector spin $0\oplus1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Same dimension, different representation"), §8.2 (Derivation "… related by conjugation", paragraph "Why the Dirac spinor is not (½, ½)"; checked numerically there) · PHY 513 Lecture 7, Part B ("Unlike a 4-vector under rotation: spin-0 (time) and spin-1 (space)")*

^thm-c5a-2-10

> [!derivation]- Derivation
> **1. Casimirs.** By Theorem §C5a.2.9, $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, so $\mathbf J_+^2 = \frac14\operatorname{diag}(\boldsymbol\sigma\cdot\boldsymbol\sigma, 0) = \frac14\operatorname{diag}(3\cdot\mathbb 1, 0)$ ($\sigma_k^2 = \mathbb 1$ for each $k$); likewise $\mathbf J_-^2$. On the vector representation both are $\frac34\mathbb 1$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-7|Theorem §C3.2.7]]). An equivalence $D_{\rm Dirac} = UD_{\rm vec}U^{-1}$ would give $\mathbf J_+^2|_{\rm Dirac} = U\frac34\mathbb 1U^{-1} = \frac34\mathbb 1$: false.
>
> **2. 2π rotation.** Theorem §C5a.2.9, step 5: $-\mathbb 1_4$ against $+\mathbb 1_4$; an equivalence maps $+\mathbb 1$ to $+\mathbb 1$.
>
> **3. Rotation content.** $\mathbf J = \frac12\boldsymbol\Sigma$ is spin ½ on each block; on the vector, $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$ (Theorem §C3.2.7): spin $0$ on $v^0$, spin $1$ on $\mathbf v$.
>
> **What the derivation shows**
> - In the Dirac spinor no component feels both copies $\mathbf J_\pm$ (a direct sum, $2 + 2$); in the vector every component feels both (a product, $2\times2$). The equality of dimensions is a coincidence of four dimensions ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-6|Remark: What each Dirac index labels]]).

^der-c5a-2-10

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-7|Theorem §C3.2.7]]

> [!theorem] Theorem §C5a.2.11: Adjoints of the Generators
> 1. For the spinor generators ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]) of Hermitian Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]), $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$. In particular $S^{ij}$ commutes with $\gamma^0$ and is Hermitian; $S^{0i}$ anticommutes with $\gamma^0$ and is anti-Hermitian.
> 2. $\Lambda_{1/2}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]) is unitary for rotations and Hermitian positive (not unitary) for pure boosts, the spin-½ case of [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", "Consequence for the generators"; Derivation "What replaces unitarity", Step 1; Caution "Spinor boosts are not unitary") · PHY 513 Lecture 8, Part B (slides "The Hermitean Conjugate Spinor", "The Dirac Conjugate Spinor") · PS §3.2, p. 41 ("The boost generators $S^{0i}$ are not Hermitian") and p. 43*

^thm-c5a-2-11

> [!derivation]- Derivation
> **1. Adjoint of a commutator.** $[A, B]^\dagger = (AB - BA)^\dagger = B^\dagger A^\dagger - A^\dagger B^\dagger = [B^\dagger, A^\dagger]$, and the $i$ is conjugated: $S^{\mu\nu\dagger} = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$.
>
> **2. Insert Hermiticity.** With $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ (Theorem §C5a.2.3): $[\gamma^0\gamma^\nu\gamma^0, \gamma^0\gamma^\mu\gamma^0] = \gamma^0\gamma^\nu\gamma^0\gamma^0\gamma^\mu\gamma^0 - \gamma^0\gamma^\mu\gamma^0\gamma^0\gamma^\nu\gamma^0 = \gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0$, using $(\gamma^0)^2 = \mathbb 1$ in the middle of each product. So $S^{\mu\nu\dagger} = -\frac i4\gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0 = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu]\gamma^0 = \gamma^0S^{\mu\nu}\gamma^0$.
>
> **3. The two cases.** $S^{ij} = \frac i2\gamma^i\gamma^j$ ($i \ne j$): moving $\gamma^0$ through two $\gamma$'s gives $(-1)^2$, so $\gamma^0S^{ij} = S^{ij}\gamma^0$ and $S^{ij\dagger} = S^{ij}(\gamma^0)^2 = S^{ij}$. $S^{0i} = \frac i2\gamma^0\gamma^i$: $\gamma^0$ anticommutes with $\gamma^i$ and commutes with itself, so $\gamma^0S^{0i} = -S^{0i}\gamma^0$ and $S^{0i\dagger} = -S^{0i}$. (In the chiral basis this is visible in Theorem §C5a.2.8: $\frac12\Sigma^k$ Hermitian, $-\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$ anti-Hermitian.)
>
> **4. Part 2.** For a rotation $\Lambda_{1/2} = e^{-i\boldsymbol\theta\cdot\mathbf J}$ with $\mathbf J$ Hermitian: $(e^{-iX})^\dagger = e^{iX} = (e^{-iX})^{-1}$, unitary. For a pure boost $\Lambda_{1/2} = e^{-i\boldsymbol\eta\cdot\mathbf K}$ and $-i\mathbf K$ is Hermitian ($\mathbf K$ anti-Hermitian), so $\Lambda_{1/2}$ is the exponential of a Hermitian matrix: Hermitian with positive eigenvalues, unitary only for $\boldsymbol\eta = 0$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]]).
>
> **What the derivation shows**
> - $\psi^\dagger\psi$ is not invariant under boosts. What replaces unitarity is that $\gamma^0$ turns the adjoint into the inverse, $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$, so $\bar\psi = \psi^\dagger\gamma^0$ transforms with $\Lambda_{1/2}^{-1}$: [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]].
> - That is the price of Theorem §C3.2.12 for spin ½; the lecture: "$\psi$ is not a wavefunction; it is a classical field" (PS p. 41), so non-unitarity is harmless.

^der-c5a-2-11

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]]

## γ^μ carries a vector index

> [!theorem] Theorem §C5a.2.12: The Dirac Matrices Are an Invariant Vector of Matrices
> For $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]) and $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) built from the same $\omega$:
> 1. $\Lambda_{1/2}^{-1}\,\gamma^\mu\,\Lambda_{1/2} = \Lambda^\mu{}_\nu\,\gamma^\nu$;
> 2. $\Lambda_{1/2}^{-1}S^{\mu\nu}\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma S^{\rho\sigma}$, $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = (\Lambda^{-1})^\nu{}_\mu\gamma_\nu$, and $\Lambda_{1/2}^{-1}\mathbb 1\Lambda_{1/2} = \mathbb 1$;
> 3. in the chiral basis, with the Weyl matrices and $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]] and [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]], $\Lambda_L^{-1}\sigma^\mu\Lambda_R = \Lambda^\mu{}_\nu\sigma^\nu$ and $\Lambda_R^{-1}\bar\sigma^\mu\Lambda_L = \Lambda^\mu{}_\nu\bar\sigma^\nu$.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The covariance of $\gamma^\mu$: finite transformations", eq. (gammacov), with its second proof and corollaries) · Yu §5.1, eqs. (5.17)–(5.31) · the user's pre-course notes, §5.1, eq. (gamma-vector)*

^thm-c5a-2-12

> [!derivation]- Derivation
> Let $A = -\frac i2\omega_{\rho\sigma}S^{\rho\sigma}$, so $\Lambda_{1/2} = e^A$, and recall $-\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu = \omega^\mu{}_\nu$, so $\Lambda = e^{\omega}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]]).
>
> **1. The infinitesimal statement.** By Theorem §C5a.2.6, $[\gamma^\mu, A] = -\frac i2\omega_{\rho\sigma}[\gamma^\mu, S^{\rho\sigma}] = -\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\nu\gamma^\nu$.
>
> **2. Two curves.** For $t \in [0, 1]$ put $F^\mu(t) = e^{-tA}\gamma^\mu e^{tA}$ and $G^\mu(t) = (e^{t\omega})^\mu{}_\nu\gamma^\nu$, four matrices each; $F^\mu(0) = G^\mu(0) = \gamma^\mu$.
>
> **3. The same linear equation.** $\frac{d}{dt}F^\mu = e^{-tA}(-A\gamma^\mu + \gamma^\mu A)e^{tA} = e^{-tA}[\gamma^\mu, A]e^{tA} = \omega^\mu{}_\nu e^{-tA}\gamma^\nu e^{tA} = \omega^\mu{}_\nu F^\nu$, by step 1 (the numbers $\omega^\mu{}_\nu$ pass through $e^{\pm tA}$). And $\frac{d}{dt}G^\mu = (\omega e^{t\omega})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\kappa G^\kappa$.
>
> **4. Uniqueness.** The difference $D^\mu = F^\mu - G^\mu$ obeys $\dot D^\mu = \omega^\mu{}_\nu D^\nu$, $D^\mu(0) = 0$. Then $\frac{d}{dt}\bigl[(e^{-t\omega})^\kappa{}_\mu D^\mu(t)\bigr] = -(e^{-t\omega}\omega)^\kappa{}_\mu D^\mu + (e^{-t\omega})^\kappa{}_\mu\omega^\mu{}_\nu D^\nu = 0$ ($\omega$ commutes with $e^{-t\omega}$), so $(e^{-t\omega})^\kappa{}_\mu D^\mu(t) = 0$ for all $t$; multiplying by $e^{t\omega}$, $D \equiv 0$. At $t = 1$: $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$.
>
> **5. Part 2.** $\Lambda_{1/2}^{-1}[\gamma^\mu, \gamma^\nu]\Lambda_{1/2} = [\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}, \Lambda_{1/2}^{-1}\gamma^\nu\Lambda_{1/2}]$ (insert $\Lambda_{1/2}\Lambda_{1/2}^{-1}$ between the factors) $= \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma[\gamma^\rho, \gamma^\sigma]$; times $\frac i4$ this is the law for $S$. For the lower index, $\gamma_\mu = g_{\mu\nu}\gamma^\nu$ gives $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = g_{\mu\nu}\Lambda^\nu{}_\rho g^{\rho\kappa}\gamma_\kappa$, and $\Lambda^{\mathsf T}g\Lambda = g$ means $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\kappa{}_\mu = g^{\kappa\rho}\Lambda^\nu{}_\rho g_{\nu\mu}$, which is the coefficient found.
>
> **6. Part 3.** In the chiral basis $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ (Theorem §C5a.2.9), and block multiplication gives $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \begin{pmatrix}0 & \Lambda_L^{-1}\sigma^\mu\Lambda_R\\ \Lambda_R^{-1}\bar\sigma^\mu\Lambda_L & 0\end{pmatrix}$; compare the blocks of part 1. Since $\Lambda_L^{-1} = \Lambda_R^\dagger$ and $\Lambda_R^{-1} = \Lambda_L^\dagger$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-2|Theorem §C5a.1.2]], 2), these are the invariance statements of [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-7|Theorem §C5a.1.7]], 2, obtained here independently.
>
> **What the derivation shows**
> - Transforming the two spinor indices of $\gamma^\mu$ is the same as transforming its vector index: $\gamma^\mu$ is an invariant tensor with one vector slot and two spinor slots, as $g_{\mu\nu}$ is with two vector slots. "Take the vector index on $\gamma^\mu$ seriously" (PS): $\gamma^\mu\partial_\mu$ is a Lorentz-invariant operator on spinors ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]]), and $\bar\psi\gamma^\mu\psi$ a vector ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]]).
> - Part 2 for $S$ is the general law "the generators transform as a tensor" ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-1|Theorem §C3.2.1]]) for the Dirac representation.
> - Only the matched pair works: $\Lambda$ and $\Lambda_{1/2}$ from the same six numbers. The two-valuedness of $\Lambda_{1/2}$ is invisible here, since $\pm\Lambda_{1/2}$ give the same conjugation.

^der-c5a-2-12

> [!derivation]- Derivation (second route: the nested-commutator series)
> **1. The series.** For matrices $A$, $B$ define $[B, A]_{(0)} = B$, $[B, A]_{(n+1)} = [[B, A]_{(n)}, A]$. The function $f(t) = e^{-tA}Be^{tA}$ satisfies $f'(t) = e^{-tA}[B, A]e^{tA}$ (as in step 3 above), and by induction $f^{(n)}(t) = e^{-tA}[B, A]_{(n)}e^{tA}$; $f$ is entire in $t$ (products of exponential series), so its Taylor series at $0$ converges at $t = 1$: $e^{-A}Be^A = \sum_{n\ge0}\frac1{n!}[B, A]_{(n)}$ (Yu (5.23), proved there by the binomial rearrangement (5.18)–(5.22)).
>
> **2. Iterate step 1 of the first route.** $[\gamma^\mu, A]_{(1)} = \omega^\mu{}_\nu\gamma^\nu$; if $[\gamma^\mu, A]_{(n)} = (\omega^n)^\mu{}_\nu\gamma^\nu$, then $[\gamma^\mu, A]_{(n+1)} = (\omega^n)^\mu{}_\nu[\gamma^\nu, A] = (\omega^n)^\mu{}_\nu\omega^\nu{}_\kappa\gamma^\kappa = (\omega^{n+1})^\mu{}_\kappa\gamma^\kappa$.
>
> **3. Sum.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \sum_n\frac1{n!}(\omega^n)^\mu{}_\nu\gamma^\nu = (e^\omega)^\mu{}_\nu\gamma^\nu = \Lambda^\mu{}_\nu\gamma^\nu$ (Yu (5.25)–(5.27)).
>
> *What this route shows:* the finite law is the infinitesimal one summed to all orders, term by term; the first route reaches it through uniqueness for a linear differential equation instead.

^der-c5a-2-12b

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-6|Theorem §C5a.2.6]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-2|Theorem §C5a.1.2]]

> [!remark] Remark: The lecture's form of the covariance
> Lecture 8 writes $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$, the infinitesimal version $(1 - \frac i2\omega S)\gamma^\mu(1 + \frac i2\omega S) = (1 + \frac i2\omega\mathcal J)^\mu{}_\nu\gamma^\nu$, and then $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$. All three are Theorem §C5a.2.12 with $\omega \to -\omega$ ($\Lambda_{1/2}(-\omega) = \Lambda_{1/2}^{-1}$, $e^{-\omega} = \Lambda^{-1}$), and Peskin–Schroeder's infinitesimal form is the same with the opposite sign of $\omega$. The last form carries the slide's message: "$\gamma^\nu$ are just numbers. They do not transform!" — transforming the vector index and both spinor indices at once returns the same matrices. That is what "invariant tensor" means, and why $\gamma^\nu\psi$ transforms as a spinor and a vector at once, $\gamma^\nu\psi \to \Lambda^\nu{}_\mu\Lambda_{1/2}(\gamma^\mu\psi)$.
>
> *Source: PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · PS §3.2, p. 42 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"), §8.1 (Definition "What 'transforms like a spinor' means")*

^rem-c5a-2-5

## γ⁵ and the Weyl halves

> [!definition] Definition §C5a.2.5: The Matrix γ⁵
>
> $$
> \gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3 ,
> $$
>
> with $\gamma^\mu$ the Dirac matrices of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]. The "5" is a label, not a Lorentz index: there is no $\gamma_5$ obtained by lowering.
>
> *Source: PS §3.4, eq. (3.68) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$", eq. (gamma5)) · PHY 513, Problem Set 5, Problem 5 (statement: "there is no way to lower a '5' index") · Yu §5.1, eq. (5.32)*

^def-c5a-2-5

Yu writes $\gamma_5 \equiv \gamma^5$ for the same matrix. Its totally antisymmetric form $\gamma^5 = -\frac i{4!}\varepsilon_{\mu\nu\rho\sigma}\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma$ (with $\varepsilon^{0123} = +1$) and the duality identities are [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-5|Theorem §C5a.7.5]]–[[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-7|§C5a.7.7]].

> [!theorem] Theorem §C5a.2.13: Algebraic Properties of γ⁵
>
> $$
> (\gamma^5)^2 = \mathbb 1, \qquad \gamma^{5\dagger} = \gamma^5, \qquad \{\gamma^5, \gamma^\mu\} = 0, \qquad \operatorname{tr}\gamma^5 = 0 ,
> $$
>
> for $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]] (Hermiticity in a basis with $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]).
>
> *Source: PHY 513, Problem Set 5, Problem 5(a)–(b) (as the user wrote it) · PS §3.4, eqs. (3.69)–(3.71) · the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$" and its proof) · Yu §5.1, eqs. (5.37)–(5.40)*

^thm-c5a-2-13

> [!derivation]- Derivation
> **1. Anticommutation.** Move $\gamma^\mu$ from the right of $\gamma^0\gamma^1\gamma^2\gamma^3$ to the left, one factor at a time. It passes three factors with index $\ne \mu$, each giving $-1$ (Theorem §C5a.2.1), and the one equal to $\mu$, with which it commutes: $\gamma^5\gamma^\mu = (-1)^3\gamma^\mu\gamma^5$. (The user's Problem Set 5 solution does the same move with $\gamma^a\gamma^\mu = 2g^{a\mu} - \gamma^\mu\gamma^a$ at each step and shows that the four surviving metric terms add up to $-2\gamma^\mu\gamma^5$.)
>
> **2. Hermiticity.** $(ABCD)^\dagger = D^\dagger C^\dagger B^\dagger A^\dagger$ and $\gamma^{0\dagger} = \gamma^0$, $\gamma^{i\dagger} = -\gamma^i$ (Theorem §C5a.2.3): $\gamma^{5\dagger} = -i\gamma^{3\dagger}\gamma^{2\dagger}\gamma^{1\dagger}\gamma^{0\dagger} = -i(-1)^3\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^3\gamma^2\gamma^1\gamma^0$. Reversing four distinct anticommuting factors takes $3 + 2 + 1 = 6$ swaps (three to bring $\gamma^0$ to the front, two for $\gamma^1$, one for $\gamma^2$), so $\gamma^3\gamma^2\gamma^1\gamma^0 = (-1)^6\gamma^0\gamma^1\gamma^2\gamma^3$ and $\gamma^{5\dagger} = \gamma^5$.
>
> **3. Square.** Using the reversed form of step 2 for the second factor, $(\gamma^5)^2 = \gamma^5\gamma^{5\dagger} = i\cdot i\,\gamma^0\gamma^1\gamma^2\gamma^3\gamma^3\gamma^2\gamma^1\gamma^0$. The middle pairs collapse one after another: $(\gamma^3)^2 = -\mathbb 1$, $(\gamma^2)^2 = -\mathbb 1$, $(\gamma^1)^2 = -\mathbb 1$, $(\gamma^0)^2 = \mathbb 1$, giving $i^2(-1)^3 = 1$.
>
> **4. Trace.** $\gamma^5$ is $i$ times the product $\Gamma_{\{0,1,2,3\}}$, traceless by [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], 2.
>
> **What the derivation shows**
> - $\gamma^5$ is a Hermitian involution, so its eigenvalues are $\pm1$; tracelessness makes each occur twice in four dimensions.
> - The factor $i$ in the definition is chosen to make $\gamma^5$ Hermitian with square $+1$.
> - Used next: Theorem §C5a.2.14; the chirality projectors $\frac12(\mathbb 1 \mp \gamma^5)$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-3|Def. §C5a.4.3]]); traces with $\gamma^5$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-4|Theorem §C5a.7.4]]).

^der-c5a-2-13

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]

> [!theorem] Theorem §C5a.2.14: γ⁵ Is Lorentz Invariant and Separates the Weyl Halves
> 1. $[\gamma^5, S^{\mu\nu}] = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]), hence $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$: $\gamma^5$ is a Lorentz scalar.
> 2. In the chiral basis $\gamma^5 = \begin{pmatrix}-\mathbb 1 & 0\\ 0 & \mathbb 1\end{pmatrix}$.
> 3. On the Dirac representation $\gamma^5 = \frac43\bigl(\mathbf J_-^2 - \mathbf J_+^2\bigr)$, with the Casimirs $\mathbf J_\pm^2$ of [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-4|Theorem §C3.2.4]], equivalently $\mathbf J\cdot\mathbf K = \frac{3i}4\gamma^5$.
> 4. In every basis, the eigenspaces $\gamma^5 = -1$ and $\gamma^5 = +1$ are two-dimensional, invariant under $\Lambda_{1/2}$, and carry $(\frac12, 0)$ and $(0, \frac12)$ (Theorem §C5a.2.9): left-handed spinors ([[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]]) are the $\gamma^5 = -1$ spinors.
>
> *Source: PS §3.4, p. 50 ("$[\gamma^5, S^{\mu\nu}] = 0$. Thus the Dirac representation must be reducible …"; eq. (3.72)) · Yu §5.1, eq. (5.36) ($\gamma^5$ a Lorentz scalar), §5.2, eq. (5.73) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$": "$\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$") · the user's pre-course notes, §5.2 · part 3 written out here*

^thm-c5a-2-14

> [!derivation]- Derivation
> **1. γ⁵ commutes with products of two γ's.** $\gamma^5\gamma^\mu\gamma^\nu = -\gamma^\mu\gamma^5\gamma^\nu = \gamma^\mu\gamma^\nu\gamma^5$ (Theorem §C5a.2.13, twice). Hence $\gamma^5$ commutes with $[\gamma^\mu, \gamma^\nu]$ and with $S^{\mu\nu}$, with every power of $A = -\frac i2\omega_{\mu\nu}S^{\mu\nu}$, and with $\Lambda_{1/2} = e^A$: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$.
>
> **2. Chiral form.** From Derivation §C5a.2.2, $\gamma^0\gamma^1 = \operatorname{diag}(-\sigma^1, \sigma^1)$, and $\gamma^2\gamma^3 = \operatorname{diag}(-\sigma^2\sigma^3, -\sigma^2\sigma^3) = \operatorname{diag}(-i\sigma^1, -i\sigma^1)$ ($\sigma^2\sigma^3 = i\sigma^1$, [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]). The product is $\operatorname{diag}(-\sigma^1(-i\sigma^1), \sigma^1(-i\sigma^1)) = \operatorname{diag}(i\mathbb 1, -i\mathbb 1)$, and times $i$: $\operatorname{diag}(-\mathbb 1, \mathbb 1)$ (Yu (5.73)).
>
> **3. J·K.** With Theorem §C5a.2.8, $J_kK_k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)\cdot(-\frac i2)\operatorname{diag}(\sigma^k, -\sigma^k) = -\frac i4\operatorname{diag}(\mathbb 1, -\mathbb 1)$ for each $k$ ($(\sigma^k)^2 = \mathbb 1$); summing over $k = 1, 2, 3$: $\mathbf J\cdot\mathbf K = -\frac{3i}4\operatorname{diag}(\mathbb 1, -\mathbb 1) = \frac{3i}4\gamma^5$. Here $J_k$ and $K_k$ commute (both block diagonal with commuting blocks), so $\mathbf J_\pm^2 = \frac14(\mathbf J^2 - \mathbf K^2 \pm 2i\mathbf J\cdot\mathbf K)$ and $\mathbf J_+^2 - \mathbf J_-^2 = i\mathbf J\cdot\mathbf K = -\frac34\gamma^5$. Both sides of part 3 are built from $\gamma$'s by the same formula in every basis, so a change of basis $\gamma \to U\gamma U^{-1}$ (Theorem §C5a.2.5) conjugates both, and the identity holds in every basis. ⚑ By-product: $\gamma^5$ is a function of the two Casimirs of the Lorentz algebra; that alone explains part 1.
>
> **4. Eigenspaces.** In the chiral basis the $\gamma^5 = -1$ eigenspace is the upper half, $(\frac12, 0)$, and $\gamma^5 = +1$ the lower, $(0, \frac12)$ (part 2, Theorem §C5a.2.9). In another basis, $\gamma'^\mu = U\gamma^\mu U^{-1}$ gives $\gamma'^5 = U\gamma^5U^{-1}$, $S' = USU^{-1}$, and the eigenspaces are the images under $U$, with the same generators. They are invariant under $\Lambda_{1/2}$ by part 1: an operator commuting with a representation has invariant eigenspaces (Schur's criterion, PS p. 50).
>
> **What the derivation shows**
> - The split $(\frac12, 0)\oplus(0, \frac12)$ is not an artefact of the chiral basis: it is the eigen-decomposition of the Lorentz-invariant matrix $\gamma^5$, which the chiral basis merely diagonalizes (PS footnote ‡: in another basis "the reducibility would not be manifest").
> - $\gamma^5$ commutes with $S^{\mu\nu}$ but anticommutes with $\gamma^\mu$: the Lorentz transformations preserve handedness, the vector index of $\gamma^\mu$ flips it. Under parity, which exchanges the copies ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-10|Theorem §C3.2.10]]), $\gamma^5$ changes sign (pseudoscalar; [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-2|Theorem §C5a.4.2]]).
> - Used next: chirality projectors and Weyl fields ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-3|Def. §C5a.4.3]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]]).

^der-c5a-2-14

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-2|Theorem §C5a.2.2]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!remark] Remark: What each Dirac index labels
>
> | symbol | what it is | indices |
> |---|---|---|
> | $\psi_a$ | a vector of spinor space $\mathbb C^4$ | $a$: Dirac spinor |
> | $(\gamma^\mu)_{ab}$ | a spacetime vector whose components are $4\times4$ matrices | $\mu$: spacetime; $a, b$: spinor |
> | $(S^{\mu\nu})_{ab}$ | a generator as a matrix on $\mathbb C^4$ | $\mu\nu$: generator label; $a, b$: spinor |
> | $(\Lambda_{1/2})_{ab}$ | the transformation of spinor space | $a, b$: spinor |
> | $(\gamma^0)_{ab}$ | the invariant form of the Dirac slot ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]) | $a, b$: spinor |
>
> Spinor indices are contracted by plain matrix multiplication and never moved with $g$; since $\Lambda_{1/2}$ is not unitary, not even $\psi^\dagger\psi$ is invariant. In the chiral basis the Dirac index is a pair of Weyl indices, $\psi = (\psi_a, \psi^{\dot a})$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-3|Def. §C5a.1.3]]; index positions of $\sigma^\mu$, $\bar\sigma^\mu$: [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-12|Theorem §C5a.1.12]]), and
>
> $$
> \gamma^\mu = \begin{pmatrix}0 & (\sigma^\mu)_{a\dot b}\\ (\bar\sigma^\mu)^{\dot ab} & 0\end{pmatrix}, \qquad \gamma^\mu\psi = \bigl((\sigma^\mu)_{a\dot b}\psi^{\dot b},\ (\bar\sigma^\mu)^{\dot ab}\psi_b\bigr) :
> $$
>
> $\gamma^\mu$ converts a dotted index into an undotted one and back, so it flips handedness, while $S^{\mu\nu}$, $\Lambda_{1/2}$ and $\gamma^5 = \operatorname{diag}(-1, +1)$ keep each half (figure below). That the Dirac spinor has as many components as a four-vector is a coincidence of four dimensions: in $d$ spacetime dimensions a Dirac spinor has $2^{\lfloor d/2\rfloor}$ components (32 against 10 in $d = 10$).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (table, Principle "Invariant tensors with mixed slots", paragraphs "The practical test, continued", "A coincidence of dimension") · PHY 513 Lecture 8, Part A (slide "Transformations with 4-Vectors and 4-Spinors")*

^rem-c5a-2-6

![[ph-qft-c5-2-1.svg]]
*The Dirac spinor in the chiral basis as two Weyl slots. Lorentz transformations ($S^{\mu\nu}$, $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$) and $\gamma^5$ act within each slot, so the representation is $(\frac12, 0)\oplus(0, \frac12)$ (Theorems §C5a.2.9, §C5a.2.14); $\gamma^\mu$ maps each slot to the other through $\sigma^\mu$ and $\bar\sigma^\mu$, so products of two $\gamma$'s (such as $S^{\mu\nu}$) keep the slots, and $\bar\psi = \psi^\dagger\gamma^0$ pairs each slot with the other, which is why a mass term couples them.*

> [!remark]- Connections
> - The Clifford algebra is the multiplication rule of a "square root of the metric", and the Lorentz algebra follows from it: in every dimension and signature $\frac i4[\gamma, \gamma]$ represents the orthogonal algebra, with spin ½ for rotations in three dimensions as the case $\gamma^j = i\sigma^j$ — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-4|QM Theorem §C5.1.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].
> - Pauli's theorem is the Clifford-algebra analogue of "spin ½ is unique up to basis": both follow because the generated matrix algebra is all of $M_n(\mathbb C)$, so the representation is irreducible and Schur's lemma pins the intertwiner — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]].
> - The Dirac basis of Quantum Mechanics and the chiral basis here are one unitary matrix apart; the former diagonalizes the energy sign at rest and suits the nonrelativistic limit and $g = 2$, the latter diagonalizes $\gamma^5$ and suits the Lorentz structure and massless limits — [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]], [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom|QM §C13.3★]].
> - $\gamma^\mu$ is an invariant tensor exactly as the Pauli matrices are an invariant vector of $SU(2)$ ($U^\dagger\sigma^iU = R_{ij}\sigma^j$), the relation behind the covering $SU(2) \to SO(3)$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-7|Theorem §C5a.1.7]].
> - The non-unitarity of spinor boosts is the spin-½ instance of the theorem that no nontrivial finite-dimensional Lorentz representation is unitary; $\gamma^0$ restores an invariant form as $g$ does for vectors — [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]].
> - $\gamma^5 = \frac43(\mathbf J_-^2 - \mathbf J_+^2)$ ties chirality to the two Casimirs of the Lorentz algebra, the spinor counterpart of the invariant $\mathbf E\cdot\mathbf B$ that separates the self-dual and anti-self-dual halves of the field strength — [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]].
> - The $-1$ of a $2\pi$ rotation on $\Lambda_{1/2}$ is the sign the spin–statistics theorem ties to anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-4|QM Theorem §C5.2.4]] (the measured sign).
> - The sixteen products are the matrices of the fermion bilinears (scalar, pseudoscalar, vector, axial vector, tensor) and of every trace identity used in scattering amplitudes — [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-8|Theorem §C5a.7.8]].
