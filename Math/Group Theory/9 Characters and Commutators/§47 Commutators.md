---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 47
tags: [group-theory, math493]
---
← [[§46 Characters]] · ↑ [[· 9 Characters and Commutators]] · [[§48 S₃, Aₙ and GLₙ]] →

*Reference: Pinter Ch. 15 (commutators).*

> [!definition] Definition §47.1: Commutator
> An element $h \in G$ is a **commutator** if $h = g_1 g_2 g_1^{-1} g_2^{-1}$ for some $g_1, g_2 \in G$. The identity is always a commutator (take $g_1 = g_2 = e$), and $G$ is abelian if and only if $e$ is the only commutator.

^def-47-1

> [!theorem] Proposition §47.1: Characters Kill Commutators
> Let $\chi: G \to A$ be a character and $h \in G$ a commutator. Then $\chi(h) = e_A$.
>
> *Source: PS 2.4(2)*

^prop-47-1

> [!proof]+ Proof
> Write $h = g_1g_2g_1^{-1}g_2^{-1}$. Since $\chi$ is a homomorphism and $A$ is abelian,
>
> $$ \chi(h) = \chi(g_1)\chi(g_2)\chi(g_1^{-1})\chi(g_2^{-1}) = \chi(g_1)\chi(g_1^{-1})\,\chi(g_2)\chi(g_2^{-1}) = \chi(g_1g_1^{-1})\,\chi(g_2g_2^{-1}) = \chi(e)\chi(e) = e_A. $$

^pf-47-1

