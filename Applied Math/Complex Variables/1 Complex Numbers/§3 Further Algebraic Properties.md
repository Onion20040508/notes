---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 3
bc: "3"
aliases: ["B&C 3"]
tags: [complex-variables, math342]
---
← [[§2 Basic Algebraic Properties]] · ↑ [[· 1 Complex Numbers]] · [[§4 Vectors and Moduli]] →

*Brown–Churchill, Section 3 · MAT 342 HW 1.*

With the laws of [[§2 Basic Algebraic Properties|§2]] in place, the remaining rules of elementary algebra follow for complex numbers just as they do for real ones. A product vanishes only when a factor does; subtraction and division are defined through the inverses; the usual rules for fractions hold; and the binomial formula expands $(z_1 + z_2)^n$. The one practical skill of the section is division: multiply numerator and denominator by $x_2 - iy_2$, which makes the denominator real.

## Zero Products, Subtraction and Division

> [!theorem] Theorem §3.1: A Product Is Zero Only When a Factor Is
> If $z_1z_2 = 0$, then $z_1 = 0$ or $z_2 = 0$ (or both). Equivalently, if $z_1$ and $z_2$ are nonzero, so is their product $z_1z_2$.
>
> *B&C: Sec. 3 (text)*

^thm-3-1

> [!proof]+ Proof
> Suppose $z_1z_2 = 0$ and $z_1 \ne 0$. Then the inverse $z_1^{-1}$ exists, and since any complex number times zero is zero,
>
> $$
> z_2 = z_2 \cdot 1 = z_2\big(z_1z_1^{-1}\big) = \big(z_1^{-1}z_1\big)z_2 = z_1^{-1}(z_1z_2) = z_1^{-1} \cdot 0 = 0 .
> $$

^pf-3-1

