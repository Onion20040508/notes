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

How does the Lorentz group act on spinor space? Nothing in layers 1–3 ([[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]], [[§C5a.2 The Dirac Form|§C5a.2]]) mentions it: $V$ has bases, the Clifford action $\Gamma^\mu$ and the Dirac form. This section adds **layer 4**, the action of the Lorentz *algebra* ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]): from the $\gamma$'s alone one builds six generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, proves that they obey the Lorentz algebra *because of* the Clifford algebra, exponentiates them to $\Lambda_{1/2}$, and identifies the result with the classification of §CB.18: a **spinor representation** ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]), namely $(\frac12, 0)\oplus(0, \frac12)$. This section states the Dirac representation and field law, the generators in the chiral basis, and what they mean physically. The algebra behind it — the generators of a Clifford module, the Lorentz algebra they obey, their exponentials and adjoints, and the classification of finite-dimensional representations — is mathematics, proved in [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations|§CB.5]], [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.15]] and [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.18]]–[[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.19]], linked from each box and listed at the end. The group-level structure ($SL(2, \mathbb C)$, the finite matrices, $\gamma^\mu$ as an invariant tensor) is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]; the chirality grading that separates the two halves in every basis is [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]].

**Setup.** Representation facts, no dynamics: the boxes are about the action of the Lorentz algebra and its exponential on $V$. They hold for any Dirac spinor, whether the value of a classical field (whose law $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ also moves the argument, [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), a c-number spinor, or the spinor index of the quantum field $\hat\psi$, on which the same matrix $\Lambda_{1/2}$ acts ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^cau-c5a-4-1|§C5a.4, Caution: Three different transformations]]); all of it is exact and holds for every mass. Matrix computations (the explicit generators) carry no *Model* line.

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Hermitian convention, the $D(\mathcal J^{\mu\nu})$ of §C3.2; [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]); $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with the same $\omega_{\mu\nu}$ as $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$, $K_i = \mathcal J^{0i}$; $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$.

## The Dirac representation

> [!definition] Definition §C5a.3.1: The Dirac Representation
> The **Dirac representation** is the representation of the Lorentz algebra on $\mathbb C^4$ whose generators ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-1|Def. §C3.2.1]]) are the **spinor generators** built from the Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]),
>
> $$
> D(\mathcal J^{\mu\nu}) = S^{\mu\nu} \equiv \frac i4\,[\gamma^\mu, \gamma^\nu] = -S^{\nu\mu}
> $$
>
> ([[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-16|Def. §CB.15.16]]), which obey the Lorentz algebra by the Clifford relation alone ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]). For parameters $\omega_{\mu\nu}$ ([[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-1|Def. §C1a.7.1]]),
>
> $$
> \Lambda_{1/2}(\omega) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}S^{\mu\nu}\Bigr), \qquad \psi \to \Lambda_{1/2}\,\psi ,
> $$
>
> ([[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-19|Def. §CB.15.19]] with $n = 4$), and a Dirac spinor ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-1|Def. §C5a.1.1]]; in a basis, a column $\psi \in \mathbb C^4$) transforms so.
>
> *Source: PS §3.2, eqs. (3.23), (3.30) · PHY 513 Lecture 7, Part B ("Finite Lorentz Transformations in Dirac Representation") · PHY 513 Lecture 8, Cheat Sheet II · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation $\Lambda_{1/2}$", eq. (Lhalf)) · Yu §5.1, eq. (5.14)*

^def-c5a-3-1

> [!definition] Definition §C5a.3.2: The Dirac Field
> A **Dirac field** is a four-component field that transforms as
>
> $$
> \psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)
> $$
>
> ([[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]), with $\Lambda_{1/2}$ the matrix of the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) for the parameters $\omega_{\mu\nu}$ of $\Lambda$: the matrix acts on the four components, $\Lambda^{-1}$ on the argument.
>
> *Source: PHY 513 Lecture 7, Part C (slide "Transformation of Vector and Spinor Fields", "Dirac 4-Spinor") · PHY 513 Lecture 8, Cheat Sheet II ("$\Lambda_{1/2}$ transforms field, $\Lambda^{-1}$ transforms spacetime coordinate") · PS §3.2, p. 42 (the law used after eq. (3.31)); §3.5, p. 60 · the general law: PS §3.1, eq. (3.8)*

