---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 69
tags: [differentiable-manifolds, math591]
---
← [[§68 Local Existence and Uniqueness]] · ↑ [[· 10 Integral Curves and Flows]] · [[§70 Complete Vector Fields]] →

*Stage: dynamics — The maximal integral curve through each point, and the flow: all maximal curves assembled into one smooth map on an open domain in $\mathbb{R} \times M$, which obeys the group law.*

*Lecture 24. Uniqueness on the common domain, Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]], allows one to define the maximal domain of an integral curve, given an initial condition.*

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

The union is nonempty, since an integral curve starting at $p$ exists (Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]). Each domain $I$ is an open interval containing $0$, because the curve starts at $p$, so the union is an open interval containing $0$.

> [!theorem] Proposition §69.1: The Maximal Integral Curve
> Let $\mathbf{X} \in \mathfrak{X}(M)$ and $p \in M$. There is an integral curve $\varphi^p : (\alpha(p), \beta(p)) \to M$ of $\mathbf{X}$ starting at $p$, and every integral curve $c : I \to M$ starting at $p$ satisfies $I \subseteq (\alpha(p), \beta(p))$ and $c = \varphi^p|_I$. So $(\alpha(p), \beta(p))$ is the largest possible domain of such a curve, and $\varphi^p$ is the unique maximal integral curve starting at $p$. This proves Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](1).
>
> *Lee: Theorem 9.12*

^prop-69-1

> [!proof]+ Proof
> *(Lecture 24: a point $t$ of the maximal domain lies in some $I$, so some integral curve is defined near $t$; define $\varphi^p(t)$ by it. By the previous proposition the choice of $I$ does not matter. Details filled in.)* For $t \in (\alpha(p), \beta(p))$, choose an integral curve $c : I \to M$ starting at $p$ with $t \in I$, and set $\varphi^p(t) = c(t)$. *Well defined:* if $c' : I' \to M$ is another, then $c$ and $c'$ agree at time $0$, so by Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] they agree on $I \cap I' \ni t$. *An integral curve:* near each $t$, $\varphi^p$ equals the smooth curve $c$ on the open interval $I \ni t$, so $\varphi^p$ is smooth and $\dot\varphi^p(t) = \dot c(t) = \mathbf{X}_{c(t)} = \mathbf{X}_{\varphi^p(t)}$, since velocity at $t$ only depends on the curve near $t$. And $\varphi^p(0) = p$. *Maximal:* if $c : I \to M$ starts at $p$, then $I$ is one of the domains in the union, so $I \subseteq (\alpha(p), \beta(p))$, and $c = \varphi^p|_I$ by the definition of $\varphi^p$.

^pf-69-1

*Uses:* [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

The maximal domains of the examples: $\mathbb{R}$ for the rotation and Euler fields (Examples [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]] and [[§68 Local Existence and Uniqueness#^ex-68-5|§68.5]]); $(-\infty, 1/(x_0y_0))$ and $(-\infty, -x_0)$ for the two examples that follow.

The next example is problematic: examples like it are what make the theory of flows necessarily elaborate.

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
> *Observation:* the denominator is zero at $t = 1/(x_0y_0)$. Take $M$ to be the open first quadrant $\{x > 0,\ y > 0\}$ (otherwise there are sign issues, and nothing more interesting happens). Fix $T > 0$, and let $q = (x_0, y_0)$ lie on the hyperbola $xy = 1/T$. Then
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

The integral curves lie on horizontal lines. Starting at $q$ the point moves to the right for $t > 0$, and the velocity $y_0x^2$ grows quadratically in $x$: the point gets to infinity in finite time. Backwards in time the point moves against the arrows, towards the $y$-axis, where the field vanishes: it creeps towards the axis, but there is no blowing up. The escape time $1/(x_0y_0)$ depends on the initial condition, through the hyperbola $xy = 1/T$ on which it lies. So, by inspection, not all integral curves are defined for all time. (The curve does not continue past $T$, even inside $\mathbb{R}^2$: its $x$-coordinate is unbounded. No other integral curve from $q$ does either, by uniqueness on the whole common domain: two integral curves starting at $q$ agree wherever both are defined (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]; Lee, Theorem D.4). The uniqueness in Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]] alone gives this only for $|t| < \varepsilon$.)

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

