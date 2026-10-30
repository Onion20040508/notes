---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 10
section: 68
tags: [differentiable-manifolds, math591]
---
← [[§67 Integral Curves]] · ↑ [[· 10 Integral Curves and Flows]] · [[§69 Maximal Integral Curves and Flows]] →

*Stage: dynamics — Integral curves exist and are unique for short times: in $\mathbb{R}^m$ by ODE theory, on a manifold through a chart; two integral curves that meet agree on their whole common domain.*

“There's a fundamental theorem that, again, from — we have moved from Calc 3 to Calc 4 — ODEs.” Uribe quoted it in the following form.

> [!theorem] Theorem §68.1: Local Existence and Uniqueness in Euclidean Space
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

^thm-68-1

> [!proof]+ Proof (not given in this course)
> Taken from ODE theory, not proved in the course: “a big, big theorem that takes forever to prove”, the theorem on existence, uniqueness and smooth dependence on initial conditions (Lee, Theorem D.1, proved in Appendix D). “This theorem here packs everything that we will quote from the Euclidean case.”

^pf-68-1

Items (1) and (2) together are *existence*: every $q \in U$ has an integral curve $\varphi(\cdot, q)$ starting at $q$, all defined on the same interval $(-\varepsilon, \varepsilon)$; the smoothness of $\varphi$ in the pair $(t, q)$ is *smooth dependence on the initial condition*. Item (3) is *uniqueness*, on a par with existence; on the board it came as an addition, “Furthermore (still the Euclidean theorem).”

![[m591-67-1.svg]]

“Imagine a Calc 3 plot of a field … the vectors at every point.” The theorem gives a time interval $(-\varepsilon, \varepsilon)$ and a neighbourhood $U$ of $p$ (drawn as a rectangle) such that from every point $q \in U$, $p$ included, there is an integral curve $t \mapsto \varphi(t, q)$ that starts at $q$ and is defined at least for $|t| < \varepsilon$.

*What the theorem says beyond “there is a path through $q$”* (a student's question). “It says a lot of delicate things.” The time interval is *uniform*: as long as $q \in U$, the curve is defined at least for $|t| < \varepsilon$. And $\varphi$ is smooth as a function of the pair $(t, q)$ on the product $(-\varepsilon, \varepsilon) \times U$: smooth in $t$, as an integral curve must be, but also, for fixed $t$, smooth in the initial condition $q$. Asked whether the image of $\varphi$ is “just a slightly bigger open set around $U$”, Uribe answered: “All of the above can happen.” The examples below show some of the possibilities.

> [!definition] Definition §68.1: Notation: $\varphi_t$ and $\varphi_q$
> In the setting of Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]], and likewise of Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]] below, for fixed $t \in (-\varepsilon, \varepsilon)$ and fixed $q \in U$ write
>
> $$
> \varphi_t(q) := \varphi(t, q), \qquad \varphi_q(t) := \varphi(t, q).
> $$
>
> Then $\varphi_t : U \to M$ is a smooth map, and $\varphi_q : (-\varepsilon, \varepsilon) \to M$ is the integral curve of $\mathbf{X}$ with $\varphi_q(0) = q$: it “starts at $q$”.
>
> *Lee: Ch. 9, Flows*

^def-68-1

“This notation is useful when you want to fix $t$.” For the second one: “we don't use it, but I suppose we could … maybe we should use it. It sounds pedagogical. I actually like it.” The board then used it. The two notations differ only in the letter in the subscript, so whether $\varphi_s$ means a map or a curve is read off from what $s$ is: a time or a point. Lee writes $\theta_t(p)$ and $\theta^{(p)}(t)$ for the two (Chapter 9). In these notes $\varphi$ also names charts $(U, \varphi)$; from here on it is the flow unless a chart is named.

> [!example] Example §68.1: The Rotation Field
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

^ex-68-1

“The harmonic oscillator, or rotation, whatever you want”; “everybody has solved this some time, either in an ODE class or in a physics class.” It is “the benign case”: in Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]] one can take $U = \mathbb{R}^2$ and any $\varepsilon$, indeed $t \in \mathbb{R}$. Going back to the question about the image, $\varphi_t(U)$ is $U$ rotated about the origin, possibly far from $U$.

![[m591-67-2.svg]]

![[m591-67-a1.gif|420]]

*(Not from lecture; animation added, vault only.)* The flow of the rotation field, $t$ from $0$ to $2\pi$. A disc $U$ of initial points (coloured by their initial $x$-coordinate, so that its orientation is visible) is carried along the dashed circles, the integral curves: $\varphi_t(U)$ is $U$ rotated by the angle $t$, and at $t = 2\pi$ every point is back where it started. The red point is the centre, $\varphi_t(1.2, 0) = (1.2\cos t,\ 1.2\sin t)$.

