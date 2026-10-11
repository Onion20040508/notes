---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 27
tags: [differentiable-manifolds, math591]
---
← [[§26 Transversality]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§28 Derivations and the Abstract Tangent Space]] →

*Stage: abstract — Germs of smooth functions at a point — the objects that derivations act on, available on every manifold, including those built by quotients. The motivation from geometric tangent vectors closes [[§25 The Geometric Tangent Space|§25]].*

Point (1) of [[§25 The Geometric Tangent Space#^prop-25-8|Proposition §25.8]], at the end of [[§25 The Geometric Tangent Space|§25]], is made official here: the objects a derivation eats are not functions but germs.

> [!definition] Definition §27.1: Agreement Near a Point
> Let $M$ be a smooth manifold and $p \in M$. Consider pairs $(f, U)$ with $U \subseteq M$ open, $p \in U$, and $f : U \to \mathbb{R}$ smooth. Two such pairs **agree near $p$**, written $(f,U) \sim (g,V)$, if
>
> $$
> \text{there is an open } W \text{ with } p \in W \subseteq U \cap V \text{ and } f|_W = g|_W .
> $$

^def-27-1

> [!theorem] Proposition §27.1: Agreement Near a Point Is an Equivalence Relation
> 1. $\sim$ is an equivalence relation.
> 2. Finitely many pairs in one equivalence class agree on a common open neighbourhood of $p$.

^prop-27-1

> [!proof]+ Proof
> (1) Three properties of $\sim$ must be checked against Definition [[§27 Germs#^def-27-1|§27.1]].
>
> *Reflexive:* take $W = U$. It is open, contains $p$, lies in $U \cap U = U$, and $f|_U = f|_U$; so $(f,U) \sim (f,U)$.
>
> *Symmetric:* the condition is symmetric in the two pairs. Explicitly, if $W$ is open with $p \in W \subseteq U \cap V$ and $f|_W = g|_W$, then the same $W$ satisfies $p \in W \subseteq V \cap U$ and $g|_W = f|_W$; so $(f,U) \sim (g,V)$ implies $(g,V) \sim (f,U)$.
>
> *Transitive:* let $(f,U) \sim (g,V)$ and $(g,V) \sim (h,Z)$. So $f = g$ on an open $W_1 \ni p$ with $W_1 \subseteq U \cap V$, and $g = h$ on an open $W_2 \ni p$ with $W_2 \subseteq V \cap Z$. Then $f = h$ on $W_1 \cap W_2$: for $x \in W_1 \cap W_2$,
>
> $$
> f(x) = g(x) = h(x) .
> $$
>
> The set $W_1 \cap W_2$ is open (an intersection of two open sets), contains $p$, and lies in both domains, $W_1 \cap W_2 \subseteq U \cap Z$. So $(f,U) \sim (h,Z)$.
>
> (2) If $(f_1,U_1), \ldots, (f_k,U_k)$ are equivalent, then for each $i$ there is an open $W_i \ni p$ with $W_i \subseteq U_1 \cap U_i$, on which $f_1 = f_i$ (since $(f_1,U_1) \sim (f_i,U_i)$). On $W = W_2 \cap \cdots \cap W_k$ (take $W = U_1$ if $k = 1$), which is open and contains $p$, all the $f_i$ equal $f_1$. Indeed $W \subseteq U_1 \cap U_2 \cap \cdots \cap U_k$, so every $f_i$ is defined on $W$, and for $x \in W$ and each $i$, $x \in W_i$ gives $f_i(x) = f_1(x)$. Both parts use only that a *finite* intersection of open sets is open.

^pf-27-1

*Uses:* [[§27 Germs#^def-27-1|Def. §27.1]], [[§1 Topological Spaces#^def-1-1|590 Def. §1.1]]

> [!definition] Definition §27.2: Germs of Smooth Functions
> An equivalence class $[f]$ of the relation $\sim$ of Definition [[§27 Germs#^def-27-1|§27.1]] is a **($C^\infty$) germ at $p$**, and each pair $(f,U)$ in it is a **representative** of the germ. The set of all germs at $p$ is denoted $C_p^\infty(M)$.
>
> *Lee: no counterpart; the course's germ-based route (Lee uses $C^\infty(M)$; see Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]])*

^def-27-2

![[m591-12-2.svg]]
*Two pairs $(f, U)$ and $(g, V)$ that agree on an open $W$ with $p \in W \subseteq U \cap V$ define the same germ, $[f] = [g]$ in $C_p^\infty(M)$.*

> [!example] Example §27.1: No Neighbourhood Serves a Whole Germ
> Part (2) of Proposition [[§27 Germs#^prop-27-1|§27.1]] fails for infinitely many representatives. Work at $p = 0 \in \mathbb{R}$. Let $h(s) = e^{-1/s}$ for $s > 0$ and $h(s) = 0$ for $s \le 0$, the smooth flat function (see Example [[§27 Germs#^ex-27-2|§27.2]] below), and put
>
> $$
> f_n(x) = h\big(x^2 - 1/n^2\big), \qquad n = 1, 2, 3, \ldots
> $$
>
> Each $f_n$ is smooth on all of $\mathbb{R}$ and vanishes exactly on $[-1/n, 1/n]$, so $(f_n, \mathbb{R}) \sim (0, \mathbb{R})$: every $f_n$ represents the zero germ. Yet the set on which all of them agree with $0$ is $\bigcap_n [-1/n, 1/n] = \{0\}$, which contains no open neighbourhood of $0$. The same happens, even more simply, with the representatives $\big(0, (-1/n, 1/n)\big)$: no open set around $0$ lies in all of their domains.

^ex-27-1

> [!remark] Remark
> Nothing in the theory needs a common neighbourhood for a whole class. Every construction on germs — sums, products and evaluation (Proposition [[§27 Germs#^prop-27-2|§27.2]]), derivations, pullbacks — handles finitely many representatives at a time, and part (2) supplies the common neighbourhood for those. The obstruction in the example is exactly that an *infinite* intersection of open sets need not be open. This is also the precise sense in which a germ is not a function on any particular neighbourhood of $p$: its representatives can be shrunk at will, but there is no smallest domain to shrink them to.

^rem-27-1

> [!theorem] Proposition §27.2: $C_p^\infty(M)$ Is an $\mathbb{R}$-Algebra
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

^prop-27-2

> [!proof]+ Proof
> *(Lecture 8 sketched the operations — “taking representatives \ldots and shrinking to a common domain” — and skipped the checks as “tedious”; they are filled in here.)* Let $(f,U)$ and $(g,V)$ be representatives of $[f]$ and $[g]$. Four things must be checked: the operations produce germs, they do not depend on the choices, they satisfy the algebra axioms, and evaluation is a well-defined homomorphism.
>
> *Existence of $W$ and smoothness.* $U \cap V$ is open and contains $p$, so $W = U \cap V$ will do; $f|_W + g|_W$ and $f|_W\, g|_W$ are smooth on $W$, so they define germs. Likewise $\lambda f$ is smooth on $U$.
>
> *Independence of representatives.* Suppose $(f,U) \sim (f', U')$ and $(g,V) \sim (g',V')$, say $f = f'$ on $W_1 \ni p$ and $g = g'$ on $W_2 \ni p$ (Definition [[§27 Germs#^def-27-1|§27.1]]). On the open set $W_1 \cap W_2 \ni p$ the four functions satisfy $f + g = f' + g'$ and $fg = f'g'$ pointwise: for $x \in W_1 \cap W_2$,
>
> $$
> f(x) + g(x) = f'(x) + g'(x), \qquad f(x)\,g(x) = f'(x)\,g'(x) ,
> $$
>
> so the resulting germs agree. To be precise about the auxiliary sets: if the sums are formed on $W \subseteq U \cap V$ and $W' \subseteq U' \cap V'$, then $f|_W + g|_W$ and $f'|_{W'} + g'|_{W'}$ agree on $W \cap W' \cap W_1 \cap W_2$, which is open, contains $p$, and lies in both domains; the same for products. For scalars, $f = f'$ on $W_1$ gives $\lambda f = \lambda f'$ on $W_1$, so $[\lambda f] = [\lambda f']$. Independence of the auxiliary $W$ is the same argument with $f = f'$, $g = g'$ (so $W_1 = U$, $W_2 = V$): two choices $W, W'$ give functions that agree on $W \cap W'$.
>
> *Algebra axioms.* Each is an identity between germs that holds for representatives on a common domain, hence holds after passing to classes. Explicitly: given finitely many germs $[f], [g], [h]$, choose representatives and restrict them to the common open set $W$, the intersection of their domains, which contains $p$; restricting does not change a germ, $(f,U) \sim (f|_W, W)$. By the previous step every operation may be computed on $W$, where it is the pointwise operation on functions. For example, distributivity reads
>
> $$
> \big([f] + [g]\big)[h] = [f + g]\,[h] = \big[(f+g)h\big] = [fh + gh] = [fh] + [gh] = [f][h] + [g][h],
> $$
>
> the middle equality because $(f + g)h = fh + gh$ pointwise on $W$, by distributivity in $\mathbb{R}$. In the same way, each of the remaining axioms reduces to the corresponding identity of real numbers at each point of $W$: associativity and commutativity of $+$ and of $\cdot$; the zero $[0]$, with $[f] + [0] = [f + 0] = [f]$; the negative $-[f] = [-f]$; the unit $[1]$, with $[1][f] = [1 \cdot f] = [f]$; the vector space axioms $\lambda([f] + [g]) = \lambda[f] + \lambda[g]$, $(\lambda + \mu)[f] = \lambda[f] + \mu[f]$, $(\lambda\mu)[f] = \lambda(\mu[f])$, $1[f] = [f]$; and the compatibility $\lambda([f][g]) = (\lambda[f])[g] = [f](\lambda[g])$.
>
> *Evaluation.* If $(f,U) \sim (g,V)$ then $f = g$ near $p$, in particular $f(p) = g(p)$, since $p$ lies in the set $W$ on which they agree; so $[f](p)$ is well defined. And evaluation of functions is compatible with sums and products: with representatives on a common $W \ni p$,
>
> $$
> \big([f] + [g]\big)(p) = (f + g)(p) = f(p) + g(p), \qquad \big([f][g]\big)(p) = (fg)(p) = f(p)\,g(p),
> $$
>
> $$
> (\lambda[f])(p) = \lambda f(p), \qquad [1](p) = 1 ,
> $$
>
> so evaluation is an $\mathbb{R}$-algebra homomorphism $C_p^\infty(M) \to \mathbb{R}$.

^pf-27-2

*Uses:* [[§27 Germs#^def-27-1|Def. §27.1]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§27 Germs#^prop-27-1|§27.1]]

> [!definition] Definition §27.3: Evaluation of a Germ
> The **value** of a germ $[f] \in C_p^\infty(M)$ at $p$ is $[f](p) := f(p)$, independent of the representative by Proposition [[§27 Germs#^prop-27-2|§27.2]]. The map $C_p^\infty(M) \to \mathbb{R}$, $[f] \mapsto [f](p)$, is **evaluation** at $p$.

^def-27-3

> [!remark] Remark: How to Think About a Germ
> Uribe: “when I think of a germ, I think of a representative — a smooth function defined in a neighbourhood — but I know that it is a germ, which means I can shrink its domain arbitrarily, as long as I shrink it to a neighbourhood of $p$.” In practice one works with representatives and checks at the end that the answer is unchanged by shrinking. The formal content of the definition is exactly that shrinking is free.

^rem-27-2

![[m591-12-19.svg]]
*Two representatives of one germ, drawn as graphs over $M = \mathbb{R}$: $f$ (blue) on $U$ and $g$ (red, dashed) on $V$ agree on the shaded open set $W \ni p$ and part ways outside it. The germ $[f] = [g]$ keeps only the common piece near $p$; how large the domains are and what the functions do away from $p$ is forgotten — which is exactly why shrinking a representative's domain is free.*

> [!example] Example §27.2: Germs Versus Taylor Series
> Take $M = \mathbb{R}^n$ and $x_0 \in \mathbb{R}^n$. All partial derivatives of a function at $x_0$ depend only on its germ, so the Taylor series construction descends to a map into the ring of formal power series,
>
> $$
> \mathcal{T} : C_{x_0}^\infty(\mathbb{R}^n) \longrightarrow \mathbb{R}[\![x^1, \ldots, x^n]\!], \qquad
> \mathcal{T}[f] = \sum_{\alpha} \frac{1}{\alpha!}\, \frac{\partial^{|\alpha|} f}{\partial x^\alpha}(x_0)\, (x - x_0)^\alpha ,
> $$
>
> an $\mathbb{R}$-algebra homomorphism. It is *surjective* but *not injective*.

^ex-27-2

> [!proof]+ Justification
> Four claims: $\mathcal{T}$ is well defined on germs, it is an $\mathbb{R}$-algebra homomorphism, it is surjective, and it is not injective. Write $\alpha! = \alpha_1! \cdots \alpha_n!$ and $\partial^\alpha$ for the partial derivative of multi-index $\alpha$.
>
> *Well defined.* If $f$ and $g$ represent the same germ, they agree on an open $W \ni x_0$. A partial derivative at a point of an open set is a limit of difference quotients that, for small increments, only involve values on that open set; so the first partial derivatives of $f$ and $g$ agree on $W$, and, applying the same to them, by induction on the order all partial derivatives agree on $W$, in particular at $x_0$. Hence the coefficients $\frac{1}{\alpha!}\partial^\alpha f(x_0)$ of $\mathcal{T}[f]$ depend only on $[f]$.
>
> *Homomorphism.* Each $\partial^\alpha$ is linear, so $\mathcal{T}[af + bg] = a\,\mathcal{T}[f] + b\,\mathcal{T}[g]$; and $\mathcal{T}[1] = 1$, since all derivatives of positive order of a constant vanish. For products, the multi-index Leibniz rule (the product rule $\partial_i(fg) = (\partial_i f)g + f\,\partial_i g$ applied repeatedly, by induction on $|\alpha|$) gives
>
> $$
> \partial^\alpha(fg) = \sum_{\beta \le \alpha} \frac{\alpha!}{\beta!\,(\alpha - \beta)!}\, \partial^\beta f\; \partial^{\alpha-\beta} g .
> $$
>
> So the coefficient of $(x - x_0)^\alpha$ in $\mathcal{T}[fg]$ is
>
> $$
> \frac{1}{\alpha!}\,\partial^\alpha(fg)(x_0) = \sum_{\beta + \gamma = \alpha} \frac{\partial^\beta f(x_0)}{\beta!}\cdot\frac{\partial^\gamma g(x_0)}{\gamma!} ,
> $$
>
> which is the coefficient of $(x - x_0)^\alpha$ in the product of formal power series $\mathcal{T}[f]\,\mathcal{T}[g]$, since $(x - x_0)^\beta (x - x_0)^\gamma = (x - x_0)^{\beta+\gamma}$. Hence $\mathcal{T}\big([f][g]\big) = \mathcal{T}[fg] = \mathcal{T}[f]\,\mathcal{T}[g]$.
>
> *Surjective.* Surjectivity is **Borel's theorem**: every formal power series is the Taylor series at $x_0$ of some smooth function. It is cited, not proved — Uribe: “that's not so easy to show, but it's true.”
>
> *Not injective.* Failure of injectivity is elementary. Uribe: “You can have totally flat functions that are not zero”; the example is filled in. The function
>
> $$
> f(x) = \begin{cases} e^{-1/|x-x_0|^2}, & x \neq x_0,\\ 0, & x = x_0,\end{cases}
> $$
>
> is smooth with all partial derivatives vanishing at $x_0$ (a standard computation, written out in the next two paragraphs), so $\mathcal{T}[f] = 0$, every coefficient being a partial derivative at $x_0$. On the other hand $[f] \neq 0$: $f(x) > 0$ for every $x \neq x_0$, and every open $W \ni x_0$ contains points $x \neq x_0$, so $f$ is not $0$ on any neighbourhood of $x_0$, i.e. $(f, \mathbb{R}^n) \not\sim (0, \mathbb{R}^n)$.
>
> *The one-variable function.* Let $h(s) = e^{-1/s}$ for $s > 0$ and $h(s) = 0$ for $s \le 0$. We show by induction on $j$: $h$ is $j$ times differentiable on $\mathbb{R}$, with $h^{(j)}(s) = 0$ for $s \le 0$ and $h^{(j)}(s) = P_j(1/s)\,e^{-1/s}$ for $s > 0$, where $P_j$ is a polynomial. For $j = 0$ take $P_0 = 1$. Assume the claim for $j$. For $s < 0$, $h^{(j)}$ vanishes on the open set $(-\infty, 0)$, so $h^{(j+1)}(s) = 0$. For $s > 0$, by the chain and product rules,
>
> $$
> \frac{d}{ds}\Big(P_j(1/s)\,e^{-1/s}\Big) = -\frac{1}{s^2}P_j'(1/s)\,e^{-1/s} + \frac{1}{s^2}P_j(1/s)\,e^{-1/s} = P_{j+1}(1/s)\,e^{-1/s}, \qquad P_{j+1}(y) = y^2\big(P_j(y) - P_j'(y)\big).
> $$
>
> At $s = 0$: the difference quotient $\big(h^{(j)}(s) - h^{(j)}(0)\big)/s$ is $0$ for $s < 0$, and for $s > 0$ it is
>
> $$
> \frac{P_j(1/s)\,e^{-1/s}}{s} = Q(1/s)\,e^{-1/s}, \qquad Q(y) = y\,P_j(y),
> $$
>
> which tends to $0$ as $s \to 0^+$, because $Q(y)e^{-y} \to 0$ as $y = 1/s \to \infty$ (the exponential grows faster than any polynomial). So $h^{(j+1)}(0) = 0$, completing the induction. Hence $h$ is smooth on $\mathbb{R}$ and $h^{(j)}(0) = 0$ for every $j$.
>
> *Smoothness and flatness of $f$.* Put $q(x) = |x - x_0|^2 = \sum_i (x^i - x_0^i)^2$, a polynomial with $q(x_0) = 0$ and $q(x) > 0$ for $x \neq x_0$. Then $f = h \circ q$: for $x \neq x_0$, $h(q(x)) = e^{-1/|x-x_0|^2}$, and $h(q(x_0)) = h(0) = 0$. So $f$ is smooth, as a composite of smooth maps. By induction on $|\alpha|$, every partial derivative $\partial^\alpha f$ is a finite sum of terms $(h^{(j)} \circ q)\cdot P$ with $P$ a polynomial in $x$: this holds for $\alpha = 0$ ($f = (h \circ q)\cdot 1$), and by the chain and product rules
>
> $$
> \partial_i\big((h^{(j)} \circ q)\, P\big) = (h^{(j+1)} \circ q)\,(\partial_i q)\,P + (h^{(j)} \circ q)\,\partial_i P, \qquad \partial_i q = 2(x^i - x_0^i),
> $$
>
> again of that form. At $x_0$ every term contains a factor $h^{(j)}(q(x_0)) = h^{(j)}(0) = 0$, so $\partial^\alpha f(x_0) = 0$ for every $\alpha$.

^pf-ex-27-2

*Uses:* [[§27 Germs#^def-27-2|Def. §27.2]], [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]

> [!remark]- Connections
> - The one-variable flat function $e^{-1/x^2}$, a smooth function that is not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]; Taylor series: [[§31 Taylor's Theorem#^def-31-1|451 Def. §31.1]].
> - Taylor expansion in several variables: [[Multivariable Taylor's Theorem|452 §11.2 (Multivariable Taylor's Theorem)]].

> [!definition] Definition §27.4: Flat Germ
> A germ $[f] \in C_{x_0}^\infty(\mathbb{R}^n)$ is **flat** if all partial derivatives of $f$, of all orders, vanish at $x_0$; equivalently, $\mathcal{T}[f] = 0$. So the kernel of $\mathcal{T}$ consists exactly of the flat germs.

^def-27-4

> [!remark] Remark
> The moral is that a germ carries strictly more information than its Taylor series — “one of the beauties of being in the $C^\infty$ category.” This is the same phenomenon as the rigidity of $C^\omega$ noted after Definition [[§17 Differentiable Structures#^def-17-5|§17.5]]: a real-analytic germ *is* its Taylor series, which is why there are no analytic bump functions, whereas a $C^\infty$ germ has room to spare.

^rem-27-3
