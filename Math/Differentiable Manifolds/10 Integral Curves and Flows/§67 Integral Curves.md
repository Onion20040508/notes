---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 67
tags: [differentiable-manifolds, math591]
---
← [[§66 Partitions of Unity]] · ↑ [[· 10 Integral Curves and Flows]] · [[§68 Local Existence and Uniqueness]] →

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

“This is the key notion. You might have seen this in your ordinary differential equations.”

> [!theorem] Proposition §67.1: The Velocity Curve
> Let $c : I \to M$ be a smooth curve. Then $\dot c : I \to TM$, $t \mapsto \dot c(t)$, is a smooth curve in $TM$ lying over $c$, that is, $\pi \circ \dot c = c$. A smooth curve $c$ is an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$ if and only if $\dot c = \mathbf{X} \circ c$ as maps $I \to TM$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves; Ch. 9, Integral Curves*

^prop-67-1

> [!proof]+ Proof
> *(Not from lecture; added from a question: “how is $\dot c$ defined, when $M$ is a general manifold?”)* *Over $c$.* $\dot c(t) \in T_{c(t)}M$ by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]], so $\pi(\dot c(t)) = c(t)$ (Definition [[§51 The Tangent Bundle#^def-51-2|§51.2]]).
>
> *Smooth.* Let $t_0 \in I$ and $(U, \varphi = (x^1, \ldots, x^m))$ a chart at $c(t_0)$; on the open interval $I_0 = c^{-1}(U) \ni t_0$, $\dot c$ takes values in $TU$. In the chart $\tilde\varphi$ of $TM$ over $U$ (Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]]), whose last $m$ entries are the components in the coordinate basis, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]] gives
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

The angle brackets mark $\dot c$ as a vector, not a point: “I've been trained … that you should distinguish vectors from points.” What the proposition shows is that $(\ast)$ is a *system of first-order ODEs*, usually nonlinear. All the derivatives are on the left-hand side, solved for: the right-hand side involves no derivatives. And it is a genuine *system*, because the equation for $\dot x^i$ involves, in principle, all of the $x$'s. (Lee: solving a system of ODEs is called “integrating” it, hence the name *integral* curve.)

> [!remark] Remark: Why an Integral Curve Is an ODE
> *(Not from lecture; added from a question: “how did integral curves suddenly connect to ODEs?”)* The definition is already an ODE, written without coordinates. In $(\ast)$ the unknown is the curve $c$; its derivative is set equal to something that depends on where $c$ currently is: “the velocity at time $t$ is the arrow that $\mathbf{X}$ puts at the point where $c$ is at time $t$.” The derivative of the unknown equals a known function of the unknown — that is an ODE. Proposition [[§67 Integral Curves#^prop-67-2|§67.2]] only unpacks it into components.
> - *The simplest example.* On $\mathbb{R}$, $\mathbf{X} = x\, \frac{d}{dx}$: the equation is $\dot x = x$, so $x(t) = x_0 e^t$. The point runs away from $0$ faster and faster, because the arrows get longer further out.
> - *Conversely*, every autonomous system $\dot x^i = f^i(x)$ with smooth $f^i$ on an open $U \subseteq \mathbb{R}^m$ is the system of the field $\sum_i f^i\, \partial/\partial x^i$: autonomous first-order systems on $U$ and vector fields on $U$ are the same thing. (“Autonomous”: the right-hand side does not depend on $t$, as the field does not change in time.)
> - *Higher order.* $\ddot x = -x$ becomes, with $y = \dot x$, the first-order system $\dot x = y$, $\dot y = -x$, the field $y\, \partial_x - x\, \partial_y$ — minus the rotation field of Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]], whose integral curves it runs backwards in time. The harmonic oscillator is “follow this field in the phase plane”; likewise Hamilton's equations, for a time-independent Hamiltonian, say that the motion follows the integral curves of one vector field on phase space.
> - *Local versus global.* On a manifold a chart turns $(\ast)$ into such a system, so the local questions — existence, uniqueness, smooth dependence on the starting point — reduce to ODE theory in $\mathbb{R}^m$; this is why Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]] is quoted in its Euclidean form. What one chart cannot settle is how far a solution continues: solutions in different charts must be patched together, and a solution may escape in finite time, which already happens in $\mathbb{R}^2$ (Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]). That is the content of Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]].

^rem-67-1

*Lecture 24 recalled the definition with the velocity written “in a fancy way”, $\dot c(t) = c_{\ast t}(d/dt)$, “the derivation at $c(t)$ defined by $c$” (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]), and gave the velocity curve a name: “to any curve $c : I \to M$ one can naturally associate a lift” to the tangent bundle.*

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

