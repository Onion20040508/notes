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

*Sources: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation": "One transformation, two representations"; Derivation "The covariance of $\gamma^\mu$: finite transformations"), §8.2 (Weyl spinors: Derivations "How the two halves transform", "The double cover made explicit", "The left-handed Weyl matrices are this covering"), §8.3 (Principle "Invariant tensors with mixed slots"), Ch. 10 §10.3 · PHY 513 Lecture 7 (Larsen), Part B · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$", "Interpretation") and Part C · Peskin & Schroeder, §3.2, pp. 42–44, eqs. (3.29), (3.36)–(3.42), §3.5, eqs. (3.108)–(3.110) · Yu Zhao-Huan, 量子场论讲义, Exercise 3.7, eqs. (3.259)–(3.268), §5.1, eqs. (5.17)–(5.31), §5.2, eqs. (5.55)–(5.61), (5.74) · the user's pre-course notes, §5.1, §5.2 (Remark "SL(2,C) made explicit"; Note "Four linear spaces tied to Lorentz transformations") · for the matrices entry by entry: PS §3.3, eqs. (3.48)–(3.49); PHY 513 Lecture 9, Part A; the user's PHY 513 notes, Ch. 9 §9.3; Sakurai §3.2.5, as in QM §C5.2 · PHY 513, Problem Set 6, Problem 4 (Larsen; the user's solutions).*

Which *group* acts on spinor space, and how do the $\gamma$ matrices behave under it? [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] gave the action of the Lorentz algebra (layer 4) and found two halves, $(\frac12, 0)$ and $(0, \frac12)$, on which [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]] gives $2\times2$ matrices at a complex angle, defined only up to sign on $SO^+(1,3)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-8|Theorem §CB.16.8]]); the rotation case, $SU(2) \to SO(3)$, is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]] and [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]. This section adds **layer 5**, the group: the Weyl matrices $\Lambda_L$, $\Lambda_R$, the group $SL(2, \mathbb C)$ they form, four-vectors as $2\times2$ Hermitian matrices, the covering map $SL(2, \mathbb C) \to SO^+(1,3)$ with kernel $\pm\mathbb 1$, and the integration of every $(j_+, j_-)$ (the integer ones to $SO^+(1,3)$ itself). On $V$ the group acts by $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$, and the $\gamma$'s acquire their last structure: a Minkowski index, which makes $\gamma^\mu$ an invariant tensor — fixed by a Lorentz transformation, though not by a change of basis of $V$. Three different transformations that act on spinor indices are kept apart at the end. Four-vectors as Hermitian matrices, the covering map and the integration of every $(j_+, j_-)$ are mathematics ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]]–[[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.16]]), as are $\gamma^\mu$ as an invariant tensor and Clifford multiplication ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]); they are shown in the blocks below where they are used. This section keeps the course's Weyl matrices and their covering property, $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ and the matrices entry by entry.

*Conventions* ([[Larsen PHY 513]]): $g = \operatorname{diag}(+,-,-,-)$; active reading; $\Lambda = e^{\omega} = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $(\omega)^\mu{}_\nu = \omega^\mu{}_\nu$; $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ (so $\omega_{ij} = \varepsilon_{ijk}\theta_k$), $\eta_i = \omega_{0i}$; $K_i = \mathcal J^{0i}$, so that $(\frac12, 0)$ is Peskin–Schroeder's $\psi_L$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]). Pauli matrices with the product rule of [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]; $\sigma^\mu$, $\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-2|Def. §C5a.1.2]].

## The mathematics used here

The Weyl matrices below lie in this group:

![[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2]]

They realize the representations $(\frac12, 0)$ and $(0, \frac12)$ of this definition:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2]]

Theorem §C5a.4.1 uses that complex conjugation exchanges the two copies and that no finite-dimensional representation is unitary:

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-13]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-14]]

## The Weyl matrices and SL(2, C)

> [!definition] Definition §C5a.4.1: The Weyl Matrices
> For Lorentz parameters $\omega_{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]), with angles $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and rapidities $\eta_i = \omega_{0i}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), the **left- and right-handed Weyl matrices** $\Lambda_L$, $\Lambda_R$ are the matrices of the representations $(\frac12, 0)$ and $(0, \frac12)$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]; the representation $(j_+, j_-)$: [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-16-2|Def. §CB.16.2]]), with $\mathbf J = \frac12\boldsymbol\sigma$ and $\mathbf K = -\frac i2\boldsymbol\sigma$ for $\Lambda_L$, $\mathbf K = +\frac i2\boldsymbol\sigma$ for $\Lambda_R$ (with $K_i = \mathcal J^{0i}$; the opposite sign of $\mathbf K$ exchanges the two, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|Caution: Which one is (½, 0) depends on the sign of K]]):
>
> $$
> \Lambda_L(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\boldsymbol\sigma/2}, \qquad \Lambda_R(\omega) = \exp\Bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\Bigr) = e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\boldsymbol\sigma/2} .
> $$
>
> *Source: PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$, $\psi_R \to e^{-i\vec\theta\cdot\vec\sigma/2 + \vec\eta\cdot\vec\sigma/2}\psi_R$") · PS §3.2, eqs. (3.36)–(3.37) · the user's PHY 513 notes, Ch. 8 §8.2 ($U_L$, $U_R$, eq. (weyllaws)) · Yu Exercise 3.7(c)*

^def-c5a-4-1

> [!definition] Definition §C5a.4.2: Weyl Spinors
> A **left-handed** (**right-handed**) **Weyl spinor** is a column $\psi_L \in \mathbb C^2$ ($\psi_R$) transforming as $\psi_L \to \Lambda_L\psi_L$ ($\psi_R \to \Lambda_R\psi_R$), with the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]: a vector of the representation $(\frac12, 0)$ (of $(0, \frac12)$; [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]]). These are Peskin–Schroeder's $\psi_L$, $\psi_R$.
>
> *Source: PHY 513 Lecture 8, Part C · PS §3.2, eqs. (3.36)–(3.37) · the user's PHY 513 notes, Ch. 8 §8.2 (eq. (weyllaws))*

^def-c5a-4-2

The user's notes call these matrices $U_L$, $U_R$; the letter $\Lambda$ is used here because they are not unitary, and $U$ is kept for the unitary operators on states ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1|Principle §C3.4.1]]). The handwritten Lecture 7 notes call the two halves $\xi$ and $\eta$; the Lecture 8 slides and Peskin–Schroeder use $\psi_L$, $\psi_R$. That these laws come out of the Dirac matrices is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]; here they are taken from the representation theory of §CB.4–§CB.5 and §CB.16 directly.

