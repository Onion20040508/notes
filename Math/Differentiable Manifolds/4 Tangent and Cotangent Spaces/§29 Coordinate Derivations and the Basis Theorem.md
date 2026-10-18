---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 29
tags: [differentiable-manifolds, math591]
---
← [[§28 Derivations and the Abstract Tangent Space]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§30 The Differential in Coordinates]] →

*Stage: abstract — Charts give derivations $\partial/\partial x^i|_p$, and they form a basis of $T_pM$: $\dim T_pM = \dim M$. The proof needs Taylor's theorem with a smooth remainder.*

> [!definition] Definition §29.1: Coordinate Functions of a Chart
> Let $M$ be a smooth $n$-manifold.
> 1. The **standard coordinate functions** on $\mathbb{R}^n$ are the projections
>
> $$
> r^i : \mathbb{R}^n \to \mathbb{R}, \qquad r^i(a^1, \ldots, a^n) = a^i, \qquad i = 1, \ldots, n.
> $$
>
> 2. For a smooth chart $(U, \varphi)$, the **coordinate functions of the chart**, or **local coordinates** on $U$, are
>
> $$
> x^i := r^i \circ \varphi : U \to \mathbb{R}, \qquad\text{so that}\qquad \varphi = (x^1, \ldots, x^n), \quad\text{i.e. } \varphi(q) = \big(x^1(q), \ldots, x^n(q)\big).
> $$
>
> 3. For a function $f$ defined on $U$, its **coordinate representation** in the chart is $f_\varphi = f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$, as in Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]; thus $f = f_\varphi \circ \varphi$ on $U$. In particular $(x^i)_\varphi = r^i \circ \varphi \circ \varphi^{-1} = r^i$ on $\varphi(U)$.
>
> *Lee: Ch. 1, Coordinate Charts*

^def-29-1

> [!remark] Remark
> **A notational discipline.** Uribe stopped to insist on this. The $x^i$ live *upstairs*, as functions on the manifold, and the $r^i$ *downstairs*, as functions on $\mathbb{R}^n$; conflating them is the main source of confusion in what follows. The identity $(x^i)_\varphi = r^i$ is the bridge between the two rows: it says that the coordinate functions, written in their own chart, are the standard coordinates. It also shows that each $x^i$ is a smooth function on $U$, by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]], since $r^i$ is smooth.

^rem-29-1

![[m591-12-6.svg]]
*The board diagram for this section. Both triangles commute: the left one says $f = f_\varphi \circ \varphi$, which is what smoothness of $f$ means; the right one is the* definition *$x^i = r^i \circ \varphi$ of the $i$-th coordinate function on $U$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]). Everything upstairs is expressed downstairs by composing with $\varphi$, and the derivation about to be defined does its differentiating entirely on the bottom row, where partial derivatives already make sense.*

> [!definition] Definition §29.2: Coordinate Derivations
> Let $(U,\varphi)$ be a smooth chart with $p \in U$, with coordinate functions $x^1, \ldots, x^n$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), and let $i \in \{1,\ldots,n\}$. Define $\dfrac{\partial}{\partial x^i}\Big|_p : C_p^\infty(M) \to \mathbb{R}$ by
>
> $$
> \frac{\partial}{\partial x^i}\Big|_p [f] \;:=\; \frac{\partial f_\varphi}{\partial r^i}\big(\varphi(p)\big),
> $$
>
> the ordinary $i$-th partial derivative at $\varphi(p)$ of the coordinate representation $f_\varphi = f \circ \varphi^{-1}$. For a function $f$ smooth near $p$ we also write
>
> $$
> \frac{\partial f}{\partial x^i}(p) \;:=\; \frac{\partial}{\partial x^i}\Big|_p [f] \;=\; \frac{\partial f_\varphi}{\partial r^i}\big(\varphi(p)\big),
> $$
>
> the **partial derivative** of $f$ with respect to the coordinate $x^i$. It is defined by going downstairs: there is no other way to differentiate a function on a manifold with respect to a coordinate.
>
> *Lee: Ch. 3, Computations in Coordinates*

^def-29-2

> [!theorem] Lemma §29.1: Partial Derivatives of a Smooth Function Are Smooth
> Let $(U, \varphi = (x^1, \ldots, x^n))$ be a smooth chart of $M$ and $f : U \to \mathbb{R}$ smooth, $f \in C^\infty(U)$ — for instance the restriction to $U$ of a smooth function on $M$. For each $j$, the function $\partial f/\partial x^j : U \to \mathbb{R}$, $q \mapsto \partial f/\partial x^j(q)$, satisfies
>
> $$
> \frac{\partial f}{\partial x^j} \circ \varphi^{-1} = \frac{\partial f_\varphi}{\partial r^j} \qquad \text{on } \varphi(U),
> $$
>
> and it is smooth: $\partial f/\partial x^j \in C^\infty(U)$.

