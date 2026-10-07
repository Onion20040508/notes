---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.3 The Lorentz Action on Spinor Space]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.5 Chirality and Weyl Spinors]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation": "One transformation, two representations"; Derivation "The covariance of $\gamma^\mu$: finite transformations"), §8.2 (Weyl spinors: Derivations "How the two halves transform", "The double cover made explicit", "The left-handed Weyl matrices are this covering"), §8.3 (Principle "Invariant tensors with mixed slots"), Ch. 10 §10.3 · PHY 513 Lecture 7 (Larsen), Part B · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$", "Interpretation") and Part C · Peskin & Schroeder, §3.2, pp. 42–44, eqs. (3.29), (3.36)–(3.42), §3.5, eqs. (3.108)–(3.110) · Yu Zhao-Huan, 量子场论讲义, Exercise 3.7, eqs. (3.259)–(3.268), §5.1, eqs. (5.17)–(5.31), §5.2, eqs. (5.55)–(5.61), (5.74) · the user's pre-course notes, §5.1, §5.2 (Remark "SL(2,C) made explicit"; Note "Four linear spaces tied to Lorentz transformations") · for the matrices entry by entry: PS §3.3, eqs. (3.48)–(3.49); PHY 513 Lecture 9, Part A; the user's PHY 513 notes, Ch. 9 §9.3; Sakurai §3.2.5, as in QM §C5.2.*

Which *group* acts on spinor space, and how do the $\gamma$ matrices behave under it? [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] gave the action of the Lorentz algebra (layer 4) and found two halves, $(\frac12, 0)$ and $(0, \frac12)$, on which [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]] gives $2\times2$ matrices at a complex angle, defined only up to sign on $SO^+(1,3)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]]); the rotation case, $SU(2) \to SO(3)$, is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]] and [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]. This section adds **layer 5**, the group: the Weyl matrices $\Lambda_L$, $\Lambda_R$, the group $SL(2, \mathbb C)$ they form, four-vectors as $2\times2$ Hermitian matrices, the covering map $SL(2, \mathbb C) \to SO^+(1,3)$ with kernel $\pm\mathbb 1$, and the integration of every $(j_+, j_-)$ (the integer ones to $SO^+(1,3)$ itself). On $V$ the group acts by $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$, and the $\gamma$'s acquire their last structure: a Minkowski index, which makes $\gamma^\mu$ an invariant tensor — fixed by a Lorentz transformation, though not by a change of basis of $V$. Three different transformations that act on spinor indices are kept apart at the end.

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; active reading; $\Lambda = e^{\omega} = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $(\omega)^\mu{}_\nu = \omega^\mu{}_\nu$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ (so $\omega_{ij} = \varepsilon_{ijk}\theta_k$), $\eta_i = \omega_{0i}$; $K_i = \mathcal J^{0i}$, so that $(\frac12, 0)$ is Peskin–Schroeder's $\psi_L$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]]). Pauli matrices with the product rule of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]].

## The Weyl matrices and SL(2, C)

> [!definition] Definition §C5a.4.1: The Weyl Matrices
> For Lorentz parameters $\omega_{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]), with angles $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and rapidities $\eta_i = \omega_{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), the **left- and right-handed Weyl matrices** $\Lambda_L$, $\Lambda_R$ are the matrices of the representations $(\frac12, 0)$ and $(0, \frac12)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]]; the representation $(j_+, j_-)$: [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]), with $\mathbf J = \frac12\boldsymbol\sigma$ and $\mathbf K = -\frac i2\boldsymbol\sigma$ for $\Lambda_L$, $\mathbf K = +\frac i2\boldsymbol\sigma$ for $\Lambda_R$ (with $K_i = \mathcal J^{0i}$; the opposite sign of $\mathbf K$ exchanges the two, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|Caution: Which one is (½, 0) depends on the sign of K]]):
>
> $$
> \Lambda_L(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\boldsymbol\sigma/2}, \qquad \Lambda_R(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\boldsymbol\sigma/2} .
> $$
>
> *Source: PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$, $\psi_R \to e^{-i\vec\theta\cdot\vec\sigma/2 + \vec\eta\cdot\vec\sigma/2}\psi_R$") · PS §3.2, eqs. (3.36)–(3.37) · the user's PHY 513 notes, Ch. 8 §8.2 ($U_L$, $U_R$, eq. (weyllaws)) · Yu Exercise 3.7(c)*

^def-c5a-4-1

> [!definition] Definition §C5a.4.2: Weyl Spinors
> A **left-handed** (**right-handed**) **Weyl spinor** is a column $\psi_L \in \mathbb C^2$ ($\psi_R$) transforming as $\psi_L \to \Lambda_L\psi_L$ ($\psi_R \to \Lambda_R\psi_R$), with the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]: a vector of the representation $(\frac12, 0)$ (of $(0, \frac12)$; [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-3|Theorem §C3.3.3]]). These are Peskin–Schroeder's $\psi_L$, $\psi_R$.
>
> *Source: PHY 513 Lecture 8, Part C · PS §3.2, eqs. (3.36)–(3.37) · the user's PHY 513 notes, Ch. 8 §8.2 (eq. (weyllaws))*

^def-c5a-4-2

> [!definition] Definition §C5a.4.3: The Group SL(2, C)
> $SL(2, \mathbb C) = \{\lambda \in M_2(\mathbb C) : \det\lambda = 1\}$, the complex $2\times2$ matrices of unit determinant, a group under matrix multiplication.
>
> *Source: the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit") · Yu Exercise 3.7(c)*

^def-c5a-4-3

The user's notes call these matrices $U_L$, $U_R$; the letter $\Lambda$ is used here because they are not unitary, and $U$ is kept for the unitary operators on states ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1|Principle §C3.5.1]]). The handwritten Lecture 7 notes call the two halves $\xi$ and $\eta$; the Lecture 8 slides and Peskin–Schroeder use $\psi_L$, $\psi_R$. That these laws come out of the Dirac matrices is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; here they are taken from the representation theory of §C3.2–§C3.3 directly. $SL(2, \mathbb C)$ is a group because $\det(\lambda_1\lambda_2) = \det\lambda_1\det\lambda_2$ and $\det\lambda^{-1} = (\det\lambda)^{-1}$; it has $8 - 2 = 6$ real parameters, as many as $SO^+(1,3)$.

> [!theorem] Theorem §C5a.4.1: The Weyl Matrices Lie in SL(2, C)
> For the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] and every $\omega$:
> 1. $\det\Lambda_L(\omega) = \det\Lambda_R(\omega) = 1$, so both lie in $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]);
> 2. $\Lambda_R(\omega) = \bigl(\Lambda_L(\omega)^\dagger\bigr)^{-1}$;
> 3. $\Lambda_L(\omega)^* = \sigma^2\,\Lambda_R(\omega)\,\sigma^2$;
> 4. for a rotation ($\boldsymbol\eta = 0$) $\Lambda_L = \Lambda_R \in SU(2)$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]]); for a pure boost ($\boldsymbol\theta = 0$) $\Lambda_L = e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ and $\Lambda_R = e^{+\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ are Hermitian and positive, not unitary.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "Index calculus for Weyl spinors": "Both have unit determinant", "$U_R = (U_L^\dagger)^{-1}$"; Derivation "The two halves are irreducible, inequivalent, and related by conjugation") · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit") · PS eq. (3.38)*

^thm-c5a-4-1

> [!derivation]- Derivation
> Write $\Lambda_L = e^{A_L}$, $\Lambda_R = e^{A_R}$ with $A_L = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ and $A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ ($\boldsymbol\theta$, $\boldsymbol\eta$ real).
>
> **1. Determinant.** $\det e^A = e^{\operatorname{tr}A}$ (Jacobi's formula, as in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]], step 4). The Pauli matrices are traceless, so $\operatorname{tr}A_L = \operatorname{tr}A_R = 0$ and both determinants are $e^0 = 1$.
>
> **2. Adjoint and inverse.** Term by term in the exponential series, $(e^A)^\dagger = e^{A^\dagger}$; and $(e^A)^{-1} = e^{-A}$. The $\sigma^i$ are Hermitian and $\boldsymbol\theta$, $\boldsymbol\eta$ real, so $A_L^\dagger = +\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$: the adjoint flips the sign of the rotation term only. Then $(\Lambda_L^\dagger)^{-1} = e^{-A_L^\dagger} = e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma} = e^{A_R} = \Lambda_R$.
>
> **3. Complex conjugate.** $(e^A)^{\ast} = e^{A^{\ast}}$ term by term, and $A_L^{\ast} = +\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma^{\ast} - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma^{\ast}$. By Theorem §C5a.1.9, step 4, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\sigma^2A_L^{\ast}\sigma^2 = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma = A_R$. Since $(\sigma^2)^2 = \mathbb 1$, $(\sigma^2Y\sigma^2)^n = \sigma^2Y^n\sigma^2$ for every $n$, hence $\sigma^2e^{Y}\sigma^2 = e^{\sigma^2Y\sigma^2}$. With $Y = A_L^{\ast}$: $\sigma^2\Lambda_L^{\ast}\sigma^2 = e^{A_R} = \Lambda_R$, i.e. $\Lambda_L^{\ast} = \sigma^2\Lambda_R\sigma^2$. ⚑ By-product: $\sigma^2\psi_L^{\ast}$ transforms like $\psi_R$, since $\sigma^2\psi_L^{\ast} \to \sigma^2\Lambda_L^{\ast}\psi_L^{\ast} = \Lambda_R\,\sigma^2\psi_L^{\ast}$; this is the spin-½ case of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]], in index form Theorem §C5a.5.5.
>
> **4. Rotations and boosts.** For $\boldsymbol\eta = 0$, $A_L = A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma$ is anti-Hermitian and traceless, so $e^{A_L}$ is unitary of determinant $1$: an element of $SU(2)$, the spin-½ rotation matrix ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]). For $\boldsymbol\theta = 0$, $A_L = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ is Hermitian with eigenvalues $\mp\frac12|\boldsymbol\eta|$, so $e^{A_L}$ is Hermitian with eigenvalues $e^{\mp|\boldsymbol\eta|/2} > 0$, unitary only for $\boldsymbol\eta = 0$ (as in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]).
>
> **What the derivation shows**
> - Both Weyl representations take values in the same group $SL(2, \mathbb C)$. They differ by the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$ of that group, which is the identity on $SU(2)$ (rotations) and inverts the Hermitian part (boosts).
> - Unit determinant is what will make $\varepsilon$ an invariant (Theorem §C5a.5.4); unitarity fails exactly for boosts.
> - Used next: the covering map (Theorems §C5a.4.4–§C5a.4.7) and the Dirac matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]]).

^der-c5a-4-1

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]

## Four-vectors as Hermitian matrices

> [!theorem] Theorem §C5a.4.2: Four-Vectors as Hermitian Matrices
> 1. $x \mapsto X = x_\mu\sigma^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]) is a real-linear bijection from $\mathbb R^4$ onto the Hermitian $2\times2$ matrices, with inverse $x^\nu = \frac12\operatorname{tr}(X\bar\sigma^\nu)$, and
>
> $$
> X = \begin{pmatrix} x^0 - x^3 & -x^1 + ix^2 \\ -x^1 - ix^2 & x^0 + x^3 \end{pmatrix}, \qquad \det X = x_\mu x^\mu .
> $$
>
> 2. Likewise $x \mapsto \bar X = x_\mu\bar\sigma^\mu$, with inverse $x^\nu = \frac12\operatorname{tr}(\bar X\sigma^\nu)$ and $\det\bar X = x_\mu x^\mu$.
> 3. $x^0 = \frac12\operatorname{tr}X$, and $x$ is future-directed timelike or null ($x^2 \ge 0$, $x^0 > 0$) iff $X$ is positive semidefinite and nonzero.
>
> *Source: Yu Exercise 3.7, eqs. (3.259)–(3.260) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (a)) · part 3 written out here*

^thm-c5a-4-2

> [!derivation]- Derivation
> **1. The matrix.** $X = x_0\mathbb 1 + x_i\sigma^i$ with $x_0 = x^0$, $x_i = -x^i$, i.e. $X = x^0\mathbb 1 - x^1\sigma^1 - x^2\sigma^2 - x^3\sigma^3$. Inserting $\sigma^1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma^2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\sigma^3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$: the diagonal is $x^0 \mp x^3$; the upper-right entry is $-x^1 - x^2(-i) = -x^1 + ix^2$; the lower-left is $-x^1 - x^2(i) = -x^1 - ix^2$. The two off-diagonal entries are complex conjugates and the diagonal is real: $X$ is Hermitian.
>
> **2. Onto, and the inverse.** Every Hermitian $2\times2$ matrix is $a_0\mathbb 1 + \mathbf a\cdot\boldsymbol\sigma$ with real $a_0, \mathbf a$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], part 4); it is $X$ for $x^0 = a_0$, $\mathbf x = -\mathbf a$. For the inverse, multiply $X = x_\mu\sigma^\mu$ by $\bar\sigma^\nu$ and take the trace: $\operatorname{tr}(X\bar\sigma^\nu) = x_\mu\operatorname{tr}(\sigma^\mu\bar\sigma^\nu) = 2x_\mu g^{\mu\nu} = 2x^\nu$ (Theorem §C5a.1.9, 1). So $x$ is recovered from $X$, and the map is injective.
>
> **3. Determinant.** From step 1, $\det X = (x^0 - x^3)(x^0 + x^3) - (-x^1 + ix^2)(-x^1 - ix^2) = (x^0)^2 - (x^3)^2 - \bigl((x^1)^2 + (x^2)^2\bigr) = x_\mu x^\mu$, using $(-x^1 + ix^2)(-x^1 - ix^2) = (x^1)^2 - (ix^2)^2 = (x^1)^2 + (x^2)^2$.
>
> **4. Part 2.** $\bar X = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$ is $X$ with $\mathbf x \to -\mathbf x$, so it is Hermitian, the map is onto by the same argument, and $\det\bar X = (x^0)^2 - \mathbf x^2$. The inverse uses $\operatorname{tr}(\bar\sigma^\mu\sigma^\nu) = 2g^{\mu\nu}$, which follows from Theorem §C5a.1.9, 1 by cyclicity of the trace.
>
> **5. Part 3.** $\operatorname{tr}X = 2x^0$ (the $\sigma^i$ are traceless). The eigenvalues $\lambda_\pm$ of the Hermitian $X$ are real with $\lambda_+ + \lambda_- = 2x^0$ and $\lambda_+\lambda_- = \det X = x^2$. Both are $\ge 0$ and not both $0$ iff the product is $\ge 0$ and the sum is $> 0$, i.e. iff $x^2 \ge 0$ and $x^0 > 0$.
>
> **What the derivation shows**
> - The Minkowski interval is a determinant, and the forward light cone is the cone of positive semidefinite matrices. Any operation on $X$ that preserves Hermiticity and the determinant therefore preserves the interval: that is how $SL(2, \mathbb C)$ will act (Theorem §C5a.4.4).
> - The spatial part alone, $\mathbf x\cdot\boldsymbol\sigma$ (traceless Hermitian), is the dictionary of the rotation case, with $\det(\mathbf x\cdot\boldsymbol\sigma) = -|\mathbf x|^2$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]).

^der-c5a-4-2

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## The covering map

