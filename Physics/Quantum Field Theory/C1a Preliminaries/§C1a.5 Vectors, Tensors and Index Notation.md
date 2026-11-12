---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.4 The Lorentz Group]] · ↑ [[· C1a Preliminaries]] · [[§C1a.6 Calculus with Indices]] →

*Sources: the user's PHY 513 notes, Ch. 1 §§1.4–1.5, Ch. 2 §2.3 ("Derivatives") · PHY 513 Lecture 1 (Larsen), Part C; Problem Set 1, as recorded in the user's notes · Yu Zhao-Huan, 量子场论讲义, §§1.4–1.5.*

What index calculus does field theory need, and why are its rules consequences rather than conventions? Relativity level B is the home of four-vectors, the metric and index gymnastics ([[§B1.1 The Metric and Index Notation|REL §B1.1]]), tensors defined by their components, the invariant tensors, the Levi-Civita symbol as a pseudotensor, the gradient as a covector and the covariance principle ([[§B2.2 Tensors and the Covariance Principle|REL §B2.2]]); with $c = 1$ they hold here unchanged and are linked, not restated. This section adds what field theory uses on top: tensors as multilinear maps (so that the transformation law is derived), the contraction identities of $\varepsilon$ and its link to determinants, the $\varepsilon^{0123}$ convention against Peskin–Schroeder, and the decomposition of a two-tensor and duality. The calculus with indices (plane waves, functions of $x^2$, Taylor expansion as the generator of translations, and derivatives with respect to four-vectors and tensor components, the tool behind every Euler–Lagrange equation and Noether current of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]]) is the next section, [[§C1a.6 Calculus with Indices|§C1a.6]]. The linear algebra underneath, the dual space, tensors as multilinear maps and the transformation law that multilinearity forces, is mathematics ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]]), and so is the representation theory that says which pieces of a two-tensor no Lorentz transformation mixes and which are irreducible ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors|§CB.8]], [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.19]]); they are proved there, linked from each box and listed at the end. This section keeps, in the form the calculations use, the index calculus with the metric, the transformation law of tensor components, and the invariance of $g$ and $\varepsilon$.

**Setup.** No physical system: index calculus on Minkowski space ($\hbar = c = 1$, $g = \operatorname{diag}(+,-,-,-)$, $\varepsilon^{0123} = +1$), valid in any relativistic theory, classical or quantum. The two kinematic boxes, [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]] and [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], assume only on-shell external momenta and four-momentum conservation, whatever the dynamics.

## Conventions and invariants

> [!definition] Definition §C1a.5.1: Four-Vectors and Index Positions in Natural Units
> With $c = 1$: $x^\mu = (t, \mathbf x)$, $p^\mu = (E, \mathbf p)$ (upper, contravariant); $x_\mu = g_{\mu\nu}x^\nu = (t, -\mathbf x)$ (lower, covariant); $g^{\mu\nu}$, the inverse of $g_{\mu\nu}$, is numerically the same matrix. An index appearing once up and once down in a term is summed; then
>
> $$
> x^2 = x_\mu x^\mu = t^2 - \mathbf x^2, \qquad p\cdot x = p_\mu x^\mu = Et - \mathbf p\cdot\mathbf x, \qquad p^2 = E^2 - \mathbf p^2 = m^2 \ \ (\text{mass shell}),
> $$
>
> $$
> \partial_\mu = \frac{\partial}{\partial x^\mu} = (\partial_t, \nabla), \qquad \partial^\mu = g^{\mu\nu}\partial_\nu = (\partial_t, -\nabla), \qquad \partial^2 \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2 .
> $$
>
> The last operator is the d'Alembertian (names in other sources: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|Caution: Names for the d'Alembertian]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4, eqs. (fourvector), (lowerindex), (pq), (psquared); Ch. 2 §2.3, eqs. (partial), (box) · PHY 513 Lecture 1, Part C ("Index Gymnastics") · Yu §1.3, eqs. (1.18)–(1.23); §1.4, eqs. (1.89), (1.93)*

^def-c1a-5-1

> [!caution] Caution: Names for the d'Alembertian
> These notes write $\partial^2 \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$ everywhere, as Peskin–Schroeder (eq. (2.56)) and Yu do. Lecture 2 introduces both names, $\partial_\mu\partial^\mu = \partial^2 \equiv \Box$ (slide "Klein Gordon Equation"), and the user's PHY 513 notes write $\Box$ in Ch. 2–4 and $\partial^2$ from Ch. 5 on; earlier drafts of this chapter followed the first usage. Relativity and Electromagnetism level C write $\Box = \partial_\mu\partial^\mu$, with $c$ restored ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-7|REL Theorem §B2.2.7]]); Griffiths and Electromagnetism level B write $\Box^2 = \nabla^2 - \frac{1}{c^2}\partial_t^2$ ([[§B11.1★ Potentials, Gauges and Retarded Potentials#^def-b11-1-1|EM Def. §B11.1.1]]), the opposite sign: $\partial^2 = -\Box^2$ at $c = 1$.
>
> *Source: Lecture 2, slide "Klein Gordon Equation" · the user's PHY 513 notes, Ch. 2 §2.3, eq. (box), Ch. 6 · PS §2.4, eq. (2.56) · Yu §1.4*

^cau-c1a-5-7