^lem-29-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* The open set $U$ is a smooth manifold whose smooth charts are the smooth charts of $M$ with domain in $U$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]]); in particular $(U, \varphi)$ is a smooth chart of $U$. Two things are claimed: the identity of functions on $\varphi(U)$, and the smoothness of $\partial f/\partial x^j$.
>
> *The identity.* By Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], applied to the smooth function $f$ on the manifold $U$ and its smooth chart $(U, \varphi)$, the coordinate representation $f_\varphi = f \circ \varphi^{-1}$ is smooth on $\varphi(U)$. So $f$ is smooth near every $q \in U$, and $\partial f/\partial x^j(q)$ is defined (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]). For $r \in \varphi(U)$, Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] at the point $q = \varphi^{-1}(r)$ gives
>
> $$
> \Big(\frac{\partial f}{\partial x^j} \circ \varphi^{-1}\Big)(r) = \frac{\partial f}{\partial x^j}\big(\varphi^{-1}(r)\big) = \frac{\partial f_\varphi}{\partial r^j}\big(\varphi(\varphi^{-1}(r))\big) = \frac{\partial f_\varphi}{\partial r^j}(r) .
> $$
>
> *Smoothness.* $f_\varphi$ is smooth on the open set $\varphi(U)$, so its partial derivative $\partial f_\varphi/\partial r^j$ is smooth too: every partial derivative of it, of any order, is a partial derivative of $f_\varphi$, hence exists and is continuous. By the identity, $\partial f_\varphi/\partial r^j$ is the coordinate representation of $\partial f/\partial x^j$ in the chart $(U, \varphi)$, which contains every point of $U$; so $\partial f/\partial x^j$ is smooth on $U$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]).

^pf-29-1

*Uses:* [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]]

> [!theorem] Proposition §29.2: Coordinate Derivations Are Derivations
> $\dfrac{\partial}{\partial x^i}\Big|_p$ is well defined on germs and is a derivation at $p$.

^prop-29-2

> [!proof]+ Proof
> *(Lecture 8: “it's linear, and the product rule will be inherited from the product rule of the ordinary partial derivatives” — the *Linear* and *Leibniz* steps below. Well-definedness is filled in.)*
>
> Three things are to be shown: the value $\partial f_\varphi/\partial r^i(\varphi(p))$ does not depend on the representative of $[f]$; the resulting map is linear; and it satisfies the Leibniz rule of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]. For a representative $(f, U_1)$, $f_\varphi = f \circ \varphi^{-1}$ is defined on the open set $\varphi(U \cap U_1) \ni \varphi(p)$ and smooth there (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], applied on the open set $U \cap U_1$ with the restricted chart, a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)), so its partial derivatives at $\varphi(p)$ exist.
>
> *Well defined.* If $(f,U_1) \sim (g,U_2)$, then $f = g$ on an open $W \ni p$ (Definition [[§27 Germs#^def-27-1|§27.1]]), so $f_\varphi = g_\varphi$ on the open set $\varphi(W \cap U) \ni \varphi(p)$ (open because $\varphi$ is a homeomorphism onto the open set $\varphi(U)$); partial derivatives at a point depend only on the function near that point, being limits of difference quotients that only use values in arbitrarily small neighbourhoods, so the two values agree. (Shrinking the chart domain also changes nothing, for the same reason.)
>
> *Linear.* $(\lambda f + g)_\varphi = \lambda f_\varphi + g_\varphi$ near $\varphi(p)$, since both sides take the value $\lambda f(\varphi^{-1}(r)) + g(\varphi^{-1}(r))$ at $r$; and partial differentiation is linear. So, by Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] at both ends,
>
> $$
> \frac{\partial}{\partial x^i}\Big|_p\big(\lambda[f] + [g]\big) = \frac{\partial (\lambda f + g)_\varphi}{\partial r^i}(\varphi(p)) = \lambda\,\frac{\partial f_\varphi}{\partial r^i}(\varphi(p)) + \frac{\partial g_\varphi}{\partial r^i}(\varphi(p)) = \lambda\,\frac{\partial}{\partial x^i}\Big|_p[f] + \frac{\partial}{\partial x^i}\Big|_p[g] .
> $$
>
> *Leibniz.* $(fg)_\varphi = f_\varphi\, g_\varphi$ near $\varphi(p)$, since $(fg)(\varphi^{-1}(r)) = f(\varphi^{-1}(r))\, g(\varphi^{-1}(r))$, so by the ordinary product rule at $\varphi(p)$,
>
> $$
> \frac{\partial (fg)_\varphi}{\partial r^i}(\varphi(p)) = f_\varphi(\varphi(p))\,\frac{\partial g_\varphi}{\partial r^i}(\varphi(p)) + g_\varphi(\varphi(p))\,\frac{\partial f_\varphi}{\partial r^i}(\varphi(p)),
> $$
>
> and $f_\varphi(\varphi(p)) = f(\varphi^{-1}(\varphi(p))) = f(p)$, $g_\varphi(\varphi(p)) = g(p)$. By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] the left side is $\partial/\partial x^i|_p([f][g])$ and the two partial derivatives on the right are $\partial/\partial x^i|_p[g]$ and $\partial/\partial x^i|_p[f]$, so
>
> $$
> \frac{\partial}{\partial x^i}\Big|_p\big([f][g]\big) = f(p)\,\frac{\partial}{\partial x^i}\Big|_p[g] + g(p)\,\frac{\partial}{\partial x^i}\Big|_p[f],
> $$
>
> which is the Leibniz rule.

^pf-29-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-1|§19.1]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]]

The proof of the Basis Theorem below needs a form of Taylor expansion whose remainder is not an estimate but an exact, *smooth* term — “a theorem from calculus” that is not usually taught there. It is built in two steps: first order, then the first-order statement applied again.