A much easier example than Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] of integral curves not defined for all $t$. Here the curve does not run to infinity; it runs into the end of the manifold, and there is no manifold beyond it to continue in. Again the domain depends on the initial condition; this complication is what makes the theory much longer than it would be otherwise.

![[m591-68-2.svg]]

*(Not from lecture; figure added.)* The maximal domains of Example [[§69 Maximal Integral Curves and Flows#^ex-69-2|§69.2]], assembled into the set $\mathcal{D} = \{ (t, x_0) : x_0 < 0,\ t < -x_0 \}$ of Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2), an open set. Compare the flow domain of Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]] above: there $\beta(p) = 1/(x_0y_0)$ blows up as $x_0 \to 0$, here $\beta(x_0) = -x_0$ shrinks to $0$ at the end of $M$. Neither field is complete.

![[m591-68-a2.gif|460]]

*(Not from lecture; animation added, vault only.)* Five integral curves of $d/dx$ on $(-\infty, 0)$, starting at $x_0 = -3, \ldots, -0.4$, run right at unit speed and leave $M$ at time $-x_0$. Right, their maximal domains filling the region $t < -x_0$ of the figure (drawn for $t \ge 0$): the field is not complete.

> [!theorem] Proposition §69.2: Non-Injective Maximal Integral Curves Are Periodic
> Let $\mathbf{X} \in \mathfrak{X}(M)$, $p \in M$, and let $\varphi^p : (\alpha(p), \beta(p)) \to M$ be the maximal integral curve of $\mathbf{X}$ starting at $p$. If $\varphi^p$ is not injective, say $\varphi^p(t_1) = \varphi^p(t_2)$ with $T = t_2 - t_1 > 0$, then $(\alpha(p), \beta(p)) = \mathbb{R}$ and
>
> $$
> \varphi^p(t + T) = \varphi^p(t) \qquad \text{for all } t \in \mathbb{R} .
> $$
>
> *Lee: Problem 9-1*

^prop-69-2

> [!proof]+ Proof
> *(Not from lecture: the argument sent by email, Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]], completed by maximality.)* Write $I = (\alpha, \beta) = (\alpha(p), \beta(p))$ and $c = \varphi^p$. By Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]],
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

*Lecture 25. A recap of the flow domain, with the cartoon redrawn.* Given $\mathbf{X} \in \mathfrak{X}(M)$, every $p \in M$ has its maximal domain $(\alpha(p), \beta(p)) \ni 0$, which can be all of $\mathbb{R}$; when it is, things simplify. The flow domain and the flow (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]]) are

$$
\mathcal{D} = \{ (t, p) \in \mathbb{R} \times M : t \in (\alpha(p), \beta(p)) \}, \qquad \varphi : \mathcal{D} \to M, \quad (t, p) \longmapsto \varphi(t, p),
$$

where, in words, $\varphi(t, p)$ is the integral curve starting at $p$, evaluated at $t$.

![[m591-69-3.svg]]

