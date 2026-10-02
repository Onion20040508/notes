---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 27
tags: [differentiable-manifolds, math591]
---
← [[§26 Tangent Vectors as Velocities of Curves]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§28 Local Diffeomorphisms and Submersions]] →

*Stage: abstract, dual — Differentials of functions and the cotangent space: defined as a dual, then recovered from germs alone.*

## Differentials of Functions and the Cotangent Space

*Lecture 10: “a very special case — a very important case.” The target is $N = \mathbb{R}$, and the differential of a scalar function becomes a covector.*

On $\mathbb{R}$ we always use the standard coordinate $r$. For every $c \in \mathbb{R}$ the abstract tangent space $T_c\mathbb{R}$ has the basis $\{\partial/\partial r|_c\}$ (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]), and we identify $T_c\mathbb{R} \cong \mathbb{R}$ once and for all by $\partial/\partial r|_c \mapsto 1$ — “we identify this with $\mathbb{R}$ forever.”

> [!definition] Definition §27.1: Cotangent Space and the Differential of a Function
> Let $M$ be a smooth manifold and $p \in M$. The **cotangent space** of $M$ at $p$ is the dual of the abstract tangent space,
>
> $$
> T_p^*M = (T_pM)^* .
> $$
>
> For a smooth $f : M \to \mathbb{R}$ (or one defined only near $p$), the **differential** of $f$ at $p$ is $df_p = f_{*p} : T_pM \to T_{f(p)}\mathbb{R} \cong \mathbb{R}$. Here $T_{f(p)}\mathbb{R}$ is identified with $\mathbb{R}$ by $c\,\partial/\partial r|_{f(p)} \mapsto c$, the derivation $\partial/\partial r|_{f(p)}$ being a basis (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]). So $df_p$ takes a tangent vector $D \in T_pM$ and returns a number, $df_p(D) = D[f]$ (Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]]); it is linear, so $df_p \in T_p^*M$.
>
> *Lee: Ch. 11, Covectors*

^def-27-1

![[m591-13-1.svg]]
*The differential of a function is its pushforward followed by the permanent identification of every tangent space of $\mathbb{R}$ with $\mathbb{R}$; so $df_p$ is the pushforward $f_{*p}$ under another name. The notation $T_p^*M$ puts the star on the $T$ “to save some ink.”*

