---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 34
tags: [differentiable-manifolds, math591]
---
← [[§33 Covectors in Coordinates]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§35 Local Diffeomorphisms]] →

*Stage: abstract, dual — The cotangent space recovered from germs alone, $T_p^{\ast}M \cong I_p/I_p^2$, with no dualizing; covectors then pull back along smooth maps, as germs do.*

*Assignment 3, Problem 3. The cotangent space was defined in Lecture 10 as the dual $(T_pM)^{\ast}$. This subsection shows that it also has a description with no dualizing at all, in terms of germs alone — “as you can see, it has the natural definition $I_p/I_p^2$.” The proof splits into four results: a characterization of $I_p^2$, a basis of the quotient, a non-degenerate pairing, and the isomorphism, which then comes from the [[§21 Linear Algebra Toolkit#^thm-21-5|Linear Algebra Toolkit]] for free.*

> [!definition] Definition §34.1: The Space $I_p/I_p^2$
> $I_p/I_p^2$ is the quotient vector space (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]) of $I_p$ by its subspace $I_p^2$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-1|§28.1]]). The class of $[f] \in I_p$ is written ${[}[f]{]} = [f] + I_p^2$, and ${[}[f]{]} = {[}[f']{]}$ iff $[f'] - [f] \in I_p^2$.

^def-34-1

> [!remark]- Connections
> - The quotient space construction: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].

> [!theorem] Proposition §34.1: Germs Vanishing to Second Order
> For $[f] \in C_p^\infty(M)$ the following are equivalent:
> 1. $[f] \in I_p^2$;
> 2. $f(p) = 0$ and $df_p = 0$;
> 3. $f(p) = 0$ and $\partial f/\partial x^i(p) = 0$ for all $i$, in one — hence every — chart at $p$.
>
> *Lee: Problem 11-4(a)*

^prop-34-1

> [!proof]+ Proof
> *(2)$\iff$(3).* Both conditions contain $f(p) = 0$; compare the rest. By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], in any chart at $p$,
>
> $$
> df_p = \sum_{i=1}^n \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p ,
> $$
>
> and the $dx^i|_p$ are linearly independent, so this combination is $0$ exactly when every coefficient is $0$: $df_p = 0 \iff \partial f/\partial x^i(p) = 0$ for all $i$. Condition (2) mentions no chart, so (3) in one chart gives (2), which gives (3) in every chart — which is why “one” chart implies “every”.
>
> *(1)$\Rightarrow$(2).* Let $[f] \in I_p^2$, so $[f] = \sum_k [u_k][w_k]$ with all $[u_k], [w_k] \in I_p$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]), i.e. $u_k(p) = w_k(p) = 0$. Evaluation at $p$ is an algebra homomorphism (Proposition [[§27 Germs#^prop-27-2|§27.2]]), so $f(p) = \sum_k u_k(p)\, w_k(p) = 0$. For $D \in T_pM$, by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], the linearity of $D$, and its Leibniz rule (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]),
>
> $$
> df_p(D) = D[f] = \sum_k D\big([u_k][w_k]\big) = \sum_k \big(u_k(p)\, D[w_k] + w_k(p)\, D[u_k]\big) = \sum_k \big(0 \cdot D[w_k] + 0 \cdot D[u_k]\big) = 0 .
> $$
>
> This holds for every $D$, so $df_p = 0$. (The middle steps are Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2).)
>
> *(3)$\Rightarrow$(1).* *(Assignment 3, Problem 3.)* Fix a chart $(U,\varphi)$ at $p$, a representative $f : V \to \mathbb{R}$, and put $a = \varphi(p)$ and $f_\varphi = f \circ \varphi^{-1}$. The hypotheses say $f_\varphi(a) = f(p) = 0$ and $\partial f_\varphi/\partial r^i(a) = \partial f/\partial x^i(p) = 0$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]). On an open ball $B \subseteq \varphi(U \cap V)$ centred at $a$, Hadamard's lemma (Lemma [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]]) gives smooth $f_i$ on $B$ with $f_\varphi(r) = f_\varphi(a) + \sum_i (r^i - a^i) f_i(r)$; here the constant term $f_\varphi(a)$ is $0$, so
>
> $$
> f_\varphi(r) = \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f_\varphi}{\partial r^i}(a) = 0 .
> $$
>
> On the open neighbourhood $W = \varphi^{-1}(B)$ of $p$, substitute $r = \varphi(q)$; then $r^i = x^i(q)$, $a^i = x^i(p)$ and $f_\varphi(\varphi(q)) = f(q)$, so
>
> $$
> f(q) = \sum_{i=1}^n \big(x^i(q) - x^i(p)\big)\,(f_i \circ \varphi)(q) \qquad (q \in W).
> $$
>
> Two functions that agree on a neighbourhood of $p$ have the same germ, so $[f] = \sum_i [x^i - x^i(p)]\,[f_i \circ \varphi]$. In each term both factors lie in $I_p$: $x^i(p) - x^i(p) = 0$, and $(f_i \circ \varphi)(p) = f_i(a) = 0$. So $[f]$ is a finite sum of products of two elements of $I_p$, that is, $[f] \in I_p^2$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]).

