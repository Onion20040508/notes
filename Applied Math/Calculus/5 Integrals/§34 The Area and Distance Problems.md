---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 34
stewart: "5.1"
aliases: ["Stewart 5.1"]
tags: [calculus]
---
← [[§33 Antiderivatives]] · ↑ [[· 5 Integrals]] · [[§35 The Definite Integral]] →

*Stewart, Section 5.1.*

What is the area of a region with a curved side, and how far does a car travel when its speed keeps changing? Both questions have the same answer: cut the interval into $n$ small pieces, pretend the function is constant on each piece, add up the $n$ products, and let $n \to \infty$. This section works through that procedure by hand for $y = x^2$, where the limit can be computed exactly, and uses it to *define* the area under a curve. The same limit of sums becomes the definite integral in [[§35 The Definite Integral|§35]], and the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus|§36]]) will evaluate it without any sums at all.

## The Area Problem

The **area problem**: find the area of the region $S$ under the graph of a continuous function $f \ge 0$ from $a$ to $b$, that is,

$$
S = \{(x, y) \mid a \le x \le b,\ 0 \le y \le f(x)\} .
$$

For regions with straight sides, area is easy: a rectangle has area length times width, a triangle half base times height, and a polygon is cut into triangles. A curved side needs a new idea, the same one used for tangent lines in [[§12 Derivatives and Rates of Change|§12]]: approximate (there by secant lines, here by rectangles) and take the limit of the approximations.

> [!example] Example §34.1: Estimating the Area Under a Parabola
> Use rectangles to estimate the area $A$ under the parabola $y = x^2$ from $0$ to $1$.
>
> Since $S$ lies inside the unit square, $0 < A < 1$. To do better, divide $S$ into four strips by the lines $x = \frac14, \frac12, \frac34$, and replace each strip by a rectangle of width $\frac14$.
>
> **Right endpoints.** Take the height of each rectangle to be the value of $f(x) = x^2$ at the right endpoint of its subinterval $\big[0, \tfrac14\big], \big[\tfrac14, \tfrac12\big], \big[\tfrac12, \tfrac34\big], \big[\tfrac34, 1\big]$:
>
> $$
> R_4 = \tfrac14 \big(\tfrac14\big)^2 + \tfrac14 \big(\tfrac12\big)^2 + \tfrac14 \big(\tfrac34\big)^2 + \tfrac14 \cdot 1^2 = \frac14 \cdot \frac{1 + 4 + 9 + 16}{16} = \frac{15}{32} = 0.46875 .
> $$
>
> Since $x^2$ is increasing on $[0, 1]$, each rectangle sticks out above its strip, so $A < 0.46875$.
>
> **Left endpoints.** With the heights taken at the left endpoints, each rectangle lies inside its strip (the first has height $0$ and collapses):
>
> $$
> L_4 = \tfrac14 \cdot 0^2 + \tfrac14 \big(\tfrac14\big)^2 + \tfrac14 \big(\tfrac12\big)^2 + \tfrac14 \big(\tfrac34\big)^2 = \frac14 \cdot \frac{0 + 1 + 4 + 9}{16} = \frac{7}{32} = 0.21875 .
> $$
>
> So $0.21875 < A < 0.46875$.
>
> **Eight strips.** With width $\frac18$, the left heights are $\big(\frac{k}{8}\big)^2$ for $k = 0, \ldots, 7$ and the right heights are $\big(\frac{k}{8}\big)^2$ for $k = 1, \ldots, 8$. Since $0 + 1 + 4 + 9 + 16 + 25 + 36 + 49 = 140$,
>
> $$
> L_8 = \frac18 \cdot \frac{140}{64} = \frac{140}{512} = 0.2734375, \qquad R_8 = \frac18 \cdot \frac{140 + 64}{64} = \frac{204}{512} = 0.3984375 ,
> $$
>
> so $0.2734375 < A < 0.3984375$.
>
> With a computer, $n = 50$ strips give $0.3234 < A < 0.3434$, and $n = 1000$ give $0.3328335 < A < 0.3338335$. The average of the last two, $0.3333335$, suggests $A = \frac13$.
>
> *Stewart: Example 5.1.1*

^ex-34-1

![[m233-34-1.svg]]
*The parabola with $n = 8$: the left-endpoint rectangles (blue) lie under the curve and the right-endpoint rectangles (blue plus red) cover it, so $L_8 < A < R_8$. Slid sideways, the red excess pieces stack into one column of width $\frac18$ and height $f(1) - f(0) = 1$. In general $R_n - L_n = \frac1n$, so the two estimates squeeze down on $A$ as $n \to \infty$.*

