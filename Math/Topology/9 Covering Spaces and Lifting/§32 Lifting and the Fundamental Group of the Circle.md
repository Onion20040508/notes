---
type: section
subject: "[[Topology]]"
chapter: 9
section: 32
munkres: "§53"
tags: [topology, math590]
---
← [[§31 Covering Spaces]] · ↑ [[· 9 Covering Spaces and Lifting]] · [[§33 The Fundamental Theorem of Algebra]] →

*Lifting paths and homotopies through a [[§31 Covering Spaces#^def-31-2|covering map]], the lifting correspondence, and its payoff: $\pi_1(S^1) \cong \mathbb{Z}$.*

## Liftings

> [!definition] Definition §32.1: Lift
> Let $p: E \to B$ be a map. If $f: X \to B$ is continuous, a **lift** of $f$ is a continuous map $\tilde{f}: X \to E$ such that $p \circ \tilde{f} = f$:
>
> $$\begin{array}{ccc}
> & & E \\
> & \overset{\tilde{f}}{\nearrow} & \downarrow\, p \\
> X & \xrightarrow{\;f\;} & B
> \end{array}$$
>
> That is, $\tilde{f}$ “lifts” $f$ from the base $B$ up to the covering space $E$, and projecting back down via $p$ recovers $f$.

^def-32-1

> [!remark] Remark: Reading the Diagram
> The diagram says: instead of going directly from $X$ to $B$ via $f$ (the bottom arrow), you can go from $X$ up to $E$ via $\tilde{f}$ (the diagonal arrow), then project down to $B$ via $p$ (the vertical arrow). The triangle **commutes**: both paths give the same result, i.e., $p \circ \tilde{f} = f$.
>
> The lift $\tilde{f}$ is not guaranteed to exist in general—its existence is the content of the [[Path Lifting Lemma|path lifting lemma]] (for paths) and [[Homotopy Lifting Lemma|homotopy lifting lemma]] (for homotopies). When it does exist, uniqueness (given a starting point) is the key property that makes the [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|lifting correspondence]] well-defined.

^rem-32-4

> [!remark] Remark: Role of Each Map
> In the lifting triangle $X \xrightarrow{\tilde{f}} E \xrightarrow{p} B$:
> - **$f: X \to B$ — the input.** The map you want to study. It lives in the base space $B$, where the topology may be complicated.
> - **$p: E \to B$ — the bridge.** The covering map connects the simple covering space $E$ to the complicated base $B$. It is fixed once and for all. Its structure (evenly covered neighborhoods, slices, fibers) is what makes lifting possible.
> - **$\tilde{f}: X \to E$ — the output.** The lift “decompresses” $f$ into $E$, where the topology is simpler. It is uniquely determined by $f$ and the starting point $\tilde{f}(x_0) = e_0$.
>
> Reading $p \circ \tilde{f} = f$: apply $\tilde{f}$ to go up to $E$, then $p$ to project back down to $B$, recovering $f$. The lift decompresses and $p$ compresses, but they are not literal inverses since $p$ is not injective.
>
> **Why must $E$ be a covering space of $B$?** An arbitrary surjection $p: E \to B$ would not suffice. The covering structure provides three things:
> - **Local invertibility.** Each evenly covered $U \subseteq B$ has slices $V_\alpha$ with $p|_{V_\alpha}: V_\alpha \to U$ a homeomorphism. So $p$ has local inverses $(p|_{V_\alpha})^{-1}$: given a point in $U$, you can canonically lift it to any chosen slice. An arbitrary map has no such local inverses.
> - **Discrete choice $\Rightarrow$ uniqueness.** The slices are *disjoint* open sets — $p^{-1}(U)$ looks like separate, non-overlapping copies of $U$ stacked above $B$. This is the essential property. If two slices $V_\alpha$ and $V_\beta$ overlapped, a continuous lift could “branch” at a point in the overlap — there would be two valid local inverses and no way to choose between them, destroying uniqueness. With disjoint slices, once the lift starts in $V_\alpha$ (fixed by the choice $\tilde{f}(x_0) = e_0$), continuity forces it to stay there: [[§15 Connected Spaces#^lem-15-4|the image of a connected set in a disjoint union must lie in a single component]]. The lift cannot jump across the gap between slices.
>
>   This is what drives the entire machinery:
>
>   $$\text{disjoint slices} \;\Rightarrow\; \text{unique lift} \;\Rightarrow\; \text{endpoint well-defined} \;\Rightarrow\; \text{can distinguish homotopy classes.}$$
>
>   Without disjointness, the endpoint $\tilde{f}(1)$ would depend on choices made during the lift, not just on $f$ and $e_0$ — and the lifting correspondence, which converts topological questions into arithmetic, would collapse.
> - **Local to global via compactness.** Each small piece of a path maps into some evenly covered $U$, where the local inverse lifts it. The [[Lebesgue Number Lemma|Lebesgue number lemma]] (using compactness of $I$) guarantees finitely many pieces suffice, and the [[Pasting Lemma|pasting lemma]] glues them into a global lift.
>
> In short, the covering structure turns “$p$ is locally invertible” into “$f$ can be lifted globally and uniquely.”

^rem-32-5

> [!remark] Remark: Connection to Quotient Maps (§13)
> The lifting triangle has the same shape as the [[Universal Property of Quotient Maps|quotient map universal property]], but with the arrows through $p$ reversed:
>
> **Quotient maps:** Given $p: X \to X/{\sim}$ and $f: X \to Z$ constant on fibers, there is a unique $\bar{f}: X/{\sim} \to Z$ with $f = \bar{f} \circ p$:
>
> $$X \xrightarrow{\;p\;} X/{\sim} \xrightarrow{\;\bar{f}\;} Z$$
>
> Direction: factor *downward* through $p$—compress $f$ through the quotient.
>
> **Covering maps:** Given $p: E \to B$ and $f: X \to B$, there is a unique $\tilde{f}: X \to E$ with $f = p \circ \tilde{f}$:
>
> $$X \xrightarrow{\;\tilde{f}\;} E \xrightarrow{\;p\;} B$$
>
> Direction: lift *upward* through $p$—decompress $f$ into the covering space.
>
> In both cases, $p$ is the bridge, there is an existence and uniqueness statement for the induced map, and a condition must be satisfied (constant on fibers for quotients, choice of starting point for lifts). This common pattern—a special map $p$ with a unique factorization property—is called a **universal property** in mathematics.

^rem-32-6

> [!example] Example §32.1: Lifting Loops on $S^1$ to Paths in $\mathbb{R}$
> Here the general framework specializes to: $B = S^1$ (complicated base), $E = \mathbb{R}$ (simple covering space), $p(x) = (\cos 2\pi x, \sin 2\pi x)$ (the bridge), $b_0 = (1,0)$, $e_0 = 0$.
>
> The fiber is $p^{-1}(b_0) = \mathbb{Z}$: infinitely many points in $\mathbb{R}$ sit above $(1,0)$, one per winding.
>
> **Lifting in action.** Each loop $f$ in $S^1$ (input) lifts to a path $\tilde{f}$ in $\mathbb{R}$ (output):
> - **Winding twice:** $f(s) = (\cos 4\pi s, \sin 4\pi s)$. Lift: $\tilde{f}(s) = 2s$, path from $0$ to $2$.
> - **Winding three times:** $g(s) = (\cos 6\pi s, \sin 6\pi s)$. Lift: $\tilde{g}(s) = 3s$, path from $0$ to $3$.
> - **Winding once clockwise:** $h(s) = (\cos(-2\pi s), \sin(-2\pi s))$. Lift: $\tilde{h}(s) = -s$, path from $0$ to $-1$.
> - **Constant loop:** $e_{b_0}(s) = (1, 0)$. Lift: $\tilde{e}(s) = 0$, constant path. Endpoint: $0$.
>
> In each case, the loop in $S^1$ *closes* ($f(0) = f(1) = b_0$), but the lifted path in $\mathbb{R}$ typically does *not* close—it ends at an integer recording the net winding.
>
> **Where the covering structure is used.** Consider the loop $f(s) = (\cos 4\pi s, \sin 4\pi s)$ concretely:
> - **Local invertibility:** On the right half-circle $U = \{x_1 > 0\}$, the slice $V_0 = (-1/4, 1/4)$ gives a local inverse $(p|_{V_0})^{-1}$, which lifts the initial part of $f$ near $s = 0$ to a path starting at $0$ in $\mathbb{R}$.
> - **Discrete choice:** As $\tilde{f}$ reaches the boundary of $V_0$, it enters the next slice (say $V_1 = (3/4, 5/4)$) and continues. The disjointness of slices means there is no ambiguity about which slice to enter—continuity forces the choice.
> - **Local to global:** The [[Lebesgue Number Lemma|Lebesgue number lemma]] subdivides $[0, 1]$ into finitely many pieces, each mapping into an evenly covered set. The [[Pasting Lemma|pasting lemma]] glues the local lifts into $\tilde{f}(s) = 2s$ on all of $[0, 1]$.

^ex-32-1

> [!remark] Remark: Why Lifting is Powerful
> **Concrete example: four loops on $S^1$.** Consider $p: \mathbb{R} \to S^1$, $e_0 = 0$, $b_0 = (1,0)$. The fiber is $p^{-1}(b_0) = \mathbb{Z}$ — infinitely many “floors” above the same point. Four loops in $S^1$, all starting and ending at $(1,0)$:
> - *Wind once counterclockwise.* In $S^1$: leaves $(1,0)$, returns to $(1,0)$ — looks like nothing happened. Lift: starts at $0$, walks to $1$. Changed floors. **Endpoint: $1$.**
> - *Wind twice counterclockwise.* In $S^1$: same as above. Lift: starts at $0$, walks to $2$. Passed floor $1$, kept going. **Endpoint: $2$.**
> - *Wind once clockwise.* In $S^1$: same again. Lift: starts at $0$, walks to $-1$. Went downstairs. **Endpoint: $-1$.**
> - *Constant loop (sit still).* Lift: starts at $0$, stays at $0$. **Endpoint: $0$.**
>
> In $S^1$, all four are indistinguishable at the endpoint level. In $\mathbb{R}$, the copies of $b_0$ (the integers) separate them: each loop ends at a different floor, and the floor number *is* the winding number.
>
> **Distinguishing loops.** Are $f$ (winding twice) and $g$ (winding three times) homotopic? Without lifts, you would need to prove that no homotopy $F: I \times I \to S^1$ exists—ruling out *every* possible continuous map from the square into the circle. With lifts, compute $\tilde{f}(1) = 2$ and $\tilde{g}(1) = 3$. Since $2 \neq 3$, the loops are not homotopic. The covering space converts an impossible analytic question into a trivial arithmetic check.
>
> **Identifying loops.** Consider a “wiggly” loop $f'$ that wobbles erratically but winds twice overall. Its lift $\tilde{f'}$ is a wiggly path in $\mathbb{R}$ that goes up and down, but ends at $2$. Since $\tilde{f}(1) = \tilde{f'}(1) = 2$ and $\mathbb{R}$ is [[§29 The Fundamental Group#^ex-29-1|simply connected]], the lifts are [[§29 The Fundamental Group#^lem-29-1|path-homotopic]] (every loop in $\mathbb{R}$ contracts). Projecting via $p$ gives $f \simeq_p f'$ in $S^1$. The wobbles are irrelevant—only the net winding matters.
>
> **The general principle.** The covering map decompresses $S^1$ into $\mathbb{R}$, where the topology is trivial. The fiber $p^{-1}(b_0) = \mathbb{Z}$ is a scoreboard: each integer records a distinct homotopy class, and the lift is the mechanism that reads off the score. This is why $\pi_1(S^1) \cong \mathbb{Z}$—the group structure of winding numbers is the group structure of the integers.

^rem-32-7

![[m590-24-5.svg]]
*The lifts from Example §32.1 and the remark above, drawn as graphs $s \mapsto \tilde f(s) \in \mathbb{R}$. Every lift starts at $0$ and ends at an integer, which is a point of the fiber $p^{-1}(b_0) = \mathbb{Z}$, and that endpoint is the winding number. The wiggly lift $\tilde{f'}$ (red) wanders up and down but ends at $2$, just like $\tilde f(s) = 2s$ (blue), so $f \simeq_p f'$. Since $\tilde g$ ends at $3$, $g \not\simeq_p f$.*

## Path Lifting

> [!theorem] Lemma §32.1: Path Lifting Lemma
> Let $p: E \to B$ be a covering map and $p(e_0) = b_0$. For any path $f: [0,1] \to B$ beginning at $b_0$, there exists a **unique** lift $\tilde{f}: [0,1] \to E$ beginning at $e_0$ (i.e., $\tilde{f}(0) = e_0$ and $p \circ \tilde{f} = f$).

^lem-32-1

> [!proof]+ Proof
> **Existence.** Cover $B$ by open sets $\{U_i\}$ each evenly covered by $p$. The collection $\{f^{-1}(U_i)\}$ is an open cover of $[0, 1]$, which is a compact metric space. By the **Lebesgue number lemma** ([[Lebesgue Number Lemma|Lemma §19.2]], [[§19 Limit Point Compactness|§19]]), there exists $\delta > 0$ such that every subset of $[0,1]$ with diameter $< \delta$ lies in some $f^{-1}(U_i)$.
>
> Subdivide $[0, 1]$ into intervals $[s_0, s_1], [s_1, s_2], \ldots, [s_{n-1}, s_n]$ with each $|s_{i+1} - s_i| < \delta$. Then each $f([s_i, s_{i+1}])$ lies in some evenly covered open set $U_i$.
>
> Define $\tilde{f}$ inductively. Set $\tilde{f}(0) = e_0$. Suppose $\tilde{f}(s)$ is defined for all $0 \leq s \leq s_i$. We extend to $[s_i, s_{i+1}]$:
>
> Since $f([s_i, s_{i+1}]) \subseteq U$ for some evenly covered $U$, we have $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$ with $p|_{V_\alpha}: V_\alpha \to U$ a homeomorphism. The point $\tilde{f}(s_i) \in p^{-1}(f(s_i)) \subseteq p^{-1}(U)$ lies in exactly one slice, say $V_0$. Define:
>
> $$\tilde{f}(s) = (p|_{V_0})^{-1}(f(s)) \quad \text{for all } s \in [s_i, s_{i+1}].$$
>
> Since $p|_{V_0}$ is a homeomorphism, $\tilde{f}$ is continuous on $[s_i, s_{i+1}]$, and $p \circ \tilde{f} = f$ on this interval. At $s = s_i$: $(p|_{V_0})^{-1}(f(s_i)) = \tilde{f}(s_i)$ (since $\tilde{f}(s_i) \in V_0$ and $p(\tilde{f}(s_i)) = f(s_i)$), so $\tilde{f}$ agrees with the previous piece.
>
> By induction, $\tilde{f}: [0,1] \to E$ is defined, continuous ([[Pasting Lemma|pasting lemma]] on finitely many closed intervals), and satisfies $p \circ \tilde{f} = f$.
>
> **Uniqueness.** Suppose $\tilde{g}$ is another lift of $f$ with $\tilde{g}(0) = e_0$. We show $\tilde{f} = \tilde{g}$ on each $[s_i, s_{i+1}]$ by induction.
>
> At $s = 0$: $\tilde{f}(0) = e_0 = \tilde{g}(0)$. Suppose $\tilde{f}(s_i) = \tilde{g}(s_i)$. Both $\tilde{f}$ and $\tilde{g}$ map $[s_i, s_{i+1}]$ into $p^{-1}(U)= \bigsqcup_\alpha V_\alpha$. Since $\tilde{g}([s_i, s_{i+1}])$ is connected ([[Continuous Image of a Connected Space is Connected|continuous image]] of an [[§16 Connected Subspaces of ℝ#^cor-16-2|interval]]) and the $V_\alpha$'s are disjoint open sets, $\tilde{g}([s_i, s_{i+1}])$ lies entirely in one slice. Since $\tilde{g}(s_i) = \tilde{f}(s_i) \in V_0$, we have $\tilde{g}([s_i, s_{i+1}]) \subseteq V_0$.
>
> Now $\tilde{g}(s) \in V_0$ and $p(\tilde{g}(s)) = f(s)$, so $\tilde{g}(s) = (p|_{V_0})^{-1}(f(s)) = \tilde{f}(s)$ for all $s \in [s_i, s_{i+1}]$. By induction, $\tilde{f} = \tilde{g}$.

^pf-32-1

*Uses:* [[§18 Compact Spaces#^thm-18-10|§18.10]], [[Lebesgue Number Lemma|§19.2]], [[Pasting Lemma|§10.5]], [[Continuous Image of a Connected Space is Connected|§15.3]], [[§16 Connected Subspaces of ℝ#^cor-16-2|§16.2]], [[§15 Connected Spaces#^lem-15-4|§15.4]]

> [!remark]- Connections
> - Computational version: [[§93 Argument Principle#^lem-93-1|342 Lemma §93.1]] (a continuous argument along a contour, the lift of a loop in ℂ ∖ {0} through θ ↦ eⁱᶿ, given by an integral of w′/w).

> [!remark] Remark: What the Lift Is
> Concretely, the lift $\tilde{f}: I \to E$ is a **path in the covering space** $E$ that sits above $f$: at every time $s$, the lifted point $\tilde{f}(s)$ lies in the fiber $p^{-1}(f(s))$ above $f(s)$. The path $f$ in $B$ tells you *where* to go; the covering structure of $p$ tells you *how to go there upstairs*.
>
> Two key features distinguish $\tilde{f}$ from $f$:
> - **A loop may lift to a non-loop.** If $f$ is a loop ($f(0) = f(1) = b_0$), the lift $\tilde{f}$ starts at $e_0$ but may end at a *different* point in the fiber $p^{-1}(b_0)$. For example, the loop winding once around $S^1$ lifts to the path from $0$ to $1$ in $\mathbb{R}$ — which is not a loop.
> - **The endpoint records information.** The endpoint $\tilde{f}(1) \in p^{-1}(b_0)$ depends only on the homotopy class of $f$ (by the [[Homotopy Lifting Lemma|homotopy lifting lemma]] below). If $E$ is simply connected, different homotopy classes land at different points in the fiber.

^rem-32-8

## Homotopy Lifting

> [!theorem] Lemma §32.2: Homotopy Lifting Lemma
> Let $p: E \to B$ be a covering map with $p(e_0) = b_0$. Let $F: I \times I \to B$ be continuous with $F(0, 0) = b_0$. Then there exists a unique lift $\tilde{F}: I \times I \to E$ with $\tilde{F}(0, 0) = e_0$ and $p \circ \tilde{F} = F$.
>
> Moreover, if $F$ is a path homotopy (i.e., $F(0, t) = b_0$ and $F(1, t) = b_1$ for all $t$), then $\tilde{F}$ is also a path homotopy.

^lem-32-2

> [!proof]+ Proof
> The proof follows the same strategy as the [[Path Lifting Lemma|path lifting lemma]], extended from $I$ to $I \times I$.
>
> **Subdivision.** $I \times I$ is a compact metric space. Cover $B$ by evenly covered open sets $\{U_i\}$. The collection $\{F^{-1}(U_i)\}$ is an open cover of $I \times I$. By the Lebesgue number lemma ([[Lebesgue Number Lemma|Lemma §19.2]]), there exists $\delta > 0$ such that every subset of $I \times I$ with diameter $< \delta$ lies in some $F^{-1}(U_i)$.
>
> Subdivide $I \times I$ into small rectangles $I_i \times J_j = [s_{i-1}, s_i] \times [t_{j-1}, t_j]$ with diameter $< \delta$, so each $F(I_i \times J_j)$ lies in some evenly covered open set.
>
> **Step 1: Define $\tilde{F}$ on $0 \times I$ and $I \times 0$.** By the path lifting lemma, lift the paths $F|_{0 \times I}$ and $F|_{I \times 0}$ starting at $e_0$.
>
> **Step 2: Inductive extension.** Suppose $\tilde{F}$ is defined on the set $A = (0 \times I) \cup (I \times 0) \cup \text{all previously completed rectangles}$, and we extend to $I_i \times J_j$.
>
> Since $F(I_i \times J_j) \subseteq U$ for some evenly covered $U$, we have $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$ with $p|_{V_\alpha}: V_\alpha \to U$ a homeomorphism. The set $C = A \cap (I_i \times J_j)$ is connected (it is the “left and bottom edges” of the rectangle), and $\tilde{F}$ is already defined on $C$.
>
> Since $\tilde{F}(C)$ is connected and lies in $p^{-1}(U) = \bigsqcup_\alpha V_\alpha$ (disjoint open), it lies entirely in one slice $V_0$. Let $p_0 = p|_{V_0}: V_0 \to U$ (a homeomorphism). Define:
>
> $$\tilde{F}(x) = p_0^{-1}(F(x)) \quad \text{for all } x \in I_i \times J_j.$$
>
> This extends $\tilde{F}$ continuously, agreeing with the previous definition on $C$.
>
> **Uniqueness:** Same argument as for path lifting—connectedness of each rectangle forces the lift into a single slice.
>
> **Path homotopy preservation:** If $F(0, t) = b_0$ for all $t$, then $\tilde{F}(0, t)$ is a lift of the constant path at $b_0$ starting at $e_0$. By uniqueness of path lifting, $\tilde{F}(0, t) = e_0$ for all $t$. Similarly, $\tilde{F}(1, t)$ is a lift of the constant path at $b_1$, so $\tilde{F}(1, t) = e_1$ (constant) for all $t$. Thus $\tilde{F}$ is a path homotopy.

^pf-32-2

*Uses:* [[Path Lifting Lemma|§32.1]], [[Lebesgue Number Lemma|§19.2]], [[Continuous Image of a Connected Space is Connected|§15.3]], [[§15 Connected Spaces#^lem-15-4|§15.4]], [[Pasting Lemma|§10.5]]

![[m590-24-6.svg]]
*The order of construction in the homotopy lifting lemma. First lift the left edge $0 \times I$ and the bottom edge $I \times 0$ by path lifting (blue). Then fill in the small rectangles one at a time, in the numbered order. When the turn of $I_i \times J_j$ comes (red), $\tilde F$ is already defined on $C$, the rectangle's left and bottom edges. Since $C$ is connected, $\tilde F(C)$ lies in a single slice $V_0$, and $p_0^{-1} \circ F$ extends $\tilde F$ over the rectangle.*

> [!theorem] Theorem §32.3: Lifts of Path-Homotopic Paths
> Let $p: E \to B$ be a covering map with $p(e_0) = b_0$. Let $f, g$ be paths in $B$ from $b_0$ to $b_1$, and let $\tilde{f}, \tilde{g}$ be their lifts starting at $e_0$. If $f \simeq_p g$, then $\tilde{f}$ and $\tilde{g}$ end at the same point and $\tilde{f} \simeq_p \tilde{g}$.

^thm-32-3

> [!proof]+ Proof
> Let $F: I \times I \to B$ be a path homotopy from $f$ to $g$. By the [[Homotopy Lifting Lemma|homotopy lifting lemma]], there exists a unique lift $\tilde{F}: I \times I \to E$ with $\tilde{F}(0, 0) = e_0$. Since $F$ is a path homotopy, so is $\tilde{F}$:
> - $\tilde{F}(0, t) = e_0$ for all $t$ (constant at $e_0$).
> - $\tilde{F}(1, t) = e_1$ for all $t$ (constant at some $e_1 \in p^{-1}(b_1)$).
>
> Now $\tilde{F}|_{I \times 0}$ is a path in $E$ starting at $e_0$ that lifts $F|_{I \times 0} = f$. By [[Path Lifting Lemma|uniqueness of path lifting]], $\tilde{F}|_{I \times 0} = \tilde{f}$. Similarly, $\tilde{F}|_{I \times 1} = \tilde{g}$.
>
> So $\tilde{F}$ is a path homotopy from $\tilde{f}$ to $\tilde{g}$, both ending at the same point $e_1 = \tilde{f}(1) = \tilde{g}(1)$.

^pf-32-3

*Uses:* [[Homotopy Lifting Lemma|§32.2]], [[Path Lifting Lemma|§32.1]]

## The Lifting Correspondence

> [!definition] Definition §32.2: Lifting Correspondence
> Let $p: E \to B$ be a covering map, $b_0 \in B$, and $e_0 \in E$ with $p(e_0) = b_0$. Define the map (of sets):
>
> $$\phi = \phi_{e_0}: \pi_1(B, b_0) \to p^{-1}(b_0), \qquad \phi([f]) = \tilde{f}(1),$$
>
> where $\tilde{f}$ is the unique lift of $f$ beginning at $e_0$. This is called the **lifting correspondence**.

^def-32-2

> [!remark] Remark: Well-Definedness
> $\phi$ is well-defined: if $[f] = [g]$, i.e., $f \simeq_p g$, then by the theorem on [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-3|lifts of path-homotopic paths]], $\tilde{f}(1) = \tilde{g}(1)$. So $\phi([f])$ depends only on the homotopy class, not the representative.

^rem-32-9

> [!remark] Remark: The Contrapositive is the Real Tool
> The [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-3|theorem]] says: $f \simeq_p g \Rightarrow \tilde{f}(1) = \tilde{g}(1)$. The contrapositive is:
>
> $$\tilde{f}(1) \neq \tilde{g}(1) \quad \Longrightarrow \quad f \not\simeq_p g.$$
>
> **Different endpoints $\Rightarrow$ not homotopic.** This is how covering spaces actually detect topology: to show two loops are not homotopic, lift them and check whether their endpoints differ. This converts an impossible analytic question (“prove no homotopy $F: I \times I \to B$ exists”) into a trivial check (“do the lifted paths end at different points?”).

^rem-32-10

> [!remark] Remark: Why the Endpoint is Constant: Discreteness
> In the proof that $\tilde{f}(1) = \tilde{g}(1)$, the key step is: the function $t \mapsto \tilde{F}(1, t)$ traces the endpoints of the lifted paths as you deform $f$ into $g$. This function is:
> - **Continuous** (because $\tilde{F}$ is continuous).
> - **Maps into the fiber** $p^{-1}(b_1)$ (because $F(1,t) = b_1$ for all $t$, since $F$ is a path homotopy).
> - **The fiber is discrete** (disjoint copies; [[§31 Covering Spaces#^prop-31-1|Proposition §31.1(3)]]).
>
> A continuous map from $[0,1]$ (connected) to a discrete space must be constant. So the endpoint cannot change during the deformation: $\tilde{f}(1) = \tilde{F}(1, 0) = \tilde{F}(1, 1) = \tilde{g}(1)$.
>
> This is the “discrete choice” principle in action: disjoint copies $\Rightarrow$ the lift can't jump between copies $\Rightarrow$ the endpoint is locked in place.

^rem-32-11

*Chain: earlier in [[§25 The Lower Limit Topology, ℝ^ω and Discrete Subspaces|Chapter 6]] · [[Discrete and indiscrete topologies|all appearances]]*

> [!theorem] Theorem §32.4: Properties of the Lifting Correspondence
> Let $p: E \to B$ be a covering map with $p(e_0) = b_0$.
> 1. If $E$ is [[§16 Connected Subspaces of ℝ#^def-16-4|path-connected]], then $\phi: \pi_1(B, b_0) \to p^{-1}(b_0)$ is surjective.
> 2. If $E$ is [[§29 The Fundamental Group#^def-29-3|simply connected]], then $\phi$ is bijective.

^thm-32-4

> [!proof]+ Proof
> **(1) Surjectivity (assuming $E$ path-connected).** Given $e_1 \in p^{-1}(b_0)$, since $E$ is path-connected, there exists a path $\tilde{f}$ in $E$ from $e_0$ to $e_1$. Then $f = p \circ \tilde{f}$ is a loop in $B$ based at $b_0$ (since $p(\tilde{f}(0)) = p(e_0) = b_0$ and $p(\tilde{f}(1)) = p(e_1) = b_0$). So $\phi([f]) = \tilde{f}(1) = e_1$.
>
> **(2) Injectivity (assuming $E$ simply connected).** Suppose $\phi([f]) = \phi([g])$, i.e., $\tilde{f}(1) = \tilde{g}(1)$. Let $[f], [g] \in \pi_1(B, b_0)$ with lifts $\tilde{f}, \tilde{g}$ starting at $e_0$.
>
> Since $\tilde{f}(1) = \tilde{g}(1)$, the concatenation $\tilde{f} * \bar{\tilde{g}}$ is a loop in $E$ based at $e_0$. Since $E$ is simply connected, $[\tilde{f} * \bar{\tilde{g}}] = [e_{e_0}]$, so $[\tilde{f}] = [\tilde{g}]$.
>
> Then $\tilde{f} \simeq_p \tilde{g}$ via some path homotopy $\tilde{F}$. Projecting: $f = p \circ \tilde{f} \simeq_p p \circ \tilde{g} = g$ via the path homotopy $p \circ \tilde{F}$. So $[f] = [g]$.

^pf-32-4

*Uses:* [[Path Lifting Lemma|§32.1]], [[§29 The Fundamental Group#^def-29-3|Def. §29.3]], [[§29 The Fundamental Group#^lem-29-1|§29.1]], [[Properties of Path Concatenation|§28.6]]

> [!remark]- Connections
> - Used in Quantum Field Theory: the double cover $SU(2) \to SO(3)$, with $SU(2) \cong S^3$ simply connected, so that the lifting correspondence is a bijection onto the two-point fiber $\{\pm\mathbb 1\}$ and $\pi_1(SO(3)) \cong \mathbb Z_2$ — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|QFT Theorem §C3.1.8]]; the same for the double cover $SL(2, \mathbb C) \to SO^+(1,3)$ — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|QFT Theorem §C5a.4.7]].

> [!remark] Remark: Why This Matters
> This [[Properties of the Lifting Correspondence|theorem]] is the engine of the entire computation $\pi_1(S^1) \cong \mathbb{Z}$. It says: **to compute $\pi_1(B)$, find a covering space $E$ that is simply connected.** Then the lifting correspondence is a bijection $\pi_1(B) \leftrightarrow p^{-1}(b_0)$, and you read off $\pi_1(B)$ by identifying the fiber. For $p: \mathbb{R} \to S^1$: $\mathbb{R}$ is simply connected, the fiber is $\mathbb{Z}$, so $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§32.5]]). For $p: S^n \to P^n$: $S^n$ is [[Sⁿ is Simply Connected for n ≥ 2|simply connected]] ($n \geq 2$), the fiber has $2$ points, so $|\pi_1(P^n)| = 2$ ([[§38 Fundamental Group of Some Surfaces#^thm-38-3|Theorem §38.3]]).

^rem-32-12

## The Fundamental Group of $S^1$

> [!theorem] Theorem §32.5: $\pi_1(S^1) \cong \mathbb{Z}$
> The fundamental group of $S^1$ is isomorphic to $(\mathbb{Z}, +)$.

^thm-32-5

> [!proof]+ Proof
> **Strategy.** We need an explicit bijective homomorphism $\phi: \pi_1(S^1, b_0) \to \mathbb{Z}$. The [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|lifting correspondence]] provides it: $\phi([f]) = \tilde{f}(1)$ (send each homotopy class to the endpoint of its lifted path). We must verify three things: (1) the codomain is $\mathbb{Z}$, (2) $\phi$ is a bijection, (3) $\phi$ is a homomorphism.
>
> Use the [[§31 Covering Spaces#^thm-31-2|covering map]] $p: \mathbb{R} \to S^1$, $p(x) = (\cos 2\pi x, \sin 2\pi x)$, with $e_0 = 0$ and $b_0 = (1, 0)$.
>
> **Step 1: Identify the codomain.** The lifting correspondence maps $\pi_1(S^1, b_0) \to p^{-1}(b_0)$. We compute the fiber:
>
> $$p^{-1}(b_0) = \{x \in \mathbb{R} \mid (\cos 2\pi x, \sin 2\pi x) = (1,0)\} = \{x \in \mathbb{R} \mid x \in \mathbb{Z}\} = \mathbb{Z}.$$
>
> So the lifting correspondence is $\phi: \pi_1(S^1, b_0) \to \mathbb{Z}$. Each integer represents a potential winding number.
>
> **Step 2: $\phi$ is a bijection.** This follows from properties of $\mathbb{R}$ (the covering space), not $S^1$:
> - **Surjective** (every integer is hit): $\mathbb{R}$ is path-connected, so for any $n \in \mathbb{Z}$, there is a path in $\mathbb{R}$ from $0$ to $n$. Projecting via $p$ gives a loop in $S^1$ with $\phi([f]) = n$.
> - **Injective** (different classes hit different integers): $\mathbb{R}$ is simply connected (convex $\Rightarrow$ every loop contracts via [[§28 Homotopy of Paths#^thm-28-1|straight-line homotopy]]). If $\phi([f]) = \phi([g])$, then $\tilde{f}(1) = \tilde{g}(1)$, so $\tilde{f} \ast  \bar{\tilde{g}}$ is a loop in $\mathbb{R}$ which must contract, and projecting the homotopy gives $f \simeq_p g$.
>
> Alternatively, this entire step is a direct application of the [[Properties of the Lifting Correspondence|Lifting Correspondence Properties theorem]]: $\mathbb{R}$ is path-connected and simply connected, so $\phi$ is bijective. The argument above is just that theorem applied to $p: \mathbb{R} \to S^1$.
>
> At this point, $\phi$ is a bijection of sets: $\pi_1(S^1, b_0)$ and $\mathbb{Z}$ have the same cardinality. But a bijection of sets is not an isomorphism of groups—we need $\phi$ to respect the operations.
>
> **Step 3: $\phi$ is a group homomorphism.** We must show $\phi([f] \ast  [g]) = \phi([f]) + \phi([g])$, i.e., the lift of $f \ast  g$ starting at $0$ ends at $\tilde{f}(1) + \tilde{g}(1)$. This is the only step that uses the specific geometry of $p: \mathbb{R} \to S^1$ (Steps 1–2 used only the general covering space theory).
>
> Let $\tilde{f}$ be the lift of $f$ starting at $0$, with $\tilde{f}(1) = m \in \mathbb{Z}$. Let $\tilde{g}$ be the lift of $g$ starting at $0$, with $\tilde{g}(1) = n \in \mathbb{Z}$.
>
> The key question: the lift of $f \ast  g$ follows $\tilde{f}$ on the first half, arriving at $m$. Then it must lift $g$ *starting from $m$*, not from $0$. The lift of $g$ starting at $m$ is $\tilde{g}(s) + m$—a translated copy. This works because $p$ has period $1$: $p(x + m) = p(x)$ for any integer $m$.
>
> Formally, define $\widetilde{f * g}: I \to \mathbb{R}$ by:
>
> $$\widetilde{f * g}(s) = \begin{cases} \tilde{f}(2s) & s \in [0, 1/2] \\ \tilde{g}(2s - 1) + m & s \in [1/2, 1]. \end{cases}$$
>
> **This is a valid lift:**
> - **Starts at $0$:** $\widetilde{f \ast  g}(0) = \tilde{f}(0) = 0$. ✓
> - **Well-defined at $s = 1/2$:** $\tilde{f}(1) = m$ and $\tilde{g}(0) + m = 0 + m = m$. ✓
> - **Continuous:** By the [[Pasting Lemma|pasting lemma]]. ✓
> - **Projects to $f \ast  g$:** On $[0, 1/2]$: $p(\tilde{f}(2s)) = f(2s) = (f \ast  g)(s)$. On $[1/2, 1]$: $p(\tilde{g}(2s-1) + m) = p(\tilde{g}(2s-1))$ (since $p(x + m) = p(x)$). So $p(\tilde{g}(2s-1) + m) = g(2s-1) = (f \ast  g)(s)$. ✓
>
> **Endpoint:** $\widetilde{f \ast  g}(1) = \tilde{g}(1) + m = n + m$.
>
> By [[Path Lifting Lemma|uniqueness of path lifting]], this is the unique lift of $f * g$ starting at $0$. Therefore:
>
> $$\phi([f] * [g]) = \widetilde{f * g}(1) = m + n = \phi([f]) + \phi([g]).$$
>
> Since $\phi$ is a bijective homomorphism, it is an isomorphism: $\pi_1(S^1, b_0) \cong \mathbb{Z}$.

^pf-32-5

*Uses:* [[§31 Covering Spaces#^thm-31-2|§31.2]], [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|Def. §32.2]], [[§29 The Fundamental Group#^ex-29-1|Ex. §29.1]], [[Properties of the Lifting Correspondence|§32.4]], [[Pasting Lemma|§10.5]], [[Path Lifting Lemma|§32.1]], [[§28 Homotopy of Paths#^thm-28-1|§28.1]]

![[m590-24-7.svg]]
*Step 3 in one picture. The lift of $f \ast  g$ starting at $0$ follows $\tilde f(2s)$ up to $m$ (blue). The lift $\tilde g$ starts at $0$ (dashed), so it cannot be used as it is. Translated up by $m$ it starts where $\tilde f$ stopped (red), and it still lies over $g$ because $p(x + m) = p(x)$. The endpoint is $m + n$, which is why $\phi([f] \ast  [g]) = \phi([f]) + \phi([g])$.*

> [!remark]- Connections
> - Consequences: [[Fundamental Theorem of Algebra (topological proof)|Fundamental Theorem of Algebra]], [[No-Retraction Theorem|No-Retraction Theorem]], Brouwer Fixed Point Theorem for $B^2$ ([[Brouwer Fixed Point Theorem|§34.7]]).
> - Same method for $P^2$: $\pi_1(P^2) \cong \mathbb{Z}/2\mathbb{Z}$ ([[§38 Fundamental Group of Some Surfaces#^thm-38-2|§38.2]]).
> - Computational version: [[§93 Argument Principle#^thm-93-4|342 Thm. §93.4]] (the argument principle computes the winding number of f(C) around 0 as Z − P); no branch of log z is continuous on a circle around 0, which is why branches need a cut, [[§33 Branches and Derivatives of Logarithms#^thm-33-1|342 Thm. §33.1]].

> [!theorem] Theorem §32.6: The Generator of $\pi_1(S^1)$
> Every element of $\pi_1(S^1, b_0)$ can be written uniquely as $[\omega]^k$ for some $k \in \mathbb{Z}$, where $\omega(s) = (\cos 2\pi s, \sin 2\pi s)$ is the standard counterclockwise loop. Here:
> - $[\omega]^k = [\underbrace{\omega * \omega * \cdots * \omega}_{k \text{ times}}]$ for $k > 0$ (wind counterclockwise $k$ times),
> - $[\omega]^{-k} = [\underbrace{\bar{\omega} * \bar{\omega} * \cdots * \bar{\omega}}_{k \text{ times}}]$ for $k > 0$ (wind clockwise $k$ times),
> - $[\omega]^0 = [e_{b_0}]$ (the constant loop).
>
> The isomorphism $\phi: \pi_1(S^1, b_0) \xrightarrow{\;\cong\;} \mathbb{Z}$ sends $[\omega]^k \mapsto k$.

^thm-32-6

> [!proof]+ Proof
> The lift of $\omega$ starting at $0$ is $\tilde{\omega}(s) = s$, which ends at $1$. So $\phi([\omega]) = 1$, i.e., $[\omega]$ corresponds to the generator $1 \in \mathbb{Z}$.
>
> Since $\phi$ is an isomorphism ([[Fundamental Group of the Circle|Theorem above]]) and $\phi([\omega]) = 1$ generates $\mathbb{Z}$, every element of $\pi_1(S^1, b_0)$ is a power of $[\omega]$: given $[f] \in \pi_1(S^1, b_0)$ with $\phi([f]) = k$, we have $\phi([\omega]^k) = k\phi([\omega]) = k = \phi([f])$, so $[f] = [\omega]^k$ by injectivity of $\phi$. Uniqueness follows from the same injectivity.

^pf-32-6

*Uses:* [[Fundamental Group of the Circle|§32.5]], [[§27 Free Groups and Presentations#^def-27-2|Def. §27.2]]

> [!remark] Remark
> Since $S^1$ is path-connected, the [[Basepoint Independence of π₁|basepoint independence theorem]] ([[§29 The Fundamental Group|§29]]) gives $\pi_1(S^1, b_0) \cong \pi_1(S^1, b_1)$ for any two basepoints. So we may write $\pi_1(S^1) \cong \mathbb{Z}$ without specifying the basepoint.

^rem-32-13

> [!remark] Remark: How to Establish or Refute Isomorphisms
> The proof above illustrates the general method. Now that we have the first nontrivial computation, we can state the methodology explicitly.
>
> **To show $G \cong G'$** (isomorphic): construct an explicit bijective homomorphism $f: G \to G'$. In practice:
> - Define $f$ (a candidate map). For fundamental groups, the [[§32 Lifting and the Fundamental Group of the Circle#^def-32-2|lifting correspondence]] $\phi$ or an [[§29 The Fundamental Group#^def-29-4|induced homomorphism]] $h_*$ are the typical candidates.
> - Verify $f$ is a homomorphism: $f(xy) = f(x)f(y)$.
> - Verify $f$ is bijective (either directly, or by constructing a [[§26 Algebra Prerequisites꞉ Groups#^prop-26-4|two-sided inverse]]).
>
> For example, in the proof of $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§32.5]]): the candidate was $\phi([f]) = \tilde{f}(1)$, bijectivity came from properties of $\mathbb{R}$, and the homomorphism property came from the translation trick $p(x + m) = p(x)$.
>
> **To show $G \not\cong G'$** (not isomorphic): find an algebraic property [[§26 Algebra Prerequisites꞉ Groups#^thm-26-6|preserved by isomorphisms]] that $G$ and $G'$ disagree on. Any of the following suffices:
> - Different cardinalities: $|G| \neq |G'|$ (e.g., $\mathbb{Z} \not\cong \{e\}$).
> - One abelian, the other not (e.g., $\mathbb{Z} \not\cong S_3$).
> - One cyclic, the other not (e.g., $\mathbb{Z} \not\cong \mathbb{Z}^2$).
> - Different counts of elements of a given order (e.g., $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$).
>
> You do *not* need to check all possible maps—a single invariant that differs is enough.
>
> **For distinguishing spaces:** Since homeomorphisms induce isomorphisms on $\pi_1$ ([[§29 The Fundamental Group#^cor-29-6|§29.6]]) ([[§29 The Fundamental Group|§29]]):
> - $\pi_1(X) \cong \pi_1(Y)$: use covering spaces (lifting correspondence), [[§35 Deformation Retracts and Homotopy Type#^cor-35-2|deformation retracts]], or [[Functoriality of π₁|functoriality]] to build an isomorphism.
> - $X \not\cong Y$: show $\pi_1(X) \not\cong \pi_1(Y)$ using an algebraic invariant. For instance, $\pi_1(S^1) \cong \mathbb{Z} \not\cong \{e\} \cong \pi_1(\mathbb{R}^2)$ (different cardinalities) gives $S^1 \not\cong \mathbb{R}^2$, and $\pi_1(S^1) \cong \mathbb{Z} \not\cong \mathbb{Z}^2 \cong \pi_1(T^2)$ (cyclic vs. not) gives $S^1 \not\cong T^2$.

^rem-32-14

## Characterizing Nullhomotopic Maps from $S^1$

> [!theorem] Lemma §32.7: Equivalent Conditions for Nullhomotopy
> Let $h: S^1 \to X$ be continuous. The following are equivalent:
> 1. $h$ is [[§28 Homotopy of Paths#^def-28-2|nullhomotopic]].
> 2. $h$ extends to a continuous map $k: B^2 \to X$ (i.e., $k|_{S^1} = h$, where $B^2$ is the closed unit disk).
> 3. $h_*: \pi_1(S^1, b_0) \to \pi_1(X, h(b_0))$ is the trivial homomorphism.

^lem-32-7

> [!proof]+ Proof
> **(1) $\Rightarrow$ (2):** Let $H: S^1 \times I \to X$ be a homotopy between $h$ and a constant map. Define $\pi: S^1 \times I \to B^2$ by $\pi(x, t) = (1-t)x$. Then $\pi$ is continuous, surjective, and closed (continuous map from compact to Hausdorff), hence a quotient map.
>
> Since $H$ is constant on $\pi^{-1}((0,0)) = S^1 \times \{1\}$ (the fiber over the origin), $H$ factors through $\pi$: there is an induced continuous map $k: B^2 \to X$ with $H = k \circ \pi$.
>
> Check: for $x \in S^1 = \partial B^2$, we have $k(x) = k(\pi(x, 0)) = H(x, 0) = h(x)$, so $k|_{S^1} = h$.
>
> **(2) $\Rightarrow$ (3):** If $h = k \circ j$ where $j: S^1 \hookrightarrow B^2$ is the inclusion, then $h_{\ast} = k_{\ast} \circ j_{\ast}$ by [[Functoriality of π₁|functoriality]]. Since $B^2$ is [[§29 The Fundamental Group#^ex-29-2|convex]], $\pi_1(B^2, b_0) = \{e\}$, so $j_{\ast}$ maps everything to the identity. Thus $h_{\ast} = k_{\ast} \circ j_{\ast}$ is trivial.
>
> **(3) $\Rightarrow$ (1):** Let $p: \mathbb{R} \to S^1$ be the [[§31 Covering Spaces#^thm-31-2|standard covering map]]. Let $p_0 = p|_{[0,1]}: I \to S^1$. Then $[p_0]$ is a [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-6|generator]] of $\pi_1(S^1, b_0)$, since $p_0$ is a loop at $b_0 = (1,0)$ whose lift begins at $0$ and ends at $1$.
>
> Let $x_0 = h(b_0)$. By (3), $h_*([p_0]) = [h \circ p_0] = [e_{x_0}] \in \pi_1(X, x_0)$. So there exists a path homotopy $F: I \times I \to X$ between $h \circ p_0$ and $e_{x_0}$.
>
> Now $p_0 \times \operatorname{id}_I: I \times I \to S^1 \times I$ is a quotient map (continuous, surjective, closed). Since $F$ respects the fibers of $p_0 \times \operatorname{id}_I$ (the path homotopy conditions ensure the identifications are consistent), $F$ induces a continuous map $H: S^1 \times I \to X$. This $H$ is a homotopy between $h$ and a constant map.

^pf-32-7

*Uses:* [[Continuous Image of a Compact Space is Compact|§18.3]], [[Compact Subspace of a Hausdorff Space is Closed|§18.4]], [[§13 Quotient Topology#^prop-13-2|§13.2]], [[Universal Property of Quotient Maps|§13.3]], [[Functoriality of π₁|§29.5]], [[§29 The Fundamental Group#^ex-29-2|Ex. §29.2]], [[Fundamental Group of the Circle|§32.5]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-6|§32.6]], [[§31 Covering Spaces#^thm-31-2|§31.2]]

> [!remark] Remark
> This lemma bridges the algebraic and geometric perspectives:
> - **(1) $\Leftrightarrow$ (2):** A loop contracts $\Leftrightarrow$ it bounds a disk. This is the topological intuition.
> - **(1) $\Leftrightarrow$ (3):** A loop contracts $\Leftrightarrow$ its homotopy class is trivial. This is the algebraic formulation.
>
> The direction (3) $\Rightarrow$ (1) is the most subtle: it uses $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§32.5]]) to reduce checking nullhomotopy of $h$ to checking that $h_*$ kills the generator. This lemma will be used to prove the [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem]].

^rem-32-15

> [!remark]- Connections
> - Generalized to $S^n$: [[§34 Retractions and Fixed Points#^lem-34-8|Generalized Nullhomotopy Lemma]].
