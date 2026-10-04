---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 46
tags: [group-theory, math493]
---
← [[§45 Characters]] · ↑ [[· 9 Characters and Commutators]] · [[§47 S₃, Aₙ and GLₙ]] →

*Reference: Pinter Ch. 15 (commutators).*

> [!definition] Definition §46.1: Commutator
> An element $h \in G$ is a **commutator** if $h = g_1 g_2 g_1^{-1} g_2^{-1}$ for some $g_1, g_2 \in G$. The identity is always a commutator (take $g_1 = g_2 = e$), and $G$ is abelian if and only if $e$ is the only commutator.

^def-46-1

> [!theorem] Proposition §46.1: Characters Kill Commutators
> Let $\chi: G \to A$ be a character and $h \in G$ a commutator. Then $\chi(h) = e_A$.
>
> *Source: PS 2.4(2)*

^prop-46-1

> [!proof]+ Proof
> Write $h = g_1g_2g_1^{-1}g_2^{-1}$. Since $\chi$ is a homomorphism and $A$ is abelian,
>
> $$ \chi(h) = \chi(g_1)\chi(g_2)\chi(g_1^{-1})\chi(g_2^{-1}) = \chi(g_1)\chi(g_1^{-1})\,\chi(g_2)\chi(g_2^{-1}) = \chi(g_1g_1^{-1})\,\chi(g_2g_2^{-1}) = \chi(e)\chi(e) = e_A. $$

^pf-46-1

