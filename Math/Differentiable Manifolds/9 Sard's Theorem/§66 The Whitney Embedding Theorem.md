---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 66
tags: [differentiable-manifolds, math591]
---
← [[§65 Partitions of Unity]] · ↑ [[· 9 Sard's Theorem]] · [[§67 Integral Curves]] →

*Stage: analysis — Every manifold sits inside some Euclidean space; Sard's theorem pushes the dimension down to $2m + 1$.*

*Lecture 21: the Whitney embedding and immersion theorems. (To cover more of the syllabus some proofs are skipped; degree theory, officially on the syllabus, is left to assigned reading.)*

The proof, for $M$ compact, has two parts with entirely different ideas: bump functions embed $M$ in some $\mathbb{R}^k$ (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]]), and projections along well-chosen lines lower the dimension (Lemmas [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]] and [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]]). The lemmas come first; Theorem [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]] assembles them. The general case, Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], is sketched in [[§66 The Whitney Embedding Theorem|§66]].

> [!theorem] Lemma §66.1: Compact Manifolds Embed in Some $\mathbb{R}^k$
> Let $M$ be a compact smooth manifold of dimension $m$. Then there is an embedding $F : M \to \mathbb{R}^k$ for some $k$.
>
> *Lee: proof of Theorem 6.15*

^lem-66-1

> [!proof]+ Proof
> *(Lecture 21, Part I of the proof of Theorem [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]], in the lecture's steps with details filled in.)* The tool is bump functions; the idea of a partition of unity ([[§65 Partitions of Unity|§65]]) is behind the construction.
>
> *The cover.* For every $x \in M$ choose a chart $(U_x, \varphi_x)$ at $x$ and an open coordinate ball $B_x \ni x$ with $\overline{B_x} \subseteq U_x$ and $\varphi_x(\overline{B_x})$ a closed ball in $\mathbb{R}^m$ — possible because $\varphi_x(U_x)$ is open, so it contains a closed Euclidean ball about $\varphi_x(x)$, whose preimage under $\varphi_x$ is $\overline{B_x}$. Let $\chi_x \in C^\infty_0(M)$ with $\operatorname{supp}\chi_x \subseteq U_x$ and $\chi_x \equiv 1$ on $\overline{B_x}$ (the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]). The *open* balls $B_x$ cover $M$; it matters that the cover is by the $B_x$, not the $U_x$, since the steps below use $\chi_i \equiv 1$ on $B_i$. $M$ is compact, so finitely many cover; relabel them $B_1, \ldots, B_n$, with charts $(U_i, \varphi_i)$ and bump functions $\chi_i$.
>
> *The map.* Each $\chi_i\varphi_i : M \to \mathbb{R}^m$, defined as $\chi_i \varphi_i$ on $U_i$ and $0$ outside, is smooth: it is smooth on $U_i$ and zero on the open set $M \setminus \operatorname{supp}\chi_i$, and these cover $M$ ($\operatorname{supp}\chi_i$ is compact, hence closed). Define
>
> $$
> F = \big(\chi_1\varphi_1, \ldots, \chi_n\varphi_n, \chi_1, \ldots, \chi_n\big) : M \to \mathbb{R}^{nm + n},
> $$
>
> a large Euclidean space: $n$ blocks of $m$ components, then $n$ scalars.
>
> *$F$ is injective.* Suppose $F(p) = F(q)$. There is $i$ with $p \in B_i$, so $\chi_i(p) = 1$. The last $n$ components of $F$ are the $\chi$'s, so $\chi_i(q) = \chi_i(p) = 1$; in particular $\chi_i(q) \neq 0$, so $q \in U_i$, because $\chi_i$ vanishes outside $U_i$ ($q$ need not lie in $B_i$). The $i$-th block gives $\chi_i(p)\varphi_i(p) = \chi_i(q)\varphi_i(q)$, that is, $\varphi_i(p) = \varphi_i(q)$; the charts are bijective, so $p = q$. The last $n$ components, the $\chi$'s, are what place $p$ and $q$ in the same coordinate chart.
>
> *$F$ is an immersion.* Write $F = (F_1, \ldots, F_n, \chi_1, \ldots, \chi_n)$ with $F_j = \chi_j\varphi_j : M \to \mathbb{R}^m$. Let $p \in M$, $v \in T_pM$, and $\gamma$ a curve with $\gamma(0) = p$ and $D_\gamma = v$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]). Using curves, $dF_p(v) = \frac{d}{dt}\big|_{t=0} F(\gamma(t)) = (v_1, \ldots, v_n, \ldots)$, with $v_j = d(F_j)_p(v) \in \mathbb{R}^m$, componentwise. Choose $i$ with $p \in B_i$. Then $\chi_i \equiv 1$ on the open set $B_i \ni p$, so $F_i = \varphi_i$ near $p$ and $v_i = d(\varphi_i)_p(v)$ — equivalently $d(\chi_i)_p = 0$, since $\chi_i \equiv 1$ in a neighbourhood of $p$. As $\varphi_i$ is a diffeomorphism onto its image (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), $v \neq 0$ gives $v_i \neq 0$, so $dF_p(v) \neq 0$: $dF_p$ is injective.
>
> *An embedding.* An injective immersion of a compact manifold is an embedding (Corollary [[§44 Embeddings#^cor-44-6|§44.6]]).

^pf-66-1

*Uses:* [[§56 Vector Fields#^prop-56-4|§56.4]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§44 Embeddings#^cor-44-6|§44.6]]

![[m591-61-1.svg]]

The lecture's cartoon for injectivity: $\chi_i \equiv 1$ on $\overline{B}_i$ (possibly also a little outside it), and zero outside $U_i$. So $\chi_i(q) = 1$ forces $q \in U_i$, where the chart $\varphi_i$ separates points.

*Part II: lower the ambient dimension.* By Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]], a compact $M$ may be taken to be a regular submanifold $M \subseteq \mathbb{R}^N$ (the image of the embedding, Theorem [[§44 Embeddings#^thm-44-1|§44.1]]). Regard $\mathbb{R}^{N-1} \subseteq \mathbb{R}^N$ by $x \mapsto (x, 0)$. To every line $\ell \subseteq \mathbb{R}^N$ through $0$ that is transverse to $\mathbb{R}^{N-1}$, that is, not contained in it, so that $\mathbb{R}^N = \mathbb{R}^{N-1} \oplus \ell$, associate the projection along $\ell$, a linear map $\mathbb{R}^N \to \mathbb{R}^{N-1}$ with kernel $\ell$, and its restriction

$$
\pi_\ell : M \longrightarrow \mathbb{R}^{N-1} .
$$

We want: *if $N > 2m + 1$, there is an $\ell$ such that $\pi_\ell$ is an embedding.* Applying this repeatedly lowers $N$ to $2m + 1$, where the hypothesis $N > 2m + 1$ stops holding.

> [!theorem] Lemma §66.2: Lines in a Hyperplane Have Measure Zero
> Identify $\mathbb{R}^{N-1}$ with $\{y \in \mathbb{R}^N : y^N = 0\}$. The set
>
> $$
> H = \{\, [y] \in \mathbb{RP}^{N-1} : y^N = 0 \,\}
> $$
>
> of lines through $0$ contained in $\mathbb{R}^{N-1}$ is an embedded submanifold of $\mathbb{RP}^{N-1}$ of dimension $N - 2$, and it has measure zero in $\mathbb{RP}^{N-1}$.

^lem-66-2

> [!proof]+ Proof
> *(Assignment 6, Problem 4, with $N = 2m + 1$; the submitted solution. The fact is used in the proof of Lemma [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]] as well.)* $H$ is well defined, since $y^N = 0$ is unchanged by scaling $y$. Index the coordinates of $\mathbb{R}^N$ by $1, \ldots, N$, and for $i = 1, \ldots, N$ let $U_i = \{[y] : y^i \neq 0\}$ with the affine chart $\varphi_i([y]) = (y^k/y^i)_{k \neq i}$ (Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]). Then $H \cap U_N = \varnothing$, and for $i \leq N - 1$, $\varphi_i(H \cap U_i)$ is the coordinate hyperplane $\{y^N/y^i = 0\}$ of $\mathbb{R}^{N-1}$. So the charts $\varphi_i$ are slice charts for $H$, and $H$ is an embedded $(N-2)$-dimensional submanifold of $\mathbb{RP}^{N-1}$. Since $N - 2 < N - 1$, $H$ has measure zero in $\mathbb{RP}^{N-1}$ by Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]], applied to its inclusion. *(Filled in: directly from Definition [[§62 Sets of Measure Zero#^def-62-2|§62.2]], the chart images $\varphi_i(H \cap U_i)$ are hyperplanes, of measure zero in $\mathbb{R}^{N-1}$ by the same corollary applied to a linear map $\mathbb{R}^{N-2} \to \mathbb{R}^{N-1}$ onto each.)*

^pf-66-2

*Uses:* [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§63 Sard's Theorem#^cor-63-4|§63.4]], [[§62 Sets of Measure Zero#^def-62-2|Def. §62.2]]

> [!theorem] Lemma §66.3: Projections That Stay Injective
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, with $N > 2m + 1$. Then the lines $\ell \subseteq \mathbb{R}^N$ through $0$ for which $\ell \subseteq \mathbb{R}^{N-1}$, or $\pi_\ell : M \to \mathbb{R}^{N-1}$ is not injective, form a set of measure zero in $\mathbb{RP}^{N-1}$. In particular there are lines $\ell \not\subseteq \mathbb{R}^{N-1}$ with $\pi_\ell$ injective.
>
> *Lee: Lemma 6.13*

^lem-66-3

> [!proof]+ Proof
> *(Lecture 21, Part II of the proof of Theorem [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]].)* The key idea: let $\Delta = \{ (p, p) : p \in M \}$, closed in $M \times M$ since $M$ is Hausdorff, and
>
> $$
> \sigma : (M \times M) \setminus \Delta \longrightarrow \mathbb{RP}^{N-1}, \qquad (p, q) \longmapsto \operatorname{span}(q - p),
> $$
>
> the line through $0$ parallel to the secant from $p$ to $q$, the vector $\vec{pq}$; $q - p \neq 0$ because $p \neq q$. *(Filled in.)* $\sigma$ is smooth: it is $(p, q) \mapsto q - p \in \mathbb{R}^N \setminus \{0\}$ followed by the quotient map to $\mathbb{RP}^{N-1}$, which in the chart $\varphi_i$ of Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]] is $w \mapsto (w_k/w_i)_{k \neq i}$, rational with nonvanishing denominator. Its domain is open in $M \times M$, of dimension $2m$, and $\dim \mathbb{RP}^{N-1} = N - 1$. If $2m < N - 1$, the image of $\sigma$ has measure zero (Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]]). So do the lines contained in $\mathbb{R}^{N-1}$: they form a copy of $\mathbb{RP}^{N-2}$, of lower dimension, whose image under the smooth inclusion has measure zero by the same corollary (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-2|§66.2]]). A union of two sets of measure zero has measure zero (Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]), so its complement is dense (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4), in charts): pick $\ell$ not in the image of $\sigma$ and transverse to $\mathbb{R}^{N-1}$. For such $\ell$, $\pi_\ell$ is injective: $\pi_\ell(p) = \pi_\ell(q)$ means $q - p \in \ker = \ell$, so for $p \neq q$, $\ell = \operatorname{span}(q - p) = \sigma(p, q)$, contrary to the choice. So injectivity is lost exactly when the secant of some pair $p \neq q$ is parallel to the line of projection. The condition $2m < N - 1$ is $N > 2m + 1$, exactly the bound in the statement.

