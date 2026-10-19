---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 38
tags: [group-theory, math493]
---
← [[§37 Multiplying Cosets]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§39 Sources of Normal Subgroups]] →

*Reference: Pinter Ch. 14, Exs. D–E.*

> [!definition] Definition §38.1: Normal Subgroup
> A subgroup $H$ of $G$ is a **normal subgroup** if $gHg^{-1} \subseteq H$ for all $g \in G$, i.e. $ghg^{-1} \in H$ for all $g \in G$ and $h \in H$. This is commonly written $H \trianglelefteq G$.
>
> *Source: lecture; WS 6*

^def-38-1

> [!remark]- Connections
> - 590 counterpart: [[§27 Free Groups and Presentations#^def-27-7|Normal Subgroup (590 §27.7)]].

> [!theorem] Proposition §38.1: First Examples of Normal Subgroups
> 1. Every subgroup of an abelian group is normal.
> 2. In any group $G$, the subgroups $\{e\}$ and $G$ are normal.
>
> *Source: lecture*

^prop-38-1

> [!proof]+ Proof
> (1) If $G$ is abelian, $ghg^{-1} = hgg^{-1} = h \in H$. (2) $geg^{-1} = e$, and $gxg^{-1} \in G$ for all $x$ by closure.

^pf-38-1

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]]

> [!remark] Remark: Where to Look for Non-Normal Subgroups
> To find a subgroup that is *not* normal one must therefore look in a non-abelian group, and at a proper nontrivial subgroup.

^rem-38-1

> [!theorem] Proposition §38.2: Characterizations of Normality
> For a subgroup $H$ of a group $G$, the following are equivalent:
> 1. $H$ is a normal subgroup of $G$, i.e. $gHg^{-1} \subseteq H$ for all $g \in G$;
> 2. $gHg^{-1} = H$ for all $g \in G$;
> 3. $gH = Hg$ for all $g \in G$;
> 4. the set of left cosets of $H$ equals the set of right cosets of $H$.
>
> *Source: lecture*

^prop-38-2

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
> **(4) $\Rightarrow$ (3).** Let $g \in G$. By (4), the left coset $gH$ is also a right coset, and it contains $g$. The right cosets partition $G$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]), and the one containing $g$ is $Hg$; hence $gH = Hg$.
>
> **(1) $\Rightarrow$ (3) directly (lecture 9/25).** Let $n \in N$. Then $gn = (gng^{-1})g \in Ng$, because $gng^{-1} \in N$; so $gN \subseteq Ng$. Similarly $ng = g(g^{-1}ng) \in gN$, because $g^{-1}ng = g^{-1}n(g^{-1})^{-1} \in N$; so $Ng \subseteq gN$.

^pf-38-2

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets (§38)]]

