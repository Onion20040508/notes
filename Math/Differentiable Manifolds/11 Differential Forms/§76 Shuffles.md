---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 76
tags: [differentiable-manifolds, math591]
---
← [[§75 Multilinear Algebra]] · ↑ [[· 11 Differential Forms]] · [[§77 The Wedge Product]] →

*Stage: forms — The permutations that interleave two ordered piles: one for each choice of the places taken by the first pile, and one in each coset of $S_k \times S_l$.*

*(Lectures 29 and 30.)* The wedge in $dx^i \wedge dx^j$ has been written many times (Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]), but as an operation it has not been defined. Its definition, in the next section ([[§77 The Wedge Product|§77]]), is a signed sum over a particular set of permutations, the shuffles. This section is about them: what they are, how many there are, and how every permutation factors through exactly one of them. Throughout, $k, l \ge 0$.

> [!definition] Definition §76.1: Shuffles
> For $k, l \ge 0$, a **$(k, l)$-shuffle** is a permutation $\sigma \in S_{k+l}$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|§11.3]]) with
>
> $$
> \sigma(1) < \sigma(2) < \cdots < \sigma(k) \qquad \text{and} \qquad \sigma(k+1) < \sigma(k+2) < \cdots < \sigma(k+l) .
> $$
>
> $\mathrm{Sh}(k, l)$ denotes the set of $(k, l)$-shuffles.

^def-76-1

The name comes from shuffling a deck of cards. Put $k$ cards on the left and $l$ cards on the right and interleave the two piles: the cards mix, but the internal order of each pile does not change. The card in place $i$ before the shuffle lands in place $\sigma(i)$ of the deck; the first pile is the cards $1, \ldots, k$ and the second the cards $k + 1, \ldots, k + l$. A shuffle is determined by the set $\{\sigma(1), \ldots, \sigma(k)\}$ of places taken by the first pile (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](2)).

![[m591-76-1.svg]]

*(Figure added after Lecture 29; Lecture 30 drew this same shuffle on the board.)* One $(2, 3)$-shuffle, $\sigma = (2, 4, 1, 3, 5)$ in one-line notation ($\sigma(1) = 2$, $\sigma(2) = 4$, $\sigma(3) = 1$, $\sigma(4) = 3$, $\sigma(5) = 5$): the cards $1, 2$ of the first pile land in places $2, 4$, the cards $3, 4, 5$ of the second pile in places $1, 3, 5$, each pile keeping its order. It has three inversions (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]), the pairs $(1, 3)$, $(2, 3)$ and $(2, 4)$, so $\operatorname{sgn}(\sigma) = -1$. In the picture the inversions are the crossings: two arrows cross exactly when the card that starts further left lands further right, and for a shuffle only a red arrow and a blue arrow can cross.

