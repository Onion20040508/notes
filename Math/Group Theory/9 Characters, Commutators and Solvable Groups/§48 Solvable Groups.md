---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 48
tags: [group-theory, math493]
---
← [[§47 Commutators]] · ↑ [[· 9 Characters, Commutators and Solvable Groups]] · [[§49 The Derived Series]] →

*Reference: not covered in the Pinter chapters used so far.*

> [!definition] Definition §48.1: Solvable Group
> A group $G$ is **solvable** if there is a chain of [[§4 Subgroups#^def-4-1|subgroups]]
>
> $$ \{e\} = G_0 \trianglelefteq G_1 \trianglelefteq G_2 \trianglelefteq \cdots \trianglelefteq G_N = G $$
>
> in which each $G_{j-1}$ is [[§38 Normal Subgroups#^def-38-1|normal]] in $G_j$ and each [[§40 Quotient Groups#^def-40-1|quotient]] $G_j/G_{j-1}$ is [[§1 The Definition of a Group#^def-1-2|abelian]].
>
> *Source: WS 9*

^def-48-1

> [!remark] Remark: Normal in the Next Term Only
> Each $G_{j-1}$ is required to be [[§38 Normal Subgroups#^def-38-1|normal]] in $G_j$, not in $G$. For example, in the chain for $S_4$ [[§48 Solvable Groups#^prop-48-1|below]], $K$ is normal in $A_4$ (and happens to be normal in $S_4$ as well), but in general the terms of such a chain need not be normal in $G$. Every [[§1 The Definition of a Group#^def-1-2|abelian]] group is [[§48 Solvable Groups#^def-48-1|solvable]], via the chain $\{e\} \trianglelefteq G$.

^rem-48-1

> [!theorem] Proposition §48.1: $S_3$ and $S_4$ Are Solvable
> The chains
>
> $$ \{e\} \trianglelefteq A_3 \trianglelefteq S_3 \qquad\text{and}\qquad \{e\} \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4 $$
>
> have the required properties, so $S_3$ and $S_4$ are [[§48 Solvable Groups#^def-48-1|solvable]].
>
> *Source: WS 9.1*

^prop-48-1

> [!proof]+ Proof
> *$S_3$.* $A_3$ is normal in $S_3$ (index $2$, [[§39 Sources of Normal Subgroups#^prop-39-1|Proposition §39.1]]), and $A_3/\{e\} \cong A_3 \cong \mathbb{Z}/3\mathbb{Z}$ and $S_3/A_3 \cong \{\pm 1\}$ are abelian (the sign, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|Theorem §21.3]], and the First Isomorphism Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).
>
> *$S_4$.* $K \trianglelefteq A_4$ and $A_4/K \cong \mathbb{Z}/3\mathbb{Z}$ (The Pair-Partition Homomorphism, [[§43 Simple Groups#^prop-43-10|Proposition §43.10]]); $A_4 \trianglelefteq S_4$ (index $2$) with $S_4/A_4 \cong \{\pm 1\}$; and $K/\{e\} \cong K$ is abelian, having order $4$ (Groups of Order $4$ Are Abelian, [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|Proposition §34.6]]). All three quotients are abelian.

^pf-48-1

*Uses:* [[§48 Solvable Groups#^def-48-1|Def. §48.1]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§43 Simple Groups#^prop-43-10|§43.10]], [[§34 Conjugation as an Action and the Class Equation#^prop-34-6|§34.6]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!remark]- Connections
> - The same chains are the derived series of $S_3$ and $S_4$: [[§49 The Derived Series#^ex-49-1|Ex. §49.1]] (1) and (2).

> [!theorem] Proposition §48.2: Subgroups of Solvable Groups Are Solvable
> If $G$ is [[§48 Solvable Groups#^def-48-1|solvable]] and $S \leq G$, then $S$ is solvable.
>
> *Source: WS 9.2; lecture 10/7*

^prop-48-2

> [!proof]+ Proof
> Let $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ be a chain as in [[§48 Solvable Groups#^def-48-1|the definition]]. We show that
>
> $$ \{e\} = S \cap G_0 \;\leq\; S \cap G_1 \;\leq\; \cdots \;\leq\; S \cap G_N = S $$
>
> is such a chain for $S$.
>
> *Normality.* Let $g \in S \cap G_{j-1}$ and $h \in S \cap G_j$. Then $hgh^{-1} \in G_{j-1}$, since $h \in G_j$, $g \in G_{j-1}$ and $G_{j-1} \trianglelefteq G_j$; and $hgh^{-1} \in S$, since $g, h \in S$. So $hgh^{-1} \in S \cap G_{j-1}$, and $S \cap G_{j-1} \trianglelefteq S \cap G_j$.
>
> *Abelian quotients.* The composite $\alpha: S \cap G_j \hookrightarrow G_j \twoheadrightarrow G_j/G_{j-1}$ is a homomorphism with kernel $(S \cap G_j) \cap G_{j-1} = S \cap G_{j-1}$ (Restricting a Homomorphism, [[§41 The First and Second Isomorphism Theorems#^lem-41-4|Lemma §41.4]]). By the First Isomorphism Theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|Theorem §41.1]]), $(S \cap G_j)/(S \cap G_{j-1}) \cong \operatorname{Im}\alpha$, a subgroup of the abelian group $G_j/G_{j-1}$, hence abelian.

^pf-48-2

*Uses:* [[§48 Solvable Groups#^def-48-1|Def. §48.1]], [[§4 Subgroups#^prop-4-3|§4.3]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!theorem] Proposition §48.3: Quotients of Solvable Groups Are Solvable
> If $G$ is [[§48 Solvable Groups#^def-48-1|solvable]] and $\pi: G \to Q$ is a surjective [[§15 Homomorphisms#^def-15-1|homomorphism]] (for instance, the [[§40 Quotient Groups#^prop-40-2|projection]] onto a [[§40 Quotient Groups#^def-40-1|quotient group]] $G/N$), then $Q$ is solvable. The natural candidate chain is
>
> $$ \{e\} = \pi(G_0) \;\leq\; \pi(G_1) \;\leq\; \cdots \;\leq\; \pi(G_N) = Q. $$
>
> *Source: WS 9.3*

^prop-48-3

> [!proof]- Proof
> *[To be proved.]*

^pf-48-3

> [!remark] Remark: Status of WS 9.3
> The lecture set up the [[§48 Solvable Groups#^prop-48-3|chain]] $\pi(G_j)$ and postponed the verification (normality of $\pi(G_{j-1})$ in $\pi(G_j)$, and abelian quotients) to Friday, Oct 9.

^rem-48-2
