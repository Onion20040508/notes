---
type: section
subject: "[[Topology]]"
chapter: 11
section: 37
munkres: "§59"
tags: [topology, math590]
---
← [[§36 The Punctured Plane, the Figure Eight and the Torus]] · ↑ [[· 11 Computing π₁]] · [[§38 Fundamental Group of Some Surfaces]] →

The main result of this section is $\pi_1(S^n) = 0$ for $n \geq 2$ ([[Sⁿ is Simply Connected for n ≥ 2|§37.3]]). The proof requires a [[§37 The Fundamental Group of Sⁿ#^thm-37-1|general theorem]] about how $\pi_1$ interacts with open covers.

## The Generation Theorem

> [!theorem] Theorem §37.1: Generation by Open Cover (Munkres 59.1)
> Let $X = U \cup V$, where $U$ and $V$ are open in $X$. Suppose $U \cap V$ is [[§16 Connected Subspaces of ℝ#^def-16-4|path-connected]] and $x_0 \in U \cap V$. Let $i_U: U \hookrightarrow X$ and $i_V: V \hookrightarrow X$ be the inclusion maps. Then the images of the [[§29 The Fundamental Group#^def-29-4|induced homomorphisms]]
>
> $$
> i_{U*}: \pi_1(U, x_0) \to \pi_1(X, x_0) \qquad \text{and} \qquad i_{V*}: \pi_1(V, x_0) \to \pi_1(X, x_0)
> $$
>
> generate $\pi_1(X, x_0)$: every element $[\gamma] \in \pi_1(X, x_0)$ can be written as a finite product
>
> $$
> [\gamma] = [g_1] * [g_2] * \cdots * [g_n]
> $$
>
> where each $g_i$ is a loop at $x_0$ that lies entirely in $U$ or entirely in $V$. In other words, every loop in $X$ can be broken into pieces that each stay within one of the open sets.

^thm-37-1

> [!proof]+ Proof
> Let $f: I \to X$ be a loop at $x_0$. We must show $[f] = [g_1] * [g_2] * \cdots * [g_n]$ where each $g_i$ is a loop in $U$ or $V$ at $x_0$.
>
> **Step 1: Subdivide the loop into pieces that each lie in $U$ or $V$.**
>
> The sets $\{f^{-1}(U), f^{-1}(V)\}$ form an open cover of $I = [0, 1]$ (since $X = U \cup V$ and $f$ is continuous). By the **[[Lebesgue Number Lemma|Lebesgue number lemma]]** (applied to the [[§18 Compact Spaces#^thm-18-10|compact]] metric space $I$), there exists $\delta > 0$ such that every subset of $I$ with diameter less than $\delta$ is contained in either $f^{-1}(U)$ or $f^{-1}(V)$.
>
> Choose a subdivision $0 = b_0 < b_1 < \cdots < b_m = 1$ with $b_{i+1} - b_i < \delta$ for each $i$. Then $f([b_i, b_{i+1}]) \subseteq U$ or $f([b_i, b_{i+1}]) \subseteq V$ for each $i$.
>
> **Refine so that the division points map into $U \cap V$:** Some $f(b_i)$ may lie in $U$ but not $V$ (or vice versa). If $f(b_i) \in U \setminus V$, then both $f([b_{i-1}, b_i]) \subseteq U$ and $f([b_i, b_{i+1}]) \subseteq U$ (since $f(b_i) \notin V$ forces both intervals into $U$). So we can remove $b_i$ from the subdivision without losing the property. Similarly if $f(b_i) \in V \setminus U$. Repeat until all remaining division points $a_0 < a_1 < \cdots < a_n$ satisfy $f(a_i) \in U \cap V$, while each $f([a_i, a_{i+1}])$ still lies entirely in $U$ or $V$.
>
> Note: $f(a_0) = f(0) = x_0 \in U \cap V$ and $f(a_n) = f(1) = x_0 \in U \cap V$, so the endpoints are already fine.
>
> **Step 2: Decompose $f$ into paths.**
>
> For each $i = 1, \ldots, n$, define $f_i: I \to X$ by reparametrizing $f|_{[a_{i-1}, a_i]}$:
>
> $$
> f_i(s) = f(a_{i-1} + s(a_i - a_{i-1})), \qquad s \in [0, 1].
> $$
>
> This is $I \xrightarrow{\text{linear}} [a_{i-1}, a_i] \xrightarrow{f} X$. Each $f_i$ is a path from $f(a_{i-1})$ to $f(a_i)$, and lies entirely in $U$ or $V$ (by the subdivision property). By construction:
>
> $$
> [f] = [f_1] * [f_2] * \cdots * [f_n].
> $$
>
> **Step 3: Convert paths into loops at $x_0$.**
>
> Each $f_i$ is a path in $U$ or $V$, but it goes from $f(a_{i-1})$ to $f(a_i)$ — not a loop at $x_0$. We fix this using connecting paths.
>
> Since $f(a_i) \in U \cap V$ for each $i$, and $U \cap V$ is path-connected, there exist paths $\alpha_i: I \to U \cap V$ from $x_0$ to $f(a_i)$. Set $\alpha_0 = \alpha_n = e_{x_0}$ (the constant path, since $f(a_0) = f(a_n) = x_0$).
>
> Define the loops:
>
> $$
> g_i = \alpha_{i-1} * f_i * \bar{\alpha}_i, \qquad i = 1, \ldots, n.
> $$
>
> Each $g_i$ is a loop at $x_0$: it goes from $x_0$ to $f(a_{i-1})$ via $\alpha_{i-1}$, then from $f(a_{i-1})$ to $f(a_i)$ via $f_i$, then back from $f(a_i)$ to $x_0$ via $\bar{\alpha}_i$.
>
> Since $\alpha_i$ lies in $U \cap V$ (which is contained in both $U$ and $V$) and $f_i$ lies in $U$ or $V$, the entire loop $g_i$ lies in $U$ or $V$.
>
> **Step 4: The products match.**
>
> We compute:
>
> $$
> \begin{aligned}
> [g_1] * [g_2] * \cdots * [g_n] &= [\alpha_0 * f_1 * \bar{\alpha}_1] * [\alpha_1 * f_2 * \bar{\alpha}_2] * \cdots * [\alpha_{n-1} * f_n * \bar{\alpha}_n] \\
> &= [\alpha_0] * [f_1] * \underbrace{[\bar{\alpha}_1] * [\alpha_1]}_{= [e]} * [f_2] * \underbrace{[\bar{\alpha}_2] * [\alpha_2]}_{= [e]} * \cdots * [f_n] * [\bar{\alpha}_n] \\
> &= [e_{x_0}] * [f_1] * [f_2] * \cdots * [f_n] * [e_{x_0}] \\
> &= [f_1] * [f_2] * \cdots * [f_n] = [f].
> \end{aligned}
> $$

^pf-37-1

*Uses:* [[Lebesgue Number Lemma|§19.2]], [[§18 Compact Spaces#^thm-18-10|§18.10]], [[Properties of Path Concatenation|§28.6]]

![[m590-27-1.svg]]
*The proof in one picture ($n = 3$). The loop $f$ is cut at $f(a_1), f(a_2) \in U \cap V$ into pieces lying in $U$ (blue: $f_1, f_3$) or in $V$ (green: $f_2$); $U$ and $V$ are open, so their boundaries are dashed. The red paths $\alpha_i$ run inside the path-connected overlap from $x_0$ to the cut points, turning the pieces into loops at $x_0$: $g_1 = f_1 \ast  \bar\alpha_1$ in $U$, $g_2 = \alpha_1 \ast  f_2 \ast  \bar\alpha_2$ in $V$, $g_3 = \alpha_2 \ast  f_3$ in $U$. Each $\alpha_i$ is traversed once each way, so the product $g_1 \ast  g_2 \ast  g_3$ is $f$ again.*

> [!remark]- Connections
> - Upgraded from “generate” to the exact group by the [[Seifert–van Kampen Theorem|Seifert-van Kampen theorem]], whose surjectivity step is this theorem.

> [!remark] Remark: Why This Matters
> This is the stepping stone to both the [[§37 The Fundamental Group of Sⁿ#^cor-37-2|simply connected corollary]] and the [[Seifert–van Kampen Theorem|Seifert-van Kampen theorem]]. It says: if you can cover $X$ by two open sets, then every loop in $X$ can be decomposed into pieces from $U$ and $V$. The simply connected corollary uses this when both pieces contribute nothing ($\pi_1(U) = \pi_1(V) = 0$). Van Kampen uses it in general: the pieces generate $\pi_1(X)$, and the overlap $U \cap V$ determines the relations between them.

^rem-37-1

## Consequence: Simply Connected Spaces

> [!theorem] Corollary §37.2: Simply Connected from Open Cover
> Let $X = U \cup V$, where $U$ and $V$ are open and [[§29 The Fundamental Group#^def-29-3|simply connected]], and $U \cap V$ is [[§16 Connected Subspaces of ℝ#^def-16-4|path-connected]]. Then $X$ is simply connected.

^cor-37-2

> [!proof]+ Proof
> By [[§37 The Fundamental Group of Sⁿ#^thm-37-1|the theorem]], every element of $\pi_1(X, x_0)$ is a product of elements from $i_{U*}(\pi_1(U, x_0))$ and $i_{V*}(\pi_1(V, x_0))$. Since $U$ and $V$ are simply connected, $\pi_1(U, x_0) = 0$ and $\pi_1(V, x_0) = 0$. Both images are trivial. A product of trivial elements is trivial. So $\pi_1(X, x_0) = 0$.
>
> For simple connectivity, we also need $X$ to be path-connected. Since $U$ and $V$ are simply connected (hence path-connected) and $U \cap V \neq \emptyset$, the union $X = U \cup V$ is path-connected.

^pf-37-2

*Uses:* [[§37 The Fundamental Group of Sⁿ#^thm-37-1|§37.1]]

## $\pi_1(S^n) = 0$ for $n \geq 2$

> [!theorem] Theorem §37.3: $S^n$ is Simply Connected for $n \geq 2$
> The $n$-sphere $S^n$ is simply connected for $n \geq 2$.

^thm-37-3

> [!proof]+ Proof
> Write $S^n = U \cup V$ where $U = S^n \setminus \{p\}$ and $V = S^n \setminus \{q\}$, with:
>
> $$
> p = (0, 0, \ldots, 0, 1) \in S^n \quad \text{(north pole)}, \qquad q = (0, 0, \ldots, 0, -1) \in S^n \quad \text{(south pole)}.
> $$
>
> We verify the three hypotheses of [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]].
>
> **1. $U$ and $V$ are open.** Each is the complement of a single ([[§9 Hausdorff Spaces#^thm-9-1|closed]]) point in $S^n$.
>
> **2. $U$ and $V$ are simply connected.** We show $U = S^n \setminus \{p\} \cong \mathbb{R}^n$ via **stereographic projection**.
>
> Define $f: S^n \setminus \{p\} \to \mathbb{R}^n$ by projecting from the north pole:
>
> $$
> f(x_1, \ldots, x_n, x_{n+1}) = \frac{1}{1 - x_{n+1}}(x_1, \ldots, x_n).
> $$
>
> This is well-defined since $x_{n+1} \neq 1$ on $S^n \setminus \{p\}$. The inverse is $g: \mathbb{R}^n \to S^n \setminus \{p\}$:
>
> $$
> g(y_1, \ldots, y_n) = \left(t(y)\,y_1, \;\ldots,\; t(y)\,y_n, \;1 - t(y)\right), \qquad \text{where } t(y) = \frac{2}{1 + \|y\|^2}.
> $$
>
> One can verify $f(g(y)) = y$ and $g(f(x)) = x$ by direct computation (the key identity is $\|x\|^2 = x_1^2 + \cdots + x_{n+1}^2 = 1$ on $S^n$). Both $f$ and $g$ are continuous (rational functions with nonzero denominators), so $f$ is a [[§10 Continuous Functions#^def-10-2|homeomorphism]].
>
> Since $\mathbb{R}^n$ is convex $\Rightarrow$ [[§35 Deformation Retracts and Homotopy Type#^def-35-4|contractible]] $\Rightarrow$ [[§29 The Fundamental Group#^ex-29-1|simply connected]], we get $\pi_1(U) = 0$.
>
> For $V = S^n \setminus \{q\}$: the reflection $r: S^n \to S^n$ defined by $r(x_1, \ldots, x_n, x_{n+1}) = (x_1, \ldots, x_n, -x_{n+1})$ is a homeomorphism (it is its own inverse) that swaps $p \leftrightarrow q$. So $r$ [[§10 Continuous Functions#^prop-10-3|restricts]] to a homeomorphism $S^n \setminus \{q\} \to S^n \setminus \{p\}$. Therefore $V \cong U \cong \mathbb{R}^n$, and $\pi_1(V) = 0$.
>
> **3. $U \cap V$ is path-connected (for $n \geq 2$).** We have $U \cap V = S^n \setminus \{p, q\}$. The stereographic projection $f: S^n \setminus \{p\} \to \mathbb{R}^n$ maps $q = (0, \ldots, 0, -1)$ to:
>
> $$
> f(0, \ldots, 0, -1) = \frac{1}{1 - (-1)}(0, \ldots, 0) = \vec{0}.
> $$
>
> Since $f$ is a homeomorphism $S^n \setminus \{p\} \to \mathbb{R}^n$ that sends $q \mapsto \vec{0}$, restricting gives a homeomorphism:
>
> $$
> U \cap V = S^n \setminus \{p, q\} \;\cong\; \mathbb{R}^n \setminus \{\vec{0}\}.
> $$
>
> For $n \geq 2$, $\mathbb{R}^n \setminus \{\vec{0}\}$ is [[§16 Connected Subspaces of ℝ#^def-16-4|path-connected]]: given any two points $a, b \neq \vec{0}$, if the straight line from $a$ to $b$ avoids the origin, use it; otherwise, detour slightly (possible in dimension $\geq 2$). Therefore $U \cap V$ is path-connected.
>
> By [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]], $S^n$ is simply connected.

^pf-37-3

*Uses:* [[§37 The Fundamental Group of Sⁿ#^cor-37-2|§37.2]], [[§9 Hausdorff Spaces#^thm-9-1|§9.1]], [[§29 The Fundamental Group#^ex-29-1|Ex. §29.1]], [[§10 Continuous Functions#^prop-10-3|§10.3]], [[§29 The Fundamental Group#^cor-29-6|§29.6]], [[§10 Continuous Functions#^def-10-2|Def. §10.2]], [[§35 Deformation Retracts and Homotopy Type#^def-35-4|Def. §35.4]], [[§16 Connected Subspaces of ℝ#^def-16-4|Def. §16.4]]

![[m590-27-2.svg]]
*Stereographic projection from the north pole $p$ (a cross-section through the $x_{n+1}$-axis): $f(x)$ is where the line from $p$ through $x$ meets the equatorial plane $\mathbb{R}^n = \{x_{n+1} = 0\}$. The lower hemisphere lands inside the unit ball, the upper hemisphere outside it, and points near $p$ run off to infinity, which is why $p$ must be removed. The south pole $q$ goes to $\vec 0$, so removing $q$ as well leaves $\mathbb{R}^n \setminus \{\vec 0\}$.*

> [!remark]- Connections
> - Stereographic projection first appeared for $S^1$ and $S^2$ in [[§20 Local Compactness#^ex-20-7|One-Point Compactification of ℝ and ℝ²]].
> - Recomputed with van Kampen in [[§39 The Seifert–van Kampen Theorem#^ex-39-1|Simply Connected Spheres via van Kampen]].
> - Used in Quantum Field Theory: $S^3 \cong SU(2)$ is simply connected, hence so is $SL(2, \mathbb C) \cong \mathbb R^3\times S^3$ — [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-9|QFT Theorem §CB.10.9]].

> [!remark] Remark
> $S^n$ ($n \geq 2$) and a one-point space have the same $\pi_1$ — both trivial. But they are not [[§35 Deformation Retracts and Homotopy Type#^def-35-2|homotopy equivalent]] ($S^n$ is not [[§35 Deformation Retracts and Homotopy Type#^def-35-4|contractible]], which can be detected by higher homotopy groups or homology).

^rem-37-2

> [!remark] Remark: Why $n \geq 2$ is Essential
> For $n = 1$: $U \cap V = S^1 \setminus \{p, q\} \cong \mathbb{R}^1 \setminus \{0\} = (-\infty, 0) \cup (0, \infty)$ — two disjoint intervals, **not** path-connected. So [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]] does not apply, and indeed $\pi_1(S^1) \cong \mathbb{Z} \neq 0$ ([[Fundamental Group of the Circle|§32.5]]).
>
> This also explains why the no-retraction theorem for $B^{n+1} \to S^n$ ([[§34 Retractions and Fixed Points#^thm-34-9|§34.9]]) cannot be proved using $\pi_1$ when $n \geq 2$: $\pi_1(S^n) = 0$ gives no contradiction, and one needs homology instead.

^rem-37-3

![[m590-27-3.svg]]
*$U \cap V$ is a sphere with both poles removed. For $n = 2$ (left) any two points $a, b$ can be joined while avoiding $p$ and $q$ (red path). For $n = 1$ (right) the two removed points cut the circle into two arcs, homeomorphic to $(-\infty, 0)$ and $(0, \infty)$, and no path joins $a$ to $b$. That missing hypothesis is exactly what lets $\pi_1(S^1) \cong \mathbb{Z}$ be nontrivial.*

> [!remark]- Connections
> - The same observation from the retraction side: [[§34 Retractions and Fixed Points#^rem-34-4|Why Our Proof Does Not Generalize]].

> [!example] Example §37.1: Wedge of Two Spheres is Simply Connected
> The space $X = S^2 \vee S^2$ (two copies of $S^2$ glued at a single point) has $\pi_1(X) = 0$.
>
> **Topology of $X$.** The space $X$ inherits the [[§13 Quotient Topology#^def-13-2|quotient topology]] from $S_1 \sqcup S_2$ (the two copies of $S^2$) under the identification $p_1 \sim p_2$ of a point $p_1 \in S_1$ with a point $p_2 \in S_2$; write $p \in X$ for the resulting junction point. Thus a set $W \subseteq X$ is open if and only if $W \cap S_1$ is open in $S_1$ and $W \cap S_2$ is open in $S_2$. The natural inclusions $S_1 \hookrightarrow X$ and $S_2 \hookrightarrow X$ are embeddings, and $X$ is [[§9 Hausdorff Spaces#^def-9-1|Hausdorff]] (since $S_1$ and $S_2$ are compact Hausdorff and meet at a single point).
>
> **Setup: remove one point from each side.** Let $q_1 = -p_1 \in S_1$ and $q_2 = -p_2 \in S_2$ be the antipodes of the junction point (so $q_1, q_2 \neq p$). Define:
>
> $$
> U = X \setminus \{q_2\} = S_1 \cup (S_2 \setminus \{q_2\}), \qquad V = X \setminus \{q_1\} = (S_1 \setminus \{q_1\}) \cup S_2.
> $$
>
> Then $X = U \cup V$. We verify the three hypotheses of [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]].
>
> **1. $U$ and $V$ are open.** Since $X$ is Hausdorff, $\{q_2\}$ is closed ([[§9 Hausdorff Spaces#^thm-9-1|§9.1]]), so $U = X \setminus \{q_2\}$ is open. Similarly $V$ is open.
>
> **2. $U$ and $V$ are simply connected.** We show $U$ [[§35 Deformation Retracts and Homotopy Type#^def-35-1|deformation retracts]] onto $S_1 \cong S^2$.
>
> By [[§37 The Fundamental Group of Sⁿ#^pf-37-3|stereographic projection]] from $q_2$, the punctured sphere $S_2 \setminus \{q_2\} \cong \mathbb{R}^2$, which is contractible. Let $r_t: S_2 \setminus \{q_2\} \to S_2 \setminus \{q_2\}$ be a deformation retraction onto $\{p\}$: explicitly, in the $\mathbb{R}^2$ coordinates, this is the [[§28 Homotopy of Paths#^thm-28-1|straight-line homotopy]] $r_t(x) = (1-t)x + t \cdot 0$ toward the origin (which corresponds to $p$ under stereographic projection from $q_2$, since $p = -q_2$ in $S_2$). Note $r_0 = \operatorname{id}$, $r_1(x) = p$ for all $x$, and $r_t(p) = p$ for all $t$.
>
> Define $F: U \times I \to U$ by:
>
> $$
> F(x, t) = \begin{cases} x & \text{if } x \in S_1, \\ r_t(x) & \text{if } x \in S_2 \setminus \{q_2\}. \end{cases}
> $$
>
> These agree at the overlap point $p$ (since $r_t(p) = p$). The sets $S_1$ and $S_2 \setminus \{q_2\}$ are both closed in $U$ (since $S_1$ is compact in Hausdorff $U$ ([[Compact Subspace of a Hausdorff Space is Closed|§18.4]]), and $S_2 \setminus \{q_2\} = S_2 \cap U$ is closed in $U$ ([[§7 Closed Sets and Limit Points#^thm-7-2|§7.2]]) because $S_2$ is closed in $X$, being compact in Hausdorff $X$), so $F$ is continuous by the **[[Pasting Lemma|pasting lemma]]** (for closed sets).
>
> Check: $F(x, 0) = x$ (identity), $F(x, 1) \in S_1$ for all $x$ (collapses $S_2 \setminus \{q_2\}$ to $p \in S_1$), and $F(x, t) = x$ for all $x \in S_1$ (fixed). So $F$ is a deformation retraction of $U$ onto $S_1 \cong S^2$. Since $\pi_1(S^2) = 0$ ([[Sⁿ is Simply Connected for n ≥ 2|§37.3]]), $U$ is simply connected.
>
> By the same argument (swapping $S_1 \leftrightarrow S_2$ and $q_1 \leftrightarrow q_2$), $V$ deformation retracts onto $S_2 \cong S^2$, hence $V$ is simply connected.
>
> **3. $U \cap V$ is path-connected.** We have:
>
> $$
> U \cap V = X \setminus \{q_1, q_2\} = (S_1 \setminus \{q_1\}) \cup (S_2 \setminus \{q_2\}).
> $$
>
> By stereographic projection, $S_1 \setminus \{q_1\} \cong \mathbb{R}^2$ and $S_2 \setminus \{q_2\} \cong \mathbb{R}^2$, both path-connected. Since they share the point $p$, their union is path-connected.
>
> By [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]], $\pi_1(X) = 0$.

^ex-37-1

![[m590-27-4.svg]]
*The deformation retraction of $U = X \setminus \{q_2\}$ onto $S_1$: with $q_2$ removed, $S_2 \setminus \{q_2\} \cong \mathbb{R}^2$, and the straight-line contraction to the origin becomes a flow along great circles from $q_2$ toward the wedge point $p$, its antipode in $S_2$ (red). $S_1$ (blue) never moves, so $\pi_1(U) \cong \pi_1(S^2) = 0$. $V = X \setminus \{q_1\}$ is the mirror image.*

> [!remark]- Connections
> - $S^2 \vee S^2$ is a [[§38 Fundamental Group of Some Surfaces#^def-38-3|wedge sum]]; see also [[§38 Fundamental Group of Some Surfaces#^ex-38-1|Wedge Sums]].

> [!remark] Remark: The “Remove One Point From Each Side” Strategy
> The proofs of $\pi_1(S^n) = 0$ ([[Sⁿ is Simply Connected for n ≥ 2|§37.3]]) and $\pi_1(S^2 \vee S^2) = 0$ ([[§37 The Fundamental Group of Sⁿ#^ex-37-1|Ex. §37.1]]) follow the same template. The key technique is: **to apply [[§37 The Fundamental Group of Sⁿ#^cor-37-2|the corollary]], choose $U$ and $V$ by removing one “bad” point from each piece of $X$**. Here is the general recipe.
>
> **Step 1: Identify the pieces.** The space $X$ is built from components (two hemispheres, two spheres glued at a point, etc.). Each component $C_i$ has the property that removing a point makes it simpler ($C_i \setminus \{q\} \cong \mathbb{R}^n$, or contractible, or deformation retracts onto something known).
>
> **Step 2: Remove one point from the “other side.”** Define $U$ by removing a point from $C_2$ (so $U$ contains all of $C_1$ and most of $C_2$), and $V$ by removing a point from $C_1$. This ensures $X = U \cup V$.
>
> **Step 3: Compute.**
> - **Open:** Each $U_i$ is the complement of a single point in a Hausdorff space.
> - **$\pi_1(U)$ and $\pi_1(V)$:** The removed point makes the “other side” contractible, so it collapses via [[§35 Deformation Retracts and Homotopy Type#^def-35-1|deformation retract]]. What remains determines $\pi_1$.
> - **$U \cap V$ path-connected:** Both bad points are removed, but each piece minus its bad point is path-connected, and the pieces share a common point.
>
> **The result need not be trivial.** The corollary (both $U, V$ simply connected $\Rightarrow$ $\pi_1(X) = 0$) is a special case. The [[§37 The Fundamental Group of Sⁿ#^thm-37-1|generation theorem]] itself gives $\pi_1(X)$ generated by $\pi_1(U)$ and $\pi_1(V)$, which may be nontrivial. The “remove one point” strategy works whenever it produces $U$ and $V$ whose $\pi_1$ you can compute — the generation theorem (or [[Seifert–van Kampen Theorem|van Kampen]]) then assembles the answer.
>
> | **Space $X$** | **$U$** (remove pt from right) | **$V$** (remove pt from left) | $\pi_1(X)$ |
> |---|---|---|---|
> | $S^n$ ($n \geq 2$) ([[Sⁿ is Simply Connected for n ≥ 2\|§37.3]]) | $S^n \setminus \{p\} \cong \mathbb{R}^n$ | $S^n \setminus \{q\} \cong \mathbb{R}^n$ | $0$ |
> | $S^2 \vee S^2$ ([[§37 The Fundamental Group of Sⁿ#^ex-37-1\|Ex. §37.1]]) | def. retract onto $S^2$ | def. retract onto $S^2$ | $0$ |
> | $S^1 \vee S^1$ ([[§39 The Seifert–van Kampen Theorem#^ex-39-2\|Ex. §39.2]]) | def. retract onto $S^1$ | def. retract onto $S^1$ | $F_2$ |
>
> The last row requires [[§39 The Seifert–van Kampen Theorem#^ex-39-2|van Kampen]] to determine that $\pi_1 \cong \mathbb{Z} * \mathbb{Z} = F_2$ (not just generated by two copies of $\mathbb{Z}$).

^rem-37-4
