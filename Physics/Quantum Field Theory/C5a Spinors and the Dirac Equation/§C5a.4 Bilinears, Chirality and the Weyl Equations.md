---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.3 The Dirac Equation and Its Lagrangian]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.5 Plane-Wave Solutions]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.9 (Fermion bilinears), §8.10 (The Weyl form of the Dirac equation), §8.8 (Derivation "The Dirac energy–momentum tensor is conserved, and the momentum operator"), Ch. 9 §9.6 (Definition "The matrix $\gamma^5$"), Ch. 3 §3.5 (Derivation "Belinfante: symmetrizing T with the spin current") · PHY 513 Lecture 8 (Larsen), Parts B–C · Peskin & Schroeder, §3.2, pp. 43–44, eqs. (3.36)–(3.44), §3.4, pp. 49–51, eqs. (3.68)–(3.76) · Yu Zhao-Huan, 量子场论讲义, §5.3, eqs. (5.93)–(5.101), (5.112)–(5.115) · the user's pre-course notes, §5.3 (Weyl spinors) · PHY 513, Problem Set 5, Problem 4 (as the user wrote it).*

Which Lorentz tensors can be built from a Dirac field, how does the field split into a left- and a right-handed half, and what does Noether's theorem give for it? The Dirac conjugate and the Lagrangian are [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]; $\gamma^5$, its algebra and the Weyl halves of the Dirac representation are [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]] and [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]; Noether's theorem and the energy–momentum tensor are [[§C1.11 Noether's Theorem|§C1.11]]–[[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum|§C1.12]] ([[P3 Noether's Procedure]]). This section adds the bilinears and their transformation, the chirality projectors, the Dirac equation in two-component form and the Weyl equations, and the Dirac field's currents: vector, axial, energy–momentum, spin and the symmetric energy–momentum tensor.

*Conventions* as in [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]; $\psi$ a classical field with commuting components; $\varepsilon^{0123} = +1$ ([[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]]); $a\overleftrightarrow{\partial}b \equiv a\,\partial b - (\partial a)\,b$.

## Bilinears

> [!definition] Definition §C5a.4.1: Fermion Bilinear
> A **fermion bilinear** is $\bar\psi\,\Gamma\,\chi$, with $\psi$, $\chi$ Dirac fields ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]), $\bar\psi$ the Dirac conjugate ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) (often $\chi = \psi$) and $\Gamma$ a constant $4\times4$ matrix, usually a product ("string") of $\gamma$ matrices. It is a number (row times matrix times column) and carries no spinor index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (opening) · PHY 513 Lecture 8, Part B ("Fermion Bilinears") · PS §3.4, p. 49 · Yu §5.3, after eq. (5.92)*

^def-c5a-4-1

> [!theorem] Theorem §C5a.4.1: Scalar, Vector and Tensor Bilinears
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]; and likewise $\chi$), a bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]]) transforms as $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$ does. In particular, with $y = \Lambda^{-1}x$,
>
> $$
> \bar\psi'\chi'(x) = \bar\psi\chi(y), \qquad \bar\psi'\gamma^\mu\chi'(x) = \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\chi(y), \qquad \bar\psi'[\gamma^\mu, \gamma^\nu]\chi'(x) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\,\bar\psi[\gamma^\rho, \gamma^\sigma]\chi(y) :
> $$
>
> a scalar, a vector and an antisymmetric tensor field ([[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-2|Def. §C1.8.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]). A string of $n$ $\gamma$'s gives an $n$-index tensor.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (Derivation "The first three bilinears") · PHY 513 Lecture 8, Part B · PS §3.4, p. 49 · Yu §5.3, eqs. (5.92), (5.94), (5.96)*

^thm-c5a-4-1

> [!derivation]- Derivation
> **1. General law.** By [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-3|Theorem §C5a.3.3]], $\bar\psi'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}$, and $\chi'(x) = \Lambda_{1/2}\chi(y)$. So $\bar\psi'\Gamma\chi'(x) = \bar\psi(y)\bigl(\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}\bigr)\chi(y)$.
>
> **2. Scalar, $\Gamma = \mathbb 1$.** $\Lambda_{1/2}^{-1}\Lambda_{1/2} = \mathbb 1$.
>
> **3. Vector, $\Gamma = \gamma^\mu$.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]); the number $\Lambda^\mu{}_\nu$ comes out of the bilinear.
>
> **4. Two $\gamma$'s.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ between them: $\Lambda_{1/2}^{-1}\gamma^\mu\gamma^\nu\Lambda_{1/2} = (\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2})(\Lambda_{1/2}^{-1}\gamma^\nu\Lambda_{1/2}) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\gamma^\rho\gamma^\sigma$. The same with $\mu \leftrightarrow \nu$, $\rho \leftrightarrow \sigma$ renamed, and subtracting: $\Lambda_{1/2}^{-1}[\gamma^\mu, \gamma^\nu]\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma[\gamma^\rho, \gamma^\sigma]$ (in the second product rename the dummies $\rho \leftrightarrow \sigma$ before subtracting).
>
> **5. $n$ $\gamma$'s.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ between every neighbouring pair: each $\gamma$ contributes one factor $\Lambda$.
>
> **What the derivation shows**
> - All spinor transformations cancel inside a bilinear; what is left is a tensor law fixed by the free indices of $\Gamma$. The symmetric combination $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ gives nothing new (the scalar times $g$).
> - ⚑ By-product: $\bar\psi[\gamma^\mu, \gamma^\nu]\psi$ transforms like $F^{\mu\nu}$, so $\bar\psi[\gamma^\mu, \gamma^\nu]\psi\,F_{\mu\nu}$ is a scalar: the structure of a magnetic-moment coupling ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-9|Theorem §C5a.7.9]]).
> - The Lecture 8 slide "Fermion Bilinears" lists the scalar as $\bar\psi\gamma^\mu\psi$, repeating the vector; the scalar is $\bar\psi\psi$, with no free index.
> - Used next: the sixteen bilinears (Def. §C5a.4.2) and every current below.

^der-c5a-4-1

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]

> [!definition] Definition §C5a.4.2: The Sixteen Bilinears
> With $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]) and
>
> $$
> \sigma^{\mu\nu} \equiv \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu} ,
> $$
>
> where $S^{\mu\nu}$ are the spinor generators ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]; other normalizations of $\sigma^{\mu\nu}$: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^cau-c5a-4-1|Caution: Three normalizations of σ^μν]]), the **standard bilinears** are
>
> | name | bilinear | number |
> |---|---|---|
> | scalar (S) | $\bar\psi\psi$ | 1 |
> | pseudoscalar (P) | $\bar\psi\,i\gamma^5\psi$ | 1 |
> | vector (V) | $\bar\psi\gamma^\mu\psi$ | 4 |
> | axial vector (A) | $\bar\psi\gamma^\mu\gamma^5\psi$ | 4 |
> | tensor (T) | $\bar\psi\sigma^{\mu\nu}\psi$, $\mu < \nu$ | 6 |
>
> Their matrices $\mathbb 1, i\gamma^5, \gamma^\mu, \gamma^\mu\gamma^5, \sigma^{\mu\nu}$ are sixteen; they span all $4\times4$ matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-8|Theorem §C5a.7.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (paragraph after the derivation), Ch. 9 §9.6 · PS §3.4, pp. 49–50 (table) · Yu §5.3, eqs. (5.93)–(5.96) · the user's pre-course notes, §5.3*

^def-c5a-4-2

> [!caution] Caution: Three normalizations of σ^μν
> Peskin–Schroeder and this note: $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. The Lorentz generators: $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac12\sigma^{\mu\nu}$. Problem Set 5 writes $\sigma^{\mu\nu} = \frac{1}{4i}[\gamma^\mu, \gamma^\nu] = -S^{\mu\nu}$. Identities homogeneous in $\sigma$ (such as the duality [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-7|Theorem §C5a.7.7]]) hold in every normalization; identities mixing $\sigma$ with other terms (the Gordon identity, [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-9|Theorem §C5a.7.9]]) do not. Peskin–Schroeder also write $\gamma^{\mu\nu} = \frac12[\gamma^\mu, \gamma^\nu] = -i\sigma^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$", last sentence) · PHY 513, Problem Set 5, Problem 5(d) statement · PS §3.4, p. 49*

