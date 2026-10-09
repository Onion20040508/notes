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

How does the Lorentz group act on spinor space? Nothing in layers 1–3 ([[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]], [[§C5a.2 The Dirac Form|§C5a.2]]) mentions it: $V$ has bases, the Clifford action $\Gamma^\mu$ and the Dirac form. This section adds **layer 4**, the action of the Lorentz *algebra* ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-2|Theorem §CB.4.2]]): from the $\gamma$'s alone one builds six generators $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, proves that they obey the Lorentz algebra *because of* the Clifford algebra, exponentiates them to $\Lambda_{1/2}$, and identifies the result with the classification of §CB.16: a **spinor representation** ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-25|Def. §CB.13.25]]), namely $(\frac12, 0)\oplus(0, \frac12)$. The algebra behind it — the generators of a Clifford module, the Lorentz algebra they obey, their exponentials and adjoints, and the classification of finite-dimensional representations — is mathematics ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations|§CB.4]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]–[[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]), shown in the blocks below; this section keeps the Dirac representation and field law, the generators in the chiral basis, and what they mean physically. The group-level structure ($SL(2, \mathbb C)$, the finite matrices, $\gamma^\mu$ as an invariant tensor) is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]; the chirality grading that separates the two halves in every basis is [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]].

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; chiral basis; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Hermitian convention, the $D(\mathcal J^{\mu\nu})$ of §C3.2; [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-2|§C3.3, Caution: Two meanings of S^μν]]); $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ with the same $\omega_{\mu\nu}$ as $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$, $K_i = \mathcal J^{0i}$; $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$.

## The mathematics used here

Every field law has six generators obeying the Lorentz algebra; the spinor generators below are generators in this sense, and Theorem §CB.13.17 checks the Lorentz algebra for them:

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-2]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-2]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-2b]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-2c]]

The six matrices built from the Dirac matrices alone (Lecture 7, Part B), the lemma that the $\gamma$'s rotate as a vector (Problem Set 4, Problem 5(b), used again for the covariance of the Dirac equation), and the Lorentz algebra they obey (Problem Set 4, Problem 5(c)):

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-16]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-16]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-17]]

Their exponentials, the matrices of the Dirac representation below:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18]]

## The Dirac representation

> [!definition] Definition §C5a.3.1: The Dirac Representation
> The **Dirac representation** is the representation of the Lorentz algebra on $\mathbb C^4$ whose generators ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]]) are $D(\mathcal J^{\mu\nu}) = S^{\mu\nu}$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15|Def. §CB.13.15]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17|Theorem §CB.13.17]]). For parameters $\omega_{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]),
>
> $$
> \Lambda_{1/2}(\omega) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}S^{\mu\nu}\Bigr), \qquad \psi \to \Lambda_{1/2}\,\psi ,
> $$
>
> ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18|Def. §CB.13.18]] with $n = 4$), and a **Dirac spinor** is a column $\psi \in \mathbb C^4$ transforming so. A **Dirac field** transforms as $\psi'(x) = \Lambda_{1/2}\,\psi(\Lambda^{-1}x)$ ([[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]).
>
> *Source: PS §3.2, eq. (3.30) · PHY 513 Lecture 7, Part B ("Finite Lorentz Transformations in Dirac Representation"), Part C ("Dirac 4-Spinor") · PHY 513 Lecture 8, Cheat Sheet II · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation $\Lambda_{1/2}$", eq. (Lhalf)) · Yu §5.1, eq. (5.14)*

^def-c5a-3-1

As a function of the group element $\Lambda = e^\omega$ rather than of $\omega$, $\Lambda_{1/2}$ is fixed only up to sign ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]). A quantum Dirac field is an operator-valued distribution; the law then holds after smearing, as for every field ([[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-2|§C3.3, Remark: The laws for fields that are distributions]]).