These are [[§B1.1 The Metric and Index Notation#^def-b1-1-1|REL Def. §B1.1.1]]–[[§B1.1 The Metric and Index Notation#^def-b1-1-4|REL Def. §B1.1.4]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]] and [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-7|REL Theorem §B2.2.7]] with $c = 1$ and $\eta \to g$. That $p^\mu = m\,dx^\mu/ds$ is a four-vector and $p^2 = m^2$ is the normalization of the four-velocity is [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-3|REL Theorem §B2.1.3]]; the corollary $\mathbf v = \mathbf p/E$ identifies the classical velocity with the real saddle point inside the light cone in [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]].

> [!caution] Caution: A contraction is a plain sum; the signs live in the components
> $a^\mu b_\mu = a^0b_0 + a^1b_1 + a^2b_2 + a^3b_3$ and $\partial_\mu F^{\mu\nu} = \partial_0F^{0\nu} + \partial_iF^{i\nu}$: no metric enters a contraction, and no minus sign appears. The familiar $a^\mu b_\mu = a^0b^0 - \mathbf a\cdot\mathbf b$ is this plain sum followed by $b_i = -b^i$, made because one insisted on upper components. In particular $\partial_i = \partial/\partial x^i$ is the ordinary gradient component, already lower, so $\partial_\mu j^\mu = \partial_tj^0 + \nabla\cdot\mathbf j$ with a plus sign. A minus is visible only in expressions written entirely with indices at one height, such as $\partial^2 = \partial_0\partial^0 + \partial_i\partial^i = \partial_t^2 - \nabla^2$, where $\partial^i = -\partial_i$ supplies it. A contracted pair may be seesawed, $\partial_iF^{i\nu} = \partial^iF_i{}^\nu$, with the same value.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Caution "A contraction is a plain sum; the signs live in the components")*

^cau-c1a-5-1

> [!caution] Caution: Index bookkeeping: legal, illegal, and matrix products
> - **Legal terms.** Within one term an index appears at most twice; if twice, once up and once down (summed); if once, it is free, and both sides of an equation carry the same free indices at the same heights ([[§B1.1 The Metric and Index Notation#^def-b1-1-2|REL Def. §B1.1.2]]). So $a_\mu a_\nu b^{\mu\rho}$ is a legal tensor with free $\nu$, $\rho$; $a_\mu a_\nu b^{\mu\rho}a_\nu$ ($\nu$ twice down) and $a_\rho a_\nu b^{\mu\rho}a_\rho$ ($\rho$ three times) are illegal; $a_\rho a_\nu b^{\rho\mu} = B^{\mu\nu}$ is illegal ($\nu$ down on the left, up on the right); $a_\rho a_\nu b^{\rho\mu} = B^{\mu\rho}{}_\nu z_\rho$ is legal.
> - **Factors commute; dummies rename.** Each factor is a number, so order is free (unlike matrices); a dummy may be renamed to any letter not used in the same term.
> - **Matrix products.** An index expression is a matrix product once ordered so that each contraction joins the second index of one factor to the first of the next: $C_{\sigma\lambda}B^\nu{}_\rho B^\mu{}_\nu D^{\rho\sigma} = (BBDC)^\mu{}_\lambda$. A contraction on the "wrong" index is a transpose; for a non-symmetric tensor $T^\mu{}_\nu$ and $T_\nu{}^\mu$ are different objects, as $\Lambda^\mu{}_\nu$ and $\Lambda_\nu{}^\mu = (\Lambda^{-1})^\mu{}_\nu$ are.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4 (Cautions "Dummy indices have no identity", "Index bookkeeping: legal, illegal, and matrix products (Problem Set 1)") · PHY 513, Problem Set 1, Problems 1–2*

^cau-c1a-5-2

> [!caution] Caution: Three deltas that are not the same object
> - $\delta^\mu{}_\nu$, one index up and one down, is the only "delta" that is a Lorentz tensor: the identity map, with trace $\delta^\mu{}_\mu = 4$, acting by substitution, $\delta^\mu{}_\nu A^\nu = A^\mu$.
> - $g_{\mu\nu}$ is $\delta$ with an index lowered, a tensor but numerically $\operatorname{diag}(1, -1, -1, -1)$; writing "$\delta_{\mu\nu}$" for it is a common source of sign errors. $g_{\mu\nu}g^{\mu\nu} = \delta^\mu{}_\mu = 4$.
> - $\delta_{ij}$, the three-dimensional delta, is invariant under rotations, not boosts; the lowered spatial block of the metric is $g_{ij} = -\delta_{ij}$, so $p_i = -p^i$ while $p_0 = p^0$. "$g_{\mu\nu}g_{\mu\nu} = 4$" is true as numbers in one basis but is not a covariant expression.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Caution "Three deltas that are not the same object")*

^cau-c1a-5-3

> [!definition] Definition §C1a.5.2: Mandelstam Variables
> For a two-body process $1 + 2 \to 3 + 4$ with on-shell four-momenta $p_i^2 = m_i^2$ and $p_1 + p_2 = p_3 + p_4$,
>
> $$
> s = (p_1 + p_2)^2, \qquad t = (p_1 - p_3)^2, \qquad u = (p_1 - p_4)^2 .
> $$
>
> $s$ is the squared centre-of-mass energy, and $t = q^2$ the square of the momentum transfer $q = p_1 - p_3 = p_4 - p_2$.
>
> *Model:* any; *applies:* kinematics of any two-body process with on-shell external momenta and four-momentum conservation, classical or quantum, free or interacting; no dynamics enters.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4 (Definition "Mandelstam variables (Problem Set 1)") · PHY 513, Problem Set 1, Problem 5*

^def-c1a-5-2

> [!theorem] Theorem §C1a.5.1: The Mandelstam Sum Rule and the Momentum Transfer
> 1. $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.
> 2. With particle 2 at rest in the laboratory, $t = m_2^2 + m_4^2 - 2m_2E_4$, where $E_4$ is the laboratory energy of particle 4.
> 3. For elastic scattering ($m_3 = m_1$, $m_4 = m_2$), in the centre-of-mass frame, with $p' = |\mathbf p_1'|$ and $\theta'$ the angle between $\mathbf p_1'$ and $\mathbf p_3'$,
>
> $$
> t = -2p'^2(1 - \cos\theta') = -4p'^2\sin^2\tfrac{\theta'}{2} \le 0 ,
> $$
>
> vanishing only for forward scattering.
>
> *Model:* any; *applies:* as for [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]; parts 2 and 3 in the frames named; exact.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4 (Definition "Mandelstam variables (Problem Set 1)") · PHY 513, Problem Set 1, Problem 5(e)–(f)*

^thm-c1a-5-1

> [!derivation]- Derivation
> **1. Expand the squares.** With $p_i^2 = m_i^2$:
>
> $$
> s = m_1^2 + m_2^2 + 2p_1\cdot p_2, \qquad t = m_1^2 + m_3^2 - 2p_1\cdot p_3, \qquad u = m_1^2 + m_4^2 - 2p_1\cdot p_4 .
> $$
>
> **2. Add and use conservation.** $s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2p_1\cdot(p_2 - p_3 - p_4)$, and $p_2 - p_3 - p_4 = -p_1$ by $p_1 + p_2 = p_3 + p_4$, so the last term is $-2p_1^2 = -2m_1^2$. This gives part 1.
>
> **3. The laboratory form of $t$.** Use the second form of $q$: $t = (p_4 - p_2)^2 = m_4^2 + m_2^2 - 2p_4\cdot p_2$. With $p_2 = (m_2, \mathbf 0)$, $p_4\cdot p_2 = E_4m_2$. This is part 2. (For elastic scattering it reads $t = -2m_2(E_4 - m_2)$: minus twice the target mass times its kinetic energy.)
>
> **4. Centre-of-mass kinematics.** In this frame $\mathbf p_2' = -\mathbf p_1'$, $\mathbf p_4' = -\mathbf p_3'$, and $E_1' + E_2' = E_3' + E_4'$. For $m_3 = m_1$, $m_4 = m_2$ the right side is $\sqrt{q'^2 + m_1^2} + \sqrt{q'^2 + m_2^2}$ with $q' = |\mathbf p_3'|$, the same strictly increasing function of $q'$ as the left side is of $p'$; so $q' = p'$, and then $E_3' = E_1'$.
>
> **5. Evaluate.** $t = (p_1' - p_3')^2 = m_1^2 + m_3^2 - 2\bigl(E_1'E_3' - \mathbf p_1'\cdot\mathbf p_3'\bigr) = 2m_1^2 - 2E_1'^2 + 2p'^2\cos\theta'$. With $E_1'^2 = p'^2 + m_1^2$: $t = -2p'^2 + 2p'^2\cos\theta' = -2p'^2(1 - \cos\theta')$, and $1 - \cos\theta' = 2\sin^2(\theta'/2)$.
>
> **What the derivation shows**
> - Only two of $s, t, u$ are independent; they are the natural arguments of a $2 \to 2$ amplitude, with $s$ fixing the energy and $t$ the angle.
> - $t \le 0$ in the physical region of elastic scattering: the exchanged momentum $q$ is spacelike, so an exchanged particle is off its mass shell ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|§C6c.6, Theorem §C6c.6.4]]; [[§C6d.5 Second Order#^ex-c6d-5-2|§C6d.5, Example §C6d.5.2]]).
> - Part 2 needs no frame change at all: one invariant evaluated in the most convenient frame (Remark below).

^der-c1a-5-1

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]

> [!remark] Remark: Compute invariants, not transformations
> Rather than transforming a quantity between frames, find an invariant that contains it, evaluate it in whichever frame is easiest, and read off the answer in the frame of interest. For a projectile on a fixed target, $s$ evaluated in the laboratory and in the centre-of-mass frame gives $E_{\rm cm}^2 = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$ ([[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]] with $c = 1$): at high energy $E_{\rm cm} \simeq \sqrt{2m_2E_{\rm lab}}$ grows only as the square root of the beam energy, while two colliding beams give $E_{\rm cm} = 2E_{\rm beam}$. That is why high-energy physics uses colliders. For $e^+e^- \to \gamma\gamma$ on an electron at rest, $E_{\rm cm} = \sqrt{2m_e(E + m_e)}$, each photon carrying $E_{\rm cm}/2$; restoring $c$ is [[P4 Restoring ħ and c|P4]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4 (Derivation "Invariants in practice: centre-of-mass energy (Problem Set 1)", Principle "Strategy: compute invariants") · PHY 513 Lecture 1, Part C · PHY 513, Problem Set 1, Problems 4–5*

^rem-c1a-5-1

## Tensors as multilinear maps

A covector is a linear functional on four-vectors (the dual space, [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]]), and a tensor of type $(r, s)$ is a multilinear map of $r$ covectors and $s$ vectors ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-10|Def. §CB.0.10]]). Multilinearity forces the law that Relativity takes as the definition of a tensor ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]; derived in [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]]), one $\Lambda$ per upper and one $\Lambda^{-1}$ per lower index:

