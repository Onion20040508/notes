---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 5
stewart: "1.5"
aliases: ["Stewart 1.5"]
tags: [calculus]
---
← [[§4 Exponential Functions]] · ↑ [[· 1 Functions and Models]] · [[§6 The Tangent and Velocity Problems]] →

*Stewart, Section 1.5.*

A function that never takes the same value twice can be run backwards: its inverse sends each output back to the one input that produced it. This section says when an inverse exists (one-to-one functions, recognized by the Horizontal Line Test), how to compute it, and how its graph is obtained (reflect in the line $y = x$). Applied to the exponential functions of [[§4 Exponential Functions|§4]] it gives the logarithms, whose laws are the Laws of Exponents read backwards; the natural logarithm $\ln$ is the inverse of $e^x$. Applied to the trigonometric functions, restricted to intervals on which they are one-to-one, it gives $\sin^{-1}$, $\cos^{-1}$ and $\tan^{-1}$.

## Inverse Functions

If the size of a bacteria population is a function of time, $N = f(t)$, one can also ask for the time at which the population reaches a given size: $t$ as a function of $N$. This is the inverse function $t = f^{-1}(N)$. For instance, if $f(6) = 550$, then $f^{-1}(550) = 6$. Not every function has an inverse: if two inputs give the same output, that output cannot be sent back to a single input.

> [!definition] Definition §5.1: One-to-One Function
> A function $f$ is **one-to-one** if it never takes on the same value twice; that is,
>
> $$
> f(x_1) \ne f(x_2) \qquad \text{whenever } x_1 \ne x_2 .
> $$
>
> In terms of inputs and outputs: each output corresponds to only one input.
>
> *Stewart: 1.5, Definition 1*

^def-5-1

> [!remark]- Connections
> - Rigorous version: an injection, [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]], with the contrapositive form $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$ that is usually more convenient in proofs. The horizontal-line description is [[§9 Injections, Surjections and Bijections#^ex-9-11|250 Ex. §9.11]].

> [!theorem] Theorem §5.1: Horizontal Line Test
> A function is one-to-one if and only if no horizontal line intersects its graph more than once.
>
> *Stewart: 1.5, Horizontal Line Test*

^thm-5-1

> [!proof]+ Proof
> The horizontal line $y = c$ meets the graph of $f$ at the points $(x, c)$ with $x$ in the domain of $f$ and $f(x) = c$.
>
> If $f$ is not one-to-one, there are $x_1 \ne x_2$ with $f(x_1) = f(x_2)$. Call this common value $c$. Then the line $y = c$ meets the graph at the two different points $(x_1, c)$ and $(x_2, c)$.
>
> Conversely, if some line $y = c$ meets the graph at two different points, these points have the same second coordinate $c$, so they differ in the first: they are $(x_1, c)$ and $(x_2, c)$ with $x_1 \ne x_2$ and $f(x_1) = c = f(x_2)$. So $f$ is not one-to-one.
>
> Both directions together (in contrapositive form) give the test.

^pf-5-1

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-1|Def. §5.1]]

> [!example] Example §5.1: Is It One-to-One?
> **(a)** Is $f(x) = x^3$ one-to-one?
>
> *By the definition.* Two different numbers cannot have the same cube. In detail: suppose $x_1^3 = x_2^3$. Then
>
> $$
> 0 = x_1^3 - x_2^3 = (x_1 - x_2)(x_1^2 + x_1 x_2 + x_2^2), \qquad x_1^2 + x_1 x_2 + x_2^2 = \Big(x_1 + \frac{x_2}{2}\Big)^2 + \frac34 x_2^2 .
> $$
>
> The second factor is a sum of two squares, so it is $0$ only if $x_2 = 0$ and then $x_1 = 0$. Either way $x_1 = x_2$. So $f$ is one-to-one (Definition §5.1, in contrapositive form).
>
> *By the graph.* The graph of $y = x^3$ rises from left to right (flattening at the origin), and every horizontal line meets it exactly once. By Theorem §5.1, $f$ is one-to-one.
>
> **(b)** Is $g(x) = x^2$ one-to-one?
>
> No: $g(1) = 1 = g(-1)$, so $1$ and $-1$ have the same output. On the graph, the horizontal line $y = 1$ meets the parabola at $(-1, 1)$ and $(1, 1)$, and so does every line $y = c$ with $c > 0$.
>
> *Stewart: Examples 1.5.1 and 1.5.2*

^ex-5-1

One-to-one functions are important because they are precisely the functions that have inverse functions.

