---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra]] →

*Sources: the user's PHY 513 notes, Ch. 1 §1.6, Ch. 7 §§7.3–7.5 · PHY 513 Lecture 7 (Larsen), Part B · PHY 513, Problem Set 4, Problem 5, and Problem Set 5, Problem 1 (as the user wrote them; submitted) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.1 · Yu Zhao-Huan, 量子场论讲义, §3.1–§3.2, §4.1 and Exercise 3.1 · the user's pre-course notes, §2.2 · the rest written here.*

Which commutation relations must the six Lorentz generators obey in every representation? The section gives the Lorentz algebra as the course derives it (PHY 513 Lecture 7, Part B; Problem Sets 4 and 5): the generators of a representation, their commutation relations with three derivations, the tensor law of the generators, and the vanishing of one-dimensional representations. Which real Lie algebra the generators form, and in which sense it is "two copies of the rotation algebra" — the split $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$, the real forms, and $\mathfrak{sl}(2, \mathbb C)$ as a real Lie algebra — is [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra|§CB.6]]. The physics that uses it, the indices of fields and their labels $(j_+, j_-)$, is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]].

*Conventions* (the course's, [[Larsen PHY 513]]): active reading; $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$; $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$ (Peskin–Schroeder's sign; Problem Set 5 uses the opposite one, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|Caution: Which one is (½, 0) depends on the sign of K]]); $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$, $\eta_i = \omega_{0i}$; $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$. Latin indices are Euclidean labels, summed when repeated. $V$ denotes the complex carrier space of a representation $D$, not Minkowski space; the generators carry no hat, as everywhere in CB.

## Generators and the Lorentz algebra

> [!definition] Definition §CB.5.1: Generators of a Representation
> Let $D$ be a representation of $SO^+(1,3)$ on a finite-dimensional complex vector space $V$. Its **generators** are the six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ on $V$ defined by
>
> $$
> D(e^{s\omega}) = \mathbb 1 - \frac{is}{2}\,\omega_{\mu\nu}\,D(\mathcal J^{\mu\nu}) + O(s^2) \quad\text{for every antisymmetric } \omega_{\mu\nu}, \qquad\text{so that}\qquad D(e^{\omega}) = \exp\Bigl(-\frac i2\,\omega_{\mu\nu}D(\mathcal J^{\mu\nu})\Bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Derivation "The Lorentz algebra from the group law alone"; Principle "How the parameters enter", eq. (Dlambda)) · PHY 513 Lecture 7, Part B ("All representations realize the abstract algebra") · PS §3.1, eqs. (3.13), (3.17) · Yu §3.2, eqs. (3.35)–(3.36)*

^def-cb-5-1

For the vector representation, $D(\Lambda) = \Lambda$, the generators are the $4\times4$ matrices $\mathcal J^{\mu\nu}$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]], 2). (The Lecture 7 slide "Vector Representation" prints their both-lower form as $i(\delta^\nu_\alpha\delta^\nu_\beta - \delta^\nu_\beta\delta^\mu_\alpha)$, with $\nu$ repeated; Peskin–Schroeder's (3.18) is $i(\delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha)$.) The exponential formula holds because $s \mapsto D(e^{s\omega})$ and $s \mapsto \exp(-\frac{is}{2}\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ are both one-parameter groups of matrices ($e^{s\omega}e^{t\omega} = e^{(s+t)\omega}$) with the same derivative at $s = 0$, and such a group is fixed by that derivative ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-8|Theorem §CB.3.8]]; for rotations, [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-3|QM Theorem §C5.1.3]]). The notation $D(\mathcal J^{\mu\nu})$ names *which* generator by its label pair and *how* it is realized by $D$; the realizations met in the course (the abstract $J^{\mu\nu}$, the orbital $L^{\mu\nu}$, the matrices $\mathcal J^{\mu\nu}$ and $S^{\mu\nu}$) are listed in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]].

The generators of the vector representation, their parameters and their exponentials, first written in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]] and restated here with their proofs (CB ordering pass, 2026-10-08); the Lie algebra they span is $\mathfrak{so}(1,3)$ of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], whose elements are the matrices $\omega = [\omega^\mu{}_\nu]$ with $\omega_{\mu\nu} = g_{\mu\rho}\omega^\rho{}_\nu$ antisymmetric (Step 6 of its proof: $X^{\mathsf T}\eta + \eta X = 0$ says that $\eta X$ is antisymmetric):

> [!definition] Definition §CB.5.2: The Generators of the Vector Representation
> The six **generators** $M^{\alpha\beta} = -M^{\beta\alpha}$ of the vector representation are the $4\times4$ matrices, and $\mathcal J^{\alpha\beta} = iM^{\alpha\beta}$ their Hermitian-convention form,
>
> $$
> (M^{\alpha\beta})^\mu{}_\nu = g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu, \qquad (\mathcal J^{\alpha\beta})^\mu{}_\nu = i\bigl(g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu\bigr),
> $$
>
> with $g$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]; for real **parameters** $\omega_{\alpha\beta} = -\omega_{\beta\alpha}$ the corresponding Lorentz transformation is
>
> $$
> \Lambda = \exp\Bigl(\tfrac12\,\omega_{\alpha\beta}M^{\alpha\beta}\Bigr) = \exp\Bigl(-\tfrac i2\,\omega_{\alpha\beta}\mathcal J^{\alpha\beta}\Bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Definition "Generators in the vector representation"), eq. (Mgenerators); Ch. 7, eq. (Jvector) · PHY 513 Lecture 7 · PHY 513, Problem Set 4, Problem 5, eq. (14) (statement) · Peskin & Schroeder, eq. (3.18) · the course's version: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], the same definition.*

^def-cb-5-2

> [!theorem] Theorem §CB.5.3: The Generators Reproduce ω
> 1. As matrices acting on $v^\nu$, $\ \frac12\omega_{\alpha\beta}(M^{\alpha\beta})^\mu{}_\nu = -\frac i2\omega_{\alpha\beta}(\mathcal J^{\alpha\beta})^\mu{}_\nu = \omega^\mu{}_\nu$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]). Hence the Lorentz transformation of Def. §CB.5.2 is the matrix exponential $\Lambda = e^{\omega}$ of $\omega = [\omega^\mu{}_\nu] \in \mathfrak{so}(1,3)$, infinitesimally $\delta v^\mu = \omega^\mu{}_\nu v^\nu$, and the $M^{\alpha\beta}$ with $\alpha < \beta$ are a basis of $\mathfrak{so}(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]).
> 2. The generators ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]) of the vector representation $D(\Lambda) = \Lambda$ are the matrices $\mathcal J^{\mu\nu}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (check after eq. (Mgenerators)); Ch. 7 (paragraph "The vector representation"; Derivation "What the vector generators do") · Yu §4.1 · the course's version: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], part 1; part 2 is the sentence after Def. §CB.5.1.*

^thm-cb-5-3

