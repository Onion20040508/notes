---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 55
tags: [group-theory, math493]
---
← [[§54 p-Groups and Sylow Subgroups]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§56 Simple Groups of Small Order]] →

*Reference: Worksheet 10; lectures 10/12–10/16. Throughout, $p$ is a prime and the groups are finite.*

> [!remark] Remark: The Strategy
> Every finite group $G$ is isomorphic to a subgroup of some $GL_n(\mathbb{F}_p)$ (Every Finite Group Is a Matrix Group, [[§25 Actions#^cor-25-6|Corollary §25.6]]), and $\Gamma = GL_n(\mathbb{F}_p)$ has an explicit Sylow $p$-subgroup $\Pi$, the unitriangular matrices (WS 10.2, [[§54 p-Groups and Sylow Subgroups#^prop-54-5|Proposition §54.5]]). The plan is to transfer Sylow subgroups from the large group $\Gamma$ down to its subgroup $G$, by letting $G$ act on $\Gamma/\Pi$ (WS 10.3, [[§55 The Sylow Theorems#^prop-55-3|Proposition §55.3]]). The lecture sketched the key step in the case where $G$ is itself a $p$-group: the next lemma.
>
> *Source: lecture 10/12*

^rem-55-1

> [!theorem] Lemma §55.1: $p$-Subgroups Lie in a Conjugate of a Sylow Subgroup
> Let $\Gamma$ be a finite group with a Sylow $p$-subgroup ([[§54 p-Groups and Sylow Subgroups#^def-54-2|Def. §54.2]]) $\Pi$, and let $P \leq \Gamma$ be a $p$-subgroup ([[§54 p-Groups and Sylow Subgroups#^def-54-1|Def. §54.1]]). Then there is $\gamma \in \Gamma$ with $P \subseteq \gamma \Pi \gamma^{-1}$.
>
> *Source: lecture 10/12*

^lem-55-1

> [!proof]+ Proof
> *Idea:* $P$ acts on $\Gamma/\Pi$, of size prime to $p$, so it fixes a coset $\gamma\Pi$.
>
> Write $|\Gamma| = p^k m$ with $p \nmid m$, so $|\Pi| = p^k$. Let $X = \Gamma/\Pi$; by Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]), $|X| = [\Gamma : \Pi] = m \not\equiv 0 \pmod p$. Let $P$ act on $X$ by left multiplication, the restriction to $P$ of the action of $\Gamma$ on $\Gamma/\Pi$ (The Action of $G$ on $G/H$, [[§31 G Acting on Coset Spaces#^prop-31-1|Proposition §31.1]]). By WS 10.1 ([[§54 p-Groups and Sylow Subgroups#^prop-54-1|Proposition §54.1]]), $P$ fixes some coset $\gamma\Pi \in X$, with $\gamma \in \Gamma$, i.e. $P \subseteq \operatorname{Stab}(\gamma\Pi)$. By part (3) of Proposition §31.1, $\operatorname{Stab}(\gamma\Pi) = \gamma\Pi\gamma^{-1}$. Hence $P \subseteq \gamma\Pi\gamma^{-1}$.

^pf-55-1

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§31 G Acting on Coset Spaces#^prop-31-1|§31.1]], [[§54 p-Groups and Sylow Subgroups#^prop-54-1|§54.1]], [[§54 p-Groups and Sylow Subgroups#^def-54-2|Def. §54.2]]

> [!theorem] Corollary §55.2: $p$-Subgroups of $GL_n(\mathbb{F}_p)$ Are Conjugate into Unitriangular Matrices
> Let $Q$ be a $p$-subgroup of $GL_n(\mathbb{F}_p)$ and $P$ the unitriangular group. Then $\gamma^{-1} Q \gamma \subseteq P$ for some $\gamma \in GL_n(\mathbb{F}_p)$.
>
> *Source: lecture 10/12*

^cor-55-2

> [!proof]+ Proof
> By WS 10.2 ([[§54 p-Groups and Sylow Subgroups#^prop-54-5|Proposition §54.5]]), $P$ is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$. By [[§55 The Sylow Theorems#^lem-55-1|Lemma §55.1]] with $\Gamma = GL_n(\mathbb{F}_p)$ and $\Pi = P$, $Q \subseteq \gamma P \gamma^{-1}$ for some $\gamma \in GL_n(\mathbb{F}_p)$; conjugating by $\gamma^{-1}$, $\gamma^{-1} Q \gamma \subseteq \gamma^{-1}(\gamma P \gamma^{-1})\gamma = P$.

^pf-55-2

*Uses:* [[§54 p-Groups and Sylow Subgroups#^prop-54-5|§54.5]], [[§55 The Sylow Theorems#^lem-55-1|§55.1]]

> [!remark] Remark: A Surprising Consequence
> The corollary is not obvious from linear algebra (Example [[§55 The Sylow Theorems#^ex-55-1|§55.1]]). The proof gives no formula for the change of basis; it comes from a counting argument.
>
> *Source: lecture 10/12*

^rem-55-2

> [!example] Example §55.1: Subgroups of Order $16$ in $GL_{10^6}(\mathbb{F}_2)$
> Any subgroup $Q$ with $16$ elements of $GL_{10^6}(\mathbb{F}_2)$, however its matrices look, becomes a group of upper triangular matrices after a single change of basis. Indeed, $|Q| = 16 = 2^4$, so $Q$ is a $2$-subgroup of $GL_n(\mathbb{F}_2)$ with $n = 10^6$, and Corollary [[§55 The Sylow Theorems#^cor-55-2|§55.2]] (with $p = 2$) gives $\gamma \in GL_n(\mathbb{F}_2)$ with $\gamma^{-1}Q\gamma \subseteq P$, the unitriangular matrices, which are upper triangular. Replacing each $q \in Q$ by $\gamma^{-1}q\gamma$ is the change of basis to the basis formed by the columns of $\gamma$.
>
> *Source: lecture 10/12*

^ex-55-1

> [!theorem] Proposition §55.3: Sylow Subgroups of a Subgroup
> Let $\Gamma$ be a finite group with a Sylow $p$-subgroup $\Pi$ ([[§54 p-Groups and Sylow Subgroups#^def-54-2|Def. §54.2]]), and let $G$ be a [[§4 Subgroups#^def-4-1|subgroup]] of $\Gamma$.
> 1. $G$ has a Sylow $p$-subgroup $P$.
> 2. More specifically, there is some $\gamma \in \Gamma$ such that $P = G \cap \gamma\Pi\gamma^{-1}$ is a Sylow $p$-subgroup of $G$.
>
> *Source: WS 10.3; proved in class 10/14*

^prop-55-3

> [!proof]+ Proof
> *Idea:* Some $G$-orbit in $\Gamma/\Pi$ has size prime to $p$; its stabilizer is Sylow in $G$.
>
> *(Class 10/14.)* Write $|\Gamma| = p^k m$ and $|G| = p^l n$ with $p \nmid m$ and $p \nmid n$, so $|\Pi| = p^k$; we must find a subgroup of $G$ of order $p^l$. Let $X = \Gamma/\Pi$, so $|X| = [\Gamma : \Pi] = m \not\equiv 0 \pmod p$ (Lagrange, [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]). Let $G$ act on $X$ by left multiplication, the restriction to $G$ of the action of $\Gamma$ on its cosets.
>
> *An orbit of size prime to $p$.* $X$ breaks up into $G$-orbits (Orbits Partition $X$, [[§27 Orbits#^prop-27-1|Proposition §27.1]]), and $|X|$ is the sum of their sizes. Since $p \nmid |X|$, at least one orbit $G \cdot (\gamma\Pi)$, with $\gamma \in \Gamma$, has size $\not\equiv 0 \pmod p$.
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

^pf-55-3

*Uses:* [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§27 Orbits#^prop-27-1|§27.1]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

*Worksheet hint for (1): consider $G$ [[§31 G Acting on Coset Spaces#^prop-31-1|acting]] on $\Gamma/\Pi$. Worksheet hint for the next three results: use [[§55 The Sylow Theorems#^prop-55-3|Proposition §55.3]].*

> [!theorem] Theorem §55.4: The First Sylow Theorem
> Every finite group $G$ has a Sylow $p$-subgroup ([[§54 p-Groups and Sylow Subgroups#^def-54-2|Def. §54.2]]).
>
> *Source: WS 10.4; proved in class 10/14*

^thm-55-4

> [!proof]+ Proof
> *Idea:* Embed $G$ in $GL_n(\mathbb{F}_p)$, which has a Sylow $p$-subgroup, and apply WS 10.3.
>
> *(Class 10/14.)* Let $G$ be finite with $|G| = n$. By Every Finite Group Is a Matrix Group ([[§25 Actions#^cor-25-6|Corollary §25.6]]), $G$ is isomorphic to a subgroup $G'$ of $\Gamma = GL_n(\mathbb{F}_p)$, and $\Gamma$ has a Sylow $p$-subgroup $\Pi$, the unitriangular matrices (WS 10.2, [[§54 p-Groups and Sylow Subgroups#^prop-54-5|Proposition §54.5]]). By WS 10.3(1) ([[§55 The Sylow Theorems#^prop-55-3|Proposition §55.3]]), $G'$ has a Sylow $p$-subgroup; its preimage under the isomorphism $G \to G'$ is a Sylow $p$-subgroup of $G$. (The order of $GL_n(\mathbb{F}_p)$ that WS 10.2 uses is [[§54 p-Groups and Sylow Subgroups#^prop-54-4|Proposition §54.4]], PS 6.4.)

^pf-55-4

*Uses:* [[§25 Actions#^cor-25-6|§25.6]], [[§54 p-Groups and Sylow Subgroups#^prop-54-5|§54.5]], [[§55 The Sylow Theorems#^prop-55-3|§55.3]], [[§54 p-Groups and Sylow Subgroups#^prop-54-4|§54.4]]

> [!theorem] Proposition §55.5: $p$-Subgroups and Conjugates of a Sylow Subgroup
> Let $G$ be a finite group and let $P$ be a Sylow $p$-subgroup with $|P| = p^k$.
> 1. If $Q$ is a $p$-subgroup of $G$ ([[§54 p-Groups and Sylow Subgroups#^def-54-1|Def. §54.1]]), there is some $g \in G$ such that $Q \subseteq gPg^{-1}$.
> 2. If $H$ is a subgroup of $G$ whose [[§4 Subgroups#^def-4-6|order]] is divisible by $p^k$, there is some $g \in G$ such that $H \supseteq gPg^{-1}$.
>
> *Source: WS 10.5; (2) proved on the board 10/14*

^prop-55-5

> [!proof]+ Proof
> *Idea:* (1) is [[§55 The Sylow Theorems#^lem-55-1|Lemma §55.1]] with $\Gamma = G$; (2) a Sylow subgroup of $H$ is a conjugate of $P$.
>
> **(1)** This is [[§55 The Sylow Theorems#^lem-55-1|Lemma §55.1]] with $\Gamma = G$, $\Pi = P$, and $Q$ in the role of its $P$; the conjugating element lies in $\Gamma = G$.
>
> **(2)** *(Board 10/14.)* Since $H \leq G$, $|H|$ divides $|G| = p^k m$ with $p \nmid m$ (Lagrange, [[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]); as $p^k$ divides $|H|$, the largest power of $p$ dividing $|H|$ is exactly $p^k$. By the First Sylow Theorem ([[§55 The Sylow Theorems#^thm-55-4|Theorem §55.4]]), $H$ has a Sylow $p$-subgroup $Q$, of order $p^k$. Then $Q$ is a $p$-subgroup of $G$, so by (1) $Q \subseteq gPg^{-1}$ for some $g \in G$; both have $p^k$ elements, so $Q = gPg^{-1}$. Hence $H \supseteq Q = gPg^{-1}$.

^pf-55-5

*Uses:* [[§55 The Sylow Theorems#^lem-55-1|§55.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§55 The Sylow Theorems#^thm-55-4|§55.4]]

> [!proof]+ Second proof (directly from WS 10.3)
> *Idea:* Apply WS 10.3(2) with $\Gamma = G$, $\Pi = P$ to the subgroups $Q$ and $H$.
>
> *(Not from lecture; from the student's worksheet solutions. This is the route of the worksheet hint.)* Write $|G| = p^k m$ with $p \nmid m$. Apply Sylow Subgroups of a Subgroup (WS 10.3(2), [[§55 The Sylow Theorems#^prop-55-3|Proposition §55.3]]) with $\Gamma = G$ and $\Pi = P$: for every subgroup $L \leq G$ there is some $g \in G$ (an element of $\Gamma = G$) such that $L \cap gPg^{-1}$ is a Sylow $p$-subgroup of $L$. Also $|gPg^{-1}| = |P| = p^k$, since conjugation by $g$ is a bijection ([[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Proposition §18.1]]).
>
> **(1)** Let $|Q| = p^j$. The largest power of $p$ dividing $|Q|$ is $p^j = |Q|$, so a Sylow $p$-subgroup of $Q$ is $Q$ itself. Taking $L = Q$ gives some $g \in G$ with $Q \cap gPg^{-1} = Q$, that is, $Q \subseteq gPg^{-1}$.
>
> **(2)** By Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]), $|H|$ divides $|G| = p^k m$, and $p \nmid m$, so $p^{k+1} \nmid |H|$; together with $p^k \mid |H|$, a Sylow $p$-subgroup of $H$ has order $p^k$. Taking $L = H$ gives some $g \in G$ with $|H \cap gPg^{-1}| = p^k = |gPg^{-1}|$. A subset of the finite set $gPg^{-1}$ with as many elements is all of it, so $H \cap gPg^{-1} = gPg^{-1}$, that is, $gPg^{-1} \subseteq H$.

^pf-55-5-2

*Uses:* [[§55 The Sylow Theorems#^prop-55-3|§55.3]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!theorem] Theorem §55.6: The Second Sylow Theorem
> Let $G$ be a finite group and let $P_1$ and $P_2$ be two Sylow $p$-subgroups of $G$. Then there is some $g \in G$ such that $P_2 = gP_1g^{-1}$.
>
> *Source: WS 10.6; lecture 10/16*

^thm-55-6

> [!proof]+ Proof
> *Idea:* WS 10.3(2) with $\Gamma = G$, $\Pi = P_1$ puts $P_2$ inside some $gP_1g^{-1}$, $g \in G$.
>
> *(Lecture 10/16.)* Let $|G| = p^k m$ with $p \nmid m$, so $|P_1| = |P_2| = p^k$. Apply WS 10.3(2) (Proposition [[§55 The Sylow Theorems#^prop-55-3|§55.3]]) with $\Gamma = G$, $\Pi = P_1$, and the subgroup $P_2$ in the role of $G$: there is $g \in G$ such that $P_2 \cap gP_1g^{-1}$ is a Sylow $p$-subgroup of $P_2$. Since $|P_2| = p^k$, a Sylow $p$-subgroup of $P_2$ has $p^k$ elements, so it is $P_2$ itself:
>
> $$ P_2 \cap gP_1g^{-1} = P_2, \qquad\text{that is,}\qquad P_2 \subseteq gP_1g^{-1}. $$
>
> Conjugation by $g$ is an isomorphism (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]), so $|gP_1g^{-1}| = |P_1| = p^k = |P_2|$, and the inclusion is an equality: $P_2 = gP_1g^{-1}$.

^pf-55-6

*Uses:* [[§55 The Sylow Theorems#^prop-55-3|§55.3]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

> [!theorem] Corollary §55.7: A Normal Sylow Subgroup Is the Only One
> Let $P$ be a Sylow $p$-subgroup of a finite group $G$.
> 1. If $P$ is [[§38 Normal Subgroups#^def-38-1|normal]] in $G$, then $P$ is the only Sylow $p$-subgroup of $G$.
> 2. Conversely, if $P$ is the only Sylow $p$-subgroup of $G$, then $P \trianglelefteq G$.
>
> *Source: lecture 10/16; (2) not stated in lecture*

^cor-55-7

> [!proof]+ Proof
> **(1) (lecture).** Let $Q$ be any Sylow $p$-subgroup. By the Second Sylow Theorem (Theorem [[§55 The Sylow Theorems#^thm-55-6|§55.6]]), $Q = gPg^{-1}$ for some $g \in G$, and $gPg^{-1} = P$ because $P$ is normal (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]). So $Q = P$.
>
> **(2)** *(Not stated in lecture; used in the example of order $15$ below.)* For $g \in G$, $gPg^{-1}$ is a subgroup with $|gPg^{-1}| = |P|$ (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]), so it is a Sylow $p$-subgroup, hence equal to $P$. So $gPg^{-1} = P$ for every $g \in G$: $P$ is normal.

^pf-55-7

*Uses:* [[§55 The Sylow Theorems#^thm-55-6|§55.6]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

> [!theorem] Lemma §55.8: The Order of a Product of Subgroups
> Let $H$ and $L$ be finite subgroups of a group $G$, and $HL = \{hl : h \in H,\ l \in L\}$ (Definition [[§41 The First and Second Isomorphism Theorems#^def-41-1|§41.1]]). Then
>
> $$ |HL| = \frac{|H|\,|L|}{|H \cap L|}. $$
>
> *Source: not from lecture; the lecture uses it in the proof of the Third Sylow Theorem*

^lem-55-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Consider the surjective map $\mu : H \times L \to HL$, $\mu(h, l) = hl$. We show that every element of $HL$ has exactly $|H \cap L|$ preimages; then $|H \times L| = |HL| \cdot |H \cap L|$, which is the formula.
>
> Fix $hl \in HL$. For $d \in H \cap L$, $(hd, d^{-1}l) \in H \times L$ and $\mu(hd, d^{-1}l) = hdd^{-1}l = hl$; distinct $d$ give distinct pairs. Conversely, if $\mu(h', l') = hl$, put $d = h^{-1}h'$. Then $d \in H$, and $d = h^{-1}h' = l\,l'^{-1}$ (from $h'l' = hl$), so $d \in L$; and $h' = hd$, $l' = d^{-1}l$. So the preimages of $hl$ are exactly the $|H \cap L|$ pairs $(hd, d^{-1}l)$, $d \in H \cap L$.

^pf-55-8

*Uses:* [[§41 The First and Second Isomorphism Theorems#^def-41-1|Def. §41.1]]

> [!theorem] Theorem §55.9: The Third Sylow Theorem
> For any finite group $G$, the number of Sylow $p$-subgroups of $G$ is [[§6 Divisibility and Congruence#^def-6-3|congruent]] to $1 \bmod p$ (Definition [[§6 Divisibility and Congruence#^def-6-3|§6.3]]): it equals $1 + kp$ for some integer $k \ge 0$, i.e. it leaves remainder $1$ on division by $p$.
>
> *Source: stated on WS 10; lecture 10/16*

^thm-55-9

> [!proof]+ Proof
> *Idea:* Let $P$ act on the Sylow $p$-subgroups by conjugation; $P$ is its only fixed point.
>
> *(Lecture 10/16.)* Let $|G| = p^k m$ with $p \nmid m$, and let $X$ be the set of Sylow $p$-subgroups of $G$. $X$ is nonempty by the First Sylow Theorem (Theorem [[§55 The Sylow Theorems#^thm-55-4|§55.4]]); fix $P \in X$.
>
> *The action.* $G$ acts on $X$ by conjugation, $g \star Q = gQg^{-1}$: $gQg^{-1}$ is a subgroup with $|gQg^{-1}| = |Q|$ (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]), so it lies in $X$, and the action axioms are checked as for the conjugation action on elements (Proposition [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]]). By the Second Sylow Theorem there is only one orbit. Restrict the action to $P$.
>
> *Counting modulo $p$.* $X$ breaks up into $P$-orbits (Proposition [[§27 Orbits#^prop-27-1|§27.1]]). Each $P$-orbit has size dividing $|P| = p^k$ (Orbit–Stabilizer, Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]), so size $p^\ell$ for some $\ell \geq 0$; it is $\equiv 0 \pmod p$ unless $\ell = 0$, that is, unless the orbit is a single fixed point. Writing $X^P = \{Q \in X : xQx^{-1} = Q \text{ for all } x \in P\}$ for the set of points fixed by $P$,
>
> $$ |X| \equiv |X^P| \pmod p. $$
>
> $P$ itself is in $X^P$: for $x \in P$, $xPx^{-1} = P$.
>
> *No other fixed point.* We show that if $Q \in X$ and $Q \neq P$, then $P$ does not fix $Q$. Assume for contradiction that $xQx^{-1} = Q$ for all $x \in P$.
>
> *Claim: $PQ$ is a subgroup of $G$.* For $x_1, x_2 \in P$ and $q_1, q_2 \in Q$,
>
> $$ (x_1q_1)(x_2q_2) = (x_1x_2)\,(x_2^{-1}q_1x_2)\,q_2 , $$
>
> with $x_1x_2 \in P$ and $x_2^{-1}q_1x_2 \in Q$ by the assumption (applied to $x_2^{-1} \in P$); so $PQ$ is closed under products. *(Filled in:)* $e = ee \in PQ$, and for $x \in P$, $q \in Q$, $(xq)^{-1} = q^{-1}x^{-1} = x^{-1}\,(xq^{-1}x^{-1}) \in PQ$, again by the assumption. This proves the claim.
>
> *Its order.* $P \cap Q$ is a subgroup of $P$, so $|P \cap Q| = p^j$ with $j \leq k$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]); and $j < k$, since $j = k$ would give $P = P \cap Q \subseteq Q$, hence $P = Q$ (both have $p^k$ elements). By the Order of a Product of Subgroups (Lemma [[§55 The Sylow Theorems#^lem-55-8|§55.8]]),
>
> $$ |PQ| = \frac{|P|\,|Q|}{|P \cap Q|} = \frac{p^k \cdot p^k}{p^j} = p^{2k - j}, \qquad 2k - j > k. $$
>
> But $p^k$ is the largest power of $p$ dividing $|G|$, so $|PQ| \nmid |G|$, contradicting Lagrange. So $P$ fixes no $Q \neq P$.
>
> *Conclusion.* $X^P = \{P\}$, so $|X| = 1 + (\text{sizes } p^\ell,\ \ell \geq 1, \text{ of the other orbits}) \equiv 1 \pmod p$.

^pf-55-9

*Uses:* [[§55 The Sylow Theorems#^thm-55-4|§55.4]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|§34.1]], [[§55 The Sylow Theorems#^thm-55-6|§55.6]], [[§27 Orbits#^prop-27-1|§27.1]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§55 The Sylow Theorems#^lem-55-8|§55.8]]

![[m493-52-1.svg]]

*The counting in the proof, for $G = S_4$ and $p = 3$ (not from lecture).* $P = \langle (1\,2\,3) \rangle$ acts by conjugation on the four Sylow $3$-subgroups ([[§54 p-Groups and Sylow Subgroups#^ex-54-1|Example §54.1]]): it fixes itself, and conjugation by $(1\,2\,3)$ permutes the other three in a cycle, an orbit of size $3$. So $n_3 = 1 + 3 \equiv 1 \pmod 3$.

> [!theorem] Corollary §55.10: The Number of Sylow Subgroups Divides $|G|$
> Let $G$ be finite, $|G| = p^k m$ with $p \nmid m$, and let $n_p$ be the number of Sylow $p$-subgroups of $G$. Then $n_p$ divides $|G|$; in fact $n_p$ divides $m$. Together with the Third Sylow Theorem: $n_p \mid m$ and $n_p \equiv 1 \pmod p$.
>
> *Source: lecture 10/16 ($n_p$ divides $|G|$); $n_p \mid m$ not from lecture*

^cor-55-10

> [!proof]+ Proof
> *Idea:* Orbit–stabilizer for the single conjugation orbit; the stabilizer of $P$ contains $P$.
>
> By the Second Sylow Theorem, the conjugation action of $G$ on the set $X$ of Sylow $p$-subgroups (proof of Theorem [[§55 The Sylow Theorems#^thm-55-9|§55.9]]) has one orbit, $X = G \star P$ for any $P \in X$. By Orbit–Stabilizer (Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]), $|G| = n_p \cdot |\operatorname{Stab}_G(P)|$, so $n_p$ divides $|G|$ (lecture). *(Not from lecture:)* $P \subseteq \operatorname{Stab}_G(P)$, since $xPx^{-1} = P$ for $x \in P$; so $p^k$ divides $|\operatorname{Stab}_G(P)|$ (Lagrange), and $n_p = p^k m / |\operatorname{Stab}_G(P)|$ divides $m$.

^pf-55-10

*Uses:* [[§55 The Sylow Theorems#^thm-55-6|§55.6]], [[§55 The Sylow Theorems#^thm-55-9|§55.9]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §55.2: The Sylow $5$-Subgroups of $S_5$
> $|S_5| = 120 = 2^3 \cdot 3 \cdot 5$, so a [[§54 p-Groups and Sylow Subgroups#^def-54-2|Sylow]] $5$-subgroup has order $5$. It is cyclic, generated by each of its $4$ non-identity elements (Groups of Prime Order, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]), and an element of order $5$ in $S_5$ is a $5$-cycle. There are $4! = 24$ five-cycles: writing a $5$-cycle as $(1\,a\,b\,c\,d)$, it is determined by the order of $a, b, c, d$. Two distinct subgroups of order $5$ meet in a subgroup whose order divides $5$ and is not $5$, so only in $e$. Hence the $24$ five-cycles fall into disjoint groups of $4$, one for each Sylow $5$-subgroup:
>
> $$ n_5 = \frac{24}{4} = 6 . $$
>
> As the Sylow theorems require, $6 \equiv 1 \pmod 5$ (Theorem [[§55 The Sylow Theorems#^thm-55-9|§55.9]]) and $6$ divides $120 / 5 = 24$ (Corollary [[§55 The Sylow Theorems#^cor-55-10|§55.10]]).
>
> *Source: lecture 10/16*

^ex-55-2

![[m493-52-2.svg]]

*The six Sylow $5$-subgroups of $S_5$ (not from lecture).* Each subgroup contains exactly one $5$-cycle sending $1 \mapsto 2$, so they can be listed as $\langle (1\,2\,a\,b\,c) \rangle$ with $(a, b, c)$ an ordering of $3, 4, 5$. They share only $e$.

## Groups of Order pq

*Lecture 10/16.* The first classification by the Sylow theorems: counting Sylow subgroups forces them to be normal, and two normal subgroups of coprime orders split the group.

> [!example] Example §55.3: Groups of Order $15$
> Let $|G| = 15 = 3 \cdot 5$. Then $G \cong \mathbb{Z}/15\mathbb{Z}$.
> 1. *One Sylow $3$-subgroup.* $n_3$ divides $15$, so $n_3 \in \{1, 3, 5, 15\}$ (Corollary [[§55 The Sylow Theorems#^cor-55-10|§55.10]]), and $n_3 \equiv 1 \pmod 3$ (Theorem [[§55 The Sylow Theorems#^thm-55-9|§55.9]]); only $1$ qualifies. So there is one Sylow $3$-subgroup $P_3$, and it is normal (Corollary [[§55 The Sylow Theorems#^cor-55-7|§55.7]], part 2).
> 2. *One Sylow $5$-subgroup.* The same for $5$: of $1, 3, 5, 15$ only $1$ is $\equiv 1 \pmod 5$. So $P_5$ is unique and normal.
> 3. *Trivial intersection.* $|P_3 \cap P_5|$ divides $3$ and $5$ (Lagrange), so $P_3 \cap P_5 = \{e\}$.
> 4. *Splitting.* $P_3$ and $P_5$ are normal with trivial intersection and $|P_3|\,|P_5| = 15 = |G|$, so by Internal Direct Products (Lemma [[§54 p-Groups and Sylow Subgroups#^lem-54-6|§54.6]]) $G = P_3P_5 \cong P_3 \times P_5$. Each $P_i$ has prime order, hence is cyclic (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]): $G \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \cong \mathbb{Z}/15\mathbb{Z}$ by the Chinese Remainder Theorem (Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]]).
>
> So every group with $15$ elements is cyclic.
>
> *Source: lecture 10/16*

^ex-55-3

![[m493-52-3.svg]]

*The subgroups used in the example (not from lecture): the two normal Sylow subgroups meet in $\{e\}$, and their product is all of $G$.*

> [!theorem] Proposition §55.11: Groups of Order $pq$
> Let $p < q$ be primes with $q \not\equiv 1 \pmod p$, and let $|G| = pq$. Then $G \cong \mathbb{Z}/pq\mathbb{Z}$.
>
> *Source: lecture 10/16, stated after the case $|G| = 15$); proof filled in*

^prop-55-11

> [!proof]+ Proof
> *Idea:* Sylow counting forces $n_p = n_q = 1$; the two normal cyclic Sylow subgroups split $G$.
>
> *(Filled in, following the case $|G| = 15$.)* The divisors of $pq$ are $1, p, q, pq$.
>
> *$n_q = 1$.* $n_q$ divides $pq$ and $n_q \equiv 1 \pmod q$ (Corollary [[§55 The Sylow Theorems#^cor-55-10|§55.10]], Theorem [[§55 The Sylow Theorems#^thm-55-9|§55.9]]). Modulo $q$: $q \equiv pq \equiv 0$, and $p \not\equiv 1$ since $1 < p < q$. So $n_q = 1$.
>
> *$n_p = 1$.* $n_p$ divides $pq$ and $n_p \equiv 1 \pmod p$. Modulo $p$: $p \equiv pq \equiv 0$, and $q \not\equiv 1$ by hypothesis. So $n_p = 1$.
>
> *Conclusion.* The unique Sylow subgroups $P_p$ and $P_q$ are normal (Corollary [[§55 The Sylow Theorems#^cor-55-7|§55.7]], part 2), of prime orders $p$ and $q$, so cyclic (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]); $P_p \cap P_q = \{e\}$ because its order divides $p$ and $q$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]); and $|P_p|\,|P_q| = pq = |G|$. By Internal Direct Products (Lemma [[§54 p-Groups and Sylow Subgroups#^lem-54-6|§54.6]]) and the Chinese Remainder Theorem (Theorem [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]], $\gcd(p, q) = 1$),
>
> $$ G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z} \cong \mathbb{Z}/pq\mathbb{Z}. $$

^pf-55-11

*Uses:* [[§55 The Sylow Theorems#^cor-55-10|§55.10]], [[§55 The Sylow Theorems#^thm-55-9|§55.9]], [[§55 The Sylow Theorems#^cor-55-7|§55.7]], [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§54 p-Groups and Sylow Subgroups#^lem-54-6|§54.6]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]]

> [!example] Example §55.4: When q ≡ 1 mod p: $S_3$
> The hypothesis $q \not\equiv 1 \pmod p$ of Proposition [[§55 The Sylow Theorems#^prop-55-11|§55.11]] cannot be dropped: $|S_3| = 6 = 2 \cdot 3$ with $3 \equiv 1 \pmod 2$, and $S_3$ is not cyclic, as it is not even abelian: $(1\,2)(2\,3) = (1\,2\,3) \neq (1\,3\,2) = (2\,3)(1\,2)$. There $n_3 = 1$ but $n_2 = 3$ (Example [[§54 p-Groups and Sylow Subgroups#^ex-54-1|§54.1]]), so the Sylow $2$-subgroups are not normal and the splitting argument stops at the second step. What remains is a [[§58 Semidirect Products#^def-58-2|semidirect product]]: $S_3 \cong \mathbb{Z}/3\mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$ (Example [[§58 Semidirect Products#^ex-58-4|§58.4]]).
>
> *Source: not from lecture*

^ex-55-4

## Flags and the Sylow Subgroups of $GL_n(\mathbb{F}_p)$

*Source: office hours (Wed Nov 4), from the board. The board gives the orders and the orbit counts for $n = 2, 3$; the identification with flags, the Bruhat decomposition and the link to the Sylow count are not from class.*

Throughout, $G = GL_n(\mathbb{F}_p)$, $B \leq G$ is the subgroup of invertible upper triangular matrices, and $P \leq B$ is the unitriangular group of WS 10.2 (Proposition [[§54 p-Groups and Sylow Subgroups#^prop-54-5|§54.5]]), a Sylow $p$-subgroup of $G$. The board writes $U$ for $P$.

> [!definition] Definition §55.1: Complete Flag
> Let $k$ be a field. A **complete flag** in $k^n$ is a chain of subspaces
>
> $$
> 0 = V_0 \subset V_1 \subset V_2 \subset \cdots \subset V_n = k^n \qquad \text{with } \dim V_i = i.
> $$
>
> *Source: office hours 11/4*

^def-55-1

The **standard flag** $\mathcal{F}_0$ has $V_i = \langle e_1, \ldots, e_i \rangle$. An invertible matrix $g$ maps an $i$-dimensional subspace to an $i$-dimensional subspace and preserves inclusions, so $g \cdot (V_i)_i = (gV_i)_i$ is an action of $GL_n(k)$ on the set of complete flags. In Example [[§52 The Jordan–Hölder Theorem#^ex-52-2|§52.2]] complete flags in $\mathbb{F}_p^n$ were composition series of $(\mathbb{Z}/p\mathbb{Z})^n$.

> [!theorem] Proposition §55.12: Complete Flags Are $G/B$
> The action of $GL_n(k)$ on complete flags in $k^n$ is transitive, and the stabilizer of $\mathcal{F}_0$ is the group $B$ of invertible upper triangular matrices. Hence $gB \mapsto g\mathcal{F}_0$ is a bijection from $GL_n(k)/B$ to the set of complete flags, and for $k = \mathbb{F}_p$,
>
> $$
> |G| = \prod_{j=0}^{n-1} (p^n - p^j), \qquad |B| = (p-1)^n p^{\binom{n}{2}}, \qquad \#\{\text{complete flags}\} = |G/B| = \frac{|G|}{|B|}.
> $$
>
> *Source: office hours 11/4 (the orders); the flag picture not from class*

^prop-55-12

> [!proof]+ Proof
> *Idea:* A flag is the same as a basis up to upper triangular change; the columns of $g$ are such a basis.
>
> *(Not from class.)* *Transitive:* given a flag $(V_i)$, choose $v_i \in V_i \setminus V_{i-1}$ for $i = 1, \ldots, n$. By induction on $i$, $v_1, \ldots, v_i$ is a basis of $V_i$: it is independent because $v_i \notin V_{i-1} = \langle v_1, \ldots, v_{i-1} \rangle$, and $\dim V_i = i$. The matrix $g$ with columns $v_1, \ldots, v_n$ is invertible and $g\langle e_1, \ldots, e_i \rangle = \langle v_1, \ldots, v_i \rangle = V_i$, so $g\mathcal{F}_0 = (V_i)$.
>
> *Stabilizer:* $g\langle e_1, \ldots, e_i \rangle = \langle e_1, \ldots, e_i \rangle$ for all $i$ holds iff $ge_i \in \langle e_1, \ldots, e_i \rangle$ for all $i$ (for “if”: then $g\langle e_1, \ldots, e_i \rangle \subseteq \langle e_1, \ldots, e_i \rangle$, with equality since $g$ is injective), that is, iff column $i$ of $g$ has zeros below row $i$ for every $i$: iff $g$ is upper triangular.
>
> The bijection is Orbit–Stabilizer (Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]) for the single orbit. The formula for $|G|$ is The Order of $GL_n(\mathbb{F}_p)$ (Proposition [[§54 p-Groups and Sylow Subgroups#^prop-54-4|§54.4]]). An invertible upper triangular matrix has nonzero diagonal entries (its determinant is their product), so there are $p - 1$ choices for each of the $n$ diagonal entries and $p$ for each of the $\binom{n}{2}$ entries above the diagonal.

^pf-55-12

*Uses:* [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§54 p-Groups and Sylow Subgroups#^prop-54-4|§54.4]]

> [!example] Example §55.5: The Unitriangular Group Acting on Flags
> Let $P$ act on $G/B$, that is, on complete flags in $\mathbb{F}_p^n$. The board computes, for $n = 2$ and $n = 3$:
>
> | | $n = 2$ | $n = 3$ |
> |---|---|---|
> | $\lvert G \rvert$ | $(p^2-1)(p^2-p)$ | $(p^3-1)(p^3-p)(p^3-p^2)$ |
> | $\lvert B \rvert$ | $(p-1)^2p$ | $(p-1)^3p^3$ |
> | $\lvert G/B \rvert$ | $\frac{p^2-1}{p-1} = p + 1$ | $\frac{(p^3-1)(p^2-1)}{(p-1)(p-1)} = (p^2+p+1)(p+1) = p^3 + 2p^2 + 2p + 1$ |
> | $P$-orbits | $p + 1$ | $p^3 + p^2 + p^2 + p + p + 1$ |
> | labels | $(1\,2)$, $e$ | $(1\,3)$; $(1\,2\,3)$, $(1\,3\,2)$; $(1\,2)$, $(2\,3)$; $e$ |
>
> 1. $n = 2$: a complete flag is just a line $V_1$ in $\mathbb{F}_p^2$, and there are $p + 1$ of them. $P = \left\{\left(\begin{smallmatrix} 1 & a \\ 0 & 1 \end{smallmatrix}\right) : a \in \mathbb{F}_p\right\}$ fixes $\langle e_1 \rangle$, an orbit of size $1$ (labeled $e$), and sends $\langle (b, 1) \rangle$ to $\langle (b + a, 1) \rangle$, so the other $p$ lines form one orbit of size $p$ (labeled $(1\,2)$).
> 2. $n = 3$: the $P$-orbits have sizes $p^3$, $p^2$, $p^2$, $p$, $p$, $1$, one for each permutation in $S_3$, the exponent being the number of inversions of the permutation (pairs $i < j$ with $w(i) > w(j)$): $(1\,3)$, which reverses $1, 2, 3$, has $3$; the $3$-cycles have $2$; the transpositions $(1\,2)$, $(2\,3)$ of neighbours have $1$; and $e$ has $0$. The orbit labeled $w$ is the one containing the flag $w\mathcal{F}_0$, with $w$ acting as the permutation matrix $e_i \mapsto e_{w(i)}$.
>
> *(Not from class.)* Checked by computer for $p = 2$ and $p = 3$: $3$ and $4$ flags for $n = 2$, and $21$ and $52$ for $n = 3$, with orbits of exactly these sizes, each containing exactly one flag $w\mathcal{F}_0$.
>
> *Source: office hours 11/4*

^ex-55-5

![[m493-55-3.svg]]

*(Not from lecture; figure added.)* Example §55.3(1) for $p = 3$: the $p + 1 = 4$ lines through $0$ in $\mathbb{F}_3^2$. The shears in $P$ fix the line $\langle e_1 \rangle$ and move the other three lines around among themselves, one orbit of size $p$.

![[m493-55-4.svg]]

> [!theorem] Proposition §55.13: The Bruhat Decomposition
> Let $G = GL_n(\mathbb{F}_p)$, with $B$ and $P$ as above, and view each $w \in S_n$ as a permutation matrix.
>
> 1. $G = \bigsqcup_{w \in S_n} BwB$ (the **Bruhat decomposition**).
> 2. Each $BwB/B \subseteq G/B$ is a single $P$-orbit of size $p^{\ell(w)}$, where $\ell(w)$ is the number of inversions of $w$.
> 3. Hence
>
> $$
> |G/B| = \sum_{w \in S_n} p^{\ell(w)} = (1 + p)(1 + p + p^2) \cdots (1 + p + \cdots + p^{n-1}),
> $$
>
> the “$p$-factorial”.
>
> *Source: not from class*

^prop-55-13

> [!proof]+ Proof (to be filled)
> Not proved in the course; the standard proof brings a matrix to the form $bwb'$ by row and column reduction with upper triangular matrices.

^pf-55-13

> [!remark] Remark: Flags and Relative Position
> The pattern of the board is general (Proposition [[§55 The Sylow Theorems#^prop-55-13|§55.13]]). At $p = 1$ the $p$-factorial gives $|S_n| = n!$. For $n = 3$: $(1 + p)(1 + p + p^2) = p^3 + 2p^2 + 2p + 1$, as on the board. The label $w$ of a flag is its relative position with respect to $\mathcal{F}_0$: up to replacing $w$ by $w^{-1}$ (a matter of conventions), it is the permutation that the Jordan–Hölder pipes read off from the two flags in Example [[§52 The Jordan–Hölder Theorem#^ex-52-2|§52.2]]. (Not proved here.)
>
> *Source: not from class*

^rem-55-3

*(Not from lecture; figure added.)* Example §55.3(2) for $p = 2$. The lines and planes of $\mathbb{F}_2^3$ are the points and lines of the Fano plane, so a complete flag is a point on a line, and there are $7 \cdot 3 = 21$. Each panel shows one flag $w\mathcal{F}_0$ and, below it, a description of its whole $P$-orbit relative to the standard flag $\langle e_1 \rangle \subset \langle e_1, e_2 \rangle$ ($P$ fixes both). Counting the flags that satisfy each description gives $1, p, p, p^2, p^2, p^3$, for every $p$.

> [!theorem] Proposition §55.14: Sylow $p$-Subgroups of $GL_n(\mathbb{F}_p)$ and Flags
> Let $G = GL_n(\mathbb{F}_p)$, with $B$ and $P$ as above.
>
> 1. The standard flag $\mathcal{F}_0$ is the only complete flag fixed by $P$.
> 2. $N_G(P) = B$, where $N_G(P) = \{ g \in G : gPg^{-1} = P \}$ is the normalizer of $P$.
> 3. $|G/B| \equiv 1 \pmod p$, and the number of Sylow $p$-subgroups of $G$ is $n_p = [G : B] = |G/B|$, the number of complete flags. For example $n_p\big(GL_2(\mathbb{F}_p)\big) = p + 1$ and $n_p\big(GL_3(\mathbb{F}_p)\big) = (p^2 + p + 1)(p + 1)$.
>
> *Source: not from class; suggested by the office-hours board*

^prop-55-14

> [!proof]+ Proof
> *Idea:* A fixed flag is pinned down one step at a time by the elementary matrices in $P$; then count $P$-orbits mod $p$ and identify the Sylow subgroups with the conjugates of $P$.
>
> *(Not from class.)* **(1)** $P$ fixes $\mathcal{F}_0$ because $P \subseteq B$ (Proposition [[§55 The Sylow Theorems#^prop-55-12|§55.12]]). For uniqueness we use induction on $n$, the case $n = 1$ being clear (there is one flag). Let $(V_i)$ be fixed by $P$, and $V_1 = \langle v \rangle$ with $v = (v_1, \ldots, v_n) \neq 0$. Suppose some coordinate $v_j$ with $j \geq 2$ is nonzero, and take the largest such $j$. The matrix $u = I + E_{j-1,j} \in P$, with a single $1$ above the diagonal in position $(j-1, j)$, gives $uv = v + v_j e_{j-1}$, which must equal $\lambda v$ for some $\lambda \in \mathbb{F}_p$, since $uV_1 = V_1$. Comparing $j$-th coordinates, $v_j = \lambda v_j$, so $\lambda = 1$ and then $v_j e_{j-1} = 0$, a contradiction. Hence $v \in \langle e_1 \rangle$ and $V_1 = \langle e_1 \rangle$.
>
> Now every $u \in P$ maps $\langle e_1 \rangle$ to itself, so it acts on the quotient space $\mathbb{F}_p^n / \langle e_1 \rangle$, which has basis $\bar e_2, \ldots, \bar e_n$ (the images of $e_2, \ldots, e_n$); in this basis $u$ acts by the lower right $(n-1) \times (n-1)$ block of $u$, and these blocks run over all unitriangular matrices of size $n - 1$. The images $V_2/\langle e_1 \rangle \subset \cdots \subset V_n/\langle e_1 \rangle$ form a complete flag in the quotient, fixed by all these blocks. By induction it is the standard one, $V_i/\langle e_1 \rangle = \langle \bar e_2, \ldots, \bar e_i \rangle$, so $V_i = \langle e_1, \ldots, e_i \rangle$ for all $i$.
>
> **(2)** $B \subseteq N_G(P)$: taking the diagonal is a homomorphism $B \to (\mathbb{F}_p^\times)^n$ (the diagonal of a product of upper triangular matrices is the product of the diagonals), with kernel $P$; kernels are normal (Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]), so $bPb^{-1} = P$ for $b \in B$. Conversely, let $gPg^{-1} = P$. For $u \in P$ we have $g^{-1}ug \in P$, which fixes $\mathcal{F}_0$, so
>
> $$
> u(g\mathcal{F}_0) = g\,(g^{-1}ug)\,\mathcal{F}_0 = g\mathcal{F}_0 :
> $$
>
> the flag $g\mathcal{F}_0$ is fixed by $P$. By (1), $g\mathcal{F}_0 = \mathcal{F}_0$, so $g \in B$ by Proposition [[§55 The Sylow Theorems#^prop-55-12|§55.12]].
>
> **(3)** $P$ is a $p$-group, so by Orbit–Stabilizer and Lagrange each $P$-orbit in $G/B$ has size dividing $|P|$, a power of $p$; the orbits of size $p, p^2, \ldots$ contribute $0 \bmod p$, and the orbits of size $1$ are the fixed flags. By (1) there is exactly one, so $|G/B| \equiv 1 \pmod p$. For the count: $G$ acts on the set of its Sylow $p$-subgroups by conjugation with a single orbit (Second Sylow Theorem, Theorem [[§55 The Sylow Theorems#^thm-55-6|§55.6]]), and the stabilizer of $P$ is $N_G(P)$. By Orbit–Stabilizer (Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]) and (2), $n_p = [G : N_G(P)] = [G : B]$. The congruence $|G/B| \equiv 1$ is thus the Third Sylow Theorem (Theorem [[§55 The Sylow Theorems#^thm-55-9|§55.9]]) for this group, proved by the fixed-point idea of WS 10.1 (Proposition [[§54 p-Groups and Sylow Subgroups#^prop-54-1|§54.1]]). The formula $n_p = [G : N(P)]$ in general is Proposition [[§56 Simple Groups of Small Order#^prop-56-4|§56.4]].

^pf-55-14

*Uses:* [[§55 The Sylow Theorems#^prop-55-12|§55.12]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§55 The Sylow Theorems#^thm-55-6|§55.6]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§55 The Sylow Theorems#^thm-55-9|§55.9]], [[§54 p-Groups and Sylow Subgroups#^prop-54-1|§54.1]], [[§56 Simple Groups of Small Order#^prop-56-4|§56.4]]