> [!theorem] Theorem §C5a.4.1: The Weyl Matrices Lie in SL(2, C)
> For the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] and every $\omega$:
> 1. $\det\Lambda_L(\omega) = \det\Lambda_R(\omega) = 1$, so both lie in $SL(2, \mathbb C)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-2|Def. §CB.1.2]]);
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
> **3. Complex conjugate.** $(e^A)^{\ast} = e^{A^{\ast}}$ term by term, and $A_L^{\ast} = +\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma^{\ast} - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma^{\ast}$. By Theorem §C5a.1.1, step 4, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\sigma^2A_L^{\ast}\sigma^2 = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma = A_R$. Since $(\sigma^2)^2 = \mathbb 1$, $(\sigma^2Y\sigma^2)^n = \sigma^2Y^n\sigma^2$ for every $n$, hence $\sigma^2e^{Y}\sigma^2 = e^{\sigma^2Y\sigma^2}$. With $Y = A_L^{\ast}$: $\sigma^2\Lambda_L^{\ast}\sigma^2 = e^{A_R} = \Lambda_R$, i.e. $\Lambda_L^{\ast} = \sigma^2\Lambda_R\sigma^2$. ⚑ By-product: $\sigma^2\psi_L^{\ast}$ transforms like $\psi_R$, since $\sigma^2\psi_L^{\ast} \to \sigma^2\Lambda_L^{\ast}\psi_L^{\ast} = \Lambda_R\,\sigma^2\psi_L^{\ast}$; this is the spin-½ case of [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13|Theorem §CB.16.13]], in index form Theorem §C5a.5.4.
>
> **4. Rotations and boosts.** For $\boldsymbol\eta = 0$, $A_L = A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma$ is anti-Hermitian and traceless, so $e^{A_L}$ is unitary of determinant $1$: an element of $SU(2)$, the spin-½ rotation matrix ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]). For $\boldsymbol\theta = 0$, $A_L = -\frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ is Hermitian with eigenvalues $\mp\frac12|\boldsymbol\eta|$, so $e^{A_L}$ is Hermitian with eigenvalues $e^{\mp|\boldsymbol\eta|/2} > 0$, unitary only for $\boldsymbol\eta = 0$ (as in [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]]).
>
> **What the derivation shows**
> - Both Weyl representations take values in the same group $SL(2, \mathbb C)$. They differ by the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$ of that group, which is the identity on $SU(2)$ (rotations) and inverts the Hermitian part (boosts).
> - Unit determinant is what will make $\varepsilon$ an invariant (Theorem §C5a.5.3); unitarity fails exactly for boosts.
> - Used next: the covering map (Theorems §CB.15.4–§CB.15.9) and the Dirac matrices $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]).

^der-c5a-4-1

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]

### The mathematics used here: four-vectors and the covering map

Four-vectors as Hermitian matrices, the topology of $SL(2, \mathbb C)$, and the homomorphism to $SO^+(1,3)$ with kernel $\pm\mathbb 1$, which Theorem §C5a.4.2 computes on the Weyl matrices:

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-15-3]]

![[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9]]

![[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^der-cb-9-9]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-15-4]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-5]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-15-5]]

Its derivation exponentiates with the binomial argument of the factorization theorem:

![[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3]]

![[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-5-3]]

## The covering map

> [!theorem] Theorem §C5a.4.2: The Weyl Matrices Cover the Vector Representation
> For the Weyl matrices $\Lambda_L(\omega)$, $\Lambda_R(\omega)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]] and every $\omega$, with $\Lambda = e^{\omega}$ the vector-representation matrix of the same parameters ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]):
> 1. $\Lambda_L(\omega)\,(x_\mu\sigma^\mu)\,\Lambda_L(\omega)^\dagger = (\Lambda x)_\mu\sigma^\mu$, i.e. $\pi(\Lambda_L(\omega)) = e^{\omega}$ ($\pi$ of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]); and $\Lambda_R(\omega)\,(x_\mu\bar\sigma^\mu)\,\Lambda_R(\omega)^\dagger = (\Lambda x)_\mu\bar\sigma^\mu$.
> 2. Equivalently, $\bar\sigma^\mu$ and $\sigma^\mu$ are invariant under the Weyl matrices:
>
> $$
> \Lambda_L^\dagger\,\bar\sigma^\mu\,\Lambda_L = \Lambda^\mu{}_\nu\,\bar\sigma^\nu, \qquad \Lambda_R^\dagger\,\sigma^\mu\,\Lambda_R = \Lambda^\mu{}_\nu\,\sigma^\nu .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 (Derivation "The left-handed Weyl matrices are this covering", eq. (SL2Ccover); checked numerically there, and again here) · Yu Exercise 3.7(e), eqs. (3.267)–(3.268) (rotation about z) · part 2 and the series argument written out here*

^thm-c5a-4-2

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
> **3. Exponentiate.** Left multiplication $\ell(M) = A_LM$ and right multiplication $r(M) = MA_L^\dagger$ commute as linear maps of $M_2(\mathbb C)$ ($A_L(MA_L^\dagger) = (A_LM)A_L^\dagger$), so $e^{s(\ell + r)} = e^{s\ell}e^{sr}$ (the binomial argument of [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-5-3|Derivation §CB.5.3]], step 3), i.e. $e^{sL}(M) = e^{sA_L}Me^{sA_L^\dagger} = \Lambda_L(s\omega)M\Lambda_L(s\omega)^\dagger$ (with $(e^{sA_L})^\dagger = e^{sA_L^\dagger}$). Iterating step 2, $L^n\circ\Phi = \Phi\circ\omega^n$ for every $n$, so summing the series (both converge absolutely; $\Phi$ is linear) $e^{sL}\circ\Phi = \Phi\circ e^{s\omega}$. At $s = 1$: $\Lambda_L(\omega)\Phi(x)\Lambda_L(\omega)^\dagger = \Phi(e^\omega x)$, part 1 for $\Lambda_L$. By the definition of $\pi$ (Theorem §CB.15.4), $\pi(\Lambda_L(\omega)) = e^{\omega}$.
>
> **4. The right-handed matrices.** $A_R = -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma$ and $\bar\Phi(x) = x^0\mathbb 1 + \mathbf x\cdot\boldsymbol\sigma$. Then $A_R\bar\Phi + \bar\Phi A_R^\dagger = -\frac i2[\boldsymbol\theta\cdot\boldsymbol\sigma, \bar\Phi] + \frac12\{\boldsymbol\eta\cdot\boldsymbol\sigma, \bar\Phi\} = -\frac i2\cdot2i(\boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma + \frac12\bigl(2x^0\boldsymbol\eta\cdot\boldsymbol\sigma + 2(\boldsymbol\eta\cdot\mathbf x)\mathbb 1\bigr) = (\boldsymbol\eta\cdot\mathbf x)\mathbb 1 + (x^0\boldsymbol\eta + \boldsymbol\theta\times\mathbf x)\cdot\boldsymbol\sigma = \bar\Phi(\omega x)$, the signs of both the rotation and the boost term having flipped relative to step 2 together with the sign of $\mathbf x$ in $\bar\Phi$. Step 3 applies verbatim.
>
> **5. Part 2.** Multiply part 1 by $\bar\sigma^\nu$ and take the trace. The right side gives $\operatorname{tr}(\Phi(\Lambda x)\bar\sigma^\nu) = 2(\Lambda x)^\nu = \Lambda^\nu{}_\mu\operatorname{tr}(\Phi(x)\bar\sigma^\mu)$ (Theorem §CB.15.3). The left side, by cyclicity, is $\operatorname{tr}(\Phi(x)\,\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L)$. So $\operatorname{tr}\bigl(X\,(\Lambda_L^\dagger\bar\sigma^\nu\Lambda_L - \Lambda^\nu{}_\mu\bar\sigma^\mu)\bigr) = 0$ for every Hermitian $X$, hence (complex-linearly) for every $X \in M_2(\mathbb C)$, since every matrix is $H_1 + iH_2$ with $H_k$ Hermitian. Taking $X = E_{ji}$ picks out the $(i, j)$ entry of the bracket, so the bracket vanishes. The same with $\Lambda_R$, $\bar\Phi$ and $\operatorname{tr}(\bar X\sigma^\nu) = 2x^\nu$ gives $\Lambda_R^\dagger\sigma^\nu\Lambda_R = \Lambda^\nu{}_\mu\sigma^\mu$.
>
> **6. Check: rotation about z.** $\boldsymbol\theta = \theta\hat{\mathbf z}$: $\Lambda_L = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$, and in the matrix of Theorem §CB.15.3 the off-diagonal entry $-x^1 + ix^2$ is multiplied by $e^{-i\theta/2}\cdot\overline{e^{i\theta/2}} = e^{-i\theta}$, which is the active rotation $(x^1, x^2) \mapsto (x^1\cos\theta - x^2\sin\theta, x^1\sin\theta + x^2\cos\theta)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]). Yu's $\lambda(\theta) = \operatorname{diag}(e^{i\theta/2}, e^{-i\theta/2})$ in (3.267) is $\Lambda_L$ at $-\theta$, the passive rotation of (3.268).
>
> **What the derivation shows**
> - The same six numbers $\omega_{\mu\nu}$ produce $\Lambda_L(\omega)$ and $e^\omega$, and the covering map sends one to the other. The half-angles of $\Lambda_L$ become full angles because $\lambda$ acts on $X$ twice, once from each side.
> - Part 2 says that $\bar\sigma^\mu$ is an invariant tensor with one vector slot and two spinor slots, as $\gamma^\mu$ will be ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]]); it is why $\psi_L^\dagger\bar\sigma^\mu\psi_L$ is a four-vector (QFT §C5a.7, the Weyl Lagrangian).
> - $\Lambda_R(\omega) = (\Lambda_L(\omega)^\dagger)^{-1}$ is *not* $\Lambda_L$ of another $\omega$ with the same $\sigma$: it covers $e^\omega$ through $\bar\sigma$. Using $\sigma$ for $\Lambda_R$ would give the parity image of $e^\omega$.
> - Used next: $\pi$ is onto (Theorem §CB.15.9), and every $(j_+, j_-)$ integrates (Theorem §CB.16.9).