> [!proof]- Proof
> *The derivation of Theorem §C1a.6.2, unchanged in steps 1–5; steps 6–7 added.*
>
> **1. Contract the first term.** $\frac12\omega_{\alpha\beta}\,g^{\alpha\mu}\delta^\beta{}_\nu = \frac12\,g^{\mu\alpha}\omega_{\alpha\nu} = \frac12\,\omega^\mu{}_\nu$ (the delta substitutes $\beta \to \nu$; the metric raises $\alpha$, [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]).
>
> **2. Contract the second term.** $-\frac12\omega_{\alpha\beta}\,g^{\beta\mu}\delta^\alpha{}_\nu = -\frac12\,\omega_{\nu\beta}\,g^{\beta\mu} = -\frac12\,\omega_\nu{}^\mu$.
>
> **3. Use antisymmetry.** $\omega_\nu{}^\mu = g^{\mu\beta}\omega_{\nu\beta} = -g^{\mu\beta}\omega_{\beta\nu} = -\omega^\mu{}_\nu$. So step 2 is $+\frac12\omega^\mu{}_\nu$, and the sum of steps 1–2 is $\omega^\mu{}_\nu$: the $\frac12$ has disappeared, as it should.
>
> **4. The Hermitian form.** $-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta} = -\frac i2\cdot i\,\omega_{\alpha\beta}M^{\alpha\beta} = \frac12\omega_{\alpha\beta}M^{\alpha\beta}$, since $-i\cdot i = 1$.
>
> **5. Exponential and first order.** The exponent of Def. §CB.5.2 is therefore the matrix $\omega = [\omega^\mu{}_\nu]$, and $\Lambda = e^\omega = \mathbb 1 + \omega + O(\omega^2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]]), so $\delta v^\mu = \omega^\mu{}_\nu v^\nu$.
>
> **6. A basis of 𝔰𝔬(1,3).** By Theorem §CB.1.17, $\mathfrak{so}(1,3)$ consists of the real $\omega$ with $g\omega$ antisymmetric, i.e. with $\omega_{\mu\nu} = g_{\mu\rho}\omega^\rho{}_\nu = -\omega_{\nu\mu}$. By step 3 every such $\omega$ is $\frac12\omega_{\alpha\beta}M^{\alpha\beta} = \sum_{\alpha<\beta}\omega_{\alpha\beta}M^{\alpha\beta}$ (the terms with $\alpha > \beta$ repeat those with $\alpha < \beta$), and conversely each $M^{\alpha\beta}$ is the $\omega$ with $\omega_{\alpha\beta} = -\omega_{\beta\alpha} = 1$ and all other entries $0$. The six $M^{\alpha\beta}$, $\alpha < \beta$, span $\mathfrak{so}(1,3)$ and, being six vectors in a six-dimensional space, are a basis.
>
> **7. Part 2.** For $D(\Lambda) = \Lambda$, steps 3–5 give $D(e^{s\omega}) = e^{s\omega} = \mathbb 1 + s\omega + O(s^2) = \mathbb 1 - \frac{is}{2}\omega_{\mu\nu}\mathcal J^{\mu\nu} + O(s^2)$, the defining expansion of Def. §CB.5.1 with $D(\mathcal J^{\mu\nu}) = \mathcal J^{\mu\nu}$.
>
> **What the proof shows**
> - The generators need not be guessed: they are read off by writing $\omega^\mu{}_\nu$ as $\frac12\omega_{\alpha\beta}(\cdots)^\mu{}_\nu$ (raise, antisymmetrize, insert a delta for each free index); the same recipe gives the spin generators of any field (the course's [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]).
> - Equivalence: part 1 is [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], with the basis statement of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]] (infinitesimal Lorentz transformations are antisymmetric) read through Theorem §CB.1.17.

^pf-cb-5-3

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]

> [!definition] Definition §CB.5.4: Rotation and Boost Generators
> For generators $\mathcal J^{\mu\nu}$ (those of the vector representation, [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]], or $D(\mathcal J^{\mu\nu})$ of any representation, [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]) the **rotation and boost generators** are
>
> $$
> J_i = \tfrac12\varepsilon_{ijk}\mathcal J^{jk}, \quad\text{i.e.}\quad \mathbf J = (\mathcal J^{23}, \mathcal J^{31}, \mathcal J^{12}); \qquad K_i = \mathcal J^{0i}, \quad\text{i.e.}\quad \mathbf K = (\mathcal J^{01}, \mathcal J^{02}, \mathcal J^{03}) ,
> $$
>
> with $\varepsilon_{ijk}$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]. With the **angles** $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and **rapidities** $\eta_i = \omega_{0i}$, $\ -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\,\boldsymbol\theta\cdot\mathbf J - i\,\boldsymbol\eta\cdot\mathbf K$, so $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$; in particular $e^{-i\theta J_3} = e^{\theta M^{12}}$ and $e^{-i\eta K_3} = e^{\eta M^{03}}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Principle "The Lorentz algebra in terms of rotations and boosts") · Yu §3.1, eqs. (3.37)–(3.38) · [[Larsen PHY 513]] (boost generator $K^i = J^{0i}$; the opposite sign $K_i = \mathcal J^{i0}$ of some sources: [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]) · the course's version: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], the same definition (the regrouping is the six-term sum $\sum_{\mu<\nu}\omega_{\mu\nu}\mathcal J^{\mu\nu}$ written by index type).*

^def-cb-5-4

> [!theorem] Theorem §CB.5.5: Rotations and Boosts as Exponentials
> With $M^{\alpha\beta}$ of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]:
> 1. **Rotation about $x^3$**, $\omega_{12} = -\omega_{21} = \theta$: $\omega^1{}_2 = -\theta$, $\omega^2{}_1 = \theta$, and $e^{\theta M^{12}}$ acts on $(x^1, x^2)$ as $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ and as the identity on $x^0, x^3$; $(M^{12})^2 = -\mathbb 1$ on that block.
> 2. **Boost along $x^3$**, $\omega_{03} = -\omega_{30} = \eta$: $\omega^0{}_3 = \omega^3{}_0 = \eta$, and $e^{\eta M^{03}}$ acts on $(x^0, x^3)$ as $B_3(\eta) = \begin{pmatrix} \cosh\eta & \sinh\eta \\ \sinh\eta & \cosh\eta \end{pmatrix}$ and as the identity on $x^1, x^2$; $(M^{03})^2 = +\mathbb 1$ on that block.
> 3. Generally $e^{\theta M^{jk}} = \operatorname{diag}\bigl(1, R(\hat{\mathbf e}_i, \theta)\bigr)$, $(ijk)$ cyclic, the rotation by $\theta$ about $x^i$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]]), and $e^{\eta M^{0i}}$ the boost of rapidity $\eta$ along $+x^i$.
> 4. For a unit vector $\hat{\mathbf n} \in \mathbb R^3$, $e^{\eta\,n_iM^{0i}} = B(u)$ with $u = (\cosh\eta, \sinh\eta\,\hat{\mathbf n})$, the pure boost taking $e_0$ to $u$ of [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|Theorem §CB.3.13]]; so a boost along $\hat{\mathbf n}$ is $e^\omega$ with $\omega_{0i} = \eta n_i$, $\omega_{ij} = 0$, and every $B(u)$ is of this form.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Definition "Generators in the vector representation", sorted by index type; Caution "A mixed pair"); Ch. 7 (Derivation "What the vector generators do") · PHY 513 Lecture 7 (Examples "Rotation around z-axis", "Boost along x-axis") · part 4 written here · the course's version: [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], parts 1–3 the same, with the matrices of the active rotation and boost of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]].*

^thm-cb-5-5

