---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 34
tags: [differentiable-manifolds, math591]
---
← [[§33 Local Diffeomorphisms]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§35 Submanifolds]] →

*Stage: maps — Maps with surjective differentials: locally projections, by the normal form — the tool that makes the regular value theorem work on any manifold ([[§35 Submanifolds|§35]]).*

> [!definition] Definition §34.1: Submersion
> Let $F : M \to N$ be smooth and $p \in M$. $F$ is a **submersion at $p$** if $F_{\ast p}$ is onto, and a **submersion** if it is a submersion at every point.
>
> *Lee: Ch. 4, Maps of Constant Rank*

^def-34-1

> [!remark]- Connections
> - Submersion at $p$ = regular point: [[§30 The Differential in Coordinates#^def-30-2|Def. §30.2]], [[§34 Submersions#^def-34-3|Def. §34.3]].

> [!definition] Definition §34.2: Immersion
> Let $F : M \to N$ be smooth and $p \in M$. $F$ is an **immersion at $p$** if $F_{\ast p}$ is injective, and an **immersion** if it is one at every point.
>
> *Lee: Ch. 4, Maps of Constant Rank*

^def-34-2

> [!remark]- Connections
> - The lecture's definition of immersion, with its normal form: [[§37 Immersions#^def-37-1|Def. §37.1]], [[§37 Immersions#^thm-37-1|§37.1]].

The submersion half is the lecture's definition. Immersions were listed as the third special type and treated in Lecture 13 ([[§37 Immersions|§37]]); the definition is recorded here in Lee's form so that the three types can be compared. In the language of Definition [[§30 The Differential in Coordinates#^def-30-2|§30.2]], $F$ is a submersion at $p$ exactly when $p$ is a regular point.

> [!theorem] Proposition §34.1: Dimension Constraints
> Let $F : M \to N$ be smooth, $m = \dim M$, $n = \dim N$, and $p \in M$.
> 1. If $F$ is a submersion at $p$ then $n \le m$; if $F$ is an immersion at $p$ then $m \le n$.
> 2. $F$ is a local diffeomorphism if and only if it is both a submersion and an immersion; in that case $m = n$.
> 3. If $m = n$ and $F$ is a submersion, or an immersion, at every point, then $F$ is a local diffeomorphism.
>
> *Lee: Proposition 4.8*

^prop-34-1

> [!proof]+ Proof
> (1) By rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), a surjective linear map $T_pM \to T_{F(p)}N$ forces $n \le m$, and an injective one forces $m \le n$. (2) A linear map is bijective if and only if it is injective and surjective, so this is Theorem [[§33 Local Diffeomorphisms#^thm-33-2|§33.2]]; then (1) gives $m = n$. (3) Between spaces of the same finite dimension, a linear map is injective iff surjective iff bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)); apply Theorem [[§33 Local Diffeomorphisms#^thm-33-2|§33.2]].

^pf-34-1

*Uses:* [[§34 Submersions#^def-34-1|Def. §34.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§33 Local Diffeomorphisms#^thm-33-2|§33.2]], [[Fundamental theorem of linear maps|LADR 3.21]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!example] Example §34.1: Projections Are Submersions
> The projection $\pi : \mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$, $(x, y) \mapsto x$, is a submersion.

^ex-34-1

> [!proof]+ Proof
> By Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] the differential is the Jacobian $\big(I_k \mid 0\big)$, a $k \times (k+l)$ matrix of rank $k$.

^pf-ex-34-1

*Uses:* [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§34 Submersions#^def-34-1|Def. §34.1]]

**Transcription note.** Page 28 of the handwritten notes writes the projection as $\mathbb{R}^m \times \mathbb{R}^l \to \mathbb{R}^k$; for a projection onto a factor the factor must be the target, $\mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$. Projections of *product manifolds* $M_1 \times M_2 \to M_1$ are submersions for the same reason, but that needs the tangent space of a product — “they will be direct sums of tangent spaces” — which Uribe postponed to the next lecture.

Lecture 11 supplied it (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]):

> [!example] Example §34.2: Projections of Product Manifolds Are Submersions
> The projection $\pi_1 : M_1 \times M_2 \to M_1$ is a submersion, and so is $\pi_2$.
>
> *Lee: Proposition 3.14*

^ex-34-2

> [!proof]+ Proof
> $\pi_{1*}\big(\Theta(v, w)\big) = \pi_{1*}\iota_{1*}v + \pi_{1*}\iota_{2*}w = v$, by the proof of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]; so $\pi_{1*}$ is onto $T_{p_1}M_1$.

^pf-ex-34-2

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§34 Submersions#^def-34-1|Def. §34.1]]

The projection $S^{2n+1} \to \mathbb{CP}^n$, a submersion, is collected in [[§39 Projective Spaces and the Hopf Fibration|§39]].

> [!definition] Definition §34.3: Regular Points and Critical Points
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$.
> 1. $p \in M$ is a **regular point** of $F$ if $F$ is a submersion at $p$, i.e. $F_{\ast p}$ is onto — which forces $n \le m$. Otherwise $p$ is a **critical point**, also called a **singular point**.

^def-34-3

> [!remark]- Connections
> - The two earlier definitions of regular point: [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]] (Euclidean, Lecture 3) and [[§30 The Differential in Coordinates#^def-30-2|Def. §30.2]] (manifolds, via rank).

> [!definition] Definition §34.4: Regular Values and Critical Values
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$.
> 2. $q \in N$ is a **regular value** of $F$ if $F$ is a submersion at every $p \in F^{-1}(q)$, and a **critical value** otherwise.
> 3. In particular every $q \notin F(M)$ is a regular value: its preimage is empty, and “everything is true for the empty set.”
>
> These are the notions of Definitions [[§30 The Differential in Coordinates#^def-30-2|§30.2]] and [[§30 The Differential in Coordinates#^def-30-3|§30.3]], now with critical points and the empty-preimage convention made explicit; for maps between open subsets of Euclidean spaces they are those of Definitions [[§7 The Regular Value Theorem#^def-7-3|§7.3]] and [[§7 The Regular Value Theorem#^def-7-4|§7.4]].

^def-34-4

> [!remark]- Connections
> - The two earlier definitions of regular value: [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]] (Euclidean, Lecture 3) and [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]] (manifolds, via rank).

Uribe called (3) “kind of a trivial way to be [regular], but important”: it matters in Sard's theorem, about the set of regular values, which is still to come. **Transcription note.** Page 29 of the handwritten notes has “if $q \in \operatorname{Im} F$, then $q$ is regular”; the audio has “if $q$ is not in the image of $F$”, as in (3). The same page writes the preimage in (2) as $F^{-1}(p)$ for $F^{-1}(q)$.

> [!theorem] Proposition §34.2: Critical Points of Real-Valued Functions
> Let $f : M \to \mathbb{R}$ be smooth. Then $df_p$ is either onto or zero, so
>
> $$
> p \text{ is a critical point of } f \iff df_p = 0 \iff \frac{\partial f}{\partial x^i}(p) = 0 \text{ for all } i,
> $$
>
> in any chart at $p$.
>
> *Lee: Exercise 11.24*

^prop-34-2

> [!proof]+ Proof
> The image of the linear map $df_p$ is a subspace of the one-dimensional $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ (Definition [[§32 The Cotangent Space#^def-32-1|§32.1]]), so it is $0$ or everything — “dimensions of images cannot be fractional.” The second equivalence is Lemma [[§32 The Cotangent Space#^lem-32-2|§32.2]].

^pf-34-2

*Uses:* [[§34 Submersions#^def-34-3|Def. §34.3]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]], [[§32 The Cotangent Space#^lem-32-2|§32.2]]

> [!remark]- Connections
> - In $\mathbb{R}^n$, critical points are where extrema can occur: [[§17 Optimization and Lagrange Multipliers#^thm-17-1|452 §17.1]] (Fermat's theorem).

This is the definition of critical point Uribe sent to the class by email, and it agrees with Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]] for $m = 1$: there $p$ is regular iff $\nabla F(p) \ne 0$.

> [!theorem] Lemma §34.3: Diffeomorphisms onto Open Sets Are Charts
> Let $U \subseteq M$ be open and $\hat\varphi : U \to \mathbb{R}^m$ smooth, with $\hat\varphi(U)$ open and $\hat\varphi : U \to \hat\varphi(U)$ a diffeomorphism. Then $(U, \hat\varphi)$ is a smooth chart of $M$.
>
> *Lee: cf. Ch. 2, Diffeomorphisms*

^lem-34-3

> [!proof]+ Proof
> It is a homeomorphism onto an open subset of $\mathbb{R}^m$, so it is a chart. For any smooth chart $(W, \chi)$ of $M$, the transition maps $\hat\varphi \circ \chi^{-1}$ and $\chi \circ \hat\varphi^{-1}$ are coordinate representations of $\hat\varphi$ and $\hat\varphi^{-1}$, smooth because these maps are (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]). So $(U, \hat\varphi)$ is compatible with every chart of the maximal atlas, and therefore belongs to it (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).

^pf-34-3

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

> [!theorem] Theorem §34.4: Local Normal Form for Submersions
> Let $F : M \to N$ be a submersion at $p$, with $\dim M = m$ and $\dim N = n$. Then there are charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$ is the projection onto the first $n$ coordinates:
>
> $$
> \tilde F\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^n\big).
> $$
>
> Equivalently, with coordinate functions $x^i = r^i \circ \varphi$ on $U$ and $y^j = r^j \circ \psi$ on $V$: $\;y^j \circ F = x^j$ on $U$ for $j = 1, \ldots, n$. In particular $n \le m$.
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-34-4

> [!remark]- Connections
> - The counterpart for immersions: [[§37 Immersions#^thm-37-1|§37.1]]. The main application: the regular value theorem for manifolds, [[§35 Submanifolds#^thm-35-6|§35.6]].

Stated in Lecture 10 and proved in Lecture 11, below. The inequality $n \le m$ needs no theorem — a surjective linear map cannot raise dimension — but the normal form does: it says that every submersion, in suitable coordinates, *is* a projection.

![[m591-14-3.svg]]
*The normal form as a square: in the charts $\varphi$ and $\psi$ of the theorem, $F$ becomes the projection $(r^1, \ldots, r^m) \mapsto (r^1, \ldots, r^n)$.*

![[m591-14-4.svg]]
*What the normal form says, for $m = 2$ and $n = 1$. Left: near $p$ the fibres $F^{-1}(c)$ of a submersion are curves, one through each point, which $F$ collapses to the points of an interval. Right: in the charts of the theorem the fibres are straightened into vertical lines, and $\tilde F$ forgets the second coordinate. Every submersion looks, locally and up to a change of coordinates, like the projection of Example [[§34 Submersions#^ex-34-1|§34.1]].*

*Lecture 11. “Back to submersions.” Uribe now made the vocabulary official, with the letters matched to the dimensions: $\dim M = m$ and $\dim N = n$. (In [[§7 The Regular Value Theorem|§7]], following the earlier lecture, $F : \mathbb{R}^N \to \mathbb{R}^m$ had $m$ as the dimension of the target.)*

Uribe singled out Lemma [[§34 Submersions#^lem-34-3|§34.3]] as “an intellectual step that should not be overlooked”: in the proof below, a map is shown to be a local diffeomorphism, and this lemma is what makes it a coordinate system.

> [!proof]+ Proof (Lecture 11)
> The steps are the lecture's, in the lecture's order. Sentences marked *(Completion.)* fill in details the lecture passed over.
>
> *1. Start with any coordinates.* “I start with any coordinates”: smooth charts $(U_0, \varphi_0 = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U_0) \subseteq V$. *(Completion.)* Such charts exist: take any charts and replace $U_0$ by the open set $U_0 \cap F^{-1}(V)$.
>
> *2. The components and their matrix.* As before, define the components of $F$, $F^j = y^j \circ F : U_0 \to \mathbb{R}$. The submersion condition says that the matrix
>
> $$
> J = \Big[\frac{\partial F^j}{\partial x^i}(p)\Big]
> $$
>
> has rank $n$. It “has $m$ columns, which are the $x$'s, and $n$ rows, that are the gradients” of the $F^j$. *(Completion.)* By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $J$ is the matrix of $F_{\ast p}$ in the coordinate bases, and $F_{\ast p}$ is onto, so $J$ has rank $n$.
>
> *3. “It's the same matrix.”* A student asked whether the matrix should be written with $\tilde F$. Uribe: “It's the same thing… That's how we define partials. We define them by going downstairs and taking the ordinary partial derivative downstairs. So it's the same matrix.” That is Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]: writing $G = \psi \circ F \circ \varphi_0^{-1}$ for the coordinate representation in these first charts (the lecture's $\tilde F$ at this stage),
>
> $$
> \frac{\partial F^j}{\partial x^i}(p) = \frac{\partial G^j}{\partial r^i}\big(\varphi_0(p)\big), \qquad J = G'\big(\varphi_0(p)\big).
> $$
>
> *4. Reindex — “the only thing we need to do.”* $J$ has $n$ linearly independent columns; “I just put them at the beginning.” Rearranging the $x^i$, we can write $J$ in block form
>
> $$
> J = \big(\, A \ \big|\ B \,\big), \qquad A \text{ an } n \times n \text{ non-singular matrix}, \quad B \text{ of size } n \times (m - n),
> $$
>
> where $B$ is “the stuff that remains here that I'm not going to care about.” *(Completion.)* Rearranging the coordinates replaces $\varphi_0$ by $P \circ \varphi_0$ for a permutation $P$ of $\mathbb{R}^m$. This is again a smooth chart: a chart by Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]], and its transition maps are those of $\varphi_0$ composed with the linear map $P$ or $P^{-1}$, hence smooth. It permutes the columns of $J$ in the same way.
>
> *5. The coordinates we want.* “The thing to do, you see, is to take the first $n$ components of $F$ as the first $n$ coordinate functions, and then we keep the remaining ones”:
>
> $$
> \hat\varphi = \big(F^1, \ldots, F^n, x^{n+1}, \ldots, x^m\big) : U_0 \to \mathbb{R}^m .
> $$
>
> *(Completion.)* This makes sense because $n \le m$ — the theorem's “in particular”, true since $F_{\ast p}$ is onto (Proposition [[§34 Submersions#^prop-34-1|§34.1]]) — so there are $m - n \ge 0$ remaining coordinates. $\hat\varphi$ is smooth because its components are. It has $m$ components, so it maps into $\mathbb{R}^m$ (see the transcription note below).
>
> *6. The claim.* $\hat\varphi$ is a local diffeomorphism in a neighbourhood of $p$.
>
> *7. The Jacobian of $\hat\varphi$ in the old coordinates.* “Gradient across”: the first $n$ rows are the gradients of $F^1, \ldots, F^n$, which give the matrix $J = (A \mid B)$; the last $m - n$ rows are the gradients of $x^{n+1}, \ldots, x^m$. These give the $(m-n) \times (m-n)$ identity, and zero in the first $n$ columns, “because I would be taking partials of these $x$'s with respect to $x$'s that come before.” So
>
> $$
> \begin{pmatrix} A & B \\ 0 & I_{m-n} \end{pmatrix},
> $$
>
> and “by the block nature, the fact that we have a big zero there, this is non-degenerate” at $p$: its determinant is $\det A \ne 0$. *(Completion.)* “The Jacobian of $\hat\varphi$ in the $x$-coordinates” is the Jacobian at $\varphi_0(p)$ of the ordinary map $H = \hat\varphi \circ \varphi_0^{-1} : \varphi_0(U_0) \to \mathbb{R}^m$. Its rows are the partials of the components of $\hat\varphi$ by Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], applied with the identity chart on $\mathbb{R}^m$, and $\partial x^k/\partial x^i = \delta^k_i$ gives the identity and zero blocks.
>
> *8. The inverse function theorem, “possibly after shrinking $U$.”* By the inverse function theorem (Theorem [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]]), possibly after shrinking, $\hat\varphi$ is a diffeomorphism onto $\hat\varphi(U)$. *(Completion.)* The theorem gives an open $W \ni \varphi_0(p)$, contained in $\varphi_0(U_0)$, with $H|_W$ a diffeomorphism onto the open set $H(W) \subseteq \mathbb{R}^m$. Put $U = \varphi_0^{-1}(W)$, an open neighbourhood of $p$. Then $\hat\varphi|_U = H|_W \circ \varphi_0|_U$ is a composite of diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), mapping $U$ onto the open set $\hat\varphi(U) = H(W)$.
>
> *9. The intellectual step: $\hat\varphi$ is a chart.* “There's an intellectual step here that should not be overlooked. If I have a local diffeomorphism like this from an open set in $M$ into its image, which is open in $\mathbb{R}^m$, that is a chart”: it is a homeomorphism, and being smooth with smooth inverse makes it compatible with every other smooth chart, so it lies in the maximal atlas. This is Lemma [[§34 Submersions#^lem-34-3|§34.3]]. So $(U, \hat\varphi)$ is a smooth chart at $p$, and $F(U) \subseteq F(U_0) \subseteq V$.
>
> *10. Do not change the $y$-coordinates.* The chart $(V, \psi)$ on $N$ stays as it was. Only the chart on $M$ is new.
>
> *11. Going up and coming down.* Let $\tilde F = \psi \circ F \circ \hat\varphi^{-1} : \hat\varphi(U) \to \psi(V)$ be the coordinate representation of $F$ in the new chart. “I take a point down here, $r^1$ up to $r^m$, and I go upstairs”: going up means finding the point $q = \hat\varphi^{-1}(r)$ of $U$ whose values of the first $n$ functions $F^1, \ldots, F^n$ are the first $n$ coordinates of $r$. By the definition of $\hat\varphi$,
>
> $$
> F^i\big(\hat\varphi^{-1}(r^1, \ldots, r^m)\big) = r^i \qquad (i = 1, \ldots, n).
> $$
>
> Coming back down by $\psi$, the $i$-th coordinate of $\tilde F(r)$ is $y^i(F(q)) = F^i(q) = r^i$. So $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$: “this coordinate system labels every point in $U$; the first $n$ labels are the values of the $F$'s at that point.”

^pf-34-4

*Uses:* [[§34 Submersions#^def-34-1|Def. §34.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§34 Submersions#^prop-34-1|§34.1]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§34 Submersions#^lem-34-3|§34.3]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

![[m591-14-5.svg]]
*The change of chart in one diagram. The first chart $\varphi_0$ and the new chart $\hat\varphi$ differ by $H$, a diffeomorphism near $\varphi_0(p)$ by step 8. In the new chart, $F$ becomes $\tilde F$, the projection (step 11). The lecture used the letters $\phi$ and $\tilde F$ both for the first charts and for the new ones. The notes write $\varphi_0$ and $G$ for the first, and $\hat\varphi$ and $\tilde F$ for the new, to keep the two stages apart.*

**Transcription note.** In the lecture, $\hat\varphi$ was twice called “a map from $U$ into $\mathbb{R}^n$”, and page 30 of the handwritten notes writes $\phi : U \to \mathbb{R}$; it has $m$ components, so $\hat\varphi : U \to \mathbb{R}^m$. The matrix of partials was spoken as “$\partial x^j/\partial x^i$”, for $\partial F^j/\partial x^i$.

> [!theorem] Corollary §34.5: Being a Submersion Is an Open Condition
> If $F : M \to N$ is a submersion at $p$, then $F$ is a submersion at every point of some neighbourhood of $p$.
>
> *Lee: Proposition 4.1*

^cor-34-5

> [!proof]+ Proof
> In the charts of the theorem, $\tilde F$ is the projection, whose Jacobian $(I_n \mid 0)$ has rank $n$ at every point of $\hat\varphi(U)$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $F_{*q}$ is onto for every $q \in U$.

^pf-34-5

*Uses:* [[§34 Submersions#^thm-34-4|§34.4]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]

> [!theorem] Corollary §34.6: Submersions Are Open Maps
> If $F : M \to N$ is a submersion, then $F(W)$ is open in $N$ for every open $W \subseteq M$.
>
> *Lee: Proposition 4.28*

^cor-34-6

> [!proof]+ Proof
> Let $q = F(p)$ with $p \in W$, and take the charts of the theorem at $p$, shrinking $U$ to $U \cap W$. Then $F(U) = \psi^{-1}\big(\mathrm{pr}(\hat\varphi(U))\big)$, where $\mathrm{pr} : \mathbb{R}^m \to \mathbb{R}^n$ is the projection onto the first $n$ coordinates. Projections are open (Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]]), and $\hat\varphi(U)$ is open, so $\mathrm{pr}(\hat\varphi(U))$ is an open subset of $\psi(V)$, and $F(U)$ is open in $N$. It contains $q$ and lies in $F(W)$.

^pf-34-6

*Uses:* [[§34 Submersions#^thm-34-4|§34.4]], [[§4 Quotient Spaces and Open Maps#^ex-4-2|Ex. §4.2]]

> [!theorem] Theorem §34.7: Submersions from Compact Manifolds
> Let $M$ be compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]) and nonempty, $N$ connected ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]), and $F : M \to N$ a submersion ([[§34 Submersions#^def-34-1|Def. §34.1]]). Then $F$ is surjective, and $N$ is compact.

^thm-34-7

> [!proof]+ Proof
> *(Assignment 4, Problem 2, where $N = \mathbb{R}^k$; the same argument gives the general statement.)* $F(M)$ is open in $N$ because a submersion is an open map (Corollary [[§34 Submersions#^cor-34-6|§34.6]]), and compact, hence closed in the Hausdorff space $N$, because $M$ is compact. It is nonempty, and $N$ is connected, so $F(M) = N$. Then $N = F(M)$ is compact.

^pf-34-7

*Uses:* [[§34 Submersions#^cor-34-6|§34.6]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§18 Compact Spaces#^thm-18-3|590 §18.3]], [[§18 Compact Spaces#^thm-18-4|590 §18.4]], [[§15 Connected Spaces#^lem-15-1|590 §15.1]]

> [!remark]- Connections
> - The point-set steps: [[Continuous Image of a Compact Space is Compact|590 §18.3]], [[Compact Subspace of a Hausdorff Space is Closed|590 §18.4]], and clopen subsets of a connected space, [[§15 Connected Spaces#^lem-15-1|590 Lem. §15.1]]; in 591, [[§1 Point-Set Topology Review#^prop-1-8|§1.8]] and [[§1 Point-Set Topology Review#^prop-1-7|§1.7]].

> [!theorem] Corollary §34.8: No Submersions from Compact Manifolds to Euclidean Space
> If $M$ is compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]) and nonempty and $k \ge 1$, there is no submersion ([[§34 Submersions#^def-34-1|Def. §34.1]]) $M \to \mathbb{R}^k$.

^cor-34-8

> [!proof]+ Proof
> *(Assignment 4, Problem 2.)* $\mathbb{R}^k$ is connected but not compact, since it is unbounded; apply Theorem [[§34 Submersions#^thm-34-7|§34.7]].

^pf-34-8

*Uses:* [[§34 Submersions#^thm-34-7|§34.7]], [[§16 Connected Subspaces of ℝ#^thm-16-1|590 §16.1]], [[§15 Connected Spaces#^thm-15-6|590 §15.6]], [[Heine–Borel Theorem|590 §18.12]]

> [!remark]- Connections
> - Compact subsets of $\mathbb{R}^k$ are bounded: [[Heine–Borel Theorem]].

The submitted solution also noted the edge cases: for $k = 0$ the constant map $M \to \mathbb{R}^0$ is a submersion, since every differential maps onto the zero space; and for $M = \emptyset$ the empty map is vacuously one. In particular, a compact manifold carries no nonconstant submersion to $\mathbb{R}$ — the maximum of any smooth function $f : M \to \mathbb{R}$ is a [[§34 Submersions#^def-34-3|critical point]].

![[m591-29-1.svg]]
*A compact $M$ (a sphere) and its height function $h : M \to \mathbb{R}$. The image $h(M) = [a, b]$ is compact and nonempty but not open in $\mathbb{R}$. At the top and bottom points $p_{\max}$ and $p_{\min}$ (red) the tangent planes are horizontal, so $dh = 0$ there: they are [[§34 Submersions#^def-34-3|critical points]] ([[§34 Submersions#^prop-34-2|§34.2]]), and $h$ is not a submersion. The box is the proof of [[§34 Submersions#^thm-34-7|Theorem §34.7]] and [[§34 Submersions#^cor-34-8|Corollary §34.8]]: the image of a submersion would be open ([[§34 Submersions#^cor-34-6|§34.6]]) as well as compact, hence closed, hence all of the connected $\mathbb{R}^k$, which is not compact. (Drawn for these notes in the vault; not in the course tex.)*
