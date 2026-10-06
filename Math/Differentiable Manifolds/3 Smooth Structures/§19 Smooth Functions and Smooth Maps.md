---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 19
tags: [differentiable-manifolds, math591]
---
← [[§18 Projective Spaces as Smooth Manifolds]] · ↑ [[· 3 Smooth Structures]] · [[§20 Manifolds in Euclidean Space]] →

*Stage: foundations — With a smooth structure in hand the chart drops out of the phrase “smooth”: smooth functions, smooth maps, diffeomorphisms and product manifolds.*

[[§17 Differentiable Structures#^def-17-2|Def. §17.2]] explains what it means for a function to be smooth *in the sense of one chart*. With a smooth structure in hand the chart can be dropped from the phrase. Throughout, $M$ is a smooth manifold with maximal atlas $\mathcal{A}$.

> [!definition] Definition §19.1: Smooth Chart
> Let $M$ be a smooth manifold with maximal atlas $\mathcal{A}$. A **smooth chart** of $M$ is a chart belonging to $\mathcal{A}$ — equivalently, by [[§17 Differentiable Structures#^thm-17-5|§17.5]], a chart compatible with every chart of some, hence any, atlas generating $\mathcal{A}$.
>
> *Lee: Ch. 1, Smooth Structures*

^def-19-1

> [!definition] Definition §19.2: Smooth Function on a Manifold
> A function $f : M \to \mathbb{R}$ is **smooth** if for every $p \in M$ there exists a smooth chart $(U,\varphi)$ with $p \in U$ such that
>
> $$
> f_\varphi \;:=\; f|_U \circ \varphi^{-1} : \varphi(U) \longrightarrow \mathbb{R}
> $$
>
> is smooth in the sense of analysis. (The function $f_\varphi$ is $f$ written in the coordinates of the chart; it is what [[§17 Differentiable Structures#^def-17-2|Def. §17.2]] called $h \circ \varphi^{-1}$.)
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^def-19-2

> [!theorem] Proposition §19.1: Some Chart Suffices — Every Chart Then Works
> If $f : M \to \mathbb{R}$ is smooth, then $f_\psi = f|_V \circ \psi^{-1}$ is smooth for *every* smooth chart $(V,\psi)$ of $M$.
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^prop-19-1

> [!proof]+ Proof
> *(Stated in lecture, with the proof left to the class; filled in.)* Let $(V,\psi)$ be a smooth chart and $q \in V$; we show $f_\psi$ is smooth on a neighborhood of $\psi(q)$. Since smoothness of a function on an open subset of $\mathbb{R}^n$ is a local property, this suffices. By [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]] there is a smooth chart $(U,\varphi)$ with $q \in U$ and $f_\varphi$ smooth on $\varphi(U)$. Both charts belong to the maximal atlas, so they are compatible, and on the open set $\psi(U \cap V) \ni \psi(q)$,
>
> $$
> f_\psi = f \circ \psi^{-1} = \big(f \circ \varphi^{-1}\big) \circ \big(\varphi \circ \psi^{-1}\big) = f_\varphi \circ (\varphi \circ \psi^{-1}),
> $$
>
> a composite of the smooth map $f_\varphi$ with the transition function $\varphi \circ \psi^{-1}$, which is smooth by compatibility. Hence $f_\psi$ is smooth near $\psi(q)$.

^pf-19-1

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-9|Def. §17.9]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark] Remark
> The point of logic Uribe stopped to make: the definition says “there *exists* a chart,” and the proposition upgrades it to “*any* chart.” Without the proposition, smoothness of $f$ would appear to depend on which charts one happened to test it in. The upgrade costs exactly one use of compatibility — which is what compatibility was designed to buy ([[§17 Differentiable Structures#^thm-17-1|§17.1]]). He assigned this as an exercise, not to be collected: “you have to wrestle with this.”

^rem-19-1

To compare two smooth manifolds one needs smooth *maps* between them.

> [!definition] Definition §19.3: Smooth Map and Diffeomorphism
> Let $(M, \mathcal{A}_M)$ and $(N, \mathcal{A}_N)$ be smooth manifolds of dimensions $m$ and $n$. A map $F : M \to N$ is **smooth** if it is continuous and for every $p \in M$ there are charts $(U,\varphi) \in \mathcal{A}_M$ with $p \in U$ and $(V,\psi) \in \mathcal{A}_N$ with $F(U) \subseteq V$ such that the **coordinate representation**
>
> $$
> \psi \circ F \circ \varphi^{-1} : \varphi(U) \longrightarrow \psi(V) \subseteq \mathbb{R}^n
> $$
>
> is smooth. $F$ is a **diffeomorphism** if it is a smooth bijection with smooth inverse — generalizing [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], with which it agrees on open subsets of Euclidean space ([[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]]).
>
> *Lee: Ch. 2, Smooth Functions and Smooth Maps*

^def-19-3

![[m591-8-8.svg]]
*The top row is the map one cares about, between spaces where “smooth” has no meaning; the bottom row is its coordinate representation, between open subsets of Euclidean spaces where it does. The two vertical arrows are charts, so they are homeomorphisms, and the square commutes by construction. Smoothness of $F$ is defined by smoothness of the bottom arrow, and [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]] says this does not depend on which charts are used to build it.*

> [!remark]- Connections
> - The Euclidean notion it generalizes: [[§17 Differentiable Structures#^def-17-3|Def. §17.3]]; local diffeomorphisms and the bijective case: [[§33 Local Diffeomorphisms#^def-33-1|Def. §33.1]], [[§33 Local Diffeomorphisms#^cor-33-3|§33.3]].
> - The topological counterpart, homeomorphism: [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]].

> [!theorem] Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts
> If $F : M \to N$ is smooth, then for *every* pair of smooth charts $(U',\varphi')$ of $M$ and $(V',\psi')$ of $N$ with $F(U') \subseteq V'$, the coordinate representation $\psi' \circ F \circ \varphi'^{-1} : \varphi'(U') \to \psi'(V')$ is smooth. For $N = \mathbb{R}$ with its standard one-chart atlas, [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] agrees with [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]].
>
> *Lee: Proposition 2.5*

^prop-19-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Fix $a \in \varphi'(U')$ and put $p = \varphi'^{-1}(a)$. [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] supplies charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U) \subseteq V$ and $\psi \circ F \circ \varphi^{-1}$ smooth. On the open set $\varphi'(U \cap U') \ni a$,
>
> $$
> \psi' \circ F \circ \varphi'^{-1} = (\psi' \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1}).
> $$
>
> Here $\varphi \circ \varphi'^{-1}$ maps $\varphi'(U \cap U')$ into $\varphi(U \cap U')$, then $F$ maps $U \cap U'$ into $V \cap V'$, and $\psi' \circ \psi^{-1}$ is defined on $\psi(V \cap V')$. The outer factors are transition functions, smooth by compatibility, and the middle one is smooth by hypothesis. So the composite is smooth near $a$, and $a$ was arbitrary. For $N = \mathbb{R}$, taking $\psi = \mathrm{id}$ turns [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] into [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]]; continuity is automatic there, since $f = f_\varphi \circ \varphi$ near each point.

^pf-19-2

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-2|Def. §19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^ex-17-1|Ex. §17.1]], [[Multivariable Chain Rule|452 §12.2]]

> [!definition] Definition §19.5: Diffeomorphic Manifolds
> Smooth manifolds $M$ and $N$ are **diffeomorphic** if there is a diffeomorphism $F : M \to N$. Diffeomorphic manifolds are also called **isomorphic as smooth manifolds**.
>
> *Lee: Ch. 2, Diffeomorphisms*

^def-19-5

> [!remark] Remark
> “Diffeomorphic” is to smooth manifolds what “homeomorphic” is to topological spaces: the notion of sameness, under which every smooth property is preserved. No symbol is introduced for it; $\cong$ is already used in these notes for homeomorphisms and linear isomorphisms, so the word is written out.

^rem-19-2

> [!theorem] Proposition §19.3: The Two Notions of Diffeomorphism Agree
> Give open sets $A \subseteq \mathbb{R}^m$ and $B \subseteq \mathbb{R}^n$ their standard smooth structures, determined by the charts $(A, \mathrm{id}_A)$ and $(B, \mathrm{id}_B)$. Then a map $F : A \to B$ is smooth in the sense of [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] if and only if it is smooth in the Euclidean sense. Consequently, for $m = n$, $F$ is a diffeomorphism in the sense of [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] if and only if it is one in the sense of [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], and $A$ and $B$ are diffeomorphic in the sense of [[§19 Smooth Functions and Smooth Maps#^def-19-5|Def. §19.5]] if and only if they are in the sense of [[§17 Differentiable Structures#^def-17-3|Def. §17.3]].

^prop-19-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $F$ is smooth in the Euclidean sense, it is continuous, and in the charts $(A, \mathrm{id}_A)$ and $(B, \mathrm{id}_B)$ its coordinate representation is $F$ itself, which is smooth. Conversely, suppose $F$ is smooth in the sense of [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], and let $p \in A$ with charts $(U, \varphi)$ and $(V, \psi)$ as in that definition. These charts belong to the standard structures, so they are compatible with the identity charts: $\varphi = \varphi \circ \mathrm{id}_A^{-1}$ and $\psi^{-1} = \mathrm{id}_B \circ \psi^{-1}$ are smooth in the Euclidean sense, by [[§17 Differentiable Structures#^def-17-4|Def. §17.4]]. Hence on $U$
>
> $$
> F = \psi^{-1} \circ \big(\psi \circ F \circ \varphi^{-1}\big) \circ \varphi
> $$
>
> is a composite of Euclidean-smooth maps, so $F$ is smooth near $p$. For diffeomorphisms, apply this to $F$ and to $F^{-1}$.

^pf-19-3

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-5|Def. §19.5]], [[§17 Differentiable Structures#^ex-17-1|Ex. §17.1]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark] Remark
> Not stated in lecture. The word is defined twice because the logic needs it twice: [[§17 Differentiable Structures#^def-17-3|Def. §17.3]] must exist before smooth manifolds do, since compatibility of charts is phrased with it, and [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]] is the general notion. The proposition is what licenses using one word for both. A third notion, the *local* diffeomorphism of [[§33 Local Diffeomorphisms|§33]], is genuinely different; [[§33 Local Diffeomorphisms#^cor-33-3|§33.3]] relates it to the other two.

^rem-19-3

> [!theorem] Lemma §19.4: Composition of Smooth Maps
> If $F : M \to N$ and $G : N \to P$ are smooth maps of smooth manifolds, then $G \circ F : M \to P$ is smooth.
>
> *Lee: Proposition 2.10*

^lem-19-4

> [!proof]+ Proof
> *(Lecture 7: “something that I would trust ChatGPT to prove without looking at the answer”; filled in.)* $G \circ F$ is continuous as a composite of continuous maps. Fix $p \in M$; we must produce charts at $p$ and at $G(F(p))$ satisfying [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]. The order of choices matters.
>
> *Step 1: charts for $G$ at $F(p)$.* Since $G$ is smooth, there are smooth charts $(V, \psi)$ of $N$ with $F(p) \in V$ and $(W, \chi)$ of $P$ with $G(V) \subseteq W$ such that $\chi \circ G \circ \psi^{-1}$ is smooth on $\psi(V)$.
>
> *Step 2: a chart for $F$ at $p$ landing inside $V$.* Since $F$ is smooth, there are smooth charts $(U_0, \varphi)$ of $M$ with $p \in U_0$ and $(V_0, \psi_0)$ of $N$ with $F(U_0) \subseteq V_0$ such that $\psi_0 \circ F \circ \varphi^{-1}$ is smooth. The chart $(V_0,\psi_0)$ need not be the $(V,\psi)$ of Step 1, so we adjust. Put $U = U_0 \cap F^{-1}(V)$, an open neighborhood of $p$ since $F$ is continuous, and keep the coordinate map $\varphi|_U$; $(U, \varphi|_U)$ is still a smooth chart (a restriction of one to an open subset). Now $F(U) \subseteq V \cap V_0$, and on $\varphi(U)$
>
> $$
> \psi \circ F \circ \varphi^{-1} = (\psi \circ \psi_0^{-1}) \circ (\psi_0 \circ F \circ \varphi^{-1}),
> $$
>
> which is smooth: the first factor is a transition function of the maximal atlas of $N$, the second is smooth by the choice of $(U_0,\varphi)$.
>
> *Step 3: compose.* $G \circ F$ maps $U$ into $W$, and on $\varphi(U)$
>
> $$
> \chi \circ (G \circ F) \circ \varphi^{-1} = \big(\chi \circ G \circ \psi^{-1}\big) \circ \big(\psi \circ F \circ \varphi^{-1}\big),
> $$
>
> a composite of two smooth maps between open subsets of Euclidean spaces (the inner map takes values in $\psi(V)$ because $F(U) \subseteq V$). So $(U, \varphi|_U)$ and $(W, \chi)$ witness the smoothness of $G \circ F$ at $p$.

^pf-19-4

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§10 Continuous Functions#^thm-10-4|590 §10.4]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark]- Connections
> - The Euclidean case is the chain rule: [[Multivariable Chain Rule|452 §12.2]].

> [!theorem] Proposition §19.5: Being Diffeomorphic Is an Equivalence Relation
> 1. Being diffeomorphic is an equivalence relation on smooth manifolds.
> 2. Diffeomorphic manifolds are homeomorphic.
>
> *Lee: Proposition 2.15*

^prop-19-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) *Reflexive:* $\mathrm{id}_M$ is a diffeomorphism, its coordinate representation in any chart $(U,\varphi)$, taken on both sides, being the identity of $\varphi(U)$. *Symmetric:* if $F$ is a diffeomorphism, so is $F^{-1}$, since the definition is symmetric in $F$ and $F^{-1}$. *Transitive:* if $F : M \to N$ and $G : N \to P$ are diffeomorphisms, then $G \circ F$ is smooth by [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], and so is its inverse $F^{-1} \circ G^{-1}$. (2) Smooth maps are continuous by [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], so a diffeomorphism is a continuous bijection with continuous inverse.

^pf-19-5

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-5|Def. §19.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]]

> [!remark] Remark
> The converse of (2) is false: Milnor's exotic $7$-spheres are homeomorphic to $S^7$ but not diffeomorphic to it (see the [[§19 Smooth Functions and Smooth Maps#^rem-19-8|remark on distinct structures]]). Two further distinctions are worth keeping apart. *Different smooth structures* on one set may still be *diffeomorphic*: in [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]], $\mathbb{R}$ and $\widetilde{\mathbb{R}}$ have different maximal atlases, yet $x \mapsto x^3$ is a diffeomorphism between them. And being diffeomorphic is a property of a *pair* of manifolds, while being a diffeomorphism is a property of a *map*: $\mathrm{id} : \mathbb{R} \to \widetilde{\mathbb{R}}$ is not a diffeomorphism even though the two are diffeomorphic.

^rem-19-4

> [!remark] Remark
> Uribe: “the composition of smooth maps is smooth is something I would trust ChatGPT to prove without looking at the answer.” The only content is Step 2 — the middle charts produced by the two hypotheses need not agree, and one must shrink the domain using continuity of $F$ and then pay one transition function to switch. “Just compose the two” skips exactly this.

^rem-19-5

> [!example] Example §19.1: Two Smooth Structures on the Real Line
> Take $M = \mathbb{R}$ as a topological space in both cases, and put
>
> $$
> \mathbb{R} = (\mathbb{R}, \{(\mathbb{R}, \varphi)\}), \ \ \varphi = \mathrm{id}; \qquad\qquad
> \widetilde{\mathbb{R}} = (\mathbb{R}, \{(\mathbb{R}, \psi)\}), \ \ \psi(p) = \sqrt[3]{p}.
> $$
>
> Both $\varphi$ and $\psi$ are homeomorphisms of $\mathbb{R}$ onto $\mathbb{R}$, so each is a legitimate chart ([[§17 Differentiable Structures#^def-17-1|Def. §17.1]]), and a one-chart atlas is automatically smooth: the only compatibility to check is of the chart with itself, and the transition function is the identity. By [[§17 Differentiable Structures#^thm-17-5|§17.5]] each therefore determines a smooth structure.
>
> *Lee: Example 1.23*

^ex-19-1

> [!proof]+ Working out the example
> *(Lecture 5 introduced this example — the two structures are “not compatible, but isomorphic” — and Lecture 6 returned to it: “different, but isomorphic. We're going to say diffeomorphic.” Worked out here.)* *Step 1: the formula of a chart is not a legality condition.* One is tempted to object that $\psi$ “is not smooth.” On a bare topological manifold that question is not yet posed: “smooth” for a function on $M$ has no meaning until a structure is fixed, and here $\psi$ is what supplies the structure. What makes $\sqrt[3]{\,\cdot\,}$ look illegitimate is a silent comparison against the standard structure of $\mathbb{R}$ — and that comparison is not part of [[§17 Differentiable Structures#^def-17-1|Def. §17.1]]; it is the compatibility question of [[§17 Differentiable Structures#Compatibility of Charts|Compatibility of Charts]], arriving early and in disguise. Any homeomorphism onto an open set is a chart, whatever its formula. The formula is irrelevant to whether the chart may be written down, and decisive for which structure it produces.
>
> *Step 2: each chart is smooth for its own structure.* By [[§17 Differentiable Structures#^def-17-2|Def. §17.2]], a function $h : \mathbb{R} \to \mathbb{R}$ is smooth in the sense of $\psi$ iff $h \circ \psi^{-1}$ is smooth, where $\psi^{-1}(y) = y^3$. Taking $h = \psi$ gives $\psi \circ \psi^{-1} = \mathrm{id}$, which is smooth. So $\sqrt[3]{\,\cdot\,}$ *is* a smooth function on $\widetilde{\mathbb{R}}$. Nothing is special about this chart: the coordinate representation of any chart in its own coordinates is the identity, so every chart of an atlas is smooth for the structure that atlas generates. In the same way $\psi : \widetilde{\mathbb{R}} \to \mathbb{R}$ is a diffeomorphism — a chart is exactly an identification of its domain with a piece of Euclidean space, carried out in whichever coordinate the chart names.
>
> *Step 3: the two structures are different.* Compatibility is a condition on a *pair* of charts, and it is here that the two disagree. The two transition functions are
>
> $$
> \psi \circ \varphi^{-1}(x) = \sqrt[3]{x}, \qquad\qquad \varphi \circ \psi^{-1}(y) = y^3,
> $$
>
> and note the asymmetry: the second is smooth, the first is not, since $\tfrac{d}{dx}\sqrt[3]{x} = \tfrac13 x^{-2/3}$ blows up at $x = 0$. [[§17 Differentiable Structures#^def-17-4|Def. §17.4]] demands that the transition function be a diffeomorphism, i.e. that *both* directions be smooth — and this example is why: with only one direction required, compatibility would not even be a symmetric relation. So the charts are not compatible, the atlases are not compatible, and the maximal atlases are distinct. Equivalently, in the language of [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]: the identity map $\mathbb{R} \to \widetilde{\mathbb{R}}$ has coordinate representation $\psi \circ \mathrm{id} \circ \varphi^{-1}(t) = \sqrt[3]{t}$ and is *not* smooth.
>
> *Step 4: which functions are smooth in each.* Smooth in the sense of $\varphi$ means $h \circ \varphi^{-1} = h$ is smooth, so $C^\infty(\mathbb{R})$ is the usual class. Smooth in the sense of $\psi$ means $y \mapsto h(y^3)$ is smooth. Every ordinarily smooth $h$ passes this test, being a composite of smooth maps; and $h = \sqrt[3]{\,\cdot\,}$ passes it while failing the first. Hence
>
> $$
> C^\infty(\mathbb{R}) \subsetneq C^\infty(\widetilde{\mathbb{R}}),
> $$
>
> a *strict* containment: $\widetilde{\mathbb{R}}$ has more smooth functions than $\mathbb{R}$. The two structures are genuinely different objects, not two names for one.
>
> *Step 5: and yet they are isomorphic.* Define $\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$, $\Phi(x) = x^3$. Its coordinate representation is $\psi \circ \Phi \circ \varphi^{-1}(t) = \sqrt[3]{t^3} = t$, the identity; the representation of $\Phi^{-1}(y) = \sqrt[3]{y}$ is likewise the identity. So $\Phi$ is a diffeomorphism and $\mathbb{R} \cong \widetilde{\mathbb{R}}$ as smooth manifolds. There is no contradiction with Step 4: the isomorphism is not the identity map, and pullback along $\Phi$ carries $C^\infty(\widetilde{\mathbb{R}})$ bijectively onto $C^\infty(\mathbb{R})$, so a strict containment between isomorphic objects is no more paradoxical here than elsewhere in infinite mathematics.
>
> The moral is that $x$ is merely a *label* for points of $\mathbb{R}$; the structure decides which functions of that label count as smooth, and the two structures decide differently. The identity map respects labels but not structure, while $x \mapsto x^3$ respects structure and scrambles labels.

^pf-ex-19-1

*Uses:* [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-2|Def. §17.2]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[Multivariable Chain Rule|452 §12.2]]

> [!remark]- Connections
> - The general mechanism: [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]] and [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]]; this example redone as a transported structure: [[§19 Smooth Functions and Smooth Maps#^ex-19-2|Ex. §19.2]].

**Transcription note.** The board reads “Claim: $\exists\,\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$ which is $C^\infty$, $\Phi(x) = \sqrt[3]{x}$.” With $\widetilde{\mathbb{R}}$ carrying the chart $\psi = \sqrt[3]{\ \cdot\ }$, that map has coordinate representation $\sqrt[3]{\sqrt[3]{t}} = t^{1/9}$, which is not smooth at $0$; the domain and the formula have been paired the wrong way. The two correct readings are $\Phi : \mathbb{R} \to \widetilde{\mathbb{R}}$ with $\Phi(x) = x^3$ (used above), or the same map read backwards, $\Phi : \widetilde{\mathbb{R}} \to \mathbb{R}$ with $\Phi(x) = \sqrt[3]{x}$. Either way the coordinate representation is the identity, which is what the lecture meant by “it looks strange, but rewritten in the differentiable coordinate you just get the identity.”

![[m591-8-9.svg]]
*The two coordinate pictures of [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]]: left, the transition function $\psi\circ\varphi^{-1}(t)=\sqrt[3]{t}$, whose vertical tangent at $0$ makes the two charts incompatible; right, the coordinate representation $\psi\circ\Phi\circ\varphi^{-1}(t)=t$ of $\Phi(x) = x^3$, the identity, which is why $\Phi$ is a diffeomorphism.*

> [!theorem] Proposition §19.6: Transport of Smooth Structure
> Let $N$ be a smooth $n$-manifold, $X$ a topological space, and $h : X \to N$ a homeomorphism. Then:
> 1. $X$ is a topological $n$-manifold, and $\mathcal{A}_h = \{\, (h^{-1}(V),\ \psi \circ h) \mid (V,\psi) \text{ a smooth chart of } N \,\}$ is a smooth atlas on $X$;
> 2. for the smooth structure it determines, $h$ is a diffeomorphism;
> 3. it is the *only* smooth structure on $X$ for which $h$ is a diffeomorphism.
>
> *Lee: cf. Problem 1-6*

^prop-19-6

> [!proof]+ Proof
> (1) Hausdorffness and second countability pass through homeomorphisms. Each $\psi \circ h$ is a homeomorphism of the open set $h^{-1}(V)$ onto the open set $\psi(V) \subseteq \mathbb{R}^n$, and these domains cover $X$ because the $V$ cover $N$. Transition functions are $(\psi' \circ h) \circ (\psi \circ h)^{-1} = \psi' \circ \psi^{-1}$, transition functions of $N$, hence smooth.
>
> (2) In the charts $(h^{-1}(V), \psi \circ h)$ of $X$ and $(V, \psi)$ of $N$, the coordinate representation of $h$ is $\psi \circ h \circ (\psi \circ h)^{-1} = \mathrm{id}$, and likewise for $h^{-1}$. Both are continuous, so both are smooth.
>
> (3) Suppose $h$ is a diffeomorphism for some smooth structure $\mathcal{S}$ on $X$, and let $(W, \chi) \in \mathcal{S}$. Then $(\psi \circ h) \circ \chi^{-1} = \psi \circ h \circ \chi^{-1}$ is a coordinate representation of $h$, and $\chi \circ (\psi \circ h)^{-1} = \chi \circ h^{-1} \circ \psi^{-1}$ one of $h^{-1}$; both are smooth by [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]. So every chart of $\mathcal{S}$ is compatible with every chart of $\mathcal{A}_h$, i.e. $\mathcal{S}$ lies in the maximal atlas generated by $\mathcal{A}_h$. Since $\mathcal{S}$ is itself maximal, the two coincide ([[§17 Differentiable Structures#^thm-17-5|§17.5]]).

^pf-19-6

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]]

> [!definition] Definition §19.6: Transported Smooth Structure
> In the situation of [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], the smooth structure on $X$ generated by $\mathcal{A}_h$ — the unique one for which $h$ is a diffeomorphism — is the smooth structure **transported** along $h$.
>
> *Lee: cf. Problem 1-6*

^def-19-6

> [!remark] Remark
> This is the smooth counterpart of [[§15 The Topology of G∕H and Real Grassmannians#^def-15-2|Def. §15.2]], where a *topology* was transported along a bijection. Here a smooth structure is transported along a homeomorphism: the charts of $N$, precomposed with $h$, become charts of $X$. The structure on $X$ is then “$N$'s structure, relabelled by $h$”, which is why $h$ is automatically a diffeomorphism.

^rem-19-6

> [!theorem] Corollary §19.7: Single-Chart Structures on $\mathbb{R}^n$
> Let $h : \mathbb{R}^n \to \mathbb{R}^n$ be a homeomorphism, and let $M$ be $\mathbb{R}^n$ with the smooth structure determined by the one-chart atlas $\{(\mathbb{R}^n, h)\}$.
> 1. $\{(\mathbb{R}^n, h)\}$ is a smooth atlas.
> 2. $h : M \to \mathbb{R}^n$ is a diffeomorphism onto $\mathbb{R}^n$ with its standard structure. So $M$ is diffeomorphic to standard $\mathbb{R}^n$.
> 3. The smooth structure of $M$ *equals* the standard one if and only if $h$ is a diffeomorphism of standard $\mathbb{R}^n$.
>
> *Lee: Example 1.23 and Problem 1-6*

^cor-19-7

> [!proof]+ Proof
> *(Assignment 3, Problem 1.)* (1) The single domain $\mathbb{R}^n$ covers $M$; $h$ is a homeomorphism onto $h(\mathbb{R}^n) = \mathbb{R}^n$, which is open; and the only transition function is $h \circ h^{-1} = \mathrm{id}_{\mathbb{R}^n}$, which is smooth.
>
> (2) The underlying topological spaces of $M$ and of standard $\mathbb{R}^n$ are the same, so $h$ is a homeomorphism $M \to \mathbb{R}^n$, in particular continuous with continuous inverse $h^{-1}$. In the charts $(\mathbb{R}^n, h)$ of $M$ and $(\mathbb{R}^n, \mathrm{id})$ of standard $\mathbb{R}^n$, the coordinate representation of $h$ is $\mathrm{id} \circ h \circ h^{-1} = \mathrm{id}_{\mathbb{R}^n}$, and that of $h^{-1}$ is $h \circ h^{-1} \circ \mathrm{id}^{-1} = \mathrm{id}_{\mathbb{R}^n}$. Both are smooth, so $h$ is a smooth bijection with smooth inverse. Equivalently, $M$ carries exactly the structure transported along $h$ from standard $\mathbb{R}^n$ ([[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], with the atlas $\{(\mathbb{R}^n, \mathrm{id})\}$ of the target).
>
> (3) The two one-chart atlases determine the same smooth structure if and only if they are compatible ([[§17 Differentiable Structures#^def-17-7|Def. §17.7]]), i.e. if and only if $h \circ \mathrm{id}^{-1} = h$ and $\mathrm{id} \circ h^{-1} = h^{-1}$ are both smooth — that is, if and only if $h$ is a diffeomorphism of standard $\mathbb{R}^n$.

^pf-19-7

*Uses:* [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§17 Differentiable Structures#^ex-17-1|Ex. §17.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§17 Differentiable Structures#^def-17-7|Def. §17.7]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]]

![[m591-8-10.svg]]
*The proof of (2) in one square. Upstairs, $h$ is the map between the two manifolds; the vertical arrows are their charts, $h$ on the left and $\mathrm{id}$ on the right. The square commutes, so the coordinate representation along the bottom is the identity: $h$ is as smooth as a map can be, even when, as a map of standard $\mathbb{R}^n$, it is not differentiable at all.*

> [!example] Example §19.2: The Real Line with the Cube-Root Chart
> For $n = 1$ and $h(x) = \sqrt[3]{x}$, the manifold $M$ is the $\widetilde{\mathbb{R}}$ of [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]]. By [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]](3) its structure differs from the standard one, since $h$ is not differentiable at $0$. By part (2) it is nevertheless diffeomorphic to standard $\mathbb{R}$, via $h : \widetilde{\mathbb{R}} \to \mathbb{R}$ — equivalently via $h^{-1}(x) = x^3$ in the other direction, the map $\Phi$ of that example.
>
> *Lee: Example 1.23*

^ex-19-2

*Uses:* [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]], [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]]

> [!remark] Remark
> [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]] produces, from each homeomorphism of $\mathbb{R}^n$ that is not a diffeomorphism — there are uncountably many — a smooth structure on $\mathbb{R}^n$ *different* from the standard one. By (2), every one of them is *diffeomorphic* to the standard one. So “how many smooth structures” is the wrong question: the right one is how many up to diffeomorphism. It also shows something about the exotic structures of the [[§19 Smooth Functions and Smooth Maps#^rem-19-8|next remark]]. An exotic $\mathbb{R}^4$ cannot admit a single chart whose image is all of $\mathbb{R}^4$, since by the argument of (2) that chart would be a diffeomorphism onto standard $\mathbb{R}^4$.

^rem-19-7

> [!remark] Remark: Distinct Structures versus Non-Diffeomorphic Manifolds
> [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]] shows that one topological manifold can carry distinct smooth structures — but that alone is cheap, since pulling any structure back along a homeomorphism that is not a diffeomorphism produces another one, and all of these are diffeomorphic to the original ([[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]]). The deep question is whether a topological manifold can carry structures that are *not* diffeomorphic to one another. It can: Milnor found smooth structures on $S^7$ not diffeomorphic to the standard one (1956), and $\mathbb{R}^4$ admits uncountably many pairwise non-diffeomorphic structures, the first produced by combining Freedman's topological classification with Donaldson's gauge theory, the uncountable family by Taubes. By contrast $\mathbb{R}^n$ for $n \neq 4$ admits exactly one up to diffeomorphism — a result of Stallings for $n \ge 5$ and of Radó and Moise for $n \le 3$, not of Donaldson, to whom the lecture attributed it. All of this is far outside the course, but it is why the definitions above are made so carefully.

^rem-19-8

## Product Manifolds

*Lecture 11 (Fri Sep 25). The product of two smooth manifolds is a smooth manifold, with the products of charts as an atlas; its tangent spaces are treated in [[§31 Tangent Vectors as Velocities of Curves|§31]].*

> [!theorem] Proposition §19.8: The Product Smooth Structure
> Let $M_1$, $M_2$ be smooth manifolds of dimensions $m_1$, $m_2$. The product space $M_1 \times M_2$ is a topological manifold of dimension $m_1 + m_2$, and the **product charts**
>
> $$
> \big(U_1 \times U_2,\ \varphi_1 \times \varphi_2\big), \qquad (\varphi_1 \times \varphi_2)(q_1, q_2) = \big(\varphi_1(q_1), \varphi_2(q_2)\big) \in \mathbb{R}^{m_1} \times \mathbb{R}^{m_2} = \mathbb{R}^{m_1 + m_2},
> $$
>
> with $(U_i, \varphi_i)$ a smooth chart of $M_i$, form a smooth atlas on it.
>
> *Lee: Example 1.34*

^prop-19-8

> [!proof]+ Proof
> Hausdorffness and second countability pass to products ([[§3 Subspaces and Products#^thm-3-12|§3.12]]). Each $U_1 \times U_2$ is open, and these sets cover $M_1 \times M_2$. The map $\varphi_1 \times \varphi_2$ is a bijection of $U_1 \times U_2$ onto $\varphi_1(U_1) \times \varphi_2(U_2)$, which is open in $\mathbb{R}^{m_1 + m_2}$; it is continuous with continuous inverse $\varphi_1^{-1} \times \varphi_2^{-1}$, because each is continuous in each component ([[§3 Subspaces and Products#^thm-3-10|§3.10]]). So the product charts are charts, and $M_1 \times M_2$ is locally Euclidean of dimension $m_1 + m_2$. Two product charts overlap in $(U_1 \cap U_1') \times (U_2 \cap U_2')$, and their transition map is
>
> $$
> (\psi_1 \times \psi_2) \circ (\varphi_1 \times \varphi_2)^{-1} = (\psi_1 \circ \varphi_1^{-1}) \times (\psi_2 \circ \varphi_2^{-1}),
> $$
>
> smooth because each component is.

^pf-19-8

*Uses:* [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§3 Subspaces and Products#^thm-3-12|§3.12]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§17 Differentiable Structures#^def-17-1|Def. §17.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1]]

> [!remark]- Connections
> - Product topology in 590: [[§4 Product Topology#^def-4-1|590 Def. §4.1]]; the tangent space of a product: [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]].

> [!definition] Definition §19.7: Product Manifold
> The **product manifold** $M_1 \times M_2$ is the product space with the smooth structure generated by the product charts ([[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]]). If $\varphi_1 = (x^1, \ldots, x^{m_1})$ and $\varphi_2 = (y^1, \ldots, y^{m_2})$, the coordinate functions of the product chart are $x^i \circ \pi_1$ and $y^j \circ \pi_2$, written again $x^i$, $y^j$: “the $x$'s and then the $y$'s”. For $p_2 \in M_2$ and $p_1 \in M_1$, the **slice inclusions** are
>
> $$
> \iota^{p_2} : M_1 \to M_1 \times M_2, \ q \mapsto (q, p_2), \qquad\qquad \iota^{p_1} : M_2 \to M_1 \times M_2, \ q \mapsto (p_1, q).
> $$

^def-19-7

> [!theorem] Proposition §19.9: Projections and Slice Inclusions Are Smooth
> The projections $\pi_1 : M_1 \times M_2 \to M_1$, $\pi_2 : M_1 \times M_2 \to M_2$ and the slice inclusions $\iota^{p_2}$, $\iota^{p_1}$ are smooth. In product charts their coordinate representations are
>
> $$
> (r, s) \mapsto r, \qquad (r, s) \mapsto s, \qquad r \mapsto \big(r, \varphi_2(p_2)\big), \qquad s \mapsto \big(\varphi_1(p_1), s\big).
> $$

^prop-19-9

> [!proof]+ Proof
> All four are continuous: the projections by the definition of the product topology, the inclusions because their components are continuous ([[§3 Subspaces and Products#^thm-3-10|§3.10]]). The coordinate representations are read off from $\varphi_1 \circ \pi_1 \circ (\varphi_1 \times \varphi_2)^{-1}(r, s) = r$ and $(\varphi_1 \times \varphi_2) \circ \iota^{p_2} \circ \varphi_1^{-1}(r) = (r, \varphi_2(p_2))$, and the same for the others. They are smooth, so the maps are smooth ([[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]).

^pf-19-9

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1]]

> [!remark]- Connections
> - Projections are submersions: [[§34 Submersions#^ex-34-2|Ex. §34.2]]; their differentials: [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]].
