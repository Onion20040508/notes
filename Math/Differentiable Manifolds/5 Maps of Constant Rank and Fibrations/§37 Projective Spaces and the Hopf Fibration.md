---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 37
tags: [differentiable-manifolds, math591]
---
← [[§36 Embeddings]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§38 SU(2) → SO(3)꞉ The Double Cover]] →

*Stage: bundles — The maps of this chapter on projective spaces: $S^n \to \mathbb{RP}^n$ is a two-to-one local diffeomorphism, and $S^{2n+1} \to \mathbb{CP}^n$ is a submersion and a fibration, the Hopf fibration, with local sections but no global one.*

The projections $S^n \to \mathbb{RP}^n$ and $S^{2n+1} \to \mathbb{CP}^n$ through the course: the second is the quotient map that defines $\mathbb{CP}^n$ in [[§9 Complex Projective Space|Complex Projective Space]], an orbit map in [[§12 Group Actions and Orbit Spaces#^ex-12-3|projective space as an orbit space]]; the first is the quotient map of [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|The Two Topologies on RPⁿ Agree]], and both are read in the standard atlases of [[§17 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; *this section* shows the first is a two-to-one local diffeomorphism and the second a submersion and a fibration, the Hopf fibration, with local but no global sections; and for $n = 3$ the first returns as $S^3 = \mathrm{SU}(2) \to \mathrm{SO}(3) \cong \mathbb{RP}^3$ in [[§38 SU(2) → SO(3)꞉ The Double Cover#^thm-38-10|The Double Cover]].

> [!example] Example §37.1: Spheres Cover Projective Spaces
> The projection $\pi : S^n \to \mathbb{RP}^n$, $x \mapsto [x]$, is a local diffeomorphism, exactly two-to-one.

^ex-37-1

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* Use coordinates $x_0, \ldots, x_n$ on $\mathbb{R}^{n+1}$, matching the charts $(U_i, \varphi_i)$ of Corollary [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|§17.5]], and give $S^n = \{|x|^2 = 1\}$ its level-set structure. For each $i$ and $\varepsilon = \pm 1$, the open hemisphere $U_i^\varepsilon = \{x \in S^n \mid \varepsilon x_i > 0\}$ is mapped by $\pi$ bijectively onto $U_i = \{[x] \mid x_i \neq 0\}$, since a line not contained in $\{x_i = 0\}$ meets $U_i^\varepsilon$ exactly once. In the chart $\varphi_i$,
>
> $$
> \varphi_i \circ \pi(x) = (x_k/x_i)_{k \neq i},
> $$
>
> the restriction of a smooth map on the open set $\{x_i \neq 0\} \subseteq \mathbb{R}^{n+1}$, hence smooth by Lemma [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]](1). Its inverse is $y \mapsto \varepsilon\,\hat y/|\hat y|$, where $\hat y$ is $y$ with a $1$ inserted in slot $i$. This is smooth into $\mathbb{R}^{n+1}$ with values in $U_i^\varepsilon$, hence smooth into $S^n$ by Lemma [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]](2). So $\varphi_i \circ \pi$ is a diffeomorphism of $U_i^\varepsilon$ onto $\mathbb{R}^n$, and $\pi|_{U_i^\varepsilon} = \varphi_i^{-1} \circ (\varphi_i \circ \pi)$ is a diffeomorphism onto $U_i$ by Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]. The hemispheres cover $S^n$, and $\pi(x) = \pi(-x)$.

^pf-ex-37-1

*Uses:* [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]], [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|§17.5]], [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]], [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]

