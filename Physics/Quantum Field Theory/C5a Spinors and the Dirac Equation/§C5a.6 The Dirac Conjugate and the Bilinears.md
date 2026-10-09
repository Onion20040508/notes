---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.5 Chirality and Weyl Spinors]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.7 The Dirac Equation and Its Lagrangian]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.7 (The Dirac conjugate), §8.9 (Fermion bilinears), §8.8 (reality of the bilinears), §8.10 · PHY 513 Lecture 8 (Larsen), Part B ("The Hermitean Conjugate Spinor", "The Dirac Conjugate Spinor") · Peskin & Schroeder, §3.2, p. 43, eqs. (3.32)–(3.33), §3.4, pp. 49–51, eqs. (3.68)–(3.76) · Yu Zhao-Huan, 量子场论讲义, §5.3, eqs. (5.83)–(5.101), (5.112)–(5.115) · the user's pre-course notes, §5.3.*

Which numbers built from two spinors do all observers agree on, and which Lorentz tensors can be built from a Dirac field? The Dirac form and the Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$ are layer 3 ([[§C5a.2 The Dirac Form|§C5a.2]]), the Lorentz action $\Lambda_{1/2}$ layers 4–5 ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]), the chirality projectors layer 6 ([[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]). This section puts them together: why $\psi^\dagger\psi$ is not a scalar, why the Dirac form is Lorentz invariant ($\Lambda_{1/2}$ is pseudo-unitary for $\gamma^0$), how $\bar\psi$ transforms, and the sixteen bilinears $\bar\psi\Gamma\chi$ with their transformation and reality. Their Weyl components are taken up with the two-component Dirac equation in [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]. The field equation and the Lagrangian built from them are [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; the Noether currents [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]]. The pseudo-unitarity of $\Lambda_{1/2}$ and the classification of the sixteen products are mathematics ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]), shown in the blocks below; this section keeps $\bar\psi$ and the bilinears of fields.

*Conventions* as in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]; $\psi$ a classical field with commuting components; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $a\overleftrightarrow{\partial}b \equiv a\,\partial b - (\partial a)\,b$.

## The mathematics used here

Why $\psi^\dagger\psi$ is not a scalar and $\bar\psi\psi$ is: the adjoints of the generators, the non-unitarity of finite-dimensional Lorentz representations, and the pseudo-unitarity of $\Lambda_{1/2}$, from which Theorem §C5a.6.1 follows:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-21]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-12]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13b]]

## Why ψ†ψ is not a scalar, and what is

> [!remark] Remark: Why ψ†ψ is not a scalar
> A Lagrangian must be a scalar, so $\psi$ needs a partner that transforms with $\Lambda_{1/2}^{-1}$. The quantum-mechanical candidate $\psi^\dagger$ transforms as $\psi^\dagger \to \psi^\dagger\Lambda_{1/2}^\dagger = \psi^\dagger\exp(+\frac i2\omega_{\mu\nu}S^{\mu\nu\dagger})$, which would be $\psi^\dagger\Lambda_{1/2}^{-1}$ if every $S^{\mu\nu}$ were Hermitian. The rotation generators $S^{ij}$ are; the boost generators $S^{0i}$ are anti-Hermitian ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]]). So $\Lambda_{1/2}$ is unitary on rotations and not on boosts, and $\psi^\dagger\psi$ is invariant under rotations only. This is not a defect of the basis: no finite-dimensional representation of the Lorentz group is unitary ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]]). Indeed $\psi^\dagger\psi$ will turn out to be the time component of the vector $\bar\psi\gamma^\mu\psi$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (opening paragraph; Derivation "Why $\psi^\dagger\psi$ fails", Step 1) · PHY 513 Lecture 8, Part B ("The Hermitean Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.83)–(5.85)*

^rem-c5a-6-1

> [!theorem] Theorem §C5a.6.1: The Dirac Conjugate Transforms with the Inverse
> If $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), its Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) transforms as
>
> $$
> \bar\psi'(x) = \bar\psi(\Lambda^{-1}x)\,\Lambda_{1/2}^{-1} ,
> $$
>
> and for any two Dirac fields $\psi$, $\chi$ the number $\bar\psi\chi = \psi^\dagger\gamma^0\chi$ is a Lorentz scalar field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]), $(\bar\psi'\chi')(x) = (\bar\psi\chi)(\Lambda^{-1}x)$. Moreover $(\bar\psi)^\dagger = \gamma^0\psi$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Derivation, Step 4; Definition "The Dirac conjugate") · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.33) · Yu §5.3, eqs. (5.91)–(5.92)*

