---
type: section
subject: "[[Topology]]"
chapter: 7
section: "21a"
munkres: "§69"
tags: [topology, math590]
---
← [[§21 Algebra Prerequisites꞉ Groups]] · ↑ [[· 7 Algebraic Foundations]] · [[§22 Homotopy of Paths]] →

*The group-theory review of [[§21 Algebra Prerequisites꞉ Groups]] continued: cyclic groups, free groups and free products, group presentations, and the normal subgroups and quotient groups that make presentations rigorous.*

## Cyclic Groups and Free Groups

> [!definition] Definition §21.7: Powers
> Let $G$ be a group and $x \in G$. We define the **powers** of $x$:
> - $x^n = \underbrace{x \cdot x \cdots x}_{n}$ for $n > 0$ (the $n$-fold product of $x$ with itself),
> - $x^0 = e$ (the identity element),
> - $x^{-n} = \underbrace{x^{-1} \cdot x^{-1} \cdots x^{-1}}_{n}$ for $n > 0$.

^def-21-7

> [!definition] Definition §21.7: Cyclic Groups and Generators
> Let $G$ be a group and $x \in G$. If the set $\{x^m \mid m \in \mathbb{Z}\}$ of [[§21a Free Groups and Presentations#^def-21-7|powers]] equals all of $G$, then $G$ is called a **cyclic group** and $x$ is called a **generator** of $G$. We write $G = \langle x \rangle$.

^def-21-new2

> [!remark] Remark
> Every cyclic group is isomorphic to either $\mathbb{Z}$ (infinite cyclic) or $\mathbb{Z}/n\mathbb{Z}$ (cyclic of order $n$).
>
> **Infinite cyclic:** $G = \langle x \rangle \cong \mathbb{Z}$, where $x^m = x^n$ only if $m = n$. The elements $\ldots, x^{-2}, x^{-1}, e, x, x^2, \ldots$ are all distinct.
>
> **Finite cyclic of order $n$:** $G = \langle x \mid x^n = e \rangle \cong \mathbb{Z}/n\mathbb{Z}$. The relation $x^n = e$ forces everything to wrap around: $x^n = e$, $x^{n+1} = x$, $x^{-1} = x^{n-1}$. Exactly $n$ distinct elements: $\{e, x, x^2, \ldots, x^{n-1}\}$.
>
> **Why $\mathbb{Z}$ is “free on one generator”:** If $G = \langle x \rangle \cong \mathbb{Z}$ and $H$ is *any* group with an element $h \in H$, there is a unique homomorphism $\varphi: G \to H$ with $\varphi(x) = h$, defined by $\varphi(x^n) = h^n$. This is well-defined because there are no relations to check — the only constraint is $x \cdot x^{-1} = e$, and $h \cdot h^{-1} = e$ holds automatically in any group. You can map the generator *anywhere*, no questions asked.

^rem-21-9

> [!remark]- Connections
> - Linear-algebra analogue of “map the generator anywhere”: [[Linear map lemma]].
> - Developed in full in Group Theory: integer powers [[§4 Subgroups#^def-4-2|493 Def. §4.2]] with the [[Exponent Laws]], cyclic groups [[§4 Subgroups#^def-4-5|493 Def. §4.5]]; the classification in the remark is proved as [[Classification of Cyclic Groups]] ([[§17 Cyclic Groups#^thm-17-1|493 Thm. §17.1]]), and mapping a generator anywhere is [[§17 Cyclic Groups#^prop-17-3|493 Prop. §17.3]].

> [!definition] Definition §21.8: Free Group
> The **free group** $F_n$ on generators $\{a_1, \ldots, a_n\}$ consists of all **reduced words** in the symbols $a_i$ and $a_i^{-1}$. A **word** is a finite sequence like $a_1^2 a_3^{-1} a_2 a_1^{-1}$. A word is **reduced** if no adjacent pair cancels (no $a_i a_i^{-1}$ or $a_i^{-1} a_i$ appears). The group operation is concatenation followed by reduction, the identity is the empty word $\varepsilon$, and the inverse of $s_1 \cdots s_k$ is $s_k^{-1} \cdots s_1^{-1}$.
>
> “Free” means **no relations** between generators other than $a_i a_i^{-1} = e$. In particular, $F_1 \cong \mathbb{Z}$ (one generator, no relations — just powers $a^n$). For $F_2 = \langle a, b \rangle$: $ab \neq ba$ (the group is non-abelian), and every different-looking reduced word is a different element.

^def-21-8

> [!remark]- Connections
> - Formal version: [[§21a Free Groups and Presentations#^def-21-10|Free Group on Elements]]. $F_n$ is $\pi_1$ of a wedge of $n$ circles: [[§29 The Seifert–van Kampen Theorem#^ex-29-3|Example §29.3]].
> - Words in an arbitrary group, and the subgroup they generate: [[§4 Subgroups#^def-4-4|493 Def. §4.4]]; in a free group distinct reduced words are distinct elements, in a general group they need not be.

> [!example] Example §21.3: Multiplication in $F_2$
> The operation is “concatenate, then cancel adjacent inverse pairs until reduced”:
> 1. $(ab^{-1}) \cdot (ba) = ab^{-1}ba$. The $b^{-1}$ and $b$ cancel: $\to a \cdot a = a^2$.
> 2. $(ab) \cdot (b^{-1}a^{-1}) = abb^{-1}a^{-1} \to aa^{-1} \to \varepsilon$. Cascading cancellation; confirms $(ab)^{-1} = b^{-1}a^{-1}$.
> 3. $(aba) \cdot (a^{-1}b) = abaa^{-1}b \to ab^2$. Only the inner $a, a^{-1}$ pair cancels.
> 4. $(ab^{-1}) \cdot (ba^{-1}) = ab^{-1}ba^{-1} \to aa^{-1} \to \varepsilon$. Two rounds of cancellation.
> 5. $ab \cdot ba = abba = ab^2a$. No cancellation at all — $b$ and $b$ are from the same generator, so they combine to $b^2$.
>
> **What “no relations” really means:** Two reduced words are equal if and only if they are literally the same string. In particular: $ab \neq ba$ (different strings, both reduced), $aba^{-1}b^{-1} \neq \varepsilon$ (already reduced, no adjacent pair cancels), $a^2b^3 \neq b^3a^2$ (different strings). Compare with $\mathbb{Z} \times \mathbb{Z}$: there the relation $ab = ba$ lets you rearrange any word into $a^m b^n$. In $F_2$, order is permanent.

^ex-21-3

> [!definition] Definition §21.9: Free Product of Groups
> Let $G$ and $H$ be groups. The **free product** $G \ast  H$ is the group whose elements are **reduced words** — finite alternating sequences of nontrivial elements from $G$ and $H$:
>
> $$
> g_1 h_1 g_2 h_2 \cdots \qquad \text{or} \qquad h_1 g_1 h_2 g_2 \cdots
> $$
>
> where each $g_i \in G \setminus \{e_G\}$ and each $h_i \in H \setminus \{e_H\}$. “Reduced” means no adjacent elements come from the same group (if they did, multiply them using that group's operation).
>
> The group operation is **concatenation followed by reduction**:
>
> $$
> (a_1 \cdots a_n) * (b_1 \cdots b_m) = a_1 \cdots a_n b_1 \cdots b_m \quad \text{(then reduce if $a_n$ and $b_1$ are in the same group)}.
> $$
>
> The identity is the empty word. The inverse of $a_1 \cdots a_n$ is $a_n^{-1} \cdots a_1^{-1}$.

^def-21-9

> [!remark]- Connections
> - Where free products arise as $\pi_1$: [[§29 The Seifert–van Kampen Theorem#^cor-29-2|Free Product Formula]].

> [!example] Example §21.4: $\mathbb{Z} * \mathbb{Z} \cong F_2$
> Let $G = \mathbb{Z} = \{a^n \mid n \in \mathbb{Z}\}$ and $H = \mathbb{Z} = \{b^m \mid m \in \mathbb{Z}\}$. Then $G * H$ consists of all reduced words in powers of $a$ and powers of $b$:
>
> $$
> \mathbb{Z} * \mathbb{Z} = \{a^{n_1} b^{m_1} a^{n_2} b^{m_2} \cdots a^{n_j} b^{m_j} \mid n_i, m_i \in \mathbb{Z} \setminus \{0\} \text{ (except possibly first/last)}\}.
> $$
>
> This is exactly $F_2$: reduced words in $a, a^{-1}, b, b^{-1}$.
>
> **Not abelian:** $a \ast  b \neq b \ast  a$ (both are already reduced, and they are different words).
>
> **Compare with $\mathbb{Z} \times \mathbb{Z}$:** In the direct product, $a^{n_1}b^{m_1}a^{n_2}b^{m_2} = a^{n_1+n_2}b^{m_1+m_2}$ (rearrange using commutativity). In the free product, you *cannot* rearrange — order matters.

^ex-21-4

![[m590-21-1.svg]]
*Why order is permanent in $F_2$ but not in $\mathbb{Z} \times \mathbb{Z}$. In both pictures the vertices are group elements and an edge joins $w$ to $wa$ (blue) or to $wb$ (red). From the identity, the words $ab$ and $ba$ (gray paths) end at *different* vertices of the tree for $F_2$: a tree has no cycles, so each reduced word is its own path and no relation closes the square. In the grid for $\mathbb{Z} \times \mathbb{Z}$ the relation $ab = ba$ closes every square, and both words land on the same vertex.*

> [!remark]- Connections
> - Realized as $\pi_1$ of the figure eight: [[§29 The Seifert–van Kampen Theorem#^ex-29-2|Example §29.2]].

> [!example] Example §21.5: Multiplication in $\mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/3\mathbb{Z}$
> Let $G = \langle a \mid a^2 = e \rangle$ and $H = \langle b \mid b^3 = e \rangle$. The nontrivial elements of $G$: just $a$ (since $a^2 = e$, $a = a^{-1}$). The nontrivial elements of $H$: $b$ and $b^2$ (since $b^3 = e$, $b^{-1} = b^2$). Some multiplications:
> 1. $a \cdot a = a^2 = e_G$. Both from $G$, so multiply in $G$: cancels to $\varepsilon$.
> 2. $b \cdot b = b^2$. Both from $H$, multiply in $H$: stays as $b^2$.
> 3. $a \cdot b = ab$. Different groups, no simplification.
> 4. $ab \cdot ab = abab$. No adjacent pair from same group. Result: $abab$.
> 5. $(aba) \cdot (ab^2) = abaab^2$. The two $a$'s are adjacent, both from $G$: $a \cdot a = e$, delete. Left with $ab \cdot b^2 = ab^3$. Now $b^3 = e_H$, so $ab^3 = a$. **Two rounds of cascading cancellation.**
>
> This group is infinite — alternating strings $ababab\cdots$ of any length are all distinct — even though both factors are finite ($|G| = 2$, $|H| = 3$). Compare with $G \times H = \mathbb{Z}/2 \times \mathbb{Z}/3 \cong \mathbb{Z}/6$, which has only $6$ elements.

^ex-21-5

> [!remark] Remark: Direct Product vs Free Product
> | | **Direct Product $G \times H$** | **Free Product $G \ast  H$** |
> |---|---|---|
> | Elements | Pairs $(g, h)$ | Reduced alternating words |
> | Relation | $G$ and $H$ commute: $(g, e)(e, h) = (e, h)(g, e)$ | No relation between $G$ and $H$ |
> | Size | $\vert G\vert \cdot \vert H\vert$ | Much larger (usually infinite) |
> | Abelian? | Yes if $G, H$ abelian | Almost never |
> | $\pi_1$ of | Product spaces ($X \times Y$) | Wedge sums ($X \vee Y$, via van Kampen) |
>
> The free product is the “most general” way to combine two groups: no relations imposed. The direct product forces commutativity between the factors. Every other way of combining $G$ and $H$ is a quotient of $G * H$ (impose relations to get a smaller group).

^rem-21-10

> [!remark]- Connections
> - The last row: [[§23 The Fundamental Group#^thm-23-7|π₁ of a Product Space]]; [[§28 Fundamental Group of Some Surfaces#^def-28-3|Wedge Sum]] with the [[§29 The Seifert–van Kampen Theorem#^cor-29-2|Free Product Formula]].

> [!remark] Remark: Groups in Algebraic Topology
> | **Group** | **Description** | **Appears as $\pi_1$ of** |
> |---|---|---|
> | $\{e\}$ | Trivial | Simply connected spaces ($\mathbb{R}^n$, $S^n$ for $n \geq 2$) |
> | $\mathbb{Z}$ | Infinite cyclic | $S^1$, cylinder, Möbius band |
> | $\mathbb{Z}/n\mathbb{Z}$ | Finite cyclic | Lens spaces; for $n = 2$, $P^m$ ($m \geq 2$) |
> | $\mathbb{Z}^n$ | Free abelian (direct product) | Torus $T^n = (S^1)^n$ |
> | $F_n \cong \mathbb{Z} * \cdots * \mathbb{Z}$ | Free on $n$ generators (free product) | Wedge of $n$ circles |

^rem-21-11

> [!remark]- Connections
> - Trivial: [[§23 The Fundamental Group#^ex-23-1|ℝⁿ is Simply Connected]], [[Sⁿ is Simply Connected for n ≥ 2|Sⁿ is Simply Connected for n ≥ 2]]. Infinite cyclic: [[Fundamental Group of the Circle|π₁(S¹) ≅ ℤ]].
> - Finite cyclic: [[§28 Fundamental Group of Some Surfaces#^thm-28-3|π₁(Pⁿ) for all n]]. Free abelian: [[§23 The Fundamental Group#^cor-23-8|Fundamental Group of the Torus]]. Free: [[§29 The Seifert–van Kampen Theorem#^ex-29-3|Example §29.3]].

> [!remark] Remark: The Hierarchy of Relations
> $$
> \underbrace{\mathbb{Z}/n\mathbb{Z}}_{\text{one gen, one rel}} \;\longleftarrow\; \underbrace{\mathbb{Z} \cong F_1}_{\text{one gen, no rel}} \;\longleftarrow\; \underbrace{F_n = \mathbb{Z} * \cdots * \mathbb{Z}}_{\text{$n$ gen, no rel}} \;\overset{\text{add rels $ab = ba$}}{\longrightarrow}\; \underbrace{\mathbb{Z}^n}_{\text{$n$ gen, all commute}}
> $$
>
> Each arrow represents adding a relation, which makes the group smaller. The free group $F_n$ is the largest group on $n$ generators — every other group with $\leq n$ generators is a quotient of it. In particular:
>
> $$
> G \times H = (G * H) / \langle ghg^{-1}h^{-1} \mid g \in G, h \in H \rangle.
> $$
>
> You start with the free product (no relations between factors) and impose commutativity. This shrinks the group whenever both factors are nontrivial: $F_2$ is non-abelian, while $\mathbb{Z}^2$ is abelian, so the quotient map $F_2 \to \mathbb{Z}^2$ sends the nontrivial element $aba^{-1}b^{-1}$ to the identity. Adding relations kills elements.

^rem-21-12

## Group Presentations

> [!definition] Definition §21.10: Free Group on Elements
> Let $\{a_\alpha\}_{\alpha \in J}$ be an arbitrary indexed family. For each $\alpha$, let $G_\alpha = \{a_\alpha^n \mid n \in \mathbb{Z}\} \cong \mathbb{Z}$. The [[§21a Free Groups and Presentations#^def-21-9|free product]] $\ast _{\alpha \in J}\, G_\alpha$ is called the **free group on the elements** $\{a_\alpha\}$, and $\{a_\alpha\}$ is called a **system of free generators**.

^def-21-10

> [!definition] Definition §21.11: Group Presentation
> Let $G$ be a group with a family of generators $\{a_\alpha\}_{\alpha \in J}$. Let $F$ be the [[§21a Free Groups and Presentations#^def-21-10|free group]] on $\{a_\alpha\}$. Then there exists a surjective homomorphism $h: F \to G$ with $h(a_\alpha) = a_\alpha$.
>
> Let $N = \ker(h)$, which is a [[§21a Free Groups and Presentations#^def-21-12|normal subgroup]] of $F$ (defined below, with the [[§21a Free Groups and Presentations#^def-21-new3|quotient group]] $F/N$). Then $F/N \cong G$ (by the [[First Isomorphism Theorem for Groups|first isomorphism theorem]]). Each element of $N$ is called a **relation** on $F$.
>
> If $\{r_\beta\}_{\beta \in I}$ is a set of elements of $F$ such that $\{r_\beta\}$ and their conjugates generate $N$, then $\{r_\beta\}$ is called a **complete set of relations** for $G$.
>
> A **presentation** for $G$ is denoted
>
> $$
> G \cong \langle\, a_\alpha \mid r_\beta \,\rangle
> $$
>
> consisting of a family of generators $\{a_\alpha\}$ and a complete set of relations $\{r_\beta\}$.

^def-21-11

> [!remark]- Connections
> - Vector-space version of the first isomorphism theorem: [[First isomorphism theorem]] (with [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]]).
> - Why $\ker(h)$ is normal: [[§21a Free Groups and Presentations#^rem-21-17|Remark after Definition §21.12]]; the quotient $F/N$: [[§21a Free Groups and Presentations#^def-21-new3|Quotient Group]].

> [!remark] Remark: Reading the $\langle \mid \rangle$ Notation
> The bar $\mid$ separates *what you have* (generators) from *what you force* (relations). Building up:
> - $\langle a \rangle$ = the group generated by $a$ = all powers $\{\ldots, a^{-2}, a^{-1}, e, a, a^2, \ldots\}$. With no relations, this is $\mathbb{Z}$.
> - $\langle a, b \rangle$ = the group generated by $a$ and $b$ = all reduced words in $a, b$. With no relations, this is $F_2 = \mathbb{Z} * \mathbb{Z}$.
> - $\langle a \mid a^n \rangle$ = $\langle a \rangle$ with $a^n$ forced to $e$. Only $\{e, a, \ldots, a^{n-1}\}$ survive. This is $\mathbb{Z}/n\mathbb{Z}$.
> - $\langle a, b \mid aba^{-1}b^{-1} \rangle$ = $\langle a, b \rangle$ with $ab = ba$ forced. Every word simplifies to $a^m b^n$. This is $\mathbb{Z} \times \mathbb{Z}$.
>
> Formally: $\langle a_1, \ldots, a_k \mid r_1, \ldots, r_m \rangle = F_k / \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$ where $F_k$ is the free group and $\langle\!\langle \cdot \rangle\!\rangle$ denotes the normal closure (smallest normal subgroup containing $r_1, \ldots, r_m$).

^rem-21-13

> [!example] Example §21.6: Standard Presentations
> 1. $\langle\, a \mid \emptyset\,\rangle = \langle\, a \,\rangle \cong \mathbb{Z}$. One generator, no relations: the free group on one element.
> 2. $\langle\, a, b \mid \emptyset\,\rangle \cong \mathbb{Z} * \mathbb{Z} = F_2$. Two generators, no relations: the free group on two elements. Elements are reduced words like $a^2 b^{-1} a b^3$.
> 3. $\langle\, a \mid a^n \,\rangle \cong \mathbb{Z}/n\mathbb{Z}$. One generator, one relation $a^n = e$: the cyclic group of order $n$.
> 4. $\langle\, a, b \mid aba^{-1}b^{-1} \,\rangle \cong \mathbb{Z} \times \mathbb{Z}$. Two generators, one relation $ab = ba$: the free *abelian* group on two generators. This is $F_2$ with commutativity forced.
> 5. $\langle\, a, b \mid a^3, b^4 \,\rangle \cong \mathbb{Z}/3\mathbb{Z} * \mathbb{Z}/4\mathbb{Z}$. Two generators, each constrained independently: free product.

^ex-21-6

> [!remark] Remark: Simplifying Presentations
> Three techniques for reducing $\langle \text{generators} \mid \text{relations} \rangle$:
>
> **1. Elimination.** If a relation lets you solve for one generator in terms of others (e.g., $a = \text{word in } b$), substitute everywhere and eliminate that generator. This reduces the number of generators.
>
> *Example:* $\langle a, b \mid aba^{-1}b^{-1}, a \rangle$. The relation $a = e$ lets us substitute $a = e$ everywhere. The other relation becomes $ebe^{-1}b^{-1} = bb^{-1} = e$ (automatic). Result: $\langle b \rangle \cong \mathbb{Z}$.
>
> **2. Splitting.** If each relation involves only one generator, the group splits as a free product: $\langle a, b \mid r(a), s(b) \rangle \cong \langle a \mid r(a) \rangle \ast  \langle b \mid s(b) \rangle$.
>
> *Example:* $\langle a, b \mid b^4 \rangle$. The relation constrains only $b$; $a$ is free. So $\langle a \rangle \ast  \langle b \mid b^4 \rangle \cong \mathbb{Z} \ast  \mathbb{Z}/4\mathbb{Z}$.
>
> **3. Abelianization.** If the relation forces all generators to commute (contains $a_i a_j a_i^{-1} a_j^{-1}$ for all pairs $i, j$), the free product becomes a direct product.
>
> *Example:* $\langle a, b \mid aba^{-1}b^{-1} \rangle$. The relation $ab = ba$ turns $F_2$ into $\mathbb{Z} \times \mathbb{Z}$.

^rem-21-14

> [!remark] Remark: Connection to Van Kampen
> The [[Seifert–van Kampen Theorem|Seifert-van Kampen theorem]] ([[§29 The Seifert–van Kampen Theorem|§29]]) outputs a group as $(G * H)/N$. The $\langle \mid \rangle$ notation makes this concrete. If $G = \langle a_1, \ldots \mid R_1, \ldots \rangle$ and $H = \langle b_1, \ldots \mid S_1, \ldots \rangle$, then:
> - **Free product** (pool generators, keep existing relations, no new ones):
>
>   $$
>   G * H = \langle a_1, \ldots, b_1, \ldots \mid R_1, \ldots, S_1, \ldots \rangle.
>   $$
>
> - **Quotient by $N$** (add new relations from $A \cap B$):
>
>   $$
>   (G * H)/N = \langle a_1, \ldots, b_1, \ldots \mid R_1, \ldots, S_1, \ldots, \underbrace{i_1(t_1) \cdot i_2(t_1)^{-1}, \ldots}_{\text{new: force } i_1(t) = i_2(t)} \rangle.
>   $$
>
> So $(G * H)/N$ means: take the free product (maximum freedom between $G$ and $H$), then add relations that identify loops in $A \cap B$ as seen from both sides. The recipe for computing $i_1(t)$ and $i_2(t)$ — tracing loops through $A$ and $B$ — is the [[§29 The Seifert–van Kampen Theorem#^rem-29-4|geometric step]] in [[§29 The Seifert–van Kampen Theorem|§29]].

^rem-21-15

## Normal Subgroups and Quotient Groups

The notation $\langle a, b \mid r \rangle$ means “force $r = e$.” But what does “force” mean rigorously? Quotient groups are the answer — they are the machinery that makes presentations well-defined.

> [!remark] Remark: The Problem Presentations Solve
> When we write $\langle a, b \mid a^3 \rangle$ and say “force $a^3 = e$, simplify words using this rule,” we are implicitly claiming: (1) the result is a group, (2) the operation is well-defined (simplifying in different orders gives the same answer), and (3) we know which words are “the same.” Quotient groups provide the rigorous foundation for all three claims.

^rem-21-16

> [!definition] Definition §21.12: Normal Subgroup
> $N \leq G$ is **normal** ($N \trianglelefteq G$) if $gng^{-1} \in N$ for all $g \in G$, $n \in N$. Equivalently: conjugating any element of $N$ by anything in $G$ stays in $N$.

^def-21-12

> [!remark]- Connections
> - Developed in full in Group Theory: [[§38 Normal Subgroups#^def-38-1|493 Def. §38.1]], with equivalent forms in [[Characterizations of Normality]]; the kernel fact of the next remark is [[Kernels Are Normal]].

> [!remark] Remark
> Every subgroup of an abelian group is normal ($gng^{-1} = n \in N$, since conjugation does nothing). The [[§21 Algebra Prerequisites꞉ Groups#^def-21-6|kernel]] of any homomorphism is always normal: if $f(n) = e$, then $f(gng^{-1}) = f(g) \cdot e \cdot f(g)^{-1} = e$, so $gng^{-1} \in \ker(f)$.

^rem-21-17

> [!definition] Definition §21.13: Cosets
> The **left coset** of $N$ by $g$ is $gN = \{gn \mid n \in N\}$.

^def-21-13

> [!definition] Definition §21.13: Quotient Group
> If $N \trianglelefteq G$, the **quotient group** $G/N = \{gN \mid g \in G\}$ with operation $(gN)(hN) = (gh)N$. The canonical map $p: G \to G/N$, $x \mapsto xN$, is a surjective homomorphism with $\ker(p) = N$.

^def-21-new3

> [!remark]- Connections
> - Linear-algebra versions: cosets ↔ [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|Translate]], $G/N$ ↔ [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]], $p$ ↔ [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]].
> - Topological version: [[§12 Quotient Topology#^def-12-3|Quotient Space]].
> - Developed in full in Group Theory: cosets in [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2]] ([[Cosets Partition a Group]]) and quotient groups in [[§40 Quotient Groups#^def-40-1|493 Def. §40.1]] ([[Quotient Groups]]).

> [!remark] Remark: What the Slash Means
> $G/N$ means: take $G$, declare everything in $N$ to be the identity, see what's left. Two elements $g, h \in G$ become “the same” in $G/N$ if they differ by something in $N$ — i.e., $g^{-1}h \in N$. The slash is literally division: you divide $G$ into groups of equivalent elements (cosets). Each coset $gN$ is one element of $G/N$. The elements of $N$ itself all collapse to the identity coset $eN = N$.
>
> The notation is consistent across mathematics:
>
> | **Context** | **Notation** | **Meaning** |
> |---|---|---|
> | Integers | $\mathbb{Z}/n\mathbb{Z}$ | Force multiples of $n$ to $0$ (mod $n$) |
> | Groups | $G/N$ | Force $N = e$ (collapse a subgroup) |
> | Topology | $X/{\sim}$ | Force $x \sim y$ (glue points together) |
>
> Same idea everywhere: identify things, see what remains.

^rem-21-18

> [!remark] Remark: Why Normality is Required
> The operation on $G/N$ is $(gN)(hN) = (gh)N$: multiply representatives, take the coset of the result. This requires **well-definedness**: if we pick different representatives $g' \in gN$ and $h' \in hN$, we need $(g'h')N = (gh)N$.
>
> Suppose $g' = gn_1$ and $h' = hn_2$ for some $n_1, n_2 \in N$. Then:
>
> $$
> g'h' = gn_1 \cdot hn_2 = g \cdot (n_1 h) \cdot n_2 = g \cdot h \cdot \underbrace{(h^{-1} n_1 h)}_{\in N?} \cdot n_2.
> $$
>
> We need $h^{-1}n_1 h \in N$, i.e., conjugation by any $h \in G$ must send $N$ back into $N$. This is exactly the **normality** condition $gNg^{-1} \subseteq N$. If $N$ is not normal, the “multiplication” gives different answers depending on which representative you pick — not a well-defined operation, not a group.
>
> For abelian groups (like $\mathbb{Z}$), every subgroup is automatically normal ($gng^{-1} = n$), so this is never an issue. For non-abelian groups, you must check.

^rem-21-19

> [!example] Example §21.7: $\mathbb{Z}/n\mathbb{Z}$
> $n\mathbb{Z} \trianglelefteq \mathbb{Z}$ (normal since $\mathbb{Z}$ abelian). Force all multiples of $n$ to equal $0$: then $n = 0$, so $n+1 = 1$, $n+2 = 2$, $2n = 0$, etc. Everything wraps around. Only $n$ distinct elements survive: $\{[0], [1], \ldots, [n-1]\}$ with addition mod $n$.
>
> *Concrete case $n = 3$:* Start with $\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, 4, 5, \ldots\}$. Force $3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, 9, \ldots\}$ to equal $0$. Since $3 = 0$: $4 = 3+1 = 1$, $5 = 3+2 = 2$, $7 = 6+1 = 1$, $-1 = -3+2 = 2$. Every integer collapses to its remainder mod $3$. Result: $\mathbb{Z}/3\mathbb{Z} = \{[0], [1], [2]\}$ with $[2] + [1] = [0]$.

^ex-21-7

> [!remark]- Connections
> - 493 counterpart: [[§7 The Group ℤ∕nℤ#^def-7-1|493 Def. §7.1]], and ℤ/nℤ as a quotient group in [[§40 Quotient Groups#^ex-40-1|493 Ex. §40.1]].

> [!example] Example §21.8: Forcing Commutativity
> Start with $F_2 = \langle a, b \rangle$ (all words in $a, b$, no simplification). Force $aba^{-1}b^{-1} = e$, i.e., $ab = ba$. Now every word reduces to $a^m b^n$: for instance, $bab^{-1} = a$, $a^2ba^{-1} = ab$, $baba = a^2b^2$. Result: $\mathbb{Z} \times \mathbb{Z}$.

^ex-21-8

> [!remark] Remark: How Quotient Groups Make Presentations Rigorous
> The presentation $\langle a_1, \ldots, a_k \mid r_1, \ldots, r_m \rangle$ is formally defined as $F_k / \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$:
> 1. Start with the free group $F_k = \langle a_1, \ldots, a_k \rangle$ — all reduced words, no relations.
> 2. “Force $r_j = e$” means: declare two words $u, v$ to be the same whenever they differ by insertions/deletions of $r_j$ and its conjugates $gr_jg^{-1}$. (Why conjugates? If $r = e$, then $grg^{-1} = geg^{-1} = e$ too — logical consequence.)
> 3. The set of all words that become trivial forms $N = \langle\!\langle r_1, \ldots, r_m \rangle\!\rangle$ — the **normal closure**, the smallest normal subgroup containing all the $r_j$.
> 4. The resulting group is $F_k / N$: the free group modulo the relations.
>
> You do not need quotient groups to *use* presentations — “force $r = e$, simplify words” gives correct answers. The quotient group is the proof that this process is well-defined and gives a group.

^rem-21-20

> [!remark]- Connections
> - The general construction in 493: the abelianization, the quotient by the commutator subgroup, [[§47 Commutators#^def-47-3|493 Def. §47.3]], which is abelian by [[§47 Commutators#^prop-47-6|493 Prop. §47.6]].