> [!remark]- Connections
> - As a covering map of topological spaces, for $n = 2$: [[§28 Fundamental Group of Some Surfaces#^thm-28-1|590 §28.1]] ($S^2 \to P^2$ is a covering map).

> [!example] Example §37.2: The Projection $S^{2n+1} \to \mathbb{CP}^n$
> The projection $S^{2n+1} \to \mathbb{CP}^n$ of [[§9 Complex Projective Space|§9]] is a submersion.
>
> *Lee: Problem 4-5(a)*

^ex-37-2

*Uses:* [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Ex. §37.3]], [[§34 Fibrations#^prop-34-1|§34.1]]

> [!remark]- Connections
> - Proved below, as a consequence of the local triviality of the Hopf fibration: [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Ex. §37.3]] with [[§34 Fibrations#^prop-34-1|§34.1]](2).

Stated in lecture as an example (“the projection you worked with from a sphere to complex projective space”); not proved in that lecture; the proof follows [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Example §37.3]] below. The dimensions are consistent, $2n \le 2n+1$. A proof needs the differential of a map *out of* a level set in terms of the ambient Jacobian, which Lemma [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]] makes available for smoothness but not yet for differentials.

> [!example] Example §37.3: The Hopf Fibration $S^{2n+1} \to \mathbb{CP}^n$
> The projection $\pi : S^{2n+1} \to \mathbb{CP}^n$, $\pi(z) = [z]$, is a fibration with fibre $S^1$. Over the chart domain $U_j = \{z_j \ne 0\}$ a local trivialization is
>
> $$
> \phi_j : \pi^{-1}(U_j) \to U_j \times S^1, \qquad \phi_j(z) = \Big(\, [z],\ \frac{z_j}{|z_j|} \,\Big),
> $$
>
> with inverse $([w], \lambda) \mapsto \lambda\, \hat w / |\hat w|$, where $\hat w$ is the representative of $[w]$ with $\hat w_j = 1$.
>
> *Lee: Problem 4-5(a) and the Hopf map of Ch. 21*

^ex-37-3

> [!proof]+ Proof
> *(Claimed in lecture — a student supplied the fibre, $S^1$; the trivialization is filled in.)* The sets $U_j$ cover $\mathbb{CP}^n$, and $\pi^{-1}(U_j) = S^{2n+1} \cap \{z_j \ne 0\}$ is open. $\phi_j$ is smooth: in the chart $\varphi_j$ of [[§17 Projective Spaces as Smooth Manifolds#^def-17-2|Definition §17.2]] its first component is $z \mapsto (z_k/z_j)_{k \ne j}$, and its second is $z \mapsto z_j/|z_j|$, both smooth on $\{z_j \ne 0\}$, with the second taking values in $S^1$ ([[§19 Manifolds in Euclidean Space#^lem-19-3|Lemma §19.3]]). The proposed inverse is smooth, since in the chart it is $(u, \lambda) \mapsto \lambda \hat w(u)/|\hat w(u)|$ with $\hat w(u)$ the vector $u$ with the entry $1$ inserted in slot $j$, a smooth map into $\mathbb{C}^{n+1} \setminus \{0\}$ landing in $S^{2n+1}$ ([[§19 Manifolds in Euclidean Space#^lem-19-3|Lemma §19.3]]). They are mutually inverse: for $z \in S^{2n+1}$ with $z_j \ne 0$, $\hat w = z/z_j$ and $\lambda = z_j/|z_j|$ give $\lambda \hat w/|\hat w| = z/|z| = z$; conversely $z = \lambda \hat w/|\hat w|$ has $[z] = [\hat w]$ and $z_j/|z_j| = \lambda$. Finally $\mathrm{pr}_1 \circ \phi_j = \pi$ by definition. So each $\phi_j$ is a local trivialization.

^pf-ex-37-3

*Uses:* [[§34 Fibrations#^def-34-1|Def. §34.1]], [[§17 Projective Spaces as Smooth Manifolds#^def-17-2|Def. §17.2]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]]

![[m591-16-7.svg]]
*The fibres of the Hopf fibration for $n = 1$, $S^3 \to \mathbb{CP}^1$, made visible in $\mathbb{R}^3$ by stereographic projection of $S^3$ from the point $(0, 1)$. Blue: the fibre through $(1, 0)$, which projects to the unit circle, and the fibre through $(0, 1)$ itself, which projects to the vertical axis closed up at infinity. Red: two more fibres, through points with $|z_1| = |z_2|$. Each fibre is a circle $\{\lambda z : |\lambda| = 1\}$, no two meet, and any two are linked: over each $U_j$ the circles sit side by side as in $U_j \times S^1$, but globally they are woven together.*

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space $S^{2n+1}/\mathrm{U}(1)$: [[§12 Group Actions and Orbit Spaces#^ex-12-3|Ex. §12.3]]. The Hopf fibration has no section: [[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Remark: Sections Need Not Exist]].

With [[§34 Fibrations#^prop-34-1|Proposition §34.1]](2), this also proves [[§37 Projective Spaces and the Hopf Fibration#^ex-37-2|Example §37.2]], which Lecture 10 stated without proof: the projection $S^{2n+1} \to \mathbb{CP}^n$ is a submersion. Its fibres are the circles $\{\lambda z : |\lambda| = 1\}$.

> [!remark] Remark: Sections Need Not Exist
> “A fact”: the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ of [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Example §37.3]] — “the fibration that you're working with in homework” — has no continuous section, for $n \ge 1$. (For $n = 0$ the base is a single point.) This is stated, not proved, here; a proof uses the fundamental group. A vector bundle, by contrast, always has sections — the zero section at least — and in fact “a very infinite-dimensional space” of them.

^rem-37-1

For the Hopf fibration the converse of [[§34 Fibrations#^prop-34-4|Proposition §34.4]] holds: the circle acting on the fibres turns any local section into a local trivialization.

> [!theorem] Proposition §37.1: Local Sections of the Hopf Fibration Give Trivializations
> Let $\pi : S^{2n+1} \to \mathbb{CP}^n$ be the Hopf fibration ([[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Ex. §37.3]]), on which $S^1$ acts ([[§12 Group Actions and Orbit Spaces#^def-12-1|Def. §12.1]]) by $\lambda \cdot z = \lambda z$, and let $s : U \to \pi^{-1}(U)$ be a local section ([[§34 Fibrations#^def-34-3|Def. §34.3]]). Then
>
> $$
> \Psi_s : U \times S^1 \longrightarrow \pi^{-1}(U), \qquad \Psi_s(u, \lambda) = \lambda\, s(u),
> $$
>
> is a diffeomorphism ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]) with $\pi \circ \Psi_s = \mathrm{pr}_1$ and $\Psi_s(u, 1) = s(u)$, equivariant for the actions $\lambda \cdot (u, \mu) = (u, \lambda\mu)$ and $\lambda \cdot z = \lambda z$. Its inverse is
>
> $$
> \Psi_s^{-1}(z) = \Big( \pi(z),\ \big\langle z, s(\pi(z)) \big\rangle \Big), \qquad \langle z, w \rangle = \textstyle\sum_k z_k \bar w_k .
> $$

^prop-37-1

> [!proof]+ Proof
> *(Assignment 4, Problem 4 did this for the explicit sections $s_i$ of [[§37 Projective Spaces and the Hopf Fibration#^cor-37-2|the corollary below]]; the inner-product formula for the inverse, which works for every local section, is filled in.)* $\Psi_s$ lands in $\pi^{-1}(U)$: $|\lambda s(u)| = 1$, and $\lambda s(u)$ spans the same complex line as $s(u)$, so $\pi(\lambda s(u)) = \pi(s(u)) = u$. This also gives $\pi \circ \Psi_s = \mathrm{pr}_1$, and equivariance is $\mu\,(\lambda s(u)) = (\mu\lambda)\, s(u)$. Both maps are smooth: $\Psi_s$ is a product of smooth maps into $\mathbb{C}^{n+1}$ landing in $S^{2n+1}$ (Lemma [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]]), and the proposed inverse is built from $\pi$, $s$ and the polynomial $\langle \cdot, \cdot \rangle$, with second component of modulus $1$. They are mutually inverse. If $z \in \pi^{-1}(U)$, then $z$ and the unit vector $s(\pi(z))$ span the same complex line, so $z = \lambda s(\pi(z))$ for some $\lambda$, and $\lambda = \lambda \langle s, s \rangle = \langle z, s(\pi(z)) \rangle$; hence $\Psi_s(\Psi_s^{-1}(z)) = z$. Conversely $\Psi_s^{-1}(\lambda s(u)) = (u, \lambda \langle s(u), s(u) \rangle) = (u, \lambda)$.

^pf-37-1

*Uses:* [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Ex. §37.3]], [[§34 Fibrations#^def-34-3|Def. §34.3]], [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]], [[§18 Smooth Functions and Smooth Maps#^prop-18-9|§18.9]], [[§18 Smooth Functions and Smooth Maps#^lem-18-4|§18.4]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]

> [!remark]- Connections
> - The discrete-fibre analogue: the sheets over an evenly covered set, [[§24 Covering Spaces#^def-24-1|590 Def. §24.1]], each a local section of the covering map, [[§24 Covering Spaces#^def-24-2|590 Def. §24.2]].
> - $\mathbb{CP}^n$ as the orbit space of this circle action: [[§12 Group Actions and Orbit Spaces#^ex-12-3|Ex. §12.3]].

![[m591-31-1.svg]]
*Sections and trivializations. (a) A fibration $\pi : E \to B$ ([[§34 Fibrations#^def-34-1|Definition §34.1]]), drawn schematically with its fibres as grey curves; over the open set $U \subseteq B$ the shaded piece $\pi^{-1}(U)$, bounded by the dashed fibres over the ends of $U$, is carried by the local trivialization $\phi$ onto the box $U \times F$, where $\mathrm{pr}_1$ projects to $U$ and the vertical direction is the model fibre $F$. Fixing $f_0 \in F$ gives the red slice $U \times \{f_0\}$, which meets each vertical fibre $\{u\} \times F$ exactly once; its preimage under $\phi$ is the red curve $s(U)$, and $s(u) = \phi^{-1}(u, f_0)$ is the local section of [[§34 Fibrations#^prop-34-4|Proposition §34.4]] ([[§34 Fibrations#^def-34-3|Definition §34.3]]): it picks one point on the fibre over each $u$, which is $\pi \circ s = \mathrm{id}_U$. (b) The converse for the Hopf fibration, [[§37 Projective Spaces and the Hopf Fibration#^prop-37-1|Proposition §37.1]]. On the right, over $U \subseteq \mathbb{CP}^n$, each fibre of $\pi^{-1}(U) \subseteq S^{2n+1}$ is a circle (back halves dotted), and a local section picks the red point $s(u)$ on each, tracing the red curve $s(U)$. Multiplying by $\lambda = e^{i\theta}$ moves $s(u)$ along its own circle to the green point $\lambda\, s(u)$, and as $\theta$ runs from $0$ to $2\pi$ it sweeps out the whole circle exactly once. On the left the same motion in the product $U \times S^1$: the red line $U \times \{1\}$ and the green point $(u, \lambda)$ on the circle $\{u\} \times S^1$. The trivialization $\Psi_s(u, \lambda) = \lambda\, s(u)$ (orange) matches the two pictures, sending $U \times \{1\}$ to $s(U)$ and commuting with $\mathrm{pr}_1$ and $\pi$; for the sections $s_i$ of [[§37 Projective Spaces and the Hopf Fibration#^cor-37-2|Corollary §37.2]] its inverse is the trivialization of [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Example §37.3]]. The circles are drawn side by side as in $U \times S^1$; in $S^3$ they are linked, as in the stereographic picture after Example §38.3. (Drawn for these notes in the vault; not in the course tex.)*

> [!theorem] Corollary §37.2: Local but Not Global Sections of the Hopf Fibration
> Over each chart domain $U_i = \{[z] : z_i \neq 0\}$ of $\mathbb{CP}^n$ ([[§17 Projective Spaces as Smooth Manifolds#^def-17-2|Def. §17.2]]), the Hopf fibration has the local section ([[§34 Fibrations#^def-34-3|Def. §34.3]])
>
> $$
> s_i([z]) = \frac{\hat z}{|\hat z|}, \qquad \hat z = \frac{z}{z_i} ,
> $$
>
> and the trivialization $\Psi_{s_i}^{-1}$ it gives is the one of Example [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|§37.3]], $z \mapsto ([z], z_i/|z_i|)$. For $n \ge 1$ there is no global section ([[§34 Fibrations#^def-34-2|Def. §34.2]]).

^cor-37-2

> [!proof]+ Proof
> *(Assignment 4, Problem 4; the global statement is the fact of Remark [[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Sections Need Not Exist]] above, stated there without proof.)* $\hat z$ is independent of the representative $z$, smooth in the chart $\varphi_i$ (it is $\varphi_i([z])$ with a $1$ inserted in slot $i$), and nonzero, so $s_i$ is smooth and lands in $S^{2n+1}$; it spans the line of $z$, so $\pi \circ s_i = \mathrm{id}$. For $|z| = 1$ with $z_i \neq 0$, $s_i([z]) = \bar z_i z / |z_i|$, so $\langle z, s_i([z]) \rangle = z_i \langle z, z \rangle / |z_i| = z_i/|z_i|$. By Proposition [[§37 Projective Spaces and the Hopf Fibration#^prop-37-1|§37.1]] a global section would make $\pi$ globally trivial, $S^{2n+1} \cong \mathbb{CP}^n \times S^1$; that this is impossible for $n \ge 1$ is the fact of Remark [[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Sections Need Not Exist]].

^pf-37-2

*Uses:* [[§17 Projective Spaces as Smooth Manifolds#^def-17-2|Def. §17.2]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]], [[§34 Fibrations#^def-34-3|Def. §34.3]], [[§37 Projective Spaces and the Hopf Fibration#^ex-37-3|Ex. §37.3]], [[§37 Projective Spaces and the Hopf Fibration#^prop-37-1|§37.1]], [[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Remark: Sections Need Not Exist]]

