---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: "22a"
eccles: "Ch. 22"
aliases: ["Eccles 22 (cont.)"]
tags: [logic-and-proofs, mat250]
---
← [[§22 Partitions and Equivalence Relations]] · ↑ [[· 5 Modular Arithmetic]] · [[§23 The Sequence of Prime Numbers]] →

*Eccles, Chapter 22 and Problems V · MAT 200 lecture (syllabus week 13: relations, equivalence relations and partitions, quotient sets, constructions of the integers and rational numbers) · the student's Rational Number Project (MAT 250, Oct 2024) · Sundstrom §7.1–7.3.*

This section uses quotient sets ([[§22 Partitions and Equivalence Relations#^def-22-new2|Def. §22.4]]) to *construct* the number systems that [[§13 Number Systems|§13]] took for granted: $\mathbb{Q}$ from $\mathbb{Z}$ (the Rational Number Project) and $\mathbb{Z}$ from $\mathbb{N}$.

## 22.4 Construction of the Rational Numbers

[[§22 Partitions and Equivalence Relations#^ex-22-6|Example §22.6]] *assumed* that $\mathbb{Q}$ exists. With hindsight we can reverse it and *define* $\mathbb{Q}$ to be the quotient set, so that a rational number simply *is* a class of fractions; the temporary notation of [[§13 Number Systems#^def-13-new1|Definition §13.1]] for "the fraction $a/b$ represents $q$" anticipated $q = [(a, b)]$. This is the construction carried out in the student's Rational Number Project, whose motivation is that $\mathbb{Z}$ is not closed under division ($6 \div 4 \notin \mathbb{Z}$): we want a number system extending $\mathbb{Z}$, with the same laws of arithmetic, in which $bx = a$ can be solved for every $b \neq 0$ ([[§22 Partitions and Equivalence Relations#^prop-22-10|Proposition §22.10]]). It uses only the following properties of $\mathbb{Z}$: addition and multiplication are commutative and associative, multiplication distributes over addition, $0$ and $1$ are identities, every integer has a negative, and there are **no zero divisors**: $ab = 0 \Rightarrow a = 0$ or $b = 0$, equivalently, $cx = cy$ with $c \neq 0$ implies $x = y$ ([[§2 Implications#^def-2-8|Def. §2.8]], Eccles Properties 2.3.1; [[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]]). The Project's list of properties of $\mathbb{Z}$ (its §1.1) contains all of these except the last; the last is what makes $bd \neq 0$ whenever $b, d \neq 0$, so that sums and products of fractions are again fractions.

> [!definition] Definition §22.5: The Set of Fractions and Its Relation
> Let
>
> $$
> S = \mathbb{Z} \times (\mathbb{Z} - \{0\}) = \{(a, b) \in \mathbb{Z} \times \mathbb{Z} \mid b \neq 0\} ,
> $$
>
> where $(a, b)$ stands for the potential rational number $a/b$ (numerator $a$, non-zero denominator $b$). On $S$ define
>
> $$
> (a, b) \sim (c, d) \iff ad = bc .
> $$
>
> For example $(1, 2) \sim (2, 4) \sim (3, 6) \sim (-1, -2)$, since $1 \times 4 = 2 \times 2$, and so on.
>
> *Source: Rational Number Project §2.1–2.2*
> *Eccles: §22.3 (after Example 22.3.5)*

^def-22-5

> [!theorem] Lemma §22.6: The Relation on Fractions Is an Equivalence Relation
> The relation $\sim$ on $S$ is reflexive, symmetric and transitive.
>
> *Eccles: Example 22.2.4(f)*
> *Source: Sundstrom §7.3 Exercise 9*
> *The Rational Number Project takes $\sim$ to be an equivalence relation without checking it; transitivity is the step that needs the denominators to be non-zero.*

^lem-22-6

> [!proof]+ Proof
> *Reflexive:* $ab = ba$, so $(a, b) \sim (a, b)$. *Symmetric:* if $ad = bc$ then $cb = da$, i.e. $(c, d) \sim (a, b)$.
>
> *Transitive:* let $(a, b) \sim (c, d)$ and $(c, d) \sim (e, f)$, i.e. $ad = bc$ and $cf = de$. Then
>
> $$
> (af)\,d = (ad)\,f = (bc)\,f = b\,(cf) = b\,(de) = (be)\,d ,
> $$
>
> so $(af - be)\,d = 0$. Since $d \neq 0$ and $\mathbb{Z}$ has no zero divisors, $af = be$, i.e. $(a, b) \sim (e, f)$.
>
> (Eccles argues via $a_1/b_1 = a_2/b_2 \in \mathbb{Q}$; that is fine once $\mathbb{Q}$ is known, but circular when $\sim$ is used to *construct* $\mathbb{Q}$, so here only $\mathbb{Z}$ is used.)

^pf-22-6

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-5|Def. §22.5]], [[§22 Partitions and Equivalence Relations#^def-22-3|Def. §22.3]], [[§22 Partitions and Equivalence Relations#^def-22-new1|Def. §22.3]], [[§4 Proof by Contradiction#^prop-4-4|§4.4]] (no zero divisors)

> [!definition] Definition §22.6: The Rational Numbers
> The set of **rational numbers** is the quotient set
>
> $$
> \mathbb{Q} = S/{\sim} = \{ [(a, b)] \mid a, b \in \mathbb{Z},\ b \neq 0 \} .
> $$
>
> We write $\dfrac{a}{b}$ or $a/b$ for the class $[(a, b)]$. By Theorem [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]], $\ a/b = c/d \iff ad = bc$, and each rational is a single class: all the fractions representing it.
>
> (The Project first names each class by a symbol $q = f([(a, b)])$ through a map $f$ that sends different classes to different symbols, and calls these symbols the rational numbers. Such an $f$ is a bijection from $S/{\sim}$ onto its image, so nothing changes if the classes themselves are taken as the rational numbers, as here.)
>
> *Source: Rational Number Project §2.3–2.5*
> *Eccles: §22.3 (after Example 22.3.5)*

^def-22-6

![[m250-22-1.svg]]
*The pairs $(a, b) \in S$ as lattice points, numerator $a$ across, denominator $b$ up; the row $b = 0$ is excluded. $(a, b) \sim (c, d)$ means $ad = bc$, i.e. the two points lie on the same line through the origin, so each rational number is one such line with its lattice points: $\tfrac12 = \{(1,2), (2,4), (-1,-2), \ldots\}$ (blue), $1$ (red), $2$ (orange), $-\tfrac13$ (green), and $0$ is the whole $b$-axis (black). The origin itself is not in $S$. (A flat version of the 3D plot of $(a, b) \mapsto a/b$ in the Rational Number Project.)*

> [!theorem] Lemma §22.7: Basic Facts About Fractions
> For $(a, b) \in S$:
> 1. $\dfrac{ka}{kb} = \dfrac{a}{b}$ for every integer $k \neq 0$; in particular $\dfrac{a}{b} = \dfrac{-a}{-b}$, so every rational has a representative with positive denominator;
> 2. $\dfrac{a}{b} = \dfrac{0}{1} \iff a = 0$;
> 3. $\dfrac{a}{b} = \dfrac{1}{1} \iff a = b$.
>
> *Source: Rational Number Project §5.5 (used there in computations)*

^lem-22-7

> [!proof]+ Proof
> (1) $(ka, kb) \in S$ since $kb \neq 0$ (no zero divisors), and $(ka)\,b = (kb)\,a$. (2) $(a, b) \sim (0, 1) \iff a \cdot 1 = b \cdot 0 \iff a = 0$. (3) $(a, b) \sim (1, 1) \iff a \cdot 1 = b \cdot 1 \iff a = b$.

^pf-22-7

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-6|Def. §22.6]], [[§22 Partitions and Equivalence Relations#^thm-22-3|§22.3]], [[§4 Proof by Contradiction#^prop-4-4|§4.4]]

> [!definition] Definition §22.7: Addition and Multiplication of Rationals
> For $a/b, c/d \in \mathbb{Q}$ define
>
> $$
> \frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd} ,
> $$
>
> i.e. $[(a, b)] + [(c, d)] = [(ad + bc, bd)]$ and $[(a, b)] \cdot [(c, d)] = [(ac, bd)]$. The right-hand sides are classes of elements of $S$ since $bd \neq 0$ (no zero divisors); so $\mathbb{Q}$ is closed under both operations.
>
> *Source: Rational Number Project §3.1, §4.1, §5.1*
> *Eccles: §22.3 (after Example 22.3.5)*

^def-22-7

> [!remark] Remark: Why These Formulas
> (1) *They are forced by what $a/b$ should mean.* If $q_1$ is to satisfy $b q_1 = a$ and $q_2$ to satisfy $d q_2 = c$, then $bd\,(q_1 + q_2) = ad + bc$ and $bd\, q_1 q_2 = ac$, so $q_1 + q_2$ "is" $(ad + bc)/bd$ and $q_1 q_2$ "is" $ac/bd$ — the computation before [[§13 Number Systems#^def-13-3|Def. §13.3]] (Eccles §13.1).
>
> (2) *They extend integer arithmetic.* Treating the integer $a$ as $a/1$: $\ a/1 + b/1 = (a \cdot 1 + 1 \cdot b)/(1 \cdot 1) = (a + b)/1$ and $(a/1)(b/1) = ab/1$.
>
> (3) *They must respect $\sim$.* The formulas use representatives, so they define operations on classes only if equivalent inputs give equivalent outputs — [[§22 Partitions and Equivalence Relations#^prop-22-8|Proposition §22.8]].
>
> *Source: Rational Number Project §3.2, §4.2; Eccles §13.1*

^rem-22-1

> [!theorem] Proposition §22.8: The Operations Are Well-Defined
> If $(a_1, b_1) \sim (a_2, b_2)$ and $(c_1, d_1) \sim (c_2, d_2)$, then
>
> $$
> (a_1 c_1,\ b_1 d_1) \sim (a_2 c_2,\ b_2 d_2) \quad \text{and} \quad (a_1 d_1 + b_1 c_1,\ b_1 d_1) \sim (a_2 d_2 + b_2 c_2,\ b_2 d_2) .
> $$
>
> So addition and multiplication of rational numbers are well defined. (This is the computation of [[§13 Number Systems#^prop-13-3|Proposition §13.3]], where $\mathbb{Q}$ was assumed; here $ad = bc$ is the definition of $\sim$, and nothing else is used.)
>
> *Source: Rational Number Project §3.3, §4.3*
> *Eccles: Proposition 13.1.5*

^prop-22-8

> [!proof]+ Proof
> The hypotheses are $a_1 b_2 = a_2 b_1$ and $c_1 d_2 = c_2 d_1$.
>
> *Multiplication:* $(a_1 c_1)(b_2 d_2) = (a_1 b_2)(c_1 d_2) = (a_2 b_1)(c_2 d_1) = (a_2 c_2)(b_1 d_1)$.
>
> *Addition:* expanding and substituting,
>
> $$
> \begin{aligned}
> (a_1 d_1 + b_1 c_1)(b_2 d_2) &= (a_1 b_2)\, d_1 d_2 + (c_1 d_2)\, b_1 b_2 \\
> &= (a_2 b_1)\, d_1 d_2 + (c_2 d_1)\, b_1 b_2 = (a_2 d_2 + b_2 c_2)(b_1 d_1) .
> \end{aligned}
> $$

^pf-22-8

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-5|Def. §22.5]], [[§22 Partitions and Equivalence Relations#^def-22-7|Def. §22.7]]

> [!theorem] Theorem §22.9: $\mathbb{Q}$ Is a Field
> With $0 = 0/1$ and $1 = 1/1$, for all $x, y, z \in \mathbb{Q}$:
> 1. *Commutativity:* $x + y = y + x$ and $xy = yx$.
> 2. *Associativity:* $(x + y) + z = x + (y + z)$ and $(xy)z = x(yz)$.
> 3. *Distributivity:* $x(y + z) = xy + xz$.
> 4. *Identities:* $x + 0 = x$ and $x \cdot 1 = x$; and $0 \neq 1$.
> 5. *Additive inverses:* for $x = a/b$, $\ -x := (-a)/b$ satisfies $x + (-x) = 0$.
> 6. *Multiplicative inverses:* if $x \neq 0$, then $x = a/b$ with $a \neq 0$, and $x^{-1} := b/a$ satisfies $x \cdot x^{-1} = 1$.
>
> Subtraction and division are then defined by $x - y = x + (-y)$ and $x \div y = x\, y^{-1}$ ($y \neq 0$).
>
> *Source: Rational Number Project §5 (Theorems 1–6)*
> *In its distributivity step (§5.6) the Project writes $\frac{ac}{bd} + \frac{ae}{bf} = \frac{acf + aed}{bdf}$ directly; by Definition [[§22 Partitions and Equivalence Relations#^def-22-7|§22.7]] the sum is $\frac{b(acf + ade)}{b(bdf)}$, and removing the common factor $b$ is Lemma [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]](1).*

^thm-22-9

> [!proof]+ Proof
> Let $x = a/b$, $y = c/d$, $z = e/f$. Since the operations are well defined (Proposition [[§22 Partitions and Equivalence Relations#^prop-22-8|§22.8]]), each law can be checked on these representatives, using the laws of $\mathbb{Z}$.
>
> (1) $x + y = \dfrac{ad + bc}{bd} = \dfrac{cb + da}{db} = y + x$ and $xy = \dfrac{ac}{bd} = \dfrac{ca}{db} = yx$.
>
> (2) $(x + y) + z = \dfrac{ad + bc}{bd} + \dfrac{e}{f} = \dfrac{adf + bcf + bde}{bdf}$ and $x + (y + z) = \dfrac{a}{b} + \dfrac{cf + de}{df} = \dfrac{adf + bcf + bde}{bdf}$. For products both sides are $\dfrac{ace}{bdf}$.
>
> (3) $x(y + z) = \dfrac{a}{b} \cdot \dfrac{cf + de}{df} = \dfrac{acf + ade}{bdf}$, while
>
> $$
> xy + xz = \frac{ac}{bd} + \frac{ae}{bf} = \frac{ac \cdot bf + bd \cdot ae}{bd \cdot bf} = \frac{b\,(acf + ade)}{b\,(bdf)} = \frac{acf + ade}{bdf}
> $$
>
> by Lemma [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]](1) with $k = b \neq 0$.
>
> (4) $\dfrac{a}{b} + \dfrac{0}{1} = \dfrac{a \cdot 1 + b \cdot 0}{b \cdot 1} = \dfrac{a}{b}$ and $\dfrac{a}{b} \cdot \dfrac{1}{1} = \dfrac{a}{b}$. And $0/1 \neq 1/1$ since $0 \cdot 1 \neq 1 \cdot 1$.
>
> (5) $\dfrac{a}{b} + \dfrac{-a}{b} = \dfrac{ab + b(-a)}{b^2} = \dfrac{0}{b^2} = \dfrac{0}{1}$ by Lemma [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]](2).
>
> (6) If $x = a/b \neq 0/1$ then $a \neq 0$ by Lemma [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]](2), so $(b, a) \in S$ and $\dfrac{a}{b} \cdot \dfrac{b}{a} = \dfrac{ab}{ba} = \dfrac{1}{1}$ by Lemma [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]](3).

^pf-22-9

*Uses:* [[§22 Partitions and Equivalence Relations#^prop-22-8|§22.8]], [[§22 Partitions and Equivalence Relations#^lem-22-7|§22.7]], [[§22 Partitions and Equivalence Relations#^def-22-7|Def. §22.7]]

> [!remark]- Connections
> - The field axioms: [[§3 The Set ℝ of Real Numbers#^def-3-1|451 Def. §3.1]]; $\mathbb{Q}$ as the basic example of a field: [[§2 The Set ℚ of Rational Numbers#^def-2-4|451 Def. §2.4]], [[§3 Basic Examples of Groups#^def-3-3|493 Def. §3.3]].

Finally, $\mathbb{Z}$ sits inside the new $\mathbb{Q}$, and $a/b$ really is $a$ divided by $b$.

> [!theorem] Proposition §22.10: The Integers Inside $\mathbb{Q}$
> The map $\iota : \mathbb{Z} \to \mathbb{Q}$, $\ \iota(a) = a/1$, is injective and preserves the operations:
>
> $$
> \iota(a + b) = \iota(a) + \iota(b), \qquad \iota(ab) = \iota(a)\,\iota(b), \qquad \iota(0) = 0, \quad \iota(1) = 1 .
> $$
>
> Moreover for $(a, b) \in S$, $\ a/b = \iota(a) \cdot \iota(b)^{-1}$, and this is the unique $x \in \mathbb{Q}$ with $\iota(b)\, x = \iota(a)$.
>
> *Source: Rational Number Project §3.2, §4.2*
> *Eccles: §22.3 (after Example 22.3.5)*

^prop-22-10

> [!proof]+ Proof
> *Injective:* $a/1 = c/1 \iff a \cdot 1 = 1 \cdot c \iff a = c$. *Operations:* $\dfrac a1 + \dfrac b1 = \dfrac{a \cdot 1 + 1 \cdot b}{1 \cdot 1} = \dfrac{a + b}{1}$ and $\dfrac a1 \cdot \dfrac b1 = \dfrac{ab}{1}$; $\iota(0) = 0/1 = 0$, $\iota(1) = 1/1 = 1$.
>
> *Division:* $b \neq 0$, so $\iota(b) = b/1 \neq 0$ and $\iota(b)^{-1} = 1/b$ by Theorem [[§22 Partitions and Equivalence Relations#^thm-22-9|§22.9]](6); thus $\iota(a)\,\iota(b)^{-1} = \dfrac a1 \cdot \dfrac 1b = \dfrac ab$. If $\iota(b)\, x = \iota(a)$, multiplying by $\iota(b)^{-1}$ (and using the field laws) gives $x = \iota(b)^{-1}\iota(a)$; and this $x$ is a solution. So the solution exists and is unique.

^pf-22-10

*Uses:* [[§22 Partitions and Equivalence Relations#^thm-22-9|§22.9]], [[§22 Partitions and Equivalence Relations#^def-22-7|Def. §22.7]]

Identifying each integer $a$ with $\iota(a) = a/1$, we get $\mathbb{Z} \subseteq \mathbb{Q}$, the fraction $a/b$ denotes $[(a, b)]$, and we are back to the usual notation — but now $\mathbb{Q}$ has been *built* from $\mathbb{Z}$ rather than assumed. The order extends too: choosing representatives with $b, d > 0$ ([[§22 Partitions and Equivalence Relations#^lem-22-7|Lemma §22.7]](1)), put $a/b < c/d$ iff $ad < bc$; one checks as in [[§22 Partitions and Equivalence Relations#^prop-22-8|Proposition §22.8]] that this does not depend on the choice (Eccles Problems III Q21).

## 22.5 Construction of the Integers

The same idea builds $\mathbb{Z}$ from $\mathbb{N} = \{0, 1, 2, \ldots\}$: a pair $(a, b)$ of natural numbers stands for the difference $a - b$, which need not exist in $\mathbb{N}$, and $(a, b)$, $(c, d)$ should represent the same integer when $a - b = c - d$, i.e. $a + d = b + c$ — a condition stated without subtraction. We use only the following properties of $\mathbb{N}$ (all consequences of Peano's axioms, [[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]]): $+$ and $\cdot$ are commutative and associative, $\cdot$ distributes over $+$, $0$ and $1$ are identities, and
- *cancellation:* $a + c = b + c \Rightarrow a = b$;
- *no zero divisors:* $ab = 0 \Rightarrow a = 0$ or $b = 0$;
- *no negatives:* $a + b = 0 \Rightarrow a = b = 0$;
- *comparison:* for $a, b \in \mathbb{N}$, either $a = b + n$ for some $n \in \mathbb{N}$, or $b = a + n$ for some $n \geq 1$.

> [!definition] Definition §22.8: The Relation on Pairs of Natural Numbers
> On $\mathbb{N} \times \mathbb{N}$ define
>
> $$
> (a, b) \approx (c, d) \iff a + d = b + c .
> $$
>
> *Source: MAT 200 lecture (syllabus week 13); standard*
> *Eccles: Exercise 22.3 (with $\mathbb{Z}^+ \times \mathbb{Z}^+$ and $f(x_1, x_2) = x_1 - x_2$)*

^def-22-8

> [!theorem] Lemma §22.11: $\approx$ Is an Equivalence Relation
> The relation $\approx$ on $\mathbb{N} \times \mathbb{N}$ is reflexive, symmetric and transitive.
>
> *Source: MAT 200 lecture (syllabus week 13); standard*

^lem-22-11

> [!proof]+ Proof
> *Reflexive:* $a + b = b + a$. *Symmetric:* $a + d = b + c \Rightarrow c + b = d + a$. *Transitive:* if $a + d = b + c$ and $c + f = d + e$, then
>
> $$
> (a + f) + (c + d) = (a + d) + (c + f) = (b + c) + (d + e) = (b + e) + (c + d) ,
> $$
>
> and cancelling $c + d$ gives $a + f = b + e$, i.e. $(a, b) \approx (e, f)$.

^pf-22-11

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-8|Def. §22.8]], [[§22 Partitions and Equivalence Relations#^def-22-3|Def. §22.3]], [[§22 Partitions and Equivalence Relations#^def-22-new1|Def. §22.3]]

> [!definition] Definition §22.9: The Integers
> The set of **integers** is the quotient set $\mathbb{Z} = (\mathbb{N} \times \mathbb{N})/{\approx}$, with
>
> $$
> [(a, b)] + [(c, d)] = [(a + c,\ b + d)], \qquad [(a, b)] \cdot [(c, d)] = [(ac + bd,\ ad + bc)] .
> $$
>
> (Motivation: $(a - b) + (c - d) = (a + c) - (b + d)$ and $(a - b)(c - d) = (ac + bd) - (ad + bc)$.)
>
> *Source: MAT 200 lecture (syllabus week 13); standard*

^def-22-9

![[m250-22-2.svg]]
*$\mathbb{N} \times \mathbb{N}$ near the origin. $(a, b) \approx (c, d)$ means $a + d = b + c$, i.e. $a - b = c - d$: the classes are the diagonals $a - b = \text{const}$, each labelled by the integer it becomes. The diagonal through $(n, 0)$ is $n$, the one through $(0, n)$ is $-n$, and the main diagonal is $0$.*

> [!theorem] Proposition §22.12: The Operations on $\mathbb{Z}$ Are Well-Defined
> If $(a, b) \approx (a', b')$ and $(c, d) \approx (c', d')$, then
>
> $$
> (a + c,\ b + d) \approx (a' + c',\ b' + d') \quad \text{and} \quad (ac + bd,\ ad + bc) \approx (a'c' + b'd',\ a'd' + b'c') .
> $$
>
> *Source: MAT 200 lecture (syllabus week 13); standard*

^prop-22-12

> [!proof]+ Proof
> Both formulas are symmetric in the two arguments: swapping $(a, b)$ and $(c, d)$ gives $(c + a, d + b)$ and $(ca + db, cb + da)$, the same pairs. So it suffices to change the *first* argument with the second fixed (then change the second the same way, and chain the two by transitivity). Let $(a, b) \approx (a', b')$ and put $s = a + b' = b + a'$.
>
> *Sum:* $(a + c) + (b' + d) = (a + b') + c + d = (b + a') + c + d = (b + d) + (a' + c)$, i.e. $(a + c, b + d) \approx (a' + c, b' + d)$.
>
> *Product:* we need $(ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd)$. Grouping,
>
> $$
> (ac + bd) + (a'd + b'c) = (a + b')\,c + (b + a')\,d = sc + sd, \qquad (ad + bc) + (a'c + b'd) = (b + a')\,c + (a + b')\,d = sc + sd .
> $$

^pf-22-12

*Uses:* [[§22 Partitions and Equivalence Relations#^def-22-8|Def. §22.8]], [[§22 Partitions and Equivalence Relations#^def-22-9|Def. §22.9]], [[§22 Partitions and Equivalence Relations#^lem-22-11|§22.11]]

> [!theorem] Theorem §22.13: The Integers
> Let $0 = [(0, 0)]$ and $1 = [(1, 0)]$.
> 1. $\mathbb{Z}$ satisfies the commutative, associative and distributive laws; $0$ and $1$ are identities for $+$ and $\cdot$; and every $x = [(a, b)]$ has the additive inverse $-x = [(b, a)]$.
> 2. The map $j : \mathbb{N} \to \mathbb{Z}$, $j(n) = [(n, 0)]$, is injective and satisfies $j(n + k) = j(n) + j(k)$, $j(nk) = j(n)\,j(k)$.
> 3. Every integer is exactly one of: $j(n)$ with $n \geq 1$; $\ 0$; $\ -j(n)$ with $n \geq 1$.
> 4. $\mathbb{Z}$ has no zero divisors: $xy = 0 \Rightarrow x = 0$ or $y = 0$.
>
> *Source: MAT 200 lecture (syllabus week 13); standard*

^thm-22-13

> [!proof]+ Proof
> (1) Commutativity of both operations is the symmetry noted in the proof of Proposition [[§22 Partitions and Equivalence Relations#^prop-22-12|§22.12]]. Addition is associative coordinatewise. For multiplication, with $x = [(a, b)]$, $y = [(c, d)]$, $z = [(e, f)]$, both $(xy)z$ and $x(yz)$ equal
>
> $$
> [(ace + adf + bcf + bde,\ \ acf + ade + bce + bdf)] ,
> $$
>
> e.g. $(xy)z = [(ac + bd, ad + bc)] \cdot [(e, f)] = [((ac + bd)e + (ad + bc)f,\ (ac + bd)f + (ad + bc)e)]$. Distributivity: $x(y + z) = [(a, b)] \cdot [(c + e, d + f)] = [(ac + ae + bd + bf,\ ad + af + bc + be)]$, which is $xy + xz = [(ac + bd, ad + bc)] + [(ae + bf, af + be)]$. Identities: $[(a, b)] + [(0, 0)] = [(a, b)]$ and $[(a, b)] \cdot [(1, 0)] = [(a \cdot 1 + b \cdot 0,\ a \cdot 0 + b \cdot 1)] = [(a, b)]$. Inverses: $[(a, b)] + [(b, a)] = [(a + b, b + a)] = [(0, 0)]$, since $(a + b) + 0 = (b + a) + 0$.
>
> (2) $j(n) = j(k) \iff n + 0 = 0 + k \iff n = k$. Also $j(n) + j(k) = [(n + k, 0)]$ and $j(n)\,j(k) = [(nk + 0 \cdot 0,\ n \cdot 0 + 0 \cdot k)] = [(nk, 0)]$.
>
> (3) Given $(a, b)$, by comparison either $a = b + n$ with $n \in \mathbb{N}$, and then $(a, b) \approx (n, 0)$ since $a + 0 = b + n$; or $b = a + n$ with $n \geq 1$, and then $(a, b) \approx (0, n)$ and $[(0, n)] = -j(n)$. So every integer is $j(n)$ ($n \geq 0$, with $j(0) = 0$) or $-j(n)$ ($n \geq 1$). These are distinct: $j(n) = -j(k)$ means $(n, 0) \approx (0, k)$, i.e. $n + k = 0$, which forces $n = k = 0$.
>
> (4) Using (3) write $x = \pm j(n)$, $y = \pm j(k)$. The rules $(-u)v = -(uv)$ and $(-u)(-v) = uv$ follow from (1) as in any number system, so $xy = \pm j(n)j(k) = \pm j(nk)$. If $xy = 0$ then $j(nk) = 0 = j(0)$ (as $-w = 0 \Rightarrow w = -(-w) = 0$), so $nk = 0$ by (2), hence $n = 0$ or $k = 0$, i.e. $x = 0$ or $y = 0$.

^pf-22-13

*Uses:* [[§22 Partitions and Equivalence Relations#^prop-22-12|§22.12]], [[§22 Partitions and Equivalence Relations#^def-22-9|Def. §22.9]], [[§22 Partitions and Equivalence Relations#^lem-22-11|§22.11]]

Identifying $n \in \mathbb{N}$ with $j(n)$ gives $\mathbb{N} \subseteq \mathbb{Z}$, and then $[(a, b)] = j(a) + (-j(b)) = a - b$: every integer is a difference of natural numbers. Parts (1) and (4) are exactly the properties of $\mathbb{Z}$ used in 22.4, so the two constructions compose: starting from $\mathbb{N}$ (Peano), quotient sets produce $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q}$ with all the arithmetic that [[§13 Number Systems|§13]] assumed. (Building $\mathbb{R}$ from $\mathbb{Q}$ needs a different idea, completeness.)

> [!remark]- Connections
> - The starting point, Peano's axioms: [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]]; the informal passage $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q}$ via semigroup, ring and field: [[§2 The Set ℚ of Rational Numbers#^def-2-3|451 Def. §2.3]] (ring), [[§2 The Set ℚ of Rational Numbers#^def-2-4|451 Def. §2.4]] (field).
> - $\mathbb{Z}$ under $+$ as a group: [[§3 Basic Examples of Groups#^def-3-1|493 Def. §3.1]]; the completion of $\mathbb{Q}$ to $\mathbb{R}$: [[§6 Dedekind Cuts#^def-6-1|451 Def. §6.1]] (Dedekind cuts), which yields the [[Completeness Axiom]].