^cau-c5a-4-1

> [!theorem] Theorem §C5a.4.2: Pseudoscalar and Axial Vector under Proper Lorentz Transformations
> Under $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]), the pseudoscalar and axial bilinears of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]] obey
>
> $$
> \bar\psi\,i\gamma^5\psi \;\to\; \bar\psi\,i\gamma^5\psi, \qquad \bar\psi\gamma^\mu\gamma^5\psi \;\to\; \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\gamma^5\psi \qquad (\text{at } \Lambda^{-1}x) :
> $$
>
> for proper orthochronous $\Lambda$ ([[§C1.4 The Lorentz Group#^thm-c1-4-3|Theorem §C1.4.3]]) they transform exactly as a scalar and a vector. They differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ only by a sign under parity (QFT C9, planned).
>
> *Source: PS §3.4, p. 50 ("pseudo-vector and pseudo-scalar") · Yu §5.3, eqs. (5.93), (5.95) · the user's PHY 513 notes, Ch. 8 §8.9 (closing paragraph)*

^thm-c5a-4-2

> [!derivation]- Derivation
> **1. $\gamma^5$ is invariant.** $\gamma^5$ commutes with every $S^{\mu\nu}$, hence with $\Lambda_{1/2} = \exp(-\frac i2\omega S)$ and its inverse: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]]).
>
> **2. Pseudoscalar.** Step 1 of Derivation §C5a.4.1 with $\Gamma = i\gamma^5$: $\Lambda_{1/2}^{-1}i\gamma^5\Lambda_{1/2} = i\gamma^5$.
>
> **3. Axial vector.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$: $\Lambda_{1/2}^{-1}\gamma^\mu\gamma^5\Lambda_{1/2} = (\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2})(\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2}) = \Lambda^\mu{}_\nu\gamma^\nu\gamma^5$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]] and step 1).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ comes from the identity component only, so it cannot see the "pseudo": $\gamma^5 \propto \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-5|Theorem §C5a.7.5]]) carries one $\varepsilon$, which is invariant under $\det\Lambda = +1$ and odd under parity ([[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5|§C1.5, Caution: The sign of ε⁰¹²³]]).
> - Used next: the axial current (Theorem §C5a.4.10).

^der-c5a-4-2

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]]

> [!theorem] Theorem §C5a.4.3: The Bilinears Are Real
> For any bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]]) of commuting components, $(\bar\psi\Gamma\psi)^* = \bar\psi\,\bar\Gamma\,\psi$ with $\bar\Gamma \equiv \gamma^0\Gamma^\dagger\gamma^0$. For the five standard matrices of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]], $\bar\Gamma = \Gamma$:
>
> $$
> \bar\psi\psi,\quad \bar\psi\,i\gamma^5\psi,\quad \bar\psi\gamma^\mu\psi,\quad \bar\psi\gamma^\mu\gamma^5\psi,\quad \bar\psi\sigma^{\mu\nu}\psi \quad\text{are real},
> $$
>
> while $\bar\psi\gamma^5\psi$ is imaginary. After quantization the same computation makes them Hermitian operators, once the product of two field operators at one point is defined by normal ordering ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]) and smeared with a test function (operator-valued distributions, [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the user's PHY 513 notes, Ch. 8 §8.8 ("Yu (5.97)–(5.101) give the reality of the bilinears") · the user's pre-course notes, §5.3*

^thm-c5a-4-3

> [!derivation]- Derivation
> **1. General.** A bilinear is a $1\times1$ matrix, so its complex conjugate is its adjoint: $(\psi^\dagger\gamma^0\Gamma\psi)^\dagger = \psi^\dagger\Gamma^\dagger\gamma^{0\dagger}\psi = \psi^\dagger\Gamma^\dagger\gamma^0\psi$. Insert $(\gamma^0)^2 = \mathbb 1$ in front: $= \psi^\dagger\gamma^0(\gamma^0\Gamma^\dagger\gamma^0)\psi = \bar\psi\bar\Gamma\psi$.
>
> **2. The five matrices.** Use $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]), $\gamma^{5\dagger} = \gamma^5$ and $\gamma^0\gamma^5 = -\gamma^5\gamma^0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]):
> - $\Gamma = \mathbb 1$: $\gamma^0\gamma^0 = \mathbb 1$.
> - $\Gamma = \gamma^\mu$: $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^0\gamma^\mu\gamma^0\gamma^0 = \gamma^\mu$.
> - $\Gamma = i\gamma^5$: $(i\gamma^5)^\dagger = -i\gamma^5$; $\gamma^0(-i\gamma^5)\gamma^0 = -i(-\gamma^5\gamma^0)\gamma^0 = i\gamma^5$.
> - $\Gamma = \gamma^\mu\gamma^5$: $(\gamma^\mu\gamma^5)^\dagger = \gamma^5\gamma^{\mu\dagger}$; $\gamma^0\gamma^5\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^0\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^\mu = \gamma^\mu\gamma^5$ (anticommute once more).
> - $\Gamma = \sigma^{\mu\nu}$: $\sigma^{\mu\nu\dagger} = -\frac i2[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$; sandwiching, $\gamma^0\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^{\nu\dagger}\gamma^0\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\nu\gamma^\mu$, so $\bar\sigma^{\mu\nu} = -\frac i2[\gamma^\nu, \gamma^\mu] = \sigma^{\mu\nu}$.
>
> **3. Without the $i$.** For $\Gamma = \gamma^5$, $\bar\Gamma = \gamma^0\gamma^5\gamma^0 = -\gamma^5$, so $(\bar\psi\gamma^5\psi)^{\ast} = -\bar\psi\gamma^5\psi$. ⚑ By-product: the $i$ in the pseudoscalar is the reality convention, as the $i$ in the Lagrangian is ([[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-3|§C5a.3, Remark: Why the i]]).
>
> **What the derivation shows**
> - The bar operation $\Gamma \mapsto \gamma^0\Gamma^\dagger\gamma^0$ is the adjoint with respect to the indefinite form $\gamma^0$ of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]]; the standard basis is chosen self-adjoint.
> - Step 1 used only $(AB)^\dagger = B^\dagger A^\dagger$, valid also for operator-valued components: the quantized bilinears are Hermitian ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).

^der-c5a-4-3

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]

## Chirality

> [!definition] Definition §C5a.4.3: Chirality Projectors
> $$
> P_L \equiv \tfrac12\bigl(\mathbb 1 - \gamma^5\bigr), \qquad P_R \equiv \tfrac12\bigl(\mathbb 1 + \gamma^5\bigr) .
> $$
>
> With $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]: a Dirac spinor with $\gamma^5\psi = -\psi$ ($P_L\psi = \psi$) has **left-handed chirality**, one with $\gamma^5\psi = +\psi$ right-handed. In the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), where $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]]), $P_L\psi = (\psi_L, 0)$ and $P_R\psi = (0, \psi_R)$ for $\psi = (\psi_L, \psi_R)$, the Weyl halves of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]].
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PS §3.4, eqs. (3.72), (3.76) · Yu §5.1 ($\gamma^5$), §5.3, eq. (5.112)*

^def-c5a-4-3

The same letters denote the two-component Weyl spinors $\psi_L$, $\psi_R$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]) and, by abuse, the four-component $P_L\psi$, $P_R\psi$; context decides. Chirality is the eigenvalue of $\gamma^5$, a property of the representation; helicity is the spin along the momentum, a property of a state. They agree only for massless positive-frequency solutions (Theorem §C5a.4.8; [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-14|Theorem §C5a.6.14]]).