> [!theorem] Theorem §C5a.4.3: SL(2, C) Is Connected and Simply Connected
> Every $\lambda \in SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]) is uniquely $\lambda = e^{h}U$ with $U \in SU(2)$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]]) and $h$ traceless Hermitian, $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ for a unique $\boldsymbol\eta \in \mathbb R^3$, and $\lambda \mapsto (\boldsymbol\eta, U)$ is a homeomorphism $SL(2, \mathbb C) \cong \mathbb R^3\times S^3$. Hence $SL(2, \mathbb C)$ is path-connected and simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]).
>
> *Source: Yu Exercise 3.7(d), eq. (3.265) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (d)) · the continuity of the decomposition quoted from the functional calculus*

^thm-c5a-4-3

> [!derivation]- Derivation
> **1. The positive part.** $\lambda\lambda^\dagger$ is Hermitian and positive definite: $v^\dagger\lambda\lambda^\dagger v = |\lambda^\dagger v|^2 > 0$ for $v \ne 0$, since $\lambda$ is invertible. By the spectral theorem it is $W\operatorname{diag}(p_1, p_2)W^\dagger$ with $W$ unitary and $p_k > 0$. Set $h = \frac12W\operatorname{diag}(\ln p_1, \ln p_2)W^\dagger$, Hermitian, so that $e^{2h} = \lambda\lambda^\dagger$ ($e^{WDW^\dagger} = We^DW^\dagger$ term by term). It is the unique Hermitian $h$ with $e^{2h} = \lambda\lambda^\dagger$: $e^{2h}$ and $h$ have the same eigenvectors, and $\ln$ is injective on $(0, \infty)$; equivalently $e^h$ is the unique positive square root of $\lambda\lambda^\dagger$ ([[§25 Positive Operators#^ladr-7-39|LADR 7.39]]).
>
> **2. The unitary part.** Put $U = e^{-h}\lambda$. Then $UU^\dagger = e^{-h}\lambda\lambda^\dagger e^{-h} = e^{-h}e^{2h}e^{-h} = \mathbb 1$, so $U$ is unitary and $\lambda = e^hU$: the polar decomposition ([[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], here with the positive factor on the left).
>
> **3. Determinants.** $1 = \det\lambda = \det e^h\det U = e^{\operatorname{tr}h}\det U$. Here $e^{\operatorname{tr}h} > 0$ ($h$ Hermitian has real trace) and $|\det U| = 1$; a positive number times a unit-modulus number equals $1$ only if the positive number is $1$ and the phase is $1$. So $\operatorname{tr}h = 0$ and $\det U = 1$: $U \in SU(2)$, and $h$ is traceless Hermitian, $h = \mathbf a\cdot\boldsymbol\sigma$ with $\mathbf a$ real ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], part 4); write $\mathbf a = -\frac12\boldsymbol\eta$.
>
> **4. Uniqueness.** If $\lambda = e^{h'}U'$ is another such decomposition, then $\lambda\lambda^\dagger = e^{h'}U'U'^\dagger e^{h'} = e^{2h'}$, so $h' = h$ by step 1, and $U' = e^{-h}\lambda = U$.
>
> **5. Homeomorphism.** The map $(\boldsymbol\eta, U) \mapsto e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}U$ is continuous (products and the exponential series), and by steps 1–4 it is a bijection $\mathbb R^3\times SU(2) \to SL(2, \mathbb C)$. Its inverse $\lambda \mapsto h = \frac12\ln(\lambda\lambda^\dagger)$, $U = e^{-h}\lambda$ is continuous because the logarithm of positive definite matrices is continuous (functional calculus; quoted). $SU(2)$ is homeomorphic to $S^3$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]]; [[§C3.1 Groups, Algebras and Representations of Rotations#^der-c3-1-8|Derivation §C3.1.8]], step 1).
>
> **6. Topology.** $\mathbb R^3$ is convex, so path-connected with every loop contractible (straight-line homotopy); $S^3$ is path-connected and simply connected ([[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]]). A product of path-connected spaces is path-connected, and $\pi_1(\mathbb R^3\times S^3) \cong \pi_1(\mathbb R^3)\times\pi_1(S^3) = 1$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]).
>
> **What the derivation shows**
> - $SL(2, \mathbb C)$ is "rotations times boosts": $U$ will map to a rotation and $e^h$ to a pure boost, the $2\times2$ counterpart of $\Lambda = B(u)R$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]).
> - The noncompact factor $\mathbb R^3$ is topologically trivial; all the topology sits in the compact factor, and for $SL(2, \mathbb C)$ that factor is the simply connected $S^3$.
> - One input was quoted: the continuity of the matrix logarithm on positive matrices.
> - Used next: connectedness puts the image of the covering map in $SO^+(1,3)$ (Theorem §C5a.4.4); simple connectivity makes it the universal cover (Theorem §C5a.4.7).

^der-c5a-4-3

*Uses:* [[§25 Positive Operators#^ladr-7-39|LADR 7.39]], [[§28 Consequences of Singular Value Decomposition#^ladr-7-93|LADR 7.93]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]], [[§37 The Fundamental Group of Sⁿ#^thm-37-3|590 Thm. §37.3]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; quoted: continuity of the logarithm of positive matrices

> [!theorem] Theorem §C5a.4.4: Every Element of SL(2, C) Gives a Lorentz Transformation
> For $\lambda \in SL(2, \mathbb C)$ define $\Lambda(\lambda)$ through the dictionary $x \leftrightarrow x_\mu\sigma^\mu$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]] by
>
> $$
> \lambda\,(x_\mu\sigma^\mu)\,\lambda^\dagger = \bigl(\Lambda(\lambda)x\bigr)_\mu\sigma^\mu, \qquad\text{i.e.}\qquad \Lambda(\lambda)^\mu{}_\nu = \tfrac12\operatorname{tr}\bigl(\lambda\sigma_\nu\lambda^\dagger\bar\sigma^\mu\bigr) .
> $$
>
> Then $\Lambda(\lambda)$ is a proper orthochronous Lorentz transformation, $\Lambda(\lambda) \in SO^+(1,3)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-4|Def. §C1a.4.4]]), $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$, $\Lambda(\mathbb 1) = \mathbb 1$, and $\lambda \mapsto \Lambda(\lambda)$ is continuous: a continuous homomorphism $\pi: SL(2, \mathbb C) \to SO^+(1,3)$.
>
> *Source: Yu Exercise 3.7(b)–(c), eqs. (3.261)–(3.264), (d) · the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", parts (b), (d))*

^thm-c5a-4-4

> [!derivation]- Derivation
> **1. A real linear map.** For Hermitian $X$, $(\lambda X\lambda^\dagger)^\dagger = \lambda X^\dagger\lambda^\dagger = \lambda X\lambda^\dagger$ is Hermitian, so by Theorem §C5a.4.2 it is $X'$ for a unique real $x'$. $X$ is linear in $x$ and $X \mapsto \lambda X\lambda^\dagger$ is linear, so $x' = \Lambda(\lambda)x$ with $\Lambda(\lambda)$ a real $4\times4$ matrix. Its entries: $X = x_\nu\sigma^\nu = x^\nu\sigma_\nu$, and by the inverse formula $x'^\mu = \frac12\operatorname{tr}(\lambda x^\nu\sigma_\nu\lambda^\dagger\bar\sigma^\mu)$, which gives the trace formula; it is a polynomial in the entries of $\lambda$ and $\lambda^{\ast}$, hence continuous.
>
> **2. The interval is preserved.** $\det X' = \det\lambda\,\det X\,\det\lambda^\dagger = |\det\lambda|^2\det X = \det X$, i.e. $x'^2 = x^2$ (Theorem §C5a.4.2). A linear map preserving the quadratic form preserves the bilinear form, by polarization: $x\cdot y = \frac12\bigl((x + y)^2 - x^2 - y^2\bigr)$. So $\Lambda(\lambda)^{\mathsf T}g\Lambda(\lambda) = g$: $\Lambda(\lambda) \in O(1,3)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]).
>
> **3. Homomorphism.** $(\lambda_1\lambda_2)X(\lambda_1\lambda_2)^\dagger = \lambda_1(\lambda_2X\lambda_2^\dagger)\lambda_1^\dagger$: first $x \mapsto \Lambda(\lambda_2)x$, then $\Lambda(\lambda_1)$. By injectivity of $x \mapsto X$, $\Lambda(\lambda_1\lambda_2) = \Lambda(\lambda_1)\Lambda(\lambda_2)$. For $\lambda = \mathbb 1$, $X' = X$, so $\Lambda(\mathbb 1) = \mathbb 1$.
>
> **4. Proper and orthochronous.** $SL(2, \mathbb C)$ is path-connected (Theorem §C5a.4.3) and $\pi$ is continuous (step 1), so the image $\pi(SL(2, \mathbb C))$ is a path-connected subset of $O(1,3)$ containing $\pi(\mathbb 1) = \mathbb 1$. It therefore lies in the component of the identity, which is $SO^+(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], 2).
>
> **What the derivation shows**
> - Only $|\det\lambda| = 1$ was used for step 2; Yu then fixes the phase by $\det\lambda = 1$, since $\lambda$ and $e^{i\alpha}\lambda$ give the same $\Lambda$. The group $SL(2, \mathbb C)$ is what remains after that redundancy is removed, up to the sign left over in Theorem §C5a.4.5.
> - Determinant $+1$ and $\Lambda^0{}_0 > 0$ were not checked by hand: connectedness does it. Directly, $\Lambda^0{}_0 = \frac12\operatorname{tr}(\lambda\lambda^\dagger) > 0$.
> - Used next: the kernel (Theorem §C5a.4.5), the link to the parameters $\omega$ (Theorem §C5a.4.6).

^der-c5a-4-4

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]

> [!theorem] Theorem §C5a.4.5: The Kernel Is ±1
> For the homomorphism $\pi$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], $\pi(\lambda) = \mathbb 1$ iff $\lambda = \pm\mathbb 1$. Hence $\pi(\lambda) = \pi(\lambda')$ iff $\lambda' = \pm\lambda$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit", part (c)) · Yu Exercise 3.7(d) (paragraph after (3.265))*

^thm-c5a-4-5

> [!derivation]- Derivation
> **1. ±1 are in the kernel.** $(\pm\mathbb 1)X(\pm\mathbb 1)^\dagger = X$, and $\det(\pm\mathbb 1) = 1$.
>
> **2. An element of the kernel is unitary.** If $\pi(\lambda) = \mathbb 1$, then $\lambda X\lambda^\dagger = X$ for every Hermitian $X$. Take $X = \mathbb 1$ ($x = (1, \mathbf 0)$): $\lambda\lambda^\dagger = \mathbb 1$, so $\lambda^\dagger = \lambda^{-1}$.
>
> **3. It commutes with everything.** With $\lambda^\dagger = \lambda^{-1}$ the condition reads $\lambda X\lambda^{-1} = X$, i.e. $\lambda X = X\lambda$, for every Hermitian $X$, in particular for $\sigma^1, \sigma^2, \sigma^3$. Together with $\mathbb 1$ these span $M_2(\mathbb C)$ over $\mathbb C$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], part 4), so $\lambda$ commutes with every $2\times2$ matrix; taking the matrix units $E_{12}$, $E_{21}$ forces $\lambda = c\mathbb 1$ (the same conclusion as Schur's lemma, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-3|Theorem §C3.1.3]]).
>
> **4. The scalar.** $\det(c\mathbb 1) = c^2 = 1$ gives $c = \pm1$.
>
> **5. Fibres.** $\pi(\lambda) = \pi(\lambda')$ iff $\pi(\lambda'\lambda^{-1}) = \mathbb 1$ (homomorphism, Theorem §C5a.4.4) iff $\lambda'\lambda^{-1} = \pm\mathbb 1$.
>
> **What the derivation shows**
> - The sign ambiguity is the only one: two spinor matrices $\pm\lambda$ for each Lorentz transformation. This is the matrix origin of "a spinor's matrix is fixed only up to sign" ([[§C3.4 How Fields Transform under the Lorentz Group#^rem-c3-4-4|§C3.4, Remark: Why a spinor's matrix is fixed only up to sign]]).
> - The argument is that of the rotation case ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], 3), with $X = \mathbb 1$ added to force unitarity first.

^der-c5a-4-5

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!theorem] Theorem §C5a.4.6: The Weyl Matrices Cover the Vector Representation
> For the Weyl matrices $\Lambda_L(\omega)$, $\Lambda_R(\omega)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] and every $\omega$, with $\Lambda = e^{\omega}$ the vector-representation matrix of the same parameters ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]):
> 1. $\Lambda_L(\omega)\,(x_\mu\sigma^\mu)\,\Lambda_L(\omega)^\dagger = (\Lambda x)_\mu\sigma^\mu$, i.e. $\pi(\Lambda_L(\omega)) = e^{\omega}$ ($\pi$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]]); and $\Lambda_R(\omega)\,(x_\mu\bar\sigma^\mu)\,\Lambda_R(\omega)^\dagger = (\Lambda x)_\mu\bar\sigma^\mu$.
> 2. Equivalently, $\bar\sigma^\mu$ and $\sigma^\mu$ are invariant under the Weyl matrices:
>
> $$
> \Lambda_L^\dagger\,\bar\sigma^\mu\,\Lambda_L = \Lambda^\mu{}_\nu\,\bar\sigma^\nu, \qquad \Lambda_R^\dagger\,\sigma^\mu\,\Lambda_R = \Lambda^\mu{}_\nu\,\sigma^\nu .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering", eq. (SL2Ccover); checked numerically there, and again here) · Yu Exercise 3.7(e), eqs. (3.267)–(3.268) (rotation about z) · part 2 and the series argument written out here*

^thm-c5a-4-6

