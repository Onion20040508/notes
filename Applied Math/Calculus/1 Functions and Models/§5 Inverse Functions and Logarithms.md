---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 5
stewart: "1.5"
aliases: ["Stewart 1.5"]
tags: [calculus]
---
← [[§4 Exponential Functions]] · ↑ [[· 1 Functions and Models]] · [[§5a Logarithmic and Inverse Trigonometric Functions]] →

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
> Both directions together (in [[Contrapositive, Converse and Inverse|contrapositive]] form) give the test.

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
> The second factor is a sum of two squares, so it is $0$ only if $x_2 = 0$ and then $x_1 = 0$. Either way $x_1 = x_2$. So $f$ is one-to-one ([[§5 Inverse Functions and Logarithms#^def-5-1|Definition §5.1]], in contrapositive form).
>
> *By the graph.* The graph of $y = x^3$ rises from left to right (flattening at the origin), and every horizontal line meets it exactly once. By [[§5 Inverse Functions and Logarithms#^thm-5-1|Theorem §5.1]], $f$ is one-to-one.
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
> Let $x \in A$ and put $y = f(x)$, which lies in the range $B$. Since $f(x) = y$, [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]] gives $f^{-1}(y) = x$, that is, $f^{-1}(f(x)) = x$.
>
> Let $x \in B$ and put $y = f^{-1}(x)$. By the form (3) of the definition, $f^{-1}(x) = y$ means $f(y) = x$, that is, $f(f^{-1}(x)) = x$.

^pf-5-2

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§9 Injections, Surjections and Bijections#^def-9-3|250 Def. §9.3]] defines the inverse by the same "$y = f(x) \iff x = g(y)$", and [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]] shows that an inverse exists exactly for bijections. Stewart's $f$ is a bijection from $A$ onto its range $B$: one-to-one by assumption, onto because $B$ is the range.
> - The cancellation equations characterize the inverse: $g \circ f = I_A$ and $f \circ g = I_B$ hold exactly when $g = f^{-1}$, [[§9 Injections, Surjections and Bijections#^prop-9-3|250 Prop. §9.3]].

> [!remark] Remark: Method — How to Find the Inverse Function of a One-to-One Function f
> 1. Write $y = f(x)$.
> 2. Solve this equation for $x$ in terms of $y$ (if possible). By [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]] the result is $x = f^{-1}(y)$.
> 3. To express $f^{-1}$ as a function of $x$, interchange $x$ and $y$. The resulting equation is $y = f^{-1}(x)$.
>
> Check the answer with the cancellation equations ([[§5 Inverse Functions and Logarithms#^thm-5-2|Theorem §5.2]]), and record the domain of $f^{-1}$, which is the range of $f$ (it may be smaller than the natural domain of the formula, as in [[§5 Inverse Functions and Logarithms#^ex-5-2|Example §5.2]](b)).
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
> **Points are swapped.** By [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]], $f(a) = b$ if and only if $f^{-1}(b) = a$. So $(a, b)$ is on the graph of $f$ if and only if $(b, a)$ is on the graph of $f^{-1}$.
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
> $f$ is defined for $-1 - x \ge 0$, so its domain is $(-\infty, -1]$, and its range is $[0, \infty)$. Squaring $y = \sqrt{-1 - x}$ gives $y^2 = -1 - x$, that is, $x = -y^2 - 1$: the graph of $f$ is the top half ($y \ge 0$) of this parabola, which opens to the left and has its vertex at $(-1, 0)$. Reflecting about $y = x$ ([[§5 Inverse Functions and Logarithms#^thm-5-3|Theorem §5.3]]) gives the graph of $f^{-1}$.
>
> *Check by formula.* Solving $y = \sqrt{-1 - x}$ for $x$ gives $x = -y^2 - 1$ with $y \ge 0$; interchanging, $f^{-1}(x) = -x^2 - 1$ for $x \ge 0$. The restriction $x \ge 0$ is essential: the domain of $f^{-1}$ is the range $[0, \infty)$ of $f$. So the graph of $f^{-1}$ is the right half of the parabola $y = -x^2 - 1$, starting at $(0, -1)$, the mirror image of the endpoint $(-1, 0)$ of the graph of $f$.
>
> *Stewart: Examples 1.5.4 and 1.5.5*

^ex-5-2

*Continued in [[§5a Logarithmic and Inverse Trigonometric Functions]]: logarithmic functions, natural logarithms and inverse trigonometric functions.*
