---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 52
tags: [group-theory, math493]
---
← [[§51 p-Groups and Sylow Subgroups]] · ↑ [[· 10 The Sylow Theorems]]

*Reference: Worksheet 10. Throughout, $p$ is a prime and the groups are finite.*

> [!remark] Remark: The Strategy
> Every finite group $G$ is a subgroup of some $GL_n(\mathbb{F}_p)$ (Every Finite Group Is a Matrix Group, [[§25 Actions#^cor-25-6|Corollary §25.6]]), and $\Gamma = GL_n(\mathbb{F}_p)$ has an explicit Sylow $p$-subgroup $\Pi$, the unitriangular matrices (WS 10.2, [[§51 p-Groups and Sylow Subgroups#^prop-51-5|Proposition §51.5]]). The plan is to transfer Sylow subgroups from the large group $\Gamma$ down to its subgroup $G$, by letting $G$ act on $\Gamma/\Pi$ (WS 10.3, [[§52 The Sylow Theorems#^prop-52-3|Proposition §52.3]]). The lecture sketched the key step in the case where $G$ is itself a $p$-group: the next lemma.
>
> *Source: lecture 10/12*

^rem-52-1

> [!theorem] Lemma §52.1: $p$-Subgroups Lie in a Conjugate of a Sylow Subgroup
> Let $\Gamma$ be a finite group with a [[§51 p-Groups and Sylow Subgroups#^def-51-2|Sylow $p$-subgroup]] $\Pi$, and let $P \leq \Gamma$ be a [[§51 p-Groups and Sylow Subgroups#^def-51-1|$p$-subgroup]]. Then there is $\gamma \in \Gamma$ with $P \subseteq \gamma \Pi \gamma^{-1}$.
>
> *Source: lecture 10/12*

^lem-52-1

> [!proof]+ Proof
> Write $|\Gamma| = p^k m$ with $p \nmid m$, so $|\Pi| = p^k$. Let $X = \Gamma/\Pi$; by Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]), $|X| = [\Gamma : \Pi] = m \not\equiv 0 \pmod p$. Let $P$ act on $X$ by left multiplication, the restriction to $P$ of the action of $\Gamma$ on $\Gamma/\Pi$ (The Action of $G$ on $G/H$, [[§31 G Acting on Coset Spaces#^prop-31-1|Proposition §31.1]]). By WS 10.1 ([[§51 p-Groups and Sylow Subgroups#^prop-51-1|Proposition §51.1]]), $P$ fixes some coset $\gamma\Pi \in X$, i.e. $P \subseteq \operatorname{Stab}(\gamma\Pi)$. By part (3) of Proposition §31.1, $\operatorname{Stab}(\gamma\Pi) = \gamma\Pi\gamma^{-1}$. Hence $P \subseteq \gamma\Pi\gamma^{-1}$. (The argument rests on WS 10.1, whose proof is still to be filled in.)

^pf-52-1

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]], [[§51 p-Groups and Sylow Subgroups#^prop-51-1|§51.1]], [[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]

> [!theorem] Corollary §52.2: $p$-Subgroups of $GL_n(\mathbb{F}_p)$ Are Conjugate into Unitriangular Matrices
> Let $Q$ be a $p$-subgroup of $GL_n(\mathbb{F}_p)$ and $P$ the unitriangular group. Then $\gamma^{-1} Q \gamma \subseteq P$ for some $\gamma \in GL_n(\mathbb{F}_p)$.
>
> *Source: lecture 10/12*

^cor-52-2

> [!proof]+ Proof
> By WS 10.2 ([[§51 p-Groups and Sylow Subgroups#^prop-51-5|Proposition §51.5]]), $P$ is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$. By [[§52 The Sylow Theorems#^lem-52-1|Lemma §52.1]] with $\Gamma = GL_n(\mathbb{F}_p)$ and $\Pi = P$, $Q \subseteq \gamma P \gamma^{-1}$ for some $\gamma$; conjugating by $\gamma^{-1}$, $\gamma^{-1} Q \gamma \subseteq \gamma^{-1}(\gamma P \gamma^{-1})\gamma = P$.

^pf-52-2

*Uses:* [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]], [[§52 The Sylow Theorems#^lem-52-1|§52.1]]

> [!remark] Remark: A Surprising Consequence
> The corollary is not obvious from linear algebra. For instance, any subgroup with $16$ elements of $GL_{10^6}(\mathbb{F}_2)$, however its matrices look, becomes a group of upper triangular matrices after a single change of basis. The proof gives no formula for the change of basis; it comes from a counting argument.
>
> *Source: lecture 10/12*

^rem-52-2

> [!theorem] Proposition §52.3: Sylow Subgroups of a Subgroup
> Let $\Gamma$ be a finite group with a Sylow $p$-subgroup $\Pi$ ([[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]), and let $G$ be a [[§4 Subgroups#^def-4-1|subgroup]] of $\Gamma$.
> 1. $G$ has a Sylow $p$-subgroup $P$.
> 2. More specifically, there is some $\gamma \in \Gamma$ such that $P = G \cap \gamma\Pi\gamma^{-1}$ is a Sylow $p$-subgroup of $G$.
>
> *Source: WS 10.3; proved in class 10/14*

^prop-52-3

> [!proof]+ Proof
> *(Class 10/14.)* Write $|\Gamma| = p^k m$ and $|G| = p^l n$ with $p \nmid m$ and $p \nmid n$, so $|\Pi| = p^k$; we must find a subgroup of $G$ of order $p^l$. Let $X = \Gamma/\Pi$, so $|X| = [\Gamma : \Pi] = m \not\equiv 0 \pmod p$ (Lagrange, [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]). Let $G$ act on $X$ by left multiplication, the restriction to $G$ of the action of $\Gamma$ on its cosets.
>
> *An orbit of size prime to $p$.* $X$ breaks up into $G$-orbits (Orbits Partition $X$, [[§27 Orbits#^prop-27-1|Proposition §27.1]]), and $|X|$ is the sum of their sizes. Since $p \nmid |X|$, at least one orbit $G \cdot (\gamma\Pi)$ has size $\not\equiv 0 \pmod p$.
>
> *Its stabilizer.* For $h \in G$, $h\gamma\Pi = \gamma\Pi$ iff $\gamma^{-1}h\gamma \in \Pi$ iff $h \in \gamma\Pi\gamma^{-1}$. So
>
> $$ \operatorname{Stab}_G(\gamma\Pi) = G \cap \gamma\Pi\gamma^{-1}. $$
>
> *Counting.* By Orbit–Stabilizer ([[§30 Orbit–Stabilizer#^thm-30-3|Theorem §30.3]]),
>
> $$ p^l n = |G| = |G \cdot (\gamma\Pi)| \cdot |G \cap \gamma\Pi\gamma^{-1}|. $$
>
> The first factor is not divisible by $p$, so all $l$ factors of $p$ lie in the second: $p^l$ divides $|G \cap \gamma\Pi\gamma^{-1}|$. On the other hand, $G \cap \gamma\Pi\gamma^{-1}$ is a subgroup of $\gamma\Pi\gamma^{-1}$, which has order $|\Pi| = p^k$ (conjugation is an isomorphism, [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Proposition §18.1]]), so by Lagrange $|G \cap \gamma\Pi\gamma^{-1}| = p^j$ for some $j$ with $l \leq j \leq k$. It is also a subgroup of $G$, so $p^j$ divides $p^l n$, giving $j \leq l$. Hence $j = l$, and
>
> $$ P := G \cap \gamma\Pi\gamma^{-1} $$
>
> is a subgroup of $G$ of order $p^l$: a Sylow $p$-subgroup of $G$, of the form required in (2).

^pf-52-3

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§27 Orbits#^prop-27-1|§27.1]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

*Worksheet hint for (1): consider $G$ [[§31 G Acting on Coset Spaces#^prop-31-1|acting]] on $\Gamma/\Pi$. Worksheet hint for the next three results: use [[§52 The Sylow Theorems#^prop-52-3|Proposition §52.3]].*

> [!theorem] Theorem §52.4: The First Sylow Theorem
> Every finite group $G$ has a Sylow $p$-subgroup ([[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]).
>
> *Source: WS 10.4; proved in class 10/14*

^thm-52-4

> [!proof]+ Proof
> *(Class 10/14.)* Let $G$ be finite with $|G| = n$. By Every Finite Group Is a Matrix Group ([[§25 Actions#^cor-25-6|Corollary §25.6]]), $G$ is isomorphic to a subgroup $G'$ of $\Gamma = GL_n(\mathbb{F}_p)$, and $\Gamma$ has a Sylow $p$-subgroup $\Pi$, the unitriangular matrices (WS 10.2, [[§51 p-Groups and Sylow Subgroups#^prop-51-5|Proposition §51.5]]). By WS 10.3(1) ([[§52 The Sylow Theorems#^prop-52-3|Proposition §52.3]]), $G'$ has a Sylow $p$-subgroup; its preimage under the isomorphism $G \to G'$ is a Sylow $p$-subgroup of $G$. (The argument rests on WS 10.2, still to be proved; the order of $GL_n(\mathbb{F}_p)$ it uses is [[§51 p-Groups and Sylow Subgroups#^prop-51-4|Proposition §51.4]], PS 6.4.)

^pf-52-4

*Uses:* [[§25 Actions#^cor-25-6|§25.6]], [[§51 p-Groups and Sylow Subgroups#^prop-51-5|§51.5]], [[§52 The Sylow Theorems#^prop-52-3|§52.3]], [[§51 p-Groups and Sylow Subgroups#^prop-51-4|§51.4]]

> [!theorem] Proposition §52.5: $p$-Subgroups and Conjugates of a Sylow Subgroup
> Let $G$ be a finite group and let $P$ be a Sylow $p$-subgroup with $|P| = p^k$.
> 1. If $Q$ is a $p$-subgroup of $G$ ([[§51 p-Groups and Sylow Subgroups#^def-51-1|Def. §51.1]]), there is some $g \in G$ such that $Q \subseteq gPg^{-1}$.
> 2. If $H$ is a subgroup of $G$ whose [[§4 Subgroups#^def-4-6|order]] is divisible by $p^k$, there is some $g \in G$ such that $H \supseteq gPg^{-1}$.
>
> *Source: WS 10.5; (2) proved on the board 10/14*

^prop-52-5

> [!proof]+ Proof
> **(1)** This is [[§52 The Sylow Theorems#^lem-52-1|Lemma §52.1]] with $\Gamma = G$ and $\Pi = P$.
>
> **(2)** *(Board 10/14.)* Since $H \leq G$, $|H|$ divides $|G| = p^k m$ with $p \nmid m$ (Lagrange, [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]); as $p^k$ divides $|H|$, the largest power of $p$ dividing $|H|$ is exactly $p^k$. By the First Sylow Theorem ([[§52 The Sylow Theorems#^thm-52-4|Theorem §52.4]]), $H$ has a Sylow $p$-subgroup $Q$, of order $p^k$. Then $Q$ is a $p$-subgroup of $G$, so by (1) $Q \subseteq gPg^{-1}$ for some $g \in G$; both have $p^k$ elements, so $Q = gPg^{-1}$. Hence $H \supseteq Q = gPg^{-1}$.

^pf-52-5

*Uses:* [[§52 The Sylow Theorems#^lem-52-1|§52.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§52 The Sylow Theorems#^thm-52-4|§52.4]]

> [!theorem] Theorem §52.6: The Second Sylow Theorem
> Let $G$ be a finite group and let $P_1$ and $P_2$ be two Sylow $p$-subgroups of $G$. Then there is some $g \in G$ such that $P_2 = gP_1g^{-1}$.
>
> *Source: WS 10.6; stated 10/14, to be proved Fri Oct 16*

^thm-52-6

> [!proof]- Proof
> *[To be proved.]*

^pf-52-6

> [!theorem] Theorem §52.7: The Third Sylow Theorem
> For any finite group $G$, the number of Sylow $p$-subgroups of $G$ is congruent to $1 \bmod p$.
>
> *Source: stated on WS 10 and 10/14; to be proved Fri Oct 16*

^thm-52-7

> [!proof]- Proof
> *[To be proved.]*

^pf-52-7

Worksheet 10: “Realistically, we'll wind up covering this in lecture.”