^def-c5a-3-2

As a function of the group element $\Lambda = e^\omega$ rather than of $\omega$, $\Lambda_{1/2}$ is fixed only up to sign ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]). A quantum Dirac field is an operator-valued distribution; the law then holds after smearing, as for every field ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]]).

> [!theorem] Theorem §C5a.3.1: The Spinor Generators Obey the Lorentz Algebra, and the γ's Transform as a Vector
> For Dirac matrices ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]]), $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) and the vector generators $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$ ([[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-1|Def. §C1a.7.1]]):
> 1. $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\,\gamma^\nu = i\bigl(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho\bigr)$;
> 2. $[S^{\mu\nu}, S^{\rho\sigma}] = i\bigl(g^{\nu\rho}S^{\mu\sigma} - g^{\mu\rho}S^{\nu\sigma} - g^{\nu\sigma}S^{\mu\rho} + g^{\mu\sigma}S^{\nu\rho}\bigr)$, the Lorentz algebra ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]): the $S^{\mu\nu}$ generate a representation, the Dirac representation;
> 3. for $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ and $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ with the same $\omega_{\mu\nu}$: $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ and $\Lambda_{1/2}^{-1}S^{\mu\nu}\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma S^{\rho\sigma}$.
>
> How to read it: only the Clifford relation is used, so any set of Dirac matrices carries a spinor representation; sandwiching $\gamma^\mu$ between $\Lambda_{1/2}^{-1}$ and $\Lambda_{1/2}$ performs a vector Lorentz transformation on its index, so $\gamma^\mu\partial_\mu$ is invariant ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]) and each $\gamma$ between $\bar\psi$ and $\psi$ carries one vector index ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).
>
> *Proof:* [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-17|Theorem §CB.15.17]] (part 1), [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-18|Theorem §CB.15.18]] (part 2), [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-7|Theorem §CB.19.7]] (part 3).
>
> *Source: PS §3.2, p. 40, eq. (3.23) ("By repeated use of (3.22), it is easy to verify that these matrices satisfy the commutation relations (3.17)"), p. 42, eq. (3.29) · Yu §5.1, eqs. (5.11)–(5.12), (5.24)–(5.27), (5.31) · PHY 513, Problem Set 4, Problem 5(b)–(c) (as the user wrote them) · PHY 513 Lecture 7, Part B ("Claim: $S^{\mu\nu}$ satisfy Lorentz algebra"); Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$")*

^thm-c5a-3-1

> [!definition] Definition §C5a.3.3: Spin Matrices of the Dirac Representation
> The **spin matrices** of the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) are the $4\times4$ matrices
>
> $$
> S^i \equiv \tfrac12\varepsilon^{ijk}S^{jk}, \qquad i = 1, 2, 3, \qquad \mathbf S = (S^1, S^2, S^3), \qquad \Sigma^i \equiv 2S^i ,
> $$
>
> the rotation generators among the spinor generators $S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; they are the matrices $J_i$ of [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-2|Def. §C1a.7.2]] for this representation, named $\mathbf S$ so that $\hat{\mathbf J}$ stays the Hilbert-space angular momentum, as for the vector field, [[§C4.1 The Vector Field and Its Lorentz Transformation#^def-c4-1-1|Def. §C4.1.1]]). In the chiral basis $\Sigma^i = \operatorname{diag}(\sigma^i, \sigma^i)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]).
>
> *Source: PS §3.2, eq. (3.27) and §3.3, p. 45 · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis"), Ch. 9 §9.2 · Yu §5.2, eqs. (5.76)–(5.79)*

^def-c5a-3-3

> [!theorem] Theorem §C5a.3.2: The Generators in the Chiral Basis
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), with $\Sigma^k = \operatorname{diag}(\sigma^k, \sigma^k)$,
>
> $$
> S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k = \frac12\varepsilon^{ijk}\begin{pmatrix}\sigma^k&0\\0&\sigma^k\end{pmatrix}, \qquad S^{0i} = -\frac i2\begin{pmatrix}\sigma^i&0\\0&-\sigma^i\end{pmatrix}, \qquad S^{\mu\nu} = \frac i4\begin{pmatrix}\sigma^\mu\bar\sigma^\nu - \sigma^\nu\bar\sigma^\mu & 0\\0 & \bar\sigma^\mu\sigma^\nu - \bar\sigma^\nu\sigma^\mu\end{pmatrix} ,
> $$
>
> so the rotation and boost generators ([[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-2|Def. §C1a.7.2]]) are $\mathbf J = \frac12\boldsymbol\Sigma$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$. All six are block diagonal.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) · PHY 513 Lecture 7, Part B; Lecture 8, Cheat Sheet I · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis", eq. (Sexplicit)) · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-2

