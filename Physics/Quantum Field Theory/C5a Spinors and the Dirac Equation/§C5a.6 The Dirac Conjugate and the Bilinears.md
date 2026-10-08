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

Which numbers built from two spinors do all observers agree on, and which Lorentz tensors can be built from a Dirac field? The Dirac form and the Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$ are layer 3 ([[§C5a.2 The Dirac Form|§C5a.2]]), the Lorentz action $\Lambda_{1/2}$ layers 4–5 ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]), the chirality projectors layer 6 ([[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]). This section puts them together: why $\psi^\dagger\psi$ is not a scalar, why the Dirac form is Lorentz invariant ($\Lambda_{1/2}$ is pseudo-unitary for $\gamma^0$), how $\bar\psi$ transforms, and the sixteen bilinears $\bar\psi\Gamma\chi$ with their transformation and reality. Their Weyl components are taken up with the two-component Dirac equation in [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]. The field equation and the Lagrangian built from them are [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; the Noether currents [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]].

*Conventions* as in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]; $\psi$ a classical field with commuting components; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $a\overleftrightarrow{\partial}b \equiv a\,\partial b - (\partial a)\,b$.

## Why ψ†ψ is not a scalar, and what is

> [!remark] Remark: Why ψ†ψ is not a scalar
> A Lagrangian must be a scalar, so $\psi$ needs a partner that transforms with $\Lambda_{1/2}^{-1}$. The quantum-mechanical candidate $\psi^\dagger$ transforms as $\psi^\dagger \to \psi^\dagger\Lambda_{1/2}^\dagger = \psi^\dagger\exp(+\frac i2\omega_{\mu\nu}S^{\mu\nu\dagger})$, which would be $\psi^\dagger\Lambda_{1/2}^{-1}$ if every $S^{\mu\nu}$ were Hermitian. The rotation generators $S^{ij}$ are; the boost generators $S^{0i}$ are anti-Hermitian ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]]). So $\Lambda_{1/2}$ is unitary on rotations and not on boosts, and $\psi^\dagger\psi$ is invariant under rotations only. This is not a defect of the basis: no finite-dimensional representation of the Lorentz group is unitary ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]). Indeed $\psi^\dagger\psi$ will turn out to be the time component of the vector $\bar\psi\gamma^\mu\psi$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (opening paragraph; Derivation "Why $\psi^\dagger\psi$ fails", Step 1) · PHY 513 Lecture 8, Part B ("The Hermitean Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.83)–(5.85)*

^rem-c5a-6-1

> [!theorem] Theorem §C5a.6.1: Λ½ Is Pseudo-Unitary
> For every real $\omega_{\mu\nu}$, the Dirac-representation matrix $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) and $\gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) satisfy
>
> $$
> \Lambda_{1/2}^\dagger\,\gamma^0 = \gamma^0\,\Lambda_{1/2}^{-1}, \qquad\text{equivalently}\qquad \Lambda_{1/2}^\dagger\,\gamma^0\,\Lambda_{1/2} = \gamma^0, \qquad \Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0 .
> $$
>
> $\gamma^0$ is a Hermitian form on $\mathbb C^4$ preserved by every $\Lambda_{1/2}$; it is indefinite, with eigenvalues $+1$, $+1$, $-1$, $-1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary)), §8.7 (Derivation "Why $\psi^\dagger\psi$ fails, and how $\gamma^0$ repairs it: the lecture's route", Steps 2–3, eq. (gammaSdagger)) · PHY 513 Lecture 8, Part B ("The Dirac Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.86)–(5.89)*

^thm-c5a-6-1

> [!derivation]- Derivation (the lecture's route: which generators γ⁰ commutes with)
> **1. $\gamma^0$ commutes with $S^{ij}$.** For $i \ne j$, $[\gamma^i, \gamma^j] = 2\gamma^i\gamma^j$ (distinct $\gamma$'s anticommute, [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]]), so $S^{ij} = \frac i2\gamma^i\gamma^j$. Moving $\gamma^0$ through $\gamma^i$ and then $\gamma^j$ costs two signs: $\gamma^0\gamma^i\gamma^j = (-\gamma^i\gamma^0)\gamma^j = \gamma^i\gamma^j\gamma^0$. Hence $\gamma^0S^{ij} = S^{ij}\gamma^0$.
>
> **2. $\gamma^0$ anticommutes with $S^{0i}$.** $S^{0i} = \frac i2\gamma^0\gamma^i$. Then $\gamma^0S^{0i} = \frac i2(\gamma^0)^2\gamma^i = \frac i2\gamma^i$, using $(\gamma^0)^2 = \mathbb 1$; and $S^{0i}\gamma^0 = \frac i2\gamma^0\gamma^i\gamma^0 = \frac i2\gamma^0(-\gamma^0\gamma^i) = -\frac i2\gamma^i$. Hence $\gamma^0S^{0i} = -S^{0i}\gamma^0$.
>
> **3. Combine with the Hermiticity pattern.** By [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], $S^{ij\dagger} = S^{ij}$ and $S^{0i\dagger} = -S^{0i}$. Therefore $S^{ij\dagger}\gamma^0 = S^{ij}\gamma^0 = \gamma^0S^{ij}$ (step 1) and $S^{0i\dagger}\gamma^0 = -S^{0i}\gamma^0 = \gamma^0S^{0i}$ (step 2). In every case
>
> $$
> S^{\mu\nu\dagger}\,\gamma^0 = \gamma^0\,S^{\mu\nu} :
> $$
>
> the generators that fail to be Hermitian are exactly those that anticommute with $\gamma^0$, so the two signs cancel.
>
> **4. The exponent.** Let $X = \omega_{\mu\nu}S^{\mu\nu}$ (summed). Since the $\omega_{\mu\nu}$ are real, $X^\dagger = \omega_{\mu\nu}S^{\mu\nu\dagger}$, and step 3 gives $X^\dagger\gamma^0 = \gamma^0X$. By induction on $n$, $(X^\dagger)^n\gamma^0 = (X^\dagger)^{n-1}\gamma^0X = \cdots = \gamma^0X^n$.
>
> **5. The series.** $\Lambda_{1/2} = \exp(-\frac i2X)$, and the adjoint of a norm-convergent series is the series of adjoints, so $\Lambda_{1/2}^\dagger = \exp(+\frac i2X^\dagger)$. Term by term with step 4,
>
> $$
> \Lambda_{1/2}^\dagger\gamma^0 = \sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^n(X^\dagger)^n\gamma^0 = \gamma^0\sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^nX^n = \gamma^0\exp\Bigl(+\frac i2X\Bigr) = \gamma^0\Lambda_{1/2}^{-1} ,
> $$
>
> the last step because $\exp(\frac i2X)\exp(-\frac i2X) = \mathbb 1$ ($X$ commutes with itself).
>
> **6. The other forms.** Multiply step 5 by $\Lambda_{1/2}$ on the right: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$. Multiply step 5 by $\gamma^0$ on the right and use $(\gamma^0)^2 = \mathbb 1$: $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$.
>
> **7. The form is indefinite.** $\gamma^0$ is Hermitian with $(\gamma^0)^2 = \mathbb 1$, so its eigenvalues are $\pm1$; it is traceless ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]), so each occurs twice. In the chiral basis $\gamma^0$ swaps the upper and lower blocks, with eigenvectors $(\xi, \xi)$ and $(\xi, -\xi)$. ⚑ By-product: $\psi^\dagger\gamma^0\psi$ can have either sign; the invariant of a Dirac spinor is not a norm → [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]] (it pairs left- with right-handed components).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ preserves the Hermitian form $\gamma^0$ as $\Lambda$ preserves $g$ ($\Lambda^{\mathsf T}g\Lambda = g$): $\gamma^0$ plays the role of the metric for the Dirac spinor slot; both forms are indefinite.
> - ⚑ By-product: the sign ambiguity $\pm\Lambda_{1/2}$ cancels in $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2}$.
> - Used next: the Dirac conjugate (Def. §C5a.2.5, Theorem §C5a.6.2).

