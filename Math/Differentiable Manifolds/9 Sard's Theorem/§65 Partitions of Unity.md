---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 9
section: 65
tags: [differentiable-manifolds, math591]
---
← [[§64 Parametric Transversality]] · ↑ [[· 9 Sard's Theorem]] · [[§66 The Whitney Embedding Theorem]] →

*Stage: analysis — Writing $1$ as a locally finite sum of smooth functions subordinate to any open cover: the tool for gluing local constructions into global ones.*

*Lecture 22. Partitions of unity: a key tool for constructing exhaustion functions and much else, for example for integrating forms. Lee develops them up front (Lee, Chapter 2); the course introduces them where they are first needed. In the lectures they came after the Whitney embedding theorem for compact manifolds (Lecture 21), together with its noncompact case (Lectures 22–23); these notes put them first, since the noncompact case uses them ([[§66 The Whitney Embedding Theorem|§66]]).*

> [!definition] Definition §65.1: Locally Finite Family
> Let $X$ be a topological space. A family $\{S_\alpha\}_{\alpha \in A}$ of subsets of $X$, over any index set $A$, is **locally finite** if every $p \in X$ has a neighbourhood $U$ that meets only finitely many of the sets: $\{ \alpha \in A : U \cap S_\alpha \neq \varnothing \}$ is finite.
>
> *(Lecture 22 stated the condition inside the definition of a partition of unity, and again in that of a paracompact space; stated once here.)*
>
> *Lee: Ch. 1, Paracompactness*

^def-65-1

> [!example] Example §65.1: Intervals Centred at the Integers
> *(Not from lecture.)* The intervals $S_n = (n - 1, n + 1)$, $n \in \mathbb{Z}$, form a locally finite family in $\mathbb{R}$, although there are infinitely many of them and they cover $\mathbb{R}$. For $p \in \mathbb{R}$ take the neighbourhood $U = (p - 1, p + 1)$. If $U \cap S_n \neq \varnothing$, some $x$ has $|x - p| < 1$ and $|x - n| < 1$, so $|n - p| < 2$; at most four integers $n$ satisfy this. So $U$ meets at most four of the $S_n$.

^ex-65-1

> [!example] Example §65.2: Nested Intervals
> *(Not from lecture.)* The intervals $S_n = (-n, n)$, $n \ge 1$, do not form a locally finite family in $\mathbb{R}$, and the condition of Definition [[§65 Partitions of Unity#^def-65-1|§65.1]] fails at every point. Let $p \in \mathbb{R}$ and $U$ any neighbourhood of $p$. For every integer $n > |p|$ we have $p \in S_n$, so $p \in U \cap S_n$; hence $U$ meets the infinitely many $S_n$ with $n > |p|$.

^ex-65-2

> [!example] Example §65.3: Intervals Accumulating at $0$
> *(Not from lecture.)* The intervals $S_n = \big(\tfrac{1}{n+1}, \tfrac{1}{n}\big)$, $n \ge 1$, satisfy the condition of Definition [[§65 Partitions of Unity#^def-65-1|§65.1]] at every $p \neq 0$ but not at $p = 0$; so the family is not locally finite, since the condition must hold at every point.
> - $p < 0$: the neighbourhood $(-\infty, 0)$ meets no $S_n$.
> - $p > 0$: the neighbourhood $U = (p/2, \infty)$ meets $S_n$ only if $\tfrac1n > \tfrac p2$, i.e. $n < \tfrac2p$; finitely many $n$.
> - $p = 0$: a neighbourhood $U$ of $0$ contains some $(-\varepsilon, \varepsilon)$, which contains $S_n$ for every $n$ with $\tfrac1n < \varepsilon$; infinitely many $n$.

^ex-65-3

> [!theorem] Lemma §65.1: Closures and Unions in a Locally Finite Family
> Let $\{S_i\}_{i \in I}$ be a locally finite family of subsets of a topological space $X$ (Definition [[§65 Partitions of Unity#^def-65-1|§65.1]]).
>
> 1. The closures $\{\overline{S_i}\}_{i \in I}$ also form a locally finite family.
> 2. $\overline{\bigcup_i S_i} = \bigcup_i \overline{S_i}$. In particular, if every $S_i$ is closed, then $\bigcup_i S_i$ is closed.
>
> *Lee: Lemma 1.13*

^lem-65-1

> [!proof]+ Proof
> *(Lee leaves the proof as an exercise, Exercise 1.14; the proof of Theorem 2.23 in the assigned reading uses both parts. Filled in.)* Neighbourhoods can be taken open: a neighbourhood meeting only finitely many $S_i$ contains an open neighbourhood with the same property.
>
> (1) Let $p \in X$, and let $W$ be an open neighbourhood of $p$ meeting only finitely many $S_i$. If $W$ meets $\overline{S_i}$, say at $x$, then $W$ is an open set containing the point $x$ of the closure of $S_i$, so $W$ meets $S_i$. Hence $\{ i : W \cap \overline{S_i} \neq \varnothing \} \subseteq \{ i : W \cap S_i \neq \varnothing \}$, a finite set.
>
> (2) *$\supseteq$.* For each $i$, $S_i \subseteq \bigcup_j S_j$, so $\overline{S_i} \subseteq \overline{\bigcup_j S_j}$. *$\subseteq$.* Let $p \notin \bigcup_i \overline{S_i}$; we show $p \notin \overline{\bigcup_i S_i}$. Take an open neighbourhood $W$ of $p$ meeting only $S_{i_1}, \ldots, S_{i_k}$. The set $C = \overline{S_{i_1}} \cup \cdots \cup \overline{S_{i_k}}$ is closed, as a finite union of closed sets, and $p \notin C$. So $W' = W \setminus C$ is an open neighbourhood of $p$. It misses $S_{i_1}, \ldots, S_{i_k}$ (they lie in $C$) and every other $S_i$ (which $W$ already misses), so $W' \cap \bigcup_i S_i = \varnothing$ and $p \notin \overline{\bigcup_i S_i}$. If every $S_i$ is closed, this reads $\overline{\bigcup_i S_i} = \bigcup_i S_i$.

^pf-65-1

> [!theorem] Lemma §65.2: Locally Finite Sums of Smooth Functions Are Smooth
> Let $\{f_\alpha\}_{\alpha \in A}$ be smooth functions on a smooth manifold $M$ whose supports $\{\operatorname{supp} f_\alpha\}_{\alpha \in A}$ form a locally finite family (Definition [[§65 Partitions of Unity#^def-65-1|§65.1]]). Then every $p \in M$ has an open neighbourhood on which all but finitely many $f_\alpha$ vanish identically; in particular the sum $f = \sum_{\alpha \in A} f_\alpha$ has only finitely many nonzero terms at each point, and $f$ is smooth on $M$.

^lem-65-2

> [!proof]+ Proof
> *(Not from lecture; the argument the proofs of Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]] and Proposition [[§65 Partitions of Unity#^prop-65-13|§65.13]] use.)* Let $p \in M$. By local finiteness $p$ has a neighbourhood meeting only finitely many supports; shrinking it, take it open, $U$, and let $F = \{ \alpha \in A : U \cap \operatorname{supp} f_\alpha \neq \varnothing \}$, a finite set. For $\alpha \notin F$, $U$ does not meet $\operatorname{supp} f_\alpha$, which contains $\{ f_\alpha \neq 0 \}$; so $f_\alpha = 0$ on $U$. Hence on $U$
>
> $$
> f = \sum_{\alpha \in F} f_\alpha ,
> $$
>
> a finite sum of smooth functions, so $f|_U$ is smooth. Every point of $M$ has an open neighbourhood on which $f$ is smooth, and smoothness is a local property; so $f$ is smooth on $M$.

^pf-65-2

*Uses:* [[§65 Partitions of Unity#^def-65-1|Def. §65.1]]

> [!example] Example §65.4: Pointwise Finiteness Is Not Enough
> *(Not from lecture.)* Lemma [[§65 Partitions of Unity#^lem-65-2|§65.2]] needs the supports to be locally finite; it is not enough that each point lies in only finitely many supports. On $M = \mathbb{R}$ let $a_n = \tfrac{1}{n+1}$, $b_n = \tfrac1n$ ($n \ge 1$), and let $f_n$ be the smooth function equal to $c_n\, e^{-1/((x - a_n)(b_n - x))}$ on $(a_n, b_n)$ and $0$ elsewhere, with $c_n > 0$ chosen so that $\max f_n = 1$, attained at the midpoint $m_n$ of $[a_n, b_n]$ (the exponent is largest there). Then $\operatorname{supp} f_n = [a_n, b_n]$.
> - *Pointwise finite.* A point lies in at most two of the supports (the endpoints $\tfrac1n$, $n \ge 2$, lie in two), and $0$ in none, so $f = \sum_n f_n$ is defined everywhere.
> - *Not continuous.* $f(m_n) = f_n(m_n) = 1$, since $m_n$ lies in no other support, and $m_n \to 0$; but $f(0) = 0$. So $f$ is not even continuous at $0$.
> - *Not locally finite.* The supports accumulate at $0$, as in Example [[§65 Partitions of Unity#^ex-65-3|§65.3]]: every neighbourhood of $0$ meets infinitely many of them.

^ex-65-4

> [!definition] Definition §65.2: Partition of Unity
> A **partition of unity** on $M$ is an indexed family $\{\chi_\alpha\}_{\alpha \in A}$ of smooth functions on $M$, over an arbitrary index set $A$ (possibly uncountable), such that
>
> 1. $0 \le \chi_\alpha \le 1$ for every $\alpha$;
> 2. the family of supports $\{\operatorname{supp}\chi_\alpha\}_{\alpha \in A}$ is locally finite (Definition [[§65 Partitions of Unity#^def-65-1|§65.1]]): every $p \in M$ has a neighbourhood $U$ for which $\{ \alpha \in A : U \cap \operatorname{supp}\chi_\alpha \neq \varnothing \}$ is finite;
> 3. $\sum_{\alpha \in A} \chi_\alpha(p) = 1$ for every $p \in M$.
>
> By (2) the sum in (3) has only finitely many nonzero terms at each point. The partition is **subordinate** to an open cover $\{U_\alpha\}_{\alpha \in A}$ if $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$ for every $\alpha$.
>
> *Lee: Ch. 2, Partitions of Unity*

^def-65-2

The name: the number one is written as a sum of smooth functions. Partitions of unity allow one to localize; the bump functions so far, and the cutoff functions in the proof of the Whitney embedding theorem ([[§66 The Whitney Embedding Theorem|§66]]), are made of the same material.

![[m591-66-2.svg]]

The simplest example, on $M = \mathbb{R}$: a function $\chi_1$ that is $1$ far to the left and $0$ far to the right, and $\chi_2 = 1 - \chi_1$.

The main result of this section is that every open cover has a subordinate partition of unity (Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]] below). Its proof has two steps of different kinds: an analysis step in $\mathbb{R}^m$ (Lemma [[§65 Partitions of Unity#^lem-65-3|§65.3]]), and genuine point-set topology on $M$ (paracompactness, Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]]). The ingredients come first.

> [!theorem] Lemma §65.3: Plateau Functions
> For all $\varepsilon > \delta > 0$ there is $\rho \in C^\infty(\mathbb{R})$ with $0 \le \rho \le 1$, $\rho \equiv 1$ on $[-\delta, \delta]$ and $\operatorname{supp}\rho \subseteq (-\varepsilon, \varepsilon)$. Then $f(x) = \rho(|x|)$ is smooth on $\mathbb{R}^m$, $f \equiv 1$ on the closed ball $\overline{B}_\delta$, and $\operatorname{supp} f \subseteq B_\varepsilon = \{ x \in \mathbb{R}^m : |x| < \varepsilon \}$.
>
> *Lee: Lemmas 2.20–2.22*

^lem-65-3

> [!proof]+ Proof
> *(Not proved in Lecture 22, which described the method: start from the function equal to $e^{-1/x}$ for $x$ positive and zero for $x$ negative, then reflect, divide and add; not complicated, only a routine check. This is step 2 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]].)* With $h$ as there and $\delta < r' < \varepsilon$, take $\rho(t) = h(r'^2 - t^2)\big/\big(h(r'^2 - t^2) + h(t^2 - \delta^2)\big)$: smooth, between $0$ and $1$, equal to $1$ for $|t| \le \delta$ and $0$ for $|t| \ge r'$, so $\operatorname{supp}\rho \subseteq [-r', r'] \subseteq (-\varepsilon, \varepsilon)$. Then $f(x) = \rho(|x|)$ is the function $H$ of that proof (with $r = \delta$), smooth on $\mathbb{R}^m$ — $|x|$ is not smooth at the origin, but $\rho$ is constant equal to one near $0$, so $f$ is constant near $x = 0$ — with $f \equiv 1$ on $\overline{B}_\delta$ and $\operatorname{supp} f = \overline{B}_{r'} \subseteq B_\varepsilon$.

^pf-65-3

*Uses:* [[§56 Vector Fields#^prop-56-4|§56.4]]

![[m591-66-3.svg]]

*The topology.* The second step needs some point-set topology, which pays for the use of partitions of unity before their construction.

> [!definition] Definition §65.3: Refinement of a Cover
> Let $\{U_\alpha\}_{\alpha \in A}$ be a cover of a topological space $X$. A cover $\{V_i\}_{i \in I}$ of $X$ is a **refinement** of $\{U_\alpha\}$ if every $V_i$ lies in some $U_\alpha$: for each $i$ there is $\alpha(i) \in A$ with $V_i \subseteq U_{\alpha(i)}$. It is an **open refinement** if every $V_i$ is open. A subcover is the special case in which every $V_i$ is one of the $U_\alpha$.
>
> *(Lecture 22 stated the condition inside the definition of a paracompact space; stated once here.)*
>
> *Lee: Ch. 1, Paracompactness*

^def-65-3

> [!example] Example §65.5: A Locally Finite Refinement That Is Not a Subcover
> *(Not from lecture.)* On $\mathbb{R}$, the open cover $\{(-n, n)\}_{n \ge 1}$ is not locally finite (Example [[§65 Partitions of Unity#^ex-65-2|§65.2]]). The intervals $V_k = (k - 1, k + 1)$, $k \in \mathbb{Z}$, form a locally finite open refinement of it (Definition [[§65 Partitions of Unity#^def-65-3|§65.3]]):
> - *A cover.* Every $x \in \mathbb{R}$ lies in $V_k$ for $k = \lfloor x \rfloor$, since $k \le x < k + 1$.
> - *A refinement.* If $|x - k| < 1$ then $|x| < |k| + 1$, so $V_k \subseteq (-n, n)$ with $n = |k| + 1$.
> - *Locally finite.* This is Example [[§65 Partitions of Unity#^ex-65-1|§65.1]].
>
> It is not a subcover: $V_1 = (0, 2)$ is not one of the intervals $(-n, n)$. Refining, not only passing to a subcover, is needed here: a subcover of $\{(-n, n)\}$ must contain infinitely many of the intervals (finitely many have bounded union), and all of them contain $0$, so no subcover is locally finite at $0$.

^ex-65-5

> [!definition] Definition §65.4: Paracompact Space
> A space $X$ is **paracompact** if every open cover $\{U_\alpha\}_{\alpha \in A}$ has an open refinement $\{V_i\}_{i \in \mathbb{N}}$ (Definition [[§65 Partitions of Unity#^def-65-3|§65.3]]) that covers and is locally finite (Definition [[§65 Partitions of Unity#^def-65-1|§65.1]]):
>
> 1. $X = \bigcup_i V_i$, and for every $i$ there is $\alpha(i)$ with $V_i \subseteq U_{\alpha(i)}$;
> 2. every $p \in X$ has a neighbourhood $W$ such that $\{ i : W \cap V_i \neq \varnothing \}$ is finite.
>
> *Lee: Ch. 1, Paracompactness*

^def-65-4

Compactness gives a finite subcover; paracompactness gives a locally finite refinement, which need not be a subcover. (The usual definition allows refinements indexed by any set; with the countable index set of the lecture it is what holds for manifolds, Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]] below.)

> [!theorem] Lemma §65.4: Exhaustion by Compact Sets
> A second-countable, locally compact Hausdorff space $X$ is the union of compact sets $K_1 \subseteq K_2 \subseteq \cdots$ with $K_j \subseteq \operatorname{Int}K_{j+1}$ for every $j$.
>
> *Lee: Proposition A.60*

^lem-65-4

> [!proof]+ Proof
> *(Not from lecture; filled in, following Lee.)* *A countable basis of precompact sets.* Let $\mathcal{B}$ be a countable basis, and $\mathcal{B}'$ the set of $B \in \mathcal{B}$ with compact closure. $\mathcal{B}'$ is still a basis: if $x \in W$ open, local compactness gives an open $V \ni x$ with $\overline V$ compact, and some $B \in \mathcal{B}$ has $x \in B \subseteq V \cap W$; then $\overline B$ is a closed subset of the compact $\overline V$ (closures computed in the Hausdorff space $X$), so compact. Enumerate $\mathcal{B}' = \{B_1, B_2, \ldots\}$ (if it is finite, $X$ is compact and $K_j = X$ works).
> *The exhaustion.* Put $K_1 = \overline{B_1}$. Given $K_j$ compact, it is covered by the $B_i$, hence by $B_1, \ldots, B_n$ for some $n$; take the least such $n$ with $n \ge j + 1$, and $K_{j+1} = \overline{B_1} \cup \cdots \cup \overline{B_n}$, compact as a finite union of compact sets. Then $K_j \subseteq B_1 \cup \cdots \cup B_n \subseteq \operatorname{Int}K_{j+1}$, and $B_j \subseteq K_j$ for all $j$, so $\bigcup_j K_j = X$.

^pf-65-4

> [!theorem] Theorem §65.5: Manifolds Are Paracompact
> Let $M$ be a topological manifold, $\{U_\alpha\}$ an open cover, and $\mathcal{B}$ any basis of the topology of $M$. Then $\{U_\alpha\}$ has a countable, locally finite open refinement that covers $M$ and consists of elements of $\mathcal{B}$. In particular $M$ is paracompact. More generally, every second-countable, locally compact Hausdorff space is paracompact, by the same proof.
>
> *Lee: Theorem 1.15*

^thm-65-5

> [!proof]+ Proof
> *(Stated in Lecture 22, with the proof left to Lee; filled in, following Lee.)* $M$ is Hausdorff, second countable (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]) and locally compact (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]); let $K_1 \subseteq K_2 \subseteq \cdots$ be as in Lemma [[§65 Partitions of Unity#^lem-65-4|§65.4]], and $K_0 = K_{-1} = \varnothing$. For $j \ge 0$ put
>
> $$
> A_j = K_{j+1} \setminus \operatorname{Int}K_j \ \ \text{(compact)}, \qquad W_j = \operatorname{Int}K_{j+2} \setminus K_{j-1} \ \ \text{(open)}, \qquad A_j \subseteq W_j .
> $$
>
> For each $x \in A_j$ choose $\alpha$ with $x \in U_\alpha$, and $B_x \in \mathcal{B}$ with $x \in B_x \subseteq U_\alpha \cap W_j$. Finitely many $B_x$ cover the compact set $A_j$. The union over $j$ of these finite families is a countable family of elements of $\mathcal{B}$; it covers $M$, because the $A_j$ do (each point lies in some $K_{j+1} \setminus \operatorname{Int}K_j$); and it refines $\{U_\alpha\}$. *Locally finite:* the sets chosen for $j$ lie in $W_j$, and $W_j \cap W_k = \varnothing$ when $|j - k| \ge 3$; a point of $A_j$ has the neighbourhood $W_j$, which meets only the sets chosen for $j - 2, \ldots, j + 2$, finitely many.

^pf-65-5

*Uses:* [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[§65 Partitions of Unity#^lem-65-4|§65.4]]

![[m591-66-1.svg]]

*(Not from lecture; figure added.)* The proof of Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]] for $j = 2$. The compact ring $A_2 = K_3 \setminus \operatorname{Int}K_2$ (teal) is covered by finitely many basis sets $B_x$ (blue), each inside some $U_\alpha$ and inside the open ring $W_2 = \operatorname{Int}K_4 \setminus K_1$ (between the dashed circles). Rings $W_j$ and $W_k$ with $|j - k| \ge 3$ are disjoint, so a point of $A_j$ has the neighbourhood $W_j$, which meets only the sets chosen for $j - 2, \ldots, j + 2$: the refinement is locally finite.

> [!remark] Remark: Is Local Compactness Needed?
> The board stated the theorem as “if $X$ is $T_2$ and second countable, then it is paracompact”, leaving open whether local compactness is needed. The email of Oct 26 settled it: local compactness is needed; Hausdorff, second countable and locally compact imply paracompact, and Lee proves directly what is needed for manifolds in Theorem 1.15 (p. 9). So the theorem is stated with local compactness, as above. *(Filled in.)* Some hypothesis beyond Hausdorff and second countable is needed: the $K$-topology on $\mathbb{R}$ is Hausdorff and second countable but not paracompact (Example [[§65 Partitions of Unity#^ex-65-6|§65.6]] below). Local compactness, as above, suffices; so does regularity. For manifolds nothing changes: they are locally compact. Second countability is essential here; it was used once before, for countable subcovers in measure zero (Lemma [[§62 Sets of Measure Zero#^lem-62-3|§62.3]]).

^rem-65-1

> [!example] Example §65.6: The K-Topology on the Real Line
> *(Filled in; not from lecture.)* Let $K = \{1/n : n \ge 1\}$. The *$K$-topology* on $\mathbb{R}$ is generated by the open intervals $(a, b)$ and the sets $(a, b) \setminus K$. It is Hausdorff and second countable but not regular (Munkres, §31), so not paracompact.
>
> *Basis.* The open intervals and the sets $(a, b) \setminus K$ cover $\mathbb{R}$, and the intersection of two of them is empty or again of one of the two forms, since $\big((a, b) \setminus K\big) \cap (c, d) = \big((a, b) \cap (c, d)\big) \setminus K$. So they form a basis, and the open sets are their unions.
>
> *Hausdorff.* Every open interval is open, so the $K$-topology is finer than the standard one; two distinct points have disjoint open intervals around them.
>
> *Second countable.* The intervals $(p, q)$ and the sets $(p, q) \setminus K$ with $p < q$ rational form a countable family. It is a basis: if $x$ lies in a basic set $(a, b)$, respectively $(a, b) \setminus K$, choose rationals $p, q$ with $a \le p < x < q \le b$; then $x \in (p, q) \subseteq (a, b)$, respectively $x \in (p, q) \setminus K \subseteq (a, b) \setminus K$.
>
> *Not regular.* $K$ is closed: $K \cup \{0\}$ is closed in the standard topology, so $\mathbb{R} \setminus (K \cup \{0\})$ is open, and $\mathbb{R} \setminus K$ is its union with the basic set $(-1, 1) \setminus K$. Suppose $U \ni 0$ and $V \supseteq K$ are disjoint open sets. $U$ contains a basic set $B \ni 0$. $B$ is not an interval: an interval around $0$ contains some $1/n \in K \subseteq V$, while $B \subseteq U$ and $U \cap V = \varnothing$. So $B = (a, b) \setminus K$ with $a < 0 < b$. Choose $n$ with $1/n < b$. $V$ contains a basic set $C \ni 1/n$, which is an interval $(c, d)$, since the sets $(c, d) \setminus K$ do not contain $1/n$; replacing it by $(\max(c, 0), \min(d, b))$, which still contains $1/n$, we may assume $(c, d) \subseteq (0, b)$. The interval $(c, d)$ is uncountable and $K$ is countable, so there is $z \in (c, d) \setminus K$. Then $z \in (a, b) \setminus K = B \subseteq U$ and $z \in (c, d) \subseteq V$, contradicting $U \cap V = \varnothing$. So the point $0$ and the closed set $K$ cannot be separated by open sets.
>
> *Not paracompact.* A paracompact Hausdorff space is normal, in particular regular (Munkres, Theorem 41.1). Munkres's paracompactness asks only for a locally finite open refinement, not a countable one, so it follows from Definition [[§65 Partitions of Unity#^def-65-4|§65.4]]. As the $K$-topology is Hausdorff but not regular, it is not paracompact.

^ex-65-6

> [!definition] Definition §65.5: Regular Coordinate Ball
> An open set $B \subseteq M$ is a **regular coordinate ball** if there are a chart $(U, \varphi)$ with $B \subseteq U$ and numbers $0 < \delta < \varepsilon$ such that $\varphi(B) = B_\delta(0)$, the $\delta$-ball centred at $0$, and $B_\varepsilon(0) \subseteq \varphi(U)$ — an $\varepsilon$-ball centred at $0$ containing $\varphi(B)$, with room to spare. The room is needed to pull back the plateau function of Lemma [[§65 Partitions of Unity#^lem-65-3|§65.3]], equal to $1$ on $\overline{B}_\delta$ and supported in $B_\varepsilon$.
>
> *Lee: Ch. 1, Regular Coordinate Balls*

^def-65-5

![[m591-66-4.svg]]

*(Figure redrawn with the manifold side.)* Definition [[§65 Partitions of Unity#^def-65-5|§65.5]] in pictures. Left, in $M$: the chart domain $U$, the regular coordinate ball $B$ around $p = \varphi^{-1}(0)$, and the larger set $\varphi^{-1}(B_\varepsilon(0))$, which still lies in $U$. Right, their images under $\varphi$: the open set $\varphi(U) \subseteq \mathbb{R}^m$, the $\varepsilon$-ball inside it, and $\varphi(B) = B_\delta(0)$. The room between the two balls is where the plateau function of Lemma [[§65 Partitions of Unity#^lem-65-3|§65.3]] climbs from $1$ to $0$.

> [!theorem] Lemma §65.6: Regular Coordinate Balls Form a Basis
> Let $\{U_\alpha\}$ be an open cover of $M$. The regular coordinate balls $B$ whose chart $(U, \varphi)$ can be chosen with $U$ inside some $U_\alpha$ form a basis of the topology of $M$.

^lem-65-6

> [!proof]+ Proof
> *(Filled in.)* Let $W$ be open and $x \in W$, say $x \in U_\alpha$. Take a chart $(V, \psi)$ at $x$, restrict it to $U = V \cap W \cap U_\alpha$, and translate so that $\varphi = \psi|_U - \psi(x)$ sends $x$ to $0$. $\varphi(U)$ is open, so it contains some $B_\varepsilon(0)$; for $0 < \delta < \varepsilon$, $B = \varphi^{-1}(B_\delta(0))$ is a regular coordinate ball with $x \in B \subseteq U \subseteq W$, and its chart domain $U$ lies in $U_\alpha$.

^pf-65-6

> [!theorem] Theorem §65.7: Existence of Partitions of Unity
> If $\{U_\alpha\}_{\alpha \in A}$ is any open cover of $M$, there is a partition of unity $\{\chi_\alpha\}_{\alpha \in A}$ subordinate to it.
>
> *Lee: Theorem 2.23*

^thm-65-7

> [!proof]+ Proof (Lee's proof of Theorem 2.23)
> *(The assigned reading, email of Oct 26: Lee, Chapter 2, from Lemma 2.20 to the beginning of the section on applications of partitions of unity, p. 44; for paracompactness, Theorem 1.15, p. 9. Lecture 22 began the proof; its first version is compared in the remark after this proof.)* Let $\{U_\alpha\}_{\alpha \in A}$ be an open cover of $M$.
>
> *Step 1: a locally finite cover by regular coordinate balls.* By Lemma [[§65 Partitions of Unity#^lem-65-6|§65.6]], the regular coordinate balls whose chart domain lies in some $U_\alpha$ form a basis $\mathcal{B}$ of the topology of $M$. By Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]], applied with this basis, $\{U_\alpha\}$ has a countable, locally finite open refinement $\{B_i\}_{i \ge 1}$ covering $M$ with every $B_i \in \mathcal{B}$. So for each $i$ there are a chart $(U_i, \varphi_i)$ and numbers $0 < \delta_i < \varepsilon_i$ with
>
> $$
> \varphi_i(B_i) = B_{\delta_i}(0), \qquad B_{\varepsilon_i}(0) \subseteq \varphi_i(U_i), \qquad U_i \subseteq U_{\alpha(i)} \ \text{ for some } \alpha(i) \in A
> $$
>
> (Definition [[§65 Partitions of Unity#^def-65-5|§65.5]]). By Lemma [[§65 Partitions of Unity#^lem-65-1|§65.1]](1), the closures $\{\overline{B_i}\}$ also form a locally finite family.
>
> *Step 2: a function positive exactly on $B_i$.* With $h(t) = e^{-1/t}$ for $t > 0$ and $h(t) = 0$ for $t \le 0$ (step 1 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]]), define
>
> $$
> f_i = h\big(\delta_i^2 - |\varphi_i|^2\big) \ \text{ on } U_i, \qquad f_i = 0 \ \text{ on } M \setminus \overline{B_i} .
> $$
>
> *Well defined.* The set $K_i = \varphi_i^{-1}\big(\overline{B}_{\delta_i}(0)\big)$ is compact, because $\overline{B}_{\delta_i}(0) \subseteq B_{\varepsilon_i}(0) \subseteq \varphi_i(U_i)$ is compact and $\varphi_i^{-1}$ is continuous; so $K_i$ is closed in $M$ (Hausdorff). It contains $B_i$ and lies in the closure of $B_i$ (every point of $\overline{B}_{\delta_i}(0)$ is a limit of points of $B_{\delta_i}(0)$), so $K_i = \overline{B_i}$. On the overlap $U_i \setminus \overline{B_i}$ of the two formulas, $|\varphi_i| > \delta_i$, so $h(\delta_i^2 - |\varphi_i|^2) = 0$: the two formulas agree. *Smooth.* $f_i$ is smooth on the open set $U_i$ (a composition of smooth maps) and zero on the open set $M \setminus \overline{B_i}$, and these two open sets cover $M$. *Support.* $f_i > 0$ exactly on $B_i$, so $\operatorname{supp} f_i = \overline{B_i} \subseteq U_i \subseteq U_{\alpha(i)}$.
>
> *Step 3: normalize.* The supports $\operatorname{supp} f_i = \overline{B_i}$ form a locally finite family (Step 1), so $f = \sum_i f_i$ is smooth by Lemma [[§65 Partitions of Unity#^lem-65-2|§65.2]]. Each $f_i \ge 0$, and every $p$ lies in some $B_i$, where $f_i(p) > 0$; so $f > 0$ on $M$. Hence $g_i = f_i / f$ is smooth, $0 \le g_i \le 1$, $\operatorname{supp} g_i = \overline{B_i}$, and $\sum_i g_i = f / f = 1$.
>
> *Step 4: re-index by $A$.* For $\alpha \in A$ put
>
> $$
> \chi_\alpha = \sum_{i \,:\, \alpha(i) = \alpha} g_i ,
> $$
>
> the zero function if no $i$ has $\alpha(i) = \alpha$. The family $\{\operatorname{supp} g_i\} = \{\overline{B_i}\}$ is locally finite, so each $\chi_\alpha$ is smooth (Lemma [[§65 Partitions of Unity#^lem-65-2|§65.2]]); $0 \le \chi_\alpha \le \sum_i g_i = 1$; and $\sum_\alpha \chi_\alpha = \sum_i g_i = 1$, since each $i$ has exactly one $\alpha(i)$. *Subordinate.* $\{\chi_\alpha \neq 0\} \subseteq \bigcup_{\alpha(i) = \alpha} B_i$, and by Lemma [[§65 Partitions of Unity#^lem-65-1|§65.1]](2) (the subfamily $\{B_i\}_{\alpha(i) = \alpha}$ is still locally finite)
>
> $$
> \operatorname{supp}\chi_\alpha \subseteq \overline{\bigcup_{\alpha(i) = \alpha} B_i} = \bigcup_{\alpha(i) = \alpha} \overline{B_i} \subseteq \bigcup_{\alpha(i) = \alpha} U_i \subseteq U_\alpha .
> $$
>
> *Locally finite.* If an open set $W$ meets only finitely many $\overline{B_i}$, it meets $\operatorname{supp}\chi_\alpha$ only for the finitely many $\alpha = \alpha(i)$ of those $i$. So $\{\chi_\alpha\}_{\alpha \in A}$ is a partition of unity subordinate to $\{U_\alpha\}$ (Definition [[§65 Partitions of Unity#^def-65-2|§65.2]]).

^pf-65-7

*Uses:* [[§65 Partitions of Unity#^lem-65-6|§65.6]], [[§65 Partitions of Unity#^thm-65-5|§65.5]], [[§65 Partitions of Unity#^def-65-5|Def. §65.5]], [[§65 Partitions of Unity#^lem-65-1|§65.1]], [[§56 Vector Fields#^prop-56-4|§56.4]], [[§65 Partitions of Unity#^lem-65-2|§65.2]], [[§65 Partitions of Unity#^def-65-2|Def. §65.2]]

> [!remark] Remark: Lecture 22's First Version of the Construction
> Lecture 22 built the functions differently: pull back the plateau function of Lemma [[§65 Partitions of Unity#^lem-65-3|§65.3]] (with $\delta_i < \varepsilon_i$) by $\varphi_i$ and extend by zero, as in step 3 of the proof of Proposition [[§56 Vector Fields#^prop-56-4|§56.4]], which gives smooth $f_i$ with
>
> $$
> f_i|_{B_i} \equiv 1, \qquad \operatorname{supp} f_i \subseteq U_i \subseteq U_{\alpha(i)} ,
> $$
>
> so that $\sum_j f_j \ge 1$ everywhere; then $g_i = f_i / \sum_j f_j$ and $\chi_\alpha = \sum_{\alpha(i) = \alpha} g_i$, as in Steps 3 and 4. One point needs care in that version: local finiteness of $\{B_i\}$ does not by itself make $\{\operatorname{supp} f_i\}$ locally finite, since $\operatorname{supp} f_i$ then sits in the larger ball $\varphi_i^{-1}(B_{\varepsilon_i}(0))$, not in $\overline{B_i}$. Lee's choice in Step 2, $f_i$ positive exactly on $B_i$ and supported in $\overline{B_i}$, avoids this; $f_i$ is then no longer $\equiv 1$ on $B_i$, only positive there, which is all the division needs.

^rem-65-2

**Transcription note (Lecture 22).** Page 58 of the handwritten notes states the theorem “if $X$ is $T_2$ and 2nd countable, then it is paracompact (need locally compact?)”; as stated it is false in general, and local compactness, which manifolds have, is the missing hypothesis (the remark *Is Local Compactness Needed?* after Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]]).

> [!theorem] Proposition §65.8: Bump Functions for Closed Sets
> Let $A \subseteq M$ be closed and $U \subseteq M$ open with $A \subseteq U$. Then there is a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $A$ and $\operatorname{supp}\psi \subseteq U$.
>
> *Lee: Proposition 2.25*

^prop-65-8

> [!proof]+ Proof
> *(Lee's proof. Not part of the assigned reading, which stops before the applications of partitions of unity; Lee's proof of the Whitney embedding theorem, Theorem [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], uses it.)* Put $U_0 = U$ and $U_1 = M \setminus A$. Both are open ($A$ is closed), and they cover $M$, since a point not in $U$ is not in $A \subseteq U$. By Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]] there is a partition of unity $\{\chi_0, \chi_1\}$ subordinate to $\{U_0, U_1\}$. Let $\psi = \chi_0$. It is smooth, $0 \le \psi \le 1$, and $\operatorname{supp}\psi \subseteq U_0 = U$. For $p \in A$: $\operatorname{supp}\chi_1 \subseteq M \setminus A$, so $\chi_1(p) = 0$, and $\psi(p) = \chi_0(p) + \chi_1(p) = 1$.

^pf-65-8

*Uses:* [[§66 The Whitney Embedding Theorem#^thm-66-11|§66.11]], [[§65 Partitions of Unity#^thm-65-7|§65.7]]

## Application: Extending Functions and Vector Fields from a Submanifold

*(Assignment 7, Problem 1, and what its proof gives.)* The standard use of a partition of unity: build an object locally, in charts, and glue the local pieces. Here the local pieces come from adapted charts (Lemmas [[§37 Regular Submanifolds#^lem-37-8|§37.8]] and [[§59 Related Vector Fields#^lem-59-7|§59.7]]), and the gluing is the next lemma.

> [!theorem] Lemma §65.9: Gluing Vector Fields with a Partition of Unity
> Let $\{U_\alpha\}_{\alpha \in A}$ be an open cover of $M$, $\mathbf{Y}_\alpha \in \mathfrak{X}(U_\alpha)$ for each $\alpha \in A$, and $\{\chi_\alpha\}_{\alpha \in A}$ a partition of unity subordinate to the cover (Definition [[§65 Partitions of Unity#^def-65-2|§65.2]]). Then:
>
> 1. each field $\chi_\alpha \mathbf{Y}_\alpha$, extended by $0$ outside $U_\alpha$, is a smooth vector field on $M$;
> 2. $\widetilde{\mathbf{X}} = \sum_{\alpha \in A} \chi_\alpha \mathbf{Y}_\alpha$ is a well-defined smooth vector field on $M$;
> 3. if $p \in M$ and $v \in T_pM$ satisfy $(\mathbf{Y}_\alpha)_p = v$ for every $\alpha$ with $p \in U_\alpha$, then $\widetilde{\mathbf{X}}_p = v$.

^lem-65-9

> [!proof]+ Proof
> *(Assignment 7, Problem 1: the submitted solution, the steps “Gluing” and “$\widetilde X$ extends $X$”.)* *(1)* The field $\chi_\alpha \mathbf{Y}_\alpha$, $(\chi_\alpha \mathbf{Y}_\alpha)_q = \chi_\alpha(q)(\mathbf{Y}_\alpha)_q$ for $q \in U_\alpha$ and $0$ outside $U_\alpha$, is smooth on the open set $U_\alpha$, as the product of a smooth function and a smooth vector field; it vanishes on the open set $M \setminus \operatorname{supp}\chi_\alpha$; and these two open sets cover $M$, since $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$. Smoothness is local, so $\chi_\alpha \mathbf{Y}_\alpha \in \mathfrak{X}(M)$.
>
> *(2)* Let $q \in M$. Since $\{\operatorname{supp}\chi_\alpha\}_{\alpha \in A}$ is locally finite, $q$ has an open neighbourhood $N$ for which $F = \{\alpha \in A : N \cap \operatorname{supp}\chi_\alpha \neq \varnothing\}$ is finite. For $\alpha \notin F$, $\chi_\alpha \mathbf{Y}_\alpha \equiv 0$ on $N$, so on $N$
>
> $$
> \widetilde{\mathbf{X}} = \sum_{\alpha \in F} \chi_\alpha \mathbf{Y}_\alpha ,
> $$
>
> a finite sum of smooth vector fields. Hence $\widetilde{\mathbf{X}}$ is a well-defined vector field, smooth on $N$; as $q$ was arbitrary, $\widetilde{\mathbf{X}} \in \mathfrak{X}(M)$.
>
> *(3)* For $\alpha$ with $p \notin U_\alpha$, $\chi_\alpha(p) = 0$, since $\operatorname{supp}\chi_\alpha \subseteq U_\alpha$. Let $A_p = \{\alpha \in A : p \in U_\alpha\}$. Then $\sum_{\alpha \in A_p} \chi_\alpha(p) = \sum_{\alpha \in A} \chi_\alpha(p) = 1$, and
>
> $$
> \widetilde{\mathbf{X}}_p = \sum_{\alpha \in A_p} \chi_\alpha(p)\, (\mathbf{Y}_\alpha)_p = \Big(\sum_{\alpha \in A_p} \chi_\alpha(p)\Big)\, v = v .
> $$

^pf-65-9

> [!theorem] Proposition §65.10: Extension of Smooth Functions from a Closed Submanifold
> Let $S \subseteq M$ be a regular submanifold that is closed in $M$, and $f \in C^\infty(S)$. Then there is $\tilde f \in C^\infty(M)$ with $\tilde f|_S = f$.
>
> *Lee: Lemma 5.34*

^prop-65-10

> [!proof]+ Proof
> *(Not from the assignment; filled in: the proof of Theorem [[§65 Partitions of Unity#^thm-65-11|§65.11]] below, with functions in place of vector fields.)* By Lemma [[§37 Regular Submanifolds#^lem-37-6|§37.6]], $S$ is covered by the domains of adapted charts $(U_\alpha, \varphi_\alpha)$, $\alpha \in A'$, with product images; let $\pi_\alpha : U_\alpha \to U_\alpha \cap S$ be their retractions (Lemma [[§37 Regular Submanifolds#^lem-37-7|§37.7]]). Since $S$ is closed, $U_0 = M \setminus S$ is open, and $\{U_\alpha\}_{\alpha \in A}$, $A = A' \sqcup \{0\}$, is an open cover of $M$. Take a subordinate partition of unity $\{\chi_\alpha\}_{\alpha \in A}$ (Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]]). Put $f_\alpha = f|_{U_\alpha \cap S} \circ \pi_\alpha \in C^\infty(U_\alpha)$ for $\alpha \in A'$, equal to $f$ on $U_\alpha \cap S$ by Lemma [[§37 Regular Submanifolds#^lem-37-8|§37.8]], and $f_0 = 0$. As in Lemma [[§65 Partitions of Unity#^lem-65-9|§65.9]](1), each $\chi_\alpha f_\alpha$, extended by $0$, is smooth on $M$, with support in $\operatorname{supp}\chi_\alpha$; these supports are locally finite, so $\tilde f = \sum_{\alpha \in A} \chi_\alpha f_\alpha$ is smooth (Lemma [[§65 Partitions of Unity#^lem-65-2|§65.2]]). For $p \in S$: $\chi_0(p) = 0$, since $\operatorname{supp}\chi_0 \subseteq M \setminus S$; $\chi_\alpha(p) = 0$ if $p \notin U_\alpha$; and $f_\alpha(p) = f(p)$ if $p \in U_\alpha$, $\alpha \in A'$. So $\tilde f(p) = \big(\sum_{\alpha} \chi_\alpha(p)\big) f(p) = f(p)$.

^pf-65-10

*Uses:* [[§65 Partitions of Unity#^thm-65-11|§65.11]], [[§37 Regular Submanifolds#^lem-37-6|§37.6]], [[§37 Regular Submanifolds#^lem-37-7|§37.7]], [[§65 Partitions of Unity#^thm-65-7|§65.7]], [[§37 Regular Submanifolds#^lem-37-8|§37.8]], [[§65 Partitions of Unity#^lem-65-9|§65.9]], [[§65 Partitions of Unity#^lem-65-2|§65.2]]

> [!theorem] Theorem §65.11: Extension of Vector Fields from a Submanifold
> Let $S \subseteq M$ be a regular submanifold, $\iota : S \hookrightarrow M$ the inclusion, and $\mathbf{X} \in \mathfrak{X}(S)$.
>
> 1. There are an open set $W \supseteq S$ of $M$ and $\widetilde{\mathbf{X}} \in \mathfrak{X}(W)$ with $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$ for every $p \in S$.
> 2. If $S$ is closed in $M$, one can take $W = M$: there is $\widetilde{\mathbf{X}} \in \mathfrak{X}(M)$ with $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$ for every $p \in S$, that is, $\mathbf{X}$ is $\iota$-related to $\widetilde{\mathbf{X}}$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]).
>
> *Lee: Problem 8-15*

^thm-65-11

> [!proof]+ Proof
> *(Assignment 7, Problem 1: the submitted solution, which proves (2); its steps are stated above as Lemmas [[§37 Regular Submanifolds#^lem-37-6|§37.6]], [[§37 Regular Submanifolds#^lem-37-7|§37.7]], [[§37 Regular Submanifolds#^lem-37-8|§37.8]], [[§59 Related Vector Fields#^lem-59-7|§59.7]] and [[§65 Partitions of Unity#^lem-65-9|§65.9]]. The problem as posted did not assume $S$ closed; the submitted solution adds this hypothesis, which Example [[§65 Partitions of Unity#^ex-65-7|§65.7]] shows is needed for (2). Part (1) is filled in.)* For $p \in S$, $\widetilde{\mathbf{X}}_p \in T_pM$ while $\mathbf{X}_p \in T_pS$, so “$\widetilde{\mathbf{X}}$ extends $\mathbf{X}$” means $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$; $\iota_{\ast p}$ is kept explicit throughout.
>
> *(2) The open cover.* By Lemma [[§37 Regular Submanifolds#^lem-37-6|§37.6]], every point of $S$ lies in the domain of an adapted chart with product image; let $\{(U_\alpha, \varphi_\alpha)\}_{\alpha \in A'}$ be a family of such charts whose domains cover $S$. Since $S$ is closed in $M$, $U_0 = M \setminus S$ is open in $M$. With $A = A' \sqcup \{0\}$, $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $M$: every $p \in S$ lies in some $U_\alpha$ with $\alpha \in A'$, and every $p \notin S$ lies in $U_0$.
>
> *The partition of unity.* By Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]] there is a partition of unity $\{\chi_\alpha\}_{\alpha \in A}$ subordinate to $\{U_\alpha\}_{\alpha \in A}$.
>
> *The local extensions.* For $\alpha \in A'$, Lemma [[§59 Related Vector Fields#^lem-59-7|§59.7]] gives $\mathbf{Y}_\alpha \in \mathfrak{X}(U_\alpha)$ with $(\mathbf{Y}_\alpha)_p = \iota_{\ast p}(\mathbf{X}_p)$ for $p \in U_\alpha \cap S$; let $\mathbf{Y}_0 = 0 \in \mathfrak{X}(U_0)$.
>
> *Gluing.* By Lemma [[§65 Partitions of Unity#^lem-65-9|§65.9]](1) and (2), $\widetilde{\mathbf{X}} = \sum_{\alpha \in A} \chi_\alpha \mathbf{Y}_\alpha \in \mathfrak{X}(M)$. Let $p \in S$. Then $p \notin U_0$, and $(\mathbf{Y}_\alpha)_p = \iota_{\ast p}(\mathbf{X}_p)$ for every $\alpha \in A'$ with $p \in U_\alpha$; by Lemma [[§65 Partitions of Unity#^lem-65-9|§65.9]](3) with $v = \iota_{\ast p}(\mathbf{X}_p)$, $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$.
>
> *(1)* *(Filled in.)* Without closedness, let $W = \bigcup_{\alpha \in A'} U_\alpha$, an open set containing $S$ and an open submanifold of $M$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]). The $U_\alpha$, $\alpha \in A'$, form an open cover of $W$; Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]] on the manifold $W$ gives a subordinate partition of unity, and the gluing step, without the index $0$, gives $\widetilde{\mathbf{X}} \in \mathfrak{X}(W)$ with $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$ for $p \in S$.

^pf-65-11

*Uses:* [[§37 Regular Submanifolds#^lem-37-6|§37.6]], [[§37 Regular Submanifolds#^lem-37-7|§37.7]], [[§37 Regular Submanifolds#^lem-37-8|§37.8]], [[§59 Related Vector Fields#^lem-59-7|§59.7]], [[§65 Partitions of Unity#^lem-65-9|§65.9]], [[§65 Partitions of Unity#^ex-65-7|Ex. §65.7]], [[§65 Partitions of Unity#^thm-65-7|§65.7]], [[§37 Regular Submanifolds#^def-37-1|Def. §37.1]]

> [!example] Example §65.7: A Vector Field on a Non-Closed Submanifold That Does Not Extend
> *(Not from the assignment.)* In $M = \mathbb{R}^2$ let $S = \{(x, 0) : x > 0\}$, and on $S$ let $\mathbf{X} = \frac{1}{x}\, \frac{\partial}{\partial x}\big|^S$. There is no $\widetilde{\mathbf{X}} \in \mathfrak{X}(\mathbb{R}^2)$ with $\widetilde{\mathbf{X}}_p = \iota_{\ast p}(\mathbf{X}_p)$ for every $p \in S$. So the hypothesis “$S$ closed” in Theorem [[§65 Partitions of Unity#^thm-65-11|§65.11]](2) cannot be dropped; by part (1), $\mathbf{X}$ does extend to the open set $W = \{(x, y) : x > 0\}$, for instance by $\frac{1}{x}\, \partial/\partial x$.

^ex-65-7

> [!proof]+ Proof
> *(Filled in.)* *The setting.* On $U = \{(x, y) : x > 0\}$ the identity chart $(x, y)$ of $\mathbb{R}^2$ is adapted to $S$, with $S \cap U = S = \{y = 0\}$; so $S$ is a regular submanifold of dimension $1$, with chart $x|_S$, and $\mathbf{X}$ is smooth on $S$, its coefficient $1/x$ being smooth for $x > 0$. $S$ is not closed: $(0, 0) \in \overline{S} \setminus S$.
>
> *No extension.* Suppose $\widetilde{\mathbf{X}} \in \mathfrak{X}(\mathbb{R}^2)$ extends $\mathbf{X}$, and write $\widetilde{\mathbf{X}} = a\, \partial/\partial x + b\, \partial/\partial y$ with $a, b$ smooth, hence continuous, on $\mathbb{R}^2$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]). For $p = (x, 0) \in S$, $\iota_{\ast p}(\partial/\partial x|^S_p) = \partial/\partial x|_p$ (Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]]), so $\widetilde{\mathbf{X}}_p = \frac{1}{x}\, \partial/\partial x|_p$ and $a(x, 0) = 1/x$. As $x \to 0^+$, $a(x, 0) \to +\infty$; but $a$ is continuous at $(0, 0)$, so $a(x, 0) \to a(0, 0)$, a real number. This contradiction shows that no extension exists.

^pf-ex-65-7

*Uses:* [[§56 Vector Fields#^prop-56-1|§56.1]], [[§37 Regular Submanifolds#^prop-37-9|§37.9]]

## An Application: Exhaustion Functions

*Lecture 23. The application of partitions of unity needed for the sketch of the noncompact Whitney embedding theorem ([[§66 The Whitney Embedding Theorem|§66]]): the existence of exhaustion functions, which partitions of unity make quick. Exhaustion functions were defined, and their existence stated, in Lecture 22 with that sketch; they are collected here so that the proof follows the statement.*

> [!definition] Definition §65.6: Exhaustion Function
> An **exhaustion function** on $M$ is a smooth function $f : M \to \mathbb{R}$, $f \ge 0$, such that for every $c \in \mathbb{R}$ the **sublevel set** $f^{-1}\big((-\infty, c]\big)$ is compact.
>
> *Lee: Ch. 2, Exhaustion Functions*

^def-65-6

The cartoon, also used in Morse theory: stand $M$ up with $f$ as the height. The level set at $c$ is the slice at height $c$, and the sublevel set is everything below it, compact for every $c$. It is not obvious that exhaustion functions always exist (Proposition [[§65 Partitions of Unity#^prop-65-13|§65.13]]).

The proof starts from a countable cover by open sets with compact closures, which was set as an exercise.

> [!theorem] Lemma §65.12: Countable Precompact Covers
> Every manifold $M$ has a countable open cover $\{V_i\}_{i \ge 1}$ such that $\overline{V_i}$ is compact for every $i$.
>
> *Lee: Proposition 2.28 (proof)*

^lem-65-12

> [!proof]+ Proof
> *(Set in Lecture 23 as an exercise, the intended argument using paracompactness; filled in, by paracompactness.)* Every $p \in M$ has an open neighbourhood $W_p$ with $\overline{W_p}$ compact (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]). By Theorem [[§65 Partitions of Unity#^thm-65-5|§65.5]] the cover $\{W_p\}_{p \in M}$ has a countable open refinement $\{V_i\}$ covering $M$; if it is finite, repeat one of its sets to index it by $i \ge 1$. Each $V_i$ lies in some $W_{p(i)}$, so $\overline{V_i}$ is a closed subset of the compact set $\overline{W_{p(i)}}$, hence compact. (Another way: the countable basis of precompact sets built in the proof of Lemma [[§65 Partitions of Unity#^lem-65-4|§65.4]] is already such a cover. Local finiteness of the refinement is not needed here.)

^pf-65-12

*Uses:* [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[§65 Partitions of Unity#^lem-65-4|§65.4]], [[§65 Partitions of Unity#^thm-65-5|§65.5]]

> [!theorem] Proposition §65.13: Exhaustion Functions Exist
> Every smooth manifold admits an exhaustion function.
>
> *Lee: Proposition 2.28*

^prop-65-13

> [!proof]+ Proof
> *(Lecture 23. The proposition was announced in Lecture 22, where the sketch of the noncompact Whitney theorem used it before it was proved.)* Let $\{V_i\}_{i \ge 1}$ be as in Lemma [[§65 Partitions of Unity#^lem-65-12|§65.12]], and let $\{\chi_i\}_{i \ge 1}$ be a partition of unity subordinate to it (Theorem [[§65 Partitions of Unity#^thm-65-7|§65.7]]). Reviewing what this means (Definition [[§65 Partitions of Unity#^def-65-2|§65.2]]):
>
> 1. $0 \le \chi_i \le 1$ for all $i$;
> 2. $\{\operatorname{supp}\chi_i\}$ is locally finite;
> 3. $\sum_i \chi_i(p) = 1$ for all $p \in M$ — a finite sum at each point, by (2);
> 4. $\operatorname{supp}\chi_i \subseteq V_i$ for all $i$ — this is what *subordinate* means.
>
> The key construction is to define
>
> $$
> f = \sum_{j \ge 1} j\, \chi_j .
> $$
>
> Without the weights $j$ the sum would be identically $1$; the weights are what make the sublevel sets compact. Again this is a locally finite sum of smooth functions, so $f$ is smooth (Lemma [[§65 Partitions of Unity#^lem-65-2|§65.2]]); and $f \ge 0$ because the $\chi_j$ are nonnegative (in fact $f \ge \sum_j \chi_j = 1$). It remains to show that the sublevel sets are compact.
>
> *Claim.* For every $c \in \mathbb{R}$ and every integer $N \ge 0$ with $N \ge c$,
>
> $$
> f^{-1}\big((-\infty, c]\big) \subseteq \bigcup_{i=1}^N V_i \subseteq \bigcup_{i=1}^N \overline{V_i} .
> $$
>
> *The claim implies the proposition.* $\bigcup_{i=1}^N \overline{V_i}$ is a finite union of compact sets, so it is compact. $f^{-1}((-\infty, c])$ is closed, since $f$ is continuous, and a closed subset of a compact set is compact.
>
> *Proof of the claim.* We prove the contrapositive. Let $p \notin \bigcup_{i=1}^N V_i$. For $i = 1, \ldots, N$, $p \notin V_i \supseteq \operatorname{supp}\chi_i$, so $\chi_i(p) = 0$. Hence the sum defining $f(p)$ really starts at $N + 1$, and since every coefficient is at least $N + 1$,
>
> $$
> f(p) = \sum_{j = N+1}^\infty j\, \chi_j(p) \ \ge\ (N + 1) \underbrace{\sum_{j = N+1}^\infty \chi_j(p)}_{=\, \sum_j \chi_j(p) \,=\, 1} = N + 1 > c .
> $$
>
> So $p \notin f^{-1}((-\infty, c])$.

^pf-65-13

*Uses:* [[§65 Partitions of Unity#^lem-65-12|§65.12]], [[§65 Partitions of Unity#^thm-65-7|§65.7]], [[§65 Partitions of Unity#^def-65-2|Def. §65.2]]

> [!remark] Remark: Why the Closures
> Should the contrapositive use the union of the *closures*? The proof shows the inclusion in $\bigcup_{i \le N} V_i$, which is contained in the union of the closures, so it makes no difference. The open sets give the stronger statement; the closures are where compactness lives, since the $V_i$ were chosen so that the $\overline{V_i}$ are compact, and $\bigcup_{i \le N} V_i$ alone need not be compact. Lee runs the contrapositive from $p \notin \bigcup_{j \le N} \overline{V_j}$ instead (Proposition 2.28); either way the sublevel set lands inside the compact set $\bigcup_{j \le N} \overline{V_j}$.

^rem-65-3

![[m591-66-5.svg]]

*(Not from lecture; figure added, computed.)* The construction on $M = \mathbb{R}$, with $V_1 = (-1, 1)$ and $V_j = \{ j - 1.6 < |x| < j \}$ for $j \ge 2$, and $\chi_j$ obtained by normalizing bumps positive exactly on $V_j$. Then $f = \sum_j j\chi_j$ climbs one step on each successive $V_j$, so it grows like $|x|$. The sublevel set $f^{-1}((-\infty, 2.5])$ (red) lies inside $\overline{V_1} \cup \overline{V_2} \cup \overline{V_3} = [-3, 3]$, as the claim with $N = 3$ says.

![[m591-66-a1.gif|460]]

*(Not from lecture; animation added, vault only.)* The construction of the figure on $M = \mathbb{R}$ (drawn on $[-5.8, 5.8]$): bumps $\psi_j$ positive exactly on the $V_j$, then normalized, $\chi_j = \psi_j / \sum_k \psi_k$. Their sum (black) goes from a wavy curve, between $0.04$ and $1$, to the constant $1$.

Partitions of unity are a very common technique in the subject, best learned by using them in homework problems with hints; the next assignment contains at least one application of partitions of unity.

**Transcription note (Lecture 23).** The board defined $f = \sum_{j \ge 0} j\chi_j$ but wrote the union in the claim from $i = 1$. These notes index the cover and the partition from $1$, as Lee does. If the index starts at $0$, the union in the claim must start at $i = 0$ too. Otherwise a point of $V_0$ outside $V_1, \ldots, V_N$ can have $f(p) = \sum_{j > N} j\chi_j(p) < N + 1$, since then $\sum_{j > N}\chi_j(p) = 1 - \chi_0(p)$.
