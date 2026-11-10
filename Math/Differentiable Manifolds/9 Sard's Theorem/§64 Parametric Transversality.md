---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 64
tags: [differentiable-manifolds, math591]
---
← [[§63 Sard's Theorem]] · ↑ [[· 9 Sard's Theorem]] · [[§65 Partitions of Unity]] →

*Stage: analysis — Transversality of a whole family passes, by Sard's theorem, to almost every member.*

*Lecture 20. The transversality theorem of René Thom, or parametric transversality; together with Sard's theorem it has important consequences.*

> [!definition] Definition §64.1: Smooth Family of Maps
> Let $S$, $M$, $N$ be smooth manifolds. A **smooth family** of maps $M \to N$, parametrized by $S$, is a collection $\{F_s\}_{s \in S}$ of maps $F_s : M \to N$ such that $F : S \times M \to N$, $F(s, p) = F_s(p)$, is smooth. $S$ is the **parameter space**.
>
> *Lee: Ch. 6, The Transversality Homotopy Theorem*

^def-64-1

Smoothness of the family means smoothness of the single map $F$, jointly in $s$ and $p$. Each $F_s = F \circ \iota_s$, with $\iota_s : M \to S \times M$, $p \mapsto (s, p)$, the slice inclusion (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-9|§19.9]]), so each $F_s$ is smooth.

> [!theorem] Theorem §64.1: Parametric Transversality
> Let $F : S \times M \to N$ be smooth, $Z \subseteq N$ a regular submanifold, and suppose $F \pitchfork Z$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]). Then $W = F^{-1}(Z)$ is a regular submanifold of $S \times M$, and with $\pi : W \to S$ the restriction of the projection $(s, p) \mapsto s$: for $s \in S$,
>
> $$
> s \text{ is a regular value of } \pi \iff F_s : M \to N \text{ is transverse to } Z .
> $$
>
> *Lee: Theorem 6.35 (proof)*

^thm-64-1

> [!proof]+ Proof
> *(Lecture 20 proved the direction that matters for applications, $(\Rightarrow)$, and left the converse as an exercise; the converse is filled in.)*
>
> *Preliminaries.* $W$ is a regular submanifold of $S \times M$ and, for $(s, p) \in W$ with $q = F(s, p)$,
>
> $$
> T_{(s,p)}W = \big(dF_{(s,p)}\big)^{-1}\big(T_qZ\big) \tag{1}
> $$
>
> (Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]]): the preimage of the tangent space of $Z$ under the differential. $\pi$ is smooth, as the restriction of the smooth projection to a regular submanifold. Write tangent vectors to $S \times M$ as pairs $(\sigma, u) \in T_sS \oplus T_pM$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]]); then $d\pi(\sigma, u) = \sigma$, and
>
> $$
> dF_{(s,p)}(0, u) = d(F_s)_p(u), \tag{2}
> $$
>
> because $F_s = F \circ \iota_s$ and $d(\iota_s)_p(u) = (0, u)$: it is a partial derivative, computed with the first entry frozen at $s$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|§31.4]]).
>
> *$(\Rightarrow)$* Let $s$ be a regular value of $\pi$, and $p \in M$ with $q = F_s(p) = F(s,p) \in Z$. We must show $\operatorname{Im} d(F_s)_p + T_qZ = T_qN$; the inclusion $\subseteq$ is clear. Let $w \in T_qN$. Since $F \pitchfork Z$, there are $(\sigma, u) \in T_{(s,p)}(S \times M)$ and $v \in T_qZ$ with
>
> $$
> w = dF_{(s,p)}(\sigma, u) + v . \tag{$\ast$}
> $$
>
> Since $s$ is a regular value of $\pi$, $\sigma$ is in the image of $d\pi_{(s,p)}$: there is a tangent vector to $W$ at $(s, p)$ projecting to $\sigma$, and since $d\pi$ only reads the first component, it has the form $(\sigma, \tau)$ for some $\tau \in T_pM$. Write $(\sigma, u) = (\sigma, \tau) + (0, u - \tau)$ and substitute into $(\ast)$:
>
> $$
> w = dF_{(s,p)}(\sigma, \tau) + dF_{(s,p)}(0, u - \tau) + v = d(F_s)_p(u - \tau) + \big(dF_{(s,p)}(\sigma, \tau) + v\big),
> $$
>
> by (2). By (1), $dF_{(s,p)}(\sigma, \tau) \in T_qZ$, so the bracket is tangent to $Z$, and $w \in \operatorname{Im} d(F_s)_p + T_qZ$. So $F_s$ intersects $Z$ transversely.
>
> *$(\Leftarrow)$* *(Filled in.)* Suppose $F_s \pitchfork Z$, and let $(s, p) \in \pi^{-1}(s)$, so $q = F_s(p) \in Z$; we show $d\pi_{(s,p)}$ is onto $T_sS$. Let $\sigma \in T_sS$. By transversality of $F_s$, $dF_{(s,p)}(\sigma, 0) = d(F_s)_p(u) + v$ for some $u \in T_pM$, $v \in T_qZ$. By (2), $dF_{(s,p)}(\sigma, -u) = dF_{(s,p)}(\sigma, 0) - d(F_s)_p(u) = v \in T_qZ$, so $(\sigma, -u) \in T_{(s,p)}W$ by (1), and $d\pi(\sigma, -u) = \sigma$.

^pf-64-1

*Uses:* [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|Def. §31.4]]

![[m591-60-1.svg]]