> [!derivation]- Derivation
> Write $\Phi(x) = x_\mu\sigma^\mu$, $\bar\Phi(x) = x_\mu\bar\sigma^\mu$, and $\Lambda_L(s\omega) = e^{sA_L}$, $A_L = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ (the exponent is linear in $\omega$).
>
> **1. The vector side, infinitesimally.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], $\Lambda = e^{\omega}$ with $(\omega x)^\mu = \omega^\mu{}_\nu x^\nu$. Its components, with $\omega^0{}_i = \omega_{0i} = \eta_i$, $\omega^i{}_0 = g^{ii}\omega_{i0} = \eta_i$ and $\omega^i{}_j = -\omega_{ij} = -\varepsilon_{ijk}\theta_k$:
>
> $$
> (\omega x)^0 = \boldsymbol\eta\cdot\mathbf x, \qquad (\omega x)^i = \eta_ix^0 - \varepsilon_{ijk}\theta_kx^j = \eta_ix^0 + (\boldsymbol\theta\times\mathbf x)_i ,
> $$
>
> the last step by relabelling $j \leftrightarrow k$ and $\varepsilon_{ikj} = -\varepsilon_{ijk}$. Hence $\Phi(\omega x) = (\omega x)^0\mathbb 1 - (\omega x)\cdot\boldsymbol\sigma = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 - (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma$.
>
> **2. The spinor side, infinitesimally.** Define the linear map $L(M) = A_LM + MA_L^\dagger$ on $M_2(\mathbb C)$. With $A_L^\dagger = \frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$,
>
> $$
> L(\Phi(x)) = -\tfrac i2\bigl[\boldsymbol\theta\cdot\boldsymbol\sigma, \Phi(x)\bigr] - \tfrac12\bigl\{\boldsymbol\eta\cdot\boldsymbol\sigma, \Phi(x)\bigr\} .
> $$
>
> With $\Phi(x) = x^0\mathbb 1 - \mathbf x\cdot\boldsymbol\sigma$ and the vector form of the Pauli product, $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)\mathbb 1 + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 3): $[\boldsymbol\theta\cdot\boldsymbol\sigma, \mathbf x\cdot\boldsymbol\sigma] = 2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma$ and $\{\boldsymbol\eta\cdot\boldsymbol\sigma, \mathbf x\cdot\boldsymbol\sigma\} = 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1$; $\mathbb 1$ commutes with everything and $\{\boldsymbol\eta\cdot\boldsymbol\sigma, x^0\mathbb 1\} = 2x^0\boldsymbol\eta\cdot\boldsymbol\sigma$. So
>
> $$
> L(\Phi(x)) = -\tfrac i2\bigl(-2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma\bigr) - \tfrac12\bigl(2x^0\boldsymbol\eta\cdot\boldsymbol\sigma - 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1\bigr) = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 - (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma ,
> $$
>
> using $-\frac i2\cdot(-2i) = -1$. Comparing with step 1: $L\circ\Phi = \Phi\circ\omega$ as maps $\mathbb R^4 \to M_2(\mathbb C)$.
>
> **3. Exponentiate.** Left multiplication $\ell(M) = A_LM$ and right multiplication $r(M) = MA_L^\dagger$ commute as linear maps of $M_2(\mathbb C)$ ($A_L(MA_L^\dagger) = (A_LM)A_L^\dagger$), so $e^{s(\ell + r)} = e^{s\ell}e^{sr}$ (the binomial argument of [[§C3.2 The Lorentz Algebra#^der-c3-2-4|Derivation §C3.2.4]], step 3), i.e. $e^{sL}(M) = e^{sA_L}Me^{sA_L^\dagger} = \Lambda_L(s\omega)M\Lambda_L(s\omega)^\dagger$ (with $(e^{sA_L})^\dagger = e^{sA_L^\dagger}$). Iterating step 2, $L^n\circ\Phi = \Phi\circ\omega^n$ for every $n$, so summing the series (both converge absolutely; $\Phi$ is linear) $e^{sL}\circ\Phi = \Phi\circ e^{s\omega}$. At $s = 1$: $\Lambda_L(\omega)\Phi(x)\Lambda_L(\omega)^\dagger = \Phi(e^\omega x)$, part 1 for $\Lambda_L$. By the definition of $\pi$ (Theorem §C5a.4.4), $\pi(\Lambda_L(\omega)) = e^{\omega}$.
>
> **4. The right-handed matrices.** $A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ and $\bar\Phi(x) = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$. Then $A_R\bar\Phi + \bar\Phi A_R^\dagger = -\frac i2[\boldsymbol\theta\cdot\boldsymbol\sigma, \bar\Phi] + \frac12\{\boldsymbol\eta\cdot\boldsymbol\sigma, \bar\Phi\} = -\frac i2\cdot2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma + \frac12\bigl(2x^0\boldsymbol\eta\cdot\boldsymbol\sigma + 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1\bigr) = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 + (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma = \bar\Phi(\omega x)$, the signs of both the rotation and the boost term having flipped relative to step 2 together with the sign of $\mathbf x$ in $\bar\Phi$. Step 3 applies verbatim.
>
> **5. Part 2.** Multiply part 1 by $\bar\sigma^\nu$ and take the trace. The right side gives $\operatorname{tr}(\Phi(\Lambda x)\bar\sigma^\nu) = 2(\Lambda x)^\nu = \Lambda^\nu{}_\mu\operatorname{tr}(\Phi(x)\bar\sigma^\mu)$ (Theorem §C5a.4.2). The left side, by cyclicity, is $\operatorname{tr}(\Phi(x)\,\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L)$. So $\operatorname{tr}\bigl(X\,(\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L - \Lambda^\nu{}_\mu\bar\sigma^\mu)\bigr) = 0$ for every Hermitian $X$, hence (complex-linearly) for every $X \in M_2(\mathbb C)$, since every matrix is $H_1 + iH_2$ with $H_k$ Hermitian. Taking $X = E_{ji}$ picks out the $(i, j)$ entry of the bracket, so the bracket vanishes. The same with $\Lambda_R$, $\bar\Phi$ and $\operatorname{tr}(\bar X\sigma^\nu) = 2x^\nu$ gives $\Lambda_R^\dagger\sigma^\nu\Lambda_R = \Lambda^\nu{}_\mu\sigma^\mu$.
>
> **6. Check: rotation about z.** $\boldsymbol\theta = \theta\hat{\mathbf z}$: $\Lambda_L = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$, and in the matrix of Theorem §C5a.4.2 the off-diagonal entry $-x^1 + ix^2$ is multiplied by $e^{-i\theta/2}\cdot\overline{e^{i\theta/2}} = e^{-i\theta}$, which is the active rotation $(x^1, x^2) \mapsto (x^1\cos\theta - x^2\sin\theta, x^1\sin\theta + x^2\cos\theta)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]). Yu's $\lambda(\theta) = \operatorname{diag}(e^{i\theta/2}, e^{-i\theta/2})$ in (3.267) is $\Lambda_L$ at $-\theta$, the passive rotation of (3.268).
>
> **What the derivation shows**
> - The same six numbers $\omega_{\mu\nu}$ produce $\Lambda_L(\omega)$ and $e^\omega$, and the covering map sends one to the other. The half-angles of $\Lambda_L$ become full angles because $\lambda$ acts on $X$ twice, once from each side.
> - Part 2 says that $\bar\sigma^\mu$ is an invariant tensor with one vector slot and two spinor slots, as $\gamma^\mu$ will be ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]]); it is why $\psi_L^\dagger\bar\sigma^\mu\psi_L$ is a four-vector (QFT §C5a.7, the Weyl Lagrangian).
> - $\Lambda_R(\omega) = (\Lambda_L(\omega)^\dagger)^{-1}$ is *not* $\Lambda_L$ of another $\omega$ with the same $\sigma$: it covers $e^\omega$ through $\bar\sigma$. Using $\sigma$ for $\Lambda_R$ would give the parity image of $e^\omega$.
> - Used next: $\pi$ is onto (Theorem §C5a.4.7), and every $(j_+, j_-)$ integrates (Theorem §C5a.4.8).

^der-c5a-4-6

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C3.2 The Lorentz Algebra#^der-c3-2-4|Derivation §C3.2.4]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]

> [!theorem] Theorem §C5a.4.7: SL(2, C) Is the Double Cover of SO⁺(1,3)
> 1. $\pi: SL(2, \mathbb C) \to SO^+(1,3)$ is onto, and $SO^+(1,3) \cong SL(2, \mathbb C)/\{\pm\mathbb 1\}$.
> 2. $SO^+(1,3)$ is homeomorphic to $\mathbb R^3\times SO(3)$, so its fundamental group ([[§29 The Fundamental Group#^def-29-2|590 Def. §29.2]]) is $\pi_1(SO^+(1,3)) \cong \mathbb Z_2$: it is doubly connected, as anticipated in [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-8|§C3.1, Remark: The same pattern for the Lorentz group]]. The non-contractible loops are those homotopic to a rotation through $2\pi$; the lift ([[§32 Lifting and the Fundamental Group of the Circle#^def-32-1|590 Def. §32.1]]) of that loop to $SL(2, \mathbb C)$ starting at $\mathbb 1$, $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, ends at $-\mathbb 1$.
> 3. Under $\pi$, $U \in SU(2)$ goes to the rotation $\operatorname{diag}(1, R(U))$ of [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], and $e^{-\boldsymbol\eta\cdot\boldsymbol\sigma/2}$ to the pure boost $e^{\omega}$ with $\omega_{0i} = \eta_i$, $\omega_{ij} = 0$. $\pi$ is a covering map ([[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]), and since $SL(2, \mathbb C)$ is simply connected ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), it is the universal covering group of $SO^+(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering": "every element of $\mathrm{SO}^+(1,3)$ is reached … $\mathrm{SO}^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$") · Yu Exercise 3.7(d) · Yu §3.2 (the covering group of SO⁺(1,3) named, below Fig. 3.5) · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit": kernel and surjectivity "stated, not proved here") · the user's PHY 513 notes, Ch. 7 §7.2 (end of Derivation "Why the sign appears": the topological argument) · that a surjective Lie-group homomorphism with bijective differential is a covering map, quoted*

^thm-c5a-4-7

> [!derivation]- Derivation
> **1. Onto.** Every $\Lambda \in SO^+(1,3)$ is a boost times a rotation, $\Lambda = B(u)R$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]), and each factor is an exponential $e^{\omega_1}$, $e^{\omega_2}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]; a boost along $\hat{\mathbf n}$ is $e^{\omega}$ with $\omega_{0i} = \eta n_i$, as used in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^der-c3-3-10|Derivation §C3.3.10]], step 5). By Theorem §C5a.4.6, $\pi(\Lambda_L(\omega_1)\Lambda_L(\omega_2)) = e^{\omega_1}e^{\omega_2} = \Lambda$.
>
> **2. The quotient.** $\pi$ is an onto homomorphism with kernel $\{\pm\mathbb 1\}$ (Theorem §C5a.4.5), so $SL(2, \mathbb C)/\{\pm\mathbb 1\} \cong SO^+(1,3)$ by the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]).
>
> **3. The topology of SO⁺(1,3).** By [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], $\Lambda = B(u)R$ with $u = \Lambda e_0$, the first column, $u = (\gamma, \mathbf u)$, $\gamma = \sqrt{1 + \mathbf u^2}$. The map $\Lambda \mapsto (\mathbf u, R)$, $R = B(u)^{-1}\Lambda$, is continuous (the entries of $B(u)$ are continuous in $\mathbf u$, $\gamma \ge 1$), and its inverse $(\mathbf u, R) \mapsto B(u)R$ is continuous: a homeomorphism $SO^+(1,3) \cong \mathbb R^3\times SO(3)$. Hence $\pi_1(SO^+(1,3)) \cong \pi_1(\mathbb R^3)\times\pi_1(SO(3)) = 1\times\mathbb Z_2$ ([[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]]; [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]), and a loop is non-contractible iff its $SO(3)$ component is, i.e. iff it is homotopic to the $2\pi$ rotation loop.
>
> **4. The lift of the 2π loop.** $\theta \mapsto \Lambda_L(\theta\hat{\mathbf z}) = e^{-i\theta\sigma^3/2}$, $0 \le \theta \le 2\pi$, is continuous, starts at $\mathbb 1$, and lies over the rotation loop by Theorem §C5a.4.6. At $\theta = 2\pi$ it is $\operatorname{diag}(e^{-i\pi}, e^{i\pi}) = -\mathbb 1$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]): a closed loop downstairs whose lift is open. ⚑ By-product: this is the "$2\pi$ rotation $= -1$" of every half-integer representation, now seen as the endpoint of a lift → [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]].
>
> **5. The two decompositions match.** For $U \in SU(2)$, $UXU^\dagger = x^0\mathbb 1 - U(\mathbf x\cdot\boldsymbol\sigma)U^\dagger = x^0\mathbb 1 - (R(U)\mathbf x)\cdot\boldsymbol\sigma$ by the definition of $R(U)$ in QM Theorem §C5.2.6, so $\pi(U) = \operatorname{diag}(1, R(U))$. For $h = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$, $e^h = \Lambda_L(\omega)$ with $\boldsymbol\theta = 0$, so $\pi(e^h) = e^{\omega}$, a pure boost (Theorem §C5a.4.6). The polar decomposition $\lambda = e^hU$ of Theorem §C5a.4.3 is mapped to "boost times rotation".
>
> **6. Universal cover.** $\pi$ is a continuous surjective homomorphism of Lie groups whose differential at $\mathbb 1$ sends the generator $A_L(\omega)$ to $\omega$ (step 2 of Derivation §C5a.4.6), a bijection between the two six-dimensional algebras; such a map is a covering map (quoted). A simply connected covering space is the universal cover, and its fibre $\{\pm\mathbb 1\}$ has as many points as $\pi_1(SO^+(1,3))$ has elements, consistently with step 3 ([[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]).
>
> **What the derivation shows**
> - All topology of the Lorentz group is that of its rotation subgroup: boosts form a contractible $\mathbb R^3$, and the cover unwraps only the $SO(3)$ factor into $S^3$. This makes the remark of §C3.1 precise.
> - $SO^+(1,3) \cong \mathbb{RP}^3\times\mathbb R^3$, $SL(2, \mathbb C) \cong S^3\times\mathbb R^3$, the $\pm$ identification acting on the sphere only.
> - One input was quoted: that $\pi$ is a covering map. Everything needed later (onto, kernel, the lift of the $2\pi$ loop) was derived.
> - Used next: integrating $(j_+, j_-)$ (Theorem §C5a.4.8).

^der-c5a-4-7

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§29 The Fundamental Group#^thm-29-7|590 Thm. §29.7]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]]; quoted: a surjective Lie-group homomorphism with bijective differential is a covering map

> [!remark] Remark: The rotation story, one level up
>
> | | rotations | Lorentz transformations |
> |---|---|---|
> | vectors as matrices | $\mathbf x\cdot\boldsymbol\sigma$, traceless Hermitian | $x_\mu\sigma^\mu$, Hermitian |
> | invariant | $-\det = \lvert\mathbf x\rvert^2$ | $\det = x_\mu x^\mu$ |
> | action | $U(\mathbf x\cdot\boldsymbol\sigma)U^\dagger$, $U \in SU(2)$ | $\lambda(x_\mu\sigma^\mu)\lambda^\dagger$, $\lambda \in SL(2, \mathbb C)$ |
> | kernel | $\pm\mathbb 1$ | $\pm\mathbb 1$ |
> | covering space | $S^3$, compact | $S^3\times\mathbb R^3$, not compact |
> | finite-dimensional representations | unitary | not unitary (except trivial) |
>
> The left column is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; the right column contains it as the subgroup fixing $x^0 = \frac12\operatorname{tr}X$ (unitary $\lambda$). Two things change: $\lambda^\dagger$ is no longer $\lambda^{-1}$, so $\lambda X\lambda^\dagger$ is not a similarity transformation and the trace (time) is no longer preserved; and the group is not compact, so averaging over it is impossible and unitarity is lost ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The double cover made explicit": "Rotations had $U^\dagger\sigma^iU = R^i{}_j\sigma^j$ … The Lorentz version turns a four-vector into a $2\times2$ matrix")*

^rem-c5a-4-1

## Every finite-dimensional representation integrates

> [!theorem] Theorem §C5a.4.8: Integer (j₊, j₋) Are Representations of SO⁺(1,3)
> 1. On $V_{j_+}\otimes V_{j_-}$, $V_j$ the homogeneous polynomials of degree $2j$ in $z \in \mathbb C^2$ (the spin-$j$ space of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]]), the matrices
>
> $$
> \tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}\bigl((\lambda^\dagger)^{-1}\bigr), \qquad \bigl(D^{(j)}(M)P\bigr)(z) = P(M^{\mathsf T}z),
> $$
>
> form a representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-5|Def. §C3.1.5]]) of $SL(2, \mathbb C)$ with $\tilde D(\Lambda_L(\omega)) = \exp\bigl(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})\bigr)$, $D(\mathcal J^{\mu\nu})$ the generators ([[§C3.2 The Lorentz Algebra#^def-c3-2-1|Def. §C3.2.1]]) of the representation $(j_+, j_-)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]), and $\tilde D(-\mathbb 1) = (-1)^{2(j_+ + j_-)}$. It is the only one with these generators.
> 2. If $j_+ + j_-$ is an integer, $D(\Lambda) \equiv \tilde D(\lambda)$ for any $\lambda$ with $\pi(\lambda) = \Lambda$ is a well-defined representation of $SO^+(1,3)$. If $j_+ + j_-$ is half an odd integer, $D(\Lambda)$ is defined only up to sign, a two-valued representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-14|Def. §C3.1.14]]), as [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]] found.
> 3. Hence a finite-dimensional representation of the Lorentz algebra (a sum of pieces $(j_+, j_-)$, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]) integrates to $SO^+(1,3)$ iff every piece $(j_+, j_-)$ in it has $j_+ + j_-$ an integer; every one integrates to $SL(2, \mathbb C)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (spin $j$ on polynomials), §7.4.4 (the sign rule) and Ch. 8 §8.1 ("the Dirac representation is a representation of the double cover") · the proof written out here*

