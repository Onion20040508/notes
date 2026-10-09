---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.9 Plane-Wave Solutions]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.11 Gamma-Matrix Technology]] →

*Sources: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis (Problem Set 5, Problem 6)"), §9.4 (Normalization and spin sums), §9.5 (Negative-frequency solutions: normalizations, orthogonality, spin sum, "Why neither spin sum is the identity"), §9.7 (Summary) and "Correspondence with Yu" · PHY 513 Lecture 9 (Larsen), Parts B and C · the user's write-up of PHY 513, Problem Set 5, Problem 6 (submitted) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.3, eqs. (3.52)–(3.67) · Yu Zhao-Huan, 量子场论讲义, §5.4.2, eqs. (5.158)–(5.214) · the user's pre-course notes, §5.4 ("Helicity spinors in the Weyl representation", notes "Fixing the normalization constants", "Rest frame, and what ω_λω_{−λ} = m means", "Checking the spin sums").*

How are the spinors $u^s(p)$, $v^s(p)$ of [[§C5a.9 Plane-Wave Solutions|§C5a.9]] ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]]) normalized, how do they sit relative to each other, and what survives of them in a computation? Every answer here is a short calculation with the square-root identities ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]]) and the Dirac conjugate $\bar u = u^\dagger\gamma^0$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]), whose rows $\bar u^s(p)$, $\bar v^s(p)$ are [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]. The results — $\bar uu = 2m$, $u^\dagger u = 2E_{\mathbf p}$, $\bar vv = -2m$, the orthogonality relations and the spin sums $\sum u\bar u = \slashed{p} + m$, $\sum v\bar v = \slashed{p} - m$ — are what later amplitudes and the quantized field use. The section ends with the helicity basis, in which no matrix square root is needed, and the massless limit, where helicity becomes chirality ([[§C3.7★ Massless Particles and Helicity|§C3.7★]]). The covariance of $\gamma^\mu$, the invariance of the Dirac form and $\gamma^5$ are mathematics ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element|§CB.11]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]), shown in the blocks below.

*Conventions* as in [[§C5a.9 Plane-Wave Solutions|§C5a.9]]: chiral basis, $p^0 = E_{\mathbf p} > 0$, $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, so for a row $(a^\dagger, b^\dagger)$ the product $(a^\dagger, b^\dagger)\gamma^0 = (b^\dagger, a^\dagger)$ exchanges the halves. $\sqrt{p\cdot\sigma}$, $\sqrt{p\cdot\bar\sigma}$ are Hermitian ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|Def. §C5a.9.5]]), so $(\sqrt{p\cdot\sigma}\,\xi)^\dagger = \xi^\dagger\sqrt{p\cdot\sigma}$; the conjugate rows, derived once, are $\bar u^s(p) = (\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma})$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]]) and $\bar v^s(p) = (-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma})$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]). $\tilde p \equiv (E_{\mathbf p}, -\mathbf p)$ is $p$ with the three-momentum reversed.

## The mathematics used here

The spin sums are covariant (Theorem §C5a.10.9) because the Dirac matrices rotate as a vector and $\Lambda_{1/2}$ preserves the Dirac form:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-17]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7b]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13b]]

## Normalization

> [!theorem] Theorem §C5a.10.1: u†u = 2E
> For the spinors $u^s(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] with an orthonormal spin basis ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]), $u^{r\dagger}(p)\,u^s(p) = 2E_{\mathbf p}\,\delta^{rs}$. Different spin labels are orthogonal; the value depends on the frame.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Derivation "Normalization I: u†u") · PHY 513 Lecture 9, Part B ("Normalization I") · PS §3.3, eq. (3.55) · Yu §5.4.2, eq. (5.198)*

^thm-c5a-10-1

> [!derivation]- Derivation
> **Step 1** (the row). $u^s = (\sqrt{p\cdot\sigma}\,\xi^s, \sqrt{p\cdot\bar\sigma}\,\xi^s)$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]]); its Hermitian conjugate is the row $u^{r\dagger} = (\xi^{r\dagger}\sqrt{p\cdot\sigma},\ \xi^{r\dagger}\sqrt{p\cdot\bar\sigma})$, the roots being Hermitian ([[§C5a.9 Plane-Wave Solutions#^der-c5a-9-10|Derivation §C5a.9.10]], Steps 1–2).
>
> **Step 2** (row times column, upper with upper, lower with lower).
>
> $$
> u^{r\dagger}u^s = \xi^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}\,\xi^s + \xi^{r\dagger}\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma}\,\xi^s = \xi^{r\dagger}\bigl(p\cdot\sigma + p\cdot\bar\sigma\bigr)\xi^s ,
> $$
>
> by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], 1.
>
> **Step 3** (the spatial parts cancel). $p\cdot\sigma + p\cdot\bar\sigma = (E - \mathbf p\cdot\boldsymbol\sigma) + (E + \mathbf p\cdot\boldsymbol\sigma) = 2E_{\mathbf p}\mathbb 1$ ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]]), so $u^{r\dagger}u^s = 2E_{\mathbf p}\,\xi^{r\dagger}\xi^s = 2E_{\mathbf p}\,\delta^{rs}$ by orthonormality.
>
> **What the derivation shows**
> - No step divides by $m$: valid for $m = 0$.
> - $2E_{\mathbf p}$ is the time component of a four-vector, so it changes with the frame → [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-1|Remark: Why u†u depends on the frame and ūu does not]].
> - Used in: the Hamiltonian of the quantized field ([[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]]).

^der-c5a-10-1

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]

> [!theorem] Theorem §C5a.10.2: ūu = 2m
> $\bar u^r(p)\,u^s(p) = 2m\,\delta^{rs}$, with $u^s$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and its Dirac conjugate $\bar u^r = u^{r\dagger}\gamma^0$ ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]; the row: [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]]); the value is the same in every frame.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Derivation "Normalization II: ūu") · PHY 513 Lecture 9, Part B ("Normalization II") · PS §3.3, eqs. (3.56)–(3.57), (3.60) · Yu §5.4.2, eqs. (5.205), (5.207)*

^thm-c5a-10-2

> [!derivation]- Derivation
> **Step 1** (the conjugate row). By [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], $\bar u^r = u^{r\dagger}\gamma^0 = (\xi^{r\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{r\dagger}\sqrt{p\cdot\sigma})$: the dagger puts each root to the right of $\xi^{r\dagger}$, and $\gamma^0$ exchanges the halves.
>
> **Step 2** (row times column). Now each term pairs a $\sqrt{p\cdot\bar\sigma}$ with a $\sqrt{p\cdot\sigma}$:
>
> $$
> \bar u^ru^s = \xi^{r\dagger}\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\,\xi^s + \xi^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\,\xi^s = m\,\xi^{r\dagger}\xi^s + m\,\xi^{r\dagger}\xi^s = 2m\,\delta^{rs} ,
> $$
>
> by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], 3, and orthonormality.
>
> **What the derivation shows**
> - $\bar uu$ is the value of the scalar $\bar\psi\psi$ on a plane wave ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]), so it cannot depend on the frame; the computation confirms it.
> - ⚑ By-product: at $m = 0$, $\bar uu = 0$: the invariant form cannot normalize massless spinors, and $u^\dagger u = 2E_{\mathbf p}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]]) is used instead → [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-4|Def. §C5a.9.4]].
> - At rest, $\bar u_0 = u_0^\dagger$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], 3) and $\bar u_0u_0 = \sqrt m\sqrt m(\xi^\dagger\xi + \xi^\dagger\xi) = 2m$ directly: this is what the $\sqrt m$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]] was chosen for.

^der-c5a-10-2

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]

