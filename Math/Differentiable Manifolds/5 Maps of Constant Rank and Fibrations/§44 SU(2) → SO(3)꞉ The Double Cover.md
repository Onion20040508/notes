---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 44
tags: [differentiable-manifolds, math591]
---
← [[§43 The Unit Quaternions and SU(2)]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§45 Recap꞉ Germs, Derivations and Tangent Vectors]] →

*Stage: maps — One example that uses everything so far: submanifolds, embeddings, local diffeomorphisms, and translation in a group.*

*From Assignment 4, Problem 3: the submitted solution, reorganized, with every claim the problem allowed us to assume now proved. References: Lee, Problems 7-22 and 7-23 (quaternions).*

The unit quaternions form a group $S^3$; acting on $\mathbb{C}^2$ they identify it with $\mathrm{SU}(2)$, and acting by conjugation on the pure imaginary quaternions $\mathbb{R}^3$ they give rotations. The result is a two-to-one local diffeomorphism $\mathrm{SU}(2) \to \mathrm{SO}(3)$, and with it $\mathrm{SO}(3) \cong \mathbb{RP}^3$.

![[m591-35-1.svg]]
*The three maps of the section: $F$ identifies unit quaternions with matrices in $\mathrm{SU}(2)$ ([[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5]]); $C$ is conjugation ([[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|Proposition §44.1]]); and $G = C \circ F^{-1}$ is the double cover ([[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|Theorem §44.4]]).*

## Conjugation and Rotations

> [!theorem] Proposition §44.1: Conjugation by Unit Quaternions Is Rotation
> For $q \in S^3$, the map $C_q(v) = q v \bar q$ sends $\mathbb{H}_0 \cong \mathbb{R}^3$ to itself, and:
> 1. $C_q \in \mathrm{SO}(3)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]]), and $C : S^3 \to \mathrm{SO}(3)$, $q \mapsto C_q$, is a smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]);
> 2. $\ker C = \{\pm 1\}$ ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]]), so $C_p = C_q$ if and only if $p = \pm q$;
> 3. if $u \in \mathbb{H}_0$ is a unit vector and $\theta \in \mathbb{R}$, then $C_q$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ is the rotation by the angle $\theta$ about the axis $u$.

^prop-44-1

