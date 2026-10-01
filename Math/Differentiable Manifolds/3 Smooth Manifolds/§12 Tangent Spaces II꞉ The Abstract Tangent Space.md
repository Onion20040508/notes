---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 12
tags: [differentiable-manifolds, math591]
---
← [[§11 Tangent Spaces I꞉ The Geometric Picture]] · ↑ [[· 3 Smooth Manifolds]] · [[§13 Tangent Spaces III꞉ The Cotangent Space]] →

*Stage: abstract — Tangent vectors as derivations of germs — available for every manifold, including those built by quotients. The two notions agree wherever both exist (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]]).*

## From Tangent Vectors to Derivations

*Motivation only; nothing in this subsection is used later, but it is where the abstract definition comes from.*

Keep $M = F^{-1}(c)$ and, by Lemmas [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|§11.1]] and [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]], assume $M$ is the graph of a smooth $G : A \to \mathbb{R}^k$ over an open $A \subseteq \mathbb{R}^n$, with chart $\varphi : M \to A$ the projection $(x, G(x)) \mapsto x$ and $p = (x_0, G(x_0))$. Let $f : M \to \mathbb{R}$ be smooth, so that $f_\varphi = f \circ \varphi^{-1} : A \to \mathbb{R}$ is smooth (Definition [[§8 Differentiable Structures#^def-8-13|§8.13]]).

Given $v \in T^{\mathrm{geo}}_pM$, Lemma [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]] provides a unique $u \in \mathbb{R}^n$ with $v = (u, G'(x_0)u)$. Lift the straight line $t \mapsto x_0 + tu$ from the chart to the manifold:

$$
\gamma(t) = \big(x_0 + tu,\; G(x_0 + tu)\big), \qquad \gamma(0) = p, \quad \gamma'(0) = v .
$$

![[m591-12-1.svg]]
*The chart triangle for the graph case, as drawn on the board. Downstairs is the open set $A \subseteq \mathbb{R}^n$; upstairs is the manifold. The chart $\varphi(x, G(x)) = x$ and its inverse $\varphi^{-1}(x) = (x, G(x))$ pass between them, and the triangle commutes: $f = f_\varphi \circ \varphi$. Smoothness of $f$* means *smoothness of $f_\varphi$, so every computation with $f$ can be pushed downstairs, done in ordinary calculus, and read back. That is the manoeuvre in the next definition: the curve is built downstairs as a straight line, lifted upstairs by $\varphi^{-1}$, and the derivative taken downstairs again. “Upstairs and downstairs are very useful terminologies.”*

> [!definition] Definition §12.1: The Directional Derivative Attached to a Tangent Vector
> Let $M \subseteq \mathbb{R}^{n+k}$ be the graph of a smooth $G : A \to \mathbb{R}^k$ on an open $A \subseteq \mathbb{R}^n$, with chart $\varphi(x, G(x)) = x$, and $p = (x_0, G(x_0))$. Let $v \in T^{\mathrm{geo}}_pM$, let $u \in \mathbb{R}^n$ be the vector with $v = (u, G'(x_0)u)$ (Lemma [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]]), and let $\gamma(t) = (x_0 + tu, G(x_0 + tu))$ be the lifted line, a curve in $M$ with $\gamma(0) = p$ and $\gamma'(0) = v$. For $f$ a smooth real-valued function on a neighbourhood of $p$ in $M$, set
>
> $$
> D_v(f) \;=\; \frac{d}{dt}\Big|_{t=0} f(\gamma(t)) \;=\; \frac{d}{dt}\Big|_{t=0} f_\varphi(x_0 + tu) \;=\; u \cdot \nabla f_\varphi(x_0),
> $$
>
> the second equality because $\varphi(\gamma(t)) = x_0 + tu$ and $f = f_\varphi \circ \varphi$, the third by the [[Multivariable Chain Rule|chain rule]]. So $D_v$ takes a smooth function defined near $p$ and returns a real number, and it depends only on the values of $f$ near $p$ — which is what the germs of the next subsection make precise.
>
> *Lee: Proposition 3.2 (in $\mathbb{R}^n$)*

^def-12-1

> [!remark]- Connections
> - The Euclidean directional derivative and its gradient formula: [[Directional Derivative Formula|452 §7.1 (Directional Derivative Formula)]].
> - In $\mathbb{R}^n$ the trade $v \leftrightarrow D_v$ is exactly the identification of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]; on an arbitrary manifold, velocities of curves: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14|Def. §12.14]].

> [!theorem] Proposition §12.1: Basic Properties of $D_v$
> In the setting of Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|§12.1]]:
> 1. $D_v(f)$ depends only on the germ of $f$ at $p$;
> 2. if $\sigma$ is *any* smooth curve in $M$ with $\sigma(0) = p$ and $\sigma'(0) = v$, then $D_v(f) = \frac{d}{dt}\big|_{t=0} f(\sigma(t))$; so $D_v$ depends on $v$ alone, not on the curve used to define it;
> 3. $D_v$ is linear and obeys the product rule $D_v(fg) = f(p)\,D_v(g) + g(p)\,D_v(f)$.

^prop-12-1

> [!proof]+ Proof
> (1) $\gamma(t)$ lies in any given neighbourhood of $p$ for $|t|$ small, so only the values of $f$ near $p$ enter — “we don't need the whole manifold.” (2) The chart $\varphi$ is the restriction to $M$ of the linear projection $(x,y) \mapsto x$, so $\varphi \circ \sigma$ is a smooth curve in $A$ whose velocity at $0$ is the first component $u$ of $v$. Since $f \circ \sigma = f_\varphi \circ (\varphi \circ \sigma)$, the chain rule gives $\frac{d}{dt}\big|_0 f(\sigma(t)) = \nabla f_\varphi(x_0) \cdot u = D_v(f)$. (3) Linearity and the product rule are inherited from those of the gradient, $\nabla(f_\varphi g_\varphi) = f_\varphi \nabla g_\varphi + g_\varphi \nabla f_\varphi$, evaluated at $x_0$, where $f_\varphi(x_0) = f(p)$.

^pf-12-1

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|Def. §12.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]], [[Multivariable Chain Rule|452 §10.2]], [[§6 Differentiability#^thm-6-4|452 §6.4]]

> [!theorem] Proposition §12.2: $D_v$ Determines $v$
> The map $v \mapsto D_v$ is injective on $T^{\mathrm{geo}}_pM$: if $D_v = D_{v'}$ then $v = v'$.
>
> *Lee: Proposition 3.2(b)*

^prop-12-2

> [!proof]+ Proof
> Write $v = (u, G'(x_0)u)$ and $v' = (u', G'(x_0)u')$. For $i = 1, \ldots, n$ let $x^i : M \to \mathbb{R}$ be the $i$-th coordinate of the chart, so $(x^i)_\varphi = r^i$ is the $i$-th coordinate function on $A$ and $\nabla (x^i)_\varphi = e_i$. Then $D_v(x^i) = u \cdot e_i = u^i$. If $D_v = D_{v'}$, applying both to $x^i$ gives $u^i = (u')^i$ for every $i$, so $u = u'$ and hence $v = v'$.

^pf-12-2

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|Def. §12.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]]

> [!remark] Remark
> Uribe's version of this argument: the numbers $D_v(f) = u \cdot \nabla f_\varphi(x_0)$ range over the dot products of $u$ with an arbitrary vector, because the gradient of a function at a point can be prescribed freely; so knowing all of them determines $u$. Taking $f$ to be the coordinate functions is the cheapest way to prescribe it.
>
> The conclusion is that a tangent vector loses nothing by being replaced by the operator it defines — and the operator, unlike the vector, makes sense with no ambient space in sight. *Tangent vectors will be defined as operators:* you feed them a function and they return a number.

^rem-12-1

## Germs

Point (1) of the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|note above]] is made official first: the objects a derivation eats are not functions but germs.

> [!definition] Definition §12.2: Agreement Near a Point
> Let $M$ be a smooth manifold and $p \in M$. Consider pairs $(f, U)$ with $U \subseteq M$ open, $p \in U$, and $f : U \to \mathbb{R}$ smooth. Two such pairs **agree near $p$**, written $(f,U) \sim (g,V)$, if
>
> $$
> \text{there is an open } W \text{ with } p \in W \subseteq U \cap V \text{ and } f|_W = g|_W .
> $$

^def-12-2

> [!theorem] Proposition §12.3: Agreement Near a Point Is an Equivalence Relation
> 1. $\sim$ is an equivalence relation.
> 2. Finitely many pairs in one equivalence class agree on a common open neighbourhood of $p$.

^prop-12-3

> [!proof]+ Proof
> (1) *Reflexive:* take $W = U$. *Symmetric:* the condition is symmetric in the two pairs. *Transitive:* if $f = g$ on an open $W_1 \ni p$ and $g = h$ on an open $W_2 \ni p$, then $f = h$ on $W_1 \cap W_2$, which is open, contains $p$, and lies in both domains.
>
> (2) If $(f_1,U_1), \ldots, (f_k,U_k)$ are equivalent, then for each $i$ there is an open $W_i \ni p$ on which $f_1 = f_i$. On $W = W_2 \cap \cdots \cap W_k$, which is open and contains $p$, all the $f_i$ equal $f_1$. Both parts use only that a *finite* intersection of open sets is open.

^pf-12-3

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-2|Def. §12.2]], [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]

> [!definition] Definition §12.3: Germs of Smooth Functions
> An equivalence class $[f]$ of the relation $\sim$ of Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-2|§12.2]] is a **($C^\infty$) germ at $p$**, and each pair $(f,U)$ in it is a **representative** of the germ. The set of all germs at $p$ is denoted $C_p^\infty(M)$.
>
> *Lee: no counterpart; the course's germ-based route (Lee uses $C^\infty(M)$; see Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-7|§12.7]])*

^def-12-3

![[m591-12-2.svg]]
*Two pairs $(f, U)$ and $(g, V)$ that agree on an open $W$ with $p \in W \subseteq U \cap V$ define the same germ, $[f] = [g]$ in $C_p^\infty(M)$.*

> [!example] Example §12.1: No Neighbourhood Serves a Whole Germ
> Part (2) of Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-3|§12.3]] fails for infinitely many representatives. Work at $p = 0 \in \mathbb{R}$. Let $h(s) = e^{-1/s}$ for $s > 0$ and $h(s) = 0$ for $s \le 0$, the smooth flat function (see Example [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^ex-12-2|§12.2]] below), and put
>
> $$
> f_n(x) = h\big(x^2 - 1/n^2\big), \qquad n = 1, 2, 3, \ldots
> $$
>
> Each $f_n$ is smooth on all of $\mathbb{R}$ and vanishes exactly on $[-1/n, 1/n]$, so $(f_n, \mathbb{R}) \sim (0, \mathbb{R})$: every $f_n$ represents the zero germ. Yet the set on which all of them agree with $0$ is $\bigcap_n [-1/n, 1/n] = \{0\}$, which contains no open neighbourhood of $0$. The same happens, even more simply, with the representatives $\big(0, (-1/n, 1/n)\big)$: no open set around $0$ lies in all of their domains.

^ex-12-1

> [!remark] Remark
> Nothing in the theory needs a common neighbourhood for a whole class. Every construction on germs — sums, products and evaluation (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]]), derivations, pullbacks — handles finitely many representatives at a time, and part (2) supplies the common neighbourhood for those. The obstruction in the example is exactly that an *infinite* intersection of open sets need not be open. This is also the precise sense in which a germ is not a function on any particular neighbourhood of $p$: its representatives can be shrunk at will, but there is no smallest domain to shrink them to.

^rem-12-2

> [!theorem] Proposition §12.4: $C_p^\infty(M)$ Is an $\mathbb{R}$-Algebra
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

^prop-12-4

> [!proof]+ Proof
> *(Lecture 8 sketched the operations — “taking representatives … and shrinking to a common domain” — and skipped the checks as “tedious”; they are filled in here.)* *Existence of $W$ and smoothness.* $U \cap V$ is open and contains $p$, so $W = U \cap V$ will do; $f|_W + g|_W$ and $f|_W\, g|_W$ are smooth on $W$, so they define germs.
>
> *Independence of representatives.* Suppose $(f,U) \sim (f', U')$ and $(g,V) \sim (g',V')$, say $f = f'$ on $W_1 \ni p$ and $g = g'$ on $W_2 \ni p$. On the open set $W_1 \cap W_2 \ni p$ the four functions satisfy $f + g = f' + g'$ and $fg = f'g'$ pointwise, so the resulting germs agree. Independence of the auxiliary $W$ is the same argument with $f = f'$, $g = g'$.
>
> *Algebra axioms.* Each is an identity between germs that holds for representatives on a common domain, hence holds after passing to classes.
>
> *Evaluation.* If $(f,U) \sim (g,V)$ then $f = g$ near $p$, in particular $f(p) = g(p)$; and evaluation of functions is compatible with sums and products.

^pf-12-4

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-2|Def. §12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-3|Def. §12.3]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-3|§12.3]]