*Uses:* [[§45 Characters#^def-45-1|Def. §45.1]], [[§46 Commutators#^def-46-1|Def. §46.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: The Contrapositive as a Tool
> This gives a practical test: to show an element $h$ is *not* a commutator, exhibit one character $\chi$ with $\chi(h) \neq e_A$. [[§46 Commutators#^prop-46-3|PS 2.4(4)]] below is exactly this, with $\chi = \operatorname{sgn}$.

^rem-46-1

> [!theorem] Proposition §46.2: $3$-Cycles Are Commutators
> Let $n \geq 3$ and let $c = (i\,j\,k) \in S_n$ with $i, j, k$ distinct. Then $c$ is a commutator: with $g_1 = (j\,k)$ and $g_2 = (i\,j)$,
>
> $$ g_1 g_2 g_1^{-1} g_2^{-1} = (j\,k)(i\,j)(j\,k)(i\,j) = (i\,j\,k). $$
>
> *Source: PS 2.4(3)*

^prop-46-2

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

^pf-46-2

*Uses:* [[§46 Commutators#^def-46-1|Def. §46.1]], [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex. §12.1]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]

![[m493-41-1.svg]]
*The commutator of §46.2 as a wiring diagram, read left to right in the order the factors act (right to left in the product $g_1g_2g_1^{-1}g_2^{-1}$). Following each strand through the four swaps: $i$ ends at $j$ (blue), $j$ at $k$ (red), $k$ at $i$ (green). The result is the $3$-cycle $(i\,j\,k)$.*

> [!theorem] Proposition §46.3: Transpositions Are Not Commutators
> Let $n \geq 2$ and let $s = (i\,j) \in S_n$ with $i \neq j$. Then $s$ is not a commutator.
>
> *Source: PS 2.4(4)*

^prop-46-3

> [!proof]+ Proof
> The sign $\operatorname{sgn}: S_n \to \{\pm 1\}$ is a character (the target is abelian). By [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], $\operatorname{sgn}(s) = \det M(s) = -1$, since $M(s)$ is the identity matrix with two columns interchanged. If $s$ were a commutator, [[§46 Commutators#^prop-46-1|Characters Kill Commutators]] would force $\operatorname{sgn}(s) = 1$, a contradiction.

^pf-46-3

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def. §21.2]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§34 Determinants#^ladr-9-57|LADR 9.57]], [[§46 Commutators#^prop-46-1|§46.1]]

> [!definition] Definition §46.2: Commutator Subgroup
> The **commutator subgroup** of $G$, written $[G,G]$ ([[493 Problem Set 4#^hw-4-4|PS 4.4]] writes $D(G)$), is the [[§4 Subgroups#^def-4-4|subgroup generated]] by all [[§46 Commutators#^def-46-1|commutators]] $aba^{-1}b^{-1}$, $a, b \in G$. (A product of commutators need not itself be a commutator, which is why the generated subgroup is taken.)

^def-46-2

> [!theorem] Proposition §46.4: Properties of the Commutator Subgroup
> 1. $[G,G]$ is a normal subgroup of $G$ ([[· 8 Normal Subgroups and Quotient Groups|Chapter 8]]).
> 2. Every character $\chi: G \to A$ is trivial on $[G,G]$, i.e. $[G,G] \subseteq \operatorname{Ker}\chi$.
> 3. $[G,G] = \{e\}$ if and only if $G$ is abelian.
>
> *Source: (1) is PS 4.4(1)*

^prop-46-4

> [!proof]+ Proof
> **(1)** Conjugation carries commutators to commutators:
>
> $$ g\,(aba^{-1}b^{-1})\,g^{-1} = (gag^{-1})(gbg^{-1})(gag^{-1})^{-1}(gbg^{-1})^{-1}. $$
>
> The inverse of a commutator is a commutator, $(aba^{-1}b^{-1})^{-1} = bab^{-1}a^{-1}$, so every element of $[G,G]$ is a product of commutators $c_1 \cdots c_m$, and since [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|conjugation is a homomorphism]],
>
> $$ g(c_1 \cdots c_m)g^{-1} = (gc_1g^{-1}) \cdots (gc_mg^{-1}) \in [G,G]. $$
>
> **(2)** $\chi$ kills every commutator ([[§46 Commutators#^prop-46-1|Characters Kill Commutators]]), and $\operatorname{Ker}\chi$ is a subgroup, so it contains the subgroup they generate. **(3)** $G$ is abelian iff every commutator equals $e$, iff $[G,G] = \{e\}$.

^pf-46-4

*Uses:* [[§46 Commutators#^def-46-2|Def. §46.2]], [[§4 Subgroups#^def-4-4|Def. §4.4]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§46 Commutators#^prop-46-1|§46.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§46 Commutators#^def-46-1|Def. §46.1]]

> [!theorem] Theorem §46.5: The Commutator Subgroup and Characters of $S_n$
> For $n \geq 2$, $[S_n, S_n] = A_n$. Consequently every [[§45 Characters#^def-45-1|character]] $\chi: S_n \to A$ is trivial on $A_n$ and is determined by its value $c = \chi(\tau)$ on any transposition $\tau$, which satisfies $c^2 = e_A$: $\chi(\sigma) = e_A$ for even $\sigma$ and $\chi(\sigma) = c$ for odd $\sigma$.
>
> *Source: PS 4.5*

^thm-46-5

> [!proof]+ Proof
> ($\subseteq$) The sign $\operatorname{sgn}$ is a character, so by (2) ([[§46 Commutators#^prop-46-4|§46.4]]) $[S_n, S_n] \subseteq \operatorname{Ker}\operatorname{sgn} = A_n$. ($\supseteq$) For $n = 2$, $A_2 = \{e\}$. For $n \geq 3$, $A_n$ is generated by $3$-cycles ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]]), each of which is a commutator ([[§46 Commutators#^prop-46-2|§46.2]]); so $A_n \subseteq [S_n, S_n]$. For the consequence: $\chi$ is trivial on $[S_n, S_n] = A_n$ by (2). All transpositions are conjugate ([[§33 Conjugacy Classes#^prop-33-2|§33.2]]), so $\chi$ takes a single value $c$ on them ([[§45 Characters#^prop-45-1|Characters Are Constant on Conjugacy Classes]]), and $c^2 = \chi(\tau^2) = \chi(e) = e_A$. An odd $\sigma$ equals $\tau(\tau\sigma)$ with $\tau\sigma$ even, so $\chi(\sigma) = \chi(\tau)\chi(\tau\sigma) = c$.
>
> *Direct proof of the consequence ([[493 Problem Set 4#^hw-4-5|PS 4.5]]).* Let $a = \chi((1\,2))$. **(1)** For a transposition $(i\,j)$, choose $\sigma \in S_n$ with $\sigma(i) = 1$, $\sigma(j) = 2$, mapping the remaining $n - 2$ points bijectively onto the remaining $n - 2$ points. By [[§33 Conjugacy Classes#^lem-33-1|Conjugation Relabels the Entries]] (§33), $\sigma(i\,j)\sigma^{-1} = (1\,2)$, so, $A$ being abelian, $a = \chi(\sigma)\chi((i\,j))\chi(\sigma)^{-1} = \chi((i\,j))$. **(2)** $a^2 = \chi((1\,2)^2) = \chi(e) = e_A$. **(3)** Write $\sigma = t_1 \cdots t_k$ with each $t_i$ of the form $(1\,j)$ (Generators of $S_n$, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]]). Then $\operatorname{sgn}(\sigma) = (-1)^k$ ([[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]]), so $\sigma \in A_n$ iff $k$ is even, while $\chi(\sigma) = a^k$, which by (2) is $e_A$ for even $k$ and $a$ for odd $k$.

^pf-46-5

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§46 Commutators#^prop-46-4|§46.4]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-9|§21.9]], [[§46 Commutators#^prop-46-2|§46.2]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§33 Conjugacy Classes#^prop-33-2|§33.2]], [[§45 Characters#^prop-45-1|§45.1]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§45 Characters#^def-45-1|Def. §45.1]], [[§33 Conjugacy Classes#^lem-33-1|§33.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|§21.7]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark] Remark: What the Theorem Says About $S_n$
> In $S_n$ all $3$-cycles are commutators and no transposition is, and [[§46 Commutators#^thm-46-5|the theorem]] shows that characters of $S_n$ can only distinguish even from odd permutations: $\operatorname{sgn}$ is essentially the only nontrivial one.

^rem-46-2

> [!definition] Definition §46.3: Abelianization
> The **abelianization** of $G$ is the [[§40 Quotient Groups#^def-40-1|quotient group]] $G^{\mathrm{ab}} := G/[G,G]$, defined because $[G,G]$ is normal ([[§46 Commutators#^prop-46-4|Properties of the Commutator Subgroup]]).
>
> *Source: PS 4.4*

^def-46-3

> [!remark]- Connections
> - In 590, forcing commutativity is the quotient $F_2 \to \mathbb{Z} \times \mathbb{Z}$: [[§21 Algebra Prerequisites꞉ Groups#^ex-21-8|Forcing Commutativity]], [[§21 Algebra Prerequisites꞉ Groups#^rem-21-12|The Hierarchy of Relations]], and “Abelianization” in [[§21 Algebra Prerequisites꞉ Groups#^rem-21-14|Simplifying Presentations]].

> [!theorem] Proposition §46.6: The Abelianization Is Abelian
> $G/[G,G]$ is abelian.
>
> *Source: PS 4.4(2)*

^prop-46-6

> [!proof]+ Proof
> Let $N = [G,G]$. For $a, b \in G$, $(aN)(bN)(aN)^{-1}(bN)^{-1} = aba^{-1}b^{-1}N = N$, since the commutator $aba^{-1}b^{-1}$ lies in $N$. So $(aN)(bN) = (bN)(aN)$.
>
> *Second proof, by the coset criterion ([[493 Problem Set 4#^hw-4-4|PS 4.4(2)]]).* For $x, y \in G$, $xN = yN$ iff $x^{-1}y \in N$ ([[§28 Left and Right Cosets#^prop-28-2|§28.2]]). With $x = ab$ and $y = ba$, $x^{-1}y = b^{-1}a^{-1}ba$, which is the [[§46 Commutators#^def-46-1|commutator]] of the pair $(b^{-1}, a^{-1})$ and so lies in $N$. Hence $(ab)N = (ba)N$, i.e. $(aN)(bN) = (bN)(aN)$.

^pf-46-6

*Uses:* [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§40 Quotient Groups#^thm-40-1|§40.1]], [[§28 Left and Right Cosets#^prop-28-2|§28.2]], [[§46 Commutators#^def-46-2|Def. §46.2]], [[§28 Left and Right Cosets#^def-28-1|Def. §28.1]], [[§46 Commutators#^def-46-1|Def. §46.1]], [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]]

> [!example] Example §46.1: The Abelianization of $S_n$
> For $n \geq 2$, $S_n/[S_n, S_n] = S_n/A_n \cong \{\pm 1\}$: by The Commutator Subgroup and Characters of $S_n$ ([[§46 Commutators#^thm-46-5|§46.5]]), $[S_n, S_n] = A_n$, and the [[§41 The First Isomorphism Theorem#^thm-41-1|First Isomorphism Theorem]] applied to the surjective homomorphism $\operatorname{sgn}$, whose kernel is $A_n$, gives $S_n/A_n \cong \{\pm 1\}$ ([[§41 The First Isomorphism Theorem#^ex-41-1|Ex. §41.1]]).
>
> *Source: not from class*

^ex-46-1

> [!theorem] Corollary §46.7: Every Square Root of $e_A$ Gives a Character
> Let $n \geq 2$ and let $A$ be abelian. For each $a \in A$ with $a^2 = e_A$, the map
>
> $$ \chi_a(\sigma) = \begin{cases} e_A & \sigma \in A_n, \\ a & \sigma \notin A_n \end{cases} $$
>
> is a [[§45 Characters#^def-45-1|character]] of $S_n$, and $a \mapsto \chi_a$ is a bijection from $\{a \in A : a^2 = e_A\}$ onto the set of characters $S_n \to A$, with inverse $\chi \mapsto \chi((1\,2))$.
>
> *Source: not from class*

^cor-46-7

> [!proof]+ Proof
> Define $\iota_a: \{\pm 1\} \to A$ by $\iota_a(1) = e_A$ and $\iota_a(-1) = a$. It is a homomorphism: the only product to check is $\iota_a((-1)(-1)) = \iota_a(1) = e_A = a^2 = \iota_a(-1)\iota_a(-1)$. So $\chi_a = \iota_a \circ \operatorname{sgn}$ is a homomorphism, and $\chi_a((1\,2)) = a$. Conversely, by The Commutator Subgroup and Characters of $S_n$ ([[§46 Commutators#^thm-46-5|§46.5]]), every character $\chi$ equals $\chi_a$ for $a = \chi((1\,2))$, which satisfies $a^2 = e_A$. So the two assignments are mutually inverse.

^pf-46-7

*Uses:* [[§45 Characters#^def-45-1|Def. §45.1]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]], [[§16 Isomorphisms#^prop-16-2|§16.2]], [[§46 Commutators#^thm-46-5|§46.5]]

> [!remark] Remark: The Characters of $S_n$, Completely
> [[§46 Commutators#^thm-46-5|PS 4.5]] shows every character of $S_n$ is “trivial or the sign in disguise”; [[§46 Commutators#^cor-46-7|the corollary]] shows every such candidate actually occurs. For $A = \mathbb{C}^\times$ ([[§3 Basic Examples of Groups#^def-3-4|Def. §3.4]]) the square roots of $1$ are $\pm 1$, so $S_n$ ($n \geq 2$) has exactly two characters with values in $\mathbb{C}^\times$: the trivial one and $\operatorname{sgn}$ ([[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|Def. §21.2]]).

^rem-46-3

> [!theorem] Proposition §46.8: Normal Subgroups with Trivial Intersection Commute
> Let $M$ and $N$ be [[§38 Normal Subgroups#^def-38-1|normal subgroups]] of $G$ with $M \cap N = \{e\}$. Then $mn = nm$ for all $m \in M$ and $n \in N$.
>
> *Source: PS 4.2*

^prop-46-8

> [!proof]+ Proof
> Let $x = mnm^{-1}n^{-1}$. Grouping as $x = (mnm^{-1})\,n^{-1}$: $mnm^{-1} \in N$ because $N$ is normal, and $n^{-1} \in N$, so $x \in N$. Grouping as $x = m\,(nm^{-1}n^{-1})$: $nm^{-1}n^{-1} \in M$ because $M$ is normal, and $m \in M$, so $x \in M$. Hence $x \in M \cap N = \{e\}$, i.e. $mnm^{-1}n^{-1} = e$, and then
>
> $$ mn = mn\,(m^{-1}n^{-1}nm) = (mnm^{-1}n^{-1})\,nm = nm. $$

^pf-46-8

*Uses:* [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§4 Subgroups#^def-4-1|Def. §4.1]]

> [!remark] Remark: Commutators of Normal Subgroups
> [[§46 Commutators#^pf-46-8|The proof]] shows more: for normal $M, N$, every [[§46 Commutators#^def-46-1|commutator]] $mnm^{-1}n^{-1}$ with $m \in M$, $n \in N$ lies in $M \cap N$. When $M \cap N = \{e\}$, elements of $M$ commute with elements of $N$; this is the first step toward recognizing $G$ as a [[§3 Basic Examples of Groups#^def-3-2|direct product]] $M \times N$ when also $MN = G$ ([[§42 The Second and Third Isomorphism Theorems#^def-42-1|Def. §42.1]]) (not from class).

^rem-46-4
