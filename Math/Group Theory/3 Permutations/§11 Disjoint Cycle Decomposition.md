---
type: section
subject: "[[Group Theory]]"
chapter: 3
section: 11
tags: [group-theory, math493]
---
← [[§10 Cycle Notation and the Group S₃]] · ↑ [[· 3 Permutations]] · [[§12 Multiplying and Conjugating Cycles]] →

*Reference: Pinter Ch. 8.*

> [!definition] Definition §11.1: Disjoint Cycles
> Two cycles $(a_1\ \cdots\ a_r)$ and $(b_1\ \cdots\ b_s)$ are **disjoint** if they move no common element: $\{a_i\} \cap \{b_j\} = \varnothing$. More generally, a family of cycles is disjoint if no element of $\{1, \ldots, n\}$ appears in two of them.

^def-11-1

> [!theorem] Lemma §11.1: An $r$-Cycle Has Order $r$
> An $r$-cycle $c = (a_1\ \cdots\ a_r)$ has order $r$.

^lem-11-1

> [!proof]+ Proof
> By induction on $m \geq 0$, $c^m$ sends $a_i \mapsto a_{i+m}$ (indices modulo $r$) and fixes every element outside $\{a_1, \ldots, a_r\}$: the case $m = 0$ is trivial, and applying $c$ once more advances each index by $1$. So for $0 < m < r$, $c^m(a_1) = a_{1+m} \neq a_1$ and $c^m \neq e$; while $c^r$ sends each $a_i$ to $a_{i+r} = a_i$ and fixes everything else, so $c^r = e$. Hence the least positive $m$ with $c^m = e$ is $r$.

^pf-11-1