> [!definition] Definition §12.4: Evaluation of a Germ
> The **value** of a germ $[f] \in C_p^\infty(M)$ at $p$ is $[f](p) := f(p)$, independent of the representative by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]]. The map $C_p^\infty(M) \to \mathbb{R}$, $[f] \mapsto [f](p)$, is **evaluation** at $p$.

^def-12-4

> [!remark] Remark: How to Think About a Germ
> Uribe: “when I think of a germ, I think of a representative — a smooth function defined in a neighbourhood — but I know that it is a germ, which means I can shrink its domain arbitrarily, as long as I shrink it to a neighbourhood of $p$.” In practice one works with representatives and checks at the end that the answer is unchanged by shrinking. The formal content of the definition is exactly that shrinking is free.

^rem-12-3

![[m591-12-19.svg]]
*Two representatives of one germ, drawn as graphs over $M = \mathbb{R}$: $f$ (blue) on $U$ and $g$ (red, dashed) on $V$ agree on the shaded open set $W \ni p$ and part ways outside it. The germ $[f] = [g]$ keeps only the common piece near $p$; how large the domains are and what the functions do away from $p$ is forgotten — which is exactly why shrinking a representative's domain is free.*

> [!example] Example §12.2: Germs Versus Taylor Series
> Take $M = \mathbb{R}^n$ and $x_0 \in \mathbb{R}^n$. All partial derivatives of a function at $x_0$ depend only on its germ, so the Taylor series construction descends to a map into the ring of formal power series,
>
> $$
> \mathcal{T} : C_{x_0}^\infty(\mathbb{R}^n) \longrightarrow \mathbb{R}[\![x^1, \ldots, x^n]\!], \qquad
> \mathcal{T}[f] = \sum_{\alpha} \frac{1}{\alpha!}\, \frac{\partial^{|\alpha|} f}{\partial x^\alpha}(x_0)\, (x - x_0)^\alpha ,
> $$
>
> an $\mathbb{R}$-algebra homomorphism. It is *surjective* but *not injective*.

^ex-12-2

> [!proof]+ Justification
> Surjectivity is **Borel's theorem**: every formal power series is the Taylor series at $x_0$ of some smooth function. It is cited, not proved — Uribe: “that's not so easy to show, but it's true.” Failure of injectivity is elementary. Uribe: “You can have totally flat functions that are not zero”; the example is filled in. The function
>
> $$
> f(x) = \begin{cases} e^{-1/|x-x_0|^2}, & x \neq x_0,\\ 0, & x = x_0,\end{cases}
> $$
>
> is smooth with all partial derivatives vanishing at $x_0$ (a standard computation, not reproduced here), so $\mathcal{T}[f] = 0$ while $[f] \neq 0$.

^pf-ex-12-2

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-3|Def. §12.3]], [[§31 Taylor's Theorem#^ex-31-3|451 §31.3]]

> [!remark]- Connections
> - The one-variable flat function $e^{-1/x^2}$, a smooth function that is not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; Taylor series: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]].
> - Taylor expansion in several variables: [[Multivariable Taylor's Theorem|452 §9.2 (Multivariable Taylor's Theorem)]].

> [!definition] Definition §12.5: Flat Germ
> A germ $[f] \in C_{x_0}^\infty(\mathbb{R}^n)$ is **flat** if all partial derivatives of $f$, of all orders, vanish at $x_0$; equivalently, $\mathcal{T}[f] = 0$. So the kernel of $\mathcal{T}$ consists exactly of the flat germs.

^def-12-5

> [!remark] Remark
> The moral is that a germ carries strictly more information than its Taylor series — “one of the beauties of being in the $C^\infty$ category.” This is the same phenomenon as the rigidity of $C^\omega$ noted after Definition [[§8 Differentiable Structures#^def-8-5|§8.5]]: a real-analytic germ *is* its Taylor series, which is why there are no analytic bump functions, whereas a $C^\infty$ germ has room to spare.

^rem-12-4

## Derivations and the Abstract Tangent Space

> [!remark] Remark: Two Faces of a Tangent Vector
> Lecture 9 opened with a framing that the rest of the course keeps returning to. A tangent vector has two faces — “like Janus.” It is a *velocity*, the $\gamma'(0)$ of a curve — an element of the geometric tangent space $T^{\mathrm{geo}}_pM$, which is how [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#From Tangent Vectors to Derivations|§12, From Tangent Vectors to Derivations]] met it; and it is a *derivation*, an operator that eats germs and returns numbers — an element of the abstract tangent space $T_pM$, the formal definition below. Formally they are different objects, and the relation between them has to be proved (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]]). The same split will reappear for vector fields: as velocities attached to every point they *generate dynamics*, and as operators they lead to the *Lie derivative*.

^rem-12-5

> [!definition] Definition §12.6: Derivation at a Point
> Let $M$ be a smooth manifold and $p \in M$. A **derivation at $p$** is an $\mathbb{R}$-linear map
>
> $$
> D : C_p^\infty(M) \longrightarrow \mathbb{R}
> $$
>
> satisfying the **Leibniz rule**
>
> $$
> D\big([f][g]\big) \;=\; f(p)\, D[g] \;+\; g(p)\, D[f] \qquad \text{for all } [f], [g] \in C_p^\infty(M),
> $$
>
> where $f(p) = [f](p)$ is the evaluation of Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]].
>
> *Lee: Ch. 3, Tangent Vectors, on $C^\infty(M)$ rather than germs*

^def-12-6

> [!definition] Definition §12.7: The Abstract Tangent Space
> The **(abstract) tangent space** to $M$ at $p$ is
>
> $$
> T_pM \;=\; \{\, \text{all derivations at } p \,\},
> $$
>
> a real vector space under the pointwise operations $(D + D')[f] = D[f] + D'[f]$ and $(\lambda D)[f] = \lambda\, D[f]$. An element $D \in T_pM$ is a **tangent vector** at $p$. It is not an arrow in any ambient space but a function on germs, $D : C^\infty_p(M) \to \mathbb{R}$, so $D[f]$ is a real number for each germ $[f]$ at $p$.
>
> *Lee: Ch. 3, Tangent Vectors, via $C^\infty(M)$ (see Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-7|§12.7]])*

^def-12-7

> [!proof]+ Verification that $T_pM$ is a vector space
> $D + D'$ and $\lambda D$ are linear, being pointwise combinations of linear maps, and each satisfies the Leibniz rule because the rule is linear in $D$: for instance
>
> $$
> (D+D')([f][g]) = f(p)D[g] + g(p)D[f] + f(p)D'[g] + g(p)D'[f] = f(p)(D+D')[g] + g(p)(D+D')[f].
> $$
>
> The zero map is a derivation, and the vector space axioms hold pointwise.

^pf-def-12-7

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-6|Def. §12.6]], [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]

> [!remark]- Connections
> - The geometric tangent space it replaces: [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]]; the two agree by [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]].
> - Its dual, the cotangent space: [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|Def. §13.1]]; all the $T_pM$ together: [[§17 The Tangent Bundle#^def-17-1|the tangent bundle, Def. §17.1]].

> [!definition] Definition §12.8: The Ideal of Germs Vanishing at a Point
> The **ideal of germs vanishing at $p$** is
>
> $$
> I_p = \{\, [f] \in C_p^\infty(M) \mid f(p) = 0 \,\},
> $$
>
> the kernel of evaluation at $p$ (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-4|§12.4]]). Its **square** $I_p^2$ is the set of all finite sums $\sum_k [u_k][w_k]$ of products of two elements of $I_p$, the empty sum $0$ included.
>
> *Lee: Problem 11-4, where $I_p \subseteq C^\infty(M)$ consists of global functions*

^def-12-8

> [!theorem] Lemma §12.5: $I_p$ and $I_p^2$
> $I_p$ is an ideal of $C_p^\infty(M)$ and $I_p^2 \subseteq I_p$; both are linear subspaces.

^lem-12-5

> [!proof]+ Proof
> $I_p$ is the kernel of the algebra homomorphism of evaluation (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]]), hence a linear subspace and an ideal: $[g][f] \in I_p$ whenever $[f] \in I_p$, since $g(p)f(p) = 0$. $I_p^2$ is closed under sums by construction and under scalars since $c\,[u][w] = [cu][w]$ with $[cu] \in I_p$; and each product $[u][w]$ lies in $I_p$, since $u(p)w(p) = 0$.

^pf-12-5

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-8|Def. §12.8]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]]

> [!theorem] Lemma §12.6: First Properties of Derivations
> Let $D$ be a derivation at $p$, and $I_p$, $I_p^2$ as in Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-8|§12.8]].
> 1. $D$ annihilates constants: if $c \in \mathbb{R}$ and $\underline{c}$ denotes the germ of the constant function $c$, then $D[\underline{c}] = 0$. Consequently $D[f] = D\big[f - \underline{f(p)}\big]$, so $D$ is determined by its values on $I_p$.
> 2. $D$ annihilates products of vanishing germs: if $[f], [g] \in I_p$, then $D([f][g]) = 0$. Consequently $D$ vanishes on all of $I_p^2$.
>
> *Lee: Lemmas 3.1 and 3.4*

^lem-12-6

> [!proof]+ Proof
> (1) The germ of the constant $1$ satisfies $[\underline 1] = [\underline 1][\underline 1]$, so by the Leibniz rule
>
> $$
> D[\underline 1] = D\big([\underline 1][\underline 1]\big) = 1 \cdot D[\underline 1] + 1 \cdot D[\underline 1] = 2\, D[\underline 1],
> $$
>
> whence $D[\underline 1] = 0$. For general $c$, linearity gives $D[\underline c] = c\, D[\underline 1] = 0$.
>
> (2) Immediate from the Leibniz rule: $D([f][g]) = f(p)D[g] + g(p)D[f] = 0 + 0 = 0$. A general element of $I_p^2$ is a finite sum of such products, and $D$ is linear.

^pf-12-6

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-6|Def. §12.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-8|Def. §12.8]]

Both parts were set as an exercise in Lecture 9, where Uribe noted that (2) is “a very simple consequence of the product rule” and is part of a problem on Assignment 3, which introduces the ideal $I_p$ under that name. In commutative algebra the same ideal is written $\mathfrak{m}_p$, the notation used in the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-10|remark]] at the end of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#Coordinate Derivations and the Basis Theorem|§12, Coordinate Derivations and the Basis Theorem]].

> [!remark] Remark
> Uribe listed exactly these two as what must be shown before the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|basis theorem]], and deferred them to the following lecture. They are the entire reason the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-18|Taylor–Hadamard]] expansion collapses: the constant term dies by (1), the quadratic remainder dies by (2), and only the linear term survives.

^rem-12-6

> [!theorem] Proposition §12.7: Germ Derivations and Global Derivations
> Lee defines $T_pM$ as the space of derivations of $C^\infty(M)$ at $p$: linear maps $v : C^\infty(M) \to \mathbb{R}$ with $v(fg) = f(p)\,vg + g(p)\,vf$. For $D \in T_pM$ in the sense of Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-7|§12.7]], the formula $v_D(f) = D[f]$ defines such a derivation, and $D \mapsto v_D$ is a linear isomorphism between the two spaces.
>
> *Lee: Ch. 3, with Propositions 2.25 and 3.8*

^prop-12-7

> [!proof]+ Proof, granting smooth bump functions
> Taking germs is an algebra homomorphism $C^\infty(M) \to C_p^\infty(M)$ compatible with evaluation at $p$, so $v_D$ is a derivation, and $D \mapsto v_D$ is linear. Both remaining steps use a *bump function*: for an open $U \ni p$, a smooth $\psi : M \to [0,1]$ supported in $U$ with $\psi \equiv 1$ near $p$ (Lee, Proposition 2.25; these notes do not construct one). *Injective:* every germ $[f]$, with $f$ defined on $U$, has the global representative $\psi f$, extended by zero; so if $v_D = 0$ then $D[f] = v_D(\psi f) = 0$ for every germ. *Surjective:* given Lee's $v$, set $D[f] = v(\tilde f)$ for any global $\tilde f$ representing $[f]$. This is well defined because $v$ is local — if $\tilde f = \tilde g$ near $p$ then $v\tilde f = v\tilde g$ (Lee, Proposition 3.8, whose proof uses a bump function) — it is a derivation on germs, and $v_D = v$.

^pf-12-7

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-6|Def. §12.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-7|Def. §12.7]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]]

**Comparison with Lee.** This is where the course's algebraic route and Lee's part company. Lee works with global functions and pays for locality with bump functions: Proposition 3.8 shows a derivation of $C^\infty(M)$ only sees a function near $p$, and Proposition 3.9 identifies $T_pU$ with $T_pM$. Germs build locality into the definition, so the course needs no bump functions at all — Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]] is pure algebra. The proposition above is the bridge. Since the two spaces are isomorphic, every result about $T_pM$ in these notes transfers to Lee's, and conversely.

