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
> **(2).** *(Not from lecture; filled in.)* Let $A := \pi^{-1}(B)$. By (1), $A$ is a subgroup of $G$ containing $N$, so Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](2) applies to it: $A \trianglelefteq G$ if and only if $\pi(A) \trianglelefteq G/N$. It remains to show $\pi(A) = B$. If $g \in A$, then $\pi(g) \in B$ by the definition of $A$; so $\pi(A) \subseteq B$. Conversely, let $b \in B$. Since $\pi$ is surjective (Proposition [[§40 Quotient Groups#^prop-40-2|§40.2]]), $b = \pi(g)$ for some $g \in G$; then $\pi(g) \in B$, so $g \in A$ and $b = \pi(g) \in \pi(A)$. Hence $\pi(A) = B$, and therefore $\pi^{-1}(B) = A$ is normal in $G$ if and only if $B = \pi(A)$ is normal in $G/N$.

^pf-42-2

*Uses:* [[§15 Homomorphisms#^prop-15-4|§15.4]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]], [[§40 Quotient Groups#^prop-40-2|§40.2]]

> [!theorem] Theorem §42.3: The Correspondence Theorem
> Let $N \trianglelefteq G$ and $\pi: G \to G/N$. The maps $A \mapsto \pi(A)$ and $B \mapsto \pi^{-1}(B)$ are mutually inverse bijections
>
> $$ \{\text{subgroups of } G \text{ containing } N\} \;\longleftrightarrow\; \{\text{subgroups of } G/N\}, $$
>
> and they take normal subgroups to normal subgroups. (In the lecture's summary: $\downarrow$ is WS 8.4, [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|Proposition §42.1]]; $\uparrow$ is WS 8.5, [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|Proposition §42.2]].)
>
> *Source: the “third/fourth isomorphism theorem” of WS 8*

^thm-42-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Write $\Phi(A) := \pi(A)$ for a subgroup $A$ of $G$ containing $N$, and $\Psi(B) := \pi^{-1}(B)$ for a subgroup $B$ of $G/N$.
>
> **(1) The maps land where claimed.** If $A$ is a subgroup of $G$ with $N \subseteq A$, then $\Phi(A) = \pi(A)$ is a subgroup of $G/N$ (Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](1)). If $B$ is a subgroup of $G/N$, then $\Psi(B) = \pi^{-1}(B)$ is a subgroup of $G$ containing $N$ (Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|§42.2]](1)).
>
> **(2) $\Phi(\Psi(B)) = B$, i.e. $\pi(\pi^{-1}(B)) = B$.** If $g \in \pi^{-1}(B)$, then $\pi(g) \in B$ by the definition of the preimage; so $\pi(\pi^{-1}(B)) \subseteq B$. Conversely, let $b \in B$. Since $\pi$ is surjective (Proposition [[§40 Quotient Groups#^prop-40-2|§40.2]]), $b = \pi(g)$ for some $g \in G$; then $g \in \pi^{-1}(B)$, so $b \in \pi(\pi^{-1}(B))$.
>
> **(3) $\Psi(\Phi(A)) = A$, i.e. $\pi^{-1}(\pi(A)) = A$ when $N \subseteq A$.** If $a \in A$, then $\pi(a) \in \pi(A)$; so $A \subseteq \pi^{-1}(\pi(A))$. Conversely, let $g \in \pi^{-1}(\pi(A))$. Then $\pi(g) = \pi(a)$ for some $a \in A$, i.e. $gN = aN$, which by the coset criterion (Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]](1), Definition [[§28 Left and Right Cosets#^def-28-1|§28.1]]) means $a^{-1}g \in N$. Since $N \subseteq A$, also $a^{-1}g \in A$, and by closure of $A$ under products
>
> $$ g = a\,(a^{-1}g) \in A . $$
>
> So $\pi^{-1}(\pi(A)) \subseteq A$. (The hypothesis $N \subseteq A$ is needed: for $A = \{e\}$ one gets $\pi^{-1}(\pi(A)) = \pi^{-1}(\{N\}) = N$.)
>
> By (2) and (3), $\Phi \circ \Psi$ and $\Psi \circ \Phi$ are identity maps, so $\Phi$ and $\Psi$ are mutually inverse bijections.
>
> **(4) Normal subgroups.** If $A \supseteq N$ is normal in $G$, then $\pi(A) \trianglelefteq G/N$ by Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](2). If $B \trianglelefteq G/N$, then $\pi^{-1}(B) \trianglelefteq G$ by Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|§42.2]](2). So $\Phi$ and $\Psi$ restrict to mutually inverse bijections between the normal subgroups of $G$ containing $N$ and the normal subgroups of $G/N$.

^pf-42-3

*Uses:* [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-2|§42.2]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]]

> [!theorem] Proposition §42.4: Quotients Along the Correspondence
> Let $N \subseteq A_1 \subseteq A_2 \subseteq G$ be subgroups containing the normal subgroup $N$, and let $B_1 = \pi(A_1)$, $B_2 = \pi(A_2)$.
> 1. $gA_1 \mapsto \pi(g)B_1$ is a bijection $A_2/A_1 \to B_2/B_1$.
> 2. $A_1 \trianglelefteq A_2$ if and only if $B_1 \trianglelefteq B_2$.
> 3. If $A_1 \trianglelefteq A_2$, then $A_2/A_1 \cong B_2/B_1$.
>
> *Source: WS 8.6*

^prop-42-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Here $A_2/A_1$ is the set of left cosets $gA_1$ with $g \in A_2$ (Definition [[§29 The Index and Lagrange's Theorem#^def-29-1|§29.1]], for the subgroup $A_1$ of the group $A_2$), and likewise $B_2/B_1$. By Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](1), $B_1$ and $B_2$ are subgroups of $G/N$, and $B_1 \subseteq B_2$ because $A_1 \subseteq A_2$. We use one fact from the Correspondence Theorem (Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]], step (3) of its proof, with $A = A_1 \supseteq N$): $\pi^{-1}(B_1) = A_1$, that is,
>
> $$ (\ast) \qquad \text{for } x \in G: \quad x \in A_1 \iff \pi(x) \in B_1 . $$
>
> **(1)** Define $f: A_2/A_1 \to B_2/B_1$ by $f(gA_1) = \pi(g)B_1$ for $g \in A_2$; note $\pi(g) \in \pi(A_2) = B_2$, so $\pi(g)B_1 \in B_2/B_1$. For $g, g' \in A_2$,
>
> $$ \begin{aligned} gA_1 = g'A_1 &\iff g^{-1}g' \in A_1 \iff \pi(g^{-1}g') \in B_1 \\ &\iff \pi(g)^{-1}\pi(g') \in B_1 \iff \pi(g)B_1 = \pi(g')B_1 . \end{aligned} $$
>
> The first and the last equivalence are the coset criterion (Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]](1), Definition [[§28 Left and Right Cosets#^def-28-1|§28.1]]), for the subgroup $A_1$ of $A_2$ and for the subgroup $B_1$ of $B_2$; the second is $(\ast)$ with $x = g^{-1}g'$; the third holds because $\pi$ is a homomorphism (Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]]). Read from left to right, the chain says that $\pi(g)B_1$ does not depend on the representative $g$ of $gA_1$, so $f$ is well defined; read from right to left, it says that $f$ is injective. $f$ is surjective: an element of $B_2/B_1$ is $bB_1$ with $b \in B_2 = \pi(A_2)$, so $b = \pi(g)$ for some $g \in A_2$, and $bB_1 = f(gA_1)$.
>
> **(2)** (The argument of Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](2), carried out inside $A_2$.)
>
> ($\Rightarrow$) Suppose $A_1 \trianglelefteq A_2$. Let $b_1 \in B_1$ and $b_2 \in B_2$, and write $b_1 = \pi(a_1)$, $b_2 = \pi(a_2)$ with $a_1 \in A_1$, $a_2 \in A_2$. Then (Proposition [[§15 Homomorphisms#^prop-15-1|§15.1]])
>
> $$ b_2b_1b_2^{-1} = \pi(a_2)\,\pi(a_1)\,\pi(a_2)^{-1} = \pi(a_2a_1a_2^{-1}) \in \pi(A_1) = B_1, $$
>
> since $a_2a_1a_2^{-1} \in A_1$ (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]). So $B_1 \trianglelefteq B_2$.
>
> ($\Leftarrow$) Suppose $B_1 \trianglelefteq B_2$. Let $a_1 \in A_1$ and $a_2 \in A_2$. Then
>
> $$ \pi(a_2a_1a_2^{-1}) = \pi(a_2)\,\pi(a_1)\,\pi(a_2)^{-1} \in B_1, $$
>
> because $\pi(a_1) \in B_1$, $\pi(a_2) \in B_2$ and $B_1 \trianglelefteq B_2$. By $(\ast)$, $a_2a_1a_2^{-1} \in A_1$. So $A_1 \trianglelefteq A_2$.
>
> **(3)** Suppose $A_1 \trianglelefteq A_2$; then $B_1 \trianglelefteq B_2$ by (2), so $A_2/A_1$ and $B_2/B_1$ are groups under coset multiplication (Definition [[§40 Quotient Groups#^def-40-1|§40.1]], Theorem [[§40 Quotient Groups#^thm-40-1|§40.1]]). The bijection $f$ of (1) is a homomorphism: for $g, g' \in A_2$,
>
> $$ f\big((gA_1)(g'A_1)\big) = f(gg'A_1) = \pi(gg')B_1 = \big(\pi(g)\pi(g')\big)B_1 = \big(\pi(g)B_1\big)\big(\pi(g')B_1\big) = f(gA_1)\,f(g'A_1). $$
>
> So $f$ is an isomorphism (Definition [[§16 Isomorphisms#^def-16-1|§16.1]]), and $A_2/A_1 \cong B_2/B_1$.

^pf-42-4

*Uses:* [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!theorem] Theorem §42.5: Third Isomorphism Theorem
> Let $N \subseteq K$ be [[§38 Normal Subgroups#^def-38-1|normal subgroups]] of $G$. Then $K/N$ is a normal subgroup of $G/N$ ([[§40 Quotient Groups#^def-40-1|Def. §40.1]]), and $(G/N)/(K/N) \cong G/K$.
>
> *Source: named in lecture 10/2; not covered*

^thm-42-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $\pi: G \to G/N$ be the projection.
>
> **$K/N$ is normal in $G/N$.** By Remark [[§42 The Correspondence and Third Isomorphism Theorems#^rem-42-1|Notation A/N (§42)]], $K/N = \pi(K)$. Since $K$ is a subgroup of $G$ containing $N$ and $K \trianglelefteq G$, Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]](2) gives $\pi(K) \trianglelefteq G/N$.
>
> **The isomorphism.** Apply Proposition [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-4|§42.4]] with $A_1 = K$ and $A_2 = G$, so that $N \subseteq K \subseteq G$, $B_1 = \pi(K) = K/N$, and $B_2 = \pi(G) = G/N$ because $\pi$ is surjective (Proposition [[§40 Quotient Groups#^prop-40-2|§40.2]]). Since $K \trianglelefteq G$, part (3) gives the isomorphism
>
> $$ G/K \to (G/N)/(K/N), \qquad gK \mapsto \pi(g)\,(K/N) = (gN)(K/N), $$
>
> and its inverse is an isomorphism (Proposition [[§16 Isomorphisms#^prop-16-1|§16.1]]), so $(G/N)/(K/N) \cong G/K$.
>
> **Second route, through the First Isomorphism Theorem.** Define $\alpha: G/N \to G/K$ by $\alpha(gN) = gK$. *Well defined:* if $gN = g'N$, then $g^{-1}g' \in N \subseteq K$ by the coset criterion (Proposition [[§28 Left and Right Cosets#^prop-28-2|§28.2]](1), Definition [[§28 Left and Right Cosets#^def-28-1|§28.1]]), so $gK = g'K$. *Homomorphism:* by Definition [[§40 Quotient Groups#^def-40-1|§40.1]], applied in $G/N$ and in $G/K$,
>
> $$ \alpha\big((gN)(g'N)\big) = \alpha(gg'N) = gg'K = (gK)(g'K) = \alpha(gN)\,\alpha(g'N). $$
>
> *Surjective:* every $gK$ equals $\alpha(gN)$. *Kernel:* the identity of $G/K$ is $eK = K$ (Theorem [[§40 Quotient Groups#^thm-40-1|§40.1]]), and $gK = eK$ if and only if $g^{-1}e = g^{-1} \in K$, i.e. $g \in K$ (coset criterion); so
>
> $$ \operatorname{Ker}\alpha = \{gN : g \in K\} = \pi(K) = K/N . $$
>
> (This reproves $K/N \trianglelefteq G/N$, by Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]].) The First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]) gives
>
> $$ (G/N)/(K/N) = (G/N)/\operatorname{Ker}\alpha \cong \operatorname{Im}\alpha = G/K . $$

^pf-42-5

*Uses:* [[§42 The Correspondence and Third Isomorphism Theorems#^rem-42-1|Notation A/N (§42)]], [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-1|§42.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-4|§42.4]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§16 Isomorphisms#^prop-16-1|§16.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

> [!remark] Remark: The Isomorphism Theorems
> The lecture's theme: these theorems are about how to work in a quotient that did not come to you as the image of some map. The [[§41 The First and Second Isomorphism Theorems#^thm-41-1|first]] identifies $G/N$ with an image; the [[§41 The First and Second Isomorphism Theorems#^thm-41-5|second]] and [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|third]] compare quotients of subgroups and quotients of quotients. A worksheet on the second and third theorems is on the course Canvas site; the lecture recommended experimenting with small groups to make them intuitive.

^rem-42-2

> [!remark] Remark: Naming the Isomorphism Theorems
> Part (3) of [[§42 The Correspondence and Third Isomorphism Theorems#^prop-42-4|Proposition §42.4]] with $A_1 = K$ and $A_2 = G$ is the Third Isomorphism Theorem, $G/K \cong (G/N)/(K/N)$, [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|Theorem §42.5]], just above. Worksheet 8 calls the correspondence theorem the “third/fourth isomorphism theorem”; textbooks vary, and many call it the correspondence (or lattice) theorem and number it fourth. Note also that the worksheet's “$N \subset A$” allows $A = N$, which corresponds to the trivial subgroup of $G/N$.

^rem-42-3

[[§45 S₃, S₄, A₄ and A₅#^ex-45-2|Example §45.2]], in the $S_4$ part of [[§45 S₃, S₄, A₄ and A₅|§45]], lists the six subgroups of $S_4$ containing $K$.
