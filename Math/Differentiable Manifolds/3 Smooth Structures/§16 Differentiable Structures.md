---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 16
tags: [differentiable-manifolds, math591]
---
← [[§15 The Classical Groups]] · ↑ [[· 3 Smooth Structures]] · [[§17 Projective Spaces as Smooth Manifolds]] →

*Stage: foundations — Charts, compatibility, atlases and maximal atlases: what a smooth structure is, for every manifold. The projective spaces get theirs next ([[§17 Projective Spaces as Smooth Manifolds|§17]]), then smooth maps ([[§18 Smooth Functions and Smooth Maps|§18]]).*

*Reference: Lee Ch. 1, “Smooth Structures.” Lecture 5 was given by a substitute; the transcript is poor, so several steps below are reconstructions and are flagged as such.*

> [!remark] Remark: Why This Section
> “We want to describe differentiable manifolds. So we take a topological manifold and decorate it a little.” A topological manifold supports the notion of a *continuous* function and nothing finer; the whole point of a differentiable structure is to make the phrase “$f$ is differentiable” meaningful on an abstract space that has no linear structure of its own. Differentiability could mean $C^1, C^2, \ldots$; **in this course it always means $C^\infty$**, and “smooth” and “differentiable” are used interchangeably. Everything below was previewed in [[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]]; the new content is the compatibility requirement and the bookkeeping (atlases, maximal atlases) needed to make the resulting notion independent of choices.

^rem-16-1

## Smooth Functions Relative to a Chart