> [!theorem] Theorem §C5a.4.4: Properties of the Chirality Projectors
> 1. $P_L^2 = P_L$, $P_R^2 = P_R$, $P_LP_R = P_RP_L = 0$, $P_L + P_R = \mathbb 1$.
> 2. $P_L\gamma^\mu = \gamma^\mu P_R$ and $P_R\gamma^\mu = \gamma^\mu P_L$.
> 3. $[P_{L,R}, S^{\mu\nu}] = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]), so $P_{L,R}\Lambda_{1/2} = \Lambda_{1/2}P_{L,R}$: chirality is Lorentz invariant, and $P_L\psi$, $P_R\psi$ transform separately.
> 4. $\overline{P_L\psi} = \bar\psi P_R$ and $\overline{P_R\psi} = \bar\psi P_L$.
>
> *Source: PS §3.4, pp. 50–51 (eqs. (3.71)–(3.72), (3.76) and the paragraph on reducibility) · the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$")*

^thm-c5a-4-4

> [!derivation]- Derivation
> Use $(\gamma^5)^2 = \mathbb 1$, $\gamma^{5\dagger} = \gamma^5$, $\{\gamma^5, \gamma^\mu\} = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]) and $[\gamma^5, S^{\mu\nu}] = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]]).
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
> - Step 2 is why every $\gamma$ flips chirality, and why the kinetic term, with one $\gamma$ between $\bar\psi$ and $\psi$, does not mix chiralities while the mass term, with none, does (Theorem §C5a.4.5).
> - ⚑ By-product: the projector on a "left-handed" field appears as $P_R$ next to $\bar\psi$ (step 4): $\overline{\psi_L}\psi_L = \bar\psi P_RP_L\psi = 0$.

^der-c5a-4-4

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-3|Def. §C5a.4.3]]

> [!theorem] Theorem §C5a.4.5: Bilinears in Weyl Components
> For $\psi = (\psi_L, \psi_R)$, $\chi = (\chi_L, \chi_R)$ in the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]; Weyl halves [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]]), $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) and
>
> $$
> \bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R, \qquad \bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R ,
> $$
>
> $$
> \bar\psi\gamma^\mu\gamma^5\chi = -\psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R, \qquad \bar\psi\,i\gamma^5\chi = i\bigl(\psi_L^\dagger\chi_R - \psi_R^\dagger\chi_L\bigr) .
> $$
>
> Hence the Dirac Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) is
>
> $$
> \mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m\bigl(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L\bigr) :
> $$
>
> the kinetic terms keep the chiralities apart, the mass term pairs them.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 ("This is the Dirac invariant": $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$), §8.10 · PS §3.2, eqs. (3.36), (3.42)*

^thm-c5a-4-5

> [!derivation]- Derivation
> In the chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]]).
>
> **1. The conjugate row.** $\psi^\dagger = (\psi_L^\dagger, \psi_R^\dagger)$; multiplying by $\gamma^0$ swaps the blocks: $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$.
>
> **2. Scalar.** $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$.
>
> **3. Vector.** $\gamma^\mu\chi = (\sigma^\mu\chi_R,\ \bar\sigma^\mu\chi_L)$, so $\bar\psi\gamma^\mu\chi = \psi_R^\dagger\sigma^\mu\chi_R + \psi_L^\dagger\bar\sigma^\mu\chi_L$.
>
> **4. Axial vector.** $\gamma^5\chi = (-\chi_L, \chi_R)$, then $\gamma^\mu\gamma^5\chi = (\sigma^\mu\chi_R,\ -\bar\sigma^\mu\chi_L)$, so $\bar\psi\gamma^\mu\gamma^5\chi = \psi_R^\dagger\sigma^\mu\chi_R - \psi_L^\dagger\bar\sigma^\mu\chi_L$.
>
> **5. Pseudoscalar.** $\bar\psi\gamma^5\chi = (\psi_R^\dagger, \psi_L^\dagger)(-\chi_L, \chi_R) = -\psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$; multiply by $i$.
>
> **6. The Lagrangian.** Step 3 with $\chi \to \partial_\mu\psi$ (the blocks of $\partial_\mu\psi$ are $\partial_\mu\psi_L$, $\partial_\mu\psi_R$) gives the kinetic terms; step 2 with $\chi = \psi$ gives the mass term.
>
> **What the derivation shows**
> - The invariant form $\gamma^0$ of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]] *is* the pairing of a left- with a right-handed slot ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-11|Theorem §C5a.1.11]]): a Lorentz scalar without derivatives must couple $\psi_L$ to $\psi_R$, so a Dirac mass needs both ([[§C5a.1 Weyl Spinors and SL(2,C)#^rem-c5a-1-3|§C5a.1, Remark: Kinematics allows one handedness, a mass needs both]]).
> - The vector current splits into a left and a right current with no cross terms; the axial current is their difference. Both statements are basis independent by [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-4|Theorem §C5a.4.4]]: $\bar\psi\gamma^\mu\psi = \bar\psi\gamma^\mu P_L\psi + \bar\psi\gamma^\mu P_R\psi$.

^der-c5a-4-5

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]

## The Weyl form and the Weyl equations

> [!theorem] Theorem §C5a.4.6: The Dirac Equation in Two-Component Form
> For $\psi = (\psi_L, \psi_R)$ in the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) is equivalent to
>
> $$
> i\bar\sigma^\mu\partial_\mu\psi_L = m\,\psi_R, \qquad i\sigma^\mu\partial_\mu\psi_R = m\,\psi_L ,
> $$
>
> with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]], i.e. $i(\partial_0 - \boldsymbol\sigma\cdot\nabla)\psi_L = m\psi_R$, $i(\partial_0 + \boldsymbol\sigma\cdot\nabla)\psi_R = m\psi_L$. The kinetic operators act within each Weyl block; only the mass couples them.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Derivation "The Dirac equation in two-component form", eq. (weylcoupled)) · PHY 513 Lecture 8, Part C ("Dirac Equation in 2-Component Form") · PS §3.2, eqs. (3.39), (3.43) · Yu §5.3, eqs. (5.113)–(5.114)*

^thm-c5a-4-6

> [!derivation]- Derivation
> **1. The operator in blocks.** With $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ and $-m\mathbb 1_4 = \operatorname{diag}(-m\mathbb 1_2, -m\mathbb 1_2)$,
>
> $$
> i\gamma^\mu\partial_\mu - m = \begin{pmatrix}-m & i\sigma^\mu\partial_\mu\\ i\bar\sigma^\mu\partial_\mu & -m\end{pmatrix} .
> $$
>
> **2. Act on the column.** $\begin{pmatrix}-m & i\sigma\cdot\partial\\ i\bar\sigma\cdot\partial & -m\end{pmatrix}\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix} = \begin{pmatrix}i\sigma^\mu\partial_\mu\psi_R - m\psi_L\\ i\bar\sigma^\mu\partial_\mu\psi_L - m\psi_R\end{pmatrix}$, which vanishes exactly when both stated equations hold.
>
> **3. In components.** $\sigma^\mu\partial_\mu = \mathbb 1\partial_0 + \sigma^i\partial_i = \partial_0 + \boldsymbol\sigma\cdot\nabla$ and $\bar\sigma^\mu\partial_\mu = \partial_0 - \boldsymbol\sigma\cdot\nabla$ (no metric: upper index on $\sigma$, lower on $\partial$; [[§C5a.3 The Dirac Equation and Its Lagrangian#^cau-c5a-3-1|§C5a.3, Caution: γ^μ∂_μ has a plus sign]]).
>
> **What the derivation shows**
> - Representation theory allows the two blocks to be treated separately ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]); the equation of motion couples them, through the mass and only through it (figure).
> - The same equations follow by varying $\psi_L^\dagger$ and $\psi_R^\dagger$ in the Lagrangian of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]].

^der-c5a-4-6

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]

