---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 76
tags: [differentiable-manifolds, math591]
---
← [[§75 Multilinear Algebra]] · ↑ [[· 11 Differential Forms]]

*Stage: forms — Multiplying a $k$-form and an $l$-form into a $(k + l)$-form, by signed shuffles; bilinear, associative, graded anticommutative.*

*(Lecture 29.)* The wedge in $dx^i \wedge dx^j$ has been written many times (Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]), but as an operation it has not been defined. This section defines it: a product that takes a $k$-form $\alpha$ and an $l$-form $\beta$ on $V$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]) to a $(k + l)$-form $\alpha \wedge \beta$. The forms of all degrees with this product make up the *Grassmann algebra* of $V$ (Lee: the exterior algebra). It was developed in the 19th century, and brought into its present form, for differential forms, by \'Elie Cartan in the first half of the 20th century. Throughout, $V$ is an $m$-dimensional real vector space and $k, l \ge 0$.

> [!definition] Definition §76.1: Shuffles
> For $k, l \ge 0$, a **$(k, l)$-shuffle** is a permutation $\sigma \in S_{k+l}$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|§11.3]]) with
>
> $$
> \sigma(1) < \sigma(2) < \cdots < \sigma(k) \qquad \text{and} \qquad \sigma(k+1) < \sigma(k+2) < \cdots < \sigma(k+l) .
> $$
>
> $\mathrm{Sh}(k, l)$ denotes the set of $(k, l)$-shuffles.

^def-76-1

The name comes from shuffling a deck of cards. Put $k$ cards on the left and $l$ cards on the right and interleave the two piles: the cards mix, but the internal order of each pile does not change. The card in place $i$ before the shuffle lands in place $\sigma(i)$ of the deck; the first pile is the cards $1, \ldots, k$ and the second the cards $k + 1, \ldots, k + l$. A shuffle is determined by the set $\{\sigma(1), \ldots, \sigma(k)\}$ of places taken by the first pile (Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](2)).

![[m591-76-1.svg]]

*(Not from lecture; figure added.)* One $(2, 3)$-shuffle, $\sigma = (2, 4, 1, 3, 5)$ in one-line notation ($\sigma(1) = 2$, $\sigma(2) = 4$, $\sigma(3) = 1$, $\sigma(4) = 3$, $\sigma(5) = 5$): the cards $1, 2$ of the first pile land in places $2, 4$, the cards $3, 4, 5$ of the second pile in places $1, 3, 5$, each pile keeping its order. It has three inversions (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]), the pairs $(1, 3)$, $(2, 3)$ and $(2, 4)$, so $\operatorname{sgn}(\sigma) = -1$. In the picture the inversions are the crossings: two arrows cross exactly when the card that starts further left lands further right, and for a shuffle only a red arrow and a blue arrow can cross.

![[m591-76-a1.gif|620]]

