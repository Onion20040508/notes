---
type: section
subject: "[[Group Theory]]"
chapter: 4
section: 16
tags: [group-theory, math493]
---
← [[§15 Homomorphisms]] · ↑ [[· 4 Homomorphisms and Isomorphisms]] · [[§17 Cyclic Groups]] →

*Reference: Pinter Ch. 9.*

> [!definition] Definition §16.1: Isomorphism; Isomorphic Groups
> A bijective group homomorphism is called an **isomorphism**, and two groups are called **isomorphic** if there is an isomorphism between them. We write $G \cong H$ if $G$ and $H$ are isomorphic.

^def-16-1

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^def-21-4|Isomorphism]] (590 §21.4).
> - Linear-algebra version: [[§10 Invertibility and Isomorphisms#^ladr-3-69|Isomorphism, isomorphic]] (LADR 3.69).
> - First met informally in 250: [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-5|250 Prop. §21.5]] (remainders and congruence classes have the same tables).

> [!theorem] Proposition §16.1: The Inverse of an Isomorphism Is an Isomorphism
> Let $\varphi: G \to H$ be a bijective group homomorphism. Then the inverse map $\varphi^{-1}: H \to G$ is also a group homomorphism (hence an isomorphism). Consequently the definition of isomorphism need not require anything of $\varphi^{-1}$.

^prop-16-1

> [!proof]+ Proof
> Let $h_1, h_2 \in H$ and put $g_i = \varphi^{-1}(h_i)$, so that $\varphi(g_i) = h_i$. Since $\varphi$ is a homomorphism, $\varphi(g_1 g_2) = \varphi(g_1)\varphi(g_2) = h_1 h_2$. Applying $\varphi^{-1}$ to both sides gives $g_1 g_2 = \varphi^{-1}(h_1 h_2)$, i.e. $\varphi^{-1}(h_1 h_2) = \varphi^{-1}(h_1)\,\varphi^{-1}(h_2)$.

^pf-16-1

*Uses:* [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^thm-21-5|Inverse of an Isomorphism is a Homomorphism]] (590 §21.5).

