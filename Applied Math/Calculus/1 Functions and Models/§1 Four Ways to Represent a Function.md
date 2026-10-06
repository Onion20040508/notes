---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 1
stewart: "1.1"
aliases: ["Stewart 1.1"]
tags: [calculus]
---
↑ [[· 1 Functions and Models]] · [[§2 Mathematical Models꞉ A Catalog of Essential Functions]] →

*Stewart, Section 1.1.*

Calculus is about functions: how one quantity depends on another, and how fast it changes. This section fixes the vocabulary (domain, range, graph) and the four ways a function is usually given: in words, by a table, by a graph or by a formula. It answers the question of which curves are graphs of functions (the Vertical Line Test), introduces functions defined piece by piece, such as the absolute value, and names two kinds of behavior that recur throughout the course: symmetry (even and odd functions) and monotonicity (increasing and decreasing functions).

## Functions

Functions arise whenever one quantity depends on another. The area $A$ of a circle depends on its radius $r$ by the rule $A = \pi r^2$. The world population $P$ depends on the time $t$. The cost $C$ of mailing an envelope depends on its weight $w$, by a rule the post office publishes as a table. The vertical acceleration $a$ of the ground during an earthquake depends on the elapsed time $t$, and a seismograph records it as a graph. In each case a rule assigns to a number ($r$, $t$, $w$) another number ($A$, $P$, $C$, $a$).

> [!definition] Definition §1.1: Function
> A **function** $f$ is a rule that assigns to each element $x$ in a set $D$ exactly one element, called $f(x)$, in a set $E$.
>
> Here $D$ and $E$ are usually sets of real numbers.
> - $D$ is the **domain** of $f$.
> - $f(x)$ is the **value of $f$ at $x$**, read "$f$ of $x$".
> - The **range** of $f$ is the set of all possible values $f(x)$ as $x$ varies throughout the domain: $\{f(x) \mid x \in D\}$.
> - A symbol standing for an arbitrary number in the domain is an **independent variable**; a symbol standing for a number in the range is a **dependent variable**. In $A = \pi r^2$, written in **function notation** as $A = f(r)$, $r$ is the independent and $A$ the dependent variable.
>
> *Stewart: 1.1 (boxed; domain, range and variables in the text)*

^def-1-1

> [!remark] Remark: Machines and Arrows
> Two pictures help. A function is a **machine**: it accepts an **input** $x$ from the domain and produces an **output** $f(x)$ by its rule, so the domain is the set of all possible inputs and the range the set of all possible outputs. (The squaring key of a calculator is such a machine.) Or a function is an **arrow diagram**: each element $x$ of $D$ sends one arrow to the element $f(x)$ of $E$. Exactly one arrow leaves each element of $D$; an element of $E$ may receive one arrow, several, or none. The elements receiving at least one arrow form the range.

^rem-1-1

