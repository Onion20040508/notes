---
type: section
subject: "[[Topology]]"
chapter: 8
section: 23
munkres: "§52"
tags: [topology, math590]
---
← [[§22 Homotopy of Paths]] · ↑ [[8 Homotopy and the Fundamental Group]] · [[§24 Covering Spaces]] →

## Definition

> [!definition] Definition §23.1: Loop
> Fix a topological space $X$ and a point $x_0 \in X$. A **loop based at $x_0$** is a [[§22 Homotopy of Paths#^def-22-3|path]] $f: I \to X$ with $f(0) = f(1) = x_0$.

^def-23-1

> [!definition] Definition §23.2: Fundamental Group
> The **fundamental group** of $X$ based at $x_0$ is
>
> $$\pi_1(X, x_0) = \{[f] \mid f \text{ is a loop based at } x_0\}$$
>
> with group operation $[f] * [g] = [f * g]$.

^def-23-2

> [!remark] Remark
> By the results of [[§22 Homotopy of Paths|§22]], $\pi_1(X, x_0)$ is indeed a [[§21 Algebra Prerequisites꞉ Groups#^def-21-1|group]]:
> - The operation $*$ is well-defined on homotopy classes ([[§22 Homotopy of Paths#^prop-22-4|Proposition §22.4]]).
> - Associativity: $[f] * ([g] * [h]) = ([f] * [g]) * [h]$ ([[Properties of Path Concatenation|Theorem §22.6(1)]]).
> - Identity: $[e_{x_0}]$, where $e_{x_0}(s) = x_0$ for all $s$ ([[Properties of Path Concatenation|Theorem §22.6(2)]]).
> - Inverses: $[f]^{-1} = [\bar{f}]$, where $\bar{f}(s) = f(1-s)$ ([[Properties of Path Concatenation|Theorem §22.6(3)]]).
>
> All products are defined because every loop starts and ends at $x_0$.

^rem-23-1

## Simply Connected Spaces

> [!definition] Definition §23.3: Simply Connected
> A space $X$ is **simply connected** if $X$ is [[§14 Connected Subspaces of ℝ#^def-14-3|path-connected]] and $\pi_1(X, x_0) = \{[e_{x_0}]\}$ (the trivial group) for some ([[§23 The Fundamental Group#^cor-23-3|hence every]]) basepoint $x_0$.
>
> Equivalently: $X$ is path-connected and every loop in $X$ can be continuously shrunk to a point.
>
> **Notation:** $\pi_1(X, x_0) = 0$ means $X$ is simply connected.

^def-23-3

> [!theorem] Lemma §23.1: Paths in Simply Connected Spaces
> In a simply connected space $X$, any two paths having the same initial and terminal points are path homotopic.

^lem-23-1

> [!proof]+ Proof
> Let $\alpha, \beta$ be two paths from $x_0$ to $x_1$. Then $\alpha * \bar{\beta}$ is a loop based at $x_0$. Since $\pi_1(X, x_0) = 0$, this loop is path homotopic to the constant loop:
>
> $$[\alpha * \bar{\beta}] = [e_{x_0}].$$
>
> Then:
>
> $$[\alpha] = [\alpha] * [e_{x_1}] = [\alpha] * [\bar{\beta} * \beta] = [\alpha] * [\bar{\beta}] * [\beta] = [e_{x_0}] * [\beta] = [\beta].$$
>
> (Using: identity, inverse property $[\bar{\beta}] * [\beta] = [e_{x_1}]$, associativity, the hypothesis, and identity again.)

^pf-23-1

*Uses:* [[Properties of Path Concatenation|§22.6]]

## First Computations

> [!example] Example §23.1: $\mathbb{R}^n$ is Simply Connected
> $\mathbb{R}^n$ is simply connected. Let $f$ be any loop at $x_0$. The [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy]]
>
> $$H(s, t) = (1 - t)\,f(s) + t\,x_0$$
>
> is a path homotopy from $f$ to $e_{x_0}$: it continuously shrinks $f$ to the constant loop. (Check: $H(s,0) = f(s)$, $H(s,1) = x_0$, $H(0,t) = (1-t)x_0 + tx_0 = x_0$, $H(1,t) = (1-t)x_0 + tx_0 = x_0$.) So $[f] = [e_{x_0}]$ for every loop $f$, and $\pi_1(\mathbb{R}^n, x_0) = \{[e_{x_0}]\}$.

^ex-23-1

> [!example] Example §23.2: Convex Subsets of $\mathbb{R}^n$ are Simply Connected
> If $X \subseteq \mathbb{R}^n$ is convex and $x_0 \in X$, then $\pi_1(X, x_0) \cong \{e\}$ by the same argument: for any loop $f$ at $x_0$, the straight-line homotopy $H(s,t) = (1-t)f(s) + tx_0$ stays inside $X$ (by convexity: $f(s) \in X$ and $x_0 \in X$ implies $(1-t)f(s) + tx_0 \in X$).
>
> This includes: open balls, closed balls, $\mathbb{R}^n$ itself, any open convex set, $[0,1]^n$, etc.

^ex-23-2

![[m590-23-2.svg]]
*Left: in a convex $X$, each point $f(s)$ of the loop slides straight to $x_0$ (red segments), and the intermediate loops $H(\cdot,t)$ (dashed) shrink onto $x_0$; convexity keeps every segment inside $X$. Right: the same formula fails in $\mathbb{R}^2 \setminus \{0\}$. For the point $f(s)$ opposite $x_0$ the segment runs through the missing origin, so $H(s,\tfrac12) = 0$ is not in the space (see [[§22 Homotopy of Paths#^rem-22-3|the convexity remark in §22]]).*

> [!remark]- Connections
> - Closed balls specifically: $B^n$ is Convex and Simply Connected ([[§26 Deformation Retracts and Homotopy Type#^prop-26-5|§26.5]]).

> [!remark] Remark: What $\pi_1$ Cannot See
> $\pi_1(\mathbb{R}^n) = \{e\}$ for all $n$, so the fundamental group alone cannot distinguish $\mathbb{R}^2$ from $\mathbb{R}^3$. But we don't apply $\pi_1$ to $\mathbb{R}^n$ directly—we apply it to $\mathbb{R}^n$ *minus a point*. The punctured spaces have different loop structures:
> - $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$: loops around the puncture cannot contract.
> - $\pi_1(\mathbb{R}^3 \setminus \{0\}) = \{e\}$: every loop can “go around” the missing point in 3D.
>
> If $\mathbb{R}^2 \cong \mathbb{R}^3$, then $\mathbb{R}^2 \setminus \{0\} \cong \mathbb{R}^3 \setminus \{0\}$, which would force $\mathbb{Z} \cong \{e\}$—a contradiction. The proof of $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]) (which gives $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ since $\mathbb{R}^2 \setminus \{0\}$ deformation retracts onto $S^1$ ([[§26 Deformation Retracts and Homotopy Type#^ex-26-7|Ex. §26.7]])) is the main goal of the next several sections.

^rem-23-2

> [!remark]- Connections
> - $\pi_1(\mathbb{R}^3 \setminus \{0\})$: $\pi_1(S^n) \cong \pi_1(\mathbb{R}^{n+1} \setminus \{0\})$ ([[§26 Deformation Retracts and Homotopy Type#^thm-26-2|§26.2]]) together with $S^n$ is Simply Connected for $n \geq 2$ ([[Sⁿ is Simply Connected for n ≥ 2|§27.3]]).

## Dependence on Basepoint

> [!theorem] Theorem §23.2: Basepoint Independence
> If there exists a path $\alpha$ in $X$ from $x_0$ to $x_1$, then there is an isomorphism of groups
>
> $$\hat{\alpha}: \pi_1(X, x_0) \to \pi_1(X, x_1).$$

^thm-23-2

![[m590-23-3.svg]]
*The isomorphism $\hat\alpha$ from the proof below. A loop $f$ at $x_0$ (blue) becomes the loop $\bar\alpha * f * \alpha$ at $x_1$: travel $\bar\alpha$ from $x_1$ to $x_0$, run $f$, and return along $\alpha$ (red). So $\hat\alpha([f]) = [\bar\alpha] * [f] * [\alpha]$.*

> [!proof]+ Proof
> Define $\hat{\alpha}: \pi_1(X, x_0) \to \pi_1(X, x_1)$ by
>
> $$\hat{\alpha}([f]) = [\bar{\alpha}] * [f] * [\alpha]$$
>
> where $\bar{\alpha}(s) = \alpha(1-s)$ is the reverse path. Concretely: start at $x_1$, run along $\bar{\alpha}$ to $x_0$, run the loop $f$ at $x_0$, then run along $\alpha$ back to $x_1$. This produces a loop based at $x_1$.
>
> **$\hat{\alpha}$ is a homomorphism:**
>
> $$\begin{aligned}
> \hat{\alpha}([f]) * \hat{\alpha}([g]) &= ([\bar{\alpha}] * [f] * [\alpha]) * ([\bar{\alpha}] * [g] * [\alpha]) \\
> &= [\bar{\alpha}] * [f] * \underbrace{[\alpha] * [\bar{\alpha}]}_{= [e_{x_0}]} * [g] * [\alpha] \\
> &= [\bar{\alpha}] * [f] * [g] * [\alpha] \\
> &= \hat{\alpha}([f] * [g]).
> \end{aligned}$$
>
> (Using associativity and $[\alpha] * [\bar{\alpha}] = [e_{x_0}]$, which acts as the identity.)
>
> **$\hat{\alpha}$ is bijective:** Let $\beta = \bar{\alpha}$ (the reverse path of $\alpha$, from $x_1$ to $x_0$). Define $\hat{\beta}: \pi_1(X, x_1) \to \pi_1(X, x_0)$ by $\hat{\beta}([g]) = [\bar{\beta}] * [g] * [\beta] = [\alpha] * [g] * [\bar{\alpha}]$.
>
> Then for any $[f] \in \pi_1(X, x_0)$:
>
> $$\hat{\beta}(\hat{\alpha}([f])) = [\alpha] * ([\bar{\alpha}] * [f] * [\alpha]) * [\bar{\alpha}] = \underbrace{[\alpha] * [\bar{\alpha}]}_{[e_{x_0}]} * [f] * \underbrace{[\alpha] * [\bar{\alpha}]}_{[e_{x_0}]} = [f].$$
>
> Similarly $\hat{\alpha}(\hat{\beta}([g])) = [g]$ for all $[g] \in \pi_1(X, x_1)$. So $\hat{\alpha}$ and $\hat{\beta}$ are inverses, hence $\hat{\alpha}$ is a bijection.
>
> Since $\hat{\alpha}$ is a bijective homomorphism, it is an [[§21 Algebra Prerequisites꞉ Groups#^def-21-4|isomorphism]].

^pf-23-2

*Uses:* [[Properties of Path Concatenation|§22.6]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|§21.4]], [[§21 Algebra Prerequisites꞉ Groups#^def-21-4|Def. §21.4]]

> [!theorem] Corollary §23.3: $\pi_1$ is Independent of Basepoint for Path-Connected Spaces
> If $X$ is [[§14 Connected Subspaces of ℝ#^def-14-3|path-connected]], then $\pi_1(X, x_0) \cong \pi_1(X, x_1)$ for any $x_0, x_1 \in X$. In particular, the isomorphism *type* of $\pi_1(X, x_0)$ is a well-defined invariant of $X$.

^cor-23-3

*Uses:* [[Basepoint Independence of π₁|§23.2]]

> [!remark] Remark
> For path-connected spaces, we often write $\pi_1(X)$ (suppressing the basepoint) when we only care about the isomorphism type. However, the isomorphism $\hat{\alpha}$ *depends on the choice of path $\alpha$*: a different path $\alpha'$ from $x_0$ to $x_1$ gives a potentially different isomorphism $\hat{\alpha}'$. The isomorphism is “canonical up to conjugation” in a precise sense: $\hat{\alpha}'([f]) = [\bar{\alpha}' * \alpha] \cdot \hat{\alpha}([f]) \cdot [\bar{\alpha} * \alpha']$. When $\pi_1$ is abelian, all such isomorphisms agree, and the basepoint truly doesn't matter.

^rem-23-3

## The Induced Homomorphism

> [!definition] Definition §23.4: Induced Homomorphism
> Let $h: (X, x_0) \to (Y, y_0)$ be a continuous map with $h(x_0) = y_0$. The **induced homomorphism** $h_*: \pi_1(X, x_0) \to \pi_1(Y, y_0)$ is defined by
>
> $$h_*([f]) = [h \circ f].$$

^def-23-4

> [!theorem] Proposition §23.4: $h_*$ is a Well-Defined Group Homomorphism
> The map $h_*$ defined above is a well-defined group [[§21 Algebra Prerequisites꞉ Groups#^def-21-3|homomorphism]].

^prop-23-4

> [!proof]+ Proof
> Three things must be verified.
>
> **(1) $h \circ f$ is a loop in $Y$ based at $y_0$.** If $f: I \to X$ is a loop at $x_0$, then $h \circ f: I \to Y$ is continuous (composition of continuous maps), and:
>
> $$(h \circ f)(0) = h(f(0)) = h(x_0) = y_0, \qquad (h \circ f)(1) = h(f(1)) = h(x_0) = y_0.$$
>
> So $h \circ f$ is indeed a loop in $Y$ based at $y_0$, and $[h \circ f] \in \pi_1(Y, y_0)$. The hypothesis $h(x_0) = y_0$ is essential: without it, $h \circ f$ would not start and end at $y_0$.
>
> **(2) $h_*$ is well-defined on homotopy classes.** We must show: if $f \simeq_p f'$, then $h \circ f \simeq_p h \circ f'$. Let $F: I \times I \to X$ be a path homotopy from $f$ to $f'$. Then $h \circ F: I \times I \to Y$ is a path homotopy from $h \circ f$ to $h \circ f'$:
> - $(h \circ F)(s, 0) = h(f(s)) = (h \circ f)(s)$ and $(h \circ F)(s, 1) = h(f'(s)) = (h \circ f')(s)$.
> - $(h \circ F)(0, t) = h(F(0,t)) = h(x_0) = y_0$ and $(h \circ F)(1, t) = h(F(1,t)) = h(x_0) = y_0$.
>
> So $[f] = [f']$ implies $[h \circ f] = [h \circ f']$, and $h_*$ depends only on the homotopy class.
>
> **(3) $h_*$ is a homomorphism.** We verify $h_*([f] * [g]) = h_*([f]) * h_*([g])$:
>
> $$h_*([f] * [g]) = h_*([f * g]) = [h \circ (f * g)] = [(h \circ f) * (h \circ g)] = [h \circ f] * [h \circ g] = h_*([f]) * h_*([g]).$$
>
> The key step is $h \circ (f * g) = (h \circ f) * (h \circ g)$: since $(f * g)(s)$ equals $f(2s)$ or $g(2s-1)$ depending on $s$, applying $h$ pointwise gives $h(f(2s))$ or $h(g(2s-1))$, which is exactly $((h \circ f) * (h \circ g))(s)$.

^pf-23-4

*Uses:* [[§9 Continuous Functions#^thm-9-4|§9.4]], [[§22 Homotopy of Paths#^def-22-4|Def. §22.4]], [[§22 Homotopy of Paths#^def-22-6|Def. §22.6]]

## Functorial Properties

> [!theorem] Theorem §23.5: Functoriality of $\pi_1$
> 1. **Composition:** If $h: (X, x_0) \to (Y, y_0)$ and $k: (Y, y_0) \to (Z, z_0)$ are continuous, then $(k \circ h)_* = k_* \circ h_*$.
> 2. **Identity:** If $\operatorname{id}: (X, x_0) \to (X, x_0)$ is the identity map, then $\operatorname{id}_*$ is the identity homomorphism on $\pi_1(X, x_0)$.

^thm-23-5

> [!proof]+ Proof
> **(1)** For any $[f] \in \pi_1(X, x_0)$:
>
> $$(k \circ h)_*([f]) = [(k \circ h) \circ f] = [k \circ (h \circ f)] = k_*([h \circ f]) = k_*(h_*([f])) = (k_* \circ h_*)([f]).$$
>
> (Using associativity of function composition.)
>
> **(2)** $\operatorname{id}_*([f]) = [\operatorname{id} \circ f] = [f]$.

^pf-23-5

*Uses:* [[§23 The Fundamental Group#^def-23-4|Def. §23.4]]

> [!theorem] Corollary §23.6: $\pi_1$ is a Topological Invariant
> If $h: X \to Y$ is a [[§9 Continuous Functions#^def-9-2|homeomorphism]], then $h_*: \pi_1(X, x_0) \to \pi_1(Y, h(x_0))$ is an isomorphism.

^cor-23-6

> [!proof]+ Proof
> Let $k = h^{-1}$. Then $k \circ h = \operatorname{id}_X$ and $h \circ k = \operatorname{id}_Y$. By [[Functoriality of π₁|functoriality]]:
>
> $$k_* \circ h_* = (k \circ h)_* = (\operatorname{id}_X)_* = \operatorname{id}_{\pi_1(X, x_0)}$$
>
> and similarly $h_* \circ k_* = \operatorname{id}_{\pi_1(Y, h(x_0))}$. So $h_*$ and $k_*$ are inverses, hence $h_*$ is an isomorphism.

^pf-23-6

*Uses:* [[Functoriality of π₁|§23.5]], [[§23 The Fundamental Group#^prop-23-4|§23.4]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|§21.4]]

> [!remark]- Connections
> - Weakened to homotopy equivalences: Homotopy Equivalence Induces Isomorphism on $\pi_1$ ([[§26 Deformation Retracts and Homotopy Type#^thm-26-15|§26.15]]).
> - Used to distinguish surfaces: [[§28 Fundamental Group of Some Surfaces#^cor-28-6|Four Topologically Distinct Surfaces]].

> [!remark] Remark
> This is the payoff: if $X \cong Y$, then $\pi_1(X) \cong \pi_1(Y)$. Equivalently, $\pi_1(X) \not\cong \pi_1(Y)$ implies $X \not\cong Y$. The functorial properties say that $\pi_1$ is a **functor** from the category of pointed topological spaces to the category of groups—it converts topological problems (are these spaces homeomorphic?) into algebraic problems (are these groups isomorphic?).

^rem-23-4

> [!remark] Remark: Naturality: Structure Transports Across Homeomorphisms
> Functoriality has a powerful practical consequence: if you compute $\pi_1(X) \cong G$ using a covering map $p: E \to X$ and the [[§24 Covering Spaces#^def-24-7|lifting correspondence]], then for any homeomorphism $h: Y \to X$:
> 1. The **transported covering** $p' = h^{-1} \circ p: E \to Y$ is a covering map ([[§24 Covering Spaces#^prop-24-5|§24]]).
> 2. The **transported computation** gives $\pi_1(Y) \cong G$ via $h_*$.
> 3. The **diagram commutes** by functoriality: the lifting correspondence for $p'$ and the lifting correspondence for $p$ give the same group $G$, connected by $h_*$.
>
> ![[m590-23-1.svg]]
> *Transporting a covering and its $\pi_1$ computation along a homeomorphism $h: Y \to X$. Left: the transported covering $p' = h^{-1} \circ p$ (red). Right: with $y_0 = h^{-1}(x_0)$, the lifting correspondence $\phi'$ of $p'$ (blue) factors as $\phi' = \phi \circ h_*$ through the lifting correspondence $\phi$ of $p$, because a lift of $g$ through $p'$ is exactly a lift of $h \circ g$ through $p$ (both land in the same fiber $p^{-1}(x_0) = p'^{-1}(y_0)$, identified with $G$).*
>
> This means: **compute $\pi_1$ once for one representative of a homeomorphism class, and it transfers for free to every homeomorphic space.** This is why we can freely switch between $S^1_{\mathbb{C}}$ and $S^1_{\mathbb{R}^2}$ ([[§9 Continuous Functions#^ex-9-5|§9]])—the computation via $p: \mathbb{R} \to S^1_{\mathbb{R}^2}$ automatically gives $\pi_1(S^1_{\mathbb{C}}) \cong \mathbb{Z}$ via the [[§24 Covering Spaces#^ex-24-4|transported covering]] $p'(x) = e^{2\pi i x}$.

^rem-23-5

> [!remark] Remark: Upcoming: Computing Fundamental Groups
> We will develop techniques to compute the fundamental groups of spaces including:
> - $S^1$ (the circle) — $\pi_1(S^1) \cong \mathbb{Z}$ ([[Fundamental Group of the Circle|§24.10]]), the central computation.
> - $S^n$ ($n$-sphere, $n \geq 2$) — $\pi_1(S^n) = 0$ ([[Sⁿ is Simply Connected for n ≥ 2|§27.3]]), simply connected.
> - $S^1 \times S^1$ (torus) — $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ ([[§23 The Fundamental Group#^cor-23-8|§23.8]]).
> - $S^1 \times \mathbb{R}$ (infinite cylinder) — $\pi_1 \cong \mathbb{Z}$.
> - $B^2 \times S^1$ (solid torus) — $\pi_1 \cong \mathbb{Z}$.
> - $\mathbb{R}^2 \setminus \{0\}$ (punctured plane) — $\pi_1 \cong \mathbb{Z}$.
> - $\mathbb{R}^3 \setminus \{x, y, z \text{ axes}\}$ — more complex.
>
> And applications: [[Brouwer Fixed Point Theorem|Brouwer fixed point theorem]], [[Fundamental Theorem of Algebra (topological proof)|fundamental theorem of algebra]], and more.

^rem-23-6

## Fundamental Group of Product Spaces

> [!theorem] Theorem §23.7: $\pi_1$ of a Product Space
> For any spaces $X$ and $Y$ with basepoints $x_0 \in X$ and $y_0 \in Y$:
>
> $$\pi_1(X \times Y, \; (x_0, y_0)) \cong \pi_1(X, x_0) \times \pi_1(Y, y_0).$$

^thm-23-7

> [!proof]+ Proof
> **Strategy.** We construct an explicit isomorphism $\Phi$ that “splits” a loop in $X \times Y$ into its $X$-component and $Y$-component, and show this is a bijective homomorphism.
>
> **The map.** Let $p_1: X \times Y \to X$ and $p_2: X \times Y \to Y$ be the projection maps, $p_1(x,y) = x$ and $p_2(x,y) = y$. Define
>
> $$\Phi: \pi_1(X \times Y, \; (x_0, y_0)) \to \pi_1(X, x_0) \times \pi_1(Y, y_0), \qquad \Phi([\gamma]) = ([p_1 \circ \gamma], \; [p_2 \circ \gamma]).$$
>
> In words: given a loop $\gamma$ in $X \times Y$, project it onto the $X$-coordinate to get a loop in $X$, and onto the $Y$-coordinate to get a loop in $Y$.
>
> **Step 1: $\Phi$ is well-defined.** We must check two things.
>
> *(a) $p_1 \circ \gamma$ is a loop at $x_0$:* Since $p_1$ is continuous and $\gamma: I \to X \times Y$ is continuous, $p_1 \circ \gamma: I \to X$ is continuous. Since $\gamma(0) = \gamma(1) = (x_0, y_0)$, we get $(p_1 \circ \gamma)(0) = x_0 = (p_1 \circ \gamma)(1)$. So $p_1 \circ \gamma$ is a loop at $x_0$. Similarly $p_2 \circ \gamma$ is a loop at $y_0$.
>
> *(b) $\Phi$ is independent of representative:* Suppose $\gamma \simeq_p \gamma'$ via a path homotopy $\Gamma: I \times I \to X \times Y$ (so $\Gamma(s,0) = \gamma(s)$, $\Gamma(s,1) = \gamma'(s)$, $\Gamma(0,t) = \Gamma(1,t) = (x_0,y_0)$). Then $p_1 \circ \Gamma: I \times I \to X$ is a path homotopy between $p_1 \circ \gamma$ and $p_1 \circ \gamma'$:
> - $(p_1 \circ \Gamma)(s, 0) = p_1(\gamma(s)) = (p_1 \circ \gamma)(s)$. ✓
> - $(p_1 \circ \Gamma)(s, 1) = p_1(\gamma'(s)) = (p_1 \circ \gamma')(s)$. ✓
> - $(p_1 \circ \Gamma)(0, t) = p_1(x_0, y_0) = x_0 = (p_1 \circ \Gamma)(1, t)$. ✓
>
> So $[p_1 \circ \gamma] = [p_1 \circ \gamma']$. Similarly $[p_2 \circ \gamma] = [p_2 \circ \gamma']$. Hence $\Phi([\gamma]) = \Phi([\gamma'])$.
>
> **Step 2: $\Phi$ is a homomorphism.** We need $\Phi([\gamma] * [\gamma']) = \Phi([\gamma]) \cdot \Phi([\gamma'])$.
>
> The key observation: projection commutes with concatenation, i.e., $p_1 \circ (\gamma * \gamma') = (p_1 \circ \gamma) * (p_1 \circ \gamma')$. To see this, recall that $(\gamma * \gamma')(s) = \gamma(2s)$ for $s \in [0, 1/2]$ and $\gamma'(2s-1)$ for $s \in [1/2, 1]$. Applying $p_1$:
>
> $$(p_1 \circ (\gamma * \gamma'))(s) = \begin{cases} p_1(\gamma(2s)) = (p_1 \circ \gamma)(2s) & s \in [0, 1/2] \\ p_1(\gamma'(2s-1)) = (p_1 \circ \gamma')(2s-1) & s \in [1/2, 1] \end{cases}$$
>
> which is exactly $((p_1 \circ \gamma) * (p_1 \circ \gamma'))(s)$. The same holds for $p_2$. Therefore:
>
> $$\begin{aligned}
> \Phi([\gamma] * [\gamma']) &= \Phi([\gamma * \gamma']) = ([p_1 \circ (\gamma * \gamma')], \; [p_2 \circ (\gamma * \gamma')]) \\
> &= ([(p_1 \circ \gamma) * (p_1 \circ \gamma')], \; [(p_2 \circ \gamma) * (p_2 \circ \gamma')]) \\
> &= ([p_1 \circ \gamma] * [p_1 \circ \gamma'], \; [p_2 \circ \gamma] * [p_2 \circ \gamma']) \\
> &= ([p_1 \circ \gamma], [p_2 \circ \gamma]) \cdot ([p_1 \circ \gamma'], [p_2 \circ \gamma']) = \Phi([\gamma]) \cdot \Phi([\gamma']).
> \end{aligned}$$
>
> **Step 3: $\Phi$ is injective.** Since $\Phi$ is a homomorphism, it suffices to show $\ker(\Phi) = \{[e_{(x_0,y_0)}]\}$ (trivial kernel $\Leftrightarrow$ injective, from [[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|§21]]).
>
> Suppose $\Phi([\gamma]) = ([e_{x_0}], [e_{y_0}])$. This means:
> - $[p_1 \circ \gamma] = [e_{x_0}]$: the $X$-component of $\gamma$ is nullhomotopic. So there exists a path homotopy $H_1: I \times I \to X$ from $p_1 \circ \gamma$ to the constant loop $e_{x_0}$.
> - $[p_2 \circ \gamma] = [e_{y_0}]$: the $Y$-component is nullhomotopic. So there exists a path homotopy $H_2: I \times I \to Y$ from $p_2 \circ \gamma$ to $e_{y_0}$.
>
> Combine them: define $H: I \times I \to X \times Y$ by $H(s, t) = (H_1(s, t), \; H_2(s, t))$.
>
> Check $H$ is a path homotopy from $\gamma$ to $e_{(x_0,y_0)}$:
> - *Continuous:* Both coordinates $H_1, H_2$ are continuous, so $H$ is continuous.
> - *Starts at $\gamma$:* $H(s, 0) = (H_1(s,0), H_2(s,0)) = ((p_1 \circ \gamma)(s), (p_2 \circ \gamma)(s))$. But a point in $X \times Y$ is determined by its coordinates: $\gamma(s) = (p_1(\gamma(s)), p_2(\gamma(s))) = ((p_1 \circ \gamma)(s), (p_2 \circ \gamma)(s))$. So $H(s,0) = \gamma(s)$. ✓
> - *Ends at constant:* $H(s, 1) = (H_1(s,1), H_2(s,1)) = (x_0, y_0) = e_{(x_0,y_0)}(s)$. ✓
> - *Endpoints fixed:* $H(0, t) = (H_1(0,t), H_2(0,t)) = (x_0, y_0)$ and $H(1, t) = (x_0, y_0)$. ✓
>
> So $[\gamma] = [e_{(x_0,y_0)}]$, the identity. Hence $\ker(\Phi)$ is trivial and $\Phi$ is injective.
>
> **Step 4: $\Phi$ is surjective.** Given any $([f], [g]) \in \pi_1(X, x_0) \times \pi_1(Y, y_0)$, we must find a loop $\gamma$ in $X \times Y$ with $\Phi([\gamma]) = ([f], [g])$.
>
> Define $\gamma: I \to X \times Y$ by $\gamma(t) = (f(t), g(t))$. Check:
> - *Continuous:* Both coordinates $f$ and $g$ are continuous.
> - *Loop at $(x_0, y_0)$:* $\gamma(0) = (f(0), g(0)) = (x_0, y_0) = (f(1), g(1)) = \gamma(1)$.
> - *$\Phi$ hits the target:* $\Phi([\gamma]) = ([p_1 \circ \gamma], [p_2 \circ \gamma]) = ([f], [g])$, since $(p_1 \circ \gamma)(t) = f(t)$ and $(p_2 \circ \gamma)(t) = g(t)$.
>
> Since $\Phi$ is a bijective homomorphism, it is an isomorphism.

^pf-23-7

*Uses:* [[§21 Algebra Prerequisites꞉ Groups#^def-21-5|Def. §21.5]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|§21.8]], [[§10 Product Topology on Arbitrary Products#^thm-10-1|§10.1]]

> [!theorem] Corollary §23.8: Fundamental Group of the Torus
> $\pi_1(S^1 \times S^1) \cong \pi_1(S^1) \times \pi_1(S^1) \cong \mathbb{Z} \times \mathbb{Z}$.

^cor-23-8

> [!proof]+ Proof
> Apply the [[§23 The Fundamental Group#^thm-23-7|theorem]] with $X = Y = S^1$ and the [[§21 Algebra Prerequisites꞉ Groups#^thm-21-7|product of isomorphisms theorem]] (§21):
>
> $$\pi_1(S^1 \times S^1) \cong \pi_1(S^1) \times \pi_1(S^1) \cong \mathbb{Z} \times \mathbb{Z}.$$

^pf-23-8

*Uses:* [[§23 The Fundamental Group#^thm-23-7|§23.7]], [[§21 Algebra Prerequisites꞉ Groups#^thm-21-7|§21.7]], [[Fundamental Group of the Circle|§24.10]]

> [!remark]- Connections
> - Second computation via van Kampen: $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ via van Kampen ([[§29 The Seifert–van Kampen Theorem#^ex-29-4|Ex. §29.4]]).
> - Covering $\mathbb{R}^2 \to T^2$: [[§24 Covering Spaces#^ex-24-3|Example §24.3]].

> [!remark] Remark
> The two generators of $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$ correspond to the two independent loops on the torus: one around the “hole” (the longitude) and one around the “tube” (the meridian). The element $(m, n) \in \mathbb{Z} \times \mathbb{Z}$ represents a loop that winds $m$ times around the longitude and $n$ times around the meridian. Since $\mathbb{Z} \times \mathbb{Z}$ is abelian, the order doesn't matter—going around the hole then the tube is the same as the tube then the hole. This is in contrast to the [[§28 Fundamental Group of Some Surfaces#^thm-28-4|figure-eight]], where $\pi_1 \cong F_2$ (nonabelian).

^rem-23-7