^der-c5a-6-1

> [!derivation]- Derivation (second route: from the Hermiticity of the γ's)
> **1.** By [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; multiplying by $\gamma^0$ on the right, $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$.
>
> **2.** $S^{\mu\nu\dagger} = (\frac i4[\gamma^\mu, \gamma^\nu])^\dagger = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}] = -\frac i4\bigl(\gamma^{\nu\dagger}\gamma^{\mu\dagger} - \gamma^{\mu\dagger}\gamma^{\nu\dagger}\bigr)$ (the adjoint reverses products and conjugates $i$).
>
> **3.** Multiply on the right by $\gamma^0$ and push it left with step 1, twice in each product: $\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^{\nu\dagger}\gamma^0\gamma^\mu = \gamma^0\gamma^\nu\gamma^\mu$. Hence $S^{\mu\nu\dagger}\gamma^0 = -\frac i4\gamma^0(\gamma^\nu\gamma^\mu - \gamma^\mu\gamma^\nu) = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu] = \gamma^0S^{\mu\nu}$, step 3 of the first route.
>
> **4.** Steps 4–6 of the first route follow unchanged.
>
> **What the derivation shows**
> - No explicit matrices and no case split between rotations and boosts: the result follows from $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ alone, hence holds in every basis in which that relation holds (every unitary change of the chiral basis, [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-12|Theorem §C5a.1.12]]).