> [!theorem] Theorem §12.8: Ambient and Abstract Agree
> Let $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ be a regular level set and $p \in M$. Then
>
> $$
> T^{\mathrm{geo}}_pM \longrightarrow T_pM, \qquad v \longmapsto D_v,
> $$
>
> from the geometric tangent space (a subspace of $\mathbb{R}^{n+k}$) to the abstract tangent space (derivations at $p$) is an isomorphism of vector spaces.
>
> *Lee: Propositions 3.2, 5.37 and 5.38*

^thm-12-8

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|Def. §12.1]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|§12.1]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|§12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]]

> [!remark]- Connections
> - Stated here, proved in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-20|Consequences, §12.20]] once the basis theorem gives $\dim T_pM = n$.
> - The same identification read through velocities of curves: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-16|The Two Faces Reconciled]].

**Announced in lecture; proved below.** Stated in lecture in answer to a student's question — “are the ambient and the abstract tangent spaces the same, just defined differently?” — with the answer that they are, but that it has to be proved. Injectivity is Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|§12.2]]; that $D_v$ really is a derivation is Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|§12.1]]; surjectivity will follow from the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|basis theorem]] below, both spaces having dimension $n$. Even once it is proved, the notes keep the notations apart: $T^{\mathrm{geo}}_pM$ is the geometric tangent space, $T_pM$ the abstract one.

## Pushing Derivations Forward

*Lecture 9. Derivations can be pushed forward along smooth maps. In lecture this appeared in the middle of the proof of the basis theorem, as a “new derivation” $\tilde D$ on $\mathbb{R}^n$ built from one on $M$, and was defined properly only afterwards — “the order of my presentation is not ideal.” Here it comes first, so the proof can cite it.*

Throughout, $F : M \to N$ is a smooth map of smooth manifolds and $p \in M$. The construction has two steps: functions are pulled back, and derivations, being linear functionals on functions, are pushed forward by duality.

> [!definition] Definition §12.9: Pullback of Germs
> Let $F : M \to N$ be a smooth map between smooth manifolds, and $p \in M$, so that $F(p)$ is a point of $N$. Let $[g] \in C^\infty_{F(p)}(N)$ be a germ *at the point $F(p)$ of $N$*, with a representative $(g, V)$: $V \subseteq N$ is open with $F(p) \in V$, and $g : V \to \mathbb{R}$ is smooth. Then $F^{-1}(V)$ is an open neighbourhood of $p$ in $M$, and $g \circ F : F^{-1}(V) \to \mathbb{R}$ is smooth (Lemma [[§8 Differentiable Structures#^lem-8-15|§8.15]]), so $(g \circ F, F^{-1}(V))$ represents a germ at $p$ on $M$. The **pullback** of germs along $F$ at $p$ is the map
>
> $$
> F_p^* : C^\infty_{F(p)}(N) \longrightarrow C^\infty_p(M), \qquad F_p^*[g] = [\,g \circ F\,],
> $$
>
> which takes a germ on $N$ at $F(p)$ to a germ on $M$ at $p$. It does not depend on the representative $(g, V)$ (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-9|§12.9]]).
>
> *Lee: no counterpart; the course's germ-based route*

^def-12-9

> [!theorem] Proposition §12.9: Properties of the Pullback
> Let $F : M \to N$ be smooth and $p \in M$. The map $F_p^* : C^\infty_{F(p)}(N) \to C^\infty_p(M)$ is well defined, it is a homomorphism of $\mathbb{R}$-algebras, and it is compatible with evaluation: for every germ $[g] \in C^\infty_{F(p)}(N)$,
>
> $$
> \big(F_p^*[g]\big)(p) = g\big(F(p)\big).
> $$
>
> In particular $F_p^*$ maps the germs on $N$ vanishing at $F(p)$ to germs on $M$ vanishing at $p$: $F_p^*\big(I_{F(p)}\big) \subseteq I_p$.

^prop-12-9

> [!proof]+ Proof
> *Well defined.* For a representative $(g, V)$, the set $F^{-1}(V)$ is open and contains $p$ because $F$ is continuous, and $g \circ F$ is smooth there by Lemma [[§8 Differentiable Structures#^lem-8-15|§8.15]]. If $(g, V)$ and $(g', V')$ represent the same germ at $F(p)$, then $g = g'$ on some open $W$ with $F(p) \in W \subseteq V \cap V'$; so $g \circ F = g' \circ F$ on the open set $F^{-1}(W) \ni p$, and the two pulled-back germs at $p$ are equal.
>
> *Algebra homomorphism.* Composition with $F$ respects the pointwise operations: $(g + h)\circ F = g \circ F + h \circ F$, $(gh) \circ F = (g\circ F)(h \circ F)$, $(\lambda g)\circ F = \lambda (g \circ F)$, and $1 \circ F = 1$.
>
> *Evaluation.* $(g \circ F)(p) = g(F(p))$ by definition of composition.

^pf-12-9

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-9|Def. §12.9]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-2|Def. §12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-4|§12.4]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-8|Def. §12.8]], [[§8 Differentiable Structures#^lem-8-15|§8.15]]

> [!definition] Definition §12.10: Pushforward — the Differential
> Let $F : M \to N$ be smooth and $p \in M$, and let $D \in T_pM$ be a tangent vector at $p$ — that is, a derivation at $p$, a linear map $D : C^\infty_p(M) \to \mathbb{R}$ satisfying the Leibniz rule. The **pushforward** of $D$ along $F$ is the map
>
> $$
> F_{*p}D : C^\infty_{F(p)}(N) \longrightarrow \mathbb{R}, \qquad \big(F_{*p}D\big)[g] \;:=\; D\big(F_p^*[g]\big) = D[\,g \circ F\,],
> $$
>
> defined on germs $[g]$ at $F(p)$ on $N$: pull the germ back to $p$, then apply $D$. In one line, $F_{*p}D = D \circ F_p^*$. It is a derivation at $F(p)$, i.e. an element of $T_{F(p)}N$ (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]]). Letting $D$ vary gives the **pushforward**, or **differential**, of $F$ at $p$,
>
> $$
> F_{*p} : T_pM \longrightarrow T_{F(p)}N, \qquad D \longmapsto F_{*p}D,
> $$
>
> a map from tangent vectors at $p$ in $M$ to tangent vectors at $F(p)$ in $N$, also written $dF_p$. (Uribe: “the awkward notation $F_{*p}$.”) So $F_{*p}$ acts on derivations; its value $F_{*p}D$ is again a derivation, which acts on germs at $F(p)$.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^def-12-10

![[m591-12-3.svg]]

![[m591-12-4.svg]]
*Above, the definition as a diagram: $F_{*p}D = D \circ F_p^*$, a derivation at $F(p)$ obtained by first pulling the germ back to $p$ and then applying $D$. Below, the directions. Points move forward along $F$; functions move backward, since a function on $N$ composed with $F$ is a function on $M$; and derivations, being dual to functions, reverse the arrow once more and move forward again.*

> [!remark]- Connections
> - Pushforward as the transpose of pullback: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]]; 591's version, [[§10 Vector Spaces and Matrix Groups#^def-10-2|Def. §10.2]].
> - On open subsets of Euclidean space it is the Jacobian: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]; the calculus differential, [[§8 The Differential#^def-8-1|452 Def. §8.1]].

> [!theorem] Proposition §12.10: The Differential Is a Linear Map of Abstract Tangent Spaces
> For every $D \in T_pM$, $F_{*p}D$ is a derivation at $F(p)$; and $F_{*p} : T_pM \to T_{F(p)}N$ is linear.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^prop-12-10

> [!proof]+ Proof
> $F_{*p}D = D \circ F_p^*$ is linear, as a composite of linear maps. For the Leibniz rule, let $[g],[h] \in C^\infty_{F(p)}(N)$. Then
>
> $$
> \begin{aligned}
> \big(F_{*p}D\big)\big([g][h]\big)
> &= D\big(F_p^*[g]\cdot F_p^*[h]\big) \\
> &= \big(F_p^*[g]\big)(p)\, D\big(F_p^*[h]\big) + \big(F_p^*[h]\big)(p)\, D\big(F_p^*[g]\big) \\
> &= g(F(p))\,\big(F_{*p}D\big)[h] + h(F(p))\,\big(F_{*p}D\big)[g],
> \end{aligned}
> $$
>
> using, in turn, that $F_p^*$ is multiplicative, the Leibniz rule for $D$ at $p$, and compatibility with evaluation. So $F_{*p}D$ is a derivation at $F(p)$. Linearity in $D$ holds because $(D + \lambda D')\circ F_p^* = D \circ F_p^* + \lambda\, D' \circ F_p^*$.

^pf-12-10

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-6|Def. §12.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-9|§12.9]]

Every object of this subsection, with what it is and where it lives. The rows go in order of the diagram above: germs travel backwards, from $N$ to $M$, and derivations forwards, from $M$ to $N$.

| **Object** | **What it is** | **Lives in** |
|---|---|---|
| $F$ | a smooth map | $M \to N$ |
| $p$, $F(p)$ | a point of $M$, and its image, a point of $N$ | $M$, $N$ |
| $[f]$ | a germ at $p$: a class of smooth functions defined near $p$ in $M$ | $C^\infty_p(M)$ |
| $[g]$ | a germ at $F(p)$: a class of smooth functions defined near $F(p)$ in $N$ | $C^\infty_{F(p)}(N)$ |
| $F_p^*$ | pullback, an algebra homomorphism, $[g] \mapsto [g \circ F]$ | $C^\infty_{F(p)}(N) \to C^\infty_p(M)$ |
| $D$ | a tangent vector at $p$: a derivation, a linear map $C^\infty_p(M) \to \mathbb{R}$ | $T_pM$ |
| $F_{*p}$ | pushforward, a linear map, $D \mapsto D \circ F_p^*$ | $T_pM \to T_{F(p)}N$ |
| $F_{*p}D$ | a tangent vector at $F(p)$: a derivation, a linear map $C^\infty_{F(p)}(N) \to \mathbb{R}$ | $T_{F(p)}N$ |
| $(F_{*p}D)[g]$ | a real number, equal to $D[g \circ F]$ | $\mathbb{R}$ |

The board justified the derivation property with “since $F_p^*$ is a ring morphism.” That is one of the two facts used, and not quite enough on its own: the Leibniz rule *at $F(p)$* needs the coefficients $g(F(p))$ and $h(F(p))$, and these appear only because pullback is compatible with evaluation, $(g \circ F)(p) = g(F(p))$ — the third equality above. It is automatic here, but it is a separate property from multiplicativity, and it is the one that moves the base point from $p$ to $F(p)$.

> [!theorem] Theorem §12.11: The Chain Rule
> If $F : M \to N$ and $G : N \to P$ are smooth and $p \in M$, then
>
> $$
> (G \circ F)_{*p} = G_{*F(p)} \circ F_{*p} : T_pM \to T_{G(F(p))}P, \qquad (\mathrm{id}_M)_{*p} = \mathrm{id}_{T_pM} .
> $$
>
> *Lee: Proposition 3.6(b)*

^thm-12-11

> [!proof]+ Proof
> *(Lecture 10: “the proof of the chain rule is one line” — pullbacks compose in the opposite order, because composition is associative. The dualization that follows was set as an exercise, “use this to conclude the proof”; it is filled in.)* Pullback reverses composition: $(G\circ F)_p^* = F_p^* \circ G_{F(p)}^*$, since $g \circ (G \circ F) = (g \circ G) \circ F$. Hence for $D \in T_pM$ and a germ $[g]$ at $G(F(p))$,
>
> $$
> \big((G\circ F)_{*p}D\big)[g] = D\big(F_p^*\, G_{F(p)}^*[g]\big) = \big(F_{*p}D\big)\big(G_{F(p)}^*[g]\big) = \big(G_{*F(p)}\,F_{*p}D\big)[g].
> $$
>
> The identity pulls back every germ to itself, so it pushes every derivation to itself.

^pf-12-11

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-9|Def. §12.9]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]]

![[m591-12-5.svg]]
*The upper row is the composite of maps; the lower row says its differential is the composite of the differentials. In coordinates (Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|§12.23]]) it becomes the multiplication of Jacobian matrices — the chain rule of calculus, now as a statement about manifolds.*

> [!remark]- Connections
> - The chain rule of calculus: [[Multivariable Chain Rule|452 §10.2 (Multivariable Chain Rule)]].
> - Duals compose in the opposite order, $(ST)' = T'S'$: [[§12 Duality#^ladr-3-120|LADR 3.120]]; 591's version, [[§10 Vector Spaces and Matrix Groups#^prop-10-4|§10.4]].

**Lecture 10.** Uribe stated this as the Chain Rule and proved the pullback identity $(G \circ F)_p^* = F_p^* \circ G_{F(p)}^*$ on the board — “see, you know that this is the right point of view when proofs become one line” — leaving the dualization as an exercise; the displayed computation above is that exercise. Pullbacks compose in the *opposite* order, so pushforwards, being their duals, compose in the *same* order as the maps. (The theorem appeared here, ahead of the lecture, because the two results below depend on it.)

> [!theorem] Corollary §12.12: Diffeomorphisms Induce Isomorphisms
> If $\Phi : M \to N$ is a diffeomorphism, then $\Phi_{*p} : T_pM \to T_{\Phi(p)}N$ is a linear isomorphism, with inverse $(\Phi^{-1})_{*\Phi(p)}$.
>
> *Lee: Proposition 3.6(d)*

^cor-12-12

> [!proof]+ Proof
> Apply Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]] to $\Phi^{-1} \circ \Phi = \mathrm{id}_M$ and $\Phi \circ \Phi^{-1} = \mathrm{id}_N$.

