---
type: section
subject: "[[Topology]]"
chapter: 4
section: 14
munkres: "§24"
tags: [topology, math590]
---
← [[Topology §13 Connected Spaces]] · ↑ [[Topology — 4 Connectedness]] · [[Topology §15 Compact Spaces]] →

## Least Upper Bound Property and Linear Continuum

> [!definition] Definition §14.1: Least Upper Bound Property
> An [[Topology §3 Order Topology#^def-3-1|ordered set]] $A$ has the **least upper bound property** (l.u.b. property) if every nonempty $A_0 \subseteq A$ that is bounded above has a least upper bound (called $\sup$) in $A$.

^def-14-1

> [!remark]- Connections
> - For $\mathbb{R}$ this is the [[Completeness Axiom]] of MATH 451.

> [!example] Example §14.1
> $\mathbb{R}$ has the l.u.b. property, so does $(0, 1)$.

^ex-14-1

> [!example] Example §14.2
> $A = (0, 1) \cup (1, 2)$ does not have the l.u.b. property. (Take $A_0 = (0, 1)$.)

^ex-14-2

> [!example] Example §14.3
> $\mathbb{Q}$ does not have the l.u.b. property. (Take $A_0 = \{q \in \mathbb{Q} \mid q < \sqrt{2}\}$.)

^ex-14-3

> [!definition] Definition §14.2: Linear Continuum
> A [[Topology §3 Order Topology#^def-3-1|simply ordered set]] $L$ having more than one element is called a **linear continuum** if:
>
> 1. $L$ has the l.u.b. property.
> 2. If $x < y$, there exists $z$ such that $x < z < y$.

^def-14-2

> [!remark] Remark: Why Linear Continua are Connected
> The two conditions capture what makes $\mathbb{R}$ “continuous” (no gaps):
>
> **Condition 1 (l.u.b. property):** Prevents “jumps”—bounded sets have suprema, so there are no holes where a limit should be.
>
> **Condition 2 (density):** Prevents “gaps”—between any two points, there's another point, so the space is “filled in.”
>
> **Together:** Any attempt to separate $L$ into two open pieces fails. If you try to cut at a point $c$, the l.u.b. property forces $c$ to belong to one side, and density forces that side to “leak” past $c$ into the other.
>
> **Key consequence:** Connected subsets of a linear continuum are exactly the convex subsets (intervals and rays). This is why [[Topology §14 Connected Subspaces of ℝ#^thm-14-3|IVT]] works: [[Continuous Image of a Connected Space is Connected|continuous images of connected sets are connected]], hence intervals.

^rem-14-1

> [!example] Example §14.4
> $\mathbb{R}$ is a linear continuum. $\mathbb{Z}$ is not (fails condition 2).

^ex-14-4

## Connectedness of Linear Continua

> [!theorem] Theorem §14.1: Linear Continuum is Connected
> If $L$ is a linear continuum, with [[Topology §3 Order Topology#^def-3-4|order topology]] on it, $L$ is connected, so are the intervals and rays in $L$.

^thm-14-1

> [!theorem] Corollary §14.2
> $\mathbb{R}$ is connected, so are intervals in $\mathbb{R}$. (Convex: $\forall a, b \in Y$, $[a, b] \subseteq Y$.)

^cor-14-2

> [!proof]+ Proof of Theorem
> We'll prove: if $Y$ is a convex subspace of $L$, then $Y$ is connected.
>
> Suppose $Y = A \cup B$ is a separation of $Y$. Choose $a \in A$, $b \in B$, without loss of generality $a < b$. $Y$ convex $\Rightarrow [a, b] \subseteq Y = A \cup B$.
>
> Let $A_0 = [a, b] \cap A$ and $B_0 = [a, b] \cap B$, $a \in A_0$, $b \in B_0$. $A_0, B_0$ open in $[a, b]$ (subspace topology $=$ order topology). $\Rightarrow$ $A_0, B_0$ form a separation of $[a, b]$. (Since $A_0, B_0$ disjoint, nonempty, open, $A_0 \cup B_0 = [a, b]$.)
>
> Let $c = \sup A_0$. ($c$ exists since $[a, b]$ is a linear continuum and $A_0$ has an upper bound $b \in [a, b]$.)
>
> We have $c \in [a, b]$, but we'll show $c \notin A_0$ and $c \notin B_0$, a contradiction.
>
> **Case 1:** Suppose $c \in B_0$, $c \neq a$. So either $c = b$ or $a < c < b$. $c \in B_0 \subseteq$ open in $[a, b]$ $\Rightarrow$ $(d, c] \subseteq B_0$ for some $d$. If $c = b$, then $d$ is a smaller upper bound on $A_0$ than $c$ (but $c = \sup A_0$, contradiction). If $a < c < b$, then $(c, b] \cap A_0 = \emptyset$ since $c = \sup A_0$. So $(d, b] = (d, c] \cup (c, b] \subseteq B_0$. Again, $d$ is a smaller upper bound of $A_0$ than $c$. Contradiction.
>
> **Case 2:** Suppose $c \in A_0$. Then $c = a$ or $a < c < b$. $c \in A_0 \subseteq$ open in $[a, b]$ $\Rightarrow$ $[c, e) \subseteq A_0$ for some $e$.
>
> By (2) of [[Topology §14 Connected Subspaces of ℝ#^def-14-2|linear continuum]], there exists $z \in L$ such that $c < z < e$, then $z \in A_0$. Contradicts $c = \sup A_0$ (since $z > c$ and $z \in A_0$, so $c$ is not an upper bound of $A_0$).
>
> **Remark:** We're proving a stronger claim: convexity $\Rightarrow$ connected. Note that linear continuum $\Rightarrow$ convex subspaces are exactly the intervals and rays. Check.

^pf-14-1

*Uses:* [[Topology §14 Connected Subspaces of ℝ#^def-14-2|Def. §14.2]]

## Intermediate Value Theorem

> [!theorem] Theorem §14.3: Intermediate Value Theorem
> Let $f: X \to Y$ be a continuous map, $X$ is connected, $Y$ has order topology. If $a, b \in X$, and $f(a) < r < f(b)$ for some $r \in Y$, then there exists $c \in X$ such that $f(c) = r$.

^thm-14-3

> [!remark]- Connections
> - MATH 451 version on $[a,b]$: [[Intermediate Value Theorem]] ([[Single Variable Analysis §18 Properties of Continuous Functions#^thm-18-3|Theorem §18.3]]).

> [!remark] Remark: IVT: The Power of Connectedness
> The Intermediate Value Theorem is connectedness in action:
>
> **The key insight:** A continuous function “preserves connectedness.” Since $X$ is connected, $f(X)$ must be connected ([[Continuous Image of a Connected Space is Connected|Theorem §13.3]]). In an ordered space, connected subsets are intervals—so $f(X)$ contains all values between $f(a)$ and $f(b)$.
>
> **Why IVT fails without connectedness:** If $X = [0,1] \cup [2,3]$, define $f(x) = 0$ on $[0,1]$ and $f(x) = 2$ on $[2,3]$. Then $f$ is continuous, $0, 2 \in f(X)$, but $1 \notin f(X)$.
>
> **Applications:**
>
> - *Root finding:* If $f(a) < 0 < f(b)$, then $f$ has a root in $(a,b)$.
> - *Fixed points:* If $f: [0,1] \to [0,1]$ is continuous, then $f$ has a fixed point (apply IVT to $g(x) = f(x) - x$).

^rem-14-2

> [!remark]- Connections
> - The fixed-point application is MATH 451's [[Single Variable Analysis §18 Properties of Continuous Functions#^thm-18-6|Theorem §18.6: Fixed Point Theorem on an Interval]]; its two-dimensional version is Brouwer Fixed Point Theorem for $B^2$ ([[Brouwer Fixed Point Theorem|§26.7]]).

> [!example] Example §14.5
> $f: [a, b] \to \mathbb{R}$, continuous, satisfies [[Topology §14 Connected Subspaces of ℝ#^thm-14-3|IVT]].

^ex-14-5

> [!proof]+ Proof
> If no $c \in X$ such that $f(c) = r$, then $f(X) = A \cup B$, where $A = f(X) \cap (-\infty, r)$, $B = (r, +\infty) \cap f(X)$.
>
> $A, B$ disjoint, nonempty ($(f(a) \in A$, $f(b) \in B$). $A, B$ open in $f(X)$ $\Rightarrow$ $f(X)$ has separation $A, B$.
>
> But image of connected $X$ under a continuous $f$ is connected ([[Continuous Image of a Connected Space is Connected|§13.3]]). Contradiction.

^pf-14-3

*Uses:* [[Continuous Image of a Connected Space is Connected|§13.3]]

![[m590-14-2.svg]]
*IVT via connectedness, drawn for $X = [a,b]$: $f(a) < r < f(b)$. If $r$ were not a value of $f$, the image $f(X)$ (right) would split at $r$ into $A = f(X) \cap (-\infty, r)$ (blue) and $B = f(X) \cap (r, \infty)$ (red), a separation of the connected set $f(X)$. So $r$ is hit, possibly several times (red dots), and $c$ is any one of them.*

## Path-Connectedness

> [!definition] Definition §14.3: Path and Path-Connected
> Given $x, y \in X$, a **path** from $x$ to $y$ is a continuous map $f: [a, b] \to X$ such that $f(a) = x$, $f(b) = y$.
>
> A space $X$ is **path-connected** if every pair of points in $X$ can be joined by a path in $X$.

^def-14-3

> [!remark]- Connections
> - MATH 451 version (metric spaces): [[Single Variable Analysis §22 More on Metric Spaces꞉ Connectedness#^def-22-1|Definition §22.1: Path-Connected]].
> - Paths on $[0,1]$ become the objects of homotopy theory: [[Topology §22 Homotopy of Paths#^def-22-3|Definition §22.3: Path]].

> [!remark] Remark: Path-Connectedness vs Connectedness
> Path-connectedness is a more intuitive notion: you can “walk” between any two points. But it's strictly stronger than connectedness.
>
> **1. Path-connected $\Rightarrow$ connected, but not conversely.**
> The [[Topology §14 Connected Subspaces of ℝ#^ex-14-7|topologist's sine curve (below)]] is connected but not path-connected—you can't draw a continuous path from the $y$-axis to the oscillating part.
>
> **2. For “nice” spaces, they coincide.** Open subsets of $\mathbb{R}^n$, manifolds, and CW complexes are connected iff path-connected. The distinction only matters for pathological spaces.
>
> **3. Path-connectedness is easier to verify.** To show path-connectedness, construct explicit paths. To show connectedness, you must rule out *all* possible separations—often harder.
>
> **4. Both are topological invariants.** Homeomorphisms preserve both properties, making them useful for distinguishing spaces.

^rem-14-3

> [!example] Example §14.6
> Unit ball in $\mathbb{R}^n$ is path-connected. $\mathbb{R}^n \setminus \{0\}$, $n > 1$, is path-connected.

^ex-14-6

> [!theorem] Theorem §14.4: Path-Connected Implies Connected
> Path-connected $\Rightarrow$ connected.

^thm-14-4

> [!proof]+ Proof
> Let $X$ be path-connected.
>
> If $X$ were not connected, then there exists $X = A \cup B$ separation of $X$. Let $x \in A$, $y \in B$, and let $f: [a, b] \to X$ be a path from $x$ to $y$.
>
> $f([a, b])$ is connected (since [[Topology §14 Connected Subspaces of ℝ#^cor-14-2|$[a, b]$ connected]] and $f$ continuous ([[Continuous Image of a Connected Space is Connected|§13.3]])). [[Topology §13 Connected Spaces#^lem-13-4|$f([a, b]) \subseteq A$ or $f([a, b]) \subseteq B$]]. Contradiction, since $f(a) = x \in A$ and $f(b) = y \in B$.

^pf-14-4

*Uses:* [[Topology §14 Connected Subspaces of ℝ#^cor-14-2|§14.2]], [[Continuous Image of a Connected Space is Connected|§13.3]], [[Topology §13 Connected Spaces#^lem-13-4|§13.4]]

> [!remark] Remark
> The converse is not true in general: there exist connected spaces that are not path-connected (e.g., the [[Topology §14 Connected Subspaces of ℝ#^ex-14-7|topologist's sine curve]]).

^rem-14-4

> [!example] Example §14.7: Topologist's Sine Curve
> $S \subseteq \mathbb{R}^2$, $S = \{(x, \sin(\frac{1}{x})) \mid 0 < x \leq 1\}$.
>
> $S$ is the image of $(0, 1]$ under a continuous map. $S$ is connected.
>
> $\Rightarrow$ closure $\overline{S}$ of $S$ is connected. $\overline{S} = S \cup \{0\} \times [-1, 1]$. $\overline{S}$ is not path-connected.
>
> This shows: connected $\not\Rightarrow$ path-connected. (Proof in Munkres.)

^ex-14-7

![[m590-14-1.svg]]
*The topologist's sine curve. $S$ (blue) is a continuous image of $(0,1]$, so it is connected. As $x \to 0^+$ it oscillates ever faster between $\pm1$ and accumulates on the whole segment $\{0\} \times [-1,1]$ (red), so $\overline{S} = S \cup \{0\} \times [-1,1]$ is connected. No path can travel from the red segment into $S$: it would have to pass through infinitely many oscillations of height $2$ in a finite parameter interval, which is incompatible with continuity.*

> [!theorem] Theorem §14.5: Product of Path-Connected Spaces
> If $X$ and $Y$ are path-connected, then $X \times Y$ is path-connected.

^thm-14-5

> [!proof]+ Proof
> Let $(x_1, y_1), (x_2, y_2) \in X \times Y$. Since $X$ is path-connected, there exists a path $f: I \to X$ from $x_1$ to $x_2$. Since $Y$ is path-connected, there exists a path $g: I \to Y$ from $y_1$ to $y_2$. Define $F: I \to X \times Y$ by $F(t) = (f(t), g(t))$. Then:
>
> - $F$ is continuous (its coordinate functions $f$ and $g$ are both continuous ([[Topology §10 Product Topology on Arbitrary Products#^thm-10-1|§10.1]])).
> - $F(0) = (f(0), g(0)) = (x_1, y_1)$.
> - $F(1) = (f(1), g(1)) = (x_2, y_2)$.
>
> So $F$ is a path from $(x_1, y_1)$ to $(x_2, y_2)$.

^pf-14-5

*Uses:* [[Topology §10 Product Topology on Arbitrary Products#^thm-10-1|§10.1]]

> [!remark] Remark
> Combined with the earlier result that finite products of connected spaces are connected ([[Topology §13 Connected Spaces#^thm-13-6|§13.6]]), we now have: finite products preserve both connectedness and path-connectedness. In particular, $S^1 \times S^1$ (the torus) is path-connected since $S^1$ is path-connected.

^rem-14-5
