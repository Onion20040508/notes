---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 116
stewart: "15.2"
aliases: ["Stewart 15.2"]
tags: [calculus, math233]
---
← [[§115 Double Integrals Over Rectangles]] · ↑ [[· 15 Multiple Integrals]] · [[§117 Double Integrals in Polar Coordinates]] →

*Stewart, Section 15.2 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q7, Q10, Q11), Practice Final Exam (Q1(b)), Practice Final Set 1 (Part I, Q2).*

A double integral over a bounded region $D$ is defined by enclosing $D$ in a rectangle and extending the integrand by $0$. For the two kinds of region met in practice, those lying between two graphs $y = g_1(x)$, $y = g_2(x)$ (type I) or $x = h_1(y)$, $x = h_2(y)$ (type II), Fubini's Theorem turns the integral into an iterated integral whose inner limits are functions. The real work is reading the limits off a sketch of $D$. Describing the same region the other way reverses the order of integration, which can make an impossible iterated integral easy. The section ends with the properties of double integrals: linearity, comparison, additivity over regions, area, and the resulting bounds.

## General Regions

> [!definition] Definition §139.1: The Double Integral over a Bounded Region
> Let $D$ be a **bounded** region, that is, one that can be enclosed in a rectangular region $R$. For a function $f$ defined on $D$, define a new function $F$ with domain $R$ by
>
> $$
> F(x, y) = \begin{cases} f(x, y) & \text{if } (x, y) \text{ is in } D \\ 0 & \text{if } (x, y) \text{ is in } R \text{ but not in } D. \end{cases} \qquad (1)
> $$
>
> If $F$ is integrable over $R$ ([[§115 Double Integrals Over Rectangles#^def-115-2|Definition §115.2]]), the **double integral of $f$ over $D$** is
>
> $$
> \iint_D f(x, y)\,dA = \iint_R F(x, y)\,dA . \qquad (2)
> $$
>
> *Stewart: 15.2, Equations 1 and 2*

^def-116-1

This makes sense because $\iint_R F\,dA$ was defined in [[§115 Double Integrals Over Rectangles#^def-115-2|Definition §115.2]], and it does not matter which rectangle $R \supseteq D$ is used, since $F = 0$ outside $D$ contributes nothing. If $f(x, y) \ge 0$, then $\iint_D f(x, y)\,dA$ is the volume of the solid above $D$ and under the graph of $f$: it is the volume under the graph of $F$, which is the graph of $f$ over $D$ and the flat plane $z = 0$ elsewhere in $R$.

$F$ is likely to be discontinuous at the boundary points of $D$. Nonetheless, if $f$ is continuous on $D$ and the boundary curve of $D$ is "well behaved" (in a sense outside the scope of Stewart's book), then $\iint_R F\,dA$ exists, and therefore $\iint_D f\,dA$ exists ([[§115 Double Integrals Over Rectangles#^thm-115-1|Theorem §115.1]]). In particular this is the case for the following two types of region.

> [!definition] Definition §139.2: Type I Region
> A plane region $D$ is of **type I** if it lies between the graphs of two continuous functions of $x$:
>
> $$
> D = \{(x, y) \mid a \le x \le b,\ g_1(x) \le y \le g_2(x)\} ,
> $$
>
> where $g_1$ and $g_2$ are continuous on $[a, b]$. The functions need not be given by a single formula: a continuous piecewise-defined $g_2$ is allowed.
>
> *Stewart: 15.2 (text)*

^def-116-2

> [!theorem] Theorem §139.1: Integrals over Type I Regions
> If $f$ is continuous on a type I region $D$ described by
>
> $$
> D = \{(x, y) \mid a \le x \le b,\ g_1(x) \le y \le g_2(x)\} ,
> $$
>
> then
>
> $$
> \iint_D f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx .
> $$
>
> In the inner integral $x$ is constant, not only in $f(x, y)$ but also in the limits $g_1(x)$ and $g_2(x)$.
>
> *Stewart: 15.2, Equation 3*

^thm-116-1

> [!proof]+ Proof
> Choose a rectangle $R = [a, b] \times [c, d]$ that contains $D$, and let $F$ be the function of Equation 1: $F = f$ on $D$ and $F = 0$ on the rest of $R$. By [[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]] and Fubini's Theorem ([[§115 Double Integrals Over Rectangles#^thm-115-3|Theorem §115.3]], in its general form, since $F$ is bounded and discontinuous at most on the boundary curves $y = g_1(x)$, $y = g_2(x)$),
>
> $$
> \iint_D f(x, y)\,dA = \iint_R F(x, y)\,dA = \int_a^b \int_c^d F(x, y)\,dy\,dx .
> $$
>
> For fixed $x$ in $[a, b]$, the point $(x, y)$ lies outside $D$ when $y < g_1(x)$ or $y > g_2(x)$, so $F(x, y) = 0$ there, while $F(x, y) = f(x, y)$ for $g_1(x) \le y \le g_2(x)$. Therefore
>
> $$
> \int_c^d F(x, y)\,dy = \int_{g_1(x)}^{g_2(x)} F(x, y)\,dy = \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy ,
> $$
>
> and substituting this into the outer integral gives the formula.

^pf-116-1

*Uses:* [[§116 Double Integrals Over General Regions#^def-116-1|Def. §116.1]], [[§116 Double Integrals Over General Regions#^def-116-2|Def. §116.2]], [[§115 Double Integrals Over Rectangles#^thm-115-3|§115.3]]

> [!definition] Definition §139.3: Type II Region
> A plane region $D$ is of **type II** if it can be expressed as
>
> $$
> D = \{(x, y) \mid c \le y \le d,\ h_1(y) \le x \le h_2(y)\} ,
> $$
>
> where $h_1$ and $h_2$ are continuous on $[c, d]$.
>
> *Stewart: 15.2 (text)*

^def-116-3

> [!theorem] Theorem §139.2: Integrals over Type II Regions
> If $f$ is continuous on a type II region $D$ described by
>
> $$
> D = \{(x, y) \mid c \le y \le d,\ h_1(y) \le x \le h_2(y)\} ,
> $$
>
> then
>
> $$
> \iint_D f(x, y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\,dy .
> $$
>
> *Stewart: 15.2, Equation 4*

^thm-116-2

> [!proof]+ Proof
> The proof of [[§116 Double Integrals Over General Regions#^thm-116-1|Theorem §116.1]] with the roles of $x$ and $y$ exchanged. Enclose $D$ in $R = [a, b] \times [c, d]$ and extend $f$ by $0$ to $F$. Fubini's Theorem in the order $dx\,dy$ gives $\iint_D f\,dA = \int_c^d \int_a^b F(x, y)\,dx\,dy$. For fixed $y$, $F(x, y) = 0$ when $x < h_1(y)$ or $x > h_2(y)$, and $F(x, y) = f(x, y)$ for $h_1(y) \le x \le h_2(y)$, so $\int_a^b F(x, y)\,dx = \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx$.

^pf-116-2

*Uses:* [[§116 Double Integrals Over General Regions#^def-116-1|Def. §116.1]], [[§116 Double Integrals Over General Regions#^def-116-3|Def. §116.3]], [[§115 Double Integrals Over Rectangles#^thm-115-3|§115.3]]

> [!remark]- Connections
> - Rigorous treatment: type I and type II regions [[§23 Fubini's Theorem#^def-23-1|452 Def. §23.1]], and the two formulas [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]], [[§23 Fubini's Theorem#^thm-23-3|452 Thm. §23.3]]. 452 proves them directly, controlling the error from the curved boundary, instead of extending by $0$ and invoking Fubini for a discontinuous function.

> [!remark] Remark: Method — Setting Up a Double Integral
> 1. **Draw $D$.** Find where the boundary curves intersect; these give the outer limits.
> 2. **Type I (order $dy\,dx$).** Draw a vertical arrow through $D$ at a typical $x$. It enters $D$ at the lower boundary $y = g_1(x)$ (lower limit of the inner integral) and leaves at the upper boundary $y = g_2(x)$ (upper limit). The outer limits are the extreme values $a \le x \le b$.
> 3. **Type II (order $dx\,dy$).** Draw a horizontal arrow from the left boundary $x = h_1(y)$ to the right boundary $x = h_2(y)$; the outer limits are $c \le y \le d$. Boundary curves must now be solved for $x$.
> 4. **Choose the description with one piece.** If the arrows in one direction enter or leave $D$ through different curves for different values of the outer variable, that description needs $D$ cut into pieces and several iterated integrals (Property 8 below). Use the other one if it has a single piece ([[§116 Double Integrals Over General Regions#^ex-116-2|Examples §116.2]] and [[§116 Double Integrals Over General Regions#^ex-116-3|§116.3]]).
> 5. **Check the result.** The inner limits contain at most the outer variable; the outer limits are constants.

^rem-116-1

> [!example] Example §139.1: A Type I Region
> Evaluate $\displaystyle\iint_D (x + 2y)\,dA$, where $D$ is the region bounded by the parabolas $y = 2x^2$ and $y = 1 + x^2$.
>
> The parabolas intersect when $2x^2 = 1 + x^2$, that is, $x^2 = 1$, so $x = \pm 1$. Between these, the lower boundary is $y = 2x^2$ and the upper boundary is $y = 1 + x^2$, so $D$ is a type I region (it is not type II: a horizontal line at height $1 < y < 2$ meets it in two segments):
>
> $$
> D = \{(x, y) \mid -1 \le x \le 1,\ 2x^2 \le y \le 1 + x^2\} .
> $$
>
> By [[§116 Double Integrals Over General Regions#^thm-116-1|Theorem §116.1]],
>
> $$
> \begin{aligned}
> \iint_D (x + 2y)\,dA &= \int_{-1}^{1} \int_{2x^2}^{1 + x^2} (x + 2y)\,dy\,dx = \int_{-1}^{1} \Big[ xy + y^2 \Big]_{y = 2x^2}^{y = 1 + x^2} dx \\
> &= \int_{-1}^{1} \big[ x(1 + x^2) + (1 + x^2)^2 - x(2x^2) - (2x^2)^2 \big]\,dx = \int_{-1}^{1} (-3x^4 - x^3 + 2x^2 + x + 1)\,dx \\
> &= \Big[ -3\frac{x^5}{5} - \frac{x^4}{4} + 2\frac{x^3}{3} + \frac{x^2}{2} + x \Big]_{-1}^{1} = 2\Big( -\frac35 + \frac23 + 1 \Big) = \frac{32}{15} .
> \end{aligned}
> $$
>
> *Stewart: Example 15.2.1*

^ex-116-1

> [!example] Example §139.2: Choosing the Simpler Description
> Evaluate $\displaystyle\iint_D xy\,dA$, where $D$ is the region bounded by the line $y = x - 1$ and the parabola $y^2 = 2x + 6$.
>
> The curves meet where $(x - 1)^2 = 2x + 6$, that is, $x^2 - 4x - 5 = (x - 5)(x + 1) = 0$: at $(-1, -2)$ and $(5, 4)$. $D$ is both type I and type II, but as a type I region its lower boundary consists of two parts. As a type II region, with the left boundary $x = \tfrac12 y^2 - 3$ and the right boundary $x = y + 1$,
>
> $$
> D = \{(x, y) \mid -2 \le y \le 4,\ \tfrac12 y^2 - 3 \le x \le y + 1\} .
> $$
>
> By [[§116 Double Integrals Over General Regions#^thm-116-2|Theorem §116.2]],
>
> $$
> \begin{aligned}
> \iint_D xy\,dA &= \int_{-2}^{4} \int_{\frac12 y^2 - 3}^{y + 1} xy\,dx\,dy = \int_{-2}^{4} \Big[ \frac{x^2}{2} y \Big]_{x = \frac12 y^2 - 3}^{x = y + 1} dy = \frac12 \int_{-2}^{4} y \Big[ (y + 1)^2 - \big(\tfrac12 y^2 - 3\big)^2 \Big]\,dy \\
> &= \frac12 \int_{-2}^{4} \Big( -\frac{y^5}{4} + 4y^3 + 2y^2 - 8y \Big)\,dy = \frac12 \Big[ -\frac{y^6}{24} + y^4 + 2\frac{y^3}{3} - 4y^2 \Big]_{-2}^{4} = \frac12 \big( 64 - (-8) \big) = 36 .
> \end{aligned}
> $$
>
> As a type I region, the lower boundary would be $g_1(x) = -\sqrt{2x + 6}$ for $-3 \le x \le -1$ and $g_1(x) = x - 1$ for $-1 < x \le 5$, and we would need two integrals:
>
> $$
> \iint_D xy\,dA = \int_{-3}^{-1} \int_{-\sqrt{2x + 6}}^{\sqrt{2x + 6}} xy\,dy\,dx + \int_{-1}^{5} \int_{x - 1}^{\sqrt{2x + 6}} xy\,dy\,dx .
> $$
>
> *Stewart: Example 15.2.3*

^ex-116-2

![[m233-99-1.svg]]
*[[§116 Double Integrals Over General Regions#^ex-116-2|Example §116.2]] both ways. Left: as a type I region, the vertical arrows enter $D$ through the lower half of the parabola for $x < -1$ and through the line for $x > -1$, so the integral splits at $x = -1$. Right: as a type II region every horizontal arrow runs from the parabola $x = \frac12 y^2 - 3$ to the line $x = y + 1$, and one integral suffices.*

> [!example] Example §139.3: A Region Bounded by Three Curves
> Let $D$ be the region in the $xy$-plane enclosed by $y = 0$, $y = x^2$ and $y = 2 - x$. Compute $\displaystyle\iint_D (xy^2 - x)\,dA$.
>
> **The region.** The parabola and the line meet where $x^2 = 2 - x$, that is, $(x + 2)(x - 1) = 0$; in the region enclosed together with $y = 0$, this is the point $(1, 1)$. So $D$ has corners $(0, 0)$, $(2, 0)$ and $(1, 1)$, with the parabola on the left and the line on the right. A horizontal arrow at height $y$, $0 \le y \le 1$, runs from $x = \sqrt{y}$ to $x = 2 - y$:
>
> $$
> D = \{(x, y) \mid 0 \le y \le 1,\ \sqrt{y} \le x \le 2 - y\} .
> $$
>
> (As a type I region it needs two pieces: $0 \le y \le x^2$ for $0 \le x \le 1$ and $0 \le y \le 2 - x$ for $1 \le x \le 2$.)
>
> **The integral.** Since $xy^2 - x = x(y^2 - 1)$,
>
> $$
> \iint_D (xy^2 - x)\,dA = \int_0^1 (y^2 - 1) \int_{\sqrt y}^{2 - y} x\,dx\,dy = \int_0^1 (y^2 - 1) \cdot \frac12 \big[ (2 - y)^2 - y \big]\,dy = \frac12 \int_0^1 (y^2 - 1)(y^2 - 5y + 4)\,dy .
> $$
>
> Expanding, $(y^2 - 1)(y^2 - 5y + 4) = y^4 - 5y^3 + 3y^2 + 5y - 4$, so
>
> $$
> \iint_D (xy^2 - x)\,dA = \frac12 \Big[ \frac{y^5}{5} - \frac{5y^4}{4} + y^3 + \frac{5y^2}{2} - 4y \Big]_0^1 = \frac12 \Big( \frac15 - \frac54 + 1 + \frac52 - 4 \Big) = \frac12 \Big( -\frac{31}{20} \Big) = -\frac{31}{40} .
> $$
>
> *Source: 233 Exam 2 Practice Questions, Q7 (also Practice Final Exam, Q1(b))*

^ex-116-3

## Changing the Order of Integration

By [[§116 Double Integrals Over General Regions#^thm-116-1|Theorems §116.1]] and [[§116 Double Integrals Over General Regions#^thm-116-2|§116.2]], a region that is both type I and type II gives two iterated integrals equal to the same double integral. Sometimes one order is much harder than the other, or even impossible. To change the order of an iterated integral: read off the region $D$ from its limits, sketch it, and describe $D$ the other way.

> [!example] Example §139.4: An Integral That Needs Reversing
> Evaluate $\displaystyle\int_0^1 \int_x^1 \sin(y^2)\,dy\,dx$.
>
> As it stands, we would first have to evaluate $\int \sin(y^2)\,dy$, and this is impossible in finite terms: $\int \sin(y^2)\,dy$ is not an elementary function ([[§55 Strategy for Integration#^thm-55-2|Theorem §55.2]]). So we change the order. Using [[§116 Double Integrals Over General Regions#^thm-116-1|Theorem §116.1]] backward, the iterated integral is $\iint_D \sin(y^2)\,dA$ over
>
> $$
> D = \{(x, y) \mid 0 \le x \le 1,\ x \le y \le 1\} ,
> $$
>
> the triangle with vertices $(0, 0)$, $(0, 1)$, $(1, 1)$. The same triangle is $D = \{(x, y) \mid 0 \le y \le 1,\ 0 \le x \le y\}$, so by [[§116 Double Integrals Over General Regions#^thm-116-2|Theorem §116.2]]
>
> $$
> \int_0^1 \int_x^1 \sin(y^2)\,dy\,dx = \int_0^1 \int_0^y \sin(y^2)\,dx\,dy = \int_0^1 \Big[ x \sin(y^2) \Big]_{x=0}^{x=y} dy = \int_0^1 y \sin(y^2)\,dy = -\tfrac12 \cos(y^2) \Big]_0^1 = \tfrac12 (1 - \cos 1) .
> $$
>
> *Stewart: Example 15.2.5*

^ex-116-4

> [!example] Example §116.5: Two More Reversals
> **(a)** Evaluate $\displaystyle\int_0^1 \int_{\sqrt y}^{1} \sqrt{x^3 + 1}\,dx\,dy$ by reversing the order of integration.
>
> The region is $0 \le y \le 1$, $\sqrt y \le x \le 1$: between the parabola $x = \sqrt y$ (that is, $y = x^2$) on the left and the line $x = 1$ on the right. As a type I region it is $0 \le x \le 1$, $0 \le y \le x^2$. So
>
> $$
> \int_0^1 \int_{\sqrt y}^{1} \sqrt{x^3 + 1}\,dx\,dy = \int_0^1 \int_0^{x^2} \sqrt{x^3 + 1}\,dy\,dx = \int_0^1 x^2 \sqrt{x^3 + 1}\,dx = \Big[ \frac29 (x^3 + 1)^{3/2} \Big]_0^1 = \frac29 \big( 2^{3/2} - 1 \big) ,
> $$
>
> the last step by the substitution $u = x^3 + 1$, $du = 3x^2\,dx$ ([[§43 The Substitution Rule#^thm-43-3|Theorem §43.3]]).
>
> **(b)** Evaluate $\displaystyle\int_0^1 \int_{x^2}^{1} x^3 \sin(y^3)\,dy\,dx$.
>
> The region $0 \le x \le 1$, $x^2 \le y \le 1$ lies between $y = x^2$ and $y = 1$; as a type II region it is $0 \le y \le 1$, $0 \le x \le \sqrt y$. So
>
> $$
> \int_0^1 \int_{x^2}^{1} x^3 \sin(y^3)\,dy\,dx = \int_0^1 \sin(y^3) \int_0^{\sqrt y} x^3\,dx\,dy = \int_0^1 \sin(y^3) \frac{y^2}{4}\,dy = \frac{1}{12} \Big[ -\cos(y^3) \Big]_0^1 = \frac{1}{12} (1 - \cos 1) .
> $$
>
> In both, the inner integral in the given order has no elementary antiderivative; after reversing, the new inner integral produces exactly the factor ($x^2$, resp. $y^2$) that the substitution needs.
>
> *Source: 233 Exam 2 Practice Questions, Q10 and Q11*

^ex-116-5

> [!remark] Remark: When Reversing Needs Two Integrals
> Which of the following become a sum of two double integrals when the order is reversed?
>
> $$
> \text{A: } \int_{-1}^{2} \int_{x^2 - 2}^{x} f\,dy\,dx, \qquad \text{B: } \int_0^1 \int_{y^2}^{2 - y} g\,dx\,dy, \qquad \text{C: } \int_0^1 \int_{\arctan x}^{\pi/4} h\,dy\,dx .
> $$
>
> - **A**: the region lies between the parabola $y = x^2 - 2$ and the line $y = x$, which meet at $(-1, -1)$ and $(2, 2)$. For $-2 \le y \le -1$ a horizontal line meets it between the two halves $x = \pm\sqrt{y + 2}$ of the parabola, while for $-1 \le y \le 2$ it runs from the line $x = y$ to $x = \sqrt{y + 2}$. The left boundary changes, so two integrals are needed.
> - **B**: the region lies between $x = y^2$ and $x = 2 - y$, which meet at $(1, 1)$, and $0 \le x \le 2$. For $0 \le x \le 1$ the vertical line runs from $y = 0$ to $y = \sqrt x$, for $1 \le x \le 2$ from $y = 0$ to $y = 2 - x$: two integrals.
> - **C**: the region $0 \le x \le 1$, $\arctan x \le y \le \pi/4$ is also $0 \le y \le \pi/4$, $0 \le x \le \tan y$: one integral.
>
> So the answer is A and B. In each case the test is step 4 of the method: does the arrow in the new direction always enter and leave through the same two curves?
>
> *Source: 233 Practice Final Set 1, Part I Q2*

^rem-116-2

## Properties of Double Integrals

Assume that all of the following integrals exist.

> [!theorem] Theorem §139.3: Linearity and Comparison
> For functions $f$, $g$ integrable over $D$ and a constant $c$,
>
> $$
> \iint_D [f(x, y) + g(x, y)]\,dA = \iint_D f(x, y)\,dA + \iint_D g(x, y)\,dA , \qquad (5)
> $$
>
> $$
> \iint_D c f(x, y)\,dA = c \iint_D f(x, y)\,dA . \qquad (6)
> $$
>
> If $f(x, y) \ge g(x, y)$ for all $(x, y)$ in $D$, then
>
> $$
> \iint_D f(x, y)\,dA \ge \iint_D g(x, y)\,dA . \qquad (7)
> $$
>
> *Stewart: 15.2, Properties 5, 6 and 7*

^thm-116-3

> [!proof]+ Proof
> *Stewart says these "can be proved in the same manner as in Section 5.2" for rectangles, and follow from [[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]] for general regions; here are the details.*
>
> **Rectangles.** Let $D = R$ be a rectangle. For any $m$, $n$ and sample points, the double Riemann sums satisfy
>
> $$
> \sum_{i,j} (f + g)(x_{ij}^*, y_{ij}^*)\,\Delta A = \sum_{i,j} f(x_{ij}^*, y_{ij}^*)\,\Delta A + \sum_{i,j} g(x_{ij}^*, y_{ij}^*)\,\Delta A , \qquad \sum_{i,j} c f(x_{ij}^*, y_{ij}^*)\,\Delta A = c \sum_{i,j} f(x_{ij}^*, y_{ij}^*)\,\Delta A .
> $$
>
> The right-hand sides converge to $\iint_R f\,dA + \iint_R g\,dA$ and $c\iint_R f\,dA$ as $m, n \to \infty$, by the Sum and Constant Multiple Laws for limits, so the left-hand sides converge to the same numbers: this is (5) and (6). If $f \ge g$ on $R$, then every Riemann sum of $f - g$ is $\ge 0$, so its limit is $\ge 0$; by (5) and (6) that limit is $\iint_R f\,dA - \iint_R g\,dA$, which gives (7).
>
> **General regions.** Enclose $D$ in a rectangle $R$ and write $F_f$ for the extension of $f$ by $0$ ([[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]]). Then $F_{f+g} = F_f + F_g$ and $F_{cf} = cF_f$ on $R$, and $f \ge g$ on $D$ gives $F_f \ge F_g$ on $R$ (both are $0$ outside $D$). So (5), (6) and (7) for $D$ are (5), (6) and (7) for $F_f$, $F_g$ on $R$.

^pf-116-3

*Uses:* [[§115 Double Integrals Over Rectangles#^def-115-2|Def. §115.2]], [[§116 Double Integrals Over General Regions#^def-116-1|Def. §116.1]], [[§40 Properties of the Definite Integral#^thm-40-1|§40.1]], [[§40 Properties of the Definite Integral#^thm-40-3|§40.3]] (the single-integral properties, proved the same way)

> [!remark]- Connections
> - Rigorous treatment: [[§22 Properties of the Integral#^thm-22-2|452 Thm. §22.2]] (additivity in the integrand), [[§22 Properties of the Integral#^thm-22-1|452 Thm. §22.1]] (scalar multiples), [[§22 Properties of the Integral#^thm-22-4|452 Thm. §22.4]] (comparison), where the existence of $\iint (f + g)$ and $\iint cf$ is also proved.

> [!theorem] Theorem §139.4: Additivity over Regions
> If $D = D_1 \cup D_2$, where $D_1$ and $D_2$ don't overlap except perhaps on their boundaries, then
>
> $$
> \iint_D f(x, y)\,dA = \iint_{D_1} f(x, y)\,dA + \iint_{D_2} f(x, y)\,dA . \qquad (8)
> $$
>
> *Stewart: 15.2, Property 8*

^thm-116-4

*Stewart omits the proof (it is the analogue of $\int_a^b = \int_a^c + \int_c^b$, [[§40 Properties of the Definite Integral#^thm-40-2|Theorem §40.2]]); see [[§22 Properties of the Integral#^thm-22-3|452 Thm. §22.3]].*

Property 8 evaluates double integrals over regions $D$ that are neither type I nor type II but can be cut into regions of type I or type II: integrate over each piece and add. This is what [[§116 Double Integrals Over General Regions#^ex-116-2|Examples §116.2]] and [[§116 Double Integrals Over General Regions#^ex-116-3|§116.3]] do when they describe a region as type I in two pieces.

> [!theorem] Theorem §139.5: Area as a Double Integral
> If we integrate the constant function $f(x, y) = 1$ over a region $D$, we get the area of $D$:
>
> $$
> \iint_D 1\,dA = A(D) . \qquad (9)
> $$
>
> *Stewart: 15.2, Property 9*

^thm-116-5

> [!remark] Remark: Why It Works
> A solid cylinder whose base is $D$ and whose height is $1$ has volume $A(D) \cdot 1 = A(D)$. By [[§115 Double Integrals Over Rectangles#^thm-115-2|Theorem §115.2]] (and [[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]]) its volume is also $\iint_D 1\,dA$.

^rem-116-3

> [!proof]+ Proof
> *Stewart gives only the cylinder argument above; here is a computation for the regions of this section.* If $D = \{a \le x \le b,\ g_1(x) \le y \le g_2(x)\}$ is of type I, then by [[§116 Double Integrals Over General Regions#^thm-116-1|Theorem §116.1]]
>
> $$
> \iint_D 1\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} 1\,dy\,dx = \int_a^b \big[ g_2(x) - g_1(x) \big]\,dx ,
> $$
>
> which is the area between the curves $y = g_1(x)$ and $y = g_2(x)$ ([[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]]; for type II, [[§45 Areas Between Curves#^thm-45-3|Theorem §45.3]]). A type II region is the same with $x$ and $y$ exchanged, and a finite union of non-overlapping regions of these types follows by Property 8.

^pf-116-5

*Uses:* [[§116 Double Integrals Over General Regions#^thm-116-1|§116.1]], [[§116 Double Integrals Over General Regions#^thm-116-2|§116.2]], [[§116 Double Integrals Over General Regions#^thm-116-4|§116.4]], [[§45 Areas Between Curves#^thm-45-1|§45.1]], [[§45 Areas Between Curves#^thm-45-3|§45.3]]

> [!theorem] Theorem §139.6: Bounds for a Double Integral
> If $m \le f(x, y) \le M$ for all $(x, y)$ in $D$, then
>
> $$
> m \cdot A(D) \le \iint_D f(x, y)\,dA \le M \cdot A(D) . \qquad (10)
> $$
>
> *Stewart: 15.2, Property 10*

^thm-116-6

> [!proof]+ Proof
> *Stewart leaves this as Exercise 73, combining Properties 6, 7 and 9.* Since $m \le f(x, y)$ on $D$, Property 7 (with the constant function $m$), then Property 6 and Property 9 give
>
> $$
> \iint_D f(x, y)\,dA \ge \iint_D m\,dA = m \iint_D 1\,dA = m \cdot A(D) .
> $$
>
> The upper bound is the same argument with $f(x, y) \le M$.

^pf-116-6

*Uses:* [[§116 Double Integrals Over General Regions#^thm-116-3|§116.3]], [[§116 Double Integrals Over General Regions#^thm-116-5|§116.5]]

For $m > 0$ the bounds compare the volume under the graph of $f$ with the volumes of the two cylinders with base $D$ and heights $m$ and $M$ (compare the single-integral version, Property 8 in [[§40 Properties of the Definite Integral#^thm-40-3|Theorem §40.3]]).

> [!remark] Remark: Estimating a Double Integral
> Stewart's Example 15.2.6: use Property 10 to estimate $\displaystyle\iint_D e^{\sin x \cos y}\,dA$, where $D$ is the disk with center the origin and radius $2$.
>
> Since $-1 \le \sin x \le 1$ and $-1 \le \cos y \le 1$, we have $-1 \le \sin x \cos y \le 1$, and because the natural exponential function is increasing,
>
> $$
> e^{-1} \le e^{\sin x \cos y} \le e^1 = e .
> $$
>
> With $m = e^{-1} = 1/e$, $M = e$ and $A(D) = \pi(2)^2 = 4\pi$, [[§116 Double Integrals Over General Regions#^thm-116-6|Theorem §116.6]] gives
>
> $$
> \frac{4\pi}{e} \le \iint_D e^{\sin x \cos y}\,dA \le 4\pi e .
> $$

^rem-116-4
