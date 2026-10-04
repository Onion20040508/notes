---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 24
tags: [differentiable-manifolds, math591]
---
← [[§23 Derivations and the Abstract Tangent Space]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§25 The Differential in Coordinates]] →

*Stage: abstract — Charts give derivations $\partial/\partial x^i|_p$, and they form a basis of $T_pM$: $\dim T_pM = \dim M$. The proof needs Taylor's theorem with a smooth remainder.*

> [!definition] Definition §24.1: Coordinate Functions of a Chart
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
> 3. For a function $f$ defined on $U$, its **coordinate representation** in the chart is $f_\varphi = f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$, as in Definition [[§15 Smooth Functions and Smooth Maps#^def-15-2|§15.2]]; thus $f = f_\varphi \circ \varphi$ on $U$. In particular $(x^i)_\varphi = r^i \circ \varphi \circ \varphi^{-1} = r^i$ on $\varphi(U)$.
>
> *Lee: Ch. 1, Coordinate Charts*

^def-24-1

> [!remark] Remark
> **A notational discipline.** Uribe stopped to insist on this. The $x^i$ live *upstairs*, as functions on the manifold, and the $r^i$ *downstairs*, as functions on $\mathbb{R}^n$; conflating them is the main source of confusion in what follows. The identity $(x^i)_\varphi = r^i$ is the bridge between the two rows: it says that the coordinate functions, written in their own chart, are the standard coordinates. It also shows that each $x^i$ is a smooth function on $U$, by Definition [[§15 Smooth Functions and Smooth Maps#^def-15-2|§15.2]], since $r^i$ is smooth.

^rem-24-1

![[m591-12-6.svg]]
*The board diagram for this section. Both triangles commute: the left one says $f = f_\varphi \circ \varphi$, which is what smoothness of $f$ means; the right one is the* definition *$x^i = r^i \circ \varphi$ of the $i$-th coordinate function on $U$ (Definition [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|§24.1]]). Everything upstairs is expressed downstairs by composing with $\varphi$, and the derivation about to be defined does its differentiating entirely on the bottom row, where partial derivatives already make sense.*

> [!definition] Definition §24.2: Coordinate Derivations
> Let $(U,\varphi)$ be a smooth chart with $p \in U$, with coordinate functions $x^1, \ldots, x^n$ (Definition [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|§24.1]]), and let $i \in \{1,\ldots,n\}$. Define $\dfrac{\partial}{\partial x^i}\Big|_p : C_p^\infty(M) \to \mathbb{R}$ by
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

^def-24-2

> [!theorem] Proposition §24.1: Coordinate Derivations Are Derivations
> $\dfrac{\partial}{\partial x^i}\Big|_p$ is well defined on germs and is a derivation at $p$.

^prop-24-1

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

^pf-24-1

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^def-24-2|Def. §24.2]], [[§22 Tangent Spaces II꞉ Germs#^def-22-2|Def. §22.2]], [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§6 Differentiability#^thm-6-4|452 §6.4]]

The proof of the Basis Theorem below needs a form of Taylor expansion whose remainder is not an estimate but an exact, *smooth* term — “a theorem from calculus” that is not usually taught there. It is built in two steps: first order, then the first-order statement applied again.

> [!theorem] Lemma §24.2: Hadamard's Lemma
> Let $W \subseteq \mathbb{R}^n$ be open, $a = (a^1,\ldots,a^n) \in W$, $f : W \to \mathbb{R}$ smooth, and $B \subseteq W$ an open ball centred at $a$. Then there are smooth functions $f_1, \ldots, f_n$ on $B$ with
>
> $$
> f(r) = f(a) + \sum_{i=1}^n (r^i - a^i)\, f_i(r) \quad (r \in B), \qquad f_i(a) = \frac{\partial f}{\partial r^i}(a) .
> $$
>
> Explicitly, $f_i(r) = \displaystyle\int_0^1 \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt$.
>
> *Lee: cf. Theorem C.15, used in the proof of Proposition 3.2*

^lem-24-2

> [!proof]+ Proof
> *(Lecture 9: “the proof is delightfully simple.”)* Fix $r \in B$. The segment $t \mapsto a + t(r - a)$, $t \in [0,1]$, runs from $a$ to $r$ and stays in $B$, a ball being convex. By the fundamental theorem of calculus and the chain rule,
>
> $$
> f(r) - f(a) = \int_0^1 \frac{d}{dt} f\big(a + t(r-a)\big)\, dt = \int_0^1 \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}\big(a + t(r-a)\big)\, dt = \sum_{i=1}^n (r^i - a^i)\, f_i(r),
> $$
>
> the factors $r^i - a^i$ coming out of the integral because they do not depend on $t$. Each $f_i$ is smooth on $B$: the integrand is smooth in $(t, r)$ on $[0,1] \times B$, so differentiation under the integral sign is legitimate to every order. At $r = a$ the integrand is constant, and $f_i(a) = \partial f/\partial r^i(a)$.

^pf-24-2

*Uses:* [[Fundamental Theorem of Calculus|451 §34.1]], [[Multivariable Chain Rule|452 §10.2]]

**Transcription note.** In Lecture 9 the path in the integral was first written with the wrong endpoints; a student corrected it to the convex combination $t(r - a) + a$, which runs from $a$ at $t = 0$ to $r$ at $t = 1$, as above.

Uribe called the proof “delightfully simple.” A student corrected the path on the board: it must be the segment $a + t(r - a)$, equal to $a$ at $t = 0$ and to $r$ at $t = 1$. Convexity of $B$ is what the proof uses — “everything is local,” but the neighbourhood must contain the segment from $a$ to each of its points, which is why a ball (or any set star-shaped about $a$) is taken.

> [!theorem] Lemma §24.3: Taylor–Hadamard
> In the setting of Lemma [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]], there are smooth functions $f_{ij}$ on $B$, $1 \le i, j \le n$, with
>
> $$
> f(r) \;=\; f(a) \;+\; \sum_{i=1}^n (r^i - a^i)\, \frac{\partial f}{\partial r^i}(a) \;+\; \sum_{i,j=1}^n (r^i - a^i)(r^j - a^j)\, f_{ij}(r) \qquad (r \in B),
> $$
>
> and $f_{ij}(a) = \tfrac12\, \dfrac{\partial^2 f}{\partial r^i\,\partial r^j}(a)$. This is an identity, not an approximation.
>
> *Lee: cf. Theorem C.15*

