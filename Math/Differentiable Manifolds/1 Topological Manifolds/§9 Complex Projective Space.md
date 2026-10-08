---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 9
tags: [differentiable-manifolds, math591]
---
← [[§8 Spheres]] · ↑ [[· 1 Topological Manifolds]] · [[§10 The Line with Two Origins]] →

*Thread: quotients — $\mathbb{CP}^n$, the first manifold built as a quotient: the open quotient $S^{2n+1}/S^1$ is Hausdorff, second countable ([[§6 Open Quotients|§6]]) and compact, and it is the space of complex lines. Its charts come in [[§18 Projective Spaces as Smooth Manifolds|§18]].*

Complex projective space through the course: the open quotient $S^{2n+1}/S^1$, Hausdorff, second countable and compact, in *this section*; the circle group $\mathrm{U}(1)$ acting there in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; an orbit space in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; a smooth and complex manifold through its standard atlas in [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; a homogeneous space of $\mathrm{U}(n+1)$ in [[§25 The Geometric Tangent Space#^rem-25-9|Dimension Checks through Homogeneous Spaces]]; the domain of the moment map in [[§30 The Differential in Coordinates#^rem-30-5|Remark: The Strategy]]; and the base of the Hopf fibration in [[§40 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]].

The following was set up in the last four minutes of lecture; the proof of the claim was given verbally, chalk down. **Uribe: “I'll write this again next time”** — so expect a [[§13 Group Actions and Orbit Spaces#^cor-13-4|careful reprise]]; the details below reconstruct the verbal argument.

> [!definition] Definition §9.1: Complex Projective Space $\mathbb{CP}^n$
> Consider the sphere $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$, and identify $\mathbb{R}^{2n+2} \cong \mathbb{C}^{n+1}$ by
>
> $$
> (x, y) \longmapsto x + iy, \qquad x, y \in \mathbb{R}^{n+1}
> $$
>
> (any such identification works). So points of $S^{2n+1}$ are complex vectors $z = (z_1, \dots, z_{n+1}) \in \mathbb{C}^{n+1}$ with $|z| = 1$. Let $S^1 = \{\xi \in \mathbb{C} \mid |\xi| = 1\}$ be the unit circle, and define a relation $\sim$ on $S^{2n+1}$ by
>
> $$
> z \sim w \iff \exists\, \xi \in S^1 \text{ such that } w = \xi z
> $$
>
> (componentwise complex multiplication: all entries of $w$ are obtained by rotating the entries of $z$ through the *same* angle). This is an equivalence relation ($\xi = 1$ gives reflexivity; $\xi^{-1} \in S^1$ gives symmetry; products give transitivity). The quotient
>
> $$
> \mathbb{CP}^n \;:=\; S^{2n+1}/{\sim}
> $$
>
> is the **complex projective space** of complex dimension $n$. Explicitly: a point of $\mathbb{CP}^n$ is a class $[z] = \{\, \xi z \mid \xi \in S^1 \,\}$, a circle inside $S^{2n+1}$; $\pi(z) = [z]$; and $W \subseteq \mathbb{CP}^n$ is open iff the union of the circles belonging to $W$ is open in $S^{2n+1}$. The class $[z]$ is the same as the complex line $\mathbb{C} z \subseteq \mathbb{C}^{n+1}$ through $z$ (a line meets the unit sphere in exactly the circle $\{\xi z\}$), so $\mathbb{CP}^n$ is the space of complex lines through the origin in $\mathbb{C}^{n+1}$; the identification is $[z] \mapsto \mathbb{C} z$, with inverse $\ell \mapsto \ell \cap S^{2n+1}$.
>
> *Lee: Problem 1-9*

^def-9-1

> [!remark]- Connections
> - As an orbit space of $\mathrm{U}(1) = S^1$: [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]] (cf. group actions and orbits, [[§25 Actions#^def-25-1|493 Def. §25.1]], [[§27 Orbits#^def-27-1|493 Def. §27.1]]); charts and smooth structure in [[§18 Projective Spaces as Smooth Manifolds#^def-18-2|Def. §18.2]], [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]]; the projection is a submersion, [[§40 Projective Spaces and the Hopf Fibration#^ex-40-2|Ex. §40.2]].
> - Real analogue in MATH 590: [[§38 Fundamental Group of Some Surfaces#^def-38-2|590 Def. §38.2 (Projective n-Space)]], [[Projective plane]].

> [!theorem] Proposition §9.1: $\mathbb{CP}^n$ is Hausdorff and Second Countable
> The quotient topology on $\mathbb{CP}^n$ is $T_2$ and second countable.
>
> *Lee: Problem 1-9*

^prop-9-1

> [!proof]+ Proof (verbal sketch in Lecture 2; the general form is Corollary [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]])
> *(Lecture 4: the graph of the orbit relation is the continuous image of the compact $G \times X$, hence compact, hence closed in the Hausdorff $X \times X$.)* We verify the two hypotheses of the [[§6 Open Quotients#^thm-6-1|Hausdorff Criterion]].
>
> *The relation is open.* For $\xi \in S^1$ define $R_\xi : S^{2n+1} \to S^{2n+1}$, $R_\xi(z) = \xi z$. This is well defined: $|\xi z| = |\xi|\,|z| = |z| = 1$. It is continuous, being the restriction to $S^{2n+1}$ of the $\mathbb{C}$-linear (hence $\mathbb{R}$-linear, hence continuous) map $z \mapsto \xi z$ on $\mathbb{C}^{n+1} \cong \mathbb{R}^{2n+2}$. Since $\xi^{-1} \in S^1$ and $R_{\xi^{-1}} \circ R_\xi = R_\xi \circ R_{\xi^{-1}} = \mathrm{id}$, $R_\xi$ is a homeomorphism; in particular $R_\xi(U)$ is open for every open $U \subseteq S^{2n+1}$. Now let $U \subseteq S^{2n+1}$ be open. For $w \in S^{2n+1}$,
>
> $$\begin{aligned}
> w \in \pi^{-1}(\pi(U)) &\iff \exists\, z \in U \text{ with } w \sim z \\
> &\iff \exists\, z \in U,\ \xi \in S^1 \text{ with } w = \xi z \iff w \in \bigcup_{\xi \in S^1} R_\xi(U),
> \end{aligned}$$
>
> so the saturation $\pi^{-1}(\pi(U)) = \bigcup_{\xi \in S^1} R_\xi(U)$ is a union of open sets, hence open. By [[§4 Quotient Spaces and Open Maps#^prop-4-5|Proposition §4.5]], $\sim$ is open.
>
> *The graph is closed.* Define
>
> $$
> \Phi : S^1 \times S^{2n+1} \longrightarrow S^{2n+1} \times S^{2n+1}, \qquad \Phi(\xi, z) = (z, \xi z).
> $$
>
> By [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10]], $\Phi$ is continuous because its two components are: $(\xi, z) \mapsto z$ is the projection, and $(\xi, z) \mapsto \xi z$ is the restriction of the map $\mathbb{C} \times \mathbb{C}^{n+1} \to \mathbb{C}^{n+1}$, $(\xi, z) \mapsto \xi z$, whose real and imaginary parts are polynomial in the real coordinates. Its image is $\Gamma$: for $(z, w) \in S^{2n+1} \times S^{2n+1}$,
>
> $$\begin{aligned}
> (z, w) \in \Phi\big(S^1 \times S^{2n+1}\big) &\iff \exists\, \xi \in S^1 \text{ with } (z, w) = (z, \xi z) \\
> &\iff \exists\, \xi \in S^1 \text{ with } w = \xi z \iff z \sim w \iff (z,w) \in \Gamma.
> \end{aligned}$$
>
> $S^1 \subseteq \mathbb{R}^2$ and $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$ are closed and bounded, hence compact, and a finite product of compact spaces is compact ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]); so $S^1 \times S^{2n+1}$ is compact and its continuous image $\Gamma$ is compact. The space $S^{2n+1} \times S^{2n+1}$ is a subspace of $\mathbb{R}^{4n+4}$, hence metrizable, hence Hausdorff ([[§1 Point-Set Topology Review#^prop-1-6|Proposition §1.6]]), and a compact subset of a Hausdorff space is closed ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]). Therefore $\Gamma$ is closed in $S^{2n+1} \times S^{2n+1}$.
>
> By the Hausdorff Criterion, $\mathbb{CP}^n$ is $T_2$; and since $S^{2n+1}$ is second countable (subspace of $\mathbb{R}^{2n+2}$) and $\sim$ is open, [[§6 Open Quotients#^thm-6-3|Theorem §6.3]] gives second countability.

^pf-9-1

*Uses:* [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients#^def-6-1|Def. §6.1]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§6 Open Quotients#^thm-6-1|§6.1]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§6 Open Quotients#^thm-6-3|§6.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^ex-1-1|Ex. §1.1]], [[Heine–Borel Theorem]], [[§18 Compact Spaces#^thm-18-9|590 §18.9]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§12 Metric Topology#^thm-12-4|590 §12.4]]

> [!remark]- Connections
> - The general form for compact groups acting on compact Hausdorff spaces: [[§13 Group Actions and Orbit Spaces#^cor-13-4|§13.4]], of which this is a special case ([[§13 Group Actions and Orbit Spaces#^rem-13-9|§13, Remark]]).

**Transcription note.** Page 7 of the handwritten notes writes the map in this argument as $S^1 \times S^{2n+1} \to S^{2n+2} \times S^{2n+2}$; the target is $S^{2n+1} \times S^{2n+1}$, where the graph of the relation lives.

**Transcription note.** On the board (and in the handwritten notes) the target of $\Phi$ was written with superscripts $2n+2$; the target must be $S^{2n+1} \times S^{2n+1}$ — pairs of points of the sphere being quotiented — as recorded here.

> [!proof]+ A direct proof that $\mathbb{CP}^n$ is Hausdorff (Assignment 2)
> This bypasses the Hausdorff criterion and exhibits the separating sets. Let $u \neq v$ in $S^{2n+1}/S^1$, with representatives $\vec u, \vec v \in S^{2n+1}$. Their orbits $S^1 \vec u$ and $S^1 \vec v$ are disjoint (distinct orbits), and compact, being images of the compact $S^1$ under $\mu \mapsto \mu\vec u$, $\mu \mapsto \mu \vec v$.
>
> *The orbits are at positive distance.* Let $d = \inf\{|\vec a - \vec b| : \vec a \in S^1\vec u,\ \vec b \in S^1 \vec v\}$. If $d = 0$, choose $\vec a_k \in S^1\vec u$, $\vec b_k \in S^1\vec v$ with $|\vec a_k - \vec b_k| \to 0$; by compactness a subsequence $\vec a_{k_j} \to \vec a \in S^1\vec u$, whence $\vec b_{k_j} \to \vec a$ too, and $\vec a \in S^1 \vec v$ since that orbit is closed. This contradicts disjointness, so $d > 0$.
>
> *Thickened orbits.* Put $r = d/3$ and $A = \bigcup_{\lambda \in S^1} \lambda\, B(\vec u, r)$, $B = \bigcup_{\lambda \in S^1} \lambda\, B(\vec v, r)$, with balls taken in $S^{2n+1}$. Each is open (a union of images of an open set under the homeomorphisms $\vec z \mapsto \lambda\vec z$) and saturated (a union of orbits). If $\lambda\vec z_1 = \lambda'\vec z_2$ with $\vec z_1 \in B(\vec u, r)$, $\vec z_2 \in B(\vec v, r)$, then
>
> $$
> d \le |\lambda\vec u - \lambda'\vec v| \le |\lambda\vec u - \lambda \vec z_1| + |\lambda\vec z_1 - \lambda'\vec z_2| + |\lambda'\vec z_2 - \lambda'\vec v| < r + 0 + r = \tfrac23 d,
> $$
>
> using $|\lambda| = |\lambda'| = 1$; a contradiction, so $A \cap B = \emptyset$. Since $\pi$ is open and $A$, $B$ are disjoint and saturated, $\pi(A)$ and $\pi(B)$ are disjoint open neighbourhoods of $u$ and $v$.

^pf-9-1-2

*Uses:* [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def. §4.6]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§9 Complex Projective Space#^pf-9-1|§9.1 (openness of the relation)]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§19 Limit Point Compactness#^thm-19-4|590 §19.4]]

> [!remark] Remark
> The one place the group enters the direct proof is $|\lambda \vec u - \lambda \vec z_1| = |\vec u - \vec z_1|$: every $\lambda \in S^1$ is an *isometry*, so the thickening by $r$ is uniform over the whole group. That uniformity — a compact group acting by isometries — is the concrete mechanism behind [[§13 Group Actions and Orbit Spaces#^cor-13-4|Corollary §13.4]], and it is exactly what fails for $\mathbb{R}^+$ in [[§13 Group Actions and Orbit Spaces#^ex-13-6|Example §13.6]], where $t \cdot (x,y) = (tx, y/t)$ distorts distances without bound.

^rem-9-1

> [!theorem] Proposition §9.2: $\mathbb{CP}^n$ Is Compact
> $\mathbb{CP}^n$ is compact.
>
> *Lee: Problem 1-9*

^prop-9-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$ is closed and bounded, hence compact ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]](1)), and $\mathbb{CP}^n = \pi(S^{2n+1})$ is its image under the continuous surjection $\pi$.

^pf-9-2

*Uses:* [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]

> [!theorem] Proposition §9.3: $\mathbb{CP}^n$ as the Space of Complex Lines
> Let the multiplicative group $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ act on $\mathbb{C}^{n+1} \setminus \{0\}$ by scalar multiplication, $\lambda \cdot \vec z = \lambda \vec z$. Then:
> 1. this is a continuous action, and the orbit of $\vec z$ is the punctured complex line $\operatorname{span}_{\mathbb{C}}(\vec z) \setminus \{0\}$; so the orbit space $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$ is in natural bijection with the set of complex lines through the origin in $\mathbb{C}^{n+1}$;
> 2. the map
>
> $$
> \Theta : \big(\mathbb{C}^{n+1} \setminus \{0\}\big)/\mathbb{C}^\times \longrightarrow S^{2n+1}/S^1, \qquad \mathbb{C}^\times\vec z \longmapsto S^1 \cdot \frac{\vec z}{|\vec z|},
> $$
>
> is a homeomorphism.
>
> Consequently the two natural quotient topologies on the set of lines agree, and either may be taken as the topology of $\mathbb{CP}^n$.
>
> *Lee: Problem 1-9*

^prop-9-3

![[m591-3-7.svg]]
*Here $g(\vec z) = \vec z/|\vec z|$ and $\iota$ is the inclusion. Both squares commute: $\Theta \circ \pi_1 = \pi_2 \circ g$ and $\Psi \circ \pi_2 = \pi_1 \circ \iota$. Upstairs, $g$ and $\iota$ are **not** mutually inverse — $g \circ \iota = \mathrm{id}$, but $\iota \circ g$ replaces $\vec z$ by $\vec z/|\vec z|$. Downstairs they become inverse, because passing to the quotient forgets exactly the scale that $\iota \circ g$ changes. The proof below is the chase around these two squares.*

> [!proof]+ Proof
> Write $\pi_1 : \mathbb{C}^{n+1}\setminus\{0\} \to (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$ and $\pi_2 : S^{2n+1} \to S^{2n+1}/S^1$ for the two projections, both quotient maps.
>
> (1) If $\lambda \neq 0$ and $\vec z \neq 0$ then $\lambda\vec z \neq 0$, so the action preserves $\mathbb{C}^{n+1}\setminus\{0\}$. The axioms are $1 \cdot \vec z = \vec z$ and associativity of multiplication in $\mathbb{C}$, coordinatewise. Continuity: each component $(\lambda, \vec z) \mapsto \lambda z_k$ is polynomial in the real and imaginary parts ([[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Definition §11.9]]), and the action is the restriction of this map to a subspace. The orbit $\{\lambda\vec z : \lambda \neq 0\}$ is $\operatorname{span}_{\mathbb{C}}(\vec z) \setminus \{0\}$, and a line $\ell$ is recovered from $\ell \setminus \{0\}$ by adjoining $0$.
>
> (2) *$\Theta$ is well defined and continuous.* Let $g(\vec z) = \vec z/|\vec z|$, continuous on $\mathbb{C}^{n+1} \setminus \{0\}$ with values in $S^{2n+1}$. For $\lambda \in \mathbb{C}^\times$,
>
> $$
> g(\lambda\vec z) = \frac{\lambda}{|\lambda|}\, g(\vec z), \qquad \Big|\frac{\lambda}{|\lambda|}\Big| = 1,
> $$
>
> so $g(\lambda\vec z)$ and $g(\vec z)$ lie in the same $S^1$-orbit: $\pi_2 \circ g$ is constant on the fibres of $\pi_1$, although $g$ itself is not. By the universal property ([[§5 Quotient Maps#^thm-5-1|Theorem §5.1]]), $\pi_2 \circ g$ descends to a unique continuous map on the $\mathbb{C}^\times$-quotient, which is $\Theta$.
>
> *The inverse is continuous.* Let $\iota : S^{2n+1} \hookrightarrow \mathbb{C}^{n+1}\setminus\{0\}$ be the inclusion. Then $\pi_1 \circ \iota$ is continuous and constant on $S^1$-orbits, since $S^1 \subseteq \mathbb{C}^\times$; so it descends to a continuous $\Psi : S^{2n+1}/S^1 \to (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$, $S^1\vec z \mapsto \mathbb{C}^\times \vec z$.
>
> *They are mutually inverse.* For $|\vec z| = 1$, $\Theta(\Psi(S^1\vec z)) = S^1 \vec z$; for $\vec z \neq 0$, $\Psi(\Theta(\mathbb{C}^\times\vec z)) = \mathbb{C}^\times(\vec z/|\vec z|) = \mathbb{C}^\times\vec z$, the vector $\vec z/|\vec z|$ lying in the $\mathbb{C}^\times$-orbit of $\vec z$.

^pf-9-3

*Uses:* [[§9 Complex Projective Space#^def-9-1|Def. §9.1]], [[§5 Quotient Maps#^ex-5-1|Ex. §5.1]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§13 Group Actions and Orbit Spaces#^def-13-1|Def. §13.1]], [[§13 Group Actions and Orbit Spaces#^def-13-2|Def. §13.2]], [[§13 Group Actions and Orbit Spaces#^def-13-5|Def. §13.5]]

> [!remark]- Connections
> - The $\mathbb{C}^\times$-description gives homogeneous coordinates: [[§18 Projective Spaces as Smooth Manifolds#^def-18-1|Def. §18.1]]; the real analogue is [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|§18.6]].

> [!remark] Remark
> The key identity behind (2) is that for a unit vector $\vec z$ the part of its $\mathbb{C}^\times$-orbit lying on the sphere is exactly its $S^1$-orbit: $|\lambda\vec z| = |\lambda|$, which equals $1$ iff $\lambda \in S^1$. So each punctured line meets the unit sphere in precisely one circle, and normalizing $\vec z \mapsto \vec z/|\vec z|$ is the bridge between the two descriptions — a point downstairs, a whole line upstairs in one, a circle upstairs in the other.

^rem-9-2

![[m591-3-9.svg]]
*A cartoon in real dimensions: the complex line $\mathbb{C}\vec z$ is drawn as a plane (blue) through the removed origin, and the unit sphere $S^{2n+1}$ cuts it in exactly one circle, the $S^1$-orbit $S^1\vec z$ (red). Normalizing $g(\vec w) = \vec w/|\vec w|$ pushes every point of the punctured line radially onto that circle — $\vec z$ and $\lambda\vec z$ land on different points of it, but on the same circle. So one $\mathbb{C}^\times$-orbit upstairs corresponds to one $S^1$-orbit, which is why $\Theta$ is a bijection.*

> [!example] Example §9.1: Why the Origin Must Be Removed
> Let $\mathbb{C}^\times$ act instead on all of $\mathbb{C}^{n+1}$ by scalar multiplication. The action is still continuous, but the orbit space acquires one extra point, the orbit $\{\lambda \cdot 0\} = \{0\}$, which is not a line; and that point cannot be separated from any other. Indeed, let $U$ be an open set of the quotient containing $\{0\}$. Its preimage is open, saturated, and contains $0$, hence contains a ball $B(0,\varepsilon)$. For every $\vec z \neq 0$ the vector $\frac{\varepsilon}{2|\vec z|}\vec z$ lies in that ball and in the orbit of $\vec z$, so by saturation the preimage contains every orbit. Thus $U$ is the whole quotient: every neighbourhood of $\{0\}$ contains every point, and the quotient is not Hausdorff. Deleting the origin removes exactly this one orbit. Every orbit accumulates at $0$ — the same pathology as [[§13 Group Actions and Orbit Spaces#^ex-13-6|Example §13.6]], where orbits accumulate on other orbits, here concentrated at a single point.

^ex-9-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def. §4.6]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]]

> [!remark] Remark: Where This Is Going
> $\mathbb{CP}^n$ is “one of the main examples of manifolds” and will recur throughout the course. With $T_2$ and second countability now secured, what is missing from manifold status is the locally Euclidean condition — charts on $\mathbb{CP}^n$ — which is supplied in [[§18 Projective Spaces as Smooth Manifolds|§18, Projective Spaces as Smooth Manifolds]], together with the smooth structure. The same two-step pattern ($\sim$ open via a group acting by homeomorphisms + graph closed via compactness) is the template for many quotient constructions to come: real projective space $\mathbb{RP}^n$ (Lee Example 1.5), Grassmannians, tori, and lens spaces all fit it.

^rem-9-3