> [!definition] Definition §5.2: Inverse Function
> Let $f$ be a one-to-one function with domain $A$ and range $B$. Then its **inverse function** $f^{-1}$ has domain $B$ and range $A$ and is defined by
>
> $$
> f^{-1}(y) = x \quad\Longleftrightarrow\quad f(x) = y
> $$
>
> for any $y$ in $B$. So
>
> $$
> \text{domain of } f^{-1} = \text{range of } f, \qquad \text{range of } f^{-1} = \text{domain of } f .
> $$
>
> If $f$ maps $x$ to $y$, then $f^{-1}$ maps $y$ back to $x$. Every $y \in B$ is a value $f(x)$, and since $f$ is one-to-one there is only one such $x$; if $f$ were not one-to-one, $f^{-1}(y)$ would not be uniquely defined.
>
> Since $x$ is traditionally the independent variable, one usually reverses the roles of $x$ and $y$ and writes the definition as
>
> $$
> f^{-1}(x) = y \quad\Longleftrightarrow\quad f(y) = x . \qquad (3)
> $$
>
> *Stewart: 1.5, Definition 2 and Equation 3*

^def-5-2

> [!remark] Remark: Reading the Definition
> - **The $-1$ is not an exponent.** $f^{-1}(x)$ does *not* mean $\dfrac{1}{f(x)}$; the reciprocal would be written $[f(x)]^{-1}$.
> - **Tables reverse.** If $f$ is one-to-one with $f(1) = 5$, $f(3) = 7$ and $f(8) = -10$, then $f^{-1}(7) = 3$, $f^{-1}(5) = 1$ and $f^{-1}(-10) = 8$: read the arrow diagram of $f$ backwards (Stewart, Example 1.5.3).
> - **An example.** The inverse of $f(x) = x^3$ is $f^{-1}(x) = x^{1/3}$: if $y = x^3$, then $f^{-1}(y) = (x^3)^{1/3} = x$.

^rem-5-1

> [!theorem] Theorem §5.2: Cancellation Equations
> Let $f$ be one-to-one with domain $A$ and range $B$. Then
>
> $$
> f^{-1}(f(x)) = x \quad \text{for every } x \text{ in } A, \qquad\qquad f(f^{-1}(x)) = x \quad \text{for every } x \text{ in } B .
> $$
>
> The first equation says that $f^{-1}$ undoes what $f$ does; the second says that $f$ undoes what $f^{-1}$ does. For $f(x) = x^3$: $(x^3)^{1/3} = x$ and $(x^{1/3})^3 = x$, so the cube and the cube root cancel each other.
>
> *Stewart: 1.5, Equation 4*

^thm-5-2

> [!proof]+ Proof
> Let $x \in A$ and put $y = f(x)$, which lies in the range $B$. Since $f(x) = y$, Definition §5.2 gives $f^{-1}(y) = x$, that is, $f^{-1}(f(x)) = x$.
>
> Let $x \in B$ and put $y = f^{-1}(x)$. By the form (3) of the definition, $f^{-1}(x) = y$ means $f(y) = x$, that is, $f(f^{-1}(x)) = x$.

^pf-5-2

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§9 Injections, Surjections and Bijections#^def-9-3|250 Def. §9.3]] defines the inverse by the same "$y = f(x) \iff x = g(y)$", and [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]] shows that an inverse exists exactly for bijections. Stewart's $f$ is a bijection from $A$ onto its range $B$: one-to-one by assumption, onto because $B$ is the range.
> - The cancellation equations characterize the inverse: $g \circ f = I_A$ and $f \circ g = I_B$ hold exactly when $g = f^{-1}$, [[§9 Injections, Surjections and Bijections#^prop-9-3|250 Prop. §9.3]].

> [!remark] Remark: Method — How to Find the Inverse Function of a One-to-One Function f
> 1. Write $y = f(x)$.
> 2. Solve this equation for $x$ in terms of $y$ (if possible). By Definition §5.2 the result is $x = f^{-1}(y)$.
> 3. To express $f^{-1}$ as a function of $x$, interchange $x$ and $y$. The resulting equation is $y = f^{-1}(x)$.
>
> Check the answer with the cancellation equations (Theorem §5.2), and record the domain of $f^{-1}$, which is the range of $f$ (it may be smaller than the natural domain of the formula, as in Example §5.2(b)).
>
> *Stewart: 1.5, Box 5*

^rem-5-2

Interchanging $x$ and $y$ also gives the graph of $f^{-1}$ from the graph of $f$.

> [!theorem] Theorem §5.3: The Graph of the Inverse Function
> The graph of $f^{-1}$ is obtained by reflecting the graph of $f$ about the line $y = x$.
>
> *Stewart: 1.5 (text)*

^thm-5-3

> [!proof]+ Proof
> **Points are swapped.** By Definition §5.2, $f(a) = b$ if and only if $f^{-1}(b) = a$. So $(a, b)$ is on the graph of $f$ if and only if $(b, a)$ is on the graph of $f^{-1}$.
>
> **Swapping is reflecting.** The reflection of $(a, b)$ about the line $y = x$ is $(b, a)$. If $a = b$ the point lies on the line and is its own mirror image. If $a \ne b$, the segment from $(a, b)$ to $(b, a)$ has slope $\dfrac{a - b}{b - a} = -1$, so it is perpendicular to the line $y = x$ (slope $1$), and its midpoint $\big(\frac{a + b}{2}, \frac{a + b}{2}\big)$ lies on that line. So $y = x$ is the perpendicular bisector of the segment, which is what it means for $(b, a)$ to be the mirror image of $(a, b)$.
>
> Hence the graph of $f^{-1}$ consists exactly of the mirror images of the points of the graph of $f$.

^pf-5-3

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]]

