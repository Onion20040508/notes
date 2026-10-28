---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 39
tags: [differentiable-manifolds, math591]
---
← [[§38 The Regular Value Theorem for Manifolds]] · ↑ [[· 5 Submersions, Submanifolds and Fibrations]] · [[§40 Fibrations]] →

*Stage: submanifolds — Preimages of transverse submanifolds are submanifolds; normal and conormal spaces, critical points of restrictions, Lagrange multipliers, and transverse intersections.*

*Assignment 5, Problem 2.* [[§26 Transversality|§26]] treated transversality in Euclidean space: a smooth map $F : \mathbb{R}^N \to \mathbb{R}^k$ transverse to a regular level set $S = G^{-1}(0)$ (Definition [[§26 Transversality#^def-26-2|§26.2]]) pulls $S$ back to a manifold of the same codimension, with $T^{\mathrm{geo}}_pF^{-1}(S) = F'(p)^{-1}(T^{\mathrm{geo}}_{F(p)}S)$ (Theorem [[§26 Transversality#^thm-26-1|§26.1]]). That proof needed a global defining map $G$. With regular submanifolds and their adapted charts, the same statement holds for any smooth map between manifolds and any regular submanifold of the target — an adapted chart supplies a defining map $x_b$ near each point, which is the localization announced in the remark *An Intrinsic Statement with a Chosen Proof* in [[§26 Transversality|§26]].

> [!definition] Definition §39.1: Transversality to a Submanifold
> Let $F : M \to N$ be smooth, $S \subseteq N$ a regular submanifold, and $\iota : S \to N$ the inclusion. For $p \in F^{-1}(S)$, $F$ is **transverse to $S$ at $p$** if
>
> $$
> F_{\ast p}\big(T_pM\big) + \iota_{\ast F(p)}\big(T_{F(p)}S\big) = T_{F(p)}N ,
> $$
>
> the sum of two subspaces of $T_{F(p)}N$; and $F$ is **transverse to $S$**, written $F \pitchfork S$, if it is transverse to $S$ at every $p \in F^{-1}(S)$. Here $T_qS$ is regarded as a subspace of $T_qN$ through the injective map $\iota_{\ast q}$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]). The condition is imposed only at points of the preimage, and holds vacuously if $F^{-1}(S) = \emptyset$.
>
> *Lee: Ch. 6, Transversality*

^def-39-1

> [!theorem] Theorem §39.1: Preimages of Transverse Submanifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, let $S \subseteq N$ be a regular submanifold of codimension $k$, and suppose $F \pitchfork S$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]). Let $\iota : S \to N$ and $j : F^{-1}(S) \to M$ be the inclusions.
>
> 1. $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$, the codimension of $S$ in $N$ (possibly empty). If it is nonempty, then $k \le m$ and $\dim F^{-1}(S) = m - k$.
> 2. For every $p \in F^{-1}(S)$,
>
> $$
> j_{\ast p}\big(T_pF^{-1}(S)\big) = (F_{\ast p})^{-1}\big(\iota_{\ast F(p)}(T_{F(p)}S)\big) = \big\{\, v \in T_pM : F_{\ast p}v \in \iota_{\ast F(p)}(T_{F(p)}S) \,\big\} .
> $$
>
> Identifying the tangent spaces of the two submanifolds with their images (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), (2) reads $T_pF^{-1}(S) = F_{\ast p}^{-1}\big(T_{F(p)}S\big)$, the formula of Theorem [[§26 Transversality#^thm-26-1|§26.1]].
>
> *Lee: Theorem 6.30(a)*

^thm-39-1

> [!proof]+ Proof
> *(Assignment 5, Problem 2; the student's route, with two steps completed — the normal form is applied at a single point, and the kernel of $(x_b)_{\ast q}$ is computed directly, without the regular value theorem.)* *(The two completions are now separate statements, Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]] and Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]], which Steps 2, 6 and 7 and part (2) below cite; the details are written out in their proofs.)* For (1) we must produce, at every $p \in F^{-1}(S)$, a smooth chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). If $F^{-1}(S) = \emptyset$ there is nothing to check, since the condition of Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] is one condition at each point of the subset (the convention of Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], whose fibres may be empty); and (2) is then vacuous. So fix $p \in F^{-1}(S)$ and put $q = F(p)$, a point of $S$. The plan: an adapted chart of $S$ at $q$ supplies a local defining map $x_b$ for $S$; transversality makes $G = x_b \circ F$ a submersion at $p$; the normal form of $G$ then straightens $F^{-1}(S)$ near $p$. Throughout, the tangent space of an open subset at a point is identified with that of the ambient manifold (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), as everywhere in the notes; by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), applied to a restriction $F|_V = F \circ \iota_V$ with $\iota_V$ the inclusion of the open set $V$, this identification turns the differential of a restriction of $F$ into $F_{\ast p}$.
>
> *Step 1: an adapted chart at $q$.* Since $q \in S$ and $S$ is a regular submanifold of codimension $k$, there is a smooth chart $(U, \varphi = (x^1, \ldots, x^n))$ of $N$ with $q \in U$ and
>
> $$
> U \cap S = \{\, q' \in U : x_b(q') = \vec 0 \,\}, \qquad x_a = (x^1, \ldots, x^{n-k}), \quad x_b = (x^{n-k+1}, \ldots, x^n)
> $$
>
> (Definitions [[§37 Regular Submanifolds#^def-37-2|§37.2]] and [[§37 Regular Submanifolds#^def-37-3|§37.3]]). By Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], applied to $S \subseteq N$,
>
> $$
> \iota_{\ast q}\big(T_qS\big) = \operatorname{Span}\Big\{\frac{\partial}{\partial x^1}\Big|_q, \ldots, \frac{\partial}{\partial x^{n-k}}\Big|_q\Big\} .
> $$
>
> *Step 2: the map $x_b$ and its differential.* Regard $x_b : U \to \mathbb{R}^k$ as a map from the open submanifold $U$ to $\mathbb{R}^k$, the latter with the identity chart, whose coordinate functions are $r^1, \ldots, r^k$. Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]], applied to the regular submanifold $S \subseteq N$ of codimension $k$ and the adapted chart $(U, \varphi)$ of Step 1 (so with $n$ in place of $m$), gives: $x_b$ is smooth, and at $q$ (where $x_b(q) = \vec 0$, as $q \in U \cap S$) $(x_b)_{\ast q}(\partial/\partial x^i|_q)$ is $0$ for $i \le n - k$ and $\partial/\partial r^{\,i-(n-k)}|_{\vec 0}$ for $i > n - k$. Two consequences.
>
> 1. [(a)] *$(x_b)_{\ast q}$ is onto $T_{\vec 0}\mathbb{R}^k$*: by part (2) of the proposition, $x_b$ is a submersion at every point of $U$, in particular at $q$.
> 2. [(b)] *$\ker (x_b)_{\ast q} = \iota_{\ast q}(T_qS)$*: part (4) of the proposition, at the point $q \in U \cap S$.
>
> *Step 3: a chart at $p$ mapped into $U$, and the map $G$.* $F$ is continuous, so $F^{-1}(U)$ is an open set containing $p$. Take any smooth chart $(\tilde V, \tilde\psi)$ of $M$ at $p$ and put $V = \tilde V \cap F^{-1}(U)$, an open set containing $p$ with $F(V) \subseteq U$; the restriction of $\tilde\psi$ to $V$ is again a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1), with $U' = V$). Define
>
> $$
> G = x_b \circ F|_V : V \longrightarrow \mathbb{R}^k .
> $$
>
> It is smooth: $F|_V$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](2)), and smooth as a map into the open submanifold $U$, since it takes values in $U$ and its composite with the inclusion $U \hookrightarrow N$ is the smooth map $F|_V$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3)); then $G$ is a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and the identifications $T_pV = T_pM$, $T_qU = T_qN$,
>
> $$
> G_{\ast p} = (x_b)_{\ast q} \circ F_{\ast p} : T_pM \longrightarrow T_{\vec 0}\mathbb{R}^k .
> $$
>
> *Step 4: $G$ cuts out $F^{-1}(S)$ in $V$.* For $p' \in V$ we have $F(p') \in U$, so
>
> $$
> G(p') = \vec 0 \iff x_b\big(F(p')\big) = \vec 0 \iff F(p') \in U \cap S \iff F(p') \in S \iff p' \in F^{-1}(S) :
> $$
>
> the first equivalence is the definition of $G$; the second is Step 1, $F(p')$ being a point of $U$; the third holds because $F(p') \in U$ anyway. Hence $G^{-1}(\vec 0) = V \cap F^{-1}(S)$.
>
> *Step 5: $G$ is a submersion at $p$.* We show $G_{\ast p}$ is onto. Let $w \in T_{\vec 0}\mathbb{R}^k$. By Step 2(a) there is $u \in T_qN$ with $(x_b)_{\ast q}u = w$. By transversality at $p$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]), $u = F_{\ast p}v + t$ with $v \in T_pM$ and $t \in \iota_{\ast q}(T_qS)$, and $(x_b)_{\ast q}t = 0$ by Step 2(b). By linearity of $(x_b)_{\ast q}$ and Step 3,
>
> $$
> w = (x_b)_{\ast q}u = (x_b)_{\ast q}F_{\ast p}v + (x_b)_{\ast q}t = (x_b)_{\ast q}F_{\ast p}v + 0 = G_{\ast p}v .
> $$
>
> So $G_{\ast p}$ is onto, i.e. $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-1|§36.1]]). In particular $k \le m$: a surjective linear map $T_pM \to T_{\vec 0}\mathbb{R}^k$ has $\dim T_pM \ge \dim T_{\vec 0}\mathbb{R}^k$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), and these dimensions are $m$ and $k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]).
>
> *Step 6: the normal form of $G$ at $p$.* Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]] requires $G$ to be a submersion only at the one point $p$, which is Step 5; no shrinking of $V$ is needed. Its part (1), applied to $G : V \to \mathbb{R}^k$ at $p$ with $c = G(p) = \vec 0$ (and $k$ in place of $n$), gives — by the normal form of $G$ — a smooth chart $(W, \theta = (z^1, \ldots, z^m))$ of $M$ at $p$ with $W \subseteq V$ and a smooth chart $(Y, \chi)$ of $\mathbb{R}^k$ at $\vec 0$ with $G(W) \subseteq Y$ and $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^k(p')\big)$ for $p' \in W$; and, with $\vec c = \chi(\vec 0) = (c_1, \ldots, c_k)$,
>
> $$
> W \cap G^{-1}(\vec 0) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^k(p') = c_k \,\} .
> $$
>
> *Step 7: an adapted chart at $p$.* Since $W \subseteq V$, Step 4 gives $W \cap F^{-1}(S) = W \cap V \cap F^{-1}(S) = W \cap G^{-1}(\vec 0)$, so
>
> $$
> W \cap F^{-1}(S) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^k(p') = c_k \,\} ,
> $$
>
> the intersection cut out in the smooth chart $(W, \theta)$ of $M$ by setting $k$ of its coordinates equal to constants. By Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](2), with the subset $F^{-1}(S)$ — that is, Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] with the coordinates $z^1, \ldots, z^k$ and the constant vector $\vec c$ — there is a chart of $M$ with domain $W$ adapted to $F^{-1}(S)$, of codimension $k$: explicitly, $\big(z^{k+1}, \ldots, z^m, \ z^1 - c_1, \ldots, z^k - c_k\big)$, the translation and permutation of the student's solution. Here $k \le m$ by Step 5.
>
> *Conclusion of (1).* As $p \in F^{-1}(S)$ was arbitrary, every point of $F^{-1}(S)$ lies in a chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations, so $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and $\dim F^{-1}(S) = m - k$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]. The codimension of $S$ in $N$ is also $k$, by hypothesis.
>
> *(2): $j_{\ast p}(T_pF^{-1}(S)) \subseteq \ker G_{\ast p}$.* Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](3) applies to $G : V \to \mathbb{R}^k$, a submersion at $p$ (Step 5) with $c = G(p) = \vec 0$, to the regular submanifold $F^{-1}(S)$ of $M$ of codimension $k$ (part (1)) with inclusion $j$, and to $W' = V$: by Step 4, $F^{-1}(S) \cap V = G^{-1}(\vec 0) = G^{-1}(\vec 0) \cap V$. The inclusion is the first half of its proof: on the open neighbourhood $V \cap F^{-1}(S)$ of $p$ in $F^{-1}(S)$ the composite $G \circ j$ is constant with value $\vec 0$, by Step 4, so $G_{\ast p} \circ j_{\ast p} = (G \circ j)_{\ast p} = 0$ by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]; that is, $G_{\ast p}(j_{\ast p}v) = 0$ for every $v \in T_pF^{-1}(S)$.
>
> *(2): dimensions.* The second half of the lemma's proof: $\dim j_{\ast p}(T_pF^{-1}(S)) = \dim F^{-1}(S) = m - k$, since $j_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]) and by (1); and $\dim \ker G_{\ast p} = m - k$ by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), $G_{\ast p}$ being onto the $k$-dimensional $T_{\vec 0}\mathbb{R}^k$ (Step 5). A subspace of the same finite dimension is the whole space, so $j_{\ast p}(T_pF^{-1}(S)) = \ker G_{\ast p}$.
>
> *(2): the kernel of $G_{\ast p}$.* By Step 3, the definition of the kernel, and Step 2(b),
>
> $$
> \begin{aligned}\ker G_{\ast p} &= \big\{\, v \in T_pM : (x_b)_{\ast q}\big(F_{\ast p}v\big) = 0 \,\big\} \\
> &= \big\{\, v \in T_pM : F_{\ast p}v \in \ker (x_b)_{\ast q} \,\big\} = \big\{\, v \in T_pM : F_{\ast p}v \in \iota_{\ast q}(T_qS) \,\big\} ,\end{aligned}
> $$
>
> which is $(F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. With the previous paragraph, $j_{\ast p}(T_pF^{-1}(S)) = (F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. This is Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](3) — the argument of the tangent-space half of Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]] — run for $G$, followed by the computation of $\ker G_{\ast p}$ that ends the proof of Theorem [[§26 Transversality#^thm-26-1|§26.1]].

^pf-39-1

*Uses:* [[§37 Regular Submanifolds#^prop-37-7|§37.7]], [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§39 Transversality and Lagrange Multipliers#^def-39-1|Def. §39.1]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§26 Transversality#^thm-26-1|§26.1]]

> [!proof]+ Second proof (reduction to Theorem [[§26 Transversality#^thm-26-1|§26.1]] in charts)
> *(Not from lecture; the route of the official solution of Assignment 5, Problem 2, and the one its hint intends. The three facts that transport the Euclidean theorem are checked explicitly.)* Fix $p \in F^{-1}(S)$ and $q = F(p)$. As in Steps 1 and 3 of the first proof, take a chart $(U, \varphi = (x^1, \ldots, x^n))$ of $N$ adapted to $S$ at $q$, so $U \cap S = x_b^{-1}(\vec 0)$, and a chart $(V, \psi)$ of $M$ at $p$ with $F(V) \subseteq U$. Downstairs, set
>
> $$
> \tilde F = \varphi \circ F \circ \psi^{-1} : \psi(V) \to \mathbb{R}^n, \qquad \tilde G : \mathbb{R}^n \to \mathbb{R}^k, \quad \tilde G(y) = (y^{n-k+1}, \ldots, y^n) .
> $$
>
> $\tilde G$ is linear with $\tilde G' = (0 \mid I_k)$ surjective everywhere, so $\tilde S = \tilde G^{-1}(\vec 0) = \mathbb{R}^{n-k} \times \{\vec 0\}$ is a regular level set with $T^{\mathrm{geo}}_y\tilde S = \ker\tilde G' = \mathbb{R}^{n-k} \times \{\vec 0\}$, and $\varphi(U \cap S) = \tilde S \cap \varphi(U)$. As $\tilde F$ takes values in $\varphi(U)$,
>
> $$
> \tilde F^{-1}(\tilde S) = \psi\big(V \cap F^{-1}(S)\big) .
> $$
>
> *Fact 1: transversality survives the charts.* Let $p' \in V \cap F^{-1}(S)$, $q' = F(p')$, $x' = \psi(p')$. By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $\tilde F_{\ast x'} = \varphi_{\ast q'} \circ F_{\ast p'} \circ (\psi^{-1})_{\ast x'}$, and $(\psi^{-1})_{\ast x'}$ is onto (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), so $\operatorname{im}\tilde F_{\ast x'} = \varphi_{\ast q'}(\operatorname{im}F_{\ast p'})$. The chart is adapted at $q'$ too, so $\iota_{\ast q'}(T_{q'}S)$ is spanned by the $\partial/\partial x^i|_{q'}$ with $i \le n - k$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), which $\varphi_{\ast q'}$ sends to the $\partial/\partial r^i|_{\varphi(q')}$, that is, to $e_1, \ldots, e_{n-k}$ under the identification of Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]. Applying the isomorphism $\varphi_{\ast q'}$ to $\operatorname{im}F_{\ast p'} + \iota_{\ast q'}(T_{q'}S) = T_{q'}N$ gives
>
> $$
> \operatorname{im}\tilde F'(x') + T^{\mathrm{geo}}_{\tilde F(x')}\tilde S = \mathbb{R}^n .
> $$
>
> *Fact 2: Theorem [[§26 Transversality#^thm-26-1|§26.1]] on an open set.* Its proof is pointwise until the regular value theorem is invoked: the surjectivity step (or the remark *The Surjectivity Step as an Image Computation*) uses only Fact 1 at each point. So $0$ is a regular value of $\tilde H = \tilde G \circ \tilde F : \psi(V) \to \mathbb{R}^k$, and $\tilde H^{-1}(\vec 0) = \tilde F^{-1}(\tilde S) = \psi(V \cap F^{-1}(S))$. Note $\tilde H = x_b \circ F \circ \psi^{-1}$.
>
> *Fact 3: slice charts pull back.* By the Regular Value Theorem for manifolds (Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]), applied to $\tilde H$ on the open submanifold $\psi(V)$ of $\mathbb{R}^m$, there is a chart $(W', \theta)$ of $\psi(V)$ at $x' = \psi(p)$ adapted to $\tilde H^{-1}(\vec 0)$, with $k$ equations. Then $\theta \circ \psi : \psi^{-1}(W') \to \theta(W')$ is a diffeomorphism onto an open set, so a smooth chart of $M$ (Lemma [[§36 Submersions#^lem-36-5|§36.5]]), and for $p'' \in \psi^{-1}(W') \subseteq V$, the last $k$ coordinates of $\theta(\psi(p''))$ vanish if and only if $\psi(p'') \in \tilde H^{-1}(\vec 0)$, if and only if $p'' \in F^{-1}(S)$. So $(\psi^{-1}(W'), \theta \circ \psi)$ is a chart of $M$ adapted to $F^{-1}(S)$ at $p$, with $k$ equations.
>
> As $p$ was arbitrary, $F^{-1}(S)$ is a regular submanifold of codimension $k$, which is (1). For (2), $G = x_b \circ F|_V = \tilde H \circ \psi$ is the map of the first proof; it is a submersion at $p$, since $\tilde H$ is one at $\psi(p)$ and $\psi_{\ast p}$ is an isomorphism; and (2) follows as there.

^pf-39-1-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§26 Transversality#^thm-26-1|§26.1]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§36 Submersions#^lem-36-5|§36.5]]

> [!definition] Definition §39.2: Normal Space
> Let $S \subseteq M$ be a regular submanifold with inclusion $\iota$, and $p \in S$. The **normal space** of $S$ at $p$ is the quotient vector space (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]])
>
> $$
> T_pM / \iota_{\ast p}(T_pS) ,
> $$
>
> written $T_pM / T_pS$ when $T_pS$ is identified with its image (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]).

^def-39-2

*(Not from lecture.)* If $S$ has codimension $k$, the normal space has dimension $k$: $\dim T_pM = m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), $\dim \iota_{\ast p}(T_pS) = \dim T_pS = m - k$ because $\iota_{\ast p}$ is injective (Propositions [[§37 Regular Submanifolds#^prop-37-6|§37.6]] and [[§37 Regular Submanifolds#^prop-37-3|§37.3]]), and $\dim T_pM/\iota_{\ast p}(T_pS) = m - (m - k) = k$ by Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](3). It needs no metric, unlike the normal vectors of the remark *No Normal Vectors Without a Metric*; its dimension is that of the conormal space $N_pS$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]]).

> [!theorem] Proposition §39.2: Normal Spaces Under a Transverse Map
> Let $F : M \to N$ be smooth, $S \subseteq N$ a regular submanifold of codimension $k$ with inclusion $\iota$, $p \in F^{-1}(S)$ and $q = F(p)$. Put
>
> $$
> K_p = (F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big) \subseteq T_pM .
> $$
>
> 1. $F_{\ast p}$ induces a well-defined linear map of quotient spaces (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]])
>
> $$
> \bar F_{\ast p} : T_pM / K_p \longrightarrow T_qN / \iota_{\ast q}(T_qS), \qquad v + K_p \longmapsto F_{\ast p}v + \iota_{\ast q}(T_qS) .
> $$
>
> 2. $\bar F_{\ast p}$ is injective.
> 3. $\bar F_{\ast p}$ is surjective if and only if $F$ is transverse to $S$ at $p$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]).
>
> So if $F \pitchfork S$, then $K_p = j_{\ast p}(T_pF^{-1}(S))$, with $j$ the inclusion of $F^{-1}(S)$ (Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]]) and $\bar F_{\ast p}$ is an isomorphism $T_pM/T_pF^{-1}(S) \cong T_qN/T_qS$ of the normal spaces (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-2|§39.2]]): both have dimension $k$, which is the reason the codimension is preserved.

^prop-39-2

> [!proof]+ Proof
> *(Not from lecture.)* Write $E = \iota_{\ast q}(T_qS)$, a subspace of $T_qN$ (the image of a linear map), and $\pi_N : T_qN \to T_qN/E$, $\pi_M : T_pM \to T_pM/K_p$ for the projections. $K_p$ is a subspace of $T_pM$, as the preimage of the subspace $E$ under the linear map $F_{\ast p}$: if $F_{\ast p}v, F_{\ast p}v' \in E$, then $F_{\ast p}(v + cv') = F_{\ast p}v + c\,F_{\ast p}v' \in E$. Throughout, two vectors have the same coset iff their difference lies in the subspace (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]).
>
> *(1)* Let $A = \pi_N \circ F_{\ast p} : T_pM \to T_qN/E$, $A(v) = F_{\ast p}v + E$, linear as a composite of linear maps (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)). Its kernel is $K_p$: by $\ker \pi_N = E$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)),
>
> $$
> A(v) = 0 \iff \pi_N\big(F_{\ast p}v\big) = 0 \iff F_{\ast p}v \in E \iff v \in K_p .
> $$
>
> In particular $K_p \subseteq \ker A$, so by the universal property (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](2)) there is a unique linear $\bar F_{\ast p} : T_pM/K_p \to T_qN/E$ with $\bar F_{\ast p} \circ \pi_M = A$, namely $\bar F_{\ast p}(v + K_p) = A(v) = F_{\ast p}v + E$ — the map of (1), well defined and linear.
>
> *(2)* Suppose $\bar F_{\ast p}(v + K_p) = 0$. Then $A(v) = 0$, so $v \in \ker A = K_p$ by (1), i.e. $v + K_p = 0 + K_p$, the zero of $T_pM/K_p$. A linear map with zero kernel is injective.
>
> *(3)* Since $\pi_M$ is surjective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)), every element of $T_pM/K_p$ is some $v + K_p$, and the image of $\bar F_{\ast p}$ is $\{F_{\ast p}v + E : v \in T_pM\}$. So, by the criterion for equal cosets,
>
> $$
> \begin{aligned}\bar F_{\ast p} \text{ is surjective} &\iff \text{for every } u \in T_qN \text{ there is } v \in T_pM \text{ with } u + E = F_{\ast p}v + E \\
> &\iff \text{for every } u \in T_qN \text{ there is } v \in T_pM \text{ with } u - F_{\ast p}v \in E \\
> &\iff \text{every } u \in T_qN \text{ lies in } F_{\ast p}(T_pM) + E .\end{aligned}
> $$
>
> For the last equivalence: if $u - F_{\ast p}v = t \in E$, then $u = F_{\ast p}v + t$ lies in the sum; conversely if $u = F_{\ast p}v + t$ with $t \in E$, then $u - F_{\ast p}v = t \in E$. The last condition says $F_{\ast p}(T_pM) + \iota_{\ast q}(T_qS) = T_qN$, since the sum is a subspace of $T_qN$ in any case; this is transversality at $p$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]).
>
> *The transverse case.* If $F \pitchfork S$, then $\bar F_{\ast p}$ is injective by (2) and surjective by (3), hence an isomorphism, and $K_p = j_{\ast p}(T_pF^{-1}(S))$ by Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]](2). The dimensions are $\dim T_pM = m$ and $\dim T_qN = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]); $\dim E = \dim T_qS = n - k$, as $\iota_{\ast q}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]); and $\dim K_p = m - k$ (Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]](1)). So by Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](3)
>
> $$
> \dim T_pM/K_p = m - (m - k) = k = n - (n - k) = \dim T_qN/E ,
> $$
>
> as an isomorphism requires. Read backwards, the isomorphism alone gives $\dim K_p = m - \dim T_qN/E = m - k$: the codimension of $F^{-1}(S)$ in $M$ is the dimension of its normal space $T_pM/K_p$, and transversality makes $F_{\ast p}$ carry that normal space isomorphically onto the normal space of $S$, of dimension $k$.

