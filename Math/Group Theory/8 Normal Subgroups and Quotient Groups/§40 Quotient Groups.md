---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 40
tags: [group-theory, math493]
---
← [[§39 Sources of Normal Subgroups]] · ↑ [[· 8 Normal Subgroups and Quotient Groups]] · [[§41 The First and Second Isomorphism Theorems]] →

*Reference: Pinter Ch. 15.*

> [!remark] Remark: The Question
> If $\alpha: G \to H$ is a homomorphism, then $\operatorname{Ker}\alpha$ is normal in $G$ ([[§39 Sources of Normal Subgroups#^prop-39-2|Kernels Are Normal]], §39). Conversely, if $N \trianglelefteq G$, is $N = \operatorname{Ker}\alpha$ for some homomorphism $\alpha$? The answer is yes: we construct a group $G/N$ and a homomorphism $G \to G/N$ with kernel exactly $N$.
>
> *Source: lecture*

^rem-40-1

Recall that for $N \trianglelefteq G$ we have $gN = Ng$ for every $g$ ([[§38 Normal Subgroups#^prop-38-2|Characterizations of Normality]], §38, whose proof includes the lecture's direct argument). So $G/N = \{gN : g \in G\} = \{Ng : g \in G\}$, and for a normal subgroup there is no ambiguity between left and right cosets.

> [!definition] Definition §40.1: Quotient Group
> Let $N \trianglelefteq G$. The **quotient group** $G/N$ (read “$G$ mod $N$”) is the set of cosets $\{gN : g \in G\}$ with the operation
>
> $$ (g_1N)(g_2N) := (g_1g_2)N. $$
>
> The map $\pi: G \to G/N$, $\pi(g) = gN$, is the **canonical projection** (or quotient map).
>
> *Source: lecture*

^def-40-1

> [!remark]- Connections
> - 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^def-21-new3|Quotient Group (590 §21.13)]].
> - Linear-algebra versions: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|Quotient space, V∕U]] and [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]]; topological version: [[§12 Quotient Topology#^def-12-3|Quotient Space]].

> [!theorem] Theorem §40.1: $G/N$ Is a Group
> Let $N \trianglelefteq G$. With coset multiplication, $G/N$ is a group, with identity $eN = N$ and inverses $(gN)^{-1} = g^{-1}N$. If $G$ is finite, $|G/N| = [G : N] = |G|/|N|$.
>
> *Source: lecture*

^thm-40-1

> [!proof]+ Proof
> The operation is well defined by [[§37 Multiplying Cosets#^prop-37-1|When Coset Multiplication Is Well Defined]] (§37); the lecture's set-product proof is recorded as a remark after [[§38 Normal Subgroups#^rem-38-2|Multiplying Sets]] ([[§38 Normal Subgroups#^rem-38-3|§38]]). Every property reduces to the corresponding property of $G$ by computing with representatives: *associativity*, $(g_1N\,g_2N)\,g_3N = (g_1g_2)g_3N = g_1(g_2g_3)N = g_1N\,(g_2N\,g_3N)$; *identity*, $(eN)(gN) = gN = (gN)(eN)$; *inverses*, $(gN)(g^{-1}N) = eN = (g^{-1}N)(gN)$. The count is the definition of the index together with Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

^pf-40-1

*Uses:* [[§37 Multiplying Cosets#^prop-37-1|§37.1]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]], [[§29 The Index and Lagrange's Theorem#^def-29-1|Def. §29.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!remark]- Connections
> - Vector-space version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|Quotient space is a vector space]].

> [!theorem] Proposition §40.2: Every Normal Subgroup Is a Kernel
> Let $N \trianglelefteq G$. The canonical projection $\pi: G \to G/N$, $g \mapsto gN$, is a surjective homomorphism with $\operatorname{Ker}\pi = N$.
>
> *Source: lecture*

^prop-40-2

> [!proof]+ Proof
> $\pi(g_1g_2) = g_1g_2N = (g_1N)(g_2N) = \pi(g_1)\pi(g_2)$ by the definition of the operation; $\pi$ is surjective by construction. The identity of $G/N$ is $N$, so $\operatorname{Ker}\pi = \{g : gN = N\} = \{g : g \in N\} = N$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]).

^pf-40-2

*Uses:* [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§15 Homomorphisms#^def-15-2|Def. §15.2]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]]

> [!remark]- Connections
> - Vector-space version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|Quotient map, π]] ($\operatorname{null}\pi = U$, shown in the proof of [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|Dimension of quotient space]]); in 590 stated in [[§21 Algebra Prerequisites꞉ Groups#^def-21-new3|Quotient Group]].

> [!remark] Remark: Kernels and Normal Subgroups Are the Same Thing
> Together with [[§39 Sources of Normal Subgroups#^prop-39-2|Kernels Are Normal]], the proposition says: the normal subgroups of $G$ are exactly the kernels of homomorphisms out of $G$. This is why normality, a condition that looks technical, is the natural one.

^rem-40-2

> [!example] Example §40.1: Quotient Groups
> 1. $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the (normal, since $\mathbb{Z}$ is abelian) subgroup $n\mathbb{Z}$: its elements are the cosets $a + n\mathbb{Z} = [a]$, and coset addition is the addition of residue classes of [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]. The notation of [[· 2 Arithmetic Modulo n|Chapter 2]] is thus an instance of the general one.
> 2. $G/G$ is the trivial group, and $G/\{e\} \cong G$ via $g\{e\} \mapsto g$.
> 3. $S_3/A_3$ has two elements, $A_3$ and $(1\,2)A_3$; it is cyclic of order $2$.

^ex-40-1

![[m493-37-1.svg]]
*Part 1 of the example with $n = 3$: the canonical projection $\pi: \mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$ collapses each coset $a + 3\mathbb{Z}$ (one colour each) to a single element $[a]$ of the quotient group. The grey arrows show adding $[1]$: $[0] \to [1] \to [2] \to [0]$.*

> [!remark]- Connections
> - 590 version of (1): [[§21 Algebra Prerequisites꞉ Groups#^ex-21-7|Example §21.7]].

## Computing with Representatives

*Source: Lecture (Fri Oct 2).*

> [!definition] Definition §40.2: Set of Representatives
> Let $N \trianglelefteq G$ ([[§38 Normal Subgroups#^def-38-1|Def. §38.1]]). A **set of representatives** for $G/N$ ([[§40 Quotient Groups#^def-40-1|Def. §40.1]]) is a subset $S \subseteq G$ such that every [[§28 Left and Right Cosets#^def-28-2|coset]] $C \in G/N$ contains exactly one $s \in S$, i.e. $C = sN$ for a unique $s \in S$. Equivalently, $G = \bigsqcup_{s \in S} sN$, where $Z = X \sqcup Y$ means $Z = X \cup Y$ and $X \cap Y = \varnothing$. Then $s \mapsto sN$ is a bijection $S \to G/N$, so the elements of $G/N$ can be named by the elements of $S$.
>
> *Source: lecture 10/2*

^def-40-2

> [!theorem] Proposition §40.3: Multiplying Through Representatives
> Let $S$ be a [[§40 Quotient Groups#^def-40-2|set of representatives]] for $G/N$. For $s_1, s_2 \in S$, write $s_1s_2 = s_3\,n$ with $s_3 \in S$ and $n \in N$; such $s_3$ and $n$ exist and are unique. Then $(s_1N)(s_2N) = s_3N$. In words: to multiply two representatives in $G/N$, multiply them in $G$ and replace the result by the representative of its coset.
>
> *Source: lecture 10/2*

^prop-40-3

> [!proof]+ Proof
> The coset $s_1s_2N$ contains exactly one $s_3 \in S$, and $s_3 \in s_1s_2N$ means $s_1s_2N = s_3N$, i.e. $n := s_3^{-1}s_1s_2 \in N$ and $s_1s_2 = s_3n$. Then $(s_1N)(s_2N) = s_1s_2N = s_3nN = s_3N$.

^pf-40-3

*Uses:* [[§40 Quotient Groups#^def-40-2|Def. §40.2]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]]

> [!remark]- Connections
> - 590 version: [[§21 Algebra Prerequisites꞉ Groups#^rem-21-19|multiply representatives, take the coset]] (590 §21).
> - Vector-space version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|Addition and scalar multiplication on V∕U]] (LADR 3.102).

> [!example] Example §40.2: $(\mathbb{Z}/4\mathbb{Z})/(2\mathbb{Z}/4\mathbb{Z})$
> Let $G = \mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ and $N = 2\mathbb{Z}/4\mathbb{Z} = \{0, 2\}$, so $G = \{0, 2\} \sqcup \{1, 3\}$, with [[§40 Quotient Groups#^def-40-2|representatives]] $S = \{0, 1\}$. The only sum that leaves $S$ is $1 + 1 = 2$, which lies in the coset of $0$:
>
> $$ \begin{array}{c|cc} + & 0 & 1 \\ \hline 0 & 0 & 1 \\ 1 & 1 & 0 \end{array} $$
>
> So the quotient is [[§4 Subgroups#^def-4-5|cyclic]] of order $2$. Here $S$ is not a [[§4 Subgroups#^def-4-1|subgroup]] ($1 + 1 \notin S$).
>
> *Source: lecture 10/2*

^ex-40-2

> [!example] Example §40.3: $S_3/A_3$
> $S_3 = \{e, (1\,2\,3), (1\,3\,2)\} \sqcup \{(1\,2), (1\,3), (2\,3)\} = A_3 \sqcup (2\,3)A_3$. With [[§40 Quotient Groups#^def-40-2|representatives]] $S = \{e, (2\,3)\}$, and $(2\,3)(2\,3) = e$,
>
> $$ \begin{array}{c|cc} \cdot & e & (2\,3) \\ \hline e & e & (2\,3) \\ (2\,3) & (2\,3) & e \end{array} $$
>
> This time no product leaves $S$, because $S$ is a [[§4 Subgroups#^def-4-1|subgroup]].
>
> *Source: lecture 10/2*

^ex-40-3

![[m493-37-2.svg]]
*Computing in $G/N$ through a [[§40 Quotient Groups#^def-40-2|set of representatives]] $S$ (blue strip: one blue element in each coset box). (a) [[§40 Quotient Groups#^ex-40-2|Ex. §40.2]]: $G = \mathbb{Z}/4\mathbb{Z}$ splits into the cosets $0 + N = \{0, 2\}$ and $1 + N = \{1, 3\}$, with $S = \{0, 1\}$; the pair $(1, 1)$ is added in $G$ (red arrow) and lands on $2$, outside $S$ but in the box of $0$, so it is replaced by the representative $0$ (dashed arrow). This is [[§40 Quotient Groups#^prop-40-3|§40.3]] with $1 + 1 = 0 + 2$, i.e. $s_3 = 0$, $n = 2$; and since $1 + 1 \notin S$, $S$ is not a subgroup. (b) [[§40 Quotient Groups#^ex-40-3|Ex. §40.3]]: $S_3 = A_3 \sqcup (2\,3)A_3$ with $S = \{e, (2\,3)\}$; the product $(2\,3)(2\,3) = e$ (red arrow) lands directly on a representative, as every product of elements of $S$ does because $S$ is a subgroup (green line), so $S \cong S_3/A_3$ by [[§40 Quotient Groups#^prop-40-4|§40.4]]. (Drawn for these notes in the vault; not in the course tex.)*

> [!theorem] Proposition §40.4: Representatives Forming a Subgroup
> Let $S$ be a [[§40 Quotient Groups#^def-40-2|set of representatives]] for $G/N$ that is also a [[§4 Subgroups#^def-4-1|subgroup]] of $G$. Then $S \cap N = \{e\}$, and the composite $S \hookrightarrow G \twoheadrightarrow G/N$, $s \mapsto sN$, is an [[§16 Isomorphisms#^def-16-1|isomorphism]]. So $G/N \cong S$, and products in $G/N$ can be computed inside $S$.
>
> *Source: lecture 10/2*

^prop-40-4

> [!proof]+ Proof
> The composite is the restriction of the projection $\pi$ ([[§40 Quotient Groups#^prop-40-2|§40.2]]) to $S$, hence a homomorphism. The fibres of $\pi$ are the cosets of $N$, and $S$ contains exactly one element of each, so the composite is a bijection. For $S \cap N$: $N = eN$ is a coset, and $e \in S$ because $S$ is a subgroup; by uniqueness $e$ is the only element of $S$ in $N$. (This is also the special case $H = S$ of the [[§41 The First and Second Isomorphism Theorems#^thm-41-4|Second Isomorphism Theorem]], §41.4.)

^pf-40-4

*Uses:* [[§40 Quotient Groups#^prop-40-2|§40.2]], [[§40 Quotient Groups#^def-40-2|Def. §40.2]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - Re-proved from the Second Isomorphism Theorem: [[§41 The First and Second Isomorphism Theorems#^cor-41-7|Subgroup Representatives, Again]] (§41.7).
> - Vector-space analogue: a complement $W$ of $U$ ([[§5 Bases#^ladr-2-33|LADR 2.33]]) plays the role of $S$, with $V/U \cong W$; for groups such a subgroup need not exist ([[§40 Quotient Groups#^rem-40-3|Remark]] below).

> [!remark] Remark: Life Is Especially Nice When $S$ Is a Subgroup
> In $S_3/A_3$ ([[§40 Quotient Groups#^ex-40-3|Ex. §40.3]]) the representatives $\{e, (2\,3)\}$ form a subgroup, so $S_3/A_3 \cong \langle (2\,3) \rangle$ ([[§40 Quotient Groups#^prop-40-4|§40.4]]). In $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ ([[§40 Quotient Groups#^ex-40-2|Ex. §40.2]]) no choice works: a subgroup set of representatives would have order $2$, and the only subgroup of order $2$ is $\{0, 2\} = N$ itself, which lies in a single coset. The quotient is still $\cong \mathbb{Z}/2\mathbb{Z}$; it just is not realized by a subgroup of $\mathbb{Z}/4\mathbb{Z}$.

^rem-40-3