> [!derivation]- Derivation
> **1. General block form.** By Theorem §C5a.1.7, $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$; subtracting the same with $\mu \leftrightarrow \nu$ and multiplying by $\frac i4$ gives the third formula.
>
> **2. Rotations.** For spatial $i, j$: $\sigma^i\bar\sigma^j - \sigma^j\bar\sigma^i = -\sigma^i\sigma^j + \sigma^j\sigma^i = -[\sigma^i, \sigma^j] = -2i\varepsilon^{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 2), and the lower block $\bar\sigma^i\sigma^j - \bar\sigma^j\sigma^i = -[\sigma^i, \sigma^j]$ is the same. Times $\frac i4$: $\frac i4(-2i)\varepsilon^{ijk}\sigma^k = \frac12\varepsilon^{ijk}\sigma^k$ in both blocks.
>
> **3. Boosts.** Upper block of $S^{0i}$: $\sigma^0\bar\sigma^i - \sigma^i\bar\sigma^0 = -\sigma^i - \sigma^i = -2\sigma^i$, times $\frac i4$: $-\frac i2\sigma^i$. Lower block: $\bar\sigma^0\sigma^i - \bar\sigma^i\sigma^0 = \sigma^i + \sigma^i = 2\sigma^i$, times $\frac i4$: $+\frac i2\sigma^i = -\frac i2(-\sigma^i)$.
>
> **4. J and K.** By [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-2|Def. §C1a.7.2]], $J_k = \frac12\varepsilon_{kij}S^{ij} = \frac12\varepsilon_{kij}\cdot\frac12\varepsilon_{ijl}\Sigma^l = \frac14\cdot2\delta_{kl}\Sigma^l = \frac12\Sigma^k$, using $\varepsilon_{kij}\varepsilon_{lij} = 2\delta_{kl}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and $\varepsilon_{ijl} = \varepsilon_{lij}$; and $K_i = S^{0i}$.
>
> **What the derivation shows**
> - The rotation generators are spin ½ twice over, $\frac12\boldsymbol\sigma$ in each block; the boost generators are $\mp\frac i2\boldsymbol\sigma$, opposite in the two blocks: exactly the two rows of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]], stacked.
> - The factor $\frac12$ in $S^{ij}$ is what makes a $2\pi$ rotation $-1$ (Theorem §C5a.3.3, Theorem §C5a.4.3; [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]).

^der-c5a-3-2

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-2|Def. §C1a.7.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

