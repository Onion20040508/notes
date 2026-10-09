---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.4 The Lorentz Group]] · ↑ [[· C1a Preliminaries]] · [[§C1a.6 Infinitesimal Lorentz Transformations and Generators]] →

*Sources: the user's PHY 513 notes, Ch. 1 §§1.4–1.5, Ch. 2 §2.3 ("Derivatives") · PHY 513 Lecture 1 (Larsen), Part C; Problem Set 1, as recorded in the user's notes · Yu Zhao-Huan, 量子场论讲义, §§1.4–1.5.*

What index calculus does field theory need, and why are its rules consequences rather than conventions? Relativity level B is the home of four-vectors, the metric and index gymnastics ([[§B1.1 The Metric and Index Notation|REL §B1.1]]), tensors defined by their components, the invariant tensors, the Levi-Civita symbol as a pseudotensor, the gradient as a covector and the covariance principle ([[§B2.2 Tensors and the Covariance Principle|REL §B2.2]]); with $c = 1$ they hold here unchanged and are linked, not restated. This section adds what field theory uses on top: tensors as multilinear maps (so that the transformation law is derived), the contraction identities of $\varepsilon$ and its link to determinants, the $\varepsilon^{0123}$ convention against Peskin–Schroeder, the decomposition of a two-tensor and duality, and calculus with indices: plane waves, functions of $x^2$, Taylor expansion as the generator of translations, and derivatives with respect to four-vectors and tensor components, the tool behind every Euler–Lagrange equation and Noether current of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]]. The linear algebra underneath, the dual space, tensors as multilinear maps and the transformation law that multilinearity forces, is mathematics ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]]), and so is the representation theory that says which pieces of a two-tensor no Lorentz transformation mixes and which are irreducible ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors|§CB.8]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.18]]); they are shown in the blocks below, and this section keeps the index calculus with the metric.

## The mathematics used here

Covectors, and the metric's identification of vectors with them (Theorem §C1a.5.2), live in the dual space:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7]]

A tensor is a multilinear map on covectors and vectors:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9]]

Its components transform with one $\Lambda$ per upper and one $\Lambda^{-1}$ per lower index because of multilinearity; Relativity takes this law as the definition ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]), and every tensor computation below uses it:

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14]]

![[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^der-cb-0-14]]

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
> The last operator is the d'Alembertian (names in other sources: [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-8|Caution: Names for the d'Alembertian]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4, eqs. (fourvector), (lowerindex), (pq), (psquared); Ch. 2 §2.3, eqs. (partial), (box) · PHY 513 Lecture 1, Part C ("Index Gymnastics") · Yu §1.3, eqs. (1.18)–(1.23); §1.4, eqs. (1.89), (1.93)*

^def-c1a-5-1

> [!caution] Caution: Names for the d'Alembertian
> These notes write $\partial^2 \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$ everywhere, as Peskin–Schroeder (eq. (2.56)) and Yu do. Lecture 2 introduces both names, $\partial_\mu\partial^\mu = \partial^2 \equiv \Box$ (slide "Klein Gordon Equation"), and the user's PHY 513 notes write $\Box$ in Ch. 2–4 and $\partial^2$ from Ch. 5 on; earlier drafts of this chapter followed the first usage. Relativity and Electromagnetism level C write $\Box = \partial_\mu\partial^\mu$, with $c$ restored ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-7|REL Theorem §B2.2.7]]); Griffiths and Electromagnetism level B write $\Box^2 = \nabla^2 - \frac{1}{c^2}\partial_t^2$ ([[§B11.1★ Potentials, Gauges and Retarded Potentials#^def-b11-1-1|EM Def. §B11.1.1]]), the opposite sign: $\partial^2 = -\Box^2$ at $c = 1$.
>
> *Source: Lecture 2, slide "Klein Gordon Equation" · the user's PHY 513 notes, Ch. 2 §2.3, eq. (box), Ch. 6 · PS §2.4, eq. (2.56) · Yu §1.4*

^cau-c1a-5-8

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
> - $t \le 0$ in the physical region of elastic scattering: the exchanged momentum $q$ is spacelike, so an exchanged particle is off its mass shell (QFT C7, planned).
> - Part 2 needs no frame change at all: one invariant evaluated in the most convenient frame (Remark below).

^der-c1a-5-1

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]

> [!remark] Remark: Compute invariants, not transformations
> Rather than transforming a quantity between frames, find an invariant that contains it, evaluate it in whichever frame is easiest, and read off the answer in the frame of interest. For a projectile on a fixed target, $s$ evaluated in the laboratory and in the centre-of-mass frame gives $E_{\rm cm}^2 = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$ ([[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]] with $c = 1$): at high energy $E_{\rm cm} \simeq \sqrt{2m_2E_{\rm lab}}$ grows only as the square root of the beam energy, while two colliding beams give $E_{\rm cm} = 2E_{\rm beam}$. That is why high-energy physics uses colliders. For $e^+e^- \to \gamma\gamma$ on an electron at rest, $E_{\rm cm} = \sqrt{2m_e(E + m_e)}$, each photon carrying $E_{\rm cm}/2$; restoring $c$ is [[P4 Restoring ħ and c|P4]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.4 (Derivation "Invariants in practice: centre-of-mass energy (Problem Set 1)", Principle "Strategy: compute invariants") · PHY 513 Lecture 1, Part C · PHY 513, Problem Set 1, Problems 4–5*

^rem-c1a-5-1

## Tensors as multilinear maps

The dual space, tensors as multilinear maps and the transformation law they force are in the block above ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-9|Def. §CB.0.9]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]). What field theory adds is the metric, which identifies the two kinds of slot:

