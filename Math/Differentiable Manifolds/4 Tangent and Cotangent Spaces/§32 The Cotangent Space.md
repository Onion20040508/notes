---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 32
tags: [differentiable-manifolds, math591]
---
← [[§31 Tangent Vectors as Velocities of Curves]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§33 Local Diffeomorphisms]] →

*Stage: abstract, dual — Differentials of functions and the cotangent space: defined as a dual, then recovered from germs alone.*

## Differentials of Functions and the Cotangent Space

*Lecture 10: “a very special case — a very important case.” The target is $N = \mathbb{R}$, and the differential of a scalar function becomes a covector.*

On $\mathbb{R}$ we always use the standard coordinate $r$. For every $c \in \mathbb{R}$ the abstract tangent space $T_c\mathbb{R}$ has the basis $\{\partial/\partial r|_c\}$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]), and we identify $T_c\mathbb{R} \cong \mathbb{R}$ once and for all by $\partial/\partial r|_c \mapsto 1$ — “we identify this with $\mathbb{R}$ forever.”

> [!definition] Definition §32.1: Cotangent Space
> Let $M$ be a smooth manifold and $p \in M$. The **cotangent space** of $M$ at $p$ is the dual of the abstract tangent space,
>
> $$
> T_p^*M = (T_pM)^* .
> $$
>
> *Lee: Ch. 11, Covectors*

^def-32-1

> [!definition] Definition §32.2: The Differential of a Function
> Let $M$ be a smooth manifold and $p \in M$. For a smooth $f : M \to \mathbb{R}$ (or one defined only near $p$), the **differential** of $f$ at $p$ is $df_p = f_{\ast p} : T_pM \to T_{f(p)}\mathbb{R} \cong \mathbb{R}$. Here $T_{f(p)}\mathbb{R}$ is identified with $\mathbb{R}$ by $c\,\partial/\partial r|_{f(p)} \mapsto c$, the derivation $\partial/\partial r|_{f(p)}$ being a basis (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). So $df_p$ takes a tangent vector $D \in T_pM$ and returns a number, $df_p(D) = D[f]$ (Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]]); it is linear, so $df_p \in T_p^{\ast}M$, the cotangent space of [[§32 The Cotangent Space#^def-32-1|Definition §32.1]].
>
> *Lee: Ch. 11, Covectors*

^def-32-2

![[m591-13-1.svg]]
*The differential of a function is its pushforward followed by the permanent identification of every tangent space of $\mathbb{R}$ with $\mathbb{R}$; so $df_p$ is the pushforward $f_{\ast p}$ under another name. The notation $T_p^{\ast}M$ puts the star on the $T$ “to save some ink.”*

> [!remark]- Connections
> - The linear algebra: the dual space is [[§12 Duality#^ladr-3-110|LADR 3.110]].
> - In multivariable calculus: [[§10 The Differential#^def-10-1|452 Def. §10.1]] and [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1 (gradient = differential = 1-form)]].
> - Assembled over all of $M$: the cotangent bundle, [[§46 The Cotangent Bundle#^def-46-1|Def. §46.1]].
> - Used in Relativity: the differential of a scalar field is why its gradient $\partial_\mu\phi$ carries a lower index — [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-5|REL Remark: Why the gradient carries a lower index]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]].

> [!theorem] Proposition §32.1: The Differential Evaluates Derivations
> For every $D \in T_pM$, $\ df_p(D) = D[f]$. In particular $df_p\big(\partial/\partial x^j|_p\big) = \partial f/\partial x^j(p)$ in any chart.
>
> *Lee: Ch. 11, Covectors*

^prop-32-1

> [!proof]+ Proof
> By the universal formula ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]) at $f(p)$ with the coordinate $r$, $f_{*p}D = (f_{*p}D)[r]\,\partial/\partial r|_{f(p)}$, and $(f_{*p}D)[r] = D[r \circ f] = D[f]$. Under the identification, $\partial/\partial r|_{f(p)} \mapsto 1$.

^pf-32-1

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]]

> [!theorem] Lemma §32.2: The Differential in Coordinates
> Let $(x^1, \ldots, x^m)$ be coordinates near $p$, and write $dx^i|_p$ for the differential at $p$ of the coordinate function $x^i$. Then $\{dx^1|_p, \ldots, dx^m|_p\}$ is the dual basis of $\{\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p\}$, so $\dim T_p^*M = m$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), and for every smooth $f$ defined near $p$,
>
> $$
> df_p = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p .
> $$
>
> *Lee: Ch. 11, Covectors*

^lem-32-2

> [!proof]+ Proof
> *(Lecture 10: “it suffices to check the identity on basis vectors.” In lecture the left side came from the matrix of $f_{\ast p}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), a $1 \times m$ row — “remember, gradients are across”, after a student first proposed $m \times 1$ — whose $j$-th entry is $\partial f/\partial x^j(p)$. Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]] gives the same value directly.)* By Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]], $dx^i|_p(\partial/\partial x^j|_p) = \partial x^i/\partial x^j(p) = \partial r^i/\partial r^j = \delta^i_j$, which is the defining property of the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]). Two linear functionals agree if they agree on a basis (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2)), so it suffices to evaluate both sides of the formula on $\partial/\partial x^j|_p$. The left side gives $\partial f/\partial x^j(p)$, again by Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]]; the right side gives $\sum_i \partial f/\partial x^i(p)\,\delta^i_j = \partial f/\partial x^j(p)$.