^pf-34-1

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|§29.3]], [[§27 Germs#^prop-27-2|§27.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]]

> [!remark] Remark
> The proposition is the conceptual centre of Problem 3. $I_p$ consists of the germs vanishing to *first* order at $p$, and $I_p^2$ of those vanishing to *second* order — value and first derivatives zero. So the quotient $I_p/I_p^2$ remembers exactly the first derivatives of a germ that vanishes at $p$, and nothing else. It only needs first-order Hadamard: the vanishing of $f_i(a)$ is what puts the second factor in $I_p$.

^rem-34-1

![[m591-13-4.svg]]
*Classes in $I_p/I_p^2$, for $M = \mathbb{R}$. The blue germs $f_1$ and $f_2$ both vanish at $p$ with the same slope $c$, so $f_1 - f_2$ vanishes to second order and ${[}[f_1]{]} = {[}[f_2]{]} = c\,{[}[x - p]{]}$: the class keeps only the red tangent line and forgets the curvature. The green $g$ has value and slope zero at $p$, so $[g] \in I_p^2$ and ${[}[g]{]} = 0$ (Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]]).*

> [!theorem] Proposition §34.2: A Basis of $I_p/I_p^2$
> Let $(U, \varphi)$ be a chart at $p$ with coordinate functions $x^1, \ldots, x^n$. For every $[f] \in I_p$,
>
> $$
> {[}[f]{]} = \sum_{i=1}^n \frac{\partial f}{\partial x^i}(p)\, {[}[x^i - x^i(p)]{]},
> $$
>
> and the classes ${[}[x^1 - x^1(p)]{]}, \ldots, {[}[x^n - x^n(p)]{]}$ form a basis of $I_p/I_p^2$. In particular $\dim I_p/I_p^2 = n$.
>
> *Lee: cf. Problem 11-4(a)*

^prop-34-2

> [!proof]+ Proof
> Each $x^i - x^i(p)$ is smooth on $U$ and vanishes at $p$, so its germ lies in $I_p$. Two facts about partial derivatives at $p$ are used. They are linear, since $\partial/\partial x^j|_p$ is a derivation (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); and
>
> $$
> \frac{\partial\big(x^i - x^i(p)\big)}{\partial x^j}(p) = \frac{\partial x^i}{\partial x^j}(p) - 0 = \delta^i_j ,
> $$
>
> because a derivation kills constants (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)) and $\partial x^i/\partial x^j(p) = dx^i|_p(\partial/\partial x^j|_p) = \delta^i_j$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], then Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]: the $dx^i|_p$ are the basis dual to the $\partial/\partial x^j|_p$, Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]).
>
> *The expansion.* Let $[f] \in I_p$, write $c_i = \partial f/\partial x^i(p)$, and put $g = f - \sum_i c_i\,(x^i - x^i(p))$ near $p$. Then $g(p) = f(p) - \sum_i c_i \cdot 0 = 0$, and for each $j$
>
> $$
> \frac{\partial g}{\partial x^j}(p) = \frac{\partial f}{\partial x^j}(p) - \sum_{i=1}^n c_i\, \delta^i_j = c_j - c_j = 0 .
> $$
>
> By Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] ((3)$\Rightarrow$(1)), $[g] \in I_p^2$, that is, ${[}[g]{]} = 0$. The projection $[f] \mapsto {[}[f]{]}$ is linear (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)), so from $[f] = [g] + \sum_i c_i\,[x^i - x^i(p)]$,
>
> $$
> {[}[f]{]} = {[}[g]{]} + \sum_{i=1}^n c_i\, {[}[x^i - x^i(p)]{]} = \sum_{i=1}^n \frac{\partial f}{\partial x^i}(p)\, {[}[x^i - x^i(p)]{]} .
> $$
>
> *Spanning.* Every element of $I_p/I_p^2$ is a class ${[}[f]{]}$ with $[f] \in I_p$, so by the expansion the classes ${[}[x^i - x^i(p)]{]}$ span.
>
> *Independence.* Suppose $\sum_i c_i\,{[}[x^i - x^i(p)]{]} = 0$. By linearity of the projection, the germ $[h] = \sum_i c_i\,[x^i - x^i(p)]$ has ${[}[h]{]} = 0$, i.e. $[h] \in I_p^2$. By Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] ((1)$\Rightarrow$(3)), $\partial h/\partial x^j(p) = 0$ for every $j$; and by the two facts above, $\partial h/\partial x^j(p) = \sum_i c_i\, \delta^i_j = c_j$. So every $c_j = 0$.
>
> So the $n$ classes form a basis, and $\dim I_p/I_p^2 = n$.

