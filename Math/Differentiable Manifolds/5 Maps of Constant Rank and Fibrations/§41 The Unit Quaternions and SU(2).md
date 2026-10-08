---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 41
tags: [differentiable-manifolds, math591]
---
← [[§40 Projective Spaces and the Hopf Fibration]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§42 SU(2) → SO(3)꞉ The Double Cover]] →

*Stage: maps — The unit quaternions $S^3$: a submanifold of $\mathbb{R}^4$, a group, and the matrix group $\mathrm{SU}(2)$, with its tangent space at the identity.*

*From Assignment 4, Problem 3: the submitted solution, reorganized, with every claim the problem allowed us to assume now proved. References: Lee, Problems 7-22 and 7-23 (quaternions).*

The unit quaternions form a group $S^3$; acting on $\mathbb{C}^2$ they identify it with $\mathrm{SU}(2)$. The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ built from them is [[§42 SU(2) → SO(3)꞉ The Double Cover|§42]].

## Quaternions and the Unit Sphere

> [!definition] Definition §41.1: Quaternions
> The **quaternions** are $\mathbb{H} = \{ q = x_0 + x_1 i + x_2 j + x_3 k : x_a \in \mathbb{R} \} \cong \mathbb{R}^4$, with the associative, bilinear multiplication determined by
>
> $$
> i^2 = j^2 = k^2 = -1, \qquad ij = -ji = k, \quad jk = -kj = i, \quad ki = -ik = j .
> $$
>
> The **conjugate** of $q$ is $\bar q = x_0 - x_1 i - x_2 j - x_3 k$, its **norm** is the Euclidean norm $|q|$ of $(x_0, \ldots, x_3)$, and $q$ is **pure imaginary** if $x_0 = 0$; the pure imaginary quaternions form $\mathbb{H}_0 \cong \mathbb{R}^3$. We identify $\mathbb{C}$ with $\{x_2 = x_3 = 0\}$.
>
> *Lee: Problem 7-22*

^def-41-1

> [!theorem] Proposition §41.1: Norm and Conjugation
> For $p, q \in \mathbb{H}$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]]): $\overline{pq} = \bar q\, \bar p$, $\ q \bar q = \bar q q = |q|^2$, and $|pq| = |p|\,|q|$. Hence every $q \neq 0$ has inverse $q^{-1} = \bar q / |q|^2$, and $S^3 = \{|q| = 1\}$ is a group ([[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]), with $q^{-1} = \bar q$.

^prop-41-1

> [!proof]+ Proof
> *(Not proved in the submitted solution, where the problem stated it; filled in.)* Both sides of $\overline{pq} = \bar q \bar p$ are real-bilinear in $(p, q)$, so it suffices to check basis elements, where it reads, for instance, $\overline{ij} = \bar k = -k$ and $\bar j \bar i = (-j)(-i) = ji = -k$. Expanding $q \bar q$, the cross terms cancel in pairs ($x_1 x_2 (-ij - ji) = 0$, and so on) and the squares give $x_0^2 + x_1^2 + x_2^2 + x_3^2$. Then $|pq|^2 = pq\, \overline{pq} = p\, q \bar q\, \bar p = |q|^2 p \bar p = |p|^2 |q|^2$, using that the real number $|q|^2$ commutes with everything. The rest follows.

^pf-41-1

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]], [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]

> [!definition] Definition §41.2: Hyperspherical Coordinates
> Points of $\mathbb{H} = \mathbb{R}^4$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]]) are written $\vec x = (x_0, x_1, x_2, x_3)$, and the standard basis vectors are $\vec e_0, \ldots, \vec e_3$. Throughout, $c_k = \cos\theta_k$ and $s_k = \sin\theta_k$. The **hyperspherical coordinates** $(r, \theta_1, \theta_2, \theta_3)$ on $\mathbb{R}^4$ (cf. [[Polar and spherical coordinates|452: polar and spherical coordinates]]) are given by the map $\Phi$ below. Let
>
> $$
> \Phi : (0, \infty) \times \mathbb{R}^3 \to \mathbb{R}^4, \qquad \Phi(r, \theta_1, \theta_2, \theta_3) = \bigl( r c_1,\ r s_1 c_2,\ r s_1 s_2 c_3,\ r s_1 s_2 s_3 \bigr).
> $$
>
> It is smooth, and using $c_k^2 + s_k^2 = 1$ three times, $|\Phi(r, \theta)|^2 = r^2\bigl(c_1^2 + s_1^2 c_2^2 + s_1^2 s_2^2\bigr) = r^2\bigl(c_1^2 + s_1^2\bigr) = r^2$, so $|\Phi(r, \theta)| = r$.

^def-41-2