> [!proof]- Proof
> *Steps 1–6 are the derivation of Theorem §C1a.6.3 with the citations replaced; step 7 (part 4) is written here.*
>
> **1. The matrix $M^{12}$.** From Def. §CB.5.2, $(M^{12})^\mu{}_\nu = g^{1\mu}\delta^2{}_\nu - g^{2\mu}\delta^1{}_\nu$. The only nonzero entries: $(\mu, \nu) = (1, 2)$ gives $g^{11} = -1$; $(\mu, \nu) = (2, 1)$ gives $-g^{22} = +1$. On $(x^1, x^2)$, $M^{12} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \equiv \epsilon$, zero elsewhere.
>
> **2. Its parameters.** With $\omega_{12} = -\omega_{21} = \theta$ and the rest zero, $\frac12\omega_{\alpha\beta}M^{\alpha\beta} = \frac12(\theta M^{12} + (-\theta)M^{21}) = \theta M^{12}$; raising the first index of $\omega$: $\omega^1{}_2 = g^{11}\omega_{12} = -\theta$, $\omega^2{}_1 = g^{22}\omega_{21} = +\theta$, consistent with $\theta\epsilon$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]]).
>
> **3. Exponentiate.** $\epsilon^2 = -\mathbb 1_2$, so the even powers are $(-1)^n\theta^{2n}\mathbb 1_2$ and the odd ones $(-1)^n\theta^{2n+1}\epsilon$; summing the exponential series ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]]) separately,
>
> $$
> e^{\theta\epsilon} = \cos\theta\,\mathbb 1_2 + \sin\theta\,\epsilon = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
> $$
>
> and $e^{\theta M^{12}}$ is the identity on $x^0$, $x^3$. Applied to $\hat{\mathbf x}$ it gives $(\cos\theta, \sin\theta)$: counterclockwise, active.
>
> **4. The matrix $M^{03}$.** $(M^{03})^\mu{}_\nu = g^{0\mu}\delta^3{}_\nu - g^{3\mu}\delta^0{}_\nu$: $(\mu, \nu) = (0, 3)$ gives $g^{00} = 1$; $(3, 0)$ gives $-g^{33} = +1$. On $(x^0, x^3)$, $M^{03} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \equiv \sigma$, symmetric, with $\sigma^2 = +\mathbb 1_2$. With $\omega_{03} = -\omega_{30} = \eta$: $\omega^0{}_3 = g^{00}\eta = \eta$, $\omega^3{}_0 = g^{33}(-\eta) = \eta$.
>
> **5. Exponentiate.** Even powers $\eta^{2n}\mathbb 1_2$, odd powers $\eta^{2n+1}\sigma$, so $e^{\eta\sigma} = \cosh\eta\,\mathbb 1_2 + \sinh\eta\,\sigma = B_3(\eta)$. On $e_0 = (1, 0)$: $(1, 0) \mapsto (\cosh\eta, \sinh\eta)$, velocity $\tanh\eta$ along $+x^3$.
>
> **6. The other axes.** For $(ijk) = (1,2,3), (2,3,1), (3,1,2)$ the computation of step 1 gives $(M^{jk})^j{}_k = g^{jj} = -1$, $(M^{jk})^k{}_j = +1$, all other entries $0$: on the spatial components $M^{jk}$ is the matrix with $(j, k)$ entry $-1 = -\varepsilon_{ijk}$ and $(k, j)$ entry $+1 = -\varepsilon_{ikj}$, i.e. $(A_i)_{lm} = -\varepsilon_{ilm}$ of [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]]. So $e^{\theta M^{jk}} = \operatorname{diag}(1, e^{\theta A_i}) = \operatorname{diag}(1, R(\hat{\mathbf e}_i, \theta))$. Step 4 with $3 \to i$ gives the boost along $x^i$. ⚑ By-product: rotations exponentiate to trigonometric functions because $\epsilon^2 = -1$, boosts to hyperbolic ones because $\sigma^2 = +1$; that sign is the metric's, and it is why rotation angles are periodic and rapidities are not.
>
> **7. Part 4.** Let $N = n_iM^{0i}$. By step 4 (with $3 \to i$), $(M^{0i})^0{}_i = (M^{0i})^i{}_0 = 1$ and all other entries vanish, so in block form $N = \begin{pmatrix} 0 & \hat{\mathbf n}^{\mathsf T} \\ \hat{\mathbf n} & 0 \end{pmatrix}$, and $N^2 = \begin{pmatrix} 1 & 0 \\ 0 & \hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix}$ (using $\hat{\mathbf n}^{\mathsf T}\hat{\mathbf n} = 1$), $N^3 = N$. Hence the even powers $N^{2m}$, $m \ge 1$, all equal $N^2$ and the odd powers equal $N$, and the exponential series sums to
>
> $$
> e^{\eta N} = \mathbb 1 + \sinh\eta\,N + (\cosh\eta - 1)\,N^2 = \begin{pmatrix} \cosh\eta & \sinh\eta\,\hat{\mathbf n}^{\mathsf T} \\ \sinh\eta\,\hat{\mathbf n} & \mathbb 1_3 + (\cosh\eta - 1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix} .
> $$
>
> With $\gamma = \cosh\eta$ and $\mathbf u = \sinh\eta\,\hat{\mathbf n}$: $\mathbf u\mathbf u^{\mathsf T}/(1 + \gamma) = \sinh^2\eta\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}/(1 + \cosh\eta) = (\cosh\eta - 1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}$ (because $\sinh^2\eta = (\cosh\eta - 1)(\cosh\eta + 1)$), so this is the matrix $B(u)$ of Theorem §CB.3.13, 1. Its parameters: $\frac12\omega_{\alpha\beta}M^{\alpha\beta} = \eta N$ means $\omega_{0i} = \eta n_i$ and $\omega_{ij} = 0$. Conversely every future unit timelike $u = (\gamma, \mathbf u)$ is $(\cosh\eta, \sinh\eta\,\hat{\mathbf n})$ for $\eta = \operatorname{arccosh}\gamma \ge 0$ and a unit $\hat{\mathbf n}$ ($\hat{\mathbf n} = \mathbf u/|\mathbf u|$ if $\mathbf u \ne 0$, any if $\mathbf u = 0$), since $\gamma^2 - \mathbf u^2 = 1$.
>
> **What the proof shows**
> - The slide's rotation matrix (with $+\sin\theta$ upper right) is $e^{-\theta M^{12}}$, the passive rotation (the course's [[§C1a.4 The Lorentz Group#^cau-c1a-4-3|§C1a.4, Caution: The slides' rotation matrix is passive]]); its boost is $e^{\eta M^{03}}$ as written.
> - $e^{\eta_1M^{03}}e^{\eta_2M^{03}} = e^{(\eta_1 + \eta_2)M^{03}}$ (commuting exponents): rapidities add along one axis because they are parameters of a one-parameter subgroup; with Theorem §CB.3.13, every element of $SO^+(1,3)$ is a product of two exponentials, a boost and a rotation.
> - Equivalence: parts 1–3 are [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]; there $B_3(\eta)$ is the active boost $B_z$ of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]] written with the rapidity of [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]].

^pf-cb-5-5

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|Theorem §CB.3.13]]

> [!theorem] Theorem §CB.5.6: The Lorentz Algebra
> The generators $D(\mathcal J^{\mu\nu})$ of every representation ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]), written $\mathcal J^{\mu\nu}$, among them the $4\times4$ matrices of the vector representation ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]), obey
>
> $$
> [\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i\bigl(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho}\bigr),
> $$
>
> equivalently, in terms of the rotation and boost generators $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-4|Def. §CB.5.4]]),
>
> $$
> [J_i, J_j] = i\varepsilon_{ijk}J_k, \qquad [J_i, K_j] = i\varepsilon_{ijk}K_k, \qquad [K_i, K_j] = -i\varepsilon_{ijk}J_k ,
> $$
>
> The complex combinations $\mathbf J_\pm$ that split this algebra into two commuting angular momenta are [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|Theorem §CB.6.2]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Principle "The Lorentz algebra in terms of rotations and boosts", eq. (JKalgebra); checked numerically there in the vector representation, and checked again here) · PHY 513, Problem Set 4, Problem 5, eq. (15) (statement) · Yu §3.1, eq. (3.63)*

^thm-cb-5-6