> [!definition] Definition §C5a.3.2: Spin Matrices of the Dirac Representation
> The **spin matrices** of the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) are the $4\times4$ matrices
>
> $$
> S^i \equiv \tfrac12\varepsilon^{ijk}S^{jk}, \qquad i = 1, 2, 3, \qquad \mathbf S = (S^1, S^2, S^3), \qquad \Sigma^i \equiv 2S^i ,
> $$
>
> the rotation generators among the spinor generators $S^{\mu\nu}$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15|Def. §CB.13.15]]; they are the matrices $J_i$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] for this representation, named $\mathbf S$ so that $\hat{\mathbf J}$ stays the Hilbert-space angular momentum, as for the vector field, [[§C4.1 The Vector Field and Its Lorentz Transformation#^def-c4-1-1|Def. §C4.1.1]]). In the chiral basis $\Sigma^i = \operatorname{diag}(\sigma^i, \sigma^i)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]).
>
> *Source: PS §3.2, eq. (3.27) and §3.3, p. 45 · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis"), Ch. 9 §9.2 · Yu §5.2, eqs. (5.76)–(5.79)*

^def-c5a-3-2

> [!theorem] Theorem §C5a.3.1: The Generators in the Chiral Basis
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), with $\Sigma^k = \operatorname{diag}(\sigma^k, \sigma^k)$,
>
> $$
> S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k = \frac12\varepsilon^{ijk}\begin{pmatrix}\sigma^k&0\\0&\sigma^k\end{pmatrix}, \qquad S^{0i} = -\frac i2\begin{pmatrix}\sigma^i&0\\0&-\sigma^i\end{pmatrix}, \qquad S^{\mu\nu} = \frac i4\begin{pmatrix}\sigma^\mu\bar\sigma^\nu - \sigma^\nu\bar\sigma^\mu & 0\\0 & \bar\sigma^\mu\sigma^\nu - \bar\sigma^\nu\sigma^\mu\end{pmatrix} ,
> $$
>
> so the rotation and boost generators ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]) are $\mathbf J = \frac12\boldsymbol\Sigma$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$. All six are block diagonal.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) · PHY 513 Lecture 7, Part B; Lecture 8, Cheat Sheet I · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The generators in the chiral basis", eq. (Sexplicit)) · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-1

> [!derivation]- Derivation
> **1. General block form.** By Theorem §C5a.1.2, $\gamma^\mu\gamma^\nu = \operatorname{diag}(\sigma^\mu\bar\sigma^\nu, \bar\sigma^\mu\sigma^\nu)$; subtracting the same with $\mu \leftrightarrow \nu$ and multiplying by $\frac i4$ gives the third formula.
>
> **2. Rotations.** For spatial $i, j$: $\sigma^i\bar\sigma^j - \sigma^j\bar\sigma^i = -\sigma^i\sigma^j + \sigma^j\sigma^i = -[\sigma^i, \sigma^j] = -2i\varepsilon^{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 2), and the lower block $\bar\sigma^i\sigma^j - \bar\sigma^j\sigma^i = -[\sigma^i, \sigma^j]$ is the same. Times $\frac i4$: $\frac i4(-2i)\varepsilon^{ijk}\sigma^k = \frac12\varepsilon^{ijk}\sigma^k$ in both blocks.
>
> **3. Boosts.** Upper block of $S^{0i}$: $\sigma^0\bar\sigma^i - \sigma^i\bar\sigma^0 = -\sigma^i - \sigma^i = -2\sigma^i$, times $\frac i4$: $-\frac i2\sigma^i$. Lower block: $\bar\sigma^0\sigma^i - \bar\sigma^i\sigma^0 = \sigma^i + \sigma^i = 2\sigma^i$, times $\frac i4$: $+\frac i2\sigma^i = -\frac i2(-\sigma^i)$.
>
> **4. J and K.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], $J_k = \frac12\varepsilon_{kij}S^{ij} = \frac12\varepsilon_{kij}\cdot\frac12\varepsilon_{ijl}\Sigma^l = \frac14\cdot2\delta_{kl}\Sigma^l = \frac12\Sigma^k$, using $\varepsilon_{kij}\varepsilon_{lij} = 2\delta_{kl}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and $\varepsilon_{ijl} = \varepsilon_{lij}$; and $K_i = S^{0i}$.
>
> **What the derivation shows**
> - The rotation generators are spin ½ twice over, $\frac12\boldsymbol\sigma$ in each block; the boost generators are $\mp\frac i2\boldsymbol\sigma$, opposite in the two blocks: exactly the two rows of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]], stacked.
> - The factor $\frac12$ in $S^{ij}$ is what makes a $2\pi$ rotation $-1$ (Theorem §C5a.3.2, Theorem §C5a.4.3; [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]).

