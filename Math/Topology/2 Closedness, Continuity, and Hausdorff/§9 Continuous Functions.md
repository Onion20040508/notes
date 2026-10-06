---
type: section
subject: "[[Topology]]"
chapter: 2
section: 9
munkres: "§18"
tags: [topology, math590]
---
← [[§8 Hausdorff Spaces]] · ↑ [[· 2 Closedness, Continuity, and Hausdorff]] · [[§10 Product Topology on Arbitrary Products]] →

## Definition and Basic Properties

> [!definition] Definition §9.1: Continuous Function
> Let $X, Y$ be topological spaces. A function $f: X \to Y$ is **continuous** if for each open set $V \subseteq Y$, the preimage $f^{-1}(V)$ is a subset of $X$ that is open.
>
> (This generalizes the $\varepsilon$-$\delta$ definition of continuity for metric spaces.)

^def-9-1

> [!proof]+ Proof That Checking on a Basis Suffices
> It suffices to show the inverse image of every basis element is open. Let $V = \bigcup_\alpha B_\alpha$. Then $f^{-1}(V) = \bigcup_\alpha f^{-1}(B_\alpha)$. If each $f^{-1}(B_\alpha)$ is open, then $f^{-1}(V)$ is open.

^pf-def-9-1

*Uses:* [[§2 Basis for a Topology#^lem-2-1|§2.1]]

![[m590-9-1.svg]]
*Continuity is a statement about preimages: for the open set $V \subseteq Y$ (red), the set $f^{-1}(V)$ of everything that lands in $V$ (blue, here in two pieces) must be open in $X$. Nothing is required of forward images; $f$ may send open sets to non-open ones.*

> [!remark]- Connections
> - MATH 451 version: [[§21 More on Metric Spaces꞉ Continuity#^def-21-1|Continuous Maps Between Metric Spaces]].
> - Recovered for metric spaces: [[§11 Metric Topology#^thm-11-7|ε-δ Characterization of Continuity]].

> [!example] Example §9.1: $f: \mathbb{R} \to \mathbb{R}$ in Analysis
> The “$\varepsilon$-$\delta$” definition of continuous function: $\forall \varepsilon > 0$, w.t.s. $\exists \delta > 0$ s.t. $|f(x) - f(y)| < \varepsilon$ if $|x - y| < \delta$.
>
> Topological definition $\Leftrightarrow$ “$\varepsilon$-$\delta$”: $\forall x \in \mathbb{R}$, $f^{-1}((f(x) - \varepsilon, f(x) + \varepsilon))$ is an open set in $\mathbb{R}$, i.e., is a neighborhood of $x$.
>
> $\exists \delta > 0$ s.t. $(x - \delta, x + \delta) \subset f^{-1}((f(x) - \varepsilon, f(x) + \varepsilon))$. ✓

^ex-9-1

> [!remark]- Connections
> - MATH 451: [[§17 Continuous Functions#^thm-17-1|The Epsilon-Delta Characterization]].

> [!example] Example §9.2: $\mathbb{R}_\ell$: Lower Limit Topology
> $\mathcal{B}_\ell = \{[a,b) \mid a, b \in \mathbb{R}\}$. $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x$.
>
> **(1)** $f: \mathbb{R}_{\text{std}} \to \mathbb{R}_\ell$ not continuous. $[a,b)$ open in $\mathbb{R}_\ell$, but $f^{-1}([a,b)) = [a,b)$ not open in $\mathbb{R}_{\text{std}}$.
>
> **(2)** $f: \mathbb{R}_\ell \to \mathbb{R}$. $f^{-1}((a,b)) = (a,b) = \bigcup_{n=1}^{\infty} [a + \frac{1}{n}, b)$. This is open in $\mathbb{R}_\ell$. So $f$ is continuous.
>
> **Conclusion:** Continuity depends on $f$, and the topologies on $X$, $Y$.

^ex-9-2

> [!remark]- Connections
> - Defined in [[§2 Basis for a Topology#^ex-2-3|Lower Limit Topology]]; (1) and (2) reflect [[§2 Basis for a Topology#^ex-2-5|ℝ_ℓ is strictly finer than ℝ_std]].

> [!theorem] Theorem §9.1: Equivalent Conditions for Continuity
> Let $f: X \to Y$ be a function between topological spaces. The following are equivalent:
> 1. $f$ is continuous.
> 2. For every subset $A$ of $X$, $f(\overline{A}) \subseteq \overline{f(A)}$.
> 3. For every closed subset $B$ of $Y$, $f^{-1}(B)$ is closed in $X$.
> 4. For each $x \in X$ and each neighborhood $V$ of $f(x)$, there is a neighborhood $U$ of $x$ such that $f(U) \subseteq V$. (Continuity at $x$)

^thm-9-1

> [!proof]+ Proof
> $(1) \Rightarrow (4)$: Let $x \in X$ and let $V$ be a neighborhood of $f(x)$. Since $V$ is open and $f$ is continuous, $f^{-1}(V)$ is open in $X$. Since $f(x) \in V$, we have $x \in f^{-1}(V)$. So $U = f^{-1}(V)$ is a neighborhood of $x$, and $f(U) = f(f^{-1}(V)) \subseteq V$.
>
> $(4) \Rightarrow (1)$: Let $V \subseteq Y$ be open. We show $f^{-1}(V)$ is open. Let $x \in f^{-1}(V)$. Then $f(x) \in V$, so $V$ is a neighborhood of $f(x)$. By (4), there exists a neighborhood $U_x$ of $x$ such that $f(U_x) \subseteq V$. This means $U_x \subseteq f^{-1}(V)$. Since $U_x$ is open and contains $x$, we have shown that every point of $f^{-1}(V)$ has an open neighborhood contained in $f^{-1}(V)$. Thus $f^{-1}(V) = \bigcup_{x \in f^{-1}(V)} U_x$ is a union of open sets, hence open.
>
> $(1) \Rightarrow (3)$: Let $B \subseteq Y$ be closed. Then $Y \setminus B$ is open. By (1), $f^{-1}(Y \setminus B) = X \setminus f^{-1}(B)$ is open. Thus $f^{-1}(B)$ is closed.
>
> $(3) \Rightarrow (1)$: Let $V \subseteq Y$ be open. Then $Y \setminus V$ is closed. By (3), $f^{-1}(Y \setminus V) = X \setminus f^{-1}(V)$ is closed. Thus $f^{-1}(V)$ is open.
>
> $(1) \Rightarrow (2)$: Let $A \subseteq X$. We show $f(\overline{A}) \subseteq \overline{f(A)}$. Let $x \in \overline{A}$. We need $f(x) \in \overline{f(A)}$, i.e., every neighborhood of $f(x)$ intersects $f(A)$. Let $V$ be a neighborhood of $f(x)$. By (1), $f^{-1}(V)$ is open, and $x \in f^{-1}(V)$. Since $x \in \overline{A}$, $f^{-1}(V)$ intersects $A$, say at point $a \in f^{-1}(V) \cap A$. Then $f(a) \in V \cap f(A)$, so $V$ intersects $f(A)$.
>
> $(2) \Rightarrow (3)$: Let $B \subseteq Y$ be closed. Let $A = f^{-1}(B)$. By (2), $f(\overline{A}) \subseteq \overline{f(A)} \subseteq \overline{B} = B$ (since $B$ is closed). Thus $\overline{A} \subseteq f^{-1}(B) = A$. Since $A \subseteq \overline{A}$ always, we have $\overline{A} = A$, so $f^{-1}(B)$ is closed.

^pf-9-1

*Uses:* [[§7 Interior and Closure#^thm-7-3|§7.3]], [[§7 Interior and Closure#^lem-7-1|§7.1]]

> [!remark]- Connections
> - Metric spaces: [[§11 Metric Topology#^thm-11-7|ε-δ Characterization of Continuity]], [[§11 Metric Topology#^thm-11-9|Continuity and Sequences]].

## Homeomorphisms

> [!definition] Definition §9.2: Homeomorphism
> Let $f: X \to Y$ be a bijection with inverse $f^{-1}: Y \to X$. If both $f$ and $f^{-1}$ are continuous, then $f$ is called a **homeomorphism**.

^def-9-2

> [!remark]- Connections
> - A shortcut: [[Bijection from Compact to Hausdorff is a Homeomorphism|Bijection from Compact to Hausdorff]].
> - Algebraic analogues: [[§21 Algebra Prerequisites꞉ Groups#^def-21-4|group isomorphism]], [[§10 Invertibility and Isomorphisms#^ladr-3-69|vector space isomorphism]]; see [[§21 Algebra Prerequisites꞉ Groups#^rem-21-7|Analogy: Topology ↔ Algebra]].
> - The smooth analogue: diffeomorphism, [[§18 Smooth Functions and Smooth Maps#^def-18-3|591 Def. §18.3]].

> [!theorem] Proposition §9.2: Equivalent Definition of Homeomorphism
> A bijection $f: X \to Y$ is a homeomorphism if and only if $f(U)$ is open $\Leftrightarrow$ $U$ is open.

^prop-9-2

> [!proof]+ Proof
> $(\Rightarrow)$ Suppose $f$ is a homeomorphism, i.e., $f$ and $f^{-1}$ are both continuous.
>
> If $U \subseteq X$ is open, then since $f^{-1}: Y \to X$ is continuous and $U$ is open, $(f^{-1})^{-1}(U) = f(U)$ is open in $Y$.
>
> If $f(U) \subseteq Y$ is open, then since $f: X \to Y$ is continuous, $f^{-1}(f(U)) = U$ is open in $X$ (using that $f$ is a bijection).
>
> $(\Leftarrow)$ Suppose $f(U)$ is open $\Leftrightarrow$ $U$ is open.
>
> To show $f$ is continuous: Let $V \subseteq Y$ be open. Then $f(f^{-1}(V)) = V$ is open, so by our assumption, $f^{-1}(V)$ is open. Thus $f$ is continuous.
>
> To show $f^{-1}$ is continuous: Let $U \subseteq X$ be open. Then $(f^{-1})^{-1}(U) = f(U)$ is open by assumption. Thus $f^{-1}$ is continuous.

^pf-9-2

> [!remark] Remark
> Homeomorphisms identify open sets: $U$ is open in $X$ if and only if $f(U)$ is open in $Y$. This is why homeomorphic spaces are considered “topologically the same.”

^rem-9-1

> [!remark] Remark: What Homeomorphism Really Means
> A homeomorphism is the topological notion of “sameness”—just as isomorphism is for groups or vector spaces. Two homeomorphic spaces are indistinguishable from the perspective of topology: they have the same open sets, the same convergent sequences, the same compact and connected subsets.
>
> This is the precise version of “rubber sheet geometry”: you can stretch, bend, and deform a space continuously (with a continuous inverse), and topology cannot tell the difference. A coffee mug and a doughnut are homeomorphic; a circle and a line segment are not (removing one point from a circle leaves it connected; removing an interior point from a segment does not).
>
> The central question of topology is: *when are two spaces homeomorphic?* This motivates topological invariants—[[§15 Compact Spaces#^def-15-2|compactness]], [[§13 Connected Spaces#^def-13-1|connectedness]], [[§23 The Fundamental Group#^def-23-2|fundamental groups]]—properties preserved under homeomorphism that can distinguish non-homeomorphic spaces.

^rem-9-2

> [!remark]- Connections
> - Invariance: [[Continuous Image of a Connected Space is Connected|Continuous Image of Connected Space]], [[Continuous Image of a Compact Space is Compact|Continuous Image of Compact is Compact]], [[§23 The Fundamental Group#^cor-23-6|π₁ is a Topological Invariant]].
> - The question it answers: [[§1 Topological Spaces#^rem-1-1|Basic Question]].

> [!example] Example §9.3
> $f: \mathbb{R} \to \mathbb{R}$, $f(x) = 3x + 1$. Homeomorphism. $g(y) = \frac{1}{3}(y-1)$. Easily check $g \circ f(x) = x$, $f \circ g(y) = y$.

^ex-9-3

> [!example] Example §9.4
> $f: (a,b) \to (0,1)$. $f(x) = (x-a) \cdot \frac{1}{b-a}$. $g(y) = (b-a)y + a$. Homeomorphism.

^ex-9-4

> [!theorem] Proposition §9.3: Homeomorphisms Restrict to Subspaces
> Let $f: X \to Y$ be a homeomorphism and $A \subseteq X$. Then $f|_A: A \to f(A)$ is a homeomorphism (with the subspace topologies on $A$ and $f(A)$).

^prop-9-3

> [!proof]+ Proof
> $f|_A$ is a bijection $A \to f(A)$ (restriction of a bijection to a subset). For continuity: $f|_A$ is the restriction of $f$ to $A$, hence continuous ([[§9 Continuous Functions#^thm-9-4|Rule 4]] of Theorem §9.4 below). For the inverse: $(f|_A)^{-1} = (f^{-1})|_{f(A)}$, which is the restriction of $f^{-1}$ to $f(A)$, hence continuous.

^pf-9-3

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]]

> [!remark]- Connections
> - Covering-map analogue: [[§24 Covering Spaces#^thm-24-3|Covering Maps Restrict to Subspaces]].

> [!example] Example §9.5: $\mathbb{C} \cong \mathbb{R}^2$ and the Two Faces of $S^1$
> Define $\phi: \mathbb{C} \to \mathbb{R}^2$ by $\phi(a + bi) = (a, b)$, with inverse $\phi^{-1}(a, b) = a + bi$.
>
> **$\phi$ is a homeomorphism.** Both $\mathbb{C}$ and $\mathbb{R}^2$ are metric spaces, with metrics
>
> $$
> d_{\mathbb{C}}(z_1, z_2) = |z_1 - z_2|, \qquad d_{\mathbb{R}^2}(\mathbf{x}_1, \mathbf{x}_2) = \|\mathbf{x}_1 - \mathbf{x}_2\|.
> $$
>
> Writing $z_j = a_j + b_j i$, we compute directly:
>
> $$
> |z_1 - z_2| = |(a_1 - a_2) + (b_1 - b_2)i| = \sqrt{(a_1-a_2)^2 + (b_1-b_2)^2} = \|\phi(z_1) - \phi(z_2)\|.
> $$
>
> So $d_{\mathbb{R}^2}(\phi(z_1), \phi(z_2)) = d_{\mathbb{C}}(z_1, z_2)$ for all $z_1, z_2$. This means $\phi$ is continuous: given $\varepsilon > 0$, take $\delta = \varepsilon$; then $d_{\mathbb{C}}(z_1, z_2) < \delta$ implies $d_{\mathbb{R}^2}(\phi(z_1), \phi(z_2)) < \varepsilon$. The same $\delta = \varepsilon$ argument applies to $\phi^{-1}$. Since $\phi$ is a continuous bijection with continuous inverse, it is a homeomorphism.
>
> **Restricting to $S^1$.** Since $|z| = 1 \iff a^2 + b^2 = 1$, we have $\phi(S^1_{\mathbb{C}}) = S^1_{\mathbb{R}^2}$. By [[§9 Continuous Functions#^prop-9-3|the restriction proposition]], $\phi|_{S^1}: S^1_{\mathbb{C}} \to S^1_{\mathbb{R}^2}$ is a homeomorphism.
>
> This is why we freely write $S^1$ without specifying the ambient space. In particular, the [[§24 Covering Spaces#^thm-24-2|covering map]] $p(x) = e^{2\pi i x} \in \mathbb{C}$ and $p(x) = (\cos 2\pi x, \sin 2\pi x) \in \mathbb{R}^2$ are the same map under this identification.
>
> **Consequence for $\pi_1$:** Once we compute $\pi_1(S^1_{\mathbb{R}^2}) \cong \mathbb{Z}$ (via the covering map $p: \mathbb{R} \to S^1_{\mathbb{R}^2}$ in [[Fundamental Group of the Circle|§24]]), we get $\pi_1(S^1_{\mathbb{C}}) \cong \mathbb{Z}$ for free: the homeomorphism $\phi$ induces an isomorphism $\phi_{\ast}: \pi_1(S^1_{\mathbb{C}}) \to \pi_1(S^1_{\mathbb{R}^2})$ ([[§23 The Fundamental Group#^cor-23-6|§23]], “$\pi_1$ is a topological invariant”), so $\pi_1(S^1_{\mathbb{C}}) \cong \pi_1(S^1_{\mathbb{R}^2}) \cong \mathbb{Z}$. No separate computation needed.

^ex-9-5

> [!remark]- Connections
> - The transported covering map: [[§24 Covering Spaces#^prop-24-5|Transport of Covering Maps via Homeomorphism]], [[§24 Covering Spaces#^ex-24-4|e^{2πix} as a Transported Covering Map]].

## Rules for Constructing Continuous Functions

> [!theorem] Theorem §9.4: Rules for Continuous Functions
> 1. (Constant) Constant functions are continuous: $f(x) = c$.
> 2. (Inclusion) If $A \subseteq X$, the inclusion $f: A \to X$ is continuous.
> 3. (Composition) Compositions of continuous functions are continuous: $f \circ g$ is continuous if $f, g$ are continuous.
> 4. (Restriction) Restricting the domain: $f$ continuous $\Rightarrow$ $f|_A$ continuous.
> 5. (Restriction/Expansion on range) Let $f: X \to Y$ be continuous. If $Z$ is a subspace of $Y$ with $f(X) \subseteq Z$, then $f$, viewed as a map $X \to Z$, is continuous. If $Z$ is a space having $Y$ as a subspace, then $h: X \to Z$, $h(x) = f(x)$, is continuous.
> 6. (Local formulation of continuity) If $X = \bigcup U_\alpha$ (open in $X$), if $f|_{U_\alpha}$ continuous, then $f$ is continuous.

^thm-9-4

*The lecture omits the proof; see Munkres Theorem 18.2.*

> [!remark]- Connections
> - MATH 451 version of (3): [[§17 Continuous Functions#^thm-17-4|Composition of Continuous Functions]].
> - Maps into products: [[§10 Product Topology on Arbitrary Products#^thm-10-1|Continuity into Product Spaces]].

> [!theorem] Theorem §9.5: Pasting Lemma
> Let $X = A \cup B$, $A, B$ closed. $f: A \to Y$, $g: B \to Y$ continuous, and they agree on $A \cap B$.
>
> Then $h(x) = \begin{cases} f(x) & x \in A \\ g(x) & x \in B \end{cases}$ is continuous.

^thm-9-5

> [!proof]+ Proof
> We use [[Equivalent Conditions for Continuity|criterion (3)]]: $h$ is continuous iff the preimage of every closed set is closed.
>
> Let $C \subseteq Y$ be closed. We show $h^{-1}(C)$ is closed in $X$.
>
> Note that $h^{-1}(C) = \{x \in X : h(x) \in C\} = \{x \in A : f(x) \in C\} \cup \{x \in B : g(x) \in C\} = f^{-1}(C) \cup g^{-1}(C)$.
>
> Since $f: A \to Y$ is continuous and $C$ is closed in $Y$, $f^{-1}(C)$ is closed in $A$. Since $A$ is closed in $X$, by [[§6 Closed Sets and Limit Points#^thm-6-3|Theorem §6.3]], $f^{-1}(C)$ is closed in $X$.
>
> Similarly, $g^{-1}(C)$ is closed in $B$, and since $B$ is closed in $X$, $g^{-1}(C)$ is closed in $X$.
>
> Thus $h^{-1}(C) = f^{-1}(C) \cup g^{-1}(C)$ is a finite union of closed sets, hence closed in $X$.

^pf-9-5

*Uses:* [[§9 Continuous Functions#^thm-9-1|§9.1]], [[§6 Closed Sets and Limit Points#^thm-6-3|§6.3]], [[§6 Closed Sets and Limit Points#^thm-6-1|§6.1]]

> [!example] Example §9.6
> $f_1: [0, \infty) \to \mathbb{R}$, $f_1(x) = x$. $f_2: (-\infty, 0] \to \mathbb{R}$, $f_2(x) = -x$. (Both continuous.) $\Rightarrow$ $f(x) = |x|$ continuous.

^ex-9-6

![[m590-9-2.svg]]
*The pasting lemma for $|x|$: $f_2(x) = -x$ (red) on the closed piece $(-\infty, 0]$ and $f_1(x) = x$ (blue) on the closed piece $[0, \infty)$, which agree on the overlap $\{0\}$. For the closed set $C = [\tfrac12, 1]$, the preimage under the glued map is $f_2^{-1}(C) \cup f_1^{-1}(C) = [-1, -\tfrac12] \cup [\tfrac12, 1]$. Each part is closed in a closed piece, hence closed in $\mathbb{R}$, exactly as in the proof.*
