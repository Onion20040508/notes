---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.3 The Dirac Equation and Its Lagrangian]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.9 (Fermion bilinears), §8.10 (The Weyl form of the Dirac equation), §8.8 (reality of the bilinears), Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PHY 513 Lecture 8 (Larsen), Parts B–C · Peskin & Schroeder, §3.2, pp. 43–44, eqs. (3.36)–(3.44), §3.4, pp. 49–51, eqs. (3.68)–(3.76) · Yu Zhao-Huan, 量子场论讲义, §5.3, eqs. (5.93)–(5.101), (5.112)–(5.115) · the user's pre-course notes, §5.3 (Weyl spinors).*

Which Lorentz tensors can be built from a Dirac field, and how does the field split into a left- and a right-handed half? The Dirac conjugate and the Lagrangian are [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]; $\gamma^5$, its algebra and the Weyl halves of the Dirac representation are [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-7|Def. §C5a.2.7]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]] and [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]. This section adds the bilinears and their transformation, the chirality projectors, the Dirac equation in two-component form and the Weyl equations. The Noether currents built from these bilinears (vector, axial, energy–momentum, spin) are [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field|§C5a.5]].

*Conventions* as in [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]; $\psi$ a classical field with commuting components; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $a\overleftrightarrow{\partial}b \equiv a\,\partial b - (\partial a)\,b$.

## Bilinears

> [!definition] Definition §C5a.4.1: Fermion Bilinear
> A **fermion bilinear** is $\bar\psi\,\Gamma\,\chi$, with $\psi$, $\chi$ Dirac fields ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]), $\bar\psi$ the Dirac conjugate ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) (often $\chi = \psi$) and $\Gamma$ a constant $4\times4$ matrix, usually a product ("string") of $\gamma$ matrices. It is a number (row times matrix times column) and carries no spinor index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (opening) · PHY 513 Lecture 8, Part B ("Fermion Bilinears") · PS §3.4, p. 49 · Yu §5.3, after eq. (5.92)*

^def-c5a-4-1

> [!theorem] Theorem §C5a.4.1: Scalar, Vector and Tensor Bilinears
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]; and likewise $\chi$), a bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]]) transforms as $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$ does. In particular, with $y = \Lambda^{-1}x$,
>
> $$
> \bar\psi'\chi'(x) = \bar\psi\chi(y), \qquad \bar\psi'\gamma^\mu\chi'(x) = \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\chi(y), \qquad \bar\psi'[\gamma^\mu, \gamma^\nu]\chi'(x) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\,\bar\psi[\gamma^\rho, \gamma^\sigma]\chi(y) :
> $$
>
> a scalar, a vector and an antisymmetric tensor field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]]). A string of $n$ $\gamma$'s gives an $n$-index tensor.
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
> - ⚑ By-product: $\bar\psi[\gamma^\mu, \gamma^\nu]\psi$ transforms like $F^{\mu\nu}$, so $\bar\psi[\gamma^\mu, \gamma^\nu]\psi\,F_{\mu\nu}$ is a scalar: the structure of a magnetic-moment coupling ([[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-9|Theorem §C5a.8.9]]).
> - The Lecture 8 slide "Fermion Bilinears" lists the scalar as $\bar\psi\gamma^\mu\psi$, repeating the vector; the scalar is $\bar\psi\psi$, with no free index.
> - Used next: the sixteen bilinears (Def. §C5a.4.2) and every current below.

^der-c5a-4-1

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]

> [!definition] Definition §C5a.4.2: The Sixteen Bilinears
> With $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-7|Def. §C5a.2.7]]) and
>
> $$
> \sigma^{\mu\nu} \equiv \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu} ,
> $$
>
> where $S^{\mu\nu}$ are the spinor generators ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]; other normalizations of $\sigma^{\mu\nu}$: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^cau-c5a-4-1|Caution: Three normalizations of σ^μν]]), the **standard bilinears** are
>
> | name | bilinear | number |
> |---|---|---|
> | scalar (S) | $\bar\psi\psi$ | 1 |
> | pseudoscalar (P) | $\bar\psi\,i\gamma^5\psi$ | 1 |
> | vector (V) | $\bar\psi\gamma^\mu\psi$ | 4 |
> | axial vector (A) | $\bar\psi\gamma^\mu\gamma^5\psi$ | 4 |
> | tensor (T) | $\bar\psi\sigma^{\mu\nu}\psi$, $\mu < \nu$ | 6 |
>
> Their matrices $\mathbb 1, i\gamma^5, \gamma^\mu, \gamma^\mu\gamma^5, \sigma^{\mu\nu}$ are sixteen; they span all $4\times4$ matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (paragraph after the derivation), Ch. 9 §9.6 · PS §3.4, pp. 49–50 (table) · Yu §5.3, eqs. (5.93)–(5.96) · the user's pre-course notes, §5.3*

