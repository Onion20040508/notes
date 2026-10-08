---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.5 Vectors, Tensors and Index Notation]] · ↑ [[· C1a Preliminaries]] · [[§C1a.7 Relativistic Electrodynamics in Index Form]] →

*Sources: the user's PHY 513 notes, Ch. 1 §1.6; Ch. 7 (paragraph "The vector representation", Derivations "What the vector generators do", "Every exponential exp(ω) is a proper orthochronous Lorentz transformation", Principle "Hermitian generators do not make boosts unitary") · PHY 513 Lecture 1 (Larsen), Part B; Lecture 7 · PHY 513, Problem Set 4, Problem 5 (statement; part (a) as the user wrote it) · PHY 513, Problem Set 5, Problem 1(a) (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, §3.1, eqs. (3.37)–(3.38), (3.63); §3.2, eqs. (3.30)–(3.33) · the user's pre-course notes, §1.7 (Example "Explicit vector-representation generators") · for the explicit matrices: the user's PHY 513 notes, Ch. 1 §1.2, eq. (rotboost), Ch. 8 §8.1 (Derivation "From six numbers to two matrices"); PHY 513 Lecture 1, Part B; Lecture 9, Part A; PS §3.1, eqs. (3.20)–(3.21), §3.3, eq. (3.48); Yu §1.3, eqs. (1.30)–(1.32), (1.36), Exercise 1.5; Sakurai §3.1.1 (as in QM §C5.1) · PHY 513, Problem Set 6, Problem 4(a), (c)–(d) (the user's solutions).*

What does the Lorentz group look like near the identity, and which objects does field theory actually use to describe it? [[§C1a.4 The Lorentz Group|§C1a.4]] studied finite elements. Near the identity the six parameters become the independent entries of one antisymmetric matrix $\omega_{\mu\nu}$, and every element of the identity component is built from exponentials of six fixed matrices, the **generators**. Relativity level B met the antisymmetry only in a ★ remark ([[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-6|REL ★ Remark: Infinitesimal Lorentz transformations]]); this note is its in-course home, adds the generators of the vector representation, their exponentials and the rotation and boost generators, writes all six generators and the finite rotations and boosts about and along any axis as explicit $4\times4$ matrices, and sets the conventions (active reading, Hermitian generators $\mathcal J = iM$) used for every field from here on. The commutation relations of the generators, the Lorentz algebra, are Lecture 7 material and live in [[§C3.2 The Lorentz Algebra|§C3.2]] ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]), derived there for every representation from the group law; the representations it classifies are [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]].

## The group near the identity

> [!theorem] Theorem §C1a.6.1: Infinitesimal Lorentz Transformations Are Antisymmetric
> Let $\Lambda(s)$ be a differentiable path in $O(1,3)$ with $\Lambda(0) = \mathbb 1$, so $\Lambda^\mu{}_\nu = \delta^\mu{}_\nu + s\,\omega^\mu{}_\nu + O(s^2)$ with $\omega = \Lambda'(0)$. Then
>
> $$
> \omega_{\mu\nu} \equiv g_{\mu\rho}\,\omega^\rho{}_\nu = -\omega_{\nu\mu} .
> $$
>
> The set of such $\omega$, the Lie algebra $\mathfrak{so}(1,3)$, is six-dimensional: three rotation parameters $\omega_{ij}$ and three boost parameters $\omega_{0i}$. The mixed-index $\omega^\mu{}_\nu$ is not antisymmetric. The infinitesimal transformation of coordinates is $\delta x^\mu = \omega^\mu{}_\nu x^\nu$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Derivation "Infinitesimal Lorentz transformations are antisymmetric"), eq. (omegaantisym) · PHY 513 Lecture 7 ("ω_μν are 6 'angles'")*

^thm-c1a-6-1

> [!derivation]- Derivation
> **1. Insert into the defining condition.** The covariant form $g_{\rho\sigma}\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu = g_{\mu\nu}$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]) holds for every $s$. Substitute $\Lambda^\rho{}_\mu = \delta^\rho{}_\mu + s\,\omega^\rho{}_\mu + O(s^2)$ and expand the product into all four terms:
>
> $$
> g_{\rho\sigma}\bigl(\delta^\rho{}_\mu + s\,\omega^\rho{}_\mu\bigr)\bigl(\delta^\sigma{}_\nu + s\,\omega^\sigma{}_\nu\bigr) = g_{\mu\nu} + s\,g_{\mu\sigma}\omega^\sigma{}_\nu + s\,g_{\rho\nu}\omega^\rho{}_\mu + s^2\,g_{\rho\sigma}\omega^\rho{}_\mu\omega^\sigma{}_\nu + O(s^2) .
> $$
>
> **2. Name the lowered matrix.** $g_{\mu\sigma}\omega^\sigma{}_\nu = \omega_{\mu\nu}$ and $g_{\rho\nu}\omega^\rho{}_\mu = g_{\nu\rho}\omega^\rho{}_\mu = \omega_{\nu\mu}$ (symmetry of $g$).
>
> **3. First order.** The left side must equal $g_{\mu\nu}$ for all $s$, so the coefficient of $s$ vanishes: $\omega_{\mu\nu} + \omega_{\nu\mu} = 0$. The $s^2$ terms constrain the second derivative of the path, not $\omega$.
>
> **4. Count.** An antisymmetric $4\times4$ matrix is fixed by its six entries above the diagonal. Conversely every antisymmetric $\omega_{\mu\nu}$ is the tangent of the path $s \mapsto e^{s\omega}$ in $SO^+(1,3)$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]), so the tangent space is exactly six-dimensional: the cleanest form of the count $3 + 3 = 6$ (three angles, three rapidities) of [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-6|REL Theorem §B1.2.6]], and of the naive count $16 - 10 = 6$ (sixteen entries of $\Lambda$, ten independent conditions in the symmetric matrix equation $\Lambda^{\mathsf T}g\Lambda = g$).
>
> **5. The mixed matrix.** Raising the first index, $\omega^0{}_i = g^{00}\omega_{0i} = \omega_{0i}$ and $\omega^i{}_0 = g^{ii}\omega_{i0} = -\omega_{i0} = \omega_{0i}$ (no sum on $i$): the boost block of $\omega^\mu{}_\nu$ is *symmetric*, because lowering the index $0$ costs no sign and lowering $i$ costs one. On the spatial block, $\omega^i{}_j = -\omega_{ij}$ is antisymmetric.
>
> **6. Coordinates.** $x'^\mu = \Lambda^\mu{}_\nu x^\nu = x^\mu + s\,\omega^\mu{}_\nu x^\nu + O(s^2)$; to first order $\delta x^\mu = \omega^\mu{}_\nu x^\nu$ (absorbing $s$ into $\omega$).
>
> **What the derivation shows**
> - Antisymmetry is a property of $\omega$ with *both indices down*; that is why the boost matrix of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]] is symmetric while a rotation matrix is not.
> - This is the Lorentz version of "the tangent space of $O(n)$ at the identity is the antisymmetric matrices" ([[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]), with $g$ in place of $\mathbb 1$: $\omega^{\mathsf T}g + g\omega = 0$.
> - Used next: the generators (Def. §C1a.6.1); the Lorentz Noether current, where $\delta x^\mu = \omega^\mu{}_\nu x^\nu$ is the displacement ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]]); the infinitesimal field law ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]).

^der-c1a-6-1

*Uses:* [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]

> [!remark] Remark: The factor ½ and why ω may be taken antisymmetric
> In $\frac12\omega_{\alpha\beta}M^{\alpha\beta}$ the sum runs over all sixteen pairs; since $\omega_{\alpha\beta}$ and $M^{\alpha\beta}$ are both antisymmetric, each independent pair appears twice, and the $\frac12$ undoes the double counting: $\frac12\omega_{\alpha\beta}M^{\alpha\beta} = \sum_{\alpha<\beta}\omega_{\alpha\beta}M^{\alpha\beta}$. A symmetric part of $\omega_{\alpha\beta}$ would contract to zero against the antisymmetric $M^{\alpha\beta}$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2), so taking $\omega$ antisymmetric loses nothing, and Theorem §C1a.6.1 says nothing else could arise anyway. Dropping the $\frac12$ (as in the handwritten form $\delta V^\beta = -i\omega_{\mu\nu}(\mathcal J^{\mu\nu})^\beta{}_\alpha V^\alpha$ recorded in the user's notes) doubles every angle.
>
> *Source: the user's PHY 513 notes, Ch. 7 (Principle on eq. (Dlambda): "Two conventions are hidden here"; Derivation "What the vector generators do")*

^rem-c1a-6-1

## Generators of the vector representation

> [!definition] Definition §C1a.6.1: Generators of the Vector Representation
> The six **generators** $M^{\alpha\beta} = -M^{\beta\alpha}$ are the $4\times4$ matrices, and $\mathcal J^{\alpha\beta} = iM^{\alpha\beta}$ their Hermitian-convention form,
>
> $$
> (M^{\alpha\beta})^\mu{}_\nu = g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu, \qquad (\mathcal J^{\alpha\beta})^\mu{}_\nu = i\bigl(g^{\alpha\mu}\delta^\beta{}_\nu - g^{\beta\mu}\delta^\alpha{}_\nu\bigr),
> $$
>
> and a Lorentz transformation with parameters $\omega_{\alpha\beta}$ is
>
> $$
> \Lambda = \exp\Bigl(\tfrac12\,\omega_{\alpha\beta}M^{\alpha\beta}\Bigr) = \exp\Bigl(-\tfrac i2\,\omega_{\alpha\beta}\mathcal J^{\alpha\beta}\Bigr) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Definition "Generators in the vector representation"), eq. (Mgenerators); Ch. 7, eq. (Jvector) · PHY 513 Lecture 7 · PHY 513, Problem Set 4, Problem 5, eq. (14) (statement) · Peskin & Schroeder, eq. (3.18), as quoted there · the user's pre-course notes, §1.7, eq. (vector-generators)*

