---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 30
tags: [differentiable-manifolds, math591]
---
← [[§29 Coordinate Derivations and the Basis Theorem]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§31 Tangent Vectors as Velocities of Curves]] →

*Stage: abstract — In charts the differential $F_{\ast p}$ is the Jacobian of the coordinate representation, and the chain rule is matrix multiplication.*

*Lecture 9. The differential $F_{\ast p}$ is defined without coordinates; choosing charts on both sides turns it into a matrix, and the matrix is the Jacobian of the coordinate representation. “This should be very much reminiscent of the things we said about vector spaces — another instance of the same thing.”*

Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$, and $p \in M$. Choose smooth charts $(U, \varphi)$ of $M$ with $p \in U$ and $(V, \psi)$ of $N$ with $F(U) \subseteq V$ — possible because $F$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]) — and write

$$
\varphi = (x^1, \ldots, x^m), \qquad \psi = (y^1, \ldots, y^n), \qquad \tilde F = \psi \circ F \circ \varphi^{-1}, \qquad F^j = y^j \circ F : U \to \mathbb{R}.
$$

By Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]] there are bases

$$
\mathcal{B}_M = \Big\{ \frac{\partial}{\partial x^i}\Big|_p \Big\}_{i=1}^m \ \text{ of } T_pM, \qquad \mathcal{B}_N = \Big\{ \frac{\partial}{\partial y^j}\Big|_{F(p)} \Big\}_{j=1}^n \ \text{ of } T_{F(p)}N .
$$

![[m591-12-9.svg]] ![[m591-12-10.svg]]
*Left, the maps: upstairs $F$ between manifolds, downstairs its coordinate representation $\tilde F$ between open sets of Euclidean space. Right, their linearizations: upstairs the differential, intrinsic; downstairs the Jacobian matrix, and the vertical isomorphisms send $\partial/\partial x^i|_p \mapsto e_i$ and $\partial/\partial y^j|_{F(p)} \mapsto e_j$. Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] below says the right-hand square commutes. It is the square of [[§22 The Differential of a Map Between Vector Spaces|§22, The Differential of a Map Between Vector Spaces]] again, with abstract tangent spaces in place of abstract vector spaces and coordinate bases in place of linear coordinates.*

> [!theorem] Proposition §30.1: Partial Derivatives Upstairs and Downstairs
> Let $F : M \to N$ be smooth, with smooth charts $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ and $(V, \psi = (y^1, \ldots, y^n))$ of $N$ such that $F(U) \subseteq V$. Let $F^j = y^j \circ F : U \to \mathbb{R}$ be the components of $F$, functions on the manifold, and $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ the coordinate representation, with components $\tilde F^j = r^j \circ \tilde F$, functions on Euclidean space. Then $F^j \circ \varphi^{-1} = \tilde F^j$, and therefore, for every $p \in U$,
>
> $$
> \underbrace{\frac{\partial F^j}{\partial x^i}(p)}_{\text{upstairs, on } M} \;=\; \underbrace{\frac{\partial \tilde F^j}{\partial r^i}\big(\varphi(p)\big)}_{\text{downstairs, in } \mathbb{R}^m} .
> $$

^prop-30-1

> [!proof]+ Proof
> Two things are claimed: the identity of functions $F^j \circ \varphi^{-1} = \tilde F^j$ on $\varphi(U)$, and the equality of the two partial derivatives at every $p \in U$.
>
> *The identity of functions.* Both sides are defined on all of $\varphi(U)$: for $r \in \varphi(U)$ the point $\varphi^{-1}(r)$ lies in $U$, so $F(\varphi^{-1}(r)) \in F(U) \subseteq V$, where $y^j$ and $\psi$ are defined. By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](2), applied to the chart $(V, \psi)$ of $N$, its coordinate functions are $y^j = r^j \circ \psi$ on $V$. Hence, on $\varphi(U)$,
>
> $$
> F^j \circ \varphi^{-1} = y^j \circ F \circ \varphi^{-1} = r^j \circ \psi \circ F \circ \varphi^{-1} = r^j \circ \tilde F = \tilde F^j ,
> $$
>
> where the first equality is the definition $F^j = y^j \circ F$, the second is $y^j = r^j \circ \psi$, the third is the definition $\tilde F = \psi \circ F \circ \varphi^{-1}$, and the fourth is the definition $\tilde F^j = r^j \circ \tilde F$. By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](3), the left side is the coordinate representation $(F^j)_\varphi$ of the function $F^j$ in the chart $(U, \varphi)$. So the coordinate representation of $F^j$ is $\tilde F^j$, on all of $\varphi(U)$. In particular $(F^j)_\varphi$ is smooth, since $\tilde F$ is (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]), so $F^j$ is smooth on $U$ and its partial derivatives are defined.
>
> *The partial derivatives.* By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], the upstairs partial derivative of $F^j$ at $p$ is the ordinary partial derivative of its coordinate representation at $\varphi(p)$; and the two functions $F^j \circ \varphi^{-1}$ and $\tilde F^j$, being equal on the open set $\varphi(U) \ni \varphi(p)$, have the same partial derivatives there. So
>
> $$
> \frac{\partial F^j}{\partial x^i}(p) = \frac{\partial (F^j)_\varphi}{\partial r^i}\big(\varphi(p)\big) = \frac{\partial (F^j \circ \varphi^{-1})}{\partial r^i}\big(\varphi(p)\big) = \frac{\partial \tilde F^j}{\partial r^i}\big(\varphi(p)\big) .
> $$

^pf-30-1

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]

