---
type: section
subject: "[[Group Theory]]"
chapter: 5
section: 20
tags: [group-theory, math493]
---
← [[§19 Polynomial Rings, Permutation Matrices, and Representations]] · ↑ [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] · [[§21 The Structure of Uₙ]] →

*Reference: Pinter Ch. 8 (even and odd permutations).*

*Source: [[493 Problem Set 1#^hw-1-5|PS 1.5]]; class discussion (Wed Sept 9).*

> [!definition] Definition §20.1: Inversions of a Permutation
> For $\sigma \in S_n$, an **inversion** of $\sigma$ is a pair $(i, j)$ with $1 \leq i < j \leq n$ and $\sigma(i) > \sigma(j)$: a pair whose order is reversed by $\sigma$. The number of inversions is written
>
> $$
> \operatorname{inv}(\sigma) = \#\{(i, j) : 1 \leq i < j \leq n,\ \sigma(i) > \sigma(j)\}.
> $$
>
> Equivalently, $\operatorname{inv}(\sigma)$ counts the pairs of entries in the sequence $(\sigma(1), \ldots, \sigma(n))$ that appear in decreasing order. An **adjacent inversion** is an index $k$ with $\sigma(k) > \sigma(k+1)$.

^def-20-1

> [!theorem] Lemma §20.1: Sorting by Adjacent Swaps
> Consider a sequence of $n$ distinct numbers, and let $\operatorname{inv}$ denote its number of inversions (pairs of positions $i < j$ whose entries are in decreasing order).
> 1. Swapping the two entries at an adjacent inversion decreases $\operatorname{inv}$ by exactly $1$.
> 2. The sequence has no adjacent inversion if and only if $\operatorname{inv} = 0$, i.e. it is sorted increasingly.
> 3. Consequently, repeatedly swapping at any adjacent inversion (*bubble sort*) terminates in the sorted sequence after exactly $\operatorname{inv}$ swaps.
> 4. If the sequence is $(\rho(1), \ldots, \rho(n))$ for $\rho \in S_n$, then swapping the entries at positions $k, k+1$ produces the sequence of $\rho \circ (k\ \ k{+}1)$.

^lem-20-1

> [!proof]+ Proof
> **(1)** For each value $v$ in the sequence, let $L(v)$ be the number of larger values appearing before $v$. Every inversion is counted exactly once, at its later (smaller) entry, so $\operatorname{inv} = \sum_v L(v)$. Let $p, q$ be adjacent with $p$ before $q$ and $p > q$, and swap them. $L(p)$ is unchanged ($q$ now precedes $p$, but $q < p$). $L(q)$ drops by exactly $1$ ($p$ no longer precedes $q$, and $p > q$ did count). For every other $v$, the set of values preceding $v$ is unchanged, since $p, q$ are both before $v$ or both after. So $\operatorname{inv}$ decreases by $1$.
>
> **(2)** If $\operatorname{inv} = 0$ there are no inversions at all. Conversely, with no adjacent inversion the entries strictly increase from each position to the next, hence (by transitivity) from any position to any later one, so $\operatorname{inv} = 0$.
>
> **(3)** By (1) and (2), a swap is available exactly when $\operatorname{inv} > 0$ and each swap lowers $\operatorname{inv}$ by $1$; so the process performs exactly $\operatorname{inv}$ swaps and stops at $\operatorname{inv} = 0$.
>
> **(4)** The new entry at position $k$ is $\rho(k+1) = (\rho \circ (k\ k{+}1))(k)$, at position $k+1$ it is $\rho(k) = (\rho \circ (k\ k{+}1))(k+1)$, and other positions are unchanged, as $(k\ k{+}1)$ fixes them.

^pf-20-1

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^def-20-1|Def. §20.1]]