^pf-39-2

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-6|Def. §21.6]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§39 Transversality and Lagrange Multipliers#^def-39-1|Def. §39.1]], [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]]

> [!theorem] Corollary §39.3: Special Cases of Transversality
> Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$.
>
> 1. *A point.* For $c \in N$, $\{c\}$ is a regular submanifold of $N$ of codimension $n$, and $F \pitchfork \{c\}$ if and only if $c$ is a regular value of $F$. In that case Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]] returns the regular value theorem, Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]: $F^{-1}(c)$ is a regular submanifold of $M$ of codimension $n$, and $j_{\ast p}(T_pF^{-1}(c)) = \ker F_{\ast p}$ for $p \in F^{-1}(c)$.
> 2. *Two submanifolds.* Let $S, S' \subseteq N$ be regular submanifolds of codimensions $k$ and $k'$, with inclusions $\iota$ and $\iota'$, that *intersect transversally*:
>
> $$
> \iota'_{\ast p}\big(T_pS'\big) + \iota_{\ast p}\big(T_pS\big) = T_pN \qquad \text{for every } p \in S' \cap S ,
> $$
>
> that is, $\iota' \pitchfork S$ (a condition symmetric in $S$ and $S'$). Then $S' \cap S$ is a regular submanifold of $S'$ of codimension $k$, and a regular submanifold of $N$ of codimension $k + k'$; and, with all tangent spaces regarded as subspaces of $T_pN$, $T_p(S' \cap S) = T_pS' \cap T_pS$.
> 3. *Submersions.* If $F$ is a submersion, then $F \pitchfork S$ for every regular submanifold $S \subseteq N$, and $F^{-1}(S)$ is a regular submanifold of $M$ of the same codimension as $S$.
>
> *Lee: Theorem 6.30(b), for (2)*