^pf-66-3

*Uses:* [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]], [[§63 Sard's Theorem#^cor-63-4|§63.4]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]], [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]]

![[m591-61-2.svg]]

Projection along a line $\ell$, in the plane ($N = 2$). Points of $M$ slide along lines parallel to $\ell$ onto $\mathbb{R}^{N-1}$. Two points $p \neq q$ collide exactly when the secant $q - p$ is parallel to $\ell$; choosing $\ell$ outside the image of $\sigma$ avoids every such pair. This argument gives the non-optimal Whitney embedding theorem, into $\mathbb{R}^{2m+1}$.

![[m591-61-3.svg]]

*(Not from lecture; figure added.)* Why the bound is $2m + 1$. For a curve ($m = 1$) in $\mathbb{R}^3$ ($N = 3$), $(M \times M) \setminus \Delta$ has dimension $2m = 2 = N - 1$, so the secant directions $\sigma(p, q)$ can fill an open set of $\mathbb{RP}^2$ and Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]] does not apply. Indeed, projecting a curve in space onto a plane along $\ell$ typically produces crossings: here $q - p$ is parallel to $\ell$, and $\pi_\ell(p) = \pi_\ell(q)$. The shadow is still an immersed curve, matching the immersion into $\mathbb{R}^{2m}$ of Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], but not an embedded one.

> [!theorem] Lemma §66.4: When a Projection Is an Immersion
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, $\ell = \mathbb{R}v$ a line with $v^N \neq 0$, and $UM$ the unit tangent bundle (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-5|§42.5]]), with
>
> $$
> G : UM \to \mathbb{RP}^{N-1}, \qquad G(x, u) = [u] .
> $$
>
> Then $G$ is smooth, and the projection $\pi_\ell : M \to \mathbb{R}^{N-1}$ along $\ell$ satisfies $d(\pi_\ell)_x = \pi_\ell|_{T_xM}$, so that
>
> $$
> \pi_\ell \text{ is an immersion} \iff T_xM \cap \ell = \{0\} \text{ for every } x \in M \iff \ell \notin G(UM) .
> $$

^lem-66-4

