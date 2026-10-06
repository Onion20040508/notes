---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: 22
eccles: "Ch. 22"
aliases: ["Eccles 22"]
tags: [logic-and-proofs, mat250]
---
← [[§21 Congruence Classes and the Arithmetic of Remainders]] · ↑ [[· 5 Modular Arithmetic]] · [[§23 The Sequence of Prime Numbers]] →

*Eccles, Chapter 22 and Problems V · MAT 200 lecture (syllabus week 13: relations, equivalence relations and partitions, quotient sets, constructions of the integers and rational numbers) · the student's Rational Number Project (MAT 250, Oct 2024) · Sundstrom §7.1–7.3.*

Congruence modulo $m$ can be seen in two ways: as a *relation* between integers, and as a *partition* of $\mathbb{Z}$ into congruence classes, the set $\mathbb{Z}_m$ of [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-2|Def. §21.2]]. This is one instance of a concept met everywhere in pure mathematics: equivalence relations on a set correspond exactly to partitions of it, and the set of classes (the quotient set) is a new object. The last two parts ([[§22a Constructing ℚ and ℤ|§22a]]) use quotient sets to *construct* the number systems that [[§13 Number Systems|§13]] took for granted: $\mathbb{Q}$ from $\mathbb{Z}$ (the Rational Number Project) and $\mathbb{Z}$ from $\mathbb{N}$.

## 22.1 Partitions