^def-c5a-4-2

Reducing an arbitrary product of $\gamma$'s to these sixteen is [[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-8|Theorem §C5a.8.8]].

> [!caution] Caution: Three normalizations of σ^μν
> Peskin–Schroeder and this note: $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. The Lorentz generators: $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac12\sigma^{\mu\nu}$. Problem Set 5 writes $\sigma^{\mu\nu} = \frac{1}{4i}[\gamma^\mu, \gamma^\nu] = -S^{\mu\nu}$. Identities homogeneous in $\sigma$ (such as the duality [[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-7|Theorem §C5a.8.7]]) hold in every normalization; identities mixing $\sigma$ with other terms (the Gordon identity, [[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-9|Theorem §C5a.8.9]]) do not. Peskin–Schroeder also write $\gamma^{\mu\nu} = \frac12[\gamma^\mu, \gamma^\nu] = -i\sigma^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$", last sentence) · PHY 513, Problem Set 5, Problem 5(d) statement · PS §3.4, p. 49*

^cau-c5a-4-1

> [!theorem] Theorem §C5a.4.2: Pseudoscalar and Axial Vector under Proper Lorentz Transformations
> Under $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]]), the pseudoscalar and axial bilinears of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]] obey
>
> $$
> \bar\psi\,i\gamma^5\psi \;\to\; \bar\psi\,i\gamma^5\psi, \qquad \bar\psi\gamma^\mu\gamma^5\psi \;\to\; \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\gamma^5\psi \qquad (\text{at } \Lambda^{-1}x) :
> $$
>
> for proper orthochronous $\Lambda$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]) they transform exactly as a scalar and a vector. They differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ only by a sign under parity (QFT C9, planned).
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
> - $\Lambda_{1/2}$ comes from the identity component only, so it cannot see the "pseudo": $\gamma^5 \propto \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ ([[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-5|Theorem §C5a.8.5]]) carries one $\varepsilon$, which is invariant under $\det\Lambda = +1$ and odd under parity ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
> - Used next: the axial current (Theorem §C5a.5.4).

^der-c5a-4-2

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]]

> [!theorem] Theorem §C5a.4.3: The Bilinears Are Real
> For any bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]]) of commuting components, $(\bar\psi\Gamma\psi)^* = \bar\psi\,\bar\Gamma\,\psi$ with $\bar\Gamma \equiv \gamma^0\Gamma^\dagger\gamma^0$. For the five standard matrices of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-2|Def. §C5a.4.2]], $\bar\Gamma = \Gamma$:
>
> $$
> \bar\psi\psi,\quad \bar\psi\,i\gamma^5\psi,\quad \bar\psi\gamma^\mu\psi,\quad \bar\psi\gamma^\mu\gamma^5\psi,\quad \bar\psi\sigma^{\mu\nu}\psi \quad\text{are real},
> $$
>
> while $\bar\psi\gamma^5\psi$ is imaginary.
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

> [!remark] Remark: The quantized bilinears are Hermitian
> After quantization the same computation makes the five standard bilinears of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]] Hermitian operators, once the product of two field operators at one point is defined by normal ordering ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]) and smeared with a test function (operator-valued distributions, [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]): step 1 of the derivation used only $(AB)^\dagger = B^\dagger A^\dagger$.
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the operator reading written here*

^rem-c5a-4-1

## Chirality