^der-c5a-6-1b

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]

> [!theorem] Theorem §C5a.6.2: The Dirac Conjugate Transforms with the Inverse
> If $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), its Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]) transforms as
>
> $$
> \bar\psi'(x) = \bar\psi(\Lambda^{-1}x)\,\Lambda_{1/2}^{-1} ,
> $$
>
> and for any two Dirac fields $\psi$, $\chi$ the number $\bar\psi\chi = \psi^\dagger\gamma^0\chi$ is a Lorentz scalar field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]), $(\bar\psi'\chi')(x) = (\bar\psi\chi)(\Lambda^{-1}x)$. Moreover $(\bar\psi)^\dagger = \gamma^0\psi$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Derivation, Step 4; Definition "The Dirac conjugate") · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.33) · Yu §5.3, eqs. (5.91)–(5.92)*

^thm-c5a-6-2

> [!derivation]- Derivation
> Write $y = \Lambda^{-1}x$.
>
> **1. Conjugate the transformed field.** $\psi'(x)^\dagger = (\Lambda_{1/2}\psi(y))^\dagger = \psi(y)^\dagger\Lambda_{1/2}^\dagger$ (the adjoint reverses the product; $y$ is a real point, untouched).
>
> **2. Multiply by $\gamma^0$ and use Theorem §C5a.6.1.** $\bar\psi'(x) = \psi(y)^\dagger\Lambda_{1/2}^\dagger\gamma^0 = \psi(y)^\dagger\gamma^0\Lambda_{1/2}^{-1} = \bar\psi(y)\Lambda_{1/2}^{-1}$.
>
> **3. The pairing.** $(\bar\psi'\chi')(x) = \bar\psi(y)\Lambda_{1/2}^{-1}\Lambda_{1/2}\chi(y) = \bar\psi(y)\chi(y)$: a one-component field whose value at $x$ is the old value at $\Lambda^{-1}x$, the scalar law of [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]].
>
> **4. The adjoint of $\bar\psi$.** $(\psi^\dagger\gamma^0)^\dagger = \gamma^{0\dagger}\psi = \gamma^0\psi$, with $\gamma^{0\dagger} = \gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]).
>
> **What the derivation shows**
> - $\bar\psi$ is an "inverse Dirac spinor": its column index is contracted, its row transforms with $\Lambda_{1/2}^{-1}$ from the right; the $\gamma^0$ converts the non-unitary $\Lambda_{1/2}^\dagger$ into $\Lambda_{1/2}^{-1}$ exactly on the boosts.
> - ⚑ By-product: $\bar\psi\psi$ is real ($(\psi^\dagger\gamma^0\psi)^* = \psi^\dagger\gamma^{0\dagger}\psi$) but not positive (step 7 of Derivation §C5a.6.1); the positive $\psi^\dagger\psi$ is not invariant. A relativistic spinor field has no invariant positive density: the probability interpretation of Quantum Mechanics' $\Psi^\dagger\Psi$ ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]) survives only as the time component of a current.
> - Used next: the Lagrangian (Model §C5a.7.3) and every bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]).

^der-c5a-6-2