*(Figure after the board.)* Time is horizontal and $M$ vertical here: over each $p$ the open segment $(\alpha(p), \beta(p)) \times \{p\}$, which always contains $(0, p)$; together they fill $\mathcal{D}$. The figure after Lemma [[§70 Complete Vector Fields#^lem-70-1|§70.1]] in [[§70 Complete Vector Fields|§70]] is the same cartoon with the axes exchanged.

*Careful.* The definition of integral curve allows any curve $c : I \to M$ with $\dot c(t) = \mathbf{X}_{c(t)}$ for all $t \in I$ (Definition [[§67 Integral Curves#^def-67-1|§67.1]]), so $I$ need not contain $0$: translating an integral curve (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)) gives one whose domain misses $0$. The curve $t \mapsto \varphi^p(t)$, in the notation $\varphi_t(p) = \varphi(t, p) = \varphi^p(t)$ (Definition [[§68 Local Existence and Uniqueness#^def-68-1|§68.1]] and the paragraph after it), is an integral curve that is defined at $t = 0$, where it is $p$. The flow $\varphi$ is the local maps of Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]] glued together; they fit together by uniqueness.

That $\mathcal{D}$ is open and $\varphi$ smooth (Theorem [[§69 Maximal Integral Curves and Flows#^thm-69-4|§69.4]](2)) was not proved in class; the proof, from Lee, is filled in after the theorem.

> [!definition] Definition §69.2: Flow Box
> Let $\mathbf{X} \in \mathfrak{X}(M)$ with flow $\varphi : \mathcal{D} \to M$, and $p \in M$. A **flow box** (or **local domain**) at $p$ is a product $(-\varepsilon, \varepsilon) \times U \subseteq \mathcal{D}$, with $\varepsilon > 0$ and $U$ an open neighbourhood of $p$, on which $\varphi$ is smooth; together with the restriction $\varphi| : (-\varepsilon, \varepsilon) \times U \to M$.
>
> *Lee: Ch. 9, Flows*

^def-69-2

Both names are in use. Every point has such a box, by the next lemma.

> [!theorem] Lemma §69.3: Flow Boxes Exist
> Let $\mathbf{X} \in \mathfrak{X}(M)$. Every $p \in M$ has a flow box $(-\varepsilon, \varepsilon) \times U$.
>
> *Lee: Theorem 9.12 (proof)*

^lem-69-3

> [!proof]+ Proof
> *(Lecture 25, recalled from Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]]; the identification with the maximal flow is filled in.)* Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]] gives $\varepsilon > 0$, an open $U \ni p$ and a smooth $\varphi' : (-\varepsilon, \varepsilon) \times U \to M$ such that, for $q \in U$, $\varphi'(\cdot, q)$ is an integral curve starting at $q$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]], $(-\varepsilon, \varepsilon) \subseteq (\alpha(q), \beta(q))$ and $\varphi'(t, q) = \varphi^q(t) = \varphi(t, q)$. So $(-\varepsilon, \varepsilon) \times U \subseteq \mathcal{D}$, and $\varphi$ restricted to it is $\varphi'$, which is smooth.

^pf-69-3

*Uses:* [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

*The flow. Lecture 23, the last minutes: the bigger picture, stated before it is proved; a large part of it is proved in Lecture 24.*

> [!theorem] Theorem §69.4: Maximal Integral Curves and the Flow
> Let $M$ be a smooth manifold and $\mathbf{X} \in \mathfrak{X}(M)$.
>
> 1. For every $p \in M$ there is a unique *maximal* integral curve of $\mathbf{X}$ starting at $p$, maximal with respect to its domain. Write it $\varphi^p$ and its domain $(\alpha(p), \beta(p))$, where $\alpha(p) \in [-\infty, 0)$ and $\beta(p) \in (0, +\infty]$, so either may be infinite.
> 2. Let
>
> $$
> \mathcal{D} = \bigcup_{p \in M} \big(\alpha(p), \beta(p)\big) \times \{p\} \ \subseteq\ \mathbb{R} \times M, \qquad \varphi : \mathcal{D} \longrightarrow M, \quad (t, p) \longmapsto \varphi^p(t).
> $$
>
> Then $\mathcal{D}$ is open in $\mathbb{R} \times M$, and $\varphi$ is smooth.
>
> *Lee: Theorem 9.12*

^thm-69-4

> [!proof]+ Proof
> *(1)* is Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]] above, proved in Lecture 24. The indication for (1) given in Lecture 23: by uniqueness and the translation lemma, which is easy, there is only one way to continue the curve forwards in time and then backwards in time until either it never stops or it runs into the edge of the manifold. Openness of $\mathcal{D}$ is surprisingly long to prove.
>
> *(2)* *(Lecture 25: not proved in detail in class. That $\mathcal{D}$ is open is the hard part and takes quite a bit of work; once it is known, smoothness follows from local ODE theory. Filled in, following Lee's proof of Theorem 9.12; the argument gives openness and smoothness together.)* Let $W$ be the set of $(t, p) \in \mathcal{D}$ that have a neighbourhood of the form $J \times U \subseteq \mathcal{D}$, with $J \subseteq \mathbb{R}$ an open interval containing $0$ and $t$ and $U \subseteq M$ open, on which $\varphi$ is smooth. Every point $(t', p')$ of such a $J \times U$ is again in $W$, with the same $J \times U$, since $J \ni 0, t'$. So $W$ is open in $\mathbb{R} \times M$, and $\varphi$ is smooth on $W$, smoothness being local. It suffices to show $W = \mathcal{D}$.
>
> By the flow boxes of Lemma [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]], every $p \in M$ has $\varepsilon > 0$ and an open $U \ni p$ with $(-\varepsilon, \varepsilon) \times U \subseteq W$. Suppose $(\tau, p_0) \in \mathcal{D} \setminus W$. Then $\tau \neq 0$; say $\tau > 0$ (for $\tau < 0$ the argument is the same, with the supremum of the times $t \le 0$ where $(t, p_0) \notin W$). Let
>
> $$
> t_0 = \inf\{ t \ge 0 : (t, p_0) \notin W \} .
> $$
>
> The flow box at $p_0$ gives $t_0 > 0$; and $t_0 \le \tau$, so $t_0$ lies in the interval $(\alpha(p_0), \beta(p_0))$, which contains $0$ and $\tau$. By the definition of $t_0$, $(t, p_0) \in W$ for $0 \le t < t_0$.
>
> Let $q_0 = \varphi(t_0, p_0)$, and take a flow box $(-\varepsilon, \varepsilon) \times U_0 \subseteq W$ at $q_0$. The curve $\varphi^{p_0}$ is continuous at $t_0$, so there is $t_1$ with $\max(0, t_0 - \varepsilon) < t_1 < t_0$ and $\varphi(t_1, p_0) \in U_0$. As $(t_1, p_0) \in W$, there is $J_1 \times U_1 \subseteq \mathcal{D}$ around it, with $J_1 \ni 0, t_1$, on which $\varphi$ is smooth; shrinking $U_1$, by continuity, $\varphi(\{t_1\} \times U_1) \subseteq U_0$.
>
> Fix $p \in U_1$ and let $q = \varphi_{t_1}(p) \in U_0$. The curve $t \mapsto \varphi_{t - t_1}(q)$ is defined for $|t - t_1| < \varepsilon$ (flow box at $q_0$), it is an integral curve (translation lemma), and at $t = t_1$ it equals $q = \varphi^p(t_1)$. By Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] it agrees with $\varphi^p$ on the common domain, and the two together form an integral curve starting at $p$ on the open interval $\tilde J = J_1 \cup (t_1 - \varepsilon, t_1 + \varepsilon)$. By Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]], $\tilde J \subseteq (\alpha(p), \beta(p))$ and this curve is $\varphi^p$. Hence $\tilde J \times U_1 \subseteq \mathcal{D}$, and
>
> $$
> \varphi(t, p) = \varphi\big(t - t_1, \varphi(t_1, p)\big) \qquad \text{for } (t, p) \in (t_1 - \varepsilon, t_1 + \varepsilon) \times U_1 ,
> $$
>
> a composite of smooth maps ($\varphi$ on $J_1 \times U_1$, then $\varphi$ on the flow box $(-\varepsilon, \varepsilon) \times U_0$). So $\varphi$ is smooth on the two open sets $J_1 \times U_1$ and $(t_1 - \varepsilon, t_1 + \varepsilon) \times U_1$, which cover $\tilde J \times U_1$. Now $\tilde J$ is an open interval containing $0$ and every $t \in [0, t_1 + \varepsilon)$, so $(t, p_0) \in W$ for all these $t$. As $t_1 + \varepsilon > t_0$, this contradicts the definition of $t_0$. Hence $W = \mathcal{D}$: $\mathcal{D}$ is open and $\varphi$ is smooth.

