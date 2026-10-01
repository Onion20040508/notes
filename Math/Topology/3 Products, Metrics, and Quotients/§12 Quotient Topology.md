---
type: section
subject: "[[Topology]]"
chapter: 3
section: 12
munkres: "§22"
tags: [topology, math590]
---
← [[§11 Metric Topology]] · ↑ [[· 3 Products, Metrics, and Quotients]] · [[§13 Connected Spaces]] →

Motivated from geometry: can form topological spaces by “pasting” or identifying points together on a given space.

> [!example] Example §12.1: Geometric Examples
> - Rectangle $\to$ cylinder $\to$ torus (by identifying edges)
> - “Glue” end points of an interval $[0,1]$ together $\to$ circle
> - Disk $\to$ identify all boundary to one point (collapse the boundary to a point) $\to$ sphere

^ex-12-1

> [!remark] Remark: What Quotient Spaces Represent
> The quotient construction is topology's version of “gluing” and “collapsing.” Given a space $X$ and an equivalence relation $\sim$, we declare certain points to be “the same” and ask: what topology does the resulting space inherit?
>
> This is arguably the most powerful construction in topology. Circles, tori, projective spaces, and spheres all arise as quotient spaces. But it is also the *trickiest*: the quotient topology can behave unexpectedly. A quotient map need not be open (the image of an open set need not be open), and quotient spaces of Hausdorff spaces can fail to be Hausdorff. Developing intuition for when quotients are well-behaved is a recurring theme—particularly important when computing fundamental groups in the second half of this course.

^rem-12-1

## Quotient Maps

> [!definition] Definition §12.1: Quotient Map
> Let $X, Y$ be topological spaces. Let $p: X \to Y$ be a surjective map. The map $p$ is called a **quotient map** if for all $U \subseteq Y$, $U$ is open in $Y$ if and only if $p^{-1}(U)$ is open in $X$.

^def-12-1