^pf-34-2

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]], [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]]

This is the cotangent counterpart of the basis theorem for $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]): the coefficients of ${[}[f]{]}$ are the first partials of $f$, just as the coefficients of a derivation $D$ were its values $D[x^i]$.

> [!definition] Definition §34.2: The Pairing Between Tangent Vectors and $I_p/I_p^2$
> The **pairing** of $T_pM$ with $I_p/I_p^2$ is
>
> $$
> \langle\ ,\ \rangle : T_pM \times I_p/I_p^2 \to \mathbb{R}, \qquad \langle D, {[}[f]{]} \rangle = D[f] .
> $$

^def-34-2

> [!theorem] Proposition §34.3: The Pairing Is Well Defined and Non-Degenerate
> The pairing of Definition [[§34 The Cotangent Space from Germs#^def-34-2|§34.2]] is well defined, bilinear, and non-degenerate in the sense of Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]].
>
> *Lee: no counterpart; Lee proves Problem 11-4(b) without a pairing*

^prop-34-3

> [!proof]+ Proof
> *Well defined* *(Problem 3(a))*. The value $\langle D, {[}[f]{]} \rangle = D[f]$ must not depend on the representative $[f]$ of the class. If ${[}[f]{]} = {[}[f']{]}$, then $[f'] - [f] \in I_p^2$ (Definition [[§34 The Cotangent Space from Germs#^def-34-1|§34.1]]), say $[f'] - [f] = \sum_k [u_k][w_k]$ with $[u_k], [w_k] \in I_p$. By the linearity and the Leibniz rule of $D$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]),
>
> $$
> D[f'] - D[f] = D\big([f'] - [f]\big) = \sum_k \big(u_k(p)\, D[w_k] + w_k(p)\, D[u_k]\big) = 0,
> $$
>
> since $u_k(p) = w_k(p) = 0$. (Equivalently: $D$ restricted to $I_p$ is linear and vanishes on $I_p^2$, Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](2), so it descends to $I_p/I_p^2$ by the universal property of quotient spaces, Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](2).)
>
> *Bilinear.* In the second argument, by the quotient operations (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]) and the linearity of $D$:
>
> $$
> \big\langle D,\ a{[}[f]{]} + b{[}[g]{]} \big\rangle = \big\langle D, {[}[af + bg]{]} \big\rangle = D[af + bg] = a\,D[f] + b\,D[g] = a\,\langle D, {[}[f]{]} \rangle + b\,\langle D, {[}[g]{]} \rangle .
> $$
>
> In the first argument, because derivations are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]):
>
> $$
> \big\langle aD + bE,\ {[}[f]{]} \big\rangle = (aD + bE)[f] = a\,D[f] + b\,E[f] = a\,\langle D, {[}[f]{]} \rangle + b\,\langle E, {[}[f]{]} \rangle .
> $$
>
> *Left non-degenerate.* Suppose $\langle D, {[}[f]{]} \rangle = D[f] = 0$ for every $[f] \in I_p$. Let $[f] \in C_p^\infty(M)$ be any germ. Then $[f] - \underline{f(p)} \in I_p$, since it vanishes at $p$, and $D$ kills the constant germ $\underline{f(p)}$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)); so
>
> $$
> D[f] = D\big[f - \underline{f(p)}\big] + D\big[\underline{f(p)}\big] = 0 + 0 = 0 .
> $$
>
> So $D$ vanishes on all germs: $D = 0$.
>
> *Right non-degenerate.* Suppose $[f] \in I_p$ and $\langle D, {[}[f]{]} \rangle = D[f] = 0$ for every $D \in T_pM$. By Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], $df_p(D) = D[f] = 0$ for every $D$, so $df_p = 0$; and $f(p) = 0$ since $[f] \in I_p$. By Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]] ((2)$\Rightarrow$(1)), $[f] \in I_p^2$, that is, ${[}[f]{]} = 0$.