> [!remark] Remark: Why u†u depends on the frame and ūu does not
> $\psi^\dagger\psi$ is not a Lorentz scalar ([[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]): it is the time component of the current $\bar\psi\gamma^\mu\psi$ ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]]). On a plane wave the whole current is $\bar u^r\gamma^\mu u^s = 2p^\mu\delta^{rs}$ (the Gordon identity at $p' = p$, [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]], with Theorem §C5a.10.2), whose time component is $2E_{\mathbf p}\delta^{rs}$: the frame dependence of $u^\dagger u$ is that of $p^0$. $\bar\psi\psi$ is a scalar, and $\bar uu = 2m$ is the same number in every frame. The $2E_{\mathbf p}$ is the same weight as in the relativistic normalization of states, $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), which is why the Dirac mode expansion carries the same $1/\sqrt{2E_{\mathbf p}}$ as the scalar one.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 ("it is the time component of the current") · PHY 513 Lecture 9, Part B ("Not surprising: ψ†ψ is not Lorentz invariant") · PS §3.3, p. 47*

^rem-c5a-10-1

> [!theorem] Theorem §C5a.10.3: v†v = 2E
> For the spinors $v^s(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], $v^{r\dagger}(p)\,v^s(p) = 2E_{\mathbf p}\,\delta^{rs}$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Normalizations of the v's") · PHY 513 Lecture 9, Part C ("Normalization of v's") · PS §3.3, eq. (3.63) · Yu §5.4.2, eq. (5.199)*

^thm-c5a-10-3

> [!derivation]- Derivation
> As [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-1|Derivation §C5a.10.1]], with the sign of the lower half carried. $v^s = (\sqrt{p\cdot\sigma}\,\eta^s, -\sqrt{p\cdot\bar\sigma}\,\eta^s)$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]]), $v^{r\dagger} = (\eta^{r\dagger}\sqrt{p\cdot\sigma},\ -\eta^{r\dagger}\sqrt{p\cdot\bar\sigma})$ ([[§C5a.9 Plane-Wave Solutions#^der-c5a-9-12|Derivation §C5a.9.12]], Step 2). Upper with upper, lower with lower:
>
> $$
> v^{r\dagger}v^s = \eta^{r\dagger}(p\cdot\sigma)\eta^s + (-1)(-1)\,\eta^{r\dagger}(p\cdot\bar\sigma)\eta^s = \eta^{r\dagger}\,2E_{\mathbf p}\,\eta^s = 2E_{\mathbf p}\,\delta^{rs} .
> $$
>
> The extra sign appears twice in the lower-lower term and cancels.
>
> **What the derivation shows**
> - $v^\dagger v$ is positive, like $u^\dagger u$: $\psi^\dagger\psi \ge 0$ for every solution, the reason why the Dirac charge density is positive before quantization ([[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]], draft).
> - Valid for $m \ge 0$.

^der-c5a-10-3

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]

> [!theorem] Theorem §C5a.10.4: v̄v = −2m
> $\bar v^r(p)\,v^s(p) = -2m\,\delta^{rs}$ ($v^s$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], $\bar v^r = v^{r\dagger}\gamma^0$ as in [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], the row of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]): Lorentz invariant, and negative.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Normalizations of the v's") · PHY 513 Lecture 9, Part C ("Normalization of v's") · PS §3.3, eq. (3.63) · Yu §5.4.2, eqs. (5.206), (5.208)*

^thm-c5a-10-4

> [!derivation]- Derivation
> **Step 1** (the conjugate row). By [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], $\bar v^r = (-\eta^{r\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{r\dagger}\sqrt{p\cdot\sigma})$: $\gamma^0$ has moved the minus sign to the *upper* half of the row.
>
> **Step 2** (row times column). Each term pairs an upper half with a lower half, and each carries the sign exactly once:
>
> $$
> \bar v^rv^s = \bigl(-\eta^{r\dagger}\sqrt{p\cdot\bar\sigma}\bigr)\sqrt{p\cdot\sigma}\,\eta^s + \eta^{r\dagger}\sqrt{p\cdot\sigma}\bigl(-\sqrt{p\cdot\bar\sigma}\,\eta^s\bigr) = -m\,\delta^{rs} - m\,\delta^{rs} = -2m\,\delta^{rs} ,
> $$
>
> by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], 3.
>
> **What the derivation shows**
> - ⚑ By-product: the bilinear form $\bar ab = a^\dagger\gamma^0b$ on $\mathbb C^4$ is indefinite ($\gamma^0$ has eigenvalues $+1, +1, -1, -1$): positive on the $u$'s, negative on the $v$'s → [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-1|Caution: The sign of v̄v]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-10|Theorem §C5a.10.10]].

^der-c5a-10-4

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]]

> [!caution] Caution: The sign of v̄v
> $\bar vv = -2m$, and correspondingly $-m$ in the $v$ spin sum ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]]), are where sign errors happen. The lecture's advice: rederive them from $u^s$, $v^s$ and the square-root identities whenever in doubt, remembering that $\gamma^0$ moves the minus sign of $v$ from the lower half of the column to the upper half of the row ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], 1). The negative value is not a defect: the same indefiniteness is that of the Klein–Gordon inner product on negative-frequency modes ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|§C2a.2, Remark: Why this inner product, and why it is indefinite]]).
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 ("this is a sign error waiting to happen"), §9.7 · PHY 513 Lecture 9, Part C*

^cau-c5a-10-1

> [!theorem] Theorem §C5a.10.5: u and v Are Orthogonal under the Dirac Conjugate
> For all $r, s$ (equal or not) and all choices of the bases $\xi^s$, $\eta^s$ ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]), with $u^s$, $v^s$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]] and their Dirac conjugates ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]; rows [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]),
>
> $$
> \bar v^r(p)\,u^s(p) = 0, \qquad \bar u^r(p)\,v^s(p) = 0 .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Orthogonality of u and v") · PHY 513 Lecture 9, Part C ("Bonus Material: Orthogonality of u and v") · PS §3.3, eq. (3.64) · Yu §5.4.2, eqs. (5.209)–(5.210)*

^thm-c5a-10-5

> [!derivation]- Derivation
> **Step 1** ($\bar vu$). With the row $\bar v^r = (-\eta^{r\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{r\dagger}\sqrt{p\cdot\sigma})$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]],
>
> $$
> \bar v^ru^s = \bigl(-\eta^{r\dagger}\sqrt{p\cdot\bar\sigma}\bigr)\sqrt{p\cdot\sigma}\,\xi^s + \eta^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\,\xi^s = -m\,\eta^{r\dagger}\xi^s + m\,\eta^{r\dagger}\xi^s = 0 .
> $$
>
> **Step 2** ($\bar uv$). With the row $\bar u^r = (\xi^{r\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{r\dagger}\sqrt{p\cdot\sigma})$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]],
>
> $$
> \bar u^rv^s = \xi^{r\dagger}\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\,\eta^s + \xi^{r\dagger}\sqrt{p\cdot\sigma}\bigl(-\sqrt{p\cdot\bar\sigma}\,\eta^s\bigr) = m\,\xi^{r\dagger}\eta^s - m\,\xi^{r\dagger}\eta^s = 0 .
> $$
>
> The two-spinor products $\eta^{r\dagger}\xi^s$ need not vanish; the two terms cancel for any of them.
>
> **What the derivation shows**
> - With Theorems §C5a.10.2 and §C5a.10.4, $\{u^1, u^2, v^1, v^2\}$ is an orthogonal basis for the indefinite form $\bar ab$, with "norms" $+2m, +2m, -2m, -2m$; used in [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-10|Theorem §C5a.10.10]].
> - A second reason: $\bar v^r(\slashed{p} - m)u^s = 0$, and $\bar v^r\slashed{p} = -m\bar v^r$ (the conjugate of $\slashed{p}\,v = -mv$: [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], 2), so $-2m\,\bar v^ru^s = 0$; for $m > 0$ this gives the result without components.

^der-c5a-10-5

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]]

> [!theorem] Theorem §C5a.10.6: u and v Are Orthogonal at Opposite Three-Momenta
> With $\tilde p = (E_{\mathbf p}, -\mathbf p)$ and $u^s$, $v^s$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], for all $r, s$,
>
> $$
> u^{r\dagger}(p)\,v^s(\tilde p) = 0, \qquad v^{r\dagger}(p)\,u^s(\tilde p) = 0 ,
> $$
>
> while at equal momenta $u^{r\dagger}(p)\,v^s(p) = -2\,\xi^{r\dagger}(\mathbf p\cdot\boldsymbol\sigma)\,\eta^s$, which is neither zero nor Lorentz invariant in general.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Orthogonality of u and v", "With Hermitian conjugates") · PHY 513 Lecture 9, Part C ("Warning") · PS §3.3, eq. (3.65) · Yu §5.4.1, eq. (5.142); §5.4.2, eq. (5.203)*

^thm-c5a-10-6