> [!example] Example §C5a.3.1: The Six Spinor Generators as 4×4 Matrices
> Write the generators of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]] entry by entry in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]), as the rotation and boost generators $J_k = \frac12\varepsilon_{kij}S^{ij}$, $K_k = S^{0k}$ of [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^def-c1a-7-2|Def. §C1a.7.2]] (rows and columns are the four components of $\psi = (\psi_L, \psi_R)$).
>
> *Rotations*, $J_k = \frac12\Sigma^k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$, the spin matrices of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-3|Def. §C5a.3.3]]:
>
> $$
> J_1 = S^{23} = \frac12\begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&1\\ 0&0&1&0 \end{pmatrix}, \qquad J_2 = S^{31} = \frac12\begin{pmatrix} 0&-i&0&0\\ i&0&0&0\\ 0&0&0&-i\\ 0&0&i&0 \end{pmatrix}, \qquad J_3 = S^{12} = \frac12\begin{pmatrix} 1&0&0&0\\ 0&-1&0&0\\ 0&0&1&0\\ 0&0&0&-1 \end{pmatrix} .
> $$
>
> *Boosts*, $K_k = S^{0k} = -\frac i2\operatorname{diag}(\sigma^k, -\sigma^k)$:
>
> $$
> K_1 = S^{01} = -\frac i2\begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&-1&0 \end{pmatrix}, \qquad K_2 = S^{02} = \frac12\begin{pmatrix} 0&-1&0&0\\ 1&0&0&0\\ 0&0&0&1\\ 0&0&-1&0 \end{pmatrix}, \qquad K_3 = S^{03} = -\frac i2\begin{pmatrix} 1&0&0&0\\ 0&-1&0&0\\ 0&0&-1&0\\ 0&0&0&1 \end{pmatrix} .
> $$
>
> *Computation.* $J_1 = \frac12(\varepsilon_{123}S^{23} + \varepsilon_{132}S^{32}) = S^{23}$, likewise $J_2 = S^{31}$, $J_3 = S^{12}$; by Theorem §C5a.3.2, $S^{23} = \frac12\varepsilon^{231}\Sigma^1 = \frac12\Sigma^1$, $S^{31} = \frac12\Sigma^2$, $S^{12} = \frac12\Sigma^3$, and each $\sigma^k$ is placed twice on the diagonal. For the boosts, $-\frac i2\sigma^2 = -\frac i2\begin{pmatrix} 0&-i\\ i&0 \end{pmatrix} = \begin{pmatrix} 0&-\frac12\\ \frac12&0 \end{pmatrix}$ in the upper block and its negative in the lower block, which is why $K_2$ is real; $K_1$ and $K_3$ are $-\frac i2$ times real matrices. (All six checked numerically against $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$.)
>
> *Reading.* Each $J_k$ is Hermitian with eigenvalues $\frac12, \frac12, -\frac12, -\frac12$; each $K_k$ is anti-Hermitian with eigenvalues $\frac i2, \frac i2, -\frac i2, -\frac i2$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]]); e.g. $K_3$ has $-\frac i2$ on the components $1$, $4$ and $+\frac i2$ on $2$, $3$. The vector generators of [[§C1a.7 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-7-5|Theorem §C1a.7.5]] have $\pm1, 0, 0$ and $\pm i, 0, 0$: half of each here, no zero, and every $2\times2$ block is spin $\frac12$ ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]). All six are block diagonal, $J_k$ equal in the two blocks and $K_k$ opposite. Since $(2J_k)^2 = (2iK_k)^2 = \mathbb 1_4$, their exponentials split into $\cos\frac\theta2$, $\sin\frac\theta2$ and $\cosh\frac\eta2$, $\sinh\frac\eta2$: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]].
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) (the block form) · the user's PHY 513 notes, Ch. 8 §8.1, eq. (Sexplicit) · PHY 513 Lecture 8, Cheat Sheet I · the $4\times4$ entries written out here · PHY 513, Problem Set 6, Problem 4(a), (c) (the generators $S^{03}$, $S^{12}$ used there, as the user wrote them)*

^ex-c5a-3-1

## The Dirac representation is a spinor representation

