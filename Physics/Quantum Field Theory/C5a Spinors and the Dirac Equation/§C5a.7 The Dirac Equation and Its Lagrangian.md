---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.6 The Dirac Conjugate and the Bilinears]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.4 (Lecture 8's starting point), §8.5 (The Dirac equation), §8.6 (Why the Dirac equation is covariant), §8.8 (The Dirac Lagrangian), §8.10 (The Weyl form of the Dirac equation), §8.11 (Dirac implies Klein–Gordon) · PHY 513 Lecture 8 (Larsen), Parts A–C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.2, pp. 41–44, eqs. (3.29)–(3.44), §3.5, p. 52, eqs. (3.83)–(3.85) · Yu Zhao-Huan, 量子场论讲义, §5.2–§5.3, eqs. (5.72), (5.102)–(5.115) · PHY 513 Lecture 10, slide 16, and the user's PHY 513 notes, Ch. 10 §10.5 (the single-particle Hamiltonian) · the user's pre-course notes, §5.3 · the basis-change statements written here.*

Which first-order field equation can a Dirac spinor obey, why does it look the same to every observer and in every basis, and from which Lagrangian does it follow? The structure of spinor space is complete after [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]]: the Clifford action, the Dirac form and $\bar\psi$, the Lorentz action $\Lambda_{1/2}$ with the key identity $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]), chirality and the bilinears. This section adds **layer 8**, fields $\psi : M \to V$: the Dirac equation and its covariance, its form invariance under a change of basis of $V$, the single-particle Hamiltonian $H_{\text{s.p.}}$, the Dirac Lagrangian with its field equations (also basis independent, for unitary changes of basis), the fact that every solution obeys the Klein–Gordon equation, and the equation in two-component form with the Weyl equations. The action principle and the Euler–Lagrange equations are [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]], whose models are scalar. The canonical momenta, the Hamiltonian density and the Noether currents of this Lagrangian are [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]]; the solutions [[§C5a.9 Plane-Wave Solutions|§C5a.9]]. The mathematics it uses — the Dirac matrices and their covariance, $\gamma^5$, Hermitian bases and the invariance of the Dirac form — is [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules|§CB.10]]–[[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]] and [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]], shown in the blocks below.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+,-,-,-)$, active Lorentz transformations ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]), $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]). In this section $\psi$ is a classical field with commuting complex components; the quantized field, with anticommuting components, is [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The mathematics used here

The Dirac equation is built from the Dirac matrices; the matrix of the Dirac maps in any basis is what Theorem §C5a.7.2 transforms:

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-12]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-14]]

![[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^der-cb-10-14]]

Its covariance (Theorem §C5a.7.1) rests on the $\gamma$'s rotating as a vector, infinitesimally and finitely:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-16]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-16]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7b]]

$\gamma^5$ and its properties (Theorem §C5a.7.2), and Pauli's theorem behind the closing remark on what depends on the basis:

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14]]

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^der-cb-11-14]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-12]]

## The Dirac equation

> [!definition] Definition §C5a.7.1: The Dirac Equation
> A **Dirac field** $\psi(x)$ is a four-component field transforming as $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$, with $\Lambda_{1/2}$ the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; spinor fields, [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]; Lorentz transformations read actively, [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]). The **Dirac equation** is
>
> $$
> \bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi(x) = 0, \qquad\text{in components}\qquad \bigl[i(\gamma^\mu)_{ab}\,\partial_\mu - m\,\delta_{ab}\bigr]\psi_b(x) = 0, \quad a = 1, \dots, 4 ,
> $$
>
> with $\gamma^\mu$ the Dirac matrices ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]; the course uses the chiral basis, [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]) and $m$ a real constant times the $4\times4$ identity: four coupled, first-order, linear partial differential equations. The matrix of differential operators $i\gamma^\mu\partial_\mu - m$ is the **Dirac operator**.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.5 (Definition "The Dirac equation", eq. (dirac)) · PHY 513 Lecture 8, Part A ("Introducing the Dirac Equation") · PS §3.2, eq. (3.31) · Yu §5.3, eqs. (5.107)–(5.108)*

^def-c5a-7-1

> [!definition] Definition §C5a.7.2: Feynman Slash
> For any four-vector $a_\mu$ (numbers, or operators commuting with the $\gamma$'s, such as $\partial_\mu$),
>
> $$
> \slashed{a} \equiv \gamma^\mu a_\mu = \gamma^0a_0 + \gamma^ia_i ,
> $$
>
> a $4\times4$ matrix built from the Dirac matrices ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]). In particular $\slashed{p} = \gamma^\mu p_\mu$, $\slashed{\partial} = \gamma^\mu\partial_\mu$, and the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) reads $(i\slashed{\partial} - m)\psi = 0$. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]) $\slashed{p} = \begin{pmatrix}0 & p\cdot\sigma\\ p\cdot\bar\sigma & 0\end{pmatrix}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Definition "Feynman slash") · PHY 513 Lecture 9 ("Notation: $\gamma^\mu p_\mu \equiv \slashed{p}$") · PS §3.3, p. 49 · Yu §5.4, eq. (5.146) · PHY 513, Problem Set 5, Problem 2 (closing note on notation, as the user wrote it)*

^def-c5a-7-2

The chiral form uses $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]) with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]: $\gamma^\mu p_\mu$ has upper-right block $\sigma^\mu p_\mu = p\cdot\sigma$. The square $\slashed{a}^{\,2} = a^2$ is [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-12|Theorem §CB.10.12]]; the rest of the slash algebra is [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]. The slash is a contraction, so $\slashed{a}$ is "invariant" only in the sense of [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|Remark: What covariance shows and what it does not]]: it is a matrix whose two spinor slots still transform.

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

^cau-c5a-7-1

> [!remark] Remark: What covariance shows and what it does not
> Theorem §C5a.7.1 below shows that the Dirac equation is **covariant**: if $\psi$ solves it, so does the transformed field, with the same matrices $\gamma^\mu$ and the same $m$. That makes it a consistent candidate for a law of motion, not a proof that nature uses it. Covariance needs $m$ to be a Lorentz scalar; that $m$ is the mass is Theorem §C5a.7.8. The explicit $i$ is not required by covariance; it is required by consistency with the conjugate equation and by reality of the Lagrangian ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|Remark: Why the i]]). Expressions such as $\slashed{\partial}$ or $\slashed{p}$ are called "Lorentz invariant" in the lecture in the sense that every vector index is contracted; they remain matrices whose spinor slots transform, $\Lambda_{1/2}\slashed{p}\,\Lambda_{1/2}^{-1} = (\Lambda p)\!\!\!/$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]] read with $\Lambda^{-1}$). What is invariant is the *form* of a relation between such matrices.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.5 (Principle "What has been shown, and what has not"), Ch. 9 §9.4 (Caution "In what sense $\slashed{p}$ is 'Lorentz invariant'")*

^rem-c5a-7-1

## Covariance, and form invariance under a change of basis