> [!remark] Remark
> This is stronger than [[§9 Continuous Functions#^def-9-1|continuity]]. Continuity only requires: $U$ open in $Y$ $\Rightarrow$ $p^{-1}(U)$ open in $X$.
>
> A quotient map additionally requires: $p^{-1}(U)$ open in $X$ $\Rightarrow$ $U$ open in $Y$.

^rem-12-2

## Quotient Topology from a Surjection

> [!theorem] Proposition §12.1: Existence and Uniqueness of the Quotient Topology
> Let $X$ be a topological space, $A$ a set, and $p: X \to A$ a surjective map. Then there exists a unique topology $\mathcal{T}$ on $A$ such that $p$ is a quotient map. Explicitly,
>
> $$
> \mathcal{T} = \{U \subseteq A \mid p^{-1}(U) \text{ open in } X\}.
> $$

^prop-12-1

> [!proof]+ Proof
> **Existence:** We verify $\mathcal{T}$ is a [[§1 Topological Spaces#^def-1-1|topology]] on $A$.
>
> (1) $\emptyset \in \mathcal{T}$: $p^{-1}(\emptyset) = \emptyset$, which is open in $X$. $A \in \mathcal{T}$: $p^{-1}(A) = X$ (since $p$ is surjective), which is open in $X$.
>
> (2) Arbitrary unions: Suppose $\{U_\alpha\}_{\alpha \in J} \subseteq \mathcal{T}$. Then $p^{-1}(U_\alpha)$ is open in $X$ for each $\alpha$. Since
>
> $$
> p^{-1}\!\left(\bigcup_{\alpha \in J} U_\alpha\right) = \bigcup_{\alpha \in J} p^{-1}(U_\alpha),
> $$
>
> this is a union of open sets in $X$, hence open. So $\bigcup U_\alpha \in \mathcal{T}$.
>
> (3) Finite intersections: Suppose $U_1, \ldots, U_n \in \mathcal{T}$. Then $p^{-1}(U_i)$ is open in $X$ for each $i$. Since
>
> $$
> p^{-1}\!\left(\bigcap_{i=1}^n U_i\right) = \bigcap_{i=1}^n p^{-1}(U_i),
> $$
>
> this is a finite intersection of open sets in $X$, hence open. So $\bigcap_{i=1}^n U_i \in \mathcal{T}$.
>
> Thus $\mathcal{T}$ is a topology. By construction, $U \in \mathcal{T} \Leftrightarrow p^{-1}(U)$ is open in $X$, so $p$ is a quotient map with respect to $\mathcal{T}$.
>
> **Uniqueness:** Suppose $\mathcal{T}'$ is any topology on $A$ such that $p: X \to (A, \mathcal{T}')$ is a quotient map. Then by definition of quotient map:
>
> $$
> U \in \mathcal{T}' \iff p^{-1}(U) \text{ is open in } X \iff U \in \mathcal{T}.
> $$
>
> Thus $\mathcal{T}' = \mathcal{T}$.

^pf-12-1

*Uses:* [[§1 Topological Spaces#^def-1-1|Def. §1.1]]

> [!definition] Definition §12.2: Quotient Topology
> The unique topology $\mathcal{T}$ from [[§12 Quotient Topology#^prop-12-1|Proposition §12.1]] is called the **quotient topology** on $A$ induced by $p$.

^def-12-2

> [!remark] Remark: Which Comes First: the Topology or the Map
> We start with $X$ (a topological space), $A$ (a set), and $p: X \to A$ (a surjection). The quotient topology on $A$ is defined so that $p$ becomes a quotient map.

^rem-12-3

> [!remark] Remark: The Quotient Topology is the Finest Making $p$ Continuous
> Many topologies on $A$ can make $p: X \to A$ continuous—continuity only requires the forward direction ($U$ open $\Rightarrow$ $p^{-1}(U)$ open), so *fewer* open sets in $A$ makes continuity *easier*. In particular, the [[§1 Topological Spaces#^ex-1-2|trivial topology]] $\{\emptyset, A\}$ always works. The quotient topology $\mathcal{T}_q = \{U \subseteq A \mid p^{-1}(U) \text{ open in } X\}$ includes *every* set whose preimage is open, making it the **[[§1 Topological Spaces#^def-1-2|finest]]** topology on $A$ for which $p$ is continuous: any topology strictly finer would contain some $U$ with $p^{-1}(U)$ not open, breaking continuity. Any coarser topology $\mathcal{T} \subsetneq \mathcal{T}_q$ also makes $p$ continuous, but not a quotient map—there would exist $U \in \mathcal{T}_q \setminus \mathcal{T}$ with $p^{-1}(U)$ open yet $U \notin \mathcal{T}$, violating the backward direction.
>
> *Example:* Let $p: [0,1] \to \{a, b\}$ with $p(x) = a$ for $x \in [0, 1/2)$ and $p(x) = b$ for $x \in [1/2, 1]$.
>
> - $\mathcal{T}_q = \{\emptyset, \{a\}, \{a,b\}\}$: $p^{-1}(\{a\}) = [0, 1/2)$ is open, $p^{-1}(\{b\}) = [1/2, 1]$ is not. So $\{a\}$ is open but $\{b\}$ is not.
> - Trivial topology $\{\emptyset, \{a,b\}\}$: $p$ is continuous but not quotient ($p^{-1}(\{a\})$ is open yet $\{a\}$ is not declared open).
> - Discrete topology $\{\emptyset, \{a\}, \{b\}, \{a,b\}\}$: $p$ is *not* continuous ($p^{-1}(\{b\}) = [1/2, 1]$ is not open). This is finer than $\mathcal{T}_q$.
>
> The quotient topology sits at the exact boundary: the finest topology where $p$ is still continuous, and the only one where $p$ is a quotient map.

^rem-12-4

> [!remark] Remark: Why Surjectivity is Required
> The definition requires $p: X \to A$ to be surjective. If $a \in A \setminus p(X)$ is a point not in the image, then $p^{-1}(\{a\}) = \emptyset$, which is open in $X$. So $\{a\}$ would be declared open. More generally, for any $U \in \mathcal{T}$ and any $S \subseteq A \setminus p(X)$:
>
> $$
> p^{-1}(U \cup S) = p^{-1}(U) \cup \underbrace{p^{-1}(S)}_{= \emptyset} = p^{-1}(U),
> $$
>
> so $U \cup S \in \mathcal{T}$ whenever $U \in \mathcal{T}$. Points outside the image can be freely added or removed without affecting openness—they automatically get the discrete topology, carrying no information from $X$.
>
> The philosophy of the quotient topology is that *$X$ determines the topology on $A$ through $p$*. If $p$ misses part of $A$, the determination fails at those points: every fiber $p^{-1}(\{a\}) = \emptyset$ tells us nothing. Surjectivity ensures every point of $A$ has a nonempty fiber, so $X$ genuinely controls the entire topology on $A$.

^rem-12-5

## Equivalence Relations and Quotient Spaces

> [!definition] Definition §12.3: Quotient Space
> Suppose we have an equivalence relation $\sim$ on a set $X$. (Recall: $x \sim x$; $x \sim y \Leftrightarrow y \sim x$; $x \sim y$ and $y \sim z \Rightarrow x \sim z$.)
>
> For $x \in X$, let $[x]$ denote its equivalence class. Let $X/{\sim}$ (or $X^*$) denote the set of all equivalence classes (i.e., a partition of $X$ into disjoint subsets whose union is $X$).
>
> The canonical surjection $p: X \to X/{\sim}$, $x \mapsto [x]$, is a quotient map which induces the [[§12 Quotient Topology#^def-12-2|quotient topology]] on $X/{\sim}$.
>
> We call $X/{\sim}$ a **quotient space** of $X$.

^def-12-3

> [!example] Example §12.2: Circle as Quotient Space
> $X = [0, 1]$. Let $\sim$ be defined by $0 \sim 1$ (i.e., glue the endpoints). Then $X/{\sim}$ is homeomorphic to a circle.
>
> $f: X/{\sim} \to S^1$, $f([t]) = e^{2\pi i t}$.

^ex-12-2

![[m590-12-2.svg]]
*Gluing the endpoints of $[0,1]$: the two red endpoints become the single class $[0] = [1]$, and $f([t]) = e^{2\pi i t}$ wraps the interval once around $S^1$ (so $[\tfrac14] \mapsto i$). Only the endpoints are identified; every other class is a single point.*

> [!example] Example §12.3: Torus as Quotient Space
> $X = [0, 1] \times [0, 1]$. Define $\sim$ by:
>
> - $x \times 0 \sim x \times 1$ for all $x \in [0, 1]$
> - $0 \times y \sim 1 \times y$ for all $y \in [0, 1]$
>
> Then $X/{\sim} \cong$ torus.

^ex-12-3

![[m590-12-3.svg]]
*Square to torus: the edges $x \times 0$ and $x \times 1$ (blue, single arrows) are glued to form one circle on the torus, and $0 \times y$ and $1 \times y$ (red, double arrows) are glued to form another. The arrows show the orientations that are matched. All four corners become the single black point where the two circles cross.*

> [!remark]- Connections
> - The quotient map to $S^1 \times S^1$ is justified in [[§12 Quotient Topology#^ex-12-6|Example §12.6: The Square-to-Torus Quotient Map]].

## Properties of Quotient Maps

> [!example] Example §12.4: Composition of Quotient Maps
> Suppose $p, q$ are quotient maps, $X \xrightarrow{p} Y \xrightarrow{q} Z$. Recall $p^{-1}(q^{-1}(U)) = (q \circ p)^{-1}(U)$.
>
> $U \subseteq Z$ open $\Leftrightarrow$ $q^{-1}(U)$ open in $Y$ $\Leftrightarrow$ $p^{-1}(q^{-1}(U))$ open in $X$ $\Leftrightarrow$ $(q \circ p)^{-1}(U)$ open in $X$.
>
> So $q \circ p$ is a quotient map.

^ex-12-4

> [!example] Example §12.5: Quotient Topology Example
> $p: \mathbb{R} \to \{a, b, c\}$, $p(x) = \begin{cases} a & \text{if } x < 0 \\ b & \text{if } x > 0 \\ c & \text{if } x = 0 \end{cases}$
>
> What is the quotient topology induced by $p$ on $\{a, b, c\}$?
>
> $\{\emptyset, \{a\}, \{b\}, \{a, b\}, \{a, b, c\}\}$.
>
> Since $\{0\}, (-\infty, 0], [0, +\infty)$ are not open in $\mathbb{R}$.
>
> It suffices to find the allowed basis of $Y$ to find the quotient topology on $Y$. Verify.
>
> **Remark:** The quotient space we found is not Hausdorff, but $\mathbb{R}$ is.

^ex-12-5

> [!definition] Definition §12.4: Open and Closed Maps
> $f: X \to Y$ is **open** (resp. **closed**) if for all open (resp. closed) $U \subseteq X$, $f(U)$ is open (resp. closed) in $Y$.

^def-12-4

> [!theorem] Proposition §12.2
> If $p: X \to Y$ is a surjective continuous map that is either open or closed, then $p$ is a quotient map.

^prop-12-2

> [!proof]+ Proof
> Since $p$ is continuous, $U$ open in $Y$ $\Rightarrow$ $p^{-1}(U)$ open in $X$. We need the converse.
>
> **Case 1: $p$ is open.** Suppose $p^{-1}(U)$ is open in $X$. Since $p$ is surjective, $p(p^{-1}(U)) = U$. Since $p$ is open and $p^{-1}(U)$ is open, $U = p(p^{-1}(U))$ is open in $Y$.
>
> **Case 2: $p$ is closed.** Suppose $p^{-1}(U)$ is open in $X$. Then $X \setminus p^{-1}(U) = p^{-1}(Y \setminus U)$ is closed in $X$. Since $p$ is closed and surjective, $p(p^{-1}(Y \setminus U)) = Y \setminus U$ is closed in $Y$. Thus $U$ is open in $Y$.

^pf-12-2

> [!remark] Remark: This is a Strong Condition
> Being open or closed is *sufficient* but not *necessary* for a continuous surjection to be a quotient map. There exist quotient maps that are neither open nor closed (HW5: $\pi_1|_A$ where $A$ is chosen so that the restriction maps some open sets to non-open sets and some closed sets to non-closed sets). In practice, the compact-to-Hausdorff shortcut ([[§15 Compact Spaces#^rem-15-6|§15, closed-map argument]]) is often more useful: a continuous surjection from a compact space to a Hausdorff space is automatically a closed map, hence a quotient map.

^rem-12-6

## Universal Property of Quotient Maps

> [!theorem] Theorem §12.3: Universal Property
> Let $p: X \to Y$ be a quotient map. Let $Z$ be a space and $g: X \to Z$ be a map that is constant on each set $p^{-1}(\{y\})$ for all $y \in Y$. Then there exists a unique $f: Y \to Z$ such that $f \circ p = g$. Moreover:
>
> 1. $f$ continuous $\Leftrightarrow$ $g$ continuous
> 2. $f$ is quotient map $\Leftrightarrow$ $g$ is quotient map
>
> ![[m590-12-1.svg]]
> *$g$ factors through the quotient map $p$ (double-headed arrow: surjective) as $g = f \circ p$. The red dashed arrow is the induced $f$, which exists and is unique because $g$ is constant on each fiber $p^{-1}(\{y\})$. Statements (1) and (2) say that $f$ inherits continuity, and the quotient property, from $g$.*

^thm-12-3

> [!remark] Remark: Constant on Fibers
> “$g$ is constant on each fiber $p^{-1}(\{y\})$” means: if $p(x_1) = p(x_2)$, then $g(x_1) = g(x_2)$.
>
> This condition is necessary for $f$ to be well-defined. We want to define $f(y) = g(x)$ for any $x$ with $p(x) = y$. But there may be many such $x$'s in the fiber $p^{-1}(\{y\})$. For $f$ to be well-defined, $g$ must give the same value on all of them.

^rem-12-7

> [!proof]+ Proof
> To define $f: Y \to Z$: for each $y \in Y$, $g(p^{-1}(\{y\})) = \{z_y\}$ is a one-point set (since $g$ is constant on fibers).
>
> Define $f(y) = z_y$, then $f(p(x)) = z_{p(x)} = g(x)$.
>
> **Proof of (1):** If $f$ is continuous, $g$ is a [[§9 Continuous Functions#^thm-9-4|composition of continuous maps]] $\Rightarrow$ $g$ continuous.
>
> If $g$ continuous, let $V \subseteq Z$ be open. $g^{-1}(V)$ open in $X$. But $g^{-1}(V) = (f \circ p)^{-1}(V) = p^{-1}(f^{-1}(V))$.
>
> Since $p$ is a quotient map, $f^{-1}(V)$ is open in $Y$. $\Rightarrow$ $f$ is continuous.
>
> **Proof of (2):** If $f$ is a quotient map, $g$ is a [[§12 Quotient Topology#^ex-12-4|composition of quotient maps]], so $g$ is a quotient map.
>
> If $g$ is a quotient map, then $g$ surjective $\Rightarrow$ $f$ surjective.
>
> Let $V \subseteq Z$. $f^{-1}(V)$ open in $Y$ $\Leftrightarrow$ $p^{-1}(f^{-1}(V))$ open in $X$ $\Leftrightarrow$ $g^{-1}(V)$ open in $X$ $\Leftrightarrow$ $V$ open in $Z$.
>
> So $f$ is a quotient map.

^pf-12-3

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]], [[§12 Quotient Topology#^ex-12-4|Ex. §12.4]]

> [!theorem] Corollary §12.4: Induced Bijection from Quotient
> Let $p: X \to X^*$ be a quotient map, where $X^* = \{g^{-1}(\{z\}) \mid z \in Z\}$, where $g: X \to Z$ is surjective continuous. Then the map $g$ induces a bijection continuous map $f: X^* \to Z$.
>
> Moreover:
>
> 1. $f$ is a homeomorphism $\Leftrightarrow$ $g$ is a quotient map.
> 2. If $Z$ is Hausdorff, then so is $X^*$.

^cor-12-4

> [!proof]+ Proof
> By [[Universal Property of Quotient Maps|the preceding theorem]], $g$ induces a continuous $f: X^* \to Z$. Since $g$ is surjective $\Rightarrow$ $f$ is surjective (since $f \circ p = g$).
>
> If $f(y_1) = f(y_2) = z$ with $y_1, y_2 \in X^*$, then $y_1 = g^{-1}(\{z\}) = y_2$, since the only element of $X^*$ that $f$ sends to $z$ is the fiber $g^{-1}(\{z\})$. So $f$ is injective $\Rightarrow$ $f$ is bijective.
>
> **Proof of (1):** If $f$ is a homeomorphism, then in particular $f$ is a quotient map. Then $g$ is a [[§12 Quotient Topology#^ex-12-4|composition of quotient maps]] $\Rightarrow$ $g$ is a quotient map.
>
> Conversely, suppose $g$ is a quotient map. By [[Universal Property of Quotient Maps|the theorem]], $f$ is also a quotient map. Since $f$ is bijective, $f^{-1}$ is well defined and continuous. So $f$ is a homeomorphism.
>
> **Proof of (2):** Suppose $Z$ is Hausdorff. Let $x, y \in X^*$, $x \neq y$. Since $f$ is injective $\Rightarrow$ $f(x) \neq f(y)$, and there exist disjoint neighborhoods $U$ and $V$ such that $f(x) \in U$ and $f(y) \in V$. Then $f^{-1}(U)$ and $f^{-1}(V)$ are disjoint neighborhoods of $x$ and $y$ in $X^*$.

^pf-12-4

*Uses:* [[§12 Quotient Topology#^thm-12-3|§12.3]], [[§12 Quotient Topology#^ex-12-4|Ex. §12.4]]

> [!theorem] Theorem §12.5: Product of Quotient Maps (Compact-Hausdorff Case)
> Let $\pi_1: X_1 \to Y_1$ and $\pi_2: X_2 \to Y_2$ be quotient maps. If $X_1 \times X_2$ is compact and $Y_1 \times Y_2$ is Hausdorff, then
>
> $$
> \pi_1 \times \pi_2: X_1 \times X_2 \to Y_1 \times Y_2, \qquad (\pi_1 \times \pi_2)(x_1, x_2) = (\pi_1(x_1), \pi_2(x_2))
> $$
>
> is a quotient map.

^thm-12-5

> [!proof]+ Proof
> We verify the hypotheses of the compact-to-Hausdorff shortcut ([[§15 Compact Spaces#^rem-15-6|§15, closed-map argument]]):
>
> - *Continuous:* $\pi_1$ and $\pi_2$ are continuous, so $\pi_1 \times \pi_2$ is continuous ([[§10 Product Topology on Arbitrary Products#^thm-10-1|a map into a product is continuous iff each coordinate function is]]).
> - *Surjective:* Given $(y_1, y_2) \in Y_1 \times Y_2$, surjectivity of $\pi_1$ and $\pi_2$ gives $x_1, x_2$ with $\pi_i(x_i) = y_i$, so $(\pi_1 \times \pi_2)(x_1, x_2) = (y_1, y_2)$.
> - *Compact domain:* $X_1 \times X_2$ is compact by assumption.
> - *Hausdorff codomain:* $Y_1 \times Y_2$ is Hausdorff by assumption.
>
> So $\pi_1 \times \pi_2$ is a continuous surjection from a compact space to a Hausdorff space, hence closed, [[§12 Quotient Topology#^prop-12-2|hence a quotient map]].

^pf-12-5

*Uses:* [[§10 Product Topology on Arbitrary Products#^thm-10-1|§10.1]], [[§15 Compact Spaces#^thm-15-2|§15.2]], [[§15 Compact Spaces#^thm-15-3|§15.3]], [[§15 Compact Spaces#^thm-15-4|§15.4]], [[§12 Quotient Topology#^prop-12-2|§12.2]]

> [!example] Example §12.6: The Square-to-Torus Quotient Map
> Each $\pi_i: [0, 2\pi] \to S^1$ by $\pi_i(s) = e^{is}$ is a quotient map (compact $\to$ Hausdorff). The product $\pi_1 \times \pi_2: [0, 2\pi]^2 \to S^1 \times S^1 = T^2$ is automatically a quotient map by [[§12 Quotient Topology#^thm-12-5|the theorem]]: $[0, 2\pi]^2$ is compact and $T^2$ is Hausdorff.

^ex-12-6

> [!remark] Remark: The Quotient Space Toolkit
> Three theorems form the complete toolkit for working with quotient spaces:
>
> **Theorem A (Compact-to-Hausdorff, [[§15 Compact Spaces#^rem-15-6|§15, closed-map argument]]):** A continuous surjection from a compact space to a Hausdorff space is automatically a quotient map. This is how you *verify* that a map is a quotient map without checking the open-set condition directly.
>
> **Theorem B (Product of Quotients, [[§12 Quotient Topology#^thm-12-5|above]]):** Products of quotient maps are quotient maps (in the compact-Hausdorff setting). This is how you *build quotient maps of product spaces* from quotient maps of the factors.
>
> **Theorem C (Universal Property, [[Universal Property of Quotient Maps|Thm. §12.3]]):** If $\pi$ is a quotient map and $g$ is constant on fibers of $\pi$, then $g$ descends to a continuous map on the quotient. This is how you *construct continuous maps on quotient spaces*.
>
> The standard workflow: use A and B to establish that your map is a quotient map, then use C to descend maps from the “simple” space to the “glued” space. This toolkit will be used extensively in Part II for computing fundamental groups of spaces built by gluing.

^rem-12-8

> [!remark]- Connections
> - Revisited in Part II: [[§21 Algebra Prerequisites꞉ Groups#^rem-II-2|Remark: The Role of the Quotient Space Toolkit in Part II]].