^der-c5a-3-1

*Uses:* [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-15|Def. §CB.13.15]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

> [!example] Example §C5a.3.1: The Six Spinor Generators as 4×4 Matrices
> Write the generators of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]] entry by entry in the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), as the rotation and boost generators $J_k = \frac12\varepsilon_{kij}S^{ij}$, $K_k = S^{0k}$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] (rows and columns are the four components of $\psi = (\psi_L, \psi_R)$).
>
> *Rotations*, $J_k = \frac12\Sigma^k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$, the spin matrices of [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]:
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
> *Computation.* $J_1 = \frac12(\varepsilon_{123}S^{23} + \varepsilon_{132}S^{32}) = S^{23}$, likewise $J_2 = S^{31}$, $J_3 = S^{12}$; by Theorem §C5a.3.1, $S^{23} = \frac12\varepsilon^{231}\Sigma^1 = \frac12\Sigma^1$, $S^{31} = \frac12\Sigma^2$, $S^{12} = \frac12\Sigma^3$, and each $\sigma^k$ is placed twice on the diagonal. For the boosts, $-\frac i2\sigma^2 = -\frac i2\begin{pmatrix} 0&-i\\ i&0 \end{pmatrix} = \begin{pmatrix} 0&-\frac12\\ \frac12&0 \end{pmatrix}$ in the upper block and its negative in the lower block, which is why $K_2$ is real; $K_1$ and $K_3$ are $-\frac i2$ times real matrices. (All six checked numerically against $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$.)
>
> *Reading.* Each $J_k$ is Hermitian with eigenvalues $\frac12, \frac12, -\frac12, -\frac12$; each $K_k$ is anti-Hermitian with eigenvalues $\frac i2, \frac i2, -\frac i2, -\frac i2$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]]); e.g. $K_3$ has $-\frac i2$ on the components $1$, $4$ and $+\frac i2$ on $2$, $3$. The vector generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] have $\pm1, 0, 0$ and $\pm i, 0, 0$: half of each here, no zero, and every $2\times2$ block is spin $\frac12$ ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]). All six are block diagonal, $J_k$ equal in the two blocks and $K_k$ opposite. Since $(2J_k)^2 = (2iK_k)^2 = \mathbb 1_4$, their exponentials split into $\cos\frac\theta2$, $\sin\frac\theta2$ and $\cosh\frac\eta2$, $\sinh\frac\eta2$: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]].
>
> *Source: PS §3.2, eqs. (3.26)–(3.27) (the block form) · the user's PHY 513 notes, Ch. 8 §8.1, eq. (Sexplicit) · PHY 513 Lecture 8, Cheat Sheet I · the $4\times4$ entries written out here · PHY 513, Problem Set 6, Problem 4(a), (c) (the generators $S^{03}$, $S^{12}$ used there, as the user wrote them)*

^ex-c5a-3-1

### The mathematics used here: the two Weyl halves

The classification of finite-dimensional representations ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]) provides the spinor/tensor dichotomy and the meaning of the labels:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-25]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-8]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-16-2]]

Theorem §C5a.3.2 identifies the two halves by the labels $(j_+, j_-)$ and their irreducibility:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-3]]

The same split without a basis: the Dirac module restricted to $SL(2, \mathbb C)$, and $\gamma^5$ commuting with the generators and splitting the module ($K_i = i\gamma^5J_i$):

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-3]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-3]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-4]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-17-4]]