*(Not from lecture; animation added, vault only.)* All ten $(2, 3)$-shuffles, one after another, as riffles of two piles. The red cards are the two entries of $\alpha$ and the blue cards the three entries of $\beta$; the places of the deck hold the vectors $v^1, \ldots, v^5$, and a card landing on $v^p$ means that this entry receives $v^p$. Each pile keeps its order, so strands of one colour never cross; every crossing of a red strand with a blue one is an inversion of $\sigma$, and the sign of the shuffle is $+1$ for an even number of crossings and $-1$ for an odd number. Each riffle is one term of $(\alpha \wedge \beta)(v^1, \ldots, v^5)$ in Definition [[§76 The Wedge Product#^def-76-2|§76.2]]; the sixth one is the shuffle of the figure above.

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

> [!remark]- Connections
> - Left cosets and their count in MATH 493: [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2]] and Lagrange's theorem, [[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]: the index of $S_k \times S_l$ in $S_{k+l}$ is the number of shuffles.

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Write $n = k + l$, $I = \{1, \ldots, k\}$ and $J = \{k+1, \ldots, n\}$.
>
> (1) If $\rho(I) = I$ then also $\rho(J) = J$, because $\rho$ is a bijection of $I \cup J$. If $\rho$ and $\rho'$ map $I$ onto $I$, so do $\rho \circ \rho'$ and $\rho^{-1}$, and so does the identity: $S_k \times S_l$ is a subgroup. The element $\rho$ is determined by the pair $(\tau, \tau')$, and every pair occurs, so there are $k!\, l!$ elements. For the sign, count inversions (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]). A pair $i < j$ with $i \in I$ and $j \in J$ is not an inversion of $\rho$, since $\rho(i) \le k < \rho(j)$. The inversions with $i, j \in I$ are the inversions of $\tau$, and those with $i, j \in J$ correspond to the inversions of $\tau'$. So the number of inversions of $\rho$ is the sum of those of $\tau$ and $\tau'$, and $\operatorname{sgn}(\rho) = \operatorname{sgn}(\tau)\operatorname{sgn}(\tau')$.
>
> (2) Let $\sigma$ be a shuffle and $P = \sigma(I)$. Since $\sigma(1) < \cdots < \sigma(k)$, these values are the elements of $P$ in increasing order; since $\sigma(k+1) < \cdots < \sigma(n)$, those values are the elements of the complement of $P$ in increasing order. So $P$ determines $\sigma$. Conversely, for any $k$-element subset $P = \{p_1 < \cdots < p_k\}$ of $\{1, \ldots, n\}$, with complement $\{q_1 < \cdots < q_l\}$, the permutation $\sigma(i) = p_i$ for $i \le k$, $\sigma(k + j) = q_j$ for $j \le l$, is a shuffle with $\sigma(I) = P$. So $\sigma \mapsto \sigma(I)$ is a bijection from $\mathrm{Sh}(k, l)$ to the set of $k$-element subsets of $\{1, \ldots, n\}$, which has $\binom{n}{k}$ elements.
>
> (3) *Existence.* Given $\pi$, let $\sigma$ be the shuffle with $\sigma(I) = \pi(I)$, from (2), and put $\rho = \sigma^{-1} \circ \pi$. Then $\rho(I) = \sigma^{-1}(\pi(I)) = \sigma^{-1}(\sigma(I)) = I$, so $\rho \in S_k \times S_l$, and $\pi = \sigma \circ \rho$. *Uniqueness.* If $\pi = \sigma \circ \rho$ with $\sigma$ a shuffle and $\rho(I) = I$, then $\sigma(I) = \sigma(\rho(I)) = \pi(I)$, which determines $\sigma$ by (2), and then $\rho = \sigma^{-1} \circ \pi$.

^pf-76-1

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]]

By (3) the shuffles are a set of representatives for the left cosets $\sigma \circ (S_k \times S_l)$ of the subgroup $S_k \times S_l$, one in each coset. The count agrees: $(k+l)! = \binom{k+l}{k} \cdot k!\, l!$.

> [!example] Example §76.1: Shuffles Do Not Form a Subgroup
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
> so $\sigma' \circ \sigma = (1, 3, 2)$, which is not a shuffle: its values at $2$ and $3$ are $3 > 2$. So $\mathrm{Sh}(1, 2)$ is not closed under composition. The subgroup in the picture is $S_1 \times S_2 = \{(1, 2, 3), (1, 3, 2)\}$, with two elements, and the three shuffles represent its three left cosets (Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](3)).

^ex-76-1

