---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 28
tags: [group-theory, math493]
---
← [[§27 Orbits]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§29 The Index and Lagrange's Theorem]] →

*Reference: Pinter Ch. 13.*

> [!definition] Definition §28.1: Congruence Modulo a Subgroup
> Fix a group $G$ and a subgroup $H \subseteq G$. For $g_1, g_2 \in G$:
> 1. $g_1$ is **left congruent** to $g_2$ modulo $H$, written $g_1 \equiv_\ell g_2 \pmod H$, if $g_1^{-1} g_2 \in H$;
> 2. $g_1$ is **right congruent** to $g_2$ modulo $H$, written $g_1 \equiv_r g_2 \pmod H$, if $g_1 g_2^{-1} \in H$.

^def-28-1

> [!remark] Remark: Why Two Definitions, and When They Agree
> Since $H$ is a subgroup, $g_1 g_2^{-1} \in H \iff g_2 g_1^{-1} \in H$ (closure under inverses), so the right relation is symmetric in the two elements as expected. If $G$ is abelian, $g_1^{-1}g_2 = g_2 g_1^{-1}$ and the two relations coincide; in general they differ, which is the “small subtlety” of the non-commutative case. For $G = (\mathbb{Z}, +)$ and $H = n\mathbb{Z}$, both relations read $-g_1 + g_2 \in n\mathbb{Z}$, i.e. $g_1 \equiv g_2 \pmod n$: ordinary congruence.

^rem-28-1

> [!remark]- Connections
> - In a linear space with Y a subspace, written additively: equivalence mod Y, [[§2 Quotient Spaces and Complements#^def-2-1|556 Def. §2.1]].

> [!definition] Definition §28.2: Left and Right Cosets
> For $g \in G$ and $H \leq G$, the **left coset** of $H$ containing $g$ and the **right coset** are
>
> $$
> gH := \{ gh : h \in H \}, \qquad Hg := \{ hg : h \in H \}.
> $$

^def-28-2

> [!remark]- Connections
> - MATH 590 counterpart: [[§27 Free Groups and Presentations#^def-27-8|590 Def. §27.8 (Cosets)]].
> - Linear-algebra analogue of a coset $v + U$: [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97 (Translate)]].
> - With a topology: the coset space G/H with the quotient topology from the projection, [[§15 The Topology of G∕H and Real Grassmannians#^def-15-1|591 Def. §15.1]] (cosets restated in [[§14 Homogeneous Spaces#^def-14-5|591 Def. §14.5]]).
> - A coset in linear algebra: the solution set of Ax = b is the coset p + Nul A of the subgroup Nul A of ℝⁿ, [[§6 Solution Sets of Linear Systems#^thm-6-3|235 Thm. §6.3]].

> [!theorem] Proposition §28.1: Cosets Are Orbits
> Let $H$ be a subgroup of $G$.
> 1. $H$ acts on $G$ on the right by multiplication, $g \star h := gh$; its orbits are the left cosets $gH$, so $G/H$ is the orbit space of this right action — consistent with the notation $X/G$ above ([[§27 Orbits#^def-27-4|Def. §27.4]]).
> 2. $H$ acts on $G$ on the left by $h \star g := hg$; its orbits are the right cosets $Hg$, and the orbit space is $H \backslash G$.
> 3. Consequently $[G : H] = |G/H|$, and [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange]] reads $|G| = |H| \cdot |G/H| = |H| \cdot [G : H]$.
>
> More generally, if $H$ acts on any set $X$ on the left, $H \backslash X = \{Hx : x \in X\}$.
>
> *Source: lecture*

^prop-28-1

> [!proof]+ Proof
> (1) The right-action axioms are $g(h_1h_2) = (gh_1)h_2$ (associativity) and $ge = g$. The orbit of $g$ is $\{gh : h \in H\} = gH$. (2) Likewise with $(h_1h_2)g = h_1(h_2g)$, and orbit $Hg$. (3) The index counts left cosets, i.e. orbits in (1); Lagrange is [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]].

^pf-28-1

*Uses:* [[§25 Actions#^def-25-1|Def. §25.1]], [[§25 Actions#^def-25-2|Def. §25.2]], [[§27 Orbits#^def-27-1|Def. §27.1]], [[§27 Orbits#^def-27-2|Def. §27.2]], [[§27 Orbits#^def-27-4|Def. §27.4]], [[§28 Left and Right Cosets#^def-28-2|Def. §28.2]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!remark]- Connections
> - The other side of this picture, $G$ acting on the orbit space $G/H$: [[§31 G Acting on Coset Spaces#^prop-31-1|The Action of G on G∕H, §31.1]].
> - Used in 591 to present G/H as an orbit space, of H acting on G by right translation, [[§14 Homogeneous Spaces#^prop-14-4|591 Prop. §14.4]].

> [!theorem] Proposition §28.2: Cosets Are the Equivalence Classes
> Let $H$ be a subgroup of $G$.
> 1. $\equiv_\ell \pmod H$ is an equivalence relation on $G$, and its equivalence classes are exactly the left cosets $gH$, $g \in G$.
> 2. $\equiv_r \pmod H$ is an equivalence relation on $G$, and its equivalence classes are exactly the right cosets $Hg$, $g \in G$.
>
> In particular $G$ is the disjoint union of the distinct left cosets, and also of the distinct right cosets.

^prop-28-2

> [!proof]+ Proof
> We prove (1); (2) is similar.
>
> **Reflexive:** $g^{-1}g = e \in H$, so $g \equiv_\ell g$.
>
> **Symmetric:** if $g_1^{-1}g_2 \in H$, then since $H$ is closed under inverses and $(g_1^{-1}g_2)^{-1} = g_2^{-1}g_1$, we get $g_2^{-1}g_1 \in H$, i.e. $g_2 \equiv_\ell g_1$.
>
> **Transitive:** if $g_1^{-1}g_2 \in H$ and $g_2^{-1}g_3 \in H$, then by closure under products
>
> $$
> g_1^{-1}g_3 = (g_1^{-1}g_2)(g_2^{-1}g_3) \in H.
> $$
>
> **Classes are left cosets:** the class of $g$ is $\{g' : g \equiv_\ell g'\} = \{g' : g^{-1}g' \in H\}$. Now $g^{-1}g' \in H$ iff $g^{-1}g' = h$ for some $h \in H$, iff $g' = gh$ for some $h \in H$, iff $g' \in gH$. So the class of $g$ is $gH$.

^pf-28-2

*Uses:* [[§24 Equivalence Relations and Partitions#^def-24-1|Def. §24.1]], [[§24 Equivalence Relations and Partitions#^def-24-2|Def. §24.2]], [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§28 Left and Right Cosets#^def-28-2|Def. §28.2]]

> [!example] Example §28.1: Left and Right Cosets Differ in $S_3$
> Let $G = S_3$ and $H = \{e, (1\,2)\}$. Then
>
> $$
> (1\,3)H = \{(1\,3),\ (1\,3)(1\,2)\} = \{(1\,3),\ (1\,2\,3)\},
> $$
>
> $$
> H(1\,3) = \{(1\,3),\ (1\,2)(1\,3)\} = \{(1\,3),\ (1\,3\,2)\}.
> $$
>
> These are different sets, though both contain $(1\,3)$ and both have two elements.

^ex-28-1

![[m493-26-1.svg]]
*The same six elements of $S_3$, partitioned into the left cosets and into the right cosets of $H = \{e, (1\,2)\}$. Both partitions contain $H$ itself, but the other two blocks differ.*

> [!remark]- Connections
> - The same cosets, sorted by the value at $3$: [[§30 Orbit–Stabilizer#^ex-30-2|Ex. §30.2]] (via [[§30 Orbit–Stabilizer#^prop-30-4|§30.4]]).
> - The standard non-normal subgroup: [[§38 Normal Subgroups#^ex-38-1|A Non-Normal Subgroup of S₃, Ex. §38.1]].

> [!remark] Remark: Normal Subgroups
> In many important cases the two decompositions coincide, i.e. $gH = Hg$ for every $g$; such a subgroup is called *[[§38 Normal Subgroups#^def-38-1|normal]]*, and these are exactly the subgroups for which the set of cosets inherits a group structure. See [[· 8 Normal Subgroups and Quotient Groups|Chapter 8]]; the example [[§28 Left and Right Cosets#^ex-28-1|Left and Right Cosets Differ in S₃]] is the standard non-normal one.

^rem-28-2

## Counting Left and Right Cosets

> [!theorem] Proposition §28.3: A Natural Bijection $G/H \to H\backslash G$
> Let $H$ be a subgroup of $G$. The map
>
> $$
> G/H \longrightarrow H\backslash G, \qquad gH \longmapsto Hg^{-1},
> $$
>
> is a well-defined bijection, with inverse $Hg \mapsto g^{-1}H$. The content is well-definedness: for $g, g' \in G$,
>
> $$
> gH = g'H \iff Hg^{-1} = H(g')^{-1},
> $$
>
> i.e. $g \equiv_\ell g' \pmod H$ if and only if $g^{-1} \equiv_r (g')^{-1} \pmod H$. Consequently the number of left cosets equals the number of right cosets, and the index may equivalently be defined using right cosets.
>
> *Source: lecture exercise*

^prop-28-3

> [!proof]+ Proof
> For $g, g' \in G$: $gH = g'H$ iff $g^{-1}g' \in H$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]), while $Hg^{-1} = Hg'^{-1}$ iff $g^{-1}(g'^{-1})^{-1} = g^{-1}g' \in H$ (the [[§28 Left and Right Cosets#^prop-28-2|right-coset criterion]], with $H$ closed under inverses). The two conditions coincide, so $gH \mapsto Hg^{-1}$ is well defined and injective; it is surjective since every right coset is $Hg^{-1}$ for $g = (\text{its representative})^{-1}$. The inverse map $Hg \mapsto g^{-1}H$ is checked identically. Hence the numbers of left and right cosets agree.

^pf-28-3

*Uses:* [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!remark]- Connections
> - Why the inverse is forced, seen on the point stabilizer in $S_n$: [[§30 Orbit–Stabilizer#^rem-30-3|Why the Bijection Uses g⁻¹]].

> [!remark] Remark: This Is WS 4.1
> By [[§28 Left and Right Cosets#^prop-28-1|Cosets Are Orbits]], $G/H$ is the orbit space of the right action of $H$ on $G$ by multiplication, and $H\backslash G$ that of the left action. WS 4.1 ([[§25 Actions#^prop-25-1|§25.1]]) converts a right action into a left one by $g \mapsto g^{-1}$; applied here it sends the right-$H$-orbit $gH$ to the left-$H$-orbit $Hg^{-1}$. The bijection above is exactly that conversion, which is why the inverse is unavoidable.

^rem-28-3

> [!example] Example §28.2: The Map $gH \mapsto Hg$ Is Not Well Defined
> The obvious-looking assignment $gH \mapsto Hg$ is *not* well defined: in [[§28 Left and Right Cosets#^ex-28-1|Left and Right Cosets Differ in S₃]], $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ equals $(1\,2\,3)H$ (both contain $(1\,2\,3)$, and [[§28 Left and Right Cosets#^prop-28-2|cosets are equal or disjoint]]), but $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ and $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$ are different. Passing to the inverse is what repairs this.

^ex-28-2

![[m493-26-2.svg]]
*Inversion $g \mapsto g^{-1}$ fixes $e$ and the three transpositions and swaps $(1\,2\,3) \leftrightarrow (1\,3\,2)$ (red), so it carries each left coset of $H = \{e, (1\,2)\}$ (blue) onto a right coset: $(1\,3)H \mapsto H(1\,3)$ and $(2\,3)H \mapsto H(2\,3)$. This is the bijection $gH \mapsto Hg^{-1}$ of §28.3; by contrast $gH \mapsto Hg$ would send the single coset $(1\,3)H = (1\,2\,3)H$ to both $H(1\,3)$ and $H(1\,2\,3) = H(2\,3)$.*