> [!proof]+ Proof
> *(The problem stated (1) and the two-to-one property without proof; filled in. Part (3) contains the submitted computation: for $q = \gamma_j(t)$ it gives the rotation by $2t$ about $e_j$; the submitted computation itself is in the second proof of Theorem [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|§44.4]].)* Throughout, $\mathbb{H}_0 \cong \mathbb{R}^3$ by $y_1 i + y_2 j + y_3 k \leftrightarrow (y_1, y_2, y_3)$, so $i, j, k$ correspond to $e_1, e_2, e_3$, and the norm, dot product and cross product of $\mathbb{R}^3$ are used on $\mathbb{H}_0$; matrices of maps $\mathbb{H}_0 \to \mathbb{H}_0$ are taken in the basis $i, j, k$.
>
> *$C_q$ maps $\mathbb{H}_0$ to itself isometrically.* A quaternion $v = x_0 + w$ ($w$ pure imaginary) has $\bar v = x_0 - w$, so $\bar v = -v$ iff $x_0 = -x_0$ iff $x_0 = 0$: $v$ is pure imaginary iff $\bar v = -v$. For such $v$, applying $\overline{pq} = \bar q \bar p$ (Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-1|§43.1]]) twice and $\bar{\bar q} = q$,
>
> $$
> \overline{q v \bar q} = \bar{\bar q}\; \overline{qv} = q\, \bar v\, \bar q = q(-v)\bar q = -q v \bar q ,
> $$
>
> so $C_q(v) \in \mathbb{H}_0$. By $|pq| = |p|\,|q|$, $|C_q(v)| = |q|\,|v|\,|\bar q| = |v|$. $C_q$ is $\mathbb{R}$-linear, since multiplication is bilinear. So $C_q$ is a linear isometry of $\mathbb{R}^3$. A linear map preserving norms preserves dot products, by polarization: $C_q v \cdot C_q w = \frac12\big(|C_q(v + w)|^2 - |C_q v|^2 - |C_q w|^2\big) = \frac12\big(|v + w|^2 - |v|^2 - |w|^2\big) = v \cdot w$. So the columns of its matrix are orthonormal, $C_q^{\mathsf T} C_q = I$, and $C_q \in \mathrm{O}(3)$.
>
> (1) *Homomorphism.* By $\overline{pq} = \bar q \bar p$ and associativity, for $v \in \mathbb{H}_0$,
>
> $$
> C_{pq}(v) = (pq)\, v\, \overline{pq} = p q v \bar q \bar p = p\,(q v \bar q)\,\bar p = C_p(C_q(v)) ,
> $$
>
> so $C_{pq} = C_p C_q$.
>
> *Smooth into $\operatorname{Mat}(3, \mathbb{R})$.* The $(a, b)$ entry of the matrix of $C_q$ is the $e_a$-coordinate of $q\, e_b\, \bar q$. With $q = \sum_c x_c e_c$ and $\bar q = \sum_d \pm x_d e_d$, bilinearity gives $q e_b \bar q = \sum_{c,d} \pm x_c x_d\, e_c e_b e_d$, and each $e_c e_b e_d$ is $\pm$ a basis element. So the entries of $C_q$ are quadratic polynomials in the coordinates $x_0, \ldots, x_3$ of $q$: $C$ is the restriction to $S^3$ of a smooth map $\mathbb{R}^4 \to \operatorname{Mat}(3, \mathbb{R})$, hence smooth from $S^3$ (compose with the inclusion, Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)).
>
> *Values in $\mathrm{SO}(3)$.* For $A \in \mathrm{O}(3)$, $\det(A)^2 = \det(A^{\mathsf T} A) = 1$, so $\det \circ C : S^3 \to \{\pm 1\}$. It is continuous, and $S^3$ is connected (Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-4|§43.4]]); if it took both values, the preimages of $1$ and of $-1$ would be disjoint nonempty open sets covering $S^3$. So it is constant, equal to its value $\det C_1 = \det I = 1$ at $q = 1$ (where $C_1(v) = v$). Hence $C$ takes values in $\mathrm{SO}(3)$.
>
> *Smooth into $\mathrm{SO}(3)$.* $\mathrm{O}(3)$ is the regular level set $F^{-1}(I)$ of $F(g) = gg^{\mathsf T}$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], Example [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|§23.1]]), so a regular submanifold of $\operatorname{Mat}(3, \mathbb{R})$ (Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]]). $\mathrm{SO}(3)$ is open in $\mathrm{O}(3)$: $\mathrm{SO}(3) = \mathrm{O}(3) \cap W$ with $W = \det^{-1}\big((0, \infty)\big)$ open in $\operatorname{Mat}(3, \mathbb{R})$, because $\det = \pm 1$ on $\mathrm{O}(3)$. An adapted chart $(U, \varphi)$ of $\mathrm{O}(3)$, restricted to $U \cap W$, satisfies $(U \cap W) \cap \mathrm{SO}(3) = \{q \in U \cap W : x_b(q) = \vec 0\}$, so it is adapted to $\mathrm{SO}(3)$; thus $\mathrm{SO}(3)$ is a regular submanifold of $\operatorname{Mat}(3, \mathbb{R})$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]). Since $C$ is smooth into $\operatorname{Mat}(3, \mathbb{R})$ with values in $\mathrm{SO}(3)$, it is smooth into $\mathrm{SO}(3)$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)).
>
> (2) *The kernel.* If $C_q = \mathrm{id}$, then $q v \bar q = v$ for all $v \in \mathbb{H}_0$; multiplying on the right by $q$ and using $\bar q q = 1$ gives $qv = vq$. So $q$ commutes with $i$, $j$ and $k$. Write $q = x_0 + x_1 i + x_2 j + x_3 k$. By the multiplication table,
>
> $$
> qi - iq = (x_0 i - x_1 - x_2 k + x_3 j) - (x_0 i - x_1 + x_2 k - x_3 j) = 2x_3\, j - 2x_2\, k ,
> $$
>
> $$
> qj - jq = (x_0 j + x_1 k - x_2 - x_3 i) - (x_0 j - x_1 k - x_2 + x_3 i) = 2x_1\, k - 2x_3\, i .
> $$
>
> So $qi = iq$ forces $x_2 = x_3 = 0$, and $qj = jq$ forces $x_1 = 0$; so $q = x_0$ is real, and $|q| = 1$ gives $q = \pm 1$. Conversely $C_{\pm 1}(v) = (\pm 1)\, v\, (\pm 1) = v$, so $C_{\pm 1} = \mathrm{id}$. Hence $\ker C = \{\pm 1\}$.
>
> *Fibres.* Since $C$ is a homomorphism and $\bar q = q^{-1}$, $C_{\bar q} = C_q^{-1}$, and $C_{p \bar q} = C_p C_q^{-1}$. So
>
> $$
> C_p = C_q \iff C_{p\bar q} = \mathrm{id} \iff p\bar q = \pm 1 \iff p = \pm q ,
> $$
>
> the last step by multiplying on the right by $q$ (and by $\bar q$ for the converse), using $\bar q q = q \bar q = 1$.
>
> (3) *Products of pure imaginary quaternions.* Write $c = \cos\frac\theta2$, $s = \sin\frac\theta2$, so $q = c + su$ and $\bar q = c - su$, with $|q|^2 = c^2 + s^2 |u|^2 = 1$. For pure imaginary $u = \sum_a u_a e_a$, $v = \sum_b v_b e_b$ ($a, b \in \{1, 2, 3\}$), bilinearity, $e_a^2 = -1$ and $ij = k = -ji$, $jk = i = -kj$, $ki = j = -ik$ give
>
> $$
> uv = \sum_a u_a v_a\, e_a^2 + \sum_{a \neq b} u_a v_b\, e_a e_b = -u \cdot v + (u_2 v_3 - u_3 v_2)\, i + (u_3 v_1 - u_1 v_3)\, j + (u_1 v_2 - u_2 v_1)\, k = -u\cdot v + u \times v .
> $$
>
> *The axis is fixed.* In particular $u^2 = -|u|^2 = -1$. So $u$ commutes with $q$: $uq = cu + s u^2 = qu$. Hence $C_q(u) = q u \bar q = u q \bar q = u\, |q|^2 = u$.
>
> *The plane $u^\perp$ is rotated.* If $v \in \mathbb{H}_0$ with $v \perp u$, then $u \cdot v = 0$, so $uv = u \times v$ and $vu = v \times u = -u \times v = -uv$. Hence $v \bar q = cv - s\, vu = cv + s\, uv = (c + su) v = qv$, and
>
> $$
> C_q(v) = q\,(v \bar q) = q\,(q v) = q^2 v = \big(\cos\theta + \sin\theta\, u\big) v = \cos\theta\, v + \sin\theta\, (u \times v) ,
> $$
>
> where $q^2 = c^2 + 2cs\, u + s^2 u^2 = (c^2 - s^2) + 2cs\, u = \cos\theta + \sin\theta\, u$ by the double-angle formulas, and the last step uses $uv = u \times v$.
>
> *This is the rotation by $\theta$ about $u$.* Choose a unit $v \perp u$ and put $w = u \times v$, a unit vector orthogonal to $u$ and $v$. Then $(v, w, u)$ is an orthonormal basis with $v \times w = v \times (u \times v) = u\,(v \cdot v) - v\,(v \cdot u) = u$, so $Q = (v \ w \ u)$, the matrix with these columns, lies in $\mathrm{SO}(3)$ ($\det Q = (v \times w) \cdot u = 1$) and $Q e_3 = u$. By the previous step, applied to $v$ and to $w \perp u$, and $u \times w = u \times (u \times v) = u\,(u \cdot v) - v\,(u \cdot u) = -v$,
>
> $$
> C_q(v) = \cos\theta\, v + \sin\theta\, w, \qquad C_q(w) = \cos\theta\, w - \sin\theta\, v, \qquad C_q(u) = u .
> $$
>
> So $C_q Q = Q R(\theta)$ with $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$, i.e. $C_q = Q R(\theta) Q^{\mathsf T}$: by Example [[§25 The Geometric Tangent Space#^ex-25-4|§25.4]] this is the rotation about $Qe_3 = u$ by the angle $\theta$. It fixes $u$ and turns the plane $u^\perp$ through $\theta$.

^pf-44-1

*Uses:* [[§43 The Unit Quaternions and SU(2)#^def-43-1|Def. §43.1]], [[§43 The Unit Quaternions and SU(2)#^prop-43-1|§43.1]], [[§43 The Unit Quaternions and SU(2)#^prop-43-4|§43.4]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|Def. §11.7]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[Continuous Image of a Connected Space is Connected|590 §15.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|§44.4]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§37 Regular Submanifolds#^thm-37-9|§37.9]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§25 The Geometric Tangent Space#^ex-25-4|Ex. §25.4]]

> [!remark]- Connections
> - The half-angle in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - Isometries in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]; the kernel $\{\pm 1\}$ as a center in 493: [[§35 The Center#^def-35-2|493 Def. §35.2]].

The half-angle in (3) is the source of the factor $2$ below: the curve $\gamma_j(t)$ through $1$ moves at unit speed in $S^3$, but its image rotates by $2t$.

> [!theorem] Lemma §44.2: Every Rotation Has an Axis
> Every $A \in \mathrm{SO}(3)$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]]) is the rotation by some angle $\theta$ about some unit axis $u$.

^lem-44-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* We must find a unit $u$ and an angle $\theta$ with $A = Q R(\theta) Q^{\mathsf T}$ for some $Q \in \mathrm{SO}(3)$ with $Qe_3 = u$, which is the rotation by $\theta$ about $u$ (Example [[§25 The Geometric Tangent Space#^ex-25-4|§25.4]]). Recall $A^{\mathsf T} A = A A^{\mathsf T} = I$ and $\det A = 1$.
>
> *An axis.* Using $I = AA^{\mathsf T}$, multiplicativity of $\det$, $\det A = 1$, $\det B^{\mathsf T} = \det B$, and $\det(-B) = (-1)^3 \det B$ for $3 \times 3$ matrices,
>
> $$
> \det(A - I) = \det(A - A A^{\mathsf T}) = \det A \, \det(I - A^{\mathsf T}) = \det\big((I - A)^{\mathsf T}\big) = \det(I - A) = -\det(A - I),
> $$
>
> the last step because $3$ is odd. So $\det(A - I) = 0$, $A - I$ has a nonzero kernel vector $x$, and $u = x/|x|$ is a unit vector with $Au = u$.
>
> *The plane $u^\perp$.* $A$ preserves dot products ($Av \cdot Aw = v^{\mathsf T} A^{\mathsf T} A w = v \cdot w$), so for $v \perp u$, $Av \cdot u = Av \cdot Au = v \cdot u = 0$: $A$ preserves $u^\perp$ and restricts to an isometry of that plane. To see that it is an orientation-preserving one, a rotation by some $\theta$, choose a unit $v \perp u$ and put $w = u \times v$; as in the proof of Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](3), $Q = (v \ w \ u) \in \mathrm{SO}(3)$ and $Qe_3 = u$. The matrix $B = Q^{\mathsf T} A Q$ is orthogonal with $\det B = \det A = 1$, and its third column is $Q^{\mathsf T} A u = Q^{\mathsf T} u = e_3$. Its columns are orthonormal, so the first two are orthogonal to $e_3$ and have third entry $0$; so
>
> $$
> B = \begin{pmatrix} b_{11} & b_{12} & 0 \\ b_{21} & b_{22} & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} \text{ orthogonal with determinant } \det B = 1 .
> $$
>
> The first column $(b_{11}, b_{21})$ is a unit vector, so equals $(\cos\theta, \sin\theta)$ for some $\theta$; the second is a unit vector orthogonal to it, so $\pm(-\sin\theta, \cos\theta)$; and determinant $1$ forces the sign $+$. So $B = R(\theta)$, and $A = Q B Q^{\mathsf T} = Q R(\theta) Q^{\mathsf T}$, the rotation by $\theta$ about $u$.

^pf-44-2

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-8|Def. §11.8]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§37 Determinants#^ladr-9-56|LADR 9.56]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]], [[§25 The Geometric Tangent Space#^ex-25-4|Ex. §25.4]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]]

> [!remark]- Connections
> - Rotations in Quantum Mechanics, by Euler angles: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-2|QM Def. §C5.2.2]]; isometries in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