> [!theorem] Theorem §C5a.7.1: The Dirac Equation Is Covariant
> Let $\psi$ be a $C^1$ four-component field and $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]). Then
>
> $$
> \bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi'(x) = \Lambda_{1/2}\,\bigl[\bigl(i\gamma^\nu\partial_\nu - m\bigr)\psi\bigr](\Lambda^{-1}x) ,
> $$
>
> with the same $\gamma^\mu$ and the same $m$ on both sides. Hence $\psi'$ solves the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) if and only if $\psi$ does; in particular $\gamma^\mu\partial_\mu\psi$ transforms exactly like $\psi$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.6 (Derivation "Covariance of the Dirac equation, the lecture's way", Steps 4–5) · PHY 513 Lecture 8, Part A ("Relativistic Invariance of the Dirac Equation") · PS §3.2, p. 42 · Yu §5.3, eq. (5.109)*

^thm-c5a-7-1

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
> **3. Push $\Lambda_{1/2}$ to the left.** Insert $\mathbb 1 = \Lambda_{1/2}\Lambda_{1/2}^{-1}$ in front: $\gamma^\mu\Lambda_{1/2} = \Lambda_{1/2}\bigl(\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}\bigr) = \Lambda_{1/2}\,\Lambda^\mu{}_\rho\gamma^\rho$ by [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]. So
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
> **5. The mass term.** $m\psi'(x) = m\Lambda_{1/2}\psi(y) = \Lambda_{1/2}\,m\psi(y)$, because $m$ multiplies the identity and commutes with $\Lambda_{1/2}$. ⚑ By-product: this step needs $m$ to be the same number in every frame, a Lorentz scalar; a term $v^\mu\gamma_\mu$ with a fixed vector $v$ would fail step 4 (no $\partial$ to absorb $\Lambda$) → [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|Remark: What covariance shows and what it does not]].
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
> - The whole content is one identity, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: $\gamma^\mu$ is an invariant tensor with one vector slot and two spinor slots, and "contract the vector index with $\partial_\mu$" is the rule that builds a spinor out of a spinor ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]).
> - ⚑ By-product: $\Lambda_{1/2}$ is fixed by $\Lambda$ only up to sign ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-4|§C3.3, Remark: Why a spinor's matrix is fixed only up to sign]]); the equation is linear and homogeneous, so both signs give the same statement.
> - Assumption: $\psi \in C^1$. For a distribution the same computation holds term by term, since derivatives and linear changes of variables are defined on $\mathcal S'$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
> - Used next: the Lagrangian is a scalar (Theorem §C5a.7.4); the same push-through gives the transformation of every bilinear ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).

^der-c5a-7-1

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]

The slides phrase the transformation passively ("the physical point that the field is evaluated at does not change but its coordinates do") while the formula is written actively; the two readings give the same formula ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]). Quantum Mechanics records the same check with $\hbar$, $c$ and a passive transformation, for one boost ([[§C13.2★ The Dirac Equation#^rem-c13-2-4|QM Remark: Lorentz covariance and the rapidity]]); here it holds for every $\omega$ because the identity of Theorem §CB.17.7 is proved for the whole group.

> [!theorem] Theorem §C5a.7.2: The Dirac Equation Keeps Its Form When ψ and γ Change Together
> Let $\psi(x)$ be a $C^1$ field with values in $V$, with columns $\psi(x)$ and $\psi'(x) = U\psi(x)$ in two bases and Dirac matrices $\gamma^\mu$, $\gamma'^\mu = U\gamma^\mu U^{-1}$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-14|Theorem §CB.10.14]]). Then
>
> $$
> \bigl(i\gamma'^\mu\partial_\mu - m\bigr)\psi'(x) = U\,\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi(x) ,
> $$
>
> so $\psi'$ solves the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) with $\gamma'$ iff $\psi$ solves it with $\gamma$: the equation is the basis-free statement $(i\Gamma^\mu\partial_\mu - m)\psi = 0$ about a $V$-valued field.
>
> *Source: Yu §5.2, eq. (5.72) (the similarity transformation of the $\gamma$'s) · PS §3.2, p. 41 · the derivation written here*

^thm-c5a-7-2

> [!derivation]- Derivation
> **1. The derivative passes through U.** $U$ is a constant matrix, so $\partial_\mu\psi'(x) = \partial_\mu(U\psi(x)) = U\partial_\mu\psi(x)$, component by component: $\partial_\mu\sum_bU_{ab}\psi_b = \sum_bU_{ab}\partial_\mu\psi_b$.
>
> **2. The kinetic term.** $\gamma'^\mu\partial_\mu\psi' = U\gamma^\mu U^{-1}U\partial_\mu\psi = U\gamma^\mu\partial_\mu\psi$ (insert step 1, cancel $U^{-1}U = \mathbb 1$).
>
> **3. The mass term.** $m\psi' = mU\psi = U(m\psi)$ ($m$ is a number times $\mathbb 1$, which commutes with $U$).
>
> **4. Combine.** $(i\gamma'^\mu\partial_\mu - m)\psi' = U(i\gamma^\mu\partial_\mu - m)\psi$. $U$ is invertible, so one side vanishes iff the other does.
>
> **5. ⚑ By-product: changing γ without ψ breaks solutions.** Take $U = \gamma^5$, which is unitary and its own inverse with $\gamma^5\gamma^\mu\gamma^5 = -\gamma^\mu$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]]): the new matrices $\gamma'^\mu = -\gamma^\mu$ are a legitimate set of Dirac matrices. If $\psi$ solves the old equation, $i\gamma^\mu\partial_\mu\psi = m\psi$, and its columns are kept unchanged while only the $\gamma$'s are replaced, then $(i\gamma'^\mu\partial_\mu - m)\psi = -i\gamma^\mu\partial_\mu\psi - m\psi = -2m\psi \ne 0$ for $m \ne 0$, $\psi \ne 0$. The correctly transformed spinor $\psi' = \gamma^5\psi$ does solve it, by step 4. A solution is a pair (matrices, columns) in one basis.
>
> **What the derivation shows**
> - The form invariance needs only that $U$ is constant and invertible; unitarity is not used. (A position-dependent $U(x)$ would produce an extra term $i\gamma'^\mu(\partial_\mu U)U^{-1}\psi'$, the seed of a connection — not needed in flat spacetime with a global basis.)
> - Used next: Lagrangian (Theorem §C5a.7.5), which does need unitarity.

^der-c5a-7-2

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-14|Theorem §CB.10.14]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]]

## The single-particle Hamiltonian

