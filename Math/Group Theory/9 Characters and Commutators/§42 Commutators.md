---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 42
tags: [group-theory, math493]
---
← [[§41 Characters]] · ↑ [[· 9 Characters and Commutators]]

*Reference: Pinter Ch. 15 (commutators).*

> [!definition] Definition §42.1: Commutator
> An element $h \in G$ is a **commutator** if $h = g_1 g_2 g_1^{-1} g_2^{-1}$ for some $g_1, g_2 \in G$. The identity is always a commutator (take $g_1 = g_2 = e$), and $G$ is abelian if and only if $e$ is the only commutator.

^def-42-1

> [!theorem] Proposition §42.1: Characters Kill Commutators
> Let $\chi: G \to A$ be a character and $h \in G$ a commutator. Then $\chi(h) = e_A$.
>
> *Source: PS 2.4(2)*

^prop-42-1

> [!proof]+ Proof
> Write $h = g_1g_2g_1^{-1}g_2^{-1}$. Since $\chi$ is a homomorphism and $A$ is abelian,
>
> $$ \chi(h) = \chi(g_1)\chi(g_2)\chi(g_1^{-1})\chi(g_2^{-1}) = \chi(g_1)\chi(g_1^{-1})\,\chi(g_2)\chi(g_2^{-1}) = \chi(g_1g_1^{-1})\,\chi(g_2g_2^{-1}) = \chi(e)\chi(e) = e_A. $$

^pf-42-1

