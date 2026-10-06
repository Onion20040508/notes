---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 25
tags: [differentiable-manifolds, math591]
---
← [[§24 Transversality]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§26 Derivations and the Abstract Tangent Space]] →

*Stage: abstract — Germs of smooth functions at a point — the objects that derivations act on, available on every manifold, including those built by quotients. The motivation from geometric tangent vectors closes [[§23 The Geometric Tangent Space|§23]].*

Point (1) of [[§23 The Geometric Tangent Space#^prop-23-8|Proposition §23.8]], at the end of [[§23 The Geometric Tangent Space|§23]], is made official here: the objects a derivation eats are not functions but germs.

> [!definition] Definition §25.1: Agreement Near a Point
> Let $M$ be a smooth manifold and $p \in M$. Consider pairs $(f, U)$ with $U \subseteq M$ open, $p \in U$, and $f : U \to \mathbb{R}$ smooth. Two such pairs **agree near $p$**, written $(f,U) \sim (g,V)$, if
>
> $$
> \text{there is an open } W \text{ with } p \in W \subseteq U \cap V \text{ and } f|_W = g|_W .
> $$

^def-25-1

> [!theorem] Proposition §25.1: Agreement Near a Point Is an Equivalence Relation
> 1. $\sim$ is an equivalence relation.
> 2. Finitely many pairs in one equivalence class agree on a common open neighbourhood of $p$.

^prop-25-1

> [!proof]+ Proof
> (1) *Reflexive:* take $W = U$. *Symmetric:* the condition is symmetric in the two pairs. *Transitive:* if $f = g$ on an open $W_1 \ni p$ and $g = h$ on an open $W_2 \ni p$, then $f = h$ on $W_1 \cap W_2$, which is open, contains $p$, and lies in both domains.
>
> (2) If $(f_1,U_1), \ldots, (f_k,U_k)$ are equivalent, then for each $i$ there is an open $W_i \ni p$ on which $f_1 = f_i$. On $W = W_2 \cap \cdots \cap W_k$, which is open and contains $p$, all the $f_i$ equal $f_1$. Both parts use only that a *finite* intersection of open sets is open.

^pf-25-1

*Uses:* [[§25 Germs#^def-25-1|Def. §25.1]], [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]

> [!definition] Definition §25.2: Germs of Smooth Functions
> An equivalence class $[f]$ of the relation $\sim$ of Definition [[§25 Germs#^def-25-1|§25.1]] is a **($C^\infty$) germ at $p$**, and each pair $(f,U)$ in it is a **representative** of the germ. The set of all germs at $p$ is denoted $C_p^\infty(M)$.
>
> *Lee: no counterpart; the course's germ-based route (Lee uses $C^\infty(M)$; see Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-3|§26.3]])*

^def-25-2

![[m591-12-2.svg]]
*Two pairs $(f, U)$ and $(g, V)$ that agree on an open $W$ with $p \in W \subseteq U \cap V$ define the same germ, $[f] = [g]$ in $C_p^\infty(M)$.*

> [!example] Example §25.1: No Neighbourhood Serves a Whole Germ
> Part (2) of Proposition [[§25 Germs#^prop-25-1|§25.1]] fails for infinitely many representatives. Work at $p = 0 \in \mathbb{R}$. Let $h(s) = e^{-1/s}$ for $s > 0$ and $h(s) = 0$ for $s \le 0$, the smooth flat function (see Example [[§25 Germs#^ex-25-2|§25.2]] below), and put
>
> $$
> f_n(x) = h\big(x^2 - 1/n^2\big), \qquad n = 1, 2, 3, \ldots
> $$
>
> Each $f_n$ is smooth on all of $\mathbb{R}$ and vanishes exactly on $[-1/n, 1/n]$, so $(f_n, \mathbb{R}) \sim (0, \mathbb{R})$: every $f_n$ represents the zero germ. Yet the set on which all of them agree with $0$ is $\bigcap_n [-1/n, 1/n] = \{0\}$, which contains no open neighbourhood of $0$. The same happens, even more simply, with the representatives $\big(0, (-1/n, 1/n)\big)$: no open set around $0$ lies in all of their domains.

^ex-25-1

> [!remark] Remark
> Nothing in the theory needs a common neighbourhood for a whole class. Every construction on germs — sums, products and evaluation (Proposition [[§25 Germs#^prop-25-2|§25.2]]), derivations, pullbacks — handles finitely many representatives at a time, and part (2) supplies the common neighbourhood for those. The obstruction in the example is exactly that an *infinite* intersection of open sets need not be open. This is also the precise sense in which a germ is not a function on any particular neighbourhood of $p$: its representatives can be shrunk at will, but there is no smallest domain to shrink them to.

^rem-25-1

> [!theorem] Proposition §25.2: $C_p^\infty(M)$ Is an $\mathbb{R}$-Algebra
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

^prop-25-2

> [!proof]+ Proof
> *(Lecture 8 sketched the operations — “taking representatives … and shrinking to a common domain” — and skipped the checks as “tedious”; they are filled in here.)* *Existence of $W$ and smoothness.* $U \cap V$ is open and contains $p$, so $W = U \cap V$ will do; $f|_W + g|_W$ and $f|_W\, g|_W$ are smooth on $W$, so they define germs.
>
> *Independence of representatives.* Suppose $(f,U) \sim (f', U')$ and $(g,V) \sim (g',V')$, say $f = f'$ on $W_1 \ni p$ and $g = g'$ on $W_2 \ni p$. On the open set $W_1 \cap W_2 \ni p$ the four functions satisfy $f + g = f' + g'$ and $fg = f'g'$ pointwise, so the resulting germs agree. Independence of the auxiliary $W$ is the same argument with $f = f'$, $g = g'$.
>
> *Algebra axioms.* Each is an identity between germs that holds for representatives on a common domain, hence holds after passing to classes.
>
> *Evaluation.* If $(f,U) \sim (g,V)$ then $f = g$ near $p$, in particular $f(p) = g(p)$; and evaluation of functions is compatible with sums and products.

^pf-25-2

*Uses:* [[§25 Germs#^def-25-1|Def. §25.1]], [[§25 Germs#^def-25-2|Def. §25.2]], [[§25 Germs#^prop-25-1|§25.1]]

> [!definition] Definition §25.3: Evaluation of a Germ
> The **value** of a germ $[f] \in C_p^\infty(M)$ at $p$ is $[f](p) := f(p)$, independent of the representative by Proposition [[§25 Germs#^prop-25-2|§25.2]]. The map $C_p^\infty(M) \to \mathbb{R}$, $[f] \mapsto [f](p)$, is **evaluation** at $p$.

^def-25-3

> [!remark] Remark: How to Think About a Germ
> Uribe: “when I think of a germ, I think of a representative — a smooth function defined in a neighbourhood — but I know that it is a germ, which means I can shrink its domain arbitrarily, as long as I shrink it to a neighbourhood of $p$.” In practice one works with representatives and checks at the end that the answer is unchanged by shrinking. The formal content of the definition is exactly that shrinking is free.

^rem-25-2

![[m591-12-19.svg]]
*Two representatives of one germ, drawn as graphs over $M = \mathbb{R}$: $f$ (blue) on $U$ and $g$ (red, dashed) on $V$ agree on the shaded open set $W \ni p$ and part ways outside it. The germ $[f] = [g]$ keeps only the common piece near $p$; how large the domains are and what the functions do away from $p$ is forgotten — which is exactly why shrinking a representative's domain is free.*

> [!example] Example §25.2: Germs Versus Taylor Series
> Take $M = \mathbb{R}^n$ and $x_0 \in \mathbb{R}^n$. All partial derivatives of a function at $x_0$ depend only on its germ, so the Taylor series construction descends to a map into the ring of formal power series,
>
> $$
> \mathcal{T} : C_{x_0}^\infty(\mathbb{R}^n) \longrightarrow \mathbb{R}[\![x^1, \ldots, x^n]\!], \qquad
> \mathcal{T}[f] = \sum_{\alpha} \frac{1}{\alpha!}\, \frac{\partial^{|\alpha|} f}{\partial x^\alpha}(x_0)\, (x - x_0)^\alpha ,
> $$
>
> an $\mathbb{R}$-algebra homomorphism. It is *surjective* but *not injective*.

^ex-25-2

> [!proof]+ Justification
> Surjectivity is **Borel's theorem**: every formal power series is the Taylor series at $x_0$ of some smooth function. It is cited, not proved — Uribe: “that's not so easy to show, but it's true.” Failure of injectivity is elementary. Uribe: “You can have totally flat functions that are not zero”; the example is filled in. The function
>
> $$
> f(x) = \begin{cases} e^{-1/|x-x_0|^2}, & x \neq x_0,\\ 0, & x = x_0,\end{cases}
> $$
>
> is smooth with all partial derivatives vanishing at $x_0$ (a standard computation, not reproduced here), so $\mathcal{T}[f] = 0$ while $[f] \neq 0$.

^pf-ex-25-2

*Uses:* [[§25 Germs#^def-25-2|Def. §25.2]], [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]

> [!remark]- Connections
> - The one-variable flat function $e^{-1/x^2}$, a smooth function that is not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; Taylor series: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]].
> - Taylor expansion in several variables: [[Multivariable Taylor's Theorem|452 §11.2 (Multivariable Taylor's Theorem)]].

> [!definition] Definition §25.4: Flat Germ
> A germ $[f] \in C_{x_0}^\infty(\mathbb{R}^n)$ is **flat** if all partial derivatives of $f$, of all orders, vanish at $x_0$; equivalently, $\mathcal{T}[f] = 0$. So the kernel of $\mathcal{T}$ consists exactly of the flat germs.

^def-25-4

> [!remark] Remark
> The moral is that a germ carries strictly more information than its Taylor series — “one of the beauties of being in the $C^\infty$ category.” This is the same phenomenon as the rigidity of $C^\omega$ noted after Definition [[§16 Differentiable Structures#^def-16-5|§16.5]]: a real-analytic germ *is* its Taylor series, which is why there are no analytic bump functions, whereas a $C^\infty$ germ has room to spare.

^rem-25-3
