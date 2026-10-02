---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 39
tags: [group-theory, math493]
---
← [[§38 The First Isomorphism Theorem]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§40 Simple Groups]] →

*Source: Lecture (Fri Oct 2).*

> [!definition] Definition §39.1: The Product Set $HN$
> For [[§4 Subgroups#^def-4-1|subgroups]] $H, N$ of $G$, write $HN := \{hn : h \in H,\ n \in N\}$.

^def-39-1

> [!theorem] Lemma §39.1: $HN$ Is a Subgroup When $N$ Is Normal
> If $H \leq G$ and $N \trianglelefteq G$ ([[§35 Normal Subgroups#^def-35-1|Def. §35.1]]), then $HN$ ([[§39 The Second and Third Isomorphism Theorems#^def-39-1|Def. §39.1]]) is a subgroup of $G$, and it contains both $H$ and $N$.
>
> *Source: lecture 10/2*

^lem-39-1

> [!proof]+ Proof
> *Closure (lecture).* Let $h_1, h_2 \in H$ and $n_1, n_2 \in N$. Since $N$ is normal, $n_1h_2 = h_2n'$ for some $n' \in N$ ($n' = h_2^{-1}n_1h_2$). So $h_1n_1 \cdot h_2n_2 = h_1h_2 \cdot n'n_2 \in HN$. *Containment:* $h = he$ and $n = en$.
>
> *Identity and inverses:* *[To be proved; assigned as homework.]*

^pf-39-1

*Uses:* [[§39 The Second and Third Isomorphism Theorems#^def-39-1|Def. §39.1]], [[§35 Normal Subgroups#^def-35-1|Def. §35.1]]

> [!theorem] Theorem §39.2: Second Isomorphism Theorem
> Let $G$ be a group, $N \trianglelefteq G$, $H \leq G$, and $\pi: G \to G/N$ the [[§37 Quotient Groups#^def-37-1|projection]]. Then $H \cap N \trianglelefteq H$, $N \trianglelefteq HN$ ([[§39 The Second and Third Isomorphism Theorems#^def-39-1|Def. §39.1]], [[§39 The Second and Third Isomorphism Theorems#^lem-39-1|§39.1]]), $\pi(H) = \pi(HN)$, and
>
> $$ H/(H \cap N) \;\cong\; \pi(H) \;=\; \pi(HN) \;\cong\; HN/N. $$
>
> In particular $H/(H \cap N) \cong HN/N$.
>
> *Source: lecture 10/2*

^thm-39-2

> [!proof]+ Proof
> *$\pi(H) = \pi(HN)$.* For $h \in H$, $\pi(h) = \pi(he) \in \pi(HN)$. For $hn \in HN$, $\pi(hn) = \pi(h)\pi(n) = \pi(h) \in \pi(H)$, since $n \in N = \operatorname{Ker}\pi$ ([[§37 Quotient Groups#^prop-37-2|§37.2]]).
>
> *Two applications of the [[§38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]]* (§38). Restrict $\pi$ to $H$: the kernel is $\{h \in H : hN = N\} = H \cap N$, so $H \cap N$ is normal in $H$ ([[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]]) and $H/(H \cap N) \cong \pi(H)$. Restrict $\pi$ to $HN$: the kernel is $HN \cap N = N$, since $N \subseteq HN$ ([[§39 The Second and Third Isomorphism Theorems#^lem-39-1|§39.1]]), so $N \trianglelefteq HN$ and $HN/N \cong \pi(HN)$. Combining with $\pi(H) = \pi(HN)$ gives the chain.

^pf-39-2

*Uses:* [[§39 The Second and Third Isomorphism Theorems#^def-39-1|Def. §39.1]], [[§39 The Second and Third Isomorphism Theorems#^lem-39-1|§39.1]], [[§37 Quotient Groups#^prop-37-2|§37.2]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]], [[§38 The First Isomorphism Theorem#^thm-38-1|§38.1]]

![[m493-38-3.svg]]
*The “diamond” picture of the Second Isomorphism Theorem: lines denote inclusion, and the two marked quotients on opposite sides agree, $HN/N \cong H/(H \cap N)$.*

> [!theorem] Corollary §39.3: Subgroup Representatives, Again
> If a [[§37 Quotient Groups#^def-37-2|set of representatives]] $S$ for $G/N$ is a [[§4 Subgroups#^def-4-1|subgroup]], then $S \cong G/N$.
>
> *Source: lecture 10/2*

^cor-39-3

> [!proof]+ Proof
> Take $H = S$. Every $g \in G$ lies in some coset $sN$ with $s \in S$, so $SN = G$; and $S \cap N = \{e\}$ ([[§37 Quotient Groups#^prop-37-4|Representatives Forming a Subgroup]], §37). The [[§39 The Second and Third Isomorphism Theorems#^thm-39-2|theorem]] gives $S \cong S/\{e\} = S/(S \cap N) \cong SN/N = G/N$.

^pf-39-3

*Uses:* [[§39 The Second and Third Isomorphism Theorems#^thm-39-2|§39.2]], [[§37 Quotient Groups#^def-37-2|Def. §37.2]], [[§37 Quotient Groups#^prop-37-4|§37.4]]

> [!remark]- Connections
> - Proved directly, without the theorem: [[§37 Quotient Groups#^prop-37-4|Representatives Forming a Subgroup]] (§37.4).

> [!example] Example §39.1: The Second Isomorphism Theorem in Action
> 1. $G = S_3$, $N = A_3$ ([[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]]), $H = \langle (1\,2) \rangle$: $H \cap N = \{e\}$ and $HN = S_3$, so $\langle (1\,2) \rangle \cong S_3/A_3$.
> 2. $G = S_4$, $N = V$ ([[§36 Sources of Normal Subgroups#^ex-36-3|Ex. §36.3]]), $H = \operatorname{Stab}(4) \cong S_3$ ([[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]]): every non-identity element of $V$ moves $4$, so $H \cap V = \{e\}$, and $HV/V \cong H$ has $6 = 24/4 = |S_4/V|$ elements, so $HV/V = S_4/V$. Hence $S_4/V \cong S_3$, recovering [[§40 Simple Groups#^prop-40-10|The Pair-Partition Homomorphism]] (§40) by a second route.

^ex-39-1

> [!theorem] Theorem §39.4: Third Isomorphism Theorem
> Let $N \subseteq K$ be [[§35 Normal Subgroups#^def-35-1|normal subgroups]] of $G$. Then $K/N$ is a normal subgroup of $G/N$ ([[§37 Quotient Groups#^def-37-1|Def. §37.1]]), and $(G/N)/(K/N) \cong G/K$.
>
> *Source: named in lecture 10/2; not covered*

^thm-39-4

> [!proof]- Proof
> *[To be proved.]*

^pf-39-4

> [!remark] Remark: The Isomorphism Theorems
> The lecture's theme: these theorems are about how to work in a quotient that did not come to you as the image of some map. The [[§38 The First Isomorphism Theorem#^thm-38-1|first]] identifies $G/N$ with an image; the [[§39 The Second and Third Isomorphism Theorems#^thm-39-2|second]] and [[§39 The Second and Third Isomorphism Theorems#^thm-39-4|third]] compare quotients of subgroups and quotients of quotients. A worksheet on the second and third theorems is on the course Canvas site; the lecture recommended experimenting with small groups to make them intuitive.

^rem-39-1
