---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 22
tags: [differentiable-manifolds, math591]
---
← [[§21 Linear Algebra Toolkit]] · ↑ [[· 3 Smooth Structures]] · [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds]] →

*Stage: linear — The derivative of a map between finite-dimensional vector spaces, without coordinates — the model for the differential of a smooth map.*

*Lecture 7. “A careful analysis of what we did last time — last time I was rushing.” The $\mathrm{O}(n)$ argument computed a derivative by differentiating along straight lines and read off surjectivity from the result, without ever writing a Jacobian matrix. This section says exactly what that computes and why it is legitimate. “For now it's all linear algebra,” but it is also the template for the differential of a map between manifolds, to come.*

Throughout, $X$ and $Y$ are finite-dimensional real vector spaces, of dimensions $m$ and $n$, and $F : X \to Y$ is a map of sets.

> [!definition] Definition §22.1: Linear Coordinate System
> A **linear coordinate system** on $X$ is a linear isomorphism $L : X \to \mathbb{R}^m$ — equivalently, a choice of basis, $L$ sending a vector to its coordinate column.
>
> *Lee: Example 1.24*

^def-22-1

> [!remark]- Connections
> - In LADR this is the coordinate map v ↦ M(v) of a basis ([[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]]).

> [!definition] Definition §22.2: Coordinate Representation
> Given linear coordinate systems $L$ on $X$ and $K$ on $Y$ ([[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Definition §22.1]]), the **coordinate representation** of $F$ is
>
> $$
> \widetilde F = K \circ F \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^n .
> $$
>
> *Lee: Example 1.24*

^def-22-2

> [!remark]- Connections
> - In LADR the coordinate representation of a linear map is its matrix ([[§10 Invertibility and Isomorphisms#^ladr-3-76|LADR 3.76]]).

Since $L$ and $K$ are bijections, $\widetilde F$ is the unique map making the square commute:

![[m591-10-3.svg]]
*The coordinate representation $\widetilde F$ is $F$ read through the linear coordinate systems $L$ and $K$.*

$$
\widetilde F = K \circ F \circ L^{-1}.
$$

Commutativity means: apply $F$ and then take coordinates, or take coordinates and then apply $\widetilde F$; the result is the same. “$\widetilde F$ is just $F$ expressed in coordinates.”

> [!definition] Definition §22.3: Smooth Map Between Vector Spaces
> $F : X \to Y$ is **smooth** if $\widetilde F = K \circ F \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^n$ is smooth for any choice of linear coordinates $L, K$ — equivalently, by Lemma [[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]], for some choice.

^def-22-3

> [!theorem] Lemma §22.1: Independence of Coordinates
> If the coordinate representation $\widetilde F = K \circ F \circ L^{-1}$ of [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]] is smooth for one choice of linear coordinates $L$ on $X$ and $K$ on $Y$, it is smooth for every choice. Hence “any” in [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]] may be replaced by “some” — Uribe's “little observation” in Lecture 7.

^lem-22-1

> [!proof]+ Proof
> *(Not proved in lecture, where it was called “a little observation”; filled in.)* Let $L', K'$ be another choice, with $\widetilde F' = K' F L'^{-1}$; we show $\widetilde F'$ is smooth, given that $\widetilde F = K F L^{-1}$ is. Since $L$ and $K$ are bijections, $F$ can be recovered from $\widetilde F$:
>
> $$
> K^{-1} \circ \widetilde F \circ L = K^{-1} \circ K \circ F \circ L^{-1} \circ L = F .
> $$
>
> Substituting this expression for $F$ into the definition of $\widetilde F'$ gives
>
> $$
> \widetilde F' = K' \circ F \circ L'^{-1} = K' \circ \big(K^{-1} \circ \widetilde F \circ L\big) \circ L'^{-1} = (K' K^{-1}) \circ \widetilde F \circ (L L'^{-1}),
> $$
>
> and $K'K^{-1} : \mathbb{R}^n \to \mathbb{R}^n$, $LL'^{-1} : \mathbb{R}^m \to \mathbb{R}^m$ are linear isomorphisms, being composites of linear isomorphisms, hence smooth: by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3) each component of a linear map $\mathbb{R}^m \to \mathbb{R}^m$ is a linear function $\sum_j a_{ij} r^j$ of the coordinates, a polynomial. A composite of smooth maps between Euclidean spaces is smooth (chain rule), so $\widetilde F'$ is smooth.

