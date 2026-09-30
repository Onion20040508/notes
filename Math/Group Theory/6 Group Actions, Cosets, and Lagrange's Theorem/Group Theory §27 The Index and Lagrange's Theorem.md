---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 27
tags: [group-theory, math493]
---
← [[Group Theory §26 Left and Right Cosets]] · ↑ [[Group Theory — 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[Group Theory §28 Orbit–Stabilizer]] →

*Reference: Pinter Ch. 13 (with Exs. C–D).*

> [!theorem] Proposition §27.1: All Cosets Have the Same Size
> Let $H \leq G$. For every $g \in G$,
>
> $$
> \#(gH) = |H| = \#(Hg) \qquad \text{in } \mathbb{Z}_{>0} \cup \{\infty\}.
> $$

^prop-27-1

> [!proof]+ Proof
> Define $\varphi: H \to gH$ by $\varphi(h) = gh$. It is surjective by the definition of $gH$. It is injective by cancellation ([[Group Theory §2 First Consequences of the Axioms#^prop-2-1|Cancellation, §2.1]]): $gh_1 = gh_2 \implies h_1 = h_2$. So $\varphi$ is a bijection and $\#(gH) = |H|$. The map $h \mapsto hg$ gives the other equality.

^pf-27-1

*Uses:* [[Group Theory §26 Left and Right Cosets#^def-26-2|Def. §26.2]], [[Group Theory §2 First Consequences of the Axioms#^prop-2-1|§2.1]]

> [!definition] Definition §27.1: Index
> The **index** of $H$ in $G$, written $[G : H]$, is the number of left cosets of $H$ in $G$, an element of $\mathbb{Z}_{>0} \cup \{\infty\}$. The set of left cosets is denoted $G/H$, and the set of right cosets $H \backslash G$.

^def-27-1

> [!remark]- Connections
> - Index $2$ forces normality: [[Group Theory §36 Sources of Normal Subgroups#^prop-36-1|Subgroups of Index 2 Are Normal, §36.1]].

> [!theorem] Theorem §27.2: Lagrange
> Let $H$ be a subgroup of $G$. Then
>
> $$
> |G| = |H| \cdot [G : H],
> $$
>
> meaning that the left-hand side is finite if and only if both factors on the right are finite, and in that case equality holds. In particular, if $G$ is a finite group, then $|H|$ divides $|G|$.

^thm-27-2

> [!proof]+ Proof
> By [[Group Theory §27 The Index and Lagrange's Theorem#^prop-27-1|All Cosets Have the Same Size]], $G$ is the disjoint union of its distinct left cosets; there are $[G : H]$ of them, and each has exactly $|H|$ elements. Counting the elements of $G$ gives $|G| = |H| \cdot [G : H]$.

^pf-27-2

*Uses:* [[Group Theory §26 Left and Right Cosets#^prop-26-2|§26.2]], [[Group Theory §27 The Index and Lagrange's Theorem#^prop-27-1|§27.1]], [[Group Theory §27 The Index and Lagrange's Theorem#^def-27-1|Def. §27.1]]

> [!remark]- Connections
> - MATH 590 states this without proof: [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 §21.1 (3)]].
> - Generalized to orbits: [[Group Theory §28 Orbit–Stabilizer#^thm-28-3|Orbit–Stabilizer, §28.3]]; the homomorphism version: [[Group Theory §38 The First Isomorphism Theorem#^cor-38-2|§38.2]].

> [!theorem] Corollary §27.3: Order of an Element Divides $|G|$; $g^{|G|} = e$
> Let $G$ be a finite group and $g \in G$. Then $\operatorname{ord}(g)$ divides $|G|$, and $g^{|G|} = e$.

^cor-27-3

> [!proof]+ Proof
> Apply Lagrange to $H = \langle g \rangle$, whose order is $\operatorname{ord}(g)$ ([[Group Theory §17 Cyclic Groups#^prop-17-3|§17.3]]): $\operatorname{ord}(g) \mid |G|$. Writing $|G| = \operatorname{ord}(g)\,k$, we get $g^{|G|} = (g^{\operatorname{ord}(g)})^k = e$.

^pf-27-3

*Uses:* [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]], [[Group Theory §17 Cyclic Groups#^prop-17-3|§17.3]], [[Group Theory §4 Subgroups#^lem-4-4|§4.4]]

> [!theorem] Corollary §27.4: Fermat's Little Theorem
> Let $p$ be a prime. Then $a^{p-1} \equiv 1 \pmod p$ for every integer $a$ with $p \nmid a$.

^cor-27-4

> [!proof]+ Proof
> $(\mathbb{Z}/p\mathbb{Z})^\times$ is a group with $p - 1$ elements ([[Group Theory §8 Invertibility and Unit Groups#^prop-8-3|§8.3]]). For $p \nmid a$ we have $\gcd(a, p) = 1$, so $[a] \in (\mathbb{Z}/p\mathbb{Z})^\times$, and [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-3|Order of an Element Divides]] $|G|$ gives $[a]^{p-1} = [1]$, i.e. $a^{p-1} \equiv 1 \pmod p$.

^pf-27-4

*Uses:* [[Group Theory §8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]], [[Group Theory §8 Invertibility and Unit Groups#^prop-8-3|§8.3]], [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-3|§27.3]]

> [!remark] Remark: Uses of Lagrange
> The divisibility $|H| \mid |G|$ is the main tool for locating subgroups of a finite group: e.g. the subgroups of $S_3$ ([[Group Theory §13 Subgroups of S₃#^prop-13-1|§13.1]]) have orders $1, 2, 3, 6$, and no subgroup of order $4$ or $5$ can exist. [[Group Theory §27 The Index and Lagrange's Theorem#^cor-27-3|The corollary]] explains the pattern observed in [[Group Theory §15 Homomorphisms#^ex-15-2|Ex. §15.2]]: for $\varphi: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$, the image had $3$ elements and the kernel $2$, with $3 \cdot 2 = 6$ — the index of $\operatorname{Ker}(\varphi)$ equals $|\operatorname{Im}(\varphi)|$, a fact that the [[Group Theory §38 The First Isomorphism Theorem#^thm-38-1|first isomorphism theorem]] will make precise. Note also that the [[Group Theory §27 The Index and Lagrange's Theorem#^ex-27-1|converse of Lagrange fails]] in general: a divisor of $|G|$ need not be the order of a subgroup.

^rem-27-1

> [!theorem] Proposition §27.5: The Index Is Multiplicative
> Let $K \leq H \leq G$ with $[G : H]$ and $[H : K]$ finite. Then $[G : K]$ is finite and
>
> $$
> [G : K] = [G : H]\,[H : K].
> $$
>
> *Source: cf. Pinter Ch. 13, Ex. D1*

^prop-27-5

> [!proof]+ Proof
> Let $g_1H, \ldots, g_mH$ be the distinct left cosets of $H$ in $G$, and $h_1K, \ldots, h_nK$ those of $K$ in $H$. We show the $mn$ sets $g_ih_jK$ are exactly the distinct left cosets of $K$ in $G$.
>
> *They cover $G$:* for $x \in G$, $x \in g_iH$ for some $i$, so $g_i^{-1}x \in H$ lies in some $h_jK$, and $x \in g_ih_jK$.
>
> *They are distinct:* suppose $g_ih_jK = g_{i'}h_{j'}K$. Since $h_jK \subseteq H$, this coset lies in $g_iH$ and also in $g_{i'}H$; left cosets of $H$ are equal or disjoint, so $g_iH = g_{i'}H$ and $i = i'$. Cancelling $g_i$ on the left gives $h_jK = h_{j'}K$, so $j = j'$.

^pf-27-5

*Uses:* [[Group Theory §27 The Index and Lagrange's Theorem#^def-27-1|Def. §27.1]], [[Group Theory §26 Left and Right Cosets#^prop-26-2|§26.2]], [[Group Theory §2 First Consequences of the Axioms#^prop-2-1|§2.1]]

> [!theorem] Theorem §27.6: Cauchy's Theorem
> Let $G$ be finite and $p$ a prime dividing $|G|$. Then $G$ has an element of order $p$.
>
> *Source: not from class; cf. Pinter Ch. 13*

^thm-27-6

> [!proof]- Proof
> *[To be proved.]*

^pf-27-6

> [!remark] Remark: A Partial Converse to Lagrange
> Lagrange says that the order of every subgroup, and hence of every element, divides $|G|$. Cauchy's theorem is the converse for *prime* divisors. The standard proofs use either the class equation ([[Group Theory §32 Conjugation as an Action and the Class Equation#^thm-32-4|§32.4]]) or an action of $\mathbb{Z}/p\mathbb{Z}$ on $p$-tuples together with orbit–stabilizer ([[Group Theory §28 Orbit–Stabilizer#^thm-28-3|§28.3]]).

^rem-27-2

> [!example] Example §27.1: The Converse of Lagrange Fails: $A_4$
> A divisor of $|G|$ need not be the order of a subgroup: $|A_4| = 12$, but $A_4$ has no subgroup of order $6$.
>
> *Source: not from class*

^ex-27-1

> [!proof]+ Proof
> Suppose $H \leq A_4$ with $|H| = 6$. Then $[A_4 : H] = 2$, so $H$ is normal ([[Group Theory §36 Sources of Normal Subgroups#^prop-36-1|Subgroups of Index 2 Are Normal, §36.1]]) and $A_4/H$ is a group of order $2$ ([[Group Theory §37 Quotient Groups#^thm-37-1|§37.1]]). In a group of order $2$ every element squares to the identity, so $(gH)^2 = H$, i.e. $g^2 \in H$, for every $g \in A_4$. For a $3$-cycle $\sigma$ this gives $\sigma = \sigma^4 = (\sigma^2)^2 \in H$, since $\sigma^2 \in H$. The eight $3$-cycles of $S_4$ are even ([[Group Theory §20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]]), so they lie in $A_4$ and hence in $H$; with $e$, that is $9 > 6$ elements, a contradiction.

^pf-ex-27-1

*Uses:* [[Group Theory §20 The Sign Homomorphism and the Alternating Group#^prop-20-5|§20.5]], [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]], [[Group Theory §36 Sources of Normal Subgroups#^prop-36-1|§36.1]], [[Group Theory §37 Quotient Groups#^def-37-1|Def. §37.1]], [[Group Theory §37 Quotient Groups#^thm-37-1|§37.1]], [[Group Theory §11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]], [[Group Theory §20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[Group Theory §20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]]

> [!theorem] Theorem §27.7: Groups of Prime Order
> Let $p$ be a prime and let $G$ be a group with $|G| = p$. Then $G$ is cyclic; in fact $G = \langle g \rangle$ for *every* $g \neq e$, and $G \cong \mathbb{Z}/p\mathbb{Z}$.
>
> *Source: PS 2.5*

^thm-27-7

> [!proof]+ Proof
> Since $p \geq 2$, choose $g \in G$ with $g \neq e$. By the pigeonhole proposition ([[Group Theory §4 Subgroups#^prop-4-8|§4.8]]) $g$ has finite order, so $\langle g \rangle$ is a subgroup of $G$ with $|\langle g \rangle| = \operatorname{ord}(g)$ ([[Group Theory §17 Cyclic Groups#^prop-17-3|§17.3]]). By Lagrange, $|\langle g \rangle|$ divides $p$, hence equals $1$ or $p$. If it were $1$ then $\langle g \rangle = \{e\}$, forcing $g = e$, contrary to the choice of $g$. So $|\langle g \rangle| = p = |G|$, and a subset of a finite set with as many elements is the whole set: $\langle g \rangle = G$. Thus $G$ is cyclic of order $p$, and $G \cong \mathbb{Z}/p\mathbb{Z}$ by the [[Group Theory §17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups (§17.1)]] — explicitly, $\varphi([k]) = g^k$ is well defined (if $k' = k + mp$ then $g^{k'} = g^k(g^p)^m = g^k$), is a homomorphism by the [[Group Theory §4 Subgroups#^lem-4-4|Exponent Laws]], is surjective since $\langle g \rangle = G$, and is injective since $g^{k} = g^{k'}$ forces $p \mid k' - k$ by minimality of $\operatorname{ord}(g) = p$.

^pf-27-7

*Uses:* [[Group Theory §4 Subgroups#^prop-4-8|§4.8]], [[Group Theory §4 Subgroups#^prop-4-5|§4.5]], [[Group Theory §17 Cyclic Groups#^prop-17-3|§17.3]], [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]], [[Group Theory §4 Subgroups#^def-4-5|Def. §4.5]], [[Group Theory §17 Cyclic Groups#^thm-17-1|§17.1]], [[Group Theory §4 Subgroups#^lem-4-4|§4.4]]

> [!remark]- Connections
> - Among abelian groups these are exactly the simple ones: [[Group Theory §39 Simple Groups#^thm-39-1|Abelian Simple Groups, §39.1]].

> [!theorem] Corollary §27.8: Groups of Prime Order Have No Proper Nontrivial Subgroups
> If $|G| = p$ is prime, the only subgroups of $G$ are $\{e\}$ and $G$.

^cor-27-8

> [!proof]+ Proof
> By Lagrange, a subgroup has order dividing $p$, hence $1$ or $p$; the first gives $\{e\}$, the second gives $G$ by the cardinality argument [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-7|above]].

^pf-27-8

*Uses:* [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]], [[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-7|§27.7]]

> [!remark] Remark: A Classification, for Once
> For each prime $p$ there is exactly one group of order $p$ up to isomorphism. This is the first complete classification in these notes that covers infinitely many orders: contrast order $4$, where there are two groups ($\mathbb{Z}/4\mathbb{Z}$ and the Klein four-group $\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, distinguished in [[Group Theory §16 Isomorphisms#^prop-16-8|§16.8]]), and order $6$, where there are two ($\mathbb{Z}/6\mathbb{Z}$ and $S_3$, distinguished by commutativity). The proof also shows that in a group of prime order, *every* non-identity element is a generator — so such a group has $p - 1$ generators.

^rem-27-3