> [!derivation]- Derivation (from the group law: every representation)
> Let $D$ be a representation of $SO^+(1,3)$ on a finite-dimensional complex space, $D(\Lambda_1)D(\Lambda_2) = D(\Lambda_1\Lambda_2)$, $D(\mathbb 1) = \mathbb 1$, differentiable at the identity. Its generators $J^{\mu\nu} \equiv D(\mathcal J^{\mu\nu}) = -J^{\nu\mu}$ are defined by the first-order term along one-parameter subgroups, $D(e^{s\omega}) = \mathbb 1 - \frac{is}{2}\,\omega_{\mu\nu}J^{\mu\nu} + O(s^2)$ for every antisymmetric $\omega_{\mu\nu}$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]); for the vector representation $D(\Lambda) = \Lambda$ they are the $\mathcal J^{\mu\nu}$ of Def. §CB.5.2 (Theorem §CB.5.3).
>
> **1. Conjugate a one-parameter subgroup.** Fix $\Lambda \in SO^+(1,3)$ and an antisymmetric $\omega'_{\mu\nu}$. The path $s \mapsto e^{s\omega'}$ lies in $SO^+(1,3)$ (Theorem §CB.1.17), and conjugation passes through the power series, $(\Lambda^{-1}A\Lambda)^n = \Lambda^{-1}A^n\Lambda$, so
>
> $$
> \Lambda^{-1}e^{s\omega'}\Lambda = e^{s\,\Lambda^{-1}\omega'\Lambda} .
> $$
>
> **2. Lower the indices of the conjugated matrix.** From $\Lambda^{\mathsf T}g\Lambda = g$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]), $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\kappa{}_\alpha = g^{\kappa\tau}\Lambda^\lambda{}_\tau\,g_{\lambda\alpha}$. Then
>
> $$
> (\Lambda^{-1}\omega'\Lambda)_{\mu\nu} \equiv g_{\mu\kappa}(\Lambda^{-1})^\kappa{}_\alpha\,\omega'^\alpha{}_\beta\,\Lambda^\beta{}_\nu = g_{\mu\kappa}g^{\kappa\tau}\Lambda^\lambda{}_\tau\,g_{\lambda\alpha}\,\omega'^\alpha{}_\beta\,\Lambda^\beta{}_\nu = \Lambda^\lambda{}_\mu\,\omega'_{\lambda\beta}\,\Lambda^\beta{}_\nu ,
> $$
>
> using $g_{\mu\kappa}g^{\kappa\tau} = \delta_\mu{}^\tau$ and $g_{\lambda\alpha}\omega'^\alpha{}_\beta = \omega'_{\lambda\beta}$. Exchanging $\mu \leftrightarrow \nu$ and renaming the dummies $\lambda \leftrightarrow \beta$ gives $\Lambda^\beta{}_\nu\,\omega'_{\beta\lambda}\,\Lambda^\lambda{}_\mu = -\Lambda^\lambda{}_\mu\,\omega'_{\lambda\beta}\,\Lambda^\beta{}_\nu$: the conjugated matrix is again antisymmetric with lower indices, i.e. again in the Lie algebra (Theorem §CB.1.17).
>
> **3. The group law, to first order in s.** The representation property, used twice with $D(\Lambda^{-1}) = D(\Lambda)^{-1}$, gives $D(\Lambda)^{-1}D(e^{s\omega'})D(\Lambda) = D(\Lambda^{-1}e^{s\omega'}\Lambda) = D(e^{s\Lambda^{-1}\omega'\Lambda})$. Expand both sides with the definition of the generators and drop $O(s^2)$:
>
> $$
> \mathbb 1 - \frac{is}{2}\,\omega'_{\rho\sigma}\,D(\Lambda)^{-1}J^{\rho\sigma}D(\Lambda) = \mathbb 1 - \frac{is}{2}\,(\Lambda^{-1}\omega'\Lambda)_{\mu\nu}J^{\mu\nu} = \mathbb 1 - \frac{is}{2}\,\omega'_{\rho\sigma}\,\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu\,J^{\mu\nu} ,
> $$
>
> the last step inserting step 2 and renaming the dummies $\lambda \to \rho$, $\beta \to \sigma$.
>
> **4. Compare coefficients: the tensor law.** Both coefficients of $\omega'_{\rho\sigma}$ are antisymmetric in $\rho\sigma$ ($J^{\rho\sigma}$ is; in $\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu J^{\mu\nu}$ exchange $\rho \leftrightarrow \sigma$ and rename $\mu \leftrightarrow \nu$). An antisymmetric $X^{\rho\sigma}$ with $\omega'_{\rho\sigma}X^{\rho\sigma} = 0$ for every antisymmetric $\omega'$ vanishes: the choice $\omega'_{01} = -\omega'_{10} = 1$, all else $0$, gives $2X^{01} = 0$, and likewise for each of the six pairs. Hence, for every finite $\Lambda$,
>
> $$
> D(\Lambda)^{-1}\,J^{\rho\sigma}\,D(\Lambda) = \Lambda^\rho{}_\mu\,\Lambda^\sigma{}_\nu\,J^{\mu\nu} .
> $$
>
> ⚑ By-product: the generators of any representation transform under conjugation as a tensor with two upper indices → [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-8|Theorem §CB.5.8]].
>
> **5. Make Λ infinitesimal: the left side.** Put $\Lambda = e^{t\omega}$ and keep first order in $t$ (absorbed into $\omega$ below): $D(\Lambda) = \mathbb 1 - \frac i2\omega_{\alpha\beta}J^{\alpha\beta} + O(\omega^2)$ and $D(\Lambda)^{-1} = \mathbb 1 + \frac i2\omega_{\alpha\beta}J^{\alpha\beta} + O(\omega^2)$ (their product is $\mathbb 1 + O(\omega^2)$). Expanding the triple product into its four terms and dropping the one of second order,
>
> $$
> \Bigl(\mathbb 1 + \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}\Bigr)J^{\rho\sigma}\Bigl(\mathbb 1 - \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}\Bigr) = J^{\rho\sigma} + \tfrac i2\omega_{\alpha\beta}J^{\alpha\beta}J^{\rho\sigma} - \tfrac i2\omega_{\alpha\beta}J^{\rho\sigma}J^{\alpha\beta} + O(\omega^2) = J^{\rho\sigma} + \tfrac i2\,\omega_{\alpha\beta}\,[J^{\alpha\beta}, J^{\rho\sigma}] + O(\omega^2) .
> $$
>
> **6. The right side.** With $\Lambda^\rho{}_\mu = \delta^\rho{}_\mu + \omega^\rho{}_\mu + O(\omega^2)$, the product has four terms:
>
> $$
> (\delta^\rho{}_\mu + \omega^\rho{}_\mu)(\delta^\sigma{}_\nu + \omega^\sigma{}_\nu)J^{\mu\nu} = J^{\rho\sigma} + \omega^\rho{}_\mu J^{\mu\sigma} + \omega^\sigma{}_\nu J^{\rho\nu} + \omega^\rho{}_\mu\omega^\sigma{}_\nu J^{\mu\nu} ;
> $$
>
> the last is second order and is dropped.
>
> **7. Write the right side with the lower-index ω, antisymmetrized.** Raise with the metric and rename the dummy $\mu \to \beta$: $\omega^\rho{}_\mu J^{\mu\sigma} = g^{\rho\alpha}\omega_{\alpha\beta}J^{\beta\sigma}$. Write it as two halves and in the second rename $\alpha \leftrightarrow \beta$, then use $\omega_{\beta\alpha} = -\omega_{\alpha\beta}$:
>
> $$
> g^{\rho\alpha}\omega_{\alpha\beta}J^{\beta\sigma} = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma}\bigr), \qquad \omega^\sigma{}_\nu J^{\rho\nu} = g^{\sigma\alpha}\omega_{\alpha\beta}J^{\rho\beta} = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> **8. Compare coefficients again.** Steps 5–7 and the $J^{\rho\sigma}$ on both sides cancelling:
>
> $$
> \tfrac i2\,\omega_{\alpha\beta}\,[J^{\alpha\beta}, J^{\rho\sigma}] = \tfrac12\,\omega_{\alpha\beta}\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma} + g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> Both coefficients of $\omega_{\alpha\beta}$ are antisymmetric in $\alpha\beta$ (on the right, exchanging $\alpha \leftrightarrow \beta$ maps the four terms to minus themselves in the order 2, 1, 4, 3), so by the argument of step 4, after multiplying by $-2i$,
>
> $$
> [J^{\alpha\beta}, J^{\rho\sigma}] = -i\bigl(g^{\rho\alpha}J^{\beta\sigma} - g^{\rho\beta}J^{\alpha\sigma} + g^{\sigma\alpha}J^{\rho\beta} - g^{\sigma\beta}J^{\rho\alpha}\bigr) .
> $$
>
> **9. Rename to the standard form.** Rename $\alpha \to \mu$, $\beta \to \nu$, use $g^{\rho\mu} = g^{\mu\rho}$ etc., and distribute the $-i$:
>
> $$
> [J^{\mu\nu}, J^{\rho\sigma}] = i\bigl(g^{\nu\rho}J^{\mu\sigma} - g^{\mu\rho}J^{\nu\sigma} - g^{\mu\sigma}J^{\rho\nu} + g^{\nu\sigma}J^{\rho\mu}\bigr) .
> $$
>
> In the last two terms use the antisymmetry $J^{\rho\nu} = -J^{\nu\rho}$ and $J^{\rho\mu} = -J^{\mu\rho}$: $-g^{\mu\sigma}J^{\rho\nu} = +g^{\mu\sigma}J^{\nu\rho}$ and $+g^{\nu\sigma}J^{\rho\mu} = -g^{\nu\sigma}J^{\mu\rho}$. Reordering gives the covariant relation of Theorem §CB.5.6.
>
> **What the derivation shows**
> - Nothing but the multiplication law of the group and the definition of the generators entered, so the six generators of *every* representation obey the same relation with the same structure constants: the $4\times4$ matrices $\mathcal J^{\mu\nu}$ (checked directly in the second route below), the orbital operators on functions ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-2|Theorem §C3.3.2]]), the Dirac matrices $S^{\mu\nu}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|Theorem §CB.14.18]]) and the Hilbert-space charges ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]], where the same argument is run with unitary operators $U(\Lambda)$, as in Yu §3.2).
> - The finite identity of step 4 is the stronger statement; the algebra is its first-order part → [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^rem-cb-5-2|§CB.5, Remark: The algebra is the infinitesimal tensor law]].
> - Assumptions: $D$ is differentiable at the identity and multiplicative near it. For the spinor representations, defined on $SO^+(1,3)$ only up to a sign ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-8|Theorem §CB.17.8]]), the sign of $D(\Lambda)$ cancels between $D(\Lambda)^{-1}$ and $D(\Lambda)$ in step 4, and steps 5–9 use only elements near the identity, where the sign is fixed to $+$ by continuity.
> - Used next: the reduction to $\mathbf J$, $\mathbf K$ and $\mathbf J_\pm$ (third derivation below), and the classification of [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]].
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Derivation "The Lorentz algebra from the group law alone") · Yu §3.2, eqs. (3.30)–(3.33) (the same computation for the operators on states)*