^thm-c5a-4-8

> [!derivation]- Derivation
> **1. A representation of SL(2, C).** For any invertible $M_1, M_2$: $(D^{(j)}(M_1)D^{(j)}(M_2)P)(z) = (D^{(j)}(M_2)P)(M_1^{\mathsf T}z) = P(M_2^{\mathsf T}M_1^{\mathsf T}z) = P((M_1M_2)^{\mathsf T}z)$, so $D^{(j)}(M_1M_2) = D^{(j)}(M_1)D^{(j)}(M_2)$; $D^{(j)}(M)P$ is again homogeneous of degree $2j$. The map $\lambda \mapsto (\lambda^\dagger)^{-1}$ is a homomorphism: $((\lambda_1\lambda_2)^\dagger)^{-1} = (\lambda_2^\dagger\lambda_1^\dagger)^{-1} = (\lambda_1^\dagger)^{-1}(\lambda_2^\dagger)^{-1}$. A tensor product of representations is one, $(A\otimes B)(A'\otimes B') = AA'\otimes BB'$. So $\tilde D(\lambda_1\lambda_2) = \tilde D(\lambda_1)\tilde D(\lambda_2)$.
>
> **2. On the Weyl matrices.** With $\boldsymbol\alpha = \boldsymbol\theta - i\boldsymbol\eta \in \mathbb C^3$: $\Lambda_L(\omega) = e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2}$ and $(\Lambda_L(\omega)^\dagger)^{-1} = \Lambda_R(\omega) = e^{-i\bar{\boldsymbol\alpha}\cdot\boldsymbol\sigma/2}$, $\bar{\boldsymbol\alpha} = \boldsymbol\theta + i\boldsymbol\eta$ (Theorem §C5a.4.1, 2). So $\tilde D(\Lambda_L(\omega)) = f_{j_+}(\boldsymbol\alpha)\otimes f_{j_-}(\bar{\boldsymbol\alpha})$ with $f_j(\boldsymbol\alpha) \equiv D^{(j)}(e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2})$.
>
> **3. Real angles.** For real $\boldsymbol\alpha = s\hat{\mathbf n}$, $s \mapsto e^{-is\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ is a one-parameter subgroup of $SU(2)$, so $s \mapsto f_j(s\hat{\mathbf n})$ is a one-parameter group of matrices whose derivative at $0$ is $-i\hat{\mathbf n}\cdot\mathbf J^{(j)}$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], 1: $D^{(j)}$ on $SU(2)$ has the spin-$j$ matrices as generators). A one-parameter group is fixed by its derivative at $0$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]]), so $f_j(\boldsymbol\alpha) = g_j(\boldsymbol\alpha) \equiv e^{-i\boldsymbol\alpha\cdot\mathbf J^{(j)}}$ for all $\boldsymbol\alpha \in \mathbb R^3$.
>
> **4. Complex angles: analytic continuation.** Each entry of $f_j$ is a polynomial in the entries of $e^{-i\boldsymbol\alpha\cdot\boldsymbol\sigma/2}$, each of which is an entire function of $(\alpha_1, \alpha_2, \alpha_3) \in \mathbb C^3$ (an everywhere convergent power series); each entry of $g_j$ is entire for the same reason. An entire function $F$ on $\mathbb C^3$ vanishing on $\mathbb R^3$ vanishes identically: for fixed real $\alpha_2, \alpha_3$, $\alpha_1 \mapsto F$ is entire and vanishes on $\mathbb R$, so it vanishes on $\mathbb C$ (identity theorem); then for fixed $\alpha_1 \in \mathbb C$, real $\alpha_3$, the same in $\alpha_2$; then in $\alpha_3$. Applied to the entries of $f_j - g_j$: $f_j(\boldsymbol\alpha) = e^{-i\boldsymbol\alpha\cdot\mathbf J^{(j)}}$ for all complex $\boldsymbol\alpha$.
>
> **5. The generators.** By steps 2 and 4, $\tilde D(\Lambda_L(\omega)) = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J^{(j_+)}}\otimes e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J^{(j_-)}}$. Using $e^{A}\otimes e^{B} = (e^A\otimes\mathbb 1)(\mathbb 1\otimes e^B) = e^{A\otimes\mathbb 1}e^{\mathbb 1\otimes B}$ (as in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^der-c3-3-5|Derivation §C3.3.5]], step 1), this is $e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+}e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-}$ with $\mathbf J_\pm$ of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], which is $\exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ by [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]]. Differentiating at $\omega = 0$: the generators of $\tilde D$ are those of $(j_+, j_-)$.
>
> **6. The element −1.** $P$ is homogeneous of degree $2j$, so $(D^{(j)}(-\mathbb 1)P)(z) = P(-z) = (-1)^{2j}P(z)$; and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. Hence $\tilde D(-\mathbb 1) = (-1)^{2j_+}(-1)^{2j_-} = (-1)^{2(j_+ + j_-)}$.
>
> **7. Uniqueness.** Every $\lambda$ is $\pm\Lambda_L(\omega_1)\Lambda_L(\omega_2)$: $\pi(\lambda) = e^{\omega_1}e^{\omega_2}$ (step 1 of Derivation §C5a.4.7) $= \pi(\Lambda_L(\omega_1)\Lambda_L(\omega_2))$, and Theorem §C5a.4.5; and $-\mathbb 1 = \Lambda_L(2\pi\hat{\mathbf z})$. So the Weyl matrices generate $SL(2, \mathbb C)$, and a continuous representation is fixed by its values on them. On each one-parameter group $s \mapsto \Lambda_L(s\omega)$ these values form a one-parameter group of matrices, fixed by its derivative at $s = 0$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]]), i.e. by the generators, which step 5 identified.
>
> **8. Descending to SO⁺(1,3).** Let $j_+ + j_-$ be an integer. Then $\tilde D(-\lambda) = \tilde D(-\mathbb 1)\tilde D(\lambda) = \tilde D(\lambda)$. For $\Lambda \in SO^+(1,3)$ there is $\lambda$ with $\pi(\lambda) = \Lambda$ (Theorem §C5a.4.7), and the only other is $-\lambda$ (Theorem §C5a.4.5), so $D(\Lambda) = \tilde D(\lambda)$ is well defined. If $\pi(\lambda_k) = \Lambda_k$ then $\pi(\lambda_1\lambda_2) = \Lambda_1\Lambda_2$, so $D(\Lambda_1\Lambda_2) = \tilde D(\lambda_1\lambda_2) = D(\Lambda_1)D(\Lambda_2)$: a representation. Its value on $e^\omega = \pi(\Lambda_L(\omega))$ is $\exp(-\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ by step 5, so it is *the* representation that §C3.2 wrote down on exponentials. For $j_+ + j_-$ half an odd integer, $\tilde D(-\lambda) = -\tilde D(\lambda)$, so the two lifts of $\Lambda$ give opposite matrices, and no choice of signs gives a representation ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], 3).
>
> **9. Part 3.** By [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]] every finite-dimensional representation of the algebra is a direct sum of pieces $(j_+, j_-)$; integrate each by steps 1–5 and add. The sum descends to $SO^+(1,3)$ iff $\tilde D(-\mathbb 1) = \mathbb 1$, i.e. iff every piece has $(-1)^{2(j_+ + j_-)} = 1$.
>
> **What the derivation shows**
> - $(j_+, j_-)$ is literally $2j_+$ symmetrized left-handed slots and $2j_-$ symmetrized right-handed slots: $D^{(j)}(\lambda)$ acts by one $\lambda$ per variable $z$, as spin $j$ acts by one $U$ per slot in the rotation case.
> - The sign $(-1)^{2(j_+ + j_-)}$ of §C3.3 is the parity of the total number of spinor slots, the value of $\tilde D$ on the kernel of the covering.
> - The only analytic input is the identity theorem: the complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$ of the factorization (§C3.2) are honest complex arguments of entire functions.
> - Used next: the Dirac representation as the case $(\frac12, 0)\oplus(0, \frac12)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]); fields of every spin ([[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]]).

^der-c5a-4-8

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^der-c3-3-5|Derivation §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]]; the identity theorem for entire functions

## The group action on spinor space

> [!theorem] Theorem §C5a.4.9: The Spinor Lorentz Matrices Are Pairs of Weyl Matrices
> 1. In the chiral basis, with the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], the Dirac-representation matrices ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) are
>
> $$
> \Lambda_{1/2}(\omega) = \begin{pmatrix}\Lambda_L(\omega) & 0\\ 0 & \Lambda_R(\omega)\end{pmatrix} = \begin{pmatrix} e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma} & 0\\ 0 & e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}\end{pmatrix} .
> $$
>
> 2. $\lambda \mapsto \operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ is a representation of $SL(2, \mathbb C)$ with $\Lambda_{1/2}(\omega)$ the image of $\Lambda_L(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]); on $SO^+(1,3)$, $\Lambda_{1/2}$ is defined up to sign, a two-valued representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-14|Def. §C3.1.14]]), and a rotation by $2\pi$ gives $-\mathbb 1_4$.
> 3. Rotation by $\theta$ about $z$: $\Lambda_{1/2} = \operatorname{diag}(e^{-i\theta\sigma^3/2}, e^{-i\theta\sigma^3/2})$. Boost of rapidity $\eta$ along $x$: $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\sigma^1/2}, e^{+\eta\sigma^1/2})$, $e^{\mp\eta\sigma^1/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\sigma^1$.
>
> *Source: PS §3.2, eqs. (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts") · PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$ …") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation", Examples 1–2, eq. (spinorboost); checked numerically there), §8.2 (Derivation "How the two halves transform") · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit")*

^thm-c5a-4-9

> [!derivation]- Derivation
> **1. The exponent.** $-\frac i2\omega_{\mu\nu}S^{\mu\nu} = -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$ (the regrouping of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], linear in the generators). Inserting Theorem §C5a.3.3: $-i\boldsymbol\theta\cdot\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) - i\boldsymbol\eta\cdot(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma) = \operatorname{diag}\bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma,\ -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\bigr)$, since $-i\cdot(-\frac i2) = -\frac12$.
>
> **2. Exponentiate.** Powers of a block-diagonal matrix are block diagonal with the powers of the blocks, so $\exp\operatorname{diag}(A, B) = \operatorname{diag}(e^A, e^B)$. The blocks are $\Lambda_L(\omega)$ and $\Lambda_R(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]).
>
> **3. SL(2, C).** $\lambda \mapsto \lambda$ and $\lambda \mapsto (\lambda^\dagger)^{-1}$ are representations (Derivation §C5a.4.8, step 1), hence so is their direct sum; at $\lambda = \Lambda_L(\omega)$ it gives $\operatorname{diag}(\Lambda_L, (\Lambda_L^\dagger)^{-1}) = \operatorname{diag}(\Lambda_L, \Lambda_R) = \Lambda_{1/2}(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2). This is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]] for $(\frac12, 0)\oplus(0, \frac12)$; $j_+ + j_- = \frac12$, so the image of $-\mathbb 1$ is $-\mathbb 1_4$ and $\Lambda_{1/2}$ is two-valued on $SO^+(1,3)$.
>
> **4. Rotation about z.** $\omega_{12} = -\omega_{21} = \theta$ gives $\boldsymbol\theta = \theta\hat{\mathbf z}$, $\boldsymbol\eta = 0$ (the two terms $\frac12(\omega_{12}S^{12} + \omega_{21}S^{21}) = \theta S^{12}$), so both blocks are $e^{-i\theta\sigma^3/2} = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$. At $\theta = 2\pi$ each is $-\mathbb 1$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]), while the vector-representation matrix of the same $\omega$ is $\exp(-2\pi i\,\mathcal J^{12}) = \mathbb 1$ (the eigenvalues of $\mathcal J^{12}$ are $0, 0, \pm1$). ⚑ By-product: the same physical rotation multiplies the four spinor components by $e^{-i\theta/2}, e^{i\theta/2}, e^{-i\theta/2}, e^{i\theta/2}$: no component is left alone, unlike $V^0$, $V^3$ of a vector.
>
> **5. Boost along x.** $\omega_{01} = -\omega_{10} = \eta$ gives $\boldsymbol\eta = \eta\hat{\mathbf x}$, $\boldsymbol\theta = 0$, so the blocks are $e^{\mp\eta\sigma^1/2}$. Since $(\sigma^1)^2 = \mathbb 1$, the even terms of the series sum to $\cosh\frac\eta2\,\mathbb 1$ and the odd ones to $\mp\sinh\frac\eta2\,\sigma^1$. No $i$ appears: the blocks are Hermitian, not unitary, and stretched in opposite senses. The same $\omega$ gives in the vector representation $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\eta$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\eta$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **What the derivation shows**
> - The Dirac representation is reducible: the halves never mix under rotations or boosts. If the lower half vanishes in one frame, it vanishes in all, which could never happen for a four-vector.
> - Half the angle and half the rapidity appear in every spinor matrix ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]); entry by entry for any axis: Theorems §C5a.4.13–§C5a.4.14 below.
> - Used next: boosting rest-frame spinors ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|Theorem §C5a.9.8]]); the Weyl form of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]).

^der-c5a-4-9

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

