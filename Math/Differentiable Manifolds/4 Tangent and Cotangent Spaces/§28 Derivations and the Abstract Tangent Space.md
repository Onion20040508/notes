---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 28
tags: [differentiable-manifolds, math591]
---
← [[§27 Germs]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§29 Coordinate Derivations and the Basis Theorem]] →

*Stage: abstract — The abstract tangent space $T_pM$ as the derivations at $p$, and the differential $F_{\ast p}$ that pushes them forward. The two notions of tangent space agree wherever both exist (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]).*

> [!remark] Remark: Two Faces of a Tangent Vector
> Lecture 9 opened with a framing that the rest of the course keeps returning to. A tangent vector has two faces — “like Janus.” It is a *velocity*, the $\gamma'(0)$ of a curve — an element of the geometric tangent space $T^{\mathrm{geo}}_pM$, which is how [[§25 The Geometric Tangent Space#From Tangent Vectors to Derivations|§25, From Tangent Vectors to Derivations]] met it; and it is a *derivation*, an operator that eats germs and returns numbers — an element of the abstract tangent space $T_pM$, the formal definition below. Formally they are different objects, and the relation between them has to be proved (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). The same split will reappear for vector fields: as velocities attached to every point they *generate dynamics*, and as operators they lead to the *Lie derivative*.

^rem-28-1