^pf-34-3

*Uses:* [[§34 The Cotangent Space from Germs#^def-34-2|Def. §34.2]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§21 Linear Algebra Toolkit#^def-21-5|Def. §21.5]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]], [[§34 The Cotangent Space from Germs#^def-34-1|Def. §34.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§21 Linear Algebra Toolkit#^def-21-6|Def. §21.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

> [!theorem] Theorem §34.4: The Cotangent Space from Germs
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

^thm-34-4

> [!proof]+ Proof
> *(1)* Apply Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]] with $V = T_pM$, $W = I_p/I_p^2$ and $B = \langle\ ,\ \rangle$. Its hypotheses hold: the pairing is bilinear and non-degenerate (Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]]), and $T_pM$ is finite-dimensional, of dimension $m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). So the two induced maps of Definition [[§21 Linear Algebra Toolkit#^def-21-4|§21.4]],
>
> $$
> B^\flat : T_pM \to \big(I_p/I_p^2\big)^{\ast}, \ \ D \mapsto \langle D, \cdot\,\rangle, \qquad\qquad \Phi = B^\sharp : I_p/I_p^2 \to (T_pM)^{\ast}, \ \ {[}[f]{]} \mapsto \langle \cdot\,, {[}[f]{]} \rangle,
> $$
>
> are isomorphisms.
>
> *(2)* For every $D \in T_pM$, by the definition of $\Phi$, the definition of the pairing, and Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]],
>
> $$
> \Phi({[}[f]{]})(D) = \langle D, {[}[f]{]} \rangle = D[f] = df_p(D) .
> $$
>
> The covectors $\Phi({[}[f]{]})$ and $df_p$ agree at every $D$, so they are equal.
>
> *(3)* By (2) and the linearity of $d$ (Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]](1)), applied to $x^i$ and the constant function $x^i(p)$,
>
> $$
> \Phi\big({[}[x^i - x^i(p)]{]}\big) = d\big(x^i - x^i(p)\big)_p = dx^i|_p - d\big(x^i(p)\big)_p = dx^i|_p ,
> $$
>
> because the differential of a constant function $c$ is $0$: by Definition [[§32 The Cotangent Space#^def-32-5|§32.5]], $dc_p = \iota_c \circ c_{\ast p}$, and $c_{\ast p} = 0$ by Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]](1), $c$ being a constant map $M \to \mathbb{R}$. Directly, $dc_p(D) = D[\underline{c}] = 0$ for every $D$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)). The $dx^i|_p$ are the basis dual to the $\partial/\partial x^i|_p$ by Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]].
>
> *No chart.* The pairing $\langle D, {[}[f]{]} \rangle = D[f]$ is defined without coordinates, and so are $B^\flat$ and $\Phi$, which are built from it alone; a chart enters only in (3), to name the bases.

^pf-34-4

*Uses:* [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]], [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§32 The Cotangent Space#^cor-32-3|§32.3]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]

![[m591-13-3.svg]]
*The three spaces and their three bases. $\Phi$ sends the class of a germ to its differential, so the coordinate classes go to the coordinate covectors, and those are the dual basis of the coordinate derivations. Uribe's $dx^i|_p$ of Lecture 10 and the classes ${[}[x^i - x^i(p)]{]}$ of Problem 3 are the same objects, seen through $\Phi$.*

> [!remark] Remark: The Most Natural Description
> Lecture 15 came back to this theorem: “the cotangent space is, in a way, very extremely natural from the point of view of functions.” The tangent space needed derivations; the cotangent space needs only functions — germs vanishing at $p$, modulo those vanishing to second order. This is one reason why the cotangent bundle will turn out to carry structure that the tangent bundle does not.

^rem-34-2

> [!remark] Remark: Review Session: The More Natural Space
> *Review session, Oct 16, recalling this homework problem.* $I_p$, the germs vanishing at $p$, is an ideal, and $T_p^{\ast}M \cong I_p/I_p^2$ naturally: “nothing with curves, nothing with ambient spaces … very, very general and very quick.” Uribe recalled a professor of his at MIT: “this tells you that the cotangent space really is the more natural space. … It has a one-page definition, and it has this symplectic structure that is … God-given. It's just sitting there” — even though we are less used to working with the dual object.

^rem-34-3

> [!theorem] Theorem §34.5: Dimension of the Cotangent Space
> Let $M$ be a smooth $m$-manifold and $p \in M$. Then
>
> $$
> \dim T_p^{\ast}M \;=\; \dim \big(I_p/I_p^2\big) \;=\; \dim T_pM \;=\; m .
> $$
>
> The cotangent space ([[§32 The Cotangent Space#^def-32-4|Def. §32.4]]) has the same dimension as the tangent space, at every point.

^thm-34-5

> [!proof]+ Proof
> *(Collected from the results above; not stated as a single theorem in lecture.)* $T_p^{\ast}M = (T_pM)^{\ast}$ is the dual of a space of dimension $m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), and the dual of a finite-dimensional space has the same dimension (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]); explicitly, the $m$ covectors $dx^i|_p$ form a basis (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]). And $I_p/I_p^2$ has the basis of $m$ classes ${[}[x^i - x^i(p)]{]}$ (Proposition [[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]]), or equivalently is isomorphic to $T_p^{\ast}M$ by $\Phi$ (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]).

^pf-34-5

*Uses:* [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§34 The Cotangent Space from Germs#^prop-34-2|§34.2]], [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]

Equal dimension is what makes the isomorphisms of Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]] possible, but the dimension count alone does not produce them: any two spaces of dimension $m$ are isomorphic, by choosing bases. What Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]] adds is that $\Phi$ needs no choice. Between $T_pM$ and $T_p^{\ast}M$ themselves there is no such choice-free isomorphism, which is why the tangent and cotangent bundles are isomorphic “but not naturally” ([[§50 The Cotangent Bundle|§50]]).