> [!remark] Remark: One transformation, two matrices
> One Lorentz transformation is six numbers $\omega_{\mu\nu}$; the vector and the Dirac representation exponentiate them with different generators:
>
> | | four-vector $A^\mu$ | Dirac spinor $\psi_a$ |
> |---|---|---|
> | components label | a direction, $\mu = 0, \dots, 3$ | a component of $\mathbb C^4$; no direction |
> | generators | $(\mathcal J^{\mu\nu})^\alpha{}_\beta$ | $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, same algebra |
> | matrix | $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, real | $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$, complex |
> | rotation by $\theta$ about $z$ | $\cos\theta$, $\sin\theta$ in the $(1, 2)$ block | phases $e^{\mp i\theta/2}$: half the angle |
> | boost by $\eta$ along $x$ | $\cosh\eta$, $\sinh\eta$ | $\cosh\frac\eta2 \mp \sigma^1\sinh\frac\eta2$, opposite in the halves |
> | invariant form | $g$: $\Lambda^{\mathsf T}g\Lambda = g$ | $\gamma^0$: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1\|Theorem §C5a.6.1]]) |
> | rotation by $2\pi$ | $+\mathbb 1$ | $-\mathbb 1$ |
> | fixed by $\Lambda$? | yes | up to sign: a representation of $SL(2, \mathbb C)$ |
>
> Both matrices are $4\times4$ for unrelated reasons: $\Lambda$ because spacetime has four dimensions, $\Lambda_{1/2}$ because the Clifford algebra needs four components (Theorem §C5a.1.6). Relations such as $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ hold only for a matched pair built from the same $\omega$ (checked numerically in the user's notes, matched and mismatched). This is why the lecture calls $\psi$ a four-component *column*, not a four-vector. Both matrices written out entry by entry, for rotations about and boosts along any axis: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-14|Theorem §C5a.4.14]] (vector side: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]); one rotation and one boost side by side, with the generators and the check of $\gamma^\mu$ entry by entry: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation": "One transformation, two representations"; Derivation "From six numbers to two matrices"; Principle "Transforming as a vector and as a spinor, side by side"; paragraph "Same dimension, different representation")*

^rem-c5a-4-2

> [!theorem] Theorem §C5a.4.10: The Dirac Representation Is Not the Vector Representation
> The Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) and the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) are both four-dimensional, but they are inequivalent ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-7|Def. §C3.1.7]]); these are the two tests of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^rem-c3-3-2|§C3.3, Remark: Sums versus products]]:
> 1. on the Dirac representation the Casimirs ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]) are $\mathbf J_+^2 = \operatorname{diag}(\frac34, \frac34, 0, 0)$ and $\mathbf J_-^2 = \operatorname{diag}(0, 0, \frac34, \frac34)$, on the vector representation $\mathbf J_\pm^2 = \frac34\mathbb 1$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4|Theorem §C3.3.4]]);
> 2. a rotation by $2\pi$ is $-\mathbb 1$ on Dirac spinors and $+\mathbb 1$ on four-vectors;
> 3. under rotations the Dirac spinor is spin $\frac12\oplus\frac12$, the vector spin $0\oplus1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Same dimension, different representation"), §8.2 (Derivation "… related by conjugation", paragraph "Why the Dirac spinor is not (½, ½)"; checked numerically there) · PHY 513 Lecture 7, Part B ("Unlike a 4-vector under rotation: spin-0 (time) and spin-1 (space)")*

^thm-c5a-4-10

> [!derivation]- Derivation
> **1. Casimirs.** By Theorem §C5a.3.4, $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, so $\mathbf J_+^2 = \frac14\operatorname{diag}(\boldsymbol\sigma\cdot\boldsymbol\sigma, 0) = \frac14\operatorname{diag}(3\cdot\mathbb 1, 0)$ ($\sigma_k^2 = \mathbb 1$ for each $k$); likewise $\mathbf J_-^2$. On the vector representation both are $\frac34\mathbb 1$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4|Theorem §C3.3.4]]). An equivalence $D_{\rm Dirac} = UD_{\rm vec}U^{-1}$ would give $\mathbf J_+^2|_{\rm Dirac} = U\frac34\mathbb 1U^{-1} = \frac34\mathbb 1$: false.
>
> **2. 2π rotation.** Theorem §C5a.4.9, step 4: $-\mathbb 1_4$ against $+\mathbb 1_4$; an equivalence maps $+\mathbb 1$ to $+\mathbb 1$.
>
> **3. Rotation content.** $\mathbf J = \frac12\boldsymbol\Sigma$ is spin ½ on each block; on the vector, $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$ (Theorem §C3.3.4): spin $0$ on $v^0$, spin $1$ on $\mathbf v$.
>
> **What the derivation shows**
> - In the Dirac spinor no component feels both copies $\mathbf J_\pm$ (a direct sum, $2 + 2$); in the vector every component feels both (a product, $2\times2$). The equality of dimensions is a coincidence of four dimensions ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|Remark: What each Dirac index labels]]).

^der-c5a-4-10

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4|Theorem §C3.3.4]]

## γ^μ carries a vector index

> [!theorem] Theorem §C5a.4.11: The Dirac Matrices Are an Invariant Vector of Matrices
> For $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) and $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) built from the same $\omega$:
> 1. $\Lambda_{1/2}^{-1}\,\gamma^\mu\,\Lambda_{1/2} = \Lambda^\mu{}_\nu\,\gamma^\nu$;
> 2. $\Lambda_{1/2}^{-1}S^{\mu\nu}\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma S^{\rho\sigma}$, $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = (\Lambda^{-1})^\nu{}_\mu\gamma_\nu$, and $\Lambda_{1/2}^{-1}\mathbb 1\Lambda_{1/2} = \mathbb 1$;
> 3. in the chiral basis, with the Weyl matrices and $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] and [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]], $\Lambda_L^{-1}\sigma^\mu\Lambda_R = \Lambda^\mu{}_\nu\sigma^\nu$ and $\Lambda_R^{-1}\bar\sigma^\mu\Lambda_L = \Lambda^\mu{}_\nu\bar\sigma^\nu$.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The covariance of $\gamma^\mu$: finite transformations", eq. (gammacov), with its second proof and corollaries) · Yu §5.1, eqs. (5.17)–(5.31) · the user's pre-course notes, §5.1, eq. (gamma-vector)*

^thm-c5a-4-11

> [!derivation]- Derivation
> Let $A = -\frac i2\omega_{\rho\sigma}S^{\rho\sigma}$, so $\Lambda_{1/2} = e^A$, and recall $-\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu = \omega^\mu{}_\nu$, so $\Lambda = e^{\omega}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]]).
>
> **1. The infinitesimal statement.** By Theorem §C5a.3.1, $[\gamma^\mu, A] = -\frac i2\omega_{\rho\sigma}[\gamma^\mu, S^{\rho\sigma}] = -\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\nu\gamma^\nu$.
>
> **2. Two curves.** For $t \in [0, 1]$ put $F^\mu(t) = e^{-tA}\gamma^\mu e^{tA}$ and $G^\mu(t) = (e^{t\omega})^\mu{}_\nu\gamma^\nu$, four matrices each; $F^\mu(0) = G^\mu(0) = \gamma^\mu$.
>
> **3. The same linear equation.** $\frac{d}{dt}F^\mu = e^{-tA}(-A\gamma^\mu + \gamma^\mu A)e^{tA} = e^{-tA}[\gamma^\mu, A]e^{tA} = \omega^\mu{}_\nu e^{-tA}\gamma^\nu e^{tA} = \omega^\mu{}_\nu F^\nu$, by step 1 (the numbers $\omega^\mu{}_\nu$ pass through $e^{\pm tA}$). And $\frac{d}{dt}G^\mu = (\omega e^{t\omega})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\kappa G^\kappa$.
>
> **4. Uniqueness.** The difference $D^\mu = F^\mu - G^\mu$ obeys $\dot D^\mu = \omega^\mu{}_\nu D^\nu$, $D^\mu(0) = 0$. Then $\frac{d}{dt}\bigl[(e^{-t\omega})^\kappa{}_\mu D^\mu(t)\bigr] = -(e^{-t\omega}\omega)^\kappa{}_\mu D^\mu + (e^{-t\omega})^\kappa{}_\mu\omega^\mu{}_\nu D^\nu = 0$ ($\omega$ commutes with $e^{-t\omega}$), so $(e^{-t\omega})^\kappa{}_\mu D^\mu(t) = 0$ for all $t$; multiplying by $e^{t\omega}$, $D \equiv 0$. At $t = 1$: $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$.
>
> **5. Part 2.** $\Lambda_{1/2}^{-1}[\gamma^\mu, \gamma^\nu]\Lambda_{1/2} = [\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}, \Lambda_{1/2}^{-1}\gamma^\nu\Lambda_{1/2}]$ (insert $\Lambda_{1/2}\Lambda_{1/2}^{-1}$ between the factors) $= \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma[\gamma^\rho, \gamma^\sigma]$; times $\frac i4$ this is the law for $S$. For the lower index, $\gamma_\mu = g_{\mu\nu}\gamma^\nu$ gives $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = g_{\mu\nu}\Lambda^\nu{}_\rho g^{\rho\kappa}\gamma_\kappa$, and $\Lambda^{\mathsf T}g\Lambda = g$ means $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\kappa{}_\mu = g^{\kappa\rho}\Lambda^\nu{}_\rho g_{\nu\mu}$, which is the coefficient found.
>
> **6. Part 3.** In the chiral basis $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ (Theorem §C5a.4.9), and block multiplication gives $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \begin{pmatrix}0 & \Lambda_L^{-1}\sigma^\mu\Lambda_R\\ \Lambda_R^{-1}\bar\sigma^\mu\Lambda_L & 0\end{pmatrix}$; compare the blocks of part 1. Since $\Lambda_L^{-1} = \Lambda_R^\dagger$ and $\Lambda_R^{-1} = \Lambda_L^\dagger$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2), these are the invariance statements of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], 2, obtained here independently.
>
> **What the derivation shows**
> - Transforming the two spinor indices of $\gamma^\mu$ is the same as transforming its vector index: $\gamma^\mu$ is an invariant tensor with one vector slot and two spinor slots, as $g_{\mu\nu}$ is with two vector slots. "Take the vector index on $\gamma^\mu$ seriously" (PS): $\gamma^\mu\partial_\mu$ is a Lorentz-invariant operator on spinors ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]), and $\bar\psi\gamma^\mu\psi$ a vector ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]).
> - Part 2 for $S$ is the general law "the generators transform as a tensor" ([[§C3.2 The Lorentz Algebra#^thm-c3-2-2|Theorem §C3.2.2]]) for the Dirac representation.
> - Only the matched pair works: $\Lambda$ and $\Lambda_{1/2}$ from the same six numbers. The two-valuedness of $\Lambda_{1/2}$ is invisible here, since $\pm\Lambda_{1/2}$ give the same conjugation.

^der-c5a-4-11

> [!derivation]- Derivation (second route: the nested-commutator series)
> **1. The series.** For matrices $A$, $B$ define $[B, A]_{(0)} = B$, $[B, A]_{(n+1)} = [[B, A]_{(n)}, A]$. The function $f(t) = e^{-tA}Be^{tA}$ satisfies $f'(t) = e^{-tA}[B, A]e^{tA}$ (as in step 3 above), and by induction $f^{(n)}(t) = e^{-tA}[B, A]_{(n)}e^{tA}$; $f$ is entire in $t$ (products of exponential series), so its Taylor series at $0$ converges at $t = 1$: $e^{-A}Be^A = \sum_{n\ge0}\frac1{n!}[B, A]_{(n)}$ (Yu (5.23), proved there by the binomial rearrangement (5.18)–(5.22)).
>
> **2. Iterate step 1 of the first route.** $[\gamma^\mu, A]_{(1)} = \omega^\mu{}_\nu\gamma^\nu$; if $[\gamma^\mu, A]_{(n)} = (\omega^n)^\mu{}_\nu\gamma^\nu$, then $[\gamma^\mu, A]_{(n+1)} = (\omega^n)^\mu{}_\nu[\gamma^\nu, A] = (\omega^n)^\mu{}_\nu\omega^\nu{}_\kappa\gamma^\kappa = (\omega^{n+1})^\mu{}_\kappa\gamma^\kappa$.
>
> **3. Sum.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \sum_n\frac1{n!}(\omega^n)^\mu{}_\nu\gamma^\nu = (e^\omega)^\mu{}_\nu\gamma^\nu = \Lambda^\mu{}_\nu\gamma^\nu$ (Yu (5.25)–(5.27)).
>
> *What this route shows:* the finite law is the infinitesimal one summed to all orders, term by term; the first route reaches it through uniqueness for a linear differential equation instead.

^der-c5a-4-11b

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]]

> [!remark] Remark: The lecture's form of the covariance
> Lecture 8 writes $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$, the infinitesimal version $(1 - \frac i2\omega S)\gamma^\mu(1 + \frac i2\omega S) = (1 + \frac i2\omega\mathcal J)^\mu{}_\nu\gamma^\nu$, and then $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$. All three are Theorem §C5a.4.11 with $\omega \to -\omega$ ($\Lambda_{1/2}(-\omega) = \Lambda_{1/2}^{-1}$, $e^{-\omega} = \Lambda^{-1}$), and Peskin–Schroeder's infinitesimal form is the same with the opposite sign of $\omega$. The last form carries the slide's message: "$\gamma^\nu$ are just numbers. They do not transform!" — transforming the vector index and both spinor indices at once returns the same matrices. That is what "invariant tensor" means, and why $\gamma^\nu\psi$ transforms as a spinor and a vector at once, $\gamma^\nu\psi \to \Lambda^\nu{}_\mu\Lambda_{1/2}(\gamma^\mu\psi)$.
>
> *Source: PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · PS §3.2, p. 42 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"), §8.1 (Definition "What 'transforms like a spinor' means")*

^rem-c5a-4-3

> [!definition] Definition §C5a.4.4: Clifford Multiplication
> Let $M = \mathbb R^{1,3}$ be Minkowski space with metric $g$ ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]]). **Clifford multiplication** is the map
>
> $$
> M\times V \to V, \qquad (a, \psi) \mapsto \slashed{a}\,\psi \equiv a_\mu\Gamma^\mu\psi, \qquad a_\mu = g_{\mu\nu}a^\nu ,
> $$
>
> with the Dirac maps $\Gamma^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-9|Def. §C5a.1.9]]; the slash notation is introduced with the Dirac equation, [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]). It is linear in $a$ and in $\psi$, and $\slashed{a}\,\slashed{a}\,\psi = (a\cdot a)\,\psi$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], 2). As a tensor, $\Gamma = (\Gamma^\mu) \in M\otimes\operatorname{End}(V) \cong M\otimes V\otimes V'$, with components $(\gamma^\mu)_{ab}$: one Minkowski slot $\mu$, one $V$-slot $a$, one $V'$-slot $b$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-6|Def. §C5a.1.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "$\gamma^\mu$ is an invariant tensor with one spacetime slot and two spinor slots") · PS §3.2, p. 42 · the name and the map formulation written here*

^def-c5a-4-4

> [!theorem] Theorem §C5a.4.12: Clifford Multiplication Is Lorentz Equivariant
> Let $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ be built from the same $\omega$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]). Then, for Clifford multiplication ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]):
> 1. $\Lambda_{1/2}\bigl(\slashed{a}\,\psi\bigr) = \slashed{(\Lambda a)}\,\bigl(\Lambda_{1/2}\psi\bigr)$ for all $a \in M$, $\psi \in V$: moving the vector and the spinor together moves their product;
> 2. equivalently, transforming all three slots of $\gamma^\mu$ returns it: $\Lambda^\mu{}_\nu\,\Lambda_{1/2}\,\gamma^\nu\,\Lambda_{1/2}^{-1} = \gamma^\mu$.
>
> Both are the covariance of $\gamma^\mu$, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]]), read as a statement about an intertwiner $M\otimes V \to V$ for the Lorentz group.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots") · the equivariance form written here*

^thm-c5a-4-12

