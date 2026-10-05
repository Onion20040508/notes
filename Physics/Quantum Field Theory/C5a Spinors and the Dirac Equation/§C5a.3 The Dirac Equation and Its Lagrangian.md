---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.2 The Clifford Algebra and the Dirac Representation]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.4 Bilinears, Chirality and the Weyl Equations]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.4 (Lecture 8's starting point), §8.5 (The Dirac equation), §8.6 (Why the Dirac equation is covariant), §8.7 (The Dirac conjugate), §8.8 (The Dirac Lagrangian), §8.11 (Dirac implies Klein–Gordon) · PHY 513 Lecture 8 (Larsen), Parts A–C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 42–44, eqs. (3.29)–(3.35), §3.5, p. 52, eqs. (3.83)–(3.85) · Yu Zhao-Huan, 量子场论讲义, §5.2–§5.3, eqs. (5.83)–(5.111) · the user's pre-course notes, §5.3.*

Which first-order field equation can a Dirac spinor obey, why does it look the same to every observer, and from which Lagrangian does it follow? The Dirac representation, its generators $S^{\mu\nu}$, the matrices $\Lambda_{1/2}$ and the key identity $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ are [[§C5a.2 The Clifford Algebra and the Dirac Representation|§C5a.2]] ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]); the action principle and the Euler–Lagrange equations are [[§C1.9 The Action Principle and the Euler–Lagrange Equations|§C1.9]], whose models are scalar. This section adds the Dirac field: the equation and its covariance, the Dirac conjugate $\bar\psi$ (why $\psi^\dagger$ will not do), the Dirac Lagrangian with its field equations, momenta and Hamiltonian density, and the fact that every solution obeys the Klein–Gordon equation. Bilinears, chirality and the currents are [[§C5a.4 Bilinears, Chirality and the Weyl Equations|§C5a.4]]; the solutions [[§C5a.5 Plane-Wave Solutions|§C5a.5]].

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+,-,-,-)$, active Lorentz transformations ([[§C1.4 The Lorentz Group#^def-c1-4-1|Def. §C1.4.1]]), $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]). In this section $\psi$ is a classical field with commuting complex components; the quantized field, with anticommuting components, is [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The Dirac equation

> [!definition] Definition §C5a.3.1: The Dirac Equation
> A **Dirac field** $\psi(x)$ is a four-component field transforming as $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$, with $\Lambda_{1/2}$ the Dirac representation ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]; spinor fields, [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]; Lorentz transformations read actively, [[§C1.4 The Lorentz Group#^def-c1-4-1|Def. §C1.4.1]]). The **Dirac equation** is
>
> $$
> \bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi(x) = 0, \qquad\text{in components}\qquad \bigl[i(\gamma^\mu)_{ab}\,\partial_\mu - m\,\delta_{ab}\bigr]\psi_b(x) = 0, \quad a = 1, \dots, 4 ,
> $$
>
> with $\gamma^\mu$ the Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]; the course uses the chiral basis, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]) and $m$ a real constant times the $4\times4$ identity: four coupled, first-order, linear partial differential equations. The matrix of differential operators $i\gamma^\mu\partial_\mu - m$ is the **Dirac operator**.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.5 (Definition "The Dirac equation", eq. (dirac)) · PHY 513 Lecture 8, Part A ("Introducing the Dirac Equation") · PS §3.2, eq. (3.31) · Yu §5.3, eqs. (5.107)–(5.108)*

^def-c5a-3-1

> [!definition] Definition §C5a.3.2: Feynman Slash
> For any four-vector $a_\mu$ (numbers, or operators commuting with the $\gamma$'s, such as $\partial_\mu$),
>
> $$
> \slashed{a} \equiv \gamma^\mu a_\mu = \gamma^0a_0 + \gamma^ia_i ,
> $$
>
> a $4\times4$ matrix built from the Dirac matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]). In particular $\slashed{p} = \gamma^\mu p_\mu$, $\slashed{\partial} = \gamma^\mu\partial_\mu$, and the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) reads $(i\slashed{\partial} - m)\psi = 0$. In the chiral basis ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]]) $\slashed{p} = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Definition "Feynman slash") · PHY 513 Lecture 9 ("Notation: $\gamma^\mu p_\mu \equiv \slashed{p}$") · PS §3.3, p. 49 · Yu §5.4, eq. (5.146) · PHY 513, Problem Set 5, Problem 2 (closing note on notation, as the user wrote it)*

^def-c5a-3-2

The chiral form uses $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-2|Def. §C5a.2.2]]) with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Weyl Spinors and SL(2,C)#^def-c5a-1-1|Def. §C5a.1.1]]: $\gamma^\mu p_\mu$ has upper-right block $\sigma^\mu p_\mu = p\cdot\sigma$. The square $\slashed{a}^{\,2} = a^2$ is [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]]; the rest of the slash algebra is [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]. The slash is a contraction, so $\slashed{a}$ is "invariant" only in the sense of [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-1|Remark: What covariance shows and what it does not]]: it is a matrix whose two spinor slots still transform.

> [!caution] Caution: γ^μ∂_μ has a plus sign
> With $\partial_i = \partial/\partial x^i$ (lower index, the usual meaning) the contraction needs no metric:
>
> $$
> \gamma^\mu\partial_\mu = \gamma^0\partial_t + \gamma^i\frac{\partial}{\partial x^i} = \gamma^0\partial_t + \boldsymbol\gamma\cdot\nabla .
> $$
>
> A minus sign appears only when an index is moved: $\gamma^\mu\partial_\mu = \gamma_\mu\partial^\mu = \gamma^0\partial_t - \gamma^i\partial^i$, since $\partial^i = -\partial_i$. Writing $\gamma^0\partial_t - \boldsymbol\gamma\cdot\nabla$ flips the sign of every spatial derivative in the equation.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.5 (Caution "The sign in $\gamma^\mu\partial_\mu$") · PHY 513 Lecture 8, Part A*

^cau-c5a-3-1

> [!remark] Remark: What covariance shows and what it does not
> Theorem §C5a.3.1 below shows that the Dirac equation is **covariant**: if $\psi$ solves it, so does the transformed field, with the same matrices $\gamma^\mu$ and the same $m$. That makes it a consistent candidate for a law of motion, not a proof that nature uses it. Covariance needs $m$ to be a Lorentz scalar; that $m$ is the mass is Theorem §C5a.3.10. The explicit $i$ is not required by covariance; it is required by consistency with the conjugate equation and by reality of the Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-3|Remark: Why the i]]). Expressions such as $\slashed{\partial}$ or $\slashed{p}$ are called "Lorentz invariant" in the lecture in the sense that every vector index is contracted; they remain matrices whose spinor slots transform, $\Lambda_{1/2}\slashed{p}\,\Lambda_{1/2}^{-1} = (\Lambda p)\!\!\!/$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]] read with $\Lambda^{-1}$). What is invariant is the *form* of a relation between such matrices.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.5 (Principle "What has been shown, and what has not"), Ch. 9 §9.4 (Caution "In what sense $\slashed{p}$ is 'Lorentz invariant'")*

^rem-c5a-3-1

## Covariance

> [!theorem] Theorem §C5a.3.1: The Dirac Equation Is Covariant
> Let $\psi$ be a $C^1$ four-component field and $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]). Then
>
> $$
> \bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi'(x) = \Lambda_{1/2}\,\bigl[\bigl(i\gamma^\nu\partial_\nu - m\bigr)\psi\bigr](\Lambda^{-1}x) ,
> $$
>
> with the same $\gamma^\mu$ and the same $m$ on both sides. Hence $\psi'$ solves the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) if and only if $\psi$ does; in particular $\gamma^\mu\partial_\mu\psi$ transforms exactly like $\psi$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.6 (Derivation "Covariance of the Dirac equation, the lecture's way", Steps 4–5) · PHY 513 Lecture 8, Part A ("Relativistic Invariance of the Dirac Equation") · PS §3.2, p. 42 · Yu §5.3, eq. (5.109)*