> [!remark] Remark: Why This Identity Carries So Much
> Uribe stated it in Lecture 10 and recalled it at the decisive moment of Lecture 11 — it is marked with “!!!” on page 30 of the handwritten notes. When a student asked whether the matrix in the proof of the normal form should be written with $\tilde F$, the answer was: “it's the same thing … that's how we define partials.” Partial derivatives on a manifold are *defined* by going downstairs, so the matrix of partials of the components $F^j$ upstairs is literally the ordinary Jacobian of $\tilde F$ downstairs. This is what turns every local computation on a manifold into calculus in $\mathbb{R}^m$, and it is used in:
> 1. the matrix of the differential (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), which is a one-line proof because of it;
> 2. regular values in one chart (Proposition [[§30 The Differential in Coordinates#^prop-30-8|§30.8]]): the rank of $F_{*p}$ is the rank of $\tilde F'(\varphi(p))$;
> 3. the proof of the local normal form (Theorem [[§36 Submersions#^thm-36-4|§36.4]]), where the matrix $\big[\partial F^j/\partial x^i(p)\big]$ is built from the components $F^j$ but is the Jacobian of $\tilde F$;
> 4. [[§30 The Differential in Coordinates#^rem-30-6|Assignment 3, Problem 4]], whose “matching coefficients” step computes $F_{*p}(\partial/\partial u_k|_p)[x^j]$ as an ordinary partial derivative of $F_\varphi$.
>
> Both sides depend on the charts: changing $\varphi$ or $\psi$ changes the matrix (Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), while $F_{*p}$ itself does not.

^rem-30-1

> [!theorem] Theorem §30.2: The Matrix of the Differential
> $F_{*p}$ is linear, and
>
> $$
> F_{*p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{j=1}^n \frac{\partial F^j}{\partial x^i}(p)\, \frac{\partial}{\partial y^j}\Big|_{F(p)} .
> $$
>
> So the matrix of $F_{*p}$ in the bases $\mathcal{B}_M$, $\mathcal{B}_N$ has the upstairs partials $\partial F^j/\partial x^i(p)$ as entries, and by Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]] it is the $n \times m$ Jacobian of the coordinate representation,
>
> $$
> \Big[\, \frac{\partial F^j}{\partial x^i}(p) \,\Big]_{j, i} = \tilde F'\big(\varphi(p)\big),
> $$
>
> with $j$ the row index and $i$ the column index.
>
> *Lee: Ch. 3, Computations in Coordinates*

^thm-30-2

> [!proof]+ Proof
> *(Lecture 10 — “once you think about it a little bit, it's a one-line proof.”)* Three things are claimed: $F_{\ast p}$ is linear; the displayed formula for $F_{\ast p}(\partial/\partial x^i|_p)$; and the description of the matrix of $F_{\ast p}$.
>
> *Linearity.* This is Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]: $F_{\ast p}$ maps $T_pM$ into $T_{F(p)}N$ and is linear.
>
> *The formula.* Fix $i$ and put $E = F_{\ast p}(\partial/\partial x^i|_p)$, a derivation at $F(p)$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). The universal formula of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], applied at the point $F(p)$ of $N$ with the chart $(V, \psi)$, whose coordinate functions are $y^1, \ldots, y^n$, says that the $j$-th coefficient of any derivation at $F(p)$ is its value on the germ $[y^j]$:
>
> $$
> E = \sum_{j=1}^n E\big[y^j\big]\, \frac{\partial}{\partial y^j}\Big|_{F(p)} .
> $$
>
> So it suffices to compute $E[y^j]$. By the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]), $E[y^j] = \partial/\partial x^i|_p\,[y^j \circ F]$; the function $y^j \circ F$ is the component $F^j$, defined on $U$ because $F(U) \subseteq V$; and $\partial/\partial x^i|_p[F^j]$ is what Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] writes $\partial F^j/\partial x^i(p)$. In one chain:
>
> $$
> F_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big)\big[y^j\big] = \frac{\partial}{\partial x^i}\Big|_p\big[y^j \circ F\big] = \frac{\partial}{\partial x^i}\Big|_p\big[F^j\big] = \frac{\partial F^j}{\partial x^i}(p).
> $$
>
> Substituting these coefficients into the universal formula gives $F_{\ast p}(\partial/\partial x^i|_p) = \sum_j \partial F^j/\partial x^i(p)\, \partial/\partial y^j|_{F(p)}$. That is the formula.
>
> *The matrix.* By Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3), with the basis $e_i = \partial/\partial x^i|_p$ of $T_pM$ (the basis $\mathcal{B}_M$) and the basis $f_j = \partial/\partial y^j|_{F(p)}$ of $T_{F(p)}N$ (the basis $\mathcal{B}_N$), the $i$-th column of the matrix of $F_{\ast p}$ consists of the coefficients of $F_{\ast p}(\partial/\partial x^i|_p)$ in the basis $\mathcal{B}_N$, and its entry in row $j$ is the coefficient of $f_j$. By the formula, that coefficient is $\partial F^j/\partial x^i(p)$; so $j$ is the row index and $i$ the column index. For the identification with $\tilde F'(\varphi(p))$ — the “claim” of the lecture — this is Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]: the partials are *defined* through the chart, and $F^j \circ \varphi^{-1} = \tilde F^j$, so $\partial F^j/\partial x^i(p) = \partial \tilde F^j/\partial r^i(\varphi(p))$, which is the $(j,i)$ entry of $\tilde F'(\varphi(p))$, row $j$ of the Jacobian being the gradient of the $j$-th component $\tilde F^j$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]). So the two $n \times m$ matrices agree entry by entry. “It's all the same.”

^pf-30-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§9 Matrices#^ladr-3-31|LADR 3.31]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]]

> [!remark]- Connections
> - The matrix of a linear map with respect to bases: [[§9 Matrices#^ladr-3-31|LADR 3.31]]; the Jacobian matrix of calculus: [[§7 Differentiability#^def-7-3|452 Def. §7.3]].
> - The same statement between vector spaces: [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]].

> [!remark] Remark
> **Which index is the row.** Uribe's mnemonic, “from the mid-nineteenth century”: *gradients go across*. Row $j$ of the matrix is the gradient of the single function $F^j$, so moving along a row changes $i$; the column $i$ is the image of the $i$-th basis vector, as it must be for the matrix of a linear map.

^rem-30-2

**Transcription notes.** Page 26 of the handwritten notes calls $\mathcal{B}_N$ a basis “of $T_{F(p)}M$”. Page 27 (Lecture 10) repeats the lemma with the basis written $\{\partial/\partial y^j|_p,\ 1 \le j \le m\}$ “of $T_{F(p)}M$” — three slips at once: the base point is $F(p)$, the index runs to $n = \dim N$, and the space is $T_{F(p)}N$. In the same proof the universal formula is written with $\partial/\partial y^j|_p$ for $\partial/\partial y^j|_{F(p)}$. A student asked whether the index on $F^j$ belongs upstairs or downstairs; upstairs, as for coordinates, with $j$ the row index. Uribe also announced that the partials will from now on be written in calculus notation, $\partial F^j/\partial x^i(p)$ rather than $\partial/\partial x^i|_p[F^j]$.

> [!theorem] Corollary §30.3: The Chain Rule in Coordinates
> Let $F : M \to N$ and $G : N \to O$ be smooth, with charts $(U,\varphi)$ at $p$, $(V,\psi)$ at $F(p)$ and $(W,\chi)$ at $G(F(p))$ such that $F(U) \subseteq V$ and $G(V) \subseteq W$, and write $\tilde F = \psi \circ F \circ \varphi^{-1}$, $\tilde G = \chi \circ G \circ \psi^{-1}$ and $\widetilde{G \circ F} = \chi \circ (G \circ F) \circ \varphi^{-1}$ for the coordinate representations. Then $\widetilde{G \circ F} = \tilde G \circ \tilde F$ on $\varphi(U)$, and
>
> $$
> \big(\widetilde{G \circ F}\big)'\big(\varphi(p)\big) = \tilde G'\big(\psi(F(p))\big)\; \tilde F'\big(\varphi(p)\big):
> $$
>
> the matrix of $(G \circ F)_{*p}$ is the product of the matrices of $G_{*F(p)}$ and $F_{*p}$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-30-3

> [!proof]+ Proof
> Two things are claimed: the equality $\widetilde{G \circ F} = \tilde G \circ \tilde F$ on $\varphi(U)$, and the matrix identity.
>
> *The coordinate representations.* First, the charts $(U, \varphi)$ and $(W, \chi)$ are admissible for $G \circ F$: $(G \circ F)(U) = G(F(U)) \subseteq G(V) \subseteq W$. Let $r \in \varphi(U)$ and $q = \varphi^{-1}(r) \in U$. Then $F(q) \in F(U) \subseteq V$, so $\psi^{-1}(\psi(F(q))) = F(q)$: the identity $\psi^{-1} \circ \psi$ of $V$ may be inserted between $G$ and $F$. Hence $\chi \circ G \circ F \circ \varphi^{-1} = (\chi \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$ on $\varphi(U)$, that is,
>
> $$
> \widetilde{G \circ F}(r) = \chi\big(G(F(q))\big) = \chi\Big(G\big(\psi^{-1}(\psi(F(q)))\big)\Big) = \big(\chi \circ G \circ \psi^{-1}\big)\big((\psi \circ F \circ \varphi^{-1})(r)\big) = \tilde G\big(\tilde F(r)\big),
> $$
>
> where $\tilde F(r) = \psi(F(q))$ lies in $\psi(V)$, the domain of $\tilde G$.
>
> *The matrices.* Apply Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] three times, each time in the coordinate bases of the two charts named:
> - to $F$ at $p$, with $(U, \varphi)$ and $(V, \psi)$: the matrix of $F_{\ast p}$ is $\tilde F'(\varphi(p))$;
> - to $G$ at $F(p)$, with $(V, \psi)$ and $(W, \chi)$: the matrix of $G_{\ast F(p)}$ is $\tilde G'(\psi(F(p)))$;
> - to $G \circ F$ at $p$ (smooth by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), with $(U, \varphi)$ and $(W, \chi)$, admissible by the inclusion above: the matrix of $(G \circ F)_{\ast p}$ is $(\widetilde{G \circ F})'(\varphi(p))$.
>
> By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $(G \circ F)_{\ast p} = G_{\ast F(p)} \circ F_{\ast p}$. By Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3) the matrix of a composite is the product of the matrices, $[AB] = [A][B]$, provided the same basis is used on the middle space for both factors — here the coordinate basis of $\psi$ at $F(p)$, which is the case. So
>
> $$
> \big(\widetilde{G \circ F}\big)'\big(\varphi(p)\big) = \big[(G \circ F)_{\ast p}\big] = \big[G_{\ast F(p)} \circ F_{\ast p}\big] = \big[G_{\ast F(p)}\big]\,\big[F_{\ast p}\big] = \tilde G'\big(\psi(F(p))\big)\; \tilde F'\big(\varphi(p)\big):
> $$
>
> the three matrices are the three Jacobians, and the matrix of $(G \circ F)_{\ast p}$ is the product of the matrices of $G_{\ast F(p)}$ and $F_{\ast p}$.
>
> *A second route.* The formula is also the Euclidean chain rule applied to $\widetilde{G \circ F} = \tilde G \circ \tilde F$ at $\varphi(p)$, where $\tilde F(\varphi(p)) = \psi(F(p))$: the Jacobian of a composite of smooth maps between open subsets of Euclidean spaces is the product of the Jacobians, the outer one taken at the image point. The two routes agree, as they must.

