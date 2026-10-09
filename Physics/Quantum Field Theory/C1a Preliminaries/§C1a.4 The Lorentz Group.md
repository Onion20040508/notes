---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1a
section: C1a.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.3 Causal Structure and the Causality of a Single Particle]] · ↑ [[· C1a Preliminaries]] · [[§C1a.5 Vectors, Tensors and Index Notation]] →

*Sources: the user's PHY 513 notes, Ch. 1 §§1.2–1.3 (and Ch. 7, Principle "Active and passive conventions") · PHY 513 Lecture 1 (Larsen), Part B · Yu Zhao-Huan, 量子场论讲义, §1.3.*

Which transformations relate the descriptions of one physical situation, and what structure does the set of them have that field theory will use? Relativity level B already defines the Lorentz group by $\Lambda^{\mathsf T}g\Lambda = g$, proves that it is a group with four pieces, writes every proper orthochronous element as a boost times a rotation, and lists the orbits ([[§B1.2 Lorentz Transformations and the Lorentz Group|REL §B1.2]], [[§B1.3 Causal Structure and Proper Time#^rem-b1-3-1|REL Remark: Normal forms, and the orbits of the Lorentz group]]); those statements are not repeated here, except that the boost-times-rotation decomposition is recalled in the active reading with the explicit boost matrix that the orbits need (Theorem §CB.2.13, 1). This section adds what quantum field theory needs on top: natural units and the *active* reading of $\Lambda$ used by Peskin–Schroeder and the lectures, the invariant volume elements, and the orbits of the group on spacetime with the action of $\mathcal P$ and $\mathcal T$ on them, which is where the light cone, positive energy and microcausality enter. The group-theoretic vocabulary (matrix groups, the four components as cosets of a normal subgroup, the identity component) is mathematics; it lives in [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] and [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]] and is shown in the block below.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$; $x^\mu = (t, \mathbf x)$; $g = \operatorname{diag}(+1, -1, -1, -1)$; $\Lambda$ read actively; rapidity $\eta$.

## The mathematics used here

The groups named throughout, $O(1,3)$, $SO(1,3)$ and $SO^+(1,3)$, as groups of matrices; that $O(1,3)$ is a group, with $\det\Lambda = \pm1$ and $|\Lambda^0{}_0| \ge 1$, is [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]] and [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]:

![[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1]]

"Lorentz invariant" refers to the identity component (Remark: What "Lorentz invariant" means in field theory), in this sense:

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-9]]

The orbit theorems use the group structure: Theorem §C1a.4.3 lets $O(1,3)$ act coset by coset, and Theorem §C1a.4.2 uses the boost $B(u)$ of the decomposition of $SO^+(1,3)$ into boosts times rotations (the model case with one label, the rotation group, is [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-11|Theorem §CB.2.11]]):

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12]]

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^der-cb-2-12]]

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13]]

![[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^der-cb-2-13]]

## Lorentz transformations in field theory

> [!definition] Definition §C1a.4.1: Lorentz Transformation, Active Reading
> A **Lorentz transformation** is a real $4\times4$ matrix $\Lambda = [\Lambda^\mu{}_\nu]$ with
>
> $$
> \Lambda^{\mathsf T}g\,\Lambda = g, \qquad g = \operatorname{diag}(1, -1, -1, -1), \qquad\text{in components}\quad g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta} .
> $$
>
> In these notes $\Lambda$ acts **actively**: one observer, and a point, field configuration or state moved from $x$ to $x' = \Lambda x$. The set of all $\Lambda$ is the Lorentz group $O(1,3)$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3, eq. (LorentzGroup), Caution "Active and passive boosts" · PHY 513 Lecture 1, Part B ("Definition of Lorentz group") · Yu §1.3, eq. (1.34)*

^def-c1a-4-1