^thm-c5a-3-1

> [!derivation]- Derivation
> Write $y = \Lambda^{-1}x$, i.e. $y^\nu = (\Lambda^{-1})^\nu{}_\rho\,x^\rho$.
>
> **1. The derivative of the transformed field (chain rule).** $\Lambda_{1/2}$ is a constant matrix, so it passes through $\partial_\mu = \partial/\partial x^\mu$. The inner function has $\partial y^\nu/\partial x^\mu = (\Lambda^{-1})^\nu{}_\mu$ (the $x^\rho$-derivative of a linear map is its matrix). Hence
>
> $$
> \partial_\mu\psi'(x) = \Lambda_{1/2}\,\frac{\partial y^\nu}{\partial x^\mu}\,(\partial_\nu\psi)(y) = \Lambda_{1/2}\,(\Lambda^{-1})^\nu{}_\mu\,(\partial_\nu\psi)(y) .
> $$
>
> The derivative is a lower-index vector and is transformed with the inverse matrix.
>
> **2. Multiply by $\gamma^\mu$ and sum over $\mu$.**
>
> $$
> \gamma^\mu\partial_\mu\psi'(x) = \gamma^\mu\Lambda_{1/2}\,(\Lambda^{-1})^\nu{}_\mu\,(\partial_\nu\psi)(y) .
> $$
>
> The numbers $(\Lambda^{-1})^\nu{}_\mu$ commute with the matrices; the matrices $\gamma^\mu$ and $\Lambda_{1/2}$ do not commute and their order is kept.
>
> **3. Push $\Lambda_{1/2}$ to the left.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ in front: $\gamma^\mu\Lambda_{1/2} = \Lambda_{1/2}\bigl(\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}\bigr) = \Lambda_{1/2}\,\Lambda^\mu{}_\rho\gamma^\rho$ by [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]]. So
>
> $$
> \gamma^\mu\partial_\mu\psi'(x) = \Lambda_{1/2}\,\gamma^\rho\;\Lambda^\mu{}_\rho(\Lambda^{-1})^\nu{}_\mu\;(\partial_\nu\psi)(y) .
> $$
>
> **4. Contract the vector indices.** $(\Lambda^{-1})^\nu{}_\mu\Lambda^\mu{}_\rho$ is the $(\nu, \rho)$ entry of the matrix product $\Lambda^{-1}\Lambda = \mathbb 1$, i.e. $\delta^\nu{}_\rho$. Summing over $\rho$:
>
> $$
> \gamma^\mu\partial_\mu\psi'(x) = \Lambda_{1/2}\,\gamma^\nu(\partial_\nu\psi)(y) = \Lambda_{1/2}\,\bigl(\gamma^\nu\partial_\nu\psi\bigr)(\Lambda^{-1}x) .
> $$
>
> The spinor transformation pushed through $\gamma^\mu$ produced exactly the vector transformation $\Lambda$ that undoes the $\Lambda^{-1}$ suffered by $\partial_\mu$.
>
> **5. The mass term.** $m\psi'(x) = m\Lambda_{1/2}\psi(y) = \Lambda_{1/2}\,m\psi(y)$, because $m$ multiplies the identity and commutes with $\Lambda_{1/2}$. ⚑ By-product: this step needs $m$ to be the same number in every frame, a Lorentz scalar; a term $v^\mu\gamma_\mu$ with a fixed vector $v$ would fail step 4 (no $\partial$ to absorb $\Lambda$) → [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-1|Remark: What covariance shows and what it does not]].
>
> **6. Combine.** Multiply step 4 by $i$ and subtract step 5:
>
> $$
> \bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi'(x) = \Lambda_{1/2}\bigl[\bigl(i\gamma^\nu\partial_\nu - m\bigr)\psi\bigr](y) .
> $$
>
> $\Lambda_{1/2}$ is invertible (an exponential), so the left side vanishes for all $x$ exactly when the bracket vanishes for all $y = \Lambda^{-1}x$, which ranges over all of spacetime as $x$ does.
>
> **What the derivation shows**
> - The whole content is one identity, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: $\gamma^\mu$ is an invariant tensor with one vector slot and two spinor slots, and "contract the vector index with $\partial_\mu$" is the rule that builds a spinor out of a spinor ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-6|§C5a.2, Remark: What each Dirac index labels]]).
> - ⚑ By-product: $\Lambda_{1/2}$ is fixed by $\Lambda$ only up to sign ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]); the equation is linear and homogeneous, so both signs give the same statement.
> - Assumption: $\psi \in C^1$. For a distribution the same computation holds term by term, since derivatives and linear changes of variables are defined on $\mathcal S'$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
> - Used next: the Lagrangian is a scalar (Theorem §C5a.3.5); the same push-through gives the transformation of every bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]]).

^der-c5a-3-1

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-12|Theorem §C5a.2.12]], [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]

