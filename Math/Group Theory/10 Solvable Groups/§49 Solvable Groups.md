---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 49
tags: [group-theory, math493]
---
← [[§48 S₃, Aₙ and GLₙ]] · ↑ [[· 10 Solvable Groups]] · [[§50 The Derived Series]] →

*Reference: not covered in the Pinter chapters used so far.*

> [!definition] Definition §49.1: Solvable Group
> A group $G$ is **solvable** if there is a chain of [[§4 Subgroups#^def-4-1|subgroups]]
>
> $$ \{e\} = G_0 \trianglelefteq G_1 \trianglelefteq G_2 \trianglelefteq \cdots \trianglelefteq G_N = G $$
>
> in which each $G_{j-1}$ is [[§38 Normal Subgroups#^def-38-1|normal]] in $G_j$ and each [[§40 Quotient Groups#^def-40-1|quotient]] $G_j/G_{j-1}$ is [[§1 The Definition of a Group#^def-1-2|abelian]].
>
> *Source: WS 9*

^def-49-1

> [!remark] Remark: Normal in the Next Term Only
> Each $G_{j-1}$ is required to be [[§38 Normal Subgroups#^def-38-1|normal]] in $G_j$, not in $G$. For example, in the chain for $S_4$ [[§49 Solvable Groups#^prop-49-1|below]], $V$ is normal in $A_4$ (and happens to be normal in $S_4$ as well), but in general the terms of such a chain need not be normal in $G$. Every [[§1 The Definition of a Group#^def-1-2|abelian]] group is [[§49 Solvable Groups#^def-49-1|solvable]], via the chain $\{e\} \trianglelefteq G$.

^rem-49-1

> [!theorem] Proposition §49.1: $S_3$ and $S_4$ Are Solvable
> The chains
>
> $$ \{e\} \trianglelefteq A_3 \trianglelefteq S_3 \qquad\text{and}\qquad \{e\} \trianglelefteq V \trianglelefteq A_4 \trianglelefteq S_4 $$
>
> have the required properties, so $S_3$ and $S_4$ are [[§49 Solvable Groups#^def-49-1|solvable]].
>
> *Source: WS 9.1*

^prop-49-1

> [!proof]+ Proof
> *$S_3$.* $A_3$ is normal in $S_3$ (index $2$, [[§39 Sources of Normal Subgroups#^prop-39-1|Proposition §39.1]]), and $A_3/\{e\} \cong A_3 \cong \mathbb{Z}/3\mathbb{Z}$ and $S_3/A_3 \cong \{\pm 1\}$ are abelian (the sign, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|Theorem §21.3]], and the First Isomorphism Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).
>
> *$S_4$.* $V \trianglelefteq A_4$ and $A_4/V \cong \mathbb{Z}/3\mathbb{Z}$ (The Pair-Partition Homomorphism, [[§43 Simple Groups#^prop-43-10|Proposition §43.10]]); $A_4 \trianglelefteq S_4$ (index $2$) with $S_4/A_4 \cong \{\pm 1\}$; and $V/\{e\} \cong V$ is abelian, having order $4$ (Groups of Order $4$ Are Abelian, [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|Proposition §34.6]]). All three quotients are abelian.

^pf-49-1

*Uses:* [[§49 Solvable Groups#^def-49-1|Def. §49.1]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§43 Simple Groups#^prop-43-10|§43.10]], [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|§34.6]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!remark]- Connections
> - The same chains are the derived series of $S_3$ and $S_4$: [[§50 The Derived Series#^ex-50-1|Ex. §50.1]] (1) and (2).

> [!theorem] Proposition §49.2: Subgroups of Solvable Groups Are Solvable
> If $G$ is [[§49 Solvable Groups#^def-49-1|solvable]] and $S \leq G$, then $S$ is solvable.
>
> *Source: WS 9.2; lecture 10/7*

^prop-49-2

> [!proof]+ Proof
> Let $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ be a chain as in [[§49 Solvable Groups#^def-49-1|the definition]]. We show that
>
> $$ \{e\} = S \cap G_0 \;\leq\; S \cap G_1 \;\leq\; \cdots \;\leq\; S \cap G_N = S $$
>
> is such a chain for $S$.
>
> *Normality.* Let $g \in S \cap G_{j-1}$ and $h \in S \cap G_j$. Then $hgh^{-1} \in G_{j-1}$, since $h \in G_j$, $g \in G_{j-1}$ and $G_{j-1} \trianglelefteq G_j$; and $hgh^{-1} \in S$, since $g, h \in S$. So $hgh^{-1} \in S \cap G_{j-1}$, and $S \cap G_{j-1} \trianglelefteq S \cap G_j$.
>
> *Abelian quotients.* The composite $\alpha: S \cap G_j \hookrightarrow G_j \twoheadrightarrow G_j/G_{j-1}$ is a homomorphism with kernel $(S \cap G_j) \cap G_{j-1} = S \cap G_{j-1}$ (Restricting a Homomorphism, [[§41 The First and Second Isomorphism Theorems#^lem-41-4|Lemma §41.4]]). By the First Isomorphism Theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|Theorem §41.1]]), $(S \cap G_j)/(S \cap G_{j-1}) \cong \operatorname{Im}\alpha$, a subgroup of the abelian group $G_j/G_{j-1}$, hence abelian.

^pf-49-2

*Uses:* [[§49 Solvable Groups#^def-49-1|Def. §49.1]], [[§4 Subgroups#^prop-4-3|§4.3]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!theorem] Proposition §49.3: Quotients of Solvable Groups Are Solvable
> If $G$ is [[§49 Solvable Groups#^def-49-1|solvable]] and $\pi: G \to Q$ is a surjective [[§15 Homomorphisms#^def-15-1|homomorphism]] (for instance, the [[§40 Quotient Groups#^prop-40-2|projection]] onto a [[§40 Quotient Groups#^def-40-1|quotient group]] $G/N$), then $Q$ is solvable. The natural candidate chain is
>
> $$ \{e\} = \pi(G_0) \;\leq\; \pi(G_1) \;\leq\; \cdots \;\leq\; \pi(G_N) = Q. $$
>
> *Source: WS 9.3*

^prop-49-3

> [!proof]- Proof
> *[To be proved.]*

^pf-49-3

> [!remark] Remark: Status of WS 9.3
> The lecture set up the [[§49 Solvable Groups#^prop-49-3|chain]] $\pi(G_j)$ and postponed the verification (normality of $\pi(G_{j-1})$ in $\pi(G_j)$, and abelian quotients) to Friday, Oct 9.

^rem-49-2