^der-c5a-4-2

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^der-cb-5-3|Derivation §CB.5.3]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]

### The mathematics used here: the double cover

With Theorem §C5a.4.2 the covering is onto: $SL(2, \mathbb C)$ is the double cover of $SO^+(1,3)$, the rotation story one level up:

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^der-cb-15-9]]

![[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^rem-cb-15-1]]

Theorem §C5a.4.3 says the spinor matrix is a two-valued function of Λ, by the integration of the representations $(j_+, j_-)$:

![[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-7]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9]]

![[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^der-cb-16-9]]

The remark "One transformation, two matrices" rests on the inequivalence of the Dirac and vector representations:

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-5]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-5]]

## The group action on spinor space

> [!theorem] Theorem §C5a.4.3: The Spinor Lorentz Matrices Are Pairs of Weyl Matrices
> 1. In the chiral basis, with the Weyl matrices of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], the Dirac-representation matrices ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]) are
>
> $$
> \Lambda_{1/2}(\omega) = \begin{pmatrix}\Lambda_L(\omega) & 0\\ 0 & \Lambda_R(\omega)\end{pmatrix} = \begin{pmatrix} e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma} & 0\\ 0 & e^{-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma}\end{pmatrix} .
> $$
>
> 2. $\lambda \mapsto \operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ is a representation of $SL(2, \mathbb C)$ with $\Lambda_{1/2}(\omega)$ the image of $\Lambda_L(\omega)$ ([[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]]); on $SO^+(1,3)$, $\Lambda_{1/2}$ is defined up to sign, a two-valued representation ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^def-cb-9-7|Def. §CB.9.7]]), and a rotation by $2\pi$ gives $-\mathbb 1_4$.
> 3. Rotation by $\theta$ about $z$: $\Lambda_{1/2} = \operatorname{diag}(e^{-i\theta\sigma^3/2}, e^{-i\theta\sigma^3/2})$. Boost of rapidity $\eta$ along $x$: $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\sigma^1/2}, e^{+\eta\sigma^1/2})$, $e^{\mp\eta\sigma^1/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\sigma^1$.
>
> *Source: PS §3.2, eqs. (3.36)–(3.37) · PHY 513 Lecture 7, Part B (slides "Spinors and Rotation", "Spinors and Boosts") · PHY 513 Lecture 8, Part C ("$\psi_L \to e^{-i\vec\theta\cdot\vec\sigma/2 - \vec\eta\cdot\vec\sigma/2}\psi_L$ …") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation", Examples 1–2, eq. (spinorboost); checked numerically there), §8.2 (Derivation "How the two halves transform") · the user's pre-course notes, §5.2 (Remark "SL(2,C) made explicit")*

^thm-c5a-4-3

> [!derivation]- Derivation
> **1. The exponent.** $-\frac i2\omega_{\mu\nu}S^{\mu\nu} = -i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$ (the regrouping of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], linear in the generators). Inserting Theorem §C5a.3.1: $-i\boldsymbol\theta\cdot\frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma) - i\boldsymbol\eta\cdot(-\frac i2)\operatorname{diag}(\boldsymbol\sigma, -\boldsymbol\sigma) = \operatorname{diag}\bigl(-\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma - \frac12\boldsymbol\eta\cdot\boldsymbol\sigma,\ -\frac i2\boldsymbol\theta\cdot\boldsymbol\sigma + \frac12\boldsymbol\eta\cdot\boldsymbol\sigma\bigr)$, since $-i\cdot(-\frac i2) = -\frac12$.
>
> **2. Exponentiate.** Powers of a block-diagonal matrix are block diagonal with the powers of the blocks, so $\exp\operatorname{diag}(A, B) = \operatorname{diag}(e^A, e^B)$. The blocks are $\Lambda_L(\omega)$ and $\Lambda_R(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]).
>
> **3. SL(2, C).** $\lambda \mapsto \lambda$ and $\lambda \mapsto (\lambda^\dagger)^{-1}$ are representations (Derivation §CB.16.9, step 1), hence so is their direct sum; at $\lambda = \Lambda_L(\omega)$ it gives $\operatorname{diag}(\Lambda_L, (\Lambda_L^\dagger)^{-1}) = \operatorname{diag}(\Lambda_L, \Lambda_R) = \Lambda_{1/2}(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2). This is [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]] for $(\frac12, 0)\oplus(0, \frac12)$; $j_+ + j_- = \frac12$, so the image of $-\mathbb 1$ is $-\mathbb 1_4$ and $\Lambda_{1/2}$ is two-valued on $SO^+(1,3)$.
>
> **4. Rotation about z.** $\omega_{12} = -\omega_{21} = \theta$ gives $\boldsymbol\theta = \theta\hat{\mathbf z}$, $\boldsymbol\eta = 0$ (the two terms $\frac12(\omega_{12}S^{12} + \omega_{21}S^{21}) = \theta S^{12}$), so both blocks are $e^{-i\theta\sigma^3/2} = \operatorname{diag}(e^{-i\theta/2}, e^{i\theta/2})$. At $\theta = 2\pi$ each is $-\mathbb 1$ ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]), while the vector-representation matrix of the same $\omega$ is $\exp(-2\pi i\,\mathcal J^{12}) = \mathbb 1$ (the eigenvalues of $\mathcal J^{12}$ are $0, 0, \pm1$). ⚑ By-product: the same physical rotation multiplies the four spinor components by $e^{-i\theta/2}, e^{i\theta/2}, e^{-i\theta/2}, e^{i\theta/2}$: no component is left alone, unlike $V^0$, $V^3$ of a vector.
>
> **5. Boost along x.** $\omega_{01} = -\omega_{10} = \eta$ gives $\boldsymbol\eta = \eta\hat{\mathbf x}$, $\boldsymbol\theta = 0$, so the blocks are $e^{\mp\eta\sigma^1/2}$. Since $(\sigma^1)^2 = \mathbb 1$, the even terms of the series sum to $\cosh\frac\eta2\,\mathbb 1$ and the odd ones to $\mp\sinh\frac\eta2\,\sigma^1$. No $i$ appears: the blocks are Hermitian, not unitary, and stretched in opposite senses. The same $\omega$ gives in the vector representation $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\eta$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\eta$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]).
>
> **What the derivation shows**
> - The Dirac representation is reducible: the halves never mix under rotations or boosts. If the lower half vanishes in one frame, it vanishes in all, which could never happen for a four-vector.
> - Half the angle and half the rapidity appear in every spinor matrix ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|Remark: Why half the angle]]); entry by entry for any axis: Theorems §C5a.4.4–§C5a.4.5 below.
> - Used next: boosting rest-frame spinors ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-5|Theorem §C5a.9.5]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|Theorem §C5a.9.8]]); the Weyl form of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-10|Theorem §C5a.7.10]]).