The slides phrase the transformation passively ("the physical point that the field is evaluated at does not change but its coordinates do") while the formula is written actively; the two readings give the same formula ([[§C1.4 The Lorentz Group#^def-c1-4-1|Def. §C1.4.1]]). Quantum Mechanics records the same check with $\hbar$, $c$ and a passive transformation, for one boost ([[§C13.2★ The Dirac Equation#^rem-c13-2-4|QM Remark: Lorentz covariance and the rapidity]]); here it holds for every $\omega$ because the identity of Theorem §C5a.2.12 is proved for the whole group.

## The Dirac conjugate

> [!remark] Remark: Why ψ†ψ is not a scalar
> A Lagrangian must be a scalar, so $\psi$ needs a partner that transforms with $\Lambda_{1/2}^{-1}$. The quantum-mechanical candidate $\psi^\dagger$ transforms as $\psi^\dagger \to \psi^\dagger\Lambda_{1/2}^\dagger = \psi^\dagger\exp(+\frac i2\omega_{\mu\nu}S^{\mu\nu\dagger})$, which would be $\psi^\dagger\Lambda_{1/2}^{-1}$ if every $S^{\mu\nu}$ were Hermitian. The rotation generators $S^{ij}$ are; the boost generators $S^{0i}$ are anti-Hermitian ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-11|Theorem §C5a.2.11]]). So $\Lambda_{1/2}$ is unitary on rotations and not on boosts, and $\psi^\dagger\psi$ is invariant under rotations only. This is not a defect of the basis: no finite-dimensional representation of the Lorentz group is unitary ([[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]]). Indeed $\psi^\dagger\psi$ will turn out to be the time component of the vector $\bar\psi\gamma^\mu\psi$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (opening paragraph; Derivation "Why $\psi^\dagger\psi$ fails", Step 1) · PHY 513 Lecture 8, Part B ("The Hermitean Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.83)–(5.85)*

^rem-c5a-3-2

> [!theorem] Theorem §C5a.3.2: Λ½ Is Pseudo-Unitary
> For every real $\omega_{\mu\nu}$, the Dirac-representation matrix $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]) and $\gamma^0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]) satisfy
>
> $$
> \Lambda_{1/2}^\dagger\,\gamma^0 = \gamma^0\,\Lambda_{1/2}^{-1}, \qquad\text{equivalently}\qquad \Lambda_{1/2}^\dagger\,\gamma^0\,\Lambda_{1/2} = \gamma^0, \qquad \Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0 .
> $$
>
> $\gamma^0$ is a Hermitian form on $\mathbb C^4$ preserved by every $\Lambda_{1/2}$; it is indefinite, with eigenvalues $+1$, $+1$, $-1$, $-1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary)), §8.7 (Derivation "Why $\psi^\dagger\psi$ fails, and how $\gamma^0$ repairs it: the lecture's route", Steps 2–3, eq. (gammaSdagger)) · PHY 513 Lecture 8, Part B ("The Dirac Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.86)–(5.89)*

^thm-c5a-3-2

> [!derivation]- Derivation (the lecture's route: which generators γ⁰ commutes with)
> **1. $\gamma^0$ commutes with $S^{ij}$.** For $i \ne j$, $[\gamma^i, \gamma^j] = 2\gamma^i\gamma^j$ (distinct $\gamma$'s anticommute, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]]), so $S^{ij} = \frac i2\gamma^i\gamma^j$. Moving $\gamma^0$ through $\gamma^i$ and then $\gamma^j$ costs two signs: $\gamma^0\gamma^i\gamma^j = (-\gamma^i\gamma^0)\gamma^j = \gamma^i\gamma^j\gamma^0$. Hence $\gamma^0S^{ij} = S^{ij}\gamma^0$.
>
> **2. $\gamma^0$ anticommutes with $S^{0i}$.** $S^{0i} = \frac i2\gamma^0\gamma^i$. Then $\gamma^0S^{0i} = \frac i2(\gamma^0)^2\gamma^i = \frac i2\gamma^i$, using $(\gamma^0)^2 = \mathbb 1$; and $S^{0i}\gamma^0 = \frac i2\gamma^0\gamma^i\gamma^0 = \frac i2\gamma^0(-\gamma^0\gamma^i) = -\frac i2\gamma^i$. Hence $\gamma^0S^{0i} = -S^{0i}\gamma^0$.
>
> **3. Combine with the Hermiticity pattern.** By [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-11|Theorem §C5a.2.11]], $S^{ij\dagger} = S^{ij}$ and $S^{0i\dagger} = -S^{0i}$. Therefore $S^{ij\dagger}\gamma^0 = S^{ij}\gamma^0 = \gamma^0S^{ij}$ (step 1) and $S^{0i\dagger}\gamma^0 = -S^{0i}\gamma^0 = \gamma^0S^{0i}$ (step 2). In every case
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
> **7. The form is indefinite.** $\gamma^0$ is Hermitian with $(\gamma^0)^2 = \mathbb 1$, so its eigenvalues are $\pm1$; it is traceless ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]), so each occurs twice. In the chiral basis $\gamma^0$ swaps the upper and lower blocks, with eigenvectors $(\xi, \xi)$ and $(\xi, -\xi)$. ⚑ By-product: $\psi^\dagger\gamma^0\psi$ can have either sign; the invariant of a Dirac spinor is not a norm → [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]] (it pairs left- with right-handed components).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ preserves the Hermitian form $\gamma^0$ as $\Lambda$ preserves $g$ ($\Lambda^{\mathsf T}g\Lambda = g$): $\gamma^0$ plays the role of the metric for the Dirac spinor slot; both forms are indefinite.
> - ⚑ By-product: the sign ambiguity $\pm\Lambda_{1/2}$ cancels in $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2}$.
> - Used next: the Dirac conjugate (Def. §C5a.3.3, Theorem §C5a.3.3).

^der-c5a-3-2

> [!derivation]- Derivation (second route: from the Hermiticity of the γ's)
> **1.** By [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; multiplying by $\gamma^0$ on the right, $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$.
>
> **2.** $S^{\mu\nu\dagger} = (\frac i4[\gamma^\mu, \gamma^\nu])^\dagger = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}] = -\frac i4\bigl(\gamma^{\nu\dagger}\gamma^{\mu\dagger} - \gamma^{\mu\dagger}\gamma^{\nu\dagger}\bigr)$ (the adjoint reverses products and conjugates $i$).
>
> **3.** Multiply on the right by $\gamma^0$ and push it left with step 1, twice in each product: $\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^{\nu\dagger}\gamma^0\gamma^\mu = \gamma^0\gamma^\nu\gamma^\mu$. Hence $S^{\mu\nu\dagger}\gamma^0 = -\frac i4\gamma^0(\gamma^\nu\gamma^\mu - \gamma^\mu\gamma^\nu) = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu] = \gamma^0S^{\mu\nu}$, step 3 of the first route.
>
> **4.** Steps 4–6 of the first route follow unchanged.
>
> **What the derivation shows**
> - No explicit matrices and no case split between rotations and boosts: the result follows from $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ alone, hence holds in every basis in which that relation holds (every unitary change of the chiral basis, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-5|Theorem §C5a.2.5]]).

^der-c5a-3-2b

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-11|Theorem §C5a.2.11]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]

> [!definition] Definition §C5a.3.3: The Dirac Conjugate
> The **Dirac conjugate** of a Dirac spinor (or field) $\psi$ is the row
>
> $$
> \bar\psi \equiv \psi^\dagger\gamma^0 .
> $$
>
> It is not the Hermitian conjugate: the extra $\gamma^0$, the invariant form of [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], is essential.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Definition "The Dirac conjugate", eq. (psibar)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.32) · Yu §5.3, eq. (5.90)*

^def-c5a-3-3

> [!theorem] Theorem §C5a.3.3: The Dirac Conjugate Transforms with the Inverse
> If $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]), its Dirac conjugate ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) transforms as
>
> $$
> \bar\psi'(x) = \bar\psi(\Lambda^{-1}x)\,\Lambda_{1/2}^{-1} ,
> $$
>
> and for any two Dirac fields $\psi$, $\chi$ the number $\bar\psi\chi = \psi^\dagger\gamma^0\chi$ is a Lorentz scalar field ([[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-2|Def. §C1.8.2]]), $(\bar\psi'\chi')(x) = (\bar\psi\chi)(\Lambda^{-1}x)$. Moreover $(\bar\psi)^\dagger = \gamma^0\psi$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.7 (Derivation, Step 4; Definition "The Dirac conjugate") · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.33) · Yu §5.3, eqs. (5.91)–(5.92)*

^thm-c5a-3-3

> [!derivation]- Derivation
> Write $y = \Lambda^{-1}x$.
>
> **1. Conjugate the transformed field.** $\psi'(x)^\dagger = (\Lambda_{1/2}\psi(y))^\dagger = \psi(y)^\dagger\Lambda_{1/2}^\dagger$ (the adjoint reverses the product; $y$ is a real point, untouched).
>
> **2. Multiply by $\gamma^0$ and use Theorem §C5a.3.2.** $\bar\psi'(x) = \psi(y)^\dagger\Lambda_{1/2}^\dagger\gamma^0 = \psi(y)^\dagger\gamma^0\Lambda_{1/2}^{-1} = \bar\psi(y)\Lambda_{1/2}^{-1}$.
>
> **3. The pairing.** $(\bar\psi'\chi')(x) = \bar\psi(y)\Lambda_{1/2}^{-1}\Lambda_{1/2}\chi(y) = \bar\psi(y)\chi(y)$: a one-component field whose value at $x$ is the old value at $\Lambda^{-1}x$, the scalar law of [[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-2|Def. §C1.8.2]].
>
> **4. The adjoint of $\bar\psi$.** $(\psi^\dagger\gamma^0)^\dagger = \gamma^{0\dagger}\psi = \gamma^0\psi$, with $\gamma^{0\dagger} = \gamma^0$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]).
>
> **What the derivation shows**
> - $\bar\psi$ is an "inverse Dirac spinor": its column index is contracted, its row transforms with $\Lambda_{1/2}^{-1}$ from the right; the $\gamma^0$ converts the non-unitary $\Lambda_{1/2}^\dagger$ into $\Lambda_{1/2}^{-1}$ exactly on the boosts.
> - ⚑ By-product: $\bar\psi\psi$ is real ($(\psi^\dagger\gamma^0\psi)^* = \psi^\dagger\gamma^{0\dagger}\psi$) but not positive (step 7 of Derivation §C5a.3.2); the positive $\psi^\dagger\psi$ is not invariant. A relativistic spinor field has no invariant positive density: the probability interpretation of Quantum Mechanics' $\Psi^\dagger\Psi$ ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]) survives only as the time component of a current.
> - Used next: the Lagrangian (Model §C5a.3.4) and every bilinear ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]]).