## The Double Cover

> [!theorem] Lemma §44.3: Translating the Differential
> Let $G : H \to K$ be a smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) between groups of matrices that are regular submanifolds ([[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]), closed under products and inverses. For $h \in H$ let $L_h(x) = hx$. Then for every $g \in H$,
>
> $$
> G_{\ast g} = (L_{G(g)})_{\ast I} \circ G_{\ast I} \circ (L_{g^{-1}})_{\ast g} ,
> $$
>
> and each $(L_h)_{\ast}$ is an isomorphism. In particular, if $G_{\ast I}$ is an isomorphism, so is every $G_{\ast g}$.

^lem-44-3

> [!proof]+ Proof
> *(The submitted solution's argument, isolated as a lemma; in its original form it is part of the second proof of Theorem [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|§44.4]].)* Two claims: each $L_h$ (on $H$, and likewise on $K$) is a diffeomorphism, so its differentials are isomorphisms; and the displayed formula for $G_{\ast g}$.
>
> *Translations are diffeomorphisms.* Let $h \in H$. On the ambient matrix space the map $x \mapsto hx$ is linear, hence smooth; $L_h$ is its restriction to $H$, so it is smooth into the ambient space (compose with the inclusion, Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), and its values lie in $H$ because $H$ is closed under products; so $L_h : H \to H$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)). The same holds for $L_{h^{-1}}$, since $h^{-1} \in H$. By associativity, $L_h \circ L_{h^{-1}}(x) = h h^{-1} x = x$ and $L_{h^{-1}} \circ L_h(x) = x$; so $L_h$ is a diffeomorphism with smooth inverse $L_{h^{-1}}$. For every $x \in H$, the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) applied to these two identities at $x$ and at $hx$ gives
>
> $$
> (L_{h^{-1}})_{\ast hx} \circ (L_h)_{\ast x} = \mathrm{id}, \qquad (L_h)_{\ast x} \circ (L_{h^{-1}})_{\ast hx} = \mathrm{id},
> $$
>
> so $(L_h)_{\ast x}$ is an isomorphism with inverse $(L_{h^{-1}})_{\ast hx}$. In particular, with $h = g$ and $x = I$: $(L_g)_{\ast I}^{-1} = (L_{g^{-1}})_{\ast g}$. The same argument applies verbatim to $K$, which is also closed under products and inverses; so each $(L_k)_{\ast}$, $k \in K$, is an isomorphism.
>
> *The formula.* $G$ is a homomorphism, so $G(I) = I$, and for all $x \in H$,
>
> $$
> G(L_g(x)) = G(gx) = G(g)\,G(x) = L_{G(g)}(G(x)) ,
> $$
>
> i.e. $G \circ L_g = L_{G(g)} \circ G$. Differentiating both sides at $I$ with the Chain Rule, using $L_g(I) = g$ and $G(I) = I$, gives
>
> $$
> G_{\ast g} \circ (L_g)_{\ast I} = (L_{G(g)})_{\ast I} \circ G_{\ast I} .
> $$
>
> Composing on the right with $(L_g)_{\ast I}^{-1} = (L_{g^{-1}})_{\ast g}$ gives $G_{\ast g} = (L_{G(g)})_{\ast I} \circ G_{\ast I} \circ (L_{g^{-1}})_{\ast g}$. If $G_{\ast I}$ is an isomorphism, the right side is a composite of three isomorphisms, so $G_{\ast g}$ is an isomorphism.