^lem-24-3

> [!proof]+ Proof
> *(Lecture 9, exactly: first order, then “apply the claim to each $f_i$” and substitute back. Uribe wrote the quadratic term with a factor $\tfrac12$ — “doesn't matter” — which the notes absorb into $f_{ij}$; the value of $f_{ij}(a)$ at the end is a completion, the lecture needing only that the $f_{ij}$ are smooth.)* Apply Lemma [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]] to $f$, obtaining $f_1, \ldots, f_n$; then apply it again to each $f_i$, obtaining smooth $f_{ij}$ with
>
> $$
> f_i(r) = f_i(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r) = \frac{\partial f}{\partial r^i}(a) + \sum_{j=1}^n (r^j - a^j)\, f_{ij}(r).
> $$
>
> Substituting this into $f(r) = f(a) + \sum_i (r^i - a^i) f_i(r)$ gives the identity. For the value at $a$: by Lemma [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]] applied to $f_i$, $f_{ij}(a) = \partial f_i/\partial r^j(a)$, and differentiating the integral formula for $f_i$ under the integral sign,
>
> $$
> \frac{\partial f_i}{\partial r^j}(r) = \int_0^1 t\, \frac{\partial^2 f}{\partial r^j\,\partial r^i}\big(a + t(r-a)\big)\, dt, \qquad\text{so}\qquad \frac{\partial f_i}{\partial r^j}(a) = \frac12\, \frac{\partial^2 f}{\partial r^i\,\partial r^j}(a).
> $$

^pf-24-3

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]]

