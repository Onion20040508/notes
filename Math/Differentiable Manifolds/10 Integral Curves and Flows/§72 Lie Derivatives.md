---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 72
tags: [differentiable-manifolds, math591]
---
← [[§71 The Exponential Map]] · ↑ [[· 10 Integral Curves and Flows]]

*Stage: dynamics — Differentiating along a flow: on functions the Lie derivative is the field itself, on vector fields it is the bracket; commuting fields are those invariant under each other's flows.*

*(Lecture 27.)* The Lie derivative is a general construction; it returns with differential forms, the next chapter.

*Motivation.* Go back to the definition of $\partial/\partial x^1$ on functions $f : \mathbb{R}^m \to \mathbb{R}$ (or on an open subset; the definition is local). If $p = (a^1, \ldots, a^m)$,

$$
\frac{\partial f}{\partial x^1}(p) = \lim_{t \to 0} \frac{1}{t}\Big( f(a^1 + t, a^2, \ldots, a^m) - f(a^1, \ldots, a^m) \Big) ,
$$

*Observation:* the integral curve of $\mathbf{X} = \partial/\partial x^1$ starting at $p$ is $\varphi_t(a) = (a^1 + t, a^2, \ldots, a^m)$, exactly what sits inside the first $f$. So, with the pullback $(\varphi_t^{\ast}f)(p) = f(\varphi_t(p))$ (Definition [[§53 One-Forms#^def-53-3|§53.3]]),

$$
\frac{\partial f}{\partial x^1}(p) = \lim_{t \to 0} \frac{1}{t}\Big( (\varphi_t^{\ast}f)(p) - f(p) \Big) ,
$$

and the right-hand side now makes sense on a manifold.

> [!definition] Definition §72.1: Lie Derivative of a Function
> Let $\mathbf{X} \in \mathfrak{X}(M)$, with flow $\varphi$, and $p \in M$. For $f \in C^\infty(M)$, the **Lie derivative** of $f$ with respect to $\mathbf{X}$ at $p$ is
>
> $$
> (\mathcal{L}_{\mathbf{X}} f)(p) = \lim_{t \to 0} \frac{1}{t}\Big( (\varphi_t^{\ast}f)(p) - f(p) \Big) .
> $$
>
> The field differentiated along is the subscript. Only small $t$ enter, and $\varphi_t(p)$ is defined for $|t|$ small (Lemma [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]]), so $\mathbf{X}$ need not be complete.
>
> *Lee: Ch. 9, Lie Derivatives*

^def-72-1

> [!theorem] Proposition §72.1: On Functions $\mathcal{L}_{\mathbf{X}}$ Is $\mathbf{X}$
> For $\mathbf{X} \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, $\mathcal{L}_{\mathbf{X}} f = \mathbf{X}f$. So $\mathcal{L}_{\mathbf{X}}$, as an operator on $C^\infty(M)$, is $\mathbf{X}$ itself.
>
> *Lee: Ch. 9, Lie Derivatives*

^prop-72-1

> [!proof]+ Proof
> *(Lecture 27.)* The limit is the derivative at $t = 0$ of the real function $t \mapsto f(\varphi_t(p))$:
>
> $$
> (\mathcal{L}_{\mathbf{X}} f)(p) = \frac{d}{dt}\Big|_{t=0} f\big(\varphi_t(p)\big) = (\mathbf{X}f)(p),
> $$
>
> because $t \mapsto \varphi_t(p)$ is an integral curve of $\mathbf{X}$ starting at $p$, so its velocity at $0$, which acts on $f$ by this derivative (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]), is $\mathbf{X}_p$.

^pf-72-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]]

> [!remark] Remark: The Flow and the Operator
> Proposition [[§72 Lie Derivatives#^prop-72-1|§72.1]] gives no new operator, but it connects the two descriptions of a vector field: the dynamical one, by its flow, and the algebraic one, as a derivation of $C^\infty(M)$. The Lie derivative of other objects is defined by the same formula.

^rem-72-1

> [!remark] Remark: Lie Derivatives of Other Objects
> In the definition, $f$ can be replaced by any object that can be pulled back by $\varphi_t$ (a tensor field; tensors are not yet defined in these notes). In this course these are differential forms, which pull back naturally (for one-forms, Definition [[§53 One-Forms#^def-53-4|§53.4]]), and vector fields. A vector field cannot be pulled back by a general map, but each $\varphi_t$ is a diffeomorphism onto its image, so $d\varphi_t$ is invertible and its inverse carries the field back; this is Definition [[§72 Lie Derivatives#^def-72-2|§72.2]] below.

^rem-72-2

> [!remark] Remark: Where $\varphi_t$ Is Defined
> If $\mathbf{X}$ is incomplete, $\varphi_t$ is not defined on all of $M$. By the existence of flow boxes (Lemma [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]]), every $p$ has a neighbourhood $U$ and $\varepsilon > 0$ such that $\varphi_t$ is defined on $U$ for $|t| < \varepsilon$; $\varphi_t(U)$ need not lie in $U$, and $\varphi_{-t} : \varphi_t(U) \to U$ brings it back, by the group law (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]]); moreover $\varphi_{-t}$ is defined and smooth on an open set containing $\varphi_t(U)$ (Lemma [[§72 Lie Derivatives#^lem-72-2|§72.2]] below). An open domain is needed: the definition below takes the differential of $\varphi_{-t}$, which requires the map on a neighbourhood, not only along one trajectory.

^rem-72-3

> [!theorem] Lemma §72.2: The Inverse Flow Map $\varphi_{-t}$ Has an Open Domain
> Let $\mathbf{X} \in \mathfrak{X}(M)$ with flow $\varphi : \mathcal{D} \to M$ (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]]), and let $(-\varepsilon, \varepsilon) \times U$ be a flow box (Definition [[§69 Maximal Integral Curves and Flows#^def-69-2|§69.2]]). For $|t| < \varepsilon$:
>
> 1. $M_{-t} = \{ q \in M : (-t, q) \in \mathcal{D} \}$ is open in $M$, and $\varphi_{-t} : M_{-t} \to M$ is smooth;
> 2. $\varphi_t(U) \subseteq M_{-t}$, and $\varphi_{-t}(\varphi_t(q)) = q$ for every $q \in U$.

^lem-72-2

> [!proof]+ Proof
> *(Filled in.)* *(1)* The map $j : M \to \mathbb{R} \times M$, $j(q) = (-t, q)$, is smooth, its components being a constant and the identity (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]]); in particular it is continuous. $\mathcal{D}$ is open (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)), so $M_{-t} = j^{-1}(\mathcal{D})$ is open. On $M_{-t}$, $\varphi_{-t} = \varphi \circ j$, a composite of smooth maps, $\varphi$ being smooth on $\mathcal{D}$ (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)).
>
> *(2)* Let $q \in U$. Since $(t, q) \in (-\varepsilon, \varepsilon) \times U \subseteq \mathcal{D}$, $t \in (\alpha(q), \beta(q))$. Put $q' = \varphi_t(q)$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]](1) with $s = t$, $(\alpha(q'), \beta(q')) = (\alpha(q) - t, \beta(q) - t)$, which contains $-t$ because $0 \in (\alpha(q), \beta(q))$. So $(-t, q') \in \mathcal{D}$, that is, $q' \in M_{-t}$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]](2) with $s = t$ and time $-t$, allowed since $-t + t = 0 \in (\alpha(q), \beta(q))$, $\varphi_{-t}(\varphi_t(q)) = \varphi_0(q) = q$, the maximal integral curve starting at $q$ being at $q$ at time $0$.

^pf-72-2

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]]