> [!remark]- Connections
> - The linear algebra: the dual space is [[§12 Duality#^ladr-3-110|LADR 3.110]].
> - In multivariable calculus: [[§8 The Differential#^def-8-1|452 Def. §8.1]] and [[§22 The Algebra of Differential Forms#^prop-22-6|452 §22.6 (gradient = differential = 1-form)]].
> - Assembled over all of $M$: the cotangent bundle, [[§31 The Tangent Bundle#^def-31-5|Def. §31.5]].
> - Used in Relativity: the differential of a scalar field is why its gradient $\partial_\mu\phi$ carries a lower index — [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-5|REL Remark: Why the gradient carries a lower index]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]].

> [!theorem] Proposition §27.1: The Differential Evaluates Derivations
> For every $D \in T_pM$, $\ df_p(D) = D[f]$. In particular $df_p\big(\partial/\partial x^j|_p\big) = \partial f/\partial x^j(p)$ in any chart.
>
> *Lee: Ch. 11, Covectors*

^prop-27-1

> [!proof]+ Proof
> By the universal formula ([[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]) at $f(p)$ with the coordinate $r$, $f_{*p}D = (f_{*p}D)[r]\,\partial/\partial r|_{f(p)}$, and $(f_{*p}D)[r] = D[r \circ f] = D[f]$. Under the identification, $\partial/\partial r|_{f(p)} \mapsto 1$.

^pf-27-1

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]], [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Def. §23.5]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|Def. §27.1]]

> [!theorem] Lemma §27.2: The Differential in Coordinates
> Let $(x^1, \ldots, x^m)$ be coordinates near $p$, and write $dx^i|_p$ for the differential at $p$ of the coordinate function $x^i$. Then $\{dx^1|_p, \ldots, dx^m|_p\}$ is the dual basis of $\{\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p\}$, so $\dim T_p^*M = m$ (Proposition [[§17 Linear Algebra Toolkit#^prop-17-2|§17.2]]), and for every smooth $f$ defined near $p$,
>
> $$
> df_p = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p .
> $$
>
> *Lee: Ch. 11, Covectors*

^lem-27-2

> [!proof]+ Proof
> *(Lecture 10: “it suffices to check the identity on basis vectors.” In lecture the left side came from the matrix of $f_{*p}$ (Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]]), a $1 \times m$ row — “remember, gradients are across”, after a student first proposed $m \times 1$ — whose $j$-th entry is $\partial f/\partial x^j(p)$. Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]] gives the same value directly.)* By Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], $dx^i|_p(\partial/\partial x^j|_p) = \partial x^i/\partial x^j(p) = \partial r^i/\partial r^j = \delta^i_j$, which is the defining property of the dual basis (Definition [[§17 Linear Algebra Toolkit#^def-17-1|§17.1]]). Two linear functionals agree if they agree on a basis (Proposition [[§17 Linear Algebra Toolkit#^prop-17-1|§17.1]](2)), so it suffices to evaluate both sides of the formula on $\partial/\partial x^j|_p$. The left side gives $\partial f/\partial x^j(p)$, again by Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]]; the right side gives $\sum_i \partial f/\partial x^i(p)\,\delta^i_j = \partial f/\partial x^j(p)$.

^pf-27-2

*Uses:* [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], [[§17 Linear Algebra Toolkit#^def-17-1|Def. §17.1]], [[§17 Linear Algebra Toolkit#^prop-17-1|§17.1]], [[§17 Linear Algebra Toolkit#^prop-17-2|§17.2]], [[§25 The Differential in Coordinates#^thm-25-2|§25.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]], [[Linear map lemma|LADR 3.4]]

> [!remark]- Connections
> - The dual basis and its coefficients: [[§12 Duality#^ladr-3-112|LADR 3.112]], [[§12 Duality#^ladr-3-114|LADR 3.114]], [[§12 Duality#^ladr-3-116|LADR 3.116]].

> [!theorem] Corollary §27.3: Properties of the Differential of a Function
> Let $f, g$ be smooth near $p$ and $a, b \in \mathbb{R}$. Then
>
> $$
> d(af + bg)_p = a\,df_p + b\,dg_p, \qquad d(fg)_p = f(p)\,dg_p + g(p)\,df_p,
> $$
>
> and if $h$ is smooth on an open interval containing the values of $f$ near $p$, then $d(h \circ f)_p = h'(f(p))\,df_p$.
>
> *Lee: Proposition 11.20*

^cor-27-3

> [!proof]+ Proof
> Evaluate at $D \in T_pM$ using Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]]. The first two identities are the linearity and the Leibniz rule of $D$. For the third, $D[h \circ f] = (f_{*p}D)[h]$, and under the identification of Definition [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|§27.1]], $f_{*p}D = df_p(D)\,\partial/\partial r|_{f(p)}$; applying this to $h$ gives $df_p(D)\,h'(f(p))$.

^pf-27-3

*Uses:* [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Def. §23.5]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|Def. §27.1]]

> [!remark] Remark
> Equivalently, by Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]] with the coordinate $r$ on the target, the matrix of $f_{*p}$ is the $1 \times m$ row
>
> $$
> \Big( \frac{\partial f}{\partial x^1}(p) \ \ \cdots \ \ \frac{\partial f}{\partial x^m}(p) \Big).
> $$
>
> A student proposed $m \times 1$; it is $1 \times m$ — “gradients go across” — since the target is one-dimensional. The lecture's proof took this route and paused over the shape of the matrix; the version above goes through Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]] instead, which avoids the question.

^rem-27-1

![[m591-13-2.svg]]
*The differential as a covector, for $f(x,y) = y + 0.3x^2$ near $p = (0.8, 0)$. Left: level curves of $f$ at equal spacing $\Delta$, and a tangent vector $v$ at $p$. Right: in $T_pM$, the level lines of the linear functional $df_p$ at the same spacing — the linearization of the curves on the left, straight and parallel. The value $df_p(v)$ counts, in units of $\Delta$, how many lines $v$ crosses: here exactly $2\Delta$, since $v$ ends on the line $df_p = 2\Delta$. On the left, $v$ crosses* approximately *two level curves; the curvature is what the linearization discards.*