^pf-22-1

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]], [[Multivariable Chain Rule|452 §12.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!theorem] Proposition §22.2: A Vector Space Is a Smooth Manifold
> Any two linear coordinate systems $L, L' : X \to \mathbb{R}^m$ on a finite-dimensional real vector space are $C^\infty$-compatible charts. Consequently $X$ carries a canonical smooth structure, the one generated by any single linear chart $(X, L)$, and a map $F : X \to Y$ is smooth in the sense of [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]] iff it is smooth in the sense of [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] for these structures.
>
> *Lee: Example 1.24*

^prop-22-2

> [!proof]+ Proof
> *Topology.* Give $X$ the topology transported from $\mathbb{R}^m$ by $L$: $U \subseteq X$ is open iff $L(U)$ is open. It is independent of $L$ since all norms on $\mathbb{R}^m$ are equivalent; concretely, for another linear coordinate system $L'$, $L'(U) = (L'L^{-1})\big(L(U)\big)$, and $L'L^{-1}$ is a linear isomorphism of $\mathbb{R}^m$, continuous with continuous (linear) inverse $LL'^{-1}$, i.e. a homeomorphism, so $L(U)$ is open iff $L'(U)$ is. With this topology $L$ is a homeomorphism of $X$ onto the open set $\mathbb{R}^m$, so $X$ is Hausdorff, second countable and locally Euclidean, like $\mathbb{R}^m$ — a topological $m$-manifold — and $(X, L)$ is a chart (Definition [[§2 Topological Manifolds#^def-2-3|§2.3]]).
>
> *Compatibility.* For two linear coordinate systems $L, L'$, the overlap of the charts $(X, L)$ and $(X, L')$ is $X$, and the transition function is $L' \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^m$, a linear isomorphism with linear inverse $L \circ L'^{-1}$. Linear maps of $\mathbb{R}^m$ are smooth (their components are linear polynomials, Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)), so $L' \circ L^{-1}$ is a smooth bijection with smooth inverse, a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]), and the two charts are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]).
>
> *The smooth structure.* A single chart is an atlas (Example [[§17 Differentiable Structures#^ex-17-1|§17.1]]), so by Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] the one-chart atlas $\{(X,L)\}$ determines a smooth structure, the unique maximal atlas $\overline{\{(X,L)\}}$ of charts compatible with $(X, L)$. It is the same structure for every $L$, by compatibility: $(X, L')$ is compatible with $(X, L)$, so $\overline{\{(X,L)\}}$ is a maximal atlas containing $\{(X, L')\}$, and by the uniqueness in Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] it equals $\overline{\{(X,L')\}}$.
>
> *Smooth maps.* For the last claim, the coordinate representation of $F$ in the linear charts $L$ and $K$ is precisely $K \circ F \circ L^{-1} = \widetilde F$. If $F$ is smooth in the sense of Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|§22.3]], then $F = K^{-1} \circ \widetilde F \circ L$ is continuous, as a composite of continuous maps, and at every $p \in X$ the charts $(X, L) \ni p$ and $(Y, K)$, with $F(X) \subseteq Y$, have smooth coordinate representation $\widetilde F$; so $F$ is smooth in the sense of Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]. Conversely, if $F$ is smooth in the sense of Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], then by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], applied to the smooth charts $(X, L)$ and $(Y, K)$ with $F(X) \subseteq Y$, the coordinate representation $K \circ F \circ L^{-1} = \widetilde F$ is smooth; so $F$ is smooth in the sense of Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|§22.3]].