> [!theorem] Lemma §29.3: Hadamard's Lemma
> Let $W \subseteq \mathbb{R}^n$ be open, $a = (a^1,\ldots,a^n) \in W$, $f : W \to \mathbb{R}$ smooth, and $B \subseteq W$ an open ball centred at $a$. Then there are smooth functions $f_1, \ldots, f_n$ on $B$ with
>
> $$
> f(r) = f(a) + \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f}{\partial r^i}(a) .
> $$
>
> Explicitly, $f_i(r) = \displaystyle\int_0^1 \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt$.
>
> *Lee: cf. Theorem C.15, used in the proof of Proposition 3.2*

^lem-29-3

> [!proof]+ Proof
> *(Lecture 9: “the proof is delightfully simple.”)* Fix $r \in B$. The segment $t \mapsto a + t(r - a)$, $t \in [0,1]$, runs from $a$ to $r$ and stays in $B$, a ball being convex. Put $h(t) = f\big(a + t(r-a)\big)$. It is defined on the set of $t$ with $a + t(r-a) \in W$, which is open (the preimage of the open $W$ under a continuous map) and contains $[0,1]$, hence also open intervals around $0$ and $1$, hence an open interval containing $[0,1]$; there $h$ is smooth, as the composite of $f$ with an affine map. By the fundamental theorem of calculus, $f(r) - f(a) = h(1) - h(0) = \int_0^1 h'(t)\, dt$, and by the chain rule, since $\frac{d}{dt}\big(a^i + t(r^i - a^i)\big) = r^i - a^i$,
>
> $$
> h'(t) = \sum_{i=1}^n \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\,(r^i - a^i) .
> $$
>
> Hence
>
> $$
> f(r) - f(a) = \int_0^1 \frac{d}{dt} f\big(a + t(r-a)\big)\, dt = \int_0^1 \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt = \sum_{i=1}^n (r^i - a^i)\, f_i(r),
> $$
>
> the factors $r^i - a^i$ coming out of the integral because they do not depend on $t$ (linearity of the integral), and $f_i$ being the integral of the statement. Adding $f(a)$ to both sides gives the identity.
>
> *Smoothness.* Each $f_i$ is smooth on $B$: the integrand $(t, r) \mapsto \partial f/\partial r^i\big(a + t(r-a)\big)$ is the composite of the smooth map $(t,r) \mapsto a + t(r-a)$ with the smooth function $\partial f/\partial r^i$, so it is smooth in $(t, r)$ on an open set containing $[0,1] \times B$, and all its partial derivatives in $r$ are continuous there; so differentiation under the integral sign over the compact interval $[0,1]$ is legitimate to every order.
>
> *Value at $a$.* At $r = a$ the integrand is constant: $a + t(a - a) = a$ for every $t$, so the integrand is the number $\partial f/\partial r^i(a)$, and
>
> $$
> f_i(a) = \int_0^1 \frac{\partial f}{\partial r^i}(a)\, dt = \frac{\partial f}{\partial r^i}(a) .
> $$

^pf-29-3

*Uses:* [[Fundamental Theorem of Calculus|451 §34.1]], [[Multivariable Chain Rule|452 §12.2]]

**Transcription note.** In Lecture 9 the path in the integral was first written with the wrong endpoints; a student corrected it to the convex combination $t(r - a) + a$, which runs from $a$ at $t = 0$ to $r$ at $t = 1$, as above.

Uribe called the proof “delightfully simple.” A student corrected the path on the board: it must be the segment $a + t(r - a)$, equal to $a$ at $t = 0$ and to $r$ at $t = 1$. Convexity of $B$ is what the proof uses — “everything is local,” but the neighbourhood must contain the segment from $a$ to each of its points, which is why a ball (or any set star-shaped about $a$) is taken.

> [!theorem] Lemma §29.4: Taylor–Hadamard
> In the setting of Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]], there are smooth functions $f_{ij}$ on $B$, $1 \le i, j \le n$, with
>
> $$
> f(r) \;=\; f(a) \;+\; \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}(a) \;+\; \sum_{i,j=1}^n (r^i - a^i)(r^j - a^j)\, f_{ij}(r) \qquad (r \in B),
> $$
>
> and $f_{ij}(a) = \tfrac12\, \dfrac{\partial^2 f}{\partial r^i\,\partial r^j}(a)$. This is an identity, not an approximation.
> In matrix form, with $r - a$ written as a column, the quadratic term is
>
> $$
> \sum_{i,j=1}^n (r^i - a^i)(r^j - a^j)\, f_{ij}(r) = (r - a)^{\mathsf T} \begin{pmatrix} f_{11}(r) & \cdots & f_{1n}(r) \\ \vdots & \ddots & \vdots \\ f_{n1}(r) & \cdots & f_{nn}(r) \end{pmatrix} (r - a),
> $$
>
> and at $r = a$ the $n \times n$ matrix of the $f_{ij}$ is half the Hessian of $f$:
>
> $$
> \begin{pmatrix} f_{11}(a) & \cdots & f_{1n}(a) \\ \vdots & \ddots & \vdots \\ f_{n1}(a) & \cdots & f_{nn}(a) \end{pmatrix} = \frac12 \begin{pmatrix} \dfrac{\partial^2 f}{\partial r^1\,\partial r^1}(a) & \cdots & \dfrac{\partial^2 f}{\partial r^1\,\partial r^n}(a) \\ \vdots & \ddots & \vdots \\ \dfrac{\partial^2 f}{\partial r^n\,\partial r^1}(a) & \cdots & \dfrac{\partial^2 f}{\partial r^n\,\partial r^n}(a) \end{pmatrix} .
> $$
>
> *Lee: cf. Theorem C.15*

