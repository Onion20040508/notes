---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 23
tags: [differentiable-manifolds, math591]
---
← [[§22 Tangent Spaces II꞉ Germs]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§24 Coordinate Derivations and the Basis Theorem]] →

*Stage: abstract — The abstract tangent space $T_pM$ as the derivations at $p$, and the differential $F_{*p}$ that pushes them forward. The two notions of tangent space agree wherever both exist (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|§24.6]]).*

> [!remark] Remark: Two Faces of a Tangent Vector
> Lecture 9 opened with a framing that the rest of the course keeps returning to. A tangent vector has two faces — “like Janus.” It is a *velocity*, the $\gamma'(0)$ of a curve — an element of the geometric tangent space $T^{\mathrm{geo}}_pM$, which is how [[§22 Tangent Spaces II꞉ Germs#From Tangent Vectors to Derivations|§12, From Tangent Vectors to Derivations]] met it; and it is a *derivation*, an operator that eats germs and returns numbers — an element of the abstract tangent space $T_pM$, the formal definition below. Formally they are different objects, and the relation between them has to be proved (Theorem [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|§24.6]]). The same split will reappear for vector fields: as velocities attached to every point they *generate dynamics*, and as operators they lead to the *Lie derivative*.

^rem-23-1

> [!definition] Definition §23.1: Derivation at a Point
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
> where $f(p) = [f](p)$ is the evaluation of Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]].
>
> *Lee: Ch. 3, Tangent Vectors, on $C^\infty(M)$ rather than germs*

^def-23-1

> [!definition] Definition §23.2: The Abstract Tangent Space
> The **(abstract) tangent space** to $M$ at $p$ is
>
> $$
> T_pM \;=\; \{\, \text{all derivations at } p \,\},
> $$
>
> a real vector space under the pointwise operations $(D + D')[f] = D[f] + D'[f]$ and $(\lambda D)[f] = \lambda\, D[f]$. An element $D \in T_pM$ is a **tangent vector** at $p$. It is not an arrow in any ambient space but a function on germs, $D : C^\infty_p(M) \to \mathbb{R}$, so $D[f]$ is a real number for each germ $[f]$ at $p$.
>
> *Lee: Ch. 3, Tangent Vectors, via $C^\infty(M)$ (see Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-3|§23.3]])*

^def-23-2

> [!proof]+ Verification that $T_pM$ is a vector space
> $D + D'$ and $\lambda D$ are linear, being pointwise combinations of linear maps, and each satisfies the Leibniz rule because the rule is linear in $D$: for instance
>
> $$
> (D+D')([f][g]) = f(p)D[g] + g(p)D[f] + f(p)D'[g] + g(p)D'[f] = f(p)(D+D')[g] + g(p)(D+D')[f].
> $$
>
> The zero map is a derivation, and the vector space axioms hold pointwise.

^pf-def-23-2

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]

