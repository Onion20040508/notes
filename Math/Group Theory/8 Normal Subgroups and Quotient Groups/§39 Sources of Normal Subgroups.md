---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 39
tags: [group-theory, math493]
---
← [[§38 Normal Subgroups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§40 Quotient Groups]] →

*Reference: Pinter Ch. 14.*

## Subgroups of Index Two

> [!theorem] Proposition §39.1: Subgroups of Index $2$ Are Normal
> If $H$ is a subgroup of $G$ with $[G : H] = 2$, then $H$ is normal in $G$.
>
> *Source: lecture*

^prop-39-1

> [!proof]+ Proof
> There are exactly two left cosets. One of them is $H = eH$, and since the left cosets partition $G$, the other is the complement $G \setminus H$. Likewise there are exactly two right cosets (the number of right cosets equals the number of left cosets, [[§28 Left and Right Cosets#^prop-28-3|§28.3]]), namely $H$ and $G \setminus H$. So the set of left cosets equals the set of right cosets, and $H$ is normal by characterization (4) ([[§38 Normal Subgroups#^prop-38-2|§38.2]]).

^pf-39-1

*Uses:* [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§28 Left and Right Cosets#^prop-28-3|§28.3]], [[§38 Normal Subgroups#^prop-38-2|§38.2]]

> [!example] Example §39.1: Index-$2$ Examples
> 1. In $S_3$, the subgroup $\langle (1\,2\,3) \rangle$ has order $3$, hence index $6/3 = 2$ by [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange]], so it is normal.
> 2. For every $n \geq 2$, $[S_n : A_n] = 2$ ([[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|§21.5]]: $|A_n| = n!/2$), so $A_n$ is a normal subgroup of $S_n$.
>
> *Source: lecture; WS 6.2(2)*

^ex-39-1

## Kernels, Images, and Preimages

> [!theorem] Proposition §39.2: Kernels Are Normal
> If $\varphi: G_1 \to G_2$ is a group homomorphism, then $\operatorname{Ker}(\varphi)$ is a normal subgroup of $G_1$.
>
> *Source: lecture; WS 6.4*

^prop-39-2

> [!proof]+ Proof
> $\operatorname{Ker}(\varphi)$ is a subgroup ([[§15 Homomorphisms#^prop-15-2|§15.2]]). For $g \in G_1$ and $h \in \operatorname{Ker}(\varphi)$,
>
> $$ \varphi(ghg^{-1}) = \varphi(g)\varphi(h)\varphi(g^{-1}) = \varphi(g)\,e\,\varphi(g)^{-1} = e, $$
>
> so $ghg^{-1} \in \operatorname{Ker}(\varphi)$.

^pf-39-2

*Uses:* [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]]

> [!remark]- Connections
> - 590 counterpart: [[§27 Free Groups and Presentations#^rem-27-17|Remark after Definition §21.12]] (kernels are normal).
> - Converse: [[§40 Quotient Groups#^prop-40-2|Every Normal Subgroup Is a Kernel]]; used in [[§43 Simple Groups#^prop-43-3|Homomorphisms out of a Simple Group]].

The converse also holds: every normal subgroup is the kernel of a homomorphism, namely of the projection onto the quotient group ([[§40 Quotient Groups#^prop-40-2|Every Normal Subgroup Is a Kernel]], §40).

> [!example] Example §39.2: Kernels
> 1. $A_n = \operatorname{Ker}(\operatorname{sgn})$ for the sign $\operatorname{sgn}: S_n \to \{\pm 1\}$, giving a second proof that $A_n \trianglelefteq S_n$ (lecture).
> 2. $SL_n(\mathbb{R}) = \operatorname{Ker}(\det) \trianglelefteq GL_n(\mathbb{R})$.
> 3. For $G$ acting on $X$, the kernel of $G \to S_X$ — the elements acting trivially on every point — is normal; for the conjugation action this kernel is the center, so $Z(G) \trianglelefteq G$ ([[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]]).

^ex-39-2

> [!theorem] Proposition §39.3: Images Need Not Be Normal
> The image of a homomorphism need not be a normal subgroup of the target. For example, the inclusion $\iota: \langle (1\,2) \rangle \to S_3$ is a homomorphism whose image $\{e, (1\,2)\}$ is not normal in $S_3$.
>
> *Source: WS 6.5; lecture 9/25*

^prop-39-3

> [!proof]+ Proof
> The inclusion is a homomorphism because the operation of $\langle (1\,2) \rangle$ is that of $S_3$. Its image $\{e, (1\,2)\}$ is not normal: $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3) \notin \{e, (1\,2)\}$ (A Non-Normal Subgroup of $S_3$, [[§38 Normal Subgroups#^ex-38-1|Ex. §38.1]]). The lecture of Fri Sept 25 used the same example in the form $\mathbb{Z}/2\mathbb{Z} \to S_3$, $a \mapsto (1\,2)^a$ ([[§41 The First and Second Isomorphism Theorems#^rem-41-1|§41]]).

^pf-39-3

*Uses:* [[§38 Normal Subgroups#^ex-38-1|Ex. §38.1]]

> [!theorem] Proposition §39.4: Preimages and Images of Normal Subgroups
> Let $N \trianglelefteq G$.
> 1. If $\varphi: F \to G$ is a homomorphism, then $\varphi^{-1}(N)$ is normal in $F$.
> 2. If $\psi: G \to H$ is a homomorphism, then $\psi(N)$ need not be normal in $H$.
> 3. If $\psi: G \to H$ is a *surjective* homomorphism, then $\psi(N)$ is normal in $H$.
>
> *Source: WS 6.6*

^prop-39-4

> [!proof]- Proof
> *[To be proved.]*

^pf-39-4

> [!theorem] Theorem §39.5: A Normal Subgroup Inside a Subgroup of Finite Index
> Let $H$ be a subgroup of $G$ with $[G : H] = n$ finite. Then there is a normal subgroup $N$ of $G$ with $N \subseteq H \subseteq G$ and $[G : N] \leq n!$.
>
> *Source: PS 3.2; PS 4.3*

^thm-39-5

> [!proof]+ Proof
> $G$ acts on the $n$-element set $G/H$ by $g \star (xH) = (gx)H$ ([[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]]), so there is a homomorphism $\varphi: G \to S_{G/H}$ (Actions Are Homomorphisms to $S_X$, [[§25 Actions#^thm-25-3|§25.3]]). Let $N = \operatorname{Ker}\varphi$, which is normal ([[§39 Sources of Normal Subgroups#^prop-39-2|Kernels Are Normal]]).
>
> **$N \subseteq H$.** If $g \in N$, then $g$ fixes every coset, in particular $g \star (eH) = gH = H$, so $g = ge \in gH = H$.
>
> **$[G : N] \leq n!$.** Define $\bar\varphi: G/N \to S_{G/H}$ by $\bar\varphi(gN) = \varphi(g)$. It is well defined: if $gN = g'N$ then $g' = gk$ with $k \in N$, so $\varphi(g') = \varphi(g)\varphi(k) = \varphi(g)$. It is injective: if $\varphi(g) = \varphi(g')$, then $\varphi(g^{-1}g') = e$, so $g^{-1}g' \in N$ and $gN = g'N$. Hence $[G : N] = |G/N| \leq |S_{G/H}| = n!$, the last equality because relabelling the $n$ cosets gives $S_{G/H} \cong S_n$. The argument does not require $G$ to be finite.

^pf-39-5

*Uses:* [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]], [[§25 Actions#^thm-25-3|§25.3]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]]

![[m493-36-1.svg]]
*The proof of PS 3.2: $N = \operatorname{Ker}\varphi$, and $\bar\varphi(gN) = \varphi(g)$ is injective, so $[G : N] \leq n!$.*

> [!remark]- Connections
> - Re-read through the First Isomorphism Theorem: [[§41 The First and Second Isomorphism Theorems#^rem-41-3|PS 3.1 and PS 3.2 as Instances]]; $N$ is identified in [[§39 Sources of Normal Subgroups#^prop-39-6|The Normal Core]].

> [!theorem] Proposition §39.6: The Normal Core
> In [[§39 Sources of Normal Subgroups#^thm-39-5|PS 3.2]], let $N = \operatorname{Ker}(G \to S_{G/H})$. Then:
> 1. $N = \bigcap_{x \in G} xHx^{-1}$;
> 2. $N$ is the largest normal subgroup of $G$ contained in $H$: if $M \trianglelefteq G$ and $M \subseteq H$, then $M \subseteq N$. (So $N$ is the *normal core* of $H$.)
> 3. $[G : N]$ divides $n!$.
>
> *Source: not from class*

^prop-39-6

> [!proof]+ Proof
> **(1)** The kernel of an action is the intersection of all stabilizers, and $\operatorname{Stab}(xH) = xHx^{-1}$ ([[§31 G Acting on Coset Spaces#^prop-31-1|WS 5.4]]). **(2)** If $M \trianglelefteq G$ and $M \subseteq H$, then $M = xMx^{-1} \subseteq xHx^{-1}$ for every $x$, so $M \subseteq N$ by (1). **(3)** The image of $\bar\varphi$ is $\varphi(G)$, a subgroup of $S_{G/H}$, so $[G : N] = |\varphi(G)|$ divides $|S_{G/H}| = n!$ by [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange]]. With the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem]] this is the statement $G/N \cong \varphi(G)$ ([[§41 The First and Second Isomorphism Theorems#^rem-41-3|PS 3.1 and PS 3.2 as Instances]], §41).

^pf-39-6

*Uses:* [[§25 Actions#^def-25-4|Def. §25.4]], [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]], [[§38 Normal Subgroups#^prop-38-2|§38.2]], [[§39 Sources of Normal Subgroups#^thm-39-5|§39.5]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

> [!remark]- Connections
> - Part (3) recorded again as item 4 of [[§41 The First and Second Isomorphism Theorems#^ex-41-1|The First Isomorphism Theorem in Action]].

## Unions of Conjugacy Classes

> [!theorem] Proposition §39.7: Normal Subgroups Are Unions of Conjugacy Classes
> A subgroup $H$ of $G$ is normal if and only if $H$ is a union of conjugacy classes of $G$, i.e. if and only if $h \in H$ implies $\operatorname{Conj}(h) \subseteq H$.
>
> *Source: cf. Pinter Ch. 14*

^prop-39-7

> [!proof]+ Proof
> $H$ is normal iff $ghg^{-1} \in H$ for all $g \in G$, $h \in H$, iff for each $h \in H$ the whole orbit $\operatorname{Conj}(h) = \{ghg^{-1} : g \in G\}$ of $h$ under the [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|conjugation action]] lies in $H$. A subset containing, with each of its points, that point's entire orbit is exactly a union of orbits.

^pf-39-7

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§33 Conjugacy Classes#^def-33-1|Def. §33.1]], [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]], [[§27 Orbits#^prop-27-1|§27.1]]

> [!remark]- Connections
> - This is condition (2) of [[§38 Normal Subgroups#^thm-38-3|Five Characterizations of Normality]]; used to prove [[§43 Simple Groups#^prop-43-6|A₅ Is Simple]].

> [!example] Example §39.3: Normal Subgroups of $S_3$ and $S_4$
> (For $S_3$, compare the lattice in [[§13 The Symmetric Group S₃#^prop-13-1|the figure of §13]].) In the language of [[· 7 Conjugacy and the Center|Chapter 7]]: $G$ acts on itself by conjugation, the orbits are the conjugacy classes, and a subgroup is normal precisely when it is a union of orbits — stable under the action. This gives a quick normality test once the conjugacy classes are known. In $S_3$ the classes are $\{e\}$, the three transpositions, and the two $3$-cycles ([[§34 Conjugation as an Action and the Class Equation#^ex-34-1|Ex. §34.1]]), so a normal subgroup must be a union of these containing $e$ with order dividing $6$: the only options are $\{e\}$, $\{e, (1\,2\,3), (1\,3\,2)\}$, and $S_3$, confirming that $\{e, (1\,2)\}$ is not normal. In $S_4$, with class sizes $1, 6, 3, 8, 6$, a normal subgroup has order a sum of class sizes including the $1$ and dividing $24$; this singles out $\{e\}$, $1 + 3 = 4$ (the Klein four-group $K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$), $1 + 3 + 8 = 12$ ($A_4$), and $S_4$, and each is indeed a normal subgroup.

^ex-39-3

![[m493-36-2.svg]]
*The normal subgroups of $S_4$ as unions of conjugacy classes (class sizes in parentheses): $K$ (red) is $\{e\}$ together with the class of type $2^2$, and $A_4$ (blue) adds the eight $3$-cycles. Apart from $\{e\}$ and $S_4$, no other union of classes containing $e$ has a size dividing $24$.*

> [!theorem] Proposition §39.9: Normal Subgroups of $GL_2(\mathbb{R})$
> In $GL_2(\mathbb{R})$:
> 1. the subgroup of invertible diagonal matrices is *not* normal;
> 2. the subgroup of invertible upper triangular matrices is *not* normal;
> 3. the subgroup $SL_2(\mathbb{R})$ of matrices of determinant $1$ is normal;
> 4. the subgroup $\{I_2, -I_2\}$ is normal.
>
> *Source: WS 6.3*

^prop-39-9

> [!proof]- Proof
> *[To be proved.]*

^pf-39-9