^der-c5a-4-3

*Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-9|Theorem §CB.16.9]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

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
> | invariant form | $g$: $\Lambda^{\mathsf T}g\Lambda = g$ | $\gamma^0$: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$ ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-13\|Theorem §CB.17.13]]) |
> | rotation by $2\pi$ | $+\mathbb 1$ | $-\mathbb 1$ |
> | fixed by $\Lambda$? | yes | up to sign: a representation of $SL(2, \mathbb C)$ |
>
> Both matrices are $4\times4$ for unrelated reasons: $\Lambda$ because spacetime has four dimensions, $\Lambda_{1/2}$ because the Clifford algebra needs four components (Theorem §CB.11.9). Relations such as $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ hold only for a matched pair built from the same $\omega$ (checked numerically in the user's notes, matched and mismatched). This is why the lecture calls $\psi$ a four-component *column*, not a four-vector. Both matrices written out entry by entry, for rotations about and boosts along any axis: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]] (vector side: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]); one rotation and one boost side by side, with the generators and the check of $\gamma^\mu$ entry by entry: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]].
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation": "One transformation, two representations"; Derivation "From six numbers to two matrices"; Principle "Transforming as a vector and as a spinor, side by side"; paragraph "Same dimension, different representation")*

^rem-c5a-4-1

### The mathematics used here: γ^μ as an invariant tensor

The covariance of the Dirac matrices, infinitesimal and finite — the lecture's form is the remark below — and Clifford multiplication as an equivariant map (Remark: Why γ is fixed under a Lorentz transformation):

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-17]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-17]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-7b]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-17-1]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-8]]

![[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-17-8]]

## γ^μ carries a vector index

> [!remark] Remark: The lecture's form of the covariance
> Lecture 8 writes $\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1} = (\Lambda^{-1})^\mu{}_\nu\gamma^\nu$, the infinitesimal version $(1 - \frac i2\omega S)\gamma^\mu(1 + \frac i2\omega S) = (1 + \frac i2\omega\mathcal J)^\mu{}_\nu\gamma^\nu$, and then $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$. All three are Theorem §CB.17.7 with $\omega \to -\omega$ ($\Lambda_{1/2}(-\omega) = \Lambda_{1/2}^{-1}$, $e^{-\omega} = \Lambda^{-1}$), and Peskin–Schroeder's infinitesimal form is the same with the opposite sign of $\omega$. The last form carries the slide's message: "$\gamma^\nu$ are just numbers. They do not transform!" — transforming the vector index and both spinor indices at once returns the same matrices. That is what "invariant tensor" means, and why $\gamma^\nu\psi$ transforms as a spinor and a vector at once, $\gamma^\nu\psi \to \Lambda^\nu{}_\mu\Lambda_{1/2}(\gamma^\mu\psi)$.
>
> *Source: PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · PS §3.2, p. 42 · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots"), §8.1 (Definition "What 'transforms like a spinor' means")*

^rem-c5a-4-2

> [!remark] Remark: Why γ is fixed under a Lorentz transformation but not under a change of basis
> $\gamma^\mu$ has three slots: Minkowski, $V$, $V'$. A **Lorentz transformation** acts on all of them at once — $\Lambda$ on the Minkowski slot, $\Lambda_{1/2}$ and $\Lambda_{1/2}^{-1}$ on the spinor slots — and returns the same array (Theorem §CB.17.8, 2): "$\gamma^\nu$ are just numbers. They do not transform!" (Lecture 8). What transforms is $\psi$, and $\partial_\mu$ with it, and the equation keeps its form. A **change of basis of $V$** acts only on the spinor slots, with one $U$ and its inverse; the Minkowski slot is untouched because no basis of spacetime changes. Nothing compensates, so the array changes: $\gamma' = U\gamma U^{-1}$ (Theorem §CB.10.15). In short, the Lorentz group acts on spacetime *and* spinor space and $\gamma$ is invariant under the combined action; $GL(V)$ acts on spinor space alone and $\gamma$ is merely covariant under it.
>
> *Source: PHY 513 Lecture 8, Part A (slide "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 · the comparison written here*

^rem-c5a-4-3

### The mathematics used here: the matrices

Theorems §C5a.4.4–§C5a.4.5 and the two examples use the $2\pi$-rotation test, the Lorentz algebra and the adjoints of the generators:

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-26]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-6]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-6b]]

![[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-4-6c]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-22]]

![[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^der-cb-13-22]]

Theorem §C5a.4.6 reads eigenvalues, which do not depend on the basis:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-5]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-15]]

## The matrices entry by entry

Theorem §C5a.4.3 gives $\Lambda_{1/2}$ as a pair of $2\times2$ exponentials. Here the rotations and boosts about and along an arbitrary axis are written as full $4\times4$ matrices in the chiral basis, next to the vector matrices of the same parameters ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]), and the covariance of $\gamma^\mu$ (Theorem §CB.17.7) is checked entry by entry. Throughout, $\hat{\mathbf n} = (n^1, n^2, n^3)$ is a unit vector and

$$
\hat{\mathbf n}\cdot\boldsymbol\sigma = \begin{pmatrix} n^3 & n^1 - in^2 \\ n^1 + in^2 & -n^3 \end{pmatrix} .
$$