> [!theorem] Theorem §C1a.5.2: The Metric Identifies Vectors with Covectors
> The metric $g(x, y) = g_{\mu\nu}x^\mu y^\nu$ is a symmetric, nondegenerate, indefinite bilinear form. The map $x \mapsto x^\flat = g(x, \cdot\,)$ is an isomorphism $V \to V^*$, with components and inverse
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
> - In differential geometry this is the musical isomorphism of a pseudo-Riemannian metric on one tangent space ([[§32 The Cotangent Space#^def-32-1|591 Def. §32.1]]).

^der-c1a-5-2

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-7|Def. §CB.0.7]], [[§B1.1 The Metric and Index Notation#^thm-b1-1-1|REL Theorem §B1.1.1]], [[§B1.1 The Metric and Index Notation#^thm-b1-1-2|REL Theorem §B1.1.2]], [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]

> [!caution] Caution: A tensor is not a product of vectors
> The law is exhibited on products $p^\mu q^\nu$, but a general two-tensor is a *sum* of such products: a product has rank one as a $4\times4$ matrix, a general $T^{\mu\nu}$ rank up to four. The field-strength tensor of electromagnetism is not a product ([[§C1a.7 Relativistic Electrodynamics in Index Form|§C1a.7]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Caution "A tensor is not a product of vectors") · PHY 513 Lecture 1, Part C ("Tensors")*

^cau-c1a-5-4

### The mathematics used here: invariant tensors

The metric and the Levi-Civita symbol are invariant tensors, $\varepsilon$ only up to $\det\Lambda$ (the law recalled below and Theorem §C1a.5.4):

![[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-14]]

![[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^pf-cb-8-14]]

## The Levi-Civita symbol

> [!caution] Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder
> These notes, the course (Problem Set 1), Yu (1.104) and Relativity level B ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]]) use $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$; Peskin–Schroeder use $\varepsilon^{0123} = -1$. Every quantity containing one $\varepsilon$ changes sign between the two: the dual field tensor $\tilde F^{\mu\nu}$, and $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$ here, $+8\,\mathbf E\cdot\mathbf B$ in Peskin–Schroeder ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]). Products of two $\varepsilon$'s do not. Check the convention of a source before comparing any pseudoscalar sign. Lowering all four indices always costs $\det g = -1$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Definition "The Levi-Civita symbol, and the convention of these notes") · PHY 513, Problem Set 1, Problem 3 · Yu §1.5, eq. (1.104)*

^cau-c1a-5-5

Its transformation law, $\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,\varepsilon^{\alpha\beta\gamma\delta} = (\det\Lambda)\,\varepsilon^{\mu\nu\rho\sigma}$, invariant under $\det\Lambda = +1$ and odd under $\mathcal P$ and $\mathcal T$ separately (a pseudotensor), is [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]].

> [!theorem] Theorem §C1a.5.3: Contraction Identities of the Levi-Civita Symbol
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

^thm-c1a-5-3

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
> - Used next: duality squares to $-1$ (Theorem §C1a.5.6); the invariants of the field tensor ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]); the three-dimensional identity is the tool behind the vector-calculus product rules of [[§B1.1 Fields, Integral Theorems and Curvilinear Coordinates#^thm-b1-1-1|EM Theorem §B1.1.1]].

^der-c1a-5-3

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-2|REL Def. §B2.2.2]], [[§37 Determinants#^ladr-9-45|LADR Thm. 9.45]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]

> [!theorem] Theorem §C1a.5.4: The Levi-Civita Symbol and the Determinant
> For every $4\times4$ matrix $A^\mu{}_\nu$:
> 1. $\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$;
> 2. $\det A = -\dfrac{1}{4!}\,\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta$;
> 3. if $\det A \ne 0$, $\ (A^{-1})^\nu{}_\mu = -\dfrac{1}{3!\,\det A}\,\varepsilon_{\mu\mu_2\mu_3\mu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4}A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4}$;
> 4. for four vectors, $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = -\det[a|b|c|d]$ (the matrix with columns $a^\mu, \dots, d^\mu$), which vanishes if and only if $a, b, c, d$ are linearly dependent.
>
> In Euclidean signature the minus signs in 2–4 are absent.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Levi-Civita and determinants"), eq. (epsdet) · Yu §1.5, eqs. (1.107)–(1.110)*

^thm-c1a-5-4

> [!derivation]- Derivation
> **1. Part 1.** Call the left side $L_{\alpha\beta\gamma\delta}$. Exchanging two of its free indices, say $\alpha \leftrightarrow \beta$, and renaming the dummies $\mu \leftrightarrow \nu$ gives back $L$ with $\varepsilon_{\nu\mu\rho\sigma} = -\varepsilon_{\mu\nu\rho\sigma}$: $L$ is totally antisymmetric, hence $L_{\alpha\beta\gamma\delta} = L_{0123}\,\varepsilon_{\alpha\beta\gamma\delta}/\varepsilon_{0123}$. And $L_{0123} = \varepsilon_{\mu\nu\rho\sigma}A^\mu{}_0A^\nu{}_1A^\rho{}_2A^\sigma{}_3 = \varepsilon_{0123}\sum_\pi\operatorname{sgn}\pi\,A^{\pi(0)}{}_0\cdots A^{\pi(3)}{}_3 = \varepsilon_{0123}\det A$ by the Leibniz formula ([[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]]). So $L_{\alpha\beta\gamma\delta} = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$. (For $A = \Lambda$ this is the pseudotensor law of [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]].)
>
> **2. Part 2.** Contract part 1 with $\varepsilon^{\alpha\beta\gamma\delta}$ and use $\varepsilon_{\alpha\beta\gamma\delta}\varepsilon^{\alpha\beta\gamma\delta} = -24$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]]): $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\alpha\beta\gamma\delta}A^\mu{}_\alpha\cdots = -24\det A$.
>
> **3. Part 3.** Call the right side $B^\nu{}_\mu$ and compute $B^\nu{}_\mu A^\mu{}_\lambda$. By part 1 with the first slot filled by $A^\mu{}_\lambda$: $\varepsilon_{\mu\mu_2\mu_3\mu_4}A^\mu{}_\lambda A^{\mu_2}{}_{\nu_2}A^{\mu_3}{}_{\nu_3}A^{\mu_4}{}_{\nu_4} = \det A\,\varepsilon_{\lambda\nu_2\nu_3\nu_4}$. Then $B^\nu{}_\mu A^\mu{}_\lambda = -\frac{1}{3!}\varepsilon_{\lambda\nu_2\nu_3\nu_4}\varepsilon^{\nu\nu_2\nu_3\nu_4} = -\frac{1}{6}(-6\,\delta^\nu_\lambda) = \delta^\nu_\lambda$ by Theorem §C1a.5.3. A left inverse of a square matrix is the inverse.
>
> **4. Part 4.** Put $A = [a|b|c|d]$, $A^\mu{}_0 = a^\mu$ etc., and $(\alpha\beta\gamma\delta) = (0123)$ in part 1: $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = \varepsilon_{0123}\det A = -\det A$. It vanishes iff $\det A = 0$ iff the columns are dependent ([[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]]). ⚑ By-product: with all indices raised on $\varepsilon$ and lowered on the vectors the same number results, $\varepsilon^{\mu\nu\rho\sigma}a_\mu b_\nu c_\rho d_\sigma = \det[a_\mu|\cdots] = \det g\,\det[a|\cdots] = -\det[a|b|c|d]$: the signed four-volume of the parallelepiped spanned by $a, b, c, d$ is $-\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma$ in this convention. (The user's PHY 513 notes, Ch. 1 §1.5, item 3, write it without the minus sign; checked numerically.)
>
> **What the derivation shows**
> - $\varepsilon$ is the antisymmetrizer, and the determinant is what antisymmetrizing a product of rows produces; the Minkowski minus signs are all $\varepsilon_{0123} = \det g$.
> - The cofactor formula is the same identity read backwards; it never needs Gaussian elimination.
> - Used next: Example §C1a.5.1; a pseudoscalar built from momenta needs four linearly independent ones, hence at least five particles in a process (with momentum conservation).

^der-c1a-5-4

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], [[§37 Determinants#^ladr-9-46|LADR Thm. 9.46]], [[§37 Determinants#^ladr-9-50|LADR Thm. 9.50]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]]

> [!example] Example §C1a.5.1: Momentum Conservation Kills ε p₁p₂p₃p₄
> For four momenta with $\sum_{i=1}^4 p_i = 0$, $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = 0$: by [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 4, it is $\pm$ the determinant with columns $p_1, \dots, p_4$, and adding the first three columns to the fourth produces the zero column. The contraction is a pseudoscalar, invariant only under $\det\Lambda = +1$; it can appear in an amplitude only when five or more momenta are involved. (For the course: $\varepsilon^{0123} = +1$, $\varepsilon^{1230} = -1$, three transpositions, and $\varepsilon^{1213} = 0$.)
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Levi-Civita and determinants", physical instance) · PHY 513, Problem Set 1, Problem 3*

^ex-c1a-5-1

> [!remark] Remark: What the cross product is
> In three dimensions $\varepsilon_{ijk}$ converts an antisymmetric two-index object into a one-index one, $(\mathbf a\times\mathbf b)_i = \frac12\varepsilon_{ijk}(a_jb_k - a_kb_j)$, with inverse $a_jb_k - a_kb_j = \varepsilon_{jki}(\mathbf a\times\mathbf b)_i$. This works only because an antisymmetric $3\times3$ matrix has three entries, the number of a vector's components: the antisymmetric tensor is the fundamental object and the vector its three-dimensional shorthand, which is why cross products and curls are axial (they carry a hidden $\varepsilon$). In four dimensions an antisymmetric two-tensor has six components, there is no cross product of two four-vectors, and the curl survives as the antisymmetrized derivative $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ with no $\varepsilon$ at all; the four-dimensional $\varepsilon$ acts one level up, trading one antisymmetric tensor for another (duality, Theorem §C1a.5.6), and $\nabla\cdot(\nabla\times\mathbf A) = 0$ becomes the Bianchi identity $\partial_\mu\tilde F^{\mu\nu} = 0$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]]).
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

### The mathematics used here: decomposing a two-tensor

Theorem §C1a.5.5 splits a two-tensor into pieces that no Lorentz transformation mixes: the symmetric and antisymmetric parts are subrepresentations, and irreducible means, as in Def. §CB.3.7, having no smaller invariant subspace:

![[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13]]

![[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^pf-cb-8-13]]

![[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-7]]

That the pieces are irreducible, and that the antisymmetric part splits over $\mathbb C$ into the two eigenspaces of duality of Theorem §C1a.5.6, is the representation theory of two-index tensors and two-forms:

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-12]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^der-cb-18-12]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-11]]

