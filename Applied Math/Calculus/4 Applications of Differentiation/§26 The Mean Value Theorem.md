---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 26
stewart: "4.2"
aliases: ["Stewart 4.2"]
tags: [calculus]
---
← [[§25 Maximum and Minimum Values]] · ↑ [[· 4 Applications of Differentiation]] · [[§27 What Derivatives Tell Us About the Shape of a Graph]] →

*Stewart, Section 4.2.*

The Mean Value Theorem says that somewhere between $a$ and $b$ the instantaneous rate of change $f'(c)$ equals the average rate of change $\frac{f(b) - f(a)}{b - a}$. It is proved from Rolle's Theorem, its special case $f(a) = f(b)$, which in turn comes from the Extreme Value Theorem and Fermat's Theorem ([[§25 Maximum and Minimum Values#^thm-25-1|Theorem §25.1]], [[§25 Maximum and Minimum Values#^thm-25-2|Theorem §25.2]]). Like those, it only asserts that some number $c$ exists. Its value is that it turns information about $f'$ into information about $f$. The first instance is proved here: a function with zero derivative on an interval is constant. Most of the results of this chapter, and the theory of antiderivatives ([[§33 Antiderivatives|§33]]), depend on it.

## Rolle's Theorem

> [!theorem] Theorem §26.1: Rolle's Theorem
> Let $f$ be a function that satisfies the following three hypotheses:
> 1. $f$ is continuous on the closed interval $[a, b]$.
> 2. $f$ is differentiable on the open interval $(a, b)$.
> 3. $f(a) = f(b)$.
>
> Then there is a number $c$ in $(a, b)$ such that $f'(c) = 0$.
>
> *Stewart: 4.2, Rolle's Theorem*

^thm-26-1

> [!proof]+ Proof
> There are three cases.
>
> **Case I: $f(x) = k$, a constant.** Then $f'(x) = 0$ for all $x$, so $c$ can be taken to be any number in $(a, b)$.
>
> **Case II: $f(x) > f(a)$ for some $x$ in $(a, b)$.** By the Extreme Value Theorem (which applies by hypothesis 1), $f$ has an absolute maximum value somewhere in $[a, b]$. This maximum is $> f(a) = f(b)$, so it is attained at a number $c$ in the open interval $(a, b)$, not at an endpoint. Then $f$ has a *local* maximum at $c$ (the open interval $(a, b)$ contains $c$), and $f'(c)$ exists by hypothesis 2. By Fermat's Theorem, $f'(c) = 0$.
>
> **Case III: $f(x) < f(a)$ for some $x$ in $(a, b)$.** By the Extreme Value Theorem, $f$ has an absolute minimum value in $[a, b]$, which is $< f(a) = f(b)$, so it is attained at some $c$ in $(a, b)$. Again $f'(c) = 0$ by Fermat's Theorem.
>
> If neither II nor III occurs, then $f(x) = f(a)$ for all $x$ in $[a, b]$, which is Case I.

^pf-26-1