*Uses:* [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]

## Bilinears

> [!definition] Definition §C5a.6.1: Fermion Bilinear
> A **fermion bilinear** is $\bar\psi\,\Gamma\,\chi$, with $\psi$, $\chi$ Dirac fields ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), $\bar\psi$ the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]) (often $\chi = \psi$) and $\Gamma$ a constant $4\times4$ matrix, usually a product ("string") of $\gamma$ matrices. It is a number (row times matrix times column) and carries no spinor index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (opening) · PHY 513 Lecture 8, Part B ("Fermion Bilinears") · PS §3.4, p. 49 · Yu §5.3, after eq. (5.92)*

^def-c5a-6-1

> [!theorem] Theorem §C5a.6.3: Scalar, Vector and Tensor Bilinears
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]; and likewise $\chi$), a bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]) transforms as $\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}$ does. In particular, with $y = \Lambda^{-1}x$,
>
> $$
> \bar\psi'\chi'(x) = \bar\psi\chi(y), \qquad \bar\psi'\gamma^\mu\chi'(x) = \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\chi(y), \qquad \bar\psi'[\gamma^\mu, \gamma^\nu]\chi'(x) = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma\,\bar\psi[\gamma^\rho, \gamma^\sigma]\chi(y) :
> $$
>
> a scalar, a vector and an antisymmetric tensor field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]]). A string of $n$ $\gamma$'s gives an $n$-index tensor.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (Derivation "The first three bilinears") · PHY 513 Lecture 8, Part B · PS §3.4, p. 49 · Yu §5.3, eqs. (5.92), (5.94), (5.96)*

^thm-c5a-6-3

> [!derivation]- Derivation
> **1. General law.** By [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], $\bar\psi'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}$, and $\chi'(x) = \Lambda_{1/2}\chi(y)$. So $\bar\psi'\Gamma\chi'(x) = \bar\psi(y)\bigl(\Lambda_{1/2}^{-1}\Gamma\Lambda_{1/2}\bigr)\chi(y)$.
>
> **2. Scalar, $\Gamma = \mathbb 1$.** $\Lambda_{1/2}^{-1}\Lambda_{1/2} = \mathbb 1$.
>
> **3. Vector, $\Gamma = \gamma^\mu$.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]]); the number $\Lambda^\mu{}_\nu$ comes out of the bilinear.
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

^der-c5a-6-3

*Uses:* [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]]

> [!definition] Definition §C5a.6.2: The Sixteen Bilinears
> With $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]) and
>
> $$
> \sigma^{\mu\nu} \equiv \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu} ,
> $$
>
> where $S^{\mu\nu}$ are the spinor generators ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; other normalizations of $\sigma^{\mu\nu}$: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|Caution: Three normalizations of σ^μν]]), the **standard bilinears** are
>
> | name | bilinear | number |
> |---|---|---|
> | scalar (S) | $\bar\psi\psi$ | 1 |
> | pseudoscalar (P) | $\bar\psi\,i\gamma^5\psi$ | 1 |
> | vector (V) | $\bar\psi\gamma^\mu\psi$ | 4 |
> | axial vector (A) | $\bar\psi\gamma^\mu\gamma^5\psi$ | 4 |
> | tensor (T) | $\bar\psi\sigma^{\mu\nu}\psi$, $\mu < \nu$ | 6 |
>
> Their matrices $\mathbb 1, i\gamma^5, \gamma^\mu, \gamma^\mu\gamma^5, \sigma^{\mu\nu}$ are sixteen; they span all $4\times4$ matrices ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.9 (paragraph after the derivation), Ch. 9 §9.6 · PS §3.4, pp. 49–50 (table) · Yu §5.3, eqs. (5.93)–(5.96) · the user's pre-course notes, §5.3*

^def-c5a-6-2

Reducing an arbitrary product of $\gamma$'s to these sixteen is [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]].

