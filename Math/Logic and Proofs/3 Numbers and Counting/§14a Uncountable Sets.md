---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: "14a"
eccles: "Ch. 14"
aliases: ["Eccles 14 (cont.)"]
tags: [logic-and-proofs, mat250]
---
← [[§14 Counting Infinite Sets]] · ↑ [[· 3 Numbers and Counting]] · [[§15 The Division Theorem]] →

*Eccles, Chapter 14 and Problems III (Q12, Q26–Q28) · MAT 250 HW5 (Exercises 14.1–14.4) · MAT 200 lecture (syllabus week 15).*

Not all infinite sets have the same size: $\R$ is uncountable, every set is smaller than its power set (Cantor), and two sets each injecting into the other are equipotent (Cantor–Schröder–Bernstein).

## 14.3 Uncountable Sets

So many infinite sets turn out to be denumerable that Galileo's view might seem right after all. It is not. In 1874 Cantor proved not only that $\Q$ is denumerable but that $\R$ is not.

To show that $\R$ is not denumerable is to show that *no* bijection $\Z^+ \to \R$ exists, a non-existence statement. The method: given *any* function $\Z^+ \to \R$, construct a real number that is not a value, by **Cantor's diagonal process** on decimal expansions. Since some numbers have two expansions ($0.\dot9 = 1.\dot0$, [[§13 Number Systems#^ex-13-4|Example §13.4]]), we first fix one.

> [!theorem] Lemma §14.11: Decimal Expansions Not Ending in Nines
> 1. Every real $x$ with $0 \le x < 1$ is represented by an infinite decimal $0.a_1 a_2 \ldots$ that does not end in recurring $9$s.
> 2. Two infinite decimals that do not end in recurring $9$s and represent the same real number are identical.
>
> *Eccles: Problems III Q26–Q27 (the case used in the proof of Theorem 14.3.1)*

^lem-14-11

