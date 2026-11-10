---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 67
tags: [differentiable-manifolds, math591]
---
← [[§66 The Whitney Embedding Theorem]] · ↑ [[· 10 Integral Curves and Flows]] · [[§68 Local Existence and Uniqueness]] →

*Stage: dynamics — Curves whose velocity is prescribed by a vector field; in coordinates, a first-order system of ODEs.*

The velocity of a curve at a time $t$, from [[§31 Tangent Vectors as Velocities of Curves|§31]]:

![[§31 Tangent Vectors as Velocities of Curves#^def-31-3]]

![[§31 Tangent Vectors as Velocities of Curves#^cor-31-2]]

In this chapter curves are mostly called $c : I \to M$, with velocity $\dot c(t)$; the corollary is the board's $\dot c = \langle \dot x^1, \ldots, \dot x^m \rangle$.

> [!definition] Definition §67.1: Integral Curve
> Let $\mathbf{X} \in \mathfrak{X}(M)$. An **integral curve** of $\mathbf{X}$ is a smooth map $c : I \to M$, where $I = (a, b) \subseteq \mathbb{R}$ is an open interval (possibly $a = -\infty$ or $b = +\infty$), such that
>
> $$
> \dot c(t) = \mathbf{X}_{c(t)} \qquad \text{for all } t \in I. \tag{$\ast$}
> $$
>
> The variable $t$ is called **time**. If $0 \in I$ and $c(0) = q$, the curve **starts at** $q$.
>
> *Lee: Ch. 9, Integral Curves*

^def-67-1

![[m591-67-a7.gif|420]]

*(Not from lecture; animation added, vault only.)* Integral curves on a surface in $\mathbb{R}^3$: $\mathbf{X}_p = e_3 - \langle e_3, p\rangle p$, the tangential part of the vertical, on $S^2$ (chosen for the picture; green arrows: $\mathbf{X}$ at the moving points). Points start near the south pole and climb their meridians toward the north pole; both poles are zeros of $\mathbf{X}$ and stay fixed.

This is the key notion of the chapter, familiar from ordinary differential equations (Proposition [[§67 Integral Curves#^prop-67-2|§67.2]]).

> [!theorem] Proposition §67.1: The Velocity Curve
> Let $c : I \to M$ be a smooth curve. Then $\dot c : I \to TM$, $t \mapsto \dot c(t)$, is a smooth curve in $TM$ lying over $c$, that is, $\pi \circ \dot c = c$. A smooth curve $c$ is an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$ if and only if $\dot c = \mathbf{X} \circ c$ as maps $I \to TM$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves; Ch. 9, Integral Curves*

^prop-67-1

> [!proof]+ Proof
> *(Not from lecture; added to answer how $\dot c$ is defined when $M$ is a general manifold.)* *Over $c$.* $\dot c(t) \in T_{c(t)}M$ by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]], so $\pi(\dot c(t)) = c(t)$ (Definition [[§51 The Tangent Bundle#^def-51-2|§51.2]]).
>
> *Smooth.* Let $t_0 \in I$ and $(U, \varphi = (x^1, \ldots, x^m))$ a chart at $c(t_0)$; on the open set $I_0 = c^{-1}(U) \ni t_0$, $\dot c$ takes values in $TU$. In the chart $\tilde\varphi$ of $TM$ over $U$ (Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]]), whose last $m$ entries are the components in the coordinate basis, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]] gives
>
> $$
> \tilde\varphi\big(\dot c(t)\big) = \Big(x^1(c(t)), \ldots, x^m(c(t)),\ (x^1 \circ c)'(t), \ldots, (x^m \circ c)'(t)\Big), \qquad t \in I_0 ,
> $$
>
> smooth in $t$ because each $x^j \circ c$ is a smooth real function. So $\dot c$ is smooth near every $t_0$.
>
> *The integral-curve equation.* Both $\dot c(t)$ and $\mathbf{X}_{c(t)} = (\mathbf{X} \circ c)(t)$ lie in $T_{c(t)}M$, so $(\ast)$ compares two vectors in the same tangent space, for each $t$; and $(\ast)$ for all $t \in I$ says exactly that the maps $\dot c$ and $\mathbf{X} \circ c$ from $I$ to $TM$ are equal.

^pf-67-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]], [[§51 The Tangent Bundle#^def-51-2|Def. §51.2]], [[§51 The Tangent Bundle#^def-51-5|Def. §51.5]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]]

So an integral curve is a curve whose velocity curve in $TM$ is the field read along the curve. For a curve in a regular level set $M \subseteq \mathbb{R}^N$, the velocity $\dot c(t)$ is the ordinary derivative $c'(t)$, seen as the derivation $D_{c'(t)}$ (Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-3|§31.3]]).

> [!theorem] Proposition §67.2: Integral Curves in Coordinates
> Let $M \subseteq \mathbb{R}^m$ be open, with coordinates $x^1, \ldots, x^m$, and $\mathbf{X} = \sum_i f^i\, \partial/\partial x^i$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). Write a smooth curve as $c(t) = (x^1(t), \ldots, x^m(t))$, with velocity $\dot c(t) = \langle \dot x^1(t), \ldots, \dot x^m(t) \rangle$. Then $c$ is an integral curve of $\mathbf{X}$ if and only if
>
> $$
> \dot x^i(t) = f^i\big(x^1(t), \ldots, x^m(t)\big) \qquad \text{for all } i = 1, \ldots, m \text{ and all } t \in I .
> $$
>
> The same holds on any manifold, in any chart, with the $x^i(t)$ the coordinates of $c(t)$.
>
> *Lee: Ch. 9, Integral Curves, (9.1)*