$$
T'^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s} = \Lambda^{\mu_1}{}_{\rho_1}\cdots\Lambda^{\mu_r}{}_{\rho_r}\,\Lambda_{\nu_1}{}^{\sigma_1}\cdots\Lambda_{\nu_s}{}^{\sigma_s}\,T^{\rho_1\cdots\rho_r}{}_{\sigma_1\cdots\sigma_s}, \qquad \Lambda_\nu{}^\sigma = (\Lambda^{-1})^\sigma{}_\nu \quad (\Lambda \in O(1,3)) ;
$$

every tensor computation below uses it. What field theory adds is the metric, which identifies the two kinds of slot:

> [!theorem] Theorem §C1a.5.2: The Metric Identifies Vectors with Covectors
> The metric $g(x, y) = g_{\mu\nu}x^\mu y^\nu$ is a symmetric, nondegenerate, indefinite bilinear form. The map $x \mapsto x^\flat = g(x, \cdot\,)$ is an isomorphism $V \to V^\ast$, with components and inverse
>
> $$
> (x^\flat)_\mu = g_{\mu\nu}x^\nu \equiv x_\mu, \qquad x^\mu = g^{\mu\nu}x_\nu, \qquad g^{\mu\nu}g_{\nu\rho} = \delta^\mu{}_\rho .
> $$
>
> Lowering an index *is* this isomorphism: upper indices are components of vectors, lower ones of covectors, and $x_\mu x^\mu$ is the functional $x^\flat$ evaluated on $x$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5, eqs. (metricform), (flat), (inversemetric); Principle "Why indices go up and down"*

^thm-c1a-5-2

