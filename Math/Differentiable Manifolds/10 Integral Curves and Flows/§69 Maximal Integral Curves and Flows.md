---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 69
tags: [differentiable-manifolds, math591]
---
← [[§68 Local Existence and Uniqueness]] · ↑ [[· 10 Integral Curves and Flows]]

*Stage: dynamics — The maximal integral curve through each point, complete vector fields, and the flow: all maximal curves assembled into one smooth map on an open domain in $\mathbb{R} \times M$.*

*Lecture 24. “What this allows us to do” — uniqueness on the common domain, Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] — “is to define the maximal domain of an integral curve, given an initial condition.”*

> [!definition] Definition §69.1: Maximal Domain
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. Define
>
> $$
> \big(\alpha(p), \beta(p)\big) = \bigcup_{I} I ,
> $$
>
> the union over the domains $I$ of all integral curves of $\mathbf{X}$ starting at $p$:
> an open interval containing $0$, possibly infinite or semi-infinite. It is the **maximal domain** of integral curves of $\mathbf{X}$ starting at $p$.
>
> *Lee: Theorem 9.12*

^def-69-1

The union is nonempty, since an integral curve starting at $p$ exists (Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]). Each domain $I$ is an open interval containing $0$, “because it starts at $p$”, so the union is an open interval containing $0$. “So it's something that is very harmless to take.”

> [!theorem] Proposition §69.1: The Maximal Integral Curve
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. There is an integral curve $\varphi_p : (\alpha(p), \beta(p)) \to M$ of $\mathbf{X}$ starting at $p$, and every integral curve $c : I \to M$ starting at $p$ satisfies $I \subseteq (\alpha(p), \beta(p))$ and $c = \varphi_p|_I$. So $(\alpha(p), \beta(p))$ is the largest possible domain of such a curve, and $\varphi_p$ is the unique maximal integral curve starting at $p$. This proves Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](1).
>
> *Lee: Theorem 9.12*

^prop-69-1

> [!proof]+ Proof
> *(Lecture 24: “How do you define it? Well, I take a point $t$ here. It's in some $I$, so there is some integral curve defined in the neighbourhood of that. I define it by that, and it doesn't matter which $I$ I chose, by the previous lemma.” Details filled in.)* For $t \in (\alpha(p), \beta(p))$, choose an integral curve $c : I \to M$ starting at $p$ with $t \in I$, and set $\varphi_p(t) = c(t)$. *Well defined:* if $c' : I' \to M$ is another, then $c$ and $c'$ agree at time $0$, so by Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] they agree on $I \cap I' \ni t$. *An integral curve:* near each $t$, $\varphi_p$ equals the smooth curve $c$ on the open interval $I \ni t$, so $\varphi_p$ is smooth and $\dot\varphi_p(t) = \dot c(t) = \mathbf{X}_{c(t)} = \mathbf{X}_{\varphi_p(t)}$, since velocity at $t$ only depends on the curve near $t$. And $\varphi_p(0) = p$. *Maximal:* if $c : I \to M$ starts at $p$, then $I$ is one of the domains in the union, so $I \subseteq (\alpha(p), \beta(p))$, and $c = \varphi_p|_I$ by the definition of $\varphi_p$.

^pf-69-1