> [!remark] Remark: Contrast with Topology
> This is a genuinely algebraic phenomenon. “Preserves the operation” is an *equation* between elements, and a bijection transports equations in both directions. Continuity is not an equation, and a continuous bijection need not have a continuous inverse: $[0, 2\pi) \to S^1$, $t \mapsto e^{it}$, is a continuous bijection whose inverse is discontinuous at $1$ ([[§9 Continuous Functions#^def-9-2|590 notes]]). That is why a homeomorphism must be *defined* as a continuous bijection with continuous inverse, whereas a group isomorphism is simply a bijective homomorphism.

^rem-16-1

> [!remark]- Connections
> - MATH 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-5|Contrast with Topology]] (590 §21); the definition it contrasts with: [[§9 Continuous Functions#^def-9-2|Homeomorphism]] (590 §9.2).
> - When a continuous bijection *is* a homeomorphism: [[Bijection from Compact to Hausdorff is a Homeomorphism]] (here $[0, 2\pi)$ is not compact).

> [!theorem] Proposition §16.2: Composition; $\cong$ Is an Equivalence Relation
> 1. If $\varphi: G \to H$ and $\psi: H \to K$ are homomorphisms, then $\psi \circ \varphi: G \to K$ is a homomorphism. If both are isomorphisms, so is $\psi \circ \varphi$.
> 2. Isomorphism of groups is an equivalence relation: $G \cong G$; $G \cong H$ implies $H \cong G$; and $G \cong H$, $H \cong K$ imply $G \cong K$.

^prop-16-2

> [!proof]+ Proof
> (1) $\psi(\varphi(g_1 g_2)) = \psi(\varphi(g_1)\varphi(g_2)) = \psi(\varphi(g_1))\,\psi(\varphi(g_2))$, and a composition of bijections is a bijection. (2) Reflexivity: the identity map $G \to G$ is an isomorphism. Symmetry: [[§16 Isomorphisms#^prop-16-1|The Inverse of an Isomorphism Is an Isomorphism]]. Transitivity: part (1).

^pf-16-2

*Uses:* [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]], [[§16 Isomorphisms#^prop-16-1|§16.1]]

> [!remark] Remark: What Isomorphic Means
> An isomorphism $\varphi: G \to H$ is a relabeling of the elements of $G$ by elements of $H$ under which the multiplication table of $G$ becomes the multiplication table of $H$: if $g_1 g_2 = g_3$ in $G$, then $\varphi(g_1)\varphi(g_2) = \varphi(g_3)$ in $H$. Isomorphic groups are the same group with different names for the elements; any property expressible purely in terms of the group operation (being abelian, the number of elements $x$ with $x^2 = e$, the existence of an element of a given order, …) is shared by isomorphic groups. Such properties are therefore the tools for *proving* two groups are *not* isomorphic.

^rem-16-2

> [!definition] Definition §16.2: Commuting Elements
> For $g_1, g_2 \in G$, we say $g_1$ and $g_2$ **commute** if $g_1 g_2 = g_2 g_1$. A group is **commutative** (abelian) if all pairs of its elements commute. E.g. $\mathbb{Z}/6\mathbb{Z}$ is commutative; $S_3$ is not, since $(1\,2)(2\,3) = (1\,2\,3) \neq (1\,3\,2) = (2\,3)(1\,2)$.

^def-16-2

> [!theorem] Proposition §16.3: Two Isomorphism Invariants
> Let $\varphi: G \to H$ be an isomorphism.
> 1. If $G$ is commutative, then so is $H$.
> 2. If $g^2 = e_G$ for all $g \in G$, then $h^2 = e_H$ for all $h \in H$.
>
> Consequently: $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, and $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.
>
> *Source: WS 2.6*

^prop-16-3

> [!proof]+ Proof
> To prove two groups are *not* isomorphic, one shows no bijective homomorphism can exist; the method is to find a property preserved by isomorphisms that one group has and the other lacks.
>
> **(1)** Suppose $H$ is not commutative: there are $h_1, h_2 \in H$ with $h_1 h_2 \neq h_2 h_1$. Since $\varphi^{-1}$ is a homomorphism ([[§16 Isomorphisms#^prop-16-1|§16.1]]) and $G$ is commutative,
>
> $$
> \varphi^{-1}(h_1 h_2) = \varphi^{-1}(h_1)\,\varphi^{-1}(h_2) = \varphi^{-1}(h_2)\,\varphi^{-1}(h_1) = \varphi^{-1}(h_2 h_1).
> $$
>
> As $\varphi^{-1}$ is injective, $h_1 h_2 = h_2 h_1$, a contradiction.
>
> **(2)** Let $h \in H$ and set $g = \varphi^{-1}(h)$. Then $h^2 = \varphi(g)^2 = \varphi(g^2) = \varphi(e_G) = e_H$ (using $\varphi(e_G) = e_H$, [[§15 Homomorphisms#^prop-15-1|WS 2.9]]).
>
> **Consequences.** $\mathbb{Z}/6\mathbb{Z}$ is commutative and $S_3$ is not, so by (1) there is no isomorphism $\mathbb{Z}/6\mathbb{Z} \to S_3$ (nor $S_3 \to \mathbb{Z}/6\mathbb{Z}$, by symmetry of $\cong$, [[§16 Isomorphisms#^prop-16-2|§16.2]]). In $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ every element satisfies $g + g = (0, 0)$, while in $\mathbb{Z}/4\mathbb{Z}$, $1 + 1 = 2 \neq 0$; so by (2) they are not isomorphic.

^pf-16-3

*Uses:* [[§16 Isomorphisms#^prop-16-1|§16.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§16 Isomorphisms#^def-16-2|Def. §16.2]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^thm-21-6|Isomorphisms Preserve All Algebraic Properties]] (590 §21.6).

> [!theorem] Proposition §16.4: Homomorphisms and Orders of Elements
> Let $\varphi: G \to H$ be a homomorphism and $g \in G$.
> 1. $\varphi(g^k) = \varphi(g)^k$ for all $k \in \mathbb{Z}$.
> 2. If $g$ has finite order $n$, then $\varphi(g)^n = e_H$; hence $\varphi(g)$ has finite order, and its order divides $n$.
> 3. If $\varphi$ is injective (in particular, an isomorphism), then $\varphi(g)$ has the same order as $g$ (finite or infinite).

^prop-16-4

> [!proof]+ Proof
> **(1)** For $k \geq 0$ by induction: $\varphi(g^{k+1}) = \varphi(g^k g) = \varphi(g^k)\varphi(g) = \varphi(g)^{k+1}$. For $k < 0$, $\varphi(g^k) = \varphi((g^{-k})^{-1}) = \varphi(g^{-k})^{-1} = (\varphi(g)^{-k})^{-1} = \varphi(g)^k$, using [[§15 Homomorphisms#^prop-15-1|WS 2.9]].
>
> **(2)** $\varphi(g)^n = \varphi(g^n) = \varphi(e_G) = e_H$. Let $d$ be the order of $\varphi(g)$, so $d \leq n$. Write $n = qd + r$ with $0 \leq r < d$; then $e_H = \varphi(g)^n = (\varphi(g)^d)^q \varphi(g)^r = \varphi(g)^r$, and minimality of $d$ forces $r = 0$. So $d \mid n$.
>
> **(3)** By (1) and injectivity, $\varphi(g)^k = e_H = \varphi(e_G)$ iff $g^k = e_G$. So the set of $k \geq 1$ with $g^k = e_G$ equals the set of $k \geq 1$ with $\varphi(g)^k = e_H$; the least element (or the absence of one) is the same on both sides.

^pf-16-4

*Uses:* [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§4 Subgroups#^def-4-2|Def. §4.2]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!theorem] Proposition §16.5: Isomorphism Invariants
> Let $\varphi: G \to H$ be an isomorphism. Then:
> 1. $|G| = |H|$;
> 2. $G$ is abelian iff $H$ is abelian;
> 3. for each $n \geq 1$, $\varphi$ restricts to a bijection $\{g \in G : g^n = e_G\} \to \{h \in H : h^n = e_H\}$; in particular these sets have the same size;
> 4. for each $n$, $G$ and $H$ have the same number of elements of order $n$;
> 5. $G$ is cyclic iff $H$ is cyclic; more precisely, $G = \langle g \rangle$ iff $H = \langle \varphi(g) \rangle$.

^prop-16-5

> [!proof]+ Proof
> (1) $\varphi$ is a bijection. (2) [[§16 Isomorphisms#^prop-16-3|WS 2.6(1)]], applied to $\varphi$ and to $\varphi^{-1}$. (3) By [[§16 Isomorphisms#^prop-16-4|Homomorphisms and Orders of Elements]] (3) applied to $\varphi$ and to $\varphi^{-1}$, $g^n = e_G \iff \varphi(g)^n = e_H$, so $\varphi$ maps the first set into the second and $\varphi^{-1}$ maps the second into the first. (4) Same, since $\varphi$ preserves the order of each element. (5) If $G = \langle g \rangle$, every $h \in H$ is $h = \varphi(g^k) = \varphi(g)^k$ for some $k$, so $H = \langle \varphi(g) \rangle$; conversely apply $\varphi^{-1}$.

^pf-16-5

*Uses:* [[§16 Isomorphisms#^prop-16-3|§16.3]], [[§16 Isomorphisms#^prop-16-4|§16.4]], [[§16 Isomorphisms#^prop-16-1|§16.1]], [[§4 Subgroups#^def-4-3|Def. §4.3]], [[§4 Subgroups#^def-4-5|Def. §4.5]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^thm-21-6|Isomorphisms Preserve All Algebraic Properties]] (590 §21.6).

> [!remark] Remark: Using Invariants
> To prove $G \not\cong H$, exhibit one of these quantities on which they differ. [[§16 Isomorphisms#^prop-16-3|WS 2.6]] used (2) and (3) with $n = 2$; [[§16 Isomorphisms#^prop-16-8|WS 2.7(1)]] used (3) with $n = 2$, or equivalently (5). Any property expressible purely in terms of the group operation is preserved in this way, by the same mechanism: transport the property through $\varphi$ or $\varphi^{-1}$ using the homomorphism identity. Conversely, matching invariants never *prove* isomorphism; for that one must construct the map, as in [[§16 Isomorphisms#^prop-16-7|WS 2.5]], [[§16 Isomorphisms#^prop-16-8|2.7(2)]], [[§16 Isomorphisms#^prop-16-9|2.8]].

^rem-16-3

> [!theorem] Proposition §16.6: Further Isomorphism Invariants
> Let $\varphi: G \to H$ be an isomorphism.
> 1. If $z$ is central in $G$, then $\varphi(z)$ is central in $H$; consequently $\varphi(Z(G)) = Z(H)$ and $|Z(G)| = |Z(H)|$.
> 2. If $G$ has a subgroup $G'$ with $G' \neq \{e_G\}$ and $G' \neq G$, then $H$ has a subgroup $H'$ with $H' \neq \{e_H\}$ and $H' \neq H$. More generally $G' \mapsto \varphi(G')$ is a bijection between the subgroups of $G$ and the subgroups of $H$, preserving inclusions and orders.
>
> *Source: PS 2.2*

^prop-16-6

> [!proof]+ Proof
> **(1)** Let $h \in H$. As $\varphi$ is surjective, $h = \varphi(g)$ for some $g \in G$, and then
>
> $$
> \varphi(z)h = \varphi(z)\varphi(g) = \varphi(zg) = \varphi(gz) = \varphi(g)\varphi(z) = h\varphi(z),
> $$
>
> using the homomorphism property twice and centrality of $z$. So $\varphi(z) \in Z(H)$, i.e. $\varphi(Z(G)) \subseteq Z(H)$; applying the same to $\varphi^{-1}$ (an isomorphism, [[§16 Isomorphisms#^prop-16-1|§16.1]]) gives $\varphi^{-1}(Z(H)) \subseteq Z(G)$, whence equality.
>
> **(2)** Put $H' = \varphi(G')$, a subgroup of $H$ by [[§15 Homomorphisms#^prop-15-4|Images and Preimages of Subgroups]] (§15.4). If $g' \in G'$ with $g' \neq e_G$, then $\varphi(g') \neq \varphi(e_G) = e_H$ by injectivity, so $H' \neq \{e_H\}$. If $g \in G \setminus G'$, then $\varphi(g) \notin H'$: otherwise $\varphi(g) = \varphi(g')$ for some $g' \in G'$, and injectivity would give $g = g' \in G'$. So $H' \neq H$. The general statement follows from part (3) of [[§15 Homomorphisms#^prop-15-4|Images and Preimages of Subgroups]] (§15.4) applied to $\varphi$ and $\varphi^{-1}$; orders are preserved since $\varphi$ is a bijection, and inclusions since $\varphi$ is a map of sets.

^pf-16-6

*Uses:* [[§35 The Center#^def-35-1|Def. §35.1]], [[§16 Isomorphisms#^prop-16-1|§16.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§15 Homomorphisms#^prop-15-4|§15.4]]

> [!remark] Remark: Using These to Distinguish Groups
> Both give non-isomorphism tests. For instance $|Z(\mathbb{Z}/6\mathbb{Z})| = 6$ while $|Z(S_3)| = 1$ ([[§35 The Center#^def-35-1|§35]]), re-proving $\mathbb{Z}/6\mathbb{Z} \not\cong S_3$ without invoking commutativity directly. And since the subgroup lattices correspond, a group with no proper nontrivial subgroup cannot be isomorphic to one that has such a subgroup: $\mathbb{Z}/4\mathbb{Z}$ has the subgroup $\{[0],[2]\}$ and $U_8$ has $\{1,3\}$, whereas $\mathbb{Z}/5\mathbb{Z}$, of prime order, has none ([[§29 The Index and Lagrange's Theorem#^cor-29-8|§29.8]]).

^rem-16-4

> [!theorem] Proposition §16.7: $\mathbb{Z}/4\mathbb{Z} \cong U_5$
> The map $\varphi: \mathbb{Z}/4\mathbb{Z} \to (\mathbb{Z}/5\mathbb{Z})^\times$, $\ k \mapsto 2^k$, is an isomorphism. Explicitly,
>
> $$
> 0 \mapsto 1, \qquad 1 \mapsto 2, \qquad 2 \mapsto 4, \qquad 3 \mapsto 8 \equiv 3 \pmod 5.
> $$
>
> *Source: WS 2.5*

^prop-16-7

> [!proof]+ Proof
> To show two groups are isomorphic one must exhibit a bijection $\varphi$ with $\varphi(gh) = \varphi(g)\varphi(h)$.
>
> **Well-defined.** The formula uses a representative $k \in \mathbb{Z}$ of a class in $\mathbb{Z}/4\mathbb{Z}$. Since $2^4 = 16 \equiv 1 \pmod 5$, if $k' = k + 4m$ then $2^{k'} = 2^k (2^4)^m \equiv 2^k \pmod 5$, so $\varphi$ depends only on the class of $k$. Also $2^k$ is coprime to $5$, so the values lie in $U_5$.
>
> **Homomorphism.** $\varphi(k + l) = 2^{k+l} = 2^k \cdot 2^l = \varphi(k)\varphi(l)$, by the [[§4 Subgroups#^lem-4-4|Exponent Laws]]. Note the operation on the left is addition modulo $4$ and on the right multiplication modulo $5$.
>
> **Bijective.** The four values $1, 2, 4, 3$ listed above are distinct and exhaust $U_5 = \{1, 2, 3, 4\}$.

^pf-16-7

*Uses:* [[§7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - An instance of the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]] (§17.1): see [[§17 Cyclic Groups#^rem-17-1|Remark §17.1]].

> [!remark] Remark: Reading the Isomorphism off the Tables
> Relabel the $\mathbb{Z}/4\mathbb{Z}$ table by $0 \to 1$, $1 \to 2$, $2 \to 4$, $3 \to 3$ and reorder rows and columns to $1, 2, 3, 4$; the result is the $U_5$ table. One spot check: $1 + 3 = 0$ in $\mathbb{Z}/4\mathbb{Z}$ corresponds to $2 \cdot 3 = 6 \equiv 1$ in $U_5$. The isomorphism turns multiplication modulo $5$ into addition of exponents modulo $4$ — a finite version of the logarithm, and the reason $U_5$ “looks like” a cyclic group: it is generated by $2$.

^rem-16-5

> [!theorem] Proposition §16.8: $U_8$ and $U_7$
> 1. $(\mathbb{Z}/8\mathbb{Z})^\times \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, and hence $(\mathbb{Z}/8\mathbb{Z})^\times \not\cong \mathbb{Z}/4\mathbb{Z}$.
> 2. $(\mathbb{Z}/7\mathbb{Z})^\times \cong \mathbb{Z}/6\mathbb{Z}$, via $k \mapsto 3^k$.
>
> *Source: WS 2.7*

^prop-16-8

> [!proof]+ Proof
> **(1)** In $U_8 = \{1, 3, 5, 7\}$ every element squares to $1$ ([[§14 Multiplication Tables#^ex-14-4|WS 2.3]]). Define $\varphi: U_8 \to \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ by
>
> $$
> 1 \mapsto (0,0), \quad 3 \mapsto (1,0), \quad 5 \mapsto (0,1), \quad 7 \mapsto (1,1).
> $$
>
> This is a bijection. It is a homomorphism: products involving $1$ are trivially respected; $3 \cdot 5 = 15 \equiv 7$ and $(1,0)+(0,1) = (1,1)$; $3 \cdot 7 = 21 \equiv 5$ and $(1,0)+(1,1) = (0,1)$; $5 \cdot 7 = 35 \equiv 3$ and $(0,1)+(1,1) = (1,0)$; and each $x \cdot x = 1$ matches $v + v = (0,0)$. Since both groups are abelian, checking each unordered pair suffices. So $U_8 \cong \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$, and since $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z} \not\cong \mathbb{Z}/4\mathbb{Z}$ ([[§16 Isomorphisms#^prop-16-3|WS 2.6]]) and $\cong$ is transitive ([[§16 Isomorphisms#^prop-16-2|§16.2]]), $U_8 \not\cong \mathbb{Z}/4\mathbb{Z}$. (Directly: every element of $U_8$ squares to $1$, and $1 + 1 \neq 0$ in $\mathbb{Z}/4\mathbb{Z}$.)
>
> **(2)** The powers of $3$ modulo $7$ are
>
> $$
> 3^0 = 1, \quad 3^1 = 3, \quad 3^2 = 9 \equiv 2, \quad 3^3 = 6, \quad 3^4 = 18 \equiv 4, \quad 3^5 = 12 \equiv 5, \quad 3^6 = 15 \equiv 1,
> $$
>
> which exhaust $U_7 = \{1, \ldots, 6\}$. So $U_7 = \langle 3 \rangle$ is cyclic of order $6$. The map $\varphi: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 3^k$, is well-defined since $3^6 \equiv 1$ (if $k' = k + 6m$ then $3^{k'} = 3^k (3^6)^m \equiv 3^k$), is a homomorphism since $3^{k+l} = 3^k 3^l$, and is a bijection by the list above. Exactly as in [[§16 Isomorphisms#^prop-16-7|WS 2.5]] with $2$ replaced by $3$ and $5$ by $7$.

^pf-16-8

*Uses:* [[§14 Multiplication Tables#^ex-14-4|Ex. §14.4]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§16 Isomorphisms#^prop-16-3|§16.3]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§16 Isomorphisms#^prop-16-7|§16.7]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - Part (2) as an instance of the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]] (§17.1), and why $U_8$ is not cyclic: [[§17 Cyclic Groups#^rem-17-1|Remark §17.1]].

> [!remark] Remark: Reading Cyclicity off a Table
> Both questions reduce to: does the unit group have a generator? In the $U_7$ table ([[§14 Multiplication Tables#^ex-14-3|WS 2.2]]), the row of $3$ read as successive powers cycles through all six elements; in the $U_8$ table, every row returns to $1$ after two steps, so no element generates. A group of order $4$ in which every element squares to the identity cannot be cyclic; a group of order $n$ with an element whose powers exhaust it is $\cong \mathbb{Z}/n\mathbb{Z}$ by the argument of (2), which is made general in the [[§17 Cyclic Groups#^thm-17-1|Classification of Cyclic Groups]] (§17.1).

^rem-16-6

![[m493-16-1.svg]]
*Colour-coded tables. Listing $U_5$ in the order $2^0, 2^1, 2^2, 2^3$ reproduces the colour pattern of $\mathbb{Z}/4\mathbb{Z}$ ([[§16 Isomorphisms#^prop-16-7|WS 2.5]]: $\mathbb{Z}/4\mathbb{Z} \cong U_5$). No ordering of $U_8$ can: its diagonal (outlined in red) is constantly the identity, so every element squares to $1$ ([[§16 Isomorphisms#^prop-16-8|WS 2.7]]).*

> [!theorem] Proposition §16.9: Structure of $\mathbb{R}^\times$ and $\mathbb{Q}^\times$
> 1. $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \mathbb{Z}/2\mathbb{Z}$, where $\mathbb{R}_{>0}$ is the positive reals under multiplication.
> 2. $\mathbb{Q}^\times \cong \mathbb{Z}^{\oplus\infty} \times \mathbb{Z}/2\mathbb{Z}$, where $\mathbb{Z}^{\oplus\infty}$ is the group of integer sequences $(a_1, a_2, \ldots)$ with only finitely many nonzero terms, under componentwise addition.
>
> *Source: WS 2.8*

^prop-16-9

> [!proof]+ Proof
> **(1)** Define $\varphi(x) = (|x|, s(x))$, where $s(x) = [0]$ if $x > 0$ and $s(x) = [1]$ if $x < 0$. Homomorphism: $|xy| = |x||y|$, and the sign of a product is the product of signs, which in $\mathbb{Z}/2\mathbb{Z}$ reads $s(xy) = s(x) + s(y)$ (negative times negative is positive: $[1] + [1] = [0]$). Bijective: the inverse map is $(r, [0]) \mapsto r$, $(r, [1]) \mapsto -r$, which is well-defined since $r > 0$ and $-r < 0$ are distinct and every nonzero real is exactly one of these.
>
> **(2)** Let $p_1 = 2, p_2 = 3, p_3 = 5, \ldots$ be the primes. By [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|unique factorization]] (extended to negative exponents by clearing denominators), every $q \in \mathbb{Q}^\times$ has a unique expression
>
> $$
> q = \pm\, p_1^{a_1} p_2^{a_2} p_3^{a_3} \cdots, \qquad a_i \in \mathbb{Z}, \text{ almost all } 0.
> $$
>
> Define $\varphi(q) = \big((a_1, a_2, \ldots),\, s(q)\big)$ with $s$ the sign class as in (1). Homomorphism: multiplying rationals adds exponents prime by prime and multiplies signs, i.e. adds sign classes. Injective: uniqueness of the factorization. Surjective: any finitely supported exponent sequence and sign defines a rational. Hence $\varphi$ is an isomorphism.

^pf-16-9

*Uses:* [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark] Remark: Interpretation
> Both isomorphisms split a multiplicative group into “size” and “sign.” In (2), the size part says that, as a group, the positive rationals are freely generated by the primes: $\mathbb{Q}_{>0} \cong \mathbb{Z}^{\oplus\infty}$ is the group-theoretic content of the [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|Fundamental Theorem of Arithmetic]].

^rem-16-7
