---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 29
tags: [group-theory, math493]
---
← [[Group Theory §28 Orbit–Stabilizer]] · ↑ [[Group Theory — 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[Group Theory §30 Examples꞉ Linear Groups and the Cube]] →

*Reference: Not treated in Pinter.*

*Source: Worksheet 5.*

> [!theorem] Proposition §29.1: The Action of $G$ on $G/H$
> Let $G$ be a group and $H$ a subgroup, and let $G/H$ be the set of left cosets of $H$.
> 1. The rule $g \star (g'H) := (gg')H$ is a well-defined action of $G$ on $G/H$.
> 2. This action has a single orbit (it is transitive), and $\operatorname{Stab}(eH) = H$.
> 3. For $g' \in G$, $\operatorname{Stab}(g'H) = g'Hg'^{-1}$.
>
> Thus for every subgroup $H$ there is a set with a transitive $G$-action containing a point whose stabilizer is $H$.
>
> *Source: WS 5.4*

^prop-29-1

> [!proof]+ Proof
> **(1)** *Well defined:* the rule uses a representative $g'$ of the coset $g'H$, so suppose $g'H = g''H$, i.e. $(g')^{-1}g'' \in H$. Then
>
> $$
> (gg')^{-1}(gg'') = (g')^{-1}g^{-1}gg'' = (g')^{-1}g'' \in H,
> $$
>
> so $(gg')H = (gg'')H$. *Axioms:* $e \star (g'H) = (eg')H = g'H$, and
>
> $$
> (g_1g_2) \star (g'H) = (g_1g_2g')H = g_1 \star \big((g_2g')H\big) = g_1 \star \big(g_2 \star (g'H)\big).
> $$
>
> **(2)** *Transitive:* given cosets $g'H$ and $g''H$, the element $g = g''(g')^{-1}$ satisfies
>
> $$
> g \star (g'H) = \big(g''(g')^{-1}g'\big)H = g''H;
> $$
>
> so any coset can be moved to any other, and $G/H$ is a single orbit. *Stabilizer of $eH$:* $g \star (eH) = gH$, so $g \in \operatorname{Stab}(eH)$ iff $gH = H$ iff $g \in H$ ([[Group Theory §26 Left and Right Cosets#^prop-26-2|§26.2]]). Hence $\operatorname{Stab}(eH) = H$.
>
> **(3)** Since $g'H = g' \star (eH)$, the [[Group Theory §24 Stabilizers and Fixed Points#^cor-24-3|corollary on stabilizers along an orbit]] gives
>
> $$
> \operatorname{Stab}(g'H) = g' \operatorname{Stab}(eH) (g')^{-1} = g'H(g')^{-1}.
> $$

^pf-29-1

*Uses:* [[Group Theory §26 Left and Right Cosets#^prop-26-2|§26.2]], [[Group Theory §23 Actions#^def-23-1|Def. §23.1]], [[Group Theory §25 Orbits#^def-25-1|Def. §25.1]], [[Group Theory §24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]], [[Group Theory §24 Stabilizers and Fixed Points#^cor-24-3|§24.3]]

![[m493-29-1.svg]]
*$S_3$ acting on $S_3/H$ for $H = \{e, (1\,2)\}$: the three points are the three left cosets. Single elements carry $eH$ to each other coset, and $(1\,2\,3) = (2\,3)(1\,3)^{-1}$ carries $(1\,3)H$ to $(2\,3)H$, as in the proof of transitivity. The stabilizers (red) are the conjugates $g'H(g')^{-1}$, one for each point.*

> [!remark]- Connections
> - The homomorphism $G \to S_{G/H}$ of this action produces a normal subgroup inside $H$: [[Group Theory §36 Sources of Normal Subgroups#^thm-36-5|A Normal Subgroup Inside a Subgroup of Finite Index, §36.5]], whose kernel is [[Group Theory §36 Sources of Normal Subgroups#^prop-36-6|The Normal Core, §36.6]].
