---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 39
tags: [differentiable-manifolds, math591]
---
← [[§38 Example꞉ Projective Spaces and the Hopf Fibration]] · ↑ [[· 5 Maps of Constant Rank and Bundles]]

*Stage: maps — One example that uses everything so far: submanifolds, embeddings, local diffeomorphisms, and translation in a group.*

*From Assignment 4, Problem 3: the submitted solution, reorganized, with every claim the problem allowed us to assume now proved. References: Lee, Problems 7-22 and 7-23 (quaternions).*

The unit quaternions form a group $S^3$; acting on $\mathbb{C}^2$ they identify it with $\mathrm{SU}(2)$, and acting by conjugation on the pure imaginary quaternions $\mathbb{R}^3$ they give rotations. The result is a two-to-one local diffeomorphism $\mathrm{SU}(2) \to \mathrm{SO}(3)$, and with it $\mathrm{SO}(3) \cong \mathbb{RP}^3$.

![[m591-35-1.svg]]
*The three maps of the section: $F$ identifies unit quaternions with matrices in $\mathrm{SU}(2)$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|Proposition §39.3]]); $C$ is conjugation ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5]]); and $G = C \circ F^{-1}$ is the double cover ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]]).*

## Quaternions and the Unit Sphere

> [!definition] Definition §39.1: Quaternions
> The **quaternions** are $\mathbb{H} = \{ q = x_0 + x_1 i + x_2 j + x_3 k : x_a \in \mathbb{R} \} \cong \mathbb{R}^4$, with the associative, bilinear multiplication determined by
>
> $$
> i^2 = j^2 = k^2 = -1, \qquad ij = -ji = k, \quad jk = -kj = i, \quad ki = -ik = j .
> $$
>
> The **conjugate** of $q$ is $\bar q = x_0 - x_1 i - x_2 j - x_3 k$, its **norm** is the Euclidean norm $|q|$ of $(x_0, \ldots, x_3)$, and $q$ is **pure imaginary** if $x_0 = 0$; the pure imaginary quaternions form $\mathbb{H}_0 \cong \mathbb{R}^3$. We identify $\mathbb{C}$ with $\{x_2 = x_3 = 0\}$.
>
> *Lee: Problem 7-22*

^def-39-1

> [!theorem] Proposition §39.1: Norm and Conjugation
> For $p, q \in \mathbb{H}$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]]): $\overline{pq} = \bar q\, \bar p$, $\ q \bar q = \bar q q = |q|^2$, and $|pq| = |p|\,|q|$. Hence every $q \neq 0$ has inverse $q^{-1} = \bar q / |q|^2$, and $S^3 = \{|q| = 1\}$ is a group ([[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]), with $q^{-1} = \bar q$.

^prop-39-1

> [!proof]+ Proof
> *(Not proved in the submitted solution, where the problem stated it; filled in.)* Both sides of $\overline{pq} = \bar q \bar p$ are real-bilinear in $(p, q)$, so it suffices to check basis elements, where it reads, for instance, $\overline{ij} = \bar k = -k$ and $\bar j \bar i = (-j)(-i) = ji = -k$. Expanding $q \bar q$, the cross terms cancel in pairs ($x_1 x_2 (-ij - ji) = 0$, and so on) and the squares give $x_0^2 + x_1^2 + x_2^2 + x_3^2$. Then $|pq|^2 = pq\, \overline{pq} = p\, q \bar q\, \bar p = |q|^2 p \bar p = |p|^2 |q|^2$, using that the real number $|q|^2$ commutes with everything. The rest follows.

^pf-39-1

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]], [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]