*Uses:* [[§41 Characters#^def-41-1|Def. §41.1]], [[§42 Commutators#^def-42-1|Def. §42.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: The Contrapositive as a Tool
> This gives a practical test: to show an element $h$ is *not* a commutator, exhibit one character $\chi$ with $\chi(h) \neq e_A$. [[§42 Commutators#^prop-42-3|PS 2.4(4)]] below is exactly this, with $\chi = \operatorname{sgn}$.

^rem-42-1

> [!theorem] Proposition §42.2: $3$-Cycles Are Commutators
> Let $n \geq 3$ and let $c = (i\,j\,k) \in S_n$ with $i, j, k$ distinct. Then $c$ is a commutator: with $g_1 = (j\,k)$ and $g_2 = (i\,j)$,
>
> $$ g_1 g_2 g_1^{-1} g_2^{-1} = (j\,k)(i\,j)(j\,k)(i\,j) = (i\,j\,k). $$
>
> *Source: PS 2.4(3)*

^prop-42-2

> [!proof]+ Proof
> Transpositions are their own inverses, so $g_1^{-1} = g_1$ and $g_2^{-1} = g_2$ and the displayed product is $g_1g_2g_1^{-1}g_2^{-1}$. To evaluate it, first note $(j\,k)(i\,j) = (i\,k\,j)$: applying the right factor first,
>
> $$ i \mapsto j \mapsto k, \qquad j \mapsto i \mapsto i, \qquad k \mapsto k \mapsto j, $$
>
> so the product sends $i \mapsto k \mapsto j \mapsto i$, which is $(i\,k\,j)$. Hence
>
> $$ (j\,k)(i\,j)(j\,k)(i\,j) = (i\,k\,j)^2 = (i\,k\,j)^{-1} = (i\,j\,k), $$
>
> using that a $3$-cycle $\gamma$ satisfies $\gamma^3 = e$, so $\gamma^2 = \gamma^{-1}$, and that reversing the loop of $(i\,k\,j)$ gives $(i\,j\,k)$.

^pf-42-2

*Uses:* [[§42 Commutators#^def-42-1|Def. §42.1]], [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex. §12.1]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]

![[m493-41-1.svg]]
*The commutator of §42.2 as a wiring diagram, read left to right in the order the factors act (right to left in the product $g_1g_2g_1^{-1}g_2^{-1}$). Following each strand through the four swaps: $i$ ends at $j$ (blue), $j$ at $k$ (red), $k$ at $i$ (green). The result is the $3$-cycle $(i\,j\,k)$.*

> [!theorem] Proposition §42.3: Transpositions Are Not Commutators
> Let $n \geq 2$ and let $s = (i\,j) \in S_n$ with $i \neq j$. Then $s$ is not a commutator.
>
> *Source: PS 2.4(4)*

^prop-42-3

> [!proof]+ Proof
> The sign $\operatorname{sgn}: S_n \to \{\pm 1\}$ is a character (the target is abelian). By [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], $\operatorname{sgn}(s) = \det M(s) = -1$, since $M(s)$ is the identity matrix with two columns interchanged. If $s$ were a commutator, [[§42 Commutators#^prop-42-1|Characters Kill Commutators]] would force $\operatorname{sgn}(s) = 1$, a contradiction.

^pf-42-3

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|Def. §20.2]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§34 Determinants#^ladr-9-57|LADR 9.57]], [[§42 Commutators#^prop-42-1|§42.1]]

> [!definition] Definition §42.2: Commutator Subgroup
> The **commutator subgroup** of $G$, written $[G,G]$ ([[493 Problem Set 4#^hw-4-4|PS 4.4]] writes $D(G)$), is the [[§4 Subgroups#^def-4-4|subgroup generated]] by all [[§42 Commutators#^def-42-1|commutators]] $aba^{-1}b^{-1}$, $a, b \in G$. (A product of commutators need not itself be a commutator, which is why the generated subgroup is taken.)

^def-42-2

> [!theorem] Proposition §42.4: Properties of the Commutator Subgroup
> 1. $[G,G]$ is a normal subgroup of $G$ ([[· 8 Normal Subgroups and Quotient Groups|Chapter 8]]).
> 2. Every character $\chi: G \to A$ is trivial on $[G,G]$, i.e. $[G,G] \subseteq \operatorname{Ker}\chi$.
> 3. $[G,G] = \{e\}$ if and only if $G$ is abelian.
>
> *Source: (1) is PS 4.4(1)*

^prop-42-4

> [!proof]+ Proof
> **(1)** Conjugation carries commutators to commutators:
>
> $$ g\,(aba^{-1}b^{-1})\,g^{-1} = (gag^{-1})(gbg^{-1})(gag^{-1})^{-1}(gbg^{-1})^{-1}. $$
>
> The inverse of a commutator is a commutator, $(aba^{-1}b^{-1})^{-1} = bab^{-1}a^{-1}$, so every element of $[G,G]$ is a product of commutators $c_1 \cdots c_m$, and since [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|conjugation is a homomorphism]],
>
> $$ g(c_1 \cdots c_m)g^{-1} = (gc_1g^{-1}) \cdots (gc_mg^{-1}) \in [G,G]. $$
>
> **(2)** $\chi$ kills every commutator ([[§42 Commutators#^prop-42-1|Characters Kill Commutators]]), and $\operatorname{Ker}\chi$ is a subgroup, so it contains the subgroup they generate. **(3)** $G$ is abelian iff every commutator equals $e$, iff $[G,G] = \{e\}$.

^pf-42-4

*Uses:* [[§42 Commutators#^def-42-2|Def. §42.2]], [[§4 Subgroups#^def-4-4|Def. §4.4]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§35 Normal Subgroups#^def-35-1|Def. §35.1]], [[§42 Commutators#^prop-42-1|§42.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§42 Commutators#^def-42-1|Def. §42.1]]

> [!theorem] Theorem §42.5: The Commutator Subgroup and Characters of $S_n$
> For $n \geq 2$, $[S_n, S_n] = A_n$. Consequently every [[§41 Characters#^def-41-1|character]] $\chi: S_n \to A$ is trivial on $A_n$ and is determined by its value $c = \chi(\tau)$ on any transposition $\tau$, which satisfies $c^2 = e_A$: $\chi(\sigma) = e_A$ for even $\sigma$ and $\chi(\sigma) = c$ for odd $\sigma$.
>
> *Source: PS 4.5*

^thm-42-5

> [!proof]+ Proof
> ($\subseteq$) The sign $\operatorname{sgn}$ is a character, so by (2) ([[§42 Commutators#^prop-42-4|§42.4]]) $[S_n, S_n] \subseteq \operatorname{Ker}\operatorname{sgn} = A_n$. ($\supseteq$) For $n = 2$, $A_2 = \{e\}$. For $n \geq 3$, $A_n$ is generated by $3$-cycles ([[§20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]]), each of which is a commutator ([[§42 Commutators#^prop-42-2|§42.2]]); so $A_n \subseteq [S_n, S_n]$. For the consequence: $\chi$ is trivial on $[S_n, S_n] = A_n$ by (2). All transpositions are conjugate ([[§31 Conjugacy Classes#^prop-31-2|§31.2]]), so $\chi$ takes a single value $c$ on them ([[§41 Characters#^prop-41-1|Characters Are Constant on Conjugacy Classes]]), and $c^2 = \chi(\tau^2) = \chi(e) = e_A$. An odd $\sigma$ equals $\tau(\tau\sigma)$ with $\tau\sigma$ even, so $\chi(\sigma) = \chi(\tau)\chi(\tau\sigma) = c$.
>
> *Direct proof of the consequence ([[493 Problem Set 4#^hw-4-5|PS 4.5]]).* Let $a = \chi((1\,2))$. **(1)** For a transposition $(i\,j)$, choose $\sigma \in S_n$ with $\sigma(i) = 1$, $\sigma(j) = 2$, mapping the remaining $n - 2$ points bijectively onto the remaining $n - 2$ points. By [[§31 Conjugacy Classes#^lem-31-1|Conjugation Relabels the Entries]] (§31), $\sigma(i\,j)\sigma^{-1} = (1\,2)$, so, $A$ being abelian, $a = \chi(\sigma)\chi((i\,j))\chi(\sigma)^{-1} = \chi((i\,j))$. **(2)** $a^2 = \chi((1\,2)^2) = \chi(e) = e_A$. **(3)** Write $\sigma = t_1 \cdots t_k$ with each $t_i$ of the form $(1\,j)$ (Generators of $S_n$, [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]]). Then $\operatorname{sgn}(\sigma) = (-1)^k$ ([[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]]), so $\sigma \in A_n$ iff $k$ is even, while $\chi(\sigma) = a^k$, which by (2) is $e_A$ for even $k$ and $a$ for odd $k$.

^pf-42-5

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]], [[§42 Commutators#^prop-42-4|§42.4]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]], [[§42 Commutators#^prop-42-2|§42.2]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§31 Conjugacy Classes#^prop-31-2|§31.2]], [[§41 Characters#^prop-41-1|§41.1]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§41 Characters#^def-41-1|Def. §41.1]], [[§31 Conjugacy Classes#^lem-31-1|§31.1]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: What the Theorem Says About $S_n$
> In $S_n$ all $3$-cycles are commutators and no transposition is, and [[§42 Commutators#^thm-42-5|the theorem]] shows that characters of $S_n$ can only distinguish even from odd permutations: $\operatorname{sgn}$ is essentially the only nontrivial one.

^rem-42-2

> [!definition] Definition §42.3: Abelianization
> The **abelianization** of $G$ is the [[§37 Quotient Groups#^def-37-1|quotient group]] $G^{\mathrm{ab}} := G/[G,G]$, defined because $[G,G]$ is normal ([[§42 Commutators#^prop-42-4|Properties of the Commutator Subgroup]]).
>
> *Source: PS 4.4*

^def-42-3

> [!remark]- Connections
> - In 590, forcing commutativity is the quotient $F_2 \to \mathbb{Z} \times \mathbb{Z}$: [[§21 Algebra Prerequisites꞉ Groups#^ex-21-8|Forcing Commutativity]], [[§21 Algebra Prerequisites꞉ Groups#^rem-21-12|The Hierarchy of Relations]], and “Abelianization” in [[§21 Algebra Prerequisites꞉ Groups#^rem-21-14|Simplifying Presentations]].

> [!theorem] Proposition §42.6: The Abelianization Is Abelian
> $G/[G,G]$ is abelian.
>
> *Source: PS 4.4(2)*

^prop-42-6

> [!proof]+ Proof
> Let $N = [G,G]$. For $a, b \in G$, $(aN)(bN)(aN)^{-1}(bN)^{-1} = aba^{-1}b^{-1}N = N$, since the commutator $aba^{-1}b^{-1}$ lies in $N$. So $(aN)(bN) = (bN)(aN)$.
>
> *Second proof, by the coset criterion ([[493 Problem Set 4#^hw-4-4|PS 4.4(2)]]).* For $x, y \in G$, $xN = yN$ iff $x^{-1}y \in N$ ([[§26 Left and Right Cosets#^prop-26-2|§26.2]]). With $x = ab$ and $y = ba$, $x^{-1}y = b^{-1}a^{-1}ba$, which is the [[§42 Commutators#^def-42-1|commutator]] of the pair $(b^{-1}, a^{-1})$ and so lies in $N$. Hence $(ab)N = (ba)N$, i.e. $(aN)(bN) = (bN)(aN)$.

^pf-42-6

*Uses:* [[§37 Quotient Groups#^def-37-1|Def. §37.1]], [[§37 Quotient Groups#^thm-37-1|§37.1]], [[§26 Left and Right Cosets#^prop-26-2|§26.2]], [[§42 Commutators#^def-42-2|Def. §42.2]], [[§26 Left and Right Cosets#^def-26-1|Def. §26.1]], [[§42 Commutators#^def-42-1|Def. §42.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!example] Example §42.1: The Abelianization of $S_n$
> For $n \geq 2$, $S_n/[S_n, S_n] = S_n/A_n \cong \{\pm 1\}$: by The Commutator Subgroup and Characters of $S_n$ ([[§42 Commutators#^thm-42-5|§42.5]]), $[S_n, S_n] = A_n$, and the [[§38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]] applied to the surjective homomorphism $\operatorname{sgn}$, whose kernel is $A_n$, gives $S_n/A_n \cong \{\pm 1\}$ ([[§38 The First Isomorphism Theorem#^ex-38-1|Ex. §38.1]]).
>
> *Source: not from class*

^ex-42-1

> [!theorem] Corollary §42.7: Every Square Root of $e_A$ Gives a Character
> Let $n \geq 2$ and let $A$ be abelian. For each $a \in A$ with $a^2 = e_A$, the map
>
> $$ \chi_a(\sigma) = \begin{cases} e_A & \sigma \in A_n, \\ a & \sigma \notin A_n \end{cases} $$
>
> is a [[§41 Characters#^def-41-1|character]] of $S_n$, and $a \mapsto \chi_a$ is a bijection from $\{a \in A : a^2 = e_A\}$ onto the set of characters $S_n \to A$, with inverse $\chi \mapsto \chi((1\,2))$.
>
> *Source: not from class*

^cor-42-7

> [!proof]+ Proof
> Define $\iota_a: \{\pm 1\} \to A$ by $\iota_a(1) = e_A$ and $\iota_a(-1) = a$. It is a homomorphism: the only product to check is $\iota_a((-1)(-1)) = \iota_a(1) = e_A = a^2 = \iota_a(-1)\iota_a(-1)$. So $\chi_a = \iota_a \circ \operatorname{sgn}$ is a homomorphism, and $\chi_a((1\,2)) = a$. Conversely, by The Commutator Subgroup and Characters of $S_n$ ([[§42 Commutators#^thm-42-5|§42.5]]), every character $\chi$ equals $\chi_a$ for $a = \chi((1\,2))$, which satisfies $a^2 = e_A$. So the two assignments are mutually inverse.

^pf-42-7

*Uses:* [[§41 Characters#^def-41-1|Def. §41.1]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§42 Commutators#^thm-42-5|§42.5]]

> [!remark] Remark: The Characters of $S_n$, Completely
> [[§42 Commutators#^thm-42-5|PS 4.5]] shows every character of $S_n$ is “trivial or the sign in disguise”; [[§42 Commutators#^cor-42-7|the corollary]] shows every such candidate actually occurs. For $A = \mathbb{C}^\times$ ([[§3 Basic Examples of Groups#^def-3-4|Def. §3.4]]) the square roots of $1$ are $\pm 1$, so $S_n$ ($n \geq 2$) has exactly two characters with values in $\mathbb{C}^\times$: the trivial one and $\operatorname{sgn}$ ([[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|Def. §20.2]]).

^rem-42-3

> [!theorem] Proposition §42.8: Normal Subgroups with Trivial Intersection Commute
> Let $M$ and $N$ be [[§35 Normal Subgroups#^def-35-1|normal subgroups]] of $G$ with $M \cap N = \{e\}$. Then $mn = nm$ for all $m \in M$ and $n \in N$.
>
> *Source: PS 4.2*

^prop-42-8

> [!proof]+ Proof
> Let $x = mnm^{-1}n^{-1}$. Grouping as $x = (mnm^{-1})\,n^{-1}$: $mnm^{-1} \in N$ because $N$ is normal, and $n^{-1} \in N$, so $x \in N$. Grouping as $x = m\,(nm^{-1}n^{-1})$: $nm^{-1}n^{-1} \in M$ because $M$ is normal, and $m \in M$, so $x \in M$. Hence $x \in M \cap N = \{e\}$, i.e. $mnm^{-1}n^{-1} = e$, and then
>
> $$ mn = mn\,(m^{-1}n^{-1}nm) = (mnm^{-1}n^{-1})\,nm = nm. $$

^pf-42-8

*Uses:* [[§35 Normal Subgroups#^def-35-1|Def. §35.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!remark] Remark: Commutators of Normal Subgroups
> [[§42 Commutators#^pf-42-8|The proof]] shows more: for normal $M, N$, every [[§42 Commutators#^def-42-1|commutator]] $mnm^{-1}n^{-1}$ with $m \in M$, $n \in N$ lies in $M \cap N$. When $M \cap N = \{e\}$, elements of $M$ commute with elements of $N$; this is the first step toward recognizing $G$ as a [[§3 Basic Examples of Groups#^def-3-2|direct product]] $M \times N$ when also $MN = G$ ([[§39 The Second and Third Isomorphism Theorems#^def-39-1|Def. §39.1]]) (not from class).

^rem-42-4