> [!caution] Caution: Three normalizations of σ^μν
> Peskin–Schroeder and this note: $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. The Lorentz generators: $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac12\sigma^{\mu\nu}$. Problem Set 5 writes $\sigma^{\mu\nu} = \frac{1}{4i}[\gamma^\mu, \gamma^\nu] = -S^{\mu\nu}$. Identities homogeneous in $\sigma$ (such as the duality [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-7|Theorem §C5a.11.7]]) hold in every normalization; identities mixing $\sigma$ with other terms (the Gordon identity, [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]]) do not. Peskin–Schroeder also write $\gamma^{\mu\nu} = \frac12[\gamma^\mu, \gamma^\nu] = -i\sigma^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.6 (Principle "Properties of $\gamma^5$", last sentence) · PHY 513, Problem Set 5, Problem 5(d) statement · PS §3.4, p. 49*

^cau-c5a-6-1

> [!theorem] Theorem §C5a.6.4: Pseudoscalar and Axial Vector under Proper Lorentz Transformations
> Under $\psi \to \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), the pseudoscalar and axial bilinears of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]] obey
>
> $$
> \bar\psi\,i\gamma^5\psi \;\to\; \bar\psi\,i\gamma^5\psi, \qquad \bar\psi\gamma^\mu\gamma^5\psi \;\to\; \Lambda^\mu{}_\nu\,\bar\psi\gamma^\nu\gamma^5\psi \qquad (\text{at } \Lambda^{-1}x) :
> $$
>
> for proper orthochronous $\Lambda$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]) they transform exactly as a scalar and a vector. They differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ only by a sign under parity ([[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]]).
>
> *Source: PS §3.4, p. 50 ("pseudo-vector and pseudo-scalar") · Yu §5.3, eqs. (5.93), (5.95) · the user's PHY 513 notes, Ch. 8 §8.9 (closing paragraph)*

^thm-c5a-6-4

> [!derivation]- Derivation
> **1. $\gamma^5$ is invariant.** $\gamma^5$ commutes with every $S^{\mu\nu}$, hence with $\Lambda_{1/2} = \exp(-\frac i2\omega S)$ and its inverse: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]).
>
> **2. Pseudoscalar.** Step 1 of Derivation §C5a.6.3 with $\Gamma = i\gamma^5$: $\Lambda_{1/2}^{-1}i\gamma^5\Lambda_{1/2} = i\gamma^5$.
>
> **3. Axial vector.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$: $\Lambda_{1/2}^{-1}\gamma^\mu\gamma^5\Lambda_{1/2} = (\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2})(\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2}) = \Lambda^\mu{}_\nu\gamma^\nu\gamma^5$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]] and step 1).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ comes from the identity component only, so it cannot see the "pseudo": $\gamma^5 \propto \varepsilon_{\kappa\lambda\mu\nu}\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]]) carries one $\varepsilon$, which is invariant under $\det\Lambda = +1$ and odd under parity ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
> - Used next: the axial current (Theorem §C5a.8.4).

^der-c5a-6-4

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]

> [!theorem] Theorem §C5a.6.5: The Bilinears Are Real
> For any bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-1|Def. §C5a.6.1]]) of commuting components, $(\bar\psi\Gamma\psi)^* = \bar\psi\,\bar\Gamma\,\psi$ with $\bar\Gamma \equiv \gamma^0\Gamma^\dagger\gamma^0$. For the five standard matrices of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], $\bar\Gamma = \Gamma$:
>
> $$
> \bar\psi\psi,\quad \bar\psi\,i\gamma^5\psi,\quad \bar\psi\gamma^\mu\psi,\quad \bar\psi\gamma^\mu\gamma^5\psi,\quad \bar\psi\sigma^{\mu\nu}\psi \quad\text{are real},
> $$
>
> while $\bar\psi\gamma^5\psi$ is imaginary.
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the user's PHY 513 notes, Ch. 8 §8.8 ("Yu (5.97)–(5.101) give the reality of the bilinears") · the user's pre-course notes, §5.3*

^thm-c5a-6-5