^pf-12-12

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]

> [!theorem] Lemma §12.13: Open Subsets Have the Same Abstract Tangent Spaces
> Let $U \subseteq M$ be open with $p \in U$, and $\iota : U \hookrightarrow M$ the inclusion. Then $\iota_p^* : C^\infty_p(M) \to C^\infty_p(U)$ is restriction of germs, an isomorphism of $\mathbb{R}$-algebras, and consequently $\iota_{*p} : T_pU \to T_pM$ is a linear isomorphism. We use it to identify $T_pU = T_pM$.
>
> *Lee: Proposition 3.9*

^lem-12-13

> [!proof]+ Proof
> Restriction is well defined and an algebra homomorphism by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-9|§12.9]]. It is surjective because a germ at $p$ on $U$ has a representative defined on an open subset of $U$, which is open in $M$ and so already represents a germ on $M$; and injective because if $f|_U$ and $g|_U$ agree near $p$ then $f$ and $g$ agree near $p$. A derivation on one algebra corresponds to exactly one on the other by composing with this isomorphism, so $\iota_{*p}$ is a bijection; it is linear by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]].

^pf-12-13

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-9|§12.9]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-3|Def. §12.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-2|§3.2]]

> [!theorem] Proposition §12.14: Charts Are Diffeomorphisms
> If $(U, \varphi)$ is a smooth chart of $M$, then $\varphi : U \to \varphi(U)$ is a diffeomorphism. Consequently, for every $p \in U$,
>
> $$
> T_pM \;=\; T_pU \xrightarrow[\ \cong\ ]{\ \varphi_{*p}\ } T_{\varphi(p)}\,\varphi(U)
> $$
>
> is a linear isomorphism of abstract tangent spaces.

^prop-12-14

> [!proof]+ Proof
> In the charts $(U,\varphi)$ on $U$ and $(\varphi(U), \mathrm{id})$ on $\varphi(U)$, both $\varphi$ and $\varphi^{-1}$ have coordinate representation the identity, so both are smooth (Definition [[§8 Differentiable Structures#^def-8-14|§8.14]]). The isomorphism is then Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]] followed by Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12|§12.12]].

^pf-12-14

*Uses:* [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12|§12.12]]

> [!remark] Remark: The Chart Pushforward
> This is the $\tilde D$ of the lecture: for $D \in T_pM$, $\tilde D = \varphi_{*p}D$ acts by $\tilde D[g] = D[g \circ \varphi]$, identifying tangent vectors on $M$ with derivations at a point of an open subset of $\mathbb{R}^n$. Everything about the abstract tangent space $T_pM$ can therefore be settled in $\mathbb{R}^n$, which is how the basis theorem is proved.

^rem-12-7

## Coordinate Derivations and the Basis Theorem

> [!definition] Definition §12.11: Coordinate Functions of a Chart
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
> 3. For a function $f$ defined on $U$, its **coordinate representation** in the chart is $f_\varphi = f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$, as in Definition [[§8 Differentiable Structures#^def-8-13|§8.13]]; thus $f = f_\varphi \circ \varphi$ on $U$. In particular $(x^i)_\varphi = r^i \circ \varphi \circ \varphi^{-1} = r^i$ on $\varphi(U)$.
>
> *Lee: Ch. 1, Coordinate Charts*

^def-12-11

> [!remark] Remark
> **A notational discipline.** Uribe stopped to insist on this. The $x^i$ live *upstairs*, as functions on the manifold, and the $r^i$ *downstairs*, as functions on $\mathbb{R}^n$; conflating them is the main source of confusion in what follows. The identity $(x^i)_\varphi = r^i$ is the bridge between the two rows: it says that the coordinate functions, written in their own chart, are the standard coordinates. It also shows that each $x^i$ is a smooth function on $U$, by Definition [[§8 Differentiable Structures#^def-8-13|§8.13]], since $r^i$ is smooth.

^rem-12-8

![[m591-12-6.svg]]
*The board diagram for this subsection. Both triangles commute: the left one says $f = f_\varphi \circ \varphi$, which is what smoothness of $f$ means; the right one is the* definition *$x^i = r^i \circ \varphi$ of the $i$-th coordinate function on $U$ (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|§12.11]]). Everything upstairs is expressed downstairs by composing with $\varphi$, and the derivation about to be defined does its differentiating entirely on the bottom row, where partial derivatives already make sense.*

> [!definition] Definition §12.12: Coordinate Derivations
> Let $(U,\varphi)$ be a smooth chart with $p \in U$, with coordinate functions $x^1, \ldots, x^n$ (Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|§12.11]]), and let $i \in \{1,\ldots,n\}$. Define $\dfrac{\partial}{\partial x^i}\Big|_p : C_p^\infty(M) \to \mathbb{R}$ by
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

^def-12-12

> [!theorem] Proposition §12.15: Coordinate Derivations Are Derivations
> $\dfrac{\partial}{\partial x^i}\Big|_p$ is well defined on germs and is a derivation at $p$.

^prop-12-15

> [!proof]+ Proof
> *(Lecture 8: “it's linear, and the product rule will be inherited from the product rule of the ordinary partial derivatives” — the* Linear *and* Leibniz *steps below. Well-definedness is filled in.)* *Well defined.* If $(f,U_1) \sim (g,U_2)$, then $f = g$ on an open $W \ni p$, so $f_\varphi = g_\varphi$ on the open set $\varphi(W \cap U) \ni \varphi(p)$; partial derivatives at a point depend only on the function near that point, so the two values agree. (Shrinking the chart domain also changes nothing, for the same reason.)
>
> *Linear.* $(\lambda f + g)_\varphi = \lambda f_\varphi + g_\varphi$, and partial differentiation is linear.
>
> *Leibniz.* $(fg)_\varphi = f_\varphi\, g_\varphi$, so by the ordinary product rule at $\varphi(p)$,
>
> $$
> \frac{\partial (fg)_\varphi}{\partial r^i}(\varphi(p)) = f_\varphi(\varphi(p))\,\frac{\partial g_\varphi}{\partial r^i}(\varphi(p)) + g_\varphi(\varphi(p))\,\frac{\partial f_\varphi}{\partial r^i}(\varphi(p)),
> $$
>
> and $f_\varphi(\varphi(p)) = f(p)$, $g_\varphi(\varphi(p)) = g(p)$.

^pf-12-15

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|Def. §12.12]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-2|Def. §12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-6|Def. §12.6]], [[§6 Differentiability#^thm-6-4|452 §6.4]]

> [!theorem] Theorem §12.16: Basis Theorem
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

^thm-12-16

The proof needs a form of Taylor expansion whose remainder is not an estimate but an exact, *smooth* term — “a theorem from calculus” that is not usually taught there. It is built in two steps: first order, then the first-order statement applied again.

> [!theorem] Lemma §12.17: Hadamard's Lemma
> Let $W \subseteq \mathbb{R}^n$ be open, $a = (a^1,\ldots,a^n) \in W$, $f : W \to \mathbb{R}$ smooth, and $B \subseteq W$ an open ball centred at $a$. Then there are smooth functions $f_1, \ldots, f_n$ on $B$ with
>
> $$
> f(r) = f(a) + \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f}{\partial r^i}(a) .
> $$
>
> Explicitly, $f_i(r) = \displaystyle\int_0^1 \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt$.
>
> *Lee: cf. Theorem C.15, used in the proof of Proposition 3.2*

^lem-12-17

> [!proof]+ Proof
> *(Lecture 9: “the proof is delightfully simple.”)* Fix $r \in B$. The segment $t \mapsto a + t(r - a)$, $t \in [0,1]$, runs from $a$ to $r$ and stays in $B$, a ball being convex. By the fundamental theorem of calculus and the chain rule,
>
> $$
> f(r) - f(a) = \int_0^1 \frac{d}{dt} f\big(a + t(r-a)\big)\, dt = \int_0^1 \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt = \sum_{i=1}^n (r^i - a^i)\, f_i(r),
> $$
>
> the factors $r^i - a^i$ coming out of the integral because they do not depend on $t$. Each $f_i$ is smooth on $B$: the integrand is smooth in $(t, r)$ on $[0,1] \times B$, so differentiation under the integral sign is legitimate to every order. At $r = a$ the integrand is constant, and $f_i(a) = \partial f/\partial r^i(a)$.

^pf-12-17

*Uses:* [[Fundamental Theorem of Calculus|451 §34.1]], [[Multivariable Chain Rule|452 §10.2]]

**Transcription note.** In Lecture 9 the path in the integral was first written with the wrong endpoints; a student corrected it to the convex combination $t(r - a) + a$, which runs from $a$ at $t = 0$ to $r$ at $t = 1$, as above.

Uribe called the proof “delightfully simple.” A student corrected the path on the board: it must be the segment $a + t(r - a)$, equal to $a$ at $t = 0$ and to $r$ at $t = 1$. Convexity of $B$ is what the proof uses — “everything is local,” but the neighbourhood must contain the segment from $a$ to each of its points, which is why a ball (or any set star-shaped about $a$) is taken.

> [!theorem] Lemma §12.18: Taylor–Hadamard
> In the setting of Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17|§12.17]], there are smooth functions $f_{ij}$ on $B$, $1 \le i, j \le n$, with
>
> $$
> f(r) \;=\; f(a) \;+\; \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}(a) \;+\; \sum_{i,j=1}^n (r^i - a^i)(r^j - a^j)\, f_{ij}(r) \qquad (r \in B),
> $$
>
> and $f_{ij}(a) = \tfrac12\, \dfrac{\partial^2 f}{\partial r^i\,\partial r^j}(a)$. This is an identity, not an approximation.
>
> *Lee: cf. Theorem C.15*

^lem-12-18

> [!proof]+ Proof
> *(Lecture 9, exactly: first order, then “apply the claim to each $f_i$” and substitute back. Uribe wrote the quadratic term with a factor $\tfrac12$ — “doesn't matter” — which the notes absorb into $f_{ij}$; the value of $f_{ij}(a)$ at the end is a completion, the lecture needing only that the $f_{ij}$ are smooth.)* Apply Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17|§12.17]] to $f$, obtaining $f_1, \ldots, f_n$; then apply it again to each $f_i$, obtaining smooth $f_{ij}$ with
>
> $$
> f_i(r) = f_i(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r) = \frac{\partial f}{\partial r^i}(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r).
> $$
>
> Substituting this into $f(r) = f(a) + \sum_i (r^i - a^i) f_i(r)$ gives the identity. For the value at $a$: by Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17|§12.17]] applied to $f_i$, $f_{ij}(a) = \partial f_i/\partial r^j(a)$, and differentiating the integral formula for $f_i$ under the integral sign,
>
> $$
> \frac{\partial f_i}{\partial r^j}(r) = \int_0^1 t\, \frac{\partial^2 f}{\partial r^j\,\partial r^i}\big(a + t(r-a)\big)\, dt, \qquad\text{so}\qquad \frac{\partial f_i}{\partial r^j}(a) = \frac12\, \frac{\partial^2 f}{\partial r^i\,\partial r^j}(a).
> $$

^pf-12-18

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17|§12.17]]