^cor-39-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)*
>
> *(1)* $\{c\}$ is a regular submanifold of $N$ of codimension $n$: it is the fibre $\mathrm{id}_N^{-1}(c)$ of the identity, a submersion since $(\mathrm{id}_N)_{\ast} = \mathrm{id}$ (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), so Corollary [[§38 The Regular Value Theorem for Manifolds#^cor-38-3|§38.3]] applies. Its tangent space is $0$ (dimension $n - n = 0$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]] and Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]), so transversality at $p \in F^{-1}(c)$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]) reads $F_{\ast p}(T_pM) + 0 = T_cN$: $F_{\ast p}$ is onto. Thus $F \pitchfork \{c\}$ iff $F$ is a submersion at every point of $F^{-1}(c)$, iff $c$ is a regular value (Definition [[§36 Submersions#^def-36-4|§36.4]], the empty case included). Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], with $S = \{c\}$ and $k = n$, then gives that $F^{-1}(c)$ is a regular submanifold of codimension $n$, and $j_{\ast p}(T_pF^{-1}(c)) = (F_{\ast p})^{-1}(0) = \ker F_{\ast p}$.
>
> *(2), in $S'$.* The inclusion $\iota' : S' \to N$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), $(\iota')^{-1}(S) = S' \cap S$, and $\iota'_{\ast p}(T_pS')$ is the image of the differential of $\iota'$ at $p$; so $\iota' \pitchfork S$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]) is the displayed condition, which is symmetric in $S$ and $S'$ because a sum of subspaces is. Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], applied to $\iota'$ in place of $F$, makes $S' \cap S$ a regular submanifold of $S'$ of codimension $k = \operatorname{codim} S$, so of dimension $(n - k') - k = n - (k' + k)$, $S'$ having dimension $n - k'$ (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]); and, with $j : S' \cap S \to S'$ the inclusion, $j_{\ast p}(T_p(S' \cap S)) = (\iota'_{\ast p})^{-1}\big(\iota_{\ast p}(T_pS)\big)$: the vectors of $T_pS'$ whose image in $T_pN$ lies in $\iota_{\ast p}(T_pS)$. Applying $\iota'_{\ast p}$, and using that $\iota' \circ j$ is the inclusion of $S' \cap S$ into $N$ (Chain Rule), the tangent space of $S' \cap S$ inside $T_pN$ is
>
> $$
> \iota'_{\ast p}\Big((\iota'_{\ast p})^{-1}\big(\iota_{\ast p}(T_pS)\big)\Big) = \iota'_{\ast p}\big(T_pS'\big) \cap \iota_{\ast p}\big(T_pS\big) ,
> $$
>
> since for a linear map $A$ and a subspace $E$ of its target, $A\big(A^{-1}(E)\big) = \operatorname{im} A \cap E$: an element $Av$ with $Av \in E$ lies in both; conversely $w = Av \in E$ gives $v \in A^{-1}(E)$. With all tangent spaces regarded as subspaces of $T_pN$: $T_p(S' \cap S) = T_pS' \cap T_pS$.
>
> *(2), in $N$.* Fix $p \in S' \cap S$ (if $S' \cap S = \emptyset$ there is nothing to check). Take charts $(U, \varphi)$ adapted to $S$ and $(U', \varphi')$ adapted to $S'$ at $p$, with local defining maps $x_b : U \to \mathbb{R}^k$ and $x'_b : U' \to \mathbb{R}^{k'}$ (Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]), and on the open set $V = U \cap U' \ni p$ put
>
> $$
> H = (x_b, x'_b) : V \longrightarrow \mathbb{R}^{k + k'} ,
> $$
>
> smooth because its components are. Its first $k$ components are those of $x_b$ and its last $k'$ those of $x'_b$.
> - *$H^{-1}(\vec 0) = V \cap S \cap S'$*: $H(q) = \vec 0$ iff $x_b(q) = \vec 0$ and $x'_b(q) = \vec 0$, iff $q \in U \cap S$ and $q \in U' \cap S'$ (Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]](3)).
> - *$\ker H_{\ast p} = \iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$*: by Proposition [[§36 Submersions#^prop-36-4|§36.4]](1), $H_{\ast p}v = \sum_j dH^j|_p(v)\, \partial/\partial r^j|_{\vec 0}$, which is $0$ iff every coefficient $dH^j|_p(v)$ is $0$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); by the same formula for $x_b$ and $x'_b$, $(x_b)_{\ast p}v = 0$ iff $dH^j|_p(v) = 0$ for $j \le k$, and $(x'_b)_{\ast p}v = 0$ iff $dH^j|_p(v) = 0$ for $j > k$. So $\ker H_{\ast p} = \ker (x_b)_{\ast p} \cap \ker (x'_b)_{\ast p}$, which is $\iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$ by Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]](4).
> - *$H$ is a submersion at $p$*: by the dimension formula for a sum of two subspaces, with $\dim \iota_{\ast p}(T_pS) = n - k$ and $\dim \iota'_{\ast p}(T_pS') = n - k'$ ($\iota_{\ast p}$, $\iota'_{\ast p}$ injective, Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]) and their sum $T_pN$ by transversality,
>
> $$
> \dim \ker H_{\ast p} = (n - k) + (n - k') - n = n - k - k' ,
> $$
>
> so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) $\operatorname{rank} H_{\ast p} = n - (n - k - k') = k + k'$, and $H_{\ast p}$ is onto the $(k + k')$-dimensional $T_{\vec 0}\mathbb{R}^{k+k'}$.
>
> By Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](2), applied to $H : V \to \mathbb{R}^{k+k'}$ at $p$ with $c = \vec 0$, there is a chart $(W, \hat\theta)$ of $N$ at $p$, $W \subseteq V$, whose last $k + k'$ components vanish exactly on $W \cap H^{-1}(\vec 0) = W \cap S \cap S'$; it is adapted to $S' \cap S$, of codimension $k + k'$. As $p$ was arbitrary, $S' \cap S$ is a regular submanifold of $N$ of codimension $k + k'$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), of dimension $n - k - k'$, in agreement with the first part. And Lemma [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]](3), with $W' = V$, gives again that its tangent space at $p$ is $\ker H_{\ast p} = \iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$.
>
> *(3)* If $F$ is a submersion, then $F_{\ast p}(T_pM) = T_{F(p)}N$ already, so the sum in Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]] is all of $T_{F(p)}N$ at every $p \in F^{-1}(S)$: $F \pitchfork S$. Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]] then makes $F^{-1}(S)$ a regular submanifold of $M$ of the same codimension as $S$.