> [!definition] Definition §C5a.7.3: Single-Particle Hamiltonian
> The **single-particle Hamiltonian** of the Dirac equation is the $4\times4$ matrix differential operator
>
> $$
> H_{\text{s.p.}} \equiv \gamma^0\bigl(-i\boldsymbol\gamma\cdot\nabla + m\bigr) = -i\boldsymbol\alpha\cdot\nabla + \beta m, \qquad \boldsymbol\gamma\cdot\nabla \equiv \gamma^j\partial_j, \quad \boldsymbol\alpha = \gamma^0\boldsymbol\gamma, \ \beta = \gamma^0 ,
> $$
>
> the kernel of the Hamiltonian density of the Dirac field, $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi$ (derived from the Lagrangian in [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]]). It is Hermitian ($\boldsymbol\alpha$, $\beta$ Hermitian: [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], step 5 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-2|Derivation §C5a.8.2]]), and on $e^{i\mathbf p\cdot\mathbf x}$ it acts as the matrix $H_{\text{s.p.}}(\mathbf p) = \gamma^0(\gamma^jp^j + m)$ (names in other sources: [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-2|Caution: Names for the single-particle Hamiltonian]]). It is the Hamiltonian that relativistic quantum mechanics takes for a four-component wave function ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]).
>
> *Source: Lecture 10, slide 16 · the user's PHY 513 notes, Ch. 10 §10.5 (Definition "The single-particle Hamiltonian"; there $\gamma^0\gamma^i$ is called anti-Hermitian: it is Hermitian, $(\gamma^0\gamma^i)^\dagger = \gamma^{i\dagger}\gamma^0 = -\gamma^i\gamma^0 = \gamma^0\gamma^i$, Step 5 of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-8-2|Derivation §C5a.8.2]], which is what makes $\gamma^0\gamma^i(-i\partial_i)$ Hermitian) · PS §3.5, eq. (3.85)*

^def-c5a-7-3

> [!caution] Caution: Names for the single-particle Hamiltonian
> One operator, several names. These notes write $H_{\text{s.p.}}$ everywhere, as Lecture 10 (slide 16) and the user's PHY 513 notes (Ch. 10 §10.5) do; Peskin–Schroeder write the bracket of eq. (3.84), $-i\gamma^0\boldsymbol\gamma\cdot\nabla + m\gamma^0$, and name it $h_D = -i\boldsymbol\alpha\cdot\nabla + m\beta$ in eq. (3.85), "the Dirac Hamiltonian of one-particle quantum mechanics"; earlier drafts of this vault followed them, with $h_D$ for it and $h(\mathbf p)$ for its momentum-space form, now $H_{\text{s.p.}}(\mathbf p)$. Quantum Mechanics (Sakurai) also calls it the Dirac Hamiltonian, $H = c\,\boldsymbol\alpha\cdot\mathbf p + \beta mc^2$, acting on a four-component wave function ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]). In momentum space, with $\hbar = c = 1$, $H_{\text{s.p.}}(\mathbf p) = \boldsymbol\alpha\cdot\mathbf p + \beta m = \gamma^0(\gamma^jp^j + m)$. Not to be confused with the field Hamiltonian $\hat H = \int d^3x\,\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$, an operator on Fock space ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]), or with the density $\mathcal H$.
>
> *Source: Lecture 10, slide 16 · the user's PHY 513 notes, Ch. 10 §10.5 · PS §3.5, eq. (3.85) · Sakurai, eqs. (8.51)–(8.53), as in QM §C13.2★*

^cau-c5a-7-2

### The mathematics used here: the Lagrangian

The Lagrangian is a scalar because the Dirac form is invariant, and keeps its form under exactly the changes of basis that keep the Dirac form (Theorem §C5a.7.5):

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-11]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-18]]

![[§CB.12 Complex Clifford Algebras and Clifford Modules#^der-cb-12-18]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13b]]

## The Dirac Lagrangian

> [!model] Model §C5a.7.3: The Free Dirac Field
> A Dirac field $\psi$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) with the Lagrangian density ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|Def. §C1b.2.1]])
>
> $$
> \mathcal L = \bar\psi\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi = i\bar\psi\slashed{\partial}\psi - m\bar\psi\psi ,
> $$
>
> where $\bar\psi$ is the Dirac conjugate ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) and $\slashed{\partial}$ the slash ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]); $\psi$ and $\bar\psi$ are varied as independent fields. Its field equation is the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]]).
>
> *Assumptions:* classical field with commuting complex components (anticommuting after quantization, [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]); free (quadratic $\mathcal L$, linear equation); $m \ge 0$ a real parameter, the mass ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]]; the sign of $m$ is a convention); kinetic term normalized without a factor, which fixes $[\psi] = \frac32$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]); variations vanishing on the boundary; flat spacetime.
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Definition "The Dirac Lagrangian", eq. (diracL)) · PHY 513 Lecture 8, Part B ("The Dirac Lagrangian") · PS §3.2, eq. (3.34) · Yu §5.3, eq. (5.103)*

^mod-c5a-7-3

It is the spinor entry of the list that began with the scalar fields [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]] and [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], previewed in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-7|§C1b.2, Remark: One equation for every kind of field]]. Two differences from the scalar: $\mathcal L$ is first order in derivatives, so it is linear in the velocities, and it vanishes on solutions ($\mathcal L = \bar\psi\cdot0$). The mass dimension $[\psi] = \frac32$ and its consequence, a coupling of dimension $-2$ for a four-fermion term $(\bar\psi\psi)^2$ (the Fermi constant), are [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]] and [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]].

> [!theorem] Theorem §C5a.7.4: The Dirac Lagrangian Is a Lorentz Scalar
> Under $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]), the density of [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] obeys
>
> $$
> \mathcal L'(x) \equiv \bar\psi'(x)\bigl(i\slashed{\partial} - m\bigr)\psi'(x) = \mathcal L(\Lambda^{-1}x) ,
> $$
>
> the law of a scalar field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]); so the action $S = \int d^4x\,\mathcal L$ is Lorentz invariant ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Definition "The Dirac Lagrangian"; Figure "Why $\bar\psi\,i\gamma^\mu\partial_\mu\psi$ is a scalar") · PHY 513 Lecture 8, Part B ("Proof of invariance") · Yu §5.3, eq. (5.102)*

^thm-c5a-7-4

> [!derivation]- Derivation
> **1. The right factor.** By [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], $(i\slashed{\partial} - m)\psi'(x) = \Lambda_{1/2}[(i\slashed{\partial} - m)\psi](y)$, $y = \Lambda^{-1}x$.
>
> **2. The left factor.** By [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], $\bar\psi'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}$.
>
> **3. Multiply.** $\mathcal L'(x) = \bar\psi(y)\Lambda_{1/2}^{-1}\Lambda_{1/2}[(i\slashed{\partial} - m)\psi](y) = \mathcal L(y)$.
>
> **4. The action.** A density with $\mathcal L'(x) = \mathcal L(\Lambda^{-1}x)$ gives an invariant action by [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]] (substitute $y = \Lambda^{-1}x$, Jacobian $\lvert\det\Lambda^{-1}\rvert = 1$).
>
> **What the derivation shows**
> - Each of the three slots of $\gamma^\mu$ is cancelled by a neighbour transforming with the inverse rule: the row spinor slot by $\bar\psi$, the column slot by $\psi$, the vector slot by $\partial_\mu$ (figure). The mass term uses only the spinor contraction. This is the spinor case of "invariant Lagrangians are $(0, 0)$ pieces" ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]).
> - Used next: the field equations (Theorem §C5a.7.6) are covariant because they come from an invariant action.

