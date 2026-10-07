---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.2 The Dirac Form]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.4 SL(2,C) and the Group Action on Spinor Space]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.1–§3.2, pp. 38–43, eqs. (3.17)–(3.30) · PHY 513 Lecture 7 (Larsen), Part B ("Given such $\gamma^\mu$, form a $4\times4$ matrix for each $(\mu\nu)$ pair"; "Finite Lorentz Transformations in Dirac Representation"); Lecture 8, Cheat Sheets I–II and Part A · the user's PHY 513 notes, Ch. 7 §7.4 (the $(j_+, j_-)$ classification), Ch. 8 §8.1 (Definitions "The spinor generators", "The spinor Lorentz transformation $\Lambda_{1/2}$"; Derivations "Proof of the claim", "The generators in the chiral basis", "Hermiticity of the Dirac matrices: Consequence for the generators"; paragraph "Why 'half'"), §8.2 ("How the two halves transform") · PHY 513, Problem Set 4, Problem 5(b)–(c) (as the user wrote them; submitted) · Yu Zhao-Huan, 量子场论讲义, opening of Ch. 5, §5.1, eqs. (5.8)–(5.16), (5.24), §5.2, eqs. (5.76)–(5.79) · the user's pre-course notes, §5.1.*

How does the Lorentz group act on spinor space? Nothing in layers 1–3 ([[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]], [[§C5a.2 The Dirac Form|§C5a.2]]) mentions it: $V$ has bases, the Clifford action $\Gamma^\mu$ and the Dirac form. This section adds **layer 4**, the action of the Lorentz *algebra* ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]): from the $\gamma$'s alone one builds six generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, proves that they obey the Lorentz algebra *because of* the Clifford algebra, exponentiates them to $\Lambda_{1/2}$, and identifies the result with the classification of §C3.3: a **spinor representation** ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]), namely $(\frac12, 0)\oplus(0, \frac12)$. The definitions it uses are recalled below by embedding. The group-level structure ($SL(2, \mathbb C)$, the finite matrices, $\gamma^\mu$ as an invariant tensor) is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]; the chirality grading that separates the two halves in every basis is [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]].

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Hermitian convention, the $D(\mathcal J^{\mu\nu})$ of §C3.2; [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]]); $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with the same $\omega_{\mu\nu}$ as $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$, $K_i = \mathcal J^{0i}$; $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$.

## The spinor generators

> [!definition] Definition §C5a.3.1: The Spinor Generators
> Given Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]), the six **spinor generators** are
>
> $$
> S^{\mu\nu} = \frac i4\,[\gamma^\mu, \gamma^\nu] = -S^{\nu\mu}, \qquad\text{equivalently}\qquad S^{\mu\nu} = \frac i2\bigl(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbb 1\bigr) .
> $$
>
> *Source: PS §3.2, eq. (3.23) · PHY 513 Lecture 7, Part B ("Given such $\gamma^\mu$, form a $4\times4$ matrix for each $(\mu\nu)$ pair") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor generators", eq. (Sdef)) · Yu §5.1, eqs. (5.8)–(5.9) · the user's pre-course notes, §5.1, eq. (spinor-generators)*

^def-c5a-3-1

The second form follows from $\gamma^\nu\gamma^\mu = 2g^{\mu\nu} - \gamma^\mu\gamma^\nu$: $[\gamma^\mu, \gamma^\nu] = 2\gamma^\mu\gamma^\nu - 2g^{\mu\nu}$. For $\mu \ne \nu$, $S^{\mu\nu} = \frac i2\gamma^\mu\gamma^\nu$; $S^{\mu\mu} = 0$. Yu and Peskin–Schroeder also use $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] = 2S^{\mu\nu}$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]).