^der-c5a-3-3

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-2|Def. §C1.8.2]]

## The Dirac Lagrangian

> [!model] Model §C5a.3.4: The Free Dirac Field
> A Dirac field $\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]) with the Lagrangian density ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^def-c1-9-1|Def. §C1.9.1]])
>
> $$
> \mathcal L = \bar\psi\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi = i\bar\psi\slashed{\partial}\psi - m\bar\psi\psi ,
> $$
>
> where $\bar\psi$ is the Dirac conjugate ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) and $\slashed{\partial}$ the slash ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]); $\psi$ and $\bar\psi$ are varied as independent fields. Its field equation is the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]]).
>
> *Assumptions:* classical field with commuting complex components (anticommuting after quantization, [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]); free (quadratic $\mathcal L$, linear equation); $m \ge 0$ a real parameter, the mass ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]]; the sign of $m$ is a convention); kinetic term normalized without a factor, which fixes $[\psi] = \frac32$ ([[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-5|Theorem §C1.2.5]]); variations vanishing on the boundary; flat spacetime.
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Definition "The Dirac Lagrangian", eq. (diracL)) · PHY 513 Lecture 8, Part B ("The Dirac Lagrangian") · PS §3.2, eq. (3.34) · Yu §5.3, eq. (5.103)*

^mod-c5a-3-4

It is the spinor entry of the list that began with the scalar fields [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^mod-c1-9-6|Model §C1.9.6]] and [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^mod-c1-9-7|Model §C1.9.7]], previewed in [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^rem-c1-9-5|§C1.9, Remark: One equation for every kind of field]]. Two differences from the scalar: $\mathcal L$ is first order in derivatives, so it is linear in the velocities, and it vanishes on solutions ($\mathcal L = \bar\psi\cdot0$). The mass dimension $[\psi] = \frac32$ and its consequence, a coupling of dimension $-2$ for a four-fermion term $(\bar\psi\psi)^2$ (the Fermi constant), are [[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-5|Theorem §C1.2.5]] and [[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-6|Theorem §C1.2.6]].

> [!theorem] Theorem §C5a.3.5: The Dirac Lagrangian Is a Lorentz Scalar
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]), the density of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] obeys
>
> $$
> \mathcal L'(x) \equiv \bar\psi'(x)\bigl(i\slashed{\partial} - m\bigr)\psi'(x) = \mathcal L(\Lambda^{-1}x) ,
> $$
>
> the law of a scalar field ([[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^def-c1-8-2|Def. §C1.8.2]]); so the action $S = \int d^4x\,\mathcal L$ is Lorentz invariant ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-1|Theorem §C1.9.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Definition "The Dirac Lagrangian"; Figure "Why $\bar\psi\,i\gamma^\mu\partial_\mu\psi$ is a scalar") · PHY 513 Lecture 8, Part B ("Proof of invariance") · Yu §5.3, eq. (5.102)*

^thm-c5a-3-5

> [!derivation]- Derivation
> **1. The right factor.** By [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]], $(i\slashed{\partial} - m)\psi'(x) = \Lambda_{1/2}[(i\slashed{\partial} - m)\psi](y)$, $y = \Lambda^{-1}x$.
>
> **2. The left factor.** By [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-3|Theorem §C5a.3.3]], $\bar\psi'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}$.
>
> **3. Multiply.** $\mathcal L'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}\Lambda_{1/2}[(i\slashed{\partial} - m)\psi](y) = \mathcal L(y)$.
>
> **4. The action.** A density with $\mathcal L'(x) = \mathcal L(\Lambda^{-1}x)$ gives an invariant action by [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-1|Theorem §C1.9.1]] (substitute $y = \Lambda^{-1}x$, Jacobian $\lvert\det\Lambda^{-1}\rvert = 1$).
>
> **What the derivation shows**
> - Each of the three slots of $\gamma^\mu$ is cancelled by a neighbour transforming with the inverse rule: the row spinor slot by $\bar\psi$, the column slot by $\psi$, the vector slot by $\partial_\mu$ (figure). The mass term uses only the spinor contraction. This is the spinor case of "invariant Lagrangians are $(0, 0)$ pieces" ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]).
> - Used next: the field equations (Theorem §C5a.3.6) are covariant because they come from an invariant action.

^der-c5a-3-5

*Uses:* [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-1|Theorem §C1.9.1]]

![[ph-qft-c5-3-1.svg]]
*Why $\bar\psi\,i\gamma^\mu\partial_\mu\psi$ is a scalar: each slot of $\gamma^\mu$ is contracted with a neighbour that transforms by the inverse rule (adapted from the user's PHY 513 notes, Ch. 8 §8.8).*

> [!theorem] Theorem §C5a.3.6: The Field Equations of the Dirac Lagrangian
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]:
> 1. the Euler–Lagrange equation ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-4|Theorem §C1.9.4]]) of the Dirac conjugate $\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-3|Def. §C5a.3.3]]) is the Dirac equation $(i\gamma^\mu\partial_\mu - m)\psi = 0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]);
> 2. the Euler–Lagrange equation of $\psi$ is the **conjugate Dirac equation**
>
> $$
> i\,\partial_\mu\bar\psi\,\gamma^\mu + m\bar\psi = 0 ;
> $$
>
> 3. each is the Hermitian conjugate of the other (multiplied by $\gamma^0$): they are one complex equation.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The equations of motion, and why the i is there", eq. (diracbarEOM)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.35) · Yu §5.3, eqs. (5.104)–(5.107) · PHY 513, Problem Set 5, Problem 4(a) (the conjugate equation, as the user wrote it)*

^thm-c5a-3-6