^der-c5a-7-4

*Uses:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]

![[ph-qft-c5-3-1.svg]]
*Why $\bar\psi\,i\gamma^\mu\partial_\mu\psi$ is a scalar: each slot of $\gamma^\mu$ is contracted with a neighbour that transforms by the inverse rule (adapted from the user's PHY 513 notes, Ch. 8 §8.8).*

> [!theorem] Theorem §C5a.7.5: The Dirac Lagrangian under a Change of Basis
> With the hypotheses of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]], the old basis Hermitian ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-11|Def. §CB.12.11]]) and $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]):
>
> $$
> \mathcal L' \equiv \psi'^\dagger\gamma'^0\bigl(i\gamma'^\mu\partial_\mu - m\bigr)\psi' = \psi^\dagger\,(U^\dagger U)\,\gamma^0\bigl(i\gamma^\mu\partial_\mu - m\bigr)\psi .
> $$
>
> For $m \ne 0$, $\mathcal L' = \mathcal L$ for every field iff $U$ is unitary; for $U = \sqrt c\,W$ ($W$ unitary), $\mathcal L' = c\,\mathcal L$.
>
> *Source: the derivation written here, from Theorems §C5a.2.2 and §C5a.7.2 · PS §3.2, p. 41 (unitary equivalence)*

^thm-c5a-7-5

> [!derivation]- Derivation
> **1. The left factor.** $\psi'^\dagger\gamma'^0 = \psi^\dagger U^\dagger\,U\gamma^0U^{-1}$ (Theorem §C5a.2.2, step 1).
>
> **2. The right factor.** $(i\gamma'^\mu\partial_\mu - m)\psi' = U(i\gamma^\mu\partial_\mu - m)\psi$ (Theorem §C5a.7.2).
>
> **3. Multiply.** $\mathcal L' = \psi^\dagger U^\dagger U\gamma^0U^{-1}U(i\gamma^\mu\partial_\mu - m)\psi = \psi^\dagger(U^\dagger U)\gamma^0(i\gamma^\mu\partial_\mu - m)\psi$.
>
> **4. When equal.** If $U^\dagger U = \mathbb 1$, $\mathcal L' = \psi^\dagger\gamma^0(\cdots)\psi = \mathcal L$. Conversely, let $m \ne 0$ and $\mathcal L' = \mathcal L$ for all fields. Take constant fields ($\partial_\mu\psi = 0$): $-m\,\psi^\dagger A\psi = 0$ for every column $\psi$, with $A = (U^\dagger U - \mathbb 1)\gamma^0$. Over $\mathbb C$ a matrix with $\psi^\dagger A\psi = 0$ for all $\psi$ is zero (polarization, [[§23 Self-Adjoint and Normal Operators#^ladr-7-13|LADR Thm. 7.13]]), so $(U^\dagger U - \mathbb 1)\gamma^0 = 0$, and multiplying by $\gamma^0$ on the right, $U^\dagger U = \mathbb 1$. If $U^\dagger U = c\mathbb 1$, step 3 gives $c\mathcal L$.
>
> **What the derivation shows**
> - The field equation is basis independent for every invertible $U$ (Theorem §C5a.7.2), the Lagrangian only for unitary $U$. A factor $c$ rescales the action, which changes the normalization of the field (the canonical anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]] would acquire $1/c$), not the dynamics.
> - The Lorentz scalar property of $\mathcal L$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-4|Theorem §C5a.7.4]]) is a different statement: there the basis is fixed and the field is moved (Caution: Three different transformations).

^der-c5a-7-5

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-2|Theorem §C5a.7.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-13|LADR Thm. 7.13]]

> [!theorem] Theorem §C5a.7.6: The Field Equations of the Dirac Lagrangian
> For [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]:
> 1. the Euler–Lagrange equation ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]) of the Dirac conjugate $\bar\psi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) is the Dirac equation $(i\gamma^\mu\partial_\mu - m)\psi = 0$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]);
> 2. the Euler–Lagrange equation of $\psi$ is the **conjugate Dirac equation**
>
> $$
> i\,\partial_\mu\bar\psi\,\gamma^\mu + m\bar\psi = 0 ;
> $$
>
> 3. each is the Hermitian conjugate of the other (multiplied by $\gamma^0$): they are one complex equation.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The equations of motion, and why the i is there", eq. (diracbarEOM)) · PHY 513 Lecture 8, Part B · PS §3.2, eq. (3.35) · Yu §5.3, eqs. (5.104)–(5.107) · PHY 513, Problem Set 5, Problem 4(a) (the conjugate equation, as the user wrote it)*

^thm-c5a-7-6

> [!derivation]- Derivation
> In components, $\mathcal L = \sum_{a,b}\bar\psi_a\bigl[i(\gamma^\nu)_{ab}\partial_\nu\psi_b - m\delta_{ab}\psi_b\bigr]$; the summed spacetime index is called $\nu$ to keep $\mu$ free ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]]).
>
> **1. Independent variables.** The eight real fields $\operatorname{Re}\psi_a$, $\operatorname{Im}\psi_a$ may be traded for $\psi_a$ and $\psi_a^{\ast}$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], component by component), and $\psi^{\ast}$ for $\bar\psi_a = \sum_b\psi_b^{\ast}(\gamma^0)_{ba}$, an invertible linear change since $(\gamma^0)^2 = \mathbb 1$. So the Euler–Lagrange equations of $\bar\psi_a$ and of $\psi_a$ together are equivalent to those of the real components. (Here $\mathcal L$ is real only up to a divergence, Theorem §C5a.7.7; a divergence does not change the equations, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]].)
>
> **2. Vary $\bar\psi$.** $\mathcal L$ contains no derivative of $\bar\psi$, so $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a) = 0$, and it is linear in $\bar\psi_a$: $\partial\mathcal L/\partial\bar\psi_a = [(i\gamma^\nu\partial_\nu - m)\psi]_a$. The Euler–Lagrange equation ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]) $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\bar\psi_a)} - \frac{\partial\mathcal L}{\partial\bar\psi_a} = 0$ is $0 - [(i\slashed{\partial} - m)\psi]_a = 0$: part 1, for each $a$.
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
> **6. Simplify the matrices.** $\gamma^{0\dagger} = \gamma^0$ and $(\gamma^0\gamma^\mu)^\dagger = \gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu\gamma^0\gamma^0 = \gamma^0\gamma^\mu$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], then $(\gamma^0)^2 = \mathbb 1$). So step 5 reads $-\gamma^0(i\gamma^\mu\partial_\mu - m)\psi = 0$. Multiply by $-\gamma^0$: the Dirac equation. The steps reverse, so part 1 conjugates to part 2: part 3.
>
> **What the derivation shows**
> - "Treat $\psi$ and $\bar\psi$ as independent" is the complex-field device of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]] with the invertible matrix $\gamma^0$ inserted; varying the conjugate gives the equation for the field directly, without derivatives to move.
> - ⚑ By-product: the agreement of the two equations needs both $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ and the $i$ in $\mathcal L$ → [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-2|Remark: Why the i]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-3|Caution: The order of γ⁰ and γ^μ in the conjugate equation]].
> - The conjugate equation is itself covariant: it transforms like $\bar\psi$, with $\Lambda_{1/2}^{-1}$ on the right (conjugate Theorem §C5a.7.1 with Theorem §CB.17.13).
> - Used next: both equations are needed for every conservation law of the field ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|Theorem §C5a.8.5]]); for plane waves part 2 becomes $\bar u(p)(\slashed{p} - m) = 0$ ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]]).