> [!proof]- Proof
> Write $s_n$ for the truncation of a decimal at place $n$.
>
> (1) By the standing assumption of §13 (stated before [[§13 Number Systems#^def-13-5|Definition §13.5]]), $x$ is represented by some decimal $a_0.a_1a_2\ldots$; $a_0 \le s_1 \le x < 1$ forces $a_0 = 0$. Suppose it ends in $9$s, say $a_i = 9$ for all $i > k$. If $k = 0$, then $x = 0.\dot9 = 1$ (Example [[§13 Number Systems#^ex-13-4|§13.4]]), which is excluded. So take $k \ge 1$ least, so that $a_k \le 8$, and let $d = s_k + 10^{-k} = 0.a_1 \ldots a_{k-1}(a_k + 1)$. For $n \ge k$, $s_n = d - 10^{-n}$, so the defining inequalities give $d - 10^{-n} \le x \le d$, hence $|d - x| \le 10^{-n}$ for all $n \ge k$, and $x = d$ by the argument of Proposition [[§13 Number Systems#^prop-13-5|§13.5]]. The terminating decimal $0.a_1 \ldots a_{k-1}(a_k + 1)000\ldots$ represents $d$: its truncation $t_n$ is $d$ for $n \ge k$, and for $n < k$, $0 \le d - t_n \le 9 \cdot 10^{-(n+1)} + \cdots + 9 \cdot 10^{-k} = 10^{-n} - 10^{-k}$. It does not end in $9$s.
>
> (2) Let $a = 0.a_1 a_2 \ldots = 0.b_1 b_2 \ldots$ (truncations $s_n$, $t_n$), neither ending in $9$s, and suppose they differ; let $k$ be the first place where $a_k \ne b_k$, say $a_k < b_k$. Then $s_{k-1} = t_{k-1}$ (both $0$ if $k = 1$) and
>
> $$
> t_k = s_{k-1} + b_k 10^{-k} \ge s_{k-1} + (a_k + 1) 10^{-k} = s_k + 10^{-k}.
> $$
>
> Since $a_1 a_2 \ldots$ does not end in $9$s, some $j > k$ has $a_j \le 8$, and then
>
> $$
> s_j = s_k + \sum_{i=k+1}^{j} a_i 10^{-i} \le s_k + \sum_{i=k+1}^{j} 9 \cdot 10^{-i} - 10^{-j} = s_k + 10^{-k} - 2 \cdot 10^{-j}.
> $$
>
> So $a \le s_j + 10^{-j} < s_k + 10^{-k} \le t_k \le a$, a contradiction.

^pf-14-11

*Uses:* [[§13 Number Systems#^def-13-5|Def. §13.5]], [[§13 Number Systems#^prop-13-5|§13.5]], [[§13 Number Systems#^ex-13-4|Ex. §13.4]]

> [!theorem] Theorem §14.12: The Reals Are Uncountable (Cantor, 1874)
> The set $\R$ of real numbers is uncountable.
>
> *Eccles: Theorem 14.3.1*

^thm-14-12

> [!proof]+ Proof
> $\R$ is infinite, since the inclusion $\Z^+ \to \R$ is injective (Proposition [[§14 Counting Infinite Sets#^prop-14-1|§14.1]]). We show that no function $f : \Z^+ \to \R$ is surjective, so $\R$ is not denumerable either.
>
> For each $n$ with $0 \le f(n) < 1$, write $f(n) = 0.a_{n1} a_{n2} \ldots a_{nn} \ldots$, the expansion not ending in recurring $9$s (Lemma [[§14 Counting Infinite Sets#^lem-14-11|§14.11]](1)). Define $b = 0.b_1 b_2 \ldots b_n \ldots$ by
>
> $$
> b_n = \begin{cases} 1 & \text{if } 0 \le f(n) < 1 \text{ and } a_{nn} = 0, \\ 0 & \text{otherwise}. \end{cases}
> $$
>
> This decimal has only the digits $0$ and $1$, so it does not end in recurring $9$s, and $0 \le 0.b_1 \le b \le 0.b_1 + 10^{-1} \le 0.1 + 0.1 < 1$ (the defining inequalities of [[§13 Number Systems#^def-13-5|Definition §13.5]] at $n = 1$). Now fix $n$. If $f(n) \notin [0, 1)$ then $f(n) \ne b$. If $0 \le f(n) < 1$, the $n$th digit $b_n$ of $b$ differs from the $n$th digit $a_{nn}$ of $f(n)$ (if $a_{nn} = 0$ then $b_n = 1$, and if $a_{nn} \ne 0$ then $b_n = 0$), so the two expansions differ, and by Lemma [[§14 Counting Infinite Sets#^lem-14-11|§14.11]](2) $f(n) \ne b$. So $b$ is not a value of $f$.

^pf-14-12

*Uses:* [[§14 Counting Infinite Sets#^prop-14-1|§14.1]], [[§14 Counting Infinite Sets#^lem-14-11|§14.11]], [[§13 Number Systems#^def-13-5|Def. §13.5]]

The real number $b$ is built to disagree with the $n$th listed number in the $n$th decimal place: it runs down the diagonal of the array of digits $(a_{nm})$, which is where the name comes from.

> [!definition] Definition §14.3: Comparing Cardinalities
> Sets $X$ and $Y$ have the **same cardinality**, $|X| = |Y|$, if they are equipotent. If there is an injection $X \to Y$ we write $|X| \le |Y|$. We write $|X| < |Y|$, and say $X$ has **smaller cardinality** than $Y$, when $|X| \le |Y|$ and $|X| \ne |Y|$.
>
> *Eccles: Definition 14.3.2*

^def-14-3

Composites of injections are injections, so $|X| \le |Y|$ and $|Y| \le |Z|$ give $|X| \le |Z|$. Theorem [[§14 Counting Infinite Sets#^thm-14-12|§14.12]] says $|\Z^+| < |\R|$, that is, $|\R| > \aleph_0$: the inclusion gives $\le$, and the theorem gives $\ne$.

> [!remark]- Remark: The Continuum Hypothesis
> Is there a set of size strictly between $\Z^+$ and $\R$ (the "continuum")? In 1878 Cantor conjectured not: *every uncountable subset $X \subseteq \R$ has $|X| = |\R|$*. This **continuum hypothesis** can be neither proved (Cohen, 1963) nor disproved (Gödel, 1938) from the usual axioms of set theory, so there are consistent versions of set theory in which it is true and others in which it is false.

^rem-14-3

The other natural question is whether there is a set larger than $\R$. There is, and every set has a larger one: its power set.

> [!theorem] Theorem §14.13: Cantor's Theorem
> For every set $X$, $|X| < |\mathcal{P}(X)|$.
>
> *Eccles: Theorem 14.3.3*
> *Source: MAT 200 lecture (syllabus week 15)*

^thm-14-13

An injection $X \to \mathcal{P}(X)$ is easy: send each element to its singleton. The point is that there is no bijection, and the method is that of Theorem [[§14 Counting Infinite Sets#^thm-14-12|§14.12]]: from any function $f : X \to \mathcal{P}(X)$, construct a subset of $X$ that is not a value. The subset is easy to describe; why it is not a value is subtle.

> [!proof]+ Proof
> The map $x \mapsto \{x\}$ is an injection $X \to \mathcal{P}(X)$, so $|X| \le |\mathcal{P}(X)|$.
>
> Let $f : X \to \mathcal{P}(X)$ be any function. For each $x \in X$, $f(x)$ is a subset of $X$, so either $x \in f(x)$ or $x \notin f(x)$; thus "$x \notin f(x)$" is a predicate on $X$, and it defines a subset
>
> $$
> A = \{ x \in X \mid x \notin f(x) \} \in \mathcal{P}(X).
> $$
>
> Suppose for contradiction that $A = f(a)$ for some $a \in X$. Either $a \in A$ or $a \notin A$. If $a \in A$, then by the predicate defining $A$, $a \notin f(a) = A$, a contradiction. If $a \notin A$, then $a$ fails the predicate, so $a \in f(a) = A$, a contradiction. So $A$ is not a value of $f$, and $f$ is not a surjection.
>
> Hence there is no bijection $X \to \mathcal{P}(X)$, while there is an injection: $|X| < |\mathcal{P}(X)|$.

^pf-14-13

*Uses:* [[§14 Counting Infinite Sets#^def-14-3|Def. §14.3]], [[§6 The Language of Set Theory#^def-6-9|Def. §6.9]], [[§6 The Language of Set Theory#^def-6-new2|Def. §6.9]]

> [!remark]- Connections
> - Developed further in: [[§4 Uncountability#^thm-4-1|551 Thm. §4.1]] ([[Cantor's Theorem]]), with the power set [[§4 Uncountability#^def-4-1|551 Def. §4.1]].

Applied to $\Z^+$, $\mathcal{P}(\Z^+)$ is uncountable; iterating, $\Z^+, \mathcal{P}(\Z^+), \mathcal{P}(\mathcal{P}(\Z^+)), \ldots$ have strictly increasing cardinalities, an endless hierarchy of infinities. For finite $X$ the theorem says $n < 2^n$ ([[§12★ Counting Functions and Subsets#^prop-12-4|Proposition §12.4]]).

The most important result about finite sets was the pigeonhole principle ([[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]]): an injection $X \to Y$ forces $|X| \le |Y|$. It still holds for infinite sets, but now the content lies in the following theorem: inequalities between cardinalities in both directions force equality, as they do for numbers.

> [!theorem] Theorem §14.14: The Cantor–Schröder–Bernstein Theorem
> If there are injections $f : X \to Y$ and $g : Y \to X$, then $X$ and $Y$ are equipotent. That is, $|X| \le |Y|$ and $|Y| \le |X|$ imply $|X| = |Y|$.
>
> *Eccles: Theorem 14.3.4 and Exercise 14.4 (proof omitted in Eccles)*
> *Source: MAT 200 lecture (syllabus week 15); standard*

^thm-14-14

The difficulty is that neither $f$ nor $g^{-1}$ alone is a bijection; we use $f$ on part of $X$ and $g^{-1}$ on the rest. Points of $X$ outside the image of $g$ cannot be sent anywhere by $g^{-1}$, so they must go by $f$; then $g(f(x))$ must go by $f$ too (if it went by $g^{-1}$ it would land on $f(x)$, already taken), and so on. This gives the set $C$ below.

> [!proof]+ Proof
> Define subsets $C_k \subseteq X$ inductively by
>
> $$
> C_0 = X - g(Y), \qquad C_{k+1} = g(f(C_k)) \quad (k \ge 0),
> $$
>
> and let $C = \bigcup_{k \ge 0} C_k$. If $x \notin C$ then $x \notin C_0$, so $x \in g(Y)$, and since $g$ is injective there is exactly one $y \in Y$ with $g(y) = x$; call it $g^{-1}(x)$. Define $h : X \to Y$ by
>
> $$
> h(x) = \begin{cases} f(x) & \text{if } x \in C, \\ g^{-1}(x) & \text{if } x \notin C. \end{cases}
> $$
>
> *$h$ is injective.* Let $h(x) = h(x')$. If $x, x' \in C$, then $f(x) = f(x')$ and $x = x'$. If $x, x' \notin C$, then $g^{-1}(x) = g^{-1}(x')$, and applying $g$ gives $x = x'$. If $x \in C$ and $x' \notin C$, then $f(x) = g^{-1}(x')$, so $x' = g(f(x))$; but $x \in C_k$ for some $k$, so $x' \in g(f(C_k)) = C_{k+1} \subseteq C$, a contradiction. So this case cannot occur.
>
> *$h$ is surjective.* Let $y \in Y$. If $g(y) \notin C$, then $h(g(y)) = g^{-1}(g(y)) = y$. If $g(y) \in C$, then $g(y) \in C_k$ for some $k$, and $k \ne 0$ because $g(y) \in g(Y)$. So $g(y) \in C_k = g(f(C_{k-1}))$: $g(y) = g(f(x))$ for some $x \in C_{k-1}$, and as $g$ is injective, $y = f(x) = h(x)$ since $x \in C$.
>
> So $h$ is a bijection $X \to Y$.

^pf-14-14

*Uses:* [[§14 Counting Infinite Sets#^def-14-3|Def. §14.3]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (definition by induction from $k = 0$), [[§9 Injections, Surjections and Bijections#^def-9-4|Def. §9.4]] (images of subsets)

> [!remark]- Connections
> - Developed further in: [[§2 The Cantor–Bernstein Theorem#^thm-2-1|551 Thm. §2.1]] ([[Cantor–Bernstein Theorem]]); 551 proves it differently, finding the dividing set $A$ ([[§2 The Cantor–Bernstein Theorem#^lem-2-2|551 Lemma §2.2]]) as the union of all "admissible" sets rather than by the chains $C_k$ used here.

Eccles states the theorem in a form that looks like the pigeonhole principle.

> [!theorem] Corollary §14.15: The Pigeonhole Principle for Infinite Sets
> Let $X$ and $Y$ be non-empty sets with $|X| > |Y|$. Then no function $f : X \to Y$ is an injection: there are distinct $x_1, x_2 \in X$ with $f(x_1) = f(x_2)$.
>
> *Eccles: Theorem 14.3.4 (stated there under the name Cantor–Schröder–Bernstein)*

^cor-14-15

> [!proof]+ Proof
> $|X| > |Y|$ means $|Y| \le |X|$ and $|X| \ne |Y|$. If $f : X \to Y$ were injective, then also $|X| \le |Y|$, and Theorem [[§14 Counting Infinite Sets#^thm-14-14|§14.14]] would give $|X| = |Y|$, a contradiction.

^pf-14-15

*Uses:* [[§14 Counting Infinite Sets#^thm-14-14|§14.14]], [[§14 Counting Infinite Sets#^def-14-3|Def. §14.3]]

For finite sets this is the pigeonhole principle, [[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]], which needed no Cantor–Schröder–Bernstein theorem (for finite sets, $|X| > |Y|$ in the sense of Definition [[§14 Counting Infinite Sets#^def-14-3|§14.3]] is the inequality of the numbers $|X|$ and $|Y|$, by [[§11 Properties of Finite Sets#^cor-11-1|Corollary §11.1]] and [[§10 Counting#^prop-10-3|Proposition §10.3]]).

> [!example] Example §14.5: The Usual Form from Eccles's Form
> Use Eccles's form of the Cantor–Schröder–Bernstein theorem (Corollary [[§14 Counting Infinite Sets#^cor-14-15|§14.15]]) to prove that if $|X| \le |Y|$ and $|Y| \le |X|$ then $|X| = |Y|$.
>
> *Solution.* Suppose for contradiction that $|X| \ne |Y|$. With $|X| \le |Y|$ this gives $|X| < |Y|$, and with $|Y| \le |X|$ it gives $|Y| < |X|$, i.e. $|X| > |Y|$. By $|X| < |Y|$ there is an injection $X \to Y$; by $|X| > |Y|$ and Eccles's form, no function $X \to Y$ is an injection. This contradiction shows $|X| = |Y|$. (If $X$ or $Y$ is empty, both are, since there is no function from a non-empty set to $\emptyset$, and $|X| = |Y|$ trivially.)
>
> So the two forms are equivalent; neither is easier than the other, and Theorem [[§14 Counting Infinite Sets#^thm-14-14|§14.14]] is the proof of both.
>
> *Eccles: Exercise 14.4*
> *Source: HW5*

^ex-14-5

*Uses:* [[§14 Counting Infinite Sets#^cor-14-15|§14.15]], [[§14 Counting Infinite Sets#^def-14-3|Def. §14.3]]

To show the power of these ideas, here is one of Cantor's results.

> [!definition] Definition §14.4: Algebraic and Transcendental Numbers
> A real number is **algebraic** if it satisfies a polynomial equation
>
> $$
> x^n + a_1 x^{n-1} + \cdots + a_{n-1} x + a_n = 0 \qquad (n \ge 1)
> $$
>
> with all coefficients $a_i$ rational. It is **transcendental** if it is not algebraic.
>
> *Eccles: Definition 14.3.5*

^def-14-4

Every rational number $m/n$ is algebraic ($x - m/n = 0$), and so is $\sqrt2$ ($x^2 - 2 = 0$). Liouville (1844) constructed the first explicit transcendental numbers; Hermite (1873) proved $e$ transcendental and Lindemann (1882) $\pi$, which finally showed that the circle cannot be squared by ruler and compass. Whether $\pi + e$ is transcendental is still unknown. Cantor's result is that, nevertheless, *most* real numbers are transcendental.

> [!theorem] Theorem §14.16: Algebraic Numbers Are Denumerable, Transcendental Numbers Are Not
> The set $\mathbb{A}$ of algebraic numbers is denumerable, and the set $\R - \mathbb{A}$ of transcendental numbers is uncountable.
>
> *Eccles: Section 14.3 (text after Definition 14.3.5) and Problems III Q28*

^thm-14-16

> [!proof]+ Proof
> We use the fact (from algebra; Eccles quotes it in the hint) that a polynomial equation of degree $n$ has at most $n$ real roots.
>
> Let $P_n$ be the set of polynomials $x^n + a_1 x^{n-1} + \cdots + a_n$ with rational coefficients. Sending a polynomial to its coefficients $(a_1, \ldots, a_n)$ is a bijection $P_n \to \Q^n$, and $\Q^n$ is denumerable (Theorem [[§14 Counting Infinite Sets#^thm-14-10|§14.10]], Corollary [[§14 Counting Infinite Sets#^cor-14-9|§14.9]]). The sets $P_1, P_2, \ldots$ are pairwise disjoint (different degrees), so $P = \bigcup_n P_n$ is denumerable by Example [[§14 Counting Infinite Sets#^ex-14-4|§14.4]]. List it as $P = \{p_1, p_2, \ldots\}$.
>
> For $\alpha \in \mathbb{A}$ let $k(\alpha)$ be the least $k$ with $p_k(\alpha) = 0$. The real roots of $p_{k(\alpha)}$ form a finite non-empty set; list them in increasing order $r_1 < r_2 < \cdots < r_j$ (repeatedly taking the minimum, [[§11 Properties of Finite Sets#^prop-11-9|Proposition §11.9]]), and let $i(\alpha)$ be the index with $\alpha = r_{i(\alpha)}$. Then $\alpha \mapsto (k(\alpha), i(\alpha))$ is an injection $\mathbb{A} \to \Z^+ \times \Z^+$: $\alpha$ is recovered as the $i(\alpha)$-th root of $p_{k(\alpha)}$. Composing with the bijection $\varphi$ of Proposition [[§14 Counting Infinite Sets#^prop-14-8|§14.8]] gives an injection $\mathbb{A} \to \Z^+$, so $\mathbb{A}$ is countable (Corollary [[§14 Counting Infinite Sets#^cor-14-6|§14.6]]). It is infinite because it contains $\Q$ (a subset of a finite set would be finite, [[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]). So $\mathbb{A}$ is denumerable.
>
> Since $\R$ is uncountable (Theorem [[§14 Counting Infinite Sets#^thm-14-12|§14.12]]) and $\mathbb{A} \subseteq \R$ is denumerable, $\R - \mathbb{A}$ is uncountable by Example [[§14 Counting Infinite Sets#^ex-14-3|§14.3]](b).

^pf-14-16

*Uses:* [[§14 Counting Infinite Sets#^thm-14-10|§14.10]], [[§14 Counting Infinite Sets#^cor-14-9|§14.9]], [[§14 Counting Infinite Sets#^ex-14-4|Ex. §14.4]], [[§14 Counting Infinite Sets#^prop-14-8|§14.8]], [[§14 Counting Infinite Sets#^cor-14-6|§14.6]], [[§14 Counting Infinite Sets#^thm-14-12|§14.12]], [[§14 Counting Infinite Sets#^ex-14-3|Ex. §14.3]], [[§11 Properties of Finite Sets#^prop-11-9|§11.9]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]]

> [!remark]- Connections
> - In 451: [[§2 The Set ℚ of Rational Numbers#^def-2-5|451 Def. §2.5]] (algebraic numbers, with integer coefficients, equivalent by clearing denominators), [[§2 The Set ℚ of Rational Numbers#^thm-2-6|451 Thm. §2.6]] (they are countable), [[§2 The Set ℚ of Rational Numbers#^def-2-10|451 Def. §2.10]] and [[§2 The Set ℚ of Rational Numbers#^thm-2-7|451 Thm. §2.7]] (transcendental numbers exist).

So the transcendental numbers, of which hardly any explicit example is easy to verify, form the overwhelming majority of $\R$, while the algebraic numbers, which include every number one usually writes down, are only countably many.