![[ph-qft-c5-4-1.svg]]
*The Dirac equation in two-component form: the Weyl halves are separate representations, and the mass is the only coupling between them (adapted from the user's PHY 513 notes, Ch. 8 §8.10).*

> [!model] Model §C5a.4.7: The Weyl Fields
> A **left-handed Weyl field** is a two-component field $\psi_L$ in $(\frac12, 0)$ ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-6|Theorem §C3.2.6]]; Weyl matrices [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]]) with
>
> $$
> \mathcal L_L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L, \qquad i\bar\sigma^\mu\partial_\mu\psi_L = 0 ;
> $$
>
> a **right-handed Weyl field** $\psi_R$ in $(0, \frac12)$ has $\mathcal L_R = i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = 0$. These are the **Weyl equations**.
>
> *Assumptions:* $m = 0$ (the two blocks of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]] decouple, and either may be kept alone, consistently both as a representation and dynamically); classical, free; no parity symmetry (parity exchanges the two, [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-10|Theorem §C3.2.10]]).
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations", eq. (weyl)) · PHY 513 Lecture 8, Part C ("Weyl Equation") · PS §3.2, eqs. (3.40), (3.44) · Yu §5.3, eq. (5.115)*

^mod-c5a-4-7

The 513 notes box the Weyl equations as a principle; here they are a model, the massless idealization of the Dirac theory (or, in the Standard Model, the starting point). Each component of a Weyl solution obeys the massless Klein–Gordon equation, by $(\sigma\cdot\partial)(\bar\sigma\cdot\partial) = \partial^2$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-1|Theorem §C5a.1.1]]), the two-component version of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]].

> [!theorem] Theorem §C5a.4.8: Weyl Plane Waves Have Fixed Helicity
> Let $\psi_L = \xi\,e^{-ip\cdot x}$ with $p^0 > 0$ and a constant nonzero two-spinor $\xi$. It solves the left-handed Weyl equation ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]]) if and only if $p^2 = 0$ ($p^0 = \lvert\mathbf p\rvert$) and
>
> $$
> \bigl(\hat{\mathbf p}\cdot\boldsymbol\sigma\bigr)\,\xi = -\xi :
> $$
>
> helicity ([[§C3.6★ Massless Particles and Helicity#^def-c3-6-1|Def. §C3.6.1]]) $h = \hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2 = -\frac12$. For $\psi_R = \eta\,e^{-ip\cdot x}$, $p^2 = 0$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$, $h = +\frac12$. One Weyl field has one helicity for its positive-frequency solutions.
>
> *Source: the user's pre-course notes, §5.3 ("Weyl spinors": "$(E + \boldsymbol\sigma\cdot\mathbf p)\eta = 0$, i.e. $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = -\eta$: helicity $-\frac12$") · Yu §5.3 (paragraph after eq. (5.115)) · the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations": "a single Weyl field describes a massless particle of one helicity")*

^thm-c5a-4-8

> [!derivation]- Derivation
> **1. The derivative.** $\partial_\mu e^{-ip\cdot x} = -ip_\mu e^{-ip\cdot x}$, so $i\bar\sigma^\mu\partial_\mu\psi_L = i(-i)\bar\sigma^\mu p_\mu\,\xi\,e^{-ip\cdot x} = (\bar\sigma^\mu p_\mu)\xi\,e^{-ip\cdot x}$. The exponential never vanishes: the equation is $(\bar\sigma^\mu p_\mu)\xi = 0$.
>
> **2. The matrix.** $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ and $p_\mu = (p^0, -\mathbf p)$, so $\bar\sigma^\mu p_\mu = p^0 + \boldsymbol\sigma\cdot\mathbf p$ (two minus signs).
>
> **3. A nonzero solution needs $p^2 = 0$.** $\det(p^0 + \boldsymbol\sigma\cdot\mathbf p) = (p^0)^2 - \mathbf p^2 = p^2$ (the eigenvalues of $\boldsymbol\sigma\cdot\mathbf p$ are $\pm\lvert\mathbf p\rvert$, since $(\boldsymbol\sigma\cdot\mathbf p)^2 = \mathbf p^2$ and $\operatorname{tr}\boldsymbol\sigma\cdot\mathbf p = 0$). A nonzero kernel requires $p^2 = 0$; with $p^0 > 0$, $p^0 = \lvert\mathbf p\rvert$ and $\mathbf p \ne 0$.
>
> **4. The kernel.** $(\lvert\mathbf p\rvert + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$; divide by $\lvert\mathbf p\rvert$: $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = -\xi$, a one-dimensional kernel.
>
> **5. Right-handed.** $\sigma^\mu p_\mu = p^0 - \boldsymbol\sigma\cdot\mathbf p$; the same steps give $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$.
>
> **6. Helicity.** For spin $\frac12$ the spin operator in each Weyl block is $\frac12\boldsymbol\sigma$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]), so the spin along $\hat{\mathbf p}$ is $\hat{\mathbf p}\cdot\boldsymbol\sigma/2 = \mp\frac12$ ([[§C3.6★ Massless Particles and Helicity#^def-c3-6-1|Def. §C3.6.1]]).
>
> **What the derivation shows**
> - Chirality and helicity coincide for massless positive-frequency solutions: left-handed means helicity $-\frac12$. For the negative-frequency solutions $\xi\,e^{+ip\cdot x}$ the condition is the same, $(p^0 + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$ (step 1 with $p \to -p$ gives $-(\bar\sigma\cdot p)\xi = 0$); after quantization they describe the antiparticle, which carries the opposite helicity $+\frac12$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]): the neutrino–antineutrino pair of [[§C3.6★ Massless Particles and Helicity|§C3.6★]].
> - ⚑ By-product: half the components of a Weyl spinor are removed for each momentum; a Weyl field has one physical polarization per momentum, the minimal content of a massless spin-½ particle (the little-group count of [[§C3.6★ Massless Particles and Helicity#^thm-c3-6-6|Theorem §C3.6.6]]).
> - For massive Dirac spinors helicity is frame dependent; it approaches chirality at high energy ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-14|Theorem §C5a.6.14]]).
> - Assumption: the plane wave solves the Weyl equation pointwise; as a field on spacetime it is not square integrable but a tempered distribution, and the equation holds also in $\mathcal S'$, as for the Dirac plane waves ([[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]]).

^der-c5a-4-8

*Uses:* [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]], [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C3.6★ Massless Particles and Helicity#^def-c3-6-1|Def. §C3.6.1]]

> [!remark] Remark: When the Weyl description is useful
> Not for the electron of Dirac's problem: in hydrogen the electron's kinetic energy is tiny compared with its mass, and the mass couples the two halves at full strength. It is natural where the mass is zero or small, as for neutrinos: in the Standard Model the neutrinos are massless and only left-handed ones exist. Their observed small masses require going beyond it. A mass of the form of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]], a *Dirac* mass, needs a separate right-handed field.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (paragraph "When is the Weyl description useful?") · PHY 513 Lecture 8, Part C*

^rem-c5a-4-1

> [!remark]- ★ Remark: A Majorana mass needs no second field
> By [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-11|Theorem §C3.2.11]] and [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-11|Theorem §C5a.1.11]], $\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, so a single left-handed field can supply its own partner: $\psi_L^{\mathsf T}\varepsilon\,\psi_L$ is Lorentz invariant, because $\Lambda_L^{\mathsf T}\varepsilon\Lambda_L = (\det\Lambda_L)\varepsilon = \varepsilon$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-10|Theorem §C5a.1.10]]). This is a *Majorana* mass. For commuting components it vanishes identically, $\psi^{\mathsf T}\varepsilon\psi = \psi_1\psi_2 - \psi_2\psi_1 = 0$ (with $\varepsilon^{12} = 1$); it exists only for anticommuting fields ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]; Majorana fields, QFT C9, planned). Whether neutrino masses are of Dirac or Majorana type is not known.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Caution "'A neutrino mass needs a right-handed neutrino'")*

^rem-c5a-4-2

## Currents