> [!theorem] Theorem §C5a.3.1: The Dirac Matrices Rotate as a Vector
> With the vector generators $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]],
>
> $$
> [\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\,\gamma^\nu = i\bigl(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho\bigr) .
> $$
>
> *Source: PHY 513, Problem Set 4, Problem 5(b) (as the user wrote it) · PS §3.2, p. 42 (stated, "with a short computation") · PHY 513 Lecture 8, Part A ("Compute (using Dirac algebra)") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 1, eq. (gammaS)) · Yu §5.1, eqs. (5.11), (5.24)*

^thm-c5a-3-1

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
> - The commutator with a spinor generator acts on the *label* $\mu$ of $\gamma^\mu$ exactly as the vector generator acts on a four-vector: the infinitesimal form of "$\gamma^\mu$ is a vector" (finite form, Theorem §C5a.4.11).
> - Only the Clifford algebra was used; the result holds in every basis and every dimension $n$.
> - Used next: the Lorentz algebra for $S^{\mu\nu}$ (Theorem §C5a.3.2).

^der-c5a-3-1

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]

> [!theorem] Theorem §C5a.3.2: The Spinor Generators Obey the Lorentz Algebra
>
> $$
> [S^{\mu\nu}, S^{\rho\sigma}] = i\bigl(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho}\bigr) ,
> $$
>
> the relations of [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]] with $\mathcal J \to S$. Hence the $S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) are the generators of a representation of the Lorentz algebra on $\mathbb C^n$ ([[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]).
>
> *Source: PHY 513, Problem Set 4, Problem 5(c) (as the user wrote it) · PS §3.2, p. 40 ("By repeated use of (3.22), it is easy to verify") · PHY 513 Lecture 7, Part B ("Claim: $S^{\mu\nu}$ satisfy Lorentz algebra") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Proof of the claim", Step 2) · Yu §5.1, eq. (5.12)*

^thm-c5a-3-2

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
> **3. Insert Theorem §C5a.3.1.** $[\gamma^\mu, S^{\rho\sigma}] = i(g^{\rho\mu}\gamma^\sigma - g^{\sigma\mu}\gamma^\rho)$ and $[\gamma^\nu, S^{\rho\sigma}] = i(g^{\rho\nu}\gamma^\sigma - g^{\sigma\nu}\gamma^\rho)$. Expanding all four products into eight terms:
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
> **5. Back to S.** From Def. §C5a.3.1, $[\gamma^a, \gamma^b] = -4iS^{ab}$, so $X = i(-4i)[g^{\rho\nu}S^{\mu\sigma} - g^{\sigma\nu}S^{\mu\rho} + g^{\rho\mu}S^{\sigma\nu} - g^{\sigma\mu}S^{\rho\nu}] = 4[\dots]$.
>
> **6. Restore the factor and reorder.** $[S^{\mu\nu}, S^{\rho\sigma}] = \frac i4X = i(g^{\nu\rho}S^{\mu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\rho}S^{\sigma\nu} - g^{\mu\sigma}S^{\rho\nu})$; with $S^{\sigma\nu} = -S^{\nu\sigma}$, $S^{\rho\nu} = -S^{\nu\rho}$ and the symmetry of $g$ this is $i(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho})$.
>
> **What the derivation shows**
> - The Lorentz algebra of the $S$'s is a consequence of the Clifford algebra alone, through Theorem §C5a.3.1: in any dimension and signature, $\frac i4[\gamma, \gamma]$ represents the corresponding orthogonal algebra (PS: in three Euclidean dimensions $\gamma^j = i\sigma^j$ gives $S^{ij} = \frac12\varepsilon^{ijk}\sigma^k$, spin ½, PS (3.24)).
> - This is "the step that makes everything after it legitimate" (the user's notes): exponentiating six matrices gives a representation of the group, up to the global sign of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], only if they obey its algebra. Yu's route (5.11)–(5.12) is the same computation, with $[S^{\mu\nu}, \gamma^\rho]$ in place of $[\gamma^\mu, S^{\rho\sigma}]$.
> - Used next: the Dirac representation (Def. §C5a.3.2).

^der-c5a-3-2

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]

## The Dirac representation

