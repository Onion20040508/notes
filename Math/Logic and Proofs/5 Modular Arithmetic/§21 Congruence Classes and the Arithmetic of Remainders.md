---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: 21
eccles: "Ch. 21"
aliases: ["Eccles 21"]
tags: [logic-and-proofs, mat250]
---
← [[§20 Linear Congruences]] · ↑ [[· 5 Modular Arithmetic]] · [[§22 Partitions and Equivalence Relations]] →

*Eccles, Chapter 21 · MAT 200 lecture (syllabus weeks 11–12: congruence classes, operations on congruence classes). No homework survives for this chapter.*

Instead of saying that integers are *congruent*, we can say that their *congruence classes are equal*: the set of all even integers replaces "an even integer". This is a typical step of abstraction, and it pays: there are only $m$ classes, so counting arguments such as the pigeonhole principle ([[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]]) apply, and the classes can be added and multiplied, giving an *arithmetic of remainders* (Dedekind, 1857). As an application, Theorem [[§20 Linear Congruences#^thm-20-4|§20.4]] gets a second proof that makes it look almost obvious. Throughout, $m$ is a fixed positive integer.

## 21.1 Congruence Classes

> [!definition] Definition §21.1: Congruence Class
> Given an integer $a$, the **congruence class of $a$ modulo $m$** is the set of integers congruent to $a$ modulo $m$, denoted $[a]_m$:
>
> $$
> [a]_m = \{ x \in \mathbb{Z} \mid x \equiv a \pmod m \} = \{ a + mq \mid q \in \mathbb{Z} \} .
> $$
>
> *Eccles: Definition 21.1.1*

^def-21-1

> [!example] Example §21.1: Classes Modulo 2 and Modulo 6
> (a) Modulo $2$ there are just two classes, the even and the odd integers:
>
> $$
> \begin{aligned}
> [0]_2 &= \{\ldots, -4, -2, 0, 2, 4, \ldots\} = \{2q \mid q \in \mathbb{Z}\} = [2]_2 = [-16]_2, \\
> [1]_2 &= \{\ldots, -3, -1, 1, 3, 5, \ldots\} = \{2q + 1 \mid q \in \mathbb{Z}\} = [3]_2 = [-53]_2 .
> \end{aligned}
> $$
>
> (b) Modulo $6$ there are six: $[r]_6 = \{6q + r \mid q \in \mathbb{Z}\}$ for $r = 0, 1, \ldots, 5$; for instance $[0]_6 = [36]_6 = [-594]_6$ and $[1]_6 = [49]_6$. Listing the integers in rows of six, the columns are the six classes:
>
> | $[0]_6$ | $[1]_6$ | $[2]_6$ | $[3]_6$ | $[4]_6$ | $[5]_6$ |
> |---|---|---|---|---|---|
> | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
> | $-12$ | $-11$ | $-10$ | $-9$ | $-8$ | $-7$ |
> | $-6$ | $-5$ | $-4$ | $-3$ | $-2$ | $-1$ |
> | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ |
> | $12$ | $13$ | $14$ | $15$ | $16$ | $17$ |
> | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
>
> *Eccles: Examples 21.1.2*

^ex-21-1

These examples show the classes modulo $m$ *partitioning* $\mathbb{Z}$: two classes are either equal or disjoint. To prove $[a]_m = [b]_m$ is to prove an equality of subsets, $x \in [a]_m \iff x \in [b]_m$, i.e. $x \equiv a \iff x \equiv b \pmod m$. The statements $[a]_m \cap [b]_m = \varnothing$ (non-existence) and $a \not\equiv b$ (negative) suggest proof by contradiction for both directions of (2).

> [!theorem] Proposition §21.1: Congruence Classes Are Equal or Disjoint
> For integers $a, b$:
> 1. $a \equiv b \pmod m \iff [a]_m = [b]_m$;
> 2. $a \not\equiv b \pmod m \iff [a]_m \cap [b]_m = \varnothing$.
>
> Thus two congruence classes modulo $m$ are either equal or disjoint.
>
> *Eccles: Proposition 21.1.3*

^prop-21-1

> [!proof]+ Proof
> (1) ($\Rightarrow$) Let $a \equiv b$. If $x \in [a]_m$, then $x \equiv a$ and $a \equiv b$, so $x \equiv b$ by transitivity, i.e. $x \in [b]_m$. So $[a]_m \subseteq [b]_m$; since also $b \equiv a$ (symmetry), the same argument gives $[b]_m \subseteq [a]_m$. Hence $[a]_m = [b]_m$.
>
> ($\Leftarrow$) Let $[a]_m = [b]_m$. Since $a \equiv a$, $\ a \in [a]_m = [b]_m$, i.e. $a \equiv b$.
>
> (2) ($\Rightarrow$) Let $a \not\equiv b$, and suppose for contradiction that $[a]_m \cap [b]_m \neq \varnothing$. Choose $x_0 \in [a]_m \cap [b]_m$. Then $x_0 \equiv a$ and $x_0 \equiv b$, so $a \equiv x_0 \equiv b$, contradicting the hypothesis. Hence $[a]_m \cap [b]_m = \varnothing$.
>
> ($\Leftarrow$) Let $[a]_m \cap [b]_m = \varnothing$, and suppose for contradiction that $a \equiv b$. Then $a \in [a]_m$ and $a \in [b]_m$, so $a \in [a]_m \cap [b]_m \neq \varnothing$, a contradiction. Hence $a \not\equiv b$.

^pf-21-1

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-1|Def. §21.1]], [[§19 Congruence of Integers#^prop-19-1|§19.1]]

> [!remark]- Connections
> - Residue classes in group theory: [[§6 Divisibility and Congruence#^def-6-4|493 Def. §6.4]]; the general statement for any equivalence relation is [[§22 Partitions and Equivalence Relations#^thm-22-3|Theorem §22.3]] here, and [[§24 Equivalence Relations and Partitions#^prop-24-1|493 Prop. §24.1]].

> [!remark] Remark: The Box Model of the Remainder Map
> Picture the remainder map $r_m : \mathbb{Z} \to R_m$ ([[§19 Congruence of Integers#^def-19-3|Def. §19.3]]) as $m$ boxes labelled $0, 1, \ldots, m - 1$, each integer dropped into the box of its remainder (the box model of a function, [[§8 Functions#^ex-8-1|Example §8.1]]). The contents of box $r$ form the pre-image ([[§9 Injections, Surjections and Bijections#^def-9-7|Def. §9.7]])
>
> $$
> \overleftarrow{r_m}(\{r\}) = \{x \in \mathbb{Z} \mid r_m(x) = r\} = [r]_m ,
> $$
>
> by Proposition [[§19 Congruence of Integers#^prop-19-5|§19.5]] (as $r_m(r) = r$). So the boxes are the classes, the columns of the table in [[§21 Congruence Classes and the Arithmetic of Remainders#^ex-21-1|Example §21.1]](b) for $m = 6$, or the columns of a calendar for $m = 7$. For any integer $a$, $\ [a]_m = [r]_m$ iff $r_m(a) = r$; in particular $[a]_m = [r_m(a)]_m$.
>
> *Source: Eccles Table 21.1.4*

^rem-21-1

> [!definition] Definition §21.2: The Set $\mathbb{Z}_m$
> We write $\mathbb{Z}_m$ for the set of congruence classes modulo $m$:
>
> $$
> \mathbb{Z}_m = \{ [a]_m \mid a \in \mathbb{Z} \} .
> $$
>
> Note that an *element* of $\mathbb{Z}_m$ is a *subset* of $\mathbb{Z}$.
>
> *Eccles: Definition 21.1.5*

^def-21-2

Each integer $a$ lies in its own class $[a]_m$, and by [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|Proposition §21.1]] two classes are equal or disjoint: so $\mathbb{Z}_m$ is a *partition* of $\mathbb{Z}$ into non-empty, pairwise disjoint sets. This is the model example of [[§22 Partitions and Equivalence Relations|§22]], which defines partitions in general ([[§22 Partitions and Equivalence Relations#^def-22-1|Def. §22.1]]), proves Proposition §21.1 for any equivalence relation ([[§22 Partitions and Equivalence Relations#^thm-22-3|Theorem §22.3]]), and recovers $\mathbb{Z}_m$ as the quotient set $\mathbb{Z}/{\equiv}$ ([[§22 Partitions and Equivalence Relations#^def-22-6|Def. §22.6]]).

> [!theorem] Proposition §21.2: $\mathbb{Z}_m$ Has $m$ Elements
> The set $\mathbb{Z}_m$ is finite of cardinality $m$; its elements are $[r]_m$ for the integers $0 \leq r < m$:
>
> $$
> \mathbb{Z}_m = \{[0]_m, [1]_m, \ldots, [m-1]_m\} .
> $$
>
> *Eccles: Proposition 21.1.6, Exercise 21.6*

^prop-21-2

> [!proof]+ Proof
> Count the boxes from left to right. With the standard set $\mathbb{N}_m = \{1, 2, \ldots, m\}$ of [[§10 Counting#^def-10-1|Def. §10.1]], define
>
> $$
> f : \mathbb{N}_m \to \mathbb{Z}_m, \quad f(i) = [i - 1]_m, \qquad g : \mathbb{Z}_m \to \mathbb{N}_m, \quad g([a]_m) = r_m(a) + 1 .
> $$
>
> *$g$ is well defined:* its formula uses a representative $a$ of the class, so we must check that the value does not depend on the choice. If $[a_1]_m = [a_2]_m$, then $a_1 \equiv a_2$ (Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]]), so $r_m(a_1) = r_m(a_2)$ (Proposition [[§19 Congruence of Integers#^prop-19-5|§19.5]]). Also $r_m(a) + 1 \in \{1, \ldots, m\}$.
>
> *$g \circ f = \mathrm{id}$:* for $i \in \mathbb{N}_m$, $\ i - 1 \in R_m$, so $r_m(i-1) = i - 1$ and $g(f(i)) = i$.
>
> *$f \circ g = \mathrm{id}$:* $f(g([a]_m)) = [r_m(a)]_m = [a]_m$, since $r_m(a) \equiv a$.
>
> So $f$ is a bijection, $|\mathbb{Z}_m| = m$ by definition of cardinality, and $\mathbb{Z}_m = \{f(1), \ldots, f(m)\} = \{[0]_m, \ldots, [m-1]_m\}$.

^pf-21-2

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]], [[§19 Congruence of Integers#^prop-19-5|§19.5]], [[§19 Congruence of Integers#^def-19-3|Def. §19.3]], [[§10 Counting#^def-10-1|Def. §10.1]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]] (inverse maps)

> [!remark]- Connections
> - The same set as a group: [[§7 The Group ℤ∕nℤ#^def-7-1|493 Def. §7.1]] ($\mathbb{Z}/n\mathbb{Z}$, of order $n$).

## 21.2 The Arithmetic of Congruence Classes

> [!example] Example §21.2: Parity as Arithmetic in $\mathbb{Z}_2$
> The familiar rules for even and odd,
>
> | $+$ | even | odd |
> |---|---|---|
> | **even** | even | odd |
> | **odd** | odd | even |
>
> | $\times$ | even | odd |
> |---|---|---|
> | **even** | even | even |
> | **odd** | even | odd |
>
> say how the class modulo $2$ of $a$ and of $b$ determines the class of $a + b$ and of $ab$. Read with even $= [0]_2$, odd $= [1]_2$, they *define* an addition and a multiplication on $\mathbb{Z}_2$: $[1]_2 + [1]_2 = [0]_2$, $[1]_2 \times [1]_2 = [1]_2$, and so on.
>
> *Eccles: §21.2 (tables before Definition 21.2.1)*

^ex-21-2

The same idea works for every $m$: to add two columns of the table, pick any element of each, add, and see which column the sum lies in. The point to prove is that the column does not depend on the choices.

> [!definition] Definition §21.3: Arithmetic in $\mathbb{Z}_m$
> **Addition**, **subtraction** and **multiplication** of elements of $\mathbb{Z}_m$ are defined by
>
> $$
> [a]_m + [b]_m = [a + b]_m, \qquad [a]_m - [b]_m = [a - b]_m, \qquad [a]_m \times [b]_m = [ab]_m .
> $$
>
> *Eccles: Definition 21.2.1*

^def-21-3

> [!remark] Remark: Why Well-Definedness Needs Checking
> The formulas in [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|Definition §21.3]] are written in terms of *representatives*, and a class has many. In $\mathbb{Z}_8$, the third column is $[2]_8 = [10]_8$ and the eighth is $[7]_8 = [31]_8$. With the first representatives, $2 \times 7 = 14 \in [6]_8$; with the second, $10 \times 31 = 310 = 8 \times 38 + 6 \in [6]_8$ too. That the answer is always the same column is exactly what "multiplication is well defined" means; a rule that fails this test defines no function at all ([[§22 Partitions and Equivalence Relations#^ex-22-5|Example §22.5]]).

^rem-21-2

> [!theorem] Proposition §21.3: The Operations Are Well-Defined
> Addition, subtraction and multiplication in $\mathbb{Z}_m$ are well defined: if $[a_1]_m = [a_2]_m$ and $[b_1]_m = [b_2]_m$, then
>
> $$
> [a_1 + b_1]_m = [a_2 + b_2]_m, \qquad [a_1 - b_1]_m = [a_2 - b_2]_m, \qquad [a_1 b_1]_m = [a_2 b_2]_m .
> $$
>
> *Eccles: Proposition 21.2.2, Exercise 21.1*

^prop-21-3

> [!proof]+ Proof
> By Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]](1) the hypothesis says $a_1 \equiv a_2$ and $b_1 \equiv b_2 \pmod m$, and each conclusion says a congruence: $a_1 + b_1 \equiv a_2 + b_2$, $\ a_1 - b_1 \equiv a_2 - b_2$, $\ a_1 b_1 \equiv a_2 b_2 \pmod m$. These are the three parts of Proposition [[§19 Congruence of Integers#^prop-19-2|§19.2]] (modular arithmetic).

^pf-21-3

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]], [[§19 Congruence of Integers#^prop-19-2|§19.2]], [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|Def. §21.3]]

> [!remark]- Connections
> - [[§7 The Group ℤ∕nℤ#^prop-7-1|493 Prop. §7.1]] (addition of residue classes is well defined); the general notion: [[§7 The Group ℤ∕nℤ#^def-7-2|493 Def. §7.2]].

> [!theorem] Proposition §21.4: Laws of Arithmetic in $\mathbb{Z}_m$
> For all $\alpha, \beta, \gamma \in \mathbb{Z}_m$:
> 1. $\alpha + \beta = \beta + \alpha$ and $\alpha \times \beta = \beta \times \alpha$;
> 2. $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$ and $(\alpha \times \beta) \times \gamma = \alpha \times (\beta \times \gamma)$;
> 3. $\alpha \times (\beta + \gamma) = \alpha \times \beta + \alpha \times \gamma$;
> 4. $[0]_m$ is an additive identity, $\alpha + [0]_m = \alpha$, and $[1]_m$ a multiplicative identity, $\alpha \times [1]_m = \alpha$;
> 5. $[a]_m + [-a]_m = [0]_m$, and $\alpha - \beta = \alpha + (-\beta)$ where $-[b]_m = [-b]_m$.
>
> *Eccles: §21.2 (text after Proposition 21.2.2), parts 1–4; part 5 added here*

^prop-21-4

> [!proof]+ Proof
> Write $\alpha = [a]_m$, $\beta = [b]_m$, $\gamma = [c]_m$. By Definition [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|§21.3]] (legitimate by Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-3|§21.3]]) each law reduces to the corresponding law in $\mathbb{Z}$; for instance
>
> $$
> \alpha \times (\beta + \gamma) = [a]_m \times [b + c]_m = [a(b + c)]_m = [ab + ac]_m = [ab]_m + [ac]_m = \alpha \times \beta + \alpha \times \gamma ,
> $$
>
> and likewise $[a]_m + [b]_m = [a + b]_m = [b + a]_m = [b]_m + [a]_m$, $\ ([a]_m + [b]_m) + [c]_m = [(a + b) + c]_m = [a + (b + c)]_m = [a]_m + ([b]_m + [c]_m)$, the same for $\times$, $\ [a]_m + [0]_m = [a + 0]_m = [a]_m$, $\ [a]_m \times [1]_m = [a]_m$, $\ [a]_m + [-a]_m = [0]_m$ and $[a]_m - [b]_m = [a - b]_m = [a + (-b)]_m = [a]_m + [-b]_m$.

^pf-21-4

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|Def. §21.3]], [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-3|§21.3]], [[§2 Implications#^def-2-9|Def. §2.9]] (the laws in $\mathbb{Z}$)

> [!remark]- Connections
> - With (1)–(5), $\mathbb{Z}_m$ under $+$ is the group [[§7 The Group ℤ∕nℤ#^def-7-1|493 Def. §7.1]]; it is a field exactly when $m$ is prime, [[§8 Invertibility and Unit Groups#^prop-8-4|493 Prop. §8.4]].

## 21.3 The Arithmetic of Remainders

The same arithmetic can be done with remainders instead of classes, which may feel more concrete.

> [!definition] Definition §21.4: Arithmetic in $R_m$
> **Addition**, **subtraction** and **multiplication** of elements of $R_m$ are defined by
>
> $$
> a +_m b = r_m(a + b), \qquad a -_m b = r_m(a - b), \qquad a \times_m b = r_m(ab) \qquad (a, b \in R_m).
> $$
>
> That is, compute as usual and take the remainder modulo $m$.
>
> *Eccles: Definition 21.3.1*

^def-21-4

> [!example] Example §21.3: The Multiplication Table of $R_{10}$
> Modulo $10$ the remainder of a positive integer is its last decimal digit, so $\times_{10}$ is "multiply and keep the last digit":
>
> | $\times_{10}$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
> |---|---|---|---|---|---|---|---|---|---|---|
> | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
> | $1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
> | $2$ | $0$ | $2$ | $4$ | $6$ | $8$ | $0$ | $2$ | $4$ | $6$ | $8$ |
> | $3$ | $0$ | $3$ | $6$ | $9$ | $2$ | $5$ | $8$ | $1$ | $4$ | $7$ |
> | $4$ | $0$ | $4$ | $8$ | $2$ | $6$ | $0$ | $4$ | $8$ | $2$ | $6$ |
> | $5$ | $0$ | $5$ | $0$ | $5$ | $0$ | $5$ | $0$ | $5$ | $0$ | $5$ |
> | $6$ | $0$ | $6$ | $2$ | $8$ | $4$ | $0$ | $6$ | $2$ | $8$ | $4$ |
> | $7$ | $0$ | $7$ | $4$ | $1$ | $8$ | $5$ | $2$ | $9$ | $6$ | $3$ |
> | $8$ | $0$ | $8$ | $6$ | $4$ | $2$ | $0$ | $8$ | $6$ | $4$ | $2$ |
> | $9$ | $0$ | $9$ | $8$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ |
>
> *Eccles: §21.3 (table after Definition 21.3.1)*

^ex-21-3

> [!theorem] Proposition §21.5: Remainders Compute Classes
> For $a, b \in R_m$,
>
> $$
> [a]_m + [b]_m = [a +_m b]_m, \qquad [a]_m - [b]_m = [a -_m b]_m, \qquad [a]_m \times [b]_m = [a \times_m b]_m .
> $$
>
> *Eccles: Proposition 21.3.2, Exercise 21.2*

^prop-21-5

> [!proof]+ Proof
> By definition of the remainder map, $r_m(c) \equiv c \pmod m$ for every integer $c$; with $c = a + b$, $a - b$, $ab$ this gives
>
> $$
> a +_m b \equiv a + b, \qquad a -_m b \equiv a - b, \qquad a \times_m b \equiv ab \pmod m .
> $$
>
> By Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]](1), $[a +_m b]_m = [a + b]_m = [a]_m + [b]_m$, and likewise for $-$ and $\times$.

^pf-21-5

*Uses:* [[§19 Congruence of Integers#^def-19-3|Def. §19.3]], [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]], [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|Def. §21.3]], [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-4|Def. §21.4]]

So the bijection $R_m \to \mathbb{Z}_m$, $a \mapsto [a]_m$ (Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-2|§21.2]]) turns the tables of $R_m$ into those of $\mathbb{Z}_m$: replace each $a$ by $[a]_m$. Two algebraic structures related like this are **isomorphic** ("of the same form"), a notion developed in abstract algebra.

> [!remark]- Connections
> - Isomorphism of groups: [[§16 Isomorphisms#^def-16-1|493 Def. §16.1]].

## 21.4 Linear Congruences in $\mathbb{Z}_m$

Arithmetic in $\mathbb{Z}_m$ (or $R_m$) differs from arithmetic in $\mathbb{Z}$ in two ways. The set is finite, so every equation can be solved by trying all possibilities. And division behaves differently: in $\mathbb{Z}$ we can always divide only by $\pm 1$, but in $R_m$ there may be other numbers we can always divide by. Since $ax \equiv b \pmod m$ iff $[ax]_m = [b]_m$, i.e. $[a]_m \times [x]_m = [b]_m$, Theorem [[§20 Linear Congruences#^thm-20-4|§20.4]] can be restated in $\mathbb{Z}_m$, and finiteness then gives a proof by counting.

> [!theorem] Theorem §21.6: Solving $[a][x] = [b]$ in $\mathbb{Z}_m$
> Suppose that $a$ and $b$ are integers with $a$ and $m$ coprime. Then the equation
>
> $$
> [a]_m \times [x]_m = [b]_m
> $$
>
> has a solution $[x]_m \in \mathbb{Z}_m$, and this solution is unique.
>
> *Eccles: Theorem 21.4.1*

^thm-21-6

> [!proof]+ Proof
> Define $f : \mathbb{Z}_m \to \mathbb{Z}_m$ by $f([x]_m) = [a]_m \times [x]_m$; this is a function because multiplication is well defined (Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-3|§21.3]]).
>
> *$f$ is injective.* Since $\gcd(a, m) = 1$,
>
> $$
> f([x_1]_m) = f([x_2]_m) \Rightarrow [a x_1]_m = [a x_2]_m \Rightarrow a x_1 \equiv a x_2 \pmod m \Rightarrow x_1 \equiv x_2 \pmod m \Rightarrow [x_1]_m = [x_2]_m ,
> $$
>
> by Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]] and Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]].
>
> *$f$ is surjective.* Suppose for contradiction that some $[y_0]_m \in \mathbb{Z}_m$ is not a value of $f$. Then $f$ is an injection from $\mathbb{Z}_m$, of cardinality $m$ (Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-2|§21.2]]), to $\mathbb{Z}_m - \{[y_0]_m\}$, of cardinality $m - 1$, contradicting the pigeonhole principle ([[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]]). Hence $f$ is a surjection, so a bijection.
>
> Therefore there is exactly one $[x_0]_m \in \mathbb{Z}_m$ with $f([x_0]_m) = [b]_m$, i.e. $[a]_m \times [x_0]_m = [b]_m$.

^pf-21-6

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-1|§21.1]], [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-2|§21.2]], [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-3|§21.3]], [[§19 Congruence of Integers#^prop-19-7|§19.7]], [[§11 Properties of Finite Sets#^thm-11-2|§11.2]]

> [!remark] Remark: The Idea — Rows of the Multiplication Table
> Let $\mathrm{Row}(a)$ be the set of entries in the row of $[a]_m$ in the multiplication table of $\mathbb{Z}_m$. The equation has a solution iff $[b]_m \in \mathrm{Row}(a)$. If the $m$ entries of the row are distinct, then $\mathrm{Row}(a)$ is a subset of $\mathbb{Z}_m$ with $m$ elements, hence all of $\mathbb{Z}_m$, and $[b]_m$ occurs exactly once. And the entries *are* distinct when $\gcd(a, m) = 1$, by cancellation (Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]]). The formal proof phrases this with a function and the pigeonhole principle.

^rem-21-3

This proof is **non-constructive**: it guarantees a solution without saying how to find it (short of trying all $m$ classes), which is typical of counting arguments; the Euclidean-algorithm proof of [[§20 Linear Congruences#^thm-20-4|Theorem §20.4]] computes it. On the other hand the counting proof shows *why* the result holds: multiplication by a class coprime to $m$ just permutes $\mathbb{Z}_m$. Different proofs of one theorem can illuminate different things.

> [!example] Example §21.4: Rows That Contain Everything
> In the multiplication table of $R_{10}$ ([[§21 Congruence Classes and the Arithmetic of Remainders#^ex-21-3|Example §21.3]]) the row of $7$ is $0, 7, 4, 1, 8, 5, 2, 9, 6, 3$: every remainder occurs exactly once. So we can always "divide by $7$": $7 \times_{10} x = b$, equivalently $[7]_{10} \times [x]_{10} = [b]_{10}$, has a unique solution for every $b \in R_{10}$. The rows with this property are those of $1, 3, 7, 9$, exactly the elements of $R_{10}$ coprime to $10$; and these are also exactly the rows containing $1$. The row of $5$, by contrast, is $0, 5, 0, 5, \ldots$, missing $1$ and repeating $0$.
>
> *Eccles: Example 21.4.2*

^ex-21-4

An element is *invertible* when its row contains $1$; we now show that the pattern of [[§21 Congruence Classes and the Arithmetic of Remainders#^ex-21-4|Example §21.4]] always holds.

> [!definition] Definition §21.5: Invertible; Inverse Modulo $m$
> The element $[a]_m \in \mathbb{Z}_m$ is **invertible** (or $a \in \mathbb{Z}$ is **invertible modulo $m$**) if there is an integer $a'$ with $[a]_m \times [a']_m = [1]_m$, equivalently $a a' \equiv 1 \pmod m$. Then $[a']_m$ is called the **inverse** of $[a]_m$, written $[a']_m = ([a]_m)^{-1}$, and $a'$ is called an **inverse of $a$ modulo $m$**.
>
> *Eccles: Definition 21.4.3*

^def-21-5

The inverse class is unique: if $aa' \equiv 1 \equiv aa''$, then $a' \equiv a'(aa'') = (a'a)a'' \equiv a''$.

> [!remark]- Connections
> - [[§8 Invertibility and Unit Groups#^def-8-2|493 Def. §8.2]]; the invertible classes form the unit group [[§8 Invertibility and Unit Groups#^def-8-4|493 Def. §8.4]].

> [!theorem] Proposition §21.7: Solving by Multiplying by the Inverse
> Suppose that $a'$ is an inverse of $a$ modulo $m$. Then for all integers $b$ and $x$,
>
> $$
> ax \equiv b \pmod m \iff x \equiv a' b \pmod m .
> $$
>
> *Eccles: Proposition 21.4.5*

^prop-21-7

> [!proof]+ Proof
> We have $aa' \equiv 1 \pmod m$. ($\Rightarrow$) $ax \equiv b \Rightarrow a'ax \equiv a'b \Rightarrow x \equiv a'b$, since $a'a x \equiv 1 \cdot x$. ($\Leftarrow$) $x \equiv a'b \Rightarrow ax \equiv aa'b \Rightarrow ax \equiv b$, since $aa'b \equiv 1 \cdot b$. All steps are modular arithmetic.

^pf-21-7

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|Def. §21.5]], [[§19 Congruence of Integers#^prop-19-2|§19.2]]

> [!theorem] Proposition §21.8: Invertible Means Always Uniquely Solvable
> The integer $a$ is invertible modulo $m$ if and only if every linear congruence $ax \equiv b \pmod m$ has a unique solution modulo $m$. Equivalently, every class occurs exactly once in the row of $[a]_m$ in the multiplication table of $\mathbb{Z}_m$.
>
> *Eccles: Proposition 21.4.4*

^prop-21-8

> [!proof]+ Proof
> ($\Rightarrow$) If $a'$ is an inverse of $a$, then by Proposition [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-7|§21.7]] the solutions of $ax \equiv b$ are exactly the $x \equiv a'b \pmod m$: one solution, unique modulo $m$.
>
> ($\Leftarrow$) Take $b = 1$: the congruence $ax \equiv 1 \pmod m$ has a solution $a'$, which is an inverse of $a$.

^pf-21-8

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-7|§21.7]], [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|Def. §21.5]], [[§20 Linear Congruences#^def-20-1|Def. §20.1]]

> [!theorem] Corollary §21.9: Invertible If and Only If Coprime
> An integer $a$ is invertible modulo $m$ if and only if $a$ and $m$ are coprime.
>
> *Eccles: Exercise 21.4*

^cor-21-9

> [!proof]+ Proof
> $a$ is invertible modulo $m$ exactly when $ax \equiv 1 \pmod m$ has a solution. By Theorem [[§20 Linear Congruences#^thm-20-5|§20.5]] this happens iff $\gcd(a, m)$ divides $1$, i.e. iff $\gcd(a, m) = 1$.

^pf-21-9

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|Def. §21.5]], [[§20 Linear Congruences#^thm-20-5|§20.5]]

For a prime modulus $p$ every class other than $[0]_p$ is invertible; the counting proof of [[§21 Congruence Classes and the Arithmetic of Remainders#^thm-21-6|Theorem §21.6]] then leads to Fermat's little theorem, [[§24★ Congruence Modulo a Prime#^thm-24-1|Theorem §24.1]].

> [!remark]- Connections
> - [[§8 Invertibility and Unit Groups#^prop-8-1|493 Prop. §8.1]] (invertibility criterion).

> [!example] Example §21.5: Computing Inverses
> (a) In $\mathbb{Z}_{10}$ the invertible elements are $[1], [3], [7], [9]$ (the rows of [[§21 Congruence Classes and the Arithmetic of Remainders#^ex-21-3|Example §21.3]] containing $1$), with $[1]^{-1} = [1]$, $[3]^{-1} = [7]$, $[7]^{-1} = [3]$, $[9]^{-1} = [9]$.
>
> (b) Modulo $12$ the invertible elements are $1, 5, 7, 11$ (the elements of $R_{12}$ coprime to $12$), and each is its own inverse: $1, 25, 49, 121 \equiv 1 \pmod{12}$.
>
> (c) *$290$ is invertible modulo $357$.* Example [[§20 Linear Congruences#^ex-20-4|§20.4]] found $\gcd(290, 357) = 1$ and $290 \times (-16) \equiv 1 \pmod{357}$, so $([290]_{357})^{-1} = [-16]_{357} = [341]_{357}$. By [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-7|Proposition §21.7]] every congruence $290x \equiv b \pmod{357}$ is now solved by one multiplication:
>
> | $b$ | $x \equiv -16\, b$ | answer |
> |---|---|---|
> | $2$ | $-32$ | $x \equiv 325 \pmod{357}$ |
> | $5$ | $-80$ | $x \equiv 277 \pmod{357}$ |
> | $355 \equiv -2$ | $32$ | $x \equiv 32 \pmod{357}$ |
>
> *Eccles: Definition 21.4.3 (examples), Exercises 21.3, 21.5*

^ex-21-5