> [!caution] Caution: Active and passive readings
> The same matrix has two readings. **Active** (Peskin–Schroeder, the lectures, these notes): the object is moved, $x \mapsto \Lambda x$, in one frame. **Passive** (Yu (1.16), [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]]): one event is described by a second observer. The passive matrix for an observer moving with velocity $+\mathbf v$ is the active matrix for velocity $-\mathbf v$, its inverse: Yu's $t' = \gamma(t - \beta x)$ is the active $t' = \gamma(t + vx)$ with $v = -\beta$. Every statement about the *group* (closure, components, orbits, generators, the algebra in terms of $\omega_{\mu\nu}$) is identical in both readings, because $\Lambda$ and $\Lambda^{-1}$ are both in it. Only formulas that name a particular velocity, angle or rapidity differ, by a sign; mixing the two readings in one calculation flips that sign ([[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-2|§C1a.7, Caution: The sign of the v × B term]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2 (Caution "Active and passive boosts"), Ch. 7 (Principle "Active and passive conventions: Peskin–Schroeder and Larsen versus Yu") · Yu §1.3, eq. (1.16)*

^cau-c1a-4-1

> [!caution] Caution: Notation against Relativity level B
> Relativity level B keeps $c$ ($x^0 = ct$), writes the metric $\eta_{\mu\nu}$, the rapidity $\varphi$, and reads $\Lambda$ passively. Here $c = 1$, the metric is $g_{\mu\nu}$ (the letter of the user's notes, Peskin–Schroeder and Yu), the rapidity is $\eta$ (the lectures' letter), and $\Lambda$ is active. To use a level-B formula: set $c = 1$, rename $\eta_{\mu\nu} \to g_{\mu\nu}$, $\varphi \to \eta$, and for a formula naming a velocity replace $\boldsymbol\beta \to -\mathbf v$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2 ("Units") · PHY 513 Lecture 1 ("always take c = 1!")*

^cau-c1a-4-2

> [!definition] Definition §C1a.4.2: Active Rotation and Boost
> The active rotation by $\theta$ about $z$ and the active boost to velocity $v$ along $z$ act on $(x, y)$ and on $(t, z)$ respectively, as the identity on the other two coordinates:
>
> $$
> R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad B_z = \gamma\begin{pmatrix} 1 & v \\ v & 1 \end{pmatrix}, \qquad \gamma = (1 - v^2)^{-1/2} .
> $$
>
> A particle at rest, $(1, \mathbf 0)$, is sent to $\gamma(1, 0, 0, v)$, moving with velocity $+v\hat{\mathbf z}$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2, eqs. (boostz), (rotboost) · PHY 513 Lecture 1, Part B*

^def-c1a-4-2

> [!definition] Definition §C1a.4.3: Rapidity
> The **rapidity** $\eta$ of the boost $B_z$ of [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]] is defined by $\tanh\eta = v$; then $\cosh\eta = \gamma$, $\sinh\eta = \gamma v$, and
>
> $$
> B_z(\eta) = \begin{pmatrix} \cosh\eta & \sinh\eta \\ \sinh\eta & \cosh\eta \end{pmatrix} ,
> $$
>
> which sends $(1, \mathbf 0)$ to $(\cosh\eta, 0, 0, \sinh\eta)$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2, eq. (rapidity) · PHY 513 Lecture 1, Part B*

^def-c1a-4-3

Both matrices satisfy Definition §C1a.4.1 by the computation of [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]] with $c = 1$ ($\cosh^2\eta - \sinh^2\eta = 1$ in place of $\gamma^2(1 - \beta^2) = 1$), and rapidities along one axis add, $B_z(\eta_1)B_z(\eta_2) = B_z(\eta_1 + \eta_2)$, which is the velocity-addition law ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-7|REL Theorem §B1.2.7]]). Both matrices are exponentials of generators ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]); written as full $4\times4$ matrices, together with the rotation about and the boost along an arbitrary unit vector, they are [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]].

> [!caution] Caution: The slides' rotation matrix is passive
> Lecture 1 writes the boost along $z$ as $B_z(\eta)$ above (active) but the rotation about $z$ with $+\sin\theta$ in the upper right, which is $R_z(-\theta)$: applied to $\hat{\mathbf x}$ it gives $(\cos\theta, -\sin\theta)$, a clockwise turn, i.e. the axes rotated by $+\theta$. Both are Lorentz transformations and no group statement is affected; but used together in one convention, the active rotation by $\theta$ is the slide's matrix with $\theta \to -\theta$. Yu's (1.36) is the same passive rotation, consistently with Yu's passive boost.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.2 (Caution "A mixed pair: the rotation matrix above is passive") · PHY 513 Lecture 1, Part B · Yu §1.3, eqs. (1.35)–(1.36)*

^cau-c1a-4-3

## The group