![[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^pf-cb-18-11]]

## Decomposing a two-tensor; duality

> [!theorem] Theorem §C1a.5.5: The Trace, Symmetric and Antisymmetric Parts Do Not Mix
> Every two-tensor splits uniquely as
>
> $$
> T^{\mu\nu} = \underbrace{\Bigl(T^{(\mu\nu)} - \tfrac14g^{\mu\nu}T^\rho{}_\rho\Bigr)}_{\text{symmetric traceless: }9} + \underbrace{T^{[\mu\nu]}}_{\text{antisymmetric: }6} + \underbrace{\tfrac14g^{\mu\nu}T^\rho{}_\rho}_{\text{trace: }1},
> $$
>
> $T^{(\mu\nu)} = \frac12(T^{\mu\nu} + T^{\nu\mu})$, $T^{[\mu\nu]} = \frac12(T^{\mu\nu} - T^{\nu\mu})$, and each of the three subspaces is mapped into itself by every Lorentz transformation. (That each is irreducible under $SO^+(1,3)$ over $\mathbb R$ is representation theory, [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-12|Theorem §CB.18.12]], irreducible in the sense of [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-7|Def. §CB.3.7]].)
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 ("Irreducible pieces of a two-tensor"), eq. (decomposition) · PHY 513 Lecture 1, Part C ("Irreducible parts of two-tensor representation")*

^thm-c1a-5-5

> [!derivation]- Derivation
> **1. Symmetric and antisymmetric.** The split $T = T^{(\,)} + T^{[\,]}$ is unique, and a symmetric (antisymmetric) tensor stays so under every $\Lambda$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 1): exchanging $\mu \leftrightarrow \nu$ in $\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma}$ is the same as exchanging the dummies $\rho \leftrightarrow \sigma$.
>
> **2. The trace is a scalar.** $g_{\mu\nu}T'^{\mu\nu} = g_{\mu\nu}\Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma T^{\rho\sigma} = g_{\rho\sigma}T^{\rho\sigma}$ by the defining condition ([[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]); only the symmetric part contributes to it, $g_{\mu\nu}T^{[\mu\nu]} = 0$ (symmetric times antisymmetric, [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2).
>
> **3. Split off the trace.** Write $t = T^\rho{}_\rho$ and $S^{\mu\nu} = T^{(\mu\nu)} - \frac14g^{\mu\nu}t$. Then $g_{\mu\nu}S^{\mu\nu} = t - \frac14\cdot4\,t = 0$, using $g_{\mu\nu}g^{\mu\nu} = 4$. The trace part $\frac14g^{\mu\nu}t$ transforms to $\frac14g^{\mu\nu}t$ (the metric is invariant, [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]]; $t$ is a scalar by step 2). A traceless symmetric tensor stays symmetric (step 1) and traceless (step 2). Uniqueness: the trace part is fixed by $t$, the rest by step 1.
>
> **4. Count.** Symmetric: $4 + 6 = 10$ entries, minus one trace condition: $9$; antisymmetric: $6$; trace: $1$; total $16$.
>
> **What the derivation shows**
> - The $16\times16$ matrix $\Lambda^\mu{}_\lambda\Lambda^\nu{}_\sigma$ is block diagonal in this basis: the lecture's "symmetric and antisymmetric parts do not mix".
> - Six antisymmetric components are exactly $\mathbf E$ and $\mathbf B$; nine symmetric traceless ones, a traceless stress tensor of a scale-invariant theory.
> - Used next: the antisymmetric block splits further over $\mathbb C$ (Theorem §C1a.5.6).

^der-c1a-5-5

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]]