*Lecture 24. The definition again, then the local theorem on a manifold, two “simple and useful lemmas”, and uniqueness on the whole common domain: “the deep — meaning foundational — theory of the subject.” The definition and the lemmas are in [[§67 Integral Curves|§67]].*

The Euclidean theorem (Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]]) is “Theorem D.1 in Lee, with proof. I will forever be amazed by how much [Lee] was able to put in his book.” Its manifold version “follows immediately from the Euclidean version.”

> [!theorem] Theorem §68.2: Local Existence and Uniqueness on a Manifold
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
> 3. *(local uniqueness)* if $c : I \to M$ is any integral curve of $\mathbf{X}$ on an open interval $I \ni 0$ with $c(0) = q$ for some $q \in U$, then $c(t) = \varphi_t(q)$ for all $t \in I \cap (-\varepsilon, \varepsilon)$.
>
> Moreover, $\varphi$ is smooth.
>
> *Lee: Proposition 9.2; Theorem D.1*

^thm-68-2

On the board, (3) was stated for $c : (-\delta, \delta) \to M$, with the conclusion on $(-\varepsilon, \varepsilon) \cap (-\delta, \delta)$; “these domains don't have to be symmetric”, which is the form of (3) above. By (3), “there's only one map like that.”

> [!proof]+ Proof
> *(Lecture 24: “use a chart at $p$, and then push forward … push this thing down here. Now we have the theorem at the level of open sets in Euclidean space, and we just push it up again.” The chart is called $\psi$, since $\varphi$ is the flow — “which is why Lee uses $\theta$.” The details are filled in.)* When $M$ is an open set in $\mathbb{R}^m$ this is Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]]. In general, take a chart $\psi : W \to \psi(W) \subseteq \mathbb{R}^m$ at $p$. It is a diffeomorphism of the open submanifold $W$ onto the open set $\psi(W)$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), so the field $\mathbf{X}|_W$ has a pushforward $\mathbf{Y} = \psi_\ast\mathbf{X} \in \mathfrak{X}(\psi(W))$ (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]], Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]).
>
> *The check.* By Lemma [[§67 Integral Curves#^lem-67-5|§67.5]], applied to the diffeomorphism $\psi : W \to \psi(W)$, a curve $c : I \to W$ is an integral curve of $\mathbf{X}$ if and only if $\psi \circ c$ is an integral curve of $\mathbf{Y}$.
>
> *Push down, solve, push up.* Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]], for $\mathbf{Y}$ on $\psi(W)$ at $\psi(p)$, gives $\varepsilon > 0$, an open $U' \ni \psi(p)$ and a smooth $\varphi' : (-\varepsilon, \varepsilon) \times U' \to \psi(W)$. Put $U = \psi^{-1}(U')$ and
>
> $$
> \varphi(t, q) = \psi^{-1}\big(\varphi'(t, \psi(q))\big) \in W .
> $$
>
> $\varphi$ is smooth, as a composite of smooth maps, and $\varphi(0, q) = \psi^{-1}(\psi(q)) = q$. For $q \in U$ the curve $t \mapsto \varphi'(t, \psi(q))$ is an integral curve of $\mathbf{Y}$ in $\psi(W)$, so by the check, applied to $c = \varphi(\cdot, q)$ (for which $\psi \circ c = \varphi'(\cdot, \psi(q))$), $t \mapsto \varphi_t(q)$ is an integral curve of $\mathbf{X}$. This gives (1) and (2).
>
> *Uniqueness.* The one point beyond pushing down is that an integral curve $c$ of $\mathbf{X}$ might leave $W$, where the chart says nothing. Let $c : I \to M$ be an integral curve, $I \ni 0$ an open interval, $c(0) = q \in U$, and let $J = I \cap (-\varepsilon, \varepsilon)$. The set $c^{-1}(W) \cap J$ is open and contains $0$; let $J_0$ be the open interval that is its connected component containing $0$. On $J_0$, $\psi \circ c$ is an integral curve of $\mathbf{Y}$ starting at $\psi(q)$ (the check), so Theorem [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]](3) gives $\psi(c(t)) = \varphi'(t, \psi(q))$, that is, $c(t) = \varphi(t, q)$, for $t \in J_0$. Suppose $J_0 \neq J$, say $b = \sup J_0 < \sup J$ (the left end is handled the same way). Then $b \in J$, and by continuity $c(b) = \lim_{t \to b^-} \varphi(t, q) = \varphi(b, q)$, which lies in $W$. So $b \in c^{-1}(W) \cap J$, an open set; an interval around $b$ lies in it, and the component $J_0$ would contain $b$ and points beyond it, contradicting $b = \sup J_0$. Hence $J_0 = J$, and $c(t) = \varphi_t(q)$ on all of $I \cap (-\varepsilon, \varepsilon)$: this is (3).