^pf-39-3

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§38 The Regular Value Theorem for Manifolds#^cor-38-3|§38.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§39 Transversality and Lagrange Multipliers#^def-39-1|Def. §39.1]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§39 Transversality and Lagrange Multipliers#^thm-39-1|§39.1]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§37 Regular Submanifolds#^prop-37-7|§37.7]], [[§36 Submersions#^prop-36-4|§36.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|§38.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]

> [!remark] Remark: Special Cases and the Euclidean Versions
> *(Not from lecture.)* Corollary [[§39 Transversality and Lagrange Multipliers#^cor-39-3|§39.3]](1) is the manifold version of Corollary [[§26 Transversality#^cor-26-3|§26.3]], and (2) that of Proposition [[§26 Transversality#^prop-26-4|§26.4]]: the codimensions add, as for level sets. For $S = \{c\}$ a point, (3) is Corollary [[§38 The Regular Value Theorem for Manifolds#^cor-38-3|§38.3]]: a submersion is transverse to every point, and its fibres are regular submanifolds of codimension $n$.

^rem-39-1

*Assignment 5, Problem 4 (“Revisiting Lagrange multipliers”), in the notation of these notes: the assignment's submanifold $M \subset N$ is here $S \subseteq M$, with $M$ the ambient manifold of dimension $m$; its conormal space $\mathcal{N}_pM$ is $N_pS$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]); and $d(G^j)_p$ is written $dG^j|_p$. The problem: (a) a point is a critical point of the restriction $f = \Phi|_S$ of a smooth function $\Phi$ on $M$ exactly when $d\Phi_p$ is conormal to $S$; (b) for a regular level set $S = G^{-1}(0)$ the differentials $dG^1|_p, \ldots, dG^k|_p$ form a basis of $N_pS$, and the method of Lagrange multipliers follows. The proofs are the submitted solution's, written out.*

> [!theorem] Proposition §39.4: Critical Points of a Restriction
> Let $S \subseteq M$ be a regular submanifold, $\iota : S \to M$ the inclusion, $p \in S$, and $\iota_p^{\ast} : T_p^{\ast}M \to T_p^{\ast}S$ the pullback of covectors (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]). Let $\Phi : M \to \mathbb{R}$ be smooth and $f = \Phi \circ \iota = \Phi|_S : S \to \mathbb{R}$ its restriction.
>
> 1. $N_pS = \ker \iota_p^{\ast}$.
> 2. $df_p = \iota_p^{\ast}\big(d\Phi_p\big)$.
> 3. $p$ is a critical point of $f$ if and only if $d\Phi_p \in N_pS$.

^prop-39-4

> [!proof]+ Proof
> *(Assignment 5, Problem 4(a).)* The restriction $f = \Phi \circ \iota$ is smooth, as a composite of smooth maps (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) and Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), so $df_p \in T_p^{\ast}S$ is defined. By Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]] with $F = \iota$ and $F(p) = \iota(p) = p$, the pullback of a covector $\xi \in T_p^{\ast}M$ is the covector on $T_pS$
>
> $$
> \big(\iota_p^{\ast}\xi\big)(v) = \xi\big(\iota_{\ast p}v\big), \qquad v \in T_pS .
> $$
>
> *(1)* Let $\xi \in T_p^{\ast}M$. A covector is zero when it vanishes at every vector, and every element of $\iota_{\ast p}(T_pS)$ is $\iota_{\ast p}v$ for some $v \in T_pS$; so
>
> $$
> \iota_p^{\ast}\xi = 0 \iff \xi\big(\iota_{\ast p}v\big) = 0 \ \text{ for all } v \in T_pS \iff \xi(w) = 0 \ \text{ for all } w \in \iota_{\ast p}(T_pS) \iff \xi \in N_pS ,
> $$
>
> the last step by Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]. So the annihilator of the tangent space, which is how Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]] describes $N_pS$, is the kernel of the pullback, which is how the assignment describes it.
>
> *(2)* This is Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]] with $F = \iota$ and the function $\Phi$, smooth near $\iota(p) = p$: it gives $\iota_p^{\ast}(d\Phi_p) = d(\Phi \circ \iota)_p = df_p$. Written out for $v \in T_pS$, by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]), Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] again, and the formula for $\iota_p^{\ast}$ above,
>
> $$
> df_p(v) = v\big[\Phi \circ \iota\big] = \big(\iota_{\ast p}v\big)[\Phi] = d\Phi_p\big(\iota_{\ast p}v\big) = \big(\iota_p^{\ast}(d\Phi_p)\big)(v) .
> $$
>
> Two covectors on $T_pS$ that agree at every $v$ are equal.
>
> *(3)* By Proposition [[§36 Submersions#^prop-36-2|§36.2]], applied to the smooth function $f$ on the manifold $S$, then (2), then (1),
>
> $$
> p \text{ is a critical point of } f \iff df_p = 0 \iff \iota_p^{\ast}\big(d\Phi_p\big) = 0 \iff d\Phi_p \in \ker \iota_p^{\ast} = N_pS .
> $$
>
> In words: $p$ is critical for the restriction exactly when $d\Phi_p$ vanishes on every vector tangent to $S$ at $p$.

^pf-39-4

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]], [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§36 Submersions#^prop-36-2|§36.2]]

> [!theorem] Proposition §39.5: The Conormal Space of a Regular Level Set
> Let $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$ be smooth, with $0$ a regular value of $G$ (Definition [[§36 Submersions#^def-36-4|§36.4]]), and let $S = G^{-1}(0)$. Then for every $p \in S$ the covectors $dG^1|_p, \ldots, dG^k|_p$ form a basis of the conormal space $N_pS$.

^prop-39-5

> [!proof]+ Proof
> *(Assignment 5, Problem 4(b), first part. The dimension count cites Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]], which the submitted solution re-derives in an adapted chart; the submitted solution's independence argument, and its second, Jacobian form, are now the two proofs of Proposition [[§36 Submersions#^prop-36-4|§36.4]].)* Let $r^1, \ldots, r^k$ be the standard coordinates of $\mathbb{R}^k$, so that $G^j = r^j \circ G$; each $G^j$ is smooth, as a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). Fix $p \in S$. We show three things: $\dim N_pS = k$; each $dG^j|_p$ lies in $N_pS$; and the $k$ covectors $dG^j|_p$ are linearly independent. Then they span a $k$-dimensional subspace of the $k$-dimensional space $N_pS$, and a subspace of the same finite dimension is the whole space; so they are a basis.
>
> *$S$ is a regular submanifold, and $\dim N_pS = k$.* By Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], applied to $G : M \to \mathbb{R}^k$ and the regular value $0$ (so $n = k$ there), $S$ is a regular submanifold of $M$ of codimension $k$; so $N_pS$ is defined, and $\dim N_pS = k$ by Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2). In an adapted chart $(x^1, \ldots, x^m)$ at $p$, a covector $\xi = \sum_i \xi_i\, dx^i|_p$ lies in $N_pS$ exactly when $\xi_i = 0$ for $i \le m - k$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](1)), so $N_pS$ has basis $dx^{m-k+1}|_p, \ldots, dx^m|_p$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2)).
>
> *Each $dG^j|_p$ lies in $N_pS$.* Let $1 \le j \le k$. Every $q \in S = G^{-1}(0)$ has $G(q) = 0$, so $(G^j \circ \iota)(q) = G^j(q) = 0$: the function $G^j \circ \iota$ is the constant $0$ on $S$, and its germ at $p$ is the constant germ $[\underline 0]$. So $(G^j \circ \iota)_{\ast p} = 0$, the pushforward along a constant map being zero (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]), and hence $d(G^j \circ \iota)_p = 0$, the differential being this pushforward followed by the identification $T_0\mathbb{R} \cong \mathbb{R}$ (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]). By Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]](2) with $\Phi = G^j$,
>
> $$
> \iota_p^{\ast}\big(dG^j|_p\big) = d\big(G^j \circ \iota\big)_p = 0 ,
> $$
>
> so $dG^j|_p \in \ker \iota_p^{\ast} = N_pS$ by Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]](1).
>
> *Linear independence.* Since $0$ is a regular value and $p \in G^{-1}(0)$, $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-4|§36.4]](2)). By Proposition [[§36 Submersions#^prop-36-4|§36.4]](2), direction ($\Rightarrow$), the covectors $dG^1|_p, \ldots, dG^k|_p$ are therefore linearly independent. Its proof is the submitted solution's argument: by its formula (1), $G_{\ast p}v = \sum_j dG^j|_p(v)\, \partial/\partial r^j|_0$, a relation $\sum_j c_j\, dG^j|_p = 0$ says $c \cdot G_{\ast p}(v) = 0$ for every $v$, and since $G_{\ast p}$ is onto we may take $G_{\ast p}(v) = c$, which gives $|c|^2 = 0$. Its second proof is the Jacobian form: the relation says $J^{\mathsf T} c = 0$ for the $k \times m$ matrix $J = [\partial G^j/\partial x^i(p)]$ of $G_{\ast p}$ in any chart, and $J^{\mathsf T}$ has rank $k$.
>
> *Conclusion.* $dG^1|_p, \ldots, dG^k|_p$ are $k$ linearly independent elements of $N_pS$, which has dimension $k$, so they form a basis of $N_pS$. As $p \in S$ was arbitrary, this holds at every point of $S$.

^pf-39-5

*Uses:* [[§37 Regular Submanifolds#^prop-37-8|§37.8]], [[§36 Submersions#^prop-36-4|§36.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]], [[§36 Submersions#^def-36-4|Def. §36.4]]

The assignment adds that a regular submanifold is *locally* always a regular level set: this is Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]. Given an adapted chart $(U, \varphi = (x_a, x_b))$, put $G = x_b : U \to \mathbb{R}^k$. By that proposition, $U \cap S = G^{-1}(0)$ and $0$ is a regular value of $G$ (part (3)), $G$ being a submersion at every point of $U$ (part (2)). So Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]] and the theorem below apply to $U \cap S \subseteq U$. For this $G$ the basis $dG^j|_p = dx^{m-k+j}|_p$ is the basis of Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2).