> [!derivation]- Derivation
> **1. Conjugate the slash.** $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = (\Lambda a)_\mu\,\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}$ (the numbers $(\Lambda a)_\mu$ pull out) $= (\Lambda a)_\mu\,\Lambda^\mu{}_\nu\gamma^\nu$ (Theorem §C5a.4.11, 1).
>
> **2. Lower the index explicitly.** $(\Lambda a)_\mu = g_{\mu\rho}\Lambda^\rho{}_\sigma a^\sigma$, so the coefficient of $\gamma^\nu$ is $g_{\mu\rho}\Lambda^\rho{}_\sigma\Lambda^\mu{}_\nu\,a^\sigma = g_{\sigma\nu}a^\sigma = a_\nu$, by the defining property $g_{\mu\rho}\Lambda^\mu{}_\nu\Lambda^\rho{}_\sigma = g_{\nu\sigma}$ of a Lorentz transformation ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]). Hence $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = a_\nu\gamma^\nu = \slashed{a}$.
>
> **3. Part 1.** Multiply step 2 on the left by $\Lambda_{1/2}$ and apply to $\psi$: $\slashed{(\Lambda a)}\,\Lambda_{1/2}\psi = \Lambda_{1/2}\,\slashed{a}\,\psi$.
>
> **4. Part 2.** From Theorem §C5a.4.11, 1, multiply on the left by $\Lambda_{1/2}$ and on the right by $\Lambda_{1/2}^{-1}$: $\gamma^\mu = \Lambda_{1/2}\,\Lambda^\mu{}_\nu\gamma^\nu\,\Lambda_{1/2}^{-1} = \Lambda^\mu{}_\nu\,\Lambda_{1/2}\gamma^\nu\Lambda_{1/2}^{-1}$. The three factors are the slot rules: $\Lambda$ on the Minkowski index, $\Lambda_{1/2}$ on the $V$-index (left), $\Lambda_{1/2}^{-1}$ on the $V'$-index (right) — the slot rule of Theorem §C5a.1.3 with the Lorentz matrices in place of $U$. This is the lecture's form $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-3|§C5a.4, Remark: The lecture's form of the covariance]]).
>
> **What the derivation shows**
> - Clifford multiplication is a map between representations of the Lorentz group (vector ⊗ Dirac → Dirac) that commutes with the group action; such a map is an intertwiner, and its components $(\gamma^\mu)_{ab}$ are an invariant tensor. This is why a $\gamma$ matrix never acquires a transformation of its own under a Lorentz transformation.
> - Assumption used: $\Lambda$ and $\Lambda_{1/2}$ come from the same $\omega$, i.e. $\Lambda$ is the image of $\Lambda_{1/2}$ under the covering map $SL(2, \mathbb C) \to SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]); for a mismatched pair the identity fails ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|§C5a.4, Remark: One transformation, two matrices]]).
> - Used next: covariance of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]) is part 1 applied to $a = \partial$.

^der-c5a-4-12

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-3|Theorem §C5a.1.3]]

> [!remark] Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis
> $\gamma^\mu$ has three slots: Minkowski, $V$, $V'$. A **Lorentz transformation** acts on all of them at once — $\Lambda$ on the Minkowski slot, $\Lambda_{1/2}$ and $\Lambda_{1/2}^{-1}$ on the spinor slots — and returns the same array (Theorem §C5a.4.12, 2): "$\gamma^\nu$ are just numbers. They do not transform!" (Lecture 8). What transforms is $\psi$, and $\partial_\mu$ with it, and the equation keeps its form. A **change of basis of $V$** acts only on the spinor slots, with one $U$ and its inverse; the Minkowski slot is untouched because no basis of spacetime changes. Nothing compensates, so the array changes: $\gamma' = U\gamma U^{-1}$ (Theorem §C5a.1.7). In short, the Lorentz group acts on spacetime *and* spinor space and $\gamma$ is invariant under the combined action; $GL(V)$ acts on spinor space alone and $\gamma$ is merely covariant under it.
>
> *Source: PHY 513 Lecture 8, Part A (slide "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 · the comparison written here*

^rem-c5a-4-4

## The matrices entry by entry

Theorem §C5a.4.9 gives $\Lambda_{1/2}$ as a pair of $2\times2$ exponentials. Here the rotations and boosts about and along an arbitrary axis are written as full $4\times4$ matrices in the chiral basis, next to the vector matrices of the same parameters ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]), and the covariance of $\gamma^\mu$ (Theorem §C5a.4.11) is checked entry by entry. Throughout, $\hat{\mathbf n} = (n^1, n^2, n^3)$ is a unit vector and

$$
\hat{\mathbf n}\cdot\boldsymbol\sigma = \begin{pmatrix} n^3 & n^1 - in^2 \\ n^1 + in^2 & -n^3 \end{pmatrix} .
$$

> [!theorem] Theorem §C5a.4.13: The Rotation Matrices in the Dirac Representation, Entry by Entry
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), with the rotation generators $J_k = \frac12\Sigma^k$ ([[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]) and the parameters of the vector rotations in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]:
> 1. **Rotation about $z$** by $\theta$: $\Lambda_{1/2} = e^{-i\theta J_3} = \operatorname{diag}\bigl(e^{-i\theta/2}, e^{i\theta/2}, e^{-i\theta/2}, e^{i\theta/2}\bigr)$.
> 2. **Rotation about** $\hat{\mathbf n}$ by $\theta$, with $c = \cos\frac\theta2$, $s = \sin\frac\theta2$:
>
> $$
> \Lambda_{1/2} = e^{-i\theta\,\hat{\mathbf n}\cdot\mathbf J} = \begin{pmatrix} U & 0 \\ 0 & U \end{pmatrix}, \quad U = e^{-i\theta\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = c\,\mathbb 1 - is\,\hat{\mathbf n}\cdot\boldsymbol\sigma, \quad \Lambda_{1/2} = \begin{pmatrix} c - isn^3 & -is(n^1 - in^2) & 0 & 0 \\ -is(n^1 + in^2) & c + isn^3 & 0 & 0 \\ 0 & 0 & c - isn^3 & -is(n^1 - in^2) \\ 0 & 0 & -is(n^1 + in^2) & c + isn^3 \end{pmatrix} .
> $$
>
> The two blocks are equal and $U \in SU(2)$, so $\Lambda_{1/2}$ is unitary; $U$ is the spin-½ rotation of [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]. At $\theta = 2\pi$, $\Lambda_{1/2} = -\mathbb 1_4$; at $\theta = 4\pi$, $\Lambda_{1/2} = +\mathbb 1_4$.
>
> *Source: PS §3.2, eq. (3.37) (infinitesimal) · PHY 513 Lecture 7, Part B (slide "Spinors and Rotation") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation", Example 1: rotation about $z$) · Sakurai §3.2.5, eqs. (3.60)–(3.63), as in QM §C5.2 (the $2\times2$ block) · the $4\times4$ matrix about $\hat{\mathbf n}$ written here (checked numerically)*

^thm-c5a-4-13

> [!derivation]- Derivation
> **1. The exponent.** By Theorem §C5a.4.9, step 1, with $\boldsymbol\theta = \theta\hat{\mathbf n}$ and $\boldsymbol\eta = 0$: $-i\theta\,\hat{\mathbf n}\cdot\mathbf J = -i\theta\,n^k\cdot\frac12\operatorname{diag}(\sigma^k, \sigma^k) = \operatorname{diag}\bigl(-\frac{i\theta}2\hat{\mathbf n}\cdot\boldsymbol\sigma,\ -\frac{i\theta}2\hat{\mathbf n}\cdot\boldsymbol\sigma\bigr)$. The exponential of a block-diagonal matrix is block diagonal with the exponentials of the blocks (Derivation §C5a.4.9, step 2), so $\Lambda_{1/2} = \operatorname{diag}(U, U)$ with $U = e^{-i\theta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$.
>
> **2. The square of the axis matrix.** Multiplying out with the displayed $\hat{\mathbf n}\cdot\boldsymbol\sigma$:
>
> $$
> (\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \begin{pmatrix} (n^3)^2 + (n^1 - in^2)(n^1 + in^2) & n^3(n^1 - in^2) - (n^1 - in^2)n^3 \\ (n^1 + in^2)n^3 - n^3(n^1 + in^2) & (n^1 + in^2)(n^1 - in^2) + (n^3)^2 \end{pmatrix} = \begin{pmatrix} |\hat{\mathbf n}|^2 & 0 \\ 0 & |\hat{\mathbf n}|^2 \end{pmatrix} = \mathbb 1 ,
> $$
>
> using $(n^1 - in^2)(n^1 + in^2) = (n^1)^2 + (n^2)^2$ (the same as [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 3, with $\mathbf a = \mathbf b = \hat{\mathbf n}$).
>
> **3. The series, for any complex number a.** By step 2, $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^{2k} = \mathbb 1$ and $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^{2k+1} = \hat{\mathbf n}\cdot\boldsymbol\sigma$, so splitting the exponential series into even and odd terms,
>
> $$
> e^{a\,\hat{\mathbf n}\cdot\boldsymbol\sigma} = \Bigl(\sum_{k\ge0}\frac{a^{2k}}{(2k)!}\Bigr)\mathbb 1 + \Bigl(\sum_{k\ge0}\frac{a^{2k+1}}{(2k+1)!}\Bigr)\hat{\mathbf n}\cdot\boldsymbol\sigma = \cosh a\,\mathbb 1 + \sinh a\,\hat{\mathbf n}\cdot\boldsymbol\sigma .
> $$
>
> (This step is used again, with real $a$, for the boosts: Theorem §C5a.4.14.)
>
> **4. Imaginary a (part 2).** For $a = -\frac{i\theta}2$: $\cosh(-\frac{i\theta}2) = \cos\frac\theta2 = c$ and $\sinh(-\frac{i\theta}2) = -i\sin\frac\theta2 = -is$ (from $\cosh ix = \cos x$, $\sinh ix = i\sin x$ and the parity of $\cosh$, $\sinh$). So $U = c\,\mathbb 1 - is\,\hat{\mathbf n}\cdot\boldsymbol\sigma$; inserting the entries of $\hat{\mathbf n}\cdot\boldsymbol\sigma$ gives $U_{11} = c - isn^3$, $U_{12} = -is(n^1 - in^2)$, $U_{21} = -is(n^1 + in^2)$, $U_{22} = c + isn^3$, placed in both diagonal blocks.
>
> **5. About z (part 1).** For $\hat{\mathbf n} = \hat{\mathbf z}$, $\hat{\mathbf n}\cdot\boldsymbol\sigma = \sigma^3 = \operatorname{diag}(1, -1)$, so $U = \operatorname{diag}(c - is, c + is) = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$ (Euler's formula), in both blocks.
>
> **6. Unitary, unit determinant.** $U^\dagger = c\,\mathbb 1 + is\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ ($\hat{\mathbf n}\cdot\boldsymbol\sigma$ is Hermitian), and all four terms of $U^\dagger U = c^2\,\mathbb 1 - ics\,\hat{\mathbf n}\cdot\boldsymbol\sigma + ics\,\hat{\mathbf n}\cdot\boldsymbol\sigma + s^2(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = (c^2 + s^2)\mathbb 1 = \mathbb 1$. $\det U = (c - isn^3)(c + isn^3) - (-is)^2(n^1 - in^2)(n^1 + in^2) = c^2 + s^2(n^3)^2 + s^2\bigl((n^1)^2 + (n^2)^2\bigr) = c^2 + s^2 = 1$. So $U \in SU(2)$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]]), as [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 4, says for every rotation.
>
> **7. 2π and 4π.** At $\theta = 2\pi$: $c = \cos\pi = -1$, $s = \sin\pi = 0$, so $U = -\mathbb 1$ and $\Lambda_{1/2} = -\mathbb 1_4$, while the vector matrix of the same parameters is $\mathbb 1$ (Theorem §C1a.6.6). At $\theta = 4\pi$: $c = \cos2\pi = 1$, $s = 0$, and $\Lambda_{1/2} = \mathbb 1_4$.
>
> **What the derivation shows**
> - Every entry is a function of $\theta/2$: the rotation generators have eigenvalues $\pm\frac12$ where the vector ones have $\pm1, 0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). Hence the period $4\pi$, and $-\mathbb 1_4$ at $2\pi$: the Dirac representation is a spinor representation ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]).
> - The two Weyl halves rotate by the same unitary $U$, because $J_k$ is the same in both blocks: rotations cannot tell $\psi_L$ from $\psi_R$; only boosts can (Theorem §C5a.4.14).
> - Used next: the side-by-side comparison and the $\gamma$ check (Example §C5a.4.1).

^der-c5a-4-13

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]

> [!example] Example §C5a.4.1: One Rotation, Two Matrices
> Take the rotation by $\theta$ about $z$, $\omega_{12} = -\omega_{21} = \theta$, and compare its two matrices: the vector one ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]) and the Dirac one ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]]), and their generators $J_3$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]).
>
> *Generators* (vector left, spinor right):
>
> $$
> J_3^{\rm vec} = \begin{pmatrix} 0&0&0&0\\ 0&0&-i&0\\ 0&i&0&0\\ 0&0&0&0 \end{pmatrix}\ \text{(eigenvalues } 1, -1, 0, 0\text{)}, \qquad J_3^{\rm Dirac} = \frac12\begin{pmatrix} 1&0&0&0\\ 0&-1&0&0\\ 0&0&1&0\\ 0&0&0&-1 \end{pmatrix}\ \text{(eigenvalues } \tfrac12, -\tfrac12, \tfrac12, -\tfrac12\text{)} .
> $$
>
> *Matrices*, for general $\theta$ and for $\theta = \frac\pi2$ ($e^{\mp i\pi/4} = (1 \mp i)/\sqrt2$):
>
> $$
> R_z(\theta) = \begin{pmatrix} 1&0&0&0\\ 0&\cos\theta&-\sin\theta&0\\ 0&\sin\theta&\cos\theta&0\\ 0&0&0&1 \end{pmatrix}, \quad \Lambda_{1/2} = \begin{pmatrix} e^{-i\theta/2}&0&0&0\\ 0&e^{i\theta/2}&0&0\\ 0&0&e^{-i\theta/2}&0\\ 0&0&0&e^{i\theta/2} \end{pmatrix}; \qquad R_z(\tfrac\pi2) = \begin{pmatrix} 1&0&0&0\\ 0&0&-1&0\\ 0&1&0&0\\ 0&0&0&1 \end{pmatrix}, \quad \Lambda_{1/2} = \frac1{\sqrt2}\begin{pmatrix} 1-i&0&0&0\\ 0&1+i&0&0\\ 0&0&1-i&0\\ 0&0&0&1+i \end{pmatrix} .
> $$
>
> *Reading.* An eigenvalue $m$ of $J_3$ becomes the phase $e^{-im\theta}$: $m = \pm1, 0$ gives entries in $\theta$ (and the untouched $t$, $z$), $m = \pm\frac12$ gives entries in $\theta/2$, and no spinor component is left alone. At $\theta = 2\pi$ the vector matrix is $\mathbb 1$ ($e^{\mp2\pi i} = e^0 = 1$) and the spinor matrix is $-\mathbb 1_4$ ($e^{\mp i\pi} = -1$): the vector representation is a tensor representation and the Dirac representation a spinor representation ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]). At $\theta = 4\pi$ both are $\mathbb 1$. The algebra is the same, $[J_1, J_2] = iJ_3$ in both, and the matched pair satisfies $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ with $\Lambda = R_z(\theta)$: at $\theta = \frac\pi2$, $\Lambda_{1/2}^{-1}\gamma^1\Lambda_{1/2} = -\gamma^2$ and $\Lambda_{1/2}^{-1}\gamma^2\Lambda_{1/2} = \gamma^1$ (derivation below).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Principle "Transforming as a vector and as a spinor, side by side"; Example 1), Ch. 7 §7.3 (Derivation "What the vector generators do") · PHY 513 Lecture 7, Part B ("Unlike a 4-vector under rotation") · PS §3.1, eq. (3.20), §3.2, eq. (3.37) · the side-by-side matrices and the entry-by-entry checks written here (checked numerically)*