> [!theorem] Theorem §C5a.4.4: The Rotation Matrices in the Dirac Representation, Entry by Entry
> In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), with the rotation generators $J_k = \frac12\Sigma^k$ ([[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]) and the parameters of the vector rotations in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]:
> 1. **Rotation about $z$** by $\theta$: $\Lambda_{1/2} = e^{-i\theta J_3} = \operatorname{diag}\bigl(e^{-i\theta/2}, e^{i\theta/2}, e^{-i\theta/2}, e^{i\theta/2}\bigr)$.
> 2. **Rotation about** $\hat{\mathbf n}$ by $\theta$, with $c = \cos\frac\theta2$, $s = \sin\frac\theta2$:
>
> $$
> \Lambda_{1/2} = e^{-i\theta\,\hat{\mathbf n}\cdot\mathbf J} = \begin{pmatrix} U & 0 \\ 0 & U \end{pmatrix}, \quad U = e^{-i\theta\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = c\,\mathbb 1 - is\,\hat{\mathbf n}\cdot\boldsymbol\sigma, \quad \Lambda_{1/2} = \begin{pmatrix} c - isn^3 & -is(n^1 - in^2) & 0 & 0 \\ -is(n^1 + in^2) & c + isn^3 & 0 & 0 \\ 0 & 0 & c - isn^3 & -is(n^1 - in^2) \\ 0 & 0 & -is(n^1 + in^2) & c + isn^3 \end{pmatrix} .
> $$
>
> The two blocks are equal and $U \in SU(2)$, so $\Lambda_{1/2}$ is unitary; $U$ is the spin-½ rotation of [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]]. At $\theta = 2\pi$, $\Lambda_{1/2} = -\mathbb 1_4$; at $\theta = 4\pi$, $\Lambda_{1/2} = +\mathbb 1_4$.
>
> *Source: PS §3.2, eq. (3.37) (infinitesimal) · PHY 513 Lecture 7, Part B (slide "Spinors and Rotation") · the user's PHY 513 notes, Ch. 8 §8.1 (Definition "The spinor Lorentz transformation", Example 1: rotation about $z$) · Sakurai §3.2.5, eqs. (3.60)–(3.63), as in QM §C5.2 (the $2\times2$ block) · the $4\times4$ matrix about $\hat{\mathbf n}$ written here (checked numerically) · PHY 513, Problem Set 6, Problem 4(c)–(d) (part 1 and the value $-\mathbb 1_4$ at $2\pi$, as the user wrote them; same signs)*

^thm-c5a-4-4

> [!derivation]- Derivation
> **1. The exponent.** By Theorem §C5a.4.3, step 1, with $\boldsymbol\theta = \theta\hat{\mathbf n}$ and $\boldsymbol\eta = 0$: $-i\theta\,\hat{\mathbf n}\cdot\mathbf J = -i\theta\,n^k\cdot\frac12\operatorname{diag}(\sigma^k, \sigma^k) = \operatorname{diag}\bigl(-\frac{i\theta}2\hat{\mathbf n}\cdot\boldsymbol\sigma,\ -\frac{i\theta}2\hat{\mathbf n}\cdot\boldsymbol\sigma\bigr)$. The exponential of a block-diagonal matrix is block diagonal with the exponentials of the blocks (Derivation §C5a.4.3, step 2), so $\Lambda_{1/2} = \operatorname{diag}(U, U)$ with $U = e^{-i\theta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$.
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
> (This step is used again, with real $a$, for the boosts: Theorem §C5a.4.5.)
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
> - Every entry is a function of $\theta/2$: the rotation generators have eigenvalues $\pm\frac12$ where the vector ones have $\pm1, 0$ ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). Hence the period $4\pi$, and $-\mathbb 1_4$ at $2\pi$: the Dirac representation is a spinor representation ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-26|Def. §CB.13.26]]).
> - The two Weyl halves rotate by the same unitary $U$, because $J_k$ is the same in both blocks: rotations cannot tell $\psi_L$ from $\psi_R$; only boosts can (Theorem §C5a.4.5).
> - Used next: the side-by-side comparison and the $\gamma$ check (Example §C5a.4.1).

^der-c5a-4-4

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]

> [!example] Example §C5a.4.1: One Rotation, Two Matrices
> Take the rotation by $\theta$ about $z$, $\omega_{12} = -\omega_{21} = \theta$, and compare its two matrices: the vector one ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]]) and the Dirac one ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]]), and their generators $J_3$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]).
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
> *Reading.* An eigenvalue $m$ of $J_3$ becomes the phase $e^{-im\theta}$: $m = \pm1, 0$ gives entries in $\theta$ (and the untouched $t$, $z$), $m = \pm\frac12$ gives entries in $\theta/2$, and no spinor component is left alone. At $\theta = 2\pi$ the vector matrix is $\mathbb 1$ ($e^{\mp2\pi i} = e^0 = 1$) and the spinor matrix is $-\mathbb 1_4$ ($e^{\mp i\pi} = -1$): the vector representation is a tensor representation and the Dirac representation a spinor representation ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-26|Def. §CB.13.26]]). At $\theta = 4\pi$ both are $\mathbb 1$. The algebra is the same, $[J_1, J_2] = iJ_3$ in both, and the matched pair satisfies $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ with $\Lambda = R_z(\theta)$: at $\theta = \frac\pi2$, $\Lambda_{1/2}^{-1}\gamma^1\Lambda_{1/2} = -\gamma^2$ and $\Lambda_{1/2}^{-1}\gamma^2\Lambda_{1/2} = \gamma^1$ (derivation below).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (Principle "Transforming as a vector and as a spinor, side by side"; Example 1), Ch. 7 §7.3 (Derivation "What the vector generators do") · PHY 513 Lecture 7, Part B ("Unlike a 4-vector under rotation") · PS §3.1, eq. (3.20), §3.2, eq. (3.37) · the side-by-side matrices and the entry-by-entry checks written here (checked numerically) · PHY 513, Problem Set 6, Problem 4(c)–(d) (the same pair of matrices and the $2\pi$ comparison, as the user wrote them)*

^ex-c5a-4-1

> [!derivation]- Derivation (the commutator and the covariance of γ, entry by entry)
> $E_{AB}$ is the matrix with $1$ in row $A$, column $B$; $E_{AB}E_{CD} = \delta_{BC}E_{AD}$. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]), rows and columns $A, B = 1, \dots, 4$,
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
> **2. [J₁, J₂] = iJ₃ for the spinor.** $J_k = \frac12\operatorname{diag}(\sigma^k, \sigma^k)$, so $[J_1, J_2] = \frac14\operatorname{diag}([\sigma^1, \sigma^2], [\sigma^1, \sigma^2])$. With $\sigma^1\sigma^2 = \begin{pmatrix} 0&1\\ 1&0 \end{pmatrix}\begin{pmatrix} 0&-i\\ i&0 \end{pmatrix} = \begin{pmatrix} i&0\\ 0&-i \end{pmatrix} = i\sigma^3$ and $\sigma^2\sigma^1 = \begin{pmatrix} -i&0\\ 0&i \end{pmatrix} = -i\sigma^3$: $[\sigma^1, \sigma^2] = 2i\sigma^3$, and $[J_1, J_2] = \frac14\operatorname{diag}(2i\sigma^3, 2i\sigma^3) = i\cdot\frac12\Sigma^3 = iJ_3$. Same relation ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]), different matrices.
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
> - Each entry of $\gamma^\mu$ joins a component with phase $e^{\mp i\theta/2}$ to one with phase $e^{\pm i\theta/2}$, and the two half-angle phases multiply to the full-angle phase $e^{\pm i\theta}$ of the vector: $\gamma^\mu$ has one spinor slot of each kind ([[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-17-1|Def. §CB.17.1]]), and this is how the vector angle is rebuilt from two spinor half-angles.
> - $\pm\Lambda_{1/2}$ give the same conjugation (step 7), so the covariance of $\gamma$ cannot see the sign that distinguishes the two representations; Theorem §CB.17.7 in its general form, here made visible.

