---
type: section
subject: "[[Group Theory]]"
chapter: 4
section: 15
tags: [group-theory, math493]
---
← [[§14 Multiplication Tables]] · ↑ [[· 4 Homomorphisms and Isomorphisms]] · [[§16 Isomorphisms]] →

*Reference: Pinter Ch. 14.*

> [!definition] Definition §15.1: Group Homomorphism
> Given two groups $G$ and $H$, a **group homomorphism** is a map $\varphi: G \to H$ obeying
>
> $$
> \varphi(g_1 * g_2) = \varphi(g_1) * \varphi(g_2) \qquad \text{for all } g_1, g_2 \in G,
> $$
>
> where the $*$ on the left is the operation of $G$ and the $*$ on the right is the operation of $H$.

^def-15-1

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^def-21-3|Homomorphism]] (590 §21.3).
> - Linear-algebra analogue: [[§7 Vector Space of Linear Maps#^ladr-3-1|Linear map]] (LADR 3.1).

> [!theorem] Proposition §15.1: Homomorphisms Preserve Identity and Inverses
> Let $\varphi: G \to H$ be a group homomorphism. Then $\varphi(e_G) = e_H$, and $\varphi(g^{-1}) = \varphi(g)^{-1}$ for all $g \in G$.
>
> *Source: WS 2.9*

^prop-15-1

> [!proof]+ Proof
> $\varphi(e_G) = \varphi(e_G \cdot e_G) = \varphi(e_G)\varphi(e_G)$; cancelling $\varphi(e_G)$ in $H$ ([[§2 First Consequences of the Axioms#^prop-2-1|Cancellation]], §2) gives $\varphi(e_G) = e_H$. Then $\varphi(g)\varphi(g^{-1}) = \varphi(g g^{-1}) = \varphi(e_G) = e_H$, so $\varphi(g^{-1})$ is a one-sided, hence two-sided, inverse of $\varphi(g)$ ([[§2 First Consequences of the Axioms#^prop-2-6|One-Sided Inverses Suffice]], §2).

^pf-15-1

*Uses:* [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[§2 First Consequences of the Axioms#^prop-2-6|§2.6]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^thm-21-3|Homomorphisms Preserve Identity and Inverses]] (590 §21.3).
> - Linear-algebra version of the first half: [[§7 Vector Space of Linear Maps#^ladr-3-10|Linear maps take 0 to 0]] (LADR 3.10).

> [!definition] Definition §15.2: Image and Kernel
> Let $\varphi: G \to H$ be a group homomorphism. The **image** of $\varphi$ is
>
> $$
> \operatorname{Im}(\varphi) := \{ \varphi(g) : g \in G \} \subseteq H,
> $$
>
> and the **kernel** of $\varphi$ is
>
> $$
> \operatorname{Ker}(\varphi) := \{ g \in G : \varphi(g) = e_H \} \subseteq G.
> $$

^def-15-2

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^def-21-6|Kernel and Image]] (590 §21.6).
> - Linear-algebra versions: [[§8 Null Spaces and Ranges#^ladr-3-11|Null space]] (LADR 3.11) and [[§8 Null Spaces and Ranges#^ladr-3-16|Range]] (LADR 3.16).
> - Computational version for linear maps: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-5|235 Def. §24.5]] (kernel and range), computed as Nul A and Col A.

> [!example] Example §15.1: Homomorphisms and Their Kernels
> 1. $\det: GL_n(\mathbb{R}) \to \mathbb{R}^\times$ is a homomorphism, since $\det(AB) = \det A \det B$ ([[§34 Determinants#^ladr-9-49|LADR 9.49]]). Kernel: $SL_n(\mathbb{R}) = \{A : \det A = 1\}$. Image: all of $\mathbb{R}^\times$ (use $\operatorname{diag}(\lambda, 1, \ldots, 1)$).
> 2. Reduction $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $x \mapsto [x]$, is a homomorphism: $[x + y] = [x] + [y]$ is the definition of addition on classes ([[§7 The Group ℤ∕nℤ#^def-7-1|Def. §7.1]]). Kernel: $n\mathbb{Z}$. Image: everything.
> 3. $\mathbb{R}^\times \to \mathbb{R}_{>0}$, $x \mapsto |x|$, is a homomorphism since $|xy| = |x||y|$. Kernel: $\{\pm 1\}$.
> 4. $(\mathbb{R}, +) \to \mathbb{R}^\times$, $x \mapsto 10^x$, is a homomorphism since $10^{x+y} = 10^x 10^y$: it converts addition into multiplication. Kernel: $\{0\}$. Image: $\mathbb{R}_{>0}$.
> 5. $\mathbb{Z}/4\mathbb{Z} \to U_5$, $k \mapsto 2^k$ ([[§16 Isomorphisms#^prop-16-7|WS 2.5]]), has kernel $\{[0]\}$ and image all of $U_5$.
>
> In each case the kernel is a subgroup of the source and the image a subgroup of the target, as [[§15 Homomorphisms#^prop-15-2|WS 2.10]] asserts in general.
>
> *Source: cf. MATH 412*

^ex-15-1

*Uses:* [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§7 The Group ℤ∕nℤ#^def-7-1|Def. §7.1]]

> [!theorem] Proposition §15.2: Image and Kernel Are Subgroups
> Let $\varphi: G \to H$ be a group homomorphism. Then $\operatorname{Im}(\varphi)$ is a subgroup of $H$, and $\operatorname{Ker}(\varphi)$ is a subgroup of $G$.
>
> *Source: WS 2.10*

^prop-15-2

> [!proof]+ Proof
> **Image.** $e_H = \varphi(e_G) \in \operatorname{Im}\varphi$. If $\varphi(g) \in \operatorname{Im}\varphi$, then $\varphi(g)^{-1} = \varphi(g^{-1}) \in \operatorname{Im}\varphi$. If $\varphi(g), \varphi(g') \in \operatorname{Im}\varphi$, then $\varphi(g)\varphi(g') = \varphi(gg') \in \operatorname{Im}\varphi$.
>
> **Kernel.** $\varphi(e_G) = e_H$, so $e_G \in \operatorname{Ker}\varphi$. If $\varphi(g) = e_H$, then $\varphi(g^{-1}) = \varphi(g)^{-1} = e_H$. If $\varphi(g) = \varphi(g') = e_H$, then $\varphi(gg') = e_H \cdot e_H = e_H$.

^pf-15-2

*Uses:* [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|Proposition §21.8]] (590 §21.8).
> - Linear-algebra versions: [[§8 Null Spaces and Ranges#^ladr-3-13|The null space is a subspace]] (LADR 3.13), [[§8 Null Spaces and Ranges#^ladr-3-18|The range is a subspace]] (LADR 3.18).
> - Kernels are even normal: [[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]] (§36.2).
> - Computational version for linear maps: [[§24 Null Spaces, Column Spaces, and Linear Transformations#^thm-24-5|235 Thm. §24.5]].

> [!theorem] Proposition §15.3: Surjectivity and Injectivity via Image and Kernel
> Let $\varphi: G \to H$ be a homomorphism.
> 1. $\varphi$ is surjective if and only if $\operatorname{Im}(\varphi) = H$.
> 2. $\varphi$ is injective if and only if $\operatorname{Ker}(\varphi) = \{e_G\}$.
> 3. Hence $\varphi$ is an isomorphism if and only if $\operatorname{Im}(\varphi) = H$ and $\operatorname{Ker}(\varphi) = \{e_G\}$.

^prop-15-3

> [!proof]+ Proof
> (1) is the definition of surjective. (2) ($\Rightarrow$) $\varphi(e_G) = e_H$, and injectivity forbids any other element from mapping to $e_H$. ($\Leftarrow$) If $\varphi(g_1) = \varphi(g_2)$, then $\varphi(g_1 g_2^{-1}) = \varphi(g_1)\varphi(g_2)^{-1} = e_H$, so $g_1 g_2^{-1} \in \operatorname{Ker}\varphi = \{e_G\}$, giving $g_1 = g_2$. (3) combines (1), (2).

^pf-15-3

*Uses:* [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - MATH 590 version: [[§21 Algebra Prerequisites꞉ Groups#^prop-21-8|Proposition §21.8]] (590 §21.8).
> - Linear-algebra version: [[§8 Null Spaces and Ranges#^ladr-3-15|Injectivity ⟺ null space equals {0}]] (LADR 3.15).
> - Computational version for linear maps ℝⁿ → ℝᵐ: [[§9 The Matrix of a Linear Transformation#^thm-9-2|235 Thm. §9.2]] (one-to-one iff T(x) = 0 has only the trivial solution, with worked examples).

> [!example] Example §15.2: $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$
> Since $2^6 = 64 = 9 \cdot 7 + 1 \equiv 1 \pmod 7$, the map $\varphi: \mathbb{Z}/6\mathbb{Z} \to (\mathbb{Z}/7\mathbb{Z})^\times$, $k \mapsto 2^k$, is well-defined, and it is a homomorphism ($2^{k+l} = 2^k 2^l$). Its values are $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8 \equiv 1$, $2^4 \equiv 2$, $2^5 \equiv 4$. So
>
> $$
> \operatorname{Im}(\varphi) = \{1, 2, 4\}, \qquad \operatorname{Ker}(\varphi) = \{0, 3\}.
> $$
>
> Neither injective nor surjective, though the source and target both have order $6$. Contrast $k \mapsto 3^k$ ([[§16 Isomorphisms#^prop-16-8|WS 2.7]]), which is an isomorphism: the difference is that $3$ generates $U_7$ while $2$ generates only the subgroup $\{1, 2, 4\}$ of order $3$. Note also that the image has order $3$ and the kernel order $2$, with $3 \cdot 2 = 6 = |\mathbb{Z}/6\mathbb{Z}|$; this is not a coincidence.

^ex-15-2

![[m493-15-1.svg]]
*The homomorphism $\varphi: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$, of Ex. §15.2. The kernel $\{0, 3\}$ (red) goes to the identity $1$; the boxes $\{1, 4\}$ and $\{2, 5\}$ go to $2$ and $4$; and $3, 5, 6$ are never hit. Every box is a translate of the kernel with $2$ elements, so the $6$ elements of the source fill only $6/2 = 3$ values: this is the “not a coincidence” $3 \cdot 2 = 6$.*

> [!remark]- Connections
> - The general statement: [[§38 The First Isomorphism Theorem#^cor-38-2|Corollary §38.2]] of the First Isomorphism Theorem.

> [!theorem] Proposition §15.4: Images and Preimages of Subgroups
> Let $\varphi: G \to H$ be a group homomorphism.
> 1. If $G' \leq G$, then $\varphi(G') = \{\varphi(g') : g' \in G'\}$ is a subgroup of $H$. (Taking $G' = G$ recovers $\operatorname{Im}\varphi \leq H$.)
> 2. If $H' \leq H$, then $\varphi^{-1}(H') = \{g \in G : \varphi(g) \in H'\}$ is a subgroup of $G$. (Taking $H' = \{e_H\}$ recovers $\operatorname{Ker}\varphi \leq G$.)
> 3. If $\varphi$ is injective, then $\varphi$ restricts to an isomorphism $G' \to \varphi(G')$, and $G' \mapsto \varphi(G')$ is injective on subgroups.

^prop-15-4

> [!proof]+ Proof
> **(1)** $e_H = \varphi(e_G) \in \varphi(G')$ since $e_G \in G'$. For $g_1', g_2' \in G'$: $\varphi(g_1')\varphi(g_2') = \varphi(g_1'g_2') \in \varphi(G')$ by closure in $G'$, and $\varphi(g_1')^{-1} = \varphi(g_1'^{-1}) \in \varphi(G')$ since $g_1'^{-1} \in G'$.
>
> **(2)** $\varphi(e_G) = e_H \in H'$, so $e_G \in \varphi^{-1}(H')$. If $\varphi(g_1), \varphi(g_2) \in H'$ then $\varphi(g_1g_2) = \varphi(g_1)\varphi(g_2) \in H'$ and $\varphi(g_1^{-1}) = \varphi(g_1)^{-1} \in H'$, using that $H'$ is a subgroup.
>
> **(3)** The restriction $G' \to \varphi(G')$ is a surjective homomorphism by (1), and injective as a restriction of an injective map. If $\varphi(G_1') = \varphi(G_2')$ and $g \in G_1'$, then $\varphi(g) = \varphi(g')$ for some $g' \in G_2'$, so $g = g'$ by injectivity and $g \in G_2'$; symmetrically $G_2' \subseteq G_1'$.

^pf-15-4

*Uses:* [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The normal-subgroup version: [[§36 Sources of Normal Subgroups#^prop-36-4|Preimages and Images of Normal Subgroups]] (§36.4).

> [!remark] Remark: Kernels Are Normal: A Preview
> Kernels are not merely subgroups but *normal* subgroups: $\varphi(ghg^{-1}) = \varphi(g)\varphi(h)\varphi(g)^{-1} = e$ whenever $\varphi(h) = e$ ([[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]]). Images need not be normal.

^rem-15-1

> [!remark] Remark: Kernel as the Measure of Non-Injectivity
> The criterion “injective iff trivial kernel” is the standard way to prove a homomorphism is injective: instead of comparing arbitrary pairs $\varphi(g_1) = \varphi(g_2)$, one checks only which elements map to the identity. It has no analogue for arbitrary functions between sets; it works for homomorphisms because $\varphi(g_1) = \varphi(g_2)$ can be rewritten as $\varphi(g_1 g_2^{-1}) = e_H$.

^rem-15-2