The cartoon, in $S \times M$ with $S$ horizontal. $W = F^{-1}(Z)$ is the orange curve and $\pi$ projects it to $S$. At $s$ the slice $\{s\} \times M$ crosses $W$ transversally: $s$ is a regular value of $\pi$, and $F_s \pitchfork Z$. At $s'$ the slice is tangent to $W$: $s'$ is a singular value, and $F_{s'}$ need not be transverse to $Z$. At $s''$ the slice misses $W$: $F_{s''}(M) \cap Z = \varnothing$, vacuously transverse.

![[m591-60-3.svg]]

*(Not from lecture; figure added.)* An explicit instance of the cartoon. Take $S = M = \mathbb{R}$, $N = \mathbb{R}^2$, $Z = \{ y = x^2 \}$ and $F(s, x) = (x, s)$, so $F_s$ parametrizes the horizontal line at height $s$. Then $F$ is a diffeomorphism, so $F \pitchfork Z$, and $W = F^{-1}(Z) = \{ (s, x) : s = x^2 \}$. Parametrizing $W$ by $x \mapsto (x^2, x)$, the projection is $\pi(x^2, x) = x^2$, with derivative $2x$: the only critical point is $x = 0$, and the only critical value is $s = 0$. For $s > 0$, $F_s$ crosses $Z$ transversally at $x = \pm\sqrt{s}$; for $s < 0$, $F_s^{-1}(Z) = \varnothing$; at $s = 0$, $\operatorname{Im} d(F_0)_0 = \operatorname{span}\{(1, 0)\} = T_{(0,0)}Z$, so $F_0$ is tangent to $Z$, not transverse — exactly as Theorem [[§64 Parametric Transversality#^thm-64-1|§64.1]] predicts.

> [!theorem] Corollary §64.2: Almost Every Member Is Transverse
> If $F : S \times M \to N$ is smooth and $F \pitchfork Z$, then $F_s \pitchfork Z$ for almost every $s \in S$: the set of $s$ with $F_s$ not transverse to $Z$ has measure zero in $S$.
>
> *Lee: Theorem 6.35*

^cor-64-2

> [!proof]+ Proof
> *(Lecture 20.)* By Sard's theorem (Theorem [[§63 Sard's Theorem#^thm-63-3|§63.3]]) applied to $\pi : W \to S$, the singular values of $\pi$ form a set of measure zero; for every other $s$, $F_s \pitchfork Z$ by Theorem [[§64 Parametric Transversality#^thm-64-1|§64.1]].

^pf-64-2

*Uses:* [[§63 Sard's Theorem#^thm-63-3|§63.3]], [[§64 Parametric Transversality#^thm-64-1|§64.1]]

The corollary passes from transversality of the family to transversality of the individual members of the family.

> [!example] Example §64.1: Translates Are Generically Transverse
> Let $Y, Z \subseteq \mathbb{R}^d$ be regular submanifolds. For almost every $a \in \mathbb{R}^d$, the translate $a + Y$ intersects $Z$ transversally.

^ex-64-1

> [!proof]+ Proof
> *(Lecture 20, the first classical geometric application; details filled in.)* The parameter space is $\mathbb{R}^d$ itself: $F : \mathbb{R}^d \times Y \to \mathbb{R}^d$, $F(a, p) = a + p$, using the vector space structure to translate. Then $F_a(Y) = a + Y$. *$F$ is a submersion*: fixing $p$ and varying $a$, $dF_{(a,p)}(\sigma, 0) = \sigma$ for every $\sigma \in T_a\mathbb{R}^d = \mathbb{R}^d$. So $F \pitchfork Z$ (Corollary [[§39 Transversality and Lagrange Multipliers#^cor-39-5|§39.5]](3)), and $F^{-1}(Z) = \{ (a, p) : a + p \in Z \}$. By Corollary [[§64 Parametric Transversality#^cor-64-2|§64.2]], $F_a \pitchfork Z$ for almost every $a$. Finally $F_a : Y \to \mathbb{R}^d$ is the inclusion of $a + Y$ composed with the diffeomorphism $Y \to a + Y$, $p \mapsto a + p$, and $a + Y$ is a regular submanifold, a translate of one, so $F_a \pitchfork Z$ says $(a + Y) \pitchfork Z$ (Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]]).

^pf-ex-64-1

*Uses:* [[§39 Transversality and Lagrange Multipliers#^cor-39-5|§39.5]], [[§64 Parametric Transversality#^cor-64-2|§64.2]], [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]]

> [!theorem] Corollary §64.3: Transverse Submanifolds of Small Total Dimension Are Disjoint
> Let $Y, Z \subseteq \mathbb{R}^d$ be regular submanifolds with $\dim Y + \dim Z < d$.
>
> 1. If $Y \pitchfork Z$, then $Y \cap Z = \varnothing$: a transverse intersection must be empty.
> 2. For almost every $a \in \mathbb{R}^d$, the translate $a + Y$ is disjoint from $Z$.

^cor-64-3

> [!proof]+ Proof
> *(The reason is the one given with the statement in the notes, “since $T_qY + T_qZ$ has dimension at most $\dim Y + \dim Z$”; details filled in.)*
>
> *(1)* We show that $Y \cap Z$ has no point. Suppose $q \in Y \cap Z$. Since $Y \pitchfork Z$, $T_qY + T_qZ = T_q\mathbb{R}^d$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-3|§39.3]]), a vector space of dimension $d$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-10|§29.10]]). On the other hand $T_qY$ has a basis of $\dim Y$ vectors and $T_qZ$ a basis of $\dim Z$ vectors (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-10|§29.10]]), and the two bases together span $T_qY + T_qZ$; so $T_qY + T_qZ$ has dimension at most $\dim Y + \dim Z < d$. This is a contradiction, so $Y \cap Z = \varnothing$.
>
> *(2)* By Example [[§64 Parametric Transversality#^ex-64-1|§64.1]], $(a + Y) \pitchfork Z$ for almost every $a \in \mathbb{R}^d$. For each $a$, $a + Y$ is a regular submanifold of $\mathbb{R}^d$ diffeomorphic to $Y$ by $p \mapsto a + p$ (as in the proof of Example [[§64 Parametric Transversality#^ex-64-1|§64.1]]), so $\dim(a + Y) + \dim Z = \dim Y + \dim Z < d$. By (1), applied to $a + Y$ and $Z$, $(a + Y) \cap Z = \varnothing$ for every $a$ with $(a + Y) \pitchfork Z$, that is, for almost every $a$.

^pf-64-3

*Uses:* [[§39 Transversality and Lagrange Multipliers#^def-39-3|Def. §39.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-10|§29.10]], [[§64 Parametric Transversality#^ex-64-1|Ex. §64.1]]

> [!example] Example §64.2: Two Curves in Space
> Two curves in $\mathbb{R}^3$ ($1 + 1 < 3$): translating one by a generic vector makes it disjoint from the other (Corollary [[§64 Parametric Transversality#^cor-64-3|§64.3]](2)).

^ex-64-2

For two curves in the plane that are tangent, a generic translate either separates them or makes them cross transversally. This is the idea of *general position*: a configuration is not in general position if moving one of the objects a little changes the geometry radically. Objects in general position are transverse, which may mean that they do not intersect; an empty intersection is still a meaningful, and often powerful, statement.

![[m591-60-2.svg]]

The lecture's picture: $Z$ (blue) and $Y$ (red) tangent at a point, not transverse; a translate $a + Y$ meeting $Z$ in two transverse crossings; another translate $a' + Y$ disjoint from $Z$. Only translates making them tangent again are excluded, and those form a set of measure zero.

![[m591-60-a1.gif|420]]

*(Not from lecture; animation added, vault only.)* $Y$ a circle and $Z$ the graph of $\sin$ (chosen for the picture); the translate $a + Y$ moves vertically, $a = (0.9, s)$. The number of crossings changes only at $s = 0.098$ and $s = 1.404$ (computed), where $a + Y$ is tangent to $Z$ (orange); every other translate meets $Z$ transversally, in $0$ or $2$ points.

A further application, Assignment 6, Problem 5 ([[§64 Parametric Transversality#Height Functions Are Almost Always Morse|§64, Height Functions Are Almost Always Morse]]): for a submanifold of Euclidean space, almost all linear functions restricted to the submanifold are Morse (Definition [[§54 Critical Points and the Hessian#^def-54-4|§54.4]]), so Morse functions are plentiful.

**Transcription note (Lecture 20).** Page 54 of the handwritten notes writes “$\pi$ onto” under $F^{-1}(Z) \to \mathbb{R}^d$. This does not hold in general: $(a, p) \in F^{-1}(Z)$ exactly when $a + p \in Z$, so the image of $\pi$ is $\{ z - p : z \in Z,\ p \in Y \}$, the set of $a$ for which $a + Y$ meets $Z$ (a single point when $Y$ and $Z$ are points). Surjectivity plays no role in the argument.

## Height Functions Are Almost Always Morse

*Assignment 6, Problem 5: the homework announced in Lecture 20. Not from lecture; the submitted solution, with the bundle facts it uses filled in ([[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]]) and its main implication completed to an equivalence.*

*Setting.* Throughout this subsection $M \subseteq \mathbb{R}^N$ is a regular submanifold of dimension $m < N$, with the geometric tangent spaces $T^{\mathrm{geo}}_pM$, written $T_pM$ (the Setting of [[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]] with $n = N$); $T^{\mathrm{geo}}M$ is its tangent bundle with zero section $\mathcal{Z}$ and $\pi_p : \mathbb{R}^N \to T_pM$ the orthogonal projection (Definitions [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-5|§42.5]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-6|§42.6]] and [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-8|§42.8]], Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]]). Points of the parameter space $\mathbb{R}^N$ are written $\mathbf{a}, \mathbf{b}$. From Proposition [[§64 Parametric Transversality#^prop-64-6|§64.6]] on, $S$ denotes $F^{-1}(\mathcal{Z})$, as in the assignment: it plays the role of the $W$ of Theorem [[§64 Parametric Transversality#^thm-64-1|§64.1]], not of the parameter space $S$ there, which here is $\mathbb{R}^N$. (If $m = N$, $M$ is open in $\mathbb{R}^N$ and the functions below have no critical points unless $\mathbf{a} = 0$.)

> [!theorem] Lemma §64.4: The Zero Section and the Splitting Along It
> 1. The zero section $\zeta : M \to T^{\mathrm{geo}}M$, $\zeta(p) = (p, 0)$, is smooth, and $\mathcal{Z} = \zeta(M)$ is a closed regular submanifold of $T^{\mathrm{geo}}M$ of dimension $m$.
> 2. For $p \in M$, with tangent spaces of the submanifolds $\mathcal{Z} \subseteq T^{\mathrm{geo}}M \subseteq \mathbb{R}^{2N}$ taken geometrically,
>
> $$
> T_{(p,0)}\mathcal{Z} = \{(u, 0) : u \in T_pM\}, \qquad V = \{(0, w) : w \in T_pM\}, \qquad T_{(p,0)}T^{\mathrm{geo}}M = T_{(p,0)}\mathcal{Z} \oplus V = T_pM \times T_pM .
> $$

^lem-64-4

> [!proof]+ Proof
> *(1)* *(Filled in.)* The projection $\pi(q, v) = q$ is the restriction to $T^{\mathrm{geo}}M$ of a linear map, smooth by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1); $\zeta$ is smooth into $\mathbb{R}^{2N}$ and lands in the regular submanifold $T^{\mathrm{geo}}M$ (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-4|§42.4]]), so it is smooth into it (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)). As $\pi \circ \zeta = \mathrm{id}_M$, Proposition [[§44 Embeddings#^prop-44-11|§44.11]] makes $\zeta$ an embedding with closed image, a closed regular submanifold of dimension $m$.
>
> *(2)* *(Assignment 6, Problem 5(a); the submitted solution.)* If $\gamma$ is a curve in $M$ with $\gamma(0) = p$ and $\gamma'(0) = u$, then $t \mapsto (\gamma(t), 0)$ is a curve in $\mathcal{Z}$ with velocity $(u, 0)$ at $t = 0$; so $\{(u, 0) : u \in T_pM\} \subseteq T_{(p,0)}\mathcal{Z}$, with equality since both have dimension $m$ (by (1) and Corollary [[§25 The Geometric Tangent Space#^cor-25-7|§25.7]]). For $w \in T_pM$, $t \mapsto (p, tw)$ is a curve in $T^{\mathrm{geo}}M$ with velocity $(0, w)$ at $t = 0$, so $V \subseteq T_{(p,0)}T^{\mathrm{geo}}M$. Both $T_{(p,0)}\mathcal{Z}$ and $V$ are $m$-dimensional, and $T_{(p,0)}\mathcal{Z} \cap V = \{0\}$, since $(u, 0) = (0, w)$ forces $u = w = 0$. Hence $T_{(p,0)}\mathcal{Z} + V$ is a $2m$-dimensional subspace of the $2m$-dimensional space $T_{(p,0)}T^{\mathrm{geo}}M$ (Proposition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-4|§42.4]]), so they are equal.

^pf-64-4

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-4|§42.4]], [[§44 Embeddings#^prop-44-11|§44.11]], [[§25 The Geometric Tangent Space#^cor-25-7|§25.7]]

This is the splitting of Proposition [[§55 Morse Functions and the Zero Section#^prop-55-6|§55.6]] for $T^{\ast}M$, seen inside $\mathbb{R}^{2N}$: horizontal (along the zero section) plus vertical (along the fibre).

> [!definition] Definition §64.2: Height Function
> For $\mathbf{a} \in \mathbb{R}^N$, the **height function** in the direction $\mathbf{a}$ is $f_{\mathbf{a}} : M \to \mathbb{R}$, $f_{\mathbf{a}}(p) = p \cdot \mathbf{a}$, the restriction to $M$ of a linear function.

^def-64-2

> [!theorem] Lemma §64.5: Critical Points of a Height Function
> For $p \in M$ and $w \in T_pM$, $d(f_{\mathbf{a}})_p(w) = w \cdot \mathbf{a} = w \cdot \pi_p(\mathbf{a})$. Hence
>
> $$
> p \in \operatorname{Crit}(f_{\mathbf{a}}) \iff \mathbf{a} \perp T_pM \iff \pi_p(\mathbf{a}) = 0 .
> $$

^lem-64-5

> [!proof]+ Proof
> *(Assignment 6, Problem 5(b); the submitted solution.)* $f_{\mathbf{a}}$ is the restriction to $M$ of the linear function $y \mapsto y \cdot \mathbf{a}$, so along a curve $\gamma$ in $M$ with $\gamma(0) = p$, $\gamma'(0) = w$, $d(f_{\mathbf{a}})_p(w) = \frac{d}{dt}\big|_{t=0}\, \gamma(t) \cdot \mathbf{a} = w \cdot \mathbf{a}$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). Since $w \cdot \mathbf{a} = w \cdot \pi_p(\mathbf{a})$ for $w \in T_pM$ (Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]](1)), this is the identification $T_pM \cong T_p^{\ast}M$ by the inner product: $d(f_{\mathbf{a}})_p$ corresponds to $\pi_p(\mathbf{a})$. So $d(f_{\mathbf{a}})_p = 0$ if and only if $\mathbf{a} \perp T_pM$, if and only if $\pi_p(\mathbf{a}) = 0$ (Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]](1)).

^pf-64-5

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]]

So $\pi_p(\mathbf{a})$ is the gradient of $f_{\mathbf{a}}$ at $p$, and the family of gradients is the map of the next proposition.

> [!theorem] Proposition §64.6: The Gradient Family Is Transverse to the Zero Section
> Let $F : \mathbb{R}^N \times M \to T^{\mathrm{geo}}M$, $F(\mathbf{a}, p) = (p, \pi_p(\mathbf{a}))$. Then $F$ is smooth, $F \pitchfork \mathcal{Z}$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]), and
>
> $$
> S = F^{-1}(\mathcal{Z}) = \{(\mathbf{a}, p) \in \mathbb{R}^N \times M : \mathbf{a} \perp T_pM\}
> $$
>
> is a regular submanifold of $\mathbb{R}^N \times M$ of dimension $N$: the normal bundle $\mathcal{N}$ of $M$ (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-2|§42.2]]) with the two factors written in the opposite order. For $(\mathbf{a}, p) \in S$ and $\mathbf{b} \in \mathbb{R}^N$,
>
> $$
> dF_{(\mathbf{a},p)}(\mathbf{b}, 0) = \big(0,\ \pi_p(\mathbf{b})\big) .
> $$

^prop-64-6

> [!proof]+ Proof
> *(Assignment 6, Problem 5(a); the submitted solution. Smoothness, not asked for, is Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]](3).)* *$F^{-1}(\mathcal{Z})$.* The zero section is $\mathcal{Z} = \{(p, 0) : p \in M\}$, so
>
> $$
> F^{-1}(\mathcal{Z}) = \{(\mathbf{a}, p) \in \mathbb{R}^N \times M : \pi_p(\mathbf{a}) = 0\} = \{(\mathbf{a}, p) : p \in M,\ \mathbf{a} \in (T_pM)^\perp\}
> $$
>
> by Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]](1). This is the normal bundle $\mathcal{N} = \{(p, v) : p \in M,\ v \perp T_pM\}$ of $M$, with the two factors written in the opposite order.
>
> *$F \pitchfork \mathcal{Z}$.* Let $(\mathbf{a}, p) \in F^{-1}(\mathcal{Z})$, so $F(\mathbf{a}, p) = (p, 0)$. We must show $\operatorname{Im} dF_{(\mathbf{a}, p)} + T_{(p,0)}\mathcal{Z} = T_{(p,0)}T^{\mathrm{geo}}M$. By Lemma [[§64 Parametric Transversality#^lem-64-4|§64.4]](2), it suffices to show $V \subseteq \operatorname{Im} dF_{(\mathbf{a}, p)}$. For $\mathbf{b} \in \mathbb{R}^N$, the curve $t \mapsto (\mathbf{a} + t\mathbf{b}, p)$ in $\mathbb{R}^N \times M$ has velocity $(\mathbf{b}, 0)$ at $t = 0$, and by linearity of $\pi_p$, $F(\mathbf{a} + t\mathbf{b}, p) = \big(p,\ \pi_p(\mathbf{a}) + t\,\pi_p(\mathbf{b})\big)$, so
>
> $$
> dF_{(\mathbf{a}, p)}(\mathbf{b}, 0) = \frac{d}{dt}\Big|_{t=0} F(\mathbf{a} + t\mathbf{b}, p) = \big(0,\ \pi_p(\mathbf{b})\big).
> $$
>
> Given $w \in T_pM$, take $\mathbf{b} = w$; since $\pi_p(w) = w$, this gives $(0, w) = dF_{(\mathbf{a},p)}(w, 0) \in \operatorname{Im} dF_{(\mathbf{a}, p)}$. Hence $V \subseteq \operatorname{Im} dF_{(\mathbf{a}, p)}$, and
>
> $$
> \operatorname{Im} dF_{(\mathbf{a}, p)} + T_{(p,0)}\mathcal{Z} \supseteq V + T_{(p,0)}\mathcal{Z} = T_{(p,0)}T^{\mathrm{geo}}M.
> $$
>
> In block form with respect to $\mathbb{R}^N \oplus T_pM$ and $T_{(p,0)}T^{\mathrm{geo}}M = T_pM \oplus T_pM$ (horizontal $\oplus$ vertical),
>
> $$
> dF_{(\mathbf{a}, p)} = \begin{pmatrix} 0 & I_m \\ \pi_p & \ast \end{pmatrix},
> $$
>
> and the first column alone, together with $T_{(p,0)}\mathcal{Z}$, spans $T_{(p,0)}T^{\mathrm{geo}}M$. Therefore $F \pitchfork \mathcal{Z}$.
>
> *The manifold $S$.* By Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], applied to $F$ and the submanifold $\mathcal{Z}$ of codimension $2m - m = m$ in $T^{\mathrm{geo}}M$ (Lemma [[§64 Parametric Transversality#^lem-64-4|§64.4]](1)), $S$ is a regular submanifold of $\mathbb{R}^N \times M$ of codimension $m$, so $\dim S = N + m - m = N$, and $T_{(\mathbf{a},p)}S = \{(\mathbf{b}, u) \in \mathbb{R}^N \oplus T_pM : dF_{(\mathbf{a},p)}(\mathbf{b}, u) \in T_{(p,0)}\mathcal{Z}\}$.

^pf-64-6

*Uses:* [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]], [[§64 Parametric Transversality#^lem-64-4|§64.4]], [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]]

> [!theorem] Proposition §64.7: The Hessian of a Height Function
> Let $(\mathbf{a}, p) \in S$, that is, $p \in \operatorname{Crit}(f_{\mathbf{a}})$, and $F_{\mathbf{a}} = F(\mathbf{a}, \cdot) : M \to T^{\mathrm{geo}}M$, $F_{\mathbf{a}}(q) = (q, \pi_q(\mathbf{a}))$. Then
>
> $$
> d(F_{\mathbf{a}})_p(u) = (u, A_pu), \qquad A_pu = \frac{d}{dt}\Big|_{t=0}\pi_{\gamma(t)}(\mathbf{a}) \quad (\gamma(0) = p,\ \gamma'(0) = u),
> $$
>
> for a linear map $A_p : T_pM \to T_pM$. In an adapted chart as in the Setting of [[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]], the matrix of $A_p$ in the basis $X_1(p), \ldots, X_m(p)$ is $g(p)^{-1}H_p$, where $g$ is the Gram matrix (Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]]) and $H_p$ the Hessian matrix of $f_{\mathbf{a}}$ in the chart $(x^1, \ldots, x^m)$ of $M$ (Definition [[§54 Critical Points and the Hessian#^def-54-1|§54.1]]). So $A_p$ is invertible if and only if $p$ is a nondegenerate critical point of $f_{\mathbf{a}}$.

^prop-64-7

> [!proof]+ Proof
> *(Assignment 6, Problem 5(b); the submitted solution.)* *The vertical derivative.* For $u \in T_pM$ and a curve $\gamma$ in $M$ with $\gamma(0) = p$, $\gamma'(0) = u$,
>
> $$
> d(F_{\mathbf{a}})_p(u) = \frac{d}{dt}\Big|_{t=0}\big(\gamma(t), \pi_{\gamma(t)}(\mathbf{a})\big) = (u, A_pu), \qquad A_pu = \frac{d}{dt}\Big|_{t=0}\pi_{\gamma(t)}(\mathbf{a}).
> $$
>
> Since $T_{(p,0)}T^{\mathrm{geo}}M = \{(u, w) : u, w \in T_pM\}$ (Lemma [[§64 Parametric Transversality#^lem-64-4|§64.4]](2)), $A_pu \in T_pM$, and $A_p$ is linear since $d(F_{\mathbf{a}})_p$ is. In block form, $d(F_{\mathbf{a}})_p = \begin{pmatrix} I_m \\ A_p \end{pmatrix}$.
>
> *$A_p$ in coordinates.* Restricted to $U \cap M$, the first $m$ coordinates $(x^1, \ldots, x^m)$ of the adapted chart form a chart of $M$, whose coordinate vectors at $q \in U \cap M$ are the $X_j(q) = \partial_j(q) \in T_qM \subseteq \mathbb{R}^N$. By Lemma [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]](2), $\pi_q(\mathbf{a}) = \sum_{i,j} g^{ij}(q)\,\big(\mathbf{a} \cdot \partial_j(q)\big)\,\partial_i(q)$, and $\frac{\partial f_{\mathbf{a}}}{\partial x^j}(q) = \partial_j(q) \cdot \mathbf{a}$ (Lemma [[§64 Parametric Transversality#^lem-64-5|§64.5]] with $w = \partial_j(q)$). Since $p$ is a critical point, $\mathbf{a} \cdot \partial_j(p) = 0$ for all $j$. Differentiating $\pi_q(\mathbf{a})$ in the direction $\partial_k$ at $q = p$ by the product rule, every term in which the derivative does not fall on $\mathbf{a} \cdot \partial_j(q)$ contains the factor $\mathbf{a} \cdot \partial_j(p) = 0$, so
>
> $$
> A_p(\partial_k(p)) = \sum_{i,j} g^{ij}(p)\, \frac{\partial^2 f_{\mathbf{a}}}{\partial x^k \partial x^j}(p)\, \partial_i(p).
> $$
>
> Thus the matrix of $A_p$ in the basis $(\partial_i(p))$ is $g(p)^{-1}H_p$. As $g(p)$ is invertible, $A_p$ is invertible if and only if $\det H_p \neq 0$, that is (Proposition [[§54 Critical Points and the Hessian#^prop-54-4|§54.4]](2)), if and only if $p$ is nondegenerate.

^pf-64-7

*Uses:* [[§64 Parametric Transversality#^lem-64-4|§64.4]], [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^lem-42-6|§42.6]], [[§64 Parametric Transversality#^lem-64-5|§64.5]], [[§54 Critical Points and the Hessian#^def-54-3|Def. §54.3]], [[§54 Critical Points and the Hessian#^prop-54-4|§54.4]]

> [!theorem] Theorem §64.8: Height Functions and Regular Values
> Let $\pi : S \to \mathbb{R}^N$, $\pi(\mathbf{a}, p) = \mathbf{a}$, be the projection of the manifold $S$ of Proposition [[§64 Parametric Transversality#^prop-64-6|§64.6]] onto the parameter (not to be confused with the orthogonal projections $\pi_p$). Then $\pi^{-1}(\mathbf{a}) = \{\mathbf{a}\} \times \operatorname{Crit}(f_{\mathbf{a}})$, and
>
> $$
> \mathbf{a} \text{ is a regular value of } \pi \iff f_{\mathbf{a}} \text{ is a Morse function.}
> $$

^thm-64-8

> [!proof]+ Proof
> *(Assignment 6, Problem 5(b): the direction $(\Rightarrow)$ is the submitted solution; $(\Leftarrow)$ is filled in.)* By Lemma [[§64 Parametric Transversality#^lem-64-5|§64.5]], $(\mathbf{a}, p) \in S$ if and only if $p \in \operatorname{Crit}(f_{\mathbf{a}})$, so $\pi^{-1}(\mathbf{a}) = \{\mathbf{a}\} \times \operatorname{Crit}(f_{\mathbf{a}})$. Since $\pi$ is the restriction of the linear projection $(\mathbf{a}, p) \mapsto \mathbf{a}$, $\pi_{\ast(\mathbf{a},p)}(\mathbf{b}, u) = \mathbf{b}$.
>
> *The tangent space of $S$.* Let $(\mathbf{a}, p) \in S$. Since $F(\mathbf{a}, q) = F_{\mathbf{a}}(q)$, the chain rule gives $dF_{(\mathbf{a},p)}(0, u) = d(F_{\mathbf{a}})_p(u) = (u, A_pu)$ (Proposition [[§64 Parametric Transversality#^prop-64-7|§64.7]]), and with Proposition [[§64 Parametric Transversality#^prop-64-6|§64.6]], by linearity,
>
> $$
> dF_{(\mathbf{a},p)}(\mathbf{b}, u) = \big(u,\ \pi_p(\mathbf{b}) + A_pu\big) .
> $$
>
> As $T_{(p,0)}\mathcal{Z} = \{(u', 0) : u' \in T_pM\}$, Proposition [[§64 Parametric Transversality#^prop-64-6|§64.6]] gives
>
> $$
> T_{(\mathbf{a},p)}S = \{(\mathbf{b}, u) : \pi_p(\mathbf{b}) + A_pu = 0\}, \qquad \ker \pi_{\ast(\mathbf{a},p)} = \{(0, u) : u \in T_pM,\ A_pu = 0\}.
> $$
>
> *$(\Rightarrow)$ Regular values give Morse functions.* Suppose $\mathbf{a}$ is a regular value of $\pi$, and let $p$ be a critical point of $f_{\mathbf{a}}$, so $(\mathbf{a}, p) \in \pi^{-1}(\mathbf{a})$. Then $\pi_{\ast(\mathbf{a},p)} : T_{(\mathbf{a},p)}S \to \mathbb{R}^N$ is surjective, and since $\dim T_{(\mathbf{a},p)}S = N$, it is also injective. By the kernel computation, $A_pu = 0$ implies $u = 0$, so $A_p$ is injective, hence invertible, and $p$ is nondegenerate (Proposition [[§64 Parametric Transversality#^prop-64-7|§64.7]]). Since $p$ was an arbitrary critical point, $f_{\mathbf{a}}$ is Morse.
>
> *$(\Leftarrow)$* Suppose $f_{\mathbf{a}}$ is Morse, and let $(\mathbf{a}, p) \in \pi^{-1}(\mathbf{a})$. Then $p$ is a nondegenerate critical point, so $A_p$ is invertible (Proposition [[§64 Parametric Transversality#^prop-64-7|§64.7]]). Given $\mathbf{b} \in \mathbb{R}^N$, put $u = -A_p^{-1}\pi_p(\mathbf{b}) \in T_pM$; then $(\mathbf{b}, u) \in T_{(\mathbf{a},p)}S$ and $\pi_{\ast(\mathbf{a},p)}(\mathbf{b}, u) = \mathbf{b}$. So $\pi_{\ast(\mathbf{a},p)}$ is onto at every point of $\pi^{-1}(\mathbf{a})$: $\mathbf{a}$ is a regular value.

^pf-64-8

*Uses:* [[§64 Parametric Transversality#^lem-64-5|§64.5]], [[§64 Parametric Transversality#^prop-64-7|§64.7]], [[§64 Parametric Transversality#^prop-64-6|§64.6]]

The image of $\pi_{\ast(\mathbf{a},p)}$ is $\{\mathbf{b} : \pi_p(\mathbf{b}) \in \operatorname{Im} A_p\}$; the theorem says this is all of $\mathbb{R}^N$ exactly when $A_p$ is onto.

> [!theorem] Corollary §64.9: Almost Every Height Function Is Morse
> For almost every $\mathbf{a} \in \mathbb{R}^N$ (all $\mathbf{a}$ outside a set of measure zero), $f_{\mathbf{a}} : M \to \mathbb{R}$ is a Morse function.

^cor-64-9

> [!proof]+ Proof
> *(Assignment 6, Problem 5(b); the submitted solution.)* By Sard's theorem (Theorem [[§63 Sard's Theorem#^thm-63-3|§63.3]]) applied to the smooth map $\pi : S \to \mathbb{R}^N$, the set of critical values of $\pi$ has measure zero in $\mathbb{R}^N$. Hence almost every $\mathbf{a} \in \mathbb{R}^N$ is a regular value of $\pi$, and for all such $\mathbf{a}$, $f_{\mathbf{a}}$ is a Morse function (Theorem [[§64 Parametric Transversality#^thm-64-8|§64.8]]).

^pf-64-9

*Uses:* [[§63 Sard's Theorem#^thm-63-3|§63.3]], [[§64 Parametric Transversality#^thm-64-8|§64.8]]

> [!proof]+ Second proof
> *(Not from the assignment: the problem as an instance of Corollary [[§64 Parametric Transversality#^cor-64-2|§64.2]].)* $F$ is a smooth family of maps $F_{\mathbf{a}} : M \to T^{\mathrm{geo}}M$ parametrized by $\mathbb{R}^N$ (Definition [[§64 Parametric Transversality#^def-64-1|§64.1]]), and $F \pitchfork \mathcal{Z}$ (Proposition [[§64 Parametric Transversality#^prop-64-6|§64.6]]); so $F_{\mathbf{a}} \pitchfork \mathcal{Z}$ for almost every $\mathbf{a}$. At $p \in F_{\mathbf{a}}^{-1}(\mathcal{Z}) = \operatorname{Crit}(f_{\mathbf{a}})$, by Proposition [[§64 Parametric Transversality#^prop-64-7|§64.7]] and Lemma [[§64 Parametric Transversality#^lem-64-4|§64.4]](2),
>
> $$
> \operatorname{Im} d(F_{\mathbf{a}})_p + T_{(p,0)}\mathcal{Z} = \{(u, A_pu)\} + \{(u', 0)\} = T_pM \times \operatorname{Im} A_p ,
> $$
>
> which is all of $T_{(p,0)}T^{\mathrm{geo}}M = T_pM \times T_pM$ if and only if $A_p$ is onto, that is, $p$ is nondegenerate. So $F_{\mathbf{a}} \pitchfork \mathcal{Z}$ exactly when $f_{\mathbf{a}}$ is Morse, and the claim follows. Under the identification $T^{\mathrm{geo}}M \cong T^{\ast}M$ of the hint (“one can identify $TM \cong T^{\ast}M$ using the inner product”), $F_{\mathbf{a}}$ is the section $s_{f_{\mathbf{a}}} : p \mapsto (p, d(f_{\mathbf{a}})_p)$, and this equivalence is Theorem [[§55 Morse Functions and the Zero Section#^thm-55-8|§55.8]].

^pf-64-9-2

*Uses:* [[§64 Parametric Transversality#^cor-64-2|§64.2]], [[§64 Parametric Transversality#^def-64-1|Def. §64.1]], [[§64 Parametric Transversality#^prop-64-6|§64.6]], [[§64 Parametric Transversality#^prop-64-7|§64.7]], [[§64 Parametric Transversality#^lem-64-4|§64.4]], [[§55 Morse Functions and the Zero Section#^thm-55-8|§55.8]]

![[m591-60-a2.gif|620]]

*(Not from lecture; animation added, vault only.)* A height function (Definition [[§64 Parametric Transversality#^def-64-2|§64.2]]) on a torus standing in $\mathbb{R}^3$, parametrized by $(u, v) \mapsto \big((2 + 0.8\cos v)\cos u,\ 0.8\sin v,\ (2 + 0.8\cos v)\sin u\big)$, in the direction $\mathbf{a} = e_3$ (chosen for the picture): $f_{\mathbf{a}} = (2 + 0.8\cos v)\sin u$. The level $c$ rises; red is the level set $f_{\mathbf{a}}^{-1}(c)$, blue the part of the torus below it. There are four critical points, the points where $\mathbf{a} \perp T_pM$ (Lemma [[§64 Parametric Transversality#^lem-64-5|§64.5]]), with critical values $\mp 2.8$ and $\mp 1.2$. All four are nondegenerate, of Morse index $0, 1, 1, 2$ (Definition [[§54 Critical Points and the Hessian#^def-54-5|§54.5]]), so this $f_{\mathbf{a}}$ is a Morse function. At a regular value the level set is one or two circles; at the two critical values of index $1$ it is a figure eight, and at the minimum and the maximum it is a point.

![[m591-60-a3.gif|620]]

*(Not from lecture; animation added, vault only.)* The same torus while the direction tilts, $\mathbf{a} = (0, \sin\theta, \cos\theta)$, from $\theta = 12^\circ$ to $90^\circ$, where $\mathbf{a}$ is the axis of the torus. For $\theta < 90^\circ$ there are four critical points, at $(u, v) = (\tfrac{\pi}{2}, \theta)$, $(\tfrac{\pi}{2}, \theta - \pi)$, $(-\tfrac{\pi}{2}, \pi - \theta)$, $(-\tfrac{\pi}{2}, -\theta)$, all nondegenerate: there $\partial^2 f_{\mathbf{a}}/\partial u\,\partial v = 0$, $\partial^2 f_{\mathbf{a}}/\partial v^2 = \pm 0.8$ and $\partial^2 f_{\mathbf{a}}/\partial u^2 = \pm\cos\theta\,(2 \pm 0.8\cos\theta) \neq 0$. At $\theta = 90^\circ$, $f_{\mathbf{a}} = 0.8\sin v$, and every point of the two circles $v = \pm\tfrac{\pi}{2}$ (dashed) is critical: the critical points are not isolated, so $f_{\mathbf{a}}$ is not a Morse function (Corollary [[§55 Morse Functions and the Zero Section#^cor-55-9|§55.9]]). By the symmetry of the torus about its axis, the directions for which $f_{\mathbf{a}}$ fails to be Morse are exactly the multiples of $e_2$: a line, of measure zero in $\mathbb{R}^3$, as Corollary [[§64 Parametric Transversality#^cor-64-9|§64.9]] predicts. (This computation is not in the notes.)

> [!remark] Remark: Directions Outside the Image
> “Incidentally, what can you say about $f_{\mathbf{a}}$ if $\mathbf{a}$ is not in the image of $\pi$?” *(The submitted answer.)* If $\mathbf{a} \notin \pi(S)$, then $\pi^{-1}(\mathbf{a}) = \{\mathbf{a}\} \times \operatorname{Crit}(f_{\mathbf{a}})$ is empty, so $f_{\mathbf{a}}$ has no critical points; in particular it is vacuously Morse (Definition [[§54 Critical Points and the Hessian#^def-54-4|§54.4]]). Corollaries [[§64 Parametric Transversality#^cor-64-10|§64.10]] and [[§64 Parametric Transversality#^cor-64-11|§64.11]] below add two facts about the image and the critical values of $\pi$.

^rem-64-1

> [!theorem] Corollary §64.10: For Compact $M$ the Projection $\pi$ Is Onto
> If $M$ is compact and nonempty, then every $\mathbf{a} \in \mathbb{R}^N$ lies in the image of $\pi : S \to \mathbb{R}^N$ (Theorem [[§64 Parametric Transversality#^thm-64-8|§64.8]]): $\pi$ is onto, and every $f_{\mathbf{a}}$ has a critical point.

^cor-64-10

> [!proof]+ Proof
> *(Not from the assignment.)* Let $\mathbf{a} \in \mathbb{R}^N$. The height function $f_{\mathbf{a}}$ (Definition [[§64 Parametric Transversality#^def-64-2|§64.2]]) is continuous on the compact nonempty set $M$, so it attains a maximum at some $p \in M$. A local extremum is a critical point (Proposition [[§36 Submersions#^prop-36-3|§36.3]]), so $p \in \operatorname{Crit}(f_{\mathbf{a}})$, and $(\mathbf{a}, p) \in \{\mathbf{a}\} \times \operatorname{Crit}(f_{\mathbf{a}}) = \pi^{-1}(\mathbf{a})$ (Theorem [[§64 Parametric Transversality#^thm-64-8|§64.8]]). So $\mathbf{a} = \pi(\mathbf{a}, p)$.

^pf-64-10

*Uses:* [[§64 Parametric Transversality#^def-64-2|Def. §64.2]], [[§36 Submersions#^prop-36-3|§36.3]], [[§64 Parametric Transversality#^thm-64-8|§64.8]]

> [!theorem] Corollary §64.11: The Direction $0$ Is Always a Critical Value
> If $M$ is nonempty and $m \ge 1$, then $0$ is a critical value of $\pi : S \to \mathbb{R}^N$.

^cor-64-11

> [!proof]+ Proof
> *(Not from the assignment.)* For $\mathbf{a} = 0$, $f_0(p) = p \cdot 0 = 0$: $f_0 \equiv 0$. So $d(f_0)_p = 0$ for every $p$, and every point of $M$ is a critical point of $f_0$. In any chart the Hessian matrix of the constant function is the zero $m \times m$ matrix, with determinant $0$ since $m \ge 1$; so every critical point is degenerate (Proposition [[§54 Critical Points and the Hessian#^prop-54-4|§54.4]](2), (a) $\Leftrightarrow$ (d)). As $M \neq \varnothing$, $f_0$ has a degenerate critical point and is not a Morse function (Definition [[§54 Critical Points and the Hessian#^def-54-4|§54.4]]). By Theorem [[§64 Parametric Transversality#^thm-64-8|§64.8]], $0$ is not a regular value of $\pi$, that is, it is a critical value (Definition [[§36 Submersions#^def-36-4|§36.4]]).

^pf-64-11

*Uses:* [[§54 Critical Points and the Hessian#^prop-54-4|§54.4]], [[§54 Critical Points and the Hessian#^def-54-4|Def. §54.4]], [[§64 Parametric Transversality#^thm-64-8|§64.8]], [[§36 Submersions#^def-36-4|Def. §36.4]]

> [!remark]- ★ Remark: The Shape Operator
> *(Beyond the course; stated, not proved here.)* For $(\mathbf{a}, p) \in S$, $\mathbf{a}$ is a normal vector at $p$, and $A_p$ is the *shape operator* (Weingarten map) of $M$ at $p$ in the normal direction $\mathbf{a}$: writing $\mathbf{a} = \pi_{\gamma(t)}(\mathbf{a}) + \nu(t)$ with $\nu(t) \perp T_{\gamma(t)}M$, $A_pu = -\nu'(0)$, the classical $S_{\mathbf{a}}(u) = -(D_u\nu)^{\top}$. The Hessian is the second fundamental form $\mathrm{II}$ paired with $\mathbf{a}$: $\operatorname{Hess}_p f_{\mathbf{a}}(u, w) = \mathbf{a} \cdot \mathrm{II}_p(u, w)$. So $f_{\mathbf{a}}$ fails to be Morse exactly when $M$ is curved degenerately in the direction $\mathbf{a}$ at some point where $\mathbf{a}$ is normal. For a hypersurface ($m = N - 1$), $\pi$ restricted to unit normals is the Gauss map, and the excluded directions are those of normals at points of zero Gauss–Kronecker curvature. The companion statement for distances, $L_{\mathbf{a}}(p) = |p - \mathbf{a}|^2$, is Milnor's (*Morse Theory*, §6): $L_{\mathbf{a}}$ is Morse if and only if $\mathbf{a}$ is not a focal point of $M$ (Definition [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^def-42-4|§42.4]]), the eigenvalue condition of the remark *Focal Points in General* in [[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]].

^rem-64-2