^thm-c5a-6-1

> [!derivation]- Derivation
> Write $y = \Lambda^{-1}x$.
>
> **1. Conjugate the transformed field.** $\psi'(x)^\dagger = (\Lambda_{1/2}\psi(y))^\dagger = \psi(y)^\dagger\Lambda_{1/2}^\dagger$ (the adjoint reverses the product; $y$ is a real point, untouched).
>
> **2. Multiply by $\gamma^0$ and use Theorem §CB.17.13.** $\bar\psi'(x) = \psi(y)^\dagger\Lambda_{1/2}^\dagger\gamma^0 = \psi(y)^\dagger\gamma^0\Lambda_{1/2}^{-1} = \bar\psi(y)\Lambda_{1/2}^{-1}$.
>
> **3. The pairing.** $(\bar\psi'\chi')(x) = \bar\psi(y)\Lambda_{1/2}^{-1}\Lambda_{1/2}\chi(y) = \bar\psi(y)\chi(y)$: a one-component field whose value at $x$ is the old value at $\Lambda^{-1}x$, the scalar law of [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]].
>
> **4. The adjoint of $\bar\psi$.** $(\psi^\dagger\gamma^0)^\dagger = \gamma^{0\dagger}\psi = \gamma^0\psi$, with $\gamma^{0\dagger} = \gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]).
>
> **What the derivation shows**
> - $\bar\psi$ is an "inverse Dirac spinor": its column index is contracted, its row transforms with $\Lambda_{1/2}^{-1}$ from the right; the $\gamma^0$ converts the non-unitary $\Lambda_{1/2}^\dagger$ into $\Lambda_{1/2}^{-1}$ exactly on the boosts.
> - ⚑ By-product: $\bar\psi\psi$ is real ($(\psi^\dagger\gamma^0\psi)^* = \psi^\dagger\gamma^{0\dagger}\psi$) but not positive (step 7 of Derivation §CB.17.13); the positive $\psi^\dagger\psi$ is not invariant. A relativistic spinor field has no invariant positive density: the probability interpretation of Quantum Mechanics' $\Psi^\dagger\Psi$ ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]) survives only as the time component of a current.
> - Used next: the Lagrangian (Model §C5a.7.3) and every bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]).

^der-c5a-6-1

*Uses:* [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]

### The mathematics used here: bilinears

The covariance of $\bar\psi\Gamma\psi$ rests on the covariance of the Dirac matrices:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-16]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-16]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7b]]

The sixteen bilinears are built from the spinor generators, $\gamma^5$ and the sixteen products; as a representation the Clifford algebra is $\Lambda V$, and two-index tensors decompose as $(0,0)\oplus(1,0)\oplus(0,1)\oplus(1,1)$:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-13]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-14]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-8]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-8]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-14]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-14]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-12]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-12]]

The pseudoscalar and axial vector (Theorem §C5a.6.3) use that $\gamma^5$ commutes with every $\Lambda_{1/2}$:

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-4]]

## Bilinears

> [!definition] Definition §C5a.6.1: Fermion Bilinear
> A **fermion bilinear** is $\bar\psi\,\Gamma\,\chi$, with $\psi$, $\chi$ Dirac fields ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), $\bar\psi$ the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) (often $\chi = \psi$) and $\Gamma$ a constant $4\times4$ matrix, usually a product ("string") of $\gamma$ matrices. It is a number (row times matrix times column) and carries no spinor index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (opening) · PHY 513 Lecture 8, Part B ("Fermion Bilinears") · PS §3.4, p. 49 · Yu §5.3, after eq. (5.92)*

^def-c5a-6-1

> [!theorem] Theorem §C5a.6.2: Scalar, Vector and Tensor Bilinears
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; and likewise $\chi$), a bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]) transforms as $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$ does. In particular, with $y = \Lambda^{-1}x$,
>
> $$
> \bar\psi'\chi'(x) = \bar\psi\chi(y), \qquad \bar\psi'\gamma^\mu\chi'(x) = \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\chi(y), \qquad \bar\psi'[\gamma^\mu, \gamma^\nu]\chi'(x) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\,\bar\psi[\gamma^\rho, \gamma^\sigma]\chi(y) :
> $$
>
> a scalar, a vector and an antisymmetric tensor field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]). A string of $n$ $\gamma$'s gives an $n$-index tensor.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (Derivation "The first three bilinears") · PHY 513 Lecture 8, Part B · PS §3.4, p. 49 · Yu §5.3, eqs. (5.92), (5.94), (5.96)*

