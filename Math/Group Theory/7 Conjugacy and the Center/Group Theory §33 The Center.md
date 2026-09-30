---
type: section
subject: "[[Group Theory]]"
chapter: 7
section: 33
tags: [group-theory, math493]
---
← [[Group Theory §32 Conjugation as an Action and the Class Equation]] · ↑ [[Group Theory — 7 Conjugacy and the Center]] · [[Group Theory §34 Multiplying Cosets]] →

*Reference: Pinter Ch. 15, Exs. F–G.*

> [!definition] Definition §33.1: Central Elements; The Center $Z(G)$
> Let $G$ be a group and $z \in G$. We say $z$ is **central** in $G$ if $zg = gz$ for all $g \in G$. The set of all central elements in $G$ is called the **center** of $G$ and written $Z(G)$.
>
> *Source: WS 3*

^def-33-1

> [!theorem] Proposition §33.1: Central iff Singleton Conjugacy Class
> Let $G$ be a group and $z \in G$. Then $z$ is central in $G$ if and only if $\operatorname{Conj}(z) = \{z\}$.
>
> *Source: WS 3.5*

^prop-33-1

> [!proof]+ Proof
> For any $z$, $z \in \operatorname{Conj}(z)$ (take $g = e$), so $\operatorname{Conj}(z) = \{z\}$ says exactly that $gzg^{-1} = z$ for every $g \in G$. Multiplying on the right by $g$, this holds iff $gz = zg$ for every $g$, i.e. iff $z$ is central.

^pf-33-1

*Uses:* [[Group Theory §31 Conjugacy Classes#^def-31-1|Def. §31.1]], [[Group Theory §33 The Center#^def-33-1|Def. §33.1]]

> [!theorem] Proposition §33.2: The Center Is a Subgroup
> For any group $G$, the center $Z(G)$ is a subgroup of $G$. It is abelian, and $Z(G) = G$ if and only if $G$ is abelian.
>
> *Source: WS 3.6*

^prop-33-2

> [!proof]+ Proof
> *Subgroup:* $eg = g = ge$ for all $g$, so $e \in Z(G)$. If $z_1, z_2 \in Z(G)$ and $g \in G$, then
>
> $$
> (z_1z_2)g = z_1(z_2g) = z_1(gz_2) = (z_1g)z_2 = (gz_1)z_2 = g(z_1z_2),
> $$
>
> so $z_1z_2 \in Z(G)$. If $z \in Z(G)$, then from $zg = gz$, multiplying on both sides by $z^{-1}$ gives $gz^{-1} = z^{-1}g$, so $z^{-1} \in Z(G)$.
>
> *Abelian:* elements of $Z(G)$ commute with every element of $G$, in particular with each other.
>
> *$Z(G) = G$ iff $G$ abelian:* $Z(G) = G$ says every $z \in G$ commutes with every $g \in G$, which is the definition of abelian.

^pf-33-2

*Uses:* [[Group Theory §33 The Center#^def-33-1|Def. §33.1]], [[Group Theory §4 Subgroups#^def-4-1|Def. §4.1]], [[Group Theory §1 The Definition of a Group#^def-1-2|Def. §1.2]]

> [!remark] Remark: A Second Proof
> $Z(G)$ is the kernel of the homomorphism $G \to S_G$ given by the conjugation action ([[Group Theory §32 Conjugation as an Action and the Class Equation#^prop-32-1|§32.1]]), and kernels are subgroups ([[Group Theory §15 Homomorphisms#^prop-15-2|§15.2]]) — indeed normal subgroups ([[Group Theory §36 Sources of Normal Subgroups#^prop-36-2|§36.2]]).

^rem-33-1

> [!definition] Definition §33.2: $p$-Group
> For a prime $p$, a **$p$-group** is a group of order $p^k$ for some $k \geq 0$. [[Group Theory §33 The Center#^thm-33-3|The theorem below]] is the starting point for their structure theory.

^def-33-2

> [!theorem] Theorem §33.3: Groups of Prime-Power Order Have Nontrivial Center
> Let $p$ be prime and $|G| = p^k$ with $k \geq 1$. Then there is $g \neq e$ with $\operatorname{Conj}(g) = \{g\}$; such a $g$ commutes with every element of $G$. Thus $Z(G) \neq \{e\}$.
>
> *Source: PS 3.5*

^thm-33-3

> [!proof]+ Proof
> For each $g$, $|\operatorname{Conj}(g)| \cdot |C_G(g)| = p^k$, so $|\operatorname{Conj}(g)|$ is a divisor of $p^k$, hence ([[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|unique factorization]]) a power $p^{a}$ with $a \geq 0$. Take class representatives $g_1 = e, g_2, \ldots, g_c$, with $|\operatorname{Conj}(g_i)| = p^{a_i}$. Since the classes partition $G$,
>
> $$
> 1 + \sum_{i=2}^{c} p^{a_i} = p^k.
> $$
>
> If every $a_i \geq 1$ ($i \geq 2$), the left side is $1 + pm$ for an integer $m$, while $p \mid p^k$; then $p$ would divide $(1 + pm) - pm = 1$, which is absurd. So some $i \geq 2$ has $a_i = 0$, i.e. $\operatorname{Conj}(g_i) = \{g_i\}$ with $g_i \neq e$. By [[Group Theory §33 The Center#^prop-33-1|Central iff Singleton Conjugacy Class]], $g_i$ is central.

^pf-33-3

*Uses:* [[Group Theory §32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]], [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]], [[Group Theory §25 Orbits#^prop-25-1|§25.1]], [[Group Theory §32 Conjugation as an Action and the Class Equation#^prop-32-1|§32.1]], [[Group Theory §33 The Center#^prop-33-1|§33.1]]

> [!theorem] Corollary §33.4: $p$ Divides $|Z(G)|$
> If $|G| = p^k$ with $p$ prime and $k \geq 1$, then $p$ divides $|Z(G)|$; in particular $|Z(G)| \geq p$.

^cor-33-4

> [!proof]+ Proof
> In the class equation $|G| = |Z(G)| + \sum_i [G : C_G(g_i)]$ over representatives of the non-central classes ([[Group Theory §32 Conjugation as an Action and the Class Equation#^thm-32-4|§32.4]]), each index $[G : C_G(g_i)] = |\operatorname{Conj}(g_i)|$ divides $p^k$ and exceeds $1$, so it is a positive power of $p$. As $p$ divides $|G|$, it divides $|Z(G)| = |G| - \sum_i [G : C_G(g_i)]$. Since $e \in Z(G)$, $|Z(G)| \geq 1$, hence $|Z(G)| \geq p$.

^pf-33-4

*Uses:* [[Group Theory §32 Conjugation as an Action and the Class Equation#^thm-32-4|§32.4]], [[Group Theory §32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]], [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]], [[Group Theory §33 The Center#^prop-33-2|§33.2]]
