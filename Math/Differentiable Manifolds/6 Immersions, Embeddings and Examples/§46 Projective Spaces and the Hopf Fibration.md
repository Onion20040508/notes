---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 46
tags: [differentiable-manifolds, math591]
---
← [[§45 Geometric and Abstract Manifolds]] · ↑ [[· 6 Immersions, Embeddings and Examples]] · [[§47 The Unit Quaternions and SU(2)]] →

*Stage: bundles — The maps of this chapter on projective spaces: $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism, and $S^{2n+1} \to \mathbb{CP}^n$ is a submersion and a fibration, the Hopf fibration, with local sections but no global one.*

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Complex Projective Space|Complex Projective Space]], an orbit map in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; the first is the quotient map of [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; *this section* shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§48 SU(2) → SO(3)꞉ The Double Cover#^thm-48-4|The Double Cover]].

> [!example] Example §46.1: Spheres Cover Projective Spaces
> The projection $\pi : S^n \to \mathbb{RP}^n$, $x \mapsto [x]$, is a local diffeomorphism, exactly two-to-one.

^ex-46-1

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* Three things are claimed: $\pi$ is smooth; it is a local diffeomorphism, that is (Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]), every $x \in S^n$ has a neighbourhood $U$ that $\pi$ maps onto a neighbourhood $V$ of $\pi(x)$ with $\pi|_U^V$ having a smooth inverse; and every fibre of $\pi$ has exactly two points.
>
> *Setup.* Use coordinates $x_0, \ldots, x_n$ on $\mathbb{R}^{n+1}$, matching the charts $(U_i, \varphi_i)$ of Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]: $U_i = \{[x] \mid x_i \neq 0\}$ and $\varphi_i([x]) = (x_k/x_i)_{k \neq i}$. Whether $x_i \neq 0$ does not depend on the representative, since $(\lambda x)_i = \lambda x_i$ with $\lambda \neq 0$. Give $S^n = \{|x|^2 = 1\}$ its level-set structure (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]), so that Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]] applies to maps out of and into $S^n$. For each $i$ and $\varepsilon = \pm 1$ let
>
> $$
> U_i^\varepsilon = \{x \in S^n \mid \varepsilon x_i > 0\},
> $$
>
> the open hemisphere; it is the intersection of $S^n$ with an open half-space of $\mathbb{R}^{n+1}$, hence open in $S^n$. Every $x \in S^n$ is nonzero, so some $x_i \neq 0$, and then $x \in U_i^\varepsilon$ for $\varepsilon$ the sign of $x_i$: the $2(n+1)$ hemispheres cover $S^n$.
>
> *$\pi$ maps $U_i^\varepsilon$ bijectively onto $U_i$.* If $x \in U_i^\varepsilon$ then $x_i \neq 0$, so $\pi(x) = [x] \in U_i$. Conversely, a point of $U_i$ is a line $[x]$ with $x_i \neq 0$; it meets $S^n$ in the two points $\pm x/|x|$, whose $i$-th coordinates $\pm x_i/|x|$ are nonzero and of opposite signs, so exactly one of them lies in $U_i^\varepsilon$. So $\pi$ maps $U_i^\varepsilon$ bijectively onto $U_i$: a line not contained in $\{x_i = 0\}$ meets $U_i^\varepsilon$ exactly once.
>
> *$\pi$ in the chart.* In the chart $\varphi_i$, for $x \in U_i^\varepsilon$,
>
> $$
> \varphi_i \circ \pi(x) = \varphi_i([x]) = (x_k/x_i)_{k \neq i}.
> $$
>
> The right side is the map $H(x) = (x_k/x_i)_{k \neq i}$, smooth on the open set $W' = \{x_i \neq 0\} \subseteq \mathbb{R}^{n+1}$ (each component is a quotient of coordinate functions with nonvanishing denominator), restricted to $S^n \cap W'$ and then to its open subset $U_i^\varepsilon$; hence $h = \varphi_i \circ \pi|_{U_i^\varepsilon} : U_i^\varepsilon \to \mathbb{R}^n$ is smooth by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](1).
>
> *The inverse of $h$.* For $y \in \mathbb{R}^n$ let $\hat y \in \mathbb{R}^{n+1}$ be $y$ with a $1$ inserted in slot $i$, and put $\kappa(y) = \varepsilon\,\hat y/|\hat y|$. Since $|\hat y| \ge 1$, $\kappa$ is smooth from $\mathbb{R}^n$ into $\mathbb{R}^{n+1}$. Its values have $|\kappa(y)| = 1$ and $\varepsilon\, \kappa(y)_i = \varepsilon^2/|\hat y| = 1/|\hat y| > 0$, so they lie in $U_i^\varepsilon$; by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2) $\kappa$ is smooth into $S^n$, hence into its open subset $U_i^\varepsilon$ (an open subset carries the restricted charts). The two maps are mutually inverse. For $y \in \mathbb{R}^n$, the $k$-th component of $h(\kappa(y))$ is
>
> $$
> \frac{\kappa(y)_k}{\kappa(y)_i} = \frac{\varepsilon\,\hat y_k/|\hat y|}{\varepsilon/|\hat y|} = \hat y_k = y_k \qquad (k \neq i).
> $$
>
> For $x \in U_i^\varepsilon$, $h(x) = (x_k/x_i)_{k \neq i}$, so $\widehat{h(x)} = x/x_i$ (its $i$-th entry is $x_i/x_i = 1$), with norm $|x|/|x_i| = 1/|x_i|$; and $\varepsilon x_i > 0$ gives $|x_i| = \varepsilon x_i$, i.e. $\varepsilon |x_i| = x_i$. Hence
>
> $$
> \kappa(h(x)) = \varepsilon\, \frac{x}{x_i}\, |x_i| = \frac{\varepsilon |x_i|}{x_i}\, x = x .
> $$
>
> So $h = \varphi_i \circ \pi$ is a diffeomorphism of $U_i^\varepsilon$ onto $\mathbb{R}^n$, with inverse $y \mapsto \varepsilon\,\hat y/|\hat y|$.
>
> *Local diffeomorphism.* The chart $\varphi_i : U_i \to \varphi_i(U_i) = \mathbb{R}^n$ is a diffeomorphism by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]. Hence
>
> $$
> \pi|_{U_i^\varepsilon} = \varphi_i^{-1} \circ (\varphi_i \circ \pi) = \varphi_i^{-1} \circ h : U_i^\varepsilon \to U_i
> $$
>
> is a composite of diffeomorphisms, a diffeomorphism onto the open set $U_i$, with inverse $\kappa \circ \varphi_i$. In particular $\pi$ is smooth on each of the open sets $U_i^\varepsilon$, which cover $S^n$; since smoothness is checked near each point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), $\pi$ is smooth. For $x \in U_i^\varepsilon$ the neighbourhoods $U = U_i^\varepsilon$ of $x$ and $V = U_i$ of $\pi(x)$ satisfy Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]], with local inverse $\kappa \circ \varphi_i$.
>
> *Exactly two-to-one.* The hemispheres cover $S^n$, as shown in the setup. Let $x \in S^n$. A point $y \in S^n$ has $\pi(y) = \pi(x)$ iff $y$ lies on the line through $x$, i.e. $y = \lambda x$ with $\lambda \in \mathbb{R}^\times$, and then $1 = |y| = |\lambda|$, so $\lambda = \pm 1$. Hence $\pi^{-1}(\pi(x)) = \{x, -x\}$, two distinct points since $x \neq 0$; in particular $\pi(x) = \pi(-x)$.

