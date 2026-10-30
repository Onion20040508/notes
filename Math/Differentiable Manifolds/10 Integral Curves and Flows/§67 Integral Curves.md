---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 67
tags: [differentiable-manifolds, math591]
---
← [[§66 Partitions of Unity]] · ↑ [[· 10 Integral Curves and Flows]] · [[§68 Flows]] →

*Stage: dynamics — Curves whose velocity is prescribed by a vector field; in coordinates, a first-order system of ODEs.*

The velocity of a curve at a time $t$, from [[§31 Tangent Vectors as Velocities of Curves|§31]]:

![[§31 Tangent Vectors as Velocities of Curves#^def-31-3]]

![[§31 Tangent Vectors as Velocities of Curves#^cor-31-2]]

In this chapter curves are mostly called $c : I \to M$, with velocity $\dot c(t)$; the corollary is the board's $\dot c = \langle \dot x^1, \ldots , \dot x^m \rangle$.

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
> *Smooth.* Let $t_0 \in I$ and $(U, \varphi = (x^1, \ldots , x^m))$ a chart at $c(t_0)$; on the open interval $I_0 = c^{-1}(U) \ni t_0$, $\dot c$ takes values in $TU$. In the chart $\tilde\varphi$ of $TM$ over $U$ (Definition [[§51 The Tangent Bundle#^def-51-5|§51.5]]), whose last $m$ entries are the components in the coordinate basis, Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]] gives
>
> $$
> \tilde\varphi\big(\dot c(t)\big) = \Big(x^1(c(t)), … , x^m(c(t)),\ (x^1 \circ c)'(t), … , (x^m \circ c)'(t)\Big), \qquad t \in I_0 ,
> $$
>
> smooth in $t$ because each $x^j \circ c$ is a smooth real function. So $\dot c$ is smooth near every $t_0$.
>
> *The integral-curve equation.* Both $\dot c(t)$ and $\mathbf{X}_{c(t)} = (\mathbf{X} \circ c)(t)$ lie in $T_{c(t)}M$, so $(\ast)$ compares two vectors in the same tangent space, for each $t$; and $(\ast)$ for all $t \in I$ says exactly that the maps $\dot c$ and $\mathbf{X} \circ c$ from $I$ to $TM$ are equal.

^pf-67-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]], [[§51 The Tangent Bundle#^def-51-2|Def. §51.2]], [[§51 The Tangent Bundle#^def-51-5|Def. §51.5]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-2|§31.2]]

So an integral curve is a curve whose velocity curve in $TM$ is the field read along the curve. For a curve in a regular level set $M \subseteq \mathbb{R}^N$, the velocity $\dot c(t)$ is the ordinary derivative $c'(t)$, seen as the derivation $D_{c'(t)}$ (Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-3|§31.3]]).

> [!theorem] Proposition §67.2: Integral Curves in Coordinates
> Let $M \subseteq \mathbb{R}^m$ be open, with coordinates $x^1, \ldots , x^m$, and $\mathbf{X} = \sum_i f^i\, \partial/\partial x^i$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). Write a smooth curve as $c(t) = (x^1(t), \ldots , x^m(t))$, with velocity $\dot c(t) = \langle \dot x^1(t), \ldots , \dot x^m(t) \rangle$. Then $c$ is an integral curve of $\mathbf{X}$ if and only if
>
> $$
> \dot x^i(t) = f^i\big(x^1(t), … , x^m(t)\big) \qquad \text{for all } i = 1, … , m \text{ and all } t \in I .
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
> - *Higher order.* $\ddot x = -x$ becomes, with $y = \dot x$, the first-order system $\dot x = y$, $\dot y = -x$, the field $y\, \partial_x - x\, \partial_y$ — minus the rotation field of Example [[§67 Integral Curves#^ex-67-1|§67.1]], whose integral curves it runs backwards in time. The harmonic oscillator is “follow this field in the phase plane”; likewise Hamilton's equations, for a time-independent Hamiltonian, say that the motion follows the integral curves of one vector field on phase space.
> - *Local versus global.* On a manifold a chart turns $(\ast)$ into such a system, so the local questions — existence, uniqueness, smooth dependence on the starting point — reduce to ODE theory in $\mathbb{R}^m$; this is why Theorem [[§67 Integral Curves#^thm-67-3|§67.3]] is quoted in its Euclidean form. What one chart cannot settle is how far a solution continues: solutions in different charts must be patched together, and a solution may escape in finite time, which already happens in $\mathbb{R}^2$ (Example [[§67 Integral Curves#^ex-67-2|§67.2]]). That is the content of Theorem [[§68 Flows#^thm-68-1|§68.1]].

^rem-67-1

“There's a fundamental theorem that, again, from — we have moved from Calc 3 to Calc 4 — ODEs.” Uribe quoted it in the following form.

> [!theorem] Theorem §67.3: Local Existence and Uniqueness
> Let $M \subseteq \mathbb{R}^m$ be open and $\mathbf{X} \in \mathfrak{X}(M)$. Given any $p \in M$, there are $\varepsilon > 0$, an open neighbourhood $U \subseteq M$ of $p$, and a smooth map
>
> $$
> \varphi : (-\varepsilon, \varepsilon) \times U \longrightarrow M
> $$
>
> such that
>
> 1. $\varphi(0, q) = q$ for every $q \in U$;
> 2. for every $q \in U$, the curve $(-\varepsilon, \varepsilon) \to M$, $t \mapsto \varphi(t, q)$, is an integral curve of $\mathbf{X}$;
> 3. *(uniqueness)* if $q \in U$ and $c : I \to M$ is any integral curve of $\mathbf{X}$ with $0 \in I$ and $c(0) = q$, then
>
> $$
> c|_{I \cap (-\varepsilon, \varepsilon)} = \varphi(\cdot, q)|_{I \cap (-\varepsilon, \varepsilon)} .
> $$
>
> *Lee: Theorem D.1*

^thm-67-3

> [!proof]+ Proof (not given in this course)
> Taken from ODE theory, not proved in the course: “a big, big theorem that takes forever to prove”, the theorem on existence, uniqueness and smooth dependence on initial conditions (Lee, Theorem D.1, proved in Appendix D). “This theorem here packs everything that we will quote from the Euclidean case.”

^pf-67-3

Items (1) and (2) together are *existence*: every $q \in U$ has an integral curve $\varphi(\cdot, q)$ starting at $q$, all defined on the same interval $(-\varepsilon, \varepsilon)$; the smoothness of $\varphi$ in the pair $(t, q)$ is *smooth dependence on the initial condition*. Item (3) is *uniqueness*, on a par with existence; on the board it came as an addition, “Furthermore (still the Euclidean theorem).”

![[m591-67-1.svg]]

“Imagine a Calc 3 plot of a field … the vectors at every point.” The theorem gives a time interval $(-\varepsilon, \varepsilon)$ and a neighbourhood $U$ of $p$ (drawn as a rectangle) such that from every point $q \in U$, $p$ included, there is an integral curve $t \mapsto \varphi(t, q)$ that starts at $q$ and is defined at least for $|t| < \varepsilon$.

*What the theorem says beyond “there is a path through $q$”* (a student's question). “It says a lot of delicate things.” The time interval is *uniform*: as long as $q \in U$, the curve is defined at least for $|t| < \varepsilon$. And $\varphi$ is smooth as a function of the pair $(t, q)$ on the product $(-\varepsilon, \varepsilon) \times U$: smooth in $t$, as an integral curve must be, but also, for fixed $t$, smooth in the initial condition $q$. Asked whether the image of $\varphi$ is “just a slightly bigger open set around $U$”, Uribe answered: “All of the above can happen.” The examples below show some of the possibilities.

> [!definition] Definition §67.2: Notation: $\varphi_t$ and $\varphi_q$
> In the setting of Theorem [[§67 Integral Curves#^thm-67-3|§67.3]], for fixed $t \in (-\varepsilon, \varepsilon)$ and fixed $q \in U$ write
>
> $$
> \varphi_t(q) := \varphi(t, q), \qquad \varphi_q(t) := \varphi(t, q).
> $$
>
> Then $\varphi_t : U \to M$ is a smooth map, and $\varphi_q : (-\varepsilon, \varepsilon) \to M$ is the integral curve of $\mathbf{X}$ with $\varphi_q(0) = q$: it “starts at $q$”.
>
> *Lee: Ch. 9, Flows*

^def-67-2

“This notation is useful when you want to fix $t$.” For the second one: “we don't use it, but I suppose we could … maybe we should use it. It sounds pedagogical. I actually like it.” The board then used it. The two notations differ only in the letter in the subscript, so whether $\varphi_s$ means a map or a curve is read off from what $s$ is: a time or a point. Lee writes $\theta_t(p)$ and $\theta^{(p)}(t)$ for the two (Chapter 9). In these notes $\varphi$ also names charts $(U, \varphi)$; from here on it is the flow unless a chart is named.

> [!example] Example §67.1: The Rotation Field
> On $\mathbb{R}^2$ let $\mathbf{X} = -y\, \dfrac{\partial}{\partial x} + x\, \dfrac{\partial}{\partial y}$, “the classical rotation.” By Proposition [[§67 Integral Curves#^prop-67-2|§67.2]] the integral curves solve
>
> $$
> \dot x = -y, \qquad \dot y = x .
> $$
>
> Then $\ddot x = -\dot y = -x$, so $x(t) = A\cos t + B\sin t$ and $y(t) = -\dot x(t) = A\sin t - B\cos t$. At $t = 0$, $(x_0, y_0) = (A, -B)$. So
>
> $$
> \varphi : \mathbb{R} \times \mathbb{R}^2 \longrightarrow \mathbb{R}^2, \qquad \big(t, (x_0, y_0)\big) \longmapsto \big(x_0\cos t - y_0\sin t,\ x_0\sin t + y_0\cos t\big).
> $$
>
> $\varphi_t$ is the rotation by the angle $t$. The integral curves are the circles centred at the origin, traversed counterclockwise, and the constant curve at the origin. They exist for all time.
>
> *Lee: Example 9.1*

^ex-67-1

“The harmonic oscillator, or rotation, whatever you want”; “everybody has solved this some time, either in an ODE class or in a physics class.” It is “the benign case”: in Theorem [[§67 Integral Curves#^thm-67-3|§67.3]] one can take $U = \mathbb{R}^2$ and any $\varepsilon$, indeed $t \in \mathbb{R}$. Going back to the question about the image, $\varphi_t(U)$ is $U$ rotated about the origin, possibly far from $U$.

![[m591-67-2.svg]]

“Now I want to give you a problematic example. Problematic in the sense that because of examples like the one I'm about to give you, the theory becomes, well, necessarily elaborate.”

> [!example] Example §67.2: Escape in Finite Time
> On $\mathbb{R}^2$ let $\mathbf{X} = y x^2\, \dfrac{\partial}{\partial x} + 0 \cdot \dfrac{\partial}{\partial y}$. The integral curves solve
>
> $$
> \dot x = y(t)\, x(t)^2, \qquad \dot y = 0 .
> $$
>
> So $y(t) = y(0) = y_0$ for all $t$, and $dx/dt = y_0 x^2$ separates, for $x_0 \neq 0$, as $dx/x^2 = y_0\, dt$: $-1/x(t) = y_0 t + C$ with $C = -1/x_0$. Hence
>
> $$
> x(t) = \frac{x_0}{1 - x_0 y_0\, t}, \qquad y(t) = y_0 .
> $$
>
> *Observation:* the denominator is zero at $t = 1/(x_0y_0)$. Take $M$ to be the open first quadrant $\{x > 0,\ y > 0\}$ (“otherwise there are sign issues; nothing interesting happens”). Fix $T > 0$, and let $q = (x_0, y_0)$ lie on the hyperbola $xy = 1/T$. Then
>
> $$
> \lim_{t \to T^-} x(t) = +\infty .
> $$
>
> For negative $t$ nothing goes wrong: the denominator only grows, and $x(t) \to 0$ as $t \to -\infty$. So the maximal domain of an integral curve of $\mathbf{X}$ starting at $(x_0, y_0)$ is
>
> $$
> \Big( -\infty,\ \frac{1}{x_0 y_0} \Big).
> $$
>
> *Lee: Example 9.10*

^ex-67-2

![[m591-67-3.svg]]

The integral curves lie on horizontal lines. Starting at $q$ the point moves to the right for $t > 0$, and the velocity $y_0x^2$ grows quadratically in $x$: “the particle just gets to infinity in finite time, beating everybody else.” Backwards in time the point moves against the arrows, towards the $y$-axis, where the field vanishes: “it gets stuck,” but there is no blowing up. The escape time $1/(x_0y_0)$ depends on the initial condition, through the hyperbola $xy = 1/T$ on which it lies. So, by inspection, not all integral curves are defined for all time — “and that makes life complicated.” (The curve does not continue past $T$, even inside $\mathbb{R}^2$: its $x$-coordinate is unbounded. No other integral curve from $q$ does either, by uniqueness on the whole common domain: two integral curves starting at $q$ agree wherever both are defined (Proposition [[§67 Integral Curves#^prop-67-6|§67.6]]; Lee, Theorem D.4). The uniqueness in Theorem [[§67 Integral Curves#^thm-67-3|§67.3]] alone gives this only for $|t| < \varepsilon$.)

## Local Theory on a Manifold

*Lecture 24. The definition again, then the local theorem on a manifold, two “simple and useful lemmas”, and uniqueness on the whole common domain: “the deep — meaning foundational — theory of the subject.”*

*The definition, recalled.* $c : I \to M$ is an integral curve of $\mathbf{X}$ if $\dot c(t) = \mathbf{X}_{c(t)}$ for all $t \in I$, where $\dot c(t) = c_{\ast t}(d/dt)$, “in a fancy way”: “the derivation at $c(t)$ defined by $c$” (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]). “To any curve $c : I \to M$ one can naturally associate a lift” to the tangent bundle,

$$
\tilde c(t) = \big(c(t), \dot c(t)\big),
$$

![[m591-67-11.svg]]

the velocity curve of Proposition [[§67 Integral Curves#^prop-67-1|§67.1]], written there $\dot c$. It exists for every smooth curve, injective or not. The integral-curve condition says that the lift is the field along the curve: $\tilde c = \mathbf{X} \circ c$.

![[m591-67-4.svg]]

If $c$ runs through the same point at two times, $c(t_1) = c(t_2)$, with different velocities $\dot c(t_1) \neq \dot c(t_2)$, the lift is still a well-defined map: it records the time, not just the point. “But this cannot be an integral curve of anything.” At $c(t_1) = c(t_2)$ the velocity would have to equal the value of the field there, and “the field is single-valued at each point.”

A student asked whether, then, an integral curve has to be injective. “We're about to prove something related … except if it's constant”: at a zero of $\mathbf{X}$ the constant curve is an integral curve. *(Filled in.)* Constant curves are not the only exception. The circles of the rotation field (Example [[§67 Integral Curves#^ex-67-1|§67.1]]) are integral curves that return to the same point with the same velocity, every $2\pi$. The “something related” is Proposition [[§67 Integral Curves#^prop-67-6|§67.6]] below. With it, Lee shows that a maximal integral curve is exactly one of: constant, injective, or periodic and nonconstant (Lee, Problem 9-1).

![[m591-67-5.svg]]

*(Not from lecture; figure added.)* The three kinds of maximal integral curve (Lee, Problem 9-1). An integral curve that comes back to a point comes back with the same velocity, the value of the field there; by Proposition [[§67 Integral Curves#^prop-67-6|§67.6]] below it then repeats itself. The loop of the previous figure, which comes back with a different velocity, is none of the three: it is not an integral curve.

> [!example] Example §67.3: Running Off the Edge
> Let $M = (-\infty, 0)$ and $\mathbf{X} = \dfrac{d}{dx}$. The integral curves solve $\dot c(t) = 1$, so the integral curve starting at $x_0$ is
>
> $$
> \varphi_t(x_0) = x_0 + t ,
> $$
>
> translation by time $t$, with $\varphi_t(x_0)|_{t=0} = x_0$. It stays in $M$ exactly while $x_0 + t < 0$. So for every $x_0 \in (-\infty, 0)$ the maximal domain in $t$ is
>
> $$
> \{ t : x_0 + t < 0 \} = (-\infty, -x_0) .
> $$

^ex-67-3

![[m591-67-6.svg]]

*(Not from lecture; figure added.)* The field $d/dx$ on $M = (-\infty, 0)$ and the integral curve from $x_0$, which reaches the end $0$ of $M$ at time $-x_0$.

“A much easier example” than Example [[§67 Integral Curves#^ex-67-2|§67.2]] of integral curves not defined for all $t$. Here the curve does not run to infinity; it runs into the end of the manifold: “we cannot go beyond that because there's the abyss instead of the nothingness.” Again the domain depends on the initial condition. “Another example of this complication that makes the theory much longer than it would be otherwise.”

The Euclidean theorem (Theorem [[§67 Integral Curves#^thm-67-3|§67.3]]) is “Theorem D.1 in Lee, with proof. I will forever be amazed by how much [Lee] was able to put in his book.” Its manifold version “follows immediately from the Euclidean version.”

> [!theorem] Theorem §67.4: Local Existence and Uniqueness on a Manifold
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. There are $\varepsilon > 0$, an open neighbourhood $U$ of $p$, and a map
>
> $$
> \varphi : (-\varepsilon, \varepsilon) \times U \longrightarrow M
> $$
>
> such that
>
> 1. $\varphi(0, q) = q$ for every $q \in U$;
> 2. for every $q \in U$, the curve $(-\varepsilon, \varepsilon) \to M$, $t \mapsto \varphi_t(q)$, is an integral curve of $\mathbf{X}$;
> 3. *(local uniqueness)* if $c : (-\delta, \delta) \to M$ is any integral curve with $c(0) = q$ for some $q \in U$, then $c(t) = \varphi_t(q)$ for all $t \in (-\varepsilon, \varepsilon) \cap (-\delta, \delta)$.
>
> Moreover, $\varphi$ is smooth.
>
> *Lee: Proposition 9.2; Theorem D.1*

^thm-67-4

In (3) “these domains don't have to be symmetric”: the same holds for an integral curve $c : I \to M$ on any open interval $I \ni 0$, on $I \cap (-\varepsilon, \varepsilon)$; the proof below does it in that form. By (3), “there's only one map like that.”

> [!proof]+ Proof
> *(Lecture 24: “use a chart at $p$, and then push forward … push this thing down here. Now we have the theorem at the level of open sets in Euclidean space, and we just push it up again.” The chart is called $\psi$, since $\varphi$ is the flow — “which is why Lee uses $\theta$.” The details are filled in.)* When $M$ is an open set in $\mathbb{R}^m$ this is Theorem [[§67 Integral Curves#^thm-67-3|§67.3]]. In general, take a chart $\psi : W \to \psi(W) \subseteq \mathbb{R}^m$ at $p$. It is a diffeomorphism of the open submanifold $W$ onto the open set $\psi(W)$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), so the field $\mathbf{X}|_W$ has a pushforward $\mathbf{Y} = \psi_\ast\mathbf{X} \in \mathfrak{X}(\psi(W))$ (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]).
>
> *The check: $c : I \to W$ is an integral curve of $\mathbf{X}$ if and only if $\psi \circ c$ is an integral curve of $\mathbf{Y}$.* By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), the velocity of $\psi \circ c$ at $t$ is $(\psi \circ c)_{\ast t}(d/dt) = d\psi_{c(t)}\big(c_{\ast t}(d/dt)\big) = d\psi_{c(t)}\big(\dot c(t)\big)$, and by definition $\mathbf{Y}_{\psi(c(t))} = d\psi_{c(t)}\big(\mathbf{X}_{c(t)}\big)$. Since $d\psi_{c(t)}$ is injective, the two right-hand sides agree exactly when $\dot c(t) = \mathbf{X}_{c(t)}$. “This is a kind of naturality that I will come back to, because this is very general.” (Lee, Proposition 9.6: a smooth $F$ takes integral curves of $\mathbf{X}$ to integral curves of $\mathbf{Y}$ for all integral curves exactly when $\mathbf{X}$ and $\mathbf{Y}$ are $F$-related.)
>
> *Push down, solve, push up.* Theorem [[§67 Integral Curves#^thm-67-3|§67.3]], for $\mathbf{Y}$ on $\psi(W)$ at $\psi(p)$, gives $\varepsilon > 0$, an open $U' \ni \psi(p)$ and a smooth $\varphi' : (-\varepsilon, \varepsilon) \times U' \to \psi(W)$. Put $U = \psi^{-1}(U')$ and
>
> $$
> \varphi(t, q) = \psi^{-1}\big(\varphi'(t, \psi(q))\big) \in W .
> $$
>
> $\varphi$ is smooth, as a composite of smooth maps, and $\varphi(0, q) = \psi^{-1}(\psi(q)) = q$. For $q \in U$ the curve $t \mapsto \varphi'(t, \psi(q))$ is an integral curve of $\mathbf{Y}$ in $\psi(W)$, so by the check, applied to $c = \varphi(\cdot, q)$ (for which $\psi \circ c = \varphi'(\cdot, \psi(q))$), $t \mapsto \varphi_t(q)$ is an integral curve of $\mathbf{X}$. This gives (1) and (2).
>
> *Uniqueness.* The one point beyond pushing down is that an integral curve $c$ of $\mathbf{X}$ might leave $W$, where the chart says nothing. Let $c : I \to M$ be an integral curve, $I \ni 0$ an open interval, $c(0) = q \in U$, and let $J = I \cap (-\varepsilon, \varepsilon)$. The set $c^{-1}(W) \cap J$ is open and contains $0$; let $J_0$ be the open interval that is its connected component containing $0$. On $J_0$, $\psi \circ c$ is an integral curve of $\mathbf{Y}$ starting at $\psi(q)$ (the check), so Theorem [[§67 Integral Curves#^thm-67-3|§67.3]](3) gives $\psi(c(t)) = \varphi'(t, \psi(q))$, that is, $c(t) = \varphi(t, q)$, for $t \in J_0$. Suppose $J_0 \neq J$, say $b = \sup J_0 < \sup J$ (the left end is handled the same way). Then $b \in J$, and by continuity $c(b) = \lim_{t \to b^-} \varphi(t, q) = \varphi(b, q)$, which lies in $W$. So $b \in c^{-1}(W) \cap J$, an open set; an interval around $b$ lies in it, and the component $J_0$ would contain $b$ and points beyond it, contradicting $b = \sup J_0$. Hence $J_0 = J$, and $c(t) = \varphi_t(q)$ on all of $I \cap (-\varepsilon, \varepsilon)$: this is (3).

^pf-67-4

*Uses:* [[§67 Integral Curves#^thm-67-3|§67.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§59 Related Vector Fields#^prop-59-2|§59.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]

![[m591-67-7.svg]]

*(Figure after the board.)* Upstairs, the field $\mathbf{X}$ on the chart domain $W$ and a curve $c$; downstairs, the pushed-forward field $\psi_\ast\mathbf{X}$ on $\psi(W)$ and the curve $\psi \circ c$.

*Simple and useful lemmas,* for any $\mathbf{X} \in \mathfrak{X}(M)$, “completely general.”

> [!theorem] Lemma §67.5: Translation and Rescaling
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. *(Translation lemma.)* For $t_0 \in \mathbb{R}$, the curve $\tilde c(t) = c(t + t_0)$, defined on $I - t_0 = \{ t - t_0 : t \in I \}$, is an integral curve of $\mathbf{X}$.
> 2. *(Rescaling.)* For $\lambda \in \mathbb{R}$, the curve $\tilde c(t) = c(\lambda t)$, defined on $\{ t : \lambda t \in I \}$, is an integral curve of $\lambda\mathbf{X}$.
>
> *Lee: Lemmas 9.3 and 9.4*

^lem-67-5

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

^pf-67-5

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]]

“You can always translate time. We're going to use it a lot.” Rescaling: “you can rescale a field pointwise by a fixed factor, and the integral curves of that are easily related to the integral curves of the original.” With $\lambda = -1$: the integral curves of $-\mathbf{X}$ are those of $\mathbf{X}$ run backwards.

![[m591-67-8.svg]]

*(Not from lecture; figure added.)* Both operations keep the image of the curve and change only the clock. Translation relabels the times, so the point reached at time $t_0$ by $c$ is reached at time $0$ by $\tilde c$; the arrow (the velocity) is unchanged. Rescaling by $\lambda = -1$ reverses the arrow, which is why $\tilde c$ follows $-\mathbf{X}$. (A general $\lambda$ also changes the speed by the factor $|\lambda|$.)

“Now the core technical result that I want to prove today.”

> [!theorem] Proposition §67.6: Uniqueness on the Common Domain
> Let $\mathbf{X} \in \mathfrak{X}(M)$, and let $c_i : I_i \to M$, $i = 1, 2$, be integral curves of $\mathbf{X}$. If there is $t_0 \in I_1 \cap I_2$ with $c_1(t_0) = c_2(t_0)$, then
>
> $$
> c_1|_{I_1 \cap I_2} = c_2|_{I_1 \cap I_2} .
> $$
>
> *Lee: Theorem 9.12 (proof)*

^prop-67-6

“Suppose you have two integral curves that agree at some time $t_0$ … Then the conclusion is that they agree wherever they can.”

> [!proof]+ Proof
> *(Lecture 24. Details from the discussion in class are added where noted.)* *Reduction to $t_0 = 0$.* By the translation lemma (Lemma [[§67 Integral Curves#^lem-67-5|§67.5]](1)), $t \mapsto c_i(t + t_0)$ are integral curves on $I_i - t_0$ that agree at $0$, and the conclusion for them is the conclusion for the $c_i$. So assume $t_0 = 0$, and let $q = c_1(0) = c_2(0)$.
>
> *Local uniqueness.* By Theorem [[§67 Integral Curves#^thm-67-4|§67.4]](3) at $q$ (in the form for any open interval containing $0$), both $c_i$ equal $\varphi_\cdot(q)$ near $0$. So there is $\varepsilon > 0$ with $(-\varepsilon, \varepsilon) \subseteq I_1 \cap I_2$ and
>
> $$
> c_1|_{(-\varepsilon, \varepsilon)} = c_2|_{(-\varepsilon, \varepsilon)} .
> $$
>
> “The only thing is to extend this local uniqueness into global uniqueness.”
>
> *Argue by contradiction.* Introduce
>
> $$
> \mathcal{T}_+ = \{ t \in I_1 \cap I_2 \cap (0, \infty) : c_1(t) \neq c_2(t) \} .
> $$
>
> We want to show $\mathcal{T}_+ = \varnothing$. Assume $\mathcal{T}_+ \neq \varnothing$. It is bounded below by $\varepsilon$; let $\tau = \inf \mathcal{T}_+ \ge \varepsilon > 0$. *(Filled in: $\tau$ is in the domain.)* $I_1 \cap I_2$ is an interval containing $\varepsilon/2$ and some point of $\mathcal{T}_+ \ge \tau$, and $\varepsilon/2 < \tau$, so $\tau \in I_1 \cap I_2$. By the definition of the infimum, $c_1 = c_2$ on $(0, \tau)$.
>
> *Claim: $c_1(\tau) = c_2(\tau)$.* Again by contradiction. If $c_1(\tau) \neq c_2(\tau)$, since $M$ is Hausdorff (Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]]) there are neighbourhoods $U_i$ of $c_i(\tau)$ with $U_1 \cap U_2 = \varnothing$. By continuity of $c_1$ and $c_2$ there is an open interval $J \ni \tau$, inside $I_1 \cap I_2$ (which is open), with $c_i(J) \subseteq U_i$. So there is $\tau_1 \in J$ with $0 < \tau_1 < \tau$, and $c_1(\tau_1) \in U_1$, $c_2(\tau_1) \in U_2$, so $c_1(\tau_1) \neq c_2(\tau_1)$ and $\tau_1 \in \mathcal{T}_+$. This contradicts $\tau = \inf \mathcal{T}_+$. Hence $c_1(\tau) = c_2(\tau)$.
>
> *Local uniqueness at $\tau$.* “By the translation lemma, local uniqueness at $t = 0$ is equivalent to local uniqueness at any $\tau$”: apply the local-uniqueness step to the integral curves $c_i(\cdot + \tau)$, which agree at $0$. So there is $\delta > 0$ such that the curves agree on $(\tau - \delta, \tau + \delta)$. Together with $c_1 = c_2$ on $(0, \tau]$, they agree on $(0, \tau + \delta) \cap I_1 \cap I_2$, so every point of $\mathcal{T}_+$ is $\ge \tau + \delta$, and $\inf \mathcal{T}_+ \ge \tau + \delta > \tau$: a contradiction. So $\mathcal{T}_+ = \varnothing$.
>
> *Negative times.* “Of course you do the same thing for $\tau_-$ from the other side. You take the sup”: with $\mathcal{T}_- = \{ t \in I_1 \cap I_2 \cap (-\infty, 0) : c_1(t) \neq c_2(t) \}$ and $\sup \mathcal{T}_-$, or apply the above to $t \mapsto c_i(-t)$, integral curves of $-\mathbf{X}$ (Lemma [[§67 Integral Curves#^lem-67-5|§67.5]](2)). With $c_1(0) = c_2(0)$, the curves agree on all of $I_1 \cap I_2$.

^pf-67-6

*Uses:* [[§67 Integral Curves#^lem-67-5|§67.5]], [[§67 Integral Curves#^thm-67-4|§67.4]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]]

![[m591-67-9.svg]]

*(Figure after the board.)* The situation the claim rules out: the curves agree on $(0, \tau)$ and differ at $\tau$, with disjoint neighbourhoods $U_1, U_2$. “When you do elementary Euclidean geometry and argue by contradiction, every picture that you draw doesn't look contradictory, because the thing is true.” A student noted that the argument is “very similar” to the Euclidean one; Uribe agreed. On a manifold, the Hausdorff property is what makes the set where the curves agree closed. Another student asked how $J$ stays inside $I_1 \cap I_2$; it does because the domains are open intervals.

> [!example] Example §67.4: The Euler Field
> On $\mathbb{R}^2$ let $\mathbf{X} = x\, \dfrac{\partial}{\partial x} + y\, \dfrac{\partial}{\partial y}$. The integral curves solve $\dot x = x$, $\dot y = y$, so $\varphi_t(x_0, y_0) = e^t(x_0, y_0)$, $t \in \mathbb{R}$. For $(x_0, y_0) \neq 0$ the image is the open ray from the origin through $(x_0, y_0)$, since $e^t$ takes every value in $(0, \infty)$ and never $0$; at the origin the integral curve is constant.

^ex-67-4

![[m591-67-10.svg]]

“If you go to Desmos or whatever, you see the integral curves of the Euler field … on $\mathbb{R}^2$ radial, like that, and they seem to intersect, but they don't.” The rays are open, and the origin is its own integral curve. The images of the integral curves $t \mapsto e^t(x_0, y_0)$, $t \in \mathbb{R}$, partition $\mathbb{R}^2$, as Proposition [[§67 Integral Curves#^prop-67-6|§67.6]] requires. *(Filled in.)* If two of them pass through a common point, $c_1(t_1) = c_2(t_2)$, then $t \mapsto c_2(t + t_2 - t_1)$ is an integral curve (Lemma [[§67 Integral Curves#^lem-67-5|§67.5]](1)) that agrees with $c_1$ at time $t_1$, so it equals $c_1$ on $\mathbb{R}$ (Proposition [[§67 Integral Curves#^prop-67-6|§67.6]]), and the two images coincide.