> [!theorem] Theorem §39.6: Lagrange Multipliers
> Let $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$ be smooth with $0$ a regular value, $S = G^{-1}(0)$, $\Phi : M \to \mathbb{R}$ smooth, and $f = \Phi|_S$.
>
> 1. If $f$ has a local extremum at $p \in S$ — $f(q) \le f(p)$ for all $q$ in some neighbourhood of $p$ in $S$, or $f(q) \ge f(p)$ for all such $q$ — then $p$ is a critical point of $f$.
> 2. A point $p \in S$ is a critical point of $f$ if and only if there are $\lambda_1, \ldots, \lambda_k \in \mathbb{R}$ with
>
> $$
> d\Phi_p = \sum_{j=1}^k \lambda_j\, dG^j|_p ,
> $$
>
> and the **Lagrange multipliers** $\lambda_j$ are then unique. Equivalently, the critical points of $f$ are the points $p \in M$ for which there is $\lambda \in \mathbb{R}^k$ with
>
> $$
> d\Big(\Phi - \sum_{j=1}^k \lambda_j G^j\Big)_p = 0, \qquad G(p) = 0 .
> $$
>
> 3. If $M = \mathbb{R}^m$, with the gradient $\nabla h(p) = \big(\partial h/\partial r^1(p), \ldots, \partial h/\partial r^m(p)\big)$ (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]), the vector with $\nabla h(p) \cdot v = dh_p(v)$ (Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]), the conditions of (2) read
>
> $$
> \nabla\Phi(p) = \sum_{j=1}^k \lambda_j\, \nabla G^j(p), \qquad G^1(p) = \cdots = G^k(p) = 0 ,
> $$
>
> $m + k$ equations in the $m + k$ unknowns $(p, \lambda) \in \mathbb{R}^m \times \mathbb{R}^k$.

