---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 53
tags: [group-theory, math493]
---
← [[§52 The Sylow Theorems]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§54 Internal and External Direct Products]] →

*Source: Lecture and slides (Fri Oct 23). Reference: not covered in the Pinter chapters used so far.*

> [!remark] Remark: The Game
> Which numbers $n \leq 100$ are the order of a simple group? The slides list $n = 2, \ldots, 100$ and mark each $n$ with the test that rules it out: *prime*; $\clubsuit$, a prime power (Proposition [[§53 Simple Groups of Small Order#^prop-53-1|§53.1]]); $\diamondsuit p$, a prime $p$ for which $n_p = 1$ is forced (Corollary [[§53 Simple Groups of Small Order#^cor-53-3|§53.3]]); $\blacksquare p$, a prime $p$ for which $|G|$ does not divide $n_p!$ (Proposition [[§53 Simple Groups of Small Order#^prop-53-4|§53.4]]). After these tests only $30$, $56$, $60$ and $90$ survive. The orders $30$, $56$ and $90$ are ruled out on the homework, and $60$ is the order of $A_5$.
>
> *Source: lecture 10/23*

^rem-53-1

![[m493-53-1.svg]]

*(Not from lecture; figure added.)* The slides' table, recomputed: each $n \leq 100$ is coloured by the first test that rules it out, in the order prime, $\clubsuit$, $\diamondsuit p$, $\blacksquare p$. Exactly $30$, $56$, $60$ and $90$ survive. ($18$ is $\diamondsuit 3$, as corrected in lecture.)

> [!theorem] Proposition §53.1: Primes and Prime Powers
> 1. The trivial group is not simple.
> 2. If $|G| = p$ is prime, then $G \cong \mathbb{Z}/p\mathbb{Z}$ is simple.
> 3. If $|G| = p^k$ with $p$ prime and $k \geq 2$, then $G$ is not simple.
>
> *Source: lecture 10/23*

^prop-53-1

> [!proof]+ Proof
> *Idea:* for (3), the center is a nontrivial normal subgroup; it is proper unless $G$ is abelian, and abelian simple groups have prime order.
>
> **(1)** By Definition [[§43 Simple Groups#^def-43-1|§43.1]]: the trivial group has only one normal subgroup.
>
> **(2)** A group of prime order is cyclic, hence $\cong \mathbb{Z}/p\mathbb{Z}$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]), and it is simple by Theorem [[§43 Simple Groups#^thm-43-1|§43.1]].
>
> **(3)** The center $Z(G) = \{z \in G : zg = gz \text{ for all } g \in G\}$ (Definition [[§35 The Center#^def-35-2|§35.2]]) is nontrivial by Theorem [[§35 The Center#^thm-35-3|§35.3]], and it is normal in $G$: for $z \in Z(G)$ and $g \in G$, $gzg^{-1} = z$. If $Z(G) \neq G$, then $Z(G)$ is a proper nontrivial normal subgroup, and $G$ is not simple. If $Z(G) = G$, then $G$ is abelian, and an abelian simple group has prime order (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]); but $|G| = p^k$ with $k \geq 2$ is not prime. Either way $G$ is not simple.

^pf-53-1

*Uses:* [[§43 Simple Groups#^def-43-1|Def. §43.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]], [[§43 Simple Groups#^thm-43-1|§43.1]], [[§35 The Center#^def-35-2|Def. §35.2]], [[§35 The Center#^thm-35-3|§35.3]]

> [!remark] Remark: Notation for This Section
> Throughout, $G$ is finite, $p$ is a prime dividing $|G|$, and $|G| = p^k m$ with $p \nmid m$. Write $n_p$ for the number of Sylow $p$-subgroups of $G$. The conjugate $gPg^{-1}$ of a Sylow $p$-subgroup $P$ is again a Sylow $p$-subgroup, since conjugation by $g$ is an isomorphism (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]); so $G$ acts on the set of Sylow $p$-subgroups by conjugation, $g \cdot P = gPg^{-1}$, as in the proof of Theorem [[§52 The Sylow Theorems#^thm-52-9|§52.9]].

^rem-53-2

> [!definition] Definition §53.1: Normalizer
> Let $H \leq G$. The **normalizer** of $H$ in $G$ is
>
> $$
> N_G(H) = N(H) := \{ g \in G : gHg^{-1} = H \},
> $$
>
> the stabilizer of $H$ under the action of $G$ on its subgroups by conjugation.
>
> *Source: lecture 10/23*

^def-53-1

> [!remark] Remark: Basic Properties of the Normalizer
> $N(H)$ is a subgroup of $G$, since stabilizers are subgroups (Proposition [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]]); it contains $H$, since $hHh^{-1} = H$ for $h \in H$; and $H \trianglelefteq N(H)$, directly from the definition. $H$ is normal in $G$ (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]) if and only if $N(H) = G$.

^rem-53-3

> [!theorem] Proposition §53.2: $n_p$ and the Normalizer
> Let $P$ be a Sylow $p$-subgroup of $G$. Then $n_p = [G : N(P)]$, and
>
> $$
> m = [N(P) : P] \cdot n_p.
> $$
>
> In particular $n_p$ divides $m$ (Corollary [[§52 The Sylow Theorems#^cor-52-10|§52.10]]). Together with the Third Sylow Theorem (Theorem [[§52 The Sylow Theorems#^thm-52-9|§52.9]]), $n_p \mid m$ and $n_p \equiv 1 \pmod p$.
>
> *Source: lecture 10/23*

^prop-53-2

> [!proof]+ Proof
> *Idea:* orbit–stabilizer for the single conjugation orbit, whose stabilizer is $N(P) \supseteq P$.
>
> *(Board 10/23.)* Let $G$ act on the set of Sylow $p$-subgroups by conjugation. By the Second Sylow Theorem (Theorem [[§52 The Sylow Theorems#^thm-52-6|§52.6]]), any two Sylow $p$-subgroups are conjugate, so there is only one orbit, of size $n_p$. The stabilizer of $P$ is $\operatorname{Stab}(P) = \{g \in G : gPg^{-1} = P\} = N(P)$ (Definition [[§53 Simple Groups of Small Order#^def-53-1|§53.1]]). By Orbit–Stabilizer (Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]), $n_p = [G : N(P)]$, and using Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) for $P \leq N(P)$,
>
> $$
> p^k m = |G| = |N(P)| \cdot n_p = |P| \cdot [N(P) : P] \cdot n_p = p^k \, [N(P) : P] \cdot n_p.
> $$
>
> Cancelling $p^k$ gives $m = [N(P) : P] \cdot n_p$.

^pf-53-2

*Uses:* [[§52 The Sylow Theorems#^thm-52-6|§52.6]], [[§53 Simple Groups of Small Order#^def-53-1|Def. §53.1]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!proof]+ Alternative proof that $n_p \mid m$ (number theory)
> *(Board 10/23.)* From $n_p = [G : N(P)]$, $n_p$ divides $|G| = p^k m$. By the Third Sylow Theorem (Theorem [[§52 The Sylow Theorems#^thm-52-9|§52.9]]) $n_p \equiv 1 \pmod p$, so $p \nmid n_p$; hence no factor of $p$ occurs in $n_p$, and $n_p$ divides $m$.

^pf-53-2-2

*Uses:* [[§52 The Sylow Theorems#^thm-52-9|§52.9]]

![[m493-53-2.svg]]

*(Not from lecture; figure added.)* Left: the chain $\{e\} \leq P \leq N(P) \leq G$ with its indices; the index $m$ of $P$ in $G$ splits as $[N(P) : P] \cdot n_p$. Right: $G$ permutes the Sylow $p$-subgroups $P_1, \ldots, P_{n_p}$ transitively by conjugation (Theorem [[§52 The Sylow Theorems#^thm-52-6|§52.6]]); the stabilizer of $P_1$ is $N(P_1)$, so the orbit has $[G : N(P_1)]$ points.

> [!theorem] Corollary §53.3: A Unique Sylow Subgroup Rules Out Simplicity
> If $n_p = 1$, then the Sylow $p$-subgroup $P$ is normal in $G$. If moreover $|G|$ is not a power of $p$, then $\{e\} \neq P \neq G$, so $G$ is not simple.
>
> *Source: lecture 10/23*

^cor-53-3

> [!proof]+ Proof
> $P$ is normal by Corollary [[§52 The Sylow Theorems#^cor-52-7|§52.7]](2): $gPg^{-1}$ is a Sylow $p$-subgroup for every $g \in G$, and $P$ is the only one, so $gPg^{-1} = P$. Since $p$ divides $|G|$, $|P| = p^k > 1$; if $|G|$ is not a power of $p$, then $m > 1$, so $|P| = p^k < |G|$.

^pf-53-3

*Uses:* [[§52 The Sylow Theorems#^cor-52-7|§52.7]]

> [!remark] Remark: The Sylow Test
> So to show that no group of order $n$ is simple, it suffices to find a prime $p \mid n$ such that the only divisor $d$ of $m$ with $d \equiv 1 \pmod p$ is $d = 1$ (Proposition [[§53 Simple Groups of Small Order#^prop-53-2|§53.2]], Corollary [[§53 Simple Groups of Small Order#^cor-53-3|§53.3]]). This rules out a large part of the table.

^rem-53-4

> [!example] Example §53.1: Order $21$
> $21 = 3 \cdot 7$. The candidates are: $n_3 \mid 7$ and $n_3 \equiv 1 \pmod 3$, so $n_3 \in \{1, 7\}$; $n_7 \mid 3$ and $n_7 \equiv 1 \pmod 7$, so $n_7 = 1$ ($3 \not\equiv 1 \pmod 7$). Hence the Sylow $7$-subgroup is normal, and no group of order $21$ is simple. (Marked $\diamondsuit 7$ on the slides.) Both values of $n_3$ occur: $n_3 = 1$ for $\mathbb{Z}/21\mathbb{Z}$, and $n_3 = 7$ for $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$ (Example [[§55 Semidirect Products#^ex-55-2|§55.2]]).
>
> *Source: lecture 10/23*

^ex-53-1

> [!example] Example §53.2: Four Orders That Survive the Sylow Test
> The class split into four groups to compute the candidates for $n_p$, namely the divisors $d$ of $m$ with $d \equiv 1 \pmod p$:
> | Order | $p$ | candidates for $n_p$ |
> |---|---|---|
> | $12 = 2^2 \cdot 3$ | $2$ | $1, 3$ |
> |  | $3$ | $1, 4$ |
> | $56 = 2^3 \cdot 7$ | $2$ | $1, 7$ |
> |  | $7$ | $1, 8$ |
> | $60 = 2^2 \cdot 3 \cdot 5$ | $2$ | $1, 3, 5, 15$ |
> |  | $3$ | $1, 4, 10$ |
> |  | $5$ | $1, 6$ |
> | $80 = 2^4 \cdot 5$ | $2$ | $1, 5$ |
> |  | $5$ | $1, 16$ |
> For each of these orders and each prime, some $n_p > 1$ is allowed, so the Sylow test alone does not rule them out. (The lecture also corrected the slides: $18 = 2 \cdot 3^2$ should be marked $\diamondsuit 3$, since $n_3 \mid 2$ and $n_3 \equiv 1 \pmod 3$ force $n_3 = 1$.)
>
> *Source: lecture 10/23*

^ex-53-2

> [!theorem] Proposition §53.4: The Conjugation Homomorphism $G \to S_{n_p}$
> Suppose $n_p > 1$. Numbering the Sylow $p$-subgroups $1, \ldots, n_p$, the conjugation action gives a homomorphism
>
> $$
> \varphi: G \to S_{n_p}.
> $$
>
> Then $\operatorname{Ker}\varphi \neq G$. Consequently, if $G$ is simple, then $\varphi$ is injective and $|G|$ divides $n_p!$. Equivalently: if $|G| \nmid n_p!$, then $\operatorname{Ker}\varphi$ is a proper nontrivial normal subgroup and $G$ is not simple.
>
> *Source: lecture 10/23*

^prop-53-4

> [!proof]+ Proof
> *Idea:* a transitive action on $n_p > 1$ points is not trivial, so its kernel is a normal subgroup other than $G$.
>
> An action on a set with $n_p$ elements is a homomorphism to $S_{n_p}$ (Theorem [[§25 Actions#^thm-25-3|§25.3]]). By the Second Sylow Theorem (Theorem [[§52 The Sylow Theorems#^thm-52-6|§52.6]]) the action is transitive, and there are $n_p > 1$ points, so some $g$ moves some point: $\varphi$ is not trivial, i.e. $\operatorname{Ker}\varphi \neq G$. Kernels are normal (Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]), so if $G$ is simple then $\operatorname{Ker}\varphi = \{e\}$, and $\varphi$ is injective. Then $G \cong \varphi(G) \leq S_{n_p}$ (First Isomorphism Theorem, Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]), so $|G|$ divides $|S_{n_p}| = n_p!$ by Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

^pf-53-4

*Uses:* [[§25 Actions#^thm-25-3|§25.3]], [[§52 The Sylow Theorems#^thm-52-6|§52.6]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §53.3: Orders $12$ and $80$
> 1. $|G| = 12$. If $n_2 = 1$, the Sylow $2$-subgroup is normal. If $n_2 = 3$, we get $\varphi: G \to S_3$, and $12 > 6 = |S_3|$, so $\varphi$ is not injective: $\operatorname{Ker}\varphi$ is a proper nontrivial normal subgroup. Either way $G$ is not simple. (Marked $\blacksquare 2$.)
> 2. $|G| = 80$. If $n_2 = 1$ we are done. If $n_2 = 5$, we get $\varphi: G \to S_5$ with $|S_5| = 5! = 120$. Here $80 < 120$, but $80 \nmid 120$, so again $\varphi$ is not injective. (Marked $\blacksquare 2$.)
>
> This test does not kill $56$ or $60$: $56$ divides $7!$ and $8!$, and $60$ divides $5!$, $6!$, $10!$ and $15!$.
>
> *Source: lecture 10/23*

^ex-53-3

> [!theorem] Lemma §53.5: Homomorphisms That Leave $A_N$
> Let $\varphi: G \to S_N$ be a homomorphism with $\varphi(G) \not\subseteq A_N$, and suppose $|G| > 2$. Then $G$ is not simple: $\varphi^{-1}(A_N)$ is a normal subgroup of $G$ of index $2$.
>
> *Source: lecture and slides 10/23*

^lem-53-5

> [!proof]+ Proof
> *Idea:* the composite $\operatorname{sgn} \circ \varphi : G \to \{\pm 1\}$ is a homomorphism onto a group of order $2$; its kernel is normal, not all of $G$, and not trivial.
>
> *(Board 10/23; the lecture's version: normal subgroups come from kernels, so to find one, build a map.)* Let $\psi = \operatorname{sgn} \circ \varphi: G \to S_N \to \{\pm 1\}$, a homomorphism (Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]]). Then $\operatorname{Ker}\psi \trianglelefteq G$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). $\operatorname{Ker}\psi \neq G$, because $\operatorname{Ker}\psi = \varphi^{-1}(\operatorname{Ker}\operatorname{sgn}) = \varphi^{-1}(A_N)$ (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]) and $\varphi(G) \not\subseteq A_N$. And $\operatorname{Ker}\psi \neq \{e\}$, because $|G| > 2 = |\{\pm 1\}|$, so $\psi$ cannot be injective. Hence $\operatorname{Ker}\psi$ is a proper nontrivial normal subgroup. It has index $2$: $\psi$ is onto $\{\pm 1\}$ (its image is not $\{1\}$), so $G/\operatorname{Ker}\psi \cong \{\pm 1\}$ (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).

^pf-53-5

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

> [!proof]+ Second proof (indices)
> *(Not from class.)* Let $H = \varphi^{-1}(A_N)$. It is normal in $G$: for $h \in H$ and $g \in G$, $\varphi(ghg^{-1}) = \varphi(g)\varphi(h)\varphi(g)^{-1} \in A_N$, because $A_N \trianglelefteq S_N$ (it is the kernel of $\operatorname{sgn}$, Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). The rule $gH \mapsto \varphi(g)A_N$ is well defined and injective ($\varphi(g)A_N = \varphi(g')A_N \iff \varphi(g^{-1}g') \in A_N \iff g^{-1}g' \in H$), so $[G : H] \leq [S_N : A_N] = 2$. Hence $|H| \geq |G|/2 > 1$, so $H \neq \{e\}$; and $H \neq G$ because $\varphi(G) \not\subseteq A_N$.

^pf-53-5-2

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]

> [!theorem] Corollary §53.6: Simple Groups Land in $A_{n_p}$
> If $G$ is simple with $|G| > 2$, then every homomorphism $G \to S_N$ has image in $A_N$. In particular, if $n_p > 1$, then $G$ embeds in $A_{n_p}$, and $|G|$ divides $n_p!/2$.
>
> *Source: lecture and slides 10/23*

^cor-53-6

> [!proof]+ Proof
> The first statement is Lemma [[§53 Simple Groups of Small Order#^lem-53-5|§53.5]]. For the second, the map $\varphi: G \to S_{n_p}$ of Proposition [[§53 Simple Groups of Small Order#^prop-53-4|§53.4]] is injective with image in $A_{n_p}$, so $|G|$ divides $|A_{n_p}| = n_p!/2$ by Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

^pf-53-6

*Uses:* [[§53 Simple Groups of Small Order#^lem-53-5|§53.5]], [[§53 Simple Groups of Small Order#^prop-53-4|§53.4]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §53.4: Order $112$
> The first order where the lemma is needed for the Sylow action is beyond the table: $112 = 2^4 \cdot 7$. Here $n_2 \in \{1, 7\}$ and $n_7 \in \{1, 8\}$. If $G$ were simple, $n_2 = 7$ and $G$ would embed in $S_7$. Now $112$ divides $7! = 5040$ ($5040 = 45 \cdot 112$), so Proposition [[§53 Simple Groups of Small Order#^prop-53-4|§53.4]] alone does not help; but $112 \nmid 7!/2 = 2520$, so by Corollary [[§53 Simple Groups of Small Order#^cor-53-6|§53.6]] $G$ is not simple.
>
> *Source: slides 10/23*

^ex-53-4

> [!remark] Remark: Other Embeddings
> The homework uses another way of mapping a group into a symmetric group, besides the action on Sylow subgroups, together with the lemma, to rule out the orders $30$ and $90$, and yet another trick to rule out $56$. These are left to the homework.
>
> *Source: slides 10/23*

^rem-53-5

> [!theorem] Theorem §53.7: Simple Groups of Order at Most $100$
> If $G$ is a simple group with $|G| \leq 100$, then either $G \cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$, or $|G| = 60$.
>
> *Source: lecture 10/23*

^thm-53-7

> [!proof]+ Proof (to be filled)
> The results of this section rule out every order except the primes and $30$, $56$, $60$, $90$. The cases $30$, $56$ and $90$ are on the current homework (Problem Set 7), to be added after submission.

^pf-53-7

Since $A_5$ is simple of order $60$ (Proposition [[§43 Simple Groups#^prop-43-6|§43.6]]), the order $60$ does occur; the homework also shows that every simple group of order $60$ is isomorphic to $A_5$. Once filled in, the proof also gives Theorem [[§43 Simple Groups#^thm-43-7|§43.7]]: every non-abelian simple group has order at least $60$.

> [!remark] Remark: The Classification of Finite Simple Groups
> *(Overview only.)* The classification was an enormous 20th-century project, run in two streams in parallel: ruling out more and more orders, with computations like those above, and finding new ways to construct simple groups. The proof is spread over journal articles totalling about $10{,}000$ pages. There is an ongoing effort to collect it in one place and check that it has no gaps, and ultimately to verify it in a proof assistant such as Lean. Very roughly, every finite simple group is one of the following.
>
> 1. The cyclic groups $\mathbb{Z}/p\mathbb{Z}$, $p$ prime.
> 2. The alternating groups $A_n$ for $n \neq 1, 2, 4$. ($A_1$ and $A_2$ are trivial and $A_4$ is not simple; $A_3 \cong \mathbb{Z}/3\mathbb{Z}$ is already in the first family, so one usually says $n \geq 5$.)
> 3. The groups of Lie type, very roughly groups of matrices with entries in a finite field. The most tractable are the $PSL_n(\mathbb{F}_q)$, $\mathbb{F}_q$ a finite field with $q$ elements, $n \geq 2$, except $(n, q) = (2, 2)$ and $(2, 3)$, where $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$ (Theorem [[§43 Simple Groups#^thm-43-13|§43.13]]). There are coincidences between the families: $PSL_2(\mathbb{F}_4) \cong PSL_2(\mathbb{F}_5) \cong A_5$.
> 4. $26$ sporadic groups, which fit in no family. The largest is the **Monster**, of order
>
> $$
> 2^{46} \cdot 3^{20} \cdot 5^{9} \cdot 7^{6} \cdot 11^{2} \cdot 13^{3} \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 \cdot 41 \cdot 47 \cdot 59 \cdot 71 \approx 8 \times 10^{53}.
> $$
>
> For a long time this order was a number that passed every test without anyone being able to construct a group of that order, and no proof of the classification could be complete until the Monster was either constructed or ruled out. (It was first constructed by Robert Griess, around 1980–82; later constructions are due to Conway and others. Not from class.)
>
> In the lecturer's working summary: there is $\mathbb{Z}/p\mathbb{Z}$, there are the alternating groups, there is $PSL$ and things like it, and there are the sporadic groups.
>
> *Source: lecture 10/23*

^rem-53-6

> [!remark] Remark: Where the Groups of Lie Type Come From
> *(Overview only.)* A **Lie group** is a group that is also a manifold, with the group operations smooth. There is a much easier classification, due to Killing and Cartan (late 19th century), of the compact Lie groups. Roughly, they fall into three infinite families,
>
> $$
> \begin{aligned}O_n(\mathbb{R}) &= \{ g \in GL_n(\mathbb{R}) : g g^{T} = I_n \} && \text{(orthogonal group)}, \\
> U_n(\mathbb{C}) &= \{ g \in GL_n(\mathbb{C}) : g \bar{g}^{T} = I_n \} && \text{(unitary group)}, \\
> Sp(n) &= \{ g \in GL_n(\mathbb{H}) : g \bar{g}^{T} = I_n \} && \text{(quaternionic unitary group)},\end{aligned}
> $$
>
> where $\mathbb{H}$ denotes the quaternions (notation for the third family varies), together with five exceptional groups with the unbeautiful names $E_6$, $E_7$, $E_8$, $F_4$, $G_2$. The groups of Lie type arise by replacing $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ by finite fields and doing the analogous constructions with matrices over finite fields. For example, the $n \times n$ matrices over $\mathbb{F}_q$ with $gg^{T} = I_n$ form a finite orthogonal group, and passing to a suitable subgroup and quotient (in the spirit of $SL_n \to PSL_n$) gives simple groups. There are choices when making this replacement, so a single family on the Lie side can give several families of finite groups.
>
> *Source: lecture 10/23*

^rem-53-7
