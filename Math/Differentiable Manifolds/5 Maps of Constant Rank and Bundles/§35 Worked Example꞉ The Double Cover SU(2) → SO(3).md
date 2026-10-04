---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 35
tags: [differentiable-manifolds, math591]
---
← [[§34 Embeddings]] · ↑ [[· 5 Maps of Constant Rank and Bundles]]

*Stage: maps — One example that uses everything so far: submanifolds, embeddings, local diffeomorphisms, and translation in a group.*

*From Assignment 4, Problem 3: the submitted solution, reorganized, with every claim the problem allowed us to assume now proved. References: Lee, Problems 7-22 and 7-23 (quaternions).*

The unit quaternions form a group $S^3$; acting on $\mathbb{C}^2$ they identify it with $\mathrm{SU}(2)$, and acting by conjugation on the pure imaginary quaternions $\mathbb{R}^3$ they give rotations. The result is a two-to-one local diffeomorphism $\mathrm{SU}(2) \to \mathrm{SO}(3)$, and with it $\mathrm{SO}(3) \cong \mathbb{RP}^3$.

![[m591-35-1.svg]]
*The three maps of the section: $F$ identifies unit quaternions with matrices in $\mathrm{SU}(2)$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-3|Proposition §35.3]]); $C$ is conjugation ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-5|Proposition §35.5]]); and $G = C \circ F^{-1}$ is the double cover ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-35-8|Theorem §35.8]]).*

## Quaternions and the Unit Sphere

> [!definition] Definition §35.1: Quaternions
> The **quaternions** are $\mathbb{H} = \{ q = x_0 + x_1 i + x_2 j + x_3 k : x_a \in \mathbb{R} \} \cong \mathbb{R}^4$, with the associative, bilinear multiplication determined by
>
> $$
> i^2 = j^2 = k^2 = -1, \qquad ij = -ji = k, \quad jk = -kj = i, \quad ki = -ik = j .
> $$
>
> The **conjugate** of $q$ is $\bar q = x_0 - x_1 i - x_2 j - x_3 k$, its **norm** is the Euclidean norm $|q|$ of $(x_0, \ldots, x_3)$, and $q$ is **pure imaginary** if $x_0 = 0$; the pure imaginary quaternions form $\mathbb{H}_0 \cong \mathbb{R}^3$. We identify $\mathbb{C}$ with $\{x_2 = x_3 = 0\}$.
>
> *Lee: Problem 7-22*

^def-35-1

> [!theorem] Proposition §35.1: Norm and Conjugation
> For $p, q \in \mathbb{H}$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-35-1|Def. §35.1]]): $\overline{pq} = \bar q\, \bar p$, $\ q \bar q = \bar q q = |q|^2$, and $|pq| = |p|\,|q|$. Hence every $q \neq 0$ has inverse $q^{-1} = \bar q / |q|^2$, and $S^3 = \{|q| = 1\}$ is a group ([[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]), with $q^{-1} = \bar q$.

^prop-35-1

> [!proof]+ Proof
> *(Not proved in the submitted solution, where the problem stated it; filled in.)* Both sides of $\overline{pq} = \bar q \bar p$ are real-bilinear in $(p, q)$, so it suffices to check basis elements, where it reads, for instance, $\overline{ij} = \bar k = -k$ and $\bar j \bar i = (-j)(-i) = ji = -k$. Expanding $q \bar q$, the cross terms cancel in pairs ($x_1 x_2 (-ij - ji) = 0$, and so on) and the squares give $x_0^2 + x_1^2 + x_2^2 + x_3^2$. Then $|pq|^2 = pq\, \overline{pq} = p\, q \bar q\, \bar p = |q|^2 p \bar p = |p|^2 |q|^2$, using that the real number $|q|^2$ commutes with everything. The rest follows.

^pf-35-1

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-35-1|Def. §35.1]], [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]