^thm-c5a-6-2

> [!derivation]- Derivation
> **1. General law.** By [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], $\bar\psi'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}$, and $\chi'(x) = \Lambda_{1/2}\chi(y)$. So $\bar\psi'\Gamma\chi'(x) = \bar\psi(y)\bigl(\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}\bigr)\chi(y)$.
>
> **2. Scalar, $\Gamma = \mathbb 1$.** $\Lambda_{1/2}^{-1}\Lambda_{1/2} = \mathbb 1$.
>
> **3. Vector, $\Gamma = \gamma^\mu$.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]); the number $\Lambda^\mu{}_\nu$ comes out of the bilinear.
>
> **4. Two $\gamma$'s.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ between them: $\Lambda_{1/2}^{-1}\gamma^\mu\gamma^\nu\Lambda_{1/2} = (\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2})(\Lambda_{1/2}^{-1}\gamma^\nu\Lambda_{1/2}) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\gamma^\rho\gamma^\sigma$. The same with $\mu \leftrightarrow \nu$, $\rho \leftrightarrow \sigma$ renamed, and subtracting: $\Lambda_{1/2}^{-1}[\gamma^\mu, \gamma^\nu]\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma[\gamma^\rho, \gamma^\sigma]$ (in the second product rename the dummies $\rho \leftrightarrow \sigma$ before subtracting).
>
> **5. $n$ $\gamma$'s.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ between every neighbouring pair: each $\gamma$ contributes one factor $\Lambda$.
>
> **What the derivation shows**
> - All spinor transformations cancel inside a bilinear; what is left is a tensor law fixed by the free indices of $\Gamma$. The symmetric combination $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ gives nothing new (the scalar times $g$).
> - ⚑ By-product: $\bar\psi[\gamma^\mu, \gamma^\nu]\psi$ transforms like $F^{\mu\nu}$, so $\bar\psi[\gamma^\mu, \gamma^\nu]\psi\,F_{\mu\nu}$ is a scalar: the structure of a magnetic-moment coupling ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]]).
> - The Lecture 8 slide "Fermion Bilinears" lists the scalar as $\bar\psi\gamma^\mu\psi$, repeating the vector; the scalar is $\bar\psi\psi$, with no free index.
> - Used next: the sixteen bilinears (Def. §C5a.6.2) and every current below.

^der-c5a-6-2

*Uses:* [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]

> [!definition] Definition §C5a.6.2: The Sixteen Bilinears
> With $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-13|Def. §CB.11.13]]) and
>
> $$
> \sigma^{\mu\nu} \equiv \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu} ,
> $$
>
> where $S^{\mu\nu}$ are the spinor generators ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15|Def. §CB.13.15]]; other normalizations of $\sigma^{\mu\nu}$: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|Caution: Three normalizations of σ^μν]]), the **standard bilinears** are
>
> | name | symbol | bilinear | number |
> |---|---|---|---|
> | scalar (S) | $\mathsf S$ | $\bar\psi\psi$ | 1 |
> | pseudoscalar (P) | $\mathsf P$ | $\bar\psi\,i\gamma^5\psi$ | 1 |
> | vector (V) | $\mathsf V^\mu$ | $\bar\psi\gamma^\mu\psi$ | 4 |
> | axial vector (A) | $\mathsf A^\mu$ | $\bar\psi\gamma^\mu\gamma^5\psi$ | 4 |
> | tensor (T) | $\mathsf T^{\mu\nu}$ | $\bar\psi\sigma^{\mu\nu}\psi$, $\mu < \nu$ | 6 |
>
> Their matrices $\mathbb 1, i\gamma^5, \gamma^\mu, \gamma^\mu\gamma^5, \sigma^{\mu\nu}$ are sixteen; they span all $4\times4$ matrices ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-8|Theorem §CB.11.8]]). The sans-serif symbols are Lecture 11's (slide 19); the conserved currents of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]] are $j^\mu = \mathsf V^\mu$ and $j^{\mu5} = \mathsf A^\mu$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (paragraph after the derivation), Ch. 9 §9.6 · PS §3.4, pp. 49–50 (table) · Yu §5.3, eqs. (5.93)–(5.96) · the user's pre-course notes, §5.3 · PHY 513 Lecture 11, slide 19 (the sans-serif symbols) · PHY 513, Problem Set 6, Problem 5(b) ($V^\mu = \bar\psi\gamma^\mu\psi$)*