^der-cb-5-6

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]

> [!derivation]- Derivation (second route: direct computation in the vector representation)
> This is the user's submitted solution of PHY 513 Problem Set 4, Problem 5(a), in the notation of this note. Work with the real matrices $M^{\mu\nu}$ of Def. §CB.5.2, $\mathcal J^{\mu\nu} = iM^{\mu\nu}$, so that $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i^2[M^{\mu\nu}, M^{\rho\sigma}]$; the factor $i^2$ is restored in step 7. Generator labels are $\mu\nu$, $\rho\sigma$; matrix indices $\alpha, \beta, \gamma$, with $\gamma$ summed.
>
> **1. The matrix commutator.** Its $(\alpha, \beta)$ entry is $([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta = (M^{\mu\nu})^\alpha{}_\gamma(M^{\rho\sigma})^\gamma{}_\beta - (M^{\rho\sigma})^\alpha{}_\gamma(M^{\mu\nu})^\gamma{}_\beta$, with $(M^{\mu\nu})^\alpha{}_\gamma = g^{\mu\alpha}\delta^\nu{}_\gamma - g^{\nu\alpha}\delta^\mu{}_\gamma$ and $(M^{\rho\sigma})^\gamma{}_\beta = g^{\rho\gamma}\delta^\sigma{}_\beta - g^{\sigma\gamma}\delta^\rho{}_\beta$.
>
> **2. The first product, all four terms.**
>
> $$
> (M^{\mu\nu})^\alpha{}_\gamma(M^{\rho\sigma})^\gamma{}_\beta = g^{\mu\alpha}\delta^\nu{}_\gamma g^{\rho\gamma}\delta^\sigma{}_\beta - g^{\mu\alpha}\delta^\nu{}_\gamma g^{\sigma\gamma}\delta^\rho{}_\beta - g^{\nu\alpha}\delta^\mu{}_\gamma g^{\rho\gamma}\delta^\sigma{}_\beta + g^{\nu\alpha}\delta^\mu{}_\gamma g^{\sigma\gamma}\delta^\rho{}_\beta .
> $$
>
> **3. Sum over γ.** Each $\delta^\cdot{}_\gamma$ sets $\gamma$ equal to its other index:
>
> $$
> (M^{\mu\nu}M^{\rho\sigma})^\alpha{}_\beta = g^{\mu\alpha}g^{\rho\nu}\delta^\sigma{}_\beta - g^{\mu\alpha}g^{\sigma\nu}\delta^\rho{}_\beta - g^{\nu\alpha}g^{\rho\mu}\delta^\sigma{}_\beta + g^{\nu\alpha}g^{\sigma\mu}\delta^\rho{}_\beta .
> $$
>
> **4. The second product.** It is the first with the labels exchanged, $\mu \leftrightarrow \rho$, $\nu \leftrightarrow \sigma$:
>
> $$
> (M^{\rho\sigma}M^{\mu\nu})^\alpha{}_\beta = g^{\rho\alpha}g^{\mu\sigma}\delta^\nu{}_\beta - g^{\rho\alpha}g^{\nu\sigma}\delta^\mu{}_\beta - g^{\sigma\alpha}g^{\mu\rho}\delta^\nu{}_\beta + g^{\sigma\alpha}g^{\nu\rho}\delta^\mu{}_\beta .
> $$
>
> **5. Subtract: eight terms.**
>
> $$
> \begin{aligned}
> ([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta = {}& g^{\mu\alpha}g^{\rho\nu}\delta^\sigma{}_\beta - g^{\mu\alpha}g^{\sigma\nu}\delta^\rho{}_\beta - g^{\nu\alpha}g^{\rho\mu}\delta^\sigma{}_\beta + g^{\nu\alpha}g^{\sigma\mu}\delta^\rho{}_\beta \\
> & - g^{\rho\alpha}g^{\mu\sigma}\delta^\nu{}_\beta + g^{\rho\alpha}g^{\nu\sigma}\delta^\mu{}_\beta + g^{\sigma\alpha}g^{\mu\rho}\delta^\nu{}_\beta - g^{\sigma\alpha}g^{\nu\rho}\delta^\mu{}_\beta .
> \end{aligned}
> $$
>
> **6. Pair the terms by the metric that carries only labels.** Pairing the first with the eighth, the second with the sixth, the third with the seventh and the fourth with the fifth (and using $g^{\rho\nu} = g^{\nu\rho}$ etc.),
>
> $$
> \begin{aligned}
> ([M^{\mu\nu}, M^{\rho\sigma}])^\alpha{}_\beta &= g^{\nu\rho}\bigl(g^{\mu\alpha}\delta^\sigma{}_\beta - g^{\sigma\alpha}\delta^\mu{}_\beta\bigr) + g^{\nu\sigma}\bigl(g^{\rho\alpha}\delta^\mu{}_\beta - g^{\mu\alpha}\delta^\rho{}_\beta\bigr) + g^{\mu\rho}\bigl(g^{\sigma\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\sigma{}_\beta\bigr) + g^{\mu\sigma}\bigl(g^{\nu\alpha}\delta^\rho{}_\beta - g^{\rho\alpha}\delta^\nu{}_\beta\bigr) \\
> &= g^{\nu\rho}(M^{\mu\sigma})^\alpha{}_\beta + g^{\nu\sigma}(M^{\rho\mu})^\alpha{}_\beta + g^{\mu\rho}(M^{\sigma\nu})^\alpha{}_\beta + g^{\mu\sigma}(M^{\nu\rho})^\alpha{}_\beta ,
> \end{aligned}
> $$
>
> each bracket being an entry of $M$ by Def. §CB.5.2. With $M^{\rho\mu} = -M^{\mu\rho}$ and $M^{\sigma\nu} = -M^{\nu\sigma}$, as matrices
>
> $$
> [M^{\mu\nu}, M^{\rho\sigma}] = g^{\nu\rho}M^{\mu\sigma} - g^{\mu\rho}M^{\nu\sigma} - g^{\nu\sigma}M^{\mu\rho} + g^{\mu\sigma}M^{\nu\rho} .
> $$
>
> **7. Restore i.** $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i^2[M^{\mu\nu}, M^{\rho\sigma}] = i\bigl(g^{\nu\rho}\,iM^{\mu\sigma} - g^{\mu\rho}\,iM^{\nu\sigma} - g^{\nu\sigma}\,iM^{\mu\rho} + g^{\mu\sigma}\,iM^{\nu\rho}\bigr) = i\bigl(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho}\bigr)$.
>
> **What the derivation shows**
> - The real matrices obey the algebra without any $i$: $[M^{\mu\nu}, M^{\rho\sigma}] = g^{\nu\rho}M^{\mu\sigma} - \dots$ is the real Lie algebra $\mathfrak{so}(1,3)$, and the $i$'s of the covariant relation are the price of the Hermitian convention $\mathcal J = iM$, as in Quantum Mechanics ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]]).
> - Using the mixed-index matrices avoids raising and lowering matrix indices; with Peskin–Schroeder's both-lower form the product rule is $(AB)_{\alpha\gamma} = A_{\alpha\beta}B^\beta{}_\gamma$, and the computation is the same.
> - It confirms the group-law derivation in one representation, as it must; it does not by itself say anything about other representations.
>
> *Source: the user's write-up of PHY 513, Problem Set 4, Problem 5(a) (submitted) · Yu §4.1, eqs. (4.5)–(4.6) · the user's pre-course notes, §2.2 (Example "The vector-representation matrices satisfy the algebra")*

^der-cb-5-6b

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]

> [!derivation]- Derivation (the J, K form and the J± split)
> This is the user's submitted solution of PHY 513 Problem Set 5, Problem 1(a), written with $K_i = \mathcal J^{0i}$ (Def. §CB.5.4); the problem set defines $K_i = \mathcal J^{i0}$, which changes nothing in the relations below (each is unchanged by $\mathbf K \to -\mathbf K$), but exchanges $\mathbf J_+ \leftrightarrow \mathbf J_-$. Here $\mathcal J^{\mu\nu}$ are the generators in any representation. Latin indices run over $1, 2, 3$, are summed when repeated, and their position carries no meaning; between spatial generator labels the metric is $g^{ij} = -\delta_{ij}$, and $g^{0i} = 0$, $g^{00} = 1$.
>
> **1. Invert the definitions.** $\varepsilon_{ijk}J_k = \frac12\varepsilon_{ijk}\varepsilon_{kab}\mathcal J^{ab} = \frac12(\delta_{ia}\delta_{jb} - \delta_{ib}\delta_{ja})\mathcal J^{ab} = \frac12(\mathcal J^{ij} - \mathcal J^{ji}) = \mathcal J^{ij}$, using $\varepsilon_{ijk}\varepsilon_{kab} = \delta_{ia}\delta_{jb} - \delta_{ib}\delta_{ja}$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]], three-dimensional form). Also $\mathcal J^{i0} = -\mathcal J^{0i} = -K_i$ and $\mathcal J^{aa} = 0$ (antisymmetry).
>
> **2. Rotations with rotations.** The $\varepsilon$'s are numbers, so $[J_i, J_j] = \frac14\varepsilon_{ikl}\varepsilon_{jmn}[\mathcal J^{kl}, \mathcal J^{mn}]$, and the covariant relation with all labels spatial gives
>
> $$
> [\mathcal J^{kl}, \mathcal J^{mn}] = i\bigl(g^{lm}\mathcal J^{kn} - g^{km}\mathcal J^{ln} - g^{ln}\mathcal J^{km} + g^{kn}\mathcal J^{lm}\bigr) = i\bigl(-\delta_{lm}\mathcal J^{kn} + \delta_{km}\mathcal J^{ln} + \delta_{ln}\mathcal J^{km} - \delta_{kn}\mathcal J^{lm}\bigr) .
> $$
>
> Contract each $\delta$ with the $\varepsilon$'s; each of the four terms equals $\mathcal J^{ij}$:
>
> $$
> \begin{aligned}
> -\varepsilon_{ikl}\varepsilon_{jln}\mathcal J^{kn} &= \varepsilon_{lik}\varepsilon_{ljn}\mathcal J^{kn} = (\delta_{ij}\delta_{kn} - \delta_{in}\delta_{kj})\mathcal J^{kn} = \delta_{ij}\mathcal J^{kk} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> \varepsilon_{ikl}\varepsilon_{jkn}\mathcal J^{ln} &= \varepsilon_{kli}\varepsilon_{knj}\mathcal J^{ln} = (\delta_{ln}\delta_{ij} - \delta_{lj}\delta_{in})\mathcal J^{ln} = \delta_{ij}\mathcal J^{ll} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> \varepsilon_{ikl}\varepsilon_{jml}\mathcal J^{km} &= \varepsilon_{lik}\varepsilon_{ljm}\mathcal J^{km} = (\delta_{ij}\delta_{km} - \delta_{im}\delta_{kj})\mathcal J^{km} = \delta_{ij}\mathcal J^{kk} - \mathcal J^{ji} = \mathcal J^{ij}, \\
> -\varepsilon_{ikl}\varepsilon_{jmk}\mathcal J^{lm} &= -\varepsilon_{kli}\varepsilon_{kjm}\mathcal J^{lm} = -(\delta_{lj}\delta_{im} - \delta_{lm}\delta_{ij})\mathcal J^{lm} = -\mathcal J^{ji} + \delta_{ij}\mathcal J^{ll} = \mathcal J^{ij},
> \end{aligned}
> $$
>
> where the first line used $\varepsilon_{ikl} = \varepsilon_{lik}$ (cyclic) and $\varepsilon_{jln} = -\varepsilon_{ljn}$, the others only cyclic permutations, and every line $\mathcal J^{kk} = 0$, $\mathcal J^{ji} = -\mathcal J^{ij}$. Hence $[J_i, J_j] = \frac i4\cdot4\,\mathcal J^{ij} = i\varepsilon_{ijk}J_k$ by step 1.
>
> **3. Rotations with boosts.** $[J_i, K_j] = \frac12\varepsilon_{ikl}[\mathcal J^{kl}, \mathcal J^{0j}]$, and the covariant relation with $(\mu\nu\rho\sigma) = (kl0j)$ gives, since $g^{l0} = g^{k0} = 0$,
>
> $$
> [\mathcal J^{kl}, \mathcal J^{0j}] = i\bigl(g^{l0}\mathcal J^{kj} - g^{k0}\mathcal J^{lj} - g^{lj}\mathcal J^{k0} + g^{kj}\mathcal J^{l0}\bigr) = i\bigl(\delta_{lj}\mathcal J^{k0} - \delta_{kj}\mathcal J^{l0}\bigr) = i\bigl(-\delta_{lj}K_k + \delta_{kj}K_l\bigr) .
> $$
>
> Contracting with $\frac12\varepsilon_{ikl}$: $[J_i, K_j] = \frac i2\bigl(-\varepsilon_{ikj}K_k + \varepsilon_{ijl}K_l\bigr) = \frac i2\bigl(\varepsilon_{ijk}K_k + \varepsilon_{ijk}K_k\bigr) = i\varepsilon_{ijk}K_k$, using $\varepsilon_{ikj} = -\varepsilon_{ijk}$ and renaming $l \to k$. So $\mathbf K$ is a vector under rotations.
>
> **4. Boosts with boosts.** With $(\mu\nu\rho\sigma) = (0i0j)$, $g^{i0} = g^{0j} = 0$, $g^{00} = 1$, $\mathcal J^{00} = 0$:
>
> $$
> [K_i, K_j] = [\mathcal J^{0i}, \mathcal J^{0j}] = i\bigl(g^{i0}\mathcal J^{0j} - g^{00}\mathcal J^{ij} - g^{ij}\mathcal J^{00} + g^{0j}\mathcal J^{i0}\bigr) = -i\,\mathcal J^{ij} = -i\varepsilon_{ijk}J_k .
> $$
>
> ⚑ By-product: the minus sign, $g^{00} = +1$ against $g^{ij} = -\delta_{ij}$, is the only place where the Minkowski signature enters → [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|Remark: Two boosts make a rotation]].
>
> **5. The reversed mixed commutator.** $[K_i, J_j] = -[J_j, K_i] = -i\varepsilon_{jik}K_k = i\varepsilon_{ijk}K_k$.
>
> ⚑ By-product: steps 6–7 below, the split into two commuting angular momenta, are the content of [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|Theorem §CB.6.2]], part 1, whose derivation uses them.
>
> **6. The two copies commute.** With $J_{\pm i} = \frac12(J_i \pm iK_i)$ and bilinearity, all four terms:
>
> $$
> [J_{+i}, J_{-j}] = \tfrac14\bigl([J_i, J_j] - i[J_i, K_j] + i[K_i, J_j] + [K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k + \varepsilon_{ijk}K_k - \varepsilon_{ijk}K_k - i\varepsilon_{ijk}J_k\bigr) = 0 ,
> $$
>
> using steps 2–5 term by term: $-i[J_i, K_j] = -i\cdot i\varepsilon_{ijk}K_k = \varepsilon_{ijk}K_k$; $i[K_i, J_j] = i\cdot i\varepsilon_{ijk}K_k = -\varepsilon_{ijk}K_k$; $[iK_i, -iK_j] = (i)(-i)[K_i, K_j] = [K_i, K_j] = -i\varepsilon_{ijk}J_k$.
>
> **7. Each copy is an angular momentum.** Same signs in both slots:
>
> $$
> [J_{\pm i}, J_{\pm j}] = \tfrac14\bigl([J_i, J_j] \pm i[J_i, K_j] \pm i[K_i, J_j] + (\pm i)^2[K_i, K_j]\bigr) = \tfrac14\bigl(i\varepsilon_{ijk}J_k \mp \varepsilon_{ijk}K_k \mp \varepsilon_{ijk}K_k + i\varepsilon_{ijk}J_k\bigr) = \tfrac i2\varepsilon_{ijk}\bigl(J_k \pm iK_k\bigr) = i\varepsilon_{ijk}J_{\pm k},
> $$
>
> with $(\pm i)\cdot i = \mp1$ in the two mixed terms and $(\pm i)^2\cdot(-i) = +i$ in the last; in the third step $\mp\frac12\varepsilon_{ijk}K_k = \frac i2\varepsilon_{ijk}(\pm iK_k)$.
>
> **8. Equivalence.** The change of basis is invertible over $\mathbb C$: $\mathbf J = \mathbf J_+ + \mathbf J_-$, $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$. Each of the fifteen commutators of the six $\mathcal J^{\mu\nu}$ is, up to sign, one of $[J_i, J_j]$, $[J_i, K_j]$, $[K_i, K_j]$, so the covariant relation, the $\mathbf J$, $\mathbf K$ relations and the $\mathbf J_\pm$ relations say the same thing (the converse direction is computed in [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|Theorem §CB.6.2]]).
>
> **What the derivation shows**
> - $\mathbf J$ closes on itself (the rotation subalgebra); $\mathbf K$ does not.
> - The split needs the complex combinations $\mathbf J \pm i\mathbf K$; with real coefficients no pair of commuting rotation algebras exists, because of the sign in step 4 (for $SO(4)$, where $[K_i, K_j] = +i\varepsilon_{ijk}J_k$, the real combinations $\frac12(\mathbf J \pm \mathbf K)$ do the job).
> - Which copy is then called $(\frac12, 0)$:([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]) (pointer moved here from the opening paragraph, CB ordering pass).
> - Used next: the classification of all finite-dimensional representations by two spins ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-2|Def. §CB.17.2]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|Theorem §CB.17.5]]).
>
> *Source: the user's write-up of PHY 513, Problem Set 5, Problem 1(a) (submitted) · the user's PHY 513 notes, Ch. 7 §7.4 (Derivation "The rotation–boost algebra and its complex split") · Yu §3.2, eqs. (3.39)–(3.41), (3.61)–(3.63), and Exercise 3.1 · the user's pre-course notes, §2.2 (Note "Deriving the component form")*

