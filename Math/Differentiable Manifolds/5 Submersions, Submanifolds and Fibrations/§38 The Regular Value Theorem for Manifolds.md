---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 38
tags: [differentiable-manifolds, math591]
---
← [[§37 Regular Submanifolds]] · ↑ [[· 5 Submersions, Submanifolds and Fibrations]] · [[§39 Transversality and Lagrange Multipliers]] →

*Stage: submanifolds — Regular level sets of smooth maps between manifolds are regular submanifolds — the regular submanifolds of [[§37 Regular Submanifolds|§37]] as solution sets of equations.*

*Lecture 12. “And now we go back to submersions” — to “[the] wonderful version of the regular value theorem.”*

The local half of the theorem below holds at a single point where a map is a submersion. It is isolated as a lemma because it is used twice: for level sets here, and for preimages of transverse submanifolds in [[§39 Transversality and Lagrange Multipliers|§39]].

> [!theorem] Lemma §38.1: Level Sets Near a Regular Point
> Let $V \subseteq M$ be open, $\dim M = m$, $G : V \to N$ smooth with $\dim N = n$, $p \in V$ a point at which $G$ is a submersion (Definition [[§36 Submersions#^def-36-1|§36.1]]), and $c = G(p)$.
>
> 1. There are a smooth chart $(W, \theta = (z^1, \ldots, z^m))$ of $M$ at $p$ with $W \subseteq V$ and a smooth chart $(Y, \chi)$ of $N$ at $c$ with $G(W) \subseteq Y$, such that $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^n(p')\big)$ for $p' \in W$; consequently, with $\vec c = \chi(c) = (c_1, \ldots, c_n)$,
>
> $$
> W \cap G^{-1}(c) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^n(p') = c_n \,\} .
> $$
>
> In particular $n \le m$.
> 2. $\hat\theta = \big(z^{n+1}, \ldots, z^m,\ z^1 - c_1, \ldots, z^n - c_n\big)$ is a smooth chart of $M$ with domain $W$, whose last $n$ components vanish exactly on $W \cap G^{-1}(c)$. Hence, if $S \subseteq M$ is a subset with $S \cap W = G^{-1}(c) \cap W$, then $(W, \hat\theta)$ is a chart adapted to $S$ of codimension $n$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]).
> 3. Let $S \subseteq M$ be a regular submanifold of codimension $n$ with inclusion $\iota$ and $p \in S$, and suppose $S \cap W' = G^{-1}(c) \cap W'$ for some open $W' \subseteq V$ containing $p$. Then $\iota_{\ast p}(T_pS) = \ker G_{\ast p}$.

^lem-38-1

> [!proof]+ Proof
> *(Lecture 12's argument for the regular value theorem below, and Steps 6–7 and part (2) of the submitted solution of Assignment 5, Problem 2; isolated here, with the details filled in.)* Throughout, the tangent spaces of the open sets $V$ and $W'$ at their points are identified with those of $M$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]).
>
> *(1)* $V$ is an open submanifold of $M$, of dimension $m$. The normal form (Theorem [[§36 Submersions#^thm-36-6|§36.6]]) requires $G$ to be a submersion only at the one point $p$. (That $G$ is then a submersion on a whole neighbourhood of $p$, Corollary [[§36 Submersions#^cor-36-7|§36.7]], is a consequence of the normal form, not a hypothesis of it; no shrinking of $V$ is needed.) Applied to $G : V \to N$ at $p$, it gives smooth charts $(W, \theta = (z^1, \ldots, z^m))$ of $V$ at $p$ and $(Y, \chi)$ of $N$ at $G(p) = c$, with $G(W) \subseteq Y$, $n \le m$, and
>
> $$
> \chi \circ G \circ \theta^{-1}\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^n\big) \quad \text{on } \theta(W) ;
> $$
>
> applying this identity at $\theta(p')$, and using $z^i = r^i \circ \theta$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), gives $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^n(p')\big)$ for $p' \in W$. Since $W \subseteq V$ is open in $V$, hence in $M$, $(W, \theta)$ is also a smooth chart of $M$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)). For $p' \in W$,
>
> $$
> p' \in G^{-1}(c) \iff G(p') = c \iff \chi\big(G(p')\big) = \chi(c) \iff \big(z^1(p'), \ldots, z^n(p')\big) = (c_1, \ldots, c_n) .
> $$
>
> The first equivalence is the definition of the preimage; the second holds because $G(p')$ and $c = G(p)$ both lie in $Y$ (as $G(W) \subseteq Y$ and $p, p' \in W$), on which $\chi$ is injective; the third is the identity just derived from the normal form.
>
> *(2)* By (1), $W \cap G^{-1}(c)$ is cut out in the smooth chart $(W, \theta)$ of $M$ by setting $n$ of its coordinates, $z^1, \ldots, z^n$, equal to the constants $c_1, \ldots, c_n$; and so is $W \cap S$ for any subset $S$ with $S \cap W = G^{-1}(c) \cap W$. Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]], with $k = n$, the coordinates $z^1, \ldots, z^n$ and the constant vector $\vec c$, therefore gives the chart $(W, A \circ \theta)$ of $M$ adapted to $S$, where, in the notation of its proof, $A(r) = \big(r^{n+1}, \ldots, r^m,\ r^1 - c_1, \ldots, r^n - c_n\big)$; explicitly $A \circ \theta = \hat\theta$. Its last $n$ components $z^1 - c_1, \ldots, z^n - c_n$ vanish at $p' \in W$ if and only if $z^i(p') = c_i$ for $i = 1, \ldots, n$, that is, by (1), if and only if $p' \in G^{-1}(c)$; this is the case $S = G^{-1}(c)$.
>
> *(3): $\iota_{\ast p}(T_pS) \subseteq \ker G_{\ast p}$.* The set $S \cap W'$ is open in $S$ (subspace topology) and contains $p$, so its tangent space at $p$ is $T_pS$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). On it the composite $G \circ \iota$ is defined — $\iota$ maps it into $W' \subseteq V$, and its restriction is smooth into the open set $V$ by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) and Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3) — and constant with value $c$, since $S \cap W' \subseteq G^{-1}(c)$. The pushforward along a constant map is zero (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]), so by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]])
>
> $$
> G_{\ast p} \circ \iota_{\ast p} = (G \circ \iota)_{\ast p} = 0 ,
> $$
>
> that is, $G_{\ast p}(\iota_{\ast p}v) = 0$ for every $v \in T_pS$.
>
> *(3): dimensions.* $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), so, by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]] and Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]],
>
> $$
> \dim \iota_{\ast p}\big(T_pS\big) = \dim T_pS = \dim S = m - n .
> $$
>
> On the other side, $G_{\ast p}$ is onto the $n$-dimensional space $T_cN$, so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1))
>
> $$
> \dim \ker G_{\ast p} = \dim T_pM - \operatorname{rank} G_{\ast p} = m - n .
> $$
>
> A subspace of the same finite dimension is the whole space, so $\iota_{\ast p}(T_pS) = \ker G_{\ast p}$.

