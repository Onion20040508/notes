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
> Each $G_{j-1}$ is required to be [[§38 Normal Subgroups#^def-38-1|normal]] in $G_j$, not in $G$. For example, in the chain for $S_4$ [[§48 Solvable Groups#^prop-48-1|below]], $K$ is normal in $A_4$ (and happens to be normal in $S_4$ as well), but in general the terms of such a chain need not be normal in $G$. Normality is not transitive: $A \trianglelefteq B \trianglelefteq C$ does not imply $A \trianglelefteq C$ (PS 6.1; an example will be added once Problem Set 6 is submitted). Every [[§1 The Definition of a Group#^def-1-2|abelian]] group is [[§48 Solvable Groups#^def-48-1|solvable]], via the chain $\{e\} \trianglelefteq G$.

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
> *Source: WS 9.2; lecture 10/7, 10/9*

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
>
> *Second proof of the abelian step (lecture 10/9).* By Abelian Quotients and Commutators ([[§47 Commutators#^prop-47-11|Proposition §47.11]]), it suffices to show that every commutator of $S \cap G_j$ lies in $S \cap G_{j-1}$. Let $g, h \in S \cap G_j$. Then $ghg^{-1}h^{-1} \in G_{j-1}$, because $g, h \in G_j$ and $G_j/G_{j-1}$ is abelian; and $ghg^{-1}h^{-1} \in S$, because $g, h \in S$.

^pf-48-2

*Uses:* [[§48 Solvable Groups#^def-48-1|Def. §48.1]], [[§4 Subgroups#^prop-4-3|§4.3]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]], [[§47 Commutators#^prop-47-11|§47.11]]

> [!theorem] Proposition §48.3: Quotients of Solvable Groups Are Solvable
> If $G$ is [[§48 Solvable Groups#^def-48-1|solvable]] and $\pi: G \to Q$ is a surjective [[§15 Homomorphisms#^def-15-1|homomorphism]] (for instance, the [[§40 Quotient Groups#^prop-40-2|projection]] onto a [[§40 Quotient Groups#^def-40-1|quotient group]] $G/N$), then $Q$ is solvable. The natural candidate chain is
>
> $$ \{e\} = \pi(G_0) \;\leq\; \pi(G_1) \;\leq\; \cdots \;\leq\; \pi(G_N) = Q. $$
>
> *Source: WS 9.3; lecture 10/9*

^prop-48-3

> [!proof]+ Proof
> *(Lecture 10/9.)* Let $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ be a chain with abelian quotients. Each $\pi(G_j)$ is a subgroup of $Q$, being the image of a subgroup under a homomorphism (Images and Preimages of Subgroups, [[§15 Homomorphisms#^prop-15-4|Proposition §15.4]]). Also $G_{j-1} \subseteq G_j$ gives $\pi(G_{j-1}) \subseteq \pi(G_j)$; $\pi(G_0) = \{\pi(e)\} = \{e\}$; and $\pi(G_N) = \pi(G) = Q$, since $\pi$ is surjective.
>
> *Normality.* Let $\pi(h) \in \pi(G_{j-1})$ and $\pi(g) \in \pi(G_j)$, with $h \in G_{j-1}$ and $g \in G_j$. Then
>
> $$ \pi(g)\,\pi(h)\,\pi(g)^{-1} = \pi(ghg^{-1}) \in \pi(G_{j-1}), $$
>
> since $ghg^{-1} \in G_{j-1}$, as $G_{j-1} \trianglelefteq G_j$. So $\pi(G_{j-1}) \trianglelefteq \pi(G_j)$.
>
> *Abelian quotients.* By Abelian Quotients and Commutators ([[§47 Commutators#^prop-47-11|Proposition §47.11]]), it suffices to show that every commutator of $\pi(G_j)$ lies in $\pi(G_{j-1})$. Let $g, h \in G_j$. Since $G_j/G_{j-1}$ is abelian, the same proposition gives $ghg^{-1}h^{-1} \in G_{j-1}$. Hence
>
> $$ \pi(g)\,\pi(h)\,\pi(g)^{-1}\pi(h)^{-1} = \pi(ghg^{-1}h^{-1}) \in \pi(G_{j-1}). $$
>
> So $\pi(G_j)/\pi(G_{j-1})$ is abelian, and $Q$ is solvable.

^pf-48-3

*Uses:* [[§48 Solvable Groups#^def-48-1|Def. §48.1]], [[§15 Homomorphisms#^prop-15-4|§15.4]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§47 Commutators#^prop-47-11|§47.11]]

> [!theorem] Proposition §48.4: Subquotients: An Injection and a Surjection
> Let $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ be a chain, let $S \leq G$, and let $\pi: G \to Q$ be a surjective [[§15 Homomorphisms#^def-15-1|homomorphism]].
> 1. $x(S \cap G_{j-1}) \mapsto xG_{j-1}$ is a well-defined injective homomorphism
>
>    $$ (S \cap G_j)/(S \cap G_{j-1}) \hookrightarrow G_j/G_{j-1}. $$
>
> 2. $xG_{j-1} \mapsto \pi(x)\pi(G_{j-1})$ is a well-defined surjective homomorphism
>
>    $$ G_j/G_{j-1} \twoheadrightarrow \pi(G_j)/\pi(G_{j-1}). $$
>
> So each quotient of the chain for $S$ is (isomorphic to) a *subgroup* of the corresponding quotient for $G$, and each quotient of the chain for $Q$ is a *quotient* (homomorphic image) of it. Since subgroups and homomorphic images of abelian groups are abelian, this proves the abelian steps of WS 9.2 and WS 9.3 once more ([[§48 Solvable Groups#^prop-48-2|Proposition §48.2]], [[§48 Solvable Groups#^prop-48-3|Proposition §48.3]]).
>
> *Source: lecture 10/9*

^prop-48-4

> [!proof]+ Proof
> **(1)** This is the map induced by $\alpha: S \cap G_j \to G_j/G_{j-1}$, $x \mapsto xG_{j-1}$, whose kernel is $S \cap G_{j-1}$ (proof of Subgroups of Solvable Groups Are Solvable, [[§48 Solvable Groups#^prop-48-2|Proposition §48.2]]). By the First Isomorphism Theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|Theorem §41.1]]) it is a well-defined isomorphism onto $\operatorname{Im}\alpha$, hence injective into $G_j/G_{j-1}$.
>
> **(2)** Let $\varphi: G_j \to \pi(G_j)/\pi(G_{j-1})$, $\varphi(x) = \pi(x)\pi(G_{j-1})$, the restriction of $\pi$ to $G_j$ followed by the projection; it is a surjective homomorphism, and $G_{j-1} \subseteq \operatorname{Ker}\varphi$ because $\pi(G_{j-1})$ is the identity of the target. *Well defined on cosets:* if $xG_{j-1} = yG_{j-1}$, then $y = xn$ with $n \in G_{j-1}$, so $\varphi(y) = \varphi(x)\varphi(n) = \varphi(x)$. The induced map is a homomorphism because $\varphi$ is, and surjective because $\varphi$ is.

^pf-48-4

*Uses:* [[§48 Solvable Groups#^prop-48-2|§48.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]]

> [!remark] Remark: The Trap: Do Not Cancel $N$
> For $Q = G/N$, the isomorphism theorems describe the pieces of the chain for $Q$:
>
> $$ \pi(G_j) \cong G_j/(G_j \cap N) \cong G_jN/N $$
>
> (First, then Second Isomorphism Theorem, [[§41 The First and Second Isomorphism Theorems#^thm-41-1|Theorems §41.1]] and [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]), and so, by the Third Isomorphism Theorem ([[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|Theorem §42.5]]),
>
> $$ \pi(G_j)/\pi(G_{j-1}) \cong (G_jN/N)\big/(G_{j-1}N/N) \cong G_jN/G_{j-1}N. $$
>
> It is tempting to “cancel $N$” and conclude $\pi(G_j)/\pi(G_{j-1}) \cong G_j/G_{j-1}$. This is false in general: for $N = G$, every $\pi(G_j)$ is trivial, while $G_j/G_{j-1}$ need not be. The correct relation is the surjection of part (2) of [[§48 Solvable Groups#^prop-48-4|Proposition §48.4]]: $G_j/G_{j-1}$ maps *onto* $\pi(G_j)/\pi(G_{j-1})$, with a kernel that can be nontrivial. The lecture's advice: rather than chase isomorphism-theorem formulas, write down the obviously well-defined injection or surjection.

^rem-48-2