> [!definition] Definition §28.1: Derivation at a Point
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
> where $f(p) = [f](p)$ is the evaluation of Proposition [[§27 Germs#^prop-27-2|§27.2]].
>
> *Lee: Ch. 3, Tangent Vectors, on $C^\infty(M)$ rather than germs*

^def-28-1

> [!definition] Definition §28.2: The Abstract Tangent Space
> The **(abstract) tangent space** to $M$ at $p$ is
>
> $$
> T_pM \;=\; \{\, \text{all derivations at } p \,\},
> $$
>
> a real vector space under the pointwise operations $(D + D')[f] = D[f] + D'[f]$ and $(\lambda D)[f] = \lambda\, D[f]$. An element $D \in T_pM$ is a **tangent vector** at $p$. It is not an arrow in any ambient space but a function on germs, $D : C^\infty_p(M) \to \mathbb{R}$, so $D[f]$ is a real number for each germ $[f]$ at $p$.
>
> *Lee: Ch. 3, Tangent Vectors, via $C^\infty(M)$ (see Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-3|§28.3]])*

^def-28-2

> [!proof]+ Verification that $T_pM$ is a vector space
> What has to be shown. The set of *all* maps $C_p^\infty(M) \to \mathbb{R}$ is a real vector space under the pointwise operations $(D + D')[f] = D[f] + D'[f]$ and $(\lambda D)[f] = \lambda\, D[f]$: each vector space axiom is an identity between values at a germ $[f]$, and it holds there because it holds in $\mathbb{R}$. $T_pM$ is a subset of this space, so it is a vector space under the same operations as soon as it contains the zero map and is closed under sums and scalar multiples, i.e. as soon as $D + D'$ and $\lambda D$ are again derivations whenever $D$ and $D'$ are (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]). $D + D'$ and $\lambda D$ are linear, being pointwise combinations of linear maps, and each satisfies the Leibniz rule because the rule is linear in $D$. In detail, fix germs $[f], [g] \in C_p^\infty(M)$ and numbers $a, b \in \mathbb{R}$.
>
> *Zero.* The zero map is linear, and it satisfies the Leibniz rule since $0 = f(p) \cdot 0 + g(p) \cdot 0$.
>
> *The sum is linear.* By the definition of $D + D'$, then the linearity of $D$ and of $D'$, then the definition of $D + D'$ again:
>
> $$
> (D+D')\big(a[f] + b[g]\big) = D\big(a[f] + b[g]\big) + D'\big(a[f] + b[g]\big) = a\,D[f] + b\,D[g] + a\,D'[f] + b\,D'[g] = a\,(D+D')[f] + b\,(D+D')[g] .
> $$
>
> *The sum satisfies the Leibniz rule.* By the definition of $D + D'$, the Leibniz rules of $D$ and of $D'$ separately, regrouping the four terms, and the definition of $D + D'$ again:
>
> $$
> \begin{aligned}
> (D+D')([f][g]) &= D([f][g]) + D'([f][g]) = f(p)D[g] + g(p)D[f] + f(p)D'[g] + g(p)D'[f] \\
> &= f(p)\big(D[g] + D'[g]\big) + g(p)\big(D[f] + D'[f]\big) = f(p)(D+D')[g] + g(p)(D+D')[f].
> \end{aligned}
> $$
>
> *The scalar multiple.* By the definition of $\lambda D$ and the linearity, resp. the Leibniz rule, of $D$:
>
> $$
> (\lambda D)\big(a[f] + b[g]\big) = \lambda\big(a\,D[f] + b\,D[g]\big) = a\,(\lambda D)[f] + b\,(\lambda D)[g],
> $$
>
> $$
> (\lambda D)([f][g]) = \lambda\big(f(p)D[g] + g(p)D[f]\big) = f(p)\,(\lambda D)[g] + g(p)\,(\lambda D)[f].
> $$
>
> So $T_pM$ is a linear subspace of the space of all maps $C_p^\infty(M) \to \mathbb{R}$, and the vector space axioms hold in it pointwise.

^pf-def-28-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]

> [!remark]- Connections
> - The geometric tangent space it replaces: [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]]; the two agree by [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]].
> - Its dual, the cotangent space: [[§32 The Cotangent Space#^def-32-4|Def. §32.4]]; all the $T_pM$ together: [[§47 The Tangent Bundle#^def-47-1|the tangent bundle, Def. §47.1]].

> [!definition] Definition §28.3: The Ideal of Germs Vanishing at a Point
> The **ideal of germs vanishing at $p$** is
>
> $$
> I_p = \{\, [f] \in C_p^\infty(M) \mid f(p) = 0 \,\},
> $$
>
> the kernel of evaluation at $p$ (Definition [[§27 Germs#^def-27-3|§27.3]]).
>
> *Lee: Problem 11-4, where $I_p \subseteq C^\infty(M)$ consists of global functions*

^def-28-3

> [!definition] Definition §28.4: The Square of $I_p$
> The **square** $I_p^2$ of $I_p$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-3|Definition §28.3]]) is the set of all finite sums $\sum_k [u_k][w_k]$ of products of two elements of $I_p$, the empty sum $0$ included.
>
> *Lee: Problem 11-4, where $I_p \subseteq C^\infty(M)$ consists of global functions*

^def-28-4

> [!theorem] Lemma §28.1: $I_p$ and $I_p^2$
> $I_p$ is an ideal of $C_p^\infty(M)$ and $I_p^2 \subseteq I_p$; both are linear subspaces.

^lem-28-1

> [!proof]+ Proof
> Three things are claimed: $I_p$ is a linear subspace and an ideal; $I_p^2$ is a linear subspace; and $I_p^2 \subseteq I_p$. Throughout, evaluation $[f] \mapsto f(p)$ is an algebra homomorphism $C_p^\infty(M) \to \mathbb{R}$ (Proposition [[§27 Germs#^prop-27-2|§27.2]], Definition [[§27 Germs#^def-27-3|§27.3]]), so the value at $p$ of a sum, scalar multiple or product of germs is the sum, scalar multiple or product of the values.
>
> *$I_p$.* $I_p$ is the kernel of the algebra homomorphism of evaluation (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]]), hence a linear subspace and an ideal. Explicitly: if $[f], [g] \in I_p$ and $a, b \in \mathbb{R}$, then $(a[f] + b[g])(p) = a\,f(p) + b\,g(p) = a \cdot 0 + b \cdot 0 = 0$, so $a[f] + b[g] \in I_p$; and $[g][f] \in I_p$ whenever $[f] \in I_p$ and $[g] \in C_p^\infty(M)$ is arbitrary, since $([g][f])(p) = g(p)f(p) = g(p) \cdot 0 = 0$.
>
> *$I_p^2$ is a subspace.* It contains $0$, the empty sum (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]). It is closed under sums by construction: the sum of two finite sums of products $[u][w]$ with $[u], [w] \in I_p$ is again such a finite sum. It is closed under scalars since $c\,[u][w] = [cu][w]$ (the algebra axioms of Proposition [[§27 Germs#^prop-27-2|§27.2]]) with $[cu] \in I_p$, because $(cu)(p) = c \cdot 0 = 0$; so
>
> $$
> c \sum_k [u_k][w_k] = \sum_k [cu_k][w_k] \in I_p^2 .
> $$
>
> *$I_p^2 \subseteq I_p$.* Each product $[u][w]$ with $[u], [w] \in I_p$ lies in $I_p$, since $u(p)w(p) = 0 \cdot 0 = 0$; and $I_p$ is closed under finite sums, being a subspace. So every element $\sum_k [u_k][w_k]$ of $I_p^2$ lies in $I_p$.

^pf-28-1

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]], [[§27 Germs#^prop-27-2|§27.2]], [[§27 Germs#^def-27-3|Def. §27.3]]

> [!theorem] Lemma §28.2: First Properties of Derivations
> Let $D$ be a derivation at $p$, and $I_p$, $I_p^2$ as in Definitions [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]] and [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]].
> 1. $D$ annihilates constants: if $c \in \mathbb{R}$ and $\underline{c}$ denotes the germ of the constant function $c$, then $D[\underline{c}] = 0$. Consequently $D[f] = D\big[f - \underline{f(p)}\big]$, so $D$ is determined by its values on $I_p$.
> 2. $D$ annihilates products of vanishing germs: if $[f], [g] \in I_p$, then $D([f][g]) = 0$. Consequently $D$ vanishes on all of $I_p^2$.
>
> *Lee: Lemmas 3.1 and 3.4*

^lem-28-2

> [!proof]+ Proof
> (1) The constant function $1$ satisfies $1 \cdot 1 = 1$, so its germ satisfies $[\underline 1] = [\underline 1][\underline 1]$ (products of germs are taken on representatives, Proposition [[§27 Germs#^prop-27-2|§27.2]]), and its value at $p$ is $1$. By the Leibniz rule (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]) with $[f] = [g] = [\underline 1]$,
>
> $$
> D[\underline 1] = D\big([\underline 1][\underline 1]\big) = 1 \cdot D[\underline 1] + 1 \cdot D[\underline 1] = 2\, D[\underline 1],
> $$
>
> whence, subtracting $D[\underline 1]$ from both sides, $D[\underline 1] = 0$. For general $c$, the constant germ is the scalar multiple $[\underline c] = c\,[\underline 1]$, and linearity gives $D[\underline c] = c\, D[\underline 1] = c \cdot 0 = 0$.
>
> For the consequence, let $[f]$ be any germ. As germs, $[f] = \big[f - \underline{f(p)}\big] + \big[\underline{f(p)}\big]$, and $\big[f - \underline{f(p)}\big] \in I_p$, since its value at $p$ is $f(p) - f(p) = 0$. By linearity and the first part,
>
> $$
> D[f] = D\big[f - \underline{f(p)}\big] + D\big[\underline{f(p)}\big] = D\big[f - \underline{f(p)}\big] + 0 .
> $$
>
> So if two derivations agree on $I_p$, they agree on every germ: $D$ is determined by its values on $I_p$.
>
> (2) Immediate from the Leibniz rule: if $[f], [g] \in I_p$ then $f(p) = g(p) = 0$, so $D([f][g]) = f(p)D[g] + g(p)D[f] = 0 \cdot D[g] + 0 \cdot D[f] = 0$. A general element of $I_p^2$ is a finite sum $\sum_k [u_k][w_k]$ of such products (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-4|§28.4]]), and $D$ is linear, so
>
> $$
> D\Big(\sum_k [u_k][w_k]\Big) = \sum_k D\big([u_k][w_k]\big) = \sum_k 0 = 0 .
> $$

^pf-28-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§28 Derivations and the Abstract Tangent Space#^def-28-4|Def. §28.4]], [[§27 Germs#^prop-27-2|§27.2]]

Both parts were set as an exercise in Lecture 9, where Uribe noted that (2) is “a very simple consequence of the product rule” and is part of a problem on Assignment 3, which introduces the ideal $I_p$ under that name. In commutative algebra the same ideal is written $\mathfrak{m}_p$, the notation used in the [[§29 Coordinate Derivations and the Basis Theorem#^rem-29-3|remark]] at the end of [[§29 Coordinate Derivations and the Basis Theorem|§29, Coordinate Derivations and the Basis Theorem]].

> [!remark] Remark
> Uribe listed exactly these two as what must be shown before the [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|basis theorem]], and deferred them to the following lecture. They are the entire reason the [[§29 Coordinate Derivations and the Basis Theorem#^lem-29-3|Taylor–Hadamard]] expansion collapses: the constant term dies by (1), the quadratic remainder dies by (2), and only the linear term survives.

^rem-28-2

> [!theorem] Proposition §28.3: Germ Derivations and Global Derivations
> Lee defines $T_pM$ as the space of derivations of $C^\infty(M)$ at $p$: linear maps $v : C^\infty(M) \to \mathbb{R}$ with $v(fg) = f(p)\,vg + g(p)\,vf$. For $D \in T_pM$ in the sense of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]], the formula $v_D(f) = D[f]$ defines such a derivation, and $D \mapsto v_D$ is a linear isomorphism between the two spaces.
>
> *Lee: Ch. 3, with Propositions 2.25 and 3.8*

^prop-28-3

> [!proof]+ Proof, granting smooth bump functions
> Three things are to be shown: each $v_D$ is a derivation of $C^\infty(M)$ at $p$; $D \mapsto v_D$ is linear; and it is bijective.
>
> *$v_D$ is a derivation, and $D \mapsto v_D$ is linear.* Taking germs, $f \mapsto [f]$ (the class of the pair $(f, M)$), is an algebra homomorphism $C^\infty(M) \to C_p^\infty(M)$ compatible with evaluation at $p$: by the definition of the germ operations (Proposition [[§27 Germs#^prop-27-2|§27.2]]), with $W = M$, $[af + bg] = a[f] + b[g]$ and $[fg] = [f][g]$, and $[f](p) = f(p)$. Hence, for $f, g \in C^\infty(M)$ and $a, b \in \mathbb{R}$, by the linearity and the Leibniz rule of $D$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]),
>
> $$
> v_D(af + bg) = D\big(a[f] + b[g]\big) = a\,v_D(f) + b\,v_D(g), \qquad v_D(fg) = D\big([f][g]\big) = f(p)\,v_D(g) + g(p)\,v_D(f),
> $$
>
> so $v_D$ is a derivation in Lee's sense. And for $D, E \in T_pM$, by the pointwise operations of Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]], $v_{aD + bE}(f) = (aD + bE)[f] = a\,D[f] + b\,E[f] = a\,v_D(f) + b\,v_E(f)$ for every $f$, so $v_{aD + bE} = a\,v_D + b\,v_E$.
>
> Both remaining steps use a *bump function*: for an open $U \ni p$, a smooth $\psi : M \to [0,1]$ supported in $U$ with $\psi \equiv 1$ near $p$ (Lee, Proposition 2.25; these notes do not construct one).
>
> *Injective.* Every germ $[f]$, with $f$ defined on $U$, has the global representative $\psi f$, extended by zero. (It is smooth: on $U$ it is the product of smooth functions, on the open set $M \setminus \operatorname{supp}\psi$ it is $0$, and these two open sets cover $M$. It equals $f$ on the open set near $p$ where $\psi \equiv 1$, so $[\psi f] = [f]$.) So if $v_D = 0$ then $D[f] = D[\psi f] = v_D(\psi f) = 0$ for every germ, i.e. $D = 0$; a linear map with zero kernel is injective.
>
> *Surjective.* Given Lee's $v$, set $D[f] = v(\tilde f)$ for any global $\tilde f$ representing $[f]$; one exists by the previous paragraph. This is well defined because $v$ is local — if $\tilde f = \tilde g$ near $p$ then $v\tilde f = v\tilde g$ (Lee, Proposition 3.8, whose proof uses a bump function) — and two global representatives of the same germ agree near $p$. It is a derivation on germs: if $\tilde f$ and $\tilde g$ represent $[f]$ and $[g]$, then $a\tilde f + b\tilde g$ and $\tilde f \tilde g$ represent $a[f] + b[g]$ and $[f][g]$, so
>
> $$
> D\big(a[f] + b[g]\big) = v(a\tilde f + b\tilde g) = a\,v(\tilde f) + b\,v(\tilde g) = a\,D[f] + b\,D[g],
> $$
>
> $$
> D\big([f][g]\big) = v(\tilde f\tilde g) = \tilde f(p)\, v(\tilde g) + \tilde g(p)\, v(\tilde f) = f(p)\, D[g] + g(p)\, D[f],
> $$
>
> using $\tilde f(p) = f(p)$ and $\tilde g(p) = g(p)$. Finally $v_D = v$: a global $f$ is itself a global representative of its germ, so $v_D(f) = D[f] = v(f)$.

^pf-28-3

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§27 Germs#^prop-27-2|§27.2]]

Both steps borrowed from Lee are now in these notes: bump functions are Proposition [[§50 Vector Fields#^prop-50-4|§50.4]] (existence stated, proof deferred in lecture), the global representative of a germ is Corollary [[§50 Vector Fields#^cor-50-5|§50.5]], and locality of derivations is Lemma [[§50 Vector Fields#^lem-50-6|§50.6]] (Lecture 16).

**Comparison with Lee.** This is where the course's algebraic route and Lee's part company. Lee works with global functions and pays for locality with bump functions: Proposition 3.8 shows a derivation of $C^\infty(M)$ only sees a function near $p$, and Proposition 3.9 identifies $T_pU$ with $T_pM$. Germs build locality into the definition, so the course needs no bump functions at all — Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] is pure algebra. The proposition above is the bridge. Since the two spaces are isomorphic, every result about $T_pM$ in these notes transfers to Lee's, and conversely.

## Pushing Derivations Forward

*Lecture 9. Derivations can be pushed forward along smooth maps. In lecture this appeared in the middle of the proof of the basis theorem, as a “new derivation” $\tilde D$ on $\mathbb{R}^n$ built from one on $M$, and was defined properly only afterwards — “the order of my presentation is not ideal.” Here it comes first, so the proof can cite it.*

Throughout, $F : M \to N$ is a smooth map of smooth manifolds and $p \in M$. The construction has two steps: functions are pulled back, and derivations, being linear functionals on functions, are pushed forward by duality.

> [!definition] Definition §28.5: Pullback of Germs
> Let $F : M \to N$ be a smooth map between smooth manifolds, and $p \in M$, so that $F(p)$ is a point of $N$. Let $[g] \in C^\infty_{F(p)}(N)$ be a germ *at the point $F(p)$ of $N$*, with a representative $(g, V)$: $V \subseteq N$ is open with $F(p) \in V$, and $g : V \to \mathbb{R}$ is smooth. Then $F^{-1}(V)$ is an open neighbourhood of $p$ in $M$, and $g \circ F : F^{-1}(V) \to \mathbb{R}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), so $(g \circ F, F^{-1}(V))$ represents a germ at $p$ on $M$. The **pullback** of germs along $F$ at $p$ is the map
>
> $$
> F_p^* : C^\infty_{F(p)}(N) \longrightarrow C^\infty_p(M), \qquad F_p^*[g] = [\,g \circ F\,],
> $$
>
> which takes a germ on $N$ at $F(p)$ to a germ on $M$ at $p$. It does not depend on the representative $(g, V)$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]]).
>
> *Lee: no counterpart; the course's germ-based route*

^def-28-5

> [!theorem] Proposition §28.4: Properties of the Pullback
> Let $F : M \to N$ be smooth and $p \in M$. The map $F_p^* : C^\infty_{F(p)}(N) \to C^\infty_p(M)$ is well defined, it is a homomorphism of $\mathbb{R}$-algebras, and it is compatible with evaluation: for every germ $[g] \in C^\infty_{F(p)}(N)$,
>
> $$
> \big(F_p^*[g]\big)(p) = g\big(F(p)\big).
> $$
>
> In particular $F_p^*$ maps the germs on $N$ vanishing at $F(p)$ to germs on $M$ vanishing at $p$: $F_p^*\big(I_{F(p)}\big) \subseteq I_p$.

^prop-28-4

> [!proof]+ Proof
> *Well defined.* For a representative $(g, V)$, the set $F^{-1}(V)$ is open and contains $p$ because $F$ is continuous, and $g \circ F$ is smooth there by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]. If $(g, V)$ and $(g', V')$ represent the same germ at $F(p)$, then $g = g'$ on some open $W$ with $F(p) \in W \subseteq V \cap V'$; so $g \circ F = g' \circ F$ on the open set $F^{-1}(W) \ni p$, and the two pulled-back germs at $p$ are equal.
>
> *Algebra homomorphism.* Composition with $F$ respects the pointwise operations: $(g + h)\circ F = g \circ F + h \circ F$, $(gh) \circ F = (g\circ F)(h \circ F)$, $(\lambda g)\circ F = \lambda (g \circ F)$, and $1 \circ F = 1$, since each side takes the same value at every point $q$ (for instance $((g+h) \circ F)(q) = g(F(q)) + h(F(q))$). To pass to germs, let $(g, V)$ and $(h, V')$ represent $[g]$ and $[h]$, and let $W$ be open with $F(p) \in W \subseteq V \cap V'$, so that $[g] + [h] = [g|_W + h|_W]$ (Proposition [[§27 Germs#^prop-27-2|§27.2]]). The set $F^{-1}(W)$ is open, contains $p$, and lies in the domains of $g \circ F$ and $h \circ F$, so by the definition of the sum of germs at $p$,
>
> $$
> F_p^{\ast}\big([g] + [h]\big) = \big[(g|_W + h|_W) \circ F\big] = \big[(g \circ F)|_{F^{-1}(W)} + (h \circ F)|_{F^{-1}(W)}\big] = [g \circ F] + [h \circ F] = F_p^{\ast}[g] + F_p^{\ast}[h] .
> $$
>
> The same chain with every $+$ replaced by a product gives $F_p^{\ast}([g][h]) = F_p^{\ast}[g]\, F_p^{\ast}[h]$. For scalars, $F_p^{\ast}(\lambda[g]) = [(\lambda g) \circ F] = [\lambda (g \circ F)] = \lambda\, F_p^{\ast}[g]$, and for the unit, $F_p^{\ast}[1] = [1 \circ F] = [1]$.
>
> *Evaluation.* $(g \circ F)(p) = g(F(p))$ by definition of composition; this is the displayed formula, since the value of the germ $F_p^{\ast}[g] = [g \circ F]$ at $p$ is $(g \circ F)(p)$ (Definition [[§27 Germs#^def-27-3|§27.3]]).
>
> *In particular.* If $[g] \in I_{F(p)}$, i.e. $g(F(p)) = 0$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-3|§28.3]]), then by the evaluation formula $(F_p^{\ast}[g])(p) = g(F(p)) = 0$, so $F_p^{\ast}[g] \in I_p$.

^pf-28-4

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Def. §28.5]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§27 Germs#^prop-27-2|§27.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-3|Def. §28.3]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§27 Germs#^def-27-3|Def. §27.3]]

> [!definition] Definition §28.6: Pushforward — the Differential
> Let $F : M \to N$ be smooth and $p \in M$, and let $D \in T_pM$ be a tangent vector at $p$ — that is, a derivation at $p$, a linear map $D : C^\infty_p(M) \to \mathbb{R}$ satisfying the Leibniz rule. The **pushforward** of $D$ along $F$ is the map
>
> $$
> F_{*p}D : C^\infty_{F(p)}(N) \longrightarrow \mathbb{R}, \qquad \big(F_{*p}D\big)[g] \;:=\; D\big(F_p^*[g]\big) = D[\,g \circ F\,],
> $$
>
> defined on germs $[g]$ at $F(p)$ on $N$: pull the germ back to $p$, then apply $D$. In one line, $F_{\ast p}D = D \circ F_p^{\ast}$. It is a derivation at $F(p)$, i.e. an element of $T_{F(p)}N$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). Letting $D$ vary gives the **pushforward**, or **differential**, of $F$ at $p$,
>
> $$
> F_{*p} : T_pM \longrightarrow T_{F(p)}N, \qquad D \longmapsto F_{*p}D,
> $$
>
> a map from tangent vectors at $p$ in $M$ to tangent vectors at $F(p)$ in $N$, also written $dF_p$. (Uribe: “the awkward notation $F_{*p}$.”) So $F_{*p}$ acts on derivations; its value $F_{*p}D$ is again a derivation, which acts on germs at $F(p)$.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^def-28-6

![[m591-12-3.svg]]

![[m591-12-4.svg]]
*Above, the definition as a diagram: $F_{\ast p}D = D \circ F_p^{\ast}$, a derivation at $F(p)$ obtained by first pulling the germ back to $p$ and then applying $D$. Below, the directions. Points move forward along $F$; functions move backward, since a function on $N$ composed with $F$ is a function on $M$; and derivations, being dual to functions, reverse the arrow once more and move forward again.*

> [!remark]- Connections
> - Pushforward as the transpose of pullback: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]]; 591's version, [[§21 Linear Algebra Toolkit#^def-21-3|Def. §21.3]].
> - On open subsets of Euclidean space it is the Jacobian: [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]; the calculus differential, [[§10 The Differential#^def-10-1|452 Def. §10.1]].

> [!theorem] Proposition §28.5: The Differential Is a Linear Map of Abstract Tangent Spaces
> For every $D \in T_pM$, $F_{*p}D$ is a derivation at $F(p)$; and $F_{*p} : T_pM \to T_{F(p)}N$ is linear.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^prop-28-5

> [!proof]+ Proof
> Two claims: for fixed $D$, the map $F_{\ast p}D : C^\infty_{F(p)}(N) \to \mathbb{R}$ is a derivation at $F(p)$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-1|§28.1]]), i.e. linear and satisfying the Leibniz rule with the values at $F(p)$; and $D \mapsto F_{\ast p}D$ is linear.
>
> *$F_{\ast p}D$ is linear.* $F_{\ast p}D = D \circ F_p^{\ast}$ is linear, as a composite of linear maps: $F_p^{\ast}$ is linear by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]], and $D$ is linear. Explicitly, for germs $[g], [h]$ at $F(p)$ and $a, b \in \mathbb{R}$, by Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]], the linearity of $F_p^{\ast}$, the linearity of $D$, and Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] again,
>
> $$
> \big(F_{\ast p}D\big)\big(a[g] + b[h]\big) = D\big(F_p^{\ast}(a[g] + b[h])\big) = D\big(a\,F_p^{\ast}[g] + b\,F_p^{\ast}[h]\big) = a\,D\big(F_p^{\ast}[g]\big) + b\,D\big(F_p^{\ast}[h]\big) = a\,\big(F_{\ast p}D\big)[g] + b\,\big(F_{\ast p}D\big)[h] .
> $$
>
> *Leibniz rule.* Let $[g],[h] \in C^\infty_{F(p)}(N)$. Then
>
> $$
> \begin{aligned}
> \big(F_{\ast p}D\big)\big([g][h]\big)
> &= D\big(F_p^{\ast}([g][h])\big) = D\big(F_p^{\ast}[g]\cdot F_p^{\ast}[h]\big) \\
> &= \big(F_p^{\ast}[g]\big)(p)\, D\big(F_p^{\ast}[h]\big) + \big(F_p^{\ast}[h]\big)(p)\, D\big(F_p^{\ast}[g]\big) \\
> &= g(F(p))\,\big(F_{\ast p}D\big)[h] + h(F(p))\,\big(F_{\ast p}D\big)[g],
> \end{aligned}
> $$
>
> using, in turn, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]], that $F_p^{\ast}$ is multiplicative, the Leibniz rule for $D$ at $p$ applied to the two germs $F_p^{\ast}[g], F_p^{\ast}[h] \in C^\infty_p(M)$, and compatibility with evaluation, $(F_p^{\ast}[g])(p) = g(F(p))$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]]), together with Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] once more. So $F_{\ast p}D$ is a derivation at $F(p)$.
>
> *Linearity in $D$.* Linearity in $D$ holds because $(D + \lambda D')\circ F_p^{\ast} = D \circ F_p^{\ast} + \lambda\, D' \circ F_p^{\ast}$: for every germ $[g]$ at $F(p)$, by Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] and the pointwise operations on derivations (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]),
>
> $$
> \big(F_{\ast p}(D + \lambda D')\big)[g] = (D + \lambda D')\big(F_p^{\ast}[g]\big) = D\big(F_p^{\ast}[g]\big) + \lambda\, D'\big(F_p^{\ast}[g]\big) = \big(F_{\ast p}D + \lambda\, F_{\ast p}D'\big)[g] .
> $$
>
> The two derivations agree on every germ, so $F_{\ast p}(D + \lambda D') = F_{\ast p}D + \lambda\, F_{\ast p}D'$.

^pf-28-5

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-1|Def. §28.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

Every object of this section, with what it is and where it lives. The rows go in order of the diagram above: germs travel backwards, from $N$ to $M$, and derivations forwards, from $M$ to $N$.

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

The board justified the derivation property with “since $F_p^{\ast}$ is a ring morphism.” That is one of the two facts used, and not quite enough on its own: the Leibniz rule *at $F(p)$* needs the coefficients $g(F(p))$ and $h(F(p))$, and these appear only because pullback is compatible with evaluation, $(g \circ F)(p) = g(F(p))$ — the third equality above. It is automatic here, but it is a separate property from multiplicativity, and it is the one that moves the base point from $p$ to $F(p)$.

> [!theorem] Theorem §28.6: The Chain Rule
> If $F : M \to N$ and $G : N \to P$ are smooth and $p \in M$, then
>
> $$
> (G \circ F)_{*p} = G_{*F(p)} \circ F_{*p} : T_pM \to T_{G(F(p))}P, \qquad (\mathrm{id}_M)_{*p} = \mathrm{id}_{T_pM} .
> $$
>
> *Lee: Proposition 3.6(b)*

^thm-28-6

> [!proof]+ Proof
> *(Lecture 10: “the proof of the chain rule is one line” — pullbacks compose in the opposite order, because composition is associative. The dualization that follows was set as an exercise, “use this to conclude the proof”; it is filled in.)* $G \circ F$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), so $(G \circ F)_{\ast p}$ is defined. Two linear maps $T_pM \to T_{G(F(p))}P$ are equal if they agree at every $D$, and two derivations at $G(F(p))$ are equal if they agree at every germ; so fix $D \in T_pM$ and a germ $[g]$ at $G(F(p))$.
>
> *Pullback reverses composition:* $(G\circ F)_p^{\ast} = F_p^{\ast} \circ G_{F(p)}^{\ast}$, since $g \circ (G \circ F) = (g \circ G) \circ F$. Indeed, by Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]] applied three times (to $G \circ F$ at $p$, to $F$ at $p$, and to $G$ at $F(p)$),
>
> $$
> (G\circ F)_p^{\ast}[g] = \big[g \circ (G \circ F)\big] = \big[(g \circ G) \circ F\big] = F_p^{\ast}[g \circ G] = F_p^{\ast}\big(G_{F(p)}^{\ast}[g]\big).
> $$
>
> *Dualization.* Hence
>
> $$
> \big((G\circ F)_{\ast p}D\big)[g] = D\big((G\circ F)_p^{\ast}[g]\big) = D\big(F_p^{\ast}\, G_{F(p)}^{\ast}[g]\big) = \big(F_{\ast p}D\big)\big(G_{F(p)}^{\ast}[g]\big) = \big(G_{\ast F(p)}\,F_{\ast p}D\big)[g].
> $$
>
> The first equality is Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] for $G \circ F$ at $p$; the second is the reversal just shown; the third is Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] for $F$ at $p$, applied to the germ $G_{F(p)}^{\ast}[g]$ at $F(p)$; the fourth is Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]] for $G$ at $F(p)$, applied to the derivation $F_{\ast p}D \in T_{F(p)}N$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]).
>
> *Identity.* The identity pulls back every germ to itself, $(\mathrm{id}_M)_p^{\ast}[f] = [f \circ \mathrm{id}_M] = [f]$, so it pushes every derivation to itself: $\big((\mathrm{id}_M)_{\ast p}D\big)[f] = D\big((\mathrm{id}_M)_p^{\ast}[f]\big) = D[f]$ for every germ $[f]$ at $p$, i.e. $(\mathrm{id}_M)_{\ast p}D = D$.