![[m233-5-1.svg]]
*The graph of $y = \ln x$ (red) is the mirror image of the graph of $y = e^x$ (blue) in the line $y = x$ (green). A point $(a, b)$ on the graph of $e^x$ (here $a = 0.8$, $b = e^{0.8} \approx 2.23$) corresponds to the point $(b, a)$ on the graph of $\ln x$; the segment joining them is perpendicular to $y = x$ and is bisected by it. The intercept $(0, 1)$ of $e^x$ becomes the intercept $(1, 0)$ of $\ln x$, and the horizontal asymptote $y = 0$ of $e^x$ becomes the vertical asymptote $x = 0$ of $\ln x$.*

> [!example] Example §5.2: Finding and Graphing an Inverse
> **(a)** Find the inverse function of $f(x) = x^3 + 2$.
>
> Following the method (Remark above): write $y = x^3 + 2$; solve for $x$:
>
> $$
> x^3 = y - 2, \qquad x = \sqrt[3]{y - 2} ;
> $$
>
> interchange $x$ and $y$: $y = \sqrt[3]{x - 2}$. So $f^{-1}(x) = \sqrt[3]{x - 2}$. Check: $f(f^{-1}(x)) = (x - 2) + 2 = x$ and $f^{-1}(f(x)) = \sqrt[3]{x^3} = x$. In words, $f$ is "cube, then add $2$" and $f^{-1}$ is "subtract $2$, then take the cube root": the steps are undone in reverse order.
>
> **(b)** Sketch the graphs of $f(x) = \sqrt{-1 - x}$ and its inverse function on the same axes.
>
> $f$ is defined for $-1 - x \ge 0$, so its domain is $(-\infty, -1]$, and its range is $[0, \infty)$. Squaring $y = \sqrt{-1 - x}$ gives $y^2 = -1 - x$, that is, $x = -y^2 - 1$: the graph of $f$ is the top half ($y \ge 0$) of this parabola, which opens to the left and has its vertex at $(-1, 0)$. Reflecting about $y = x$ (Theorem §5.3) gives the graph of $f^{-1}$.
>
> *Check by formula.* Solving $y = \sqrt{-1 - x}$ for $x$ gives $x = -y^2 - 1$ with $y \ge 0$; interchanging, $f^{-1}(x) = -x^2 - 1$ for $x \ge 0$. The restriction $x \ge 0$ is essential: the domain of $f^{-1}$ is the range $[0, \infty)$ of $f$. So the graph of $f^{-1}$ is the right half of the parabola $y = -x^2 - 1$, starting at $(0, -1)$, the mirror image of the endpoint $(-1, 0)$ of the graph of $f$.
>
> *Stewart: Examples 1.5.4 and 1.5.5*

^ex-5-2

## Logarithmic Functions

If $b > 0$ and $b \ne 1$, the exponential function $f(x) = b^x$ is either increasing or decreasing ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]), so no horizontal line meets its graph twice, and it is one-to-one by the Horizontal Line Test (Theorem §5.1). It therefore has an inverse function.

> [!definition] Definition §5.3: Logarithmic Function with Base b
> Let $b > 0$, $b \ne 1$. The inverse of the exponential function $f(x) = b^x$ is the **logarithmic function with base $b$**, denoted $\log_b$. By the form (3) of Definition §5.2,
>
> $$
> \log_b x = y \quad\Longleftrightarrow\quad b^y = x . \qquad (6)
> $$
>
> So for $x > 0$, $\log_b x$ is *the exponent to which the base $b$ must be raised to give $x$*. For example, $\log_{10} 0.001 = -3$ because $10^{-3} = 0.001$.
>
> *Stewart: 1.5, Equation 6*