![[m591-72-1.svg]]

> [!theorem] Lemma §72.3: $\varphi_t$ Is a Diffeomorphism from $M_t$ onto $M_{-t}$
> Let $\mathbf{X} \in \mathfrak{X}(M)$ with flow $\varphi : \mathcal{D} \to M$ (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]]). For $t \in \mathbb{R}$ let $M_t = \{ p \in M : (t, p) \in \mathcal{D} \}$. Then $M_t$ is open, and $\varphi_t$ maps $M_t$ diffeomorphically onto $M_{-t}$, with inverse $\varphi_{-t}$.
>
> *Lee: Theorem 9.12(c)*

^lem-72-3

> [!proof]+ Proof
> *(Not from lecture; Lee's argument, used below for every time $t$, where Lemma [[§72 Lie Derivatives#^lem-72-2|§72.2]] covers small $|t|$.)* *Open and smooth.* The map $j_t : M \to \mathbb{R} \times M$, $j_t(p) = (t, p)$, is continuous, and $M_t = j_t^{-1}(\mathcal{D})$ is open because $\mathcal{D}$ is (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)); $\varphi_t = \varphi \circ j_t$ is smooth on $M_t$.
>
> *$\varphi_t(M_t) \subseteq M_{-t}$.* Let $p \in M_t$, i.e. $t \in (\alpha(p), \beta(p))$, and $q = \varphi_t(p)$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]](1), $(\alpha(q), \beta(q)) = (\alpha(p) - t, \beta(p) - t)$, which contains $-t$ because $0 \in (\alpha(p), \beta(p))$. So $q \in M_{-t}$.
>
> *Inverse.* For $p \in M_t$, Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]](2) with $s = t$ and time $-t$ (allowed, since $-t + t = 0 \in (\alpha(p), \beta(p))$) gives $\varphi_{-t}(\varphi_t(p)) = \varphi_0(p) = p$. The same argument with $-t$ in place of $t$ shows that $\varphi_{-t}$ maps $M_{-t}$ into $M_t$ and $\varphi_t(\varphi_{-t}(q)) = q$ for $q \in M_{-t}$. So $\varphi_t : M_t \to M_{-t}$ and $\varphi_{-t} : M_{-t} \to M_t$ are smooth and inverse to each other.

^pf-72-3

*Uses:* [[§72 Lie Derivatives#^lem-72-2|§72.2]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]]

> [!definition] Definition §72.2: Lie Derivative of a Vector Field
> Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, let $\varphi$ be the flow of $\mathbf{X}$, and $p \in M$. The **Lie derivative** of $\mathbf{Y}$ with respect to $\mathbf{X}$ at $p$ is
>
> $$
> (\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p = \lim_{t \to 0} \frac{1}{t}\Big( d(\varphi_{-t})_{\varphi_t(p)}\big(\mathbf{Y}_{\varphi_t(p)}\big) - \mathbf{Y}_p \Big) \in T_pM .
> $$
>
> *Lee: Ch. 9, Lie Derivatives*

^def-72-2

The two fields play different roles: $\mathbf{Y}$ is differentiated, along the flow of $\mathbf{X}$. Along the integral curve $t \mapsto \varphi_t(p)$, take the value of $\mathbf{Y}$ at $\varphi_t(p)$ and carry it back to $T_pM$ by $d(\varphi_{-t})_{\varphi_t(p)} : T_{\varphi_t(p)}M \to T_pM$; this uses $\varphi_{-t}$ near $\varphi_t(p)$, which it sends back to $p$ by the group law.

![[m591-72-2.svg]]

*(Figure after the board.)* The value of $\mathbf{Y}$ along the trajectory, carried back to $T_pM$ by the flow.

![[m591-72-a2.gif|620]]

*(Not from lecture; animation added, vault only.)* The definition in motion, for an explicit flow on $\mathbb{R}^2$: $\mathbf{X} = \partial_x + f(x)\,\partial_y$ with $f = F'$, $F(x) = \tfrac12 \sin(0.9x)$, whose flow $\varphi_t(x, y) = (x + t,\ y + F(x + t) - F(x))$ moves along the grey curves, and $\mathbf{Y} = (0.6 + 0.25y)\,\partial_x + (0.25 + 0.35x)\,\partial_y$. As $t$ runs down to $0$, the value $\mathbf{Y}_{\varphi_t(p)}$ (orange, right) is carried back by $d(\varphi_{-t})$ (here the shear $\begin{psmallmatrix} 1 & 0 \\ f(x_p) - f(x_p + t) & 1 \end{psmallmatrix}$) to $V_t \in T_pM$ (blue). Both $\mathbf{Y}_{\varphi_t(p)}$ and $V_t$ approach $\mathbf{Y}_p$, by continuity; what the Lie derivative measures is the rate. The gap $V_t - \mathbf{Y}_p$ (green, drawn at the tip of $\mathbf{Y}_p$ and again on the right) shrinks to $0$ like $t\,[\mathbf{X}, \mathbf{Y}]_p$, while the difference quotient $\frac1t(V_t - \mathbf{Y}_p)$ (red) does not shrink: it settles on $[\mathbf{X}, \mathbf{Y}]_p = \big(\tfrac14 f(x_p),\ 0.35 - \mathbf{Y}^1(p) f'(x_p)\big)$ (grey), computed from the bracket in coordinates, as Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]] predicts.

