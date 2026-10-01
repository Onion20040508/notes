---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 120
stewart: "Appendix E"
aliases: ["Stewart Appendix E"]
tags: [calculus]
---
← [[§119 Trigonometry]] · ↑ [[· 17 Background from the Appendices]] · [[§121 The Logarithm Defined as an Integral]] →

*Stewart, Appendix E.*

Sigma notation writes a long sum compactly, and three rules (constants factor out, sums split) let one manipulate it like an integral. The closed forms for $\sum 1$, $\sum i$, $\sum i^2$ and $\sum i^3$, proved here by Gauss's pairing trick, a telescoping sum and mathematical induction, are exactly what is needed to evaluate limits of Riemann sums by hand in Chapter 5 ([[§34 The Area and Distance Problems#^def-34-1|Definition §34.1]], [[§35 The Definite Integral#^thm-35-2|Theorem §35.2]]); the last example is such a limit.

> [!definition] Definition §120.1: Sigma Notation
> If $a_m, a_{m+1}, \ldots, a_n$ are real numbers and $m$ and $n$ are integers with $m \le n$, then
>
> $$
> \sum_{i=m}^{n} a_i = a_m + a_{m+1} + a_{m+2} + \cdots + a_{n-1} + a_n .
> $$
>
> With function notation, $\displaystyle\sum_{i=m}^n f(i) = f(m) + f(m + 1) + \cdots + f(n - 1) + f(n)$. The letter $i$, the **index of summation**, takes the consecutive integer values $m, m + 1, \ldots, n$: $\Sigma$ says "add", $i = m$ where to start, $n$ where to end. Other letters can be used for the index.
>
> *Stewart: Appendix E, Definition 1*

^def-120-1