## The Dirac representation is a spinor representation

> [!theorem] Theorem §C5a.3.2: The Dirac Representation Is (½, 0) ⊕ (0, ½)
> In the chiral basis $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-4-1|Def. §CB.4.1]]) are $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, $\mathbf J_- = \frac12\operatorname{diag}(0, \boldsymbol\sigma)$: the upper half is the representation $(\frac12, 0)$, the lower $(0, \frac12)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]). The Dirac representation is a spinor representation ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-25|Def. §CB.13.25]]): a rotation by $2\pi$ acts as $-\mathbb 1_4$.
>
> *Source: PS §3.2, eqs. (3.26)–(3.27), (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts": "4 dim. Dirac spinor representation is reducible") · the user's PHY 513 notes, Ch. 8 §8.2 (Derivations "How the two halves transform", "… related by conjugation": "Their labels") · Yu §5.2, eqs. (5.76)–(5.79)*

^thm-c5a-3-2

> [!derivation]- Derivation
> **1. The labels.** From Theorem §C5a.3.1, $\mathbf J = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$ and $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, so $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K) = \frac12\bigl(\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm i(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr) = \frac14\bigl(\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) \pm \operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)\bigr)$, using $i\cdot(-\frac i2) = \frac12$. The upper sign gives $\frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, the lower $\frac12\operatorname{diag}(0, \boldsymbol\sigma)$.
>
> **2. Each block is one of the two representations.** On the upper block $\mathbf J_+ = \frac12\boldsymbol\sigma$ (spin $\frac12$) and $\mathbf J_- = 0$ (spin $0$): by [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]] with $j_+ = \frac12$, $j_- = 0$ this is $(\frac12, 0)$, and indeed $\mathbf J = \frac12\boldsymbol\sigma$, $\mathbf K = -\frac i2\boldsymbol\sigma$ there, the first row of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]. On the lower block $\mathbf J_+ = 0$, $\mathbf J_- = \frac12\boldsymbol\sigma$, $\mathbf K = +\frac i2\boldsymbol\sigma$: $(0, \frac12)$, the second row. Both blocks are invariant, since every generator is block diagonal (Theorem §C5a.3.1).
>
> **3. Spinor representation.** On each block $j_+ + j_- = \frac12$, so a $2\pi$ rotation is $(-1)^{2\cdot\frac12} = -1$ there ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]], 1). Directly: $e^{-2\pi iJ_3} = \operatorname{diag}(e^{-i\pi\sigma^3}, e^{-i\pi\sigma^3}) = \operatorname{diag}(-\mathbb 1, -\mathbb 1)$, since $e^{-i\pi\sigma^3} = \operatorname{diag}(e^{-i\pi}, e^{i\pi})$.
>
> **What the derivation shows**
> - $\mathbf J_+$ acts only on the upper two components and $\mathbf J_-$ only on the lower two: the Dirac spinor is a direct sum, $2 + 2$, of the two smallest spinor representations, read off from $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ in one basis. In every basis the halves are the eigenspaces of $\gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).
> - Each half is irreducible and the two are inequivalent ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-3|Theorem §CB.16.3]]; the user's notes argue directly: an intertwiner commutes with $\frac12\boldsymbol\sigma$, so is $c\mathbb 1$ by Schur, and cannot turn $-\frac i2\boldsymbol\sigma$ into $+\frac i2\boldsymbol\sigma$); they are complex conjugates of each other up to basis ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-4|Theorem §C5a.5.4]]).
> - Used next: the finite matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]).

^der-c5a-3-2

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]

