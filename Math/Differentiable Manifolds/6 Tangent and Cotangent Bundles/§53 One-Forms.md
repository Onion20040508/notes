---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 53
tags: [differentiable-manifolds, math591]
---
← [[§52 The Cotangent Bundle]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§54 Critical Points and the Hessian]] →

*Stage: fields — Smooth sections of $T^{\ast}M$, a covector at every point; functions give one-forms through $d$, but not every one-form is a $df$; one-forms pull back along smooth maps, and $d$ commutes with pulling back.*

*Lecture 15. The sections of the cotangent bundle, and the operator $d$ that produces them from functions — “which will be the beginning of a chain of operators when we discuss the de Rham cohomology.”*

A one-form is a section of the cotangent bundle ([[§40 Fibrations#^def-40-3|Definition §40.3]]): it picks a covector in every fibre $T_p^{\ast}M$. Every vector bundle has sections, the zero section at least — unlike a general fibration: the Hopf fibration has none ([[§46 Projective Spaces and the Hopf Fibration#^rem-46-1|Remark: Sections Need Not Exist]]).

## One-Forms and Their Coordinates

> [!definition] Definition §53.1: One-Form
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
> Equivalently, $\pi \circ \theta = \mathrm{id}_M$ for the projection $\pi : T^{\ast}M \to M$: a one-form is a section of the cotangent bundle ([[§40 Fibrations#^def-40-3|Definition §40.3]]).
>
> *Lee: Ch. 11, Covector Fields*

^def-53-1

In words: a one-form chooses one covector at every point of $M$, and the choice varies smoothly. Its value at $p$ is written $\theta_p$, not $\theta(p)$; it is a linear function $\theta_p : T_pM \to \mathbb{R}$, $v \mapsto \theta_p(v)$.

> [!remark]- Connections
> - On open subsets of $\mathbb{R}^n$: [[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]] (differential forms, here in degree 1).
> - The value at one point is a covector, an element of a dual space: [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§12 Duality#^ladr-3-110|LADR 3.110]].

Uribe on the notation: “$\theta$ is really a function of two variables, a point and a vector, and you want to make room for the vector variable” — so the point goes into the subscript and the vector into the parentheses. A student asked where a $\theta_p$ comes from; the answer is that the definition describes *every* one-form, and the examples come next.

> [!definition] Definition §53.2: The Space of One-Forms
> The set of all one-forms on $M$ is written $C^\infty(M, T^{\ast}M)$ (Uribe's notation; also $\Omega^1(M)$).
>
> *Lee: Ch. 11, Covector Fields*

^def-53-2

> [!theorem] Proposition §53.1: One-Forms in Coordinates
> Let $\theta$ be a section of $T^{\ast}M \to M$ (not assumed smooth) and $(U, \varphi = (x^i))$ a chart.
>
> 1. On $U$,
>
> $$
> \theta = \sum_{j=1}^m \theta_j\, dx^j, \qquad \theta_j(p) = \theta_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big).
> $$
>
> 2. $\theta$ maps $U$ into $T^{\ast}U$, and its coordinate representation in the charts $(U, \varphi)$ of $M$ and $(T^{\ast}U, \hat\varphi)$ of $T^{\ast}M$ (Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]]) is
>
> $$
> \hat\varphi \circ \theta \circ \varphi^{-1}(r) = \big(r,\ \theta_1(\varphi^{-1}(r)), \ldots, \theta_m(\varphi^{-1}(r))\big), \qquad r \in \varphi(U) .
> $$
>
> 3. $\theta$ is smooth on $U$ if and only if the coefficient functions $\theta_1, \ldots, \theta_m$ are smooth on $U$.
>
> *Lee: Proposition 11.11*

^prop-53-1

> [!proof]+ Proof
> *(Lecture 15 stated it — “smoothness of the form will translate into these functions being smooth”; the proof is filled in.)* Three things are claimed: the expansion of $\theta$ on $U$ with the stated coefficients, (1); the coordinate representation, (2); and the smoothness criterion, (3). Since $\theta$ is a section, $\pi \circ \theta = \mathrm{id}_M$, so $\theta(p) = (p, \theta_p)$ with $\theta_p \in T_p^{\ast}M$ for every $p$.
>
> *(1) The expansion.* The equation $\theta = \sum_j \theta_j\, dx^j$ on $U$ means $\theta_p = \sum_j \theta_j(p)\, dx^j|_p$ for every $p \in U$. At each $p \in U$ the $dx^j|_p$ form a basis of $T_p^{\ast}M$ dual to the $\partial/\partial x^j|_p$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), and Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]] with $\alpha = \theta_p$ gives
>
> $$
> \theta_p = \sum_{j=1}^m \theta_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big)\, dx^j\big|_p = \sum_{j=1}^m \theta_j(p)\, dx^j\big|_p ,
> $$
>
> which is the expansion, with $\theta_j(p) = \theta_p(\partial/\partial x^j|_p)$.
>
> *(2) The coordinate representation.* Since $\pi(\theta(p)) = p$, $\theta$ maps $U$ into $T^{\ast}U = \pi^{-1}(U)$, so the charts $(U, \varphi)$ of $M$ and $(T^{\ast}U, \hat\varphi)$ of $T^{\ast}M$ (Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]]) are admissible for $\theta|_U$. For $r \in \varphi(U)$ put $p = \varphi^{-1}(r)$; by Definition [[§52 The Cotangent Bundle#^def-52-5|§52.5]], whose last $m$ entries are the components $\theta_p(\partial/\partial x^j|_p) = \theta_j(p)$,
>
> $$
> \hat\varphi \circ \theta \circ \varphi^{-1}(r) = \hat\varphi(p, \theta_p) = \big(\varphi(p), \theta_1(p), \ldots, \theta_m(p)\big) = \big(r,\ \theta_1(\varphi^{-1}(r)), \ldots, \theta_m(\varphi^{-1}(r))\big) .
> $$
>
> A map into $\mathbb{R}^{2m}$ is smooth exactly when all its components are; the first $m$ components, $r \mapsto r$, are smooth. So this coordinate representation is smooth exactly when every $\theta_j \circ \varphi^{-1}$ is smooth on $\varphi(U)$.
>
> *(3) If $\theta$ is smooth on $U$,* then its coordinate representation in these charts is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]), so every $\theta_j \circ \varphi^{-1}$ is smooth on $\varphi(U)$; this is the coordinate representation $(\theta_j)_\varphi$ of $\theta_j$, so $\theta_j$ is smooth on $U$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]], with the chart $(U, \varphi)$ at every point).
>
> *If every $\theta_j$ is smooth on $U$,* then each $\theta_j \circ \varphi^{-1}$ is smooth on $\varphi(U)$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], applied on the manifold $U$ with its chart $(U, \varphi)$), so the coordinate representation above is smooth. Moreover $\theta|_U$ is continuous: it equals $\hat\varphi^{-1} \circ (\hat\varphi \circ \theta \circ \varphi^{-1}) \circ \varphi$, a composite of continuous maps ($\hat\varphi$ is a homeomorphism by Proposition [[§52 The Cotangent Bundle#^prop-52-2|§52.2]]). So $\theta$ is smooth on $U$ by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], using these two charts at every point of $U$.

^pf-53-1

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§52 The Cotangent Bundle#^def-52-5|Def. §52.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§52 The Cotangent Bundle#^prop-52-2|§52.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]

## The Operator $d$

> [!theorem] Proposition §53.2: The Differential of a Function Is a One-Form
> For $f \in C^\infty(M)$, the section $df : p \mapsto df_p$ is a one-form, given in a chart by
>
> $$
> df = \sum_{j=1}^m \frac{\partial f}{\partial x^j}\, dx^j .
> $$
>
> The resulting operator $d : C^\infty(M) \to C^\infty(M, T^{\ast}M)$, $f \mapsto df$, is $\mathbb{R}$-linear and satisfies $d(fg) = f\, dg + g\, df$.
>
> *Lee: Ch. 11, The Differential of a Function*

^prop-53-2

> [!proof]+ Proof
> *(The coordinate formula is Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], which Lecture 15 recalled; the rest is filled in.)* Four things are claimed: $df$ is a section of $T^{\ast}M$, it has the stated coordinate formula, it is smooth, and $d$ is linear and satisfies the product rule.
>
> *A section, and the formula.* For each $p \in M$, $df_p \in T_p^{\ast}M$ (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]), so $df(p) = (p, df_p)$ satisfies $\pi \circ df = \mathrm{id}_M$. In a chart $(U, \varphi = (x^j))$, Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] at each $p \in U$ gives $df_p = \sum_j \partial f/\partial x^j(p)\, dx^j|_p$, which is the formula $df = \sum_j (\partial f/\partial x^j)\, dx^j$ on $U$; its coefficient functions are $\partial f/\partial x^j : U \to \mathbb{R}$, in agreement with Proposition [[§53 One-Forms#^prop-53-1|§53.1]], since $df_p(\partial/\partial x^j|_p) = \partial f/\partial x^j(p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]).
>
> *Smoothness.* The coefficients $\partial f/\partial x^j$ are smooth on $U$: Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to the restriction of $f$ to the chart domain $U$ (smooth, as $f \in C^\infty(M)$), gives $\partial f/\partial x^j \in C^\infty(U)$, with $(\partial f/\partial x^j) \circ \varphi^{-1} = \partial f_\varphi/\partial r^j$ on $\varphi(U)$. By Proposition [[§53 One-Forms#^prop-53-1|§53.1]](3), $df$ is smooth on $U$. The chart domains cover $M$, and smoothness of a map is checked near each point (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), so $df$ is smooth on $M$: a one-form, $df \in C^\infty(M, T^{\ast}M)$.
>
> *Linearity and the product rule.* One-forms are added, and multiplied by functions, pointwise: $(a\,\theta + b\,\sigma)_p = a\,\theta_p + b\,\sigma_p$ and $(f\theta)_p = f(p)\,\theta_p$. So the two identities are equalities of covectors at each $p$, and two covectors are equal when they agree at every $v \in T_pM$. Fix $p$ and $v \in T_pM$, and let $f, g \in C^\infty(M)$, $a, b \in \mathbb{R}$. By Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] ($dk_p(v) = v[k]$), the $\mathbb{R}$-linearity of the derivation $v$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]), and the pointwise operations of $T_p^{\ast}M$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]),
>
> $$
> d(af + bg)_p(v) = v[af + bg] = a\, v[f] + b\, v[g] = a\, df_p(v) + b\, dg_p(v) = \big(a\, df_p + b\, dg_p\big)(v) ;
> $$
>
> and, by the Leibniz rule of $v$ instead of its linearity,
>
> $$
> d(fg)_p(v) = v[fg] = f(p)\, v[g] + g(p)\, v[f] = f(p)\, dg_p(v) + g(p)\, df_p(v) = \big(f(p)\, dg_p + g(p)\, df_p\big)(v) .
> $$
>
> These are Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]](1) and (2) at the point $p$. As $p$ and $v$ were arbitrary, $d(af + bg) = a\, df + b\, dg$ and $d(fg) = f\, dg + g\, df$.