*(Lecture 30.)* A shuffle is built in two steps, here for $k = 2$ and $l = 3$. First choose $\sigma(1) < \sigma(2)$: any two of the five places, for instance $2$ and $4$ (the choice $\sigma(1) = 5$ is impossible, because it leaves no place for $\sigma(2)$). Then $\sigma(3) < \sigma(4) < \sigma(5)$ have to be the three remaining places in increasing order, and there is no choice left. In the picture, the shuffle condition says that two arrows of the same colour do not cross. Choosing a shuffle is therefore choosing the $k$ places of the first pile, which gives the count $\binom{k+l}{k}$ of Lemma [[§76 Shuffles#^lem-76-1|§76.1]](2).

![[m591-76-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* All ten $(2, 3)$-shuffles, one after another, as riffles of two piles. The red cards are the two entries of $\alpha$ and the blue cards the three entries of $\beta$; the places of the deck hold the vectors $v^1, \ldots, v^5$, and a card landing on $v^p$ means that this entry receives $v^p$. Each pile keeps its order, so strands of one colour never cross; every crossing of a red strand with a blue one is an inversion of $\sigma$, and the sign of the shuffle is $+1$ for an even number of crossings and $-1$ for an odd number. Each riffle is one term of $(\alpha \wedge \beta)(v^1, \ldots, v^5)$ in Definition [[§77 The Wedge Product#^def-77-1|§77.1]]; the sixth one is the shuffle of the figure above.

> [!theorem] Lemma §76.1: Shuffles and the Subgroup $S_k \times S_l$
> Let $S_k \times S_l \subseteq S_{k+l}$ denote the set of permutations $\rho$ with $\rho(\{1, \ldots, k\}) = \{1, \ldots, k\}$. Such a $\rho$ permutes $\{1, \ldots, k\}$ by some $\tau \in S_k$ and $\{k+1, \ldots, k+l\}$ by $\rho(k + j) = k + \tau'(j)$ for some $\tau' \in S_l$.
>
> 1. $S_k \times S_l$ is a subgroup of $S_{k+l}$ with $k!\, l!$ elements, and $\operatorname{sgn}(\rho) = \operatorname{sgn}(\tau)\, \operatorname{sgn}(\tau')$.
> 2. A $(k, l)$-shuffle $\sigma$ is determined by the set $\sigma(\{1, \ldots, k\})$, and every $k$-element subset of $\{1, \ldots, k+l\}$ is $\sigma(\{1, \ldots, k\})$ for a shuffle $\sigma$. Hence $|\mathrm{Sh}(k, l)| = \binom{k+l}{k}$.
> 3. Every $\pi \in S_{k+l}$ factors in exactly one way as
>
> $$
> \pi = \sigma \circ \rho, \qquad \sigma \in \mathrm{Sh}(k, l), \quad \rho \in S_k \times S_l .
> $$

^lem-76-1

> [!proof]+ Proof
> *(Lecture 30 gave (2) with the picture above, and stated (3) as a claim, in the form $\sigma = s \circ (\lambda \oplus \tau)$ of the remark [[§76 Shuffles#^rem-76-1|Notation of Lecture 30]] below, with Example [[§76 Shuffles#^ex-76-1|§76.1]] in place of a proof. The proofs are filled in.)* Write $n = k + l$, $I = \{1, \ldots, k\}$ and $J = \{k+1, \ldots, n\}$.
>
> (1) If $\rho(I) = I$ then also $\rho(J) = J$, because $\rho$ is a bijection of $I \cup J$. If $\rho$ and $\rho'$ map $I$ onto $I$, so do $\rho \circ \rho'$ and $\rho^{-1}$, and so does the identity: $S_k \times S_l$ is a subgroup. The element $\rho$ is determined by the pair $(\tau, \tau')$, and every pair occurs, so there are $k!\, l!$ elements. For the sign, count inversions (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]). A pair $i < j$ with $i \in I$ and $j \in J$ is not an inversion of $\rho$, since $\rho(i) \le k < \rho(j)$. The inversions with $i, j \in I$ are the inversions of $\tau$, and those with $i, j \in J$ correspond to the inversions of $\tau'$. So the number of inversions of $\rho$ is the sum of those of $\tau$ and $\tau'$, and $\operatorname{sgn}(\rho) = \operatorname{sgn}(\tau)\operatorname{sgn}(\tau')$.
>
> (2) Let $\sigma$ be a shuffle and $P = \sigma(I)$. Since $\sigma(1) < \cdots < \sigma(k)$, these values are the elements of $P$ in increasing order; since $\sigma(k+1) < \cdots < \sigma(n)$, those values are the elements of the complement of $P$ in increasing order. So $P$ determines $\sigma$. Conversely, for any $k$-element subset $P = \{p_1 < \cdots < p_k\}$ of $\{1, \ldots, n\}$, with complement $\{q_1 < \cdots < q_l\}$, the permutation $\sigma(i) = p_i$ for $i \le k$, $\sigma(k + j) = q_j$ for $j \le l$, is a shuffle with $\sigma(I) = P$. So $\sigma \mapsto \sigma(I)$ is a bijection from $\mathrm{Sh}(k, l)$ to the set of $k$-element subsets of $\{1, \ldots, n\}$, which has $\binom{n}{k}$ elements.
>
> (3) *Existence.* Given $\pi$, let $\sigma$ be the shuffle with $\sigma(I) = \pi(I)$, from (2), and put $\rho = \sigma^{-1} \circ \pi$. Then $\rho(I) = \sigma^{-1}(\pi(I)) = \sigma^{-1}(\sigma(I)) = I$, so $\rho \in S_k \times S_l$, and $\pi = \sigma \circ \rho$. *Uniqueness.* If $\pi = \sigma \circ \rho$ with $\sigma$ a shuffle and $\rho(I) = I$, then $\sigma(I) = \sigma(\rho(I)) = \pi(I)$, which determines $\sigma$ by (2), and then $\rho = \sigma^{-1} \circ \pi$.

^pf-76-1

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]]

> [!remark]- Connections
> - Left cosets and their count in MATH 493: [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2]] and Lagrange's theorem, [[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]: the index of $S_k \times S_l$ in $S_{k+l}$ is the number of shuffles.

By (3) the shuffles are a set of representatives for the left cosets $\sigma \circ (S_k \times S_l)$ of the subgroup $S_k \times S_l$, one in each coset. The count agrees: $(k+l)! = \binom{k+l}{k} \cdot k!\, l!$.

> [!remark] Remark: Notation of Lecture 30
> Lecture 30 returned to shuffles and the wedge product with letters different from the ones used here and in the next two sections. The dictionary between the board and these notes, in addition to the remark [[§75 Multilinear Algebra#^rem-75-1|Notation in This Section]] in [[§75 Multilinear Algebra|§75]]:
> - *Shuffles and permutations.* The board writes $s$ for a shuffle, $\sigma$ for a general permutation in $S_{k+l}$, and $\lambda \in S_k$, $\tau \in S_l$ for permutations of the two blocks. These notes write $\sigma$ for a shuffle, $\pi$ for a general permutation, and $\tau \in S_k$, $\tau' \in S_l$ (Lemma [[§76 Shuffles#^lem-76-1|§76.1]]).
> - *The direct sum.* For $\lambda \in S_k$ and $\tau \in S_l$ the board defines $\lambda \oplus \tau \in S_{k+l}$ by $(\lambda \oplus \tau)(j) = \lambda(j)$ for $1 \le j \le k$ and $(\lambda \oplus \tau)(j) = \tau(j - k) + k$ for $k + 1 \le j \le k + l$. It is the element $\rho$ of $S_k \times S_l$ that acts by $\lambda$ on the first block and by $\tau$ on the second, in the sense of Lemma [[§76 Shuffles#^lem-76-1|§76.1]]; so the board's factorization $\sigma = s \circ (\lambda \oplus \tau)$ is $\pi = \sigma \circ \rho$ here.
> - *One-line notation.* The board lists the images in order in square brackets, $[\sigma(1), \sigma(2), \ldots]$; this is not cycle notation. These notes use round brackets, with a bar after the first $k$ entries when the two blocks matter.
> - *Signs and sets.* $(-1)^s$ is $\operatorname{sgn}(s)$; the board writes both $\mathrm{Sh}(k, l)$ and $S(k, l)$ for the set of shuffles, and $\Lambda^k$ for $\Lambda^k V^{\ast}$.
> - *Multilinear maps.* The board's $\psi$ is the multilinear map $T$ of Definition [[§77 The Wedge Product#^def-77-3|§77.3]], its $(V^{\ast})^{\otimes n}$ is the space of all multilinear maps $V^n \to \mathbb{R}$, its *antisymmetrizer* $A$ is the skew-symmetrizer $\mathcal{A}$, and its vectors carry lower labels, $v_1, v_2, \ldots$

^rem-76-1

> [!example] Example §76.1: Factoring a Permutation
> *(Lecture 30, as an example of Lemma [[§76 Shuffles#^lem-76-1|§76.1]](3); in the letters of these notes.)* Take $k = 2$, $l = 3$ and
>
> $$
> \pi = (4, 2 \mid 1, 5, 3), \qquad \text{that is,} \quad \pi(1) = 4,\ \pi(2) = 2,\ \pi(3) = 1,\ \pi(4) = 5,\ \pi(5) = 3 ,
> $$
>
> which is not a shuffle, since $\pi(1) > \pi(2)$.
>
> *The shuffle.* By the proof of Lemma [[§76 Shuffles#^lem-76-1|§76.1]](3), $\sigma$ is the shuffle with $\sigma(\{1, 2\}) = \pi(\{1, 2\}) = \{2, 4\}$: put each block of values of $\pi$ in increasing order,
>
> $$
> \sigma = (2, 4 \mid 1, 3, 5) .
> $$
>
> *The block permutation.* $\rho = \sigma^{-1} \circ \pi$ is found entry by entry from $\pi(j) = \sigma(\rho(j))$: $\pi(1) = 4 = \sigma(2)$ gives $\rho(1) = 2$; $\pi(2) = 2 = \sigma(1)$ gives $\rho(2) = 1$; $\pi(3) = 1 = \sigma(3)$ gives $\rho(3) = 3$; $\pi(4) = 5 = \sigma(5)$ gives $\rho(4) = 5$; and $\pi(5) = 3 = \sigma(4)$ gives $\rho(5) = 4$. So
>
> $$
> \rho = (2, 1 \mid 3, 5, 4) ,
> $$
>
> which permutes $\{1, 2\}$ by $\tau = (2, 1) \in S_2$ and $\{3, 4, 5\}$ by $\rho(2 + j) = 2 + \tau'(j)$ with $\tau' = (1, 3, 2) \in S_3$. That $\rho$ preserves the two blocks is forced: $\sigma$ and $\pi$ send the first block to the same set $\{2, 4\}$.
>
> *The signs.* $\sigma$ is the shuffle of the figure after Definition [[§76 Shuffles#^def-76-1|§76.1]], with three inversions, so $\operatorname{sgn}(\sigma) = -1$; and $\operatorname{sgn}(\rho) = \operatorname{sgn}(\tau)\,\operatorname{sgn}(\tau') = (-1)(-1) = 1$ (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](1)). Hence $\operatorname{sgn}(\pi) = -1$, in agreement with the five inversions of $\pi$: the pairs of positions $(1, 2)$, $(1, 3)$, $(1, 5)$, $(2, 3)$ and $(4, 5)$.

^ex-76-1

![[m591-76-4.svg]]

*(Not from lecture; figure added.)* Example [[§76 Shuffles#^ex-76-1|§76.1]] as two layers of arrows: first $\rho$, which stays on its side of the dashed line, then the shuffle $\sigma$. Following the arrows from the top row to the bottom row gives $\pi$.

> [!example] Example §76.2: Shuffles Do Not Form a Subgroup
> *(Lecture 29: a student asked whether $\mathrm{Sh}(k, l)$ is a subgroup of $S_{k+l}$ isomorphic to $S_k \times S_l$. It is not; the example is filled in.)* Take $k = 1$ and $l = 2$. The only condition on a $(1, 2)$-shuffle is $\sigma(2) < \sigma(3)$, and in one-line notation $(\sigma(1), \sigma(2), \sigma(3))$,
>
> $$
> \mathrm{Sh}(1, 2) = \{ (1, 2, 3),\ (2, 1, 3),\ (3, 1, 2) \} ,
> $$
>
> three elements, in agreement with $\binom{3}{1} = 3$. Let $\sigma = (2, 1, 3)$ and $\sigma' = (3, 1, 2)$. Then
>
> $$
> (\sigma' \circ \sigma)(1) = \sigma'(2) = 1, \qquad (\sigma' \circ \sigma)(2) = \sigma'(1) = 3, \qquad (\sigma' \circ \sigma)(3) = \sigma'(3) = 2 ,
> $$
>
> so $\sigma' \circ \sigma = (1, 3, 2)$, which is not a shuffle: its values at $2$ and $3$ are $3 > 2$. So $\mathrm{Sh}(1, 2)$ is not closed under composition. The subgroup in the picture is $S_1 \times S_2 = \{(1, 2, 3), (1, 3, 2)\}$, with two elements, and the three shuffles represent its three left cosets (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](3)).

^ex-76-2