^der-cb-5-6c

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-4|Def. §CB.5.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-17|Theorem §CB.0.17]]

> [!remark] Remark: Where the Lorentz algebra is derived
> The three folded derivations under Theorem §CB.5.6 prove it: from the group law alone, hence in every representation at once (the user's PHY 513 notes, Ch. 7 §7.3; the same argument for the operators on states is Yu §3.2); by direct matrix computation in the vector representation (the user's submitted solution of PHY 513 Problem Set 4, Problem 5(a)); and the reduction to $\mathbf J$, $\mathbf K$ with the split into $\mathbf J_\pm$ (the user's submitted solution of Problem Set 5, Problem 1(a); Yu eqs. (3.39), (3.61)–(3.63) and Exercise 3.1). The finite statement behind the first route, that the generators of any representation transform as a tensor, is [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-8|Theorem §CB.5.8]]; what the $\mathbf J_\pm$ split buys, the classification of all finite-dimensional representations by two spins $(j_+, j_-)$, is [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6; Ch. 7 §§7.3–7.4 · the user's write-ups of PHY 513 Problem Set 4, Problem 5(a), and Problem Set 5, Problem 1(a) (both submitted)*

^rem-cb-5-1

> [!definition] Definition §CB.5.7: Representation of the Lorentz Algebra
> Six matrices $D(\mathcal J^{\mu\nu}) = -D(\mathcal J^{\nu\mu})$ on a complex vector space $V$ that obey the covariant relation of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] form a **representation of the Lorentz algebra** on $V$ (a representation of a Lie algebra in the sense of [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-5|Def. §CB.3.5]]). Its rotation and boost generators are $J_i = \frac12\varepsilon_{ijk}D(\mathcal J^{jk})$ and $K_i = D(\mathcal J^{0i})$, and its complex combinations $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 (Principle "How the parameters enter"), §7.4 ("The rotation–boost algebra and its complex split") · PHY 513 Lecture 7, Part B ("All representations realize the abstract algebra") · PS §3.1, eqs. (3.13), (3.17) · Yu §3.2, eqs. (3.35)–(3.36)*

