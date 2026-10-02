---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 38
tags: [group-theory, math493]
---
← [[§37 Quotient Groups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§39 Simple Groups]] →

*Reference: Pinter Ch. 16 (there called the Fundamental Homomorphism Theorem).*

> [!theorem] Theorem §38.1: First Isomorphism Theorem
> Let $\alpha: G \to H$ be a homomorphism, $N = \operatorname{Ker}\alpha$ (so $N \trianglelefteq G$), and $I = \operatorname{Im}\alpha$ (so $I \leq H$). Then
>
> $$ \beta: G/N \to I, \qquad \beta(gN) = \alpha(g), $$
>
> is a well-defined isomorphism. In particular $G/\operatorname{Ker}\alpha \cong \operatorname{Im}\alpha$.
>
> *Source: lecture*

^thm-38-1

> [!proof]+ Proof
> **Well defined.** Suppose $gN = g'N$. Then $g = g'n$ for some $n \in N$, so $\alpha(g) = \alpha(g')\alpha(n) = \alpha(g')\,e_H = \alpha(g')$.
>
> **Injective.** Suppose $\beta(gN) = \beta(g'N)$, i.e. $\alpha(g) = \alpha(g')$. Let $h = g^{-1}g'$, so $gh = g'$. Then $\alpha(h) = \alpha(g)^{-1}\alpha(g') = e_H$, so $h \in N$, and $g'N = ghN = gN$.
>
> **Surjective.** If $x \in I$, then $x = \alpha(g)$ for some $g \in G$, so $x = \beta(gN)$.
>
> **Homomorphism.** $\beta\big((g_1N)(g_2N)\big) = \beta(g_1g_2N) = \alpha(g_1g_2) = \alpha(g_1)\alpha(g_2) = \beta(g_1N)\,\beta(g_2N)$.

^pf-38-1

*Uses:* [[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§26 Left and Right Cosets#^prop-26-2|§26.2]], [[§37 Quotient Groups#^def-37-1|Def. §37.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

![[m493-38-1.svg]]
*The First Isomorphism Theorem: every homomorphism factors as the projection $\pi$, the isomorphism $\beta$, and the inclusion of the image.*

> [!remark]- Connections
> - Vector-space version: [[First isomorphism theorem]] (LADR 3.107).
> - Used in 590 to present a group as $F/N$: [[§21 Algebra Prerequisites꞉ Groups#^def-21-11|Group Presentation]].
> - Set-level version: [[§22 Partitions and Equivalence Relations#^prop-22-5|250 Prop. §22.5]] (a surjection induces a bijection on the quotient set).
> - Used in Quantum Mechanics: $SO(3) \cong SU(2)/\{\pm1\}$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].

> [!remark] Remark: Images Are Quotients
> Whenever $G$ is mapped into another group — into some $S_n$, some $GL_n(k)$, by various actions — the image looks like a quotient of $G$, determined entirely by what is sent to the identity. So understanding all possible images of $G$ amounts to understanding its normal subgroups. Note the asymmetry: kernels are always normal, but images are merely subgroups and need not be normal; for example $\mathbb{Z}/2\mathbb{Z} \to S_3$, $a \mapsto (1\,2)^a$, has image $\langle (1\,2) \rangle$, which is not normal ([[§36 Sources of Normal Subgroups#^prop-36-3|WS 6.5]], §36). This is one way in which groups are harder than vector spaces.
>
> *Source: lecture*

^rem-38-1

> [!theorem] Corollary §38.2: $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$
> Let $G$ be finite and $\alpha: G \to H$ a homomorphism. Then $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$.
>
> *Source: lecture*

^cor-38-2

> [!proof]+ Proof
> $|\operatorname{Im}\alpha| = |G/\operatorname{Ker}\alpha| = |G|/|\operatorname{Ker}\alpha|$, by the [[§38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]] and $G/N$ Is a Group ([[§37 Quotient Groups#^thm-37-1|§37.1]]).

^pf-38-2

*Uses:* [[§38 The First Isomorphism Theorem#^thm-38-1|§38.1]], [[§37 Quotient Groups#^thm-37-1|§37.1]]

> [!remark] Remark: Rank–Nullity
> The corollary is the group version of the [[§8 Null Spaces and Ranges#^ladr-3-21|rank–nullity theorem]]. For a linear map $\mathbb{F}_p^m \to \mathbb{F}_p^n$, the kernel is $\cong \mathbb{F}_p^{\text{nullity}}$ and the image is $\cong \mathbb{F}_p^{\text{rank}}$, so the corollary reads $p^m = p^{\text{nullity}} \cdot p^{\text{rank}}$. Rank–nullity has a plus where the corollary has a times because sizes of $\mathbb{F}_p$-spaces are powers of $p$, and multiplying powers adds exponents: $m = \text{nullity} + \text{rank}$.
>
> *Source: lecture*

^rem-38-2

> [!example] Example §38.1: The First Isomorphism Theorem in Action
> 1. $\operatorname{sgn}: S_n \to \{\pm 1\}$ is surjective for $n \geq 2$, with kernel $A_n$; so $S_n/A_n \cong \{\pm 1\}$ and $|A_n| = n!/2$.
> 2. $\det: GL_n(k) \to k^\times$ is surjective ($\det \operatorname{diag}(a, 1, \ldots, 1) = a$), with kernel $SL_n(k)$; so $GL_n(k)/SL_n(k) \cong k^\times$.
> 3. $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$ has kernel $\{[0], [3]\}$ and image $\{1, 2, 4\}$ ([[§15 Homomorphisms#^ex-15-2|Ex. §15.2]]); indeed $6 = 2 \cdot 3$, and $(\mathbb{Z}/6\mathbb{Z})/\{[0],[3]\} \cong \{1, 2, 4\} \cong \mathbb{Z}/3\mathbb{Z}$.
> 4. In [[§36 Sources of Normal Subgroups#^thm-36-5|PS 3.2]] (§36), $G/N \cong \varphi(G) \leq S_{G/H}$, so $[G : N] = |\varphi(G)|$ divides $n!$ by [[§27 The Index and Lagrange's Theorem#^thm-27-2|Lagrange]] — part (3) of [[§36 Sources of Normal Subgroups#^prop-36-6|The Normal Core]], recorded there.
> 5. The conjugation homomorphism $G \to \operatorname{Aut}(G)$, $a \mapsto c_a$, has kernel $Z(G)$ and image the inner automorphisms ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|PS 1.2]], §18); so $G/Z(G) \cong \operatorname{Inn}(G)$, the group of inner automorphisms.

^ex-38-1

![[m493-38-2.svg]]
*Part 3 of the example, $\alpha: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$. The kernel $N = \{[0], [3]\}$ (red) and its cosets are exactly the fibres of $\alpha$: each coset goes to a single element of the image $I = \{1, 2, 4\}$ (blue). So $\beta(gN) = \alpha(g)$ is well defined and bijective, $(\mathbb{Z}/6\mathbb{Z})/N \cong I$, and $6 = 2 \cdot 3$.*

> [!remark]- Connections
> - The homomorphism in (2): [[§34 Determinants#^ladr-9-49|Determinant is multiplicative]] (LADR 9.49).

> [!remark] Remark: PS 3.1 and PS 3.2 as Instances
> Both problems of Problem Set 3 that build a homomorphism into a symmetric group are special cases of the theorem.
>
> **[[§23 Actions#^thm-23-5|PS 3.1]] (Cayley).** Left multiplication gives $\varphi: G \to S_G$ with $\operatorname{Ker}\varphi = \{e\}$. For a trivial kernel the theorem reads
>
> $$ G \cong G/\{e\} \cong \operatorname{Im}\varphi \leq S_G: $$
>
> an injective homomorphism is an isomorphism onto its image, which is exactly the step used in the proof of [[§23 Actions#^thm-23-5|Cayley's Theorem]] (§23).
>
> **[[§36 Sources of Normal Subgroups#^thm-36-5|PS 3.2]] (a normal subgroup inside $H$).** The proof defines $\bar\varphi: G/N \to S_{G/H}$, $\bar\varphi(gN) = \varphi(g)$, for $N = \operatorname{Ker}\varphi$, and checks that it is well defined ($g' = gk$ with $k \in N$ gives $\varphi(g') = \varphi(g)$) and injective ($\varphi(g) = \varphi(g')$ gives $g^{-1}g' \in N$). These are the first two steps of the proof of the First Isomorphism Theorem, carried out before the theorem was available, when $G/N$ was only a set of cosets and injectivity gave $[G:N] \leq n!$ by counting. Now that $G/N$ is a group, $\bar\varphi$ is the isomorphism $\beta$ of the theorem onto $\varphi(G) \leq S_{G/H}$, so $[G:N] = |\varphi(G)|$ divides $n!$ by Lagrange.

^rem-38-3
