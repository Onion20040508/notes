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
> - Used in Quantum Field Theory: $SO^+(1,3) \cong SL(2, \mathbb C)/\{\pm1\}$ — [[§C5.1 Weyl Spinors and SL(2,C)#^thm-c5-1-8|QFT Theorem §C5.1.8]].

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

## The Second Isomorphism Theorem

*Source: Lecture (Fri Oct 2).*

> [!definition] Definition §38.1: The Product Set $HN$
> For [[§4 Subgroups#^def-4-1|subgroups]] $H, N$ of $G$, write $HN := \{hn : h \in H,\ n \in N\}$.

^def-38-1

> [!theorem] Lemma §38.3: $HN$ Is a Subgroup When $N$ Is Normal
> If $H \leq G$ and $N \trianglelefteq G$ ([[§35 Normal Subgroups#^def-35-1|Def. §35.1]]), then $HN$ ([[§38 The First Isomorphism Theorem#^def-38-1|Def. §38.1]]) is a subgroup of $G$, and it contains both $H$ and $N$.
>
> *Source: lecture 10/2*

^lem-38-3

> [!proof]+ Proof
> *Closure (lecture).* Let $h_1, h_2 \in H$ and $n_1, n_2 \in N$. Since $N$ is normal, $n_1h_2 = h_2n'$ for some $n' \in N$ ($n' = h_2^{-1}n_1h_2$). So $h_1n_1 \cdot h_2n_2 = h_1h_2 \cdot n'n_2 \in HN$. *Containment:* $h = he$ and $n = en$.
>
> *Identity and inverses:* *[To be proved; assigned as homework.]*

^pf-38-3

*Uses:* [[§38 The First Isomorphism Theorem#^def-38-1|Def. §38.1]], [[§35 Normal Subgroups#^def-35-1|Def. §35.1]]

> [!theorem] Theorem §38.4: Second Isomorphism Theorem
> Let $G$ be a group, $N \trianglelefteq G$, $H \leq G$, and $\pi: G \to G/N$ the [[§37 Quotient Groups#^def-37-1|projection]]. Then $H \cap N \trianglelefteq H$, $N \trianglelefteq HN$ ([[§38 The First Isomorphism Theorem#^def-38-1|Def. §38.1]], [[§38 The First Isomorphism Theorem#^lem-38-3|§38.3]]), $\pi(H) = \pi(HN)$, and
>
> $$ H/(H \cap N) \;\cong\; \pi(H) \;=\; \pi(HN) \;\cong\; HN/N. $$
>
> In particular $H/(H \cap N) \cong HN/N$.
>
> *Source: lecture 10/2*

^thm-38-4

> [!proof]+ Proof
> *$\pi(H) = \pi(HN)$.* For $h \in H$, $\pi(h) = \pi(he) \in \pi(HN)$. For $hn \in HN$, $\pi(hn) = \pi(h)\pi(n) = \pi(h) \in \pi(H)$, since $n \in N = \operatorname{Ker}\pi$ ([[§37 Quotient Groups#^prop-37-2|§37.2]]).
>
> *Two applications of the [[§38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]]* (§38). Restrict $\pi$ to $H$: the kernel is $\{h \in H : hN = N\} = H \cap N$, so $H \cap N$ is normal in $H$ ([[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]]) and $H/(H \cap N) \cong \pi(H)$. Restrict $\pi$ to $HN$: the kernel is $HN \cap N = N$, since $N \subseteq HN$ ([[§38 The First Isomorphism Theorem#^lem-38-3|§38.3]]), so $N \trianglelefteq HN$ and $HN/N \cong \pi(HN)$. Combining with $\pi(H) = \pi(HN)$ gives the chain.

^pf-38-4

*Uses:* [[§38 The First Isomorphism Theorem#^def-38-1|Def. §38.1]], [[§38 The First Isomorphism Theorem#^lem-38-3|§38.3]], [[§37 Quotient Groups#^prop-37-2|§37.2]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]], [[§38 The First Isomorphism Theorem#^thm-38-1|§38.1]]

![[m493-38-3.svg]]
*The “diamond” picture of the Second Isomorphism Theorem: lines denote inclusion, and the two marked quotients on opposite sides agree, $HN/N \cong H/(H \cap N)$.*

> [!theorem] Corollary §38.5: Subgroup Representatives, Again
> If a [[§37 Quotient Groups#^def-37-2|set of representatives]] $S$ for $G/N$ is a [[§4 Subgroups#^def-4-1|subgroup]], then $S \cong G/N$.
>
> *Source: lecture 10/2*

^cor-38-5

> [!proof]+ Proof
> Take $H = S$. Every $g \in G$ lies in some coset $sN$ with $s \in S$, so $SN = G$; and $S \cap N = \{e\}$ ([[§37 Quotient Groups#^prop-37-4|Representatives Forming a Subgroup]], §37). The [[§38 The First Isomorphism Theorem#^thm-38-4|theorem]] gives $S \cong S/\{e\} = S/(S \cap N) \cong SN/N = G/N$.

^pf-38-5

*Uses:* [[§38 The First Isomorphism Theorem#^thm-38-4|§38.4]], [[§37 Quotient Groups#^def-37-2|Def. §37.2]], [[§37 Quotient Groups#^prop-37-4|§37.4]]

> [!remark]- Connections
> - Proved directly, without the theorem: [[§37 Quotient Groups#^prop-37-4|Representatives Forming a Subgroup]] (§37.4).

> [!example] Example §38.2: The Second Isomorphism Theorem in Action
> 1. $G = S_3$, $N = A_3$ ([[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]]), $H = \langle (1\,2) \rangle$: $H \cap N = \{e\}$ and $HN = S_3$, so $\langle (1\,2) \rangle \cong S_3/A_3$.
> 2. $G = S_4$, $N = V$ ([[§36 Sources of Normal Subgroups#^ex-36-3|Ex. §36.3]]), $H = \operatorname{Stab}(4) \cong S_3$ ([[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]]): every non-identity element of $V$ moves $4$, so $H \cap V = \{e\}$, and $HV/V \cong H$ has $6 = 24/4 = |S_4/V|$ elements, so $HV/V = S_4/V$. Hence $S_4/V \cong S_3$, recovering [[§39 Simple Groups#^prop-39-10|The Pair-Partition Homomorphism]] (§39) by a second route.

^ex-38-2

> [!theorem] Theorem §38.6: Third Isomorphism Theorem
> Let $N \subseteq K$ be [[§35 Normal Subgroups#^def-35-1|normal subgroups]] of $G$. Then $K/N$ is a normal subgroup of $G/N$ ([[§37 Quotient Groups#^def-37-1|Def. §37.1]]), and $(G/N)/(K/N) \cong G/K$.
>
> *Source: named in lecture 10/2; not covered*

^thm-38-6

> [!proof]- Proof
> *[To be proved.]*

^pf-38-6

> [!remark] Remark: The Isomorphism Theorems
> The lecture's theme: these theorems are about how to work in a quotient that did not come to you as the image of some map. The [[§38 The First Isomorphism Theorem#^thm-38-1|first]] identifies $G/N$ with an image; the [[§38 The First Isomorphism Theorem#^thm-38-4|second]] and [[§38 The First Isomorphism Theorem#^thm-38-6|third]] compare quotients of subgroups and quotients of quotients. A worksheet on the second and third theorems is on the course Canvas site; the lecture recommended experimenting with small groups to make them intuitive.

^rem-38-4