^pf-30-3

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[Multivariable Chain Rule|452 §12.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

![[m591-12-11.svg]]
*Upstairs the composite of maps between manifolds; downstairs the composite of their coordinate representations. Each square commutes, so the outer rectangle does, and differentiating the bottom row at $\varphi(p)$ multiplies the Jacobians.*

> [!remark]- Connections
> - The Euclidean chain rule for Jacobians: [[§12 Composition of Functions and the Chain Rule#^rem-12-4|452 §12 (Chain Rule for Jacobians)]]; matrix of a product: [[§9 Matrices#^ladr-3-43|LADR 3.43]].

> [!theorem] Corollary §30.4: Change of Coordinates
> If $(U, \varphi)$ and $(\tilde U, \tilde\varphi)$ are two smooth charts at $p$, with coordinates $x^i$ and $\tilde x^j$, then
>
> $$
> \frac{\partial}{\partial \tilde x^j}\Big|_p = \sum_{i=1}^n \frac{\partial x^i}{\partial \tilde x^j}(p)\, \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> and the change-of-basis matrix is the Jacobian of the transition function $\varphi \circ \tilde\varphi^{-1}$ at $\tilde\varphi(p)$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-30-4

> [!proof]+ Proof
> Write $n = \dim M$. The claim is an equality of tangent vectors at $p$ for each $j$, together with the identification of the coefficient matrix.
>
> *Setting up.* Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] needs a source chart whose domain is mapped into the domain of the target chart. Restrict both charts to the open set $U \cap \tilde U \ni p$; a restriction of a smooth chart to an open subset is again a smooth chart (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)). This changes neither the coordinate derivations at $p$ nor the partial derivatives at $p$, since these are ordinary partial derivatives at $\varphi(p)$, resp. $\tilde\varphi(p)$, which depend only on the functions near that point (the remark on shrinking the chart domain in the proof of Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-1|§29.1]]). So we may assume $U = \tilde U$.
>
> *Applying the theorem.* Take $F = \mathrm{id}_M$, which is smooth, with the chart $(\tilde U, \tilde\varphi)$, coordinates $\tilde x^j$, on the source and the chart $(U, \varphi)$, coordinates $x^i$, on the target; then $\mathrm{id}_M(\tilde U) = U$. The components of $F$ in the target chart are $F^i = x^i \circ \mathrm{id}_M = x^i$, and the coordinate representation is $\varphi \circ \mathrm{id}_M \circ \tilde\varphi^{-1} = \varphi \circ \tilde\varphi^{-1}$, the transition function. Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], with $\tilde x^j$ in the role of the source coordinates and $x^i$ in the role of the target coordinates, gives
>
> $$
> (\mathrm{id}_M)_{\ast p}\Big(\frac{\partial}{\partial \tilde x^j}\Big|_p\Big) = \sum_{i=1}^n \frac{\partial x^i}{\partial \tilde x^j}(p)\, \frac{\partial}{\partial x^i}\Big|_p .
> $$
>
> By Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], $(\mathrm{id}_M)_{\ast p} = \mathrm{id}_{T_pM}$, so the left side is $\partial/\partial \tilde x^j|_p$. That is the formula.
>
> *The matrix.* The formula says that the $j$-th new basis vector $\partial/\partial \tilde x^j|_p$ has the coordinates $\partial x^i/\partial \tilde x^j(p)$ in the old basis $\partial/\partial x^i|_p$, so the change-of-basis matrix $P$ of Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](4) (defined by $e'_j = \sum_i P_{ij}\, e_i$) has entries $P_{ij} = \partial x^i/\partial \tilde x^j(p)$. This is the matrix of $(\mathrm{id}_M)_{\ast p}$ in the two coordinate bases, and by the second part of Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] it is the Jacobian of the coordinate representation $\varphi \circ \tilde\varphi^{-1}$ at $\tilde\varphi(p)$.

^pf-30-4

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-1|§29.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!remark]- Connections
> - The change-of-basis formula of linear algebra: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].
> - Transition functions: [[§2 Topological Manifolds#^def-2-4|Def. §2.4]].

> [!example] Example §30.1: Polar Coordinates
> On $M = \mathbb{R}^2 \setminus \{(x, 0) \mid x \le 0\}$ take the standard chart $(x, y)$ and the polar chart $(r, \theta)$, $0 < r$, $-\pi < \theta < \pi$, with $x = r\cos\theta$ and $y = r\sin\theta$. By Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]],
>
> $$
> \frac{\partial}{\partial r} = \cos\theta\, \frac{\partial}{\partial x} + \sin\theta\, \frac{\partial}{\partial y}, \qquad
> \frac{\partial}{\partial \theta} = -r\sin\theta\, \frac{\partial}{\partial x} + r\cos\theta\, \frac{\partial}{\partial y},
> $$
>
> the coefficients being $\partial x/\partial r$, $\partial y/\partial r$ and $\partial x/\partial\theta$, $\partial y/\partial\theta$.
>
> *Lee: cf. Example C.37*

^ex-30-1