^der-ex-c5a-4-1

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]]

> [!theorem] Theorem §C5a.4.5: The Boost Matrices in the Dirac Representation, Entry by Entry
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
> *Source: PS §3.2, eq. (3.37) (infinitesimal), §3.3, eq. (3.49) (boost along $z$) · PHY 513 Lecture 7, Part B (slide "Spinors and Boosts"); Lecture 9, Part A, Step 4 · the user's PHY 513 notes, Ch. 8 §8.1 (Example 2: boost along $x$), Ch. 9 §9.3 (Derivations "Step 4: the spinor boost along z, as a square root", "Any direction (filled in)") · Yu §5.1, eq. (5.14) · the $4\times4$ matrix along $\hat{\mathbf n}$ written here (checked numerically) · PHY 513, Problem Set 6, Problem 4(a) (part 1, as the user wrote it; same signs)*

^thm-c5a-4-5

> [!derivation]- Derivation
> **1. The exponent.** By Theorem §C5a.4.3, step 1, with $\boldsymbol\theta = 0$ and $\boldsymbol\eta = \eta\hat{\mathbf n}$: $-i\eta\,\hat{\mathbf n}\cdot\mathbf K = -i\eta\,n^k\bigl(-\frac i2\bigr)\operatorname{diag}(\sigma^k, -\sigma^k) = \operatorname{diag}\bigl(-\frac\eta2\hat{\mathbf n}\cdot\boldsymbol\sigma,\ +\frac\eta2\hat{\mathbf n}\cdot\boldsymbol\sigma\bigr)$, since $(-i)(-\frac i2) = -\frac12$. Block by block, $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}, e^{+\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2})$.
>
> **2. The blocks.** Step 3 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-4|Derivation §C5a.4.4]] with $a = \mp\frac\eta2$ (real): $e^{\mp\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ ($\cosh$ even, $\sinh$ odd). Inserting the entries of $\hat{\mathbf n}\cdot\boldsymbol\sigma$: upper block $\begin{pmatrix} C - Sn^3 & -S(n^1 - in^2) \\ -S(n^1 + in^2) & C + Sn^3 \end{pmatrix}$, lower block the same with $S \to -S$.
>
> **3. Along z (part 1).** For $\hat{\mathbf n} = \hat{\mathbf z}$, $\hat{\mathbf n}\cdot\boldsymbol\sigma = \operatorname{diag}(1, -1)$: upper block $\operatorname{diag}(C - S, C + S) = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2})$, lower block $\operatorname{diag}(C + S, C - S) = \operatorname{diag}(e^{\eta/2}, e^{-\eta/2})$, using $C \pm S = e^{\pm\eta/2}$. The signs follow from $S^{03} = -\frac i2\operatorname{diag}(\sigma^3, -\sigma^3)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]), as in [[§C5a.9 Plane-Wave Solutions#^der-c5a-9-5|Derivation §C5a.9.5]], step 1.
>
> **4. Hermitian, positive, mutually inverse, not unitary.** $C$, $S$ are real and $\hat{\mathbf n}\cdot\boldsymbol\sigma$ is Hermitian, so each block is Hermitian; on the eigenvectors of $\hat{\mathbf n}\cdot\boldsymbol\sigma$ (eigenvalues $\pm1$, by step 2 of Derivation §C5a.4.4) the upper block has eigenvalues $C \mp S = e^{\mp\eta/2} > 0$. The product of the blocks, all four terms: $(C - S\,\hat{\mathbf n}\cdot\boldsymbol\sigma)(C + S\,\hat{\mathbf n}\cdot\boldsymbol\sigma) = C^2 + CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma - CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma - S^2(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = (C^2 - S^2)\mathbb 1 = \mathbb 1$. Unitarity would need the block's square (it is Hermitian) to be $\mathbb 1$, but $(C\,\mathbb 1 - S\,\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = (C^2 + S^2)\mathbb 1 - 2CS\,\hat{\mathbf n}\cdot\boldsymbol\sigma = \cosh\eta\,\mathbb 1 - \sinh\eta\,\hat{\mathbf n}\cdot\boldsymbol\sigma \ne \mathbb 1$ for $\eta \ne 0$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-22|Theorem §CB.13.22]], 2).
>
> **5. The boost from rest.** For $\hat{\mathbf n} = \hat{\mathbf p}$, $\cosh\eta = E_{\mathbf p}/m$, $\sinh\eta = |\mathbf p|/m$, the squares in step 4 are $(E_{\mathbf p} \mp \mathbf p\cdot\boldsymbol\sigma)/m = p\cdot\sigma/m$, $p\cdot\bar\sigma/m$, and the blocks are their positive square roots: Theorem §C5a.9.8, not repeated here.
>
> **What the derivation shows**
> - Every entry is a function of $\eta/2$: the boost generators have eigenvalues $\pm\frac i2$ where the vector ones have $\pm i, 0$. Squaring a block restores the full rapidity (step 4; [[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-4|§C5a.9, Remark: Why a square root restores the full rapidity]]).
> - The two Weyl halves are stretched oppositely, $\Lambda_L = \Lambda_R^{-1}$ for a pure boost ($\Lambda_R = (\Lambda_L^\dagger)^{-1}$ with $\Lambda_L$ Hermitian, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2): boosts distinguish $(\frac12, 0)$ from $(0, \frac12)$, rotations do not (Theorem §C5a.4.4).
> - Used next: the side-by-side comparison and the $\gamma$ check (Example §C5a.4.2).

^der-c5a-4-5

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-4|Derivation §C5a.4.4]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-22|Theorem §CB.13.22]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]