> [!theorem] Theorem §C5a.4.9: The Vector Current
> The global phase rotation $\psi \to e^{i\alpha}\psi$, $\bar\psi \to e^{-i\alpha}\bar\psi$ leaves the Dirac Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) invariant ($\mathcal J = 0$, [[§C1.11 Noether's Theorem#^def-c1-11-3|Def. §C1.11.3]]). Its Noether current ([[§C1.11 Noether's Theorem#^thm-c1-11-2|Theorem §C1.11.2]]) is $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$; with the conventional sign,
>
> $$
> j^\mu \equiv \bar\psi\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0 \ \ \text{on solutions}, \qquad Q = \int d^3x\,j^0 = \int d^3x\,\psi^\dagger\psi \ge 0 .
> $$
>
> $j^\mu$ is a real four-vector field, for every $m$. The sign convention is that of the complex scalar ([[§C1.11 Noether's Theorem#^cau-c1-11-3|§C1.11, Caution: Sign and normalization of the U(1) current]]).
>
> *Source: PS §3.4, eqs. (3.73)–(3.74) and p. 51 (Noether currents of $\psi \to e^{i\alpha}\psi$) · the user's PHY 513 notes, Ch. 9 §9.4 ("it is the time component of the current $\bar\psi\gamma^\mu\psi$"), Ch. 9 §9.6 (paragraph "What the Gordon identity says") · Yu §5.3, eq. (5.94)*

^thm-c5a-4-9

> [!derivation]- Derivation
> The steps of [[P3 Noether's Procedure]]; two independent fields $\psi$, $\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], step 1).
>
> **1. Generators.** $\psi' = e^{i\alpha}\psi$, $\bar\psi' = (e^{i\alpha}\psi)^\dagger\gamma^0 = e^{-i\alpha}\bar\psi$ ($\alpha$ real). To first order $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$ ([[§C1.11 Noether's Theorem#^def-c1-11-2|Def. §C1.11.2]]).
>
> **2. Substitute.** $\alpha$ is constant, so $\partial_\mu(e^{i\alpha}\psi) = e^{i\alpha}\partial_\mu\psi$ and $\mathcal L' = e^{-i\alpha}e^{i\alpha}\bar\psi(i\slashed{\partial} - m)\psi = \mathcal L$, exactly: every term has one $\bar\psi$ and one $\psi$.
>
> **3. Test.** $\delta\mathcal L = 0$: $\mathcal J^\mu = 0$.
>
> **4. Current.** $\partial\mathcal L/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$, $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$ (Derivation §C5a.3.6, step 3). [[§C1.11 Noether's Theorem#^thm-c1-11-2|Theorem §C1.11.2]]: $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\psi) + 0\cdot(-i\bar\psi) = -\bar\psi\gamma^\mu\psi$. Any constant multiple of a conserved current is conserved; the convention is $j^\mu = -j^\mu_{\rm N}$.
>
> **5. Check, directly.** Product rule: $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$. The conjugate Dirac equation $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$ gives $(\partial_\mu\bar\psi)\gamma^\mu = im\bar\psi$; the Dirac equation $i\gamma^\mu\partial_\mu\psi = m\psi$ gives $\gamma^\mu\partial_\mu\psi = -im\psi$. So $\partial_\mu j^\mu = im\bar\psi\psi - im\bar\psi\psi = 0$. Both equations are used, one per field.
>
> **6. Charge.** $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger(\gamma^0)^2\psi = \psi^\dagger\psi = \sum_a\lvert\psi_a\rvert^2 \ge 0$. $Q$ is constant for fields falling off faster than $1/r^2$ ([[§C1.11 Noether's Theorem#^thm-c1-11-3|Theorem §C1.11.3]]). Reality: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]]; vector law: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]].
>
> **What the derivation shows**
> - ⚑ By-product: the classical charge is positive definite, unlike the scalar's ([[§C1.11 Noether's Theorem#^thm-c1-11-5|Theorem §C1.11.5]]); it is Quantum Mechanics' probability density. After quantization with anticommutators, normal-ordered, it becomes particles minus antiparticles and can have either sign ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]).
> - ⚑ By-product: the sign of the Noether current is opposite to the conventional one, as for the complex scalar ([[§C1.11 Noether's Theorem#^cau-c1-11-3|§C1.11, Caution: Sign and normalization of the U(1) current]]).
> - Used next: coupled to the photon, $e\,j^\mu A_\mu$ (QFT C8, planned); its matrix elements are split by the Gordon identity ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-9|Theorem §C5a.7.9]]).

^der-c5a-4-9

*Uses:* [[§C1.11 Noether's Theorem#^def-c1-11-2|Def. §C1.11.2]], [[§C1.11 Noether's Theorem#^thm-c1-11-2|Theorem §C1.11.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C1.11 Noether's Theorem#^thm-c1-11-3|Theorem §C1.11.3]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–6]]

> [!theorem] Theorem §C5a.4.10: The Axial Current
> For every solution of the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]), with $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]],
>
> $$
> j^{\mu5} \equiv \bar\psi\gamma^\mu\gamma^5\psi, \qquad \partial_\mu j^{\mu5} = 2im\,\bar\psi\gamma^5\psi .
> $$
>
> It is conserved if and only if $m = 0$ (for generic solutions); then the **chiral transformation** $\psi \to e^{i\alpha\gamma^5}\psi$ is a symmetry, and the chiral currents $j^\mu_L = \bar\psi\gamma^\mu P_L\psi = \psi_L^\dagger\bar\sigma^\mu\psi_L$ and $j^\mu_R = \bar\psi\gamma^\mu P_R\psi = \psi_R^\dagger\sigma^\mu\psi_R$ are separately conserved ($P_{L,R}$: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-3|Def. §C5a.4.3]]; Weyl forms: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]).
>
> *Source: PS §3.4, eqs. (3.73), (3.75)–(3.76) and p. 51 (the chiral transformation)*

^thm-c5a-4-10

> [!derivation]- Derivation
> **1. Product rule.** $\partial_\mu(\bar\psi\gamma^\mu\gamma^5\psi) = (\partial_\mu\bar\psi)\gamma^\mu\gamma^5\psi + \bar\psi\gamma^\mu\gamma^5\partial_\mu\psi$ ($\gamma$'s constant).
>
> **2. First term.** $(\partial_\mu\bar\psi)\gamma^\mu = im\bar\psi$ (conjugate equation, as in Derivation §C5a.4.9, step 5): $im\bar\psi\gamma^5\psi$.
>
> **3. Second term.** Move $\gamma^5$ to the left: $\gamma^\mu\gamma^5 = -\gamma^5\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]), so $\bar\psi\gamma^\mu\gamma^5\partial_\mu\psi = -\bar\psi\gamma^5\gamma^\mu\partial_\mu\psi = -\bar\psi\gamma^5(-im\psi) = im\bar\psi\gamma^5\psi$.
>
> **4. Add.** $\partial_\mu j^{\mu5} = 2im\bar\psi\gamma^5\psi$; for $m = 0$ it vanishes.
>
> **5. The chiral transformation.** $\psi' = e^{i\alpha\gamma^5}\psi$. Then $\psi'^\dagger = \psi^\dagger e^{-i\alpha\gamma^5}$ ($\gamma^5$ Hermitian) and $\bar\psi' = \psi^\dagger e^{-i\alpha\gamma^5}\gamma^0 = \bar\psi e^{+i\alpha\gamma^5}$, since $\gamma^5\gamma^0 = -\gamma^0\gamma^5$ term by term in the series. Kinetic term: $\bar\psi e^{i\alpha\gamma^5}\gamma^\mu e^{i\alpha\gamma^5}\partial_\mu\psi = \bar\psi\gamma^\mu e^{-i\alpha\gamma^5}e^{i\alpha\gamma^5}\partial_\mu\psi$: invariant. Mass term: $\bar\psi e^{2i\alpha\gamma^5}\psi \ne \bar\psi\psi$: not invariant unless $m = 0$. Noether: $\Delta\psi = i\gamma^5\psi$, $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\gamma^5\psi) = -j^{\mu5}$ (with $\mathcal J = 0$ for $m = 0$).
>
> **6. Chiral currents.** $j^\mu \pm j^{\mu5}$ over 2 are $\bar\psi\gamma^\mu P_{R,L}\psi$; their Weyl forms are [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]. For $m = 0$ both $j^\mu$ and $j^{\mu5}$ are conserved, hence each combination.
>
> **What the derivation shows**
> - The mass is the only term that breaks chiral symmetry, because it is the only term that pairs $\psi_L$ with $\psi_R$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]).
> - ⚑ By-product: classical conservation for $m = 0$; whether it survives quantization is a separate question (it does not, in general: the axial anomaly, PS ch. 19, beyond the course).

^der-c5a-4-10

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]

## Energy, momentum and spin

> [!theorem] Theorem §C5a.4.11: The Canonical Energy–Momentum Tensor of the Dirac Field
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] the canonical tensor ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^def-c1-12-2|Def. §C1.12.2]]) is
>
> $$
> T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L ,
> $$
>
> and $\partial_\mu T^{\mu\nu} = 0$ on solutions (the first index is the current index). On solutions $\mathcal L = 0$, so $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi$, which is not symmetric.
>
> *Source: PHY 513, Problem Set 5, Problem 4(a) (as the user wrote it) · the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The Dirac energy–momentum tensor is conserved, and the momentum operator"), Ch. 3 §3.5 (table of canonical tensors)*

^thm-c5a-4-11

> [!derivation]- Derivation (as the user wrote it for Problem Set 5, Problem 4(a))
> Write $\mathcal L = \bar\psi(i\gamma^\rho\partial_\rho - m)\psi$ with the summed index renamed $\rho$, apart from the free $\mu$, $\nu$.
>
> **1. The tensor.** $\partial\mathcal L/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$ and $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$, so Def. §C1.12.2 gives $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi + 0 - g^{\mu\nu}\mathcal L$.
>
> **2. The two equations of motion.** $i\gamma^\rho\partial_\rho\psi = m\psi$ and $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]]).
>
> **3. The divergence, by the product rule.** With $\partial_\mu g^{\mu\nu} = 0$ and $g^{\mu\nu}\partial_\mu = \partial^\nu$,
>
> $$
> \partial_\mu T^{\mu\nu} = i(\partial_\mu\bar\psi)\gamma^\mu\partial^\nu\psi + i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - (\partial^\nu\bar\psi)(i\gamma^\rho\partial_\rho - m)\psi - \bar\psi(i\gamma^\rho\partial_\rho - m)\partial^\nu\psi .
> $$
>
> The last two terms are $\partial^\nu\mathcal L$, the derivative hitting $\bar\psi$ and then $\psi$; $\gamma$'s and $m$ are constant.
>
> **4. Use the equations.** First term: $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$, so it is $-m\bar\psi\partial^\nu\psi$. Third term: $(i\gamma^\rho\partial_\rho - m)\psi = 0$, so it vanishes.
>
> **5. Expand the last term.** $-\bar\psi(i\gamma^\rho\partial_\rho - m)\partial^\nu\psi = -i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi + m\bar\psi\partial^\nu\psi$.
>
> **6. Collect.**
>
> $$
> \partial_\mu T^{\mu\nu} = \bigl(-m\bar\psi\partial^\nu\psi + m\bar\psi\partial^\nu\psi\bigr) + \bigl(i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi\bigr) = 0 ,
> $$
>
> the mass terms cancelling and the second pair being equal ($\mu$, $\rho$ are both dummies).
>
> **What the derivation shows**
> - Both equations of motion are needed, one for each field; this is the general statement [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-5|Theorem §C1.12.5]] (off shell, $\partial_\mu T^{\mu\nu} = -\sum_a\mathrm{EL}_a\partial^\nu\phi_a$) for this $\mathcal L$, here checked directly.
> - ⚑ By-product: $T^{\mu\nu} - T^{\nu\mu} = i\bar\psi(\gamma^\mu\partial^\nu - \gamma^\nu\partial^\mu)\psi \ne 0$; the antisymmetric part is the divergence of the spin current ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-8|Theorem §C1.12.8]]; Theorem §C5a.4.13), and is removed in Theorem §C5a.4.14.
> - Assumption: $\psi \in C^2$ (second derivatives commute in the cancellation of step 6).

