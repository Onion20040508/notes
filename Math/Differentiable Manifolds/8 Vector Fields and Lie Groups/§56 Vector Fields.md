---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 56
tags: [differentiable-manifolds, math591]
---
← [[§55 Morse Functions and the Zero Section]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§57 Differential Operators]] →

*Stage: fields — Smooth sections of $TM$, a tangent vector at every point — and vector fields acting on functions, as derivations of $C^\infty(M)$.*

*Lecture 15: “now we want to start a big chapter, new chapter, and now it is on vector fields.” References: Lee Ch. 8. The definition itself was given in Lectures 12 and 13, with the tangent bundle; Lecture 15 restated it “analogously” to one-forms.*

## Vector Fields and Their Coordinates

> [!definition] Definition §56.1: Vector Field
> A **vector field** on $M$ is a smooth map
>
> $$
> \mathbf{X} : M \longrightarrow TM
> $$
>
> such that
>
> $$
> \mathbf{X}(p) \in T_pM \qquad \text{for every } p \in M .
> $$
>
> Equivalently, $\pi \circ \mathbf{X} = \mathrm{id}_M$ for the projection $\pi : TM \to M$: a vector field is a section of the tangent bundle ([[§40 Fibrations#^def-40-3|Definition §40.3]]).
>
> *Lee: Ch. 8, Vector Fields*

^def-56-1

In words: a vector field chooses one tangent vector at every point of $M$, and the choice varies smoothly — “for every point, [it] selects a tangent vector at that point.”

![[m591-44-2.svg]]
*A vector field in two pictures, on the circle $M = S^1$ with $\mathbf{X} = c(\theta)\,\partial/\partial\theta$, $c(\theta) = 0.55 + 0.35\sin\theta$. Left: the usual picture, an arrow $\mathbf{X}(p)$ at each point $p$. Right: the tangent bundle $TS^1$, with $S^1$ cut open at $(1,0)$; each fibre $T_pM$ is a vertical line over $p$, and the height of a point on it measures the vector $c\,\partial/\partial\theta$ (above the dashed zero section: counterclockwise). The vector field is the curve $\mathbf{X}(M)$, which meets every fibre exactly once — that is the condition $\mathbf{X}(p) \in T_pM$ — and $\pi \circ \mathbf{X} = \mathrm{id}_M$ says that the point of the curve above $p$ projects back to $p$. The points $p_1, p_2, p_3$ carry the same colour in both pictures.*

![[m591-44-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The two pictures of the figure joined, in 3D, for the same field $c(\theta) = 0.55 + 0.35\sin\theta$. Each arrow $\mathbf{X}(p)$, tangent to the circle, turns up into its fibre $T_pS^1$, now vertical, so $TS^1$ becomes a cylinder and the arrow's length becomes a height; the tips form the section $\mathbf{X}(S^1)$ (green). Then the field changes (a family chosen for the picture): the section rises and falls with the arrows, and where it crosses the circle (the zero section) the field vanishes and the arrows flip (red).

![[m591-44-a3.gif|500]]

*(Not from lecture; animation added, vault only.)* The figure's two pictures side by side, with the field changing (the same family as above, starting from the figure's $c(\theta) = 0.55 + 0.35\sin\theta$). Left: arrows on $S^1$, those at $p_1, p_2, p_3$ in colour. Right: the flattened $TS^1$, the circle cut open at $(1, 0)$, each fibre a vertical line (the fibres over $p_1, p_2, p_3$ in colour), and the field as the section (black). Each coloured dot's height is the signed length of the arrow of the same colour. Where the section crosses the zero section (red rings), the arrows on the left vanish at the same points.

> [!remark]- Connections
> - Vector fields on open subsets of $\mathbb{R}^3$ in 452: [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §13]].
> - Computational version: vector fields on regions of $\mathbb{R}^2$ and $\mathbb{R}^3$ in calculus, [[§125 Vector Fields#^def-125-1|Calc Def. §125.1]] and [[§125 Vector Fields#^def-125-2|Calc Def. §125.2]].

**Transcription note.** Page 36 of the handwritten notes writes “Section of $TM \xrightarrow{F} M$”; the map is the projection $\pi$.

**Notation.** The value of a vector field $\mathbf{X}$ ([[§56 Vector Fields#^def-56-1|Definition §56.1]]) at $p$ is written $\mathbf{X}_p \in T_pM$, again with $p$ as a subscript, to make room for the function a tangent vector acts on.

> [!definition] Definition §56.2: The Space of Vector Fields
> The set of all vector fields on $M$ is denoted
>
> $$
> \mathfrak{X}(M) \qquad \big(\text{LaTeX: } \mathtt{\backslash mathfrak\{X\}}\big).
> $$
>
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ and $c \in \mathbb{R}$, the sum and the scalar multiple are defined pointwise, in the vector space $T_pM$:
>
> $$
> (\mathbf{X} + \mathbf{Y})_p = \mathbf{X}_p + \mathbf{Y}_p, \qquad (c\mathbf{X})_p = c\, \mathbf{X}_p, \qquad p \in M .
> $$
>
> Proposition [[§56 Vector Fields#^prop-56-2|§56.2]] shows that these are again vector fields and that $\mathfrak{X}(M)$ is a real vector space. Multiplying by a function rather than a constant is the next definition.
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-56-2

> [!definition] Definition §56.3: Product of a Function and a Vector Field
> For $f \in C^\infty(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, the product $f\mathbf{X}$ is defined pointwise:
>
> $$
> (f\mathbf{X})_p = f(p)\, \mathbf{X}_p \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-56-3

> [!theorem] Proposition §56.1: Vector Fields in Coordinates
> Let $\mathbf{X}$ be a section of $TM$ (not assumed smooth), $m = \dim M$, and $(U, \varphi = (x^1, \ldots, x^m))$ a chart *of $M$*: $U \subseteq M$ open, with coordinate functions $x^j : U \to \mathbb{R}$. Then on $U$
>
> $$
> \mathbf{X} = \sum_{j=1}^m \mathbf{X}^j\, \frac{\partial}{\partial x^j}, \qquad \mathbf{X}^j(p) = \mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p),
> $$
>
> where $\partial/\partial x^j$ is the coordinate vector field of the chart ($p \mapsto \partial/\partial x^j|_p \in T_pM$) and the coefficients $\mathbf{X}^j : U \to \mathbb{R}$ are functions on $U \subseteq M$. Moreover $\mathbf{X}$ is smooth on $U$ if and only if the coefficient functions $\mathbf{X}^1, \ldots, \mathbf{X}^m$ are smooth on $U$; smoothness of $\mathbf{X} : U \to TU$ is tested in the chart $\tilde\varphi$ of $TM$ induced by $\varphi$ (Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]]), whose $2m$ coordinates are $x^1, \ldots, x^m$ and the components $v^j = dx^j(v)$.
>
> *Lee: Proposition 8.1*

^prop-56-1

> [!proof]+ Proof
> *(Stated in Lecture 15, “analogously” to one-forms; filled in.)* Three things are claimed: the expansion of $\mathbf{X}$ at each point of $U$, the two formulas for its coefficients, and the smoothness criterion.
>
> *The expansion.* Fix $p \in U$. Since $\mathbf{X}$ is a section of $TM$, $\mathbf{X}_p \in T_pM$ is a derivation at $p$. The universal formula of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], applied to $D = \mathbf{X}_p$, gives
>
> $$
> \mathbf{X}_p = \sum_{j=1}^m \mathbf{X}_p[x^j]\, \frac{\partial}{\partial x^j}\Big|_p = \sum_{j=1}^m \mathbf{X}^j(p)\, \frac{\partial}{\partial x^j}\Big|_p , \qquad \mathbf{X}^j(p) := \mathbf{X}_p[x^j] .
> $$
>
> By Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] with $f = x^j$ and $D = \mathbf{X}_p$, $\mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p)$, which is the second formula for $\mathbf{X}^j(p)$. As $p \in U$ was arbitrary, $\mathbf{X} = \sum_j \mathbf{X}^j\, \partial/\partial x^j$ on $U$, the equality holding at every point.
>
> *The coordinate representation.* For $p \in U$ the point $\mathbf{X}(p) = (p, \mathbf{X}_p)$ of $TM$ lies over $p \in U$, so $\mathbf{X}$ maps $U$ into $TU = \pi^{-1}(U)$ (Definition [[§51 The Tangent Bundle#^def-51-4|§51.4]]), the domain of the chart $\tilde\varphi$ of $TM$ (Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]]). That chart sends $(p, v)$ to $\big(x^1(p), \ldots, x^m(p), v[x^1], \ldots, v[x^m]\big)$. Let $r \in \varphi(U)$ and $p = \varphi^{-1}(r)$; then $(x^1(p), \ldots, x^m(p)) = \varphi(p) = r$, and for $v = \mathbf{X}_p$ the last $m$ entries are $\mathbf{X}_p[x^j] = \mathbf{X}^j(p)$. Hence
>
> $$
> \tilde\varphi \circ \mathbf{X} \circ \varphi^{-1}(r) = \big(r,\ \mathbf{X}^1(\varphi^{-1}(r)), \ldots, \mathbf{X}^m(\varphi^{-1}(r))\big), \qquad r \in \varphi(U) .
> $$
>
> A map into $\mathbb{R}^{2m}$ is smooth if and only if each of its $2m$ components is; the first $m$ components $r \mapsto r^i$ are smooth, so this coordinate representation is smooth exactly when every $\mathbf{X}^j \circ \varphi^{-1}$ is smooth on $\varphi(U)$.
>
> *Smooth $\Rightarrow$ smooth coefficients.* Suppose $\mathbf{X}$ is smooth on $U$, i.e. $\mathbf{X}|_U : U \to TM$ is smooth, $U$ being an open submanifold (Definition [[§3 Subspaces and Products#^def-3-2|§3.2]]). Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], applied to the chart $(U, \varphi)$ of $U$ and the chart $(TU, \tilde\varphi)$ of $TM$ (Proposition [[§51 The Tangent Bundle#^prop-51-2|§51.2]]), with $\mathbf{X}(U) \subseteq TU$, says that the coordinate representation above is smooth. So every $\mathbf{X}^j \circ \varphi^{-1} = (\mathbf{X}^j)_\varphi$ is smooth on $\varphi(U)$, and by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]], tested with the chart $(U, \varphi)$ at every point of $U$, each $\mathbf{X}^j$ is smooth on $U$.
>
> *Smooth coefficients $\Rightarrow$ smooth.* Suppose every $\mathbf{X}^j$ is smooth on $U$. By Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], applied in the chart $(U, \varphi)$, every $\mathbf{X}^j \circ \varphi^{-1}$ is smooth on $\varphi(U)$, so the coordinate representation is smooth. $\mathbf{X}|_U$ is also continuous: on $U$,
>
> $$
> \mathbf{X} = \tilde\varphi^{-1} \circ \big(\tilde\varphi \circ \mathbf{X} \circ \varphi^{-1}\big) \circ \varphi ,
> $$
>
> a composite of continuous maps ($\varphi$ is a homeomorphism onto $\varphi(U)$, the middle map is smooth, and $\tilde\varphi^{-1}$ is continuous by Proposition [[§51 The Tangent Bundle#^prop-51-3|§51.3]]). So Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]] holds at every $p \in U$ with the charts $(U, \varphi)$ and $(TU, \tilde\varphi)$: $\mathbf{X}$ is smooth on $U$.

^pf-56-1

*Uses:* [[§56 Vector Fields#^def-56-1|Def. §56.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§51 The Tangent Bundle#^def-51-4|Def. §51.4]], [[§51 The Tangent Bundle#^prop-51-2|§51.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§51 The Tangent Bundle#^def-51-5|Def. §51.5]], [[§3 Subspaces and Products#^def-3-2|Def. §3.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§51 The Tangent Bundle#^prop-51-3|§51.3]]

> [!theorem] Proposition §56.2: The Space of Vector Fields Is a Real Vector Space
> Let $M$ be a smooth manifold.
> 1. If $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ and $c \in \mathbb{R}$, then $\mathbf{X} + \mathbf{Y}$ and $c\mathbf{X}$ ([[§56 Vector Fields#^def-56-2|Definition §56.2]]) are [[§56 Vector Fields#^def-56-1|vector fields]].
> 2. The zero field $\mathbf{0}$, $\mathbf{0}_p = 0_p \in T_pM$, is a vector field.
> 3. With these operations $\mathfrak{X}(M)$ is a real vector space, with zero vector $\mathbf{0}$ and additive inverse $-\mathbf{X} = (-1)\mathbf{X}$.
> 4. More generally, if $f \in C^\infty(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, then $f\mathbf{X}$ ([[§56 Vector Fields#^def-56-3|Definition §56.3]]) is a vector field.

^prop-56-2

> [!proof]+ Proof
> *(Not from lecture: the notes stated the vector-space structure without proof; filled in.)* *The operations give sections.* At each $p$, $\mathbf{X}_p + \mathbf{Y}_p$, $c\,\mathbf{X}_p$, $f(p)\,\mathbf{X}_p$ and $0_p$ lie in $T_pM$, a real vector space ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]]); so each of $\mathbf{X} + \mathbf{Y}$, $c\mathbf{X}$, $f\mathbf{X}$, $\mathbf{0}$ assigns to every $p$ a tangent vector at $p$, a section of $TM$.
>
> *(1), (2), (4): smoothness.* Let $(U, (x^j))$ be a chart. By [[§56 Vector Fields#^prop-56-1|Proposition §56.1]], $\mathbf{X} = \sum_j \mathbf{X}^j\, \partial/\partial x^j$ and $\mathbf{Y} = \sum_j \mathbf{Y}^j\, \partial/\partial x^j$ on $U$ with smooth coefficients. At each $p \in U$, by linearity in $T_pM$,
>
> $$
> (\mathbf{X} + \mathbf{Y})_p = \sum_j \big(\mathbf{X}^j(p) + \mathbf{Y}^j(p)\big) \frac{\partial}{\partial x^j}\Big|_p, \qquad (f\mathbf{X})_p = \sum_j f(p)\, \mathbf{X}^j(p)\, \frac{\partial}{\partial x^j}\Big|_p, \qquad \mathbf{0}_p = \sum_j 0 \cdot \frac{\partial}{\partial x^j}\Big|_p ,
> $$
>
> so the coefficients of $\mathbf{X} + \mathbf{Y}$, $f\mathbf{X}$ and $\mathbf{0}$ are $\mathbf{X}^j + \mathbf{Y}^j$, $f\mathbf{X}^j$ and $0$, smooth on $U$ as sums and products of smooth functions. By [[§56 Vector Fields#^prop-56-1|Proposition §56.1]] again these sections are smooth on $U$; the chart domains cover $M$, and smoothness is local, so they are smooth. The scalar multiple $c\mathbf{X}$ is the case $f \equiv c$ of (4).
>
> *(3): the axioms.* Each axiom is an equality of vector fields, that is, of their values at every $p \in M$, and there it is the corresponding axiom of the vector space $T_pM$. Explicitly, for $\mathbf{X}, \mathbf{Y}, \mathbf{Z} \in \mathfrak{X}(M)$, $a, b \in \mathbb{R}$ and every $p \in M$:
> - commutativity: $(\mathbf{X} + \mathbf{Y})_p = \mathbf{X}_p + \mathbf{Y}_p = \mathbf{Y}_p + \mathbf{X}_p = (\mathbf{Y} + \mathbf{X})_p$;
> - associativity: $\big((\mathbf{X} + \mathbf{Y}) + \mathbf{Z}\big)_p = (\mathbf{X}_p + \mathbf{Y}_p) + \mathbf{Z}_p = \mathbf{X}_p + (\mathbf{Y}_p + \mathbf{Z}_p) = \big(\mathbf{X} + (\mathbf{Y} + \mathbf{Z})\big)_p$;
> - zero: $(\mathbf{X} + \mathbf{0})_p = \mathbf{X}_p + 0_p = \mathbf{X}_p$;
> - inverses: $\big(\mathbf{X} + (-1)\mathbf{X}\big)_p = \mathbf{X}_p - \mathbf{X}_p = 0_p = \mathbf{0}_p$;
> - unit: $(1\mathbf{X})_p = 1 \cdot \mathbf{X}_p = \mathbf{X}_p$;
> - compatibility: $\big((ab)\mathbf{X}\big)_p = (ab)\,\mathbf{X}_p = a\,(b\,\mathbf{X}_p) = \big(a(b\mathbf{X})\big)_p$;
> - distributivity: $\big(a(\mathbf{X} + \mathbf{Y})\big)_p = a\,\mathbf{X}_p + a\,\mathbf{Y}_p = (a\mathbf{X} + a\mathbf{Y})_p$ and $\big((a + b)\mathbf{X}\big)_p = a\,\mathbf{X}_p + b\,\mathbf{X}_p = (a\mathbf{X} + b\mathbf{X})_p$.
>
> So $\mathfrak{X}(M)$ is a real vector space.

^pf-56-2

*Uses:* [[§56 Vector Fields#^def-56-1|Def. §56.1]], [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§56 Vector Fields#^prop-56-1|§56.1]]

By (4), $\mathfrak{X}(M)$ is moreover a module over the ring $C^\infty(M)$ — the same pointwise check gives $(fg)\mathbf{X} = f(g\mathbf{X})$, $(f + g)\mathbf{X} = f\mathbf{X} + g\mathbf{X}$ and $f(\mathbf{X} + \mathbf{Y}) = f\mathbf{X} + f\mathbf{Y}$ — which is what Uribe meant by “an algebra over the smooth functions” in Lecture 17. It is infinite-dimensional as a real vector space (for $\dim M \ge 1$), but over $C^\infty(U)$ the fields on a chart domain $U$ have the basis $\partial/\partial x^1, \ldots, \partial/\partial x^m$ ([[§56 Vector Fields#^prop-56-1|Proposition §56.1]]).

> [!remark] Remark: Vector Fields and One-Forms Side by Side
> | Field | A section of | In a chart | Picture |
> |---|---|---|---|
> | vector field $\mathbf{X}$ | $TM$ ([[§56 Vector Fields#^def-56-1\|Definition §56.1]]) | $\sum_j \mathbf{X}^j\, \partial/\partial x^j$ | wind on the surface |
> | one-form $\theta$ | $T^{\ast}M$ ([[§53 One-Forms#^def-53-1\|Definition §53.1]]) | $\sum_j \theta_j\, dx^j$ | a rule pricing every step |
>
> Every function gives a one-form, $f \mapsto df$ ([[§53 One-Forms#^prop-53-2|Proposition §53.2]]), but not every one-form is a $df$ ([[§53 One-Forms#^prop-53-3|Proposition §53.3]]). A one-form and a vector field together give a function, $p \mapsto \theta_p(\mathbf{X}_p)$. And a vector field acting on a function gives a function, $p \mapsto \mathbf{X}_p[f]$ — the starting point of the next subsection.

^rem-56-1

## Vector Fields as Derivations

> [!remark] Remark: Two Faces of a Vector Field
> “Just as tangent vectors, fields have a double life.” Tangent vectors were defined as derivations and then shown to be velocities of curves ([[§31 Tangent Vectors as Velocities of Curves|§31]]). Vector fields likewise have two faces: *operators on functions*, studied first because it continues the definition by derivations; and *dynamics on $M$* — integral curves, the trajectories that follow the field, to come later.

^rem-56-2

> [!definition] Definition §56.4: Operator on $C^\infty(M)$
> An **operator** on $C^\infty(M)$ is a map
>
> $$
> P : C^\infty(M) \longrightarrow C^\infty(M), \qquad f \longmapsto Pf ,
> $$
>
> taking [[§19 Smooth Functions and Smooth Maps#^def-19-2|smooth functions]] on $M$ to smooth functions on $M$.

^def-56-4

*(Not from lecture: Uribe uses the word without defining it — “it's an $\mathbb{R}$-linear operator”.)* $C^\infty(M)$ is a real vector space under pointwise addition and scalar multiplication, and an operator $P$ is *$\mathbb{R}$-linear*, or a *linear operator*, if it is a [[§7 Vector Space of Linear Maps#^ladr-3-1|linear map]] of this space: $P(af + bg) = a\,Pf + b\,Pg$ for $a, b \in \mathbb{R}$ and $f, g \in C^\infty(M)$. Operators can be added, $(P + Q)f = Pf + Qf$, and composed, $(P \circ Q)f = P(Qf)$, and sums and composites of linear operators are linear. Examples: $f \mapsto D_\mathbf{X}f$ for a vector field $\mathbf{X}$ ([[§56 Vector Fields#^lem-56-3|Lemma §56.3]] below), and multiplication by a fixed function, $f \mapsto gf$ ([[§57 Differential Operators#^def-57-1|Definition §57.1]] below). A [[§56 Vector Fields#^def-56-5|derivation]], a [[§56 Vector Fields#^def-56-6|local operator]] and a [[§57 Differential Operators#^def-57-2|differential operator]], defined below, are operators with extra properties; the [[§58 Lie Bracket and Lie Algebra#^def-58-1|Lie bracket]] of [[§58 Lie Bracket and Lie Algebra|§58]] is the commutator of two operators.

> [!definition] Definition §56.5: Derivation of $C^\infty(M)$
> A **derivation** of $C^\infty(M)$ is an $\mathbb{R}$-linear [[§56 Vector Fields#^def-56-4|operator]] $D : C^\infty(M) \to C^\infty(M)$ ([[§56 Vector Fields#^def-56-4|Definition §56.4]]) satisfying the product rule
>
> $$
> D(fg) = f\, Dg + g\, Df \qquad \text{for all } f, g \in C^\infty(M).
> $$
>
> Compare a derivation *at a point* ([[§28 Derivations and the Abstract Tangent Space#^def-28-1|Definition §28.1]]), which takes values in $\mathbb{R}$ and acts on [[§27 Germs#^def-27-2|germs]].
>
> *Lee: Ch. 8, Vector Fields as Derivations*

^def-56-5

> [!theorem] Lemma §56.3: A Vector Field Is a Derivation
> For $\mathbf{X} \in \mathfrak{X}(M)$ ([[§56 Vector Fields#^def-56-2|Def. §56.2]]) and $f \in C^\infty(M)$, the function $D_\mathbf{X}f : p \mapsto \mathbf{X}_p[f]$ is smooth, and $D_\mathbf{X} : C^\infty(M) \to C^\infty(M)$ is a [[§56 Vector Fields#^def-56-5|derivation]]. In a chart, $D_\mathbf{X}f = \sum_j \mathbf{X}^j\, \partial f/\partial x^j$. (Lee writes $\mathbf{X}f$ for $D_\mathbf{X}f$.)

^lem-56-3

> [!proof]+ Proof
> *(Lecture 15: linearity and the product rule are “an immediate consequence of the corresponding properties for tangent vectors”, applied at each point. Smoothness of $D_\mathbf{X}f$, which the lecture did not address, is filled in.)* Three things are claimed: the chart formula, smoothness of $D_\mathbf{X}f$, and that $D_\mathbf{X}$ is $\mathbb{R}$-linear and satisfies the product rule (Definition [[§56 Vector Fields#^def-56-5|§56.5]]). Throughout, $[f]$ denotes the germ at $p$ of $f \in C^\infty(M)$.
>
> *The chart formula.* Let $(U, \varphi = (x^j))$ be a chart and $p \in U$. By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], $\mathbf{X}_p = \sum_j \mathbf{X}^j(p)\, \partial/\partial x^j|_p$. Derivations at $p$ are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]), so evaluating at $[f]$ and using Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]],
>
> $$
> (D_\mathbf{X}f)(p) = \mathbf{X}_p[f] = \sum_{j=1}^m \mathbf{X}^j(p)\, \frac{\partial}{\partial x^j}\Big|_p[f] = \sum_{j=1}^m \mathbf{X}^j(p)\, \frac{\partial f}{\partial x^j}(p) .
> $$
>
> *Smoothness.* Fix $p \in M$ and a chart $(U, \varphi)$ at $p$; by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]] it suffices that $(D_\mathbf{X}f) \circ \varphi^{-1}$ is smooth on $\varphi(U)$. By the chart formula, for $r \in \varphi(U)$,
>
> $$
> (D_\mathbf{X}f)\big(\varphi^{-1}(r)\big) = \sum_{j=1}^m \mathbf{X}^j\big(\varphi^{-1}(r)\big)\, \frac{\partial f}{\partial x^j}\big(\varphi^{-1}(r)\big) = \sum_{j=1}^m \big(\mathbf{X}^j \circ \varphi^{-1}\big)(r)\, \frac{\partial f_\varphi}{\partial r^j}(r),
> $$
>
> the second equality by Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], $\partial f/\partial x^j(q) = \partial f_\varphi/\partial r^j(\varphi(q))$ with $q = \varphi^{-1}(r)$. Here $\mathbf{X}^j \circ \varphi^{-1}$ is smooth because $\mathbf{X}^j$ is smooth on $U$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], $\mathbf{X}$ being smooth) and by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]; and $\partial f_\varphi/\partial r^j$ is smooth because $f_\varphi$ is (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]). A sum of products of smooth functions is smooth, so $D_\mathbf{X}f \in C^\infty(M)$.
>
> *Linearity.* Let $f, g \in C^\infty(M)$, $a, b \in \mathbb{R}$ and $p \in M$. The germ of $af + bg$ is $a[f] + b[g]$ (Proposition [[§27 Germs#^prop-27-2|§27.2]]), and $\mathbf{X}_p$ is $\mathbb{R}$-linear (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]):
>
> $$
> \big(D_\mathbf{X}(af + bg)\big)(p) = \mathbf{X}_p\big(a[f] + b[g]\big) = a\,\mathbf{X}_p[f] + b\,\mathbf{X}_p[g] = \big(a\, D_\mathbf{X}f + b\, D_\mathbf{X}g\big)(p) .
> $$
>
> *Product rule.* The germ of $fg$ is $[f][g]$ (Proposition [[§27 Germs#^prop-27-2|§27.2]]), and $\mathbf{X}_p$ satisfies the Leibniz rule at $p$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]):
>
> $$
> \big(D_\mathbf{X}(fg)\big)(p) = \mathbf{X}_p\big([f][g]\big) = f(p)\, \mathbf{X}_p[g] + g(p)\, \mathbf{X}_p[f] = \big(f\, D_\mathbf{X}g + g\, D_\mathbf{X}f\big)(p) .
> $$
>
> Both identities hold at every $p$, so they hold as identities of functions, and $D_\mathbf{X}$ is a derivation of $C^\infty(M)$.

^pf-56-3

*Uses:* [[§56 Vector Fields#^def-56-5|Def. §56.5]], [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§27 Germs#^prop-27-2|§27.2]]

![[m591-44-a2.gif|460]]

*(Not from lecture; animation added, vault only.)* The field of the figure acting on $f = y$, the height: as $p$ goes once around, the arrow $\mathbf{X}_p$ (blue) and its vertical part (red), the rate of change of $f$ along it. Right: the function $\mathbf{X}f = df(\mathbf{X}) = c(\theta)\cos\theta$, traced. The operator $f \mapsto \mathbf{X}f$ is the derivation of the lemma.

The goal of this section is the converse of the lemma: every derivation of $C^\infty(M)$ comes from a vector field ([[§56 Vector Fields#^prop-56-7|Proposition §56.7]], at the end). Tangent vectors act on germs, which only see a neighbourhood of a point, while a derivation of $C^\infty(M)$ acts on functions on all of $M$. The bridge is locality ([[§56 Vector Fields#^lem-56-6|Lemma §56.6]]), and its proof needs bump functions, so these come first.

> [!definition] Definition §56.6: Local Operator
> An [[§56 Vector Fields#^def-56-4|operator]] $D : C^\infty(M) \to C^\infty(M)$ ([[§56 Vector Fields#^def-56-4|Definition §56.4]]) is **local** if for every open $U \subseteq M$ and all $f, g \in C^\infty(M)$,
>
> $$
> f|_U = g|_U \quad \Longrightarrow \quad (Df)|_U = (Dg)|_U .
> $$

^def-56-6

“Even though $D$ a priori is defined on functions on $M$, it's actually going to be given by local data”: knowing $f$ on $U$ determines $Df$ on $U$.

> [!definition] Definition §56.7: Support
> The **support** of a function $\chi : M \to \mathbb{R}$ is the *[[§8 Interior and Closure#^def-8-2|closure]]* of the set where it is nonzero,
>
> $$
> \operatorname{supp}\chi = \overline{\{ q \in M : \chi(q) \neq 0 \}} .
> $$
>
> *Lee: Ch. 2, Partitions of Unity*

^def-56-7

> [!definition] Definition §56.8: Compactly Supported Functions
> $C^\infty_0(M)$ is the set of smooth functions $\chi : M \to \mathbb{R}$ whose support ([[§56 Vector Fields#^def-56-7|Definition §56.7]]) is [[§18 Compact Spaces#^def-18-2|compact]].
>
> *Lee: Ch. 2, Partitions of Unity*

^def-56-8

> [!definition] Definition §56.9: Bump Function
> Let $p \in M$. A **bump function at $p$** is a $\chi \in C^\infty_0(M)$ ([[§56 Vector Fields#^def-56-8|Definition §56.8]]) with $\chi \equiv 1$ on a neighbourhood of $p$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-56-9

“It's a technical term, and it's not a joke”: the graph is a plateau, equal to $1$ near $p$ and dying off to $0$ outside a compact set — “smooth, but not analytic”, since an analytic function equal to $1$ on an open set would equal $1$ on the whole connected domain.

![[m591-44-3.svg]]
*A bump function at $p$, after the board sketch, with the front quarter cut away. $M$ is a plane, and the graph of $\chi$ is a surface over it: $\chi \equiv 1$ on a disc around $p$ (the blue plateau, at height $1$); from its edge the graph falls smoothly to $0$ (orange); and $\chi = 0$ outside the compact set $\operatorname{supp}\chi$, whose boundary is the dashed circle on $M$. The two cut faces show the profile of $\chi$ along two rays from $p$, and $p$ lies on $M$ at their inner corner, directly below the plateau, where $\chi(p) = 1$. The cross-section below shows the same profile along a whole line through $p$.*

![[m591-45-1.svg]]
*A bump function, drawn over a one-dimensional slice of $M$ (the graph is the plateau of Uribe's picture, in cross-section). It equals $1$ on a neighbourhood of $p$, is smooth everywhere, and vanishes outside its support, which is compact and lies inside the given open set $U$. This one is built from $h(t) = e^{-1/t}$ for $t > 0$, $h(t) = 0$ for $t \le 0$, as $\chi(x) = h(b - |x|)/\big(h(b - |x|) + h(|x| - a)\big)$, which is $1$ for $|x| \le a$ and $0$ for $|x| \ge b$.*

![[m591-45-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* Left: $h(t) = e^{-1/t}$ (dashed) and the smooth step $g = h(t)/(h(t) + h(1 - t))$, $0$ for $t \le 0$ and $1$ for $t \ge 1$. Right: the bump $\chi(x) = g\big((r_2 - |x|)/(r_2 - r_1)\big)$ as the radii vary, $1$ on the plateau $[-r_1, r_1]$ (blue) and $0$ outside $(-r_2, r_2)$, smooth everywhere.

**Transcription note.** Page 41 of the handwritten notes defines $\operatorname{supp}(\chi) = \{q \in M : \chi(q) \neq 0\}$; the support is the *closure* of that set, as Uribe said (“and then you take the closure of that”). Without the closure, the support of a bump function would not be compact.

> [!theorem] Proposition §56.4: Bump Functions Exist
> For every open $U \subseteq M$ and every $p \in U$ there is a [[§56 Vector Fields#^def-56-9|bump function]] $\chi$ at $p$ with $\operatorname{supp}\chi \subseteq U$.
>
> *Lee: Proposition 2.25*

^prop-56-4

> [!proof]+ Proof
> *(Stated in Lecture 15, and again in Lecture 16 — “we're going to prove it next week, but not this week” — as “technical things that you will not be using in homework.” “The existence is not so obvious, but it's true.” Lecture 21 gave the recipe while proving the Whitney embedding theorem: the function “is constructed in the Euclidean space first, and then you pull back with the chart.” Filled in along that recipe, following Lee, Lemmas 2.20–2.22.)* We prove slightly more, needed in Theorem [[§65 The Whitney Embedding Theorem#^thm-65-7|§65.7]]: *if $(V, \varphi)$ is a chart at $p$ with $V \subseteq U$, and $0 < r < r'$ with $\overline{B}(\varphi(p), r') \subseteq \varphi(V)$, there is a bump function $\chi$ at $p$ with $\operatorname{supp}\chi \subseteq V$ and $\chi \equiv 1$ on the closed coordinate ball $\varphi^{-1}\big(\overline{B}(\varphi(p), r)\big)$.* Such a chart exists: restrict any chart at $p$ to its intersection with $U$, and choose a small ball.
>
> *1. A smooth function vanishing to infinite order.* Let $h(t) = e^{-1/t}$ for $t > 0$ and $h(t) = 0$ for $t \le 0$. By induction, for $t > 0$, $h^{(k)}(t) = P_k(1/t)\, e^{-1/t}$ with $P_k$ a polynomial, since $\frac{d}{dt}\big(P(1/t) e^{-1/t}\big) = \big(-P'(1/t)/t^2 + P(1/t)/t^2\big) e^{-1/t}$. As $s^j e^{-s} \to 0$ for $s = 1/t \to \infty$, every $h^{(k)}(t) \to 0$ as $t \to 0^+$, and the right difference quotient $\big(h^{(k)}(t) - 0\big)/t = (1/t)\, P_k(1/t)\, e^{-1/t} \to 0$ as well. So by induction every $h^{(k)}$ exists at $0$ and equals $0$, and $h$ is smooth on $\mathbb{R}$, with $h > 0$ exactly on $(0, \infty)$.
>
> *2. A plateau on $\mathbb{R}^m$.* Put
>
> $$
> H(x) = \frac{h\big(r'^2 - |x|^2\big)}{h\big(r'^2 - |x|^2\big) + h\big(|x|^2 - r^2\big)}, \qquad x \in \mathbb{R}^m .
> $$
>
> The denominator never vanishes: if $|x| < r'$ the first term is positive, and if $|x| \ge r' > r$ the second is. So $H$ is smooth, $0 \le H \le 1$, $H(x) = 1$ when $|x| \le r$ (the second term vanishes), and $H(x) = 0$ when $|x| \ge r'$.
>
> *3. Pull back by the chart.* Define $\chi = H\big(\varphi - \varphi(p)\big)$ on $V$ and $\chi = 0$ on $M \setminus V$. The set $K = \varphi^{-1}\big(\overline{B}(\varphi(p), r')\big)$ is compact, as the image of a compact set under the continuous map $\varphi^{-1}$, hence closed in the Hausdorff space $M$, and $K \subseteq V$. $\chi$ is smooth on the open set $V$ and zero on the open set $M \setminus K$; these two open sets cover $M$, so $\chi$ is smooth. Its support lies in $K$, so it is compact and inside $V \subseteq U$; and $\chi \equiv 1$ on $\varphi^{-1}\big(\overline{B}(\varphi(p), r)\big)$, which contains the open neighbourhood $\varphi^{-1}\big(B(\varphi(p), r)\big)$ of $p$. So $\chi$ is a bump function at $p$ (Definition [[§56 Vector Fields#^def-56-9|§56.9]]).

^pf-56-4

*Uses:* [[§65 The Whitney Embedding Theorem#^thm-65-7|§65.7]], [[§56 Vector Fields#^def-56-9|Def. §56.9]]

![[m591-53-1.svg]]

*(Not from lecture; figure added.)* The two steps of the construction for $m = 1$. Left: $h(t) = e^{-1/t}$ for $t > 0$ and $h = 0$ for $t \le 0$ is smooth, with all derivatives $0$ at $t = 0$, so it switches on without a corner (Step 1). Right: the plateau $H(x) = h(r'^2 - x^2) / \big(h(r'^2 - x^2) + h(x^2 - r^2)\big)$ is $1$ on $|x| \le r$, $0$ for $|x| \ge r'$, and smooth in between (Step 2); pulling it back by a chart gives the bump function (Step 3).

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$, smooth but not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]].
> - Bump functions were already granted (Lee, Proposition 2.25) in [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|Germ Derivations and Global Derivations, §28.3]].

*Terminology (Lecture 16).* A function $\chi$ with $\operatorname{supp}\chi \subseteq U$ is said to be *subordinate to $U$*, “because this is a condition that is going to show up several times.”

*Lecture 16: the corollary of the [[§56 Vector Fields#^prop-56-4|bump function lemma]] that the proof of [[§56 Vector Fields#^prop-56-7|Proposition §56.7]] uses.*

> [!theorem] Corollary §56.5: Every Germ Has a Global Representative
> Let $p \in M$ and $\gamma \in C^\infty_p(M)$, represented by $f \in C^\infty(U)$ with $U \ni p$ open. If $\chi$ is a [[§56 Vector Fields#^def-56-9|bump function]] at $p$ subordinate to $U$, then
>
> $$
> \tilde f = \begin{cases} \chi f & \text{on } U, \\ 0 & \text{on } M \setminus U \end{cases}
> $$
>
> is smooth on all of $M$ and represents $\gamma$. In particular every [[§27 Germs#^def-27-2|germ]] at $p$ has a representative defined on all of $M$.
>
> *Lee: Lemma 2.26 (extension lemma)*

^cor-56-5

> [!proof]+ Proof
> *(Lecture 16.)* Two things are claimed: $\tilde f \in C^\infty(M)$, and $[\tilde f] = [f] = \gamma$ in $C^\infty_p(M)$.
>
> *$\tilde f$ is smooth.* Smoothness of a function is tested at each point with a chart at that point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]), and a smooth chart may be shrunk to any smaller open neighbourhood of the point (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)); so it suffices to cover $M$ by open sets on each of which $\tilde f$ is smooth. Take the two sets $U$ and $M \setminus \operatorname{supp}\chi$. The second is open because $\operatorname{supp}\chi$ is closed, being a closure (Definition [[§56 Vector Fields#^def-56-7|§56.7]]). They cover $M$: a point $q \notin U$ is not in $\operatorname{supp}\chi$, because $\operatorname{supp}\chi \subseteq U$.
> - On $U$, $\tilde f = \chi f$ is a product of the smooth functions $\chi|_U$ and $f$, hence smooth.
> - On $M \setminus \operatorname{supp}\chi$, $\tilde f \equiv 0$. Let $q \notin \operatorname{supp}\chi$. Then $\chi(q) = 0$, since every point where $\chi \ne 0$ lies in $\operatorname{supp}\chi$. If $q \in U$, $\tilde f(q) = \chi(q)\, f(q) = 0 \cdot f(q) = 0$; if $q \notin U$, $\tilde f(q) = 0$ by definition. A constant function is smooth.
>
> So $\tilde f \in C^\infty(M)$.
>
> *$\tilde f$ represents $\gamma$.* Since $\chi$ is a bump function at $p$, there is an open $V \ni p$ with $\chi \equiv 1$ on $V$ (Definition [[§56 Vector Fields#^def-56-9|§56.9]]). For $q \in V \cap U$,
>
> $$
> \tilde f(q) = \chi(q)\, f(q) = 1 \cdot f(q) = f(q) .
> $$
>
> $V \cap U$ is open, contains $p$, and lies in the intersection $M \cap U$ of the two domains, so $(\tilde f, M) \sim (f, U)$ (Definition [[§27 Germs#^def-27-1|§27.1]]), that is, $[\tilde f] = [f] = \gamma$.
>
> *In particular.* Every germ $\gamma$ at $p$ has some representative $f \in C^\infty(U)$ with $U \ni p$ open (Definition [[§27 Germs#^def-27-2|§27.2]]), and a bump function at $p$ subordinate to $U$ exists by Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]; so the construction applies to every germ.

^pf-56-5

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§56 Vector Fields#^def-56-7|Def. §56.7]], [[§56 Vector Fields#^def-56-9|Def. §56.9]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§56 Vector Fields#^prop-56-4|§56.4]]

![[m591-47-1.svg]]
*The extension of a germ. Above: $f$ is defined only on $U$ (its ends are open), and $\chi$ (dashed) is a bump function at $p$ subordinate to $U$. Below: $\tilde f = \chi f$, extended by $0$. On $V$, where $\chi \equiv 1$, it agrees with $f$ (dotted), so it has the same germ at $p$; it dies off inside $U$ and is $0$ outside $\operatorname{supp}\chi$, so it is smooth on all of $M$.*

> [!theorem] Lemma §56.6: Derivations Are Local
> Every [[§56 Vector Fields#^def-56-5|derivation]] of $C^\infty(M)$ is a [[§56 Vector Fields#^def-56-6|local operator]].

^lem-56-6

> [!proof]+ Proof
> *(Lecture 16, in full: “you'll see how incredibly powerful the product rule is.”)* Let $D$ be a derivation of $C^\infty(M)$, $U \subseteq M$ open, and $f, g \in C^\infty(M)$ with $f|_U = g|_U$; we must show $(Df)|_U = (Dg)|_U$.
>
> *Reduction to the kernel.* Put $h = f - g \in C^\infty(M)$; then $h|_U = 0$. By linearity of $D$, $Df - Dg = D(f - g) = Dh$. So it suffices to show: if $h|_U = 0$ then $(Dh)|_U = 0$ — “like showing that something is injective by showing that the kernel is zero.”
>
> *The kernel.* Let $h|_U = 0$ and fix $p \in U$. By Proposition [[§56 Vector Fields#^prop-56-4|§56.4]] there is a bump function $\chi$ at $p$ subordinate to $U$: $\chi \in C^\infty(M)$, $\operatorname{supp}\chi \subseteq U$, and $\chi \equiv 1$ near $p$, in particular $\chi(p) = 1$ (Definition [[§56 Vector Fields#^def-56-9|§56.9]]). The product $\chi h$ is the zero function on $M$. Indeed, for $q \in U$, $h(q) = 0$; and for $q \notin U$, $q \notin \operatorname{supp}\chi$, so $\chi(q) = 0$ (every point where $\chi \ne 0$ lies in the support, Definition [[§56 Vector Fields#^def-56-7|§56.7]]). A linear map sends $0$ to $0$, so $D(\chi h) = D(0) = 0$; and by the product rule (Definition [[§56 Vector Fields#^def-56-5|§56.5]]),
>
> $$
> 0 = D(\chi h) = \chi\, Dh + h\, D\chi ,
> $$
>
> an equality of functions on $M$. Evaluate it at $p$, using $\chi(p) = 1$ and $h(p) = 0$ (as $p \in U$):
>
> $$
> 0 = \chi(p)\,(Dh)(p) + h(p)\,(D\chi)(p) = 1 \cdot (Dh)(p) + 0 \cdot (D\chi)(p) = (Dh)(p) .
> $$
>
> As $p \in U$ was arbitrary, $(Dh)|_U = 0$, and therefore $(Df)|_U = (Dg)|_U$.

^pf-56-6

*Uses:* [[§56 Vector Fields#^def-56-5|Def. §56.5]], [[§56 Vector Fields#^def-56-6|Def. §56.6]], [[§56 Vector Fields#^def-56-9|Def. §56.9]], [[§56 Vector Fields#^def-56-7|Def. §56.7]], [[§56 Vector Fields#^prop-56-4|§56.4]]

“Derivations are local, thanks to the product rule and the existence of bump functions.”

> [!remark]- Connections
> - The pointwise version, a derivation of $C^\infty(M)$ at $p$ only sees a function near $p$ (Lee, Proposition 3.8), in the proof of [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|Germ Derivations and Global Derivations, §28.3]].

*Lecture 15, after stating the lemma (proved above in Lecture 16): “I want to make an observation.”* The observation was the ring of differential operators, generated by the operators $D_\mathbf{X}$ and the multiplications by functions, all of whose elements are local; it is collected, with what follows from it, in the next section, [[§57 Differential Operators|§57]].

*Lecture 16 proved the converse of [[§56 Vector Fields#^lem-56-3|Lemma §56.3]]. “It's not an immediate thing at all … tangent vectors are defined in terms of germs”, local objects near a point, “whereas” a derivation of $C^\infty(M)$ “a priori” acts on functions on all of $M$. Locality ([[§56 Vector Fields#^lem-56-6|Lemma §56.6]]) is half the bridge; the other half is that germs can be globalized ([[§56 Vector Fields#^cor-56-5|Corollary §56.5]]).*

> [!theorem] Proposition §56.7: Derivations Are Vector Fields
> Conversely, every [[§56 Vector Fields#^def-56-5|derivation]] $D$ of $C^\infty(M)$ is of the form $D = D_\mathbf{X}$ ([[§56 Vector Fields#^lem-56-3|Lemma §56.3]]) for a unique $\mathbf{X} \in \mathfrak{X}(M)$.
>
> *Lee: Proposition 8.15*

^prop-56-7

> [!proof]+ Proof
> *(Lecture 16, in the lecture's steps. Uribe “skip[ped] a little bit the details” of smoothness; they are completed below, as are two steps the lecture did not state: that each $\mathbf{X}_p$ is a derivation at $p$, and uniqueness.)* Let $D$ be a derivation of $C^\infty(M)$. We must produce $\mathbf{X} \in \mathfrak{X}(M)$, i.e. a smooth section of $TM$, with $D_\mathbf{X} = D$, and show that it is the only one.
>
> *1. Define $\mathbf{X}$ pointwise.* For $p \in M$ and a germ $\gamma \in C^\infty_p(M)$, set
>
> $$
> \mathbf{X}_p(\gamma) = (Df)(p), \qquad f \in C^\infty(M) \text{ a global representative of } \gamma,
> $$
>
> which exists by Corollary [[§56 Vector Fields#^cor-56-5|§56.5]] (with a bump function supplied by Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]).
>
> *2. It is well defined.* Let $f, f' \in C^\infty(M)$ both represent $\gamma$. Then $(f, M) \sim (f', M)$, so there is an open $W \ni p$ with $f|_W = f'|_W$ (Definition [[§27 Germs#^def-27-1|§27.1]]). By Lemma [[§56 Vector Fields#^lem-56-6|§56.6]], applied with the open set $W$, $(Df)|_W = (Df')|_W$; since $p \in W$, $(Df)(p) = (Df')(p)$. So $\mathbf{X}_p(\gamma)$ does not depend on the choice of $f$. “So you see, we need all these lemmas.”
>
> *3. Each $\mathbf{X}_p$ is a derivation at $p$.* *(Completion.)* Let $\gamma, \delta \in C^\infty_p(M)$ with global representatives $f, g$, and $a, b \in \mathbb{R}$. Germ operations are computed on representatives (Proposition [[§27 Germs#^prop-27-2|§27.2]]), here on the common domain $M$, so $af + bg$ is a global representative of $a\gamma + b\delta$, and $fg$ one of $\gamma\delta$. By step 1 and the linearity of $D$,
>
> $$
> \mathbf{X}_p(a\gamma + b\delta) = \big(D(af + bg)\big)(p) = a\,(Df)(p) + b\,(Dg)(p) = a\,\mathbf{X}_p(\gamma) + b\,\mathbf{X}_p(\delta) .
> $$
>
> By step 1, the product rule of $D$, and $\gamma(p) = f(p)$, $\delta(p) = g(p)$ (Definition [[§27 Germs#^def-27-3|§27.3]]),
>
> $$
> \mathbf{X}_p(\gamma\delta) = \big(D(fg)\big)(p) = f(p)\,(Dg)(p) + g(p)\,(Df)(p) = \gamma(p)\,\mathbf{X}_p(\delta) + \delta(p)\,\mathbf{X}_p(\gamma) .
> $$
>
> So $\mathbf{X}_p$ is a derivation at $p$, i.e. $\mathbf{X}_p \in T_pM$ (Definitions [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]] and [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]). Thus $\mathbf{X} : p \mapsto \mathbf{X}_p$ is a section of $TM$, so far not known to be smooth.
>
> *4. $\mathbf{X}$ is smooth.* In a chart $(U, (x^1, \ldots, x^m))$ at $p$, $\mathbf{X}_q = \sum_j \mathbf{X}_q(x^j)\, \partial/\partial x^j|_q$ for $q \in U$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), and “$\mathbf{X}_p(x^j)$ is $D(\tilde x^j)(p)$, where $\tilde x^j$ is a smooth extension of $x^j$.” *(Completion.)* Smoothness of a map is a condition at each point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), so it suffices to find an open $V \ni p$ on which $\mathbf{X}$ is smooth. Take one bump function $\chi$ at $p$ subordinate to $U$ (Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]), equal to $1$ on an open $V \ni p$. Then $V \subseteq U$, since $V \subseteq \{\chi \ne 0\} \subseteq \operatorname{supp}\chi \subseteq U$. Let $\tilde x^j = \chi x^j$, extended by $0$ outside $U$: the single extension of Corollary [[§56 Vector Fields#^cor-56-5|§56.5]], smooth on $M$. For $q \in V$, $\tilde x^j$ and $x^j$ agree on the open set $V \ni q$ (because $\chi = 1$ there), so $\tilde x^j$ is a global representative of the germ of $x^j$ at $q$ (Definition [[§27 Germs#^def-27-1|§27.1]]), and by step 1
>
> $$
> \mathbf{X}_q(x^j) = D(\tilde x^j)(q) \qquad \text{for all } q \in V .
> $$
>
> The right side is the function $D(\tilde x^j) \in C^\infty(M)$ evaluated at $q$; its restriction to $V$ is smooth. Now $(V, (x^1|_V, \ldots, x^m|_V))$ is a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)), and in it the coefficients of $\mathbf{X}$ are $\mathbf{X}^j(q) = \mathbf{X}_q(x^j)$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]), which we have just shown to be smooth on $V$. By Proposition [[§56 Vector Fields#^prop-56-1|§56.1]], $\mathbf{X}$ is smooth on $V$. As $p$ was arbitrary, $\mathbf{X}$ is smooth, and $\mathbf{X} \in \mathfrak{X}(M)$.
>
> *5. $D = D_\mathbf{X}$.* Let $f \in C^\infty(M)$ and $p \in M$. The function $f$ is a global representative of its own germ $[f]$ at $p$, so step 1 with $\gamma = [f]$ and the definition of $D_\mathbf{X}$ (Lemma [[§56 Vector Fields#^lem-56-3|§56.3]]) give
>
> $$
> (D_\mathbf{X} f)(p) = \mathbf{X}_p[f] = (Df)(p) .
> $$
>
> This holds for every $p$ and every $f$, so $D_\mathbf{X} f = Df$ for all $f$, i.e. $D_\mathbf{X} = D$.
>
> *6. Uniqueness.* *(Completion.)* Suppose $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ with $D_\mathbf{X} = D_\mathbf{Y}$. Fix $p$ and a germ $\gamma$ at $p$, with global representative $f$ (Corollary [[§56 Vector Fields#^cor-56-5|§56.5]]), so $\gamma = [f]$. Then
>
> $$
> \mathbf{X}_p(\gamma) = \mathbf{X}_p[f] = (D_\mathbf{X} f)(p) = (D_\mathbf{Y} f)(p) = \mathbf{Y}_p[f] = \mathbf{Y}_p(\gamma) .
> $$
>
> So $\mathbf{X}_p$ and $\mathbf{Y}_p$ agree on every germ, $\mathbf{X}_p = \mathbf{Y}_p$, for every $p$; that is, $\mathbf{X} = \mathbf{Y}$.

^pf-56-7

*Uses:* [[§56 Vector Fields#^cor-56-5|§56.5]], [[§56 Vector Fields#^prop-56-4|§56.4]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§56 Vector Fields#^lem-56-6|§56.6]], [[§27 Germs#^prop-27-2|§27.2]], [[§27 Germs#^def-27-3|Def. §27.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§56 Vector Fields#^lem-56-3|§56.3]]

So $\mathbf{X} \mapsto D_\mathbf{X}$ is a bijection from $\mathfrak{X}(M)$ onto the derivations of $C^\infty(M)$. *Notation (Lecture 16).* From now on $D_\mathbf{X}$ is written $\mathbf{X}$: “you say to yourself, I'm thinking of $\mathbf{X}$ as an operator … if you say $\mathbf{X}(f)$, then it's an operator.”

**Transcription note.** Page 43 of the handwritten notes asks “is $\mathbf{X}_p$ $C^\infty$?”; the question is whether the field $\mathbf{X}$ is smooth, $\mathbf{X}_p$ being a single tangent vector. The same line writes the coordinates as $(x^1, \ldots, x^n)$ and then sums to $m$; the dimension is $m$ throughout.

> [!theorem] Lemma §56.8: A Smoothness Criterion for Vector Fields
> Let $\mathbf{X}$ be a [[§40 Fibrations#^def-40-3|section]] of $TM$, not assumed smooth, and for $f \in C^\infty(M)$ let $\mathbf{X}f$ be the function $p \mapsto \mathbf{X}_p[f]$. Then $\mathbf{X}$ is smooth if and only if $\mathbf{X}f$ is smooth for every $f \in C^\infty(M)$.
>
> *Lee: Proposition 8.14*

^lem-56-8

> [!proof]+ Proof
> *(Not from lecture; filled in, for use in Lecture 17's theorem on Lie algebras. The argument is step 4 of the proof of Proposition [[§56 Vector Fields#^prop-56-7|§56.7]].)* Two implications.
>
> *$\mathbf{X}$ smooth $\Rightarrow$ every $\mathbf{X}f$ smooth.* If $\mathbf{X}$ is smooth, then $\mathbf{X} \in \mathfrak{X}(M)$ and $\mathbf{X}f$ is the function $D_\mathbf{X}f$, which is smooth by Lemma [[§56 Vector Fields#^lem-56-3|§56.3]].
>
> *Every $\mathbf{X}f$ smooth $\Rightarrow$ $\mathbf{X}$ smooth.* Smoothness of a map is a condition at each point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), so it suffices to show that every $p \in M$ has an open neighbourhood $V$ on which $\mathbf{X}$ is smooth. Let $p \in M$ and $(U, (x^1, \ldots, x^m))$ a chart at $p$. Take a bump function $\chi$ at $p$ subordinate to $U$ (Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]), equal to $1$ on an open $V \ni p$; then $V \subseteq \{\chi \ne 0\} \subseteq \operatorname{supp}\chi \subseteq U$. Let $\tilde x^j = \chi x^j$ (extended by $0$ outside $U$) be the global function of Corollary [[§56 Vector Fields#^cor-56-5|§56.5]]. For $q \in V$, $\tilde x^j$ and $x^j$ agree on the open set $V \ni q$, so they have the same germ at $q$ (Definition [[§27 Germs#^def-27-1|§27.1]]), and the derivation $\mathbf{X}_q$, which acts on germs, gives them the same value. In the smooth chart $(V, (x^j|_V))$ (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)) the coefficients of $\mathbf{X}$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]) are therefore
>
> $$
> \mathbf{X}^j(q) = \mathbf{X}_q[x^j] = \mathbf{X}_q[\tilde x^j] = (\mathbf{X}\tilde x^j)(q), \qquad q \in V,
> $$
>
> and $\mathbf{X}\tilde x^j$ is smooth on $M$ by hypothesis, since $\tilde x^j \in C^\infty(M)$; so each $\mathbf{X}^j$ is smooth on $V$. So $\mathbf{X}$ is smooth on $V$, by Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]; $p$ was arbitrary.

^pf-56-8

*Uses:* [[§56 Vector Fields#^prop-56-7|§56.7]], [[§56 Vector Fields#^lem-56-3|§56.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§56 Vector Fields#^prop-56-4|§56.4]], [[§56 Vector Fields#^cor-56-5|§56.5]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§56 Vector Fields#^prop-56-1|§56.1]]
