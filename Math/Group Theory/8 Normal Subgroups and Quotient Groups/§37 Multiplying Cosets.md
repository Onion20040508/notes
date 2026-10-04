---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 37
tags: [group-theory, math493]
---
← [[§36 S₃, S₄ and GLₙ]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§38 Normal Subgroups]] →

*Reference: Pinter Ch. 15.*

> [!remark] Remark: Motivation: Quotients
> A recurring construction throughout mathematics: impose an equivalence relation on an object and try to transport its structure to the set of equivalence classes. In topology this produces [[§12 Quotient Topology#^def-12-3|quotient spaces]] (590 notes); in algebra it sometimes works and sometimes does not, and it is important to understand exactly when. Here the object is a group $G$, the equivalence relation is left congruence modulo a subgroup $H$ ([[§28 Left and Right Cosets#^def-28-1|Def. §28.1]]), and the classes are the left cosets $gH$, forming the set $G/H$. The model case is $G = \mathbb{Z}$, $H = n\mathbb{Z}$, where the classes are residue classes and $\mathbb{Z}/n\mathbb{Z}$ inherits addition ([[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]).
>
> *Vector spaces (lecture 9/25).* For a vector space $V$ and a subspace $W$ there is a [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|quotient space]] $V/W$ in which the vectors of $W$ are set to zero. The construction is the same as for groups; it is easier only because addition of vectors is commutative, so every subspace plays the role of a normal subgroup. For groups one must distinguish subgroups from normal subgroups.

^rem-37-1

The natural attempt is to multiply cosets by multiplying representatives:

$$ (g_1H)(g_2H) := (g_1g_2)H. $$

Since the right side is computed from the chosen representatives $g_1, g_2$, this rule is *not necessarily well defined*.

> [!theorem] Proposition §37.1: When Coset Multiplication Is Well Defined
> Let $H$ be a subgroup of $G$. The rule $(g_1H)(g_2H) := (g_1g_2)H$ gives a well-defined operation on $G/H$ if and only if
>
> $$ gHg^{-1} \subseteq H \quad \text{for all } g \in G, \qquad \text{where } gHg^{-1} := \{ghg^{-1} : h \in H\}. $$
>
> *Source: lecture*

^prop-37-1

> [!proof]+ Proof
> Well-definedness means: whenever $u_1H = u_2H$ and $v_1H = v_2H$, also $(u_1v_1)H = (u_2v_2)H$. By the coset criterion $aH = bH \iff a^{-1}b \in H$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]), the hypotheses are $u_1^{-1}u_2 \in H$ and $v_1^{-1}v_2 \in H$, and the desired conclusion is $(u_1v_1)^{-1}(u_2v_2) \in H$. Compute
>
> $$ (u_1v_1)^{-1}(u_2v_2) = v_1^{-1}u_1^{-1}u_2v_2 = \big(v_1^{-1}(u_1^{-1}u_2)v_1\big)\big(v_1^{-1}v_2\big). $$
>
> Since the second factor lies in $H$, the conclusion holds if and only if $v_1^{-1}(u_1^{-1}u_2)v_1 \in H$.
>
> ($\Leftarrow$) If $gHg^{-1} \subseteq H$ for all $g$, take $g = v_1^{-1}$: then $v_1^{-1}(u_1^{-1}u_2)v_1 \in H$, since $u_1^{-1}u_2 \in H$.
>
> ($\Rightarrow$) Suppose the operation is well defined, and let $g \in G$, $h \in H$. Take $u_1 = e$, $u_2 = h$, and $v_1 = v_2 = g^{-1}$. The hypotheses hold ($u_1^{-1}u_2 = h \in H$, $v_1^{-1}v_2 = e \in H$), so the conclusion gives $v_1^{-1}(u_1^{-1}u_2)v_1 = ghg^{-1} \in H$.
>
> A second proof of ($\Leftarrow$), from lecture 9/25, multiplies cosets as sets; it needs [[§38 Normal Subgroups|§38]] and is given there, after [[§38 Normal Subgroups#^rem-38-2|Remark: Multiplying Sets]] ([[§38 Normal Subgroups#^rem-38-3|Second Proof of (⇐)]]).

^pf-37-1

*Uses:* [[§28 Left and Right Cosets#^prop-28-2|§28.2]]

![[m493-34-1.svg]]
*Left: for $H = \{e, (1\,2)\}$, both $e$ and $(1\,2)$ represent the coset $H$, but multiplying them by $(1\,3)$ (red) lands in two different cosets, $(1\,3)H$ and $(2\,3)H$, so $H \cdot (1\,3)H$ has no well-defined value. This is the ($\Rightarrow$) step of the proof with $h = (1\,2)$ and $g = (1\,3)$: $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3) \notin H$. Right: for the normal subgroup $A_3$, every representative of $A_3$ times $(1\,3)$ lands in the same coset $(1\,2)A_3$.*

> [!remark]- Connections
> - 590 version of this computation: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-19|Why Normality is Required]].
> - Vector-space version (automatic, since addition commutes): [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]].
> - Worksheet form of this condition: item (5) of [[§38 Normal Subgroups#^thm-38-3|Five Characterizations of Normality]].