> [!theorem] Proposition §39.2: The Unit Quaternions
> $S^3 \subseteq \mathbb{H} = \mathbb{R}^4$ is a regular submanifold ([[§33 Submanifolds#^def-33-1|Def. §33.1]]) of dimension $3$ and a group ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|§39.1]]) whose multiplication and inversion are smooth ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]). It is connected ([[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]): every $q \in S^3$ other than $\pm 1$ can be written $q = \cos\theta + \sin\theta\, u$ with $\theta \in (0, \pi)$ and $u \in \mathbb{H}_0$, $|u| = 1$, and $t \mapsto \cos t + \sin t\, u$ joins $1$ to $q$ in $S^3$.

^prop-39-2

> [!proof]+ Proof
> *(The submitted solution proved the submanifold claim with hyperspherical charts; the regular value theorem is shorter. Filled in; the submitted proof follows.)* $1$ is a regular value of $f(x) = |x|^2$, since $f'(x) = 2x^{\mathsf T} \neq 0$ on $S^3$, so $S^3$ is a submanifold of codimension $1$ ([[§33 Submanifolds#^thm-33-6|Theorem §33.6]]). Multiplication is polynomial in the coordinates and inversion is $q \mapsto \bar q$, linear; both are smooth into $\mathbb{R}^4$ and land in $S^3$, hence are smooth into $S^3$ ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]). For the polar form, write $q = x_0 + v$ with $v \in \mathbb{H}_0$; if $q \neq \pm 1$ then $v \neq 0$, $x_0^2 + |v|^2 = 1$, and $\theta = \arccos x_0 \in (0, \pi)$, $u = v/|v|$ work, since $|v| = \sin\theta$. The path stays in $S^3$ because $|\cos t + \sin t\, u|^2 = \cos^2 t + \sin^2 t$; and $-1$ is joined to $1$ by $t \mapsto \cos t + \sin t\, i$, $t \in [0, \pi]$.

^pf-39-2

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|§39.1]], [[§33 Submanifolds#^thm-33-6|§33.6]], [[§33 Submanifolds#^lem-33-3|§33.3]], [[§14 Connected Subspaces of ℝ#^thm-14-4|590 §14.4]]

> [!proof]+ Second proof of the submanifold claim: hyperspherical charts (the submitted solution)
>
> *(Assignment 4, Problem 3(a), as submitted. Points of $\mathbb{H} = \mathbb{R}^4$ are written $\vec x = (x_0, x_1, x_2, x_3)$, the standard basis vectors are $\vec e_0, \ldots, \vec e_3$, and an “embedded submanifold” is a submanifold in the sense of [[§33 Submanifolds#^def-33-1|Definition §33.1]]. The group and connectedness claims are proved above.)* Throughout, $c_k = \cos\theta_k$ and $s_k = \sin\theta_k$.
>
> **$S^3$ is an embedded submanifold of $\mathbb{R}^4$.** By the definition from lecture ([[§33 Submanifolds#^def-33-1|Definition §33.1]]), we must show that every $p \in S^3$ lies in the domain of a chart $(U, \psi = (y^1, y^2, y^3, y^4))$ of $\mathbb{R}^4$ with
>
> $$
> U \cap S^3 = \{ \vec u \in U : y^4(\vec u) = 0 \};
> $$
>
> such a chart is *adapted* to $S^3$. Any [[§18 Smooth Functions and Smooth Maps#^def-18-3|diffeomorphism]] from an open subset of $\mathbb{R}^4$ onto an open subset of $\mathbb{R}^4$ is a chart of the standard smooth structure ([[§32 Submersions#^lem-32-3|Lemma §32.3]]).
>
> *(i) Hyperspherical coordinates* (cf. [[Polar and spherical coordinates|452: polar and spherical coordinates]]). Let
>
> $$
> \Phi : (0, \infty) \times \mathbb{R}^3 \to \mathbb{R}^4, \qquad \Phi(r, \theta_1, \theta_2, \theta_3) = \bigl( r c_1,\ r s_1 c_2,\ r s_1 s_2 c_3,\ r s_1 s_2 s_3 \bigr).
> $$
>
> It is smooth, and using $c_k^2 + s_k^2 = 1$ three times, $|\Phi(r, \theta)|^2 = r^2\bigl(c_1^2 + s_1^2 c_2^2 + s_1^2 s_2^2\bigr) = r^2\bigl(c_1^2 + s_1^2\bigr) = r^2$, so $|\Phi(r, \theta)| = r$.
>
> *(ii) Its Jacobian.* With columns indexed by $r, \theta_1, \theta_2, \theta_3$,
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
>
> *(iii) Inverting $\Phi$ off $B$.* Let $p = (x_0, x_1, x_2, x_3) \in S^3 \setminus B$, so $x_2^2 + x_3^2 > 0$. Since $x_0^2 = 1 - x_1^2 - x_2^2 - x_3^2 < 1$, there is $\theta_1 \in (0, \pi)$ with $c_1 = x_0$, and then $s_1 = \sqrt{1 - x_0^2} > 0$. Since $(x_1/s_1)^2 = x_1^2 / (x_1^2 + x_2^2 + x_3^2) < 1$, there is $\theta_2 \in (0, \pi)$ with $c_2 = x_1/s_1$, and then $s_2 > 0$. Now $x_2^2 + x_3^2 = 1 - c_1^2 - s_1^2 c_2^2 = s_1^2 s_2^2$, so $(x_2, x_3)/(s_1 s_2)$ lies on the unit circle and equals $(c_3, s_3)$ for some $\theta_3$. Then $\Phi(1, \theta) = p$ and $\det \Phi'(1, \theta) = s_1^2 s_2 \neq 0$.
>
> *(iv) Adapted charts off $B$.* With $p$ and $\theta$ as in (iii), the inverse function theorem ([[§31 Local Diffeomorphisms#^thm-31-1|Theorem §31.1]]) gives an open $W \ni (1, \theta)$ in $(0, \infty) \times \mathbb{R}^3$ such that $U_p = \Phi(W)$ is open and $\Phi|_W : W \to U_p$ is a diffeomorphism. Let
>
> $$
> \psi_p = \tau \circ (\Phi|_W)^{-1}, \qquad \tau(r, \theta_1, \theta_2, \theta_3) = (\theta_1, \theta_2, \theta_3, r - 1),
> $$
>
> a diffeomorphism onto the open set $\tau(W)$, hence a chart about $p$, with last component $y^4 = r - 1$. For $\vec u = \Phi(r, \theta') \in U_p$ we have $|\vec u| = r$ by (i), so $\vec u \in S^3 \iff r = 1 \iff y^4(\vec u) = 0$. Thus $\psi_p$ is adapted to $S^3$.
>
> *(v) Adapted charts on $B$.* Let $P(x_0, x_1, x_2, x_3) = (x_2, x_3, x_0, x_1)$, a linear [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|isometry]] of $\mathbb{R}^4$ with $\det P = \pm 1$, and $\tilde\Phi = P \circ \Phi$. Then $|\tilde\Phi(r, \theta)| = r$ and $\det \tilde\Phi' = \det P \cdot \det \Phi'$, so (i)–(iv) hold for $\tilde\Phi$ with $B$ replaced by $P(B) = \{ \vec x \in S^3 : x_0 = x_1 = 0 \}$, the angles for $p$ being those of $P^{-1}p$. A point of $B \cap P(B)$ would be $0 \notin S^3$, so $B \cap P(B) = \emptyset$, and every $p \in B$ gets an adapted chart from $\tilde\Phi$.
>
> Hence every point of $S^3$ lies in an adapted chart, and $S^3$ is an embedded submanifold of $\mathbb{R}^4$ of codimension $1$.

^pf-39-2-2

*Uses:* [[§33 Submanifolds#^def-33-1|Def. §33.1]], [[§32 Submersions#^lem-32-3|§32.3]], [[§31 Local Diffeomorphisms#^thm-31-1|§31.1]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[Polar and spherical coordinates|452 Polar and spherical coordinates]], [[Inverse Function Theorem (several variables)|452 §13.2]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]]

> [!remark]- Connections
> - Topological groups: [[§10 Topological Groups and Classical Matrix Groups#^def-10-1|Def. §10.1]]; the sphere as a level set in 452: [[Unit circle and unit sphere|452 Unit circle and unit sphere]].
> - $S^3$ is simply connected: [[Sⁿ is Simply Connected for n ≥ 2|590 §27.3]].

## $S^3$ and $\mathrm{SU}(2)$

> [!theorem] Proposition §39.3: $S^3$ Is $\mathrm{SU}(2)$
> Identify $\mathbb{C}^2$ with $\mathbb{H}$ by $(z, w) \mapsto z + wj$, so that $\mathbb{C}$ acts by left multiplication.
> 1. For $q = a + bj$ ($a, b \in \mathbb{C}$), right multiplication $R_q(x) = xq$ is complex-linear, with matrix $\begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$; for $q \in S^3$ this matrix lies in $\mathrm{SU}(2)$ (unitary: [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]]).
> 2. $F : S^3 \to \mathrm{SU}(2)$, $F(q) =$ the matrix of $R_{q^{-1}}$, is a group isomorphism ([[§16 Isomorphisms#^def-16-1|493 Def. §16.1]]), explicitly
>
> $$
> F(x_0 + x_1 i + x_2 j + x_3 k) = \begin{pmatrix} x_0 - x_1 i & x_2 - x_3 i \\ -x_2 - x_3 i & x_0 + x_1 i \end{pmatrix}.
> $$
>
> 3. $\mathrm{SU}(2)$ is a regular submanifold ([[§33 Submanifolds#^def-33-1|Def. §33.1]]) of $\operatorname{Mat}(2, \mathbb{C}) \cong \mathbb{R}^8$ of dimension $3$, and $F$ is a diffeomorphism ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]).

^prop-39-3

> [!proof]+ Proof
> *(The submitted warm-up gave the matrix in (1) and (2); the problem stated the rest, and the proof of (3) is new, using [[§37 Embeddings|§37]]; the submitted proof of (3), with adapted charts, follows.)* (1) Left multiplication by $c \in \mathbb{C}$ commutes with right multiplication by $q$ (associativity), so $R_q$ is complex-linear. Using $jc = \bar c\, j$ for $c \in \mathbb{C}$ and $j^2 = -1$,
>
> $$
> (z + wj)(a + bj) = za + zbj + w\bar a\, j + w \bar b\, j^2 = (az - \bar b w) + (bz + \bar a w)\, j ,
> $$
>
> which is the matrix shown. Its determinant is $|a|^2 + |b|^2 = |q|^2$; and $R_q$ preserves norms when $|q| = 1$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|Proposition §39.1]]), and the norm of $\mathbb{H}$ is the Hermitian norm of $\mathbb{C}^2$, so the matrix is unitary. Hence it lies in $\mathrm{SU}(2)$.
>
> (2) $q^{-1} = \bar q = \bar a - bj$, so (1) with $(a, b)$ replaced by $(\bar a, -b)$ gives the formula. $F$ is a homomorphism because $R_{(pq)^{-1}}(x) = x q^{-1} p^{-1} = R_{p^{-1}}(R_{q^{-1}}(x))$ — the inverse is there to make the order come out right. It is injective, since $R_{q^{-1}} = \mathrm{id}$ forces $q^{-1} = 1 \cdot q^{-1} = 1$. It is surjective: a matrix $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in \mathrm{SU}(2)$ has inverse $\begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$ (determinant $1$) equal to its conjugate transpose $\begin{pmatrix} \bar\alpha & \bar\gamma \\ \bar\beta & \bar\delta \end{pmatrix}$, so $\delta = \bar\alpha$ and $\gamma = -\bar\beta$, with $|\alpha|^2 + |\beta|^2 = 1$; this is $F(a + bj)$ for $a = \bar\alpha$, $b = \bar\beta$.
>
> (3) The formula defines an $\mathbb{R}$-linear map $L : \mathbb{R}^4 \to \operatorname{Mat}(2, \mathbb{C})$ with $F = L|_{S^3}$, and $L$ is injective (its first row determines $x$). An injective linear map is an embedding — an immersion, and a homeomorphism onto its image, with the inverse a restriction of a linear map — and so is $L|_{S^3}$, as the composite of the embeddings $S^3 \hookrightarrow \mathbb{R}^4 \xrightarrow{L} \operatorname{Mat}(2, \mathbb{C})$. Its image is $F(S^3) = \mathrm{SU}(2)$ by (2), so $\mathrm{SU}(2)$ is a regular submanifold of dimension $3$ ([[§37 Embeddings#^thm-37-1|Theorem §37.1]]) and $F$ is a diffeomorphism onto it ([[§37 Embeddings#^cor-37-3|Corollary §37.3]]).

^pf-39-3

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|§39.1]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]], [[§37 Embeddings#^def-37-1|Def. §37.1]], [[§37 Embeddings#^thm-37-1|§37.1]], [[§37 Embeddings#^cor-37-3|§37.3]], [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|LADR 7.53]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]]

> [!proof]+ Second proof of (3): adapted charts (the submitted solution)
>
> *(Assignment 4, Problem 3, as submitted: its notation and setup, its proof that $\mathrm{SU}(2)$ is a submanifold and $F$ is smooth, and, moved here from its part (b), its proof that $F^{-1}$ is smooth; together they give (3). The adapted charts of $\mathbb{R}^4$ are those of the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-2-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|Proposition §39.2]]. What the submitted solution takes from the problem — that $F$ is a bijection onto $\mathrm{SU}(2)$, and that $\SO(3)$ is a submanifold of dimension $3$ — is proved in (2) above and in [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|Theorem §23.5]].)*
>
> **Notation.** The problem writes $dF_p$ for the differential of a smooth map $F$ at a point $p$. As in lecture and in Problem 1 ([[§28 The Differential in Coordinates#^prop-28-9|Proposition §28.9]]), we write $F_{\ast,p}$ instead, so that $dF_p = F_{\ast,p}$. Since we work in $\mathbb{R}^4$ (see below), the problem's point $1 \in S^3$ is $\vec e_0$; thus the problem's $T_1 S^3$, $\sigma_j = dF_1(\vec e_j)$ and $dG_I(\sigma_j)$ are, in our notation, $T_{\vec e_0} S^3$, $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ and $G_{\ast,I}(\sigma_j)$.
>
> **Setup.** Let $h : \mathbb{R}^4 \to \mathbb{H}$, $h(x_0, x_1, x_2, x_3) = x_0 + x_1 i + x_2 j + x_3 k$, be the $\mathbb{R}$-linear isomorphism of the problem. We work in $\mathbb{R}^4$ throughout, and pass to $\mathbb{H}$ only by plugging in $h$. Since $|h(\vec x)| = |\vec x|$, the sphere is $S^3 = \{ \vec x \in \mathbb{R}^4 : |\vec x| = 1 \}$, the point $1 \in S^3$ of the problem is $\vec e_0 = h^{-1}(1) = (1, 0, 0, 0)$, and $h(\vec e_1), h(\vec e_2), h(\vec e_3) = i, j, k$. Working in $\mathbb{R}^4$ loses nothing: $h$ is an $\mathbb{R}$-linear isomorphism, hence a diffeomorphism whose differential at every point is $h$ itself, and it carries the unit sphere of $\mathbb{R}^4$ onto the unit quaternions and $\vec e_0$ to $1$. So if $\hat F$ denotes the problem's map on unit quaternions, then $F = \hat F \circ h$ and, by the [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|chain rule]], $F_{\ast,\vec e_0} = \hat F_{\ast,1} \circ h$; in particular $F_{\ast,\vec e_0}(\vec e_j) = \hat F_{\ast,1}\bigl(h(\vec e_j)\bigr)$, so computing in $\mathbb{R}^4$ with $\vec e_j$ gives the same $\sigma_j$ as computing in $\mathbb{H}$ with the tangent vectors $i, j, k$ at $1$, and likewise for $C$ and $G$ in part (b) (the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-8-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]]). Quaternion multiplication enters only through $h$, in the definitions of $F$ and of the conjugation map $C$. In part (b), the $3 \times 3$ matrices are taken with respect to the identification of $\mathbb{R}^3$ with the purely imaginary quaternions fixed in the problem. In this notation
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
> Let $M \in \mathrm{SU}(2)$, say $M = L(p)$ with $p \in S^3$, and let $(U, \psi = (y^1, \ldots, y^4))$ be an adapted chart of $\mathbb{R}^4$ at $p$ as constructed above (in the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-2-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|Proposition §39.2]]). Then $\Lambda(U \times \mathbb{R}^4)$ is an open neighborhood of $M$, and
>
> $$
> \Psi = (\psi \times \mathrm{id}_{\mathbb{R}^4}) \circ \Lambda^{-1} : \Lambda(U \times \mathbb{R}^4) \to \psi(U) \times \mathbb{R}^4,
> $$
>
> with components $(y^1, y^2, y^3, y^4, w^1, \ldots, w^4)$, is a diffeomorphism onto an open subset of $\mathbb{R}^8$, hence a chart of $\mathrm{Mat}(2, \mathbb{C})$ at $M$ ([[§32 Submersions#^lem-32-3|Lemma §32.3]]). Since $\Lambda$ is bijective, a point $\Lambda(\vec x, \vec w)$ of its domain lies in $\mathrm{SU}(2)$ if and only if $\vec x \in S^3$ and $\vec w = 0$, that is, if and only if $y^4 = 0$ and $w^1 = \cdots = w^4 = 0$. Listing these five components last, $\Psi$ is adapted to $\mathrm{SU}(2)$. Hence $\mathrm{SU}(2)$ is an embedded submanifold of $\mathrm{Mat}(2, \mathbb{C})$ of dimension $8 - 5 = 3$; by the result on tangent spaces ([[§33 Submanifolds#^prop-33-4|Proposition §33.4]]), the differential $\jmath_{\ast I}$ of the inclusion $\jmath : \mathrm{SU}(2) \hookrightarrow \mathrm{Mat}(2, \mathbb{C})$ is injective, and we identify $T_I\,\mathrm{SU}(2)$ with its image, a $3$-dimensional subspace of $\mathrm{Mat}(2, \mathbb{C})$. Moreover $L \circ \iota : S^3 \to \mathrm{Mat}(2, \mathbb{C})$ is smooth, as the composite of the inclusion $\iota$ of the embedded submanifold $S^3$ and the linear map $L$, and its image $F(S^3)$ lies in the embedded submanifold $\mathrm{SU}(2)$; since a smooth map whose image lies in an embedded submanifold is smooth into that submanifold ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]), $F : S^3 \to \mathrm{SU}(2)$ is smooth.
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

^pf-39-3-2

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|§39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|§39.2]], [[§32 Submersions#^lem-32-3|§32.3]], [[§33 Submanifolds#^def-33-1|Def. §33.1]], [[§33 Submanifolds#^prop-33-4|§33.4]], [[§33 Submanifolds#^lem-33-3|§33.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§5 Bases#^ladr-2-32|LADR 2.32]]

> [!remark]- Connections
> - $\mathrm{SU}(2)$ in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]]; unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]].
> - The unitary groups in 591: [[§10 Topological Groups and Classical Matrix Groups#^def-10-8|Def. §10.8]], [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|Ex. §22.2]].

The sphere through the course: a topological manifold with hemisphere charts in [[§8 Example꞉ Spheres|Example: Spheres]]; the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$ in [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; the Riemann sphere $\mathbb{CP}^1$ in [[§17 Projective Spaces as Smooth Manifolds#^prop-17-4|the Riemann sphere]]; its geometric tangent spaces in [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-1|the tangent space of the sphere]] and its transverse intersection with a plane in [[§24 Transversality#^ex-24-1|the sphere and the plane re-read]]; the double cover $S^n \to \mathbb{RP}^n$ and the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ in [[§38 Example꞉ Projective Spaces and the Hopf Fibration|Example: Projective Spaces and the Hopf Fibration]]; and $S^3 = \mathrm{SU}(2)$ in [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|the unit quaternions as SU(2)]].

> [!theorem] Proposition §39.4: The Tangent Space of $\mathrm{SU}(2)$ at the Identity
> The curves $\gamma_1(t) = \cos t + \sin t\, i$, $\gamma_2(t) = \cos t + \sin t\, j$, $\gamma_3(t) = \cos t + \sin t\, k$ in $S^3$ pass through $1$ with velocities ([[§29 Tangent Vectors as Velocities of Curves#^def-29-1|Def. §29.1]]) $i, j, k$, and
>
> $$
> \sigma_1 = F_{\ast 1}(i) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}, \qquad
> \sigma_2 = F_{\ast 1}(j) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad
> \sigma_3 = F_{\ast 1}(k) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}.
> $$
>
> They form a basis of $T_I\,\mathrm{SU}(2) = \mathfrak{su}(2) = \{ X \in \operatorname{Mat}(2, \mathbb{C}) : X^{\ast} = -X,\ \operatorname{tr} X = 0 \}$.

^prop-39-4

> [!proof]+ Proof
> *(The submitted solution computed the $\sigma_j$ — “use curves, not coordinates”, as the problem's hint said; the identification of the tangent space is filled in; the submitted computation, with the curves obtained from a hyperspherical chart, follows.)* By the chain rule for curves ([[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|Corollary §29.3]]), $F_{\ast 1}(\gamma_j'(0)) = (F \circ \gamma_j)'(0)$, the entrywise derivative of
>
> $$
> F(\gamma_1(t)) = \begin{pmatrix} e^{-it} & 0 \\ 0 & e^{it} \end{pmatrix}, \quad
> F(\gamma_2(t)) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}, \quad
> F(\gamma_3(t)) = \begin{pmatrix} \cos t & -i\sin t \\ -i\sin t & \cos t \end{pmatrix}
> $$
>
> at $t = 0$. The three matrices are linearly independent (compare the $(1,1)$, $(1,2)$ and $(2,1)$ entries), and $T_I\,\mathrm{SU}(2)$ has dimension $3$ ([[§27 Coordinate Derivations and the Basis Theorem#^thm-27-8|Theorem §27.8]]), so they are a basis. Each lies in $\mathfrak{su}(2)$, which has real dimension $3$: a skew-Hermitian $2 \times 2$ matrix has imaginary diagonal and $x_{21} = -\bar x_{12}$, four real parameters, and $\operatorname{tr} X = 0$ removes one. So $T_I\,\mathrm{SU}(2) = \operatorname{Span}\{\sigma_j\} = \mathfrak{su}(2)$.

^pf-39-4

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]], [[§29 Tangent Vectors as Velocities of Curves#^def-29-1|Def. §29.1]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-8|§27.8]], [[§33 Submanifolds#^prop-33-4|§33.4]]

> [!proof]+ Second proof of the formulas for the $\sigma_j$: curves from a hyperspherical chart (the submitted solution)
>
> *(Assignment 4, Problem 3(a), as submitted, in the notation of the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-3-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|Proposition §39.3]]: $\vec e_0 = 1$ and $\vec e_1, \vec e_2, \vec e_3$ correspond to $i, j, k$, so $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ is the $\sigma_j$ of the statement, and the curves $\gamma_j$ below are those of the statement. Items (i)–(v) and the map $\tilde\Phi$ are those of the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-2-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|Proposition §39.2]]. That the $\sigma_j$ form a basis is shown in the proof above, and again in the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-8-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]].)*
>
> **The tangent space $T_{\vec e_0} S^3$.** By the result from lecture on tangent spaces of submanifolds ([[§33 Submanifolds#^prop-33-4|Proposition §33.4]]), if $\psi = (y^1, \ldots, y^4)$ is an [[§33 Submanifolds#^def-33-1|adapted chart]] at $p \in S^3$, then $\iota_{\ast p} : T_p S^3 \to T_p\mathbb{R}^4$ is injective and
>
> $$
> \iota_{\ast p}(T_p S^3) = \operatorname{span}\left\{ \frac{\partial}{\partial y^1}\Big|_p, \frac{\partial}{\partial y^2}\Big|_p, \frac{\partial}{\partial y^3}\Big|_p \right\}.
> $$
>
> We identify $T_p\mathbb{R}^4$ with $\mathbb{R}^4$ by $\frac{\partial}{\partial x_a}\big|_p \leftrightarrow \vec e_a$ ([[§28 The Differential in Coordinates#^cor-28-6|Corollary §28.6]]), and $T_p S^3$ with its image under $\iota_{\ast p}$. By the chain rule ([[§28 The Differential in Coordinates#^cor-28-4|Corollary §28.4]]), $\frac{\partial}{\partial y^i}\big|_p = \sum_a \frac{\partial x_a}{\partial y^i}\,\frac{\partial}{\partial x_a}\big|_p$ is then the $i$-th column of the Jacobian of $\psi^{-1}$ at $\psi(p)$.
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
> **Computing $\sigma_j$ with curves.** We use two results from lecture. First, every tangent vector is a velocity ([[§29 Tangent Vectors as Velocities of Curves#^thm-29-2|Theorem §29.2]]): if $D \in T_p M$ and $(U, \psi)$ is a chart at $p$ with $D = \sum_i a^i \frac{\partial}{\partial y^i}\big|_p$, then $\gamma = \psi^{-1} \circ \ell$, where $\ell(t) = \psi(p) + t\,a$, is a smooth curve with $\gamma(0) = p$ and [[§29 Tangent Vectors as Velocities of Curves#^def-29-1|velocity]] $D_\gamma = D$. Second, the chain rule for curves ([[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|Corollary §29.3]]): for a smooth map $G$, $G_{\ast,p}(D_\gamma) = D_{G \circ \gamma}$. For a curve in $\mathbb{R}^4$ or in $\mathrm{Mat}(2, \mathbb{C})$, the velocity is the ordinary derivative at $t = 0$, computed entry by entry.
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

^pf-39-4-2

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|§39.2]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]], [[§33 Submanifolds#^prop-33-4|§33.4]], [[§28 The Differential in Coordinates#^cor-28-6|§28.6]], [[§28 The Differential in Coordinates#^cor-28-4|§28.4]], [[§29 Tangent Vectors as Velocities of Curves#^def-29-1|Def. §29.1]], [[§29 Tangent Vectors as Velocities of Curves#^thm-29-2|§29.2]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]]

> [!remark]- Connections
> - The tangent space of $\mathrm{U}(n)$ at the identity: [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-3|Ex. §23.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]].
> - The Pauli matrices in Quantum Mechanics: [[§B6.1 Spin One-Half and the Pauli Matrices#^def-b6-1-2|QM Def. §B6.1.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]].

## Conjugation and Rotations

> [!theorem] Proposition §39.5: Conjugation by Unit Quaternions Is Rotation
> For $q \in S^3$, the map $C_q(v) = q v \bar q$ sends $\mathbb{H}_0 \cong \mathbb{R}^3$ to itself, and:
> 1. $C_q \in \mathrm{SO}(3)$ ([[§10 Topological Groups and Classical Matrix Groups#^def-10-7|Def. §10.7]]), and $C : S^3 \to \mathrm{SO}(3)$, $q \mapsto C_q$, is a smooth ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]);
> 2. $\ker C = \{\pm 1\}$ ([[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]), so $C_p = C_q$ if and only if $p = \pm q$;
> 3. if $u \in \mathbb{H}_0$ is a unit vector and $\theta \in \mathbb{R}$, then $C_q$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ is the rotation by the angle $\theta$ about the axis $u$.

^prop-39-5

> [!proof]+ Proof
> *(The problem stated (1) and the two-to-one property without proof; filled in. Part (3) contains the submitted computation: for $q = \gamma_j(t)$ it gives the rotation by $2t$ about $e_j$; the submitted computation itself is in the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-8-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]].)* A quaternion $v$ is pure imaginary iff $\bar v = -v$, and then $\overline{q v \bar q} = q \bar v \bar q = -q v \bar q$, so $C_q(v) \in \mathbb{H}_0$; and $|C_q(v)| = |v|$ by [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|Proposition §39.1]]. So $C_q$ is a linear isometry of $\mathbb{R}^3$, $C_q \in \mathrm{O}(3)$.
>
> (1) $C_{pq}(v) = pq v \bar q \bar p = C_p(C_q(v))$. The entries of $C_q$ are quadratic polynomials in the coordinates of $q$, so $C$ is smooth into $\operatorname{Mat}(3, \mathbb{R})$, with values in the submanifold $\mathrm{O}(3)$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|Theorem §23.5]]). $\det \circ C : S^3 \to \{\pm 1\}$ is continuous on the connected $S^3$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|Proposition §39.2]]) and equals $1$ at $q = 1$, so $C$ takes values in $\mathrm{SO}(3)$, an open subset of $\mathrm{O}(3)$; hence $C$ is smooth into $\mathrm{SO}(3)$ ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]).
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

^pf-39-5

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^def-39-1|Def. §39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-1|§39.1]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-2|§39.2]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-7|Def. §10.7]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-3|§10.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]], [[§33 Submanifolds#^lem-33-3|§33.3]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]], [[Continuous Image of a Connected Space is Connected|590 §13.3]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[§15 Homomorphisms#^def-15-2|493 Def. §15.2]]

> [!remark]- Connections
> - The half-angle in Quantum Mechanics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]].
> - Isometries in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]; the kernel $\{\pm 1\}$ as a center in 493: [[§33 The Center#^def-33-1|493 Def. §33.1]].

The half-angle in (3) is the source of the factor $2$ below: the curve $\gamma_j(t)$ through $1$ moves at unit speed in $S^3$, but its image rotates by $2t$.

> [!theorem] Lemma §39.6: Every Rotation Has an Axis
> Every $A \in \mathrm{SO}(3)$ ([[§10 Topological Groups and Classical Matrix Groups#^def-10-7|Def. §10.7]]) is the rotation by some angle $\theta$ about some unit axis $u$.

^lem-39-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $\det(A - I) = \det(A - A A^{\mathsf T}) = \det A \, \det(I - A^{\mathsf T}) = \det(I - A) = -\det(A - I)$, the last step because $3$ is odd. So $\det(A - I) = 0$, and $Au = u$ for some unit $u$. $A$ preserves $u^\perp$ and restricts to an orientation-preserving isometry of that plane, a rotation by some $\theta$.

^pf-39-6

*Uses:* [[§10 Topological Groups and Classical Matrix Groups#^def-10-7|Def. §10.7]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§34 Determinants#^ladr-9-56|LADR 9.56]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]]

> [!remark]- Connections
> - Rotations in Quantum Mechanics, by Euler angles: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-2|QM Def. §C5.2.2]]; isometries in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

## The Double Cover

> [!theorem] Lemma §39.7: Translating the Differential
> Let $G : H \to K$ be a smooth ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]) group homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) between groups of matrices that are regular submanifolds ([[§33 Submanifolds#^def-33-1|Def. §33.1]]), closed under products and inverses. For $h \in H$ let $L_h(x) = hx$. Then for every $g \in H$,
>
> $$
> G_{\ast g} = (L_{G(g)})_{\ast I} \circ G_{\ast I} \circ (L_{g^{-1}})_{\ast g} ,
> $$
>
> and each $(L_h)_{\ast}$ is an isomorphism. In particular, if $G_{\ast I}$ is an isomorphism, so is every $G_{\ast g}$.

^lem-39-7

> [!proof]+ Proof
> *(The submitted solution's argument, isolated as a lemma; in its original form it is part of the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-8-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]].)* $L_h$ is the restriction of the linear map $x \mapsto hx$, so it is smooth ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]), with smooth inverse $L_{h^{-1}}$: a diffeomorphism, so its differentials are isomorphisms ([[§26 Derivations and the Abstract Tangent Space#^thm-26-6|chain rule]]). $G$ is a homomorphism, so $G \circ L_g = L_{G(g)} \circ G$; differentiating at $I$ gives $G_{\ast g} \circ (L_g)_{\ast I} = (L_{G(g)})_{\ast I} \circ G_{\ast I}$, and $(L_g)_{\ast I}^{-1} = (L_{g^{-1}})_{\ast g}$.

^pf-39-7

*Uses:* [[§33 Submanifolds#^lem-33-3|§33.3]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§26 Derivations and the Abstract Tangent Space#^cor-26-7|§26.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!remark]- Connections
> - The geometric version for the classical groups, $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$: [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|§23.5]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-7|Remark: Left and Right Translates]].

This is the left translation of the [[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-7|discussion of moving base points]]: in a group, translation carries the tangent space at $I$ to the tangent space at every $g$, so what happens at the identity happens everywhere.

> [!theorem] Theorem §39.8: The Double Cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$
> $G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a surjective smooth group homomorphism and a local diffeomorphism ([[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]]), with
>
> $$
> G_{\ast I}(\sigma_j) = 2\,\hat e_j \qquad (j = 1, 2, 3),
> $$
>
> twice the basis of $\operatorname{Skew}(3, \mathbb{R}) = T_I\,\mathrm{SO}(3)$ given by the hat map ([[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-3|Def. §23.3]]). It is two-to-one: $G(g) = G(h)$ iff $h = \pm g$. Consequently $G$ induces a homeomorphism ([[§9 Continuous Functions#^def-9-2|590 Def. §9.2]])
>
> $$
> \mathrm{SO}(3) \;\cong\; \mathrm{SU}(2)/\{\pm I\} \;\cong\; S^3/\{\pm 1\} \;=\; \mathbb{RP}^3 .
> $$

^thm-39-8

> [!proof]+ Proof
> *(The submitted solution computed $G_{\ast I}(\sigma_j)$ and proved the local diffeomorphism; surjectivity, the two-to-one property and the identification with $\mathbb{RP}^3$ are filled in; the submitted proof follows.)* $G$ is a smooth homomorphism, as a composite of $F^{-1}$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|Proposition §39.3]]) and $C$.
>
> *The differential at $I$.* By the chain rule $G_{\ast I}(\sigma_j) = G_{\ast I}(F_{\ast 1}(\gamma_j'(0))) = C_{\ast 1}(\gamma_j'(0)) = (C \circ \gamma_j)'(0)$, and by [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5]](3) with $\theta = 2t$, $C(\gamma_j(t))$ is the rotation by $2t$ about $e_j$; for $j = 1$,
>
> $$
> C(\gamma_1(t)) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2t & -\sin 2t \\ 0 & \sin 2t & \cos 2t \end{pmatrix}, \qquad \frac{d}{dt}\Big|_{t=0} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix} = 2\,\hat e_1 ,
> $$
>
> and likewise for $j = 2, 3$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-3|Definition §23.3]]). The $\hat e_j$ are a basis of $T_I\,\mathrm{SO}(3) = \operatorname{Skew}(3, \mathbb{R})$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|Example §23.4]]), so $G_{\ast I}$ is an isomorphism.
>
> *Local diffeomorphism.* By [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-39-7|Lemma §39.7]] every $G_{\ast g}$ is an isomorphism, so $G$ is a local diffeomorphism ([[§31 Local Diffeomorphisms#^thm-31-2|Theorem §31.2]]).
>
> *Surjective.* By [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-39-6|Lemma §39.6]], an element of $\mathrm{SO}(3)$ is a rotation by some $\theta$ about some $u$, which is $C_q = G(F(q))$ for $q = \cos\frac\theta2 + \sin\frac\theta2\, u$ by [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5]](3).
>
> *Two-to-one.* $G(g) = G(h)$ iff $C_{F^{-1}(g)} = C_{F^{-1}(h)}$ iff $F^{-1}(h) = \pm F^{-1}(g)$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5]](2)) iff $h = \pm g$, since $F$ is a homomorphism with $F(-1) = -I$.
>
> *$\mathbb{RP}^3$.* $C$ is constant on the classes $\{\pm q\}$, so it induces a map $\bar C : S^3/\{\pm 1\} \to \mathrm{SO}(3)$, continuous by the [[§5 Quotient Maps#^cor-5-2|universal property of the quotient]], and bijective by the last two steps. $S^3/\{\pm 1\} = \mathbb{RP}^3$ ([[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|Corollary §17.5]]) is compact as the image of $S^3$, and $\mathrm{SO}(3)$ is Hausdorff, so $\bar C$ is a homeomorphism ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]); and $F$ identifies $S^3/\{\pm 1\}$ with $\mathrm{SU}(2)/\{\pm I\}$.

^pf-39-8

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-4|§39.4]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|§39.5]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-39-6|§39.6]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-39-7|§39.7]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-3|Def. §23.3]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|Ex. §23.4]], [[§31 Local Diffeomorphisms#^thm-31-2|§31.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|§17.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Universal Property of Quotient Maps|590 §12.3]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]

> [!proof]+ Second proof: the conjugation map computed explicitly (the submitted solution)
>
> *(Assignment 4, Problem 3(b), as submitted, in the notation of the second proofs of Propositions [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]] and [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-4|§39.4]]; “part (a)” is the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-4-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-4|Proposition §39.4]]. It proves that $G$ is smooth, the formula for $G_{\ast I}(\sigma_j)$ — the three matrices it finds are $2\hat e_1$, $2\hat e_2$, $2\hat e_3$ ([[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-3|Definition §23.3]]) — and that $G$ is a [[§31 Local Diffeomorphisms#^def-31-1|local diffeomorphism]]; surjectivity, the two-to-one property and $\mathbb{RP}^3$ are proved above. What it takes as given from the problem is proved in Propositions [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]] and [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|§39.5]]. Its proof that $F^{-1}$ is smooth is in the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-3-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|Proposition §39.3]]. In $C(\vec x)$, $\vec x$ is a point of $S^3$; in the proof above, $C_q$ is the same map for $q = h(\vec x)$.)*
>
> **Reduction to the conjugation map.** Let $\mathbb{H}_0 = \{ y_1 i + y_2 j + y_3 k : y_1, y_2, y_3 \in \mathbb{R} \}$ be the purely imaginary quaternions, and identify $\mathbb{R}^3$ with $\mathbb{H}_0$ by $h_0(y_1, y_2, y_3) = h(0, y_1, y_2, y_3) = y_1 i + y_2 j + y_3 k$. For $\vec x \in S^3$, conjugation by the unit quaternion $h(\vec x)$, whose inverse is $\overline{h(\vec x)}$, defines the linear map
>
> $$
> C(\vec x) : \mathbb{R}^3 \to \mathbb{R}^3, \qquad C(\vec x)(\vec y) = h_0^{-1}\Bigl( h(\vec x)\; h_0(\vec y)\; \overline{h(\vec x)} \Bigr).
> $$
>
> As stated in the problem, $C(\vec x) \in \mathrm{SO}(3)$, and $C : S^3 \to \mathrm{SO}(3)$ is a $2$–$1$ [[§15 Homomorphisms#^def-15-1|group morphism]]; we take these facts as given.
>
> *Smoothness.* Each coordinate of the quaternion $h(\vec x)\, h_0(\vec y)\, \overline{h(\vec x)}$ is a polynomial in the variables $x_0, \ldots, x_3$ and $y_1, y_2, y_3$, quadratic in $\vec x$ and linear in $\vec y$, so each entry of the matrix $C(\vec x)$ is a quadratic polynomial in $x_0, \ldots, x_3$. Hence $C$ is the restriction to $S^3$ of a smooth map $\mathbb{R}^4 \to \mathrm{Mat}(3, \mathbb{R})$, so it is smooth as a map $S^3 \to \mathrm{Mat}(3, \mathbb{R})$ (composing with the inclusion of $S^3$), and since its image lies in the embedded submanifold $\mathrm{SO}(3)$, it is smooth as a map $S^3 \to \mathrm{SO}(3)$ ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]). [The submitted proof that $F^{-1} : \mathrm{SU}(2) \to S^3$ is smooth stands here; it is now the last paragraph of the [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^pf-39-3-2|second proof]] of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|Proposition §39.3]].] Thus
>
> $$
> G = C \circ F^{-1} : \mathrm{SU}(2) \to \mathrm{SO}(3)
> $$
>
> is smooth, as a composite of smooth maps.
>
> *Reduction.* Since $G \circ F = C$ and $F(\vec e_0) = I$, the [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|chain rule]] gives $G_{\ast,I} \circ F_{\ast,\vec e_0} = C_{\ast,\vec e_0}$. Applying this to $\vec e_j$ and using $\sigma_j = F_{\ast,\vec e_0}(\vec e_j)$ from part (a),
>
> $$
> G_{\ast,I}(\sigma_j) = C_{\ast,\vec e_0}(\vec e_j), \qquad j = 1, 2, 3.
> $$
>
> By the chain rule for curves ([[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|Corollary §29.3]]), with the curves $\gamma_j$ of part (a), which satisfy $\gamma_j(0) = \vec e_0$ and $D_{\gamma_j} = \vec e_j$,
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
> *Translations are diffeomorphisms.* On $\mathrm{Mat}(2, \mathbb{C})$ the map $M \mapsto gM$ is linear, hence smooth; its restriction to the embedded submanifold $\mathrm{SU}(2)$ is smooth, and it takes values in $\mathrm{SU}(2)$ because $\mathrm{SU}(2)$ is closed under products, so $L_g : \mathrm{SU}(2) \to \mathrm{SU}(2)$ is smooth, since a smooth map whose image lies in an embedded submanifold is smooth into that submanifold ([[§33 Submanifolds#^lem-33-3|Lemma §33.3]]). The same holds for $L_{g^{-1}}$, and $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$ by associativity and $g g^{-1} = g^{-1} g = I$. Hence $L_g$ is a diffeomorphism, and by the chain rule ([[§26 Derivations and the Abstract Tangent Space#^thm-26-6|Theorem §26.6]]) $(L_{g^{-1}})_{\ast,g} \circ (L_g)_{\ast,I} = \mathrm{id}$ and $(L_g)_{\ast,I} \circ (L_{g^{-1}})_{\ast,g} = \mathrm{id}$, so $(L_g)_{\ast,I}$ is an isomorphism with inverse $(L_{g^{-1}})_{\ast,g}$. In the same way, using that $\mathrm{SO}(3)$ is an embedded submanifold of $\mathrm{Mat}(3, \mathbb{R})$ closed under products, $L_{G(g)}$ is a diffeomorphism of $\mathrm{SO}(3)$ and $(L_{G(g)})_{\ast,I}$ is an isomorphism.
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
> **$G$ is a local diffeomorphism.** Let $g \in \mathrm{SU}(2)$. Choose a chart $(V, \chi)$ of $\mathrm{SO}(3)$ at $G(g)$ and, using continuity of $G$, a chart $(U, \varphi)$ of $\mathrm{SU}(2)$ at $g$ with $G(U) \subseteq V$. The coordinate representation $\hat G = \chi \circ G \circ \varphi^{-1} : \varphi(U) \to \chi(V)$ is a smooth map between open subsets of $\mathbb{R}^3$, and its Jacobian at $\varphi(g)$ is the matrix of $G_{\ast,g}$ in the coordinate bases ([[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2]]), hence invertible. By the inverse function theorem ([[§31 Local Diffeomorphisms#^thm-31-1|Theorem §31.1]]), there are open sets $U_0 \ni \varphi(g)$ in $\varphi(U)$ and $V_0 = \hat G(U_0) \subseteq \chi(V)$ such that $\hat G|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse. Then $\varphi^{-1}(U_0)$ is an open neighborhood of $g$, $\chi^{-1}(V_0)$ is open in $\mathrm{SO}(3)$, and
>
> $$
> G|_{\varphi^{-1}(U_0)} = \chi^{-1} \circ \hat G|_{U_0} \circ \varphi : \varphi^{-1}(U_0) \to \chi^{-1}(V_0)
> $$
>
> is a composite of diffeomorphisms, hence a diffeomorphism. As $g$ was arbitrary, $G$ is a local diffeomorphism.

^pf-39-8-2

*Uses:* [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-3|§39.3]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-4|§39.4]], [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|§39.5]], [[§23 Tangent Spaces I꞉ The Geometric Picture#^def-23-3|Def. §23.3]], [[§33 Submanifolds#^lem-33-3|§33.3]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§31 Local Diffeomorphisms#^thm-31-1|§31.1]], [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]], [[§15 Homomorphisms#^def-15-1|493 Def. §15.1]], [[Inverse Function Theorem (several variables)|452 §13.2]]

> [!remark]- Connections
> - The same theorem in physics: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; $\mathrm{SU}(2) \cong S^3$ and $\mathrm{SO}(3) \cong \mathbb{RP}^3$ topologically, with $\pi_1$: [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|QFT Theorem §C3.1.8]].
> - The algebraic quotient in 493: [[§38 The First Isomorphism Theorem#^thm-38-1|493 §38.1]]; $\mathbb{RP}^n$ as the quotient $S^n/(x \sim -x)$ in 590: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 Def. §28.2]].

The classical groups through the course: defined in [[§10 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§15 Example꞉ The Classical Groups|Example: The Classical Groups]]; topological manifolds as level sets in [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§12 Group Actions and Orbit Spaces#^ex-12-4|the rotations of the plane]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§13 Homogeneous Spaces#^ex-13-2|the isotropy of the north pole]] and [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|the orthogonal group]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|the unitary group]]; their tangent spaces at the identity in [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|The Classical Groups]], with [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|The Double Cover]].

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Example꞉ Complex Projective Space|Example: Complex Projective Space]], an orbit map in [[§12 Group Actions and Orbit Spaces#^ex-12-3|projective space as an orbit space]]; the first is the quotient map of [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§17 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; [[§38 Example꞉ Projective Spaces and the Hopf Fibration|Example: Projective Spaces and the Hopf Fibration]] shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|The Double Cover]].

![[m591-35-2.svg]]
*(a) For $q = \cos t + \sin t\, u$, with $u \in \mathbb{H}_0$ a unit vector, $C_q(v) = q v \bar q$ fixes the axis $u$ and turns $v$ by the angle $2t$ about it, along the dashed circle traced by the tip of $v$: [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5]](3) with $\theta = 2t$. (b) Why it is two-to-one: the great circle $\gamma(t) = \cos t + \sin t\, u$ in $S^3$, drawn as a circle, is mapped by $C$ onto the loop of rotations about $u$ in $\mathrm{SO}(3)$. The antipodal points $q$ and $-q = \gamma(t + \pi)$ (red) give the same rotation $C_q = C_{-q}$, by the angle $2t$, and $\pm 1$ both give $I$ ([[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|§39.5]](2)). The first half of the circle, $t \in [0, \pi]$ (blue), already goes once around the loop of rotations, and the second half (orange) goes around it again: once around the circle is twice around the rotations, the double cover of [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8]]. (Drawn for these notes in the vault; not in the course tex.)*

> [!remark] Remark: What the Example Shows
> $G$ is a local diffeomorphism ([[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]]) that is not a diffeomorphism: locally $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are indistinguishable — their tangent spaces at $I$ are isomorphic, and $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ — but globally $\mathrm{SU}(2) \cong S^3$ wraps twice around $\mathrm{SO}(3) \cong \mathbb{RP}^3$. Every fibre $G^{-1}(A) = \{\pm g\}$ is two points, and $G$ is a proper ([[§37 Embeddings#^def-37-2|Def. §37.2]]) surjective submersion ([[§32 Submersions#^def-32-1|Def. §32.1]]) onto the connected $\mathrm{SO}(3)$, so Ehresmann's theorem ([[§34 Fibrations#^thm-34-3|Theorem §34.3]], stated without proof) makes it a fibration ([[§34 Fibrations#^def-34-1|Def. §34.1]]) whose fibre is two points: a double cover. The smooth version of the last statement — that $\bar C$ is a diffeomorphism for the smooth structure of $\mathbb{RP}^3$ — needs the quotient map $S^3 \to \mathbb{RP}^3$ to be a local diffeomorphism, and is not proved here.

^rem-39-1

> [!remark]- Connections
> - The quotient map $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§38 Example꞉ Projective Spaces and the Hopf Fibration#^ex-38-1|Ex. §38.1]]; bijective local diffeomorphisms: [[§31 Local Diffeomorphisms#^cor-31-3|§31.3]].
> - Covering maps: [[§31 Local Diffeomorphisms#^rem-31-2|Remark: Covering Maps]]; in 590: [[§24 Covering Spaces#^def-24-2|590 Def. §24.2]], [[Properties of the Lifting Correspondence|590 §24.9]].
