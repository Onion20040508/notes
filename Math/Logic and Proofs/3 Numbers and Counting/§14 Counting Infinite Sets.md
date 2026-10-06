---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: 14
eccles: "Ch. 14"
aliases: ["Eccles 14"]
tags: [logic-and-proofs, mat250]
---
← [[§13 Number Systems]] · ↑ [[· 3 Numbers and Counting]] · [[§14a Uncountable Sets]] →

*Eccles, Chapter 14 and Problems III (Q12, Q26–Q28) · MAT 250 HW5 (Exercises 14.1–14.4) · MAT 200 lecture (syllabus week 15).*

For finite sets, "same number of elements" means "there is a bijection" ([[§10 Counting#^prop-10-3|Proposition §10.3]]). This section takes the bijection as the definition for arbitrary sets and explores which properties of finite sets survive. Several do not: an infinite set can be equipotent to a proper subset, and unions and products of denumerable sets are no bigger than the sets themselves; $\Z$ and $\Q$ turn out to be no larger than $\Z^+$. But not all infinite sets have the same size: $\R$ is uncountable, every set is smaller than its power set (Cantor), and two sets each injecting into the other are equipotent (Cantor–Schröder–Bernstein). This is the cardinality unit of the MAT 200 syllabus. The uncountable sets are treated in [[§14a Uncountable Sets|§14a]].

## 14.1 Countable Sets

> [!definition] Definition §14.1: Equipotent Sets
> Two sets $X$ and $Y$ are **equipotent** if there is a bijection $X \to Y$.
>
> *Eccles: Definition 14.1.1*

^def-14-1

So $X$ is finite of cardinality $n \in \Z^+$ if and only if $X$ is equipotent to $\N_n$.

> [!definition] Definition §14.3: Denumerable Set
> A set $X$ is **denumerable** (or enumerable) if there is a bijection $\Z^+ \to X$, i.e. $X$ is equipotent to $\Z^+$. Such an $X$ has **cardinality $\aleph_0$** ("aleph null"), written $|X| = \aleph_0$.
>
> *Eccles: Definition 14.1.2*

^def-14-2

A bijection $f : \Z^+ \to X$ lists the elements of a denumerable set in an infinite list, $X = \{x_1, x_2, \ldots, x_n, \ldots\}$ with $x_n = f(n)$, each element occurring exactly once.

> [!definition] Definition §14a.1: Countable and Uncountable Sets
> A set is **countable** if it is finite or denumerable, and **uncountable** if it is not countable.
>
> *Eccles: Definition 14.1.2*

^def-14-3

> [!remark] Remark: Terminology Elsewhere
> Conventions differ. In 451, "countable" means *denumerable* ([[§2 The Set ℚ of Rational Numbers#^def-2-8|451 Def. §2.8]], for infinite sets only), and $\N$ there is $\{1, 2, 3, \ldots\}$, our $\Z^+$. In 551, "countable" means finite or countably infinite, as here ([[§1 Countability and Set Theory#^def-1-8|551 Def. §1.8]]), and "equivalent" means equipotent ([[§1 Countability and Set Theory#^def-1-7|551 Def. §1.7]]).

^rem-14-1

> [!example] Example §14.1: Denumerable Sets
> (a) $\Z^+$ is denumerable, by the identity map: $\Z^+ = \{1, 2, \ldots, n, \ldots\}$.
>
> (b) $\N = \{0, 1, 2, \ldots\}$ is denumerable, by $n \mapsto n - 1$: $\N = \{0, 1, \ldots, n - 1, \ldots\}$.
>
> (c) $\Z$ is denumerable, by
>
> $$
> n \mapsto \begin{cases} -(n-1)/2 & \text{if } n \text{ is odd}, \\ n/2 & \text{if } n \text{ is even}, \end{cases}
> $$
>
> which lists $\Z = \{0, 1, -1, 2, -2, \ldots, n, -n, \ldots\}$. (The even $n$ go bijectively to the positive integers, the odd $n$ to the integers $\le 0$.)
>
> (d) The positive even integers $\{2n \mid n \in \Z^+\}$ are denumerable, by $n \mapsto 2n$.
>
> (e) The positive perfect squares $\{n^2 \mid n \in \Z^+\}$ are denumerable, by $n \mapsto n^2$ (injective because $m < n \Rightarrow m^2 < n^2$ for positive integers).
>
> *Eccles: Examples 14.1.3*

^ex-14-1

> [!remark]- Connections
> - (c) in 451: [[§2 The Set ℚ of Rational Numbers#^thm-2-4|451 Thm. §2.4]].

A finite set is never equipotent to a proper subset ([[§11 Properties of Finite Sets#^cor-11-5|Corollary §11.5]]), but (d) and (e) show that $\Z^+$ is. In this sense there are "as many" even numbers, or perfect squares, as positive integers, although the squares become ever scarcer. Galileo (*Two New Sciences*, 1638) noticed this for the squares and concluded that "greater than" makes no sense for infinite quantities; Bolzano (1850) found many such bijections but suspected that some infinite sets are genuinely bigger, anticipating Cantor; and Dedekind (1872) turned the phenomenon into a definition of "infinite". We first check that denumerable sets really are infinite.

> [!theorem] Proposition §14.1: Sets Containing a Copy of the Positive Integers Are Infinite
> If there is an injection $f : \Z^+ \to X$, then $X$ is infinite. In particular $\Z^+$ and every denumerable set are infinite.
>
> *Eccles: Problems III Q12*

^prop-14-1

> [!proof]+ Proof
> Suppose for contradiction that $X$ is finite. It is non-empty, as $f(1) \in X$, so $|X| = n \ge 1$. The restriction of $f$ to $\N_{n+1}$ is an injection $\N_{n+1} \to X$, so $n + 1 \le n$ by Corollary [[§11 Properties of Finite Sets#^cor-11-1|§11.1]], a contradiction.

^pf-14-1

*Uses:* [[§11 Properties of Finite Sets#^cor-11-1|§11.1]]

> [!theorem] Lemma §14.2: Infinite Sets Contain Denumerable Subsets
> If $X$ is infinite, there is an injection $\Z^+ \to X$; its image $A = \{a_1, a_2, \ldots\}$ is a denumerable subset of $X$.
>
> *Eccles: proof of Theorem 14.1.4*

^lem-14-2

> [!proof]+ Proof
> Define distinct $a_1, a_2, \ldots \in X$ inductively. $X \ne \emptyset$ since $\emptyset$ is finite; choose any $a_1 \in X$. Suppose distinct $a_1, \ldots, a_k$ have been chosen, and let $A_k = \{a_1, \ldots, a_k\}$, a finite set. Then $X - A_k \ne \emptyset$, since otherwise $X = A_k$ would be finite; choose any $a_{k+1} \in X - A_k$. The map $n \mapsto a_n$ is injective, since for $m < n$, $a_n \notin A_{n-1} \ni a_m$; so it is a bijection from $\Z^+$ onto its image $A$.

^pf-14-2

*Uses:* [[§10 Counting#^def-10-2|Def. §10.2]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]] (definition by induction, as in [[§5 The Induction Principle#^def-5-2|Def. §5.2]])

> [!remark]- Remark: Infinitely Many Choices
> The proof makes infinitely many arbitrary choices, one at each step. That this is legitimate is an axiom of set theory (the axiom of dependent choice, a weak form of the axiom of choice), used tacitly by Eccles here and in similar places below (choosing a bijection $\Z^+ \to A_n$ for every $n$ in Example [[§14 Counting Infinite Sets#^ex-14-4|§14.4]]). Where a choice can be made by a rule, such as "the least element", no axiom is needed; Proposition [[§14 Counting Infinite Sets#^prop-14-5|§14.5]] works that way.

^rem-14-2

> [!remark]- Connections
> - In 551: [[§1 Countability and Set Theory#^thm-1-2|551 Thm. §1.2]].

> [!theorem] Theorem §14.3: Dedekind's Characterization of Infinite Sets
> A set $X$ is infinite if and only if it is equipotent to a proper subset of itself.
>
> *Eccles: Theorem 14.1.4*

^thm-14-3

> [!proof]+ Proof
> ($\Leftarrow$) Suppose $X$ is equipotent to a proper subset $Y$. If $X$ were finite, then $|Y| < |X|$ by Corollary [[§11 Properties of Finite Sets#^cor-11-5|§11.5]], while $|Y| = |X|$ by Proposition [[§10 Counting#^prop-10-3|§10.3]]. So $X$ is infinite.
>
> ($\Rightarrow$) Let $X$ be infinite and $A = \{a_1, a_2, \ldots\} \subseteq X$ as in Lemma [[§14 Counting Infinite Sets#^lem-14-2|§14.2]], the $a_n$ distinct. Define $f : X \to X - \{a_1\}$ by
>
> $$
> f(x) = \begin{cases} a_{n+1} & \text{if } x = a_n \in A, \\ x & \text{if } x \notin A. \end{cases}
> $$
>
> It maps into $X - \{a_1\}$, since $a_1$ is neither some $a_{n+1}$ nor outside $A$. It is injective: $f$ maps $A$ into $A$ injectively ($a_m \mapsto a_{m+1}$) and $X - A$ into $X - A$ identically, so two points can only have the same image if they lie on the same side, and then they are equal. It is surjective: $y \in X - \{a_1\}$ is either outside $A$, and then $y = f(y)$, or $y = a_n$ with $n \ge 2$, and then $y = f(a_{n-1})$. So $X$ is equipotent to the proper subset $X - \{a_1\}$.

^pf-14-3

*Uses:* [[§11 Properties of Finite Sets#^cor-11-5|§11.5]], [[§10 Counting#^prop-10-3|§10.3]], [[§14 Counting Infinite Sets#^lem-14-2|§14.2]]

The map shifts the sequence $a_1, a_2, \ldots$ one step along, like the guests of an infinite hotel each moving up one room to free room $1$.

## 14.2 Denumerable Sets

For finite sets, the cardinality decides whether there is a bijection between them. The same holds for cardinality $\aleph_0$.

> [!theorem] Proposition §14.4: Equipotent to a Denumerable Set
> Let $X$ be denumerable. A set $Y$ is denumerable if and only if it is equipotent to $X$.
>
> *Eccles: Proposition 14.2.1*

^prop-14-4

> [!proof]+ Proof
> Let $f : \Z^+ \to X$ be a bijection. If $Y$ is denumerable, with bijection $g : \Z^+ \to Y$, then $g \circ f^{-1} : X \to \Z^+ \to Y$ is a bijection. Conversely, if $h : X \to Y$ is a bijection, then $h \circ f : \Z^+ \to X \to Y$ is a bijection, so $Y$ is denumerable.

^pf-14-4

*Uses:* [[§14 Counting Infinite Sets#^def-14-2|Def. §14.2]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]]

To prove statements about all denumerable sets, prove them first for the standard set $\Z^+$, as was done with $\N_n$ for finite sets.

> [!theorem] Proposition §14.5: Subsets of Denumerable Sets
> A subset of a denumerable set is countable (finite or denumerable).
>
> *Eccles: Proposition 14.2.5*

^prop-14-5

The conclusion is an "or" statement, so (as in [[§4 Proof by Contradiction#^ex-4-3|Example §4.3]]) we assume the subset is not finite and show it is denumerable, listing its elements in increasing order.

> [!proof]+ Proof
> (a) Let $A \subseteq \Z^+$ be infinite. Define $f : \Z^+ \to A$ inductively: $f(1) = \min A$, which exists by the well-ordering principle ([[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]); and $f(k+1) = \min\{ a \in A \mid a > f(k) \}$. This set is non-empty, since otherwise $A \subseteq \N_{f(k)}$ would be finite ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]).
>
> *Injective:* $f(k) < f(k+1)$ for all $k$, so $j < k \Rightarrow f(j) < f(k)$.
>
> *Surjective:* first, $f(n) \ge n$ for all $n$, by induction: $f(1) \ge 1$, and $f(k+1) > f(k) \ge k$ gives $f(k+1) \ge k + 1$. Let $a \in A$. Since $f(a) \ge a$, the set $\{ m \in \Z^+ \mid f(m) \ge a \}$ is non-empty; let $m$ be its least element. If $m = 1$, then $a \ge \min A = f(1) \ge a$, so $f(1) = a$. If $m > 1$, then $f(m-1) < a$, so $a$ belongs to $\{ a' \in A \mid a' > f(m-1) \}$, whose least element is $f(m)$; hence $f(m) \le a \le f(m)$ and $f(m) = a$.
>
> So $f$ is a bijection and $A$ is denumerable. Hence every subset of $\Z^+$ is finite or denumerable.
>
> (b) Let $A$ be a subset of a denumerable set $X$, and $g : \Z^+ \to X$ a bijection. The preimage $g^{-1}(A) \subseteq \Z^+$ is finite or denumerable by (a), and $g$ restricts to a bijection $g^{-1}(A) \to A$. Composing it with a bijection $\N_n \to g^{-1}(A)$ or $\Z^+ \to g^{-1}(A)$ shows that $A$ is finite or denumerable.

^pf-14-5

*Uses:* [[§5 The Induction Principle#^cor-5-7|§5.7]] (well-ordering), [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§9 Injections, Surjections and Bijections#^def-9-7|Def. §9.7]] (pre-images)

> [!theorem] Corollary §14.6: Countable Means Injecting into the Positive Integers
> A set $X$ is countable if and only if there is an injection $X \to \Z^+$.
>
> *Source: standard; a consequence of Eccles Proposition 14.2.5*

^cor-14-6

> [!proof]+ Proof
> ($\Rightarrow$) If $X = \emptyset$, the empty function is an injection. If $|X| = n \ge 1$ with bijection $f : \N_n \to X$, then $f^{-1}$ followed by the inclusion $\N_n \subseteq \Z^+$ is an injection. If $X$ is denumerable, the inverse of a bijection $\Z^+ \to X$ is one.
>
> ($\Leftarrow$) An injection $h : X \to \Z^+$ is a bijection $X \to h(X)$, and $h(X) \subseteq \Z^+$ is finite or denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-5|§14.5]]; composing with the inverse of $h$ shows the same for $X$.

^pf-14-6

*Uses:* [[§14 Counting Infinite Sets#^prop-14-5|§14.5]]

> [!remark]- Connections
> - This is 551's definition of countable: [[§1 Countability and Set Theory#^def-1-8|551 Def. §1.8]] (a bijection onto a subset of $\N$).

> [!example] Example §14.2: Finite Union Denumerable
> If $A$ is finite and $B$ is denumerable, then $A \cup B$ is denumerable.
>
> *Solution.* $A \cup B = (A - B) \cup B$ is a disjoint union, and $A - B \subseteq A$ is finite ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]). If $A - B = \emptyset$ then $A \cup B = B$. Otherwise let $f : \N_m \to A - B$ and $g : \Z^+ \to B$ be bijections and count $A - B$ first, then $B$ (the other way round we would never reach $A - B$):
>
> $$
> h : \Z^+ \to A \cup B, \qquad h(k) = \begin{cases} f(k) & \text{if } k \le m, \\ g(k - m) & \text{if } k > m. \end{cases}
> $$
>
> As in the addition principle ([[§10 Counting#^thm-10-4|Theorem §10.4]]), $h$ is surjective because $f$ and $g$ are, and injective because $f$ and $g$ are and $(A - B) \cap B = \emptyset$.
>
> *Eccles: Exercise 14.1*
> *Source: HW5*
>
> *The HW5 solution uses this map with $A$ in place of $A - B$, which is a bijection only when $A \cap B = \emptyset$; replacing $A$ by $A - B$ handles the general case.*

^ex-14-2

*Uses:* [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§10 Counting#^thm-10-4|§10.4]]

Forming unions or products of finite sets normally makes them bigger. For denumerable sets it does not.

> [!theorem] Proposition §14.7: Union of Two Denumerable Sets
> If $A$ and $B$ are denumerable, then so is $A \cup B$.
>
> *Eccles: Proposition 14.2.2 (proof: Exercise 14.2)*

^prop-14-7

> [!proof]+ Proof
> $A \cup B = A \cup (B - A)$ is a disjoint union, and $B - A \subseteq B$ is finite or denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-5|§14.5]]. If it is finite, Example [[§14 Counting Infinite Sets#^ex-14-2|§14.2]] applies. If it is denumerable, let $f : \Z^+ \to A$ and $g : \Z^+ \to B - A$ be bijections. Counting one set and then the other would never reach the second, so alternate:
>
> $$
> h : \Z^+ \to A \cup B, \qquad h(2n - 1) = f(n), \quad h(2n) = g(n) \qquad (n \in \Z^+).
> $$
>
> Every $k \in \Z^+$ is either $2n - 1$ or $2n$ for exactly one $n \in \Z^+$ ([[§11 Properties of Finite Sets#^prop-11-11|Proposition §11.11]]), so $h$ is well defined. It is surjective because $f$ and $g$ are. It is injective because $f$ and $g$ are and the odd places land in $A$, the even places in $B - A$, which are disjoint.

^pf-14-7

*Uses:* [[§14 Counting Infinite Sets#^prop-14-5|§14.5]], [[§14 Counting Infinite Sets#^ex-14-2|Ex. §14.2]], [[§11 Properties of Finite Sets#^prop-11-11|§11.11]]

> [!example] Example §14.3: Removing a Denumerable Set
> (a) If $A$ and $B$ are denumerable then $A \cup B$ is denumerable: this is Proposition [[§14 Counting Infinite Sets#^prop-14-7|§14.7]].
>
> (b) If $X$ is uncountable and $A \subseteq X$ is denumerable, then $X - A$ is uncountable.
>
> *Solution of (b).* Suppose for contradiction that $X - A$ is countable. Since $X = (X - A) \cup A$, if $X - A$ is finite then $X$ is denumerable by Example [[§14 Counting Infinite Sets#^ex-14-2|§14.2]], and if $X - A$ is denumerable then $X$ is denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-7|§14.7]]. Either way $X$ is countable, a contradiction.
>
> *Eccles: Exercise 14.2*
> *Source: HW5*
>
> *The HW5 solution to (a) uses $a_n \mapsto 2n + 1$, $b_m \mapsto 2m$, which misses $1$ ($2n - 1$ fixes it) and assumes $A \cap B = \emptyset$; part (b) is not in the HW5 solution.*

^ex-14-3

*Uses:* [[§14 Counting Infinite Sets#^prop-14-7|§14.7]], [[§14 Counting Infinite Sets#^ex-14-2|Ex. §14.2]]

> [!theorem] Proposition §14.8: Product of Two Denumerable Sets
> If $A$ and $B$ are denumerable, then so is $A \times B$.
>
> *Eccles: Proposition 14.2.3*

^prop-14-8

List $A = \{a_1, a_2, \ldots\}$ and $B = \{b_1, b_2, \ldots\}$ and arrange $A \times B$ in an infinite array, $(a_m, b_n)$ in column $m$ and row $n$. Counting along the first row never reaches the second. Counting along the diagonals $m + n - 1 = 1, 2, 3, \ldots$ in turn does reach every element: diagonal $s$ has $s$ elements, and $(a_m, b_n)$ is the $n$th element of diagonal $m + n - 1$, so its number is $1 + 2 + \cdots + (m + n - 2) + n = \tfrac12 (m+n-2)(m+n-1) + n$ ([[§5 The Induction Principle#^prop-5-5|Proposition §5.5]]).

> [!proof]+ Proof
> Let $T(s) = s(s+1)/2 = 1 + 2 + \cdots + s$ for $s \ge 0$, so $T(0) = 0$ and $T(s) - T(s-1) = s$; in particular $T$ is strictly increasing. Define
>
> $$
> \varphi : \Z^+ \times \Z^+ \to \Z^+, \qquad \varphi(m, n) = T(m + n - 2) + n = \tfrac12 (m + n - 2)(m + n - 1) + n .
> $$
>
> With $s = m + n - 1 \ge 1$ we have $1 \le n \le s$, so $T(s-1) < \varphi(m, n) \le T(s)$.
>
> *Surjective.* Let $N \in \Z^+$. Since $T(N) \ge N$, there is a least $s \in \Z^+$ with $T(s) \ge N$, and then $T(s - 1) < N$. Put $n = N - T(s-1)$, so $1 \le n \le T(s) - T(s-1) = s$, and $m = s - n + 1 \ge 1$. Then $\varphi(m, n) = T(s-1) + n = N$.
>
> *Injective.* If $\varphi(m, n) = \varphi(m', n') = N$, then $s = m + n - 1$ and $s' = m' + n' - 1$ both satisfy $T(s - 1) < N \le T(s)$. The intervals $(T(s-1), T(s)]$ are disjoint for different $s$ because $T$ is increasing, so $s = s'$; then $n = N - T(s - 1) = n'$ and $m = s - n + 1 = m'$.
>
> So $\varphi$ is a bijection. For denumerable $A$, $B$ with bijections $f : \Z^+ \to A$, $g : \Z^+ \to B$, the map $(f(m), g(n)) \mapsto \varphi(m, n)$, that is, $\varphi \circ (f^{-1} \times g^{-1})$, is a bijection $A \times B \to \Z^+$.

^pf-14-8

*Uses:* [[§5 The Induction Principle#^prop-5-5|§5.5]] (the sum $1 + \cdots + s$), [[§5 The Induction Principle#^cor-5-7|§5.7]] (well-ordering), [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]]

![[m250-14-1.svg]]
*The diagonal count of $\Z^+ \times \Z^+$: the point $(m, n)$ is labelled $\varphi(m, n)$. Each diagonal $m + n - 1 = s$ is run from $(s, 1)$ up to $(1, s)$ (solid arrows), and the count then jumps to the start of the next diagonal (dotted). Every point is reached after finitely many steps, unlike a row-by-row count, which never leaves the first row.*

> [!theorem] Corollary §14.9: Finite Powers of a Denumerable Set
> If $A$ is denumerable, then so is $A^n$ for every $n \in \Z^+$.
>
> *Eccles: Corollary 14.2.4*

^cor-14-9

> [!proof]+ Proof
> Induction on $n$. $A^1 = A$. If $A^k$ is denumerable, then $(a_1, \ldots, a_{k+1}) \mapsto ((a_1, \ldots, a_k), a_{k+1})$ is a bijection $A^{k+1} \to A^k \times A$, and $A^k \times A$ is denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-8|§14.8]]; so $A^{k+1}$ is denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-4|§14.4]].

^pf-14-9

*Uses:* [[§14 Counting Infinite Sets#^prop-14-8|§14.8]], [[§14 Counting Infinite Sets#^prop-14-4|§14.4]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

> [!example] Example §14.4: A Denumerable Union of Denumerable Sets
> If $\{A_n \mid n \in \Z^+\}$ is a denumerable set of pairwise disjoint denumerable sets, then
>
> $$
> \bigcup_{n \in \Z^+} A_n = \{ x \mid x \in A_n \text{ for some } n \in \Z^+ \}
> $$
>
> is denumerable.
>
> *Solution.* For each $n$ choose a bijection $g_n : \Z^+ \to A_n$, listing $A_n = \{a_{n1}, a_{n2}, \ldots\}$ with $a_{nm} = g_n(m)$. Define
>
> $$
> F : \Z^+ \times \Z^+ \to \bigcup_{n} A_n, \qquad F(n, m) = a_{nm} = g_n(m).
> $$
>
> $F$ is surjective, since every element of the union lies in some $A_n$ and $g_n$ is surjective. $F$ is injective: if $a_{nm} = a_{n'm'}$, this element lies in $A_n \cap A_{n'}$, so $n = n'$ by disjointness, and then $m = m'$ because $g_n$ is injective. So the union is equipotent to $\Z^+ \times \Z^+$, which is denumerable by Proposition [[§14 Counting Infinite Sets#^prop-14-8|§14.8]]; by Proposition [[§14 Counting Infinite Sets#^prop-14-4|§14.4]] the union is denumerable. The array $(a_{nm})$ is counted along diagonals exactly as in the figure.
>
> Disjointness is not essential: without it $F$ is still surjective, the union is infinite (it contains $A_1$), and sending each $x$ to the $\varphi$-least $(n, m)$ with $F(n, m) = x$ is an injection into $\Z^+ \times \Z^+$; so the union is denumerable by Corollary [[§14 Counting Infinite Sets#^cor-14-6|§14.6]].
>
> *Eccles: Exercise 14.3*
> *Source: HW5*
>
> *The HW5 solution proves by induction that $A_1 \cup \cdots \cup A_n$ is denumerable for each $n$, which covers finite unions only; the union of all the $A_n$ needs the array $\Z^+ \times \Z^+$.*

^ex-14-4

*Uses:* [[§14 Counting Infinite Sets#^prop-14-8|§14.8]], [[§14 Counting Infinite Sets#^prop-14-4|§14.4]], [[§14 Counting Infinite Sets#^cor-14-6|§14.6]], [[§14 Counting Infinite Sets#^prop-14-1|§14.1]]

> [!remark]- Connections
> - The general statement, a countable union of countable sets is countable: [[§3 Countability of Rationals and Unions#^prop-3-1|551 Prop. §3.1]] ([[Countable Union of Countable Sets is Countable]]).

> [!theorem] Theorem §14.10: The Rationals Are Denumerable (Cantor, 1874)
> The set $\Q$ of rational numbers is denumerable.
>
> *Eccles: Theorem 14.2.6*

^thm-14-10

Eccles sends $q$ to its fraction in lowest terms. That this fraction is unique is only proved in [[§17 Consequences of the Euclidean Algorithm#^ex-17-7|Example §17.7]], so we single it out directly as the fraction with the least positive denominator.

> [!proof]+ Proof
> For $q \in \Q$, the set $\{ n \in \Z^+ \mid nq \in \Z \}$ is non-empty ($q = a/b$ with $b > 0$ gives $bq = a$); let $n$ be its least element, $m = nq$, and $f(q) = (m, n)$. This defines
>
> $$
> f : \Q \to \Z \times \Z^+ .
> $$
>
> (Then $m/n$ is in fact in lowest terms: a common divisor $d > 1$ would give $(n/d)\,q = m/d \in \Z$ with $n/d < n$.) $f$ is injective, since $q = m/n$ is recovered from $f(q)$. The set $\Z \times \Z^+$ is denumerable, by Example [[§14 Counting Infinite Sets#^ex-14-1|§14.1]](c) and Proposition [[§14 Counting Infinite Sets#^prop-14-8|§14.8]]. The image of $f$ is infinite, since it contains $f(k) = (k, 1)$ for every $k \in \Z^+$ (Proposition [[§14 Counting Infinite Sets#^prop-14-1|§14.1]]), so by Proposition [[§14 Counting Infinite Sets#^prop-14-5|§14.5]] it is denumerable. As $f$ is a bijection from $\Q$ onto its image, $\Q$ is denumerable (Proposition [[§14 Counting Infinite Sets#^prop-14-4|§14.4]]).

^pf-14-10

*Uses:* [[§14 Counting Infinite Sets#^ex-14-1|Ex. §14.1]], [[§14 Counting Infinite Sets#^prop-14-8|§14.8]], [[§14 Counting Infinite Sets#^prop-14-5|§14.5]], [[§14 Counting Infinite Sets#^prop-14-4|§14.4]], [[§14 Counting Infinite Sets#^prop-14-1|§14.1]], [[§13 Number Systems#^def-13-1|Def. §13.1]], [[§13 Number Systems#^def-13-2|Def. §13.2]]

> [!remark]- Connections
> - In 451 and 551: [[§2 The Set ℚ of Rational Numbers#^thm-2-5|451 Thm. §2.5]], [[§3 Countability of Rationals and Unions#^cor-3-2|551 Cor. §3.2]] (there via countable unions).

Uncountable sets, Cantor's theorem and the Cantor–Schröder–Bernstein theorem continue in [[§14a Uncountable Sets]].
