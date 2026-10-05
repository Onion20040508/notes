---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 43
tags: [differentiable-manifolds, math591]
---
← [[§42 The Cotangent Bundle]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§44 Vector Fields]] →

*Stage: fields — Smooth sections of $T^{\ast}M$, a covector at every point; functions give one-forms through $d$, but not every one-form is a $df$; one-forms pull back along smooth maps, and $d$ commutes with pulling back.*

*Lecture 15. The sections of the cotangent bundle, and the operator $d$ that produces them from functions — “which will be the beginning of a chain of operators when we discuss the de Rham cohomology.”*

A one-form is a section of the cotangent bundle ([[§34 Fibrations#^def-34-2|Definition §34.2]]): it picks a covector in every fibre $T_p^{\ast}M$. Every vector bundle has sections, the zero section at least — unlike a general fibration: the Hopf fibration has none ([[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Remark in §37]]).

## One-Forms and Their Coordinates

> [!definition] Definition §43.1: One-Form
> A **one-form** (or *$1$-form*, or *covector field*) on $M$ is a smooth map
>
> $$
> \theta : M \longrightarrow T^*M
> $$
>
> such that
>
> $$
> \theta_p \in T_p^*M \qquad \text{for every } p \in M .
> $$
>
> Equivalently, $\pi \circ \theta = \mathrm{id}_M$ for the projection $\pi : T^{\ast}M \to M$: a one-form is a section of the cotangent bundle ([[§34 Fibrations#^def-34-2|Definition §34.2]]).
>
> *Lee: Ch. 11, Covector Fields*

^def-43-1

In words: a one-form chooses one covector at every point of $M$, and the choice varies smoothly. Its value at $p$ is written $\theta_p$, not $\theta(p)$; it is a linear function $\theta_p : T_pM \to \mathbb{R}$, $v \mapsto \theta_p(v)$.

> [!remark]- Connections
> - On open subsets of $\mathbb{R}^n$: [[§21 Introduction to Differential Forms#^def-21-1|452 Def. §21.1]] (differential forms, here in degree 1).
> - The value at one point is a covector, an element of a dual space: [[§30 The Cotangent Space#^def-30-1|Def. §30.1]], [[§12 Duality#^ladr-3-110|LADR 3.110]].

Uribe on the notation: “$\theta$ is really a function of two variables, a point and a vector, and you want to make room for the vector variable” — so the point goes into the subscript and the vector into the parentheses. A student asked where a $\theta_p$ comes from; the answer is that the definition describes *every* one-form, and the examples come next.

> [!definition] Definition §43.2: The Space of One-Forms
> The set of all one-forms on $M$ is written $C^\infty(M, T^{\ast}M)$ (Uribe's notation; also $\Omega^1(M)$).
>
> *Lee: Ch. 11, Covector Fields*

^def-43-2

> [!theorem] Proposition §43.1: One-Forms in Coordinates
> Let $\theta$ be a section of $T^{\ast}M \to M$ (not assumed smooth) and $(U, \varphi = (x^i))$ a chart. Then on $U$
>
> $$
> \theta = \sum_{j=1}^m \theta_j\, dx^j, \qquad \theta_j(p) = \theta_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big),
> $$
>
> and $\theta$ is smooth on $U$ if and only if the coefficient functions $\theta_1, \ldots, \theta_m$ are smooth on $U$.
>
> *Lee: Proposition 11.11*

^prop-43-1

> [!proof]+ Proof
> *(Lecture 15 stated it — “smoothness of the form will translate into these functions being smooth”; the proof is filled in.)* At each $p$ the $dx^j|_p$ form a basis of $T_p^{\ast}M$ dual to the $\partial/\partial x^j|_p$, which gives the expansion and the formula for $\theta_j(p)$. In the chart of $T^{\ast}M$ over $U$ ([[§42 The Cotangent Bundle#^def-42-5|Definition §42.5]]) and the chart $\varphi$ of $M$, the coordinate representation of $\theta$ is $r \mapsto \big(r, \theta_1(\varphi^{-1}(r)), \ldots, \theta_m(\varphi^{-1}(r))\big)$, which is smooth exactly when every $\theta_j \circ \varphi^{-1}$ is.

^pf-43-1

*Uses:* [[§43 One-Forms#^def-43-1|Def. §43.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§30 The Cotangent Space#^cor-30-3|§30.3]], [[§42 The Cotangent Bundle#^def-42-1|Def. §42.1]], [[§42 The Cotangent Bundle#^prop-42-2|§42.2]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§18 Smooth Functions and Smooth Maps#^prop-18-2|§18.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]]

## The Operator $d$

> [!theorem] Proposition §43.2: The Differential of a Function Is a One-Form
> For $f \in C^\infty(M)$, the section $df : p \mapsto df_p$ is a one-form, given in a chart by
>
> $$
> df = \sum_{j=1}^m \frac{\partial f}{\partial x^j}\, dx^j .
> $$
>
> The resulting operator $d : C^\infty(M) \to C^\infty(M, T^{\ast}M)$, $f \mapsto df$, is $\mathbb{R}$-linear and satisfies $d(fg) = f\, dg + g\, df$.
>
> *Lee: Ch. 11, The Differential of a Function*

^prop-43-2

> [!proof]+ Proof
> *(The coordinate formula is [[§30 The Cotangent Space#^lem-30-2|Lemma §30.2]], which Lecture 15 recalled; the rest is filled in.)* The coefficients $\partial f/\partial x^j$ are smooth, so $df$ is smooth by [[§43 One-Forms#^prop-43-1|Proposition §43.1]]. For $v \in T_pM$, $d(fg)_p(v) = v[fg] = f(p)\, v[g] + g(p)\, v[f]$ because $v$ is a derivation, and linearity is the same one line.

^pf-43-2

*Uses:* [[§30 The Cotangent Space#^def-30-1|Def. §30.1]], [[§30 The Cotangent Space#^prop-30-1|§30.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§26 Derivations and the Abstract Tangent Space#^def-26-1|Def. §26.1]], [[§43 One-Forms#^def-43-1|Def. §43.1]], [[§43 One-Forms#^prop-43-1|§43.1]]

> [!remark]- Connections
> - The same rules at a single point: [[§30 The Cotangent Space#^cor-30-4|§30.4]].
> - On $\mathbb{R}^3$, $d$ on functions is the gradient: [[§22 The Algebra of Differential Forms#^prop-22-2|452 §22.2]], [[§22 The Algebra of Differential Forms#^prop-22-6|452 §22.6]].

> [!example] Example §43.1: Two One-Forms on the Plane
> On $\mathbb{R}^2$ with coordinates $x, y$, any expression $a(x,y)\, dx + b(x,y)\, dy$ with smooth $a, b$ is a one-form. Uribe's two examples:
>
> $$
> \theta = \tfrac12\,(x\, dy - y\, dx), \qquad \sigma = \tfrac12\,(x\, dx + y\, dy) .
> $$
>
> $\sigma$ is the differential of a function: $\sigma = d\big(\tfrac14(x^2 + y^2)\big)$.

^ex-43-1

$\theta$ is not the differential of any function, as the next proposition shows.

> [!theorem] Proposition §43.3: A Necessary Condition for Being a Differential
> If $\theta = \sum_j \theta_j\, dx^j = df$ on a chart domain $U$ for some $f \in C^\infty(U)$, then
>
> $$
> \frac{\partial \theta_j}{\partial x^k} = \frac{\partial \theta_k}{\partial x^j} \qquad \text{for all } j, k .
> $$
>
> In particular, $\theta = \tfrac12(x\,dy - y\,dx)$ is not $df$ for any $f$ on any open subset of $\mathbb{R}^2$.

^prop-43-3

> [!proof]+ Proof
> *(Lecture 15.)* If $\theta = df$ then $\theta_j = \partial f/\partial x^j$ for every $j$ ([[§43 One-Forms#^prop-43-2|Proposition §43.2]]), and so $\partial\theta_j/\partial x^k = \partial^2 f/\partial x^k \partial x^j$. By equality of mixed partials ([[Schwarz–Clairaut Theorem|Clairaut's theorem]]) this is $\partial^2 f/\partial x^j \partial x^k = \partial\theta_k/\partial x^j$. *(Completion.)* For $\theta = \tfrac12(x\,dy - y\,dx)$, $\theta_x = -\tfrac{y}{2}$ and $\theta_y = \tfrac{x}{2}$, so $\partial\theta_y/\partial x = \tfrac12 \neq -\tfrac12 = \partial\theta_x/\partial y$.

^pf-43-3

*Uses:* [[§43 One-Forms#^prop-43-2|§43.2]], [[§43 One-Forms#^prop-43-1|§43.1]], [[§43 One-Forms#^ex-43-1|Ex. §43.1]], [[Schwarz–Clairaut Theorem|452 §5.1]]

> [!remark]- Connections
> - In 452: exact forms are closed, [[§22 The Algebra of Differential Forms#^prop-22-10|452 §22.10]] (closed and exact: [[§22 The Algebra of Differential Forms#^def-22-8|452 Def. §22.8]]); in vector-field language, a gradient field is irrotational, [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|452 Def. §11.1]].

“You know this from multivariable calculus in various different forms. Not every vector field is a gradient field”: the condition is the vanishing of the curl, “a curl condition.”

![[m591-44-1.svg]]
*The two forms of [[§43 One-Forms#^ex-43-1|Example §43.1]], drawn as arrows. A one-form is not an arrow — it eats arrows — so the picture uses the Euclidean dot product to turn $a\,dx + b\,dy$ into the vector $(a, b)$; this identification is available in $\mathbb{R}^2$, not on a general manifold, and it is how “$df$” becomes the “gradient” of calculus. Right: $\sigma = df$ for $f = \tfrac14(x^2+y^2)$, and its arrows cross the level circles of $f$ at right angles, as a gradient's must. Left: $\theta$'s arrows run along the circles. If $\theta$ were $df$, then $f$ would increase steadily all the way around a circle and return to its starting value — impossible.*

> [!remark] Remark: The Condition Is Not Sufficient
> The mixed-partials condition is necessary but not sufficient, and Uribe flagged this as “the beginning of de Rham theory”: whether it suffices “has to do with the topology of the domain.” The standard example (Lee, Example 11.36; not from lecture) is
>
> $$
> \omega = \frac{x\, dy - y\, dx}{x^2 + y^2} \quad \text{on } \mathbb{R}^2 \setminus \{0\} .
> $$
>
> It satisfies the condition: both mixed partials equal $(y^2 - x^2)/(x^2 + y^2)^2$. But it is not $df$. Along the circle $c(t) = (\cos t, \sin t)$, with velocity $c'(t) = -\sin t\, \partial_x + \cos t\, \partial_y$ ([[§29 Tangent Vectors as Velocities of Curves|§29]]), one finds $\omega(c'(t)) = 1$. If $\omega = df$, then $(f \circ c)'(t) = df(c'(t)) = 1$, so $f(c(2\pi)) - f(c(0)) = 2\pi$; but $c(2\pi) = c(0)$. The hole at the origin is what makes this possible: on all of $\mathbb{R}^2$ — indeed on any star-shaped domain — the condition is sufficient (Lee, Corollary 11.50).

^rem-43-1

> [!remark]- Connections
> - The same form in 452, closed but not exact: [[§22 The Algebra of Differential Forms#^prop-22-11|452 §22.11]]; sufficiency on star-shaped domains: [[Poincaré Lemma|452 §22.12]].

## Pullbacks of One-Forms

> [!definition] Definition §43.3: Pullback of One-Forms
> Let $F : M \to N$ be smooth. The **pullback** of functions is $F^{\ast}f = f \circ F$. For a one-form $\theta$ on $N$, the **pullback** $F^{\ast}\theta$ is the section of $T^{\ast}M$ whose value at $p$ is the pullback of the covector $\theta_{F(p)}$ ([[§30 The Cotangent Space#^def-30-5|Definition §30.5]]):
>
> $$
> (F^*\theta)_p = F_p^*\big(\theta_{F(p)}\big), \qquad (F^*\theta)_p(v) = \theta_{F(p)}\big(F_{*p}v\big) .
> $$
>
> It is smooth, hence a one-form, by [[§43 One-Forms#^prop-43-5|Proposition §43.5]] below.
>
> *Lee: Ch. 11, Pullbacks of Covector Fields*

^def-43-3

> [!remark]- Connections
> - At each point $F_p^{\ast}$ is the dual map of $F_{\ast p}$: [[§12 Duality#^ladr-3-118|LADR 3.118]]. On open subsets of $\mathbb{R}^n$: [[§22 The Algebra of Differential Forms#^def-22-3|452 Def. §22.3]].

> [!theorem] Corollary §43.4: Pullback Commutes with $d$
> Let $F : M \to N$ be smooth and $f \in C^\infty(N)$. Then $F^{\ast}(df) = d(F^{\ast}f)$ as one-forms on $M$.
>
> *Lee: Proposition 11.25*

^cor-43-4

> [!proof]+ Proof
> *(Lecture 15 stated it in this form, “one says that the pullback map commutes with $d$”.)* At each $p \in M$ the two sides are $F_p^{\ast}(df_{F(p)})$ and $d(f \circ F)_p$, which agree by [[§30 The Cotangent Space#^prop-30-10|Proposition §30.10]].

^pf-43-4

*Uses:* [[§43 One-Forms#^def-43-3|Def. §43.3]], [[§43 One-Forms#^prop-43-2|§43.2]], [[§30 The Cotangent Space#^prop-30-10|§30.10]]

> [!theorem] Proposition §43.5: Pullbacks in Coordinates
> In charts $(x^i)$ on $M$ and $(y^j)$ on $N$, with $F^j = y^j \circ F$,
>
> $$
> F^*\Big(\sum_j \theta_j\, dy^j\Big) = \sum_i \Big( \sum_j (\theta_j \circ F)\, \frac{\partial F^j}{\partial x^i} \Big)\, dx^i .
> $$
>
> In particular $F^{\ast}\theta$ is smooth whenever $\theta$ is.

^prop-43-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Evaluate both sides on $\partial/\partial x^i|_p$: by definition the left side gives $\sum_j \theta_j(F(p))\, dy^j|_{F(p)}\big(F_{\ast p}\, \partial/\partial x^i|_p\big)$, and $F_{\ast p}\, \partial/\partial x^i|_p = \sum_j \partial F^j/\partial x^i(p)\, \partial/\partial y^j|_{F(p)}$ ([[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2]]). Smoothness follows from [[§43 One-Forms#^prop-43-1|Proposition §43.1]].

^pf-43-5

*Uses:* [[§43 One-Forms#^def-43-3|Def. §43.3]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§30 The Cotangent Space#^cor-30-3|§30.3]], [[§43 One-Forms#^prop-43-1|§43.1]]

> [!remark]- Connections
> - The substitution $dx_i = \sum_j (\partial x_i/\partial u_j)\, du_j$ of 452: [[§22 The Algebra of Differential Forms#^def-22-3|452 Def. §22.3]]; the matrix of a dual map is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