> [!derivation]- Derivation
> **Step 1** (reversing the three-momentum exchanges the matrices). By [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]], $\tilde p\cdot\sigma = E_{\mathbf p} - (-\mathbf p)\cdot\boldsymbol\sigma = E_{\mathbf p} + \mathbf p\cdot\boldsymbol\sigma = p\cdot\bar\sigma$ and likewise $\tilde p\cdot\bar\sigma = p\cdot\sigma$ ($E_{-\mathbf p} = E_{\mathbf p}$). The positive roots are exchanged too (the root of a matrix depends only on the matrix). So
>
> $$
> v^s(\tilde p) = \begin{pmatrix}\sqrt{p\cdot\bar\sigma}\,\eta^s\\ -\sqrt{p\cdot\sigma}\,\eta^s\end{pmatrix}, \qquad u^s(\tilde p) = \begin{pmatrix}\sqrt{p\cdot\bar\sigma}\,\xi^s\\ \sqrt{p\cdot\sigma}\,\xi^s\end{pmatrix} .
> $$
>
> **Step 2** ($u^\dagger(p)v(\tilde p)$). Upper with upper, lower with lower:
>
> $$
> u^{r\dagger}(p)v^s(\tilde p) = \xi^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\,\eta^s + \xi^{r\dagger}\sqrt{p\cdot\bar\sigma}\bigl(-\sqrt{p\cdot\sigma}\bigr)\eta^s = m\,\xi^{r\dagger}\eta^s - m\,\xi^{r\dagger}\eta^s = 0 ,
> $$
>
> by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], 3 (both orders give $m$).
>
> **Step 3** ($v^\dagger(p)u(\tilde p)$). $v^{r\dagger}(p) = (\eta^{r\dagger}\sqrt{p\cdot\sigma}, -\eta^{r\dagger}\sqrt{p\cdot\bar\sigma})$, so
>
> $$
> v^{r\dagger}(p)u^s(\tilde p) = \eta^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma}\,\xi^s - \eta^{r\dagger}\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\,\xi^s = m\,\eta^{r\dagger}\xi^s - m\,\eta^{r\dagger}\xi^s = 0 .
> $$
>
> **Step 4** (equal momenta). Without reversing: $u^{r\dagger}(p)v^s(p) = \xi^{r\dagger}\sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}\,\eta^s - \xi^{r\dagger}\sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma}\,\eta^s = \xi^{r\dagger}(p\cdot\sigma - p\cdot\bar\sigma)\eta^s = -2\,\xi^{r\dagger}(\mathbf p\cdot\boldsymbol\sigma)\eta^s$, which vanishes at $\mathbf p = 0$ but not in general (e.g. $\mathbf p = p\hat{\mathbf z}$, $\xi = \eta = (1, 0)$ gives $-2p$).
>
> **What the derivation shows**
> - The relation pairs $\mathbf p$ with $-\mathbf p$ because the $\mathbf x$-integral of $\psi^\dagger\psi$-type quantities produces $\delta^3(\mathbf p + \mathbf q)$ for the cross terms between $e^{-ip\cdot x}$ and $e^{+iq\cdot x}$, exactly as for the scalar field ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|§C2a.2, Remark: Why the modes decouple]]).
> - Used in: the cross terms of $\hat H$, $\hat{\mathbf P}$ and $\hat Q$ of the quantized Dirac field, where they vanish by this theorem: this flipped-momentum version is the one needed when the Dirac field is quantized, because the $\mathbf x$ integral in the Hamiltonian pairs $\mathbf p$ with $-\mathbf p$ (the user's PHY 513 notes, Ch. 9, Derivation "Orthogonality of u and v", as updated for Lecture 10; Lecture 10, slide 19) — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2b|Derivation §C5b.3.2, second route]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]].
> - Valid for $m \ge 0$.

^der-c5a-10-6

*Uses:* [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|Def. §C5a.9.5]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]]

> [!derivation]- Derivation (second route: eigenvectors of the Hermitian Dirac Hamiltonian, the pre-course notes)
> **Step 1** (the Hamiltonian form). Multiply the Dirac equation $(i\gamma^0\partial_0 + i\gamma^i\partial_i - m)\psi = 0$ by $\gamma^0$ from the left, $(\gamma^0)^2 = \mathbb 1$: $i\partial_0\psi = \gamma^0(-i\gamma^i\partial_i + m)\psi$. On $\psi = w\,e^{i\mathbf k\cdot\mathbf x}e^{-i\omega t}$, $-i\gamma^i\partial_i \to -i\gamma^i(ik^i) = \gamma^ik^i$ and $i\partial_0 \to \omega$: $\omega\,w = H_{\text{s.p.}}(\mathbf k)\,w$ with $H_{\text{s.p.}}(\mathbf k) = \gamma^0\gamma^ik^i + m\gamma^0$, Hermitian ([[§C5a.9 Plane-Wave Solutions#^der-c5a-9-2b|Derivation §C5a.9.2, second route]], Step 1).
>
> **Step 2** (identify the eigenvectors). $u(p)e^{-ip\cdot x} = u(p)e^{i\mathbf p\cdot\mathbf x}e^{-iE_{\mathbf p}t}$: $\mathbf k = \mathbf p$, $\omega = +E_{\mathbf p}$. $v(\tilde p)e^{+i\tilde p\cdot x} = v(\tilde p)e^{iE_{\mathbf p}t - i(-\mathbf p)\cdot\mathbf x} = v(\tilde p)e^{i\mathbf p\cdot\mathbf x}e^{+iE_{\mathbf p}t}$: $\mathbf k = \mathbf p$, $\omega = -E_{\mathbf p}$. So $u(p)$ and $v(\tilde p)$ are eigenvectors of the same Hermitian $H_{\text{s.p.}}(\mathbf p)$ with eigenvalues $+E_{\mathbf p} \neq -E_{\mathbf p}$ (for $E_{\mathbf p} > 0$).
>
> **Step 3** (orthogonality). Eigenvectors of a Hermitian matrix with distinct eigenvalues are orthogonal: $E\,u^\dagger v = (hu)^\dagger v = u^\dagger hv = -E\,u^\dagger v$, so $2E\,u^\dagger v = 0$. The same with $\mathbf p \to -\mathbf p$ gives $v^\dagger(p)u(\tilde p) = 0$.
>
> *Source: the user's pre-course notes, §5.4 ("eigenvectors of the same Hermitian matrix … with distinct eigenvalues ±E_p") · Yu §5.4.1, eqs. (5.133)–(5.142)*

^der-c5a-10-6b

*Uses:* [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-2b|Derivation §C5a.9.2 (second route)]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]

## Spin sums

> [!theorem] Theorem §C5a.10.7: The Spin Sum over u
> For any spin basis $\xi^s$ ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]) in $u^s(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], with $\bar u^s$ of [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]] ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]]) and $\slashed{p}$ of [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]],
>
> $$
> \sum_{s=1,2}u^s(p)\,\bar u^s(p) = \slashed{p} + m ,
> $$
>
> a $4\times4$ matrix (column times row), independent of the choice of basis.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Derivation "Completeness: the spin sum over u") · PHY 513 Lecture 9, Part B ("Completeness for Dirac Spinors") · PS §3.3, eq. (3.66) · Yu §5.4.2, eq. (5.212)*

^thm-c5a-10-7

> [!derivation]- Derivation
> **Step 1** (column times row, block by block). With $u^s = (\sqrt{p\cdot\sigma}\,\xi^s, \sqrt{p\cdot\bar\sigma}\,\xi^s)$ and $\bar u^s = (\xi^{s\dagger}\sqrt{p\cdot\bar\sigma}, \xi^{s\dagger}\sqrt{p\cdot\sigma})$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]]), the four $2\times2$ blocks of $u^s\bar u^s$ are
>
> $$
> u^s\bar u^s = \begin{pmatrix}\sqrt{p\cdot\sigma}\,\xi^s\xi^{s\dagger}\sqrt{p\cdot\bar\sigma} & \sqrt{p\cdot\sigma}\,\xi^s\xi^{s\dagger}\sqrt{p\cdot\sigma}\\ \sqrt{p\cdot\bar\sigma}\,\xi^s\xi^{s\dagger}\sqrt{p\cdot\bar\sigma} & \sqrt{p\cdot\bar\sigma}\,\xi^s\xi^{s\dagger}\sqrt{p\cdot\sigma}\end{pmatrix} .
> $$
>
> **Step 2** (sum over $s$). The sum acts only on the middle factor, and $\sum_s\xi^s\xi^{s\dagger} = \mathbb 1_2$ for any orthonormal basis ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]):
>
> $$
> \sum_su^s\bar u^s = \begin{pmatrix}\sqrt{p\cdot\sigma}\sqrt{p\cdot\bar\sigma} & \sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}\\ \sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\bar\sigma} & \sqrt{p\cdot\bar\sigma}\sqrt{p\cdot\sigma}\end{pmatrix} = \begin{pmatrix}m & p\cdot\sigma\\ p\cdot\bar\sigma & m\end{pmatrix} ,
> $$
>
> by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], 1 and 3.
>
> **Step 3** (recognize). The off-diagonal blocks are $\slashed{p}$ in the chiral basis ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]]) and the diagonal ones $m\,\mathbb 1_2$, i.e. $m\,\mathbb 1_4$: the sum is $\slashed{p} + m$. ⚑ By-product: basis independence came from completeness of the $\xi^s$ alone; the spin sum is a property of the solution space, not of the labels → [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|Theorem §C5a.10.9]].
>
> **What the derivation shows**
> - Completeness in the "wrong" order (column times row) gives a matrix, as $\sum_n|n\rangle\langle n|$ does ([[§38 The Completeness Relation#^prop-38-1|556 Prop. §38.1]]); here with $\bar u$ instead of $u^\dagger$.
> - It is not the identity: the $u$'s span only half of $\mathbb C^4$ → [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-10|Theorem §C5a.10.10]].
> - Valid for $m \ge 0$; used in every spin-summed amplitude and in the numerator of the Dirac propagator ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], draft).

^der-c5a-10-7

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]]

> [!theorem] Theorem §C5a.10.8: The Spin Sum over v
> For any spin basis $\eta^s$ ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]) in $v^s(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], with $\bar v^s$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]],
>
> $$
> \sum_{s=1,2}v^s(p)\,\bar v^s(p) = \slashed{p} - m .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Completeness: the spin sum over v") · PHY 513 Lecture 9, Part C ("Completeness of v's") · PS §3.3, eq. (3.67) · Yu §5.4.2, eq. (5.213)*

^thm-c5a-10-8