^pf-69-4

*Uses:* [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]], [[§69 Maximal Integral Curves and Flows#^lem-69-3|§69.3]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

![[m591-68-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* The flow of a complete field, the pendulum field $y\,\partial_x - \sin x\,\partial_y$ (chosen for the picture; gray: its integral curves), integrated numerically. A disc of initial points with a grid is carried along: each $\varphi_t$ moves it as a diffeomorphism would. Then flowing $1.2$ and then $s$ more (green) is compared with flowing $2.2$ at once (red dashed); at $s = 1$ they coincide, $\varphi_s \circ \varphi_t = \varphi_{s+t}$. The diffeomorphism property and this group law are Lee, Theorem 9.12, not yet in the notes.

$\varphi$ is just flowing along integral curves, as before, except that the domain of the time variable depends on the point, as in Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]. The theorem is the local picture of Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]], with its rectangles $(-\varepsilon, \varepsilon) \times U$, put together on the whole manifold. In the two examples:
- Rotation (Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]]): $\alpha \equiv -\infty$, $\beta \equiv +\infty$, $\mathcal{D} = \mathbb{R} \times \mathbb{R}^2$.
- Escape (Example [[§69 Maximal Integral Curves and Flows#^ex-69-1|§69.1]]): $\alpha \equiv -\infty$, $\beta(x, y) = 1/(xy)$, so $\mathcal{D} = \{ (t, (x, y)) : x, y > 0,\ t\,xy < 1 \}$, open, and $\varphi(t, (x, y)) = \big(x/(1 - xyt),\ y\big)$, smooth on $\mathcal{D}$.

The first property of the flow is the group law, which is easy to prove.

> [!theorem] Proposition §69.5: The Group Law
> Let $\mathbf{X} \in \mathfrak{X}(M)$, $p \in M$ and $s \in (\alpha(p), \beta(p))$, and put $q = \varphi_s(p)$. Then:
>
> 1. $(\alpha(q), \beta(q)) = (\alpha(p) - s, \beta(p) - s)$;
> 2. $\varphi_t(\varphi_s(p)) = \varphi_{t+s}(p)$ for every $t$ with $t + s \in (\alpha(p), \beta(p))$.
>
> *Lee: Theorem 9.12(b)*

^prop-69-5

> [!proof]+ Proof
> *(Lecture 25. On the board: fix $s$; $t \mapsto \varphi_t(\varphi_s(p))$ is an integral curve starting at $\varphi_s(p)$; so is $t \mapsto \varphi_{t+s}(p) = \varphi^p(t + s)$, by the translation lemma (the variable $t$ is translated by $s$); by uniqueness, these curves agree. The domains in (1) are filled in.)* Let
>
> $$
> c(t) = \varphi^p(t + s), \qquad t \in (\alpha(p) - s, \beta(p) - s).
> $$
>
> By the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)), $c$ is an integral curve of $\mathbf{X}$, and $c(0) = \varphi^p(s) = q$. So $c$ starts at $q$, and by Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]
>
> $$
> (\alpha(p) - s, \beta(p) - s) \subseteq (\alpha(q), \beta(q)) \qquad\text{and}\qquad \varphi^q(t) = \varphi^p(t + s) \ \text{ for } t \in (\alpha(p) - s, \beta(p) - s). \tag{$\ast\ast$}
> $$
>
> In particular $-s \in (\alpha(q), \beta(q))$ and $\varphi_{-s}(q) = \varphi^p(0) = p$. The same argument with $q$ and $-s$ in place of $p$ and $s$ gives $(\alpha(q) + s, \beta(q) + s) \subseteq (\alpha(p), \beta(p))$, that is, $(\alpha(q), \beta(q)) \subseteq (\alpha(p) - s, \beta(p) - s)$. This proves (1). Then (2) is $(\ast\ast)$: if $t + s \in (\alpha(p), \beta(p))$, then $\varphi_t(\varphi_s(p)) = \varphi^q(t) = \varphi^p(t + s) = \varphi_{t+s}(p)$.