> [!remark]- Connections
> - The precise (inductive) definition, $\sum_{i=1}^{k+1} a(i) = \sum_{i=1}^k a(i) + a(k + 1)$: [[§5 The Induction Principle#^def-5-2|250 Def. §5.2]].

> [!example] Example §120.1: Reading and Writing Sigma Notation
> **Expanding.**
>
> $$
> \sum_{i=1}^4 i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 30, \qquad \sum_{j=0}^5 2^j = 2^0 + 2^1 + \cdots + 2^5 = 63, \qquad \sum_{i=3}^n i = 3 + 4 + \cdots + (n - 1) + n ,
> $$
>
> $$
> \sum_{k=1}^n \frac1k = 1 + \frac12 + \frac13 + \cdots + \frac1n, \qquad \sum_{i=1}^3 \frac{i - 1}{i^2 + 3} = 0 + \frac17 + \frac{2}{12} = \frac{6}{42} + \frac{7}{42} = \frac{13}{42}, \qquad \sum_{i=1}^4 2 = 2 + 2 + 2 + 2 = 8 .
> $$
>
> **Writing.** There is no unique way to write a sum in sigma notation:
>
> $$
> 2^3 + 3^3 + \cdots + n^3 = \sum_{i=2}^n i^3 = \sum_{j=1}^{n-1} (j + 1)^3 = \sum_{k=0}^{n-2} (k + 2)^3 ,
> $$
>
> shifting the index ($j = i - 1$, $k = i - 2$) and the limits together.
>
> *Stewart: Appendix E, Examples 1 and 2*

^ex-120-1

> [!theorem] Theorem §120.1: Rules for Sums
> If $c$ is any constant (it does not depend on $i$), then
>
> $$
> \text{(a)}\ \sum_{i=m}^n ca_i = c\sum_{i=m}^n a_i, \qquad \text{(b)}\ \sum_{i=m}^n (a_i + b_i) = \sum_{i=m}^n a_i + \sum_{i=m}^n b_i, \qquad \text{(c)}\ \sum_{i=m}^n (a_i - b_i) = \sum_{i=m}^n a_i - \sum_{i=m}^n b_i .
> $$
>
> *Stewart: Appendix E, Theorem 2*

^thm-120-1

> [!proof]+ Proof
> Write both sides in expanded form. Rule (a) is the distributive property of real numbers:
>
> $$
> ca_m + ca_{m+1} + \cdots + ca_n = c(a_m + a_{m+1} + \cdots + a_n) .
> $$
>
> Rule (b) follows from the associative and commutative properties of addition:
>
> $$
> (a_m + b_m) + (a_{m+1} + b_{m+1}) + \cdots + (a_n + b_n) = (a_m + a_{m+1} + \cdots + a_n) + (b_m + b_{m+1} + \cdots + b_n) .
> $$
>
> Rule (c) follows from (a) with $c = -1$ and (b): $\sum (a_i - b_i) = \sum a_i + \sum (-1)b_i = \sum a_i - \sum b_i$. (With the inductive definition of a sum, each rule is an induction on the number of terms, using these same properties at each step.)

^pf-120-1

*Uses:* [[§120 Sigma Notation#^def-120-1|Def. §120.1]]

Stewart states the same three rules again in 5.2 (Equations 9–11), where they are [[§35 The Definite Integral#^thm-35-3|Theorem §35.3]].

> [!definition] Definition §120.2: Principle of Mathematical Induction
> Let $S_n$ be a statement involving the positive integer $n$. Suppose that
> 1. $S_1$ is true, and
> 2. if $S_k$ is true, then $S_{k+1}$ is true (for every positive integer $k$).
>
> Then $S_n$ is true for all positive integers $n$.
>
> *Stewart: Appendix E (margin); Principles of Problem Solving after Chapter 1*

^def-120-2

> [!remark]- Connections
> - The same principle as an axiom in 250, [[§5 The Induction Principle#^def-5-1|250 Def. §5.1]], and as a theorem from the Peano axioms in 451, [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 Thm. §1.1]].

> [!theorem] Theorem §120.2: Formulas for Power Sums
> Let $c$ be a constant and $n$ a positive integer. Then
>
> $$
> \text{(a)}\ \sum_{i=1}^n 1 = n, \qquad \text{(b)}\ \sum_{i=1}^n c = nc, \qquad \text{(c)}\ \sum_{i=1}^n i = \frac{n(n + 1)}{2},
> $$
>
> $$
> \text{(d)}\ \sum_{i=1}^n i^2 = \frac{n(n + 1)(2n + 1)}{6}, \qquad \text{(e)}\ \sum_{i=1}^n i^3 = \Big[\frac{n(n + 1)}{2}\Big]^2 .
> $$
>
> *Stewart: Appendix E, Theorem 3 (Examples 3, 4, 5)*

^thm-120-2

> [!proof]+ Proof
> **(a), (b).** $\sum_{i=1}^n 1 = 1 + 1 + \cdots + 1$ ($n$ terms) $= n$, and then $\sum c = c\sum 1 = nc$ by Theorem §120.1(a).
>
> **(c)** (Gauss's method, at age ten). Write $S = \sum_{i=1}^n i$ twice, once in the usual order and once in reverse order:
>
> $$
> \begin{aligned}
> S &= 1 + 2 + 3 + \cdots + (n - 1) + n \\
> S &= n + (n - 1) + (n - 2) + \cdots + 2 + 1 .
> \end{aligned}
> $$
>
> Adding the columns, each of the $n$ columns sums to $n + 1$, so $2S = n(n + 1)$ and $S = n(n + 1)/2$.
>
> **(d), first proof (telescoping).** Let $S = \sum_{i=1}^n i^2$. In the telescoping (collapsing) sum
>
> $$
> \sum_{i=1}^n \big[(1 + i)^3 - i^3\big] = (2^3 - 1^3) + (3^3 - 2^3) + (4^3 - 3^3) + \cdots + \big[(n + 1)^3 - n^3\big]
> $$
>
> most terms cancel in pairs, leaving $(n + 1)^3 - 1^3 = n^3 + 3n^2 + 3n$. On the other hand $(1 + i)^3 - i^3 = 3i^2 + 3i + 1$, so by Theorem §120.1 and parts (a) and (c),
>
> $$
> \sum_{i=1}^n \big[(1 + i)^3 - i^3\big] = 3\sum_{i=1}^n i^2 + 3\sum_{i=1}^n i + \sum_{i=1}^n 1 = 3S + \frac{3n(n + 1)}{2} + n = 3S + \tfrac32 n^2 + \tfrac52 n .
> $$
>
> Hence $n^3 + 3n^2 + 3n = 3S + \frac32 n^2 + \frac52 n$, so $3S = n^3 + \frac32 n^2 + \frac12 n$ and
>
> $$
> S = \frac{2n^3 + 3n^2 + n}{6} = \frac{n(n + 1)(2n + 1)}{6} .
> $$
>
> **(d), second proof (induction).** Let $S_n$ be the formula. $S_1$ is true: $1^2 = \frac{1 \cdot 2 \cdot 3}{6}$. Assume $S_k$: $1^2 + \cdots + k^2 = \frac{k(k + 1)(2k + 1)}{6}$. Then
>
> $$
> \begin{aligned}
> 1^2 + \cdots + k^2 + (k + 1)^2 &= \frac{k(k + 1)(2k + 1)}{6} + (k + 1)^2 = (k + 1)\,\frac{k(2k + 1) + 6(k + 1)}{6} = (k + 1)\,\frac{2k^2 + 7k + 6}{6} \\
> &= \frac{(k + 1)(k + 2)(2k + 3)}{6} = \frac{(k + 1)[(k + 1) + 1][2(k + 1) + 1]}{6} ,
> \end{aligned}
> $$
>
> which is $S_{k+1}$. By the Principle of Mathematical Induction, $S_n$ holds for all $n$.
>
> **(e)** (Stewart leaves this to Exercises 37–40; by induction.) For $n = 1$: $1^3 = 1 = \big[\frac{1 \cdot 2}{2}\big]^2$. If $\sum_{i=1}^k i^3 = \frac{k^2(k + 1)^2}{4}$, then
>
> $$
> \sum_{i=1}^{k+1} i^3 = \frac{k^2(k + 1)^2}{4} + (k + 1)^3 = \frac{(k + 1)^2\,(k^2 + 4k + 4)}{4} = \frac{(k + 1)^2(k + 2)^2}{4} = \Big[\frac{(k + 1)(k + 2)}{2}\Big]^2 .
> $$

^pf-120-2

*Uses:* [[§120 Sigma Notation#^thm-120-1|§120.1]], [[§120 Sigma Notation#^def-120-2|Def. §120.2]]

> [!remark]- Connections
> - Part (c) by induction in 250: [[§5 The Induction Principle#^prop-5-5|250 Prop. §5.5]].

> [!example] Example §120.2: Evaluating a Sum with the Formulas
> Evaluate $\displaystyle\sum_{i=1}^n i(4i^2 - 3)$.
>
> By Theorems §120.1 and §120.2,
>
> $$
> \begin{aligned}
> \sum_{i=1}^n i(4i^2 - 3) &= \sum_{i=1}^n (4i^3 - 3i) = 4\sum_{i=1}^n i^3 - 3\sum_{i=1}^n i = 4\Big[\frac{n(n + 1)}{2}\Big]^2 - 3\,\frac{n(n + 1)}{2} \\
> &= \frac{n(n + 1)[2n(n + 1) - 3]}{2} = \frac{n(n + 1)(2n^2 + 2n - 3)}{2} .
> \end{aligned}
> $$
>
> *Stewart: Appendix E, Example 6*

^ex-120-2

> [!example] Example §120.3: A Limit of Sums
> Find $\displaystyle\lim_{n \to \infty} \sum_{i=1}^n \frac3n\Big[\Big(\frac in\Big)^2 + 1\Big]$.
>
> $$
> \begin{aligned}
> \lim_{n \to \infty} \sum_{i=1}^n \frac3n\Big[\Big(\frac in\Big)^2 + 1\Big]
> &= \lim_{n \to \infty} \sum_{i=1}^n \Big[\frac{3}{n^3}i^2 + \frac3n\Big]
> = \lim_{n \to \infty} \Big[\frac{3}{n^3}\sum_{i=1}^n i^2 + \frac3n\sum_{i=1}^n 1\Big] \\
> &= \lim_{n \to \infty} \Big[\frac{3}{n^3}\cdot\frac{n(n + 1)(2n + 1)}{6} + \frac3n \cdot n\Big]
> = \lim_{n \to \infty} \Big[\frac12 \cdot \frac nn \cdot \Big(\frac{n + 1}{n}\Big)\Big(\frac{2n + 1}{n}\Big) + 3\Big] \\
> &= \lim_{n \to \infty} \Big[\frac12 \cdot 1 \cdot \Big(1 + \frac1n\Big)\Big(2 + \frac1n\Big) + 3\Big] = \frac12 \cdot 1 \cdot 1 \cdot 2 + 3 = 4 .
> \end{aligned}
> $$
>
> This is a right-endpoint Riemann sum for $\int_0^3 \big(\frac{x^2}{9} + 1\big)\,dx = 1 + 3 = 4$ (with $x_i = 3i/n$, $\Delta x = 3/n$), the kind of calculation that computes areas by [[§34 The Area and Distance Problems#^def-34-1|Definition §34.1]] and integrals by [[§35 The Definite Integral#^thm-35-2|Theorem §35.2]].
>
> *Stewart: Appendix E, Example 7*

^ex-120-3
