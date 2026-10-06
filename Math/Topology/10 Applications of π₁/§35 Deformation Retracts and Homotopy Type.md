---
type: section
subject: "[[Topology]]"
chapter: 10
section: 35
munkres: "§55, §58"
tags: [topology, math590]
---
← [[§34 Retractions and Fixed Points]] · ↑ [[· 10 Applications of π₁]] · [[§36 The Punctured Plane, the Figure Eight and the Torus]] →

*Homotopic maps and induced homomorphisms, retractions, and the no-retraction and Brouwer fixed point theorems come first, in [[§34 Retractions and Fixed Points]].*

## Deformation Retracts

A [[§34 Retractions and Fixed Points#^prop-34-3|retraction]] gives $j_*$ injective and $r_*$ surjective, but not an isomorphism. The extra ingredient needed is a homotopy from $\operatorname{id}_X$ to $j \circ r$ — this upgrades the retraction to a deformation retraction and the injection to a full isomorphism.

> [!definition] Definition §35.1: Deformation Retract
> A subspace $A \subseteq X$ is a **deformation retract** of $X$ if $\operatorname{id}_X: X \to X$ is [[§28 Homotopy of Paths#^def-28-1|homotopic]] to a map that carries all of $X$ into $A$, such that each point of $A$ remains fixed during the homotopy.
>
> That is, there exists a continuous map $H: X \times I \to X$ (called a **deformation retraction**) such that:
> - $H(x, 0) = x$ for all $x \in X$ (starts as identity).
> - $H(x, 1) \in A$ for all $x \in X$ (ends in $A$).
> - $H(a, t) = a$ for all $a \in A$, $t \in I$ ($A$ stays fixed throughout).

^def-35-1

> [!remark] Remark
> The map $r(x) = H(x, 1)$ is a [[§34 Retractions and Fixed Points#^def-34-1|retraction]] of $X$ onto $A$ (check: $r(a) = H(a, 1) = a$ by condition 3). A deformation retract is thus a retract with the additional property that the retraction is homotopic to the identity—this “continuous collapsing over time” is what gives surjectivity of $j_*$.

^rem-35-6

> [!theorem] Theorem §35.1: Deformation Retract Induces Isomorphism on $\pi_1$
> Let $A$ be a deformation retract of $X$, and let $x_0 \in A$. Then the inclusion $j: (A, x_0) \hookrightarrow (X, x_0)$ induces an isomorphism on fundamental groups.

^thm-35-1

> [!remark]- Connections
> - Special case of [[§35 Deformation Retracts and Homotopy Type#^thm-35-5|Homotopy Equivalence Induces Isomorphism on π₁]] (see [[§35 Deformation Retracts and Homotopy Type#^rem-35-12|Deformation Retract as a Special Case]]).

> [!proof]+ Proof
> The argument is the [[§34 Retractions and Fixed Points#^thm-34-2|same]] as for $S^n \hookrightarrow \mathbb{R}^{n+1} \setminus \{0\}$.
>
> Let $r: X \to A$ be the retraction ($r(x) = H(x,1)$) and $j: A \hookrightarrow X$ the inclusion.
>
> **$j_{\ast}$ is injective:** $r \circ j = \operatorname{id}_A$, so $r_{\ast} \circ j_{\ast} = \operatorname{id}$ on $\pi_1(A, x_0)$.
>
> **$j_{\ast}$ is surjective:** $H$ is a homotopy from $\operatorname{id}_X$ to $j \circ r$ that fixes $x_0$ (since $x_0 \in A$ and $H(a, t) = a$ for all $a \in A$). By [[§34 Retractions and Fixed Points#^lem-34-1|the lemma]] (homotopic maps with fixed basepoint induce the same homomorphism), $(j \circ r)_{\ast} = (\operatorname{id}_X)_{\ast} = \operatorname{id}$ on $\pi_1(X, x_0)$. So $j_{\ast} \circ r_{\ast} = \operatorname{id}$, giving surjectivity of $j_{\ast}$.

^pf-35-1

*Uses:* [[§34 Retractions and Fixed Points#^thm-34-2|§34.2]], [[§34 Retractions and Fixed Points#^prop-34-3|§34.3]], [[Functoriality of π₁|§29.5]], [[§34 Retractions and Fixed Points#^lem-34-1|§34.1]]

> [!theorem] Corollary §35.2: Deformation Retracts Have the Same $\pi_1$
> If $A$ is a deformation retract of $X$, then $\pi_1(X, x_0) \cong \pi_1(A, x_0)$ for any $x_0 \in A$.
>
> In practice: to compute $\pi_1(X)$, find a deformation retract $A \subseteq X$ whose $\pi_1$ you already know.

^cor-35-2

*Immediate from [[Deformation Retract Induces Isomorphism on π₁|Theorem §35.1]]: $j_{\ast}$ is an isomorphism.*

*Uses:* [[Deformation Retract Induces Isomorphism on π₁|§35.1]]

> [!remark] Remark: Retraction vs. Deformation Retraction: Summary
> |  | **Retraction** | **Deformation retraction** |
> |---|---|---|
> | Definition | $r \circ j = \operatorname{id}_A$ | Same, plus $H$ from $\operatorname{id}_X$ to $j \circ r$ fixing $A$ |
> | $j_*$ | injective | isomorphism |
> | $r_*$ | surjective | isomorphism |
> | $\pi_1(X)$ vs $\pi_1(A)$ | $\pi_1(A)$ embeds, $\pi_1(X)$ can be bigger | $\pi_1(X) \cong \pi_1(A)$ |
>
> **Exam consequence:** To show $A$ is not a deformation retract of $X$, it suffices to show $\pi_1(X) \not\cong \pi_1(A)$ (easier). To show $A$ is not a retract, you need the stronger argument that $j_{\ast}$ injective with left inverse leads to a contradiction (harder, but catches cases where $\pi_1(X) \cong \pi_1(A)$).

^rem-35-7

## Examples

> [!example] Example §35.1: $\mathbb{R}^3 \setminus \{z\text{-axis}\}$ Deformation Retracts onto $\mathbb{R}^2 \setminus \{0\}$
> Let $X = \mathbb{R}^3 \setminus \{z\text{-axis}\}$. Note $\mathbb{R}^2 \setminus \{0\} \subseteq X$ (as the $z = 0$ plane minus the origin). Define
>
> $$
> H: X \times I \to X, \qquad H(x, y, z, t) = (x, y, z(1-t)).
> $$
>
> This collapses the $z$-coordinate to $0$ while preserving $(x, y) \neq (0,0)$. So $\mathbb{R}^2 \setminus \{0\}$ is a [[§35 Deformation Retracts and Homotopy Type#^def-35-1|deformation retract]] of $X$, and by [[§35 Deformation Retracts and Homotopy Type#^cor-35-2|Corollary §35.2]]
>
> $$
> \pi_1(\mathbb{R}^3 \setminus \{z\text{-axis}\}) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1) \cong \mathbb{Z}.
> $$

^ex-35-1

![[m590-26-11.svg]]
*$H(x,y,z,t) = (x, y, (1-t)z)$ moves every point straight down (red) onto the blue plane $z = 0$; points below the plane rise the same way. Since $(x, y) \neq (0,0)$ never changes, no point ever touches the removed $z$-axis (red, dashed), and in particular none lands on the origin.*

> [!example] Example §35.2: $B^2$ Deformation Retracts onto a Point
> $H: B^2 \times I \to B^2$ defined by $H(x, t) = (1-t)x$. So $\pi_1(B^2) = 0$ (trivial).

^ex-35-2

> [!example] Example §35.3: $\{x \in \mathbb{R}^2 : \|x\| > 1\}$ Deformation Retracts onto $S^1$
> The exterior of the unit disk deformation retracts onto the unit circle via
>
> $$
> H(x, t) = (1-t)x + t\frac{x}{\|x\|}.
> $$
>
> This is the [[§34 Retractions and Fixed Points#^pf-34-2|same formula]] as for $\mathbb{R}^2 \setminus \{0\}$ restricted to $\|x\| > 1$. So $\pi_1(\{x : \|x\| > 1\}) \cong \mathbb{Z}$.

^ex-35-3

> [!example] Example §35.4: Doubly Punctured Plane
> $\mathbb{R}^2 \setminus \{p, q\}$ (two points removed) deformation retracts onto a [[§38 Fundamental Group of Some Surfaces#^def-38-4|figure-eight space]] (wedge of two circles). So $\pi_1(\mathbb{R}^2 \setminus \{p, q\}) \cong F_2$ (the [[§27 Free Groups and Presentations#^def-27-3|free group]] on two generators).

^ex-35-4

> [!example] Example §35.5: Doubly Punctured Plane: Two Deformation Retracts
> The plane with two points removed deformation retracts onto both a figure-eight space and a “theta” space ($\Theta$). However, neither the figure-eight nor the theta space is a deformation retract of the other, but they have isomorphic fundamental groups (both $\cong F_2$).
>
> This illustrates that **isomorphic $\pi_1$ does not imply deformation retract**—the relationship is one-directional.

^ex-35-5

![[m590-26-12.svg]]
*The doubly punctured plane deformation retracts onto the figure eight (left) and onto the theta space (right): points flow away from the punctures $p, q$ and in from far away onto the blue graph. So both graphs have $\pi_1 \cong F_2$ and the same homotopy type as $\mathbb{R}^2 \setminus \{p, q\}$, although neither graph is a deformation retract of the other.*

> [!example] Example §35.6: $S^n$ is a Deformation Retract of $\mathbb{R}^{n+1} \setminus \{0\}$
> Via $H(x,t) = (1-t)x + tx/\|x\|$ (proved in [[§34 Retractions and Fixed Points#^thm-34-2|Theorem §34.2]]). So $\pi_1(\mathbb{R}^{n+1} \setminus \{0\}) \cong \pi_1(S^n)$.
>
> For $n \geq 2$: $\pi_1(S^n) = 0$ ([[Sⁿ is Simply Connected for n ≥ 2|simply connected]]), so $\pi_1(\mathbb{R}^{n+1} \setminus \{0\}) = 0$.
>
> For $n = 1$: $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§32.5]]), so $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$.

^ex-35-6

> [!example] Example §35.7: $\mathbb{R}^2 \setminus \{0\}$ is Not a Deformation Retract of $\mathbb{R}^2$
> If $\mathbb{R}^2 \setminus \{0\}$ were a deformation retract of $\mathbb{R}^2$, then by [[§35 Deformation Retracts and Homotopy Type#^cor-35-2|the corollary]]:
>
> $$
> \pi_1(\mathbb{R}^2) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}).
> $$
>
> But $\pi_1(\mathbb{R}^2) = 0$ ([[§29 The Fundamental Group#^ex-29-2|convex]]) and $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ ([[§35 Deformation Retracts and Homotopy Type#^ex-35-6|deformation retracts]] onto $S^1$). Since $0 \not\cong \mathbb{Z}$, no such deformation retract exists.
>
> **General principle:** To show $A$ is *not* a deformation retract of $X$, show $\pi_1(X) \not\cong \pi_1(A)$. This is $\pi_1$ as an **obstruction**: it doesn't tell you when a deformation retract exists, but it tells you when one *cannot* exist.

^ex-35-7

> [!example] Example §35.8: $T^2 \setminus \{pt\}$ Deformation Retracts onto the Figure Eight
> The punctured torus has $\pi_1(T^2 \setminus \{pt\}) \cong F_2$ (the free group on two generators). The proof combines the quotient map construction ([[§13 Quotient Topology|§13]]) with a deformation retract argument, using the [[Universal Property of Quotient Maps|universal property]] to pass from the square to the torus. We go through this step by step.
>
> **Step 1: Represent the torus as a quotient of the square.**
>
> The torus $T^2 = S^1 \times S^1$ is the [[§13 Quotient Topology#^ex-13-3|quotient of the square]] $[0, 2\pi]^2$ by the equivalence relation that identifies opposite edges:
> - $(0, t) \sim (2\pi, t)$ for all $t$ (left edge $\sim$ right edge),
> - $(s, 0) \sim (s, 2\pi)$ for all $s$ (bottom edge $\sim$ top edge).
>
> The quotient map is $\pi: [0, 2\pi]^2 \to T^2$, defined by $\pi(s, t) = (e^{is}, e^{it})$. This map is:
> - *Continuous:* Composition of continuous functions.
> - *Surjective:* Every $(e^{is}, e^{it}) \in S^1 \times S^1$ is hit.
> - *Quotient map:* $[0, 2\pi]^2$ is compact, $T^2$ is Hausdorff, so $\pi$ is closed, hence a [[§13 Quotient Topology#^prop-13-2|quotient map]].
>
> **Step 2: Identify what the boundary becomes.**
>
> Under $\pi$, the boundary $\partial[0, 2\pi]^2$ maps onto $(S^1 \times \{1\}) \cup (\{1\} \times S^1)$—the **[[§38 Fundamental Group of Some Surfaces#^def-38-4|figure eight]]** in $T^2$. Concretely:
> - All four corners $(0,0), (2\pi, 0), (0, 2\pi), (2\pi, 2\pi)$ map to the single point $(1, 1) \in T^2$ (the basepoint).
> - The top and bottom edges ($t = 0$ and $t = 2\pi$) both map to $S^1 \times \{1\}$ (one circle of the figure eight).
> - The left and right edges ($s = 0$ and $s = 2\pi$) both map to $\{1\} \times S^1$ (the other circle).
>
> **Step 3: Choose the puncture point.**
>
> Let $q = (\pi, \pi)$ be the center of the square, and let $pt = \pi(q) \in T^2$. Since $q$ is in the interior of $[0, 2\pi]^2$, it is the *only* preimage of $pt$ under $\pi$ (the identifications only happen on the boundary). So:
> - $[0, 2\pi]^2 \setminus \{q\}$ is the punctured square (simple, convex minus a point).
> - $T^2 \setminus \{pt\}$ is the punctured torus (what we want to study).
> - $\pi$ restricts to a quotient map $\pi: [0, 2\pi]^2 \setminus \{q\} \to T^2 \setminus \{pt\}$.
>
> **Step 4: Deformation retract on the punctured square.**
>
> On the punctured square $[0, 2\pi]^2 \setminus \{q\}$, we deformation retract onto the boundary $\partial[0, 2\pi]^2$ by “pushing outward from $q$.” For each point $x \neq q$, draw the ray from $q$ through $x$; it hits the boundary at a unique point $r(x)$. Define:
>
> $$
> \tilde{F}: ([0, 2\pi]^2 \setminus \{q\}) \times I \to [0, 2\pi]^2 \setminus \{q\}, \qquad \tilde{F}(x, t) = (1-t)x + t \cdot r(x).
> $$
>
> This is a straight-line homotopy from $x$ toward $r(x)$. Check the deformation retract conditions:
> - $\tilde{F}(x, 0) = x$ for all $x$ (starts as identity). ✓
> - $\tilde{F}(x, 1) = r(x) \in \partial[0, 2\pi]^2$ for all $x$ (ends on boundary). ✓
> - If $x \in \partial[0, 2\pi]^2$: the ray from $q$ through $x$ hits the boundary at $x$ itself, so $r(x) = x$, and $\tilde{F}(x, t) = (1-t)x + tx = x$ for all $t$ (boundary stays fixed). ✓
> - $\tilde{F}(x, t) \neq q$ for all $t$: each $(1-t)x + tr(x)$ lies on the segment from $x$ to $r(x)$, which lies on the ray from $q$ through $x$, beyond $x$ (as seen from $q$), so it never contains $q$. ✓
>
> So $\tilde{F}$ is a deformation retraction of the punctured square onto its boundary.
>
> **Step 5: Descend to the torus via the universal property.**
>
> We want a deformation retraction $F: (T^2 \setminus \{pt\}) \times I \to T^2 \setminus \{pt\}$. We have $\tilde{F}$ on the square. Consider the diagram:
>
> ![[m590-26-6.svg]]
> *Upstairs, $\tilde F$ is an explicit straight-line push to the boundary; the vertical maps are the quotient maps. The red dashed $F$ is what the universal property delivers, and the only thing to check is that $\pi \circ \tilde F$ is constant on fibers, which holds because $\tilde F$ never moves the (glued) boundary points.*
>
> We want the dashed arrow $F$ to exist and be continuous. By the universal property ([[Universal Property of Quotient Maps|§13.3]]), the composite $\pi \circ \tilde{F}$ descends to a continuous map $F$ on $(T^2 \setminus \{pt\}) \times I$ if and only if $\pi \circ \tilde{F}$ is **constant on fibers** of $\pi \times \operatorname{id}$.
>
> **What does “constant on fibers” mean here?** Two points $(x_1, t)$ and $(x_2, t)$ are in the same fiber of $\pi \times \operatorname{id}$ when $\pi(x_1) = \pi(x_2)$ (and same $t$). This happens exactly when $x_1 \sim x_2$ under the edge identifications. We need:
>
> $$
> \text{if } x_1 \sim x_2, \quad \text{then } \pi(\tilde{F}(x_1, t)) = \pi(\tilde{F}(x_2, t)) \text{ for all } t.
> $$
>
> **Verification.** The identifications only happen on the boundary: $(0, s) \sim (2\pi, s)$ and $(s, 0) \sim (s, 2\pi)$. Since $\tilde{F}$ is **stationary on the boundary** ($\tilde{F}(x, t) = x$ for all $x \in \partial[0, 2\pi]^2$ and all $t$), identified points stay where they are throughout the homotopy:
>
> $$
> \tilde{F}((0, s), t) = (0, s) \quad \text{and} \quad \tilde{F}((2\pi, s), t) = (2\pi, s).
> $$
>
> Since $(0, s) \sim (2\pi, s)$ under $\pi$, we have $\pi(\tilde{F}((0,s), t)) = \pi(0, s) = \pi(2\pi, s) = \pi(\tilde{F}((2\pi, s), t))$. ✓
>
> Similarly for $(s, 0) \sim (s, 2\pi)$. ✓
>
> No other identifications exist (interior points have unique preimages), so there is nothing else to check.
>
> **Step 6: Conclusion.**
>
> By the universal property, $F$ exists and is continuous. Since $\tilde{F}$ is a deformation retraction of the punctured square onto $\partial[0, 2\pi]^2$, $F$ is a deformation retraction of $T^2 \setminus \{pt\}$ onto $\pi(\partial[0, 2\pi]^2)$ = the figure eight. Therefore:
>
> $$
> \pi_1(T^2 \setminus \{pt\}) \cong \pi_1(\text{figure eight}) \cong F_2.
> $$
>
> **Summary of the method:**
> 1. Work on the *square* (simple geometry: rays, straight lines).
> 2. Build a deformation retraction $\tilde{F}$ on the square.
> 3. Check that $\tilde{F}$ *respects the gluing*: identified boundary points stay identified throughout the homotopy (because $\tilde{F}$ is stationary on the boundary).
> 4. The universal property of quotient maps automatically gives a continuous deformation retraction $F$ on the torus.
>
> This is the general strategy whenever you want to build continuous maps on quotient spaces: work upstairs where geometry is simple, verify the gluing is respected, then descend.

^ex-35-8

![[m590-26-13.svg]]
*Step 4 on the square $[0, 2\pi]^2$: the red rays push every point away from the puncture $q = (\pi, \pi)$ onto the boundary, which stays fixed. After gluing (the two $a$ edges together, the two $b$ edges together, all four corners to one point) the boundary is the figure eight $a \vee b$. The orange loop $t$ around $q$ expands to the boundary word $aba^{-1}b^{-1}$ ([[§35 Deformation Retracts and Homotopy Type#^rem-35-8|the ungluing argument]]).*

> [!remark]- Connections
> - $\pi_1$ of the figure eight: [[§39 The Seifert–van Kampen Theorem#^ex-39-2|π₁(S¹ ∨ S¹) ≅ ℤ ∗ ℤ]]. Used in [[§39 The Seifert–van Kampen Theorem#^ex-39-4|π₁(T²) ≅ ℤ × ℤ via van Kampen]].
> - The square-to-torus quotient map: [[§13 Quotient Topology#^ex-13-6|The Square-to-Torus Quotient Map]].

> [!remark] Remark: The Ungluing Argument
> The punctured torus result is used in the van Kampen computation of $\pi_1(T^2)$ ([[§39 The Seifert–van Kampen Theorem#^ex-39-4|§39]]), where the key step is showing that a small loop $t$ around the puncture satisfies $i_1(t) = aba^{-1}b^{-1}$ in $\pi_1(T^2 \setminus \{pt\}) \cong F_2$. Here is the geometric argument:
>
> **1. $t$ survives ungluing.** The loop $t$ is a small circle around $q = (\pi, \pi)$, the center of the fundamental square. Since $t$ lives entirely in the *interior* of $[0, 2\pi]^2$ — it doesn't touch any edge — it is unaffected by the edge identifications. When we “unglue” (go from the torus back to the square), $t$ remains a loop.
>
> **2. Expand $t$ to the boundary.** In the punctured square, the deformation retract ([[§35 Deformation Retracts and Homotopy Type#^ex-35-8|Step 4 above]]) pushes $t$ radially outward from $q$, expanding it until it reaches the boundary $\partial[0, 2\pi]^2$.
>
> **3. Read off the boundary word.** Going counterclockwise around $\partial[0, 2\pi]^2$ from the bottom-left corner: bottom edge = $a$, right edge = $b$, top edge = $a^{-1}$ (same label, reversed direction), left edge = $b^{-1}$. So $t \simeq aba^{-1}b^{-1}$.
>
> **Why other loops can't be treated this way:** The loop $a$ (going around the “hole” of the torus) *crosses* an identified edge — it enters through the left side and exits through the right side. When you unglue, it breaks into a path from the left edge to the right edge, not a loop. You cannot make $a$ small enough to avoid the edges, because crossing the edge *is* what the loop does. So $a$ and $b$ are generators of the figure eight, not expressible as boundary words.
>
> **Connection to van Kampen:** Removing $q$ “frees” $aba^{-1}b^{-1}$ from being trivial: in $T^2$ it contracts to $pt$, but in $T^2 \setminus \{pt\}$ the contraction is blocked. Gluing the disk back (the van Kampen computation, [[§39 The Seifert–van Kampen Theorem#^ex-39-4|§39]]) forces $aba^{-1}b^{-1} = e$, which is exactly $ab = ba$, recovering $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ ([[§29 The Fundamental Group#^cor-29-8|§29.8]]).

^rem-35-8

## Homotopy Equivalence

Deformation retracts give isomorphisms on $\pi_1$, but they require $A \subseteq X$ and that $A$ stays fixed throughout the homotopy. The notion of *homotopy equivalence* is far more general: it relates spaces that need not be subspaces of each other.

> [!definition] Definition §35.2: Homotopy Equivalence
> Let $f: X \to Y$ and $g: Y \to X$ be continuous maps. If
>
> $$
> f \circ g \simeq \operatorname{id}_Y \qquad \text{and} \qquad g \circ f \simeq \operatorname{id}_X,
> $$
>
> then $f$ and $g$ are called **homotopy equivalences**, and $g$ is a **homotopy inverse** of $f$ (and vice versa).

^def-35-2

> [!remark] Remark: Homotopy Equivalence vs Homeomorphism
> The definition is structurally identical to [[§10 Continuous Functions#^def-10-2|homeomorphism]], with equality relaxed to homotopy:
>
> |  | **Homeomorphism** | **Homotopy Equivalence** |
> |---|---|---|
> | Condition | $f \circ g = \operatorname{id}_Y$ and $g \circ f = \operatorname{id}_X$ | $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$ |
> | Meaning | Points go back to exactly where they started | The composition can be continuously deformed into the identity |
> | Preserves | All topological properties (compactness, dimension, $\pi_1$, …) | $\pi_1$ and all homotopy invariants, but NOT compactness, dimension, … |
>
> Since $=$ is a special case of $\simeq$ (use the constant homotopy $H(x,t) = x$):
>
> $$
> \text{Homeomorphic} \implies \text{Homotopy equivalent} \implies \text{Isomorphic } \pi_1.
> $$
>
> Neither arrow reverses:
> - $S^1$ and $\mathbb{R}^2 \setminus \{0\}$: homotopy equivalent ([[§35 Deformation Retracts and Homotopy Type#^ex-35-6|deformation retract]]) but NOT homeomorphic (compact vs. non-compact).
> - $S^2$ and $\{pt\}$: both have $\pi_1 = 0$, but NOT homotopy equivalent ($S^2$ is not [[§35 Deformation Retracts and Homotopy Type#^def-35-4|contractible]]).

^rem-35-9

> [!remark] Remark: Composition of Homotopy Equivalences
> If $f: X \to Y$ and $h: Y \to Z$ are homotopy equivalences, then $h \circ f: X \to Z$ is a homotopy equivalence.
>
> *Proof.* Let $g$ be a homotopy inverse of $f$ (so $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$) and $k$ a homotopy inverse of $h$ (so $h \circ k \simeq \operatorname{id}_Z$ and $k \circ h \simeq \operatorname{id}_Y$). We claim $g \circ k$ is a homotopy inverse of $h \circ f$.
>
> **Check 1:** $(g \circ k) \circ (h \circ f) \simeq \operatorname{id}_X$?
>
> $$
> \begin{aligned}
> (g \circ k) \circ (h \circ f) &= g \circ (k \circ h) \circ f &\text{(associativity of composition)}\\
> &\simeq g \circ \operatorname{id}_Y \circ f &\text{(since } k \circ h \simeq \operatorname{id}_Y\text{)}\\
> &= g \circ f &\\
> &\simeq \operatorname{id}_X. &\text{(since } g \circ f \simeq \operatorname{id}_X\text{)}
> \end{aligned}
> $$
>
> (Here we use: if $\alpha \simeq \beta$, then $g \circ \alpha \circ f \simeq g \circ \beta \circ f$—homotopy is preserved by pre- and post-composition with continuous maps.)
>
> **Check 2:** $(h \circ f) \circ (g \circ k) \simeq \operatorname{id}_Z$? Same idea: $h \circ (f \circ g) \circ k \simeq h \circ \operatorname{id}_Y \circ k = h \circ k \simeq \operatorname{id}_Z$.

^rem-35-10

> [!theorem] Theorem §35.3: Homotopy Equivalence is an Equivalence Relation
> The relation “$X \simeq Y$” (there exists a homotopy equivalence $f: X \to Y$) is an [[§22 Partitions and Equivalence Relations#^def-22-4|equivalence relation]] on topological spaces.

^thm-35-3

> [!proof]+ Proof
> **Reflexive ($X \simeq X$):** Take $f = \operatorname{id}_X: X \to X$. Its homotopy inverse is also $\operatorname{id}_X$: $\operatorname{id}_X \circ \operatorname{id}_X = \operatorname{id}_X \simeq \operatorname{id}_X$ in both directions.
>
> **Symmetric ($X \simeq Y \Rightarrow Y \simeq X$):** Suppose $f: X \to Y$ is a homotopy equivalence with homotopy inverse $g: Y \to X$. The [[§35 Deformation Retracts and Homotopy Type#^def-35-2|definition]] is symmetric in $f$ and $g$: the conditions $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$ say exactly that $g$ is a homotopy equivalence with homotopy inverse $f$.
>
> **Transitive ($X \simeq Y$ and $Y \simeq Z \Rightarrow X \simeq Z$):** Suppose $f: X \to Y$ and $h: Y \to Z$ are homotopy equivalences. By [[§35 Deformation Retracts and Homotopy Type#^rem-35-10|the remark above]], $h \circ f: X \to Z$ is a homotopy equivalence.

^pf-35-3

*Uses:* [[§35 Deformation Retracts and Homotopy Type#^def-35-2|Def. §35.2]]

> [!definition] Definition §35.3: Homotopy Type
> Two topological spaces that are homotopy equivalent are said to have the same **homotopy type**.

^def-35-3

> [!example] Example §35.9: Deformation Retracts Give Homotopy Equivalences
> If $A$ is a [[§35 Deformation Retracts and Homotopy Type#^def-35-1|deformation retract]] of $X$, then the retraction $r: X \to A$ and the inclusion $j: A \hookrightarrow X$ are homotopy inverses: $r \circ j = \operatorname{id}_A$ (exactly, not just up to homotopy) and $j \circ r \simeq \operatorname{id}_X$ (via the deformation retraction). In particular, $A$ and $X$ have the same homotopy type.

^ex-35-9

> [!example] Example §35.10: Figure-Eight and Theta Space
> The [[§38 Fundamental Group of Some Surfaces#^def-38-4|figure-eight space]] $S^1 \vee S^1$ and the theta space $\Theta$ (two arcs joining two points) have the same homotopy type, even though neither is a deformation retract of the other. Both have $\pi_1 \cong F_2$.

^ex-35-10

## The General Basepoint-Change Lemma

The [[§34 Retractions and Fixed Points#^lem-34-1|lemma in §34.1]] assumed the basepoint stays fixed during the homotopy ($H(x_0, t) = y_0$ for all $t$). In practice, homotopy equivalences move the basepoint. The following generalization handles this by introducing a [[Basepoint Independence of π₁|basepoint-change]] path.

> [!theorem] Lemma §35.4: Homotopic Maps and $\pi_1$: General Case
> Let $h, k: X \to Y$ be continuous, and let $H: X \times I \to Y$ be a homotopy from $h$ to $k$. Let $x_0 \in X$, and define the path $\alpha: I \to Y$ by
>
> $$
> \alpha(t) = H(x_0, t).
> $$
>
> Then $\alpha$ is a path from $h(x_0)$ to $k(x_0)$, and
>
> $$
> k_* = \hat{\alpha} \circ h_*,
> $$
>
> where $\hat{\alpha}: \pi_1(Y, h(x_0)) \to \pi_1(Y, k(x_0))$ is the [[Basepoint Independence of π₁|basepoint-change isomorphism]] $\hat{\alpha}([f]) = [\bar{\alpha}] * [f] * [\alpha]$.
>
> In diagram form:
>
> ![[m590-26-7.svg]]
> *The lemma asserts the red arrow: $k_{\ast}$ is $h_{\ast}$ followed by the basepoint-change isomorphism $\hat\alpha$ along the track $\alpha(t) = H(x_0, t)$ of the basepoint. If the basepoint does not move, $\hat\alpha = \operatorname{id}$ and the triangle collapses to $k_{\ast} = h_{\ast}$.*

^lem-35-4

> [!proof]+ Proof
> This generalizes the [[§34 Retractions and Fixed Points#^lem-34-1|fixed-basepoint lemma]]. Let $[f] \in \pi_1(X, x_0)$, so $f: I \to X$ is a loop at $x_0$.
>
> Consider the composition $H \circ (f \times \operatorname{id}): I \times I \to Y$, where $(f \times \operatorname{id})(s, t) = (f(s), t)$. This map sends:
> - Bottom edge ($t = 0$): $(s, 0) \mapsto H(f(s), 0) = h(f(s))$, i.e., the loop $h \circ f$.
> - Top edge ($t = 1$): $(s, 1) \mapsto H(f(s), 1) = k(f(s))$, i.e., the loop $k \circ f$.
> - Left edge ($s = 0$): $(0, t) \mapsto H(f(0), t) = H(x_0, t) = \alpha(t)$.
> - Right edge ($s = 1$): $(1, t) \mapsto H(f(1), t) = H(x_0, t) = \alpha(t)$.
>
> The bottom is the loop $h \circ f$ at $h(x_0)$; the top is the loop $k \circ f$ at $k(x_0)$; both side edges trace the path $\alpha$. The paths
>
> $$
> \alpha * (k \circ f) \qquad \text{and} \qquad (h \circ f) * \alpha
> $$
>
> are path homotopic. Indeed, let $\beta_1$ be the path in $I \times I$ that runs along the bottom edge and then up the right edge, and $\beta_2$ the path that runs up the left edge and then along the top edge. Both go from $(0,0)$ to $(1,1)$, and $I \times I$ is convex, so the straight-line homotopy $(1-t)\beta_1(s) + t\beta_2(s)$ is a path homotopy from $\beta_1$ to $\beta_2$ inside $I \times I$ ([[§29 The Fundamental Group#^ex-29-2|Example §29.2]]). Composing it with $H \circ (f \times \operatorname{id})$, which carries $\beta_1$ to $(h \circ f) * \alpha$ and $\beta_2$ to $\alpha * (k \circ f)$, gives a path homotopy between these two paths. Therefore:
>
> $$
> [\alpha] * [k \circ f] = [h \circ f] * [\alpha],
> $$
>
> which gives $[k \circ f] = [\bar{\alpha}] * [h \circ f] * [\alpha] = \hat{\alpha}([h \circ f])$, i.e., $k_*([f]) = \hat{\alpha}(h_*([f]))$.

^pf-35-4

*Uses:* [[Basepoint Independence of π₁|§29.2]], [[§34 Retractions and Fixed Points#^lem-34-1|§34.1]], [[§29 The Fundamental Group#^ex-29-2|Ex. §29.2]]

![[m590-26-14.svg]]
*The square $I \times I$, each corner labeled by its image under $H \circ (f \times \operatorname{id})$: bottom $h \circ f$, top $k \circ f$, both sides $\alpha$. The blue path (bottom, then right side) and the red path (left side, then top) have the same endpoints in the convex square, so they are path homotopic there (gray). Composing with $H \circ (f \times \operatorname{id})$ gives $(h \circ f) \ast  \alpha \simeq_p \alpha \ast  (k \circ f)$.*

> [!remark] Remark
> When $H(x_0, t) = y_0$ for all $t$ (the basepoint stays fixed), the path $\alpha$ is constant, so $\hat{\alpha} = \operatorname{id}$ and we recover [[§34 Retractions and Fixed Points#^lem-34-1|the earlier lemma]]: $k_* = h_*$.

^rem-35-11

## Homotopy Equivalences Induce Isomorphisms on $\pi_1$

> [!theorem] Theorem §35.5: Homotopy Equivalence Induces Isomorphism on $\pi_1$
> If $f: X \to Y$ is a homotopy equivalence, then for every $x_0 \in X$,
>
> $$
> f_*: \pi_1(X, x_0) \to \pi_1(Y, f(x_0))
> $$
>
> is an isomorphism.

^thm-35-5

> [!proof]+ Proof
> Let $g: Y \to X$ be a homotopy inverse of $f$, so $f \circ g \simeq \operatorname{id}_Y$ and $g \circ f \simeq \operatorname{id}_X$.
>
> Consider the chain $X \xrightarrow{f} Y \xrightarrow{g} X \xrightarrow{f} Y$.
>
> **$f_{\ast}$ is surjective (at another basepoint):** Let $y_0 = f(x_0)$ and $x_1 = g(y_0)$. Since $f \circ g \simeq \operatorname{id}_Y$, the [[§35 Deformation Retracts and Homotopy Type#^lem-35-4|general lemma]] (at the basepoint $y_0$) gives
>
> $$
> (\operatorname{id}_Y)_* = \hat{\alpha} \circ (f \circ g)_* = \hat{\alpha} \circ f_* \circ g_*
> $$
>
> for some path $\alpha$. Since $(\operatorname{id}_Y)_* = \operatorname{id}$ and $\hat{\alpha}$ is an [[Basepoint Independence of π₁|isomorphism]], $f_* \circ g_*$ is an isomorphism. In particular, $f_*$ is surjective (it has a right inverse up to isomorphism), but as a map $\pi_1(X, x_1) \to \pi_1(Y, f(x_1))$, not at $x_0$. What we keep from this step: $g_*: \pi_1(Y, y_0) \to \pi_1(X, x_1)$ is injective.
>
> **$f_{\ast}$ is injective:** Since $g \circ f \simeq \operatorname{id}_X$, the [[§35 Deformation Retracts and Homotopy Type#^lem-35-4|general lemma]] gives
>
> $$
> (\operatorname{id}_X)_* = \hat{\beta} \circ (g \circ f)_* = \hat{\beta} \circ g_* \circ f_*
> $$
>
> for some path $\beta$. So $g_* \circ f_*$ is an isomorphism, hence $f_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$ is injective (it has a left inverse up to isomorphism), and $g_*: \pi_1(Y, y_0) \to \pi_1(X, x_1)$ is surjective.
>
> **Basepoint change:** Thus $g_{\ast}: \pi_1(Y, y_0) \to \pi_1(X, x_1)$ is bijective, and $f_{\ast} = g_{\ast}^{-1} \circ \hat{\beta}^{-1}$ is an isomorphism $\pi_1(X, x_0) \to \pi_1(Y, y_0)$ (Munkres 58.7).

^pf-35-5

*Uses:* [[§35 Deformation Retracts and Homotopy Type#^lem-35-4|§35.4]], [[Basepoint Independence of π₁|§29.2]], [[Functoriality of π₁|§29.5]]

> [!remark] Remark: Deformation Retract as a Special Case
> For a deformation retract $A \subseteq X$, the inclusion $j: A \hookrightarrow X$ is a [[§35 Deformation Retracts and Homotopy Type#^ex-35-9|homotopy equivalence]] (with homotopy inverse $r$). The theorem recovers [[Deformation Retract Induces Isomorphism on π₁|our earlier result]] that $j_*$ is an isomorphism—but now we see it as a special case of a much more general principle.

^rem-35-12

## Contractible Spaces

> [!definition] Definition §35.4: Contractible Space
> A space $X$ is **contractible** if $\operatorname{id}_X: X \to X$ is [[§28 Homotopy of Paths#^def-28-2|nullhomotopic]], i.e., homotopic to a constant map.

^def-35-4

> [!theorem] Theorem §35.6: $X$ Contractible $\iff$ Homotopy Type of a Point
> A space $X$ is contractible if and only if $X$ has the homotopy type of a one-point space.

^thm-35-6

> [!proof]+ Proof
> ($\Rightarrow$) Suppose $X$ is contractible, so $\operatorname{id}_X \simeq c$ where $c: X \to X$ is the constant map $c(x) = x_0$ for some $x_0 \in X$. Let $\{p\}$ be a one-point space. Define $f: X \to \{p\}$ (the unique map) and $g: \{p\} \to X$ by $g(p) = x_0$. Then:
> - $f \circ g = \operatorname{id}_{\{p\}}$ (exactly).
> - $g \circ f: X \to X$ sends every point to $x_0$, i.e., $g \circ f = c \simeq \operatorname{id}_X$.
>
> So $f$ and $g$ are homotopy inverses.
>
> ($\Leftarrow$) Suppose $f: X \to \{p\}$ and $g: \{p\} \to X$ are homotopy inverses. Then $g \circ f: X \to X$ is a constant map (it sends everything to $g(p)$), and $g \circ f \simeq \operatorname{id}_X$. So $\operatorname{id}_X$ is nullhomotopic.

^pf-35-6

*Uses:* [[§35 Deformation Retracts and Homotopy Type#^def-35-2|Def. §35.2]], [[§35 Deformation Retracts and Homotopy Type#^def-35-4|Def. §35.4]]

> [!remark] Remark
> Since a one-point space has trivial fundamental group, any contractible space satisfies $\pi_1(X, x_0) = 0$. Examples: $\mathbb{R}^n$, $B^n$, and any convex subset of $\mathbb{R}^n$ are contractible (via [[§28 Homotopy of Paths#^thm-28-1|straight-line homotopies]]).

^rem-35-13

> [!theorem] Proposition §35.7: Retract of a Contractible Space is Contractible
> If $X$ is contractible and $A$ is a retract of $X$, then $A$ is contractible.

^prop-35-7

> [!proof]+ Proof
> Let $r: X \to A$ be a [[§34 Retractions and Fixed Points#^def-34-1|retraction]] ($r|_A = \operatorname{id}_A$). Since $X$ is contractible, $\operatorname{id}_X$ is nullhomotopic: there exists $F: X \times I \to X$ with $F(x, 0) = x$ and $F(x, 1) = x_0$ for some point $x_0$.
>
> Define $F': A \times I \to A$ by $F' = r \circ F|_{A \times I}$. Check:
> - $F'(a, 0) = r(F(a, 0)) = r(a) = a$ (since $a \in A$ and $r|_A = \operatorname{id}_A$).
> - $F'(a, 1) = r(F(a, 1)) = r(x_0)$ (a fixed point in $A$).
> - $F'$ is continuous (composition of continuous maps).
>
> So $F'$ is a homotopy from $\operatorname{id}_A$ to the constant map $a \mapsto r(x_0)$. Thus $A$ is contractible.

^pf-35-7

*Uses:* [[§34 Retractions and Fixed Points#^def-34-1|Def. §34.1]], [[§35 Deformation Retracts and Homotopy Type#^def-35-4|Def. §35.4]]