> [!derivation]- Derivation
> **1. General.** A bilinear is a $1\times1$ matrix, so its complex conjugate is its adjoint: $(\psi^\dagger\gamma^0\Gamma\psi)^\dagger = \psi^\dagger\Gamma^\dagger\gamma^{0\dagger}\psi = \psi^\dagger\Gamma^\dagger\gamma^0\psi$. Insert $(\gamma^0)^2 = \mathbb 1$ in front: $= \psi^\dagger\gamma^0(\gamma^0\Gamma^\dagger\gamma^0)\psi = \bar\psi\bar\Gamma\psi$.
>
> **2. The five matrices.** Use $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]), $\gamma^{5\dagger} = \gamma^5$ and $\gamma^0\gamma^5 = -\gamma^5\gamma^0$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]):
> - $\Gamma = \mathbb 1$: $\gamma^0\gamma^0 = \mathbb 1$.
> - $\Gamma = \gamma^\mu$: $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^0\gamma^\mu\gamma^0\gamma^0 = \gamma^\mu$.
> - $\Gamma = i\gamma^5$: $(i\gamma^5)^\dagger = -i\gamma^5$; $\gamma^0(-i\gamma^5)\gamma^0 = -i(-\gamma^5\gamma^0)\gamma^0 = i\gamma^5$.
> - $\Gamma = \gamma^\mu\gamma^5$: $(\gamma^\mu\gamma^5)^\dagger = \gamma^5\gamma^{\mu\dagger}$; $\gamma^0\gamma^5\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^0\gamma^{\mu\dagger}\gamma^0 = -\gamma^5\gamma^\mu = \gamma^\mu\gamma^5$ (anticommute once more).
> - $\Gamma = \sigma^{\mu\nu}$: $\sigma^{\mu\nu\dagger} = -\frac i2[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$; sandwiching, $\gamma^0\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^{\nu\dagger}\gamma^0\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\nu\gamma^\mu$, so $\bar\sigma^{\mu\nu} = -\frac i2[\gamma^\nu, \gamma^\mu] = \sigma^{\mu\nu}$.
>
> **3. Without the $i$.** For $\Gamma = \gamma^5$, $\bar\Gamma = \gamma^0\gamma^5\gamma^0 = -\gamma^5$, so $(\bar\psi\gamma^5\psi)^{\ast} = -\bar\psi\gamma^5\psi$. ⚑ By-product: the $i$ in the pseudoscalar is the reality convention, as the $i$ in the Lagrangian is ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|§C5a.7, Remark: Why the i]]).
>
> **What the derivation shows**
> - The bar operation $\Gamma \mapsto \gamma^0\Gamma^\dagger\gamma^0$ is the adjoint with respect to the indefinite form $\gamma^0$ of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]; the standard basis is chosen self-adjoint.
> - Step 1 used only $(AB)^\dagger = B^\dagger A^\dagger$, valid also for operator-valued components: the quantized bilinears are Hermitian ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).

^der-c5a-6-5

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]

> [!remark] Remark: The quantized bilinears are Hermitian
> After quantization the same computation makes the five standard bilinears of [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]] Hermitian operators, once the product of two field operators at one point is defined by normal ordering ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]) and smeared with a test function (operator-valued distributions, [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]): step 1 of the derivation used only $(AB)^\dagger = B^\dagger A^\dagger$.
>
> *Source: Yu §5.3, eqs. (5.97)–(5.101) · the operator reading written here*

^rem-c5a-6-2

> [!remark]- Connections
> - $\gamma^0$ is to the Dirac spinor slot what $g_{\mu\nu}$ is to a vector slot: both are indefinite forms preserved by the group, and both are needed because the Lorentz group is noncompact — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]].
> - The sixteen bilinears are the Dirac field's analogue of decomposing a two-index tensor into trace, antisymmetric and symmetric parts: $(\frac12, 0)\oplus(0, \frac12)$ tensored with its conjugate gives $(0,0)$ twice, $(\frac12,\frac12)$ twice and $(1,0)\oplus(0,1)$, i.e. S, P, V, A and T — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-6|Theorem §C3.4.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-7|Theorem §C3.4.7]].
> - The tensor bilinear transforms like $F^{\mu\nu}$, and the Gordon identity shows it is the magnetic-moment part of the vector current, which gives $g = 2$ — [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]], [[§C13.2★ The Dirac Equation#^thm-c13-2-5|QM Theorem §C13.2.5]].
> - The invariance of $\bar\psi\chi$ is the invariance of the Dirac form of [[§C5a.2 The Dirac Form|§C5a.2]] under $\Lambda_{1/2}$, as $g(v, w)$ is invariant under $\Lambda$ — [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]].