> [!remark]- Connections
> - Worksheet form: [[§38 Normal Subgroups#^thm-38-3|Five Characterizations of Normality]] (WS 6.1).

> [!remark] Remark: Multiplying Sets
> Here $gH$, $Hg$, $gHg^{-1}$ are subsets of $G$, and “multiplying an equality of subsets by $g$” means applying the bijection $x \mapsto xg$ of $G$ to both sides; this is legitimate for equalities of sets, and preserves inclusions as well.

^rem-38-2

> [!remark] Remark: Second Proof of (⇐) in Proposition §37.1 (lecture 9/25)
> Using products of subsets and $g_2'N = Ng_2'$ for normal $N$ ([[§38 Normal Subgroups#^prop-38-2|Characterizations of Normality]]): if $g_1N = g_1'N$ and $g_2N = g_2'N$, then
>
> $$ g_1g_2N = g_1g_2'N = g_1Ng_2' = g_1'Ng_2' = g_1'g_2'N. $$

^rem-38-3

*Uses:* [[§37 Multiplying Cosets#^prop-37-1|§37.1]], [[§38 Normal Subgroups#^prop-38-2|§38.2]], [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets]]

> [!theorem] Theorem §38.3: Five Characterizations of Normality
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

^thm-38-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* We show that each of (2), (3), (4), (5) is equivalent to (1). Throughout, recall that for a subgroup $N$ the inclusion “$gNg^{-1} \subseteq N$ for all $g \in G$” (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]) is equivalent to the equality (1), by Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]], (1) $\Leftrightarrow$ (2).
>
> **(1) $\Rightarrow$ (2).** Let $n \in N$. Then $n = ene^{-1} \in \operatorname{Conj}(n)$ (Definition [[§33 Conjugacy Classes#^def-33-1|§33.1]]), and for every $h \in G$ we have $hnh^{-1} \in hNh^{-1} = N$ by (1); so $\operatorname{Conj}(n) \subseteq N$. Hence
>
> $$ N = \bigcup_{n \in N} \{n\} \subseteq \bigcup_{n \in N} \operatorname{Conj}(n) \subseteq N, $$
>
> so $N = \bigcup_{n \in N} \operatorname{Conj}(n)$ is a union of conjugacy classes of $G$.
>
> **(2) $\Rightarrow$ (1).** Write $N = \bigcup_{i \in I} \operatorname{Conj}(x_i)$. Let $g \in G$ and $n \in N$. Then $n \in \operatorname{Conj}(x_i)$ for some $i \in I$, i.e. $n = hx_ih^{-1}$ for some $h \in G$, and, using $(gh)^{-1} = h^{-1}g^{-1}$ (Proposition [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]),
>
> $$ gng^{-1} = g\,(hx_ih^{-1})\,g^{-1} = (gh)\,x_i\,(gh)^{-1} \in \operatorname{Conj}(x_i) \subseteq N. $$
>
> So $gNg^{-1} \subseteq N$ for every $g \in G$, and (1) follows by Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]], (1) $\Rightarrow$ (2).
>
> **(1) $\Rightarrow$ (3).** By Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]](3), for every element $g'N$ of $G/N$,
>
> $$ \operatorname{Stab}(g'N) = g'N(g')^{-1} = N, $$
>
> the second equality by (1). So every element of $G/N$ has the same stabilizer, namely $N$.
>
> **(3) $\Rightarrow$ (1).** By (3), every element of $G/N$ has the same stabilizer as $eN$, and $\operatorname{Stab}(eN) = N$ by Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]](2). For $g \in G$, Proposition [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]](3) then gives
>
> $$ gNg^{-1} = \operatorname{Stab}(gN) = \operatorname{Stab}(eN) = N. $$
>
> **(1) $\Rightarrow$ (4).** Let $gN$ be a left coset. Multiplying the equality $gNg^{-1} = N$ of (1) on the right by $g$ (Remark [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets (§38)]]) gives $gN = Ng$; so $gN$ is the right coset $Ng$.
>
> **(4) $\Rightarrow$ (1).** Let $g \in G$. By (4), $gN = Nx$ for some $x \in G$. Now $g = ge \in gN = Nx$, and also $g = eg \in Ng$. The right cosets are the equivalence classes of $\equiv_r \pmod N$ (Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]](2)), and two equivalence classes with a common element are equal (Proposition [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]]); so $Nx = Ng$. Hence $gN = Ng$, and multiplying on the right by $g^{-1}$ (Remark [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets (§38)]]) gives $gNg^{-1} = N$.
>
> **(1) $\Leftrightarrow$ (5).** Condition (5) says precisely that the rule $(g_1N)(g_2N) := (g_1g_2)N$ is a well-defined operation on $G/N$, i.e. that the result does not depend on the representatives $g_1, g_2$ chosen. By Proposition [[§37 Multiplying Cosets#^prop-37-1|§37.1]], this holds if and only if $gNg^{-1} \subseteq N$ for all $g \in G$, which is equivalent to (1) by Proposition [[§38 Normal Subgroups#^prop-38-2|§38.2]], (1) $\Leftrightarrow$ (2).
>
> Finally, since (1) is equivalent to “$gNg^{-1} \subseteq N$ for all $g \in G$”, which is Definition [[§38 Normal Subgroups#^def-38-1|§38.1]], the subgroups satisfying (1)–(5) are exactly the normal subgroups of $G$.

^pf-38-3

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§38 Normal Subgroups#^prop-38-2|§38.2]], [[§33 Conjugacy Classes#^def-33-1|Def. §33.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]], [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets (§38)]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]], [[§37 Multiplying Cosets#^prop-37-1|§37.1]]

> [!remark]- Connections
> - Lecture form: [[§38 Normal Subgroups#^prop-38-2|Characterizations of Normality]].

> [!remark] Remark: Relation to the Lecture
> Four of the five conditions have already appeared: (1) is characterization (2) of [[§38 Normal Subgroups#^prop-38-2|Characterizations of Normality]] (lecture), (4) is its characterization (4), (5) is the well-definedness of coset multiplication ([[§37 Multiplying Cosets#^prop-37-1|§37.1]]), and (2) is [[§39 Sources of Normal Subgroups#^prop-39-7|Normal Subgroups Are Unions of Conjugacy Classes]] (§39). Condition (3) is new: it phrases normality through the action of $G$ on $G/N$ from Worksheet 5 ([[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]).

^rem-38-4

> [!example] Example §38.1: A Non-Normal Subgroup of $S_3$
> Let $G = S_3$ and $H = \{e, (1\,2)\}$. As computed in [[§28 Left and Right Cosets#^ex-28-1|Ex. §28.1]],
>
> $$ (1\,3)H = \{(1\,3),\ (1\,2\,3)\} \neq \{(1\,3),\ (1\,3\,2)\} = H(1\,3), $$
>
> so by the characterization (3) ([[§38 Normal Subgroups#^prop-38-2|§38.2]]), $H$ is not normal. Directly: $(1\,3)(1\,2)(1\,3)^{-1} = (3\,2) \notin H$ ([[§12 Multiplying and Conjugating Cycles#^prop-12-1|conjugation relabels the cycle]]).
>
> The subgroup $\langle(1\,2\,3)\rangle$ would have been a poor choice for a non-normal example: it has index $2$, and index-$2$ subgroups are always normal ([[§39 Sources of Normal Subgroups#^prop-39-1|below]]). The same computation works with any of the three transposition subgroups.
>
> *Source: lecture; WS 6.2(1)*

^ex-38-1