^ex-c5a-4-1

> [!derivation]- Derivation (the commutator and the covariance of γ, entry by entry)
> $E_{AB}$ is the matrix with $1$ in row $A$, column $B$; $E_{AB}E_{CD} = \delta_{BC}E_{AD}$. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]), rows and columns $A, B = 1, \dots, 4$,
>
> $$
> \gamma^0 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&1\\ 1&0&0&0\\ 0&1&0&0 \end{pmatrix}, \quad \gamma^1 = \begin{pmatrix} 0&0&0&1\\ 0&0&1&0\\ 0&-1&0&0\\ -1&0&0&0 \end{pmatrix}, \quad \gamma^2 = \begin{pmatrix} 0&0&0&-i\\ 0&0&i&0\\ 0&i&0&0\\ -i&0&0&0 \end{pmatrix}, \quad \gamma^3 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&-1\\ -1&0&0&0\\ 0&1&0&0 \end{pmatrix} .
> $$
>
> **1. [J₁, J₂] = iJ₃ for the vector.** In spacetime matrix units (rows and columns $0, \dots, 3$), $J_1 = -iE_{23} + iE_{32}$, $J_2 = iE_{13} - iE_{31}$, $J_3 = -iE_{12} + iE_{21}$ (Theorem §C1a.6.5). All four products:
>
> $$
> J_1J_2 = (-i)(i)E_{23}E_{13} + (-i)(-i)E_{23}E_{31} + (i)(i)E_{32}E_{13} + (i)(-i)E_{32}E_{31} = 0 - E_{21} + 0 + 0, \qquad J_2J_1 = (i)(-i)E_{13}E_{23} + (i)(i)E_{13}E_{32} + (-i)(-i)E_{31}E_{23} + (-i)(i)E_{31}E_{32} = 0 - E_{12} + 0 + 0 .
> $$
>
> So $[J_1, J_2] = E_{12} - E_{21}$, and $iJ_3 = i(-iE_{12} + iE_{21}) = E_{12} - E_{21}$: equal.
>
> **2. [J₁, J₂] = iJ₃ for the spinor.** $J_k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$, so $[J_1, J_2] = \frac14\operatorname{diag}([\sigma^1, \sigma^2], [\sigma^1, \sigma^2])$. With $\sigma^1\sigma^2 = \begin{pmatrix} 0&1\\ 1&0 \end{pmatrix}\begin{pmatrix} 0&-i\\ i&0 \end{pmatrix} = \begin{pmatrix} i&0\\ 0&-i \end{pmatrix} = i\sigma^3$ and $\sigma^2\sigma^1 = \begin{pmatrix} -i&0\\ 0&i \end{pmatrix} = -i\sigma^3$: $[\sigma^1, \sigma^2] = 2i\sigma^3$, and $[J_1, J_2] = \frac14\operatorname{diag}(2i\sigma^3, 2i\sigma^3) = i\cdot\frac12\Sigma^3 = iJ_3$. Same relation ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]), different matrices.
>
> **3. Conjugating by a diagonal matrix.** $\Lambda_{1/2} = D = \operatorname{diag}(\alpha, \bar\alpha, \alpha, \bar\alpha)$ with $\alpha = e^{-i\theta/2}$, and $D^{-1} = \operatorname{diag}(\bar\alpha, \alpha, \bar\alpha, \alpha)$. For any matrix $X$, $(D^{-1}XD)_{AB} = (D^{-1})_{AA}\,X_{AB}\,D_{BB}$: each entry is multiplied by a factor $f_{AB}$. The $\gamma$'s have entries only at the positions $(1,3), (2,4), (3,1), (4,2)$ ($\gamma^0$, $\gamma^3$) and $(1,4), (2,3), (3,2), (4,1)$ ($\gamma^1$, $\gamma^2$), where
>
> $$
> f_{13} = \bar\alpha\alpha = 1,\ f_{24} = \alpha\bar\alpha = 1,\ f_{31} = 1,\ f_{42} = 1; \qquad f_{14} = \bar\alpha\bar\alpha = e^{i\theta},\ f_{23} = \alpha\alpha = e^{-i\theta},\ f_{32} = e^{i\theta},\ f_{41} = e^{-i\theta} .
> $$
>
> **4. μ = 0 and μ = 3.** All factors are $1$: $\Lambda_{1/2}^{-1}\gamma^0\Lambda_{1/2} = \gamma^0$ and $\Lambda_{1/2}^{-1}\gamma^3\Lambda_{1/2} = \gamma^3$. The vector side: row $0$ of $R_z(\theta)$ is $(1, 0, 0, 0)$ and row $3$ is $(0, 0, 0, 1)$, so $\Lambda^0{}_\nu\gamma^\nu = \gamma^0$, $\Lambda^3{}_\nu\gamma^\nu = \gamma^3$. Equal.
>
> **5. μ = 1.** Left side, entries of $\gamma^1$ times the factors: $(1,4)$: $e^{i\theta}$; $(2,3)$: $e^{-i\theta}$; $(3,2)$: $-e^{i\theta}$; $(4,1)$: $-e^{-i\theta}$. Right side, row $1$ of $R_z(\theta)$: $\Lambda^1{}_\nu\gamma^\nu = \cos\theta\,\gamma^1 - \sin\theta\,\gamma^2$, with entries $(1,4)$: $\cos\theta - \sin\theta(-i) = e^{i\theta}$; $(2,3)$: $\cos\theta - i\sin\theta = e^{-i\theta}$; $(3,2)$: $-\cos\theta - i\sin\theta = -e^{i\theta}$; $(4,1)$: $-\cos\theta - \sin\theta(-i) = -e^{-i\theta}$. Equal.
>
> **6. μ = 2.** Left side: $(1,4)$: $-ie^{i\theta}$; $(2,3)$: $ie^{-i\theta}$; $(3,2)$: $ie^{i\theta}$; $(4,1)$: $-ie^{-i\theta}$. Right side, row $2$: $\Lambda^2{}_\nu\gamma^\nu = \sin\theta\,\gamma^1 + \cos\theta\,\gamma^2$, entries $(1,4)$: $\sin\theta - i\cos\theta = -ie^{i\theta}$; $(2,3)$: $\sin\theta + i\cos\theta = ie^{-i\theta}$; $(3,2)$: $-\sin\theta + i\cos\theta = ie^{i\theta}$; $(4,1)$: $-\sin\theta - i\cos\theta = -ie^{-i\theta}$. Equal.
>
> **7. θ = π/2 and θ = 2π.** At $\theta = \frac\pi2$, $e^{\pm i\theta} = \pm i$, and step 5 gives entries $i, -i, -i, i$ at $(1,4), (2,3), (3,2), (4,1)$, which are those of $-\gamma^2$; step 6 gives $1, 1, -1, -1$, those of $\gamma^1$. At $\theta = 2\pi$ every factor is $1$ and $\Lambda_{1/2} = -\mathbb 1_4$ conjugates trivially: the sign of the spinor matrix is invisible in the covariance of $\gamma$.
>
> **What the derivation shows**
> - Each entry of $\gamma^\mu$ joins a component with phase $e^{\mp i\theta/2}$ to one with phase $e^{\pm i\theta/2}$, and the two half-angle phases multiply to the full-angle phase $e^{\pm i\theta}$ of the vector: $\gamma^\mu$ has one spinor slot of each kind ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]), and this is how the vector angle is rebuilt from two spinor half-angles.
> - $\pm\Lambda_{1/2}$ give the same conjugation (step 7), so the covariance of $\gamma$ cannot see the sign that distinguishes the two representations; Theorem §C5a.4.11 in its general form, here made visible.

^der-ex-c5a-4-1

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]

> [!theorem] Theorem §C5a.4.14: The Boost Matrices in the Dirac Representation, Entry by Entry
> In the chiral basis, with the boost generators $K_k = -\frac i2\operatorname{diag}(\sigma^k, -\sigma^k)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]) and the parameters of the vector boosts in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]:
> 1. **Boost along $z$** to rapidity $\eta$: $\Lambda_{1/2} = e^{-i\eta K_3} = \operatorname{diag}\bigl(e^{-\eta/2}, e^{\eta/2}, e^{\eta/2}, e^{-\eta/2}\bigr)$.
> 2. **Boost along** $\hat{\mathbf n}$, with $C = \cosh\frac\eta2$, $S = \sinh\frac\eta2$:
>
> $$
> \Lambda_{1/2} = e^{-i\eta\,\hat{\mathbf n}\cdot\mathbf K} = \begin{pmatrix} e^{-\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2} & 0 \\ 0 & e^{+\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2} \end{pmatrix}, \quad e^{\mp\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = C\,\mathbb 1 \mp S\,\hat{\mathbf n}\cdot\boldsymbol\sigma, \quad \Lambda_{1/2} = \begin{pmatrix} C - Sn^3 & -S(n^1 - in^2) & 0 & 0 \\ -S(n^1 + in^2) & C + Sn^3 & 0 & 0 \\ 0 & 0 & C + Sn^3 & S(n^1 - in^2) \\ 0 & 0 & S(n^1 + in^2) & C - Sn^3 \end{pmatrix} .
> $$
>
> The blocks are Hermitian, positive and inverse to each other (opposite signs), so $\Lambda_{1/2}$ is not unitary for $\eta \ne 0$. Part 1 is [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-5|Theorem §C5a.9.5]] by entries; part 2 with $\hat{\mathbf n} = \hat{\mathbf p}$, $\cosh\eta = E_{\mathbf p}/m$ is the boost from rest $\Lambda_{1/2}(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|Theorem §C5a.9.8]].
>
> *Source: PS §3.2, eq. (3.37) (infinitesimal), §3.3, eq. (3.49) (boost along $z$) · PHY 513 Lecture 7, Part B (slide "Spinors and Boosts"); Lecture 9, Part A, Step 4 · the user's PHY 513 notes, Ch. 8 §8.1 (Example 2: boost along $x$), Ch. 9 §9.3 (Derivations "Step 4: the spinor boost along z, as a square root", "Any direction (filled in)") · Yu §5.1, eq. (5.14) · the $4\times4$ matrix along $\hat{\mathbf n}$ written here (checked numerically)*

^thm-c5a-4-14

> [!derivation]- Derivation
> **1. The exponent.** By Theorem §C5a.4.9, step 1, with $\boldsymbol\theta = 0$ and $\boldsymbol\eta = \eta\hat{\mathbf n}$: $-i\eta\,\hat{\mathbf n}\cdot\mathbf K = -i\eta\,n^k\bigl(-\frac i2\bigr)\operatorname{diag}(\sigma^k, -\sigma^k) = \operatorname{diag}\bigl(-\frac\eta2\hat{\mathbf n}\cdot\boldsymbol\sigma,\ +\frac\eta2\hat{\mathbf n}\cdot\boldsymbol\sigma\bigr)$, since $(-i)(-\frac i2) = -\frac12$. Block by block, $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}, e^{+\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2})$.
>
> **2. The blocks.** Step 3 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-13|Derivation §C5a.4.13]] with $a = \mp\frac\eta2$ (real): $e^{\mp\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ ($\cosh$ even, $\sinh$ odd). Inserting the entries of $\hat{\mathbf n}\cdot\boldsymbol\sigma$: upper block $\begin{pmatrix} C - Sn^3 & -S(n^1 - in^2) \\ -S(n^1 + in^2) & C + Sn^3 \end{pmatrix}$, lower block the same with $S \to -S$.
>
> **3. Along z (part 1).** For $\hat{\mathbf n} = \hat{\mathbf z}$, $\hat{\mathbf n}\cdot\boldsymbol\sigma = \operatorname{diag}(1, -1)$: upper block $\operatorname{diag}(C - S, C + S) = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2})$, lower block $\operatorname{diag}(C + S, C - S) = \operatorname{diag}(e^{\eta/2}, e^{-\eta/2})$, using $C \pm S = e^{\pm\eta/2}$. The signs follow from $S^{03} = -\frac i2\operatorname{diag}(\sigma^3, -\sigma^3)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]), as in [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-5|Derivation §C5a.9.5]], step 1.
>
> **4. Hermitian, positive, mutually inverse, not unitary.** $C$, $S$ are real and $\hat{\mathbf n}\cdot\boldsymbol\sigma$ is Hermitian, so each block is Hermitian; on the eigenvectors of $\hat{\mathbf n}\cdot\boldsymbol\sigma$ (eigenvalues $\pm1$, by step 2 of Derivation §C5a.4.13) the upper block has eigenvalues $C \mp S = e^{\mp\eta/2} > 0$. The product of the blocks, all four terms: $(C - S\,\hat{\mathbf n}\cdot\boldsymbol\sigma)(C + S\,\hat{\mathbf n}\cdot\boldsymbol\sigma) = C^2 + CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma - CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma - S^2(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = (C^2 - S^2)\mathbb 1 = \mathbb 1$. Unitarity would need the block's square (it is Hermitian) to be $\mathbb 1$, but $(C\,\mathbb 1 - S\,\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = (C^2 + S^2)\mathbb 1 - 2CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma = \cosh\eta\,\mathbb 1 - \sinh\eta\,\hat{\mathbf n}\cdot\boldsymbol\sigma \ne \mathbb 1$ for $\eta \ne 0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], 2).
>
> **5. The boost from rest.** For $\hat{\mathbf n} = \hat{\mathbf p}$, $\cosh\eta = E_{\mathbf p}/m$, $\sinh\eta = |\mathbf p|/m$, the squares in step 4 are $(E_{\mathbf p} \mp \mathbf p\cdot\boldsymbol\sigma)/m = p\cdot\sigma/m$, $p\cdot\bar\sigma/m$, and the blocks are their positive square roots: Theorem §C5a.9.8, not repeated here.
>
> **What the derivation shows**
> - Every entry is a function of $\eta/2$: the boost generators have eigenvalues $\pm\frac i2$ where the vector ones have $\pm i, 0$. Squaring a block restores the full rapidity (step 4; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-4|§C5a.9, Remark: Why a square root restores the full rapidity]]).
> - The two Weyl halves are stretched oppositely, $\Lambda_L = \Lambda_R^{-1}$ for a pure boost ($\Lambda_R = (\Lambda_L^\dagger)^{-1}$ with $\Lambda_L$ Hermitian, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2): boosts distinguish $(\frac12, 0)$ from $(0, \frac12)$, rotations do not (Theorem §C5a.4.13).
> - Used next: the side-by-side comparison and the $\gamma$ check (Example §C5a.4.2).

^der-c5a-4-14

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-13|Derivation §C5a.4.13]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]