> [!definition] Definition §76.2: Wedge Product
> Given $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]), their **wedge product** is the function $\alpha \wedge \beta : V^{k+l} \to \mathbb{R}$,
>
> $$
> (\alpha \wedge \beta)(v^1, \ldots, v^{k+l}) = \sum_{\sigma \in \mathrm{Sh}(k, l)} \operatorname{sgn}(\sigma)\, \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big)\, \beta\big(v^{\sigma(k+1)}, \ldots, v^{\sigma(k+l)}\big) ,
> $$
>
> the sum over all $(k, l)$-shuffles (Definition [[§76 The Wedge Product#^def-76-1|§76.1]]). It is a linear $(k + l)$-form, $\alpha \wedge \beta \in \Lambda^{k+l} V^{\ast}$ (Proposition [[§76 The Wedge Product#^prop-76-3|§76.3]](3)).
>
> *Lee: Ch. 14, The Wedge Product*

^def-76-2

> [!remark]- Connections
> - MATH 452 introduces the wedge product of forms on $\mathbb{R}^n$ by its rules (anticommutativity of the $dx_i$, bilinearity, associativity), [[§37 The Algebra of Differential Forms#^def-37-1|452 Def. §37.1]]; here it is defined by a formula and the rules become Proposition [[§76 The Wedge Product#^prop-76-4|§76.4]].

Degrees add under multiplication, as a degree should. Each term of the sum hands $k$ of the $k + l$ vectors to $\alpha$ and the remaining $l$ to $\beta$, both in increasing order of their labels; by Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](2) there is one term for each way of choosing which $k$ vectors go to $\alpha$, and its sign is the sign of the shuffle. For $k = 0$, $\alpha$ is a number $c$, the only $(0, l)$-shuffle is the identity, and $c \wedge \beta = c\, \beta$. In practice the formula is used directly only in low degrees.

**Transcription note (Lecture 29).** The board wrote $(-1)^\sigma$ for $\operatorname{sgn}(\sigma)$, lower labels $v_{\sigma(1)}, \ldots$ for the vectors, and $r_{\sigma(1)}, \ldots, r_{\sigma(k)}$ in the entries of $\alpha$, which are $v^{\sigma(1)}, \ldots, v^{\sigma(k)}$.

One can also sum over all permutations of $\{1, \ldots, k+l\}$ instead of the shuffles, but then there are many repetitions: in each term the entries of $\alpha$, and those of $\beta$, can be put into increasing order at the price of a sign. This, and the algebraic meaning of the formula, are made precise next. The lecture presented the algebraic description for conceptual understanding only; it is not used in computations.

> [!definition] Definition §76.3: Tensor Product of Multilinear Maps
> Let $S : V^k \to \mathbb{R}$ and $T : V^l \to \mathbb{R}$ be multilinear. Their **tensor product** is the map $S \otimes T : V^{k+l} \to \mathbb{R}$,
>
> $$
> (S \otimes T)(v^1, \ldots, v^{k+l}) = S(v^1, \ldots, v^k)\, T(v^{k+1}, \ldots, v^{k+l}) .
> $$
>
> It is multilinear.
>
> *Lee: Ch. 12, Multilinear Algebra*

^def-76-3

$S \otimes T$ is linear in each of the first $k$ entries because $S$ is, and in each of the last $l$ entries because $T$ is. For forms $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$ the tensor product $\alpha \otimes \beta$ is multilinear but in general not alternating: for $k = l = 1$, $(\alpha \otimes \beta)(v, v) = \alpha(v)\beta(v)$, which is not $0$ when $\alpha(v) \neq 0 \neq \beta(v)$ (compare Lemma [[§75 Multilinear Algebra#^lem-75-2|§75.2]](1)). The board writes $V^{\ast} \otimes \cdots \otimes V^{\ast}$ ($n$ factors) for the vector space of all multilinear maps $V^n \to \mathbb{R}$.

> [!definition] Definition §76.4: The Skew-Symmetrizer
> Let $T : V^n \to \mathbb{R}$ be multilinear. For $\pi \in S_n$ let $T^\pi$ be $T$ with its entries rearranged by $\pi$,
>
> $$
> T^\pi(v^1, \ldots, v^n) = T\big(v^{\pi(1)}, \ldots, v^{\pi(n)}\big) .
> $$
>
> The **skew-symmetrizer** is the map $\mathcal{A}$ that sends $T$ to
>
> $$
> \mathcal{A}(T) = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, T^\pi .
> $$
>
> *Lee: Ch. 14, The Algebra of Alternating Tensors*

^def-76-4

*(Lecture 29 named the map and described it as the natural projection onto the completely antisymmetric maps, without writing the formula; the formula is filled in. Lee calls it alternation and writes $\operatorname{Alt}$.)* Each $T^\pi$ is multilinear, so $\mathcal{A}(T)$ is multilinear, and $\mathcal{A}$ is a linear map from the space of multilinear maps $V^n \to \mathbb{R}$ to itself.

> [!theorem] Lemma §76.2: The Skew-Symmetrizer Projects onto the Forms
> Let $T : V^n \to \mathbb{R}$ be multilinear and $\mathcal{A}$ the skew-symmetrizer (Definition [[§76 The Wedge Product#^def-76-4|§76.4]]).
>
> 1. $\mathcal{A}(T)$ is alternating: $\mathcal{A}(T) \in \Lambda^n V^{\ast}$.
> 2. If $T$ is alternating, then $\mathcal{A}(T) = T$.
>
> So $\mathcal{A}$ is a linear projection of the space of multilinear maps $V^n \to \mathbb{R}$ onto $\Lambda^n V^{\ast}$: its image is $\Lambda^n V^{\ast}$, and $\mathcal{A} \circ \mathcal{A} = \mathcal{A}$.
>
> *Lee: Proposition 14.3*

^lem-76-2

> [!proof]+ Proof
> *(Not proved in lecture; filled in.)* *A rule for rearranging twice.* For $\pi, \mu \in S_n$, $(T^\pi)^\mu = T^{\mu \circ \pi}$. Indeed, put $w^i = v^{\mu(i)}$; then
>
> $$
> \begin{aligned}
> (T^\pi)^\mu(v^1, \ldots, v^n) &= T^\pi(w^1, \ldots, w^n) = T\big(w^{\pi(1)}, \ldots, w^{\pi(n)}\big) \\
> &= T\big(v^{\mu(\pi(1))}, \ldots, v^{\mu(\pi(n))}\big) = T^{\mu \circ \pi}(v^1, \ldots, v^n) .
> \end{aligned}
> $$
>
> (1) Let $\mu \in S_n$. By the rule, and since $\operatorname{sgn}(\pi) = \operatorname{sgn}(\mu)\, \operatorname{sgn}(\mu \circ \pi)$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](1), with $\operatorname{sgn}(\mu)^2 = 1$),
>
> $$
> \mathcal{A}(T)^\mu = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, T^{\mu \circ \pi} = \operatorname{sgn}(\mu)\, \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\mu \circ \pi)\, T^{\mu \circ \pi} = \operatorname{sgn}(\mu)\, \mathcal{A}(T) ;
> $$
>
> the last step holds because $\pi \mapsto \mu \circ \pi$ is a bijection of $S_n$, so the sum runs over all of $S_n$ again. Thus $\mathcal{A}(T)\big(v^{\mu(1)}, \ldots, v^{\mu(n)}\big) = \operatorname{sgn}(\mu)\, \mathcal{A}(T)(v^1, \ldots, v^n)$ for every $\mu$, and $\mathcal{A}(T)$ is multilinear. By the converse in Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]], $\mathcal{A}(T)$ is alternating.
>
> (2) If $T$ is alternating, $T^\pi = \operatorname{sgn}(\pi)\, T$ for every $\pi$, by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]]. Then $\mathcal{A}(T) = \frac{1}{n!} \sum_\pi \operatorname{sgn}(\pi)^2\, T = T$, as $S_n$ has $n!$ elements.
>
> *The projection.* By (1) the image of $\mathcal{A}$ lies in $\Lambda^n V^{\ast}$, and by (2) every element of $\Lambda^n V^{\ast}$ is its own image. Applying (2) to the alternating map $\mathcal{A}(T)$ gives $\mathcal{A}(\mathcal{A}(T)) = \mathcal{A}(T)$.

^pf-76-2

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]]

> [!theorem] Proposition §76.3: The Wedge Product as a Skew-Symmetrized Tensor Product
> Let $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$.
>
> 1. The wedge product (Definition [[§76 The Wedge Product#^def-76-2|§76.2]]) is also the sum over all permutations, divided by $k!\, l!$:
>
> $$
> (\alpha \wedge \beta)(v^1, \ldots, v^{k+l}) = \frac{1}{k!\, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi)\, \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big)\, \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(k+l)}\big) .
> $$
>
> 2. In terms of the tensor product (Definition [[§76 The Wedge Product#^def-76-3|§76.3]]) and the skew-symmetrizer (Definition [[§76 The Wedge Product#^def-76-4|§76.4]]),
>
> $$
> \alpha \wedge \beta = \frac{(k + l)!}{k!\, l!}\, \mathcal{A}(\alpha \otimes \beta) .
> $$
>
> 3. $\alpha \wedge \beta$ is a linear $(k + l)$-form: $\alpha \wedge \beta \in \Lambda^{k+l} V^{\ast}$.
>
> *Lee: Ch. 14, The Wedge Product*

^prop-76-3

> [!proof]+ Proof
> *((1) was stated in Lecture 29, and (2) in the form $\alpha \wedge \beta = \mathcal{A}(\alpha \otimes \beta)$; the proofs and the factor in (2) are filled in.)* Write $n = k + l$.
>
> (1) Let $\pi \in S_n$ and factor it as $\pi = \sigma \circ \rho$ with $\sigma \in \mathrm{Sh}(k, l)$ and $\rho \in S_k \times S_l$ (Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](3)), where $\rho$ acts by $\tau \in S_k$ on $\{1, \ldots, k\}$ and by $\rho(k + j) = k + \tau'(j)$, $\tau' \in S_l$. Put $u^i = v^{\sigma(i)}$ for $i \le k$ and $w^j = v^{\sigma(k + j)}$ for $j \le l$. Then $v^{\pi(i)} = v^{\sigma(\tau(i))} = u^{\tau(i)}$ and $v^{\pi(k + j)} = v^{\sigma(k + \tau'(j))} = w^{\tau'(j)}$, and by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]], applied to $\alpha$ and to $\beta$,
>
> $$
> \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big) = \alpha\big(u^{\tau(1)}, \ldots, u^{\tau(k)}\big) = \operatorname{sgn}(\tau)\, \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big) ,
> $$
>
> $$
> \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(k+l)}\big) = \beta\big(w^{\tau'(1)}, \ldots, w^{\tau'(l)}\big) = \operatorname{sgn}(\tau')\, \beta\big(v^{\sigma(k+1)}, \ldots, v^{\sigma(k+l)}\big) .
> $$
>
> Also $\operatorname{sgn}(\pi) = \operatorname{sgn}(\sigma)\, \operatorname{sgn}(\rho) = \operatorname{sgn}(\sigma)\, \operatorname{sgn}(\tau)\, \operatorname{sgn}(\tau')$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](1) and Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](1)). Multiplying the three equations, the signs of $\tau$ and $\tau'$ appear squared, and the term of $\pi$ in the sum over $S_n$ equals the term of $\sigma$ in the sum over shuffles:
>
> $$
> \operatorname{sgn}(\pi)\, \alpha\big(v^{\pi(1)}, \ldots\big)\, \beta\big(v^{\pi(k+1)}, \ldots\big) = \operatorname{sgn}(\sigma)\, \alpha\big(v^{\sigma(1)}, \ldots\big)\, \beta\big(v^{\sigma(k+1)}, \ldots\big) .
> $$
>
> By the uniqueness of the factorization, the permutations $\pi$ with a given shuffle $\sigma$ are the $\sigma \circ \rho$ with $\rho \in S_k \times S_l$, and there are $k!\, l!$ of them. So the sum over $S_n$ is $k!\, l!$ times the sum over $\mathrm{Sh}(k, l)$.
>
> (2) By Definitions [[§76 The Wedge Product#^def-76-3|§76.3]] and [[§76 The Wedge Product#^def-76-4|§76.4]], $(\alpha \otimes \beta)^\pi(v^1, \ldots, v^n) = \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big)\, \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(n)}\big)$, so the sum in (1) is $\sum_\pi \operatorname{sgn}(\pi)\, (\alpha \otimes \beta)^\pi = n!\, \mathcal{A}(\alpha \otimes \beta)$. Dividing by $k!\, l!$ gives (2).
>
> (3) $\mathcal{A}(\alpha \otimes \beta) \in \Lambda^n V^{\ast}$ by Lemma [[§76 The Wedge Product#^lem-76-2|§76.2]](1), and $\Lambda^n V^{\ast}$ is a vector space; so (3) follows from (2).

^pf-76-3

*Uses:* [[§76 The Wedge Product#^lem-76-1|§76.1]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§76 The Wedge Product#^def-76-3|Def. §76.3]], [[§76 The Wedge Product#^def-76-4|Def. §76.4]], [[§76 The Wedge Product#^lem-76-2|§76.2]]

> [!remark] Remark: Two Conventions for the Wedge Product
> The board wrote $\alpha \wedge \beta = \mathcal{A}(\alpha \otimes \beta)$: take the tensor product, then its skew-symmetric part. With $\mathcal{A}$ normalized as a projection (Lemma [[§76 The Wedge Product#^lem-76-2|§76.2]]), this holds up to the factor $\binom{k+l}{k}$ of Proposition [[§76 The Wedge Product#^prop-76-3|§76.3]](2). Lee defines the wedge product by the formula with the factor and calls this the *determinant convention*: the factor is what makes $\varepsilon^{a_1} \wedge \cdots \wedge \varepsilon^{a_k}$ equal to the determinant $\varepsilon^A$ with no factorials (Proposition [[§76 The Wedge Product#^prop-76-4|§76.4]](4)), and it is the convention of the shuffle formula of Definition [[§76 The Wedge Product#^def-76-2|§76.2]], which has no factorials at all. Some books, for example Kobayashi–Nomizu, define the product as $\mathcal{A}(\alpha \otimes \beta)$ without the factor (the *Alt convention*); their wedge product differs from this one by the constant $\binom{k+l}{k}$.

^rem-76-1

> [!example] Example §76.2: The Wedge of Two One-Forms
> Let $k = l = 1$, so $\alpha, \beta \in V^{\ast}$. The group $S_2$ has two elements, the identity $(1, 2)$ and the transposition $(2, 1)$ in one-line notation, and both are shuffles: $\mathrm{Sh}(1, 1) = S_2$, because with $k = l = 1$ there are no two values to compare. The identity has sign $+1$ and the transposition $-1$, so
>
> $$
> (\alpha \wedge \beta)(v^1, v^2) = \alpha(v^1)\beta(v^2) - \alpha(v^2)\beta(v^1) = \det \begin{pmatrix} \alpha(v^1) & \alpha(v^2) \\ \beta(v^1) & \beta(v^2) \end{pmatrix} .
> $$
>
> *Lee: Ch. 14, The Wedge Product*

^ex-76-2

This is the formula of Lecture 28: for $\alpha = dx^i$ and $\beta = dx^j$ on $\mathbb{R}^3$ it gives $(dx^i \wedge dx^j)(u, v) = u^i v^j - u^j v^i$, which is Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]. So the two-form named $dx^i \wedge dx^j$ there is the wedge product of the one-forms $dx^i$ and $dx^j$. This case of the wedge product is the one used most often. The next case, $k = 1$ and $l = 2$, is left for Lecture 30.

![[m591-76-3.svg]]

*(Not from lecture; figure added.)* Example [[§76 The Wedge Product#^ex-76-2|§76.2]] as an area, for the covectors $\alpha(x) = 0.9\, x^1 + 0.3\, x^2$ and $\beta(x) = -0.35\, x^1 + 0.85\, x^2$ on $V = \mathbb{R}^2$. Left: the level lines $\alpha = 0, 1, 2, \ldots$ (blue) and $\beta = 0, 1, 2, \ldots$ (red) cut $V$ into cells; the cell $0 \le \alpha \le 1$, $0 \le \beta \le 1$ is shaded grey. Right: the linear map $v \mapsto (\alpha(v), \beta(v))$ sends the cells to the unit squares of the $(\alpha, \beta)$-plane, and the vectors $v^1, v^2$ to $(\alpha(v^1), \beta(v^1)) = (2, 0.5)$ and $(\alpha(v^2), \beta(v^2)) = (0.5, 1.5)$. The determinant $(\alpha \wedge \beta)(v^1, v^2) = 2 \cdot 1.5 - 0.5 \cdot 0.5 = 2.75$ is the signed area of the parallelogram on the right, which is the area of the parallelogram spanned by $v^1$ and $v^2$ on the left measured in cells of the grid (orange). Exchanging $v^1$ and $v^2$ reverses the orientation and the sign.

> [!example] Example §76.3: The Wedge of Two Two-Forms
> *(Not from lecture; filled in.)* Let $k = l = 2$. A $(2, 2)$-shuffle is determined by the two places $\sigma(1) < \sigma(2)$, so there are $\binom{4}{2} = 6$ of them (Lemma [[§76 The Wedge Product#^lem-76-1|§76.1]](2)); in one-line notation, with their signs, they are
>
> $$
> (1, 2, 3, 4)\ {+}, \quad (1, 3, 2, 4)\ {-}, \quad (1, 4, 2, 3)\ {+}, \quad (2, 3, 1, 4)\ {+}, \quad (2, 4, 1, 3)\ {-}, \quad (3, 4, 1, 2)\ {+} ,
> $$
>
> with $0, 1, 2, 2, 3, 4$ inversions. For $\alpha, \beta \in \Lambda^2 V^{\ast}$, Definition [[§76 The Wedge Product#^def-76-2|§76.2]] gives
>
> $$
> \begin{aligned}
> (\alpha \wedge \beta)(v^1, v^2, v^3, v^4) ={}& \alpha(v^1, v^2)\beta(v^3, v^4) - \alpha(v^1, v^3)\beta(v^2, v^4) + \alpha(v^1, v^4)\beta(v^2, v^3) \\
> &+ \alpha(v^2, v^3)\beta(v^1, v^4) - \alpha(v^2, v^4)\beta(v^1, v^3) + \alpha(v^3, v^4)\beta(v^1, v^2) .
> \end{aligned}
> $$

^ex-76-3

![[m591-76-2.svg]]

*(Not from lecture; figure added.)* The six $(2, 2)$-shuffles of Example [[§76 The Wedge Product#^ex-76-3|§76.3]]. In each diagram the top row is the entries $1, 2$ of $\alpha$ (red) and $3, 4$ of $\beta$ (blue), and the strand from $i$ ends at the vector $v^{\sigma(i)}$ that this entry receives. Strands of the same colour never cross, which is the shuffle condition. Each crossing of a red strand with a blue one (black dot) is an inversion of $\sigma$, so the sign of the term is $+$ for an even number of crossings (green) and $-$ for an odd number (red).

> [!theorem] Proposition §76.4: Properties of the Wedge Product
> For $\alpha, \alpha_1, \alpha_2 \in \Lambda^k V^{\ast}$, $\beta \in \Lambda^l V^{\ast}$, $\gamma \in \Lambda^r V^{\ast}$ and $\lambda \in \mathbb{R}$:
>
> 1. *bilinear*: $(\alpha_1 + \lambda\alpha_2) \wedge \beta = \alpha_1 \wedge \beta + \lambda\, \alpha_2 \wedge \beta$, and likewise in $\beta$;
> 2. *associative*: $\alpha \wedge (\beta \wedge \gamma) = (\alpha \wedge \beta) \wedge \gamma$;
> 3. *graded anticommutative*: $\beta \wedge \alpha = (-1)^{kl}\, \alpha \wedge \beta$; in particular, forms of even degree commute with all forms;
> 4. for a basis $(\varepsilon^i)$ of $V^{\ast}$ and $A = \{a_1 < \cdots < a_k\}$: $\varepsilon^A = \varepsilon^{a_1} \wedge \cdots \wedge \varepsilon^{a_k}$ (Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]]).
>
> *Lee: Proposition 14.11*

^prop-76-4

> [!proof]+ Proof (to be filled)
> Lecture 29 stated the four properties without proof. (1) is immediate from Definition [[§76 The Wedge Product#^def-76-2|§76.2]], each term of the sum being linear in $\alpha$ and in $\beta$. In (3), forms of even degree commute with all forms because $(-1)^{kl} = 1$ when $k$ or $l$ is even. (4) is a nontrivial computation: the shuffle formula is, in disguise, an expansion of a determinant. (2)–(4) are to be filled.

^pf-76-4

*Uses:* [[§76 The Wedge Product#^def-76-2|Def. §76.2]]

> [!theorem] Corollary §76.5: Forms of Odd Degree Square to Zero
> If $\alpha \in \Lambda^k V^{\ast}$ with $k$ odd, then $\alpha \wedge \alpha = 0$. In particular $\varepsilon \wedge \varepsilon = 0$ for every covector $\varepsilon \in V^{\ast}$.

^cor-76-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By Proposition [[§76 The Wedge Product#^prop-76-4|§76.4]](3) with $\beta = \alpha$ and $l = k$: $\alpha \wedge \alpha = (-1)^{k^2}\, \alpha \wedge \alpha = -\alpha \wedge \alpha$, since $k^2$ is odd. So $2\, \alpha \wedge \alpha = 0$. For a covector, $k = 1$; this can also be read off Example [[§76 The Wedge Product#^ex-76-2|§76.2]]: $(\varepsilon \wedge \varepsilon)(v^1, v^2) = \varepsilon(v^1)\varepsilon(v^2) - \varepsilon(v^2)\varepsilon(v^1) = 0$.

^pf-76-5

*Uses:* [[§76 The Wedge Product#^prop-76-4|§76.4]], [[§76 The Wedge Product#^ex-76-2|Ex. §76.2]]

For $\varepsilon = dx^i$ this is $dx^i \wedge dx^i = 0$, as in Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](2).

> [!example] Example §76.4: A Form of Even Degree with Nonzero Square
> *(Not from lecture; filled in.)* For even degree the corollary fails. On $\mathbb{R}^4$ let
>
> $$
> \omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4 \in \Lambda^2 (\mathbb{R}^4)^{\ast} , \qquad \omega(u, v) = u^1 v^2 - u^2 v^1 + u^3 v^4 - u^4 v^3
> $$
>
> (Example [[§75 Multilinear Algebra#^ex-75-2|§75.2]]). On the standard basis, $\omega(e_1, e_2) = \omega(e_3, e_4) = 1$, and $\omega(e_i, e_j) = 0$ for the other pairs $i < j$. By the six-term formula of Example [[§76 The Wedge Product#^ex-76-3|§76.3]] with $\alpha = \beta = \omega$, only the first and the last term are not zero:
>
> $$
> (\omega \wedge \omega)(e_1, e_2, e_3, e_4) = \omega(e_1, e_2)\,\omega(e_3, e_4) + \omega(e_3, e_4)\,\omega(e_1, e_2) = 2 .
> $$
>
> So $\omega \wedge \omega \neq 0$. By Corollary [[§75 Multilinear Algebra#^cor-75-7|§75.7]], $\omega \wedge \omega = 2\, \varepsilon^{\{1, 2, 3, 4\}}$, twice the determinant; with Proposition [[§76 The Wedge Product#^prop-76-4|§76.4]](4) this reads $\omega \wedge \omega = 2\, dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4$.

^ex-76-4

Next (Lecture 30): more computations in low degree; then $V$ becomes the tangent space $T_pM$ again, and the point $p$ varies over a manifold, so that the forms become functions of the point.