> [!derivation]- Derivation
> As [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-7|Derivation §C5a.10.7]], with the signs carried. The column $v^s = (\sqrt{p\cdot\sigma}\,\eta^s, -\sqrt{p\cdot\bar\sigma}\,\eta^s)$ has its sign in the lower half; the row $\bar v^s = (-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma}, \eta^{s\dagger}\sqrt{p\cdot\sigma})$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]) in the upper half. Block by block, after $\sum_s\eta^s\eta^{s\dagger} = \mathbb 1_2$:
>
> $$
> \sum_sv^s\bar v^s = \begin{pmatrix}\sqrt{p\cdot\sigma}\,\bigl(-\sqrt{p\cdot\bar\sigma}\bigr) & \sqrt{p\cdot\sigma}\sqrt{p\cdot\sigma}\\ \bigl(-\sqrt{p\cdot\bar\sigma}\bigr)\bigl(-\sqrt{p\cdot\bar\sigma}\bigr) & \bigl(-\sqrt{p\cdot\bar\sigma}\bigr)\sqrt{p\cdot\sigma}\end{pmatrix} = \begin{pmatrix}-m & p\cdot\sigma\\ p\cdot\bar\sigma & -m\end{pmatrix} = \slashed{p} - m .
> $$
>
> The off-diagonal blocks pick up both signs (lower left) or neither (upper right) and are unchanged; each diagonal block picks up one sign.
>
> **What the derivation shows**
> - Relative to the $u$ sum only $m \to -m$; the sign is the one of $\bar vv = -2m$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-1|Caution: The sign of v̄v]]).
> - Valid for $m \ge 0$.

^der-c5a-10-8

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-7|Theorem §C5a.9.7]]

> [!theorem] Theorem §C5a.10.9: The Spin Sums Are Covariant
> For every Lorentz transformation $\Lambda$ with spinor matrix $\Lambda_{1/2}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]),
> 1. $\Lambda_{1/2}\,\slashed{p}\,\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)}$, hence $\Lambda_{1/2}(\slashed{p} \pm m)\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)} \pm m$;
> 2. the transformed spinors $\Lambda_{1/2}u^s(p)$ solve $(\slashed{(\Lambda p)} - m)\,w = 0$, and $\sum_s(\Lambda_{1/2}u^s)\overline{(\Lambda_{1/2}u^s)} = \slashed{(\Lambda p)} + m$; likewise for $v$ with $-m$.
>
> $\slashed{p}$ is a matrix with two spinor slots, not a number: it is "Lorentz invariant" only in the sense that relations such as $\sum u\bar u = \slashed{p} + m$ keep their form in every frame.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 (Caution "In what sense p̸ is 'Lorentz invariant'") · PHY 513 Lecture 9, Part B*

^thm-c5a-10-9

> [!derivation]- Derivation
> **Step 1** (the $\gamma$'s as an invariant vector). $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]). Multiply from the left by $\Lambda_{1/2}$ and from the right by $\Lambda_{1/2}^{-1}$: $\gamma^\mu = \Lambda^\mu{}_\nu\,\Lambda_{1/2}\gamma^\nu\Lambda_{1/2}^{-1}$.
>
> **Step 2** (contract with $(\Lambda p)_\mu$). $(\Lambda p)_\mu\Lambda^\mu{}_\nu = p_\nu$, because $(\Lambda p)\cdot(\Lambda a) = p\cdot a$ for every $a$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]), i.e. $(\Lambda p)_\mu\Lambda^\mu{}_\nu a^\nu = p_\nu a^\nu$ for all $a^\nu$. So $\slashed{(\Lambda p)} = (\Lambda p)_\mu\gamma^\mu = p_\nu\Lambda_{1/2}\gamma^\nu\Lambda_{1/2}^{-1} = \Lambda_{1/2}\slashed{p}\,\Lambda_{1/2}^{-1}$. The number $m$ commutes with $\Lambda_{1/2}$: part 1. (The sign ambiguity of $\Lambda_{1/2}$ cancels between $\Lambda_{1/2}$ and $\Lambda_{1/2}^{-1}$.)
>
> **Step 3** (transformed solutions). $(\slashed{(\Lambda p)} - m)\Lambda_{1/2}u^s = \Lambda_{1/2}(\slashed{p} - m)\Lambda_{1/2}^{-1}\Lambda_{1/2}u^s = \Lambda_{1/2}(\slashed{p} - m)u^s = 0$.
>
> **Step 4** (the conjugate). $\Lambda_{1/2}^\dagger\gamma^0 = \gamma^0\Lambda_{1/2}^{-1}$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]]), so $\overline{\Lambda_{1/2}w} = w^\dagger\Lambda_{1/2}^\dagger\gamma^0 = w^\dagger\gamma^0\Lambda_{1/2}^{-1} = \bar w\,\Lambda_{1/2}^{-1}$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]). Then $\sum_s(\Lambda_{1/2}u^s)\overline{(\Lambda_{1/2}u^s)} = \Lambda_{1/2}\bigl(\sum_su^s\bar u^s\bigr)\Lambda_{1/2}^{-1} = \Lambda_{1/2}(\slashed{p} + m)\Lambda_{1/2}^{-1} = \slashed{(\Lambda p)} + m$ by [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]] and part 1. Same for $v$ with [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]]. Part 2.
>
> **What the derivation shows**
> - $\Lambda_{1/2}u^s(p)$ need not equal $u^s(\Lambda p)$ (for a boost not along $\mathbf p$ the spin labels are rotated by a Wigner rotation, [[§C3.6★ Particle States and the Little Group#^thm-c3-6-3|Theorem §C3.6.3]]), but the spin sum does not care: it depends only on the solution space.
> - The invariance of $\bar ab$ under $a, b \to \Lambda_{1/2}a, \Lambda_{1/2}b$ (Step 4) also makes $\bar uu$ and $\bar vv$ frame independent, as computed in Theorems §C5a.10.2 and §C5a.10.4.

^der-c5a-10-9

*Uses:* [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]]

> [!theorem] Theorem §C5a.10.10: Completeness and the Energy Projectors
> Let $m > 0$, $u^s$, $v^s$ as in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], and $\Lambda_\pm(p) \equiv \dfrac{\pm\slashed{p} + m}{2m}$. Then
> 1. $\dfrac1{2m}\sum_{s=1,2}\bigl[u^s(p)\bar u^s(p) - v^s(p)\bar v^s(p)\bigr] = \mathbb 1_4$;
> 2. $\Lambda_+ = \frac1{2m}\sum_su^s\bar u^s$ and $\Lambda_- = -\frac1{2m}\sum_sv^s\bar v^s$ are complementary projectors: $\Lambda_\pm^2 = \Lambda_\pm$, $\Lambda_+\Lambda_- = \Lambda_-\Lambda_+ = 0$, $\Lambda_+ + \Lambda_- = \mathbb 1$;
> 3. $\Lambda_+u^s = u^s$, $\Lambda_+v^s = 0$, $\Lambda_-v^s = v^s$, $\Lambda_-u^s = 0$: $\Lambda_+$ projects onto the $u$'s (eigenvalue $+m$ of $\slashed{p}$), $\Lambda_-$ onto the $v$'s; $\operatorname{tr}\Lambda_\pm = 2$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.5 (Derivation "Why neither spin sum is the identity, and what is") · Lecture 9 ended on this point*

^thm-c5a-10-10

> [!derivation]- Derivation
> **Step 1** (part 1 from the spin sums). By [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]] and [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]], $\frac1{2m}[(\slashed{p} + m) - (\slashed{p} - m)] = \frac{2m}{2m}\mathbb 1 = \mathbb 1$.
>
> **Step 2** (part 1 checked on a basis). On $u^r$: $\sum_su^s(\bar u^su^r) = \sum_su^s\,2m\delta^{sr} = 2m\,u^r$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]]) and $\sum_sv^s(\bar v^su^r) = 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-5|Theorem §C5a.10.5]]), so the bracket gives $2m\,u^r$. On $v^r$: the first sum gives $0$, the second $-\sum_sv^s(\bar v^sv^r) = -(-2m)v^r = 2m\,v^r$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|Theorem §C5a.10.4]]). Since $\{u^s, v^s\}$ is a basis of $\mathbb C^4$ for $m > 0$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]]), the operator is $\mathbb 1$. ⚑ By-product: in a completeness relation for an indefinite form each basis vector enters divided by its "norm"; the $v$'s have norm $-2m$, hence the minus sign.
>
> **Step 3** (projector algebra). With $\slashed{p}^{\,2} = m^2$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]], 1), expanding all terms: $\Lambda_+^2 = \frac{\slashed{p}^{\,2} + 2m\slashed{p} + m^2}{4m^2} = \frac{2m^2 + 2m\slashed{p}}{4m^2} = \Lambda_+$; $\Lambda_-^2 = \frac{\slashed{p}^{\,2} - 2m\slashed{p} + m^2}{4m^2} = \Lambda_-$; $\Lambda_+\Lambda_- = \frac{(m + \slashed{p})(m - \slashed{p})}{4m^2} = \frac{m^2 - m\slashed{p} + m\slashed{p} - \slashed{p}^{\,2}}{4m^2} = 0$, and $\Lambda_-\Lambda_+$ is the same product in the other order (the factors commute); $\Lambda_+ + \Lambda_- = \frac{2m}{2m} = \mathbb 1$. Part 2.
>
> **Step 4** (action and trace). $\Lambda_+u^s = \frac{(\slashed{p} + m)u^s}{2m} = \frac{2m\,u^s}{2m} = u^s$ and $\Lambda_+v^s = \frac{(-m + m)v^s}{2m} = 0$, using $\slashed{p}\,u = mu$, $\slashed{p}\,v = -mv$; likewise for $\Lambda_-$. $\operatorname{tr}\Lambda_\pm = \frac{\pm\operatorname{tr}\slashed{p} + 4m}{2m} = 2$ ($\operatorname{tr}\slashed{p} = 0$, [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]): rank two each. Part 3.
>
> **What the derivation shows**
> - These are the projectors of Step 3 of [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-2|Derivation §C5a.9.2]], now written through the spinors.
> - At rest $\Lambda_\pm = \frac12(\mathbb 1 \pm \gamma^0)$; in the Dirac basis $\gamma^0 = \beta$, so they are the projectors onto upper and lower components of Quantum Mechanics' Dirac spinors at rest ([[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]).
> - Assumption $m > 0$: at $m = 0$ the $u$'s and $v$'s span the same space ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]], 3) and $\Lambda_\pm$ do not exist.