> [!theorem] Theorem §C1a.5.6: Duality Squares to −1 on Antisymmetric Tensors
> On antisymmetric $A^{\mu\nu}$ let $(\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}A_{\rho\sigma}$. Then:
> 1. $\star\star A = -A$;
> 2. $\star(\Lambda A) = (\det\Lambda)\,\Lambda(\star A)$: duality commutes with proper Lorentz transformations and anticommutes with $\mathcal P$ and $\mathcal T$;
> 3. over $\mathbb C$, the six-dimensional space is the direct sum of the eigenspaces $\star A = \pm iA$, each three-dimensional and mapped into itself by every $\Lambda$ with $\det\Lambda = 1$; $\mathcal P$ exchanges them.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.5 (Derivation "Contracting Levi-Civita symbols", four-dimensional example; "Irreducible pieces of a two-tensor")*

^thm-c1a-5-6

> [!derivation]- Derivation
> **1. Lower the dual.** $(\star A)_{\rho\sigma} = g_{\rho\kappa}g_{\sigma\lambda}\frac12\varepsilon^{\kappa\lambda\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma}{}^{\alpha\beta}A_{\alpha\beta} = \frac12\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$ (seesaw on the pair $\alpha\beta$, [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|Caution: A contraction is a plain sum]]).
>
> **2. Apply twice.** $(\star\star A)^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}(\star A)_{\rho\sigma} = \frac14\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}$.
>
> **3. Bring the contracted pair to the front.** $\varepsilon^{\mu\nu\rho\sigma} = \varepsilon^{\rho\sigma\mu\nu}$: the permutation $(\mu\nu\rho\sigma) \to (\rho\sigma\mu\nu)$ is the product of the transpositions of the first with the third slot and the second with the fourth, even.
>
> **4. Contract.** By [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]] (two contracted pairs, upper and lower roles exchanged, which is the same identity), $\varepsilon^{\rho\sigma\mu\nu}\varepsilon_{\rho\sigma\alpha\beta} = -2(\delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha)$. So $(\star\star A)^{\mu\nu} = -\frac12(A^{\mu\nu} - A^{\nu\mu}) = -A^{\mu\nu}$, by antisymmetry. ⚑ By-product: the $-1$ is $\det g$ again; in Euclidean four dimensions $\star\star = +1$ and the eigenvalues are real (self-dual and anti-self-dual forms) → part 3.
>
> **5. Part 2.** Multiply the pseudotensor law $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\Lambda^\rho{}_\alpha\Lambda^\sigma{}_\beta\varepsilon^{\kappa\lambda\alpha\beta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]]) by $\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$ and use $\Lambda^\rho{}_\alpha\Lambda_\rho{}^\gamma = \delta_\alpha{}^\gamma$: $\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\varepsilon^{\kappa\lambda\gamma\delta} = \det\Lambda\,\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta$. With $(\Lambda A)_{\rho\sigma} = \Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta}$ and $(\det\Lambda)^2 = 1$:
>
> $$
> (\star\Lambda A)^{\mu\nu} = \tfrac12\varepsilon^{\mu\nu\rho\sigma}\Lambda_\rho{}^\gamma\Lambda_\sigma{}^\delta A_{\gamma\delta} = \det\Lambda\;\Lambda^\mu{}_\kappa\Lambda^\nu{}_\lambda\,\tfrac12\varepsilon^{\kappa\lambda\gamma\delta}A_{\gamma\delta} = \det\Lambda\;(\Lambda\star A)^{\mu\nu} .
> $$
>
> **6. Part 3.** $\star$ is a real linear map with $\star^2 = -1$, so over $\mathbb C$ its eigenvalues are $\pm i$ and $A = \frac12(A - i\star A) + \frac12(A + i\star A)$ splits $A$ into a $(+i)$- and a $(-i)$-eigenvector (check: $\star(A - i\star A) = \star A + iA = i(A - i\star A)$). Complex conjugation commutes with the real map $\star$ and exchanges the two eigenspaces, so they have equal dimension, $6/2 = 3$. A $\Lambda$ with $\det\Lambda = 1$ commutes with $\star$ (part 2), hence preserves each eigenspace; $\mathcal P$ anticommutes, hence sends $\star A = iA$ to $\star(\mathcal PA) = -i\mathcal PA$.
>
> **What the derivation shows**
> - Taking the dual twice returns $-A$, not $A$: the Minkowski sign. For the field tensor, $\tilde{\tilde F} = -F$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]).
> - The two three-dimensional halves are, for $F$, built from $\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]); as representations they are called $(1, 0)$ and $(0, 1)$, with $\mathbf E - i\mathbf B$ the $(1, 0)$ half in these conventions ([[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]]).

^der-c1a-5-6

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]], [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|Caution: A contraction is a plain sum; the signs live in the components]]

## Calculus with indices

> [!theorem] Theorem §C1a.5.7: Basic Derivative Identities
>
> $$
> \partial_\mu x^\nu = \delta^\nu{}_\mu, \qquad \partial^\mu x^\nu = g^{\mu\nu}, \qquad \partial_\mu x^\mu = 4, \qquad \partial_\mu(x^2) = 2x_\mu, \qquad \partial_\mu\partial_\nu(x^2) = 2g_{\mu\nu},
> $$
>
> and for a plane wave with $k\cdot x = \omega t - \mathbf k\cdot\mathbf x$,
>
> $$
> \partial_\mu e^{-ik\cdot x} = -ik_\mu\,e^{-ik\cdot x}, \qquad \partial^\mu e^{-ik\cdot x} = -ik^\mu\,e^{-ik\cdot x}, \qquad \partial^2\,e^{-ik\cdot x} = -k^2\,e^{-ik\cdot x} :
> $$
>
> the derivative pulls down the *lower*-index momentum $k_\mu = (\omega, -\mathbf k)$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3, eqs. (dxsquared), (partialtransform); Derivation "Differentiating with respect to any four-vector" ("Plane waves") · Yu §1.4, eq. (1.90)*

^thm-c1a-5-7

