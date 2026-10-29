---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 54
tags: [group-theory, math493]
---
← [[§53 The Sylow Theorems]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§55 Internal and External Direct Products]] →

*Source: Lecture and slides (Fri Oct 23). Reference: not covered in the Pinter chapters used so far.*

> [!remark] Remark: The Game
> Which numbers $n \leq 100$ are the order of a simple group? The slides list $n = 2, \ldots, 100$ and mark each $n$ with the test that rules it out: *prime*; $\clubsuit$, a prime power (Proposition [[§54 Simple Groups of Small Order#^prop-54-1|§54.1]]); $\diamondsuit p$, a prime $p$ for which $n_p = 1$ is forced (Corollary [[§54 Simple Groups of Small Order#^cor-54-3|§54.3]]); $\blacksquare p$, a prime $p$ for which $|G|$ does not divide $n_p!$ (Proposition [[§54 Simple Groups of Small Order#^prop-54-4|§54.4]]). After these tests only $30$, $56$, $60$ and $90$ survive. The orders $30$, $56$ and $90$ are ruled out on the homework, and $60$ is the order of $A_5$.
>
> *Source: lecture 10/23*

^rem-54-1

![[m493-53-1.svg]]

*(Not from lecture; figure added.)* The slides' table, recomputed: each $n \leq 100$ is coloured by the first test that rules it out, in the order prime, $\clubsuit$, $\diamondsuit p$, $\blacksquare p$. Exactly $30$, $56$, $60$ and $90$ survive. ($18$ is $\diamondsuit 3$, as corrected in lecture.)

> [!theorem] Proposition §54.1: Primes and Prime Powers
> 1. The trivial group is not simple.
> 2. If $|G| = p$ is prime, then $G \cong \mathbb{Z}/p\mathbb{Z}$ is simple.
> 3. If $|G| = p^k$ with $p$ prime and $k \geq 2$, then $G$ is not simple.
>
> *Source: lecture 10/23*

^prop-54-1

> [!proof]+ Proof
> *Idea:* for (3), the center is a nontrivial normal subgroup; it is proper unless $G$ is abelian, and abelian simple groups have prime order.
>
> **(1)** By Definition [[§43 Simple Groups#^def-43-1|§43.1]]: the trivial group has only one normal subgroup.
>
> **(2)** A group of prime order is cyclic, hence $\cong \mathbb{Z}/p\mathbb{Z}$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]), and it is simple by Theorem [[§43 Simple Groups#^thm-43-1|§43.1]].
>
> **(3)** The center $Z(G) = \{z \in G : zg = gz \text{ for all } g \in G\}$ (Definition [[§35 The Center#^def-35-2|§35.2]]) is nontrivial by Theorem [[§35 The Center#^thm-35-3|§35.3]], and it is normal in $G$: for $z \in Z(G)$ and $g \in G$, $gzg^{-1} = z$. If $Z(G) \neq G$, then $Z(G)$ is a proper nontrivial normal subgroup, and $G$ is not simple. If $Z(G) = G$, then $G$ is abelian, and an abelian simple group has prime order (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]); but $|G| = p^k$ with $k \geq 2$ is not prime. Either way $G$ is not simple.

^pf-54-1

*Uses:* [[§43 Simple Groups#^def-43-1|Def. §43.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]], [[§43 Simple Groups#^thm-43-1|§43.1]], [[§35 The Center#^def-35-2|Def. §35.2]], [[§35 The Center#^thm-35-3|§35.3]]

> [!remark] Remark: Notation for This Section
> Throughout, $G$ is finite, $p$ is a prime dividing $|G|$, and $|G| = p^k m$ with $p \nmid m$. Write $n_p$ for the number of Sylow $p$-subgroups of $G$. The conjugate $gPg^{-1}$ of a Sylow $p$-subgroup $P$ is again a Sylow $p$-subgroup, since conjugation by $g$ is an isomorphism (Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]); so $G$ acts on the set of Sylow $p$-subgroups by conjugation, $g \cdot P = gPg^{-1}$, as in the proof of Theorem [[§53 The Sylow Theorems#^thm-53-9|§53.9]].

^rem-54-2

> [!definition] Definition §54.1: Normalizer
> Let $H \leq G$. The **normalizer** of $H$ in $G$ is
>
> $$
> N_G(H) = N(H) := \{ g \in G : gHg^{-1} = H \},
> $$
>
> the stabilizer of $H$ under the action of $G$ on its subgroups by conjugation.
>
> *Source: lecture 10/23*

^def-54-1

> [!remark] Remark: Basic Properties of the Normalizer
> $N(H)$ is a subgroup of $G$, since stabilizers are subgroups (Proposition [[§26 Stabilizers and Fixed Points#^prop-26-1|§26.1]]); it contains $H$, since $hHh^{-1} = H$ for $h \in H$; and $H \trianglelefteq N(H)$, directly from the definition. $H$ is normal in $G$ (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]) if and only if $N(H) = G$.

^rem-54-3

> [!theorem] Proposition §54.2: $n_p$ and the Normalizer
> Let $P$ be a Sylow $p$-subgroup of $G$. Then $n_p = [G : N(P)]$, and
>
> $$
> m = [N(P) : P] \cdot n_p.
> $$
>
> In particular $n_p$ divides $m$ (Corollary [[§53 The Sylow Theorems#^cor-53-10|§53.10]]). Together with the Third Sylow Theorem (Theorem [[§53 The Sylow Theorems#^thm-53-9|§53.9]]), $n_p \mid m$ and $n_p \equiv 1 \pmod p$.
>
> *Source: lecture 10/23*

^prop-54-2

> [!proof]+ Proof
> *Idea:* orbit–stabilizer for the single conjugation orbit, whose stabilizer is $N(P) \supseteq P$.
>
> *(Board 10/23.)* Let $G$ act on the set of Sylow $p$-subgroups by conjugation. By the Second Sylow Theorem (Theorem [[§53 The Sylow Theorems#^thm-53-6|§53.6]]), any two Sylow $p$-subgroups are conjugate, so there is only one orbit, of size $n_p$. The stabilizer of $P$ is $\operatorname{Stab}(P) = \{g \in G : gPg^{-1} = P\} = N(P)$ (Definition [[§54 Simple Groups of Small Order#^def-54-1|§54.1]]). By Orbit–Stabilizer (Theorem [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]]), $n_p = [G : N(P)]$, and using Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) for $P \leq N(P)$,
>
> $$
> p^k m = |G| = |N(P)| \cdot n_p = |P| \cdot [N(P) : P] \cdot n_p = p^k \, [N(P) : P] \cdot n_p.
> $$
>
> Cancelling $p^k$ gives $m = [N(P) : P] \cdot n_p$.

^pf-54-2

*Uses:* [[§53 The Sylow Theorems#^thm-53-6|§53.6]], [[§54 Simple Groups of Small Order#^def-54-1|Def. §54.1]], [[§30 Orbit–Stabilizer#^thm-30-3|§30.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!proof]+ Alternative proof that $n_p \mid m$ (number theory)
> *(Board 10/23.)* From $n_p = [G : N(P)]$, $n_p$ divides $|G| = p^k m$. By the Third Sylow Theorem (Theorem [[§53 The Sylow Theorems#^thm-53-9|§53.9]]) $n_p \equiv 1 \pmod p$, so $p \nmid n_p$; hence no factor of $p$ occurs in $n_p$, and $n_p$ divides $m$.

^pf-54-2-2

*Uses:* [[§53 The Sylow Theorems#^thm-53-9|§53.9]]

![[m493-53-2.svg]]

*(Not from lecture; figure added.)* Left: the chain $\{e\} \leq P \leq N(P) \leq G$ with its indices; the index $m$ of $P$ in $G$ splits as $[N(P) : P] \cdot n_p$. Right: $G$ permutes the Sylow $p$-subgroups $P_1, \ldots, P_{n_p}$ transitively by conjugation (Theorem [[§53 The Sylow Theorems#^thm-53-6|§53.6]]); the stabilizer of $P_1$ is $N(P_1)$, so the orbit has $[G : N(P_1)]$ points.

> [!theorem] Corollary §54.3: A Unique Sylow Subgroup Rules Out Simplicity
> If $n_p = 1$, then the Sylow $p$-subgroup $P$ is normal in $G$. If moreover $|G|$ is not a power of $p$, then $\{e\} \neq P \neq G$, so $G$ is not simple.
>
> *Source: lecture 10/23*

^cor-54-3

> [!proof]+ Proof
> $P$ is normal by Corollary [[§53 The Sylow Theorems#^cor-53-7|§53.7]](2): $gPg^{-1}$ is a Sylow $p$-subgroup for every $g \in G$, and $P$ is the only one, so $gPg^{-1} = P$. Since $p$ divides $|G|$, $|P| = p^k > 1$; if $|G|$ is not a power of $p$, then $m > 1$, so $|P| = p^k < |G|$.

^pf-54-3

*Uses:* [[§53 The Sylow Theorems#^cor-53-7|§53.7]]

> [!remark] Remark: The Sylow Test
> So to show that no group of order $n$ is simple, it suffices to find a prime $p \mid n$ such that the only divisor $d$ of $m$ with $d \equiv 1 \pmod p$ is $d = 1$ (Proposition [[§54 Simple Groups of Small Order#^prop-54-2|§54.2]], Corollary [[§54 Simple Groups of Small Order#^cor-54-3|§54.3]]). This rules out a large part of the table.

^rem-54-4

> [!example] Example §54.1: Order $21$
> $21 = 3 \cdot 7$. The candidates are: $n_3 \mid 7$ and $n_3 \equiv 1 \pmod 3$, so $n_3 \in \{1, 7\}$; $n_7 \mid 3$ and $n_7 \equiv 1 \pmod 7$, so $n_7 = 1$ ($3 \not\equiv 1 \pmod 7$). Hence the Sylow $7$-subgroup is normal, and no group of order $21$ is simple. (Marked $\diamondsuit 7$ on the slides.) Both values of $n_3$ occur: $n_3 = 1$ for $\mathbb{Z}/21\mathbb{Z}$, and $n_3 = 7$ for $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$ (Example [[§56 Semidirect Products#^ex-56-2|§56.2]]).
>
> *Source: lecture 10/23*

^ex-54-1

> [!example] Example §54.2: Four Orders That Survive the Sylow Test
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

^ex-54-2

> [!theorem] Proposition §54.4: The Conjugation Homomorphism $G \to S_{n_p}$
> Suppose $n_p > 1$. Numbering the Sylow $p$-subgroups $1, \ldots, n_p$, the conjugation action gives a homomorphism
>
> $$
> \varphi: G \to S_{n_p}.
> $$
>
> Then $\operatorname{Ker}\varphi \neq G$. Consequently, if $G$ is simple, then $\varphi$ is injective and $|G|$ divides $n_p!$. Equivalently: if $|G| \nmid n_p!$, then $\operatorname{Ker}\varphi$ is a proper nontrivial normal subgroup and $G$ is not simple.
>
> *Source: lecture 10/23*

^prop-54-4

> [!proof]+ Proof
> *Idea:* a transitive action on $n_p > 1$ points is not trivial, so its kernel is a normal subgroup other than $G$.
>
> An action on a set with $n_p$ elements is a homomorphism to $S_{n_p}$ (Theorem [[§25 Actions#^thm-25-3|§25.3]]). By the Second Sylow Theorem (Theorem [[§53 The Sylow Theorems#^thm-53-6|§53.6]]) the action is transitive, and there are $n_p > 1$ points, so some $g$ moves some point: $\varphi$ is not trivial, i.e. $\operatorname{Ker}\varphi \neq G$. Kernels are normal (Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]), so if $G$ is simple then $\operatorname{Ker}\varphi = \{e\}$, and $\varphi$ is injective. Then $G \cong \varphi(G) \leq S_{n_p}$ (First Isomorphism Theorem, Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]), so $|G|$ divides $|S_{n_p}| = n_p!$ by Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

^pf-54-4

*Uses:* [[§25 Actions#^thm-25-3|§25.3]], [[§53 The Sylow Theorems#^thm-53-6|§53.6]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §54.3: Orders $12$ and $80$
> 1. $|G| = 12$. If $n_2 = 1$, the Sylow $2$-subgroup is normal. If $n_2 = 3$, we get $\varphi: G \to S_3$, and $12 > 6 = |S_3|$, so $\varphi$ is not injective: $\operatorname{Ker}\varphi$ is a proper nontrivial normal subgroup. Either way $G$ is not simple. (Marked $\blacksquare 2$.)
> 2. $|G| = 80$. If $n_2 = 1$ we are done. If $n_2 = 5$, we get $\varphi: G \to S_5$ with $|S_5| = 5! = 120$. Here $80 < 120$, but $80 \nmid 120$, so again $\varphi$ is not injective. (Marked $\blacksquare 2$.)
>
> This test does not kill $56$ or $60$: $56$ divides $7!$ and $8!$, and $60$ divides $5!$, $6!$, $10!$ and $15!$.
>
> *Source: lecture 10/23*

^ex-54-3

> [!theorem] Lemma §54.5: Homomorphisms That Leave $A_N$
> Let $\varphi: G \to S_N$ be a homomorphism with $\varphi(G) \not\subseteq A_N$, and suppose $|G| > 2$. Then $G$ is not simple: $\varphi^{-1}(A_N)$ is a normal subgroup of $G$ of index $2$.
>
> *Source: lecture and slides 10/23*

^lem-54-5

> [!proof]+ Proof
> *Idea:* the composite $\operatorname{sgn} \circ \varphi : G \to \{\pm 1\}$ is a homomorphism onto a group of order $2$; its kernel is normal, not all of $G$, and not trivial.
>
> *(Board 10/23; the lecture's version: normal subgroups come from kernels, so to find one, build a map.)* Let $\psi = \operatorname{sgn} \circ \varphi: G \to S_N \to \{\pm 1\}$, a homomorphism (Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]]). Then $\operatorname{Ker}\psi \trianglelefteq G$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). $\operatorname{Ker}\psi \neq G$, because $\operatorname{Ker}\psi = \varphi^{-1}(\operatorname{Ker}\operatorname{sgn}) = \varphi^{-1}(A_N)$ (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]) and $\varphi(G) \not\subseteq A_N$. And $\operatorname{Ker}\psi \neq \{e\}$, because $|G| > 2 = |\{\pm 1\}|$, so $\psi$ cannot be injective. Hence $\operatorname{Ker}\psi$ is a proper nontrivial normal subgroup. It has index $2$: $\psi$ is onto $\{\pm 1\}$ (its image is not $\{1\}$), so $G/\operatorname{Ker}\psi \cong \{\pm 1\}$ (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).

^pf-54-5

*Uses:* [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|§21.3]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|Def. §21.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

> [!proof]+ Second proof (indices)
> *(Not from class.)* Let $H = \varphi^{-1}(A_N)$. It is normal in $G$: for $h \in H$ and $g \in G$, $\varphi(ghg^{-1}) = \varphi(g)\varphi(h)\varphi(g)^{-1} \in A_N$, because $A_N \trianglelefteq S_N$ (it is the kernel of $\operatorname{sgn}$, Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). The rule $gH \mapsto \varphi(g)A_N$ is well defined and injective ($\varphi(g)A_N = \varphi(g')A_N \iff \varphi(g^{-1}g') \in A_N \iff g^{-1}g' \in H$), so $[G : H] \leq [S_N : A_N] = 2$. Hence $|H| \geq |G|/2 > 1$, so $H \neq \{e\}$; and $H \neq G$ because $\varphi(G) \not\subseteq A_N$.

^pf-54-5-2

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]

> [!theorem] Corollary §54.6: Simple Groups Land in $A_{n_p}$
> If $G$ is simple with $|G| > 2$, then every homomorphism $G \to S_N$ has image in $A_N$. In particular, if $n_p > 1$, then $G$ embeds in $A_{n_p}$, and $|G|$ divides $n_p!/2$.
>
> *Source: lecture and slides 10/23*

^cor-54-6

> [!proof]+ Proof
> The first statement is Lemma [[§54 Simple Groups of Small Order#^lem-54-5|§54.5]]. For the second, the map $\varphi: G \to S_{n_p}$ of Proposition [[§54 Simple Groups of Small Order#^prop-54-4|§54.4]] is injective with image in $A_{n_p}$, so $|G|$ divides $|A_{n_p}| = n_p!/2$ by Lagrange (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]).

^pf-54-6

*Uses:* [[§54 Simple Groups of Small Order#^lem-54-5|§54.5]], [[§54 Simple Groups of Small Order#^prop-54-4|§54.4]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!example] Example §54.4: Order $112$
> The first order where the lemma is needed for the Sylow action is beyond the table: $112 = 2^4 \cdot 7$. Here $n_2 \in \{1, 7\}$ and $n_7 \in \{1, 8\}$. If $G$ were simple, $n_2 = 7$ and $G$ would embed in $S_7$. Now $112$ divides $7! = 5040$ ($5040 = 45 \cdot 112$), so Proposition [[§54 Simple Groups of Small Order#^prop-54-4|§54.4]] alone does not help; but $112 \nmid 7!/2 = 2520$, so by Corollary [[§54 Simple Groups of Small Order#^cor-54-6|§54.6]] $G$ is not simple.
>
> *Source: slides 10/23*

^ex-54-4

> [!remark] Remark: Other Embeddings
> The homework uses another way of mapping a group into a symmetric group, besides the action on Sylow subgroups, together with the lemma, to rule out the orders $30$ and $90$, and yet another trick to rule out $56$. These are left to the homework: Propositions [[§54 Simple Groups of Small Order#^prop-54-7|§54.7]] and [[§54 Simple Groups of Small Order#^prop-54-8|§54.8]] (Problem Set 7).
>
> *Source: slides 10/23*

^rem-54-5

## The Orders $30$, $56$ and $90$

*Source: Problem Set 7 (submitted Thu Oct 29). The homework rules out the three orders that the tests above leave open besides $60$, with two other ways of producing a normal subgroup.*

> [!theorem] Proposition §54.7: Groups of Order $2 \bmod 4$ Are Not Simple
> Let $G$ be a finite group with $|G| \equiv 2 \pmod 4$ and $|G| > 2$. Then $G$ is not simple. In particular there are no simple groups of order $30$ or $90$.
>
> *Source: PS 7.2*

^prop-54-7

> [!proof]+ Proof
> *Idea:* an element $t$ of order $2$ acts on $G$ by left multiplication as a product of $|G|/2$ disjoint transpositions, an odd number, so the Cayley embedding $G \to S_{|G|}$ leaves $A_{|G|}$ (Lemma [[§54 Simple Groups of Small Order#^lem-54-5|§54.5]]).
>
> *(Problem Set 7, Problem 7.2, as submitted.)* Since $|G| \equiv 2 \bmod 4$, write $|G| = 4k + 2 = 2(2k+1)$, where $k \geq 1$ since $|G| > 2$.
>
> **(1) An element $t$ of order $2$.** By the first Sylow theorem, $G$ has a $2$-Sylow subgroup $P$, whose order $|P| = 2^n$ is the largest power of $2$ dividing $|G|$. Since $2 \mid |G|$, $n \geq 1$.
>
> **$|P| = 2$.** Suppose $n \geq 2$. Then $4 \mid 2^n$, and $2^n \mid |G|$ by Lagrange's theorem, so $4 \mid 4k + 2$. But $4k + 2 \equiv 2 \bmod 4$, a contradiction. Hence $n = 1$ and $|P| = 2$.
>
> Hence $P = \{e, t\}$ with $t \neq e$. By Lagrange's theorem, the order of $t$ divides $|P| = 2$, and since $t \neq e$, $t$ has order $2$.
>
> **(2) $\operatorname{sgn}\phi(t) = -1$,** where $\phi : G \to S_{4k+2}$ is the embedding given by left multiplication (as in Problem 3.1; Cayley's Theorem, Theorem [[§25 Actions#^thm-25-5|§25.5]]). Let $\sigma = \phi(t)$, the permutation of the $4k+2$ elements of $G$ given by $\sigma(x) = tx$.
>
> **No fixed points.** If $\sigma(x) = x$ for some $x \in G$, then $tx = x$, so $t = e$ after multiplying on the right by $x^{-1}$, contradicting $t \neq e$. Hence $\sigma(x) \neq x$ for all $x \in G$.
>
> **Cycle lengths.** Since $\phi$ is a homomorphism and $t^2 = e$,
>
> $$
> \sigma^2 = \phi(t)^2 = \phi(t^2) = \phi(e) = \operatorname{id}_G.
> $$
>
> Let $x \in G$. Following $x$ under $\sigma$ gives $x \mapsto \sigma(x) \mapsto \sigma^2(x) = x$, so the cycle of $\sigma$ containing $x$ is either $(x)$, if $\sigma(x) = x$, or the transposition $(x\ \ tx)$. Since $\sigma$ has no fixed points, every cycle of $\sigma$ is a transposition $(x\ \ tx)$.
>
> **Counting.** The disjoint cycles of $\sigma$ partition $G$, so the transpositions $(x\ \ tx)$ partition the $4k+2$ elements of $G$ into $2$-element sets $\{x, tx\}$. Hence $\sigma$ is a product of
>
> $$
> \frac{4k+2}{2} = 2k+1
> $$
>
> disjoint transpositions. Since $\operatorname{sgn}$ is a homomorphism and every transposition has sign $-1$,
>
> $$
> \operatorname{sgn}\phi(t) = \operatorname{sgn}\sigma = (-1)^{2k+1} = -1.
> $$
>
> **(3) $G$ is not simple.** The composite $\operatorname{sgn} \circ \phi \colon G \to \{\pm 1\}$ is a homomorphism, as a composite of homomorphisms, so $\ker(\operatorname{sgn} \circ \phi)$ is a normal subgroup of $G$.
>
> **Proper.** By (2), $\operatorname{sgn}(\phi(t)) = -1$, so $t \notin \ker(\operatorname{sgn} \circ \phi)$, and hence $\ker(\operatorname{sgn} \circ \phi) \neq G$.
>
> **Nontrivial.** If $\ker(\operatorname{sgn} \circ \phi) = \{e\}$, then $\operatorname{sgn} \circ \phi$ would be an injective map from $G$ into the two-element set $\{\pm 1\}$, which is impossible since $|G| = 4k + 2 > 2$. Hence $\ker(\operatorname{sgn} \circ \phi) \neq \{e\}$.
>
> Thus $\ker(\operatorname{sgn} \circ \phi)$ is a normal subgroup of $G$ other than $\{e\}$ and $G$, so $G$ is not simple.

^pf-54-7

*Uses:* [[§54 Simple Groups of Small Order#^lem-54-5|§54.5]], [[§25 Actions#^thm-25-5|§25.5]]

> [!remark] Remark: A Normal Subgroup of Index $2$
> *(Not from class.)* The proof gives more: $\operatorname{Ker}(\operatorname{sgn} \circ \phi)$ has index $2$ (Lemma [[§54 Simple Groups of Small Order#^lem-54-5|§54.5]]), so every group of order $2m$ with $m > 1$ odd has a normal subgroup of index $2$. The element $t$ also comes directly from Cauchy's theorem (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-6|§29.6]]). The cycle count of part (2) works for any $g \in G$: if $g$ has order $d$, the orbits of $x \mapsto gx$ are the right cosets $\langle g \rangle x$, each with $d$ elements, so $\phi(g)$ is a product of $|G|/d$ disjoint $d$-cycles and $\operatorname{sgn}\phi(g) = (-1)^{(d-1)|G|/d}$. For $d = 2$ and $|G|/2$ odd, this is $-1$.

^rem-54-6

> [!theorem] Proposition §54.8: There Is No Simple Group of Order $56$
> There is no simple group of order $56$.
>
> *Source: PS 7.3*

^prop-54-8

> [!proof]+ Proof
> *Idea:* a simple group of order $56$ would have eight Sylow $7$-subgroups, with $48$ elements of order $7$ between them, and seven Sylow $2$-subgroups, two of which already have at least $12$ elements; $48 + 12 > 56$.
>
> *(Problem Set 7, Problem 7.3, as submitted.)* Suppose, to the contrary, that $G$ is a simple group of order $56$. Let $P_1, P_2, \dots, P_7$ be the $2$-Sylows and $Q_1, Q_2, \dots, Q_8$ the $7$-Sylows (part (1)).
>
> **(1) $n_7 = 8$ and $n_2 = 7$.** We have $56 = 2^3 \cdot 7$.
>
> **Conjugates of Sylows.** For $g \in G$, the map $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$, is an injective homomorphism, so for every subgroup $K$ of $G$, $gKg^{-1} = c_g(K)$ is a subgroup of $G$ with $|gKg^{-1}| = |K|$. Hence if $P$ is a $p$-Sylow of $G$, so is $gPg^{-1}$ for every $g \in G$. If moreover $n_p = 1$, then $gPg^{-1} = P$ for all $g \in G$, so $P$ is normal in $G$.
>
> **$p = 7$.** Since $56 = 7 \cdot 8$ with $7 \nmid 8$, a $7$-Sylow of $G$ has order $7$, and by the Sylow theorems $n_7 \mid 8$ and $n_7 \equiv 1 \pmod 7$. The divisors of $8$ are $1, 2, 4, 8$, which are congruent to $1, 2, 4, 1$ modulo $7$, so $n_7 \in \{1, 8\}$. If $n_7 = 1$, the unique $7$-Sylow would be a normal subgroup of $G$ of order $7$, with $1 < 7 < 56$, contradicting the simplicity of $G$. Hence $n_7 = 8$.
>
> **$p = 2$.** Since $56 = 2^3 \cdot 7$ with $2 \nmid 7$, a $2$-Sylow of $G$ has order $8$, and by the Sylow theorems $n_2 \mid 7$ and $n_2 \equiv 1 \pmod 2$. The divisors of $7$ are $1$ and $7$, both odd, so $n_2 \in \{1, 7\}$. If $n_2 = 1$, the unique $2$-Sylow would be a normal subgroup of $G$ of order $8$, with $1 < 8 < 56$, contradicting the simplicity of $G$. Hence $n_2 = 7$.
>
> **(2) $|P_1 \cup P_2| \geq 12$ and $|Q_1 \cup \cdots \cup Q_8| = 49$.** **$|P_1 \cup P_2| \geq 12$.** The intersection $P_1 \cap P_2$ is a subgroup of $P_1$, so by Lagrange's theorem $|P_1 \cap P_2|$ divides $|P_1| = 8$, that is, $|P_1 \cap P_2| \in \{1, 2, 4, 8\}$. If $|P_1 \cap P_2| = 8$, then $P_1 \cap P_2 = P_1$, so $P_1 \subseteq P_2$, and since $|P_1| = |P_2| = 8$, $P_1 = P_2$, contradicting $P_1 \neq P_2$. Hence $|P_1 \cap P_2| \leq 4$, and
>
> $$
> |P_1 \cup P_2| = |P_1| + |P_2| - |P_1 \cap P_2| = 16 - |P_1 \cap P_2| \geq 16 - 4 = 12.
> $$
>
> **$|Q_1 \cup Q_2 \cup \cdots \cup Q_8| = 49$.** Let $i \neq j$. The intersection $Q_i \cap Q_j$ is a subgroup of $Q_i$, so by Lagrange's theorem $|Q_i \cap Q_j|$ divides $|Q_i| = 7$, that is, $|Q_i \cap Q_j| \in \{1, 7\}$. If $|Q_i \cap Q_j| = 7$, then $Q_i \subseteq Q_j$, and since $|Q_i| = |Q_j| = 7$, $Q_i = Q_j$, contradicting $i \neq j$. Hence $Q_i \cap Q_j = \{e\}$ for all $i \neq j$.
>
> So the sets $Q_1 \setminus \{e\}, \dots, Q_8 \setminus \{e\}$ are pairwise disjoint, each with $7 - 1 = 6$ elements, and
>
> $$
> Q_1 \cup Q_2 \cup \cdots \cup Q_8 = \{e\} \cup (Q_1 \setminus \{e\}) \cup \cdots \cup (Q_8 \setminus \{e\})
> $$
>
> is a disjoint union. Therefore
>
> $$
> |Q_1 \cup Q_2 \cup \cdots \cup Q_8| = 1 + 8 \cdot 6 = 49.
> $$
>
> **(3) The contradiction.** Let $Q = Q_1 \cup Q_2 \cup \cdots \cup Q_8$.
>
> **$P_i \cap Q_j = \{e\}$.** Let $i \in \{1, 2\}$, $j \in \{1, \dots, 8\}$, and $x \in P_i \cap Q_j$. Since $x \in P_i$, by Lagrange's theorem the order of $x$ divides $|P_i| = 8$, so it lies in $\{1, 2, 4, 8\}$. Since $x \in Q_j$, by Lagrange's theorem the order of $x$ divides $|Q_j| = 7$, so it lies in $\{1, 7\}$. Hence the order of $x$ is $1$, that is, $x = e$. So $P_i \cap Q_j = \{e\}$.
>
> **Intersection.** By distributivity,
>
> $$
> (P_1 \cup P_2) \cap Q = \bigcup_{i \in \{1, 2\}} \bigcup_{j = 1}^{8} (P_i \cap Q_j) = \{e\}.
> $$
>
> **Counting.** By inclusion–exclusion and (2),
>
> $$
> |P_1 \cup P_2 \cup Q| = |P_1 \cup P_2| + |Q| - |(P_1 \cup P_2) \cap Q| \geq 12 + 49 - 1 = 60.
> $$
>
> But $P_1 \cup P_2 \cup Q$ is a subset of $G$, so $|P_1 \cup P_2 \cup Q| \leq |G| = 56$, a contradiction. Hence there is no simple group of order $56$.

^pf-54-8

> [!remark] Remark: What the Count Gives
> *(Not from class.)* The count shows more. The eight Sylow $7$-subgroups contain exactly $48$ elements of order $7$, which leaves $56 - 48 = 8$ elements; a Sylow $2$-subgroup has $8$ elements, none of order $7$, so it consists of exactly these $8$, and there is only one. So $n_7 = 8$ forces $n_2 = 1$: every group of order $56$ has a normal Sylow $7$-subgroup or a normal Sylow $2$-subgroup (Corollary [[§53 The Sylow Theorems#^cor-53-7|§53.7]]). The general tool: if the Sylow $p$-subgroups of $G$ have order $p$, any two of them intersect trivially, and $G$ has exactly $n_p(p - 1)$ elements of order $p$. Speyer: “this kind of counting elements approach can also handle a number of other cases — for example, you might enjoy working it out for $30$.”

^rem-54-7

> [!theorem] Theorem §54.9: Simple Groups of Order at Most $100$
> If $G$ is a simple group with $|G| \leq 100$, then either $G \cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$, or $|G| = 60$.
>
> *Source: lecture 10/23*

^thm-54-9

> [!proof]+ Proof
> *Idea:* the tests of the lecture leave only $30$, $56$, $60$, $90$ besides the primes; the homework rules out $30$, $56$, $90$.
>
> The tests of this section (the remark *The Game* and its table) rule out every order $n \le 100$ except the primes and $30$, $56$, $60$, $90$; a group of prime order is $\mathbb{Z}/p\mathbb{Z}$ (Proposition [[§54 Simple Groups of Small Order#^prop-54-1|§54.1]](2)). Since $30 = 4 \cdot 7 + 2$ and $90 = 4 \cdot 22 + 2$, Proposition [[§54 Simple Groups of Small Order#^prop-54-7|§54.7]] (PS 7.2) rules out $30$ and $90$, and Proposition [[§54 Simple Groups of Small Order#^prop-54-8|§54.8]] (PS 7.3) rules out $56$.

^pf-54-9

*Uses:* [[§54 Simple Groups of Small Order#^prop-54-1|§54.1]], [[§54 Simple Groups of Small Order#^prop-54-7|§54.7]], [[§54 Simple Groups of Small Order#^prop-54-8|§54.8]]

## Simple Groups of Order $60$

*Source: Problem Set 7, Problem 7.1 (submitted Thu Oct 29).*

> [!theorem] Proposition §54.10: Proper Subgroups of $A_n$ Have Index at Least $n$
> Let $n \geq 5$ and let $H$ be a subgroup of $A_n$ other than $A_n$ itself. Then $[A_n : H] \geq n$.
>
> *Source: PS 7.1(1)*

^prop-54-10

> [!proof]+ Proof
> *Idea:* $A_n$ acts on the $k = [A_n : H]$ cosets of $H$; the action is injective because $A_n$ is simple, so $n!/2 \leq k!$, which fails for $k < n$.
>
> *(Problem Set 7, Problem 7.1(1), as submitted.)* Let $k = |A_n/H| = [A_n : H]$. For $x \in A_n$, recall that $xH = H$ if and only if $x \in H$.
>
> Let $A_n$ act on $A_n/H$ by left multiplication, $g \cdot xH = gxH$ for $g \in A_n$ and $xH \in A_n/H$. This is well defined: if $xH = yH$, then $x^{-1}y \in H$, so $(gx)^{-1}(gy) = x^{-1}y \in H$ and $gxH = gyH$. It is a group action, since $e \cdot xH = xH$ and $(g_1g_2) \cdot xH = g_1g_2xH = g_1 \cdot (g_2 \cdot xH)$. As in Problem 3.1, defining $\hat g \colon A_n/H \to A_n/H$ by $\hat g(xH) = gxH$, each $\hat g$ is a bijection and
>
> $$
> \psi \colon A_n \to S_{A_n/H}, \qquad \psi(g) = \hat g,
> $$
>
> is a group homomorphism.
>
> **The kernel of $\psi$ is trivial.** Since $\ker\psi$ is a normal subgroup of $A_n$ and $A_n$ is simple for $n \geq 5$, either $\ker\psi = \{e\}$ or $\ker\psi = A_n$. Since $H \neq A_n$, there exists $g \in A_n$ with $g \notin H$. Acting on $eH = H$,
>
> $$
> \hat g(H) = gH \neq H,
> $$
>
> because $g \notin H$. So $\hat g \neq \operatorname{id}_{A_n/H}$, that is, $g \notin \ker\psi$, and hence $\ker\psi \neq A_n$. Therefore $\ker\psi = \{e\}$.
>
> **Counting.** Since $\ker\psi = \{e\}$, $\psi$ is injective, so $A_n$ is isomorphic to its image $\psi(A_n)$, which is a subgroup of $S_{A_n/H}$. As $A_n/H$ has $k$ elements, $|S_{A_n/H}| = k!$. Hence
>
> $$
> \frac{n!}{2} = |A_n| = |\psi(A_n)| \leq |S_{A_n/H}| = k!.
> $$
>
> Suppose, for contradiction, that $k < n$. Then $k!$ divides $n!$, with
>
> $$
> a = \frac{n!}{k!} = n(n-1)\cdots(k+1),
> $$
>
> a product of $n - k \geq 1$ factors, one of which is $n$. So $a \geq n > 2$, since $n \geq 5$, and therefore
>
> $$
> k! = \frac{n!}{a} < \frac{n!}{2},
> $$
>
> contradicting $\frac{n!}{2} \leq k!$. Hence $k \geq n$, that is, $[A_n : H] \geq n$.

^pf-54-10

> [!remark] Remark: A Shortcut
> *(Not from class.)* By Corollary [[§54 Simple Groups of Small Order#^cor-54-6|§54.6]], the injective homomorphism $A_n \to S_k$ has image in $A_k$, so $n!/2$ divides $k!/2$ (Lagrange), i.e. $n!$ divides $k!$, which forces $k \geq n$; this replaces the counting step.

^rem-54-8

> [!theorem] Lemma §54.11: The Subgroup of Index $2$ in $S_m$
> Let $m \geq 3$ and let $U$ be a subgroup of $S_m$ with $|U| = \frac{m!}{2}$. Then $U = A_m$.
>
> *Source: PS 7.1(2), lemma*

^lem-54-11

> [!proof]+ Proof
> *Idea:* a subgroup of index $2$ missing a $3$-cycle $(i\,j\,k)$ would have the three distinct cosets $U$, $(i\,j\,k)U$, $(i\,k\,j)U$.
>
> *(Problem Set 7, Problem 7.1(2), lemma, as submitted.)* Suppose $U \neq A_m$. If every $3$-cycle lay in $U$, then, since $A_m$ is generated by $3$-cycles for $m \geq 3$, we would get $A_m \subseteq U$, and $|A_m| = \frac{m!}{2} = |U|$ would give $U = A_m$, contradicting $U \neq A_m$. So some $3$-cycle $(ijk)$ is not in $U$. Since $U$ is a subgroup, its inverse $(ikj) = (ijk)^{-1}$ is not in $U$ either. Consider the left cosets
>
> $$
> U, \qquad (ijk)U, \qquad (ikj)U.
> $$
>
> We have $(ijk)U \neq U$ and $(ikj)U \neq U$, since $(ijk), (ikj) \notin U$. If $(ijk)U = (ikj)U$, then
>
> $$
> (ikj)^{-1}(ijk) = (ijk)(ijk) = (ijk)^2 = (ijk)^{-1} = (ikj) \in U,
> $$
>
> a contradiction. So these are three distinct left cosets of $U$ in $S_m$. But by Lagrange's theorem, $[S_m : U] = \frac{m!}{m!/2} = 2$, so $U$ has exactly two left cosets in $S_m$, a contradiction. Hence $U = A_m$.

^pf-54-11

> [!theorem] Proposition §54.12: Subgroups of Index $n$ in $A_n$
> Let $n \geq 5$ and let $H$ be a subgroup of $A_n$ with $[A_n : H] = n$. Then $H \cong A_{n-1}$.
>
> *Source: PS 7.1(2)*

^prop-54-12

> [!proof]+ Proof
> *Idea:* $H$ fixes the coset $H$ in the action of $A_n$ on $A_n/H$, so it embeds in the stabilizer of a point, a copy of $S_{n-1}$, as a subgroup of index $2$; Lemma [[§54 Simple Groups of Small Order#^lem-54-11|§54.11]] identifies it.
>
> *(Problem Set 7, Problem 7.1(2), as submitted.)* Now suppose $[A_n : H] = n$. Since $n > 1$, $H \neq A_n$. Let $\psi \colon A_n \to S_{A_n/H}$, $\psi(g) = \hat g$, be as in (1); since $H \neq A_n$, (1) gives $\ker\psi = \{e\}$. By Lagrange's theorem,
>
> $$
> |H| = \frac{|A_n|}{[A_n : H]} = \frac{n!/2}{n} = \frac{(n-1)!}{2}.
> $$
>
> Since $\ker\psi = \{e\}$, the restriction of $\psi$ to $H$ is injective, so $H$ is isomorphic to its image $\psi(H)$.
>
> **The image lies in a stabilizer.** Let
>
> $$
> \operatorname{Stab}(H) = \{\sigma \in S_{A_n/H} : \sigma(H) = H\}.
> $$
>
> This is a subgroup of $S_{A_n/H}$: it contains $\operatorname{id}_{A_n/H}$, and if $\sigma, \tau$ fix $H$, then $\sigma\tau(H) = \sigma(H) = H$ and $\sigma^{-1}(H) = H$. For $h \in H$, $\hat h(H) = hH = H$ since $h \in H$, so $\psi(H) \leq \operatorname{Stab}(H)$.
>
> **The stabilizer is isomorphic to $S_{n-1}$.** Since $|A_n/H| = n$, write
>
> $$
> A_n/H = \{H, a_1H, \dots, a_{n-1}H\}, \qquad Y = \{a_1H, \dots, a_{n-1}H\}.
> $$
> For $\sigma \in \operatorname{Stab}(H)$, $\sigma$ is a bijection of $A_n/H$ with $\sigma(H) = H$, so by injectivity $\sigma(Y) \subseteq Y$, and $\sigma|_Y \colon Y \to Y$ is a bijection with inverse $\sigma^{-1}|_Y$. Define
>
> $$
> R \colon \operatorname{Stab}(H) \to S_Y, \qquad R(\sigma) = \sigma|_Y.
> $$
>
> $R$ is a homomorphism, since $(\sigma\tau)|_Y = \sigma|_Y \circ \tau|_Y$. It is bijective: its inverse sends $\tau \in S_Y$ to the permutation of $A_n/H$ that fixes $H$ and agrees with $\tau$ on $Y$. So $R$ is an isomorphism. The labeling $\beta \colon Y \to \{1, \dots, n-1\}$, $\beta(a_iH) = i$, gives an isomorphism $S_Y \to S_{n-1}$, $\tau \mapsto \beta \circ \tau \circ \beta^{-1}$. Composing, we obtain an isomorphism
>
> $$
> \Theta \colon \operatorname{Stab}(H) \to S_{n-1}.
> $$
>
> **Conclusion.** $\Theta(\psi(H))$ is a subgroup of $S_{n-1}$ of order $|\psi(H)| = |H| = \frac{(n-1)!}{2}$. Since $n - 1 \geq 4 \geq 3$, the lemma gives $\Theta(\psi(H)) = A_{n-1}$. Therefore
>
> $$
> H \cong \psi(H) \cong \Theta(\psi(H)) = A_{n-1}.
> $$

^pf-54-12

*Uses:* [[§54 Simple Groups of Small Order#^lem-54-11|§54.11]]

> [!theorem] Theorem §54.13: Simple Groups of Order $60$
> Every simple group of order $60$ is isomorphic to $A_5$.
>
> *Source: PS 7.1(3)*

^thm-54-13

> [!proof]+ Proof
> *Idea:* conjugation on the six Sylow $5$-subgroups embeds $G$ in $A_6$ with index $6$; Proposition [[§54 Simple Groups of Small Order#^prop-54-12|§54.12]] with $n = 6$ gives $G \cong A_5$.
>
> *(Problem Set 7, Problem 7.1(3), as submitted.)* Let $G$ be a simple group of order $60 = 2^2 \cdot 3 \cdot 5$.
>
> **Conjugation.** For $g \in G$, the map $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$, is a homomorphism, since $(gxg^{-1})(gyg^{-1}) = g(xy)g^{-1}$, and it is injective, since $gxg^{-1} = gyg^{-1}$ implies $x = y$. Hence for every subgroup $K$ of $G$, $gKg^{-1} = c_g(K)$ is a subgroup of $G$ with $|gKg^{-1}| = |K|$.
>
> **The number of $5$-Sylows.** Since $60 = 5 \cdot 12$ with $5 \nmid 12$, the $5$-Sylow subgroups of $G$ are its subgroups of order $5$, and by the Sylow theorems their number $n_5$ satisfies $n_5 \mid 12$ and $n_5 \equiv 1 \pmod 5$. The divisors of $12$ are $1, 2, 3, 4, 6, 12$, which are congruent to $1, 2, 3, 4, 1, 2$ modulo $5$, so $n_5 \in \{1, 6\}$.
>
> Suppose $n_5 = 1$, and let $P$ be the unique $5$-Sylow. For $g \in G$, $gPg^{-1}$ is a subgroup of order $5$, that is, a $5$-Sylow, so $gPg^{-1} = P$. Thus $P$ is normal in $G$, and $1 < |P| = 5 < 60 = |G|$, contradicting the simplicity of $G$. Therefore $n_5 = 6$. Let $X = \{P_1, P_2, \dots, P_6\}$ be the set of $5$-Sylows of $G$.
>
> **The conjugation action.** Let $G$ act on $X$ by $g \ast P_i = gP_ig^{-1}$.
> - *Well defined:* $gP_ig^{-1}$ is a subgroup of $G$ of order $5$, hence a $5$-Sylow, so $gP_ig^{-1} = P_j$ for some $P_j \in X$.
> - *Identity:* $e \ast P_i = eP_ie^{-1} = P_i$ for every $P_i \in X$.
> - *Compatibility:* for $g_1, g_2 \in G$,
>
> $$
> (g_1g_2) \ast P_i = (g_1g_2)P_i(g_1g_2)^{-1} = g_1g_2P_ig_2^{-1}g_1^{-1} = g_1\big(g_2P_ig_2^{-1}\big)g_1^{-1} = g_1 \ast (g_2 \ast P_i).
> $$
>
> So this is a group action, and as in Problem 3.1,
>
> $$
> \varphi \colon G \to S_X, \qquad \varphi(g)(P_i) = g \ast P_i,
> $$
>
> is a group homomorphism. The labeling $P_i \mapsto i$ identifies $S_X$ with $S_6$, and we regard $\varphi$ as a homomorphism $G \to S_6$.
>
> **$\varphi$ is injective.** Since $\ker\varphi$ is a normal subgroup of $G$ and $G$ is simple, either $\ker\varphi = \{e\}$ or $\ker\varphi = G$. Suppose $\ker\varphi = G$. Then every $g \in G$ fixes every $P_i$, that is, $gP_1g^{-1} = P_1$ for all $g \in G$, so $P_1$ is normal in $G$; since $1 < |P_1| = 5 < 60 = |G|$, this contradicts the simplicity of $G$. Hence $\ker\varphi = \{e\}$, $\varphi$ is injective, and $G$ is isomorphic to its image $\varphi(G)$, a subgroup of $S_6$.
>
> **$\varphi(G)$ lies in $A_6$.** Suppose there exists $g \in G$ with $\varphi(g) \notin A_6$, that is, $\operatorname{sgn}(\varphi(g)) = -1$. The composite $\operatorname{sgn} \circ \varphi \colon G \to \{\pm 1\}$ is a homomorphism, so its kernel is a normal subgroup of $G$. Since $\operatorname{sgn}(\varphi(g)) = -1$, $\ker(\operatorname{sgn} \circ \varphi) \neq G$. If $\ker(\operatorname{sgn} \circ \varphi) = \{e\}$, then $\operatorname{sgn} \circ \varphi$ would be an injective map from a group of order $60$ into the two-element set $\{\pm 1\}$, which is impossible; so $\ker(\operatorname{sgn} \circ \varphi) \neq \{e\}$. Thus $\ker(\operatorname{sgn} \circ \varphi)$ is a normal subgroup of $G$ other than $\{e\}$ and $G$, contradicting the simplicity of $G$. Therefore $\operatorname{sgn}(\varphi(g)) = 1$ for all $g \in G$, that is, $\varphi(G) \leq A_6$. Hence $G \cong \varphi(G)$, a subgroup of $A_6$.
>
> **Conclusion.** Let $H = \varphi(G)$, a subgroup of $A_6$ with $|H| = |G| = 60$. Since $|A_6| = \frac{6!}{2} = 360 \neq 60$, $H \neq A_6$, and $[A_6 : H] = 360/60 = 6$. Applying (2) with $n = 6 \geq 5$ gives $H \cong A_5$. Therefore $G \cong \varphi(G) = H \cong A_5$.

^pf-54-13

*Uses:* [[§54 Simple Groups of Small Order#^prop-54-12|§54.12]]

> [!theorem] Corollary §54.14: The Simple Groups of Order at Most $100$
> A simple group of order at most $100$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$ for a prime $p$, or to $A_5$.

^cor-54-14

> [!proof]+ Proof
> By Theorem [[§54 Simple Groups of Small Order#^thm-54-9|§54.9]], $G \cong \mathbb{Z}/p\mathbb{Z}$ or $|G| = 60$, and in the second case $G \cong A_5$ by Theorem [[§54 Simple Groups of Small Order#^thm-54-13|§54.13]]. Conversely, these groups are simple (Proposition [[§54 Simple Groups of Small Order#^prop-54-1|§54.1]](2) and Theorem [[§43 Simple Groups#^thm-43-9|§43.9]]).

^pf-54-14

*Uses:* [[§54 Simple Groups of Small Order#^thm-54-9|§54.9]], [[§54 Simple Groups of Small Order#^thm-54-13|§54.13]], [[§54 Simple Groups of Small Order#^prop-54-1|§54.1]], [[§43 Simple Groups#^thm-43-9|§43.9]]

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

^rem-54-9

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

^rem-54-10