^lem-29-4

> [!proof]+ Proof
> *(Lecture 9, exactly: first order, then “apply the claim to each $f_i$” and substitute back. Uribe wrote the quadratic term with a factor $\tfrac12$ — “doesn't matter” — which the notes absorb into $f_{ij}$; the value of $f_{ij}(a)$ at the end is a completion, the lecture needing only that the $f_{ij}$ are smooth.)*
>
> *Two applications of Hadamard.* Apply Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] to $f$, obtaining smooth $f_1, \ldots, f_n$ on $B$ with
>
> $$
> f(r) = f(a) + \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f}{\partial r^i}(a) .
> $$
>
> Then apply it again to each $f_i$, now with the open set $B$ in place of $W$ and the same ball $B$ (which is centred at $a$), obtaining smooth $f_{ij}$ on $B$ with $f_{ij}(a) = \partial f_i/\partial r^j(a)$ and
>
> $$
> f_i(r) = f_i(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r) = \frac{\partial f}{\partial r^i}(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r),
> $$
>
> the second equality by the value $f_i(a)$ from the first application.
>
> *Substitution.* Substituting this into $f(r) = f(a) + \sum_i (r^i - a^i) f_i(r)$ and multiplying out gives the identity:
>
> $$
> f(r) = f(a) + \sum_{i=1}^n (r^i - a^i)\Big(\frac{\partial f}{\partial r^i}(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r)\Big) = f(a) + \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}(a) + \sum_{i,j=1}^n (r^i - a^i)(r^j - a^j)\, f_{ij}(r) .
> $$
>
> *The value at $a$.* By Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]] applied to $f_i$, $f_{ij}(a) = \partial f_i/\partial r^j(a)$. Differentiate the integral formula $f_i(r) = \int_0^1 \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt$ under the integral sign (legitimate, as in the proof of Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]). By the chain rule, since $\partial\big(a^k + t(r^k - a^k)\big)/\partial r^j = t\,\delta^k_j$, the $r^j$-derivative of the integrand is $\sum_k \frac{\partial^2 f}{\partial r^k\,\partial r^i}\big(a + t(r-a)\big)\, t\,\delta^k_j = t\, \frac{\partial^2 f}{\partial r^j\,\partial r^i}\big(a + t(r-a)\big)$. At $r = a$ the second derivative is the constant $\frac{\partial^2 f}{\partial r^j\,\partial r^i}(a)$, and $\int_0^1 t\, dt = \tfrac12$; the order of the two partial derivatives does not matter, $f$ being smooth (equality of mixed partials). So
>
> $$
> \frac{\partial f_i}{\partial r^j}(r) = \int_0^1 t\, \frac{\partial^2 f}{\partial r^j\,\partial r^i}\big(a + t(r-a)\big)\, dt, \qquad\text{so}\qquad \frac{\partial f_i}{\partial r^j}(a) = \frac{\partial^2 f}{\partial r^j\,\partial r^i}(a) \int_0^1 t\, dt = \frac12\, \frac{\partial^2 f}{\partial r^i\,\partial r^j}(a).
> $$

^pf-29-4

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]