> [!derivation]- Derivation
> **1. Coordinates.** The $x^\nu$ are independent variables: $\partial x^\nu/\partial x^\mu$ is $1$ for $\nu = \mu$ and $0$ otherwise, $\delta^\nu{}_\mu$. Raising, $\partial^\mu x^\nu = g^{\mu\rho}\delta^\nu{}_\rho = g^{\mu\nu}$; contracting, $\delta^\mu{}_\mu = 1 + 1 + 1 + 1 = 4$, no signs (a plain sum).
>
> **2. The square.** $x^2 = g_{\alpha\beta}x^\alpha x^\beta$, so by the product rule $\partial_\mu(x^2) = g_{\alpha\beta}(\delta^\alpha{}_\mu x^\beta + x^\alpha\delta^\beta{}_\mu) = g_{\mu\beta}x^\beta + g_{\alpha\mu}x^\alpha = 2x_\mu$. In components: $\partial_\mu(t^2 - \mathbf x^2) = (2t, -2\mathbf x) = 2x_\mu$, the signs of the lower-index vector appearing by themselves. Once more: $\partial_\nu(2x_\mu) = 2g_{\mu\alpha}\delta^\alpha{}_\nu = 2g_{\mu\nu}$.
>
> **3. Plane wave.** $\partial_\mu(k_\alpha x^\alpha) = k_\alpha\delta^\alpha{}_\mu = k_\mu$ (constant $k$), and the chain rule gives $\partial_\mu e^{-ik\cdot x} = -ik_\mu e^{-ik\cdot x}$; raising, $-ik^\mu$; then $\partial_\mu\partial^\mu e^{-ik\cdot x} = (-ik_\mu)(-ik^\mu)e^{-ik\cdot x} = -k^2e^{-ik\cdot x}$.
>
> **What the derivation shows**
> - Index placement is self-consistent: "an upper index in the denominator counts as a lower index", and both sides of each identity carry the same free indices.
> - *Sense of the plane-wave rule in field theory.* For a single plane wave the identities hold pointwise. Under a Fourier integral, $f(x) = \int\frac{d^4k}{(2\pi)^4}\tilde f(k)e^{-ik\cdot x}$, the statement $\partial_\mu \leftrightarrow -ik_\mu$ is the derivative rule of the Fourier transform, an identity in $\mathcal S$ and, by duality, in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]); this is how $(\partial^2 + m^2) \to m^2 - k^2$ turns the Klein–Gordon equation into algebra.
> - Used next: Theorem §C1a.5.8; the Heisenberg field and the Wightman function ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], step 1).

^der-c1a-5-7

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-1|Def. §C1a.5.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]

> [!caution] Caution: The Hessian is not the wave operator
> - $\partial_\mu\partial_\nu f$ is the four-dimensional Hessian: a symmetric $(0,2)$ tensor with two free indices, not a scalar; it needs something to contract with.
> - $\partial_\mu\partial^\mu f = g^{\mu\nu}\partial_\mu\partial_\nu f = (\partial_t^2 - \nabla^2)f$ is its trace with the metric: the one invariant operator, $\partial^2$.
> - $\sum_\mu\partial_\mu\partial_\mu f = (\partial_t^2 + \nabla^2)f$, the trace without the metric, is not a tensor expression and never occurs; two lower indices summed is the error the notation exists to expose.
>
> Contracted with anything antisymmetric the Hessian vanishes, $\partial_\mu\partial_\nu F^{\mu\nu} = 0$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2): that one line is why $\partial_\mu F^{\mu\nu} = J^\nu$ forces $\partial_\nu J^\nu = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Caution "The Hessian is not the wave operator")*

^cau-c1a-5-7

> [!theorem] Theorem §C1a.5.8: The d'Alembertian of a Function of x²
> Let $\rho = x^2$ and $f$ twice differentiable on an interval of $\rho$ values. Where $\rho$ lies in that interval,
>
> $$
> \partial_\mu f(\rho) = 2x_\mu f'(\rho), \qquad \partial^2 f(\rho) = 8f'(\rho) + 4\rho f''(\rho) \quad\bigl(\text{in } d \text{ spacetime dimensions: } 2d\,f' + 4\rho f''\bigr),
> $$
>
> so $\partial^2\rho = 8$, $\partial^2\rho^2 = 24\rho$, $x^\mu\partial_\mu f = 2\rho f'$. The functions of $\rho$ alone with $\partial^2 f = 0$ on $\rho > 0$ or on $\rho < 0$ are $f = c_1/\rho + c_2$; in particular $\partial^2(1/x^2) = 0$ wherever $x^2 \ne 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Derivatives of functions of x² (Problem Set 1)"), eq. (boxf) · PHY 513, Problem Set 1, Problem 6*

^thm-c1a-5-8

> [!derivation]- Derivation
> **1. First derivative.** Chain rule with [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]: $\partial_\mu f(\rho) = f'(\rho)\,\partial_\mu\rho = 2x_\mu f'(\rho)$.
>
> **2. Second derivative.** $\partial^2 f = \partial^\mu(2x_\mu f') = 2(\partial^\mu x_\mu)f' + 2x_\mu\,\partial^\mu f'$. The first term: $\partial^\mu x_\mu = \delta^\mu{}_\mu = d$ ($= 4$). The second: $\partial^\mu f'(\rho) = 2x^\mu f''(\rho)$ by step 1 applied to $f'$, so $2x_\mu\cdot2x^\mu f'' = 4\rho f''$. Total: $2d\,f' + 4\rho f''$.
>
> **3. Checks.** $f = \rho$: $f' = 1$, $f'' = 0$, $\partial^2\rho = 8$. $f = \rho^2$: $8\cdot2\rho + 4\rho\cdot2 = 24\rho$, and then $(\partial^2)^2\rho^2 = 24\cdot8 = 192$. $x^\mu\partial_\mu f = x^\mu2x_\mu f' = 2\rho f'$.
>
> **4. Harmonic functions of $\rho$.** $\partial^2 f = 0$ reads $4\rho f'' = -8f'$, i.e. $(f')'/f' = -2/\rho$ where $f' \ne 0$, so $f' = c\,\rho^{-2}$ and $f = c_1/\rho + c_2$ (with $c_1 = -c$); in $d$ dimensions $f' \propto \rho^{-d/2}$, $f \propto \rho^{1 - d/2}$. Directly: $f = 1/\rho$ has $f' = -\rho^{-2}$, $f'' = 2\rho^{-3}$, and $8(-\rho^{-2}) + 4\rho(2\rho^{-3}) = 0$. ⚑ By-product: the computation holds only where $\rho \ne 0$; on the light cone $1/x^2$ is not even locally integrable → Remark below, and [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]].
>
> **What the derivation shows**
> - The dimension enters only through $\partial^\mu x_\mu = d$.
> - $1/x^2$ is the massless two-point function up to a constant; that it is harmonic off the cone is the massless Klein–Gordon equation for it there ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1|Theorem §C2b.3.1]], $m = 0$).
> - Used next: the distributional statement on all of $\mathbb R^4$ (Remark below).

^der-c1a-5-8

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]]

> [!remark] Remark: In what sense 1/x² is harmonic, and where the source sits
> Theorem §C1a.5.8 is a pointwise statement off the cone $x^2 = 0$. Across the cone $1/x^2$ behaves like $1/u$ near $u = 0$, is not locally integrable, and defines no distribution by itself. Distributions are obtained only as boundary values of the analytic function $1/(z^2 - \mathbf x^2)$, $z = t - i\varepsilon$ or $t(1 - i\varepsilon)$ ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-1|Theorem §CA.6.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-4|Theorem §CA.6.4]]), and different boundary values satisfy different equations on all of $\mathbb R^4$: the Wightman boundary value $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0\,x^0}$, the massless $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]), solves $\partial^2 D_W = 0$ in $\mathcal S'$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]); the Feynman boundary value $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0}$, the massless $D_F$ ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]]), solves $\partial^2 D_F = -i\delta^4(x)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]). The pointwise computation cannot tell them apart; the source of the Green's function sits at the tip $x = 0$ of the cone, invisible to a calculation done where $x^2 \ne 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Derivatives of functions of x²", last paragraph) · the distributional statement assembled here from §C2b.2–§C2b.7*