^pf-28-6

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Def. §28.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]

![[m591-12-5.svg]]
*The upper row is the composite of maps; the lower row says its differential is the composite of the differentials. In coordinates (Corollary [[§30 The Differential in Coordinates#^cor-30-3|§30.3]]) it becomes the multiplication of Jacobian matrices — the chain rule of calculus, now as a statement about manifolds.*

> [!remark]- Connections
> - The chain rule of calculus: [[Multivariable Chain Rule|452 §12.2 (Multivariable Chain Rule)]].
> - Duals compose in the opposite order, $(ST)' = T'S'$: [[§12 Duality#^ladr-3-120|LADR 3.120]]; 591's version, [[§21 Linear Algebra Toolkit#^prop-21-4|§21.4]].

**Lecture 10.** Uribe stated this as the Chain Rule and proved the pullback identity $(G \circ F)_p^{\ast} = F_p^{\ast} \circ G_{F(p)}^{\ast}$ on the board — “see, you know that this is the right point of view when proofs become one line” — leaving the dualization as an exercise; the displayed computation above is that exercise. Pullbacks compose in the *opposite* order, so pushforwards, being their duals, compose in the *same* order as the maps. (The theorem appeared here, ahead of the lecture, because the two results below depend on it.)

> [!theorem] Corollary §28.7: Diffeomorphisms Induce Isomorphisms
> If $\Phi : M \to N$ is a diffeomorphism, then $\Phi_{*p} : T_pM \to T_{\Phi(p)}N$ is a linear isomorphism, with inverse $(\Phi^{-1})_{*\Phi(p)}$.
>
> *Lee: Proposition 3.6(d)*

^cor-28-7

> [!proof]+ Proof
> Since $\Phi$ is a diffeomorphism, $\Phi$ and $\Phi^{-1}$ are both smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]), so their pushforwards are defined, and they are linear by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]. Apply Proposition [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]] to $\Phi^{-1} \circ \Phi = \mathrm{id}_M$ at $p$ and to $\Phi \circ \Phi^{-1} = \mathrm{id}_N$ at $\Phi(p)$, using $\Phi^{-1}(\Phi(p)) = p$:
>
> $$
> (\Phi^{-1})_{\ast \Phi(p)} \circ \Phi_{\ast p} = (\Phi^{-1} \circ \Phi)_{\ast p} = (\mathrm{id}_M)_{\ast p} = \mathrm{id}_{T_pM}, \qquad
> \Phi_{\ast p} \circ (\Phi^{-1})_{\ast \Phi(p)} = (\Phi \circ \Phi^{-1})_{\ast \Phi(p)} = (\mathrm{id}_N)_{\ast \Phi(p)} = \mathrm{id}_{T_{\Phi(p)}N} .
> $$
>
> So $\Phi_{\ast p}$ has the two-sided inverse $(\Phi^{-1})_{\ast \Phi(p)}$; a linear bijection is a linear isomorphism.

^pf-28-7

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]