^def-c1a-6-1

The form with both matrix indices down, $(\mathcal J^{\alpha\beta})_{\mu\nu} = i(\delta^\alpha_\mu\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\mu)$, is the one printed in Peskin–Schroeder and the slides; it is obtained by lowering $\mu$, but the matrix that multiplies a vector $v^\nu$ is the mixed one above.

> [!theorem] Theorem §C1a.6.2: The Generators Reproduce ω
> As matrices acting on $v^\nu$, $\ \frac12\omega_{\alpha\beta}(M^{\alpha\beta})^\mu{}_\nu = -\frac i2\omega_{\alpha\beta}(\mathcal J^{\alpha\beta})^\mu{}_\nu = \omega^\mu{}_\nu$. Hence the vector representation of Def. §C1a.6.1 is the matrix exponential $\Lambda = e^{\omega}$ of $\omega^\mu{}_\nu$, and infinitesimally $\delta v^\mu = \omega^\mu{}_\nu v^\nu$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (check after eq. (Mgenerators)); Ch. 7 (paragraph "The vector representation"; Derivation "What the vector generators do") · Yu §4.1 (as cited there)*

^thm-c1a-6-2

> [!derivation]- Derivation
> **1. Contract the first term.** $\frac12\omega_{\alpha\beta}\,g^{\alpha\mu}\delta^\beta{}_\nu = \frac12\,g^{\mu\alpha}\omega_{\alpha\nu} = \frac12\,\omega^\mu{}_\nu$ (the delta substitutes $\beta \to \nu$; the metric raises $\alpha$).
>
> **2. Contract the second term.** $-\frac12\omega_{\alpha\beta}\,g^{\beta\mu}\delta^\alpha{}_\nu = -\frac12\,\omega_{\nu\beta}\,g^{\beta\mu} = -\frac12\,\omega_\nu{}^\mu$.
>
> **3. Use antisymmetry.** $\omega_\nu{}^\mu = g^{\mu\beta}\omega_{\nu\beta} = -g^{\mu\beta}\omega_{\beta\nu} = -\omega^\mu{}_\nu$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]). So step 2 is $+\frac12\omega^\mu{}_\nu$, and the sum of steps 1–2 is $\omega^\mu{}_\nu$: the $\frac12$ has disappeared, as it should.
>
> **4. The Hermitian form.** $-\frac i2\omega_{\alpha\beta}\mathcal J^{\alpha\beta} = -\frac i2\cdot i\,\omega_{\alpha\beta}M^{\alpha\beta} = \frac12\omega_{\alpha\beta}M^{\alpha\beta}$, since $-i\cdot i = 1$.
>
> **5. Exponential and first order.** The exponent of Def. §C1a.6.1 is therefore the matrix $\omega = [\omega^\mu{}_\nu]$, and $\Lambda = e^\omega = \mathbb 1 + \omega + O(\omega^2)$, so $\delta v^\mu = \omega^\mu{}_\nu v^\nu$ (the coordinate law of Theorem §C1a.6.1 for $v = x$).
>
> **What the derivation shows**
> - The generators need not be guessed: they are read off by writing $\omega^\mu{}_\nu$ as $\frac12\omega_{\alpha\beta}(\cdots)^\mu{}_\nu$ (raise, antisymmetrize, insert a delta for each free index). The same recipe gives the spin generators $S^{\alpha\beta}$ of any field ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]); for the four-vector field they are these matrices ([[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|Example §C1b.1.1]]).
> - Used next: the exponentials of single generators (Theorem §C1a.6.3).

^der-c1a-6-2

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]

> [!theorem] Theorem §C1a.6.3: Rotations and Boosts as Exponentials
> 1. **Rotation about $z$**, $\omega_{12} = -\omega_{21} = \theta$: $\omega^1{}_2 = -\theta$, $\omega^2{}_1 = \theta$, and $e^{\theta M^{12}}$ acts on $(x^1, x^2)$ as $R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, the active rotation of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]; $(M^{12})^2 = -\mathbb 1$ on that block.
> 2. **Boost along $z$**, $\omega_{03} = -\omega_{30} = \eta$: $\omega^0{}_3 = \omega^3{}_0 = \eta$, and $e^{\eta M^{03}}$ acts on $(x^0, x^3)$ as $B_z(\eta) = \begin{pmatrix} \cosh\eta & \sinh\eta \\ \sinh\eta & \cosh\eta \end{pmatrix}$; $(M^{03})^2 = +\mathbb 1$ on that block.
> 3. Generally $e^{\theta M^{jk}}$, $(ijk)$ cyclic, is the active rotation by $\theta$ about $x^i$, and $e^{\eta M^{0i}}$ the active boost to rapidity $\eta$ along $+x^i$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Definition "Generators in the vector representation", sorted by index type; Caution "A mixed pair"); Ch. 7 (Derivation "What the vector generators do") · PHY 513 Lecture 7 (Examples "Rotation around z-axis", "Boost along x-axis")*

^thm-c1a-6-3

> [!derivation]- Derivation
> **1. The matrix $M^{12}$.** From Def. §C1a.6.1, $(M^{12})^\mu{}_\nu = g^{1\mu}\delta^2{}_\nu - g^{2\mu}\delta^1{}_\nu$. The only nonzero entries: $(\mu, \nu) = (1, 2)$ gives $g^{11} = -1$; $(\mu, \nu) = (2, 1)$ gives $-g^{22} = +1$. On $(x^1, x^2)$, $M^{12} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \equiv \epsilon$, zero elsewhere.
>
> **2. Its parameters.** With $\omega_{12} = -\omega_{21} = \theta$ and the rest zero, $\frac12\omega_{\alpha\beta}M^{\alpha\beta} = \frac12(\theta M^{12} + (-\theta)M^{21}) = \theta M^{12}$; raising the first index of $\omega$: $\omega^1{}_2 = g^{11}\omega_{12} = -\theta$, $\omega^2{}_1 = g^{22}\omega_{21} = +\theta$, consistent with $\theta\epsilon$ (Theorem §C1a.6.2).
>
> **3. Exponentiate.** $\epsilon^2 = -\mathbb 1_2$, so the even powers are $(-1)^n\theta^{2n}\mathbb 1_2$ and the odd ones $(-1)^n\theta^{2n+1}\epsilon$; summing the exponential series ([[§39★ Fundamental Matrices#^def-39-3|331 Def. §39.3]]) separately,
>
> $$
> e^{\theta\epsilon} = \cos\theta\,\mathbb 1_2 + \sin\theta\,\epsilon = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
> $$
>
> and $e^{\theta M^{12}}$ is the identity on $x^0$, $x^3$. Applied to $\hat{\mathbf x}$ it gives $(\cos\theta, \sin\theta)$: counterclockwise, active.
>
> **4. The matrix $M^{03}$.** $(M^{03})^\mu{}_\nu = g^{0\mu}\delta^3{}_\nu - g^{3\mu}\delta^0{}_\nu$: $(\mu, \nu) = (0, 3)$ gives $g^{00} = 1$; $(3, 0)$ gives $-g^{33} = +1$. On $(x^0, x^3)$, $M^{03} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \equiv \sigma$, symmetric, with $\sigma^2 = +\mathbb 1_2$. With $\omega_{03} = -\omega_{30} = \eta$: $\omega^0{}_3 = g^{00}\eta = \eta$, $\omega^3{}_0 = g^{33}(-\eta) = \eta$.
>
> **5. Exponentiate.** Even powers $\eta^{2n}\mathbb 1_2$, odd powers $\eta^{2n+1}\sigma$, so $e^{\eta\sigma} = \cosh\eta\,\mathbb 1_2 + \sinh\eta\,\sigma = B_z(\eta)$. On a particle at rest, $(1, 0) \mapsto (\cosh\eta, \sinh\eta)$: velocity $\tanh\eta$ along $+z$.
>
> **6. The other axes.** For $(ijk) = (1,2,3), (2,3,1), (3,1,2)$ the computation of step 1 gives $(M^{jk})^j{}_k = g^{jj} = -1$, $(M^{jk})^k{}_j = +1$: on $(x^j, x^k)$ the same $\epsilon$, a rotation carrying $x^j$ toward $x^k$, which is the right-handed rotation about $x^i$. Step 4 with $3 \to i$ gives the boost along $x^i$. ⚑ By-product: rotations exponentiate to trigonometric functions because $\epsilon^2 = -1$, boosts to hyperbolic ones because $\sigma^2 = +1$; that sign is the metric's, and it is why rotation angles are periodic and rapidities are not → [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-4|REL Remark: A rotation with a hyperbola instead of a circle]].
>
> **What the derivation shows**
> - The slide's rotation matrix (with $+\sin\theta$ upper right) is $e^{-\theta M^{12}}$, the passive rotation ([[§C1a.4 The Lorentz Group#^cau-c1a-4-3|§C1a.4, Caution: The slides' rotation matrix is passive]]); its boost is $e^{\eta M^{03}}$ as written.
> - $e^{\eta_1M^{03}}e^{\eta_2M^{03}} = e^{(\eta_1 + \eta_2)M^{03}}$ (commuting exponents): rapidities add along one axis because they are parameters of a one-parameter subgroup.
> - Used next: the rotation and boost generators $\mathbf J$, $\mathbf K$ (Def. §C1a.6.2).

