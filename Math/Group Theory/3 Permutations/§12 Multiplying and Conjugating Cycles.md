---
type: section
subject: "[[Group Theory]]"
chapter: 3
section: 12
tags: [group-theory, math493]
---
← [[§11 Disjoint Cycle Decomposition]] · ↑ [[· 3 Permutations]] · [[§13 The Symmetric Group S₃]] →

*Reference: Pinter Ch. 8.*

> [!example] Example §12.1: Multiplying Cycles: The Tracking Algorithm
> To compute a product $c_k \cdots c_2 c_1$ of cycles (rightmost applied first) directly in cycle notation: start with the smallest unplaced number $x$, open a parenthesis, and push $x$ through the factors from right to left — in each cycle, $x$ becomes the entry after it (wrapping around), or is unchanged if absent. Write the output, then push the output through in the same way, and continue until returning to $x$; close the parenthesis. Repeat with the smallest unplaced number until all are placed; omit $1$-cycles.
>
> **Example.** $(1\,2\,3)(2\,4)$ in $S_4$:
>
> $$ 1 \xrightarrow{(2\,4)} 1 \xrightarrow{(1\,2\,3)} 2, \quad 2 \xrightarrow{(2\,4)} 4 \xrightarrow{(1\,2\,3)} 4, \quad 4 \xrightarrow{(2\,4)} 2 \xrightarrow{(1\,2\,3)} 3, \quad 3 \xrightarrow{(2\,4)} 3 \xrightarrow{(1\,2\,3)} 1. $$
>
> So $(1\,2\,3)(2\,4) = (1\,2\,4\,3)$.
>
> **Example with three factors.** $(1\,3)(2\,5\,4)(1\,2\,3\,5)$ in $S_5$: tracking gives $1 \to 2 \to 5 \to 5$, then $5 \to 1 \to 1 \to 3$, then $3 \to 5 \to 4 \to 4$, then $4 \to 4 \to 2 \to 2$, then $2 \to 3 \to 3 \to 1$. So the product is the single $5$-cycle $(1\,5\,3\,4\,2)$.
>
> **Checks.** Each number must appear at most once across the output cycles (the result is a bijection). The commonest error is reading a factor left to right; when a product looks wrong, recheck the direction first. Powers of a single cycle need no tracking: $c^m$ advances each entry $m$ steps along the loop, e.g. $(1\,2\,3\,4\,5)^2 = (1\,3\,5\,2\,4)$.

^ex-12-1

> [!theorem] Proposition §12.1: Conjugation Relabels a Cycle
> For any $\sigma \in S_n$ and any cycle $(a_1\ a_2\ \cdots\ a_r)$,
>
> $$ \sigma\,(a_1\ a_2\ \cdots\ a_r)\,\sigma^{-1} = \big(\sigma(a_1)\ \sigma(a_2)\ \cdots\ \sigma(a_r)\big). $$
>
> Consequently, conjugation preserves the cycle type (the multiset of cycle lengths) of any permutation.

^prop-12-1

> [!proof]+ Proof
> Let $\tau = (a_1 \cdots a_r)$. For each $i$, $(\sigma\tau\sigma^{-1})(\sigma(a_i)) = \sigma(\tau(a_i)) = \sigma(a_{i+1})$ (indices mod $r$), and for $y$ not of the form $\sigma(a_i)$, $\sigma^{-1}(y)$ is not among the $a_i$, so $\tau$ fixes it and $(\sigma\tau\sigma^{-1})(y) = y$. This is exactly the cycle $(\sigma(a_1) \cdots \sigma(a_r))$. For a product of disjoint cycles, conjugate factor by factor: $\sigma (c_1 \cdots c_k) \sigma^{-1} = (\sigma c_1 \sigma^{-1}) \cdots (\sigma c_k \sigma^{-1})$, and the relabeled cycles remain disjoint since $\sigma$ is injective.

^pf-12-1