^pf-53-2

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§53 One-Forms#^prop-53-1|§53.1]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§32 The Cotangent Space#^cor-32-3|§32.3]]

> [!remark]- Connections
> - The same rules at a single point: [[§32 The Cotangent Space#^cor-32-3|§32.3]].
> - On $\mathbb{R}^3$, $d$ on functions is the gradient: [[§38 The Exterior Derivative#^prop-38-1|452 §38.1]], [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1]].

> [!example] Example §53.1: Two One-Forms on the Plane
> On $\mathbb{R}^2$ with coordinates $x, y$, any expression $a(x,y)\, dx + b(x,y)\, dy$ with smooth $a, b$ is a one-form. Uribe's two examples:
>
> $$
> \theta = \tfrac12\,(x\, dy - y\, dx), \qquad \sigma = \tfrac12\,(x\, dx + y\, dy) .
> $$
>
> $\sigma$ is the differential of a function: $\sigma = d\big(\tfrac14(x^2 + y^2)\big)$.

^ex-53-1

$\theta$ is not the differential of any function, as the next proposition shows.

> [!theorem] Proposition §53.3: A Necessary Condition for Being a Differential
> If $\theta = \sum_j \theta_j\, dx^j = df$ on a chart domain $U$ for some $f \in C^\infty(U)$, then
>
> $$
> \frac{\partial \theta_j}{\partial x^k} = \frac{\partial \theta_k}{\partial x^j} \qquad \text{for all } j, k .
> $$
>
> In particular, $\theta = \tfrac12(x\,dy - y\,dx)$ is not $df$ for any $f$ on any open subset of $\mathbb{R}^2$.

^prop-53-3

> [!proof]+ Proof
> *(Lecture 15.)* *The condition.* Suppose $\theta = df$ on $U$. Then $\theta_p = df_p$ for every $p \in U$, and the coefficients of a covector in the basis $dx^j|_p$ are unique (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]); comparing $\theta_p = \sum_j \theta_j(p)\, dx^j|_p$ with $df_p = \sum_j \partial f/\partial x^j(p)\, dx^j|_p$ (Proposition [[§53 One-Forms#^prop-53-2|§53.2]]) gives $\theta_j = \partial f/\partial x^j$ for every $j$. By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], $(\partial f/\partial x^j) \circ \varphi^{-1} = \partial f_\varphi/\partial r^j$ on $\varphi(U)$, where $f_\varphi = f \circ \varphi^{-1}$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]). Applying Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] once more, now to the function $\theta_j$,
>
> $$
> \frac{\partial \theta_j}{\partial x^k}(p) = \frac{\partial (\theta_j \circ \varphi^{-1})}{\partial r^k}\big(\varphi(p)\big) = \frac{\partial}{\partial r^k}\Big(\frac{\partial f_\varphi}{\partial r^j}\Big)\big(\varphi(p)\big) = \frac{\partial^2 f_\varphi}{\partial r^k\, \partial r^j}\big(\varphi(p)\big) ,
> $$
>
> which is what $\partial\theta_j/\partial x^k = \partial^2 f/\partial x^k \partial x^j$ means. By equality of mixed partials (Clairaut's theorem) for the smooth function $f_\varphi$ on the open set $\varphi(U)$, this is $\partial^2 f_\varphi/\partial r^j\, \partial r^k(\varphi(p))$, i.e. $\partial^2 f/\partial x^j \partial x^k$, and the same computation with $j$ and $k$ exchanged identifies it with $\partial\theta_k/\partial x^j(p)$. So $\partial\theta_j/\partial x^k = \partial\theta_k/\partial x^j$ on $U$.
>
> *(Completion.)* *The example.* Let $W \subseteq \mathbb{R}^2$ be a nonempty open set and suppose $\theta = \tfrac12(x\,dy - y\,dx) = df$ on $W$ for some $f \in C^\infty(W)$. $W$ is a chart domain, with the chart $\mathrm{id}_W$ and coordinates $x, y$; in it, coordinate partial derivatives are the ordinary ones (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] with $\varphi = \mathrm{id}$). The coefficients of $\theta$ are read off from $\theta = -\tfrac{y}{2}\, dx + \tfrac{x}{2}\, dy$: $\theta_x = -\tfrac{y}{2}$ and $\theta_y = \tfrac{x}{2}$. The condition just proved, with $j = x$ and $k = y$, would require $\partial\theta_y/\partial x = \partial\theta_x/\partial y$ at every point of $W$. But at every point
>
> $$
> \frac{\partial\theta_y}{\partial x} = \frac{\partial}{\partial x}\Big(\frac{x}{2}\Big) = \tfrac12 \neq -\tfrac12 = \frac{\partial}{\partial y}\Big(-\frac{y}{2}\Big) = \frac{\partial\theta_x}{\partial y} ,
> $$
>
> and $W$ has at least one point. So no such $f$ exists.

^pf-53-3

*Uses:* [[§53 One-Forms#^prop-53-2|§53.2]], [[§53 One-Forms#^prop-53-1|§53.1]], [[§53 One-Forms#^ex-53-1|Ex. §53.1]], [[Schwarz–Clairaut Theorem|452 §6.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]]

> [!remark]- Connections
> - In 452: exact forms are closed, [[§39 Closed and Exact Forms#^prop-39-5|452 §39.5]] (closed and exact: [[§39 Closed and Exact Forms#^def-39-2|452 Def. §39.2]]); in vector-field language, a gradient field is irrotational, [[§13 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-13-2|452 Def. §13.2]].

“You know this from multivariable calculus in various different forms. Not every vector field is a gradient field”: the condition is the vanishing of the curl, “a curl condition.”

![[m591-44-1.svg]]
*The two forms of [[§53 One-Forms#^ex-53-1|Example §53.1]], drawn as arrows. A one-form is not an arrow — it eats arrows — so the picture uses the Euclidean dot product to turn $a\,dx + b\,dy$ into the vector $(a, b)$; this identification is available in $\mathbb{R}^2$, not on a general manifold, and it is how “$df$” becomes the “gradient” of calculus. Right: $\sigma = df$ for $f = \tfrac14(x^2+y^2)$, and its arrows cross the level circles of $f$ at right angles, as a gradient's must. Left: $\theta$'s arrows run along the circles. If $\theta$ were $df$, then $f$ would increase steadily all the way around a circle and return to its starting value — impossible.*

> [!remark] Remark: The Condition Is Not Sufficient
> The mixed-partials condition is necessary but not sufficient, and Uribe flagged this as “the beginning of de Rham theory”: whether it suffices “has to do with the topology of the domain.” The standard example (Lee, Example 11.36; not from lecture) is
>
> $$
> \omega = \frac{x\, dy - y\, dx}{x^2 + y^2} \quad \text{on } \mathbb{R}^2 \setminus \{0\} .
> $$
>
> It satisfies the condition: both mixed partials equal $(y^2 - x^2)/(x^2 + y^2)^2$. But it is not $df$. Along the circle $c(t) = (\cos t, \sin t)$, with velocity $c'(t) = -\sin t\, \partial_x + \cos t\, \partial_y$ ([[§31 Tangent Vectors as Velocities of Curves|§31]]), one finds $\omega(c'(t)) = 1$. If $\omega = df$, then $(f \circ c)'(t) = df(c'(t)) = 1$, so $f(c(2\pi)) - f(c(0)) = 2\pi$; but $c(2\pi) = c(0)$. The hole at the origin is what makes this possible: on all of $\mathbb{R}^2$ — indeed on any star-shaped domain — the condition is sufficient (Lee, Corollary 11.50).

^rem-53-1

> [!example] Example §53.2: The Angle Form on the Punctured Plane
> *(Not from lecture; added on request: the remark above, written out.)* The form is $\omega = (x\,dy - y\,dx)/(x^2+y^2)$. Names, used below: a one-form $\omega$ is **closed** if its coefficients satisfy the mixed-partials condition of Proposition [[§53 One-Forms#^prop-53-3|§53.3]] in every chart, and **exact** if $\omega = df$ for some smooth function $f$. Proposition [[§53 One-Forms#^prop-53-3|§53.3]] says exact $\Rightarrow$ closed. This example shows closed $\not\Rightarrow$ exact.
>
> 1. *The manifold.* $M = \mathbb{R}^2 \setminus \{0\}$, an open subset of $\mathbb{R}^2$, hence an open submanifold (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]), with the single chart $\mathrm{id}_M$ and coordinates $x, y$. Its coordinate derivations $\partial_x, \partial_y$ are the ordinary partial derivatives.
> 2. *The one-form.* $\omega = a\, dx + b\, dy$ with coefficient functions
>
> $$
> a, b : M \to \mathbb{R}, \qquad a(x,y) = \frac{-y}{x^2 + y^2}, \qquad b(x,y) = \frac{x}{x^2 + y^2} .
> $$
>
> They are smooth on $M$ because $x^2 + y^2 > 0$ there; so $\omega$ is a one-form on $M$ (Proposition [[§53 One-Forms#^prop-53-1|§53.1]]): at each $p \in M$ it is the covector $\omega_p = a(p)\, dx|_p + b(p)\, dy|_p \in T_p^{\ast}M$, a linear map $T_pM \to \mathbb{R}$. It is not defined at $0$.
> 3. *$\omega$ is closed.* By the quotient rule,
>
> $$
> \frac{\partial b}{\partial x} = \frac{(x^2 + y^2) - x \cdot 2x}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2},
> \qquad
> \frac{\partial a}{\partial y} = -\frac{(x^2 + y^2) - y \cdot 2y}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} ,
> $$
>
> so $\partial a/\partial y = \partial b/\partial x$ on $M$: the necessary condition of Proposition [[§53 One-Forms#^prop-53-3|§53.3]] holds. (Compare $\theta = \tfrac12(x\,dy - y\,dx)$ of Example [[§53 One-Forms#^ex-53-1|§53.1]], where the two sides are $\tfrac12$ and $-\tfrac12$.)
> 4. *The test curve.* $c : \mathbb{R} \to M$, $c(t) = (\cos t, \sin t)$, the unit circle run once around in time $2\pi$. It is smooth and lands in $M$ ($|c(t)| = 1$). Its velocity at time $t$ is the tangent vector (Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], components $(x \circ c)'(t)$, $(y \circ c)'(t)$)
>
> $$
> D_c(t) = -\sin t\; \partial_x|_{c(t)} + \cos t\; \partial_y|_{c(t)} \in T_{c(t)}M .
> $$
>
> 5. *$\omega$ along the curve.* Evaluating the covector $\omega_{c(t)}$ on this tangent vector, with $x^2 + y^2 = 1$ on the circle,
>
> $$
> \omega_{c(t)}\big(D_c(t)\big) = a(c(t))\,(-\sin t) + b(c(t))\,\cos t = (-\sin t)(-\sin t) + (\cos t)(\cos t) = 1 \qquad \text{for every } t .
> $$
>
> 6. *$\omega$ is not exact.* Suppose $\omega = df$ for some $f \in C^\infty(M)$. The function $f \circ c : \mathbb{R} \to \mathbb{R}$ is smooth, and by the definition of the velocity (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]) and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]],
>
> $$
> (f \circ c)'(t) = D_c(t)[f] = df_{c(t)}\big(D_c(t)\big) = \omega_{c(t)}\big(D_c(t)\big) = 1 .
> $$
>
> By the fundamental theorem of calculus, $f(c(2\pi)) - f(c(0)) = \int_0^{2\pi} (f \circ c)'(t)\, dt = 2\pi$. But $c(2\pi) = (1, 0) = c(0)$, so the left side is $0$. Contradiction: no such $f$ exists on $M$.
> 7. *What $f$ would have to be: the angle.* Let $U = M \setminus \{(x, 0) : x < 0\}$, the plane slit along the negative $x$-axis, and $\vartheta : U \to (-\pi, \pi)$ the polar angle, so that $x = r\cos\vartheta$, $y = r\sin\vartheta$ with $r = \sqrt{x^2 + y^2}$ (the polar coordinates of Example [[§30 The Differential in Coordinates#^ex-30-1|§30.1]]; $(r, \vartheta)$ is a chart on $U$, so $\vartheta$ is smooth there). In that chart
>
> $$
> dx = \cos\vartheta\, dr - r\sin\vartheta\, d\vartheta, \qquad dy = \sin\vartheta\, dr + r\cos\vartheta\, d\vartheta ,
> $$
>
> $$
> x\,dy - y\,dx = r\cos\vartheta\,(\sin\vartheta\, dr + r\cos\vartheta\, d\vartheta) - r\sin\vartheta\,(\cos\vartheta\, dr - r\sin\vartheta\, d\vartheta) = r^2\, d\vartheta ,
> $$
>
> so $\omega = r^2\, d\vartheta / r^2 = d\vartheta$ on $U$: on the slit plane $\omega$ *is* exact, with $f = \vartheta$. The obstruction is global: going once around the hole, $\vartheta$ increases by $2\pi$ (step 6), so it cannot be continued continuously across the slit, where it jumps from near $\pi$ (just above) to near $-\pi$ (just below). Any $f$ with $df = \omega$ on all of $M$ would be such a continuation (two functions with the same differential on a connected open set differ by a constant).
> 8. *Why the hole matters.* On $\mathbb{R}^2$ itself, or on any star-shaped open set (a disk, the slit plane $U$), a closed form is exact (Poincaré lemma; Lee, Corollary 11.50, not proved in these notes). $M$ is not star-shaped, and step 6 shows the lemma cannot extend to it: whether closed forms are exact depends on the topology of the domain, which is what de Rham cohomology measures.

^ex-53-2

![[m591-51-1.svg]]

> [!remark]- Connections
> - The same form in 452, closed but not exact: [[§39 Closed and Exact Forms#^prop-39-6|452 §39.6]]; sufficiency on star-shaped domains: [[Poincaré Lemma|452 §39.7]].

## Pullbacks of One-Forms

> [!definition] Definition §53.3: Pullback of Functions
> Let $F : M \to N$ be smooth. The **pullback** of functions is $F^{\ast}f = f \circ F$.
>
> *Lee: Ch. 11, Pullbacks of Covector Fields*

^def-53-3

> [!definition] Definition §53.4: Pullback of One-Forms
> Let $F : M \to N$ be smooth. For a one-form $\theta$ on $N$, the **pullback** $F^{\ast}\theta$ is the section of $T^{\ast}M$ whose value at $p$ is the pullback of the covector $\theta_{F(p)}$ ([[§34 The Cotangent Space from Germs#^def-34-3|Definition §34.3]]):
>
> $$
> (F^*\theta)_p = F_p^*\big(\theta_{F(p)}\big), \qquad (F^*\theta)_p(v) = \theta_{F(p)}\big(F_{*p}v\big) .
> $$
>
> It is smooth, hence a one-form, by [[§53 One-Forms#^prop-53-5|Proposition §53.5]] below.
>
> *Lee: Ch. 11, Pullbacks of Covector Fields*

^def-53-4

> [!remark]- Connections
> - At each point $F_p^{\ast}$ is the dual map of $F_{\ast p}$: [[§12 Duality#^ladr-3-118|LADR 3.118]]. On open subsets of $\mathbb{R}^n$: [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]].

> [!theorem] Corollary §53.4: Pullback Commutes with $d$
> Let $F : M \to N$ be smooth and $f \in C^\infty(N)$. Then $F^{\ast}(df) = d(F^{\ast}f)$ as one-forms on $M$.
>
> *Lee: Proposition 11.25*

^cor-53-4

> [!proof]+ Proof
> *(Lecture 15 stated it in this form, “one says that the pullback map commutes with $d$”.)* Both sides are sections of $T^{\ast}M$, and two sections are equal when their values agree at every point; so fix $p \in M$ and compute the two values.
>
> *Left side.* By Proposition [[§53 One-Forms#^prop-53-2|§53.2]], $df$ is a one-form on $N$ whose value at $F(p)$ is $df_{F(p)}$. By Definition [[§53 One-Forms#^def-53-4|§53.4]] with $\theta = df$,
>
> $$
> \big(F^{\ast}(df)\big)_p = F_p^{\ast}\big((df)_{F(p)}\big) = F_p^{\ast}\big(df_{F(p)}\big) .
> $$
>
> *Right side.* By Definition [[§53 One-Forms#^def-53-3|§53.3]], $F^{\ast}f = f \circ F$, which is smooth on $M$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]); so $d(F^{\ast}f)$ is a one-form on $M$ (Proposition [[§53 One-Forms#^prop-53-2|§53.2]]) with value $d(f \circ F)_p$ at $p$.
>
> *Comparison.* Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], applied to this $F$, the point $p$, and $f$ (smooth on $N$, so in particular near $F(p)$), gives $F_p^{\ast}\big(df_{F(p)}\big) = d(f \circ F)_p$ in $T_p^{\ast}M$. So the two sides agree at $p$, and $p$ was arbitrary.

^pf-53-4

*Uses:* [[§53 One-Forms#^def-53-3|Def. §53.3]], [[§53 One-Forms#^def-53-4|Def. §53.4]], [[§53 One-Forms#^prop-53-2|§53.2]], [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]

> [!theorem] Proposition §53.5: Pullbacks in Coordinates
> In charts $(x^i)$ on $M$ and $(y^j)$ on $N$, with $F^j = y^j \circ F$,
>
> $$
> F^*\Big(\sum_j \theta_j\, dy^j\Big) = \sum_i \Big( \sum_j (\theta_j \circ F)\, \frac{\partial F^j}{\partial x^i} \Big)\, dx^i .
> $$
> In matrix form, with $m = \dim M$ and $n = \dim N$, the column of coefficients of $F^{\ast}\theta$ is the transpose of the Jacobian $\big[\partial F^j/\partial x^i\big]$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]) applied to the column of the $\theta_j \circ F$:
>
> $$
> \begin{pmatrix}
> \sum_j (\theta_j \circ F)\, \dfrac{\partial F^j}{\partial x^1} \\ \vdots \\ \sum_j (\theta_j \circ F)\, \dfrac{\partial F^j}{\partial x^m}
> \end{pmatrix}
> =
> \begin{pmatrix}
> \dfrac{\partial F^1}{\partial x^1} & \cdots & \dfrac{\partial F^n}{\partial x^1} \\
> \vdots & \ddots & \vdots \\
> \dfrac{\partial F^1}{\partial x^m} & \cdots & \dfrac{\partial F^n}{\partial x^m}
> \end{pmatrix}
> \begin{pmatrix} \theta_1 \circ F \\ \vdots \\ \theta_n \circ F \end{pmatrix} .
> $$
>
> In particular $F^{\ast}\theta$ is smooth whenever $\theta$ is.

^prop-53-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $(U, \varphi = (x^i))$ and $(V, \psi = (y^j))$ be the charts, with $F(U) \subseteq V$ so that $F^j = y^j \circ F$ is defined on $U$ (otherwise replace $U$ by $U \cap F^{-1}(V)$, open since $F$ is continuous; the restriction of $\varphi$ to it is a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)). Write $\theta = \sum_j \theta_j\, dy^j$ on $V$, with $\theta_j(q) = \theta_q(\partial/\partial y^j|_q)$ (Proposition [[§53 One-Forms#^prop-53-1|§53.1]]), and let $c_i = \sum_j (\theta_j \circ F)\, \partial F^j/\partial x^i$ be the coefficients on the right. Two things are claimed: the identity on $U$, and the smoothness of $F^{\ast}\theta$.
>
> *The identity.* Fix $p \in U$. Both sides have values in $T_p^{\ast}M$, linear functionals on $T_pM$, so by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2) it suffices that they agree on each basis vector $\partial/\partial x^i|_p$. The right side, evaluated pointwise and using $dx^l|_p(\partial/\partial x^i|_p) = \delta^l_i$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), gives $\sum_l c_l(p)\, \delta^l_i = c_i(p)$. For the left side, use in turn Definition [[§53 One-Forms#^def-53-4|§53.4]]; the expansion $\theta_{F(p)} = \sum_k \theta_k(F(p))\, dy^k|_{F(p)}$; the formula $F_{\ast p}\, \partial/\partial x^i|_p = \sum_j \partial F^j/\partial x^i(p)\, \partial/\partial y^j|_{F(p)}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]); linearity of the covectors $dy^k|_{F(p)}$; and $dy^k|_{F(p)}(\partial/\partial y^j|_{F(p)}) = \delta^k_j$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]):
>
> $$
> \begin{aligned}
> (F^{\ast}\theta)_p\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) &= \theta_{F(p)}\Big(F_{\ast p}\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_k \theta_k(F(p))\, dy^k\big|_{F(p)}\Big(F_{\ast p}\frac{\partial}{\partial x^i}\Big|_p\Big) \\
> &= \sum_k \theta_k(F(p))\, \sum_j \frac{\partial F^j}{\partial x^i}(p)\, dy^k\big|_{F(p)}\Big(\frac{\partial}{\partial y^j}\Big|_{F(p)}\Big) = \sum_k \theta_k(F(p))\, \sum_j \frac{\partial F^j}{\partial x^i}(p)\, \delta^k_j \\
> &= \sum_j \theta_j(F(p))\, \frac{\partial F^j}{\partial x^i}(p) = c_i(p) .
> \end{aligned}
> $$
>
> The two covectors agree on every basis vector, so they are equal; as $p \in U$ was arbitrary, the identity holds on $U$.
>
> *Smoothness.* Let $\theta$ be smooth. By Proposition [[§53 One-Forms#^prop-53-1|§53.1]] the $\theta_j$ are smooth on $V$, so $\theta_j \circ F$ is smooth on $U$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], with $F|_U : U \to V$). By Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], $F^j \circ \varphi^{-1} = \tilde F^j$, a component of the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$, which is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]); so $F^j$ is smooth on $U$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]), and Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], applied to $F^j \in C^\infty(U)$, gives $\partial F^j/\partial x^i \in C^\infty(U)$, with $(\partial F^j/\partial x^i) \circ \varphi^{-1} = \partial \tilde F^j/\partial r^i$ on $\varphi(U)$. Sums and products of smooth functions are smooth, so each $c_i$ is smooth on $U$, and $F^{\ast}\theta$ is smooth on $U$ by Proposition [[§53 One-Forms#^prop-53-1|§53.1]](3). Every $p \in M$ lies in such a $U$: Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], applied to $F$ at $p$, gives smooth charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$. So $F^{\ast}\theta$ is smooth on $M$.

^pf-53-5

*Uses:* [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§53 One-Forms#^prop-53-1|§53.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§53 One-Forms#^def-53-4|Def. §53.4]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-1|§29.1]], [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]]

> [!remark]- Connections
> - The substitution $dx_i = \sum_j (\partial x_i/\partial u_j)\, du_j$ of 452: [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]; the matrix of a dual map is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