![[m591-12-12.svg]]
*At a point $p$ at radius $r$, the four coordinate derivations — elements of the abstract tangent space $T_pM$ — drawn as the vectors of $T^{\mathrm{geo}}_pM = \mathbb{R}^2$ they correspond to under the identification $\partial_x \leftrightarrow e_1$, $\partial_y \leftrightarrow e_2$ of Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] below (all at the common scale $0.7$). The polar ones are the radial and tangential directions, but $\partial_\theta$ is not a unit vector: it has length $r$, because it records the velocity of the curve $\theta \mapsto (r\cos\theta, r\sin\theta)$ along which the other coordinate is held fixed. A coordinate vector depends on the whole chart, not only on its own coordinate function — the same abstract tangent space, and a different matrix for every map out of it.*

> [!remark]- Connections
> - Polar coordinates in multivariable calculus (Jacobians, change of variables): [[Polar and spherical coordinates]].

> [!theorem] Proposition §30.5: Agreement with the Vector-Space Differential
> Let $W \subseteq \mathbb{R}^m$ be open, $F : W \to \mathbb{R}^n$ smooth, and $a \in W$, and identify the abstract tangent spaces $T_aW \cong \mathbb{R}^m$ and $T_{F(a)}\mathbb{R}^n \cong \mathbb{R}^n$ by $\partial/\partial r^i \mapsto e_i$ — that is, with the geometric tangent spaces $T^{\mathrm{geo}}_aW = \mathbb{R}^m$ and $T^{\mathrm{geo}}_{F(a)}\mathbb{R}^n = \mathbb{R}^n$. Then $F_{*a}$ corresponds to the Jacobian $F'(a)$, i.e. to the differential $dF_a$ of [[§22 The Differential of a Map Between Vector Spaces|§22, The Differential of a Map Between Vector Spaces]]. Under the same identification, $v = \sum_i v^i e_i$ corresponds to the derivation
>
> $$
> [g] \longmapsto \sum_i v^i\, \frac{\partial g}{\partial r^i}(a) = \frac{d}{dt}\Big|_{t=0} g(a + tv),
> $$
>
> the directional derivative $D_v$ of [[§25 The Geometric Tangent Space#From Tangent Vectors to Derivations|§25, From Tangent Vectors to Derivations]].
>
> *Lee: Proposition 3.13 and Corollary 3.3*

^prop-30-5

> [!proof]+ Proof
> On $W$ use the identity chart $(W, \mathrm{id}_W)$, whose coordinate functions are the standard coordinates $r^1, \ldots, r^m$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), and on $\mathbb{R}^n$ the identity chart, with coordinates $r^1, \ldots, r^n$. In an identity chart the coordinate representation of a function $g$ is $g$ itself, so by Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] the coordinate derivation $\partial/\partial r^i|_a$ sends $[g]$ to the ordinary partial derivative $\partial g/\partial r^i(a)$.
>
> *The differential.* Apply Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] with the identity charts; this is allowed, since $F(W) \subseteq \mathbb{R}^n$. The coordinate representation is $\tilde F = \mathrm{id} \circ F \circ \mathrm{id}^{-1} = F$, so the theorem gives
>
> $$
> F_{\ast a}\Big(\frac{\partial}{\partial r^i}\Big|_a\Big) = \sum_{j=1}^n \frac{\partial F^j}{\partial r^i}(a)\, \frac{\partial}{\partial r^j}\Big|_{F(a)} ,
> $$
>
> and the matrix of $F_{\ast a}$ in these bases is $F'(a)$. Under the identifications $\partial/\partial r^i|_a \mapsto e_i$ and $\partial/\partial r^j|_{F(a)} \mapsto e_j$, this says that the linear map $\mathbb{R}^m \to \mathbb{R}^n$ corresponding to $F_{\ast a}$ sends $e_i$ to $\sum_j \partial F^j/\partial r^i(a)\, e_j$, the $i$-th column of $F'(a)$, which is $F'(a)\,e_i$. Two linear maps that agree on a basis are equal (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2)), so $F_{\ast a}$ corresponds to $F'(a)$. This is also the differential $dF_a$ of [[§22 The Differential of a Map Between Vector Spaces|§22]]: in Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|§22.5]] with the identity coordinates $L = \mathrm{id}$ and $K = \mathrm{id}$, $dF_a = K^{-1} \circ F'(a) \circ L = F'(a)$.
>
> *The directional derivative.* Under the identification, $v = \sum_i v^i e_i$ corresponds to $D = \sum_i v^i\, \partial/\partial r^i|_a$. For a germ $[g]$ at $a$, since derivations are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]) and by the identity-chart partials above,
>
> $$
> D[g] = \sum_{i=1}^m v^i\, \frac{\partial}{\partial r^i}\Big|_a[g] = \sum_{i=1}^m v^i\, \frac{\partial g}{\partial r^i}(a) .
> $$
>
> For the second expression, apply the chain rule to $t \mapsto g(a + tv)$: the curve $c(t) = a + tv$ lies in the open domain of a representative $g$ for $|t|$ small, with $c(0) = a$ and $c'(0) = v$, so by the chain rule for a curve (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]])
>
> $$
> \frac{d}{dt}\Big|_{t=0} g(a + tv) = \nabla g(a) \cdot c'(0) = \sum_{i=1}^m \frac{\partial g}{\partial r^i}(a)\, v^i ,
> $$
>
> the same number. So $D$ is the directional derivative $D_v$.

^pf-30-5

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[Multivariable Chain Rule|452 §12.2]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]]