*Uses:* [[§2 Basic Algebraic Properties#^thm-2-1|§2.1]], [[§2 Basic Algebraic Properties#^thm-2-2|§2.2]], [[§2 Basic Algebraic Properties#^thm-2-4|§2.4]], [[§1 Sums and Products#^rem-1-1|§1 Remark]] ($z \cdot 0 = 0$)

> [!definition] Definition §3.1: Subtraction and Division
> Subtraction and division are defined in terms of the additive and multiplicative inverses:
>
> $$
> z_1 - z_2 = z_1 + (-z_2) , \qquad (1)
> $$
>
> $$
> \frac{z_1}{z_2} = z_1z_2^{-1} \qquad (z_2 \ne 0) . \qquad (2)
> $$
>
> *B&C: Sec. 3, Equations (1) and (2)*

^def-3-1

> [!theorem] Proposition §3.2: Differences and Quotients in Coordinates
> For $z_1 = (x_1, y_1) = x_1 + iy_1$ and $z_2 = (x_2, y_2) = x_2 + iy_2$,
>
> $$
> z_1 - z_2 = (x_1 - x_2,\ y_1 - y_2) = (x_1 - x_2) + i(y_1 - y_2) , \qquad (3),\ (5)
> $$
>
> $$
> \frac{z_1}{z_2} = \Big(\frac{x_1x_2 + y_1y_2}{x_2^2 + y_2^2},\ \frac{y_1x_2 - x_1y_2}{x_2^2 + y_2^2}\Big) = \frac{x_1x_2 + y_1y_2}{x_2^2 + y_2^2} + i\,\frac{y_1x_2 - x_1y_2}{x_2^2 + y_2^2} \qquad (z_2 \ne 0) . \qquad (4),\ (6)
> $$
>
> *B&C: Sec. 3, Equations (3)–(6)*

^prop-3-2

> [!proof]+ Proof
> By (1) and the additive inverse $-z_2 = (-x_2, -y_2)$, $z_1 - z_2 = (x_1, y_1) + (-x_2, -y_2) = (x_1 - x_2,\ y_1 - y_2)$. By (2) and the inverse formula (6) of [[§2 Basic Algebraic Properties#^thm-2-4|Theorem §2.4]],
>
> $$
> \frac{z_1}{z_2} = (x_1, y_1)\Big(\frac{x_2}{x_2^2 + y_2^2},\ \frac{-y_2}{x_2^2 + y_2^2}\Big) ,
> $$
>
> and the product rule (4) of [[§1 Sums and Products#^def-1-3|Definition §1.3]] gives the real part $\big(x_1x_2 - y_1(-y_2)\big)/(x_2^2 + y_2^2)$ and the imaginary part $\big(y_1x_2 + x_1(-y_2)\big)/(x_2^2 + y_2^2)$, which is (4). Equations (5) and (6) are (3) and (4) in the notation $x + iy$.

^pf-3-2

*Uses:* [[§3 Further Algebraic Properties#^def-3-1|Def. §3.1]], [[§2 Basic Algebraic Properties#^thm-2-3|§2.3]], [[§2 Basic Algebraic Properties#^thm-2-4|§2.4]], [[§1 Sums and Products#^def-1-3|Def. §1.3]]

## Rules for Quotients

> [!theorem] Proposition §3.3: Rules for Quotients
> Whenever the denominators are nonzero,
>
> $$
> \frac{z_1 + z_2}{z_3} = \frac{z_1}{z_3} + \frac{z_2}{z_3} , \qquad (8)
> $$
>
> $$
> \frac{1}{z_2} = z_2^{-1}, \qquad (9) \qquad\qquad \frac{z_1}{z_2} = z_1\Big(\frac{1}{z_2}\Big), \qquad (10)
> $$
>
> $$
> \Big(\frac{1}{z_1}\Big)\Big(\frac{1}{z_2}\Big) = \frac{1}{z_1z_2}, \qquad (11) \qquad\qquad \Big(\frac{z_1}{z_3}\Big)\Big(\frac{z_2}{z_4}\Big) = \frac{z_1z_2}{z_3z_4} , \qquad (12)
> $$
>
> and the **cancellation law** holds:
>
> $$
> \frac{z_1z}{z_2z} = \frac{z_1}{z_2} \qquad (z_2 \ne 0,\ z \ne 0) .
> $$
>
> *B&C: Sec. 3, Equations (8)–(12) and Exercises 3, 6, 7*

^prop-3-3

> [!proof]+ Proof
> **(8)** By (2) and the distributive law, $(z_1 + z_2)z_3^{-1} = z_1z_3^{-1} + z_2z_3^{-1}$.
>
> **(9), (10)** Equation (2) with $z_1 = 1$ gives $1/z_2 = 1 \cdot z_2^{-1} = z_2^{-1}$, and then (2) reads $z_1/z_2 = z_1(1/z_2)$.
>
> **(11)** By the associative and commutative laws (Exercise 3: $(z_1z_2)(z_3z_4) = (z_1z_3)(z_2z_4)$),
>
> $$
> (z_1z_2)\big(z_1^{-1}z_2^{-1}\big) = \big(z_1z_1^{-1}\big)\big(z_2z_2^{-1}\big) = 1 \cdot 1 = 1 .
> $$
>
> Since $z_1z_2 \ne 0$ (Theorem §3.1), its inverse is unique ([[§2 Basic Algebraic Properties#^thm-2-4|Theorem §2.4]]), so $z_1^{-1}z_2^{-1} = (z_1z_2)^{-1}$. By (9) this is (11).
>
> **(12)** (Exercise 6.) By (10), regrouping, and (11),
>
> $$
> \Big(\frac{z_1}{z_3}\Big)\Big(\frac{z_2}{z_4}\Big) = \Big(z_1\frac{1}{z_3}\Big)\Big(z_2\frac{1}{z_4}\Big) = (z_1z_2)\Big(\frac{1}{z_3}\cdot\frac{1}{z_4}\Big) = (z_1z_2)\frac{1}{z_3z_4} = \frac{z_1z_2}{z_3z_4} .
> $$
>
> **Cancellation** (Exercise 7). By (12), $\dfrac{z_1z}{z_2z} = \dfrac{z_1}{z_2}\cdot\dfrac{z}{z}$, and $z/z = zz^{-1} = 1$.

^pf-3-3

*Uses:* [[§3 Further Algebraic Properties#^def-3-1|Def. §3.1]], [[§3 Further Algebraic Properties#^thm-3-1|§3.1]], [[§2 Basic Algebraic Properties#^thm-2-1|§2.1]], [[§2 Basic Algebraic Properties#^thm-2-4|§2.4]]

> [!remark] Remark: Method — Dividing Complex Numbers
> Formula (6) is not easy to remember. Instead:
> 1. **Multiply numerator and denominator by $x_2 - iy_2$** (allowed by the cancellation law, since $x_2 - iy_2 \ne 0$ when $z_2 \ne 0$):
>
> $$
> \frac{z_1}{z_2} = \frac{(x_1 + iy_1)(x_2 - iy_2)}{(x_2 + iy_2)(x_2 - iy_2)} . \qquad (7)
> $$
>
> 2. **The denominator is now real:** $(x_2 + iy_2)(x_2 - iy_2) = x_2^2 + y_2^2$.
> 3. **Expand the numerator** and split by (8) into real and imaginary parts.
>
> The number $x_2 - iy_2$ is the complex conjugate $\bar z_2$, and step 2 is the identity $z_2\bar z_2 = |z_2|^2$ of [[§6 Complex Conjugates#^prop-6-3|Proposition §6.3]]; that is the reason the method works.

^rem-3-1

## The Binomial Formula

> [!theorem] Theorem §3.4: Binomial Formula
> If $z_1$ and $z_2$ are any two nonzero complex numbers, then
>
> $$
> (z_1 + z_2)^n = \sum_{k=0}^{n}\binom{n}{k}z_1^kz_2^{n-k} \qquad (n = 1, 2, \ldots) , \qquad (13)
> $$
>
> where $\binom{n}{k} = \dfrac{n!}{k!(n - k)!}$ $(k = 0, 1, 2, \ldots, n)$ and $0! = 1$. Because addition is commutative, it can also be written
>
> $$
> (z_1 + z_2)^n = \sum_{k=0}^{n}\binom{n}{k}z_1^{n-k}z_2^{k} \qquad (n = 1, 2, \ldots) . \qquad (14)
> $$
>
> (B&C assume $z_1, z_2 \ne 0$ so that $z^0 = 1$ is defined, [[§8 Products and Powers in Exponential Form#^def-8-1|Definition §8.1]]; with the convention $0^0 = 1$ the formula holds for all $z_1, z_2$.)
>
> *B&C: Sec. 3, Equations (13)–(14) (proof: Exercise 8)*

^thm-3-4

> [!proof]+ Proof
> B&C leave the proof as Exercise 8, by induction on $n$. For $n = 1$ the right side of (13) is $\binom10 z_2 + \binom11 z_1 = z_1 + z_2$. Suppose (13) holds for $n = m$. Then, distributing,
>
> $$
> (z_1 + z_2)^{m+1} = (z_2 + z_1)\sum_{k=0}^{m}\binom{m}{k}z_1^kz_2^{m-k} = \sum_{k=0}^{m}\binom{m}{k}z_1^kz_2^{m+1-k} + \sum_{k=0}^{m}\binom{m}{k}z_1^{k+1}z_2^{m-k} .
> $$
>
> Replace $k$ by $k - 1$ in the last sum, so that it runs over $k = 1, \ldots, m + 1$ with terms $\binom{m}{k-1}z_1^kz_2^{m+1-k}$. Splitting off the term $k = 0$ of the first sum and $k = m + 1$ of the second,
>
> $$
> (z_1 + z_2)^{m+1} = z_2^{m+1} + \sum_{k=1}^{m}\Big[\binom{m}{k} + \binom{m}{k-1}\Big]z_1^kz_2^{m+1-k} + z_1^{m+1} .
> $$
>
> Pascal's rule finishes the step: for $1 \le k \le m$,
>
> $$
> \binom{m}{k} + \binom{m}{k-1} = \frac{m!}{k!(m - k)!} + \frac{m!}{(k - 1)!(m - k + 1)!} = \frac{m!\,\big[(m + 1 - k) + k\big]}{k!(m + 1 - k)!} = \binom{m+1}{k} ,
> $$
>
> and $z_2^{m+1} = \binom{m+1}{0}z_1^0z_2^{m+1}$, $z_1^{m+1} = \binom{m+1}{m+1}z_1^{m+1}z_2^0$. So
>
> $$
> (z_1 + z_2)^{m+1} = \sum_{k=0}^{m+1}\binom{m+1}{k}z_1^kz_2^{m+1-k} ,
> $$
>
> which is (13) for $n = m + 1$. Formula (14) is (13) with $z_1$ and $z_2$ interchanged.

^pf-3-4

*Uses:* [[§2 Basic Algebraic Properties#^thm-2-1|§2.1]]

> [!remark]- Connections
> - The real binomial theorem, with the same induction: [[§12★ Counting Functions and Subsets#^thm-12-10|250 Thm. §12.10]]. The proof uses only the commutative, associative and distributive laws, so it holds in any field, in particular in $\mathbb{C}$.

## Examples

> [!example] Example §3.1: A Quotient
> Compute $\dfrac{4 + i}{2 - 3i}$.
>
> Multiply numerator and denominator by $2 + 3i$ ([[§3 Further Algebraic Properties#^rem-3-1|Method]]):
>
> $$
> \frac{4 + i}{2 - 3i} = \frac{(4 + i)(2 + 3i)}{(2 - 3i)(2 + 3i)} = \frac{8 + 12i + 2i + 3i^2}{4 + 9} = \frac{5 + 14i}{13} = \frac{5}{13} + \frac{14}{13}i .
> $$
>
> *B&C: Sec. 3, Example*

^ex-3-1

> [!example] Example §3.2: Reducing Quotients to Real Numbers
> Reduce to a real number: **(a)** $\dfrac{1 + 2i}{3 - 4i} + \dfrac{2 - i}{5i}$; **(b)** $\dfrac{5i}{(1 - i)(2 - i)(3 - i)}$; **(c)** $(1 - i)^4$.
>
> **(a)** By the method,
>
> $$
> \frac{1 + 2i}{3 - 4i} = \frac{(1 + 2i)(3 + 4i)}{9 + 16} = \frac{3 + 4i + 6i + 8i^2}{25} = \frac{-5 + 10i}{25} = \frac{-1 + 2i}{5} ,
> $$
>
> and, multiplying by $-i$ above and below (the denominator becomes $5i(-i) = 5$),
>
> $$
> \frac{2 - i}{5i} = \frac{(2 - i)(-i)}{5} = \frac{-2i + i^2}{5} = \frac{-1 - 2i}{5} .
> $$
>
> The sum is $\dfrac{(-1 + 2i) + (-1 - 2i)}{5} = -\dfrac25$.
>
> **(b)** The denominator: $(1 - i)(2 - i) = 2 - i - 2i + i^2 = 1 - 3i$, and $(1 - 3i)(3 - i) = 3 - i - 9i + 3i^2 = -10i$. So the quotient is $\dfrac{5i}{-10i} = -\dfrac12$.
>
> **(c)** By the binomial formula (14) with $z_1 = 1$, $z_2 = -i$, and $i^2 = -1$, $i^3 = -i$, $i^4 = 1$:
>
> $$
> (1 - i)^4 = 1 + 4(-i) + 6(-i)^2 + 4(-i)^3 + (-i)^4 = 1 - 4i - 6 + 4i + 1 = -4 .
> $$
>
> (Check: $(1 - i)^2 = -2i$ and $(-2i)^2 = -4$.)
>
> *B&C: Sec. 3, Exercise 1; Source: 342 HW 1 (part (a))*

^ex-3-2

> [!example] Example §3.3: Three Factors
> Prove that if $z_1z_2z_3 = 0$, then at least one of the three factors is zero.
>
> Write $z_1z_2z_3 = (z_1z_2)z_3$. By Theorem §3.1 applied to the two factors $z_1z_2$ and $z_3$, either $z_3 = 0$ or $z_1z_2 = 0$; in the second case, Theorem §3.1 again gives $z_1 = 0$ or $z_2 = 0$.
>
> *B&C: Sec. 3, Exercise 4*

^ex-3-3