^der-c1a-6-3

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§39★ Fundamental Matrices#^def-39-3|331 Def. §39.3]]

> [!caution] Caution: Which ω is a rotation by θ
> The matrices $\Lambda = e^{-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}}$ are the same in Peskin–Schroeder, the lectures and Yu; what differs is the meaning given to a parameter. Actively (these notes, PS), $\omega_{12} = \theta$ rotates the system by $+\theta$ about $z$ and $\omega_{03} = \eta$ boosts it to $+z$. Yu reads $\Lambda$ passively, so his angle and rapidity are $\theta_{\rm Yu} = -\omega_{12}$, $\xi_{\rm Yu} = -\omega_{01}$ ([[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]]). The Lecture 7 slides label the boost example $\omega_{10} = -\omega_{01} = \eta$ but display the matrix of $e^{\eta M^{01}}$, which belongs to $\omega_{01} = \eta$; with $\omega_{10} = \eta$ the boost goes the other way. Formulas written in $\omega_{\mu\nu}$ (generators, algebra, field laws) are identical everywhere; only those written in "the angle" or "the rapidity" flip.
>
> *Source: the user's PHY 513 notes, Ch. 7 (Principle "Active and passive conventions"; Caution "The index order in the boost example") · PHY 513 Lecture 7 · Yu §3.1*

^cau-c1a-6-1

> [!theorem] Theorem §C1a.6.4: Every Exponential Is Proper Orthochronous
> For every real antisymmetric $\omega_{\mu\nu}$, $\Lambda = e^{\omega} = \exp\bigl(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}\bigr)$ lies in $SO^+(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 (Derivation "Every exponential exp(ω) is a proper orthochronous Lorentz transformation") · Yu §4.1, eqs. (4.9)–(4.12), as cited there*

^thm-c1a-6-4

> [!derivation]- Derivation
> **1. Antisymmetry as a matrix identity.** $(g^{-1}\omega^{\mathsf T}g)^\alpha{}_\beta = g^{\alpha\gamma}\,\omega^\delta{}_\gamma\,g_{\delta\beta} = g^{\alpha\gamma}\omega_{\beta\gamma} = -g^{\alpha\gamma}\omega_{\gamma\beta} = -\omega^\alpha{}_\beta$, using $g_{\delta\beta}\omega^\delta{}_\gamma = \omega_{\beta\gamma}$ and antisymmetry. So $g^{-1}\omega^{\mathsf T}g = -\omega$.
>
> **2. Through the exponential.** Transposition and conjugation by $g$ act term by term on the convergent series: $(e^\omega)^{\mathsf T} = e^{\omega^{\mathsf T}}$ and $g^{-1}e^{\omega^{\mathsf T}}g = e^{g^{-1}\omega^{\mathsf T}g}$, since $(g^{-1}Ag)^n = g^{-1}A^ng$. Hence $g^{-1}\Lambda^{\mathsf T}g = e^{-\omega}$.
>
> **3. Lorentz.** $-\omega$ and $\omega$ commute, so $e^{-\omega}e^{\omega} = e^0 = \mathbb 1$: $g^{-1}\Lambda^{\mathsf T}g\Lambda = \mathbb 1$, i.e. $\Lambda^{\mathsf T}g\Lambda = g$.
>
> **4. Proper.** $\det e^{A} = e^{\operatorname{tr}A}$: $\frac{d}{dt}\det e^{tA} = \operatorname{tr}(A)\det e^{tA}$ by Jacobi's formula ([[Jacobi's Formula]], with $\frac{d}{dt}e^{tA} = Ae^{tA}$), and $\det e^{0} = 1$. Here $\operatorname{tr}\omega = \omega^\mu{}_\mu = g^{\mu\alpha}\omega_{\alpha\mu} = 0$, a symmetric tensor contracted with an antisymmetric one. So $\det\Lambda = 1$.
>
> **5. Orthochronous.** $t \mapsto e^{t\omega}$, $t \in [0, 1]$, is a continuous path from $\mathbb 1$ to $\Lambda$ through Lorentz transformations (steps 1–3 for $t\omega$), so $\Lambda$ is in the component of the identity, $SO^+(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]), where $\Lambda^0{}_0 \ge 1$.
>
> **What the derivation shows**
> - The exponential map lands exactly in the identity component; $\mathcal P$, $\mathcal T$ and $\mathcal P\mathcal T$ are never exponentials of generators, which is why discrete symmetries carry no Noether charge.
> - Combined with [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]] (every element is a boost times a rotation, each an exponential), $SO^+(1,3)$ is generated by the exponentials; that a single exponential already suffices is true but not needed in the course.
> - Used next: Theorem §C1a.6.1, step 4 (every antisymmetric $\omega$ is a tangent vector).

^der-c1a-6-4

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[Jacobi's Formula]]

> [!remark] Remark: Hermitian generators do not make boosts unitary
> The factor $i$ in $\mathcal J = iM$ makes the *rotation* generators Hermitian as acting matrices: $(\mathcal J^{jk})^\mu{}_\nu$ is $i$ times a real antisymmetric matrix. The boost generators $\mathcal J^{0i}$ are $i$ times a real *symmetric* matrix (Theorem §C1a.6.3, step 4), hence anti-Hermitian, and a finite boost is real symmetric, not orthogonal: not unitary. A Lorentz transformation preserves the Minkowski form, $\Lambda^{\mathsf T}g\Lambda = g$, not the Euclidean length. (The both-lower form $(\mathcal J^{\mu\nu})_{\alpha\beta}$ is Hermitian for all six, probably the source of the contrary statement, but it is not the matrix that acts.) This is no defect of the vector representation: a noncompact simple Lie group such as $SO^+(1,3)$ has no finite-dimensional unitary representation besides the trivial one ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-10|Theorem §C3.3.10]]; the compact rotation group, by contrast, has every finite-dimensional representation unitary in a suitable inner product, [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|Theorem §C3.1.5]]). Representations on quantum states, which must be unitary, are infinite-dimensional (Wigner's one-particle spaces, [[§C3.6★ Particle States and the Little Group#^pr-c3-6-1|Principle §C3.6.1]]); the finite-dimensional ones act on the *indices of fields* and are not unitary ([[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-5|§C3.1, Remark: Two uses of one theory: field indices and quantum states]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 (Principle "Hermitian generators do not make boosts unitary", citing Weinberg, The Quantum Theory of Fields I, ch. 2)*

^rem-c1a-6-2

## Rotations and boosts

> [!definition] Definition §C1a.6.2: Rotation and Boost Generators
>
> $$
> J_i = \tfrac12\varepsilon_{ijk}\mathcal J^{jk}, \quad\text{i.e.}\quad \mathbf J = (\mathcal J^{23}, \mathcal J^{31}, \mathcal J^{12}); \qquad K_i = \mathcal J^{0i}, \quad\text{i.e.}\quad \mathbf K = (\mathcal J^{01}, \mathcal J^{02}, \mathcal J^{03}) .
> $$
>
> With $\theta_i = \frac12\varepsilon_{ijk}\omega_{jk}$ and $\eta_i = \omega_{0i}$, $\ -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\,\boldsymbol\theta\cdot\mathbf J - i\,\boldsymbol\eta\cdot\mathbf K$, so $\Lambda = e^{-i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K}$; in particular $e^{-i\theta J_3} = e^{\theta M^{12}}$ and $e^{-i\eta K_3} = e^{\eta M^{03}}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (Principle "The Lorentz algebra in terms of rotations and boosts") · Yu §3.1, eqs. (3.37)–(3.38) · [[Larsen PHY 513]] (boost generator $K^i = J^{0i}$)*

^def-c1a-6-2

The exponent formula is the six-term sum $\sum_{\mu<\nu}\omega_{\mu\nu}\mathcal J^{\mu\nu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-1|Remark: The factor ½]]) regrouped: $\omega_{0i}\mathcal J^{0i} = \eta_iK_i$ and $\omega_{23}\mathcal J^{23} + \omega_{31}\mathcal J^{31} + \omega_{12}\mathcal J^{12} = \theta_iJ_i$ (with $\omega_{13}\mathcal J^{13} = \omega_{31}\mathcal J^{31}$). A single exponential of a sum is not the product of the separate exponentials, since $\mathbf J$ and $\mathbf K$ do not commute. Some sources define $K^i = \mathcal J^{i0}$, the opposite sign, as does the Noether boost charge $K^i \equiv J^{i0}$ of [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-8-1|Def. §C1b.8.1]] ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^cau-c1b-8-1|§C1b.8, Caution: Notation in Yu and in the conventions table]]); the algebra ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]) is unchanged, finite boosts reverse.