^der-c5a-7-6

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]

> [!caution] Caution: The order of γ⁰ and γ^μ in the conjugate equation
> The conjugate equation contains $\psi^\dagger\gamma^0\gamma^\mu$, so its adjoint contains $(\gamma^0\gamma^\mu)^\dagger = \gamma^0\gamma^\mu$, with $\gamma^0$ on the left where it factors out. The other order gives $(\gamma^\mu\gamma^0)^\dagger = \gamma^0\gamma^{\mu\dagger} = \gamma^\mu\gamma^0$, which equals $\gamma^0\gamma^\mu$ only for $\mu = 0$; using it flips the sign of the spatial derivatives (the slip was made and corrected in Lecture 8).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Caution "The order of $\gamma^0$ and $\gamma^\mu$ in the conjugate equation")*

^cau-c5a-7-3

> [!theorem] Theorem §C5a.7.7: The Dirac Lagrangian Is Real up to a Divergence
> For the density of [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] and every (not necessarily on-shell) $C^1$ field,
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

^thm-c5a-7-7

> [!derivation]- Derivation
> **1. Complex conjugate of a number is its adjoint.** Each term of $\mathcal L$ is a $1\times1$ matrix (row times matrix times column), so $z^{\ast} = z^\dagger$.
>
> **2. The kinetic term.** $(\bar\psi\gamma^\mu\partial_\mu\psi)^\dagger = (\psi^\dagger\gamma^0\gamma^\mu\partial_\mu\psi)^\dagger = (\partial_\mu\psi^\dagger)\gamma^{\mu\dagger}\gamma^0\psi$. With $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]] times $\gamma^0$ on the right) this is $(\partial_\mu\psi^\dagger)\gamma^0\gamma^\mu\psi = (\partial_\mu\bar\psi)\gamma^\mu\psi$ ($\gamma^0$ constant). Hence $(i\bar\psi\gamma^\mu\partial_\mu\psi)^{\ast} = -i(\partial_\mu\bar\psi)\gamma^\mu\psi$.
>
> **3. Product rule.** $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$, so $-i(\partial_\mu\bar\psi)\gamma^\mu\psi = i\bar\psi\gamma^\mu\partial_\mu\psi - i\partial_\mu(\bar\psi\gamma^\mu\psi)$.
>
> **4. The mass term.** $(\bar\psi\psi)^{\ast} = (\psi^\dagger\gamma^0\psi)^\dagger = \psi^\dagger\gamma^{0\dagger}\psi = \bar\psi\psi$: real.
>
> **5. Add.** $\mathcal L^{\ast} = i\bar\psi\gamma^\mu\partial_\mu\psi - i\partial_\mu(\bar\psi\gamma^\mu\psi) - m\bar\psi\psi = \mathcal L - i\partial_\mu(\bar\psi\gamma^\mu\psi)$.
>
> **6. The symmetric form.** $\frac12(\mathcal L + \mathcal L^{\ast})$ is real, and by step 5 equals $\mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$; expanding the derivative with step 3 gives $\mathcal L_{\rm sym}$. ⚑ By-product: $\mathcal L$ and $\mathcal L_{\rm sym}$ differ by a total divergence, so they have the same field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]) but different canonical momenta and canonical $T^{\mu\nu}$ (an improvement, [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]]).
>
> **7. The action.** $\int d^4x\,\partial_\mu(\bar\psi\gamma^\mu\psi)$ is a surface integral (Gauss), zero for fields vanishing at infinity (fall-off faster than $r^{-3/2}$ in space suffices for the spatial part; the time boundary is the fixed initial and final data of the variational problem). So $S^{\ast} = S$.
>
> **What the derivation shows**
> - The $i$ is what makes the derivative term real: without it the kinetic term would equal minus its own conjugate up to a divergence, i.e. be imaginary.
> - Assumption used: $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$, commuting (c-number) components. For anticommuting fields the same steps go through with the operator adjoint, $(AB)^\dagger = B^\dagger A^\dagger$ ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]).

^der-c5a-7-7

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]

> [!remark] Remark: Why the i
> Drop the $i$ and use $\mathcal L' = \bar\psi(\gamma^\mu\partial_\mu - m)\psi$. Varying $\bar\psi$ gives $(\slashed{\partial} - m)\psi = 0$; varying $\psi$ gives $(\partial_\mu\bar\psi)\gamma^\mu + m\bar\psi = 0$, whose adjoint, by steps 5–6 of Derivation §C5a.7.6 without the factor $i$, is $\gamma^0(\slashed{\partial} + m)\psi = 0$. The two equations together force $m\psi = 0$. With the $i$, conjugation supplies exactly the sign that reconciles them, and the same $i$ makes $\mathcal L$ real (Theorem §C5a.7.7). The $i$ is the spinor analogue of the $i$ in a quantum-mechanical $\psi^*i\partial_t\psi$: a first-order derivative term is anti-Hermitian, and needs an $i$ to become Hermitian.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The equations of motion, and why the i is there", last paragraph; "It is real, up to a total derivative")*

^rem-c5a-7-2

## Dirac implies Klein–Gordon

> [!theorem] Theorem §C5a.7.8: Every Dirac Solution Solves the Klein–Gordon Equation
> If $\psi \in C^2$ solves the Dirac equation $(i\slashed{\partial} - m)\psi = 0$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]; slash [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]), then each of its four components satisfies the Klein–Gordon equation ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]])
>
> $$
> \bigl(\partial^2 + m^2\bigr)\psi_a = 0 , \qquad\text{because}\qquad \bigl(-i\slashed{\partial} - m\bigr)\bigl(i\slashed{\partial} - m\bigr) = \partial^2 + m^2 .
> $$
>
> The identity uses only the Clifford algebra ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]). So $m^2$ is the Klein–Gordon mass squared; the sign of $m$ is a convention. The converse fails.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (Derivation "Every solution of the Dirac equation solves the Klein–Gordon equation", eq. (diracKG)) · PHY 513 Lecture 8, Part C ("Klein-Gordon Equation from Dirac Equation") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.110)–(5.111)*

^thm-c5a-7-8

