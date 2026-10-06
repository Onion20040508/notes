---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 42
tags: [group-theory, math493]
---
← [[§41 The First and Second Isomorphism Theorems]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§43 Simple Groups]] →

*Source: Lecture (Fri Oct 2); Lecture and Worksheet 8 (Mon Oct 5).*

> [!remark] Remark: Notation $A/N$
> For any subgroup $A$, the [[§41 The First and Second Isomorphism Theorems#^thm-41-5|Second Isomorphism Theorem]] gives $\pi(A) \cong AN/N$. When $N \subseteq A$, $AN = A$, and $\pi(A) = \{aN : a \in A\}$ is written $A/N$: it is the quotient group $A/N$ (as $N \trianglelefteq A$), sitting inside $G/N$. In this notation, the question of WS 8.4(2) is: if $A/N \trianglelefteq G/N$, i.e. $(gag^{-1})N \in A/N$ for all $g$, must $A \trianglelefteq G$? Since $N \subseteq A$, $gAg^{-1}N = A$ forces $gAg^{-1} = A$ (lecture 10/5).

^rem-42-1

> [!theorem] Proposition §42.1: Images of Subgroups Containing $N$
> Let $N \trianglelefteq G$, $\pi: G \to G/N$, and let $A$ be a subgroup of $G$ with $N \subseteq A$.
> 1. $\pi(A)$ is a subgroup of $G/N$.
> 2. $\pi(A)$ is normal in $G/N$ if and only if $A$ is normal in $G$.
>
> *Source: WS 8.4; lecture 10/5*

^prop-42-1

> [!proof]+ Proof
> **(1)** $\pi(A) = \operatorname{Im}(\pi|_A)$, the image of a homomorphism, hence a subgroup (Image and Kernel Are Subgroups, [[§15 Homomorphisms#^prop-15-2|§15.2]]).
>
> **(2), $\Leftarrow$.** Let $A \trianglelefteq G$, $\pi(a) \in \pi(A)$ and $gN \in G/N$. Then $(gN)\,\pi(a)\,(gN)^{-1} = \pi(g)\pi(a)\pi(g)^{-1} = \pi(gag^{-1})$, and $gag^{-1} \in A$, so this lies in $\pi(A)$.
>
> **(2), $\Rightarrow$.** Let $\pi(A) \trianglelefteq G/N$, $a \in A$ and $g \in G$; we need $gag^{-1} \in A$. Now
>
> $$ \pi(gag^{-1}) = \pi(g)\pi(a)\pi(g)^{-1} \in \pi(A) = A/N, $$
>
> so $gag^{-1} = a'n$ for some $a' \in A$ and $n \in N$. Since $N \subseteq A$, $a'n \in A$. (This is the only place the hypothesis $N \subseteq A$ is needed, as discussed in lecture.)

^pf-42-1

*Uses:* [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^rem-42-1|Rem. §42 (Notation A/N)]]

> [!theorem] Proposition §42.2: Preimages of Subgroups of $G/N$
> Let $N \trianglelefteq G$, $\pi: G \to G/N$, and let $B$ be a subgroup of $G/N$.
> 1. $\pi^{-1}(B)$ is a subgroup of $G$ containing $N$.
> 2. $\pi^{-1}(B)$ is normal in $G$ if and only if $B$ is normal in $G/N$.
>
> *Source: WS 8.5*

^prop-42-2

> [!proof]+ Proof
> **(1) (lecture 10/5).** $\pi^{-1}(B) = \{g \in G : \pi(g) \in B\}$. If $n \in N$, then $\pi(n) = e \in B$, so $n \in \pi^{-1}(B)$; in particular $\pi^{-1}(B)$ contains $e$. If $g_1, g_2 \in \pi^{-1}(B)$, then $\pi(g_1g_2) = g_1g_2N = (g_1N)(g_2N) \in B$, since $B$ is a subgroup; so $g_1g_2 \in \pi^{-1}(B)$. Closure under inverses is the same, as $\pi(g^{-1}) = \pi(g)^{-1}$. (This is also a case of Images and Preimages of Subgroups, [[§15 Homomorphisms#^prop-15-4|§15.4]].)
>
> **(2).** *To be filled (WS 8.5(2) was not done in class).*

^pf-42-2

*Uses:* [[§15 Homomorphisms#^prop-15-4|§15.4]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]]

> [!theorem] Theorem §42.3: The Correspondence Theorem
> Let $N \trianglelefteq G$ and $\pi: G \to G/N$. The maps $A \mapsto \pi(A)$ and $B \mapsto \pi^{-1}(B)$ are mutually inverse bijections
>
> $$ \{\text{subgroups of } G \text{ containing } N\} \;\longleftrightarrow\; \{\text{subgroups of } G/N\}, $$
>
> and they take normal subgroups to normal subgroups. (In the lecture's summary: $\downarrow$ is WS 8.4, [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|Proposition §42.1]]; $\uparrow$ is WS 8.5, [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|Proposition §42.2]].)
>
> *Source: the “third/fourth isomorphism theorem” of WS 8*

^thm-42-3

> [!proof]- Proof
> *[To be proved.]*

^pf-42-3

> [!theorem] Proposition §42.4: Quotients Along the Correspondence
> Let $N \subseteq A_1 \subseteq A_2 \subseteq G$ be subgroups containing the normal subgroup $N$, and let $B_1 = \pi(A_1)$, $B_2 = \pi(A_2)$.
> 1. $gA_1 \mapsto \pi(g)B_1$ is a bijection $A_2/A_1 \to B_2/B_1$.
> 2. $A_1 \trianglelefteq A_2$ if and only if $B_1 \trianglelefteq B_2$.
> 3. If $A_1 \trianglelefteq A_2$, then $A_2/A_1 \cong B_2/B_1$.
>
> *Source: WS 8.6*

^prop-42-4

> [!proof]- Proof
> *[To be proved.]*

^pf-42-4

> [!theorem] Theorem §42.5: Third Isomorphism Theorem
> Let $N \subseteq K$ be [[§38 Normal Subgroups#^def-38-1|normal subgroups]] of $G$. Then $K/N$ is a normal subgroup of $G/N$ ([[§40 Quotient Groups#^def-40-1|Def. §40.1]]), and $(G/N)/(K/N) \cong G/K$.
>
> *Source: named in lecture 10/2; not covered*

^thm-42-5

> [!proof]- Proof
> *[To be proved.]*

^pf-42-5

> [!remark] Remark: The Isomorphism Theorems
> The lecture's theme: these theorems are about how to work in a quotient that did not come to you as the image of some map. The [[§41 The First and Second Isomorphism Theorems#^thm-41-1|first]] identifies $G/N$ with an image; the [[§41 The First and Second Isomorphism Theorems#^thm-41-5|second]] and [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|third]] compare quotients of subgroups and quotients of quotients. A worksheet on the second and third theorems is on the course Canvas site; the lecture recommended experimenting with small groups to make them intuitive.

^rem-42-2

> [!remark] Remark: Naming the Isomorphism Theorems
> Part (3) of [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-4|Proposition §42.4]] with $A_1 = K$ and $A_2 = G$ is the Third Isomorphism Theorem, $G/K \cong (G/N)/(K/N)$, [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|Theorem §42.5]], just above. Worksheet 8 calls the correspondence theorem the “third/fourth isomorphism theorem”; textbooks vary, and many call it the correspondence (or lattice) theorem and number it fourth. Note also that the worksheet's “$N \subset A$” allows $A = N$, which corresponds to the trivial subgroup of $G/N$.

^rem-42-3

[[§45 S₃, S₄, A₄ and A₅#^ex-45-2|Example §45.2]], in the $S_4$ part of [[§45 S₃, S₄, A₄ and A₅|§45]], lists the six subgroups of $S_4$ containing $V$.
