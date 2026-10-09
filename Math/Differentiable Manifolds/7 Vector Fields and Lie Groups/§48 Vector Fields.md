---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 48
tags: [differentiable-manifolds, math591]
---
← [[§47 One-Forms]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§49 Differential Operators]] →

*Stage: fields — Smooth sections of $TM$, a tangent vector at every point — and vector fields acting on functions, as derivations of $C^\infty(M)$.*

*Lecture 15: “now we want to start a big chapter, new chapter, and now it is on vector fields.” References: Lee Ch. 8. The definition itself was given in Lectures 12 and 13, with the tangent bundle; Lecture 15 restated it “analogously” to one-forms.*

## Vector Fields and Their Coordinates

> [!definition] Definition §48.1: Vector Field
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
> Equivalently, $\pi \circ \mathbf{X} = \mathrm{id}_M$ for the projection $\pi : TM \to M$: a vector field is a section of the tangent bundle ([[§36 Fibrations#^def-36-2|Definition §36.2]]).
>
> *Lee: Ch. 8, Vector Fields*

^def-48-1

In words: a vector field chooses one tangent vector at every point of $M$, and the choice varies smoothly — “for every point, [it] selects a tangent vector at that point.”

![[m591-44-2.svg]]
*A vector field in two pictures, on the circle $M = S^1$ with $\mathbf{X} = c(\theta)\,\partial/\partial\theta$, $c(\theta) = 0.55 + 0.35\sin\theta$. Left: the usual picture, an arrow $\mathbf{X}(p)$ at each point $p$. Right: the tangent bundle $TS^1$, with $S^1$ cut open at $(1,0)$; each fibre $T_pM$ is a vertical line over $p$, and the height of a point on it measures the vector $c\,\partial/\partial\theta$ (above the dashed zero section: counterclockwise). The vector field is the curve $\mathbf{X}(M)$, which meets every fibre exactly once — that is the condition $\mathbf{X}(p) \in T_pM$ — and $\pi \circ \mathbf{X} = \mathrm{id}_M$ says that the point of the curve above $p$ projects back to $p$. The points $p_1, p_2, p_3$ carry the same colour in both pictures.*

> [!remark]- Connections
> - Vector fields on open subsets of $\mathbb{R}^3$ in 452: [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §13]].
> - Computational version: vector fields on regions of $\mathbb{R}^2$ and $\mathbb{R}^3$ in calculus, [[§125 Vector Fields#^def-125-1|Calc Def. §125.1]] and [[§125 Vector Fields#^def-125-2|Calc Def. §125.2]].

**Transcription note.** Page 36 of the handwritten notes writes “Section of $TM \xrightarrow{F} M$”; the map is the projection $\pi$.

**Notation.** The value of a vector field $\mathbf{X}$ ([[§48 Vector Fields#^def-48-1|Definition §48.1]]) at $p$ is written $\mathbf{X}_p \in T_pM$, again with $p$ as a subscript, to make room for the function a tangent vector acts on.

> [!definition] Definition §48.2: The Space of Vector Fields
> The set of all vector fields on $M$ is denoted
>
> $$
> \mathfrak{X}(M) \qquad \big(\text{LaTeX: } \mathtt{\backslash mathfrak\{X\}}\big).
> $$
>
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, $c \in \mathbb{R}$ and $f \in C^\infty(M)$, the sum, the scalar multiple and the product with $f$ are defined pointwise, in the vector space $T_pM$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]]):
>
> $$
> (\mathbf{X} + \mathbf{Y})_p = \mathbf{X}_p + \mathbf{Y}_p, \qquad (c\mathbf{X})_p = c\, \mathbf{X}_p, \qquad (f\mathbf{X})_p = f(p)\, \mathbf{X}_p, \qquad p \in M .
> $$
>
> [[§48 Vector Fields#^prop-48-2|Proposition §48.2]] shows that these are again vector fields and that $\mathfrak{X}(M)$ is a real vector space.
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-48-2

> [!definition] Definition §48.3: Product of a Function and a Vector Field
> For $f \in C^\infty(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, the product $f\mathbf{X}$ is defined pointwise:
>
> $$
> (f\mathbf{X})_p = f(p)\, \mathbf{X}_p \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-48-3

> [!theorem] Proposition §48.1: Vector Fields in Coordinates
> Let $\mathbf{X}$ be a section of $TM$ (not assumed smooth) and $(U, \varphi = (x^j))$ a chart. Then on $U$
>
> $$
> \mathbf{X} = \sum_{j=1}^m \mathbf{X}^j\, \frac{\partial}{\partial x^j}, \qquad \mathbf{X}^j(p) = \mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p),
> $$
>
> and $\mathbf{X}$ is smooth on $U$ if and only if the coefficient functions $\mathbf{X}^1, \ldots, \mathbf{X}^m$ are smooth on $U$.
>
> *Lee: Proposition 8.1*

^prop-48-1

> [!proof]+ Proof
> *(Stated in Lecture 15, “analogously” to one-forms; filled in.)* The expansion is the basis theorem at each point, with coefficients $\mathbf{X}_p[x^j]$ ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]). In the chart $\tilde\varphi$ of $TM$ ([[§45 The Tangent Bundle#^def-45-5|Definition §45.5]]) the coordinate representation of $\mathbf{X}$ is $r \mapsto \big(r, \mathbf{X}^1(\varphi^{-1}(r)), \ldots, \mathbf{X}^m(\varphi^{-1}(r))\big)$, smooth exactly when every $\mathbf{X}^j \circ \varphi^{-1}$ is.

^pf-48-1

*Uses:* [[§48 Vector Fields#^def-48-1|Def. §48.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§45 The Tangent Bundle#^def-45-4|Def. §45.4]], [[§45 The Tangent Bundle#^prop-45-2|§45.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]

> [!theorem] Proposition §48.2: The Space of Vector Fields Is a Real Vector Space
> Let $M$ be a smooth manifold.
> 1. If $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ and $c \in \mathbb{R}$, then $\mathbf{X} + \mathbf{Y}$ and $c\mathbf{X}$ ([[§48 Vector Fields#^def-48-2|Definition §48.2]]) are [[§48 Vector Fields#^def-48-1|vector fields]].
> 2. The zero field $\mathbf{0}$, $\mathbf{0}_p = 0_p \in T_pM$, is a vector field.
> 3. With these operations $\mathfrak{X}(M)$ is a real vector space, with zero vector $\mathbf{0}$ and additive inverse $-\mathbf{X} = (-1)\mathbf{X}$.
> 4. More generally, if $f \in C^\infty(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, then $f\mathbf{X}$ is a vector field.

^prop-48-2

> [!proof]+ Proof
> *(Not from lecture: the notes stated the vector-space structure without proof; filled in.)* *The operations give sections.* At each $p$, $\mathbf{X}_p + \mathbf{Y}_p$, $c\,\mathbf{X}_p$, $f(p)\,\mathbf{X}_p$ and $0_p$ lie in $T_pM$, a real vector space ([[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]]); so each of $\mathbf{X} + \mathbf{Y}$, $c\mathbf{X}$, $f\mathbf{X}$, $\mathbf{0}$ assigns to every $p$ a tangent vector at $p$, a section of $TM$.
>
> *(1), (2), (4): smoothness.* Let $(U, (x^j))$ be a chart. By [[§48 Vector Fields#^prop-48-1|Proposition §48.1]], $\mathbf{X} = \sum_j \mathbf{X}^j\, \partial/\partial x^j$ and $\mathbf{Y} = \sum_j \mathbf{Y}^j\, \partial/\partial x^j$ on $U$ with smooth coefficients. At each $p \in U$, by linearity in $T_pM$,
>
> $$
> (\mathbf{X} + \mathbf{Y})_p = \sum_j \big(\mathbf{X}^j(p) + \mathbf{Y}^j(p)\big) \frac{\partial}{\partial x^j}\Big|_p, \qquad (f\mathbf{X})_p = \sum_j f(p)\, \mathbf{X}^j(p)\, \frac{\partial}{\partial x^j}\Big|_p, \qquad \mathbf{0}_p = \sum_j 0 \cdot \frac{\partial}{\partial x^j}\Big|_p ,
> $$
>
> so the coefficients of $\mathbf{X} + \mathbf{Y}$, $f\mathbf{X}$ and $\mathbf{0}$ are $\mathbf{X}^j + \mathbf{Y}^j$, $f\mathbf{X}^j$ and $0$, smooth on $U$ as sums and products of smooth functions. By [[§48 Vector Fields#^prop-48-1|Proposition §48.1]] again these sections are smooth on $U$; the chart domains cover $M$, and smoothness is local, so they are smooth. The scalar multiple $c\mathbf{X}$ is the case $f \equiv c$ of (4).
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

^pf-48-2

*Uses:* [[§48 Vector Fields#^def-48-1|Def. §48.1]], [[§48 Vector Fields#^def-48-2|Def. §48.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§48 Vector Fields#^prop-48-1|§48.1]]

By (4), $\mathfrak{X}(M)$ is moreover a module over the ring $C^\infty(M)$ — the same pointwise check gives $(fg)\mathbf{X} = f(g\mathbf{X})$, $(f + g)\mathbf{X} = f\mathbf{X} + g\mathbf{X}$ and $f(\mathbf{X} + \mathbf{Y}) = f\mathbf{X} + f\mathbf{Y}$ — which is what Uribe meant by “an algebra over the smooth functions” in Lecture 17. It is infinite-dimensional as a real vector space (for $\dim M \ge 1$), but over $C^\infty(U)$ the fields on a chart domain $U$ have the basis $\partial/\partial x^1, \ldots, \partial/\partial x^m$ ([[§48 Vector Fields#^prop-48-1|Proposition §48.1]]).

> [!remark] Remark: Vector Fields and One-Forms Side by Side
> | Field | A section of | In a chart | Picture |
> |---|---|---|---|
> | vector field $\mathbf{X}$ | $TM$ ([[§48 Vector Fields#^def-48-1\|Definition §48.1]]) | $\sum_j \mathbf{X}^j\, \partial/\partial x^j$ | wind on the surface |
> | one-form $\theta$ | $T^{\ast}M$ ([[§47 One-Forms#^def-47-1\|Definition §47.1]]) | $\sum_j \theta_j\, dx^j$ | a rule pricing every step |
>
> Every function gives a one-form, $f \mapsto df$ ([[§47 One-Forms#^prop-47-2|Proposition §47.2]]), but not every one-form is a $df$ ([[§47 One-Forms#^prop-47-3|Proposition §47.3]]). A one-form and a vector field together give a function, $p \mapsto \theta_p(\mathbf{X}_p)$. And a vector field acting on a function gives a function, $p \mapsto \mathbf{X}_p[f]$ — the starting point of the next subsection.

^rem-48-1

## Vector Fields as Derivations

> [!remark] Remark: Two Faces of a Vector Field
> “Just as tangent vectors, fields have a double life.” Tangent vectors were defined as derivations and then shown to be velocities of curves ([[§31 Tangent Vectors as Velocities of Curves|§31]]). Vector fields likewise have two faces: *operators on functions*, studied first because it continues the definition by derivations; and *dynamics on $M$* — integral curves, the trajectories that follow the field, to come later.

^rem-48-2

> [!definition] Definition §48.4: Operator on $C^\infty(M)$
> An **operator** on $C^\infty(M)$ is a map
>
> $$
> P : C^\infty(M) \longrightarrow C^\infty(M), \qquad f \longmapsto Pf ,
> $$
>
> taking [[§19 Smooth Functions and Smooth Maps#^def-19-2|smooth functions]] on $M$ to smooth functions on $M$.

^def-48-4

*(Not from lecture: Uribe uses the word without defining it — “it's an $\mathbb{R}$-linear operator”.)* $C^\infty(M)$ is a real vector space under pointwise addition and scalar multiplication, and an operator $P$ is *$\mathbb{R}$-linear*, or a *linear operator*, if it is a [[§7 Vector Space of Linear Maps#^ladr-3-1|linear map]] of this space: $P(af + bg) = a\,Pf + b\,Pg$ for $a, b \in \mathbb{R}$ and $f, g \in C^\infty(M)$. Operators can be added, $(P + Q)f = Pf + Qf$, and composed, $(P \circ Q)f = P(Qf)$, and sums and composites of linear operators are linear. Examples: $f \mapsto D_\mathbf{X}f$ for a vector field $\mathbf{X}$ ([[§48 Vector Fields#^lem-48-3|Lemma §48.3]] below), and multiplication by a fixed function, $f \mapsto gf$ ([[§49 Differential Operators#^def-49-1|Definition §49.1]] below). A [[§48 Vector Fields#^def-48-5|derivation]], a [[§48 Vector Fields#^def-48-6|local operator]] and a [[§49 Differential Operators#^def-49-2|differential operator]], defined below, are operators with extra properties; the [[§50 Lie Bracket and Lie Algebra#^def-50-1|Lie bracket]] of [[§50 Lie Bracket and Lie Algebra|§50]] is the commutator of two operators.

> [!definition] Definition §48.5: Derivation of $C^\infty(M)$
> A **derivation** of $C^\infty(M)$ is an $\mathbb{R}$-linear [[§48 Vector Fields#^def-48-4|operator]] $D : C^\infty(M) \to C^\infty(M)$ ([[§48 Vector Fields#^def-48-4|Definition §48.4]]) satisfying the product rule
>
> $$
> D(fg) = f\, Dg + g\, Df \qquad \text{for all } f, g \in C^\infty(M).
> $$
>
> Compare a derivation *at a point* ([[§28 Derivations and the Abstract Tangent Space#^def-28-1|Definition §28.1]]), which takes values in $\mathbb{R}$ and acts on [[§27 Germs#^def-27-2|germs]].
>
> *Lee: Ch. 8, Vector Fields as Derivations*

^def-48-5

> [!theorem] Lemma §48.3: A Vector Field Is a Derivation
> For $\mathbf{X} \in \mathfrak{X}(M)$ ([[§48 Vector Fields#^def-48-2|Def. §48.2]]) and $f \in C^\infty(M)$, the function $D_\mathbf{X}f : p \mapsto \mathbf{X}_p[f]$ is smooth, and $D_\mathbf{X} : C^\infty(M) \to C^\infty(M)$ is a [[§48 Vector Fields#^def-48-5|derivation]]. In a chart, $D_\mathbf{X}f = \sum_j \mathbf{X}^j\, \partial f/\partial x^j$. (Lee writes $\mathbf{X}f$ for $D_\mathbf{X}f$.)

^lem-48-3

> [!proof]+ Proof
> *(Lecture 15: linearity and the product rule are “an immediate consequence of the corresponding properties for tangent vectors”, applied at each point. Smoothness of $D_\mathbf{X}f$, which the lecture did not address, is filled in.)* In a chart, $\mathbf{X}_p[f] = \sum_j \mathbf{X}^j(p)\, \partial f/\partial x^j(p)$ by [[§48 Vector Fields#^prop-48-1|Proposition §48.1]], a sum of products of smooth functions. At each $p$, $\mathbf{X}_p[fg] = f(p)\, \mathbf{X}_p[g] + g(p)\, \mathbf{X}_p[f]$ because $\mathbf{X}_p$ is a derivation at $p$; that is the product rule for $D_\mathbf{X}$, and linearity is the same.

^pf-48-3

*Uses:* [[§48 Vector Fields#^def-48-5|Def. §48.5]], [[§48 Vector Fields#^def-48-2|Def. §48.2]], [[§48 Vector Fields#^prop-48-1|§48.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]]

The goal of this section is the converse of the lemma: every derivation of $C^\infty(M)$ comes from a vector field ([[§48 Vector Fields#^prop-48-7|Proposition §48.7]], at the end). Tangent vectors act on germs, which only see a neighbourhood of a point, while a derivation of $C^\infty(M)$ acts on functions on all of $M$. The bridge is locality ([[§48 Vector Fields#^lem-48-6|Lemma §48.6]]), and its proof needs bump functions, so these come first.

> [!definition] Definition §48.6: Local Operator
> An [[§48 Vector Fields#^def-48-4|operator]] $D : C^\infty(M) \to C^\infty(M)$ ([[§48 Vector Fields#^def-48-4|Definition §48.4]]) is **local** if for every open $U \subseteq M$ and all $f, g \in C^\infty(M)$,
>
> $$
> f|_U = g|_U \quad \Longrightarrow \quad (Df)|_U = (Dg)|_U .
> $$

^def-48-6

“Even though $D$ a priori is defined on functions on $M$, it's actually going to be given by local data”: knowing $f$ on $U$ determines $Df$ on $U$.

> [!definition] Definition §48.7: Support
> The **support** of a function $\chi : M \to \mathbb{R}$ is the *[[§8 Interior and Closure#^def-8-2|closure]]* of the set where it is nonzero,
>
> $$
> \operatorname{supp}\chi = \overline{\{ q \in M : \chi(q) \neq 0 \}} .
> $$
>
> *Lee: Ch. 2, Partitions of Unity*

^def-48-7

> [!definition] Definition §48.8: Compactly Supported Functions
> $C^\infty_0(M)$ is the set of smooth functions $\chi : M \to \mathbb{R}$ whose support ([[§48 Vector Fields#^def-48-7|Definition §48.7]]) is [[§18 Compact Spaces#^def-18-2|compact]].
>
> *Lee: Ch. 2, Partitions of Unity*

^def-48-8

> [!definition] Definition §48.9: Bump Function
> Let $p \in M$. A **bump function at $p$** is a $\chi \in C^\infty_0(M)$ ([[§48 Vector Fields#^def-48-8|Definition §48.8]]) with $\chi \equiv 1$ on a neighbourhood of $p$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-48-9

“It's a technical term, and it's not a joke”: the graph is a plateau, equal to $1$ near $p$ and dying off to $0$ outside a compact set — “smooth, but not analytic”, since an analytic function equal to $1$ on an open set would equal $1$ on the whole connected domain.

![[m591-44-3.svg]]
*A bump function at $p$, after the board sketch, with the front quarter cut away. $M$ is a plane, and the graph of $\chi$ is a surface over it: $\chi \equiv 1$ on a disc around $p$ (the blue plateau, at height $1$); from its edge the graph falls smoothly to $0$ (orange); and $\chi = 0$ outside the compact set $\operatorname{supp}\chi$, whose boundary is the dashed circle on $M$. The two cut faces show the profile of $\chi$ along two rays from $p$, and $p$ lies on $M$ at their inner corner, directly below the plateau, where $\chi(p) = 1$. The cross-section below shows the same profile along a whole line through $p$.*

![[m591-45-1.svg]]
*A bump function, drawn over a one-dimensional slice of $M$ (the graph is the plateau of Uribe's picture, in cross-section). It equals $1$ on a neighbourhood of $p$, is smooth everywhere, and vanishes outside its support, which is compact and lies inside the given open set $U$. This one is built from $h(t) = e^{-1/t}$ for $t > 0$, $h(t) = 0$ for $t \le 0$, as $\chi(x) = h(b - |x|)/\big(h(b - |x|) + h(|x| - a)\big)$, which is $1$ for $|x| \le a$ and $0$ for $|x| \ge b$.*

**Transcription note.** Page 41 of the handwritten notes defines $\operatorname{supp}(\chi) = \{q \in M : \chi(q) \neq 0\}$; the support is the *closure* of that set, as Uribe said (“and then you take the closure of that”). Without the closure, the support of a bump function would not be compact.

> [!theorem] Proposition §48.4: Bump Functions Exist
> For every open $U \subseteq M$ and every $p \in U$ there is a [[§48 Vector Fields#^def-48-9|bump function]] $\chi$ at $p$ with $\operatorname{supp}\chi \subseteq U$.
>
> *Lee: Proposition 2.25*

^prop-48-4

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15, and again in Lecture 16 — “we're going to prove it next week, but not this week” — as “technical things that you will not be using in homework.” “The existence is not so obvious, but it's true.” To be filled.

^pf-48-4

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$, smooth but not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]].
> - Bump functions were already granted (Lee, Proposition 2.25) in [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|Germ Derivations and Global Derivations, §28.3]].

*Terminology (Lecture 16).* A function $\chi$ with $\operatorname{supp}\chi \subseteq U$ is said to be *subordinate to $U$*, “because this is a condition that is going to show up several times.”

*Lecture 16: the corollary of the [[§48 Vector Fields#^prop-48-4|bump function lemma]] that the proof of [[§48 Vector Fields#^prop-48-7|Proposition §48.7]] uses.*

> [!theorem] Corollary §48.5: Every Germ Has a Global Representative
> Let $p \in M$ and $\gamma \in C^\infty_p(M)$, represented by $f \in C^\infty(U)$ with $U \ni p$ open. If $\chi$ is a [[§48 Vector Fields#^def-48-9|bump function]] at $p$ subordinate to $U$, then
>
> $$
> \tilde f = \begin{cases} \chi f & \text{on } U, \\ 0 & \text{on } M \setminus U \end{cases}
> $$
>
> is smooth on all of $M$ and represents $\gamma$. In particular every [[§27 Germs#^def-27-2|germ]] at $p$ has a representative defined on all of $M$.
>
> *Lee: Lemma 2.26 (extension lemma)*

^cor-48-5

> [!proof]+ Proof
> *(Lecture 16.)* *$\tilde f$ is smooth.* The open sets $U$ and $M \setminus \operatorname{supp}\chi$ cover $M$, because $\operatorname{supp}\chi \subseteq U$. On $U$, $\tilde f = \chi f$ is a product of smooth functions. On $M \setminus \operatorname{supp}\chi$, $\tilde f \equiv 0$: there $\chi = 0$ (inside $U$), or $\tilde f = 0$ by definition (outside $U$). Smoothness is local, so $\tilde f$ is smooth. *$\tilde f$ represents $\gamma$.* Let $V \ni p$ be open with $\chi \equiv 1$ on $V$. Then $\tilde f = f$ on $V \cap U$, a neighbourhood of $p$, so $[\tilde f] = [f] = \gamma$.

^pf-48-5

*Uses:* [[§48 Vector Fields#^def-48-9|Def. §48.9]], [[§48 Vector Fields#^def-48-7|Def. §48.7]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]]

![[m591-47-1.svg]]
*The extension of a germ. Above: $f$ is defined only on $U$ (its ends are open), and $\chi$ (dashed) is a bump function at $p$ subordinate to $U$. Below: $\tilde f = \chi f$, extended by $0$. On $V$, where $\chi \equiv 1$, it agrees with $f$ (dotted), so it has the same germ at $p$; it dies off inside $U$ and is $0$ outside $\operatorname{supp}\chi$, so it is smooth on all of $M$.*

> [!theorem] Lemma §48.6: Derivations Are Local
> Every [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$ is a [[§48 Vector Fields#^def-48-6|local operator]].

^lem-48-6

> [!proof]+ Proof
> *(Lecture 16, in full: “you'll see how incredibly powerful the product rule is.”)* Let $U \subseteq M$ be open and $f|_U = g|_U$. By linearity of $D$, replacing $f$ by $f - g$, it suffices to show: if $f|_U = 0$ then $(Df)|_U = 0$ — “like showing that something is injective by showing that the kernel is zero.” Let $p \in U$, and let $\chi$ be a [[§48 Vector Fields#^def-48-9|bump function]] at $p$ subordinate to $U$ ([[§48 Vector Fields#^prop-48-4|Proposition §48.4]]). Then $\chi f \equiv 0$ on $M$: inside $U$ because $f = 0$ there, outside $U$ because $\chi = 0$ there. So, by linearity and then the [[§48 Vector Fields#^def-48-5|product rule]],
>
> $$
> 0 = D(\chi f) = \chi\, Df + f\, D\chi ,
> $$
>
> an equality of functions. Evaluate at $p$: $\chi(p) = 1$ and $f(p) = 0$, so $0 = (Df)(p)$. As $p \in U$ was arbitrary, $(Df)|_U = 0$.

^pf-48-6

*Uses:* [[§48 Vector Fields#^def-48-5|Def. §48.5]], [[§48 Vector Fields#^def-48-6|Def. §48.6]], [[§48 Vector Fields#^def-48-9|Def. §48.9]], [[§48 Vector Fields#^def-48-7|Def. §48.7]], [[§48 Vector Fields#^prop-48-4|§48.4]]

“Derivations are local, thanks to the product rule and the existence of bump functions.”

> [!remark]- Connections
> - The pointwise version, a derivation of $C^\infty(M)$ at $p$ only sees a function near $p$ (Lee, Proposition 3.8), in the proof of [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|Germ Derivations and Global Derivations, §28.3]].

*Lecture 15, after stating the lemma (proved above in Lecture 16): “I want to make an observation.”* The observation was the ring of differential operators, generated by the operators $D_\mathbf{X}$ and the multiplications by functions, all of whose elements are local; it is collected, with what follows from it, in the next section, [[§49 Differential Operators|§49]].

*Lecture 16 proved the converse of [[§48 Vector Fields#^lem-48-3|Lemma §48.3]]. “It's not an immediate thing at all … tangent vectors are defined in terms of germs”, local objects near a point, “whereas” a derivation of $C^\infty(M)$ “a priori” acts on functions on all of $M$. Locality ([[§48 Vector Fields#^lem-48-6|Lemma §48.6]]) is half the bridge; the other half is that germs can be globalized ([[§48 Vector Fields#^cor-48-5|Corollary §48.5]]).*

> [!theorem] Proposition §48.7: Derivations Are Vector Fields
> Conversely, every [[§48 Vector Fields#^def-48-5|derivation]] $D$ of $C^\infty(M)$ is of the form $D = D_\mathbf{X}$ ([[§48 Vector Fields#^lem-48-3|Lemma §48.3]]) for a unique $\mathbf{X} \in \mathfrak{X}(M)$.
>
> *Lee: Proposition 8.15*

^prop-48-7

> [!proof]+ Proof
> *(Lecture 16, in the lecture's steps. Uribe “skip[ped] a little bit the details” of smoothness; they are completed below, as are two steps the lecture did not state: that each $\mathbf{X}_p$ is a derivation at $p$, and uniqueness.)* Let $D$ be a [[§48 Vector Fields#^def-48-5|derivation]] of $C^\infty(M)$.
>
> *1. Define $\mathbf{X}$ pointwise.* For $p \in M$ and a [[§27 Germs#^def-27-2|germ]] $\gamma \in C^\infty_p(M)$, set
>
> $$
> \mathbf{X}_p(\gamma) = (Df)(p), \qquad f \in C^\infty(M) \text{ a global representative of } \gamma,
> $$
>
> which exists by [[§48 Vector Fields#^cor-48-5|Corollary §48.5]].
>
> *2. It is well defined.* Two global representatives of $\gamma$ agree on some neighbourhood of $p$, so by [[§48 Vector Fields#^lem-48-6|Lemma §48.6]] their images under $D$ agree there, in particular at $p$. “So you see, we need all these lemmas.”
>
> *3. Each $\mathbf{X}_p$ is a derivation at $p$.* *(Completion.)* If $f, g$ represent $\gamma, \delta$, then $fg$ represents $\gamma\delta$, and $\mathbf{X}_p(\gamma\delta) = D(fg)(p) = f(p)\,(Dg)(p) + g(p)\,(Df)(p) = \gamma(p)\,\mathbf{X}_p(\delta) + \delta(p)\,\mathbf{X}_p(\gamma)$; linearity is the same. So $\mathbf{X}_p \in T_pM$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-1|Definition §28.1]]).
>
> *4. $\mathbf{X}$ is smooth.* In a chart $(U, (x^1, \ldots, x^m))$ at $p$, $\mathbf{X}_q = \sum_j \mathbf{X}_q(x^j)\, \partial/\partial x^j|_q$ for $q \in U$ ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]), and “$\mathbf{X}_p(x^j)$ is $D(\tilde x^j)(p)$, where $\tilde x^j$ is a smooth extension of $x^j$.” *(Completion.)* Take one [[§48 Vector Fields#^def-48-9|bump function]] $\chi$ at $p$ subordinate to $U$, equal to $1$ on an open $V \ni p$, and the single extension $\tilde x^j = \chi x^j$ of [[§48 Vector Fields#^cor-48-5|Corollary §48.5]]. It agrees with $x^j$ on $V$, so it represents the germ of $x^j$ at every $q \in V$, and
>
> $$
> \mathbf{X}_q(x^j) = D(\tilde x^j)(q) \qquad \text{for all } q \in V .
> $$
>
> The right side is a smooth function of $q$, so the coefficients of $\mathbf{X}$ are smooth on $V$, and $\mathbf{X}$ is smooth near $p$ ([[§48 Vector Fields#^prop-48-1|Proposition §48.1]]).
>
> *5. $D = D_\mathbf{X}$.* For $f \in C^\infty(M)$, $f$ is a global representative of its own germ, so $(D_\mathbf{X} f)(p) = \mathbf{X}_p[f] = (Df)(p)$.
>
> *6. Uniqueness.* *(Completion.)* If $D_\mathbf{X} = D_\mathbf{Y}$, then for every germ $\gamma$ at $p$, with global representative $f$, $\mathbf{X}_p(\gamma) = (D_\mathbf{X} f)(p) = (D_\mathbf{Y} f)(p) = \mathbf{Y}_p(\gamma)$; so $\mathbf{X}_p = \mathbf{Y}_p$ for every $p$.

^pf-48-7

*Uses:* [[§48 Vector Fields#^def-48-5|Def. §48.5]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§48 Vector Fields#^cor-48-5|§48.5]], [[§48 Vector Fields#^lem-48-6|§48.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§48 Vector Fields#^def-48-9|Def. §48.9]], [[§48 Vector Fields#^prop-48-4|§48.4]], [[§48 Vector Fields#^prop-48-1|§48.1]], [[§48 Vector Fields#^lem-48-3|§48.3]]

So $\mathbf{X} \mapsto D_\mathbf{X}$ is a bijection from $\mathfrak{X}(M)$ onto the derivations of $C^\infty(M)$. *Notation (Lecture 16).* From now on $D_\mathbf{X}$ is written $\mathbf{X}$: “you say to yourself, I'm thinking of $\mathbf{X}$ as an operator … if you say $\mathbf{X}(f)$, then it's an operator.”

**Transcription note.** Page 43 of the handwritten notes asks “is $\mathbf{X}_p$ $C^\infty$?”; the question is whether the field $\mathbf{X}$ is smooth, $\mathbf{X}_p$ being a single tangent vector. The same line writes the coordinates as $(x^1, \ldots, x^n)$ and then sums to $m$; the dimension is $m$ throughout.

> [!theorem] Lemma §48.8: A Smoothness Criterion for Vector Fields
> Let $\mathbf{X}$ be a [[§36 Fibrations#^def-36-2|section]] of $TM$, not assumed smooth, and for $f \in C^\infty(M)$ let $\mathbf{X}f$ be the function $p \mapsto \mathbf{X}_p[f]$. Then $\mathbf{X}$ is smooth if and only if $\mathbf{X}f$ is smooth for every $f \in C^\infty(M)$.
>
> *Lee: Proposition 8.14*

^lem-48-8

> [!proof]+ Proof
> *(Not from lecture; filled in, for use in Lecture 17's [[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|theorem on Lie algebras]]. The argument is step 4 of the proof of [[§48 Vector Fields#^prop-48-7|Proposition §48.7]].)* If $\mathbf{X}$ is smooth, $\mathbf{X}f$ is smooth by [[§48 Vector Fields#^lem-48-3|Lemma §48.3]]. Conversely, let $p \in M$ and $(U, (x^1, \ldots, x^m))$ a chart at $p$. Take a [[§48 Vector Fields#^def-48-9|bump function]] $\chi$ at $p$ subordinate to $U$, equal to $1$ on an open $V \ni p$, and the global function $\tilde x^j = \chi x^j$ of [[§48 Vector Fields#^cor-48-5|Corollary §48.5]]. It represents the [[§27 Germs#^def-27-2|germ]] of $x^j$ at every $q \in V$, so the coefficients of $\mathbf{X}$ ([[§48 Vector Fields#^prop-48-1|Proposition §48.1]]) are
>
> $$
> \mathbf{X}^j(q) = \mathbf{X}_q[x^j] = (\mathbf{X}\tilde x^j)(q), \qquad q \in V,
> $$
>
> smooth by hypothesis. So $\mathbf{X}$ is smooth on $V$, by [[§48 Vector Fields#^prop-48-1|Proposition §48.1]]; $p$ was arbitrary.

^pf-48-8

*Uses:* [[§48 Vector Fields#^lem-48-3|§48.3]], [[§48 Vector Fields#^def-48-9|Def. §48.9]], [[§48 Vector Fields#^prop-48-4|§48.4]], [[§48 Vector Fields#^cor-48-5|§48.5]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§48 Vector Fields#^prop-48-1|§48.1]], [[§48 Vector Fields#^prop-48-7|§48.7]]