*Uses:* [[§10 Cycle Notation and the Group S₃#^def-10-1|Def. §10.1]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!theorem] Lemma §11.2: Disjoint Cycles Commute
> If $c$ and $d$ are disjoint cycles, then $cd = dc$.

^lem-11-2

> [!proof]+ Proof
> Let $x \in \{1, \ldots, n\}$. If $x$ is moved by $c$, then $x$ and $c(x)$ are both fixed by $d$ (they lie in $c$'s loop, which $d$ does not touch), so $cd(x) = c(x) = dc(x)$. Symmetrically if $x$ is moved by $d$. If neither moves $x$, both sides give $x$.

^pf-11-2

*Uses:* [[§11 Disjoint Cycle Decomposition#^def-11-1|Def. §11.1]], [[§10 Cycle Notation and the Group S₃#^def-10-1|Def. §10.1]]

> [!theorem] Theorem §11.3: Disjoint Cycle Decomposition
> Every $\sigma \in S_n$ is a product of disjoint cycles. The decomposition is unique up to the order of the factors and the choice of starting point within each cycle (with fixed points either omitted or written as $1$-cycles).
>
> *Source: cf. Pinter Ch. 8, Thm. 1*

^thm-11-3

> [!proof]+ Proof
> **Existence.** Pick $a \in \{1, \ldots, n\}$ and follow the arrows $a,\ \sigma(a),\ \sigma^2(a),\ \ldots$. Since there are only $n$ values, some repetition $\sigma^i(a) = \sigma^j(a)$ with $i < j$ occurs; applying $\sigma^{-i}$ (i.e. cancelling, since $\sigma$ is injective) gives $\sigma^{j-i}(a) = a$. Let $r$ be the least positive integer with $\sigma^r(a) = a$; then $a, \sigma(a), \ldots, \sigma^{r-1}(a)$ are distinct (a repetition among them would give a smaller return time), and $\sigma$ acts on this set as the cycle $c_1 = (a\ \sigma(a)\ \cdots\ \sigma^{r-1}(a))$. Now choose any $b$ not in this set and repeat, obtaining $c_2$. The loops of $c_1$ and $c_2$ are disjoint: if they shared an element, following arrows forward from it would trace the same loop, since each element has exactly one outgoing arrow. Continue until every element is accounted for; then $\sigma = c_1 c_2 \cdots c_k$, because on each loop $\sigma$ agrees with the corresponding $c_i$ and the other $c_j$ act trivially there.
>
> **Uniqueness.** The loops are determined by $\sigma$ alone: the loop through $a$ is the set $\{\sigma^i(a)\}$, and the cyclic order on it is dictated by $\sigma$. So any disjoint-cycle expression for $\sigma$ must consist of exactly these loops, each written starting somewhere; and since [[§11 Disjoint Cycle Decomposition#^lem-11-2|disjoint cycles commute]], the order of the factors is immaterial.

^pf-11-3

*Uses:* [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§10 Cycle Notation and the Group S₃#^def-10-1|Def. §10.1]], [[§11 Disjoint Cycle Decomposition#^def-11-1|Def. §11.1]], [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]], [[§4 Subgroups#^lem-4-4|§4.4]]

> [!remark]- Connections
> - The multiset of cycle lengths is the [[§31 Conjugacy Classes#^def-31-2|Cycle Type]], which classifies conjugacy: [[§31 Conjugacy Classes#^thm-31-3|Conjugacy Classes in Sₙ Are Cycle Types]].
> - The loops are the orbits of $\langle \sigma \rangle$ acting on $\{1, \ldots, n\}$: [[§25 Orbits#^def-25-1|Orbit]].

> [!example] Example §11.1: Decomposing a Permutation in $S_7$
> Let $\sigma \in S_7$ be given by $1\mapsto5,\ 2\mapsto2,\ 3\mapsto7,\ 4\mapsto1,\ 5\mapsto4,\ 6\mapsto3,\ 7\mapsto6$. Starting at $1$: $1 \to 5 \to 4 \to 1$, giving $(1\,5\,4)$. The smallest unvisited element is $2$, which is fixed. Next, $3 \to 7 \to 6 \to 3$, giving $(3\,7\,6)$. All seven elements are now accounted for:
>
> $$ \sigma = (1\,5\,4)(3\,7\,6), $$
>
> with $2$ fixed and omitted. Its inverse reverses each loop: $\sigma^{-1} = (1\,4\,5)(3\,6\,7)$. A single loop through all of $\{1,2,3,4\}$, such as $(2\,3\,1\,4)$, unrolls to $2\mapsto3,\ 3\mapsto1,\ 1\mapsto4,\ 4\mapsto2$; by convention it is written starting at its smallest entry, $(1\,4\,2\,3)$.

^ex-11-1

![[m493-11-1.svg]]
*$\sigma = (1\,5\,4)(3\,7\,6)$ in $S_7$, drawn by following arrows: two disjoint $3$-cycles (blue, red) and the fixed point $2$ (a $1$-cycle). Every element has exactly one arrow out and one in, which is why the loops cannot overlap; reversing all arrows gives $\sigma^{-1} = (1\,4\,5)(3\,6\,7)$.*

> [!theorem] Proposition §11.4: Computing with Disjoint Cycles
> Let $\sigma = c_1 c_2 \cdots c_k$ be a product of disjoint cycles of lengths $r_1, \ldots, r_k$.
> 1. $\sigma^{-1} = c_1^{-1} \cdots c_k^{-1}$, where the inverse of a cycle is the same loop traversed backwards: $(a_1\ a_2\ \cdots\ a_r)^{-1} = (a_r\ \cdots\ a_2\ a_1)$.
> 2. $\sigma^m = c_1^m c_2^m \cdots c_k^m$ for all $m \in \mathbb{Z}$.
> 3. The order of $\sigma$ is $\operatorname{lcm}(r_1, \ldots, r_k)$.

^prop-11-4

> [!proof]+ Proof
> (1) Since the $c_i$ commute, $(c_1 \cdots c_k)(c_1^{-1} \cdots c_k^{-1}) = e$ after pairing each $c_i$ with $c_i^{-1}$; the formula for a cycle's inverse is read off by reversing arrows. (2) Commuting factors can be regrouped: $(c_1 \cdots c_k)^m = c_1^m \cdots c_k^m$. (3) Since the $c_i^m$ act on disjoint sets, $\sigma^m = e$ iff each $c_i^m = e$, iff $r_i \mid m$ for every $i$, iff $\operatorname{lcm}(r_1, \ldots, r_k) \mid m$. The least such positive $m$ is the lcm.

^pf-11-4

*Uses:* [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§2 First Consequences of the Axioms#^cor-2-5|§2.5]]
