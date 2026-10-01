---
type: section
subject: "[[Group Theory]]"
chapter: 4
section: 18
tags: [group-theory, math493]
---
← [[§17 Cyclic Groups]] · ↑ [[· 4 Homomorphisms and Isomorphisms]] · [[§19 Polynomial Rings, Permutation Matrices, and Representations]] →

*Reference: Pinter Ch. 4, Ex. G (direct products); Ch. 13, Ex. I (conjugate elements).*

> [!definition] Definition §18.1: Automorphisms; $\operatorname{Aut}(G)$
> An **automorphism** of a group $G$ is an isomorphism $G \to G$. The set of all automorphisms is written $\operatorname{Aut}(G)$; it is a group under composition (compositions and inverses of isomorphisms are isomorphisms, and $\operatorname{id}_G$ is the identity), a subgroup of $S_G$.

^def-18-1

*Uses:* [[§16 Isomorphisms#^prop-16-1|§16.1]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!definition] Definition §18.2: Conjugation; Conjugate Elements; Inner Automorphism
> Let $G$ be a group and $a \in G$. **Conjugation by $a$** is the map $c_a: G \to G$, $c_a(g) = aga^{-1}$. Elements $g, g' \in G$ are **conjugate** if $g' = aga^{-1}$ for some $a \in G$. The maps $c_a$ are automorphisms of $G$ ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Conjugation Is an Automorphism]], next); they are called the **inner automorphisms** of $G$.

^def-18-2

> [!remark]- Connections
> - The classes of conjugate elements: [[§31 Conjugacy Classes#^def-31-1|Conjugacy Class]] (§31.1).

> [!theorem] Proposition §18.1: Conjugation Is an Automorphism
> Let $G$ be a group and $a \in G$. Let $c_a: G \to G$, $c_a(g) = a g a^{-1}$, be conjugation by $a$.
> 1. $c_a$ is a group homomorphism.
> 2. $c_a$ is an automorphism of $G$, with inverse $c_{a^{-1}}$.
> 3. $c_a \circ c_b = c_{ab}$ for all $a, b \in G$; hence $a \mapsto c_a$ is a group homomorphism $G \to \operatorname{Aut}(G)$. Its image consists of the inner automorphisms of $G$.
>
> *Source: PS 1.2*

^prop-18-1

> [!proof]+ Proof
> **(1)** For $g, h \in G$,
>
> $$
> c_a(gh) = a (gh) a^{-1} = a g (a^{-1} a) h a^{-1} = (a g a^{-1})(a h a^{-1}) = c_a(g)\, c_a(h),
> $$
>
> inserting $e = a^{-1}a$ between $g$ and $h$ and regrouping by associativity. No reordering of factors occurs, so commutativity is not needed.
>
> **(2)** $c_{a^{-1}}(c_a(g)) = a^{-1}(a g a^{-1}) a = g$ and $c_a(c_{a^{-1}}(g)) = a(a^{-1} g a)a^{-1} = g$, so $c_{a^{-1}}$ is a two-sided inverse of $c_a$; thus $c_a$ is a bijective homomorphism.
>
> **(3)** $c_a(c_b(g)) = a (b g b^{-1}) a^{-1} = (ab)\, g\, (b^{-1} a^{-1}) = (ab)\, g\, (ab)^{-1} = c_{ab}(g)$, using $(ab)^{-1} = b^{-1}a^{-1}$. So $a \mapsto c_a$ respects the operations (composition in $\operatorname{Aut}(G)$, multiplication in $G$).

^pf-18-1

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Def. §18.2]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]], [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|Def. §18.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!remark]- Connections
> - Conjugation as an action of $G$ on itself: [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|The Conjugation Action]] (§32.1).

