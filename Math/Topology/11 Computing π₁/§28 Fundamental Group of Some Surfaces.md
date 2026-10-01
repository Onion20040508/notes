---
type: section
subject: "[[Topology]]"
chapter: 11
section: 28
munkres: "§60"
tags: [topology, math590]
---
← [[§27 The Fundamental Group of Sⁿ]] · ↑ [[· 11 Computing π₁]] · [[§29 The Seifert–van Kampen Theorem]] →

## The Projective Plane $P^2$

> [!definition] Definition §28.1: Projective Plane
> The **projective plane** $P^2$ is the [[§12 Quotient Topology#^def-12-3|quotient space]] obtained from $S^2$ by identifying each point with its antipodal point:
>
> $$
> P^2 = S^2 / (x \sim -x).
> $$
>
> The quotient map is $p: S^2 \to P^2$, $p(x) = \{x, -x\}$ (the equivalence class).

^def-28-1

> [!theorem] Theorem §28.1: $p: S^2 \to P^2$ is a Covering Map
> The quotient map $p: S^2 \to P^2$ is a $2$-sheeted [[§24 Covering Spaces#^def-24-2|covering map]] (recall from [[§24 Covering Spaces#^def-24-5|§24]]: this means every fiber $p^{-1}(y)$ has exactly $2$ elements).

^thm-28-1

> [!proof]+ Proof
> We verify three properties.
>
> **$p$ is continuous.** This is immediate: $p$ is a [[§12 Quotient Topology#^def-12-1|quotient map]].
>
> **$p$ is an [[§12 Quotient Topology#^def-12-4|open map]].** The antipodal map $a: S^2 \to S^2$, $a(x) = -x$, is a [[§9 Continuous Functions#^def-9-2|homeomorphism]] (it is continuous, bijective, and its own inverse: $a \circ a = \operatorname{id}$). If $U \subseteq S^2$ is open, then $a(U)$ is also open. Now $p^{-1}(p(U)) = U \cup a(U)$, which is a union of open sets, hence open in $S^2$. By the definition of [[§12 Quotient Topology#^def-12-2|quotient topology]], $p(U)$ is open in $P^2$. So $p$ is an open map.
>
> **Every point has an [[§24 Covering Spaces#^def-24-1|evenly covered]] neighborhood.** Let $y \in P^2$. The fiber $p^{-1}(y)$ consists of two antipodal points $\{x, -x\} \subseteq S^2$. Choose $\varepsilon < 1$ (using the Euclidean metric in $\mathbb{R}^3$) and let $U = B(x, \varepsilon) \cap S^2$ be an open neighborhood of $x$ in $S^2$.
>
> Since $\varepsilon < 1$ and $d(x, -x) = 2$, the set $U$ contains no pair of antipodal points: if $z \in U$, then $d(z, x) < 1$, so $d(-z, x) \geq d(x, -x) - d(-z, -x) = 2 - d(z, x) > 1$, hence $-z \notin U$.
>
> Therefore $p|_U: U \to p(U)$ is injective (distinct points in $U$ go to distinct equivalence classes). Since $p$ is continuous and open, $p|_U$ is a homeomorphism onto $p(U)$.
>
> Similarly, $a(U) = B(-x, \varepsilon) \cap S^2$ is an open neighborhood of $-x$, disjoint from $U$, and $p|_{a(U)}: a(U) \to p(U)$ is also a homeomorphism.
>
> The preimage is $p^{-1}(p(U)) = U \sqcup a(U)$ — two disjoint open sets, each mapped homeomorphically onto $p(U)$. So $p(U)$ is evenly covered, and $p$ is a $2$-sheeted covering map.

^pf-28-1

*Uses:* [[§12 Quotient Topology#^def-12-2|Def. §12.2]], [[§24 Covering Spaces#^def-24-1|Def. §24.1]], [[§12 Quotient Topology#^def-12-1|Def. §12.1]], [[§12 Quotient Topology#^def-12-4|Def. §12.4]], [[§9 Continuous Functions#^def-9-2|Def. §9.2]]

![[m590-28-1.svg]]
*The evenly covered neighborhood from the proof: $U = B(x,\varepsilon)\cap S^2$ (dark red) and its antipodal copy $a(U)$ (light red, on the far side of the sphere) are disjoint because $\varepsilon < 1$ while $d(x,-x) = 2$ (dotted diameter). $p$ maps each of them homeomorphically onto the same set $p(U) \subseteq P^2$: two sheets over $p(U)$.*

> [!remark]- Connections
> - In every dimension the quotient Sⁿ → ℝPⁿ is a two-to-one local diffeomorphism: [[§14 Local Diffeomorphisms and Submersions#^ex-14-2|591 Ex. §14.2]].

> [!theorem] Theorem §28.2: $\pi_1(P^2) \cong \mathbb{Z}/2\mathbb{Z}$
> The fundamental group of the projective plane is the cyclic group of order $2$.

^thm-28-2

> [!proof]+ Proof
> The quotient map $p: S^2 \to P^2$ is a covering map ([[§28 Fundamental Group of Some Surfaces#^thm-28-1|proved above]]). Since $S^2$ is simply connected ($\pi_1(S^2) = 0$, proved in §27 ([[Sⁿ is Simply Connected for n ≥ 2|§27.3]])), the [[§24 Covering Spaces#^def-24-7|lifting correspondence]]
>
> $$
> \phi: \pi_1(P^2, y_0) \to p^{-1}(y_0)
> $$
>
> is a bijection (by [[Properties of the Lifting Correspondence|Theorem §24.9]]: when the covering space is simply connected, the lifting correspondence is bijective).
>
> The fiber $p^{-1}(y_0) = \{x_0, -x_0\}$ has exactly $2$ elements (the point and its antipode). Therefore $|\pi_1(P^2, y_0)| = 2$.
>
> Any group of order $2$ is isomorphic to $\mathbb{Z}/2\mathbb{Z}$: if $\pi_1(P^2) = \{e, g\}$, then $g \neq e$ and $g^2$ must be $e$ or $g$. If $g^2 = g$, then $g = e$ (multiply by $g^{-1}$), contradicting $g \neq e$. So $g^2 = e$, and the map $k \mapsto g^k$ gives an isomorphism $\mathbb{Z}/2\mathbb{Z} \to \pi_1(P^2)$.

^pf-28-2

*Uses:* [[§28 Fundamental Group of Some Surfaces#^thm-28-1|§28.1]], [[Sⁿ is Simply Connected for n ≥ 2|§27.3]], [[Properties of the Lifting Correspondence|§24.9]], [[§24 Covering Spaces#^def-24-7|Def. §24.7]]

> [!remark]- Connections
> - Recomputed with van Kampen: $\pi_1(P^2) \cong \mathbb{Z}/2\mathbb{Z}$ via van Kampen ([[§29 The Seifert–van Kampen Theorem#^ex-29-5|Ex. §29.5]]).
> - The final step is the case p = 2 of [[§27 The Index and Lagrange's Theorem#^thm-27-7|493 Thm. §27.7]] (hub [[Groups of Prime Order Are Cyclic]]); the group itself is [[§7 The Group ℤ∕nℤ#^def-7-1|493 Def. §7.1]].

> [!remark] Remark: The Non-Trivial Loop in $P^2$
> The generator of $\pi_1(P^2)$ is any path in $S^2$ from $x_0$ to $-x_0$ (e.g., half a great circle), projected to $P^2$. This projects to a *loop* in $P^2$ (since $p(x_0) = p(-x_0) = y_0$). It cannot be contracted because its lift in $S^2$ is a path from $x_0$ to $-x_0$, which is not a loop.
>
> Traversing this loop twice gives a full great circle in $S^2$, which IS contractible (since $S^2$ is simply connected ([[Sⁿ is Simply Connected for n ≥ 2|§27.3]])). So the generator has order $2$: $[g]^2 = [e]$.

^rem-28-1

![[m590-28-2.svg]]
*Why the generator has order $2$. The first traversal of $g$ lifts to the half great circle from $x_0$ to $-x_0$ (solid red), which is not a loop in $S^2$, so $[g] \neq [e]$. The second traversal lifts to the antipodal half (dashed) and returns to $x_0$; together they form a full great circle, a loop in the simply connected $S^2$, so $[g]^2 = [e]$.*

## Projective $n$-Space

> [!definition] Definition §28.2: Projective $n$-Space
> For any $n \geq 1$, the **real projective $n$-space** is $P^n = S^n / (x \sim -x)$.

^def-28-2

[[§28 Fundamental Group of Some Surfaces#^pf-28-1|The same proof]] shows: $p: S^n \to P^n$ is a $2$-sheeted covering map (the antipodal map is a homeomorphism in any dimension, and the $\varepsilon$-ball argument is dimension-independent).

> [!remark]- Connections
> - In 591 ℝPⁿ gets a smooth atlas, [[§8 Differentiable Structures#^cor-8-10|591 Cor. §8.10]], and this quotient topology is shown to agree with its Grassmannian description, [[§8 Differentiable Structures#^prop-8-11|591 Prop. §8.11]]; the complex analogue ℂPⁿ is [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|591 Def. §3.11]].

> [!theorem] Theorem §28.3: $\pi_1(P^n)$ for all $n$
> $$
> \pi_1(P^n) \cong \begin{cases} \mathbb{Z} & n = 1 \text{ (since $P^1 \cong S^1$)} \\ \mathbb{Z}/2\mathbb{Z} & n \geq 2. \end{cases}
> $$

^thm-28-3

> [!proof]+ Proof
> For $n \geq 2$: $S^n$ is simply connected ([[Sⁿ is Simply Connected for n ≥ 2|§27]]), so the [[Properties of the Lifting Correspondence|lifting correspondence]] $\pi_1(P^n) \to p^{-1}(y_0)$ is a bijection. The fiber has $2$ elements, so $|\pi_1(P^n)| = 2$, giving $\pi_1(P^n) \cong \mathbb{Z}/2\mathbb{Z}$.
>
> For $n = 1$: $P^1 = S^1 / (x \sim -x)$. The map $z \mapsto z^2$ is a homeomorphism $P^1 \to S^1$ (it identifies antipodal points on $S^1$ and maps onto $S^1$ bijectively). So $\pi_1(P^1) \cong \pi_1(S^1)$ ([[§23 The Fundamental Group#^cor-23-6|§23.6]]) $\cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]).

^pf-28-3

*Uses:* [[Sⁿ is Simply Connected for n ≥ 2|§27.3]], [[Properties of the Lifting Correspondence|§24.9]], [[§23 The Fundamental Group#^cor-23-6|§23.6]], [[Fundamental Group of the Circle|§24.10]]

## The Wedge Sum

> [!definition] Definition §28.3: Wedge Sum
> Let $X$ and $Y$ be topological spaces with chosen basepoints $x_0 \in X$ and $y_0 \in Y$. The **wedge sum** (or **wedge product**) $X \vee Y$ is the quotient space
>
> $$
> X \vee Y = (X \sqcup Y) / (x_0 \sim y_0),
> $$
>
> i.e., the disjoint union of $X$ and $Y$ with the two basepoints identified to a single point. The result is a space where $X$ and $Y$ are “joined at a single point.”

^def-28-3

> [!remark] Remark: The Topology on $X \vee Y$
> The wedge sum is a quotient space ([[§12 Quotient Topology|§12]]), so its topology is the **[[§12 Quotient Topology#^def-12-2|quotient topology]]** induced by the canonical surjection $q: X \sqcup Y \to X \vee Y$ that sends $x_0$ and $y_0$ to the same point $[x_0] = [y_0]$ and is injective on every other point.
>
> **What are the open sets?** A set $W \subseteq X \vee Y$ is open if and only if $q^{-1}(W)$ is open in $X \sqcup Y$. Since the disjoint union topology declares $U \subseteq X \sqcup Y$ open iff $U \cap X$ is open in $X$ and $U \cap Y$ is open in $Y$, this gives:
> - If $[x_0] \notin W$: then $W$ is open iff it is an open subset of $X \setminus \{x_0\}$ or $Y \setminus \{y_0\}$ (or a union of such).
> - If $[x_0] \in W$: then $W$ is open iff its preimage meets $X$ in an open neighborhood of $x_0$ in $X$ *and* meets $Y$ in an open neighborhood of $y_0$ in $Y$.
>
> In other words, away from the junction point, $X \vee Y$ looks like $X$ or $Y$ individually. At the junction point, a neighborhood must extend into *both* $X$ and $Y$ — this is where the two spaces are genuinely glued together.

^rem-28-2

> [!example] Example §28.1: Wedge Sums
> - $S^1 \vee S^1$: two circles sharing one point — the [[§28 Fundamental Group of Some Surfaces#^def-28-4|figure eight]]. A neighborhood of the junction point is a cross (small arc of each circle).
> - $S^1 \vee S^1 \vee S^1$: three circles sharing one point.
> - $S^2 \vee S^2$: two spheres touching at one point. A neighborhood of the junction is a union of two small disks, one from each sphere.
> - $T^2 \vee T^2$: two tori sharing one point (arises in the double torus retraction, [[§28 Fundamental Group of Some Surfaces#^pf-28-5|§28]]).

^ex-28-1

> [!remark]- Connections
> - $\pi_1(S^2 \vee S^2) = 0$: [[§27 The Fundamental Group of Sⁿ#^ex-27-1|Wedge of Two Spheres is Simply Connected]]. $\pi_1$ of a wedge of circles: $F_n$ ([[§29 The Seifert–van Kampen Theorem#^ex-29-3|Ex. §29.3]]).

> [!remark] Remark: Wedge Sum vs. Product
> The wedge sum $X \vee Y$ and the product $X \times Y$ are very different constructions:
> - **Topologically:** $X \vee Y$ glues $X$ and $Y$ at a single point; $X \times Y$ takes all pairs $(x, y)$. The wedge sum has $\dim(X \vee Y) = \max(\dim X, \dim Y)$, while $\dim(X \times Y) = \dim X + \dim Y$.
> - **For $\pi_1$:** The product gives $\pi_1(X \times Y) \cong \pi_1(X) \times \pi_1(Y)$ ([[§21 Algebra Prerequisites꞉ Groups#^def-21-5|direct product]], always abelian if the factors are; [[§23 The Fundamental Group#^thm-23-7|proved in §23]]). The wedge sum gives $\pi_1(X \vee Y) \cong \pi_1(X) * \pi_1(Y)$ ([[§21 Algebra Prerequisites꞉ Groups#^def-21-9|free product]], typically non-abelian) when $X$ and $Y$ are “nice” — but proving this requires the [[§29 The Seifert–van Kampen Theorem#^cor-29-2|Seifert-van Kampen theorem (§29)]]. For now, we prove a weaker result: $\pi_1(S^1 \vee S^1)$ is non-abelian ([[§28 Fundamental Group of Some Surfaces#^thm-28-4|§28.4]]).

^rem-28-3

> [!remark]- Connections
> - The algebraic side of the same contrast: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-10|Direct Product vs Free Product]].

## The Figure Eight: Non-Commutativity

> [!definition] Definition §28.4: Figure Eight (Wedge of Circles)
> The **figure eight** space is $X = S^1 \vee S^1$, the [[§28 Fundamental Group of Some Surfaces#^def-28-3|wedge sum]] of two circles. Concretely, $X = A \cup B$ where $A$ and $B$ are circles in $\mathbb{R}^2$ that intersect in exactly one point $x_0$ (the basepoint).

^def-28-4

![[m590-28-3.svg]]
*The figure eight $X = A \cup B$: the circles $A$ (blue, traversed by $f$) and $B$ (red, traversed by $g$) meet only at $x_0$. A basic neighborhood of $x_0$ (green, open ends hollow) contains a small open arc of each circle through $x_0$: the cross of Example §28.1.*

We cannot yet prove $\pi_1(X) \cong F_2$ (that requires the [[§29 The Seifert–van Kampen Theorem#^ex-29-2|Seifert-van Kampen theorem, §29]]). But using covering spaces, we can prove the key fact that $\pi_1(X)$ is **non-abelian**: $[f] * [g] \neq [g] * [f]$ for the generators.

> [!theorem] Theorem §28.4: $\pi_1$ of the Figure Eight is Non-Abelian
> Let $X = A \cup B$ be the figure eight, with $A, B$ circles meeting at $x_0$. Let $f$ be a loop traversing $A$ once and $g$ a loop traversing $B$ once. Then $f * g \not\simeq_p g * f$.

^thm-28-4

> [!proof]+ Proof
> We construct a covering space of $X$ and use the [[Path Lifting Lemma|uniqueness of path lifting]].
>
> **Step 1: The covering space.** Let $E \subseteq \mathbb{R}^2$ be the space consisting of:
> - The $x$-axis and the $y$-axis (two perpendicular lines).
> - At each nonzero integer point $n \times 0$ on the $x$-axis: a small circle tangent to the $x$-axis at that point.
> - At each nonzero integer point $0 \times n$ on the $y$-axis: a small circle tangent to the $y$-axis at that point.
>
> Let $e_0 = (0, 0)$ (the origin).
>
> **Step 2: The covering map.** Define $p: E \to X$ as follows:
> - $p$ wraps the $x$-axis around circle $A$: integer points map to $x_0$.
> - $p$ wraps the $y$-axis around circle $B$: integer points map to $x_0$.
> - Each small circle tangent to the $x$-axis at $n \times 0$ is mapped homeomorphically onto $B$.
> - Each small circle tangent to the $y$-axis at $0 \times n$ is mapped homeomorphically onto $A$.
> - All tangent points map to $x_0$.
>
> One can verify that $p$ is a covering map (each point of $X$ has an [[§24 Covering Spaces#^def-24-1|evenly covered]] neighborhood).
>
> **Step 3: Lift $f * g$ and $g * f$.**
>
> *Recall the framework ([[§24 Covering Spaces|§24]]).* We have a covering map $p: E \to B$ (here $B = X$ is the figure eight, $E$ is the grid-with-circles space from Step 1). Two results from §24 do all the work:
>
> - **[[Path Lifting Lemma|Path lifting theorem]]:** Given a path $\alpha$ in $B$ starting at $b_0$, and a point $e_0 \in E$ with $p(e_0) = b_0$, there exists a *unique* path $\tilde{\alpha}$ in $E$ satisfying two conditions:
>     1. $\tilde{\alpha}(0) = e_0$ (starts at the chosen lift of the basepoint),
>     2. $p \circ \tilde{\alpha} = \alpha$ (projects back to the original path).
>
>     To find a lift, it suffices to exhibit *any* path in $E$ satisfying (1) and (2) — uniqueness guarantees it is the only one.
> - **[[§24 Covering Spaces#^thm-24-8|Homotopy lifting lemma]]:** If two loops $\alpha \simeq_p \beta$ are path-homotopic in $B$, then their lifts starting at the same point $e_0$ must end at the same point. Equivalently: *different endpoints $\Rightarrow$ the loops are not path-homotopic ([[§24 Covering Spaces#^rem-24-10|§24]]).*
>
> *Our setup:* $B = X$ (figure eight), $E$ = grid-with-circles, $b_0 = x_0$ (junction point), $e_0 = (0,0)$, and $p(0,0) = x_0$. ✓
>
> **Lifting $f$ from $(0,0)$.** The loop $f: I \to X$ traverses circle $A$ once, starting and ending at $x_0$. We need to find a path $\tilde{f}$ in $E$ satisfying (1) $\tilde{f}(0) = (0,0)$ and (2) $p \circ \tilde{f} = f$.
>
> By construction, $p$ maps the $x$-axis to circle $A$ by wrapping — exactly like the standard covering $\mathbb{R} \to S^1$ ([[§24 Covering Spaces#^thm-24-2|§24.2]]): the segment from $(0,0)$ to $(1,0)$ maps onto $A$, with both endpoints mapping to $x_0$. So define $\tilde{f}(s) = (s, 0)$ for $s \in [0,1]$. Check:
> 1. $\tilde{f}(0) = (0, 0) = e_0$. ✓
> 2. $p(\tilde{f}(s)) = p(s, 0) = f(s)$ for all $s$, since $p$ restricted to this segment of the $x$-axis traces out $A$ exactly as $f$ does. ✓
>
> By **uniqueness** of path lifting, this is *the* lift. Endpoint: $\tilde{f}(1) = (1, 0)$.
>
> **Lifting $g$ from $(0,0)$.** The loop $g: I \to X$ traverses circle $B$ once. By the same reasoning, $p$ maps the $y$-axis to $B$ by wrapping. Define $\tilde{g}(s) = (0, s)$. Check:
> 1. $\tilde{g}(0) = (0, 0) = e_0$. ✓
> 2. $p(\tilde{g}(s)) = p(0, s) = g(s)$. ✓
>
> Endpoint: $\tilde{g}(1) = (0, 1)$.
>
> **Lifting $f * g$ from $(0,0)$.** The concatenation $f * g$ first traverses $A$, then $B$. To lift it, we lift each half in sequence — the lift of the second half must *start where the first half ended* (since the lift is a continuous path in $E$).
>
> *First half (lifting $f$ from $(0,0)$):* Exactly as above. The lift goes along the $x$-axis from $(0,0)$ to $(1,0)$.
>
> *Second half (lifting $g$ from $(1,0)$):* We now need a path in $E$ that starts at $(1,0)$ and projects to $g$ (the loop traversing $B$). The question is: *what part of $E$ sits above circle $B$ near the point $(1,0)$?*
>
> By construction of $E$ (Step 1), there is a small circle tangent to the $x$-axis at $(1,0)$, and $p$ maps this circle homeomorphically onto $B$ (with the tangent point $(1,0)$ mapping to $x_0$). So the path that goes around this small circle starting and ending at $(1,0)$ is a valid lift: it starts at $(1,0)$ and projects to $g$. By uniqueness, it is the only lift.
>
> Note that the $y$-axis also maps to $B$, but it is irrelevant here — the $y$-axis passes through $(0,0)$, not $(1,0)$. The lift starting at $(1,0)$ must stay in the part of $E$ that contains $(1,0)$ and maps to $B$, which is the small tangent circle.
>
> **Result:** The lift of $f * g$ starts at $(0,0)$ and ends at $\mathbf{(1,0)}$.
>
> **Lifting $g * f$ from $(0,0)$.** Now $g * f$ first traverses $B$, then $A$.
>
> *First half (lifting $g$ from $(0,0)$):* The lift goes along the $y$-axis from $(0,0)$ to $(0,1)$.
>
> *Second half (lifting $f$ from $(0,1)$):* We need a path in $E$ starting at $(0,1)$ that projects to $f$ (the loop traversing $A$). What part of $E$ sits above circle $A$ near $(0,1)$? By construction, there is a small circle tangent to the $y$-axis at $(0,1)$, mapped homeomorphically onto $A$ by $p$ (with the tangent point $(0,1)$ mapping to $x_0$). The lift goes around this small circle, returning to $(0,1)$.
>
> Again, the $x$-axis also maps to $A$, but passes through $(0,0)$ not $(0,1)$, so it plays no role here.
>
> **Result:** The lift of $g * f$ starts at $(0,0)$ and ends at $\mathbf{(0,1)}$.
>
> **Step 4: Conclude.** The lifts of $f * g$ and $g * f$ both start at $e_0 = (0, 0)$ but end at *different points*: $(1, 0) \neq (0, 1)$.
>
> By the **[[§24 Covering Spaces#^thm-24-8|homotopy lifting lemma]]** ([[§24 Covering Spaces|§24]]): if $f * g \simeq_p g * f$, then their lifts starting at the same point $(0,0)$ must end at the same point. But the lift of $f * g$ ends at $(1, 0)$ while the lift of $g * f$ ends at $(0, 1)$. Contradiction.
>
> Therefore $f * g \not\simeq_p g * f$, i.e., $[f] * [g] \neq [g] * [f]$ in $\pi_1(X, x_0)$, so $\pi_1(X, x_0)$ is non-abelian.

^pf-28-4

*Uses:* [[Path Lifting Lemma|§24.6]], [[§24 Covering Spaces#^thm-24-8|§24.8]], [[§24 Covering Spaces#^thm-24-2|§24.2]], [[§24 Covering Spaces#^def-24-1|Def. §24.1]]

![[m590-28-4.svg]]
*The covering $p: E \to X$ from the proof. The $x$-axis and the circles on the $y$-axis lie over $A$ (blue); the $y$-axis and the circles on the $x$-axis lie over $B$ (red). The lift of $f*g$ from $e_0$ runs along the $x$-axis to $(1,0)$ and then around the red circle there, so it ends at $(1,0)$. The lift of $g*f$ runs up to $(0,1)$ and around the blue circle, so it ends at $(0,1)$. Different endpoints, so $f*g \not\simeq_p g*f$.*

> [!remark] Remark
> This proves $\pi_1(X)$ is non-abelian, which already distinguishes the figure eight from any space with abelian $\pi_1$ (such as the [[§23 The Fundamental Group#^cor-23-8|torus]], $S^1$ ([[Fundamental Group of the Circle|§24.10]]), or any $S^n$ ([[Sⁿ is Simply Connected for n ≥ 2|§27.3]])). The full result $\pi_1(X) \cong F_2$ (the [[§21 Algebra Prerequisites꞉ Groups#^def-21-8|free group]] on two generators — meaning not only non-abelian, but with *no relations at all* between $[f]$ and $[g]$) requires the [[§29 The Seifert–van Kampen Theorem#^ex-29-2|Seifert-van Kampen theorem (§29)]].

^rem-28-4

## The Double Torus

> [!definition] Definition §28.5: Genus $2$ Surface (Double Torus)
> The **double torus** $\Sigma_2$ is the surface obtained by taking two copies of the torus and gluing them together along a small disk removed from each. Equivalently, it is the “figure-eight-shaped” surface with two holes.

^def-28-5

> [!remark]- Connections
> - The same construction in 250 (two tori joined by a tube), with Euler characteristic −2: [[§25 Surfaces and the Euler Characteristic#^ex-25-4|250 Ex. §25.4]].

> [!theorem] Theorem §28.5: $\pi_1(\Sigma_2)$ is Non-Abelian
> The fundamental group of the genus $2$ surface is not abelian.

^thm-28-5

> [!proof]+ Proof
> The proof chains three results:
>
> **Step 1: The figure eight is a [[§26 Deformation Retracts and Homotopy Type#^def-26-1|retract]] of $\Sigma_2$.** The retraction $r: \Sigma_2 \to X$ is constructed in two stages:
>
> *Stage (a): Collapse the connecting neck to a point.* The double torus $\Sigma_2$ consists of two torus-shaped handles joined by a connecting tube. Collapse this tube to a single point $x_0$. The result is two tori sharing the single point $x_0$ (a wedge $T^2 \vee T^2$).
>
> *Stage (b): Collapse each torus to a circle.* Each torus retracts onto a meridian circle (one of its generating loops). Applying this to each torus independently (fixing $x_0$ throughout), we collapse $T^2 \vee T^2$ to $S^1 \vee S^1$ — the figure eight.
>
> The composition of these two collapses gives a retraction $r: \Sigma_2 \to S^1 \vee S^1 = X$ with $r|_X = \operatorname{id}_X$ (the two circles are fixed throughout).
>
> **Step 2: Retraction gives an injective homomorphism.** Since $X$ is a retract of $\Sigma_2$, the inclusion $j: X \hookrightarrow \Sigma_2$ satisfies $r \circ j = \operatorname{id}_X$, so $r_* \circ j_* = \operatorname{id}$ on $\pi_1(X)$. In particular, $j_*: \pi_1(X, x_0) \to \pi_1(\Sigma_2, x_0)$ is injective (§26, retraction $\Rightarrow$ $j_*$ injective ([[§26 Deformation Retracts and Homotopy Type#^prop-26-3|§26.3]])).
>
> **Step 3: Apply the subgroup machinery.** By the proposition “[[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|Injective Homomorphisms Preserve Subgroup Structure]]” (§21): since $j_*$ is injective, $j_*(\pi_1(X))$ is a subgroup of $\pi_1(\Sigma_2)$ isomorphic to $\pi_1(X)$. Since $\pi_1(X)$ is non-abelian ([[§28 Fundamental Group of Some Surfaces#^thm-28-4|proved above]]), $j_*(\pi_1(X))$ is a non-abelian subgroup of $\pi_1(\Sigma_2)$. By the [[§21 Algebra Prerequisites꞉ Groups#^prop-21-2|contrapositive proposition]] (§21): a group containing a non-abelian subgroup is itself non-abelian. Therefore $\pi_1(\Sigma_2)$ is non-abelian.
>
> **Important caveat:** This proof shows $\pi_1(\Sigma_2)$ is non-abelian, but does NOT compute $\pi_1(\Sigma_2)$ exactly. The retraction is *not* a [[§26 Deformation Retracts and Homotopy Type#^def-26-3|deformation retract]] — $\pi_1(\Sigma_2)$ is strictly larger than $F_2$ (it has 4 generators with one relation, [[§29 The Seifert–van Kampen Theorem#^ex-29-8|computable via van Kampen]]). The retraction only gives a “lower bound” on complexity.

^pf-28-5

*Uses:* [[§26 Deformation Retracts and Homotopy Type#^prop-26-3|§26.3]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-9|§21.9]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-2|§21.2]], [[§28 Fundamental Group of Some Surfaces#^thm-28-4|§28.4]], [[§26 Deformation Retracts and Homotopy Type#^def-26-1|Def. §26.1]]

![[m590-28-5.svg]]
*The figure eight $X$ (red) inside $\Sigma_2$: one circle around each hole, meeting at $x_0$ on the neck (dashed). The retraction $r$ collapses the neck to $x_0$ and then each torus onto its red circle, keeping $X$ fixed. This is why $j_*$ is injective and $r_*$ is surjective.*

> [!proof]+ Alternative Proof (via surjection)
> We use $r_*$ instead of $j_*$, applying the surjective direction.
>
> **Step 1:** Same as above: $r: \Sigma_2 \to X$ is a retraction onto the figure eight.
>
> **Step 2: Retraction gives a surjective homomorphism.** Since $r \circ j = \operatorname{id}_X$, we have $r_* \circ j_* = \operatorname{id}$ on $\pi_1(X)$. In particular, $r_*: \pi_1(\Sigma_2) \to \pi_1(X)$ is [[§26 Deformation Retracts and Homotopy Type#^prop-26-3|surjective]] (it has a right inverse $j_*$: every element of $\pi_1(X)$ is hit, since $r_*(j_*([f])) = [f]$).
>
> **Step 3: Contradiction.** Suppose $\pi_1(\Sigma_2)$ is abelian. By the proposition “[[§21 Algebra Prerequisites꞉ Groups#^prop-21-10|Surjective Homomorphisms Preserve Abelianness]]” (§21): since $r_*$ is surjective and $\pi_1(\Sigma_2)$ is abelian, $\operatorname{im}(r_*) = \pi_1(X)$ is abelian. But $\pi_1(X)$ is non-abelian ([[§28 Fundamental Group of Some Surfaces#^thm-28-4|§28.4]]). Contradiction.

^pf-28-5-2

*Uses:* [[§26 Deformation Retracts and Homotopy Type#^prop-26-3|§26.3]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-10|§21.10]], [[§28 Fundamental Group of Some Surfaces#^thm-28-4|§28.4]]

> [!remark]- Connections
> - First stated in $\pi_1(\Sigma_2)$ is Non-Abelian ([[§26 Deformation Retracts and Homotopy Type#^ex-26-1|Ex. §26.1]]) (§26); the “up/down” transfer principle behind both proofs is [[§26 Deformation Retracts and Homotopy Type#^cor-26-4|What Properties Transfer via Retraction]].
> - Exact group: [[§29 The Seifert–van Kampen Theorem#^ex-29-8|Surface Fundamental Groups]].

> [!remark] Remark: Comparing the Two Proofs
> Both proofs use the same retraction $r: \Sigma_2 \to X$ with inclusion $j: X \hookrightarrow \Sigma_2$, but exploit different directions:
>
> | | **[[§28 Fundamental Group of Some Surfaces#^pf-28-5\|Proof 1 (injection)]]** | **[[§28 Fundamental Group of Some Surfaces#^pf-28-5-2\|Proof 2 (surjection)]]** |
> |---|---|---|
> | Uses | $j_*: \pi_1(X) \hookrightarrow \pi_1(\Sigma_2)$ | $r_*: \pi_1(\Sigma_2) \twoheadrightarrow \pi_1(X)$ |
> | Logic | Non-abelian subgroup embeds, so the ambient group is non-abelian | Abelian group can only surject onto abelian groups; $\pi_1(X)$ is non-abelian, contradiction |
> | Style | Direct (constructs the non-commuting pair) | Contradiction |

^rem-28-5

## Distinguishing Surfaces via $\pi_1$

> [!theorem] Corollary §28.6: Four Topologically Distinct Surfaces
> The sphere $S^2$, the torus $S^1 \times S^1$, the projective plane $P^2$, and the double torus $\Sigma_2$ are pairwise non-homeomorphic.

^cor-28-6

> [!proof]+ Proof
> Their fundamental groups are all different:
>
> | **Surface** | $\pi_1$ | **Property** |
> |---|---|---|
> | $S^2$ | $0$ ([[Sⁿ is Simply Connected for n ≥ 2\|§27.3]]) | Trivial |
> | $P^2$ | $\mathbb{Z}/2\mathbb{Z}$ ([[§28 Fundamental Group of Some Surfaces#^thm-28-2\|§28.2]]) | Finite, order $2$ |
> | $S^1 \times S^1$ | $\mathbb{Z} \times \mathbb{Z}$ ([[§23 The Fundamental Group#^cor-23-8\|§23.8]]) | Infinite, abelian |
> | $\Sigma_2$ | [[§28 Fundamental Group of Some Surfaces#^thm-28-5\|non-abelian]] | Infinite, non-abelian |
>
> Since [[§23 The Fundamental Group#^cor-23-6|homeomorphic spaces have isomorphic fundamental groups]] (§23), and no two of these groups are isomorphic (they differ in the properties listed: trivial vs. finite vs. infinite abelian vs. non-abelian), the four surfaces are pairwise non-homeomorphic.

^pf-28-6

*Uses:* [[Sⁿ is Simply Connected for n ≥ 2|§27.3]], [[§28 Fundamental Group of Some Surfaces#^thm-28-2|§28.2]], [[§23 The Fundamental Group#^cor-23-8|§23.8]], [[§28 Fundamental Group of Some Surfaces#^thm-28-5|§28.5]], [[§23 The Fundamental Group#^cor-23-6|§23.6]]

> [!remark] Remark
> This is the payoff of the entire course: purely algebraic invariants ($\pi_1$) distinguish geometric objects (surfaces). Each computation used different tools:
> - $\pi_1(S^2) = 0$: [[§27 The Fundamental Group of Sⁿ#^thm-27-1|generation theorem]] + stereographic projection ([[Sⁿ is Simply Connected for n ≥ 2|§27]]).
> - $\pi_1(P^2) \cong \mathbb{Z}/2\mathbb{Z}$: covering space with simply connected cover ([[§28 Fundamental Group of Some Surfaces#^thm-28-2|§28]]).
> - $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$: [[§23 The Fundamental Group#^thm-23-7|product formula]] (§23) + $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]) via [[§24 Covering Spaces#^def-24-7|lifting correspondence]] ([[§24 Covering Spaces|§24]]).
> - $\pi_1(\Sigma_2)$ non-abelian: retract of figure eight + covering space lifting argument ([[§28 Fundamental Group of Some Surfaces#^thm-28-5|§28]]).

^rem-28-6

> [!remark]- Connections
> - In 250 the Euler characteristics 2, 0, 1, −2 also tell these four surfaces apart ([[§25 Surfaces and the Euler Characteristic#^ex-25-1|250 Ex. §25.1]], [[§25 Surfaces and the Euler Characteristic#^ex-25-3|250 Ex. §25.3]], [[§25 Surfaces and the Euler Characteristic#^thm-25-7|250 Thm. §25.7]], [[§25 Surfaces and the Euler Characteristic#^ex-25-4|250 Ex. §25.4]]), but the invariance of the Euler characteristic, [[§25 Surfaces and the Euler Characteristic#^thm-25-2|250 Thm. §25.2]], is taken on trust there ([[§25 Surfaces and the Euler Characteristic#^rem-25-1|250 Remark §25.1]] (what is taken on trust)).