> [!remark]- Connections
> - Taylor's theorem with an estimated remainder: [[Multivariable Taylor's Theorem|452 §9.2 (Multivariable Taylor's Theorem)]]; in one variable, [[§31 Taylor's Theorem#^thm-31-2|451 §31.2]].

**On the factor $\tfrac12$.** The board states the lemma with $\tfrac12 \sum_{i,j}$ in front of the quadratic term; Uribe added it “just for consistency,” saying it “doesn't matter.” For the *existence* statement that is right — replacing $f_{ij}$ by $2f_{ij}$ converts one form into the other. But the two forms are not interchangeable as written: the iterated proof above produces the version *without* the $\tfrac12$, and with $f_{ij}(a) = \tfrac12 \partial_{ij} f(a)$. The board's normalization is the one in which $f_{ij}(a) = \partial_{ij} f(a)$, matching the Hessian term $\tfrac12 \sum \partial_{ij}f(a)(r^i - a^i)(r^j - a^j)$ of the ordinary Taylor polynomial. A numerical check on a test function confirms the unscaled identity to machine precision and shows the scaled one, with the same $f_{ij}$, to be off. Nothing below depends on the normalization, since only the vanishing of the quadratic term under a derivation is used.

> [!remark] Remark
> **What matters.** “The point is that these functions don't blow up at $a$”: the remainder is a product of two factors vanishing at $a$ with a *smooth* function, not merely a quantity that is small compared with $|r - a|^2$. The same iteration continues to any order.

^rem-24-2

![[m591-12-7.svg]]
*Taylor–Hadamard for $f(r) = e^r$ at $a = 0$, in one variable. Left: the remainder $f(r) - f(a) - f'(a)(r-a)$ is the gap between the graph and its tangent line. Right: the same gap divided by $(r - a)^2$. The quotient $f_{11}(r) = (e^r - 1 - r)/r^2$ has only a removable singularity at $a$: it is smooth there, with value $\tfrac12 = \tfrac12 f''(0)$, exactly as the lemma predicts, and as the iterated proof computes it — $f_1(r) = (e^r - 1)/r$, then $f_{11}(r) = (f_1(r) - f_1(0))/r$. That the quotient extends smoothly across $a$ is the whole content of the lemma.*

> [!theorem] Corollary §24.4: Derivations on $\mathbb{R}^n$
> Let $W \subseteq \mathbb{R}^n$ be open, $a \in W$, and $D$ a derivation at $a$ on $W$. Then for every germ $[f]$ at $a$,
>
> $$
> D[f] = \sum_{i=1}^n \frac{\partial f}{\partial r^i}(a)\, D[r^i], \qquad\text{that is,}\qquad D = \sum_{i=1}^n D[r^i]\, \frac{\partial}{\partial r^i}\Big|_a .
> $$
>
> *Lee: Proposition 3.2 and Corollary 3.3*

^cor-24-4

> [!proof]+ Proof
> Choose a representative $f$ on an open ball $B \subseteq W$ centred at $a$, which changes nothing since $D$ acts on germs, and apply $D$ to the identity of Lemma [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3|§24.3]]:
>
> $$
> D[f] = D\big[\underline{f(a)}\big] + \sum_{i} \frac{\partial f}{\partial r^i}(a)\, D\big[r^i - a^i\big] + \sum_{i,j} D\Big[(r^i - a^i)\cdot\big((r^j - a^j) f_{ij}\big)\Big].
> $$
>
> The constant term vanishes by Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](1). Each quadratic term is $D$ of a product of two germs in $I_a$ — namely $r^i - a^i$ and $(r^j - a^j)f_{ij}$, both zero at $a$ — so it vanishes by Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](2). Finally $D[r^i - a^i] = D[r^i]$ by (1) again. So $D$ sees only the linear part of $f$: “the ultimate formula in the Euclidean case.”