> [!definition] Definition §22.1: Partition
> Let $X$ be a set and $\mathcal{P}(X)$ its [[§6 The Language of Set Theory#^def-6-9|power set]], the set of all subsets of $X$. A **partition** of $X$ is a subset $\Pi \subseteq \mathcal{P}(X)$, i.e. a set of subsets of $X$, such that
> 1. the subsets in $\Pi$ are non-empty: $A \in \Pi \Rightarrow A \neq \varnothing$;
> 2. the subsets in $\Pi$ are disjoint: $\forall A_1, A_2 \in \Pi,\ (A_1 \neq A_2 \Rightarrow A_1 \cap A_2 = \varnothing)$;
> 3. the subsets in $\Pi$ cover $X$: $\forall x \in X,\ \exists A \in \Pi,\ x \in A$.
>
> Equivalently, every element of $X$ lies in exactly one member of $\Pi$, and no member is empty.
>
> *Eccles: Definition 22.1.1*

^def-22-1

> [!remark]- Connections
> - [[§24 Equivalence Relations and Partitions#^def-24-3|493 Def. §24.3]] (partition).

> [!example] Example §22.1: Partitions and Non-Partitions
> (a) By Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]], the set of congruence classes $\mathbb{Z}_m = \{[a]_m \mid a \in \mathbb{Z}\} = \{[a]_m \mid a \in R_m\}$ is a partition of $\mathbb{Z}$ into $m$ subsets ([[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-2|Proposition §21.2]]). It is the model for everything in this section.
>
> (b) A set of people is partitioned by year of birth.
>
> (c) $\Pi = \{\{1, 3, 7, 8\}, \{2, 9, 10\}, \{4\}, \{5, 6\}\}$ is a partition of $\{1, 2, \ldots, 10\}$.
>
> (d) $\Pi = \{\mathbb{Z}^+, \{0\}, \mathbb{Z}^-\}$, where $\mathbb{Z}^- = \{n \in \mathbb{Z} \mid n < 0\}$, is a partition of $\mathbb{Z}$.
>
> (e) $\{\{1, 2, 3, 4, 5\}, \{5, 6, 7, 8, 9\}\}$ is *not* a partition of $\{1, \ldots, 9\}$: $5$ lies in both subsets (condition 2 fails).
>
> (f) $\{\{1, 2, 3, 4\}, \{6, 7, 8, 9\}\}$ is *not* a partition of $\{1, \ldots, 9\}$: $5$ lies in neither (condition 3 fails).
>
> *Eccles: Examples 22.1.2*

^ex-22-1

Partitions are usually described by a property of the elements — the remainder in (a), the year of birth in (b) — that is, by the value of a function.

> [!theorem] Proposition §22.1: The Partition by the Values of a Surjection
> Let $f : X \to Y$ be a surjection. Then
>
> $$
> \Pi = \{ \overleftarrow{f}(\{y\}) \mid y \in Y \}, \qquad \overleftarrow{f}(\{y\}) = \{x \in X \mid f(x) = y\},
> $$
>
> is a partition of $X$: $X$ is partitioned according to the value of $f$.
>
> *Eccles: Proposition 22.1.3*

^prop-22-1

> [!proof]+ Proof
> *Non-empty:* given $y \in Y$, since $f$ is surjective there is $x$ with $f(x) = y$, so $x \in \overleftarrow{f}(\{y\})$.
>
> *Disjoint:* if $\overleftarrow{f}(\{y_1\}) \neq \overleftarrow{f}(\{y_2\})$ then $y_1 \neq y_2$; and an $x$ in both would have $f(x) = y_1$ and $f(x) = y_2$, impossible since $f$ has a single value at $x$.
>
> *Cover:* each $x \in X$ lies in $\overleftarrow{f}(\{f(x)\})$, because $f$ has a value at every point of $X$.

^pf-22-1

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-1|Def. §22.1]], [[§9 Injections, Surjections and Bijections#^def-9-new1|Def. §9.1]], [[§9 Injections, Surjections and Bijections#^def-9-new3|Def. §9.4]]

> [!example] Example §22.2: Partitions Given by Functions
> (a) The partition of $\mathbb{Z}$ into congruence classes modulo $m$ comes from the remainder map $r_m : \mathbb{Z} \to R_m$: its parts are $\overleftarrow{r_m}(\{r\}) = [r]_m$ (the box model of the remark after [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|Proposition §21.1]]).
>
> (b) The partition $\{\mathbb{Z}^+, \{0\}, \mathbb{Z}^-\}$ of [[§22 Partitions and Equivalence Relations#^ex-22-1|Example §22.1]](d) comes from the sign function
>
> $$
> f : \mathbb{Z} \to \{-1, 0, 1\}, \qquad f(x) = \begin{cases} x/|x| & \text{if } x \neq 0, \\ 0 & \text{if } x = 0. \end{cases}
> $$
>
> (c) Conversely the relation "same part" for this partition is $a \sim b \iff ab > 0$ or $a = b = 0$.
>
> *Eccles: Examples 22.1.4, Exercise 22.2*

^ex-22-2

## 22.2 Equivalence Relations

A partition starts from the whole set. The same idea seen from the elements: if a set of people is partitioned into rooms, nobody need know the overall picture, but everyone can see who is in the same room. So a partition determines a *relation*: two elements are related if they lie in the same part.

> [!definition] Definition §22.2: Relation
> A **relation** on a set $X$ is determined by a property that each [[§7 Quantifiers#^def-7-new1|ordered pair]] $(a, b) \in X \times X$ may or may not satisfy. If $(a, b)$ satisfies it we say $a$ and $b$ are **related** and write $a \sim b$; otherwise we write $a \not\sim b$. Formally, a relation on $X$ *is* the subset $R = \{(a, b) \in X \times X \mid a \sim b\}$ of $X \times X$, and $a \sim b$ means $(a, b) \in R$.
>
> *Eccles: §22.2 (text before Proposition 22.2.1)*
> *Source: Sundstrom §7.1 (relation as a subset of $A \times A$)*

^def-22-2

> [!theorem] Proposition §22.2: A Partition Gives a Relation
> Let $\Pi$ be a partition of $X$. For $a, b \in X$ let $a \sim_\Pi b$ if and only if $a$ and $b$ belong to the same subset of the partition. Then:
> 1. *Reflexive:* $a \sim_\Pi a$ for all $a \in X$.
> 2. *Symmetric:* if $a \sim_\Pi b$, then $b \sim_\Pi a$.
> 3. *Transitive:* if $a \sim_\Pi b$ and $b \sim_\Pi c$, then $a \sim_\Pi c$.
>
> *Eccles: Proposition 22.2.1*

^prop-22-2

> [!proof]+ Proof
> (1) Each $a \in X$ lies in some $A \in \Pi$ (the parts cover $X$), so $a \sim_\Pi a$. (2) "$a$ and $b$ lie in a common part" is symmetric in $a$ and $b$. (3) Suppose $a, b \in A_1$ and $b, c \in A_2$ with $A_1, A_2 \in \Pi$. Then $b \in A_1 \cap A_2$, so these parts are not disjoint, and hence $A_1 = A_2$ (condition 2 of Definition [[§22 Partitions and Equivalence Relations#^def-22-1|§22.1]], contrapositive). So $a, c \in A_1$ and $a \sim_\Pi c$.

^pf-22-2

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-1|Def. §22.1]], [[§22 Partitions and Equivalence Relations#^def-22-2|Def. §22.2]]

Compare Proposition [[§19 Congruence of Integers#^prop-19-1|§19.1]]: starting from the partition $\mathbb{Z}_m$, this produces congruence modulo $m$.

> [!definition] Definition §22.3: Reflexive, Symmetric, Transitive
> Let $\sim$ be a relation on a set $X$. It is
> 1. **reflexive** when $x \sim x$ for all $x \in X$;
> 2. **symmetric** when, for all $x, y \in X$, $\ x \sim y \Rightarrow y \sim x$;
> 3. **transitive** when, for all $x, y, z \in X$, $\ x \sim y$ and $y \sim z \Rightarrow x \sim z$.
>
> *Eccles: Definition 22.2.3*

^def-22-3

> [!definition] Definition §22.3: Equivalence Relation
> An **equivalence relation** on $X$ is a relation that is reflexive, symmetric and transitive.
>
> *Eccles: Definition 22.2.3*

^def-22-new1

> [!remark]- Connections
> - [[§24 Equivalence Relations and Partitions#^def-24-1|493 Def. §24.1]] (equivalence relation); a non-arithmetic example, $x - y \in \mathbb{Q}$ on $[0,1]$, behind the [[The Vitali Set is Not Measurable|Vitali set]]: [[§11 Borel Sets and Measure Spaces#^def-11-10|551 Def. §11.10]].

Each property is a universal statement, so to show that one *fails* a single counterexample suffices.

> [!example] Example §22.3: Which Properties Hold?
> | relation | reflexive | symmetric | transitive |
> |---|---|---|---|
> | $a \leq b$ on $\mathbb{Z}$ | yes | no: $1 \leq 2$, $2 \not\leq 1$ | yes |
> | $a < b$ on $\mathbb{Z}$ | no: $1 \not< 1$ | no: $1 < 2$, $2 \not< 1$ | yes |
> | $a = b$ on $\mathbb{Z}$ | yes | yes | yes |
> | $ab > 0$ on $\mathbb{Z}$ | no: $0 \cdot 0 = 0$ | yes: $ab = ba$ | yes |
> | $ab = 0$ on $\mathbb{Z}$ | no: $1 \cdot 1 \neq 0$ | yes | no: $1 \sim 0$, $0 \sim 1$, $1 \not\sim 1$ |
> | $a_1 b_2 = a_2 b_1$ on $\mathbb{Z} \times (\mathbb{Z} - \{0\})$ | yes | yes | yes |
> | $a \equiv b \pmod m$ on $\mathbb{Z}$ | yes | yes | yes |
>
> Transitivity of $ab > 0$: if $ab > 0$ and $bc > 0$ then $ab^2c = (ab)(bc) > 0$, and $b^2 > 0$ (as $b \neq 0$), so $ac > 0$. The equivalence relations are $=$, congruence modulo $m$ (Proposition [[§19 Congruence of Integers#^prop-19-1|§19.1]]), and the relation on pairs, proved in [[§22 Partitions and Equivalence Relations#^lem-22-6|Lemma §22.6]] below, in §22a; more generally $\sim_\Pi$ for any partition $\Pi$ ([[§22 Partitions and Equivalence Relations#^prop-22-2|Proposition §22.2]]).
>
> *Eccles: Examples 22.2.2, 22.2.4*

^ex-22-3

> [!example] Example §22.4: Describing the Classes
> For each relation: which properties hold, and, for equivalence relations, what are the classes?
>
> | $X$ | $a \sim b \iff$ | R | S | T | classes |
> |---|---|---|---|---|---|
> | $\mathbb{Z}$ | $a + b$ even | yes | yes | yes | the evens, the odds (this is congruence mod $2$: $a + b$ and $a - b$ differ by $2b$) |
> | $\mathbb{Z}$ | $a + b$ odd | no ($0 + 0$) | yes | no ($0 \sim 1 \sim 0$, $0 \not\sim 0$) | — |
> | $\mathbb{Z}$ | $3 \mid a + b$ | no ($1 + 1$) | yes | no ($1 \sim 2 \sim 1$, $1 \not\sim 1$) | — |
> | $\mathbb{Z}$ | $a^2 = b^2$ | yes | yes | yes | $\{0\}, \{1, -1\}, \{2, -2\}, \ldots$ |
> | $\{1, 2\}$ | $a = 1$ and $b = 1$ | no ($2 \not\sim 2$) | yes | yes | — |
> | $\{1, 2\}$ | $a = 1$ or $b = 1$ | no ($2 \not\sim 2$) | yes | no ($2 \sim 1 \sim 2$, $2 \not\sim 2$) | — |
> | $\mathbb{R} \times \mathbb{R}$ | $a_1 = b_1$ | yes | yes | yes | vertical lines $\{a_1\} \times \mathbb{R}$ |
> | $\mathbb{R} \times \mathbb{R}$ | $a_1^2 + a_2^2 = b_1^2 + b_2^2$ | yes | yes | yes | circles centred at the origin, and $\{(0,0)\}$ |
>
> (Here $a = (a_1, a_2)$, $b = (b_1, b_2)$ in the last two rows.) The fifth row shows that reflexivity does *not* follow from symmetry and transitivity: the tempting argument "$x \sim y \Rightarrow y \sim x \Rightarrow x \sim x$" needs some $y$ with $x \sim y$, and $2$ is related to nothing.
>
> *Eccles: Exercise 22.1*

^ex-22-4

## 22.3 Equivalence Relations and Partitions

In [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-2|Def. §21.2]] the partition $\mathbb{Z}_m$ was built from the relation of congruence. The construction works for every equivalence relation.

> [!definition] Definition §22.4: Equivalence Class
> Let $\sim$ be an equivalence relation on a non-empty set $X$. For $a \in X$, the **equivalence class of $a$** is the set of elements equivalent to $a$:
>
> $$
> [a] = \{ x \in X \mid x \sim a \} \subseteq X .
> $$
>
> *Eccles: Definition 22.3.1*

^def-22-4

> [!remark]- Connections
> - [[§24 Equivalence Relations and Partitions#^def-24-2|493 Def. §24.2]] (equivalence class); [[§11 Borel Sets and Measure Spaces#^def-11-11|551 Def. §11.11]].

> [!definition] Definition §22.4: Quotient Set
> The set of all equivalence classes is denoted $X/{\sim}$ (the **quotient set**, "$X$ modulo $\sim$"):
>
> $$
> X/{\sim} = \{ [a] \mid a \in X \} \subseteq \mathcal{P}(X) .
> $$
>
> The main example: for congruence modulo $m$ on $\mathbb{Z}$ the equivalence classes are the congruence classes $[a] = [a]_m$ ([[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-1|Def. §21.1]]) and $\mathbb{Z}/{\equiv} = \mathbb{Z}_m$ ([[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-2|Def. §21.2]]).
>
> *Eccles: Definition 22.3.1*

^def-22-new2

The next theorem generalizes Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]] with the same proof, each property of congruence replaced by the corresponding axiom.

> [!theorem] Theorem §22.3: Classes Are Equal or Disjoint
> Let $\sim$ be an equivalence relation on $X$. For $a, b \in X$:
> 1. $a \sim b \iff [a] = [b]$;
> 2. $a \not\sim b \iff [a] \cap [b] = \varnothing$.
>
> *Eccles: Theorem 22.3.2*

^thm-22-3

> [!proof]+ Proof
> (1) ($\Rightarrow$) Let $a \sim b$. Then $x \in [a] \Rightarrow x \sim a \Rightarrow x \sim b$ (transitivity) $\Rightarrow x \in [b]$, so $[a] \subseteq [b]$. Since $a \sim b \Rightarrow b \sim a$ (symmetry), likewise $[b] \subseteq [a]$; so $[a] = [b]$.
> ($\Leftarrow$) Let $[a] = [b]$. Since $a \in [a]$ (reflexivity), $a \in [b]$, i.e. $a \sim b$.
>
> (2) ($\Rightarrow$) Let $a \not\sim b$ and suppose for contradiction that $[a] \cap [b] \neq \varnothing$; choose $x_0 \in [a] \cap [b]$. Then $x_0 \sim a$ and $x_0 \sim b$, so $a \sim x_0$ (symmetry) and $x_0 \sim b$, so $a \sim b$ (transitivity), contradicting the hypothesis. Hence $[a] \cap [b] = \varnothing$.
> ($\Leftarrow$) Let $[a] \cap [b] = \varnothing$ and suppose for contradiction that $a \sim b$. Then $a \in [a]$ (reflexivity) and $a \in [b]$, so $a \in [a] \cap [b] \neq \varnothing$, a contradiction. Hence $a \not\sim b$.

^pf-22-3

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-3|Def. §22.3]], [[§22 Partitions and Equivalence Relations#^def-22-new1|Def. §22.3]], [[§22 Partitions and Equivalence Relations#^def-22-4|Def. §22.4]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

> [!remark]- Connections
> - [[§24 Equivalence Relations and Partitions#^prop-24-1|493 Prop. §24.1]] (equivalence classes partition a set), applied to cosets in [[Cosets Partition a Group]].

> [!theorem] Corollary §22.4: Equivalence Relations Are Partitions
> Let $\sim$ be an equivalence relation on a non-empty set $X$. Then $\Pi = X/{\sim}$ is a partition of $X$, and the relation $\sim_\Pi$ arising from it (Proposition [[§22 Partitions and Equivalence Relations#^prop-22-2|§22.2]]) is $\sim$. Conversely, for any partition $\Pi$ of $X$, the classes of $\sim_\Pi$ are exactly the members of $\Pi$: $X/{\sim_\Pi} = \Pi$.
>
> So $\sim \;\mapsto X/{\sim}$ and $\Pi \mapsto \;\sim_\Pi$ are mutually inverse: equivalence relations on $X$ and partitions of $X$ are two descriptions of the same thing.
>
> *Eccles: Corollary 22.3.3*
> *Source: Sundstrom §7.3 Exercise 12 (the converse half)*

^cor-22-4

> [!proof]+ Proof
> *$X/{\sim}$ is a partition.* Its members are non-empty, since each is $[a]$ for some $a$ and $a \in [a]$ (reflexivity). They cover $X$, since $x \in [x]$. Distinct classes are disjoint: if $[a] \neq [b]$ then $a \not\sim b$ by Theorem [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]](1), so $[a] \cap [b] = \varnothing$ by §22.3(2).
>
> *$\sim_\Pi = \;\sim$.* By definition, $a \sim_\Pi b$ iff $a$ and $b$ lie in a common class $[c]$. If $a \sim b$, both lie in $[b]$. Conversely if $a, b \in [c]$, then $a \sim c$ and $b \sim c$, so $a \sim b$. (This is Theorem §22.3(1) in another form.)
>
> *$X/{\sim_\Pi} = \Pi$.* Let $a \in X$ and let $A$ be the member of $\Pi$ containing $a$ (exactly one, by Definition [[§22 Partitions and Equivalence Relations#^def-22-1|§22.1]]). Then $x \sim_\Pi a$ iff $x$ lies in the part containing $a$, i.e. $x \in A$; so the class of $a$ under $\sim_\Pi$ is $A$. Every class is thus a member of $\Pi$, and every member $A \in \Pi$ is non-empty, hence the class of any of its elements.

^pf-22-4

*Uses:* [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]], [[§22 Partitions and Equivalence Relations#^prop-22-2|§22.2]], [[§22 Partitions and Equivalence Relations#^def-22-1|Def. §22.1]], [[§22 Partitions and Equivalence Relations#^def-22-4|Def. §22.4]], [[§22 Partitions and Equivalence Relations#^def-22-new1|Def. §22.3]], [[§22 Partitions and Equivalence Relations#^def-22-new2|Def. §22.4]]

> [!remark]- Connections
> - [[§24 Equivalence Relations and Partitions#^prop-24-2|493 Prop. §24.2]] (partitions come from equivalence relations).

A surjection $f : X \to Y$ partitions $X$ (Proposition [[§22 Partitions and Equivalence Relations#^prop-22-1|§22.1]]); in the language of equivalence relations this becomes:

> [!theorem] Proposition §22.5: A Surjection Induces a Bijection on the Quotient
> Let $f : X \to Y$ be a surjection, and define an equivalence relation on $X$ by $x_1 \sim x_2 \iff f(x_1) = f(x_2)$. Then $f$ induces a bijection
>
> $$
> F : X/{\sim} \to Y, \qquad F([x]) = f(x) .
> $$
>
> *Eccles: Proposition 22.3.4*

^prop-22-5

> [!proof]+ Proof
> The relation is an equivalence relation because $=$ on $Y$ is one. *$F$ is well defined:* its formula uses a representative $x$ of the class, and if $[x_1] = [x_2]$ then $x_1 \sim x_2$ (Theorem [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]]), i.e. $f(x_1) = f(x_2)$. *Surjective:* every $y \in Y$ is $f(x) = F([x])$ for some $x$, as $f$ is surjective. *Injective:*
>
> $$
> F([x_1]) = F([x_2]) \Rightarrow f(x_1) = f(x_2) \Rightarrow x_1 \sim x_2 \Rightarrow [x_1] = [x_2] .
> $$
>
> So $F$ is a bijection.

^pf-22-5

*Uses:* [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]], [[§22 Partitions and Equivalence Relations#^def-22-4|Def. §22.4]], [[§22 Partitions and Equivalence Relations#^def-22-new2|Def. §22.4]], [[§9 Injections, Surjections and Bijections#^def-9-1|Def. §9.1]], [[§9 Injections, Surjections and Bijections#^def-9-new1|Def. §9.1]], [[§9 Injections, Surjections and Bijections#^def-9-new2|Def. §9.1]]

> [!remark]- Connections
> - The group version: [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]] (first isomorphism theorem); defining maps on $\mathbb{Z}_n$ by representatives: [[§7 The Group ℤ∕nℤ#^lem-7-2|493 Lemma §7.2]]; the topological version: [[Universal Property of Quotient Maps]].

The proof contains the general principle for defining functions on a quotient set: a rule $[x] \mapsto g(x)$, computed from a representative, defines a function $X/{\sim} \to Z$ exactly when $x \sim x' \Rightarrow g(x) = g(x')$. Otherwise it is not *well defined*.

> [!example] Example §22.5: Well-Defined or Not?
> (a) Which formulas define a function $f : \mathbb{Z}_6 \to \mathbb{Z}_4$? Here $[a]_6 = [a']_6$ means $a' = a + 6k$ for some $k \in \mathbb{Z}$.
> - $f([a]_6) = [a + 1]_4$: **not** well defined. $[0]_6 = [6]_6$, but $[1]_4 \neq [7]_4 = [3]_4$.
> - $f([a]_6) = [2a]_4$: well defined, since $2a' - 2a = 12k = 4 \cdot 3k$.
> - $f([a]_6) = [a^2]_4$: well defined, since $a'^2 - a^2 = 12ak + 36k^2 = 4(3ak + 9k^2)$.
>
> (b) Which formulas define a function $f : \mathbb{Q} \to \mathbb{Q}$? Here $a/b = c/d$ means $ad = bc$ ([[§13 Number Systems#^prop-13-1|Proposition §13.1]]).
> - $f(a/b) = a^2/b^2$: well defined, since $ad = bc \Rightarrow a^2 d^2 = b^2 c^2$.
> - $f(a/b) = a^2/b^3$: **not**: $1/1 = 2/2$, but $1/1 \neq 4/8$.
> - $f(a/b) = b/a$: **not** a function on $\mathbb{Q}$: $0 = 0/1$ would go to $1/0$, which is not a fraction. (On $\mathbb{Q} - \{0\}$ it is well defined: $ad = bc \Rightarrow da = cb$.)
> - $f(a/b) = a + b$: **not**: $1/1 = 2/2$, but $2 \neq 4$.
> - $f(a/b) = (a - b)/2b$: well defined, since $ad = bc$ gives $(a - b)(2d) = 2ad - 2bd = 2bc - 2bd = (2b)(c - d)$.
>
> *Eccles: Problems V Q18, Q19*

^ex-22-5

> [!example] Example §22.6: Fractions and Rational Numbers
> Define $f : \mathbb{Z} \times (\mathbb{Z} - \{0\}) \to \mathbb{Q}$ by $f(a, b) = a/b$. Then
>
> $$
> f(a_1, b_1) = f(a_2, b_2) \iff a_1/b_1 = a_2/b_2 \iff a_1 b_2 = a_2 b_1 ,
> $$
>
> so the equivalence relation induced by $f$ as in Proposition [[§22 Partitions and Equivalence Relations#^prop-22-5|§22.5]] is the relation on pairs of [[§22 Partitions and Equivalence Relations#^ex-22-3|Example §22.3]], and $f$ (surjective, as every rational is a fraction) induces a bijection
>
> $$
> F : \bigl(\mathbb{Z} \times (\mathbb{Z} - \{0\})\bigr)/{\sim} \;\to\; \mathbb{Q} .
> $$
>
> This makes precise the relation between fractions and rationals of [[§13 Number Systems#^prop-13-1|Proposition §13.1]]: a fraction is a pair $(a, b)$ written $a/b$, and two fractions represent the same rational iff $a_1 b_2 = a_2 b_1$.
>
> *Eccles: Example 22.3.5*

^ex-22-6

The constructions of $\mathbb{Q}$ and $\mathbb{Z}$ from quotient sets continue in [[§22a Constructing ℚ and ℤ]].
