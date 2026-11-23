---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 85
tags: [differentiable-manifolds, math591]
---
← [[§84 Contraction by Vector Fields]] · ↑ [[· 11 Differential Forms]] · [[§86 Cartan's Magic Formula]] →

*Stage: forms — Differentiating a form along the flow of a vector field: the definition, the model computation in straightening coordinates, and four properties; a form with zero Lie derivative is invariant under the flow.*

*(Lecture 34.)* The Lie derivative of functions and of vector fields ([[§72 Lie Derivatives|§72]]) is now defined for differential forms, by the same recipe: pull back along the flow, then differentiate in time. Forms pull back under any smooth map (Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]]), so this is simpler than for vector fields. Throughout, $\mathbf{X} \in \mathfrak{X}(M)$ is fixed, and $\varphi : \mathcal{D} \to M$ is its flow (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]]); for $t \in \mathbb{R}$, $M_t = \{p : (t, p) \in \mathcal{D}\}$ is open and $\varphi_t$ is smooth on it (Lemma [[§72 Lie Derivatives#^lem-72-2|§72.2]]).

> [!remark] Remark: Notation of Lecture 34
> In addition to the remark *Notation of Lecture 33* ([[§83 The First Cohomology of the Circle|§83]]):
> - *Contraction.* The board writes $i_\mathbf{X}$ for the contraction; these notes write $\iota_\mathbf{X}$, as in Definition [[§84 Contraction by Vector Fields#^def-84-1|§84.1]].
> - *Lie derivative.* The board's definition box writes $(\mathcal{L}\alpha)_p$; the field is fixed, and the notes write $(\mathcal{L}_\mathbf{X}\alpha)_p$.
> - *The curve $\alpha_p(t)$.* $\alpha_p(t) = (\varphi_t^{\ast}\alpha)_p$ is a point of $\Lambda^k T_p^{\ast}M$ for each $t$; it is not $\alpha$ evaluated at a moving point. In particular $\alpha_p(0) = \alpha_p$. The board's “$(\varphi_t)^{\ast}(\alpha_{\varphi_t(p)})$” is $(d\varphi_t)_p^{\ast}\big(\alpha_{\varphi_t(p)}\big)$, the pullback of Definition [[§80 Differential Forms on Manifolds#^def-80-9|§80.9]] at the point $p$.
> - *Two letters $d$.* $\frac{d}{dt}$ differentiates curves in a fixed vector space; $d$ alone is the exterior derivative.

^rem-85-1

> [!definition] Definition §85.1: Lie Derivative of a Form
> Let $\alpha \in \Omega^k(M)$ and $p \in M$. For $t$ with $p \in M_t$ (at least for $|t|$ small) define
>
> $$
> \alpha_p(t) = (\varphi_t^{\ast}\alpha)_p = (d\varphi_t)_p^{\ast}\big(\alpha_{\varphi_t(p)}\big) \in \Lambda^k T_p^{\ast}M ,
> $$
>
> a curve in the vector space $\Lambda^k T_p^{\ast}M$; the vector space is the same for every $t$ (the board's “$t$-independent”), and only the point $\alpha_p(t)$ moves. The curve $t \mapsto \alpha_p(t)$ is smooth (Lemma [[§85 Lie Derivatives of Forms#^lem-85-1|§85.1]]). The **Lie derivative** of $\alpha$ with respect to $\mathbf{X}$ is the $k$-form $\mathcal{L}_\mathbf{X}\alpha$ given at each $p$ by
>
> $$
> (\mathcal{L}_\mathbf{X}\alpha)_p = \frac{d}{dt}\Big|_{t=0} \alpha_p(t) = \lim_{t \to 0} \frac{1}{t}\Big( (\varphi_t^{\ast}\alpha)_p - \alpha_p \Big) .
> $$
>
> *Lee: Ch. 12, Lie Derivatives of Tensor Fields (12.8)*

^def-85-1


> [!remark]- Connections
> - The same recipe for functions and for vector fields: [[§72 Lie Derivatives#^def-72-1|Def. §72.1]], [[§72 Lie Derivatives#^def-72-2|Def. §72.2]]; for vector fields the flow has to be run backwards, $\varphi_{-t}$, because vectors push forward, while forms pull back.
> - The pullback of $k$-forms used here: [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]]; the flow and the open sets $M_t$: [[§69 Maximal Integral Curves and Flows|§69]].

The definition makes sense for every $p$, because $(t, p) \in \mathcal{D}$ for $|t|$ small, and the open set $M_t$ containing $p$ is where $\varphi_t$ is defined and smooth; $\mathbf{X}$ need not be complete. The curve lives in one fixed finite-dimensional vector space, so its derivative is taken componentwise in any basis.

![[m591-81-1.svg]]

*(Not from lecture; figure added.)* Definition [[§85 Lie Derivatives of Forms#^def-85-1|§85.1]]. Left, as on the board: the value of $\alpha$ at $\varphi_t(p)$ is carried back to $p$ by the pullback $(d\varphi_t)_p^{\ast}$. Right: for each $t$ this gives a point $\alpha_p(t)$ of the one vector space $\Lambda^k T_p^{\ast}M$, which does not depend on $t$; the curve passes through $\alpha_p$ at $t = 0$, and its velocity there is $(\mathcal{L}_\mathbf{X}\alpha)_p$. For forms no inverse $\varphi_{-t}$ is needed, unlike for vector fields (Definition [[§72 Lie Derivatives#^def-72-2|§72.2]]): forms pull back.


![[m591-81-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* The curve $\alpha_p(t)$ for $\alpha = dx$ on $\mathbb{R}^2$, $p = (1, 0)$ and $\mathbf{X} = -y\,\partial_x + x\,\partial_y$, whose flow $\varphi_t$ is rotation by $t$. Covectors $a\,dx + b\,dy$ are drawn as their coefficient vectors $(a, b)$. Left: as $\varphi_t(p)$ goes around the circle, $dx$ there (blue) is carried back to $p$ by $(d\varphi_t)_p^{\ast}$ (orange): $(\varphi_t^{\ast}dx)_p = d(\cos t\, x - \sin t\, y)_p = \cos t\, dx - \sin t\, dy$. Right: these points form a circle in the one fixed plane $T_p^{\ast}\mathbb{R}^2$, through $dx$ at $t = 0$ with velocity $-dy$ (red). So $\mathcal{L}_\mathbf{X}\, dx = -dy$, as Cartan's formula ([[§86 Cartan's Magic Formula#^thm-86-2|§86.2]]) also gives: $d(\iota_\mathbf{X} dx) + \iota_\mathbf{X}(d\,dx) = d(-y) = -dy$.

> [!theorem] Lemma §85.1: The Lie Derivative of a Form Is a Smooth Form
> For $\alpha \in \Omega^k(M)$ and $p \in M$, the curve $t \mapsto \alpha_p(t)$ is smooth. More precisely, for every chart $(U, (x^i))$ at $p$ there are a neighbourhood $U' \subseteq U$ of $p$ and $\varepsilon > 0$ such that, on $U'$ and for $|t| < \varepsilon$,
>
> $$
> \varphi_t^{\ast}\alpha = \sum_A g_A(t, x)\, dx^A
> $$
>
> with $g_A$ smooth on $(-\varepsilon, \varepsilon) \times U'$. Consequently $\mathcal{L}_\mathbf{X}\alpha = \sum_A \frac{\partial g_A}{\partial t}(0, x)\, dx^A$ on $U'$, and $\mathcal{L}_\mathbf{X}\alpha \in \Omega^k(M)$.
>
> *Lee: Lemma 12.30*

^lem-85-1

> [!proof]+ Proof
> *(Stated in Lecture 34, “$t \mapsto \alpha_p(t)$ is a $C^\infty$ curve”; filled in, as for vector fields in Lemma [[§72 Lie Derivatives#^lem-72-4|§72.4]].)* Since $\mathcal{D}$ is open and $\varphi$ is continuous with $\varphi(0, p) = p$, there are $\varepsilon > 0$ and an open $U' \subseteq U$ containing $p$ with $(-\varepsilon, \varepsilon) \times U' \subseteq \mathcal{D}$ and $\varphi\big((-\varepsilon, \varepsilon) \times U'\big) \subseteq U$. Write $\alpha = \sum_B f_B\, dx^B$ on $U$, and $\varphi^i(t, x)$ for the components of $\varphi$ in the chart, smooth on $(-\varepsilon, \varepsilon) \times U'$. For fixed $t$, $\varphi_t$ maps $U'$ into $U$, and Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](4) gives, on $U'$,
>
> $$
> \varphi_t^{\ast}\alpha = \sum_A \Big( \sum_B f_B\big(\varphi(t, x)\big)\, \det\Big( \frac{\partial \varphi^{b_i}}{\partial x^{a_j}}(t, x) \Big)_{i, j} \Big)\, dx^A .
> $$
>
> The coefficient $g_A(t, x)$ is a sum of products of smooth functions of $(t, x)$. At $x = p$, the components of $t \mapsto \alpha_p(t)$ in the basis $dx^A|_p$ are the smooth functions $g_A(t, p)$, so the curve is smooth and its derivative at $0$ has components $\partial_t g_A(0, p)$. These are smooth functions of $x \in U'$, so $\mathcal{L}_\mathbf{X}\alpha$ is smooth near $p$, for every $p$ (Definition [[§80 Differential Forms on Manifolds#^def-80-4|§80.4]]).

^pf-85-1

*Uses:* [[§72 Lie Derivatives#^lem-72-4|§72.4]], [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]], [[§80 Differential Forms on Manifolds#^def-80-4|Def. §80.4]]

*Observation* (Lecture 34). If $k = 0$, $\alpha = f \in C^\infty(M)$, then $\mathcal{L}_\mathbf{X} f = \mathbf{X}(f)$. Indeed $\Lambda^0 T_p^{\ast}M = \mathbb{R}$, $\alpha_p(t) = (\varphi_t^{\ast}f)(p) = f(\varphi_t(p))$, and Definition [[§85 Lie Derivatives of Forms#^def-85-1|§85.1]] is Definition [[§72 Lie Derivatives#^def-72-1|§72.1]]; this is Proposition [[§72 Lie Derivatives#^prop-72-1|§72.1]]. This is the green vertical arrow $\mathcal{L}_\mathbf{X}$ of the diagram in [[§86 Cartan's Magic Formula|§86]], in degree $0$.

> [!example] Example §85.1: The Lie Derivative in Straightening Coordinates
> *(Lecture 34.)* Take $\mathbf{X} = \partial/\partial x^1$ in local coordinates $(x^1, \ldots, x^m)$, and $\alpha = f_A\, dx^A$, one of the monomials that generate forms in local coordinates, with $f_A$ smooth. By the canonical form near a regular point (Lemma [[§72 Lie Derivatives#^lem-72-5|§72.5]]) this is the normal form of a vector field near any point where it does not vanish. Then
>
> $$
> \mathcal{L}_\mathbf{X}\alpha = \frac{\partial f_A}{\partial x^1}\, dx^A .
> $$

^ex-85-1

> [!proof]+ Computation
> *(Lecture 34; the locality is filled in as in Case 2 of Theorem [[§72 Lie Derivatives#^thm-72-6|§72.6]].)* The flow is translation in the $x^1$-coordinate, $\varphi_t(x^1, \ldots, x^m) = (x^1 + t, x^2, \ldots, x^m)$, for $x$ near a given point and $|t|$ small (Example [[§72 Lie Derivatives#^ex-72-1|§72.1]]). So the Jacobian of $\varphi_t$ in these coordinates is the identity matrix, and $\varphi_t^{\ast}(dx^A) = dx^A$: indeed $\varphi_t^{\ast}(dx^a) = d(x^a \circ \varphi_t) = d(x^a + t\,\delta^a_1) = dx^a$ (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](3)), and pullback preserves wedge products. Hence
>
> $$
> \varphi_t^{\ast}\alpha = (f_A \circ \varphi_t)\, dx^A = (\varphi_t^{\ast} f_A)\, dx^A ,
> $$
>
> and the curve is just the coefficient function composed with the flow, $f_A(x^1 + t, x^2, \ldots, x^m)$ times the fixed $dx^A|_x$. Its derivative at $t = 0$ is $\frac{\partial f_A}{\partial x^1}\, dx^A$.

^pf-ex-85-1

*Uses:* [[§72 Lie Derivatives#^thm-72-6|§72.6]], [[§72 Lie Derivatives#^ex-72-1|Ex. §72.1]], [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]]

The Lie derivative of forms has properties analogous to those of the exterior derivative; the only question in the product rule is whether there is a sign.

> [!theorem] Theorem §85.2: Properties of the Lie Derivative of Forms
> Let $\mathbf{X} \in \mathfrak{X}(M)$ with flow $\varphi$, and let $\alpha \in \Omega^k(M)$, $\beta \in \Omega^l(M)$.
>
> 1. $\mathcal{L}_\mathbf{X}$ is $\mathbb{R}$-linear: $\mathcal{L}_\mathbf{X}(\alpha + c\,\alpha') = \mathcal{L}_\mathbf{X}\alpha + c\,\mathcal{L}_\mathbf{X}\alpha'$ for $\alpha, \alpha' \in \Omega^k(M)$ and $c \in \mathbb{R}$.
> 2. $\mathcal{L}_\mathbf{X}(\alpha \wedge \beta) = (\mathcal{L}_\mathbf{X}\alpha) \wedge \beta + \alpha \wedge (\mathcal{L}_\mathbf{X}\beta)$, with no sign.
> 3. $\mathcal{L}_\mathbf{X}(d\alpha) = d(\mathcal{L}_\mathbf{X}\alpha)$.
> 4. $\mathcal{L}_\mathbf{X}(\varphi_t^{\ast}\alpha) = \varphi_t^{\ast}(\mathcal{L}_\mathbf{X}\alpha)$, for every $t$, on the open set $M_t$ where $\varphi_t$ is defined.
>
> *Lee: Proposition 14.33; Corollary 14.36; Proposition 12.36; for tensor fields, Proposition 12.32*

^thm-85-2

The symbol $\mathcal{L}$ has two entries, $\mathbf{X}$ and $\alpha$; in this section $\mathbf{X}$ is fixed. Lecture 34 stated (1) also with respect to $\mathbf{X}$: $\mathcal{L}_{\mathbf{X} + c\mathbf{Y}}\alpha = \mathcal{L}_\mathbf{X}\alpha + c\,\mathcal{L}_\mathbf{Y}\alpha$. This is not visible from the definition, since the flow of $\mathbf{X} + c\mathbf{Y}$ is not built simply from those of $\mathbf{X}$ and $\mathbf{Y}$; it is Corollary [[§86 Cartan's Magic Formula#^cor-86-3|§86.3]], proved with Cartan's formula. In (4), the left-hand side is the Lie derivative of the form $\varphi_t^{\ast}\alpha$ on the open submanifold $M_t$, with respect to the restriction of $\mathbf{X}$, whose flow near each point is again $\varphi_s$ for small $|s|$.

Lecture 34 gave explanations of (2) and (3), close to proofs, and a proof of (4). Below, each explanation is kept and completed to a proof.

> [!proof]+ Proof
> *(Lecture 34: explanations of (2) and (3) and the proof of (4), each completed; (1) is filled in.)*
>
> (1) Pullback is linear (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](1)), so $(\varphi_t^{\ast}(\alpha + c\alpha'))_p = \alpha_p(t) + c\,\alpha'_p(t)$, and the derivative at $t = 0$ of a sum of curves in the vector space $\Lambda^k T_p^{\ast}M$ is the sum of the derivatives.
>
> (2) *Explanation* (Lecture 34). Very schematically, $\mathcal{L}_\mathbf{X}(\alpha \wedge \beta) = \frac{d}{dt}\big|_{t=0} \varphi_t^{\ast}(\alpha \wedge \beta)$, and pullback fits well with wedge, $\varphi_t^{\ast}(\alpha \wedge \beta) = (\varphi_t^{\ast}\alpha) \wedge (\varphi_t^{\ast}\beta)$. Evaluated on $k + l$ vectors this is a sum over shuffles $\sigma \in \mathrm{Sh}(k, l)$ of $\operatorname{sgn}(\sigma)$ times an ordinary product of a value of $\varphi_t^{\ast}\alpha$ and a value of $\varphi_t^{\ast}\beta$. The ordinary product rule of calculus gives a plus sign, and reconstituting the whole thing gives no additional signs. *Proof* *(filled in)*. Fix $p$. By Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](2), $(\alpha \wedge \beta)_p(t) = \alpha_p(t) \wedge \beta_p(t)$. The wedge product $\Lambda^k T_p^{\ast}M \times \Lambda^l T_p^{\ast}M \to \Lambda^{k+l} T_p^{\ast}M$ is bilinear on fixed finite-dimensional spaces, and for a bilinear map $B$ and smooth curves $a(t)$, $b(t)$, $\frac{d}{dt} B(a(t), b(t)) = B(\dot a(t), b(t)) + B(a(t), \dot b(t))$ (in bases, $B$ is a sum of products of components, and this is the product rule for each). At $t = 0$ this is (2) at $p$.
>
> (3) *Explanation* (Lecture 34). $\mathcal{L}_\mathbf{X}(d\alpha) = \frac{d}{dt}\big|_{t=0} \varphi_t^{\ast}(d\alpha) = \frac{d}{dt}\big|_{t=0} d(\varphi_t^{\ast}\alpha)$, since $d$ commutes with pullbacks (Theorem [[§81 The Exterior Derivative#^thm-81-7|§81.7]](4)). It remains to commute $d$ with $\frac{d}{dt}$, and that is Clairaut: written in coordinates, $\varphi_t^{\ast}\alpha$ is a smooth function of $t$ and $x$; $d$ involves the partials $\partial/\partial x^i$, and $\frac{d}{dt}$ is the derivative in $t$, so this is exchanging the order of differentiation. *Proof* *(filled in)*. Fix $p$ and take $U'$, $\varepsilon$ and $\varphi_t^{\ast}\alpha = \sum_A g_A(t, x)\, dx^A$ on $U'$ as in Lemma [[§85 Lie Derivatives of Forms#^lem-85-1|§85.1]]. For each fixed $t$, $\varphi_t^{\ast}(d\alpha) = d(\varphi_t^{\ast}\alpha)$ on $U'$ (naturality for $\varphi_t|_{U'}$, with Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](3)), and by Corollary [[§81 The Exterior Derivative#^cor-81-6|§81.6]],
>
> $$
> \varphi_t^{\ast}(d\alpha) = \sum_A \sum_j \frac{\partial g_A}{\partial x^j}(t, x)\; dx^j \wedge dx^A \quad \text{on } U' .
> $$
>
> Differentiating in $t$ at $t = 0$, componentwise, gives $\mathcal{L}_\mathbf{X}(d\alpha) = \sum_A \sum_j \frac{\partial^2 g_A}{\partial t\, \partial x^j}(0, x)\, dx^j \wedge dx^A$ on $U'$. On the other hand $\mathcal{L}_\mathbf{X}\alpha = \sum_A \frac{\partial g_A}{\partial t}(0, x)\, dx^A$, so $d(\mathcal{L}_\mathbf{X}\alpha) = \sum_A \sum_j \frac{\partial^2 g_A}{\partial x^j\, \partial t}(0, x)\, dx^j \wedge dx^A$. The mixed partials of the smooth functions $g_A$ agree.
>
> (4) *(Lecture 34; it follows from the group law.)* Fix $t$ and $p \in M_t$, and let $q = \varphi_t(p)$. For $|s|$ small, the group law (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]]) gives $\varphi_s \circ \varphi_t = \varphi_{t+s} = \varphi_t \circ \varphi_s$ near $p$ (these flows commute), and in particular $\varphi_{t+s}(p) = \varphi_s(q)$. By Definition [[§85 Lie Derivatives of Forms#^def-85-1|§85.1]] and Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]](1),
>
> $$
> \mathcal{L}_\mathbf{X}(\varphi_t^{\ast}\alpha)_p = \frac{d}{ds}\Big|_{s=0} \big(\varphi_s^{\ast}\varphi_t^{\ast}\alpha\big)_p = \frac{d}{ds}\Big|_{s=0} \big(\varphi_t^{\ast}\varphi_s^{\ast}\alpha\big)_p = \frac{d}{ds}\Big|_{s=0} (d\varphi_t)_p^{\ast}\, \big(\varphi_s^{\ast}\alpha\big)_q = \frac{d}{ds}\Big|_{s=0} (d\varphi_t)_p^{\ast}\, \alpha_q(s) .
> $$
>
> Now $t$ is fixed, so the differential $(d\varphi_t)_p : T_pM \to T_qM$ induces a fixed linear map $(d\varphi_t)_p^{\ast} : \Lambda^k T_q^{\ast}M \to \Lambda^k T_p^{\ast}M$; and $s \mapsto \alpha_q(s)$ is a curve in $\Lambda^k T_q^{\ast}M$. The curve in $\Lambda^k T_p^{\ast}M$ being differentiated is the image of this curve under the linear map, and taking the derivative commutes with a linear map:
>
> $$
> \mathcal{L}_\mathbf{X}(\varphi_t^{\ast}\alpha)_p = (d\varphi_t)_p^{\ast}\, \frac{d}{ds}\Big|_{s=0} \alpha_q(s) = (d\varphi_t)_p^{\ast}\, (\mathcal{L}_\mathbf{X}\alpha)_q = \big(\varphi_t^{\ast}(\mathcal{L}_\mathbf{X}\alpha)\big)_p .
> $$

^pf-85-2

*Uses:* [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]], [[§81 The Exterior Derivative#^thm-81-7|§81.7]], [[§85 Lie Derivatives of Forms#^lem-85-1|§85.1]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]], [[§81 The Exterior Derivative#^cor-81-6|§81.6]], [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]], [[§85 Lie Derivatives of Forms#^def-85-1|Def. §85.1]]

![[m591-81-2.svg]]

*(Figure after the board.)* The proof of (4), with $t$ fixed and $q = \varphi_t(p)$. Top: the differential of the time-$t$ map. Middle: the linear map it induces on $k$-covectors, in the opposite direction. Bottom: a point of the curve $s \mapsto \alpha_q(s)$ in the fixed space $\Lambda^k T_q^{\ast}M$ and its image in $\Lambda^k T_p^{\ast}M$. The image of the curve is the curve $s \mapsto (\varphi_t^{\ast}\varphi_s^{\ast}\alpha)_p$, and the derivative of the image is the image of the derivative.

**Transcription notes (Lecture 34).** In the proof of (4) the board first wrote $T_q M$ where $\Lambda^k T_q^{\ast}M$ is meant (corrected in class to $T_q^{\ast}M$, and then to $\Lambda^k T_q^{\ast}M$), and $\alpha_{\varphi_s(q)}$ for the point of $\Lambda^k T_q^{\ast}M$; that is a covector at the moving point $\varphi_s(q)$, not a point of $\Lambda^k T_q^{\ast}M$, and the object is $\alpha_q(s) = (\varphi_s^{\ast}\alpha)_q$, a curve at the fixed point $q$. In the handwritten notes the same object appears as $\alpha_{q(s)}$.

> [!theorem] Corollary §85.3: Zero Lie Derivative Means Invariance
> Let $\alpha \in \Omega^k(M)$. For every $p$ and every $t$ with $p \in M_t$,
>
> $$
> \frac{d}{dt}\, (\varphi_t^{\ast}\alpha)_p = \big(\varphi_t^{\ast}(\mathcal{L}_\mathbf{X}\alpha)\big)_p .
> $$
>
> In particular, if $\mathcal{L}_\mathbf{X}\alpha = 0$, then $\varphi_t^{\ast}\alpha = \alpha$ wherever defined.
>
> *Lee: Proposition 12.36; Theorem 12.37*

^cor-85-3

> [!proof]+ Proof
> *(Lecture 34: the curves $t \mapsto (\varphi_t^{\ast}\alpha)_p$ are constant; the derivative at every time is filled in.)* Fix $p$ and $t_0$ with $p \in M_{t_0}$. Then $(\varphi_{t_0 + s}^{\ast}\alpha)_p = (\varphi_s^{\ast}\varphi_{t_0}^{\ast}\alpha)_p$ for small $|s|$, by the group law, so the derivative at $t_0$ of $t \mapsto (\varphi_t^{\ast}\alpha)_p$ is the derivative at $s = 0$ of $s \mapsto (\varphi_s^{\ast}(\varphi_{t_0}^{\ast}\alpha))_p$, which is $\mathcal{L}_\mathbf{X}(\varphi_{t_0}^{\ast}\alpha)_p = (\varphi_{t_0}^{\ast}\mathcal{L}_\mathbf{X}\alpha)_p$ by (4). If $\mathcal{L}_\mathbf{X}\alpha = 0$, the curve $t \mapsto (\varphi_t^{\ast}\alpha)_p$, defined on the open interval of times of the maximal integral curve through $p$, an interval containing $0$, has zero derivative everywhere, so it is constant, equal to its value $\alpha_p$ at $t = 0$.

^pf-85-3

*Divergence and volume.* Lecture 34 gave a first application of Corollary [[§85 Lie Derivatives of Forms#^cor-85-3|§85.3]], on open subsets of $\mathbb{R}^m$ (or in local coordinates), through a problem on Homework 10.

> [!definition] Definition §85.2: Divergence
> *(Calculus III; recalled in Lecture 34.)* Let $M \subseteq \mathbb{R}^m$ be open and $\mathbf{X} = \sum_{i=1}^m f^i\, \partial/\partial x^i \in \mathfrak{X}(M)$. The **divergence** of $\mathbf{X}$ is the function
>
> $$
> \operatorname{div}\mathbf{X} = \sum_{i=1}^m \frac{\partial f^i}{\partial x^i} \in C^\infty(M) .
> $$

^def-85-2


> [!remark]- Connections
> - On $\mathbb{R}^3$ the divergence is $d$ on two-forms: [[§81 The Exterior Derivative#^ex-81-1|Ex. §81.1]]; in MATH 452, [[§38 The Exterior Derivative#^prop-38-3|452 Prop. §38.3]].

> [!definition] Definition §85.3: Volume Form of an Open Subset of $\mathbb{R}^m$
> *(Lecture 34.)* Let $M \subseteq \mathbb{R}^m$ be open. The **volume form** of $M$ is the $m$-form
>
> $$
> \mathrm{dvol} = dx^1 \wedge \cdots \wedge dx^m \in \Omega^m(M) .
> $$

^def-85-3

The name: given $m$ vectors $v^1, \ldots, v^m$ at a point, $\mathrm{dvol}(v^1, \ldots, v^m)$ is the $m \times m$ determinant of their components, $\det\big(dx^i(v^j)\big)$ (Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]]), and its absolute value is the volume of the parallelepiped spanned by the vectors.

> [!theorem] Proposition §85.4: The Lie Derivative of the Volume Form
> *(Lecture 34; a problem on Homework 10.)* Let $M \subseteq \mathbb{R}^m$ be open and $\mathbf{X} \in \mathfrak{X}(M)$. Then
>
> $$
> \mathcal{L}_\mathbf{X}\, \mathrm{dvol} = (\operatorname{div}\mathbf{X})\; \mathrm{dvol} .
> $$

^prop-85-4

> [!proof]+ Proof (to be filled after the homework)
> Lecture 34 stated this as a problem on Homework 10, so the proof is written here after the homework is handed in.

^pf-85-4

So the divergence is the rate at which the flow changes volume: by Corollary [[§85 Lie Derivatives of Forms#^cor-85-3|§85.3]], $\frac{d}{dt}(\varphi_t^{\ast}\mathrm{dvol})_p = \big(\varphi_t^{\ast}((\operatorname{div}\mathbf{X})\,\mathrm{dvol})\big)_p$.

> [!theorem] Corollary §85.5: Divergence-Free Flows Preserve Volume
> *(Lecture 34.)* Let $M \subseteq \mathbb{R}^m$ be open and $\mathbf{X} \in \mathfrak{X}(M)$ with $\operatorname{div}\mathbf{X} = 0$, with flow $\varphi$. Then $\varphi_t^{\ast}\,\mathrm{dvol} = \mathrm{dvol}$ on $M_t$, for every $t$. Equivalently, the Jacobian matrix of $\varphi_t$ has determinant $1$ at every point of $M_t$: the flow is *volume-preserving*.

^cor-85-5

> [!proof]+ Proof
> *(Lecture 34; the Jacobian is filled in.)* By Proposition [[§85 Lie Derivatives of Forms#^prop-85-4|§85.4]], $\mathcal{L}_\mathbf{X}\,\mathrm{dvol} = 0 \cdot \mathrm{dvol} = 0$, so $\varphi_t^{\ast}\,\mathrm{dvol} = \mathrm{dvol}$ wherever defined, by Corollary [[§85 Lie Derivatives of Forms#^cor-85-3|§85.3]]. *The Jacobian.* Write $\varphi_t = (\varphi_t^1, \ldots, \varphi_t^m)$ on $M_t$. Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](4), with the identity charts, $F = \varphi_t$, $\omega = \mathrm{dvol}$ and $k = m$ (so $A = B = \{1, \ldots, m\}$ is the only index set), gives
>
> $$
> \varphi_t^{\ast}\,\mathrm{dvol} = \det\Big( \frac{\partial \varphi_t^i}{\partial x^j} \Big)_{i, j = 1, \ldots, m}\; \mathrm{dvol} \qquad \text{on } M_t .
> $$
>
> Since $\mathrm{dvol}_p \ne 0$ at every $p$, $\varphi_t^{\ast}\,\mathrm{dvol} = \mathrm{dvol}$ holds exactly when this determinant is $1$ at every point of $M_t$.

^pf-85-5

*Uses:* [[§85 Lie Derivatives of Forms#^prop-85-4|§85.4]], [[§85 Lie Derivatives of Forms#^cor-85-3|§85.3]], [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]]


![[m591-81-a2.gif|600]]

*(Not from lecture; animation added, vault only.)* A unit square carried by two flows on $\mathbb{R}^2$. Left: the shear field $\mathbf{X} = y\,\partial_x$, with flow $\varphi_t(x, y) = (x + ty, y)$ and $\operatorname{div}\mathbf{X} = 0$: the square becomes a parallelogram of the same area, since the Jacobian of $\varphi_t$ has determinant $1$ ([[§85 Lie Derivatives of Forms#^cor-85-5|§85.5]]). Right: $\mathbf{X} = x\,\partial_x$, with flow $\varphi_t(x, y) = (e^t x, y)$ and $\operatorname{div}\mathbf{X} = 1$: the area is $e^t$, and its rate of change at $t = 0$ is $1 = \operatorname{div}\mathbf{X}$.

> [!remark] Remark: Hamiltonian Flows
> *(Lecture 34.)* In classical mechanics, the flow of a Hamiltonian vector field preserves the symplectic form, for the same reason: the Lie derivative of the symplectic form along the field is zero, and Corollary [[§85 Lie Derivatives of Forms#^cor-85-3|§85.3]] applies. Symplectic forms are not developed in these notes; the one on a cotangent bundle is mentioned in [[§52 The Cotangent Bundle|§52]]. These are preliminary results; Cartan's formula comes next.

^rem-85-2