^pf-24-4

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3|§24.3]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]], [[§22 Tangent Spaces II꞉ Germs#^def-22-3|Def. §22.3]], [[§24 Coordinate Derivations and the Basis Theorem#^def-24-2|Def. §24.2]]

> [!theorem] Theorem §24.5: Basis Theorem
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

^thm-24-5

> [!proof]+ Proof
> *(Lecture 9. In lecture the derivation $\tilde D$ was introduced inside this proof — “this is how you push forward derivations … we'll come back to this construction immediately after” — and Uribe remarked that “the order of my presentation is not ideal.” The notes define the pushforward first, in [[§23 Derivations and the Abstract Tangent Space#Pushing Derivations Forward|§23, Pushing Derivations Forward]], so that the proof can cite it.)* Let $D \in T_pM$ and put $a = \varphi(p) = (r_0^1, \ldots, r_0^n)$.
>
> *Step 1: push $D$ down.* Let $\tilde D = \varphi_{\ast p}D \in T_a\,\varphi(U)$, the chart pushforward of Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]; so $\tilde D[g] = D[g \circ \varphi]$ for germs $g$ at $a$.
>
> *Step 2: apply the Euclidean formula downstairs.* By Corollary [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4|§24.4]] on the open set $\varphi(U)$,
>
> $$
> \tilde D[g] = \sum_{i=1}^n \frac{\partial g}{\partial r^i}(a)\, \tilde D[r^i] .
> $$
>
> *Step 3: read it back upstairs.* Let $[f]$ be a germ at $p$, and take $g = f_\varphi = f \circ \varphi^{-1}$. Then $f_\varphi \circ \varphi = f$ near $p$, so $\tilde D[f_\varphi] = D[f]$; by Definition [[§24 Coordinate Derivations and the Basis Theorem#^def-24-2|§24.2]], $\partial f_\varphi/\partial r^i(a) = \partial/\partial x^i|_p[f]$; and $\tilde D[r^i] = D[r^i \circ \varphi] = D[x^i]$. Substituting,
>
> $$
> D[f] = \sum_{i=1}^n D[x^i]\, \frac{\partial}{\partial x^i}\Big|_p[f] \qquad\text{for every germ } [f],
> $$
>
> so $D = \sum_i D[x^i]\, \partial/\partial x^i|_p$ and the coordinate derivations span.
>
> *Step 4: independence.* If $\sum_i c_i\, \partial/\partial x^i|_p = 0$, apply it to $[x^j]$. Since $(x^j)_\varphi = r^j$, we get $\partial/\partial x^i|_p[x^j] = \partial r^j/\partial r^i = \delta^j_i$, hence $c_j = 0$. So the $n$ coordinate derivations form a basis, and the coefficients of $D$ are the numbers $D[x^i]$ — uniquely.

^pf-24-5

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]], [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Def. §23.5]], [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4|§24.4]], [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|Def. §24.1]], [[§24 Coordinate Derivations and the Basis Theorem#^def-24-2|Def. §24.2]], [[§24 Coordinate Derivations and the Basis Theorem#^prop-24-1|§24.1]]

![[m591-12-8.svg]]

$$
\varphi^*[r^i] = [x^i], \qquad \varphi^*[f_\varphi] = [f]
$$

*The proof in one diagram — the defining triangle of the pushforward, for the chart. Downstairs the Euclidean formula computes $\tilde D$ on everything; the two pullback identities displayed under the diagram carry the answer back upstairs, turning $\tilde D[r^i]$ into $D[x^i]$ and $\tilde D[f_\varphi]$ into $D[f]$.*

> [!remark]- Connections
> - The coefficients $D[x^i]$ are the values of the dual basis $dx^i|_p$: [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]]; cf. [[§12 Duality#^ladr-3-114|LADR 3.114]].
> - The components in the coordinate basis give the charts of the tangent bundle: [[§32 The Tangent Bundle#^def-32-2|Def. §32.2]].

**Reconciliation with the lecture.** This is the lecture's proof, in the lecture's order of ideas but with the pushforward defined before it is used rather than after. Two details of the board version. It opens with “$\forall\, [f] \in I_p$”: restricting to germs vanishing at $p$ is harmless, since $D[f] = D[f - f(p)]$ by Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-2|§23.2]](1), but the argument works verbatim for every germ. And the notes had filled in a proof of this theorem before Lecture 9, via two reduction lemmas; those were the pushforward by an inclusion and by the chart in disguise, and they now appear as Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]] and Corollary [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]].