> [!theorem] Proposition §67.3: An Integral Curve Returns with the Same Velocity
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$. If $c(t_1) = c(t_2)$ for some $t_1, t_2 \in I$, then $\dot c(t_1) = \dot c(t_2)$. Hence a smooth curve that passes through a point twice with different velocities is an integral curve of no vector field.
>
> *Lee: Ch. 9, Integral Curves*

^prop-67-3

> [!proof]+ Proof
> *(Lecture 24: “the field is single-valued at each point.”)* By $(\ast)$ at the times $t_1$ and $t_2$, and since $c(t_1) = c(t_2)$,
>
> $$
> \dot c(t_1) = \mathbf{X}_{c(t_1)} = \mathbf{X}_{c(t_2)} = \dot c(t_2) .
> $$
>
> The second sentence is the contrapositive: if $c(t_1) = c(t_2)$ but $\dot c(t_1) \neq \dot c(t_2)$, no vector field $\mathbf{X}$ satisfies $(\ast)$ at both times.

^pf-67-3

> [!example] Example §67.1: A Curve with a Loop
> Let $c : I \to M$ pass through the same point at two times, $c(t_1) = c(t_2)$, with different velocities $\dot c(t_1) \neq \dot c(t_2)$, as in the figure. Its lift $\tilde c$ is still a well-defined map: it records the time, not just the point. “But this cannot be an integral curve of anything” (Proposition [[§67 Integral Curves#^prop-67-3|§67.3]]).

^ex-67-1

![[m591-67-4.svg]]

*Simple and useful lemmas,* (Lecture 24) for any $\mathbf{X} \in \mathfrak{X}(M)$, “completely general.”

> [!theorem] Lemma §67.4: Translation and Rescaling
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. *(Translation lemma.)* For $t_0 \in \mathbb{R}$, the curve $\tilde c(t) = c(t + t_0)$, defined on $I - t_0 = \{ t - t_0 : t \in I \}$, is an integral curve of $\mathbf{X}$.
> 2. *(Rescaling.)* For $\lambda \in \mathbb{R}$, the curve $\tilde c(t) = c(\lambda t)$, defined on $\{ t : \lambda t \in I \}$, is an integral curve of $\lambda\mathbf{X}$.
>
> *Lee: Lemmas 9.3 and 9.4*

^lem-67-4

> [!proof]+ Proof
> *(Lecture 24: “immediate by chain rule”; filled in.)* Both domains are open intervals (for $\lambda = 0$ the second is all of $\mathbb{R}$). Fix $t$ in the domain and a germ $f$ at $\tilde c(t)$; by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]] and the chain rule for real functions of one variable:
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

“You can always translate time. We're going to use it a lot.” Rescaling: “you can rescale a field pointwise by a fixed factor, and the integral curves of that are easily related to the integral curves of the original.” With $\lambda = -1$: the integral curves of $-\mathbf{X}$ are those of $\mathbf{X}$ run backwards.

![[m591-67-8.svg]]

*(Not from lecture; figure added.)* Both operations keep the image of the curve and change only the clock. Translation relabels the times, so the point reached at time $t_0$ by $c$ is reached at time $0$ by $\tilde c$; the arrow (the velocity) is unchanged. Rescaling by $\lambda = -1$ reverses the arrow, which is why $\tilde c$ follows $-\mathbf{X}$. (A general $\lambda$ also changes the speed by the factor $|\lambda|$.)

> [!theorem] Lemma §67.5: Integral Curves Under a Diffeomorphism
> Let $F : M \to N$ be a diffeomorphism, $\mathbf{X} \in \mathfrak{X}(M)$, and $F_\ast\mathbf{X} \in \mathfrak{X}(N)$ its pushforward (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]). A smooth curve $c : I \to M$ is an integral curve of $\mathbf{X}$ if and only if $F \circ c$ is an integral curve of $F_\ast\mathbf{X}$.
>
> *Lee: Proposition 9.6*

^lem-67-5

> [!proof]+ Proof
> *(Lecture 24: “the check” in the proof of Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]], there for a chart; written here for any diffeomorphism.)* $F \circ c$ is smooth, as a composite of smooth maps. Fix $t \in I$. By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), the velocity of $F \circ c$ at $t$ is
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

*Uses:* [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]]

“This is a kind of naturality that I will come back to, because this is very general.” (Lee, Proposition 9.6: a smooth $F$ takes integral curves of $\mathbf{X}$ to integral curves of $\mathbf{Y}$ for all integral curves exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.)