Their algebra, $[J_i, J_j] = i\varepsilon_{ijk}J_k$, $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$ and the covariant relation for $\mathcal J^{\mu\nu}$, is [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]], with its three derivations (from the group law, by direct computation in the vector representation as in PHY 513 Problem Set 4, Problem 5(a), and in the $\mathbf J$, $\mathbf K$ form as in Problem Set 5, Problem 1(a)).

> [!remark] Remark: Why generators
> Field theory works with generators rather than group elements for three reasons. Noether charges are generators represented on the fields: the six conserved charges of a Lorentz-invariant theory are the angular momentum $\mathbf J$ and the boost charge $\mathbf K$ (Def. §C1b.8.1, whose $K^i \equiv J^{i0}$ carries the opposite index order to the generator $K_i = \mathcal J^{0i}$ of Def. §C1a.6.2). A field with indices is specified by six matrices $S^{\mu\nu}$ obeying the algebra, which is how spinors are defined ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]; [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]). And the split into $\mathbf J_\pm$ reduces the representation theory of the Lorentz group to that of angular momentum ([[§C3.2 The Lorentz Algebra#^thm-c3-2-3|Theorem §C3.2.3]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-6|Theorem §C3.1.6]]). Should one start from rotation-and-boost invariance or from the metric condition? From the metric condition $\Lambda^{\mathsf T}g\Lambda = g$: the generators and their algebra follow from it, as here.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.6 (paragraphs "Why generators", "Discussion")*

^rem-c1a-6-3

## The generators and the finite matrices, entry by entry

Definitions §C1a.6.1–§C1a.6.2 give the generators as index formulas and Theorem §C1a.6.3 exponentiates two of them on a $2\times2$ block. Here all six are written as $4\times4$ matrices, and the finite rotations and boosts are written in full, about and along an arbitrary direction. Rows are labelled by $\mu$, columns by $\nu = 0, 1, 2, 3$: these are the matrices $\Lambda^\mu{}_\nu$ (and generators) that multiply a column $v^\nu$. $E_{\mu\nu}$ denotes the matrix with $1$ in row $\mu$, column $\nu$ and $0$ elsewhere, so that $E_{\mu\nu}E_{\rho\sigma} = \delta_{\nu\rho}E_{\mu\sigma}$.

> [!theorem] Theorem §C1a.6.5: The Rotation and Boost Generators as 4×4 Matrices
> In the vector representation ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) the rotation and boost generators $J_k = \frac12\varepsilon_{kij}\mathcal J^{ij}$, $K_k = \mathcal J^{0k}$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] are
>
> $$
> J_1 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&0\\ 0&0&0&-i\\ 0&0&i&0 \end{pmatrix}, \qquad J_2 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&i\\ 0&0&0&0\\ 0&-i&0&0 \end{pmatrix}, \qquad J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&-i&0\\ 0&i&0&0\\ 0&0&0&0 \end{pmatrix},
> $$
>
> $$
> K_1 = \begin{pmatrix} 0&i&0&0\\ i&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix}, \qquad K_2 = \begin{pmatrix} 0&0&i&0\\ 0&0&0&0\\ i&0&0&0\\ 0&0&0&0 \end{pmatrix}, \qquad K_3 = \begin{pmatrix} 0&0&0&i\\ 0&0&0&0\\ 0&0&0&0\\ i&0&0&0 \end{pmatrix},
> $$
>
> i.e. $(J_k)^l{}_m = -i\varepsilon_{klm}$ with zero time row and column, and $(K_k)^0{}_m = (K_k)^m{}_0 = i\delta_{km}$, all other entries $0$. Each $J_k$ is $i$ times a real antisymmetric matrix: Hermitian, eigenvalues $1, -1, 0, 0$ ($J_3$: on $e_1 \pm ie_2$, and $e_0$, $e_3$). Each $K_k$ is $i$ times a real symmetric matrix: anti-Hermitian, eigenvalues $i, -i, 0, 0$ ($K_3$: on $e_0 \pm e_3$, and $e_1$, $e_2$). The real matrices in the exponent of $\Lambda$ are $-iJ_k$ and $-iK_k$, e.g. $-iJ_3 = M^{12} = E_{21} - E_{12}$ and $-iK_3 = M^{03} = E_{03} + E_{30}$.
>
> *Source: PS §3.1, eq. (3.18) (the both-lower form) and eqs. (3.20)–(3.21) (the infinitesimal rotation about $z$ and boost along $x$ as $4\times4$ matrices) · PHY 513 Lecture 7 (Examples "Rotation around z-axis", "Boost along x-axis") · the user's PHY 513 notes, Ch. 1 §1.6 (Definition "Generators in the vector representation"), Ch. 7 §7.3 (Derivation "What the vector generators do") · the six matrices and their spectra written out here · PHY 513, Problem Set 6, Problem 4(a), (c) (the generator $(\mathcal J^{\mu\nu})^\alpha{}_\beta = i(g^{\mu\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\mu{}_\beta)$ and the exponents $-i\eta\mathcal J^{03}$, $-i\theta\mathcal J^{12}$, as the user wrote them)*

^thm-c1a-6-5

> [!derivation]- Derivation
> **1. Which $\mathcal J$ is which.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], $J_1 = \frac12(\varepsilon_{123}\mathcal J^{23} + \varepsilon_{132}\mathcal J^{32}) = \frac12(\mathcal J^{23} - \mathcal J^{32}) = \mathcal J^{23}$, using $\mathcal J^{32} = -\mathcal J^{23}$; in the same way $J_2 = \mathcal J^{31}$, $J_3 = \mathcal J^{12}$. And $K_k = \mathcal J^{0k}$.
>
> **2. Entries of a rotation generator.** From [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], $(\mathcal J^{jk})^\mu{}_\nu = i(g^{j\mu}\delta^k{}_\nu - g^{k\mu}\delta^j{}_\nu)$. Since $g^{j\mu} = -\delta^{j\mu}$ for spatial $j$, the first term is nonzero only at $(\mu, \nu) = (j, k)$, where it is $ig^{jj} = -i$, and the second only at $(\mu, \nu) = (k, j)$, where it is $-ig^{kk} = +i$. So $\mathcal J^{jk} = -iE_{jk} + iE_{kj}$:
>
> $$
> J_3 = \mathcal J^{12} = -iE_{12} + iE_{21}, \qquad J_1 = \mathcal J^{23} = -iE_{23} + iE_{32}, \qquad J_2 = \mathcal J^{31} = -iE_{31} + iE_{13} ,
> $$
>
> which are the three displayed matrices. On the spatial block this is $(J_k)^l{}_m = -i\varepsilon_{klm}$: e.g. $(J_3)^1{}_2 = -i\varepsilon_{312} = -i$, $(J_2)^1{}_3 = -i\varepsilon_{213} = +i$. The time row and column vanish because $g^{j0} = 0$ and $\delta^k{}_0 = 0$.
>
> **3. Entries of a boost generator.** $(\mathcal J^{0k})^\mu{}_\nu = i(g^{0\mu}\delta^k{}_\nu - g^{k\mu}\delta^0{}_\nu)$: the first term is nonzero only at $(0, k)$, where it is $ig^{00} = i$; the second only at $(k, 0)$, where it is $-ig^{kk} = +i$. So $K_k = i(E_{0k} + E_{k0})$ (for $k = 3$ this is $i$ times the matrix $M^{03}$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], step 4).
>
> **4. Hermiticity.** For a real matrix $A$, $(iA)^\dagger = -iA^{\mathsf T}$. If $A$ is antisymmetric this is $iA$ (Hermitian: the $J_k$, step 2); if $A$ is symmetric it is $-iA$ (anti-Hermitian: the $K_k$, step 3).
>
> **5. Eigenvectors of $J_3$ and $K_3$.** $J_3e_1 = ie_2$ and $J_3e_2 = -ie_1$ (the columns $1$ and $2$ of $J_3$), so $J_3(e_1 \pm ie_2) = ie_2 \pm i(-i)e_1 = \pm(e_1 \pm ie_2)$; $J_3e_0 = J_3e_3 = 0$. $K_3e_0 = ie_3$ and $K_3e_3 = ie_0$, so $K_3(e_0 \pm e_3) = i(e_3 \pm e_0) = \pm i(e_0 \pm e_3)$; $K_3e_1 = K_3e_2 = 0$. For $k = 1, 2$ relabel the axes.
>
> **6. The real exponents.** $\mathcal J = iM$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]) gives $M^{\alpha\beta} = -i\mathcal J^{\alpha\beta}$: $-iJ_3 = -i(-iE_{12} + iE_{21}) = -E_{12} + E_{21} = M^{12}$ and $-iK_3 = -i\cdot i(E_{03} + E_{30}) = E_{03} + E_{30} = M^{03}$, the matrices $\epsilon$ and $\sigma$ of Theorem §C1a.6.3 on their $2\times2$ blocks.
>
> **What the derivation shows**
> - A rotation generator never touches $e_0$ and a boost generator $K_k$ touches only $e_0$ and $e_k$: the $2\times2$ blocks of Theorem §C1a.6.3 are the whole story, padded with zeros. On the spatial block the $J_k$ are the spin-1 matrices ([[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]]).
> - The eigenvalues are the numbers that multiply $\theta$ and $\eta$ in the exponent: $\pm1$ for a rotation gives the phases $e^{\mp i\theta}$, $\pm i$ for a boost gives $e^{\pm\eta}$; the spinor generators have half of each ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]; side by side: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]]).
> - These matrices obey the algebra of [[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]; $[J_1, J_2] = iJ_3$ and $[K_1, K_2] = -iJ_3$ are multiplied out entry by entry, next to their spinor counterparts, in Examples §C5a.4.1 and §C5a.4.2.
> - Used next: their exponentials (Theorems §C1a.6.6–§C1a.6.7).

^der-c1a-6-5

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]