> [!remark]- Connections
> - The geometric tangent space it replaces: [[§20 Tangent Spaces I꞉ The Geometric Picture#^def-20-1|Def. §20.1]]; the two agree by [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-6|§24.6]].
> - Its dual, the cotangent space: [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|Def. §27.1]]; all the $T_pM$ together: [[§31 The Tangent Bundle#^def-31-1|the tangent bundle, Def. §31.1]].

> [!definition] Definition §23.3: The Ideal of Germs Vanishing at a Point
> The **ideal of germs vanishing at $p$** is
>
> $$
> I_p = \{\, [f] \in C_p^\infty(M) \mid f(p) = 0 \,\},
> $$
>
> the kernel of evaluation at $p$ (Definition [[§22 Tangent Spaces II꞉ Germs#^def-22-4|§22.4]]). Its **square** $I_p^2$ is the set of all finite sums $\sum_k [u_k][w_k]$ of products of two elements of $I_p$, the empty sum $0$ included.
>
> *Lee: Problem 11-4, where $I_p \subseteq C^\infty(M)$ consists of global functions*

^def-23-3

> [!theorem] Lemma §23.1: $I_p$ and $I_p^2$
> $I_p$ is an ideal of $C_p^\infty(M)$ and $I_p^2 \subseteq I_p$; both are linear subspaces.

^lem-23-1

> [!proof]+ Proof
> $I_p$ is the kernel of the algebra homomorphism of evaluation (Proposition [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]]), hence a linear subspace and an ideal: $[g][f] \in I_p$ whenever $[f] \in I_p$, since $g(p)f(p) = 0$. $I_p^2$ is closed under sums by construction and under scalars since $c\,[u][w] = [cu][w]$ with $[cu] \in I_p$; and each product $[u][w]$ lies in $I_p$, since $u(p)w(p) = 0$.

^pf-23-1

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-3|Def. §23.3]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]]

> [!theorem] Lemma §23.2: First Properties of Derivations
> Let $D$ be a derivation at $p$, and $I_p$, $I_p^2$ as in Definition [[§23 Derivations and the Abstract Tangent Space#^def-23-3|§23.3]].
> 1. $D$ annihilates constants: if $c \in \mathbb{R}$ and $\underline{c}$ denotes the germ of the constant function $c$, then $D[\underline{c}] = 0$. Consequently $D[f] = D\big[f - \underline{f(p)}\big]$, so $D$ is determined by its values on $I_p$.
> 2. $D$ annihilates products of vanishing germs: if $[f], [g] \in I_p$, then $D([f][g]) = 0$. Consequently $D$ vanishes on all of $I_p^2$.
>
> *Lee: Lemmas 3.1 and 3.4*

^lem-23-2

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

^pf-23-2

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§23 Derivations and the Abstract Tangent Space#^def-23-3|Def. §23.3]]

Both parts were set as an exercise in Lecture 9, where Uribe noted that (2) is “a very simple consequence of the product rule” and is part of a problem on Assignment 3, which introduces the ideal $I_p$ under that name. In commutative algebra the same ideal is written $\mathfrak{m}_p$, the notation used in the [[§24 Coordinate Derivations and the Basis Theorem#^rem-24-3|remark]] at the end of [[§24 Coordinate Derivations and the Basis Theorem|§12, Coordinate Derivations and the Basis Theorem]].

> [!remark] Remark
> Uribe listed exactly these two as what must be shown before the [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|basis theorem]], and deferred them to the following lecture. They are the entire reason the [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3|Taylor–Hadamard]] expansion collapses: the constant term dies by (1), the quadratic remainder dies by (2), and only the linear term survives.

^rem-23-2

> [!theorem] Proposition §23.3: Germ Derivations and Global Derivations
> Lee defines $T_pM$ as the space of derivations of $C^\infty(M)$ at $p$: linear maps $v : C^\infty(M) \to \mathbb{R}$ with $v(fg) = f(p)\,vg + g(p)\,vf$. For $D \in T_pM$ in the sense of Definition [[§23 Derivations and the Abstract Tangent Space#^def-23-2|§23.2]], the formula $v_D(f) = D[f]$ defines such a derivation, and $D \mapsto v_D$ is a linear isomorphism between the two spaces.
>
> *Lee: Ch. 3, with Propositions 2.25 and 3.8*

^prop-23-3

> [!proof]+ Proof, granting smooth bump functions
> Taking germs is an algebra homomorphism $C^\infty(M) \to C_p^\infty(M)$ compatible with evaluation at $p$, so $v_D$ is a derivation, and $D \mapsto v_D$ is linear. Both remaining steps use a *bump function*: for an open $U \ni p$, a smooth $\psi : M \to [0,1]$ supported in $U$ with $\psi \equiv 1$ near $p$ (Lee, Proposition 2.25; these notes do not construct one). *Injective:* every germ $[f]$, with $f$ defined on $U$, has the global representative $\psi f$, extended by zero; so if $v_D = 0$ then $D[f] = v_D(\psi f) = 0$ for every germ. *Surjective:* given Lee's $v$, set $D[f] = v(\tilde f)$ for any global $\tilde f$ representing $[f]$. This is well defined because $v$ is local — if $\tilde f = \tilde g$ near $p$ then $v\tilde f = v\tilde g$ (Lee, Proposition 3.8, whose proof uses a bump function) — it is a derivation on germs, and $v_D = v$.

^pf-23-3

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§23 Derivations and the Abstract Tangent Space#^def-23-2|Def. §23.2]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]]

**Comparison with Lee.** This is where the course's algebraic route and Lee's part company. Lee works with global functions and pays for locality with bump functions: Proposition 3.8 shows a derivation of $C^\infty(M)$ only sees a function near $p$, and Proposition 3.9 identifies $T_pU$ with $T_pM$. Germs build locality into the definition, so the course needs no bump functions at all — Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]] is pure algebra. The proposition above is the bridge. Since the two spaces are isomorphic, every result about $T_pM$ in these notes transfers to Lee's, and conversely.

## Pushing Derivations Forward

*Lecture 9. Derivations can be pushed forward along smooth maps. In lecture this appeared in the middle of the proof of the basis theorem, as a “new derivation” $\tilde D$ on $\mathbb{R}^n$ built from one on $M$, and was defined properly only afterwards — “the order of my presentation is not ideal.” Here it comes first, so the proof can cite it.*

Throughout, $F : M \to N$ is a smooth map of smooth manifolds and $p \in M$. The construction has two steps: functions are pulled back, and derivations, being linear functionals on functions, are pushed forward by duality.

> [!definition] Definition §23.4: Pullback of Germs
> Let $F : M \to N$ be a smooth map between smooth manifolds, and $p \in M$, so that $F(p)$ is a point of $N$. Let $[g] \in C^\infty_{F(p)}(N)$ be a germ *at the point $F(p)$ of $N$*, with a representative $(g, V)$: $V \subseteq N$ is open with $F(p) \in V$, and $g : V \to \mathbb{R}$ is smooth. Then $F^{-1}(V)$ is an open neighbourhood of $p$ in $M$, and $g \circ F : F^{-1}(V) \to \mathbb{R}$ is smooth (Lemma [[§15 Smooth Functions and Smooth Maps#^lem-15-4|§15.4]]), so $(g \circ F, F^{-1}(V))$ represents a germ at $p$ on $M$. The **pullback** of germs along $F$ at $p$ is the map
>
> $$
> F_p^* : C^\infty_{F(p)}(N) \longrightarrow C^\infty_p(M), \qquad F_p^*[g] = [\,g \circ F\,],
> $$
>
> which takes a germ on $N$ at $F(p)$ to a germ on $M$ at $p$. It does not depend on the representative $(g, V)$ (Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-4|§23.4]]).
>
> *Lee: no counterpart; the course's germ-based route*

^def-23-4

> [!theorem] Proposition §23.4: Properties of the Pullback
> Let $F : M \to N$ be smooth and $p \in M$. The map $F_p^* : C^\infty_{F(p)}(N) \to C^\infty_p(M)$ is well defined, it is a homomorphism of $\mathbb{R}$-algebras, and it is compatible with evaluation: for every germ $[g] \in C^\infty_{F(p)}(N)$,
>
> $$
> \big(F_p^*[g]\big)(p) = g\big(F(p)\big).
> $$
>
> In particular $F_p^*$ maps the germs on $N$ vanishing at $F(p)$ to germs on $M$ vanishing at $p$: $F_p^*\big(I_{F(p)}\big) \subseteq I_p$.

^prop-23-4

> [!proof]+ Proof
> *Well defined.* For a representative $(g, V)$, the set $F^{-1}(V)$ is open and contains $p$ because $F$ is continuous, and $g \circ F$ is smooth there by Lemma [[§15 Smooth Functions and Smooth Maps#^lem-15-4|§15.4]]. If $(g, V)$ and $(g', V')$ represent the same germ at $F(p)$, then $g = g'$ on some open $W$ with $F(p) \in W \subseteq V \cap V'$; so $g \circ F = g' \circ F$ on the open set $F^{-1}(W) \ni p$, and the two pulled-back germs at $p$ are equal.
>
> *Algebra homomorphism.* Composition with $F$ respects the pointwise operations: $(g + h)\circ F = g \circ F + h \circ F$, $(gh) \circ F = (g\circ F)(h \circ F)$, $(\lambda g)\circ F = \lambda (g \circ F)$, and $1 \circ F = 1$.
>
> *Evaluation.* $(g \circ F)(p) = g(F(p))$ by definition of composition.

^pf-23-4

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-4|Def. §23.4]], [[§22 Tangent Spaces II꞉ Germs#^def-22-2|Def. §22.2]], [[§22 Tangent Spaces II꞉ Germs#^prop-22-4|§22.4]], [[§23 Derivations and the Abstract Tangent Space#^def-23-3|Def. §23.3]], [[§15 Smooth Functions and Smooth Maps#^lem-15-4|§15.4]]

> [!definition] Definition §23.5: Pushforward — the Differential
> Let $F : M \to N$ be smooth and $p \in M$, and let $D \in T_pM$ be a tangent vector at $p$ — that is, a derivation at $p$, a linear map $D : C^\infty_p(M) \to \mathbb{R}$ satisfying the Leibniz rule. The **pushforward** of $D$ along $F$ is the map
>
> $$
> F_{*p}D : C^\infty_{F(p)}(N) \longrightarrow \mathbb{R}, \qquad \big(F_{*p}D\big)[g] \;:=\; D\big(F_p^*[g]\big) = D[\,g \circ F\,],
> $$
>
> defined on germs $[g]$ at $F(p)$ on $N$: pull the germ back to $p$, then apply $D$. In one line, $F_{*p}D = D \circ F_p^*$. It is a derivation at $F(p)$, i.e. an element of $T_{F(p)}N$ (Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-5|§23.5]]). Letting $D$ vary gives the **pushforward**, or **differential**, of $F$ at $p$,
>
> $$
> F_{*p} : T_pM \longrightarrow T_{F(p)}N, \qquad D \longmapsto F_{*p}D,
> $$
>
> a map from tangent vectors at $p$ in $M$ to tangent vectors at $F(p)$ in $N$, also written $dF_p$. (Uribe: “the awkward notation $F_{*p}$.”) So $F_{*p}$ acts on derivations; its value $F_{*p}D$ is again a derivation, which acts on germs at $F(p)$.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^def-23-5

![[m591-12-3.svg]]

![[m591-12-4.svg]]
*Above, the definition as a diagram: $F_{*p}D = D \circ F_p^*$, a derivation at $F(p)$ obtained by first pulling the germ back to $p$ and then applying $D$. Below, the directions. Points move forward along $F$; functions move backward, since a function on $N$ composed with $F$ is a function on $M$; and derivations, being dual to functions, reverse the arrow once more and move forward again.*

> [!remark]- Connections
> - Pushforward as the transpose of pullback: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]]; 591's version, [[§17 Linear Algebra Toolkit#^def-17-2|Def. §17.2]].
> - On open subsets of Euclidean space it is the Jacobian: [[§25 The Differential in Coordinates#^prop-25-5|§25.5]]; the calculus differential, [[§8 The Differential#^def-8-1|452 Def. §8.1]].

> [!theorem] Proposition §23.5: The Differential Is a Linear Map of Abstract Tangent Spaces
> For every $D \in T_pM$, $F_{*p}D$ is a derivation at $F(p)$; and $F_{*p} : T_pM \to T_{F(p)}N$ is linear.
>
> *Lee: Ch. 3, The Differential of a Smooth Map*

^prop-23-5

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

^pf-23-5

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Def. §23.5]], [[§23 Derivations and the Abstract Tangent Space#^def-23-1|Def. §23.1]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-4|§23.4]]

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

The board justified the derivation property with “since $F_p^*$ is a ring morphism.” That is one of the two facts used, and not quite enough on its own: the Leibniz rule *at $F(p)$* needs the coefficients $g(F(p))$ and $h(F(p))$, and these appear only because pullback is compatible with evaluation, $(g \circ F)(p) = g(F(p))$ — the third equality above. It is automatic here, but it is a separate property from multiplicativity, and it is the one that moves the base point from $p$ to $F(p)$.

> [!theorem] Theorem §23.6: The Chain Rule
> If $F : M \to N$ and $G : N \to P$ are smooth and $p \in M$, then
>
> $$
> (G \circ F)_{*p} = G_{*F(p)} \circ F_{*p} : T_pM \to T_{G(F(p))}P, \qquad (\mathrm{id}_M)_{*p} = \mathrm{id}_{T_pM} .
> $$
>
> *Lee: Proposition 3.6(b)*

^thm-23-6

> [!proof]+ Proof
> *(Lecture 10: “the proof of the chain rule is one line” — pullbacks compose in the opposite order, because composition is associative. The dualization that follows was set as an exercise, “use this to conclude the proof”; it is filled in.)* Pullback reverses composition: $(G\circ F)_p^* = F_p^* \circ G_{F(p)}^*$, since $g \circ (G \circ F) = (g \circ G) \circ F$. Hence for $D \in T_pM$ and a germ $[g]$ at $G(F(p))$,
>
> $$
> \big((G\circ F)_{*p}D\big)[g] = D\big(F_p^*\, G_{F(p)}^*[g]\big) = \big(F_{*p}D\big)\big(G_{F(p)}^*[g]\big) = \big(G_{*F(p)}\,F_{*p}D\big)[g].
> $$
>
> The identity pulls back every germ to itself, so it pushes every derivation to itself.

^pf-23-6

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^def-23-4|Def. §23.4]], [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Def. §23.5]]

![[m591-12-5.svg]]
*The upper row is the composite of maps; the lower row says its differential is the composite of the differentials. In coordinates (Corollary [[§25 The Differential in Coordinates#^cor-25-3|§25.3]]) it becomes the multiplication of Jacobian matrices — the chain rule of calculus, now as a statement about manifolds.*

> [!remark]- Connections
> - The chain rule of calculus: [[Multivariable Chain Rule|452 §10.2 (Multivariable Chain Rule)]].
> - Duals compose in the opposite order, $(ST)' = T'S'$: [[§12 Duality#^ladr-3-120|LADR 3.120]]; 591's version, [[§17 Linear Algebra Toolkit#^prop-17-4|§17.4]].

**Lecture 10.** Uribe stated this as the Chain Rule and proved the pullback identity $(G \circ F)_p^* = F_p^* \circ G_{F(p)}^*$ on the board — “see, you know that this is the right point of view when proofs become one line” — leaving the dualization as an exercise; the displayed computation above is that exercise. Pullbacks compose in the *opposite* order, so pushforwards, being their duals, compose in the *same* order as the maps. (The theorem appeared here, ahead of the lecture, because the two results below depend on it.)

> [!theorem] Corollary §23.7: Diffeomorphisms Induce Isomorphisms
> If $\Phi : M \to N$ is a diffeomorphism, then $\Phi_{*p} : T_pM \to T_{\Phi(p)}N$ is a linear isomorphism, with inverse $(\Phi^{-1})_{*\Phi(p)}$.
>
> *Lee: Proposition 3.6(d)*

^cor-23-7

> [!proof]+ Proof
> Apply Proposition [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]] to $\Phi^{-1} \circ \Phi = \mathrm{id}_M$ and $\Phi \circ \Phi^{-1} = \mathrm{id}_N$.

^pf-23-7

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-5|§23.5]], [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]

> [!theorem] Lemma §23.8: Open Subsets Have the Same Abstract Tangent Spaces
> Let $U \subseteq M$ be open with $p \in U$, and $\iota : U \hookrightarrow M$ the inclusion. Then $\iota_p^* : C^\infty_p(M) \to C^\infty_p(U)$ is restriction of germs, an isomorphism of $\mathbb{R}$-algebras, and consequently $\iota_{*p} : T_pU \to T_pM$ is a linear isomorphism. We use it to identify $T_pU = T_pM$.
>
> *Lee: Proposition 3.9*

^lem-23-8

> [!proof]+ Proof
> Restriction is well defined and an algebra homomorphism by Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-4|§23.4]]. It is surjective because a germ at $p$ on $U$ has a representative defined on an open subset of $U$, which is open in $M$ and so already represents a germ on $M$; and injective because if $f|_U$ and $g|_U$ agree near $p$ then $f$ and $g$ agree near $p$. A derivation on one algebra corresponds to exactly one on the other by composing with this isomorphism, so $\iota_{*p}$ is a bijection; it is linear by Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-5|§23.5]].

