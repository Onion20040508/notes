---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 42
tags: [group-theory, math493]
---
← [[§41 The First Isomorphism Theorem]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§43 Simple Groups]] →

*Source: Lecture (Fri Oct 2).*

> [!definition] Definition §42.1: The Product Set $HN$
> For [[§4 Subgroups#^def-4-1|subgroups]] $H, N$ of $G$, write $HN := \{hn : h \in H,\ n \in N\}$.

^def-42-1

> [!theorem] Lemma §42.1: $HN$ Is a Subgroup When $N$ Is Normal
> If $H \leq G$ and $N \trianglelefteq G$ ([[§38 Normal Subgroups#^def-38-1|Def. §38.1]]), then $HN$ ([[§42 The Second and Third Isomorphism Theorems#^def-42-1|Def. §42.1]]) is a subgroup of $G$, and it contains both $H$ and $N$.
>
> *Source: lecture 10/2; PS 4.1(2)*

^lem-42-1

> [!proof]+ Proof
> *Closure (lecture).* Let $h_1, h_2 \in H$ and $n_1, n_2 \in N$. Since $N$ is normal, $n_1h_2 = h_2n'$ for some $n' \in N$ ($n' = h_2^{-1}n_1h_2$). So $h_1n_1 \cdot h_2n_2 = h_1h_2 \cdot n'n_2 \in HN$. *Containment:* $h = he$ and $n = en$.
>
> *Identity (PS 4.1(2)).* $e = ee \in HN$, since $e \in H$ and $e \in N$.
>
> *Inverses (PS 4.1(2)).* For $hn \in HN$, $(hn)^{-1} = n^{-1}h^{-1} = h^{-1}\big(hn^{-1}h^{-1}\big)$ ([[§2 First Consequences of the Axioms#^prop-2-4|Inverse of a Product]]). Here $h^{-1} \in H$, and $hn^{-1}h^{-1} \in N$ by [[§38 Normal Subgroups#^def-38-1|normality]] applied to $n^{-1} \in N$; so $(hn)^{-1} \in HN$.
>
> By the symmetric argument, $HN$ is also a subgroup when $H$, rather than $N$, is normal (as [[493 Problem Set 4#^hw-4-1|PS 4.1(2)]] notes). Without either hypothesis it can fail: $AB$ Need Not Be a Subgroup ([[§42 The Second and Third Isomorphism Theorems#^ex-42-1|Ex. §42.1]]), below.

^pf-42-1

*Uses:* [[§42 The Second and Third Isomorphism Theorems#^def-42-1|Def. §42.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!theorem] Theorem §42.2: Second Isomorphism Theorem
> Let $G$ be a group, $N \trianglelefteq G$, $H \leq G$, and $\pi: G \to G/N$ the [[§40 Quotient Groups#^def-40-1|projection]]. Then $H \cap N \trianglelefteq H$, $N \trianglelefteq HN$ ([[§42 The Second and Third Isomorphism Theorems#^def-42-1|Def. §42.1]], [[§42 The Second and Third Isomorphism Theorems#^lem-42-1|§42.1]]), $\pi(H) = \pi(HN)$, and
>
> $$ H/(H \cap N) \;\cong\; \pi(H) \;=\; \pi(HN) \;\cong\; HN/N. $$
>
> In particular $H/(H \cap N) \cong HN/N$.
>
> *Source: lecture 10/2*

^thm-42-2

> [!proof]+ Proof
> *$\pi(H) = \pi(HN)$.* For $h \in H$, $\pi(h) = \pi(he) \in \pi(HN)$. For $hn \in HN$, $\pi(hn) = \pi(h)\pi(n) = \pi(h) \in \pi(H)$, since $n \in N = \operatorname{Ker}\pi$ ([[§40 Quotient Groups#^prop-40-2|§40.2]]).
>
> *Two applications of the [[§41 The First Isomorphism Theorem#^thm-41-1|First Isomorphism Theorem]]* (§38). Restrict $\pi$ to $H$: the kernel is $\{h \in H : hN = N\} = H \cap N$, so $H \cap N$ is normal in $H$ ([[§39 Sources of Normal Subgroups#^prop-39-2|Kernels Are Normal]]) and $H/(H \cap N) \cong \pi(H)$. Restrict $\pi$ to $HN$: the kernel is $HN \cap N = N$, since $N \subseteq HN$ ([[§42 The Second and Third Isomorphism Theorems#^lem-42-1|§42.1]]), so $N \trianglelefteq HN$ and $HN/N \cong \pi(HN)$. Combining with $\pi(H) = \pi(HN)$ gives the chain.

^pf-42-2

*Uses:* [[§42 The Second and Third Isomorphism Theorems#^def-42-1|Def. §42.1]], [[§42 The Second and Third Isomorphism Theorems#^lem-42-1|§42.1]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First Isomorphism Theorem#^thm-41-1|§41.1]]

![[m493-38-3.svg]]
*The “diamond” picture of the Second Isomorphism Theorem: lines denote inclusion, and the two marked quotients on opposite sides agree, $HN/N \cong H/(H \cap N)$.*

> [!theorem] Corollary §42.3: Subgroup Representatives, Again
> If a [[§40 Quotient Groups#^def-40-2|set of representatives]] $S$ for $G/N$ is a [[§4 Subgroups#^def-4-1|subgroup]], then $S \cong G/N$.
>
> *Source: lecture 10/2*

^cor-42-3

> [!proof]+ Proof
> Take $H = S$. Every $g \in G$ lies in some coset $sN$ with $s \in S$, so $SN = G$; and $S \cap N = \{e\}$ ([[§40 Quotient Groups#^prop-40-4|Representatives Forming a Subgroup]], §37.4). The [[§42 The Second and Third Isomorphism Theorems#^thm-42-2|theorem]] gives $S \cong S/\{e\} = S/(S \cap N) \cong SN/N = G/N$.

^pf-42-3

*Uses:* [[§42 The Second and Third Isomorphism Theorems#^thm-42-2|§42.2]], [[§40 Quotient Groups#^def-40-2|Def. §40.2]], [[§40 Quotient Groups#^prop-40-4|§40.4]]

> [!remark]- Connections
> - Proved directly, without the theorem: [[§40 Quotient Groups#^prop-40-4|Representatives Forming a Subgroup]] (§37.4).

> [!theorem] Theorem §42.4: Third Isomorphism Theorem
> Let $N \subseteq K$ be [[§38 Normal Subgroups#^def-38-1|normal subgroups]] of $G$. Then $K/N$ is a normal subgroup of $G/N$ ([[§40 Quotient Groups#^def-40-1|Def. §40.1]]), and $(G/N)/(K/N) \cong G/K$.
>
> *Source: named in lecture 10/2; not covered*

^thm-42-4

> [!proof]- Proof
> *[To be proved.]*

^pf-42-4

> [!remark] Remark: The Isomorphism Theorems
> The lecture's theme: these theorems are about how to work in a quotient that did not come to you as the image of some map. The [[§41 The First Isomorphism Theorem#^thm-41-1|first]] identifies $G/N$ with an image; the [[§42 The Second and Third Isomorphism Theorems#^thm-42-2|second]] and [[§42 The Second and Third Isomorphism Theorems#^thm-42-4|third]] compare quotients of subgroups and quotients of quotients. A worksheet on the second and third theorems is on the course Canvas site; the lecture recommended experimenting with small groups to make them intuitive.

^rem-42-1

> [!example] Example §42.1: $AB$ Need Not Be a Subgroup
> Without normality, the [[§42 The Second and Third Isomorphism Theorems#^def-42-1|product set]] of two [[§4 Subgroups#^def-4-1|subgroups]] can fail to be a subgroup. In $S_3$ ([[§10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]]) take $A = \{e, (1\,2)\}$ and $B = \{e, (1\,3)\}$. Then
>
> $$ AB = \{e,\ (1\,3),\ (1\,2),\ (1\,2)(1\,3)\} = \{e,\ (1\,2),\ (1\,3),\ (1\,3\,2)\}, $$
>
> since $(1\,2)(1\,3)$ sends $1 \mapsto 3 \mapsto 3$, $3 \mapsto 1 \mapsto 2$, $2 \mapsto 2 \mapsto 1$. But $(1\,3\,2)^{-1} = (1\,2\,3) \notin AB$, so $AB$ is not closed under inverses. (Neither $A$ nor $B$ is [[§38 Normal Subgroups#^def-38-1|normal]] in $S_3$ ([[§38 Normal Subgroups#^ex-38-1|Ex. §38.1]]); compare $HN$ Is a Subgroup When $N$ Is Normal ([[§42 The Second and Third Isomorphism Theorems#^lem-42-1|§42.1]]), above. Alternatively: $|AB| = 4$ does not divide $6$.)
>
> *Source: PS 4.1(1)*

^ex-42-1
