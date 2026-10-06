---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 44
tags: [differentiable-manifolds, math591]
---
← [[§43 One-Forms]] · ↑ [[· 6 Bundles and Vector Fields]]

*Stage: fields — Smooth sections of $TM$, a tangent vector at every point — and vector fields acting on functions, as derivations of $C^\infty(M)$.*

*Lecture 15: “now we want to start a big chapter, new chapter, and now it is on vector fields.” References: Lee Ch. 8. The definition itself was given in Lectures 12 and 13, with the tangent bundle; Lecture 15 restated it “analogously” to one-forms.*

## Vector Fields and Their Coordinates

> [!definition] Definition §44.1: Vector Field
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
> Equivalently, $\pi \circ \mathbf{X} = \mathrm{id}_M$ for the projection $\pi : TM \to M$: a vector field is a section of the tangent bundle ([[§34 Fibrations#^def-34-2|Definition §34.2]]).
>
> *Lee: Ch. 8, Vector Fields*

^def-44-1

In words: a vector field chooses one tangent vector at every point of $M$, and the choice varies smoothly — “for every point, [it] selects a tangent vector at that point.”

![[m591-44-2.svg]]
*A vector field in two pictures, on the circle $M = S^1$ with $\mathbf{X} = c(\theta)\,\partial/\partial\theta$, $c(\theta) = 0.55 + 0.35\sin\theta$. Left: the usual picture, an arrow $\mathbf{X}(p)$ at each point $p$. Right: the tangent bundle $TS^1$, with $S^1$ cut open at $(1,0)$; each fibre $T_pM$ is a vertical line over $p$, and the height of a point on it measures the vector $c\,\partial/\partial\theta$ (above the dashed zero section: counterclockwise). The vector field is the curve $\mathbf{X}(M)$, which meets every fibre exactly once — that is the condition $\mathbf{X}(p) \in T_pM$ — and $\pi \circ \mathbf{X} = \mathrm{id}_M$ says that the point of the curve above $p$ projects back to $p$. The points $p_1, p_2, p_3$ carry the same colour in both pictures.*

> [!remark]- Connections
> - Vector fields on open subsets of $\mathbb{R}^3$ in 452: [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]].
> - Computational version: vector fields on regions of $\mathbb{R}^2$ and $\mathbb{R}^3$ in calculus, [[§107 Vector Fields#^def-107-1|Calc Def. §107.1]] and [[§107 Vector Fields#^def-107-2|Calc Def. §107.2]].

**Transcription note.** Page 36 of the handwritten notes writes “Section of $TM \xrightarrow{F} M$”; the map is the projection $\pi$.

**Notation.** The value of a vector field $\mathbf{X}$ ([[§44 Vector Fields#^def-44-1|Definition §44.1]]) at $p$ is written $\mathbf{X}_p \in T_pM$, again with $p$ as a subscript, to make room for the function a tangent vector acts on.

> [!definition] Definition §44.2: The Space of Vector Fields
> The set of all vector fields on $M$ is denoted
>
> $$
> \mathfrak{X}(M) \qquad \big(\text{LaTeX: } \mathtt{\backslash mathfrak\{X\}}\big).
> $$
>
> It is a real vector space under pointwise addition and scalar multiplication.
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-44-2

> [!definition] Definition §44.3: Product of a Function and a Vector Field
> For $f \in C^\infty(M)$ and $\mathbf{X} \in \mathfrak{X}(M)$, the product $f\mathbf{X}$ is defined pointwise:
>
> $$
> (f\mathbf{X})_p = f(p)\, \mathbf{X}_p \qquad \text{for every } p \in M .
> $$
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-44-3

> [!theorem] Proposition §44.1: Vector Fields in Coordinates
> Let $\mathbf{X}$ be a section of $TM$ (not assumed smooth) and $(U, \varphi = (x^j))$ a chart. Then on $U$
>
> $$
> \mathbf{X} = \sum_{j=1}^m \mathbf{X}^j\, \frac{\partial}{\partial x^j}, \qquad \mathbf{X}^j(p) = \mathbf{X}_p[x^j] = dx^j|_p(\mathbf{X}_p),
> $$
>
> and $\mathbf{X}$ is smooth on $U$ if and only if the coefficient functions $\mathbf{X}^1, \ldots, \mathbf{X}^m$ are smooth on $U$.
>
> *Lee: Proposition 8.1*

^prop-44-1

> [!proof]+ Proof
> *(Stated in Lecture 15, “analogously” to one-forms; filled in.)* The expansion is the basis theorem at each point, with coefficients $\mathbf{X}_p[x^j]$ ([[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5]]). In the chart $\tilde\varphi$ of $TM$ ([[§41 The Tangent Bundle#^def-41-5|Definition §41.5]]) the coordinate representation of $\mathbf{X}$ is $r \mapsto \big(r, \mathbf{X}^1(\varphi^{-1}(r)), \ldots, \mathbf{X}^m(\varphi^{-1}(r))\big)$, smooth exactly when every $\mathbf{X}^j \circ \varphi^{-1}$ is.

^pf-44-1

*Uses:* [[§44 Vector Fields#^def-44-1|Def. §44.1]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|§27.5]], [[§30 The Cotangent Space#^prop-30-1|§30.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§41 The Tangent Bundle#^def-41-4|Def. §41.4]], [[§41 The Tangent Bundle#^prop-41-2|§41.2]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§18 Smooth Functions and Smooth Maps#^prop-18-2|§18.2]]

> [!remark] Remark: Vector Fields and One-Forms Side by Side
> | Field | A section of | In a chart | Picture |
> |---|---|---|---|
> | vector field $\mathbf{X}$ | $TM$ ([[§44 Vector Fields#^def-44-1\|Definition §44.1]]) | $\sum_j \mathbf{X}^j\, \partial/\partial x^j$ | wind on the surface |
> | one-form $\theta$ | $T^{\ast}M$ ([[§43 One-Forms#^def-43-1\|Definition §43.1]]) | $\sum_j \theta_j\, dx^j$ | a rule pricing every step |
>
> Every function gives a one-form, $f \mapsto df$ ([[§43 One-Forms#^prop-43-2|Proposition §43.2]]), but not every one-form is a $df$ ([[§43 One-Forms#^prop-43-3|Proposition §43.3]]). A one-form and a vector field together give a function, $p \mapsto \theta_p(\mathbf{X}_p)$. And a vector field acting on a function gives a function, $p \mapsto \mathbf{X}_p[f]$ — the starting point of the next subsection.

^rem-44-1

## Vector Fields as Derivations

> [!remark] Remark: Two Faces of a Vector Field
> “Just as tangent vectors, fields have a double life.” Tangent vectors were defined as derivations and then shown to be velocities of curves ([[§29 Tangent Vectors as Velocities of Curves|§29]]). Vector fields likewise have two faces: *operators on functions*, studied first because it continues the definition by derivations; and *dynamics on $M$* — integral curves, the trajectories that follow the field, to come later.

^rem-44-2

> [!definition] Definition §44.4: Derivation of $C^\infty(M)$
> A **derivation** of $C^\infty(M)$ is an $\mathbb{R}$-linear map $D : C^\infty(M) \to C^\infty(M)$ satisfying the product rule
>
> $$
> D(fg) = f\, Dg + g\, Df \qquad \text{for all } f, g \in C^\infty(M).
> $$
>
> Compare a derivation *at a point* ([[§26 Derivations and the Abstract Tangent Space#^def-26-1|Definition §26.1]]), which takes values in $\mathbb{R}$ and acts on [[§25 Germs#^def-25-2|germs]].
>
> *Lee: Ch. 8, Vector Fields as Derivations*

^def-44-4

> [!theorem] Lemma §44.2: A Vector Field Is a Derivation
> For $\mathbf{X} \in \mathfrak{X}(M)$ ([[§44 Vector Fields#^def-44-2|Def. §44.2]]) and $f \in C^\infty(M)$, the function $D_Xf : p \mapsto \mathbf{X}_p[f]$ is smooth, and $D_\mathbf{X} : C^\infty(M) \to C^\infty(M)$ is a [[§44 Vector Fields#^def-44-4|derivation]]. In a chart, $D_Xf = \sum_j \mathbf{X}^j\, \partial f/\partial x^j$. (Lee writes $\mathbf{X}f$ for $D_Xf$.)

^lem-44-2

> [!proof]+ Proof
> *(Lecture 15: linearity and the product rule are “an immediate consequence of the corresponding properties for tangent vectors”, applied at each point. Smoothness of $D_Xf$, which the lecture did not address, is filled in.)* In a chart, $\mathbf{X}_p[f] = \sum_j \mathbf{X}^j(p)\, \partial f/\partial x^j(p)$ by [[§44 Vector Fields#^prop-44-1|Proposition §44.1]], a sum of products of smooth functions. At each $p$, $\mathbf{X}_p[fg] = f(p)\, \mathbf{X}_p[g] + g(p)\, \mathbf{X}_p[f]$ because $\mathbf{X}_p$ is a derivation at $p$; that is the product rule for $D_\mathbf{X}$, and linearity is the same.

^pf-44-2

*Uses:* [[§44 Vector Fields#^def-44-4|Def. §44.4]], [[§44 Vector Fields#^def-44-2|Def. §44.2]], [[§44 Vector Fields#^prop-44-1|§44.1]], [[§26 Derivations and the Abstract Tangent Space#^def-26-1|Def. §26.1]]

The goal of this section is the converse of the lemma: every derivation of $C^\infty(M)$ comes from a vector field ([[§44 Vector Fields#^prop-44-6|Proposition §44.6]], at the end). Tangent vectors act on germs, which only see a neighbourhood of a point, while a derivation of $C^\infty(M)$ acts on functions on all of $M$. The bridge is locality ([[§44 Vector Fields#^lem-44-4|Lemma §44.4]]), and its proof needs bump functions, so these come first.

> [!definition] Definition §44.5: Local Operator
> An operator $D : C^\infty(M) \to C^\infty(M)$ is **local** if for every open $U \subseteq M$ and all $f, g \in C^\infty(M)$,
>
> $$
> f|_U = g|_U \quad \Longrightarrow \quad (Df)|_U = (Dg)|_U .
> $$

^def-44-5

“Even though $D$ a priori is defined on functions on $M$, it's actually going to be given by local data”: knowing $f$ on $U$ determines $Df$ on $U$.

> [!definition] Definition §44.6: Support
> The **support** of a function $\chi : M \to \mathbb{R}$ is the *[[§7 Interior and Closure#^def-7-new1|closure]]* of the set where it is nonzero,
>
> $$
> \operatorname{supp}\chi = \overline{\{ q \in M : \chi(q) \neq 0 \}} .
> $$
>
> *Lee: Ch. 2, Partitions of Unity*

^def-44-6

> [!definition] Definition §44.7: Compactly Supported Functions
> $C^\infty_0(M)$ is the set of smooth functions $\chi : M \to \mathbb{R}$ whose support ([[§44 Vector Fields#^def-44-6|Definition §44.6]]) is [[§15 Compact Spaces#^def-15-2|compact]].
>
> *Lee: Ch. 2, Partitions of Unity*

^def-44-7

> [!definition] Definition §44.8: Bump Function
> Let $p \in M$. A **bump function at $p$** is a $\chi \in C^\infty_0(M)$ ([[§44 Vector Fields#^def-44-7|Definition §44.7]]) with $\chi \equiv 1$ on a neighbourhood of $p$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-44-8

“It's a technical term, and it's not a joke”: the graph is a plateau, equal to $1$ near $p$ and dying off to $0$ outside a compact set — “smooth, but not analytic”, since an analytic function equal to $1$ on an open set would equal $1$ on the whole connected domain.

![[m591-44-3.svg]]
*A bump function at $p$, after the board sketch, with the front quarter cut away. $M$ is a plane, and the graph of $\chi$ is a surface over it: $\chi \equiv 1$ on a disc around $p$ (the blue plateau, at height $1$); from its edge the graph falls smoothly to $0$ (orange); and $\chi = 0$ outside the compact set $\operatorname{supp}\chi$, whose boundary is the dashed circle on $M$. The two cut faces show the profile of $\chi$ along two rays from $p$, and $p$ lies on $M$ at their inner corner, directly below the plateau, where $\chi(p) = 1$. The cross-section below shows the same profile along a whole line through $p$.*

![[m591-45-1.svg]]
*A bump function, drawn over a one-dimensional slice of $M$ (the graph is the plateau of Uribe's picture, in cross-section). It equals $1$ on a neighbourhood of $p$, is smooth everywhere, and vanishes outside its support, which is compact and lies inside the given open set $U$. This one is built from $h(t) = e^{-1/t}$ for $t > 0$, $h(t) = 0$ for $t \le 0$, as $\chi(x) = h(b - |x|)/\big(h(b - |x|) + h(|x| - a)\big)$, which is $1$ for $|x| \le a$ and $0$ for $|x| \ge b$.*

**Transcription note.** Page 41 of the handwritten notes defines $\operatorname{supp}(\chi) = \{q \in M : \chi(q) \neq 0\}$; the support is the *closure* of that set, as Uribe said (“and then you take the closure of that”). Without the closure, the support of a bump function would not be compact.

> [!theorem] Proposition §44.3: Bump Functions Exist
> For every open $U \subseteq M$ and every $p \in U$ there is a [[§44 Vector Fields#^def-44-8|bump function]] $\chi$ at $p$ with $\operatorname{supp}\chi \subseteq U$.
>
> *Lee: Proposition 2.25*

^prop-44-3

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15, to be proved next week — “the week before the exam”, so Uribe will prove “technical things that you will not be using in homework.” “The existence is not so obvious, but it's true.”

^pf-44-3

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$, smooth but not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]].
> - Bump functions were already granted (Lee, Proposition 2.25) in [[§26 Derivations and the Abstract Tangent Space#^prop-26-3|Germ Derivations and Global Derivations, §26.3]].

> [!theorem] Lemma §44.4: Derivations Are Local
> Every [[§44 Vector Fields#^def-44-4|derivation]] of $C^\infty(M)$ is a [[§44 Vector Fields#^def-44-5|local operator]].

^lem-44-4

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15; the proof “uses the existence of bump functions” ([[§44 Vector Fields#^prop-44-3|Proposition §44.3]], above) and is to come.

^pf-44-4

*Uses:* [[§44 Vector Fields#^prop-44-3|§44.3]]

> [!remark]- Connections
> - The pointwise version, a derivation of $C^\infty(M)$ at $p$ only sees a function near $p$ (Lee, Proposition 3.8), in the proof of [[§26 Derivations and the Abstract Tangent Space#^prop-26-3|Germ Derivations and Global Derivations, §26.3]].

*Lecture 15, before the proof of the lemma: “I want to make an observation.”*

> [!definition] Definition §44.9: Multiplication Operator
> For $g \in C^\infty(M)$, the **multiplication operator** $m_g : C^\infty(M) \to C^\infty(M)$ is $m_g f = g f$.

^def-44-9

> [!definition] Definition §44.10: Differential Operators
> The **ring of differential operators** on $M$, written $\mathrm{Diff}(M)$ here, is the subring of the $\mathbb{R}$-linear maps $C^\infty(M) \to C^\infty(M)$ (with sum and composition) generated by
>
> $$
> D_\mathbf{X} \quad (\mathbf{X} \in \mathfrak{X}(M)) \qquad \text{and} \qquad m_g \quad (g \in C^\infty(M)) ,
> $$
>
> the operators of [[§44 Vector Fields#^lem-44-2|Lemma §44.2]] and [[§44 Vector Fields#^def-44-9|Definition §44.9]]. Its elements, the **differential operators**, are the finite sums of finite composites of such operators.

^def-44-10

Uribe: “I can take a vector field, apply it … I can compose that with multiplication by a function, or compose it with another vector field, and do finitely many of these things, and add linear combinations of such things.” (The name $\mathrm{Diff}(M)$ is not from lecture.)

> [!example] Example §44.1: Differential Operators in Coordinates
> *(Not from lecture.)* On $M = \mathbb{R}$ with coordinate $x$, write $\partial = D_{\partial/\partial x}$. Then $P = \partial \circ \partial + m_x \circ \partial$ is a differential operator, $Pf = f'' + x f'$. On $M = \mathbb{R}^2$ the Laplacian $\Delta = \partial_x \circ \partial_x + \partial_y \circ \partial_y$ is one. Composites can always be rewritten with the multiplications in front, because of the product rule $\partial \circ m_g = m_{\partial g} + m_g \circ \partial$: for instance $\partial \circ m_x \circ \partial = \partial + m_x \circ \partial \circ \partial$, that is, $(x f')' = f' + x f''$. So in a chart a differential operator is a finite sum $\sum_\alpha a_\alpha\, \partial^\alpha$ with smooth coefficients $a_\alpha$ — “they are given by differential expressions in local coordinates.”

^ex-44-1

> [!remark] Remark: Differential Operators Are Local
> Every differential operator is a local operator ([[§44 Vector Fields#^def-44-5|Definition §44.5]]). *(Lecture 15: “these are all local operators”; the reason is filled in.)* The generators are local: $(m_g f)(p) = g(p) f(p)$ depends only on $f(p)$, and $(D_\mathbf{X} f)(p) = \mathbf{X}_p[f]$ depends only on the germ of $f$ at $p$, because $\mathbf{X}_p$ is a derivation at $p$, acting on germs ([[§26 Derivations and the Abstract Tangent Space#^def-26-1|Definition §26.1]]). Sums and composites of local operators are local: if $f|_U = g|_U$ then $(Pf)|_U = (Pg)|_U$, and applying $Q$ gives $(QPf)|_U = (QPg)|_U$.

^rem-44-3

> [!theorem] Theorem §44.5: Local Operators Are Differential Operators
> Let $P : C^\infty(M) \to C^\infty(M)$ be an $\mathbb{R}$-linear local operator. Then $P$ is a differential operator near each point: every $p \in M$ has a neighbourhood $U$ on which, in a chart, $Pf = \sum_{|\alpha| \le k} a_\alpha\, \partial^\alpha f$ for some $k$ and smooth $a_\alpha$. Conversely, every differential operator is local ([[§44 Vector Fields#^rem-44-3|Remark: Differential Operators Are Local]]).

^thm-44-5

> [!proof]+ Proof (not given in this course)
> Stated in Lecture 15 “FYI”: “There's a theorem which is that every local operator … is a differential operator, and conversely, of course, the converse is easy. … We're not going to prove this theorem, but it's true.” It is Peetre's theorem. The statement is local because on a non-compact $M$ the order $k$ need not be bounded as $p$ varies, and then $P$ is not a finite sum of composites on all of $M$.

^pf-44-5

> [!theorem] Proposition §44.6: Derivations Are Vector Fields
> Conversely, every [[§44 Vector Fields#^def-44-4|derivation]] $D$ of $C^\infty(M)$ is of the form $D = D_\mathbf{X}$ ([[§44 Vector Fields#^lem-44-2|Lemma §44.2]]) for a unique $\mathbf{X} \in \mathfrak{X}(M)$.
>
> *Lee: Proposition 8.15*

^prop-44-6

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15 as “the goal”; the proof is to come. “It's not an immediate thing at all … tangent vectors are defined in terms of germs”, local objects near a point, “whereas” a derivation of $C^\infty(M)$ “a priori” acts on functions on all of $M$. Locality ([[§44 Vector Fields#^lem-44-4|Lemma §44.4]]) bridges the two.

^pf-44-6