> [!proof]+ Proof
> *(Assignment 6, Problem 4, with $N = 2m + 1$; the submitted solution, which writes $\pi_v$ for $\pi_\ell$. Tangent spaces are geometric, $T_xM \subseteq \mathbb{R}^N$.)* *The projection.* With $\mathbb{R}^{N-1} = \{y : y^N = 0\}$, the projection with kernel $\ell = \mathbb{R}v$ is
>
> $$
> \pi_\ell(y) = y - \frac{y^N}{v^N}\,v .
> $$
>
> It is linear, its values have last coordinate $0$, and $\pi_\ell(y) = 0$ if and only if $y \in \mathbb{R}v$. On $M$ it is $F = \pi_\ell \circ \iota$, with $\iota : M \hookrightarrow \mathbb{R}^N$ the inclusion.
>
> *The differential of $F$.* Since $\pi_\ell$ is linear, $\pi_\ell(y + tw) = \pi_\ell(y) + t\,\pi_\ell(w)$, so $d(\pi_\ell)_y(w) = \frac{d}{dt}\big|_{t=0}\pi_\ell(y + tw) = \pi_\ell(w)$ for all $y, w \in \mathbb{R}^N$; that is, $d(\pi_\ell)_y = \pi_\ell$. By the chain rule, for $x \in M$, $dF_x = d(\pi_\ell)_x \circ d\iota_x = \pi_\ell|_{T_xM}$.
>
> *Its kernel.* A vector $w \in T_xM$ satisfies $\pi_\ell(w) = 0$ if and only if $w \in \ker \pi_\ell = \mathbb{R}v$, so $\ker dF_x = T_xM \cap \mathbb{R}v$. The linear map $dF_x$ is injective if and only if this is $\{0\}$: no nonzero tangent vector to $M$ at $x$ is parallel to $v$. This is the first equivalence.
>
> *Restating the condition with $G$.* For nonzero $y \in \mathbb{R}^N$, $[y] \in \mathbb{RP}^{N-1}$ is the line $\mathbb{R}y$, so $[y] = [y']$ if and only if $y' = cy$ for some $c \neq 0$. Suppose some nonzero $w \in T_xM$ is parallel to $v$, say $w = cv$; then $c \neq 0$ since $w \neq 0$. Let $u = w/|w|$. Since $T_xM$ is a subspace, $u \in T_xM$, and $|u| = 1$, so $(x, u) \in UM$. Moreover $u = \frac{c}{|w|}\,v$, so $G(x, u) = [u] = [v]$ and $[v] \in G(UM)$. Conversely, suppose $[v] = G(x, u) = [u]$ for some $(x, u) \in UM$. Then $u = cv$ for some $c \neq 0$, so $u$ is a tangent vector to $M$ at $x$, nonzero since $|u| = 1$, and parallel to $v$. Combining both directions with the first equivalence gives the second.
>
> *$G$ is smooth.* It is the composite of the smooth map $(x, u) \mapsto u$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), which takes values in $\mathbb{R}^N \setminus \{0\}$ since $|u| = 1$, with the smooth quotient map $q : \mathbb{R}^N \setminus \{0\} \to \mathbb{RP}^{N-1}$, $q(y) = [y]$, which in the chart $\varphi_i$ of Corollary [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]] is $y \mapsto (y^k/y^i)_{k \neq i}$, rational with nonvanishing denominator.

^pf-66-4

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|§18.5]]

> [!theorem] Lemma §66.5: Projections That Stay Immersions
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, with $N > 2m$. Then the lines $\ell \subseteq \mathbb{R}^N$ through $0$ for which $\ell \subseteq \mathbb{R}^{N-1}$, or $\pi_\ell : M \to \mathbb{R}^{N-1}$ is not an immersion, form a set of measure zero in $\mathbb{RP}^{N-1}$. In particular there are lines $\ell \not\subseteq \mathbb{R}^{N-1}$ with $\pi_\ell$ an immersion.
>
> *Lee: Lemma 6.13; Problem 6-2*

^lem-66-5

> [!proof]+ Proof
> *(Assignment 6, Problem 4: the submitted solution, written there for $N = 2m + 1$; it uses $N$ only through $2m - 1 < N - 1$, so it proves the lemma for every $N > 2m$, one less than Lemma [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]] needs.)* Lecture 21 sketched the same idea as for Lemma [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]], with tangent vectors in place of pairs $(p, q)$, as if $p$ and $q$ were infinitesimally close together: map nonzero tangent vectors to lines, $(p, v) \mapsto \mathbb{R}v$, with $T_pM \subseteq \mathbb{R}^N$ (the homework restricts to unit vectors $v$), and choose $\ell$ also outside its image. A line outside this image gives an immersion precisely because the differential of the projection is the projection itself (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]).
>
> *$G(UM)$ has measure zero.* By Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-5|§42.5]], $UM$ is a regular submanifold of $\mathbb{R}^{2N}$ of dimension $2m - 1$, and $G : UM \to \mathbb{RP}^{N-1}$, $G(x, u) = [u]$, is smooth (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]). Since $\dim UM = 2m - 1 < N - 1 = \dim \mathbb{RP}^{N-1}$, Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]] shows that $G(UM)$ has measure zero in $\mathbb{RP}^{N-1}$.
>
> *The bad lines.* By Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]], a line $\ell \not\subseteq \mathbb{R}^{N-1}$ for which $\pi_\ell$ is not an immersion lies in $G(UM)$. So the lines of the statement lie in $G(UM) \cup H$, with $H$ the lines in $\mathbb{R}^{N-1}$, of measure zero by Lemma [[§66 The Whitney Embedding Theorem#^lem-66-2|§66.2]]. A union of two sets of measure zero has measure zero (Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]), and so does any subset of it.
>
> *Choosing $\ell$.* On the other hand, $\mathbb{RP}^{N-1}$ does not have measure zero, since $\varphi_N(U_N) = \mathbb{R}^{N-1}$ does not have Lebesgue measure zero (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4) and Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]). Hence there exists $[v] \in \mathbb{RP}^{N-1} \setminus \big(G(UM) \cup H\big)$. Let $v$ be any representative. Since $[v] \notin H$, $v^N \neq 0$, so $v \in \mathbb{R}^N \setminus \mathbb{R}^{N-1}$ and $\pi_\ell$, $\ell = \mathbb{R}v$, is defined; since $[v] \notin G(UM)$, Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]] shows that $\pi_\ell : M \to \mathbb{R}^{N-1}$ is an immersion.

^pf-66-5