To compute the limit we need the sum of the first $n$ squares,

$$
1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n + 1)(2n + 1)}{6} , \qquad (1)
$$

Stewart's Formula 1, proved in Appendix E ([[§120 Sigma Notation|§120]], Example 5).

> [!example] Example §34.2: The Exact Area Under the Parabola
> For the region $S$ of Example §34.1, show that $\lim_{n \to \infty} R_n = \frac13$.
>
> Divide $[0, 1]$ into $n$ subintervals of width $\frac1n$. The right endpoints are $\frac1n, \frac2n, \ldots, \frac{n}{n}$, so
>
> $$
> \begin{aligned}
> R_n &= \frac1n \Big(\frac1n\Big)^2 + \frac1n \Big(\frac2n\Big)^2 + \cdots + \frac1n \Big(\frac{n}{n}\Big)^2
> = \frac{1}{n^3} \big(1^2 + 2^2 + \cdots + n^2\big) \\
> &= \frac{1}{n^3} \cdot \frac{n(n + 1)(2n + 1)}{6} = \frac{(n + 1)(2n + 1)}{6n^2}
> \end{aligned}
> $$
>
> by Formula (1). Therefore
>
> $$
> \lim_{n \to \infty} R_n = \lim_{n \to \infty} \frac16 \Big(\frac{n + 1}{n}\Big)\Big(\frac{2n + 1}{n}\Big) = \lim_{n \to \infty} \frac16 \Big(1 + \frac1n\Big)\Big(2 + \frac1n\Big) = \frac16 \cdot 1 \cdot 2 = \frac13 .
> $$
>
> Here $n$ runs through the positive integers only: this is the limit of a sequence ([[§69 Sequences|§69]]), computed like a limit at infinity ([[§11 Limits at Infinity; Horizontal Asymptotes|§11]]) using $\lim_{n \to \infty} 1/n = 0$.
>
> **Left endpoints.** Stewart states that $L_n \to \frac13$ as well. Indeed $L_n$ and $R_n$ use the same heights except for the first and the last: $L_n$ has $\frac1n f(0)$ where $R_n$ has $\frac1n f(1)$. So
>
> $$
> R_n - L_n = \frac1n \big(f(1) - f(0)\big) = \frac1n \to 0, \qquad\text{hence}\qquad \lim_{n \to \infty} L_n = \lim_{n \to \infty} R_n - \lim_{n \to \infty} \frac1n = \frac13 .
> $$
>
> So the area, defined below as this limit, is $A = \frac13$.
>
> *Stewart: Example 5.1.2*

^ex-34-2

Now the same procedure for the general region $S$. Divide $[a, b]$ into $n$ subintervals of equal width

$$
\Delta x = \frac{b - a}{n},
$$

namely $[x_0, x_1], [x_1, x_2], \ldots, [x_{n-1}, x_n]$ with $x_0 = a$, $x_n = b$, and in general $x_i = a + i\,\Delta x$. Approximate the $i$th strip by the rectangle of width $\Delta x$ and height $f(x_i)$, the value of $f$ at the right endpoint. The rectangles have total area

$$
R_n = f(x_1)\,\Delta x + f(x_2)\,\Delta x + \cdots + f(x_n)\,\Delta x ,
$$

and the approximation improves as $n \to \infty$.

> [!definition] Definition §34.1: Area Under a Curve
> The **area** $A$ of the region $S$ that lies under the graph of the continuous function $f \ge 0$ on $[a, b]$ is the limit of the sum of the areas of approximating rectangles:
>
> $$
> A = \lim_{n \to \infty} R_n = \lim_{n \to \infty} \big[ f(x_1)\,\Delta x + f(x_2)\,\Delta x + \cdots + f(x_n)\,\Delta x \big] ,
> $$
>
> where $\Delta x = (b - a)/n$ and $x_i = a + i\,\Delta x$.
>
> *Stewart: 5.1, Definition 2*

^def-34-1

> [!definition] Definition §34.2: Sample Points; Lower and Upper Sums
> Instead of an endpoint, the height of the $i$th rectangle may be the value of $f$ at **any** number $x_i^*$ in the $i$th subinterval $[x_{i-1}, x_i]$. The numbers $x_1^*, x_2^*, \ldots, x_n^*$ are called **sample points**.
>
> Choosing each $x_i^*$ so that $f(x_i^*)$ is the minimum value of $f$ on $[x_{i-1}, x_i]$ gives a **lower sum**; choosing the maximum value gives an **upper sum**. (These extreme values exist by the Extreme Value Theorem, [[§25 Maximum and Minimum Values|§25]], since $f$ is continuous on the closed subinterval.)
>
> *Stewart: 5.1 (text and Note)*