> [!remark] Remark: Differential — Not Gradient
> “The standard formula from Calc 3 now has this manifold general interpretation.” The formula $df = \sum \partial f/\partial x^i\,dx^i$ of multivariable calculus is now a statement about covectors: the $dx^i|_p$ are not infinitesimals but the dual basis of the coordinate derivations, the coefficients are numbers, and the dual basis “extracts the components of a vector in the original basis.” What does *not* survive on a manifold is the gradient. A function on $M$ has no gradient *vector* — converting $df_p$ into a vector requires an inner product on $T_pM$, i.e. a Riemannian metric — but it always has its differential $df_p \in T_p^*M$, and that is where differentials of scalar functions live. Differential forms, later in the term, will be built from covectors, and will pull back as naturally as germs do. Uribe also announced that tangent vectors, written $D$ while thought of as derivations, will soon be written $v$.

^rem-27-2

> [!remark]- Connections
> - The Calc 3 formula and the gradient it replaces: [[§22 The Algebra of Differential Forms#^prop-22-6|452 §22.6]], [[§8 The Differential#^def-8-1|452 Def. §8.1]].
> - Converting a covector into a vector with an inner product: [[Riesz representation theorem|LADR 6.42]].
> - The same point for normal vectors: [[§29 Submanifolds#^rem-29-1|No Normal Vectors Without a Metric]].

## The Cotangent Space from Germs

*Assignment 3, Problem 3. The cotangent space was defined in Lecture 10 as the dual $(T_pM)^*$. This subsection shows that it also has a description with no dualizing at all, in terms of germs alone — “as you can see, it has the natural definition $I_p/I_p^2$.” The proof splits into four results: a characterization of $I_p^2$, a basis of the quotient, a non-degenerate pairing, and the isomorphism, which then comes from the [[§17 Linear Algebra Toolkit#^thm-17-5|Linear Algebra Toolkit]] for free.*

> [!definition] Definition §27.2: The Space $I_p/I_p^2$
> $I_p/I_p^2$ is the quotient vector space (Definition [[§17 Linear Algebra Toolkit#^def-17-4|§17.4]]) of $I_p$ by its subspace $I_p^2$ (Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-1|§23.1]]). The class of $[f] \in I_p$ is written ${[}[f]{]} = [f] + I_p^2$, and ${[}[f]{]} = {[}[f']{]}$ iff $[f'] - [f] \in I_p^2$.

^def-27-2

> [!remark]- Connections
> - The quotient space construction: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].

> [!theorem] Proposition §27.4: Germs Vanishing to Second Order
> For $[f] \in C_p^\infty(M)$ the following are equivalent:
> 1. $[f] \in I_p^2$;
> 2. $f(p) = 0$ and $df_p = 0$;
> 3. $f(p) = 0$ and $\partial f/\partial x^i(p) = 0$ for all $i$, in one — hence every — chart at $p$.
>
> *Lee: Problem 11-4(a)*

^prop-27-4

> [!proof]+ Proof
> (2)$\iff$(3): by Lemma [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]], $df_p = \sum_i \partial f/\partial x^i(p)\,dx^i|_p$, and the $dx^i|_p$ form a basis. Condition (2) mentions no chart, which is why “one” chart implies “every”.
>
> (1)$\Rightarrow$(2): every element of $I_p^2$ lies in $I_p$, so it vanishes at $p$. And for $[u], [w] \in I_p$ and any $D \in T_pM$, Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]] and Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](2) give $d(uw)_p(D) = D([u][w]) = 0$. So $d(uw)_p = 0$, and by linearity $df_p = 0$ for every $[f] \in I_p^2$.
>
> (3)$\Rightarrow$(1): *(Assignment 3, Problem 3.)* Fix a chart $(U,\varphi)$ at $p$, a representative $f : V \to \mathbb{R}$, and put $a = \varphi(p)$ and $f_\varphi = f \circ \varphi^{-1}$. The hypotheses say $f_\varphi(a) = 0$ and $\partial f_\varphi/\partial r^i(a) = 0$. On an open ball $B \subseteq \varphi(U \cap V)$ centred at $a$, Hadamard's lemma (Lemma [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]]) gives smooth $f_i$ with
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

^pf-27-4

*Uses:* [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], [[§23 Derivations and the Abstract Tangent Space#^def-23-3|Def. §23.3]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]], [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]]

> [!remark] Remark
> The proposition is the conceptual centre of Problem 3. $I_p$ consists of the germs vanishing to *first* order at $p$, and $I_p^2$ of those vanishing to *second* order — value and first derivatives zero. So the quotient $I_p/I_p^2$ remembers exactly the first derivatives of a germ that vanishes at $p$, and nothing else. It only needs first-order Hadamard: the vanishing of $f_i(a)$ is what puts the second factor in $I_p$.

^rem-27-3

![[m591-13-4.svg]]
*Classes in $I_p/I_p^2$, for $M = \mathbb{R}$. The blue germs $f_1$ and $f_2$ both vanish at $p$ with the same slope $c$, so $f_1 - f_2$ vanishes to second order and ${[}[f_1]{]} = {[}[f_2]{]} = c\,{[}[x - p]{]}$: the class keeps only the red tangent line and forgets the curvature. The green $g$ has value and slope zero at $p$, so $[g] \in I_p^2$ and ${[}[g]{]} = 0$ (Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]]).*

> [!theorem] Proposition §27.5: A Basis of $I_p/I_p^2$
> Let $(U, \varphi)$ be a chart at $p$ with coordinate functions $x^1, \ldots, x^n$. For every $[f] \in I_p$,
>
> $$
> {[}[f]{]} = \sum_{i=1}^n \frac{\partial f}{\partial x^i}(p)\, {[}[x^i - x^i(p)]{]},
> $$
>
> and the classes ${[}[x^1 - x^1(p)]{]}, \ldots, {[}[x^n - x^n(p)]{]}$ form a basis of $I_p/I_p^2$. In particular $\dim I_p/I_p^2 = n$.
>
> *Lee: cf. Problem 11-4(a)*

^prop-27-5

> [!proof]+ Proof
> Each $x^i - x^i(p)$ is smooth on $U$ and vanishes at $p$, so its germ lies in $I_p$. Put $g = f - \sum_i \partial f/\partial x^i(p)\,(x^i - x^i(p))$ near $p$. Then $g(p) = 0$ and, using $\partial x^i/\partial x^j = \delta^i_j$,
>
> $$
> \frac{\partial g}{\partial x^j}(p) = \frac{\partial f}{\partial x^j}(p) - \sum_i \frac{\partial f}{\partial x^i}(p)\,\delta^i_j = 0,
> $$
>
> so $[g] \in I_p^2$ by Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]]. This is the displayed expansion, which shows that the classes span. For independence, suppose $\sum_i c_i\,{[}[x^i - x^i(p)]{]} = 0$, i.e. $\sum_i c_i\,[x^i - x^i(p)] \in I_p^2$. By Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]] its $j$-th partial at $p$ vanishes, and that partial is $c_j$.