^thm-39-6

> [!proof]+ Proof
> *(Assignment 5, Problem 4(b), second part: “explain how the method of Lagrange multipliers follows.”)* By Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], $S$ is a regular submanifold of $M$, and $f = \Phi \circ \iota$ is smooth on it (Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]]).
>
> *(1)* This is Proposition [[§36 Submersions#^prop-36-3|§36.3]], applied to the smooth function $f$ on the manifold $S$ (with its induced structure) and the neighbourhood of $p$ in $S$ on which $f \le f(p)$ (or $f \ge f(p)$): it gives $df_p = 0$, which by Proposition [[§36 Submersions#^prop-36-2|§36.2]] says that $p$ is a critical point of $f$. Its proof is the argument along curves: every $v \in T_pS$ is the velocity $D_\gamma$ of a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]), $f \circ \gamma$ has a local extremum at the interior point $0$, and $df_p(v) = (f \circ \gamma)'(0) = 0$. So the method, which looks for the critical points of $f$, finds in particular all local extrema of $\Phi$ subject to the constraint $G = 0$.
>
> *(2)* By Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]](3), $p$ is a critical point of $f$ iff $d\Phi_p \in N_pS$. By Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]], $N_pS$ is the span of $dG^1|_p, \ldots, dG^k|_p$. So if $p$ is critical, $d\Phi_p$ is a linear combination $\sum_j \lambda_j\, dG^j|_p$; conversely, such a combination lies in $N_pS$, which is a subspace (the kernel of the linear map $\iota_p^{\ast}$, Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]](1)) containing every $dG^j|_p$, so $p$ is critical. *Uniqueness:* if $\sum_j \lambda_j\, dG^j|_p = \sum_j \mu_j\, dG^j|_p$, then $\sum_j (\lambda_j - \mu_j)\, dG^j|_p = 0$, and linear independence of the $dG^j|_p$ (Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]], or directly Proposition [[§36 Submersions#^prop-36-4|§36.4]](2), $G$ being a submersion at $p \in G^{-1}(0)$) gives $\lambda_j = \mu_j$ for every $j$. *The equivalent form:* the function $\Phi - \sum_j \lambda_j G^j$ is smooth on $M$, and linearity of $d$ (Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]](1), applied once for each of the $k$ terms) gives
>
> $$
> d\Big(\Phi - \sum_{j=1}^k \lambda_j G^j\Big)_p = d\Phi_p - \sum_{j=1}^k \lambda_j\, dG^j|_p ,
> $$
>
> which is $0$ iff $d\Phi_p = \sum_j \lambda_j\, dG^j|_p$; and a point $p \in M$ lies in $S = G^{-1}(0)$ iff $G(p) = 0$.
>
> *(3)* Use the identity chart of $\mathbb{R}^m$, with coordinate functions $r^1, \ldots, r^m$; its coordinate derivations are the ordinary partial derivatives, $\partial/\partial r^i|_p[h] = \partial h/\partial r^i(p)$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], the chart being the identity). For a smooth $h$ on $\mathbb{R}^m$, Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] gives $dh_p = \sum_i \partial h/\partial r^i(p)\, dr^i|_p$: the components of $dh_p$ are the entries of the gradient $\nabla h(p)$ (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]). This is the identification of Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]: under the linear isomorphism $v \mapsto \xi_v$ of $\mathbb{R}^m$ onto $T_p^{\ast}\mathbb{R}^m$, $\xi_v(D_w|_p) = v \cdot w$, the vector $\nabla h(p)$ goes to $dh_p$. (So for $w = \sum_i w^i\, \partial/\partial r^i|_p$, identified with $(w^1, \ldots, w^m) \in \mathbb{R}^m$ as in Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], $dh_p(w) = \sum_i \partial h/\partial r^i(p)\, w^i = \nabla h(p) \cdot w$.) Two covectors are equal iff their components in the basis $dr^i|_p$ are equal, so, applying this to $h = \Phi$ and $h = G^j$,
>
> $$
> d\Phi_p = \sum_{j=1}^k \lambda_j\, dG^j|_p \iff \frac{\partial \Phi}{\partial r^i}(p) = \sum_{j=1}^k \lambda_j\, \frac{\partial G^j}{\partial r^i}(p) \ \ (i = 1, \ldots, m) \iff \nabla\Phi(p) = \sum_{j=1}^k \lambda_j\, \nabla G^j(p) .
> $$
>
> Equivalently, by Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]: $v \mapsto \xi_v$ is linear and injective, with $\xi_{\nabla\Phi(p)} = d\Phi_p$ and $\xi_{\nabla G^j(p)} = dG^j|_p$, so $d\Phi_p = \sum_j \lambda_j\, dG^j|_p$ says $\xi_{\nabla\Phi(p)} = \xi_{\sum_j \lambda_j \nabla G^j(p)}$, that is, $\nabla\Phi(p) = \sum_j \lambda_j\, \nabla G^j(p)$.
> With $G(p) = 0$ from (2) this is the system stated: $m$ scalar equations from the gradients and $k$ from the constraints, in the $m$ coordinates of $p$ and the $k$ multipliers. (The count makes a finite set of solutions plausible; it is not a theorem that there are any, or finitely many.)