^pf-32-2

*Uses:* [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]], [[Linear map lemma|LADR 3.4]]

> [!remark]- Connections
> - The dual basis and its coefficients: [[§12 Duality#^ladr-3-112|LADR 3.112]], [[§12 Duality#^ladr-3-114|LADR 3.114]], [[§12 Duality#^ladr-3-116|LADR 3.116]].

> [!theorem] Corollary §32.3: Components of a Covector
> In a chart $(x^1, \ldots, x^m)$ near $p$, every covector $\alpha \in T_p^*M$ is
>
> $$
> \alpha = \sum_{j=1}^m a_j\, dx^j\big|_p, \qquad a_j = \alpha\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) .
> $$
>
> The numbers $a_1, \ldots, a_m$ are the **components** of $\alpha$ in the chart.
>
> *Lee: Ch. 11, Covectors*

^cor-32-3

> [!proof]+ Proof
> *(Lecture 15 recalled the basis $dx^j|_p$ — “a fact that I forgot to mention to remind you” — and read off the components by evaluation.)* By [[§32 The Cotangent Space#^lem-32-2|Lemma §32.2]] the $dx^j|_p$ form the basis of $T_p^{\ast}M$ dual to the $\partial/\partial x^j|_p$, and [[§21 Linear Algebra Toolkit#^prop-21-2|Proposition §21.2]] expands every element of a dual space in the dual basis with the coefficients $\alpha(\partial/\partial x^j|_p)$.

^pf-32-3

*Uses:* [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]

> [!remark]- Connections
> - The same expansion in LADR: [[§12 Duality#^ladr-3-112|LADR 3.112]] (dual basis). The components are what the local trivializations and charts of the cotangent bundle record, [[§46 The Cotangent Bundle#^def-46-4|Def. §46.4]], [[§46 The Cotangent Bundle#^def-46-5|Def. §46.5]].

> [!theorem] Corollary §32.4: Properties of the Differential of a Function
> Let $f, g$ be smooth near $p$ and $a, b \in \mathbb{R}$. Then
>
> $$
> d(af + bg)_p = a\,df_p + b\,dg_p, \qquad d(fg)_p = f(p)\,dg_p + g(p)\,df_p,
> $$
>
> and if $h$ is smooth on an open interval containing the values of $f$ near $p$, then $d(h \circ f)_p = h'(f(p))\,df_p$.
>
> *Lee: Proposition 11.20*

^cor-32-4

> [!proof]+ Proof
> Evaluate at $D \in T_pM$ using Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]]. The first two identities are the linearity and the Leibniz rule of $D$. For the third, $D[h \circ f] = (f_{*p}D)[h]$, and under the identification of Definition [[§32 The Cotangent Space#^def-32-1|§32.1]], $f_{*p}D = df_p(D)\,\partial/\partial r|_{f(p)}$; applying this to $h$ gives $df_p(D)\,h'(f(p))$.

^pf-32-4

*Uses:* [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]]

> [!remark] Remark
> Equivalently, by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] with the coordinate $r$ on the target, the matrix of $f_{*p}$ is the $1 \times m$ row
>
> $$
> \Big( \frac{\partial f}{\partial x^1}(p) \ \ \cdots \ \ \frac{\partial f}{\partial x^m}(p) \Big).
> $$
>
> A student proposed $m \times 1$; it is $1 \times m$ — “gradients go across” — since the target is one-dimensional. The lecture's proof took this route and paused over the shape of the matrix; the version above goes through Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]] instead, which avoids the question.

^rem-32-1

![[m591-13-2.svg]]
*The differential as a covector, for $f(x,y) = y + 0.3x^2$ near $p = (0.8, 0)$. Left: level curves of $f$ at equal spacing $\Delta$, and a tangent vector $v$ at $p$. Right: in $T_pM$, the level lines of the linear functional $df_p$ at the same spacing — the linearization of the curves on the left, straight and parallel. The value $df_p(v)$ counts, in units of $\Delta$, how many lines $v$ crosses: here exactly $2\Delta$, since $v$ ends on the line $df_p = 2\Delta$. On the left, $v$ crosses* approximately *two level curves; the curvature is what the linearization discards.*

> [!remark] Remark: Differential — Not Gradient
> “The standard formula from Calc 3 now has this manifold general interpretation.” The formula $df = \sum \partial f/\partial x^i\,dx^i$ of multivariable calculus is now a statement about covectors: the $dx^i|_p$ are not infinitesimals but the dual basis of the coordinate derivations, the coefficients are numbers, and the dual basis “extracts the components of a vector in the original basis.” What does *not* survive on a manifold is the gradient. A function on $M$ has no gradient *vector* — converting $df_p$ into a vector requires an inner product on $T_pM$, i.e. a Riemannian metric — but it always has its differential $df_p \in T_p^{\ast}M$, and that is where differentials of scalar functions live. Differential forms, later in the term, will be built from covectors, and will pull back as naturally as germs do. Uribe also announced that tangent vectors, written $D$ while thought of as derivations, will soon be written $v$.

^rem-32-2

> [!remark]- Connections
> - The Calc 3 formula and the gradient it replaces: [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1]], [[§10 The Differential#^def-10-1|452 Def. §10.1]].
> - Converting a covector into a vector with an inner product: [[Riesz representation theorem|LADR 6.42]].
> - The same point for normal vectors: [[§35 Regular Submanifolds#^rem-35-1|No Normal Vectors Without a Metric]].

## The Cotangent Space from Germs

*Assignment 3, Problem 3. The cotangent space was defined in Lecture 10 as the dual $(T_pM)^{\ast}$. This subsection shows that it also has a description with no dualizing at all, in terms of germs alone — “as you can see, it has the natural definition $I_p/I_p^2$.” The proof splits into four results: a characterization of $I_p^2$, a basis of the quotient, a non-degenerate pairing, and the isomorphism, which then comes from the [[§21 Linear Algebra Toolkit#^thm-21-5|Linear Algebra Toolkit]] for free.*

> [!definition] Definition §32.3: The Space $I_p/I_p^2$
> $I_p/I_p^2$ is the quotient vector space (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]) of $I_p$ by its subspace $I_p^2$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-1|§28.1]]). The class of $[f] \in I_p$ is written ${[}[f]{]} = [f] + I_p^2$, and ${[}[f]{]} = {[}[f']{]}$ iff $[f'] - [f] \in I_p^2$.

^def-32-3

> [!remark]- Connections
> - The quotient space construction: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].

> [!theorem] Proposition §32.5: Germs Vanishing to Second Order
> For $[f] \in C_p^\infty(M)$ the following are equivalent:
> 1. $[f] \in I_p^2$;
> 2. $f(p) = 0$ and $df_p = 0$;
> 3. $f(p) = 0$ and $\partial f/\partial x^i(p) = 0$ for all $i$, in one — hence every — chart at $p$.
>
> *Lee: Problem 11-4(a)*

^prop-32-5

> [!proof]+ Proof
> (2)$\iff$(3): by Lemma [[§32 The Cotangent Space#^lem-32-2|§32.2]], $df_p = \sum_i \partial f/\partial x^i(p)\,dx^i|_p$, and the $dx^i|_p$ form a basis. Condition (2) mentions no chart, which is why “one” chart implies “every”.
>
> (1)$\Rightarrow$(2): every element of $I_p^2$ lies in $I_p$, so it vanishes at $p$. And for $[u], [w] \in I_p$ and any $D \in T_pM$, Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]] and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2) give $d(uw)_p(D) = D([u][w]) = 0$. So $d(uw)_p = 0$, and by linearity $df_p = 0$ for every $[f] \in I_p^2$.
>
> (3)$\Rightarrow$(1): *(Assignment 3, Problem 3.)* Fix a chart $(U,\varphi)$ at $p$, a representative $f : V \to \mathbb{R}$, and put $a = \varphi(p)$ and $f_\varphi = f \circ \varphi^{-1}$. The hypotheses say $f_\varphi(a) = 0$ and $\partial f_\varphi/\partial r^i(a) = 0$. On an open ball $B \subseteq \varphi(U \cap V)$ centred at $a$, Hadamard's lemma (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2|§29.2]]) gives smooth $f_i$ with
>
> $$
> f_\varphi(r) = \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f_\varphi}{\partial r^i}(a) = 0 .
> $$
>
> On the open neighbourhood $W = \varphi^{-1}(B)$ of $p$, with $r = \varphi(q)$ and $r^i = x^i(q)$, this reads
>
> $$
> f(q) = \sum_{i=1}^n \big(x^i(q) - x^i(p)\big)\,(f_i \circ \varphi)(q) \qquad (q \in W),
> $$
>
> an identity of germs: $[f] = \sum_i [x^i - x^i(p)]\,[f_i \circ \varphi]$. Both factors of each term vanish at $p$ — the second because $f_i(a) = 0$ — so each term is a product of two elements of $I_p$, and $[f] \in I_p^2$.

^pf-32-5

*Uses:* [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-2|§29.2]]

> [!remark] Remark
> The proposition is the conceptual centre of Problem 3. $I_p$ consists of the germs vanishing to *first* order at $p$, and $I_p^2$ of those vanishing to *second* order — value and first derivatives zero. So the quotient $I_p/I_p^2$ remembers exactly the first derivatives of a germ that vanishes at $p$, and nothing else. It only needs first-order Hadamard: the vanishing of $f_i(a)$ is what puts the second factor in $I_p$.

^rem-32-3

![[m591-13-4.svg]]
*Classes in $I_p/I_p^2$, for $M = \mathbb{R}$. The blue germs $f_1$ and $f_2$ both vanish at $p$ with the same slope $c$, so $f_1 - f_2$ vanishes to second order and ${[}[f_1]{]} = {[}[f_2]{]} = c\,{[}[x - p]{]}$: the class keeps only the red tangent line and forgets the curvature. The green $g$ has value and slope zero at $p$, so $[g] \in I_p^2$ and ${[}[g]{]} = 0$ (Proposition [[§32 The Cotangent Space#^prop-32-5|§32.5]]).*

> [!theorem] Proposition §32.6: A Basis of $I_p/I_p^2$
> Let $(U, \varphi)$ be a chart at $p$ with coordinate functions $x^1, \ldots, x^n$. For every $[f] \in I_p$,
>
> $$
> {[}[f]{]} = \sum_{i=1}^n \frac{\partial f}{\partial x^i}(p)\, {[}[x^i - x^i(p)]{]},
> $$
>
> and the classes ${[}[x^1 - x^1(p)]{]}, \ldots, {[}[x^n - x^n(p)]{]}$ form a basis of $I_p/I_p^2$. In particular $\dim I_p/I_p^2 = n$.
>
> *Lee: cf. Problem 11-4(a)*

^prop-32-6

> [!proof]+ Proof
> Each $x^i - x^i(p)$ is smooth on $U$ and vanishes at $p$, so its germ lies in $I_p$. Put $g = f - \sum_i \partial f/\partial x^i(p)\,(x^i - x^i(p))$ near $p$. Then $g(p) = 0$ and, using $\partial x^i/\partial x^j = \delta^i_j$,
>
> $$
> \frac{\partial g}{\partial x^j}(p) = \frac{\partial f}{\partial x^j}(p) - \sum_i \frac{\partial f}{\partial x^i}(p)\,\delta^i_j = 0,
> $$
>
> so $[g] \in I_p^2$ by Proposition [[§32 The Cotangent Space#^prop-32-5|§32.5]]. This is the displayed expansion, which shows that the classes span. For independence, suppose $\sum_i c_i\,{[}[x^i - x^i(p)]{]} = 0$, i.e. $\sum_i c_i\,[x^i - x^i(p)] \in I_p^2$. By Proposition [[§32 The Cotangent Space#^prop-32-5|§32.5]] its $j$-th partial at $p$ vanishes, and that partial is $c_j$.

^pf-32-6

*Uses:* [[§32 The Cotangent Space#^prop-32-5|§32.5]], [[§32 The Cotangent Space#^def-32-3|Def. §32.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]]

This is the cotangent counterpart of the basis theorem for $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]): the coefficients of ${[}[f]{]}$ are the first partials of $f$, just as the coefficients of a derivation $D$ were its values $D[x^i]$.

> [!definition] Definition §32.4: The Pairing Between Tangent Vectors and $I_p/I_p^2$
> The **pairing** of $T_pM$ with $I_p/I_p^2$ is
>
> $$
> \langle\ ,\ \rangle : T_pM \times I_p/I_p^2 \to \mathbb{R}, \qquad \langle D, {[}[f]{]} \rangle = D[f] .
> $$

^def-32-4

> [!theorem] Proposition §32.7: The Pairing Is Well Defined and Non-Degenerate
> The pairing of Definition [[§32 The Cotangent Space#^def-32-4|§32.4]] is well defined, bilinear, and non-degenerate in the sense of Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]].
>
> *Lee: no counterpart; Lee proves Problem 11-4(b) without a pairing*

^prop-32-7

> [!proof]+ Proof
> *Well defined* *(Problem 3(a))*. Each $D$ is a linear functional on $I_p$ that vanishes on $I_p^2$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2)), so it descends to $I_p/I_p^2$ by the universal property of quotient spaces (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](2)). *Bilinear:* derivations are linear, and they are added and scaled pointwise.
>
> *Left non-degenerate.* If $D[f] = 0$ for every $[f] \in I_p$, then $D = 0$, because a derivation is determined by its values on $I_p$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)).
>
> *Right non-degenerate.* If $[f] \in I_p$ and $D[f] = 0$ for every $D \in T_pM$, then $df_p = 0$ by Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]]; with $f(p) = 0$, Proposition [[§32 The Cotangent Space#^prop-32-5|§32.5]] gives $[f] \in I_p^2$, i.e. ${[}[f]{]} = 0$.

^pf-32-7

*Uses:* [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§21 Linear Algebra Toolkit#^def-21-5|Def. §21.5]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§32 The Cotangent Space#^prop-32-5|§32.5]]

> [!theorem] Theorem §32.8: The Cotangent Space from Germs
> 1. The pairing induces isomorphisms
>
>    $$
>    T_pM \xrightarrow{\ \cong\ } \big(I_p/I_p^2\big)^*, \qquad\qquad \Phi : I_p/I_p^2 \xrightarrow{\ \cong\ } (T_pM)^* = T_p^*M .
>    $$
>
> 2. $\Phi({[}[f]{]}) = df_p$: the isomorphism sends the class of a germ to its differential.
> 3. In any chart, $\Phi$ carries the basis ${[}[x^i - x^i(p)]{]}$ of $I_p/I_p^2$ to the basis $dx^i|_p$ of $T_p^*M$, which is dual to the basis $\partial/\partial x^i|_p$ of $T_pM$.
>
> The isomorphisms are defined without any chart.
>
> *Lee: Problem 11-4(b), with global functions in place of germs (see the comparison below)*

^thm-32-8

> [!proof]+ Proof
> (1) $T_pM$ is finite-dimensional (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]) and the pairing is non-degenerate (Proposition [[§32 The Cotangent Space#^prop-32-7|§32.7]]), so Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]] applies. (2) $\Phi({[}[f]{]})(D) = \langle D, {[}[f]{]} \rangle = D[f] = df_p(D)$ by Proposition [[§32 The Cotangent Space#^prop-32-1|§32.1]]. (3) By (2), $\Phi({[}[x^i - x^i(p)]{]}) = d(x^i - x^i(p))_p = dx^i|_p$, since a constant has zero differential (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)); and the $dx^i|_p$ are dual to the $\partial/\partial x^i|_p$ by Lemma [[§32 The Cotangent Space#^lem-32-2|§32.2]]. Every map in (1) is defined by $\langle D, {[}[f]{]} \rangle = D[f]$, which mentions no chart.

^pf-32-8

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§32 The Cotangent Space#^prop-32-7|§32.7]], [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]], [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§32 The Cotangent Space#^def-32-4|Def. §32.4]]

![[m591-13-3.svg]]
*The three spaces and their three bases. $\Phi$ sends the class of a germ to its differential, so the coordinate classes go to the coordinate covectors, and those are the dual basis of the coordinate derivations. Uribe's $dx^i|_p$ of Lecture 10 and the classes ${[}[x^i - x^i(p)]{]}$ of Problem 3 are the same objects, seen through $\Phi$.*

> [!remark] Remark: The Most Natural Description
> Lecture 15 came back to this theorem: “the cotangent space is, in a way, very extremely natural from the point of view of functions.” The tangent space needed derivations; the cotangent space needs only functions — germs vanishing at $p$, modulo those vanishing to second order. This is one reason why the cotangent bundle will turn out to carry structure that the tangent bundle does not.

^rem-32-4

> [!theorem] Theorem §32.9: Dimension of the Cotangent Space
> Let $M$ be a smooth $m$-manifold and $p \in M$. Then
>
> $$
> \dim T_p^{\ast}M \;=\; \dim \big(I_p/I_p^2\big) \;=\; \dim T_pM \;=\; m .
> $$
>
> The cotangent space ([[§32 The Cotangent Space#^def-32-1|Def. §32.1]]) has the same dimension as the tangent space, at every point.

^thm-32-9

> [!proof]+ Proof
> *(Collected from the results above; not stated as a single theorem in lecture.)* $T_p^{\ast}M = (T_pM)^{\ast}$ is the dual of a space of dimension $m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]), and the dual of a finite-dimensional space has the same dimension (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]); explicitly, the $m$ covectors $dx^i|_p$ form a basis (Lemma [[§32 The Cotangent Space#^lem-32-2|§32.2]]). And $I_p/I_p^2$ has the basis of $m$ classes ${[}[x^i - x^i(p)]{]}$ (Proposition [[§32 The Cotangent Space#^prop-32-6|§32.6]]), or equivalently is isomorphic to $T_p^{\ast}M$ by $\Phi$ (Theorem [[§32 The Cotangent Space#^thm-32-8|§32.8]]).

^pf-32-9

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§32 The Cotangent Space#^prop-32-6|§32.6]], [[§32 The Cotangent Space#^thm-32-8|§32.8]]

Equal dimension is what makes the isomorphisms of Theorem [[§32 The Cotangent Space#^thm-32-8|§32.8]] possible, but the dimension count alone does not produce them: any two spaces of dimension $m$ are isomorphic, by choosing bases. What Theorem [[§32 The Cotangent Space#^thm-32-8|§32.8]] adds is that $\Phi$ needs no choice. Between $T_pM$ and $T_p^{\ast}M$ themselves there is no such choice-free isomorphism, which is why the tangent and cotangent bundles are isomorphic “but not naturally” ([[§46 The Cotangent Bundle|§46]]).

**Assignment 3, Problem 3.** Part (a) is the well-definedness in Proposition [[§32 The Cotangent Space#^prop-32-7|§32.7]]. Part (b) is its non-degeneracy, and the “therefore” of (b) is Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]], which uses *both* halves: right non-degeneracy bounds $\dim I_p/I_p^2 \le n$, left non-degeneracy gives $n \le \dim I_p/I_p^2$. The submitted solution reaches the isomorphism by another route: it shows $\Phi$ injective by right non-degeneracy and surjective by checking that $\Phi({[}[x^i - x^i(p)]{]})$ is the dual basis — which is part (3) of the theorem.

**Comparison with Lee.** In the text of Chapter 11, Lee defines the cotangent space as the dual $(T_pM)^{\ast}$, motivated as the coordinate-independent replacement for the gradient. The description of this subsection is his Problem 11-4. Part (a) is Proposition [[§32 The Cotangent Space#^prop-32-5|§32.5]], down to the phrase “vanishes to second order”, and part (b) is Theorem [[§32 The Cotangent Space#^thm-32-8|§32.8]](1)–(2). There are two differences. First, Lee's $I_p$ consists of smooth functions on all of $M$ vanishing at $p$, not germs, so his version needs bump functions to pass between local and global, as everywhere in his treatment (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]]). Second, Lee proves the isomorphism directly, showing that $f \mapsto df_p$ vanishes on $I_p^2$ and descends to the quotient, where Assignment 3 goes through a non-degenerate pairing and the pairing theorem. His remark to the problem adds two points: some treatments define $T_p^{\ast}M$ first, as $I_p/I_p^2$, and then $T_pM$ as its dual — the order Uribe called in some ways more natural — and covectors, as classes of functions $M \to \mathbb{R}$, are dual to tangent vectors as classes of curves $\mathbb{R} \to M$ (his Problem 3-8; here Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]). The quotient $I_p/I_p^2$ is also the manifold analogue of the Zariski cotangent space of algebraic geometry.

## Pulling Back Covectors

*Lecture 15. A smooth map pushes tangent vectors forward; dually, it pulls covectors back. “Functions pull back by composition, and you can pull back actually any one-form by using the dual map of the forward star.”*

> [!definition] Definition §32.5: Pullback of Covectors
> Let $F : M \to N$ be smooth and $p \in M$. The **pullback of covectors** at $p$ is the dual map ([[§21 Linear Algebra Toolkit#^def-21-3|Definition §21.3]]) of the pushforward $F_{\ast p} : T_pM \to T_{F(p)}N$:
>
> $$
> F_p^* : T^*_{F(p)}N \longrightarrow T_p^*M, \qquad (F_p^*\alpha)(v) = \alpha\big(F_{*p}v\big) .
> $$
>
> *Lee: Ch. 11, Pullbacks of Covector Fields*

^def-32-5

> [!remark]- Connections
> - The dual map in LADR: [[§12 Duality#^ladr-3-118|LADR 3.118]]. The field version, pulling back a one-form point by point: [[§47 One-Forms#^def-47-4|Def. §47.4]].

Directions: points and vectors move *forward* along $F$, from $M$ to $N$; functions and covectors move *backward*, from $N$ to $M$, because they are things that eat — to evaluate one on $M$, push the input to $N$ and evaluate there.

> [!remark] Remark: One Symbol for Two Pullbacks
> The symbol $F_p^{\ast}$ now has two meanings. On germs it is the pullback $C^\infty_{F(p)}(N) \to C^\infty_p(M)$, $[g] \mapsto [g \circ F]$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5]]); on covectors it is the dual map $T^{\ast}_{F(p)}N \to T_p^{\ast}M$ of [[§32 The Cotangent Space#^def-32-5|Definition §32.5]]. Context decides which is meant, and the two are compatible: by the next proposition, pulling back the differential of $g$ is the same as differentiating the pulled-back germ, $F_p^{\ast}(dg_{F(p)}) = d\big(F_p^{\ast}[g]\big)_p$.

^rem-32-5

> [!theorem] Proposition §32.10: Pullback Commutes with $d$
> Let $F : M \to N$ be smooth, $p \in M$, and $f$ smooth near $F(p)$. Then
>
> $$
> F_p^*\big(df_{F(p)}\big) = d(f \circ F)_p \quad \text{in } T_p^*M .
> $$
>
> *Lee: Proposition 11.25*

^prop-32-10

> [!proof]+ Proof
> *(Lecture 15 — “every equal sign is a definition … maybe this is best to be reflected upon at your coffee shop of choice.”)* For $v \in T_pM$:
>
> $$
> F_p^*\big(df_{F(p)}\big)(v) = df_{F(p)}\big(F_{*p}v\big) = \big(F_{*p}v\big)[f] = v[f \circ F] = d(f \circ F)_p(v) .
> $$
>
> The first equality is the definition of the dual map; the second, of the differential of a function, applied to the vector $F_{\ast p}v \in T_{F(p)}N$; the third, of the pushforward; the fourth, of the differential of $f \circ F$. Two covectors that agree on every $v$ are equal.

^pf-32-10

*Uses:* [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§32 The Cotangent Space#^prop-32-1|§32.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§21 Linear Algebra Toolkit#^def-21-3|Def. §21.3]]

> [!remark] Remark: The Two Differentials Meet
> In $\mathbb{R}^n$, with the dot-product identification of [[§32 The Cotangent Space#^rem-32-2|Remark (Differential — Not Gradient)]], the proposition is the chain rule in the form $\nabla(f \circ F) = J_F^{\mathsf T}\, \nabla f$. Uribe added that the pushforward $F_{\ast}$ “we should have called the differential of $F$ ages ago”: for a function $f : M \to \mathbb{R}$, $df_p$ is $f_{\ast p}$ followed by the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$.

^rem-32-6

> [!remark]- Connections
> - The chain rule in 452: [[Multivariable Chain Rule]]. Pullback of forms on $\mathbb{R}^n$ commuting with $d$ in 452: [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]. The field version: [[§47 One-Forms#^cor-47-4|Cor. §47.4]].