> [!remark] Remark: Earlier Occurrences of Conjugation
> Conjugation is the operation behind the mixed hypothesis of [[§2 First Consequences of the Axioms#^prop-2-1|WS 1.1]] ($g h_1 = h_2 g$ says $h_2 = c_g(h_1)$) and behind the [[§12 Multiplying and Conjugating Cycles#^prop-12-1|relabeling of cycles]] in $S_n$ ($\sigma\,(a_1 \cdots a_r)\,\sigma^{-1} = (\sigma(a_1) \cdots \sigma(a_r))$, which is $c_\sigma$ applied to a cycle). In an abelian group every $c_a$ is the identity; the extent to which $c_a \neq \operatorname{id}$ measures non-commutativity.

^rem-18-1

> [!definition] Definition §18.3: $\operatorname{Hom}(G, H)$; Pointwise Product
> For groups $G$ and $H$, let $\operatorname{Hom}(G, H)$ denote the set of all group homomorphisms $G \to H$. For $\alpha, \beta \in \operatorname{Hom}(G, H)$, the **pointwise product** $\alpha\beta: G \to H$ is defined by $(\alpha\beta)(g) = \alpha(g)\,\beta(g)$, the product taken in $H$.

^def-18-3

> [!remark]- Connections
> - Linear-algebra analogue: [[3A Vector Space of Linear Maps#^ladr-3-5|Addition and scalar multiplication on L(V, W)]] (LADR 3.5), the pointwise sum of linear maps.

> [!theorem] Proposition §18.2: Pointwise Products of Homomorphisms
> Let $G$ and $H$ be groups.
> 1. If $H$ is abelian, then the pointwise product of two homomorphisms $G \to H$ is a homomorphism. In fact $\operatorname{Hom}(G, H)$ is then an abelian group under pointwise product, with identity the trivial homomorphism $g \mapsto e_H$ and inverse $\alpha^{-1}: g \mapsto \alpha(g)^{-1}$.
> 2. Conversely, if $H$ is not abelian, then pointwise products can fail to be homomorphisms: the pointwise product of $\operatorname{id}_H$ with itself, $g \mapsto g^2$, is not a homomorphism.
>
> *Source: PS 1.3*

^prop-18-2

> [!proof]+ Proof
> **(1)** Let $\alpha, \beta \in \operatorname{Hom}(G, H)$ and $a, b \in G$. Then
>
> $$
> (\alpha\beta)(ab) = \alpha(ab)\,\beta(ab) = \alpha(a)\alpha(b)\beta(a)\beta(b) = \alpha(a)\beta(a)\alpha(b)\beta(b) = (\alpha\beta)(a)\,(\alpha\beta)(b),
> $$
>
> using that $\alpha, \beta$ are homomorphisms and, in the third equality, commutativity of $H$ to swap the adjacent factors $\alpha(b)\beta(a)$. So $\alpha\beta \in \operatorname{Hom}(G, H)$. The trivial map $g \mapsto e_H$ is a homomorphism ($e_H = e_H e_H$) and is an identity for the pointwise product. For $\alpha \in \operatorname{Hom}(G,H)$, the map $g \mapsto \alpha(g)^{-1}$ is a homomorphism: $\alpha(ab)^{-1} = (\alpha(a)\alpha(b))^{-1} = \alpha(b)^{-1}\alpha(a)^{-1} = \alpha(a)^{-1}\alpha(b)^{-1}$, again by commutativity of $H$; and it is a pointwise inverse of $\alpha$. Associativity and commutativity of the pointwise product are inherited from $H$, value by value.
>
> **(2)** The identity map is a homomorphism, so $\operatorname{id}\cdot\operatorname{id}: g \mapsto g^2$ is a pointwise product of homomorphisms. If it were a homomorphism, then for all $a, b \in H$, $(ab)^2 = a^2 b^2$, i.e. $abab = aabb$; cancelling $a$ on the left and $b$ on the right gives $ba = ab$, so $H$ would be abelian. Concretely, in $S_3$ with $a = (1\,2)$, $b = (2\,3)$: $(ab)^2 = (1\,2\,3)^2 = (1\,3\,2)$, while $a^2 b^2 = e$.

^pf-18-2

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^def-18-3|Def. §18.3]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§14 Multiplication Tables#^ex-14-5|Ex. §14.5]]

> [!definition] Definition §18.4: Structure Maps of a Product
> For groups $G$ and $H$, the **projections** $\pi_1: G \times H \to G$, $\pi_1(g, h) = g$, and $\pi_2: G \times H \to H$, $\pi_2(g, h) = h$; the **inclusions** $\iota_1: G \to G \times H$, $\iota_1(g) = (g, e_H)$, and $\iota_2: H \to G \times H$, $\iota_2(h) = (e_G, h)$; and, for a single group $G$, the **diagonal** $\Delta: G \to G \times G$, $\Delta(g) = (g, g)$, and the **multiplication map** $\nabla: G \times G \to G$, $\nabla(g, h) = gh$.

^def-18-4

> [!theorem] Proposition §18.3: The Product and Its Universal Property
> Let $G$, $H$, $K$ be groups.
> 1. $G \times H$ with componentwise operation is a group ([[§3 Basic Examples of Groups#^def-3-2|Definition in §3]]); its identity is $(e_G, e_H)$ and $(g, h)^{-1} = (g^{-1}, h^{-1})$. It is abelian if and only if both $G$ and $H$ are.
> 2. $\pi_1$ and $\pi_2$ are surjective homomorphisms; $\iota_1$ and $\iota_2$ are injective homomorphisms.
> 3. A map $\varphi: K \to G \times H$ is a homomorphism if and only if both components $\pi_1 \circ \varphi: K \to G$ and $\pi_2 \circ \varphi: K \to H$ are homomorphisms.
> 4. The diagonal $\Delta: G \to G \times G$ is an injective homomorphism; its image $\{(g, g) : g \in G\}$ is a subgroup of $G \times G$ isomorphic to $G$.
>
> *Source: PS 1.4(1)–(2)*

^prop-18-3

> [!proof]+ Proof
> **(1)** Associativity: $((g_1,h_1)(g_2,h_2))(g_3,h_3) = ((g_1g_2)g_3, (h_1h_2)h_3) = (g_1(g_2g_3), h_1(h_2h_3)) = (g_1,h_1)((g_2,h_2)(g_3,h_3))$, by associativity in each component. Identity: $(e_G,e_H)(g,h) = (g,h) = (g,h)(e_G,e_H)$. Inverses: $(g,h)(g^{-1},h^{-1}) = (e_G,e_H) = (g^{-1},h^{-1})(g,h)$. If $G, H$ are abelian, $(g,h)(g',h') = (gg', hh') = (g'g, h'h) = (g',h')(g,h)$; conversely if, say, $gg' \neq g'g$ in $G$, then $(g, e_H)(g', e_H) \neq (g', e_H)(g, e_H)$.
>
> **(2)** $\pi_1((g_1,h_1)(g_2,h_2)) = \pi_1(g_1g_2, h_1h_2) = g_1g_2 = \pi_1(g_1,h_1)\pi_1(g_2,h_2)$; surjective since $\pi_1(g, e_H) = g$. Similarly for $\pi_2$. $\iota_1(g_1g_2) = (g_1g_2, e_H) = (g_1,e_H)(g_2,e_H) = \iota_1(g_1)\iota_1(g_2)$; injective since $\iota_1(g) = \iota_1(g')$ forces $g = g'$. Similarly for $\iota_2$.
>
> **(3)** Write $\varphi(k) = (\varphi_1(k), \varphi_2(k))$, so $\varphi_i = \pi_i \circ \varphi$. Then $\varphi(k k') = (\varphi_1(kk'), \varphi_2(kk'))$ and $\varphi(k)\varphi(k') = (\varphi_1(k)\varphi_1(k'), \varphi_2(k)\varphi_2(k'))$. Two pairs are equal iff both components agree, so $\varphi(kk') = \varphi(k)\varphi(k')$ for all $k, k'$ iff $\varphi_1(kk') = \varphi_1(k)\varphi_1(k')$ and $\varphi_2(kk') = \varphi_2(k)\varphi_2(k')$ for all $k, k'$.
>
> **(4)** $\Delta = (\operatorname{id}_G, \operatorname{id}_G)$ has both components homomorphisms, so $\Delta$ is a homomorphism by (3); directly, $\Delta(gh) = (gh, gh) = (g,g)(h,h) = \Delta(g)\Delta(h)$. It is injective since $\pi_1 \circ \Delta = \operatorname{id}_G$. Its image is a subgroup ([[§15 Homomorphisms#^prop-15-2|WS 2.10(1)]], or directly: closed under products and inverses, contains $(1,1)$), and $\Delta$ restricted to its image is a bijective homomorphism $G \to \operatorname{Im}(\Delta)$.

^pf-18-3

*Uses:* [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]], [[§1 The Definition of a Group#^def-1-2|Def. §1.2]], [[§18 Conjugation, Products, and Pointwise Products#^def-18-4|Def. §18.4]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

![[m493-18-1.svg]]
*Part (3) of the proposition: a map $\varphi: K \to G \times H$ (red) is a homomorphism exactly when its components $\pi_1 \circ \varphi$ and $\pi_2 \circ \varphi$ are. A homomorphism into a product is therefore the same thing as a pair of homomorphisms, one into each factor; the diagonal $\Delta = (\operatorname{id}_G, \operatorname{id}_G)$ of part (4) is the case $K = G = H$.*

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^def-21-5|Direct Product of Groups]] (590 §21.5).
> - Linear-algebra version: [[3E Products and Quotients of Vector Spaces#^ladr-3-87|Product of vector spaces]] (LADR 3.87).

> [!theorem] Proposition §18.4: Characterizations of Abelian Groups
> For a group $G$, the following are equivalent:
> 1. $G$ is abelian;
> 2. the multiplication map $\nabla: G \times G \to G$, $(g, h) \mapsto gh$, is a homomorphism;
> 3. the inversion map $G \to G$, $g \mapsto g^{-1}$, is a homomorphism;
> 4. the squaring map $G \to G$, $g \mapsto g^2$, is a homomorphism.
>
> *Source: PS 1.4(3)*

^prop-18-4

> [!proof]+ Proof
> **(1) $\Rightarrow$ (2):** $\nabla = \pi_1 \cdot \pi_2$ is the pointwise product of the two projections (homomorphisms into $G$), hence a homomorphism when $G$ is abelian, by the [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|Pointwise Products proposition]].
>
> **(2) $\Rightarrow$ (1):** Let $g, h \in G$ and evaluate the homomorphism condition at the pair $(g, h), (g, h) \in G \times G$:
>
> $$
> \nabla\big((g,h)(g,h)\big) = \nabla(g^2, h^2) = g^2 h^2, \qquad \nabla(g,h)\,\nabla(g,h) = (gh)^2 = ghgh.
> $$
>
> If these agree, $gghh = ghgh$; cancelling $g$ on the left and $h$ on the right yields $gh = hg$. Since $g, h$ were arbitrary, $G$ is abelian.
>
> **(1) $\Leftrightarrow$ (3):** Inversion is a homomorphism iff $(gh)^{-1} = g^{-1} h^{-1}$ for all $g, h$. Since always $(gh)^{-1} = h^{-1} g^{-1}$, this says $h^{-1} g^{-1} = g^{-1} h^{-1}$ for all $g, h$; as $g, h$ range over $G$ so do $g^{-1}, h^{-1}$, so this is precisely commutativity.
>
> **(1) $\Leftrightarrow$ (4):** Squaring is a homomorphism iff $(gh)^2 = g^2 h^2$ for all $g, h$, i.e. $ghgh = gghh$, which after cancellation is $hg = gh$.
>
> **Concrete failure of (2)–(4) in $S_3$:** with $g = (1\,2)$, $h = (2\,3)$: $gh = (1\,2\,3)$, so $(gh)^2 = (1\,3\,2)$ and $(gh)^{-1} = (1\,3\,2)$, while $g^2h^2 = e$ and $g^{-1}h^{-1} = gh = (1\,2\,3)$.

^pf-18-4

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^def-18-4|Def. §18.4]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|§18.2]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§14 Multiplication Tables#^ex-14-5|Ex. §14.5]]

> [!remark]- Connections
> - Worksheet form: [[§18 Conjugation, Products, and Pointwise Products#^prop-18-5|Characterizations of Abelian Groups, Worksheet Form (WS 3.4)]] (§18.5).

> [!remark] Remark: Relation between PS 1.3(2) and PS 1.4(3)
> Since $\nabla = \pi_1 \cdot \pi_2$, the failure of $\nabla$ to be a homomorphism for non-abelian $G$ is a special case of the failure of pointwise products in [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|PS 1.3(2)]]; and evaluating $\nabla$ at the pairs $(g,h), (g,h)$ reduces it to the condition $(gh)^2 = g^2 h^2$, which is the squaring map of [[§18 Conjugation, Products, and Pointwise Products#^prop-18-2|PS 1.3(2)]]. Both problems reduce to the same computation: $ghgh = gghh$ if and only if $gh = hg$.

^rem-18-2

Worksheet 3 restates the definition of an abelian group ($g_1 * g_2 = g_2 * g_1$ for all $g_1, g_2$; the definition in [[§1 The Definition of a Group#^def-1-2|§1.2]]) together with the convention that $+$ and $0$ are used only for abelian groups ([[§1 The Definition of a Group#^rem-1-1|§1, Notation]]). Its WS 3.4 is the characterization already proved in [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]] from the problem set:

> [!theorem] Proposition §18.5: Characterizations of Abelian Groups, Worksheet Form
> Let $G$ be a group. Then $G$ is abelian if and only if each of the following holds (and each is equivalent to abelian-ness on its own):
> 1. the map $g \mapsto g^{-1}$ is a group homomorphism;
> 2. the map $g \mapsto g^2$ is a group homomorphism;
> 3. the map $\mu: G \times G \to G$, $\mu(g, h) = g * h$, is a group homomorphism.
>
> *Source: WS 3.4*

^prop-18-5

> [!proof]+ Proof
> This is the proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|Characterizations of Abelian Groups]] in §18 (with $\mu = \nabla$), proved there. In brief: (1) inversion is a homomorphism iff $(gh)^{-1} = g^{-1}h^{-1}$, i.e. $h^{-1}g^{-1} = g^{-1}h^{-1}$ for all $g, h$, which is commutativity; (2) squaring is a homomorphism iff $ghgh = gghh$, which after cancellation is $hg = gh$; (3) $\mu$ is a homomorphism iff $\mu((g,h)(g',h')) = gg'hh'$ equals $\mu(g,h)\mu(g',h') = ghg'h'$ for all $g, h, g', h'$; taking $g = e, h' = e$ gives $g'h = hg'$, and conversely commutativity gives the equality directly.

^pf-18-5

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|§18.4]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!remark]- Connections
> - Problem-set form, with the full proof: [[§18 Conjugation, Products, and Pointwise Products#^prop-18-4|Characterizations of Abelian Groups (PS 1.4(3))]] (§18.4).