^def-5-3

*Rigorous construction: [[§121 The Logarithm Defined as an Integral#^def-121-6|Definition §121.6]] (Appendix G).*

> [!theorem] Theorem §5.4: Properties of the Logarithmic Function
> Let $b > 0$, $b \ne 1$.
> 1. **Cancellation equations:**
>
> $$
> \log_b(b^x) = x \quad \text{for every } x \in \mathbb{R}, \qquad\qquad b^{\log_b x} = x \quad \text{for every } x > 0 . \qquad (7)
> $$
>
> 2. $\log_b$ has domain $(0, \infty)$ and range $\mathbb{R}$, and its graph is the reflection of the graph of $y = b^x$ about the line $y = x$.
> 3. $\log_b 1 = 0$, so every graph $y = \log_b x$ passes through $(1, 0)$.
> 4. If $b > 1$, then $\log_b$ is increasing. (It increases very slowly for $x > 1$, reflecting the very rapid increase of $b^x$ for $x > 0$.)
>
> *Stewart: 1.5, Equation 7 and text*

^thm-5-4

> [!proof]+ Proof
> **1.** Theorem §5.2 for $f(x) = b^x$, whose domain is $\mathbb{R}$ and whose range is $(0, \infty)$ ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]).
>
> **2.** By Definition §5.2 the domain of $\log_b$ is the range $(0, \infty)$ of $b^x$, and its range is the domain $\mathbb{R}$ of $b^x$. The statement about graphs is Theorem §5.3.
>
> **3.** $b^0 = 1$, so $\log_b 1 = 0$ by (6).
>
> **4.** Let $b > 1$ and $0 < x_1 < x_2$. Suppose $\log_b x_1 \ge \log_b x_2$. Since $b^x$ is increasing for $b > 1$ ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]), $b^{\log_b x_1} \ge b^{\log_b x_2}$, and by (7) this says $x_1 \ge x_2$, a contradiction. Hence $\log_b x_1 < \log_b x_2$.

^pf-5-4