*Observation.* The limit is the limit of a curve of vectors

$$
V_t = d(\varphi_{-t})_{\varphi_t(p)}\big(\mathbf{Y}_{\varphi_t(p)}\big) \in T_pM
$$

in the fixed vector space $T_pM$, so it is taken in any linear coordinates on $T_pM$: $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p = \dot V_0$. Note that $V_t \to V_0 = \mathbf{Y}_p$ as $t \to 0$, by continuity, just as $\mathbf{Y}_{\varphi_t(p)} \to \mathbf{Y}_p$; the Lie derivative is not where $V_t$ goes but how fast it gets there: $V_t - \mathbf{Y}_p = t\,(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p + o(t)$. Letting $p$ vary, this defines $\mathcal{L}_{\mathbf{X}}\mathbf{Y}$, a vector field on $M$. (For differential forms no such construction is needed, since forms pull back.)

That the limit exists is not obvious; it is the content of the next lemma.

> [!theorem] Lemma §72.4: The Lie Derivative Exists and Is Smooth
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, the limit in Definition [[§72 Lie Derivatives#^def-72-2|§72.2]] exists at every $p \in M$, and $\mathcal{L}_{\mathbf{X}}\mathbf{Y}$ is a smooth vector field.
>
> *Lee: Lemma 9.36*

^lem-72-4

> [!proof]+ Proof
> *(Stated without proof in Lecture 27; Lee's proof, filled in.)* Fix $p \in M$ and a chart $(U, (x^i))$ at $p$. Since $\mathcal{D}$ is open, $(0, p) \in \mathcal{D}$ and $\varphi$ is continuous with $\varphi(0, p) = p$, there are $\delta > 0$ and open sets $U_1 \subseteq U_0 \subseteq U$ containing $p$ with $(-\delta, \delta) \times U_0 \subseteq \mathcal{D}$, $\varphi\big((-\delta, \delta) \times U_0\big) \subseteq U$ and $\varphi\big((-\delta, \delta) \times U_1\big) \subseteq U_0$. Write $\varphi^i(t, x)$ for the components of $\varphi$ on $(-\delta, \delta) \times U_0$ in the chart.
>
> Let $|t| < \delta$ and $x \in U_1$. Then $\varphi_t(x) \in U_0$, and on the open set $U_0$ the map $\varphi_{-t} = \varphi(-t, \cdot\,)$ is defined with values in $U$; the Jacobian of its coordinate representation at $\varphi_t(x)$ is the matrix $\big(\frac{\partial \varphi^i}{\partial x^j}(-t, \varphi(t, x))\big)$. Hence, by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] (the matrix of a differential in coordinates is the Jacobian of the coordinate representation),
>
> $$
> V_t(x) := d(\varphi_{-t})_{\varphi_t(x)}\big(\mathbf{Y}_{\varphi_t(x)}\big) = \sum_{i,j} \frac{\partial \varphi^i}{\partial x^j}\big(-t, \varphi(t, x)\big)\, Y^j\big(\varphi(t, x)\big)\, \frac{\partial}{\partial x^i}\Big|_x ,
> $$
>
> where $Y^j$ are the components of $\mathbf{Y}$. The coefficient of $\partial/\partial x^i|_x$ is a smooth function of $(t, x) \in (-\delta, \delta) \times U_1$, a composite of smooth functions. Therefore $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_x$, the $t$-derivative at $t = 0$ of this expression (Definition [[§72 Lie Derivatives#^def-72-2|§72.2]]), exists for each $x \in U_1$, and its coefficients $\frac{\partial}{\partial t}\big|_{t=0}$ of smooth functions of $(t, x)$ are smooth in $x$. As $p$ was arbitrary, $\mathcal{L}_{\mathbf{X}}\mathbf{Y}$ is defined everywhere and is a smooth vector field. The same formula shows that $t \mapsto V_t(x)$ is a smooth curve in $T_xM$ for $|t| < \delta$.

^pf-72-4

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§72 Lie Derivatives#^def-72-2|Def. §72.2]]

> [!example] Example §72.1: The Lie Derivative along $\partial/\partial x^1$
> On $\mathbb{R}^m$ let $\mathbf{X} = \partial/\partial x^1$ and $\mathbf{Y} = \sum_i g^i\, \partial/\partial x^i$. The flow is translation in the first variable,
>
> $$
> \varphi_t(x^1, \ldots, x^m) = (x^1 + t, x^2, \ldots, x^m), \qquad \text{i.e. } \varphi_t(x) = x + te_1, \quad e_1 = (1, 0, \ldots, 0) .
> $$
>
> Its differential is the identity everywhere, in the coordinate bases: $d(\varphi_{-t})_{x}(\partial/\partial x^i|_x) = \partial/\partial x^i|_{x - te_1}$. So
>
> $$
> (\mathcal{L}_{\partial/\partial x^1}\mathbf{Y})_p = \lim_{t \to 0} \frac{1}{t}\big( \mathbf{Y}_{p + te_1} - \mathbf{Y}_p \big) = \lim_{t \to 0} \frac{1}{t} \sum_{i=1}^m \big( g^i(p + te_1) - g^i(p) \big) \frac{\partial}{\partial x^i}\Big|_p = \sum_{i=1}^m \frac{\partial g^i}{\partial x^1}(p)\, \frac{\partial}{\partial x^i}\Big|_p .
> $$
>
> The flow is written down at every point $x$, not only along the trajectory of $p$, because the definition takes the differential of the time-$t$ map. Here the Lie derivative is componentwise differentiation of $\mathbf{Y}$ in the direction $x^1$; this case is the core of the proof of Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]].

^ex-72-1

The Lie derivative of a vector field turns out to be a known operation, the bracket. The proof uses a normal form for a vector field near a point where it does not vanish; its proof, by the flow, is postponed.

> [!theorem] Lemma §72.5: Canonical Form Near a Regular Point
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$ with $\mathbf{X}_p \neq 0$. There is a coordinate chart $(U, \varphi = (x^1, \ldots, x^m))$ with $p \in U$ such that
>
> $$
> \mathbf{X}|_U = \frac{\partial}{\partial x^1} .
> $$
>
> *Lee: Theorem 9.22*

^lem-72-5

> [!proof]+ Proof (to be filled)
> Postponed in Lecture 27.

^pf-72-5

![[m591-72-3.svg]]

A field that is nonzero at $p$ is nonzero on a neighbourhood of $p$, by continuity, and in suitable coordinates there it is the constant field $\partial_1$: its integral curves are straightened into parallel lines.

> [!theorem] Theorem §72.6: The Lie Derivative Is the Bracket
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$,
>
> $$
> \mathcal{L}_{\mathbf{X}}\mathbf{Y} = [\mathbf{X}, \mathbf{Y}] .
> $$
>
> *Lee: Theorem 9.38*

^thm-72-6

> [!proof]+ Proof
> *(Lecture 27, modulo Lemmas [[§72 Lie Derivatives#^lem-72-4|§72.4]] and [[§72 Lie Derivatives#^lem-72-5|§72.5]]. The locality in Case 2 and the continuity argument in Case 3 are filled in.)* Take $p \in M$.
>
> *Case 1: $\mathbf{X}$ is zero in a neighbourhood $W$ of $p$.* Then $\varphi_t(q) = q$ for all $q \in W$, since the constant curve is an integral curve there: since $\mathbf{X} = 0$ there So $\varphi_{-t}$ is the identity on the open set $W$, $d(\varphi_{-t})_p = \mathrm{id}$, $V_t = \mathbf{Y}_p$, and $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p = 0 \in T_pM$. Also $[\mathbf{X}, \mathbf{Y}]_p f = \mathbf{X}_p(\mathbf{Y}f) - \mathbf{Y}_p(\mathbf{X}f) = 0$, as $\mathbf{X}_p = 0$ and $\mathbf{X}f$ vanishes on $W$, so its germ at $p$ is $0$.
>
> *Case 2: $\mathbf{X}_p \neq 0$.* Take the chart $(U, x^1, \ldots, x^m)$ of Lemma [[§72 Lie Derivatives#^lem-72-5|§72.5]], with $\mathbf{X}|_U = \partial/\partial x^1$, and write $\mathbf{Y} = \sum_i g^i\, \partial/\partial x^i$ on $U$. *(Filled in.)* The Lie derivative at $p$ only involves $\varphi_t$ near $p$ and $\varphi_{-t}$ near $\varphi_t(p)$, for small $t$. Choose a neighbourhood $U' \subseteq U$ of $p$ and $\varepsilon > 0$ with $\varphi_t(U') \subseteq U$ for $|t| < \varepsilon$. For $q \in U'$, the curve $t \mapsto \varphi_t(q)$, $|t| < \varepsilon$, is an integral curve of $\partial/\partial x^1$ inside $U$, so in coordinates it is $x(q) + te_1$ (Lemma [[§67 Integral Curves#^lem-67-5|§67.5]] and uniqueness). So in the chart the flow is the translation of Example [[§72 Lie Derivatives#^ex-72-1|§72.1]], and the problem reduces to that Euclidean computation:
>
> $$
> \mathcal{L}_{\partial/\partial x^1}\mathbf{Y} = \sum_i \frac{\partial g^i}{\partial x^1}\, \frac{\partial}{\partial x^i} \qquad \text{at } p ,
> $$
>
> the left-hand side of the identity. The right-hand side, by Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]:
>
> $$
> \Big[ \frac{\partial}{\partial x^1}, \sum_i g^i \frac{\partial}{\partial x^i} \Big] = \sum_i \frac{\partial g^i}{\partial x^1}\, \frac{\partial}{\partial x^i} ,
> $$
>
> since the other term, $\mathbf{Y}$ applied to the coefficients of $\partial/\partial x^1$, vanishes: they are constant. The two sides agree.
>
> *Case 3: $\mathbf{X}_p = 0$, but $\mathbf{X}$ is not zero on any neighbourhood of $p$.* Cases 1 and 2 do not cover every point: $p$ may lie on the boundary of the support of $\mathbf{X}$. This case follows by continuity, given that the Lie derivative is smooth. *(Filled in.)* Every neighbourhood of $p$ contains points $q$ with $\mathbf{X}_q \neq 0$, so $p$ is a limit of such points. At those points the two sides agree by Case 2, and both $\mathcal{L}_{\mathbf{X}}\mathbf{Y}$ (Lemma [[§72 Lie Derivatives#^lem-72-4|§72.4]]) and $[\mathbf{X}, \mathbf{Y}]$ (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]) are continuous. In a chart around $p$ their components are continuous functions agreeing at the points $q$, hence at $p$.

^pf-72-6

*Uses:* [[§72 Lie Derivatives#^lem-72-4|§72.4]], [[§72 Lie Derivatives#^lem-72-5|§72.5]], [[§67 Integral Curves#^lem-67-5|§67.5]], [[§72 Lie Derivatives#^ex-72-1|Ex. §72.1]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]

> [!remark] Remark: The Bracket Has a Dynamical Meaning
> The bracket was defined algebraically, as the commutator of two derivations (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]). Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]] reaches it from the flow: $[\mathbf{X}, \mathbf{Y}]_p$ is the rate at which $\mathbf{Y}$, carried back along the flow of $\mathbf{X}$, changes at $p$. This has dynamical consequences, the first being Theorem [[§72 Lie Derivatives#^thm-72-9|§72.9]] below.

^rem-72-4

![[m591-72-4.svg]]

*(Not from lecture; figure added.)* A check of Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]] on $\mathbb{R}^2$ with the rotation field $\mathbf{X} = -y\,\partial/\partial x + x\,\partial/\partial y$, whose flow $\varphi_t$ is rotation by the angle $t$ (Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]]), and the constant field $\mathbf{Y} = \partial/\partial x$ (blue). Since $\varphi_{-t}$ is the linear rotation by $-t$, $d(\varphi_{-t})$ is that rotation too, so the value $\mathbf{Y}_{\varphi_t(p)} = (1, 0)$ carried back to $p$ is $V_t = (\cos t, -\sin t)$ (orange): the carried-back vectors turn clockwise. Their derivative at $t = 0$ is $(0, -1)$, so $\mathcal{L}_{\mathbf{X}}\mathbf{Y} = -\partial/\partial y$ (red). By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], $[\mathbf{X}, \mathbf{Y}] = \big(\mathbf{X}(1) - \mathbf{Y}(-y)\big)\partial/\partial x + \big(\mathbf{X}(0) - \mathbf{Y}(x)\big)\partial/\partial y = -\partial/\partial y$ as well. Here $\mathbf{X}_0 = 0$ while $\mathbf{X}$ vanishes on no neighbourhood of $0$: the origin is a point of Case 3 of the proof.

![[m591-72-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* The same computation in motion, with $t$ running down from $1.4$ towards $0$. Left: the point $\varphi_t(p)$ on its circle, the value $\mathbf{Y}_{\varphi_t(p)} = \partial/\partial x$ there (blue), and that value carried back to $p$ by $d(\varphi_{-t})$ (orange, $V_t$). Right, in the fixed vector space $T_pM$: the difference quotient $\frac1t(V_t - \mathbf{Y}_p)$ (red) settling on $(0, -1)$, the Lie derivative $\mathcal{L}_{\mathbf{X}}\mathbf{Y} = -\partial/\partial y = [\mathbf{X}, \mathbf{Y}]$ (grey).

> [!theorem] Corollary §72.7: Properties of the Lie Derivative
> For $\mathbf{X}, \mathbf{Y}, \mathbf{Z} \in \mathfrak{X}(M)$:
>
> 1. $\mathcal{L}_{\mathbf{X}}\mathbf{Y} = -\mathcal{L}_{\mathbf{Y}}\mathbf{X}$;
> 2. $\mathcal{L}_{\mathbf{X}}[\mathbf{Y}, \mathbf{Z}] = [\mathcal{L}_{\mathbf{X}}\mathbf{Y}, \mathbf{Z}] + [\mathbf{Y}, \mathcal{L}_{\mathbf{X}}\mathbf{Z}]$.
>
> *Lee: Corollary 9.39*

^cor-72-7

> [!proof]+ Proof (to be filled after the homework)
> From Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]]. For (2), the left-hand side is $[\mathbf{X}, [\mathbf{Y}, \mathbf{Z}]{]}$, and the tool is the Jacobi identity (Corollary [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]]). One of these entries is a problem on the next homework.

^pf-72-7

*Uses:* [[§72 Lie Derivatives#^thm-72-6|§72.6]], [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]]

**Transcription note (board 11/6 and Lecture 27).** On the board, the definition of $(\mathcal{L}_{\mathbf{X}} f)(p)$ repeats the left-hand side of the motivating formula, “$\frac{\partial f}{\partial x^1}(p) = \lim_{t \to 0} \ldots$”; the definition is the limit, as above. The board's single definition box of commuting fields and invariance is split here into Definitions [[§72 Lie Derivatives#^def-72-3|§72.3]] and [[§72 Lie Derivatives#^def-72-4|§72.4]]. Uribe cited this as Lee's Corollary 3.9, then 9.3, with a question mark; it is Lee's Corollary 9.39 (Lee's list also has $\mathcal{L}_{[\mathbf{X}, \mathbf{Y}]} = \mathcal{L}_{\mathbf{X}}\mathcal{L}_{\mathbf{Y}} - \mathcal{L}_{\mathbf{Y}}\mathcal{L}_{\mathbf{X}}$ and a product rule).

The derivative of the curve $V_t$ at $t = 0$ is $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p$ by definition. The next proposition computes it at every time; it is the key step in Theorem [[§72 Lie Derivatives#^thm-72-9|§72.9]].

> [!theorem] Proposition §72.8: The Derivative of the Pulled-Back Field at Any Time
> Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, let $\varphi$ be the flow of $\mathbf{X}$, and $p \in M$. For $t \in (\alpha(p), \beta(p))$ put
>
> $$
> V_t = d(\varphi_{-t})_{\varphi_t(p)}\big(\mathbf{Y}_{\varphi_t(p)}\big) \in T_pM .
> $$
>
> Then $t \mapsto V_t$ is a smooth curve in $T_pM$, and for every $t_0 \in (\alpha(p), \beta(p))$
>
> $$
> \frac{d}{dt}\Big|_{t = t_0} V_t = d(\varphi_{-t_0})_{\varphi_{t_0}(p)}\Big( (\mathcal{L}_{\mathbf{X}}\mathbf{Y})_{\varphi_{t_0}(p)} \Big) .
> $$
>
> *Lee: Proposition 9.41*

^prop-72-8

> [!proof]+ Proof
> *(Reading assigned by email after Lecture 27: Lee, Proposition 9.41 and Theorems 9.42 and 9.44; not presented in lecture. Lee's proof.)* $V_t$ is defined: $\varphi_t(p) \in M_{-t}$, where $\varphi_{-t}$ is defined and smooth (Lemma [[§72 Lie Derivatives#^lem-72-3|§72.3]]). Fix $t_0$ and put $q = \varphi_{t_0}(p)$. For small $|s|$, write $W_s = d(\varphi_{-s})_{\varphi_s(q)}\big(\mathbf{Y}_{\varphi_s(q)}\big) \in T_qM$, the curve of Definition [[§72 Lie Derivatives#^def-72-2|§72.2]] at the point $q$.
>
> *Step 1: $V_{t_0 + s} = d(\varphi_{-t_0})_q (W_s)$ for small $|s|$.* By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]](2), $\varphi_{t_0 + s}(p) = \varphi_s(q)$, for $|s|$ small enough that $t_0 + s \in (\alpha(p), \beta(p))$ and $s \in (\alpha(q), \beta(q))$. Near $\varphi_s(q)$ the two maps $\varphi_{-t_0 - s}$ and $\varphi_{-t_0} \circ \varphi_{-s}$ agree: both are defined on the open set of points $x$ with $\varphi_{-s}(x) \in M_{-t_0}$, which contains $\varphi_s(q)$ (since $\varphi_{-s}(\varphi_s(q)) = q \in M_{-t_0}$, Lemma [[§72 Lie Derivatives#^lem-72-3|§72.3]]), and there $\varphi_{-t_0}(\varphi_{-s}(x)) = \varphi_{-t_0 - s}(x)$ by the group law. By the chain rule, and because $\varphi_{-s}(\varphi_s(q)) = q$,
>
> $$
> d(\varphi_{-t_0 - s})_{\varphi_s(q)} = d(\varphi_{-t_0})_q \circ d(\varphi_{-s})_{\varphi_s(q)} .
> $$
>
> Applying this to $\mathbf{Y}_{\varphi_s(q)} = \mathbf{Y}_{\varphi_{t_0 + s}(p)}$ gives $V_{t_0 + s} = d(\varphi_{-t_0})_q(W_s)$.
>
> *Step 2: differentiate.* By the proof of Lemma [[§72 Lie Derivatives#^lem-72-4|§72.4]] at the point $q$, $s \mapsto W_s$ is a smooth curve in $T_qM$ near $s = 0$, with derivative $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_q$ at $s = 0$. The map $d(\varphi_{-t_0})_q : T_qM \to T_pM$ is linear and does not depend on $s$, so $s \mapsto V_{t_0 + s}$ is smooth near $0$ and
>
> $$
> \frac{d}{ds}\Big|_{s = 0} V_{t_0 + s} = d(\varphi_{-t_0})_q\Big( \frac{d}{ds}\Big|_{s = 0} W_s \Big) = d(\varphi_{-t_0})_q\big( (\mathcal{L}_{\mathbf{X}}\mathbf{Y})_q \big) .
> $$
>
> As $t_0$ was arbitrary, $V_t$ is smooth on $(\alpha(p), \beta(p))$, with the stated derivative.

^pf-72-8

*Uses:* [[§72 Lie Derivatives#^lem-72-3|§72.3]], [[§72 Lie Derivatives#^def-72-2|Def. §72.2]], [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]], [[§72 Lie Derivatives#^lem-72-4|§72.4]]

![[m591-72-6.svg]]

*(Not from lecture; figure added, after Lee's Fig. 9.14.)* The proof of Proposition [[§72 Lie Derivatives#^prop-72-8|§72.8]]. To differentiate $V_t$ at $t_0$, move the base point to $q = \varphi_{t_0}(p)$: near $t_0$, $V_t$ is the curve $W_s$ of the Lie derivative at $q$, carried back to $T_pM$ by the one fixed linear map $d(\varphi_{-t_0})_q$. So the velocity of $V_t$ at $t_0$ is the Lie derivative at $q$, carried back.

*Commuting vector fields.* The main application of Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]] is to the case $[\mathbf{X}, \mathbf{Y}] = 0$.

> [!definition] Definition §72.3: Commuting Vector Fields
> Vector fields $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ **commute** if $[\mathbf{X}, \mathbf{Y}] = 0$.
>
> *Lee: Ch. 9, Commuting Vector Fields*

^def-72-3

> [!definition] Definition §72.4: Invariance under a Flow
> Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, and let $\varphi$ be the flow of $\mathbf{X}$. Then $\mathbf{Y}$ is **invariant under the flow** $\varphi$ of $\mathbf{X}$ if for every $t$, $\mathbf{Y}$ is $\varphi_t$-related to itself (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]): $d(\varphi_t)_p(\mathbf{Y}_p) = \mathbf{Y}_{\varphi_t(p)}$ for all $(t, p)$ in the flow domain $\mathcal{D}$. For incomplete $\mathbf{X}$ the condition is read where $\varphi_t$ is defined, on the open sets of Lemma [[§72 Lie Derivatives#^lem-72-2|§72.2]] above. A complete field is invariant under its own flow (Lemma [[§70 Complete Vector Fields#^lem-70-4|§70.4]]; Lee, Corollary 9.43, without completeness).
>
> *Lee: Ch. 9, Commuting Vector Fields*

^def-72-4

> [!theorem] Theorem §72.9: Commuting Fields: Invariance and Commuting Flows
> Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, with flows $\varphi$ and $\psi$. The following are equivalent:
>
> 1. $[\mathbf{X}, \mathbf{Y}] = 0$;
> 2. $\mathbf{Y}$ is invariant under the flow of $\mathbf{X}$;
> 3. the flows commute: $\varphi_s \circ \psi_t = \psi_t \circ \varphi_s$. Precisely: for all intervals $I, J \subseteq \mathbb{R}$ containing $0$ and every $p \in M$, if $\varphi_s \circ \psi_t(p)$ or $\psi_t \circ \varphi_s(p)$ exists for all $(s, t) \in I \times J$, then the other exists too, and they are equal.
>
> If $\mathbf{X}$ and $\mathbf{Y}$ are complete, (3) just says $\varphi_s \circ \psi_t = \psi_t \circ \varphi_s$ for all $s, t \in \mathbb{R}$. Since $[\mathbf{Y}, \mathbf{X}] = -[\mathbf{X}, \mathbf{Y}]$, (1)–(3) are also equivalent to: $\mathbf{X}$ is invariant under the flow $\psi$ of $\mathbf{Y}$ (Lee, Theorem 9.42(c)).
>
> *Lee: Theorems 9.42 and 9.44*

^thm-72-9

> [!proof]+ Proof
> *(Lecture 27's indication for (1)$\Rightarrow$(2).)* $[\mathbf{X}, \mathbf{Y}] = 0$ means, by Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]], that the derivative at $t = 0$ of the curve $V_t$ of pulled-back values of $\mathbf{Y}$ is zero, at every point; by the group law, the derivative of $V_t$ at any time $t$ is the derivative at time $0$ at the point $\varphi_t(p)$, carried back to $p$ (Proposition [[§72 Lie Derivatives#^prop-72-8|§72.8]]); so it vanishes for every $t$, $V_t$ is constant, and $\mathbf{Y}$ is invariant under the flow.
>
> *(Reading assigned by email after Lecture 27: Lee, Proposition 9.41 and Theorems 9.42 and 9.44; not presented in lecture. Lee's proof.)* Throughout, for $p \in M$ let $V_t = d(\varphi_{-t})_{\varphi_t(p)}\big(\mathbf{Y}_{\varphi_t(p)}\big)$, $t \in (\alpha(p), \beta(p))$, as in Proposition [[§72 Lie Derivatives#^prop-72-8|§72.8]]; $V_0 = \mathbf{Y}_p$. By Lemma [[§72 Lie Derivatives#^lem-72-3|§72.3]], $d(\varphi_{-t})_{\varphi_t(p)}$ and $d(\varphi_t)_p$ are inverse linear isomorphisms, so
>
> $$
> \mathbf{Y} \text{ is invariant at } (t, p), \text{ i.e. } d(\varphi_t)_p(\mathbf{Y}_p) = \mathbf{Y}_{\varphi_t(p)} \iff V_t = \mathbf{Y}_p . \tag{$\dagger$}
> $$
>
> *(1)$\Rightarrow$(2)* (Lee 9.42). Let $[\mathbf{X}, \mathbf{Y}] = 0$. Then $\mathcal{L}_{\mathbf{X}}\mathbf{Y} = 0$ everywhere (Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]]), so by Proposition [[§72 Lie Derivatives#^prop-72-8|§72.8]] the derivative of $V_t$ vanishes at every $t \in (\alpha(p), \beta(p))$. A curve in the vector space $T_pM$ with zero derivative on an interval is constant (apply the mean value theorem to each component in a basis), so $V_t = V_0 = \mathbf{Y}_p$ for all $t$, and by ($\dagger$) $\mathbf{Y}$ is invariant under $\varphi$.
>
> *(2)$\Rightarrow$(1)* (Lee 9.42). If $\mathbf{Y}$ is invariant under $\varphi$, then by ($\dagger$) $V_t = \mathbf{Y}_p$ for all $t$, so $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p = \frac{d}{dt}\big|_{t=0} V_t = 0$ (Definition [[§72 Lie Derivatives#^def-72-2|§72.2]]), and $[\mathbf{X}, \mathbf{Y}]_p = 0$ by Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]]. As $p$ was arbitrary, $[\mathbf{X}, \mathbf{Y}] = 0$.
>
> *The symmetric statement.* $[\mathbf{Y}, \mathbf{X}] = -[\mathbf{X}, \mathbf{Y}]$, so the same two arguments with the roles of $\mathbf{X}$ and $\mathbf{Y}$ exchanged show: $[\mathbf{X}, \mathbf{Y}] = 0$ if and only if $\mathbf{X}$ is invariant under $\psi$.
>
> *(1)$\Rightarrow$(3)* (Lee 9.44). Let $[\mathbf{X}, \mathbf{Y}] = 0$, $p \in M$, and $I, J$ open intervals containing $0$ such that $\psi_t \circ \varphi_s(p)$ is defined for all $(s, t) \in I \times J$. (If instead $\varphi_s \circ \psi_t(p)$ is defined on $I \times J$, exchange the roles of $\mathbf{X}$ and $\mathbf{Y}$.) By the symmetric statement, $\mathbf{X}$ is invariant under $\psi$. Fix $t \in J$ and let $\gamma(s) = \psi_t(\varphi_s(p))$, $s \in I$. Then $\gamma(0) = \psi_t(p)$, and by the chain rule (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]), the fact that $s \mapsto \varphi_s(p)$ is an integral curve of $\mathbf{X}$, and invariance of $\mathbf{X}$ under $\psi$ at the point $\varphi_s(p)$ (where $\psi_t$ is defined),
>
> $$
> \dot\gamma(s) = d(\psi_t)_{\varphi_s(p)}\big(\mathbf{X}_{\varphi_s(p)}\big) = \mathbf{X}_{\psi_t(\varphi_s(p))} = \mathbf{X}_{\gamma(s)} .
> $$
>
> So $\gamma : I \to M$ is an integral curve of $\mathbf{X}$ starting at $\psi_t(p)$. The maximal integral curve $\varphi^{\psi_t(p)}$ extends every integral curve starting at $\psi_t(p)$ (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](1), Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), so its domain contains $I$ and $\varphi_s(\psi_t(p)) = \gamma(s) = \psi_t(\varphi_s(p))$ for all $s \in I$. Hence both compositions are defined on $I \times J$ and agree.
>
> *(3)$\Rightarrow$(1)* (Lee 9.44). Assume the flows commute in the sense of (3), and let $p \in M$. The map $(s, t) \mapsto \psi_t(\varphi_s(p))$ is defined near $(0, 0)$: $\psi$ is defined on an open set $(-\varepsilon_2, \varepsilon_2) \times U$ around $(0, p)$ in its domain, and $\varphi_s(p) \in U$ for $|s| < \varepsilon_1$ by continuity. With $\varepsilon = \min(\varepsilon_1, \varepsilon_2)$ and $I = J = (-\varepsilon, \varepsilon)$, (3) gives $\varphi_s(\psi_t(p)) = \psi_t(\varphi_s(p))$ for $|s|, |t| < \varepsilon$. Fix $|s| < \varepsilon$ and differentiate in $t$ at $t = 0$. On the left, $t \mapsto \psi_t(p)$ has velocity $\mathbf{Y}_p$ at $t = 0$, so the chain rule (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]) gives $d(\varphi_s)_p(\mathbf{Y}_p)$; on the right, $t \mapsto \psi_t(\varphi_s(p))$ is the integral curve of $\mathbf{Y}$ through $\varphi_s(p)$, with velocity $\mathbf{Y}_{\varphi_s(p)}$ at $t = 0$. So $d(\varphi_s)_p(\mathbf{Y}_p) = \mathbf{Y}_{\varphi_s(p)}$, that is, $V_s = \mathbf{Y}_p$ for $|s| < \varepsilon$ by ($\dagger$). Hence $(\mathcal{L}_{\mathbf{X}}\mathbf{Y})_p = \frac{d}{ds}\big|_{s=0} V_s = 0$ and $[\mathbf{X}, \mathbf{Y}]_p = 0$ (Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]]).

^pf-72-9

*Uses:* [[§72 Lie Derivatives#^thm-72-6|§72.6]], [[§72 Lie Derivatives#^prop-72-8|§72.8]], [[§72 Lie Derivatives#^lem-72-3|§72.3]], [[§72 Lie Derivatives#^def-72-2|Def. §72.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]], [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

> [!theorem] Corollary §72.10: Every Vector Field Is Invariant under Its Own Flow
> Let $\mathbf{X} \in \mathfrak{X}(M)$ with flow $\varphi$. Then $d(\varphi_t)_p(\mathbf{X}_p) = \mathbf{X}_{\varphi_t(p)}$ for all $(t, p) \in \mathcal{D}$.
>
> *Lee: Corollary 9.43*

^cor-72-10

> [!proof]+ Proof
> *(Lee's proof; not presented in lecture.)* $[\mathbf{X}, \mathbf{X}] = 0$, so Theorem [[§72 Lie Derivatives#^thm-72-9|§72.9]] (1)$\Rightarrow$(2) with $\mathbf{Y} = \mathbf{X}$ gives the invariance. For complete $\mathbf{X}$ this is Lemma [[§70 Complete Vector Fields#^lem-70-4|§70.4]].

^pf-72-10

*Uses:* [[§72 Lie Derivatives#^thm-72-9|§72.9]], [[§70 Complete Vector Fields#^lem-70-4|§70.4]]

> [!remark] Remark: Commuting Flows of Incomplete Fields
> For incomplete fields, condition (3) is delicate: $\varphi_s \circ \psi_t(p)$ need not be defined for all $s, t$, which is why it is stated with intervals $I$, $J$ on which one of the two compositions exists. A problem on the next homework shows why this care is needed.

^rem-72-5

![[m591-72-5.svg]]

*(Not from lecture; figure added.)* Condition (3) of Theorem [[§72 Lie Derivatives#^thm-72-9|§72.9]] in two examples on $\mathbb{R}^2$, with $s = 1.5$, $t = 1$. Left: the flows of $\partial_x$ and $\partial_y$ are translations, and the two routes around the rectangle end at the same point. Right: $\mathbf{Y} = x\,\partial_y$ has the flow $\psi_t(x, y) = (x, y + tx)$, a shear, so it lifts a point by $t$ times its distance from the axis $x = 0$. Moving out first (blue) gives $\psi_t \circ \varphi_s(p) = (x + s, y + t(x + s))$, moving up first (red) gives $\varphi_s \circ \psi_t(p) = (x + s, y + tx)$: they differ by $st$ in the $y$-direction. By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], $[\partial_x, x\,\partial_y] = \partial_y \neq 0$, and the gap is exactly $st\,[\mathbf{X}, \mathbf{Y}]$ here.

\appendix