> [!derivation]- Derivation
> **1. The form.** Symmetry and bilinearity, nondegeneracy ($\det g = -1 \ne 0$) and indefiniteness are [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]], 1–3.
>
> **2. $x^\flat$ is a functional.** For fixed $x$, $y \mapsto g(x, y)$ is linear in $y$ (bilinearity), so $x^\flat \in V^{\ast}$; its components are its values on the basis, $(x^\flat)_\mu = x^\flat(e_\mu) = g(x, e_\mu) = g_{\nu\mu}x^\nu = g_{\mu\nu}x^\nu$ (symmetry of $g$).
>
> **3. Injective, hence bijective.** The map $x \mapsto x^\flat$ is linear. If $x^\flat = 0$ then $g(x, y) = 0$ for all $y$, and nondegeneracy gives $x = 0$. A linear injection between spaces of equal finite dimension ($\dim V^{\ast} = \dim V$, [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]) is surjective.
>
> **4. The inverse.** Its matrix is $g_{\mu\nu}$; the inverse map has the inverse matrix $g^{\mu\nu}$, defined by $g^{\mu\nu}g_{\nu\rho} = \delta^\mu{}_\rho$; numerically $g^{\mu\nu} = g_{\mu\nu}$ because $\operatorname{diag}(1, -1, -1, -1)$ is its own inverse ([[§B1.1 The Metric and Index Notation#^thm-b1-1-2|REL Theorem §B1.1.2]], 1), a coincidence of this basis.
>
> **What the derivation shows**
> - Only nondegeneracy is used, not positivity: the identification works for any signature, which is why "metric" rather than "inner product".
> - Lowering commutes with Lorentz transformations, $(\Lambda x)^\flat = x^\flat\circ\Lambda^{-1}$, which in components is the inverse-transpose law $\Lambda_\mu{}^\nu = (\Lambda^{-1})^\nu{}_\mu$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2 and 4).
> - In differential geometry this is the musical isomorphism of a pseudo-Riemannian metric on one tangent space ([[§32 The Cotangent Space#^def-32-4|591 Def. §32.4]]).

^der-c1a-5-2

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]], [[§B1.1 The Metric and Index Notation#^thm-b1-1-2|REL Theorem §B1.1.2]], [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]

> [!caution] Caution: A tensor is not a product of vectors
> The law is exhibited on products $p^\mu q^\nu$, but a general two-tensor is a *sum* of such products: a product has rank one as a $4\times4$ matrix, a general $T^{\mu\nu}$ rank up to four. The field-strength tensor of electromagnetism is not a product ([[§C1a.8 Relativistic Electrodynamics in Index Form|§C1a.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Caution "A tensor is not a product of vectors") · PHY 513 Lecture 1, Part C ("Tensors")*

^cau-c1a-5-4

> [!theorem] Theorem §C1a.5.3: The Metric and the Levi-Civita Symbol Are Invariant Tensors
> For every Lorentz transformation $\Lambda \in O(1,3)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]), acting on components by the tensor law (one $\Lambda$ per upper, one $\Lambda^{-1}$ per lower index, [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]):
> 1. $g$, its inverse and $\delta$ have the same components in every frame,
>
> $$
> g_{\rho\sigma}\Lambda^\rho{}_\mu\Lambda^\sigma{}_\nu = g_{\mu\nu}, \qquad \Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\,g^{\alpha\beta} = g^{\mu\nu}, \qquad \Lambda^\mu{}_\alpha\,\delta^\alpha{}_\beta\,\Lambda_\nu{}^\beta = \delta^\mu{}_\nu ,
> $$
>
> so raising and lowering indices commute with every Lorentz transformation ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]]).
> 2. The Levi-Civita symbol ($\varepsilon^{0123} = +1$, [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|Caution: The sign of ε⁰¹²³]]) picks up the determinant,
>
> $$
> \Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,\varepsilon^{\alpha\beta\gamma\delta} = (\det\Lambda)\,\varepsilon^{\mu\nu\rho\sigma} :
> $$
>
> invariant under $SO(1,3)$ (so also under $\mathcal P\mathcal T = -\mathbb 1$), reversed under $\mathcal P$ and under $\mathcal T$ separately: a pseudotensor.
> 3. *How to use it:* a full contraction of tensors with $g$ and $\delta$ only is a scalar under all of $O(1,3)$; a full contraction of tensors containing one $\varepsilon$ (or any odd number) is a pseudoscalar: invariant under $SO(1,3)$, odd under $\mathcal P$ and under $\mathcal T$. For example $F_{\mu\nu}F^{\mu\nu}$ is a scalar and $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ a pseudoscalar ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]]), and so is $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]]).
>
> *Proof:* [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]] (there: $g$ is an invariant tensor and lowering an intertwiner $V \to V^\ast$; $\Lambda\cdot\varepsilon = (\det\Lambda)\,\varepsilon$). The same statements in Relativity's notation ($c$ explicit, $\eta$ for $g$) are [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]] (part 1) and [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]], 1 (part 2).
>
> *Source: Yu §1.5, p. 18, eq. (1.96) and the paragraph after it ("Minkowski 度规 $g_{\mu\nu}$ 是一个 2 阶的 (0, 2) 型 Lorentz 张量，不过，它是常数，在任何惯性系中不变"; $\delta^\mu{}_\nu$ a constant (1, 1) tensor), eqs. (1.99)–(1.100) (tensors and pseudotensors under parity), p. 20, eqs. (1.110)–(1.112) ($\varepsilon^{\mu\nu\rho\sigma}$ a constant pseudotensor) · the user's PHY 513 notes, Ch. 1 §1.5 (subsection "The invariant tensors: δ, g, and ε"; Definition "Tensors and pseudotensors")*

^thm-c1a-5-3

## The Levi-Civita symbol

> [!caution] Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder
> These notes, the course (Problem Set 1), Yu (1.104) and Relativity level B ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]]) use $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$; Peskin–Schroeder use $\varepsilon^{0123} = -1$. Every quantity containing one $\varepsilon$ changes sign between the two: the dual field tensor $\tilde F^{\mu\nu}$, and $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$ here, $+8\,\mathbf E\cdot\mathbf B$ in Peskin–Schroeder ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]]). Products of two $\varepsilon$'s do not. Check the convention of a source before comparing any pseudoscalar sign. Lowering all four indices always costs $\det g = -1$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Definition "The Levi-Civita symbol, and the convention of these notes") · PHY 513, Problem Set 1, Problem 3 · Yu §1.5, eq. (1.104)*

^cau-c1a-5-5

Its transformation law, $\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,\varepsilon^{\alpha\beta\gamma\delta} = (\det\Lambda)\,\varepsilon^{\mu\nu\rho\sigma}$, invariant under $\det\Lambda = +1$ and odd under $\mathcal P$ and $\mathcal T$ separately (a pseudotensor), is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 2 ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]]).

> [!theorem] Theorem §C1a.5.4: Contraction Identities of the Levi-Civita Symbol
> 1. (Minkowski, $\varepsilon^{0123} = +1$.) The product of two symbols is minus the determinant of deltas,
>
> $$
> \varepsilon_{\mu\nu\rho\sigma}\,\varepsilon^{\alpha\beta\gamma\delta} = -\det\begin{pmatrix} \delta^\alpha_\mu & \delta^\alpha_\nu & \delta^\alpha_\rho & \delta^\alpha_\sigma \\ \delta^\beta_\mu & \delta^\beta_\nu & \delta^\beta_\rho & \delta^\beta_\sigma \\ \delta^\gamma_\mu & \delta^\gamma_\nu & \delta^\gamma_\rho & \delta^\gamma_\sigma \\ \delta^\delta_\mu & \delta^\delta_\nu & \delta^\delta_\rho & \delta^\delta_\sigma \end{pmatrix} \equiv -\delta^{\alpha\beta\gamma\delta}_{\mu\nu\rho\sigma},
> $$
>
> and successive contractions give $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\beta\gamma\delta} = -\delta^{\beta\gamma\delta}_{\nu\rho\sigma}$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\gamma\delta} = -2\bigl(\delta^\gamma_\rho\delta^\delta_\sigma - \delta^\gamma_\sigma\delta^\delta_\rho\bigr)$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\delta} = -6\,\delta^\delta_\sigma$, $\ \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = -24$.
> 2. (Euclidean three dimensions, $\varepsilon_{123} = 1$, all indices down.) $\varepsilon_{ijk}\varepsilon_{lmn} = \delta^{lmn}_{ijk}$ (no sign), $\ \varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$, $\ \varepsilon_{ijk}\varepsilon_{ijm} = 2\delta_{km}$, $\ \varepsilon_{ijk}\varepsilon_{ijk} = 6$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols"), eqs. (epseps4), (epseps2), (epseps3) · Yu §1.5, eqs. (1.106), (1.118)–(1.119)*