**Transcription note (Lecture 8).** Page 16 of the handwritten notes states Taylor–Hadamard for “$f : U \to \mathbb{R}^2$”; the target is $\mathbb{R}$.

> [!theorem] Theorem §24.6: Ambient and Abstract Agree
> Let $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ be a regular level set and $p \in M$. Then
>
> $$
> T^{\mathrm{geo}}_pM \longrightarrow T_pM, \qquad v \longmapsto D_v,
> $$
>
> from the geometric tangent space (a subspace of $\mathbb{R}^{n+k}$) to the abstract tangent space (derivations at $p$) is an isomorphism of vector spaces.
>
> *Lee: Propositions 3.2, 5.37 and 5.38*

^thm-24-6

> [!proof]+ Proof
> **Announced in lecture.** Stated in lecture in answer to a student's question — “are the ambient and the abstract tangent spaces the same, just defined differently?” — with the answer that they are, but that it has to be proved. Injectivity is Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-2|§22.2]]; that $D_v$ really is a derivation is Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-1|§22.1]]; surjectivity follows from the [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|basis theorem]], both spaces having dimension $n$. Even once it is proved, the notes keep the notations apart: $T^{\mathrm{geo}}_pM$ is the geometric tangent space, $T_pM$ the abstract one.

^pf-24-6

*Uses:* [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-1|Def. §20.1]], [[§22 Tangent Spaces II꞉ Germs#^def-22-1|Def. §22.1]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-1|§22.1]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-2|§22.2]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|§20.3]]

> [!remark]- Connections
> - Proved in detail in [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-7|Consequences, §24.7]], once the basis theorem gives $\dim T_pM = n$.
> - The same identification read through velocities of curves: [[§26 Tangent Vectors as Velocities of Curves#^rem-26-1|The Two Faces Reconciled]].

> [!theorem] Corollary §24.7: Consequences
> Let $M$ be a smooth $n$-manifold and $p \in M$. Then the abstract tangent space has $\dim T_pM = n$, and for a regular level set $M = F^{-1}(c)$ the map $v \mapsto D_v$ of Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|§24.6]], from $T^{\mathrm{geo}}_pM$ to $T_pM$, is an isomorphism.
>
> *Lee: Proposition 3.10*

^cor-24-7

> [!proof]+ Proof
> The first claim is Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]]. For the second, $v \mapsto D_v$ is linear and injective (Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-2|§22.2]]) between spaces of dimension $n$ — the geometric tangent space $T^{\mathrm{geo}}_pM$ by Theorem [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|§20.3]], the abstract tangent space $T_pM$ by Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]] — hence an isomorphism.

^pf-24-7

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-2|§22.2]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-1|§22.1]], [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|§20.3]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - This is the detailed proof of [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|Ambient and Abstract Agree, §24.6]], stated just above.

**Comparison with Lee.** Lee meets the two kinds of tangent vector in the opposite order. He defines $T_pM$ by derivations first, identifies geometric and abstract tangent vectors in $\mathbb{R}^n$ (Proposition 3.2), and only later, for embedded submanifolds, shows $T_pS = \ker d\Phi_p$ (Proposition 5.38). The course starts geometrically, with $T^{\mathrm{geo}}_pM = \ker F'(p)$ inside the ambient space (Theorem [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|§20.3]]), and reaches derivations afterwards. The consequence above is where the two orders meet.