> [!example] Example §C5a.4.2: One Boost, Two Matrices
> Take the boost to rapidity $\eta$ along $z$, $\omega_{03} = -\omega_{30} = \eta$, and concretely $v = \frac35$: $\gamma = \cosh\eta = \frac54$, $\gamma v = \sinh\eta = \frac34$, so $e^\eta = \cosh\eta + \sinh\eta = 2$, $\eta = \ln2$, $e^{\eta/2} = \sqrt2$. Compare its two matrices ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-14|Theorem §C5a.4.14]]) and their generators $K_3$.
>
> *Generators* (vector left, spinor right):
>
> $$
> K_3^{\rm vec} = \begin{pmatrix} 0&0&0&i\\ 0&0&0&0\\ 0&0&0&0\\ i&0&0&0 \end{pmatrix}\ \text{(eigenvalues } i, -i, 0, 0\text{)}, \qquad K_3^{\rm Dirac} = -\frac i2\begin{pmatrix} 1&0&0&0\\ 0&-1&0&0\\ 0&0&-1&0\\ 0&0&0&1 \end{pmatrix}\ \text{(eigenvalues } -\tfrac i2, \tfrac i2, \tfrac i2, -\tfrac i2\text{)} .
> $$
>
> The real exponent $-i\eta K_3$ has eigenvalues $\eta, -\eta, 0, 0$ (on $e_0 + e_3$, $e_0 - e_3$, $e_1$, $e_2$) for the vector and $-\frac\eta2, \frac\eta2, \frac\eta2, -\frac\eta2$ for the spinor: this is the origin of $\eta$ against $\eta/2$.
>
> *Matrices*, for general $\eta$ and for $v = \frac35$:
>
> $$
> \Lambda_z(\eta) = \begin{pmatrix} \cosh\eta&0&0&\sinh\eta\\ 0&1&0&0\\ 0&0&1&0\\ \sinh\eta&0&0&\cosh\eta \end{pmatrix}, \quad \Lambda_{1/2} = \begin{pmatrix} e^{-\eta/2}&0&0&0\\ 0&e^{\eta/2}&0&0\\ 0&0&e^{\eta/2}&0\\ 0&0&0&e^{-\eta/2} \end{pmatrix}; \qquad \Lambda_z = \begin{pmatrix} \frac54&0&0&\frac34\\ 0&1&0&0\\ 0&0&1&0\\ \frac34&0&0&\frac54 \end{pmatrix}, \quad \Lambda_{1/2} = \begin{pmatrix} \frac1{\sqrt2}&0&0&0\\ 0&\sqrt2&0&0\\ 0&0&\sqrt2&0\\ 0&0&0&\frac1{\sqrt2} \end{pmatrix} .
> $$
>
> *Reading.* The vector matrix has $\cosh\eta$, $\sinh\eta$, i.e. eigenvalues $e^{\pm\eta} = 2, \frac12$ on the light-cone directions $e_0 \pm e_3$ and $1$ on $e_1$, $e_2$; the spinor matrix has $e^{\pm\eta/2} = \sqrt2, \frac1{\sqrt2}$, half the rapidity ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). It is real and positive, Hermitian, not unitary, and stretches $\psi_L$ and $\psi_R$ oppositely. Unlike a rotation, no value of $\eta \ne 0$ returns either matrix to $\mathbb 1$ (compare Example §C5a.4.1). The algebra is the same, $[K_1, K_2] = -iJ_3$ in both, and the matched pair satisfies $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: for $v = \frac35$, $\Lambda_{1/2}^{-1}\gamma^0\Lambda_{1/2} = \frac54\gamma^0 + \frac34\gamma^3$ has the entries $2, \frac12, \frac12, 2$ (derivation below).
>
> *Source: PS §3.3, eqs. (3.48)–(3.49) · PHY 513 Lecture 9, Part A ("Standard Lorentz boost acting on a 4-vector"; Step 4) · the user's PHY 513 notes, Ch. 8 §8.1 (Principle "Transforming as a vector and as a spinor, side by side"; Example 2), Ch. 9 §9.3 · the numerical case and the entry-by-entry checks written here (checked numerically)*

^ex-c5a-4-2

> [!derivation]- Derivation (the commutator and the covariance of γ, entry by entry)
> Notation and the $\gamma$ matrices as in the derivation under [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]]; $c = \cosh\eta$, $s = \sinh\eta$, so $c \pm s = e^{\pm\eta}$.
>
> **1. [K₁, K₂] = −iJ₃ for the vector.** $K_1 = i(E_{01} + E_{10})$, $K_2 = i(E_{02} + E_{20})$ (Theorem §C1a.6.5). All four products:
>
> $$
> K_1K_2 = i^2\bigl(E_{01}E_{02} + E_{01}E_{20} + E_{10}E_{02} + E_{10}E_{20}\bigr) = -(0 + 0 + E_{12} + 0), \qquad K_2K_1 = i^2\bigl(E_{02}E_{01} + E_{02}E_{10} + E_{20}E_{01} + E_{20}E_{10}\bigr) = -(0 + 0 + E_{21} + 0) .
> $$
>
> So $[K_1, K_2] = -E_{12} + E_{21}$, and $-iJ_3 = -i(-iE_{12} + iE_{21}) = -E_{12} + E_{21}$: equal.
>
> **2. [K₁, K₂] = −iJ₃ for the spinor.** $K_k = -\frac i2\operatorname{diag}(\sigma^k, -\sigma^k)$, so $K_1K_2 = (-\frac i2)^2\operatorname{diag}(\sigma^1\sigma^2, (-\sigma^1)(-\sigma^2)) = -\frac14\operatorname{diag}(i\sigma^3, i\sigma^3)$ and $K_2K_1 = -\frac14\operatorname{diag}(-i\sigma^3, -i\sigma^3)$ (the products of step 2 under Example §C5a.4.1). Hence $[K_1, K_2] = -\frac14\operatorname{diag}(2i\sigma^3, 2i\sigma^3) = -i\cdot\frac12\Sigma^3 = -iJ_3$. The minus sign, the same in both, is the Lorentz-specific one: two boosts commute into a rotation with the sign opposite to that of four-dimensional rotations ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]).
>
> **3. The conjugation factors.** $\Lambda_{1/2} = D = \operatorname{diag}(b^{-1}, b, b, b^{-1})$ with $b = e^{\eta/2}$, $D^{-1} = \operatorname{diag}(b, b^{-1}, b^{-1}, b)$, and $f_{AB} = (D^{-1})_{AA}D_{BB}$ (step 3 under Example §C5a.4.1):
>
> $$
> f_{13} = b\cdot b = e^{\eta},\ f_{24} = b^{-1}b^{-1} = e^{-\eta},\ f_{31} = b^{-1}b^{-1} = e^{-\eta},\ f_{42} = b\cdot b = e^{\eta}; \qquad f_{14} = b\,b^{-1} = 1,\ f_{23} = b^{-1}b = 1,\ f_{32} = 1,\ f_{41} = 1 .
> $$
>
> **4. μ = 1 and μ = 2.** All factors at the positions of $\gamma^1$, $\gamma^2$ are $1$: both are unchanged. Rows $1$ and $2$ of $\Lambda_z$ are $e_1^{\mathsf T}$ and $e_2^{\mathsf T}$, so $\Lambda^1{}_\nu\gamma^\nu = \gamma^1$, $\Lambda^2{}_\nu\gamma^\nu = \gamma^2$. Equal.
>
> **5. μ = 0.** Left side, entries of $\gamma^0$ (all $1$) times the factors: $(1,3)$: $e^\eta$; $(2,4)$: $e^{-\eta}$; $(3,1)$: $e^{-\eta}$; $(4,2)$: $e^\eta$. Right side, row $0$ of $\Lambda_z$: $c\,\gamma^0 + s\,\gamma^3$, entries $(1,3)$: $c + s = e^\eta$; $(2,4)$: $c - s = e^{-\eta}$; $(3,1)$: $c - s = e^{-\eta}$; $(4,2)$: $c + s = e^\eta$. Equal. For $v = \frac35$: $2, \frac12, \frac12, 2$, i.e. $\frac54 \pm \frac34$.
>
> **6. μ = 3.** Left side, entries of $\gamma^3$ ($1, -1, -1, 1$ at $(1,3), (2,4), (3,1), (4,2)$) times the factors: $e^\eta$, $-e^{-\eta}$, $-e^{-\eta}$, $e^\eta$. Right side, row $3$: $s\,\gamma^0 + c\,\gamma^3$, entries $s + c = e^\eta$, $s - c = -e^{-\eta}$, $s - c = -e^{-\eta}$, $s + c = e^\eta$. Equal. For $v = \frac35$: $2, -\frac12, -\frac12, 2$, i.e. $\frac34 \pm \frac54$ with the signs of $\gamma^3$.
>
> **What the derivation shows**
> - Each entry of $\gamma^0$, $\gamma^3$ joins a component stretched by $e^{\mp\eta/2}$ to one stretched by $e^{\pm\eta/2}$ in the conjugation, and the two half-rapidity factors multiply to $e^{\pm\eta}$, the eigenvalues of the vector boost on $e_0 \pm e_3$: the vector boost is rebuilt from two spinor half-boosts, as the rotation angle was in Example §C5a.4.1.
> - The check needs the matched pair: with $\Lambda_{1/2}$ of rapidity $\eta$ and $\Lambda_z$ of another rapidity $\eta'$, step 5 would require $e^{\eta} = \cosh\eta' + \sinh\eta' = e^{\eta'}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|Remark: One transformation, two matrices]]).

^der-ex-c5a-4-2

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-14|Theorem §C5a.4.14]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]] (and the derivation under it)

## Three transformations that act on spinor indices

> [!caution] Caution: Three different transformations
> Three operations look alike on paper — a matrix multiplying $\psi$, sometimes a sandwich — and are unrelated:
>
> | | change of basis of $V$ | Lorentz transformation of a classical field | Lorentz transformation of the quantum field |
> |---|---|---|---|
> | what changes | the description (basis $e \to e'$) | the configuration (moved by $\Lambda$) | the state of the system, by $U(\Lambda)$ |
> | group | $GL(V)$, unitary for $\bar\psi$ to keep its form (Theorem §C5a.2.4) | $SL(2, \mathbb C)$ on $V$ together with $SO^+(1,3)$ on $M$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7\|Theorem §C5a.4.7]]) | unitary operators on the Hilbert space ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-1\|Principle §C3.5.1]]) |
> | $\psi$ | $\psi'(x) = U\psi(x)$, same point | $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2\|Def. §C5a.3.2]]) | $U(\Lambda)^{-1}\hat\psi(x)U(\Lambda) = \Lambda_{1/2}\hat\psi(\Lambda^{-1}x)$ ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8\|Principle §C3.5.8]]) |
> | $\gamma^\mu$ | $U\gamma^\mu U^{-1}$ | unchanged (Theorem §C5a.4.12) | unchanged |
> | $\partial_\mu$ | unchanged | $\Lambda_\mu{}^\nu\partial_\nu$ (chain rule) | as for the classical field |
> | acts on | spinor index only | spinor index and argument | operator nature (sandwich) and, through the law, spinor index and argument |
> | predictions | unchanged (Remark: What depends on the basis, [[§C5a.7 The Dirac Equation and Its Lagrangian\|§C5a.7]]) | those of the moved system | those of the moved system |
>
> In the third column the sandwich $U(\Lambda)^{-1}\cdots U(\Lambda)$ acts on the Hilbert-space side of $\hat\psi$, while the single matrix $\Lambda_{1/2}$ acts on its spinor index (Yu (5.61); Peskin–Schroeder's equivalent form $U\hat\psi U^{-1} = \Lambda_{1/2}^{-1}\hat\psi(\Lambda x)$: [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-1|§C5b.4, Remark: Lorentz covariance of the quantized field]]; the two kinds of representation: [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]]). The letter $U$ is overloaded: the change-of-basis matrix $U$ is a constant $4\times4$ matrix, $U(\Lambda)$ an infinite-dimensional unitary operator. The operations are compatible: in a new basis the Lorentz law reads $\psi'(x) \mapsto \Lambda'_{1/2}\psi'(\Lambda^{-1}x)$ with $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$ (Theorem §C5a.1.7, 2), since $U\Lambda_{1/2}\psi = (U\Lambda_{1/2}U^{-1})(U\psi)$.
>
> *Source: Yu §5.2, eqs. (5.55)–(5.61) · the user's pre-course notes, §5.2 (Note "Four linear spaces tied to Lorentz transformations": spinor space with $D(\Lambda)$, Hilbert space with $U(\Lambda)$, "a field carries several of these actions at once") · the user's PHY 513 notes, Ch. 10 §10.3 · PS §3.5, eqs. (3.108)–(3.110) · the table written here*

^cau-c5a-4-1

> [!remark]- Connections
> - The covering $SL(2, \mathbb C) \to SO^+(1,3)$ restricts on $SU(2)$ to Quantum Mechanics' covering of $SO(3)$, and the polar decomposition $\lambda = e^hU$ is the spinor image of "boost times rotation" — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]].
> - The sign $(-1)^{2(j_+ + j_-)}$ of a $2\pi$ rotation is the value of a representation on the kernel $\{\pm\mathbb 1\}$ of the covering map, and the endpoint of the lift of the $2\pi$ loop: algebra (§C3.2), topology (§C3.1) and the explicit group meet here — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]].
> - That fields with half-integer $j_+ + j_-$ are two-valued is why their quanta obey Fermi statistics and are quantized with anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5b.9 Spin and Statistics|§C5b.9]].
> - The complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$ of the factorization in §C3.2 are literally the arguments of $\Lambda_L$ and $\Lambda_R$, and complex conjugation exchanging them is $\Lambda_L^* = \sigma^2\Lambda_R\sigma^2$ — [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-9|Theorem §C3.3.9]].
> - $\det X = x^2$ makes the Minkowski interval a determinant, exactly as the Euclidean length is $-\det(\mathbf x\cdot\boldsymbol\sigma)$; the light cone becomes the boundary of the cone of positive matrices, which is why null momenta factorize into spinors ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-3|§C5a.5, ★ Remark: Null vectors, spinors and the celestial sphere]]; helicity spinors, QFT §C5a.10) — [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
> - Unitarity is lost with compactness: $SU(2) = S^3$ admits an invariant average and unitary representations, the $\mathbb R^3$ of boosts does not — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]].
> - $\gamma^\mu$ is an invariant tensor exactly as the Pauli matrices are an invariant vector of $SU(2)$ ($U^\dagger\sigma^iU = R_{ij}\sigma^j$), the relation behind the covering $SU(2) \to SO(3)$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]].
> - Clifford multiplication being Lorentz equivariant is what makes $\slashed{\partial}\psi$ transform like $\psi$, hence the Dirac equation covariant and $\mathcal L$ a scalar; the same "invariant tensor" idea makes the Pauli matrices an invariant vector of $SU(2)$ — [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|§C5a.7, Remark: What covariance shows and what it does not]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
> - Rotations and boosts exponentiate by the same split of a series into even and odd powers, because the axis matrix squares to a multiple of the identity: $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \mathbb 1$ gives $\cos\frac\theta2$, $\cosh\frac\eta2$ for spinors, $[\hat{\mathbf n}]_\times^2 = -Q$ and $N_{\hat{\mathbf n}}^2 = \Pi$ give $\cos\theta$, $\cosh\eta$ for vectors — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]].
> - A change of basis of $V$ and a Lorentz transformation act on the same spinor index but belong to different groups, and the Hilbert-space $U(\Lambda)$ acts on yet another space; the three are kept apart in the field transformation laws of C3 — [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]], [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]], [[§C3.5 Quantum Poincaré Transformations#^rem-c3-5-2|§C3.5, Remark: Two kinds of representation]].