^pf-23-8

*Uses:* [[§23 Derivations and the Abstract Tangent Space#^prop-23-4|§23.4]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-5|§23.5]], [[§22 Tangent Spaces II꞉ Germs#^def-22-3|Def. §22.3]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

> [!theorem] Proposition §23.9: Charts Are Diffeomorphisms
> If $(U, \varphi)$ is a smooth chart of $M$, then $\varphi : U \to \varphi(U)$ is a diffeomorphism. Consequently, for every $p \in U$,
>
> $$
> T_pM \;=\; T_pU \xrightarrow[\ \cong\ ]{\ \varphi_{*p}\ } T_{\varphi(p)}\,\varphi(U)
> $$
>
> is a linear isomorphism of abstract tangent spaces.

^prop-23-9

> [!proof]+ Proof
> In the charts $(U,\varphi)$ on $U$ and $(\varphi(U), \mathrm{id})$ on $\varphi(U)$, both $\varphi$ and $\varphi^{-1}$ have coordinate representation the identity, so both are smooth (Definition [[§15 Smooth Functions and Smooth Maps#^def-15-3|§15.3]]). The isomorphism is then Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]] followed by Corollary [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]].

^pf-23-9

*Uses:* [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]], [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]]

> [!remark] Remark: The Chart Pushforward
> This is the $\tilde D$ of the lecture: for $D \in T_pM$, $\tilde D = \varphi_{*p}D$ acts by $\tilde D[g] = D[g \circ \varphi]$, identifying tangent vectors on $M$ with derivations at a point of an open subset of $\mathbb{R}^n$. Everything about the abstract tangent space $T_pM$ can therefore be settled in $\mathbb{R}^n$, which is how the basis theorem is proved.

^rem-23-3
