---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 29
tags: [group-theory, math493]
---
← [[§28 Left and Right Cosets]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§30 Orbit–Stabilizer]] →

*Reference: Pinter Ch. 13 (with Exs. C–D).*

> [!theorem] Proposition §29.1: All Cosets Have the Same Size
> Let $H \leq G$. For every $g \in G$,
>
> $$
> \#(gH) = |H| = \#(Hg) \qquad \text{in } \mathbb{Z}_{>0} \cup \{\infty\}.
> $$

^prop-29-1

> [!proof]+ Proof
> Define $\varphi: H \to gH$ by $\varphi(h) = gh$. It is surjective by the definition of $gH$. It is injective by cancellation ([[§2 First Consequences of the Axioms#^prop-2-1|Cancellation, §2.1]]): $gh_1 = gh_2 \implies h_1 = h_2$. So $\varphi$ is a bijection and $\#(gH) = |H|$. The map $h \mapsto hg$ gives the other equality.

^pf-29-1

*Uses:* [[§28 Left and Right Cosets#^def-28-2|Def. §28.2]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]

> [!definition] Definition §29.1: Index
> The **index** of $H$ in $G$, written $[G : H]$, is the number of left cosets of $H$ in $G$, an element of $\mathbb{Z}_{>0} \cup \{\infty\}$. The set of left cosets is denoted $G/H$, and the set of right cosets $H \backslash G$.

^def-29-1

> [!remark]- Connections
> - Index $2$ forces normality: [[§39 Sources of Normal Subgroups#^prop-39-1|Subgroups of Index 2 Are Normal, §39.1]].

> [!theorem] Theorem §29.2: Lagrange
> Let $H$ be a subgroup of $G$. Then
>
> $$
> |G| = |H| \cdot [G : H],
> $$
>
> meaning that the left-hand side is finite if and only if both factors on the right are finite, and in that case equality holds. In particular, if $G$ is a finite group, then $|H|$ divides $|G|$.

^thm-29-2

> [!proof]+ Proof
> *Idea:* $G$ is a disjoint union of $[G : H]$ cosets, each of size $|H|$.
>
> By [[§29 The Index and Lagrange's Theorem#^prop-29-1|All Cosets Have the Same Size]], $G$ is the disjoint union of its distinct left cosets; there are $[G : H]$ of them, and each has exactly $|H|$ elements. Counting the elements of $G$ gives $|G| = |H| \cdot [G : H]$.

^pf-29-2

*Uses:* [[§28 Left and Right Cosets#^prop-28-3|§28.3]], [[§29 The Index and Lagrange's Theorem#^prop-29-1|§29.1]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]]

![[m493-27-1.svg]]
*Lagrange in one picture: the left cosets (columns) are disjoint and cover $G$, and $h \mapsto g_2h$ (red) is a bijection $H \to g_2H$, so every column has exactly $|H|$ elements. Counting the dots gives $|G| = |H| \cdot [G:H]$.*

![[m493-27-a1.gif|480]]

*(Not from lecture; animation added, vault only.)* The cosets appear one at a time. Left: $H = \langle 4 \rangle$ in $\mathbb{Z}/12\mathbb{Z}$, four triangles $k + H$. Right: $H = \{e, (1\,2)\}$ in $S_3$, the left cosets $H$, $(1\,3)H$, $(2\,3)H$. They are disjoint, each has $|H|$ elements, and together they fill the group: $12 = 3 \cdot 4$, $6 = 2 \cdot 3$.

> [!remark]- Connections
> - MATH 590 states this without proof: [[§26 Algebra Prerequisites꞉ Groups#^prop-26-1|590 Prop. §26.1 (3)]].
> - Generalized to orbits: [[§30 Orbit–Stabilizer#^thm-30-3|Orbit–Stabilizer, §30.3]]; the homomorphism version: [[§41 The First and Second Isomorphism Theorems#^cor-41-2|§41.2]].
> - Elementary instance: Gauss's proof of Fermat in [[§24★ Congruence Modulo a Prime#^rem-24-1|250 Remark §24.1]] (three proofs of Fermat) is this argument for the powers of $a$ among the nonzero residues modulo $p$.

> [!theorem] Corollary §29.3: Order of an Element Divides $|G|$; $g^{|G|} = e$
> Let $G$ be a finite group and $g \in G$. Then $\operatorname{ord}(g)$ divides $|G|$, and $g^{|G|} = e$.

^cor-29-3

> [!proof]+ Proof
> Apply Lagrange to $H = \langle g \rangle$, whose order is $\operatorname{ord}(g)$ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]): $\operatorname{ord}(g) \mid |G|$. Writing $|G| = \operatorname{ord}(g)\,k$, we get $g^{|G|} = (g^{\operatorname{ord}(g)})^k = e$.

^pf-29-3

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§17 Cyclic Groups#^prop-17-3|§17.3]], [[§4 Subgroups#^lem-4-4|§4.4]]

> [!remark]- Connections
> - Elementary version for $G = U_p$: [[§24★ Congruence Modulo a Prime#^prop-24-3|250 Prop. §24.3]] (the order of $a$ modulo $p$ divides $p - 1$).

> [!theorem] Corollary §29.4: Fermat's Little Theorem
> Let $p$ be a prime. Then $a^{p-1} \equiv 1 \pmod p$ for every integer $a$ with $p \nmid a$.

^cor-29-4

> [!proof]+ Proof
> *Idea:* Lagrange in the group $(\mathbb{Z}/p\mathbb{Z})^\times$ of order $p - 1$.
>
> $(\mathbb{Z}/p\mathbb{Z})^\times$ is a group with $p - 1$ elements ([[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]]). For $p \nmid a$ we have $\gcd(a, p) = 1$, so $[a] \in (\mathbb{Z}/p\mathbb{Z})^\times$, and [[§29 The Index and Lagrange's Theorem#^cor-29-3|Order of an Element Divides]] $|G|$ gives $[a]^{p-1} = [1]$, i.e. $a^{p-1} \equiv 1 \pmod p$.

^pf-29-4

> [!remark] Remark: Uses of Lagrange
> The divisibility $|H| \mid |G|$ is the main tool for locating subgroups of a finite group (Example [[§29 The Index and Lagrange's Theorem#^ex-29-1|§29.1]]). It also explains the pattern observed in [[§15 Homomorphisms|§15]] for $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$ (Example [[§29 The Index and Lagrange's Theorem#^ex-29-2|§29.2]]): the index of the kernel equals the order of the image, a fact that the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|first isomorphism theorem]] will make precise for every homomorphism. Note also that the [[§29 The Index and Lagrange's Theorem#^ex-29-3|converse of Lagrange fails]] in general: a divisor of $|G|$ need not be the order of a subgroup (Example [[§29 The Index and Lagrange's Theorem#^ex-29-3|§29.3]], below).

^rem-29-1

> [!example] Example §29.1: Orders of Subgroups of $S_3$
> By Lagrange, the order of a subgroup of $S_3$ divides $|S_3| = 6$, so it is one of $1, 2, 3, 6$; in particular $S_3$ has no subgroup of order $4$ or $5$, since neither number divides $6$. All four orders occur: the subgroups of $S_3$ (Proposition [[§13 The Symmetric Group S₃#^prop-13-1|§13.1]], [[§13 The Symmetric Group S₃|§13]]) have orders $1, 2, 2, 2, 3, 6$.

^ex-29-1

> [!example] Example §29.2: The Pattern in $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$
> For $\varphi: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$, Example [[§15 Homomorphisms#^ex-15-2|§15.2]] found $\operatorname{Im}(\varphi) = \{1, 2, 4\}$, with $3$ elements, and $\operatorname{Ker}(\varphi) = \{0, 3\}$, with $2$, so that $3 \cdot 2 = 6$. Lagrange accounts for this. The kernel is a subgroup of $\mathbb{Z}/6\mathbb{Z}$ ([[§15 Homomorphisms|§15]]), so $[\mathbb{Z}/6\mathbb{Z} : \operatorname{Ker}(\varphi)] = 6/2 = 3$, which equals $|\operatorname{Im}(\varphi)|$. And the image is $\langle 2 \rangle \leq U_7$, of order $\operatorname{ord}(2) = 3$, which divides $|U_7| = 6$, as Order of an Element Divides $|G|$ (Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]]) requires.

^ex-29-2

*Uses:* [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]], [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]], [[§29 The Index and Lagrange's Theorem#^cor-29-3|§29.3]]

> [!remark]- Connections
> - Same theorem in 250, proved without groups by the bijection of [[§8 Invertibility and Unit Groups#^prop-8-2|§8.2]]: [[§24★ Congruence Modulo a Prime#^thm-24-1|250 Thm. §24.1]].

> [!theorem] Proposition §29.5: The Index Is Multiplicative
> Let $L \leq H \leq G$ with $[G : H]$ and $[H : L]$ finite. Then $[G : L]$ is finite and
>
> $$
> [G : L] = [G : H]\,[H : L].
> $$
>
> *Source: cf. Pinter Ch. 13, Ex. D1*

^prop-29-5

> [!proof]+ Proof
> Let $g_1H, \ldots, g_mH$ be the distinct left cosets of $H$ in $G$, and $h_1L, \ldots, h_nL$ those of $L$ in $H$. We show the $mn$ sets $g_ih_jL$ are exactly the distinct left cosets of $L$ in $G$.
>
> *They cover $G$:* for $x \in G$, $x \in g_iH$ for some $i$, so $g_i^{-1}x \in H$ lies in some $h_jL$, and $x \in g_ih_jL$.
>
> *They are distinct:* suppose $g_ih_jL = g_{i'}h_{j'}L$. Since $h_jL \subseteq H$, this coset lies in $g_iH$ and also in $g_{i'}H$; left cosets of $H$ are equal or disjoint, so $g_iH = g_{i'}H$ and $i = i'$. Cancelling $g_i$ on the left gives $h_jL = h_{j'}L$, so $j = j'$.

^pf-29-5

*Uses:* [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§28 Left and Right Cosets#^prop-28-3|§28.3]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]

![[m493-27-2.svg]]
*The proof of §29.5: each left coset $g_iH$ (blue column) is the translate by $g_i$ of $H = h_1K \sqcup \cdots \sqcup h_nK$, so it splits into the $n$ cosets $g_ih_jK$ (red cells). The $m$ columns tile $G$, so there are $mn$ cosets of $K$ in all: $[G:K] = [G:H]\,[H:K]$.*

> [!theorem] Theorem §29.6: Cauchy's Theorem
> Let $G$ be finite and $p$ a prime dividing $|G|$. Then $G$ has an element of order $p$.
>
> *Source: stated in lecture 10/12; cf. Pinter Ch. 13*

^thm-29-6

> [!proof]- Proof
> *[To be proved.]*

^pf-29-6

> [!remark] Remark: A Partial Converse to Lagrange
> Lagrange says that the order of every subgroup, and hence of every element, divides $|G|$. Cauchy's theorem is the converse for *prime* divisors. The standard proofs use either the class equation ([[§34 Conjugation as an Action and the Class Equation#^thm-34-4|§34.4]]) or an action of $\mathbb{Z}/p\mathbb{Z}$ on $p$-tuples together with orbit–stabilizer ([[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]).

^rem-29-2

> [!example] Example §29.3: The Converse of Lagrange Fails: $A_4$
> A divisor of $|G|$ need not be the order of a subgroup: $|A_4| = 12$, but $A_4$ has no subgroup of order $6$.
>
> *Source: not from class*

^ex-29-3

> [!proof]+ Proof
> Suppose $H \leq A_4$ with $|H| = 6$. Then $[A_4 : H] = 2$, so $H$ is normal ([[§39 Sources of Normal Subgroups#^prop-39-1|Subgroups of Index 2 Are Normal, §39.1]]) and $A_4/H$ is a group of order $2$ ([[§40 Quotient Groups#^thm-40-1|§40.1]]). In a group of order $2$ every element squares to the identity, so $(gH)^2 = H$, i.e. $g^2 \in H$, for every $g \in A_4$. For a $3$-cycle $\sigma$ this gives $\sigma = \sigma^4 = (\sigma^2)^2 \in H$, since $\sigma^2 \in H$. The eight $3$-cycles of $S_4$ are even ([[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]]), so they lie in $A_4$ and hence in $H$; with $e$, that is $9 > 6$ elements, a contradiction.

^pf-ex-29-3

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^prop-21-5|§21.5]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]]

> [!theorem] Theorem §29.7: Groups of Prime Order
> Let $p$ be a prime and let $G$ be a group with $|G| = p$. Then $G$ is cyclic; in fact $G = \langle g \rangle$ for *every* $g \neq e$, and $G \cong \mathbb{Z}/p\mathbb{Z}$.
>
> *Source: PS 2.5*

^thm-29-7

> [!proof]+ Proof
> *Idea:* For $g \neq e$, $|\langle g \rangle|$ divides $p$ and exceeds $1$, so $\langle g \rangle = G$.
>
> Since $p \geq 2$, choose $g \in G$ with $g \neq e$. By the pigeonhole proposition ([[§4 Subgroups#^prop-4-10|§4.10]]) $g$ has finite order, so $\langle g \rangle$ is a subgroup of $G$ with $|\langle g \rangle| = \operatorname{ord}(g)$ ([[§17 Cyclic Groups#^prop-17-3|§17.3]]). By Lagrange, $|\langle g \rangle|$ divides $p$, hence equals $1$ or $p$. If it were $1$ then $\langle g \rangle = \{e\}$, forcing $g = e$, contrary to the choice of $g$. So $|\langle g \rangle| = p = |G|$, and a subset of a finite set with as many elements is the whole set: $\langle g \rangle = G$. Thus $G$ is cyclic of order $p$, and $G \cong \mathbb{Z}/p\mathbb{Z}$ by the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups (§17.1)]] — explicitly, $\varphi([k]) = g^k$ is well defined (if $k' = k + mp$ then $g^{k'} = g^k(g^p)^m = g^k$), is a homomorphism by the [[§4 Subgroups#^lem-4-4|Exponent Laws]], is surjective since $\langle g \rangle = G$, and is injective since $g^{k} = g^{k'}$ forces $p \mid k' - k$ by minimality of $\operatorname{ord}(g) = p$.

^pf-29-7

*Uses:* [[§4 Subgroups#^prop-4-10|§4.10]], [[§4 Subgroups#^prop-4-5|§4.5]], [[§17 Cyclic Groups#^prop-17-3|§17.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§4 Subgroups#^def-4-6|Def. §4.6]], [[§4 Subgroups#^def-4-7|Def. §4.7]], [[§4 Subgroups#^def-4-8|Def. §4.8]], [[§17 Cyclic Groups#^thm-17-1|§17.1]], [[§4 Subgroups#^lem-4-4|§4.4]]

> [!remark]- Connections
> - Among abelian groups these are exactly the simple ones: [[§43 Simple Groups#^thm-43-1|Abelian Simple Groups, §43.1]].

> [!theorem] Corollary §29.8: Groups of Prime Order Have No Proper Nontrivial Subgroups
> If $|G| = p$ is prime, the only subgroups of $G$ are $\{e\}$ and $G$.

^cor-29-8

> [!proof]+ Proof
> By Lagrange, a subgroup has order dividing $p$, hence $1$ or $p$; the first gives $\{e\}$, the second gives $G$ by the cardinality argument [[§29 The Index and Lagrange's Theorem#^thm-29-7|above]].

^pf-29-8

> [!theorem] Corollary §29.9: Exactly One Group of Each Prime Order
> Let $p$ be a prime.
>
> 1. Up to isomorphism there is exactly one group of order $p$, namely $\mathbb{Z}/p\mathbb{Z}$.
> 2. In a group of order $p$ every non-identity element is a generator, so such a group has exactly $p - 1$ generators.

^cor-29-9

> [!proof]+ Proof
> *Idea:* Groups of Prime Order gives $G \cong \mathbb{Z}/p\mathbb{Z}$ and $G = \langle g \rangle$ for every $g \neq e$.
>
> **(1)** $\mathbb{Z}/p\mathbb{Z}$ is a group of order $p$. If $G$ and $G'$ are groups of order $p$, then $G \cong \mathbb{Z}/p\mathbb{Z}$ and $G' \cong \mathbb{Z}/p\mathbb{Z}$ by Groups of Prime Order (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]); since the inverse of an isomorphism is an isomorphism and a composite of isomorphisms is an isomorphism, $G \cong G'$.
>
> **(2)** By the same theorem $G = \langle g \rangle$ for every $g \neq e$, and there are $p - 1$ such $g$. The identity is not a generator, since $\langle e \rangle = \{e\} \neq G$ as $p \geq 2$. So the generators are exactly the $p - 1$ non-identity elements.

^pf-29-9

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]

> [!remark] Remark: A Classification, for Once
> Corollary [[§29 The Index and Lagrange's Theorem#^cor-29-9|§29.9]] is the first complete classification in these notes that covers infinitely many orders: contrast order $4$, where there are two groups (Example [[§29 The Index and Lagrange's Theorem#^ex-29-4|§29.4]]), and order $6$, where there are two (Example [[§29 The Index and Lagrange's Theorem#^ex-29-5|§29.5]]).

^rem-29-3

> [!example] Example §29.4: Two Groups of Order $4$
> $\mathbb{Z}/4\mathbb{Z}$ and the Klein four-group $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ both have order $4$ but are not isomorphic, as shown in [[§16 Isomorphisms|§16]]: in $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ every element $v$ satisfies $v + v = 0$, while in $\mathbb{Z}/4\mathbb{Z}$ the element $1$ has $1 + 1 = 2 \neq 0$. An isomorphism $\varphi: \mathbb{Z}/4\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ would give $\varphi(2) = \varphi(1) + \varphi(1) = 0 = \varphi(0)$, contradicting injectivity. (That every group of order $4$ is isomorphic to one of these two is asserted here, not proved.)

^ex-29-4

> [!example] Example §29.5: Two Groups of Order $6$
> $\mathbb{Z}/6\mathbb{Z}$ and $S_3$ both have order $6$ but are not isomorphic, being distinguished by commutativity. $\mathbb{Z}/6\mathbb{Z}$ is abelian; $S_3$ is not, since $(1\,2)(2\,3) = (1\,2\,3)$ while $(2\,3)(1\,2) = (1\,3\,2)$. An isomorphism $\varphi: \mathbb{Z}/6\mathbb{Z} \to S_3$ would make $S_3$ abelian: any $x, y \in S_3$ are $\varphi(a), \varphi(b)$ by surjectivity, and then $xy = \varphi(a + b) = \varphi(b + a) = yx$. (That every group of order $6$ is isomorphic to one of these two is asserted here, not proved.)

^ex-29-5

*Problem Set 5, Problem 1.*

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]

> [!theorem] Proposition §29.10: Index of an Intersection
> Let $H \leq G$ with $[G : H]$ finite, let $A \leq G$, and let $B = A \cap H$. Then $[A : B] \leq [G : H]$.
>
> *Source: PS 5.1(1)*

^prop-29-10

> [!proof]+ Proof
> *Idea:* $aB \mapsto aH$ is a well-defined injection $A/B \to G/H$.
>
> Define $\varphi: A/B \to G/H$ by $\varphi(aB) = aH$. *Well defined:* if $aB = a'B$, then $a = a'b_0$ with $b_0 \in B \subseteq H$, so $aH = a'b_0H = a'H$. *Injective:* if $aH = a'H$, then $h := a'^{-1}a \in H$, and $h \in A$ by closure of $A$; so $h \in A \cap H = B$ and $aB = a'hB = a'B$. Hence $A/B$ injects into the finite set $G/H$, and $[A : B] = |A/B| \leq |G/H| = [G : H]$.

^pf-29-10

*Uses:* [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]]

> [!example] Example §29.6: The Index Need Not Divide
> In general $[A : A \cap H]$ need not divide $[G : H]$. In $S_3$ take $H = \{e, (1\,2)\}$ and $A = \{e, (1\,3)\}$. Then $A \cap H = \{e\}$, so $[A : A \cap H] = 2$, while $[S_3 : H] = 3$, with cosets $H$, $(1\,3)H = \{(1\,3), (1\,2\,3)\}$, $(2\,3)H = \{(2\,3), (1\,3\,2)\}$. When $H$ is normal, divisibility does hold: Index of an Intersection, Normal Case ([[§41 The First and Second Isomorphism Theorems#^cor-41-8|Corollary §41.8]]).
>
> *Source: PS 5.1(2)*

^ex-29-6