> [!derivation]- Derivation
> In components, $\mathcal L = \sum_{a,b}\bar\psi_a\bigl[i(\gamma^\nu)_{ab}\partial_\nu\psi_b - m\delta_{ab}\psi_b\bigr]$; the summed spacetime index is called $\nu$ to keep $\mu$ free ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^cau-c1-9-3|§C1.9, Caution: Rename the dummy index before differentiating]]).
>
> **1. Independent variables.** The eight real fields $\operatorname{Re}\psi_a$, $\operatorname{Im}\psi_a$ may be traded for $\psi_a$ and $\psi_a^{\ast}$ ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-9|Theorem §C1.9.9]], component by component), and $\psi^{\ast}$ for $\bar\psi_a = \sum_b\psi_b^{\ast}(\gamma^0)_{ba}$, an invertible linear change since $(\gamma^0)^2 = \mathbb 1$. So the Euler–Lagrange equations of $\bar\psi_a$ and of $\psi_a$ together are equivalent to those of the real components. (Here $\mathcal L$ is real only up to a divergence, Theorem §C5a.3.7; a divergence does not change the equations, [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-5|Theorem §C1.9.5]].)
>
> **2. Vary $\bar\psi$.** $\mathcal L$ contains no derivative of $\bar\psi$, so $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a) = 0$, and it is linear in $\bar\psi_a$: $\partial\mathcal L/\partial\bar\psi_a = [(i\gamma^\nu\partial_\nu - m)\psi]_a$. The Euler–Lagrange equation ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-4|Theorem §C1.9.4]]) $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\bar\psi_a)} - \frac{\partial\mathcal L}{\partial\bar\psi_a} = 0$ is $0 - [(i\slashed{\partial} - m)\psi]_a = 0$: part 1, for each $a$.
>
> **3. Vary $\psi$: the two partial derivatives.** $\partial(\partial_\nu\psi_b)/\partial(\partial_\mu\psi_c) = \delta^\mu{}_\nu\delta_{bc}$, so
>
> $$
> \frac{\partial\mathcal L}{\partial(\partial_\mu\psi_c)} = \sum_a\bar\psi_a\,i(\gamma^\mu)_{ac} = i(\bar\psi\gamma^\mu)_c, \qquad \frac{\partial\mathcal L}{\partial\psi_c} = -m\bar\psi_c .
> $$
>
> **4. Vary $\psi$: the equation.** $\partial_\mu[i(\bar\psi\gamma^\mu)_c] - (-m\bar\psi_c) = 0$; the $\gamma^\mu$ are constant, so $\partial_\mu$ acts on $\bar\psi$ only: $i(\partial_\mu\bar\psi)\gamma^\mu + m\bar\psi = 0$, part 2. Equivalently, integrate $\int d^4x\,\bar\psi\,i\gamma^\mu\partial_\mu\psi = -\int d^4x\,i(\partial_\mu\bar\psi)\gamma^\mu\psi$ by parts (surface term dropped: variations vanish on the boundary) and vary $\psi$ in the resulting expression, which no longer contains $\partial\psi$.
>
> **5. Conjugate part 2.** Write $\bar\psi = \psi^\dagger\gamma^0$: $i(\partial_\mu\psi^\dagger)\gamma^0\gamma^\mu + m\psi^\dagger\gamma^0 = 0$. Take the Hermitian conjugate (a row becomes a column; products reverse; $i \to -i$; $\partial_\mu$ is real):
>
> $$
> -i\,(\gamma^0\gamma^\mu)^\dagger\,\partial_\mu\psi + m\,\gamma^{0\dagger}\psi = 0 .
> $$
>
> **6. Simplify the matrices.** $\gamma^{0\dagger} = \gamma^0$ and $(\gamma^0\gamma^\mu)^\dagger = \gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu\gamma^0\gamma^0 = \gamma^0\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], then $(\gamma^0)^2 = \mathbb 1$). So step 5 reads $-\gamma^0(i\gamma^\mu\partial_\mu - m)\psi = 0$. Multiply by $-\gamma^0$: the Dirac equation. The steps reverse, so part 1 conjugates to part 2: part 3.
>
> **What the derivation shows**
> - "Treat $\psi$ and $\bar\psi$ as independent" is the complex-field device of [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-9|Theorem §C1.9.9]] with the invertible matrix $\gamma^0$ inserted; varying the conjugate gives the equation for the field directly, without derivatives to move.
> - ⚑ By-product: the agreement of the two equations needs both $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ and the $i$ in $\mathcal L$ → [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-3|Remark: Why the i]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^cau-c5a-3-2|Caution: The order of γ⁰ and γ^μ in the conjugate equation]].
> - The conjugate equation is itself covariant: it transforms like $\bar\psi$, with $\Lambda_{1/2}^{-1}$ on the right (conjugate Theorem §C5a.3.1 with Theorem §C5a.3.2).
> - Used next: both equations are needed for every conservation law of the field ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-11|Theorem §C5a.4.11]]); for plane waves part 2 becomes $\bar u(p)(\slashed{p} - m) = 0$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-9|Theorem §C5a.7.9]]).

^der-c5a-3-6

*Uses:* [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-4|Theorem §C1.9.4]], [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-5|Theorem §C1.9.5]], [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-9|Theorem §C1.9.9]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]

> [!caution] Caution: The order of γ⁰ and γ^μ in the conjugate equation
> The conjugate equation contains $\psi^\dagger\gamma^0\gamma^\mu$, so its adjoint contains $(\gamma^0\gamma^\mu)^\dagger = \gamma^0\gamma^\mu$, with $\gamma^0$ on the left where it factors out. The other order gives $(\gamma^\mu\gamma^0)^\dagger = \gamma^0\gamma^{\mu\dagger} = \gamma^\mu\gamma^0$, which equals $\gamma^0\gamma^\mu$ only for $\mu = 0$; using it flips the sign of the spatial derivatives (the slip was made and corrected in Lecture 8).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Caution "The order of $\gamma^0$ and $\gamma^\mu$ in the conjugate equation")*

^cau-c5a-3-2

> [!theorem] Theorem §C5a.3.7: The Dirac Lagrangian Is Real up to a Divergence
> For the density of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] and every (not necessarily on-shell) $C^1$ field,
>
> $$
> \mathcal L^* = \mathcal L - i\,\partial_\mu\bigl(\bar\psi\gamma^\mu\psi\bigr) ,
> $$
>
> so the action is real for fields falling off at infinity. Equivalently, the symmetric density
>
> $$
> \mathcal L_{\rm sym} = \tfrac i2\bigl(\bar\psi\gamma^\mu\partial_\mu\psi - \partial_\mu\bar\psi\,\gamma^\mu\psi\bigr) - m\bar\psi\psi = \mathcal L - \tfrac i2\,\partial_\mu(\bar\psi\gamma^\mu\psi)
> $$
>
> is real and gives the same field equations.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "Two further properties of the Dirac Lagrangian (additions to the lecture)") · Yu §5.3, eqs. (5.97)–(5.99)*

^thm-c5a-3-7

> [!derivation]- Derivation
> **1. Complex conjugate of a number is its adjoint.** Each term of $\mathcal L$ is a $1\times1$ matrix (row times matrix times column), so $z^{\ast} = z^\dagger$.
>
> **2. The kinetic term.** $(\bar\psi\gamma^\mu\partial_\mu\psi)^\dagger = (\psi^\dagger\gamma^0\gamma^\mu\partial_\mu\psi)^\dagger = (\partial_\mu\psi^\dagger)\gamma^{\mu\dagger}\gamma^0\psi$. With $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]] times $\gamma^0$ on the right) this is $(\partial_\mu\psi^\dagger)\gamma^0\gamma^\mu\psi = (\partial_\mu\bar\psi)\gamma^\mu\psi$ ($\gamma^0$ constant). Hence $(i\bar\psi\gamma^\mu\partial_\mu\psi)^{\ast} = -i(\partial_\mu\bar\psi)\gamma^\mu\psi$.
>
> **3. Product rule.** $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$, so $-i(\partial_\mu\bar\psi)\gamma^\mu\psi = i\bar\psi\gamma^\mu\partial_\mu\psi - i\partial_\mu(\bar\psi\gamma^\mu\psi)$.
>
> **4. The mass term.** $(\bar\psi\psi)^{\ast} = (\psi^\dagger\gamma^0\psi)^\dagger = \psi^\dagger\gamma^{0\dagger}\psi = \bar\psi\psi$: real.
>
> **5. Add.** $\mathcal L^{\ast} = i\bar\psi\gamma^\mu\partial_\mu\psi - i\partial_\mu(\bar\psi\gamma^\mu\psi) - m\bar\psi\psi = \mathcal L - i\partial_\mu(\bar\psi\gamma^\mu\psi)$.
>
> **6. The symmetric form.** $\frac12(\mathcal L + \mathcal L^{\ast})$ is real, and by step 5 equals $\mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$; expanding the derivative with step 3 gives $\mathcal L_{\rm sym}$. ⚑ By-product: $\mathcal L$ and $\mathcal L_{\rm sym}$ differ by a total divergence, so they have the same field equations ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-5|Theorem §C1.9.5]]) but different canonical momenta and canonical $T^{\mu\nu}$ (an improvement, [[§C1.11 Noether's Theorem#^thm-c1-11-4|Theorem §C1.11.4]]).
>
> **7. The action.** $\int d^4x\,\partial_\mu(\bar\psi\gamma^\mu\psi)$ is a surface integral (Gauss), zero for fields vanishing at infinity (fall-off faster than $r^{-3/2}$ in space suffices for the spatial part; the time boundary is the fixed initial and final data of the variational problem). So $S^{\ast} = S$.
>
> **What the derivation shows**
> - The $i$ is what makes the derivative term real: without it the kinetic term would equal minus its own conjugate up to a divergence, i.e. be imaginary.
> - Assumption used: $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, commuting (c-number) components. For anticommuting fields the same steps go through with the operator adjoint, $(AB)^\dagger = B^\dagger A^\dagger$ ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).

^der-c5a-3-7

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-5|Theorem §C1.9.5]]

