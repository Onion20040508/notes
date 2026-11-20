---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 83
tags: [differentiable-manifolds, math591]
---
← [[§82 De Rham Cohomology]] · ↑ [[· 11 Differential Forms]] · [[§84 Contraction by Vector Fields]] →

*Stage: forms — The first nonzero cohomology class in positive degree: the angle form on the punctured plane is closed but not exact; on the circle, integration identifies $H^1(S^1)$ with $\mathbb{R}$.*

*(Lecture 33.)* After the terminology of [[§82 De Rham Cohomology|§82]] (closed and exact forms, $Z^k$ and $B^k$, recalled at the start of the lecture) and the degree-zero example ($b_0$ is the number of connected components, Proposition [[§82 De Rham Cohomology#^prop-82-3|§82.3]]), the next examples are in degree one.

> [!remark] Remark: Notation of Lecture 33
> In addition to the remarks *Notation of Lecture 31* and *Notation of Lecture 32*:
> - *Closed and exact forms.* $Z^k(M)$ and $B^k(M)$ are the spaces of closed and of exact $k$-forms (Definitions [[§82 De Rham Cohomology#^def-82-1|§82.1]] and [[§82 De Rham Cohomology#^def-82-2|§82.2]]); $H^k(M) = Z^k(M)/B^k(M)$, and $[\omega]$ is the class of $\omega$.
> - *Induced maps.* The map on cohomology induced by $F$ is written $F^{\ast}$, like the pullback of forms (Proposition [[§82 De Rham Cohomology#^prop-82-2|§82.2]]).
> - *Calculus notation.* On an open subset of $\mathbb{R}^2$, a one-form is written $P\, dx + Q\, dy$, and subscripts are partial derivatives: $Q_x = \partial Q/\partial x$.
> - *The angle.* $\theta$ is the polar angle, which is not a function on $\mathbb{R}^2 \setminus \{0\}$; $d\theta$ is a one-form on $\mathbb{R}^2 \setminus \{0\}$ all the same (Example [[§83 The First Cohomology of the Circle#^ex-83-2|§83.2]]), and on $S^1$ it denotes the pullback $\iota^{\ast}\omega$. For a function $g$ on $S^1$, $g' = dg/d\theta$ is the derivative of $g$ regarded as a $2\pi$-periodic function of $\theta$ (Lemma [[§83 The First Cohomology of the Circle#^lem-83-3|§83.3]]).
> - *Contraction* ([[§84 Contraction by Vector Fields|§84]]). $\iota_\mathbf{X}\alpha$ is the contraction of $\alpha$ by the vector field $\mathbf{X}$; Lee also writes $\mathbf{X} \mathbin{\lrcorner} \alpha$, read “$\mathbf{X}$ into $\alpha$”. (The handwritten notes have $\alpha \mathbin{\lrcorner} \mathbf{X}$; Lee's order puts the vector first.) The letter $\iota$ is also used for inclusions, $\iota : S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\}$; a subscript vector field marks the contraction. Vector fields are bold, $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, as elsewhere in these notes; $\mathbf{X}h$ is the function $D_\mathbf{X}h$ (Definition [[§56 Vector Fields#^def-56-8|§56.8]]), and $\alpha(\mathbf{X})$ is the function $p \mapsto \alpha_p(\mathbf{X}_p)$. Tangent vectors are $v^1, \ldots, v^{k-1}$ (the board: $v_1, \ldots, v_{k-1}$).

^rem-83-1

> [!example] Example §83.1: One-Forms on Open Subsets of the Plane
> *(Lecture 33.)* Let $M \subseteq \mathbb{R}^2$ be open and $\omega = P\, dx + Q\, dy$ with $P, Q \in C^\infty(M)$. Then
>
> $$
> d\omega = (Q_x - P_y)\; dx \wedge dy .
> $$
>
> So $\omega$ is closed exactly when $Q_x = P_y$, the condition of Definition [[§53 One-Forms#^def-53-5|§53.5]].

^ex-83-1

> [!proof]+ Computation
> *(Filled in.)* By Definition [[§81 The Exterior Derivative#^def-81-2|§81.2]], $d\omega = dP \wedge dx + dQ \wedge dy = (P_x\, dx + P_y\, dy) \wedge dx + (Q_x\, dx + Q_y\, dy) \wedge dy = P_y\, dy \wedge dx + Q_x\, dx \wedge dy$, since $dx \wedge dx = dy \wedge dy = 0$; and $dy \wedge dx = -\,dx \wedge dy$.

^pf-ex-83-1

*Uses:* [[§81 The Exterior Derivative#^def-81-2|Def. §81.2]]

The standard example, perhaps seen in Calculus III, is the one of Example [[§53 One-Forms#^ex-53-2|§53.2]], now in the language of cohomology. The form looks a little contrived, but it is a natural thing: it is $d\theta$.

> [!example] Example §83.2: The Angle Form Is Closed but Not Exact
> *(Lecture 33.)* On $M = \mathbb{R}^2 \setminus \{(0, 0)\}$ let
>
> $$
> \omega = \frac{-y}{x^2 + y^2}\; dx + \frac{x}{x^2 + y^2}\; dy .
> $$
>
> 1. $\omega$ is closed: $Q_x = P_y$ identically, so $d\omega = 0$.
> 2. In fact $\omega = d\theta$, where $\theta$ is the polar angle: on each open set where a continuous branch of $\theta$ is chosen, that branch is smooth and its differential is $\omega$.
> 3. $\omega$ is not exact: the Calculus III line integral of $\omega$ over the unit circle is $\int_{S^1} \omega = \int_0^{2\pi} d\theta = 2\pi \neq 0$, while by the fundamental theorem of calculus for line integrals, $\int_A^B df = f(B) - f(A)$, which is $0$ around a closed curve.
>
> So $[\omega] = [d\theta]$ is a nonzero class in $H^1(\mathbb{R}^2 \setminus \{0\})$.
>
> *Lee: Example 11.36; Example 17.1*

^ex-83-2

> [!remark]- Connections
> - The same form, step by step, with the angle on the slit plane: [[§53 One-Forms#^ex-53-2|Ex. §53.2]]; closed and exact one-forms: [[§53 One-Forms#^def-53-5|Def. §53.5]], [[§53 One-Forms#^def-53-6|Def. §53.6]].
> - In MATH 452: [[§39 Closed and Exact Forms#^prop-39-6|452 Prop. §39.6]]. On star-shaped domains every closed form is exact, the [[Poincaré Lemma]]; the punctured plane is not star-shaped.

> [!proof]+ Justification
> (1) is step 3 of Example [[§53 One-Forms#^ex-53-2|§53.2]], where both sides are computed to be $(y^2 - x^2)/(x^2 + y^2)^2$.
>
> (2) *(Lecture 33 did the computation for $\theta = \tan^{-1}(y/x)$; the other branches are filled in.)* On the right half-plane $\{x > 0\}$, $\theta = \tan^{-1}(y/x)$ is a branch. With $(\tan^{-1})'(s) = 1/(1 + s^2)$ and the chain rule,
>
> $$
> d\Big(\tan^{-1}\frac{y}{x}\Big) = \frac{-y/x^2}{1 + y^2/x^2}\; dx + \frac{1/x}{1 + y^2/x^2}\; dy = \frac{-y}{x^2 + y^2}\; dx + \frac{x}{x^2 + y^2}\; dy = \omega ,
> $$
>
> multiplying numerators and denominators by $x^2$. On $\{y > 0\}$, $\{x < 0\}$ and $\{y < 0\}$ the functions $\frac{\pi}{2} - \tan^{-1}(x/y)$, $\pi + \tan^{-1}(y/x)$ and $-\frac{\pi}{2} - \tan^{-1}(x/y)$ are branches of $\theta$, and the same computation gives $\omega$ for each; for instance $d\big(-\tan^{-1}(x/y)\big) = -\frac{(1/y)\, dx - (x/y^2)\, dy}{1 + x^2/y^2} = \frac{-y\, dx + x\, dy}{x^2 + y^2}$. Since $d \circ d = 0$, $\omega = d\theta$ on each half-plane justifies again that $\omega$ is closed.
>
> (3) is steps 4–6 of Example [[§53 One-Forms#^ex-53-2|§53.2]]: along $c(t) = (\cos t, \sin t)$, $\omega$ takes the value $1$ on the velocity, so $\int_{S^1}\omega = \int_0^{2\pi} 1\, dt = 2\pi$; if $\omega = df$, then $(f \circ c)' = 1$ and $f(c(2\pi)) - f(c(0)) = 2\pi$, while $c(2\pi) = c(0)$.

^pf-ex-83-2

*Uses:* [[§53 One-Forms#^ex-53-2|Ex. §53.2]]

*There is no contradiction in writing $\omega = d\theta$ with $\omega$ not exact.* The reason is that $\theta$ is not a smooth function on $\mathbb{R}^2 \setminus \{0\}$; it is not even a continuous one. It is the measure of an angle in radians, which is defined only up to an additive multiple of $2\pi$.

> [!theorem] Lemma §83.1: Branches of the Angle Differ by Constants
> *(Lecture 33, an observation.)* A *branch of $\theta$* on an open set $W \subseteq \mathbb{R}^2 \setminus \{0\}$ is a continuous function $\vartheta : W \to \mathbb{R}$ with $(x, y) = r\,(\cos\vartheta, \sin\vartheta)$ on $W$, where $r = \sqrt{x^2 + y^2}$. Any two branches of $\theta$ on a connected open set differ by a constant. So $d\theta$ is well defined: every branch is smooth, and its differential is the form $\omega$ of Example [[§83 The First Cohomology of the Circle#^ex-83-2|§83.2]], on its domain.

^lem-83-1

> [!remark]- Connections
> - A branch of $\theta$ along a path is a lift of the path through the covering $\mathbb{R} \to S^1$, $t \mapsto (\cos t, \sin t)$: [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lem. §32.1]], [[§32 Lifting and the Fundamental Group of the Circle#^ex-32-1|590 Ex. §32.1]]. Two lifts differ by a constant multiple of $2\pi$.

> [!proof]+ Proof
> *(Filled in.)* If $\vartheta_1$ and $\vartheta_2$ are branches on a connected open set $W$, then $\cos$ and $\sin$ agree at $\vartheta_1$ and $\vartheta_2$, so $\vartheta_1 - \vartheta_2$ is continuous with values in $2\pi\mathbb{Z}$, hence constant on $W$. For the second statement, let $\vartheta$ be a branch on an open set $W$ and $q \in W$. The point $q$ lies in one of the four open half-planes $H$ of the justification above, on which there is a smooth branch $\vartheta_H$ with $d\vartheta_H = \omega$. On a connected open neighbourhood of $q$ in $W \cap H$, $\vartheta - \vartheta_H$ is constant, by the first statement; so $\vartheta$ is smooth near $q$, and $d\vartheta = d\vartheta_H = \omega$ there.

^pf-83-1

*Conclusion.* $[d\theta] \neq 0$ in $H^1(\mathbb{R}^2 \setminus \{0\})$: the first nontrivial cohomology class of positive degree seen in the course. In fact $H^1(\mathbb{R}^2 \setminus \{0\})$ is one-dimensional, with basis $[d\theta]$; there is a reason why the de Rham cohomology of the punctured plane is the same as that of the circle, which will be seen later (homotopy invariance). For now, the circle.

![[m591-80-2.svg]]

*(Not from lecture; figure added.)* The angle $\theta$ on $\mathbb{R}^2 \setminus \{0\}$ (origin removed, hollow dot). A continuous branch of $\theta$ exists only after a cut is removed; across the cut drawn here, the branch with values in $(0, 2\pi)$ jumps by $2\pi$. The one-form $d\theta = \omega$ does not see the cut: on each side, branches differ by constants. On the unit circle, the rotation field $\partial_\theta$, with $\partial_\theta(x, y) = (-y, x)$, satisfies $d\theta(\partial_\theta) = 1$; going once around, $\theta$ increases by $\int_{S^1} d\theta = 2\pi$.

![[m591-80-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* A branch of $\theta$ continued along the unit circle, drawn as height over the circle: the graph is a helix of slope $d\theta(\partial_\theta) = 1$, and after one turn it is $2\pi$ above its starting value. So $\theta$ is not a function on $\mathbb{R}^2 \setminus \{0\}$, while its slope $d\theta$ is a well-defined one-form, with $\int_{S^1} d\theta = 2\pi$.

*The circle.* Let $\iota : S^1 \hookrightarrow \mathbb{R}^2 \setminus \{0\}$ be the inclusion. Abusing the notation, write

$$
d\theta = \iota^{\ast}\omega \in \Omega^1(S^1) .
$$

If $S^1$ is regarded as a Lie group (rotations), the generator of the circle action is the field $\partial_\theta$ given in Cartesian coordinates by $(-y, x)$, and $d\theta(\partial_\theta) = 1$. Every one-form on $S^1$ is closed, for dimensional reasons, and this holds for every form of top degree, that is, of degree equal to the dimension.

> [!theorem] Lemma §83.2: Top-Degree Forms Are Closed
> *(Lecture 33, in answer to a question.)* If $\dim M = m$, every $m$-form on $M$ is closed: $Z^m(M) = \Omega^m(M)$, and so $H^m(M) = \Omega^m(M)/B^m(M)$. In particular $\Omega^1(S^1) = Z^1(S^1)$.

^lem-83-2

> [!proof]+ Proof
> For $\omega \in \Omega^m(M)$, $d\omega$ is an $(m+1)$-form, and $\Lambda^{m+1}T_p^{\ast}M = 0$ at every $p$, since any $m + 1$ vectors of the $m$-dimensional space $T_pM$ are linearly dependent (Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]]). So $d\omega = 0$. For $S^1$: $\Lambda^2$ of a one-dimensional space is zero.

^pf-83-2

*Uses:* [[§75 Multilinear Algebra#^cor-75-3|§75.3]]

In particular $d\theta \in Z^1(S^1)$, and $H^1(S^1) = \Omega^1(S^1)/B^1(S^1)$: the question is which one-forms on the circle are exact.

> [!theorem] Lemma §83.3: Functions and One-Forms on the Circle
> *(Not from lecture; filled in. Lecture 33 used $C^\infty(S^1)$ as the space of $2\pi$-periodic functions of $\theta$; this lemma says what that means.)* Let $p : \mathbb{R} \to S^1$, $p(t) = (\cos t, \sin t)$.
>
> 1. $g \mapsto g \circ p$ is a linear bijection from $C^\infty(S^1)$ onto the space of smooth $2\pi$-periodic functions on $\mathbb{R}$.
> 2. $p^{\ast}(d\theta) = dt$, and $(d\theta)_q(\partial_\theta|_q) = 1$ for every $q \in S^1$. Every one-form on $S^1$ is $\alpha = f\, d\theta$ for a unique $f \in C^\infty(S^1)$, namely $f = \alpha(\partial_\theta)$.
> 3. For $f, g \in C^\infty(S^1)$: $dg = f\, d\theta$ if and only if $(g \circ p)' = f \circ p$. Writing $g' = dg/d\theta$ for $(g \circ p)'$ read as a function on $S^1$, $dg = g'\, d\theta$.

^lem-83-3

> [!proof]+ Proof
> (1) $p$ is smooth into $\mathbb{R}^2$ with values in the regular submanifold $S^1$, hence smooth into $S^1$, so $g \circ p$ is smooth, and it is $2\pi$-periodic. Conversely, let $G$ be smooth and $2\pi$-periodic. Then $G = g \circ p$ for exactly one function $g$ on $S^1$, since $p(t) = p(t')$ if and only if $t - t' \in 2\pi\mathbb{Z}$. On the chart domains $U_a$ and $U_b$ of the angle atlas (Example [[§17 Differentiable Structures#^ex-17-4|§17.4]]), $p$ restricted to $(0, 2\pi)$, respectively $(\pi, 3\pi)$, is the inverse of the chart $\varphi_a$, respectively $\varphi_b$. So $g = G \circ \varphi_a$ on $U_a$ and $g = G \circ \varphi_b$ on $U_b$, both smooth (the angle atlas belongs to the smooth structure of $S^1$, Proposition [[§24 The Circle#^prop-24-1|§24.1]]).
>
> (2) $p^{\ast}(d\theta) = (\iota \circ p)^{\ast}\omega$ (Lemma [[§81 The Exterior Derivative#^lem-81-4|§81.4]]), and with $x = \cos t$, $y = \sin t$, $x^2 + y^2 = 1$,
>
> $$
> (\iota \circ p)^{\ast}\omega = -\sin t\; d(\cos t) + \cos t\; d(\sin t) = (\sin^2 t + \cos^2 t)\, dt = dt .
> $$
>
> The velocity of $p$ at $t$ is $(-\sin t, \cos t) = \partial_\theta|_{p(t)}$, that is, $dp_t(\partial_t) = \partial_\theta|_{p(t)}$; hence $(d\theta)_{p(t)}(\partial_\theta) = (p^{\ast}d\theta)_t(\partial_t) = dt(\partial_t) = 1$. Since $T_q^{\ast}S^1$ is one-dimensional and $(d\theta)_q \neq 0$, $(d\theta)_q$ is a basis of it, and $\alpha_q = \alpha_q(\partial_\theta|_q)\, (d\theta)_q$; the function $f = \alpha(\partial_\theta)$ is smooth, because $\alpha$ and the field $\partial_\theta$ (the restriction to $S^1$ of the smooth field $(-y, x)$, which is tangent to $S^1$) are smooth.
>
> (3) $p^{\ast}(dg) = d(g \circ p) = (g \circ p)'\, dt$ (Proposition [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]](3)) and $p^{\ast}(f\, d\theta) = (f \circ p)\, dt$ by (2). For each $q \in S^1$ there is $t$ with $p(t) = q$ in $(0, 2\pi)$ or $(\pi, 3\pi)$, where $p$ is the inverse of a chart, so $dp_t$ is an isomorphism; hence a one-form $\beta$ on $S^1$ with $p^{\ast}\beta = 0$ is zero. Applied to $\beta = dg - f\, d\theta$, this gives the equivalence.

^pf-83-3

*Uses:* [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], [[§24 The Circle#^prop-24-1|§24.1]], [[§81 The Exterior Derivative#^lem-81-4|§81.4]], [[§80 Differential Forms on Manifolds#^prop-80-5|§80.5]]

> [!theorem] Proposition §83.4: The First Cohomology of the Circle
> Let $\mathcal{S} : \Omega^1(S^1) \to \mathbb{R}$ be the linear map
>
> $$
> \mathcal{S}(f\, d\theta) = \int_0^{2\pi} f(\theta)\, d\theta \qquad \Big( = \int_0^{2\pi} f(p(t))\, dt \Big) .
> $$
>
> Then $\ker \mathcal{S} = B^1(S^1)$, and $\mathcal{S}$ is surjective. Hence $\mathcal{S}$ induces an isomorphism
>
> $$
> H^1(S^1) = \Omega^1(S^1)/B^1(S^1) \cong \mathbb{R} ,
> $$
>
> and $[d\theta]$ is a basis of $H^1(S^1)$: for every $\alpha \in \Omega^1(S^1)$ there are $c \in \mathbb{R}$ and $g \in C^\infty(S^1)$ with $\alpha = c\, d\theta + dg$. So $b_1(S^1) = 1$.
>
> *Lee: Theorem 17.21 ($n = 1$)*

^prop-83-4

> [!remark]- Connections
> - In MATH 590 the same count of turns gives $\pi_1(S^1) \cong \mathbb{Z}$, by lifting loops: [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-5|590 Thm. §32.5]]. For a loop $\gamma$ in $S^1$, $\frac{1}{2\pi}\int_\gamma d\theta$ is the integer attached to $\gamma$ there.
> - The general statement, for compact oriented connected manifolds: [[§83 The First Cohomology of the Circle#^thm-83-5|Thm. §83.5]].

> [!proof]+ Proof
> *(Lecture 33, in outline; details filled in.)* *What is to be shown.* The claim $[\alpha] = c\,[d\theta]$ means that $\alpha - c\, d\theta$ is exact, $\alpha = c\, d\theta + dg$. Put otherwise: what are the exact one-forms? By Lemma [[§83 The First Cohomology of the Circle#^lem-83-3|§83.3]](2), any one-form on $S^1$ is $\alpha = f\, d\theta$ with $f \in C^\infty(S^1)$, because $d\theta$ is nowhere zero, so pointwise it generates $T^{\ast}S^1$: it is a global frame. For which $f$ is there $g \in C^\infty(S^1)$ with $f\, d\theta = dg = \frac{dg}{d\theta}\, d\theta$, that is, $f = g'$?
>
> *The calculus I answer, and why it is not enough.* Think of functions on $S^1$ as $2\pi$-periodic functions of $\theta$ (Lemma [[§83 The First Cohomology of the Circle#^lem-83-3|§83.3]](1)) and write $F = f \circ p$. The solutions of $G' = F$ on $\mathbb{R}$ are
>
> $$
> G(\theta) = \int_0^\theta F(t)\, dt + C .
> $$
>
> Does this solve the problem? The derivative is right. But a function on the circle must be periodic, and this $G$ is periodic only if $\int_0^{2\pi} F = 0$. *(Filled in.)* Since $F$ is $2\pi$-periodic, $G(\theta + 2\pi) - G(\theta) = \int_\theta^{\theta + 2\pi} F(t)\, dt = \int_0^{2\pi} F(t)\, dt$ for every $\theta$. So if $\int_0^{2\pi} F = 0$, $G$ is smooth and periodic, $G = g \circ p$ for some $g \in C^\infty(S^1)$, and $dg = f\, d\theta$ by Lemma [[§83 The First Cohomology of the Circle#^lem-83-3|§83.3]](3). Conversely, if $f\, d\theta = dg$, then $G = g \circ p$ is periodic with $G' = F$, so $\int_0^{2\pi} F = G(2\pi) - G(0) = 0$. Hence
>
> $$
> f\, d\theta \in B^1(S^1) \iff \int_0^{2\pi} f(\theta)\, d\theta = 0 ,
> $$
>
> that is, $\ker \mathcal{S} = B^1(S^1)$.
>
> *Conclusion.* $\mathcal{S}$ is well defined, since $f$ is determined by $\alpha$, and clearly linear. It is onto: $\mathcal{S}(d\theta) = 2\pi \neq 0$, so $\mathcal{S}(\tfrac{c}{2\pi}\, d\theta) = c$. A surjective linear map induces an isomorphism from the domain divided by its kernel onto its target, so $\Omega^1(S^1)/B^1(S^1) \cong \mathbb{R}$, and this quotient is precisely $H^1(S^1)$, because $Z^1(S^1) = \Omega^1(S^1)$. Under the isomorphism $[d\theta] \mapsto 2\pi \neq 0$, so $[d\theta]$ is a basis; explicitly, $\alpha - \frac{\mathcal{S}(\alpha)}{2\pi}\, d\theta \in \ker\mathcal{S} = B^1(S^1)$.

^pf-83-4

*Uses:* [[§83 The First Cohomology of the Circle#^lem-83-3|§83.3]]

![[m591-80-3.svg]]

*(Not from lecture; figure added.)* The calculus I problem on the circle, Proposition [[§83 The First Cohomology of the Circle#^prop-83-4|§83.4]]. Left, $\alpha = (1 + \cos\theta)\, d\theta$: the antiderivative $G(t) = t + \sin t$ (drawn at a smaller scale) is not $2\pi$-periodic, so it is not a function on $S^1$, and $\alpha$ is not exact; $[\alpha] = [d\theta]$. Right, $\alpha = \cos\theta\, d\theta = d(\sin\theta)$ is exact.

![[m591-80-a2.gif|600]]

*(Not from lecture; animation added, vault only.)* The antiderivative $G(t) = \int_0^t F$ while $p(t) = (\cos t, \sin t)$ goes twice around $S^1$. For $F = \cos t$, $G = \sin t$ returns to its value after each turn, so it is a function on $S^1$, and $\cos\theta\, d\theta$ is exact. For $F = 1 + \cos t$, $G$ gains $\int_0^{2\pi} F = 2\pi$ per turn, so it is not a function on $S^1$, and $(1 + \cos\theta)\, d\theta$ is not exact.

So the line integral identifies $H^1(S^1)$ with $\mathbb{R}$: $\mathcal{S}(\alpha)$ is the Calculus III line integral $\int_{S^1}\alpha$ of Example [[§83 The First Cohomology of the Circle#^ex-83-2|§83.2]](3). The computation is an instance of a general theorem, stated now and proved once orientations are defined and top-degree forms can be integrated over compact oriented manifolds.

> [!theorem] Theorem §83.5: Top-Degree Cohomology
> *(Stated in Lecture 33; to be proved.)* Let $M$ be a compact, oriented, connected smooth manifold of dimension $m$. Then integration induces an isomorphism
>
> $$
> \int_M : H^m(M) \xrightarrow{\ \cong\ } \mathbb{R} .
> $$
>
> In particular $b_m(M) = 1$.
>
> *Lee: Theorem 17.31*

^thm-83-5

> [!proof]+ Proof (to be filled)
> Stated in Lecture 33 without proof. It needs orientations and the integral of an $m$-form over a compact oriented manifold, which come later in the course (Lee, Theorem 17.31).

^pf-83-5

> [!remark]- Connections
> - That exact forms integrate to zero is Stokes' theorem on a manifold without boundary; the Calculus III case: [[§73 Stokes' Theorem in Calculus III|§73]].

For $S^1$ (compact, connected, and oriented by $d\theta$), this is Proposition [[§83 The First Cohomology of the Circle#^prop-83-4|§83.4]], done by hand. The torus is more interesting, with both an $H^1$ and an $H^2$.