^def-34-2

In **sigma notation** ([[§120 Sigma Notation|§120]]) a sum with many terms is written compactly, for instance

$$
\sum_{i=1}^{n} f(x_i)\,\Delta x = f(x_1)\,\Delta x + f(x_2)\,\Delta x + \cdots + f(x_n)\,\Delta x ,
$$

where $i$ is the index of summation, running from the value below $\Sigma$ to the value above it. Formula (1) reads $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$.

> [!theorem] Theorem §34.1: The Area as a Limit of Any Riemann Sums
> Let $f \ge 0$ be continuous on $[a, b]$, and use the notation of Definitions §34.1 and §34.2.
> 1. The limit $A = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i)\,\Delta x$ in Definition §34.1 exists.
> 2. Left endpoints give the same value:
>
> $$
> A = \lim_{n \to \infty} L_n = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_{i-1})\,\Delta x = \lim_{n \to \infty} \big[ f(x_0)\,\Delta x + f(x_1)\,\Delta x + \cdots + f(x_{n-1})\,\Delta x \big] .
> $$
>
> 3. So do arbitrary sample points:
>
> $$
> A = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x = \lim_{n \to \infty} \big[ f(x_1^*)\,\Delta x + f(x_2^*)\,\Delta x + \cdots + f(x_n^*)\,\Delta x \big] .
> $$
>
> 4. Equivalently, $A$ is the unique number that is smaller than all the upper sums and bigger than all the lower sums.
>
> *Stewart: 5.1, Equations 3 and 4 and Note*

^thm-34-1