> [!example] Example §C5a.4.2: One Boost, Two Matrices
> Take the boost to rapidity $\eta$ along $z$, $\omega_{03} = -\omega_{30} = \eta$, and concretely $v = \frac35$: $\gamma = \cosh\eta = \frac54$, $\gamma v = \sinh\eta = \frac34$, so $e^\eta = \cosh\eta + \sinh\eta = 2$, $\eta = \ln2$, $e^{\eta/2} = \sqrt2$. Compare its two matrices ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]]) and their generators $K_3$.
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
> *Reading.* The vector matrix has $\cosh\eta$, $\sinh\eta$, i.e. eigenvalues $e^{\pm\eta} = 2, \frac12$ on the light-cone directions $e_0 \pm e_3$ and $1$ on $e_1$, $e_2$; the spinor matrix has $e^{\pm\eta/2} = \sqrt2, \frac1{\sqrt2}$, half the rapidity ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). It is real and positive, Hermitian, not unitary, and stretches $\psi_L$ and $\psi_R$ oppositely. Unlike a rotation, no value of $\eta \ne 0$ returns either matrix to $\mathbb 1$ (compare Example §C5a.4.1). The vector matrix leaves $x^1$, $x^2$ alone; the spinor matrix leaves no component alone, in any basis ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], Problem Set 6, Problem 4(b)). The algebra is the same, $[K_1, K_2] = -iJ_3$ in both, and the matched pair satisfies $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$: for $v = \frac35$, $\Lambda_{1/2}^{-1}\gamma^0\Lambda_{1/2} = \frac54\gamma^0 + \frac34\gamma^3$ has the entries $2, \frac12, \frac12, 2$ (derivation below).
>
> *Source: PS §3.3, eqs. (3.48)–(3.49) · PHY 513 Lecture 9, Part A ("Standard Lorentz boost acting on a 4-vector"; Step 4) · the user's PHY 513 notes, Ch. 8 §8.1 (Principle "Transforming as a vector and as a spinor, side by side"; Example 2), Ch. 9 §9.3 · the numerical case and the entry-by-entry checks written here (checked numerically) · PHY 513, Problem Set 6, Problem 4(a) (the same pair of matrices, all components written out, as the user wrote them)*

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
> **2. [K₁, K₂] = −iJ₃ for the spinor.** $K_k = -\frac i2\operatorname{diag}(\sigma^k, -\sigma^k)$, so $K_1K_2 = (-\frac i2)^2\operatorname{diag}(\sigma^1\sigma^2, (-\sigma^1)(-\sigma^2)) = -\frac14\operatorname{diag}(i\sigma^3, i\sigma^3)$ and $K_2K_1 = -\frac14\operatorname{diag}(-i\sigma^3, -i\sigma^3)$ (the products of step 2 under Example §C5a.4.1). Hence $[K_1, K_2] = -\frac14\operatorname{diag}(2i\sigma^3, 2i\sigma^3) = -i\cdot\frac12\Sigma^3 = -iJ_3$. The minus sign, the same in both, is the Lorentz-specific one: two boosts commute into a rotation with the sign opposite to that of four-dimensional rotations ([[§CB.4 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-4-6|Theorem §CB.4.6]]).
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
> - The check needs the matched pair: with $\Lambda_{1/2}$ of rapidity $\eta$ and $\Lambda_z$ of another rapidity $\eta'$, step 5 would require $e^{\eta} = \cosh\eta' + \sinh\eta' = e^{\eta'}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|Remark: One transformation, two matrices]]).

^der-ex-c5a-4-2

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-17-7|Theorem §CB.17.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]] (and the derivation under it)

> [!theorem] Theorem §C5a.4.6: A Boost Leaves No Spinor Component Invariant
> Let $\eta \neq 0$ and $\Lambda_{1/2}$ be the spinor matrix of the boost of rapidity $\eta$ along a unit vector $\hat{\mathbf n}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]]). Its eigenvalues are $e^{\eta/2}, e^{\eta/2}, e^{-\eta/2}, e^{-\eta/2}$, none equal to $1$. Hence, in every basis of spinor space ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]]):
> 1. no component of a Dirac spinor is invariant, i.e. there is no $k$ with $(\Lambda_{1/2}\psi)_k = \psi_k$ for all $\psi$;
> 2. no spinor $\psi \neq 0$ is left unchanged.
>
> The vector boost of the same parameters ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]) has eigenvalues $e^{\eta}, e^{-\eta}, 1, 1$ and leaves the two components transverse to $\hat{\mathbf n}$ invariant: a Dirac spinor has no transverse part.
>
> *Source: PHY 513, Problem Set 6, Problem 4(b) (statement, Larsen: "A boost leaves invariant the components of a 4-vector transverse to the boost. Does the Dirac spinor have any invariant components?"; answer "No", the boost along $z$ and the basis-independence argument, as the user wrote them) · the boost along $\hat{\mathbf n}$ and the bispinor reading written here*

^thm-c5a-4-6

> [!derivation]- Derivation
> **1. Along z, chiral basis (the user's answer).** With $\psi = (\psi^1_L, \psi^2_L, \psi^1_R, \psi^2_R)$ and part 1 of Theorem §C5a.4.5,
>
> $$
> \Lambda_{1/2}\psi = \begin{pmatrix} e^{-\eta/2}&0&0&0\\ 0&e^{\eta/2}&0&0\\ 0&0&e^{\eta/2}&0\\ 0&0&0&e^{-\eta/2} \end{pmatrix}\begin{pmatrix}\psi^1_L\\ \psi^2_L\\ \psi^1_R\\ \psi^2_R\end{pmatrix} = \begin{pmatrix}e^{-\eta/2}\psi^1_L\\ e^{\eta/2}\psi^2_L\\ e^{\eta/2}\psi^1_R\\ e^{-\eta/2}\psi^2_R\end{pmatrix} :
> $$
>
> for $\eta \neq 0$ every diagonal entry is $e^{\pm\eta/2} \neq 1$, so every component is rescaled. By contrast $\Lambda_z(\eta)$ has the entries $1$ at positions $(1,1)$ and $(2,2)$ and zeros elsewhere in those rows, which leave $x^1$, $x^2$ invariant.
>
> **2. Along any axis: the eigenvalues.** By step 4 of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^der-c5a-4-5|Derivation §C5a.4.5]], the upper block $C\,\mathbb 1 - S\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ has eigenvalues $C \mp S = e^{\mp\eta/2}$ on the eigenvectors of $\hat{\mathbf n}\cdot\boldsymbol\sigma$, and the lower block, its inverse, has $e^{\pm\eta/2}$. The eigenvalues of the block-diagonal $\Lambda_{1/2}$ are those of its blocks: $e^{\eta/2}$ and $e^{-\eta/2}$, each twice. For $\eta \neq 0$ none is $1$.
>
> **3. An invariant component is a unit row.** In a basis where the boost has the matrix $\Lambda'$, the component $k$ is invariant for every $\psi'$ iff $\sum_b\Lambda'_{kb}\psi'_b = \psi'_k$ for all $\psi'$; taking $\psi' = e_b$ gives $\Lambda'_{kb} = \delta_{kb}$, i.e. $e_k^{\mathsf T}\Lambda' = e_k^{\mathsf T}$.
>
> **4. Independence of the basis (the user's argument).** Let $S$ be the invertible change-of-basis matrix, $\psi' = S\psi$, $\Lambda' = S\Lambda_{1/2}S^{-1}$ (Theorem §CB.0.5; the user takes $S$ unitary and notes that any invertible $S$ works). Multiplying $e_k^{\mathsf T}\Lambda' = e_k^{\mathsf T}$ on the right by $S$:
>
> $$
> \bigl(e_k^{\mathsf T}S\bigr)\Lambda_{1/2} = e_k^{\mathsf T}S ,
> $$
>
> so the row $e_k^{\mathsf T}S$, nonzero because $S$ is invertible, would be a left eigenvector of $\Lambda_{1/2}$ with eigenvalue $1$. The left eigenvalues of a matrix are its eigenvalues ($\det(\Lambda^{\mathsf T} - \lambda) = \det(\Lambda - \lambda)$), and by step 2 none is $1$. So no component is invariant, in any basis. (Equivalently: eigenvalues do not depend on the basis, [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]], and a unit row $k$ makes $1$ an eigenvalue of $\Lambda'^{\mathsf T}$.)
>
> **5. No fixed spinor.** $\Lambda'\psi' = \psi'$ with $\psi' \neq 0$ would make $S^{-1}\psi' \neq 0$ an eigenvector of $\Lambda_{1/2}$ with eigenvalue $1$; excluded by step 2.
>
> **6. The vector, for contrast.** $\Lambda_z(\eta)$ has eigenvalues $e^{\pm\eta}$ on $e_0 \pm e_3$ and $1$ on $e_1$, $e_2$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]]); the two eigenvalues $1$ are the transverse directions.
>
> **What the derivation shows**
> - Every spinor component is stretched or shrunk, like the light-cone components $x^0 \pm x^3$ of a vector, never left alone like $x^1$, $x^2$. The transverse components are rebuilt from pairs of spinor directions: a boost along $z$ acts on the Hermitian matrix $X$ of a four-vector ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]]) as $X \mapsto \lambda X\lambda^\dagger$ with a diagonal $\lambda = \operatorname{diag}(a, a^{-1})$, $a = e^{\pm\eta/2}$ real ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]), which multiplies the diagonal entries $x^0 \mp x^3$ by $a^2$, $a^{-2}$ and the off-diagonal entries $-x^1 \pm ix^2$ by $a\cdot a^{-1} = 1$: a transverse component pairs a stretched with a shrunk spinor direction (written here).
> - The answer does not depend on the chiral basis: invariance of a component is a statement about eigenvalues, which no change of basis alters.
> - For rotations the same test fails too (eigenvalues $e^{\mp i\theta/2} \neq 1$ for $0 < \theta < 4\pi$, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]]), whereas a vector keeps its axis component: the spinor representation has no zero weight ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]).