> [!definition] Definition §C5a.3.2: The Dirac Representation
> The **Dirac representation** is the representation of the Lorentz algebra on $\mathbb C^4$ whose generators ([[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]) are $D(\mathcal J^{\mu\nu}) = S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]). For parameters $\omega_{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]),
>
> $$
> \Lambda_{1/2}(\omega) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}S^{\mu\nu}\Bigr), \qquad \psi \to \Lambda_{1/2}\,\psi ,
> $$
>
> and a **Dirac spinor** is a column $\psi \in \mathbb C^4$ transforming so. A **Dirac field** transforms as $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ ([[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]]).
>
> *Source: PS §3.2, eq. (3.30) · PHY 513 Lecture 7, Part B ("Finite Lorentz Transformations in Dirac Representation"), Part C ("Dirac 4-Spinor") · PHY 513 Lecture 8, Cheat Sheet II · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation $\Lambda_{1/2}$", eq. (Lhalf)) · Yu §5.1, eq. (5.14)*

^def-c5a-3-2

The exponent $\omega_{\mu\nu}S^{\mu\nu}$ is linear in the six parameters; $\Lambda_{1/2}$ depends on them nonlinearly (Lecture 7). $\Lambda_{1/2}^{-1}(\omega) = \Lambda_{1/2}(-\omega)$ (Yu (5.16)). As a function of the group element $\Lambda = e^\omega$ rather than of $\omega$, $\Lambda_{1/2}$ is fixed only up to sign ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]). A quantum Dirac field is an operator-valued distribution; the law then holds after smearing, as for every field ([[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-2|§C3.4, Remark: The laws for fields that are distributions]]).

> [!definition] Definition §C5a.3.3: Spin Matrices of the Dirac Representation
> The **spin matrices** of the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) are the $4\times4$ matrices
>
> $$
> S^i \equiv \tfrac12\varepsilon^{ijk}S^{jk}, \qquad i = 1, 2, 3, \qquad \mathbf S = (S^1, S^2, S^3), \qquad \Sigma^i \equiv 2S^i ,
> $$
>
> the rotation generators among the spinor generators $S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; they are the matrices $J_i$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] for this representation, named $\mathbf S$ so that $\hat{\mathbf J}$ stays the Hilbert-space angular momentum, as for the vector field, [[§C4.1 The Vector Field and Its Lorentz Transformation#^def-c4-1-1|Def. §C4.1.1]]). In the chiral basis $\Sigma^i = \operatorname{diag}(\sigma^i, \sigma^i)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]).
>
> *Source: PS §3.2, eq. (3.27) and §3.3, p. 45 · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis"), Ch. 9 §9.2 · Yu §5.2, eqs. (5.76)–(5.79)*

^def-c5a-3-3

> [!theorem] Theorem §C5a.3.3: The Generators in the Chiral Basis
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), with $\Sigma^k = \operatorname{diag}(\sigma^k, \sigma^k)$,
>
> $$
> S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k = \frac12\varepsilon^{ijk}\begin{pmatrix}\sigma^k&0\\0&\sigma^k\end{pmatrix}, \qquad S^{0i} = -\frac i2\begin{pmatrix}\sigma^i&0\\0&-\sigma^i\end{pmatrix}, \qquad S^{\mu\nu} = \frac i4\begin{pmatrix}\sigma^\mu\bar\sigma^\nu - \sigma^\nu\bar\sigma^\mu & 0\\0 & \bar\sigma^\mu\sigma^\nu - \bar\sigma^\nu\sigma^\mu\end{pmatrix} ,
> $$
>
> so the rotation and boost generators ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]) are $\mathbf J = \frac12\boldsymbol\Sigma$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$. All six are block diagonal.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) · PHY 513 Lecture 7, Part B; Lecture 8, Cheat Sheet I · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis", eq. (Sexplicit)) · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-3