> [!theorem] Theorem §C1a.6.6: The Rotation Matrices in the Vector Representation
> With the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], read actively as in [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]] (a positive angle turns the object counterclockwise as seen from the tip of the axis, the convention of [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^def-c5-1-1|QM Def. §C5.1.1]]):
> 1. **Rotation about $z$** by $\theta$ ($\omega_{12} = -\omega_{21} = \theta$):
>
> $$
> R_z(\theta) = e^{-i\theta J_3} = \begin{pmatrix} 1&0&0&0\\ 0&\cos\theta&-\sin\theta&0\\ 0&\sin\theta&\cos\theta&0\\ 0&0&0&1 \end{pmatrix} .
> $$
>
> 2. **Rotation about a unit vector** $\hat{\mathbf n}$ by $\theta$ ($\omega_{ij} = \varepsilon_{ijk}\theta n^k$, $\omega_{0i} = 0$), in (time, space) blocks:
>
> $$
> R_{\hat{\mathbf n}}(\theta) = e^{-i\theta\,\hat{\mathbf n}\cdot\mathbf J} = \begin{pmatrix} 1 & 0 \\ 0 & R(\theta, \hat{\mathbf n}) \end{pmatrix}, \qquad R(\theta, \hat{\mathbf n}) = \cos\theta\,\mathbb 1_3 + (1 - \cos\theta)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} + \sin\theta\,[\hat{\mathbf n}]_\times, \qquad [\hat{\mathbf n}]_\times = \begin{pmatrix} 0 & -n^3 & n^2 \\ n^3 & 0 & -n^1 \\ -n^2 & n^1 & 0 \end{pmatrix},
> $$
>
> i.e. $R^i{}_j = \cos\theta\,\delta^i{}_j + (1 - \cos\theta)\,n^in^j - \sin\theta\,\varepsilon_{ijk}n^k$, where $[\hat{\mathbf n}]_\times\mathbf v = \hat{\mathbf n}\times\mathbf v$ (Rodrigues' rotation formula). $R(\theta, \hat{\mathbf n})$ is orthogonal with $\det R = 1$, fixes the axis, $R\hat{\mathbf n} = \hat{\mathbf n}$, and $R_{\hat{\mathbf n}}(2\pi) = \mathbb 1$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2, eq. (rotboost) and Caution "A mixed pair: the rotation matrix above is passive" (the rotation about $z$ as a $4\times4$ matrix), Ch. 7 §7.3 (Derivation "What the vector generators do": the finite rotation about $z$), Ch. 8 §8.1 (Derivation "From six numbers to two matrices": the angles in $\omega^\mu{}_\nu$) · PHY 513 Lecture 1, Part B ($\Lambda_{\rm rotation}$, passive); Lecture 7 (Example "Rotation around z-axis") · PS §3.1, eq. (3.20) · Yu §1.3, eq. (1.36), and Exercise 1.5, eq. (1.267) (passive rotations about $z$, $x$, $y$) · Sakurai §3.1.1, eqs. (3.1)–(3.5), as in QM §C5.1 (rotations about the axes) · the rotation about $\hat{\mathbf n}$ and its derivation from the generators written here (checked numerically) · PHY 513, Problem Set 6, Problem 4(c)–(d) (the rotation about $z$ as a $4\times4$ matrix and its value $\mathbb 1$ at $2\pi$, as the user wrote it; same signs)*

^thm-c1a-6-6

> [!derivation]- Derivation
> Write $P = \hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}$ (projector onto the axis), $Q = \mathbb 1_3 - P$ (projector onto the plane perpendicular to it), $A = [\hat{\mathbf n}]_\times$, and $E_{\mu\nu}$ for the matrix units.
>
> **1. The exponent.** By [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]] with $\theta_k = \frac12\varepsilon_{kij}\omega_{ij} = \frac12\varepsilon_{kij}\varepsilon_{ijl}\theta n^l = \theta n^k$ (using $\varepsilon_{kij}\varepsilon_{lij} = 2\delta_{kl}$, [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and $\boldsymbol\eta = 0$, $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\theta\,\hat{\mathbf n}\cdot\mathbf J$. For $\hat{\mathbf n} = \hat{\mathbf z}$ the only nonzero parameters are $\omega_{12} = -\omega_{21} = \theta$, and the exponent is $-i\theta J_3$.
>
> **2. The generator is the cross product.** By Theorem §C1a.6.5, $-iJ_k$ has zero time row and column and spatial entries $(-iJ_k)^l{}_m = -i(-i\varepsilon_{klm}) = -\varepsilon_{klm}$. So $-i\,\hat{\mathbf n}\cdot\mathbf J = \operatorname{diag}(0, A)$ with $A_{lm} = -n^k\varepsilon_{klm} = -\varepsilon_{lmk}n^k$ (cyclic order): $A_{12} = -n^3$, $A_{13} = +n^2$, $A_{23} = -n^1$, and $A_{ml} = -A_{lm}$, the displayed matrix. On a vector, $(A\mathbf v)_l = -\varepsilon_{lmk}v^mn^k = \varepsilon_{lkm}n^kv^m = (\hat{\mathbf n}\times\mathbf v)_l$.
>
> **3. Powers of A.** $A^2\mathbf v = \hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf v) = \hat{\mathbf n}(\hat{\mathbf n}\cdot\mathbf v) - \mathbf v(\hat{\mathbf n}\cdot\hat{\mathbf n}) = (P - \mathbb 1_3)\mathbf v$, so $A^2 = -Q$. Since $A\hat{\mathbf n} = \hat{\mathbf n}\times\hat{\mathbf n} = 0$, $AP = 0$, hence $AQ = A$ and $A^3 = -AQ = -A$. By induction $A^{2k} = (-1)^kQ$ ($k \ge 1$) and $A^{2k+1} = (-1)^kA$.
>
> **4. Sum the series (part 2).** Splitting $e^{\theta A}$ into the $n = 0$ term, the even terms $n = 2k \ge 2$ and the odd terms,
>
> $$
> e^{\theta A} = \mathbb 1_3 + \Bigl(\sum_{k\ge1}\frac{(-1)^k\theta^{2k}}{(2k)!}\Bigr)Q + \Bigl(\sum_{k\ge0}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}\Bigr)A = \mathbb 1_3 + (\cos\theta - 1)\,Q + \sin\theta\,A = P + \cos\theta\,Q + \sin\theta\,A ,
> $$
>
> using $\mathbb 1_3 - Q = P$; with $Q = \mathbb 1_3 - P$ this is $\cos\theta\,\mathbb 1_3 + (1 - \cos\theta)P + \sin\theta\,A$. The exponent $\theta\operatorname{diag}(0, A)$ has zero time row and column, so every power of it does too (beyond the zeroth), and $e^{-i\theta\hat{\mathbf n}\cdot\mathbf J} = \operatorname{diag}(1, e^{\theta A})$. Components: $P^{ij} = n^in^j$ and $A_{ij} = -\varepsilon_{ijk}n^k$ (step 2).
>
> **5. About z (part 1).** For $\hat{\mathbf n} = \hat{\mathbf z}$: $P = \operatorname{diag}(0, 0, 1)$ and $A = E_{21} - E_{12}$ (spatial labels), so $R = \operatorname{diag}(0, 0, 1) + \cos\theta\operatorname{diag}(1, 1, 0) + \sin\theta(E_{21} - E_{12})$, with entries $(1,1) = (2,2) = \cos\theta$, $(1,2) = -\sin\theta$, $(2,1) = \sin\theta$, $(3,3) = 1$: the active $R_z(\theta)$ of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]] and of [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^def-c5-1-1|QM Def. §C5.1.1]], now as a $4\times4$ matrix; its $2\times2$ block is [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 1.
>
> **6. The sense of rotation.** For $\mathbf v \perp \hat{\mathbf n}$ ($P\mathbf v = 0$, $Q\mathbf v = \mathbf v$), $R\mathbf v = \cos\theta\,\mathbf v + \sin\theta\,\hat{\mathbf n}\times\mathbf v$: $\mathbf v$ turns toward $\hat{\mathbf n}\times\mathbf v$, counterclockwise as seen from the tip of $\hat{\mathbf n}$ (for $\hat{\mathbf n} = \hat{\mathbf z}$, $\hat{\mathbf x} \mapsto \cos\theta\,\hat{\mathbf x} + \sin\theta\,\hat{\mathbf y}$). The object is turned (active); the passive matrix is $R(-\theta, \hat{\mathbf n}) = R(\theta, \hat{\mathbf n})^{\mathsf T}$ ([[§C1a.4 The Lorentz Group#^cau-c1a-4-3|§C1a.4, Caution: The slides' rotation matrix is passive]]).
>
> **7. Checks.** $R\hat{\mathbf n} = P\hat{\mathbf n} + \cos\theta\,Q\hat{\mathbf n} + \sin\theta\,A\hat{\mathbf n} = \hat{\mathbf n} + 0 + 0$. Orthogonality: $P$, $Q$ are symmetric and $A$ antisymmetric, so $R^{\mathsf T} = P + cQ - sA$ ($c = \cos\theta$, $s = \sin\theta$); with $P^2 = P$, $Q^2 = Q$, $PQ = QP = 0$, $PA = AP = 0$ (as $\hat{\mathbf n}^{\mathsf T}A = -(A\hat{\mathbf n})^{\mathsf T} = 0$), $QA = AQ = A$ and $A^2 = -Q$, the nine terms of $R^{\mathsf T}R$ are
>
> $$
> (P + cQ - sA)(P + cQ + sA) = P + 0 + 0 + 0 + c^2Q + cs\,A + 0 - cs\,A - s^2A^2 = P + (c^2 + s^2)\,Q = P + Q = \mathbb 1_3 .
> $$
>
> $\det R = \det e^{\theta A} = e^{\theta\operatorname{tr}A} = e^0 = 1$ ($A$ has zero diagonal; $\det e^X = e^{\operatorname{tr}X}$ as in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]], step 4). At $\theta = 2\pi$: $c = 1$, $s = 0$, $R = P + Q = \mathbb 1_3$; equivalently, the eigenvalues $\pm1, 0, 0$ of $\hat{\mathbf n}\cdot\mathbf J$ (those of $J_3$ in Theorem §C1a.6.5, carried to the axis $\hat{\mathbf n}$ by a rotation) give $e^{\mp2\pi i} = 1$ and $e^0 = 1$.
>
> **What the derivation shows**
> - A rotation leaves the time axis and the rotation axis alone and turns the perpendicular plane: $P + \cos\theta\,Q + \sin\theta\,[\hat{\mathbf n}]_\times$ is "identity on the axis, two-dimensional rotation on the plane". $[\hat{\mathbf n}]_\times^2 = -Q$ is why the series gives $\cos$ and $\sin$; the boost generator squares to $+$(a projector) and gives $\cosh$ and $\sinh$ (Theorem §C1a.6.7).
> - [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^ex-c5-1-2|QM Example §C5.1.2]] states $\exp(\phi A_{\hat n}) = R(\hat n, \phi)$ for the same $3\times3$ generators; this is the explicit matrix. Inside the Lorentz group these are the matrices $\operatorname{diag}(1, R)$ of [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]], 1.
> - Used next: a rotation carries the boost along $z$ to the boost along $\hat{\mathbf n}$ (Theorem §C1a.6.7); the spinor matrices of the same rotations ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]]).