> [!theorem] Lemma §28.8: Open Subsets Have the Same Abstract Tangent Spaces
> Let $U \subseteq M$ be open with $p \in U$, and $\iota : U \hookrightarrow M$ the inclusion. Then $\iota_p^* : C^\infty_p(M) \to C^\infty_p(U)$ is restriction of germs, an isomorphism of $\mathbb{R}$-algebras, and consequently $\iota_{*p} : T_pU \to T_pM$ is a linear isomorphism. We use it to identify $T_pU = T_pM$.
>
> *Lee: Proposition 3.9*

^lem-28-8

> [!proof]+ Proof
> The inclusion $\iota$ is smooth (in a chart of $M$ restricted to an open subset of $U$, its coordinate representation is the identity), and by Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-5|§28.5]] it pulls back the germ of $(f, V)$ to $\iota_p^{\ast}[f] = [f \circ \iota] = [f|_{U \cap V}]$: restriction of germs.
>
> *Algebra homomorphism.* Restriction is well defined and an algebra homomorphism by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]], and it is compatible with evaluation: $(\iota_p^{\ast}[f])(p) = f(p)$.
>
> *Surjective.* It is surjective because a germ at $p$ on $U$ has a representative $(g, V')$ defined on an open subset $V'$ of $U$, which is open in $M$ ($U$ being open in $M$) and so already represents a germ on $M$; and $\iota_p^{\ast}[g] = [g|_{V' \cap U}] = [g|_{V'}]$, the given germ, since $V' \subseteq U$.
>
> *Injective.* It is injective because if $f|_U$ and $g|_U$ agree near $p$ then $f$ and $g$ agree near $p$: they agree on an open $W \ni p$ of $U$, and $W$ is also open in $M$, so $[f] = [g]$ in $C^\infty_p(M)$ (Definition [[§27 Germs#^def-27-1|§27.1]]). A bijective algebra homomorphism is an algebra isomorphism; write $\rho = (\iota_p^{\ast})^{-1}$ for its inverse, again an algebra homomorphism compatible with evaluation.
>
> *The derivations.* A derivation on one algebra corresponds to exactly one on the other by composing with this isomorphism. By Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]], $\iota_{\ast p}D = D \circ \iota_p^{\ast}$ for $D \in T_pU$. In the other direction, for $E \in T_pM$ the composite $E \circ \rho$ is a derivation at $p$ on $U$: it is linear, as a composite of linear maps, and for germs $[f], [g]$ on $U$, since $\rho$ is multiplicative and compatible with evaluation,
>
> $$
> (E \circ \rho)\big([f][g]\big) = E\big(\rho[f]\, \rho[g]\big) = f(p)\, E(\rho[g]) + g(p)\, E(\rho[f]) .
> $$
>
> The two assignments are mutually inverse: $\iota_{\ast p}(E \circ \rho) = E \circ \rho \circ \iota_p^{\ast} = E$ and $(\iota_{\ast p}D) \circ \rho = D \circ \iota_p^{\ast} \circ \rho = D$. So $\iota_{\ast p}$ is a bijection; it is linear by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]].