^thm-c1a-5-4

> [!derivation]- Derivation
> **1. Both sides vanish together.** The left side vanishes if two of $\mu\nu\rho\sigma$ coincide, or two of $\alpha\beta\gamma\delta$. The determinant then has two equal columns, or two equal rows, and vanishes too ([[§37 Determinants#^ladr-9-45|LADR Thm. 9.45]]).
>
> **2. Distinct indices.** Otherwise $(\mu\nu\rho\sigma) = \tau(0123)$ and $(\alpha\beta\gamma\delta) = \pi(0123)$ for permutations $\tau$, $\pi$. The left side is $\operatorname{sgn}\tau\,\varepsilon_{0123}\cdot\operatorname{sgn}\pi\,\varepsilon^{0123} = -\operatorname{sgn}\tau\operatorname{sgn}\pi$, using $\varepsilon_{0123} = -1$ (lowering four indices costs $g_{00}g_{11}g_{22}g_{33} = -1$). The matrix of deltas has exactly one entry $1$ in each row and column: it is a permutation matrix, of determinant $\operatorname{sgn}(\tau^{-1}\pi) = \operatorname{sgn}\tau\operatorname{sgn}\pi$ ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]). So the two sides agree, with the minus sign. ⚑ By-product: the overall sign is $\varepsilon_{0123}\varepsilon^{0123} = \det g = -1$, the Minkowski signature; in Euclidean signature it is $+1$ → part 2.
>
> **3. One contraction of a $k\times k$ delta in $n$ dimensions.** Expand $\delta^{\alpha\cdots}_{\mu\cdots}$ (first upper index $\alpha$, first lower $\mu$) along its first row: $\sum_j(-1)^{1+j}\delta^\alpha_{\lambda_j}M_{1j}$, where $\lambda_j$ is the $j$-th lower index and $M_{1j}$ the minor. Set $\alpha = \mu$ and sum. The term $j = 1$ gives $\delta^\mu_\mu M_{11} = n\,M_{11}$. For $j \ge 2$, $\delta^\mu_{\lambda_j}$ replaces $\mu$ by $\lambda_j$ in the first column of $M_{1j}$; moving that column from position 1 to position $j - 1$ takes $j - 2$ transpositions and turns $M_{1j}$ into $(-1)^{j-2}M_{11}$; with the sign $(-1)^{1+j}$ each such term is $-M_{11}$. There are $k - 1$ of them:
>
> $$
> \delta^{\mu\beta\cdots}_{\mu\nu\cdots} = (n - k + 1)\,\delta^{\beta\cdots}_{\nu\cdots} .
> $$
>
> **4. Successive contractions, $n = 4$.** $k = 4$: factor $1$, so $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\beta\gamma\delta} = -\delta^{\beta\gamma\delta}_{\nu\rho\sigma}$. $k = 3$: factor $2$, giving $-2\delta^{\gamma\delta}_{\rho\sigma} = -2(\delta^\gamma_\rho\delta^\delta_\sigma - \delta^\gamma_\sigma\delta^\delta_\rho)$. $k = 2$: factor $3$, giving $-6\delta^\delta_\sigma$. $k = 1$: $\delta^\sigma_\sigma = 4$, giving $-24 = -4!$. (Check of the last: $4!$ nonzero terms, each $(\pm1)(\mp1) = -1$.)
>
> **5. Three Euclidean dimensions.** Steps 1–3 with $n = 3$, $\varepsilon_{123}\varepsilon_{123} = +1$ (indices raised and lowered by $\delta_{ij}$, no signs): $\varepsilon_{ijk}\varepsilon_{lmn} = +\delta^{lmn}_{ijk}$; contracting $i = l$ gives factor $3 - 3 + 1 = 1$, i.e. $\delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ after renaming; then factor $2$, giving $2\delta_{km}$; then $\delta_{kk} = 3$, giving $6$.
>
> **What the derivation shows**
> - Every Minkowski $\varepsilon\varepsilon$ identity is its Euclidean twin times $\det g = -1$.
> - Working rules: fix the convention for $\varepsilon_{0123}$ first; bring the contracted indices to the leading slots of both symbols by antisymmetry (one sign per transposition) before applying the identity; in three-vector notation every lowered spatial index of a four-vector carries a sign ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-6|Caution: Three-dimensional notation inside a four-dimensional expression]]).
> - Used next: duality squares to $-1$ (Theorem §C1a.5.7); the invariants of the field tensor ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]]); the three-dimensional identity is the tool behind the vector-calculus product rules of [[§B1.1 Fields, Integral Theorems and Curvilinear Coordinates#^thm-b1-1-1|EM Theorem §B1.1.1]].

^der-c1a-5-4

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]], [[§37 Determinants#^ladr-9-45|LADR Thm. 9.45]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]

> [!theorem] Theorem §C1a.5.5: The Levi-Civita Symbol and the Determinant
> For every $4\times4$ matrix $A^\mu{}_\nu$:
> 1. $\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$;
> 2. $\det A = -\dfrac{1}{4!}\,\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta$;
> 3. if $\det A \ne 0$, $\ (A^{-1})^\nu{}_\mu = -\dfrac{1}{3!\,\det A}\,\varepsilon_{\mu\mu_2\mu_3\mu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4}A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4}$;
> 4. for four vectors, $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = -\det[a|b|c|d]$ (the matrix with columns $a^\mu, \dots, d^\mu$), which vanishes if and only if $a, b, c, d$ are linearly dependent.
>
> In Euclidean signature the minus signs in 2–4 are absent.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Levi-Civita and determinants"), eq. (epsdet) · Yu §1.5, eqs. (1.107)–(1.110)*

^thm-c1a-5-5

> [!derivation]- Derivation
> **1. Part 1.** Call the left side $L_{\alpha\beta\gamma\delta}$. Exchanging two of its free indices, say $\alpha \leftrightarrow \beta$, and renaming the dummies $\mu \leftrightarrow \nu$ gives back $L$ with $\varepsilon_{\nu\mu\rho\sigma} = -\varepsilon_{\mu\nu\rho\sigma}$: $L$ is totally antisymmetric, hence $L_{\alpha\beta\gamma\delta} = L_{0123}\,\varepsilon_{\alpha\beta\gamma\delta}/\varepsilon_{0123}$. And $L_{0123} = \varepsilon_{\mu\nu\rho\sigma}A^\mu{}_0A^\nu{}_1A^\rho{}_2A^\sigma{}_3 = \varepsilon_{0123}\sum_\pi\operatorname{sgn}\pi\,A^{\pi(0)}{}_0\cdots A^{\pi(3)}{}_3 = \varepsilon_{0123}\det A$ by the Leibniz formula ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]). So $L_{\alpha\beta\gamma\delta} = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$. (For $A = \Lambda$ this is the pseudotensor law of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 2.)
>
> **2. Part 2.** Contract part 1 with $\varepsilon^{\alpha\beta\gamma\delta}$ and use $\varepsilon_{\alpha\beta\gamma\delta}\varepsilon^{\alpha\beta\gamma\delta} = -24$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]): $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha\cdots = -24\det A$.
>
> **3. Part 3.** Call the right side $B^\nu{}_\mu$ and compute $B^\nu{}_\mu A^\mu{}_\lambda$. By part 1 with the first slot filled by $A^\mu{}_\lambda$: $\varepsilon_{\mu\mu_2\mu_3\mu_4}A^\mu{}_\lambda A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4} = \det A\,\varepsilon_{\lambda\nu_2\nu_3\nu_4}$. Then $B^\nu{}_\mu A^\mu{}_\lambda = -\frac{1}{3!}\varepsilon_{\lambda\nu_2\nu_3\nu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4} = -\frac{1}{6}(-6\,\delta^\nu_\lambda) = \delta^\nu_\lambda$ by Theorem §C1a.5.4. A left inverse of a square matrix is the inverse.
>
> **4. Part 4.** Put $A = [a|b|c|d]$, $A^\mu{}_0 = a^\mu$ etc., and $(\alpha\beta\gamma\delta) = (0123)$ in part 1: $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = \varepsilon_{0123}\det A = -\det A$. It vanishes iff $\det A = 0$ iff the columns are dependent ([[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]). ⚑ By-product: with all indices raised on $\varepsilon$ and lowered on the vectors the same number results, $\varepsilon^{\mu\nu\rho\sigma}a_\mu b_\nu c_\rho d_\sigma = \det[a_\mu|\cdots] = \det g\,\det[a|\cdots] = -\det[a|b|c|d]$: the signed four-volume of the parallelepiped spanned by $a, b, c, d$ is $-\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma$ in this convention. (The user's PHY 513 notes, Ch. 1 §1.5, item 3, write it without the minus sign; checked numerically.)
>
> **What the derivation shows**
> - $\varepsilon$ is the antisymmetrizer, and the determinant is what antisymmetrizing a product of rows produces; the Minkowski minus signs are all $\varepsilon_{0123} = \det g$.
> - The cofactor formula is the same identity read backwards; it never needs Gaussian elimination.
> - Used next: Example §C1a.5.1; a pseudoscalar built from momenta needs four linearly independent ones, hence at least five particles in a process (with momentum conservation).

^der-c1a-5-5

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]]