> [!theorem] Proposition §35.2: The Unit Quaternions
> $S^3 \subseteq \mathbb{H} = \mathbb{R}^4$ is a regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of dimension $3$ and a group ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|§35.1]]) whose multiplication and inversion are smooth ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]). It is connected ([[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]): every $q \in S^3$ other than $\pm 1$ can be written $q = \cos\theta + \sin\theta\, u$ with $\theta \in (0, \pi)$ and $u \in \mathbb{H}_0$, $|u| = 1$, and $t \mapsto \cos t + \sin t\, u$ joins $1$ to $q$ in $S^3$.

^prop-35-2

> [!proof]+ Proof
> *(The submitted solution proved the submanifold claim with hyperspherical charts; the regular value theorem is shorter. Filled in.)* $1$ is a regular value of $f(x) = |x|^2$, since $f'(x) = 2x^{\mathsf T} \neq 0$ on $S^3$, so $S^3$ is a submanifold of codimension $1$ ([[§30 Submanifolds#^thm-30-6|Theorem §30.6]]). Multiplication is polynomial in the coordinates and inversion is $q \mapsto \bar q$, linear; both are smooth into $\mathbb{R}^4$ and land in $S^3$, hence are smooth into $S^3$ ([[§30 Submanifolds#^lem-30-3|Lemma §30.3]]). For the polar form, write $q = x_0 + v$ with $v \in \mathbb{H}_0$; if $q \neq \pm 1$ then $v \neq 0$, $x_0^2 + |v|^2 = 1$, and $\theta = \arccos x_0 \in (0, \pi)$, $u = v/|v|$ work, since $|v| = \sin\theta$. The path stays in $S^3$ because $|\cos t + \sin t\, u|^2 = \cos^2 t + \sin^2 t$; and $-1$ is joined to $1$ by $t \mapsto \cos t + \sin t\, i$, $t \in [0, \pi]$.

^pf-35-2

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-35-1|Def. §35.1]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|§35.1]], [[§30 Submanifolds#^thm-30-6|§30.6]], [[§30 Submanifolds#^lem-30-3|§30.3]], [[§14 Connected Subspaces of ℝ#^thm-14-4|590 §14.4]]

> [!remark]- Connections
> - Topological groups: [[§8 Topological Groups and Classical Matrix Groups#^def-8-1|Def. §8.1]]; the sphere as a level set in 452: [[Unit circle and unit sphere|452 Unit circle and unit sphere]].
> - $S^3$ is simply connected: [[Sⁿ is Simply Connected for n ≥ 2|590 §27.3]].

## $S^3$ and $\mathrm{SU}(2)$

> [!theorem] Proposition §35.3: $S^3$ Is $\mathrm{SU}(2)$
> Identify $\mathbb{C}^2$ with $\mathbb{H}$ by $(z, w) \mapsto z + wj$, so that $\mathbb{C}$ acts by left multiplication.
> 1. For $q = a + bj$ ($a, b \in \mathbb{C}$), right multiplication $R_q(x) = xq$ is complex-linear, with matrix $\begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$; for $q \in S^3$ this matrix lies in $\mathrm{SU}(2)$ (unitary: [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]]).
> 2. $F : S^3 \to \mathrm{SU}(2)$, $F(q) =$ the matrix of $R_{q^{-1}}$, is a group isomorphism ([[§16 Isomorphisms#^def-16-1|493 Def. §16.1]]), explicitly
>
> $$
> F(x_0 + x_1 i + x_2 j + x_3 k) = \begin{pmatrix} x_0 - x_1 i & x_2 - x_3 i \\ -x_2 - x_3 i & x_0 + x_1 i \end{pmatrix}.
> $$
>
> 3. $\mathrm{SU}(2)$ is a regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of $\operatorname{Mat}(2, \mathbb{C}) \cong \mathbb{R}^8$ of dimension $3$, and $F$ is a diffeomorphism ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]).

^prop-35-3

> [!proof]+ Proof
> *(The submitted warm-up gave the matrix in (1) and (2); the problem stated the rest, and the proof of (3) is new, using [[§34 Embeddings|§34]].)* (1) Left multiplication by $c \in \mathbb{C}$ commutes with right multiplication by $q$ (associativity), so $R_q$ is complex-linear. Using $jc = \bar c\, j$ for $c \in \mathbb{C}$ and $j^2 = -1$,
>
> $$
> (z + wj)(a + bj) = za + zbj + w\bar a\, j + w \bar b\, j^2 = (az - \bar b w) + (bz + \bar a w)\, j ,
> $$
>
> which is the matrix shown. Its determinant is $|a|^2 + |b|^2 = |q|^2$; and $R_q$ preserves norms when $|q| = 1$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|Proposition §35.1]]), and the norm of $\mathbb{H}$ is the Hermitian norm of $\mathbb{C}^2$, so the matrix is unitary. Hence it lies in $\mathrm{SU}(2)$.
>
> (2) $q^{-1} = \bar q = \bar a - bj$, so (1) with $(a, b)$ replaced by $(\bar a, -b)$ gives the formula. $F$ is a homomorphism because $R_{(pq)^{-1}}(x) = x q^{-1} p^{-1} = R_{p^{-1}}(R_{q^{-1}}(x))$ — the inverse is there to make the order come out right. It is injective, since $R_{q^{-1}} = \mathrm{id}$ forces $q^{-1} = 1 \cdot q^{-1} = 1$. It is surjective: a matrix $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in \mathrm{SU}(2)$ has inverse $\begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$ (determinant $1$) equal to its conjugate transpose $\begin{pmatrix} \bar\alpha & \bar\gamma \\ \bar\beta & \bar\delta \end{pmatrix}$, so $\delta = \bar\alpha$ and $\gamma = -\bar\beta$, with $|\alpha|^2 + |\beta|^2 = 1$; this is $F(a + bj)$ for $a = \bar\alpha$, $b = \bar\beta$.
>
> (3) The formula defines an $\mathbb{R}$-linear map $L : \mathbb{R}^4 \to \operatorname{Mat}(2, \mathbb{C})$ with $F = L|_{S^3}$, and $L$ is injective (its first row determines $x$). An injective linear map is an embedding — an immersion, and a homeomorphism onto its image, with the inverse a restriction of a linear map — and so is $L|_{S^3}$, as the composite of the embeddings $S^3 \hookrightarrow \mathbb{R}^4 \xrightarrow{L} \operatorname{Mat}(2, \mathbb{C})$. Its image is $F(S^3) = \mathrm{SU}(2)$ by (2), so $\mathrm{SU}(2)$ is a regular submanifold of dimension $3$ ([[§34 Embeddings#^thm-34-1|Theorem §34.1]]) and $F$ is a diffeomorphism onto it ([[§34 Embeddings#^cor-34-3|Corollary §34.3]]).

^pf-35-3

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-35-1|Def. §35.1]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|§35.1]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]], [[§34 Embeddings#^def-34-1|Def. §34.1]], [[§34 Embeddings#^thm-34-1|§34.1]], [[§34 Embeddings#^cor-34-3|§34.3]], [[§18 The Differential of a Map Between Vector Spaces#^thm-18-3|§18.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|LADR 7.53]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]]

> [!remark]- Connections
> - $\mathrm{SU}(2)$ in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]]; unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]].
> - The unitary groups in 591: [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]], [[§19 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-19-2|Ex. §19.2]].