> [!remark] Remark: A Derivation Sees Only the First Derivatives
> The basis theorem showed that, of the whole Taylor expansion of a germ, a derivation sees only the *linear* term — “of the entire Taylor series of the germ, all I care about are the first partials.” [[§27 Tangent Spaces III꞉ The Cotangent Space#The Cotangent Space from Germs|§27, The Cotangent Space from Germs]] says this algebraically: $I_p$ is a maximal ideal, being the kernel of evaluation; $I_p^2$ consists exactly of the germs vanishing to *second* order (Proposition [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]]); and $I_p/I_p^2$ is canonically the *cotangent space* $T_p^{\ast}M$ of Definition [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|§27.1]], built with no dualizing at all (Theorem [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7|§27.7]]). This is the sense in which, as Uribe remarked when he first set out to define the abstract tangent space, “it is more natural to define the dual”: the cotangent space comes first, and the abstract tangent space is its dual. We follow Lee and do not take that route.

^rem-24-3

> [!theorem] Theorem §24.8: Dimension of the Tangent Space
> Let $M$ be a smooth $n$-manifold. Then for every $p \in M$,
>
> $$
> \dim T_pM = n = \dim M ,
> $$
>
> the same at every point, and independent of the chart used to compute it.

^thm-24-8

> [!proof]+ Proof
> *(The last clause of the basis theorem, recorded as a theorem in its own right.)* Any chart $(U, \varphi)$ at $p$ has $n$ coordinate functions ([[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|Def. §24.1]]), and by Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]] the $n$ derivations $\partial/\partial x^i|_p$ form a basis of $T_pM$. A different chart gives a different basis, but every basis of a finite-dimensional vector space has the same number of elements ([[§6 Dimension#^ladr-2-34|LADR 2.34]]).

^pf-24-8

*Uses:* [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|§24.5]], [[§24 Coordinate Derivations and the Basis Theorem#^def-24-1|Def. §24.1]], [[§6 Dimension#^ladr-2-34|LADR 2.34]]

This is less obvious than it looks: the space of germs $C^\infty_p(M)$ ([[§22 Tangent Spaces II꞉ Germs#^def-22-3|Def. §22.3]]) on which the derivations act is infinite-dimensional, and it is the Hadamard lemma ([[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|§24.2]]) behind the basis theorem that cuts the derivations down to exactly $n$ dimensions.

> [!theorem] Corollary §24.9: Smooth Invariance of Dimension
> If $U \subseteq \mathbb{R}^m$ and $V \subseteq \mathbb{R}^n$ are nonempty open sets and $F : U \to V$ is a diffeomorphism ([[§13 Differentiable Structures#^def-13-3|Def. §13.3]]), then $m = n$. Consequently two smooth charts ([[§15 Smooth Functions and Smooth Maps#^def-15-1|Def. §15.1]]) of a smooth manifold at the same point have targets of the same dimension.

^cor-24-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $p \in U$. By the chain rule (Theorem [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]]), $(F^{-1})_{\ast F(p)} \circ F_{\ast p}$ and $F_{\ast p} \circ (F^{-1})_{\ast F(p)}$ are the pushforwards of the identity maps, hence identities, so $F_{\ast p} : T_pU \to T_{F(p)}V$ is a linear isomorphism. By Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-8|§24.8]], applied to the open sets $U$ and $V$ with their identity charts, these spaces have dimensions $m$ and $n$, so $m = n$. For two charts $(U_1, \varphi_1)$ and $(U_2, \varphi_2)$ at $p$ with targets $\mathbb{R}^m$ and $\mathbb{R}^n$, apply this to the transition map $\varphi_2 \circ \varphi_1^{-1} : \varphi_1(U_1 \cap U_2) \to \varphi_2(U_1 \cap U_2)$, a diffeomorphism between nonempty open sets.

^pf-24-9

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-8|§24.8]], [[§13 Differentiable Structures#^def-13-3|Def. §13.3]]

> [!remark]- Connections
> - The topological statement, true but hard: [[§2 Topological Manifolds#^thm-2-1|Topological Invariance of Dimension, §2.1]].

Compare Theorem [[§2 Topological Manifolds#^thm-2-1|§2.1]]: the same statement for *homeomorphisms* is true but genuinely hard, needing algebraic topology. For diffeomorphisms the derivative linearizes the problem, and linear algebra finishes it — one of the first payoffs of having tangent spaces.