^pf-69-5

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§69 Maximal Integral Curves and Flows#^prop-69-1|§69.1]]

> [!theorem] Corollary §69.6: Flows Commute with Themselves
> When $s$, $t$ and $s + t$ all lie in $(\alpha(p), \beta(p))$,
>
> $$
> \varphi_t\big(\varphi_s(p)\big) = \varphi_s\big(\varphi_t(p)\big) = \varphi_{t + s}(p) .
> $$

^cor-69-6

> [!proof]+ Proof
> Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]] for the pair $(s, t)$, and for the pair $(t, s)$, as $s + t = t + s$.

^pf-69-6

*Uses:* [[§69 Maximal Integral Curves and Flows#^prop-69-5|§69.5]]

The hypothesis that $s$, $t$ and $s + t$ lie in the domain is needed: with flows one always has to check where things are defined.

![[m591-69-4.svg]]

*(Not from lecture; figure added.)* The group law along one integral curve: flowing for time $s$ (red) and then for time $t$ (green) from where one has arrived lands at the same point as flowing for time $t + s$ from $p$ (dashed). The curve is a spiral, $\varphi^p(\tau) = 2.2\,e^{-0.12\tau}(\cos\tau, \sin\tau)$, chosen for the picture.

![[m591-69-a1.gif|560]]

*(Not from lecture; animation added, vault only.)* The group law as an identity of maps. A disc of initial points under the spiral flow $\dot x = -0.12x - y$, $\dot y = x - 0.12y$ (chosen for the picture). Left, $\varphi_t \circ \varphi_s$: the disc flows for time $s = 1.7$ (red trail), then the clock is restarted and it flows for time $t = 1.9$ (green). Right, $\varphi_{t+s}$: one clock runs for $3.6$. Both end in the same place.