> [!definition] Definition §C5a.4.3: Chirality Projectors
> $$
> P_L \equiv \tfrac12\bigl(\mathbb 1 - \gamma^5\bigr), \qquad P_R \equiv \tfrac12\bigl(\mathbb 1 + \gamma^5\bigr) .
> $$
>
> With $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-7|Def. §C5a.2.7]]: a Dirac spinor with $\gamma^5\psi = -\psi$ ($P_L\psi = \psi$) has **left-handed chirality**, one with $\gamma^5\psi = +\psi$ right-handed. In the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]), where $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-14|Theorem §C5a.2.14]]), $P_L\psi = (\psi_L, 0)$ and $P_R\psi = (0, \psi_R)$ for $\psi = (\psi_L, \psi_R)$, the Weyl halves of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]].
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Definition "The matrix $\gamma^5$") · PS §3.4, eqs. (3.72), (3.76) · Yu §5.1 ($\gamma^5$), §5.3, eq. (5.112)*

^def-c5a-4-3

The same letters denote the two-component Weyl spinors $\psi_L$, $\psi_R$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-9|Theorem §C5a.2.9]]) and, by abuse, the four-component $P_L\psi$, $P_R\psi$; context decides. Chirality is the eigenvalue of $\gamma^5$, a property of the representation; helicity is the spin along the momentum, a property of a state. They agree only for massless positive-frequency solutions (Theorem §C5a.4.8; [[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-14|Theorem §C5a.7.14]]).

> [!theorem] Theorem §C5a.4.4: Properties of the Chirality Projectors
> 1. $P_L^2 = P_L$, $P_R^2 = P_R$, $P_LP_R = P_RP_L = 0$, $P_L + P_R = \mathbb 1$.
> 2. $P_L\gamma^\mu = \gamma^\mu P_R$ and $P_R\gamma^\mu = \gamma^\mu P_L$.
> 3. $[P_{L,R}, S^{\mu\nu}] = 0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]), so $P_{L,R}\Lambda_{1/2} = \Lambda_{1/2}P_{L,R}$: chirality is Lorentz invariant, and $P_L\psi$, $P_R\psi$ transform separately.
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
> A **left-handed Weyl field** is a two-component field $\psi_L$ in $(\frac12, 0)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]]; Weyl matrices [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-2|Def. §C5a.1.2]]) with
>
> $$
> \mathcal L_L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L, \qquad i\bar\sigma^\mu\partial_\mu\psi_L = 0 ;
> $$
>
> a **right-handed Weyl field** $\psi_R$ in $(0, \frac12)$ has $\mathcal L_R = i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = 0$. These are the **Weyl equations**.
>
> *Assumptions:* $m = 0$ (the two blocks of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]] decouple, and either may be kept alone, consistently both as a representation and dynamically); classical, free; no parity symmetry (parity exchanges the two, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]]).
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations", eq. (weyl)) · PHY 513 Lecture 8, Part C ("Weyl Equation") · PS §3.2, eqs. (3.40), (3.44) · Yu §5.3, eq. (5.115)*

^mod-c5a-4-7

The 513 notes box the Weyl equations as a principle; here they are a model, the massless idealization of the Dirac theory (or, in the Standard Model, the starting point). Each component of a Weyl solution obeys the massless Klein–Gordon equation, by $(\sigma\cdot\partial)(\bar\sigma\cdot\partial) = \partial^2$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-1|Theorem §C5a.1.1]]), the two-component version of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]].