> [!remark]- Connections
> - Taylor's theorem with an estimated remainder: [[Multivariable Taylor's Theorem|452 §9.2 (Multivariable Taylor's Theorem)]]; in one variable, [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]].

**On the factor $\tfrac12$.** The board states the lemma with $\tfrac12 \sum_{i,j}$ in front of the quadratic term; Uribe added it “just for consistency,” saying it “doesn't matter.” For the *existence* statement that is right — replacing $f_{ij}$ by $2f_{ij}$ converts one form into the other. But the two forms are not interchangeable as written: the iterated proof above produces the version *without* the $\tfrac12$, and with $f_{ij}(a) = \tfrac12 \partial_{ij} f(a)$. The board's normalization is the one in which $f_{ij}(a) = \partial_{ij} f(a)$, matching the Hessian term $\tfrac12 \sum \partial_{ij}f(a)(r^i - a^i)(r^j - a^j)$ of the ordinary Taylor polynomial. A numerical check on a test function confirms the unscaled identity to machine precision and shows the scaled one, with the same $f_{ij}$, to be off. Nothing below depends on the normalization, since only the vanishing of the quadratic term under a derivation is used.

> [!remark] Remark
> **What matters.** “The point is that these functions don't blow up at $a$”: the remainder is a product of two factors vanishing at $a$ with a *smooth* function, not merely a quantity that is small compared with $|r - a|^2$. The same iteration continues to any order.

^rem-12-9

![[m591-12-7.svg]]
*Taylor–Hadamard for $f(r) = e^r$ at $a = 0$, in one variable. Left: the remainder $f(r) - f(a) - f'(a)(r-a)$ is the gap between the graph and its tangent line. Right: the same gap divided by $(r - a)^2$. The quotient $f_{11}(r) = (e^r - 1 - r)/r^2$ has only a removable singularity at $a$: it is smooth there, with value $\tfrac12 = \tfrac12 f''(0)$, exactly as the lemma predicts, and as the iterated proof computes it — $f_1(r) = (e^r - 1)/r$, then $f_{11}(r) = (f_1(r) - f_1(0))/r$. That the quotient extends smoothly across $a$ is the whole content of the lemma.*

> [!theorem] Corollary §12.19: Derivations on $\mathbb{R}^n$
> Let $W \subseteq \mathbb{R}^n$ be open, $a \in W$, and $D$ a derivation at $a$ on $W$. Then for every germ $[f]$ at $a$,
>
> $$
> D[f] = \sum_{i=1}^n \frac{\partial f}{\partial r^i}(a)\, D[r^i], \qquad\text{that is,}\qquad D = \sum_{i=1}^n D[r^i]\, \frac{\partial}{\partial r^i}\Big|_a .
> $$
>
> *Lee: Proposition 3.2 and Corollary 3.3*

^cor-12-19

> [!proof]+ Proof
> Choose a representative $f$ on an open ball $B \subseteq W$ centred at $a$, which changes nothing since $D$ acts on germs, and apply $D$ to the identity of Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-18|§12.18]]:
>
> $$
> D[f] = D\big[\underline{f(a)}\big] + \sum_{i} \frac{\partial f}{\partial r^i}(a)\, D\big[r^i - a^i\big] + \sum_{i,j} D\Big[(r^i - a^i)\cdot\big((r^j - a^j) f_{ij}\big)\Big].
> $$
>
> The constant term vanishes by Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]](1). Each quadratic term is $D$ of a product of two germs in $I_a$ — namely $r^i - a^i$ and $(r^j - a^j)f_{ij}$, both zero at $a$ — so it vanishes by Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]](2). Finally $D[r^i - a^i] = D[r^i]$ by (1) again. So $D$ sees only the linear part of $f$: “the ultimate formula in the Euclidean case.”

^pf-12-19

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-18|§12.18]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-3|Def. §12.3]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|Def. §12.12]]

> [!proof]+ Proof of Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]]
> *(Lecture 9. In lecture the derivation $\tilde D$ was introduced inside this proof — “this is how you push forward derivations … we'll come back to this construction immediately after” — and Uribe remarked that “the order of my presentation is not ideal.” The notes define the pushforward first, in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#Pushing Derivations Forward|§12, Pushing Derivations Forward]], so that the proof can cite it.)* Let $D \in T_pM$ and put $a = \varphi(p) = (r_0^1, \ldots, r_0^n)$.
>
> *Step 1: push $D$ down.* Let $\tilde D = \varphi_{*p}D \in T_a\,\varphi(U)$, the chart pushforward of Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]]; so $\tilde D[g] = D[g \circ \varphi]$ for germs $g$ at $a$.
>
> *Step 2: apply the Euclidean formula downstairs.* By Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-19|§12.19]] on the open set $\varphi(U)$,
>
> $$
> \tilde D[g] = \sum_{i=1}^n \frac{\partial g}{\partial r^i}(a)\, \tilde D[r^i] .
> $$
>
> *Step 3: read it back upstairs.* Let $[f]$ be a germ at $p$, and take $g = f_\varphi = f \circ \varphi^{-1}$. Then $f_\varphi \circ \varphi = f$ near $p$, so $\tilde D[f_\varphi] = D[f]$; by Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|§12.12]], $\partial f_\varphi/\partial r^i(a) = \partial/\partial x^i|_p[f]$; and $\tilde D[r^i] = D[r^i \circ \varphi] = D[x^i]$. Substituting,
>
> $$
> D[f] = \sum_{i=1}^n D[x^i]\, \frac{\partial}{\partial x^i}\Big|_p[f] \qquad\text{for every germ } [f],
> $$
>
> so $D = \sum_i D[x^i]\, \partial/\partial x^i|_p$ and the coordinate derivations span.
>
> *Step 4: independence.* If $\sum_i c_i\, \partial/\partial x^i|_p = 0$, apply it to $[x^j]$. Since $(x^j)_\varphi = r^j$, we get $\partial/\partial x^i|_p[x^j] = \partial r^j/\partial r^i = \delta^j_i$, hence $c_j = 0$. So the $n$ coordinate derivations form a basis, and the coefficients of $D$ are the numbers $D[x^i]$ — uniquely.

^pf-12-16

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-19|§12.19]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|Def. §12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|Def. §12.12]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-15|§12.15]]

![[m591-12-8.svg]]

$$
\varphi^*[r^i] = [x^i], \qquad \varphi^*[f_\varphi] = [f]
$$

*The proof in one diagram — the defining triangle of the pushforward, for the chart. Downstairs the Euclidean formula computes $\tilde D$ on everything; the two pullback identities displayed under the diagram carry the answer back upstairs, turning $\tilde D[r^i]$ into $D[x^i]$ and $\tilde D[f_\varphi]$ into $D[f]$.*

> [!remark]- Connections
> - The coefficients $D[x^i]$ are the values of the dual basis $dx^i|_p$: [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|§13.2]]; cf. [[§12 Duality#^ladr-3-114|LADR 3.114]].
> - The components in the coordinate basis give the charts of the tangent bundle: [[§17 The Tangent Bundle#^def-17-2|Def. §17.2]].

**Reconciliation with the lecture.** This is the lecture's proof, in the lecture's order of ideas but with the pushforward defined before it is used rather than after. Two details of the board version. It opens with “$\forall\, [f] \in I_p$”: restricting to germs vanishing at $p$ is harmless, since $D[f] = D[f - f(p)]$ by Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]](1), but the argument works verbatim for every germ. And the notes had filled in a proof of this theorem before Lecture 9, via two reduction lemmas; those were the pushforward by an inclusion and by the chart in disguise, and they now appear as Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]] and Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-12|§12.12]].

**Transcription note (Lecture 8).** Page 16 of the handwritten notes states Taylor–Hadamard for “$f : U \to \mathbb{R}^2$”; the target is $\mathbb{R}$.

> [!theorem] Corollary §12.20: Consequences
> Let $M$ be a smooth $n$-manifold and $p \in M$. Then the abstract tangent space has $\dim T_pM = n$, and for a regular level set $M = F^{-1}(c)$ the map $v \mapsto D_v$ of Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]], from $T^{\mathrm{geo}}_pM$ to $T_pM$, is an isomorphism.
>
> *Lee: Proposition 3.10*

^cor-12-20

> [!proof]+ Proof
> The first claim is Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]]. For the second, $v \mapsto D_v$ is linear and injective (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|§12.2]]) between spaces of dimension $n$ — the geometric tangent space $T^{\mathrm{geo}}_pM$ by Theorem [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], the abstract tangent space $T_pM$ by Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]] — hence an isomorphism.

^pf-12-20

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-2|§12.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|§12.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - This is the proof of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Ambient and Abstract Agree, §12.8]], announced before the basis theorem.

**Comparison with Lee.** Lee meets the two kinds of tangent vector in the opposite order. He defines $T_pM$ by derivations first, identifies geometric and abstract tangent vectors in $\mathbb{R}^n$ (Proposition 3.2), and only later, for embedded submanifolds, shows $T_pS = \ker d\Phi_p$ (Proposition 5.38). The course starts geometrically, with $T^{\mathrm{geo}}_pM = \ker F'(p)$ inside the ambient space (Theorem [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]]), and reaches derivations afterwards. The consequence above is where the two orders meet.

> [!remark] Remark: A Derivation Sees Only the First Derivatives
> The basis theorem showed that, of the whole Taylor expansion of a germ, a derivation sees only the *linear* term — “of the entire Taylor series of the germ, all I care about are the first partials.” [[§13 Tangent Spaces III꞉ The Cotangent Space#The Cotangent Space from Germs|§13, The Cotangent Space from Germs]] says this algebraically: $I_p$ is a maximal ideal, being the kernel of evaluation; $I_p^2$ consists exactly of the germs vanishing to *second* order (Proposition [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-4|§13.4]]); and $I_p/I_p^2$ is canonically the *cotangent space* $T_p^*M$ of Definition [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|§13.1]], built with no dualizing at all (Theorem [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|§13.7]]). This is the sense in which, as Uribe remarked when he first set out to define the abstract tangent space, “it is more natural to define the dual”: the cotangent space comes first, and the abstract tangent space is its dual. We follow Lee and do not take that route.

^rem-12-10

## The Differential in Coordinates

*Lecture 9. The differential $F_{*p}$ is defined without coordinates; choosing charts on both sides turns it into a matrix, and the matrix is the Jacobian of the coordinate representation. “This should be very much reminiscent of the things we said about vector spaces — another instance of the same thing.”*

Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$, and $p \in M$. Choose smooth charts $(U, \varphi)$ of $M$ with $p \in U$ and $(V, \psi)$ of $N$ with $F(U) \subseteq V$ — possible because $F$ is smooth (Definition [[§8 Differentiable Structures#^def-8-14|§8.14]]) — and write

$$
\varphi = (x^1, \ldots, x^m), \qquad \psi = (y^1, \ldots, y^n), \qquad \tilde F = \psi \circ F \circ \varphi^{-1}, \qquad F^j = y^j \circ F : U \to \mathbb{R}.
$$

By Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]] there are bases

$$
\mathcal{B}_M = \Big\{ \frac{\partial}{\partial x^i}\Big|_p \Big\}_{i=1}^m \ \text{ of } T_pM, \qquad \mathcal{B}_N = \Big\{ \frac{\partial}{\partial y^j}\Big|_{F(p)} \Big\}_{j=1}^n \ \text{ of } T_{F(p)}N .
$$

![[m591-12-9.svg]]

![[m591-12-10.svg]]
*Left, the maps: upstairs $F$ between manifolds, downstairs its coordinate representation $\tilde F$ between open sets of Euclidean space. Right, their linearizations: upstairs the differential, intrinsic; downstairs the Jacobian matrix, and the vertical isomorphisms send $\partial/\partial x^i|_p \mapsto e_i$ and $\partial/\partial y^j|_{F(p)} \mapsto e_j$. Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] below says the right-hand square commutes. It is the square of [[§10 Vector Spaces and Matrix Groups#The Differential of a Map Between Vector Spaces|§10, The Differential of a Map Between Vector Spaces]] again, with abstract tangent spaces in place of abstract vector spaces and coordinate bases in place of linear coordinates.*

> [!theorem] Proposition §12.21: Partial Derivatives Upstairs and Downstairs
> Let $F : M \to N$ be smooth, with smooth charts $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ and $(V, \psi = (y^1, \ldots, y^n))$ of $N$ such that $F(U) \subseteq V$. Let $F^j = y^j \circ F : U \to \mathbb{R}$ be the components of $F$, functions on the manifold, and $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ the coordinate representation, with components $\tilde F^j = r^j \circ \tilde F$, functions on Euclidean space. Then $F^j \circ \varphi^{-1} = \tilde F^j$, and therefore, for every $p \in U$,
>
> $$
> \underbrace{\frac{\partial F^j}{\partial x^i}(p)}_{\text{upstairs, on } M} \;=\; \underbrace{\frac{\partial \tilde F^j}{\partial r^i}\big(\varphi(p)\big)}_{\text{downstairs, in } \mathbb{R}^m} .
> $$

^prop-12-21

> [!proof]+ Proof
> $F^j \circ \varphi^{-1} = y^j \circ F \circ \varphi^{-1} = r^j \circ \psi \circ F \circ \varphi^{-1} = r^j \circ \tilde F = \tilde F^j$ on $\varphi(U)$, using $y^j = r^j \circ \psi$. So the coordinate representation of the function $F^j$ is $\tilde F^j$, and by Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|§12.12]], $\partial F^j/\partial x^i(p) = \partial (F^j \circ \varphi^{-1})/\partial r^i(\varphi(p)) = \partial \tilde F^j/\partial r^i(\varphi(p))$.

^pf-12-21

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|Def. §12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-12|Def. §12.12]]

> [!remark] Remark: Why This Identity Carries So Much
> Uribe stated it in Lecture 10 and recalled it at the decisive moment of Lecture 11 — it is marked with “!!!” on page 30 of the handwritten notes. When a student asked whether the matrix in the proof of the normal form should be written with $\tilde F$, the answer was: “it's the same thing … that's how we define partials.” Partial derivatives on a manifold are *defined* by going downstairs, so the matrix of partials of the components $F^j$ upstairs is literally the ordinary Jacobian of $\tilde F$ downstairs. This is what turns every local computation on a manifold into calculus in $\mathbb{R}^m$, and it is used in:
> 1. the matrix of the differential (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]]), which is a one-line proof because of it;
> 2. regular values in one chart (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|§12.27]]): the rank of $F_{*p}$ is the rank of $\tilde F'(\varphi(p))$;
> 3. the proof of the local normal form (Theorem [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|§14.5]]), where the matrix $\big[\partial F^j/\partial x^i(p)\big]$ is built from the components $F^j$ but is the Jacobian of $\tilde F$;
> 4. [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-15|Assignment 3, Problem 4]], whose “matching coefficients” step computes $F_{*p}(\partial/\partial u_k|_p)[x^j]$ as an ordinary partial derivative of $F_\varphi$.
>
> Both sides depend on the charts: changing $\varphi$ or $\psi$ changes the matrix (Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]]), while $F_{*p}$ itself does not.