> [!remark]- Connections
> - The differential between vector spaces: [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]]; in calculus, [[§10 The Differential#^def-10-1|452 Def. §10.1]] and [[Directional Derivative Formula|452 §9.1 (Directional Derivative Formula)]].

> [!theorem] Corollary §30.6: The Tangent Space to a Vector Space
> Let $V$ be a finite-dimensional vector space with its standard smooth structure, and $a \in V$. The map
>
> $$
> V \to T_aV, \qquad v \mapsto D_v|_a, \qquad D_v|_a[f] = \frac{d}{dt}\Big|_{t=0} f(a + tv),
> $$
>
> is a linear isomorphism, defined without any choice of basis. For every linear map $L : V \to W$, $L_{*a}(D_v|_a) = D_{Lv}|_{La}$.
>
> *Lee: Proposition 3.13*

^cor-30-6

> [!proof]+ Proof
> Let $m = \dim V$. To show: $D_v|_a$ is a well-defined derivation at $a$; the transformation rule for linear $L$; that $v \mapsto D_v|_a$ is a linear isomorphism; and that no basis is involved.
>
> *Well defined on germs.* Let $b, w$ be vectors of a finite-dimensional vector space and $g$ smooth on an open neighbourhood of $b$. For $|t|$ small, $b + tw$ lies in that neighbourhood, and $t \mapsto g(b + tw)$ is smooth, as the composite of $g$ with the smooth curve $t \mapsto b + tw$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). Its derivative at $0$ depends only on the values of $g$ near $b$, hence only on the germ $[g]$. So $D_w|_b[g] = \frac{d}{dt}\big|_0\, g(b + tw)$ is a well-defined map on germs at $b$.
>
> *A computation on germs.* Let $L : V \to W$ be linear, $b, w \in V$, and $[g]$ a germ at $Lb$ on $W$. Since $L(b + tw) = Lb + t\,Lw$ by linearity,
>
> $$
> D_w|_b[g \circ L] = \frac{d}{dt}\Big|_{t=0} g\big(L(b + tw)\big) = \frac{d}{dt}\Big|_{t=0} g\big(Lb + t\,Lw\big) = D_{Lw}|_{Lb}[g] . \tag{A}
> $$
>
> *$D_v|_a$ is a derivation.* Choose a linear coordinate system $L_0 : V \to \mathbb{R}^m$. It is a chart of $V$ with domain $V$ and image $\mathbb{R}^m$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), hence a diffeomorphism $V \to \mathbb{R}^m$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), with linear inverse $L_0^{-1}$. Apply (A) to the linear map $L_0^{-1} : \mathbb{R}^m \to V$, at the point $b = L_0a$, with the vector $w = L_0v$: for every germ $[g]$ at $a$ on $V$,
>
> $$
> D_{L_0v}|_{L_0a}\big[g \circ L_0^{-1}\big] = D_v|_a[g] .
> $$
>
> By Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] (its second statement, on $\mathbb{R}^m$), $D_{L_0v}|_{L_0a} = \sum_i (L_0v)^i\, \partial/\partial r^i|_{L_0a}$, a linear combination of coordinate derivations (Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-1|§29.1]]), hence a derivation at $L_0a$. So by the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]) the left side is $\big((L_0^{-1})_{\ast L_0a} D_{L_0v}|_{L_0a}\big)[g]$, and
>
> $$
> D_v|_a = (L_0^{-1})_{\ast L_0a}\Big(\sum_{i=1}^m (L_0v)^i\, \frac{\partial}{\partial r^i}\Big|_{L_0a}\Big) . \tag{B}
> $$
>
> A pushforward of a derivation is a derivation (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]), here at $L_0^{-1}(L_0a) = a$. So $D_v|_a \in T_aV$.
>
> *Isomorphism.* By (B), $v \mapsto D_v|_a$ is the composite of three maps:
>
> $$
> V \xrightarrow{\ L_0\ } \mathbb{R}^m \longrightarrow T_{L_0a}\mathbb{R}^m \xrightarrow{\ (L_0^{-1})_{\ast L_0a}\ } T_aV, \qquad v \mapsto w = L_0v \mapsto \sum_i w^i\, \frac{\partial}{\partial r^i}\Big|_{L_0a} \mapsto D_v|_a .
> $$
>
> The first is a linear isomorphism (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|§22.1]]); the second is a linear isomorphism because the $\partial/\partial r^i|_{L_0a}$ form a basis of $T_{L_0a}\mathbb{R}^m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], identity chart); the third is a linear isomorphism because $L_0^{-1}$ is a diffeomorphism (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]). A composite of linear isomorphisms is one, so $v \mapsto D_v|_a$ is a linear isomorphism.
>
> *The rule for linear $L$.* A linear $L : V \to W$ is smooth: in linear coordinates $L_0$ on $V$ and $K$ on $W$ its coordinate representation $K \circ L \circ L_0^{-1}$ is linear, hence smooth (Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]). Both $L_{\ast a}(D_v|_a)$ and $D_{Lv}|_{La}$ are derivations at $La$ (by the previous steps, applied in $V$ and in $W$), and for every germ $[g]$ at $La$, by the definition of the pushforward and then (A),
>
> $$
> L_{\ast a}(D_v|_a)[g] = D_v|_a[g \circ L] = \frac{d}{dt}\Big|_0\, g(La + t\,Lv) = D_{Lv}|_{La}[g] .
> $$
>
> So $L_{\ast a}(D_v|_a) = D_{Lv}|_{La}$. In particular, for $L = L_0$, the isomorphism $(L_0)_{\ast a}$ carries $D_v|_a$ to $D_{L_0 v}|_{L_0 a}$, which is $\sum_i (L_0v)^i\,\partial/\partial r^i$ by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]: this is (B) read backwards, $(L_0)_{\ast a}$ being the inverse of $(L_0^{-1})_{\ast L_0a}$ (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]).
>
> *No basis.* The defining formula $D_v|_a[f] = \frac{d}{dt}\big|_0 f(a + tv)$ mentions no basis; the linear coordinates $L_0$ entered only in the proof.

^pf-30-6

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-1|§29.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]

> [!remark] Remark
> This is what licenses the shared notation $dF_p$: on open subsets of Euclidean spaces the abstract differential *is* the Jacobian, and between vector spaces it is the map of Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]]. It also closes a loop opened in [[§25 The Geometric Tangent Space#From Tangent Vectors to Derivations|§25, From Tangent Vectors to Derivations]], where a tangent vector $v$ was traded for the operator $D_v$; in $\mathbb{R}^n$ that trade is exactly the identification $e_i \leftrightarrow \partial/\partial r^i$.

^rem-30-3

> [!remark] Remark: Any Vector Space Will Do
> *Lecture 17.* Nothing above needs $\mathbb{R}^N$: the ambient space can be any finite-dimensional vector space $V$, because the velocity
>
> $$
> \gamma'(0) = \lim_{h \to 0} \frac{1}{h}\big(\gamma(h) - \gamma(0)\big)
> $$
>
> makes sense in any vector space with a topology in which to take the limit (“you could take it in a Banach space … if you're doing functional analysis”).

^rem-30-4

Moreover, all the tangent spaces of $V$ are identified with one another, and with $V$, by *translations*.

> [!definition] Definition §30.1: Translation
> Let $V$ be a finite-dimensional vector space and $p \in V$ (“I want to call it $p$ because I want to think of it as a point”). The **translation** by $p$ is
>
> $$
> \tau_p : V \to V, \qquad \tau_p(v) = v + p ,
> $$
>
> the unique translation mapping $0$ to $p$.

^def-30-1

> [!theorem] Proposition §30.7: Translations Identify the Tangent Spaces of a Vector Space
> Let $V$ be a finite-dimensional vector space and $p \in V$.
> 1. $\tau_p$ ([[§30 The Differential in Coordinates#^def-30-1|Definition §30.1]]) is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]] of $V$, with inverse $\tau_{-p}$.
> 2. $(\tau_p)_{\ast 0} : T_0V \to T_pV$ is a linear isomorphism, and $(\tau_p)_{\ast 0}\big(D_v|_0\big) = D_v|_p$ for every $v \in V$.
>
> So the composite $V \cong T_0V \to T_pV$ is $v \mapsto D_v|_p$, the identification of [[§30 The Differential in Coordinates#^cor-30-6|Corollary §30.6]].

^prop-30-7

> [!proof]+ Proof
> *(Lecture 17: “its pushforward is the identification”; filled in.)*
>
> *(1)* Fix a linear coordinate system $L : V \to \mathbb{R}^m$, a chart of $V$ with domain $V$ (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), and put $\tilde p = L(p)$. For $x \in \mathbb{R}^m$, by the definition of $\tau_p$ and the linearity of $L$,
>
> $$
> \big(L \circ \tau_p \circ L^{-1}\big)(x) = L\big(L^{-1}x + p\big) = x + \tilde p .
> $$
>
> So in linear coordinates $\tau_p$ is $x \mapsto x + \tilde p$, which is smooth; and $\tau_p = L^{-1} \circ (x \mapsto x + \tilde p) \circ L$ is continuous. By Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], $\tau_p$ is smooth. The same computation with $-p$ in place of $p$ shows that $\tau_{-p}$ is smooth, and $\tau_{-p}(\tau_p(v)) = v + p - p = v$, $\tau_p(\tau_{-p}(v)) = v - p + p = v$. So $\tau_p$ is a smooth bijection with smooth inverse $\tau_{-p}$, a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]).
>
> *(2)* Since $\tau_p(0) = p$, the pushforward goes $(\tau_p)_{\ast 0} : T_0V \to T_pV$. The pushforward along a diffeomorphism is a linear isomorphism (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], applied to $\tau_p$ by (1)). For $v \in V$ and $g$ smooth near $p$, by the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]), the definition of $D_v|_0$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]) together with $(g \circ \tau_p)(0 + tv) = g(tv + p)$, and the definition of $D_v|_p$,
>
> $$
> (\tau_p)_{\ast 0}\big(D_v|_0\big)[g] = D_v|_0[g \circ \tau_p] = \frac{d}{dt}\Big|_{t=0} g(p + tv) = D_v|_p[g] .
> $$
>
> Both sides are derivations at $p$ that take the same value on every germ, so $(\tau_p)_{\ast 0}(D_v|_0) = D_v|_p$.
>
> *The composite.* The identification $V \cong T_0V$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] is $v \mapsto D_v|_0$; following it by $(\tau_p)_{\ast 0}$ gives, by (2), $v \mapsto D_v|_0 \mapsto D_v|_p$, the identification of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] at $p$.