*Uses:* [[§10 Cycle Notation and the Group S₃#^def-10-1|Def. §10.1]], [[§11 Disjoint Cycle Decomposition#^def-11-1|Def. §11.1]], [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]]

![[m493-12-1.svg]]
*Conjugation relabels a cycle. To evaluate $\sigma\tau\sigma^{-1}$ at $\sigma(a_i)$, go up the dashed arrow ($\sigma^{-1}$) to $a_i$, across by $\tau$ to $a_{i+1}$, and down by $\sigma$ to $\sigma(a_{i+1})$. So the red loop is the blue loop $\tau$ with every label replaced by its image under $\sigma$: same shape, same length.*

> [!remark]- Connections
> - Conjugation in general: [[§18 Conjugation, Products, and Pointwise Products#^def-18-2|Conjugation; Conjugate Elements; Inner Automorphism]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|Conjugation Is an Automorphism]].
> - For a whole permutation in disjoint-cycle notation: [[§33 Conjugacy Classes#^lem-33-1|Conjugation Relabels the Entries, §33.1]].
> - The converse (same cycle type ⇒ conjugate): [[§33 Conjugacy Classes#^thm-33-3|Conjugacy Classes in Sₙ Are Cycle Types]].

> [!theorem] Proposition §12.2: Every Permutation Is a Product of Transpositions
> Every $r$-cycle is a product of $r - 1$ transpositions,
>
> $$ (a_1\ a_2\ \cdots\ a_r) = (a_1\ a_r)(a_1\ a_{r-1}) \cdots (a_1\ a_2), $$
>
> and consequently every permutation in $S_n$ is a product of transpositions.
>
> *Source: cf. Pinter Ch. 8*

^prop-12-2

> [!proof]+ Proof
> Track each element through the product, rightmost factor first. $a_1$: the rightmost factor sends it to $a_2$, which all remaining factors fix. $a_i$ for $2 \leq i < r$: it is fixed by each factor until $(a_1\ a_i)$ sends it to $a_1$, which the next factor $(a_1\ a_{i+1})$ sends to $a_{i+1}$, fixed thereafter. $a_r$: fixed until the last factor $(a_1\ a_r)$ sends it to $a_1$. Elements outside $\{a_i\}$ are fixed throughout. So the product is $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_r \mapsto a_1$. By the [[§11 Disjoint Cycle Decomposition#^thm-11-3|Disjoint Cycle Decomposition]] every permutation is a product of cycles, hence of transpositions (the identity being the empty product).

^pf-12-2

*Uses:* [[§10 Cycle Notation and the Group S₃#^def-10-1|Def. §10.1]], [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]]

> [!remark]- Connections
> - Sharper generating sets: [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|Generators of Sₙ]] (PS 1.5(3)); the parity of the number of factors: [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|Parity of a Permutation]].
> - Used in Quantum Mechanics: with [[§12 Multiplying and Conjugating Cycles#^prop-12-1|Proposition §12.1]], in the proof that a permutation can act on a physical state of identical particles only as $+1$ or as its sign — [[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^thm-c12-1-5|QM Theorem §C12.1.5]].

> [!remark] Remark: Cycles Need Not Be Disjoint
> Uniqueness in the [[§11 Disjoint Cycle Decomposition#^thm-11-3|decomposition theorem]] depends on disjointness. With overlapping cycles the same permutation has many expressions — e.g. $(1\,2)(2\,3) = (1\,2\,3)$ — and factorizations into transpositions are far from unique; only the *parity* of the number of transpositions is an invariant of the permutation, as proved in [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|§21.4]] (Parity of a Permutation).

^rem-12-1

> [!remark] Remark: Finite Sets Only
> The [[§11 Disjoint Cycle Decomposition#^thm-11-3|theorem]] is about $S_n$, i.e. finite sets. For an infinite set $X$, a bijection can have infinite orbits with no return — the shift $n \mapsto n + 1$ on $\mathbb{Z}$ is a single “infinite cycle” — so finite cycle notation does not describe all of $S_X$. Throughout this course, $S_n$ is finite.

^rem-12-2
