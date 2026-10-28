---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 67
tags: [differentiable-manifolds, math591]
---
← [[§66 Partitions of Unity]] · ↑ [[· 10 Integral Curves and Flows]] · [[§68 Flows]] →

*Stage: dynamics — Curves whose velocity is prescribed by a vector field; in coordinates, a first-order system of ODEs.*

For a smooth curve $c : I \to M$ and $t \in I$, write $\dot c(t) = \frac{dc}{dt}(t) \in T_{c(t)}M$ for its velocity at time $t$: the velocity $D_\gamma$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]]) of the shifted curve $\gamma(s) = c(t + s)$, that is, $\dot c(t) = c_{\ast t}\big(\frac{d}{dt}\big|_t\big)$.

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

> [!theorem] Proposition §67.1: Integral Curves in Coordinates
> Let $M \subseteq \mathbb{R}^m$ be open, with coordinates $x^1, … , x^m$, and $\mathbf{X} = \sum_i f^i\, \partial/\partial x^i$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). Write a smooth curve as $c(t) = (x^1(t), … , x^m(t))$, with velocity $\dot c(t) = \langle \dot x^1(t), … , \dot x^m(t) \rangle$. Then $c$ is an integral curve of $\mathbf{X}$ if and only if
>
> $$
> \dot x^i(t) = f^i\big(x^1(t), … , x^m(t)\big) \qquad \text{for all } i = 1, … , m \text{ and all } t \in I .
> $$
>
> The same holds on any manifold, in any chart, with the $x^i(t)$ the coordinates of $c(t)$.
>
> *Lee: Ch. 9, Integral Curves, (9.1)*

^prop-67-1

> [!proof]+ Proof
> By Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]], applied at each time $t$ to the shifted curve $s \mapsto c(t + s)$, $\dot c(t) = \sum_i \dot x^i(t)\, \partial/\partial x^i|_{c(t)}$, while $\mathbf{X}_{c(t)} = \sum_i f^i(c(t))\, \partial/\partial x^i|_{c(t)}$. The $\partial/\partial x^i|_{c(t)}$ form a basis of $T_{c(t)}M$, so $(\ast)$ holds at $t$ exactly when the components agree. The argument uses only a chart, so it applies on any manifold.

^pf-67-1

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]

The angle brackets mark $\dot c$ as a vector, not a point: “I've been trained … that you should distinguish vectors from points.” What the proposition shows is that $(\ast)$ is a *system of first-order ODEs*, usually nonlinear. All the derivatives are on the left-hand side, solved for: the right-hand side involves no derivatives. And it is a genuine *system*, because the equation for $\dot x^i$ involves, in principle, all of the $x$'s. (Lee: solving a system of ODEs is called “integrating” it, hence the name *integral* curve.)

“There's a fundamental theorem that, again, from — we have moved from Calc 3 to Calc 4 — ODEs.” Uribe quoted it in the following form.

> [!theorem] Theorem §67.2: Local Existence and Uniqueness
> Let $M \subseteq \mathbb{R}^m$ be open and $\mathbf{X} \in \mathfrak{X}(M)$. Given any $p \in M$, there are $\varepsilon > 0$, an open neighbourhood $U \subseteq M$ of $p$, and a smooth map
>
> $$
> \varphi : (-\varepsilon, \varepsilon) \times U \longrightarrow M
> $$
>
> such that
>
> 1. $\varphi(0, q) = q$ for every $q \in U$;
> 2. for every $q \in U$, the curve $(-\varepsilon, \varepsilon) \to M$, $t \mapsto \varphi(t, q)$, is an integral curve of $\mathbf{X}$.
>
> Furthermore (uniqueness): if $q \in U$ and $c : I \to M$ is any integral curve of $\mathbf{X}$ with $0 \in I$ and $c(0) = q$, then
>
> $$
> c|_{I \cap (-\varepsilon, \varepsilon)} = \varphi(\cdot, q)|_{I \cap (-\varepsilon, \varepsilon)} .
> $$
>
> *Lee: Theorem D.1*

^thm-67-2

> [!proof]+ Proof (not given in this course)
> Taken from ODE theory, not proved in the course: “a big, big theorem that takes forever to prove”, the theorem on existence, uniqueness and smooth dependence on initial conditions (Lee, Theorem D.1, proved in Appendix D). “This theorem here packs everything that we will quote from the Euclidean case.”

^pf-67-2

![[m591-67-1.svg]]

“Imagine a Calc 3 plot of a field … the vectors at every point.” The theorem gives a time interval $(-\varepsilon, \varepsilon)$ and a neighbourhood $U$ of $p$ (drawn as a rectangle) such that from every point $q \in U$, $p$ included, there is an integral curve $t \mapsto \varphi(t, q)$ that starts at $q$ and is defined at least for $|t| < \varepsilon$.

*What the theorem says beyond “there is a path through $q$”* (a student's question). “It says a lot of delicate things.” The time interval is *uniform*: as long as $q \in U$, the curve is defined at least for $|t| < \varepsilon$. And $\varphi$ is smooth as a function of the pair $(t, q)$ on the product $(-\varepsilon, \varepsilon) \times U$: smooth in $t$, as an integral curve must be, but also, for fixed $t$, smooth in the initial condition $q$. Asked whether the image of $\varphi$ is “just a slightly bigger open set around $U$”, Uribe answered: “All of the above can happen.” The examples below show some of the possibilities.

> [!definition] Definition §67.2: Notation: $\varphi_t$ and $\varphi_q$
> In the setting of Theorem [[§67 Integral Curves#^thm-67-2|§67.2]], for fixed $t \in (-\varepsilon, \varepsilon)$ and fixed $q \in U$ write
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
> On $\mathbb{R}^2$ let $\mathbf{X} = -y\, \dfrac{\partial}{\partial x} + x\, \dfrac{\partial}{\partial y}$, “the classical rotation.” By Proposition [[§67 Integral Curves#^prop-67-1|§67.1]] the integral curves solve
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

“The harmonic oscillator, or rotation, whatever you want”; “everybody has solved this some time, either in an ODE class or in a physics class.” It is “the benign case”: in Theorem [[§67 Integral Curves#^thm-67-2|§67.2]] one can take $U = \mathbb{R}^2$ and any $\varepsilon$, indeed $t \in \mathbb{R}$. Going back to the question about the image, $\varphi_t(U)$ is $U$ rotated about the origin, possibly far from $U$.

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

The integral curves lie on horizontal lines. Starting at $q$ the point moves to the right for $t > 0$, and the velocity $y_0x^2$ grows quadratically in $x$: “the particle just gets to infinity in finite time, beating everybody else.” Backwards in time the point moves against the arrows, towards the $y$-axis, where the field vanishes: “it gets stuck,” but there is no blowing up. The escape time $1/(x_0y_0)$ depends on the initial condition, through the hyperbola $xy = 1/T$ on which it lies. So, by inspection, not all integral curves are defined for all time — “and that makes life complicated.” (The curve does not continue past $T$, even inside $\mathbb{R}^2$: its $x$-coordinate is unbounded. No other integral curve from $q$ does either, by uniqueness on the whole common domain: two integral curves starting at $q$ agree wherever both are defined (Theorem [[§68 Flows#^thm-68-1|§68.1]](1); Lee, Theorem D.4). The uniqueness in Theorem [[§67 Integral Curves#^thm-67-2|§67.2]] alone gives this only for $|t| < \varepsilon$.)
