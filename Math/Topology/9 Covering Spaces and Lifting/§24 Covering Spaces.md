---
type: section
subject: "[[Topology]]"
chapter: 9
section: 24
munkres: "§53"
tags: [topology, math590]
---
← [[§23a The Punctured Plane and the Torus]] · ↑ [[· 9 Covering Spaces and Lifting]] · [[§24a Lifting and the Fundamental Group of the Circle]] →

## Evenly Covered Sets and Covering Maps

> [!definition] Definition §24.1: Evenly Covered
> Let $p: E \to B$ be a continuous surjective map. An open set $U \subseteq B$ is **evenly covered** by $p$ if
>
> $$p^{-1}(U) = \bigsqcup_\alpha V_\alpha$$
>
> where the $V_\alpha$ are disjoint open sets in $E$ (called **slices**), and $p|_{V_\alpha}: V_\alpha \to U$ is a [[§9 Continuous Functions#^def-9-2|homeomorphism]] for each $\alpha$.

^def-24-1

> [!definition] Definition §24.2: Covering Map
> A continuous surjective map $p: E \to B$ is a **covering map** if every point $b \in B$ has a neighborhood $U$ that is evenly covered by $p$.

^def-24-2

> [!remark]- Connections
> - In 591 the smooth analogue with a discrete fibre is a fibration, [[§34 Fibrations#^def-34-1|591 Def. §34.1]], and smooth covering maps such as ℝ → S¹ are local diffeomorphisms, [[§31 Local Diffeomorphisms#^rem-31-2|591 §31, Remark: Covering Maps]].
> - Concrete example: [[§110★ Riemann Surfaces#^ex-110-1|342 Ex. §110.1]] (the Riemann surface of log z, an infinitely-sheeted covering of the punctured plane).

> [!definition] Definition §24.3: Covering Space
> If $p: E \to B$ is a covering map, the space $E$ is called a **covering space** of $B$. The space $B$ is called the **base space**. The triple $(E, p, B)$ is called a **covering**.
>
> Informally, $E$ “unwinds” $B$: above every small neighborhood $U$ in $B$, the preimage $p^{-1}(U)$ consists of *disjoint copies* of $U$ stacked above each other, each mapped homeomorphically onto $U$ by $p$. Globally, $E$ may be simpler than $B$ (e.g., $\mathbb{R}$ is [[§23 The Fundamental Group#^ex-23-1|simply connected]] while $S^1$ is not). The covering map $p$ “wraps” $E$ around $B$, and the structure of this wrapping encodes $\pi_1(B)$.

^def-24-3

> [!definition] Definition §24.4: Fiber
> Let $p: E \to B$ be a map. The **fiber** over a point $b \in B$ is the preimage $p^{-1}(b) = \{e \in E \mid p(e) = b\}$—the set of all points in $E$ that map to $b$.

^def-24-4

> [!definition] Definition §24.5: Number of Sheets
> A covering map $p: E \to B$ is **$n$-sheeted** (or has **$n$ sheets**) if every fiber has exactly $n$ elements: $|p^{-1}(b)| = n$ for all $b \in B$. We say $E$ is an **$n$-fold cover** of $B$.
>
> If $n = \infty$ (every fiber is countably infinite), we say $p$ is an **infinite-sheeted** covering.

^def-24-5

> [!remark] Remark: Why Copies Compute $\pi_1$
> **Why multiple copies compute $\pi_1$.** In $B$, every loop based at $b_0$ starts and ends at the same point — you cannot “see” the difference between winding once, winding twice, or sitting still just by looking at the endpoints. The copies of $b_0$ in the covering space $E$ are what separate these loops.
>
> A loop in $B$ lifts to a path in $E$ that starts at $e_0$ but may end at a *different* copy of $b_0$ in the fiber $p^{-1}(b_0)$. Which copy it lands on depends only on the homotopy class of the loop (by the [[Homotopy Lifting Lemma|homotopy lifting lemma]]). When $E$ is simply connected, different homotopy classes land on different copies. So the copies serve as a **scoreboard**: each point in the fiber $p^{-1}(b_0)$ records a distinct way of looping around $B$.
>
> **Why this works:**
> - If $p$ were a homeomorphism (one copy), every lift of a loop would be a loop — you would learn nothing. $E$ and $B$ would have the same topology.
> - Multiple copies give the lift room to *not come back*. A loop in $B$ “wraps around” and returns to $b_0$, hiding the winding. In $E$, the path can end at a different copy, revealing the winding.
> - Disjoint copies make the recording unambiguous — the lift can't wander between copies, so the endpoint is well-defined.
>
> **The counting formula.** When $E$ is simply connected, the [[§24a Lifting and the Fundamental Group of the Circle#^def-24-7|lifting correspondence]] ([[Properties of the Lifting Correspondence|§24]]) gives a bijection $\pi_1(B, b_0) \leftrightarrow p^{-1}(b_0)$. So:
>
> $$\text{number of sheets} = |p^{-1}(b_0)| = |\pi_1(B, b_0)|.$$
>
> Count the fiber, get the size of $\pi_1$. Examples:
> - $p: \mathbb{R} \to S^1$: $\infty$ sheets ($p^{-1}(b_0) = \mathbb{Z}$), so $|\pi_1(S^1)| = \infty$ (and $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]])).
> - $p: S^2 \to P^2$: $2$ sheets ($p^{-1}(y) = \{x, -x\}$), so $|\pi_1(P^2)| = 2$ (and $\pi_1(P^2) \cong \mathbb{Z}/2\mathbb{Z}$ ([[§28 Fundamental Group of Some Surfaces#^thm-28-2|§28.2]])).
> - $p: S^n \to P^n$ ($n \geq 2$): $2$ sheets, so $\pi_1(P^n) \cong \mathbb{Z}/2\mathbb{Z}$ ([[§28 Fundamental Group of Some Surfaces#^thm-28-3|§28.3]]).
>
> This only works when $E$ is simply connected. If $E$ is not simply connected, the lifting correspondence is not a bijection, and counting sheets does not directly give $|\pi_1(B)|$.

^rem-24-1

> [!example] Example §24.1: Basic Examples
> - The identity map $\operatorname{id}_X: X \to X$ is a covering map (each $U$ has one slice: itself).
> - The projection $p: X \times \{1, \ldots, n\} \to X$, $(x, i) \mapsto x$, is a covering map (each open $U$ has $n$ slices $U \times \{1\}, \ldots, U \times \{n\}$).

^ex-24-1

> [!theorem] Proposition §24.1: Properties of Covering Maps
> Let $p: E \to B$ be a covering map. Then:
> 1. $p$ is an [[§12 Quotient Topology#^def-12-4|open map]].
> 2. $p$ is a local [[§9 Continuous Functions#^def-9-2|homeomorphism]]: each $e \in E$ has a neighborhood mapped homeomorphically by $p$ onto an open subset of $B$.
> 3. For each $b \in B$, the fiber $p^{-1}(b)$ has the [[§1 Topological Spaces#^ex-1-3|discrete topology]].
>
> The converse of (2) is not true: a surjective local homeomorphism need not be a covering map (see the [[§24 Covering Spaces#^ex-24-2|non-example below]]).

^prop-24-1

> [!proof]+ Proof
> **(1)** Let $A$ be open in $E$. We show $p(A)$ is open in $B$. Given $x \in p(A)$, choose an evenly covered neighborhood $U$ of $x$, with $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$. There exists $y \in A$ with $p(y) = x$; let $V_\beta$ be the slice containing $y$. The set $V_\beta \cap A$ is open in $E$, hence open in $V_\beta$. Since $p|_{V_\beta}: V_\beta \to U$ is a homeomorphism, $p(V_\beta \cap A)$ is open in $U$, hence open in $B$. So $p(V_\beta \cap A)$ is a neighborhood of $x$ contained in $p(A)$.
>
> **(2)** Given $e \in E$, let $U$ be an evenly covered neighborhood of $p(e)$, and let $V$ be the slice containing $e$. Then $p|_V: V \to U$ is a homeomorphism.
>
> **(3)** Each slice $V_\alpha$ is open in $E$ and contains exactly one point of $p^{-1}(b)$. So each singleton in $p^{-1}(b)$ is open in the subspace topology.

^pf-24-1

*Uses:* [[§24 Covering Spaces#^def-24-1|Def. §24.1]], [[§5 Subspace Topology#^lem-5-2|§5.2]]

## The Covering Map $p: \mathbb{R} \to S^1$

> [!theorem] Theorem §24.2: $p: \mathbb{R} \to S^1$ is a Covering Map
> The map $p: \mathbb{R} \to S^1$ defined by $p(x) = (\cos 2\pi x, \sin 2\pi x)$ is a covering map.

^thm-24-2

> [!proof]+ Proof
> We show each point of $S^1$ has an evenly covered neighborhood.
>
> Let $U \subseteq S^1$ consist of points $(x_1, x_2) \in S^1 \subseteq \mathbb{R}^2$ with $x_1 > 0$ (the right half-circle). Then:
>
> $$p^{-1}(U) = \{x \in \mathbb{R} \mid \cos(2\pi x) > 0\} = \bigsqcup_{n \in \mathbb{Z}} V_n, \quad \text{where } V_n = \left(n - \tfrac{1}{4}, n + \tfrac{1}{4}\right).$$
>
> We verify $p|_{V_n}: V_n \to U$ is a homeomorphism:
> - **Injective:** $\sin(2\pi x)$ is strictly monotone on $V_n$, so $p|_{V_n}$ is injective.
> - **Surjective:** $p|_{\overline{V}_n}: \overline{V}_n \to \overline{U}$ is surjective by [[§14 Connected Subspaces of ℝ#^thm-14-3|IVT]] (continuous image of a compact interval covers a connected arc). Since $p|_{\overline{V}_n}$ is a [[Bijection from Compact to Hausdorff is a Homeomorphism|continuous bijection from compact to Hausdorff]], it is a homeomorphism. The restriction $p|_{V_n}$ is then also a homeomorphism.
>
> Similar arguments apply for the left half-circle ($x_1 < 0$), top half-circle ($x_2 > 0$), and bottom half-circle ($x_2 < 0$). Each half-circle is evenly covered by $p$, and every point of $S^1$ lies in at least one of these four open sets.

^pf-24-2

*Uses:* [[§14 Connected Subspaces of ℝ#^thm-14-3|§14.3]], [[§15 Compact Spaces#^thm-15-10|§15.10]], [[Bijection from Compact to Hausdorff is a Homeomorphism|§15.7]], [[§9 Continuous Functions#^prop-9-3|§9.3]]

![[m590-24-2.svg]]
*The covering $p: \mathbb{R} \to S^1$ drawn as a helix over the circle: each $x \in \mathbb{R}$ sits directly above $p(x)$, one full turn per unit length. The right half-circle $U$ (red, open, hollow endpoints) is evenly covered. Its preimage is the stack of disjoint red slices $V_n = (n - \tfrac14, n + \tfrac14)$, each carried homeomorphically onto $U$ by $p$. The fiber over $b_0 = (1,0)$ is $\mathbb{Z}$ (black dots), one point in each slice.*

> [!remark]- Connections
> - Complex form: z ↦ eᶻ covers ℂ ∖ {0}, and the branches of log z are its [[§114★ Local Inverses#^def-114-1|local inverses]] on slit planes, [[§33 Branches and Derivatives of Logarithms#^thm-33-1|342 Thm. §33.1]]; the whole covering is the Riemann surface of log z, [[§110★ Riemann Surfaces#^ex-110-1|342 Ex. §110.1]].

> [!remark] Remark
> This covering map is the key to computing $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]). The idea: $\mathbb{R}$ is simply connected, and the covering map $p: \mathbb{R} \to S^1$ “unwinds” loops on $S^1$ into paths in $\mathbb{R}$. A loop that winds $n$ times around $S^1$ lifts to a path in $\mathbb{R}$ from $0$ to $n$. The integer $n$ is the winding number, and this gives the isomorphism $\pi_1(S^1) \cong \mathbb{Z}$.
>
> A simply connected covering space is called a **universal cover**. So $\mathbb{R}$ is the universal cover of $S^1$. The [[§24a Lifting and the Fundamental Group of the Circle#^def-24-7|lifting correspondence]] is a bijection precisely when the covering space is universal—this is why the universal cover is the most useful one for computing $\pi_1$.

^rem-24-2

> [!remark] Remark: The Three Players in $p: \mathbb{R} \to S^1$
> Each of $\mathbb{R}$, $S^1$, and $\mathbb{Z}$ plays a distinct role in the lifting correspondence. The general [[§24a Lifting and the Fundamental Group of the Circle#^def-24-6|lift]] diagram $\tilde{f}: X \to E$, $f: X \to B$, $p: E \to B$ becomes:
>
> $$\begin{array}{ccc}
> & & \mathbb{R} \; (E) \\
> & {}^{\tilde{f}}\nearrow & \downarrow \, p \\
> I \; (X) & \xrightarrow{\quad f \quad} & S^1 \; (B)
> \end{array}$$
>
> Here $X = I = [0,1]$ is the parameter space (the domain of the loop), $B = S^1$ is the base space, and $E = \mathbb{R}$ is the covering space. The map $f: I \to S^1$ is a loop on the circle; the lift $\tilde{f}: I \to \mathbb{R}$ is a path in $\mathbb{R}$ with $p \circ \tilde{f} = f$.
>
> 1. **$S^1 = B$ (base space):** the space whose $\pi_1$ we want to compute. Loops live here, but all loops start and end at the same point $(1,0)$ — you cannot see the difference between winding once and winding twice just by looking at endpoints.
> 2. **$\mathbb{R} = E$ (covering space):** the “unwound” version of $S^1$. Simply connected, so all loops in $\mathbb{R}$ contract — the topology is trivial. Its job is to separate loops that $S^1$ cannot distinguish: a loop in $S^1$ lifts to a *path* in $\mathbb{R}$ that may end at a different point from where it started.
> 3. **$\mathbb{Z} = p^{-1}(1,0)$ (fiber):** the scoreboard. Each integer $n \in \mathbb{Z}$ sits above the basepoint $(1,0) \in S^1$. A loop that winds $n$ times lifts to a path from $0$ to $n$. The endpoint records the winding number. The lifting correspondence is the bijection $\pi_1(S^1, (1,0)) \to \mathbb{Z}$, $[f] \mapsto \tilde{f}(1)$.
>
> The conclusion $\pi_1(S^1) \cong \mathbb{Z}$ says: the group of loops on the circle, up to homotopy, *is* the integers under addition. The covering map $p$ is the tool that reveals this.

^rem-24-3

> [!remark]- Connections
> - As a smooth map, $t \mapsto (\cos t, \sin t)$ is a local diffeomorphism, and its restriction to $(0, 4\pi)$ is a local diffeomorphism that is not a covering map: [[§31 Local Diffeomorphisms#^ex-31-1|591 Ex. §31.1]].

## Non-Example: Local Homeomorphism $\neq$ Covering Map

> [!example] Example §24.2: $p: \mathbb{R}_+ \to S^1$ is Not a Covering Map
> The restriction $p: \mathbb{R}_+ \to S^1$ to $\mathbb{R}_+ = (0, \infty)$, $p(x) = (\cos 2\pi x, \sin 2\pi x)$, is still surjective and a local homeomorphism, but **not** a covering map.
>
> The neighborhood $U$ of $(1, 0) \in S^1$ (e.g., the right half-circle) has preimage $p^{-1}(U) = V_0 \cup \bigcup_{n \geq 1} V_n$ where $V_0 = (-1/4, 1/4) \cap \mathbb{R}_+ = (0, 1/4)$. But $p|_{V_0}: V_0 \to U$ is **not surjective** (it only covers the top-right quarter), so $V_0$ is not a valid slice. The preimage $p^{-1}(U)$ does not decompose into disjoint copies of $U$.
>
> **Consequence: lifting fails.** Consider a loop $f$ in $S^1$ that winds once clockwise from $(1,0)$. If we try to lift starting at $e_0 = 1$, we would need $\tilde{f}(s) = 1 - s$ — but $\tilde{f}(1) = 0 \notin \mathbb{R}_+$. The lift “wants to go left” to $0$, but $\mathbb{R}_+$ stops just short of it. The disjoint-copies condition fails precisely at $V_0$, and this is where the lift breaks down.

^ex-24-2

![[m590-24-3.svg]]
*Why $p: \mathbb{R}_+ \to S^1$ is not a covering map. Over the same $U$ (red), the slices $V_1, V_2, \ldots$ are still full copies of $U$. But the bottom piece $V_0 = (0, \tfrac14)$ (orange) is cut off at $0$, because the dashed part $(-\tfrac14, 0]$ (with the hollow point $0$) is missing from $\mathbb{R}_+$. So $p(V_0)$ is only the orange quarter of $U$ just after $b_0$. A clockwise loop from $b_0$, lifted from $1$, would have to end at the missing point $0$.*

## Restriction to Subspaces

> [!theorem] Theorem §24.3: Covering Maps Restrict to Subspaces
> Let $p: E \to B$ be a covering map. If $B_0 \subseteq B$ is a subspace and $E_0 = p^{-1}(B_0)$, then the restricted map $p_0: E_0 \to B_0$ is a covering map.

^thm-24-3

> [!proof]+ Proof
> Let $b_0 \in B_0$. Choose an open set $U$ in $B$ containing $b_0$ that is evenly covered by $p$, so $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$ with $p|_{V_\alpha}: V_\alpha \to U$ a homeomorphism.
>
> Then $U \cap B_0$ is a neighborhood of $b_0$ in $B_0$, and
>
> $$p_0^{-1}(U \cap B_0) = p^{-1}(U) \cap p^{-1}(B_0) = p^{-1}(U) \cap E_0 = \bigsqcup_\alpha (V_\alpha \cap E_0).$$
>
> The sets $V_\alpha \cap E_0$ are disjoint open sets in $E_0$.
>
> Each $p_0|_{V_\alpha \cap E_0}: V_\alpha \cap E_0 \to U \cap B_0$ is a homeomorphism:
> - **Injective:** $p|_{V_\alpha}$ is injective, so its restriction is injective.
> - **Surjective:** If $x \in U \cap B_0$, then since $p|_{V_\alpha}: V_\alpha \to U$ is surjective, there exists $e \in V_\alpha$ with $p(e) = x$. Since $x \in B_0$, we have $e \in p^{-1}(B_0) = E_0$, so $e \in V_\alpha \cap E_0$.
> - **Continuous:** Restriction of the continuous map $p|_{V_\alpha}$.
> - **Inverse continuous:** The inverse of $p|_{V_\alpha}$ maps $U \to V_\alpha$ continuously. Restricting to $U \cap B_0 \to V_\alpha \cap E_0$ preserves continuity (restriction to a subspace).
>
> So $U \cap B_0$ is evenly covered by $p_0$.

^pf-24-3

*Uses:* [[§24 Covering Spaces#^def-24-1|Def. §24.1]], [[§9 Continuous Functions#^thm-9-4|§9.4]]

## Product of Covering Maps

> [!theorem] Theorem §24.4: Product of Covering Maps
> If $p: E \to B$ and $p': E' \to B'$ are covering maps, then $p \times p': E \times E' \to B \times B'$ is a covering map.

^thm-24-4

> [!proof]+ Proof
> Let $(b, b') \in B \times B'$. Choose open sets $U \ni b$ and $U' \ni b'$ evenly covered by $p$ and $p'$ respectively: $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$ and $(p')^{-1}(U') = \bigsqcup_\beta V'_\beta$.
>
> Then $(p \times p')^{-1}(U \times U') = p^{-1}(U) \times (p')^{-1}(U') = \bigsqcup_{\alpha, \beta} (V_\alpha \times V'_\beta)$, which is a disjoint union of open sets in $E \times E'$. Each $V_\alpha \times V'_\beta$ is mapped homeomorphically onto $U \times U'$ by $p \times p'$ (since $p|_{V_\alpha}$ and $p'|_{V'_\beta}$ are homeomorphisms, their product is a homeomorphism).

^pf-24-4

*Uses:* [[§24 Covering Spaces#^def-24-1|Def. §24.1]], [[§4 Product Topology#^def-4-1|Def. §4.1]]

> [!example] Example §24.3
> $p \times p: \mathbb{R} \times \mathbb{R} \to S^1 \times S^1$ is a covering map. Since $S^1 \times S^1$ is the torus $T^2$, this gives a covering $\mathbb{R}^2 \to T^2$. This will be used to compute $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ ([[§23 The Fundamental Group#^cor-23-8|§23.8]]).

^ex-24-3

![[m590-24-4.svg]]
*The covering $p \times p: \mathbb{R}^2 \to T^2$ wraps each unit square of the plane once around the torus. The fiber over the basepoint $(b_0, b_0)$ is the lattice $\mathbb{Z} \times \mathbb{Z}$ (black dots). The edge from $(0,0)$ to $(1,0)$ (red) maps to the loop $S^1 \times \{b_0\}$ around the hole. The edge from $(0,0)$ to $(0,1)$ (blue) maps to the loop $\{b_0\} \times S^1$ around the tube. These two loops are the generators of $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$.*

*Chain: earlier in [[§23a The Punctured Plane and the Torus|Chapter 8]] · later in [[§26a The Punctured Plane, the Figure Eight and the Torus|Chapter 10]] · [[Torus|all appearances]]*

## Transport of Covering Maps

If you know a covering map of a space $B$, you automatically get a covering map of any space homeomorphic to $B$.

> [!theorem] Proposition §24.5: Transport of Covering Maps via Homeomorphism
> Let $p: E \to B$ be a covering map and $h: B' \to B$ a homeomorphism. Then
>
> $$p' = h^{-1} \circ p: E \to B'$$
>
> is a covering map.
>
> ![[m590-24-1.svg]]
> *The transported covering $p' = h^{-1} \circ p: E \to B'$ (red), where $h: B' \to B$ is a homeomorphism; the triangle commutes, $h \circ p' = p$.*

^prop-24-5

> [!proof]+ Proof
> We verify the three properties of a covering map for $p' = h^{-1} \circ p$.
>
> **Continuous:** $p$ is continuous and $h^{-1}$ is continuous (since $h$ is a homeomorphism), so $p' = h^{-1} \circ p$ is continuous as a composition.
>
> **Surjective:** Let $b' \in B'$. Since $h$ is a bijection, $b = h(b') \in B$. Since $p$ is surjective, there exists $e \in E$ with $p(e) = b$. Then $p'(e) = h^{-1}(p(e)) = h^{-1}(b) = b'$.
>
> **Evenly covered neighborhoods:** Let $b' \in B'$. We must find a neighborhood of $b'$ in $B'$ that is evenly covered by $p'$.
>
> Set $b = h(b') \in B$. Since $p$ is a covering map, $b$ has an open neighborhood $U \subseteq B$ that is evenly covered by $p$: $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$, with each $p|_{V_\alpha}: V_\alpha \to U$ a homeomorphism.
>
> Let $U' = h^{-1}(U) \subseteq B'$. This is open in $B'$ (since $h$ is continuous, so $h^{-1}$ maps open sets to open sets). It contains $b'$ (since $h(b') = b \in U$, so $b' \in h^{-1}(U)$).
>
> We claim $U'$ is evenly covered by $p'$. The preimage is:
>
> $$(p')^{-1}(U') = \{e \in E : p'(e) \in U'\} = \{e \in E : h^{-1}(p(e)) \in h^{-1}(U)\} = \{e \in E : p(e) \in U\} = p^{-1}(U) = \bigsqcup_\alpha V_\alpha.$$
>
> So $(p')^{-1}(U')$ has the same decomposition into slices. Each $p'|_{V_\alpha}: V_\alpha \to U'$ is a homeomorphism because it is the composition
>
> $$V_\alpha \xrightarrow{p|_{V_\alpha}} U \xrightarrow{h^{-1}} U'$$
>
> of two homeomorphisms ($p|_{V_\alpha}$ is a homeomorphism by assumption, and $h^{-1}|_U: U \to U'$ is a homeomorphism since $h$ is a homeomorphism).

^pf-24-5

*Uses:* [[§9 Continuous Functions#^def-9-2|Def. §9.2]], [[§9 Continuous Functions#^thm-9-4|§9.4]], [[§9 Continuous Functions#^prop-9-3|§9.3]]

> [!remark]- Connections
> - Transporting the whole $\pi_1$ computation: [[§23 The Fundamental Group#^rem-23-5|Naturality: Structure Transports Across Homeomorphisms]].

> [!example] Example §24.4: $e^{2\pi i x}: \mathbb{R} \to S^1_{\mathbb{C}}$ as a Transported Covering Map
> We [[§24 Covering Spaces#^thm-24-2|proved]] $p: \mathbb{R} \to S^1_{\mathbb{R}^2}$ by $p(x) = (\cos 2\pi x, \sin 2\pi x)$ is a covering map. The [[§9 Continuous Functions#^ex-9-5|homeomorphism]] $\phi: S^1_{\mathbb{C}} \to S^1_{\mathbb{R}^2}$ by $\phi(z) = (\operatorname{Re}(z), \operatorname{Im}(z))$ gives:
>
> $$p' = \phi^{-1} \circ p: \mathbb{R} \to S^1_{\mathbb{C}}, \qquad p'(x) = \phi^{-1}(\cos 2\pi x, \sin 2\pi x) = \cos 2\pi x + i\sin 2\pi x = e^{2\pi i x}.$$
>
> By the [[§24 Covering Spaces#^prop-24-5|proposition]], $p'$ is automatically a covering map—no need to re-verify the evenly-covered condition from scratch.

^ex-24-4

*Continued in [[§24a Lifting and the Fundamental Group of the Circle]]: lifts, the path and homotopy lifting lemmas, the lifting correspondence, and $\pi_1(S^1) \cong \mathbb{Z}$.*
