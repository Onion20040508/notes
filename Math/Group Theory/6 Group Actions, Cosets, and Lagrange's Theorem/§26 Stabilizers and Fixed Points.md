---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 26
tags: [group-theory, math493]
---
← [[§25 Actions]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§27 Orbits]] →

*Reference: Pinter Ch. 13, Ex. J.*

> [!definition] Definition §26.1: Stabilizer
> Let $G$ [[§25 Actions#^def-25-1|act]] on $X$. For $x \in X$, the **stabilizer** of $x$ is
>
> $$
> \operatorname{Stab}(x) := \{ g \in G : g \star x = x \} \subseteq G,
> $$
>
> the set of group elements fixing $x$.
>
> *Source: WS 4*

^def-26-1

> [!remark]- Connections
> - Stabilizers enter [[§30 Orbit–Stabilizer#^thm-30-3|Orbit–Stabilizer]]; under conjugation the stabilizer is the [[§34 Conjugation as an Action and the Class Equation#^def-34-1|centralizer]].
> - Called the isotropy subgroup in 591, [[§14 Homogeneous Spaces#^def-14-3|591 Def. §14.3]]; for a [[§13 Group Actions and Orbit Spaces#^def-13-2|continuous action]] on a space whose points are closed it is a closed subgroup, [[§14 Homogeneous Spaces#^thm-14-2|591 Thm. §14.2]].
> - Used in Quantum Field Theory: the stabilizer of a particle's standard momentum under the Lorentz group is its little group, $SO(3)$ for a massive particle, whose representations are the particle's spin — [[§C3.5★ Particle States and the Little Group#^def-c3-5-1|QFT Def. §C3.5.1]], [[§C3.5★ Particle States and the Little Group#^thm-c3-5-7|QFT Theorem §C3.5.7]], [[§C3.5★ Particle States and the Little Group#^thm-c3-5-8|QFT Theorem §C3.5.8]].

> [!definition] Definition §26.2: Fixed Points
> For $g \in G$, the **fixed points** of $g$ are
>
> $$
> \operatorname{Fix}(g) := \{ x \in X : g \star x = x \} \subseteq X,
> $$
>
> the set of points fixed by $g$. (So $g \in \operatorname{Stab}(x)$ iff $x \in \operatorname{Fix}(g)$: the two notions record the same incidence relation from the two sides.)
>
> *Source: WS 4*

^def-26-2

> [!remark]- Connections
> - Fixed points enter [[§30 Orbit–Stabilizer#^thm-30-6|Burnside's Lemma]].

> [!theorem] Proposition §26.1: The Stabilizer Is a Subgroup
> For every $x \in X$, $\operatorname{Stab}(x)$ is a subgroup of $G$. (The worksheet says “of $X$”; this is a typo — the stabilizer is a set of group elements.)
>
> *Source: WS 4.4*

^prop-26-1

> [!proof]+ Proof
> $e \star x = x$, so $e \in \operatorname{Stab}(x)$. If $g, h \in \operatorname{Stab}(x)$, then $(gh) \star x = g \star (h \star x) = g \star x = x$. If $g \in \operatorname{Stab}(x)$, apply $g^{-1}$ to both sides of $g \star x = x$: $x = g^{-1} \star (g \star x) = g^{-1} \star x$, so $g^{-1} \in \operatorname{Stab}(x)$.

^pf-26-1

*Uses:* [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§25 Actions#^def-25-1|Def. §25.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!theorem] Proposition §26.2: Stabilizers of Points in the Same Orbit Are Conjugate
> Let $G$ act on $X$, $x \in X$, and $g \in G$. Then
>
> $$
> \operatorname{Stab}(g \star x) = g\,\operatorname{Stab}(x)\,g^{-1} = \{ g s g^{-1} : s \in \operatorname{Stab}(x) \}.
> $$
>
> *Source: WS 4.5*

^prop-26-2

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

^pf-26-2

*Uses:* [[§26 Stabilizers and Fixed Points#^def-26-1|Def. §26.1]], [[§25 Actions#^def-25-1|Def. §25.1]]

![[m493-24-1.svg]]
*The proposition in one picture: if $s$ fixes $x$ (red loop), then $gsg^{-1}$ fixes $y = g \star x$ — go back to $x$ by $g^{-1}$ (dashed), loop by $s$, and return by $g$ (read right to left, $g^{-1}$ acts first). Conversely every loop at $y$ arises this way, so $\operatorname{Stab}(y) = g\operatorname{Stab}(x)g^{-1}$.*

> [!remark]- Connections
> - Used in 591 to show that the topology of a homogeneous space does not depend on the base point: [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-4|591 Prop. §15.4]].
> - Used in Quantum Field Theory: another standard momentum on the same orbit has a conjugate little group, with the same representations, so the particle does not depend on the choice — [[§C3.5★ Particle States and the Little Group#^rem-c3-5-1|QFT Remark: What the definition fixes, and what it leaves free]].

> [!theorem] Corollary §26.3: Stabilizers Along an Orbit Are Conjugate
> If $y = g \star x$ for some $g \in G$ (i.e. $y$ lies in the orbit of $x$, [[§27 Orbits#^def-27-1|Def. §27.1]]), then $\operatorname{Stab}(y) = g \operatorname{Stab}(x) g^{-1}$, and conjugation $c_g$ restricts to an isomorphism $\operatorname{Stab}(x) \to \operatorname{Stab}(y)$. In particular all stabilizers of points in one orbit are isomorphic and have the same order.

^cor-26-3

> [!proof]+ Proof
> The equality is [[§26 Stabilizers and Fixed Points#^prop-26-2|the proposition]]. Conjugation $c_g$ is an automorphism of $G$ ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]), so its restriction to $\operatorname{Stab}(x)$ is an injective homomorphism with image $g\operatorname{Stab}(x)g^{-1} = \operatorname{Stab}(y)$.

^pf-26-3

*Uses:* [[§26 Stabilizers and Fixed Points#^prop-26-2|§26.2]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - Used in part (3) of [[§31 G Acting on Coset Spaces#^prop-31-1|The Action of G on G∕H, §31.1]]; for finite $G$ the equality of stabilizer orders along an orbit also follows from [[§30 Orbit–Stabilizer#^thm-30-3|Orbit–Stabilizer]].

> [!remark] Remark: Reading the Proposition
> Moving the point by $g$ conjugates its stabilizer by $g$. For the point stabilizer $H = \operatorname{Stab}(n) \subseteq S_n$ of [[§30 Orbit–Stabilizer#^def-30-1|Def. §30.1]], this says $\operatorname{Stab}(\sigma(n)) = \sigma H \sigma^{-1}$.

^rem-26-1