^der-c5a-4-11

*Uses:* [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^def-c1-12-2|Def. §C1.12.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-5|Theorem §C1.12.5]]

*Procedure:* [[P3 Noether's Procedure#^p3-4|P3, steps 4–5]]

> [!theorem] Theorem §C5a.4.12: Energy and Momentum of the Dirac Field
> The charges $P^\nu = \int d^3x\,T^{0\nu}$ ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-6|Theorem §C1.12.6]]) of the canonical tensor of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-11|Theorem §C5a.4.11]] are, with $\mathcal H$ of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]],
>
> $$
> H = P^0 = \int d^3x\,\mathcal H = \int d^3x\,\psi^\dagger\bigl(-i\boldsymbol\alpha\cdot\nabla + \beta m\bigr)\psi \;\overset{\text{on shell}}{=}\; \int d^3x\,\psi^\dagger\,i\partial_t\psi, \qquad \mathbf P = \int d^3x\,\psi^\dagger\bigl(-i\nabla\bigr)\psi .
> $$
>
> $\mathbf P$ is the Noether charge of spatial translations, not the canonical momentum $\pi_\psi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]).
>
> *Source: PHY 513, Problem Set 5, Problem 4(b) (as the user wrote it) · the user's PHY 513 notes, Ch. 8 §8.8, eq. (diracP) · PS §3.5, eq. (3.84)*

^thm-c5a-4-12

> [!derivation]- Derivation
> **1. $T^{00}$.** $T^{00} = i\bar\psi\gamma^0\partial^0\psi - g^{00}\mathcal L = i\psi^\dagger\partial_t\psi - \mathcal L$ (with $\bar\psi\gamma^0 = \psi^\dagger$, $\partial^0 = \partial_t$, $g^{00} = 1$). This is $\pi_\psi\dot\psi - \mathcal L = \mathcal H$ identically ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]), and $i\psi^\dagger\partial_t\psi$ on shell, where $\mathcal L = 0$.
>
> **2. $T^{0i}$.** $g^{0i} = 0$, so $T^{0i} = i\bar\psi\gamma^0\partial^i\psi = i\psi^\dagger\partial^i\psi = -i\psi^\dagger\partial_i\psi$, using $\partial^i = -\partial_i$. Integrating, $P^i = \int d^3x\,\psi^\dagger(-i\partial_i)\psi$, the components of $\mathbf P$.
>
> **3. Conservation.** By Theorem §C5a.4.11 and [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-6|Theorem §C1.12.6]], $dP^\nu/dt = 0$ for fields with $T^{i\nu}$ falling off faster than $1/r^2$.
>
> **What the derivation shows**
> - $\mathbf P$ is the expectation of the one-particle momentum operator $-i\nabla$ in the "wave function" $\psi$, and $H$ that of $H_{\text{s.p.}}$: the field charges look like one-particle expectation values, the reason the Dirac sea picture works as far as it does.
> - ⚑ By-product: classically $H$ is unbounded below (negative-frequency modes, [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]]); in mode form after quantization it is positive only with anticommutators ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]).
> - The canonical momentum $\pi_\psi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]) is a field, conjugate to $\psi$ in the brackets; $\mathbf P$ is a number (an operator after quantization) generating translations. Problem Set 5's note makes the same distinction.

^der-c5a-4-12

*Uses:* [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-9|Theorem §C5a.3.9]], [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-6|Theorem §C1.12.6]]

> [!theorem] Theorem §C5a.4.13: The Spin Current and the Angular Momentum of the Dirac Field
> The spin part of the Lorentz current of [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-7|Theorem §C1.12.7]] is, for the Dirac field,
>
> $$
> \mathcal S^{\lambda\mu\nu} = \bar\psi\gamma^\lambda S^{\mu\nu}\psi = \tfrac i4\,\bar\psi\gamma^\lambda[\gamma^\mu, \gamma^\nu]\psi ,
> $$
>
> with the Hermitian-convention generators $S^{\mu\nu}$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]] (which are $i$ times the real-convention ones of Theorem §C1.12.7: [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]); and on solutions the angular momentum $J^i = \frac12\varepsilon_{ijk}J^{jk}$ ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^def-c1-12-3|Def. §C1.12.3]]) is
>
> $$
> \mathbf J = \int d^3x\,\psi^\dagger\Bigl(\mathbf x\times(-i\nabla) + \tfrac12\boldsymbol\Sigma\Bigr)\psi, \qquad \boldsymbol\Sigma = \begin{pmatrix}\boldsymbol\sigma & 0\\ 0 & \boldsymbol\sigma\end{pmatrix} :
> $$
>
> orbital plus spin $\frac12$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (eq. (Mgeneral); "the Dirac spin $\frac12$") · Yu §1.7.3, eqs. (1.241)–(1.248) (orbital and spin split) · computed here from [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-7|Theorem §C1.12.7]]*

