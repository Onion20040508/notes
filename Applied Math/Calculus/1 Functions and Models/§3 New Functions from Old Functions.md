---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 3
stewart: "1.3"
aliases: ["Stewart 1.3"]
tags: [calculus]
---
← [[§2 Mathematical Models꞉ A Catalog of Essential Functions]] · ↑ [[· 1 Functions and Models]] · [[§4 Exponential Functions]] →

*Stewart, Section 1.3.*

Starting from the essential functions of [[§2 Mathematical Models꞉ A Catalog of Essential Functions|§2]], this section builds new ones in two ways. Transforming a graph (shifting, stretching, reflecting it, or taking an absolute value) changes the formula in a predictable way, so many graphs can be sketched by hand from one known graph, and a formula can be read off a given graph. Combining two functions (arithmetic operations and composition) produces new functions, whose domains must be worked out. Composition, and the reverse skill of decomposing a function into simpler ones, is what the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]) will act on.

## Transformations of Functions

Throughout, the graph of $f$ is the set of points $(a, b)$ with $b = f(a)$ ([[§1 Four Ways to Represent a Function#^def-1-2|Def. §1.2]]).

> [!theorem] Theorem §3.1: Vertical and Horizontal Shifts
> Suppose $c > 0$. To obtain the graph of
> - $y = f(x) + c$, shift the graph of $y = f(x)$ a distance $c$ units upward;
> - $y = f(x) - c$, shift the graph of $y = f(x)$ a distance $c$ units downward;
> - $y = f(x - c)$, shift the graph of $y = f(x)$ a distance $c$ units to the right;
> - $y = f(x + c)$, shift the graph of $y = f(x)$ a distance $c$ units to the left.
>
> *Stewart: 1.3, Vertical and Horizontal Shifts*

^thm-3-1

> [!proof]+ Proof
> **Vertical shifts.** The graph of $y = f(x) + c$ consists of the points $(a, f(a) + c)$ with $a$ in the domain of $f$. Each is the point $(a, f(a))$ of the graph of $f$ moved up by $c$: every $y$-coordinate is increased by the same number $c$. Replacing $c$ by $-c$ gives the downward shift.
>
> **Horizontal shifts.** Let $g(x) = f(x - c)$. The value of $g$ at $x$ is the value of $f$ at $x - c$, which is $c$ units to the left of $x$. So the point $(a + c, b)$ lies on the graph of $g$ exactly when $g(a + c) = f\big((a + c) - c\big) = f(a) = b$, that is, exactly when $(a, b)$ lies on the graph of $f$. The graph of $g$ is therefore the graph of $f$ moved $c$ units to the right (and the domain moves with it). Replacing $c$ by $-c$ gives the shift to the left.

^pf-3-1

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-2|Def. §1.2]]

> [!remark] Remark: Why the Sign Looks Backwards
> $f(x - c)$ moves the graph to the *right*. The graph of $f(x - c)$ reaches at $x$ the height that $f$ reaches at $x - c$, so everything happens $c$ units later. For instance, $\sqrt{x - 2}$ starts at $x = 2$, where $\sqrt{x}$ starts at $0$. The same reversal occurs for horizontal stretches below: $f(cx)$ with $c > 1$ *shrinks* the graph.

^rem-3-1

> [!theorem] Theorem §3.2: Vertical and Horizontal Stretching and Reflecting
> Suppose $c > 1$. To obtain the graph of
> - $y = cf(x)$, stretch the graph of $y = f(x)$ vertically by a factor of $c$;
> - $y = (1/c)f(x)$, shrink the graph of $y = f(x)$ vertically by a factor of $c$;
> - $y = f(cx)$, shrink the graph of $y = f(x)$ horizontally by a factor of $c$;
> - $y = f(x/c)$, stretch the graph of $y = f(x)$ horizontally by a factor of $c$;
> - $y = -f(x)$, reflect the graph of $y = f(x)$ about the $x$-axis;
> - $y = f(-x)$, reflect the graph of $y = f(x)$ about the $y$-axis.
>
> For example, $y = 2\cos x$ is $\cos x$ stretched vertically by $2$ (it oscillates between $-2$ and $2$), $y = \frac12 \cos x$ is shrunk vertically, $y = \cos 2x$ is shrunk horizontally (period $\pi$), and $y = \cos\frac12 x$ is stretched horizontally (period $4\pi$).
>
> *Stewart: 1.3, Vertical and Horizontal Stretching and Reflecting*

^thm-3-2

> [!proof]+ Proof
> In each case, compare points with those of the graph of $f$; let $(a, b)$ be on the graph of $f$, so $b = f(a)$.
> - $y = cf(x)$ contains $(a, cb)$: each $y$-coordinate is multiplied by $c$, a vertical stretch. With $1/c$ in place of $c$, each $y$-coordinate is divided by $c$, a vertical shrink.
> - $y = f(cx)$ contains $(a/c, b)$, since $f(c \cdot a/c) = f(a) = b$; and every point of its graph arises this way. Each $x$-coordinate is divided by $c$: a horizontal shrink. Likewise $y = f(x/c)$ contains $(ca, b)$, since $f(ca/c) = b$: a horizontal stretch.
> - $y = -f(x)$ contains $(a, -b)$: the point $(x, y)$ is replaced by $(x, -y)$, the reflection about the $x$-axis.
> - $y = f(-x)$ contains $(-a, b)$, since $f(-(-a)) = f(a) = b$: the point $(x, y)$ is replaced by $(-x, y)$, the reflection about the $y$-axis.

^pf-3-2

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-2|Def. §1.2]]