^rem-c1a-5-3

> [!theorem] Theorem §C1a.5.9: Taylor Expansion in Index Notation
> 1. If $f$ is real-analytic at $x$, then for small $a$
>
> $$
> f(x + a) = \sum_{n=0}^\infty\frac{1}{n!}\,a^{\nu_1}\cdots a^{\nu_n}\,\partial_{\nu_1}\cdots\partial_{\nu_n}f(x) \equiv e^{a\cdot\partial}f(x), \qquad a\cdot\partial = a^\nu\partial_\nu ;
> $$
>
> for $f \in C^{N+1}$ the sum to $n = N$ holds with remainder $O(|a|^{N+1})$.
> 2. Grouping the $n!/(k_0!\cdots k_3!)$ ordered index strings with $k_\nu$ copies of $\nu$ gives the multi-index form $\sum_{k}\frac{(a^0)^{k_0}\cdots(a^3)^{k_3}}{k_0!\cdots k_3!}\partial_0^{k_0}\cdots\partial_3^{k_3}f$.
> 3. On a plane wave the series is exact for all $a$: $e^{a\cdot\partial}e^{-ik\cdot x} = e^{-ik\cdot a}e^{-ik\cdot x}$. With $\hat p_\mu = i\partial_\mu$ (so $\hat p^0 = i\partial_t$ and $\hat p^j = -i\partial_j$, Quantum Mechanics' $-i\nabla$), $e^{a\cdot\partial} = e^{-ia\cdot\hat p}$: $a\cdot\partial$ generates translations.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Taylor expansion in index notation"), eqs. (taylorindex), (taylormulti)*

^thm-c1a-5-9

> [!derivation]- Derivation
> **1. Reduce to one variable.** Let $g(s) = f(x + sa)$. By the chain rule $g'(s) = a^\nu\partial_\nu f(x + sa)$, and by induction $g^{(n)}(s) = a^{\nu_1}\cdots a^{\nu_n}\partial_{\nu_1}\cdots\partial_{\nu_n}f(x + sa)$: each derivative in $s$ brings down one more $a^\nu\partial_\nu$.
>
> **2. Taylor in $s$.** Taylor's theorem for $g$ at $s = 0$, evaluated at $s = 1$ ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]; equivalently [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|452 Thm. §11.2]]): $f(x + a) = \sum_{n=0}^N\frac{1}{n!}g^{(n)}(0) + R_N$ with $R_N = O(|a|^{N+1})$ for $f \in C^{N+1}$. For real-analytic $f$ the series converges to $f(x + a)$ for $|a|$ inside the radius of convergence. ⚑ By-product: for a merely smooth $f$ the infinite series need not converge to $f$; "$e^{a\cdot\partial}$" is then a statement order by order, which is all field theory uses for infinitesimal translations.
>
> **3. Multi-index form.** In $a^{\nu_1}\cdots a^{\nu_n}\partial_{\nu_1}\cdots\partial_{\nu_n}f$ the sum runs over all ordered strings $(\nu_1, \dots, \nu_n)$. Partial derivatives commute and the $a$'s are numbers, so a string with $k_\nu$ copies of each $\nu$ contributes $(a^0)^{k_0}\cdots(a^3)^{k_3}\partial_0^{k_0}\cdots\partial_3^{k_3}f$, and there are $n!/(k_0!\cdots k_3!)$ such strings. Dividing by $n!$ gives the multi-index coefficients; at second order in two variables, $\frac12a^\nu a^\rho\partial_\nu\partial_\rho f = \frac12(a^1)^2\partial_1^2f + a^1a^2\partial_1\partial_2f + \frac12(a^2)^2\partial_2^2f$, the textbook's mixed term with its factor $2$ cancelling the $\frac12$.
>
> **4. Plane waves.** By [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], $\partial_{\nu_1}\cdots\partial_{\nu_n}e^{-ik\cdot x} = (-i)^nk_{\nu_1}\cdots k_{\nu_n}e^{-ik\cdot x}$, so the $n$-th term is $\frac{1}{n!}(-ik\cdot a)^ne^{-ik\cdot x}$, and the exponential series converges for every $a$: $e^{-ik\cdot a}e^{-ik\cdot x} = e^{-ik\cdot(x + a)}$.
>
> **5. The generator.** With $\hat p_\mu = i\partial_\mu$, $a^\nu\partial_\nu = -i\,a^\nu\hat p_\nu = -i\,a\cdot\hat p$; on $e^{-ik\cdot x}$, $\hat p_\mu$ has eigenvalue $k_\mu$, so $\hat p^0 = i\partial_t$ is the energy and $\hat p^j = -i\partial_j$ the momentum. (The user's PHY 513 notes write $\hat p_\nu = -i\partial_\nu$ and $e^{ia\cdot\hat p}$; the two signs compensate, but that $\hat p$ has eigenvalue $-k_\mu$ on $e^{-ik\cdot x}$.)
>
> **What the derivation shows**
> - The bookkeeping of the multinomial coefficients is done by the dummy indices; there is no matrix-notation barrier at third order.
> - $a\cdot\partial$ is the infinitesimal translation; its Noether charge is the four-momentum ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]), and on quantum fields $[\hat\phi, \hat{\mathbf P}] = -i\nabla\hat\phi$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).
> - For a field with indices the expansion acts componentwise, $A^\mu(x + a) = A^\mu + a^\nu\partial_\nu A^\mu + \dots$: translations act alike on every field, while Lorentz transformations add a matrix on the index ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]).

^der-c1a-5-9

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]], [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|452 Thm. §11.2]]