^pf-30-7

*Uses:* [[§30 The Differential in Coordinates#^def-30-1|Def. §30.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

“This is a canonical way to identify all of these tangent vectors. … That's what we did already”: a [[§25 The Geometric Tangent Space#^def-25-1|geometric tangent vector]] to the circle at $p$ was drawn as a vector in $\mathbb{R}^2$, which silently translates it back to the origin.

**Transcription note (Lecture 17).** Page 45 of the handwritten notes writes the identification as “$T_pM \cong T_0V \cong V$”; it is $T_pV \cong T_0V \cong V$.

Uribe added: “this is actually kind of like a left-invariant vector field. It is a left-invariant vector field.” For fixed $v$, the field $p \mapsto D_v|_p$ is the [[§54 Lie Groups and Left-Invariant Vector Fields#^def-54-3|left-invariant field]], with value $D_v|_0$ at the identity, of the [[§54 Lie Groups and Left-Invariant Vector Fields#^def-54-1|Lie group]] $(V, +)$ ([[§54 Lie Groups and Left-Invariant Vector Fields#^ex-54-2|Example §54.2]]).

> [!definition] Definition §30.2: Rank of a Smooth Map
> Let $F : M \to N$ be a smooth map. The **rank** of $F$ at $p$ is the rank of the linear map $F_{\ast p} : T_pM \to T_{F(p)}N$ of abstract tangent spaces; by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] it is the rank of the Jacobian of any coordinate representation.
>
> *Lee: Ch. 4 and Ch. 5, p. 105*

^def-30-2

> [!remark]- Connections
> - The rank of a matrix, in the Euclidean setting: [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]].

> [!definition] Definition §30.3: Regular Point of a Smooth Map
> Let $F : M \to N$ be a smooth map. A point $p$ is a **regular point** of $F$ if $F_{\ast p}$ is surjective.
>
> *Lee: Ch. 4 and Ch. 5, p. 105*

^def-30-3

> [!remark]- Connections
> - The Euclidean definition it extends: [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]]; restated with critical points in [[§36 Submersions#^def-36-3|Def. §36.3]].
> - A regular point is a point where $F$ is a submersion: [[§36 Submersions#^def-36-1|Def. §36.1]].

> [!definition] Definition §30.4: Regular Value of a Smooth Map
> Let $F : M \to N$ be a smooth map. A value $c \in N$ is a **regular value** if every $p \in F^{-1}(c)$ is a regular point ([[§30 The Differential in Coordinates#^def-30-3|Definition §30.3]]).
>
> *Lee: Ch. 4 and Ch. 5, p. 105*

^def-30-4

> [!remark]- Connections
> - The Euclidean definition it extends: [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]]; restated with critical values in [[§36 Submersions#^def-36-4|Def. §36.4]].

> [!remark] Remark: The Map Is Intrinsic — the Matrix Is Not
> Uribe's closing point. The linear map $F_{\ast p}$ is defined with no choices, but its matrix depends on both charts: by Corollary [[§30 The Differential in Coordinates#^cor-30-4|§30.4]], changing them multiplies the matrix on each side by the Jacobian of a transition function. So only properties of $F_{\ast p}$ that survive such changes — its rank, kernel and image, injectivity and surjectivity — are properties of $F$, which is why the definition above is phrased through $F_{\ast p}$ rather than through a matrix. By Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] it agrees with Definitions [[§7 The Regular Value Theorem#^def-7-3|§7.3]] and [[§7 The Regular Value Theorem#^def-7-4|§7.4]] in the Euclidean case. A regular point is exactly a point at which $F$ is a *submersion*, in the sense of Definition [[§36 Submersions#^def-36-1|§36.1]]; maps with bijective, surjective and injective differentials are the subject of [[§35 Local Diffeomorphisms|§35]].

^rem-30-5

> [!theorem] Proposition §30.8: Regular Values Inside One Chart
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$. Suppose there are smooth charts $(U, \varphi)$ of $M$ and $(V, \psi)$ of $N$ with
>
> $$
> F^{-1}(c) \subseteq U, \qquad c \in V, \qquad F(U) \subseteq V .
> $$
>
> Let $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ be the coordinate representation of $F$, a smooth map on the open set $\varphi(U) \subseteq \mathbb{R}^m$, and put $\tilde c = \psi(c) \in \mathbb{R}^n$. Then:
> 1. $\varphi$ restricts to a homeomorphism from the level set $F^{-1}(c) \subseteq M$ onto the Euclidean level set $\tilde F^{-1}(\tilde c) \subseteq \varphi(U)$;
> 2. $c$ is a regular value of $F$ in the sense of Definition [[§30 The Differential in Coordinates#^def-30-4|§30.4]] if and only if $\tilde c$ is a regular value of $\tilde F$ in the sense of Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]];
> 3. in that case $F^{-1}(c)$ is a topological manifold of dimension $m - n$.

^prop-30-8

> [!proof]+ Proof
> *(1)* Let $x \in \varphi(U)$ and $q = \varphi^{-1}(x) \in U$. Then $F(q) \in F(U) \subseteq V$ and $c \in V$, and $\psi$ is injective on $V$; with the definitions $\tilde F = \psi \circ F \circ \varphi^{-1}$ and $\tilde c = \psi(c)$,
>
> $$
> \tilde F(x) = \tilde c \iff \psi\big(F(q)\big) = \psi(c) \iff F(q) = c .
> $$
>
> So $x \in \tilde F^{-1}(\tilde c)$ exactly when $\varphi^{-1}(x) \in F^{-1}(c)$; as $\varphi : U \to \varphi(U)$ is a bijection, this says $\varphi\big(F^{-1}(c) \cap U\big) = \tilde F^{-1}(\tilde c)$. And $F^{-1}(c) \cap U = F^{-1}(c)$ by the hypothesis $F^{-1}(c) \subseteq U$. A homeomorphism restricts to a homeomorphism from any subset onto its image, both with the subspace topology (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](3)); applied to the chart $\varphi : U \to \varphi(U)$ and the subset $F^{-1}(c)$, it gives the homeomorphism $F^{-1}(c) \to \tilde F^{-1}(\tilde c)$.
>
> *(2)* The map $\tilde F$ is smooth on the open set $\varphi(U)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]), so its Jacobian is defined. Let $p \in F^{-1}(c)$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], the matrix of $F_{\ast p}$ in the coordinate bases of the two charts is the Jacobian $\tilde F'(\varphi(p))$. A linear map $A : T_pM \to T_{F(p)}N$ is surjective exactly when its image, a subspace of dimension $\operatorname{rank} A$, is all of the $n$-dimensional target, i.e. when $\operatorname{rank} A = n$; and $\operatorname{rank} A$ is the rank of its matrix (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)). So
>
> $$
> F_{\ast p} \text{ surjective} \iff \operatorname{rank} \tilde F'\big(\varphi(p)\big) = n \iff \tilde F'\big(\varphi(p)\big) : \mathbb{R}^m \to \mathbb{R}^n \text{ surjective}:
> $$
>
> $p$ is a regular point of $F$ (Definition [[§30 The Differential in Coordinates#^def-30-3|§30.3]]) if and only if $\varphi(p)$ is a regular point of $\tilde F$ (Definition [[§7 The Regular Value Theorem#^def-7-3|§7.3]], applied to $\tilde F$ on $\varphi(U)$). By (1), $p$ runs over $F^{-1}(c)$ exactly as $\varphi(p)$ runs over $\tilde F^{-1}(\tilde c)$. Hence every point of $F^{-1}(c)$ is a regular point of $F$ — that is, $c$ is a regular value of $F$ (Definition [[§30 The Differential in Coordinates#^def-30-4|§30.4]]) — if and only if every point of $\tilde F^{-1}(\tilde c)$ is a regular point of $\tilde F$ — that is, $\tilde c$ is a regular value of $\tilde F$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]).
>
> *(3)* If $F^{-1}(c)$ is empty there is nothing to prove. Otherwise, at a point $p$ of it $F_{\ast p} : T_pM \to T_{F(p)}N$ is surjective, so $m \ge n$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)). By (2), $\tilde c$ is a regular value of the smooth map $\tilde F$ on the open set $\varphi(U) \subseteq \mathbb{R}^m$, so Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], applied with $k = n$ and $m - n$ in place of its $n$ (so that $\mathbb{R}^{n+k}$ becomes $\mathbb{R}^m$), shows that the Euclidean level set $\tilde F^{-1}(\tilde c)$ is a topological manifold of dimension $m - n$. By (1), $F^{-1}(c)$ is homeomorphic to it, and being a topological manifold of a given dimension is preserved by homeomorphisms: second countability, the Hausdorff property and local Euclideanness (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]) are all defined through open sets, which a homeomorphism matches up.

^pf-30-8

*Uses:* [[§30 The Differential in Coordinates#^def-30-3|Def. §30.3]], [[§30 The Differential in Coordinates#^def-30-2|Def. §30.2]], [[§30 The Differential in Coordinates#^def-30-4|Def. §30.4]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], [[§10 Continuous Functions#^prop-10-3|590 §10.3]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]]

![[m591-12-13.svg]]
*The proposition in one square. The level set upstairs is carried by the chart onto a level set downstairs, in Euclidean space, and the question “is $c$ regular?” is carried with it: surjectivity of $F_{\ast p}$ upstairs is the rank of $\tilde F'$ downstairs.*

> [!remark] Remark: The Strategy
> To show that $c$ is a regular value of a map between manifolds, and to see its level set:
> 1. *Locate the level set.* Show that $F^{-1}(c)$ lies inside a single chart domain $U$, and that $F(U)$ lies in a chart domain $V$ around $c$.
> 2. *Go downstairs.* Write the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$, an ordinary map between open subsets of Euclidean spaces.
> 3. *Compute as in [[§7 The Regular Value Theorem|§7]].* Check that the Jacobian of $\tilde F$ has full rank $n$ at every point of the Euclidean level set $\tilde F^{-1}(\tilde c)$.
> 4. *Come back up.* By Proposition [[§30 The Differential in Coordinates#^prop-30-8|§30.8]], $c$ is a regular value of $F$, and $F^{-1}(c)$ is homeomorphic, through the chart, to a Euclidean regular level set: a manifold of dimension $\dim M - \dim N$.
>
> Assignment 3, Problem 4 is exactly this. For the moment map $F : \mathbb{CP}^n \to \mathbb{R}^n$ and $c$ in the interior of the simplex, every point of $F^{-1}(c)$ has all homogeneous coordinates nonzero, so $F^{-1}(c) \subseteq U_0$ (step 1). The target chart is the identity of $\mathbb{R}^n$, and $\varphi_0(U_0) = \mathbb{C}^n \cong \mathbb{R}^{2n}$, so $\tilde F$ is an explicit rational map $\mathbb{R}^{2n} \to \mathbb{R}^n$ (step 2). Its Jacobian has rank $n$ on the level set (step 3). So the fibre is an $n$-dimensional manifold (step 4) — in this case a regular level set of $\mathbb{R}^{2n}$ itself, exactly the situation of [[§7 The Regular Value Theorem|§7]]. When a level set does not fit in one chart, the same argument applies around each of its points separately, as the next corollary shows.

^rem-30-6

Complex projective space through the course: the open quotient $S^{2n+1}/S^1$, Hausdorff, second countable and compact, in [[§9 Complex Projective Space|Complex Projective Space]]; the circle group $\mathrm{U}(1)$ acting there in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; an orbit space in [[§13 Group Actions and Orbit Spaces#^ex-13-3|projective space as an orbit space]]; a smooth and complex manifold through its standard atlas in [[§18 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; a homogeneous space of $\mathrm{U}(n+1)$ in [[§25 The Geometric Tangent Space#^rem-25-9|Dimension Checks through Homogeneous Spaces]]; the domain of the moment map in [[§30 The Differential in Coordinates#^rem-30-6|Remark: The Strategy]]; and the base of the Hopf fibration in [[§42 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]].

> [!theorem] Corollary §30.9: Regular Level Sets Are Topological Manifolds
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$ a regular value of $F$. Then $F^{-1}(c)$, with the subspace topology, is a topological manifold of dimension $m - n$ (or empty).

^cor-30-9

> [!proof]+ Proof
> By Definition [[§2 Topological Manifolds#^def-2-2|§2.2]], three properties of $F^{-1}(c)$, with the subspace topology, must be shown: Hausdorff, second countable, and locally Euclidean of dimension $m - n$.
>
> *Hausdorff and second countable.* Both are inherited from $M$ (Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]).
>
> *Locally Euclidean.* Let $p \in F^{-1}(c)$. Choose smooth charts $(V, \psi)$ around $c$ and $(U_0, \varphi_0)$ around $p$, and put $U = U_0 \cap F^{-1}(V)$, an open neighbourhood of $p$ because $F$ is continuous and $F(p) = c \in V$; restricting $\varphi_0$ gives a smooth chart $(U, \varphi)$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]]). Apply Proposition [[§30 The Differential in Coordinates#^prop-30-8|§30.8]] to the restriction $F|_U : U \to N$, a smooth map on the open submanifold $U$ (of dimension $m$), with the charts $(U, \varphi)$ and $(V, \psi)$. Its hypotheses hold:
> - its level set $(F|_U)^{-1}(c) = F^{-1}(c) \cap U$ lies in $U$;
> - $c \in V$;
> - it maps $U$ into $V$, because $U \subseteq F^{-1}(V)$.
>
> And $c$ is still a regular value of $F|_U$. Indeed, $F|_U = F \circ \iota$ with $\iota : U \hookrightarrow M$ the inclusion, so for $q \in F^{-1}(c) \cap U$ the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) gives $(F|_U)_{\ast q} = F_{\ast q} \circ \iota_{\ast q}$; since $\iota_{\ast q}$ is the isomorphism by which $T_qU = T_qM$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), $(F|_U)_{\ast q} = F_{\ast q}$ under this identification, and it is surjective because $q \in F^{-1}(c)$ is a regular point of $F$. By Proposition [[§30 The Differential in Coordinates#^prop-30-8|§30.8]](3), $F^{-1}(c) \cap U$ is a topological manifold of dimension $m - n$.
>
> It remains to place this inside $F^{-1}(c)$. The set $F^{-1}(c) \cap U$ is open in $F^{-1}(c)$, being the intersection of $F^{-1}(c)$ with the open set $U$ of $M$ (Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]), and its topology as a subspace of $U$ and as a subspace of $F^{-1}(c)$ are both the subspace topology from $M$. A chart of the manifold $F^{-1}(c) \cap U$ at $p$ has a domain open in $F^{-1}(c) \cap U$, hence open in $F^{-1}(c)$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). So $p$ has a neighbourhood in $F^{-1}(c)$ homeomorphic to an open subset of $\mathbb{R}^{m-n}$.

^pf-30-9

*Uses:* [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§30 The Differential in Coordinates#^prop-30-8|§30.8]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§30 The Differential in Coordinates#^def-30-4|Def. §30.4]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

> [!remark]- Connections
> - The smooth half, $F^{-1}(c)$ a submanifold with tangent space $\ker F_{*p}$: [[§37 Regular Submanifolds#^thm-37-7|§37.7]]; the Euclidean original: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].

This is the topological half of the regular value theorem for manifolds, and it is [[§7 The Regular Value Theorem|§7]] applied chart by chart. The smooth half — that $F^{-1}(c)$ is a smooth *submanifold* of $M$, with tangent space $\ker F_{\ast p}$ — came in Lecture 12, as Theorem [[§37 Regular Submanifolds#^thm-37-7|§37.7]], proved with the local normal form for submersions (Theorem [[§36 Submersions#^thm-36-4|§36.4]]): near each point of the level set, $F$ is a projection, so the level set is a coordinate slice. It is Lee's Corollary 5.14 and Proposition 5.38. The corollary above is now a consequence of it, a submanifold being in particular a topological manifold, but its proof — [[§7 The Regular Value Theorem|§7]] applied chart by chart — is more elementary.

> [!theorem] Proposition §30.10: Maps with Zero Differential Are Constant
> Let $F : M \to N$ be smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]), with $M$ connected ([[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]). If $F_{\ast p} = 0$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]]) for every $p \in M$, then $F$ is constant.

^prop-30-10

> [!proof]+ Proof
> *(Assignment 4, Problem 1: the submitted solution, condensed.)* Two steps: first, every point has an open neighbourhood on which $F$ is constant; second, a map with this property on a connected space is constant. (If $M$ is empty there is nothing to prove.)
>
> *$F$ is locally constant.* Fix $p_0 \in M$.
>
> *Charts.* Take a chart $(V, \psi)$ at $F(p_0)$ and a chart $(U_1, \varphi_1)$ at $p_0$. The set $U_2 = U_1 \cap F^{-1}(V)$ is open, since $F$ is continuous, and contains $p_0$. Its image $\varphi_1(U_2)$ is open in $\mathbb{R}^m$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)) and contains $\varphi_1(p_0)$, so it contains an open ball $B$ centred at $\varphi_1(p_0)$. Put $U_0 = \varphi_1^{-1}(B)$ and $\varphi = \varphi_1|_{U_0}$: a chart at $p_0$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)) whose image is the ball $B$ and whose domain satisfies $F(U_0) \subseteq V$ — shrink by continuity of $F$, then to a ball.
>
> *Zero Jacobian.* The coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1} : B \to \mathbb{R}^n$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]). For $p \in U_0$, the matrix of $F_{\ast p}$ in the coordinate bases is the Jacobian $\tilde F'(\varphi(p))$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]). By hypothesis $F_{\ast p} = 0$, which sends every basis vector to $0$, so every entry of its matrix is $0$. As $p$ runs over $U_0$, $\varphi(p)$ runs over $B$; so $\tilde F' \equiv 0$ on $B$, that is, $\partial \tilde F^j/\partial r^i = 0$ on $B$ for all $i$ and $j$.
>
> *Mean value theorem.* Let $p \in U_0$, and put $a = \varphi(p_0)$ and $b = \varphi(p)$. The ball $B$ is convex, so the segment $\sigma(s) = a + s\,(b - a)$, $s \in [0, 1]$, stays in $B$ (and, $B$ being open, $\sigma$ stays in $B$ for $s$ in an open interval containing $[0,1]$). For each $j$, the function $h_j(s) = \tilde F^j(\sigma(s))$ is differentiable there, and by the chain rule for a curve (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]])
>
> $$
> h_j'(s) = \sum_{i=1}^m \frac{\partial \tilde F^j}{\partial r^i}\big(\sigma(s)\big)\,(b^i - a^i) = 0 .
> $$
>
> The mean value theorem gives some $\xi \in (0,1)$ with $h_j(1) - h_j(0) = h_j'(\xi)\,(1 - 0) = 0$, so $\tilde F^j(b) = \tilde F^j(a)$ for every $j$. Hence
>
> $$
> \psi\big(F(p)\big) = \tilde F\big(\varphi(p)\big) = \tilde F\big(\varphi(p_0)\big) = \psi\big(F(p_0)\big),
> $$
>
> and since $F(p), F(p_0) \in V$ and $\psi$ is injective on $V$, $F(p) = F(p_0)$. So $F$ is constant on the open neighbourhood $U_0$ of $p_0$.
>
> *$F$ is constant.* Let $c = F(p_0)$ and $A = F^{-1}(c)$.
> - $A$ is closed. $N$ is Hausdorff (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]), so each $q \ne c$ has a neighbourhood not containing $c$ (Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]]); thus $N \setminus \{c\}$ is open and $\{c\}$ is closed, and $A = F^{-1}(\{c\})$ is closed since $F$ is continuous.
> - $A$ is open. If $q \in A$, the first step at $q$ gives an open $U_q \ni q$ with $F \equiv F(q) = c$ on $U_q$, so $U_q \subseteq A$.
> - $A$ is nonempty: $p_0 \in A$.
>
> Then $A$ and $M \setminus A$ are disjoint open sets with union $M$. As $M$ is connected, one of them is empty, and $A \ne \emptyset$; so $M \setminus A = \emptyset$, that is, $F^{-1}(c) = M$.

^pf-30-10

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 The Mean Value Theorem#^thm-29-3|451 §29.3]], [[§10 Continuous Functions#^thm-10-1|590 §10.1]], [[§15 Connected Spaces#^lem-15-1|590 §15.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]]

> [!remark]- Connections
> - Connectedness via clopen sets: [[§15 Connected Spaces#^lem-15-1|590 Lem. §15.1]]; the one-variable original: [[§29 The Mean Value Theorem#^cor-29-4|451 §29.4]] (vanishing derivative means constant).

The hypothesis that $M$ is connected cannot be dropped: on a disconnected $M$, a map that takes different constant values on different components has zero differential everywhere. Locally, the proposition is the familiar fact from calculus that a function with zero derivative on an interval is constant.