^pf-ex-46-1

*Uses:* [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

> [!remark]- Connections
> - As a covering map of topological spaces, for $n = 2$: [[§38 Fundamental Group of Some Surfaces#^thm-38-1|590 §38.1]] ($S^2 \to P^2$ is a covering map).

> [!example] Example §46.2: The Projection $S^{2n+1} \to \mathbb{CP}^n$
> The projection $S^{2n+1} \to \mathbb{CP}^n$ of [[§9 Complex Projective Space|§9]] is a submersion.
>
> *Lee: Problem 4-5(a)*

^ex-46-2

*Uses:* [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Ex. §46.3]], [[§40 Fibrations#^prop-40-1|§40.1]]

> [!remark]- Connections
> - Proved below, as a consequence of the local triviality of the Hopf fibration: [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Ex. §46.3]] with [[§40 Fibrations#^prop-40-1|§40.1]](2).

Stated in lecture as an example (“the projection you worked with from a sphere to complex projective space”); not proved in that lecture; the proof follows [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Example §46.3]] below. The dimensions are consistent, $2n \le 2n+1$. A proof needs the differential of a map *out of* a level set in terms of the ambient Jacobian, which Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]] makes available for smoothness but not yet for differentials.

> [!example] Example §46.3: The Hopf Fibration $S^{2n+1} \to \mathbb{CP}^n$
> The projection $\pi : S^{2n+1} \to \mathbb{CP}^n$, $\pi(z) = [z]$, is a fibration with fibre $S^1$. Over the chart domain $U_j = \{z_j \ne 0\}$ a local trivialization is
>
> $$
> \phi_j : \pi^{-1}(U_j) \to U_j \times S^1, \qquad \phi_j(z) = \Big(\, [z],\ \frac{z_j}{|z_j|} \,\Big),
> $$
>
> with inverse $([w], \lambda) \mapsto \lambda\, \hat w / |\hat w|$, where $\hat w$ is the representative of $[w]$ with $\hat w_j = 1$.
>
> *Lee: Problem 4-5(a) and the Hopf map of Ch. 21*

^ex-46-3

> [!proof]+ Proof
> *(Claimed in lecture — a student supplied the fibre, $S^1$; the trivialization is filled in.)* By Definition [[§40 Fibrations#^def-40-1|§40.1]] we must show: $\pi$ is smooth; the sets $U_j$ form an open cover of $\mathbb{CP}^n$; and each $\phi_j$ is a diffeomorphism $\pi^{-1}(U_j) \to U_j \times S^1$ with $\mathrm{pr}_1 \circ \phi_j = \pi|_{\pi^{-1}(U_j)}$. Throughout, $S^{2n+1} = \{|z|^2 = 1\} \subseteq \mathbb{C}^{n+1} \cong \mathbb{R}^{2n+2}$ and $S^1 = \{|\lambda|^2 = 1\} \subseteq \mathbb{C} \cong \mathbb{R}^2$ carry their level-set structures (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]), so Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]] applies to maps out of and into them.
>
> *The cover.* The sets $U_j$ cover $\mathbb{CP}^n$: every $z \in S^{2n+1}$ is nonzero, so some $z_j \neq 0$ and $[z] \in U_j$. Each $U_j$ is open (Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]]). Whether $z_j \neq 0$ does not depend on the representative, since $(\xi z)_j = \xi z_j$ with $\xi \neq 0$; hence $\pi^{-1}(U_j) = S^{2n+1} \cap \{z_j \ne 0\}$, the intersection of $S^{2n+1}$ with an open subset of $\mathbb{C}^{n+1}$, which is open.
>
> *$\phi_j$ is smooth.* A map into the product manifold $U_j \times S^1$ is smooth when its two components are, because in a product chart (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]) its coordinate representation is the pair of the coordinate representations of the components. The first component of $\phi_j$ is $z \mapsto [z]$. In the chart $\varphi_j$ of Definition [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|§18.2]] it reads
>
> $$
> \varphi_j \circ \pi(z) = \varphi_j([z]) = (z_k/z_j)_{k \ne j},
> $$
>
> the restriction to $\pi^{-1}(U_j)$ of a map that is smooth on the open set $\{z_j \ne 0\} \subseteq \mathbb{C}^{n+1}$ (in real coordinates each entry is a rational function whose denominator $|z_j|^2$ does not vanish there). By Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](1) it is smooth, and so is $\pi|_{\pi^{-1}(U_j)} = \varphi_j^{-1} \circ (\varphi_j \circ \pi)$, because the chart inverse $\varphi_j^{-1}$ is smooth (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). The second component is $z \mapsto z_j/|z_j|$, again the restriction of a map smooth on $\{z_j \ne 0\}$, where $|z_j| > 0$; so it is smooth into $\mathbb{C}$ by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](1). Its values have modulus $1$, so it is smooth into $S^1$ by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2).
>
> *$\pi$ is smooth.* By the previous step $\pi$ is smooth on each of the open sets $\pi^{-1}(U_j)$, and these cover $S^{2n+1}$ because the $U_j$ cover $\mathbb{CP}^n$. Smoothness is checked near each point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), so $\pi$ is smooth.
>
> *The proposed inverse is smooth.* Let $\psi_j : U_j \times S^1 \to \pi^{-1}(U_j)$, $\psi_j([w], \lambda) = \lambda\,\hat w/|\hat w|$. For $u \in \mathbb{C}^n$ let $\hat w(u) \in \mathbb{C}^{n+1}$ be the vector $u$ with the entry $1$ inserted in slot $j$. By Proposition [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]], $\varphi_j^{-1}(u) = [\hat w(u)]$, so the representative of $[w]$ with $j$-th entry $1$ is $\hat w(\varphi_j([w]))$, and
>
> $$
> \psi_j([w], \lambda) = \lambda\, \frac{\hat w(u)}{|\hat w(u)|}, \qquad u = \varphi_j([w]) .
> $$
>
> In the chart this is $(u, \lambda) \mapsto \lambda \hat w(u)/|\hat w(u)|$. Each entry is the product of two smooth functions on $U_j \times S^1$: the function $([w], \lambda) \mapsto \lambda$, which is the projection $\mathrm{pr}_2$ (smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]) followed by the inclusion $S^1 \to \mathbb{C}$ (smooth by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](1), restricting the identity of $\mathbb{C}$); and the function $([w], \lambda) \mapsto \hat w(u)_k/|\hat w(u)|$, which is $\mathrm{pr}_1$, then the chart $\varphi_j$, then a map smooth on all of $\mathbb{C}^n$, since $|\hat w(u)| \ge 1$. So $\psi_j$ is smooth into $\mathbb{C}^{n+1}$, a smooth map into $\mathbb{C}^{n+1} \setminus \{0\}$. Its values have modulus $|\lambda| \cdot 1 = 1$ and $j$-th entry $\lambda/|\hat w(u)| \neq 0$, so they land in $\pi^{-1}(U_j) \subseteq S^{2n+1}$; by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2) $\psi_j$ is smooth into $S^{2n+1}$, hence into its open subset $\pi^{-1}(U_j)$.
>
> *They are mutually inverse.* Let $z \in S^{2n+1}$ with $z_j \ne 0$, and $([w], \lambda) = \phi_j(z) = ([z], z_j/|z_j|)$. The representative of $[z]$ with $j$-th entry $1$ is $\hat w = z/z_j$, with $|\hat w| = |z|/|z_j|$. Hence
>
> $$
> \psi_j(\phi_j(z)) = \lambda\, \frac{\hat w}{|\hat w|} = \frac{z_j}{|z_j|} \cdot \frac{z}{z_j} \cdot \frac{|z_j|}{|z|} = \frac{z}{|z|} = z ,
> $$
>
> the last step because $|z| = 1$. Conversely let $([w], \lambda) \in U_j \times S^1$ and $z = \psi_j([w], \lambda) = \lambda \hat w/|\hat w|$. Then $z$ is the nonzero multiple $\lambda/|\hat w|$ of $\hat w$, so it lies on the same complex line and $[z] = [\hat w] = [w]$; and its $j$-th entry is $z_j = \lambda/|\hat w|$, so $z_j/|z_j| = \lambda/|\lambda| = \lambda$. Hence $\phi_j(\psi_j([w], \lambda)) = ([w], \lambda)$.
>
> *Conclusion.* So $\phi_j$ is a smooth bijection with smooth inverse $\psi_j$, a diffeomorphism. Finally $\mathrm{pr}_1 \circ \phi_j(z) = [z] = \pi(z)$, by the definition of $\phi_j$. So each $\phi_j$ is a local trivialization, and $\pi$ is a fibration with fibre $S^1$.