> [!remark] Remark: Three expansions, not one
> Classical field theory uses Taylor's theorem in three different variables, and they must be kept apart: in the **coordinates**, $f(x + a) = f + a^\nu\partial_\nu f + \dots$, for spacetime symmetries (Theorem §C1a.5.9); in a **parameter** $\alpha$, $\phi'_\alpha = \phi + \alpha\,\Delta\phi + O(\alpha^2)$, which defines the generator $\Delta\phi$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]]); and in the **field**, $\mathcal L(\phi + \delta\phi, \partial\phi + \partial\delta\phi) = \mathcal L + \frac{\partial\mathcal L}{\partial\phi}\delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial_\mu\delta\phi + \dots$, the variation ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]), whose first order gives the Euler–Lagrange equation and whose second order, the kernel $(\partial^2 + m^2)\delta^4(x - y)$ for the free field (a distribution in $x$ and $y$, [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]), is the operator inverted by the propagator ([[§C2b.5 Green's Functions and Contours|§C2b.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Taylor expansion in index notation", "Three expansions, not one")*

^rem-c1a-5-4

> [!theorem] Theorem §C1a.5.10: Derivatives with Respect to a Four-Vector
> For a function of the four independent components $a^\mu$ of a four-vector:
> 1. $\partial/\partial a^\mu$ transforms as a covector and $\partial/\partial a_\mu$ as a vector: the index of the denominator flips height.
> 2. The identity map in its four index forms:
>
> $$
> \frac{\partial a^\nu}{\partial a^\mu} = \delta^\nu{}_\mu, \qquad \frac{\partial a_\nu}{\partial a_\mu} = \delta_\nu{}^\mu, \qquad \frac{\partial a_\nu}{\partial a^\mu} = g_{\mu\nu}, \qquad \frac{\partial a^\nu}{\partial a_\mu} = g^{\mu\nu} .
> $$
>
> 3. $\dfrac{\partial(a_\nu a^\nu)}{\partial a^\mu} = 2a_\mu$, $\ \dfrac{\partial(b_\nu a^\nu)}{\partial a^\mu} = b_\mu$; and for $\mathcal L = \frac12\partial_\nu\phi\,\partial^\nu\phi$, $\ \dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \partial^\mu\phi$.
>
> The components must be independent: on the mass shell $p^0$ is a function of $\mathbf p$, and $\partial/\partial p^\mu$ must be taken before the constraint is imposed.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Differentiating with respect to any four-vector"), eq. (vectorderivs) · Yu §1.4, eqs. (1.90)–(1.92)*

^thm-c1a-5-10

> [!derivation]- Derivation
> **1. Transformation.** If $a' = \Lambda a$, then $a = \Lambda^{-1}a'$ and $\partial a^\nu/\partial a'^\mu = (\Lambda^{-1})^\nu{}_\mu$; by the chain rule $\partial/\partial a'^\mu = (\Lambda^{-1})^\nu{}_\mu\,\partial/\partial a^\nu = \Lambda_\mu{}^\nu\,\partial/\partial a^\nu$, the covector law ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]]). Nothing used that $a$ is a coordinate; for $a = x$ it is [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]]. Raising gives the vector law for $\partial/\partial a_\mu$.
>
> **2. The four forms.** The first is the independence of the four $a^\mu$. The second is the same for the four $a_\mu$, which are equally independent. The third: $a_\nu = g_{\nu\rho}a^\rho$ with constant $g$, so $\partial a_\nu/\partial a^\mu = g_{\nu\rho}\delta^\rho{}_\mu = g_{\nu\mu}$. The fourth: $a^\nu = g^{\nu\rho}a_\rho$, so $\partial a^\nu/\partial a_\mu = g^{\nu\rho}\delta_\rho{}^\mu = g^{\nu\mu}$. In components the last two are $+1$ on the time entry and $-1$ on the spatial diagonal, since $a_0 = a^0$ and $a_i = -a^i$.
>
> **3. The factor of two.** $a_\nu a^\nu = g_{\nu\rho}a^\nu a^\rho$; differentiate both factors (rename before differentiating, [[§B2.2 Tensors and the Covariance Principle#^cau-b2-2-1|REL Caution: The grammar of indices, for higher rank]]): $g_{\nu\rho}(\delta^\nu{}_\mu a^\rho + a^\nu\delta^\rho{}_\mu) = a_\mu + a_\mu = 2a_\mu$, not $a_\mu$. For $b_\nu a^\nu$ only one factor depends on $a$: $b_\nu\delta^\nu{}_\mu = b_\mu$.
>
> **4. The Lagrangian.** Treat the four $\partial_\nu\phi$ as the independent variables $a_\nu$ and write $\mathcal L = \frac12g^{\nu\rho}a_\nu a_\rho$. Step 3 with all heights flipped gives $\partial\mathcal L/\partial a_\mu = \frac12\cdot2g^{\mu\rho}a_\rho = \partial^\mu\phi$. Treating $\partial_\mu\phi$ and $\partial^\mu\phi$ as independent would lose the factor $2$: they are the same four numbers up to signs.
>
> **What the derivation shows**
> - Safe procedure: choose one set of components as the variables, express everything in them with $g$, then differentiate.
> - Momentum derivatives $\partial/\partial p^\mu$ act on off-shell functions; acting on $e^{-ip\cdot x}$ they bring down $-ix_\mu$, the Fourier dual of $\partial_\mu \to -ip_\mu$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]).
> - $\partial_\mu$ acts on the argument of a field, not on a constant four-vector multiplying it: $\partial_\mu(a^\nu\phi) = a^\nu\partial_\mu\phi$ for constant $a$, with an extra $(\partial_\mu a^\nu)\phi$ if $a^\nu(x)$ is itself a field ([[§C1b.1 Fields and Their Transformation Laws|§C1b.1]]).
> - Used next: the Euler–Lagrange equations of every scalar model ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), the canonical momentum ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]).

