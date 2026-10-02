---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: 12
eccles: "Ch. 12"
aliases: ["Eccles 12"]
tags: [logic-and-proofs, mat250, extension]
---
← [[§11 Properties of Finite Sets]] · ↑ [[· 3 Numbers and Counting]] · [[§13 Number Systems]] →

*Eccles, Chapter 12 and Problems III (Q17).*
★ *Not in the MAT 250 course record (no homework or syllabus entry for this chapter; MAT 200 read Chapters 10, 11 and 14); included from Eccles to complete the counting.*

Many counting problems ask for the number of functions between two finite sets, possibly with some property, or the number of subsets of a finite set, possibly of a given size. This section counts functions, injections and permutations, and then subsets; counting subsets of a given size produces the binomial coefficients, which are computed by Pascal's triangle and explained by the binomial theorem. One more level of abstraction is involved: a function is now treated as a single object, an element of the set of all functions $X \to Y$.

## 12.1 Counting Sets of Functions

If $X$ is a set of people and $Y$ the dishes on a menu, a function $X \to Y$ is an order for the table; if $S$ is a set of students and $T$ a set of tutors, a function $S \to T$ assigns a tutor to each student.

> [!example] Example §12.1: Functions from a 3-Set to a 2-Set
> Let $X = \{a, b, c\}$ and $Y = \{d, e\}$. A function $f : X \to Y$ is given by listing $f(a)$, $f(b)$, $f(c)$; each can be chosen in $2$ ways, so there are $2 \times 2 \times 2 = 8$ functions (they are listed in [[§8 Functions#^ex-8-2|Example §8.2]]).
>
> *Eccles: Example 12.1.1*

^ex-12-1

> [!definition] Definition §12.1: The Set of Functions
> For sets $X$ and $Y$, the set of all functions from $X$ to $Y$ is denoted $\operatorname{Fun}(X, Y)$.
>
> *Eccles: Definition 12.1.3*

^def-12-1

> [!theorem] Proposition §12.1: Counting Functions
> Let $X$ and $Y$ be non-empty finite sets with $|X| = m$ and $|Y| = n$. Then the number of functions $X \to Y$ is $n^m$: $|\operatorname{Fun}(X, Y)| = n^m$.
>
> *Eccles: Proposition 12.1.2*

^prop-12-1

The informal argument: list $X = \{x_1, \ldots, x_m\}$; there are $n$ choices for $f(x_1)$, $n$ for $f(x_2)$, and so on, giving $n \times n \times \cdots \times n = n^m$. The "and so on" is an induction on $m$, and the formal proof below is that induction written out; the simple idea underpins the more complicated formal argument.

> [!proof]+ Proof
> Induction on $m$, for all non-empty finite $Y$.
>
> *Base case $m = 1$.* If $X = \{x_1\}$ then $f \mapsto f(x_1)$ is a bijection $\operatorname{Fun}(X, Y) \to Y$, so $|\operatorname{Fun}(X, Y)| = n$.
>
> *Inductive step.* Suppose the result holds for $m = k$, and let $X_1 = \{x_1, \ldots, x_{k+1}\}$ and $Y = \{y_1, \ldots, y_n\}$. Then
>
> $$
> \operatorname{Fun}(X_1, Y) = \bigcup_{i=1}^n \{ f : X_1 \to Y \mid f(x_{k+1}) = y_i \},
> $$
>
> a union of pairwise disjoint sets. For each $i$, restriction $f \mapsto f|_{\{x_1, \ldots, x_k\}}$ is a bijection
>
> $$
> \{ f : X_1 \to Y \mid f(x_{k+1}) = y_i \} \to \operatorname{Fun}(\{x_1, \ldots, x_k\}, Y):
> $$
>
> a function with $f(x_{k+1}) = y_i$ is determined by its values on $x_1, \ldots, x_k$ (injectivity), and any $g$ on $\{x_1, \ldots, x_k\}$ extends by $x_{k+1} \mapsto y_i$ (surjectivity). By the inductive hypothesis each set in the union has $n^k$ elements, so by Corollary [[§10 Counting#^cor-10-5|§10.5]]
>
> $$
> |\operatorname{Fun}(X_1, Y)| = \sum_{i=1}^n n^k = n \times n^k = n^{k+1}.
> $$

^pf-12-1

*Uses:* [[§10 Counting#^cor-10-5|§10.5]], [[§10 Counting#^prop-10-3|§10.3]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

Often only functions with a particular property are wanted, most commonly injections.

> [!definition] Definition §12.2: The Set of Injections
> For sets $X$ and $Y$, the set of injections from $X$ to $Y$ is denoted $\operatorname{Inj}(X, Y)$.
>
> *Eccles: Definition 12.1.5*

^def-12-2

> [!theorem] Proposition §12.2: Counting Injections
> Let $X$ and $Y$ be non-empty finite sets with $|X| = m$ and $|Y| = n$. Then the number of injections $X \to Y$ is
>
> $$
> |\operatorname{Inj}(X, Y)| = n(n-1)\cdots(n-m+1).
> $$
>
> *Eccles: Proposition 12.1.4*

^prop-12-2

The number $(n)_m = n(n-1)\cdots(n-m+1)$ ($m$ factors) is the **falling factorial**. For $m = n$ it is the factorial $n!$; for $m \le n$ it equals $n!/(n-m)!$; and for $m > n$ one factor is $0$, so it vanishes. The last case is the pigeonhole principle ([[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]]): there are no injections. The proof is that of Proposition [[§12★ Counting Functions and Subsets#^prop-12-1|§12.1]], except that each new value must avoid the values already used.

> [!proof]+ Proof
> Induction on $m$, for all finite $Y$, where for $Y = \emptyset$ the claim reads $|\operatorname{Inj}(X, \emptyset)| = 0 = (0)_m$ (there are no functions from a non-empty set to $\emptyset$).
>
> *Base case $m = 1$.* If $X = \{x_1\}$, every function is injective and $f \mapsto f(x_1)$ is a bijection $\operatorname{Inj}(X, Y) = \operatorname{Fun}(X, Y) \to Y$; so the number is $n = (n)_1$.
>
> *Inductive step.* Suppose the result holds for $m = k$ and let $X_1 = \{x_1, \ldots, x_{k+1}\}$, $Y = \{y_1, \ldots, y_n\}$ with $n \ge 1$. Then
>
> $$
> \operatorname{Inj}(X_1, Y) = \bigcup_{i=1}^n \{ f \in \operatorname{Inj}(X_1, Y) \mid f(x_{k+1}) = y_i \},
> $$
>
> a disjoint union. If $f$ is injective and $f(x_{k+1}) = y_i$, none of $f(x_1), \ldots, f(x_k)$ is $y_i$; so restriction is a bijection
>
> $$
> \{ f \in \operatorname{Inj}(X_1, Y) \mid f(x_{k+1}) = y_i \} \to \operatorname{Inj}(\{x_1, \ldots, x_k\}, Y - \{y_i\}),
> $$
>
> its inverse extending $g$ by $x_{k+1} \mapsto y_i$, which keeps it injective because $y_i$ is not a value of $g$. As $|Y - \{y_i\}| = n - 1$, the inductive hypothesis gives each set $(n-1)_k = (n-1)(n-2)\cdots(n-k)$ elements (also when $n - 1 = 0$). By Corollary [[§10 Counting#^cor-10-5|§10.5]],
>
> $$
> |\operatorname{Inj}(X_1, Y)| = \sum_{i=1}^n (n-1)(n-2)\cdots(n-k) = n(n-1)\cdots(n-k) = (n)_{k+1}.
> $$

^pf-12-2

*Uses:* [[§10 Counting#^cor-10-5|§10.5]], [[§10 Counting#^thm-10-4|§10.4]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

When $m = n$ an injection $X \to Y$ is automatically a bijection ([[§11 Properties of Finite Sets#^thm-11-7|Theorem §11.7]]). Bijections of a set to itself are of particular interest.

> [!definition] Definition §12.3: Permutation
> A bijection $X \to X$ is called a **permutation** of the set $X$.
>
> *Eccles: Definition 12.1.6*

^def-12-3

> [!theorem] Corollary §12.3: Counting Permutations
> A finite non-empty set of cardinality $n$ has exactly $n!$ permutations.
>
> *Eccles: Corollary 12.1.7*

^cor-12-3

> [!proof]+ Proof
> Take $X = Y$, $m = n$ in Proposition [[§12★ Counting Functions and Subsets#^prop-12-2|§12.2]]: there are $(n)_n = n!$ injections $X \to X$, and these are exactly the bijections by Theorem [[§11 Properties of Finite Sets#^thm-11-7|§11.7]].

^pf-12-3

*Uses:* [[§12★ Counting Functions and Subsets#^prop-12-2|§12.2]], [[§11 Properties of Finite Sets#^thm-11-7|§11.7]]

> [!remark]- Connections
> - The permutations of $X$ form the symmetric group $S_X$, and $|S_n| = n!$: [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]].

## 12.2 Counting Sets of Subsets

Recall ([[§6 The Language of Set Theory#^def-6-9|Definition §6.9]]) that the **power set** of $X$ is the set of its subsets, $\mathcal{P}(X) = \{ A \mid A \subseteq X \}$.

> [!theorem] Proposition §12.4: The Size of the Power Set
> If $X$ is a finite set with $|X| = n$, then $\mathcal{P}(X)$ is finite and
>
> $$
> |\mathcal{P}(X)| = 2^{|X|} = 2^n.
> $$
>
> *Eccles: Proposition 12.2.1*

^prop-12-4

Informally: a subset $A$ is determined by deciding, for each of the $n$ elements $x$, whether $x \in A$ or $x \notin A$; two choices each time give $2^n$ subsets. Characteristic functions make this precise by turning subsets into functions.

> [!definition] Definition §12.4: Characteristic Function
> For a set $X$ and a subset $A \in \mathcal{P}(X)$, the **characteristic function** of $A$ is $\chi_A : X \to \{0, 1\}$,
>
> $$
> \chi_A(x) = \begin{cases} 0 & \text{if } x \notin A, \\ 1 & \text{if } x \in A. \end{cases}
> $$
>
> *Eccles: Definition 12.2.2*

^def-12-4

> [!theorem] Lemma §12.5: Subsets Are Functions to {0, 1}
> The function $\mathcal{P}(X) \to \operatorname{Fun}(X, \{0, 1\})$, $A \mapsto \chi_A$, is a bijection.
>
> *Eccles: Lemma 12.2.3*

^lem-12-5

> [!proof]+ Proof
> Its inverse is $\chi \mapsto \{ x \in X \mid \chi(x) = 1 \}$, the preimage of $\{1\}$: starting from $A$ we get $\{x \mid \chi_A(x) = 1\} = A$, and starting from $\chi$ the characteristic function of $\{x \mid \chi(x) = 1\}$ takes the value $1$ exactly where $\chi$ does, so it is $\chi$.

^pf-12-5

*Uses:* [[§12★ Counting Functions and Subsets#^def-12-4|Def. §12.4]]

> [!proof]+ Proof of Proposition §12.4
> If $n = 0$ then $X = \emptyset$ and $\mathcal{P}(X) = \{\emptyset\}$ has $1 = 2^0$ element. If $n \ge 1$, by Lemma [[§12★ Counting Functions and Subsets#^lem-12-5|§12.5]] and Proposition [[§12★ Counting Functions and Subsets#^prop-12-1|§12.1]],
>
> $$
> |\mathcal{P}(X)| = |\operatorname{Fun}(X, \{0, 1\})| = 2^{|X|}.
> $$

^pf-12-4

*Uses:* [[§12★ Counting Functions and Subsets#^lem-12-5|§12.5]], [[§12★ Counting Functions and Subsets#^prop-12-1|§12.1]], [[§10 Counting#^prop-10-3|§10.3]]

For infinite sets the comparison of $X$ with $\mathcal{P}(X)$ survives as Cantor's theorem, $|X| < |\mathcal{P}(X)|$ ([[§14 Counting Infinite Sets#^thm-14-13|Theorem §14.13]]).

> [!definition] Definition §12.5: r-Subsets and Binomial Coefficients
> For a set $X$ and a non-negative integer $r$, an **$r$-subset** of $X$ is a subset $A \subseteq X$ with $|A| = r$. The set of $r$-subsets is
>
> $$
> \mathcal{P}_r(X) = \{ A \subseteq X \mid |A| = r \}.
> $$
>
> The **binomial coefficient** (or binomial number) $\binom{n}{r}$, read "$n$ choose $r$", is the cardinality of $\mathcal{P}_r(X)$ when $|X| = n$.
>
> *Eccles: Definition 12.2.4*

^def-12-5

The number does not depend on which $n$-element set $X$ is used. If $|X_1| = |X_2|$, there is a bijection $f : X_1 \to X_2$ ([[§10 Counting#^prop-10-3|Proposition §10.3]]); it restricts to a bijection $A \to f(A)$ for each subset $A$, so $|f(A)| = |A|$, and $A \mapsto f(A)$ is a bijection $\mathcal{P}_r(X_1) \to \mathcal{P}_r(X_2)$ with inverse $B \mapsto f^{-1}(B)$ (images and pre-images of subsets, [[§9 Injections, Surjections and Bijections#^def-9-4|Definition §9.4]]).

> [!example] Example §12.2: The Subsets of a 4-Set
> For $X = \{a, b, c, d\}$:
>
> $$
> \begin{aligned}
> \mathcal{P}_0(X) &= \{\emptyset\}, \\
> \mathcal{P}_1(X) &= \{\{a\}, \{b\}, \{c\}, \{d\}\}, \\
> \mathcal{P}_2(X) &= \{\{a,b\}, \{a,c\}, \{a,d\}, \{b,c\}, \{b,d\}, \{c,d\}\}, \\
> \mathcal{P}_3(X) &= \{\{a,b,c\}, \{a,b,d\}, \{a,c,d\}, \{b,c,d\}\}, \\
> \mathcal{P}_4(X) &= \{X\}, \qquad \mathcal{P}_r(X) = \emptyset \text{ for } r > 4.
> \end{aligned}
> $$
>
> So $\binom40 = 1$, $\binom41 = 4$, $\binom42 = 6$, $\binom43 = 4$, $\binom44 = 1$, and $\binom4r = 0$ for $r > 4$.
>
> *Eccles: Example 12.2.5*

^ex-12-2

> [!theorem] Proposition §12.6: Basic Binomial Coefficients
> For non-negative integers $n$ and $r$:
> 1. $\binom{n}{r} = 0$ if $r > n$;
> 2. $\binom{n}{0} = 1$, $\binom{n}{1} = n$, $\binom{n}{n} = 1$;
> 3. $\binom{n}{r} = \binom{n}{n-r}$ for $0 \le r \le n$.
>
> *Eccles: Proposition 12.2.6*

^prop-12-6

> [!proof]+ Proof
> Let $|X| = n$.
>
> (1) Every subset of $X$ has at most $n$ elements ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]), so $\mathcal{P}_r(X) = \emptyset$ for $r > n$.
>
> (2) $\mathcal{P}_0(X) = \{\emptyset\}$, since only $\emptyset$ has $0$ elements, and $\mathcal{P}_n(X) = \{X\}$, since a subset with $n$ elements is $X$ ([[§11 Properties of Finite Sets#^cor-11-5|Corollary §11.5]]). If $X = \{x_1, \ldots, x_n\}$ then $\mathcal{P}_1(X) = \{\{x_1\}, \ldots, \{x_n\}\}$ has $n$ elements (for $n = 0$ it is empty, as (1) says).
>
> (3) $A \mapsto X - A$ is a bijection $\mathcal{P}_r(X) \to \mathcal{P}_{n-r}(X)$: by the addition principle $|X - A| = n - |A|$, and the map is its own inverse.

^pf-12-6

*Uses:* [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§11 Properties of Finite Sets#^cor-11-5|§11.5]], [[§10 Counting#^thm-10-4|§10.4]]

> [!theorem] Proposition §12.7: The Row Sum
> $$
> \sum_{i=0}^n \binom{n}{i} = 2^n.
> $$
>
> *Eccles: Proposition 12.2.7*

^prop-12-7

> [!proof]+ Proof
> Let $|X| = n$. Every subset of $X$ has some cardinality $i$ with $0 \le i \le n$ ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]), so $\mathcal{P}(X) = \bigcup_{i=0}^n \mathcal{P}_i(X)$, a union of pairwise disjoint sets (a set has only one cardinality). By Corollary [[§10 Counting#^cor-10-5|§10.5]] and Proposition [[§12★ Counting Functions and Subsets#^prop-12-4|§12.4]], $\sum_{i=0}^n \binom{n}{i} = |\mathcal{P}(X)| = 2^n$.

^pf-12-7

*Uses:* [[§12★ Counting Functions and Subsets#^prop-12-4|§12.4]], [[§10 Counting#^cor-10-5|§10.5]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]]

### Evaluating binomial coefficients

Listing subsets, as in Example [[§12★ Counting Functions and Subsets#^ex-12-2|§12.2]], is very inefficient. An ancient inductive method rests on the following identity.

> [!theorem] Proposition §12.8: Pascal's Rule
> For integers $n$ and $r$ with $1 \le r \le n$,
>
> $$
> \binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}.
> $$
>
> *Eccles: Proposition 12.2.8*

^prop-12-8

> [!proof]+ Proof
> Let $|X| = n$ and choose $x_1 \in X$. The sets $\mathcal{P}_{r-1}(X - \{x_1\})$ and $\mathcal{P}_r(X - \{x_1\})$ are disjoint (their elements have different cardinalities). Define
>
> $$
> f : \mathcal{P}_r(X) \to \mathcal{P}_{r-1}(X - \{x_1\}) \cup \mathcal{P}_r(X - \{x_1\}), \qquad f(A) = \begin{cases} A - \{x_1\} & \text{if } x_1 \in A, \\ A & \text{if } x_1 \notin A, \end{cases}
> $$
>
> where $|A - \{x_1\}| = r - 1$ in the first case by the addition principle. Its inverse is
>
> $$
> g(B) = \begin{cases} B \cup \{x_1\} & \text{if } B \in \mathcal{P}_{r-1}(X - \{x_1\}), \\ B & \text{if } B \in \mathcal{P}_r(X - \{x_1\}): \end{cases}
> $$
>
> $g(f(A)) = A$ in both cases, and $f(g(B)) = B$ because $x_1 \notin B$. So $f$ is a bijection, and since $|X - \{x_1\}| = n - 1$ the addition principle gives the identity.

^pf-12-8

*Uses:* [[§10 Counting#^thm-10-4|§10.4]], [[§12★ Counting Functions and Subsets#^def-12-5|Def. §12.5]]

> [!remark] Remark: Pascal's Triangle
> This rule gives an inductive way to compute binomial coefficients. It seems to have been found in China by the end of the eleventh century, and is known in the West after Blaise Pascal (1623–1662), who linked the binomial coefficients with probability. Write the numbers $\binom{n}{r}$, $r = 0, 1, \ldots, n$, in row $n$ of a triangle. By Proposition [[§12★ Counting Functions and Subsets#^prop-12-6|§12.6]] the border consists of $1$s, and by Pascal's rule each inner entry is the sum of the two entries above it.

^rem-12-1

![[m250-12-1.svg]]
*Rows $0$ to $7$ of Pascal's triangle. The border entries $\binom{n}{0} = \binom{n}{n} = 1$ are blue; the red entries show Pascal's rule $\binom52 + \binom53 = \binom63$, $10 + 10 = 20$. Each row is symmetric ($\binom{n}{r} = \binom{n}{n-r}$) and sums to $2^n$.*

The triangle is not a convenient way to find a single coefficient; there is an explicit formula.

> [!theorem] Theorem §12.9: The Formula for Binomial Coefficients
> For non-negative integers $n$ and $r$ with $r \le n$,
>
> $$
> \binom{n}{r} = \frac{n(n-1)\cdots(n-r+1)}{r!} = \frac{n!}{r!\,(n-r)!}.
> $$
>
> *Eccles: Theorem 12.2.10*

^thm-12-9

> [!remark] Remark: Why the Formula Is True
> The induction proof below is the simplest to write out, but it does not explain the formula. A better reason: for $r > 0$, an $r$-subset $A$ of an $n$-set $X$ can be specified by listing its elements, that is, by an injection $f : \N_r \to X$ with image $A$. So $\phi : \operatorname{Inj}(\N_r, X) \to \mathcal{P}_r(X)$, $\phi(f) = \operatorname{Im} f$, is a surjection; it is not injective, since the elements of $A$ can be listed in many orders. The listings of a given $A$ are the elements of $\operatorname{Inj}(\N_r, A)$, and there are $r!$ of them. Since $|\operatorname{Inj}(\N_r, X)| = n!/(n-r)!$ (Proposition [[§12★ Counting Functions and Subsets#^prop-12-2|§12.2]]) and each $A$ has $r!$ preimages, $|\mathcal{P}_r(X)| = n!/(r!\,(n-r)!)$. (Making "each $A$ has $r!$ preimages, so divide" precise is an application of Corollary [[§10 Counting#^cor-10-5|§10.5]] to the disjoint preimages $\phi^{-1}(A)$.)

^rem-12-2

> [!proof]+ Proof
> Induction on $n$, the statement being the formula for all $r$ with $0 \le r \le n$.
>
> *Base case $n = 0$.* Then $r = 0$, and $\binom00 = 1 = 0!/(0!\,0!)$ by Proposition [[§12★ Counting Functions and Subsets#^prop-12-6|§12.6]] (recall $0! = 1$).
>
> *Inductive step.* Suppose the formula holds for $n = k \ge 0$. For $r = 0$ and $r = k + 1$, $\binom{k+1}{r} = 1 = (k+1)!/(r!\,(k+1-r)!)$ by Proposition [[§12★ Counting Functions and Subsets#^prop-12-6|§12.6]]. For $1 \le r \le k$, Pascal's rule and the inductive hypothesis give
>
> $$
> \begin{aligned}
> \binom{k+1}{r} &= \binom{k}{r-1} + \binom{k}{r} = \frac{k!}{(r-1)!\,(k-r+1)!} + \frac{k!}{r!\,(k-r)!} \\
> &= \frac{k!\, r}{r!\,(k-r+1)!} + \frac{k!\,(k-r+1)}{r!\,(k-r+1)!} = \frac{k!\,(r + k - r + 1)}{r!\,(k-r+1)!} = \frac{(k+1)!}{r!\,(k+1-r)!}.
> \end{aligned}
> $$
>
> This is the formula for $n = k + 1$.

^pf-12-9

*Uses:* [[§12★ Counting Functions and Subsets#^prop-12-8|§12.8]], [[§12★ Counting Functions and Subsets#^prop-12-6|§12.6]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (induction from $0$), [[§5 The Induction Principle#^def-5-4|Def. §5.4]]

> [!example] Example §12.3: Cards
> Three people each select a different card from a pack of $52$ distinct cards. If we record who selected which card, a selection is an injection from the set of three people to the pack: there are $(52)_3 = 52 \times 51 \times 50 = 132600$ possibilities. If we forget who selected which card, a selection is a $3$-subset of the pack: there are $\binom{52}{3} = \frac{52 \times 51 \times 50}{3!} = 22100$, each unordered selection arising from $3! = 6$ ordered ones.
>
> *Eccles: Exercise 12.3*

^ex-12-3

*Uses:* [[§12★ Counting Functions and Subsets#^prop-12-2|§12.2]], [[§12★ Counting Functions and Subsets#^thm-12-9|§12.9]]

## 12.3 The Binomial Theorem

A **binomial** is a sum of two terms, such as $a + b$. The binomial coefficients are named for their role in removing the brackets from $(a + b)^n$.

> [!theorem] Theorem §12.10: The Binomial Theorem
> For all real numbers $a$ and $b$ and non-negative integers $n$,
>
> $$
> (a + b)^n = \sum_{i=0}^n \binom{n}{i} a^{n-i} b^i = a^n + \cdots + \binom{n}{i} a^{n-i} b^i + \cdots + b^n.
> $$
>
> *Eccles: Theorem 12.3.1*

^thm-12-10

> [!proof]+ Proof
> We use the convention $x^0 = 1$ for every real $x$, including $x = 0$ ([[§5 The Induction Principle#^def-5-3|Definition §5.3]]). Induction on $n$; let $P(n)$ be the statement for all $a, b$.
>
> *Base case.* $P(0)$ reads $(a + b)^0 = \binom00 a^0 b^0$, true since both sides are $1$.
>
> *Inductive step.* Suppose $P(k)$. Then for all $a$ and $b$
>
> $$
> \begin{aligned}
> (a + b)^{k+1} &= (a + b)^k (a + b) = \sum_{i=0}^k \binom{k}{i} a^{k-i} b^i (a + b) \\
> &= \sum_{i=0}^k \binom{k}{i} a^{k+1-i} b^i + \sum_{i=0}^k \binom{k}{i} a^{k-i} b^{i+1} \\
> &= \sum_{i=0}^k \binom{k}{i} a^{k+1-i} b^i + \sum_{i=1}^{k+1} \binom{k}{i-1} a^{k+1-i} b^{i} \qquad (\text{writing } i \text{ for } i + 1) \\
> &= a^{k+1} + \sum_{i=1}^k \left[ \binom{k}{i} + \binom{k}{i-1} \right] a^{k+1-i} b^i + b^{k+1} \qquad \left(\tbinom{k}{0} = \tbinom{k}{k} = 1\right) \\
> &= a^{k+1} + \sum_{i=1}^k \binom{k+1}{i} a^{k+1-i} b^i + b^{k+1} = \sum_{i=0}^{k+1} \binom{k+1}{i} a^{k+1-i} b^i,
> \end{aligned}
> $$
>
> using Pascal's rule in the last line. This is $P(k+1)$.

^pf-12-10

*Uses:* [[§12★ Counting Functions and Subsets#^prop-12-8|§12.8]], [[§12★ Counting Functions and Subsets#^prop-12-6|§12.6]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (induction from $0$), [[§5 The Induction Principle#^def-5-3|Def. §5.3]]

> [!remark]- Connections
> - Computational version: [[§3 Further Algebraic Properties#^thm-3-4|342 Thm. §3.4]] (the binomial formula for complex numbers, proved by the same induction).

The same proof works for complex $a$ and $b$. For negative or non-integer exponents there are versions in which the finite sum becomes an infinite series (Newton).

> [!example] Example §12.4: Reading Expansions off Pascal's Triangle
> $$
> \begin{aligned}
> (a + b)^2 &= a^2 + 2ab + b^2, \\
> (a + b)^3 &= a^3 + 3a^2 b + 3ab^2 + b^3, \\
> (a + b)^7 &= a^7 + 7a^6 b + 21 a^5 b^2 + 35 a^4 b^3 + 35 a^3 b^4 + 21 a^2 b^5 + 7ab^6 + b^7.
> \end{aligned}
> $$
>
> *Eccles: Examples 12.3.2*

^ex-12-4

> [!theorem] Corollary §12.11: The Row Sum Again
> $$
> \sum_{i=0}^n \binom{n}{i} = 2^n.
> $$
>
> *Eccles: Corollary 12.3.3*

^cor-12-11

> [!proof]+ Proof
> Put $a = b = 1$ in the binomial theorem. This is a second proof of Proposition [[§12★ Counting Functions and Subsets#^prop-12-7|§12.7]]. Putting $a = 1$, $b = -1$ instead gives $\sum_{i=0}^n (-1)^i \binom{n}{i} = 0$ for $n \ge 1$, the identity behind the inclusion–exclusion principle ([[§10 Counting#^thm-10-9|Theorem §10.9]]).

^pf-12-11

*Uses:* [[§12★ Counting Functions and Subsets#^thm-12-10|§12.10]]

> [!example] Example §12.5: Derangements
> A **derangement** of $\N_n$ is a permutation $f$ of $\N_n$ with no fixed point: $f(i) \ne i$ for all $i$. The number of derangements is
>
> $$
> D_n = n! \sum_{j=0}^n \frac{(-1)^j}{j!} = n!\left( \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!} \right).
> $$
>
> Let $A_i$ be the set of permutations fixing $i$. For $\emptyset \ne I \subseteq \N_n$, the permutations fixing every $i \in I$ correspond bijectively to the permutations of $\N_n - I$: such an $f$ maps $\N_n - I$ into itself (if $x \notin I$ and $f(x) = i \in I$, then $f(x) = f(i)$ forces $x = i$), injectively, hence bijectively by [[§11 Properties of Finite Sets#^thm-11-7|Theorem §11.7]]; conversely a permutation of $\N_n - I$ extends by the identity on $I$. So $|A_I| = (n - |I|)!$ by Corollary [[§12★ Counting Functions and Subsets#^cor-12-3|§12.3]] (and $|A_{\N_n}| = 1 = 0!$, only the identity). There are $\binom{n}{j}$ sets $I$ with $|I| = j$, so by inclusion–exclusion
>
> $$
> \Bigl| \bigcup_{i=1}^n A_i \Bigr| = \sum_{j=1}^n (-1)^{j-1} \binom{n}{j} (n-j)! = \sum_{j=1}^n (-1)^{j-1} \frac{n!}{j!},
> $$
>
> and $D_n = n! - |\bigcup A_i| = n! \sum_{j=0}^n (-1)^j / j!$; the terms $j = 0, 1$ cancel. For instance $D_4 = 12 - 4 + 1 = 9$. The proportion $D_n / n!$ is a partial sum of the series for $e^{-1}$, so for large $n$ about $1/e$ of all permutations are derangements.
>
> *Eccles: Problems III Q17*

^ex-12-5

*Uses:* [[§10 Counting#^thm-10-9|§10.9]], [[§12★ Counting Functions and Subsets#^cor-12-3|§12.3]], [[§12★ Counting Functions and Subsets#^thm-12-9|§12.9]], [[§11 Properties of Finite Sets#^thm-11-7|§11.7]]