^der-c5a-4-6

*Uses:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-5|Theorem §CB.0.5]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-4|Theorem §CB.15.4]]

## Three transformations that act on spinor indices

> [!caution] Caution: Three different transformations
> Three operations look alike on paper — a matrix multiplying $\psi$, sometimes a sandwich — and are unrelated:
>
> | | change of basis of $V$ | Lorentz transformation of a classical field | Lorentz transformation of the quantum field |
> |---|---|---|---|
> | what changes | the description (basis $e \to e'$) | the configuration (moved by $\Lambda$) | the state of the system, by $U(\Lambda)$ |
> | group | $GL(V)$, unitary for $\bar\psi$ to keep its form (Theorem §C5a.2.2) | $SL(2, \mathbb C)$ on $V$ together with $SO^+(1,3)$ on $M$ ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9\|Theorem §CB.15.9]]) | unitary operators on the Hilbert space ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^pr-c3-4-1\|Principle §C3.4.1]]) |
> | $\psi$ | $\psi'(x) = U\psi(x)$, same point | $\psi'(x) = \Lambda_{1/2}\psi(\Lambda^{-1}x)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1\|Def. §C5a.3.1]]) | $U(\Lambda)^{-1}\hat\psi(x)U(\Lambda) = \Lambda_{1/2}\hat\psi(\Lambda^{-1}x)$ ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1\|Principle §C3.5.1]]) |
> | $\gamma^\mu$ | $U\gamma^\mu U^{-1}$ | unchanged (Theorem §CB.17.8) | unchanged |
> | $\partial_\mu$ | unchanged | $\Lambda_\mu{}^\nu\partial_\nu$ (chain rule) | as for the classical field |
> | acts on | spinor index only | spinor index and argument | operator nature (sandwich) and, through the law, spinor index and argument |
> | predictions | unchanged (Remark: What depends on the basis, [[§C5a.7 The Dirac Equation and Its Lagrangian\|§C5a.7]]) | those of the moved system | those of the moved system |
>
> In the third column the sandwich $U(\Lambda)^{-1}\cdots U(\Lambda)$ acts on the Hilbert-space side of $\hat\psi$, while the single matrix $\Lambda_{1/2}$ acts on its spinor index (Yu (5.61); Peskin–Schroeder's equivalent form $U\hat\psi U^{-1} = \Lambda_{1/2}^{-1}\hat\psi(\Lambda x)$: [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-1|§C5b.4, Remark: Lorentz covariance of the quantized field]]; the two kinds of representation: [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]]). The letter $U$ is overloaded: the change-of-basis matrix $U$ is a constant $4\times4$ matrix, $U(\Lambda)$ an infinite-dimensional unitary operator. The operations are compatible: in a new basis the Lorentz law reads $\psi'(x) \mapsto \Lambda'_{1/2}\psi'(\Lambda^{-1}x)$ with $\Lambda'_{1/2} = U\Lambda_{1/2}U^{-1}$ (Theorem §CB.10.15, 2), since $U\Lambda_{1/2}\psi = (U\Lambda_{1/2}U^{-1})(U\psi)$.
>
> *Source: Yu §5.2, eqs. (5.55)–(5.61) · the user's pre-course notes, §5.2 (Note "Four linear spaces tied to Lorentz transformations": spinor space with $D(\Lambda)$, Hilbert space with $U(\Lambda)$, "a field carries several of these actions at once") · the user's PHY 513 notes, Ch. 10 §10.3 · PS §3.5, eqs. (3.108)–(3.110) · the table written here*

^cau-c5a-4-1

> [!remark]- Connections
> - That fields with half-integer $j_+ + j_-$ are two-valued is why their quanta obey Fermi statistics and are quantized with anticommutators — [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]], [[§C5b.9 Spin and Statistics|§C5b.9]].
> - The complex angles $\boldsymbol\theta \mp i\boldsymbol\eta$ of the factorization in §C3.2 are literally the arguments of $\Lambda_L$ and $\Lambda_R$, and complex conjugation exchanging them is $\Lambda_L^* = \sigma^2\Lambda_R\sigma^2$ — [[§CB.5 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-13|Theorem §CB.16.13]].
> - $\det X = x^2$ makes the Minkowski interval a determinant, exactly as the Euclidean length is $-\det(\mathbf x\cdot\boldsymbol\sigma)$; the light cone becomes the boundary of the cone of positive matrices, which is why null momenta factorize into spinors ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-3|§C5a.5, ★ Remark: Null vectors, spinors and the celestial sphere]]; helicity spinors, QFT §C5a.10) — [[§C3.7★ Massless Particles and Helicity#^def-c3-7-1|Def. §C3.7.1]].
> - Unitarity is lost with compactness: $SU(2) = S^3$ admits an invariant average and unitary representations, the $\mathbb R^3$ of boosts does not — [[§CB.6 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-6-16|Theorem §CB.6.16]], [[§CB.16 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-16-14|Theorem §CB.16.14]].
> - $\gamma^\mu$ is an invariant tensor exactly as the Pauli matrices are an invariant vector of $SU(2)$ ($U^\dagger\sigma^iU = R_{ij}\sigma^j$), the relation behind the covering $SU(2) \to SO(3)$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]].
> - Clifford multiplication being Lorentz equivariant is what makes $\slashed{\partial}\psi$ transform like $\psi$, hence the Dirac equation covariant and $\mathcal L$ a scalar; the same "invariant tensor" idea makes the Pauli matrices an invariant vector of $SU(2)$ — [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|§C5a.7, Remark: What covariance shows and what it does not]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
> - Rotations and boosts exponentiate by the same split of a series into even and odd powers, because the axis matrix squares to a multiple of the identity: $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \mathbb 1$ gives $\cos\frac\theta2$, $\cosh\frac\eta2$ for spinors, $[\hat{\mathbf n}]_\times^2 = -Q$ and $N_{\hat{\mathbf n}}^2 = \Pi$ give $\cos\theta$, $\cosh\eta$ for vectors — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]].
> - A change of basis of $V$ and a Lorentz transformation act on the same spinor index but belong to different groups, and the Hilbert-space $U(\Lambda)$ acts on yet another space; the three are kept apart in the field transformation laws of C3 — [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]].