^der-c1a-6-6

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^der-c1a-6-4|Derivation §C1a.6.4]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C1a.4 The Lorentz Group#^cau-c1a-4-3|§C1a.4, Caution: The slides' rotation matrix is passive]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^def-c5-1-1|QM Def. §C5.1.1]]

> [!theorem] Theorem §C1a.6.7: The Boost Matrices in the Vector Representation
> With the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], the rapidity $\eta$ of [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]] ($\gamma = \cosh\eta$, $\gamma v = \sinh\eta$) and the active reading of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]:
> 1. **Boost along $z$** ($\omega_{03} = -\omega_{30} = \eta$):
>
> $$
> \Lambda_z(\eta) = e^{-i\eta K_3} = \begin{pmatrix} \cosh\eta&0&0&\sinh\eta\\ 0&1&0&0\\ 0&0&1&0\\ \sinh\eta&0&0&\cosh\eta \end{pmatrix} = \begin{pmatrix} \gamma&0&0&\gamma v\\ 0&1&0&0\\ 0&0&1&0\\ \gamma v&0&0&\gamma \end{pmatrix} .
> $$
>
> 2. **Boost along a unit vector** $\hat{\mathbf n}$ ($\omega_{0i} = -\omega_{i0} = \eta\,n^i$, $\omega_{ij} = 0$), in (time, space) blocks and in components:
>
> $$
> \Lambda_{\hat{\mathbf n}}(\eta) = e^{-i\eta\,\hat{\mathbf n}\cdot\mathbf K} = \begin{pmatrix} \cosh\eta & \sinh\eta\,\hat{\mathbf n}^{\mathsf T} \\ \sinh\eta\,\hat{\mathbf n} & \mathbb 1_3 + (\cosh\eta - 1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix} = \begin{pmatrix} \gamma & \gamma v\,\hat{\mathbf n}^{\mathsf T} \\ \gamma v\,\hat{\mathbf n} & \mathbb 1_3 + (\gamma - 1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix}, \qquad \Lambda^0{}_0 = \gamma,\quad \Lambda^0{}_i = \Lambda^i{}_0 = \gamma v\,n^i,\quad \Lambda^i{}_j = \delta^i{}_j + (\gamma - 1)\,n^in^j .
> $$
>
> It is symmetric, satisfies $\Lambda^{\mathsf T}g\Lambda = g$, sends $(1, \mathbf 0)$ to $(\cosh\eta, \sinh\eta\,\hat{\mathbf n})$ (velocity $+v\hat{\mathbf n}$), and is the boost $B(u)$ of [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]] with $\mathbf u = \sinh\eta\,\hat{\mathbf n}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2, eq. (rotboost) (the boost along $z$ as a $4\times4$ matrix, in $\gamma$ and in $\eta$), Ch. 7 §7.3 (Derivation "What the vector generators do": the finite boost along $x$ as a $4\times4$ matrix), Ch. 8 §8.1 (Derivation "From six numbers to two matrices": the rapidities in $\omega^\mu{}_\nu$) · PHY 513 Lecture 1, Part B ($\Lambda_{\rm boost}$ along $z$); Lecture 7 (Example "Boost Along x-axis", finite action); Lecture 9, Part A ("Standard Lorentz boost acting on a 4-vector") · PS §3.3, eq. (3.48) · Yu §1.3, eqs. (1.30)–(1.32), and Exercise 1.5, eq. (1.268) (passive boosts along $x$ and $z$) · the boost along $\hat{\mathbf n}$ in rapidity form, its derivation by a rotation and the series derivations written here (all matrices checked numerically) · PHY 513, Problem Set 6, Problem 4(a) (the boost along $z$ with $\omega_{03} = -\omega_{30} = \eta$ as a $4\times4$ matrix, as the user wrote it; same signs)*

^thm-c1a-6-7