^pf-38-1

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§36 Submersions#^thm-36-6|§36.6]], [[§36 Submersions#^cor-36-7|§36.7]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!theorem] Theorem §38.2: The Regular Value Theorem for Manifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, and let $q \in N$ be a regular value of $F$ (Definition [[§36 Submersions#^def-36-4|§36.4]]). Then $S = F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$ (possibly empty), so $\dim S = m - n$, and for every $p \in S$
>
> $$
> \iota_{*p}(T_pS) = \ker F_{*p} .
> $$
>
> *Lee: Corollary 5.14 and Proposition 5.38*

^thm-38-2

> [!proof]+ Proof
> *$S$ is a submanifold (Lecture 12).* We check the definition at each $p \in S$: we need an adapted chart at $p$. (If $S = \emptyset$ there is nothing to check.) By assumption $F$ is a submersion at $p$, so the normal form (Theorem [[§36 Submersions#^thm-36-6|§36.6]]) gives charts $(U, \hat\varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q = F(p)$, with $F(U) \subseteq V$ and $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$. What are the equations of $S \cap U$ in these coordinates? For $q' \in U$,
>
> $$
> \begin{aligned}q' \in S &\iff F(q') = q \iff \psi\big(F(q')\big) = \psi(q) \\
> &\iff \tilde F\big(\hat\varphi(q')\big) = \psi(q) \iff \big(x^1(q'), \ldots, x^n(q')\big) = \big(y^1(q), \ldots, y^n(q)\big).\end{aligned}
> $$
>
> “These are not of the type $x_b = 0$, but of the type $x_a$ equals a constant”: the first $n$ coordinates equal a constant vector. By the observations after the definition (Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]) — any constant, and any $n$ of the coordinates — $S$ has an adapted chart at $p$, of codimension $n$. *(Completion.)* This is Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]], applied with $V = M$, $G = F$ and $c = q$, so that $G^{-1}(c) = S$; its proof gives the details. Part (1) of the lemma is the computation above, with the normal-form charts $(U, \hat\varphi)$ and $(V, \psi)$ and the constant vector $\vec c = \psi(q) = (y^1(q), \ldots, y^n(q))$: the first equivalence is $S = F^{-1}(q)$; the second holds because $F(q')$ and $q$ both lie in $V$, on which $\psi$ is injective; the third because $\psi \circ F = \tilde F \circ \hat\varphi$ on $U$; the last because $\tilde F(\hat\varphi(q'))$ consists of the first $n$ entries of $\hat\varphi(q')$. Part (2), with $S \cap U = F^{-1}(q) \cap U$, is Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] with $k = n$, the coordinates $x^1, \ldots, x^n$ and $\vec c = \psi(q)$: it gives the adapted chart $\big(x^{n+1}, \ldots, x^m,\ x^1 - y^1(q), \ldots, x^n - y^n(q)\big)$ at $p$, of codimension $n$, and $n \le m$ by the normal form. As $p \in S$ was arbitrary, $S$ is a regular submanifold of codimension $n$, and $\dim S = m - n$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]].
>
> *The tangent space.* *(Completion. In lecture: “I won't bother checking the kernel thing, because everything really reduces to the Euclidean [case].”)* By Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](3), applied with $V = W' = M$, $G = F$, $c = q$ and the regular submanifold $S$ of codimension $n$ itself (so that $S \cap M = F^{-1}(q) \cap M$), $\iota_{\ast p}(T_pS) = \ker F_{\ast p}$. In that lemma's proof: the composite $F \circ \iota : S \to N$ is constant, with value $q$, so $F_{\ast p} \circ \iota_{\ast p} = (F \circ \iota)_{\ast p} = 0$ by the Chain Rule and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], and $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast p}$; the left side has dimension $m - n$, since $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), and the right side has dimension $m - n$ by rank–nullity, since $F_{\ast p}$ is onto (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)); and a subspace of the same finite dimension is everything. This is the argument of Lecture 8 for $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), one level up.

^pf-38-2

*Uses:* [[§36 Submersions#^thm-36-6|§36.6]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]

![[m591-15-5.svg]]
*The proof in one square, as on the board. In the normal-form charts $\tilde F$ is the projection onto the first $n$ coordinates, so the level set $S \cap U = F^{-1}(q) \cap U$ is carried by $\hat\varphi$ onto a fibre of a projection: the slice where the first $n$ coordinates equal $\psi(q)$.*

> [!remark]- Connections
> - The earlier regular value theorems it contains: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§30 The Differential in Coordinates#^cor-30-9|§30.9]] (see the remark below); the tangent-space statement generalizes [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]].
> - Constraint sets $\{g_1 = c_1, \ldots, g_k = c_k\}$ in multivariable analysis: [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 §17.3]] (Lagrange multipliers with several constraints).
> - Fibres of submersions that are all copies of one fibre: [[§40 Fibrations#^def-40-1|fibrations, Def. §40.1]].

**Transcription note.** Page 33 of the handwritten notes states the theorem for “$q \in M$ a regular value”; the regular value lies in the target, $q \in N$.

> [!theorem] Corollary §38.3: Fibres of Submersions Are Regular Submanifolds
> If $F : M \to N$ is a submersion, then every fibre $F^{-1}(q)$, $q \in N$, is a regular submanifold of $M$ of codimension $n$ — “they could be empty, some of them.”

^cor-38-3

> [!proof]+ Proof
> Every $q \in N$ is a regular value: every point of $F^{-1}(q)$ is a regular point, and if $F^{-1}(q)$ is empty the condition holds vacuously. Indeed, $F$ is a submersion at every point of $M$ (Definition [[§36 Submersions#^def-36-1|§36.1]]), in particular at every $p \in F^{-1}(q)$, which is what Definition [[§36 Submersions#^def-36-4|§36.4]](2) asks of a regular value; and if $q \notin F(M)$, it is a regular value by Definition [[§36 Submersions#^def-36-4|§36.4]](3). Apply Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]: $F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$.

^pf-38-3

*Uses:* [[§36 Submersions#^def-36-3|Def. §36.3]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§36 Submersions#^def-36-1|Def. §36.1]]

> [!remark] Remark: The Regular Value Theorems — Old and New
> The notes now contain the regular value theorem in five forms. They are one idea met at increasing generality, not competing statements.
>
> | **Where** | **Setting** | **Conclusion** | **Role now** |
> |---|---|---|---|
> | Thm. [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]], Cor. [[§7 The Regular Value Theorem#^cor-7-4\|§7.4]] | $F : W \to \mathbb{R}^k$, $W \subseteq \mathbb{R}^{n+k}$ open | topological manifold | the first version (Lecture 3); Chapter 2 needs it |
> | Prop. [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] | the same | smooth manifold, by graph charts | the Euclidean case (Lecture 6) |
> | Prop. [[§30 The Differential in Coordinates#^prop-30-8\|§30.8]] | $F : M \to N$, level set inside one chart | regular for $F$ iff for $\tilde F$ | a computational tool |
> | Cor. [[§30 The Differential in Coordinates#^cor-30-9\|§30.9]] | $F : M \to N$ | topological manifold | subsumed; a more elementary proof |
> | Thm. [[§38 The Regular Value Theorem for Manifolds#^thm-38-2\|§38.2]] | $F : M \to N$ | submanifold, with $\iota_{*p}(T_pS) = \ker F_{*p}$ | the general theorem (Lecture 12) |
>
> The general theorem contains the others: taking $M$ an open subset of Euclidean space recovers the first two. Its proof goes through the normal form, which rests on the inverse function theorem and not on [[§7 The Regular Value Theorem|§7]], so nothing is circular. The next proposition shows that the old and new versions give the same smooth structure and the same tangent spaces.

^rem-38-1

> [!theorem] Proposition §38.4: The Old and New Versions Agree
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, $c$ a regular value, and $S = F^{-1}(c)$.
> 1. The smooth structure on $S$ given by the graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) is the induced structure of $S$ as a regular submanifold of $W$ (Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]).
> 2. In the setting of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], under the identification $T_pW = \mathbb{R}^{n+k}$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the subspace $\iota_{*p}(T_pS)$ is $T^{\mathrm{geo}}_pS = \ker F'(p)$.

^prop-38-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* First, $c$ is a regular value in both senses, since the matrix of $F_{\ast p}$ in the standard coordinates is $F'(p)$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]). In detail: with the identity charts on $W$ and on $\mathbb{R}^k$, the coordinate representation of $F$ is $F$ itself, so Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] says the matrix of $F_{\ast p}$ in the coordinate bases is $F'(p)$. A linear map is onto $T_{F(p)}\mathbb{R}^k$ iff its rank is $k$, and its rank is that of its matrix (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)); so $F_{\ast p}$ is onto (Definition [[§36 Submersions#^def-36-4|§36.4]]) iff $F'(p)$ has rank $k$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]). Hence Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]] applies to $F : W \to \mathbb{R}^k$, and $S$ is a regular submanifold of $W$ of codimension $k$.
>
> (1) Let $p \in S$. As in the construction of the graph charts, after reordering the coordinates write the points of $\mathbb{R}^{n+k}$ as $(x, y) \in \mathbb{R}^n \times \mathbb{R}^k$ with $\partial F/\partial y\,(p)$ invertible, so that the graph chart near $p$ is $(x, y) \mapsto x$ on $S$. (Here $x = x_I$, $y = x_J$ in the notation of the construction before Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], and the graph chart is $\varphi_J = \pi_I|_{U_J}$. The reordering is a permutation $P$ of coordinates; the chart produced below is then $\Phi \circ P$, with the same last $k$ components, a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]: (2), applied to the identity chart with the linear isomorphism $h = P$, and (1), restricting to an open set, make $P$ a smooth chart on $P^{-1}(U)$, and (2) again, with the diffeomorphism $h = \Phi|_U$, gives $\Phi \circ P$. We suppress $P$.) Let $\Phi(x, y) = (x, F(x, y) - c)$. Its Jacobian at $p$ is $\begin{pmatrix} I_n & 0 \\ \partial F/\partial x & \partial F/\partial y \end{pmatrix}$, which is invertible: it is block lower triangular, so its determinant is $\det I_n \cdot \det\big(\partial F/\partial y\,(p)\big) \ne 0$. Written out, with $x = (x^1, \ldots, x^n)$, $y = (y^1, \ldots, y^k)$, $F = (F^1, \ldots, F^k)$ and all partials at $p$,
>
> $$
> \Phi'(p) = \left(\begin{array}{ccc|ccc} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ \hline \dfrac{\partial F^1}{\partial x^1} & \cdots & \dfrac{\partial F^1}{\partial x^n} & \dfrac{\partial F^1}{\partial y^1} & \cdots & \dfrac{\partial F^1}{\partial y^k} \\ \vdots & & \vdots & \vdots & & \vdots \\ \dfrac{\partial F^k}{\partial x^1} & \cdots & \dfrac{\partial F^k}{\partial x^n} & \dfrac{\partial F^k}{\partial y^1} & \cdots & \dfrac{\partial F^k}{\partial y^k} \end{array}\right) = \begin{pmatrix} I_n & 0 \\ \dfrac{\partial F}{\partial x} & \dfrac{\partial F}{\partial y} \end{pmatrix} .
> $$
> So by the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], with $\Phi$ on $W$ and $a = p$) $\Phi$ restricts to a diffeomorphism of an open $U \ni p$ onto an open set, and by Lemma [[§36 Submersions#^lem-36-5|§36.5]] (with $M = W$, the diffeomorphism being one of manifolds by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]) it is a smooth chart of $W$. Its last $k$ components are $F - c$, which vanish exactly on $S \cap U$, so $\Phi$ is adapted, and its induced chart is $\Phi_S = x|_{S \cap U}$: the graph chart. More precisely, $\Phi_S$ and the graph chart $\varphi_J$ are both restrictions of the projection $(x, y) \mapsto x$, so they agree on $S \cap U \cap U_J$, an open neighbourhood of $p$ in $S$. The same construction works at every point $p'$ of the graph chart's domain $U_J$, with the same splitting $(x, y)$: there $S$ is the graph $y = h_J(x)$, and differentiating $F(x, h_J(x)) = c$ gives $\partial F/\partial x = -\,\partial F/\partial y \cdot h_J'$, so $F'(p') = \partial F/\partial y\,(p') \cdot \big({-h_J'} \mid I_k\big)$; as $F'(p')$ has rank $k$, the $k \times k$ matrix $\partial F/\partial y\,(p')$ has rank $k$, i.e. is invertible. So near each of its points, every graph chart is an induced chart. Induced charts are pairwise compatible, and smoothness of a transition map is local, so every graph chart is compatible with every induced chart, and the two atlases determine the same maximal atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). In detail: let $(U_J, \varphi_J)$ be a graph chart and $(V \cap S, \psi_S)$ an induced chart. Near each point $\varphi_J(p')$ of the domain of $\psi_S \circ \varphi_J^{-1}$, by what was just shown, $\varphi_J$ agrees with an induced chart $\Phi_S$ on an open neighbourhood $O$ of $p'$ in $S$; on $\varphi_J(O \cap V)$ the map $\psi_S \circ \varphi_J^{-1}$ equals $\psi_S \circ \Phi_S^{-1}$, a transition map between induced charts, smooth by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]](2). The same holds for $\varphi_J \circ \psi_S^{-1}$ near each point. So the two charts are compatible, the union of the two atlases is an atlas, and both generate the maximal atlas containing it.
>
> (2) Let $v \in T^{\mathrm{geo}}_pS$, and let $\gamma$ be the lifted line of Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], a curve in $S$ with $\gamma(0) = p$ and $\gamma'(0) = v$, so that $D_v = D_\gamma$. (It is smooth into $\mathbb{R}^{n+k}$ with values in $S$, hence smooth into $S$ by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2); by (1) the structure there is the induced one, so $T_pS$ and $\iota_{\ast p}$ are unambiguous. And $D_v = D_\gamma$ because both send $f$ to $\frac{d}{dt}|_{t=0} f(\gamma(t))$, by Definitions [[§25 The Geometric Tangent Space#^def-25-4|§25.4]] and [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]].) By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], $\iota_{\ast p}D_v = D_{\iota \circ \gamma}$, the derivation $g \mapsto (g \circ \gamma)'(0) = \nabla g(p) \cdot v$ at $p$ — the directional derivative in the direction $v$, which is $v$ under Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]. In detail, for a germ $[g]$ at $p$ on $W$, by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] and the chain rule (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]),
>
> $$
> (\iota_{\ast p}D_v)[g] = D_{\iota \circ \gamma}[g] = \frac{d}{dt}\Big|_{t=0} g\big(\gamma(t)\big) = \nabla g(p) \cdot \gamma'(0) = \nabla g(p) \cdot v = \frac{d}{dt}\Big|_{t=0} g(p + tv) = D_v|_p[g] ,
> $$
>
> where $D_v|_p \in T_pW$ is the derivation of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the vector $v$ under the identification $T_pW = \mathbb{R}^{n+k}$; the fifth equality is the chain rule for the line $t \mapsto p + tv$. Since $v \mapsto D_v$ is onto $T_pS$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]]), $\iota_{\ast p}(T_pS) = T^{\mathrm{geo}}_pS$: every element of $T_pS$ is $D_v$ for some $v \in T^{\mathrm{geo}}_pS$, and its image is the vector $v$. And $T^{\mathrm{geo}}_pS = \ker F'(p)$ by Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]. This matches $\ker F_{\ast p}$ in Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], $F_{\ast p}$ being $F'(p)$: by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], $F_{\ast p}$ corresponds to $F'(p)$ under the identification $\partial/\partial r^i|_p \mapsto e_i$, which is the identification of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], since $D_{e_i}|_p[g] = \frac{d}{dt}|_{t=0}\, g(p + te_i) = \partial g/\partial r^i(p)$; so $\ker F_{\ast p}$ corresponds to $\ker F'(p)$.

^pf-38-4

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§36 Submersions#^lem-36-5|§36.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]