^pf-44-3

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|§44.4]]

> [!remark]- Connections
> - The geometric version for the classical groups, $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$: [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§25 The Geometric Tangent Space#^rem-25-7|Remark: Left and Right Translates]].

This is the left translation of the [[§25 The Geometric Tangent Space#^rem-25-7|discussion of moving base points]]: in a group, translation carries the tangent space at $I$ to the tangent space at every $g$, so what happens at the identity happens everywhere.

> [!theorem] Theorem §44.4: The Double Cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$
> $G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a surjective smooth group homomorphism and a local diffeomorphism ([[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]]), with
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

^thm-44-4

> [!proof]+ Proof
> *(The submitted solution computed $G_{\ast I}(\sigma_j)$ and proved the local diffeomorphism; surjectivity, the two-to-one property and the identification with $\mathbb{RP}^3$ are filled in; the submitted proof follows.)* *Smooth homomorphism.* $F : S^3 \to \mathrm{SU}(2)$ is a group isomorphism and a diffeomorphism (Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]]), so $F^{-1}$ is a smooth homomorphism; and $C : S^3 \to \mathrm{SO}(3)$ is a smooth homomorphism (Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](1)). So $G$ is a smooth homomorphism, as a composite of $F^{-1}$ and $C$: a composite of smooth maps is smooth, and a composite of homomorphisms is a homomorphism.
>
> *The differential at $I$.* Since $G \circ F = C \circ F^{-1} \circ F = C$ and $F(1) = I$, the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives $G_{\ast I} \circ F_{\ast1} = C_{\ast1}$. By Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-6|§43.6]], $\sigma_j = F_{\ast1}(\gamma_j'(0))$, where $\gamma_j(t) = \cos t + \sin t\, u_j$ with $u_1 = i$, $u_2 = j$, $u_3 = k$. With the chain rule for curves (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]),
>
> $$
> G_{\ast I}(\sigma_j) = G_{\ast I}\big(F_{\ast1}(\gamma_j'(0))\big) = C_{\ast1}(\gamma_j'(0)) = (C \circ \gamma_j)'(0) ,
> $$
>
> the entrywise derivative of the curve $C(\gamma_j(t))$ in $\mathrm{SO}(3) \subseteq \operatorname{Mat}(3, \mathbb{R})$. Now $\gamma_j(t) = \cos\frac\theta2 + \sin\frac\theta2\, u_j$ with $\theta = 2t$, so by Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](3), $C(\gamma_j(t))$ is the rotation by $2t$ about $e_j$ ($u_j \leftrightarrow e_j$): it fixes $e_j$ and sends $v \perp e_j$ to $\cos 2t\, v + \sin 2t\, (e_j \times v)$. With $e_1 \times e_2 = e_3$, $e_2 \times e_3 = e_1$, $e_3 \times e_1 = e_2$, its columns are as follows. For $j = 1$: $e_1 \mapsto e_1$, $e_2 \mapsto \cos 2t\, e_2 + \sin 2t\, e_3$, $e_3 \mapsto \cos 2t\, e_3 - \sin 2t\, e_2$; so
>
> $$
> C(\gamma_1(t)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2t & -\sin 2t \\ 0 & \sin 2t & \cos 2t \end{pmatrix}, \qquad \frac{d}{dt}\Big|_{t=0} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix} = 2\,\hat e_1 ,
> $$
>
> using $\frac{d}{dt}\cos 2t|_0 = 0$ and $\frac{d}{dt}\sin 2t|_0 = 2$, and the hat map of Definition [[§25 The Geometric Tangent Space#^def-25-3|§25.3]] with $v = e_1$. For $j = 2$: $e_2 \mapsto e_2$, $e_3 \mapsto \cos 2t\, e_3 + \sin 2t\, e_1$, $e_1 \mapsto \cos 2t\, e_1 - \sin 2t\, e_3$. For $j = 3$: $e_3 \mapsto e_3$, $e_1 \mapsto \cos 2t\, e_1 + \sin 2t\, e_2$, $e_2 \mapsto \cos 2t\, e_2 - \sin 2t\, e_1$. So
>
> $$
> C(\gamma_2(t)) = \begin{pmatrix} \cos 2t & 0 & \sin 2t \\ 0 & 1 & 0 \\ -\sin 2t & 0 & \cos 2t \end{pmatrix}, \qquad C(\gamma_3(t)) = \begin{pmatrix} \cos 2t & -\sin 2t & 0 \\ \sin 2t & \cos 2t & 0 \\ 0 & 0 & 1 \end{pmatrix},
> $$
>
> with derivatives at $t = 0$
>
> $$
> \begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \\ -2 & 0 & 0 \end{pmatrix} = 2\,\hat e_2, \qquad \begin{pmatrix} 0 & -2 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 2\,\hat e_3
> $$
>
> (Definition [[§25 The Geometric Tangent Space#^def-25-3|§25.3]] with $v = e_2$, $e_3$). The hat map is a linear isomorphism $\mathbb{R}^3 \to \operatorname{Skew}(3, \mathbb{R})$, so the $\hat e_j$ are a basis of $T_I\,\mathrm{SO}(3) = \operatorname{Skew}(3, \mathbb{R})$ (Example [[§25 The Geometric Tangent Space#^ex-25-4|§25.4]]), and so are the $2\hat e_j$. Thus $G_{\ast I}$ maps the basis $\sigma_1, \sigma_2, \sigma_3$ of $T_I\,\mathrm{SU}(2)$ (Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-6|§43.6]]) to a basis of $T_I\,\mathrm{SO}(3)$, so $G_{\ast I}$ is an isomorphism.
>
> *Local diffeomorphism.* $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are groups of matrices, closed under products and inverses, and regular submanifolds of $\operatorname{Mat}(2, \mathbb{C})$ and $\operatorname{Mat}(3, \mathbb{R})$ (Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]](3), and the proof of Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](1)). By Lemma [[§44 SU(2) → SO(3)꞉ The Double Cover#^lem-44-3|§44.3]], every $G_{\ast g}$ is an isomorphism, so $G$ is a local diffeomorphism (Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]).
>
> *Surjective.* Let $A \in \mathrm{SO}(3)$. By Lemma [[§44 SU(2) → SO(3)꞉ The Double Cover#^lem-44-2|§44.2]], $A$ is the rotation by some $\theta$ about some unit $u \in \mathbb{R}^3 = \mathbb{H}_0$. Put $q = \cos\frac\theta2 + \sin\frac\theta2\, u \in S^3$. By Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](3), $C_q$ is that rotation, so
>
> $$
> G(F(q)) = C\big(F^{-1}(F(q))\big) = C_q = A .
> $$
>
> *Two-to-one.* $F$ is a homomorphism with $F(-1) = -I$ (the formula of Proposition [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]](2) at $x_0 = -1$), so $F(-q) = F(-1)F(q) = -F(q)$, and likewise $F^{-1}(-g) = -F^{-1}(g)$. Hence, using Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](2) for the middle step,
>
> $$
> G(g) = G(h) \iff C_{F^{-1}(g)} = C_{F^{-1}(h)} \iff F^{-1}(h) = \pm F^{-1}(g) \iff h = \pm g .
> $$
>
> Since $g \neq -g$, every fibre of $G$ has exactly two points.
>
> *$\mathbb{RP}^3$.* By Proposition [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](2), $C_{-q} = C_q$: $C$ is constant on the classes $\{\pm q\}$, so it induces a map $\bar C : S^3/\{\pm 1\} \to \mathrm{SO}(3)$ with $\bar C \circ \pi = C$, continuous by the universal property of the quotient (Corollary [[§5 Quotient Maps#^cor-5-2|§5.2]](1)). It is surjective, since $C = G \circ F$ is ($G$ by the surjectivity step, $F$ bijective). It is injective: $\bar C(\pi(p)) = \bar C(\pi(q))$ means $C_p = C_q$, so $p = \pm q$ and $\pi(p) = \pi(q)$. $S^3$ is compact (closed and bounded in $\mathbb{R}^4$), so $S^3/\{\pm 1\} = \mathbb{RP}^3$ (Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]) is compact as the image of $S^3$ under the continuous $\pi$; and $\mathrm{SO}(3)$ is Hausdorff, as a subspace of $\operatorname{Mat}(3, \mathbb{R}) \cong \mathbb{R}^9$. So the continuous bijection $\bar C$ is a homeomorphism (Fact [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1), (2), (6)). Finally, since $F(-q) = -F(q)$, $F$ carries each class $\{\pm q\}$ onto the class $\{\pm F(q)\}$, so it induces a bijection $S^3/\{\pm 1\} \to \mathrm{SU}(2)/\{\pm I\}$, continuous with continuous inverse by the universal property applied to the continuous maps $F$ and $F^{-1}$ followed by the quotient maps; so $F$ identifies $S^3/\{\pm 1\}$ with $\mathrm{SU}(2)/\{\pm I\}$.

^pf-44-4

*Uses:* [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]], [[§43 The Unit Quaternions and SU(2)#^prop-43-6|§43.6]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^lem-44-2|§44.2]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^lem-44-3|§44.3]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§25 The Geometric Tangent Space#^ex-25-4|Ex. §25.4]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Universal Property of Quotient Maps|590 §13.3]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!proof]+ Second proof: the conjugation map computed explicitly (the submitted solution)
>
> *(Assignment 4, Problem 3(b), as submitted, in the notation of the second proofs of Propositions [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]] and [[§43 The Unit Quaternions and SU(2)#^prop-43-6|§43.6]]; “part (a)” is the [[§43 The Unit Quaternions and SU(2)#^pf-43-6-2|second proof]] of [[§43 The Unit Quaternions and SU(2)#^prop-43-6|Proposition §43.6]]. It proves that $G$ is smooth, the formula for $G_{\ast I}(\sigma_j)$ — the three matrices it finds are $2\hat e_1$, $2\hat e_2$, $2\hat e_3$ ([[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]]) — and that $G$ is a [[§35 Local Diffeomorphisms#^def-35-1|local diffeomorphism]]; surjectivity, the two-to-one property and $\mathbb{RP}^3$ are proved above. What it takes as given from the problem is proved in Propositions [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]] and [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]]. Its proof that $F^{-1}$ is smooth is in the [[§43 The Unit Quaternions and SU(2)#^pf-43-5-2|second proof]] of [[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5]]. In $C(\vec x)$, $\vec x$ is a point of $S^3$; in the proof above, $C_q$ is the same map for $q = h(\vec x)$.)*
>
> **Reduction to the conjugation map.** Let $\mathbb{H}_0 = \{ y_1 i + y_2 j + y_3 k : y_1, y_2, y_3 \in \mathbb{R} \}$ be the purely imaginary quaternions, and identify $\mathbb{R}^3$ with $\mathbb{H}_0$ by $h_0(y_1, y_2, y_3) = h(0, y_1, y_2, y_3) = y_1 i + y_2 j + y_3 k$. For $\vec x \in S^3$, conjugation by the unit quaternion $h(\vec x)$, whose inverse is $\overline{h(\vec x)}$, defines the linear map
>
> $$
> C(\vec x) : \mathbb{R}^3 \to \mathbb{R}^3, \qquad C(\vec x)(\vec y) = h_0^{-1}\Bigl( h(\vec x)\; h_0(\vec y)\; \overline{h(\vec x)} \Bigr).
> $$
>
> As stated in the problem, $C(\vec x) \in \mathrm{SO}(3)$, and $C : S^3 \to \mathrm{SO}(3)$ is a $2$–$1$ [[§15 Homomorphisms#^def-15-1|group morphism]]; we take these facts as given.
>
> *Smoothness.* Each coordinate of the quaternion $h(\vec x)\, h_0(\vec y)\, \overline{h(\vec x)}$ is a polynomial in the variables $x_0, \ldots, x_3$ and $y_1, y_2, y_3$, quadratic in $\vec x$ and linear in $\vec y$, so each entry of the matrix $C(\vec x)$ is a quadratic polynomial in $x_0, \ldots, x_3$. Hence $C$ is the restriction to $S^3$ of a smooth map $\mathbb{R}^4 \to \mathrm{Mat}(3, \mathbb{R})$, so it is smooth as a map $S^3 \to \mathrm{Mat}(3, \mathbb{R})$ (composing with the inclusion of $S^3$), and since its image lies in the embedded submanifold $\mathrm{SO}(3)$, it is smooth as a map $S^3 \to \mathrm{SO}(3)$ ([[§37 Regular Submanifolds#^lem-37-5|Lemma §37.5]]). [The submitted proof that $F^{-1} : \mathrm{SU}(2) \to S^3$ is smooth stands here; it is now the last paragraph of the [[§43 The Unit Quaternions and SU(2)#^pf-43-5-2|second proof]] of [[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5]].] Thus
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
> *Translations are diffeomorphisms.* On $\mathrm{Mat}(2, \mathbb{C})$ the map $M \mapsto gM$ is linear, hence smooth; its restriction to the embedded submanifold $\mathrm{SU}(2)$ is smooth, and it takes values in $\mathrm{SU}(2)$ because $\mathrm{SU}(2)$ is closed under products, so $L_g : \mathrm{SU}(2) \to \mathrm{SU}(2)$ is smooth, since a smooth map whose image lies in an embedded submanifold is smooth into that submanifold ([[§37 Regular Submanifolds#^lem-37-5|Lemma §37.5]]). The same holds for $L_{g^{-1}}$, and $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$ by associativity and $g g^{-1} = g^{-1} g = I$. Hence $L_g$ is a diffeomorphism, and by the chain rule ([[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6]]) $(L_{g^{-1}})_{\ast,g} \circ (L_g)_{\ast,I} = \mathrm{id}$ and $(L_g)_{\ast,I} \circ (L_{g^{-1}})_{\ast,g} = \mathrm{id}$, so $(L_g)_{\ast,I}$ is an isomorphism with inverse $(L_{g^{-1}})_{\ast,g}$. In the same way, using that $\mathrm{SO}(3)$ is an embedded submanifold of $\mathrm{Mat}(3, \mathbb{R})$ closed under products, $L_{G(g)}$ is a diffeomorphism of $\mathrm{SO}(3)$ and $(L_{G(g)})_{\ast,I}$ is an isomorphism.
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
> **$G$ is a local diffeomorphism.** Let $g \in \mathrm{SU}(2)$. Choose a chart $(V, \chi)$ of $\mathrm{SO}(3)$ at $G(g)$ and, using continuity of $G$, a chart $(U, \varphi)$ of $\mathrm{SU}(2)$ at $g$ with $G(U) \subseteq V$. The coordinate representation $\hat G = \chi \circ G \circ \varphi^{-1} : \varphi(U) \to \chi(V)$ is a smooth map between open subsets of $\mathbb{R}^3$, and its Jacobian at $\varphi(g)$ is the matrix of $G_{\ast,g}$ in the coordinate bases ([[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2]]), hence invertible. By the inverse function theorem ([[§35 Local Diffeomorphisms#^thm-35-1|Theorem §35.1]]), there are open sets $U_0 \ni \varphi(g)$ in $\varphi(U)$ and $V_0 = \hat G(U_0) \subseteq \chi(V)$ such that $\hat G|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse. Then $\varphi^{-1}(U_0)$ is an open neighborhood of $g$, $\chi^{-1}(V_0)$ is open in $\mathrm{SO}(3)$, and
>
> $$
> G|_{\varphi^{-1}(U_0)} = \chi^{-1} \circ \hat G|_{U_0} \circ \varphi : \varphi^{-1}(U_0) \to \chi^{-1}(V_0)
> $$
>
> is a composite of diffeomorphisms, hence a diffeomorphism. As $g$ was arbitrary, $G$ is a local diffeomorphism.

^pf-44-4-2

*Uses:* [[§43 The Unit Quaternions and SU(2)#^prop-43-5|§43.5]], [[§43 The Unit Quaternions and SU(2)#^prop-43-6|§43.6]], [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]], [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[Inverse Function Theorem (several variables)|452 §16.2]]

> [!remark]- Connections
> - The same theorem in physics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; $\mathrm{SU}(2) \cong S^3$ and $\mathrm{SO}(3) \cong \mathbb{RP}^3$ topologically, with $\pi_1$: [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-8|QFT Theorem §CB.10.8]].
> - The algebraic quotient in 493: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 §41.1]]; $\mathbb{RP}^n$ as the quotient $S^n/(x \sim -x)$ in 590: [[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§52 Lie Bracket and Lie Algebra#^ex-52-3|Ex. §52.3]]; and Lie groups in [[§54 Lie Groups and Left-Invariant Vector Fields#^prop-54-1|§54.1]].

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Complex Projective Space|Complex Projective Space]], an orbit map in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; the first is the quotient map of [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; [[§42 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]] shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|The Double Cover]].

![[m591-35-2.svg]]
*(a) For $q = \cos t + \sin t\, u$, with $u \in \mathbb{H}_0$ a unit vector, $C_q(v) = q v \bar q$ fixes the axis $u$ and turns $v$ by the angle $2t$ about it, along the dashed circle traced by the tip of $v$: [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|Proposition §44.1]](3) with $\theta = 2t$. (b) Why it is two-to-one: the great circle $\gamma(t) = \cos t + \sin t\, u$ in $S^3$, drawn as a circle, is mapped by $C$ onto the loop of rotations about $u$ in $\mathrm{SO}(3)$. The antipodal points $q$ and $-q = \gamma(t + \pi)$ (red) give the same rotation $C_q = C_{-q}$, by the angle $2t$, and $\pm 1$ both give $I$ ([[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|§44.1]](2)). The first half of the circle, $t \in [0, \pi]$ (blue), already goes once around the loop of rotations, and the second half (orange) goes around it again: once around the circle is twice around the rotations, the double cover of [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|Theorem §44.4]]. (Drawn for these notes in the vault; not in the course tex.)*

> [!remark] Remark: What the Example Shows
> $G$ is a local diffeomorphism ([[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]]) that is not a diffeomorphism: locally $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are indistinguishable — their tangent spaces at $I$ are isomorphic, and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ — but globally $\mathrm{SU}(2) \cong S^3$ wraps twice around $\mathrm{SO}(3) \cong \mathbb{RP}^3$. Every fibre $G^{-1}(A) = \{\pm g\}$ is two points, and $G$ is a proper ([[§40 Embeddings#^def-40-2|Def. §40.2]]) surjective submersion ([[§36 Submersions#^def-36-1|Def. §36.1]]) onto the connected $\mathrm{SO}(3)$, so Ehresmann's theorem ([[§38 Fibrations#^thm-38-4|Theorem §38.4]], stated without proof) makes it a fibration ([[§38 Fibrations#^def-38-1|Def. §38.1]]) whose fibre is two points: a double cover. The smooth version of the last statement — that $\bar C$ is a diffeomorphism for the smooth structure of $\mathbb{RP}^3$ — needs the quotient map $S^3 \to \mathbb{RP}^3$ to be a local diffeomorphism, and is not proved here.

^rem-44-1

> [!remark]- Connections
> - The quotient map $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§42 Projective Spaces and the Hopf Fibration#^ex-42-1|Ex. §42.1]]; bijective local diffeomorphisms: [[§35 Local Diffeomorphisms#^cor-35-3|§35.3]].
> - Covering maps: [[§35 Local Diffeomorphisms#^rem-35-2|Remark: Covering Maps]]; in 590: [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]], [[Properties of the Lifting Correspondence|590 §32.4]].