^rem-12-11

> [!theorem] Theorem §12.22: The Matrix of the Differential
> $F_{*p}$ is linear, and
>
> $$
> F_{*p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{j=1}^n \frac{\partial F^j}{\partial x^i}(p)\, \frac{\partial}{\partial y^j}\Big|_{F(p)} .
> $$
>
> So the matrix of $F_{*p}$ in the bases $\mathcal{B}_M$, $\mathcal{B}_N$ has the upstairs partials $\partial F^j/\partial x^i(p)$ as entries, and by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|§12.21]] it is the $n \times m$ Jacobian of the coordinate representation,
>
> $$
> \Big[\, \frac{\partial F^j}{\partial x^i}(p) \,\Big]_{j, i} = \tilde F'\big(\varphi(p)\big),
> $$
>
> with $j$ the row index and $i$ the column index.
>
> *Lee: Ch. 3, Computations in Coordinates*

^thm-12-22

> [!proof]+ Proof
> *(Lecture 10 — “once you think about it a little bit, it's a one-line proof.”)* Linearity is Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]]. The $i$-th column of the matrix consists of the coefficients of $F_{*p}(\partial/\partial x^i|_p)$ in the basis $\mathcal{B}_N$, and the universal formula of Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], applied at $F(p)$ with the chart $\psi$, says the $j$-th coefficient of any derivation is its value on $[y^j]$. By the definition of the pushforward,
>
> $$
> F_{*p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big)\big[y^j\big] = \frac{\partial}{\partial x^i}\Big|_p\big[y^j \circ F\big] = \frac{\partial F^j}{\partial x^i}(p).
> $$
>
> That is the formula. For the identification with $\tilde F'(\varphi(p))$ — the “claim” of the lecture — this is Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|§12.21]]: the partials are *defined* through the chart, and $F^j \circ \varphi^{-1} = \tilde F^j$, so $\partial F^j/\partial x^i(p) = \partial \tilde F^j/\partial r^i(\varphi(p))$, the $(j,i)$ entry of $\tilde F'(\varphi(p))$. “It's all the same.”

^pf-12-22

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|§12.21]], [[§9 Matrices#^ladr-3-31|LADR 3.31]]

> [!remark]- Connections
> - The matrix of a linear map with respect to bases: [[§9 Matrices#^ladr-3-31|LADR 3.31]]; the Jacobian matrix of calculus: [[§6 Differentiability#^def-6-2|452 Def. §6.2]].
> - The same statement between vector spaces: [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]].

> [!remark] Remark
> **Which index is the row.** Uribe's mnemonic, “from the mid-nineteenth century”: *gradients go across*. Row $j$ of the matrix is the gradient of the single function $F^j$, so moving along a row changes $i$; the column $i$ is the image of the $i$-th basis vector, as it must be for the matrix of a linear map.

^rem-12-12

**Transcription notes.** Page 26 of the handwritten notes calls $\mathcal{B}_N$ a basis “of $T_{F(p)}M$”. Page 27 (Lecture 10) repeats the lemma with the basis written $\{\partial/\partial y^j|_p,\ 1 \le j \le m\}$ “of $T_{F(p)}M$” — three slips at once: the base point is $F(p)$, the index runs to $n = \dim N$, and the space is $T_{F(p)}N$. In the same proof the universal formula is written with $\partial/\partial y^j|_p$ for $\partial/\partial y^j|_{F(p)}$. A student asked whether the index on $F^j$ belongs upstairs or downstairs; upstairs, as for coordinates, with $j$ the row index. Uribe also announced that the partials will from now on be written in calculus notation, $\partial F^j/\partial x^i(p)$ rather than $\partial/\partial x^i|_p[F^j]$.

> [!theorem] Corollary §12.23: The Chain Rule in Coordinates
> Let $F : M \to N$ and $G : N \to O$ be smooth, with charts $(U,\varphi)$ at $p$, $(V,\psi)$ at $F(p)$ and $(W,\chi)$ at $G(F(p))$ such that $F(U) \subseteq V$ and $G(V) \subseteq W$, and write $\tilde F = \psi \circ F \circ \varphi^{-1}$, $\tilde G = \chi \circ G \circ \psi^{-1}$ and $\widetilde{G \circ F} = \chi \circ (G \circ F) \circ \varphi^{-1}$ for the coordinate representations. Then $\widetilde{G \circ F} = \tilde G \circ \tilde F$ on $\varphi(U)$, and
>
> $$
> \big(\widetilde{G \circ F}\big)'\big(\varphi(p)\big) = \tilde G'\big(\psi(F(p))\big)\; \tilde F'\big(\varphi(p)\big):
> $$
>
> the matrix of $(G \circ F)_{*p}$ is the product of the matrices of $G_{*F(p)}$ and $F_{*p}$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-12-23

> [!proof]+ Proof
> $\chi \circ G \circ F \circ \varphi^{-1} = (\chi \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$ on $\varphi(U)$. By the Chain Rule (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]]) the matrix of $(G\circ F)_{*p}$ is the product of the matrices of $G_{*F(p)}$ and $F_{*p}$, and by Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] the three matrices are the three Jacobians. The formula is also the Euclidean chain rule applied to $\tilde G \circ \tilde F$; the two routes agree, as they must.

^pf-12-23

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[Multivariable Chain Rule|452 §10.2]]

![[m591-12-11.svg]]
*Upstairs the composite of maps between manifolds; downstairs the composite of their coordinate representations. Each square commutes, so the outer rectangle does, and differentiating the bottom row at $\varphi(p)$ multiplies the Jacobians.*

> [!remark]- Connections
> - The Euclidean chain rule for Jacobians: [[§10 Composition of Functions and the Chain Rule#^rem-10-4|452 §10 (Chain Rule for Jacobians)]]; matrix of a product: [[§9 Matrices#^ladr-3-43|LADR 3.43]].

> [!theorem] Corollary §12.24: Change of Coordinates
> If $(U, \varphi)$ and $(\tilde U, \tilde\varphi)$ are two smooth charts at $p$, with coordinates $x^i$ and $\tilde x^j$, then
>
> $$
> \frac{\partial}{\partial \tilde x^j}\Big|_p = \sum_{i=1}^n \frac{\partial x^i}{\partial \tilde x^j}(p)\, \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> and the change-of-basis matrix is the Jacobian of the transition function $\varphi \circ \tilde\varphi^{-1}$ at $\tilde\varphi(p)$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-12-24

> [!proof]+ Proof
> Apply Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] to $F = \mathrm{id}_M$, with the chart $\tilde\varphi$ on the source and $\varphi$ on the target. Then $F^i = x^i$, the coordinate representation is the transition $\varphi \circ \tilde\varphi^{-1}$, and $(\mathrm{id}_M)_{*p} = \mathrm{id}$ by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]].

^pf-12-24

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]]

> [!remark]- Connections
> - The change-of-basis formula of linear algebra: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].
> - Transition functions: [[§2 Topological Manifolds#^def-2-4|Def. §2.4]].

> [!example] Example §12.3: Polar Coordinates
> On $M = \mathbb{R}^2 \setminus \{(x, 0) \mid x \le 0\}$ take the standard chart $(x, y)$ and the polar chart $(r, \theta)$, $0 < r$, $-\pi < \theta < \pi$, with $x = r\cos\theta$ and $y = r\sin\theta$. By Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]],
>
> $$
> \frac{\partial}{\partial r} = \cos\theta\, \frac{\partial}{\partial x} + \sin\theta\, \frac{\partial}{\partial y}, \qquad
> \frac{\partial}{\partial \theta} = -r\sin\theta\, \frac{\partial}{\partial x} + r\cos\theta\, \frac{\partial}{\partial y},
> $$
>
> the coefficients being $\partial x/\partial r$, $\partial y/\partial r$ and $\partial x/\partial\theta$, $\partial y/\partial\theta$.
>
> *Lee: cf. Example C.37*

^ex-12-3

![[m591-12-12.svg]]
*At a point $p$ at radius $r$, the four coordinate derivations — elements of the abstract tangent space $T_pM$ — drawn as the vectors of $T^{\mathrm{geo}}_pM = \mathbb{R}^2$ they correspond to under the identification $\partial_x \leftrightarrow e_1$, $\partial_y \leftrightarrow e_2$ of Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]] below (all at the common scale $0.7$). The polar ones are the radial and tangential directions, but $\partial_\theta$ is not a unit vector: it has length $r$, because it records the velocity of the curve $\theta \mapsto (r\cos\theta, r\sin\theta)$ along which the other coordinate is held fixed. A coordinate vector depends on the whole chart, not only on its own coordinate function — the same abstract tangent space, and a different matrix for every map out of it.*

> [!remark]- Connections
> - Polar coordinates in multivariable calculus (Jacobians, change of variables): [[Polar and spherical coordinates]].

> [!theorem] Proposition §12.25: Agreement with the Vector-Space Differential
> Let $W \subseteq \mathbb{R}^m$ be open, $F : W \to \mathbb{R}^n$ smooth, and $a \in W$, and identify the abstract tangent spaces $T_aW \cong \mathbb{R}^m$ and $T_{F(a)}\mathbb{R}^n \cong \mathbb{R}^n$ by $\partial/\partial r^i \mapsto e_i$ — that is, with the geometric tangent spaces $T^{\mathrm{geo}}_aW = \mathbb{R}^m$ and $T^{\mathrm{geo}}_{F(a)}\mathbb{R}^n = \mathbb{R}^n$. Then $F_{*a}$ corresponds to the Jacobian $F'(a)$, i.e. to the differential $dF_a$ of [[§10 Vector Spaces and Matrix Groups#The Differential of a Map Between Vector Spaces|§10, The Differential of a Map Between Vector Spaces]]. Under the same identification, $v = \sum_i v^i e_i$ corresponds to the derivation
>
> $$
> [g] \longmapsto \sum_i v^i\, \frac{\partial g}{\partial r^i}(a) = \frac{d}{dt}\Big|_{t=0} g(a + tv),
> $$
>
> the directional derivative $D_v$ of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#From Tangent Vectors to Derivations|§12, From Tangent Vectors to Derivations]].
>
> *Lee: Proposition 3.13 and Corollary 3.3*

^prop-12-25

> [!proof]+ Proof
> Apply Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] with the identity charts: then $\tilde F = F$, and the matrix of $F_{*a}$ is $F'(a)$. The second statement is the chain rule applied to $t \mapsto g(a + tv)$.

^pf-12-25

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark]- Connections
> - The differential between vector spaces: [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]]; in calculus, [[§8 The Differential#^def-8-1|452 Def. §8.1]] and [[Directional Derivative Formula|452 §7.1 (Directional Derivative Formula)]].

> [!theorem] Corollary §12.26: The Tangent Space to a Vector Space
> Let $V$ be a finite-dimensional vector space with its standard smooth structure, and $a \in V$. The map
>
> $$
> V \to T_aV, \qquad v \mapsto D_v|_a, \qquad D_v|_a[f] = \frac{d}{dt}\Big|_{t=0} f(a + tv),
> $$
>
> is a linear isomorphism, defined without any choice of basis. For every linear map $L : V \to W$, $L_{*a}(D_v|_a) = D_{Lv}|_{La}$.
>
> *Lee: Proposition 3.13*

^cor-12-26

> [!proof]+ Proof
> For linear $L$, $L_{*a}(D_v|_a)[g] = D_v|_a[g \circ L] = \frac{d}{dt}\big|_0\, g(La + t\,Lv) = D_{Lv}|_{La}[g]$. Now take $L = L_0 : V \to \mathbb{R}^m$ a linear coordinate system. It is a chart, hence a diffeomorphism (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]]), so $(L_0)_{*a}$ is an isomorphism, and it carries $D_v|_a$ to $D_{L_0 v}|_{L_0 a}$, which is $\sum_i (L_0 v)^i\,\partial/\partial r^i$ by Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]. The composite $v \mapsto L_0 v \mapsto \sum_i (L_0v)^i\,\partial/\partial r^i$ is an isomorphism, hence so is $v \mapsto D_v|_a$. The defining formula mentions no basis.

^pf-12-26

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]], [[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Vector Spaces and Matrix Groups#^def-10-8|Def. §10.8]]

> [!remark] Remark
> This is what licenses the shared notation $dF_p$: on open subsets of Euclidean spaces the abstract differential *is* the Jacobian, and between vector spaces it is the map of Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]]. It also closes a loop opened in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#From Tangent Vectors to Derivations|§12, From Tangent Vectors to Derivations]], where a tangent vector $v$ was traded for the operator $D_v$; in $\mathbb{R}^n$ that trade is exactly the identification $e_i \leftrightarrow \partial/\partial r^i$.