> [!remark]- Connections
> - Rigorous treatment: [[§8 Functions#^def-8-1|250 Def. §8.1]]. There the set $E$ is part of the function and is called its codomain; Stewart's range is the image [[§8 Functions#^def-8-9|250 Def. §8.9]], a subset of the codomain. Stewart's graph ([[§1 Four Ways to Represent a Function#^def-1-2|Definition §1.2]]) is [[§8 Functions#^def-8-10|250 Def. §8.10]].

> [!definition] Definition §1.2: Graph of a Function
> If $f$ is a function with domain $D$, its **graph** is the set of ordered pairs
>
> $$
> \{(x, f(x)) \mid x \in D\} .
> $$
>
> These are input-output pairs. Equivalently, the graph is the set of all points $(x, y)$ in the coordinate plane with $y = f(x)$ and $x$ in the domain of $f$. So $f(x)$ is the height of the graph above the point $x$ (below it if $f(x) < 0$), the domain is the projection of the graph onto the $x$-axis, and the range is its projection onto the $y$-axis.
>
> *Stewart: 1.1 (text)*

^def-1-2

In calculus a function is most often defined by an algebraic formula: $y = 2x - 1$ defines $y$ as a function of $x$, written $f(x) = 2x - 1$. Evaluating such an $f$ at an expression means replacing $x$ by that expression everywhere in the formula.

> [!definition] Definition §1.3: Difference Quotient
> For a function $f$ and $h \ne 0$, the expression
>
> $$
> \frac{f(a + h) - f(a)}{h}
> $$
>
> is a **difference quotient**. It is the average rate of change of $f(x)$ between $x = a$ and $x = a + h$ (Chapter 2).
>
> *Stewart: 1.1 (margin note to Example 3)*

^def-1-3

> [!example] Example §1.1: A Difference Quotient
> If $f(x) = 2x^2 - 5x + 1$ and $h \ne 0$, evaluate $\dfrac{f(a + h) - f(a)}{h}$.
>
> Replace $x$ by $a + h$ in the formula for $f$:
>
> $$
> f(a + h) = 2(a + h)^2 - 5(a + h) + 1 = 2(a^2 + 2ah + h^2) - 5a - 5h + 1 = 2a^2 + 4ah + 2h^2 - 5a - 5h + 1 .
> $$
>
> Subtract $f(a) = 2a^2 - 5a + 1$: the terms $2a^2$, $-5a$ and $1$ cancel, so
>
> $$
> \frac{f(a + h) - f(a)}{h} = \frac{4ah + 2h^2 - 5h}{h} = 4a + 2h - 5 .
> $$
>
> Dividing by $h$ is allowed because $h \ne 0$. The result still makes sense at $h = 0$, where it equals $4a - 5$; in Chapter 2 this is the slope of the tangent line at $a$.
>
> *Stewart: Example 1.1.3*

^ex-1-1

## Representations of Functions

> [!remark] Remark: Four Ways to Represent a Function
> A function can be represented
> - **verbally** (by a description in words),
> - **numerically** (by a table of values),
> - **visually** (by a graph),
> - **algebraically** (by an explicit formula).
>
> Some functions can be given in all four ways, and passing from one representation to another adds insight. But each of the four situations above has a most natural one:
> - The area of a circle: the formula $A(r) = \pi r^2$. A circle has positive radius, so the domain is $\{r \mid r > 0\} = (0, \infty)$, and the range is also $(0, \infty)$.
> - The world population $P(t)$ ($t$ in years since 1900): a table of census values, or its plot (a *scatter plot*). No formula gives $P(t)$ exactly, but a formula can approximate it, for instance $P(t) \approx (1.43653 \times 10^9) \cdot (1.01395)^t$. Such an approximating formula is a *mathematical model* ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-1|Def. §2.1]]). The methods of calculus also apply to a function known only through a table (a *tabular function*).
> - The postage $C(w)$: a table (1.00 dollar up to 1 oz, plus 15 cents for each additional ounce or less, as of 2019), equivalently the step function of [[§1 Four Ways to Represent a Function#^def-1-5|Definition §1.5]].
> - The ground acceleration $a(t)$: the seismograph's graph, on which a geologist reads off amplitudes and patterns.

^rem-1-2

> [!example] Example §1.2: From a Verbal Description to a Formula
> A rectangular storage container with an open top has a volume of $10\ \text{m}^3$. The length of its base is twice its width. Material for the base costs \$10 per square meter, and material for the sides costs \$6 per square meter. Express the cost of materials as a function of the width of the base.
>
> **Name the quantities.** Let $w$ be the width of the base, $2w$ its length, and $h$ the height (in meters).
>
> **Write the cost.** The base has area $(2w)w = 2w^2$ and costs $10(2w^2)$ dollars. Two sides have area $wh$ and two have area $2wh$, so the sides cost $6[2(wh) + 2(2wh)]$ dollars. In total
>
> $$
> C = 10(2w^2) + 6[2(wh) + 2(2wh)] = 20w^2 + 36wh .
> $$
>
> **Eliminate the extra variable.** $C$ should depend on $w$ alone, and the volume condition links $h$ to $w$: $w(2w)h = 10$, so $h = \dfrac{10}{2w^2} = \dfrac{5}{w^2}$. Substituting,
>
> $$
> C(w) = 20w^2 + 36w \cdot \frac{5}{w^2} = 20w^2 + \frac{180}{w}, \qquad w > 0 .
> $$
>
> The domain $w > 0$ comes from the physical situation, not from the formula. Setting up such functions is the first step in the optimization problems of Chapter 4 ([[§31 Optimization Problems|§31]]).
>
> *Stewart: Example 1.1.5*

^ex-1-2

> [!definition] Definition §1.4: Domain Convention
> If a function is given by a formula and the domain is not stated explicitly, the **domain** is the set of all inputs for which the formula makes sense and gives a real-number output.
>
> *Stewart: 1.1 (text)*

^def-1-4

> [!example] Example §1.3: Domains and Ranges
> Find the domain (and, for (a) and (b), the range) of
>
> $$
> \text{(a)}\ f(x) = 2x - 1 \qquad \text{(b)}\ g(x) = x^2 \qquad \text{(c)}\ f(x) = \sqrt{x + 2} \qquad \text{(d)}\ g(x) = \frac{1}{x^2 - x} .
> $$
>
> **(a)** $2x - 1$ is defined for every real number, so the domain is $\mathbb{R}$. The graph is the line $y = 2x - 1$ with slope $2$ and $y$-intercept $-1$. Every real $y$ is a value, namely $y = f\big(\frac{y + 1}{2}\big)$, so the range is $\mathbb{R}$.
>
> **(b)** The domain is $\mathbb{R}$. Since $x^2 \ge 0$ for all $x$, every value is $\ge 0$; and every $y \ge 0$ is a value, $y = (\sqrt{y})^2$. So the range is $\{y \mid y \ge 0\} = [0, \infty)$. The graph is the parabola $y = x^2$, through $(-1, 1)$, $(0, 0)$ and $(2, 4)$.
>
> **(c)** The square root of a negative number is not a real number, so we need $x + 2 \ge 0$, that is, $x \ge -2$. The domain is $[-2, \infty)$.
>
> **(d)** Factor: $g(x) = \dfrac{1}{x(x - 1)}$. Division by $0$ is not allowed, so $g(x)$ is undefined exactly when $x = 0$ or $x = 1$. The domain is
>
> $$
> \{x \mid x \ne 0,\ x \ne 1\} = (-\infty, 0) \cup (0, 1) \cup (1, \infty) .
> $$
>
> *Stewart: Examples 1.1.2 and 1.1.6*

^ex-1-3

## Which Rules Define Functions?

Not every equation, table or curve defines a function: it must give *exactly one* output for each input.

> [!theorem] Theorem §1.1: The Vertical Line Test
> A curve in the $xy$-plane is the graph of a function of $x$ if and only if no vertical line intersects the curve more than once.
>
> *Stewart: 1.1, The Vertical Line Test*

^thm-1-1

> [!proof]+ Proof
> ($\Rightarrow$) Let the curve be the graph of a function $f$ with domain $D$. A point $(a, y)$ on the vertical line $x = a$ lies on the graph only if $a \in D$ and $y = f(a)$ ([[§1 Four Ways to Represent a Function#^def-1-2|Definition §1.2]]). So the line meets the curve in the single point $(a, f(a))$ if $a \in D$, and not at all if $a \notin D$.
>
> ($\Leftarrow$) Suppose no vertical line meets the curve $C$ more than once. Let $D$ be the set of numbers $a$ for which the line $x = a$ meets $C$. For $a \in D$ the line meets $C$ in exactly one point $(a, b)$; define $f(a) = b$. This assigns exactly one number to each $a \in D$, so $f$ is a function with domain $D$ ([[§1 Four Ways to Represent a Function#^def-1-1|Definition §1.1]]). Its graph is $C$: a point $(a, b)$ lies on $C$ exactly when $a \in D$ and $(a, b)$ is the point where $x = a$ meets $C$, that is, when $b = f(a)$.
>
> In short: if the line $x = a$ met the curve at two points $(a, b)$ and $(a, c)$ with $b \ne c$, the curve would assign two values to $a$, which a function cannot do.

^pf-1-1

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-1|Def. §1.1]], [[§1 Four Ways to Represent a Function#^def-1-2|Def. §1.2]]

![[m233-1-1.svg]]
*The Vertical Line Test. (a) Each vertical line $x = a$ meets the curve once, at $(a, b)$, and that point gives the value $f(a) = b$. (b) The parabola $x = y^2 - 2$ fails: for $a > -2$ the line $x = a$ meets it twice. Its upper half (blue) and lower half (green) separately pass the test; they are the graphs of $\sqrt{x + 2}$ and $-\sqrt{x + 2}$ (Remark below).*

> [!remark]- Connections
> - Rigorous treatment: [[§8 Functions#^prop-8-2|250 Prop. §8.2]]. A subset $G \subseteq X \times Y$ is the graph of a function $X \to Y$ exactly when each "column" $\{x_0\} \times Y$ meets it in exactly one point. Since there the domain $X$ is fixed in advance, every column must be hit; here the domain is whatever set of $x$'s the curve covers.

> [!remark] Remark: Equations and Tables That Are Not Functions
> - The equation $y = x^2$ defines $y$ as a function of $x$: it determines exactly one $y$ for each $x$. The equation $y^2 = x$ does not: the input $x = 4$ gives the two outputs $y = 2$ and $y = -2$.
> - The table with inputs $2, 4, 5, 5, 6$ and outputs $3, 6, 7, 8, 9$ does not define $y$ as a function of $x$: the input $5$ gives both $7$ and $8$. (The postage table, by contrast, assigns exactly one cost to each weight.)
> - The parabola $x = y^2 - 2$ is not the graph of a function of $x$, but it *contains* the graphs of two: $x = y^2 - 2$ means $y^2 = x + 2$, so $y = \pm\sqrt{x + 2}$. The upper half is the graph of $f(x) = \sqrt{x + 2}$ ([[§1 Four Ways to Represent a Function#^ex-1-3|Example §1.3]](c)) and the lower half the graph of $g(x) = -\sqrt{x + 2}$.
> - Reversing the roles of the variables, $x = h(y) = y^2 - 2$ *does* define $x$ as a function of $y$ (independent variable $y$, dependent variable $x$), and its graph is that parabola.

^rem-1-3

## Piecewise Defined Functions

> [!definition] Definition §1.5: Piecewise Defined Function
> A **piecewise defined function** is defined by different formulas in different parts of its domain. It is still *one* function: the rule is "first see which part of the domain the input lies in, then apply that part's formula".
>
> A piecewise defined function that is constant on each piece, so that its graph is a staircase, is a **step function**. For example, the postage function of the Remark above is
>
> $$
> C(w) = \begin{cases} 1.00 & \text{if } 0 < w \le 1 \\ 1.15 & \text{if } 1 < w \le 2 \\ 1.30 & \text{if } 2 < w \le 3 \\ 1.45 & \text{if } 3 < w \le 4 \\ \ \ \vdots \end{cases}
> $$
>
> *Stewart: 1.1 (text; Example 1.1.10)*

^def-1-5

> [!example] Example §1.4: Evaluating, Graphing and Finding Piecewise Functions
> **(a)** Let
>
> $$
> f(x) = \begin{cases} 1 - x & \text{if } x \le -1 \\ x^2 & \text{if } x > -1 . \end{cases}
> $$
>
> Evaluate $f(-2)$, $f(-1)$, $f(0)$ and sketch the graph.
>
> Look at the input first, then use the matching formula:
>
> $$
> -2 \le -1 \ \Rightarrow\ f(-2) = 1 - (-2) = 3, \qquad -1 \le -1 \ \Rightarrow\ f(-1) = 1 - (-1) = 2, \qquad 0 > -1 \ \Rightarrow\ f(0) = 0^2 = 0 .
> $$
>
> To the left of the vertical line $x = -1$ (including the line), the graph is part of the line $y = 1 - x$, with slope $-1$ and $y$-intercept $1$; it ends at the solid dot $(-1, 2)$. To the right it is part of the parabola $y = x^2$, which starts at the open dot $(-1, 1)$: that point is not on the graph, since $f(-1) = 2$.
>
> **(b)** Find a formula for the function $f$ whose graph consists of the segment from $(0, 0)$ to $(1, 1)$, the segment from $(1, 1)$ to $(2, 0)$, and the part of the $x$-axis with $x > 2$.
>
> The line through $(0, 0)$ and $(1, 1)$ has slope $1$ and $y$-intercept $0$, so it is $y = x$. The line through $(1, 1)$ and $(2, 0)$ has slope $m = \frac{0 - 1}{2 - 1} = -1$, and its point-slope form is $y - 0 = (-1)(x - 2)$, that is, $y = 2 - x$. Assigning the shared endpoint $x = 1$ to the first piece (both formulas give $1$ there),
>
> $$
> f(x) = \begin{cases} x & \text{if } 0 \le x \le 1 \\ 2 - x & \text{if } 1 < x \le 2 \\ 0 & \text{if } x > 2 . \end{cases}
> $$
>
> *Stewart: Examples 1.1.7 and 1.1.9*

^ex-1-4

> [!definition] Definition §1.6: Absolute Value
> The **absolute value** of a number $a$, denoted $|a|$, is the distance from $a$ to $0$ on the real number line. Distances are positive or $0$, so $|a| \ge 0$ for every number $a$, and
>
> $$
> |a| = a \quad \text{if } a \ge 0, \qquad\qquad |a| = -a \quad \text{if } a < 0 .
> $$
>
> (If $a$ is negative, then $-a$ is positive.) For example, $|3| = |-3| = 3$, $|0| = 0$, $|\sqrt2 - 1| = \sqrt2 - 1$ and $|3 - \pi| = \pi - 3$.
>
> The **absolute value function** $f(x) = |x|$ is therefore piecewise defined: its graph is the line $y = x$ to the right of the $y$-axis and the line $y = -x$ to the left, a "V" with its corner at the origin.
>
> *Stewart: 1.1 (boxed; Example 1.1.8)*

^def-1-6

## Even and Odd Functions

> [!definition] Definition §1.7: Even and Odd Functions
> A function $f$ is **even** if $f(-x) = f(x)$ for every number $x$ in its domain, and **odd** if $f(-x) = -f(x)$ for every number $x$ in its domain. (Implicitly, $-x$ is in the domain whenever $x$ is.)
>
> For instance, $x^2$ is even, since $(-x)^2 = x^2$, and $x^3$ is odd, since $(-x)^3 = -x^3$.
>
> *Stewart: 1.1 (text)*

^def-1-7

> [!theorem] Proposition §1.2: Symmetry of Even and Odd Functions
> - $f$ is even if and only if its graph is symmetric with respect to the $y$-axis.
> - $f$ is odd if and only if its graph is symmetric about the origin, that is, unchanged by a rotation through $180^\circ$ about the origin.
>
> So for an even or odd function it suffices to graph $f$ for $x \ge 0$: reflect that part about the $y$-axis (even) or rotate it through $180^\circ$ about the origin (odd) to get the rest.
>
> *Stewart: 1.1 (text)*

^prop-1-2

> [!proof]+ Proof
> Reflection about the $y$-axis sends a point $(a, b)$ to $(-a, b)$, and rotation through $180^\circ$ about the origin sends it to $(-a, -b)$. A set is symmetric under one of these motions when the motion maps it to itself.
>
> **Even.** If $f$ is even and $(a, b)$ is on the graph, then $b = f(a) = f(-a)$, so $(-a, b)$ is on the graph. Conversely, if the graph is symmetric about the $y$-axis, then for each $x$ in the domain the point $(x, f(x))$ is on the graph, hence so is $(-x, f(x))$; that is, $-x$ is in the domain and $f(-x) = f(x)$.
>
> **Odd.** If $f$ is odd and $(a, b)$ is on the graph, then $f(-a) = -f(a) = -b$, so $(-a, -b)$ is on the graph. Conversely, if the graph is symmetric about the origin, then with $(x, f(x))$ also $(-x, -f(x))$ is on the graph, so $f(-x) = -f(x)$.

^pf-1-2

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-7|Def. §1.7]], [[§1 Four Ways to Represent a Function#^def-1-2|Def. §1.2]]

> [!example] Example §1.5: Even, Odd, or Neither
> Determine whether each function is even, odd, or neither: (a) $f(x) = x^5 + x$, (b) $g(x) = 1 - x^4$, (c) $h(x) = 2x - x^2$.
>
> **(a)** $f(-x) = (-x)^5 + (-x) = (-1)^5 x^5 - x = -x^5 - x = -(x^5 + x) = -f(x)$. So $f$ is odd.
>
> **(b)** $g(-x) = 1 - (-x)^4 = 1 - x^4 = g(x)$. So $g$ is even.
>
> **(c)** $h(-x) = 2(-x) - (-x)^2 = -2x - x^2$, which is neither $h(x) = 2x - x^2$ nor $-h(x) = -2x + x^2$ as a function. To be sure, exhibit one input where each identity fails: $h(1) = 1$ and $h(-1) = -3$, so $h(-1) \ne h(1)$ and $h(-1) \ne -h(1)$. So $h$ is neither even nor odd.
>
> A sum of odd powers is odd and a sum of even powers (a constant counts as $x^0$) is even; mixing odd and even powers, as in $h$, usually destroys both symmetries.
>
> *Stewart: Example 1.1.11*

^ex-1-5

![[m233-1-2.svg]]
*The three functions of [[§1 Four Ways to Represent a Function#^ex-1-5|Example §1.5]]. (a) The odd $f$: the point $(x, f(x))$ and its rotation $(-x, -f(x))$ are both on the graph, on a line through the origin. (b) The even $g$: $(x, g(x))$ and its mirror image $(-x, g(x))$ are both on the graph. (c) $h$ has neither symmetry: $(1, 1)$ is on the graph, but at $x = -1$ the graph passes through $(-1, -3)$, not through the mirror point $(-1, 1)$ or the rotated point $(-1, -1)$ (gray).*

## Increasing and Decreasing Functions

> [!definition] Definition §1.8: Increasing and Decreasing Functions
> A function $f$ is **increasing** on an interval $I$ if
>
> $$
> f(x_1) < f(x_2) \quad \text{whenever } x_1 < x_2 \text{ in } I .
> $$
>
> It is **decreasing** on $I$ if
>
> $$
> f(x_1) > f(x_2) \quad \text{whenever } x_1 < x_2 \text{ in } I .
> $$
>
> The inequality must hold for *every* pair of numbers $x_1 < x_2$ in $I$. On a graph: as $x$ moves to the right through $I$, an increasing graph rises and a decreasing graph falls.
>
> *Stewart: 1.1 (boxed)*

^def-1-8

> [!remark]- Connections
> - Rigorous treatment: [[§18 Properties of Continuous Functions#^def-18-2|451 Def. §18.2]] (strictly increasing and strictly decreasing, on $[a, b]$). Stewart's "increasing" is the strict notion; it is what makes a function one-to-one ([[§5 Inverse Functions and Logarithms#^def-5-1|Definition §5.1]]).

> [!remark] Remark: Checking the Definition for x²
> The graph of $f(x) = x^2$ suggests that $f$ is decreasing on $(-\infty, 0]$ and increasing on $[0, \infty)$. To verify this, factor the difference of two values:
>
> $$
> f(x_2) - f(x_1) = x_2^2 - x_1^2 = (x_2 - x_1)(x_2 + x_1) .
> $$
>
> Let $x_1 < x_2$, so $x_2 - x_1 > 0$. If $0 \le x_1 < x_2$, then $x_2 + x_1 > 0$, so $f(x_2) - f(x_1) > 0$: $f$ is increasing on $[0, \infty)$. If $x_1 < x_2 \le 0$, then $x_2 + x_1 < 0$, so $f(x_2) - f(x_1) < 0$: $f$ is decreasing on $(-\infty, 0]$. In Chapter 4 the sign of the derivative gives such conclusions directly ([[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]], the Increasing/Decreasing Test).

^rem-1-4