> [!theorem] Theorem §C5a.3.3: The Dirac Representation Is (½, 0) ⊕ (0, ½)
> In the chiral basis $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-1|Def. §C3.2.1]]) are $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, $\mathbf J_- = \frac12\operatorname{diag}(0, \boldsymbol\sigma)$: the upper half is the representation $(\frac12, 0)$, the lower $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]). The Dirac representation is a spinor representation ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]): a rotation by $2\pi$ acts as $-\mathbb 1_4$. Hence it is not the vector representation $(\frac12, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9|Theorem §C3.2.9]]), although both are four-dimensional: the Casimirs $\mathbf J_\pm^2$, the $2\pi$ rotation ($-\mathbb 1$ against $+\mathbb 1$) and the rotation content ($\frac12\oplus\frac12$ against $0\oplus1$) all differ ([[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-5|Theorem §CB.19.5]]).
>
> *Model:* none (a representation fact); *applies:* as in the opening, any Dirac spinor or spinor field, independent of the dynamics.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27), (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts": "4 dim. Dirac spinor representation is reducible") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivations "How the two halves transform", "… related by conjugation": "Their labels") · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-3

> [!derivation]- Derivation
> **1. The labels.** From Theorem §C5a.3.2, $\mathbf J = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, so $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K) = \frac12\bigl(\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm i(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr) = \frac14\bigl(\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm \operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr)$, using $i\cdot(-\frac i2) = \frac12$. The upper sign gives $\frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, the lower $\frac12\operatorname{diag}(0, \boldsymbol\sigma)$.
>
> **2. Each block is one of the two representations.** On the upper block $\mathbf J_+ = \frac12\boldsymbol\sigma$ (spin $\frac12$) and $\mathbf J_- = 0$ (spin $0$): by [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]] with $j_+ = \frac12$, $j_- = 0$ this is $(\frac12, 0)$, and indeed $\mathbf J = \frac12\boldsymbol\sigma$, $\mathbf K = -\frac i2\boldsymbol\sigma$ there, the first row of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]]. On the lower block $\mathbf J_+ = 0$, $\mathbf J_- = \frac12\boldsymbol\sigma$, $\mathbf K = +\frac i2\boldsymbol\sigma$: $(0, \frac12)$, the second row. Both blocks are invariant, since every generator is block diagonal (Theorem §C5a.3.2).
>
> **3. Spinor representation.** On each block $j_+ + j_- = \frac12$, so a $2\pi$ rotation is $(-1)^{2\cdot\frac12} = -1$ there ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]], 2). Directly: $e^{-2\pi iJ_3} = \operatorname{diag}(e^{-i\pi\sigma^3}, e^{-i\pi\sigma^3}) = \operatorname{diag}(-\mathbb 1, -\mathbb 1)$, since $e^{-i\pi\sigma^3} = \operatorname{diag}(e^{-i\pi}, e^{i\pi})$.
>
> **What the derivation shows**
> - $\mathbf J_+$ acts only on the upper two components and $\mathbf J_-$ only on the lower two: the Dirac spinor is a direct sum, $2 + 2$, of the two smallest spinor representations, read off from $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ in one basis. In every basis the halves are the eigenspaces of $\gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]).
> - Each half is irreducible and the two are inequivalent ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-4|Theorem §C3.2.4]]; the user's notes argue directly: an intertwiner commutes with $\frac12\boldsymbol\sigma$, so is $c\mathbb 1$ by Schur, and cannot turn $-\frac i2\boldsymbol\sigma$ into $+\frac i2\boldsymbol\sigma$); they are complex conjugates of each other up to basis ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]]).
> - Used next: the finite matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]).

^der-c5a-3-3

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-8|Theorem §C3.2.8]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]

> [!remark] Remark: Why half the angle
> The rotation generator $\mathcal J^{12}$ of the vector representation has eigenvalues $\pm1$ (on $x \pm iy$) and $0$ twice (on $t$, $z$); the spinor generator $S^{12} = \frac12\Sigma^3$ has $\pm\frac12$. For boosts, $\mathcal J^{01}$ has $\pm i$ and $S^{01}$ has $\pm\frac i2$. Exponentiating $\theta$ times an eigenvalue $s$ gives the phase $e^{-is\theta}$: spin $1$ turns with the full angle, spin $\frac12$ with half of it, and the $2\pi$ sign is $e^{-i\pi} = -1$. The factor $\frac12$ in $S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k$ is therefore essential; the user's notes record that the handwritten lecture notes omit it, while the Lecture 8 slides have it. The six generators as $4\times4$ matrices: [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]; next to the vector generators, with the matrices they exponentiate to: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]] (rotation), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]] (boost).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Why 'half'"), Caution "A missing ½ in the handwritten notes" · PHY 513 Lecture 8, Cheat Sheet I*

^rem-c5a-3-1

## Why ψ†ψ is not invariant

