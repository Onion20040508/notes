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
> \tilde\varphi\big(\dot c(t)\big) = \Big(x^1(c(t)), \ldots , x^m(c(t)),\ (x^1 \circ c)'(t), \ldots , (x^m \circ c)'(t)\Big), \qquad t \in I_0 ,
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
> \dot x^i(t) = f^i\big(x^1(t), \ldots , x^m(t)\big) \qquad \text{for all } i = 1, \ldots , m \text{ and all } t \in I .
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

The integral curves lie on horizontal lines. Starting at $q$ the point moves to the right for $t > 0$, and the velocity $y_0x^2$ grows quadratically in $x$: “the particle just gets to infinity in finite time, beating everybody else.” Backwards in time the point moves against the arrows, towards the $y$-axis, where the field vanishes: “it gets stuck,” but there is no blowing up. The escape time $1/(x_0y_0)$ depends on the initial condition, through the hyperbola $xy = 1/T$ on which it lies. So, by inspection, not all integral curves are defined for all time — “and that makes life complicated.” (The curve does not continue past $T$, even inside $\mathbb{R}^2$: its $x$-coordinate is unbounded. No other integral curve from $q$ does either, by uniqueness on the whole common domain: two integral curves starting at $q$ agree wherever both are defined (Theorem [[§68 Flows#^thm-68-1|§68.1]](1); Lee, Theorem D.4). The uniqueness in Theorem [[§67 Integral Curves#^thm-67-3|§67.3]] alone gives this only for $|t| < \varepsilon$.)