^pf-ex-46-3

*Uses:* [[§40 Fibrations#^def-40-1|Def. §40.1]], [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§18 Projective Spaces as Smooth Manifolds#^prop-18-1|§18.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]

![[m591-16-7.svg]]
*The fibres of the Hopf fibration for $n = 1$, $S^3 \to \mathbb{CP}^1$, made visible in $\mathbb{R}^3$ by stereographic projection of $S^3$ from the point $(0, 1)$. Blue: the fibre through $(1, 0)$, which projects to the unit circle, and the fibre through $(0, 1)$ itself, which projects to the vertical axis closed up at infinity. Red: two more fibres, through points with $|z_1| = |z_2|$. Each fibre is a circle $\{\lambda z : |\lambda| = 1\}$, no two meet, and any two are linked: over each $U_j$ the circles sit side by side as in $U_j \times S^1$, but globally they are woven together.*

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space $S^{2n+1}/\mathrm{U}(1)$: [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]]. The Hopf fibration has no section: [[§46 Projective Spaces and the Hopf Fibration#^rem-46-1|Remark: Sections Need Not Exist]].

With [[§40 Fibrations#^prop-40-1|Proposition §40.1]](2), this also proves [[§46 Projective Spaces and the Hopf Fibration#^ex-46-2|Example §46.2]], which Lecture 10 stated without proof: the projection $S^{2n+1} \to \mathbb{CP}^n$ is a submersion. Its fibres are the circles $\{\lambda z : |\lambda| = 1\}$.

> [!remark] Remark: Sections Need Not Exist
> “A fact”: the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ of [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Example §46.3]] — “the fibration that you're working with in homework” — has no continuous section, for $n \ge 1$. (For $n = 0$ the base is a single point.) This is stated, not proved, here; a proof uses the fundamental group. A vector bundle, by contrast, always has sections — the zero section at least — and in fact “a very infinite-dimensional space” of them.

^rem-46-1

For the Hopf fibration the converse of [[§40 Fibrations#^prop-40-4|Proposition §40.4]] holds: the circle acting on the fibres turns any local section into a local trivialization.

> [!theorem] Proposition §46.1: Local Sections of the Hopf Fibration Give Trivializations
> Let $\pi : S^{2n+1} \to \mathbb{CP}^n$ be the Hopf fibration ([[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Ex. §46.3]]), on which $S^1$ acts ([[§13 Group Actions and Orbit Spaces#^def-13-1|Def. §13.1]]) by $\lambda \cdot z = \lambda z$, and let $s : U \to \pi^{-1}(U)$ be a local section ([[§40 Fibrations#^def-40-4|Def. §40.4]]). Then
>
> $$
> \Psi_s : U \times S^1 \longrightarrow \pi^{-1}(U), \qquad \Psi_s(u, \lambda) = \lambda\, s(u),
> $$
>
> is a diffeomorphism ([[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]) with $\pi \circ \Psi_s = \mathrm{pr}_1$ and $\Psi_s(u, 1) = s(u)$, equivariant for the actions $\lambda \cdot (u, \mu) = (u, \lambda\mu)$ and $\lambda \cdot z = \lambda z$. Its inverse is
>
> $$
> \Psi_s^{-1}(z) = \Big( \pi(z),\ \big\langle z, s(\pi(z)) \big\rangle \Big), \qquad \langle z, w \rangle = \textstyle\sum_k z_k \bar w_k .
> $$

^prop-46-1

> [!proof]+ Proof
> *(Assignment 4, Problem 4 did this for the explicit sections $s_i$ of the corollary below; the inner-product formula for the inverse, which works for every local section, is filled in.)* We show in turn: $\Psi_s$ takes values in $\pi^{-1}(U)$, with $\pi \circ \Psi_s = \mathrm{pr}_1$ and $\Psi_s(u, 1) = s(u)$; it is equivariant; it and the proposed inverse are smooth; and the two are mutually inverse. Here $s$ is a local section: a smooth map $U \to S^{2n+1}$ with $\pi \circ s = \mathrm{id}_U$ (Definition [[§40 Fibrations#^def-40-4|§40.4]]), so $|s(u)| = 1$ and $[s(u)] = u$. Two facts are used repeatedly. First, by Definition [[§9 Complex Projective Space#^def-9-1|§9.1]], two points $z, w \in S^{2n+1}$ have $\pi(z) = \pi(w)$ iff $w = \xi z$ for some $\xi \in S^1$. Second, $\langle z, w \rangle = \sum_k z_k \bar w_k$ is complex-linear in $z$ and conjugate-linear in $w$, and $\langle z, z \rangle = |z|^2$.
>
> *Values, $\pi \circ \Psi_s = \mathrm{pr}_1$, and $\Psi_s(u,1) = s(u)$.* For $(u, \lambda) \in U \times S^1$, $|\lambda s(u)| = |\lambda|\,|s(u)| = 1$, so $\lambda s(u) \in S^{2n+1}$; and $\lambda s(u)$ is obtained from $s(u)$ by the element $\lambda$ of $S^1$, so by the first fact
>
> $$
> \pi(\Psi_s(u, \lambda)) = \pi(\lambda s(u)) = \pi(s(u)) = u .
> $$
>
> So $\Psi_s$ lands in $\pi^{-1}(U)$, and $\pi \circ \Psi_s = \mathrm{pr}_1$. Also $\Psi_s(u, 1) = 1 \cdot s(u) = s(u)$.
>
> *Equivariance.* For $\mu \in S^1$, by the definitions of the two actions and associativity of multiplication in $\mathbb{C}$,
>
> $$
> \Psi_s\big(\mu \cdot (u, \lambda)\big) = \Psi_s(u, \mu\lambda) = (\mu\lambda)\, s(u) = \mu\,\big(\lambda s(u)\big) = \mu \cdot \Psi_s(u, \lambda) .
> $$
>
> *$\Psi_s$ is smooth.* The $k$-th entry of $\Psi_s(u, \lambda)$ is $\lambda\, s(u)_k$, the product of the smooth functions $(u, \lambda) \mapsto \lambda$ (the projection $\mathrm{pr}_2$, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], followed by the inclusion $S^1 \to \mathbb{C}$) and $(u, \lambda) \mapsto s(u)_k$ (the projection $\mathrm{pr}_1$, then $s$, then the inclusion $S^{2n+1} \to \mathbb{C}^{n+1}$, then the $k$-th coordinate). So $\Psi_s$ is smooth into $\mathbb{C}^{n+1}$; it lands in $S^{2n+1}$, so it is smooth into $S^{2n+1}$ (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2)), hence into the open subset $\pi^{-1}(U)$.
>
> *The proposed inverse is smooth.* Let $\Theta(z) = \big(\pi(z), \langle z, s(\pi(z)) \rangle\big)$ for $z \in \pi^{-1}(U)$. Its first component is $\pi$, smooth by Example [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|§46.3]], with values in $U$. Its second component is the composite of $z \mapsto \big(z, s(\pi(z))\big)$, smooth into $\mathbb{C}^{n+1} \times \mathbb{C}^{n+1}$, with the map $\langle \cdot, \cdot \rangle$, whose real and imaginary parts are polynomials in the real coordinates; so it is smooth into $\mathbb{C}$. Its values have modulus $1$: since $\pi(s(\pi(z))) = \pi(z)$, the first fact gives $s(\pi(z)) = \xi z$ for some $\xi \in S^1$, and then
>
> $$
> \langle z, s(\pi(z)) \rangle = \langle z, \xi z \rangle = \bar\xi\, \langle z, z \rangle = \bar\xi\, |z|^2 = \bar\xi , \qquad |\bar\xi| = 1 . \tag{$\ast$}
> $$
>
> So the second component is smooth into $S^1$ (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2)), and $\Theta$, whose components are smooth, is smooth into the product manifold $U \times S^1$ (in a product chart its coordinate representation is the pair of those of its components, Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]).
>
> *They are mutually inverse.* Let $z \in \pi^{-1}(U)$ and write $s(\pi(z)) = \xi z$ with $\xi \in S^1$ as above; so $z = \bar\xi\, s(\pi(z))$, since $\bar\xi \xi = |\xi|^2 = 1$. In words: $z$ and the unit vector $s(\pi(z))$ span the same complex line, so $z = \lambda s(\pi(z))$ with $\lambda = \bar\xi$; and by $(\ast)$, $\lambda = \lambda \langle s, s \rangle = \langle z, s(\pi(z)) \rangle$. Hence
>
> $$
> \Psi_s(\Theta(z)) = \Psi_s\big(\pi(z), \bar\xi\big) = \bar\xi\, s(\pi(z)) = \bar\xi \xi\, z = z .
> $$
>
> Conversely, for $(u, \lambda) \in U \times S^1$, using $\pi(\lambda s(u)) = u$ (first step), linearity of $\langle \cdot, \cdot \rangle$ in its first slot, and $\langle s(u), s(u) \rangle = |s(u)|^2 = 1$,
>
> $$
> \Theta(\Psi_s(u, \lambda)) = \Big( \pi(\lambda s(u)),\ \big\langle \lambda s(u), s\big(\pi(\lambda s(u))\big) \big\rangle \Big) = \big(u,\ \lambda \langle s(u), s(u) \rangle\big) = (u, \lambda) .
> $$
>
> So $\Psi_s$ is a smooth bijection with smooth inverse $\Theta = \Psi_s^{-1}$, a diffeomorphism.

^pf-46-1

*Uses:* [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Ex. §46.3]], [[§40 Fibrations#^def-40-4|Def. §40.4]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]

> [!remark]- Connections
> - The discrete-fibre analogue: the sheets over an evenly covered set, [[§31 Covering Spaces#^def-31-1|590 Def. §31.1]], each a local section of the covering map, [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]].
> - $\mathbb{CP}^n$ as the orbit space of this circle action: [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]].

![[m591-31-1.svg]]
*Sections and trivializations. (a) A fibration $\pi : E \to B$ ([[§40 Fibrations#^def-40-1|Definition §40.1]]), drawn schematically with its fibres as grey curves; over the open set $U \subseteq B$ the shaded piece $\pi^{-1}(U)$, bounded by the dashed fibres over the ends of $U$, is carried by the local trivialization $\phi$ onto the box $U \times F$, where $\mathrm{pr}_1$ projects to $U$ and the vertical direction is the model fibre $F$. Fixing $f_0 \in F$ gives the red slice $U \times \{f_0\}$, which meets each vertical fibre $\{u\} \times F$ exactly once; its preimage under $\phi$ is the red curve $s(U)$, and $s(u) = \phi^{-1}(u, f_0)$ is the local section of [[§40 Fibrations#^prop-40-4|Proposition §40.4]] ([[§40 Fibrations#^def-40-4|Definition §40.4]]): it picks one point on the fibre over each $u$, which is $\pi \circ s = \mathrm{id}_U$. (b) The converse for the Hopf fibration, [[§46 Projective Spaces and the Hopf Fibration#^prop-46-1|Proposition §46.1]]. On the right, over $U \subseteq \mathbb{CP}^n$, each fibre of $\pi^{-1}(U) \subseteq S^{2n+1}$ is a circle (back halves dotted), and a local section picks the red point $s(u)$ on each, tracing the red curve $s(U)$. Multiplying by $\lambda = e^{i\theta}$ moves $s(u)$ along its own circle to the green point $\lambda\, s(u)$, and as $\theta$ runs from $0$ to $2\pi$ it sweeps out the whole circle exactly once. On the left the same motion in the product $U \times S^1$: the red line $U \times \{1\}$ and the green point $(u, \lambda)$ on the circle $\{u\} \times S^1$. The trivialization $\Psi_s(u, \lambda) = \lambda\, s(u)$ (orange) matches the two pictures, sending $U \times \{1\}$ to $s(U)$ and commuting with $\mathrm{pr}_1$ and $\pi$; for the sections $s_i$ of [[§46 Projective Spaces and the Hopf Fibration#^cor-46-2|Corollary §46.2]] its inverse is the trivialization of [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Example §46.3]]. The circles are drawn side by side as in $U \times S^1$; in $S^3$ they are linked, as in the stereographic picture after Example §38.3. (Drawn for these notes in the vault; not in the course tex.)*

> [!theorem] Corollary §46.2: Local but Not Global Sections of the Hopf Fibration
> Over each chart domain $U_i = \{[z] : z_i \neq 0\}$ of $\mathbb{CP}^n$ ([[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]]), the Hopf fibration has the local section ([[§40 Fibrations#^def-40-4|Def. §40.4]])
>
> $$
> s_i([z]) = \frac{\hat z}{|\hat z|}, \qquad \hat z = \frac{z}{z_i} ,
> $$
>
> and the trivialization $\Psi_{s_i}^{-1}$ it gives is the one of Example [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|§46.3]], $z \mapsto ([z], z_i/|z_i|)$. For $n \ge 1$ there is no global section ([[§40 Fibrations#^def-40-3|Def. §40.3]]).

^cor-46-2

> [!proof]+ Proof
> *(Assignment 4, Problem 4; the global statement is the fact of the remark *Sections Need Not Exist* in [[§46 Projective Spaces and the Hopf Fibration|§46]] above, stated there without proof.)* Four things are claimed: $s_i$ is well defined; it is a local section over $U_i$ (Definition [[§40 Fibrations#^def-40-4|§40.4]]: smooth, with values in $S^{2n+1}$, and $\pi \circ s_i = \mathrm{id}_{U_i}$); $\Psi_{s_i}^{-1}$ is the trivialization of Example [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|§46.3]]; and there is no global section for $n \ge 1$.
>
> *Well defined.* $\hat z$ is independent of the representative $z$: if $z' = \mu z$ with $\mu \neq 0$, then $z'/z'_i = \mu z/(\mu z_i) = z/z_i$.
>
> *Smooth, with values in $S^{2n+1}$.* For $u \in \mathbb{C}^n$ let $\hat w(u)$ be $u$ with the entry $1$ inserted in slot $i$. The vector $\hat z = z/z_i$ has $i$-th entry $1$ and remaining entries $(z_k/z_i)_{k \neq i} = \varphi_i([z])$, so $\hat z = \hat w(\varphi_i([z]))$: it is $\varphi_i([z])$ with a $1$ inserted in slot $i$. Hence
>
> $$
> s_i = g \circ \varphi_i, \qquad g(u) = \frac{\hat w(u)}{|\hat w(u)|} .
> $$
>
> The map $g : \mathbb{C}^n \to \mathbb{C}^{n+1}$ is smooth, since $\hat w(u)$ is nonzero, indeed $|\hat w(u)| \ge 1$; and $\varphi_i$ is smooth (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]). So $s_i$ is smooth into $\mathbb{C}^{n+1}$. Its values have norm $1$, so $s_i$ lands in $S^{2n+1}$ and is smooth into it (Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2)).
>
> *$\pi \circ s_i = \mathrm{id}$.* Let $[z] \in U_i$ with $|z| = 1$ and $z_i \neq 0$. Then $|\hat z| = |z|/|z_i| = 1/|z_i|$, and
>
> $$
> s_i([z]) = \frac{\hat z}{|\hat z|} = \frac{z}{z_i}\,|z_i| = \frac{|z_i|}{z_i}\, z = \frac{\bar z_i}{|z_i|}\, z ,
> $$
>
> using $\frac{|z_i|}{z_i} = \frac{|z_i|\,\bar z_i}{z_i \bar z_i} = \frac{\bar z_i}{|z_i|}$. The factor $\bar z_i/|z_i|$ lies in $S^1$, so $s_i([z])$ is in the class of $z$ (Definition [[§9 Complex Projective Space#^def-9-1|§9.1]]): it spans the line of $z$, and $\pi(s_i([z])) = [z]$. So $\pi \circ s_i = \mathrm{id}_{U_i}$.
>
> *The trivialization.* By Proposition [[§46 Projective Spaces and the Hopf Fibration#^prop-46-1|§46.1]] with $s = s_i$, $\Psi_{s_i}^{-1}(z) = \big([z], \langle z, s_i([z]) \rangle\big)$ for $z \in \pi^{-1}(U_i)$. For $|z| = 1$ with $z_i \neq 0$, the formula $s_i([z]) = \bar z_i z / |z_i|$ just shown and conjugate-linearity of $\langle \cdot, \cdot \rangle$ in its second slot give
>
> $$
> \langle z, s_i([z]) \rangle = \Big\langle z, \frac{\bar z_i}{|z_i|}\, z \Big\rangle = \frac{z_i}{|z_i|}\, \langle z, z \rangle = \frac{z_i}{|z_i|}\, |z|^2 = \frac{z_i}{|z_i|} .
> $$
>
> So $\Psi_{s_i}^{-1}(z) = ([z], z_i/|z_i|)$, which is $\phi_i$ of Example [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|§46.3]].
>
> *No global section.* A global section $s$ is a local section over $U = \mathbb{CP}^n$, and then Proposition [[§46 Projective Spaces and the Hopf Fibration#^prop-46-1|§46.1]] makes $\Psi_s : \mathbb{CP}^n \times S^1 \to \pi^{-1}(\mathbb{CP}^n) = S^{2n+1}$ a diffeomorphism: $\pi$ would be globally trivial, $S^{2n+1} \cong \mathbb{CP}^n \times S^1$. That this is impossible for $n \ge 1$ is the fact of the remark *Sections Need Not Exist* in [[§46 Projective Spaces and the Hopf Fibration|§46]], which states directly that $\pi$ has no continuous section, and a smooth section is in particular continuous.

^pf-46-2

*Uses:* [[§40 Fibrations#^def-40-4|Def. §40.4]], [[§46 Projective Spaces and the Hopf Fibration#^ex-46-3|Ex. §46.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§46 Projective Spaces and the Hopf Fibration#^prop-46-1|§46.1]]