> [!remark]- Connections
> - Taylor's theorem with an estimated remainder: [[Multivariable Taylor's Theorem|452 §11.2 (Multivariable Taylor's Theorem)]]; in one variable, [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]].

**On the factor $\tfrac12$.** The board states the lemma with $\tfrac12 \sum_{i,j}$ in front of the quadratic term; Uribe added it “just for consistency,” saying it “doesn't matter.” For the *existence* statement that is right — replacing $f_{ij}$ by $2f_{ij}$ converts one form into the other. But the two forms are not interchangeable as written: the iterated proof above produces the version *without* the $\tfrac12$, and with $f_{ij}(a) = \tfrac12 \partial_{ij} f(a)$. The board's normalization is the one in which $f_{ij}(a) = \partial_{ij} f(a)$, matching the Hessian term $\tfrac12 \sum \partial_{ij}f(a)(r^i - a^i)(r^j - a^j)$ of the ordinary Taylor polynomial. A numerical check on a test function confirms the unscaled identity to machine precision and shows the scaled one, with the same $f_{ij}$, to be off. Nothing below depends on the normalization, since only the vanishing of the quadratic term under a derivation is used.

> [!remark] Remark
> **What matters.** “The point is that these functions don't blow up at $a$”: the remainder is a product of two factors vanishing at $a$ with a *smooth* function, not merely a quantity that is small compared with $|r - a|^2$. The same iteration continues to any order.

^rem-29-2

![[m591-12-7.svg]]
*Taylor–Hadamard for $f(r) = e^r$ at $a = 0$, in one variable. Left: the remainder $f(r) - f(a) - f'(a)(r-a)$ is the gap between the graph and its tangent line. Right: the same gap divided by $(r - a)^2$. The quotient $f_{11}(r) = (e^r - 1 - r)/r^2$ has only a removable singularity at $a$: it is smooth there, with value $\tfrac12 = \tfrac12 f''(0)$, exactly as the lemma predicts, and as the iterated proof computes it — $f_1(r) = (e^r - 1)/r$, then $f_{11}(r) = (f_1(r) - f_1(0))/r$. That the quotient extends smoothly across $a$ is the whole content of the lemma.*

> [!theorem] Corollary §29.5: Derivations on $\mathbb{R}^n$
> Let $W \subseteq \mathbb{R}^n$ be open, $a \in W$, and $D$ a derivation at $a$ on $W$. Then for every germ $[f]$ at $a$,
>
> $$
> D[f] = \sum_{i=1}^n \frac{\partial f}{\partial r^i}(a)\, D[r^i], \qquad\text{that is,}\qquad D = \sum_{i=1}^n D[r^i]\, \frac{\partial}{\partial r^i}\Big|_a .
> $$
>
> *Lee: Proposition 3.2 and Corollary 3.3*

^cor-29-5

> [!proof]+ Proof
> Two formulas are claimed; the second is the first read as an equality of derivations.
>
> *Reduction to a ball.* Let $(f, V)$ represent $[f]$. Choose an open ball $B \subseteq V \cap W$ centred at $a$ (possible since $V \cap W$ is open and contains $a$). Then $(f|_B, B) \sim (f, V)$, so we may take the representative $f$ on $B$, which changes nothing since $D$ acts on germs.
>
> *The germ identity.* Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-4|§29.4]] gives smooth $f_{ij}$ on $B$ with $f(r) = f(a) + \sum_i (r^i - a^i)\,\partial f/\partial r^i(a) + \sum_{i,j} (r^i - a^i)(r^j - a^j) f_{ij}(r)$ for all $r \in B$. Functions equal on $B$ have equal germs, and the germ of a sum or product of functions on $B$ is the sum or product of their germs (Proposition [[§27 Germs#^prop-27-2|§27.2]]); so, writing $\underline{c}$ for constants as in Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]],
>
> $$
> [f] = \big[\underline{f(a)}\big] + \sum_{i} \frac{\partial f}{\partial r^i}(a)\, \big[r^i - a^i\big] + \sum_{i,j} \big[r^i - a^i\big]\,\big[(r^j - a^j) f_{ij}\big] .
> $$
>
> *Apply $D$.* Apply $D$ to this identity; $D$ is linear and the numbers $\partial f/\partial r^i(a)$ come out:
>
> $$
> D[f] = D\big[\underline{f(a)}\big] + \sum_{i} \frac{\partial f}{\partial r^i}(a)\, D\big[r^i - a^i\big] + \sum_{i,j} D\Big[(r^i - a^i)\cdot\big((r^j - a^j) f_{ij}\big)\Big].
> $$
>
> The constant term vanishes by Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1). Each quadratic term is $D$ of a product of two germs in $I_a$ — namely $r^i - a^i$ and $(r^j - a^j)f_{ij}$, both zero at $a$, the values at $a$ being $a^i - a^i = 0$ and $0 \cdot f_{ij}(a) = 0$ — so it vanishes by Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2). Finally $D[r^i - a^i] = D[r^i]$ by (1) again: $D[r^i - a^i] = D[r^i] - D[\underline{a^i}] = D[r^i] - 0$. What remains is
>
> $$
> D[f] = 0 + \sum_{i=1}^n \frac{\partial f}{\partial r^i}(a)\, D[r^i] + 0 ,
> $$
>
> the first formula. So $D$ sees only the linear part of $f$: “the ultimate formula in the Euclidean case.”
>
> *The second formula.* $\partial/\partial r^i|_a$ is the coordinate derivation (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]) of the identity chart $(W, \mathrm{id}_W)$, whose coordinate functions are the $r^i$ and in which $f_{\mathrm{id}} = f$; so $\partial/\partial r^i|_a[f] = \partial f/\partial r^i(a)$, and it is a derivation at $a$ (Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]]). Derivations are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]), so for every germ $[f]$, by the first formula,
>
> $$
> \Big(\sum_{i=1}^n D[r^i]\, \frac{\partial}{\partial r^i}\Big|_a\Big)[f] = \sum_{i=1}^n D[r^i]\, \frac{\partial f}{\partial r^i}(a) = D[f] .
> $$
>
> The two derivations agree on every germ, so they are equal.

^pf-29-5

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-4|§29.4]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§27 Germs#^prop-27-2|§27.2]], [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

> [!theorem] Theorem §29.6: Basis Theorem
> Let $M$ be a smooth $n$-manifold, $p \in M$, and $(U, \varphi)$ any smooth chart with $p \in U$. Then
>
> $$
> \left\{ \frac{\partial}{\partial x^1}\Big|_p, \ \ldots, \ \frac{\partial}{\partial x^n}\Big|_p \right\}
> $$
>
> is a basis of $T_pM$; in particular $\dim T_pM = n$. Explicitly, every derivation $D$ at $p$ satisfies the **universal formula**
>
> $$
> D \;=\; \sum_{i=1}^n D\big[x^i\big]\, \frac{\partial}{\partial x^i}\Big|_p .
> $$
>
> *Lee: Proposition 3.15 and Corollary 3.3*

^thm-29-6