^pf-27-5

*Uses:* [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-2|Def. §27.2]], [[§23 Derivations and the Abstract Tangent Space#^def-23-3|Def. §23.3]]

This is the cotangent counterpart of the basis theorem for $T_pM$ (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]): the coefficients of ${[}[f]{]}$ are the first partials of $f$, just as the coefficients of a derivation $D$ were its values $D[x^i]$.

> [!definition] Definition §27.3: The Pairing Between Tangent Vectors and $I_p/I_p^2$
> The **pairing** of $T_pM$ with $I_p/I_p^2$ is
>
> $$
> \langle\ ,\ \rangle : T_pM \times I_p/I_p^2 \to \mathbb{R}, \qquad \langle D, {[}[f]{]} \rangle = D[f] .
> $$

^def-27-3

> [!theorem] Proposition §27.6: The Pairing Is Well Defined and Non-Degenerate
> The pairing of Definition [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-3|§27.3]] is well defined, bilinear, and non-degenerate in the sense of Definition [[§17 Linear Algebra Toolkit#^def-17-3|§17.3]].
>
> *Lee: no counterpart; Lee proves Problem 11-4(b) without a pairing*

^prop-27-6

> [!proof]+ Proof
> *Well defined* *(Problem 3(a))*. Each $D$ is a linear functional on $I_p$ that vanishes on $I_p^2$ (Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](2)), so it descends to $I_p/I_p^2$ by the universal property of quotient spaces (Proposition [[§17 Linear Algebra Toolkit#^prop-17-6|§17.6]](2)). *Bilinear:* derivations are linear, and they are added and scaled pointwise.
>
> *Left non-degenerate.* If $D[f] = 0$ for every $[f] \in I_p$, then $D = 0$, because a derivation is determined by its values on $I_p$ (Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](1)).
>
> *Right non-degenerate.* If $[f] \in I_p$ and $D[f] = 0$ for every $D \in T_pM$, then $df_p = 0$ by Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]]; with $f(p) = 0$, Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]] gives $[f] \in I_p^2$, i.e. ${[}[f]{]} = 0$.