> [!example] Example §3.1: Transformations of the Square Root
> Given the graph of $y = \sqrt{x}$, use transformations to graph $y = \sqrt{x} - 2$, $y = \sqrt{x - 2}$, $y = -\sqrt{x}$, $y = 2\sqrt{x}$ and $y = \sqrt{-x}$.
>
> The graph of $\sqrt{x}$ is the upper half of the parabola $x = y^2$, starting at the origin ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-6|Def. §2.6]]). By Theorems §3.1 and §3.2:
> - $y = \sqrt{x} - 2$: shift $2$ units down. It starts at $(0, -2)$ and crosses the $x$-axis where $\sqrt{x} = 2$, at $x = 4$.
> - $y = \sqrt{x - 2}$: shift $2$ units to the right. It starts at $(2, 0)$, and its domain is $[2, \infty)$.
> - $y = -\sqrt{x}$: reflect about the $x$-axis.
> - $y = 2\sqrt{x}$: stretch vertically by a factor of $2$; it passes through $(1, 2)$ and $(4, 4)$.
> - $y = \sqrt{-x}$: reflect about the $y$-axis. Its domain is $(-\infty, 0]$.
>
> Changes to the output (outside $f$) move the graph vertically and leave the domain alone; changes to the input (inside $f$) move it horizontally and change the domain.
>
> *Stewart: Example 1.3.1*

^ex-3-1

![[m233-3-1.svg]]
*Example §3.1. (a) Operations on the output: $\sqrt{x}$ (black) shifted down by $2$ (red), reflected about the $x$-axis (green), stretched vertically by $2$ (orange). All keep the domain $[0, \infty)$. (b) Operations on the input: $\sqrt{x - 2}$ (blue) is $\sqrt{x}$ moved $2$ to the right, starting at $(2, 0)$; $\sqrt{-x}$ (green) is the mirror image of $\sqrt{x}$ in the $y$-axis, with domain $(-\infty, 0]$.*