^der-c5a-10-10

*Uses:* [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|Theorem §C5a.10.4]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-5|Theorem §C5a.10.5]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]

> [!remark] Remark: Why neither spin sum is the identity
> A spin sum over all states of a particle is the identity in nonrelativistic quantum mechanics ($\sum_s\xi^s\xi^{s\dagger} = \mathbb 1_2$). Here the sum over the two $u$'s is $\slashed{p} + m$, not $2m\,\mathbb 1$, because the $u$'s span only the eigenvalue-$(+m)$ half of $\mathbb C^4$; the other half belongs to the $v$'s. Both halves are needed for completeness, and with the Dirac conjugate the $v$'s enter with a minus sign. In amplitudes, sums over a fermion's spins produce $\slashed{p} \pm m$ between $\gamma$ matrices, and traces turn these into dot products ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]). The same $\slashed{p} + m$ appears as the numerator of the Dirac propagator ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], draft); what later computations use of the spinors is mostly these sums and the normalizations, not the explicit $u$ and $v$.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.4 ("It is not the identity"), §9.5, §9.7 ("what later computations use is the last three rows")*

^rem-c5a-10-2

## Helicity spinors

> [!definition] Definition §C5a.10.1: Helicity of a Dirac Spinor
> For $\mathbf p \neq 0$ the **helicity** operator on Dirac spinors is the spin along the direction of motion,
>
> $$
> h \equiv \hat{\mathbf p}\cdot\mathbf S = \frac12\begin{pmatrix}\hat{\mathbf p}\cdot\boldsymbol\sigma & 0\\ 0 & \hat{\mathbf p}\cdot\boldsymbol\sigma\end{pmatrix},
> $$
>
> with $\mathbf S = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$ the spin matrices ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-4|Theorem §C5a.9.4]]. A spinor with $h = +\frac12$ ($-\frac12$) is called right-handed (left-handed). This is the spinor counterpart of the helicity of states, [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
>
> *Source: PS §3.3, eq. (3.54) · the user's write-up of PHY 513, Problem Set 5, Problem 6 (statement) · the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis") · Yu §5.4.2, eqs. (5.158)–(5.161)*

^def-c5a-10-1

> [!definition] Definition §C5a.10.2: Helicity Two-Spinors
> For $\mathbf p \neq 0$ the **helicity two-spinors** $\xi_\pm(\hat{\mathbf p}) \in \mathbb C^2$ are normalized eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$, the two-component block of the helicity operator of [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|Def. §C5a.10.1]]:
>
> $$
> (\hat{\mathbf p}\cdot\boldsymbol\sigma)\,\xi_\pm = \pm\xi_\pm, \qquad \xi_\pm^\dagger\xi_\pm = 1 ,
> $$
>
> each fixed up to a phase.
>
> *Source: PS §3.3, eq. (3.54) · the user's write-up of PHY 513, Problem Set 5, Problem 6 (statement) · Yu §5.4.2, eqs. (5.158)–(5.161)*

^def-c5a-10-2

> [!theorem] Theorem §C5a.10.11: The Helicity Two-Spinors
> For $\hat{\mathbf p} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, $0 \le \theta \le \pi$, the helicity two-spinors ([[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|Def. §C5a.10.2]]) with phases chosen to reduce to $(1, 0)^{\mathsf T}$ and $(0, 1)^{\mathsf T}$ for $\hat{\mathbf p} = +\hat{\mathbf z}$ are
>
> $$
> \xi_+(\hat{\mathbf p}) = \begin{pmatrix}\cos\frac\theta2\\ e^{i\varphi}\sin\frac\theta2\end{pmatrix}, \qquad \xi_-(\hat{\mathbf p}) = \begin{pmatrix}-e^{-i\varphi}\sin\frac\theta2\\ \cos\frac\theta2\end{pmatrix} .
> $$
>
> They are an orthonormal and complete spin basis ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]).
>
> *Source: the user's write-up of PHY 513, Problem Set 5, Problem 6 (submitted) · the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis (Problem Set 5, Problem 6)") · Yu §5.4.2, eqs. (5.162)–(5.175) (Cartesian form)*

^thm-c5a-10-11

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 5, Problem 6.
>
> **Step 1** (the operator). With the Pauli matrices, $\hat{\mathbf p}\cdot\boldsymbol\sigma = \sin\theta\cos\varphi\,\sigma^1 + \sin\theta\sin\varphi\,\sigma^2 + \cos\theta\,\sigma^3$; adding the three matrices entry by entry, the off-diagonal entries are $\sin\theta(\cos\varphi \mp i\sin\varphi) = \sin\theta\,e^{\mp i\varphi}$:
>
> $$
> \hat{\mathbf p}\cdot\boldsymbol\sigma = \begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\varphi}\\ \sin\theta\,e^{i\varphi} & -\cos\theta\end{pmatrix} .
> $$
>
> The helicity equation $(\hat{\mathbf p}\cdot\boldsymbol\sigma/2)\xi = \pm\frac12\xi$, with the $\frac12$ cancelled, is $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi = \lambda\xi$, $\lambda = \pm1$. Check: $\det(\hat{\mathbf p}\cdot\boldsymbol\sigma - \lambda) = (\cos\theta - \lambda)(-\cos\theta - \lambda) - \sin^2\theta = \lambda^2 - \cos^2\theta - \sin^2\theta = \lambda^2 - 1$, zero for $\lambda = \pm1$.
>
> **Step 2** (remove $\varphi$). With $\xi = (x, y)$, the rows are $x\cos\theta + y\sin\theta\,e^{-i\varphi} = \lambda x$ and $x\sin\theta\,e^{i\varphi} - y\cos\theta = \lambda y$. Substitute $x = e^{-i\varphi/2}x'$, $y = e^{i\varphi/2}y'$: the first row becomes $e^{-i\varphi/2}(x'\cos\theta + y'\sin\theta) = \lambda e^{-i\varphi/2}x'$ (since $e^{i\varphi/2}e^{-i\varphi} = e^{-i\varphi/2}$), the second $e^{i\varphi/2}(x'\sin\theta - y'\cos\theta) = \lambda e^{i\varphi/2}y'$. Cancelling the phases,
>
> $$
> x'\cos\theta + y'\sin\theta = \lambda x', \qquad x'\sin\theta - y'\cos\theta = \lambda y' .
> $$
>
> **Step 3** (solve, in a form valid at $\theta = 0$). For $\lambda = +1$ the second equation is $x'\sin\theta = y'(1 + \cos\theta)$; for $\lambda = -1$ the first is $y'\sin\theta = -x'(1 + \cos\theta)$ (for $\sin\theta \neq 0$ each row implies the other, since $\frac{1 - \cos\theta}{\sin\theta}\cdot\frac{1 + \cos\theta}{\sin\theta} = 1$; the forms divided by $\sin\theta$ fail at $\theta = 0$, where the phases are to be fixed, so the undivided ones are kept). Solutions:
>
> $$
> \lambda = +1:\ \begin{pmatrix}x'\\ y'\end{pmatrix} = c_+\begin{pmatrix}1 + \cos\theta\\ \sin\theta\end{pmatrix}, \qquad \lambda = -1:\ \begin{pmatrix}x'\\ y'\end{pmatrix} = c_-\begin{pmatrix}-\sin\theta\\ 1 + \cos\theta\end{pmatrix} .
> $$
>
> Multiplying back the phases: $\xi_+ = c_+(e^{-i\varphi/2}(1 + \cos\theta),\ e^{i\varphi/2}\sin\theta)$, $\xi_- = c_-(-e^{-i\varphi/2}\sin\theta,\ e^{i\varphi/2}(1 + \cos\theta))$.
>
> **Step 4** (normalize). $\xi_+^\dagger\xi_+ = |c_+|^2\bigl((1 + \cos\theta)^2 + \sin^2\theta\bigr) = |c_+|^2(1 + 2\cos\theta + \cos^2\theta + \sin^2\theta) = |c_+|^2(2 + 2\cos\theta)$ (the phases $e^{\pm i\varphi/2}$ cancel against their conjugates), and the same for $\xi_-$. With the half-angle identities $1 + \cos\theta = 2\cos^2\frac\theta2$, $\sin\theta = 2\sin\frac\theta2\cos\frac\theta2$: $2 + 2\cos\theta = 4\cos^2\frac\theta2$, so for $0 \le \theta < \pi$, $c_+ = e^{i\alpha}/(2\cos\frac\theta2)$, $c_- = e^{i\beta}/(2\cos\frac\theta2)$, phases $\alpha, \beta$ free. Substituting the half-angle forms into the components, the factor $2\cos\frac\theta2$ cancels:
>
> $$
> \xi_+ = e^{i\alpha}\begin{pmatrix}e^{-i\varphi/2}\cos\frac\theta2\\ e^{i\varphi/2}\sin\frac\theta2\end{pmatrix}, \qquad \xi_- = e^{i\beta}\begin{pmatrix}-e^{-i\varphi/2}\sin\frac\theta2\\ e^{i\varphi/2}\cos\frac\theta2\end{pmatrix} .
> $$
>
> **Step 5** (fix the phases). At $\theta = 0$: $\xi_+ = e^{i\alpha}(e^{-i\varphi/2}, 0)$, $\xi_- = e^{i\beta}(0, e^{i\varphi/2})$. These are $(1, 0)$ and $(0, 1)$ for $\alpha = \varphi/2$, $\beta = -\varphi/2$, which gives the statement. ⚑ By-product: this phase choice is singular at $\theta = \pi$ → [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-2|Caution: No phase convention is smooth on the whole sphere]].
>
> **Step 6** (direct check for all $0 \le \theta \le \pi$, which also covers $\theta = \pi$ excluded in Step 4). With $\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2 = \sin(\theta - \frac\theta2) = \sin\frac\theta2$ and $\cos\theta\cos\frac\theta2 + \sin\theta\sin\frac\theta2 = \cos\frac\theta2$:
>
> $$
> (\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_+ = \begin{pmatrix}\cos\theta\cos\frac\theta2 + \sin\theta\sin\frac\theta2\\ e^{i\varphi}(\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2)\end{pmatrix} = \xi_+, \qquad (\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_- = \begin{pmatrix}e^{-i\varphi}(\sin\theta\cos\frac\theta2 - \cos\theta\sin\frac\theta2)\\ -(\sin\theta\sin\frac\theta2 + \cos\theta\cos\frac\theta2)\end{pmatrix} = -\xi_- ,
> $$
>
> and $\xi_\pm^\dagger\xi_\pm = \cos^2\frac\theta2 + \sin^2\frac\theta2 = 1$. (End of the user's solution.)
>
> **Step 7** (orthogonality and completeness). $\xi_+^\dagger\xi_- = \cos\frac\theta2(-e^{-i\varphi}\sin\frac\theta2) + e^{-i\varphi}\sin\frac\theta2\cos\frac\theta2 = 0$; also automatic, as eigenvectors of the Hermitian $\hat{\mathbf p}\cdot\boldsymbol\sigma$ with eigenvalues $+1 \neq -1$. Two orthonormal vectors in $\mathbb C^2$ form a basis, and completeness follows as in [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]].
>
> **What the derivation shows**
> - The phase substitution of Step 2 removes $\varphi$ from the equations; $\varphi$ re-enters only through the phase convention.
> - These are the spin-$\frac12$ eigenspinors along an axis of Quantum Mechanics ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]]); Griffiths' $\chi_-^{(r)}$ is $-\xi_-$, a different phase convention.