> [!derivation]- Derivation
> Write $c = \cosh\eta$, $s = \sinh\eta$, and $E_{\mu\nu}$ for the matrix units ($E_{\mu\nu}E_{\rho\sigma} = \delta_{\nu\rho}E_{\mu\sigma}$).
>
> **1. The exponent of the boost along $z$.** With $\omega_{03} = -\omega_{30} = \eta$ and all other $\omega_{\mu\nu} = 0$, the two nonzero terms of $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ are equal: $-\frac i2(\eta\mathcal J^{03} + (-\eta)\mathcal J^{30}) = -i\eta\mathcal J^{03} = -i\eta K_3$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]; $\mathcal J^{30} = -\mathcal J^{03}$). By Theorem §C1a.6.5, $-iK_3 = N \equiv E_{03} + E_{30}$, so the exponent is $\eta N$.
>
> **2. Powers of $N$.** Expanding into all four products,
>
> $$
> N^2 = E_{03}E_{03} + E_{03}E_{30} + E_{30}E_{03} + E_{30}E_{30} = 0 + E_{00} + E_{33} + 0 = P_{tz} \equiv \operatorname{diag}(1, 0, 0, 1),
> $$
>
> the projector onto the $(t, z)$ plane; $N^3 = NP_{tz} = (E_{03} + E_{30})(E_{00} + E_{33}) = E_{03} + E_{30} = N$. By induction $N^{2k} = P_{tz}$ for $k \ge 1$ and $N^{2k+1} = N$.
>
> **3. Sum the series (part 1).** Split $e^{\eta N} = \sum_n\eta^nN^n/n!$ into the $n = 0$ term $\mathbb 1$, the even terms $n = 2k \ge 2$ and the odd terms:
>
> $$
> e^{\eta N} = \mathbb 1 + \Bigl(\sum_{k\ge1}\frac{\eta^{2k}}{(2k)!}\Bigr)P_{tz} + \Bigl(\sum_{k\ge0}\frac{\eta^{2k+1}}{(2k+1)!}\Bigr)N = \mathbb 1 + (c - 1)\,P_{tz} + s\,N .
> $$
>
> The $-1$ appears because the $n = 0$ term is $\mathbb 1$, not $P_{tz}$. Entries: $(0,0)$ and $(3,3)$: $1 + c - 1 = c$; $(1,1)$ and $(2,2)$: $1$; $(0,3)$ and $(3,0)$: $s$; all others $0$. With $c = \gamma$, $s = \gamma v$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]]) this is part 1; its first column $(c, 0, 0, s)$ is the image of a particle at rest, moving with velocity $s/c = v$ along $+z$, the active convention of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]].
>
> **4. A rotation taking $\hat{\mathbf z}$ to $\hat{\mathbf n}$.** Choose a unit vector $\hat{\mathbf e}_1 \perp \hat{\mathbf n}$, put $\hat{\mathbf e}_2 = \hat{\mathbf n}\times\hat{\mathbf e}_1$, and let $R$ have the columns $\hat{\mathbf e}_1, \hat{\mathbf e}_2, \hat{\mathbf n}$. The columns are orthonormal, so $R^{\mathsf T}R = \mathbb 1_3$; $\det R = \hat{\mathbf e}_1\cdot(\hat{\mathbf e}_2\times\hat{\mathbf n}) = \hat{\mathbf e}_1\cdot\hat{\mathbf e}_1 = 1$, since $(\hat{\mathbf n}\times\hat{\mathbf e}_1)\times\hat{\mathbf n} = \hat{\mathbf e}_1(\hat{\mathbf n}\cdot\hat{\mathbf n}) - \hat{\mathbf n}(\hat{\mathbf e}_1\cdot\hat{\mathbf n}) = \hat{\mathbf e}_1$. So $R \in SO(3)$ and $R\hat{\mathbf z}$, the third column, is $\hat{\mathbf n}$ ($R$ is a rotation $R(\theta, \hat{\mathbf a})$ of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]] about some axis, but only $R\hat{\mathbf z} = \hat{\mathbf n}$ is used). Then $\tilde R = \operatorname{diag}(1, R) \in SO^+(1,3)$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]], 1), with $\tilde R^{-1} = \tilde R^{\mathsf T}$.
>
> **5. The rotated generator.** In (time, space) blocks, $N = \begin{pmatrix} 0 & \hat{\mathbf z}^{\mathsf T} \\ \hat{\mathbf z} & 0 \end{pmatrix}$. Block multiplication gives
>
> $$
> \tilde RN\tilde R^{\mathsf T} = \begin{pmatrix} 1 & 0 \\ 0 & R \end{pmatrix}\begin{pmatrix} 0 & \hat{\mathbf z}^{\mathsf T} \\ \hat{\mathbf z} & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & R^{\mathsf T} \end{pmatrix} = \begin{pmatrix} 0 & \hat{\mathbf z}^{\mathsf T}R^{\mathsf T} \\ R\hat{\mathbf z} & 0 \end{pmatrix} = \begin{pmatrix} 0 & \hat{\mathbf n}^{\mathsf T} \\ \hat{\mathbf n} & 0 \end{pmatrix},
> $$
>
> using $\hat{\mathbf z}^{\mathsf T}R^{\mathsf T} = (R\hat{\mathbf z})^{\mathsf T}$. By Theorem §C1a.6.5, $-iK_i = E_{0i} + E_{i0}$, so the last matrix is $n^i(-iK_i) = -i\,\hat{\mathbf n}\cdot\mathbf K$. Hence $\tilde R(\eta N)\tilde R^{\mathsf T} = -i\eta\,\hat{\mathbf n}\cdot\mathbf K$, which is $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ for $\eta_i = \omega_{0i} = \eta n^i$, $\boldsymbol\theta = 0$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]): the boost along $\hat{\mathbf n}$.
>
> **6. Conjugating the exponential.** $(\tilde RX\tilde R^{-1})^k = \tilde RX^k\tilde R^{-1}$ (the inner factors $\tilde R^{-1}\tilde R$ cancel), so summing term by term $e^{\tilde RX\tilde R^{-1}} = \tilde Re^X\tilde R^{-1}$. With $X = \eta N$ and step 5: $\Lambda_{\hat{\mathbf n}}(\eta) = e^{-i\eta\,\hat{\mathbf n}\cdot\mathbf K} = \tilde R\,\Lambda_z(\eta)\,\tilde R^{\mathsf T}$.
>
> **7. Block multiplication (part 2).** By step 3, in blocks $\Lambda_z(\eta) = \begin{pmatrix} c & s\,\hat{\mathbf z}^{\mathsf T} \\ s\,\hat{\mathbf z} & \mathbb 1_3 + (c - 1)\hat{\mathbf z}\hat{\mathbf z}^{\mathsf T} \end{pmatrix}$, with $\hat{\mathbf z}\hat{\mathbf z}^{\mathsf T} = \operatorname{diag}(0, 0, 1)$. Then
>
> $$
> \tilde R\Lambda_z\tilde R^{\mathsf T} = \begin{pmatrix} c & s\,\hat{\mathbf z}^{\mathsf T}R^{\mathsf T} \\ s\,R\hat{\mathbf z} & R\bigl(\mathbb 1_3 + (c - 1)\hat{\mathbf z}\hat{\mathbf z}^{\mathsf T}\bigr)R^{\mathsf T} \end{pmatrix} = \begin{pmatrix} c & s\,\hat{\mathbf n}^{\mathsf T} \\ s\,\hat{\mathbf n} & RR^{\mathsf T} + (c - 1)(R\hat{\mathbf z})(R\hat{\mathbf z})^{\mathsf T} \end{pmatrix} = \begin{pmatrix} c & s\,\hat{\mathbf n}^{\mathsf T} \\ s\,\hat{\mathbf n} & \mathbb 1_3 + (c - 1)\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix},
> $$
>
> using $RR^{\mathsf T} = \mathbb 1_3$ (a square matrix with $R^{\mathsf T}R = \mathbb 1_3$) and $R\hat{\mathbf z}\hat{\mathbf z}^{\mathsf T}R^{\mathsf T} = (R\hat{\mathbf z})(R\hat{\mathbf z})^{\mathsf T}$. In components $(\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T})^{ij} = n^in^j$, which gives the component form. The result contains $R$ only through $R\hat{\mathbf z} = \hat{\mathbf n}$, so the choice of $\hat{\mathbf e}_1$ in step 4 does not matter.
>
> **8. Direct check of $\Lambda^{\mathsf T}g\Lambda = g$.** Write $\Lambda = \Lambda_{\hat{\mathbf n}}(\eta)$, $P = \hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}$, $S = \mathbb 1_3 + (c - 1)P$. Since $\hat{\mathbf n}^{\mathsf T}\hat{\mathbf n} = 1$: $P^2 = \hat{\mathbf n}(\hat{\mathbf n}^{\mathsf T}\hat{\mathbf n})\hat{\mathbf n}^{\mathsf T} = P$, $P\hat{\mathbf n} = \hat{\mathbf n}$, $\hat{\mathbf n}^{\mathsf T}P = \hat{\mathbf n}^{\mathsf T}$, hence $S\hat{\mathbf n} = c\,\hat{\mathbf n}$, $\hat{\mathbf n}^{\mathsf T}S = c\,\hat{\mathbf n}^{\mathsf T}$ and $S^2 = \mathbb 1_3 + 2(c - 1)P + (c - 1)^2P = \mathbb 1_3 + (c^2 - 1)P = \mathbb 1_3 + s^2P$. $S$ is symmetric and the off-diagonal blocks are transposes of each other, so $\Lambda^{\mathsf T} = \Lambda$. With $g = \operatorname{diag}(1, -\mathbb 1_3)$, $g\Lambda = \begin{pmatrix} c & s\,\hat{\mathbf n}^{\mathsf T} \\ -s\,\hat{\mathbf n} & -S \end{pmatrix}$, and
>
> $$
> \Lambda^{\mathsf T}g\Lambda = \begin{pmatrix} c\cdot c + s\,\hat{\mathbf n}^{\mathsf T}(-s\,\hat{\mathbf n}) & c\,s\,\hat{\mathbf n}^{\mathsf T} + s\,\hat{\mathbf n}^{\mathsf T}(-S) \\ s\,\hat{\mathbf n}\,c + S(-s\,\hat{\mathbf n}) & s^2\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} - S^2 \end{pmatrix} = \begin{pmatrix} c^2 - s^2 & cs\,\hat{\mathbf n}^{\mathsf T} - cs\,\hat{\mathbf n}^{\mathsf T} \\ cs\,\hat{\mathbf n} - cs\,\hat{\mathbf n} & s^2P - \mathbb 1_3 - s^2P \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -\mathbb 1_3 \end{pmatrix} = g .
> $$
>
> Also $\Lambda^0{}_0 = c \ge 1$ and $\det\Lambda = \det\tilde R\,\det\Lambda_z\,\det\tilde R^{\mathsf T} = \det\Lambda_z = c^2 - s^2 = 1$ (step 6; the $(t, z)$ block times $\mathbb 1$): $\Lambda \in SO^+(1,3)$, as [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]] guarantees for every exponential.
>
> **9. Rest frame, velocity form, B(u).** The first column of $\Lambda$ is $\Lambda(1, \mathbf 0) = (c, s\,\hat{\mathbf n})$: a particle at rest is sent to velocity $(s/c)\hat{\mathbf n} = v\hat{\mathbf n}$. Substituting $c = \gamma$, $s = \gamma v$, $c - 1 = \gamma - 1$ gives the velocity form. With $\mathbf u = s\,\hat{\mathbf n}$ and $\gamma = c$, the spatial block of $B(u)$ in [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]] is $\mathbb 1_3 + \mathbf u\mathbf u^{\mathsf T}/(1 + \gamma) = \mathbb 1_3 + \frac{s^2}{1 + c}P = \mathbb 1_3 + \frac{c^2 - 1}{1 + c}P = \mathbb 1_3 + (c - 1)P$, and its other blocks are $\gamma = c$ and $\mathbf u = s\,\hat{\mathbf n}$: the same matrix.
>
> **10. Dictionary to Relativity level B.** [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]] is passive with $x^0 = ct$: $B^0{}_0 = \gamma$, $B^0{}_i = B^i{}_0 = -\gamma\beta^i$, $B^i{}_j = \delta^i{}_j + (\gamma - 1)\beta^i\beta^j/\beta^2$. With $c = 1$ and $\boldsymbol\beta \to -v\hat{\mathbf n}$ ([[§C1a.4 The Lorentz Group#^cau-c1a-4-2|§C1a.4, Caution: Notation against Relativity level B]]), $-\gamma\beta^i = \gamma v\,n^i$ and $\beta^i\beta^j/\beta^2 = n^in^j$: $\Lambda_{\hat{\mathbf n}}(\eta) = B_{\rm REL}(-v\hat{\mathbf n}) = B_{\rm REL}(v\hat{\mathbf n})^{-1}$.
>
> **What the derivation shows**
> - A boost acts only in the plane spanned by $e_0$ and $(0, \hat{\mathbf n})$: the pattern "$\mathbb 1 + (\cosh\eta - 1)\times$projector $+ \sinh\eta\times$generator" is the identity off that plane and the $2\times2$ hyperbolic rotation on it; the transverse coordinates do not change.
> - The general boost is the boost along $z$ seen in rotated axes, $\Lambda_{\hat{\mathbf n}} = \tilde R\Lambda_z\tilde R^{\mathsf T}$, because rotations carry the boost generators into each other as the components of a vector ($\tilde R(-iK_3)\tilde R^{\mathsf T} = n^i(-iK_i)$): the finite form of $[J_i, K_j] = i\varepsilon_{ijk}K_k$ ([[§C3.2 The Lorentz Algebra#^thm-c3-2-1|Theorem §C3.2.1]]).
> - A rotation returns to $\mathbb 1$ at $2\pi$, a boost never returns: $\cosh$ here against $\cos$ in [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], from $N^2 = +P_{tz}$ against $[\hat{\mathbf n}]_\times^2 = -Q$ (the metric's sign, Theorem §C1a.6.3, step 6).
> - Used next: the spinor matrices of the same boosts ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-14|Theorem §C5a.4.14]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]]); the boost from rest to momentum $p$ is part 2 with $\hat{\mathbf n} = \hat{\mathbf p}$, $\cosh\eta = E_{\mathbf p}/m$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-8|Theorem §C5a.9.8]], step 1).