> [!proof]+ Proof
> *(Lecture 9. In lecture the derivation $\tilde D$ was introduced inside this proof — “this is how you push forward derivations … we'll come back to this construction immediately after” — and Uribe remarked that “the order of my presentation is not ideal.” The notes define the pushforward first, in [[§28 Derivations and the Abstract Tangent Space|§28]], so that the proof can cite it.)* Let $D \in T_pM$ and put $a = \varphi(p) = (r_0^1, \ldots, r_0^n)$. What has to be shown: the $n$ derivations $\partial/\partial x^i|_p$, which lie in $T_pM$ by Proposition [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]], span $T_pM$ — this is the universal formula, Steps 1–3 — and are linearly independent, Step 4.
>
> *Step 1: push $D$ down.* Let $\tilde D = \varphi_{\ast p}D \in T_a\,\varphi(U)$, the chart pushforward of Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]] (with $D$ regarded as a derivation on germs on $U$, by the identification $T_pM = T_pU$ of Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). By Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] with $F = \varphi$, $\tilde D[g] = D\big(\varphi_p^{\ast}[g]\big) = D[g \circ \varphi]$ for germs $g$ at $a$.
>
> *Step 2: apply the Euclidean formula downstairs.* By Corollary [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]] on the open set $\varphi(U)$, applied to the derivation $\tilde D$ at $a$: for every germ $[g]$ at $a$,
>
> $$
> \tilde D[g] = \sum_{i=1}^n \frac{\partial g}{\partial r^i}(a)\, \tilde D[r^i] .
> $$
>
> *Step 3: read it back upstairs.* Let $[f]$ be a germ at $p$, with a representative $(f, V)$; replacing $V$ by $V \cap U$ does not change the germ, so assume $V \subseteq U$. Take $g = f_\varphi = f \circ \varphi^{-1}$, defined and smooth on the open set $\varphi(V) \ni a$. Three identities translate the terms of Step 2:
> - $f_\varphi \circ \varphi = f \circ \varphi^{-1} \circ \varphi = f$ on $V$, so by Step 1, $\tilde D[f_\varphi] = D[f_\varphi \circ \varphi] = D[f]$;
> - by Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], $\partial f_\varphi/\partial r^i(a) = \partial/\partial x^i|_p[f]$;
> - by Step 1 and Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]] ($x^i = r^i \circ \varphi$), $\tilde D[r^i] = D[r^i \circ \varphi] = D[x^i]$.
>
> Substituting these into Step 2 with $g = f_\varphi$, and using that derivations are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]),
>
> $$
> D[f] = \tilde D[f_\varphi] = \sum_{i=1}^n \frac{\partial f_\varphi}{\partial r^i}(a)\, \tilde D[r^i] = \sum_{i=1}^n D[x^i]\, \frac{\partial}{\partial x^i}\Big|_p[f] = \Big(\sum_{i=1}^n D[x^i]\, \frac{\partial}{\partial x^i}\Big|_p\Big)[f] \qquad\text{for every germ } [f],
> $$
>
> so $D = \sum_i D[x^i]\, \partial/\partial x^i|_p$, two derivations being equal when they agree on every germ. As $D$ was arbitrary, the coordinate derivations span.
>
> *Step 4: independence.* First, for all $i, j$: since $(x^j)_\varphi = r^j$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]](3)) and the projection $r^j$ has $i$-th partial derivative $1$ if $i = j$ and $0$ otherwise, Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]] gives
>
> $$
> \frac{\partial}{\partial x^i}\Big|_p[x^j] = \frac{\partial (x^j)_\varphi}{\partial r^i}(a) = \frac{\partial r^j}{\partial r^i}(a) = \delta^j_i .
> $$
>
> Now suppose $\sum_i c_i\, \partial/\partial x^i|_p = 0$, and apply it to $[x^j]$. Evaluating pointwise,
>
> $$
> 0 = \Big(\sum_{i=1}^n c_i\, \frac{\partial}{\partial x^i}\Big|_p\Big)[x^j] = \sum_{i=1}^n c_i\, \frac{\partial}{\partial x^i}\Big|_p[x^j] = \sum_{i=1}^n c_i\, \delta^j_i = c_j ,
> $$
>
> hence $c_j = 0$, for every $j$. So the $n$ coordinate derivations form a basis, and $\dim T_pM = n$. The coefficients of $D$ are the numbers $D[x^i]$ — uniquely: if also $D = \sum_i b_i\, \partial/\partial x^i|_p$, the same evaluation at $[x^j]$ gives $D[x^j] = \sum_i b_i\, \delta^j_i = b_j$.

^pf-29-6

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-5|§29.5]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^prop-29-2|§29.2]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

![[m591-12-8.svg]]

$$
\varphi^*[r^i] = [x^i], \qquad \varphi^*[f_\varphi] = [f]
$$

*The proof in one diagram — the defining triangle of the pushforward, for the chart. Downstairs the Euclidean formula computes $\tilde D$ on everything; the two pullback identities displayed under the diagram carry the answer back upstairs, turning $\tilde D[r^i]$ into $D[x^i]$ and $\tilde D[f_\varphi]$ into $D[f]$.*

> [!remark]- Connections
> - The coefficients $D[x^i]$ are the values of the dual basis $dx^i|_p$: [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]; cf. [[§12 Duality#^ladr-3-114|LADR 3.114]].
> - The components in the coordinate basis give the local trivializations and charts of the tangent bundle: [[§49 The Tangent Bundle#^def-49-4|Def. §49.4]], [[§49 The Tangent Bundle#^def-49-5|Def. §49.5]].

**Reconciliation with the lecture.** This is the lecture's proof, in the lecture's order of ideas but with the pushforward defined before it is used rather than after. Two details of the board version. It opens with “$\forall\, [f] \in I_p$”: restricting to germs vanishing at $p$ is harmless, since $D[f] = D[f - f(p)]$ by Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1), but the argument works verbatim for every germ. And the notes had filled in a proof of this theorem before Lecture 9, via two reduction lemmas; those were the pushforward by an inclusion and by the chart in disguise, and they now appear as Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] and Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]].