> [!derivation]- Derivation
> **1. Apply the sign-flipped operator.** Act on $0 = (i\gamma^\mu\partial_\mu - m)\psi$ with $-i\gamma^\nu\partial_\nu - m$ (summed index renamed $\nu$). A linear differential operator applied to zero gives zero; this needs $\psi \in C^2$ (or a distribution, where derivatives always exist, [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]).
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
> **4. Clifford algebra.** $\frac12\{\gamma^\nu, \gamma^\mu\} = g^{\nu\mu}\mathbb 1$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]]), so $T = g^{\nu\mu}\partial_\nu\partial_\mu\mathbb 1 = \partial^2\mathbb 1$, and $0 = (\partial^2 + m^2)\mathbb 1\,\psi$: the identity matrix does not mix components.
>
> **5. The sign of $m$.** Only $(-m)(-m) = m^2$ entered. ⚑ By-product: $\psi \mapsto \gamma^5\psi$ maps solutions with mass $m$ to solutions with mass $-m$, since $\gamma^5$ anticommutes with $\gamma^\mu$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]]): $(i\slashed{\partial} + m)\gamma^5\psi = -\gamma^5(i\slashed{\partial} - m)\psi$. The sign of $m$ in the Dirac equation is a convention, fixed here by $m \ge 0$.
>
> **6. The converse fails.** A Klein–Gordon solution $w\,e^{-ip\cdot x}$ with an arbitrary constant column $w$ need not satisfy the Dirac equation, which imposes $(\slashed{p} - m)w = 0$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|Theorem §C5a.9.1]]). ⚑ By-product: Dirac halves the Klein–Gordon solutions → [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-3|Remark: Eight candidates, four solutions]].
>
> **What the derivation shows**
> - The Dirac operator is a square root of the Klein–Gordon operator up to the sign flip; this is the property the Clifford algebra was built for ([[§C5a.1 Spinor Space and the Clifford Action#^rem-c5a-1-2|§C5a.1, Remark: A square root of p²]]). Conversely, asking for such a factor forces the Clifford relation ([[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]]). In momentum space it is $(-\slashed{p} - m)(\slashed{p} - m) = -(p^2 - m^2)$.
> - Assumption used: $C^2$ (or distributional) fields; constant $\gamma$'s.
> - Used next: every component of a Dirac solution is a superposition of plane waves on the mass shell ([[§C5a.9 Plane-Wave Solutions|§C5a.9]]); the Dirac propagator is $(i\slashed{\partial} + m)$ applied to a scalar one ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]).

^der-c5a-7-8

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-11|Def. §CB.10.11]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-14|Theorem §CB.11.14]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|Theorem §C5a.9.1]]

Quantum Mechanics runs the same computation backwards: there, requiring each component to obey Klein–Gordon is what forces $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ ([[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], part 1). Here the Clifford algebra is the input, found from the Lorentz group ([[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]), and Klein–Gordon is the consequence (rule 2: same identity, opposite logical direction).

> [!remark] Remark: Eight candidates, four solutions
> Klein–Gordon does not mix components, so for a fixed $\mathbf p$ it allows eight candidates: four independent columns, times $e^{-ip\cdot x}$ or $e^{+ip\cdot x}$ with $p^0 = +E_{\mathbf p}$. The Dirac equation turns them into the algebraic conditions $(\slashed{p} - m)u = 0$ and $(\slashed{p} + m)v = 0$. On the shell $(\slashed{p} + m)(\slashed{p} - m) = p^2 - m^2 = 0$, so neither matrix is invertible, and their ranks add to four; each has a two-dimensional kernel. The count therefore halves evenly:
>
> | | candidates (Klein–Gordon) | solutions (Dirac) | interpretation (preview) |
> |---|---|---|---|
> | $e^{-ip\cdot x}$, positive frequency | 4 | 2 | a spin-½ particle, two spin states |
> | $e^{+ip\cdot x}$, negative frequency | 4 | 2 | the antiparticle, two spin states |
>
> The same count from the eigenvalues $\pm m$ of $\slashed{p}$, each twice, is [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]]; in what sense a general solution is a superposition of these plane waves (an integral over $\mathbf p$, convergent in $\mathcal S'$) is [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-6|§C5a.9, Remark: In what sense a general solution is a superposition of these plane waves]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (Derivation "Eight candidates, four solutions") · PHY 513 Lecture 8, Part C ("Interpretation of Solutions: Preview")*

^rem-c5a-7-3

> [!remark] Remark: Negative frequency and antiparticles
> The negative-frequency solutions cannot be discarded: they are needed to build a general solution, as $e^{+ip\cdot x}$ was for the scalar ([[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]). Classically they carry negative energy (Theorem §C5a.8.2); after quantization with anticommutators they describe *positive*-energy antiparticles of opposite charge ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]); the lecture's analogy is the current in a wire, carried by negative electrons moving the other way. This is how Dirac was led to the positron (predicted 1931, observed by Anderson in 1932; [[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]). The free equations are symmetric between matter and antimatter; why the universe is not is a question of initial conditions or of other dynamics.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.11 (paragraph "Negative energy, antiparticles, and what the equations do not decide") · PHY 513 Lecture 8, Part C*

^rem-c5a-7-4

> [!remark] Remark: In what sense the equations hold
> For the classical field of this section $\psi$ is a $C^2$ function falling off at spatial infinity, and every statement holds pointwise. Plane waves $u\,e^{-ip\cdot x}$ are not in that class; they solve the Dirac equation pointwise but are tempered distributions as fields on spacetime ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]), and the Dirac operator acts on them through distributional derivatives, $\langle\partial_\mu T, f\rangle = -\langle T, \partial_\mu f\rangle$ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), which here agree with ordinary ones. Covariance (Theorem §C5a.7.1) holds in $\mathcal S'$ because linear changes of variables are defined there ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]). The quantized field is an operator-valued distribution ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]) and satisfies the Dirac equation smeared with test functions ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-5|Def. §C5b.1.5]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]).
>
> *Source: written here from [[§CA.2 Generalized Functions|§CA.2]]*

^rem-c5a-7-5

### The mathematics used here: the Weyl halves

The Weyl form splits spinor space by $\gamma^5$; Model §C5a.7.11 has no parity symmetry because parity exchanges the two copies, and the ★ remark on a Majorana mass uses that complex conjugation exchanges them:

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-4]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-10]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-11]]

## The Weyl form and the Weyl equations

> [!theorem] Theorem §C5a.7.9: Bilinears in Weyl Components
> For $\psi = (\psi_L, \psi_R)$, $\chi = (\chi_L, \chi_R)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]; Weyl halves [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]), $\bar\psi = (\psi_R^\dagger, \psi_L^\dagger)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) and
>
> $$
> \bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R, \qquad \bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R ,
> $$
>
> $$
> \bar\psi\gamma^\mu\gamma^5\chi = -\psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R, \qquad \bar\psi\,i\gamma^5\chi = i\bigl(\psi_L^\dagger\chi_R - \psi_R^\dagger\chi_L\bigr) .
> $$
>
> Hence the Dirac Lagrangian ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) is
>
> $$
> \mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m\bigl(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L\bigr) :
> $$
>
> the kinetic terms keep the chiralities apart, the mass term pairs them.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 ("This is the Dirac invariant": $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$), §8.10 · PS §3.2, eqs. (3.36), (3.42)*

^thm-c5a-7-9