^rem-12-13

> [!definition] Definition §12.13: Rank and Regular Values of a Smooth Map
> Let $F : M \to N$ be a smooth map. The **rank** of $F$ at $p$ is the rank of the linear map $F_{*p} : T_pM \to T_{F(p)}N$ of abstract tangent spaces; by Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] it is the rank of the Jacobian of any coordinate representation. A point $p$ is a **regular point** of $F$ if $F_{*p}$ is surjective, and $c \in N$ is a **regular value** if every $p \in F^{-1}(c)$ is a regular point.
>
> *Lee: Ch. 4 and Ch. 5, p. 105*

^def-12-13

> [!remark]- Connections
> - The Euclidean definition it extends: [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]]; restated with critical points in [[§14 Local Diffeomorphisms and Submersions#^def-14-3|Def. §14.3]].
> - A regular point is a point where $F$ is a submersion: [[§14 Local Diffeomorphisms and Submersions#^def-14-2|Def. §14.2]].

> [!remark] Remark: The Map Is Intrinsic — the Matrix Is Not
> Uribe's closing point. The linear map $F_{*p}$ is defined with no choices, but its matrix depends on both charts: by Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]], changing them multiplies the matrix on each side by the Jacobian of a transition function. So only properties of $F_{*p}$ that survive such changes — its rank, kernel and image, injectivity and surjectivity — are properties of $F$, which is why the definition above is phrased through $F_{*p}$ rather than through a matrix. By Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]] it agrees with Definition [[§4 The Regular Value Theorem#^def-4-2|§4.2]] in the Euclidean case. A regular point is exactly a point at which $F$ is a *submersion*, in the sense of Definition [[§14 Local Diffeomorphisms and Submersions#^def-14-2|§14.2]]; maps with bijective, surjective and injective differentials are the subject of [[§14 Local Diffeomorphisms and Submersions|§14]].

^rem-12-14

> [!theorem] Proposition §12.27: Regular Values Inside One Chart
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$. Suppose there are smooth charts $(U, \varphi)$ of $M$ and $(V, \psi)$ of $N$ with
>
> $$
> F^{-1}(c) \subseteq U, \qquad c \in V, \qquad F(U) \subseteq V .
> $$
>
> Let $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ be the coordinate representation of $F$, a smooth map on the open set $\varphi(U) \subseteq \mathbb{R}^m$, and put $\tilde c = \psi(c) \in \mathbb{R}^n$. Then:
> 1. $\varphi$ restricts to a homeomorphism from the level set $F^{-1}(c) \subseteq M$ onto the Euclidean level set $\tilde F^{-1}(\tilde c) \subseteq \varphi(U)$;
> 2. $c$ is a regular value of $F$ in the sense of Definition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-13|§12.13]] if and only if $\tilde c$ is a regular value of $\tilde F$ in the sense of Definition [[§4 The Regular Value Theorem#^def-4-2|§4.2]];
> 3. in that case $F^{-1}(c)$ is a topological manifold of dimension $m - n$.

^prop-12-27

> [!proof]+ Proof
> (1) Let $x \in \varphi(U)$ and $q = \varphi^{-1}(x) \in U$. Since $F(U) \subseteq V$ and $\psi$ is injective on $V$,
>
> $$
> \tilde F(x) = \tilde c \iff \psi\big(F(q)\big) = \psi(c) \iff F(q) = c .
> $$
>
> So $\varphi\big(F^{-1}(c) \cap U\big) = \tilde F^{-1}(\tilde c)$, and $F^{-1}(c) \cap U = F^{-1}(c)$ by hypothesis. A homeomorphism restricts to a homeomorphism from any subset onto its image, both with the subspace topology.
>
> (2) Let $p \in F^{-1}(c)$. By Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], the matrix of $F_{*p}$ in the coordinate bases of the two charts is the Jacobian $\tilde F'(\varphi(p))$, and a linear map is surjective exactly when its matrix has rank equal to the dimension of the target (Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]]). So $p$ is a regular point of $F$ if and only if $\varphi(p)$ is a regular point of $\tilde F$. By (1), $p$ runs over $F^{-1}(c)$ exactly as $\varphi(p)$ runs over $\tilde F^{-1}(\tilde c)$.
>
> (3) By (2) and Corollary [[§4 The Regular Value Theorem#^cor-4-4|§4.4]], applied on the open set $\varphi(U) \subseteq \mathbb{R}^m$ with $k = n$, the Euclidean level set $\tilde F^{-1}(\tilde c)$ is a topological manifold of dimension $m - n$. By (1), $F^{-1}(c)$ is homeomorphic to it, and being a topological manifold is preserved by homeomorphisms.

^pf-12-27

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-13|Def. §12.13]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[§4 The Regular Value Theorem#^cor-4-4|§4.4]], [[§9 Continuous Functions#^prop-9-3|590 §9.3]]

![[m591-12-13.svg]]
*The proposition in one square. The level set upstairs is carried by the chart onto a level set downstairs, in Euclidean space, and the question “is $c$ regular?” is carried with it: surjectivity of $F_{*p}$ upstairs is the rank of $\tilde F'$ downstairs.*

> [!remark] Remark: The Strategy
> To show that $c$ is a regular value of a map between manifolds, and to see its level set:
> 1. *Locate the level set.* Show that $F^{-1}(c)$ lies inside a single chart domain $U$, and that $F(U)$ lies in a chart domain $V$ around $c$.
> 2. *Go downstairs.* Write the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$, an ordinary map between open subsets of Euclidean spaces.
> 3. *Compute as in [[§4 The Regular Value Theorem|§4]].* Check that the Jacobian of $\tilde F$ has full rank $n$ at every point of the Euclidean level set $\tilde F^{-1}(\tilde c)$.
> 4. *Come back up.* By Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|§12.27]], $c$ is a regular value of $F$, and $F^{-1}(c)$ is homeomorphic, through the chart, to a Euclidean regular level set: a manifold of dimension $\dim M - \dim N$.
>
> Assignment 3, Problem 4 is exactly this. For the moment map $F : \mathbb{CP}^n \to \mathbb{R}^n$ and $c$ in the interior of the simplex, every point of $F^{-1}(c)$ has all homogeneous coordinates nonzero, so $F^{-1}(c) \subseteq U_0$ (step 1). The target chart is the identity of $\mathbb{R}^n$, and $\varphi_0(U_0) = \mathbb{C}^n \cong \mathbb{R}^{2n}$, so $\tilde F$ is an explicit rational map $\mathbb{R}^{2n} \to \mathbb{R}^n$ (step 2). Its Jacobian has rank $n$ on the level set (step 3). So the fibre is an $n$-dimensional manifold (step 4) — in this case a regular level set of $\mathbb{R}^{2n}$ itself, exactly the situation of [[§4 The Regular Value Theorem|§4]]. When a level set does not fit in one chart, the same argument applies around each of its points separately, as the next corollary shows.

^rem-12-15

> [!theorem] Corollary §12.28: Regular Level Sets Are Topological Manifolds
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$ a regular value of $F$. Then $F^{-1}(c)$, with the subspace topology, is a topological manifold of dimension $m - n$ (or empty).

^cor-12-28

> [!proof]+ Proof
> Hausdorffness and second countability are inherited from $M$ (Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|§3.5]]). For local Euclideanness, let $p \in F^{-1}(c)$. Choose smooth charts $(V, \psi)$ around $c$ and $(U_0, \varphi_0)$ around $p$, and put $U = U_0 \cap F^{-1}(V)$, an open neighbourhood of $p$ because $F$ is continuous; restricting $\varphi_0$ gives a smooth chart $(U, \varphi)$ (Lemma [[§2 Topological Manifolds#^lem-2-11|§2.11]]). Apply Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|§12.27]] to the restriction $F|_U : U \to N$, a smooth map on the open submanifold $U$: its level set $F^{-1}(c) \cap U$ lies in $U$, it maps $U$ into $V$, and $c$ is still a regular value, since $T_qU = T_qM$ and $(F|_U)_{*q} = F_{*q}$ for $q \in U$ (Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]]). So $F^{-1}(c) \cap U$, an open neighbourhood of $p$ in $F^{-1}(c)$, is a topological manifold of dimension $m - n$; in particular $p$ has a neighbourhood in $F^{-1}(c)$ homeomorphic to an open subset of $\mathbb{R}^{m-n}$.

^pf-12-28

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|§3.5]], [[§2 Topological Manifolds#^lem-2-11|§2.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|§12.27]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|§12.13]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-13|Def. §12.13]]

> [!remark]- Connections
> - The smooth half, $F^{-1}(c)$ a submanifold with tangent space $\ker F_{*p}$: [[§15 Submanifolds#^thm-15-6|§15.6]]; the Euclidean original: [[§4 The Regular Value Theorem#^thm-4-3|§4.3]].

This is the topological half of the regular value theorem for manifolds, and it is [[§4 The Regular Value Theorem|§4]] applied chart by chart. The smooth half — that $F^{-1}(c)$ is a smooth *submanifold* of $M$, with tangent space $\ker F_{*p}$ — came in Lecture 12, as Theorem [[§15 Submanifolds#^thm-15-6|§15.6]], proved with the local normal form for submersions (Theorem [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|§14.5]]): near each point of the level set, $F$ is a projection, so the level set is a coordinate slice. It is Lee's Corollary 5.14 and Proposition 5.38. The corollary above is now a consequence of it, a submanifold being in particular a topological manifold, but its proof — [[§4 The Regular Value Theorem|§4]] applied chart by chart — is more elementary.

## Tangent Vectors as Velocities of Curves

*Assignment 3, Problem 2.* Tangent vectors were introduced with two faces: velocities of curves, and derivations (the [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-5|remark]] at the start of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#Derivations and the Abstract Tangent Space|§12, Derivations and the Abstract Tangent Space]]). For regular level sets the two were identified by Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]], through the ambient space. This subsection identifies them on *every* smooth manifold, with no ambient space at all.

> [!definition] Definition §12.14: Smooth Curve and Its Velocity
> Let $J \subseteq \mathbb{R}$ be an open interval containing $0$, with its standard smooth structure and coordinate $t$. A **smooth curve** in $M$ is a smooth map $\gamma : J \to M$. If $\gamma(0) = p$, the **velocity** of $\gamma$ at $0$ is the abstract tangent vector
>
> $$
> D_\gamma = \gamma_{*0}\Big(\frac{d}{dt}\Big|_0\Big) \in T_pM, \qquad\text{explicitly}\qquad D_\gamma[f] = \frac{d}{dt}\Big|_{t=0} f\big(\gamma(t)\big).
> $$
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^def-12-14

> [!remark]- Connections
> - The geometric velocity $\gamma'(0)$ of a curve in $\mathbb{R}^N$: [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]]; differentials computed by curves between vector spaces: [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]].

The explicit formula is the definition of the pushforward: $\gamma_{*0}(d/dt|_0)[f] = d/dt|_0\,[f \circ \gamma]$, the ordinary derivative at $0$ of the function $f \circ \gamma$, which is defined near $0$. Lee writes $\gamma'(0)$ for $D_\gamma$. These notes keep $\gamma'(0)$ for the ordinary derivative of a curve in $\mathbb{R}^N$, which is a *geometric* tangent vector, and write $D_\gamma$ for the abstract one, as Assignment 3 does.

> [!theorem] Proposition §12.29: Velocity in Coordinates
> $D_\gamma$ is a derivation at $p$. In a chart $(U, \varphi)$ at $p$ with coordinate functions $x^1, \ldots, x^n$,
>
> $$
> D_\gamma = \sum_{j=1}^n \big(x^j \circ \gamma\big)'(0)\, \frac{\partial}{\partial x^j}\Big|_p .
> $$
>
> In particular $D_\gamma$ depends only on the velocity $(\varphi \circ \gamma)'(0) \in \mathbb{R}^n$ of the coordinate curve $\varphi \circ \gamma$.
>
> *Lee: Ch. 3, Velocity Vectors of Curves*

^prop-12-29

> [!proof]+ Proof
> $D_\gamma$ is a pushforward of a derivation, hence a derivation (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]]) — which is why Assignment 3 could waive the check. By the universal formula (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]]), the $j$-th coefficient of $D_\gamma$ is $D_\gamma[x^j] = (x^j \circ \gamma)'(0)$.

^pf-12-29

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14|Def. §12.14]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|§12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]]

The same formula comes out of the chain rule directly, as in the assignment's solution. With $c = \varphi \circ \gamma$ and $c^j = r^j \circ c = x^j \circ \gamma$, near $0$ one has $f \circ \gamma = f_\varphi \circ c$, so

$$
D_\gamma[f] = \frac{d}{dt}\Big|_0 f_\varphi\big(c(t)\big) = \sum_{j} \frac{\partial f_\varphi}{\partial r^j}\big(\varphi(p)\big)\,(c^j)'(0) = \sum_j (c^j)'(0)\,\frac{\partial}{\partial x^j}\Big|_p[f].
$$

Each input $r^j$ of $f_\varphi$ moves at speed $(c^j)'(0)$ along the curve, and contributes $\partial f_\varphi/\partial r^j \cdot (c^j)'(0)$ to the rate of change.

> [!theorem] Theorem §12.30: Every Tangent Vector Is a Velocity
> For every $D \in T_pM$ there is a smooth curve $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$ and $D_\gamma = D$.
>
> *Lee: Proposition 3.23*

^thm-12-30

> [!proof]+ Proof
> *(Assignment 3, Problem 2.)* Fix a chart $(U, \varphi)$ at $p$ with coordinate functions $x^i$, and put $a^i = D[x^i]$ and $a = (a^1, \ldots, a^n) \in \mathbb{R}^n$. These are the coefficients of $D$ in the universal formula; the freedom lies in the curve.
>
> *The curve downstairs.* Let $c(t) = \varphi(p) + t\,a$. Since $\varphi(U)$ is open, some ball $B(\varphi(p), r)$ lies in it. If $a \ne 0$ take $\varepsilon = r/|a|$, so that $|c(t) - \varphi(p)| = |t|\,|a| < r$ for $|t| < \varepsilon$. If $a = 0$, which happens exactly when $D = 0$, take $\varepsilon = 1$. In either case $c : (-\varepsilon, \varepsilon) \to \varphi(U)$ is smooth, being affine, with $c(0) = \varphi(p)$ and $c'(0) = a$.
>
> *The curve upstairs.* Let $\gamma = \varphi^{-1} \circ c$. It is smooth, since its coordinate representation in the chart $(U,\varphi)$ is $\varphi \circ \gamma = c$, and $\gamma(0) = p$. Its coordinate curve is $\varphi \circ \gamma = c$, so $(x^j \circ \gamma)'(0) = (c^j)'(0) = a^j$.
>
> *Conclusion.* By Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-29|§12.29]] and the universal formula,
>
> $$
> D_\gamma = \sum_j a^j\, \frac{\partial}{\partial x^j}\Big|_p = \sum_j D[x^j]\, \frac{\partial}{\partial x^j}\Big|_p = D.
> $$