> [!example] Example §C1a.5.1: Momentum Conservation Kills ε p₁p₂p₃p₄
> For four momenta with $\sum_{i=1}^4 p_i = 0$, $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = 0$: by [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]], 4, it is $\pm$ the determinant with columns $p_1, \dots, p_4$, and adding the first three columns to the fourth produces the zero column. The contraction is a pseudoscalar ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 3), invariant only under $\det\Lambda = +1$; it can appear in an amplitude only when five or more momenta are involved. (For the course: $\varepsilon^{0123} = +1$, $\varepsilon^{1230} = -1$, three transpositions, and $\varepsilon^{1213} = 0$.)
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Levi-Civita and determinants", physical instance) · PHY 513, Problem Set 1, Problem 3*

^ex-c1a-5-1

> [!remark] Remark: What the cross product is
> In three dimensions $\varepsilon_{ijk}$ converts an antisymmetric two-index object into a one-index one, $(\mathbf a\times\mathbf b)_i = \frac12\varepsilon_{ijk}(a_jb_k - a_kb_j)$, with inverse $a_jb_k - a_kb_j = \varepsilon_{jki}(\mathbf a\times\mathbf b)_i$. This works only because an antisymmetric $3\times3$ matrix has three entries, the number of a vector's components: the antisymmetric tensor is the fundamental object and the vector its three-dimensional shorthand, which is why cross products and curls are axial (they carry a hidden $\varepsilon$). In four dimensions an antisymmetric two-tensor has six components, there is no cross product of two four-vectors, and the curl survives as the antisymmetrized derivative $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ with no $\varepsilon$ at all; the four-dimensional $\varepsilon$ acts one level up, trading one antisymmetric tensor for another (duality, [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]), and $\nabla\cdot(\nabla\times\mathbf A) = 0$ becomes the Bianchi identity $\partial_\mu\tilde F^{\mu\nu} = 0$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-2|Theorem §C1a.8.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Three-dimensional vector calculus in index form", "What the cross product is", "Four dimensions") · Yu §1.5, eqs. (1.120)–(1.121)*

^rem-c1a-5-2

> [!caution] Caution: Three-dimensional notation inside a four-dimensional expression
> In $F_{ij} = -\varepsilon_{ijk}B_k$, $k$ is summed Euclidean-style and $B_k$ means the $k$-th component of the vector $\mathbf B$ (equal to $B^k$), not a lowered Minkowski component (which would be $-B^k$), while $i, j$ are Minkowski spatial indices whose height matters. Whenever a Minkowski expression is reduced to three-vector notation, each lowered spatial index contributes $A_i = -A^i$, and the convention for the three-dimensional symbols must be stated; that is the origin of the minus sign in $F_{ij}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Three-dimensional vector calculus in index form", last paragraph)*

^cau-c1a-5-6

