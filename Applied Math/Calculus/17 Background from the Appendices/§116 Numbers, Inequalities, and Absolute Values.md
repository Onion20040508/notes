---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 116
stewart: "Appendix A"
aliases: ["Stewart Appendix A"]
tags: [calculus]
---
← [[§115 The Divergence Theorem]] · ↑ [[· 17 Background from the Appendices]] · [[§117 Coordinate Geometry and Lines]] →

*Stewart, Appendix A.*

The background on real numbers that the rest of the course takes for granted: the number systems, the real line and its order, intervals, the rules for manipulating inequalities, and the absolute value with the Triangle Inequality. The working skill is solving inequalities, including those with absolute values, by the rules below or by sign charts. The absolute value $|a - b|$ is the distance between $a$ and $b$, which is how "close to" is made precise in the definition of a limit ([[§9 The Precise Definition of a Limit|§9]]). The rigorous construction of $\mathbb{R}$ and its order is in Single Variable Analysis (451 §3–§4).

## Numbers and the Real Line

> [!definition] Definition §116.1: Integers, Rational, Irrational and Real Numbers
> - The **integers** are $\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots$.
> - The **rational numbers** are the ratios of integers: $r = \dfrac mn$ with $m$, $n$ integers and $n \ne 0$. (Division by $0$ is always ruled out, so $\frac30$ and $\frac00$ are undefined.) For example $\frac12$, $-\frac37$, $46 = \frac{46}{1}$, $0.17 = \frac{17}{100}$.
> - Real numbers that cannot be expressed as a ratio of integers, such as $\sqrt2$, are **irrational numbers**. Further examples are $\sqrt3$, $\sqrt5$, $\sqrt[3]{2}$, $\pi$, $\sin 1°$ and $\log_{10} 2$ (with varying degrees of difficulty).
> - The set of all real numbers is denoted $\mathbb{R}$; "number" without qualification means real number.
>
> *Stewart: Appendix A (text)*

^def-116-1

> [!theorem] Proposition §116.1: Decimal Representations
> Every real number has a decimal representation. A number is rational exactly when its decimal is repeating, as in
>
> $$
> \tfrac12 = 0.5000\ldots = 0.5\overline{0}, \qquad \tfrac23 = 0.\overline{6}, \qquad \tfrac{157}{495} = 0.3\overline{17}, \qquad \tfrac97 = 1.\overline{285714}
> $$
>
> (the bar marks the block that repeats forever); an irrational number has a nonrepeating decimal, such as $\sqrt2 = 1.414213562373095\ldots$ and $\pi = 3.141592653589793\ldots$. Stopping a decimal expansion gives an approximation, such as $\pi \approx 3.14159265$; the more places retained, the better the approximation.
>
> *Stewart: Appendix A (text)*

^prop-116-1