> [!example] Example §3.2: Combining Transformations
> **(a)** Sketch $f(x) = x^2 + 6x + 10$. Completing the square,
>
> $$
> x^2 + 6x + 10 = (x^2 + 6x + 9) + 1 = (x + 3)^2 + 1 .
> $$
>
> So start with the parabola $y = x^2$, shift it $3$ units to the left (giving $(x + 3)^2$) and then $1$ unit upward. The result is a parabola opening upward with vertex $(-3, 1)$.
>
> The same computation works for every quadratic. For $a \ne 0$,
>
> $$
> ax^2 + bx + c = a\Big(x + \frac{b}{2a}\Big)^2 + \Big(c - \frac{b^2}{4a}\Big) ,
> $$
>
> so the graph is the parabola $y = ax^2$ shifted horizontally and vertically, opening upward if $a > 0$ and downward if $a < 0$ (the claim in [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-4|Def. §2.4]]).
>
> **(b)** Sketch $y = \sin 2x$. Shrink the graph of $y = \sin x$ horizontally by a factor of $2$. Since $\sin x$ has period $2\pi$, $\sin 2x$ has period $2\pi/2 = \pi$: it completes a full wave on $[0, \pi]$, with zeros at multiples of $\pi/2$ and maximum $1$ at $x = \pi/4$.
>
> **(c)** Sketch $y = 1 - \sin x$. Reflect $y = \sin x$ about the $x$-axis to get $y = -\sin x$, then shift $1$ unit upward. The graph oscillates between $0$ (at $x = \pi/2 + 2n\pi$, where $\sin x = 1$) and $2$ (at $x = 3\pi/2 + 2n\pi$), with period $2\pi$.
>
> *Stewart: Examples 1.3.2 and 1.3.3*

^ex-3-2

> [!example] Example §3.3: A Model for the Length of Daylight
> At latitude $40^\circ$N (Philadelphia), daylight lasts about $14.8$ hours on June 21 and $9.2$ hours on December 21, and a graph of daylight against the date has the shape of a shifted and stretched sine curve, starting its cycle at about $12$ hours on March 21. Find a function that models the length of daylight at Philadelphia.
>
> Build the model from $y = \sin t$ step by step, with $t$ in days.
> - **Amplitude** (vertical stretch): $\frac12(14.8 - 9.2) = 2.8$.
> - **Period** (horizontal stretch): the cycle should last about $365$ days, while $\sin t$ has period $2\pi$. So stretch horizontally by the factor $365/2\pi$, that is, replace $t$ by $\frac{2\pi}{365} t$.
> - **Horizontal shift:** the cycle begins on March 21, the 80th day of the year, so shift $80$ units to the right: replace $t$ by $t - 80$.
> - **Vertical shift:** the curve oscillates about $12$ hours (the midpoint $\frac12(14.8 + 9.2) = 12$), so shift $12$ units up.
>
> The model for the length of daylight on the $t$th day of the year is
>
> $$
> L(t) = 12 + 2.8 \sin\Big[\frac{2\pi}{365}(t - 80)\Big] .
> $$
>
> Check: the maximum occurs when $\frac{2\pi}{365}(t - 80) = \frac{\pi}{2}$, at $t = 80 + 365/4 \approx 171$ (June 20), with $L = 12 + 2.8 = 14.8$; the minimum $12 - 2.8 = 9.2$ occurs at $t = 80 + 3 \cdot 365/4 \approx 354$ (December 20).
>
> *Stewart: Example 1.3.4*

^ex-3-3

> [!theorem] Theorem §3.3: The Graph of |f(x)|
> The graph of $y = |f(x)|$ is obtained from the graph of $y = f(x)$ by keeping the part that lies on or above the $x$-axis and reflecting the part that lies below the $x$-axis about the $x$-axis.
>
> *Stewart: 1.3 (text)*

^thm-3-3

