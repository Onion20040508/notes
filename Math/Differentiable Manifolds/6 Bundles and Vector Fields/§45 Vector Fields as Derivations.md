---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 45
tags: [differentiable-manifolds, math591]
---
← [[§44 The Operator d and Pullbacks of One-Forms]] · ↑ [[· 6 Bundles and Vector Fields]]

*Stage: fields — Vector fields acting on functions: derivations of $C^\infty(M)$, local operators, and the bump functions that connect global and local.*

*Lecture 15: “now we want to start a big chapter, new chapter, and now it is on vector fields.” References: Lee Ch. 8.*

> [!remark] Remark: Two Faces of a Vector Field
> “Just as tangent vectors, fields have a double life.” Tangent vectors were defined as derivations and then shown to be velocities of curves ([[§29 Tangent Vectors as Velocities of Curves|§29]]). Vector fields likewise have two faces: *operators on functions*, studied first because it continues the definition by derivations; and *dynamics on $M$* — integral curves, the trajectories that follow the field, to come later.

^rem-45-1

> [!definition] Definition §45.1: Derivation of $C^\infty(M)$
> A **derivation** of $C^\infty(M)$ is an $\mathbb{R}$-linear map $D : C^\infty(M) \to C^\infty(M)$ satisfying the product rule
>
> $$
> D(fg) = f\, Dg + g\, Df \qquad \text{for all } f, g \in C^\infty(M).
> $$
>
> Compare a derivation *at a point* ([[§26 Derivations and the Abstract Tangent Space#^def-26-1|Definition §26.1]]), which takes values in $\mathbb{R}$ and acts on [[§25 Germs#^def-25-2|germs]].
>
> *Lee: Ch. 8, Vector Fields as Derivations*

^def-45-1

> [!theorem] Lemma §45.1: A Vector Field Is a Derivation
> For $X \in \mathfrak{X}(M)$ ([[§43 Vector Fields and One-Forms#^def-43-2|Def. §43.2]]) and $f \in C^\infty(M)$, the function $D_Xf : p \mapsto X_p[f]$ is smooth, and $D_X : C^\infty(M) \to C^\infty(M)$ is a [[§45 Vector Fields as Derivations#^def-45-1|derivation]]. In a chart, $D_Xf = \sum_j X^j\, \partial f/\partial x^j$. (Lee writes $Xf$ for $D_Xf$.)

^lem-45-1

> [!proof]+ Proof
> *(Lecture 15: linearity and the product rule are “an immediate consequence of the corresponding properties for tangent vectors”, applied at each point. Smoothness of $D_Xf$, which the lecture did not address, is filled in.)* In a chart, $X_p[f] = \sum_j X^j(p)\, \partial f/\partial x^j(p)$ by [[§43 Vector Fields and One-Forms#^prop-43-1|Proposition §43.1]], a sum of products of smooth functions. At each $p$, $X_p[fg] = f(p)\, X_p[g] + g(p)\, X_p[f]$ because $X_p$ is a derivation at $p$; that is the product rule for $D_X$, and linearity is the same.

^pf-45-1

*Uses:* [[§45 Vector Fields as Derivations#^def-45-1|Def. §45.1]], [[§43 Vector Fields and One-Forms#^def-43-2|Def. §43.2]], [[§43 Vector Fields and One-Forms#^prop-43-1|§43.1]], [[§26 Derivations and the Abstract Tangent Space#^def-26-1|Def. §26.1]]

The goal of this section is the converse of the lemma: every derivation of $C^\infty(M)$ comes from a vector field ([[§45 Vector Fields as Derivations#^prop-45-4|Proposition §45.4]], at the end). Tangent vectors act on germs, which only see a neighbourhood of a point, while a derivation of $C^\infty(M)$ acts on functions on all of $M$. The bridge is locality ([[§45 Vector Fields as Derivations#^lem-45-3|Lemma §45.3]]), and its proof needs bump functions, so these come first.

> [!definition] Definition §45.2: Local Operator
> An operator $D : C^\infty(M) \to C^\infty(M)$ is **local** if for every open $U \subseteq M$ and all $f, g \in C^\infty(M)$,
>
> $$
> f|_U = g|_U \quad \Longrightarrow \quad (Df)|_U = (Dg)|_U .
> $$

^def-45-2

“Even though $D$ a priori is defined on functions on $M$, it's actually going to be given by local data”: knowing $f$ on $U$ determines $Df$ on $U$.

> [!definition] Definition §45.3: Support and Bump Function
> The **support** of a function $\chi : M \to \mathbb{R}$ is the *[[§7 Interior and Closure#^def-7-1|closure]]* of the set where it is nonzero,
>
> $$
> \operatorname{supp}\chi = \overline{\{ q \in M : \chi(q) \neq 0 \}} ,
> $$
>
> and $C^\infty_0(M)$ is the set of smooth functions with [[§15 Compact Spaces#^def-15-2|compact]] support. A **bump function at $p$** is a $\chi \in C^\infty_0(M)$ with $\chi \equiv 1$ on a neighbourhood of $p$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-45-3

“It's a technical term, and it's not a joke”: the graph is a plateau, equal to $1$ near $p$ and dying off to $0$ outside a compact set — “smooth, but not analytic”, since an analytic function equal to $1$ on an open set would equal $1$ on the whole connected domain.

![[m591-45-1.svg]]
*A bump function, drawn over a one-dimensional slice of $M$ (the graph is the plateau of Uribe's picture, in cross-section). It equals $1$ on a neighbourhood of $p$, is smooth everywhere, and vanishes outside its support, which is compact and lies inside the given open set $U$. This one is built from $h(t) = e^{-1/t}$ for $t > 0$, $h(t) = 0$ for $t \le 0$, as $\chi(x) = h(b - |x|)/\big(h(b - |x|) + h(|x| - a)\big)$, which is $1$ for $|x| \le a$ and $0$ for $|x| \ge b$.*

**Transcription note.** Page 41 of the handwritten notes defines $\operatorname{supp}(\chi) = \{q \in M : \chi(q) \neq 0\}$; the support is the *closure* of that set, as Uribe said (“and then you take the closure of that”). Without the closure, the support of a bump function would not be compact.

> [!theorem] Proposition §45.2: Bump Functions Exist
> For every open $U \subseteq M$ and every $p \in U$ there is a [[§45 Vector Fields as Derivations#^def-45-3|bump function]] $\chi$ at $p$ with $\operatorname{supp}\chi \subseteq U$.
>
> *Lee: Proposition 2.25*

^prop-45-2

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15, to be proved next week — “the week before the exam”, so Uribe will prove “technical things that you will not be using in homework.” “The existence is not so obvious, but it's true.”

^pf-45-2

> [!remark]- Connections
> - The flat function $e^{-1/x^2}$, smooth but not its Taylor series: [[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]].
> - Bump functions were already granted (Lee, Proposition 2.25) in [[§26 Derivations and the Abstract Tangent Space#^prop-26-3|Germ Derivations and Global Derivations, §26.3]].

> [!theorem] Lemma §45.3: Derivations Are Local
> Every [[§45 Vector Fields as Derivations#^def-45-1|derivation]] of $C^\infty(M)$ is a [[§45 Vector Fields as Derivations#^def-45-2|local operator]].

^lem-45-3

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15; the proof “uses the existence of bump functions” ([[§45 Vector Fields as Derivations#^prop-45-2|Proposition §45.2]], above) and is to come.

^pf-45-3

*Uses:* [[§45 Vector Fields as Derivations#^prop-45-2|§45.2]]

> [!remark]- Connections
> - The pointwise version, a derivation of $C^\infty(M)$ at $p$ only sees a function near $p$ (Lee, Proposition 3.8), in the proof of [[§26 Derivations and the Abstract Tangent Space#^prop-26-3|Germ Derivations and Global Derivations, §26.3]].

> [!remark] Remark: Differential Operators
> The operators $D_X$, $X \in \mathfrak{X}(M)$ ([[§45 Vector Fields as Derivations#^lem-45-1|Lemma §45.1]]), together with the multiplication operators $f \mapsto gf$, generate under composition and sums the ring of *differential operators* on $M$; all of them are [[§45 Vector Fields as Derivations#^def-45-2|local]]. Uribe stated the converse “FYI”, without proof: every linear local operator is a differential operator. This is Peetre's theorem; its precise form says that a linear local operator is, near each point, a differential operator of finite order — on a non-compact $M$ the order need not be bounded globally. Stated, not proved, here.

^rem-45-2

> [!theorem] Proposition §45.4: Derivations Are Vector Fields
> Conversely, every [[§45 Vector Fields as Derivations#^def-45-1|derivation]] $D$ of $C^\infty(M)$ is of the form $D = D_X$ ([[§45 Vector Fields as Derivations#^lem-45-1|Lemma §45.1]]) for a unique $X \in \mathfrak{X}(M)$.
>
> *Lee: Proposition 8.15*

^prop-45-4

> [!proof]+ Proof (to be filled)
> Stated in Lecture 15 as “the goal”; the proof is to come. “It's not an immediate thing at all … tangent vectors are defined in terms of germs”, local objects near a point, “whereas” a derivation of $C^\infty(M)$ “a priori” acts on functions on all of $M$. Locality ([[§45 Vector Fields as Derivations#^lem-45-3|Lemma §45.3]]) bridges the two.

^pf-45-4