^pf-28-8

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^prop-28-4|§28.4]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§27 Germs#^def-27-2|Def. §27.2]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Def. §28.5]], [[§27 Germs#^def-27-1|Def. §27.1]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]]

> [!theorem] Proposition §28.9: Charts Are Diffeomorphisms
> If $(U, \varphi)$ is a smooth chart of $M$, then $\varphi : U \to \varphi(U)$ is a diffeomorphism. Consequently, for every $p \in U$,
>
> $$
> T_pM \;=\; T_pU \xrightarrow[\ \cong\ ]{\ \varphi_{*p}\ } T_{\varphi(p)}\,\varphi(U)
> $$
>
> is a linear isomorphism of abstract tangent spaces.

^prop-28-9

> [!proof]+ Proof
> *$\varphi$ is a diffeomorphism.* $\varphi : U \to \varphi(U)$ is a bijection, and a homeomorphism, so $\varphi$ and $\varphi^{-1}$ are continuous. In the charts $(U,\varphi)$ on $U$ and $(\varphi(U), \mathrm{id})$ on $\varphi(U)$, both $\varphi$ and $\varphi^{-1}$ have coordinate representation the identity:
>
> $$
> \mathrm{id} \circ \varphi \circ \varphi^{-1} = \mathrm{id}_{\varphi(U)}, \qquad \varphi \circ \varphi^{-1} \circ \mathrm{id}^{-1} = \mathrm{id}_{\varphi(U)},
> $$
>
> which is smooth; so both are smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]), and $\varphi$ is a smooth bijection with smooth inverse, a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]).
>
> *The isomorphism.* The isomorphism is then Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]] followed by Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]: the first identifies $T_pM$ with $T_pU$ by the linear isomorphism $\iota_{\ast p}$; the second, applied to the diffeomorphism $\Phi = \varphi : U \to \varphi(U)$, says that $\varphi_{\ast p} : T_pU \to T_{\varphi(p)}\varphi(U)$ is a linear isomorphism with inverse $(\varphi^{-1})_{\ast \varphi(p)}$.

^pf-28-9

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]

> [!remark] Remark: The Chart Pushforward
> This is the $\tilde D$ of the lecture: for $D \in T_pM$, $\tilde D = \varphi_{*p}D$ acts by $\tilde D[g] = D[g \circ \varphi]$, identifying tangent vectors on $M$ with derivations at a point of an open subset of $\mathbb{R}^n$. Everything about the abstract tangent space $T_pM$ can therefore be settled in $\mathbb{R}^n$, which is how the basis theorem is proved.

^rem-28-3