^der-c1a-6-7

> [!derivation]- Derivation (second route: exponentiating the boost generator along n directly)
> **1. The generator.** $N_{\hat{\mathbf n}} \equiv -i\,\hat{\mathbf n}\cdot\mathbf K = n^i(E_{0i} + E_{i0}) = \begin{pmatrix} 0 & \hat{\mathbf n}^{\mathsf T} \\ \hat{\mathbf n} & 0 \end{pmatrix}$ (Theorem §C1a.6.5).
>
> **2. Its powers.** $N_{\hat{\mathbf n}}^2 = \begin{pmatrix} \hat{\mathbf n}^{\mathsf T}\hat{\mathbf n} & 0 \\ 0 & \hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & P \end{pmatrix} \equiv \Pi$, a projector ($\Pi^2 = \Pi$ since $P^2 = P$), onto the plane of $e_0$ and $(0, \hat{\mathbf n})$; $N_{\hat{\mathbf n}}^3 = N_{\hat{\mathbf n}}\Pi = \begin{pmatrix} 0 & \hat{\mathbf n}^{\mathsf T}P \\ \hat{\mathbf n} & 0 \end{pmatrix} = N_{\hat{\mathbf n}}$, using $\hat{\mathbf n}^{\mathsf T}P = \hat{\mathbf n}^{\mathsf T}$. So $N_{\hat{\mathbf n}}^{2k} = \Pi$ ($k \ge 1$), $N_{\hat{\mathbf n}}^{2k+1} = N_{\hat{\mathbf n}}$.
>
> **3. Sum.** As in step 3 of the first route, $e^{\eta N_{\hat{\mathbf n}}} = \mathbb 1 + (c - 1)\Pi + s\,N_{\hat{\mathbf n}} = \begin{pmatrix} c & s\,\hat{\mathbf n}^{\mathsf T} \\ s\,\hat{\mathbf n} & \mathbb 1_3 + (c - 1)P \end{pmatrix}$.
>
> *What this route shows:* no rotation is needed; the projector $\Pi$ onto the boost plane plays the role of $P_{tz}$, and part 1 is the case $\hat{\mathbf n} = \hat{\mathbf z}$, $\Pi = P_{tz}$.

^der-c1a-6-7b

*Uses:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C1a.4 The Lorentz Group#^cau-c1a-4-2|§C1a.4, Caution: Notation against Relativity level B]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]]

> [!remark]- Connections
> - The tangent space at the identity of a matrix group defined by $M^{\mathsf T}GM = G$ is $\{\omega : \omega^{\mathsf T}G + G\omega = 0\}$; for $G = \mathbb 1$ these are the antisymmetric matrices of $\mathfrak{so}(n)$, for $G = g$ the matrices with $g\omega$ antisymmetric — [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-6|REL ★ Remark: Infinitesimal Lorentz transformations]].
> - The rotation half of the algebra, with the same $i$ and the same Hermiticity, is Quantum Mechanics' $[\hat J_i, \hat J_j] = i\varepsilon_{ijk}\hat J_k$ derived from the rotation group acting on kets; there it is a principle about states, here a property of $4\times4$ matrices acting on indices — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].
> - On the spatial components the rotation generators are $(J_i)^l{}_m = -i\varepsilon_{ilm}$, the spin-1 matrices, while the time component is untouched: under rotations a four-vector is spin $0 \oplus$ spin 1 — [[§C3.1 Groups, Algebras and Representations of Rotations#^ex-c3-1-2|Example §C3.1.2]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-4|Theorem §C3.3.4]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]] (the vector field itself: [[§C4.1 The Vector Field and Its Lorentz Transformation#^rem-c4-1-1|§C4.1, Remark: The quantum vector field, recalled]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]]).
> - The infinitesimal displacement $\delta x^\mu = \omega^\mu{}_\nu x^\nu$ is what Noether's theorem turns into the Lorentz current $\mathcal M^{\mu\nu\rho}$ and the charges $\mathbf J$, $\mathbf K$; the boost charge's conservation says the centre of energy moves uniformly — [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-3|Theorem §C1b.8.3]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-5|REL Remark: Ten parameters, ten conservation laws]].
> - A field transforms by an orbital part acting on its argument and a spin part $S^{\mu\nu}$ acting on its indices; for a vector field the spin part is $M^{\mu\nu}$ of this note — [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]], [[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|Example §C1b.1.1]].
> - The same rotation or boost acts on a Dirac spinor through the spinor generators, with half the angle and half the rapidity; the $4\times4$ matrices of both representations stand side by side, with the covariance of $\gamma^\mu$ checked entry by entry — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-13|Theorem §C5a.4.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-14|Theorem §C5a.4.14]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]].
> - Rodrigues' formula $R = \cos\theta\,\mathbb 1 + (1 - \cos\theta)\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T} + \sin\theta\,[\hat{\mathbf n}]_\times$ and the boost $\mathbb 1 + (\cosh\eta - 1)\Pi + \sinh\eta\,N_{\hat{\mathbf n}}$ are one formula: a projector onto the plane that moves, and a generator whose square is $\mp$ that projector; for spin ½ the same split gives $\cos\frac\theta2 - i\sin\frac\theta2\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^ex-c5-1-2|QM Example §C5.1.2]].
> - $e^{\theta\epsilon}$ with $\epsilon^2 = -1$ is Euler's formula for a $2\times2$ real matrix, the matrix version of $e^{i\theta} = \cos\theta + i\sin\theta$; $e^{\eta\sigma}$ with $\sigma^2 = +1$ is its hyperbolic twin, the "split-complex" numbers — [[§39★ Fundamental Matrices#^def-39-3|331 Def. §39.3]].