^der-c5a-10-11

*Uses:* [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-3|Def. §C5a.9.3]]

> [!derivation]- Derivation (second route: Yu's Cartesian form)
> Yu writes $\xi_+(\mathbf p) = \frac1{\sqrt{2|\mathbf p|(|\mathbf p| + p^3)}}\bigl(|\mathbf p| + p^3,\ p^1 + ip^2\bigr)$ and $\xi_-(\mathbf p) = \frac1{\sqrt{2|\mathbf p|(|\mathbf p| + p^3)}}\bigl(-p^1 + ip^2,\ |\mathbf p| + p^3\bigr)$ (5.162) and checks the eigenvalue equations, orthonormality and completeness by direct multiplication (5.170)–(5.175). In angles: $|\mathbf p| + p^3 = |\mathbf p|(1 + \cos\theta) = 2|\mathbf p|\cos^2\frac\theta2$; $p^1 \pm ip^2 = |\mathbf p|\sin\theta\,e^{\pm i\varphi} = 2|\mathbf p|\sin\frac\theta2\cos\frac\theta2\,e^{\pm i\varphi}$; the prefactor is $1/\sqrt{4|\mathbf p|^2\cos^2\frac\theta2} = 1/(2|\mathbf p|\cos\frac\theta2)$ for $\theta < \pi$. Dividing, $\xi_+ = (\cos\frac\theta2, e^{i\varphi}\sin\frac\theta2)$ and $\xi_- = (-e^{-i\varphi}\sin\frac\theta2, \cos\frac\theta2)$: the same spinors with the same phases. Yu's form is singular at $p^3 = -|\mathbf p|$ ($\theta = \pi$), the same point as in Step 4 above.
>
> *Source: Yu §5.4.2, eqs. (5.160)–(5.175) · the user's PHY 513 notes, Ch. 9 §9.3 ("These ξ± are exactly Yu's helicity states ξ_λ (5.162), written in angles")*

> [!caution] Caution: No phase convention is smooth on the whole sphere
> At $\theta = \pi$ the spinors of [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]] are $\xi_+ = (0, e^{i\varphi})$, $\xi_- = (-e^{-i\varphi}, 0)$: they depend on $\varphi$, which is meaningless at the south pole, so the phase convention is discontinuous there. Any other smooth phase choice fails somewhere: the helicity eigenvector, as a function of $\hat{\mathbf p}$ on the sphere, cannot be given a global continuous phase. It is the same obstruction as for the rotation $R(\hat{\mathbf p})$ in [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]] ("no choice is continuous on the whole sphere"), and it carries Berry's phase of a spin $\frac12$ ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]). Physical results (spin sums, $|{\rm amplitudes}|^2$) do not depend on the phases.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 ("at θ = π the phase convention is singular, a feature of any smooth choice of phase on the sphere") · the user's write-up of PHY 513, Problem Set 5, Problem 6 (the division by cos(θ/2))*

^cau-c5a-10-2

> [!theorem] Theorem §C5a.10.12: Helicity Spinors u±
> With $\xi^s = \xi_\pm(\hat{\mathbf p})$ in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], the square roots act as numbers:
>
> $$
> u_\pm(p) = \begin{pmatrix}\sqrt{E_{\mathbf p} \mp |\mathbf p|}\;\xi_\pm\\ \sqrt{E_{\mathbf p} \pm |\mathbf p|}\;\xi_\pm\end{pmatrix}, \qquad h\,u_\pm = \pm\tfrac12\,u_\pm .
> $$
>
> With Yu's abbreviation $\omega_\lambda \equiv \sqrt{E_{\mathbf p} + \lambda|\mathbf p|}$, $u_\lambda(p) = (\omega_{-\lambda}\xi_\lambda, \omega_\lambda\xi_\lambda)$ for $\lambda = \pm$, with $\omega_\lambda\omega_{-\lambda} = m$ (names in other sources: [[§C5a.9 Plane-Wave Solutions#^cau-c5a-9-3|§C5a.9, Caution: Names for the plane-wave spinors]]). All normalizations and the spin sum of this section hold for them.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 (Derivation "Example: the helicity basis", part "The Dirac spinors") · Yu §5.4.2, eqs. (5.165)–(5.181) · the user's pre-course notes, §5.4 · PS §3.3, eqs. (3.52)–(3.54)*

^thm-c5a-10-12

> [!derivation]- Derivation
> **Step 1** (the matrices on $\xi_\pm$). $p\cdot\sigma\,\xi_\pm = (E - |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_\pm = (E \mp |\mathbf p|)\xi_\pm$ and $p\cdot\bar\sigma\,\xi_\pm = (E \pm |\mathbf p|)\xi_\pm$ ([[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|Def. §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|Def. §C5a.10.2]]).
>
> **Step 2** (the roots on $\xi_\pm$). $\xi_\pm$ lies in the range of the projector $\Pi_\pm$, so by the spectral form of [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|Def. §C5a.9.5]], $\sqrt{p\cdot\sigma}\,\xi_\pm = \sqrt{E \mp |\mathbf p|}\,\xi_\pm$ and $\sqrt{p\cdot\bar\sigma}\,\xi_\pm = \sqrt{E \pm |\mathbf p|}\,\xi_\pm$. Inserting into $u^s(p)$ gives the stated $u_\pm$; with $\lambda = \pm1$ these are $\omega_{-\lambda}$ and $\omega_\lambda$, and $\omega_\lambda\omega_{-\lambda} = \sqrt{E^2 - \mathbf p^2} = m$.
>
> **Step 3** (helicity). $h$ acts on each half by $\frac12\hat{\mathbf p}\cdot\boldsymbol\sigma$, and each half of $u_\pm$ is a number times $\xi_\pm$: $h\,u_\pm = \pm\frac12u_\pm$.
>
> **Step 4** (normalizations). $\xi_\pm$ is an orthonormal spin basis ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]]), so Theorems §C5a.10.1, §C5a.10.2 and §C5a.10.7 apply unchanged; e.g. $u_\pm^\dagger u_\pm = (E \mp |\mathbf p|) + (E \pm |\mathbf p|) = 2E$ and $\bar u_\pm u_\pm = 2\sqrt{E \mp |\mathbf p|}\sqrt{E \pm |\mathbf p|} = 2m$.
>
> **What the derivation shows**
> - In a basis of eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol\sigma$ no matrix square root is needed: the only matrix in $p\cdot\sigma$ is $\mathbf p\cdot\boldsymbol\sigma$.
> - For $\mathbf p = p\hat{\mathbf z}$, $\xi_\pm = (1, 0), (0, 1)$ and these are PS's (3.52)–(3.53).
> - Used next: the massless limit ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]]).