^thm-c5a-4-13

> [!derivation]- Derivation
> **1. The generator in the convention of Theorem §C1.12.7.** There $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}_{(C1.8)}$, with $S^{\mu\nu}_{(C1.8)}$ the real-convention generators of [[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-3|Def. §C1.8.3]]; for the Dirac field $D = \Lambda_{1/2} = 1 - \frac i2\omega_{\mu\nu}S^{\mu\nu} + O(\omega^2)$. The $\omega_{\mu\nu}$ are arbitrary antisymmetric and both generators antisymmetric, so $S^{\mu\nu}_{(C1.8)} = -iS^{\mu\nu}$ ([[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]).
>
> **2. The spin current.** $\mathcal S^{\lambda\mu\nu} = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\lambda\phi_a)}(S^{\mu\nu}_{(C1.8)}\phi)_a$, summed over $\psi$ and $\bar\psi$. The $\bar\psi$ term is zero ($\partial\mathcal L/\partial(\partial_\lambda\bar\psi) = 0$). The $\psi$ term: $i\bar\psi\gamma^\lambda\cdot(-iS^{\mu\nu}\psi) = \bar\psi\gamma^\lambda S^{\mu\nu}\psi$, and $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]).
>
> **3. The spin charges.** $S^{\mu\nu}_{\rm charge} = \int d^3x\,\mathcal S^{0\mu\nu} = \int d^3x\,\bar\psi\gamma^0S^{\mu\nu}\psi = \int d^3x\,\psi^\dagger S^{\mu\nu}\psi$.
>
> **4. Spatial generators.** In the chiral basis $S^{jk} = \frac12\varepsilon^{jkl}\Sigma^l$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]), so $\frac12\varepsilon_{ijk}S^{jk} = \frac14\varepsilon_{ijk}\varepsilon_{jkl}\Sigma^l = \frac14\cdot2\delta_{il}\Sigma^l = \frac12\Sigma^i$, using $\varepsilon_{ijk}\varepsilon_{ljk} = 2\delta_{il}$ (with $\varepsilon_{jkl} = \varepsilon_{ljk}$, cyclic). The spin part of $J^i$ is $\int\psi^\dagger\frac12\Sigma^i\psi$.
>
> **5. The orbital part.** On shell $T^{0\rho} = i\psi^\dagger\partial^\rho\psi$ (Derivation §C5a.4.12). $L^{jk} = \int d^3x\,(x^jT^{0k} - x^kT^{0j}) = \int d^3x\,\psi^\dagger\,i(x^j\partial^k - x^k\partial^j)\psi = \int d^3x\,\psi^\dagger(-i)(x^j\partial_k - x^k\partial_j)\psi$ ($\partial^k = -\partial_k$). Then $\frac12\varepsilon_{ijk}L^{jk} = \int\psi^\dagger(-i)\varepsilon_{ijk}x^j\partial_k\psi = \int\psi^\dagger\bigl(\mathbf x\times(-i\nabla)\bigr)_i\psi$ (the two terms of the antisymmetric bracket give equal contributions after renaming $j \leftrightarrow k$).
>
> **6. Total.** $J^i = L^i + S^i$ by [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^def-c1-12-3|Def. §C1.12.3]].
>
> **What the derivation shows**
> - ⚑ By-product: the Dirac field carries spin $\frac12$: $\frac12\boldsymbol\Sigma$ has $(\frac12\Sigma^i)(\frac12\Sigma^i) = \frac34\mathbb 1$, two spin-½ doublets, one per Weyl block. Peskin–Schroeder prove the particle's spin from this charge after quantization ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|Theorem §C5b.4.4]]).
> - Only $\mathbf J$ is conserved, not $\mathbf L$ and $\mathbf S$ separately: $\partial_\lambda\mathcal S^{\lambda\mu\nu} = T^{\nu\mu} - T^{\mu\nu} \ne 0$ ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-8|Theorem §C1.12.8]]).
> - Used next: the symmetric tensor (Theorem §C5a.4.14).

^der-c5a-4-13

*Uses:* [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-7|Theorem §C1.12.7]], [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^def-c1-12-3|Def. §C1.12.3]], [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]], [[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-3|Def. §C1.8.3]]

This is Quantum Mechanics' $\mathbf J = \mathbf L + \frac\hbar2\boldsymbol\Sigma$, conserved while $\mathbf L$ and $\mathbf S$ are not ([[§C13.2★ The Dirac Equation#^thm-c13-2-4|QM Theorem §C13.2.4]]), now as Noether charges of a field: there it follows from commutators with $H$, here from rotation invariance of the action (rule 2).

> [!theorem] Theorem §C5a.4.14: The Symmetric Energy–Momentum Tensor of the Dirac Field
> The Belinfante tensor ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-10|Theorem §C1.12.10]]) of the Dirac field is, on solutions,
>
> $$
> \hat T^{\mu\nu} = \frac i4\,\bar\psi\bigl(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu}\bigr)\psi - g^{\mu\nu}\mathcal L = \frac i4\,\bar\psi\bigl(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu}\bigr)\psi :
> $$
>
> with $a\overleftrightarrow{\partial}b = a\,\partial b - (\partial a)\,b$: symmetric, conserved, with the same $P^\nu$ as the canonical tensor ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-11|Theorem §C5a.4.11]]) and with orbital moments that give the total $J^{\nu\rho}$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-13|Theorem §C5a.4.13]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Derivation "Belinfante: symmetrizing T with the spin current", last sentence: the Dirac result, stated) · derived here from [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-10|Theorem §C1.12.10]]*

^thm-c5a-4-14

