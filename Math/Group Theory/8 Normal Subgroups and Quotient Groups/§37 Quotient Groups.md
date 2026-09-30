---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 37
tags: [group-theory, math493]
---
← [[§36 Sources of Normal Subgroups]] · ↑ [[8 Normal Subgroups and Quotient Groups]] · [[§38 The First Isomorphism Theorem]] →

*Reference: Pinter Ch. 15.*

> [!remark] Remark: The Question
> If $\alpha: G \to H$ is a homomorphism, then $\operatorname{Ker}\alpha$ is normal in $G$ ([[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]], §36). Conversely, if $N \trianglelefteq G$, is $N = \operatorname{Ker}\alpha$ for some homomorphism $\alpha$? The answer is yes: we construct a group $G/N$ and a homomorphism $G \to G/N$ with kernel exactly $N$.
>
> *Source: lecture*

^rem-37-1

Recall that for $N \trianglelefteq G$ we have $gN = Ng$ for every $g$ ([[§35 Normal Subgroups#^prop-35-2|Characterizations of Normality]], §35, whose proof includes the lecture's direct argument). So $G/N = \{gN : g \in G\} = \{Ng : g \in G\}$, and for a normal subgroup there is no ambiguity between left and right cosets.

> [!definition] Definition §37.1: Quotient Group
> Let $N \trianglelefteq G$. The **quotient group** $G/N$ (read “$G$ mod $N$”) is the set of cosets $\{gN : g \in G\}$ with the operation
>
> $$ (g_1N)(g_2N) := (g_1g_2)N. $$
>
> The map $\pi: G \to G/N$, $\pi(g) = gN$, is the **canonical projection** (or quotient map).
>
> *Source: lecture*

^def-37-1

> [!remark]- Connections
> - 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^def-21-13|Cosets and Quotient Group (590 §21.13)]].
> - Linear-algebra versions: [[3E Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]] and [[3E Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]]; topological version: [[§12 Quotient Topology#^def-12-3|Quotient Space]].

> [!theorem] Theorem §37.1: $G/N$ Is a Group
> Let $N \trianglelefteq G$. With coset multiplication, $G/N$ is a group, with identity $eN = N$ and inverses $(gN)^{-1} = g^{-1}N$. If $G$ is finite, $|G/N| = [G : N] = |G|/|N|$.
>
> *Source: lecture*

^thm-37-1

> [!proof]+ Proof
> The operation is well defined by [[§34 Multiplying Cosets#^prop-34-1|When Coset Multiplication Is Well Defined]] (§34), where the lecture's set-product proof is recorded as a second proof. Every property reduces to the corresponding property of $G$ by computing with representatives: *associativity*, $(g_1N\,g_2N)\,g_3N = (g_1g_2)g_3N = g_1(g_2g_3)N = g_1N\,(g_2N\,g_3N)$; *identity*, $(eN)(gN) = gN = (gN)(eN)$; *inverses*, $(gN)(g^{-1}N) = eN = (g^{-1}N)(gN)$. The count is the definition of the index together with Lagrange ([[§27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]]).

^pf-37-1

*Uses:* [[§34 Multiplying Cosets#^prop-34-1|§34.1]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]], [[§27 The Index and Lagrange's Theorem#^def-27-1|Def. §27.1]], [[§27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]]

> [!remark]- Connections
> - Vector-space version: [[3E Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]].

> [!theorem] Proposition §37.2: Every Normal Subgroup Is a Kernel
> Let $N \trianglelefteq G$. The canonical projection $\pi: G \to G/N$, $g \mapsto gN$, is a surjective homomorphism with $\operatorname{Ker}\pi = N$.
>
> *Source: lecture*

^prop-37-2

> [!proof]+ Proof
> $\pi(g_1g_2) = g_1g_2N = (g_1N)(g_2N) = \pi(g_1)\pi(g_2)$ by the definition of the operation; $\pi$ is surjective by construction. The identity of $G/N$ is $N$, so $\operatorname{Ker}\pi = \{g : gN = N\} = \{g : g \in N\} = N$ ([[§26 Left and Right Cosets#^prop-26-2|§26.2]]).

^pf-37-2

*Uses:* [[§37 Quotient Groups#^def-37-1|Def. §37.1]], [[§37 Quotient Groups#^thm-37-1|§37.1]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§26 Left and Right Cosets#^prop-26-2|§26.2]]

> [!remark]- Connections
> - Vector-space version: [[3E Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]] ($\operatorname{null}\pi = U$, shown in the proof of [[3E Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]]); in 590 stated in [[§21 Algebra Prerequisites꞉ Groups#^def-21-13|Cosets and Quotient Group]].

> [!remark] Remark: Kernels and Normal Subgroups Are the Same Thing
> Together with [[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]], the proposition says: the normal subgroups of $G$ are exactly the kernels of homomorphisms out of $G$. This is why normality, a condition that looks technical, is the natural one.

^rem-37-2

> [!example] Example §37.1: Quotient Groups
> 1. $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the (normal, since $\mathbb{Z}$ is abelian) subgroup $n\mathbb{Z}$: its elements are the cosets $a + n\mathbb{Z} = [a]$, and coset addition is the addition of residue classes of [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]. The notation of [[2 Arithmetic Modulo n|Chapter 2]] is thus an instance of the general one.
> 2. $G/G$ is the trivial group, and $G/\{e\} \cong G$ via $g\{e\} \mapsto g$.
> 3. $S_3/A_3$ has two elements, $A_3$ and $(1\,2)A_3$; it is cyclic of order $2$.

^ex-37-1

![[m493-37-1.svg]]
*Part 1 of the example with $n = 3$: the canonical projection $\pi: \mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$ collapses each coset $a + 3\mathbb{Z}$ (one colour each) to a single element $[a]$ of the quotient group. The grey arrows show adding $[1]$: $[0] \to [1] \to [2] \to [0]$.*

> [!remark]- Connections
> - 590 version of (1): [[§21 Algebra Prerequisites꞉ Groups#^ex-21-7|Example §21.7]].