> [!theorem] Theorem §C1a.4.1: Invariant Volume Elements
> For every $\Lambda \in O(1,3)$ the substitutions $x' = \Lambda x$ and $p' = \Lambda p$ have Jacobian $|\det\Lambda| = 1$:
>
> $$
> d^4x' = d^4x, \qquad d^4p' = d^4p .
> $$
>
> Hence the integral over spacetime of a scalar field, $\int d^4x\,f'(x) = \int d^4x\,f(x)$ when $f'(\Lambda x) = f(x)$, is invariant, and so is $\int d^4p\,F(p)$ for a scalar function or scalar distribution $F$ (such as $\theta(p^0)\delta(p^2 - m^2)$ under orthochronous $\Lambda$). For the action this is [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]].
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (Derivation "Two consequences of ΛᵀgΛ = g")*

^thm-c1a-4-1

> [!derivation]- Derivation
> **1. The Jacobian matrix.** For the linear map $x'^\mu = \Lambda^\mu{}_\nu x^\nu$, $\partial x'^\mu/\partial x^\nu = \Lambda^\mu{}_\nu$, a constant matrix; its determinant is $\det\Lambda$.
>
> **2. The determinant.** Taking determinants of $\Lambda^{\mathsf T}g\Lambda = g$ with $\det(AB) = \det A\det B$ ([[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]]) and $\det\Lambda^{\mathsf T} = \det\Lambda$ ([[§37 Determinants#^ladr-9-56|LADR Thm. 9.56]]): $(\det\Lambda)^2\det g = \det g = -1$, so $(\det\Lambda)^2 = 1$ and $|\det\Lambda| = 1$.
>
> **3. Change of variables.** For an integrable $f$, $\int d^4x'\,f(x') = \int d^4x\,|\det\Lambda|\,f(\Lambda x) = \int d^4x\,f(\Lambda x)$ ([[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], extended from bounded regions to $\mathbb R^4$ for absolutely integrable $f$). The same with $p$ in place of $x$.
>
> **4. Scalars.** If $f$ is a scalar field, the transformed field is $f'(x') = f(x)$ at $x' = \Lambda x$ ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]]), so $\int d^4x'\,f'(x') = \int d^4x\,f'(\Lambda x) = \int d^4x\,f(x)$ by step 3; the name of the integration variable is immaterial, so $\int d^4x\,f' = \int d^4x\,f$. For distributions the substitution is the definition of the transformed distribution, $(T\circ\Lambda^{-1})[f] = T[f\circ\Lambda]$ with the factor $|\det\Lambda| = 1$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]), and "$T$ is invariant" means $T\circ\Lambda^{-1} = T$; for $\theta(p^0)\delta(p^2 - m^2)$ this holds for orthochronous $\Lambda$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1; [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]).
>
> **What the derivation shows**
> - Only $|\det\Lambda| = 1$ is used: the volume elements are invariant under all of $O(1,3)$, parity and time reversal included; an orientation (a sign of $\det\Lambda$) matters only for objects carrying an $\varepsilon$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
> - Used next: the invariance of the action ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]); the invariant measure $d^3p/2E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], step 4); every Lorentz-invariant momentum integral.

^der-c1a-4-1

*Uses:* [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]], [[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]], [[§37 Determinants#^ladr-9-56|LADR Thm. 9.56]], [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]

## Components, cosets and the identity component

The four components of $O(1,3)$ are the cosets of $SO^+(1,3)$, and $SO^+(1,3)$ is the component of the identity ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], shown in the block above; their home is [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings|§CB.2]]). In a picture:

![[ph-qft-c1-4-1.svg]]
*The four components of $O(1,3)$, labelled by $\det\Lambda$ (rows) and the sign of $\Lambda^0{}_0$ (columns); they are the cosets of $SO^+(1,3)$, and multiplying by $\mathcal P$, $\mathcal T$ or $\mathcal P\mathcal T$ moves between them as the arrows show (the figure labels the matrices $P$, $T$, i.e. $\mathcal P$, $\mathcal T$). Only the cell containing $\mathbf 1$ is a subgroup. Adapted from the user's PHY 513 notes, Ch. 1 §1.3.*