> [!theorem] Theorem §C5a.4.8: Weyl Plane Waves Have Fixed Helicity
> Let $\psi_L = \xi\,e^{-ip\cdot x}$ with $p^0 > 0$ and a constant nonzero two-spinor $\xi$. It solves the left-handed Weyl equation ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]]) if and only if $p^2 = 0$ ($p^0 = \lvert\mathbf p\rvert$) and
>
> $$
> \bigl(\hat{\mathbf p}\cdot\boldsymbol\sigma\bigr)\,\xi = -\xi :
> $$
>
> helicity ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]) $h = \hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2 = -\frac12$. For $\psi_R = \eta\,e^{-ip\cdot x}$, $p^2 = 0$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$, $h = +\frac12$. One Weyl field has one helicity for its positive-frequency solutions.
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
> **6. Helicity.** For spin $\frac12$ the spin operator in each Weyl block is $\frac12\boldsymbol\sigma$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]), so the spin along $\hat{\mathbf p}$ is $\hat{\mathbf p}\cdot\boldsymbol\sigma/2 = \mp\frac12$ ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]).
>
> **What the derivation shows**
> - Chirality and helicity coincide for massless positive-frequency solutions: left-handed means helicity $-\frac12$. For the negative-frequency solutions $\xi\,e^{+ip\cdot x}$ the condition is the same, $(p^0 + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$ (step 1 with $p \to -p$ gives $-(\bar\sigma\cdot p)\xi = 0$); after quantization they describe the antiparticle, which carries the opposite helicity $+\frac12$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]): the neutrino–antineutrino pair of [[§C3.7★ Massless Particles and Helicity|§C3.7★]].
> - ⚑ By-product: half the components of a Weyl spinor are removed for each momentum; a Weyl field has one physical polarization per momentum, the minimal content of a massless spin-½ particle (the little-group count of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
> - For massive Dirac spinors helicity is frame dependent; it approaches chirality at high energy ([[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-14|Theorem §C5a.7.14]]).
> - Assumption: the plane wave solves the Weyl equation pointwise; as a field on spacetime it is not square integrable but a tempered distribution, and the equation holds also in $\mathcal S'$, as for the Dirac plane waves ([[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-6|§C5a.3, Remark: In what sense the equations hold]]).

^der-c5a-4-8

*Uses:* [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^mod-c5a-4-7|Model §C5a.4.7]], [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]

> [!remark] Remark: When the Weyl description is useful
> Not for the electron of Dirac's problem: in hydrogen the electron's kinetic energy is tiny compared with its mass, and the mass couples the two halves at full strength. It is natural where the mass is zero or small, as for neutrinos: in the Standard Model the neutrinos are massless and only left-handed ones exist. Their observed small masses require going beyond it. A mass of the form of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-6|Theorem §C5a.4.6]], a *Dirac* mass, needs a separate right-handed field.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (paragraph "When is the Weyl description useful?") · PHY 513 Lecture 8, Part C*

^rem-c5a-4-2

> [!remark]- ★ Remark: A Majorana mass needs no second field
> By [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-8|Theorem §C3.3.8]] and [[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-11|Theorem §C5a.1.11]], $\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, so a single left-handed field can supply its own partner: $\psi_L^{\mathsf T}\varepsilon\,\psi_L$ is Lorentz invariant, because $\Lambda_L^{\mathsf T}\varepsilon\Lambda_L = (\det\Lambda_L)\varepsilon = \varepsilon$ ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-10|Theorem §C5a.1.10]]). This is a *Majorana* mass. For commuting components it vanishes identically, $\psi^{\mathsf T}\varepsilon\psi = \psi_1\psi_2 - \psi_2\psi_1 = 0$ (with $\varepsilon^{12} = 1$); it exists only for anticommuting fields ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]; Majorana fields, QFT C9, planned). Whether neutrino masses are of Dirac or Majorana type is not known.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Caution "'A neutrino mass needs a right-handed neutrino'")*

^rem-c5a-4-3

> [!remark]- Connections
> - The sixteen bilinears are the Dirac field's analogue of decomposing a two-index tensor into trace, antisymmetric and symmetric parts: $(\frac12, 0)\oplus(0, \frac12)$ tensored with its conjugate gives $(0,0)$ twice, $(\frac12,\frac12)$ twice and $(1,0)\oplus(0,1)$, i.e. S, P, V, A and T — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]].
> - The tensor bilinear transforms like $F^{\mu\nu}$, and the Gordon identity shows it is the magnetic-moment part of the vector current, which gives $g = 2$ — [[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-9|Theorem §C5a.8.9]], [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]].
> - Chirality is a property of the Lorentz representation, helicity of a state; the Weyl equation ties them for massless particles, which is why a single Weyl field realizes one helicity of Wigner's massless classification — [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]], [[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-14|Theorem §C5a.7.14]].
> - Mass breaks chiral symmetry because it pairs left with right; the same statement in group language is that $\gamma^0$, the invariant form, swaps the Weyl blocks — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.1 Weyl Spinors and SL(2,C)#^rem-c5a-1-3|§C5a.1, Remark: Kinematics allows one handedness, a mass needs both]].