^pf-68-2

*Uses:* [[§68 Local Existence and Uniqueness#^thm-68-1|§68.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§59 Related Vector Fields#^prop-59-2|§59.2]], [[§67 Integral Curves#^lem-67-5|§67.5]]

![[m591-67-7.svg]]

*(Figure after the board.)* Upstairs, the field $\mathbf{X}$ on the chart domain $W$ and a curve $c$; downstairs, the pushed-forward field $\psi_\ast\mathbf{X}$ on $\psi(W)$ and the curve $\psi \circ c$.

“Now the core technical result that I want to prove today.”

> [!theorem] Proposition §68.3: Uniqueness on the Common Domain
> Let $\mathbf{X} \in \mathfrak{X}(M)$, and let $c_i : I_i \to M$, $i = 1, 2$, be integral curves of $\mathbf{X}$. If there is $t_0 \in I_1 \cap I_2$ with $c_1(t_0) = c_2(t_0)$, then
>
> $$
> c_1|_{I_1 \cap I_2} = c_2|_{I_1 \cap I_2} .
> $$
>
> *Lee: Theorem 9.12 (proof)*

^prop-68-3

“Suppose you have two integral curves that agree at some time $t_0$ … Then the conclusion is that they agree wherever they can.”

> [!proof]+ Proof
> *(Lecture 24. Details from the discussion in class are added where noted.)* *Reduction to $t_0 = 0$.* By the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)), $t \mapsto c_i(t + t_0)$ are integral curves on $I_i - t_0$ that agree at $0$, and the conclusion for them is the conclusion for the $c_i$. So assume $t_0 = 0$, and let $q = c_1(0) = c_2(0)$.
>
> *Local uniqueness.* By Theorem [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]](3) at $q$, both $c_i$ equal $\varphi_\cdot(q)$ near $0$. So there is $\varepsilon > 0$ with $(-\varepsilon, \varepsilon) \subseteq I_1 \cap I_2$ and
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
> *Negative times.* “Of course you do the same thing for $\tau_-$ from the other side. You take the sup”: with $\mathcal{T}_- = \{ t \in I_1 \cap I_2 \cap (-\infty, 0) : c_1(t) \neq c_2(t) \}$ and $\sup \mathcal{T}_-$, or apply the above to $t \mapsto c_i(-t)$, integral curves of $-\mathbf{X}$ (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](2)). With $c_1(0) = c_2(0)$, the curves agree on all of $I_1 \cap I_2$.

^pf-68-3

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^thm-68-2|§68.2]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]]

![[m591-67-9.svg]]

*(Figure after the board.)* The situation the claim rules out: the curves agree on $(0, \tau)$ and differ at $\tau$, with disjoint neighbourhoods $U_1, U_2$. “When you do elementary Euclidean geometry and argue by contradiction, every picture that you draw doesn't look contradictory, because the thing is true.” A student noted that the argument is “very similar” to the Euclidean one; Uribe agreed. Another student asked how $J$ stays inside $I_1 \cap I_2$; it does because the domains are open intervals.

> [!remark] Remark: Where the Hausdorff Property Is Used
> *(Filled in.)* The claim $c_1(\tau) = c_2(\tau)$ is the one step of the proof that uses that $M$ is Hausdorff (“since $M$ is $T_2$” on the board): it says that the set of times where the two curves agree is closed in $I_1 \cap I_2$. Without the Hausdorff property the proposition fails. The line with two origins ([[§10 The Line with Two Origins|§10]]), two copies $\mathbb{R} \times \{1\}$ and $\mathbb{R} \times \{2\}$ glued along $x \neq 0$, has smooth charts (each copy) but is not Hausdorff. The field $d/dx$, in either chart, is well defined, and $c_i(t) = (t, i)$, $t \in \mathbb{R}$, $i = 1, 2$, are integral curves of it. They agree at every $t \neq 0$ and differ at $t = 0$, where they pass through the two different origins.

^rem-68-1

> [!theorem] Corollary §68.4: Non-Injective Integral Curves Repeat
> Let $c : I \to M$ be an integral curve of $\mathbf{X} \in \mathfrak{X}(M)$, and suppose $c(t_1) = c(t_2)$ for some $t_1 < t_2$ in $I$. Put $T = t_2 - t_1 > 0$. Then
>
> $$
> c(t + T) = c(t) \qquad \text{for every } t \in I \text{ with } t + T \in I .
> $$
>
> *Lee: Problem 9-1*