> [!example] Example §C1a.5.2: The Centre-of-Mass Momentum from a Transverse Component
> A projectile ($m_1$, $E_{\rm lab}$, momentum $p_{\rm lab}$ along $x^1$) hits $m_2$ at rest. Let $P = p_1 + p_2$, $Q = p_1 - p_2$ and $T_{\mu\nu} = \varepsilon_{\mu\nu\rho\sigma}P^\sigma Q^\rho$. The boost to the centre-of-mass frame is along $x^1$, so $\Lambda_2{}^\alpha = \delta_2{}^\alpha$, $\Lambda_3{}^\alpha = \delta_3{}^\alpha$, and $T'_{23} = \Lambda_2{}^\alpha\Lambda_3{}^\beta T_{\alpha\beta} = T_{23}$: a component transverse to a boost is invariant under that boost. Only $\{\rho, \sigma\} = \{0, 1\}$ contribute, with $\varepsilon_{2301} = \varepsilon_{0123} = -1$ (two transpositions) and $\varepsilon_{2310} = +1$:
>
> $$
> T_{23} = -Q^0P^1 + Q^1P^0 .
> $$
>
> Laboratory: $P = (E_{\rm lab} + m_2, p_{\rm lab}, 0, 0)$, $Q = (E_{\rm lab} - m_2, p_{\rm lab}, 0, 0)$, so $T_{23} = -(E_{\rm lab} - m_2)p_{\rm lab} + p_{\rm lab}(E_{\rm lab} + m_2) = 2m_2p_{\rm lab}$. Centre of mass: $P = (E_{\rm cm}, \mathbf 0)$, $Q^1 = p' - (-p') = 2p'$, so $T_{23} = 2E_{\rm cm}p'$. Equating,
>
> $$
> p' = \frac{m_2\,p_{\rm lab}}{E_{\rm cm}} .
> $$
>
> No boost was solved for: one tensor component, evaluated in two frames.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "The centre-of-mass momentum from a transverse tensor component (Problem Set 1)") · PHY 513, Problem Set 1, Problem 5(d) (the problem's suggested tensor)*

^ex-c1a-5-2

## Decomposing a two-tensor; duality

> [!theorem] Theorem §C1a.5.6: The Trace, Symmetric and Antisymmetric Parts Do Not Mix
> Every two-tensor splits uniquely as
>
> $$
> T^{\mu\nu} = \underbrace{\Bigl(T^{(\mu\nu)} - \tfrac14g^{\mu\nu}T^\rho{}_\rho\Bigr)}_{\text{symmetric traceless: }9} + \underbrace{T^{[\mu\nu]}}_{\text{antisymmetric: }6} + \underbrace{\tfrac14g^{\mu\nu}T^\rho{}_\rho}_{\text{trace: }1},
> $$
>
> $T^{(\mu\nu)} = \frac12(T^{\mu\nu} + T^{\nu\mu})$, $T^{[\mu\nu]} = \frac12(T^{\mu\nu} - T^{\nu\mu})$, and each of the three subspaces is mapped into itself by every Lorentz transformation. (Each is irreducible under $SO^+(1,3)$ over $\mathbb R$; over $\mathbb C$ the three pieces are $(1, 1)$, $(1, 0)\oplus(0, 1)$ and $(0, 0)$: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], proved in [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-12|Theorem §CB.19.12]], irreducible in the sense of [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-9|Def. §CB.3.9]].)
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Irreducible pieces of a two-tensor"), eq. (decomposition) · PHY 513 Lecture 1, Part C ("Irreducible parts of two-tensor representation")*

^thm-c1a-5-6

> [!derivation]- Derivation
> **1. Symmetric and antisymmetric.** The split $T = T^{(\,)} + T^{[\,]}$ is unique, and a symmetric (antisymmetric) tensor stays so under every $\Lambda$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 1): exchanging $\mu \leftrightarrow \nu$ in $\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma}$ is the same as exchanging the dummies $\rho \leftrightarrow \sigma$.
>
> **2. The trace is a scalar.** $g_{\mu\nu}T'^{\mu\nu} = g_{\mu\nu}\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma} = g_{\rho\sigma}T^{\rho\sigma}$ by the defining condition ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]); only the symmetric part contributes to it, $g_{\mu\nu}T^{[\mu\nu]} = 0$ (symmetric times antisymmetric, [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2).
>
> **3. Split off the trace.** Write $t = T^\rho{}_\rho$ and $S^{\mu\nu} = T^{(\mu\nu)} - \frac14g^{\mu\nu}t$. Then $g_{\mu\nu}S^{\mu\nu} = t - \frac14\cdot4\,t = 0$, using $g_{\mu\nu}g^{\mu\nu} = 4$. The trace part $\frac14g^{\mu\nu}t$ transforms to $\frac14g^{\mu\nu}t$ (the metric is invariant, [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 1; $t$ is a scalar by step 2). A traceless symmetric tensor stays symmetric (step 1) and traceless (step 2). Uniqueness: the trace part is fixed by $t$, the rest by step 1.
>
> **4. Count.** Symmetric: $4 + 6 = 10$ entries, minus one trace condition: $9$; antisymmetric: $6$; trace: $1$; total $16$.
>
> **What the derivation shows**
> - The $16\times16$ matrix $\Lambda^\mu{}_\lambda\Lambda^\nu{}_\sigma$ is block diagonal in this basis: the lecture's "symmetric and antisymmetric parts do not mix".
> - Six antisymmetric components are exactly $\mathbf E$ and $\mathbf B$; nine symmetric traceless ones, a traceless stress tensor of a scale-invariant theory.
> - Used next: the antisymmetric block splits further over $\mathbb C$ (Theorem §C1a.5.7).

^der-c1a-5-6

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]

> [!theorem] Theorem §C1a.5.7: Duality Squares to −1 on Antisymmetric Tensors
> On antisymmetric $A^{\mu\nu}$ let $(\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}A_{\rho\sigma}$. Then:
> 1. $\star\star A = -A$;
> 2. $\star(\Lambda A) = (\det\Lambda)\,\Lambda(\star A)$: duality commutes with proper Lorentz transformations and anticommutes with $\mathcal P$ and $\mathcal T$;
> 3. over $\mathbb C$, the six-dimensional space is the direct sum of the eigenspaces $\star A = \pm iA$, each three-dimensional and mapped into itself by every $\Lambda$ with $\det\Lambda = 1$; $\mathcal P$ exchanges them.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols", four-dimensional example; "Irreducible pieces of a two-tensor")*

^thm-c1a-5-7