*Uses:* [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

“The uniqueness is absolutely fantastic for the theory.” The maximal domains of the examples: $\mathbb{R}$ for the rotation and Euler fields (Examples [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]] and [[§68 Local Existence and Uniqueness#^ex-68-2|§68.2]]); $(-\infty, 1/(x_0y_0))$ and $(-\infty, -x_0)$ for the two examples that follow.

“Now I want to give you a problematic example. Problematic in the sense that because of examples like the one I'm about to give you, the theory becomes, well, necessarily elaborate.”

> [!example] Example §69.1: Escape in Finite Time
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

^ex-69-1

![[m591-67-3.svg]]

![[m591-67-a2.gif|480]]

*(Not from lecture; animation added, vault only.)* Four integral curves of $\mathbf{X} = yx^2\,\partial_x$, all starting at $x_0 = 1/2$, on the lines $y_0 = 2, 1.5, 1, 0.5$, so they escape at $T = 1/(x_0y_0) = 1, 1.33, 2, 4$. Each point moves slowly at first and then runs off to $x = \infty$ just before its time $T$: $x(t) = x_0/(1 - x_0y_0t)$. (The arrows' lengths grow like $\log(1 + yx^2)$, not $yx^2$, so that they fit.)

The integral curves lie on horizontal lines. Starting at $q$ the point moves to the right for $t > 0$, and the velocity $y_0x^2$ grows quadratically in $x$: “the particle just gets to infinity in finite time, beating everybody else.” Backwards in time the point moves against the arrows, towards the $y$-axis, where the field vanishes: “it gets stuck,” but there is no blowing up. The escape time $1/(x_0y_0)$ depends on the initial condition, through the hyperbola $xy = 1/T$ on which it lies. So, by inspection, not all integral curves are defined for all time — “and that makes life complicated.” (The curve does not continue past $T$, even inside $\mathbb{R}^2$: its $x$-coordinate is unbounded. No other integral curve from $q$ does either, by uniqueness on the whole common domain: two integral curves starting at $q$ agree wherever both are defined (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]; Lee, Theorem D.4). The uniqueness in Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]] alone gives this only for $|t| < \varepsilon$.)

![[m591-68-1.svg]]

*(Not from lecture; figure added.)* The flow domain of Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]], sliced at $y_0 = 1$. Over each initial point $p = (x_0, 1)$ the domain is the vertical half-line $t < 1/x_0$, open at the top. These segments fill the region below the hyperbola $t = 1/x_0$, which is open.

> [!example] Example §69.2: Running Off the Edge
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

^ex-69-2

![[m591-67-6.svg]]

*(Not from lecture; figure added.)* The field $d/dx$ on $M = (-\infty, 0)$ and the integral curve from $x_0$, which reaches the end $0$ of $M$ at time $-x_0$.

“A much easier example” than Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] of integral curves not defined for all $t$. Here the curve does not run to infinity; it runs into the end of the manifold: “we cannot go beyond that because there's the abyss instead of the nothingness.” Again the domain depends on the initial condition. “Another example of this complication that makes the theory much longer than it would be otherwise.”

![[m591-68-2.svg]]