> [!remark] Remark: What "Lorentz invariant" means in field theory
> Throughout quantum field theory, "Lorentz invariant" means invariant under $SO^+(1,3)$, together with translations the proper orthochronous Poincaré group ([[§B1.2 Lorentz Transformations and the Lorentz Group#^def-b1-2-4|REL Def. §B1.2.4]]), unless parity or time reversal is named explicitly. It is the only piece reachable from the identity, so it is the only piece whose elements are exponentials of generators ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]) and the only one that Noether's theorem turns into conserved charges ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]]). $\mathcal P$ and $\mathcal T$ are discrete: whether a theory respects them is decided by its Lagrangian, and the weak interaction does not ([[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-4|§C9.4, Remark: Discrete symmetries in nature]]). The same distinction recurs three times in the course: in the invariance of past and future ([[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]]), in the invariance of positive energy on the mass shell ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]), and in the classification of fields by their response to parity ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (Definition "Names and what is a subgroup"; paragraph "Components of the group") · Yu §1.3 ("Lorentz 不变量通常指的是在固有保时向 Lorentz 变换下不变的量")*

^rem-c1a-4-1

## Orbits: where the light cone enters

The four components are a property of the group, a six-dimensional manifold. The light cone is a property of spacetime, the space the group acts on ([[§25 Actions#^def-25-1|493 Def. §25.1]]). They meet through orbits ([[§27 Orbits#^def-27-1|493 Def. §27.1]]): the orbit of $x$ is $\{\Lambda x : \Lambda \in SO^+(1,3)\}$.

> [!theorem] Theorem §C1a.4.2: The Orbits of SO⁺(1,3) on Spacetime
> Under $x \mapsto \Lambda x$, $\Lambda \in SO^+(1,3)$, the orbits in $\mathbb R^4$ are exactly
> - for each $m > 0$, the **future sheet** $H^+_m = \{x^2 = m^2,\ x^0 > 0\}$ and the **past sheet** $H^-_m = \{x^2 = m^2,\ x^0 < 0\}$;
> - for each $a > 0$, the **one-sheeted hyperboloid** $S_a = \{x^2 = -a^2\}$;
> - the **future** and **past null cones** $C^\pm = \{x^2 = 0,\ \pm x^0 > 0\}$;
> - the origin.
>
> Equivalently: $x$ and $y$ lie in one orbit if and only if $x^2 = y^2$ and, when $x^2 \ge 0$ and $x \ne 0$, $\operatorname{sgn}x^0 = \operatorname{sgn}y^0$. Normal forms: $m e_0$, $-m e_0$, $a e_3$, $\pm(e_0 + e_3)$, $0$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (paragraph "Orbits: where the light cone comes in", Figure "orbits")*

^thm-c1a-4-2

> [!derivation]- Derivation
> **1. Orbits lie in level sets.** $(\Lambda x)^2 = x^2$ for every Lorentz transformation ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]]).
>
> **2. On timelike and null vectors the sign of $x^0$ is kept.** If $x^2 \ge 0$ and $x \ne 0$, then $(x^0)^2 \ge \mathbf x^2$ forces $x^0 \ne 0$, and an orthochronous $\Lambda$ preserves $\operatorname{sgn}x^0$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], 2). With step 1, each orbit lies inside one of the listed sets; it remains to show that each set is a single orbit (the group acts transitively on it).
>
> **3. Future sheet.** Let $x \in H^+_m$ and $u = x/m$: $u^2 = 1$, $u^0 > 0$. By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], step 2, $B(u) \in SO^+(1,3)$ and $B(u)e_0 = u$, so $x = B(u)(me_0)$: every point of $H^+_m$ is in the orbit of $me_0$.
>
> **4. Past sheet.** If $x \in H^-_m$ then $-x \in H^+_m$ and $-x = B(-x/m)(me_0)$; multiply by $-1$, which commutes with every matrix: $x = B(-x/m)(-me_0)$. So $H^-_m$ is the orbit of $-me_0$.
>
> **5. Spacelike.** Let $x^2 = -a^2 < 0$, so $|\mathbf x| > |x^0|$ and $\mathbf x \ne 0$. A rotation $R$ takes $\mathbf x$ to $|\mathbf x|\hat{\mathbf z}$: $Rx = (x^0, 0, 0, |\mathbf x|)$. Choose $\eta$ with $\tanh\eta = x^0/|\mathbf x| \in (-1, 1)$, so $\cosh\eta = |\mathbf x|/\sqrt{\mathbf x^2 - (x^0)^2} = |\mathbf x|/a$. Apply $B_z(-\eta)$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]]) on the $(t, z)$ block:
>
> $$
> t' = \cosh\eta\,x^0 - \sinh\eta\,|\mathbf x| = \cosh\eta\,\bigl(x^0 - \tanh\eta\,|\mathbf x|\bigr) = 0, \qquad z' = -\sinh\eta\,x^0 + \cosh\eta\,|\mathbf x| = \cosh\eta\,\frac{\mathbf x^2 - (x^0)^2}{|\mathbf x|} = a .
> $$
>
> So $B_z(-\eta)Rx = ae_3$: all of $S_a$ is the orbit of $ae_3$.
>
> **6. Null.** Let $x = \kappa(1, \hat{\mathbf n})$, $\kappa > 0$. Rotate $\hat{\mathbf n}$ to $\hat{\mathbf z}$: $\kappa(1, 0, 0, 1)$. Then $B_z(-\eta)$ gives $t' = \kappa(\cosh\eta - \sinh\eta) = \kappa e^{-\eta}$ and $z' = \kappa(-\sinh\eta + \cosh\eta) = \kappa e^{-\eta}$; with $\eta = \ln\kappa$ the result is $e_0 + e_3$. So $C^+$ is the orbit of $e_0 + e_3$, and, multiplying by $-1$ as in step 4, $C^-$ is the orbit of $-(e_0 + e_3)$. ⚑ By-product: a null vector can be rescaled by any positive factor but never brought to rest; the stabilizers of the normal forms (rotations for $me_0$; a three-parameter group for $e_0 + e_3$) are the little groups of massive and massless particles ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-7|Theorem §C3.6.7]], [[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]]).
>
> **7. The origin** is fixed by every linear map. The sets listed are disjoint and cover $\mathbb R^4$, as orbits must ([[§27 Orbits#^prop-27-1|493 Prop. §27.1]]).
>
> **What the derivation shows**
> - $x^2$ and, off the spacelike region, $\operatorname{sgn}x^0$ are complete invariants; on $S_a$ nothing but $x^2$ survives. ⚑ By-product: $S_a$ contains both $ae_3$ and $-ae_3$, so the sign of $x^0$ is not an invariant of spacelike vectors → [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], 3.
> - Transitivity used the boosts $B(u)$ of Theorem §CB.2.13 and the rotations; the orbit $H^+_m$ is the set of four-momenta of a particle of mass $m$, with stabilizer $SO(3)$ (the rest frame is unique up to rotation).
> - Used next: Lorentz-invariant functions and distributions are constant on these orbits ([[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], step 4).

^der-c1a-4-2

*Uses:* [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-2|REL Theorem §B1.2.2]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§25 Actions#^def-25-1|493 Def. §25.1]], [[§27 Orbits#^def-27-1|493 Def. §27.1]], [[§27 Orbits#^prop-27-1|493 Prop. §27.1]]

> [!theorem] Theorem §C1a.4.3: Parity and Time Reversal Permute the Orbits
> 1. $\mathcal P$ maps every orbit of Theorem §C1a.4.2 to itself (reversing its orientation along the sheet).
> 2. $\mathcal T$ and $\mathcal P\mathcal T = -\mathbb 1$ exchange $H^+_m \leftrightarrow H^-_m$ and $C^+ \leftrightarrow C^-$, and map each $S_a$ to itself.
> 3. Consequently, on timelike and null vectors $\operatorname{sgn}x^0$ is invariant under the orthochronous transformations $SO^+(1,3)\cup \mathcal P\cdot SO^+(1,3)$; on the mass shell $p^2 = m^2$, $\theta(p^0)$ is invariant. On spacelike vectors it is not invariant even under $SO^+(1,3)$: for every $x$ with $x^2 < 0$ there is $\Lambda \in SO^+(1,3)$ with $\Lambda x = -x$.
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (paragraph "Orbits"; Caution "Where the two pictures fail to match")*

^thm-c1a-4-3

> [!derivation]- Derivation
> **1. Parity.** $\mathcal Px = (x^0, -\mathbf x)$: $(\mathcal Px)^2 = x^2$ and $(\mathcal Px)^0 = x^0$, so by the complete invariants of [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]] $\mathcal Px$ lies in the orbit of $x$. Along a sheet, $\mathcal P$ reverses $\mathbf x$, the coordinate that a boost moves.
>
> **2. Time reversal.** $\mathcal Tx = (-x^0, \mathbf x)$ and $-\mathbb 1x = -x$: both keep $x^2$ and flip $x^0$. For $x^2 \ge 0$, $x \ne 0$ this moves $x$ to the sheet or cone of the other sign. For $x^2 = -a^2$ the image has the same $x^2$, and $S_a$ is a single orbit: it is mapped to itself.
>
> **3. Every element.** By [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]], every $\Lambda \in O(1,3)$ is $CK$ with $K \in SO^+(1,3)$ and $C \in \{\mathbb 1, \mathcal P, \mathcal T, \mathcal P\mathcal T\}$; $K$ keeps each orbit, so $\Lambda$ permutes the orbits as $C$ does. For $C \in \{\mathbb 1, \mathcal P\}$ (orthochronous) no sheet or cone is exchanged: $\operatorname{sgn}x^0$ is invariant on timelike and null vectors.
>
> **4. The mass shell.** For $m > 0$, $p^2 = m^2$ forces $p^0 \ne 0$, and $\{p^2 = m^2,\ p^0 > 0\} = H^+_m$ is invariant under orthochronous $\Lambda$ by step 3. So $\theta(\Lambda p) = \theta(p)$ there: positive energy is a Lorentz-invariant statement. ⚑ By-product: the invariance holds on the shell only; for $p^2 < 0$ the sign of $p^0$ is frame dependent (step 5) → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], 1.
>
> **5. Spacelike reversal.** Let $x^2 = -a^2 < 0$. Step 5 of the derivation of Theorem §C1a.4.2 gives $\Lambda_1 = B_z(-\eta)R \in SO^+(1,3)$ with $\Lambda_1x = ae_3$. The rotation $R_x(\pi)$ by $\pi$ about the $x$ axis sends $e_3 \mapsto -e_3$. Then $\Lambda = \Lambda_1^{-1}R_x(\pi)\Lambda_1 \in SO^+(1,3)$ and $\Lambda x = \Lambda_1^{-1}R_x(\pi)(ae_3) = \Lambda_1^{-1}(-ae_3) = -\Lambda_1^{-1}(ae_3) = -x$. In particular the sign of $x^0$ flips whenever $x^0 \ne 0$.
>
> **What the derivation shows**
> - The group acts on the set of orbits through its quotient $\mathbb Z_2\times\mathbb Z_2$, with $\mathcal P$ acting trivially and $\mathcal T \equiv \mathcal P\mathcal T$ exchanging past and future.
> - "Past" and "future" are invariant because the timelike sheets are separate orbits; "earlier" is meaningless for spacelike separation because $S_a$ is one connected orbit containing $x$ and $-x$.
> - Used next: positive energy ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]); the reversal $\Lambda x = -x$ is the whole proof of microcausality of the free field ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], steps 1–3).

