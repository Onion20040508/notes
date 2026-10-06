---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 91
stewart: "14.2"
aliases: ["Stewart 14.2"]
tags: [calculus, math233]
---
← [[§90 Functions of Several Variables]] · ↑ [[· 14 Partial Derivatives]] · [[§92 Partial Derivatives]] →

*Stewart, Section 14.2 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q23), Exam 1 Review (Q20–Q22).*

The limit of $f(x, y)$ as $(x, y) \to (a, b)$ is defined exactly as in one variable, with the distance $\sqrt{(x - a)^2 + (y - b)^2}$ in place of $|x - a|$. What changes is the number of ways to approach the point. On the line there are two sides; in the plane there are infinitely many directions and curves, and the limit must be the same along all of them. That makes non-existence easy to prove (find two paths with different limits) and existence harder: agreement along every line is not enough, and one needs an estimate, usually with the Squeeze Theorem. Continuity is then defined by direct substitution, and the familiar functions are continuous on their domains, as in one variable.

## Limits of Functions of Two Variables

Compare
$$
f(x, y) = \frac{\sin(x^2 + y^2)}{x^2 + y^2} \qquad\text{and}\qquad g(x, y) = \frac{x^2 - y^2}{x^2 + y^2}
$$
near the origin, where neither is defined. A table of values suggests that $f(x, y)$ approaches $1$ while $g(x, y)$ approaches no particular number. Both guesses are correct: for $f$, put $t = x^2 + y^2$, which tends to $0^+$, and use $\frac{\sin t}{t} \to 1$; for $g$, see Example §91.1(a).

> [!definition] Definition §91.1: Limit of a Function of Two Variables
> Let $f$ be a function of two variables whose domain $D$ includes points arbitrarily close to $(a, b)$. Then we say that the **limit of $f(x, y)$ as $(x, y)$ approaches $(a, b)$** is $L$, and we write
>
> $$
> \lim_{(x, y) \to (a, b)} f(x, y) = L ,
> $$
>
> if for every number $\varepsilon > 0$ there is a corresponding number $\delta > 0$ such that
>
> $$
> \text{if}\quad (x, y) \in D \quad\text{and}\quad 0 < \sqrt{(x - a)^2 + (y - b)^2} < \delta \quad\text{then}\quad |f(x, y) - L| < \varepsilon .
> $$
>
> Other notations: $\displaystyle\lim_{\substack{x \to a \\ y \to b}} f(x, y) = L$ and $f(x, y) \to L$ as $(x, y) \to (a, b)$.
>
> *Stewart: 14.2, Definition 1*

^def-91-1