**Transcription note (Lecture 8).** Page 16 of the handwritten notes states Taylor–Hadamard for “$f : U \to \mathbb{R}^2$”; the target is $\mathbb{R}$.

> [!theorem] Theorem §29.7: Ambient and Abstract Agree
> Let $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ be a regular level set and $p \in M$. Then
>
> $$
> T^{\mathrm{geo}}_pM \longrightarrow T_pM, \qquad v \longmapsto D_v,
> $$
>
> from the geometric tangent space (a subspace of $\mathbb{R}^{n+k}$) to the abstract tangent space (derivations at $p$) is an isomorphism of vector spaces.
>
> *Lee: Propositions 3.2, 5.37 and 5.38*

^thm-29-7

> [!proof]+ Proof
> **Announced in lecture.** Stated in lecture in answer to a student's question — “are the ambient and the abstract tangent spaces the same, just defined differently?” — with the answer that they are, but that it has to be proved. Injectivity is Proposition [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]]; that $D_v$ really is a derivation is Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]]; surjectivity follows from the basis theorem (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), both spaces having dimension $n$. In detail:
>
> *The map lands in $T_pM$.* Near $p$, $M$ is the graph of a smooth function, after permuting coordinates (Step 2 of the proof of Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), and passing to this open piece changes neither the geometric tangent space (Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]]) nor the germs at $p$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]); so $D_v$ is defined by Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]]. By Proposition [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]](1), $D_v(f)$ depends only on the germ $[f]$, so $D_v$ is a map $C_p^\infty(M) \to \mathbb{R}$; by (3) it is linear and obeys the Leibniz rule, so it is a derivation at $p$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]), $D_v \in T_pM$; and by (2) it does not depend on the graph piece used, only on $v$.
>
> *Linear.* In the graph chart, $v = (u, G'(x_0)u)$, so $u$ consists of the graph-variable components of $v$ and depends linearly on $v$; and $D_v(f) = u \cdot \nabla f_\varphi(x_0)$ is linear in $u$. Hence $D_{\lambda v + w}(f) = \lambda\, D_v(f) + D_w(f)$ for every $f$, i.e. $D_{\lambda v + w} = \lambda D_v + D_w$ (pointwise operations, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]).
>
> *Injective.* If $D_v = D_{v'}$ then $v = v'$ (Proposition [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]]).
>
> *Bijective.* $\dim T^{\mathrm{geo}}_pM = n$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) and $\dim T_pM = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], $M$ being a smooth $n$-manifold). A linear map between spaces of the same finite dimension is injective if and only if it is surjective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), so $v \mapsto D_v$ is a linear bijection, i.e. an isomorphism of vector spaces.
>
> Even once it is proved, the notes keep the notations apart: $T^{\mathrm{geo}}_pM$ is the geometric tangent space, $T_pM$ the abstract one.

^pf-29-7

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]], [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!remark]- Connections
> - The same argument, with both dimension counts cited ([[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] for $T^{\mathrm{geo}}_pM$, the [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|basis theorem]] for $T_pM$), is recorded as [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-8|Consequences, §29.8]].
> - The same identification read through velocities of curves: [[§31 Tangent Vectors as Velocities of Curves#^rem-31-1|The Two Faces Reconciled]].

> [!theorem] Corollary §29.8: Consequences
> Let $M$ be a smooth $n$-manifold and $p \in M$. Then the abstract tangent space has $\dim T_pM = n$, and for a regular level set $M = F^{-1}(c)$ the map $v \mapsto D_v$ of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], from $T^{\mathrm{geo}}_pM$ to $T_pM$, is an isomorphism.
>
> *Lee: Proposition 3.10*

^cor-29-8

> [!proof]+ Proof
> *First claim.* The first claim is Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]: in any chart at $p$ the $n$ coordinate derivations $\partial/\partial x^i|_p$ form a basis of $T_pM$, so $\dim T_pM = n$.
>
> *Second claim.* For the second, $v \mapsto D_v$ is linear and injective (Proposition [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]]; it lands in $T_pM$ and is linear as shown in the proof of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]]) between spaces of dimension $n$ — the geometric tangent space $T^{\mathrm{geo}}_pM$ by Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], the abstract tangent space $T_pM$ by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] — hence an isomorphism: by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), an injective linear map between spaces of equal finite dimension is also surjective.

^pf-29-8

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§25 The Geometric Tangent Space#^prop-25-9|§25.9]], [[§25 The Geometric Tangent Space#^prop-25-8|§25.8]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!remark]- Connections
> - The same argument as the proof of [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|Ambient and Abstract Agree, §29.7]], stated just above, with both dimension counts cited.

**Comparison with Lee.** Lee meets the two kinds of tangent vector in the opposite order. He defines $T_pM$ by derivations first, identifies geometric and abstract tangent vectors in $\mathbb{R}^n$ (Proposition 3.2), and only later, for embedded submanifolds, shows $T_pS = \ker d\Phi_p$ (Proposition 5.38). The course starts geometrically, with $T^{\mathrm{geo}}_pM = \ker F'(p)$ inside the ambient space (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), and reaches derivations afterwards. The consequence above is where the two orders meet.