^def-cb-5-7

> [!theorem] Theorem §CB.5.8: The Generators Transform as a Tensor
> 1. For every representation $D$ and every $\Lambda \in SO^+(1,3)$,
>
> $$
> D(\Lambda)^{-1}\,D(\mathcal J^{\rho\sigma})\,D(\Lambda) = \Lambda^\rho{}_\mu\,\Lambda^\sigma{}_\nu\,D(\mathcal J^{\mu\nu}) .
> $$
>
> 2. In particular, for a rotation $R$ ($\Lambda^0{}_0 = 1$, $\Lambda^i{}_j = R_{ij}$), $\mathbf J$ and $\mathbf K$ are vector operators: $D(R)^{-1}J_iD(R) = R_{ij}J_j$ and $D(R)^{-1}K_iD(R) = R_{ij}K_j$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3, eq. (gentensor) · Yu §3.1, eq. (3.22) (the same law for the operators on states)*

^thm-cb-5-8

> [!derivation]- Derivation
> **1. Part 1.** This is steps 1–4 of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6|Derivation §CB.5.6 (from the group law)]]: conjugate the one-parameter subgroup $e^{s\omega'}$ by $\Lambda$, lower the indices of $\Lambda^{-1}\omega'\Lambda$ to get $\Lambda^\rho{}_\mu\,\omega'_{\rho\sigma}\,\Lambda^\sigma{}_\nu$, apply $D$ and compare the coefficients of $\omega'_{\rho\sigma}$ at first order in $s$. Nothing in those steps depends on $D$ beyond $D(\Lambda_1)D(\Lambda_2) = D(\Lambda_1\Lambda_2)$; the sign ambiguity of a two-valued $D$ (Theorem §CB.17.8) cancels between $D(\Lambda)^{-1}$ and $D(\Lambda)$.
>
> **2. K under a rotation.** Put $(\rho, \sigma) = (0, i)$ in part 1. Since $\Lambda^0{}_\mu = \delta^0{}_\mu$ for a rotation, only $\mu = 0$ survives, and then $\nu$ must be spatial ($D(\mathcal J^{00}) = 0$): $D(R)^{-1}K_iD(R) = \Lambda^i{}_j\,D(\mathcal J^{0j}) = R_{ij}K_j$.
>
> **3. J under a rotation.** With $J_i = \frac12\varepsilon_{ijk}D(\mathcal J^{jk})$ and part 1 with spatial labels,
>
> $$
> D(R)^{-1}J_iD(R) = \tfrac12\varepsilon_{ijk}R_{jl}R_{km}\,D(\mathcal J^{lm}) .
> $$
>
> **4. The ε–determinant identity.** For any $3\times3$ matrix, $\varepsilon_{ajk}R_{an}R_{jl}R_{km} = (\det R)\,\varepsilon_{nlm}$ (the determinant as a triple product). Multiply by $R_{in}$, sum over $n$, and use $R_{in}R_{an} = \delta_{ia}$ ($RR^{\mathsf T} = \mathbb 1$): $\varepsilon_{ijk}R_{jl}R_{km} = (\det R)\,R_{in}\varepsilon_{nlm}$. With $\det R = 1$, step 3 becomes $R_{in}\cdot\frac12\varepsilon_{nlm}D(\mathcal J^{lm}) = R_{in}J_n$.
>
> **What the derivation shows**
> - The label pair of a generator is a pair of spacetime indices: it transforms with $\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu$, whatever space $D$ acts on. That is why the index rules of special relativity may be used on generator labels ([[§C3.1 Index Slots, Rotations and Spin in Field Theory#^def-c3-1-1|Def. §C3.1.1]]).
> - Part 2 is the vector-operator law of Quantum Mechanics, now for matrices acting on the indices of a field and with $\mathbf K$ included ([[§C7.2 Tensor Operators and the Wigner–Eckart Theorem#^def-c7-2-1|QM Def. §C7.2.1]]). Under a boost $\mathbf J$ and $\mathbf K$ mix, because $\Lambda^0{}_i \ne 0$.
> - Used next: its first-order form is the algebra ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^rem-cb-5-2|Remark: The algebra is the infinitesimal tensor law]]); for the operators on states the same law is [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-4|Theorem §C3.4.4]].

^der-cb-5-8

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6|Derivation §CB.5.6]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-1|Def. §CB.5.1]]