> [!remark] Remark: What the Definition Says
> $|f(x, y) - L|$ is the distance between the numbers $f(x, y)$ and $L$, and $\sqrt{(x - a)^2 + (y - b)^2}$ is the distance between the points $(x, y)$ and $(a, b)$. So the definition says that $f(x, y)$ can be made as close to $L$ as we like by taking $(x, y)$ close enough to $(a, b)$, but not equal to it (compare the one-variable definition, [[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]). In pictures: for any interval $(L - \varepsilon, L + \varepsilon)$ there is a disk $D_\delta$ with center $(a, b)$ and radius $\delta$ that $f$ maps, except possibly for the center, into that interval; equivalently, the part of the graph of $f$ over $D_\delta$ lies between the horizontal planes $z = L - \varepsilon$ and $z = L + \varepsilon$. The definition refers only to the *distance* between $(x, y)$ and $(a, b)$, never to the direction of approach.

^rem-91-1

> [!remark]- Connections
> - Rigorous treatment: [[§3 Continuity and Limits of Functions#^def-3-2|452 Def. §3.2]] is this definition (for $f$ defined near the point); the version for an arbitrary domain, as here, is [[§20 Limits of Functions#^def-20-1|451 Def. §20.1]] (limit along a set).

## Showing That a Limit Does Not Exist

In one variable, $x$ can approach $a$ only from the left or from the right, and if the two one-sided limits differ, the limit does not exist. In two variables $(x, y)$ can approach $(a, b)$ from infinitely many directions and along any curve, as long as it stays in the domain of $f$. Since the definition does not mention the direction of approach, the limit, if it exists, must be the same along all of them.

> [!theorem] Theorem §91.1: The Two-Path Test
> If $f(x, y) \to L_1$ as $(x, y) \to (a, b)$ along a path $C_1$ and $f(x, y) \to L_2$ as $(x, y) \to (a, b)$ along a path $C_2$, where $L_1 \ne L_2$, then $\displaystyle\lim_{(x, y) \to (a, b)} f(x, y)$ does not exist.
>
> *Stewart: 14.2 (boxed statement)*

^thm-91-1

> [!proof]+ Proof
> Stewart argues in words; here is the argument in full. "$f(x, y) \to L_1$ along $C_1$" means that $f$, restricted to the points of $C_1$ in its domain, has limit $L_1$ at $(a, b)$ in the sense of Definition §91.1 (with $D$ replaced by $D \cap C_1$, which contains points arbitrarily close to $(a, b)$).
>
> Suppose, for contradiction, that $\lim_{(x, y) \to (a, b)} f(x, y) = L$. Let $\varepsilon > 0$ and take the $\delta$ of Definition §91.1. Every point $(x, y)$ of $D \cap C_1$ with $0 < \sqrt{(x - a)^2 + (y - b)^2} < \delta$ is in particular a point of $D$, so $|f(x, y) - L| < \varepsilon$. Thus the same $\delta$ shows that the limit of $f$ along $C_1$ is $L$. A limit is unique (if $f$ were within $\varepsilon$ of two numbers $L$ and $L'$ at points arbitrarily close to $(a, b)$, then $|L - L'| < 2\varepsilon$ for every $\varepsilon > 0$, so $L = L'$), hence $L_1 = L$. In the same way $L_2 = L$. So $L_1 = L_2$, contradicting $L_1 \ne L_2$.

^pf-91-1

*Uses:* [[§91 Limits and Continuity#^def-91-1|Def. §91.1]]

> [!remark]- Connections
> - The standard example of path dependence in 452 is $\frac{2xy}{x^2 + y^2}$, twice the function of Example §91.1(b): [[§3 Continuity and Limits of Functions#^ex-3-1|452 Ex. §3.1]], [[§3 Continuity and Limits of Functions#^ex-3-2|452 Ex. §3.2]], and the workhorse page [[2xy∕(x²+y²) family]].
> - Complex-variables version: [[§15 Limits#^cor-15-2|342 Cor. §15.2]] (the two-path test for $\lim_{z\to z_0} f(z)$), with [[§15 Limits#^ex-15-2|342 Ex. §15.2]] ($z/\bar z$ has no limit at $0$).

> [!example] Example §91.1: Different Limits Along Two Lines
> **(a)** Show that $\displaystyle\lim_{(x, y) \to (0, 0)} \frac{x^2 - y^2}{x^2 + y^2}$ does not exist.
>
> Let $f(x, y) = (x^2 - y^2)/(x^2 + y^2)$. Along the $x$-axis, $y = 0$, so $f(x, 0) = x^2/x^2 = 1$ for all $x \ne 0$, and $f(x, y) \to 1$. Along the $y$-axis, $x = 0$, so $f(0, y) = -y^2/y^2 = -1$ for all $y \ne 0$, and $f(x, y) \to -1$. Two different limits along two lines: by Theorem §91.1 the limit does not exist. (This confirms the numerical guess at the start of the section.)
>
> **(b)** If $f(x, y) = \dfrac{xy}{x^2 + y^2}$, does $\displaystyle\lim_{(x, y) \to (0, 0)} f(x, y)$ exist?
>
> Along the $x$-axis $f(x, 0) = 0/x^2 = 0$, and along the $y$-axis $f(0, y) = 0/y^2 = 0$. Identical limits along the two axes do **not** show that the limit is $0$. Along the line $y = x$, for $x \ne 0$,
>
> $$
> f(x, x) = \frac{x^2}{x^2 + x^2} = \frac12 ,
> $$
>
> so $f(x, y) \to \frac12$ along $y = x$. Since $0 \ne \frac12$, the limit does not exist. More generally, along $y = mx$ the function is constant, $f(x, mx) = \dfrac{m}{1 + m^2}$: the graph has a ridge of height $\frac12$ above the line $y = x$.
>
> *Stewart: Examples 14.2.1 and 14.2.2*

^ex-91-1

> [!example] Example §91.2: The Same Limit Along Every Line, but No Limit
> If $f(x, y) = \dfrac{xy^2}{x^2 + y^4}$, does $\displaystyle\lim_{(x, y) \to (0, 0)} f(x, y)$ exist?
>
> **Lines.** Let $(x, y) \to (0, 0)$ along any non-vertical line through the origin, $y = mx$. Then
>
> $$
> f(x, mx) = \frac{x (mx)^2}{x^2 + (mx)^4} = \frac{m^2 x^3}{x^2 + m^4 x^4} = \frac{m^2 x}{1 + m^4 x^2} \to 0 \quad\text{as } x \to 0 .
> $$
>
> Along the line $x = 0$, $f(0, y) = 0$ for $y \ne 0$, so again $f \to 0$. So $f$ has the same limit $0$ along every line through the origin.
>
> **A parabola.** But along the parabola $x = y^2$,
>
> $$
> f(y^2, y) = \frac{y^2 \cdot y^2}{(y^2)^2 + y^4} = \frac{y^4}{2y^4} = \frac12 \quad (y \ne 0) ,
> $$
>
> so $f(x, y) \to \frac12$ along $x = y^2$. Different paths give different limits, so the limit does not exist.
>
> **A variant.** The same parabola settles $\displaystyle\lim_{(x, y) \to (0, 0)} \frac{xy^2 \cos y}{x^2 + y^4}$: along $x = y^2$ the function is $\frac12 \cos y \to \frac12$, while along the $x$-axis it is $0$. This limit does not exist either.
>
> *Stewart: Example 14.2.3*
> *Source: 233 Exam 1 Review, Q22*

^ex-91-2

![[m233-91-1.svg]]
*Why lines miss the value $\frac12$ in Example §91.2. On each parabola $x = \lambda y^2$ the function $f(x, y) = \frac{xy^2}{x^2 + y^4}$ is constant, equal to $\frac{\lambda}{1 + \lambda^2}$: $\frac12$ on $x = y^2$ (green), $-\frac12$ on $x = -y^2$ (red), $\pm\frac{3}{10}$ on $x = \pm 3y^2$ and $x = \pm\frac13 y^2$ (thin). All these parabolas are tangent to the $y$-axis at the origin, so a line $y = mx$ (dashed) meets $x = \lambda y^2$ only at $x = 1/(\lambda m^2)$, away from the origin. Close to the origin a line crosses only parabolas with large $|\lambda|$, where $f$ is close to $0$.*

## Properties of Limits

The Limit Laws of [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|Theorem §8.1]] extend to functions of two variables.

> [!theorem] Theorem §91.2: Limit Laws for Two Variables
> Suppose that $\lim_{(x, y) \to (a, b)} f(x, y)$ and $\lim_{(x, y) \to (a, b)} g(x, y)$ exist, and let $c$ be a constant. Then
> 1. **Sum Law:** the limit of a sum is the sum of the limits;
> 2. **Difference Law:** the limit of a difference is the difference of the limits;
> 3. **Constant Multiple Law:** the limit of a constant times a function is the constant times the limit of the function;
> 4. **Product Law:** the limit of a product is the product of the limits;
> 5. **Quotient Law:** the limit of a quotient is the quotient of the limits, provided that the limit of the denominator is not $0$.
>
> Moreover, there are the special limits
>
> $$
> \lim_{(x, y) \to (a, b)} x = a , \qquad \lim_{(x, y) \to (a, b)} y = b , \qquad \lim_{(x, y) \to (a, b)} c = c . \qquad (2)
> $$
>
> *Stewart: 14.2 (text) and Equation 2*

^thm-91-2

*Stewart states the laws verbally and leaves the special limits (2) as Exercise 54. The one-variable proofs ([[§8 Calculating Limits Using the Limit Laws#^pf-8-1|proof of Theorem §8.1]], from Appendix F) carry over word for word with $|x - a|$ replaced by the distance $\sqrt{(x - a)^2 + (y - b)^2}$; for (2), take $\delta = \varepsilon$, since $|x - a| \le \sqrt{(x - a)^2 + (y - b)^2}$. The 452 versions are stated for continuous functions: [[§3 Continuity and Limits of Functions#^thm-3-1|452 Thm. §3.1]]–[[§3 Continuity and Limits of Functions#^thm-3-3|§3.3]].*

> [!definition] Definition §91.2: Polynomial and Rational Functions of Two Variables
> A **polynomial function** of two variables (or **polynomial**) is a sum of terms of the form $cx^m y^n$, where $c$ is a constant and $m$ and $n$ are nonnegative integers. A **rational function** is a ratio of two polynomials. For instance,
>
> $$
> p(x, y) = x^4 + 5x^3 y^2 + 6xy^4 - 7y + 6 \qquad\text{and}\qquad q(x, y) = \frac{2xy + 1}{x^2 + y^2}
> $$
>
> are a polynomial and a rational function.
>
> *Stewart: 14.2 (text)*

^def-91-2

> [!theorem] Theorem §91.3: Direct Substitution for Polynomials and Rational Functions
> If $p$ is a polynomial, then
>
> $$
> \lim_{(x, y) \to (a, b)} p(x, y) = p(a, b) . \qquad (3)
> $$
>
> If $q = p/r$ is a rational function and $(a, b)$ is in the domain of $q$, then
>
> $$
> \lim_{(x, y) \to (a, b)} q(x, y) = \lim_{(x, y) \to (a, b)} \frac{p(x, y)}{r(x, y)} = \frac{p(a, b)}{r(a, b)} = q(a, b) . \qquad (4)
> $$
>
> *Stewart: 14.2, Equations 3 and 4*

^thm-91-3

> [!proof]+ Proof
> By the Product Law applied repeatedly and the special limits (2), $x^m \to a^m$ and $y^n \to b^n$, so $x^m y^n \to a^m b^n$ (for $m = 0$ or $n = 0$ the factor is the constant $1$). By the Constant Multiple Law, $cx^m y^n \to ca^m b^n$, and by the Sum Law a polynomial, being a finite sum of such terms, satisfies $p(x, y) \to p(a, b)$. This is (3).
>
> For (4), $(a, b)$ in the domain of $q$ means $r(a, b) \ne 0$. By (3), $p(x, y) \to p(a, b)$ and $r(x, y) \to r(a, b) \ne 0$, so the Quotient Law gives $q(x, y) \to p(a, b)/r(a, b) = q(a, b)$. (Stewart says only that the special limits and the Limit Laws "allow us" to do this.)

^pf-91-3

*Uses:* [[§91 Limits and Continuity#^thm-91-2|§91.2]], [[§91 Limits and Continuity#^def-91-2|Def. §91.2]]

For instance, $\lim_{(x, y) \to (1, 2)} (x^2y^3 - x^3y^2 + 3x + 2y) = 1 \cdot 8 - 1 \cdot 4 + 3 + 4 = 11$, and $\lim_{(x, y) \to (-2, 3)} \frac{x^2 y + 1}{x^3 y^2 - 2x} = \frac{(-2)^2(3) + 1}{(-2)^3(3)^2 - 2(-2)} = -\frac{13}{68}$, since the denominator is not $0$ at $(-2, 3)$ (Stewart, Examples 14.2.4 and 14.2.5).

> [!theorem] Theorem §91.4: The Squeeze Theorem for Two Variables
> If $g(x, y) \le f(x, y) \le h(x, y)$ for all $(x, y) \ne (a, b)$ near $(a, b)$ in the domain of $f$, and
>
> $$
> \lim_{(x, y) \to (a, b)} g(x, y) = \lim_{(x, y) \to (a, b)} h(x, y) = L ,
> $$
>
> then $\displaystyle\lim_{(x, y) \to (a, b)} f(x, y) = L$.
>
> *Stewart: 14.2 (text)*

^thm-91-4

*Stewart says only that the Squeeze Theorem "also holds" for functions of two or more variables. The one-variable proof ([[§8 Calculating Limits Using the Limit Laws#^pf-8-7|proof of Theorem §8.7]], from Appendix F) carries over with the distance in place of $|x - a|$: given $\varepsilon$, take the smaller of the two $\delta$'s for $g$ and $h$; then $L - \varepsilon < g \le f \le h < L + \varepsilon$.*

> [!example] Example §91.3: A Limit That Exists
> Find $\displaystyle\lim_{(x, y) \to (0, 0)} \frac{3x^2 y}{x^2 + y^2}$ if it exists.
>
> **Is $0$ a plausible value?** Along any line through the origin, and also along the parabolas $y = x^2$ and $x = y^2$, the limit is $0$. That does not prove anything, but it suggests that the limit exists and equals $0$.
>
> **Solution 1 (by Definition §91.1).** Let $\varepsilon > 0$. We want $\delta > 0$ such that
>
> $$
> 0 < \sqrt{x^2 + y^2} < \delta \quad\Longrightarrow\quad \left| \frac{3x^2 y}{x^2 + y^2} - 0 \right| = \frac{3x^2 |y|}{x^2 + y^2} < \varepsilon .
> $$
>
> Since $y^2 \ge 0$, we have $x^2 \le x^2 + y^2$, so $x^2/(x^2 + y^2) \le 1$, and therefore
>
> $$
> \frac{3x^2 |y|}{x^2 + y^2} \le 3|y| = 3\sqrt{y^2} \le 3\sqrt{x^2 + y^2} . \qquad (5)
> $$
>
> Choose $\delta = \varepsilon/3$. If $0 < \sqrt{x^2 + y^2} < \delta$, then by (5)
>
> $$
> \left| \frac{3x^2 y}{x^2 + y^2} - 0 \right| \le 3\sqrt{x^2 + y^2} < 3\delta = 3 \cdot \frac{\varepsilon}{3} = \varepsilon .
> $$
>
> Hence the limit is $0$.
>
> **Solution 2 (by the Squeeze Theorem).** As in Solution 1, $\left| \frac{3x^2 y}{x^2 + y^2} \right| \le 3|y|$, so
>
> $$
> -3|y| \le \frac{3x^2 y}{x^2 + y^2} \le 3|y| .
> $$
>
> Now $|y| \to 0$ as $(x, y) \to (0, 0)$ (by (2) and continuity of the absolute value), so $\pm 3|y| \to 0$ by the Constant Multiple Law. By Theorem §91.4 the limit is $0$.
>
> *Stewart: Example 14.2.6*
> *Source: 233 Exam 1 Review, Q21 (the same limit)*

^ex-91-3

## Continuity

> [!definition] Definition §91.3: Continuity
> A function $f$ of two variables is **continuous at $(a, b)$** if
>
> $$
> \lim_{(x, y) \to (a, b)} f(x, y) = f(a, b) .
> $$
>
> We say that $f$ is **continuous on $D$** if $f$ is continuous at every point $(a, b)$ in $D$.
>
> *Stewart: 14.2, Definition 6*

^def-91-3

The intuitive meaning: if the point $(x, y)$ changes by a small amount, then $f(x, y)$ changes by a small amount, so the graph of a continuous function is a surface with no hole or break. By Theorem §91.3, **every polynomial is continuous on $\mathbb{R}^2$** and **every rational function is continuous on its domain**.

> [!theorem] Theorem §91.5: Combining Continuous Functions
> (a) Sums, differences, products and quotients of continuous functions are continuous on their domains.
>
> (b) If $f$ is a continuous function of two variables and $g$ is a continuous function of a single variable that is defined on the range of $f$, then the composite function $h = g \circ f$, $h(x, y) = g(f(x, y))$, is continuous.
>
> *Stewart: 14.2 (text)*

^thm-91-5

> [!proof]+ Proof
> (a) If $f$ and $g$ are continuous at $(a, b)$, then $f(x, y) \to f(a, b)$ and $g(x, y) \to g(a, b)$, so by the Sum Law $f(x, y) + g(x, y) \to f(a, b) + g(a, b)$, which is continuity of $f + g$ at $(a, b)$; likewise for $f - g$, $fg$ (Difference and Product Laws) and $f/g$ at points where $g(a, b) \ne 0$ (Quotient Law).
>
> (b) Stewart says "it can be shown" and omits the proof. It is the $\varepsilon$–$\delta$ argument of [[§10 Continuity#^thm-10-7|Theorem §10.7]] with the distance in the plane: given $\varepsilon > 0$, continuity of $g$ at $f(a, b)$ gives $\delta_1$ with $|t - f(a, b)| < \delta_1 \Rightarrow |g(t) - g(f(a, b))| < \varepsilon$, and continuity of $f$ at $(a, b)$ gives $\delta$ with $\sqrt{(x - a)^2 + (y - b)^2} < \delta \Rightarrow |f(x, y) - f(a, b)| < \delta_1$. Put $t = f(x, y)$.

^pf-91-5

*Uses:* [[§91 Limits and Continuity#^thm-91-2|§91.2]], [[§91 Limits and Continuity#^def-91-3|Def. §91.3]], [[§10 Continuity#^thm-10-7|§10.7]]

> [!remark]- Connections
> - Rigorous treatment: [[§3 Continuity and Limits of Functions#^thm-3-1|452 Thm. §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|452 Thm. §3.2]], [[§3 Continuity and Limits of Functions#^thm-3-3|452 Thm. §3.3]] (sum, product, quotient), and [[§3 Continuity and Limits of Functions#^thm-3-4|452 Thm. §3.4]], which allows the outer function to have several variables too. The definition of continuity there is the $\varepsilon$–$\delta$ form [[§3 Continuity and Limits of Functions#^def-3-1|452 Def. §3.1]].

> [!example] Example §91.4: Where Is It Continuous?
> **(a)** $f(x, y) = \dfrac{x^2 - y^2}{x^2 + y^2}$ is a rational function, so it is continuous on its domain $D = \{(x, y) \mid (x, y) \ne (0, 0)\}$. It is discontinuous at $(0, 0)$, where it is not defined.
>
> **(b)** Let
>
> $$
> g(x, y) = \begin{cases} \dfrac{x^2 - y^2}{x^2 + y^2} & \text{if } (x, y) \ne (0, 0) \\[6pt] 0 & \text{if } (x, y) = (0, 0) . \end{cases}
> $$
>
> Now $g$ is defined at $(0, 0)$, but it is still discontinuous there, because $\lim_{(x, y) \to (0, 0)} g(x, y)$ does not exist (Example §91.1(a)). No value of $g(0, 0)$ can repair this.
>
> **(c)** Let
>
> $$
> f(x, y) = \begin{cases} \dfrac{3x^2 y}{x^2 + y^2} & \text{if } (x, y) \ne (0, 0) \\[6pt] 0 & \text{if } (x, y) = (0, 0) . \end{cases}
> $$
>
> For $(x, y) \ne (0, 0)$, $f$ equals a rational function near $(x, y)$, so it is continuous there. At the origin, by Example §91.3,
>
> $$
> \lim_{(x, y) \to (0, 0)} f(x, y) = \lim_{(x, y) \to (0, 0)} \frac{3x^2 y}{x^2 + y^2} = 0 = f(0, 0) .
> $$
>
> So $f$ is continuous at $(0, 0)$ as well, and hence on $\mathbb{R}^2$.
>
> **(d)** $h(x, y) = e^{-(x^2 + y^2)}$ is $g \circ f$ with $f(x, y) = x^2 + y^2$, a polynomial (continuous on $\mathbb{R}^2$), and $g(t) = e^{-t}$, continuous for all $t$. By Theorem §91.5(b), $h$ is continuous on $\mathbb{R}^2$.
>
> **(e)** $h(x, y) = \arctan(y/x)$ is $g \circ f$ with $f(x, y) = y/x$, a rational function continuous except on the line $x = 0$, and $g(t) = \arctan t$, continuous everywhere. So $h$ is continuous except where $x = 0$. Its graph breaks above the $y$-axis: as $x \to 0^{\pm}$ with $y > 0$ fixed, $y/x \to \pm\infty$ and $h \to \pm\frac{\pi}{2}$.
>
> *Stewart: Examples 14.2.7, 14.2.8, 14.2.9, 14.2.10 and 14.2.11*

^ex-91-4

## Functions of Three or More Variables

> [!definition] Definition §91.4: Limits in Three or More Variables
> For a function of three variables, $\lim_{(x, y, z) \to (a, b, c)} f(x, y, z) = L$ means: for every $\varepsilon > 0$ there is a $\delta > 0$ such that if $(x, y, z)$ is in the domain of $f$ and $0 < \sqrt{(x - a)^2 + (y - b)^2 + (z - c)^2} < \delta$, then $|f(x, y, z) - L| < \varepsilon$.
>
> In vector notation, for $f$ defined on a subset $D$ of $\mathbb{R}^n$: $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L$ means that for every $\varepsilon > 0$ there is a $\delta > 0$ such that
>
> $$
> \text{if}\quad \mathbf{x} \in D \quad\text{and}\quad 0 < |\mathbf{x} - \mathbf{a}| < \delta \quad\text{then}\quad |f(\mathbf{x}) - L| < \varepsilon , \qquad (7)
> $$
>
> For $n = 1$ this is the one-variable definition ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]), for $n = 2$ it is Definition §91.1, and for $n = 3$ the definition just given.
>
> *Stewart: 14.2, Definition 7 and text*

^def-91-4

> [!definition] Definition §91.5: Continuity in Three or More Variables
> The function $f$ is **continuous** at $(a, b, c)$ if $\lim_{(x, y, z) \to (a, b, c)} f(x, y, z) = f(a, b, c)$.
>
> In vector notation, $f$ is continuous at $\mathbf{a}$ if $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})$, with the limit of [[§91 Limits and Continuity#^def-91-4|Definition §91.4]].
>
> *Stewart: 14.2, Definition 7 and text*

^def-91-new1

For instance, $f(x, y, z) = \dfrac{1}{x^2 + y^2 + z^2 - 1}$ is a rational function of three variables, so it is continuous at every point of $\mathbb{R}^3$ except where $x^2 + y^2 + z^2 = 1$, the sphere with center the origin and radius $1$.

> [!remark] Remark: Method — Limits in Two Variables
> To find $\lim_{(x, y) \to (a, b)} f(x, y)$:
> 1. **Substitute** if $f$ is built from continuous functions ([[§91 Limits and Continuity#^thm-91-5|Theorem §91.5]]) and $(a, b)$ is in its domain: the limit is $f(a, b)$.
> 2. **Simplify** if substitution gives $\frac00$: factor and cancel, or multiply by a conjugate, then substitute.
> 3. **Test paths** to show that the limit does not exist: the two axes, the lines $y - b = m(x - a)$, and curves suggested by the powers in $f$ (for $\frac{xy^2}{x^2 + y^4}$ the parabola $x = y^2$, which makes $x^2$ and $y^4$ comparable). Two different values prove non-existence ([[§91 Limits and Continuity#^thm-91-1|Theorem §91.1]]).
> 4. **Prove existence** when all paths give the same $L$: bound $|f(x, y) - L|$ by an expression that tends to $0$, using $x^2 \le x^2 + y^2$, $|y| \le \sqrt{x^2 + y^2}$, or polar coordinates $x = r\cos\theta$, $y = r\sin\theta$ with $r \to 0^+$; then apply the Squeeze Theorem ([[§91 Limits and Continuity#^thm-91-4|Theorem §91.4]]).
>
> Agreement along every line through the point is *not* a proof that the limit exists (Example §91.2).

^rem-91-2

> [!example] Example §91.5: Three Limits from the Exams
> Find the limits, if they exist, or show that they do not exist.
>
> **(a)** $\displaystyle\lim_{(x, y) \to (0, 0)} \frac{3x^2 y^2}{2x^4 + y^4}$. Along the $x$-axis, $y = 0$ and the function is $0$, so it tends to $0$. Along the line $y = x$,
>
> $$
> \frac{3x^2 \cdot x^2}{2x^4 + x^4} = \frac{3x^4}{3x^4} = 1 \qquad (x \ne 0) ,
> $$
>
> so it tends to $1$. By Theorem §91.1 the limit does not exist. (Along $y = mx$ the function is the constant $\frac{3m^2}{2 + m^4}$.)
>
> **(b)** $\displaystyle\lim_{(x, y) \to (3, 1)} e^{x^2 + 3y}$. The exponent $x^2 + 3y$ is a polynomial and $e^t$ is continuous, so the function is continuous on $\mathbb{R}^2$ by Theorem §91.5(b). Substituting, the limit is $e^{9 + 3} = e^{12}$.
>
> **(c)** $\displaystyle\lim_{(x, y) \to (1, 2)} \frac{2x - y}{4x^2 - y^2}$. Substitution gives $\frac{2 - 2}{4 - 4} = \frac00$. The domain is $\{(x, y) \mid y \ne \pm 2x\}$, and at its points $2x - y \ne 0$, so we may factor and cancel:
>
> $$
> \frac{2x - y}{4x^2 - y^2} = \frac{2x - y}{(2x - y)(2x + y)} = \frac{1}{2x + y} .
> $$
>
> The rational function $\frac{1}{2x + y}$ is continuous at $(1, 2)$, where $2x + y = 4 \ne 0$. So the limit is $\frac14$.
>
> *Source: 233 Midterm 1 Practice Questions, Q23; 233 Exam 1 Review, Q20*

^ex-91-5