^der-c1a-4-3

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-12|Theorem §CB.2.12]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]]

![[ph-qft-c1-4-2.svg]]
*Orbits of the identity component in the $(x, t)$ plane, one spatial direction shown. The future (blue) and past (grey) sheets of $t^2 - x^2 = m^2$ are separate orbits; $\mathcal P$ maps each to itself, $\mathcal T$ and $\mathcal P\mathcal T$ exchange them (the figure labels them $P$, $T$, i.e. $\mathcal P$, $\mathcal T$). The spacelike hyperbola (orange, dashed) has two branches only in $1+1$ dimensions; in $3+1$ the spacelike hyperboloid is one connected orbit (Caution below). Adapted from the user's PHY 513 notes, Ch. 1 §1.3.*

> [!caution] Caution: The orbit picture depends on the dimension
> The four components of the group are the same in every dimension. The orbits are not. In $1+1$ dimensions the spacelike hyperbola $x^2 - t^2 = a^2$ has two branches, $x > 0$ and $x < 0$, which are separate $SO^+(1,1)$ orbits exchanged by $\mathcal P$; there is no rotation to carry one into the other, and $-x$ is not in the orbit of $x$. In $3+1$ dimensions (indeed for two or more space dimensions) $S_a$ is one connected orbit, because a rotation carries $(0, \mathbf x)$ to $(0, -\mathbf x)$ (Theorem §C1a.4.3, 3). So the criterion for "the sign of $x^0$ is invariant" is connectedness of the *orbit*, not of the region, and the figure, drawn in $1+1$, misleads on exactly this point. (Each branch still contains both signs of $x^0$, so the sign is undefined for spacelike vectors in every dimension.)
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 (Caution "Where the two pictures fail to match")*