*Uses:* [[§46 Characters#^def-46-1|Def. §46.1]], [[§47 Commutators#^def-47-1|Def. §47.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: The Contrapositive as a Tool
> This gives a practical test: to show an element $h$ is *not* a commutator, exhibit one character $\chi$ with $\chi(h) \neq e_A$. [[§47 Commutators#^prop-47-3|PS 2.4(4)]] below is exactly this, with $\chi = \operatorname{sgn}$.

^rem-47-1

> [!theorem] Proposition §47.2: $3$-Cycles Are Commutators
> Let $n \geq 3$ and let $c = (i\,j\,k) \in S_n$ with $i, j, k$ distinct. Then $c$ is a commutator: with $g_1 = (j\,k)$ and $g_2 = (i\,j)$,
>
> $$ g_1 g_2 g_1^{-1} g_2^{-1} = (j\,k)(i\,j)(j\,k)(i\,j) = (i\,j\,k). $$
>
> *Source: PS 2.4(3)*

^prop-47-2

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

^pf-47-2

*Uses:* [[§47 Commutators#^def-47-1|Def. §47.1]], [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex. §12.1]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]

![[m493-41-1.svg]]
*The commutator of §46.2 as a wiring diagram, read left to right in the order the factors act (right to left in the product $g_1g_2g_1^{-1}g_2^{-1}$). Following each strand through the four swaps: $i$ ends at $j$ (blue), $j$ at $k$ (red), $k$ at $i$ (green). The result is the $3$-cycle $(i\,j\,k)$.*

> [!theorem] Proposition §47.3: Transpositions Are Not Commutators
> Let $n \geq 2$ and let $s = (i\,j) \in S_n$ with $i \neq j$. Then $s$ is not a commutator.
>
> *Source: PS 2.4(4)*

^prop-47-3

> [!proof]+ Proof
> The sign $\operatorname{sgn}: S_n \to \{\pm 1\}$ is a character (the target is abelian). By [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], $\operatorname{sgn}(s) = \det M(s) = -1$, since $M(s)$ is the identity matrix with two columns interchanged. If $s$ were a commutator, [[§47 Commutators#^prop-47-1|Characters Kill Commutators]] would force $\operatorname{sgn}(s) = 1$, a contradiction.

^pf-47-3

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def. §21.2]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§37 Determinants#^ladr-9-57|LADR 9.57]], [[§47 Commutators#^prop-47-1|§47.1]]

> [!definition] Definition §47.2: Commutator Subgroup
> The **commutator subgroup** of $G$, written $[G,G]$ ([[493 Problem Set 4#^hw-4-4|PS 4.4]] writes $D(G)$), is the [[§4 Subgroups#^def-4-5|subgroup generated]] by all [[§47 Commutators#^def-47-1|commutators]] $aba^{-1}b^{-1}$, $a, b \in G$. (A product of commutators need not itself be a commutator, which is why the generated subgroup is taken.)

^def-47-2

> [!theorem] Proposition §47.4: Properties of the Commutator Subgroup
> 1. $[G,G]$ is a normal subgroup of $G$ ([[· 8 Normal Subgroups and Quotient Groups|Chapter 8]]).
> 2. Every character $\chi: G \to A$ is trivial on $[G,G]$, i.e. $[G,G] \subseteq \operatorname{Ker}\chi$.
> 3. $[G,G] = \{e\}$ if and only if $G$ is abelian.
>
> *Source: (1) is PS 4.4(1), WS 9.4*

^prop-47-4

> [!proof]+ Proof
> **(1)** Conjugation carries commutators to commutators:
>
> $$ g\,(aba^{-1}b^{-1})\,g^{-1} = (gag^{-1})(gbg^{-1})(gag^{-1})^{-1}(gbg^{-1})^{-1}. $$
>
> The inverse of a commutator is a commutator, $(aba^{-1}b^{-1})^{-1} = bab^{-1}a^{-1}$, so every element of $[G,G]$ is a product of commutators $c_1 \cdots c_m$, and since [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|conjugation is a homomorphism]],
>
> $$ g(c_1 \cdots c_m)g^{-1} = (gc_1g^{-1}) \cdots (gc_mg^{-1}) \in [G,G]. $$
>
> **(2)** $\chi$ kills every commutator ([[§47 Commutators#^prop-47-1|Characters Kill Commutators]]), and $\operatorname{Ker}\chi$ is a subgroup, so it contains the subgroup they generate. **(3)** $G$ is abelian iff every commutator equals $e$, iff $[G,G] = \{e\}$.

^pf-47-4

*Uses:* [[§47 Commutators#^def-47-2|Def. §47.2]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§47 Commutators#^prop-47-1|§47.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§47 Commutators#^def-47-1|Def. §47.1]]

> [!theorem] Theorem §47.5: The Commutator Subgroup and Characters of $S_n$
> For $n \geq 2$, $[S_n, S_n] = A_n$. Consequently every [[§46 Characters#^def-46-1|character]] $\chi: S_n \to A$ is trivial on $A_n$ and is determined by its value $c = \chi(\tau)$ on any transposition $\tau$, which satisfies $c^2 = e_A$: $\chi(\sigma) = e_A$ for even $\sigma$ and $\chi(\sigma) = c$ for odd $\sigma$.
>
> *Source: PS 4.5*

^thm-47-5

> [!proof]+ Proof
> ($\subseteq$) The sign $\operatorname{sgn}$ is a character, so by (2) ([[§47 Commutators#^prop-47-4|§47.4]]) $[S_n, S_n] \subseteq \operatorname{Ker}\operatorname{sgn} = A_n$. ($\supseteq$) For $n = 2$, $A_2 = \{e\}$. For $n \geq 3$, $A_n$ is generated by $3$-cycles ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]]), each of which is a commutator ([[§47 Commutators#^prop-47-2|§47.2]]); so $A_n \subseteq [S_n, S_n]$. For the consequence: $\chi$ is trivial on $[S_n, S_n] = A_n$ by (2). All transpositions are conjugate ([[§33 Conjugacy Classes#^prop-33-2|§33.2]]), so $\chi$ takes a single value $c$ on them ([[§46 Characters#^prop-46-1|Characters Are Constant on Conjugacy Classes]]), and $c^2 = \chi(\tau^2) = \chi(e) = e_A$. An odd $\sigma$ equals $\tau(\tau\sigma)$ with $\tau\sigma$ even, so $\chi(\sigma) = \chi(\tau)\chi(\tau\sigma) = c$.
>
> *Direct proof of the consequence ([[493 Problem Set 4#^hw-4-5|PS 4.5]]).* Let $a = \chi((1\,2))$. **(1)** For a transposition $(i\,j)$, choose $\sigma \in S_n$ with $\sigma(i) = 1$, $\sigma(j) = 2$, mapping the remaining $n - 2$ points bijectively onto the remaining $n - 2$ points. By [[§33 Conjugacy Classes#^lem-33-1|Conjugation Relabels the Entries]] (§33), $\sigma(i\,j)\sigma^{-1} = (1\,2)$, so, $A$ being abelian, $a = \chi(\sigma)\chi((i\,j))\chi(\sigma)^{-1} = \chi((i\,j))$. **(2)** $a^2 = \chi((1\,2)^2) = \chi(e) = e_A$. **(3)** Write $\sigma = t_1 \cdots t_k$ with each $t_i$ of the form $(1\,j)$ (Generators of $S_n$, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]]). Then $\operatorname{sgn}(\sigma) = (-1)^k$ ([[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]]), so $\sigma \in A_n$ iff $k$ is even, while $\chi(\sigma) = a^k$, which by (2) is $e_A$ for even $k$ and $a$ for odd $k$.

^pf-47-5

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§47 Commutators#^prop-47-4|§47.4]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]], [[§47 Commutators#^prop-47-2|§47.2]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§33 Conjugacy Classes#^prop-33-2|§33.2]], [[§46 Characters#^prop-46-1|§46.1]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§46 Characters#^def-46-1|Def. §46.1]], [[§33 Conjugacy Classes#^lem-33-1|§33.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: What the Theorem Says About $S_n$
> In $S_n$ all $3$-cycles are commutators and no transposition is, and [[§47 Commutators#^thm-47-5|the theorem]] shows that characters of $S_n$ can only distinguish even from odd permutations: $\operatorname{sgn}$ is essentially the only nontrivial one.

^rem-47-2

> [!definition] Definition §47.3: Abelianization
> The **abelianization** of $G$ is the [[§40 Quotient Groups#^def-40-1|quotient group]] $G^{\mathrm{ab}} := G/[G,G]$, defined because $[G,G]$ is normal ([[§47 Commutators#^prop-47-4|Properties of the Commutator Subgroup]]).
>
> *Source: PS 4.4*

^def-47-3

> [!remark]- Connections
> - In 590, forcing commutativity is the quotient $F_2 \to \mathbb{Z} \times \mathbb{Z}$: [[§27 Free Groups and Presentations#^ex-27-6|Forcing Commutativity]], [[§27 Free Groups and Presentations#^rem-27-12|The Hierarchy of Relations]], and “Abelianization” in [[§27 Free Groups and Presentations#^rem-27-14|Simplifying Presentations]].

> [!theorem] Proposition §47.6: The Abelianization Is Abelian
> $G/[G,G]$ is abelian.
>
> *Source: PS 4.4(2); WS 9.5*

^prop-47-6

> [!proof]+ Proof
> Let $N = [G,G]$. For $a, b \in G$, $(aN)(bN)(aN)^{-1}(bN)^{-1} = aba^{-1}b^{-1}N = N$, since the commutator $aba^{-1}b^{-1}$ lies in $N$. So $(aN)(bN) = (bN)(aN)$.
>
> *Second proof, by the coset criterion ([[493 Problem Set 4#^hw-4-4|PS 4.4(2)]]).* For $x, y \in G$, $xN = yN$ iff $x^{-1}y \in N$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]). With $x = ab$ and $y = ba$, $x^{-1}y = b^{-1}a^{-1}ba$, which is the [[§47 Commutators#^def-47-1|commutator]] of the pair $(b^{-1}, a^{-1})$ and so lies in $N$. Hence $(ab)N = (ba)N$, i.e. $(aN)(bN) = (bN)(aN)$.

^pf-47-6

*Uses:* [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§47 Commutators#^def-47-2|Def. §47.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§47 Commutators#^def-47-1|Def. §47.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!example] Example §47.1: The Abelianization of $S_n$
> For $n \geq 2$, $S_n/[S_n, S_n] = S_n/A_n \cong \{\pm 1\}$: by The Commutator Subgroup and Characters of $S_n$ ([[§47 Commutators#^thm-47-5|§47.5]]), $[S_n, S_n] = A_n$, and the [[§41 The First and Second Isomorphism Theorems#^thm-41-1|First Isomorphism Theorem]] applied to the surjective homomorphism $\operatorname{sgn}$, whose kernel is $A_n$, gives $S_n/A_n \cong \{\pm 1\}$ ([[§41 The First and Second Isomorphism Theorems#^ex-41-1|Ex. §41.1]]).
>
> *Source: not from class*

^ex-47-1

> [!theorem] Corollary §47.7: Every Square Root of $e_A$ Gives a Character
> Let $n \geq 2$ and let $A$ be abelian. For each $a \in A$ with $a^2 = e_A$, the map
>
> $$ \chi_a(\sigma) = \begin{cases} e_A & \sigma \in A_n, \\ a & \sigma \notin A_n \end{cases} $$
>
> is a [[§46 Characters#^def-46-1|character]] of $S_n$, and $a \mapsto \chi_a$ is a bijection from $\{a \in A : a^2 = e_A\}$ onto the set of characters $S_n \to A$, with inverse $\chi \mapsto \chi((1\,2))$.
>
> *Source: not from class*

^cor-47-7

> [!proof]+ Proof
> Define $\iota_a: \{\pm 1\} \to A$ by $\iota_a(1) = e_A$ and $\iota_a(-1) = a$. It is a homomorphism: the only product to check is $\iota_a((-1)(-1)) = \iota_a(1) = e_A = a^2 = \iota_a(-1)\iota_a(-1)$. So $\chi_a = \iota_a \circ \operatorname{sgn}$ is a homomorphism, and $\chi_a((1\,2)) = a$. Conversely, by The Commutator Subgroup and Characters of $S_n$ ([[§47 Commutators#^thm-47-5|§47.5]]), every character $\chi$ equals $\chi_a$ for $a = \chi((1\,2))$, which satisfies $a^2 = e_A$. So the two assignments are mutually inverse.

^pf-47-7

*Uses:* [[§46 Characters#^def-46-1|Def. §46.1]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§47 Commutators#^thm-47-5|§47.5]]

> [!remark] Remark: The Characters of $S_n$, Completely
> [[§47 Commutators#^thm-47-5|PS 4.5]] shows every character of $S_n$ is “trivial or the sign in disguise”; [[§47 Commutators#^cor-47-7|the corollary]] shows every such candidate actually occurs. For $A = \mathbb{C}^\times$ ([[§3 Basic Examples of Groups#^def-3-4|Def. §3.4]]) the square roots of $1$ are $\pm 1$, so $S_n$ ($n \geq 2$) has exactly two characters with values in $\mathbb{C}^\times$: the trivial one and $\operatorname{sgn}$ ([[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def. §21.2]]).

^rem-47-3

> [!theorem] Proposition §47.8: Normal Subgroups with Trivial Intersection Commute
> Let $M$ and $N$ be [[§38 Normal Subgroups#^def-38-1|normal subgroups]] of $G$ with $M \cap N = \{e\}$. Then $mn = nm$ for all $m \in M$ and $n \in N$.
>
> *Source: PS 4.2*

^prop-47-8

> [!proof]+ Proof
> Let $x = mnm^{-1}n^{-1}$. Grouping as $x = (mnm^{-1})\,n^{-1}$: $mnm^{-1} \in N$ because $N$ is normal, and $n^{-1} \in N$, so $x \in N$. Grouping as $x = m\,(nm^{-1}n^{-1})$: $nm^{-1}n^{-1} \in M$ because $M$ is normal, and $m \in M$, so $x \in M$. Hence $x \in M \cap N = \{e\}$, i.e. $mnm^{-1}n^{-1} = e$, and then
>
> $$ mn = mn\,(m^{-1}n^{-1}nm) = (mnm^{-1}n^{-1})\,nm = nm. $$

^pf-47-8

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!remark] Remark: Commutators of Normal Subgroups
> [[§47 Commutators#^pf-47-8|The proof]] shows more: for normal $M, N$, every [[§47 Commutators#^def-47-1|commutator]] $mnm^{-1}n^{-1}$ with $m \in M$, $n \in N$ lies in $M \cap N$. When $M \cap N = \{e\}$, elements of $M$ commute with elements of $N$; this is the first step toward recognizing $G$ as a [[§3 Basic Examples of Groups#^def-3-2|direct product]] $M \times N$ when also $MN = G$ ([[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]]) (not from class).

^rem-47-4

*Problem Set 5, Problems 3 and 4.*

> [!theorem] Lemma §47.9: $3$-Cycles Are Commutators in $A_n$
> Let $n \geq 5$. Every $3$-cycle $(i\,j\,k)$ is a commutator $g_1g_2g_1^{-1}g_2^{-1}$ with $g_1, g_2 \in A_n$.
>
> *Source: PS 5.3(1)*

^lem-47-9

> [!proof]+ Proof
> Recall $(i\,j\,k) = (j\,k)(i\,j)(j\,k)(i\,j)$ ($3$-Cycles Are Commutators, [[§47 Commutators#^prop-47-2|Proposition §47.2]], PS 2.4(3), where the conjugators are transpositions, hence odd). Since $n \geq 5$, choose distinct $l, m \notin \{i, j, k\}$, and set $g_1 = (l\,m)(j\,k)$ and $g_2 = (l\,m)(i\,j)$. Both are even, and each is its own inverse, since $(l\,m)$ commutes with the disjoint transpositions $(i\,j)$ and $(j\,k)$. Moving the four factors $(l\,m)$ to the front and using $(l\,m)^4 = e$,
>
> $$ g_1g_2g_1^{-1}g_2^{-1} = (l\,m)(j\,k)(l\,m)(i\,j)(l\,m)(j\,k)(l\,m)(i\,j) = (j\,k)(i\,j)(j\,k)(i\,j) = (i\,j\,k). $$

^pf-47-9

*Uses:* [[§47 Commutators#^prop-47-2|§47.2]]

> [!theorem] Theorem §47.10: Characters of $A_n$ Are Trivial for $n \geq 5$
> Let $n \geq 5$. Then $[A_n, A_n] = A_n$, and every character $\psi: A_n \to A$ is trivial.
>
> *Source: PS 5.3*

^thm-47-10

> [!proof]+ Proof
> By the lemma ([[§47 Commutators#^lem-47-9|Lemma §47.9]]) every $3$-cycle lies in $[A_n, A_n]$, and $A_n$ is generated by $3$-cycles (Generators of $A_n$, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]]); so $[A_n, A_n] = A_n$. A character kills every commutator (Characters Kill Commutators, [[§47 Commutators#^prop-47-1|§47.1]]), so $\psi$ is trivial on the $3$-cycles; as a homomorphism, it is then trivial on all of $A_n$, every element being a product of $3$-cycles.

^pf-47-10

*Uses:* [[§47 Commutators#^lem-47-9|§47.9]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]], [[§47 Commutators#^prop-47-1|§47.1]]

> [!remark] Remark: Small $n$, and the Link to Simplicity
> The bound $n \geq 5$ is sharp. $A_3 \cong \mathbb{Z}/3\mathbb{Z}$ is abelian, so the identity map is a nontrivial character. $A_4$ has the nontrivial character $\alpha|_{A_4}: A_4 \to A_3$ of The Pair-Partition Homomorphism ([[§43 Simple Groups#^prop-43-10|§43.10]]), so $[A_4, A_4] \subseteq V \neq A_4$. For $n \geq 5$ the theorem also follows from simplicity ([[§43 Simple Groups#^thm-43-9|Theorem §43.9]]): $[A_n, A_n]$ is normal and, since $A_n$ is not abelian, nontrivial, hence equal to $A_n$. PS 5.3 gives a much shorter direct proof.

^rem-47-5

> [!example] Example §47.2: Products of Commutators That Are Not Commutators
> $[G,G]$ is defined as the subgroup *generated* by commutators; this example shows that it can contain elements that are not themselves commutators. Fix $p, q, r \geq 1$ and let $G$ be the group of real block matrices
>
> $$ T(A, B, C) = \begin{bmatrix} I_p & A & C \\ 0 & I_q & B \\ 0 & 0 & I_r \end{bmatrix} \qquad (A \text{ is } p \times q,\ B \text{ is } q \times r,\ C \text{ is } p \times r). $$
>
> 1. *Formulas.* Block multiplication gives $T(A, B, C)\,T(X, Y, Z) = T(A + X,\ B + Y,\ C + Z + AY)$, hence $T(A, B, C)^{-1} = T(-A, -B, AB - C)$ and
>
>    $$ T(A, B, C)\,T(X, Y, Z)\,T(A, B, C)^{-1}\,T(X, Y, Z)^{-1} = T(0,\ 0,\ AY - XB). $$
>
> 2. *The commutator subgroup.* $[G, G] = \{T(0, 0, M)\}$. By (1) every commutator has this form, and these matrices form a subgroup, since $T(0,0,M)\,T(0,0,N) = T(0,0,M+N)$. Conversely, $T(0, 0, \lambda E_{st})$ is a commutator: take $A$ with row $s$ equal to $(\lambda/q, \ldots, \lambda/q)$ and $Y$ with column $t$ equal to $(1, \ldots, 1)^T$, all other entries $0$, so that $AY = \lambda E_{st}$; and every $T(0,0,M)$ is a product of these.
> 3. *Not every element is a commutator.* If $T(0, 0, M)$ is a commutator, then $M = AY - XB$ with $AY$ and $XB$ products through $\mathbb{R}^q$, so $\operatorname{rank} M \leq \operatorname{rank}(AY) + \operatorname{rank}(XB) \leq 2q$. So if $p, r > 2q$, any $M$ of rank $> 2q$ gives an element of $[G, G]$ that is not a commutator; e.g. $(p, q, r) = (3, 1, 3)$ and $M = I_3$, of rank $3 > 2$.
>
> *Source: PS 5.4*

^ex-47-2

