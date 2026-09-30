---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 35
tags: [group-theory, math493]
---
← [[§34 Multiplying Cosets]] · ↑ [[8 Normal Subgroups and Quotient Groups]] · [[§36 Sources of Normal Subgroups]] →

*Reference: Pinter Ch. 14, Exs. D–E.*

> [!definition] Definition §35.1: Normal Subgroup
> A subgroup $H$ of $G$ is a **normal subgroup** if $gHg^{-1} \subseteq H$ for all $g \in G$, i.e. $ghg^{-1} \in H$ for all $g \in G$ and $h \in H$. This is commonly written $H \trianglelefteq G$.
>
> *Source: lecture; WS 6*

^def-35-1

> [!remark]- Connections
> - 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^def-21-12|Normal Subgroup (590 §21.12)]].

> [!theorem] Proposition §35.1: First Examples of Normal Subgroups
> 1. Every subgroup of an abelian group is normal.
> 2. In any group $G$, the subgroups $\{e\}$ and $G$ are normal.
>
> *Source: lecture*

^prop-35-1

> [!proof]+ Proof
> (1) If $G$ is abelian, $ghg^{-1} = hgg^{-1} = h \in H$. (2) $geg^{-1} = e$, and $gxg^{-1} \in G$ for all $x$ by closure.

^pf-35-1

*Uses:* [[§35 Normal Subgroups#^def-35-1|Def. §35.1]]

> [!remark] Remark: Where to Look for Non-Normal Subgroups
> To find a subgroup that is *not* normal one must therefore look in a non-abelian group, and at a proper nontrivial subgroup.

^rem-35-1

> [!theorem] Proposition §35.2: Characterizations of Normality
> For a subgroup $H$ of a group $G$, the following are equivalent:
> 1. $H$ is a normal subgroup of $G$, i.e. $gHg^{-1} \subseteq H$ for all $g \in G$;
> 2. $gHg^{-1} = H$ for all $g \in G$;
> 3. $gH = Hg$ for all $g \in G$;
> 4. the set of left cosets of $H$ equals the set of right cosets of $H$.
>
> *Source: lecture*

^prop-35-2

> [!proof]+ Proof
> **(2) $\Rightarrow$ (1)** is clear.
>
> **(1) $\Rightarrow$ (2).** Fix $g$. By (1), $gHg^{-1} \subseteq H$; we show $H \subseteq gHg^{-1}$. Let $h \in H$. Applying (1) with $g^{-1}$ in place of $g$ gives $h' := g^{-1}hg = g^{-1}h(g^{-1})^{-1} \in H$, and then $h = gh'g^{-1} \in gHg^{-1}$.
>
> **(2) $\Rightarrow$ (3)** follows by multiplying the equality $gHg^{-1} = H$ on the right by $g$: $gH = Hg$.
>
> **(3) $\Rightarrow$ (2)** follows by multiplying the equality $gH = Hg$ on the right by $g^{-1}$: $gHg^{-1} = H$.
>
> **(3) $\Rightarrow$ (4)** is clear: every left coset $gH$ equals the right coset $Hg$, and conversely.
>
> **(4) $\Rightarrow$ (3).** Let $g \in G$. By (4), the left coset $gH$ is also a right coset, and it contains $g$. The right cosets partition $G$ ([[§26 Left and Right Cosets#^prop-26-2|§26.2]]), and the one containing $g$ is $Hg$; hence $gH = Hg$.
>
> **(1) $\Rightarrow$ (3) directly (lecture 9/25).** Let $n \in N$. Then $gn = (gng^{-1})g \in Ng$, because $gng^{-1} \in N$; so $gN \subseteq Ng$. Similarly $ng = g(g^{-1}ng) \in gN$, because $g^{-1}ng = g^{-1}n(g^{-1})^{-1} \in N$; so $Ng \subseteq gN$.

^pf-35-2

*Uses:* [[§35 Normal Subgroups#^def-35-1|Def. §35.1]], [[§26 Left and Right Cosets#^prop-26-2|§26.2]], [[§35 Normal Subgroups#^rem-35-2|Multiplying Sets (§35)]]

> [!remark]- Connections
> - Worksheet form: [[§35 Normal Subgroups#^thm-35-3|Five Characterizations of Normality]] (WS 6.1).

> [!remark] Remark: Multiplying Sets
> Here $gH$, $Hg$, $gHg^{-1}$ are subsets of $G$, and “multiplying an equality of subsets by $g$” means applying the bijection $x \mapsto xg$ of $G$ to both sides; this is legitimate for equalities of sets, and preserves inclusions as well.

^rem-35-2

> [!theorem] Theorem §35.3: Five Characterizations of Normality
> Let $G$ be a group and $N$ a subgroup. The following are equivalent:
> 1. for all $g \in G$, $gNg^{-1} = N$;
> 2. $N$ is a union of (some of the) conjugacy classes of $G$;
> 3. all elements of $G/N$ have the same stabilizer, for the left action of $G$ on $G/N$;
> 4. every left coset of $N$ in $G$ is also a right coset;
> 5. if $g_1N = g_1'N$ and $g_2N = g_2'N$, then $g_1g_2N = g_1'g_2'N$.
>
> A subgroup satisfying these conditions is a normal subgroup, $N \trianglelefteq G$.
>
> *Source: WS 6.1*

^thm-35-3

> [!proof]- Proof
> *[To be proved.]*

^pf-35-3

> [!remark]- Connections
> - Lecture form: [[§35 Normal Subgroups#^prop-35-2|Characterizations of Normality]].

> [!remark] Remark: Relation to the Lecture
> Four of the five conditions have already appeared: (1) is characterization (2) of [[§35 Normal Subgroups#^prop-35-2|Characterizations of Normality]] (lecture), (4) is its characterization (4), (5) is the well-definedness of coset multiplication ([[§34 Multiplying Cosets#^prop-34-1|§34.1]]), and (2) is [[§36 Sources of Normal Subgroups#^prop-36-7|Normal Subgroups Are Unions of Conjugacy Classes]] (§36). Condition (3) is new: it phrases normality through the action of $G$ on $G/N$ from Worksheet 5 ([[§29 G Acting on Coset Spaces#^prop-29-1|§29.1]]).

^rem-35-3

> [!example] Example §35.1: A Non-Normal Subgroup of $S_3$
> Let $G = S_3$ and $H = \{e, (1\,2)\}$. As computed in [[§26 Left and Right Cosets#^ex-26-1|Ex. §26.1]],
>
> $$ (1\,3)H = \{(1\,3),\ (1\,2\,3)\} \neq \{(1\,3),\ (1\,3\,2)\} = H(1\,3), $$
>
> so by the characterization (3) ([[§35 Normal Subgroups#^prop-35-2|§35.2]]), $H$ is not normal. Directly: $(1\,3)(1\,2)(1\,3)^{-1} = (3\,2) \notin H$ ([[§12 Multiplying and Conjugating Cycles#^prop-12-1|conjugation relabels the cycle]]).
>
> The subgroup $\langle(1\,2\,3)\rangle$ would have been a poor choice for a non-normal example: it has index $2$, and index-$2$ subgroups are always normal ([[§36 Sources of Normal Subgroups#^prop-36-1|below]]). The same computation works with any of the three transposition subgroups.
>
> *Source: lecture; WS 6.2(1)*

^ex-35-1
