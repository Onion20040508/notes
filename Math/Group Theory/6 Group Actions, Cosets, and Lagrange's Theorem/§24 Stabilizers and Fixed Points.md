---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 24
tags: [group-theory, math493]
---
← [[§23 Actions]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§25 Orbits]] →

*Reference: Pinter Ch. 13, Ex. J.*

> [!definition] Definition §24.1: Stabilizer; Fixed Points
> Let $G$ [[§23 Actions#^def-23-1|act]] on $X$. For $x \in X$, the **stabilizer** of $x$ is
>
> $$
> \operatorname{Stab}(x) := \{ g \in G : g \star x = x \} \subseteq G,
> $$
>
> the set of group elements fixing $x$. For $g \in G$, the **fixed points** of $g$ are
>
> $$
> \operatorname{Fix}(g) := \{ x \in X : g \star x = x \} \subseteq X,
> $$
>
> the set of points fixed by $g$. (So $g \in \operatorname{Stab}(x)$ iff $x \in \operatorname{Fix}(g)$: the two notions record the same incidence relation from the two sides.)
>
> *Source: WS 4*

^def-24-1

> [!remark]- Connections
> - Stabilizers enter [[§28 Orbit–Stabilizer#^thm-28-3|Orbit–Stabilizer]]; fixed points enter [[§28 Orbit–Stabilizer#^thm-28-6|Burnside's Lemma]]; under conjugation the stabilizer is the [[§32 Conjugation as an Action and the Class Equation#^def-32-1|centralizer]].
> - Called the isotropy subgroup in 591, [[§11 Homogeneous Spaces#^def-11-2|591 Def. §11.2]]; for a continuous action on a space whose points are closed it is a closed subgroup, [[§11 Homogeneous Spaces#^thm-11-2|591 Thm. §11.2]].

> [!theorem] Proposition §24.1: The Stabilizer Is a Subgroup
> For every $x \in X$, $\operatorname{Stab}(x)$ is a subgroup of $G$. (The worksheet says “of $X$”; this is a typo — the stabilizer is a set of group elements.)
>
> *Source: WS 4.4*

^prop-24-1

> [!proof]+ Proof
> $e \star x = x$, so $e \in \operatorname{Stab}(x)$. If $g, h \in \operatorname{Stab}(x)$, then $(gh) \star x = g \star (h \star x) = g \star x = x$. If $g \in \operatorname{Stab}(x)$, apply $g^{-1}$ to both sides of $g \star x = x$: $x = g^{-1} \star (g \star x) = g^{-1} \star x$, so $g^{-1} \in \operatorname{Stab}(x)$.

^pf-24-1

*Uses:* [[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]], [[§23 Actions#^def-23-1|Def. §23.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!theorem] Proposition §24.2: Stabilizers of Points in the Same Orbit Are Conjugate
> Let $G$ act on $X$, $x \in X$, and $g \in G$. Then
>
> $$
> \operatorname{Stab}(g \star x) = g\,\operatorname{Stab}(x)\,g^{-1} = \{ g s g^{-1} : s \in \operatorname{Stab}(x) \}.
> $$
>
> *Source: WS 4.5*

^prop-24-2

> [!proof]+ Proof
> ($\subseteq$) Let $h \in \operatorname{Stab}(gx)$, i.e. $h \star (g \star x) = g \star x$. Applying $g^{-1}$ to both sides, $(g^{-1}hg) \star x = x$, so $g^{-1}hg \in \operatorname{Stab}(x)$, and hence $h = g(g^{-1}hg)g^{-1} \in g\operatorname{Stab}(x)g^{-1}$.
>
> ($\supseteq$) Let $h = g g_0 g^{-1}$ with $g_0 \in \operatorname{Stab}(x)$. Then $hg = g g_0$, so
>
> $$
> h \star (g \star x) = (hg) \star x = (g g_0) \star x = g \star (g_0 \star x) = g \star x,
> $$
>
> i.e. $h \in \operatorname{Stab}(g \star x)$.

^pf-24-2

*Uses:* [[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]], [[§23 Actions#^def-23-1|Def. §23.1]]

![[m493-24-1.svg]]
*The proposition in one picture: if $s$ fixes $x$ (red loop), then $gsg^{-1}$ fixes $y = g \star x$ — go back to $x$ by $g^{-1}$ (dashed), loop by $s$, and return by $g$ (read right to left, $g^{-1}$ acts first). Conversely every loop at $y$ arises this way, so $\operatorname{Stab}(y) = g\operatorname{Stab}(x)g^{-1}$.*

> [!remark]- Connections
> - Used in 591 to show that the topology of a homogeneous space does not depend on the base point: [[§12 The Topology of G∕H and Real Grassmannians#^prop-12-4|591 Prop. §12.4]].

> [!theorem] Corollary §24.3: Stabilizers Along an Orbit Are Conjugate
> If $y = g \star x$ for some $g \in G$ (i.e. $y$ lies in the orbit of $x$, [[§25 Orbits#^def-25-1|Def. §25.1]]), then $\operatorname{Stab}(y) = g \operatorname{Stab}(x) g^{-1}$, and conjugation $c_g$ restricts to an isomorphism $\operatorname{Stab}(x) \to \operatorname{Stab}(y)$. In particular all stabilizers of points in one orbit are isomorphic and have the same order.

^cor-24-3

> [!proof]+ Proof
> The equality is [[§24 Stabilizers and Fixed Points#^prop-24-2|the proposition]]. Conjugation $c_g$ is an automorphism of $G$ ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]), so its restriction to $\operatorname{Stab}(x)$ is an injective homomorphism with image $g\operatorname{Stab}(x)g^{-1} = \operatorname{Stab}(y)$.

^pf-24-3

*Uses:* [[§24 Stabilizers and Fixed Points#^prop-24-2|§24.2]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - Used in part (3) of [[§29 G Acting on Coset Spaces#^prop-29-1|The Action of G on G∕H, §29.1]]; for finite $G$ the equality of stabilizer orders along an orbit also follows from [[§28 Orbit–Stabilizer#^thm-28-3|Orbit–Stabilizer]].

> [!remark] Remark: Reading the Proposition
> Moving the point by $g$ conjugates its stabilizer by $g$. For the point stabilizer $H = \operatorname{Stab}(n) \subseteq S_n$ of [[§28 Orbit–Stabilizer#^def-28-1|Def. §28.1]], this says $\operatorname{Stab}(\sigma(n)) = \sigma H \sigma^{-1}$.

^rem-24-1