> [!derivation]- Derivation
> In the chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).
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
> - The invariant form $\gamma^0$ of [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]] *is* the pairing of a left- with a right-handed slot ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]]): a Lorentz scalar without derivatives must couple $\psi_L$ to $\psi_R$, so a Dirac mass needs both ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]]).
> - The vector current splits into a left and a right current with no cross terms; the axial current is their difference. Both statements are basis independent by [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]: $\bar\psi\gamma^\mu\psi = \bar\psi\gamma^\mu P_L\psi + \bar\psi\gamma^\mu P_R\psi$.

^der-c5a-7-9

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]

> [!theorem] Theorem §C5a.7.10: The Dirac Equation in Two-Component Form
> For $\psi = (\psi_L, \psi_R)$ in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) is equivalent to
>
> $$
> i\bar\sigma^\mu\partial_\mu\psi_L = m\,\psi_R, \qquad i\sigma^\mu\partial_\mu\psi_R = m\,\psi_L ,
> $$
>
> with $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], i.e. $i(\partial_0 - \boldsymbol\sigma\cdot\nabla)\psi_L = m\psi_R$, $i(\partial_0 + \boldsymbol\sigma\cdot\nabla)\psi_R = m\psi_L$. The kinetic operators act within each Weyl block; only the mass couples them.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Derivation "The Dirac equation in two-component form", eq. (weylcoupled)) · PHY 513 Lecture 8, Part C ("Dirac Equation in 2-Component Form") · PS §3.2, eqs. (3.39), (3.43) · Yu §5.3, eqs. (5.113)–(5.114)*

^thm-c5a-7-10

> [!derivation]- Derivation
> **1. The operator in blocks.** With $\gamma^\mu = \begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix}$ and $-m\mathbb 1_4 = \operatorname{diag}(-m\mathbb 1_2, -m\mathbb 1_2)$,
>
> $$
> i\gamma^\mu\partial_\mu - m = \begin{pmatrix}-m & i\sigma^\mu\partial_\mu\\ i\bar\sigma^\mu\partial_\mu & -m\end{pmatrix} .
> $$
>
> **2. Act on the column.** $\begin{pmatrix}-m & i\sigma\cdot\partial\\ i\bar\sigma\cdot\partial & -m\end{pmatrix}\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix} = \begin{pmatrix}i\sigma^\mu\partial_\mu\psi_R - m\psi_L\\ i\bar\sigma^\mu\partial_\mu\psi_L - m\psi_R\end{pmatrix}$, which vanishes exactly when both stated equations hold.
>
> **3. In components.** $\sigma^\mu\partial_\mu = \mathbb 1\partial_0 + \sigma^i\partial_i = \partial_0 + \boldsymbol\sigma\cdot\nabla$ and $\bar\sigma^\mu\partial_\mu = \partial_0 - \boldsymbol\sigma\cdot\nabla$ (no metric: upper index on $\sigma$, lower on $\partial$; [[§C5a.7 The Dirac Equation and Its Lagrangian#^cau-c5a-7-1|§C5a.7, Caution: γ^μ∂_μ has a plus sign]]).
>
> **What the derivation shows**
> - Representation theory allows the two blocks to be treated separately ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]); the equation of motion couples them, through the mass and only through it (figure).
> - The same equations follow by varying $\psi_L^\dagger$ and $\psi_R^\dagger$ in the Lagrangian of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]].

^der-c5a-7-10

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]

![[ph-qft-c5-4-1.svg]]
*The Dirac equation in two-component form: the Weyl halves are separate representations, and the mass is the only coupling between them (adapted from the user's PHY 513 notes, Ch. 8 §8.10).*

> [!model] Model §C5a.7.11: The Weyl Fields
> A **left-handed Weyl field** is a two-component field $\psi_L$ in $(\frac12, 0)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]; Weyl matrices [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]) with
>
> $$
> \mathcal L_L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L, \qquad i\bar\sigma^\mu\partial_\mu\psi_L = 0 ;
> $$
>
> a **right-handed Weyl field** $\psi_R$ in $(0, \frac12)$ has $\mathcal L_R = i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R$ and $i\sigma^\mu\partial_\mu\psi_R = 0$. These are the **Weyl equations**.
>
> *Assumptions:* $m = 0$ (the two blocks of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]] decouple, and either may be kept alone, consistently both as a representation and dynamically); classical, free; no parity symmetry (parity exchanges the two, [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-10|Theorem §CB.16.10]]).
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations", eq. (weyl)) · PHY 513 Lecture 8, Part C ("Weyl Equation") · PS §3.2, eqs. (3.40), (3.44) · Yu §5.3, eq. (5.115)*

^mod-c5a-7-11

The 513 notes box the Weyl equations as a principle; here they are a model, the massless idealization of the Dirac theory (or, in the Standard Model, the starting point). Each component of a Weyl solution obeys the massless Klein–Gordon equation, by $(\sigma\cdot\partial)(\bar\sigma\cdot\partial) = \partial^2$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]), the two-component version of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-8|Theorem §C5a.7.8]].

> [!theorem] Theorem §C5a.7.12: Weyl Plane Waves Have Fixed Helicity
> Let $\psi_L = \xi\,e^{-ip\cdot x}$ with $p^0 > 0$ and a constant nonzero two-spinor $\xi$. It solves the left-handed Weyl equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]) if and only if $p^2 = 0$ ($p^0 = \lvert\mathbf p\rvert$) and
>
> $$
> \bigl(\hat{\mathbf p}\cdot\boldsymbol\sigma\bigr)\,\xi = -\xi :
> $$
>
> helicity ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]) $h = \hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2 = -\frac12$. For $\psi_R = \eta\,e^{-ip\cdot x}$, $p^2 = 0$ and $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = +\eta$, $h = +\frac12$. One Weyl field has one helicity for its positive-frequency solutions.
>
> *Source: the user's pre-course notes, §5.3 ("Weyl spinors": "$(E + \boldsymbol\sigma\cdot\mathbf p)\eta = 0$, i.e. $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = -\eta$: helicity $-\frac12$") · Yu §5.3 (paragraph after eq. (5.115)) · the user's PHY 513 notes, Ch. 8 §8.10 (Principle "The Weyl equations": "a single Weyl field describes a massless particle of one helicity")*

^thm-c5a-7-12

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
> **6. Helicity.** For spin $\frac12$ the spin operator in each Weyl block is $\frac12\boldsymbol\sigma$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), so the spin along $\hat{\mathbf p}$ is $\hat{\mathbf p}\cdot\boldsymbol\sigma/2 = \mp\frac12$ ([[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]).
>
> **What the derivation shows**
> - Chirality and helicity coincide for massless positive-frequency solutions: left-handed means helicity $-\frac12$. For the negative-frequency solutions $\xi\,e^{+ip\cdot x}$ the condition is the same, $(p^0 + \boldsymbol\sigma\cdot\mathbf p)\xi = 0$ (step 1 with $p \to -p$ gives $-(\bar\sigma\cdot p)\xi = 0$); after quantization they describe the antiparticle, which carries the opposite helicity $+\frac12$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]): the neutrino–antineutrino pair of [[§C3.7★ Massless Particles and Helicity|§C3.7★]].
> - ⚑ By-product: half the components of a Weyl spinor are removed for each momentum; a Weyl field has one physical polarization per momentum, the minimal content of a massless spin-½ particle (the little-group count of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]]).
> - For massive Dirac spinors helicity is frame dependent; it approaches chirality at high energy ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]]).
> - Assumption: the plane wave solves the Weyl equation pointwise; as a field on spacetime it is not square integrable but a tempered distribution, and the equation holds also in $\mathcal S'$, as for the Dirac plane waves ([[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-5|§C5a.7, Remark: In what sense the equations hold]]).

