---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 7
tags: [differentiable-manifolds, math591]
---
← [[§6 Open Quotients]] · ↑ [[· 1 Topological Manifolds]] · [[§8 Spheres]] →

*Thread: equations — Manifolds cut out as level sets. It sits in this chapter because the next one needs it: $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$ and $\mathrm{U}(n)$ are level sets.*

*Reference: Lee Appendix C (Inverse and Implicit Function Theorems); MATH 452. The theorem itself is PSet 1, Problem 6.*

> [!remark] Remark: Why This Section
> [[§3 Subspaces and Products|§3]]–[[§6 Open Quotients|§6]] built manifolds out of manifolds. This section builds them out of *equations*: given a smooth map $F$ on an open subset of $\mathbb{R}^{n+k}$, when is the solution set $\{F = c\}$ a topological manifold, and of what dimension? The answer — whenever the $k$ equations are independent at every solution — is the single most productive source of examples in the course. It produces the spheres, every classical matrix group ([[§11 Topological Groups and Classical Matrix Groups|§11]]), and in its smooth form every example of [[· 3 Smooth Structures|Chapter 3]]. The machinery is multivariable calculus, and the one theorem taken on faith is the [[§7 The Regular Value Theorem#^thm-7-1|implicit function theorem]].

^rem-7-1

## The Jacobian and the Rank Condition

> [!definition] Definition §7.1: Jacobian Matrix
> Let $F = (F_1, \ldots, F_m) : \mathbb{R}^N \to \mathbb{R}^m$ be $C^1$ and $p \in \mathbb{R}^N$. The **Jacobian matrix** of $F$ at $p$ is the $m \times N$ matrix of partial derivatives
>
> $$
> DF_p = \begin{pmatrix}
> \dfrac{\partial F_1}{\partial x_1}(p) & \cdots & \dfrac{\partial F_1}{\partial x_N}(p) \\[2mm]
> \vdots & & \vdots \\[1mm]
> \dfrac{\partial F_m}{\partial x_1}(p) & \cdots & \dfrac{\partial F_m}{\partial x_N}(p)
> \end{pmatrix},
> \qquad \text{row } a = \nabla F_a(p),
> $$
>
> regarded as the linear map $DF_p : \mathbb{R}^N \to \mathbb{R}^m$, $v \mapsto DF_p\, v$. It is the derivative of $F$ at $p$: $F(p + v) = F(p) + DF_p\, v + o(|v|)$, and the [[Multivariable Chain Rule|chain rule]] for a curve reads $\frac{d}{dt} F(\gamma(t)) = DF_{\gamma(t)}\, \gamma'(t)$. For $m = 1$ the Jacobian is the single row $\nabla F(p)$, and $DF_p\, v = \nabla F(p) \cdot v$.
>
> *Lee: App. C, Total and Partial Derivatives*

^def-7-1

> [!remark]- Connections
> - Home in 452: the total derivative and Jacobian, [[§7 Differentiability#^def-7-2|452 Def. §7.2]] and [[§16 The Inverse Function Theorem#^def-16-1|452 Def. §16.1]]; the differential, [[§10 The Differential#^def-10-1|452 Def. §10.1]].
> - Coordinate-free differential: [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]].

> [!definition] Definition §7.2: Rank
> The **rank** of an $m \times N$ matrix is the dimension of its image in $\mathbb{R}^m$, equivalently the number of linearly independent rows (equivalently, columns). It is at most $\min(m, N)$. The Jacobian $DF_p$ of [[§7 The Regular Value Theorem#^def-7-1|Definition §7.1]] has **rank $m$** (**full rank** when $N \ge m$) iff it is surjective onto $\mathbb{R}^m$, iff the $m$ gradients $\nabla F_1(p), \ldots, \nabla F_m(p)$ are linearly independent. For $m = 1$ this just says $\nabla F(p) \neq 0$; for $m = 2$ it says $\nabla F_1(p)$ and $\nabla F_2(p)$ are nonzero and not parallel.
>
> *Lee: App. C, Total and Partial Derivatives*

^def-7-2

> [!remark]- Connections
> - Rank: [[§9 Matrices#^ladr-3-58|LADR 3.58]]; row rank equals column rank, [[§9 Matrices#^ladr-3-57|LADR 3.57]].
> - The rank of a smooth map of manifolds: [[§30 The Differential in Coordinates#^def-30-1|Def. §30.1]].

## Regular Points and Regular Values

> [!definition] Definition §7.3: Regular Point
> Let $F : \mathbb{R}^N \to \mathbb{R}^m$ be $C^1$. A point $p \in \mathbb{R}^N$ is a **regular point** of $F$ if the Jacobian $DF_p : \mathbb{R}^N \to \mathbb{R}^m$ ([[§7 The Regular Value Theorem#^def-7-1|Definition §7.1]]) is surjective, i.e. has rank $m$ ([[§7 The Regular Value Theorem#^def-7-2|Definition §7.2]]). Otherwise $p$ is a **critical point**. For scalar-valued $F$ ($m = 1$) the Jacobian is the row vector $\nabla F(p)$, and $p$ is a regular point iff $\nabla F(p) \neq 0$.
>
> *Lee: Ch. 5, p. 105*

^def-7-3

> [!remark]- Connections
> - The same notion defined again later, for smooth maps of manifolds: [[§30 The Differential in Coordinates#^def-30-2|Def. §30.2]] and [[§34 Submersions#^def-34-3|Def. §34.3]].

> [!definition] Definition §7.4: Regular Value
> Let $F : \mathbb{R}^N \to \mathbb{R}^m$ be $C^1$. A value $c \in \mathbb{R}^m$ is a **regular value** of $F$ if every point of the level set $F^{-1}(c)$ is a regular point ([[§7 The Regular Value Theorem#^def-7-3|Definition §7.3]]). Otherwise $c$ is a **critical value**. (If $F^{-1}(c) = \emptyset$, then $c$ is vacuously a regular value.) So for scalar-valued $F$, $c \in \mathbb{R}$ is a regular value iff $\nabla F$ vanishes nowhere on $F^{-1}(c)$.
>
> *Lee: Ch. 5, p. 105, with the same convention that $c$ is regular when $F^{-1}(c) = \emptyset$*

^def-7-4

> [!remark]- Connections
> - The same notion defined again later: without coordinates, [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]]; for smooth maps of manifolds, [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]] and [[§34 Submersions#^def-34-4|Def. §34.4]].

> [!remark] Remark: The Constraint $N \ge m$
> Regular points can exist only when $N \ge m$, and the case $N = m$ is special; both facts are made precise in [[§7 The Regular Value Theorem#^prop-7-5|Proposition §7.5]], once the regular value theorem is available. Geometrically, one cannot cut an $N$-dimensional space down by more than $N$ independent constraints and have anything left — the dimension count $N - m$ would be negative. The boundary case $N = m$ belongs to the *inverse* function theorem rather than the implicit one. The situation of interest below is $N = n^2$, $m = 1$.

^rem-7-2

> [!example] Example §7.1: Regular and Critical Values of $x^2 + y^2$
> Let $f(x,y) = x^2 + y^2$ on $\mathbb{R}^2$, so $\nabla f = (2x, 2y)$, which vanishes only at the origin. Then $c > 0$ is a regular value and $f^{-1}(c)$ is a circle, a $1$-manifold; $c = 0$ is a critical value and $f^{-1}(0) = \{(0,0)\}$ is a single point, not a $1$-manifold; $c < 0$ is vacuously regular. Note the logic: one critical point on the level set makes the value critical, while the value stays regular no matter how many critical points $f$ has *off* that level set.

^ex-7-1

> [!remark]- Connections
> - The circle as a level set in 452: [[Unit circle and unit sphere]], [[§15 The Implicit Function Theorem#^ex-15-1|452 Ex. §15.1]].

> [!remark] Remark: Why the Notion Matters
> The definition is tailored to the Implicit Function Theorem: at a regular point of $F : \mathbb{R}^N \to \mathbb{R}^m$, the $m$ independent gradients $\nabla F_a(p)$ span an $m$-dimensional space of “constraint directions,” and one can solve the $m$ equations $F = c$ for $m$ of the coordinates as functions of the remaining $N - m$, so $F^{-1}(c)$ is locally a graph over the complementary $N - m$ directions. That is where the dimension $N - m$ comes from. For $\mathrm{O}(n)$ the constraint is $gg^{\mathsf T} = I$, which is $m = \tfrac{n(n+1)}{2}$ scalar equations (the independent entries of a symmetric matrix), and the task is precisely to show these $m$ gradients are independent at every orthogonal $g$; this is done in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Example §23.1]]. The general statement—*if $c$ is a regular value of $F$, then $F^{-1}(c)$ is a topological (indeed smooth) manifold of dimension $N - m$*—is [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] (PSet 1, Problem 6); the $m = 1$ case is carried out for $\det$ in Proposition [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]] below.

^rem-7-3

![[m591-4-1.svg]]
*Two equations in $\mathbb{R}^3$: a sphere and a plane meeting transversally (left, rank $2$, a curve) and tangentially (right, rank $1$, a single point).*

The figure is the case $N = 3$, $m = 2$: two equations in $\mathbb{R}^3$, each level set a surface, the common level set their intersection. On the left the sphere $x^2+y^2+z^2 = 1$ meets the plane $z = c$ with $|c| < 1$ transversally, the two gradients at a point of intersection are independent, the Jacobian has rank $2$, and the intersection is a curve of dimension $3 - 2 = 1$. On the right, $F = (x^2+y^2+z^2-1,\, z-1)$: both components have nonvanishing gradient, but at the tangency $(0,0,1)$ they are parallel, so

$$
DF_{(0,0,1)} = \begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 1 \end{pmatrix}
$$

has rank $1$, and $F^{-1}(\vec 0)$ is the single point $(0,0,1)$ rather than the predicted curve. This is what the scalar case $m = 1$ cannot show: there the hypothesis reads “$\nabla F \neq 0$” and looks like a condition on one function, whereas it is really a condition on the gradients *jointly*.

## The Implicit Function Theorem

> [!theorem] Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40
> Let $U \subseteq \mathbb{R}^n \times \mathbb{R}^k$ be an open subset, with standard coordinates written $(x, y) = (x^1, \ldots, x^n, y^1, \ldots, y^k)$. Suppose $\Phi : U \to \mathbb{R}^k$ is smooth, $(a, b) \in U$, and $c = \Phi(a,b)$. If the $k \times k$ matrix
>
> $$
> \left( \frac{\partial \Phi^i}{\partial y^j}(a, b) \right)_{1 \le i, j \le k}
> $$
>
> is nonsingular, then there exist neighborhoods $V_0 \subseteq \mathbb{R}^n$ of $a$ and $W_0 \subseteq \mathbb{R}^k$ of $b$ and a smooth function $F : V_0 \to W_0$ such that $\Phi^{-1}(c) \cap (V_0 \times W_0)$ is the graph of $F$; that is, for $(x,y) \in V_0 \times W_0$,
>
> $$
> \Phi(x, y) = c \iff y = F(x).
> $$
>
> *Lee: Theorem C.40*

^thm-7-1

> [!proof]+ Proof (sketch)
> Lee deduces this from the Inverse Function Theorem ([[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1]]; Lee, Theorem C.34), applied to the auxiliary map $(x,y) \mapsto (x, \Phi(x,y))$, whose total derivative is block lower triangular with nonsingular diagonal blocks $I_n$ and $(\partial\Phi^i/\partial y^j)$. Special cases are proved in MATH 452 (one equation: [[Implicit Function Theorem|452 §12]]; two variables: [[Inverse Function Theorem (several variables)|452 §13]]); Lee's proofs are in Appendix C.

^pf-7-1

*Uses:* [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[Inverse Function Theorem (several variables)|452 §16.2]]

> [!remark]- Connections
> - The one-equation version is proved in 452: [[§15 The Implicit Function Theorem#^thm-15-2|452 §15.2]] (hub: [[Implicit Function Theorem]]); this vector-valued version has its home here.
> - Deduced from the inverse function theorem: [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]] in this course (452 proves only the two-variable case, [[Inverse Function Theorem (several variables)]]).

> [!remark] Remark: Which Variables Are Solved For
> The theorem does not say the level set is a graph over some canonical set of coordinates: it says that *if* the $k$ coordinates $y$ are ones for which the square block $(\partial\Phi^i/\partial y^j)$ is invertible, *then* those $y$ can be solved for in terms of the remaining $n$. Since $D\Phi_{(a,b)}$ has rank $k$ exactly when *some* $k$ of its $n + k$ columns are independent, a regular point always admits such a splitting—after permuting coordinates. That permutation is the “WLOG” step in the proof of Proposition [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]] below.

^rem-7-4

We need only the scalar case $k = 1$. Write $N = n^2$ and points of $\mathbb{R}^N$ as $x = (x', x_N)$ with $x' \in \mathbb{R}^{N-1}$.

> [!theorem] Corollary §7.2: Implicit Function Theorem — Scalar Case
> Let $F : \mathbb{R}^N \to \mathbb{R}$ be smooth, let $a = (a', a_N)$ with $F(a) = c$, and suppose $\dfrac{\partial F}{\partial x_N}(a) \neq 0$. Then there exist an open set $W' \subseteq \mathbb{R}^{N-1}$ containing $a'$, an open interval $J \subseteq \mathbb{R}$ containing $a_N$, and a smooth function $h : W' \to J$ with $h(a') = a_N$ such that for all $(x', x_N) \in W' \times J$,
>
> $$
> F(x', x_N) = c \iff x_N = h(x').
> $$
>
> *Lee: Theorem C.40 with $k = 1$*

^cor-7-2

> [!proof]+ Proof
> [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1]] with $n = N - 1$, $k = 1$, $\Phi = F$: the $1 \times 1$ matrix $(\partial F/\partial x_N(a))$ is nonsingular precisely when $\partial F/\partial x_N(a) \neq 0$. Set $h = F$ in Lee's notation, and note $h(a') = a_N$ because $(a', a_N)$ lies in the level set and in $V_0 \times W_0$.

^pf-7-2

*Uses:* [[§7 The Regular Value Theorem#^thm-7-1|§7.1]]

> [!remark]- Connections
> - Home of the scalar statement: [[§15 The Implicit Function Theorem#^thm-15-2|452 §15.2]] (the $n$-variable, one-equation IFT, proved there from the two-variable case [[§15 The Implicit Function Theorem#^thm-15-1|452 §15.1]]).

## The Regular Value Theorem

> [!theorem] Theorem §7.3: Regular Value Theorem
> Let $F : \mathbb{R}^{n+k} \to \mathbb{R}^k$ be smooth and suppose $\vec 0 \in \mathbb{R}^k$ is a regular value of $F$, i.e. the Jacobian $F'(p)$ has rank $k$ at every $p \in X := F^{-1}(\vec 0)$. Then $X$, with the subspace topology, is a topological manifold of dimension $n$.
>
> *Lee: Example 1.32 and Corollary 5.14*

^thm-7-3

> [!proof]+ Proof (PSet 1, Problem 6)
> *Hausdorff and second countable.* $X$ is a subspace of $\mathbb{R}^{n+k}$, so both properties are inherited ([[§3 Subspaces and Products#^thm-3-5|Theorem §3.5]]).
>
> *Locally Euclidean.* Fix $p \in X$.
>
> *Step 1 (relabelling the coordinates).* $F'(p)$ is a $k \times (n+k)$ matrix of rank $k$, so $k$ of its $n+k$ columns are linearly independent. Let $\rho : \mathbb{R}^{n+k} \to \mathbb{R}^{n+k}$ be the coordinate permutation carrying those $k$ positions to the last $k$, and put $\widetilde F = F \circ \rho^{-1}$. Then $\widetilde F$ is smooth, $\widetilde F^{-1}(\vec 0) = \rho(X)$, and $\widetilde F'(\rho(p)) = F'(p)\,\rho^{-1}$ is $F'(p)$ with its columns permuted, so its last $k$ columns are independent. As $\rho$ restricts to a homeomorphism $X \to \rho(X)$, and local Euclideanness is a topological property, we may replace $(X, F, p)$ by $(\rho(X), \widetilde F, \rho(p))$: WLOG, writing the coordinates as $(x,y) \in \mathbb{R}^n \times \mathbb{R}^k$, the $k \times k$ matrix $\big(\partial F^i/\partial y^j (p)\big)$ — the last $k$ columns of $F'(p)$ — is nonsingular.
>
> *Step 2 (the implicit function theorem).* Write $p = (a,b)$. By [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1]] applied to $\Phi = F$ on $U = \mathbb{R}^{n+k}$ with $c = \vec 0$, there are neighborhoods $V_0 \subseteq \mathbb{R}^n$ of $a$ and $W_0 \subseteq \mathbb{R}^k$ of $b$ and a smooth $G : V_0 \to W_0$ with
>
> $$
> F(x,y) = \vec 0 \iff y = G(x) \qquad \text{for } (x,y) \in V_0 \times W_0. \tag{*}
> $$
>
> *Step 3 (the level set is locally a graph).* Put $U_p = X \cap (V_0 \times W_0)$, an open neighborhood of $p$ in $X$. By $(\ast)$,
>
> $$
> U_p = \{\, (x, G(x)) \mid x \in V_0 \,\} :
> $$
>
> “$\supseteq$” because $(x,G(x)) \in V_0 \times W_0$ satisfies $F = \vec 0$, “$\subseteq$” because a point of $U_p$ over $x$ has second coordinate $G(x)$. The maps
>
> $$
> \varphi : U_p \to V_0,\ \varphi(x,y) = x, \qquad \psi : V_0 \to U_p,\ \psi(x) = (x, G(x))
> $$
>
> are mutually inverse; $\varphi$ is continuous as a restriction of the projection, and $\psi$ is continuous because its two components $\mathrm{id}$ and $G$ are ([[§3 Subspaces and Products#^thm-3-10|Theorem §3.10]] and [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]]). So $\varphi$ is a homeomorphism onto the open set $V_0 \subseteq \mathbb{R}^n$, and [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] gives local Euclideanness of dimension $n$ at $p$.

^pf-7-3

*Uses:* [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[Multivariable Chain Rule|452 §12.2 (chain rule)]], [[§9 Matrices#^ladr-3-57|LADR 3.57]]

> [!remark]- Connections
> - The smooth structure on $X$: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; for level sets of maps between manifolds: [[§30 The Differential in Coordinates#^cor-30-8|§30.8]] and [[§35 Regular Submanifolds#^thm-35-7|§35.7]].
> - Recovered as a special case of transversality: [[§26 Transversality#^cor-26-3|§26.3]].

> [!theorem] Corollary §7.4: Open Domains and Arbitrary Values
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, and $c \in \mathbb{R}^k$ a regular value of $F$ — [[§7 The Regular Value Theorem#^def-7-4|Definition §7.4]], applied to $F$ on $W$: the Jacobian $F'(p)$ has rank $k$ at every $p \in F^{-1}(c)$. Then $F^{-1}(c)$, with the subspace topology, is a topological manifold of dimension $n$.

^cor-7-4

> [!proof]+ Proof
> The proof of [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] is local, and uses the domain and the value only through the implicit function theorem, which is stated for an arbitrary open set and value ([[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1]]). Repeat it with $W$ in place of $\mathbb{R}^{n+k}$ and $c$ in place of $\vec 0$: the permutation $\rho$ of Step 1 carries $W$ to the open set $\rho(W)$; Step 2 applies [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1]] on $U = \rho(W)$ at the value $c$; Step 3 is unchanged. Hausdorffness and second countability are inherited from $\mathbb{R}^{n+k}$ as before.

^pf-7-4

*Uses:* [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§3 Subspaces and Products#^thm-3-5|§3.5]]

This is the form needed on manifolds, where a chart has an open subset of Euclidean space as its image, not the whole space. The general version, for maps between manifolds and with the smooth structure and the tangent space included, is [[§35 Regular Submanifolds#^thm-35-7|Theorem §35.7]] (Lecture 12).

**Comparison with Lee.** Lee meets level sets twice. Example 1.32 builds graph charts for the level set of a single function with nonvanishing gradient, and Corollary 5.14 proves, via the constant-rank theorem, that every regular level set is a properly embedded submanifold. The course takes the direct route of Example 1.32 in every codimension, using the implicit function theorem, and obtains the smooth structure separately ([[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]]).

![[m591-4-2.svg]]
*The scalar case in $\mathbb{R}^2$: the circle as a graph over $x$ (left) and over $y$ (middle), and the crossing lines $x^2 = y^2$ at a critical point (right).*

The scalar case $N = 2$, $m = 1$, where every step of the proof is visible at once. *Left:* $F = x^2+y^2-1$; at a point off the horizontal axis $\partial F/\partial y \neq 0$, so the implicit function theorem solves $y = h(x) = \sqrt{1-x^2}$ and the thick arc is the graph over the $x$-interval beneath it — the chart is “project to $x$,” which is exactly $\varphi_2$ of [[§17 Differentiable Structures#^ex-17-2|Example §17.2]]. *Middle:* at $(1,0)$ that partial vanishes and the curve is vertical, so no interval of $x$ works; but $\partial F/\partial x \neq 0$, so one solves $x = h(y)$ and projects to $y$ instead. That switch is the permutation-of-coordinates step in the proof, and the picture shows it is not a technicality: which coordinate can be solved for changes from point to point. *Right:* at a critical point the conclusion fails — near the origin $\{x^2 = y^2\}$ is two crossing lines, a graph over neither axis.

> [!remark] Remark: Reading the Dimension
> The level set of $k$ independent equations in $\mathbb{R}^{n+k}$ has dimension $(n+k) - k = n$: each independent constraint costs one dimension. The independence is exactly the rank condition, and it is needed at every point of the level set, not just at one — that is what “regular *value*” means ([[§7 The Regular Value Theorem#^def-7-4|Definition §7.4]]). The theorem is the general form of the computation carried out for $\mathrm{SL}(n,\mathbb{R})$ in [[§12 The Classical Groups Are Topological Manifolds|§12, The Classical Groups Are Topological Manifolds]], the case $k = 1$, $n + k = n^2$; the smooth version, giving $X$ a smooth structure rather than just a topology, comes in [[· 3 Smooth Structures|Chapter 3]].

^rem-7-5

> [!theorem] Proposition §7.5: Regular Points When $N \le m$
> Let $W \subseteq \mathbb{R}^N$ be open and $F : W \to \mathbb{R}^m$ smooth.
> 1. $\operatorname{rank} DF_p \le \min(m, N)$ at every $p$. So if $N < m$, every point of $W$ is critical, and $c$ is a regular value if and only if $F^{-1}(c) = \emptyset$.
> 2. If $N = m$, then $p$ is a regular point if and only if $\det DF_p \ne 0$, and every regular level set $F^{-1}(c)$ is discrete: each of its points is isolated.

^prop-7-5

> [!proof]+ Proof
> (1) An $m \times N$ matrix has at most $\min(m,N)$ independent rows. If $N < m$, the rank is at most $N < m$, so $DF_p$ is never surjective and no point is regular; the condition defining a regular value then holds exactly when there is nothing to check. (2) A square matrix has maximal rank iff it is invertible. If $c$ is a regular value, [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] applies with $n = 0$ and $k = m$, so $F^{-1}(c)$ is a manifold of dimension $0$, hence discrete by [[§2 Topological Manifolds#^prop-2-5|Proposition §2.5]].

^pf-7-5

*Uses:* [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§2 Topological Manifolds#^prop-2-5|§2.5]], [[§9 Matrices#^ladr-3-57|LADR 3.57]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

> [!example] Example §7.2: A Level Set in $\mathbb{R}^4$
> *(Qualifying Review, August 2013; Assignment 2, Problem 3.)* Define
>
> $$
> F : \mathbb{R}^4 \to \mathbb{R}^2, \qquad F(x,y,u,v) = \big(x^2 - y^2 - u^2 + v^2 + 2u,\ \ 2xy - 2uv + 2v\big),
> $$
>
> and $M = F^{-1}(-1,0)$. Then $(-1,0)$ is a regular value of $F$, so $M$ is a manifold of dimension $2$; and at $x_0 = (0,1,0,0) \in M$,
>
> $$
> \ker F'(x_0) = \operatorname{span}\{(1,0,0,-1),\ (0,1,1,0)\}.
> $$

^ex-7-2

> [!proof]+ Working out the example
> *Step 1: the Jacobian.* Writing $a = 2x$, $b = 2y$, $c = 2 - 2u$, $d = 2v$,
>
> $$
> F'(p) = \begin{pmatrix} 2x & -2y & 2 - 2u & 2v \\ 2y & 2x & -2v & 2 - 2u \end{pmatrix}
> = \begin{pmatrix} a & -b & c & d \\ b & a & -d & c \end{pmatrix}.
> $$
>
> *Step 2: where the rank drops.* A $2 \times 4$ matrix has rank $< 2$ iff its rows are linearly dependent. If the second row is $0$ then $a = b = c = d = 0$. Otherwise the first is $\gamma$ times the second for some real $\gamma$; comparing entries, $a = \gamma b$ and $-b = \gamma a = \gamma^2 b$, so $b(1+\gamma^2) = 0$, whence $b = 0 = a$; likewise $c = -\gamma d$ and $d = \gamma c = -\gamma^2 d$ force $d = 0 = c$ — so this case is vacuous. Either way $a = b = c = d = 0$, i.e. $p = p_0 := (0,0,1,0)$: the rank is $2$ everywhere except at the single point $p_0$.
>
> *Step 3: the bad point misses the level set.* $F(p_0) = (0 - 0 - 1 + 0 + 2,\ 0) = (1,0) \neq (-1,0)$, so $p_0 \notin M$ and $F'(p)$ has rank $2$ at every $p \in M$: $(-1,0)$ is a regular value.
>
> *Step 4: the manifold.* By [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]], $M$ is a topological manifold of dimension $4 - 2 = 2$, smooth by [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]].
>
> *Step 5: the kernel at $x_0$.* First $F(0,1,0,0) = (-1,0)$, so $x_0 \in M$. At $x_0$,
>
> $$
> F'(x_0) = \begin{pmatrix} 0 & -2 & 2 & 0 \\ 2 & 0 & 0 & 2 \end{pmatrix},
> \qquad
> F'(x_0)\begin{pmatrix} x \\ y \\ u \\ v \end{pmatrix} = \begin{pmatrix} -2y + 2u \\ 2x + 2v \end{pmatrix},
> $$
>
> which vanishes iff $u = y$ and $v = -x$. So $\ker F'(x_0) = \{(x, y, y, -x)\}$, spanned by the two displayed vectors, of dimension $2 = \dim M$ as it must be. By [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] this kernel is the geometric tangent space $T^{\mathrm{geo}}_{x_0}M$.

^pf-ex-7-2

*Uses:* [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]

> [!remark]- Connections
> - The notion of submanifold the problem asks about: [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]; regular level sets are submanifolds by [[§35 Regular Submanifolds#^thm-35-7|§35.7]].

> [!remark] Remark
> **The workflow.** Every problem of this type runs the same five steps: (i) compute the Jacobian; (ii) find the locus where its rank drops; (iii) check that this locus *misses the level set*; (iv) read off the dimension; (v) compute the kernel. Step (iii) is the one most often skipped, and it is the point of the definition: the rank may drop anywhere at all, so long as it does not drop *on* $F^{-1}(c)$. Here it drops at exactly one point of $\mathbb{R}^4$, which happens to lie on a different level set.

^rem-7-6

**On the word “submanifold.”** The problem asks to show $M$ is a *submanifold* of $\mathbb{R}^4$, a notion not yet defined in the course; Assignment 2's own background defers it (“after the theory of submanifolds is developed”). What has been proved is that $M$ is a smooth manifold, and that its topology is the subspace topology from $\mathbb{R}^4$.

## Holomorphic Level Sets

Step 2 of [[§7 The Regular Value Theorem#^ex-7-2|Example §7.2]] found something it did not look for: the rank of $F'(p)$ is either $2$ or $0$, and never $1$. That is not a coincidence of this particular $F$. With $z = x + iy$ and $w = u + iv$,

$$
F = (\operatorname{Re} f,\ \operatorname{Im} f), \qquad f(z,w) = z^2 - w^2 + 2w,
$$

as expanding $f$ shows; so $F$ is a complex polynomial in disguise, and its rank behaviour is forced by the complex structure. This subsection makes that precise. Throughout, $\mathbb{C}^m \cong \mathbb{R}^{2m}$ as in [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Definition §11.9]].

![[m591-4-3.svg]]
*The map: $f$ on $\mathbb{C}^2$ and $F$ on $\mathbb{R}^4$, related by the identifications $\mathbb{C}^m \cong \mathbb{R}^{2m}$.*

![[m591-4-4.svg]]
*Its derivative at a point: the complex gradient $f'(p)$ and the real Jacobian $F'(p)$.*

Left, the map; right, its derivative at a point. The vertical arrows are the identifications of [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Definition §11.9]]. On the right, the top arrow is the complex gradient $(2z,\ 2-2w)$, a $1 \times 2$ complex matrix, and the bottom arrow is the real $2 \times 4$ Jacobian of [[§7 The Regular Value Theorem#^ex-7-2|Example §7.2]]. Everything that follows is about what the top row forces on the bottom one.

> [!definition] Definition §7.5: Holomorphic Map
> Let $W \subseteq \mathbb{C}^N$ be open. A map $F : W \to \mathbb{C}^m$ is **holomorphic** if it is $C^1$ as a map between open subsets of $\mathbb{R}^{2N}$ and $\mathbb{R}^{2m}$ and its real derivative $DF_p : \mathbb{C}^N \to \mathbb{C}^m$ is $\mathbb{C}$-linear at every $p \in W$. The $\mathbb{C}$-linear map $DF_p$ is then written $F'(p)$, the **complex Jacobian**, an $m \times N$ complex matrix of partial derivatives $\partial F_a / \partial z_b$.

^def-7-5

> [!remark] Remark
> $\mathbb{C}$-linearity of $DF_p$ is the Cauchy–Riemann condition. For $N = m = 1$: multiplication by $\alpha = a + ib$ sends $h = h_1 + i h_2$ to $(a h_1 - b h_2) + i(b h_1 + a h_2)$, so as a real $2 \times 2$ matrix
>
> $$
> h \mapsto \alpha h \quad\text{is}\quad \begin{pmatrix} a & -b \\ b & a \end{pmatrix}.
> $$
>
> A real $2 \times 2$ matrix is of this form iff it commutes with multiplication by $i$. Polynomials in $z_1, \ldots, z_N$ (with no $\bar z_j$) are holomorphic, by the product and chain rules; maps involving complex conjugation generally are not.

^rem-7-7

> [!theorem] Lemma §7.6: Real Rank of a Complex-Linear Map
> Let $A : \mathbb{C}^N \to \mathbb{C}^m$ be $\mathbb{C}$-linear of complex rank $r$. Regarded as an $\mathbb{R}$-linear map $\mathbb{R}^{2N} \to \mathbb{R}^{2m}$, it has real rank $2r$. In particular the real rank of a $\mathbb{C}$-linear map is always even.

^lem-7-6

> [!proof]+ Proof
> The image of $A$ is a complex subspace $V$ of complex dimension $r$; it suffices to show $\dim_{\mathbb{R}} V = 2r$. Let $v_1, \ldots, v_r$ be a complex basis of $V$. Then $v_1, iv_1, \ldots, v_r, iv_r$ span $V$ over $\mathbb{R}$, since $\sum_j c_j v_j = \sum_j \big(\operatorname{Re} c_j\, v_j + \operatorname{Im} c_j\,(i v_j)\big)$; and they are $\mathbb{R}$-independent, since $\sum_j (a_j v_j + b_j\, i v_j) = 0$ with $a_j, b_j$ real says $\sum_j (a_j + i b_j) v_j = 0$, forcing every $a_j + i b_j = 0$. So they form a real basis of $2r$ vectors.

^pf-7-6

*Uses:* [[§8 Null Spaces and Ranges#^ladr-3-18|LADR 3.18]], [[§5 Bases#^ladr-2-26|LADR 2.26]], [[§9 Matrices#^ladr-3-58|LADR 3.58]]

> [!theorem] Corollary §7.7: Holomorphic Regular Value Theorem
> Let $W \subseteq \mathbb{C}^{n+k}$ be open, $F : W \to \mathbb{C}^k$ holomorphic, and $c \in \mathbb{C}^k$ such that the complex Jacobian $F'(p)$ has complex rank $k$ at every $p \in F^{-1}(c)$. Then $F^{-1}(c)$ is a manifold of *real* dimension $2n$, smooth by [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]]. Moreover, for any holomorphic $F$ the real rank of $DF_p$ is even at every point; for $k = 1$ it is $0$ or $2$. And for $p \in F^{-1}(c)$ the kernel of $F'(p)$ is a complex subspace of $\mathbb{C}^{n+k}$; by [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] it is the geometric tangent space $T^{\mathrm{geo}}_p F^{-1}(c)$.
>
> *Lee: no counterpart; from Assignment 2*

^cor-7-7

> [!proof]+ Proof
> By [[§7 The Regular Value Theorem#^lem-7-6|Lemma §7.6]], complex rank $k$ means real rank $2k$, which is the maximal rank for a real map $\mathbb{R}^{2n+2k} \to \mathbb{R}^{2k}$. So $c$ is a regular value of $F$ regarded as a real map, and [[§7 The Regular Value Theorem#^thm-7-3|Theorem §7.3]] gives a manifold of dimension $(2n+2k) - 2k = 2n$. Evenness of the rank is the lemma again. The kernel of a $\mathbb{C}$-linear map is closed under multiplication by $i$, hence a complex subspace.

^pf-7-7

*Uses:* [[§7 The Regular Value Theorem#^lem-7-6|§7.6]], [[§7 The Regular Value Theorem#^def-7-5|Def. §7.5]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]]

> [!remark] Remark: The Example Re-read
> For $f(z,w) = z^2 - w^2 + 2w$ the complex Jacobian is the row $(2z,\ 2 - 2w)$. In the notation of [[§7 The Regular Value Theorem#^ex-7-2|Example §7.2]], $2z = a + ib$ and $2 - 2w = c - id$, and the $\mathbb{C}$-linear functional $(h, k) \mapsto (a+ib)h + (c-id)k$ has real and imaginary parts
>
> $$
> \operatorname{Re}:\ (a,\ -b,\ c,\ d), \qquad \operatorname{Im}:\ (b,\ a,\ -d,\ c)
> $$
>
> — exactly the two rows computed in Step 1. So the case analysis of Step 2 was [[§7 The Regular Value Theorem#^lem-7-6|Lemma §7.6]] in disguise: the real rank is $2$ precisely when the complex gradient $(2z, 2-2w)$ is nonzero, i.e. away from $(z,w) = (0,1)$, and $0$ there, never $1$.
>
> The kernel is complex too. At $x_0$, i.e. $(z,w) = (i, 0)$, the complex gradient is $(2i, 2)$, and its kernel is the complex line $\{2i\,h + 2k = 0\} = \{k = -i h\}$. Writing $h = h_1 + i h_2$ and $k = k_1 + i k_2$, the condition $k = -ih = h_2 - i h_1$ reads $k_1 = h_2$, $k_2 = -h_1$ — which is $\{(x,y,y,-x)\}$ from Step 5. As [[§7 The Regular Value Theorem#^cor-7-7|Corollary §7.7]] predicts, it is a complex subspace.

^rem-7-8

> [!remark] Remark: The Contrast with the Unitary Group
> The map $F(g) = gg^{\ast}$ presenting $\mathrm{U}(n)$ (Assignment 2, Problem 4) involves $\bar g$ and is *not* holomorphic: its derivative $h \mapsto hg^{\ast} + gh^{\ast}$ satisfies $DF_g(ih) = i\,hg^{\ast} - i\,gh^{\ast}$, which is not $i\,DF_g(h)$ in general. So [[§7 The Regular Value Theorem#^cor-7-7|Corollary §7.7]] is unavailable, and one is forced to regard $\operatorname{Mat}(n,\mathbb{C})$ and the Hermitian matrices as *real* vector spaces — which is exactly why that problem insists on it. The outcome shows the difference: $\dim \mathrm{U}(n) = n^2$ is odd for odd $n$ (for instance $\mathrm{U}(1) = S^1$ has dimension $1$), which no holomorphic regular level set can be.

^rem-7-9

> [!remark]- Connections
> - Assignment 2, Problem 4 worked out: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]] ($\dim \mathrm{U}(n) = n^2$); $\mathrm{U}(1) = S^1$ is [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|Ex. §11.3]].

> [!example] Example §7.3: The Level Set Is a Cylinder
> The regular value theorem says that $M$ of [[§7 The Regular Value Theorem#^ex-7-2|Example §7.2]] is a $2$-manifold, but not which one. In fact $M$ is homeomorphic to $\mathbb{C}^\times$, hence to the cylinder $S^1 \times \mathbb{R}$.

^ex-7-3

> [!proof]+ Proof
> In complex coordinates, completing the square,
>
> $$
> M = \{z^2 - (w-1)^2 = -2\} = \{(z - w + 1)(z + w - 1) = -2\}.
> $$
>
> The maps
>
> $$
> M \to \mathbb{C}^\times,\ \ (z,w) \mapsto s = z - w + 1, \qquad\qquad
> \mathbb{C}^\times \to M,\ \ s \mapsto \Big(\tfrac12\big(s - \tfrac{2}{s}\big),\ 1 - \tfrac12\big(s + \tfrac{2}{s}\big)\Big),
> $$
>
> are continuous (indeed holomorphic) and mutually inverse, because the second factor $z + w - 1 = -2/s$ is determined by the first. So $M \cong \mathbb{C}^\times$. And $\mathbb{C}^\times \cong S^1 \times \mathbb{R}$ via $s \mapsto \big(s/|s|,\ \log|s|\big)$. The base point $x_0 = (0,1,0,0)$, i.e. $(z,w) = (i,0)$, corresponds to $s = 1+i$.

^pf-ex-7-3

*Uses:* [[§7 The Regular Value Theorem#^ex-7-2|Ex. §7.2]], [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]], [[Polar and spherical coordinates]]

> [!remark]- Connections
> - $\mathbb{C}^\times = \mathbb{R}^2 \setminus \{0\}$ in 590: [[Punctured plane]], which deformation retracts onto $S^1$ ([[§35 Deformation Retracts and Homotopy Type#^ex-35-6|590 Ex. §35.6]]).

![[m591-4-5.svg]]
*The level set $M$, the parameter $s \in \mathbb{C}^\times$, and polar coordinates to the cylinder $S^1 \times \mathbb{R}$.*

$M$ upstairs in $\mathbb{C}^2$, the parameter $s$ downstairs in $\mathbb{C}^\times$, and polar coordinates $s \mapsto (s/|s|, \log|s|)$ to the cylinder. The two arrows on the left are mutually inverse, so $s$ is a single chart covering all of $M$ — something the regular value theorem, whose charts are local graphs, never promises.