> [!theorem] Theorem §C5a.3.4: Λ½ Is Pseudo-Unitary, γ⁰Λ½†γ⁰ = Λ½⁻¹
> In a Hermitian basis, $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ (the chiral one: [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]):
> 1. $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$: the rotation generators $S^{ij}$ commute with $\gamma^0$ and are Hermitian, the boost generators $S^{0i}$ anticommute with $\gamma^0$ and are anti-Hermitian;
> 2. for every real $\omega_{\mu\nu}$, $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$, equivalently $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$: $\Lambda_{1/2}$ preserves the Dirac form ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]); it is unitary for rotations and Hermitian positive, not unitary, for pure boosts.
>
> How to read it: $\psi^\dagger\psi$ changes under boosts, but $\bar\psi = \psi^\dagger\gamma^0$ transforms with $\Lambda_{1/2}^{-1}$, so $\bar\psi\chi$ is a scalar ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); $\gamma^0$ plays for spinors the role $g$ plays for vectors, the spin-½ face of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-7|Theorem §C3.2.7]].
>
> *Proof:* [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-22|Theorem §CB.15.22]] (part 1 and the rotation/boost split), [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-13|Theorem §CB.19.13]] (part 2).
>
> *Source: PS §3.2, p. 41 ("The boost generators $S^{0i}$ are not Hermitian"), p. 43, eqs. (3.32)–(3.33) · Yu §5.3, eqs. (5.83)–(5.89) · the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary); Derivation "What replaces unitarity"), §8.7 · PHY 513 Lecture 8, Part B ("The Dirac Conjugate Spinor")*

^thm-c5a-3-4

> [!remark] Remark: Spinor boosts are not unitary
> By [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], $\Lambda_{1/2}$ is unitary for rotations and Hermitian positive, not unitary, for pure boosts; in the chiral basis this is visible in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]: $\frac12\Sigma^k$ is Hermitian, $-\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$ anti-Hermitian. So $\psi^\dagger\psi$ is not invariant under boosts. What replaces unitarity is that $\gamma^0$ turns the adjoint into the inverse, $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$, so $\bar\psi = \psi^\dagger\gamma^0$ transforms with $\Lambda_{1/2}^{-1}$: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]. That is the price of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-7|Theorem §C3.2.7]] for spin ½; since $\psi$ is not a wavefunction but a classical field (PS p. 41), non-unitarity is harmless.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "What replaces unitarity"; Caution "Spinor boosts are not unitary") · PHY 513 Lecture 8, Part B · PS §3.2, p. 41*

^rem-c5a-3-2

> [!remark] Remark: What the calculations use
> - The generators in the chiral basis, $\mathbf J = \frac12\boldsymbol\Sigma$, $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, and $\sigma^{\mu\nu} = 2S^{\mu\nu}$ in bilinears: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]].
> - The finite matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$, with half angles and half rapidities: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]].
> - $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$ and its finite form $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$, for the covariance of the Dirac equation: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]].
> - $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$, for the transformation of $\bar\psi$: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]].
>
> *Source: summary written here*