^pf-22-2

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]], [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§2 Topological Manifolds#^def-2-3|Def. §2.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§17 Differentiable Structures#^ex-17-1|Ex. §17.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]

> [!remark]- Connections
> - The one-chart atlas on $\mathbb{R}^n$: [[§17 Differentiable Structures#^ex-17-1|Ex. §17.1]]; its tangent spaces are the vector space itself, [[§30 The Differential in Coordinates#^cor-30-6|§30.6]].

> [!definition] Definition §22.4: The Standard Smooth Structure on a Vector Space
> A finite-dimensional real vector space $X$ of dimension $m$ is given the topology for which one, hence every, linear coordinate system $L : X \to \mathbb{R}^m$ is a homeomorphism, and the smooth structure generated by one, hence every, **linear chart** $(X, L)$ — “hence every” by Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]. With these, $X$ is a smooth manifold of dimension $m$ whose linear coordinate systems are smooth charts.
>
> *Lee: Example 1.24*

^def-22-4

> [!remark] Remark
> This is the sense in which $\operatorname{Mat}(n,\mathbb{R})$, $\operatorname{Sym}(n,\mathbb{R})$, and $\operatorname{Mat}(n,\mathbb{C})$ are smooth manifolds without anyone having chosen coordinates on them. Uribe: “you can think of this as an abstract vector space that I make into a manifold by choosing a linear chart, and it won't matter which linear chart I choose — they are all smoothly compatible.”

^rem-22-1

Now suppose $F$ is smooth and fix $p \in X$. There is a second square, with the same vertical arrows but a *linear* map along the bottom: the linear map $\mathbb{R}^m \to \mathbb{R}^n$ given by the Jacobian matrix $\widetilde F'(\tilde p)$, where $\tilde p = L(p)$ is the coordinate vector of $p$.

> [!definition] Definition §22.5: The Differential
> Let $F : X \to Y$ be smooth and $p \in X$. Choose linear coordinates $L$ on $X$ and $K$ on $Y$, let $\widetilde F = K \circ F \circ L^{-1}$ be the coordinate representation ([[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]]), and put $\tilde p = L(p)$. The **differential** of $F$ at $p$ is the unique linear map $dF_p : X \to Y$ making the square commute:
>
> ![[m591-10-4.svg]]
>
> $$
> dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L.
> $$

^def-22-5

> [!theorem] Theorem §22.3: Coordinate-Free Formula for the Differential
> Let $F : X \to Y$ be smooth and $p, v \in X$. Then
>
> $$
> dF_p(v) \;=\; \frac{d}{dt}\Big|_{t=0} F(p + tv) \;=\; \lim_{t \to 0} \frac{1}{t}\big( F(p+tv) - F(p) \big).
> $$
>
> In particular $dF_p$ does not depend on the choice of bases used to define it.
>
> *Lee: cf. Corollary 3.25*

^thm-22-3

> [!proof]+ Proof
> Fix linear coordinates $L$ on $X$ and $K$ on $Y$ as in Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]], and write $\tilde p = L(p)$, $\tilde v = L(v)$. The plan: express the curve $t \mapsto F(p+tv)$ through $\widetilde F$, differentiate in coordinates by the chain rule, and recognise $dF_p(v)$.
>
> *The curve in coordinates.* The curve $t \mapsto p + tv$ in $X$ has coordinate curve $t \mapsto L(p+tv) = L(p) + t\,L(v) = \tilde p + t\,\tilde v$ in $\mathbb{R}^m$, by linearity of $L$. Since $\widetilde F \circ L = K \circ F \circ L^{-1} \circ L = K \circ F$, applying $K^{-1}$ gives
>
> $$
> F(p+tv) = K^{-1}\big( \widetilde F(L(p + tv)) \big) = K^{-1}\big( \widetilde F(\tilde p + t \tilde v) \big).
> $$
>
> *Differentiating in coordinates.* The map $c(t) = \widetilde F(\tilde p + t\tilde v)$ is a smooth curve in $\mathbb{R}^n$, the composite of the smooth $\widetilde F$ (smoothness of $F$, Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|§22.3]]) with the line $\gamma(t) = \tilde p + t\tilde v$, for which $\gamma(0) = \tilde p$ and $\gamma'(0) = \tilde v$. By the chain rule its velocity at $t = 0$ is the Jacobian applied to the direction:
>
> $$
> c'(0) = \frac{d}{dt}\Big|_0 \widetilde F(\tilde p + t\tilde v) = \widetilde F'(\gamma(0))\,\gamma'(0) = \widetilde F'(\tilde p)\,\tilde v .
> $$
>
> *Applying $K^{-1}$.* Since $K^{-1}$ is linear, it commutes with differentiation of curves: it is linear and continuous (a homeomorphism for the topology of Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), so
>
> $$
> \frac{d}{dt}\Big|_{t=0} K^{-1}(c(t)) = \lim_{t \to 0} \frac{1}{t}\big( K^{-1}c(t) - K^{-1}c(0) \big) = \lim_{t \to 0} K^{-1}\Big( \frac{c(t) - c(0)}{t} \Big) = K^{-1}\big( c'(0) \big) .
> $$
>
> Combining the three displays with the formula $dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L$ of Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]],
>
> $$
> \frac{d}{dt}\Big|_{t=0} F(p+tv) = K^{-1}\Big( \frac{d}{dt}\Big|_{t=0} \widetilde F(\tilde p + t\tilde v) \Big) = K^{-1}\big( \widetilde F'(\tilde p) L(v) \big) = dF_p(v).
> $$
>
> The second expression for $dF_p(v)$ is the definition of the derivative of the $Y$-valued curve $t \mapsto F(p+tv)$ at $t = 0$. The right-hand side of the displayed formula makes no reference to $L$ or $K$, so neither does $dF_p$: two choices of linear coordinates give linear maps with the same value at every $v$, hence the same map.

^pf-22-3

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-2|Def. §22.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[Multivariable Chain Rule|452 §12.2]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-3|Def. §22.3]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]]

