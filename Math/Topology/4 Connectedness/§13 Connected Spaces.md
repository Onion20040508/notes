---
type: section
subject: "[[Topology]]"
chapter: 4
section: 13
munkres: "§23"
tags: [topology, math590]
---
← [[§12 Quotient Topology]] · ↑ [[· 4 Connectedness]] · [[§14 Connected Subspaces of ℝ]] →

## Definition and Basic Properties

> [!definition] Definition §13.1: Separation and Connected Space
> A **separation** of a topological space $X$ is a pair $U, V$ of disjoint nonempty open subsets of $X$ whose union is $X$.
>
> A space is called **connected** if there doesn't exist a separation of $X$.

^def-13-1

> [!remark]- Connections
> - In the complex plane: [[§12★ Regions in the Complex Plane#^def-12-4|342 Def. §12.4]] (domains, defined by polygonal connectedness, which for open subsets of the plane agrees with connectedness).

> [!remark] Remark: Why Connectedness Matters
> Connectedness captures the intuitive notion that a space is “in one piece”—you can't split it into two separate open chunks.
>
> **1. The [[§14 Connected Subspaces of ℝ#^thm-14-3|Intermediate Value Theorem]] depends on connectedness.** If $f: X \to \mathbb{R}$ is continuous and $X$ is connected, then $f(X)$ is an interval (connected subset of $\mathbb{R}$). This is why continuous functions on $[a,b]$ satisfy IVT.
>
> **2. Connectedness is a topological invariant.** Homeomorphic spaces are either both connected or both disconnected. This gives a powerful tool for showing spaces are *not* homeomorphic.
>
> **3. The definition may seem backwards.** We define “connected” as the *absence* of a separation, rather than the presence of some positive property. This is because connectedness is fundamentally about what you *can't* do (split the space), not what you can do.
>
> **4. Connected $\neq$ path-connected.** A space can be “in one piece” topologically without having paths between all points. Path-connectedness is strictly stronger (in general).

^rem-13-1

> [!remark]- Connections
> - MATH 451 version: [[Intermediate Value Theorem]].
> - Invariance follows from [[Continuous Image of a Connected Space is Connected|Continuous Image of Connected Space]]; the strictness in point 4 is [[§14 Connected Subspaces of ℝ#^thm-14-4|Path-Connected Implies Connected]] and [[§14 Connected Subspaces of ℝ#^ex-14-7|Topologist's Sine Curve]].
> - Connected components, which 590 does not treat, are defined in [[§1 Point-Set Topology Review#^def-1-8|591 Def. §1.8]], with their basic properties in [[§1 Point-Set Topology Review#^prop-1-7|591 Prop. §1.7]].

> [!remark] Remark: Hausdorff and Connected are Independent
> The [[§8 Hausdorff Spaces#^def-8-1|Hausdorff]] property and connectedness are logically independent — neither implies nor contradicts the other:
>
> - Hausdorff and connected: $\mathbb{R}$ with standard topology
> - Hausdorff and not connected: $\{0, 1\}$ with discrete topology
> - Not Hausdorff and connected: $\{0, 1\}$ with indiscrete topology
> - Not Hausdorff and not connected: $\{a, b, c\}$ with topology $\{\emptyset, \{a\}, \{b,c\}, \{a,b,c\}\}$
>
> Hausdorff is about separating *points* (every two distinct points have disjoint neighborhoods). Connected is about *not* being able to separate the *space itself* into two disjoint open pieces.

^rem-13-2

> [!example] Example §13.1
> $X = \{0, 1, 2\}$ with indiscrete topology. $\Rightarrow$ $X$ is connected (no separation possible).

^ex-13-1

> [!example] Example §13.2
> $X = \{0, 1, 2\}$ with discrete topology. $\{0, 1\} \cup \{2\} = X$. Not connected.

^ex-13-2

> [!example] Example §13.3
> $Y = [-1, 0) \cup (0, 1]$ as subspace of $\mathbb{R}$. Not connected. Take $[-1, 0)$ and $(0, 1]$.

^ex-13-3

![[m590-13-1.svg]]
*A separation of $Y = [-1,0) \cup (0,1]$: both pieces are open in $Y$ (for example $[-1, 0) = (-2, 0) \cap Y$), disjoint, nonempty, and cover $Y$. The missing point $0$ (hollow) is the only point that could have connected them. It is a limit point of both pieces, but it is not in $Y$.*

> [!theorem] Lemma §13.1: Characterization via Clopen Sets
> A space $X$ is connected if and only if the only subsets of $X$ which are both open and closed are $\emptyset$ and $X$.

^lem-13-1

> [!proof]+ Proof
> $(\Rightarrow)$ $A \subseteq X$ both open and closed and $A \neq \emptyset \neq X$. Take $U = A$, $V = X \setminus A$. Then $V$ is also open and closed. $\Rightarrow$ separation of $X$, hence not connected.
>
> $(\Leftarrow)$ Suppose $X$ not connected. There exists $U, V$ separation of $X$. $U = X \setminus V$. $V$ open $\Rightarrow$ $U$ closed. $U \neq \emptyset$, but $U \neq X$. Similarly for $V$.

^pf-13-1

> [!remark] Remark
> The definition implies $V = U^c = X \setminus U$.

^rem-13-3

## Separation via Limit Points

> [!theorem] Lemma §13.2: Separation Characterization
> If $Y$ is a subspace of $X$, a separation of $Y$ is a pair of disjoint nonempty sets $A$ and $B$ whose union is $Y$, neither of which contains a [[§7 Interior and Closure#^def-7-3|limit point]] of the other.

^lem-13-2

> [!proof]+ Proof of Lemma
> (Old def $\Rightarrow$ new def) Suppose $A$ and $B$ form a separation of $Y$. $\Rightarrow$ $A$ is open and closed in $Y$.
>
> The closure of $A$ in $Y$ is $\overline{A} \cap Y$, where $\overline{A}$ is the closure of $A$ in $X$ ([[§7 Interior and Closure#^thm-7-2|Closure in Subspace]]). Since $A$ is closed in $Y$ $\Rightarrow$ $A = \overline{A} \cap Y$.
>
> $\Rightarrow$ $B \cap \overline{A} = \emptyset$ (since $B \cap A = \emptyset$). Recall $\overline{A} = A \cup \{\text{limit pts of } A\}$ ([[§7 Interior and Closure#^thm-7-4|Closure and Limit Points]]) $\Rightarrow$ $B$ contains no limit points of $A$.
>
> Similarly, $A$ contains no limit points of $B$.
>
> (New def $\Rightarrow$ old def) Suppose $A, B$ disjoint nonempty such that $A \cup B = Y$, neither $A$ nor $B$ contains a limit point of the other. $A \cap \overline{B} = \emptyset$ and $B \cap \overline{A} = \emptyset$. $\Rightarrow$ $Y \cap \overline{B} = B$ and $Y \cap \overline{A} = A$ (since $Y = A \cup B$). $\Rightarrow$ $A, B$ closed in $Y$. $\Rightarrow$ $Y \setminus A = B$, $Y \setminus B = A$ open in $Y$. $\Rightarrow$ separation of $Y$.

^pf-13-2

*Uses:* [[§7 Interior and Closure#^thm-7-2|§7.2]], [[§7 Interior and Closure#^thm-7-4|§7.4]]

> [!remark] Remark: Limit Points in $X$ vs. $Y$
> In this lemma, “limit point” is taken in the ambient space $X$. However, for points in $Y$, it doesn't matter:
>
> If $x \in Y$ and $A \subseteq Y$, then:
>
> $x$ is a limit point of $A$ in $X$ $\Longleftrightarrow$ $x$ is a limit point of $A$ in $Y$
>
> *Proof:* Every neighborhood of $x$ in $Y$ has the form $U \cap Y$ for some neighborhood $U$ of $x$ in $X$. So:
>
> $$
> \begin{aligned}
> &(U \cap Y) \cap (A \setminus \{x\}) \neq \emptyset \text{ for all nbhds } U \cap Y \text{ in } Y \\
> \Longleftrightarrow\quad &U \cap (A \setminus \{x\}) \neq \emptyset \text{ for all nbhds } U \text{ in } X
> \end{aligned}
> $$
>
> (The $\cap Y$ is redundant since $A \subseteq Y$.)
>
> Since $A, B \subseteq Y$, asking whether $B$ contains a limit point of $A$ gives the same answer in either space. The “$Y \subseteq X$” framing is useful when discussing connectedness of a subspace while working in a larger ambient space.

^rem-13-4

## Continuous Images of Connected Spaces

> [!theorem] Theorem §13.3: Continuous Image of Connected Space
> The image of a connected space under a continuous map is connected.

^thm-13-3

> [!proof]+ Proof
> Let $f: X \to Y$ be continuous, $X$ is connected. Want to show $f(X)$ is connected.
>
> Restrict the codomain $Y$ to $f(X)$: $g: X \to f(X)$, $g(x) = f(x)$ for all $x \in X$, is surjective. Also continuous ([[§9 Continuous Functions#^thm-9-4|can check]]).
>
> Suppose $f(X)$ has a separation $A, B$. Then $g^{-1}(A) \cup g^{-1}(B) = g^{-1}(A \cup B) = X$.
>
> $g^{-1}(A), g^{-1}(B)$ are disjoint because $g$ is a function and $A, B$ are disjoint. They are open because $g$ is continuous, and nonempty because $g$ is surjective and $A, B \neq \emptyset$.
>
> Hence $g^{-1}(A), g^{-1}(B)$ is a separation of $X$, a contradiction.

^pf-13-3

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]]

> [!remark]- Connections
> - The engine of the [[§14 Connected Subspaces of ℝ#^thm-14-3|Intermediate Value Theorem]].
> - Compactness analogue: [[Continuous Image of a Compact Space is Compact|Continuous Image of Compact is Compact]].
> - Used in Relativity: a continuous function on a connected set of velocities cannot jump between two values, in the proof that the postulates force the invariance of the interval — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-1|REL Theorem §B1.2.1]]; and in splitting the Lorentz group into its four components — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]].
> - Its case X = [a, b], Y ⊆ ℝ is the Intermediate Value Theorem: [[§10 Continuity#^thm-10-10|Calc Thm. §10.10]] (with worked examples).

> [!remark] Remark: Properties of Preimages
> Useful facts: $f^{-1}(A) \cup f^{-1}(B) = f^{-1}(A \cup B)$ and $f^{-1}(A) \cap f^{-1}(B) = f^{-1}(A \cap B)$.

^rem-13-5

## Connected Subspaces

> [!theorem] Lemma §13.4: Connected Subspace and Separation
> If $C$ and $D$ separate $X$, and $Y$ is a connected subspace of $X$, then $Y \subseteq C$ or $Y \subseteq D$.

^lem-13-4

> [!proof]+ Proof
> $C \cap Y$ and $D \cap Y$ are open in $Y$, disjoint since $C, D$ disjoint. Their union is $Y$.
>
> If both nonempty, then separation of $Y$, but $Y$ connected, so one of which must be empty.
>
> $\Rightarrow$ $Y \subseteq C$ or $Y \subseteq D$.

^pf-13-4

> [!theorem] Theorem §13.5: Union of Connected Subspaces
> The union of a collection of connected subspaces of $X$ that have a point in common is connected.

^thm-13-5

> [!proof]+ Proof
> Let $\{A_\alpha\}$ be connected subspaces of $X$. Suppose there exists $p \in \bigcap A_\alpha$. Want to show $Y = \bigcup A_\alpha$ is connected.
>
> Suppose $Y$ has a separation $C, D$. $\Rightarrow$ $p \in C$ without loss of generality. $A_\alpha$ connected $\Rightarrow$ $A_\alpha \subseteq C$ or $A_\alpha \subseteq D$ for each $\alpha$ ([[§13 Connected Spaces#^lem-13-4|Lemma §13.4]]).
>
> But $p \in A_\alpha$, $p \in C$ $\Rightarrow$ $A_\alpha \subseteq C$ (true for every $\alpha$). $\Rightarrow$ $\bigcup A_\alpha \subseteq C$, but $\bigcup A_\alpha = Y$. $\Rightarrow$ $D = \emptyset$, contradiction.

^pf-13-5

*Uses:* [[§13 Connected Spaces#^lem-13-4|§13.4]]

![[m590-13-2.svg]]
*Connected sets $A_\alpha, A_\beta, A_\gamma$ sharing the point $p$ (red). If a separation $C, D$ of the union put $p$ in $C$, then [[§13 Connected Spaces#^lem-13-4|Lemma §13.4]] would force each connected $A$ to lie entirely in $C$, since each contains $p$. That leaves $D$ empty.*

## Products of Connected Spaces

> [!theorem] Theorem §13.6: Finite Product of Connected Spaces
> A finite Cartesian product of connected spaces is also connected.

^thm-13-6

> [!proof]+ Proof
> Suffices to prove product of 2 spaces, and then induction. For $X \times Y$, $X, Y$ connected.
>
> Choose $a \in X$, $b \in Y$. $a \times b \in X \times Y$. For each $x \in X$, take $T_x = (X \times b) \cup (x \times Y)$.
>
> $X \times b$ is homeomorphic to $X$. $x \times Y$ is homeomorphic to $Y$. $\Rightarrow$ union of two connected spaces, with $x \times b$ in common.
>
> $\Rightarrow$ $T_x$ connected. $\Rightarrow$ $\bigcup_{x \in X} T_x$ is connected since union of subspaces $T_x$ with $a \times b$ in common ([[§13 Connected Spaces#^thm-13-5|§13.5]]) $\Rightarrow$ $X \times Y$ connected.

^pf-13-6

*Uses:* [[§13 Connected Spaces#^thm-13-3|§13.3]], [[§13 Connected Spaces#^thm-13-5|§13.5]]

![[m590-13-3.svg]]
*The proof for $X \times Y$: $T_x$ is the cross formed by the horizontal $X \times b$ (blue) and the vertical $x \times Y$ (red), which meet at $x \times b$, so each $T_x$ is connected. Every cross contains the same horizontal line, hence the point $a \times b$. As $x$ varies (grey lines), the crosses cover $X \times Y$, and Theorem §13.5 finishes the proof.*

> [!remark]- Connections
> - Path-connected analogue: [[§14 Connected Subspaces of ℝ#^thm-14-5|Product of Path-Connected Spaces]]; compact analogue: [[§15 Compact Spaces#^thm-15-8|Finite Product of Compact Spaces]].