^cau-c1a-4-4

> [!remark] Remark: Why the orbits matter in field theory
> - **Positive energy.** A particle's momentum lies on $H^+_m$ (or $C^+$ for $m = 0$), an orbit: "the energy is positive" survives every orthochronous change of frame, and $\theta(p^0)\delta(p^2 - m^2)\,d^4p$ is the invariant measure on it ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]).
> - **Invariant functions are functions of the orbit.** A Lorentz-invariant two-point function depends on $x^2$ and, inside the cone, on $\operatorname{sgn}x^0$ only; this is why the Wightman function needs one evaluation per orbit type ([[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]).
> - **Microcausality.** At spacelike separation $x$ and $-x$ are in one orbit, so an invariant function cannot tell them apart and the commutator $D_W(x) - D_W(-x)$ vanishes; inside the cone they are in different orbits and it need not ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]).
> - **Particles.** The orbits of momenta classify one-particle states: $H^+_m$ massive, $C^+$ massless, $S_a$ tachyonic (no stable vacuum), $p = 0$ the vacuum ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-2|Theorem §C3.6.2]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-6|Theorem §C3.6.6]], [[§C3.6★ Particle States and the Little Group#^rem-c3-6-2|§C3.6★, Remark: The orbits at a glance]]).
>
> *Source: the user's PHY 513 notes, Ch. 1 §1.3 ("the same structure recurs three times in the course")*

^rem-c1a-4-2

> [!remark]- Connections
> - The template $M^{\mathsf T}GM = G$ gives $O(N)$ for $G = \mathbb 1$, $O(1,3)$ for $G = g$, and the symplectic group for an antisymmetric $G$; the transpose is the change-of-basis rule for bilinear forms — [[§B1.2 Lorentz Transformations and the Lorentz Group|REL §B1.2]] (Connections), [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]].
> - The matrix groups of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]] are matrix Lie groups, each with a Lie algebra of generators and its structure constants — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|Def. §CB.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|Def. §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-13|Def. §CB.1.13]].
> - The homomorphism $\Lambda \mapsto (\det\Lambda, \operatorname{sgn}\Lambda^0{}_0)$ plays for $O(1,3)$ the role that $\det$ plays for $O(3)$ and $GL(n, \mathbb R)$, whose two components are its fibres — [[§16 The Classical Groups#^thm-16-2|591 Thm. §16.2]]; the sign of a permutation is the same kind of map onto $\mathbb Z_2$ — [[§21 The Sign Homomorphism and the Alternating Group|493 §21]].
> - Each future sheet is a homogeneous space, $H^+_m \cong SO^+(1,3)/SO(3)$, by orbit–stabilizer; the same construction with the stabilizer of a null vector gives the massless little group of Wigner's classification ([[§C3.7★ Massless Particles and Helicity#^thm-c3-7-1|Theorem §C3.7.1]]) — [[Homogeneous Spaces Are Coset Spaces]], [[§30 Orbit–Stabilizer|493 §30]].
> - $\theta(p^0)$ is invariant on $H^+_m$ for the same reason that "future" is invariant for timelike displacements: both are the statement that the two timelike sheets are separate orbits — [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-1|§C1a.3, Remark: Why the future cannot be boosted into the past]].
> - The invariant distributions $\theta(\pm p^0)\delta(p^2 - m^2)$ and $\theta(\pm x^0)\delta(x^2)$ are exactly the orbit measures on $H^\pm_m$ and $C^\pm$ — [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]].
> - The six parameters of $SO^+(1,3)$ and the four translations are the ten conserved charges of a relativistic field theory — [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-5|REL Remark: Ten parameters, ten conservation laws]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]].
> - The rotation subgroup acting on kets, and its double cover $SU(2)$, are Quantum Mechanics' rotation theory; the Lorentz group's own double cover $SL(2, \mathbb C)$ is the spinor story ([[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-15-9|Theorem §CB.15.9]]; [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-2|§CB.9, Remark: The same pattern for the Lorentz group]]) — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