> [!remark]- Connections
> - In $\mathbb{R}^n$ this is the [[Directional Derivative Formula|directional derivative formula, 452 §9.1]], with the differential of [[§10 The Differential#^def-10-1|452 Def. §10.1]].
> - On manifolds: agreement with the abstract differential, [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]; computing differentials by curves, [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]].

> [!remark] Remark
> Two things are worth isolating. First, the hypothesis that $F$ is smooth is used: it is what makes $\widetilde F$ differentiable so that the chain rule applies. A map can have all directional derivatives $\frac{d}{dt}\big|_0 F(p+tv)$ at a point without being differentiable there, and for such a map the formula defines nothing linear. Second, the formula uses the vector space structure of *both* spaces, in two different places: that of $X$ to form the line $p + tv$, and that of $Y$ to form the difference quotient $\frac1t\big(F(p+tv) - F(p)\big)$. Uribe stopped to ask the class where $Y$'s structure enters, and this is the answer. Neither can be dropped, which is why the same formula will *not* serve as the definition of the differential on a general manifold: there is no “$p + tv$” and no “$F(p+tv) - F(p)$.” That is the problem [[§25 The Geometric Tangent Space|§25]] begins to address.

^rem-22-2

> [!remark]- Connections
> - A witness for the first point, with every directional derivative at the origin but no derivative: [[§7 Differentiability#^rem-7-4|452 §7, Warning: The Converse Is False]].

> [!theorem] Corollary §22.4: Regular Values Without Coordinates
> Suppose $\dim X \ge \dim Y$ and $F : X \to Y$ is smooth, and let $\widetilde F = K \circ F \circ L^{-1}$ and $\tilde p = L(p)$ be taken in linear coordinates $L$, $K$, as in [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]]. Then for $p \in X$,
>
> $$
> \widetilde F'(\tilde p) \text{ has maximal rank } (= \dim Y) \iff dF_p : X \to Y \text{ is surjective},
> $$
>
> and this holds for one choice of coordinates iff for all. Hence $c \in Y$ is a regular value of $F$ iff $dF_p$ is surjective for every $p \in F^{-1}(c)$, a statement that involves no bases.

^cor-22-4

> [!proof]+ Proof
> Write $m = \dim X$ and $n = \dim Y$, so $m \ge n$ and $\widetilde F'(\tilde p)$ is an $n \times m$ matrix.
>
> *Maximal rank means surjective.* Since $m \ge n$, the maximal possible rank of an $n \times m$ matrix is $n$ (it has $n$ rows). The rank of $\widetilde F'(\tilde p)$ is the dimension of the image of the linear map $\mathbb{R}^m \to \mathbb{R}^n$ it defines (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)), so it has rank $n$ iff that image is all of $\mathbb{R}^n$, i.e. iff the map is surjective.
>
> *Bottom arrow surjective iff top arrow surjective.* In the square of Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]] the vertical arrows are bijections, and $dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L$, equivalently $\widetilde F'(\tilde p) = K \circ dF_p \circ L^{-1}$. If $\widetilde F'(\tilde p)$ is surjective and $y \in Y$, choose $a \in \mathbb{R}^m$ with $\widetilde F'(\tilde p)\,a = K(y)$; then $dF_p(L^{-1}a) = K^{-1}\big(\widetilde F'(\tilde p)\,a\big) = y$. If $dF_p$ is surjective and $b \in \mathbb{R}^n$, choose $x \in X$ with $dF_p(x) = K^{-1}(b)$; then $\widetilde F'(\tilde p)(Lx) = K\big(dF_p(x)\big) = b$. So the bottom arrow is surjective iff the top arrow $dF_p$ is.
>
> *Independence of coordinates.* The top arrow is independent of coordinates by Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], so surjectivity of $\widetilde F'(\tilde p)$ is too: if it holds for one choice $L, K$, then $dF_p$ is surjective, and by the previous paragraph applied to any other choice $L', K'$, the Jacobian of $K' F L'^{-1}$ at $L'(p)$ is surjective as well.
>
> *Regular values.* Read in linear coordinates, $c$ is a regular value of $F$ when $K(c)$ is a regular value of $\widetilde F$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]): $\widetilde F'(\tilde q)$ is surjective at every $\tilde q \in \widetilde F^{-1}(K(c))$ (Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]]). These points are exactly the $\tilde q = L(q)$ with $q \in F^{-1}(c)$, since $\widetilde F(L(q)) = K(F(q))$ equals $K(c)$ iff $F(q) = c$ ($K$ is injective) and $L$ is a bijection. By the equivalence above at each such $q$, $c$ is a regular value iff $dF_q$ is surjective for every $q \in F^{-1}(c)$, a statement that involves no bases.

^pf-22-4

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]]

> [!remark]- Connections
> - The manifold versions of this definition of regular value: [[§30 The Differential in Coordinates#^def-30-4|Def. §30.4]], [[§36 Submersions#^def-36-4|Def. §36.4]].

> [!remark] Remark: What the Curve Method Computes
> Read together, Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]] and Corollary [[§22 The Differential of a Map Between Vector Spaces#^cor-22-4|§22.4]] are the license for the computation in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|The Orthogonal Group as a Smooth Manifold]]. The board computation $\frac{d}{dt}\big|_0 F(g + tA)$ is not a shortcut around the Jacobian — it *is* the Jacobian, packaged as the linear map $A \mapsto dF_g(A)$ and read off without coordinates; and the surjectivity of that linear map *is* the maximal-rank condition, likewise without coordinates. Written as a matrix, $dF_g$ for $\mathrm{O}(n)$ would have $n(n+1)/2$ rows and $n^2$ columns of partial derivatives. None of it is needed. “Using curves to compute differentials is a basic technique in this subject.”

^rem-22-3