*(Not from lecture; figure added.)* The maximal domains of Example [[§69 Maximal Integral Curves and Flows#^ex-69-2|§69.2]], assembled into the set $\mathcal{D} = \{ (t, x_0) : x_0 < 0,\ t < -x_0 \}$ of Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2), an open set. Compare the flow domain of Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] above: there $\beta(p) = 1/(x_0y_0)$ blows up as $x_0 \to 0$, here $\beta(x_0) = -x_0$ shrinks to $0$ at the end of $M$. Neither field is complete.

![[m591-68-a2.gif|460]]

*(Not from lecture; animation added, vault only.)* Five integral curves of $d/dx$ on $(-\infty, 0)$, starting at $x_0 = -3, \ldots, -0.4$, run right at unit speed and leave $M$ at time $-x_0$. Right, their maximal domains filling the region $t < -x_0$ of the figure (drawn for $t \ge 0$): the field is not complete.

> [!theorem] Proposition §69.2: Non-Injective Maximal Integral Curves Are Periodic
> Let $\mathbf{X} \in \mathfrak{X}(M)$, $p \in M$, and let $\varphi_p : (\alpha(p), \beta(p)) \to M$ be the maximal integral curve of $\mathbf{X}$ starting at $p$. If $\varphi_p$ is not injective, say $\varphi_p(t_1) = \varphi_p(t_2)$ with $T = t_2 - t_1 > 0$, then $(\alpha(p), \beta(p)) = \mathbb{R}$ and
>
> $$
> \varphi_p(t + T) = \varphi_p(t) \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> *Lee: Problem 9-1*

^prop-69-2

> [!proof]+ Proof
> *(Not from lecture: Uribe's argument by email, Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]], completed by maximality.)* Write $I = (\alpha, \beta) = (\alpha(p), \beta(p))$ and $c = \varphi_p$. By Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]],
>
> $$
> c(s + T) = c(s) \qquad \text{whenever } s \in I \text{ and } s + T \in I . \tag{$\dagger$}
> $$
>
> Since $\alpha < t_1 < t_2 < \beta$, we have $T < \beta - \alpha$.
>
> *$\beta = +\infty$.* Suppose $\beta < +\infty$. The intervals $I = (\alpha, \beta)$ and $I + T = (\alpha + T, \beta + T)$ overlap, because $\alpha + T < \beta$, and their union is $(\alpha, \beta + T)$. Define $\tilde c$ on it by
>
> $$
> \tilde c(t) = c(t) \ \ (t \in I), \qquad \tilde c(t) = c(t - T) \ \ (t \in I + T) .
> $$
>
> This is well defined: if $t \in I \cap (I + T)$, then $s = t - T$ has $s \in I$ and $s + T = t \in I$, so $c(t - T) = c(t)$ by $(\dagger)$. On the open interval $I$, $\tilde c$ is the integral curve $c$; on the open interval $I + T$, it is the integral curve $t \mapsto c(t - T)$ (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1) with $t_0 = -T$). Smoothness and the equation $\dot{\tilde c}(t) = \mathbf{X}_{\tilde c(t)}$ only involve $\tilde c$ near $t$, so $\tilde c$ is an integral curve of $\mathbf{X}$. It starts at $p$, as $0 \in I$ and $\tilde c(0) = c(0) = p$. Its domain $(\alpha, \beta + T)$ is not contained in $(\alpha, \beta)$, which contradicts Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]. So $\beta = +\infty$.
>
> *$\alpha = -\infty$.* In the same way, if $\alpha > -\infty$, then $\tilde c(t) = c(t)$ on $I$ and $\tilde c(t) = c(t + T)$ on $I - T = (\alpha - T, \beta - T)$ define an integral curve starting at $p$ on $(\alpha - T, \beta)$: on the overlap $I \cap (I - T)$ the two agree by $(\dagger)$ with $s = t$. This again contradicts Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]].
>
> *Periodicity.* Now $I = \mathbb{R}$, so $(\dagger)$ holds for every $s \in \mathbb{R}$.

^pf-69-2