> [!derivation]- Derivation
> **1. Lower the dual.** $(\star A)_{\rho\sigma} = g_{\rho\kappa}g_{\sigma\lambda}\frac12\varepsilon^{\kappa\lambda\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma}{}^{\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$ (seesaw on the pair $\alpha\beta$, [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|Caution: A contraction is a plain sum]]).
>
> **2. Apply twice.** $(\star\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}(\star A)_{\rho\sigma} = \frac14\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$.
>
> **3. Bring the contracted pair to the front.** $\varepsilon^{\mu\nu\rho\sigma} = \varepsilon^{\rho\sigma\mu\nu}$: the permutation $(\mu\nu\rho\sigma) \to (\rho\sigma\mu\nu)$ is the product of the transpositions of the first with the third slot and the second with the fourth, even.
>
> **4. Contract.** By [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] (two contracted pairs, upper and lower roles exchanged, which is the same identity), $\varepsilon^{\rho\sigma\mu\nu}\varepsilon_{\rho\sigma\alpha\beta} = -2(\delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha)$. So $(\star\star A)^{\mu\nu} = -\frac12(A^{\mu\nu} - A^{\nu\mu}) = -A^{\mu\nu}$, by antisymmetry. ⚑ By-product: the $-1$ is $\det g$ again; in Euclidean four dimensions $\star\star = +1$ and the eigenvalues are real (self-dual and anti-self-dual forms) → part 3.
>
> **5. Part 2.** Multiply the pseudotensor law $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\Lambda^\rho{}_\alpha\Lambda^\sigma{}_\beta\varepsilon^{\kappa\lambda\alpha\beta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 2) by $\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$ and use $\Lambda^\rho{}_\alpha\Lambda_\rho{}^\gamma = \delta_\alpha{}^\gamma$: $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\varepsilon^{\kappa\lambda\gamma\delta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$. With $(\Lambda A)_{\rho\sigma} = \Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta}$ and $(\det\Lambda)^2 = 1$:
>
> $$
> (\star\Lambda A)^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta} = \det\Lambda\;\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\,\tfrac12\varepsilon^{\kappa\lambda\gamma\delta}A_{\gamma\delta} = \det\Lambda\;(\Lambda\star A)^{\mu\nu} .
> $$
>
> **6. Part 3.** $\star$ is a real linear map with $\star^2 = -1$, so over $\mathbb C$ its eigenvalues are $\pm i$ and $A = \frac12(A - i\star A) + \frac12(A + i\star A)$ splits $A$ into a $(+i)$- and a $(-i)$-eigenvector (check: $\star(A - i\star A) = \star A + iA = i(A - i\star A)$). Complex conjugation commutes with the real map $\star$ and exchanges the two eigenspaces, so they have equal dimension, $6/2 = 3$. A $\Lambda$ with $\det\Lambda = 1$ commutes with $\star$ (part 2), hence preserves each eigenspace; $\mathcal P$ anticommutes, hence sends $\star A = iA$ to $\star(\mathcal PA) = -i\mathcal PA$.
>
> **What the derivation shows**
> - Taking the dual twice returns $-A$, not $A$: the Minkowski sign. For the field tensor, $\tilde{\tilde F} = -F$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-3|Theorem §C1a.8.3]]).
> - The two three-dimensional halves are, for $F$, built from $\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$ ([[§C1a.8 Relativistic Electrodynamics in Index Form#^thm-c1a-8-4|Theorem §C1a.8.4]]); as representations they are called $(1, 0)$ and $(0, 1)$, with $\mathbf E - i\mathbf B$ the $(1, 0)$ half in these conventions ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-8|Theorem §C3.3.8]], [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]]).

^der-c1a-5-7

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|Caution: A contraction is a plain sum; the signs live in the components]]

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> Covectors, and the metric's identification of vectors with them (Theorem §C1a.5.2), live in the dual space; a tensor is a multilinear map on covectors and vectors:
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]] — the dual space $V^\ast$ and the dual basis, with no metric.
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-10|Def. §CB.0.10]] — a tensor of type $(r, s)$ as a multilinear map; vectors, covectors and numbers as special cases.
>
> Its components transform with one $\Lambda$ per upper and one $\Lambda^{-1}$ per lower index because of multilinearity; Relativity takes this law as the definition ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]), and every tensor computation above uses it:
> - [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]] with [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-15|its derivation]] — the transformation law follows from multilinearity (the display under "Tensors as multilinear maps").
>
> The metric and the Levi-Civita symbol are invariant tensors, $\varepsilon$ only up to $\det\Lambda$ (the law recalled in "The Levi-Civita symbol" and Theorem §C1a.5.5):
> - [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]] with [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^pf-cb-8-16|its proof]] — $g$ is invariant under $O(1,3)$ and lowering is an intertwiner $V \to V^\ast$; $\varepsilon$ picks up $\det\Lambda$; physics form: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]].
>
> Theorem §C1a.5.6 splits a two-tensor into pieces that no Lorentz transformation mixes: the symmetric and antisymmetric parts are subrepresentations, and irreducible means, as in Def. §CB.3.9, having no smaller invariant subspace:
> - [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]] with [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^pf-cb-8-13|its proof]] — symmetric and exterior powers are subrepresentations; $W\otimes W = \operatorname{Sym}^2W\oplus\Lambda^2W$.
> - [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-9|Def. §CB.3.9]] — invariant subspace; irreducible representation.
>
> That the pieces are irreducible, and that the antisymmetric part splits over $\mathbb C$ into the two eigenspaces of duality of Theorem §C1a.5.7, is the representation theory of two-index tensors and two-forms (in physics form: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-8|Theorem §C3.3.8]]):
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-12|Theorem §CB.19.12]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-19-12|its derivation]] — two-index tensors are $(0, 0)\oplus(1, 0)\oplus(0, 1)\oplus(1, 1)$ over $\mathbb C$; the real antisymmetric six are irreducible.
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-11|Theorem §CB.19.11]] with [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-19-11|its proof]] — two-forms are $(1, 0)\oplus(0, 1)$, the eigenspaces $\star = \pm i$ of duality.

> [!remark]- Connections
> - The dual space, multilinear maps and their components are Linear Algebra's: a $(0,2)$ tensor is a bilinear form, whose matrix changes as $C^{\mathsf T}BC$ — [[§12 Duality#^ladr-3-110|LADR Def. 3.110]], [[§38 Tensor Products#^ladr-9-85|LADR Def. 9.85]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]]; Relativity level B reaches the same law from the component side — [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]], [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-2|REL Remark: Tensors without coordinates]].
> - The Levi-Civita symbol is the alternating form of top degree, unique up to a factor because that space is one-dimensional; that is why every totally antisymmetric four-index array is a multiple of $\varepsilon$ — [[§36 Alternating Multilinear Forms#^ladr-9-37|LADR Thm. 9.37]], [[§37 The Algebra of Differential Forms#^def-37-2|452 Def. §37.2]].
> - The three-dimensional identity $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ of Theorem §C1a.5.4 is the tool behind BAC–CAB and the product rules of vector calculus — [[§B1.1 Fields, Integral Theorems and Curvilinear Coordinates#^thm-b1-1-1|EM Theorem §B1.1.1]].
> - Duality on two-forms squares to $-1$ in Lorentzian signature and to $+1$ in Euclidean signature; the Wick rotation of [[§C2b.8 Wick Rotation and the Two-Point Family|§C2b.8]] trades one for the other, and the complex split $6 = 3 + 3$ becomes the real split into self-dual and anti-self-dual forms.
> - Mandelstam variables return as the arguments of scattering amplitudes, with crossing exchanging $s$, $t$, $u$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|§C6b.1, Theorem §C6b.1.7]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|§C6c.6, Theorem §C6c.6.4]]; for fermions the $t$ and $u$ terms differ in sign, [[§C6d.5 Second Order#^thm-c6d-5-3|§C6d.5, Theorem §C6d.5.3]]).