> [!theorem] Lemma §41.2: The Jacobian of Hyperspherical Coordinates
> The map $\Phi$ of [[§41 The Unit Quaternions and SU(2)#^def-41-2|Definition §41.2]] has [[§7 The Regular Value Theorem#^def-7-1|Jacobian]] determinant
>
> $$
> \det \Phi'(r, \theta) = r^3 \sin^2\theta_1 \, \sin\theta_2 .
> $$
>
> For $r = 1$ it vanishes exactly when $\sin\theta_1 = 0$ or $\sin\theta_2 = 0$, and then $\Phi(1, \theta)$ lies on the circle
>
> $$
> B = \{ \vec x \in S^3 : x_2 = x_3 = 0 \}.
> $$

^lem-41-2

> [!proof]+ Proof
> *(Assignment 4, Problem 3(a), as submitted.)* With columns indexed by $r, \theta_1, \theta_2, \theta_3$,
>
> $$
> \Phi'(r, \theta) = \begin{pmatrix}
> c_1 & -r s_1 & 0 & 0 \\
> s_1 c_2 & r c_1 c_2 & -r s_1 s_2 & 0 \\
> s_1 s_2 c_3 & r c_1 s_2 c_3 & r s_1 c_2 c_3 & -r s_1 s_2 s_3 \\
> s_1 s_2 s_3 & r c_1 s_2 s_3 & r s_1 c_2 s_3 & r s_1 s_2 c_3
> \end{pmatrix}.
> $$
>
> Replacing rows $R_3, R_4$ by $c_3 R_3 + s_3 R_4 = (s_1 s_2,\ r c_1 s_2,\ r s_1 c_2,\ 0)$ and $-s_3 R_3 + c_3 R_4 = (0, 0, 0, r s_1 s_2)$ multiplies by a rotation and does not change the determinant; expanding along the last column, then doing the same with rows $2, 3$ of the remaining $3 \times 3$ matrix and the angle $\theta_2$, which turns them into $(s_1, r c_1, 0)$ and $(0, 0, r s_1)$,
>
> $$
> \det \Phi'(r, \theta) = r s_1 s_2 \det \begin{pmatrix} c_1 & -r s_1 & 0 \\ s_1 & r c_1 & 0 \\ 0 & 0 & r s_1 \end{pmatrix} = r s_1 s_2 \cdot r s_1 \cdot r = r^3 \sin^2\theta_1 \, \sin\theta_2 .
> $$
>
> For $r = 1$ it vanishes exactly when $\sin\theta_1 = 0$, where $\Phi(1, \theta) = (\pm 1, 0, 0, 0)$, or $\sin\theta_2 = 0$, where $\Phi(1, \theta) = (c_1, \pm s_1, 0, 0)$. In both cases $\Phi(1, \theta)$ lies on the circle
>
> $$
> B = \{ \vec x \in S^3 : x_2 = x_3 = 0 \}.
> $$

^pf-41-2

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-2|Def. §41.2]], [[§37 Determinants#^ladr-9-49|LADR 9.49]]

> [!theorem] Proposition §41.3: Hyperspherical Charts Are Adapted to $S^3$
> Let $\Phi$ and $B$ be as in [[§41 The Unit Quaternions and SU(2)#^def-41-2|Definition §41.2]] and [[§41 The Unit Quaternions and SU(2)#^lem-41-2|Lemma §41.2]]. Every $p \in S^3$ lies in the domain of a chart of $\mathbb{R}^4$ adapted to $S^3$ ([[§35 Regular Submanifolds#^def-35-2|Definition §35.2]]):
> 1. if $p \notin B$, then $p = \Phi(1, \theta)$ for some $\theta$, and for a suitable open $W \ni (1, \theta)$ in $(0, \infty) \times \mathbb{R}^3$ the map $\psi_p = \tau \circ (\Phi|_W)^{-1}$, where $\tau(r, \theta_1, \theta_2, \theta_3) = (\theta_1, \theta_2, \theta_3, r - 1)$, is such a chart, with last coordinate $y^4 = r - 1$;
> 2. if $p \in B$, the same construction with $\tilde\Phi = P \circ \Phi$ in place of $\Phi$, where $P(x_0, x_1, x_2, x_3) = (x_2, x_3, x_0, x_1)$, gives such a chart.

^prop-41-3

> [!proof]+ Proof
> *(Assignment 4, Problem 3(a), as submitted.)* Steps (i) and (ii) of the submitted solution are [[§41 The Unit Quaternions and SU(2)#^def-41-2|Definition §41.2]] and [[§41 The Unit Quaternions and SU(2)#^lem-41-2|Lemma §41.2]]. By the definition from lecture ([[§35 Regular Submanifolds#^def-35-1|Definition §35.1]]), we must show that every $p \in S^3$ lies in the domain of a chart $(U, \psi = (y^1, y^2, y^3, y^4))$ of $\mathbb{R}^4$ with
>
> $$
> U \cap S^3 = \{ \vec u \in U : y^4(\vec u) = 0 \};
> $$
>
> such a chart is *adapted* to $S^3$. Any [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] from an open subset of $\mathbb{R}^4$ onto an open subset of $\mathbb{R}^4$ is a chart of the standard smooth structure ([[§34 Submersions#^lem-34-3|Lemma §34.3]]).
>
> *(iii) Inverting $\Phi$ off $B$.* Let $p = (x_0, x_1, x_2, x_3) \in S^3 \setminus B$, so $x_2^2 + x_3^2 > 0$. Since $x_0^2 = 1 - x_1^2 - x_2^2 - x_3^2 < 1$, there is $\theta_1 \in (0, \pi)$ with $c_1 = x_0$, and then $s_1 = \sqrt{1 - x_0^2} > 0$. Since $(x_1/s_1)^2 = x_1^2 / (x_1^2 + x_2^2 + x_3^2) < 1$, there is $\theta_2 \in (0, \pi)$ with $c_2 = x_1/s_1$, and then $s_2 > 0$. Now $x_2^2 + x_3^2 = 1 - c_1^2 - s_1^2 c_2^2 = s_1^2 s_2^2$, so $(x_2, x_3)/(s_1 s_2)$ lies on the unit circle and equals $(c_3, s_3)$ for some $\theta_3$. Then $\Phi(1, \theta) = p$ and $\det \Phi'(1, \theta) = s_1^2 s_2 \neq 0$ ([[§41 The Unit Quaternions and SU(2)#^lem-41-2|Lemma §41.2]]).
>
> *(iv) Adapted charts off $B$.* With $p$ and $\theta$ as in (iii), the inverse function theorem ([[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1]]) gives an open $W \ni (1, \theta)$ in $(0, \infty) \times \mathbb{R}^3$ such that $U_p = \Phi(W)$ is open and $\Phi|_W : W \to U_p$ is a diffeomorphism. Let
>
> $$
> \psi_p = \tau \circ (\Phi|_W)^{-1}, \qquad \tau(r, \theta_1, \theta_2, \theta_3) = (\theta_1, \theta_2, \theta_3, r - 1),
> $$
>
> a diffeomorphism onto the open set $\tau(W)$, hence a chart about $p$, with last component $y^4 = r - 1$. For $\vec u = \Phi(r, \theta') \in U_p$ we have $|\vec u| = r$ by (i), so $\vec u \in S^3 \iff r = 1 \iff y^4(\vec u) = 0$. Thus $\psi_p$ is adapted to $S^3$.
>
> *(v) Adapted charts on $B$.* Let $P(x_0, x_1, x_2, x_3) = (x_2, x_3, x_0, x_1)$, a linear [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|isometry]] of $\mathbb{R}^4$ with $\det P = \pm 1$, and $\tilde\Phi = P \circ \Phi$. Then $|\tilde\Phi(r, \theta)| = r$ and $\det \tilde\Phi' = \det P \cdot \det \Phi'$, so (i)–(iv) hold for $\tilde\Phi$ with $B$ replaced by $P(B) = \{ \vec x \in S^3 : x_0 = x_1 = 0 \}$, the angles for $p$ being those of $P^{-1}p$. A point of $B \cap P(B)$ would be $0 \notin S^3$, so $B \cap P(B) = \emptyset$, and every $p \in B$ gets an adapted chart from $\tilde\Phi$.
>
> Hence every point of $S^3$ lies in an adapted chart.

^pf-41-3

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-2|Def. §41.2]], [[§41 The Unit Quaternions and SU(2)#^lem-41-2|§41.2]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§34 Submersions#^lem-34-3|§34.3]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[Inverse Function Theorem (several variables)|452 §16.2]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]]

> [!theorem] Proposition §41.4: The Unit Quaternions
> $S^3 \subseteq \mathbb{H} = \mathbb{R}^4$ is a regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) of dimension $3$ and a group ([[§41 The Unit Quaternions and SU(2)#^prop-41-1|§41.1]]) whose multiplication and inversion are smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]). It is connected ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]): every $q \in S^3$ other than $\pm 1$ can be written $q = \cos\theta + \sin\theta\, u$ with $\theta \in (0, \pi)$ and $u \in \mathbb{H}_0$, $|u| = 1$, and $t \mapsto \cos t + \sin t\, u$ joins $1$ to $q$ in $S^3$.

^prop-41-4

> [!proof]+ Proof
> *(The submitted solution proved the submanifold claim with hyperspherical charts; the regular value theorem is shorter. Filled in; the submitted proof follows.)* $1$ is a regular value of $f(x) = |x|^2$, since $f'(x) = 2x^{\mathsf T} \neq 0$ on $S^3$, so $S^3$ is a submanifold of codimension $1$ ([[§35 Regular Submanifolds#^thm-35-7|Theorem §35.7]]). Multiplication is polynomial in the coordinates and inversion is $q \mapsto \bar q$, linear; both are smooth into $\mathbb{R}^4$ and land in $S^3$, hence are smooth into $S^3$ ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]]). For the polar form, write $q = x_0 + v$ with $v \in \mathbb{H}_0$; if $q \neq \pm 1$ then $v \neq 0$, $x_0^2 + |v|^2 = 1$, and $\theta = \arccos x_0 \in (0, \pi)$, $u = v/|v|$ work, since $|v| = \sin\theta$. The path stays in $S^3$ because $|\cos t + \sin t\, u|^2 = \cos^2 t + \sin^2 t$; and $-1$ is joined to $1$ by $t \mapsto \cos t + \sin t\, i$, $t \in [0, \pi]$.

^pf-41-4

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]], [[§41 The Unit Quaternions and SU(2)#^prop-41-1|§41.1]], [[§35 Regular Submanifolds#^thm-35-7|§35.7]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§16 Connected Subspaces of ℝ#^thm-16-4|590 §16.4]]

> [!proof]+ Second proof of the submanifold claim: hyperspherical charts (the submitted solution)
>
> *(Assignment 4, Problem 3(a), as submitted. An “embedded submanifold” is a submanifold in the sense of [[§35 Regular Submanifolds#^def-35-1|Definition §35.1]]. The group and connectedness claims are proved above.)* **$S^3$ is an embedded submanifold of $\mathbb{R}^4$.** By [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3]], every point of $S^3$ lies in a chart of $\mathbb{R}^4$ adapted to $S^3$, so $S^3$ is a submanifold of $\mathbb{R}^4$ of codimension $1$ ([[§35 Regular Submanifolds#^def-35-1|Definition §35.1]]).

^pf-41-4-2

*Uses:* [[§41 The Unit Quaternions and SU(2)#^prop-41-3|§41.3]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]]

> [!remark]- Connections
> - Topological groups: [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def. §11.1]]; the sphere as a level set in 452: [[Unit circle and unit sphere|452 Unit circle and unit sphere]].
> - $S^3$ is simply connected: [[Sⁿ is Simply Connected for n ≥ 2|590 §37.3]].

## $S^3$ and $\mathrm{SU}(2)$

> [!theorem] Proposition §41.5: $S^3$ Is $\mathrm{SU}(2)$
> Identify $\mathbb{C}^2$ with $\mathbb{H}$ by $(z, w) \mapsto z + wj$, so that $\mathbb{C}$ acts by left multiplication.
> 1. For $q = a + bj$ ($a, b \in \mathbb{C}$), right multiplication $R_q(x) = xq$ is complex-linear, with matrix $\begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$; for $q \in S^3$ this matrix lies in $\mathrm{SU}(2)$ (unitary: [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]]).
> 2. $F : S^3 \to \mathrm{SU}(2)$, $F(q) =$ the matrix of $R_{q^{-1}}$, is a group isomorphism ([[§16 Isomorphisms#^def-16-1|493 Def. §16.1]]), explicitly
>
> $$
> F(x_0 + x_1 i + x_2 j + x_3 k) = \begin{pmatrix} x_0 - x_1 i & x_2 - x_3 i \\ -x_2 - x_3 i & x_0 + x_1 i \end{pmatrix}.
> $$
>
> 3. $\mathrm{SU}(2)$ is a regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) of $\operatorname{Mat}(2, \mathbb{C}) \cong \mathbb{R}^8$ of dimension $3$, and $F$ is a diffeomorphism ([[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]).

^prop-41-5

> [!proof]+ Proof
> *(The submitted warm-up gave the matrix in (1) and (2); the problem stated the rest, and the proof of (3) is new, using [[§38 Embeddings|§38]]; the submitted proof of (3), with adapted charts, follows.)* (1) Left multiplication by $c \in \mathbb{C}$ commutes with right multiplication by $q$ (associativity), so $R_q$ is complex-linear. Using $jc = \bar c\, j$ for $c \in \mathbb{C}$ and $j^2 = -1$,
>
> $$
> (z + wj)(a + bj) = za + zbj + w\bar a\, j + w \bar b\, j^2 = (az - \bar b w) + (bz + \bar a w)\, j ,
> $$
>
> which is the matrix shown. Its determinant is $|a|^2 + |b|^2 = |q|^2$; and $R_q$ preserves norms when $|q| = 1$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-1|Proposition §41.1]]), and the norm of $\mathbb{H}$ is the Hermitian norm of $\mathbb{C}^2$, so the matrix is unitary. Hence it lies in $\mathrm{SU}(2)$.
>
> (2) $q^{-1} = \bar q = \bar a - bj$, so (1) with $(a, b)$ replaced by $(\bar a, -b)$ gives the formula. $F$ is a homomorphism because $R_{(pq)^{-1}}(x) = x q^{-1} p^{-1} = R_{p^{-1}}(R_{q^{-1}}(x))$ — the inverse is there to make the order come out right. It is injective, since $R_{q^{-1}} = \mathrm{id}$ forces $q^{-1} = 1 \cdot q^{-1} = 1$. It is surjective: a matrix $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in \mathrm{SU}(2)$ has inverse $\begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$ (determinant $1$) equal to its conjugate transpose $\begin{pmatrix} \bar\alpha & \bar\gamma \\ \bar\beta & \bar\delta \end{pmatrix}$, so $\delta = \bar\alpha$ and $\gamma = -\bar\beta$, with $|\alpha|^2 + |\beta|^2 = 1$; this is $F(a + bj)$ for $a = \bar\alpha$, $b = \bar\beta$.
>
> (3) The formula defines an $\mathbb{R}$-linear map $L : \mathbb{R}^4 \to \operatorname{Mat}(2, \mathbb{C})$ with $F = L|_{S^3}$, and $L$ is injective (its first row determines $x$). An injective linear map is an embedding — an immersion, and a homeomorphism onto its image, with the inverse a restriction of a linear map — and so is $L|_{S^3}$, as the composite of the embeddings $S^3 \hookrightarrow \mathbb{R}^4 \xrightarrow{L} \operatorname{Mat}(2, \mathbb{C})$. Its image is $F(S^3) = \mathrm{SU}(2)$ by (2), so $\mathrm{SU}(2)$ is a regular submanifold of dimension $3$ ([[§38 Embeddings#^thm-38-1|Theorem §38.1]]) and $F$ is a diffeomorphism onto it ([[§38 Embeddings#^cor-38-3|Corollary §38.3]]).

^pf-41-5

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]], [[§41 The Unit Quaternions and SU(2)#^prop-41-1|§41.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]], [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§38 Embeddings#^thm-38-1|§38.1]], [[§38 Embeddings#^cor-38-3|§38.3]], [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|LADR 7.53]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]]

> [!proof]+ Second proof of (3): adapted charts (the submitted solution)
>
> *(Assignment 4, Problem 3, as submitted: its notation and setup, its proof that $\mathrm{SU}(2)$ is a submanifold and $F$ is smooth, and, moved here from its part (b), its proof that $F^{-1}$ is smooth; together they give (3). The adapted charts of $\mathbb{R}^4$ are those of [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3]]. What the submitted solution takes from the problem — that $F$ is a bijection onto $\mathrm{SU}(2)$, and that $\mathrm{SO}(3)$ is a submanifold of dimension $3$ — is proved in (2) above and in [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]].)*
>
> **Notation.** The problem writes $dF_p$ for the differential of a smooth map $F$ at a point $p$. As in lecture and in Problem 1 ([[§30 The Differential in Coordinates#^prop-30-9|Proposition §30.9]]), we write $F_{\ast,p}$ instead, so that $dF_p = F_{\ast,p}$. Since we work in $\mathbb{R}^4$ (see below), the problem's point $1 \in S^3$ is $\vec e_0$; thus the problem's $T_1 S^3$, $\sigma_j = dF_1(\vec e_j)$ and $dG_I(\sigma_j)$ are, in our notation, $T_{\vec e_0} S^3$, $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ and $G_{\ast,I}(\sigma_j)$.
>
> **Setup.** Let $h : \mathbb{R}^4 \to \mathbb{H}$, $h(x_0, x_1, x_2, x_3) = x_0 + x_1 i + x_2 j + x_3 k$, be the $\mathbb{R}$-linear isomorphism of the problem. We work in $\mathbb{R}^4$ throughout, and pass to $\mathbb{H}$ only by plugging in $h$. Since $|h(\vec x)| = |\vec x|$, the sphere is $S^3 = \{ \vec x \in \mathbb{R}^4 : |\vec x| = 1 \}$, the point $1 \in S^3$ of the problem is $\vec e_0 = h^{-1}(1) = (1, 0, 0, 0)$, and $h(\vec e_1), h(\vec e_2), h(\vec e_3) = i, j, k$. Working in $\mathbb{R}^4$ loses nothing: $h$ is an $\mathbb{R}$-linear isomorphism, hence a diffeomorphism whose differential at every point is $h$ itself, and it carries the unit sphere of $\mathbb{R}^4$ onto the unit quaternions and $\vec e_0$ to $1$. So if $\hat F$ denotes the problem's map on unit quaternions, then $F = \hat F \circ h$ and, by the [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|chain rule]], $F_{\ast,\vec e_0} = \hat F_{\ast,1} \circ h$; in particular $F_{\ast,\vec e_0}(\vec e_j) = \hat F_{\ast,1}\bigl(h(\vec e_j)\bigr)$, so computing in $\mathbb{R}^4$ with $\vec e_j$ gives the same $\sigma_j$ as computing in $\mathbb{H}$ with the tangent vectors $i, j, k$ at $1$, and likewise for $C$ and $G$ in part (b) (the [[§42 SU(2) → SO(3)꞉ The Double Cover#^pf-42-4-2|second proof]] of [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|Theorem §42.4]]). Quaternion multiplication enters only through $h$, in the definitions of $F$ and of the conjugation map $C$. In part (b), the $3 \times 3$ matrices are taken with respect to the identification of $\mathbb{R}^3$ with the purely imaginary quaternions fixed in the problem. In this notation
>
> $$
> F : S^3 \to \mathrm{SU}(2), \qquad F(\vec x) = \text{matrix of } R_{h(\vec x)^{-1}} .
> $$
>
> Write $h(\vec x) = a + b\,j$ with $a = x_0 + x_1 i$ and $b = x_2 + x_3 i$, using $ij = k$. Using $j\,c = \bar c\,j$ for $c \in \mathbb{C}$, for $(z, w) \in \mathbb{C}^2$ we have $(z + wj)(a + bj) = (az - \bar b w) + (bz + \bar a w)\,j$, so $R_{h(\vec x)}$ has matrix $\begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$. Since $|h(\vec x)| = 1$, we have $h(\vec x)^{-1} = \overline{h(\vec x)} = \bar a - b\,j$, and replacing $(a, b)$ by $(\bar a, -b)$ gives
>
> $$
> F(\vec x) = \begin{pmatrix} \bar a & \bar b \\ -b & a \end{pmatrix} = \begin{pmatrix} x_0 - x_1 i & x_2 - x_3 i \\ -x_2 - x_3 i & x_0 + x_1 i \end{pmatrix}.
> $$
>
> Let $L : \mathbb{R}^4 \to \mathrm{Mat}(2, \mathbb{C})$ be given by the same formula, now for all $\vec x \in \mathbb{R}^4$. Each entry is a real linear combination of $x_0, \ldots, x_3$, so $L$ is $\mathbb{R}$-linear, $F = L|_{S^3}$, and $F(\vec e_0) = I$. Throughout, $c_k = \cos\theta_k$ and $s_k = \sin\theta_k$.
>
> **$\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ as submanifolds.** The map $L$ is injective: if $L(\vec x) = 0$, its first row gives $x_0 - x_1 i = 0$ and $x_2 - x_3 i = 0$, so $\vec x = 0$. Hence $V = L(\mathbb{R}^4)$ is a $4$-dimensional real subspace of $\mathrm{Mat}(2, \mathbb{C})$, which has real dimension $8$. Extending the basis $L(\vec e_0), \ldots, L(\vec e_3)$ of $V$ to a basis of $\mathrm{Mat}(2, \mathbb{C})$ ([[§5 Bases#^ladr-2-32|LADR 2.32]]) gives a linear isomorphism
>
> $$
> \Lambda : \mathbb{R}^4 \times \mathbb{R}^4 \to \mathrm{Mat}(2, \mathbb{C}) \qquad \text{with} \qquad \Lambda(\vec x, 0) = L(\vec x).
> $$
>
> By the problem, $F : S^3 \to \mathrm{SU}(2)$ is a bijection, and $F = L|_{S^3}$, so
>
> $$
> \mathrm{SU}(2) = L(S^3) = \Lambda\bigl( S^3 \times \{0\} \bigr).
> $$
>
> Let $M \in \mathrm{SU}(2)$, say $M = L(p)$ with $p \in S^3$, and let $(U, \psi = (y^1, \ldots, y^4))$ be an adapted chart of $\mathbb{R}^4$ at $p$ as constructed above (in [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3]]). Then $\Lambda(U \times \mathbb{R}^4)$ is an open neighborhood of $M$, and
>
> $$
> \Psi = (\psi \times \mathrm{id}_{\mathbb{R}^4}) \circ \Lambda^{-1} : \Lambda(U \times \mathbb{R}^4) \to \psi(U) \times \mathbb{R}^4,
> $$
>
> with components $(y^1, y^2, y^3, y^4, w^1, \ldots, w^4)$, is a diffeomorphism onto an open subset of $\mathbb{R}^8$, hence a chart of $\mathrm{Mat}(2, \mathbb{C})$ at $M$ ([[§34 Submersions#^lem-34-3|Lemma §34.3]]). Since $\Lambda$ is bijective, a point $\Lambda(\vec x, \vec w)$ of its domain lies in $\mathrm{SU}(2)$ if and only if $\vec x \in S^3$ and $\vec w = 0$, that is, if and only if $y^4 = 0$ and $w^1 = \cdots = w^4 = 0$. Listing these five components last, $\Psi$ is adapted to $\mathrm{SU}(2)$. Hence $\mathrm{SU}(2)$ is an embedded submanifold of $\mathrm{Mat}(2, \mathbb{C})$ of dimension $8 - 5 = 3$; by the result on tangent spaces ([[§35 Regular Submanifolds#^prop-35-4|Proposition §35.4]]), the differential $\jmath_{\ast I}$ of the inclusion $\jmath : \mathrm{SU}(2) \hookrightarrow \mathrm{Mat}(2, \mathbb{C})$ is injective, and we identify $T_I\,\mathrm{SU}(2)$ with its image, a $3$-dimensional subspace of $\mathrm{Mat}(2, \mathbb{C})$. Moreover $L \circ \iota : S^3 \to \mathrm{Mat}(2, \mathbb{C})$ is smooth, as the composite of the inclusion $\iota$ of the embedded submanifold $S^3$ and the linear map $L$, and its image $F(S^3)$ lies in the embedded submanifold $\mathrm{SU}(2)$; since a smooth map whose image lies in an embedded submanifold is smooth into that submanifold ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]]), $F : S^3 \to \mathrm{SU}(2)$ is smooth.
>
> For $\mathrm{SO}(3)$ we have no such parametrization, and we take as given, as is implicit in the problem, that $\mathrm{SO}(3)$ is an embedded submanifold of $\mathrm{Mat}(3, \mathbb{R})$ of dimension $3$. Likewise $T_I\,\mathrm{SO}(3)$ is identified with a $3$-dimensional subspace of $\mathrm{Mat}(3, \mathbb{R})$.
>
> **$F^{-1}$ is smooth** (from part (b) of the submitted solution). By the problem, $F : S^3 \to \mathrm{SU}(2)$ is a bijection, so every $M = (m_{kl}) \in \mathrm{SU}(2)$ is $F(\vec x)$ for a unique $\vec x \in S^3$. Comparing the first row of $M$ with the first row of the matrix formula for $F(\vec x)$,
>
> $$
> m_{11} = x_0 - x_1 i, \qquad m_{12} = x_2 - x_3 i,
> $$
>
> and taking real and imaginary parts, $x_0 = \operatorname{Re} m_{11}$, $x_1 = -\operatorname{Im} m_{11}$, $x_2 = \operatorname{Re} m_{12}$, $x_3 = -\operatorname{Im} m_{12}$. Hence
>
> $$
> F^{-1}\begin{pmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{pmatrix} = \bigl( \operatorname{Re} m_{11},\ -\operatorname{Im} m_{11},\ \operatorname{Re} m_{12},\ -\operatorname{Im} m_{12} \bigr),
> $$
>
> which is the restriction to $\mathrm{SU}(2)$ of an $\mathbb{R}$-linear map $\mathrm{Mat}(2, \mathbb{C}) \to \mathbb{R}^4$, hence smooth as a map $\mathrm{SU}(2) \to \mathbb{R}^4$ (composing with the inclusion of $\mathrm{SU}(2)$); since its image lies in the embedded submanifold $S^3$, it is smooth as a map $\mathrm{SU}(2) \to S^3$.

^pf-41-5-2

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-1|Def. §41.1]], [[§41 The Unit Quaternions and SU(2)#^prop-41-1|§41.1]], [[§41 The Unit Quaternions and SU(2)#^prop-41-3|§41.3]], [[§34 Submersions#^lem-34-3|§34.3]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§5 Bases#^ladr-2-32|LADR 2.32]]

> [!remark]- Connections
> - $\mathrm{SU}(2)$ in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]]; unitary matrices in LADR: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]].
> - The unitary groups in 591: [[§11 Topological Groups and Classical Matrix Groups#^def-11-10|Def. §11.10]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]].

The sphere through the course: a topological manifold with hemisphere charts in [[§8 Spheres|Spheres]]; the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$ in [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; the Riemann sphere $\mathbb{CP}^1$ in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|the Riemann sphere]]; its geometric tangent spaces in [[§25 The Geometric Tangent Space#^ex-25-1|the tangent space of the sphere]] and its transverse intersection with a plane in [[§26 Transversality#^ex-26-1|the sphere and the plane re-read]]; the double cover $S^n \to \mathbb{RP}^n$ and the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ in [[§40 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]]; and $S^3 = \mathrm{SU}(2)$ in [[§41 The Unit Quaternions and SU(2)#^prop-41-5|the unit quaternions as SU(2)]].

> [!theorem] Proposition §41.6: The Tangent Space of $\mathrm{SU}(2)$ at the Identity
> The curves $\gamma_1(t) = \cos t + \sin t\, i$, $\gamma_2(t) = \cos t + \sin t\, j$, $\gamma_3(t) = \cos t + \sin t\, k$ in $S^3$ pass through $1$ with velocities ([[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]]) $i, j, k$, and
>
> $$
> \sigma_1 = F_{\ast 1}(i) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}, \qquad
> \sigma_2 = F_{\ast 1}(j) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad
> \sigma_3 = F_{\ast 1}(k) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}.
> $$
>
> They form a basis of $T_I\,\mathrm{SU}(2) = \mathfrak{su}(2) = \{ X \in \operatorname{Mat}(2, \mathbb{C}) : X^{\ast} = -X,\ \operatorname{tr} X = 0 \}$.

^prop-41-6

> [!proof]+ Proof
> *(The submitted solution computed the $\sigma_j$ — “use curves, not coordinates”, as the problem's hint said; the identification of the tangent space is filled in; the submitted computation, with the curves obtained from a hyperspherical chart, follows.)* By the chain rule for curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3]]), $F_{\ast 1}(\gamma_j'(0)) = (F \circ \gamma_j)'(0)$, the entrywise derivative of
>
> $$
> F(\gamma_1(t)) = \begin{pmatrix} e^{-it} & 0 \\ 0 & e^{it} \end{pmatrix}, \quad
> F(\gamma_2(t)) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}, \quad
> F(\gamma_3(t)) = \begin{pmatrix} \cos t & -i\sin t \\ -i\sin t & \cos t \end{pmatrix}
> $$
>
> at $t = 0$. The three matrices are linearly independent (compare the $(1,1)$, $(1,2)$ and $(2,1)$ entries), and $T_I\,\mathrm{SU}(2)$ has dimension $3$ ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|Theorem §29.8]]), so they are a basis. Each lies in $\mathfrak{su}(2)$, which has real dimension $3$: a skew-Hermitian $2 \times 2$ matrix has imaginary diagonal and $x_{21} = -\bar x_{12}$, four real parameters, and $\operatorname{tr} X = 0$ removes one. So $T_I\,\mathrm{SU}(2) = \operatorname{Span}\{\sigma_j\} = \mathfrak{su}(2)$.

^pf-41-6

*Uses:* [[§41 The Unit Quaternions and SU(2)#^prop-41-5|§41.5]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]]

> [!proof]+ Second proof of the formulas for the $\sigma_j$: curves from a hyperspherical chart (the submitted solution)
>
> *(Assignment 4, Problem 3(a), as submitted, in the notation of the [[§41 The Unit Quaternions and SU(2)#^pf-41-5-2|second proof]] of [[§41 The Unit Quaternions and SU(2)#^prop-41-5|Proposition §41.5]]: $\vec e_0 = 1$ and $\vec e_1, \vec e_2, \vec e_3$ correspond to $i, j, k$, so $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ is the $\sigma_j$ of the statement, and the curves $\gamma_j$ below are those of the statement. Items (i)–(v) are [[§41 The Unit Quaternions and SU(2)#^def-41-2|Definition §41.2]], [[§41 The Unit Quaternions and SU(2)#^lem-41-2|Lemma §41.2]] and the steps (iii)–(v) of the [[§41 The Unit Quaternions and SU(2)#^pf-41-3|proof]] of [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3]], and the map $\tilde\Phi$ is that of [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3]]. That the $\sigma_j$ form a basis is shown in the proof above, and again in the [[§42 SU(2) → SO(3)꞉ The Double Cover#^pf-42-4-2|second proof]] of [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|Theorem §42.4]].)*
>
> **The tangent space $T_{\vec e_0} S^3$.** By the result from lecture on tangent spaces of submanifolds ([[§35 Regular Submanifolds#^prop-35-4|Proposition §35.4]]), if $\psi = (y^1, \ldots, y^4)$ is an [[§35 Regular Submanifolds#^def-35-2|adapted chart]] at $p \in S^3$, then $\iota_{\ast p} : T_p S^3 \to T_p\mathbb{R}^4$ is injective and
>
> $$
> \iota_{\ast p}(T_p S^3) = \operatorname{span}\left\{ \frac{\partial}{\partial y^1}\Big|_p, \frac{\partial}{\partial y^2}\Big|_p, \frac{\partial}{\partial y^3}\Big|_p \right\}.
> $$
>
> We identify $T_p\mathbb{R}^4$ with $\mathbb{R}^4$ by $\frac{\partial}{\partial x_a}\big|_p \leftrightarrow \vec e_a$ ([[§30 The Differential in Coordinates#^cor-30-6|Corollary §30.6]]), and $T_p S^3$ with its image under $\iota_{\ast p}$. By the chain rule ([[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4]]), $\frac{\partial}{\partial y^i}\big|_p = \sum_a \frac{\partial x_a}{\partial y^i}\,\frac{\partial}{\partial x_a}\big|_p$ is then the $i$-th column of the Jacobian of $\psi^{-1}$ at $\psi(p)$.
>
> Since $\vec e_0 \in B$, we use $\tilde\Phi$. Applying (iii) to $P^{-1}\vec e_0 = (0, 0, 1, 0)$ gives $\theta = (\pi/2, \pi/2, 0)$, so the adapted chart at $\vec e_0$ from (iv)–(v) has
>
> $$
> \psi^{-1}(y^1, y^2, y^3, y^4) = \tilde\Phi(y^4 + 1, y^1, y^2, y^3), \qquad \psi(\vec e_0) = (\tfrac{\pi}{2}, \tfrac{\pi}{2}, 0, 0).
> $$
>
> For $i = 1, 2, 3$, the $i$-th column of the Jacobian of $\psi^{-1}$ there is $P$ applied to the $\theta_i$-column of $\Phi'(1, \frac{\pi}{2}, \frac{\pi}{2}, 0)$. With $c_1 = 0$, $s_1 = 1$, $c_2 = 0$, $s_2 = 1$, $c_3 = 1$, $s_3 = 0$, these columns are $(-1, 0, 0, 0)$, $(0, -1, 0, 0)$ and $(0, 0, 0, 1)$, so
>
> $$
> \frac{\partial}{\partial y^1}\Big|_{\vec e_0} = -\vec e_2, \qquad \frac{\partial}{\partial y^2}\Big|_{\vec e_0} = -\vec e_3, \qquad \frac{\partial}{\partial y^3}\Big|_{\vec e_0} = \vec e_1 .
> $$
>
> Therefore
>
> $$
> T_{\vec e_0} S^3 = \operatorname{span}\{ \vec e_1, \vec e_2, \vec e_3 \} = \{ \vec x \in \mathbb{R}^4 : x_0 = 0 \}.
> $$
>
> **The vectors $\sigma_j$.** The differential $F_{\ast,\vec e_0} : T_{\vec e_0} S^3 \to T_I\,\mathrm{SU}(2)$ is to be evaluated on the basis $\vec e_1, \vec e_2, \vec e_3$, with $T_I\,\mathrm{SU}(2) \subseteq \mathrm{Mat}(2, \mathbb{C})$ as above:
>
> $$
> \sigma_j = F_{\ast,\vec e_0}(\vec e_j) \in T_I\,\mathrm{SU}(2) \subseteq \mathrm{Mat}(2, \mathbb{C}), \qquad j = 1, 2, 3.
> $$
>
> **Computing $\sigma_j$ with curves.** We use two results from lecture. First, every tangent vector is a velocity ([[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2]]): if $D \in T_p M$ and $(U, \psi)$ is a chart at $p$ with $D = \sum_i a^i \frac{\partial}{\partial y^i}\big|_p$, then $\gamma = \psi^{-1} \circ \ell$, where $\ell(t) = \psi(p) + t\,a$, is a smooth curve with $\gamma(0) = p$ and [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|velocity]] $D_\gamma = D$. Second, the chain rule for curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3]]): for a smooth map $G$, $G_{\ast,p}(D_\gamma) = D_{G \circ \gamma}$. For a curve in $\mathbb{R}^4$ or in $\mathrm{Mat}(2, \mathbb{C})$, the velocity is the ordinary derivative at $t = 0$, computed entry by entry.
>
> *The curves.* We use the chart at $\vec e_0$ constructed above, restricted to $S^3$, that is, the induced chart $(y^1, y^2, y^3)$ with $\psi(\vec e_0) = (\frac{\pi}{2}, \frac{\pi}{2}, 0)$ and $\psi^{-1}(y^1, y^2, y^3) = \tilde\Phi(1, y^1, y^2, y^3)$, where
>
> $$
> \tilde\Phi(1, \theta_1, \theta_2, \theta_3) = \bigl( s_1 s_2 c_3,\ s_1 s_2 s_3,\ c_1,\ s_1 c_2 \bigr).
> $$
>
> By the computation of $T_{\vec e_0} S^3$ above, $\vec e_1 = \frac{\partial}{\partial y^3}\big|_{\vec e_0}$, $\vec e_2 = -\frac{\partial}{\partial y^1}\big|_{\vec e_0}$ and $\vec e_3 = -\frac{\partial}{\partial y^2}\big|_{\vec e_0}$, so the coefficient vectors are $a = (0, 0, 1)$, $(-1, 0, 0)$ and $(0, -1, 0)$, and the lines in the chart are
>
> $$
> \ell_1(t) = \bigl( \tfrac{\pi}{2}, \tfrac{\pi}{2}, t \bigr), \qquad \ell_2(t) = \bigl( \tfrac{\pi}{2} - t, \tfrac{\pi}{2}, 0 \bigr), \qquad \ell_3(t) = \bigl( \tfrac{\pi}{2}, \tfrac{\pi}{2} - t, 0 \bigr).
> $$
>
> Using $\sin(\frac{\pi}{2} - t) = \cos t$ and $\cos(\frac{\pi}{2} - t) = \sin t$, the curves $\gamma_j = \psi^{-1} \circ \ell_j$ are
>
> $$
> \gamma_1(t) = (\cos t, \sin t, 0, 0), \qquad \gamma_2(t) = (\cos t, 0, \sin t, 0), \qquad \gamma_3(t) = (\cos t, 0, 0, \sin t),
> $$
>
> that is, $\gamma_j(t) = \cos t\,\vec e_0 + \sin t\,\vec e_j$. Each lies on $S^3$, satisfies $\gamma_j(0) = \vec e_0$, and has velocity $D_{\gamma_j} = \vec e_j$; indeed $\gamma_j'(0) = \vec e_j$.
>
> *The images under $F$.* Plugging $\gamma_j(t)$ into the matrix formula for $F$,
>
> $$
> F(\gamma_1(t)) = \begin{pmatrix} \cos t - i \sin t & 0 \\ 0 & \cos t + i \sin t \end{pmatrix},
> $$
>
> $$
> F(\gamma_2(t)) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}, \qquad
> F(\gamma_3(t)) = \begin{pmatrix} \cos t & -i \sin t \\ -i \sin t & \cos t \end{pmatrix}.
> $$
>
> *The derivatives.* By the chain rule for curves, applied to $F$ and then to $\jmath$, $\sigma_j = F_{\ast,\vec e_0}(D_{\gamma_j}) = D_{F \circ \gamma_j}$, which under $\jmath_{\ast I}$ is the entrywise derivative of $F(\gamma_j(t))$ at $t = 0$. Hence
>
> $$
> \sigma_1 = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}.
> $$

^pf-41-6-2

*Uses:* [[§41 The Unit Quaternions and SU(2)#^def-41-2|Def. §41.2]], [[§41 The Unit Quaternions and SU(2)#^lem-41-2|§41.2]], [[§41 The Unit Quaternions and SU(2)#^prop-41-3|§41.3]], [[§41 The Unit Quaternions and SU(2)#^prop-41-5|§41.5]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Def. §31.1]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]

> [!remark]- Connections
> - The tangent space of $\mathrm{U}(n)$ at the identity: [[§25 The Geometric Tangent Space#^ex-25-3|Ex. §25.3]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].
> - The Pauli matrices in Quantum Mechanics: [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].