^pf-39-6

*Uses:* [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]], [[§36 Submersions#^prop-36-3|§36.3]], [[§36 Submersions#^prop-36-2|§36.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]], [[§36 Submersions#^prop-36-4|§36.4]], [[§32 The Cotangent Space#^cor-32-3|§32.3]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^def-33-2|Def. §33.2]], [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]

> [!remark]- Connections
> - In $\mathbb{R}^n$, with proofs by the implicit function theorem: [[Method of Lagrange Multipliers|452 hub]], [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 Thm. §17.3]] (several constraints); computational treatment: [[§114 Lagrange Multipliers#^thm-114-1|Calc Thm. §114.1]].
> - In mechanics, constraint forces as multipliers: [[§B6.3 Constraints and Lagrange Multipliers#^thm-b6-3-1|CM Thm. §B6.3.1]].

*(Not from the assignment.)* In (3) the system is the vanishing of the gradient of the single function $L(x, \lambda) = \Phi(x) - \sum_j \lambda_j G^j(x)$ on $\mathbb{R}^{m+k}$: its partial derivatives at $(p, \lambda)$ are $\partial\Phi/\partial r^i(p) - \sum_j \lambda_j\, \partial G^j/\partial r^i(p)$ in the direction of $x^i$ and $-G^j(p)$ in the direction of $\lambda_j$, so $\nabla L(p, \lambda) = 0$ is exactly the $m + k$ equations above.

> [!remark] Remark: The Conormal Bundle
> *(Not from the assignment.)* The conormal spaces $N_pS$, $p \in S$, can be put together, as the cotangent spaces are put together in the cotangent bundle $T^{\ast}M$, into the *conormal bundle* $N^{\ast}S \subseteq T^{\ast}M$. This is done later, in [[§54 Critical Points and the Hessian|§54]], once $T^{\ast}M$ and its standard coordinates are available (Definition [[§55 Morse Functions and the Zero Section#^def-55-1|§55.1]]). There $N^{\ast}S$ is shown to be a regular submanifold of $T^{\ast}M$ of dimension $m$, whatever the codimension of $S$, cut out in the standard coordinates over an adapted chart by the description of $N_pS$ in Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](1) (Proposition [[§55 Morse Functions and the Zero Section#^prop-55-2|§55.2]]); the critical points of a restriction $\Phi|_S$ are where the graph of $d\Phi$ meets it, by Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-4|§39.4]](3) (Corollary [[§55 Morse Functions and the Zero Section#^cor-55-3|§55.3]]); and for $S = G^{-1}(0)$ the Lagrange multipliers of Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-6|§39.6]] are the coordinates of $(p, d\Phi_p) \in N^{\ast}S$ in its fibre, in the basis $dG^1|_p, \ldots, dG^k|_p$ of Proposition [[§39 Transversality and Lagrange Multipliers#^prop-39-5|§39.5]].

^rem-39-2

## Transverse Submanifolds

*Review session, Oct 16 (and Uribe's email before it). The homework defined a map transverse to a submanifold (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]). “We can also talk about two submanifolds being transverse to each other, which was the original definition historically, and then it was generalized.” The Euclidean version is Definition [[§26 Transversality#^def-26-3|§26.3]].*

> [!definition] Definition §39.3: Transverse Submanifolds
> Let $S_1, S_2 \subseteq N$ be regular submanifolds. $S_1$ **intersects $S_2$ transversally**, written $S_1 \pitchfork S_2$, if
>
> $$
> T_qS_1 + T_qS_2 = T_qN \qquad \text{for every } q \in S_1 \cap S_2 ,
> $$
>
> with $T_qS_i \subseteq T_qN$ through the inclusions (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]). The condition holds vacuously if $S_1 \cap S_2 = \varnothing$.
>
> *Lee: Ch. 6, Transversality*

^def-39-3

On the notation: “I don't like it … to me it's very confusing, because intersection to me is an operation … This is a statement, not a set.”

> [!theorem] Proposition §39.7: Transverse Submanifolds and Transverse Maps
> $S_1 \pitchfork S_2$ if and only if the inclusion $\iota_1 : S_1 \hookrightarrow N$ is transverse to $S_2$ (Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]]).

^prop-39-7

> [!proof]+ Proof
> *(Stated in the review session: “if you look at the definitions, it's the same”; written out.)* $\iota_1^{-1}(S_2) = S_1 \cap S_2$, and for $q$ in it, $(\iota_1)_{\ast q}(T_qS_1)$ is $T_qS_1$ regarded as a subspace of $T_qN$. So the condition of Definition [[§39 Transversality and Lagrange Multipliers#^def-39-1|§39.1]] for $F = \iota_1$ at $q$ is $T_qS_1 + T_qS_2 = T_qN$.

^pf-39-7

*Uses:* [[§39 Transversality and Lagrange Multipliers#^def-39-1|Def. §39.1]]

> [!theorem] Theorem §39.8: Transverse Intersections in a Manifold
> If $S_1 \pitchfork S_2$ in $N$, then $S_1 \cap S_2$ is a regular submanifold of $N$, with
>
> $$
> \operatorname{codim}(S_1 \cap S_2) = \operatorname{codim} S_1 + \operatorname{codim} S_2, \qquad T_q(S_1 \cap S_2) = T_qS_1 \cap T_qS_2 .
> $$
>
> *Lee: Theorem 6.30(b)*

^thm-39-8

> [!proof]+ Proof
> *(The theorem “that you proved in homework”, first in the Euclidean case, Proposition [[§26 Transversality#^prop-26-4|§26.4]]; “again, that's just a linear algebra thing.” The manifold version is filled in, along the Euclidean proof.)* Let $n = \dim N$, $k_i = \operatorname{codim} S_i$, and $q \in S_1 \cap S_2$.
>
> *Local defining functions.* Take a slice chart $(U_i, \varphi_i)$ for $S_i$ at $q$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), so that $U_i \cap S_i = G_i^{-1}(0)$, where $G_i : U_i \to \mathbb{R}^{k_i}$ is the last $k_i$ coordinates of $\varphi_i$. $G_i$ is a submersion (a coordinate projection composed with a chart), so by the regular value theorem (Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]) $T_qS_i = \ker (dG_i)_q$, a subspace of $T_qN$ of dimension $n - k_i$.
>
> *Transversality is a regular value condition.* On $W = U_1 \cap U_2$ put $G = (G_1, G_2) : W \to \mathbb{R}^{k_1 + k_2}$, so that $W \cap S_1 \cap S_2 = G^{-1}(0)$ and $\ker dG_q = K_1 \cap K_2$, with $K_i = \ker (dG_i)_q = T_qS_i$. By the dimension formula for subspaces,
>
> $$
> \dim(K_1 \cap K_2) = \dim K_1 + \dim K_2 - \dim(K_1 + K_2) = 2n - k_1 - k_2 - \dim(K_1 + K_2).
> $$
>
> So $K_1 + K_2 = T_qN$ if and only if $\dim \ker dG_q = n - k_1 - k_2$, if and only if $dG_q$ has rank $k_1 + k_2$, that is, is onto. In a chart $(x^1, \ldots, x^n)$ at $q$, with $G_i = (G_i^1, \ldots, G_i^{k_i})$, the matrix of $dG_q$ is the $(k_1 + k_2) \times n$ matrix that stacks those of $(dG_1)_q$ and $(dG_2)_q$:
>
> $$
> \left(\begin{array}{ccc} \dfrac{\partial G_1^1}{\partial x^1}(q) & \cdots & \dfrac{\partial G_1^1}{\partial x^n}(q) \\ \vdots & & \vdots \\ \dfrac{\partial G_1^{k_1}}{\partial x^1}(q) & \cdots & \dfrac{\partial G_1^{k_1}}{\partial x^n}(q) \\ \hline \dfrac{\partial G_2^1}{\partial x^1}(q) & \cdots & \dfrac{\partial G_2^1}{\partial x^n}(q) \\ \vdots & & \vdots \\ \dfrac{\partial G_2^{k_2}}{\partial x^1}(q) & \cdots & \dfrac{\partial G_2^{k_2}}{\partial x^n}(q) \end{array}\right) ,
> $$
>
> so a vector is in its kernel exactly when it is killed by both blocks. Since $S_1 \pitchfork S_2$, this holds at every point of $G^{-1}(0)$: $0$ is a regular value of $G$.
>
> *Conclusion.* By Theorem [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]], $G^{-1}(0) = W \cap S_1 \cap S_2$ is a regular submanifold of $W$ of codimension $k_1 + k_2$, with $T_q(S_1 \cap S_2) = \ker dG_q = T_qS_1 \cap T_qS_2$. Being a regular submanifold is a local condition (slice charts at each point), and $W$ is open in $N$; $q$ was arbitrary, so $S_1 \cap S_2$ is a regular submanifold of $N$ of codimension $k_1 + k_2$.

^pf-39-8

*Uses:* [[§26 Transversality#^prop-26-4|§26.4]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|§38.2]]

*The picture*, asked for by a student (“wonderful picture … great question, I haven't drawn enough pictures”). In $\mathbb{R}^3$, if $S_1$ is a surface and $S_2$ a curve, at a point of intersection the tangent plane and the tangent line must add up to all of $\mathbb{R}^3$, so the curve “has to come across like that … it has to pierce” the surface. If both are surfaces, two planes add up to $\mathbb{R}^3$ exactly when they are different, and then they meet in a line: the surfaces cut through each other along a curve. “It's really a local picture … just the vector space picture.”

![[m591-37-1.svg]]

Codimensions add: $1 + 2 = 3$ for a surface and a curve, a point; $1 + 1 = 2$ for two surfaces, a curve. In the Morse problem of the homework the same thing happened in $T^{\ast}M$: the section $s_f = df$ “was actually an embedding because it was a section, so it's the same as intersecting the image of the embedding with the zero section” (Theorem [[§55 Morse Functions and the Zero Section#^thm-55-7|§55.7]]), and there $m + m = 2m$, the full dimension: the intersection is a set of isolated points.