> [!theorem] Proposition §35.4: The Tangent Space of $\mathrm{SU}(2)$ at the Identity
> The curves $\gamma_1(t) = \cos t + \sin t\, i$, $\gamma_2(t) = \cos t + \sin t\, j$, $\gamma_3(t) = \cos t + \sin t\, k$ in $S^3$ pass through $1$ with velocities ([[§26 Tangent Vectors as Velocities of Curves#^def-26-1|Def. §26.1]]) $i, j, k$, and
>
> $$
> \sigma_1 = F_{\ast 1}(i) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}, \qquad
> \sigma_2 = F_{\ast 1}(j) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad
> \sigma_3 = F_{\ast 1}(k) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}.
> $$
>
> They form a basis of $T_I\,\mathrm{SU}(2) = \mathfrak{su}(2) = \{ X \in \operatorname{Mat}(2, \mathbb{C}) : X^{\ast} = -X,\ \operatorname{tr} X = 0 \}$.

^prop-35-4

> [!proof]+ Proof
> *(The submitted solution computed the $\sigma_j$ — “use curves, not coordinates”, as the problem's hint said; the identification of the tangent space is filled in.)* By the chain rule for curves ([[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|Corollary §26.3]]), $F_{\ast 1}(\gamma_j'(0)) = (F \circ \gamma_j)'(0)$, the entrywise derivative of
>
> $$
> F(\gamma_1(t)) = \begin{pmatrix} e^{-it} & 0 \\ 0 & e^{it} \end{pmatrix}, \quad
> F(\gamma_2(t)) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}, \quad
> F(\gamma_3(t)) = \begin{pmatrix} \cos t & -i\sin t \\ -i\sin t & \cos t \end{pmatrix}
> $$
>
> at $t = 0$. The three matrices are linearly independent (compare the $(1,1)$, $(1,2)$ and $(2,1)$ entries), and $T_I\,\mathrm{SU}(2)$ has dimension $3$ ([[§24 Coordinate Derivations and the Basis Theorem#^thm-24-8|Theorem §24.8]]), so they are a basis. Each lies in $\mathfrak{su}(2)$, which has real dimension $3$: a skew-Hermitian $2 \times 2$ matrix has imaginary diagonal and $x_{21} = -\bar x_{12}$, four real parameters, and $\operatorname{tr} X = 0$ removes one. So $T_I\,\mathrm{SU}(2) = \operatorname{Span}\{\sigma_j\} = \mathfrak{su}(2)$.

^pf-35-4

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-3|§35.3]], [[§26 Tangent Vectors as Velocities of Curves#^def-26-1|Def. §26.1]], [[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|§26.3]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-8|§24.8]], [[§30 Submanifolds#^prop-30-4|§30.4]]

> [!remark]- Connections
> - The tangent space of $\mathrm{U}(n)$ at the identity: [[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-3|Ex. §20.3]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]].
> - The Pauli matrices in Quantum Mechanics: [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].

## Conjugation and Rotations

> [!theorem] Proposition §35.5: Conjugation by Unit Quaternions Is Rotation
> For $q \in S^3$, the map $C_q(v) = q v \bar q$ sends $\mathbb{H}_0 \cong \mathbb{R}^3$ to itself, and:
> 1. $C_q \in \mathrm{SO}(3)$ ([[§8 Topological Groups and Classical Matrix Groups#^def-8-7|Def. §8.7]]), and $C : S^3 \to \mathrm{SO}(3)$, $q \mapsto C_q$, is a smooth ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]);
> 2. $\ker C = \{\pm 1\}$ ([[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]), so $C_p = C_q$ if and only if $p = \pm q$;
> 3. if $u \in \mathbb{H}_0$ is a unit vector and $\theta \in \mathbb{R}$, then $C_q$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ is the rotation by the angle $\theta$ about the axis $u$.

^prop-35-5

> [!proof]+ Proof
> *(The problem stated (1) and the two-to-one property without proof; filled in. Part (3) contains the submitted computation: for $q = \gamma_j(t)$ it gives the rotation by $2t$ about $e_j$.)* A quaternion $v$ is pure imaginary iff $\bar v = -v$, and then $\overline{q v \bar q} = q \bar v \bar q = -q v \bar q$, so $C_q(v) \in \mathbb{H}_0$; and $|C_q(v)| = |v|$ by [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|Proposition §35.1]]. So $C_q$ is a linear isometry of $\mathbb{R}^3$, $C_q \in \mathrm{O}(3)$.
>
> (1) $C_{pq}(v) = pq v \bar q \bar p = C_p(C_q(v))$. The entries of $C_q$ are quadratic polynomials in the coordinates of $q$, so $C$ is smooth into $\operatorname{Mat}(3, \mathbb{R})$, with values in the submanifold $\mathrm{O}(3)$ ([[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|Theorem §20.5]]). $\det \circ C : S^3 \to \{\pm 1\}$ is continuous on the connected $S^3$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-2|Proposition §35.2]]) and equals $1$ at $q = 1$, so $C$ takes values in $\mathrm{SO}(3)$, an open subset of $\mathrm{O}(3)$; hence $C$ is smooth into $\mathrm{SO}(3)$ ([[§30 Submanifolds#^lem-30-3|Lemma §30.3]]).
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

^pf-35-5

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-35-1|Def. §35.1]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-1|§35.1]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-2|§35.2]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-6|Def. §8.6]], [[§8 Topological Groups and Classical Matrix Groups#^prop-8-7|§8.7]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-7|Def. §8.7]], [[§8 Topological Groups and Classical Matrix Groups#^prop-8-3|§8.3]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]], [[§30 Submanifolds#^lem-30-3|§30.3]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[Continuous Image of a Connected Space is Connected|590 §13.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]

> [!remark]- Connections
> - The half-angle in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - Isometries in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]; the kernel $\{\pm 1\}$ as a center in 493: [[§33 The Center#^def-33-1|493 Def. §33.1]].

The half-angle in (3) is the source of the factor $2$ below: the curve $\gamma_j(t)$ through $1$ moves at unit speed in $S^3$, but its image rotates by $2t$.

> [!theorem] Lemma §35.6: Every Rotation Has an Axis
> Every $A \in \mathrm{SO}(3)$ ([[§8 Topological Groups and Classical Matrix Groups#^def-8-7|Def. §8.7]]) is the rotation by some angle $\theta$ about some unit axis $u$.

^lem-35-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $\det(A - I) = \det(A - A A^{\mathsf T}) = \det A \, \det(I - A^{\mathsf T}) = \det(I - A) = -\det(A - I)$, the last step because $3$ is odd. So $\det(A - I) = 0$, and $Au = u$ for some unit $u$. $A$ preserves $u^\perp$ and restricts to an orientation-preserving isometry of that plane, a rotation by some $\theta$.

^pf-35-6

*Uses:* [[§8 Topological Groups and Classical Matrix Groups#^def-8-7|Def. §8.7]], [[§8 Topological Groups and Classical Matrix Groups#^prop-8-7|§8.7]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§34 Determinants#^ladr-9-56|LADR 9.56]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]]

> [!remark]- Connections
> - Rotations in Quantum Mechanics, by Euler angles: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-2|QM Def. §C5.2.2]]; isometries in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

## The Double Cover

> [!theorem] Lemma §35.7: Translating the Differential
> Let $G : H \to K$ be a smooth ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) between groups of matrices that are regular submanifolds ([[§30 Submanifolds#^def-30-1|Def. §30.1]]), closed under products and inverses. For $h \in H$ let $L_h(x) = hx$. Then for every $g \in H$,
>
> $$
> G_{\ast g} = (L_{G(g)})_{\ast I} \circ G_{\ast I} \circ (L_{g^{-1}})_{\ast g} ,
> $$
>
> and each $(L_h)_{\ast}$ is an isomorphism. In particular, if $G_{\ast I}$ is an isomorphism, so is every $G_{\ast g}$.

^lem-35-7

> [!proof]+ Proof
> *(The submitted solution's argument, isolated as a lemma.)* $L_h$ is the restriction of the linear map $x \mapsto hx$, so it is smooth ([[§30 Submanifolds#^lem-30-3|Lemma §30.3]]), with smooth inverse $L_{h^{-1}}$: a diffeomorphism, so its differentials are isomorphisms ([[§23 Derivations and the Abstract Tangent Space#^thm-23-6|chain rule]]). $G$ is a homomorphism, so $G \circ L_g = L_{G(g)} \circ G$; differentiating at $I$ gives $G_{\ast g} \circ (L_g)_{\ast I} = (L_{G(g)})_{\ast I} \circ G_{\ast I}$, and $(L_g)_{\ast I}^{-1} = (L_{g^{-1}})_{\ast g}$.

^pf-35-7

*Uses:* [[§30 Submanifolds#^lem-30-3|§30.3]], [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!remark]- Connections
> - The geometric version for the classical groups, $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$: [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-5|§20.5]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-7|Remark: Left and Right Translates]].

This is the left translation of the [[§20 Tangent Spaces I꞉ The Geometric Picture#^rem-20-7|discussion of moving base points]]: in a group, translation carries the tangent space at $I$ to the tangent space at every $g$, so what happens at the identity happens everywhere.

> [!theorem] Theorem §35.8: The Double Cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$
> $G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a surjective smooth group homomorphism and a local diffeomorphism ([[§28 Local Diffeomorphisms#^def-28-1|Def. §28.1]]), with
>
> $$
> G_{\ast I}(\sigma_j) = 2\,\hat e_j \qquad (j = 1, 2, 3),
> $$
>
> twice the basis of $\operatorname{Skew}(3, \mathbb{R}) = T_I\,\mathrm{SO}(3)$ given by the hat map ([[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-3|Def. §20.3]]). It is two-to-one: $G(g) = G(h)$ iff $h = \pm g$. Consequently $G$ induces a homeomorphism ([[§9 Continuous Functions#^def-9-2|590 Def. §9.2]])
>
> $$
> \mathrm{SO}(3) \;\cong\; \mathrm{SU}(2)/\{\pm I\} \;\cong\; S^3/\{\pm 1\} \;=\; \mathbb{RP}^3 .
> $$

^thm-35-8

> [!proof]+ Proof
> *(The submitted solution computed $G_{\ast I}(\sigma_j)$ and proved the local diffeomorphism; surjectivity, the two-to-one property and the identification with $\mathbb{RP}^3$ are filled in.)* $G$ is a smooth homomorphism, as a composite of $F^{-1}$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-3|Proposition §35.3]]) and $C$.
>
> *The differential at $I$.* By the chain rule $G_{\ast I}(\sigma_j) = G_{\ast I}(F_{\ast 1}(\gamma_j'(0))) = C_{\ast 1}(\gamma_j'(0)) = (C \circ \gamma_j)'(0)$, and by [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-5|Proposition §35.5]](3) with $\theta = 2t$, $C(\gamma_j(t))$ is the rotation by $2t$ about $e_j$; for $j = 1$,
>
> $$
> C(\gamma_1(t)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2t & -\sin 2t \\ 0 & \sin 2t & \cos 2t \end{pmatrix}, \qquad \frac{d}{dt}\Big|_{t=0} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix} = 2\,\hat e_1 ,
> $$
>
> and likewise for $j = 2, 3$ ([[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-3|Definition §20.3]]). The $\hat e_j$ are a basis of $T_I\,\mathrm{SO}(3) = \operatorname{Skew}(3, \mathbb{R})$ ([[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-4|Example §20.4]]), so $G_{\ast I}$ is an isomorphism.
>
> *Local diffeomorphism.* By [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-35-7|Lemma §35.7]] every $G_{\ast g}$ is an isomorphism, so $G$ is a local diffeomorphism ([[§28 Local Diffeomorphisms#^thm-28-2|Theorem §28.2]]).
>
> *Surjective.* By [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-35-6|Lemma §35.6]], an element of $\mathrm{SO}(3)$ is a rotation by some $\theta$ about some $u$, which is $C_q = G(F(q))$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ by [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-5|Proposition §35.5]](3).
>
> *Two-to-one.* $G(g) = G(h)$ iff $C_{F^{-1}(g)} = C_{F^{-1}(h)}$ iff $F^{-1}(h) = \pm F^{-1}(g)$ ([[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-5|Proposition §35.5]](2)) iff $h = \pm g$, since $F$ is a homomorphism with $F(-1) = -I$.
>
> *$\mathbb{RP}^3$.* $C$ is constant on the classes $\{\pm q\}$, so it induces a map $\bar C : S^3/\{\pm 1\} \to \mathrm{SO}(3)$, continuous by the [[§5 Quotient Maps#^cor-5-2|universal property of the quotient]], and bijective by the last two steps. $S^3/\{\pm 1\} = \mathbb{RP}^3$ ([[§14 Projective Spaces as Smooth Manifolds#^cor-14-5|Corollary §14.5]]) is compact as the image of $S^3$, and $\mathrm{SO}(3)$ is Hausdorff, so $\bar C$ is a homeomorphism ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]); and $F$ identifies $S^3/\{\pm 1\}$ with $\mathrm{SU}(2)/\{\pm I\}$.

^pf-35-8

*Uses:* [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-3|§35.3]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-4|§35.4]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-5|§35.5]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-35-6|§35.6]], [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-35-7|§35.7]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|§26.3]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-3|Def. §20.3]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^ex-20-4|Ex. §20.4]], [[§28 Local Diffeomorphisms#^thm-28-2|§28.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[§14 Projective Spaces as Smooth Manifolds#^cor-14-5|§14.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Universal Property of Quotient Maps|590 §12.3]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!remark]- Connections
> - The same theorem in physics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; $\mathrm{SU}(2) \cong S^3$ and $\mathrm{SO}(3) \cong \mathbb{RP}^3$ topologically, with $\pi_1$: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|QFT Theorem §C3.1.8]].
> - The algebraic quotient in 493: [[§38 The First Isomorphism Theorem#^thm-38-1|493 §38.1]]; $\mathbb{RP}^n$ as the quotient $S^n/(x \sim -x)$ in 590: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 Def. §28.2]].

> [!remark] Remark: What the Example Shows
> $G$ is a local diffeomorphism ([[§28 Local Diffeomorphisms#^def-28-1|Def. §28.1]]) that is not a diffeomorphism: locally $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are indistinguishable — their tangent spaces at $I$ are isomorphic, and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ — but globally $\mathrm{SU}(2) \cong S^3$ wraps twice around $\mathrm{SO}(3) \cong \mathbb{RP}^3$. Every fibre $G^{-1}(A) = \{\pm g\}$ is two points, and $G$ is a proper ([[§34 Embeddings#^def-34-2|Def. §34.2]]) surjective submersion ([[§29 Submersions#^def-29-1|Def. §29.1]]) onto the connected $\mathrm{SO}(3)$, so Ehresmann's theorem ([[§31 Fibrations#^thm-31-3|Theorem §31.3]], stated without proof) makes it a fibration ([[§31 Fibrations#^def-31-1|Def. §31.1]]) whose fibre is two points: a double cover. The smooth version of the last statement — that $\bar C$ is a diffeomorphism for the smooth structure of $\mathbb{RP}^3$ — needs the quotient map $S^3 \to \mathbb{RP}^3$ to be a local diffeomorphism, and is not proved here.

^rem-35-1

> [!remark]- Connections
> - The quotient map $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§28 Local Diffeomorphisms#^ex-28-2|Ex. §28.2]]; bijective local diffeomorphisms: [[§28 Local Diffeomorphisms#^cor-28-3|§28.3]].
> - Covering maps: [[§28 Local Diffeomorphisms#^rem-28-2|Remark: Covering Maps]]; in 590: [[§24 Covering Spaces#^def-24-2|590 Def. §24.2]], [[Properties of the Lifting Correspondence|590 §24.9]].