*Uses:* [[§25 Maximum and Minimum Values#^thm-25-1|§25.1]], [[§25 Maximum and Minimum Values#^thm-25-2|§25.2]], [[§25 Maximum and Minimum Values#^def-25-2|Def. §25.2]]

For example, if $s = f(t)$ is the position of a moving object and the object is in the same place at two instants $t = a$ and $t = b$, then at some instant in between its velocity $f'(c)$ is $0$. (A ball thrown straight up is momentarily at rest at the top.)

> [!example] Example §26.1: Exactly One Real Root
> Prove that the equation $x^3 + x - 1 = 0$ has exactly one real solution.
>
> **Existence.** Let $f(x) = x^3 + x - 1$. Then $f(0) = -1 < 0$ and $f(1) = 1 > 0$. $f$ is a polynomial, hence continuous, so by the Intermediate Value Theorem ([[§10 Continuity#^thm-10-10|Theorem §10.10]]) there is a number $c$ between $0$ and $1$ with $f(c) = 0$.
>
> **Uniqueness.** Suppose, for contradiction, that the equation had two solutions $a < b$. Then $f(a) = 0 = f(b)$, and since $f$ is a polynomial it is continuous on $[a, b]$ and differentiable on $(a, b)$. By Rolle's Theorem there is $c \in (a, b)$ with $f'(c) = 0$. But
>
> $$
> f'(x) = 3x^2 + 1 \ge 1 \qquad \text{for all } x
> $$
>
> (since $x^2 \ge 0$), so $f'(x)$ is never $0$. This contradiction shows that the equation cannot have two real solutions.
>
> *Stewart: Example 4.2.2*

^ex-26-1

## The Mean Value Theorem

> [!theorem] Theorem §26.2: The Mean Value Theorem
> Let $f$ be a function that satisfies the following hypotheses:
> 1. $f$ is continuous on the closed interval $[a, b]$.
> 2. $f$ is differentiable on the open interval $(a, b)$.
>
> Then there is a number $c$ in $(a, b)$ such that
>
> $$
> f'(c) = \frac{f(b) - f(a)}{b - a} \qquad (1)
> $$
>
> or, equivalently,
>
> $$
> f(b) - f(a) = f'(c)(b - a) . \qquad (2)
> $$
>
> *Stewart: 4.2, The Mean Value Theorem (Equations 1 and 2)*

^thm-26-2

> [!remark] Remark: Why It Works
> Let $A(a, f(a))$ and $B(b, f(b))$ be the endpoints of the graph. The slope of the secant line $AB$ is
>
> $$
> m_{AB} = \frac{f(b) - f(a)}{b - a} , \qquad (3)
> $$
>
> the right side of (1), and $f'(c)$ is the slope of the tangent line at $(c, f(c))$. So the theorem says: at some point $P(c, f(c))$ of the graph the tangent line is parallel to the secant line $AB$. (Imagine a line far away, parallel to $AB$, moving toward $AB$ until it first touches the graph; there may be several such points.) In terms of rates: if $s = f(t)$ is a position, then $\frac{f(b) - f(a)}{b - a}$ is the average velocity over $[a, b]$ and $f'(c)$ the velocity at time $c$. A car that travels $180$ km in $2$ hours has a speedometer reading of exactly $90$ km/h at least once.

^rem-26-1

> [!proof]+ Proof
> Apply Rolle's Theorem to the difference $h$ between $f$ and the function whose graph is the secant line $AB$. By (3) and the point-slope form, the line $AB$ is
>
> $$
> y = f(a) + \frac{f(b) - f(a)}{b - a}(x - a) ,
> $$
>
> so let
>
> $$
> h(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a) . \qquad (4)
> $$
>
> We check the three hypotheses of Rolle's Theorem for $h$.
> 1. $h$ is continuous on $[a, b]$: it is the sum of $f$ and a polynomial of degree $1$, both continuous there.
> 2. $h$ is differentiable on $(a, b)$, for the same reason. Since $f(a)$ and $\frac{f(b) - f(a)}{b - a}$ are constants,
>
> $$
> h'(x) = f'(x) - \frac{f(b) - f(a)}{b - a} .
> $$
>
> 3. $h(a) = f(a) - f(a) - \frac{f(b) - f(a)}{b - a}(a - a) = 0$ and
>
> $$
> h(b) = f(b) - f(a) - \frac{f(b) - f(a)}{b - a}(b - a) = f(b) - f(a) - [f(b) - f(a)] = 0 ,
> $$
>
> so $h(a) = h(b)$.
>
> By Rolle's Theorem there is a number $c$ in $(a, b)$ with $h'(c) = 0$, that is,
>
> $$
> 0 = h'(c) = f'(c) - \frac{f(b) - f(a)}{b - a}, \qquad\text{so}\qquad f'(c) = \frac{f(b) - f(a)}{b - a} .
> $$

^pf-26-2

*Uses:* [[§26 The Mean Value Theorem#^thm-26-1|§26.1]], [[§10 Continuity#^thm-10-1|§10.1]] (sums of continuous functions), [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4|§14.4]] (Sum Rule), [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-1|§14.1]] (constants)

![[m233-26-1.svg]]
*The Mean Value Theorem and its proof. The tangent at $P(c, f(c))$ (red) is parallel to the secant $AB$ (blue). The auxiliary function $h(x)$ of (4) is the vertical distance from the secant up to the graph (green). It vanishes at $a$ and $b$, and where it is largest its derivative is $0$: that is the point $c$.*

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (same proof: subtract the chord), with Rolle's Theorem as [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]]. Hub: [[Mean Value Theorem]].
> - The two-function version used to prove l'Hospital's Rule: Cauchy's Mean Value Theorem, [[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-1|Theorem §28.1]].

> [!example] Example §26.2: Finding the Number c
> Illustrate the Mean Value Theorem with $f(x) = x^3 - x$, $a = 0$, $b = 2$.
>
> $f$ is a polynomial, so it is continuous on $[0, 2]$ and differentiable on $(0, 2)$, and there is a $c \in (0, 2)$ with $f(2) - f(0) = f'(c)(2 - 0)$. Here $f(2) = 6$, $f(0) = 0$ and $f'(x) = 3x^2 - 1$, so the equation becomes
>
> $$
> 6 = (3c^2 - 1) \cdot 2 = 6c^2 - 2 ,
> $$
>
> which gives $c^2 = \frac43$, that is, $c = \pm 2/\sqrt3$. Only $c = 2/\sqrt3 \approx 1.15$ lies in $(0, 2)$. At this $c$ the tangent line is parallel to the secant line through $O(0, 0)$ and $B(2, 6)$, which has slope $3$; indeed $f'(2/\sqrt3) = 3 \cdot \frac43 - 1 = 3$.
>
> *Stewart: Example 4.2.3*

^ex-26-2

> [!example] Example §26.3: Bounding a Function by Its Derivative
> Suppose that $f(0) = -3$ and $f'(x) \le 5$ for all values of $x$. How large can $f(2)$ possibly be?
>
> $f$ is differentiable everywhere, hence continuous everywhere ([[§13 The Derivative as a Function#^thm-13-1|Theorem §13.1]]), so the Mean Value Theorem applies on $[0, 2]$: there is a number $c$ with
>
> $$
> f(2) - f(0) = f'(c)(2 - 0), \qquad\text{so}\qquad f(2) = f(0) + 2f'(c) = -3 + 2f'(c) .
> $$
>
> Since $f'(c) \le 5$, we get $2f'(c) \le 10$ and $f(2) \le -3 + 10 = 7$. The largest possible value is $7$; it is attained by $f(x) = 5x - 3$.
>
> *Stewart: Example 4.2.5*

^ex-26-3

The Mean Value Theorem gives information about $f$ from information about $f'$. The most basic instance:

> [!theorem] Theorem §26.3: Zero Derivative Means Constant
> If $f'(x) = 0$ for all $x$ in an interval $(a, b)$, then $f$ is constant on $(a, b)$.
>
> *Stewart: 4.2, Theorem 5*

^thm-26-3

> [!proof]+ Proof
> Let $x_1$ and $x_2$ be any two numbers in $(a, b)$ with $x_1 < x_2$. Since $f$ is differentiable on $(a, b)$, it is differentiable on $(x_1, x_2)$ and continuous on $[x_1, x_2]$. By the Mean Value Theorem on $[x_1, x_2]$ there is a number $c$ with $x_1 < c < x_2$ and
>
> $$
> f(x_2) - f(x_1) = f'(c)(x_2 - x_1) . \qquad (6)
> $$
>
> Since $f'(x) = 0$ for all $x$, $f'(c) = 0$, and (6) becomes $f(x_2) - f(x_1) = 0$, that is, $f(x_2) = f(x_1)$. So $f$ has the same value at any two numbers of $(a, b)$: it is constant there.

^pf-26-3

*Uses:* [[§26 The Mean Value Theorem#^thm-26-2|§26.2]], [[§13 The Derivative as a Function#^thm-13-1|§13.1]] (differentiable implies continuous)

> [!theorem] Corollary §26.4: Equal Derivatives Differ by a Constant
> If $f'(x) = g'(x)$ for all $x$ in an interval $(a, b)$, then $f - g$ is constant on $(a, b)$; that is, $f(x) = g(x) + c$ where $c$ is a constant.
>
> Geometrically: two functions with the same derivative on an interval have graphs that are vertical translates of each other there.
>
> *Stewart: 4.2, Corollary 7*

^cor-26-4

> [!proof]+ Proof
> Let $F(x) = f(x) - g(x)$. Then $F'(x) = f'(x) - g'(x) = 0$ for all $x$ in $(a, b)$. By Theorem §26.3, $F$ is constant; that is, $f - g$ is constant.

^pf-26-4

*Uses:* [[§26 The Mean Value Theorem#^thm-26-3|§26.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] and [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]].
> - With $f' = 0$ only almost everywhere the conclusion fails (the Cantor function); see the Connections of 451 Cor. §29.4.

> [!remark] Remark: The Interval Matters
> Theorem §26.3 needs an interval. Let
>
> $$
> f(x) = \frac{x}{|x|} = \begin{cases} 1 & \text{if } x > 0 \\ -1 & \text{if } x < 0 . \end{cases}
> $$
>
> Its domain is $D = \{x \mid x \ne 0\}$ and $f'(x) = 0$ for all $x$ in $D$, but $f$ is not constant. There is no contradiction: $D$ is not an interval. $f$ is constant on each of the intervals $(-\infty, 0)$ and $(0, \infty)$, with different constants. The same caution applies to antiderivatives ([[§33 Antiderivatives#^ex-33-1|Example §33.1]](b)).

^rem-26-2

> [!example] Example §26.4: Proving an Identity by Differentiating
> Prove the identity $\tan^{-1} x + \cot^{-1} x = \pi/2$.
>
> Let $f(x) = \tan^{-1} x + \cot^{-1} x$. By the derivatives of the inverse trigonometric functions ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|Theorem §19.8]]),
>
> $$
> f'(x) = \frac{1}{1 + x^2} - \frac{1}{1 + x^2} = 0
> $$
>
> for all $x$. By Theorem §26.3 on the interval $(-\infty, \infty)$, $f(x) = C$, a constant. To find $C$, put $x = 1$, where $f$ can be evaluated exactly:
>
> $$
> C = f(1) = \tan^{-1} 1 + \cot^{-1} 1 = \frac{\pi}{4} + \frac{\pi}{4} = \frac{\pi}{2} .
> $$
>
> Thus $\tan^{-1} x + \cot^{-1} x = \pi/2$. (Calculus is not needed for this identity, but the method works for many others.)
>
> *Stewart: Example 4.2.6*

^ex-26-4