> [!remark] Remark: Why the i
> Drop the $i$ and use $\mathcal L' = \bar\psi(\gamma^\mu\partial_\mu - m)\psi$. Varying $\bar\psi$ gives $(\slashed{\partial} - m)\psi = 0$; varying $\psi$ gives $(\partial_\mu\bar\psi)\gamma^\mu + m\bar\psi = 0$, whose adjoint, by steps 5–6 of Derivation §C5a.3.6 without the factor $i$, is $\gamma^0(\slashed{\partial} + m)\psi = 0$. The two equations together force $m\psi = 0$. With the $i$, conjugation supplies exactly the sign that reconciles them, and the same $i$ makes $\mathcal L$ real (Theorem §C5a.3.7). The $i$ is the spinor analogue of the $i$ in a quantum-mechanical $\psi^*i\partial_t\psi$: a first-order derivative term is anti-Hermitian, and needs an $i$ to become Hermitian.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The equations of motion, and why the i is there", last paragraph; "It is real, up to a total derivative")*

^rem-c5a-3-3

> [!theorem] Theorem §C5a.3.8: Canonical Momenta of the Dirac Field
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], with $\psi$ and $\bar\psi$ as the independent fields, the canonical momenta ([[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]]) are
>
> $$
> \pi_\psi \equiv \frac{\partial\mathcal L}{\partial(\partial_0\psi)} = i\bar\psi\gamma^0 = i\psi^\dagger, \qquad \pi_{\bar\psi} \equiv \frac{\partial\mathcal L}{\partial(\partial_0\bar\psi)} = 0 .
> $$
>
> The momentum is not a function of the velocity $\dot\psi$: the Legendre map is not invertible, and $\psi$ and $\psi^\dagger$ are themselves canonically conjugate.
>
> *Source: PS §3.5, p. 52, above eq. (3.84) · the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The Dirac energy–momentum tensor …": "the canonical momentum $\pi = \partial\mathcal L/\partial(\partial_t\psi) = i\psi^\dagger$"), Ch. 3 §3.4 ("Other fields")*

^thm-c5a-3-8

> [!derivation]- Derivation
> **1. The time-derivative part of $\mathcal L$.** Split the contraction: $\bar\psi i\gamma^\nu\partial_\nu\psi = \bar\psi i\gamma^0\partial_0\psi + \bar\psi i\gamma^j\partial_j\psi$; only the first term contains $\partial_0\psi$.
>
> **2. Differentiate.** Component by component, $\partial(\bar\psi_a i(\gamma^0)_{ab}\partial_0\psi_b)/\partial(\partial_0\psi_c) = i\bar\psi_a(\gamma^0)_{ac} = i(\bar\psi\gamma^0)_c$. With $\bar\psi\gamma^0 = \psi^\dagger(\gamma^0)^2 = \psi^\dagger$: $\pi_\psi = i\psi^\dagger$ (a row, one entry per component $\psi_c$).
>
> **3. $\bar\psi$.** $\mathcal L$ contains no derivative of $\bar\psi$: $\pi_{\bar\psi} = 0$.
>
> **What the derivation shows**
> - The momentum conjugate to $\psi$ is (essentially) $\psi^\dagger$: the complex scalar's crossover $\pi_\phi = \dot\phi^*$ ([[§C1.10 Hamiltonian Field Theory#^thm-c1-10-3|Theorem §C1.10.3]]) taken one step further, because $\mathcal L$ is first order in time ([[§C1.10 Hamiltonian Field Theory#^rem-c1-10-3|§C1.10, Remark: Constraints and first-order Lagrangians]]). Phase space is spanned by the values of $\psi$ alone; half as many data as for a second-order equation.
> - ⚑ By-product: the momenta depend on the choice among Lagrangians differing by a divergence: $\mathcal L_{\rm sym}$ of Theorem §C5a.3.7 gives $\pi_\psi = \frac i2\psi^\dagger$, $\pi_{\psi^\dagger} = -\frac i2\psi$. The equal-time brackets built from either agree once the constraint is taken into account; the course uses $\pi_\psi = i\psi^\dagger$.
> - Used next: the equal-time anticommutator $\{\psi_a(\mathbf x), \pi_{\psi,b}(\mathbf y)\} = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, i.e. $\{\psi_a, \psi_b^\dagger\} = \delta_{ab}\delta^3$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]).

^der-c5a-3-8

*Uses:* [[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]

> [!theorem] Theorem §C5a.3.9: The Hamiltonian Density of the Dirac Field
> With $\pi_\psi = i\psi^\dagger$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]]), the Hamiltonian density ([[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]]) of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] is
>
> $$
> \mathcal H \equiv \pi_\psi\,\dot\psi - \mathcal L = \bar\psi\bigl(-i\gamma^j\partial_j + m\bigr)\psi = \psi^\dagger\bigl(-i\boldsymbol\alpha\cdot\nabla + \beta m\bigr)\psi, \qquad \alpha^j = \gamma^0\gamma^j,\ \beta = \gamma^0 ,
> $$
>
> with $\boldsymbol\alpha$, $\beta$ Hermitian. On solutions of the Dirac equation $\mathcal H = i\psi^\dagger\partial_t\psi$. The bracket $H_{\text{s.p.}} = -i\boldsymbol\alpha\cdot\nabla + \beta m$ is the single-particle Hamiltonian (named and defined in [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]]; names across sources: [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|§C5b.1, Caution: Names for the single-particle Hamiltonian]]), the one-particle Dirac Hamiltonian of [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]], whose plane-wave eigenvalues are $\pm E_{\mathbf p}$: classically $\mathcal H$ is not bounded below.
>
> *Source: PS §3.5, eqs. (3.84)–(3.85) · the user's pre-course notes, §5.3 (note "First-order form: $\alpha$, $\beta$, and the positive density") · the user's PHY 513 notes, Ch. 3 §3.5 (table of canonical tensors; $T^{00} = i\psi^\dagger\partial_t\psi$)*

^thm-c5a-3-9

