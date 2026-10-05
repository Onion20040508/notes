---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 41
tags: [group-theory, math493]
---
← [[§40 Quotient Groups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§42 The Correspondence and Third Isomorphism Theorems]] →

*Reference: Pinter Ch. 16 (there called the Fundamental Homomorphism Theorem).*

> [!theorem] Theorem §41.1: First Isomorphism Theorem
> Let $\alpha: G \to H$ be a homomorphism, $N = \operatorname{Ker}\alpha$ (so $N \trianglelefteq G$), and $I = \operatorname{Im}\alpha$ (so $I \leq H$). Then
>
> $$ \beta: G/N \to I, \qquad \beta(gN) = \alpha(g), $$
>
> is a well-defined isomorphism. In particular $G/\operatorname{Ker}\alpha \cong \operatorname{Im}\alpha$.
>
> *Source: lecture*

^thm-41-1

> [!proof]+ Proof
> **Well defined.** Suppose $gN = g'N$. Then $g = g'n$ for some $n \in N$, so $\alpha(g) = \alpha(g')\alpha(n) = \alpha(g')\,e_H = \alpha(g')$.
>
> **Injective.** Suppose $\beta(gN) = \beta(g'N)$, i.e. $\alpha(g) = \alpha(g')$. Let $h = g^{-1}g'$, so $gh = g'$. Then $\alpha(h) = \alpha(g)^{-1}\alpha(g') = e_H$, so $h \in N$, and $g'N = ghN = gN$.
>
> **Surjective.** If $x \in I$, then $x = \alpha(g)$ for some $g \in G$, so $x = \beta(gN)$.
>
> **Homomorphism.** $\beta\big((g_1N)(g_2N)\big) = \beta(g_1g_2N) = \alpha(g_1g_2) = \alpha(g_1)\alpha(g_2) = \beta(g_1N)\,\beta(g_2N)$.

^pf-41-1

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§15 Homomorphisms#^prop-15-1|§15.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

![[m493-38-1.svg]]
*The First Isomorphism Theorem: every homomorphism factors as the projection $\pi$, the isomorphism $\beta$, and the inclusion of the image.*

> [!remark]- Connections
> - Vector-space version: [[First isomorphism theorem]] (LADR 3.107).
> - Used in 590 to present a group as $F/N$: [[§21 Algebra Prerequisites꞉ Groups#^def-21-11|Group Presentation]].
> - Set-level version: [[§22 Partitions and Equivalence Relations#^prop-22-5|250 Prop. §22.5]] (a surjection induces a bijection on the quotient set).
> - Used in Quantum Mechanics: $SO(3) \cong SU(2)/\{\pm1\}$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
> - Used in Quantum Field Theory: $SO^+(1,3) \cong SL(2, \mathbb C)/\{\pm1\}$ — [[§C5.1 Weyl Spinors and SL(2,C)#^thm-c5-1-8|QFT Theorem §C5.1.8]].

> [!remark] Remark: Images Are Quotients
> Whenever $G$ is mapped into another group — into some $S_n$, some $GL_n(k)$, by various actions — the image looks like a quotient of $G$, determined entirely by what is sent to the identity. So understanding all possible images of $G$ amounts to understanding its normal subgroups. Note the asymmetry: kernels are always normal, but images are merely subgroups and need not be normal; for example $\mathbb{Z}/2\mathbb{Z} \to S_3$, $a \mapsto (1\,2)^a$, has image $\langle (1\,2) \rangle$, which is not normal ([[§39 Sources of Normal Subgroups#^prop-39-3|WS 6.5]], §39). This is one way in which groups are harder than vector spaces.
>
> *Source: lecture*

^rem-41-1

> [!theorem] Corollary §41.2: $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$
> Let $G$ be finite and $\alpha: G \to H$ a homomorphism. Then $|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$.
>
> *Source: lecture*

^cor-41-2

> [!proof]+ Proof
> $|\operatorname{Im}\alpha| = |G/\operatorname{Ker}\alpha| = |G|/|\operatorname{Ker}\alpha|$, by the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem]] and $G/N$ Is a Group ([[§40 Quotient Groups#^thm-40-1|§40.1]]).

^pf-41-2

*Uses:* [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]]

> [!remark] Remark: Rank–Nullity
> The corollary is the group version of the [[§8 Null Spaces and Ranges#^ladr-3-21|rank–nullity theorem]]. For a linear map $\mathbb{F}_p^m \to \mathbb{F}_p^n$, the kernel is $\cong \mathbb{F}_p^{\text{nullity}}$ and the image is $\cong \mathbb{F}_p^{\text{rank}}$, so the corollary reads $p^m = p^{\text{nullity}} \cdot p^{\text{rank}}$. Rank–nullity has a plus where the corollary has a times because sizes of $\mathbb{F}_p$-spaces are powers of $p$, and multiplying powers adds exponents: $m = \text{nullity} + \text{rank}$.
>
> *Source: lecture*

^rem-41-2

> [!example] Example §41.1: The First Isomorphism Theorem in Action
> 1. $\operatorname{sgn}: S_n \to \{\pm 1\}$ is surjective for $n \geq 2$, with kernel $A_n$; so $S_n/A_n \cong \{\pm 1\}$ and $|A_n| = n!/2$.
> 2. $\det: GL_n(k) \to k^\times$ is surjective ($\det \operatorname{diag}(a, 1, \ldots, 1) = a$), with kernel $SL_n(k)$; so $GL_n(k)/SL_n(k) \cong k^\times$.
> 3. $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$ has kernel $\{[0], [3]\}$ and image $\{1, 2, 4\}$ ([[§15 Homomorphisms#^ex-15-2|Ex. §15.2]]); indeed $6 = 2 \cdot 3$, and $(\mathbb{Z}/6\mathbb{Z})/\{[0],[3]\} \cong \{1, 2, 4\} \cong \mathbb{Z}/3\mathbb{Z}$.
> 4. In [[§39 Sources of Normal Subgroups#^thm-39-5|PS 3.2]] (§39), $G/N \cong \varphi(G) \leq S_{G/H}$, so $[G : N] = |\varphi(G)|$ divides $n!$ by [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange]] — part (3) of [[§39 Sources of Normal Subgroups#^prop-39-6|The Normal Core]], recorded there.
> 5. The conjugation homomorphism $G \to \operatorname{Aut}(G)$, $a \mapsto c_a$, has kernel $Z(G)$ and image the inner automorphisms ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|PS 1.2]], §18); so $G/Z(G) \cong \operatorname{Inn}(G)$, the group of inner automorphisms.

^ex-41-1

![[m493-38-2.svg]]
*Part 3 of the example, $\alpha: \mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$. The kernel $N = \{[0], [3]\}$ (red) and its cosets are exactly the fibres of $\alpha$: each coset goes to a single element of the image $I = \{1, 2, 4\}$ (blue). So $\beta(gN) = \alpha(g)$ is well defined and bijective, $(\mathbb{Z}/6\mathbb{Z})/N \cong I$, and $6 = 2 \cdot 3$.*

> [!remark]- Connections
> - The homomorphism in (2): [[§34 Determinants#^ladr-9-49|Determinant is multiplicative]] (LADR 9.49).

> [!remark] Remark: PS 3.1 and PS 3.2 as Instances
> Both problems of Problem Set 3 that build a homomorphism into a symmetric group are special cases of the theorem.
>
> **[[§25 Actions#^thm-25-5|PS 3.1]] (Cayley).** Left multiplication gives $\varphi: G \to S_G$ with $\operatorname{Ker}\varphi = \{e\}$. For a trivial kernel the theorem reads
>
> $$ G \cong G/\{e\} \cong \operatorname{Im}\varphi \leq S_G: $$
>
> an injective homomorphism is an isomorphism onto its image, which is exactly the step used in the proof of [[§25 Actions#^thm-25-5|Cayley's Theorem]] (§25).
>
> **[[§39 Sources of Normal Subgroups#^thm-39-5|PS 3.2]] (a normal subgroup inside $H$).** The proof defines $\bar\varphi: G/N \to S_{G/H}$, $\bar\varphi(gN) = \varphi(g)$, for $N = \operatorname{Ker}\varphi$, and checks that it is well defined ($g' = gk$ with $k \in N$ gives $\varphi(g') = \varphi(g)$) and injective ($\varphi(g) = \varphi(g')$ gives $g^{-1}g' \in N$). These are the first two steps of the proof of the First Isomorphism Theorem, carried out before the theorem was available, when $G/N$ was only a set of cosets and injectivity gave $[G:N] \leq n!$ by counting. Now that $G/N$ is a group, $\bar\varphi$ is the isomorphism $\beta$ of the theorem onto $\varphi(G) \leq S_{G/H}$, so $[G:N] = |\varphi(G)|$ divides $n!$ by Lagrange.

^rem-41-3

## The Second Isomorphism Theorem

*Source: Lecture (Fri Oct 2); Lecture and Worksheet 8 (Mon Oct 5).*

> [!definition] Definition §41.1: The Product Set $HN$
> For [[§4 Subgroups#^def-4-1|subgroups]] $H, N$ of $G$, write $HN := \{hn : h \in H,\ n \in N\}$.

^def-41-1

> [!theorem] Lemma §41.3: $HN$ Is a Subgroup When $N$ Is Normal
> If $H \leq G$ and $N \trianglelefteq G$ ([[§38 Normal Subgroups#^def-38-1|Def. §38.1]]), then $HN$ ([[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]]) is a subgroup of $G$, and it contains both $H$ and $N$.
>
> *Source: lecture 10/2; PS 4.1(2); WS 8.1*

^lem-41-3

> [!proof]+ Proof
> *Closure (lecture).* Let $h_1, h_2 \in H$ and $n_1, n_2 \in N$. Since $N$ is normal, $n_1h_2 = h_2n'$ for some $n' \in N$ ($n' = h_2^{-1}n_1h_2$). So $h_1n_1 \cdot h_2n_2 = h_1h_2 \cdot n'n_2 \in HN$. *Containment:* $h = he$ and $n = en$.
>
> *Identity (PS 4.1(2)).* $e = ee \in HN$, since $e \in H$ and $e \in N$.
>
> *Inverses (PS 4.1(2)).* For $hn \in HN$, $(hn)^{-1} = n^{-1}h^{-1} = h^{-1}\big(hn^{-1}h^{-1}\big)$ ([[§2 First Consequences of the Axioms#^prop-2-4|Inverse of a Product]]). Here $h^{-1} \in H$, and $hn^{-1}h^{-1} \in N$ by [[§38 Normal Subgroups#^def-38-1|normality]] applied to $n^{-1} \in N$; so $(hn)^{-1} \in HN$.
>
> By the symmetric argument, $HN$ is also a subgroup when $H$, rather than $N$, is normal (as [[493 Problem Set 4#^hw-4-1|PS 4.1(2)]] notes). Without either hypothesis it can fail: $AB$ Need Not Be a Subgroup ([[§41 The First and Second Isomorphism Theorems#^ex-41-2|Ex. §41.2]]), below.

^pf-41-3

*Uses:* [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!example] Example §41.2: $AB$ Need Not Be a Subgroup
> Without normality, the [[§41 The First and Second Isomorphism Theorems#^def-41-1|product set]] of two [[§4 Subgroups#^def-4-1|subgroups]] can fail to be a subgroup. In $S_3$ ([[§10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]]) take $A = \{e, (1\,2)\}$ and $B = \{e, (1\,3)\}$. Then
>
> $$ AB = \{e,\ (1\,3),\ (1\,2),\ (1\,2)(1\,3)\} = \{e,\ (1\,2),\ (1\,3),\ (1\,3\,2)\}, $$
>
> since $(1\,2)(1\,3)$ sends $1 \mapsto 3 \mapsto 3$, $3 \mapsto 1 \mapsto 2$, $2 \mapsto 2 \mapsto 1$. But $(1\,3\,2)^{-1} = (1\,2\,3) \notin AB$, so $AB$ is not closed under inverses. (Neither $A$ nor $B$ is [[§38 Normal Subgroups#^def-38-1|normal]] in $S_3$ ([[§38 Normal Subgroups#^ex-38-1|Ex. §38.1]]); compare $HN$ Is a Subgroup When $N$ Is Normal ([[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]), above. Alternatively: $|AB| = 4$ does not divide $6$.)
>
> *Source: PS 4.1(1)*

^ex-41-2

> [!theorem] Theorem §41.4: Second Isomorphism Theorem
> Let $G$ be a group, $N \trianglelefteq G$, $H \leq G$, and $\pi: G \to G/N$ the [[§40 Quotient Groups#^def-40-1|projection]]. Then $H \cap N \trianglelefteq H$, $N \trianglelefteq HN$ ([[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]], [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]), $\pi(H) = \pi(HN)$, and
>
> $$ H/(H \cap N) \;\cong\; \pi(H) \;=\; \pi(HN) \;\cong\; HN/N. $$
>
> In particular $H/(H \cap N) \cong HN/N$.
>
> *Source: lecture 10/2, 10/5; WS 8.2*

^thm-41-4

> [!proof]+ Proof
> *$\pi(H) = \pi(HN)$.* For $h \in H$, $\pi(h) = \pi(he) \in \pi(HN)$. For $hn \in HN$, $\pi(hn) = \pi(h)\pi(n) = \pi(h) \in \pi(H)$, since $n \in N = \operatorname{Ker}\pi$ ([[§40 Quotient Groups#^prop-40-2|§40.2]]).
>
> *Two applications of the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem]]* (§41). Restrict $\pi$ to $H$: the kernel is $\{h \in H : hN = N\} = H \cap N$, so $H \cap N$ is normal in $H$ ([[§39 Sources of Normal Subgroups#^prop-39-2|Kernels Are Normal]]) and $H/(H \cap N) \cong \pi(H)$. Restrict $\pi$ to $HN$: the kernel is $HN \cap N = N$, since $N \subseteq HN$ ([[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]), so $N \trianglelefteq HN$ and $HN/N \cong \pi(HN)$. Combining with $\pi(H) = \pi(HN)$ gives the chain.

^pf-41-4

*Uses:* [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]], [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]], [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

![[m493-38-3.svg]]
*The “diamond” picture of the Second Isomorphism Theorem: lines denote inclusion, and the two marked quotients on opposite sides agree, $HN/N \cong H/(H \cap N)$.*

> [!theorem] Lemma §41.5: Restricting a Homomorphism
> Let $f: X \to Y$ be a [[§15 Homomorphisms#^def-15-1|homomorphism]] and $X' \leq X$ a subgroup. Then the restriction $f|_{X'}: X' \to Y$ is a homomorphism with $\operatorname{Ker}(f|_{X'}) = \operatorname{Ker}(f) \cap X'$.
>
> *Source: lecture 10/5*

^lem-41-5

> [!proof]+ Proof
> The restriction preserves products because $f$ does. For $x \in X'$, $f|_{X'}(x) = e_Y$ iff $f(x) = e_Y$ iff $x \in \operatorname{Ker} f$; so the kernel is $\operatorname{Ker} f \cap X'$.

^pf-41-5

*Uses:* [[§15 Homomorphisms#^def-15-1|Def. §15.1]]

> [!remark] Remark: The Second Isomorphism Theorem Revisited
> The lemma is exactly what the proof of the [[§41 The First and Second Isomorphism Theorems#^thm-41-4|Second Isomorphism Theorem]] uses: with $\pi: G \to G/N$, the restriction to $SN$ has kernel $N \cap SN = N$, the restriction to $S$ has kernel $N \cap S$, and both have the same image $\pi(SN) = \pi(S)$. So
>
> $$ SN/N \;\cong\; \pi(SN) \;=\; \pi(S) \;\cong\; S/(S \cap N), $$
>
> each $\cong$ by the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem]]. WS 8.2 phrases this as: $\alpha: S \to SN \to SN/N$ is surjective with $\operatorname{Ker}\alpha = S \cap N$.
>
> *Source: lecture 10/5*

^rem-41-4

> [!remark] Remark: Linear Algebra Analogy
> For subspaces $L_1, L_2$ of a vector space $V$, $\dim(L_1 \cap L_2) = \dim L_1 + \dim L_2 - \dim(L_1 + L_2)$. This is the linear-algebra shadow of the Second Isomorphism Theorem: $(L_1 + L_2)/L_2 \cong L_1/(L_1 \cap L_2)$, and taking dimensions gives the formula. The group version replaces dimensions by orders and sums by products ([[§41 The First and Second Isomorphism Theorems#^cor-41-6|Corollary §41.6]]).
>
> *Source: lecture 10/5*

^rem-41-5

> [!remark]- Connections
> - The dimension formula in LADR: [[§6 Dimension#^ladr-2-43|LADR 2.43]] (dimension of a sum); quotient spaces, [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].

> [!theorem] Corollary §41.6: The Order of $SN$
> Let $N \trianglelefteq G$ and $S \leq G$, with $S$ and $N$ finite. Then
>
> $$ |SN| = \frac{|S|\,|N|}{|S \cap N|}. $$
>
> *Source: WS 8.3*

^cor-41-6

> [!proof]- Proof
> *[To be proved.]*

^pf-41-6

> [!theorem] Corollary §41.7: Subgroup Representatives, Again
> If a [[§40 Quotient Groups#^def-40-2|set of representatives]] $S$ for $G/N$ is a [[§4 Subgroups#^def-4-1|subgroup]], then $S \cong G/N$.
>
> *Source: lecture 10/2*

^cor-41-7

> [!proof]+ Proof
> Take $H = S$. Every $g \in G$ lies in some coset $sN$ with $s \in S$, so $SN = G$; and $S \cap N = \{e\}$ ([[§40 Quotient Groups#^prop-40-4|Representatives Forming a Subgroup]], §40.4). The [[§41 The First and Second Isomorphism Theorems#^thm-41-4|theorem]] gives $S \cong S/\{e\} = S/(S \cap N) \cong SN/N = G/N$.

^pf-41-7

*Uses:* [[§41 The First and Second Isomorphism Theorems#^thm-41-4|§41.4]], [[§40 Quotient Groups#^def-40-2|Def. §40.2]], [[§40 Quotient Groups#^prop-40-4|§40.4]]

> [!remark]- Connections
> - Proved directly, without the theorem: [[§40 Quotient Groups#^prop-40-4|Representatives Forming a Subgroup]] (§40.4).

[[§44 S₃, S₄, A₄ and A₅#^ex-44-3|Example §44.3]], in the $GL_n$ part of [[§44 S₃, S₄, A₄ and A₅|§44]], applies the theorem to $GL_2^+(\mathbb{R})$, $SL_2(\mathbb{R})$ and the scalar matrices.