*Uses:* [[§5 Inverse Functions and Logarithms#^thm-5-2|§5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-3|§5.3]], [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]], [[§5 Inverse Functions and Logarithms#^def-5-3|Def. §5.3]], [[§4 Exponential Functions#^prop-4-2|§4.2]]

> [!remark]- Connections
> - The logarithm is continuous as the inverse of a strictly monotone continuous function: [[§18 Properties of Continuous Functions#^thm-18-9|451 Thm. §18.9]], applied to $e^x$ in [[§18 Properties of Continuous Functions#^rem-18-8|451 Remark: Beyond closed intervals]] (Calculus version: [[§10 Continuity#^thm-10-5|Theorem §10.5]]).

The following properties of logarithms come from the Laws of Exponents of [[§4 Exponential Functions#^thm-4-1|Theorem §4.1]].

> [!theorem] Theorem §5.5: Laws of Logarithms
> Let $b > 0$, $b \ne 1$. If $x$ and $y$ are positive numbers, then
>
> $$
> 1.\ \log_b(xy) = \log_b x + \log_b y \qquad 2.\ \log_b\Big(\frac{x}{y}\Big) = \log_b x - \log_b y \qquad 3.\ \log_b(x^r) = r \log_b x \quad (r \text{ any real number}) .
> $$
>
> *Stewart: 1.5, Laws of Logarithms*

^thm-5-5

> [!proof]+ Proof
> *Stewart says only that these follow from the corresponding Laws of Exponents; here is the derivation.* Let $u = \log_b x$ and $v = \log_b y$. By (6), $b^u = x$ and $b^v = y$.
>
> 1. By Law 1 of Theorem §4.1, $xy = b^u b^v = b^{u + v}$. By (6), $\log_b(xy) = u + v = \log_b x + \log_b y$.
> 2. By Law 2, $\dfrac{x}{y} = \dfrac{b^u}{b^v} = b^{u - v}$, so $\log_b(x/y) = u - v$.
> 3. By Law 3, $x^r = (b^u)^r = b^{ur}$, so $\log_b(x^r) = ur = r \log_b x$.

^pf-5-5

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-3|Def. §5.3]], [[§4 Exponential Functions#^thm-4-1|§4.1]]

*Appendix G proves the laws for $\ln$ from the integral ([[§121 The Logarithm Defined as an Integral#^thm-121-2|Theorem §121.2]], with Law 3 for real $r$ in [[§121 The Logarithm Defined as an Integral#^thm-121-8|Theorem §121.8]]) and for $\log_b$ by change of base ([[§121 The Logarithm Defined as an Integral#^thm-121-11|Theorem §121.11]]).*

> [!example] Example §5.3: Expanding and Combining Logarithms
> **(a)** Evaluate $\log_2 80 - \log_2 5$. By Law 2,
>
> $$
> \log_2 80 - \log_2 5 = \log_2 \frac{80}{5} = \log_2 16 = 4 \qquad \text{because } 2^4 = 16 .
> $$
>
> **(b)** Expand $\ln \dfrac{x^2 \sqrt{x^2 + 2}}{3x + 1}$ (with $\ln = \log_e$, Definition §5.4 below). By Laws 1, 2 and 3,
>
> $$
> \ln \frac{x^2 \sqrt{x^2 + 2}}{3x + 1} = \ln x^2 + \ln \sqrt{x^2 + 2} - \ln(3x + 1) = 2 \ln x + \tfrac12 \ln(x^2 + 2) - \ln(3x + 1) .
> $$
>
> The laws need positive arguments, so this holds for $x > 0$. (The left side is also defined for $-\frac13 < x < 0$; there $\ln x^2 = 2 \ln|x|$.)
>
> **(c)** Express $\ln a + \frac12 \ln b$ as a single logarithm. By Laws 3 and 1,
>
> $$
> \ln a + \tfrac12 \ln b = \ln a + \ln b^{1/2} = \ln a + \ln \sqrt{b} = \ln\big(a \sqrt{b}\,\big) .
> $$
>
> *Stewart: Examples 1.5.6, 1.5.9 and 1.5.10*

^ex-5-3

## Natural Logarithms

The most convenient base for calculus is the number $e$ of [[§4 Exponential Functions#^def-4-4|Definition §4.4]], as Chapter 3 will show.

> [!definition] Definition §5.4: Natural Logarithm
> The logarithm with base $e$ is called the **natural logarithm** and has a special notation:
>
> $$
> \log_e x = \ln x .
> $$
>
> *Stewart: 1.5 (text)*

^def-5-4

*Appendix G develops the natural logarithm the other way round, rigorously: $\ln x = \int_1^x dt/t$ ([[§121 The Logarithm Defined as an Integral#^def-121-1|Definition §121.1]]), whose laws ([[§121 The Logarithm Defined as an Integral#^thm-121-2|Theorem §121.2]]) are proved by differentiation; $e$ is defined by $\ln e = 1$ ([[§121 The Logarithm Defined as an Integral#^def-121-2|Definition §121.2]]), $e^x$ as the inverse of $\ln$ ([[§121 The Logarithm Defined as an Integral#^def-121-3|Definition §121.3]]), and $\log_b$ as the inverse of $b^x$ ([[§121 The Logarithm Defined as an Integral#^def-121-6|Definition §121.6]]). This supplies the existence statements that Sections 1.4 and 1.5 take on trust.*

> [!remark]- Remark: Notation for Logarithms
> Most calculus and science textbooks, and calculators, write $\ln x$ for the natural logarithm and $\log x$ for the "common logarithm" $\log_{10} x$. In more advanced mathematical and scientific literature and in computer languages, $\log x$ usually denotes the natural logarithm (the analysis notes, 451, write $\log$ this way).

^rem-5-3

> [!theorem] Corollary §5.6: Defining Properties of the Natural Logarithm
> $$
> \ln x = y \quad\Longleftrightarrow\quad e^y = x , \qquad (8)
> $$
>
> $$
> \ln(e^x) = x \quad (x \in \mathbb{R}), \qquad\qquad e^{\ln x} = x \quad (x > 0) , \qquad (9)
> $$
>
> and in particular
>
> $$
> \ln e = 1 .
> $$
>
> *Stewart: 1.5, Equations 8 and 9*

^cor-5-6

> [!proof]+ Proof
> Equations (8) and (9) are (6) and (7) with $b = e$ (Definition §5.3 and Theorem §5.4). Setting $x = 1$ in the first equation of (9) gives $\ln e = \ln(e^1) = 1$.

^pf-5-6

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-3|Def. §5.3]], [[§5 Inverse Functions and Logarithms#^thm-5-4|§5.4]], [[§5 Inverse Functions and Logarithms#^def-5-4|Def. §5.4]]

*In Appendix G, (8) and (9) define $e^x$ as the inverse of the integral logarithm: [[§121 The Logarithm Defined as an Integral#^def-121-3|Definition §121.3]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Definition §121.4]].*

> [!theorem] Proposition §5.7: Powers in Exponential Form
> For $x > 0$ and every real number $r$,
>
> $$
> x^r = e^{r \ln x} . \qquad (10)
> $$
>
> So a power of $x$ can be written in exponential form, which will be useful in the chapters to come.
>
> *Stewart: 1.5, Equation 10*

^prop-5-7

> [!proof]+ Proof
> Since $x^r > 0$, the second equation of (9) applies to it, and then Law 3 of logarithms (Theorem §5.5) gives
>
> $$
> x^r = e^{\ln(x^r)} = e^{r \ln x} .
> $$

^pf-5-7

*Uses:* [[§5 Inverse Functions and Logarithms#^cor-5-6|§5.6]], [[§5 Inverse Functions and Logarithms#^thm-5-5|§5.5]]

> [!theorem] Theorem §5.8: Change of Base Formula
> For any positive number $b$ with $b \ne 1$,
>
> $$
> \log_b x = \frac{\ln x}{\ln b} \qquad (x > 0) .
> $$
>
> So logarithms with any base can be expressed through the natural logarithm; this is how a calculator computes (and graphs) $\log_b$.
>
> *Stewart: 1.5, Formula 11*

^thm-5-8

> [!proof]+ Proof
> Let $y = \log_b x$. By (6), $b^y = x$. Taking natural logarithms of both sides and using Law 3 of Theorem §5.5,
>
> $$
> \ln x = \ln(b^y) = y \ln b .
> $$
>
> Since $b \ne 1$ and $\ln$ is one-to-one with $\ln 1 = 0$ (Theorem §5.4), $\ln b \ne 0$. (Stewart divides without comment; this is why it is allowed.) Dividing by $\ln b$ gives $y = \dfrac{\ln x}{\ln b}$.

^pf-5-8

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-3|Def. §5.3]], [[§5 Inverse Functions and Logarithms#^thm-5-4|§5.4]], [[§5 Inverse Functions and Logarithms#^thm-5-5|§5.5]]

*The same formula from the integral definition of $\ln$ in Appendix G: [[§121 The Logarithm Defined as an Integral#^thm-121-11|Theorem §121.11]].*

> [!example] Example §5.4: Solving Equations with ln
> **(a)** Find $x$ if $\ln x = 5$.
>
> *From (8):* $\ln x = 5$ means $e^5 = x$. (If the notation is confusing, write $\log_e x = 5$; by the definition of logarithm, $e^5 = x$.)
>
> *By cancellation:* apply the exponential function to both sides, $e^{\ln x} = e^5$. The second equation of (9) says $e^{\ln x} = x$. Therefore $x = e^5$.
>
> **(b)** Solve $e^{5 - 3x} = 10$.
>
> Take natural logarithms of both sides and use the first equation of (9):
>
> $$
> \ln\big(e^{5 - 3x}\big) = \ln 10, \qquad 5 - 3x = \ln 10, \qquad 3x = 5 - \ln 10, \qquad x = \tfrac13 (5 - \ln 10) .
> $$
>
> Numerically, $\ln 10 \approx 2.302585$, so $x \approx \frac13 (2.697415) \approx 0.8991$.
>
> **(c)** Evaluate $\log_8 5$ to six decimal places. By the Change of Base Formula (Theorem §5.8),
>
> $$
> \log_8 5 = \frac{\ln 5}{\ln 8} \approx \frac{1.609438}{2.079442} \approx 0.773976 .
> $$
>
> *Stewart: Examples 1.5.7, 1.5.8 and 1.5.11*

^ex-5-4

### Graph and Growth of the Natural Logarithm

> [!theorem] Proposition §5.9: The Graph of the Natural Logarithm
> The graph of $y = \ln x$ is the reflection of the graph of $y = e^x$ about the line $y = x$. Like every logarithm with base greater than $1$, $\ln$ is an increasing function defined on $(0, \infty)$, and the $y$-axis is a vertical asymptote: the values of $\ln x$ become very large negative as $x$ approaches $0$. Although it increases, $\ln x$ grows *very* slowly for $x > 1$: more slowly than any positive power of $x$. For example, $y = \ln x$ and $y = \sqrt{x}$ grow at comparable rates at first, but eventually the root far surpasses the logarithm.
>
> *Stewart: 1.5 (text)*

^prop-5-9

*The first two statements are Theorem §5.4 with $b = e$ (since $e > 1$). The asymptote and the comparison with powers Stewart reads off graphs; they are proved as limits: $\lim_{x \to 0^+} \ln x = -\infty$ in [[§7 The Limit of a Function#^thm-7-1|Theorem §7.1]], and $\ln x / \sqrt{x} \to 0$ as $x \to \infty$, with l'Hospital's Rule, in [[§28 Indeterminate Forms and L'Hospital's Rule#^ex-28-1|Example §28.1]](c). Appendix G proves the shape and the limits of $\ln$ from the integral: [[§121 The Logarithm Defined as an Integral#^thm-121-3|Theorem §121.3]].*

The graphs of other logarithmic functions follow by the transformations of [[§3 New Functions from Old Functions#^thm-3-1|Theorem §3.1]]. For instance (Stewart, Example 1.5.12), $y = \ln(x - 2) - 1$ is $y = \ln x$ shifted $2$ units right and $1$ unit down: it has the vertical asymptote $x = 2$ and passes through $(3, -1)$, the image of $(1, 0)$.

## Inverse Trigonometric Functions

The trigonometric functions are not one-to-one (they are periodic), so they have no inverse functions. The difficulty is overcome by restricting their domains to intervals on which they are one-to-one and still take all their values.

> [!definition] Definition §5.5: Inverse Sine
> The sine function restricted to $[-\pi/2, \pi/2]$ is one-to-one and takes every value in $[-1, 1]$. Its inverse is the **inverse sine function** or **arcsine function**, denoted $\sin^{-1}$ or $\arcsin$:
>
> $$
> \sin^{-1} x = y \quad\Longleftrightarrow\quad \sin y = x \ \text{ and } \ -\frac{\pi}{2} \le y \le \frac{\pi}{2} .
> $$
>
> So for $-1 \le x \le 1$, $\sin^{-1} x$ is *the number between $-\pi/2$ and $\pi/2$ whose sine is $x$*. As with $f^{-1}$, the $-1$ is not an exponent: $\sin^{-1} x \ne \dfrac{1}{\sin x}$.
>
> *Stewart: 1.5 (text and box)*

^def-5-5

> [!definition] Definition §5.6: Inverse Cosine
> The cosine function restricted to $[0, \pi]$ is one-to-one. Its inverse is the **inverse cosine function**, denoted $\cos^{-1}$ or $\arccos$:
>
> $$
> \cos^{-1} x = y \quad\Longleftrightarrow\quad \cos y = x \ \text{ and } \ 0 \le y \le \pi .
> $$
>
> *Stewart: 1.5 (text and box)*

^def-5-6

> [!definition] Definition §5.7: Inverse Tangent
> The tangent function restricted to $(-\pi/2, \pi/2)$ is one-to-one. Its inverse is the **inverse tangent function**, denoted $\tan^{-1}$ or $\arctan$:
>
> $$
> \tan^{-1} x = y \quad\Longleftrightarrow\quad \tan y = x \ \text{ and } \ -\frac{\pi}{2} < y < \frac{\pi}{2} .
> $$
>
> *Stewart: 1.5 (text and box)*

^def-5-7

> [!theorem] Proposition §5.10: Domains, Ranges and Cancellation Equations
> | function | domain | range |
> |---|---|---|
> | $\sin^{-1} = \arcsin$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |
> | $\cos^{-1} = \arccos$ | $[-1, 1]$ | $[0, \pi]$ |
> | $\tan^{-1} = \arctan$ | $\mathbb{R}$ | $(-\pi/2, \pi/2)$ |
>
> The cancellation equations are
>
> $$
> \begin{aligned}
> \sin^{-1}(\sin x) &= x \quad \text{for } -\tfrac{\pi}{2} \le x \le \tfrac{\pi}{2}, & \sin(\sin^{-1} x) &= x \quad \text{for } -1 \le x \le 1, \\
> \cos^{-1}(\cos x) &= x \quad \text{for } 0 \le x \le \pi, & \cos(\cos^{-1} x) &= x \quad \text{for } -1 \le x \le 1 .
> \end{aligned}
> $$
>
> The graph of $\tan^{-1}$ has the horizontal asymptotes $y = \pi/2$ and $y = -\pi/2$.
>
> *Stewart: 1.5 (text and boxes)*

^prop-5-10

> [!proof]+ Proof
> Each inverse function is the inverse of a one-to-one restricted function, so Definition §5.2 applies to it. Its domain is the range of the restricted function and its range is the restricted interval. On $[-\pi/2, \pi/2]$ the sine increases from $-1$ to $1$, and on $[0, \pi]$ the cosine decreases from $1$ to $-1$, taking all values in between; on $(-\pi/2, \pi/2)$ the tangent increases and takes every real value. This gives the table. The cancellation equations are Theorem §5.2 for the restricted sine and cosine.
>
> The lines $x = \pm\pi/2$ are vertical asymptotes of $\tan$. The graph of $\tan^{-1}$ is the reflection of the graph of the restricted tangent about $y = x$ (Theorem §5.3), and the reflection of a vertical line $x = c$ is the horizontal line $y = c$. So $y = \pm\pi/2$ are horizontal asymptotes of $\tan^{-1}$.

^pf-5-10

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-2|§5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-3|§5.3]], [[§5 Inverse Functions and Logarithms#^def-5-5|Def. §5.5]], [[§5 Inverse Functions and Logarithms#^def-5-6|Def. §5.6]], [[§5 Inverse Functions and Logarithms#^def-5-7|Def. §5.7]]

![[m233-5-2.svg]]
*Each inverse trigonometric function (red) is the reflection about $y = x$ (green, dashed) of the restricted trigonometric function (gray). (a) $\sin^{-1}$ from sine on $[-\pi/2, \pi/2]$: domain $[-1, 1]$, range $[-\pi/2, \pi/2]$. (b) $\cos^{-1}$ from cosine on $[0, \pi]$: domain $[-1, 1]$, range $[0, \pi]$, decreasing. (c) $\tan^{-1}$ from tangent on $(-\pi/2, \pi/2)$: domain $\mathbb{R}$; the vertical asymptotes $x = \pm\pi/2$ of tangent (gray, dashed) become the horizontal asymptotes $y = \pm\pi/2$ (red, dashed).*

The remaining inverse trigonometric functions are used less often.

> [!definition] Definition §5.8: Inverse Cosecant, Secant and Cotangent
> $$
> \begin{aligned}
> y = \csc^{-1} x \ \ (|x| \ge 1) \quad&\Longleftrightarrow\quad \csc y = x \ \text{ and } \ y \in (0, \pi/2] \cup (\pi, 3\pi/2] , \\
> y = \sec^{-1} x \ \ (|x| \ge 1) \quad&\Longleftrightarrow\quad \sec y = x \ \text{ and } \ y \in [0, \pi/2) \cup [\pi, 3\pi/2) , \\
> y = \cot^{-1} x \ \ (x \in \mathbb{R}) \quad&\Longleftrightarrow\quad \cot y = x \ \text{ and } \ y \in (0, \pi) .
> \end{aligned}
> $$
>
> The intervals for $y$ in $\csc^{-1}$ and $\sec^{-1}$ are not universally agreed upon. Some authors use $y \in [0, \pi/2) \cup (\pi/2, \pi]$ for $\sec^{-1}$; the graph of the secant shows that this choice also gives a one-to-one restriction taking every value with $|x| \ge 1$. Check which convention a formula assumes.
>
> *Stewart: 1.5, Equation 12*

^def-5-8

> [!example] Example §5.5: Evaluating and Simplifying Inverse Trigonometric Expressions
> **(a)** $\sin^{-1}\big(\frac12\big) = \dfrac{\pi}{6}$, because $\sin(\pi/6) = \frac12$ and $\pi/6$ lies between $-\pi/2$ and $\pi/2$. (Also $\sin(5\pi/6) = \frac12$, but $5\pi/6$ is outside the range of $\sin^{-1}$.)
>
> **(b)** Evaluate $\tan\big(\arcsin\frac13\big)$. Let $\theta = \arcsin\frac13$, so $\sin\theta = \frac13$ and $-\pi/2 \le \theta \le \pi/2$; since $\sin\theta > 0$, in fact $0 < \theta < \pi/2$. In a right triangle with angle $\theta$, opposite side $1$ and hypotenuse $3$, the Pythagorean Theorem gives the adjacent side $\sqrt{9 - 1} = 2\sqrt2$. So
>
> $$
> \tan\Big(\arcsin\frac13\Big) = \tan\theta = \frac{1}{2\sqrt2} = \frac{\sqrt2}{4} .
> $$
>
> **(c)** Simplify $\cos(\tan^{-1} x)$. Let $y = \tan^{-1} x$. Then $\tan y = x$ and $-\pi/2 < y < \pi/2$. Since $\tan y$ is known, find $\sec y$ first:
>
> $$
> \sec^2 y = 1 + \tan^2 y = 1 + x^2, \qquad \sec y = \sqrt{1 + x^2} ,
> $$
>
> taking the positive root because $\cos y > 0$, hence $\sec y > 0$, for $-\pi/2 < y < \pi/2$. Thus
>
> $$
> \cos(\tan^{-1} x) = \cos y = \frac{1}{\sec y} = \frac{1}{\sqrt{1 + x^2}} .
> $$
>
> Alternatively (for $y > 0$), draw a right triangle with angle $y$, opposite side $x$ and adjacent side $1$; its hypotenuse is $\sqrt{1 + x^2}$, and $\cos y = 1/\sqrt{1 + x^2}$ can be read off.
>
> *Stewart: Examples 1.5.13 and 1.5.14*

^ex-5-5