> [!derivation]- Derivation
> **1. Legendre transform.** By [[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]] summed over both fields, $\mathcal H = \pi_\psi\dot\psi + \pi_{\bar\psi}\dot{\bar\psi} - \mathcal L = i\psi^\dagger\partial_0\psi + 0 - \mathcal L$ (Theorem §C5a.3.8).
>
> **2. Expand $\mathcal L$ into time and space parts.** $\mathcal L = i\bar\psi\gamma^0\partial_0\psi + i\bar\psi\gamma^j\partial_j\psi - m\bar\psi\psi$, and $i\bar\psi\gamma^0\partial_0\psi = i\psi^\dagger(\gamma^0)^2\partial_0\psi = i\psi^\dagger\partial_0\psi$.
>
> **3. Subtract.** The two $i\psi^\dagger\partial_0\psi$ cancel: $\mathcal H = -i\bar\psi\gamma^j\partial_j\psi + m\bar\psi\psi = \bar\psi(-i\gamma^j\partial_j + m)\psi$. (No equation of motion was used: the time derivatives cancel identically, as they must for a first-order Lagrangian.)
>
> **4. Write with $\psi^\dagger$.** $\bar\psi = \psi^\dagger\gamma^0$: $\mathcal H = \psi^\dagger(-i\gamma^0\gamma^j\partial_j + m\gamma^0)\psi$, with $\partial_j = \partial/\partial x^j$ the components of $\nabla$: $\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$.
>
> **5. Hermiticity of $\alpha$, $\beta$.** $\beta^\dagger = \gamma^{0\dagger} = \gamma^0$. $(\gamma^0\gamma^j)^\dagger = \gamma^{j\dagger}\gamma^0 = (-\gamma^j)\gamma^0 = \gamma^0\gamma^j$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]; distinct $\gamma$'s anticommute).
>
> **6. On shell.** Multiply the Dirac equation by $\gamma^0$: $i\partial_0\psi = (-i\gamma^0\gamma^j\partial_j + m\gamma^0)\psi = H_{\text{s.p.}}\psi$. Hence $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi = i\psi^\dagger\partial_t\psi$.
>
> **7. The spectrum of $H_{\text{s.p.}}$.** For $\psi \propto e^{i\mathbf p\cdot\mathbf x}$, $H_{\text{s.p.}} \to \boldsymbol\alpha\cdot\mathbf p + \beta m$; its square is $\mathbf p^2 + m^2$ because $\{\alpha^i, \alpha^j\} = 2\delta^{ij}$, $\{\alpha^i, \beta\} = 0$, $\beta^2 = 1$ (from the Clifford algebra: $\{\gamma^0\gamma^i, \gamma^0\gamma^j\} = -\gamma^i\gamma^j - \gamma^j\gamma^i = 2\delta^{ij}$; $\gamma^0\gamma^i\gamma^0 + \gamma^0\gamma^0\gamma^i = -\gamma^i + \gamma^i = 0$). So its eigenvalues are $\pm E_{\mathbf p}$, each twice (traceless, [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-2|Theorem §C5a.5.2]]). ⚑ By-product: a negative-frequency solution has negative classical energy $\int\psi^\dagger H_{\text{s.p.}}\psi < 0$; no ordering of commuting fields cures this ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]), and the cure is anticommutation ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]).
>
> **What the derivation shows**
> - The first-order (Hamiltonian) form $i\partial_t\psi = H_{\text{s.p.}}\psi$ is the Dirac equation multiplied by $\gamma^0$: Dirac's original equation, with the algebra of $\boldsymbol\alpha$, $\beta$ derived from the Clifford algebra rather than postulated.
> - ⚑ By-product: $\mathcal L = 0$ on shell, so $\mathcal H = \pi\dot\psi$ there; the same fact simplifies the energy–momentum tensor ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-11|Theorem §C5a.4.11]]).
> - Used next: $H = \int d^3x\,\mathcal H$ in mode form ([[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]]); $\mathcal H = T^{00}$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-12|Theorem §C5a.4.12]]).

^der-c5a-3-9

*Uses:* [[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-8|Theorem §C5a.3.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-2|Theorem §C5a.5.2]]

This is Quantum Mechanics' $H = c\boldsymbol\alpha\cdot\mathbf p + \beta mc^2$ ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]) as a density sandwiched between fields: there it is a postulated one-particle Hamiltonian acting on a wave function, here a derived density of a classical field whose integral becomes, after quantization, the Hamiltonian of the many-particle theory (rule 2: the layer changes from principle to theorem; the meaning of $\psi$ changes from amplitude to field).

## Dirac implies Klein–Gordon

> [!theorem] Theorem §C5a.3.10: Every Dirac Solution Solves the Klein–Gordon Equation
> If $\psi \in C^2$ solves the Dirac equation $(i\slashed{\partial} - m)\psi = 0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]; slash [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]), then each of its four components satisfies the Klein–Gordon equation ([[§C1.9 The Action Principle and the Euler–Lagrange Equations#^mod-c1-9-6|Model §C1.9.6]])
>
> $$
> \bigl(\partial^2 + m^2\bigr)\psi_a = 0 , \qquad\text{because}\qquad \bigl(-i\slashed{\partial} - m\bigr)\bigl(i\slashed{\partial} - m\bigr) = \partial^2 + m^2 .
> $$
>
> The identity uses only the Clifford algebra ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]). So $m^2$ is the Klein–Gordon mass squared; the sign of $m$ is a convention. The converse fails.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (Derivation "Every solution of the Dirac equation solves the Klein–Gordon equation", eq. (diracKG)) · PHY 513 Lecture 8, Part C ("Klein-Gordon Equation from Dirac Equation") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.110)–(5.111)*

^thm-c5a-3-10

> [!derivation]- Derivation
> **1. Apply the sign-flipped operator.** Act on $0 = (i\gamma^\mu\partial_\mu - m)\psi$ with $-i\gamma^\nu\partial_\nu - m$ (summed index renamed $\nu$). A linear differential operator applied to zero gives zero; this needs $\psi \in C^2$ (or a distribution, where derivatives always exist, [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]).
>
> **2. Expand into all four terms.** The $\gamma$'s are constant matrices, so derivatives pass through them:
>
> $$
> (-i\gamma^\nu\partial_\nu)(i\gamma^\mu\partial_\mu) = \gamma^\nu\gamma^\mu\partial_\nu\partial_\mu, \quad (-i\gamma^\nu\partial_\nu)(-m) = +im\gamma^\nu\partial_\nu, \quad (-m)(i\gamma^\mu\partial_\mu) = -im\gamma^\mu\partial_\mu, \quad (-m)(-m) = m^2 ,
> $$
>
> using $(-i)(i) = 1$. The two middle terms are the same operator ($\nu$ and $\mu$ are dummies) with opposite signs: they cancel.
>
> **3. Symmetrize.** Let $T = \gamma^\nu\gamma^\mu\partial_\nu\partial_\mu$. Renaming the dummies $\nu \leftrightarrow \mu$, $T = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \gamma^\mu\gamma^\nu\partial_\nu\partial_\mu$, using $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ on $C^2$ functions. Averaging the two forms, $T = \frac12\{\gamma^\nu, \gamma^\mu\}\partial_\nu\partial_\mu$.
>
> **4. Clifford algebra.** $\frac12\{\gamma^\nu, \gamma^\mu\} = g^{\nu\mu}\mathbb 1$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]]), so $T = g^{\nu\mu}\partial_\nu\partial_\mu\mathbb 1 = \partial^2\mathbb 1$, and $0 = (\partial^2 + m^2)\mathbb 1\,\psi$: the identity matrix does not mix components.
>
> **5. The sign of $m$.** Only $(-m)(-m) = m^2$ entered. ⚑ By-product: $\psi \mapsto \gamma^5\psi$ maps solutions with mass $m$ to solutions with mass $-m$, since $\gamma^5$ anticommutes with $\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]): $(i\slashed{\partial} + m)\gamma^5\psi = -\gamma^5(i\slashed{\partial} - m)\psi$. The sign of $m$ in the Dirac equation is a convention, fixed here by $m \ge 0$.
>
> **6. The converse fails.** A Klein–Gordon solution $w\,e^{-ip\cdot x}$ with an arbitrary constant column $w$ need not satisfy the Dirac equation, which imposes $(\slashed{p} - m)w = 0$ ([[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-1|Theorem §C5a.5.1]]). ⚑ By-product: Dirac halves the Klein–Gordon solutions → [[§C5a.3 The Dirac Equation and Its Lagrangian#^rem-c5a-3-4|Remark: Eight candidates, four solutions]].
>
> **What the derivation shows**
> - The Dirac operator is a square root of the Klein–Gordon operator up to the sign flip; this is the property the Clifford algebra was built for ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^rem-c5a-2-1|§C5a.2, Remark: A square root of p²]]). In momentum space it is $(-\slashed{p} - m)(\slashed{p} - m) = -(p^2 - m^2)$.
> - Assumption used: $C^2$ (or distributional) fields; constant $\gamma$'s.
> - Used next: every component of a Dirac solution is a superposition of plane waves on the mass shell ([[§C5a.5 Plane-Wave Solutions|§C5a.5]]); the Dirac propagator is $(i\slashed{\partial} + m)$ applied to a scalar one ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]).

