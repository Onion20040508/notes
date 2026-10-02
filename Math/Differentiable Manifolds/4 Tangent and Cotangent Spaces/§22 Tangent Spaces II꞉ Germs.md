---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 22
tags: [differentiable-manifolds, math591]
---
← [[§21 Transversality]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§23 Derivations and the Abstract Tangent Space]] →

*Stage: abstract — Tangent vectors as derivations of germs — available for every manifold, including those built by quotients. First the motivation, then germs, the objects derivations act on.*

## From Tangent Vectors to Derivations

*Motivation only; nothing in this subsection is used later, but it is where the abstract definition comes from.*

Keep $M = F^{-1}(c)$ and, by Lemmas [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-1|§20.1]] and [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]], assume $M$ is the graph of a smooth $G : A \to \mathbb{R}^k$ over an open $A \subseteq \mathbb{R}^n$, with chart $\varphi : M \to A$ the projection $(x, G(x)) \mapsto x$ and $p = (x_0, G(x_0))$. Let $f : M \to \mathbb{R}$ be smooth, so that $f_\varphi = f \circ \varphi^{-1} : A \to \mathbb{R}$ is smooth (Definition [[§15 Smooth Functions and Smooth Maps#^def-15-2|§15.2]]).

Given $v \in T^{\mathrm{geo}}_pM$, Lemma [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]] provides a unique $u \in \mathbb{R}^n$ with $v = (u, G'(x_0)u)$. Lift the straight line $t \mapsto x_0 + tu$ from the chart to the manifold:

$$
\gamma(t) = \big(x_0 + tu,\; G(x_0 + tu)\big), \qquad \gamma(0) = p, \quad \gamma'(0) = v .
$$

![[m591-12-1.svg]]
*The chart triangle for the graph case, as drawn on the board. Downstairs is the open set $A \subseteq \mathbb{R}^n$; upstairs is the manifold. The chart $\varphi(x, G(x)) = x$ and its inverse $\varphi^{-1}(x) = (x, G(x))$ pass between them, and the triangle commutes: $f = f_\varphi \circ \varphi$. Smoothness of $f$* means *smoothness of $f_\varphi$, so every computation with $f$ can be pushed downstairs, done in ordinary calculus, and read back. That is the manoeuvre in the next definition: the curve is built downstairs as a straight line, lifted upstairs by $\varphi^{-1}$, and the derivative taken downstairs again. “Upstairs and downstairs are very useful terminologies.”*

> [!definition] Definition §22.1: The Directional Derivative Attached to a Tangent Vector
> Let $M \subseteq \mathbb{R}^{n+k}$ be the graph of a smooth $G : A \to \mathbb{R}^k$ on an open $A \subseteq \mathbb{R}^n$, with chart $\varphi(x, G(x)) = x$, and $p = (x_0, G(x_0))$. Let $v \in T^{\mathrm{geo}}_pM$, let $u \in \mathbb{R}^n$ be the vector with $v = (u, G'(x_0)u)$ (Lemma [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]]), and let $\gamma(t) = (x_0 + tu, G(x_0 + tu))$ be the lifted line, a curve in $M$ with $\gamma(0) = p$ and $\gamma'(0) = v$. For $f$ a smooth real-valued function on a neighbourhood of $p$ in $M$, set
>
> $$
> D_v(f) \;=\; \frac{d}{dt}\Big|_{t=0} f(\gamma(t)) \;=\; \frac{d}{dt}\Big|_{t=0} f_\varphi(x_0 + tu) \;=\; u \cdot \nabla f_\varphi(x_0),
> $$
>
> the second equality because $\varphi(\gamma(t)) = x_0 + tu$ and $f = f_\varphi \circ \varphi$, the third by the [[Multivariable Chain Rule|chain rule]]. So $D_v$ takes a smooth function defined near $p$ and returns a real number, and it depends only on the values of $f$ near $p$ — which is what the germs of the next subsection make precise.
>
> *Lee: Proposition 3.2 (in $\mathbb{R}^n$)*

^def-22-1

> [!remark]- Connections
> - The Euclidean directional derivative and its gradient formula: [[Directional Derivative Formula|452 §7.1 (Directional Derivative Formula)]].
> - In $\mathbb{R}^n$ the trade $v \leftrightarrow D_v$ is exactly the identification of [[§25 The Differential in Coordinates#^prop-25-5|§25.5]]; on an arbitrary manifold, velocities of curves: [[§26 Tangent Vectors as Velocities of Curves#^def-26-1|Def. §26.1]].

> [!theorem] Proposition §22.1: Basic Properties of $D_v$
> In the setting of Definition [[§22 Tangent Spaces II꞉ Germs#^def-22-1|§22.1]]:
> 1. $D_v(f)$ depends only on the germ of $f$ at $p$;
> 2. if $\sigma$ is *any* smooth curve in $M$ with $\sigma(0) = p$ and $\sigma'(0) = v$, then $D_v(f) = \frac{d}{dt}\big|_{t=0} f(\sigma(t))$; so $D_v$ depends on $v$ alone, not on the curve used to define it;
> 3. $D_v$ is linear and obeys the product rule $D_v(fg) = f(p)\,D_v(g) + g(p)\,D_v(f)$.

^prop-22-1

> [!proof]+ Proof
> (1) $\gamma(t)$ lies in any given neighbourhood of $p$ for $|t|$ small, so only the values of $f$ near $p$ enter — “we don't need the whole manifold.” (2) The chart $\varphi$ is the restriction to $M$ of the linear projection $(x,y) \mapsto x$, so $\varphi \circ \sigma$ is a smooth curve in $A$ whose velocity at $0$ is the first component $u$ of $v$. Since $f \circ \sigma = f_\varphi \circ (\varphi \circ \sigma)$, the chain rule gives $\frac{d}{dt}\big|_0 f(\sigma(t)) = \nabla f_\varphi(x_0) \cdot u = D_v(f)$. (3) Linearity and the product rule are inherited from those of the gradient, $\nabla(f_\varphi g_\varphi) = f_\varphi \nabla g_\varphi + g_\varphi \nabla f_\varphi$, evaluated at $x_0$, where $f_\varphi(x_0) = f(p)$.

^pf-22-1

*Uses:* [[§22 Tangent Spaces II꞉ Germs#^def-22-1|Def. §22.1]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]], [[Multivariable Chain Rule|452 §10.2]], [[§6 Differentiability#^thm-6-4|452 §6.4]]

> [!theorem] Proposition §22.2: $D_v$ Determines $v$
> The map $v \mapsto D_v$ is injective on $T^{\mathrm{geo}}_pM$: if $D_v = D_{v'}$ then $v = v'$.
>
> *Lee: Proposition 3.2(b)*

^prop-22-2

> [!proof]+ Proof
> Write $v = (u, G'(x_0)u)$ and $v' = (u', G'(x_0)u')$. For $i = 1, \ldots, n$ let $x^i : M \to \mathbb{R}$ be the $i$-th coordinate of the chart, so $(x^i)_\varphi = r^i$ is the $i$-th coordinate function on $A$ and $\nabla (x^i)_\varphi = e_i$. Then $D_v(x^i) = u \cdot e_i = u^i$. If $D_v = D_{v'}$, applying both to $x^i$ gives $u^i = (u')^i$ for every $i$, so $u = u'$ and hence $v = v'$.

^pf-22-2

*Uses:* [[§22 Tangent Spaces II꞉ Germs#^def-22-1|Def. §22.1]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^lem-20-2|§20.2]]

> [!remark] Remark
> Uribe's version of this argument: the numbers $D_v(f) = u \cdot \nabla f_\varphi(x_0)$ range over the dot products of $u$ with an arbitrary vector, because the gradient of a function at a point can be prescribed freely; so knowing all of them determines $u$. Taking $f$ to be the coordinate functions is the cheapest way to prescribe it.
>
> The conclusion is that a tangent vector loses nothing by being replaced by the operator it defines — and the operator, unlike the vector, makes sense with no ambient space in sight. *Tangent vectors will be defined as operators:* you feed them a function and they return a number.

^rem-22-1

## Germs

Point (1) of the [[§22 Tangent Spaces II꞉ Germs#^prop-22-1|note above]] is made official first: the objects a derivation eats are not functions but germs.

> [!definition] Definition §22.2: Agreement Near a Point
> Let $M$ be a smooth manifold and $p \in M$. Consider pairs $(f, U)$ with $U \subseteq M$ open, $p \in U$, and $f : U \to \mathbb{R}$ smooth. Two such pairs **agree near $p$**, written $(f,U) \sim (g,V)$, if
>
> $$
> \text{there is an open } W \text{ with } p \in W \subseteq U \cap V \text{ and } f|_W = g|_W .
> $$

^def-22-2

> [!theorem] Proposition §22.3: Agreement Near a Point Is an Equivalence Relation
> 1. $\sim$ is an equivalence relation.
> 2. Finitely many pairs in one equivalence class agree on a common open neighbourhood of $p$.

^prop-22-3

> [!proof]+ Proof
> (1) *Reflexive:* take $W = U$. *Symmetric:* the condition is symmetric in the two pairs. *Transitive:* if $f = g$ on an open $W_1 \ni p$ and $g = h$ on an open $W_2 \ni p$, then $f = h$ on $W_1 \cap W_2$, which is open, contains $p$, and lies in both domains.
>
> (2) If $(f_1,U_1), \ldots, (f_k,U_k)$ are equivalent, then for each $i$ there is an open $W_i \ni p$ on which $f_1 = f_i$. On $W = W_2 \cap \cdots \cap W_k$, which is open and contains $p$, all the $f_i$ equal $f_1$. Both parts use only that a *finite* intersection of open sets is open.

^pf-22-3

*Uses:* [[§22 Tangent Spaces II꞉ Germs#^def-22-2|Def. §22.2]], [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]

> [!definition] Definition §22.3: Germs of Smooth Functions
> An equivalence class $[f]$ of the relation $\sim$ of Definition [[§22 Tangent Spaces II꞉ Germs#^def-22-2|§22.2]] is a **($C^\infty$) germ at $p$**, and each pair $(f,U)$ in it is a **representative** of the germ. The set of all germs at $p$ is denoted $C_p^\infty(M)$.
>
> *Lee: no counterpart; the course's germ-based route (Lee uses $C^\infty(M)$; see Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-3|§23.3]])*

^def-22-3

![[m591-12-2.svg]]
*Two pairs $(f, U)$ and $(g, V)$ that agree on an open $W$ with $p \in W \subseteq U \cap V$ define the same germ, $[f] = [g]$ in $C_p^\infty(M)$.*

> [!example] Example §22.1: No Neighbourhood Serves a Whole Germ
> Part (2) of Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-3|§22.3]] fails for infinitely many representatives. Work at $p = 0 \in \mathbb{R}$. Let $h(s) = e^{-1/s}$ for $s > 0$ and $h(s) = 0$ for $s \le 0$, the smooth flat function (see Example [[§22 Tangent Spaces II꞉ Germs#^ex-22-2|§22.2]] below), and put
>
> $$
> f_n(x) = h\big(x^2 - 1/n^2\big), \qquad n = 1, 2, 3, \ldots
> $$
>
> Each $f_n$ is smooth on all of $\mathbb{R}$ and vanishes exactly on $[-1/n, 1/n]$, so $(f_n, \mathbb{R}) \sim (0, \mathbb{R})$: every $f_n$ represents the zero germ. Yet the set on which all of them agree with $0$ is $\bigcap_n [-1/n, 1/n] = \{0\}$, which contains no open neighbourhood of $0$. The same happens, even more simply, with the representatives $\big(0, (-1/n, 1/n)\big)$: no open set around $0$ lies in all of their domains.

^ex-22-1

> [!remark] Remark
> Nothing in the theory needs a common neighbourhood for a whole class. Every construction on germs — sums, products and evaluation (Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]]), derivations, pullbacks — handles finitely many representatives at a time, and part (2) supplies the common neighbourhood for those. The obstruction in the example is exactly that an *infinite* intersection of open sets need not be open. This is also the precise sense in which a germ is not a function on any particular neighbourhood of $p$: its representatives can be shrunk at will, but there is no smallest domain to shrink them to.

^rem-22-2

> [!theorem] Proposition §22.4: $C_p^\infty(M)$ Is an $\mathbb{R}$-Algebra
> The operations
>
> $$
> [f] + [g] = [f|_W + g|_W], \qquad [f]\,[g] = [f|_W \cdot g|_W], \qquad \lambda[f] = [\lambda f],
> $$
>
> where $W$ is any open set with $p \in W \subseteq U \cap V$, are well defined and make $C_p^\infty(M)$ a commutative ring with unit $[1]$ and an $\mathbb{R}$-vector space — that is, a commutative $\mathbb{R}$-algebra. Moreover the evaluation map
>
> $$
> [f] \longmapsto [f](p) := f(p)
> $$
>
> is a well-defined $\mathbb{R}$-algebra homomorphism $C_p^\infty(M) \to \mathbb{R}$.
>
> *Lee: no counterpart; the course's germ-based route*

^prop-22-4

> [!proof]+ Proof
> *(Lecture 8 sketched the operations — “taking representatives … and shrinking to a common domain” — and skipped the checks as “tedious”; they are filled in here.)* *Existence of $W$ and smoothness.* $U \cap V$ is open and contains $p$, so $W = U \cap V$ will do; $f|_W + g|_W$ and $f|_W\, g|_W$ are smooth on $W$, so they define germs.
>
> *Independence of representatives.* Suppose $(f,U) \sim (f', U')$ and $(g,V) \sim (g',V')$, say $f = f'$ on $W_1 \ni p$ and $g = g'$ on $W_2 \ni p$. On the open set $W_1 \cap W_2 \ni p$ the four functions satisfy $f + g = f' + g'$ and $fg = f'g'$ pointwise, so the resulting germs agree. Independence of the auxiliary $W$ is the same argument with $f = f'$, $g = g'$.
>
> *Algebra axioms.* Each is an identity between germs that holds for representatives on a common domain, hence holds after passing to classes.
>
> *Evaluation.* If $(f,U) \sim (g,V)$ then $f = g$ near $p$, in particular $f(p) = g(p)$; and evaluation of functions is compatible with sums and products.

^pf-22-4

*Uses:* [[§22 Tangent Spaces II꞉ Germs#^def-22-2|Def. §22.2]], [[§22 Tangent Spaces II꞉ Germs#^def-22-3|Def. §22.3]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-3|§22.3]]

> [!definition] Definition §22.4: Evaluation of a Germ
> The **value** of a germ $[f] \in C_p^\infty(M)$ at $p$ is $[f](p) := f(p)$, independent of the representative by Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]]. The map $C_p^\infty(M) \to \mathbb{R}$, $[f] \mapsto [f](p)$, is **evaluation** at $p$.

^def-22-4

> [!remark] Remark: How to Think About a Germ
> Uribe: “when I think of a germ, I think of a representative — a smooth function defined in a neighbourhood — but I know that it is a germ, which means I can shrink its domain arbitrarily, as long as I shrink it to a neighbourhood of $p$.” In practice one works with representatives and checks at the end that the answer is unchanged by shrinking. The formal content of the definition is exactly that shrinking is free.

^rem-22-3

![[m591-12-19.svg]]
*Two representatives of one germ, drawn as graphs over $M = \mathbb{R}$: $f$ (blue) on $U$ and $g$ (red, dashed) on $V$ agree on the shaded open set $W \ni p$ and part ways outside it. The germ $[f] = [g]$ keeps only the common piece near $p$; how large the domains are and what the functions do away from $p$ is forgotten — which is exactly why shrinking a representative's domain is free.*

> [!example] Example §22.2: Germs Versus Taylor Series
> Take $M = \mathbb{R}^n$ and $x_0 \in \mathbb{R}^n$. All partial derivatives of a function at $x_0$ depend only on its germ, so the Taylor series construction descends to a map into the ring of formal power series,
>
> $$
> \mathcal{T} : C_{x_0}^\infty(\mathbb{R}^n) \longrightarrow \mathbb{R}[\![x^1, \ldots, x^n]\!], \qquad
> \mathcal{T}[f] = \sum_{\alpha} \frac{1}{\alpha!}\, \frac{\partial^{|\alpha|} f}{\partial x^\alpha}(x_0)\, (x - x_0)^\alpha ,
> $$
>
> an $\mathbb{R}$-algebra homomorphism. It is *surjective* but *not injective*.

^ex-22-2

> [!proof]+ Justification
> Surjectivity is **Borel's theorem**: every formal power series is the Taylor series at $x_0$ of some smooth function. It is cited, not proved — Uribe: “that's not so easy to show, but it's true.” Failure of injectivity is elementary. Uribe: “You can have totally flat functions that are not zero”; the example is filled in. The function
>
> $$
> f(x) = \begin{cases} e^{-1/|x-x_0|^2}, & x \neq x_0,\\ 0, & x = x_0,\end{cases}
> $$
>
> is smooth with all partial derivatives vanishing at $x_0$ (a standard computation, not reproduced here), so $\mathcal{T}[f] = 0$ while $[f] \neq 0$.

^pf-ex-22-2

*Uses:* [[§22 Tangent Spaces II꞉ Germs#^def-22-3|Def. §22.3]], [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]

> [!remark]- Connections
> - The one-variable flat function $e^{-1/x^2}$, a smooth function that is not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; Taylor series: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]].
> - Taylor expansion in several variables: [[Multivariable Taylor's Theorem|452 §9.2 (Multivariable Taylor's Theorem)]].

> [!definition] Definition §22.5: Flat Germ
> A germ $[f] \in C_{x_0}^\infty(\mathbb{R}^n)$ is **flat** if all partial derivatives of $f$, of all orders, vanish at $x_0$; equivalently, $\mathcal{T}[f] = 0$. So the kernel of $\mathcal{T}$ consists exactly of the flat germs.

^def-22-5

> [!remark] Remark
> The moral is that a germ carries strictly more information than its Taylor series — “one of the beauties of being in the $C^\infty$ category.” This is the same phenomenon as the rigidity of $C^\omega$ noted after Definition [[§13 Differentiable Structures#^def-13-5|§13.5]]: a real-analytic germ *is* its Taylor series, which is why there are no analytic bump functions, whereas a $C^\infty$ germ has room to spare.

^rem-22-4