> [!derivation]- Derivation
> **1. General block form.** By Theorem §C5a.1.10, $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$; subtracting the same with $\mu \leftrightarrow \nu$ and multiplying by $\frac i4$ gives the third formula.
>
> **2. Rotations.** For spatial $i, j$: $\sigma^i\bar\sigma^j - \sigma^j\bar\sigma^i = -\sigma^i\sigma^j + \sigma^j\sigma^i = -[\sigma^i, \sigma^j] = -2i\varepsilon^{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 2), and the lower block $\bar\sigma^i\sigma^j - \bar\sigma^j\sigma^i = -[\sigma^i, \sigma^j]$ is the same. Times $\frac i4$: $\frac i4(-2i)\varepsilon^{ijk}\sigma^k = \frac12\varepsilon^{ijk}\sigma^k$ in both blocks.
>
> **3. Boosts.** Upper block of $S^{0i}$: $\sigma^0\bar\sigma^i - \sigma^i\bar\sigma^0 = -\sigma^i - \sigma^i = -2\sigma^i$, times $\frac i4$: $-\frac i2\sigma^i$. Lower block: $\bar\sigma^0\sigma^i - \bar\sigma^i\sigma^0 = \sigma^i + \sigma^i = 2\sigma^i$, times $\frac i4$: $+\frac i2\sigma^i = -\frac i2(-\sigma^i)$.
>
> **4. J and K.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], $J_k = \frac12\varepsilon_{kij}S^{ij} = \frac12\varepsilon_{kij}\cdot\frac12\varepsilon_{ijl}\Sigma^l = \frac14\cdot2\delta_{kl}\Sigma^l = \frac12\Sigma^k$, using $\varepsilon_{kij}\varepsilon_{lij} = 2\delta_{kl}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and $\varepsilon_{ijl} = \varepsilon_{lij}$; and $K_i = S^{0i}$.
>
> **What the derivation shows**
> - The rotation generators are spin ½ twice over, $\frac12\boldsymbol\sigma$ in each block; the boost generators are $\mp\frac i2\boldsymbol\sigma$, opposite in the two blocks: exactly the two rows of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]], stacked.
> - The factor $\frac12$ in $S^{ij}$ is what makes a $2\pi$ rotation $-1$ (Theorem §C5a.3.4, Theorem §C5a.4.9; [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]).

^der-c5a-3-3

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-10|Theorem §C5a.1.10]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

## The Dirac representation is a spinor representation

The classification of finite-dimensional representations is §C3.3; the three items it provides for this layer are recalled verbatim.

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-3]]

