---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 54
tags: [differentiable-manifolds, math591]
---
← [[§53 Differential Operators]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§55 Related Vector Fields]] →

*Stage: fields — Two vector fields, composed as operators, give a second-order operator; their commutator cancels the second derivatives and is again a vector field, so $\mathfrak{X}(M)$ is a Lie algebra.*

*Lecture 16. “Who cares? There is one reason we care … when we look at commutators.”*

> [!definition] Definition §54.1: The Lie Bracket of Vector Fields
> For $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$, regarded as [[§52 Vector Fields#^lem-52-3|operators]] on $C^\infty(M)$ ([[§52 Vector Fields#^def-52-4|Definition §52.4]]), the **commutator** or **Lie bracket** is the operator
>
> $$
> [\mathbf{X}, \mathbf{Y}](f) = \mathbf{X}\big(\mathbf{Y}(f)\big) - \mathbf{Y}\big(\mathbf{X}(f)\big), \qquad f \in C^\infty(M).
> $$
>
> *Lee: Ch. 8, Lie Brackets*

^def-54-1

Each composite $\mathbf{X} \circ \mathbf{Y}$ is a second-order operator, in $\mathrm{Diff}_2(M)$ ([[§53 Differential Operators#^def-53-3|Definition §53.3]]) — “you get second derivatives in local coordinates” — but “something very, very nice happens when you look at the commutator.”

> [!theorem] Lemma §54.1: The Bracket of Vector Fields Is a Vector Field
> $[\mathbf{X}, \mathbf{Y}]$ is a [[§52 Vector Fields#^def-52-5|derivation]] of $C^\infty(M)$; hence, by [[§52 Vector Fields#^prop-52-7|Proposition §52.7]], it is a [[§52 Vector Fields#^def-52-1|vector field]].
>
> *Lee: Lemma 8.25*

^lem-54-1

> [!proof]+ Proof
> *(Lecture 16 — “tedious algebra \ldots the key thing is the product rule.”)* By Definition [[§52 Vector Fields#^def-52-5|§52.5]], three things have to be shown: that $[\mathbf{X}, \mathbf{Y}]$ takes $C^\infty(M)$ to $C^\infty(M)$, that it is $\mathbb{R}$-linear, and that it satisfies the product rule. Throughout, $\mathbf{X}f$ is the function $p \mapsto \mathbf{X}_p[f]$. By Lemma [[§52 Vector Fields#^lem-52-3|§52.3]], $\mathbf{X}$ and $\mathbf{Y}$ are derivations of $C^\infty(M)$: each is linear, and $\mathbf{X}(fg) = f\,\mathbf{X}g + g\,\mathbf{X}f$, $\mathbf{Y}(fg) = f\,\mathbf{Y}g + g\,\mathbf{Y}f$.
>
> *An operator.* For $f \in C^\infty(M)$, $\mathbf{Y}f \in C^\infty(M)$ by Lemma [[§52 Vector Fields#^lem-52-3|§52.3]], and then $\mathbf{X}(\mathbf{Y}f) \in C^\infty(M)$ by the same lemma applied to the smooth function $\mathbf{Y}f$. Likewise $\mathbf{X}f$ and then $\mathbf{Y}(\mathbf{X}f)$ are smooth. So their difference $[\mathbf{X}, \mathbf{Y}](f)$ is smooth.
>
> *Linearity.* Linearity is clear, as a difference of composites of linear maps. Explicitly, for $a, b \in \mathbb{R}$ and $f, g \in C^\infty(M)$, by linearity of $\mathbf{Y}$ and then of $\mathbf{X}$,
>
> $$
> \mathbf{X}\big(\mathbf{Y}(af + bg)\big) = \mathbf{X}\big(a\,\mathbf{Y}f + b\,\mathbf{Y}g\big) = a\,\mathbf{X}\mathbf{Y}f + b\,\mathbf{X}\mathbf{Y}g ,
> $$
>
> and by linearity of $\mathbf{X}$ and then of $\mathbf{Y}$,
>
> $$
> \mathbf{Y}\big(\mathbf{X}(af + bg)\big) = \mathbf{Y}\big(a\,\mathbf{X}f + b\,\mathbf{X}g\big) = a\,\mathbf{Y}\mathbf{X}f + b\,\mathbf{Y}\mathbf{X}g .
> $$
>
> Subtracting the second line from the first and grouping the terms with $a$ and with $b$,
>
> $$
> [\mathbf{X}, \mathbf{Y}](af + bg) = a\,\big(\mathbf{X}\mathbf{Y}f - \mathbf{Y}\mathbf{X}f\big) + b\,\big(\mathbf{X}\mathbf{Y}g - \mathbf{Y}\mathbf{X}g\big) = a\,[\mathbf{X}, \mathbf{Y}](f) + b\,[\mathbf{X}, \mathbf{Y}](g) .
> $$
>
> *Product rule.* For the product rule, apply the product rule for $\mathbf{Y}$, then the linearity of $\mathbf{X}$, and then the product rule for $\mathbf{X}$ to each of the two products $f \cdot \mathbf{Y}g$ and $g \cdot \mathbf{Y}f$:
>
> $$
> \mathbf{X}\big(\mathbf{Y}(fg)\big) = \mathbf{X}\big(f\, \mathbf{Y}g + g\, \mathbf{Y}f\big) = \mathbf{X}\big(f\, \mathbf{Y}g\big) + \mathbf{X}\big(g\, \mathbf{Y}f\big) = \mathbf{X}f\; \mathbf{Y}g + f\, \mathbf{X}\mathbf{Y}g + \mathbf{X}g\; \mathbf{Y}f + g\, \mathbf{X}\mathbf{Y}f .
> $$
>
> The same expression with $\mathbf{X}$ and $\mathbf{Y}$ exchanged — the product rule for $\mathbf{X}$, the linearity of $\mathbf{Y}$, the product rule for $\mathbf{Y}$ — is
>
> $$
> \mathbf{Y}\big(\mathbf{X}(fg)\big) = \mathbf{Y}\big(f\, \mathbf{X}g + g\, \mathbf{X}f\big) = \mathbf{Y}\big(f\, \mathbf{X}g\big) + \mathbf{Y}\big(g\, \mathbf{X}f\big) = \mathbf{Y}f\; \mathbf{X}g + f\, \mathbf{Y}\mathbf{X}g + \mathbf{Y}g\; \mathbf{X}f + g\, \mathbf{Y}\mathbf{X}f .
> $$
>
> Subtracting, the first-order cross terms $\mathbf{X}f\,\mathbf{Y}g$ and $\mathbf{X}g\,\mathbf{Y}f$ cancel, because functions multiply commutatively: $\mathbf{X}f\;\mathbf{Y}g - \mathbf{Y}g\;\mathbf{X}f = 0$ and $\mathbf{X}g\;\mathbf{Y}f - \mathbf{Y}f\;\mathbf{X}g = 0$. That leaves
>
> $$
> [\mathbf{X}, \mathbf{Y}](fg) = f\,\big(\mathbf{X}\mathbf{Y}g - \mathbf{Y}\mathbf{X}g\big) + g\,\big(\mathbf{X}\mathbf{Y}f - \mathbf{Y}\mathbf{X}f\big) = f\, [\mathbf{X}, \mathbf{Y}](g) + g\, [\mathbf{X}, \mathbf{Y}](f).
> $$
>
> So $[\mathbf{X}, \mathbf{Y}]$ is a derivation of $C^\infty(M)$. By Proposition [[§52 Vector Fields#^prop-52-7|§52.7]] it is the operator $D_\mathbf{Z}$ of a unique vector field $\mathbf{Z}$, and this field is again written $[\mathbf{X}, \mathbf{Y}]$.

^pf-54-1

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[§52 Vector Fields#^def-52-5|Def. §52.5]], [[§52 Vector Fields#^lem-52-3|§52.3]], [[§52 Vector Fields#^prop-52-7|§52.7]]

> [!example] Example §54.1: A Bracket in the Plane
> On $\mathbb{R}^2$ with coordinates $(x, y)$, let $\mathbf{X} = a\, \partial_x$ and $\mathbf{Y} = b\, \partial_y$ with $a, b \in C^\infty(\mathbb{R}^2)$. Then
>
> $$
> [\mathbf{X}, \mathbf{Y}] = a\, \frac{\partial b}{\partial x}\, \frac{\partial}{\partial y} \;-\; b\, \frac{\partial a}{\partial y}\, \frac{\partial}{\partial x} .
> $$

^ex-54-1

> [!proof]+ Proof
> *(Lecture 16 — “an exercise in multivariable calculus.”)* Both sides are vector fields: the left side by Lemma [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], the right side by Proposition [[§52 Vector Fields#^prop-52-1|§52.1]], since its coefficients are products of smooth functions. A vector field is determined by its operator (the uniqueness in Proposition [[§52 Vector Fields#^prop-52-7|§52.7]]), so it suffices that both sides give the same function when applied to any $f \in C^\infty(\mathbb{R}^2)$. In the standard chart, Lemma [[§52 Vector Fields#^lem-52-3|§52.3]] gives $\mathbf{X}h = a\, \partial h/\partial x$ and $\mathbf{Y}h = b\, \partial h/\partial y$ for every smooth $h$.
>
> Apply both composites to $f$ and use the product rule for the partial derivatives $\partial/\partial x$ and $\partial/\partial y$:
>
> $$
> \mathbf{X}\mathbf{Y}f = a\, \frac{\partial}{\partial x}\Big(b\, \frac{\partial f}{\partial y}\Big) = a\, \frac{\partial b}{\partial x}\, \frac{\partial f}{\partial y} + ab\, \frac{\partial^2 f}{\partial x\, \partial y}, \qquad
> \mathbf{Y}\mathbf{X}f = b\, \frac{\partial}{\partial y}\Big(a\, \frac{\partial f}{\partial x}\Big) = b\, \frac{\partial a}{\partial y}\, \frac{\partial f}{\partial x} + ba\, \frac{\partial^2 f}{\partial y\, \partial x} .
> $$
>
> The second derivatives are equal, $ab\, \partial^2 f/\partial x\, \partial y = ba\, \partial^2 f/\partial y\, \partial x$, because $ab = ba$ and the mixed partials of the smooth function $f$ agree (Clairaut's theorem). So they cancel in the difference, leaving
>
> $$
> [\mathbf{X}, \mathbf{Y}]f = \mathbf{X}\mathbf{Y}f - \mathbf{Y}\mathbf{X}f = a\, \frac{\partial b}{\partial x}\, \frac{\partial f}{\partial y} - b\, \frac{\partial a}{\partial y}\, \frac{\partial f}{\partial x} .
> $$
>
> By Lemma [[§52 Vector Fields#^lem-52-3|§52.3]] again, the right side is the field $a\, (\partial b/\partial x)\, \partial/\partial y - b\, (\partial a/\partial y)\, \partial/\partial x$ applied to $f$. So the two fields have the same operator, and the bracket is the stated first-order operator.

^pf-ex-54-1

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[Schwarz–Clairaut Theorem|452 §6.1]], [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], [[§52 Vector Fields#^prop-52-1|§52.1]], [[§52 Vector Fields#^prop-52-7|§52.7]], [[§52 Vector Fields#^lem-52-3|§52.3]]

> [!theorem] Proposition §54.2: The Bracket in Coordinates
> In a chart with $\mathbf{X} = \sum_i X^i\, \partial_i$ and $\mathbf{Y} = \sum_i Y^i\, \partial_i$, where $\partial_i = \partial/\partial x^i$,
>
> $$
> [\mathbf{X}, \mathbf{Y}] = \sum_j \big( \mathbf{X}(Y^j) - \mathbf{Y}(X^j) \big)\, \partial_j = \sum_j \sum_i \Big( X^i\, \frac{\partial Y^j}{\partial x^i} - Y^i\, \frac{\partial X^j}{\partial x^i} \Big)\, \partial_j .
> $$
>
> *Lee: Proposition 8.26*

^prop-54-2

> [!proof]+ Proof
> *(Not from lecture; filled in — Example [[§54 Lie Bracket and Lie Algebra#^ex-54-1|§54.1]] is the case $\mathbf{X} = a\,\partial_x$, $\mathbf{Y} = b\,\partial_y$.)* Let $U$ be the chart domain. The $X^i, Y^i \in C^\infty(U)$ are the coefficient functions of Proposition [[§52 Vector Fields#^prop-52-1|§52.1]], $X^i(q) = \mathbf{X}_q[x^i]$ and $Y^i(q) = \mathbf{Y}_q[x^i]$; and for $h \in C^\infty(U)$, $\mathbf{X}(h)$ denotes the function $q \mapsto \mathbf{X}_q[h]$ on $U$. The $j$-th coefficient of a vector field is its value on the coordinate function $x^j$ (Proposition [[§52 Vector Fields#^prop-52-1|§52.1]]); applied to the vector field $[\mathbf{X}, \mathbf{Y}]$ (Lemma [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]]), this gives $[\mathbf{X}, \mathbf{Y}]_q = \sum_j [\mathbf{X}, \mathbf{Y}]^j(q)\, \partial_j|_q$ at each $q \in U$, with $[\mathbf{X}, \mathbf{Y}]^j(q) = [\mathbf{X}, \mathbf{Y}]_q[x^j]$. So what has to be shown is
>
> $$
> [\mathbf{X}, \mathbf{Y}]_p[x^j] = \mathbf{X}_p[Y^j] - \mathbf{Y}_p[X^j] \qquad \text{for every } p \in U \text{ and every } j,
> $$
>
> followed by the expansion of the right side. Informally this is $[\mathbf{X}, \mathbf{Y}](x^j) = \mathbf{X}(\mathbf{Y}x^j) - \mathbf{Y}(\mathbf{X}x^j) = \mathbf{X}(Y^j) - \mathbf{Y}(X^j)$; the one point to take care of is that the bracket acts on $C^\infty(M)$, while $x^j$ is defined only on $U$.
>
> *A global stand-in for $x^j$.* Fix $p \in U$. Let $\chi$ be a bump function at $p$ with $\operatorname{supp}\chi \subseteq U$ (Proposition [[§52 Vector Fields#^prop-52-4|§52.4]]), equal to $1$ on an open $V \ni p$; then $V \subseteq \operatorname{supp}\chi \subseteq U$. By Corollary [[§52 Vector Fields#^cor-52-5|§52.5]], $\tilde x^j = \chi x^j$, extended by $0$ outside $U$, lies in $C^\infty(M)$, and it equals $x^j$ on $V$. So at every $q \in V$ the germs of $\tilde x^j$ and $x^j$ coincide, and
>
> $$
> (\mathbf{Y}\tilde x^j)(q) = \mathbf{Y}_q[\tilde x^j] = \mathbf{Y}_q[x^j] = Y^j(q), \qquad (\mathbf{X}\tilde x^j)(q) = \mathbf{X}_q[\tilde x^j] = \mathbf{X}_q[x^j] = X^j(q) \qquad (q \in V).
> $$
>
> *The coefficient at $p$.* By the last display, $\mathbf{Y}\tilde x^j$ and $Y^j$ agree on the open neighbourhood $V$ of $p$, so they have the same germ at $p$, and $\mathbf{X}_p$, which acts on germs, gives them the same value; likewise for $\mathbf{X}\tilde x^j$, $X^j$ and $\mathbf{Y}_p$. Hence, using first $[\tilde x^j] = [x^j]$ at $p$ and then Definition [[§54 Lie Bracket and Lie Algebra#^def-54-1|§54.1]] evaluated at $p$,
>
> $$
> [\mathbf{X}, \mathbf{Y}]_p[x^j] = [\mathbf{X}, \mathbf{Y}]_p[\tilde x^j] = \mathbf{X}_p[\mathbf{Y}\tilde x^j] - \mathbf{Y}_p[\mathbf{X}\tilde x^j] = \mathbf{X}_p[Y^j] - \mathbf{Y}_p[X^j] .
> $$
>
> As $p \in U$ was arbitrary, this is the first formula: $[\mathbf{X}, \mathbf{Y}]^j = \mathbf{X}(Y^j) - \mathbf{Y}(X^j)$ on $U$.
>
> *The second form.* By the universal formula of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], $\mathbf{X}_p = \sum_i \mathbf{X}_p[x^i]\, \partial_i|_p = \sum_i X^i(p)\, \partial_i|_p$. Applied to the germ of $Y^j$, with Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], this expands $\mathbf{X}(Y^j) = \sum_i X^i\, \partial Y^j/\partial x^i$; with the letters $\mathbf{X}$ and $\mathbf{Y}$ exchanged, $\mathbf{Y}(X^j) = \sum_i Y^i\, \partial X^j/\partial x^i$. Substituting,
>
> $$
> [\mathbf{X}, \mathbf{Y}] = \sum_j \big( \mathbf{X}(Y^j) - \mathbf{Y}(X^j) \big)\, \partial_j = \sum_j \sum_i \Big( X^i\, \frac{\partial Y^j}{\partial x^i} - Y^i\, \frac{\partial X^j}{\partial x^i} \Big)\, \partial_j \qquad \text{on } U.
> $$

^pf-54-2

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], [[§52 Vector Fields#^prop-52-1|§52.1]], [[§54 Lie Bracket and Lie Algebra#^ex-54-1|Ex. §54.1]], [[§52 Vector Fields#^prop-52-4|§52.4]], [[§52 Vector Fields#^cor-52-5|§52.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]]

> [!theorem] Proposition §54.3: The Hessian at a Critical Point via Vector Fields
> Let $p$ be a critical point of $f \in C^\infty(M)$, and $v, w \in T_pM$. For every vector field $\mathbf{W}$ with $\mathbf{W}_p = w$,
>
> $$
> \mathrm{Hess}_p f(v, w) = v\big[\mathbf{W} f\big]
> $$
>
> (Definition [[§51 Critical Points and the Hessian#^def-51-2|§51.2]]). In particular the right side does not depend on the choice of $\mathbf{W}$; and, with $\mathbf{V}$ a vector field with $\mathbf{V}_p = v$, the symmetry of the Hessian is the vanishing of $df_p$ on a bracket:
>
> $$
> \mathrm{Hess}_p f(v, w) - \mathrm{Hess}_p f(w, v) = \big([\mathbf{V}, \mathbf{W}]f\big)(p) = df_p\big([\mathbf{V}, \mathbf{W}]_p\big) = 0 .
> $$

^prop-54-3

> [!proof]+ Proof
> *(Not from lecture; suggested by Assignment 5, Problem 3.)* Choose a chart $(U, \varphi = (x^1, \ldots, x^m))$ at $p$. On $U$, $\mathbf{W} = \sum_j W^j\, \partial/\partial x^j$ with smooth $W^j$ (Proposition [[§52 Vector Fields#^prop-52-1|§52.1]]), and $\mathbf{W}f = \sum_j W^j\, \partial f/\partial x^j$ (Lemma [[§52 Vector Fields#^lem-52-3|§52.3]]). The tangent vector $v$ is a derivation at $p$, acting on germs (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]), so by its linearity and Leibniz rule
>
> $$
> v\big[\mathbf{W} f\big] = \sum_{j=1}^m \Big( v\big[W^j\big]\, \frac{\partial f}{\partial x^j}(p) + W^j(p)\, v\Big[\frac{\partial f}{\partial x^j}\Big] \Big) .
> $$
>
> At a critical point $\partial f/\partial x^j(p) = df_p(\partial/\partial x^j|_p) = 0$ (Proposition [[§36 Submersions#^prop-36-2|§36.2]]), so the first terms vanish. In the second, $W^j(p) = w^j$, the components of $w = \mathbf{W}_p$, and with $v = \sum_i v^i\, \partial/\partial x^i|_p$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]) and Proposition [[§51 Critical Points and the Hessian#^prop-51-1|§51.1]](1),
>
> $$
> v\Big[\frac{\partial f}{\partial x^j}\Big] = \sum_{i=1}^m v^i\, \frac{\partial}{\partial x^i}\Big|_p\Big(\frac{\partial f}{\partial x^j}\Big) = \sum_{i=1}^m v^i\, H_{ij}(p) .
> $$
>
> So $v[\mathbf{W}f] = \sum_{i,j} H_{ij}(p)\, v^i w^j = \mathrm{Hess}_p f(v, w)$, which involves $\mathbf{W}$ only through $w$.
>
> For the last display: by what was just shown, $\mathrm{Hess}_p f(v, w) = v[\mathbf{W}f] = \mathbf{V}_p[\mathbf{W}f] = (\mathbf{V}(\mathbf{W}f))(p)$, and likewise $\mathrm{Hess}_p f(w, v) = (\mathbf{W}(\mathbf{V}f))(p)$. Their difference is $([\mathbf{V}, \mathbf{W}]f)(p)$ (Definition [[§54 Lie Bracket and Lie Algebra#^def-54-1|§54.1]]); $[\mathbf{V}, \mathbf{W}]$ is a vector field (Lemma [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]]), so this is $[\mathbf{V}, \mathbf{W}]_p[f] = df_p([\mathbf{V}, \mathbf{W}]_p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]), which is $0$ because $df_p = 0$. This is a second proof of the symmetry of $\mathrm{Hess}_p f$, without Clairaut's theorem.

^pf-54-3

*Uses:* [[§52 Vector Fields#^prop-52-1|§52.1]], [[§52 Vector Fields#^lem-52-3|§52.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§36 Submersions#^prop-36-2|§36.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§51 Critical Points and the Hessian#^prop-51-1|§51.1]], [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], [[§32 The Cotangent Space#^prop-32-2|§32.2]]

> [!definition] Definition §54.2: Lie Algebra
> A (real) **Lie algebra** $\mathfrak{g}$ is a real [[§2 Definition of Vector Space#^ladr-1-20|vector space]] together with a [[§38 Tensor Products#^ladr-9-77|bilinear]], skew-symmetric operation $[\cdot,\cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, the **Lie bracket**, satisfying the **Jacobi identity**
>
> $$
> [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 \qquad \text{for all } X, Y, Z \in \mathfrak{g}.
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-54-2

> [!remark]- Connections
> - In classical mechanics the Poisson bracket is bilinear, antisymmetric and satisfies the Jacobi identity ([[§B8.1 Poisson Brackets#^thm-b8-1-2|CM Theorem §B8.1.2]]), so the phase-space functions form a Lie algebra: [[§B8.1 Poisson Brackets#^rem-b8-1-1|CM Remark: The structure behind the four rules]].
> - In quantum mechanics the commutator of operators has the same algebra, Jacobi identity included: [[§B2.4 Commutators and the Generalized Uncertainty Principle#^thm-b2-4-1|QM Theorem §B2.4.1]].

The three terms come from one by permuting $X, Y, Z$ cyclically: “move $Y$ to the left position, $Z$ one over to the left, and $X$ jumps to the last position.”

> [!theorem] Proposition §54.4: Commutators of an Associative Product
> Let $A$ be a real vector space with a bilinear *associative* product $(X, Y) \mapsto X \ast Y$. Then the commutator $[X, Y] = X \ast Y - Y \ast X$ is bilinear, skew-symmetric, and satisfies the [[§54 Lie Bracket and Lie Algebra#^def-54-2|Jacobi identity]]; so $(A, [\cdot,\cdot])$ is a [[§54 Lie Bracket and Lie Algebra#^def-54-2|Lie algebra]].

^prop-54-4

> [!proof]+ Proof
> *(Stated in Lecture 16 as “a general fact”; filled in. “The key thing is that it be an associative product.”)* By Definition [[§54 Lie Bracket and Lie Algebra#^def-54-2|§54.2]], three properties of the commutator have to be checked; it takes values in $A$, since $A$ is closed under $\ast$ and subtraction. Bilinearity of $\ast$ means $(aX + bX') \ast Y = a\,X \ast Y + b\,X' \ast Y$ and $X \ast (aY + bY') = a\,X \ast Y + b\,X \ast Y'$ for $a, b \in \mathbb{R}$.
>
> *Skew-symmetry.* Directly from the definition, $[Y, X] = Y \ast X - X \ast Y = -(X \ast Y - Y \ast X) = -[X, Y]$.
>
> *Bilinearity.* In the first argument, by the bilinearity of $\ast$ in each of its two slots,
>
> $$
> [aX + bX', Y] = (aX + bX') \ast Y - Y \ast (aX + bX') = a\,X \ast Y + b\,X' \ast Y - a\,Y \ast X - b\,Y \ast X' = a\,[X, Y] + b\,[X', Y] .
> $$
>
> In the second argument it follows from the first and skew-symmetry:
>
> $$
> [X, aY + bY'] = -[aY + bY', X] = -a\,[Y, X] - b\,[Y', X] = a\,[X, Y] + b\,[X, Y'] .
> $$
>
> *Jacobi identity.* By associativity, triple products can be written without parentheses, $XYZ = (X \ast Y) \ast Z = X \ast (Y \ast Z)$. Expanding the inner bracket and then the outer one with the bilinearity of $\ast$,
>
> $$
> [X, [Y, Z]{]} = X \ast (Y \ast Z - Z \ast Y) - (Y \ast Z - Z \ast Y) \ast X = XYZ - XZY - YZX + ZYX .
> $$
>
> The other two terms of the Jacobi identity come from this one by the cyclic renaming $X \to Y \to Z \to X$, applied once and twice. Permuting cyclically gives
>
> $$
> [Y,[Z,X]{]} = YZX - YXZ - ZXY + XZY, \qquad [Z,[X,Y]{]} = ZXY - ZYX - XYZ + YXZ .
> $$
>
> In the sum of the three lines, each of the six words appears once with each sign: $XYZ$ with $+$ in the first and $-$ in the third; $XZY$ with $-$ in the first and $+$ in the second; $YZX$ with $-$ in the first and $+$ in the second; $ZYX$ with $+$ in the first and $-$ in the third; $YXZ$ with $-$ in the second and $+$ in the third; $ZXY$ with $-$ in the second and $+$ in the third. So the sum is $0$, and $(A, [\cdot,\cdot])$ is a Lie algebra.

^pf-54-4

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-2|Def. §54.2]]

> [!example] Example §54.2: Matrices
> $\operatorname{Mat}(n, \mathbb{R})$, with the commutator $[A, B] = AB - BA$ of matrix multiplication, is a [[§54 Lie Bracket and Lie Algebra#^def-54-2|Lie algebra]], by [[§54 Lie Bracket and Lie Algebra#^prop-54-4|Proposition §54.4]].

^ex-54-2

> [!theorem] Corollary §54.5: Vector Fields Form a Lie Algebra
> $\big(\mathfrak{X}(M), [\cdot,\cdot]\big)$ is a [[§54 Lie Bracket and Lie Algebra#^def-54-2|Lie algebra]].
>
> *Lee: Proposition 8.28*

^cor-54-5

> [!proof]+ Proof
> *(Lecture 16: the bracket of fields “comes from the product, which is the composition, which is associative.” Filled in.)* By Definition [[§54 Lie Bracket and Lie Algebra#^def-54-2|§54.2]], what has to be shown is that $\mathfrak{X}(M)$ is a real vector space, that the bracket maps $\mathfrak{X}(M) \times \mathfrak{X}(M)$ into $\mathfrak{X}(M)$, and that it is bilinear, skew-symmetric and satisfies the Jacobi identity. In this proof write $D_\mathbf{X}$ for $\mathbf{X}$ regarded as an operator (Lemma [[§52 Vector Fields#^lem-52-3|§52.3]]), to keep the field and its operator apart.
>
> *The space and the bracket.* $\mathfrak{X}(M)$ is a real vector space by Proposition [[§52 Vector Fields#^prop-52-2|§52.2]]. By Lemma [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], $\mathfrak{X}(M)$, identified with the derivations, is closed under the commutator: for $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$ the commutator of $D_\mathbf{X}$ and $D_\mathbf{Y}$ is the operator of the vector field $[\mathbf{X}, \mathbf{Y}]$,
>
> $$
> D_{[\mathbf{X}, \mathbf{Y}]} = D_\mathbf{X} \circ D_\mathbf{Y} - D_\mathbf{Y} \circ D_\mathbf{X} .
> $$
>
> *The operators form an associative algebra.* Let $A$ be the set of $\mathbb{R}$-linear operators on $C^\infty(M)$ (Definition [[§52 Vector Fields#^def-52-4|§52.4]]), a real vector space under $(aP + bQ)f = a\,Pf + b\,Qf$, with the product $P \ast Q = P \circ Q$, again a linear operator. Composition of maps is associative. It is bilinear: $\big((aP + bP') \circ Q\big)f = a\,P(Qf) + b\,P'(Qf)$ by the definition of the operations, and $\big(P \circ (aQ + bQ')\big)f = P(a\,Qf + b\,Q'f) = a\,P(Qf) + b\,P(Q'f)$ because $P$ is linear. So the linear operators on $C^\infty(M)$ form an associative algebra under composition, and by Proposition [[§54 Lie Bracket and Lie Algebra#^prop-54-4|§54.4]] their commutator $[P, Q] = P \circ Q - Q \circ P$ is bilinear, skew-symmetric and satisfies the Jacobi identity. The display above reads $D_{[\mathbf{X}, \mathbf{Y}]} = [D_\mathbf{X}, D_\mathbf{Y}]$.
>
> *From operators to fields.* The map $\mathbf{X} \mapsto D_\mathbf{X}$ is linear: for $f \in C^\infty(M)$ and $p \in M$, by Definition [[§52 Vector Fields#^def-52-2|§52.2]] and the pointwise operations of $T_pM$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]),
>
> $$
> \big(D_{a\mathbf{X} + b\mathbf{Y}} f\big)(p) = \big(a\,\mathbf{X}_p + b\,\mathbf{Y}_p\big)[f] = a\,\mathbf{X}_p[f] + b\,\mathbf{Y}_p[f] = \big((a\,D_\mathbf{X} + b\,D_\mathbf{Y}) f\big)(p) .
> $$
>
> It is injective, by the uniqueness in Proposition [[§52 Vector Fields#^prop-52-7|§52.7]]. So an identity between fields holds as soon as the corresponding identity between their operators holds. Using $D_{[\mathbf{X}, \mathbf{Y}]} = [D_\mathbf{X}, D_\mathbf{Y}]$ and the linearity of $\mathbf{X} \mapsto D_\mathbf{X}$:
> - *bilinearity:* $D_{[a\mathbf{X} + b\mathbf{X}', \mathbf{Y}]} = [a\,D_\mathbf{X} + b\,D_{\mathbf{X}'}, D_\mathbf{Y}] = a\,[D_\mathbf{X}, D_\mathbf{Y}] + b\,[D_{\mathbf{X}'}, D_\mathbf{Y}] = D_{a[\mathbf{X}, \mathbf{Y}] + b[\mathbf{X}', \mathbf{Y}]}$, and in the second argument $D_{[\mathbf{X}, a\mathbf{Y} + b\mathbf{Y}']} = [D_\mathbf{X}, a\,D_\mathbf{Y} + b\,D_{\mathbf{Y}'}] = a\,[D_\mathbf{X}, D_\mathbf{Y}] + b\,[D_\mathbf{X}, D_{\mathbf{Y}'}] = D_{a[\mathbf{X}, \mathbf{Y}] + b[\mathbf{X}, \mathbf{Y}']}$;
> - *skew-symmetry:* $D_{[\mathbf{Y}, \mathbf{X}]} = [D_\mathbf{Y}, D_\mathbf{X}] = -[D_\mathbf{X}, D_\mathbf{Y}] = D_{-[\mathbf{X}, \mathbf{Y}]}$;
> - *Jacobi:* applying the identity twice, $D_{[\mathbf{X}, [\mathbf{Y}, \mathbf{Z}]{]}} = [D_\mathbf{X}, D_{[\mathbf{Y}, \mathbf{Z}]}] = [D_\mathbf{X}, [D_\mathbf{Y}, D_\mathbf{Z}]{]}$, and the same with $\mathbf{X}, \mathbf{Y}, \mathbf{Z}$ renamed cyclically; adding the three,
>
> $$
> D_{[\mathbf{X}, [\mathbf{Y}, \mathbf{Z}]{]} + [\mathbf{Y}, [\mathbf{Z}, \mathbf{X}]{]} + [\mathbf{Z}, [\mathbf{X}, \mathbf{Y}]{]}} = [D_\mathbf{X}, [D_\mathbf{Y}, D_\mathbf{Z}]{]} + [D_\mathbf{Y}, [D_\mathbf{Z}, D_\mathbf{X}]{]} + [D_\mathbf{Z}, [D_\mathbf{X}, D_\mathbf{Y}]{]} = 0 = D_\mathbf{0} .
> $$
>
> By injectivity each identity holds between the fields themselves; in particular the Jacobi identity holds on $\mathfrak{X}(M)$.

^pf-54-5

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[§54 Lie Bracket and Lie Algebra#^def-54-2|Def. §54.2]], [[§54 Lie Bracket and Lie Algebra#^prop-54-4|§54.4]], [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], [[§52 Vector Fields#^lem-52-3|§52.3]], [[§52 Vector Fields#^prop-52-7|§52.7]], [[§52 Vector Fields#^prop-52-2|§52.2]], [[§52 Vector Fields#^def-52-4|Def. §52.4]], [[§52 Vector Fields#^def-52-2|Def. §52.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

“Which I don't recommend you check by hand. It's a big computation.” The Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional (for $\dim M \ge 1$). The finite-dimensional Lie algebras of [[§56 Lie Groups and Left-Invariant Vector Fields|§56]] sit inside it.

The bracket of two vector fields is one instance of a general fact about the ring of differential operators ([[§53 Differential Operators|§53]]): a commutator is always of lower order than the composites it is made from.

> [!theorem] Proposition §54.6: Commutators Lower the Order
> For operators $P, Q$ write $[P, Q] = P \circ Q - Q \circ P$, as in [[§54 Lie Bracket and Lie Algebra#^def-54-1|Definition §54.1]]. For the generators of $\mathrm{Diff}(M)$ ([[§53 Differential Operators#^def-53-2|Definition §53.2]]), with $g, h \in C^\infty(M)$ and $\mathbf{X}, \mathbf{Y} \in \mathfrak{X}(M)$:
> 1. $[m_g, m_h] = 0$;
> 2. $[D_\mathbf{X}, m_g] = m_{\mathbf{X}g}$;
> 3. $[D_\mathbf{X}, D_\mathbf{Y}] = D_{[\mathbf{X}, \mathbf{Y}]}$.
>
> Consequently, if $P \in \mathrm{Diff}_k(M)$ and $Q \in \mathrm{Diff}_l(M)$, then $[P, Q] \in \mathrm{Diff}_{k+l-1}(M)$ ([[§53 Differential Operators#^def-53-3|Definition §53.3]]).

^prop-54-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) is [[§53 Differential Operators#^prop-53-1|Proposition §53.1]], (2) is [[§53 Differential Operators#^prop-53-2|Proposition §53.2]] (2), and (3) is [[§54 Lie Bracket and Lie Algebra#^lem-54-1|Lemma §54.1]], read with $D_\mathbf{X}$ written out. So for generators $A, B$ of orders $a, b \in \{0, 1\}$ ($0$ for a multiplication, $1$ for a vector field), $[A, B] \in \mathrm{Diff}_{a+b-1}(M)$. Two identities, checked by expanding (each side of the first is $PQR - QRP$),
>
> $$
> [P, Q \circ R] = [P, Q] \circ R + Q \circ [P, R], \qquad [P \circ Q, R] = P \circ [Q, R] + [P, R] \circ Q ,
> $$
>
> carry this to composites, using [[§53 Differential Operators#^prop-53-3|Proposition §53.3]] (2).
>
> *A generator against a composite.* Let $A$ have order $a$ and $B = B_1 \circ \cdots \circ B_s$ be a composite of generators of orders $b_i$, $l = \sum_i b_i$. By induction on $s$ ($s = 0$: $[A, \mathrm{id}] = 0$), with $B' = B_2 \circ \cdots \circ B_s$,
>
> $$
> [A, B_1 \circ B'] = [A, B_1] \circ B' + B_1 \circ [A, B'] \in \mathrm{Diff}_{a + b_1 - 1} \circ \mathrm{Diff}_{l - b_1} + \mathrm{Diff}_{b_1} \circ \mathrm{Diff}_{a + l - b_1 - 1} \subseteq \mathrm{Diff}_{a + l - 1} .
> $$
>
> *A composite against a composite.* Let $A = A_1 \circ \cdots \circ A_r$ have orders $a_i$, $k = \sum_i a_i$; by induction on $r$ ($r = 0$: $[\mathrm{id}, B] = 0$), with $A' = A_2 \circ \cdots \circ A_r$,
>
> $$
> [A_1 \circ A', B] = A_1 \circ [A', B] + [A_1, B] \circ A' \in \mathrm{Diff}_{a_1} \circ \mathrm{Diff}_{k - a_1 + l - 1} + \mathrm{Diff}_{a_1 + l - 1} \circ \mathrm{Diff}_{k - a_1} \subseteq \mathrm{Diff}_{k + l - 1} .
> $$
>
> *Sums.* The commutator is bilinear. A $P \in \mathrm{Diff}_k(M)$ is a sum of composites with $k' \le k$ vector-field factors, a $Q \in \mathrm{Diff}_l(M)$ one of composites with $l' \le l$, and each $[\text{composite}, \text{composite}]$ lies in $\mathrm{Diff}_{k' + l' - 1} \subseteq \mathrm{Diff}_{k + l - 1}$ ([[§53 Differential Operators#^prop-53-3|Proposition §53.3]] (1)).

^pf-54-6

*Uses:* [[§54 Lie Bracket and Lie Algebra#^def-54-1|Def. §54.1]], [[§53 Differential Operators#^def-53-2|Def. §53.2]], [[§53 Differential Operators#^def-53-3|Def. §53.3]], [[§53 Differential Operators#^prop-53-1|§53.1]], [[§53 Differential Operators#^prop-53-2|§53.2]], [[§54 Lie Bracket and Lie Algebra#^lem-54-1|§54.1]], [[§53 Differential Operators#^prop-53-3|§53.3]]

So two differential operators commute “up to lower order”. For $k = l = 1$, applied to $D_\mathbf{X}$ and $D_\mathbf{Y}$, the second-order parts of $\mathbf{X} \circ \mathbf{Y}$ and $\mathbf{Y} \circ \mathbf{X}$ cancel, as in [[§54 Lie Bracket and Lie Algebra#^ex-54-1|Example §54.1]]; what is left lies in $\mathrm{Diff}_1(M)$ and kills constants, and is the vector field $[\mathbf{X}, \mathbf{Y}]$ ([[§53 Differential Operators#^prop-53-3|Proposition §53.3]] (4)).

> [!example] Example §54.3: The Cross Product
> $\mathbb{R}^3$ with the [[§96 The Cross Product#^def-96-1|cross product]] is a [[§54 Lie Bracket and Lie Algebra#^def-54-2|Lie algebra]], and the [[§25 The Geometric Tangent Space#^def-25-3|hat map]] of [[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]] is an isomorphism of Lie algebras onto $\operatorname{Skew}(3, \mathbb{R}) = \mathfrak{so}(3)$ with the [[§54 Lie Bracket and Lie Algebra#^ex-54-2|matrix commutator]]:
>
> $$
> [\hat a, \hat b] = \hat a \hat b - \hat b \hat a = \widehat{a \times b} .
> $$

^ex-54-3

> [!proof]+ Proof
> *(Lecture 16 mentioned only that the cross product satisfies the Jacobi identity — “if you want to be really mean to your 215 students, give them the Jacobi identity for the cross product. Don't do that.” The proof via the hat map is filled in.)* There are three steps: the bracket identity $[\hat a, \hat b] = \widehat{a \times b}$; that $\operatorname{Skew}(3,\mathbb{R})$ is a Lie algebra under the commutator; and the transfer of the Lie algebra axioms to $(\mathbb{R}^3, \times)$ along the hat map.
>
> *The identity.* Two $3 \times 3$ matrices are equal if they agree on every $x \in \mathbb{R}^3$, so fix $x$. By Definition [[§25 The Geometric Tangent Space#^def-25-3|§25.3]], $\hat v\, y = v \times y$ for all $v, y$, so $\hat a \hat b\, x = a \times (b \times x)$ and $\hat b \hat a\, x = b \times (a \times x)$. The vector identity $u \times (v \times w) = v\,(u \cdot w) - w\,(u \cdot v)$, with $(u, v, w) = (a, b, x)$ and with $(u, v, w) = (b, a, x)$, gives
>
> $$
> a \times (b \times x) = b\,(a \cdot x) - x\,(a \cdot b), \qquad b \times (a \times x) = a\,(b \cdot x) - x\,(b \cdot a) ,
> $$
>
> and the terms in $x$ cancel in the difference because $a \cdot b = b \cdot a$. The same identity with $(u, v, w) = (x, a, b)$, together with the antisymmetry of the cross product, gives $(a \times b) \times x = -\,x \times (a \times b) = -\big(a\,(x \cdot b) - b\,(x \cdot a)\big) = b\,(a \cdot x) - a\,(b \cdot x)$. Together, for every $x \in \mathbb{R}^3$,
>
> $$
> [\hat a, \hat b]\, x = a \times (b \times x) - b \times (a \times x) = b\,(a \cdot x) - a\,(b \cdot x) = (a \times b) \times x = \widehat{a \times b}\, x .
> $$
>
> *$\operatorname{Skew}(3,\mathbb{R})$ is a Lie algebra.* It is a linear subspace of $\operatorname{Mat}(3,\mathbb{R})$, since $A^{\mathsf T} = -A$ is a linear condition. It is closed under the commutator: for skew $A, B$, using $(XY)^{\mathsf T} = Y^{\mathsf T} X^{\mathsf T}$,
>
> $$
> [A,B]^{\mathsf T} = B^{\mathsf T} A^{\mathsf T} - A^{\mathsf T} B^{\mathsf T} = [B^{\mathsf T}, A^{\mathsf T}] = (-B)(-A) - (-A)(-B) = [B, A] = -[A,B] .
> $$
>
> So the commutator restricts to a bracket $\operatorname{Skew}(3,\mathbb{R}) \times \operatorname{Skew}(3,\mathbb{R}) \to \operatorname{Skew}(3,\mathbb{R})$, and bilinearity, skew-symmetry and the Jacobi identity hold there because they hold for all matrices; so it is a Lie algebra by Example [[§54 Lie Bracket and Lie Algebra#^ex-54-2|§54.2]].
>
> *Transfer.* The hat map is a linear isomorphism (Definition [[§25 The Geometric Tangent Space#^def-25-3|§25.3]]) carrying $\times$ to the commutator, $\widehat{a \times b} = [\hat a, \hat b]$; so the cross product inherits bilinearity, skew-symmetry and the Jacobi identity — without the big computation. In detail, for $a, a', b, b', c \in \mathbb{R}^3$ and $s, t \in \mathbb{R}$, using the linearity of the hat map, the identity, and the properties of the commutator on $\operatorname{Skew}(3,\mathbb{R})$:
> - *bilinearity:* $\widehat{(sa + ta') \times b} = [s\hat a + t\hat a', \hat b] = s\,[\hat a, \hat b] + t\,[\hat a', \hat b] = s\,\widehat{a \times b} + t\,\widehat{a' \times b}$, and $\widehat{a \times (sb + tb')} = [\hat a, s\hat b + t\hat b'] = s\,\widehat{a \times b} + t\,\widehat{a \times b'}$;
> - *skew-symmetry:* $\widehat{b \times a} = [\hat b, \hat a] = -[\hat a, \hat b] = -\widehat{a \times b}$;
> - *Jacobi:* applying the identity twice, $\widehat{a \times (b \times c)} = [\hat a, \widehat{b \times c}] = [\hat a, [\hat b, \hat c]{]}$, and likewise with $a, b, c$ renamed cyclically, so
>
> $$
> \widehat{a \times (b \times c)} + \widehat{b \times (c \times a)} + \widehat{c \times (a \times b)} = [\hat a, [\hat b, \hat c]{]} + [\hat b, [\hat c, \hat a]{]} + [\hat c, [\hat a, \hat b]{]} = 0 .
> $$
>
> Since the hat map is linear and injective, each equality between hats is the corresponding equality in $\mathbb{R}^3$. So $(\mathbb{R}^3, \times)$ is a Lie algebra, and the hat map, a linear bijection with $\widehat{a \times b} = [\hat a, \hat b]$, is an isomorphism of Lie algebras onto $\operatorname{Skew}(3,\mathbb{R})$.

^pf-ex-54-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-3|Def. §25.3]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]], [[§54 Lie Bracket and Lie Algebra#^ex-54-2|Ex. §54.2]], [[§54 Lie Bracket and Lie Algebra#^def-54-2|Def. §54.2]]

> [!remark]- Connections
> - The cross product and its algebraic properties, proved by components: [[§96 The Cross Product#^def-96-1|Calc Def. §96.1]], [[§96 The Cross Product#^thm-96-8|Calc §96.8]].
> - The same computation for the infinitesimal rotations of quantum mechanics: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], with [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§45 SU(2) → SO(3)꞉ The Double Cover#^thm-45-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§54 Lie Bracket and Lie Algebra#^ex-54-3|Ex. §54.3]]; and Lie groups in [[§56 Lie Groups and Left-Invariant Vector Fields#^prop-56-1|§56.1]].