> [!derivation]- Derivation
> Work on solutions; write $V^\mu \equiv \frac i2\bar\psi\gamma^\mu\psi = \frac i2j^\mu$ and let $\gamma^{[\lambda\mu\nu]}$ be the totally antisymmetrized product, weight $1/3!$ ([[§C5a.7 Gamma-Matrix Technology#^def-c5a-7-1|Def. §C5a.7.1]]).
>
> **1. Split a product of three $\gamma$'s.** For all $\lambda, \mu, \nu$:
>
> $$
> \gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^{[\lambda\mu\nu]} + g^{\lambda\mu}\gamma^\nu - g^{\lambda\nu}\gamma^\mu + g^{\mu\nu}\gamma^\lambda .
> $$
>
> Check case by case, using only the Clifford algebra (distinct $\gamma$'s anticommute, $(\gamma^\lambda)^2 = g^{\lambda\lambda}$, no sum): all distinct, the antisymmetrization is the product itself (each of the six terms, reordered, carries its sign twice) and all $g$'s vanish; $\lambda = \mu \ne \nu$: left $g^{\lambda\lambda}\gamma^\nu$, right $0 + g^{\lambda\lambda}\gamma^\nu$; $\lambda = \nu \ne \mu$: left $\gamma^\lambda\gamma^\mu\gamma^\lambda = -g^{\lambda\lambda}\gamma^\mu$, right $-g^{\lambda\lambda}\gamma^\mu$; $\mu = \nu \ne \lambda$: both $g^{\mu\mu}\gamma^\lambda$; all equal: left $g^{\lambda\lambda}\gamma^\lambda$, right $g^{\lambda\lambda}\gamma^\lambda(1 - 1 + 1)$. (A repeated index kills the antisymmetrized product: its terms cancel in pairs.)
>
> **2. The spin current in pieces.** Subtract step 1 with $\mu \leftrightarrow \nu$: $\gamma^\lambda[\gamma^\mu, \gamma^\nu] = 2\gamma^{[\lambda\mu\nu]} + 2g^{\lambda\mu}\gamma^\nu - 2g^{\lambda\nu}\gamma^\mu$ (the $g^{\mu\nu}\gamma^\lambda$ terms cancel, the antisymmetric part doubles). With Theorem §C5a.4.13,
>
> $$
> \mathcal S^{\lambda\mu\nu} = A^{\lambda\mu\nu} + g^{\lambda\mu}V^\nu - g^{\lambda\nu}V^\mu, \qquad A^{\lambda\mu\nu} \equiv \tfrac i2\bar\psi\gamma^{[\lambda\mu\nu]}\psi \ \ \text{(totally antisymmetric)} .
> $$
>
> **3. Belinfante's $K$.** $K^{\lambda\mu\nu} = \frac12(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\mu\nu\lambda} + \mathcal S^{\nu\mu\lambda})$. The $A$ parts: $A^{\mu\nu\lambda} = A^{\lambda\mu\nu}$ (cyclic) and $A^{\nu\mu\lambda} = -A^{\lambda\mu\nu}$ (one transposition), total $A^{\lambda\mu\nu}$. The $V$ parts: $(g^{\lambda\mu}V^\nu - g^{\lambda\nu}V^\mu) + (g^{\mu\nu}V^\lambda - g^{\mu\lambda}V^\nu) + (g^{\nu\mu}V^\lambda - g^{\nu\lambda}V^\mu) = 2g^{\mu\nu}V^\lambda - 2g^{\lambda\nu}V^\mu$. Hence
>
> $$
> K^{\lambda\mu\nu} = \tfrac12A^{\lambda\mu\nu} + g^{\mu\nu}V^\lambda - g^{\lambda\nu}V^\mu ,
> $$
>
> antisymmetric in $\lambda\mu$ as it must be.
>
> **4. Its divergence.** $\partial_\lambda K^{\lambda\mu\nu} = \frac12\partial_\lambda A^{\lambda\mu\nu} + g^{\mu\nu}\partial_\lambda V^\lambda - \partial^\nu V^\mu$. The middle term vanishes on shell ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]]).
>
> **5. The vector piece symmetrizes the derivative.** $T^{\mu\nu} - \partial^\nu V^\mu = i\bar\psi\gamma^\mu\partial^\nu\psi - \frac i2(\partial^\nu\bar\psi)\gamma^\mu\psi - \frac i2\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L = \frac i2\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi - g^{\mu\nu}\mathcal L$.
>
> **6. The divergence of $A$.** Write $\gamma^{[\lambda\mu\nu]}$ by step 1 in two ways: $= \gamma^\lambda\gamma^\mu\gamma^\nu - g^{\lambda\mu}\gamma^\nu + g^{\lambda\nu}\gamma^\mu - g^{\mu\nu}\gamma^\lambda$ (for the term with $\partial_\lambda\bar\psi$), and, since $\gamma^{[\lambda\mu\nu]} = \gamma^{[\mu\nu\lambda]}$, $= \gamma^\mu\gamma^\nu\gamma^\lambda - g^{\mu\nu}\gamma^\lambda + g^{\mu\lambda}\gamma^\nu - g^{\nu\lambda}\gamma^\mu$ (for the term with $\partial_\lambda\psi$). With $(\partial_\lambda\bar\psi)\gamma^\lambda = im\bar\psi$ and $\gamma^\lambda\partial_\lambda\psi = -im\psi$:
>
> $$
> (\partial_\lambda\bar\psi)\gamma^{[\lambda\mu\nu]}\psi = im\bar\psi\gamma^\mu\gamma^\nu\psi - (\partial^\mu\bar\psi)\gamma^\nu\psi + (\partial^\nu\bar\psi)\gamma^\mu\psi - im\,g^{\mu\nu}\bar\psi\psi ,
> $$
>
> $$
> \bar\psi\gamma^{[\lambda\mu\nu]}\partial_\lambda\psi = -im\bar\psi\gamma^\mu\gamma^\nu\psi + im\,g^{\mu\nu}\bar\psi\psi + \bar\psi\gamma^\nu\partial^\mu\psi - \bar\psi\gamma^\mu\partial^\nu\psi .
> $$
>
> Adding, all four mass terms cancel: $\partial_\lambda(\bar\psi\gamma^{[\lambda\mu\nu]}\psi) = \bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi$, so $\frac12\partial_\lambda A^{\lambda\mu\nu} = \frac i4\bigl(\bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi\bigr)$.
>
> **7. Assemble.** $\hat T^{\mu\nu} = T^{\mu\nu} + \partial_\lambda K^{\lambda\mu\nu} = \frac i2\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi + \frac i4\bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \frac i4\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi - g^{\mu\nu}\mathcal L = \frac i4\bar\psi(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu})\psi - g^{\mu\nu}\mathcal L$, and $\mathcal L = 0$ on shell. Symmetric by inspection.
>
> **What the derivation shows**
> - The improvement has two parts: a vector part that turns $\overrightarrow\partial$ into $\frac12\overleftrightarrow\partial$ (the same as passing to $\mathcal L_{\rm sym}$, [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-7|Theorem §C5a.3.7]]), and the totally antisymmetric spin part, which removes the antisymmetric part of $T$.
> - ⚑ By-product: $\hat T^{00} = \frac i2\bar\psi\gamma^0\overleftrightarrow{\partial^0}\psi = \frac i2(\psi^\dagger\dot\psi - \dot\psi^\dagger\psi)$, real, and it differs from $T^{00}$ by a total derivative; $H$ is unchanged (property 3 of Theorem §C1.12.10, for fields falling off at infinity).
> - Both equations of motion and the conservation of $j^\mu$ were used; off shell $\hat T$ is not symmetric.
> - This is the tensor that couples to gravity ([[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum|§C1.12]]).

^der-c5a-4-14

*Uses:* [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-10|Theorem §C1.12.10]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.7 Gamma-Matrix Technology#^def-c5a-7-1|Def. §C5a.7.1]]

> [!remark]- Connections
> - The sixteen bilinears are the Dirac field's analogue of decomposing a two-index tensor into trace, antisymmetric and symmetric parts: $(\frac12, 0)\oplus(0, \frac12)$ tensored with its conjugate gives $(0,0)$ twice, $(\frac12,\frac12)$ twice and $(1,0)\oplus(0,1)$, i.e. S, P, V, A and T — [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-9|Theorem §C3.2.9]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]].
> - The tensor bilinear transforms like $F^{\mu\nu}$, and the Gordon identity shows it is the magnetic-moment part of the vector current, which gives $g = 2$ — [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-9|Theorem §C5a.7.9]], [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]].
> - The positive conserved density $\psi^\dagger\psi$ is Quantum Mechanics' probability density; in the field theory it is the time component of a Noether current, and after quantization a charge of either sign — [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]], [[§C1.11 Noether's Theorem#^thm-c1-11-5|Theorem §C1.11.5]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]].
> - Chirality is a property of the Lorentz representation, helicity of a state; the Weyl equation ties them for massless particles, which is why a single Weyl field realizes one helicity of Wigner's massless classification — [[§C3.6★ Massless Particles and Helicity#^thm-c3-6-6|Theorem §C3.6.6]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-14|Theorem §C5a.6.14]].
> - The spin current $\bar\psi\gamma^\lambda S^{\mu\nu}\psi$ is the field-theoretic origin of the electron's spin $\frac12$ and of the non-conservation of $\mathbf L$ alone; Belinfante's improvement moves the spin into a symmetric $\hat T$ — [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-8|Theorem §C1.12.8]], [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^thm-c1-12-10|Theorem §C1.12.10]], [[§C13.2★ The Dirac Equation#^thm-c13-2-4|QM Theorem §C13.2.4]].
> - Mass breaks chiral symmetry because it pairs left with right; the same statement in group language is that $\gamma^0$, the invariant form, swaps the Weyl blocks — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^rem-c5a-1-3|§C5a.1, Remark: Kinematics allows one handedness, a mass needs both]].
> - The same Noether procedure gave the scalar's U(1) current and $T^{\mu\nu}$; for the Dirac field every step is identical except that only $\psi$, not $\bar\psi$, has a derivative in $\mathcal L$ — [[P3 Noether's Procedure]], [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^rem-c1-12-2|§C1.12, Remark: The canonical tensor of the standard fields]].