> [!proof]+ Proof
> By the definition of absolute value ([[§1 Four Ways to Represent a Function#^def-1-6|Def. §1.6]]), $|f(x)| = f(x)$ when $f(x) \ge 0$ and $|f(x)| = -f(x)$ when $f(x) < 0$. So where the graph of $f$ is on or above the $x$-axis, $y = |f(x)|$ has the same points; where it is below, the point $(a, f(a))$ is replaced by $(a, -f(a))$, its reflection about the $x$-axis (as in Theorem §3.2).

^pf-3-3

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-6|Def. §1.6]], [[§3 New Functions from Old Functions#^thm-3-2|§3.2]]

> [!example] Example §3.4: An Absolute Value of a Parabola
> Sketch the graph of $y = |x^2 - 1|$.
>
> First graph $y = x^2 - 1$: the parabola $y = x^2$ shifted $1$ unit down (Theorem §3.1), with vertex $(0, -1)$ and $x$-intercepts $\pm 1$. It lies below the $x$-axis exactly when $x^2 < 1$, that is, $-1 < x < 1$. By Theorem §3.3, reflect that part about the $x$-axis and keep the rest:
>
> $$
> |x^2 - 1| = \begin{cases} x^2 - 1 & \text{if } |x| \ge 1 \\ 1 - x^2 & \text{if } |x| < 1 . \end{cases}
> $$
>
> The graph has corners at $(\pm 1, 0)$ and a local peak at $(0, 1)$.
>
> *Stewart: Example 1.3.5*

^ex-3-4

![[m233-3-2.svg]]
*Example §3.4. The arc of $y = x^2 - 1$ between $-1$ and $1$ (dashed gray) lies below the $x$-axis; taking the absolute value flips it up (red arrows) to the arc $y = 1 - x^2$ through $(0, 1)$. Outside $[-1, 1]$ the parabola is already above the axis and is unchanged (blue). Where the two pieces meet, at $(\pm 1, 0)$, the graph has corners.*

## Combinations of Functions

> [!definition] Definition §3.1: Sum, Difference, Product and Quotient
> Given two functions $f$ and $g$, the **sum**, **difference**, **product** and **quotient** functions are defined by
>
> $$
> (f + g)(x) = f(x) + g(x), \qquad (f - g)(x) = f(x) - g(x), \qquad (fg)(x) = f(x)\,g(x), \qquad \Big(\frac{f}{g}\Big)(x) = \frac{f(x)}{g(x)} .
> $$
>
> If the domain of $f$ is $A$ and the domain of $g$ is $B$, then
> - $f + g$, $f - g$ and $fg$ have domain $A \cap B$, because both $f(x)$ and $g(x)$ must be defined;
> - $f/g$ has domain $\{x \in A \cap B \mid g(x) \ne 0\}$, because we cannot divide by $0$.
>
> For example, $\sqrt{x}$ has domain $A = [0, \infty)$ and $\sqrt{2 - x}$ has domain $B = (-\infty, 2]$, so $\sqrt{x} + \sqrt{2 - x}$ has domain $A \cap B = [0, 2]$. And with $f(x) = x^2$, $g(x) = x - 1$, the quotient $(f/g)(x) = x^2/(x - 1)$ has domain $\{x \mid x \ne 1\} = (-\infty, 1) \cup (1, \infty)$.
>
> *Stewart: 1.3, Definition (boxed; domains in the text)*

^def-3-1

> [!remark]- Connections
> - Developed further in: [[§17 Continuous Functions#^thm-17-3|451 Thm. §17.3]], where these combinations of continuous functions are shown to be continuous on the common domain (Calculus: [[§10 Continuity#^thm-10-1|§10.1]]).

> [!definition] Definition §3.2: Composite Function
> Given two functions $f$ and $g$, the **composite function** $f \circ g$ (also called the **composition** of $f$ and $g$, read "$f$ circle $g$") is defined by
>
> $$
> (f \circ g)(x) = f(g(x)) .
> $$
>
> Its domain is the set of all $x$ in the domain of $g$ such that $g(x)$ is in the domain of $f$: $(f \circ g)(x)$ is defined whenever both $g(x)$ and $f(g(x))$ are defined. As machines, $f \circ g$ is the $g$ machine followed by the $f$ machine: the output of $g$ is the input of $f$.
>
> The composition of three or more functions is formed in the same way: $f \circ g \circ h$ applies $h$, then $g$, then $f$,
>
> $$
> (f \circ g \circ h)(x) = f(g(h(x))) .
> $$
>
> *Stewart: 1.3, Definition (boxed; domain and three functions in the text)*

^def-3-2

> [!remark]- Connections
> - Rigorous treatment: [[§8 Functions#^def-8-5|250 Def. §8.5]], for $f : X \to Y$ and $g : Y \to Z$; Stewart's domain rule is the restriction needed when the values of $g$ do not all lie in the domain of $f$ ([[§8 Functions#^ex-8-6|250 Ex. §8.6]](b)). That $f \circ g \circ h$ needs no brackets is associativity, [[§8 Functions#^prop-8-1|250 Prop. §8.1]].

> [!remark] Remark: The Order Matters
> In general $f \circ g \ne g \circ f$. The notation $f \circ g$ means that the function $g$ is applied *first* and then $f$ is applied *second*, the reverse of the order in which the letters are read. Example §3.5(a) shows two different composites of the same pair of functions.

^rem-3-2

> [!example] Example §3.5: Composites, Their Domains, and Decomposition
> **(a)** If $f(x) = x^2$ and $g(x) = x - 3$, find $f \circ g$ and $g \circ f$.
>
> $$
> (f \circ g)(x) = f(g(x)) = f(x - 3) = (x - 3)^2, \qquad (g \circ f)(x) = g(f(x)) = g(x^2) = x^2 - 3 .
> $$
>
> $f \circ g$ first subtracts $3$ and then squares; $g \circ f$ first squares and then subtracts $3$. At $x = 0$ they give $9$ and $-3$, so $f \circ g \ne g \circ f$.
>
> **(b)** If $f(x) = \sqrt{x}$ and $g(x) = \sqrt{2 - x}$, find $f \circ g$, $g \circ f$, $f \circ f$, $g \circ g$ and their domains.
> - $(f \circ g)(x) = f\big(\sqrt{2 - x}\big) = \sqrt{\sqrt{2 - x}} = \sqrt[4]{2 - x}$. We need $2 - x \ge 0$; the inner value is then $\ge 0$, in the domain of $f$. Domain: $\{x \mid x \le 2\} = (-\infty, 2]$.
> - $(g \circ f)(x) = g\big(\sqrt{x}\big) = \sqrt{2 - \sqrt{x}}$. We need $x \ge 0$ for $\sqrt{x}$, and $2 - \sqrt{x} \ge 0$, that is, $\sqrt{x} \le 2$, or $x \le 4$ (for $0 \le a \le b$, $a^2 \le b^2$). Domain: $[0, 4]$.
> - $(f \circ f)(x) = f\big(\sqrt{x}\big) = \sqrt{\sqrt{x}} = \sqrt[4]{x}$. Domain: $[0, \infty)$.
> - $(g \circ g)(x) = g\big(\sqrt{2 - x}\big) = \sqrt{2 - \sqrt{2 - x}}$. We need $2 - x \ge 0$, that is, $x \le 2$, and $2 - \sqrt{2 - x} \ge 0$, that is, $\sqrt{2 - x} \le 2$, or $2 - x \le 4$, or $x \ge -2$. Domain: $[-2, 2]$.
>
> The simplified formula alone does not show the domain: $\sqrt[4]{2 - x}$ and $\sqrt{2 - \sqrt{x}}$ must be checked step by step, one function at a time.
>
> **(c)** Find $f \circ g \circ h$ if $f(x) = x/(x + 1)$, $g(x) = x^{10}$ and $h(x) = x + 3$. Work from the inside out:
>
> $$
> (f \circ g \circ h)(x) = f(g(h(x))) = f(g(x + 3)) = f\big((x + 3)^{10}\big) = \frac{(x + 3)^{10}}{(x + 3)^{10} + 1} .
> $$
>
> **(d)** Given $F(x) = \cos^2(x + 9)$, find $f$, $g$, $h$ with $F = f \circ g \circ h$. Read the formula $F(x) = [\cos(x + 9)]^2$ as a sequence of operations: first add $9$, then take the cosine, finally square. So let
>
> $$
> h(x) = x + 9, \qquad g(x) = \cos x, \qquad f(x) = x^2 .
> $$
>
> Then $(f \circ g \circ h)(x) = f(g(x + 9)) = f(\cos(x + 9)) = [\cos(x + 9)]^2 = F(x)$. Building up complicated functions, as in (c), is the direction used so far; decomposing them, as here, is what calculus needs.
>
> *Stewart: Examples 1.3.6, 1.3.7, 1.3.8 and 1.3.9*

^ex-3-5
