---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 41
tags: [differentiable-manifolds, math591]
---
← [[§40 The Unit Quaternions and SU(2)]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§42 Recap꞉ Germs, Derivations and Tangent Vectors]] →

*Stage: maps — One example that uses everything so far: submanifolds, embeddings, local diffeomorphisms, and translation in a group.*

*From Assignment 4, Problem 3: the submitted solution, reorganized, with every claim the problem allowed us to assume now proved. References: Lee, Problems 7-22 and 7-23 (quaternions).*

The unit quaternions form a group $S^3$; acting on $\mathbb{C}^2$ they identify it with $\mathrm{SU}(2)$, and acting by conjugation on the pure imaginary quaternions $\mathbb{R}^3$ they give rotations. The result is a two-to-one local diffeomorphism $\mathrm{SU}(2) \to \mathrm{SO}(3)$, and with it $\mathrm{SO}(3) \cong \mathbb{RP}^3$.

![[m591-35-1.svg]]
*The three maps of the section: $F$ identifies unit quaternions with matrices in $\mathrm{SU}(2)$ ([[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5]]); $C$ is conjugation ([[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|Proposition §41.1]]); and $G = C \circ F^{-1}$ is the double cover ([[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4]]).*

## Conjugation and Rotations

> [!theorem] Proposition §41.1: Conjugation by Unit Quaternions Is Rotation
> For $q \in S^3$, the map $C_q(v) = q v \bar q$ sends $\mathbb{H}_0 \cong \mathbb{R}^3$ to itself, and:
> 1. $C_q \in \mathrm{SO}(3)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]]), and $C : S^3 \to \mathrm{SO}(3)$, $q \mapsto C_q$, is a smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]);
> 2. $\ker C = \{\pm 1\}$ ([[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]), so $C_p = C_q$ if and only if $p = \pm q$;
> 3. if $u \in \mathbb{H}_0$ is a unit vector and $\theta \in \mathbb{R}$, then $C_q$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ is the rotation by the angle $\theta$ about the axis $u$.

^prop-41-1

> [!proof]+ Proof
> *(The problem stated (1) and the two-to-one property without proof; filled in. Part (3) contains the submitted computation: for $q = \gamma_j(t)$ it gives the rotation by $2t$ about $e_j$; the submitted computation itself is in the [[§41 SU(2) → SO(3)꞉ The Double Cover#^pf-41-4-2|second proof]] of [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4]].)* A quaternion $v$ is pure imaginary iff $\bar v = -v$, and then $\overline{q v \bar q} = q \bar v \bar q = -q v \bar q$, so $C_q(v) \in \mathbb{H}_0$; and $|C_q(v)| = |v|$ by [[§40 The Unit Quaternions and SU(2)#^prop-40-1|Proposition §40.1]]. So $C_q$ is a linear isometry of $\mathbb{R}^3$, $C_q \in \mathrm{O}(3)$.
>
> (1) $C_{pq}(v) = pq v \bar q \bar p = C_p(C_q(v))$. The entries of $C_q$ are quadratic polynomials in the coordinates of $q$, so $C$ is smooth into $\operatorname{Mat}(3, \mathbb{R})$, with values in the submanifold $\mathrm{O}(3)$ ([[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]]). $\det \circ C : S^3 \to \{\pm 1\}$ is continuous on the connected $S^3$ ([[§40 The Unit Quaternions and SU(2)#^prop-40-4|Proposition §40.4]]) and equals $1$ at $q = 1$, so $C$ takes values in $\mathrm{SO}(3)$, an open subset of $\mathrm{O}(3)$; hence $C$ is smooth into $\mathrm{SO}(3)$ ([[§35 Submanifolds#^lem-35-3|Lemma §35.3]]).
>
> (2) If $C_q = \mathrm{id}$, then $q$ commutes with $i$, $j$ and $k$. Writing $q = x_0 + x_1 i + x_2 j + x_3 k$, $qi = iq$ forces $x_2 = x_3 = 0$, and $qj = jq$ forces $x_1 = 0$; so $q = x_0$ is real, and $|q| = 1$ gives $q = \pm 1$. Conversely $C_{\pm 1} = \mathrm{id}$. Then $C_p = C_q$ iff $C_{p\bar q} = \mathrm{id}$ iff $p = \pm q$.
>
> (3) Write $c = \cos\frac\theta2$, $s = \sin\frac\theta2$. For pure imaginary $u, v$ one has $uv = -u\cdot v + u \times v$, so $u$ commutes with $q$ and $C_q(u) = u q \bar q = u$. If $v \perp u$, then $vu = -uv$, hence $v\bar q = (c + su) v = qv$, and
>
> $$
> C_q(v) = q^2 v = \big(\cos\theta + \sin\theta\, u\big) v = \cos\theta\, v + \sin\theta\, (u \times v) .
> $$
>
> That is the rotation by $\theta$ about $u$: it fixes $u$ and turns the plane $u^\perp$ through $\theta$.

^pf-41-1

*Uses:* [[§40 The Unit Quaternions and SU(2)#^def-40-1|Def. §40.1]], [[§40 The Unit Quaternions and SU(2)#^prop-40-1|§40.1]], [[§40 The Unit Quaternions and SU(2)#^prop-40-4|§40.4]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|Def. §11.7]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§35 Submanifolds#^lem-35-3|§35.3]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[Continuous Image of a Connected Space is Connected|590 §15.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]

> [!remark]- Connections
> - The half-angle in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - Isometries in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]; the kernel $\{\pm 1\}$ as a center in 493: [[§35 The Center#^def-35-1|493 Def. §35.1]].

The half-angle in (3) is the source of the factor $2$ below: the curve $\gamma_j(t)$ through $1$ moves at unit speed in $S^3$, but its image rotates by $2t$.

> [!theorem] Lemma §41.2: Every Rotation Has an Axis
> Every $A \in \mathrm{SO}(3)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]]) is the rotation by some angle $\theta$ about some unit axis $u$.

^lem-41-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $\det(A - I) = \det(A - A A^{\mathsf T}) = \det A \, \det(I - A^{\mathsf T}) = \det(I - A) = -\det(A - I)$, the last step because $3$ is odd. So $\det(A - I) = 0$, and $Au = u$ for some unit $u$. $A$ preserves $u^\perp$ and restricts to an orientation-preserving isometry of that plane, a rotation by some $\theta$.

^pf-41-2

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§37 Determinants#^ladr-9-56|LADR 9.56]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]]

> [!remark]- Connections
> - Rotations in Quantum Mechanics, by Euler angles: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-2|QM Def. §C5.2.2]]; isometries in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

## The Double Cover

> [!theorem] Lemma §41.3: Translating the Differential
> Let $G : H \to K$ be a smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) between groups of matrices that are regular submanifolds ([[§35 Submanifolds#^def-35-1|Def. §35.1]]), closed under products and inverses. For $h \in H$ let $L_h(x) = hx$. Then for every $g \in H$,
>
> $$
> G_{\ast g} = (L_{G(g)})_{\ast I} \circ G_{\ast I} \circ (L_{g^{-1}})_{\ast g} ,
> $$
>
> and each $(L_h)_{\ast}$ is an isomorphism. In particular, if $G_{\ast I}$ is an isomorphism, so is every $G_{\ast g}$.

^lem-41-3

> [!proof]+ Proof
> *(The submitted solution's argument, isolated as a lemma; in its original form it is part of the [[§41 SU(2) → SO(3)꞉ The Double Cover#^pf-41-4-2|second proof]] of [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4]].)* $L_h$ is the restriction of the linear map $x \mapsto hx$, so it is smooth ([[§35 Submanifolds#^lem-35-3|Lemma §35.3]]), with smooth inverse $L_{h^{-1}}$: a diffeomorphism, so its differentials are isomorphisms ([[§28 Derivations and the Abstract Tangent Space#^thm-28-6|chain rule]]). $G$ is a homomorphism, so $G \circ L_g = L_{G(g)} \circ G$; differentiating at $I$ gives $G_{\ast g} \circ (L_g)_{\ast I} = (L_{G(g)})_{\ast I} \circ G_{\ast I}$, and $(L_g)_{\ast I}^{-1} = (L_{g^{-1}})_{\ast g}$.

^pf-41-3

*Uses:* [[§35 Submanifolds#^lem-35-3|§35.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!remark]- Connections
> - The geometric version for the classical groups, $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$: [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§25 The Geometric Tangent Space#^rem-25-7|Remark: Left and Right Translates]].

This is the left translation of the [[§25 The Geometric Tangent Space#^rem-25-7|discussion of moving base points]]: in a group, translation carries the tangent space at $I$ to the tangent space at every $g$, so what happens at the identity happens everywhere.

> [!theorem] Theorem §41.4: The Double Cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$
> $G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a surjective smooth group homomorphism and a local diffeomorphism ([[§33 Local Diffeomorphisms#^def-33-1|Def. §33.1]]), with
>
> $$
> G_{\ast I}(\sigma_j) = 2\,\hat e_j \qquad (j = 1, 2, 3),
> $$
>
> twice the basis of $\operatorname{Skew}(3, \mathbb{R}) = T_I\,\mathrm{SO}(3)$ given by the hat map ([[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]]). It is two-to-one: $G(g) = G(h)$ iff $h = \pm g$. Consequently $G$ induces a homeomorphism ([[§10 Continuous Functions#^def-10-2|590 Def. §10.2]])
>
> $$
> \mathrm{SO}(3) \;\cong\; \mathrm{SU}(2)/\{\pm I\} \;\cong\; S^3/\{\pm 1\} \;=\; \mathbb{RP}^3 .
> $$

^thm-41-4

> [!proof]+ Proof
> *(The submitted solution computed $G_{\ast I}(\sigma_j)$ and proved the local diffeomorphism; surjectivity, the two-to-one property and the identification with $\mathbb{RP}^3$ are filled in; the submitted proof follows.)* $G$ is a smooth homomorphism, as a composite of $F^{-1}$ ([[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5]]) and $C$.
>
> *The differential at $I$.* By the chain rule $G_{\ast I}(\sigma_j) = G_{\ast I}(F_{\ast 1}(\gamma_j'(0))) = C_{\ast 1}(\gamma_j'(0)) = (C \circ \gamma_j)'(0)$, and by [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|Proposition §41.1]](3) with $\theta = 2t$, $C(\gamma_j(t))$ is the rotation by $2t$ about $e_j$; for $j = 1$,
>
> $$
> C(\gamma_1(t)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2t & -\sin 2t \\ 0 & \sin 2t & \cos 2t \end{pmatrix}, \qquad \frac{d}{dt}\Big|_{t=0} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix} = 2\,\hat e_1 ,
> $$
>
> and likewise for $j = 2, 3$ ([[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]]). The $\hat e_j$ are a basis of $T_I\,\mathrm{SO}(3) = \operatorname{Skew}(3, \mathbb{R})$ ([[§25 The Geometric Tangent Space#^ex-25-4|Example §25.4]]), so $G_{\ast I}$ is an isomorphism.
>
> *Local diffeomorphism.* By [[§41 SU(2) → SO(3)꞉ The Double Cover#^lem-41-3|Lemma §41.3]] every $G_{\ast g}$ is an isomorphism, so $G$ is a local diffeomorphism ([[§33 Local Diffeomorphisms#^thm-33-2|Theorem §33.2]]).
>
> *Surjective.* By [[§41 SU(2) → SO(3)꞉ The Double Cover#^lem-41-2|Lemma §41.2]], an element of $\mathrm{SO}(3)$ is a rotation by some $\theta$ about some $u$, which is $C_q = G(F(q))$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ by [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|Proposition §41.1]](3).
>
> *Two-to-one.* $G(g) = G(h)$ iff $C_{F^{-1}(g)} = C_{F^{-1}(h)}$ iff $F^{-1}(h) = \pm F^{-1}(g)$ ([[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|Proposition §41.1]](2)) iff $h = \pm g$, since $F$ is a homomorphism with $F(-1) = -I$.
>
> *$\mathbb{RP}^3$.* $C$ is constant on the classes $\{\pm q\}$, so it induces a map $\bar C : S^3/\{\pm 1\} \to \mathrm{SO}(3)$, continuous by the [[§5 Quotient Maps#^cor-5-2|universal property of the quotient]], and bijective by the last two steps. $S^3/\{\pm 1\} = \mathbb{RP}^3$ ([[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|Corollary §18.5]]) is compact as the image of $S^3$, and $\mathrm{SO}(3)$ is Hausdorff, so $\bar C$ is a homeomorphism ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]); and $F$ identifies $S^3/\{\pm 1\}$ with $\mathrm{SU}(2)/\{\pm I\}$.

^pf-41-4

*Uses:* [[§40 The Unit Quaternions and SU(2)#^prop-40-5|§40.5]], [[§40 The Unit Quaternions and SU(2)#^prop-40-6|§40.6]], [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|§41.1]], [[§41 SU(2) → SO(3)꞉ The Double Cover#^lem-41-2|§41.2]], [[§41 SU(2) → SO(3)꞉ The Double Cover#^lem-41-3|§41.3]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§25 The Geometric Tangent Space#^ex-25-4|Ex. §25.4]], [[§33 Local Diffeomorphisms#^thm-33-2|§33.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Universal Property of Quotient Maps|590 §13.3]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!proof]+ Second proof: the conjugation map computed explicitly (the submitted solution)
>
> *(Assignment 4, Problem 3(b), as submitted, in the notation of the second proofs of Propositions [[§40 The Unit Quaternions and SU(2)#^prop-40-5|§40.5]] and [[§40 The Unit Quaternions and SU(2)#^prop-40-6|§40.6]]; “part (a)” is the [[§40 The Unit Quaternions and SU(2)#^pf-40-6-2|second proof]] of [[§40 The Unit Quaternions and SU(2)#^prop-40-6|Proposition §40.6]]. It proves that $G$ is smooth, the formula for $G_{\ast I}(\sigma_j)$ — the three matrices it finds are $2\hat e_1$, $2\hat e_2$, $2\hat e_3$ ([[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]]) — and that $G$ is a [[§33 Local Diffeomorphisms#^def-33-1|local diffeomorphism]]; surjectivity, the two-to-one property and $\mathbb{RP}^3$ are proved above. What it takes as given from the problem is proved in Propositions [[§40 The Unit Quaternions and SU(2)#^prop-40-5|§40.5]] and [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|§41.1]]. Its proof that $F^{-1}$ is smooth is in the [[§40 The Unit Quaternions and SU(2)#^pf-40-5-2|second proof]] of [[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5]]. In $C(\vec x)$, $\vec x$ is a point of $S^3$; in the proof above, $C_q$ is the same map for $q = h(\vec x)$.)*
>
> **Reduction to the conjugation map.** Let $\mathbb{H}_0 = \{ y_1 i + y_2 j + y_3 k : y_1, y_2, y_3 \in \mathbb{R} \}$ be the purely imaginary quaternions, and identify $\mathbb{R}^3$ with $\mathbb{H}_0$ by $h_0(y_1, y_2, y_3) = h(0, y_1, y_2, y_3) = y_1 i + y_2 j + y_3 k$. For $\vec x \in S^3$, conjugation by the unit quaternion $h(\vec x)$, whose inverse is $\overline{h(\vec x)}$, defines the linear map
>
> $$
> C(\vec x) : \mathbb{R}^3 \to \mathbb{R}^3, \qquad C(\vec x)(\vec y) = h_0^{-1}\Bigl( h(\vec x)\; h_0(\vec y)\; \overline{h(\vec x)} \Bigr).
> $$
>
> As stated in the problem, $C(\vec x) \in \mathrm{SO}(3)$, and $C : S^3 \to \mathrm{SO}(3)$ is a $2$–$1$ [[§15 Homomorphisms#^def-15-1|group morphism]]; we take these facts as given.
>
> *Smoothness.* Each coordinate of the quaternion $h(\vec x)\, h_0(\vec y)\, \overline{h(\vec x)}$ is a polynomial in the variables $x_0, \ldots, x_3$ and $y_1, y_2, y_3$, quadratic in $\vec x$ and linear in $\vec y$, so each entry of the matrix $C(\vec x)$ is a quadratic polynomial in $x_0, \ldots, x_3$. Hence $C$ is the restriction to $S^3$ of a smooth map $\mathbb{R}^4 \to \mathrm{Mat}(3, \mathbb{R})$, so it is smooth as a map $S^3 \to \mathrm{Mat}(3, \mathbb{R})$ (composing with the inclusion of $S^3$), and since its image lies in the embedded submanifold $\mathrm{SO}(3)$, it is smooth as a map $S^3 \to \mathrm{SO}(3)$ ([[§35 Submanifolds#^lem-35-3|Lemma §35.3]]). [The submitted proof that $F^{-1} : \mathrm{SU}(2) \to S^3$ is smooth stands here; it is now the last paragraph of the [[§40 The Unit Quaternions and SU(2)#^pf-40-5-2|second proof]] of [[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5]].] Thus
>
> $$
> G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)
> $$
>
> is smooth, as a composite of smooth maps.
>
> *Reduction.* Since $G \circ F = C$ and $F(\vec e_0) = I$, the [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|chain rule]] gives $G_{\ast,I} \circ F_{\ast,\vec e_0} = C_{\ast,\vec e_0}$. Applying this to $\vec e_j$ and using $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ from part (a),
>
> $$
> G_{\ast,I}(\sigma_j) = C_{\ast,\vec e_0}(\vec e_j), \qquad j = 1, 2, 3.
> $$
>
> By the chain rule for curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3]]), with the curves $\gamma_j$ of part (a), which satisfy $\gamma_j(0) = \vec e_0$ and $D_{\gamma_j} = \vec e_j$,
>
> $$
> G_{\ast,I}(\sigma_j) = D_{C \circ \gamma_j} = \frac{d}{dt}\Big|_{t=0} C\bigl(\gamma_j(t)\bigr),
> $$
>
> the entrywise derivative of the matrix $C(\gamma_j(t))$, where $h(\gamma_j(t)) = \cos t + \sin t\, u_j$ with $u_1 = i$, $u_2 = j$, $u_3 = k$.
>
> **Computing $C(\gamma_j(t))$.** Let $\vec y \in \mathbb{R}^3$ and $v = h_0(\vec y) = y_1 i + y_2 j + y_3 k$. Since $\overline{h(\gamma_j(t))} = \cos t - \sin t\, u_j$, expanding the four terms gives
>
> $$
> (\cos t + \sin t\, u_j)\, v\, (\cos t - \sin t\, u_j) = \cos^2 t\; v + \sin t \cos t\, (u_j v - v u_j) - \sin^2 t\; u_j v u_j .
> $$
>
> Using $i^2 = j^2 = k^2 = -1$ and $ij = k = -ji$, $jk = i = -kj$, $ki = j = -ik$, the two products needed are:
> - for $u_1 = i$: $\ iv - vi = -2y_3\, j + 2y_2\, k$ and $ivi = -y_1 i + y_2 j + y_3 k$;
> - for $u_2 = j$: $\ jv - vj = 2y_3\, i - 2y_1\, k$ and $jvj = y_1 i - y_2 j + y_3 k$;
> - for $u_3 = k$: $\ kv - vk = -2y_2\, i + 2y_1\, j$ and $kvk = y_1 i + y_2 j - y_3 k$.
>
> Substituting, and using $\cos^2 t - \sin^2 t = \cos 2t$ and $2 \sin t \cos t = \sin 2t$,
>
> $$
> \begin{aligned}
> (\cos t + \sin t\, i)\, v\, (\cos t - \sin t\, i) &= y_1\, i + (\cos 2t\, y_2 - \sin 2t\, y_3)\, j + (\sin 2t\, y_2 + \cos 2t\, y_3)\, k, \\
> (\cos t + \sin t\, j)\, v\, (\cos t - \sin t\, j) &= (\cos 2t\, y_1 + \sin 2t\, y_3)\, i + y_2\, j + (-\sin 2t\, y_1 + \cos 2t\, y_3)\, k, \\
> (\cos t + \sin t\, k)\, v\, (\cos t - \sin t\, k) &= (\cos 2t\, y_1 - \sin 2t\, y_2)\, i + (\sin 2t\, y_1 + \cos 2t\, y_2)\, j + y_3\, k .
> \end{aligned}
> $$
>
> Applying $h_0^{-1}$ and reading off the matrices with respect to $\vec y$,
>
> $$
> C(\gamma_1(t)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2t & -\sin 2t \\ 0 & \sin 2t & \cos 2t \end{pmatrix}, \quad
> C(\gamma_2(t)) = \begin{pmatrix} \cos 2t & 0 & \sin 2t \\ 0 & 1 & 0 \\ -\sin 2t & 0 & \cos 2t \end{pmatrix},
> $$
>
> $$
> C(\gamma_3(t)) = \begin{pmatrix} \cos 2t & -\sin 2t & 0 \\ \sin 2t & \cos 2t & 0 \\ 0 & 0 & 1 \end{pmatrix}.
> $$
>
> **The vectors $G_{\ast,I}(\sigma_j)$.** Differentiating entrywise at $t = 0$, the constant entries give $0$, while $\frac{d}{dt}\cos 2t = -2\sin 2t$ and $\frac{d}{dt}\sin 2t = 2\cos 2t$ take the values $0$ and $2$ at $t = 0$. Hence
>
> $$
> G_{\ast,I}(\sigma_1) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix}, \qquad
> G_{\ast,I}(\sigma_2) = \begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \\ -2 & 0 & 0 \end{pmatrix}, \qquad
> G_{\ast,I}(\sigma_3) = \begin{pmatrix} 0 & -2 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
> $$
>
> **$G_{\ast,I}$ is an isomorphism.** The matrices $\sigma_1, \sigma_2, \sigma_3$ are linearly independent: if $a\sigma_1 + b\sigma_2 + c\sigma_3 = 0$ with $a, b, c \in \mathbb{R}$, the $(1,1)$, $(1,2)$ and $(2,1)$ entries give $-ai = 0$, $b - ci = 0$ and $-b - ci = 0$, so $a = b = c = 0$. Since $\dim T_I\,\mathrm{SU}(2) = 3$, they form a basis of $T_I\,\mathrm{SU}(2)$. Their images are also linearly independent: if $a\,G_{\ast,I}(\sigma_1) + b\,G_{\ast,I}(\sigma_2) + c\,G_{\ast,I}(\sigma_3) = 0$, the $(3,2)$, $(1,3)$ and $(2,1)$ entries give $2a = 0$, $2b = 0$ and $2c = 0$. So the linear map $G_{\ast,I} : T_I\,\mathrm{SU}(2) \to T_I\,\mathrm{SO}(3)$ sends a basis to $3$ linearly independent vectors of the $3$-dimensional space $T_I\,\mathrm{SO}(3)$, and is therefore an isomorphism.
>
> **$G_{\ast,g}$ is an isomorphism for every $g$.** By the problem, $C$ is a group morphism and $F$ is a group isomorphism; hence $F^{-1}$ is a group morphism, and so is $G = C \circ F^{-1}$. In particular $G(I) = I$.
>
> *The translation identity.* For $g \in \mathrm{SU}(2)$ let $L_g : \mathrm{SU}(2) \to \mathrm{SU}(2)$, $L_g(g') = gg'$, and for $A \in \mathrm{SO}(3)$ let $L_A : \mathrm{SO}(3) \to \mathrm{SO}(3)$, $L_A(A') = AA'$. For every $g' \in \mathrm{SU}(2)$,
>
> $$
> G\bigl(L_g(g')\bigr) = G(gg') = G(g)\,G(g') = L_{G(g)}\bigl(G(g')\bigr),
> $$
>
> so $G \circ L_g = L_{G(g)} \circ G$.
>
> *Translations are diffeomorphisms.* On $\mathrm{Mat}(2, \mathbb{C})$ the map $M \mapsto gM$ is linear, hence smooth; its restriction to the embedded submanifold $\mathrm{SU}(2)$ is smooth, and it takes values in $\mathrm{SU}(2)$ because $\mathrm{SU}(2)$ is closed under products, so $L_g : \mathrm{SU}(2) \to \mathrm{SU}(2)$ is smooth, since a smooth map whose image lies in an embedded submanifold is smooth into that submanifold ([[§35 Submanifolds#^lem-35-3|Lemma §35.3]]). The same holds for $L_{g^{-1}}$, and $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$ by associativity and $g g^{-1} = g^{-1} g = I$. Hence $L_g$ is a diffeomorphism, and by the chain rule ([[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6]]) $(L_{g^{-1}})_{\ast,g} \circ (L_g)_{\ast,I} = \mathrm{id}$ and $(L_g)_{\ast,I} \circ (L_{g^{-1}})_{\ast,g} = \mathrm{id}$, so $(L_g)_{\ast,I}$ is an isomorphism with inverse $(L_{g^{-1}})_{\ast,g}$. In the same way, using that $\mathrm{SO}(3)$ is an embedded submanifold of $\mathrm{Mat}(3, \mathbb{R})$ closed under products, $L_{G(g)}$ is a diffeomorphism of $\mathrm{SO}(3)$ and $(L_{G(g)})_{\ast,I}$ is an isomorphism.
>
> *The chain rule at $I$.* Since $L_g(I) = g$ and $G(I) = I$, applying the chain rule to both sides of $G \circ L_g = L_{G(g)} \circ G$ at $I$ gives
>
> $$
> G_{\ast,g} \circ (L_g)_{\ast,I} = (L_{G(g)})_{\ast,I} \circ G_{\ast,I},
> $$
>
> and therefore
>
> $$
> G_{\ast,g} = (L_{G(g)})_{\ast,I} \circ G_{\ast,I} \circ (L_{g^{-1}})_{\ast,g} .
> $$
>
> Each factor is an isomorphism, so $G_{\ast,g} : T_g\,\mathrm{SU}(2) \to T_{G(g)}\,\mathrm{SO}(3)$ is an isomorphism.
>
> **$G$ is a local diffeomorphism.** Let $g \in \mathrm{SU}(2)$. Choose a chart $(V, \chi)$ of $\mathrm{SO}(3)$ at $G(g)$ and, using continuity of $G$, a chart $(U, \varphi)$ of $\mathrm{SU}(2)$ at $g$ with $G(U) \subseteq V$. The coordinate representation $\hat G = \chi \circ G \circ \varphi^{-1} : \varphi(U) \to \chi(V)$ is a smooth map between open subsets of $\mathbb{R}^3$, and its Jacobian at $\varphi(g)$ is the matrix of $G_{\ast,g}$ in the coordinate bases ([[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2]]), hence invertible. By the inverse function theorem ([[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1]]), there are open sets $U_0 \ni \varphi(g)$ in $\varphi(U)$ and $V_0 = \hat G(U_0) \subseteq \chi(V)$ such that $\hat G|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse. Then $\varphi^{-1}(U_0)$ is an open neighborhood of $g$, $\chi^{-1}(V_0)$ is open in $\mathrm{SO}(3)$, and
>
> $$
> G|_{\varphi^{-1}(U_0)} = \chi^{-1} \circ \hat G|_{U_0} \circ \varphi : \varphi^{-1}(U_0) \to \chi^{-1}(V_0)
> $$
>
> is a composite of diffeomorphisms, hence a diffeomorphism. As $g$ was arbitrary, $G$ is a local diffeomorphism.

^pf-41-4-2

*Uses:* [[§40 The Unit Quaternions and SU(2)#^prop-40-5|§40.5]], [[§40 The Unit Quaternions and SU(2)#^prop-40-6|§40.6]], [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|§41.1]], [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§35 Submanifolds#^lem-35-3|§35.3]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[§33 Local Diffeomorphisms#^def-33-1|Def. §33.1]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[Inverse Function Theorem (several variables)|452 §16.2]]

> [!remark]- Connections
> - The same theorem in physics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; $\mathrm{SU}(2) \cong S^3$ and $\mathrm{SO}(3) \cong \mathbb{RP}^3$ topologically, with $\pi_1$: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|QFT Theorem §C3.1.8]].
> - The algebraic quotient in 493: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 §41.1]]; $\mathbb{RP}^n$ as the quotient $S^n/(x \sim -x)$ in 590: [[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]].

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Complex Projective Space|Complex Projective Space]], an orbit map in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; the first is the quotient map of [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; [[§39 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]] shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]].

![[m591-35-2.svg]]
*(a) For $q = \cos t + \sin t\, u$, with $u \in \mathbb{H}_0$ a unit vector, $C_q(v) = q v \bar q$ fixes the axis $u$ and turns $v$ by the angle $2t$ about it, along the dashed circle traced by the tip of $v$: [[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|Proposition §41.1]](3) with $\theta = 2t$. (b) Why it is two-to-one: the great circle $\gamma(t) = \cos t + \sin t\, u$ in $S^3$, drawn as a circle, is mapped by $C$ onto the loop of rotations about $u$ in $\mathrm{SO}(3)$. The antipodal points $q$ and $-q = \gamma(t + \pi)$ (red) give the same rotation $C_q = C_{-q}$, by the angle $2t$, and $\pm 1$ both give $I$ ([[§41 SU(2) → SO(3)꞉ The Double Cover#^prop-41-1|§41.1]](2)). The first half of the circle, $t \in [0, \pi]$ (blue), already goes once around the loop of rotations, and the second half (orange) goes around it again: once around the circle is twice around the rotations, the double cover of [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4]]. (Drawn for these notes in the vault; not in the course tex.)*

> [!remark] Remark: What the Example Shows
> $G$ is a local diffeomorphism ([[§33 Local Diffeomorphisms#^def-33-1|Def. §33.1]]) that is not a diffeomorphism: locally $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are indistinguishable — their tangent spaces at $I$ are isomorphic, and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ — but globally $\mathrm{SU}(2) \cong S^3$ wraps twice around $\mathrm{SO}(3) \cong \mathbb{RP}^3$. Every fibre $G^{-1}(A) = \{\pm g\}$ is two points, and $G$ is a proper ([[§38 Embeddings#^def-38-2|Def. §38.2]]) surjective submersion ([[§34 Submersions#^def-34-1|Def. §34.1]]) onto the connected $\mathrm{SO}(3)$, so Ehresmann's theorem ([[§36 Fibrations#^thm-36-3|Theorem §36.3]], stated without proof) makes it a fibration ([[§36 Fibrations#^def-36-1|Def. §36.1]]) whose fibre is two points: a double cover. The smooth version of the last statement — that $\bar C$ is a diffeomorphism for the smooth structure of $\mathbb{RP}^3$ — needs the quotient map $S^3 \to \mathbb{RP}^3$ to be a local diffeomorphism, and is not proved here.

^rem-41-1

> [!remark]- Connections
> - The quotient map $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§39 Projective Spaces and the Hopf Fibration#^ex-39-1|Ex. §39.1]]; bijective local diffeomorphisms: [[§33 Local Diffeomorphisms#^cor-33-3|§33.3]].
> - Covering maps: [[§33 Local Diffeomorphisms#^rem-33-2|Remark: Covering Maps]]; in 590: [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]], [[Properties of the Lifting Correspondence|590 §32.4]].