**Assignment 3, Problem 3.** Part (a) is the well-definedness in Proposition [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]]. Part (b) is its non-degeneracy, and the “therefore” of (b) is Theorem [[§21 Linear Algebra Toolkit#^thm-21-5|§21.5]], which uses *both* halves: right non-degeneracy bounds $\dim I_p/I_p^2 \le n$, left non-degeneracy gives $n \le \dim I_p/I_p^2$. The submitted solution reaches the isomorphism by another route: it shows $\Phi$ injective by right non-degeneracy and surjective by checking that $\Phi({[}[x^i - x^i(p)]{]})$ is the dual basis — which is part (3) of the theorem.

**Comparison with Lee.** In the text of Chapter 11, Lee defines the cotangent space as the dual $(T_pM)^{\ast}$, motivated as the coordinate-independent replacement for the gradient. The description of this subsection is his Problem 11-4. Part (a) is Proposition [[§34 The Cotangent Space from Germs#^prop-34-1|§34.1]], down to the phrase “vanishes to second order”, and part (b) is Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]](1)–(2). There are two differences. First, Lee's $I_p$ consists of smooth functions on all of $M$ vanishing at $p$, not germs, so his version needs bump functions to pass between local and global, as everywhere in his treatment (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]]). Second, Lee proves the isomorphism directly, showing that $f \mapsto df_p$ vanishes on $I_p^2$ and descends to the quotient, where Assignment 3 goes through a non-degenerate pairing and the pairing theorem. His remark to the problem adds two points: some treatments define $T_p^{\ast}M$ first, as $I_p/I_p^2$, and then $T_pM$ as its dual — the order Uribe called in some ways more natural — and covectors, as classes of functions $M \to \mathbb{R}$, are dual to tangent vectors as classes of curves $\mathbb{R} \to M$ (his Problem 3-8; here Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]). The quotient $I_p/I_p^2$ is also the manifold analogue of the Zariski cotangent space of algebraic geometry.

## Pulling Back Covectors

*Lecture 15. A smooth map pushes tangent vectors forward; dually, it pulls covectors back. “Functions pull back by composition, and you can pull back actually any one-form by using the dual map of the forward star.”*

> [!definition] Definition §34.3: Pullback of Covectors
> Let $F : M \to N$ be smooth and $p \in M$. The **pullback of covectors** at $p$ is the dual map ([[§21 Linear Algebra Toolkit#^def-21-3|Definition §21.3]]) of the pushforward $F_{\ast p} : T_pM \to T_{F(p)}N$:
>
> $$
> F_p^* : T^*_{F(p)}N \longrightarrow T_p^*M, \qquad (F_p^*\alpha)(v) = \alpha\big(F_{*p}v\big) .
> $$
>
> *Lee: Ch. 11, Pullbacks of Covector Fields*

^def-34-3

> [!remark]- Connections
> - The dual map in LADR: [[§12 Duality#^ladr-3-118|LADR 3.118]]. The field version, pulling back a one-form point by point: [[§51 One-Forms#^def-51-4|Def. §51.4]].

Directions: points and vectors move *forward* along $F$, from $M$ to $N$; functions and covectors move *backward*, from $N$ to $M$, because they are things that eat — to evaluate one on $M$, push the input to $N$ and evaluate there.

> [!remark] Remark: One Symbol for Two Pullbacks
> The symbol $F_p^{\ast}$ now has two meanings. On germs it is the pullback $C^\infty_{F(p)}(N) \to C^\infty_p(M)$, $[g] \mapsto [g \circ F]$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5]]); on covectors it is the dual map $T^{\ast}_{F(p)}N \to T_p^{\ast}M$ of [[§34 The Cotangent Space from Germs#^def-34-3|Definition §34.3]]. Context decides which is meant, and the two are compatible: by the next proposition, pulling back the differential of $g$ is the same as differentiating the pulled-back germ, $F_p^{\ast}(dg_{F(p)}) = d\big(F_p^{\ast}[g]\big)_p$.

^rem-34-4

> [!theorem] Proposition §34.6: Pullback Commutes with $d$
> Let $F : M \to N$ be smooth, $p \in M$, and $f$ smooth near $F(p)$. Then
>
> $$
> F_p^*\big(df_{F(p)}\big) = d(f \circ F)_p \quad \text{in } T_p^*M .
> $$
>
> *Lee: Proposition 11.25*

^prop-34-6

> [!proof]+ Proof
> *(Lecture 15 — “every equal sign is a definition … maybe this is best to be reflected upon at your coffee shop of choice.”)* For $v \in T_pM$:
>
> $$
> F_p^*\big(df_{F(p)}\big)(v) = df_{F(p)}\big(F_{*p}v\big) = \big(F_{*p}v\big)[f] = v[f \circ F] = d(f \circ F)_p(v) .
> $$
>
> The first equality is the definition of the dual map; the second, of the differential of a function, applied to the vector $F_{\ast p}v \in T_{F(p)}N$; the third, of the pushforward; the fourth, of the differential of $f \circ F$. Two covectors that agree on every $v$ are equal.

^pf-34-6

*Uses:* [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§21 Linear Algebra Toolkit#^def-21-3|Def. §21.3]]

> [!remark] Remark: The Two Differentials Meet
> In $\mathbb{R}^n$, with the dot-product identification $v \mapsto \xi_v$ of Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], under which $dh_p = \xi_{\nabla h(p)}$ (its part (3), with the gradient of Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]), the proposition is the chain rule in the form $\nabla(f \circ F) = J_F^{\mathsf T}\, \nabla f$. Explicitly, for $F$ smooth on an open subset of $\mathbb{R}^m$ with values in $\mathbb{R}^n$ and $J_F(p)$ its Jacobian, $F_{\ast p}(D_w|_p) = D_{J_F(p)w}|_{F(p)}$ (Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]), so for every $w \in \mathbb{R}^m$
>
> $$
> \xi_{\nabla(f \circ F)(p)}\big(D_w|_p\big) = d(f \circ F)_p\big(D_w|_p\big) = df_{F(p)}\big(D_{J_F(p)w}|_{F(p)}\big) = \nabla f(F(p)) \cdot J_F(p)w = \big(J_F(p)^{\mathsf T}\, \nabla f(F(p))\big) \cdot w = \xi_{J_F(p)^{\mathsf T} \nabla f(F(p))}\big(D_w|_p\big) ,
> $$
>
> the first and third equalities being part (3) of Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]] (for $f \circ F$ at $p$, and for $f$ at $F(p)$), the second the proposition above together with the definition of $F_p^{\ast}$; as $v \mapsto \xi_v$ is injective, $\nabla(f \circ F)(p) = J_F(p)^{\mathsf T}\, \nabla f(F(p))$. Uribe added that the pushforward $F_\ast$ “we should have called the differential of $F$ ages ago”: for a function $f : M \to \mathbb{R}$, $df_p$ is $f_{\ast p}$ followed by the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$.

^rem-34-5

> [!remark]- Connections
> - The chain rule in 452: [[Multivariable Chain Rule]]. Pullback of forms on $\mathbb{R}^n$ commuting with $d$ in 452: [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]. The field version: [[§51 One-Forms#^cor-51-4|Cor. §51.4]].

*Not from lecture: the pullback of covectors in the germ picture of this section.* The pullback of germs ([[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5]]) already moved functions backward along $F$, and the pushforward of derivations was built from it, $F_{\ast p}D = D \circ F_p^{\ast}$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6]]). Through the isomorphism $\Phi$ of [[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4]], the pullback of covectors is that same pullback of germs.

> [!theorem] Proposition §34.7: Pullback of Covectors from the Pullback of Germs
> Let $F : M \to N$ be smooth, $p \in M$, and $q = F(p)$.
> 1. The [[§28 Derivations and the Abstract Tangent Space#^def-28-5|pullback of germs]] $F_p^{\ast} : C^\infty_q(N) \to C^\infty_p(M)$ maps $I_q$ into $I_p$ and $I_q^2$ into $I_p^2$, so it induces a linear map
>
>    $$
>    \bar F_p^* : I_q/I_q^2 \longrightarrow I_p/I_p^2, \qquad {[}[g]{]} \longmapsto {[}[g \circ F]{]} .
>    $$
>
> 2. Under the isomorphisms $\Phi_q : I_q/I_q^2 \to T_q^{\ast}N$ and $\Phi_p : I_p/I_p^2 \to T_p^{\ast}M$ of [[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4]], $\bar F_p^{\ast}$ is the [[§34 The Cotangent Space from Germs#^def-34-3|pullback of covectors]]:
>
>    $$
>    \Phi_p \circ \bar F_p^* = F_p^* \circ \Phi_q .
>    $$

^prop-34-7

![[m591-34-5.svg]]

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *(1)* By [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|Proposition §28.4]], $F_p^{\ast}$ is a homomorphism of $\mathbb{R}$-algebras with $F_p^{\ast}(I_q) \subseteq I_p$. An element of $I_q^2$ is a finite sum $\sum_k [u_k][w_k]$ with $[u_k], [w_k] \in I_q$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-4|Definition §28.4]]), and since $F_p^{\ast}$ preserves sums and products,
>
> $$
> F_p^*\Big(\sum_k [u_k][w_k]\Big) = \sum_k F_p^*[u_k]\; F_p^*[w_k],
> $$
>
> a finite sum of products of two elements of $I_p$, that is, an element of $I_p^2$. So the composite of $F_p^{\ast}|_{I_q} : I_q \to I_p$ with the projection $I_p \to I_p/I_p^2$ is linear and vanishes on $I_q^2$. By the universal property of quotient spaces ([[§21 Linear Algebra Toolkit#^prop-21-6|Proposition §21.6]](2)) it descends to a linear map $\bar F_p^{\ast}$ on $I_q/I_q^2$, with $\bar F_p^{\ast}{[}[g]{]} = {[}[F_p^{\ast}[g]]{]} = {[}[g \circ F]{]}$.
>
> *(2)* Let ${[}[g]{]} \in I_q/I_q^2$. By [[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4]](2) at $p$, [[§34 The Cotangent Space from Germs#^prop-34-6|Proposition §34.6]], and Theorem §34.4(2) at $q$,
>
> $$
> \Phi_p\big(\bar F_p^*{[}[g]{]}\big) = \Phi_p\big({[}[g \circ F]{]}\big) = d(g \circ F)_p = F_p^*\big(dg_q\big) = F_p^*\big(\Phi_q{[}[g]{]}\big) .
> $$
>
> The two linear maps $\Phi_p \circ \bar F_p^{\ast}$ and $F_p^{\ast} \circ \Phi_q$ agree at every element, so they are equal.

^pf-34-7

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]], [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]]

So in the germ picture no dual map is needed: a covector at $q$ is a class of germs vanishing at $q$, and it pulls back by composing with $F$, exactly as germs do. One operation, $[g] \mapsto [g \circ F]$, moves everything: tangent vectors act on germs, so they are pushed *forward* by precomposing with it; covectors are classes of germs, so they are pulled *back* by it. “Functions pull back by composition” (Lecture 15) covers covectors too.
