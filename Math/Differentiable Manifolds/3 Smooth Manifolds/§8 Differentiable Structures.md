---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 8
tags: [differentiable-manifolds, math591]
---
← [[§7 Homogeneous Spaces]] · ↑ [[3 Smooth Manifolds]] · [[§9 Manifolds in Euclidean Space]] →

*Stage: foundations — Charts, atlases and smooth maps, for every smooth manifold. The quotient-built manifolds get their smooth structures here, from atlases written down by hand ([[§8 Differentiable Structures#Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]).*

*Reference: Lee Ch. 1, “Smooth Structures.” Lecture 5 was given by a substitute; the transcript is poor, so several steps below are reconstructions and are flagged as such.*

> [!remark] Remark: Why This Section
> “We want to describe differentiable manifolds. So we take a topological manifold and decorate it a little.” A topological manifold supports the notion of a *continuous* function and nothing finer; the whole point of a differentiable structure is to make the phrase “$f$ is differentiable” meaningful on an abstract space that has no linear structure of its own. Differentiability could mean $C^1, C^2, \ldots$; **in this course it always means $C^\infty$**, and “smooth” and “differentiable” are used interchangeably. Everything below was previewed in [[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]]; the new content is the compatibility requirement and the bookkeeping (atlases, maximal atlases) needed to make the resulting notion independent of choices.

^rem-8-1

## Smooth Functions Relative to a Chart

> [!definition] Definition §8.1: Chart
> Let $M$ be a topological $n$-manifold. As in [[§2 Topological Manifolds#^def-2-3|Def. §2.3]], a **chart** on $M$ is a pair $(U, \varphi)$ where $U \subseteq M$ is open and $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^n$ is a homeomorphism onto an open subset of $\mathbb{R}^n$. The $n$ component functions of $\varphi$ are the **local coordinates** on $U$.
>
> *Lee: Ch. 1, Coordinate Charts*

^def-8-1

> [!remark]- Connections
> - The same definition, first given for topological manifolds: [[§2 Topological Manifolds#^def-2-3|Def. §2.3]]; restricting and recomposing charts: [[§2 Topological Manifolds#^lem-2-11|§2.11]].
> - Charts of a smooth structure: [[§8 Differentiable Structures#^def-8-12|Def. §8.12]].

> [!remark] Remark
> Requiring $\varphi(U)$ to be open is not an extra condition: by invariance of domain ([[§2 Topological Manifolds#^thm-2-1|§2.1]] and the discussion there) a continuous injection from an open subset of $\mathbb{R}^n$ into $\mathbb{R}^n$ is automatically open. The lecture stated only “$\varphi$ is a homeomorphism onto its image”; we build openness into the definition to avoid invoking a hard theorem.

^rem-8-2

> [!definition] Definition §8.2: Smooth Function in the Sense of a Chart
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

^def-8-2

> [!remark] Remark: The Problem This Creates
> [[§8 Differentiable Structures#^def-8-2|Def. §8.2]] depends on $\varphi$, not only on $U$. If a point lies in two chart domains $U$ and $V$, there are *two* notions of smoothness available on $U \cap V$, and nothing so far says they agree. That is the question the rest of the subsection answers: “you've got a notion of what it means to be differentiable here, and a notion of what it means to be differentiable there — are they consistent?”

^rem-8-3

## Compatibility of Charts

> [!definition] Definition §8.3: Diffeomorphism of Open Subsets of Euclidean Space
> Let $A, B \subseteq \mathbb{R}^n$ be open. A map $F : A \to B$ is a **diffeomorphism** if it is a bijection and both $F$ and $F^{-1}$ are smooth, and $A$ and $B$ are **diffeomorphic** if such an $F$ exists. (This is the differentiable analogue of a homeomorphism: a smooth bijection whose inverse is also smooth.)
>
> *Lee: Ch. 1, Smooth Structures*

^def-8-3

> [!remark]- Connections
> - The general notion for smooth manifolds: [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]; the two agree by [[§8 Differentiable Structures#^prop-8-14|§8.14]].
> - The local version: [[§14 Local Diffeomorphisms and Submersions#^def-14-1|Def. §14.1]]; detected by the differential via the [[Inverse Function Theorem (several variables)|inverse function theorem (452 §13)]].

> [!definition] Definition §8.4: Smoothly Compatible Charts
> Two charts $(U, \varphi)$ and $(V, \psi)$ on $M$ are **$C^\infty$-compatible** if the **transition function**
>
> $$
> \psi \circ \varphi^{-1} : \varphi(U \cap V) \longrightarrow \psi(U \cap V)
> $$
>
> is a diffeomorphism in the sense of [[§8 Differentiable Structures#^def-8-3|Def. §8.3]]. If $U \cap V = \emptyset$ the condition is vacuous and the charts are compatible.
>
> *Lee: Ch. 1, Smooth Structures (“smoothly compatible)*

^def-8-4

> [!remark]- Connections
> - Transition functions were first introduced for topological manifolds: [[§2 Topological Manifolds#^def-2-4|Def. §2.4]].

> [!remark] Remark
> The domain and target are open subsets of $\mathbb{R}^n$, and $\psi \circ \varphi^{-1}$ is automatically a homeomorphism between them — this is [[§2 Topological Manifolds#^prop-2-12|§2.12]] from [[§2 Topological Manifolds#Charts and Transition Functions|§2, Charts and Transition Functions]], which used nothing but the topological manifold structure. Compatibility asks for the one genuinely new thing: that this homeomorphism and its inverse be $C^\infty$. Note that requiring $\psi\circ\varphi^{-1}$ to be a diffeomorphism is symmetric in the two charts, since $(\psi \circ \varphi^{-1})^{-1} = \varphi \circ \psi^{-1}$.

^rem-8-4

![[m591-8-1.svg]]
*The diagram drawn in lecture. The same function on $U \cap V$ is represented downstairs by $f$ in the $\varphi$-coordinates and by $g$ in the $\psi$-coordinates; the upper triangle says $f \circ \varphi = g \circ \psi$, and the lower triangle says $f = g \circ (\psi \circ \varphi^{-1})$. Compatibility is exactly the statement that the horizontal arrow is a diffeomorphism, which is what lets one pass between $f$ and $g$ without leaving the smooth category.*

> [!definition] Definition §8.5: Regularity Classes of Manifolds
> Nothing in [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], or in the definitions of atlases and maximal atlases that follow, is special to $C^\infty$: the regularity of a manifold is imposed *entirely* through its transition functions. Replacing “smooth” by another class of maps gives:
> - a **$C^k$ manifold**, for a fixed $k \ge 1$: transition functions are $C^k$ with $C^k$ inverses;
> - a **real-analytic manifold**: transition functions are real-analytic — locally given by convergent power series — with real-analytic inverses;
> - a **complex manifold** of complex dimension $n$: charts take values in open subsets of $\mathbb{C}^n$, and transition functions are holomorphic with holomorphic inverses.
>
> From here on, unless stated otherwise, everything in this course is $C^\infty$.
>
> *Lee: Ch. 1, Smooth Structures*

^def-8-5

> [!remark] Remark: Comparing the Classes
> Uribe: “it's all given by what you ask of the transition functions between charts.” Two cautions on how these classes compare, since the lecture's answer to a student's question was explicitly hedged. First, *lowering $k$ gains nothing*: by a theorem of Whitney, every $C^k$ structure with $k \ge 1$ contains a compatible $C^\infty$ structure, unique up to diffeomorphism, so $C^1$ and $C^\infty$ manifolds are the same objects up to isomorphism. What is genuinely different is $C^0$: there exist topological manifolds carrying *no* smooth structure at all. Second, regularity does matter for *theorems about maps*. Sard's theorem — that the set of critical values of $F : \mathbb{R}^N \to \mathbb{R}^m$ has measure zero — requires $F$ to be $C^k$ with $k \ge \max(1, N-m+1)$, and fails for $C^1$ maps otherwise. Real-analytic manifolds are harder to work with for a different reason: $C^\omega$ functions are rigid, so there are no bump functions and hence no partitions of unity, a tool we will rely on constantly.

^rem-8-5

> [!theorem] Theorem §8.1: Compatibility Means the Two Notions Agree
> Let $(U,\varphi)$ and $(V,\psi)$ be charts on $M$ with $U \cap V \neq \emptyset$. The following are equivalent:
> 1. $(U,\varphi)$ and $(V,\psi)$ are $C^\infty$-compatible;
> 2. for every $h : U \cap V \to \mathbb{R}$: $h$ is smooth in the sense of $\varphi$ $\iff$ $h$ is smooth in the sense of $\psi$.

^thm-8-1

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

^pf-8-1

*Uses:* [[§8 Differentiable Structures#^def-8-2|Def. §8.2]], [[§8 Differentiable Structures#^def-8-3|Def. §8.3]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark] Remark: The Board Version
> The lecture gave the direction $(1 \Rightarrow 2)$ in the compact form
>
> $$
> f = g \circ (\psi \circ \varphi^{-1}), \qquad \text{equivalently} \qquad f \circ \varphi = g \circ \psi,
> $$
>
> read as: the same function on $U \cap V$ is represented by $f$ in the $\varphi$-coordinates and by $g$ in the $\psi$-coordinates, and the transition function converts one representative into the other. The converse $(2 \Rightarrow 1)$ was not discussed; it is included because it shows compatibility is not merely *sufficient* for the two notions to agree but *necessary* — the definition is not an arbitrarily strong choice.

^rem-8-6

> [!theorem] Proposition §8.2: Compatibility Is Not an Equivalence Relation
> $C^\infty$-compatibility of charts is reflexive and symmetric, but not transitive.
>
> *Lee: cf. Ch. 1, Smooth Structures*

^prop-8-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Reflexive:* the transition function of a chart with itself is the identity. *Symmetric:* the transition function in the other direction is the inverse diffeomorphism. *Not transitive:* on $M = \mathbb{R}$ let $\varphi_1 = \mathrm{id}$ on $U_1 = \mathbb{R}$, $\varphi_2 = \mathrm{id}$ on $U_2 = (0,\infty)$, and $\varphi_3(t) = t^3$ on $U_3 = \mathbb{R}$. Then $(U_1,\varphi_1)$ and $(U_2,\varphi_2)$ are compatible, and so are $(U_2,\varphi_2)$ and $(U_3,\varphi_3)$, since on $(0,\infty)$ the transition $t \mapsto t^{1/3}$ is smooth with smooth inverse. But $(U_1,\varphi_1)$ and $(U_3,\varphi_3)$ are not: the transition $\varphi_1 \circ \varphi_3^{-1}(t) = t^{1/3}$ fails to be differentiable at $0$.

^pf-8-2

*Uses:* [[§8 Differentiable Structures#^def-8-3|Def. §8.3]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]]

> [!remark] Remark
> This is exactly why [[§8 Differentiable Structures#^thm-8-5|§8.5]] below cannot be proved by “collect all charts compatible with a given one.” The chart $(U_2,\varphi_2)$ is compatible with both of two charts that are incompatible with each other.

^rem-8-7

## Atlases

> [!definition] Definition §8.6: Atlas
> An **atlas** on a topological $n$-manifold $M$ is a collection $\mathcal{A} = \{(U_i, \varphi_i)\}_{i \in I}$ of pairwise $C^\infty$-compatible charts with $\bigcup_{i} U_i = M$.
>
> *Lee: Ch. 1, Smooth Structures (“smooth atlas)*

^def-8-6

> [!example] Example §8.1: Euclidean Space
> $\mathbb{R}^n$ has the one-chart atlas $\{(\mathbb{R}^n, \mathrm{id})\}$. More generally any open $A \subseteq \mathbb{R}^n$ has the atlas $\{(A, \mathrm{id})\}$. A single chart is automatically an atlas: compatibility with itself is the statement that $\mathrm{id}$ is a diffeomorphism.
>
> *Lee: Example 1.22*

^ex-8-1

> [!example] Example §8.2: The Four-Chart Atlas on the Circle
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

^ex-8-2

> [!remark]- Connections
> - The circle as a level set, and the implicit function theorem solving for $y$ (452): [[Unit circle and unit sphere]].
> - The same charts as graph charts of a regular level set: [[§9 Manifolds in Euclidean Space#^ex-9-1|Ex. §9.1]]; all three circle atlases give one structure: [[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]].

The board wrote “$x^2 + y^2 = 0$” when setting up the first transition function; the equation of the circle is of course $x^2 + y^2 = 1$. The sign in each transition function is dictated by the quadrant — this is what the lecture meant by “sometimes the square root is positive, sometimes negative; look at the picture to see where you are.” Note also that $\sqrt{1-t^2}$ is *not* smooth at $t = \pm 1$; it does not need to be, because those values are not in the domain of any transition function. Cutting at the axes is exactly what keeps the bad points out.

![[m591-8-2.svg]]
*Left: the four half-circles, drawn at staggered radii so the overlaps are visible. $U_1$ and $U_3$ never meet, nor do $U_2$ and $U_4$; the four nonempty overlaps are the open quadrant arcs, where consecutive colors run alongside each other. Right: the chart $\varphi_2$ on the upper half-circle is vertical projection onto the $x$-axis, a homeomorphism onto $(-1,1)$. Each of the four charts is a projection onto the axis its half-circle is a graph over, which is why the transition functions come out as $\pm\sqrt{1-t^2}$.*

> [!theorem] Proposition §8.3: The Circle Needs More Than One Chart
> There is no atlas on $S^1$ consisting of a single chart; that is, $S^1$ is not homeomorphic to an open subset of $\mathbb{R}$.

^prop-8-3

> [!proof]+ Proof
> *(Lecture 5 gave the reason: an open subset of $\mathbb{R}$ cannot be homeomorphic to the compact circle; filled in.)* Suppose $\varphi : S^1 \to \varphi(S^1) \subseteq \mathbb{R}$ were such a chart. Then $\varphi(S^1)$ is open by [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], and compact as the continuous image of the compact space $S^1$ ([[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1) gives compactness of $S^1$, closed and bounded in $\mathbb{R}^2$; (2) gives compactness of the image). A compact subset of the Hausdorff space $\mathbb{R}$ is closed ([[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4)), so $\varphi(S^1)$ is a nonempty subset of $\mathbb{R}$ that is both open and closed. Since $\mathbb{R}$ is connected, $\varphi(S^1) = \mathbb{R}$ — which is not compact. Contradiction.

^pf-8-3

*Uses:* [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]], [[Continuous Image of a Compact Space is Compact|590 §15.3]], [[Compact Subspace of a Hausdorff Space is Closed|590 §15.4]], [[§13 Connected Spaces#^lem-13-1|590 §13.1]], [[§14 Connected Subspaces of ℝ#^cor-14-2|590 §14.2]]

> [!remark] Remark
> “It is absolutely essential to break the circle into charts.” The obstruction is global (compactness), not local: every point of $S^1$ has arbitrarily small neighborhoods that are perfectly good chart domains. A student asked which open sets can serve; the answer is the next proposition.

^rem-8-8

> [!theorem] Proposition §8.4: Chart Domains on the Circle
> A connected open subset $V \subseteq S^1$ is the domain of a chart if and only if $V \ne S^1$. Every such $V$ is an open arc, homeomorphic to an open interval.

^prop-8-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $V \ne S^1$, pick $q \notin V$ and a rotation $\rho$ of $S^1$ with $\rho(q) = N$. The stereographic projection $\sigma_N : S^1 \setminus \{N\} \to \mathbb{R}$ of [[§8 Differentiable Structures#^ex-8-3|Ex. §8.3]] below is a homeomorphism, so $\sigma_N \circ \rho$ maps $V$ homeomorphically onto a connected open subset of $\mathbb{R}$, which is an open interval; this is a chart. Conversely, $S^1$ is not a chart domain, by [[§8 Differentiable Structures#^prop-8-3|§8.3]].

^pf-8-4

*Uses:* [[§8 Differentiable Structures#^ex-8-3|Ex. §8.3]], [[§8 Differentiable Structures#^prop-8-3|§8.3]], [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[Continuous Image of a Connected Space is Connected|590 §13.3]], [[§14 Connected Subspaces of ℝ#^rem-14-1|590 §14 (connected subsets of ℝ are intervals)]]

> [!example] Example §8.3: Stereographic Atlas on the Circle
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
> a diffeomorphism of $\mathbb{R} \setminus \{0\}$ onto itself. So $\{(S^1 \setminus \{N\}, \sigma_N), (S^1 \setminus \{S\}, \sigma_S)\}$ is an atlas with only two charts. (“It is going to be a rational function”: here $u \mapsto 1/u$.) Consistently with [[§8 Differentiable Structures#^prop-8-3|§8.3]], two is the minimum.
>
> *Lee: Problem 1-7*

^ex-8-3

> [!remark]- Connections
> - Compatible with the other two circle atlases: [[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]]; the complex counterpart $w \mapsto 1/w$ on $\mathbb{CP}^1$: [[§8 Differentiable Structures#^rem-8-12|Remark after §8.9]].

![[m591-8-3.svg]]
*The hollow circle marks the pole each chart omits: $\sigma_N$ is undefined at $N$, since the line through $N$ and $N$ is not determined, and as $P$ climbs towards $N$ the image $\sigma_N(P)$ runs off to $\pm\infty$. Every other point is hit exactly once, so $\sigma_N$ is a bijection onto all of $\mathbb{R}$.*

The vertical ray is the case $P = S$: the line through $N$ and $S$ meets the axis at the origin, so $\sigma_N(S) = 0/(1-(-1)) = 0$, and by symmetry $\sigma_S(N) = 0$. The two charts are mirror images in this respect — $\sigma_N$ compresses the *lower* half-circle into $(-1,1)$ and throws the upper half outside it, while $\sigma_S$ does the reverse. On the overlap $S^1 \setminus \{N,S\}$ this exchange of inside and outside is exactly the transition function $u \mapsto 1/u$.

> [!example] Example §8.4: Angle Atlas on the Circle
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

^ex-8-4

> [!remark]- Connections
> - Polar angle as a coordinate (452): [[Polar and spherical coordinates]]; parametrizations as inverse charts: [[§9 Manifolds in Euclidean Space#^rem-9-2|§9, Remark: A Parametrization Is an Inverse Chart]].

> [!remark] Remark: Three Atlases and One Structure
> $S^1$ thus carries at least three different atlases. They are not competing structures: every chart of one is compatible with every chart of another, so they determine the *same* smooth structure. This is proved in [[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]], once regular level sets are available. For instance, on the arc where $U_2$ (upper half, coordinate $x$) meets $U_a$ the transition is $\theta \mapsto \cos\theta$ with inverse $x \mapsto \arccos x$, and $\sigma_N \circ \varphi_2^{-1}(x) = x/(1 - \sqrt{1-x^2})$ is smooth on $(-1,0) \cup (0,1)$. “Which atlas you write down is a matter of convenience” — what is intrinsic is the maximal atlas they all generate.

^rem-8-9

## Maximal Atlases and Smooth Structures

> [!definition] Definition §8.7: Compatible Atlases
> Two atlases $\mathcal{A}, \mathcal{A}'$ on $M$ are **$C^\infty$-compatible** if every chart of $\mathcal{A}$ is $C^\infty$-compatible with every chart of $\mathcal{A}'$; equivalently, if $\mathcal{A} \cup \mathcal{A}'$ is again an atlas.
>
> *Lee: Proposition 1.17(b)*

^def-8-7

> [!definition] Definition §8.8: Maximal Atlas
> An atlas $\mathcal{A}$ is **maximal** if every chart compatible with all the charts of $\mathcal{A}$ already belongs to $\mathcal{A}$. Equivalently, $\mathcal{A}$ is contained in no strictly larger atlas.
>
> *Lee: Ch. 1, Smooth Structures*

^def-8-8

> [!theorem] Theorem §8.5: Every Atlas Lies in a Unique Maximal Atlas
> Let $\mathcal{A}$ be an atlas on $M$ and let
>
> $$
> \overline{\mathcal{A}} = \{\, (V, \psi) \text{ a chart on } M \mid (V,\psi) \text{ is compatible with every chart of } \mathcal{A} \,\}.
> $$
>
> Then $\overline{\mathcal{A}}$ is the unique maximal atlas containing $\mathcal{A}$. Consequently two atlases are compatible if and only if they are contained in the same maximal atlas.
>
> *Lee: Proposition 1.17(a)*

^thm-8-5

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

^pf-8-5

*Uses:* [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§8 Differentiable Structures#^def-8-7|Def. §8.7]], [[§8 Differentiable Structures#^def-8-8|Def. §8.8]], [[§8 Differentiable Structures#^prop-8-2|§8.2]], [[Multivariable Chain Rule|452 §10.2]]

Lecture 5 argued uniqueness only (“anything in one is contained in the other, so they are equal”), taking for granted that the collection of all compatible charts is an atlas. Lecture 6 returned to the lemma: Uribe defined $\overline{\mathcal{A}}$ as above, called maximality “not that hard” and the atlas property “more substantial”, and sketched it — a point of the overlap lies in some chart of $\mathcal{A}$, compatible with both charts, “and then you have to do a little bit of diagram chasing” — skipping the details for time. The proof above completes that sketch. That step is the one with content, and the [[§8 Differentiable Structures#^rem-8-7|remark on non-transitivity above]] shows it really needs the mediating chart $(U,\varphi) \in \mathcal{A}$: without an atlas to pass through, pairwise compatibility with a single chart proves nothing. Compare Lee, Proposition 1.17.

> [!definition] Definition §8.9: Smooth Manifold Structure
> A **differentiable (smooth) structure** on a topological manifold $M$ is a maximal atlas $\mathcal{A}$ on $M$. A **smooth manifold** is a pair $\mathcal{M} = (M, \mathcal{A})$. By [[§8 Differentiable Structures#^thm-8-5|§8.5]], specifying any atlas specifies a smooth structure, and two atlases specify the same structure exactly when they are compatible.
>
> *Lee: Ch. 1, Smooth Structures*

^def-8-9

> [!remark] Remark: On the Connectedness Assumption
> The board wrote “let $M$ be a topological manifold (connected).” Nothing in this section uses connectedness, and the definitions above are stated without it. It is a harmless convenience — with $n$ fixed in advance ([[§2 Topological Manifolds#^def-2-2|Def. §2.2]]) the dimension is already constant — and it can be dropped. It does matter under the convention where $n$ is allowed to vary with the point ([[§2 Topological Manifolds#^cor-2-2|§2.2]]).

^rem-8-10

## Projective Spaces as Smooth Manifolds

*Assignment 2, Problem 2(b)–(c). This completes the construction begun in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients|§3, Application: Complex Projective Space]]: there $\mathbb{CP}^n$ was shown to be compact, Hausdorff and second countable; here it acquires charts, and the charts turn out to be smoothly — indeed holomorphically — compatible.*

> [!definition] Definition §8.10: Homogeneous Coordinates
> For $\vec z = (z_0, \ldots, z_n) \in \mathbb{C}^{n+1} \setminus \{0\}$, write $[z_0 : z_1 : \cdots : z_n] \in \mathbb{CP}^n$ for the complex line through $\vec z$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3.31]]). The $z_i$ are **homogeneous coordinates** of that point; they are determined only up to a common nonzero factor, $[\vec z] = [\lambda\vec z]$ for every $\lambda \in \mathbb{C}^\times$.
>
> *Lee: Problem 1-9*

^def-8-10

Let $\pi : \mathbb{C}^{n+1} \setminus \{0\} \to \mathbb{CP}^n$ be the projection $\vec z \mapsto [\vec z]$ of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3.31]]. Throughout, $\mathbb{C}^m \cong \mathbb{R}^{2m}$ by [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]].

> [!definition] Definition §8.11: The Standard Charts on $\mathbb{CP}^n$
> For $i \in \{0, 1, \ldots, n\}$ let
>
> $$
> U_i = \{\, [\vec z] \in \mathbb{CP}^n \mid z_i \neq 0 \,\},
> \qquad
> \varphi_i : U_i \to \mathbb{C}^n, \quad \varphi_i\big([z_0 : \cdots : z_n]\big) = \Big( \frac{z_k}{z_i} \Big)_{k \neq i}.
> $$
>
> It is convenient to index the $n$ entries of a point of the target by $\{0,\ldots,n\} \setminus \{i\}$ rather than by $\{1,\ldots,n\}$; this only relabels the slots. Equivalently $U_i = \{\ell \mid \ell \cap \{z_i = 0\} = \{0\}\}$: the lines not lying in the $i$-th coordinate hyperplane.
>
> *Lee: Problem 1-9*

^def-8-11

> [!theorem] Proposition §8.6: Each $\varphi_i$ Is a Chart
> $U_i$ is open in $\mathbb{CP}^n$, and $\varphi_i$ is a well-defined homeomorphism of $U_i$ onto $\mathbb{C}^n \cong \mathbb{R}^{2n}$, with inverse
>
> $$
> \varphi_i^{-1}(\vec w) = [\, w_0 : \cdots : w_{i-1} : 1 : w_{i+1} : \cdots : w_n \,] \qquad \text{($1$ in slot $i$).}
> $$
>
> *Lee: Problem 1-9*

^prop-8-6

![[m591-8-4.svg]]
*Here $p = \pi|_{\pi^{-1}(U_i)}$, the map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ divides by the $i$-th coordinate, and $s_i$ inserts a $1$ in slot $i$. The pattern of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3.31]] recurs: upstairs $\tilde\varphi_i \circ s_i = \mathrm{id}$ but $s_i \circ \tilde\varphi_i$ rescales $\vec z$ to $\vec z/z_i$; downstairs $\varphi_i$ and $\psi_i = p \circ s_i$ are mutually inverse. The triangle $\varphi_i \circ p = \tilde\varphi_i$ is where the universal property is applied — to $p$, not to $\pi$, which is the job of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|§3.24]].*

> [!proof]+ Proof
> *$U_i$ is well defined and open.* Every nonzero vector on a line $\ell$ is a scalar multiple $\lambda\vec z$, $\lambda \neq 0$, of any one of them, and $(\lambda\vec z)_i = \lambda z_i$; so “$z_i \neq 0$” holds for one representative iff for all. Hence
>
> $$
> \pi^{-1}(U_i) = \{\, \vec z \in \mathbb{C}^{n+1}\setminus\{0\} \mid z_i \neq 0 \,\},
> $$
>
> whose complement in $\mathbb{C}^{n+1}\setminus\{0\}$ is $H_i \setminus \{0\}$ with $H_i = \{z_i = 0\}$ a linear subspace, hence closed. So $\pi^{-1}(U_i)$ is open and, by the definition of the quotient topology, $U_i$ is open.
>
> *$\varphi_i$ is well defined.* For $\lambda \in \mathbb{C}^\times$ and $k \neq i$, $(\lambda z_k)/(\lambda z_i) = z_k/z_i$.
>
> *Bijectivity.* Let $s_i : \mathbb{C}^n \to \mathbb{C}^{n+1}\setminus\{0\}$ insert $1$ in slot $i$, and $\psi_i = \pi \circ s_i$. Then $\varphi_i(\psi_i(\vec w)) = \vec w$, since the representative $s_i(\vec w)$ has $i$-th entry $1$. Conversely, for $\ell = [\vec z] \in U_i$ the vector $\vec z/z_i$ represents $\ell$, has $i$-th entry $1$, and has remaining entries $\varphi_i(\ell)$; so $\psi_i(\varphi_i(\ell)) = \ell$. Thus $\psi_i = \varphi_i^{-1}$.
>
> *$\varphi_i$ is continuous.* By [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|§3.24]], since $\pi$ is a quotient map and $U_i$ is open, the restriction $p = \pi|_{\pi^{-1}(U_i)} : \pi^{-1}(U_i) \to U_i$ is a quotient map. The map $\tilde\varphi_i(\vec z) = (z_k/z_i)_{k\neq i}$ on $\pi^{-1}(U_i)$ is continuous (each component is a quotient of continuous functions with nonvanishing denominator) and constant on the fibres of $p$ by well-definedness. By the universal property ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]]) it descends to a continuous map on $U_i$, which is $\varphi_i$.
>
> *$\varphi_i^{-1}$ is continuous.* $\psi_i = \pi \circ s_i$, and $s_i$ is continuous (its components are coordinates or the constant $1$).

^pf-8-6

*Uses:* [[§8 Differentiable Structures#^def-8-10|Def. §8.10]], [[§8 Differentiable Structures#^def-8-11|Def. §8.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3.31]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|§3.24]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]], [[Universal Property of Quotient Maps|590 §12.3]], [[§10 Product Topology on Arbitrary Products#^thm-10-1|590 §10.1]]

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space of $\mathbb{C}^\times$: [[§6 Group Actions and Orbit Spaces#^ex-6-3|Ex. §6.3]]; the home of quotient maps and their universal property: [[§12 Quotient Topology|590 §12]].

> [!remark] Remark
> This is where [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|§3.24]] earns its place. The map $\tilde\varphi_i$ is defined only on the open piece $\pi^{-1}(U_i)$ — it divides by $z_i$ — so the universal property cannot be applied to $\pi$ itself; it is applied to $\pi$ restricted over $U_i$, which the lemma guarantees is still a quotient map. Every chart on a quotient space is built by this two-step move.

^rem-8-11

> [!theorem] Theorem §8.7: The Standard Atlas Is Smooth
> $\{(U_i, \varphi_i)\}_{i=0}^n$ is a $C^\infty$ atlas on $\mathbb{CP}^n$. For $i \neq j$,
>
> $$
> \varphi_j(U_i \cap U_j) = \{\, \vec w \in \mathbb{C}^n \mid w_i \neq 0 \,\},
> \qquad
> \big(\varphi_i \circ \varphi_j^{-1}\big)(\vec w) = \Big( \frac{w_k}{w_i} \Big)_{k \neq i},
> $$
>
> with the convention $w_j := 1$.
> Consequently $\mathbb{CP}^n$ is a compact smooth manifold of (real) dimension $2n$.
>
> *Lee: Problem 1-9*

^thm-8-7

![[m591-8-5.svg]]
*The compatibility triangle of [[§8 Differentiable Structures#Compatibility of Charts|Compatibility of Charts]] for two standard charts. The overlap lives upstairs in $\mathbb{CP}^n$; its two images downstairs are open subsets of $\mathbb{C}^n$, each cut out by one nonvanishing coordinate, and the bottom arrow is the transition function computed below.*

> [!proof]+ Proof
> *Cover.* If $\vec z \neq 0$ some $z_i \neq 0$, so $[\vec z] \in U_i$.
>
> *Domains.* By [[§8 Differentiable Structures#^prop-8-6|§8.6]], $\varphi_j^{-1}(\vec w)$ is represented by $s_j(\vec w)$, whose $j$-th entry is $1$ and whose $k$-th entry is $w_k$ for $k \neq j$. It lies in $U_i$ iff its $i$-th entry is nonzero, i.e. (as $i \neq j$) iff $w_i \neq 0$. This set is open, being the preimage of $\mathbb{C}\setminus\{0\}$ under the continuous coordinate $\vec w \mapsto w_i$.
>
> *Transition functions.* Applying $\varphi_i$ to the representative $s_j(\vec w)$ divides every entry by its $i$-th entry $w_i$ and deletes slot $i$, giving the displayed formula; in particular the entry in slot $j$ is $1/w_i$. Each entry $w_k/w_i$ is a quotient of polynomials with denominator nonvanishing on the domain. In real coordinates, writing $w_k = a_k + \mathrm{i}\,b_k$ (with $\mathrm{i}$ the imaginary unit, to distinguish it from the index $i$),
>
> $$
> \frac{w_k}{w_i} = \frac{w_k\,\overline{w_i}}{|w_i|^2} = \frac{a_k a_i + b_k b_i}{a_i^2 + b_i^2} + \mathrm{i}\,\frac{b_k a_i - a_k b_i}{a_i^2 + b_i^2},
> $$
>
> so both real components are rational functions with nonvanishing denominator $|w_i|^2$, hence $C^\infty$. Exchanging $i$ and $j$ gives the inverse transition, also $C^\infty$; so any two charts are compatible.
>
> *Conclusion.* The $U_i$ are open and cover, the $\varphi_i$ are homeomorphisms onto the open set $\mathbb{C}^n \cong \mathbb{R}^{2n}$, and all transitions are diffeomorphisms: this is a smooth atlas, determining a smooth structure by [[§8 Differentiable Structures#^thm-8-5|§8.5]]. Hausdorffness, second countability and compactness are [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3.29]] and [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30|§3.30]].

^pf-8-7

*Uses:* [[§8 Differentiable Structures#^prop-8-6|§8.6]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3.29]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30|§3.30]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]], [[§6 Differentiability#^thm-6-8|452 §6.8]]

> [!theorem] Corollary §8.8: $\mathbb{CP}^n$ Is a Complex Manifold
> The transition functions of the standard atlas are holomorphic. Hence $\mathbb{CP}^n$ is a complex manifold of complex dimension $n$, in the sense of [[§8 Differentiable Structures#^def-8-5|Def. §8.5]].

^cor-8-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Each component $\vec w \mapsto w_k/w_i$ of a transition function ([[§8 Differentiable Structures#^thm-8-7|§8.7]]) is a quotient of complex polynomials with denominator nonvanishing on the domain, hence holomorphic.

^pf-8-8

*Uses:* [[§8 Differentiable Structures#^thm-8-7|§8.7]], [[§8 Differentiable Structures#^def-8-5|Def. §8.5]]

> [!theorem] Proposition §8.9: $\mathbb{CP}^1$ Is the Riemann Sphere
> $\mathbb{CP}^1$ is homeomorphic to $S^2$.
>
> *Lee: Problem 4-5(b)*

^prop-8-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* For $(x,y,z) \in S^2$ the identity $(x+iy)(x-iy) = x^2 + y^2 = (1-z)(1+z)$ shows that $[x+iy : 1-z]$, defined when $z \ne 1$, and $[1+z : x-iy]$, defined when $z \ne -1$, are the same point of $\mathbb{CP}^1$ wherever both are defined. So there is a well-defined map $\Phi : S^2 \to \mathbb{CP}^1$, continuous on each of the two open sets $\{z \ne 1\}$ and $\{z \ne -1\}$ covering $S^2$, hence continuous. On $S^2 \setminus \{N\}$ it is $p \mapsto [\sigma(p) : 1]$, where $\sigma(x,y,z) = (x+iy)/(1-z)$ is the stereographic projection. This is a bijection onto $\mathbb{C}$, with inverse $w \mapsto \big(2\operatorname{Re} w,\, 2\operatorname{Im} w,\, |w|^2 - 1\big)/(|w|^2+1)$. So $\Phi$ maps $S^2 \setminus \{N\}$ bijectively onto $U_1 = \{[w : 1]\}$, and $\Phi(N) = [2 : 0] = [1:0]$ is the one point outside $U_1$. Thus $\Phi$ is a continuous bijection from the compact $S^2$ onto the Hausdorff $\mathbb{CP}^1$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3.29]]), hence a homeomorphism.

^pf-8-9

*Uses:* [[§8 Differentiable Structures#^def-8-10|Def. §8.10]], [[§8 Differentiable Structures#^def-8-11|Def. §8.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3.29]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§9 Continuous Functions#^thm-9-4|590 §9.4 (local formulation of continuity)]], [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]]

> [!remark] Remark
> For $n = 1$ there are two standard charts and a single transition function, $w \mapsto 1/w$ on $\mathbb{C} \setminus \{0\}$ — the complex counterpart of the stereographic transition $u \mapsto 1/u$ of [[§8 Differentiable Structures#^ex-8-3|Ex. §8.3]].

^rem-8-12

> [!theorem] Corollary §8.10: Real Projective Space
> Let $\mathbb{RP}^n = S^n/\{\pm 1\} \cong (\mathbb{R}^{n+1}\setminus\{0\})/\mathbb{R}^\times$, the space of real lines through the origin in $\mathbb{R}^{n+1}$. With $U_i = \{[\vec x] \mid x_i \neq 0\}$ and $\varphi_i([\vec x]) = (x_k/x_i)_{k \neq i}$, the family $\{(U_i, \varphi_i)\}_{i=0}^n$ is a smooth atlas, and $\mathbb{RP}^n$ is a compact smooth manifold of dimension $n$.
>
> *Lee: Example 1.33*

^cor-8-10

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Every argument of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients|§3, Application: Complex Projective Space]] and of this subsection goes through verbatim with $\mathbb{R}$, $\mathbb{R}^\times$, $\{\pm1\}$ and $S^n$ in place of $\mathbb{C}$, $\mathbb{C}^\times$, $S^1$ and $S^{2n+1}$: the group $\{\pm 1\}$ is finite, hence compact, and acts on $S^n$ by isometries; the transition maps are the real rational functions $x_k/x_i$. Hausdorffness can alternatively be read off from [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]].

^pf-8-10

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|§3.29]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-30|§3.30]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-31|§3.31]], [[§8 Differentiable Structures#^prop-8-6|§8.6]], [[§8 Differentiable Structures#^thm-8-7|§8.7]], [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]]

> [!remark]- Connections
> - The same space in 590, projective $n$-space: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 §28.2]], [[Projective plane]]; the double cover $S^n \to \mathbb{RP}^n$ as a local diffeomorphism: [[§14 Local Diffeomorphisms and Submersions#^ex-14-2|Ex. §14.2]].

![[m591-8-6.svg]]
*The chart $U_0$ of $\mathbb{RP}^1$, drawn in the plane of homogeneous coordinates. A point of $\mathbb{RP}^1$ is a line through the origin. A line $L$ with $x_0 \ne 0$ meets the affine line $x_0 = 1$ in exactly one point, $(1, x_1/x_0)$, and the chart $\varphi_0(L) = x_1/x_0$ records where. The one line with $x_0 = 0$ — the $x_1$-axis, the point $[0:1]$ — is parallel to $x_0 = 1$ and never meets it: it is the point at infinity that $U_0$ misses, and the second chart $U_1$ covers it. On the right, $\mathbb{RP}^1$ drawn as a circle, with $U_0$ everything except the top point. In $\mathbb{RP}^n$ the same picture holds with the affine hyperplane $x_0 = 1$ in place of the line.*

> [!theorem] Proposition §8.11: The Two Topologies on $\mathbb{RP}^n$ Agree
> 1. Under $[\vec x] \mapsto \mathbb{R}\vec x$, the quotient topology on $\mathbb{RP}^n = S^n/\{\pm1\}$ agrees with the topology of $\mathrm{Gr}_1(\mathbb{R}^{n+1})$ transported from the coset space $\mathrm{O}(n+1)/(\mathrm{O}(1)\times\mathrm{O}(n))$ in [[§7 Homogeneous Spaces|§7]].
> 2. $\mathbb{RP}^1$ is homeomorphic to $S^1$.
>
> *Lee: Examples 1.5 and 1.33*

^prop-8-11

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) $\mathrm{O}(n+1)$ acts on $S^n/\{\pm1\}$ by $g \cdot [\vec x] = [g\vec x]$, continuously: the map $\mathrm{id} \times \pi : \mathrm{O}(n+1) \times S^n \to \mathrm{O}(n+1) \times S^n/\{\pm1\}$ is an open continuous surjection, hence a quotient map, and the action descends along it by the universal property. The action is transitive, the coset space is compact, and $S^n/\{\pm1\}$ is Hausdorff, so [[§7 Homogeneous Spaces#^thm-7-8|§7.8]] identifies $S^n/\{\pm1\}$ homeomorphically with the coset space — which is precisely the transported topology.
>
> (2) Let $\sigma_N, \sigma_S$ be the stereographic charts of [[§8 Differentiable Structures#^ex-8-3|Ex. §8.3]], and $\varphi_0, \varphi_1$ the standard charts of $\mathbb{RP}^1$. Define $F = \sigma_N^{-1} \circ \varphi_0$ on $U_0$ and $F = \sigma_S^{-1} \circ \varphi_1$ on $U_1$. On $U_0 \cap U_1$ we have $\varphi_1 = 1/\varphi_0$, and $\sigma_S \circ \sigma_N^{-1}(u) = 1/u$ gives $\sigma_N^{-1}(u) = \sigma_S^{-1}(1/u)$; so the two formulas agree and $F$ is well defined and continuous. It maps $U_0$ bijectively onto $S^1 \setminus \{N\}$, and the one point $[0:1]$ outside $U_0$ to $\sigma_S^{-1}(0) = N$. So $F$ is a continuous bijection from the compact $\mathbb{RP}^1$ onto the Hausdorff $S^1$, hence a homeomorphism. Both transition functions are $u \mapsto 1/u$, and in the charts used $F$ has coordinate representation the identity; so it is even a diffeomorphism, in the sense of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] below.

^pf-8-11

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-22|§3.22]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]], [[§7 Homogeneous Spaces#^thm-7-8|§7.8]], [[§7 Homogeneous Spaces#^def-7-7|Def. §7.7]], [[§7 Homogeneous Spaces#^cor-7-13|§7.13]], [[§8 Differentiable Structures#^ex-8-3|Ex. §8.3]], [[§8 Differentiable Structures#^cor-8-10|§8.10]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§9 Continuous Functions#^thm-9-4|590 §9.4 (local formulation of continuity)]], [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]]

> [!remark]- Connections
> - $P^1 \cong S^1$ in 590: [[§28 Fundamental Group of Some Surfaces#^thm-28-3|590 §28.3]]; Grassmannians as homogeneous spaces: [[§7 Homogeneous Spaces#^cor-7-13|§7.13]].

![[m591-8-7.svg]]
*The quotient $S^n \to \mathbb{RP}^n$ of [[§8 Differentiable Structures#^prop-8-11|§8.11]], drawn for $n = 2$. A line through the origin meets the sphere in two antipodal points $p$ and $-p$, which $\pi$ identifies. Every line meets the closed upper hemisphere: once if it is not horizontal, and in a pair of antipodal points $q$, $-q$ of the equator if it is. So $\mathbb{RP}^2$ can be pictured as a closed disc with antipodal boundary points glued, as the arrows indicate. For $n = 1$ the same gluing closes a half-circle into a circle, which is $\mathbb{RP}^1 \cong S^1$.*

## Smooth Functions and Smooth Maps

[[§8 Differentiable Structures#^def-8-2|Def. §8.2]] explains what it means for a function to be smooth *in the sense of one chart*. With a smooth structure in hand the chart can be dropped from the phrase. Throughout, $M$ is a smooth manifold with maximal atlas $\mathcal{A}$.

> [!definition] Definition §8.12: Smooth Chart
> Let $M$ be a smooth manifold with maximal atlas $\mathcal{A}$. A **smooth chart** of $M$ is a chart belonging to $\mathcal{A}$ — equivalently, by [[§8 Differentiable Structures#^thm-8-5|§8.5]], a chart compatible with every chart of some, hence any, atlas generating $\mathcal{A}$.
>
> *Lee: Ch. 1, Smooth Structures*

^def-8-12

> [!definition] Definition §8.13: Smooth Function on a Manifold
> A function $f : M \to \mathbb{R}$ is **smooth** if for every $p \in M$ there exists a smooth chart $(U,\varphi)$ with $p \in U$ such that
>
> $$
> f_\varphi \;:=\; f|_U \circ \varphi^{-1} : \varphi(U) \longrightarrow \mathbb{R}
> $$
>
> is smooth in the sense of analysis. (The function $f_\varphi$ is $f$ written in the coordinates of the chart; it is what [[§8 Differentiable Structures#^def-8-2|Def. §8.2]] called $h \circ \varphi^{-1}$.)
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^def-8-13

> [!theorem] Proposition §8.12: Some Chart Suffices — Every Chart Then Works
> If $f : M \to \mathbb{R}$ is smooth, then $f_\psi = f|_V \circ \psi^{-1}$ is smooth for *every* smooth chart $(V,\psi)$ of $M$.
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^prop-8-12

> [!proof]+ Proof
> *(Stated in lecture, with the proof left to the class; filled in.)* Let $(V,\psi)$ be a smooth chart and $q \in V$; we show $f_\psi$ is smooth on a neighborhood of $\psi(q)$. Since smoothness of a function on an open subset of $\mathbb{R}^n$ is a local property, this suffices. By [[§8 Differentiable Structures#^def-8-13|Def. §8.13]] there is a smooth chart $(U,\varphi)$ with $q \in U$ and $f_\varphi$ smooth on $\varphi(U)$. Both charts belong to the maximal atlas, so they are compatible, and on the open set $\psi(U \cap V) \ni \psi(q)$,
>
> $$
> f_\psi = f \circ \psi^{-1} = \big(f \circ \varphi^{-1}\big) \circ \big(\varphi \circ \psi^{-1}\big) = f_\varphi \circ (\varphi \circ \psi^{-1}),
> $$
>
> a composite of the smooth map $f_\varphi$ with the transition function $\varphi \circ \psi^{-1}$, which is smooth by compatibility. Hence $f_\psi$ is smooth near $\psi(q)$.

^pf-8-12

*Uses:* [[§8 Differentiable Structures#^def-8-13|Def. §8.13]], [[§8 Differentiable Structures#^def-8-12|Def. §8.12]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-9|Def. §8.9]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark] Remark
> The point of logic Uribe stopped to make: the definition says “there *exists* a chart,” and the proposition upgrades it to “*any* chart.” Without the proposition, smoothness of $f$ would appear to depend on which charts one happened to test it in. The upgrade costs exactly one use of compatibility — which is what compatibility was designed to buy ([[§8 Differentiable Structures#^thm-8-1|§8.1]]). He assigned this as an exercise, not to be collected: “you have to wrestle with this.”

^rem-8-13

To compare two smooth manifolds one needs smooth *maps* between them.

> [!definition] Definition §8.14: Smooth Map and Diffeomorphism
> Let $(M, \mathcal{A}_M)$ and $(N, \mathcal{A}_N)$ be smooth manifolds of dimensions $m$ and $n$. A map $F : M \to N$ is **smooth** if it is continuous and for every $p \in M$ there are charts $(U,\varphi) \in \mathcal{A}_M$ with $p \in U$ and $(V,\psi) \in \mathcal{A}_N$ with $F(U) \subseteq V$ such that the **coordinate representation**
>
> $$
> \psi \circ F \circ \varphi^{-1} : \varphi(U) \longrightarrow \psi(V) \subseteq \mathbb{R}^n
> $$
>
> is smooth. $F$ is a **diffeomorphism** if it is a smooth bijection with smooth inverse — generalizing [[§8 Differentiable Structures#^def-8-3|Def. §8.3]], with which it agrees on open subsets of Euclidean space ([[§8 Differentiable Structures#^prop-8-14|§8.14]]).
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^def-8-14

> [!remark]- Connections
> - The Euclidean notion it generalizes: [[§8 Differentiable Structures#^def-8-3|Def. §8.3]]; local diffeomorphisms and the bijective case: [[§14 Local Diffeomorphisms and Submersions#^def-14-1|Def. §14.1]], [[§14 Local Diffeomorphisms and Submersions#^cor-14-3|§14.3]].
> - The topological counterpart, homeomorphism: [[§9 Continuous Functions#^def-9-2|590 §9.2]].

> [!theorem] Proposition §8.13: Smoothness of a Map Does Not Depend on the Charts
> If $F : M \to N$ is smooth, then for *every* pair of smooth charts $(U',\varphi')$ of $M$ and $(V',\psi')$ of $N$ with $F(U') \subseteq V'$, the coordinate representation $\psi' \circ F \circ \varphi'^{-1} : \varphi'(U') \to \psi'(V')$ is smooth. For $N = \mathbb{R}$ with its standard one-chart atlas, [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] agrees with [[§8 Differentiable Structures#^def-8-13|Def. §8.13]].
>
> *Lee: Proposition 2.5*

^prop-8-13

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Fix $a \in \varphi'(U')$ and put $p = \varphi'^{-1}(a)$. [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] supplies charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U) \subseteq V$ and $\psi \circ F \circ \varphi^{-1}$ smooth. On the open set $\varphi'(U \cap U') \ni a$,
>
> $$
> \psi' \circ F \circ \varphi'^{-1} = (\psi' \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1}).
> $$
>
> Here $\varphi \circ \varphi'^{-1}$ maps $\varphi'(U \cap U')$ into $\varphi(U \cap U')$, then $F$ maps $U \cap U'$ into $V \cap V'$, and $\psi' \circ \psi^{-1}$ is defined on $\psi(V \cap V')$. The outer factors are transition functions, smooth by compatibility, and the middle one is smooth by hypothesis. So the composite is smooth near $a$, and $a$ was arbitrary. For $N = \mathbb{R}$, taking $\psi = \mathrm{id}$ turns [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] into [[§8 Differentiable Structures#^def-8-13|Def. §8.13]]; continuity is automatic there, since $f = f_\varphi \circ \varphi$ near each point.

^pf-8-13

*Uses:* [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^def-8-13|Def. §8.13]], [[§8 Differentiable Structures#^def-8-12|Def. §8.12]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^ex-8-1|Ex. §8.1]], [[Multivariable Chain Rule|452 §10.2]]

> [!definition] Definition §8.15: Diffeomorphic Manifolds
> Smooth manifolds $M$ and $N$ are **diffeomorphic** if there is a diffeomorphism $F : M \to N$. Diffeomorphic manifolds are also called **isomorphic as smooth manifolds**.
>
> *Lee: Ch. 2, Diffeomorphisms*

^def-8-15

> [!remark] Remark
> “Diffeomorphic” is to smooth manifolds what “homeomorphic” is to topological spaces: the notion of sameness, under which every smooth property is preserved. No symbol is introduced for it; $\cong$ is already used in these notes for homeomorphisms and linear isomorphisms, so the word is written out.

^rem-8-14

> [!theorem] Proposition §8.14: The Two Notions of Diffeomorphism Agree
> Give open sets $A \subseteq \mathbb{R}^m$ and $B \subseteq \mathbb{R}^n$ their standard smooth structures, determined by the charts $(A, \mathrm{id}_A)$ and $(B, \mathrm{id}_B)$. Then a map $F : A \to B$ is smooth in the sense of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] if and only if it is smooth in the Euclidean sense. Consequently, for $m = n$, $F$ is a diffeomorphism in the sense of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] if and only if it is one in the sense of [[§8 Differentiable Structures#^def-8-3|Def. §8.3]], and $A$ and $B$ are diffeomorphic in the sense of [[§8 Differentiable Structures#^def-8-15|Def. §8.15]] if and only if they are in the sense of [[§8 Differentiable Structures#^def-8-3|Def. §8.3]].

^prop-8-14

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $F$ is smooth in the Euclidean sense, it is continuous, and in the charts $(A, \mathrm{id}_A)$ and $(B, \mathrm{id}_B)$ its coordinate representation is $F$ itself, which is smooth. Conversely, suppose $F$ is smooth in the sense of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], and let $p \in A$ with charts $(U, \varphi)$ and $(V, \psi)$ as in that definition. These charts belong to the standard structures, so they are compatible with the identity charts: $\varphi = \varphi \circ \mathrm{id}_A^{-1}$ and $\psi^{-1} = \mathrm{id}_B \circ \psi^{-1}$ are smooth in the Euclidean sense, by [[§8 Differentiable Structures#^def-8-4|Def. §8.4]]. Hence on $U$
>
> $$
> F = \psi^{-1} \circ \big(\psi \circ F \circ \varphi^{-1}\big) \circ \varphi
> $$
>
> is a composite of Euclidean-smooth maps, so $F$ is smooth near $p$. For diffeomorphisms, apply this to $F$ and to $F^{-1}$.

^pf-8-14

*Uses:* [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^def-8-3|Def. §8.3]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-15|Def. §8.15]], [[§8 Differentiable Structures#^ex-8-1|Ex. §8.1]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark] Remark
> Not stated in lecture. The word is defined twice because the logic needs it twice: [[§8 Differentiable Structures#^def-8-3|Def. §8.3]] must exist before smooth manifolds do, since compatibility of charts is phrased with it, and [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] is the general notion. The proposition is what licenses using one word for both. A third notion, the *local* diffeomorphism of [[§14 Local Diffeomorphisms and Submersions|§14]], is genuinely different; [[§14 Local Diffeomorphisms and Submersions#^cor-14-3|§14.3]] relates it to the other two.

^rem-8-15

> [!theorem] Lemma §8.15: Composition of Smooth Maps
> If $F : M \to N$ and $G : N \to P$ are smooth maps of smooth manifolds, then $G \circ F : M \to P$ is smooth.
>
> *Lee: Proposition 2.10*

^lem-8-15

> [!proof]+ Proof
> *(Lecture 7: “something that I would trust ChatGPT to prove without looking at the answer”; filled in.)* $G \circ F$ is continuous as a composite of continuous maps. Fix $p \in M$; we must produce charts at $p$ and at $G(F(p))$ satisfying [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]. The order of choices matters.
>
> *Step 1: charts for $G$ at $F(p)$.* Since $G$ is smooth, there are smooth charts $(V, \psi)$ of $N$ with $F(p) \in V$ and $(W, \chi)$ of $P$ with $G(V) \subseteq W$ such that $\chi \circ G \circ \psi^{-1}$ is smooth on $\psi(V)$.
>
> *Step 2: a chart for $F$ at $p$ landing inside $V$.* Since $F$ is smooth, there are smooth charts $(U_0, \varphi)$ of $M$ with $p \in U_0$ and $(V_0, \psi_0)$ of $N$ with $F(U_0) \subseteq V_0$ such that $\psi_0 \circ F \circ \varphi^{-1}$ is smooth. The chart $(V_0,\psi_0)$ need not be the $(V,\psi)$ of Step 1, so we adjust. Put $U = U_0 \cap F^{-1}(V)$, an open neighborhood of $p$ since $F$ is continuous, and keep the coordinate map $\varphi|_U$; $(U, \varphi|_U)$ is still a smooth chart (a restriction of one to an open subset). Now $F(U) \subseteq V \cap V_0$, and on $\varphi(U)$
>
> $$
> \psi \circ F \circ \varphi^{-1} = (\psi \circ \psi_0^{-1}) \circ (\psi_0 \circ F \circ \varphi^{-1}),
> $$
>
> which is smooth: the first factor is a transition function of the maximal atlas of $N$, the second is smooth by the choice of $(U_0,\varphi)$.
>
> *Step 3: compose.* $G \circ F$ maps $U$ into $W$, and on $\varphi(U)$
>
> $$
> \chi \circ (G \circ F) \circ \varphi^{-1} = \big(\chi \circ G \circ \psi^{-1}\big) \circ \big(\psi \circ F \circ \varphi^{-1}\big),
> $$
>
> a composite of two smooth maps between open subsets of Euclidean spaces (the inner map takes values in $\psi(V)$ because $F(U) \subseteq V$). So $(U, \varphi|_U)$ and $(W, \chi)$ witness the smoothness of $G \circ F$ at $p$.

^pf-8-15

*Uses:* [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^def-8-12|Def. §8.12]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[§2 Topological Manifolds#^lem-2-11|§2.11]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark]- Connections
> - The Euclidean case is the chain rule: [[Multivariable Chain Rule|452 §10.2]].

> [!theorem] Proposition §8.16: Being Diffeomorphic Is an Equivalence Relation
> 1. Being diffeomorphic is an equivalence relation on smooth manifolds.
> 2. Diffeomorphic manifolds are homeomorphic.
>
> *Lee: Proposition 2.15*

^prop-8-16

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) *Reflexive:* $\mathrm{id}_M$ is a diffeomorphism, its coordinate representation in any chart $(U,\varphi)$, taken on both sides, being the identity of $\varphi(U)$. *Symmetric:* if $F$ is a diffeomorphism, so is $F^{-1}$, since the definition is symmetric in $F$ and $F^{-1}$. *Transitive:* if $F : M \to N$ and $G : N \to P$ are diffeomorphisms, then $G \circ F$ is smooth by [[§8 Differentiable Structures#^lem-8-15|§8.15]], and so is its inverse $F^{-1} \circ G^{-1}$. (2) Smooth maps are continuous by [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], so a diffeomorphism is a continuous bijection with continuous inverse.

^pf-8-16

*Uses:* [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^def-8-15|Def. §8.15]], [[§8 Differentiable Structures#^lem-8-15|§8.15]], [[§9 Continuous Functions#^def-9-2|590 §9.2]]

> [!remark] Remark
> The converse of (2) is false: Milnor's exotic $7$-spheres are homeomorphic to $S^7$ but not diffeomorphic to it (see the [[§8 Differentiable Structures#^rem-8-20|remark after Ex. §8.5]]). Two further distinctions are worth keeping apart. *Different smooth structures* on one set may still be *diffeomorphic*: in [[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]], $\mathbb{R}$ and $\widetilde{\mathbb{R}}$ have different maximal atlases, yet $x \mapsto x^3$ is a diffeomorphism between them. And being diffeomorphic is a property of a *pair* of manifolds, while being a diffeomorphism is a property of a *map*: $\mathrm{id} : \mathbb{R} \to \widetilde{\mathbb{R}}$ is not a diffeomorphism even though the two are diffeomorphic.

^rem-8-16

> [!remark] Remark
> Uribe: “the composition of smooth maps is smooth is something I would trust ChatGPT to prove without looking at the answer.” The only content is Step 2 — the middle charts produced by the two hypotheses need not agree, and one must shrink the domain using continuity of $F$ and then pay one transition function to switch. “Just compose the two” skips exactly this.

^rem-8-17

![[m591-8-8.svg]]
*The top row is the map one cares about, between spaces where “smooth” has no meaning; the bottom row is its coordinate representation, between open subsets of Euclidean spaces where it does. The two vertical arrows are charts, so they are homeomorphisms, and the square commutes by construction. Smoothness of $F$ is defined by smoothness of the bottom arrow, and [[§8 Differentiable Structures#^prop-8-13|§8.13]] says this does not depend on which charts are used to build it.*

> [!example] Example §8.5: Two Smooth Structures on the Real Line
> Take $M = \mathbb{R}$ as a topological space in both cases, and put
>
> $$
> \mathbb{R} = (\mathbb{R}, \{(\mathbb{R}, \varphi)\}), \ \ \varphi = \mathrm{id}; \qquad\qquad
> \widetilde{\mathbb{R}} = (\mathbb{R}, \{(\mathbb{R}, \psi)\}), \ \ \psi(p) = \sqrt[3]{p}.
> $$
>
> Both $\varphi$ and $\psi$ are homeomorphisms of $\mathbb{R}$ onto $\mathbb{R}$, so each is a legitimate chart ([[§8 Differentiable Structures#^def-8-1|Def. §8.1]]), and a one-chart atlas is automatically smooth: the only compatibility to check is of the chart with itself, and the transition function is the identity. By [[§8 Differentiable Structures#^thm-8-5|§8.5]] each therefore determines a smooth structure.
>
> *Lee: Example 1.23*

^ex-8-5

> [!proof]+ Working out the example
> *(Lecture 5 introduced this example — the two structures are “not compatible, but isomorphic” — and Lecture 6 returned to it: “different, but isomorphic. We're going to say diffeomorphic.” Worked out here.)* *Step 1: the formula of a chart is not a legality condition.* One is tempted to object that $\psi$ “is not smooth.” On a bare topological manifold that question is not yet posed: “smooth” for a function on $M$ has no meaning until a structure is fixed, and here $\psi$ is what supplies the structure. What makes $\sqrt[3]{\,\cdot\,}$ look illegitimate is a silent comparison against the standard structure of $\mathbb{R}$ — and that comparison is not part of [[§8 Differentiable Structures#^def-8-1|Def. §8.1]]; it is the compatibility question of [[§8 Differentiable Structures#Compatibility of Charts|Compatibility of Charts]], arriving early and in disguise. Any homeomorphism onto an open set is a chart, whatever its formula. The formula is irrelevant to whether the chart may be written down, and decisive for which structure it produces.
>
> *Step 2: each chart is smooth for its own structure.* By [[§8 Differentiable Structures#^def-8-2|Def. §8.2]], a function $h : \mathbb{R} \to \mathbb{R}$ is smooth in the sense of $\psi$ iff $h \circ \psi^{-1}$ is smooth, where $\psi^{-1}(y) = y^3$. Taking $h = \psi$ gives $\psi \circ \psi^{-1} = \mathrm{id}$, which is smooth. So $\sqrt[3]{\,\cdot\,}$ *is* a smooth function on $\widetilde{\mathbb{R}}$. Nothing is special about this chart: the coordinate representation of any chart in its own coordinates is the identity, so every chart of an atlas is smooth for the structure that atlas generates. In the same way $\psi : \widetilde{\mathbb{R}} \to \mathbb{R}$ is a diffeomorphism — a chart is exactly an identification of its domain with a piece of Euclidean space, carried out in whichever coordinate the chart names.
>
> *Step 3: the two structures are different.* Compatibility is a condition on a *pair* of charts, and it is here that the two disagree. The two transition functions are
>
> $$
> \psi \circ \varphi^{-1}(x) = \sqrt[3]{x}, \qquad\qquad \varphi \circ \psi^{-1}(y) = y^3,
> $$
>
> and note the asymmetry: the second is smooth, the first is not, since $\tfrac{d}{dx}\sqrt[3]{x} = \tfrac13 x^{-2/3}$ blows up at $x = 0$. [[§8 Differentiable Structures#^def-8-4|Def. §8.4]] demands that the transition function be a diffeomorphism, i.e. that *both* directions be smooth — and this example is why: with only one direction required, compatibility would not even be a symmetric relation. So the charts are not compatible, the atlases are not compatible, and the maximal atlases are distinct. Equivalently, in the language of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]: the identity map $\mathbb{R} \to \widetilde{\mathbb{R}}$ has coordinate representation $\psi \circ \mathrm{id} \circ \varphi^{-1}(t) = \sqrt[3]{t}$ and is *not* smooth.
>
> *Step 4: which functions are smooth in each.* Smooth in the sense of $\varphi$ means $h \circ \varphi^{-1} = h$ is smooth, so $C^\infty(\mathbb{R})$ is the usual class. Smooth in the sense of $\psi$ means $y \mapsto h(y^3)$ is smooth. Every ordinarily smooth $h$ passes this test, being a composite of smooth maps; and $h = \sqrt[3]{\,\cdot\,}$ passes it while failing the first. Hence
>
> $$
> C^\infty(\mathbb{R}) \subsetneq C^\infty(\widetilde{\mathbb{R}}),
> $$
>
> a *strict* containment: $\widetilde{\mathbb{R}}$ has more smooth functions than $\mathbb{R}$. The two structures are genuinely different objects, not two names for one.
>
> *Step 5: and yet they are isomorphic.* Define $\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$, $\Phi(x) = x^3$. Its coordinate representation is $\psi \circ \Phi \circ \varphi^{-1}(t) = \sqrt[3]{t^3} = t$, the identity; the representation of $\Phi^{-1}(y) = \sqrt[3]{y}$ is likewise the identity. So $\Phi$ is a diffeomorphism and $\mathbb{R} \cong \widetilde{\mathbb{R}}$ as smooth manifolds. There is no contradiction with Step 4: the isomorphism is not the identity map, and pullback along $\Phi$ carries $C^\infty(\widetilde{\mathbb{R}})$ bijectively onto $C^\infty(\mathbb{R})$, so a strict containment between isomorphic objects is no more paradoxical here than elsewhere in infinite mathematics.
>
> The moral is that $x$ is merely a *label* for points of $\mathbb{R}$; the structure decides which functions of that label count as smooth, and the two structures decide differently. The identity map respects labels but not structure, while $x \mapsto x^3$ respects structure and scrambles labels.

^pf-ex-8-5

*Uses:* [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§8 Differentiable Structures#^def-8-2|Def. §8.2]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark]- Connections
> - The general mechanism: [[§8 Differentiable Structures#^prop-8-17|§8.17]] and [[§8 Differentiable Structures#^cor-8-18|§8.18]]; this example redone as a transported structure: [[§8 Differentiable Structures#^ex-8-6|Ex. §8.6]].

**Transcription note.** The board reads “Claim: $\exists\,\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$ which is $C^\infty$, $\Phi(x) = \sqrt[3]{x}$.” With $\widetilde{\mathbb{R}}$ carrying the chart $\psi = \sqrt[3]{\ \cdot\ }$, that map has coordinate representation $\sqrt[3]{\sqrt[3]{t}} = t^{1/9}$, which is not smooth at $0$; the domain and the formula have been paired the wrong way. The two correct readings are $\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$ with $\Phi(x) = x^3$ (used above), or the same map read backwards, $\Phi : \widetilde{\mathbb{R}} \to \mathbb{R}$ with $\Phi(x) = \sqrt[3]{x}$. Either way the coordinate representation is the identity, which is what the lecture meant by “it looks strange, but rewritten in the differentiable coordinate you just get the identity.”

![[m591-8-9.svg]]
*The two coordinate pictures of [[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]]: left, the transition function $\psi\circ\varphi^{-1}(t)=\sqrt[3]{t}$, whose vertical tangent at $0$ makes the two charts incompatible; right, the coordinate representation $\psi\circ\Phi\circ\varphi^{-1}(t)=t$ of $\Phi(x) = x^3$, the identity, which is why $\Phi$ is a diffeomorphism.*

> [!theorem] Proposition §8.17: Transport of Smooth Structure
> Let $N$ be a smooth $n$-manifold, $X$ a topological space, and $h : X \to N$ a homeomorphism. Then:
> 1. $X$ is a topological $n$-manifold, and $\mathcal{A}_h = \{\, (h^{-1}(V),\ \psi \circ h) \mid (V,\psi) \text{ a smooth chart of } N \,\}$ is a smooth atlas on $X$;
> 2. for the smooth structure it determines, $h$ is a diffeomorphism;
> 3. it is the *only* smooth structure on $X$ for which $h$ is a diffeomorphism.
>
> *Lee: cf. Problem 1-6*

^prop-8-17

> [!proof]+ Proof
> (1) Hausdorffness and second countability pass through homeomorphisms. Each $\psi \circ h$ is a homeomorphism of the open set $h^{-1}(V)$ onto the open set $\psi(V) \subseteq \mathbb{R}^n$, and these domains cover $X$ because the $V$ cover $N$. Transition functions are $(\psi' \circ h) \circ (\psi \circ h)^{-1} = \psi' \circ \psi^{-1}$, transition functions of $N$, hence smooth.
>
> (2) In the charts $(h^{-1}(V), \psi \circ h)$ of $X$ and $(V, \psi)$ of $N$, the coordinate representation of $h$ is $\psi \circ h \circ (\psi \circ h)^{-1} = \mathrm{id}$, and likewise for $h^{-1}$. Both are continuous, so both are smooth.
>
> (3) Suppose $h$ is a diffeomorphism for some smooth structure $\mathcal{S}$ on $X$, and let $(W, \chi) \in \mathcal{S}$. Then $(\psi \circ h) \circ \chi^{-1} = \psi \circ h \circ \chi^{-1}$ is a coordinate representation of $h$, and $\chi \circ (\psi \circ h)^{-1} = \chi \circ h^{-1} \circ \psi^{-1}$ one of $h^{-1}$; both are smooth by [[§8 Differentiable Structures#^prop-8-13|§8.13]]. So every chart of $\mathcal{S}$ is compatible with every chart of $\mathcal{A}_h$, i.e. $\mathcal{S}$ lies in the maximal atlas generated by $\mathcal{A}_h$. Since $\mathcal{S}$ is itself maximal, the two coincide ([[§8 Differentiable Structures#^thm-8-5|§8.5]]).

^pf-8-17

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^prop-8-13|§8.13]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[§9 Continuous Functions#^def-9-2|590 §9.2]]

> [!definition] Definition §8.16: Transported Smooth Structure
> In the situation of [[§8 Differentiable Structures#^prop-8-17|§8.17]], the smooth structure on $X$ generated by $\mathcal{A}_h$ — the unique one for which $h$ is a diffeomorphism — is the smooth structure **transported** along $h$.
>
> *Lee: cf. Problem 1-6*

^def-8-16

> [!remark] Remark
> This is the smooth counterpart of [[§7 Homogeneous Spaces#^def-7-7|Def. §7.7]], where a *topology* was transported along a bijection. Here a smooth structure is transported along a homeomorphism: the charts of $N$, precomposed with $h$, become charts of $X$. The structure on $X$ is then “$N$'s structure, relabelled by $h$”, which is why $h$ is automatically a diffeomorphism.

^rem-8-18

> [!theorem] Corollary §8.18: Single-Chart Structures on $\mathbb{R}^n$
> Let $h : \mathbb{R}^n \to \mathbb{R}^n$ be a homeomorphism, and let $M$ be $\mathbb{R}^n$ with the smooth structure determined by the one-chart atlas $\{(\mathbb{R}^n, h)\}$.
> 1. $\{(\mathbb{R}^n, h)\}$ is a smooth atlas.
> 2. $h : M \to \mathbb{R}^n$ is a diffeomorphism onto $\mathbb{R}^n$ with its standard structure. So $M$ is diffeomorphic to standard $\mathbb{R}^n$.
> 3. The smooth structure of $M$ *equals* the standard one if and only if $h$ is a diffeomorphism of standard $\mathbb{R}^n$.
>
> *Lee: Example 1.23 and Problem 1-6*

^cor-8-18

> [!proof]+ Proof
> *(Assignment 3, Problem 1.)* (1) The single domain $\mathbb{R}^n$ covers $M$; $h$ is a homeomorphism onto $h(\mathbb{R}^n) = \mathbb{R}^n$, which is open; and the only transition function is $h \circ h^{-1} = \mathrm{id}_{\mathbb{R}^n}$, which is smooth.
>
> (2) The underlying topological spaces of $M$ and of standard $\mathbb{R}^n$ are the same, so $h$ is a homeomorphism $M \to \mathbb{R}^n$, in particular continuous with continuous inverse $h^{-1}$. In the charts $(\mathbb{R}^n, h)$ of $M$ and $(\mathbb{R}^n, \mathrm{id})$ of standard $\mathbb{R}^n$, the coordinate representation of $h$ is $\mathrm{id} \circ h \circ h^{-1} = \mathrm{id}_{\mathbb{R}^n}$, and that of $h^{-1}$ is $h \circ h^{-1} \circ \mathrm{id}^{-1} = \mathrm{id}_{\mathbb{R}^n}$. Both are smooth, so $h$ is a smooth bijection with smooth inverse. Equivalently, $M$ carries exactly the structure transported along $h$ from standard $\mathbb{R}^n$ ([[§8 Differentiable Structures#^prop-8-17|§8.17]], with the atlas $\{(\mathbb{R}^n, \mathrm{id})\}$ of the target).
>
> (3) The two one-chart atlases determine the same smooth structure if and only if they are compatible ([[§8 Differentiable Structures#^def-8-7|Def. §8.7]]), i.e. if and only if $h \circ \mathrm{id}^{-1} = h$ and $\mathrm{id} \circ h^{-1} = h^{-1}$ are both smooth — that is, if and only if $h$ is a diffeomorphism of standard $\mathbb{R}^n$.

^pf-8-18

*Uses:* [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§8 Differentiable Structures#^ex-8-1|Ex. §8.1]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^prop-8-17|§8.17]], [[§8 Differentiable Structures#^def-8-7|Def. §8.7]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[§8 Differentiable Structures#^def-8-3|Def. §8.3]]

![[m591-8-10.svg]]
*The proof of (2) in one square. Upstairs, $h$ is the map between the two manifolds; the vertical arrows are their charts, $h$ on the left and $\mathrm{id}$ on the right. The square commutes, so the coordinate representation along the bottom is the identity: $h$ is as smooth as a map can be, even when, as a map of standard $\mathbb{R}^n$, it is not differentiable at all.*

> [!example] Example §8.6: The Real Line with the Cube-Root Chart
> For $n = 1$ and $h(x) = \sqrt[3]{x}$, the manifold $M$ is the $\widetilde{\mathbb{R}}$ of [[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]]. By [[§8 Differentiable Structures#^cor-8-18|§8.18]](3) its structure differs from the standard one, since $h$ is not differentiable at $0$. By part (2) it is nevertheless diffeomorphic to standard $\mathbb{R}$, via $h : \widetilde{\mathbb{R}} \to \mathbb{R}$ — equivalently via $h^{-1}(x) = x^3$ in the other direction, the map $\Phi$ of that example.
>
> *Lee: Example 1.23*

^ex-8-6

> [!remark] Remark
> [[§8 Differentiable Structures#^cor-8-18|§8.18]] produces, from each homeomorphism of $\mathbb{R}^n$ that is not a diffeomorphism — there are uncountably many — a smooth structure on $\mathbb{R}^n$ *different* from the standard one. By (2), every one of them is *diffeomorphic* to the standard one. So “how many smooth structures” is the wrong question: the right one is how many up to diffeomorphism. It also shows something about the exotic structures of the [[§8 Differentiable Structures#^rem-8-20|next remark]]. An exotic $\mathbb{R}^4$ cannot admit a single chart whose image is all of $\mathbb{R}^4$, since by the argument of (2) that chart would be a diffeomorphism onto standard $\mathbb{R}^4$.

^rem-8-19

> [!remark] Remark: Distinct Structures versus Non-Diffeomorphic Manifolds
> [[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]] shows that one topological manifold can carry distinct smooth structures — but that alone is cheap, since pulling any structure back along a homeomorphism that is not a diffeomorphism produces another one, and all of these are diffeomorphic to the original ([[§8 Differentiable Structures#^prop-8-17|§8.17]], [[§8 Differentiable Structures#^cor-8-18|§8.18]]). The deep question is whether a topological manifold can carry structures that are *not* diffeomorphic to one another. It can: Milnor found smooth structures on $S^7$ not diffeomorphic to the standard one (1956), and $\mathbb{R}^4$ admits uncountably many pairwise non-diffeomorphic structures, the first produced by combining Freedman's topological classification with Donaldson's gauge theory, the uncountable family by Taubes. By contrast $\mathbb{R}^n$ for $n \neq 4$ admits exactly one up to diffeomorphism — a result of Stallings for $n \ge 5$ and of Radó and Moise for $n \le 3$, not of Donaldson, to whom the lecture attributed it. All of this is far outside the course, but it is why the definitions above are made so carefully.

^rem-8-20

## Product Manifolds

*Lecture 11 (Fri Sep 25). The product of two smooth manifolds is a smooth manifold, with the products of charts as an atlas; its tangent spaces are treated in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|§12]].*

> [!theorem] Proposition §8.19: The Product Smooth Structure
> Let $M_1$, $M_2$ be smooth manifolds of dimensions $m_1$, $m_2$. The product space $M_1 \times M_2$ is a topological manifold of dimension $m_1 + m_2$, and the **product charts**
>
> $$
> \big(U_1 \times U_2,\ \varphi_1 \times \varphi_2\big), \qquad (\varphi_1 \times \varphi_2)(q_1, q_2) = \big(\varphi_1(q_1), \varphi_2(q_2)\big) \in \mathbb{R}^{m_1} \times \mathbb{R}^{m_2} = \mathbb{R}^{m_1 + m_2},
> $$
>
> with $(U_i, \varphi_i)$ a smooth chart of $M_i$, form a smooth atlas on it.
>
> *Lee: Example 1.34*

^prop-8-19

> [!proof]+ Proof
> Hausdorffness and second countability pass to products ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-12|§3.12]]). Each $U_1 \times U_2$ is open, and these sets cover $M_1 \times M_2$. The map $\varphi_1 \times \varphi_2$ is a bijection of $U_1 \times U_2$ onto $\varphi_1(U_1) \times \varphi_2(U_2)$, which is open in $\mathbb{R}^{m_1 + m_2}$; it is continuous with continuous inverse $\varphi_1^{-1} \times \varphi_2^{-1}$, because each is continuous in each component ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]]). So the product charts are charts, and $M_1 \times M_2$ is locally Euclidean of dimension $m_1 + m_2$. Two product charts overlap in $(U_1 \cap U_1') \times (U_2 \cap U_2')$, and their transition map is
>
> $$
> (\psi_1 \times \psi_2) \circ (\varphi_1 \times \varphi_2)^{-1} = (\psi_1 \circ \varphi_1^{-1}) \times (\psi_2 \circ \varphi_2^{-1}),
> $$
>
> smooth because each component is.

^pf-8-19

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-12|§3.12]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§10 Product Topology on Arbitrary Products#^thm-10-1|590 §10.1]]

> [!remark]- Connections
> - Product topology in 590: [[§4 Product Topology#^def-4-1|590 §4.1]]; the tangent space of a product: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|§12.32]].

> [!definition] Definition §8.17: Product Manifold
> The **product manifold** $M_1 \times M_2$ is the product space with the smooth structure generated by the product charts ([[§8 Differentiable Structures#^prop-8-19|§8.19]]). If $\varphi_1 = (x^1, \ldots, x^{m_1})$ and $\varphi_2 = (y^1, \ldots, y^{m_2})$, the coordinate functions of the product chart are $x^i \circ \pi_1$ and $y^j \circ \pi_2$, written again $x^i$, $y^j$: “the $x$'s and then the $y$'s”. For $p_2 \in M_2$ and $p_1 \in M_1$, the **slice inclusions** are
>
> $$
> \iota^{p_2} : M_1 \to M_1 \times M_2, \ q \mapsto (q, p_2), \qquad\qquad \iota^{p_1} : M_2 \to M_1 \times M_2, \ q \mapsto (p_1, q).
> $$

^def-8-17

> [!theorem] Proposition §8.20: Projections and Slice Inclusions Are Smooth
> The projections $\pi_1 : M_1 \times M_2 \to M_1$, $\pi_2 : M_1 \times M_2 \to M_2$ and the slice inclusions $\iota^{p_2}$, $\iota^{p_1}$ are smooth. In product charts their coordinate representations are
>
> $$
> (r, s) \mapsto r, \qquad (r, s) \mapsto s, \qquad r \mapsto \big(r, \varphi_2(p_2)\big), \qquad s \mapsto \big(\varphi_1(p_1), s\big).
> $$

^prop-8-20

> [!proof]+ Proof
> All four are continuous: the projections by the definition of the product topology, the inclusions because their components are continuous ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]]). The coordinate representations are read off from $\varphi_1 \circ \pi_1 \circ (\varphi_1 \times \varphi_2)^{-1}(r, s) = r$ and $(\varphi_1 \times \varphi_2) \circ \iota^{p_2} \circ \varphi_1^{-1}(r) = (r, \varphi_2(p_2))$, and the same for the others. They are smooth, so the maps are smooth ([[§8 Differentiable Structures#^prop-8-13|§8.13]]).

^pf-8-20

*Uses:* [[§8 Differentiable Structures#^def-8-17|Def. §8.17]], [[§8 Differentiable Structures#^prop-8-19|§8.19]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^prop-8-13|§8.13]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]], [[§10 Product Topology on Arbitrary Products#^thm-10-1|590 §10.1]]

> [!remark]- Connections
> - Projections are submersions: [[§14 Local Diffeomorphisms and Submersions#^ex-14-4|Ex. §14.4]]; their differentials: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|§12.32]].