> [!theorem] Theorem §C5a.3.4: The Dirac Representation Is (½, 0) ⊕ (0, ½)
> In the chiral basis $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]) are $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, $\mathbf J_- = \frac12\operatorname{diag}(0, \boldsymbol\sigma)$: the upper half is the representation $(\frac12, 0)$, the lower $(0, \frac12)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]]). The Dirac representation is a spinor representation ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]): a rotation by $2\pi$ acts as $-\mathbb 1_4$.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27), (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts": "4 dim. Dirac spinor representation is reducible") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivations "How the two halves transform", "… related by conjugation": "Their labels") · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-4

> [!derivation]- Derivation
> **1. The labels.** From Theorem §C5a.3.3, $\mathbf J = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, so $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K) = \frac12\bigl(\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm i(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr) = \frac14\bigl(\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm \operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr)$, using $i\cdot(-\frac i2) = \frac12$. The upper sign gives $\frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, the lower $\frac12\operatorname{diag}(0, \boldsymbol\sigma)$.
>
> **2. Each block is one of the two representations.** On the upper block $\mathbf J_+ = \frac12\boldsymbol\sigma$ (spin $\frac12$) and $\mathbf J_- = 0$ (spin $0$): by [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]] with $j_+ = \frac12$, $j_- = 0$ this is $(\frac12, 0)$, and indeed $\mathbf J = \frac12\boldsymbol\sigma$, $\mathbf K = -\frac i2\boldsymbol\sigma$ there, the first row of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]]. On the lower block $\mathbf J_+ = 0$, $\mathbf J_- = \frac12\boldsymbol\sigma$, $\mathbf K = +\frac i2\boldsymbol\sigma$: $(0, \frac12)$, the second row. Both blocks are invariant, since every generator is block diagonal (Theorem §C5a.3.3).
>
> **3. Spinor representation.** On each block $j_+ + j_- = \frac12$, so a $2\pi$ rotation is $(-1)^{2\cdot\frac12} = -1$ there ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]], 1). Directly: $e^{-2\pi iJ_3} = \operatorname{diag}(e^{-i\pi\sigma^3}, e^{-i\pi\sigma^3}) = \operatorname{diag}(-\mathbb 1, -\mathbb 1)$, since $e^{-i\pi\sigma^3} = \operatorname{diag}(e^{-i\pi}, e^{i\pi})$.
>
> **What the derivation shows**
> - $\mathbf J_+$ acts only on the upper two components and $\mathbf J_-$ only on the lower two: the Dirac spinor is a direct sum, $2 + 2$, of the two smallest spinor representations, read off from $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ in one basis. In every basis the halves are the eigenspaces of $\gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]).
> - Each half is irreducible and the two are inequivalent ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]; the user's notes argue directly: an intertwiner commutes with $\frac12\boldsymbol\sigma$, so is $c\mathbb 1$ by Schur, and cannot turn $-\frac i2\boldsymbol\sigma$ into $+\frac i2\boldsymbol\sigma$); they are complex conjugates of each other up to basis ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]).
> - Used next: the finite matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]).

^der-c5a-3-4

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]

> [!remark] Remark: Why half the angle
> The rotation generator $\mathcal J^{12}$ of the vector representation has eigenvalues $\pm1$ (on $x \pm iy$) and $0$ twice (on $t$, $z$); the spinor generator $S^{12} = \frac12\Sigma^3$ has $\pm\frac12$. For boosts, $\mathcal J^{01}$ has $\pm i$ and $S^{01}$ has $\pm\frac i2$. Exponentiating $\theta$ times an eigenvalue $s$ gives the phase $e^{-is\theta}$: spin $1$ turns with the full angle, spin $\frac12$ with half of it, and the $2\pi$ sign is $e^{-i\pi} = -1$. The factor $\frac12$ in $S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k$ is therefore essential; the user's notes record that the handwritten lecture notes omit it, while the Lecture 8 slides have it.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Why 'half'"), Caution "A missing ½ in the handwritten notes" · PHY 513 Lecture 8, Cheat Sheet I*

^rem-c5a-3-1

## Adjoints of the generators

> [!theorem] Theorem §C5a.3.5: Adjoints of the Generators
> 1. For the spinor generators ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) of Hermitian Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]), $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$. In particular $S^{ij}$ commutes with $\gamma^0$ and is Hermitian; $S^{0i}$ anticommutes with $\gamma^0$ and is anti-Hermitian.
> 2. $\Lambda_{1/2}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) is unitary for rotations and Hermitian positive (not unitary) for pure boosts, the spin-½ case of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "Hermiticity of the Dirac matrices", "Consequence for the generators"; Derivation "What replaces unitarity", Step 1; Caution "Spinor boosts are not unitary") · PHY 513 Lecture 8, Part B (slides "The Hermitean Conjugate Spinor", "The Dirac Conjugate Spinor") · PS §3.2, p. 41 ("The boost generators $S^{0i}$ are not Hermitian") and p. 43*

^thm-c5a-3-5