^pf-27-6

*Uses:* [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-3|Def. §27.3]], [[§17 Linear Algebra Toolkit#^def-17-3|Def. §17.3]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]], [[§17 Linear Algebra Toolkit#^prop-17-6|§17.6]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]]

> [!theorem] Theorem §27.7: The Cotangent Space from Germs
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

^thm-27-7

> [!proof]+ Proof
> (1) $T_pM$ is finite-dimensional (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]) and the pairing is non-degenerate (Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|§27.6]]), so Theorem [[§17 Linear Algebra Toolkit#^thm-17-5|§17.5]] applies. (2) $\Phi({[}[f]{]})(D) = \langle D, {[}[f]{]} \rangle = D[f] = df_p(D)$ by Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]]. (3) By (2), $\Phi({[}[x^i - x^i(p)]{]}) = d(x^i - x^i(p))_p = dx^i|_p$, since a constant has zero differential (Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](1)); and the $dx^i|_p$ are dual to the $\partial/\partial x^i|_p$ by Lemma [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]]. Every map in (1) is defined by $\langle D, {[}[f]{]} \rangle = D[f]$, which mentions no chart.

^pf-27-7

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|§27.6]], [[§17 Linear Algebra Toolkit#^thm-17-5|§17.5]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-1|§27.1]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-3|Def. §27.3]]

![[m591-13-3.svg]]
*The three spaces and their three bases. $\Phi$ sends the class of a germ to its differential, so the coordinate classes go to the coordinate covectors, and those are the dual basis of the coordinate derivations. Uribe's $dx^i|_p$ of Lecture 10 and the classes ${[}[x^i - x^i(p)]{]}$ of Problem 3 are the same objects, seen through $\Phi$.*

**Assignment 3, Problem 3.** Part (a) is the well-definedness in Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|§27.6]]. Part (b) is its non-degeneracy, and the “therefore” of (b) is Theorem [[§17 Linear Algebra Toolkit#^thm-17-5|§17.5]], which uses *both* halves: right non-degeneracy bounds $\dim I_p/I_p^2 \le n$, left non-degeneracy gives $n \le \dim I_p/I_p^2$. The submitted solution reaches the isomorphism by another route: it shows $\Phi$ injective by right non-degeneracy and surjective by checking that $\Phi({[}[x^i - x^i(p)]{]})$ is the dual basis — which is part (3) of the theorem.

**Comparison with Lee.** In the text of Chapter 11, Lee defines the cotangent space as the dual $(T_pM)^*$, motivated as the coordinate-independent replacement for the gradient. The description of this subsection is his Problem 11-4. Part (a) is Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]], down to the phrase “vanishes to second order”, and part (b) is Theorem [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7|§27.7]](1)–(2). There are two differences. First, Lee's $I_p$ consists of smooth functions on all of $M$ vanishing at $p$, not germs, so his version needs bump functions to pass between local and global, as everywhere in his treatment (Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-3|§23.3]]). Second, Lee proves the isomorphism directly, showing that $f \mapsto df_p$ vanishes on $I_p^2$ and descends to the quotient, where Assignment 3 goes through a non-degenerate pairing and the pairing theorem. His remark to the problem adds two points: some treatments define $T_p^*M$ first, as $I_p/I_p^2$, and then $T_pM$ as its dual — the order Uribe called in some ways more natural — and covectors, as classes of functions $M \to \mathbb{R}$, are dual to tangent vectors as classes of curves $\mathbb{R} \to M$ (his Problem 3-8; here Theorem [[§26 Tangent Vectors as Velocities of Curves#^thm-26-2|§26.2]]). The quotient $I_p/I_p^2$ is also the manifold analogue of the Zariski cotangent space of algebraic geometry.