^rem-c5a-3-3

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> Every field law has six generators obeying the Lorentz algebra; the spinor generators below are generators in this sense, and Theorem §CB.15.18 checks the Lorentz algebra for them:
> - [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]] — generators of a representation ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-1|Def. §C3.2.1]]).
> - [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-7|Theorem §CB.5.7]] with [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-7|Derivation (from the group law)]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-7b|Derivation (vector representation, Problem Set 4)]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-7c|Derivation (J, K form, Problem Set 5)]] — the Lorentz algebra in every representation ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]).
>
> The six matrices built from the Dirac matrices alone (Lecture 7, Part B), the lemma that the $\gamma$'s rotate as a vector (Problem Set 4, Problem 5(b), used again for the covariance of the Dirac equation), and the Lorentz algebra they obey (Problem Set 4, Problem 5(c)):
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-16|Def. §CB.15.16]] — the spinor generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Def. §C5a.3.1).
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-17|Theorem §CB.15.17]] with [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-15-17|Derivation]] — $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$: the $\gamma$'s rotate as a vector; physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]].
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-18|Theorem §CB.15.18]] with [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-15-18|Derivation]] — the $S^{\mu\nu}$ obey the Lorentz algebra (Def. §C5a.3.1); physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]].
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-7|Theorem §CB.19.7]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-7|Derivation]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-7b|Derivation (second route: the nested-commutator series)]] — $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$, the finite form of the same statement (the proof of Theorem §C5a.3.1, part 3).
>
> Their exponentials, the matrices of the Dirac representation below:
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-19|Def. §CB.15.19]] — $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ for Dirac matrices of any size (Def. §C5a.3.1 with $n = 4$).
>
> The classification of finite-dimensional representations ([[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.18]]) provides the spinor/tensor dichotomy and the meaning of the labels:
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-26|Def. §CB.15.26]], [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-11|Theorem §CB.18.11]] with [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-18-11|Derivation]] — spinor and tensor representations by the sign of the $2\pi$ rotation ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]]).
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-18-3|§CB.18, Remark: What the labels (j₊, j₋) mean]] — the physical reading of the labels (§C3.2, Remark: Reading a field's labels).
>
> Theorem §C5a.3.3 identifies the two halves by the labels $(j_+, j_-)$ and their irreducibility:
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-18-3|Def. §CB.18.3]] — the representation $(j_+, j_-)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^def-c3-2-2|Def. §C3.2.2]]).
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-5|Theorem §CB.18.5]] with [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-18-5|Derivation]] — irreducible, read off by the Casimirs ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-4|Theorem §C3.2.4]]).
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-5|Theorem §CB.19.5]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-5|Derivation]] — the Dirac representation is not the vector representation: Casimirs, $2\pi$ sign and rotation content differ (Theorem §C5a.3.3, with [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9|Theorem §C3.2.9]]).
>
> The same split without a basis: the Dirac module restricted to $SL(2, \mathbb C)$, and $\gamma^5$ commuting with the generators and splitting the module ($K_i = i\gamma^5J_i$):
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-3|Theorem §CB.19.3]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-19-3|Proof]] — the Dirac module restricted to $SL(2, \mathbb C)$ is $(\frac12, 0)\oplus(0, \frac12)$ (Theorem §C5a.3.3).
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-4|Theorem §CB.19.4]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-19-4|Proof]] — $\gamma^5$ commutes with $S^{\mu\nu}$ and its eigenspaces are the two halves in every basis ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]).
>
> The remark "Spinor boosts are not unitary" rests on the adjoints of the generators in a Hermitian basis, the spin-½ case of the non-unitarity of finite-dimensional Lorentz representations, and what replaces unitarity:
> - [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-15-22|Theorem §CB.15.22]] with [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-15-22|Derivation]] — $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$; $\Lambda_{1/2}$ unitary for rotations, Hermitian positive for boosts; physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]].
> - [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-18-15|Theorem §CB.18.15]] with [[§CB.18 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-18-15|Derivation]] — no nontrivial finite-dimensional Lorentz representation is unitary ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-7|Theorem §C3.2.7]]).
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-13|Theorem §CB.19.13]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-13|Derivation]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-13b|Derivation (second route)]] — $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$, so $\bar\psi$ transforms with $\Lambda_{1/2}^{-1}$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); physics form: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]].

> [!remark]- Connections
> - Why the $\gamma$'s generate Lorentz transformations at all — the Clifford algebra is a "square root of the metric", and in every dimension and signature $\frac i4[\gamma, \gamma]$ represents the orthogonal algebra — is mathematics and lives with its proofs in [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.15]].
> - The non-unitarity of spinor boosts is the spin-½ instance of the theorem that no nontrivial finite-dimensional Lorentz representation is unitary; $\gamma^0$ restores an invariant form as $g$ does for vectors — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-7|Theorem §C3.2.7]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-13|Theorem §CB.19.13]].
> - The $-1$ of a $2\pi$ rotation on $\Lambda_{1/2}$ is the sign the spin–statistics theorem ties to anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]] (the measured sign).
> - The spinor representation of §CB.15 is defined by one group element, the $2\pi$ rotation; the Dirac representation realizes the smallest parity-symmetric instance, $(\frac12, 0)\oplus(0, \frac12)$, from the $\gamma$'s — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-5|Theorem §C3.2.5]] (definition: [[§CB.15 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-15-26|Def. §CB.15.26]]), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-10|Theorem §C3.2.10]].
> - The spinor generators are the $D(\mathcal J^{\mu\nu})$ of the Dirac field's transformation law ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), and the orbital part adds to them in the total angular momentum — [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]], [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-8|Theorem §C5a.9.8]].
