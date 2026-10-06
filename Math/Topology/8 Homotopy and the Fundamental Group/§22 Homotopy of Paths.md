---
type: section
subject: "[[Topology]]"
chapter: 8
section: 22
munkres: "§51"
tags: [topology, math590]
---
← [[§21a Free Groups and Presentations]] · ↑ [[· 8 Homotopy and the Fundamental Group]] · [[§23 The Fundamental Group]] →

> [!remark] Remark: Motivation: Continuously Deforming Paths
> The fundamental group will classify loops “up to continuous deformation.” To make this precise, we need to answer: when are two paths “essentially the same”?
>
> A single path $f: I \to X$ uses one parameter $s$ (position along the path). To describe a *deformation* of one path into another, we need a second parameter $t$ (time, tracking how far the deformation has progressed). This leads naturally to a map $F: I \times I \to X$, where:
> - $F(s, t)$ is “the point at position $s$ along the $t$-th path in the family.”
> - Fixing $t$ gives a single path $F(\cdot, t): I \to X$ (one frame of the movie).
> - Fixing $s$ gives a trajectory $F(s, \cdot): I \to X$ (how one point moves over time).
>
> Requiring $F$ to be continuous on $I \times I$ (in the [[§4 Product Topology#^def-4-1|product topology]]) ensures the deformation is smooth in *both* directions simultaneously—nearby $(s, t)$ values give nearby points in $X$, so there are no “jumps” in space or time. The compactness of $I = [0,1]$ is also essential: paths have definite start and end points, deformations have a definite “before” and “after,” and key arguments ([[Lebesgue Number Lemma|Lebesgue number lemma]], [[Pasting Lemma|pasting lemma]]) rely on working with compact domains.

^rem-22-1

Let $I = [0, 1]$.

## Homotopy of Continuous Maps

> [!definition] Definition §22.1: Homotopy
> Let $f, f': X \to Y$ be continuous. We say $f$ is **homotopic** to $f'$ ($f \simeq f'$) if there exists continuous $F: X \times I \to Y$ with $F(x, 0) = f(x)$ and $F(x, 1) = f'(x)$ for all $x$. The map $F$ is a **homotopy**.

^def-22-1

> [!definition] Definition §22.2: Nullhomotopic
> $f: X \to Y$ is **nullhomotopic** if $f \simeq c$ for some constant map $c$.

^def-22-2

> [!remark]- Connections
> - Nullhomotopic maps from $S^1$ are characterized in [[§24a Lifting and the Fundamental Group of the Circle#^lem-24-12|Equivalent Conditions for Nullhomotopy]].

## The Straight-Line Homotopy

> [!theorem] Theorem §22.1: Straight-Line Homotopy
> If $f, g: X \to \mathbb{R}^n$ are continuous maps, then $f \simeq g$ via
>
> $$H(x, t) = (1 - t)\,f(x) + t\,g(x).$$
>
> In particular, every continuous map $f: X \to \mathbb{R}^n$ is nullhomotopic.

^thm-22-1

> [!proof]+ Proof
> $H$ is continuous (sums and scalar products of continuous maps). $H(x, 0) = f(x)$ and $H(x, 1) = g(x)$. For the “in particular,” take $g = c_{y_0}$ (constant).

^pf-22-1

*Uses:* [[§22 Homotopy of Paths#^def-22-1|Def. §22.1]], [[§22 Homotopy of Paths#^def-22-2|Def. §22.2]]

> [!remark] Remark: Why “Straight Line”?
> Fix any $x \in X$. The trajectory $t \mapsto H(x, t) = (1 - t)f(x) + tg(x)$ is a **line segment** in $\mathbb{R}^n$ from $f(x)$ to $g(x)$. The formula $(1-t)a + tb$ is the standard parameterization of the segment from $a$ to $b$: at $t = 0$ you are at $a$, at $t = 1$ you are at $b$, and at $t = 1/2$ you are at the midpoint.

^rem-22-2

![[m590-22-1.svg]]
*The straight-line homotopy from $f$ to $g$ in $\mathbb{R}^n$: each point $f(x)$ slides along the segment to $g(x)$ (red: one trajectory $t \mapsto H(x,t)$, passing $H(x,\tfrac12)$ at the midpoint). The dashed curves are the intermediate maps $H(\cdot,\tfrac13)$ and $H(\cdot,\tfrac23)$. The only thing the construction needs is that every segment stays in the target, which is convexity.*

The straight-line homotopy is the most fundamental construction in homotopy theory. It recurs in three different forms throughout these notes:

1. **Any two maps to $\mathbb{R}^n$ are homotopic** ([[§22 Homotopy of Paths#^thm-22-1|above]]): $H(x, t) = (1-t)f(x) + tg(x)$. Works because $\mathbb{R}^n$ is convex.
2. **Every loop in a convex set contracts** ([[§23 The Fundamental Group#^ex-23-2|Example §23.2]]): Take $g = e_{x_0}$, giving $H(s, t) = (1-t)f(s) + tx_0$. This is a *path* homotopy (not just a homotopy): $H(0, t) = (1-t)x_0 + tx_0 = x_0$ and $H(1, t) = (1-t)x_0 + tx_0 = x_0$, so the endpoints stay fixed.
3. **Reparameterization lemma** ([[§22 Homotopy of Paths#^lem-22-5|Lemma §22.5]]): $H(s, t) = f((1-t)\,p(s) + t\,s)$. Here the straight-line homotopy happens *inside the parameter space* $I = [0,1]$: the convex combination $(1-t)\,p(s) + ts$ continuously blends the reparameterization $p$ into the identity, and $I$ being convex guarantees the blend stays in $[0, 1]$. Then $f$ is applied to the result.

> [!remark] Remark: The Essential Requirement is Convexity
> The formula $(1-t)a + tb$ stays in a space $X$ if and only if $X$ contains all line segments between its points—i.e., $X$ is **convex**. This is why the straight-line homotopy works in $\mathbb{R}^n$, open/closed balls, and $[0,1]$, but **fails** in spaces with holes:
> - In $\mathbb{R}^2 \setminus \{0\}$: a loop around the origin cannot be straight-line-contracted, because the line segments would pass through the missing origin.
> - In $S^1$: the “obvious” contraction $H(s,t) = (1-t)f(s) + t \cdot x_0$ leaves $S^1$ (the blend of two points on the circle passes through the interior).
>
> This failure is exactly what $\pi_1$ detects. [[§23 The Fundamental Group#^def-23-3|Simply connected]] means “the straight-line homotopy argument morally works”—every loop contracts, even if the actual homotopy is not literally a straight line.

^rem-22-3

> [!theorem] Proposition §22.2: Path-Connectedness Implies Homotopy of Constant Maps
> If $Y$ is [[§14 Connected Subspaces of ℝ#^def-14-new1|path-connected]] and $y_0, y_1 \in Y$, then the constant maps $e_{y_0}, e_{y_1}: X \to Y$ are homotopic.

^prop-22-2

> [!proof]+ Proof
> Since $Y$ is path-connected, there exists a path $p: I \to Y$ with $p(0) = y_0$ and $p(1) = y_1$. Define $H: X \times I \to Y$ by
>
> $$H(x, t) = p(t).$$
>
> This is $p$ composed with the projection $\pi_2: X \times I \to I$, hence continuous. Then $H(x, 0) = p(0) = y_0 = e_{y_0}(x)$ and $H(x, 1) = p(1) = y_1 = e_{y_1}(x)$, so $e_{y_0} \simeq e_{y_1}$.

^pf-22-2

*Uses:* [[§14 Connected Subspaces of ℝ#^def-14-new1|Def. §14.3]], [[§9 Continuous Functions#^thm-9-4|§9.4]]

> [!remark] Remark
> The key idea: a path $p: I \to Y$ is defined on $I$, but we need a homotopy defined on $X \times I$. The projection $\pi_2: X \times I \to I$, $(x, t) \mapsto t$, bridges this gap—composing $p \circ \pi_2$ promotes a path in $Y$ to a homotopy between constant maps on any domain $X$. This technique appears whenever path-connectedness needs to be converted into a homotopy statement.

^rem-22-4

## Path Homotopy

> [!definition] Definition §22.3: Path
> A **path** in $X$ is a continuous map $f: I \to X$. The point $f(0) = x_0$ is the **initial point**, $f(1) = x_1$ the **terminal point**.

^def-22-3

> [!remark]- Connections
> - Same notion as in the definition of path-connectedness: [[§14 Connected Subspaces of ℝ#^def-14-3|Path]].

> [!definition] Definition §22.4: Path Homotopy
> Paths $f, f': I \to X$ with the same endpoints ($f(0) = f'(0) = x_0$, $f(1) = f'(1) = x_1$) are **path homotopic** ($f \simeq_p f'$) if there exists continuous $F: I \times I \to X$ with:
> 1. $F(s, 0) = f(s)$, $F(s, 1) = f'(s)$ for all $s$ (interpolates from $f$ to $f'$).
> 2. $F(0, t) = x_0$, $F(1, t) = x_1$ for all $t$ (endpoints fixed).

^def-22-4

> [!remark] Remark: Visualizing Path Homotopy
> $F: I \times I \to X$ maps the unit square into $X$: bottom edge ($t=0$) is $f$, top edge ($t=1$) is $f'$, left edge pinned at $x_0$, right edge pinned at $x_1$. Each horizontal slice is an intermediate path.

^rem-22-5

![[m590-22-2.svg]]
*A path homotopy $F: I \times I \to X$. The bottom edge of the square goes to $f$ and the top edge to $f'$ (blue); the left and right edges are crushed to $x_0$ and $x_1$. Each horizontal slice at height $t$ (red) is an intermediate path $F(\cdot,t)$ from $x_0$ to $x_1$, one frame of the movie; the dashed slices are two more frames.*

## Homotopy is an Equivalence Relation

> [!theorem] Lemma §22.3
> Both $\simeq$ and $\simeq_p$ are [[§22 Partitions and Equivalence Relations#^def-22-3|equivalence relations]].

^lem-22-3

> [!proof]+ Proof
> We prove for $\simeq_p$ (drop endpoint conditions for $\simeq$).
>
> **Reflexivity:** $f \simeq_p f$ via $F(x, t) = f(x)$.
>
> **Symmetry:** If $f \simeq_p f'$ via $F$, then $f' \simeq_p f$ via $G(x, t) = F(x, 1-t)$.
>
> **Transitivity:** If $f \simeq_p f'$ via $F$ and $f' \simeq_p f''$ via $F'$, define:
>
> $$G(x, t) = \begin{cases} F(x, 2t) & t \in [0, 1/2] \\ F'(x, 2t-1) & t \in [1/2, 1]. \end{cases}$$
>
> At $t = 1/2$: $F(x,1) = f'(x) = F'(x,0)$, so $G$ is well-defined and continuous by the [[Pasting Lemma|pasting lemma]].

^pf-22-3

*Uses:* [[Pasting Lemma|§9.5]]

> [!definition] Definition §22.5: Path Homotopy Class
> The [[§22 Partitions and Equivalence Relations#^def-22-4|equivalence class]] of a path $f$ under $\simeq_p$ is denoted $[f]$.

^def-22-5

## Path Concatenation

> [!definition] Definition §22.6: Product of Paths
> Let $f$ be a path from $x_0$ to $x_1$ and $g$ a path from $x_1$ to $x_2$. The **product** $f \ast  g: I \to X$ is:
>
> $$(f * g)(s) = \begin{cases} f(2s) & s \in [0, 1/2] \\ g(2s-1) & s \in [1/2, 1]. \end{cases}$$

^def-22-6

> [!remark] Remark: Well-Definedness
> At $s = 1/2$: $f(1) = x_1 = g(0)$, so both pieces agree. Continuous by the [[Pasting Lemma|pasting lemma]]. The product traverses $f$ then $g$, each at double speed.

^rem-22-6

![[m590-22-3.svg]]
*The product $f \ast  g$: the first half of $I$ runs $f$ at double speed (blue), the second half runs $g$ at double speed (red). The pieces meet at $s = \tfrac12$, where $f(1) = x_1 = g(0)$.*

## Concatenation of Homotopy Classes

> [!definition] Definition §22.7: Product of Homotopy Classes
> Define $[f] * [g] = [f * g]$.

^def-22-7

> [!theorem] Proposition §22.4: Well-Definedness of $[f] * [g]$
> If $f, f' \in [f]$ and $g, g' \in [g]$ (i.e., $f \simeq_p f'$ and $g \simeq_p g'$), then $f * g \simeq_p f' * g'$.

^prop-22-4

> [!proof]+ Proof
> Let $F: I \times I \to X$ be a path homotopy from $f$ to $f'$ (so $F(s,0) = f(s)$, $F(s,1) = f'(s)$, $F(0,t) = x_0$, $F(1,t) = x_1$). Let $G: I \times I \to X$ be a path homotopy from $g$ to $g'$ (so $G(s,0) = g(s)$, $G(s,1) = g'(s)$, $G(0,t) = x_1$, $G(1,t) = x_2$).
>
> Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} F(2s, t) & s \in [0, 1/2] \\ G(2s - 1, t) & s \in [1/2, 1]. \end{cases}$$
>
> **Well-defined at $s = 1/2$:** $F(1, t) = x_1 = G(0, t)$ for all $t$. ✓
>
> **Continuous:** By the [[Pasting Lemma|pasting lemma]] ($[0, 1/2] \times I$ and $[1/2, 1] \times I$ are closed). ✓
>
> **Boundary conditions:**
> - $H(s, 0) = F(2s, 0) = f(2s)$ on $[0, 1/2]$ and $G(2s-1, 0) = g(2s-1)$ on $[1/2, 1]$. This is $(f * g)(s)$. ✓
> - $H(s, 1) = F(2s, 1) = f'(2s)$ on $[0, 1/2]$ and $G(2s-1, 1) = g'(2s-1)$ on $[1/2, 1]$. This is $(f' * g')(s)$. ✓
> - $H(0, t) = F(0, t) = x_0$. ✓
> - $H(1, t) = G(1, t) = x_2$. ✓
>
> So $H$ is a path homotopy from $f * g$ to $f' * g'$.

^pf-22-4

*Uses:* [[Pasting Lemma|§9.5]]

## Reparameterization Lemma

> [!theorem] Lemma §22.5: Reparameterization
> Let $f: I \to X$ be a path and $p: I \to I$ a continuous map with $p(0) = 0$ and $p(1) = 1$. Then $f \circ p \simeq_p f$.

^lem-22-5

> [!proof]+ Proof
> Define $H: I \times I \to X$ by $H(s, t) = f((1 - t)\,p(s) + t\,s)$.
>
> **Well-defined:** For each $(s, t) \in I \times I$, the argument $(1-t)\,p(s) + ts$ is a convex combination of $p(s) \in [0,1]$ and $s \in [0,1]$, hence lies in $[0,1]$.
>
> **Continuous:** $H$ is a composition of continuous maps ($f$, $p$, and affine functions of $s, t$).
>
> **Boundary conditions:**
> - $H(s, 0) = f(p(s)) = (f \circ p)(s)$. ✓
> - $H(s, 1) = f(s)$. ✓
> - $H(0, t) = f((1-t)\,p(0) + t \cdot 0) = f(0) = x_0$. ✓
> - $H(1, t) = f((1-t)\,p(1) + t \cdot 1) = f(1) = x_1$. ✓
>
> So $H$ is a path homotopy from $f \circ p$ to $f$.

^pf-22-5

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]]

> [!remark] Remark
> The composition $f \circ p$ is still a path with the same image as $f$—the “trace” (set of points visited) is unchanged—but we may travel along $f$ at a different speed. The lemma says: *reparameterizing a path does not change its homotopy class*. Only the shape of the path matters, not how fast we traverse it.

^rem-22-7

> [!remark] Remark
> The homotopy $H(s, t) = f((1-t)\,p(s) + ts)$ continuously deforms the reparameterization $p$ into the identity: at $t = 0$ we use $p(s)$, at $t = 1$ we use $s$, and intermediate values blend between them via a [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy]] *inside* $I$.

^rem-22-8

## The Group Properties

The following theorem shows that the product of path homotopy classes satisfies the group axioms. This is the foundation for the [[§23 The Fundamental Group#^def-23-2|fundamental group]].

> [!theorem] Theorem §22.6: Properties of Path Concatenation
> Let $f$, $g$, $h$ be paths in $X$ with compatible endpoints (so $f \ast  g$ and $g \ast  h$ are defined). Let $e_{x}$ denote the constant path at $x$ (i.e., $e_x(s) = x$ for all $s$), and let $\bar{f}(s) = f(1-s)$ (the **reverse path**). Then:
> 1. **Associativity:** $[f] \ast  ([g] \ast  [h]) = ([f] \ast  [g]) \ast  [h]$.
> 2. **Identity:** $[f] \ast  [e_{x_1}] = [f] = [e_{x_0}] \ast  [f]$.
> 3. **Inverse:** $[f] \ast  [\bar{f}] = [e_{x_0}]$ and $[\bar{f}] \ast  [f] = [e_{x_1}]$.

^thm-22-6

> [!remark]- Connections
> - Restricted to loops at $x_0$, these are the group axioms of [[§23 The Fundamental Group#^def-23-2|the fundamental group]] (see [[§23 The Fundamental Group#^rem-23-1|Remark in §23]]).
> - Group axioms: [[§21 Algebra Prerequisites꞉ Groups#^def-21-1|Definition §21.1: Group]].

> [!proof]+ Proof of (1): Associativity
> We must show $(f * g) * h \simeq_p f * (g * h)$. Writing out the definitions explicitly:
>
> $$((f * g) * h)(s) = \begin{cases} f(4s) & s \in [0, 1/4] \\ g(4s - 1) & s \in [1/4, 1/2] \\ h(2s - 1) & s \in [1/2, 1] \end{cases}$$
>
> $$(f * (g * h))(s) = \begin{cases} f(2s) & s \in [0, 1/2] \\ g(4s - 2) & s \in [1/2, 3/4] \\ h(4s - 3) & s \in [3/4, 1] \end{cases}$$
>
> Both traverse $f$, $g$, $h$ in order, but with different speed schedules. Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} f\!\left(\dfrac{4s}{t + 1}\right) & s \in \left[0, \dfrac{t+1}{4}\right] \\[6pt] g(4s - t - 1) & s \in \left[\dfrac{t+1}{4}, \dfrac{t+2}{4}\right] \\[6pt] h\!\left(\dfrac{4s - t - 2}{2 - t}\right) & s \in \left[\dfrac{t+2}{4}, 1\right] \end{cases}$$
>
> **Continuity:** Each piece is a composition of continuous functions. At the junctions $s = (t+1)/4$ and $s = (t+2)/4$, the pieces agree (check by substitution), so $H$ is continuous by the [[Pasting Lemma|pasting lemma]] (the three regions are closed subsets of $I \times I$).
>
> **Boundary conditions:**
> - $t = 0$: the breakpoints are $s = 1/4$ and $s = 1/2$. Then $H(s, 0) = f(4s)$ on $[0, 1/4]$, $g(4s-1)$ on $[1/4, 1/2]$, $h(2s-1)$ on $[1/2, 1]$. This is $(f*g)*h$. ✓
> - $t = 1$: the breakpoints are $s = 1/2$ and $s = 3/4$. Then $H(s, 1) = f(2s)$ on $[0, 1/2]$, $g(4s-2)$ on $[1/2, 3/4]$, $h(4s-3)$ on $[3/4, 1]$. This is $f*(g*h)$. ✓
> - $s = 0$: $H(0, t) = f(0) = x_0$ for all $t$. ✓
> - $s = 1$: $H(1, t) = h\!\left(\frac{4 - t - 2}{2 - t}\right) = h(1) = x_3$ for all $t$. ✓
>
> Thus $H$ is a path homotopy from $(f * g) * h$ to $f * (g * h)$.

^pf-22-6

*Uses:* [[Pasting Lemma|§9.5]]

> [!proof]+ Proof of (2a): Right Identity $[f] * [e_{x_1}] = [f]$
> Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} f\!\left(\dfrac{2s}{1 + t}\right) & s \in \left[0, \dfrac{1+t}{2}\right] \\[6pt] x_1 & s \in \left[\dfrac{1+t}{2}, 1\right] \end{cases}$$
>
> **Continuity:** On the first piece, $H$ is $f$ composed with a continuous function. At the junction $s = (1+t)/2$: the first piece gives $f\!\left(\frac{2 \cdot (1+t)/2}{1+t}\right) = f(1) = x_1$, matching the second piece. Continuous by the [[Pasting Lemma|pasting lemma]].
>
> **Boundary conditions:**
> - $t = 0$: breakpoint at $s = 1/2$. $H(s, 0) = f(2s)$ on $[0, 1/2]$ and $x_1$ on $[1/2, 1]$. This is $f * e_{x_1}$. ✓
> - $t = 1$: breakpoint at $s = 1$. $H(s, 1) = f(s)$ on $[0, 1]$. This is $f$. ✓
> - $s = 0$: $H(0, t) = f(0) = x_0$. ✓
> - $s = 1$: $s = 1 \geq (1+t)/2$ for $t \leq 1$, so $H(1, t) = x_1 = f(1)$. ✓
>
> Thus $f * e_{x_1} \simeq_p f$.

^pf-22-6-2

*Uses:* [[Pasting Lemma|§9.5]]

> [!proof]+ Proof of (2b): Left Identity $[e_{x_0}] * [f] = [f]$
> Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} x_0 & s \in \left[0, \dfrac{1-t}{2}\right] \\[6pt] f\!\left(\dfrac{2s - 1 + t}{1 + t}\right) & s \in \left[\dfrac{1-t}{2}, 1\right] \end{cases}$$
>
> **Continuity:** At $s = (1-t)/2$: the second piece gives $f\!\left(\frac{2 \cdot (1-t)/2 - 1 + t}{1+t}\right) = f(0) = x_0$. [[Pasting Lemma|Pasting lemma]] applies.
>
> **Boundary conditions:**
> - $t = 0$: breakpoint at $s = 1/2$. $H(s, 0) = x_0$ on $[0, 1/2]$ and $f(2s - 1)$ on $[1/2, 1]$. This is $e_{x_0} * f$. ✓
> - $t = 1$: breakpoint at $s = 0$. $H(s, 1) = f(s)$ on $[0, 1]$. This is $f$. ✓
> - $s = 0$: $H(0, t) = x_0$. ✓
> - $s = 1$: $H(1, t) = f\!\left(\frac{2 - 1 + t}{1 + t}\right) = f(1) = x_1$. ✓
>
> Thus $e_{x_0} * f \simeq_p f$.

^pf-22-6-3

*Uses:* [[Pasting Lemma|§9.5]]

> [!proof]+ Proof of (3): Inverse — $f * \bar{f} \simeq_p e_{x_0}$
> Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} f(2s) & s \in [0, (1-t)/2] \\ f(1-t) & s \in [(1-t)/2, (1+t)/2] \\ f(2 - 2s) & s \in [(1+t)/2, 1] \end{cases}$$
>
> **Interpretation:** At time $t$, walk along $f$ up to $f(1-t)$, pause there, then walk back. As $t$ increases, we walk less far before turning around.
>
> **Continuity:** At $s = (1-t)/2$: first piece gives $f(2 \cdot (1-t)/2) = f(1-t)$, matching the second piece. At $s = (1+t)/2$: third piece gives $f(2 - 2 \cdot (1+t)/2) = f(1-t)$, matching the second piece. [[Pasting Lemma|Pasting lemma]] applies (three closed regions).
>
> **Boundary conditions:**
> - $t = 0$: breakpoints at $s = 1/2$ and $s = 1/2$ (middle piece collapses). $H(s, 0) = f(2s)$ on $[0, 1/2]$ and $f(2 - 2s) = \bar{f}(2s - 1)$ on $[1/2, 1]$. This is $f * \bar{f}$. ✓
> - $t = 1$: breakpoints at $s = 0$ and $s = 1$ (middle piece fills the interval). $H(s, 1) = f(0) = x_0$ for all $s$. This is $e_{x_0}$. ✓
> - $s = 0$: $H(0, t) = f(0) = x_0$. ✓
> - $s = 1$: $H(1, t) = f(2 - 2) = f(0) = x_0$. ✓
>
> Thus $f * \bar{f} \simeq_p e_{x_0}$.

^pf-22-6-4

*Uses:* [[Pasting Lemma|§9.5]]

![[m590-22-5.svg]]
*The inverse homotopy $f \ast  \bar f \simeq_p e_{x_0}$. On the square, the slice at height $t$ runs $f(2s)$ out to $f(1-t)$, pauses there across the red triangle, then comes back along $f(2-2s)$. In $X$ (right) that slice traces only the red initial arc of $f$, out to $f(1-t)$ and back. As $t \to 1$ the arc shrinks to $x_0$ and the slice becomes $e_{x_0}$.*

> [!proof]+ Proof of (3): Inverse — $\bar{f} * f \simeq_p e_{x_1}$
> Define $H: I \times I \to X$ by:
>
> $$H(s, t) = \begin{cases} f(1 - 2s) & s \in [0, (1-t)/2] \\ f(t) & s \in [(1-t)/2, (1+t)/2] \\ f(2s - 1) & s \in [(1+t)/2, 1] \end{cases}$$
>
> **Interpretation:** At time $t$, walk backwards along $f$ from $f(1) = x_1$ to $f(t)$, pause at $f(t)$, then walk forward along $f$ from $f(t)$ to $f(1) = x_1$. As $t$ increases, we walk less far before turning around.
>
> **Well-defined at junctions:**
> - At $s = (1-t)/2$: first piece gives $f(1 - 2 \cdot (1-t)/2) = f(t)$, matching the second piece. ✓
> - At $s = (1+t)/2$: third piece gives $f(2 \cdot (1+t)/2 - 1) = f(t)$, matching the second piece. ✓
>
> **Continuous:** By the [[Pasting Lemma|pasting lemma]] (three closed regions of $I \times I$). ✓
>
> **Boundary conditions:**
> - $t = 0$: breakpoints at $s = 1/2$ and $s = 1/2$ (middle piece collapses). $H(s, 0) = f(1-2s)$ on $[0, 1/2]$ and $f(2s-1)$ on $[1/2, 1]$. This is $\bar{f}(2s)$ on $[0,1/2]$ and $f(2s-1)$ on $[1/2,1]$, i.e., $\bar{f} * f$. ✓
> - $t = 1$: breakpoints at $s = 0$ and $s = 1$ (middle piece fills the interval). $H(s, 1) = f(1) = x_1$ for all $s$. This is $e_{x_1}$. ✓
> - $s = 0$: $H(0, t) = f(1) = x_1$. ✓
> - $s = 1$: $H(1, t) = f(2 \cdot 1 - 1) = f(1) = x_1$. ✓
>
> Thus $\bar{f} * f \simeq_p e_{x_1}$.

^pf-22-6-5

*Uses:* [[Pasting Lemma|§9.5]]

> [!remark] Remark: Idea of the Associativity Homotopy
> The homotopy continuously slides the breakpoints: at $t = 0$ the three pieces occupy $[0, 1/4], [1/4, 1/2], [1/2, 1]$ (the left-associated schedule), and at $t = 1$ they occupy $[0, 1/2], [1/2, 3/4], [3/4, 1]$ (the right-associated schedule). Throughout, $g$ always occupies an interval of length $1/4$—only $f$ and $h$ trade time with each other. The arguments inside $f$, $g$, $h$ are chosen so that each function is called on $[0, 1]$ within its piece.

^rem-22-9

![[m590-22-4.svg]]
*The associativity homotopy drawn on its domain $I \times I$. The slice at height $t$ is cut at $s = (t+1)/4$ and $s = (t+2)/4$: it runs $f$ on the left piece, $g$ on the middle (red) and $h$ on the right. The bottom slice is the schedule of $(f\ast g)\ast h$, the top slice that of $f\ast (g\ast h)$. The red band has constant width $\tfrac14$, so only $f$ and $h$ trade time; the left edge stays at $x_0$ and the right edge at $x_3$.*

> [!remark] Remark: What These Properties Mean
> These three properties are exactly the group axioms for the operation $\ast$ on homotopy classes. For general paths (not loops), we don't quite have a group (the product $[f] \ast  [g]$ is only defined when the terminal point of $f$ equals the initial point of $g$—this is a *groupoid*). But if we restrict to **loops at a fixed basepoint $x_0$** (paths with $f(0) = f(1) = x_0$), then all products are defined, and we get a genuine group: the **fundamental group** $\pi_1(X, x_0)$ ([[§23 The Fundamental Group#^def-23-2|Definition §23.2]]).

^rem-22-10

> [!remark] Remark: Classes vs. Paths: Two Levels of Reasoning
> The elements of $\pi_1(X, x_0)$ are **homotopy classes** $[f]$, not paths $f$ themselves. This distinction is essential: the concatenation $f \ast  \bar{f}$ is literally not the constant path $e_{x_0}$ (it goes out and comes back), but the *class* $[f \ast  \bar{f}]$ equals $[e_{x_0}]$ because we proved a homotopy between them.
>
> However, **proofs always happen at the path level**. To show $[f] = [g]$ in $\pi_1$, you must:
> 1. Pick representative paths $f$ and $g$.
> 2. Construct an explicit homotopy $H: I \times I \to X$ between them.
> 3. Verify all boundary conditions.
> 4. Conclude equality of classes.
>
> This is analogous to modular arithmetic: you state “$3 \equiv 7 \pmod{4}$” at the class level but verify it by computing $7 - 3 = 4$ at the representative level.
>
> **Well-definedness is the recurring concern.** Any time you define something on classes using representatives—like $[f] \ast  [g] = [f \ast  g]$ or the [[§23 The Fundamental Group#^def-23-4|induced homomorphism]] $f_{\ast}([g]) = [f \circ g]$—you must check that the result is independent of which representative you chose. This is why [[§22 Homotopy of Paths#^prop-22-4|Proposition §22.4]] (if $f \simeq_p f'$ and $g \simeq_p g'$, then $f \ast  g \simeq_p f' \ast  g'$) was needed before the group properties could even be stated.

^rem-22-11
