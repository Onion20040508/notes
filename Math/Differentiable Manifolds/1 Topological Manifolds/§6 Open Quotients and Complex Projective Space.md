---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 6
tags: [differentiable-manifolds, math591]
---
← [[§5 Quotient Maps]] · ↑ [[· 1 Topological Manifolds]] · [[§7 The Regular Value Theorem]] →

*Thread: quotients — When is a quotient Hausdorff? For open relations, exactly when the graph is closed (Theorem [[§6 Open Quotients and Complex Projective Space#^thm-6-1|§6.1]]); $\mathbb{CP}^n$ is the first manifold built this way. The question returns for orbit spaces ([[§10 Group Actions and Orbit Spaces|§10]]) and coset spaces ([[§11 Homogeneous Spaces|§11]]).*

> [!definition] Definition §6.1: Graph of a Relation
> The **graph** of a relation $\sim$ on a set $X$ is
>
> $$
> \Gamma = \{\, (x, y) \in X \times X \mid x \sim y \,\} \subseteq X \times X .
> $$

^def-6-1

> [!theorem] Theorem §6.1: Hausdorff Criterion
> Assume $\sim$ is an *open* equivalence relation on a topological space $X$, and let $\Gamma \subseteq X \times X$ be its graph ([[§6 Open Quotients and Complex Projective Space#^def-6-1|Definition §6.1]]). Then:
>
> $$
> X/{\sim} \text{ is } T_2 \iff \Gamma \text{ is closed in } X \times X.
> $$
>
> *Lee: no counterpart; a course result (see the comparison below Theorem [[§6 Open Quotients and Complex Projective Space#^thm-6-3|§6.3]])*

^thm-6-1

> [!proof]+ Proof (given in full in lecture)
> ($\Leftarrow$) Assume $\Gamma$ is closed. Let $[x] \neq [y]$ in $X/{\sim}$, i.e. $x \not\sim y$, i.e. $(x, y) \notin \Gamma$. Since $\Gamma$ is closed, its complement is an open set containing $(x,y)$, so by the box characterization ([[§3 Subspaces and Products#^prop-3-8|Proposition §3.8]]) there exist neighborhoods $U$ of $x$ and $V$ of $y$ such that
>
> $$
> (U \times V) \cap \Gamma = \emptyset.
> $$
>
> Now push forward: $\pi(U)$ and $\pi(V)$ are open in $X/{\sim}$ *because the relation is open*, and $[x] \in \pi(U)$, $[y] \in \pi(V)$.
>
> **Claim:** $\pi(U) \cap \pi(V) = \emptyset$. If not, there exist $a \in U$, $b \in V$ with $\pi(a) = \pi(b)$. But $\pi(a) = \pi(b)$ means exactly $a \sim b$, i.e. $(a, b) \in \Gamma$; and $(a,b) \in U \times V$, so $(U \times V) \cap \Gamma \neq \emptyset$ — contradiction.
>
> Thus $\pi(U), \pi(V)$ separate $[x]$ and $[y]$, and $X/{\sim}$ is $T_2$.
>
> ($\Rightarrow$) Assume $X/{\sim}$ is $T_2$; we show the complement of $\Gamma$ is open. Take $(x, y) \in (X \times X) \setminus \Gamma$, i.e. $x \not\sim y$, i.e. $\pi(x) \neq \pi(y)$. By assumption there exist neighborhoods $A$ of $\pi(x)$ and $B$ of $\pi(y)$ in $X/{\sim}$ with $A \cap B = \emptyset$. Careful: $A$ and $B$ live in the *quotient*, not in $X$ — so pull back. Since $\pi$ is continuous, $\pi^{-1}(A) \times \pi^{-1}(B)$ is an open neighborhood of $(x, y)$ in $X \times X$.
>
> **Claim:** $\left(\pi^{-1}(A) \times \pi^{-1}(B)\right) \cap \Gamma = \emptyset$. Suppose by contradiction there is $(a, b) \in \Gamma$ with $a \in \pi^{-1}(A)$ and $b \in \pi^{-1}(B)$. Then $\pi(a) \in A$ and $\pi(b) \in B$; but $(a,b) \in \Gamma$ means $a \sim b$, so $\pi(a) = \pi(b)$. This common point lies in $A \cap B$, so $A \cap B \neq \emptyset$ — contradiction.
>
> Hence every point of the complement of $\Gamma$ has a neighborhood inside the complement, so $\Gamma$ is closed. (Note openness of $\sim$ was not used in this direction.)

^pf-6-1

*Uses:* [[§6 Open Quotients and Complex Projective Space#^def-6-1|Def. §6.1]], [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]], [[§3 Subspaces and Products#^prop-3-8|§3.8]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

![[m591-3-6.svg]]
*The direction ($\Leftarrow$): a point $(x,y)$ off the closed graph $\Gamma$ has a box $U \times V$ missing $\Gamma$, and then $\pi(U)$ and $\pi(V)$ separate $[x]$ from $[y]$.*

> [!remark]- Connections
> - Applied to orbit spaces: [[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]], [[§10 Group Actions and Orbit Spaces#^thm-10-5|§10.5]]; the failure mode is [[§10 Group Actions and Orbit Spaces#^ex-10-6|Ex. §10.6]].
> - Hausdorff spaces in MATH 590: [[§8 Hausdorff Spaces#^def-8-1|590 Def. §8.1]]; for the special case of a quotient onto a Hausdorff space, compare [[§12 Quotient Topology#^cor-12-4|590 §12.4]](2).

> [!remark] Remark: No Hausdorff Hypothesis on $X$
> Mid-statement, Uribe began to add the hypothesis “assume $X$ is Hausdorff”—then stopped: “actually, I don't need that.” The final statement is correct as it stands: no separation assumption on $X$ is required, only openness of the relation. (Openness, moreover, is used only in the direction $\Leftarrow$; the direction $\Rightarrow$ holds for arbitrary equivalence relations, as the [[§6 Open Quotients and Complex Projective Space#^pf-6-1|proof]] shows.)

^rem-6-1

> [!theorem] Corollary §6.2: The Diagonal Criterion
> A topological space $X$ is Hausdorff if and only if the diagonal $\Delta = \{(x,x) \mid x \in X\}$ is closed in $X \times X$.

^cor-6-2

> [!proof]+ Proof
> Apply [[§6 Open Quotients and Complex Projective Space#^thm-6-1|Theorem §6.1]] to the trivial relation, $x \sim y \iff x = y$. It is open, since every set is its own saturation. Its graph is $\Gamma = \Delta$. And $\pi : X \to X/{\sim}$ is a continuous open bijection, hence a homeomorphism, so $X/{\sim}$ is Hausdorff iff $X$ is. This classical characterization is the special case of the theorem with nothing identified; the theorem is its generalization to quotients.

^pf-6-2

*Uses:* [[§6 Open Quotients and Complex Projective Space#^thm-6-1|§6.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients and Complex Projective Space#^def-6-1|Def. §6.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (2), [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

> [!remark] Remark: This Is the Tool
> Uribe (emphasized): “this is going to be our tool for figuring out whether a quotient space is $T_2$.” The workflow it suggests, and which the [[§6 Open Quotients and Complex Projective Space#^prop-6-4|ℂPⁿ example below]] executes: (i) show the relation is open — usually via the saturation slogan; (ii) show the graph is closed — often by exhibiting $\Gamma$ as a preimage of a closed set, or as a compact set inside a Hausdorff space.

^rem-6-2

> [!theorem] Theorem §6.3: Second Countability of Open Quotients
> If $\sim$ is an open equivalence relation and $X$ is second countable, then $X/{\sim}$ is second countable.
>
> *Lee: no counterpart; a course result*

^thm-6-3

> [!proof]+ Proof (one line in lecture — “project the countable basis”)
> $\pi : X \to X/{\sim}$ is a continuous surjection, and open because $\sim$ is; so [[§5 Quotient Maps#^lem-5-6|Lemma §5.6]] applies and the image of a countable basis of $X$ is a countable basis of $X/{\sim}$.

^pf-6-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§5 Quotient Maps#^lem-5-6|§5.6]]

> [!remark]- Connections
> - Reused for coset spaces: [[§11 Homogeneous Spaces|§11]].

**Comparison with Lee.** Lee's Appendix A has no counterpart to Theorems [[§6 Open Quotients and Complex Projective Space#^thm-6-1|§6.1]] and [[§6 Open Quotients and Complex Projective Space#^thm-6-3|§6.3]]: in his book the Hausdorff property and second countability of $\mathbb{RP}^n$ and $\mathbb{CP}^n$ are checked example by example (Example 1.5, Problem 1-9). The course proves one criterion for all open quotients at once and then reuses it for orbit spaces ([[§10 Group Actions and Orbit Spaces|§10]]) and coset spaces ([[§11 Homogeneous Spaces|§11]]) — which is what makes the quotient thread a thread.

> [!example] Example §6.1: The Line with Two Origins — via the Criterion
> Let $X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\}) \subseteq \mathbb{R}^2$ with the subspace topology (two disjoint copies of $\mathbb{R}$), and $(x,1) \sim (x,2)$ for $x \neq 0$, as in [[§4 Quotient Spaces and Open Maps#^ex-4-1|Example §4.1]]. The graph
>
> $$
> \Gamma = \{(a,b) \in X \times X \mid a = b\} \cup \{\, ((x,i),(x,j)) \mid x \neq 0,\ i \neq j \,\}
> $$
>
> is *not* closed in $X \times X$: the points $\big((\tfrac1n, 1), (\tfrac1n, 2)\big)$ lie in $\Gamma$ for every $n$, and converge in $X \times X$ to $\big((0,1),(0,2)\big)$, which is not in $\Gamma$ (the two origins are distinct and are not identified, the identification being imposed only for $x \neq 0$). A closed set contains the limits of its convergent sequences, so $\Gamma$ is not closed.
>
> The relation is open: the saturation of an open $U \subseteq X$ is $U \cup \sigma(U \setminus (\{0\} \times \{1,2\}))$, where $\sigma(x,i) = (x, 3-i)$ swaps the two copies—a homeomorphism of $X$—so the saturation is a union of two open sets. [[§6 Open Quotients and Complex Projective Space#^thm-6-1|Theorem §6.1]] therefore applies and gives: $X/{\sim}$ is *not* Hausdorff. This recovers [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] from the criterion rather than by separating the origins by hand.

^ex-6-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^ex-4-1|Ex. §4.1]], [[§6 Open Quotients and Complex Projective Space#^def-6-1|Def. §6.1]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients and Complex Projective Space#^thm-6-1|§6.1]], [[§11 Metric Topology#^lem-11-8|590 §11.8]]

> [!remark]- Connections
> - “A closed set contains the limits of its convergent sequences” is the [[§11 Metric Topology#^lem-11-8|Sequence Lemma, 590 §11.8]].

PSet 1, Problem 2 asks for the non-closedness of $\Gamma$ directly. The sequence argument above needs no metrizability: in any topological space, if $z_n \to z$ with all $z_n$ in a closed set $C$, then $z \in C$ (otherwise the open set $X \setminus C$ would eventually contain the $z_n$).

## Application: Complex Projective Space

The following was set up in the last four minutes of lecture; the proof of the claim was given verbally, chalk down. **Uribe: “I'll write this again next time”** — so expect a [[§10 Group Actions and Orbit Spaces#^cor-10-4|careful reprise]]; the details below reconstruct the verbal argument.

> [!definition] Definition §6.2: Complex Projective Space $\mathbb{CP}^n$
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

^def-6-2

> [!remark]- Connections
> - As an orbit space of $\mathrm{U}(1) = S^1$: [[§10 Group Actions and Orbit Spaces#^ex-10-3|Ex. §10.3]] (cf. group actions and orbits, [[§23 Actions#^def-23-1|493 Def. §23.1]], [[§25 Orbits#^def-25-1|493 Def. §25.1]]); charts and smooth structure in [[§14 Projective Spaces as Smooth Manifolds#^def-14-2|Def. §14.2]], [[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|§14.2]]; the projection is a submersion, [[§29 Submersions#^ex-29-3|Ex. §29.3]].
> - Real analogue in MATH 590: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 Def. §28.2 (Projective n-Space)]], [[Projective plane]].

> [!theorem] Proposition §6.4: $\mathbb{CP}^n$ is Hausdorff and Second Countable
> The quotient topology on $\mathbb{CP}^n$ is $T_2$ and second countable.
>
> *Lee: Problem 1-9*

^prop-6-4

> [!proof]+ Proof (verbal sketch in Lecture 2; the general form is Corollary [[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]])
> *(Lecture 4: the graph of the orbit relation is the continuous image of the compact $G \times X$, hence compact, hence closed in the Hausdorff $X \times X$.)* We verify the two hypotheses of the [[§6 Open Quotients and Complex Projective Space#^thm-6-1|Hausdorff Criterion]].
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
> By the Hausdorff Criterion, $\mathbb{CP}^n$ is $T_2$; and since $S^{2n+1}$ is second countable (subspace of $\mathbb{R}^{2n+2}$) and $\sim$ is open, [[§6 Open Quotients and Complex Projective Space#^thm-6-3|Theorem §6.3]] gives second countability.

^pf-6-4

*Uses:* [[§6 Open Quotients and Complex Projective Space#^def-6-2|Def. §6.2]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^prop-4-5|§4.5]], [[§6 Open Quotients and Complex Projective Space#^def-6-1|Def. §6.1]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§6 Open Quotients and Complex Projective Space#^thm-6-1|§6.1]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§6 Open Quotients and Complex Projective Space#^thm-6-3|§6.3]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^ex-1-1|Ex. §1.1]], [[Heine–Borel Theorem]], [[§15 Compact Spaces#^thm-15-8|590 §15.8]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§11 Metric Topology#^thm-11-4|590 §11.4]]

> [!remark]- Connections
> - The general form for compact groups acting on compact Hausdorff spaces: [[§10 Group Actions and Orbit Spaces#^cor-10-4|§10.4]], of which this is a special case ([[§10 Group Actions and Orbit Spaces#^rem-10-9|§10, Remark]]).

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

^pf-6-4-2

*Uses:* [[§6 Open Quotients and Complex Projective Space#^def-6-2|Def. §6.2]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§6 Open Quotients and Complex Projective Space#^pf-6-4|§6.4 (openness of the relation)]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§16 Limit Point Compactness#^thm-16-2|590 §16.2]]

> [!remark] Remark
> The one place the group enters the direct proof is $|\lambda \vec u - \lambda \vec z_1| = |\vec u - \vec z_1|$: every $\lambda \in S^1$ is an *isometry*, so the thickening by $r$ is uniform over the whole group. That uniformity — a compact group acting by isometries — is the concrete mechanism behind [[§10 Group Actions and Orbit Spaces#^cor-10-4|Corollary §10.4]], and it is exactly what fails for $\mathbb{R}^+$ in [[§10 Group Actions and Orbit Spaces#^ex-10-6|Example §10.6]], where $t \cdot (x,y) = (tx, y/t)$ distorts distances without bound.

^rem-6-3

> [!theorem] Proposition §6.5: $\mathbb{CP}^n$ Is Compact
> $\mathbb{CP}^n$ is compact.
>
> *Lee: Problem 1-9*

^prop-6-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$ is closed and bounded, hence compact ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]](1)), and $\mathbb{CP}^n = \pi(S^{2n+1})$ is its image under the continuous surjection $\pi$.

^pf-6-5

*Uses:* [[§6 Open Quotients and Complex Projective Space#^def-6-2|Def. §6.2]], [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]

> [!theorem] Proposition §6.6: $\mathbb{CP}^n$ as the Space of Complex Lines
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

^prop-6-6

![[m591-3-7.svg]]
*Here $g(\vec z) = \vec z/|\vec z|$ and $\iota$ is the inclusion. Both squares commute: $\Theta \circ \pi_1 = \pi_2 \circ g$ and $\Psi \circ \pi_2 = \pi_1 \circ \iota$. Upstairs, $g$ and $\iota$ are **not** mutually inverse — $g \circ \iota = \mathrm{id}$, but $\iota \circ g$ replaces $\vec z$ by $\vec z/|\vec z|$. Downstairs they become inverse, because passing to the quotient forgets exactly the scale that $\iota \circ g$ changes. The proof below is the chase around these two squares.*

> [!proof]+ Proof
> Write $\pi_1 : \mathbb{C}^{n+1}\setminus\{0\} \to (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$ and $\pi_2 : S^{2n+1} \to S^{2n+1}/S^1$ for the two projections, both quotient maps.
>
> (1) If $\lambda \neq 0$ and $\vec z \neq 0$ then $\lambda\vec z \neq 0$, so the action preserves $\mathbb{C}^{n+1}\setminus\{0\}$. The axioms are $1 \cdot \vec z = \vec z$ and associativity of multiplication in $\mathbb{C}$, coordinatewise. Continuity: each component $(\lambda, \vec z) \mapsto \lambda z_k$ is polynomial in the real and imaginary parts ([[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Definition §8.8]]), and the action is the restriction of this map to a subspace. The orbit $\{\lambda\vec z : \lambda \neq 0\}$ is $\operatorname{span}_{\mathbb{C}}(\vec z) \setminus \{0\}$, and a line $\ell$ is recovered from $\ell \setminus \{0\}$ by adjoining $0$.
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

^pf-6-6

*Uses:* [[§6 Open Quotients and Complex Projective Space#^def-6-2|Def. §6.2]], [[§5 Quotient Maps#^ex-5-1|Ex. §5.1]], [[§5 Quotient Maps#^thm-5-1|§5.1]], [[§8 Topological Groups and Classical Matrix Groups#^def-8-8|Def. §8.8]], [[§10 Group Actions and Orbit Spaces#^def-10-1|Def. §10.1]], [[§10 Group Actions and Orbit Spaces#^def-10-2|Def. §10.2]], [[§10 Group Actions and Orbit Spaces#^def-10-5|Def. §10.5]]

> [!remark]- Connections
> - The $\mathbb{C}^\times$-description gives homogeneous coordinates: [[§14 Projective Spaces as Smooth Manifolds#^def-14-1|Def. §14.1]]; the real analogue is [[§14 Projective Spaces as Smooth Manifolds#^prop-14-6|§14.6]].

> [!remark] Remark
> The key identity behind (2) is that for a unit vector $\vec z$ the part of its $\mathbb{C}^\times$-orbit lying on the sphere is exactly its $S^1$-orbit: $|\lambda\vec z| = |\lambda|$, which equals $1$ iff $\lambda \in S^1$. So each punctured line meets the unit sphere in precisely one circle, and normalizing $\vec z \mapsto \vec z/|\vec z|$ is the bridge between the two descriptions — a point downstairs, a whole line upstairs in one, a circle upstairs in the other.

^rem-6-4

![[m591-3-9.svg]]
*A cartoon in real dimensions: the complex line $\mathbb{C}\vec z$ is drawn as a plane (blue) through the removed origin, and the unit sphere $S^{2n+1}$ cuts it in exactly one circle, the $S^1$-orbit $S^1\vec z$ (red). Normalizing $g(\vec w) = \vec w/|\vec w|$ pushes every point of the punctured line radially onto that circle — $\vec z$ and $\lambda\vec z$ land on different points of it, but on the same circle. So one $\mathbb{C}^\times$-orbit upstairs corresponds to one $S^1$-orbit, which is why $\Theta$ is a bijection.*

> [!example] Example §6.2: Why the Origin Must Be Removed
> Let $\mathbb{C}^\times$ act instead on all of $\mathbb{C}^{n+1}$ by scalar multiplication. The action is still continuous, but the orbit space acquires one extra point, the orbit $\{\lambda \cdot 0\} = \{0\}$, which is not a line; and that point cannot be separated from any other. Indeed, let $U$ be an open set of the quotient containing $\{0\}$. Its preimage is open, saturated, and contains $0$, hence contains a ball $B(0,\varepsilon)$. For every $\vec z \neq 0$ the vector $\frac{\varepsilon}{2|\vec z|}\vec z$ lies in that ball and in the orbit of $\vec z$, so by saturation the preimage contains every orbit. Thus $U$ is the whole quotient: every neighbourhood of $\{0\}$ contains every point, and the quotient is not Hausdorff. Deleting the origin removes exactly this one orbit. Every orbit accumulates at $0$ — the same pathology as [[§10 Group Actions and Orbit Spaces#^ex-10-6|Example §10.6]], where orbits accumulate on other orbits, here concentrated at a single point.

^ex-6-2

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

> [!remark] Remark: Where This Is Going
> $\mathbb{CP}^n$ is “one of the main examples of manifolds” and will recur throughout the course. With $T_2$ and second countability now secured, what is missing from manifold status is the locally Euclidean condition — charts on $\mathbb{CP}^n$ — which is supplied in [[§14 Projective Spaces as Smooth Manifolds|§14, Projective Spaces as Smooth Manifolds]], together with the smooth structure. The same two-step pattern ($\sim$ open via a group acting by homeomorphisms + graph closed via compactness) is the template for many quotient constructions to come: real projective space $\mathbb{RP}^n$ (Lee Example 1.5), Grassmannians, tori, and lens spaces all fit it.

^rem-6-5