^def-c5a-6-2

Reducing an arbitrary product of $\gamma$'s to these sixteen is [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]].

> [!caution] Caution: Three normalizations of σ^μν
> Peskin–Schroeder and this note: $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. The Lorentz generators: $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac12\sigma^{\mu\nu}$. Problem Set 5 writes $\sigma^{\mu\nu} = \frac{1}{4i}[\gamma^\mu, \gamma^\nu] = -S^{\mu\nu}$. Identities homogeneous in $\sigma$ (such as the duality [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|Theorem §C5a.11.7]]) hold in every normalization; identities mixing $\sigma$ with other terms (the Gordon identity, [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]]) do not. Peskin–Schroeder also write $\gamma^{\mu\nu} = \frac12[\gamma^\mu, \gamma^\nu] = -i\sigma^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$", last sentence) · PHY 513, Problem Set 5, Problem 5(d) statement · PS §3.4, p. 49*

^cau-c5a-6-1

> [!theorem] Theorem §C5a.6.3: Pseudoscalar and Axial Vector under Proper Lorentz Transformations
> Under $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), the pseudoscalar and axial bilinears of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]] obey
>
> $$
> \bar\psi\,i\gamma^5\psi \;\to\; \bar\psi\,i\gamma^5\psi, \qquad \bar\psi\gamma^\mu\gamma^5\psi \;\to\; \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\gamma^5\psi \qquad (\text{at } \Lambda^{-1}x) :
> $$
>
> for proper orthochronous $\Lambda$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]) they transform exactly as a scalar and a vector. They differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ only by a sign under parity ([[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]]).
>
> *Source: PS §3.4, p. 50 ("pseudo-vector and pseudo-scalar") · Yu §5.3, eqs. (5.93), (5.95) · the user's PHY 513 notes, Ch. 8 §8.9 (closing paragraph)*

^thm-c5a-6-3

> [!derivation]- Derivation
> **1. $\gamma^5$ is invariant.** $\gamma^5$ commutes with every $S^{\mu\nu}$, hence with $\Lambda_{1/2} = \exp(-\frac i2\omega S)$ and its inverse: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4|Theorem §CB.17.4]], 1).
>
> **2. Pseudoscalar.** Step 1 of Derivation §C5a.6.2 with $\Gamma = i\gamma^5$: $\Lambda_{1/2}^{-1}i\gamma^5\Lambda_{1/2} = i\gamma^5$.
>
> **3. Axial vector.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$: $\Lambda_{1/2}^{-1}\gamma^\mu\gamma^5\Lambda_{1/2} = (\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2})(\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2}) = \Lambda^\mu{}_\nu\gamma^\nu\gamma^5$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]] and step 1).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ comes from the identity component only, so it cannot see the "pseudo": $\gamma^5 \propto \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]]) carries one $\varepsilon$, which is invariant under $\det\Lambda = +1$ and odd under parity ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
> - Used next: the axial current (Theorem §C5a.8.4).

^der-c5a-6-3

*Uses:* [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4|Theorem §CB.17.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]

> [!theorem] Theorem §C5a.6.4: The Bilinears Are Real
> For any bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]) of commuting components, $(\bar\psi\Gamma\psi)^* = \bar\psi\,\bar\Gamma\,\psi$ with $\bar\Gamma \equiv \gamma^0\Gamma^\dagger\gamma^0$. For the five standard matrices of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], $\bar\Gamma = \Gamma$:
>
> $$
> \bar\psi\psi,\quad \bar\psi\,i\gamma^5\psi,\quad \bar\psi\gamma^\mu\psi,\quad \bar\psi\gamma^\mu\gamma^5\psi,\quad \bar\psi\sigma^{\mu\nu}\psi \quad\text{are real},
> $$
>
> while $\bar\psi\gamma^5\psi$ is imaginary.
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the user's PHY 513 notes, Ch. 8 §8.8 ("Yu (5.97)–(5.101) give the reality of the bilinears") · the user's pre-course notes, §5.3*

^thm-c5a-6-4