^pf-12-30

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-29|§12.29]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-11|Def. §12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14|Def. §12.14]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]

Assignment 3's solution first treats the basis vectors $\partial/\partial x^i|_p$, using curves with $c'(0) = e_i$, and then the general case. The general argument contains the basis case, with $a = e_i$ and $c(t) = \varphi(p) + t\,e_i$, so it is presented here alone.

> [!theorem] Corollary §12.31: Velocity of a Composite — Computing Differentials by Curves
> Let $F : M \to N$ be smooth and $\gamma$ a smooth curve in $M$ with $\gamma(0) = p$. Then $D_{F \circ \gamma} = F_{*p}(D_\gamma)$. Consequently, for every $D \in T_pM$,
>
> $$
> F_{*p}(D) = D_{F \circ \gamma} \qquad \text{for any smooth curve } \gamma \text{ with } \gamma(0) = p \text{ and } D_\gamma = D,
> $$
>
> and such a curve exists by Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30|§12.30]].
>
> *Lee: Proposition 3.24 and Corollary 3.25*

^cor-12-31

> [!proof]+ Proof
> By the Chain Rule (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]]), $D_{F \circ \gamma} = (F \circ \gamma)_{*0}(d/dt|_0) = F_{*p}\big(\gamma_{*0}(d/dt|_0)\big) = F_{*p}(D_\gamma)$.

^pf-12-31

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14|Def. §12.14]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30|§12.30]]

This is Lee's main computational tool: to find $F_{*p}(D)$, choose any curve with velocity $D$ and differentiate $F$ along it. It is the manifold version of Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], and it is how Lee computes the differential of the determinant (Problem 7-4).

![[m591-12-14.svg]]
*The proof in one picture. Downstairs, in the chart, the curve is the straight line through $\varphi(p)$ in the direction of the coefficient vector $a = (D[x^1], \ldots, D[x^n])$. The chart carries it upstairs to a curve $\gamma$ in $M$, bent by whatever distortion $\varphi^{-1}$ introduces. The bending is invisible to the velocity, which depends only on $(\varphi \circ \gamma)'(0) = a$ — so the velocity is $D$.*

![[m591-12-15.svg]]
*The same construction as a diagram: the curve is built downstairs as $c$ and lifted by $\varphi^{-1}$, and the triangle commutes, $\varphi \circ \gamma = c$.*

> [!remark] Remark: The Two Faces Reconciled
> Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30|§12.30]] says the map $\gamma \mapsto D_\gamma$, from smooth curves through $p$ to $T_pM$, is onto. By Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-29|§12.29]], two curves have the same velocity exactly when their coordinate curves have the same velocity in one chart, and then in every chart. So $T_pM$ may equally be described as *curves through $p$, modulo having the same velocity in coordinates* — the intrinsic “velocities of curves” definition of the tangent space, now a theorem, on every manifold, with no ambient space. For a regular level set, the abstract velocity $D_\gamma$ is the derivation $D_{\gamma'(0)}$ attached to the geometric velocity $\gamma'(0) \in T^{\mathrm{geo}}_pM$ (Proposition [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|§12.1]](2)). So the identification of Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|§12.8]] is the statement that the two notions of velocity agree.

^rem-12-16

## Tangent Spaces of Products

*Lecture 11. “There is a natural isomorphism” between the tangent space of a product and the direct sum of the tangent spaces of the factors — “natural meaning coordinate-free.” Uribe gave three ways to see it: by the inclusions of the factors, by curves, and in coordinates. He added that this part of the course is, in his experience, “the most abstract, somehow the hardest part”, and that while physicists tend to favour coordinates and pure mathematicians abstract settings, “you need both.”*

Throughout, $p = (p_1, p_2) \in M_1 \times M_2$, and $\iota_1 = \iota^{p_2} : M_1 \to M_1 \times M_2$, $\iota_2 = \iota^{p_1} : M_2 \to M_1 \times M_2$ are the slice inclusions through $p$ (Definition [[§8 Differentiable Structures#^def-8-17|§8.17]]).

> [!theorem] Theorem §12.32: The Tangent Space of a Product
> The linear map
>
> $$
> \Theta : T_{p_1}M_1 \oplus T_{p_2}M_2 \longrightarrow T_p(M_1 \times M_2), \qquad \Theta(v, w) = \iota_{1*}v + \iota_{2*}w,
> $$
>
> is an isomorphism, defined without charts, with inverse $\Psi(D) = (\pi_{1*}D, \pi_{2*}D)$. In particular $\iota_{1*}$ and $\iota_{2*}$ are injective, and $T_p(M_1 \times M_2)$ is the internal direct sum of their images, $\Theta\big(T_{p_1}M_1 \oplus \{0\}\big)$ and $\Theta\big(\{0\} \oplus T_{p_2}M_2\big)$.
>
> *Lee: Proposition 3.14*

^thm-12-32

> [!proof]+ Proof
> *(Stated in lecture; Uribe left the injectivity as “check”.)* First, the pushforward along a constant map is zero: if $\kappa$ is constant with value $q_0$ and $[g]$ is a germ at $q_0$, then $g \circ \kappa$ is constant, so $(\kappa_* D)[g] = D[g \circ \kappa] = 0$ because derivations kill constants (Lemma [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]]). Now $\pi_1 \circ \iota_1 = \mathrm{id}_{M_1}$ and $\pi_2 \circ \iota_2 = \mathrm{id}_{M_2}$, while $\pi_2 \circ \iota_1$ and $\pi_1 \circ \iota_2$ are constant. By the Chain Rule (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]]),
>
> $$
> \pi_{1*}\iota_{1*} = \mathrm{id}, \qquad \pi_{2*}\iota_{2*} = \mathrm{id}, \qquad \pi_{2*}\iota_{1*} = 0, \qquad \pi_{1*}\iota_{2*} = 0,
> $$
>
> so $\Psi(\Theta(v, w)) = (v, w)$, and $\Theta$ is injective. Both spaces have dimension $m_1 + m_2$ (Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]] and Propositions [[§8 Differentiable Structures#^prop-8-19|§8.19]], [[§10 Vector Spaces and Matrix Groups#^prop-10-7|§10.7]]), so $\Theta$ is an isomorphism (Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](1)) with inverse $\Psi$. The last sentence is Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-7|§10.7]](1), carried across $\Theta$.

^pf-12-32

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-6|§12.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Def. §12.10]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|§12.11]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§8 Differentiable Structures#^prop-8-19|§8.19]], [[§8 Differentiable Structures#^def-8-17|Def. §8.17]], [[§10 Vector Spaces and Matrix Groups#^prop-10-7|§10.7]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]]

![[m591-12-16.svg]]

![[m591-12-17.svg]]
*The slice inclusions and the projections through $p$. The four identities $\pi_1 \iota_1 = \mathrm{id}$, $\pi_2 \iota_2 = \mathrm{id}$, and $\pi_2 \iota_1$, $\pi_1 \iota_2$ constant, pushed forward to tangent spaces, are the whole proof that $\Psi \circ \Theta = \mathrm{id}$.*

> [!remark]- Connections
> - Linear algebra of products and direct sums: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92]] (dimension of a product), [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93]] (products and direct sums).
> - The product smooth structure it rests on: [[§8 Differentiable Structures#^prop-8-19|§8.19]]; projections of products are submersions: [[§14 Local Diffeomorphisms and Submersions#^ex-14-4|Ex. §14.4]].

**Partial derivatives in the $M_1$ variables.** For $v \in T_{p_1}M_1$ and a germ $[f]$ at $p$,

$$
(\iota_{1*}v)[f] = v\big[f \circ \iota_1\big], \qquad (f \circ \iota_1)(q) = f(q, p_2) :
$$

to push $v$ forward, restrict $f$ to the slice $M_1 \times \{p_2\}$ and differentiate there. So the first summand consists of derivations “only with respect to the $M_1$ variables”, with $p_2$ held fixed — partial derivatives in the direction of $M_1$ — and the second of partial derivatives in the direction of $M_2$.

![[m591-12-18.svg]]
*The isomorphism in one picture. Through $p$ run the two slices, $M_1 \times \{p_2\}$ and $\{p_1\} \times M_2$. Pushing $v$ and $w$ forward along the slice inclusions gives tangent vectors along the slices, and every $D \in T_p(M_1 \times M_2)$ is uniquely their sum. The projections take $D$ back to $v$ and $w$: $\Psi(D) = (\pi_{1*}D, \pi_{2*}D) = (v, w)$.*

> [!theorem] Corollary §12.33: Product Coordinates
> In product coordinates $(x^1, \ldots, x^{m_1}, y^1, \ldots, y^{m_2})$ at $p$,
>
> $$
> \iota_{1*}\Big(\frac{\partial}{\partial x^i}\Big|_{p_1}\Big) = \frac{\partial}{\partial x^i}\Big|_p, \qquad \iota_{2*}\Big(\frac{\partial}{\partial y^j}\Big|_{p_2}\Big) = \frac{\partial}{\partial y^j}\Big|_p .
> $$
>
> So the $\partial/\partial x^i|_p$ form a basis of the first summand and the $\partial/\partial y^j|_p$ a basis of the second.
>
> *Lee: Proposition 3.14*

^cor-12-33

> [!proof]+ Proof
> By Proposition [[§8 Differentiable Structures#^prop-8-20|§8.20]] the coordinate representation of $\iota_1$ is $r \mapsto (r, \varphi_2(p_2))$, with Jacobian $\binom{I_{m_1}}{0}$. By Theorem [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]] its $i$-th column says $\iota_{1*}(\partial/\partial x^i|_{p_1}) = \partial/\partial x^i|_p$. The same for $\iota_2$.

^pf-12-33

*Uses:* [[§8 Differentiable Structures#^prop-8-20|§8.20]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|§12.22]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|§12.32]]

> [!theorem] Corollary §12.34: Velocities of Curves in a Product
> Let $\gamma = (\gamma_1, \gamma_2)$ be a smooth curve in $M_1 \times M_2$ with $\gamma(0) = p$. Then $\Psi(D_\gamma) = (D_{\gamma_1}, D_{\gamma_2})$, that is, $D_\gamma = \iota_{1*}D_{\gamma_1} + \iota_{2*}D_{\gamma_2}$. In particular, if $\gamma_2$ is constant — a “horizontal” curve $\gamma(t) = (\gamma_1(t), p_2)$ — then $D_\gamma = \iota_{1*}D_{\gamma_1}$ lies in the first summand.

^cor-12-34

> [!proof]+ Proof
> $\gamma_i = \pi_i \circ \gamma$, so $\pi_{i*}D_\gamma = D_{\pi_i \circ \gamma} = D_{\gamma_i}$ by Corollary [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|§12.31]]. If $\gamma_2$ is constant, $D_{\gamma_2} = 0$.

^pf-12-34

*Uses:* [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|§12.31]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|§12.32]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-14|Def. §12.14]]

This is the second of Uribe's three views, and it uses the velocities of Assignment 3, Problem 2 ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#Tangent Vectors as Velocities of Curves|§12, Tangent Vectors as Velocities of Curves]]).