*Stewart omits the proof ("it can be proved"; "it can be shown"). It rests on the uniform continuity of $f$ on $[a, b]$: see [[§32 The Definition of the Riemann Integral#^thm-32-7|451 Thm. §32.7]] for the existence of the limit, and [[§32 The Definition of the Riemann Integral#^thm-32-6|451 Thm. §32.6]] for the equivalence of the limit of sums with the upper/lower-sum description in part 4.*

> [!remark]- Connections
> - Rigorous treatment: the upper and lower sums for arbitrary (not necessarily equal) subdivisions are [[§32 The Definition of the Riemann Integral#^def-32-1|451 Def. §32.1]], part 4 is the Darboux integral [[§32 The Definition of the Riemann Integral#^def-32-2|451 Def. §32.2]], and the sums with sample points are the Riemann sums of [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]]. The computation of Example §34.2 is done there with upper and lower sums for $f(x) = x$ ([[§32 The Definition of the Riemann Integral#^ex-32-1|451 Ex. §32.1]]).

In Examples §34.1 and §34.2 the function $x^2$ is increasing on $[0, 1]$, so the left-endpoint sums are the lower sums and the right-endpoint sums the upper sums, and $A = \frac13$ is trapped between all $L_n$ and all $R_n$.

> [!example] Example §34.3: The Area Under an Exponential Curve
> Let $A$ be the area of the region under the graph of $f(x) = e^{-x}$ between $x = 0$ and $x = 2$.
>
> **(a)** Using right endpoints, find an expression for $A$ as a limit. Do not evaluate the limit.
>
> **(b)** Estimate the area by taking the sample points to be midpoints, with four and then ten subintervals.
>
> **(a)** Here $a = 0$, $b = 2$, so $\Delta x = \frac{2 - 0}{n} = \frac2n$ and $x_i = \frac{2i}{n}$. By Definition §34.1,
>
> $$
> A = \lim_{n \to \infty} R_n = \lim_{n \to \infty} \big[ e^{-x_1}\,\Delta x + \cdots + e^{-x_n}\,\Delta x \big] = \lim_{n \to \infty} \frac2n \big( e^{-2/n} + e^{-4/n} + \cdots + e^{-2n/n} \big) = \lim_{n \to \infty} \frac2n \sum_{i=1}^{n} e^{-2i/n} .
> $$
>
> This limit is hard to evaluate by hand. (It is a geometric sum, and a computer algebra system finds it. In [[§36 The Fundamental Theorem of Calculus|§36]] the Fundamental Theorem gives $A = 1 - e^{-2} \approx 0.8647$ at once.)
>
> **(b)** With $n = 4$, $\Delta x = 0.5$, the subintervals are $[0, 0.5], [0.5, 1], [1, 1.5], [1.5, 2]$, with midpoints $x_1^* = 0.25$, $x_2^* = 0.75$, $x_3^* = 1.25$, $x_4^* = 1.75$. The **midpoint sum** is
>
> $$
> M_4 = \sum_{i=1}^{4} f(x_i^*)\,\Delta x = 0.5 \big( e^{-0.25} + e^{-0.75} + e^{-1.25} + e^{-1.75} \big) \approx 0.8557 .
> $$
>
> With $n = 10$, $\Delta x = 0.2$, the subintervals are $[0, 0.2], [0.2, 0.4], \ldots, [1.8, 2]$, with midpoints $0.1, 0.3, 0.5, \ldots, 1.9$, and
>
> $$
> A \approx M_{10} = 0.2 \big( e^{-0.1} + e^{-0.3} + e^{-0.5} + \cdots + e^{-1.9} \big) \approx 0.8632 .
> $$
>
> The second estimate is the better one: compared with the exact value $0.8647$, the errors are about $0.009$ and $0.0014$.
>
> *Stewart: Example 5.1.3*

^ex-34-3

## The Distance Problem

The **distance problem** is the inverse of the velocity problem of [[§6 The Tangent and Velocity Problems|§6]]: find the distance traveled by an object during a time interval when its velocity is known at all times. If the velocity is constant, distance $=$ velocity $\times$ time. If not, we approximate as for areas.

> [!example] Example §34.4: Distance from Speedometer Readings
> A car's odometer is broken. Speedometer readings every five seconds over a 30-second interval are:
>
> | Time (s) | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
> |---|---|---|---|---|---|---|---|
> | Velocity (mi/h) | 17 | 21 | 24 | 29 | 32 | 31 | 28 |
>
> Estimate the distance driven.
>
> **Units.** Convert to ft/s with $1$ mi/h $= 5280/3600$ ft/s, rounding to the nearest integer (for example $17 \cdot \frac{5280}{3600} \approx 24.93$):
>
> | Time (s) | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
> |---|---|---|---|---|---|---|---|
> | Velocity (ft/s) | 25 | 31 | 35 | 43 | 47 | 45 | 41 |
>
> **Velocity at the start of each interval.** During the first five seconds the velocity hardly changes, so take it to be $25$ ft/s throughout: the car travels about $25 \times 5 = 125$ ft. During the next five seconds, about $31 \times 5 = 155$ ft. Adding over all six intervals,
>
> $$
> (25 + 31 + 35 + 43 + 47 + 45) \times 5 = 226 \times 5 = 1130 \text{ ft} .
> $$
>
> **Velocity at the end of each interval.**
>
> $$
> (31 + 35 + 43 + 47 + 45 + 41) \times 5 = 242 \times 5 = 1210 \text{ ft} .
> $$
>
> **Interpretation.** On a graph of velocity against time, $25 \times 5$ is the area of a rectangle of height $25$ (ft/s) and width $5$ (s). So $1130$ is the left-endpoint sum $L_6$ and $1210$ the right-endpoint sum $R_6$ for the velocity function. More frequent readings give more and thinner rectangles, which approach the area under the velocity curve. So the distance traveled is the area under the velocity graph.
>
> *Stewart: Example 5.1.4*

^ex-34-4

In general, let an object move with velocity $v = f(t) \ge 0$, $a \le t \le b$ (so it always moves forward). Read the velocity at equally spaced times $t_0 (= a), t_1, \ldots, t_n (= b)$, $\Delta t = (b - a)/n$. On the $i$th time interval the object travels approximately $f(t_{i-1})\,\Delta t$, or approximately $f(t_i)\,\Delta t$. The more often we measure, the better the estimate, so the exact distance should be

$$
d = \lim_{n \to \infty} \sum_{i=1}^{n} f(t_{i-1})\,\Delta t = \lim_{n \to \infty} \sum_{i=1}^{n} f(t_i)\,\Delta t . \qquad (5)
$$

This is Stewart's Equation 5, justified in [[§37 Indefinite Integrals and the Net Change Theorem|§37]] (the Net Change Theorem). It has the form of Definition §34.1 and Theorem §34.1, part 2: **distance traveled is the area under the velocity graph.**

> [!remark] Remark: Many Quantities Are Areas
> Equation (5) is the first of many quantities computed as a limit of sums $\sum f(x_i^*)\,\Delta x$, and hence as an area under a curve: the work done by a variable force ([[§42 Work|§42]]), volumes ([[§40 Volumes|§40]]), the cardiac output of the heart ([[§55 Applications to Economics and Biology|§55]]), and others in Chapters 6 and 8. So an area computed in this chapter can be read in many practical ways.

^rem-34-1