> [!remark] Remark: A Derivation Sees Only the First Derivatives
> The basis theorem showed that, of the whole Taylor expansion of a germ, a derivation sees only the *linear* term — “of the entire Taylor series of the germ, all I care about are the first partials.” [[§34 The Cotangent Space from Germs|§34]] says this algebraically: $I_p$ is a maximal ideal, being the kernel of evaluation; $I_p^2$ consists exactly of the germs vanishing to *second* order (Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]]); and $I_p/I_p^2$ is canonically the *cotangent space* $T_p^{\ast}M$ of Definition [[§32 The Cotangent Space#^def-32-4|§32.4]], built with no dualizing at all (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]). This is the sense in which, as Uribe remarked when he first set out to define the abstract tangent space, “it is more natural to define the dual”: the cotangent space comes first, and the abstract tangent space is its dual. We follow Lee and do not take that route.

^rem-29-3

> [!theorem] Theorem §29.9: Dimension of the Tangent Space
> Let $M$ be a smooth $n$-manifold. Then for every $p \in M$,
>
> $$
> \dim T_pM = n = \dim M ,
> $$
>
> the same at every point, and independent of the chart used to compute it.

^thm-29-9

> [!proof]+ Proof
> *(The last clause of the basis theorem, recorded as a theorem in its own right.)* Fix $p \in M$. Since $M$ is a smooth $n$-manifold, there is a chart $(U, \varphi)$ at $p$, with $\varphi(U) \subseteq \mathbb{R}^n$. Any chart $(U, \varphi)$ at $p$ has $n$ coordinate functions $x^1, \ldots, x^n$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), and by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] the $n$ derivations $\partial/\partial x^i|_p$ form a basis of $T_pM$; so $\dim T_pM = n$. A different chart gives a different basis, but every basis of a finite-dimensional vector space has the same number of elements, namely its dimension; so every chart yields the same count $n$. Since $p$ was arbitrary, $\dim T_pM = n$ at every point.

^pf-29-9

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§6 Dimension#^ladr-2-34|LADR 2.34]]

This is less obvious than it looks: the space of germs $C^\infty_p(M)$ ([[§27 Germs#^def-27-2|Def. §27.2]]) on which the derivations act is infinite-dimensional, and it is the Hadamard lemma ([[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]) behind the basis theorem that cuts the derivations down to exactly $n$ dimensions.

> [!theorem] Corollary §29.10: Smooth Invariance of Dimension
> If $U \subseteq \mathbb{R}^m$ and $V \subseteq \mathbb{R}^n$ are nonempty open sets and $F : U \to V$ is a diffeomorphism ([[§17 Differentiable Structures#^def-17-3|Def. §17.3]]), then $m = n$. Consequently two smooth charts ([[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]]) of a smooth manifold at the same point have targets of the same dimension.

^cor-29-10

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Give $U$ and $V$ their standard smooth structures, with the identity charts $(U, \mathrm{id}_U)$ and $(V, \mathrm{id}_V)$; they are smooth manifolds of dimensions $m$ and $n$, and $F$ and $F^{-1}$ are smooth maps between them (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]). Let $p \in U$, which exists since $U$ is nonempty.
>
> *$F_{\ast p}$ is an isomorphism.* By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $(F^{-1})_{\ast F(p)} \circ F_{\ast p}$ and $F_{\ast p} \circ (F^{-1})_{\ast F(p)}$ are the pushforwards of the identity maps, hence identities:
>
> $$
> (F^{-1})_{\ast F(p)} \circ F_{\ast p} = (F^{-1} \circ F)_{\ast p} = (\mathrm{id}_U)_{\ast p} = \mathrm{id}_{T_pU}, \qquad F_{\ast p} \circ (F^{-1})_{\ast F(p)} = (F \circ F^{-1})_{\ast F(p)} = (\mathrm{id}_V)_{\ast F(p)} = \mathrm{id}_{T_{F(p)}V},
> $$
>
> using $F^{-1}(F(p)) = p$ in the second. So $F_{\ast p} : T_pU \to T_{F(p)}V$ is a linear isomorphism (linear by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]); this is Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]] for $\Phi = F$.
>
> *The dimensions.* By Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], applied to the open sets $U$ and $V$ with their identity charts, these spaces have dimensions $m$ and $n$. A linear isomorphism is injective and surjective, so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) $m \le n$ and $m \ge n$; so $m = n$.
>
> *Charts.* For two charts $(U_1, \varphi_1)$ and $(U_2, \varphi_2)$ at $p$ with targets $\mathbb{R}^m$ and $\mathbb{R}^n$, apply this to the transition map $\varphi_2 \circ \varphi_1^{-1} : \varphi_1(U_1 \cap U_2) \to \varphi_2(U_1 \cap U_2)$, a diffeomorphism between nonempty open sets: the two sets are open because $U_1 \cap U_2$ is open and the charts are homeomorphisms onto open sets, nonempty because they contain $\varphi_1(p)$ and $\varphi_2(p)$, and the transition map is a bijection which is smooth with smooth inverse $\varphi_1 \circ \varphi_2^{-1}$ because the two charts are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]).

^pf-29-10

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]]

> [!remark]- Connections
> - The topological statement, true but hard: [[§2 Topological Manifolds#^thm-2-1|Topological Invariance of Dimension, §2.1]].

Compare Theorem [[§2 Topological Manifolds#^thm-2-1|§2.1]]: the same statement for *homeomorphisms* is true but genuinely hard, needing algebraic topology. For diffeomorphisms the derivative linearizes the problem, and linear algebra finishes it — one of the first payoffs of having tangent spaces.