^der-c1a-5-10

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-14|Theorem §CB.0.14]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]], [[§B2.2 Tensors and the Covariance Principle#^cau-b2-2-1|REL Caution: The grammar of indices, for higher rank]]

> [!theorem] Theorem §C1a.5.11: Derivatives with Respect to Tensor Components
> 1. For independent components, the derivative is a product of deltas, slot by slot: $\dfrac{\partial T^\alpha{}_\beta}{\partial T^\mu{}_\nu} = \delta^\alpha{}_\mu\delta_\beta{}^\nu$, $\ \dfrac{\partial(\partial_\alpha A_\beta)}{\partial(\partial_\mu A_\nu)} = \delta_\alpha{}^\mu\delta_\beta{}^\nu$.
> 2. Hence $\dfrac{\partial(T_{\alpha\beta}T^{\alpha\beta})}{\partial T_{\mu\nu}} = 2T^{\mu\nu}$, $\ \dfrac{\partial(T_{\alpha\beta}U^{\alpha\beta})}{\partial T_{\mu\nu}} = U^{\mu\nu}$, $\ \dfrac{\partial T^\alpha{}_\alpha}{\partial T_{\mu\nu}} = g^{\mu\nu}$.
> 3. For an antisymmetric $F$ only six components are independent; with $\alpha < \beta$ labelling them, $\partial F_{\mu\nu}/\partial F_{\alpha\beta} = \delta^\alpha_\mu\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\mu$. Either convention gives $\delta(F_{\alpha\beta}F^{\alpha\beta}) = 2F^{\alpha\beta}\delta F_{\alpha\beta}$.
> 4. With $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$ as a function of the sixteen independent $\partial_\mu A_\nu$,
>
> $$
> \frac{\partial(F_{\alpha\beta}F^{\alpha\beta})}{\partial(\partial_\mu A_\nu)} = 4F^{\mu\nu} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Differentiating with respect to tensor components") · PHY 513, Problem Set 2, Problem 4(a), as the user's notes record its index moves*

^thm-c1a-5-11

> [!derivation]- Derivation
> **1. Deltas.** The components are the variables; the derivative of a variable with respect to itself is $1$ and with respect to any other $0$. "$1$ if $\alpha = \mu$ and $\beta = \nu$, else $0$" is, as a function of the four indices, $\delta^\alpha{}_\mu\delta_\beta{}^\nu$ (index heights placed by the rule of [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]: the denominator's indices flip). The other pairing $\delta^\alpha{}_\nu\delta^\mu{}_\beta$ would assert that $T_{\mu\nu}$ and $T_{\nu\mu}$ are one variable.
>
> **2. Corollaries.** $T_{\alpha\beta}T^{\alpha\beta} = g^{\alpha\gamma}g^{\beta\delta}T_{\alpha\beta}T_{\gamma\delta}$; both factors respond: $g^{\alpha\gamma}g^{\beta\delta}(\delta_\alpha{}^\mu\delta_\beta{}^\nu T_{\gamma\delta} + T_{\alpha\beta}\delta_\gamma{}^\mu\delta_\delta{}^\nu) = T^{\mu\nu} + T^{\mu\nu}$. With $U$ fixed only one factor responds: $U^{\mu\nu}$. And $T^\alpha{}_\alpha = g^{\alpha\beta}T_{\alpha\beta}$ gives $g^{\mu\nu}$.
>
> **3. Antisymmetric components.** $F_{21} = -F_{12}$ is not a separate variable, so $\partial F_{21}/\partial F_{12} = -1$, which is the stated formula with $(\alpha\beta) = (12)$, $(\mu\nu) = (21)$. If instead all sixteen $F_{\alpha\beta}$ are treated as independent and summed over ordered pairs, each true variable is counted twice. Either way, under $F \to F + \delta F$ with $\delta F$ antisymmetric, $\delta(F_{\alpha\beta}F^{\alpha\beta}) = \delta F_{\alpha\beta}F^{\alpha\beta} + F_{\alpha\beta}\delta F^{\alpha\beta} = 2F^{\alpha\beta}\delta F_{\alpha\beta}$ (seesaw in the second term): the variation is the safety net, since $\delta F$ inherits the symmetry of $F$.
>
> **4. Through the potential.** $\delta F_{\alpha\beta} = \delta(\partial_\alpha A_\beta) - \delta(\partial_\beta A_\alpha)$, so
>
> $$
> \delta(F_{\alpha\beta}F^{\alpha\beta}) = 2F^{\alpha\beta}\delta(\partial_\alpha A_\beta) - 2F^{\alpha\beta}\delta(\partial_\beta A_\alpha) = 2F^{\alpha\beta}\delta(\partial_\alpha A_\beta) + 2F^{\beta\alpha}\delta(\partial_\beta A_\alpha) = 4F^{\alpha\beta}\delta(\partial_\alpha A_\beta) ,
> $$
>
> using $F^{\alpha\beta} = -F^{\beta\alpha}$ in the second term and renaming the dummies $\alpha \leftrightarrow \beta$ in it. The coefficient of the independent $\delta(\partial_\mu A_\nu)$ is $4F^{\mu\nu}$.
>
> **What the derivation shows**
> - Every kinetic term in the course is quadratic, $\frac12$ or $\frac14$ times a square, and its derivative picks up the factor $2$ of item 2.
> - Item 4 gives, for $\mathcal L = -\frac14F_{\alpha\beta}F^{\alpha\beta}$, $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -F^{\mu\nu}$: the Euler–Lagrange equation of Maxwell's theory and its canonical energy–momentum tensor use exactly this ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]]).
> - Differentiating with respect to the sixteen $\partial_\mu A_\nu$, which are genuinely independent, avoids the counting issue of item 3 altogether.

^der-c1a-5-11

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]

> [!remark]- Connections
> - The dual space, multilinear maps and their components are Linear Algebra's: a $(0,2)$ tensor is a bilinear form, whose matrix changes as $C^{\mathsf T}BC$ — [[§12 Duality#^ladr-3-110|LADR Def. 3.110]], [[§38 Tensor Products#^ladr-9-85|LADR Def. 9.85]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]]; Relativity level B reaches the same law from the component side — [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]], [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-2|REL Remark: Tensors without coordinates]].
> - $\partial_\mu$ carries a lower index because the differential of a function is a covector, the cotangent-space statement of manifold theory — [[§32 The Cotangent Space#^def-32-1|591 Def. §32.1]], [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-5|REL Remark: Why the gradient carries a lower index]].
> - The Levi-Civita symbol is the alternating form of top degree, unique up to a factor because that space is one-dimensional; that is why every totally antisymmetric four-index array is a multiple of $\varepsilon$ — [[§36 Alternating Multilinear Forms#^ladr-9-37|LADR Thm. 9.37]], [[§37 The Algebra of Differential Forms#^def-37-2|452 Def. §37.2]].
> - The three-dimensional identity $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ of Theorem §C1a.5.3 is the tool behind BAC–CAB and the product rules of vector calculus — [[§B1.1 Fields, Integral Theorems and Curvilinear Coordinates#^thm-b1-1-1|EM Theorem §B1.1.1]].
> - Duality on two-forms squares to $-1$ in Lorentzian signature and to $+1$ in Euclidean signature; the Wick rotation of [[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] trades one for the other, and the complex split $6 = 3 + 3$ becomes the real split into self-dual and anti-self-dual forms.
> - The plane-wave rule $\partial_\mu \to -ik_\mu$ is the derivative rule of the Fourier transform, valid in $\mathcal S'$; it turns every free field equation into an algebraic mass-shell condition — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]].
> - $1/x^2$, harmonic off the cone, is the massless two-point function; the source of its Green's-function boundary value sits at the tip of the cone — [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]].
> - $e^{a\cdot\partial}$ is Quantum Mechanics' translation operator $e^{-i\mathbf a\cdot\hat{\mathbf P}}$ extended to time, with $\hbar = 1$ — [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]]; on quantum fields the same translation is generated by the Hilbert-space $\hat P^\mu$, $\hat\Phi(x + a) = e^{i\hat P\cdot a}\hat\Phi(x)e^{-i\hat P\cdot a}$ — [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]].
> - Mandelstam variables return as the arguments of scattering amplitudes, with crossing exchanging $s$, $t$, $u$ (QFT C7, planned).