> [!remark] Remark: The algebra is the infinitesimal tensor law
> Put $\Lambda = 1 + \omega$ in Theorem §CB.5.8: the left side becomes $D(\mathcal J^{\rho\sigma}) + \frac i2\omega_{\alpha\beta}[D(\mathcal J^{\alpha\beta}), D(\mathcal J^{\rho\sigma})]$, the right side $D(\mathcal J^{\rho\sigma})$ plus $\omega$ acting on the two labels as on a two-index tensor, and equating them is the covariant relation of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] (steps 5–9 of its derivation). So "$[J^{\mu\nu}, J^{\rho\sigma}]$ is a combination of $g$'s and $J$'s" says no more than "the generators rotate into each other like an antisymmetric tensor". The algebra acting on itself in this way is its **adjoint representation**; for the Lorentz group it is the antisymmetric two-tensor, the representation of the field strength ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.3 ("This is the Lorentz algebra: the infinitesimal form of the statement that the generators transform as a tensor")*

^rem-cb-5-2

> [!theorem] Theorem §CB.5.9: One-Dimensional Representations of the Lorentz Algebra Are Zero
> Every one-dimensional representation of the Lorentz algebra is zero: six numbers $D(\mathcal J^{\mu\nu})$ that obey the relations of [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] all vanish.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.5 (Principle "Components and functions: the scalar field carries the trivial representation") · PHY 513, Problem Set 5, Problem 1(b) (spin 0: "the generators are numbers, which commute", as the user wrote it) · Yu §4.2.1, eq. (4.27)*

^thm-cb-5-9

> [!derivation]- Derivation
> **1. Numbers commute.** In one dimension the six generators are complex numbers, so every commutator vanishes.
>
> **2. The rotation generators vanish.** $[J_1, J_2] = iJ_3$, $[J_2, J_3] = iJ_1$, $[J_3, J_1] = iJ_2$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]]) with left sides $0$ give $\mathbf J = 0$.
>
> **3. The boost generators vanish.** $[J_1, K_2] = iK_3$, $[J_2, K_3] = iK_1$, $[J_3, K_1] = iK_2$ (the relation $[J_i, K_j] = i\varepsilon_{ijk}K_k$) with left sides $0$ give $\mathbf K = 0$.
>
> **What the derivation shows**
> - Only the brackets $[J_i, J_j]$ and $[J_i, K_j]$ are used: every generator is a commutator of two others, so a representation in which all generators commute, in particular every one-dimensional one, is zero (written here).
> - Its physical reading, the scalar field: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|Theorem §C3.3.4]].

^der-cb-5-9

*Uses:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]]

> [!remark]- Connections
> - **Used in**: Definition §CB.5.1 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded; cited in [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]]), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]]), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded; cited in [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]), [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|Theorem §CB.14.18]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation|§C3.5]] (cited in [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-3|Theorem §C3.5.3]]), [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]]); Definition §CB.5.2 — [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-4|Def. §CB.5.4]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-5|Theorem §CB.5.5]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-6|Theorem §CB.6.6]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-15|Theorem §CB.7.15]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|Theorem §CB.14.17]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-16-6|Def. §CB.16.6]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-13|Theorem §CB.16.13]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-5|Theorem §CB.18.5]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]], [[§CB.20★ The Poincaré Group and Induced Representations#^thm-cb-20-5|Theorem §CB.20.5]]; Theorem §CB.5.3 — [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-5|Theorem §CB.5.5]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-8|Theorem §CB.6.8]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]]; Definition §CB.5.4 — [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-1|Theorem §CB.6.1]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-8|Theorem §CB.6.8]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-15|Theorem §CB.7.15]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-16-6|Def. §CB.16.6]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-10|Theorem §CB.16.10]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-13|Theorem §CB.16.13]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]]; Theorem §CB.5.5 — [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-4|Theorem §CB.6.4]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^ex-cb-7-20|Example §CB.7.20]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-8|Theorem §CB.16.8]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-9|Theorem §CB.16.9]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-10|Theorem §CB.16.10]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-8|Theorem §CB.17.8]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-14|Theorem §CB.17.14]]; Definition §CB.5.7 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded); Theorem §CB.5.6 — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded), [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|Theorem §C3.3.4]]), [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded; cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^rem-c3-4-2|§C3.4, Remark: Two kinds of representation]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-5|Theorem §C3.4.5]]), [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation|§C3.5]] (embedded), [[§C3.7★ Massless Particles and Helicity|§C3.7★]] (embedded; cited in [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-2|Theorem §C3.7.2]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-5|Theorem §C3.7.5]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded), [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|Theorem §CB.14.18]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]]), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]] (cited in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]]), [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (cited in [[§C3.1 Index Slots, Rotations and Spin in Field Theory#^rem-c3-1-1|§C3.1, Remark: One symbol for each realization of the generators]]), [[§B1.2 Lorentz Transformations and the Lorentz Group|REL §B1.2]] (cited in [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-6|REL §B1.2, Remark: Infinitesimal Lorentz transformations]]); §CB.5, Remark: Where the Lorentz algebra is derived — [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields|§C3.2]] (embedded); Theorem §CB.5.9 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-4|Theorem §C3.3.4]]); Theorem §CB.5.8 — [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra|§C3.4]] (embedded; cited in [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-4|Theorem §C3.4.4]]), [[§C3.6★ Particle States and the Little Group|§C3.6★]] (embedded; cited in [[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]]).