![[m493-20-1.svg]]
*Bubble sort on the sequence $(4, 3, 1, 2)$ of $\sigma = (1\,4\,2\,3)$ from [[§19 Polynomial Rings, Permutation Matrices, and Representations#^ex-19-2|Ex. §19.2]]. Each red crossing swaps an adjacent inversion and lowers $\operatorname{inv}$ by exactly one, so sorting takes $\operatorname{inv}(\sigma) = 5$ swaps and $\operatorname{sgn}(\sigma) = (-1)^5 = -1$. Two wires cross exactly when their values form an inversion ($1$ and $2$ never cross). Reading the swaps backwards gives [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]] (1): $\sigma = t_5 t_4 t_3 t_2 t_1 = (2\,3)(1\,2)(3\,4)(2\,3)(1\,2)$.*

> [!remark]- Connections
> - Linear-algebra counterpart: [[§33 Alternating Multilinear Forms#^ladr-9-34|LADR 9.34]] (swapping two entries of a permutation changes the parity of the number of inversions).

> [!theorem] Theorem §20.2: Three Formulas for the Sign
> Let $\sigma \in S_n$, let $\Delta = \prod_{1 \leq i < j \leq n}(x_i - x_j) \in \mathbb{Q}[x_1, \ldots, x_n]$, and let $M(\sigma)$ be the [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5|permutation matrix]]. Then
>
> $$
> \frac{\sigma \cdot \Delta}{\Delta} \;=\; (-1)^{\operatorname{inv}(\sigma)} \;=\; \det M(\sigma).
> $$
>
> *Source: PS 1.5(1)*

^thm-20-2

> [!proof]+ Proof
> **First equality.** $\sigma \cdot \Delta = \prod_{i<j}(x_{\sigma(i)} - x_{\sigma(j)})$. Let $\mathcal{P}$ be the set of $2$-element subsets of $\{1, \ldots, n\}$; the factors of $\Delta$ correspond to $\mathcal{P}$, the subset $\{i, j\}$ ($i < j$) giving $x_i - x_j$ with the smaller index first. The map $\Sigma: \{i, j\} \mapsto \{\sigma(i), \sigma(j)\}$ is a bijection $\mathcal{P} \to \mathcal{P}$ (well-defined and lands in $\mathcal{P}$ by injectivity of $\sigma$; injective by applying $\sigma^{-1}$; surjective by surjectivity of $\sigma$). For a fixed pair $i < j$, the factor $x_{\sigma(i)} - x_{\sigma(j)}$ of $\sigma\cdot\Delta$ equals the $\Delta$-factor of $\Sigma(\{i,j\})$ if $\sigma(i) < \sigma(j)$, and equals *minus* it if $\sigma(i) > \sigma(j)$, i.e. exactly when $(i, j)$ is an inversion. Since multiplication of polynomials is commutative, the order of the factors is immaterial, and reindexing along $\Sigma$ gives
>
> $$
> \sigma \cdot \Delta = (-1)^{\operatorname{inv}(\sigma)} \prod_{\{i,j\} \in \mathcal{P}} (\Delta\text{-factor of } \Sigma\{i,j\}) = (-1)^{\operatorname{inv}(\sigma)}\, \Delta.
> $$
>
> As $\Delta$ is a product of nonzero polynomials it is nonzero, so $\sigma\cdot\Delta/\Delta = (-1)^{\operatorname{inv}(\sigma)}$.
>
> **Second equality.** The columns of $M(\sigma)$ are $e_{\sigma(1)}, \ldots, e_{\sigma(n)}$, so swapping entries at positions $k, k+1$ of the sequence $(\sigma(1), \ldots, \sigma(n))$ is exactly swapping columns $k, k+1$ of the matrix, which [[§34 Determinants#^ladr-9-57|multiplies the determinant by]] $-1$. Bubble sort ([[§20 The Sign Homomorphism and the Alternating Group#^lem-20-1|Lemma (3)]]) reaches the sequence $(1, \ldots, n)$, whose matrix is $I_n$, after exactly $\operatorname{inv}(\sigma)$ swaps. Hence $\det M(\sigma) = (-1)^{\operatorname{inv}(\sigma)} \det I_n = (-1)^{\operatorname{inv}(\sigma)}$.

^pf-20-2

*Uses:* [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-3|Def. §19.3]], [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-1|§19.1]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-1|Def. §20.1]], [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-1|§20.1]], [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5|Def. §19.5]], [[§34 Determinants#^ladr-9-57|LADR 9.57]], [[§34 Determinants#^ladr-9-44|LADR 9.44]]

> [!remark]- Connections
> - Linear-algebra home of the determinant facts: column swaps change the sign, [[§34 Determinants#^ladr-9-57|LADR 9.57]] (b); $\det I = 1$, [[§34 Determinants#^ladr-9-44|LADR 9.44]].
> - The sign $(-1)^{\operatorname{inv}}$ is the one in the Leibniz formula for $\det$: [[§34 Determinants#^ladr-9-46|LADR 9.46]].

> [!definition] Definition §20.2: The Sign; Even and Odd Permutations
> The **sign** of $\sigma \in S_n$ is $\operatorname{sgn}(\sigma) := \det M(\sigma) = (-1)^{\operatorname{inv}(\sigma)} = \sigma\cdot\Delta/\Delta \in \{\pm 1\}$. A permutation is **even** if $\operatorname{sgn}(\sigma) = 1$ and **odd** if $\operatorname{sgn}(\sigma) = -1$. (The problem sets write $\varepsilon(\sigma)$; the lectures, and these notes, write $\operatorname{sgn}(\sigma)$.)

^def-20-2

> [!remark]- Connections
> - Linear algebra defines the sign by inversions: [[§33 Alternating Multilinear Forms#^ladr-9-32|LADR 9.32]].
> - Restated in 591 for the Leibniz formula and continuity of the determinant: [[§5 Topological Groups and Classical Matrix Groups#^def-5-3|591 Def. §5.3]], properties in [[§5 Topological Groups and Classical Matrix Groups#^prop-5-2|591 Prop. §5.2]].

> [!theorem] Theorem §20.3: The Sign Is a Homomorphism
> $\operatorname{sgn}: S_n \to \{\pm 1\}$ is a group [[§15 Homomorphisms#^def-15-1|homomorphism]], where $\{\pm 1\}$ is a group under multiplication.
>
> *Source: PS 1.5(2)*

^thm-20-3

> [!proof]+ Proof
> By [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]], $M(\sigma\tau) = M(\sigma)M(\tau)$. Hence $\operatorname{sgn}(\sigma\tau) = \det(M(\sigma)M(\tau)) = \det M(\sigma)\det M(\tau) = \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$, by [[§34 Determinants#^ladr-9-49|multiplicativity of the determinant]].

^pf-20-3

*Uses:* [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|Def. §20.2]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§34 Determinants#^ladr-9-49|LADR 9.49]]

> [!remark]- Connections
> - Linear-algebra home: [[§34 Determinants#^ladr-9-49|Determinant is multiplicative]] (LADR 9.49).

> [!theorem] Corollary §20.4: Parity of a Permutation
> 1. Every transposition is odd: $\operatorname{sgn}((a\ b)) = -1$.
> 2. If $\sigma$ is a product of $m$ transpositions, then $\operatorname{sgn}(\sigma) = (-1)^m$. In particular, the parity of the number of transpositions in any factorization of $\sigma$ is the same for all factorizations, and equals the parity of $\operatorname{inv}(\sigma)$.
> 3. An $r$-cycle has sign $(-1)^{r-1}$; the sign of a product of disjoint cycles is the product of the signs.

^cor-20-4

> [!proof]+ Proof
> (1) $M((a\ b))$ is $I_n$ with columns $a$ and $b$ exchanged, so its determinant is $-1$. (2) Apply the homomorphism property $m - 1$ times. Since $\operatorname{sgn}(\sigma)$ is defined independently of any factorization, two factorizations with $m$ and $m'$ transpositions give $(-1)^m = (-1)^{m'}$. (3) $(a_1 \cdots a_r) = (a_1\,a_r)(a_1\,a_{r-1})\cdots(a_1\,a_2)$ is a product of $r - 1$ transpositions ([[§12 Multiplying and Conjugating Cycles#^prop-12-2|§12.2]]); then apply (2) and the homomorphism property to disjoint factors.

^pf-20-4

*Uses:* [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5|Def. §19.5]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|Def. §20.2]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§12 Multiplying and Conjugating Cycles#^prop-12-2|§12.2]], [[§34 Determinants#^ladr-9-57|LADR 9.57]], [[§34 Determinants#^ladr-9-44|LADR 9.44]]

> [!remark] Remark: Parity, Settled
> [[§12 Multiplying and Conjugating Cycles#^rem-12-1|§12]] noted that factorizations into transpositions are far from unique and that “only the parity is an invariant” — deferred to this problem. [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|Corollary (2)]] is that statement, and the reason it holds is that parity is computed by a function $\operatorname{sgn}$ defined without reference to factorizations (via $\Delta$, inversions, or determinants) which happens to take the value $-1$ on every transposition.

^rem-20-1

> [!remark] Remark: Speyer's Presentation: $\operatorname{sgn} = \det \circ M$
> In class the sign is written $\operatorname{sgn}$ and introduced as the composite
>
> $$
> S_n \xrightarrow{\ \sigma \mapsto M(\sigma)\ } GL_n(\mathbb{R}) \xrightarrow{\ \det\ } \mathbb{R}^\times,
> $$
>
> a composition of two homomorphisms ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]] for the first, [[§34 Determinants#^ladr-9-49|multiplicativity]] of $\det$ for the second), hence a homomorphism, with the one thing “needing proof” being $M(\sigma\tau) = M(\sigma)M(\tau)$. Its image is $\{\pm 1\} \cong \mathbb{Z}/2\mathbb{Z}$ (it takes both values, e.g. on $e$ and $(1\,2)$), and its kernel is the [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|alternating group]] $A_n$. The problem sets write $\varepsilon$ for this map; these notes follow the lecture and write $\operatorname{sgn}$ throughout.

^rem-20-2

> [!definition] Definition §20.3: The Alternating Group $A_n$
> The **alternating group** $A_n$ is the [[§15 Homomorphisms#^def-15-2|kernel]] of the sign homomorphism, $A_n := \operatorname{Ker}(\operatorname{sgn}) = \{\sigma \in S_n : \operatorname{sgn}(\sigma) = 1\}$, the subgroup of even permutations.

^def-20-3

> [!remark]- Connections
> - As a kernel, $A_n$ is normal: [[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]]; it is simple for $n \geq 5$: [[§39 Simple Groups#^thm-39-9|§39.9]].

> [!theorem] Proposition §20.5: Size of $A_n$
> For $n \geq 2$, $\operatorname{sgn}$ is surjective and $|A_n| = n!/2$: exactly half the permutations are even.

^prop-20-5

> [!proof]+ Proof
> $\operatorname{sgn}((1\,2)) = -1$, so $\operatorname{sgn}$ is surjective. The map $\sigma \mapsto (1\,2)\sigma$ sends even permutations to odd ones ($\operatorname{sgn}((1\,2)\sigma) = -\operatorname{sgn}(\sigma)$) and is its own inverse ($(1\,2)^2 = e$), hence is a bijection $A_n \to S_n \setminus A_n$. So the two sets have equal size, $n!/2$.

^pf-20-5

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]]

![[m493-20-2.svg]]
*The proof for $n = 3$: left multiplication by $(1\,2)$ flips the sign, so it exchanges the three even permutations, $A_3$ (blue), with the three odd ones (red). Being its own inverse it is a bijection, and $|A_3| = 3!/2 = 3$.*

> [!remark]- Connections
> - Later readings: $A_n$ has index $2$, hence is normal by [[§36 Sources of Normal Subgroups#^prop-36-1|Subgroups of Index 2 Are Normal]]; the count is an instance of [[§38 The First Isomorphism Theorem#^cor-38-2|§38.2]].

> [!theorem] Lemma §20.6: Adjacent Transpositions from $(1\,j)$'s
> For $k \geq 2$, $\ (k\ \ k{+}1) = (1\,k)\,(1\ k{+}1)\,(1\,k)$; and $(1\,2)$ is itself of the form $(1\,j)$.

^lem-20-6

> [!proof]+ Proof
> Track elements through the three factors (right first): $1 \mapsto k \mapsto k \mapsto 1$; $k \mapsto 1 \mapsto k{+}1 \mapsto k{+}1$; $k{+}1 \mapsto k{+}1 \mapsto 1 \mapsto k$; all other elements are fixed by every factor. The product exchanges $k \leftrightarrow k{+}1$ and fixes everything else. (The word is a palindrome, so the result is the same under either composition convention; it is also the conjugation relabeling $(1\,k)(1\ k{+}1)(1\,k)^{-1} = ((1\,k)(1)\ \ (1\,k)(k{+}1)) = (k\ \ k{+}1)$ of [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]].)

^pf-20-6

*Uses:* [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex. §12.1]], [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]]

> [!theorem] Theorem §20.7: Generators of $S_n$
> 1. Every $\sigma \in S_n$ is a product of exactly $\operatorname{inv}(\sigma)$ adjacent transpositions $(k\ \ k{+}1)$.
> 2. $S_n$ is generated by the adjacent transpositions, and also by the transpositions $(1\,j)$, $2 \leq j \leq n$.
>
> *Source: PS 1.5(3)*

^thm-20-7

> [!proof]+ Proof
> **(1)** Bubble-sort the sequence $(\sigma(1), \ldots, \sigma(n))$; by the [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-1|Sorting Lemma]] it performs $m = \operatorname{inv}(\sigma)$ swaps, at positions $(k_1, k_1{+}1), \ldots, (k_m, k_m{+}1)$ in that order, and ends at $(1, \ldots, n)$. By [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-1|Lemma (4)]], with $t_i = (k_i\ \ k_i{+}1)$, the final sequence is that of $\sigma t_1 t_2 \cdots t_m$; a permutation is determined by its sequence of values, and $(1, \ldots, n)$ is the sequence of $e$, so $\sigma t_1 \cdots t_m = e$. Hence $\sigma = (t_1 \cdots t_m)^{-1} = t_m^{-1} \cdots t_1^{-1} = t_m \cdots t_1$, since each transposition is its own inverse.
>
> **(2)** By (1), the adjacent transpositions generate $S_n$. By Adjacent Transpositions from $(1\,j)$'s ([[§20 The Sign Homomorphism and the Alternating Group#^lem-20-6|§20.6]]), each adjacent transposition is a product of elements $(1\,j)$, so substituting expresses every $\sigma$ as a product of $(1\,j)$'s; each $(1\,j)$ is its own inverse, so no inverses are needed.

^pf-20-7

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-1|§20.1]], [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-6|§20.6]], [[§2 First Consequences of the Axioms#^cor-2-5|§2.5]], [[§4 Subgroups#^def-4-4|Def. §4.4]]

> [!theorem] Lemma §20.8: Products of Two $(1\,j)$'s
> For $k \geq 3$: $\ (1\,k)(1\,2) = (1\,2\,k)$ and $(1\,2)(1\,k) = (1\,k\,2) = (1\,2\,k)^{-1}$. For distinct $j, k \geq 3$: $\ (1\,j)(1\,k) = (1\,2\,j)(1\,2\,k)^{-1}$.

^lem-20-8

> [!proof]+ Proof
> Tracking (right factor first): under $(1\,k)(1\,2)$, $1 \mapsto 2 \mapsto 2$, $2 \mapsto 1 \mapsto k$, $k \mapsto k \mapsto 1$, giving $(1\,2\,k)$; under $(1\,2)(1\,k)$, $1 \mapsto k \mapsto k$, $k \mapsto 1 \mapsto 2$, $2 \mapsto 2 \mapsto 1$, giving $(1\,k\,2)$, the reverse loop of $(1\,2\,k)$. For the last identity insert $(1\,2)(1\,2) = e$: $(1\,j)(1\,k) = (1\,j)(1\,2)\cdot(1\,2)(1\,k) = (1\,2\,j)(1\,2\,k)^{-1}$.

^pf-20-8

*Uses:* [[§12 Multiplying and Conjugating Cycles#^ex-12-1|Ex. §12.1]]

> [!theorem] Theorem §20.9: Generators of $A_n$
> For $n \geq 3$, the alternating group $A_n$ is generated by the $3$-cycles $(1\,2\,k)$, $3 \leq k \leq n$.
>
> *Source: PS 1.5(4)*

^thm-20-9

> [!proof]+ Proof
> Let $C = \{(1\,2\,k) : 3 \leq k \leq n\}$.
>
> **$\langle C \rangle \subseteq A_n$:** $\operatorname{sgn}((1\,2\,k)) = \operatorname{sgn}((1\,k))\operatorname{sgn}((1\,2)) = (-1)(-1) = 1$, using the factorization from Products of Two $(1\,j)$'s ([[§20 The Sign Homomorphism and the Alternating Group#^lem-20-8|§20.8]]), [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|Parity of a Permutation]] (1), and the [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|homomorphism property]]; so $C \subseteq A_n$; as $A_n$ is a subgroup ([[§15 Homomorphisms#^prop-15-2|a kernel]]), $\langle C \rangle \subseteq A_n$.
>
> **$A_n \subseteq \langle C \rangle$:** Let $\sigma \in A_n$. By the Generators of $S_n$ theorem ([[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]]), $\sigma = t_m \cdots t_1$ with $m = \operatorname{inv}(\sigma)$ adjacent transpositions, and $m$ is even since $\operatorname{sgn}(\sigma) = (-1)^m = 1$. Each $t_i$ is a product of $1$ or $3$ elements $(1\,j)$ (an odd number), so $\sigma$ is a product of $N$ elements of the form $(1\,j)$ with $N \equiv m \equiv 0 \pmod 2$. Group these $N$ factors into $N/2$ consecutive pairs. Each pair $(1\,j)(1\,k)$ is: $e$ if $j = k$; $(1\,2\,k)^{-1}$ or $(1\,2\,j)$ if one of $j, k$ equals $2$; and $(1\,2\,j)(1\,2\,k)^{-1}$ if $j, k \geq 3$ are distinct — in every case an element of $\langle C \rangle$ (by Products of Two $(1\,j)$'s, [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-8|§20.8]]). Hence $\sigma \in \langle C \rangle$. Since $(1\,2\,k)$ has order $3$ ([[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]), $(1\,2\,k)^{-1} = (1\,2\,k)^2$, so inverses are not even needed as separate generators.

^pf-20-9

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-8|§20.8]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]], [[§15 Homomorphisms#^prop-15-2|§15.2]], [[§4 Subgroups#^prop-4-7|§4.7]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]], [[§20 The Sign Homomorphism and the Alternating Group#^lem-20-6|§20.6]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]

> [!remark]- Connections
> - 3-cycles drive the simplicity of $A_n$: [[§39 Simple Groups#^lem-39-8|§39.8]], [[§39 Simple Groups#^thm-39-9|§39.9]]; and they are commutators: [[§41 Commutators#^prop-41-2|§41.2]], [[§41 Commutators#^thm-41-5|The Commutator Subgroup of Sₙ]].

> [!definition] Definition §20.4: Alternating Polynomial
> A polynomial $f \in \mathbb{Q}[x_1, \ldots, x_n]$ is **alternating** if $\sigma \cdot f = \operatorname{sgn}(\sigma) f$ for every $\sigma \in S_n$: fixed by even permutations and negated by odd ones. (Compare *symmetric*, $\sigma \cdot f = f$ for all $\sigma$; [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-3|Def. §19.3]].) By the [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-2|Three Formulas for the Sign]], $\Delta$ is alternating.

^def-20-4

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-2|§20.2]]

> [!theorem] Corollary §20.10: $A_n$ Is the Stabilizer of $\Delta$
> For $\sigma \in S_n$: $\ \sigma \cdot \Delta = \Delta$ if and only if $\sigma \in A_n$.

^cor-20-10

> [!proof]+ Proof
> $\sigma \cdot \Delta = \operatorname{sgn}(\sigma)\Delta$ and $\Delta \neq 0$. Over $\mathbb{Q}$, $-\Delta \neq \Delta$ (as $2\Delta \neq 0$), so $\operatorname{sgn}(\sigma)\Delta = \Delta$ iff $\operatorname{sgn}(\sigma) = 1$, i.e. iff $\sigma \in A_n$.

^pf-20-10

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-2|§20.2]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2|Def. §20.2]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]]

> [!remark]- Connections
> - In the language of actions: $A_n = \operatorname{Stab}(\Delta)$ ([[§24 Stabilizers and Fixed Points#^def-24-1|Def. §24.1]]); $\Delta$ as a common eigenvector giving the sign character: [[§40 Characters#^ex-40-2|Ex. §40.2]].

> [!remark] Remark: The Origin of the Names
> This is the historical origin of the names: the symmetric group is attached to the [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-3|symmetric polynomials]], and the alternating group is the stabilizer of the alternating polynomial $\Delta$ (whose square, the discriminant, is symmetric). The homomorphism $\operatorname{sgn}$ is also the first nontrivial [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|representation]] of $S_n$ into $GL_1 = \mathbb{Q}^\times$, alongside the permutation representation $\sigma \mapsto M(\sigma)$ into $GL_n$.

^rem-20-3