^der-c5a-10-12

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-2|Def. §C5a.9.2]], [[§C5a.9 Plane-Wave Solutions#^def-c5a-9-5|Def. §C5a.9.5]], [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-1|Def. §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^def-c5a-10-2|Def. §C5a.10.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]]

> [!theorem] Theorem §C5a.10.13: The v Spinors in the Helicity Basis
> With $\eta^s = \lambda\,\xi_{-\lambda}$ ($\lambda = \pm$) in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]],
>
> $$
> v_\lambda(p) = \begin{pmatrix}\lambda\,\omega_\lambda\,\xi_{-\lambda}\\ -\lambda\,\omega_{-\lambda}\,\xi_{-\lambda}\end{pmatrix}, \qquad h\,v_\lambda(p) = -\tfrac\lambda2\,v_\lambda(p) ,
> $$
>
> Yu's choice; $\{\lambda\xi_{-\lambda}\}$ is an orthonormal spin basis, so $\bar vv = -2m$, $v^\dagger v = 2E$ and $\sum_\lambda v\bar v = \slashed{p} - m$ hold for it.
>
> *Source: Yu §5.4.2, eqs. (5.192)–(5.199), (5.213) · the user's pre-course notes, §5.4 · the user's PHY 513 notes, Ch. 9, "Correspondence with Yu" ("his v(p, λ) (5.196) is our (vspinor) with η^s = λξ_{−λ}")*

^thm-c5a-10-13

> [!derivation]- Derivation
> **Step 1** (the roots on $\xi_{-\lambda}$). By Step 2 of [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-12|Derivation §C5a.10.12]] with $\lambda \to -\lambda$: $\sqrt{p\cdot\sigma}\,\xi_{-\lambda} = \sqrt{E - (-\lambda)|\mathbf p|}\,\xi_{-\lambda} = \omega_\lambda\xi_{-\lambda}$ and $\sqrt{p\cdot\bar\sigma}\,\xi_{-\lambda} = \omega_{-\lambda}\xi_{-\lambda}$.
>
> **Step 2** (insert). $v = (\sqrt{p\cdot\sigma}\,\lambda\xi_{-\lambda},\ -\sqrt{p\cdot\bar\sigma}\,\lambda\xi_{-\lambda}) = (\lambda\omega_\lambda\xi_{-\lambda},\ -\lambda\omega_{-\lambda}\xi_{-\lambda})$.
>
> **Step 3** (helicity of the column). $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\xi_{-\lambda} = -\lambda\,\xi_{-\lambda}$, so $h\,v_\lambda(p) = -\frac\lambda2v_\lambda(p)$.
>
> **Step 4** (orthonormal basis). $(\lambda\xi_{-\lambda})^\dagger(\lambda'\xi_{-\lambda'}) = \lambda\lambda'\delta_{\lambda\lambda'} = \delta_{\lambda\lambda'}$ ($\lambda^2 = 1$; [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]]). Theorems §C5a.10.3, §C5a.10.4 and §C5a.10.8 then apply.
>
> **What the derivation shows**
> - ⚑ By-product: the column $v_\lambda(p)$ has helicity $-\lambda/2$, yet it is labelled $\lambda$: the label is the helicity of the *antiparticle* that its coefficient creates, which is opposite to that of the column. This is shown only after quantization (Yu §5.5.4; [[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]]); the factor $\lambda$ is a phase convention.
> - With $-i\sigma^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ and [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]]: $-i\sigma^2\xi_+^* = (-e^{-i\varphi}\sin\frac\theta2, \cos\frac\theta2) = \xi_-$ and $-i\sigma^2\xi_-^* = (-\cos\frac\theta2, -e^{i\varphi}\sin\frac\theta2) = -\xi_+$, i.e. $\lambda\xi_{-\lambda} = -i\sigma^2\xi_\lambda^*$: Yu's $v$ spinor is built from the conjugate-spin two-spinor, the pairing that charge conjugation will make systematic (QFT C9, planned).

^der-c5a-10-13

*Uses:* [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.10 Normalization, Spin Sums and Helicity#^der-c5a-10-12|Derivation §C5a.10.12]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]]

> [!remark] Remark: The helicity of a massive particle depends on the frame
> For $m > 0$ one can boost to a frame moving faster than the particle along $\hat{\mathbf p}$. There the momentum points the other way and the spin is unchanged, so the helicity flips: $u_+$ in one frame is a left-handed spinor in the other. Helicity is conserved by free motion ($h$ commutes with the free Dirac Hamiltonian, [[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]) but is not Lorentz invariant. For a massless particle no such boost exists, and helicity is a Lorentz invariant label ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]).
>
> *Source: PS §3.3, p. 47 · the user's PHY 513 notes, Ch. 7 §7.7*

^rem-c5a-10-3

### The mathematics used here: chirality

In the massless limit helicity becomes chirality, the eigenvalue of $\gamma^5$, whose eigenspaces are the Weyl halves:

![[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-14]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-4]]

## The massless and high-energy limit

> [!theorem] Theorem §C5a.10.14: The Massless and High-Energy Limit: Helicity Becomes Chirality
> 1. For $m = 0$: $u_+(p) = \sqrt{2E_{\mathbf p}}\begin{pmatrix}0\\ \xi_+\end{pmatrix}$, $u_-(p) = \sqrt{2E_{\mathbf p}}\begin{pmatrix}\xi_-\\ 0\end{pmatrix}$, and $\gamma^5u_\pm = \pm u_\pm$ ($\gamma^5$ of [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-11-14|Def. §CB.11.14]]): positive helicity lives entirely in the right-handed Weyl half $\psi_R$, negative helicity in $\psi_L$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]); helicity $\pm\frac12$ equals chirality $\pm1$ (divided by 2).
> 2. For $m > 0$, $E_{\mathbf p} \gg m$: the dominant half has amplitude $\sqrt{E + |\mathbf p|} = \sqrt{2E}\,(1 + O(m^2/E^2))$ and the other half $\sqrt{E - |\mathbf p|} = m/\sqrt{E + |\mathbf p|} \approx m/\sqrt{2E}$, so $u_\pm \to \sqrt{2E}\,(0, \xi_+)$, $\sqrt{2E}\,(\xi_-, 0)$ with corrections of relative size $m/2E$.
> 3. The $v$'s of [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-13|Theorem §C5a.10.13]] at $m = 0$: $v(p, +) = \sqrt{2E}(\xi_-, 0)$, $v(p, -) = \sqrt{2E}(0, \xi_+)$: the column of helicity $-\lambda/2$ sits in the Weyl half of that helicity.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.3 ("For E ≫ m, u₊ → √(2E)(0, ξ₊) … the origin of the names") · PS §3.3, eqs. (3.52)–(3.53) and p. 47 · the user's pre-course notes, §5.4 (note "Rest frame, and what ω_λω_{−λ} = m means")*

^thm-c5a-10-14