^der-c5a-3-10

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-1|Theorem §C5a.5.1]]

Quantum Mechanics runs the same computation backwards: there, requiring each component to obey Klein–Gordon is what forces $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ ([[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], part 1). Here the Clifford algebra is the input, found from the Lorentz group ([[§C5a.2 The Clifford Algebra and the Dirac Representation|§C5a.2]]), and Klein–Gordon is the consequence (rule 2: same identity, opposite logical direction).

> [!remark] Remark: Eight candidates, four solutions
> Klein–Gordon does not mix components, so for a fixed $\mathbf p$ it allows eight candidates: four independent columns, times $e^{-ip\cdot x}$ or $e^{+ip\cdot x}$ with $p^0 = +E_{\mathbf p}$. The Dirac equation turns them into the algebraic conditions $(\slashed{p} - m)u = 0$ and $(\slashed{p} + m)v = 0$. On the shell $(\slashed{p} + m)(\slashed{p} - m) = p^2 - m^2 = 0$, so neither matrix is invertible, and their ranks add to four; each has a two-dimensional kernel. The count therefore halves evenly:
>
> | | candidates (Klein–Gordon) | solutions (Dirac) | interpretation (preview) |
> |---|---|---|---|
> | $e^{-ip\cdot x}$, positive frequency | 4 | 2 | a spin-½ particle, two spin states |
> | $e^{+ip\cdot x}$, negative frequency | 4 | 2 | the antiparticle, two spin states |
>
> The same count from the eigenvalues $\pm m$ of $\slashed{p}$, each twice, is [[§C5a.5 Plane-Wave Solutions#^thm-c5a-5-2|Theorem §C5a.5.2]]; in what sense a general solution is a superposition of these plane waves (an integral over $\mathbf p$, convergent in $\mathcal S'$) is [[§C5a.5 Plane-Wave Solutions#^rem-c5a-5-6|§C5a.5, Remark: In what sense a general solution is a superposition of these plane waves]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (Derivation "Eight candidates, four solutions") · PHY 513 Lecture 8, Part C ("Interpretation of Solutions: Preview")*

^rem-c5a-3-4

> [!remark] Remark: Negative frequency and antiparticles
> The negative-frequency solutions cannot be discarded: they are needed to build a general solution, as $e^{+ip\cdot x}$ was for the scalar ([[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]). Classically they carry negative energy (Theorem §C5a.3.9); after quantization with anticommutators they describe *positive*-energy antiparticles of opposite charge ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]); the lecture's analogy is the current in a wire, carried by negative electrons moving the other way. This is how Dirac was led to the positron (predicted 1931, observed by Anderson in 1932; [[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]). The free equations are symmetric between matter and antimatter; why the universe is not is a question of initial conditions or of other dynamics.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (paragraph "Negative energy, antiparticles, and what the equations do not decide") · PHY 513 Lecture 8, Part C*

^rem-c5a-3-5

> [!remark] Remark: In what sense the equations hold
> For the classical field of this section $\psi$ is a $C^2$ function falling off at spatial infinity, and every statement holds pointwise. Plane waves $u\,e^{-ip\cdot x}$ are not in that class; they solve the Dirac equation pointwise but are tempered distributions as fields on spacetime ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]), and the Dirac operator acts on them through distributional derivatives, $\langle\partial_\mu T, f\rangle = -\langle T, \partial_\mu f\rangle$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), which here agree with ordinary ones. Covariance (Theorem §C5a.3.1) holds in $\mathcal S'$ because linear changes of variables are defined there ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]). The quantized field is an operator-valued distribution ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]) and satisfies the Dirac equation smeared with test functions ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-2|Def. §C5b.1.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]).
>
> *Source: written here from [[§CA.2 Generalized Functions|§CA.2]]*

^rem-c5a-3-6

> [!remark]- Connections
> - Quantum Mechanics postulates the Dirac equation for a four-component wave function, with $\boldsymbol\alpha$, $\beta$ chosen to make the equation first order and the density positive; here $\psi$ is a field, the $\gamma$'s and the covariance come from the Lorentz group, the equation follows from a Lagrangian, and $\psi^\dagger\psi$ loses its probability meaning to become a charge density — [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]], [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]].
> - $\gamma^0$ is to the Dirac spinor slot what $g_{\mu\nu}$ is to a vector slot: both are indefinite forms preserved by the group, and both are needed because the Lorentz group is noncompact — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|Theorem §C3.2.12]], [[§C1.4 The Lorentz Group#^def-c1-4-1|Def. §C1.4.1]].
> - Treating $\psi$ and $\bar\psi$ as independent is the complex scalar's device; the first-order Lagrangian pushes the crossover of momenta to its end, $\pi_\psi = i\psi^\dagger$, which is why fermions are quantized by a bracket between $\psi$ and $\psi^\dagger$ alone — [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-9|Theorem §C1.9.9]], [[§C1.10 Hamiltonian Field Theory#^rem-c1-10-3|§C1.10, Remark: Constraints and first-order Lagrangians]], [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].
> - The unbounded classical energy of Theorem §C5a.3.9 is the Dirac version of the indefinite Klein–Gordon density of Quantum Mechanics; in both cases the field theory reinterprets negative frequency as antiparticles, but only anticommutators make the Dirac Hamiltonian positive — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]].
> - "Dirac implies Klein–Gordon" is what makes the scalar machinery reusable: the mass shell, the invariant measure and the contour rules carry over, and the Dirac propagator is $(i\slashed{\partial} + m)$ times the scalar Feynman propagator — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription|§C2b.6]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[P2 Green's Functions by Contour Integration]].
> - A Lagrangian that is real only up to a divergence, and momenta that change with the divergence, are the field version of adding a total time derivative to a mechanical Lagrangian; the physics (equations, charges) is unchanged, the canonical currents shift by improvements — [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^thm-c1-9-5|Theorem §C1.9.5]], [[§C1.11 Noether's Theorem#^thm-c1-11-4|Theorem §C1.11.4]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-14|Theorem §C5a.4.14]].
> - The procedure of canonical quantization starts from exactly the data assembled here (Lagrangian, momenta, Hamiltonian density) — [[P1 Canonical Quantization#^p1-1|P1, step 1]].