*Uses:* [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]], [[§67 Integral Curves#^lem-67-4|§67.4]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

So a maximal integral curve is either injective or periodic and defined for all time. Lee's Problem 9-1 separates out the constant curves, which are periodic with every period.

> [!definition] Definition §69.2: Complete Vector Field
> $\mathbf{X} \in \mathfrak{X}(M)$ is **complete** if $(\alpha(p), \beta(p)) = \mathbb{R}$ for every $p \in M$.
>
> *Lee: Ch. 9, Complete Vector Fields*

^def-69-2

“This is the case where there are no headaches … you can go forever, and backwards in time as well, forever.” (“The existential question is: the time domain of the universe — is it complete?”) The rotation field and the Euler field are complete; the fields of Examples [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] and [[§69 Maximal Integral Curves and Flows#^ex-69-2|§69.2]] are not.

“When you're doing theory, you wonder: are there results that have the conclusion ‘this vector field is complete’? It's hard to tell in general.” “A very powerful-seeming little result”:

> [!theorem] Lemma §69.3: Uniform Time Lemma
> Let $\mathbf{X} \in \mathfrak{X}(M)$. If there is $\varepsilon > 0$ such that $(-\varepsilon, \varepsilon) \subseteq (\alpha(p), \beta(p))$ for every $p \in M$, then $\mathbf{X}$ is complete.
>
> *Lee: Lemma 9.15*

^lem-69-3

> [!proof]+ Proof (to be filled)
> To be proved in Lecture 25 (“I'll prove this on Monday”).

^pf-69-3

![[m591-68-3.svg]]

*(Figure after the board.)* “The horizontal line is $M$, and then you have $\mathbb{R}$ here”: over each $p$, the maximal domain $(\alpha(p), \beta(p))$, between the graphs $t = \beta(p) > 0$ and $t = \alpha(p) < 0$. The lemma's hypothesis is that a uniform strip $(-\varepsilon, \varepsilon) \times M$ fits inside; its conclusion is that the whole of $\mathbb{R} \times M$ does. (“I always reverse the cartoon axes. Someday I'll learn.”)

Announced for Monday, as consequences of Lemma [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]]:
- every vector field on a compact manifold is complete: “compactness will assure that there is a uniform time” (Lee, Corollary 9.17);
- every left-invariant vector field on a Lie group is complete, “because you're going to be able to translate solutions” (Lee, Theorem 9.18).

*The flow. Lecture 23, the last minutes: “Let me tell you the bigger picture of what actually is happening, and then we'll see how much of that we get to prove … We'll prove a big chunk of this on Friday.”*

> [!theorem] Theorem §69.4: Maximal Integral Curves and the Flow
> Let $M$ be a smooth manifold and $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. For every $p \in M$ there is a unique *maximal* integral curve of $\mathbf{X}$ starting at $p$, maximal with respect to its domain. Write it $\varphi_p$ and its domain $(\alpha(p), \beta(p))$, where $\alpha(p) \in [-\infty, 0)$ and $\beta(p) \in (0, +\infty]$: “$\alpha$ or $\beta$ may be $\pm\infty$.”
> 2. Let
>
> $$
> \mathcal{D} = \bigcup_{p \in M} \big(\alpha(p), \beta(p)\big) \times \{p\} \ \subseteq\ \mathbb{R} \times M, \qquad \varphi : \mathcal{D} \longrightarrow M, \quad (t, p) \longmapsto \varphi_p(t).
> $$
>
> Then $\mathcal{D}$ is open in $\mathbb{R} \times M$, and $\varphi$ is smooth.
>
> *Lee: Theorem 9.12*

^thm-69-4

> [!proof]+ Proof of (1) (Lecture 24); (2) to be filled
> Part (1) is Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]] above, proved in Lecture 24. Part (2) is to be proved. Uribe's indication for (1), in Lecture 23: “by uniqueness and something called the translation lemma, which is very easy to see,” there is “only one way to continue the curve forwards in time and then backwards in time until either you never stop or you run into the edge of the manifold.” Openness of $\mathcal{D}$ “is surprisingly long to prove.”

^pf-69-4

*Uses:* [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

![[m591-68-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* The flow of a complete field, the pendulum field $y\,\partial_x - \sin x\,\partial_y$ (chosen for the picture; gray: its integral curves), integrated numerically. A disc of initial points with a grid is carried along: each $\varphi_t$ moves it as a diffeomorphism would. Then flowing $1.2$ and then $s$ more (green) is compared with flowing $2.2$ at once (red dashed); at $s = 1$ they coincide, $\varphi_s \circ \varphi_t = \varphi_{s+t}$. The diffeomorphism property and this group law are Lee, Theorem 9.12, not yet in the notes.

$\varphi$ is “just flowing, like we were doing before”, except that the domain of the time variable depends on the point, as in Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]. The theorem is the local picture of Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]], with its rectangles $(-\varepsilon, \varepsilon) \times U$, put together on the whole manifold. In the two examples:
- Rotation (Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]]): $\alpha \equiv -\infty$, $\beta \equiv +\infty$, $\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$.
- Escape (Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]): $\alpha \equiv -\infty$, $\beta(x, y) = 1/(xy)$, so $\mathcal{D} = \{ (t, (x, y)) : x, y > 0,\ t\,xy < 1 \}$, open, and $\varphi(t, (x, y)) = \big(x/(1 - xyt),\ y\big)$, smooth on $\mathcal{D}$.