> [!definition] Definition §16.1: Chart
> Let $M$ be a topological $n$-manifold. As in [[§2 Topological Manifolds#^def-2-3|Def. §2.3]], a **chart** on $M$ is a pair $(U, \varphi)$ where $U \subseteq M$ is open and $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^n$ is a homeomorphism onto an open subset of $\mathbb{R}^n$. The $n$ component functions of $\varphi$ are the **local coordinates** on $U$.
>
> *Lee: Ch. 1, Coordinate Charts*

^def-16-1

> [!remark]- Connections
> - The same definition, first given for topological manifolds: [[§2 Topological Manifolds#^def-2-3|Def. §2.3]]; restricting and recomposing charts: [[§2 Topological Manifolds#^lem-2-10|§2.10]].
> - Charts of a smooth structure: [[§18 Smooth Functions and Smooth Maps#^def-18-1|Def. §18.1]].

> [!remark] Remark
> Requiring $\varphi(U)$ to be open is not an extra condition: by invariance of domain ([[§2 Topological Manifolds#^thm-2-1|§2.1]] and the discussion there) a continuous injection from an open subset of $\mathbb{R}^n$ into $\mathbb{R}^n$ is automatically open. The lecture stated only “$\varphi$ is a homeomorphism onto its image”; we build openness into the definition to avoid invoking a hard theorem.

^rem-16-2

> [!definition] Definition §16.2: Smooth Function in the Sense of a Chart
> Let $(U, \varphi)$ be a chart on $M$. A function $h : U \to \mathbb{R}$ is **smooth in the sense of $\varphi$** if
>
> $$
> h = f \circ \varphi \quad \text{for some smooth } f : \varphi(U) \to \mathbb{R},
> $$
>
> where “smooth” on the open set $\varphi(U) \subseteq \mathbb{R}^n$ has its usual meaning from multivariable calculus ($C^\infty$: all partial derivatives of all orders exist and are continuous). Since $\varphi$ is a bijection onto $\varphi(U)$, such an $f$ is unique if it exists, namely $f = h \circ \varphi^{-1}$; so the condition may equivalently be stated as
>
> $$
> h \text{ is smooth in the sense of } \varphi \iff h \circ \varphi^{-1} : \varphi(U) \to \mathbb{R} \text{ is smooth.}
> $$
>
> The first form builds $h$ out of a smooth $f$ and is the one used on the board; the second tests $h$ by pushing it to Euclidean space and is Lee's. They say the same thing, and both are used below.
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^def-16-2

> [!remark] Remark: The Problem This Creates
> [[§16 Differentiable Structures#^def-16-2|Def. §16.2]] depends on $\varphi$, not only on $U$. If a point lies in two chart domains $U$ and $V$, there are *two* notions of smoothness available on $U \cap V$, and nothing so far says they agree. That is the question the rest of the subsection answers: “you've got a notion of what it means to be differentiable here, and a notion of what it means to be differentiable there — are they consistent?”

^rem-16-3

## Compatibility of Charts

> [!definition] Definition §16.3: Diffeomorphism of Open Subsets of Euclidean Space
> Let $A, B \subseteq \mathbb{R}^n$ be open. A map $F : A \to B$ is a **diffeomorphism** if it is a bijection and both $F$ and $F^{-1}$ are smooth, and $A$ and $B$ are **diffeomorphic** if such an $F$ exists. (This is the differentiable analogue of a homeomorphism: a smooth bijection whose inverse is also smooth.)
>
> *Lee: Ch. 1, Smooth Structures*

^def-16-3

> [!remark]- Connections
> - The general notion for smooth manifolds: [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]; the two agree by [[§18 Smooth Functions and Smooth Maps#^prop-18-3|§18.3]].
> - The local version: [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]]; detected by the differential via the [[§31 Local Diffeomorphisms#^thm-31-1|inverse function theorem, §31.1]].
> - The $C^1$ version is the class of substitutions in the change of variables formula, [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]].
> - The topological analogue: homeomorphism, [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]].

> [!definition] Definition §16.4: Smoothly Compatible Charts
> Two charts $(U, \varphi)$ and $(V, \psi)$ on $M$ are **$C^\infty$-compatible** if the **transition function**
>
> $$
> \psi \circ \varphi^{-1} : \varphi(U \cap V) \longrightarrow \psi(U \cap V)
> $$
>
> is a diffeomorphism in the sense of [[§16 Differentiable Structures#^def-16-3|Def. §16.3]]. If $U \cap V = \emptyset$ the condition is vacuous and the charts are compatible.
>
> *Lee: Ch. 1, Smooth Structures (“smoothly compatible)*

^def-16-4

> [!remark]- Connections
> - Transition functions were first introduced for topological manifolds: [[§2 Topological Manifolds#^def-2-4|Def. §2.4]].

> [!remark] Remark
> The domain and target are open subsets of $\mathbb{R}^n$, and $\psi \circ \varphi^{-1}$ is automatically a homeomorphism between them — this is [[§2 Topological Manifolds#^prop-2-11|§2.11]] from [[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]], which used nothing but the topological manifold structure. Compatibility asks for the one genuinely new thing: that this homeomorphism and its inverse be $C^\infty$. Note that requiring $\psi\circ\varphi^{-1}$ to be a diffeomorphism is symmetric in the two charts, since $(\psi \circ \varphi^{-1})^{-1} = \varphi \circ \psi^{-1}$.

^rem-16-4

![[m591-8-1.svg]]
*The diagram drawn in lecture. The same function on $U \cap V$ is represented downstairs by $f$ in the $\varphi$-coordinates and by $g$ in the $\psi$-coordinates; the upper triangle says $f \circ \varphi = g \circ \psi$, and the lower triangle says $f = g \circ (\psi \circ \varphi^{-1})$. Compatibility is exactly the statement that the horizontal arrow is a diffeomorphism, which is what lets one pass between $f$ and $g$ without leaving the smooth category.*

> [!definition] Definition §16.5: Regularity Classes of Manifolds
> Nothing in [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], or in the definitions of atlases and maximal atlases that follow, is special to $C^\infty$: the regularity of a manifold is imposed *entirely* through its transition functions. Replacing “smooth” by another class of maps gives:
> - a **$C^k$ manifold**, for a fixed $k \ge 1$: transition functions are $C^k$ with $C^k$ inverses;
> - a **real-analytic manifold**: transition functions are real-analytic — locally given by convergent power series — with real-analytic inverses;
> - a **complex manifold** of complex dimension $n$: charts take values in open subsets of $\mathbb{C}^n$, and transition functions are holomorphic with holomorphic inverses.
>
> From here on, unless stated otherwise, everything in this course is $C^\infty$.
>
> *Lee: Ch. 1, Smooth Structures*

^def-16-5

> [!remark] Remark: Comparing the Classes
> Uribe: “it's all given by what you ask of the transition functions between charts.” Two cautions on how these classes compare, since the lecture's answer to a student's question was explicitly hedged. First, *lowering $k$ gains nothing*: by a theorem of Whitney, every $C^k$ structure with $k \ge 1$ contains a compatible $C^\infty$ structure, unique up to diffeomorphism, so $C^1$ and $C^\infty$ manifolds are the same objects up to isomorphism. What is genuinely different is $C^0$: there exist topological manifolds carrying *no* smooth structure at all. Second, regularity does matter for *theorems about maps*. Sard's theorem — that the set of critical values of $F : \mathbb{R}^N \to \mathbb{R}^m$ has measure zero — requires $F$ to be $C^k$ with $k \ge \max(1, N-m+1)$, and fails for $C^1$ maps otherwise. Real-analytic manifolds are harder to work with for a different reason: $C^\omega$ functions are rigid, so there are no bump functions and hence no partitions of unity, a tool we will rely on constantly.

^rem-16-5

> [!theorem] Theorem §16.1: Compatibility Means the Two Notions Agree
> Let $(U,\varphi)$ and $(V,\psi)$ be charts on $M$ with $U \cap V \neq \emptyset$. The following are equivalent:
> 1. $(U,\varphi)$ and $(V,\psi)$ are $C^\infty$-compatible;
> 2. for every $h : U \cap V \to \mathbb{R}$: $h$ is smooth in the sense of $\varphi$ $\iff$ $h$ is smooth in the sense of $\psi$.

^thm-16-1

> [!proof]+ Proof
> *(Not from lecture; filled in. It reconciles two phrasings: Lecture 5 asked that the transition function be a diffeomorphism, Lecture 6 that the transition functions in both directions be smooth.)* Throughout, write $A = \varphi(U \cap V)$ and $B = \psi(U \cap V)$, both open in $\mathbb{R}^n$, and $\tau = \psi \circ \varphi^{-1} : A \to B$, a homeomorphism with inverse $\tau^{-1} = \varphi \circ \psi^{-1}$.
>
> $(1 \Rightarrow 2)$ Suppose $\tau$ is a diffeomorphism, and let $h = f \circ \varphi$ with $f$ smooth on $A$. Put $g = f \circ \tau^{-1}$, smooth on $B$ as a composite of smooth maps. Then
>
> $$
> g \circ \psi = f \circ \tau^{-1} \circ \psi = f \circ \varphi \circ \psi^{-1} \circ \psi = f \circ \varphi = h,
> $$
>
> so $h$ is smooth in the sense of $\psi$. The converse implication is the same computation with $\tau$ in place of $\tau^{-1}$, using smoothness of $\tau$.
>
> $(2 \Rightarrow 1)$ Apply (2) to the $n$ coordinate functions of $\varphi$. Let $\pi^i : \mathbb{R}^n \to \mathbb{R}$ be the $i$-th coordinate projection and $h_i = \pi^i \circ \varphi$, which is smooth in the sense of $\varphi$ (take $f = \pi^i$). By (2), $h_i = g_i \circ \psi$ for some smooth $g_i$ on $B$, i.e. $g_i = h_i \circ \psi^{-1} = \pi^i \circ \varphi \circ \psi^{-1} = \pi^i \circ \tau^{-1}$. So every component of $\tau^{-1}$ is smooth, hence $\tau^{-1}$ is smooth; symmetrically $\tau$ is smooth. Both being continuous bijections already, $\tau$ is a diffeomorphism.

^pf-16-1

*Uses:* [[§16 Differentiable Structures#^def-16-2|Def. §16.2]], [[§16 Differentiable Structures#^def-16-3|Def. §16.3]], [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark] Remark: The Board Version
> The lecture gave the direction $(1 \Rightarrow 2)$ in the compact form
>
> $$
> f = g \circ (\psi \circ \varphi^{-1}), \qquad \text{equivalently} \qquad f \circ \varphi = g \circ \psi,
> $$
>
> read as: the same function on $U \cap V$ is represented by $f$ in the $\varphi$-coordinates and by $g$ in the $\psi$-coordinates, and the transition function converts one representative into the other. The converse $(2 \Rightarrow 1)$ was not discussed; it is included because it shows compatibility is not merely *sufficient* for the two notions to agree but *necessary* — the definition is not an arbitrarily strong choice.

^rem-16-6

> [!theorem] Proposition §16.2: Compatibility Is Not an Equivalence Relation
> $C^\infty$-compatibility of charts is reflexive and symmetric, but not transitive.
>
> *Lee: cf. Ch. 1, Smooth Structures*

^prop-16-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Reflexive:* the transition function of a chart with itself is the identity. *Symmetric:* the transition function in the other direction is the inverse diffeomorphism. *Not transitive:* on $M = \mathbb{R}$ let $\varphi_1 = \mathrm{id}$ on $U_1 = \mathbb{R}$, $\varphi_2 = \mathrm{id}$ on $U_2 = (0,\infty)$, and $\varphi_3(t) = t^3$ on $U_3 = \mathbb{R}$. Then $(U_1,\varphi_1)$ and $(U_2,\varphi_2)$ are compatible, and so are $(U_2,\varphi_2)$ and $(U_3,\varphi_3)$, since on $(0,\infty)$ the transition $t \mapsto t^{1/3}$ is smooth with smooth inverse. But $(U_1,\varphi_1)$ and $(U_3,\varphi_3)$ are not: the transition $\varphi_1 \circ \varphi_3^{-1}(t) = t^{1/3}$ fails to be differentiable at $0$.

^pf-16-2

*Uses:* [[§16 Differentiable Structures#^def-16-3|Def. §16.3]], [[§16 Differentiable Structures#^def-16-4|Def. §16.4]]

> [!remark] Remark
> This is exactly why [[§16 Differentiable Structures#^thm-16-5|§16.5]] below cannot be proved by “collect all charts compatible with a given one.” The chart $(U_2,\varphi_2)$ is compatible with both of two charts that are incompatible with each other.

^rem-16-7

## Atlases

> [!definition] Definition §16.6: Atlas
> An **atlas** on a topological $n$-manifold $M$ is a collection $\mathcal{A} = \{(U_i, \varphi_i)\}_{i \in I}$ of pairwise $C^\infty$-compatible charts with $\bigcup_{i} U_i = M$.
>
> *Lee: Ch. 1, Smooth Structures (“smooth atlas)*

^def-16-6

> [!example] Example §16.1: Euclidean Space
> $\mathbb{R}^n$ has the one-chart atlas $\{(\mathbb{R}^n, \mathrm{id})\}$. More generally any open $A \subseteq \mathbb{R}^n$ has the atlas $\{(A, \mathrm{id})\}$. A single chart is automatically an atlas: compatibility with itself is the statement that $\mathrm{id}$ is a diffeomorphism.
>
> *Lee: Example 1.22*

^ex-16-1

*Uses:* [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§16 Differentiable Structures#^def-16-6|Def. §16.6]]

> [!example] Example §16.2: The Four-Chart Atlas on the Circle
> Let $S^1 = \{(x,y) \in \mathbb{R}^2 \mid x^2 + y^2 = 1\}$ and cut it along the axes into four open half-circles, each projected onto the axis it is a graph over:
>
> $$
> \begin{array}{llll}
> U_1 = \{x > 0\}, & \varphi_1(x,y) = y; \qquad & U_3 = \{x < 0\}, & \varphi_3(x,y) = y;\\
> U_2 = \{y > 0\}, & \varphi_2(x,y) = x; & U_4 = \{y < 0\}, & \varphi_4(x,y) = x.
> \end{array}
> $$
>
> Each $\varphi_i$ is a homeomorphism onto $(-1,1)$, with inverse given by solving $x^2 + y^2 = 1$ for the missing coordinate with the sign determined by the half-circle: e.g. $\varphi_1^{-1}(y) = (\sqrt{1-y^2},\, y)$ and $\varphi_4^{-1}(x) = (x,\, -\sqrt{1-x^2})$. The four sets cover $S^1$, so this is an atlas once compatibility is checked.
>
> *Transition functions.* $U_1 \cap U_3 = \emptyset = U_2 \cap U_4$, so those two pairs are vacuously compatible. The four remaining overlaps are the open quadrant arcs, and on each the transition is the map that solves for the other coordinate:
>
> $$
> \varphi_2 \circ \varphi_1^{-1}(y) = \sqrt{1-y^2} \ \text{ on } (0,1), \qquad
> \varphi_3 \circ \varphi_2^{-1}(x) = \sqrt{1-x^2} \ \text{ on } (-1,0),
> $$
>
> $$
> \varphi_4 \circ \varphi_3^{-1}(y) = -\sqrt{1-y^2} \ \text{ on } (-1,0), \qquad
> \varphi_1 \circ \varphi_4^{-1}(x) = -\sqrt{1-x^2} \ \text{ on } (0,1).
> $$
>
> Each is smooth on its (open) domain, because $1 - t^2 > 0$ there, and each is its own inverse up to sign, so all four are diffeomorphisms. Hence $\{(U_i, \varphi_i)\}_{i=1}^4$ is an atlas.
>
> *Lee: Examples 1.4 and 1.31*

^ex-16-2

*Uses:* [[§16 Differentiable Structures#^def-16-1|Def. §16.1]], [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§16 Differentiable Structures#^def-16-6|Def. §16.6]]

> [!remark]- Connections
> - The circle as a level set, and the implicit function theorem solving for $y$ (452): [[Unit circle and unit sphere]].
> - The same charts as graph charts of a regular level set: [[§19 Manifolds in Euclidean Space#^ex-19-1|Ex. §19.1]]; all three circle atlases give one structure: [[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]].

The board wrote “$x^2 + y^2 = 0$” when setting up the first transition function; the equation of the circle is of course $x^2 + y^2 = 1$. The sign in each transition function is dictated by the quadrant — this is what the lecture meant by “sometimes the square root is positive, sometimes negative; look at the picture to see where you are.” Note also that $\sqrt{1-t^2}$ is *not* smooth at $t = \pm 1$; it does not need to be, because those values are not in the domain of any transition function. Cutting at the axes is exactly what keeps the bad points out.

![[m591-8-2.svg]]
*Left: the four half-circles, drawn at staggered radii so the overlaps are visible. $U_1$ and $U_3$ never meet, nor do $U_2$ and $U_4$; the four nonempty overlaps are the open quadrant arcs, where consecutive colors run alongside each other. Right: the chart $\varphi_2$ on the upper half-circle is vertical projection onto the $x$-axis, a homeomorphism onto $(-1,1)$. Each of the four charts is a projection onto the axis its half-circle is a graph over, which is why the transition functions come out as $\pm\sqrt{1-t^2}$.*

> [!theorem] Proposition §16.3: The Circle Needs More Than One Chart
> There is no atlas on $S^1$ consisting of a single chart; that is, $S^1$ is not homeomorphic to an open subset of $\mathbb{R}$.

^prop-16-3

> [!proof]+ Proof
> *(Lecture 5 gave the reason: an open subset of $\mathbb{R}$ cannot be homeomorphic to the compact circle; filled in.)* Suppose $\varphi : S^1 \to \varphi(S^1) \subseteq \mathbb{R}$ were such a chart. Then $\varphi(S^1)$ is open by [[§16 Differentiable Structures#^def-16-1|Def. §16.1]], and compact as the continuous image of the compact space $S^1$ ([[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1) gives compactness of $S^1$, closed and bounded in $\mathbb{R}^2$; (2) gives compactness of the image). A compact subset of the Hausdorff space $\mathbb{R}$ is closed ([[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4)), so $\varphi(S^1)$ is a nonempty subset of $\mathbb{R}$ that is both open and closed. Since $\mathbb{R}$ is connected, $\varphi(S^1) = \mathbb{R}$ — which is not compact. Contradiction.

^pf-16-3

*Uses:* [[§16 Differentiable Structures#^def-16-1|Def. §16.1]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §18.12 (Heine–Borel)]], [[Continuous Image of a Compact Space is Compact|590 §18.3]], [[Compact Subspace of a Hausdorff Space is Closed|590 §18.4]], [[§15 Connected Spaces#^lem-15-1|590 §15.1]], [[§16 Connected Subspaces of ℝ#^cor-16-2|590 §16.2]]

> [!remark] Remark
> “It is absolutely essential to break the circle into charts.” The obstruction is global (compactness), not local: every point of $S^1$ has arbitrarily small neighborhoods that are perfectly good chart domains. A student asked which open sets can serve; the answer is the next proposition.

^rem-16-8

> [!example] Example §16.3: Stereographic Atlas on the Circle
> Let $N = (0,1)$ and $S = (0,-1)$ be the north and south poles. For $P \in S^1 \setminus \{N\}$, the line through $N$ and $P$ meets the $x$-axis in exactly one point; sending $P$ to that point defines
>
> $$
> \sigma_N : S^1 \setminus \{N\} \to \mathbb{R}, \quad \sigma_N(x,y) = \frac{x}{1-y}, \qquad
> \sigma_S : S^1 \setminus \{S\} \to \mathbb{R}, \quad \sigma_S(x,y) = \frac{x}{1+y}.
> $$
>
> Both are homeomorphisms onto $\mathbb{R}$, with $\sigma_N^{-1}(u) = \left( \frac{2u}{u^2+1},\, \frac{u^2-1}{u^2+1} \right)$. The two domains cover $S^1$, their intersection is $S^1 \setminus \{N, S\}$, and
>
> $$
> \sigma_S \circ \sigma_N^{-1}(u) = \frac{2u/(u^2+1)}{1 + (u^2-1)/(u^2+1)} = \frac{2u}{2u^2} = \frac{1}{u},
> $$
>
> a diffeomorphism of $\mathbb{R} \setminus \{0\}$ onto itself. So $\{(S^1 \setminus \{N\}, \sigma_N), (S^1 \setminus \{S\}, \sigma_S)\}$ is an atlas with only two charts. (“It is going to be a rational function”: here $u \mapsto 1/u$.) Consistently with [[§16 Differentiable Structures#^prop-16-3|§16.3]], two is the minimum.
>
> *Lee: Problem 1-7*

^ex-16-3

*Uses:* [[§16 Differentiable Structures#^def-16-1|Def. §16.1]], [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§16 Differentiable Structures#^def-16-6|Def. §16.6]]

> [!remark]- Connections
> - Compatible with the other two circle atlases: [[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]]; the complex counterpart $w \mapsto 1/w$ on $\mathbb{CP}^1$: [[§17 Projective Spaces as Smooth Manifolds#^rem-17-2|Remark after §17.4]].
> - Stereographic projection in 590: it identifies S¹ with the one-point compactification of ℝ, [[§20 Local Compactness#^ex-20-7|590 Ex. §20.7]], and Sⁿ minus a point with ℝⁿ in the proof that Sⁿ is simply connected, [[§37 The Fundamental Group of Sⁿ#^pf-37-3|590 §37, proof of Thm. §27.3]].

![[m591-8-3.svg]]
*Left, $\sigma_N$: the line from $N$ through a point $P$ of the circle meets the horizontal axis at $\sigma_N(P)$. Right, $\sigma_S$: the same construction from the south pole.*

The hollow circle marks the pole each chart *omits*: $\sigma_N$ is undefined at $N$, since the line through $N$ and $N$ is not determined, and as $P$ climbs towards $N$ the image $\sigma_N(P)$ runs off to $\pm\infty$. Every other point is hit exactly once, so $\sigma_N$ is a bijection onto all of $\mathbb{R}$.

The vertical ray is the case $P = S$: the line through $N$ and $S$ meets the axis at the origin, so $\sigma_N(S) = 0/(1-(-1)) = 0$, and by symmetry $\sigma_S(N) = 0$. The two charts are mirror images in this respect — $\sigma_N$ compresses the *lower* half-circle into $(-1,1)$ and throws the upper half outside it, while $\sigma_S$ does the reverse. On the overlap $S^1 \setminus \{N,S\}$ this exchange of inside and outside is exactly the transition function $u \mapsto 1/u$.

> [!theorem] Proposition §16.4: Chart Domains on the Circle
> A connected open subset $V \subseteq S^1$ is the domain of a chart if and only if $V \ne S^1$. Every such $V$ is an open arc, homeomorphic to an open interval.

^prop-16-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $V \ne S^1$, pick $q \notin V$ and a rotation $\rho$ of $S^1$ with $\rho(q) = N$. The stereographic projection $\sigma_N : S^1 \setminus \{N\} \to \mathbb{R}$ of [[§16 Differentiable Structures#^ex-16-3|Ex. §16.3]] above is a homeomorphism, so $\sigma_N \circ \rho$ maps $V$ homeomorphically onto a connected open subset of $\mathbb{R}$, which is an open interval; this is a chart. Conversely, $S^1$ is not a chart domain, by [[§16 Differentiable Structures#^prop-16-3|§16.3]].

^pf-16-4

*Uses:* [[§16 Differentiable Structures#^ex-16-3|Ex. §16.3]], [[§16 Differentiable Structures#^prop-16-3|§16.3]], [[§16 Differentiable Structures#^def-16-1|Def. §16.1]], [[Continuous Image of a Connected Space is Connected|590 §15.3]], [[§16 Connected Subspaces of ℝ#^rem-16-1|590 §16 (connected subsets of ℝ are intervals)]]

> [!example] Example §16.4: Angle Atlas on the Circle
> Parametrize by angle, which cannot be done globally — the same meta-principle — so use two overlapping ranges:
>
> $$
> \begin{aligned}
> U_a &= S^1 \setminus \{(1,0)\}, & \varphi_a(\cos\theta, \sin\theta) &= \theta \in (0, 2\pi); \\
> U_b &= S^1 \setminus \{(-1,0)\}, & \varphi_b(\cos\theta, \sin\theta) &= \theta \in (\pi, 3\pi).
> \end{aligned}
> $$
>
> Here $U_a \cap U_b$ is the union of the open upper and lower half-circles, $\varphi_a(U_a \cap U_b) = (0,\pi) \cup (\pi, 2\pi)$, and
>
> $$
> \varphi_b \circ \varphi_a^{-1}(\theta) = \begin{cases} \theta + 2\pi, & \theta \in (0,\pi), \\ \theta, & \theta \in (\pi, 2\pi), \end{cases}
> $$
>
> a translation on each component of its domain, hence a diffeomorphism. A parametrization is just the inverse of a chart — “putting labels on points” — so the two descriptions carry the same information.

^ex-16-4

*Uses:* [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§16 Differentiable Structures#^def-16-6|Def. §16.6]]

> [!remark]- Connections
> - Polar angle as a coordinate (452): [[Polar and spherical coordinates]]; parametrizations as inverse charts: [[§19 Manifolds in Euclidean Space#^rem-19-2|§19, Remark: A Parametrization Is an Inverse Chart]].

> [!remark] Remark: Three Atlases and One Structure
> $S^1$ thus carries at least three different atlases. They are not competing structures: every chart of one is compatible with every chart of another, so they determine the *same* smooth structure. This is proved in [[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]], once regular level sets are available. For instance, on the arc where $U_2$ (upper half, coordinate $x$) meets $U_a$ the transition is $\theta \mapsto \cos\theta$ with inverse $x \mapsto \arccos x$, and $\sigma_N \circ \varphi_2^{-1}(x) = x/(1 - \sqrt{1-x^2})$ is smooth on $(-1,0) \cup (0,1)$. “Which atlas you write down is a matter of convenience” — what is intrinsic is the maximal atlas they all generate.

^rem-16-9

## Maximal Atlases and Smooth Structures

> [!definition] Definition §16.7: Compatible Atlases
> Two atlases $\mathcal{A}, \mathcal{A}'$ on $M$ are **$C^\infty$-compatible** if every chart of $\mathcal{A}$ is $C^\infty$-compatible with every chart of $\mathcal{A}'$; equivalently, if $\mathcal{A} \cup \mathcal{A}'$ is again an atlas.
>
> *Lee: Proposition 1.17(b)*

^def-16-7

> [!definition] Definition §16.8: Maximal Atlas
> An atlas $\mathcal{A}$ is **maximal** if every chart compatible with all the charts of $\mathcal{A}$ already belongs to $\mathcal{A}$. Equivalently, $\mathcal{A}$ is contained in no strictly larger atlas.
>
> *Lee: Ch. 1, Smooth Structures*

^def-16-8

> [!theorem] Theorem §16.5: Every Atlas Lies in a Unique Maximal Atlas
> Let $\mathcal{A}$ be an atlas on $M$ and let
>
> $$
> \overline{\mathcal{A}} = \{\, (V, \psi) \text{ a chart on } M \mid (V,\psi) \text{ is compatible with every chart of } \mathcal{A} \,\}.
> $$
>
> Then $\overline{\mathcal{A}}$ is the unique maximal atlas containing $\mathcal{A}$. Consequently two atlases are compatible if and only if they are contained in the same maximal atlas.
>
> *Lee: Proposition 1.17(a)*

^thm-16-5

> [!proof]+ Proof
> *$\overline{\mathcal{A}}$ is an atlas.* *(Lecture 6's sketch, completed.)* It contains $\mathcal{A}$ (whose charts are pairwise compatible), so its domains cover $M$. The content is that any two of its charts are compatible with *each other* — which does not follow formally, compatibility not being transitive. Let $(V,\psi), (W,\chi) \in \overline{\mathcal{A}}$; we show $\chi \circ \psi^{-1}$ is smooth on $\psi(V \cap W)$. Smoothness is a local property, so it suffices to prove it near each point $\psi(p)$, $p \in V \cap W$. Choose $(U,\varphi) \in \mathcal{A}$ with $p \in U$, possible since $\mathcal{A}$ covers $M$. On the open set $\psi(U \cap V \cap W) \ni \psi(p)$,
>
> $$
> \chi \circ \psi^{-1} = (\chi \circ \varphi^{-1}) \circ (\varphi \circ \psi^{-1}),
> $$
>
> and both factors are smooth because $(U,\varphi)$ is compatible with each of $(W,\chi)$ and $(V,\psi)$ — this factorization is the “little bit of diagram chasing” of the lecture. Hence $\chi \circ \psi^{-1}$ is smooth near $\psi(p)$. As $p$ was arbitrary it is smooth on all of $\psi(V\cap W)$, and exchanging the roles of the two charts gives smoothness of the inverse.
>
> *$\overline{\mathcal{A}}$ is maximal.* If a chart $(V,\psi)$ is compatible with every chart of $\overline{\mathcal{A}}$, then in particular with every chart of $\mathcal{A} \subseteq \overline{\mathcal{A}}$, so $(V,\psi) \in \overline{\mathcal{A}}$ by definition.
>
> *Uniqueness.* Let $\mathcal{M}$ be any maximal atlas with $\mathcal{A} \subseteq \mathcal{M}$. If $(V,\psi) \in \mathcal{M}$ then it is compatible with every chart of $\mathcal{M}$, hence with every chart of $\mathcal{A}$, so $(V,\psi) \in \overline{\mathcal{A}}$; thus $\mathcal{M} \subseteq \overline{\mathcal{A}}$. Since $\overline{\mathcal{A}}$ is an atlas containing $\mathcal{M}$ and $\mathcal{M}$ is maximal, $\mathcal{M} = \overline{\mathcal{A}}$.

^pf-16-5

*Uses:* [[§16 Differentiable Structures#^def-16-4|Def. §16.4]], [[§16 Differentiable Structures#^def-16-6|Def. §16.6]], [[§16 Differentiable Structures#^def-16-7|Def. §16.7]], [[§16 Differentiable Structures#^def-16-8|Def. §16.8]], [[§16 Differentiable Structures#^prop-16-2|§16.2]], [[Multivariable Chain Rule|452 §12.2]]

Lecture 5 argued uniqueness only (“anything in one is contained in the other, so they are equal”), taking for granted that the collection of all compatible charts is an atlas. Lecture 6 returned to the lemma: Uribe defined $\overline{\mathcal{A}}$ as above, called maximality “not that hard” and the atlas property “more substantial”, and sketched it — a point of the overlap lies in some chart of $\mathcal{A}$, compatible with both charts, “and then you have to do a little bit of diagram chasing” — skipping the details for time. The proof above completes that sketch. That step is the one with content, and the [[§16 Differentiable Structures#^rem-16-7|remark on non-transitivity above]] shows it really needs the mediating chart $(U,\varphi) \in \mathcal{A}$: without an atlas to pass through, pairwise compatibility with a single chart proves nothing. Compare Lee, Proposition 1.17.

> [!definition] Definition §16.9: Smooth Manifold Structure
> A **differentiable (smooth) structure** on a topological manifold $M$ is a maximal atlas $\mathcal{A}$ on $M$. A **smooth manifold** is a pair $\mathcal{M} = (M, \mathcal{A})$. By [[§16 Differentiable Structures#^thm-16-5|§16.5]], specifying any atlas specifies a smooth structure, and two atlases specify the same structure exactly when they are compatible.
>
> *Lee: Ch. 1, Smooth Structures*

^def-16-9

> [!remark] Remark: On the Connectedness Assumption
> The board wrote “let $M$ be a topological manifold (connected).” Nothing in this section uses connectedness, and the definitions above are stated without it. It is a harmless convenience — with $n$ fixed in advance ([[§2 Topological Manifolds#^def-2-2|Def. §2.2]]) the dimension is already constant — and it can be dropped. It does matter under the convention where $n$ is allowed to vary with the point ([[§2 Topological Manifolds#^cor-2-2|§2.2]]).

^rem-16-10