> [!derivation]- Derivation
> **1. General.** A bilinear is a $1\times1$ matrix, so its complex conjugate is its adjoint: $(\psi^\dagger\gamma^0\Gamma\psi)^\dagger = \psi^\dagger\Gamma^\dagger\gamma^{0\dagger}\psi = \psi^\dagger\Gamma^\dagger\gamma^0\psi$. Insert $(\gamma^0)^2 = \mathbb 1$ in front: $= \psi^\dagger\gamma^0(\gamma^0\Gamma^\dagger\gamma^0)\psi = \bar\psi\bar\Gamma\psi$.
>
> **2. The five matrices.** Use $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]), $\gamma^{5\dagger} = \gamma^5$ and $\gamma^0\gamma^5 = -\gamma^5\gamma^0$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]]):
> - $\Gamma = \mathbb 1$: $\gamma^0\gamma^0 = \mathbb 1$.
> - $\Gamma = \gamma^\mu$: $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^0\gamma^\mu\gamma^0\gamma^0 = \gamma^\mu$.
> - $\Gamma = i\gamma^5$: $(i\gamma^5)^\dagger = -i\gamma^5$; $\gamma^0(-i\gamma^5)\gamma^0 = -i(-\gamma^5\gamma^0)\gamma^0 = i\gamma^5$.
> - $\Gamma = \gamma^\mu\gamma^5$: $(\gamma^\mu\gamma^5)^\dagger = \gamma^5\gamma^{\mu\dagger}$; $\gamma^0\gamma^5\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^0\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^\mu = \gamma^\mu\gamma^5$ (anticommute once more).
> - $\Gamma = \sigma^{\mu\nu}$: $\sigma^{\mu\nu\dagger} = -\frac i2[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$; sandwiching, $\gamma^0\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^{\nu\dagger}\gamma^0\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\nu\gamma^\mu$, so $\bar\sigma^{\mu\nu} = -\frac i2[\gamma^\nu, \gamma^\mu] = \sigma^{\mu\nu}$.
>
> **3. Without the $i$.** For $\Gamma = \gamma^5$, $\bar\Gamma = \gamma^0\gamma^5\gamma^0 = -\gamma^5$, so $(\bar\psi\gamma^5\psi)^{\ast} = -\bar\psi\gamma^5\psi$. ⚑ By-product: the $i$ in the pseudoscalar is the reality convention, as the $i$ in the Lagrangian is ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|§C5a.7, Remark: Why the i]]).
>
> **What the derivation shows**
> - The bar operation $\Gamma \mapsto \gamma^0\Gamma^\dagger\gamma^0$ is the adjoint with respect to the indefinite form $\gamma^0$ of [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]]; the standard basis is chosen self-adjoint.
> - Step 1 used only $(AB)^\dagger = B^\dagger A^\dagger$, valid also for operator-valued components: the quantized bilinears are Hermitian ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).

^der-c5a-6-4

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]]

> [!remark] Remark: The quantized bilinears are Hermitian
> After quantization the same computation makes the five standard bilinears of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]] Hermitian operators, once the product of two field operators at one point is defined by normal ordering ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]) and smeared with a test function (operator-valued distributions, [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]): step 1 of the derivation used only $(AB)^\dagger = B^\dagger A^\dagger$.
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the operator reading written here*

^rem-c5a-6-2

> [!remark]- Connections
> - $\gamma^0$ is to the Dirac spinor slot what $g_{\mu\nu}$ is to a vector slot: both are indefinite forms preserved by the group, and both are needed because the Lorentz group is noncompact — [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]].
> - The sixteen bilinears are the Dirac field's analogue of decomposing a two-index tensor into trace, antisymmetric and symmetric parts: $(\frac12, 0)\oplus(0, \frac12)$ tensored with its conjugate gives $(0,0)$ twice, $(\frac12,\frac12)$ twice and $(1,0)\oplus(0,1)$, i.e. S, P, V, A and T — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-12|Theorem §CB.17.12]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]].
> - The tensor bilinear transforms like $F^{\mu\nu}$, and the Gordon identity shows it is the magnetic-moment part of the vector current, which gives $g = 2$ — [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]], [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]].
> - The invariance of $\bar\psi\chi$ is the invariance of the Dirac form of [[§C5a.2 The Dirac Form|§C5a.2]] under $\Lambda_{1/2}$, as $g(v, w)$ is invariant under $\Lambda$ — [[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-15|Def. §CB.12.15]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]].
