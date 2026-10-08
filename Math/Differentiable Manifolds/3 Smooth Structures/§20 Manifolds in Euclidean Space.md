---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 20
tags: [differentiable-manifolds, math591]
---
← [[§19 Smooth Functions and Smooth Maps]] · ↑ [[· 3 Smooth Structures]] · [[§21 Linear Algebra Toolkit]] →

*Stage: geometric — The equations thread made smooth: a manifold given inside $\mathbb{R}^N$, and level sets smoothed by graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]).*

## Two Descriptions of a Manifold in Euclidean Space

> [!remark] Remark: The Closing Remark
> The lecture ended before the “main theorem,” which the lecturer named as the [[§7 The Regular Value Theorem#^thm-7-1|implicit function theorem]], and summarized its message instead:
>
> > There are two ways to look at a manifold sitting in a big ambient space. Either it is defined by the simultaneous zeros of some functions, or it is parametrized. The implicit function theorem says it does not matter — they are the same thing.
>
> So one may think of a manifold *internally*, through parametrizations, or *externally*, through the equations that cut it out of the ambient space. “We started with the circle, sum of squares equals one, and we have parametrizations like $\theta$.” The rest of this subsection makes the slogan precise; none of it was proved in lecture, and the two halves are in quite different states in these notes.

^rem-20-1

> [!definition] Definition §20.1: External Description
> Let $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$. Near $p$, $X$ is described **externally** if there are an open $W \ni p$ in $\mathbb{R}^{n+k}$ and a smooth $F : W \to \mathbb{R}^k$ having $\vec 0$ as a regular value, with $X \cap W = F^{-1}(\vec 0)$ — the level-set or implicit description.

^def-20-1

> [!definition] Definition §20.2: Internal Description
> Let $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$. Near $p$, $X$ is described **internally** if there are an open $V \subseteq \mathbb{R}^n$, an open $W \ni p$ in $\mathbb{R}^{n+k}$, and a smooth $\alpha : V \to \mathbb{R}^{n+k}$ which is a homeomorphism onto $X \cap W$ and whose Jacobian $D\alpha_q$ has rank $n$ at every $q \in V$ — the parametric description.

^def-20-2

> [!remark]- Connections
> - With $n = 2$ and $k = 1$ the internal description is a regular parametrized surface, [[§31 Surface Integrals#^def-31-3|452 Def. §31.3]] (452 does not require the homeomorphism condition).

> [!theorem] Theorem §20.1: The Two Descriptions Agree
> For $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$, the external and internal descriptions near $p$ are equivalent, and each is equivalent to:
> - (G) **graph:** after a permutation of the coordinates of $\mathbb{R}^{n+k} = \mathbb{R}^n \times \mathbb{R}^k$, there are open sets $V \subseteq \mathbb{R}^n$, $V' \subseteq \mathbb{R}^k$ with $p \in V \times V'$ and a smooth $h : V \to V'$ such that $X \cap (V \times V') = \{\, (x, h(x)) \mid x \in V \,\}$.

^thm-20-1

> [!proof]+ Proof (not given in lecture)
> *External $\Rightarrow$ (G).* This is Steps 1–3 of the proof of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]]: the rank condition lets one permute coordinates so that $\big(\partial F^i/\partial y^j(p)\big)$ is nonsingular, and Theorem [[§7 The Regular Value Theorem#^thm-7-1|§7.1]] produces the smooth $h$ with $F(x,y) = \vec 0 \iff y = h(x)$ on a box.
>
> *(G) $\Rightarrow$ external.* Take $W = V \times V'$ and $F(x,y) = y - h(x)$, smooth, with $F^{-1}(\vec 0) = X \cap W$ by hypothesis. Its Jacobian is the $k \times (n+k)$ block matrix $\big(-Dh_x \ \big| \ I_k\big)$, of rank $k$ everywhere because of the identity block; so $\vec 0$ is a regular value.
>
> *(G) $\Rightarrow$ internal.* Take $\alpha(x) = (x, h(x))$ on $V$. It is smooth, its Jacobian $\big(I_n \, ; \, Dh_x\big)$ has rank $n$, and it is a homeomorphism onto $X \cap (V \times V')$ with inverse the restriction of the projection $(x,y) \mapsto x$.
>
> *Internal $\Rightarrow$ (G).* Since $D\alpha_q$ has rank $n$, some $n$ of its $n+k$ rows are independent; permute coordinates so these are the first $n$, and write $\alpha = (\alpha_1, \alpha_2)$ with $\alpha_1 : V \to \mathbb{R}^n$, $\alpha_2 : V \to \mathbb{R}^k$. Then $D(\alpha_1)_q$ is invertible, so by the [[§33 Local Diffeomorphisms#^thm-33-1|inverse function theorem]] (Lee, Theorem C.34) $\alpha_1$ restricts to a diffeomorphism of a neighborhood $V_1 \ni q$ onto an open $V_2 \subseteq \mathbb{R}^n$. Put $h = \alpha_2 \circ (\alpha_1|_{V_1})^{-1} : V_2 \to \mathbb{R}^k$, smooth. Then $\alpha(V_1) = \{(x, h(x)) \mid x \in V_2\}$, and because $\alpha$ is a homeomorphism onto $X \cap W$, the set $\alpha(V_1)$ is open in $X \cap W$, so it equals $X \cap (V_2 \times V')$ for a suitable box.

^pf-20-1

*Uses:* [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark]- Connections
> - The analytic input: the vector-valued implicit function theorem [[§7 The Regular Value Theorem#^thm-7-1|§7.1]] (one-equation version in 452: [[§15 The Implicit Function Theorem#^thm-15-2|452 §15.2]]) and the inverse function theorem [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]] (two-variable version in 452: [[Inverse Function Theorem (several variables)|452 §16.2]]).
> - The external description becomes the regular value theorem for manifolds, [[§35 Submanifolds#^thm-35-7|§35.7]], and adapted charts, [[§35 Submanifolds#^def-35-2|Def. §35.2]] — the slice description, a fourth equivalent one ([[§35 Submanifolds#^prop-35-6|§35.6]]); the internal one becomes the local normal form for immersions, [[§37 Immersions#^thm-37-1|§37.1]].
> - The tangent space in both pictures: [[§25 The Geometric Tangent Space#^cor-25-4|§25.4]].

The circle in its three descriptions is collected in [[§24 The Circle|§24]].

> [!remark] Remark: A Parametrization Is an Inverse Chart
> “A parametrization is just another name for my inverse” — if $(U, \varphi)$ is a chart then $\varphi^{-1} : \varphi(U) \to U$ is a parametrization, and conversely. The internal description is therefore the chart picture of [[· 1 Topological Manifolds|Chapter 1]] with the extra demand that the map be smooth with injective differential; the external one is the level-set picture of [[§12 The Classical Groups Are Topological Manifolds|§12, The Classical Groups Are Topological Manifolds]]. Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] says the two carry the same information locally, which is why one may pass freely between “solve the equations” and “draw the parametrization” — “the same thing.”

^rem-20-2

## Smooth Structures on Regular Level Sets

*Lecture 6. Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] produced a* topological *manifold from a regular level set. The charts it produced were not arbitrary, and the point of this subsection is that they are automatically smoothly compatible — so the regular value theorem is in fact a machine for manufacturing smooth manifolds. “This is a powerful way of constructing examples.”*

Recall the construction in the proof of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]]. Index the coordinates of $\mathbb{R}^{n+k}$ by $\{1, \ldots, n+k\}$. For $p \in M = F^{-1}(c)$, the hypothesis $\operatorname{rank} F'(p) = k$ says that some $k$ of the $n+k$ columns of $F'(p)$ are linearly independent. Choose such a set of indices $J$, $|J| = k$, and let $I = \{1,\ldots,n+k\} \setminus J$ be the complementary $n$ indices. Write $x_J \in \mathbb{R}^J$ and $x_I \in \mathbb{R}^I$ for the corresponding groups of coordinates. The [[§7 The Regular Value Theorem#^thm-7-1|implicit function theorem]] then solves for $x_J$ in terms of $x_I$: there are an open box $U_J \times V_J' \ni p$ and a smooth $h_J : V_J \to \mathbb{R}^J$ with

$$
F(x) = c \iff x_J = h_J(x_I) \qquad \text{for } x \text{ in the box},
$$

and the chart is the restriction to $M$ of the linear projection $\pi_I : \mathbb{R}^{n+k} \to \mathbb{R}^I$,

$$
\begin{aligned}
\varphi_J &: U_J \to V_J \subseteq \mathbb{R}^I, &\quad \varphi_J &= \pi_I|_{U_J}, \\
\varphi_J^{-1} &: V_J \to \mathbb{R}^{n+k}, &\quad \varphi_J^{-1}(u) &= \text{the point with } x_I = u,\ x_J = h_J(u).
\end{aligned}
$$

The inverse $\varphi_J^{-1}$ is a parametrization of that piece of $M$, in the following sense.

> [!definition] Definition §20.3: Parametrization
> Let $(U, \varphi)$ be a chart of a manifold $M$. The inverse $\varphi^{-1} : \varphi(U) \to U$ is the **parametrization** of $U$ determined by the chart. When $M \subseteq \mathbb{R}^N$, it is also regarded as a map $\varphi(U) \to \mathbb{R}^N$.
>
> *Lee: Ch. 1, Coordinate Charts (“local parametrization)*

^def-20-3

> [!theorem] Proposition §20.2: Regular Level Sets Are Smooth Manifolds
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, and $c \in \mathbb{R}^k$ a regular value. Then the charts $\{(U_J, \varphi_J)\}$ above form a $C^\infty$ atlas on $M = F^{-1}(c)$, and $M$ is a smooth manifold of dimension $n$.
>
> *Lee: Example 1.32 and Corollary 5.14*

^prop-20-2

![[m591-9-2.svg]]
*The transition function $\varphi_{J'} \circ \varphi_J^{-1}$ between two graph charts factors through $\mathbb{R}^{n+k}$: the parametrization $\varphi_J^{-1}$ up, then the linear projection $\pi_{I'}$ down.*

The proof in one picture. The transition function between two graph charts factors through the ambient space: a parametrization up, followed by a linear projection down. Both legs are smooth in the Euclidean sense, so the composite is.

> [!proof]+ Proof
> *(Lecture 6 worked the surface of [[§20 Manifolds in Euclidean Space#^ex-20-1|Ex. §20.1]] first, then gave this general argument: “the general thing is just harder to write.”)* The domains cover $M$, since each $p \in M$ lies in some $U_J$. Let $(U_J, \varphi_J)$ and $(U_{J'}, \varphi_{J'})$ be two of the charts, with complementary index sets $I$ and $I'$. Two observations, each valid for every choice of $J$:
> 1. $\varphi_J^{-1} : V_J \to \mathbb{R}^{n+k}$ is smooth *in the Euclidean sense*: its components are either coordinates of $u$ or components of the smooth map $h_J$.
> 2. $\varphi_{J'}$ is the restriction of the linear map $\pi_{I'}$, which is smooth on all of $\mathbb{R}^{n+k}$.
>
> The transition function is the composite of the two. On the open set $\varphi_J(U_J \cap U_{J'}) \subseteq \mathbb{R}^I$,
>
> $$
> \varphi_{J'} \circ \varphi_J^{-1} = \pi_{I'} \circ \varphi_J^{-1},
> $$
>
> a composite of smooth maps between open subsets of Euclidean spaces, hence smooth. Exchanging the roles of $J$ and $J'$ shows $\varphi_J \circ \varphi_{J'}^{-1}$ is smooth as well, so the transition function is a diffeomorphism and the two charts are $C^\infty$-compatible ([[§17 Differentiable Structures#^def-17-4|Def. §17.4]]). By Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] the atlas determines a smooth structure, of dimension $n$ by Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].

^pf-20-2

*Uses:* [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§20 Manifolds in Euclidean Space#^def-20-3|Def. §20.3]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§20 Manifolds in Euclidean Space#^ex-20-1|Ex. §20.1]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark]- Connections
> - Regular values are defined three times in 591: [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]] (Euclidean), [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]] and [[§34 Submersions#^def-34-4|Def. §34.4]] (manifolds).
> - Generalized to level sets in manifolds: [[§35 Submanifolds#^thm-35-7|§35.7]]; the two structures agree by [[§35 Submanifolds#^prop-35-9|§35.9]].

> [!example] Example §20.1: A Surface in $\mathbb{R}^3$
> The case $n = 2$, $k = 1$, where the indices can be written out. Let $F : W \subseteq \mathbb{R}^3 \to \mathbb{R}$ be smooth with regular value $c$, so $M = F^{-1}(c)$ is a surface and $F'(p) = \nabla F(p) \neq 0$ for $p \in M$. Suppose that at $p$ *two* partial derivatives are nonzero, say $\partial F/\partial z(p) \neq 0$ and $\partial F/\partial y(p) \neq 0$. Then $p$ lies in the domains of two charts built from different solved-for variables:
>
> $$
> \begin{aligned}
> \text{solving for } z: &\quad z = g(x,y), &\quad \varphi : U \to \mathbb{R}^2, &\quad \varphi(x,y,z) = (x,y);\\
> \text{solving for } y: &\quad y = h(x,z), &\quad \psi : V \to \mathbb{R}^2, &\quad \psi(x,y,z) = (x,z).
> \end{aligned}
> $$
>
> The parametrization inverse to $\varphi$ is $\varphi^{-1}(x,y) = (x,\,y,\,g(x,y))$, and composing with $\psi$ — which reads off the first and third coordinates — gives the transition function
>
> $$
> \psi \circ \varphi^{-1}(x,y) = \big(x,\; g(x,y)\big),
> $$
>
> smooth because $g$ is. In the other direction $\varphi \circ \psi^{-1}(x,z) = \big(x,\, h(x,z)\big)$, smooth because $h$ is. So $(U,\varphi)$ and $(V,\psi)$ are compatible, and the same picture is what Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]] formalizes: the overlap of two charts is the part of the surface expressible as a graph over two different pairs of variables, and the transition function converts one graph into the other.

^ex-20-1

*Uses:* [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-1|§7.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]]

The same level sets are submanifolds in the sense of Lecture 12, and their graph-chart structure is the induced one (Proposition [[§35 Submanifolds#^prop-35-9|§35.9]]).

> [!remark] Remark
> The only thing that varies between charts is *which* $k$ coordinates are solved for, and the whole proof is the observation that a projection composed with a parametrization is smooth no matter which choice is made. Uribe made the same point while declining to write the general indices out: “the notation becomes a mess, but it's the same thing.” Note also that the charts are graphs of smooth maps, which is what makes the parametrization smooth — the topological argument of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]] only needed $h_J$ continuous.

^rem-20-3

![[m591-9-3.svg]]
*A patch $M$ of a surface with the gradient $\nabla F(p)$, and its two chart images: straight down onto the $xy$-plane, $\varphi(U)$, where $M$ is the graph $z = g(x,y)$, and sideways onto the $xz$-plane, $\psi(U)$, where it is the graph $y = h(x,z)$.*

The board picture for this example. The patch $M$ is drawn over a rectangle of $(x,y)$, and the two shaded regions are its images under the two charts: straight down onto the $xy$-plane, giving $\varphi(U)$ and presenting $M$ as $z = g(x,y)$; and sideways onto the $xz$-plane, giving $\psi(U)$ and presenting the *same* patch as $y = h(x,z)$. The transition function is the trip up from one shadow and down to the other.

The picture only works because $\partial F/\partial z$ and $\partial F/\partial y$ are *both* nonzero throughout the patch. If $\partial F/\partial y$ vanished anywhere — if the surface were vertical in the $y$-direction there — the sideways projection would fold over and $\psi$ would not be injective, so there would be no second chart and nothing to compare. Which pairs of variables work is a condition at each point, and in general it changes from point to point; that is the content of the index set $J$ in Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]].

**Transcription note.** The board wrote the parametrization as “$\psi^{-1}(x,y) = (x,y,g(x,y))$”; it is $\varphi^{-1}$, as the recording confirms. The board also wrote “$\varphi^{-1}|_{U \cap V} : U \cap V \to \mathbb{R}^{n+k}$” — but $\varphi^{-1}$ is defined on $\varphi(U \cap V) \subseteq \mathbb{R}^n$, not on $U \cap V$, which consists of points of the manifold. Two further slips in the statement of the regular value theorem: the value $c$ lies in $\mathbb{R}^k$, not $\mathbb{R}^{n+k}$; and the rank condition is on the Jacobian $F'(p)$, not on $F^{-1}(p)$.

> [!theorem] Lemma §20.3: Smooth Maps into and out of Regular Level Sets
> Let $M = F^{-1}(c)$ be a regular level set in $\mathbb{R}^{n+k}$, with the smooth structure of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]].
> 1. If $W' \subseteq \mathbb{R}^{n+k}$ is open and $H : W' \to \mathbb{R}^l$ is smooth, then the restriction $H|_{M \cap W'} : M \cap W' \to \mathbb{R}^l$ is smooth.
> 2. If $P$ is a smooth manifold and $G : P \to \mathbb{R}^{n+k}$ is smooth with $G(P) \subseteq M$, then $G$ is smooth as a map $P \to M$.
>
> *Lee: cf. Ch. 5, Restricting Maps to Submanifolds*

^lem-20-3

> [!proof]+ Proof
> (1) $M \cap W'$ is open in $M$. For a graph chart $(U_J, \varphi_J)$, the parametrization $\varphi_J^{-1}$ is smooth into $\mathbb{R}^{n+k}$, so the coordinate representation $H \circ \varphi_J^{-1}$ is a composite of smooth maps between open subsets of Euclidean spaces. (2) $G$ is continuous into $M$ for the subspace topology. Given $q \in P$, take a graph chart $(U_J, \varphi_J)$ of $M$ at $G(q)$ and a chart $(V, \chi)$ of $P$ at $q$ with $G(V) \subseteq U_J$ (shrink $V$ to $V \cap G^{-1}(U_J)$). Then $\varphi_J \circ G \circ \chi^{-1} = \pi_I \circ (G \circ \chi^{-1})$ is a linear projection of a smooth map, hence smooth.

^pf-20-3

*Uses:* [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§20 Manifolds in Euclidean Space#^def-20-3|Def. §20.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark]- Connections
> - The same statement for embedded submanifolds of any manifold: [[§35 Submanifolds#^lem-35-3|§35.3]].

Not stated in lecture; filled in because it is used repeatedly — tacitly in the proof of [[§24 The Circle#^prop-24-1|Proposition §24.1]], and explicitly for $S^n \to \mathbb{RP}^n$ in [[§39 Projective Spaces and the Hopf Fibration#^ex-39-1|Ex. §39.1]]. In words: maps *out of* a level set may be computed by restricting ambient formulas, and maps *into* one may be computed as maps into the ambient space.

That the three circle atlases define one smooth structure is collected in [[§24 The Circle|§24]].