> [!remark] Remark: Why half the angle
> The rotation generator $\mathcal J^{12}$ of the vector representation has eigenvalues $\pm1$ (on $x \pm iy$) and $0$ twice (on $t$, $z$); the spinor generator $S^{12} = \frac12\Sigma^3$ has $\pm\frac12$. For boosts, $\mathcal J^{01}$ has $\pm i$ and $S^{01}$ has $\pm\frac i2$. Exponentiating $\theta$ times an eigenvalue $s$ gives the phase $e^{-is\theta}$: spin $1$ turns with the full angle, spin $\frac12$ with half of it, and the $2\pi$ sign is $e^{-i\pi} = -1$. The factor $\frac12$ in $S^{ij} = \frac12\varepsilon^{ijk}\Sigma^k$ is therefore essential; the user's notes record that the handwritten lecture notes omit it, while the Lecture 8 slides have it. The six generators as $4\times4$ matrices: [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]; next to the vector generators, with the matrices they exponentiate to: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]] (rotation), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]] (boost).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Why 'half'"), Caution "A missing ½ in the handwritten notes" · PHY 513 Lecture 8, Cheat Sheet I*

^rem-c5a-3-1

### The mathematics used here: adjoints

The remark "Spinor boosts are not unitary" rests on the adjoints of the generators in a Hermitian basis, the spin-½ case of the non-unitarity of finite-dimensional Lorentz representations, and what replaces unitarity:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-21]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-12]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-13b]]

## Why ψ†ψ is not invariant

> [!remark] Remark: Spinor boosts are not unitary
> By [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]], $\Lambda_{1/2}$ is unitary for rotations and Hermitian positive, not unitary, for pure boosts; in the chiral basis this is visible in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]: $\frac12\Sigma^k$ is Hermitian, $-\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$ anti-Hermitian. So $\psi^\dagger\psi$ is not invariant under boosts. What replaces unitarity is that $\gamma^0$ turns the adjoint into the inverse, $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$, so $\bar\psi = \psi^\dagger\gamma^0$ transforms with $\Lambda_{1/2}^{-1}$: [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]. That is the price of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]] for spin ½; the lecture: "$\psi$ is not a wavefunction; it is a classical field" (PS p. 41), so non-unitarity is harmless.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "What replaces unitarity"; Caution "Spinor boosts are not unitary") · PHY 513 Lecture 8, Part B · PS §3.2, p. 41*

^rem-c5a-3-2

> [!remark] Remark: What the calculations use
> - The generators in the chiral basis, $\mathbf J = \frac12\boldsymbol\Sigma$, $\mathbf K = -\frac i2\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma)$, and $\sigma^{\mu\nu} = 2S^{\mu\nu}$ in bilinears: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]].
> - The finite matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$, with half angles and half rapidities: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]].
> - $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu$ and its finite form $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$, for the covariance of the Dirac equation: [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-16|Theorem §CB.13.16]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]].
> - $S^{\mu\nu\dagger} = \gamma^0S^{\mu\nu}\gamma^0$, for the transformation of $\bar\psi$: [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]].
>
> *Source: summary written here (the option-1 demo, 2026-10-08)*

^rem-c5a-3-3

> [!remark]- Connections
> - Why the $\gamma$'s generate Lorentz transformations at all — the Clifford algebra is a "square root of the metric", and in every dimension and signature $\frac i4[\gamma, \gamma]$ represents the orthogonal algebra — is mathematics and lives with its proofs in [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]].
> - The non-unitarity of spinor boosts is the spin-½ instance of the theorem that no nontrivial finite-dimensional Lorentz representation is unitary; $\gamma^0$ restores an invariant form as $g$ does for vectors — [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-12|Theorem §CB.16.12]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13|Theorem §CB.17.13]].
> - The $-1$ of a $2\pi$ rotation on $\Lambda_{1/2}$ is the sign the spin–statistics theorem ties to anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-4|QM Theorem §C5.2.4]] (the measured sign).
> - The spinor representation of §CB.13 is defined by one group element, the $2\pi$ rotation; the Dirac representation realizes the smallest parity-symmetric instance, $(\frac12, 0)\oplus(0, \frac12)$, from the $\gamma$'s — [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-25|Def. §CB.13.25]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]].
> - The spinor generators are the $D(\mathcal J^{\mu\nu})$ of the Dirac field's transformation law, and the orbital part adds to them in the total angular momentum — [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-8|Theorem §C5a.8.8]].