^prop-67-2

> [!proof]+ Proof
> By Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], applied at each time $t$ to the shifted curve $s \mapsto c(t + s)$, $\dot c(t) = \sum_i \dot x^i(t)\, \partial/\partial x^i|_{c(t)}$, while $\mathbf{X}_{c(t)} = \sum_i f^i(c(t))\, \partial/\partial x^i|_{c(t)}$. The $\partial/\partial x^i|_{c(t)}$ form a basis of $T_{c(t)}M$, so $(\ast)$ holds at $t$ exactly when the components agree. The argument uses only a chart, so it applies on any manifold.

^pf-67-2

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]

The angle brackets mark $\dot c$ as a vector, not a point, to keep vectors and points distinct. What the proposition shows is that $(\ast)$ is a *system of first-order ODEs*, usually nonlinear. All the derivatives are on the left-hand side, solved for: the right-hand side involves no derivatives. And it is a genuine *system*, because the equation for $\dot x^i$ involves, in principle, all of the $x$'s. (Lee: solving a system of ODEs is called “integrating” it, hence the name *integral* curve.)

> [!remark] Remark: Why an Integral Curve Is an ODE
> *(Not from lecture; added to answer how integral curves connect to ODEs.)* The definition is already an ODE, written without coordinates. In $(\ast)$ the unknown is the curve $c$; its derivative is set equal to something that depends on where $c$ currently is: the velocity at time $t$ is the arrow that $\mathbf{X}$ puts at the point where $c$ is at time $t$. The derivative of the unknown equals a known function of the unknown — that is an ODE. Proposition [[§67 Integral Curves#^prop-67-2|§67.2]] only unpacks it into components.
> - *The simplest example* is the field $x\, \frac{d}{dx}$ on $\mathbb{R}$, with the equation $\dot x = x$ (Example [[§67 Integral Curves#^ex-67-1|§67.1]] below).
> - *Conversely*, every autonomous system $\dot x^i = f^i(x)$ with smooth $f^i$ on an open $U \subseteq \mathbb{R}^m$ is the system of the field $\sum_i f^i\, \partial/\partial x^i$: autonomous first-order systems on $U$ and vector fields on $U$ are the same thing. (“Autonomous”: the right-hand side does not depend on $t$, as the field does not change in time.)
> - *Higher order.* A higher-order equation becomes a first-order system once the lower derivatives are taken as new unknowns; the harmonic oscillator $\ddot x = -x$ becomes “follow this field in the phase plane” (Example [[§67 Integral Curves#^ex-67-2|§67.2]] below). Likewise Hamilton's equations, for a time-independent Hamiltonian, say that the motion follows the integral curves of one vector field on phase space.
> - *Local versus global.* On a manifold a chart turns $(\ast)$ into such a system, so the local questions — existence, uniqueness, smooth dependence on the starting point — reduce to ODE theory in $\mathbb{R}^m$; this is why Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]] is quoted in its Euclidean form. What one chart cannot settle is how far a solution continues: solutions in different charts must be patched together, and a solution may escape in finite time, which already happens in $\mathbb{R}^2$ (Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]). That is the content of Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]].

^rem-67-1

> [!example] Example §67.1: The Field $x\,d/dx$ on the Line
> *(Not from lecture.)* On $\mathbb{R}$, let $\mathbf{X} = x\, \frac{d}{dx}$. The integral curve starting at $x_0$ is $x(t) = x_0 e^t$, $t \in \mathbb{R}$. The point runs away from $0$ faster and faster, because the arrows get longer further out.
>
> *The equation.* By Proposition [[§67 Integral Curves#^prop-67-2|§67.2]], with $m = 1$ and $f^1(x) = x$, a curve $t \mapsto x(t)$ is an integral curve of $\mathbf{X}$ if and only if $\dot x = x$.
>
> *A solution.* $x(t) = x_0e^t$ has $\dot x(t) = x_0e^t = x(t)$ and $x(0) = x_0$.
>
> *The only one.* If $x$ solves $\dot x = x$ on an interval containing $0$ with $x(0) = x_0$, then $\frac{d}{dt}\big(e^{-t}x(t)\big) = e^{-t}(\dot x(t) - x(t)) = 0$, so $e^{-t}x(t) = x_0$, that is, $x(t) = x_0e^t$.
>
> *Running away.* For $x_0 \neq 0$ the speed is $|\dot x(t)| = |x(t)| = |x_0|e^t$: it equals the distance from $0$, which grows exponentially. For $x_0 = 0$ the curve is constant, at the zero of $\mathbf{X}$.

^ex-67-1

> [!example] Example §67.2: The Harmonic Oscillator as a Vector Field
> *(Not from lecture.)* The equation $\ddot x = -x$ becomes, with $y = \dot x$, the first-order system $\dot x = y$, $\dot y = -x$, the system of the field $\mathbf{Y} = y\, \partial_x - x\, \partial_y$ on $\mathbb{R}^2$. Its integral curves are the circles about the origin, run clockwise, and the constant curve at the origin: $\mathbf{Y}$ is minus the rotation field of Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]] (later), whose integral curves it runs backwards in time.
>
> *The reduction.* If $\ddot x = -x$, put $y = \dot x$; then $\dot x = y$ and $\dot y = \ddot x = -x$. Conversely, if $(x, y)$ solves the system, then $\ddot x = \dot y = -x$. By Proposition [[§67 Integral Curves#^prop-67-2|§67.2]], with $f^1(x, y) = y$ and $f^2(x, y) = -x$, the system says exactly that $t \mapsto (x(t), y(t))$ is an integral curve of $\mathbf{Y}$.
>
> *The integral curves.* The curve $c(t) = \big(x_0\cos t + y_0\sin t,\ -x_0\sin t + y_0\cos t\big)$ starts at $(x_0, y_0)$, and $\dot x = -x_0\sin t + y_0\cos t = y$, $\dot y = -x_0\cos t - y_0\sin t = -x$; so it is the integral curve starting at $(x_0, y_0)$. It is the point $(x_0, y_0)$ rotated by the angle $-t$, so $x(t)^2 + y(t)^2 = x_0^2 + y_0^2$: for $(x_0, y_0) \neq 0$ it runs around the circle of that radius clockwise, and for $(x_0, y_0) = 0$ it is constant.
>
> *Minus the rotation field.* $\mathbf{Y} = -\big(-y\, \partial_x + x\, \partial_y\big)$, and $c(t)$ is the rotation of $(x_0, y_0)$ by $-t$, the integral curve of the rotation field through $(x_0, y_0)$ at time $-t$.

^ex-67-2

*Lecture 24 recalled the definition with the velocity written as $\dot c(t) = c_{\ast t}(d/dt)$, the derivation at $c(t)$ defined by $c$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]), and gave the velocity curve a name: every curve $c : I \to M$ has a natural lift to the tangent bundle.*

> [!definition] Definition §67.2: Lift of a Curve
> Let $c : I \to M$ be a smooth curve. Its **lift** to the tangent bundle is the curve
>
> $$
> \tilde c : I \to TM, \qquad \tilde c(t) = \big(c(t), \dot c(t)\big),
> $$
>
> the point $c(t)$ together with the velocity $\dot c(t) \in T_{c(t)}M$. It is the velocity curve $\dot c$ of Proposition [[§67 Integral Curves#^prop-67-1|§67.1]], so it is smooth and $\pi \circ \tilde c = c$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^def-67-2

![[m591-67-11.svg]]

The lift exists for every smooth curve, injective or not. By Proposition [[§67 Integral Curves#^prop-67-1|§67.1]], $c$ is an integral curve of $\mathbf{X}$ exactly when $\tilde c = \mathbf{X} \circ c$: the lift is the field along the curve.

![[m591-67-a5.gif|420]]

*(Not from lecture; animation added, vault only.)* The lift in the tangent bundle, for the field $(0.55 + 0.35\sin\theta)\,\partial/\partial\theta$ of Definition [[§56 Vector Fields#^def-56-1|§56.1]]'s figure on $S^1$, with $TS^1$ drawn as a cylinder. The integral curve $c(t)$ (blue, with its velocity arrow) runs around the circle, faster where the coefficient $0.55 + 0.35\sin\theta$ is larger. Its lift $\tilde c(t) = (c(t), \dot c(t))$ (red) runs along the section $\mathbf{X}(S^1)$ (green), as Proposition §67.1 says. One turn takes $2\pi/\sqrt{0.55^2 - 0.35^2} = 14.81$.

> [!theorem] Proposition §67.3: An Integral Curve Returns with the Same Velocity
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$. If $c(t_1) = c(t_2)$ for some $t_1, t_2 \in I$, then $\dot c(t_1) = \dot c(t_2)$. Hence a smooth curve that passes through a point twice with different velocities is an integral curve of no vector field.
>
> *Lee: Ch. 9, Integral Curves*

^prop-67-3

> [!proof]+ Proof
> *(Lecture 24. The point is that the field has a single value at each point.)* By $(\ast)$ at the times $t_1$ and $t_2$, and since $c(t_1) = c(t_2)$,
>
> $$
> \dot c(t_1) = \mathbf{X}_{c(t_1)} = \mathbf{X}_{c(t_2)} = \dot c(t_2) .
> $$
>
> The second sentence is the contrapositive: if $c(t_1) = c(t_2)$ but $\dot c(t_1) \neq \dot c(t_2)$, no vector field $\mathbf{X}$ satisfies $(\ast)$ at both times.

^pf-67-3

![[m591-67-12.svg]]

*(Not from lecture; figure added.)* Proposition [[§67 Integral Curves#^prop-67-3|§67.3]] in the tangent bundle, for $M = \mathbb{R}$, where $TM = \mathbb{R} \times \mathbb{R}$ is a plane: the base point horizontally, and the fibre $T_xM$, the velocities at $x$, as the vertical line over $x$. A vector field is a section $x \mapsto (x, \mathbf{X}_x)$, so its image is a graph, which meets each fibre exactly once, and the lift of an integral curve lies on it ($\tilde c = \mathbf{X} \circ c$, Proposition [[§67 Integral Curves#^prop-67-1|§67.1]]). The curve $c(t) = t^2 - 1$ passes through $0$ at $t = -1$, moving left, and at $t = 1$, moving right. Its lift $\tilde c(t) = (t^2 - 1, 2t)$ meets the fibre $T_0M$ in the two points $(0, -2)$ and $(0, 2)$, and no graph contains both. So $c$ is an integral curve of no vector field.

> [!example] Example §67.3: A Curve with a Loop
> Let $c : I \to M$ pass through the same point at two times, $c(t_1) = c(t_2)$, with different velocities $\dot c(t_1) \neq \dot c(t_2)$, as in the figure. Its lift $\tilde c$ is still a well-defined map: it records the time, not just the point. But $c$ is an integral curve of no vector field (Proposition [[§67 Integral Curves#^prop-67-3|§67.3]]).

^ex-67-3

![[m591-67-4.svg]]

![[m591-67-13.svg]]

*(Not from lecture; figure added.)* A loop in the tangent bundle: $c(t) = (t^2 - 1, t^3 - t)$ in $M = \mathbb{R}^2$ passes through the origin at $t = -1$ and at $t = 1$, with velocities $\dot c(\mp 1) = (\mp 2, 2)$. Here $TM = \mathbb{R}^2 \times \mathbb{R}^2$ is four-dimensional; the figure keeps the point $c(t)$ (the grey floor) and, as height, only the direction of $\dot c(t)$, its angle, forgetting the speed (the angle is unrolled: $\theta$ and $\theta + 2\pi$ are the same direction). Over the crossing point the lift passes at two heights, $135^\circ$ and $45^\circ$. In $TM$ the two visits are different points of the same fibre, and the lift does not cross itself; a vector field would put only one point in that fibre.

![[m591-67-a3.gif|440]]

*(Not from lecture; animation added, vault only.)* The same picture turning, so that its depth is visible: the grey loop lies in $M$, the blue lift lies over it at the height of the direction of $\dot c$, and the red dashed fibre over the crossing point meets the lift twice, at $135^\circ$ and $45^\circ$. Seen from the side, the two branches of the lift are clearly apart.

*Simple and useful lemmas* (Lecture 24), valid for any $\mathbf{X} \in \mathfrak{X}(M)$.

> [!theorem] Lemma §67.4: Translation and Rescaling
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. *(Translation lemma.)* For $t_0 \in \mathbb{R}$, the curve $\tilde c(t) = c(t + t_0)$, defined on $I - t_0 = \{ t - t_0 : t \in I \}$, is an integral curve of $\mathbf{X}$.
> 2. *(Rescaling.)* For $\lambda \in \mathbb{R}$, the curve $\tilde c(t) = c(\lambda t)$, defined on $\{ t : \lambda t \in I \}$, is an integral curve of $\lambda\mathbf{X}$.
>
> *Lee: Lemmas 9.3 and 9.4*

^lem-67-4

> [!proof]+ Proof
> *(Lecture 24: immediate from the chain rule; filled in.)* Both domains are open intervals (for $\lambda = 0$ the second is all of $\mathbb{R}$ if $0 \in I$, and empty if $0 \notin I$, when there is nothing to prove). Fix $t$ in the domain and a germ $f$ at $\tilde c(t)$; by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]] and the chain rule for real functions of one variable:
>
> $$
> \dot{\tilde c}(t)[f] = \frac{d}{dt} f\big(c(t + t_0)\big) = (f \circ c)'(t + t_0) = \dot c(t + t_0)[f] = \mathbf{X}_{c(t + t_0)}[f] = \mathbf{X}_{\tilde c(t)}[f]
> $$
>
> for (1), and for (2)
>
> $$
> \dot{\tilde c}(t)[f] = \frac{d}{dt} f\big(c(\lambda t)\big) = \lambda\, (f \circ c)'(\lambda t) = \lambda\, \dot c(\lambda t)[f] = \lambda\, \mathbf{X}_{c(\lambda t)}[f] = (\lambda\mathbf{X})_{\tilde c(t)}[f] .
> $$
>
> Two tangent vectors at a point that agree on every germ are equal.

^pf-67-4

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]]

Time can always be translated, and this is used often below. Rescaling a field pointwise by a fixed factor gives integral curves simply related to those of the original field. With $\lambda = -1$: the integral curves of $-\mathbf{X}$ are those of $\mathbf{X}$ run backwards.

![[m591-67-8.svg]]

*(Not from lecture; figure added.)* Both operations keep the image of the curve and change only the clock. Translation relabels the times, so the point reached at time $t_0$ by $c$ is reached at time $0$ by $\tilde c$; the arrow (the velocity) is unchanged. Rescaling by $\lambda = -1$ reverses the arrow, which is why $\tilde c$ follows $-\mathbf{X}$. (A general $\lambda$ also changes the speed by the factor $|\lambda|$.)

> [!theorem] Lemma §67.5: Integral Curves Under a Diffeomorphism
> Let $F : M \to N$ be a diffeomorphism, $\mathbf{X} \in \mathfrak{X}(M)$, and $F_\ast\mathbf{X} \in \mathfrak{X}(N)$ its pushforward (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]). A smooth curve $c : I \to M$ is an integral curve of $\mathbf{X}$ if and only if $F \circ c$ is an integral curve of $F_\ast\mathbf{X}$.
>
> *Lee: Proposition 9.6*

^lem-67-5

> [!proof]+ Proof
> *(Lecture 24: the verification step in the proof of Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]], there for a chart; written here for any diffeomorphism.)* $F \circ c$ is smooth, as a composite of smooth maps. Fix $t \in I$. By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), the velocity of $F \circ c$ at $t$ is
>
> $$
> (F \circ c)_{\ast t}\Big(\frac{d}{dt}\Big) = dF_{c(t)}\Big(c_{\ast t}\Big(\frac{d}{dt}\Big)\Big) = dF_{c(t)}\big(\dot c(t)\big),
> $$
>
> and by Definition [[§59 Related Vector Fields#^def-59-1|§59.1]] at the point $F(c(t))$, whose preimage is $c(t)$,
>
> $$
> (F_\ast\mathbf{X})_{F(c(t))} = dF_{c(t)}\big(\mathbf{X}_{c(t)}\big) .
> $$
>
> The linear map $dF_{c(t)}$ is injective: by the chain rule, $d(F^{-1})_{F(c(t))} \circ dF_{c(t)} = d(F^{-1} \circ F)_{c(t)}$ is the identity. So the two vectors above agree exactly when $\dot c(t) = \mathbf{X}_{c(t)}$: $F \circ c$ satisfies the integral-curve equation of $F_\ast\mathbf{X}$ at $t$ if and only if $c$ satisfies that of $\mathbf{X}$ at $t$.

^pf-67-5

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]]

This is a kind of naturality that recurs later in greater generality (Proposition [[§70 Complete Vector Fields#^prop-70-10|§70.10]]; Lee, Proposition 9.6: a smooth $F$ takes integral curves of $\mathbf{X}$ to integral curves of $\mathbf{Y}$ for all integral curves exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.)