> [!derivation]- Derivation
> **1. Adjoint of a commutator.** $[A, B]^\dagger = (AB - BA)^\dagger = B^\dagger A^\dagger - A^\dagger B^\dagger = [B^\dagger, A^\dagger]$, and the $i$ is conjugated: $S^{\mu\nu\dagger} = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}]$.
>
> **2. Insert Hermiticity.** With $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ (Theorem §C5a.1.11): $[\gamma^0\gamma^\nu\gamma^0, \gamma^0\gamma^\mu\gamma^0] = \gamma^0\gamma^\nu\gamma^0\gamma^0\gamma^\mu\gamma^0 - \gamma^0\gamma^\mu\gamma^0\gamma^0\gamma^\nu\gamma^0 = \gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0$, using $(\gamma^0)^2 = \mathbb 1$ in the middle of each product. So $S^{\mu\nu\dagger} = -\frac i4\gamma^0[\gamma^\nu, \gamma^\mu]\gamma^0 = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu]\gamma^0 = \gamma^0S^{\mu\nu}\gamma^0$.
>
> **3. The two cases.** $S^{ij} = \frac i2\gamma^i\gamma^j$ ($i \ne j$): moving $\gamma^0$ through two $\gamma$'s gives $(-1)^2$, so $\gamma^0S^{ij} = S^{ij}\gamma^0$ and $S^{ij\dagger} = S^{ij}(\gamma^0)^2 = S^{ij}$. $S^{0i} = \frac i2\gamma^0\gamma^i$: $\gamma^0$ anticommutes with $\gamma^i$ and commutes with itself, so $\gamma^0S^{0i} = -S^{0i}\gamma^0$ and $S^{0i\dagger} = -S^{0i}$. (In the chiral basis this is visible in Theorem §C5a.3.3: $\frac12\Sigma^k$ Hermitian, $-\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$ anti-Hermitian.)
>
> **4. Part 2.** For a rotation $\Lambda_{1/2} = e^{-i\boldsymbol\theta\cdot\mathbf J}$ with $\mathbf J$ Hermitian: $(e^{-iX})^\dagger = e^{iX} = (e^{-iX})^{-1}$, unitary. For a pure boost $\Lambda_{1/2} = e^{-i\boldsymbol\eta\cdot\mathbf K}$ and $-i\mathbf K$ is Hermitian ($\mathbf K$ anti-Hermitian), so $\Lambda_{1/2}$ is the exponential of a Hermitian matrix: Hermitian with positive eigenvalues, unitary only for $\boldsymbol\eta = 0$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]).
>
> **What the derivation shows**
> - $\psi^\dagger\psi$ is not invariant under boosts. What replaces unitarity is that $\gamma^0$ turns the adjoint into the inverse, $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$, so $\bar\psi = \psi^\dagger\gamma^0$ transforms with $\Lambda_{1/2}^{-1}$: [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]].
> - That is the price of Theorem §C3.3.10 for spin ½; the lecture: "$\psi$ is not a wavefunction; it is a classical field" (PS p. 41), so non-unitarity is harmless.

^der-c5a-3-5

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]

> [!remark]- Connections
> - The Clifford algebra is the multiplication rule of a "square root of the metric", and the Lorentz algebra follows from it: in every dimension and signature $\frac i4[\gamma, \gamma]$ represents the orthogonal algebra, with spin ½ for rotations in three dimensions as the case $\gamma^j = i\sigma^j$ — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-4|QM Theorem §C5.1.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].
> - The non-unitarity of spinor boosts is the spin-½ instance of the theorem that no nontrivial finite-dimensional Lorentz representation is unitary; $\gamma^0$ restores an invariant form as $g$ does for vectors — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]].
> - The $-1$ of a $2\pi$ rotation on $\Lambda_{1/2}$ is the sign the spin–statistics theorem ties to anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-4|QM Theorem §C5.2.4]] (the measured sign).
> - The spinor representation of §C3.3 is defined by one group element, the $2\pi$ rotation; the Dirac representation realizes the smallest parity-symmetric instance, $(\frac12, 0)\oplus(0, \frac12)$, from the $\gamma$'s — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-8|Theorem §C3.3.8]].
> - The spinor generators are the $D(\mathcal J^{\mu\nu})$ of the Dirac field's transformation law, and the orbital part adds to them in the total angular momentum — [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-3|Theorem §C3.4.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-8|Theorem §C5a.8.8]].