^der-c5a-7-12

*Uses:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]]

> [!remark] Remark: When the Weyl description is useful
> Not for the electron of Dirac's problem: in hydrogen the electron's kinetic energy is tiny compared with its mass, and the mass couples the two halves at full strength. It is natural where the mass is zero or small, as for neutrinos: in the Standard Model the neutrinos are massless and only left-handed ones exist. Their observed small masses require going beyond it. A mass of the form of [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]], a *Dirac* mass, needs a separate right-handed field.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (paragraph "When is the Weyl description useful?") · PHY 513 Lecture 8, Part C*

^rem-c5a-7-6

> [!remark]- ★ Remark: A Majorana mass needs no second field
> By [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-11|Theorem §CB.16.11]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]], $\sigma^2\psi_L^{\ast}$ transforms like a right-handed spinor, so a single left-handed field can supply its own partner: $\psi_L^{\mathsf T}\varepsilon\,\psi_L$ is Lorentz invariant, because $\Lambda_L^{\mathsf T}\varepsilon\Lambda_L = (\det\Lambda_L)\varepsilon = \varepsilon$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]). This is a *Majorana* mass. For commuting components it vanishes identically, $\psi^{\mathsf T}\varepsilon\psi = \psi_1\psi_2 - \psi_2\psi_1 = 0$ (with $\varepsilon^{12} = 1$); it exists only for anticommuting fields ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]; Majorana fields, QFT C9, planned). Whether neutrino masses are of Dirac or Majorana type is not known.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.10 (Caution "'A neutrino mass needs a right-handed neutrino'")*

^rem-c5a-7-7

## What depends on the basis

> [!remark] Remark: What depends on the basis and what does not
>
> | depends on the basis of $V$ | does not depend on it |
> |---|---|
> | the entries of $\gamma^\mu$, $\gamma^5$, $S^{\mu\nu}$, $\Lambda_{1/2}$ | the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ (Theorem §CB.10.14) |
> | the components $\psi_a$ of a spinor, $u^s_a(p)$, $v^s_a(p)$ | the spinor $\psi \in V$ itself; the solution space of the Dirac equation (Theorem §C5a.7.2) |
> | "upper and lower components" and what they mean | the eigenspaces of $\Gamma^5$ (the Weyl halves, [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1\|Theorem §C5a.5.1]], 3) and of $\Gamma^0$ |
> | "$\gamma^0$ is off-diagonal", "$\gamma^5$ is diagonal", "$S^{\mu\nu}$ is block diagonal" | traces such as $\operatorname{tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$, determinants, eigenvalues: $\pm1$ twice for $\gamma^0$ and $\gamma^5$, $\pm i$ twice for $\gamma^i$ (Theorems §CB.0.12, §CB.11.9, §C5a.5.1) |
> | whether $\psi^\dagger\gamma^0\chi$ is the Dirac form (fails for non-unitary $U$) | the Dirac form $\bar\psi\chi$ and every bilinear $\bar\psi\Gamma\chi$, under unitary $U$ (Theorem §C5a.2.2) |
> | the matrix form of the Lagrangian | $\mathcal L$, the action and the field equations, under unitary $U$ (Theorem §C5a.7.5) |
> | — | every physical prediction: cross sections, energies, charges are built from traces and bilinears |
>
> Pauli's theorem ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-12|Theorem §CB.12.12]]) puts every possible set of Dirac matrices in the left column of a single row: each is the chiral set after a change of basis (Theorem §CB.12.14), so a basis-independent statement proved in the chiral basis holds in all of them. The Dirac basis of Quantum Mechanics is such a basis ([[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]]; [[§C5a.5 Chirality and Weyl Spinors#^cau-c5a-5-2|§C5a.5, Caution: Bases and conventions across the sources]]).
>
> *Source: PS §3.2, p. 41 · the user's PHY 513 notes, Ch. 8 §8.1 ("the choice of basis is a convention, like the choice of basis for spin-½"), §8.2 (Caution on "particle" and "antiparticle" components) · the table written here*

^rem-c5a-7-8

> [!remark]- Connections
> - Quantum Mechanics postulates the Dirac equation for a four-component wave function, with $\boldsymbol\alpha$, $\beta$ chosen to make the equation first order and the density positive; here $\psi$ is a field, the $\gamma$'s and the covariance come from the Lorentz group, the equation follows from a Lagrangian, and $\psi^\dagger\psi$ loses its probability meaning to become a charge density — [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]], [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]].
> - "Dirac implies Klein–Gordon" is what makes the scalar machinery reusable: the mass shell, the invariant measure and the contour rules carry over, and the Dirac propagator is $(i\slashed{\partial} + m)$ times the scalar Feynman propagator — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription|§C2b.6]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[P2 Green's Functions by Contour Integration]].
> - Theorem §C5a.7.8 is one direction of an equivalence: a first-order operator with constant coefficients is a factor of the Klein–Gordon operator exactly when its coefficients satisfy the Clifford relation, and then they must be non-commuting matrices of size at least four — [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-1|Theorem §C5a.0.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^thm-c5a-0-3|Theorem §C5a.0.3]].
> - A Lagrangian that is real only up to a divergence, and momenta that change with the divergence, are the field version of adding a total time derivative to a mechanical Lagrangian; the physics (equations, charges) is unchanged, the canonical currents shift by improvements — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]].
> - The canonical structure of this Lagrangian (momenta, Hamiltonian density) and its Noether currents (vector, axial, energy–momentum with the field-form $H$ and $\mathbf P$, spin) are collected in one place, in the order of the scalar's, and quantization starts from them — [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]], [[P1 Canonical Quantization#^p1-1|P1, steps 1–3]].
> - Chirality is a property of the Lorentz representation, helicity of a state; the Weyl equation ties them for massless particles, which is why a single Weyl field realizes one helicity of Wigner's massless classification — [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-6|Theorem §C3.7.6]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]].
> - Mass breaks chiral symmetry because it pairs left with right; the same statement in group language is that $\gamma^0$, the invariant form, swaps the Weyl blocks — [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-2|§C5a.5, Remark: Kinematics allows one handedness, a mass needs both]].
> - A basis of $V$ chosen independently at each point, $U = U(x)$, would spoil the form invariance by a term $(\partial_\mu U)U^{-1}$ (Derivation §C5a.7.2); compensating it needs a connection — the spin connection of field theory in curved spacetime, outside this course.