*Uses:* [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-5|§42.5]], [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]], [[§63 Sard's Theorem#^cor-63-4|§63.4]], [[§66 The Whitney Embedding Theorem#^lem-66-2|§66.2]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]]

> [!theorem] Theorem §66.6: The Whitney Theorems for Compact Manifolds
> Let $M$ be a compact smooth manifold of dimension $m$. Then there is an embedding $M \to \mathbb{R}^{2m+1}$ and an immersion $M \to \mathbb{R}^{2m}$.
>
> *Lee: Theorems 6.15 and 6.18, compact case*

^thm-66-6

> [!proof]+ Proof
> *(Lecture 21, in two steps with entirely different ideas: Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]] and Lemmas [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]]–[[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]]; the immersion lemma was a homework problem, Assignment 6, Problem 4, filled in above.)*
>
> *Step 1: some Euclidean space.* By Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]] there is an embedding $M \to \mathbb{R}^N$ for some $N$. Its image is a regular submanifold diffeomorphic to $M$ (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]); replace $M$ by it.
>
> *Step 2: one dimension less.* Suppose $N > 2m + 1$. By Lemmas [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]] and [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]], the lines $\ell$ that lie in $\mathbb{R}^{N-1}$, or for which $\pi_\ell$ is not injective, or not an immersion, form the union of two sets of measure zero in $\mathbb{RP}^{N-1}$, which has measure zero (Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]). A set of measure zero contains no nonempty open set (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4), in a chart), so it is not all of $\mathbb{RP}^{N-1}$: choose $\ell$ outside it. Then $\pi_\ell : M \to \mathbb{R}^{N-1}$ is an injective immersion of a compact manifold, hence an embedding (Corollary [[§44 Embeddings#^cor-44-6|§44.6]]), and its image is a regular submanifold of $\mathbb{R}^{N-1}$ diffeomorphic to $M$.
>
> *Step 3: repeat.* Apply Step 2 while $N > 2m + 1$, lowering $N$ by one each time until $N = 2m + 1$: this ends with an embedding $M \to \mathbb{R}^{2m+1}$.
>
> *Step 4: the immersion.* *(Assignment 6, Problem 4; the submitted solution's reduction.)* Now $M \subseteq \mathbb{R}^{2m+1}$, and $N = 2m + 1 > 2m$, so Lemma [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]] gives a line $\ell \not\subseteq \mathbb{R}^{2m}$ with $\pi_\ell : M \to \mathbb{R}^{2m}$ an immersion. For the original manifold, compose with the diffeomorphism $\iota$ from $M$ onto its image in $\mathbb{R}^{2m+1}$: if $F'$ is an immersion of $\iota(M)$, then so is $F' \circ \iota$, since by the chain rule $d(F' \circ \iota)_x = dF'_{\iota(x)} \circ d\iota_x$, where $d\iota_x$ is an isomorphism onto $T_{\iota(x)}\iota(M)$ and $dF'_{\iota(x)}$ is injective on $T_{\iota(x)}\iota(M)$. So one more projection is possible: where the embedding stops at $2m + 1$, the immersion goes one dimension further.

^pf-66-6

*Uses:* [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]], [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]], [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]], [[§44 Embeddings#^thm-44-1|§44.1]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]], [[§44 Embeddings#^cor-44-6|§44.6]]

## The Noncompact Case: A Sketch

*Lecture 22. Only a sketch of the proof, with precise references to Lee for the rest. The noncompact proof has the same two parts as the compact one — first put $M$ in some Euclidean space, then project as much as you can — and the lecture sketched only the first. The main tool is the existence of exhaustion functions (Proposition [[§65 Partitions of Unity#^prop-65-10|§65.10]]), proved in [[§65 Partitions of Unity|§65]] with partitions of unity.*

The sketch uses an exhaustion function (Definition [[§65 Partitions of Unity#^def-65-6|§65.6]]): a smooth $f \ge 0$ on $M$ whose sublevel sets $f^{-1}\big((-\infty, c]\big)$ are all compact. Every smooth manifold has one (Proposition [[§65 Partitions of Unity#^prop-65-10|§65.10]]); both are in [[§65 Partitions of Unity|§65]], where partitions of unity give the proof.

*Slicing $M$ into compact pieces.* The idea is to use level sets of an exhaustion function to slice $M$ into compact pieces, which have boundary (ignored in the sketch), to embed each piece, and to keep track of the overlaps. Let $f$ be an exhaustion function. Its singular values have measure zero (Theorem [[§63 Sard's Theorem#^thm-63-3|§63.3]]), so every interval contains regular values; for each $i = 0, 1, 2, \ldots$ pick regular values $a_i, b_i$ with $i < a_i < b_i < i + 1$, and put

$$
E_i = f^{-1}\big([b_{i-1}, a_{i+1}]\big), \qquad D_i = f^{-1}\big([i, i+1]\big) \qquad (i \ge 1),
$$

with $E_0 = f^{-1}\big((-\infty, a_1]\big)$ and $D_0 = f^{-1}\big((-\infty, 1]\big)$. Each $E_i$ is compact (a closed subset of a sublevel set), and a manifold with boundary, because $b_{i-1}$ and $a_{i+1}$ are regular values. Then $M = \bigcup_i D_i$, $D_i \subseteq \operatorname{Int}E_i$, and, for later use,

$$
E_i \cap E_{i+2} = \varnothing ,
$$

since $E_i \subseteq f^{-1}\big((-\infty, a_{i+1}]\big)$ and $E_{i+2} \subseteq f^{-1}\big([b_{i+1}, \infty)\big)$ with $a_{i+1} < b_{i+1}$; more generally $E_i \cap E_j = \varnothing$ when $|i - j| \ge 2$.

![[m591-65-2.svg]]

Left: a sublevel set of an exhaustion function on a surface with holes, as on the board. *(Not from lecture: the surface is plotted, not drawn.)* Here $M$ is the boundary of a thickened ladder in $\mathbb{R}^3$, the zero set of a smooth function: a noncompact surface (it continues upward) with a hole between consecutive rungs, and $f$ is the height, an exhaustion function on $M$; the sublevel set $f^{-1}\big((-\infty, c]\big)$ (orange) is compact. Right: the slicing (not pictured in Lee). $E_i$ runs from the regular value $b_{i-1}$, just below $i$, to $a_{i+1}$, just above $i + 1$, and contains the band $D_i$ (teal) between the integer levels $i$ and $i + 1$ in its interior. The height has critical points at the top and bottom of each rung, where the topology of the sublevel sets changes (the starting point of Morse theory); the levels $c$, $a_i$, $b_i$ are regular values, so they miss these heights, and each $E_i$ is a compact manifold with boundary — here $E_i$ contains two of the holes.

> [!theorem] Proposition §66.7: A Proper Embedding from the Slices
> Let $f$ be an exhaustion function on $M$, $\dim M = m$, and $E_i, D_i$ as above. Suppose that each $E_i$ admits an embedding $F_i : E_i \to \mathbb{R}^{2m+1}$, and let $\rho_i : M \to \mathbb{R}$ be smooth with $\operatorname{supp}\rho_i \subseteq \operatorname{Int}E_i$ and $\rho_i \equiv 1$ on a neighbourhood of $D_i$. Then
>
> $$
> F = \Big( \sum_{i \text{ even}} \rho_i F_i,\ \sum_{i \text{ odd}} \rho_i F_i,\ f \Big) : M \longrightarrow \mathbb{R}^{2(2m+1)+1}
> $$
>
> is a proper injective immersion, hence an embedding.
>
> *Lee: Theorem 6.15 (proof)*

^prop-66-7

> [!proof]+ Proof
> *(Lecture 22 gave the construction and the reason for properness; injectivity and the immersion property, completely analogous to the compact case, are filled in from Lee. The two hypotheses are assumed, not proved, in the lecture: that compact manifolds with boundary embed in $\mathbb{R}^{2m+1}$ (manifolds with boundary are not discussed in the course), and that the cutoffs $\rho_i$ exist, which partitions of unity provide.)*
>
> *$F$ is smooth.* $\rho_iF_i$, a priori defined only on $E_i$, extends smoothly by zero outside $E_i$: it is smooth on the open set $\operatorname{Int}E_i$ and zero on the open set $M \setminus \operatorname{supp}\rho_i$, which together cover $M$. The sums are locally finite: the $E_i$ with $i$ of one parity are pairwise disjoint closed sets, and only finitely many of them meet a neighbourhood $f^{-1}\big((c - 1, c + 1)\big)$, since $E_i \subseteq f^{-1}([i - 1, i + 2])$. So near each point at most one term of each sum is nonzero.
>
> *$F$ is proper* — properness comes from having $f$ as a component. If $K \subseteq \mathbb{R}^{2(2m+1)+1}$ is compact, the last coordinate is bounded on $K$, say by $c$, so $F^{-1}(K)$ is a closed subset of the compact sublevel set $f^{-1}\big((-\infty, c]\big)$, hence compact (Definition [[§44 Embeddings#^def-44-2|§44.2]]).
>
> *$F$ is injective.* Suppose $F(p) = F(q)$. Then $f(p) = f(q)$, so if $p \in D_j$ then $q \in D_j$, and $\rho_j(p) = \rho_j(q) = 1$. In the block of the parity of $j$, every other term vanishes at $p$ and $q$: for $i \neq j$ of that parity $|i - j| \ge 2$, so $\operatorname{supp}\rho_i \subseteq E_i$ misses $E_j \supseteq D_j$. So that block reads $F_j(p) = F_j(q)$, and $F_j$ is injective: $p = q$.
>
> *$F$ is an immersion.* Let $p \in D_j$, and $W \subseteq \operatorname{Int}E_j$ an open neighbourhood of $p$ on which $\rho_j \equiv 1$. On $W$ the block of the parity of $j$ is $F_j$, since the other terms of that block are supported in sets $E_i$ disjoint from $E_j$. So that block of $dF_p$ is $d(F_j)_p$, injective because $F_j$ is an embedding; hence $dF_p$ is injective.
>
> *An embedding.* A proper injective immersion is an embedding (Theorem [[§44 Embeddings#^thm-44-5|§44.5]]).

^pf-66-7

*Uses:* [[§44 Embeddings#^def-44-2|Def. §44.2]], [[§44 Embeddings#^thm-44-5|§44.5]]

> [!remark] Remark: Why the Last Coordinate Is $f$
> The last coordinate $f$ in Proposition [[§66 The Whitney Embedding Theorem#^prop-66-7|§66.7]] is not there for injectivity: it makes $F$ proper, since an exhaustion function is proper, and properness is what turns an injective immersion of a noncompact manifold into an embedding (Theorem [[§44 Embeddings#^thm-44-5|§44.5]]).

^rem-66-1

![[m591-65-1.svg]]

*(Not from lecture; figure added.)* Why the noncompact embedding is made proper. The curve $\gamma(t) = \big(\sin 2s, \sin s\big)$, $s = \pi + 2\arctan t$, is an injective immersion $\mathbb{R} \to \mathbb{R}^2$, but both ends approach $\gamma(0)$: the preimage of a small closed disc $\overline{B}$ about $\gamma(0)$ contains two half-lines, so $\gamma$ is not proper, and its image is not an embedded submanifold near $\gamma(0)$. Adding an exhaustion function as an extra coordinate makes the map proper: it pulls the ends apart in height, which is what Proposition [[§66 The Whitney Embedding Theorem#^prop-66-7|§66.7]] does with $f$.

*The projection step.* For a noncompact manifold the image can spread all over the ambient space, and a projection of an injective immersion need not be proper. Lee's remedy, Lemma [[§66 The Whitney Embedding Theorem#^lem-66-8|§66.8]]: squeeze the image into a tube, ball $\times\ \mathbb{R}$, where projections can be controlled. Lee's proof of the theorem also embeds each slice $E_i$, a compact manifold with boundary; manifolds with boundary are not treated in these notes, and the two facts used about them are cited after the lemma (Proposition [[§66 The Whitney Embedding Theorem#^prop-66-9|§66.9]]).

> [!theorem] Lemma §66.8: Proper Embeddings into $\mathbb{R}^{2m+1}$
> Let $M$ be a smooth manifold of dimension $m$. If $M$ admits an embedding into some $\mathbb{R}^N$, then it admits a proper embedding into $\mathbb{R}^{2m+1}$.
>
> *Lee: Lemma 6.14*

^lem-66-8

> [!proof]+ Proof
> *(Lee's proof of Lemma 6.14, the assigned reading of Oct 26; Lee's “simple geometric argument” about two tubes is written out in Step 2(e).)* For a line $S$ through $0$ in $\mathbb{R}^n$ and $R > 0$, the *tube* with axis $S$ and radius $R$ is the open set
>
> $$
> T_R(S) = \{ x \in \mathbb{R}^n : |x - y| < R \text{ for some } y \in S \} .
> $$
>
> *Step 1: a proper embedding into a tube.* Let $F : M \to \mathbb{R}^N$ be an embedding. The map $G : \mathbb{R}^N \to B^N = \{ y : |y| < 1 \}$, $G(x) = x / \sqrt{1 + |x|^2}$, is a diffeomorphism: it is smooth, $|G(x)|^2 = |x|^2 / (1 + |x|^2) < 1$, and $y \mapsto y / \sqrt{1 - |y|^2}$ is a smooth inverse (if $y = G(x)$ then $1 - |y|^2 = 1/(1 + |x|^2)$, so $y / \sqrt{1 - |y|^2} = x$; the other composite is checked the same way). Let $f$ be an exhaustion function on $M$ (Proposition [[§65 Partitions of Unity#^prop-65-10|§65.10]]) and
>
> $$
> \Phi_0 = (G \circ F, f) : M \longrightarrow \mathbb{R}^{N+1} .
> $$
>
> $\Phi_0$ is injective, because $G \circ F$ is. It is an immersion: the first $N$ components of $d(\Phi_0)_p$ form $dG_{F(p)} \circ dF_p$, injective since $dF_p$ is injective and $dG_{F(p)}$ is invertible. It is proper: if $K \subseteq \mathbb{R}^{N+1}$ is compact, the last coordinate is at most some $c$ on $K$, so $\Phi_0^{-1}(K)$ is a closed subset ($\Phi_0$ is continuous) of the compact set $f^{-1}\big((-\infty, c]\big)$, hence compact. By Theorem [[§44 Embeddings#^thm-44-5|§44.5]], $\Phi_0$ is a proper embedding. Its image lies in $B^N \times \mathbb{R} \subseteq T_1(S_0)$, with $S_0$ the last coordinate axis: $(y, t)$ with $|y| < 1$ is at distance $|y| < 1$ from $(0, t) \in S_0$.
>
> *Step 2: lowering the dimension by one.* Claim: *if $\Phi : M \to \mathbb{R}^n$ is a proper embedding with $\Phi(M) \subseteq T_R(S)$ for a line $S$ through $0$, and $n > 2m + 1$, then there are a line $\ell$ and a proper embedding $\Phi' = \pi_\ell \circ \Phi : M \to \mathbb{R}^{n-1}$ with $\Phi'(M) \subseteq T_{R'}(S')$ for a line $S'$ through $0$ in $\mathbb{R}^{n-1}$ and some $R'$.*
>
> (a) *Choice of $\ell$.* $M' = \Phi(M)$ is a regular submanifold of $\mathbb{R}^n$ of dimension $m$, and $\Phi$ is a diffeomorphism onto it (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]). By Lemma [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]] ($n > 2m + 1$) and Lemma [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]] ($n > 2m$), the lines $\ell$ with $\ell \subseteq \mathbb{R}^{n-1}$, or with $\pi_\ell|_{M'}$ not injective, or not an immersion, form a set of measure zero in $\mathbb{RP}^{n-1}$; so does the single point $S$, and so does the union $Z$ of these sets (Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](2), read in charts, Proposition [[§62 Sets of Measure Zero#^prop-62-4|§62.4]]). $Z$ is not all of $\mathbb{RP}^{n-1}$: in a chart $(U, \varphi)$ that would make the nonempty open set $\varphi(U)$ of measure zero, contradicting Lemma [[§62 Sets of Measure Zero#^lem-62-1|§62.1]](4). Choose $\ell = \mathbb{R}v \notin Z$: then $v^n \neq 0$, $\pi_\ell|_{M'}$ is an injective immersion, and $\ell \neq S$.
>
> (b) *$\Phi'$ is an injective immersion.* It is injective as a composite of injective maps. Since $\pi_\ell$ is linear, $d\Phi'_p = \pi_\ell \circ d\Phi_p$; $d\Phi_p$ is injective with image $T_{\Phi(p)}M'$, and $\pi_\ell$ is injective on $T_{\Phi(p)}M'$ because $\pi_\ell|_{M'}$ is an immersion (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]). So $d\Phi'_p$ is injective.
>
> (c) *The new tube.* Let $s$ be a unit vector with $S = \mathbb{R}s$. Since $s \notin \ell = \ker \pi_\ell$, $s' = \pi_\ell(s) \neq 0$; put $S' = \mathbb{R}s'$. A linear map is bounded: $|\pi_\ell(y)| \le C|y|$ for some $C$ and all $y$. For $p \in M$ there is $t$ with $|\Phi(p) - ts| < R$, so $|\Phi'(p) - ts'| = |\pi_\ell(\Phi(p) - ts)| \le CR$, and $\Phi'(M) \subseteq T_{R'}(S')$ with $R' = CR + 1$.
>
> (d) *$\Phi'$ is proper.* Let $K \subseteq \mathbb{R}^{n-1}$ be compact, say $K \subseteq B_{R_1}(0)$. If $\Phi'(p) \in K$, put $x = \Phi(p)$. By the formula of Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]], $\pi_\ell(x) = x - \tfrac{x^n}{v^n}v$, so $x$ lies at distance $|\pi_\ell(x)| < R_1$ from the point $\tfrac{x^n}{v^n}v \in \ell$: $x \in T_{R_1}(\ell)$. Also $x \in T_R(S)$. By (e), $|x| \le D$ for a constant $D$. So $\Phi'^{-1}(K)$ is a closed subset ($\Phi'$ is continuous) of $\Phi^{-1}\big(\overline{B}_D(0)\big)$, which is compact because $\Phi$ is proper; hence $\Phi'^{-1}(K)$ is compact.
>
> (e) *Two tubes with non-parallel axes meet in a bounded set.* Let $u = v/|v|$. The map $(a, b) \mapsto as - bu$ is linear and injective on $\mathbb{R}^2$, since $s$ and $u$ are linearly independent ($\ell \neq S$). The continuous function $(a, b) \mapsto |as - bu|$ is positive on the compact unit circle, so it has a minimum $\mu > 0$ there, and by homogeneity $|as - bu| \ge \mu\sqrt{a^2 + b^2}$ for all $(a, b)$. If $x \in T_R(S) \cap T_{R_1}(\ell)$, write $x = as + e_1 = bu + e_2$ with $|e_1| < R$, $|e_2| < R_1$. Then $|as - bu| = |e_2 - e_1| < R + R_1$, so $|a| < (R + R_1)/\mu$ and $|x| \le |a| + |e_1| < (R + R_1)/\mu + R =: D$.
>
> (f) *Conclusion of the claim.* $\Phi'$ is a proper injective immersion, hence an embedding (Theorem [[§44 Embeddings#^thm-44-5|§44.5]]), with image in the tube $T_{R'}(S')$.
>
> *Step 3: iterate.* Start from $\Phi_0$ ($n = N + 1$). While $n > 2m + 1$, Step 2 lowers $n$ by one, keeping a proper embedding with image in a tube; it stops at a proper embedding into $\mathbb{R}^{2m+1}$. If already $N + 1 \le 2m + 1$, follow $\Phi_0$ by the inclusion $\mathbb{R}^{N+1} \subseteq \mathbb{R}^{2m+1}$, a proper embedding (the preimage of a compact set is its intersection with the closed subspace $\mathbb{R}^{N+1}$); a composite of proper embeddings is a proper embedding.

^pf-66-8

*Uses:* [[§65 Partitions of Unity#^prop-65-10|§65.10]], [[§44 Embeddings#^thm-44-5|§44.5]], [[§44 Embeddings#^thm-44-1|§44.1]], [[§66 The Whitney Embedding Theorem#^lem-66-3|§66.3]], [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]], [[§62 Sets of Measure Zero#^lem-62-1|§62.1]], [[§62 Sets of Measure Zero#^prop-62-4|§62.4]], [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]

> [!theorem] Proposition §66.9: The Slices Are Compact and Embed in $\mathbb{R}^{2m+1}$
> Let $f$ be an exhaustion function on $M$, $\dim M = m$, and let $b < a$ be regular values of $f$. Let $E = f^{-1}\big([b, a]\big)$, or $E = f^{-1}\big((-\infty, a]\big)$.
>
> 1. $E$ is compact, and it is a smooth manifold with boundary contained in $f^{-1}(b) \cup f^{-1}(a)$ (a regular domain in $M$).
> 2. $E$ admits a smooth embedding into $\mathbb{R}^{2m+1}$.
>
> *Lee: Proposition 5.47; proof of Theorem 6.15*

^prop-66-9

> [!proof]+ Proof (not given in this course)
> Compactness: $E$ is closed ($f$ is continuous) and contained in the sublevel set $f^{-1}\big((-\infty, a]\big)$, which is compact (Definition [[§65 Partitions of Unity#^def-65-6|§65.6]]). The rest concerns manifolds with boundary, which these notes do not treat: (1) is Lee, Proposition 5.47, as used in Lee's proof of Theorem 6.15; for (2), Lee's proofs of the compact case (Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]], with regular coordinate half-balls allowed) and of Lemma [[§66 The Whitney Embedding Theorem#^lem-66-8|§66.8]] hold for manifolds with boundary.

^pf-66-9

*Uses:* [[§65 Partitions of Unity#^def-65-6|Def. §65.6]], [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]], [[§66 The Whitney Embedding Theorem#^lem-66-8|§66.8]]

> [!theorem] Proposition §66.10: Immersions into $\mathbb{R}^{2m}$ from Any Embedding
> Let $M \subseteq \mathbb{R}^N$ be a regular submanifold of dimension $m$, with $N \ge 2m$. Then there is a linear surjection $L : \mathbb{R}^N \to \mathbb{R}^{2m}$ such that $L|_M : M \to \mathbb{R}^{2m}$ is an immersion. In particular, every manifold that embeds in some $\mathbb{R}^N$ immerses in $\mathbb{R}^{2m}$.
>
> *Lee: Theorem 6.18*

^prop-66-10

> [!proof]+ Proof
> *(Not from the assignment. Assignment 6, Problem 4, allows “that $M$ can be embedded in some $\mathbb{R}^N$”; the submitted solution starts instead from an embedding in $\mathbb{R}^{2m+1}$, which the course proves for compact $M$ (Theorem [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]]) and in general in Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]] below. This proof needs only some $\mathbb{R}^N$: Lemma [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]] is repeated, keeping the unit tangent bundle of the original $M$, because after one projection the image of $M$ is only immersed, not a submanifold.)* Tangent spaces are geometric, $T_xM \subseteq \mathbb{R}^N$, and $UM \subseteq \mathbb{R}^{2N}$ is the unit tangent bundle, of dimension $2m - 1$ (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-5|§42.5]]).
>
> *The claim, by descending induction on $k$.* For $k = N, N - 1, \ldots, 2m$ there is a linear surjection $L_k : \mathbb{R}^N \to \mathbb{R}^k$ with $\ker L_k \cap T_xM = \{0\}$ for every $x \in M$. For $k = N$ take $L_N = \mathrm{id}$.
>
> *The step.* Suppose $L_k$ is found and $k > 2m$. Since $L_k$ is injective on each $T_xM$, $L_ku \neq 0$ for $(x, u) \in UM$, and
>
> $$
> G_k : UM \to \mathbb{RP}^{k-1}, \qquad G_k(x, u) = [L_ku],
> $$
>
> is smooth: it is $(x, u) \mapsto L_ku \in \mathbb{R}^k \setminus \{0\}$, smooth as the restriction of a linear map (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), followed by the quotient map, smooth as in Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]. As $\dim UM = 2m - 1 < k - 1$, $G_k(UM)$ has measure zero (Corollary [[§63 Sard's Theorem#^cor-63-4|§63.4]]); with Lemma [[§66 The Whitney Embedding Theorem#^lem-66-2|§66.2]] (in $\mathbb{RP}^{k-1}$) there is a line $\ell \subseteq \mathbb{R}^k$, $\ell \not\subseteq \mathbb{R}^{k-1}$, $\ell \notin G_k(UM)$, as in the proof of Lemma [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]]. Put $L_{k-1} = \pi_\ell \circ L_k : \mathbb{R}^N \to \mathbb{R}^{k-1}$, a composite of linear surjections. If $u \in T_xM$, $u \neq 0$, had $L_{k-1}u = 0$, then $L_ku \in \ker \pi_\ell = \ell$ with $L_ku \neq 0$, so $\ell = [L_ku] = G_k(x, u/|u|)$, contrary to the choice of $\ell$. So $\ker L_{k-1} \cap T_xM = \{0\}$.
>
> *Conclusion.* With $L = L_{2m}$: $L|_M = L \circ \iota$ has differential $d(L|_M)_x = L|_{T_xM}$ (the differential of a linear map is the map itself, as in Lemma [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]]), injective for every $x$. So $L|_M$ is an immersion. For the last sentence, an embedding $M \to \mathbb{R}^N$ is a diffeomorphism onto a regular submanifold (Theorem [[§44 Embeddings#^thm-44-1|§44.1]], Corollary [[§44 Embeddings#^cor-44-3|§44.3]]), and an immersion composed with a diffeomorphism is an immersion, by the chain rule.

^pf-66-10

*Uses:* [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]], [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], [[§66 The Whitney Embedding Theorem#^lem-66-5|§66.5]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-5|§42.5]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§66 The Whitney Embedding Theorem#^lem-66-4|§66.4]], [[§63 Sard's Theorem#^cor-63-4|§63.4]], [[§66 The Whitney Embedding Theorem#^lem-66-2|§66.2]], [[§44 Embeddings#^thm-44-1|§44.1]], [[§44 Embeddings#^cor-44-3|§44.3]]

This gives the immersion half of Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]] below (Lee, Theorem 6.18) from an embedding into any Euclidean space, without the dimension $2m + 1$ of the embedding half; for compact $M$, Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]] supplies the embedding.

> [!theorem] Theorem §66.11: The Whitney Embedding and Immersion Theorems
> Let $M$ be a smooth manifold of dimension $m$. Then there is an embedding $M \to \mathbb{R}^{2m+1}$ and an immersion $M \to \mathbb{R}^{2m}$.
>
> *Lee: Theorems 6.15 and 6.18*

^thm-66-11

> [!proof]+ Proof (Lee's proof of Theorem 6.15; the immersion by Proposition [[§66 The Whitney Embedding Theorem#^prop-66-10|§66.10]])
> *(The assigned reading, email of Oct 26: Lee, Lemmas 6.13 and 6.14 and Theorem 6.15; Lecture 22 sketched the noncompact case.)* *Reduction.* By Lemma [[§66 The Whitney Embedding Theorem#^lem-66-8|§66.8]], it suffices to embed $M$ in some Euclidean space; the lemma then gives a proper embedding into $\mathbb{R}^{2m+1}$.
>
> *$M$ compact.* Lemma [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]] gives an embedding into some $\mathbb{R}^k$.
>
> *$M$ noncompact.* Let $f$ be an exhaustion function (Proposition [[§65 Partitions of Unity#^prop-65-10|§65.10]]), and let $a_i, b_i$, $D_i$, $E_i$ be as in the slicing above: regular values $i < a_i < b_i < i + 1$ (they exist by Theorem [[§63 Sard's Theorem#^thm-63-3|§63.3]]), $D_0 = f^{-1}\big((-\infty, 1]\big)$, $E_0 = f^{-1}\big((-\infty, a_1]\big)$, and for $i \ge 1$, $D_i = f^{-1}\big([i, i + 1]\big)$, $E_i = f^{-1}\big([b_{i-1}, a_{i+1}]\big)$. By Proposition [[§66 The Whitney Embedding Theorem#^prop-66-9|§66.9]], each $E_i$ admits an embedding $F_i : E_i \to \mathbb{R}^{2m+1}$.
>
> *The cutoffs.* For $i \ge 1$ choose $c_i, d_i$ with $b_{i-1} < c_i < i$ and $i + 1 < d_i < a_{i+1}$, and put $A_i = f^{-1}\big([c_i, d_i]\big)$, $U_i = f^{-1}\big((b_{i-1}, a_{i+1})\big)$; for $i = 0$ choose $1 < d_0 < a_1$ and put $A_0 = f^{-1}\big((-\infty, d_0]\big)$, $U_0 = f^{-1}\big((-\infty, a_1)\big)$. $A_i$ is closed, $U_i$ is open, $A_i \subseteq U_i$, and $U_i \subseteq E_i$, so $U_i \subseteq \operatorname{Int}E_i$. Proposition [[§65 Partitions of Unity#^prop-65-8|§65.8]] gives a smooth $\rho_i : M \to [0, 1]$ with $\rho_i \equiv 1$ on $A_i$, hence on the open neighbourhood $f^{-1}\big((c_i, d_i)\big)$ of $D_i$ (for $i = 0$, $f^{-1}\big((-\infty, d_0)\big)$), and $\operatorname{supp}\rho_i \subseteq U_i \subseteq \operatorname{Int}E_i$.
>
> *Gluing.* Proposition [[§66 The Whitney Embedding Theorem#^prop-66-7|§66.7]], with these $F_i$ and $\rho_i$, gives a proper embedding
>
> $$
> F = \Big( \sum_{i \text{ even}} \rho_i F_i,\ \sum_{i \text{ odd}} \rho_i F_i,\ f \Big) : M \longrightarrow \mathbb{R}^{2(2m+1)+1} ,
> $$
>
> and the reduction applies.
>
> *The immersion.* $M$ now embeds in $\mathbb{R}^{2m+1}$, so Proposition [[§66 The Whitney Embedding Theorem#^prop-66-10|§66.10]], with $N = 2m + 1 \ge 2m$, gives an immersion $M \to \mathbb{R}^{2m}$.

^pf-66-11

*Uses:* [[§66 The Whitney Embedding Theorem#^lem-66-8|§66.8]], [[§66 The Whitney Embedding Theorem#^lem-66-1|§66.1]], [[§65 Partitions of Unity#^prop-65-10|§65.10]], [[§63 Sard's Theorem#^thm-63-3|§63.3]], [[§66 The Whitney Embedding Theorem#^prop-66-9|§66.9]], [[§65 Partitions of Unity#^prop-65-8|§65.8]], [[§66 The Whitney Embedding Theorem#^prop-66-7|§66.7]], [[§66 The Whitney Embedding Theorem#^prop-66-10|§66.10]]

In other words, every manifold is diffeomorphic to a submanifold of some Euclidean space (Theorem [[§44 Embeddings#^thm-44-1|§44.1]]). The course proves the compact case in full (Theorem [[§66 The Whitney Embedding Theorem#^thm-66-6|§66.6]]). The noncompact case, which first makes the embedding proper, was sketched in Lecture 22 and assigned as reading in Lee (Lemma 6.14 and Theorem 6.15, with a figure of the tube construction); the proof above is Lee's, with two facts about manifolds with boundary cited (Proposition [[§66 The Whitney Embedding Theorem#^prop-66-9|§66.9]]).

> [!remark] Remark: The Hard Version
> In the “hard” version the dimensions are one less: an embedding into $\mathbb{R}^{2m}$ and an immersion into $\mathbb{R}^{2m-1}$ (for $m > 1$ in the second; Lee, Theorems 6.19 and 6.20). The course does not discuss it: the proof is very specialized and long. The smaller the codimension, the tighter the fit, and the harder the manifold must be manipulated to fit in.

^rem-66-2

> [!theorem] Corollary §66.12: Every Manifold Has a Morse Function
> Every smooth manifold $M$ admits a Morse function (Definition [[§54 Critical Points and the Hessian#^def-54-4|§54.4]]). If $M$ is compact, nonempty and of dimension $m \ge 1$, such a function has finitely many critical points, and at least two.

^cor-66-12

> [!proof]+ Proof
> *(Not from the assignment; Assignment 6, Problem 5, with the Whitney embedding theorem.)* By Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]] there is an embedding $\Phi : M \to \mathbb{R}^N$ ($N = 2m + 1$); its image $M' = \Phi(M)$ is a regular submanifold and $\Phi : M \to M'$ is a diffeomorphism (Theorem [[§44 Embeddings#^thm-44-1|§44.1]], Corollary [[§44 Embeddings#^cor-44-3|§44.3]]). By Corollary [[§64 Parametric Transversality#^cor-64-8|§64.8]] there is $\mathbf{a}$ with $f_{\mathbf{a}} : M' \to \mathbb{R}$ Morse. Then $f = f_{\mathbf{a}} \circ \Phi$ is Morse: for a chart $(U, \psi)$ of $M'$, $(\Phi^{-1}(U), \psi \circ \Phi)$ is a chart of $M$ ($\psi \circ \Phi$ is a diffeomorphism onto the open set $\psi(U)$, Lemma [[§36 Submersions#^lem-36-5|§36.5]]), in which $f$ has the same coordinate representation $f \circ (\psi \circ \Phi)^{-1} = f_{\mathbf{a}} \circ \psi^{-1}$ as $f_{\mathbf{a}}$ in $\psi$; so $p$ is a critical point of $f$ exactly when $\Phi(p)$ is one of $f_{\mathbf{a}}$, with the same Hessian matrices (Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]]). If $M$ is compact, the critical points of a Morse function are finite in number (Corollary [[§55 Morse Functions and the Zero Section#^cor-55-10|§55.10]]); $f$ attains a maximum and a minimum, both critical points, and they are distinct unless $f$ is constant, which a Morse function on a manifold of dimension $m \ge 1$ is not (every point would be critical, and critical points of a Morse function are isolated, Corollary [[§55 Morse Functions and the Zero Section#^cor-55-9|§55.9]]).

^pf-66-12

*Uses:* [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], [[§44 Embeddings#^thm-44-1|§44.1]], [[§44 Embeddings#^cor-44-3|§44.3]], [[§64 Parametric Transversality#^cor-64-8|§64.8]], [[§36 Submersions#^lem-36-5|§36.5]], [[§54 Critical Points and the Hessian#^def-54-1|Def. §54.1]], [[§55 Morse Functions and the Zero Section#^cor-55-10|§55.10]], [[§55 Morse Functions and the Zero Section#^cor-55-9|§55.9]]