^cor-68-4

> [!proof]+ Proof
> *(Uribe, by email after Lecture 24: “I realized that I did not really answer today's question of whether integral curves must be injective. The answer is that if an integral curve is not injective, then it must be periodic.”)* By the translation lemma (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)), the curve $g(t) = c(t + T)$, defined on $I - T$, is an integral curve of the same field. Both $c$ and $g$ are defined at $t_1$: $t_1 \in I$, and $t_1 \in I - T$ because $t_1 + T = t_2 \in I$. There they agree:
>
> $$
> g(t_1) = c(t_1 + T) = c(t_2) = c(t_1) .
> $$
>
> Therefore, by uniqueness (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), $g = c$ on $I \cap (I - T)$, that is, $c(t + T) = c(t)$ for every $t \in I$ with $t + T \in I$.

^pf-68-4

*Uses:* [[§67 Integral Curves#^lem-67-4|§67.4]], [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]

“Note that $T$ may not be the smallest period.” For the rotation field (Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]]), the integral curve $c(t) = (\cos t, \sin t)$ has $c(0) = c(4\pi)$, so $T = 4\pi$ is a period, while the smallest period is $2\pi$. A constant curve, at a zero of $\mathbf{X}$, is periodic with every $T > 0$. *(Filled in.)* The email says $c(t + T) = c(t)$ “for all $t$”. For a curve on a bounded interval the corollary only covers the $t$ with both $t$ and $t + T$ in $I$; for the maximal integral curve the domain is then all of $\mathbb{R}$, and the identity holds for every $t$ (Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-2|§69.2]]).

> [!remark] Remark: Must an Integral Curve Be Injective?
> A student asked this in Lecture 24, after Example [[§67 Integral Curves#^ex-67-1|§67.1]]. “We're about to prove something related … except if it's constant”: at a zero of $\mathbf{X}$ the constant curve is an integral curve. The “something related” is Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]. *(Filled in.)* Constant curves are not the only exception: the circles of the rotation field (Example [[§68 Local Existence and Uniqueness#^ex-68-1|§68.1]]) are integral curves that return to the same point with the same velocity, every $2\pi$. Uribe answered the question by email after the lecture: “if an integral curve is not injective, then it must be periodic” (Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]]; for the maximal curve, Proposition [[§69 Maximal Integral Curves and Flows#^prop-69-2|§69.2]]). Lee shows that a maximal integral curve is exactly one of: constant, injective, or periodic and nonconstant (Lee, Problem 9-1).

^rem-68-2

![[m591-67-5.svg]]

*(Not from lecture; figure added.)* The three kinds of maximal integral curve (Lee, Problem 9-1). An integral curve that comes back to a point comes back with the same velocity, the value of the field there; by Corollary [[§68 Local Existence and Uniqueness#^cor-68-4|§68.4]] it then repeats itself. The loop of the previous figure, which comes back with a different velocity, is none of the three: it is not an integral curve.

> [!example] Example §68.2: The Euler Field
> On $\mathbb{R}^2$ let $\mathbf{X} = x\, \dfrac{\partial}{\partial x} + y\, \dfrac{\partial}{\partial y}$. The integral curves solve $\dot x = x$, $\dot y = y$, so $\varphi_t(x_0, y_0) = e^t(x_0, y_0)$, $t \in \mathbb{R}$. For $(x_0, y_0) \neq 0$ the image is the open ray from the origin through $(x_0, y_0)$, since $e^t$ takes every value in $(0, \infty)$ and never $0$; at the origin the integral curve is constant.

^ex-68-2

![[m591-67-10.svg]]

“If you go to Desmos or whatever, you see the integral curves of the Euler field … on $\mathbb{R}^2$ radial, like that, and they seem to intersect, but they don't.” The rays are open, and the origin is its own integral curve. The images of the integral curves $t \mapsto e^t(x_0, y_0)$, $t \in \mathbb{R}$, partition $\mathbb{R}^2$, as Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]] requires. *(Filled in.)* If two of them pass through a common point, $c_1(t_1) = c_2(t_2)$, then $t \mapsto c_2(t + t_2 - t_1)$ is an integral curve (Lemma [[§67 Integral Curves#^lem-67-4|§67.4]](1)) that agrees with $c_1$ at time $t_1$, so it equals $c_1$ on $\mathbb{R}$ (Proposition [[§68 Local Existence and Uniqueness#^prop-68-3|§68.3]]), and the two images coincide.