*Stewart states this without proof. That a repeating decimal is rational is proved in [[§13 Number Systems#^thm-13-7|250 Thm. §13.7]]; conversely, long division of $m$ by $n$ has only $n$ possible remainders, so the digits must eventually repeat.*

> [!definition] Definition §116.2: The Real Line
> Choose a point $O$, the **origin**, on a line, a positive direction (to the right) and a unit of measurement. Each positive number $x$ is represented by the point at distance $x$ to the right of $O$, each negative number $-x$ by the point $x$ units to the left, and $0$ by $O$. Every real number corresponds to exactly one point and every point $P$ to exactly one real number, the **coordinate** of $P$. The line is then a **coordinate line**, **real number line**, or **real line**, and we identify a point with its coordinate.
>
> *Stewart: Appendix A (text)*

^def-116-2

> [!definition] Definition §116.3: Order
> $a$ **is less than** $b$, written $a < b$ (equivalently $b > a$, "$b$ is greater than $a$"), if $b - a$ is a positive number. Geometrically, $a$ lies to the left of $b$ on the real line. $a \le b$ (or $b \ge a$) means that $a < b$ or $a = b$. For example $7 < 7.4 < 7.5$, $-3 > -\pi$, $\sqrt2 < 2$, $\sqrt2 \le 2$ and $2 \le 2$ are all true.
>
> *Stewart: Appendix A (text)*

^def-116-3

> [!definition] Definition §116.4: Set Notation
> A **set** is a collection of objects, its **elements**; $a \in S$ means that $a$ is an element of $S$ and $a \notin S$ that it is not. The **union** $S \cup T$ consists of the elements in $S$ or $T$ (or both), the **intersection** $S \cap T$ of the elements in both, and $\varnothing$ is the **empty set**. A set can be described by listing its elements, $A = \{1, 2, 3, 4, 5, 6\}$, or in **set-builder notation**, $A = \{x \mid x \text{ is an integer and } 0 < x < 7\}$, read "the set of $x$ such that $x$ is an integer and $0 < x < 7$".
>
> *Stewart: Appendix A (text)*

^def-116-4

## Intervals

> [!definition] Definition §116.5: Intervals
> For $a < b$ the nine types of **intervals** are:
>
> | notation | set description | | notation | set description |
> |---|---|---|---|---|
> | $(a, b)$ | $\{x \mid a < x < b\}$ | | $(a, \infty)$ | $\{x \mid x > a\}$ |
> | $[a, b]$ | $\{x \mid a \le x \le b\}$ | | $[a, \infty)$ | $\{x \mid x \ge a\}$ |
> | $[a, b)$ | $\{x \mid a \le x < b\}$ | | $(-\infty, b)$ | $\{x \mid x < b\}$ |
> | $(a, b]$ | $\{x \mid a < x \le b\}$ | | $(-\infty, b]$ | $\{x \mid x \le b\}$ |
> | | | | $(-\infty, \infty)$ | $\mathbb{R}$ |
>
> $(a, b)$ is the **open interval** and $[a, b]$ the **closed interval** from $a$ to $b$. Round brackets (open dots in a picture) exclude an endpoint, square brackets (solid dots) include it. The symbol $\infty$ is not a number: $(a, \infty)$ is the set of all numbers greater than $a$, and $\infty$ only indicates that the interval extends indefinitely in the positive direction.
>
> *Stewart: Appendix A, Table 1*

^def-116-5

## Inequalities

> [!theorem] Theorem §116.2: Rules for Inequalities
> 1. If $a < b$, then $a + c < b + c$.
> 2. If $a < b$ and $c < d$, then $a + c < b + d$.
> 3. If $a < b$ and $c > 0$, then $ac < bc$.
> 4. If $a < b$ and $c < 0$, then $ac > bc$.
> 5. If $0 < a < b$, then $1/a > 1/b$.
>
> In words: a number may be added to both sides (Rule 1) and two inequalities may be added (Rule 2). Multiplying both sides by a *positive* number keeps the direction (Rule 3), but **multiplying by a negative number reverses the direction of the inequality** (Rule 4): $3 < 5$ gives $6 < 10$ when multiplied by $2$, but $-6 > -10$ when multiplied by $-2$. Taking reciprocals of positive numbers reverses the direction (Rule 5).
>
> *Stewart: Appendix A, (2) Rules for Inequalities*

^thm-116-2

> [!proof]+ Proof
> Stewart explains the rules but does not prove them. They follow from Definition §116.3 and the facts that sums and products of positive numbers are positive.
> 1. $(b + c) - (a + c) = b - a > 0$.
> 2. $(b + d) - (a + c) = (b - a) + (d - c)$, a sum of two positive numbers.
> 3. $bc - ac = (b - a)c$, a product of two positive numbers.
> 4. $ac - bc = (b - a)(-c)$, a product of two positive numbers, since $-c > 0$.
> 5. $\dfrac1a - \dfrac1b = \dfrac{b - a}{ab} = (b - a) \cdot \dfrac{1}{ab}$. Here $ab > 0$, so $\frac{1}{ab} > 0$ (if it were negative, $1 = ab \cdot \frac{1}{ab}$ would be negative by Rule 4), and the product is positive.

^pf-116-2

*Uses:* [[§116 Numbers, Inequalities, and Absolute Values#^def-116-3|Def. §116.3]]

> [!remark]- Connections
> - The same rules from the axioms of an ordered field: [[§3 The Set ℝ of Real Numbers#^prop-3-1|451 Prop. §3.1]]; the order axioms and first consequences in 250: [[§3 Proofs#^def-3-1|250 Def. §3.1]], [[§4 Proof by Contradiction#^prop-4-3|250 Prop. §4.3]].

To **solve** an inequality is to find its **solution set**, the set of all numbers $x$ for which it is true.

> [!example] Example §116.1: Linear Inequalities
> **(a)** Solve $1 + x < 7x + 5$. Subtract $1$ (Rule 1 with $c = -1$): $x < 7x + 4$. Subtract $7x$ (Rule 1 with $c = -7x$): $-6x < 4$. Divide by $-6$, that is, multiply by $c = -\frac16 < 0$, which reverses the inequality (Rule 4): $x > -\frac46 = -\frac23$. Each step can be reversed, so the solution set is the interval $(-\frac23, \infty)$.
>
> **(b)** Solve $4 \le 3x - 2 < 13$. The solution set consists of the $x$ satisfying both inequalities. Adding $2$ and then dividing by $3$ gives the equivalent inequalities $6 \le 3x < 15$ and $2 \le x < 5$. The solution set is $[2, 5)$.
>
> *Stewart: Appendix A, Examples 1 and 2*

^ex-116-1

> [!remark] Remark: Method — Sign Charts for Polynomial Inequalities
> To solve $p(x) > 0$, $p(x) \ge 0$, $p(x) < 0$ or $p(x) \le 0$:
> 1. Move all terms to one side and factor.
> 2. The zeros of the factors divide the real line into intervals. On each interval no factor changes sign (a factor $x - r$ is negative to the left of $r$ and positive to the right).
> 3. Record the sign of each factor on each interval in a chart, and multiply. (Alternatively, evaluate $p$ at one **test value** in each interval.)
> 4. Read off the intervals where the product has the required sign; include the zeros when the inequality is $\ge$ or $\le$.

^rem-116-1

> [!example] Example §116.2: Quadratic and Cubic Inequalities
> **(a)** Solve $x^2 - 5x + 6 \le 0$. Factor: $(x - 2)(x - 3) \le 0$. The zeros $2$ and $3$ divide the line into $(-\infty, 2)$, $(2, 3)$, $(3, \infty)$:
>
> | interval | $x - 2$ | $x - 3$ | $(x - 2)(x - 3)$ |
> |---|---|---|---|
> | $x < 2$ | $-$ | $-$ | $+$ |
> | $2 < x < 3$ | $+$ | $-$ | $-$ |
> | $x > 3$ | $+$ | $+$ | $+$ |
>
> (Test value: $x = 1$ gives $1 - 5 + 6 = 2 > 0$ on the first interval.) The product is negative on $(2, 3)$ and zero at $2$ and $3$, so the solution set is $\{x \mid 2 \le x \le 3\} = [2, 3]$. Graphically, the parabola $y = x^2 - 5x + 6$ lies on or below the $x$-axis exactly for $2 \le x \le 3$.
>
> **(b)** Solve $x^3 + 3x^2 > 4x$. Move everything to one side and factor: $x^3 + 3x^2 - 4x = x(x^2 + 3x - 4) = x(x - 1)(x + 4) > 0$. The zeros $-4, 0, 1$ give four intervals:
>
> | interval | $x$ | $x - 1$ | $x + 4$ | $x(x - 1)(x + 4)$ |
> |---|---|---|---|---|
> | $x < -4$ | $-$ | $-$ | $-$ | $-$ |
> | $-4 < x < 0$ | $-$ | $-$ | $+$ | $+$ |
> | $0 < x < 1$ | $+$ | $-$ | $+$ | $-$ |
> | $x > 1$ | $+$ | $+$ | $+$ | $+$ |
>
> The solution set is $\{x \mid -4 < x < 0 \text{ or } x > 1\} = (-4, 0) \cup (1, \infty)$ (strict inequality, so the zeros are excluded).
>
> *Stewart: Appendix A, Examples 3 and 4*

^ex-116-2

## Absolute Value

> [!definition] Definition §116.6: Absolute Value
> The **absolute value** $|a|$ of a number $a$ is the distance from $a$ to $0$ on the real line. So $|a| \ge 0$ for every $a$, and
>
> $$
> |a| = a \ \text{ if } a \ge 0, \qquad |a| = -a \ \text{ if } a < 0 . \qquad (3)
> $$
>
> (If $a$ is negative, $-a$ is positive.) For example $|3| = |-3| = 3$, $|0| = 0$, $|\sqrt2 - 1| = \sqrt2 - 1$, $|3 - \pi| = \pi - 3$. The **distance** between $a$ and $b$ is $|a - b| = |b - a|$.
>
> *Stewart: Appendix A, (3)*

^def-116-6

> [!remark]- Connections
> - The same definition in 451, [[§3 The Set ℝ of Real Numbers#^def-3-4|451 Def. §3.4]], and in 250, [[§1 The Language of Mathematics#^def-1-4|250 Def. §1.4]]; the distance $|a - b|$ is the metric of $\mathbb{R}$ ([[§3 The Set ℝ of Real Numbers#^def-3-5|451 Def. §3.5]]).

> [!theorem] Proposition §116.3: The Square Root of a Square
> For every real number $a$,
>
> $$
> \sqrt{a^2} = |a| .
> $$
>
> The equation $\sqrt{a^2} = a$ is **not** always true: it holds only when $a \ge 0$.
>
> *Stewart: Appendix A, (4)*

^prop-116-3

> [!proof]+ Proof
> $\sqrt r$ means the positive (nonnegative) square root of $r$: $\sqrt r = s$ means $s^2 = r$ and $s \ge 0$. If $a \ge 0$, then $s = a$ satisfies $s^2 = a^2$ and $s \ge 0$, so $\sqrt{a^2} = a = |a|$. If $a < 0$, then $-a > 0$ and $(-a)^2 = a^2$, so $\sqrt{a^2} = -a = |a|$, by (3).

^pf-116-3

*Uses:* [[§116 Numbers, Inequalities, and Absolute Values#^def-116-6|Def. §116.6]]

> [!theorem] Theorem §116.4: Properties of Absolute Values
> Suppose $a$ and $b$ are any real numbers and $n$ is an integer. Then
>
> $$
> 1.\ |ab| = |a|\,|b| \qquad 2.\ \Big|\frac ab\Big| = \frac{|a|}{|b|} \ (b \ne 0) \qquad 3.\ |a^n| = |a|^n \ (a \ne 0 \text{ if } n < 0) .
> $$
>
> *Stewart: Appendix A, (5) Properties of Absolute Values*

^thm-116-4

> [!proof]+ Proof
> Stewart gives hints in the exercises. 1. By Proposition §116.3, $|ab| = \sqrt{(ab)^2} = \sqrt{a^2b^2} = \sqrt{a^2}\,\sqrt{b^2} = |a|\,|b|$, since $\sqrt{a^2}\sqrt{b^2}$ is $\ge 0$ and its square is $a^2b^2$. 2. By Property 1, $|b| \cdot \big|\frac ab\big| = \big|b \cdot \frac ab\big| = |a|$; divide by $|b| \ne 0$. 3. For $n \ge 0$, by induction on $n$: $|a^0| = 1 = |a|^0$, and $|a^{n+1}| = |a^n \cdot a| = |a^n|\,|a| = |a|^n|a| = |a|^{n+1}$ by Property 1. For $n = -m < 0$, Property 2 gives $|a^{-m}| = \big|\frac{1}{a^m}\big| = \frac{1}{|a^m|} = \frac{1}{|a|^m} = |a|^{-m}$.

^pf-116-4

*Uses:* [[§116 Numbers, Inequalities, and Absolute Values#^prop-116-3|§116.3]], induction ([[§120 Sigma Notation|§120]])

> [!theorem] Theorem §116.5: Equations and Inequalities with Absolute Values
> Suppose $a > 0$. Then
>
> 4. $|x| = a$ if and only if $x = \pm a$;
> 5. $|x| < a$ if and only if $-a < x < a$;
> 6. $|x| > a$ if and only if $x > a$ or $x < -a$.
>
> Geometrically, $|x| < a$ says that the distance from $x$ to the origin is less than $a$, that is, $x$ lies between $-a$ and $a$.
>
> *Stewart: Appendix A, (6)*

^thm-116-5

> [!proof]+ Proof
> Split into the cases of (3). If $x \ge 0$, then $|x| = x$, and the three statements read $x = a$; $0 \le x < a$; $x > a$. If $x < 0$, then $|x| = -x$, and they read $-x = a$, i.e. $x = -a$; $0 < -x < a$, i.e. $-a < x < 0$; $-x > a$, i.e. $x < -a$ (Rule 4 of Theorem §116.2). Combining the two cases gives 4, 5 and 6.

^pf-116-5

*Uses:* [[§116 Numbers, Inequalities, and Absolute Values#^def-116-6|Def. §116.6]], [[§116 Numbers, Inequalities, and Absolute Values#^thm-116-2|§116.2]]

> [!example] Example §116.3: Absolute Value Equations and Inequalities
> **(a)** Without the absolute-value symbol, by (3):
>
> $$
> |3x - 2| = \begin{cases} 3x - 2 & \text{if } 3x - 2 \ge 0 \\ -(3x - 2) & \text{if } 3x - 2 < 0 \end{cases} = \begin{cases} 3x - 2 & \text{if } x \ge \frac23 \\ 2 - 3x & \text{if } x < \frac23 . \end{cases}
> $$
>
> **(b)** $|2x - 5| = 3$. By Property 4, $2x - 5 = 3$ or $2x - 5 = -3$, so $2x = 8$ or $2x = 2$: $x = 4$ or $x = 1$.
>
> **(c)** $|x - 5| < 2$. By Property 5, $-2 < x - 5 < 2$; adding $5$, $3 < x < 7$. The solution set is $(3, 7)$: geometrically, the numbers whose distance from $5$ is less than $2$.
>
> **(d)** $|3x + 2| \ge 4$. By Properties 4 and 6, $3x + 2 \ge 4$ or $3x + 2 \le -4$. In the first case $3x \ge 2$, $x \ge \frac23$; in the second $3x \le -6$, $x \le -2$. The solution set is $\{x \mid x \le -2 \text{ or } x \ge \frac23\} = (-\infty, -2] \cup [\frac23, \infty)$.
>
> *Stewart: Appendix A, Examples 5, 6, 7 and 8*

^ex-116-3

> [!theorem] Theorem §116.6: The Triangle Inequality
> If $a$ and $b$ are any real numbers, then
>
> $$
> |a + b| \le |a| + |b| .
> $$
>
> *Stewart: Appendix A, (7) The Triangle Inequality*

^thm-116-6

> [!remark] Remark: Why It Works
> If $a$ and $b$ are both positive or both negative, the two sides are equal. If they have opposite signs, the left side involves a subtraction and the right side does not.

^rem-116-2

> [!proof]+ Proof
> Since $a$ equals either $|a|$ or $-|a|$, we always have $-|a| \le a \le |a|$; likewise $-|b| \le b \le |b|$. Adding these inequalities (Rule 2 of Theorem §116.2, together with the case of equality),
>
> $$
> -(|a| + |b|) \le a + b \le |a| + |b| .
> $$
>
> By Properties 4 and 5 of Theorem §116.5, with $x$ replaced by $a + b$ and $a$ by $|a| + |b|$ (if $|a| + |b| = 0$ then $a = b = 0$ and there is nothing to prove), this says $|a + b| \le |a| + |b|$.

^pf-116-6

*Uses:* [[§116 Numbers, Inequalities, and Absolute Values#^thm-116-2|§116.2]], [[§116 Numbers, Inequalities, and Absolute Values#^thm-116-5|§116.5]]

> [!remark]- Connections
> - Rigorous treatment, with the same proof: [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]] (hub [[Triangle inequality]]).

> [!example] Example §116.4: Estimating with the Triangle Inequality
> If $|x - 4| < 0.1$ and $|y - 7| < 0.2$, estimate $|(x + y) - 11|$.
>
> Apply Theorem §116.6 with $a = x - 4$ and $b = y - 7$:
>
> $$
> |(x + y) - 11| = |(x - 4) + (y - 7)| \le |x - 4| + |y - 7| < 0.1 + 0.2 = 0.3 .
> $$
>
> So $|(x + y) - 11| < 0.3$. The same estimate is the heart of the proof of the Sum Law for limits ([[§8 Calculating Limits Using the Limit Laws|§8]]; proof in Appendix F).
>
> *Stewart: Appendix A, Example 9*

^ex-116-4