> [!derivation]- Derivation
> **Step 1** ($m = 0$). $E_{\mathbf p} = |\mathbf p|$, so $\sqrt{E - |\mathbf p|} = 0$ and $\sqrt{E + |\mathbf p|} = \sqrt{2E}$. In [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-12|Theorem §C5a.10.12]]: $u_+ = (0, \sqrt{2E}\,\xi_+)$, $u_- = (\sqrt{2E}\,\xi_-, 0)$ (the formula holds at $m = 0$ by [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], 2).
>
> **Step 2** (chirality). In the chiral basis $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, the upper half being $\psi_L$ and the lower $\psi_R$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]). So $\gamma^5u_+ = (0, \sqrt{2E}\xi_+) = +u_+$ and $\gamma^5u_- = (-\sqrt{2E}\xi_-, 0) = -u_-$; the chirality projectors $P_{R,L} = \frac12(\mathbb 1 \pm \gamma^5)$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]) keep $u_+$ and $u_-$ respectively. Part 1.
>
> **Step 3** (high energy). $E - |\mathbf p| = \frac{(E - |\mathbf p|)(E + |\mathbf p|)}{E + |\mathbf p|} = \frac{m^2}{E + |\mathbf p|}$, multiplying and dividing by $E + |\mathbf p| > 0$, so $\sqrt{E - |\mathbf p|} = m/\sqrt{E + |\mathbf p|}$. And $|\mathbf p| = \sqrt{E^2 - m^2} = E(1 - m^2/2E^2 + O(m^4/E^4))$, so $E + |\mathbf p| = 2E(1 - m^2/4E^2 + \dots)$ and $\sqrt{E + |\mathbf p|} = \sqrt{2E}(1 + O(m^2/E^2))$. The ratio of the small to the large half is $m/(E + |\mathbf p|) \approx m/2E$. Part 2.
>
> **Step 4** ($v$). At $m = 0$, $\omega_+ = \sqrt{2E}$, $\omega_- = 0$; [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-13|Theorem §C5a.10.13]] gives $v(p, +) = (\omega_+\xi_-, -\omega_-\xi_-) = \sqrt{2E}(\xi_-, 0)$ and $v(p, -) = (-\omega_-\xi_+, \omega_+\xi_+) = \sqrt{2E}(0, \xi_+)$. Part 3.
>
> **What the derivation shows**
> - At $m = 0$ each helicity spinor occupies a single Weyl block: the solutions of the Weyl equations have fixed helicity ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-12|Theorem §C5a.7.12]]), and the Lorentz invariance of chirality ($\gamma^5$ commutes with $\Lambda_{1/2}$) is the Lorentz invariance of massless helicity ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]).
> - The $\sqrt m$ convention keeps the spinors finite as $m \to 0$ (PS, p. 47).
> - ⚑ By-product: the wrong-chirality amplitude is $m/\sqrt{E + |\mathbf p|}$, linear in $m$ → [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-4|Remark: The mass is what connects the two chiral blocks]].

^der-c5a-10-14

*Uses:* [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-12|Theorem §C5a.10.12]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-13|Theorem §C5a.10.13]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]

> [!remark] Remark: The mass is what connects the two chiral blocks
> In $u_\lambda(p) = (\omega_{-\lambda}\xi_\lambda, \omega_\lambda\xi_\lambda)$ the two Weyl blocks have sizes $\omega_{-\lambda}$ and $\omega_\lambda$ with $\omega_\lambda\omega_{-\lambda} = m$: the "wrong" chirality is present with amplitude $m/\omega_\lambda$. At rest both blocks are equal ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]]); boosting shrinks one and grows the other; at $m = 0$ one vanishes. This is the plane-wave form of the Dirac equation in Weyl components, where only $m$ couples $\psi_L$ and $\psi_R$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]). Chirality is Lorentz invariant but, for $m > 0$, not conserved; helicity is conserved by free motion but, for $m > 0$, frame dependent ([[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-3|Remark: The helicity of a massive particle depends on the frame]]); at $m = 0$ they coincide and both are good labels. Interactions that couple to one chirality (the vector coupling $\bar\psi\gamma^\mu\psi$ preserves chirality) therefore suppress helicity flips by powers of $m/E$ — the helicity structure of QED amplitudes at high energy (Lecture 20; QFT C8, planned).
>
> *Source: the user's pre-course notes, §5.4 (note "Rest frame, and what ω_λω_{−λ} = m means": "the mass, divided by the energy scale, is the amplitude with which the 'wrong' chirality is populated") · PS §3.3, p. 47*

^rem-c5a-10-4

> [!remark] Remark: The solutions at a glance
> For the Dirac equation $(i\slashed{\partial} - m)\psi = 0$, with $p^0 = +E_{\mathbf p}$ in both columns and orthonormal bases $\xi^s$, $\eta^s$:
>
> | | positive frequency | negative frequency |
> |---|---|---|
> | solution | $u^s(p)\,e^{-ip\cdot x}$ | $v^s(p)\,e^{+ip\cdot x}$ |
> | spinor | $(\sqrt{p\cdot\sigma}\,\xi^s,\ \sqrt{p\cdot\bar\sigma}\,\xi^s)$ | $(\sqrt{p\cdot\sigma}\,\eta^s,\ -\sqrt{p\cdot\bar\sigma}\,\eta^s)$ |
> | equation | $(\slashed{p} - m)u = 0$ | $(\slashed{p} + m)v = 0$ |
> | Dirac conjugate | $(\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma})$ | $(-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma})$ |
> | conjugate equation | $\bar u(\slashed{p} - m) = 0$ | $\bar v(\slashed{p} + m) = 0$ |
> | $\psi^\dagger\psi$ type | $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$ | $v^{r\dagger}v^s = 2E_{\mathbf p}\delta^{rs}$ |
> | invariant | $\bar u^ru^s = 2m\,\delta^{rs}$ | $\bar v^rv^s = -2m\,\delta^{rs}$ |
> | spin sum | $\sum_su^s\bar u^s = \slashed{p} + m$ | $\sum_sv^s\bar v^s = \slashed{p} - m$ |
>
> and $\bar v^ru^s = \bar u^rv^s = 0$, $u^{r\dagger}(\mathbf p)v^s(-\mathbf p) = v^{r\dagger}(\mathbf p)u^s(-\mathbf p) = 0$. Homes: [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], Theorems §C5a.10.1–§C5a.10.8.
>
> *Source: the user's PHY 513 notes, Ch. 9 §9.7 (Principle "Solutions of the Dirac equation") · PHY 513 Lecture 9, Summary I–III*

^rem-c5a-10-5

> [!remark]- Connections
> - $u^\dagger u = 2E_{\mathbf p}$ is the same weight as the relativistic normalization of states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); with it the Dirac mode expansion has the scalar field's $1/\sqrt{2E_{\mathbf p}}$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]; [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]), and one-particle Dirac states are normalized exactly as scalar ones.
> - The orthogonality of $u^r(p)$ and $v^s(\tilde p)$, $\tilde p = (E_{\mathbf p}, -\mathbf p)$, is the spinor counterpart of the scalar field's pairing of $\mathbf p$ with $-\mathbf p$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|§C2a.2, Remark: Why the modes decouple]]): it removes the $\hat a^\dagger \hat b^\dagger$ and $\hat b\hat a$ cross terms of $\hat H$ (mode operators named as in [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-1|§C5b.1, Caution: Names for the Dirac field and its mode operators across sources]]), as the $\hat a_{\mathbf p}\hat a_{-\mathbf p}$ terms cancelled for $\hat\phi$.
> - The indefinite form $\bar ab$, positive on $u$ and negative on $v$, parallels the Klein–Gordon inner product, positive on positive-frequency and negative on negative-frequency modes ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|Remark: Why this inner product, and why it is indefinite]]); $\psi^\dagger\psi = \bar\psi\gamma^0\psi$ is positive for both, which is why the Dirac charge before quantization is positive and its energy is not ([[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]], Connections).
> - The spin sums are the numerators of the Dirac propagator: $\slashed{p} + m$ at the positive-energy pole and $\slashed{p} - m$ (with $p \to -p$) at the negative one ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], draft; [[P2 Green's Functions by Contour Integration|P2]], Dirac row); summed over spins, squared amplitudes become traces ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]]).
> - $\Lambda_\pm = (\pm\slashed{p} + m)/2m$ are the covariant versions of $\frac12(1 \pm \beta)$, the projectors onto the large and small components of Quantum Mechanics' Dirac spinors at rest ([[§C13.3★ Solutions of the Dirac Equation and the Hydrogen Atom#^thm-c13-3-1|QM Theorem §C13.3.1]]).
> - The helicity two-spinors are the spin-up and spin-down spinors along $\hat{\mathbf p}$ of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-5|QM Theorem §B6.1.5]] (Bloch-sphere angles of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-6|QM Theorem §B6.1.6]]); their phase singularity at the south pole is the one behind Berry's phase ([[§C9.4 Time-Dependent Perturbation Theory, Sudden and Adiabatic Limits#^thm-c9-4-8|QM Theorem §C9.4.8]]) and behind the discontinuous $R(\hat{\mathbf p})$ of [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
> - Helicity = chirality at $m = 0$ is the field-level statement of [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]: the Weyl representations $(\frac12, 0)$ and $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]) carry helicity $-\frac12$ and $+\frac12$ particles; a single Weyl field describes the neutrino of [[§C3.7★ Massless Particles and Helicity#^rem-c3-7-2|§C3.7★, Remark: Parity pairs λ with −λ]] ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-11|Model §C5a.7.11]]).
> - $\bar u(p')\gamma^\mu u(p)$ at $p' = p$ is $2p^\mu$ by the Gordon identity ([[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]]): the spinors are "square roots" of the momentum, the counterpart of the half-rapidity of [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-4|§C5a.9, Remark: Why a square root restores the full rapidity]].
> - Math: completeness relations ([[§38 The Completeness Relation#^prop-38-1|556 Prop. §38.1]]); orthogonality of eigenvectors of a Hermitian matrix (second route of Theorem §C5a.10.6); complementary projectors $P^2 = P$, $PQ = 0$, $P + Q = 1$ (Theorem §C5a.10.10).
