---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 35
stewart: "5.2"
aliases: ["Stewart 5.2"]
tags: [calculus]
---
← [[§34 The Area and Distance Problems]] · ↑ [[· 5 Integrals]] · [[§36 The Fundamental Theorem of Calculus]] →

*Stewart, Section 5.2.*

The limit of sums $\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^{\ast})\,\Delta x$ that gave areas and distances in [[§34 The Area and Distance Problems|§34]] is now named the definite integral $\int_a^b f(x)\,dx$, for any function $f$, positive or not. When $f$ changes sign the integral is a *net* area. This section evaluates a few integrals directly from the definition using formulas for sums of powers, introduces the Midpoint Rule for approximating them, and proves the algebraic and comparison properties of the integral. These properties, together with the Fundamental Theorem of the next section, are what one actually computes with.

## The Definite Integral

The same limit occurs for areas, for distances, and (Chapters 6 and 8) for lengths of curves, volumes, centers of mass, force due to water pressure and work. It gets a name.

> [!definition] Definition §35.1: Definite Integral
> Let $f$ be a function defined for $a \le x \le b$. Divide $[a, b]$ into $n$ subintervals of equal width $\Delta x = (b - a)/n$. Let $x_0 (= a), x_1, x_2, \ldots, x_n (= b)$ be the endpoints of these subintervals, and let $x_1^{\ast}, x_2^{\ast}, \ldots, x_n^{\ast}$ be any **sample points** in them, so $x_i^{\ast}$ lies in the $i$th subinterval $[x_{i-1}, x_i]$. The **definite integral of $f$ from $a$ to $b$** is
>
> $$
> \int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x ,
> $$
>
> provided that this limit exists and gives the same value for all possible choices of sample points. If it does, $f$ is **integrable** on $[a, b]$.
>
> Precisely: for every $\varepsilon > 0$ there is an integer $N$ such that
>
> $$
> \left| \int_a^b f(x)\,dx - \sum_{i=1}^{n} f(x_i^*)\,\Delta x \right| < \varepsilon
> $$
>
> for every integer $n > N$ and for every choice of $x_i^*$ in $[x_{i-1}, x_i]$.
>
> *Stewart: 5.2, Definition 2*

^def-35-1

> [!remark]- Connections
> - Rigorous treatment: [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]] allows subintervals of unequal width and asks that the Riemann sums be close to the integral as soon as the widest subinterval is short enough (as in the remark on unequal subintervals below). Its equivalence with the upper/lower-sum definition is [[§32 The Definition of the Riemann Integral#^thm-32-6|451 Thm. §32.6]].
> - Every Riemann integrable function is Lebesgue integrable with the same integral: [[§15 The General Lebesgue Integral#^thm-15-10|551 Thm. §15.10]].

> [!definition] Definition §35.2: Integrand, Limits of Integration, Riemann Sum
> In the notation $\int_a^b f(x)\,dx$, the symbol $\int$ (introduced by Leibniz: an elongated S, for "sum") is the **integral sign**, $f(x)$ is the **integrand**, $a$ and $b$ are the **limits of integration**, $a$ is the **lower limit** and $b$ the **upper limit**. For now $dx$ has no meaning by itself: $\int_a^b f(x)\,dx$ is one symbol, and $dx$ only indicates that the independent variable is $x$. Calculating an integral is called **integration**.
>
> The sum $\sum_{i=1}^{n} f(x_i^{\ast})\,\Delta x$ is a **Riemann sum** (after Bernhard Riemann, 1826–1866). Definition §35.1 says that the integral of an integrable function can be approximated to any desired accuracy by a Riemann sum.
>
> *Stewart: 5.2, Notes 1 and 3*

^def-35-2

The definite integral is a *number*; it does not depend on $x$. Any letter can replace $x$ (a **dummy variable**) without changing the value (Stewart, Note 2):

$$
\int_a^b f(x)\,dx = \int_a^b f(t)\,dt = \int_a^b f(r)\,dr .
$$

When writing $\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x = \int_a^b f(x)\,dx$, Leibniz's notation records the limiting process: $\lim \Sigma$ becomes $\int$, $x_i^*$ becomes $x$, and $\Delta x$ becomes $dx$.

> [!remark] Remark: The Integral as a Net Area
> If $f \ge 0$, a Riemann sum is a sum of areas of rectangles, and comparing Definition §35.1 with [[§34 The Area and Distance Problems#^def-34-1|Definition §34.1]] shows that $\int_a^b f(x)\,dx$ is the **area under the curve** $y = f(x)$ from $a$ to $b$.
>
> If $f$ takes both signs, the Riemann sum is the sum of the areas of the rectangles above the $x$-axis minus the areas of those below it, since $f(x_i^{\ast})\,\Delta x < 0$ when $f(x_i^{\ast}) < 0$. In the limit, the integral is a **net area**:
>
> $$
> \int_a^b f(x)\,dx = A_1 - A_2 ,
> $$
>
> where $A_1$ is the area of the region above the $x$-axis and below the graph of $f$, and $A_2$ the area of the region below the $x$-axis and above the graph of $f$.

^rem-35-1

> [!remark] Remark: Subintervals of Unequal Width
> Sometimes subintervals of unequal widths $\Delta x_1, \Delta x_2, \ldots, \Delta x_n$ are more convenient: velocity data recorded at unequally spaced times, or numerical methods that adapt the subdivision. Then all widths must tend to $0$, which happens when the largest width does:
>
> $$
> \int_a^b f(x)\,dx = \lim_{\max \Delta x_i \to 0} \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i .
> $$

^rem-35-2

> [!theorem] Theorem §35.1: Continuous Functions Are Integrable
> If $f$ is continuous on $[a, b]$, or if $f$ has only a finite number of jump discontinuities, then $f$ is integrable on $[a, b]$; that is, the definite integral $\int_a^b f(x)\,dx$ exists.
>
> *Stewart: 5.2, Theorem 3*

^thm-35-1

*Stewart omits the proof ("proved in more advanced courses"). See [[§32 The Definition of the Riemann Integral#^thm-32-7|451 Thm. §32.7]] for continuous functions (via uniform continuity). For jumps, [[§32 The Definition of the Riemann Integral#^ex-32-2|451 Ex. §32.2]] shows how a jump is isolated in a short subinterval, and [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]] glues the continuous pieces together.*

Not every function is integrable: the function that is $1$ at rational and $0$ at irrational numbers is not (Stewart, Exercises 81–82; [[§32 The Definition of the Riemann Integral#^ex-32-3|451 Ex. §32.3]]).

> [!theorem] Theorem §35.2: The Integral as a Limit of Right-Endpoint Sums
> If $f$ is integrable on $[a, b]$, then
>
> $$
> \int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i)\,\Delta x ,
> \qquad\text{where}\qquad
> \Delta x = \frac{b - a}{n} \quad\text{and}\quad x_i = a + i\,\Delta x .
> $$
>
> *Stewart: 5.2, Theorem 4*

^thm-35-2

> [!proof]+ Proof
> Since $f$ is integrable, the limit in Definition §35.1 exists and has the same value for every choice of sample points. Choose $x_i^* = x_i$, the right endpoint of $[x_{i-1}, x_i]$. The endpoints of the $n$ equal subintervals are $x_i = a + i\,\Delta x$, so the Riemann sums become $\sum_{i=1}^{n} f(x_i)\,\Delta x$, and their limit is $\int_a^b f(x)\,dx$.

^pf-35-2

*Uses:* [[§35 The Definite Integral#^def-35-1|Def. §35.1]]

For instance, comparing with Theorem §35.2 on $[0, \pi]$ (so $x_i = i\pi/n$),

$$
\lim_{n \to \infty} \sum_{i=1}^{n} (x_i^3 + x_i \sin x_i)\,\Delta x = \int_0^{\pi} (x^3 + x \sin x)\,dx
$$

(Stewart, Example 5.2.2). Recognizing a limit of sums as an integral, as here, is the key step in every application of Chapter 6.

## Evaluating Definite Integrals

To compute a limit of Riemann sums by hand we need the sums of powers of the first $n$ positive integers (Stewart's Equations 5–8; 7 was used in [[§34 The Area and Distance Problems#^ex-34-2|Example §34.2]], and all four are proved in Appendix E, [[§120 Sigma Notation#^thm-120-2|Theorem §120.2]]):

$$
\sum_{i=1}^{n} 1 = n, \qquad
\sum_{i=1}^{n} i = \frac{n(n + 1)}{2}, \qquad
\sum_{i=1}^{n} i^2 = \frac{n(n + 1)(2n + 1)}{6}, \qquad
\sum_{i=1}^{n} i^3 = \left[ \frac{n(n + 1)}{2} \right]^2 .
$$

> [!theorem] Theorem §35.3: Properties of Sums
> For numbers $a_1, \ldots, a_n$, $b_1, \ldots, b_n$ and a constant $c$:
>
> $$
> \sum_{i=1}^{n} c\,a_i = c \sum_{i=1}^{n} a_i, \qquad
> \sum_{i=1}^{n} (a_i + b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i, \qquad
> \sum_{i=1}^{n} (a_i - b_i) = \sum_{i=1}^{n} a_i - \sum_{i=1}^{n} b_i .
> $$
>
> *Stewart: 5.2, Equations 9–11*

^thm-35-3

> [!proof]+ Proof
> Write out each side. For the first, $c a_1 + c a_2 + \cdots + c a_n = c(a_1 + a_2 + \cdots + a_n)$ by the distributive law (this is Stewart's margin proof). For the second, $(a_1 + b_1) + \cdots + (a_n + b_n) = (a_1 + \cdots + a_n) + (b_1 + \cdots + b_n)$ by the commutative and associative laws of addition. The third follows from the first two: $a_i - b_i = a_i + (-1) b_i$, so
>
> $$
> \sum_{i=1}^{n} (a_i - b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} (-1) b_i = \sum_{i=1}^{n} a_i - \sum_{i=1}^{n} b_i .
> $$

^pf-35-3

*Uses:* field axioms of $\mathbb{R}$ ([[§3 The Set ℝ of Real Numbers#^def-3-1|451 Def. §3.1]])

The same rules, for sums running from any $i = m$ to $n$, are [[§120 Sigma Notation#^thm-120-1|Theorem §120.1]] (Stewart's Appendix E), together with the other rules of sigma notation.

> [!example] Example §35.1: A Riemann Sum and the Exact Integral of x³ − 6x
> Let $f(x) = x^3 - 6x$ on $[0, 3]$.
>
> **(a)** Evaluate the Riemann sum with $n = 6$ subintervals and right endpoints as sample points.
>
> **(b)** Evaluate $\displaystyle\int_0^3 (x^3 - 6x)\,dx$.
>
> **(a)** $\Delta x = (3 - 0)/6 = \frac12$, and the right endpoints are $0.5, 1.0, 1.5, 2.0, 2.5, 3.0$. Since $f(0.5) = -2.875$, $f(1) = -5$, $f(1.5) = -5.625$, $f(2) = -4$, $f(2.5) = 0.625$, $f(3) = 9$,
>
> $$
> R_6 = \sum_{i=1}^{6} f(x_i)\,\Delta x = \tfrac12 (-2.875 - 5 - 5.625 - 4 + 0.625 + 9) = \tfrac12 (-7.875) = -3.9375 .
> $$
>
> $f$ is not positive, so this is not a sum of areas: it is the sum of the areas of the rectangles above the $x$-axis minus those below it.
>
> **(b)** $f$ is continuous, hence integrable (Theorem §35.1), so Theorem §35.2 applies with $\Delta x = \frac3n$ and $x_i = \frac{3i}{n}$:
>
> $$
> \begin{aligned}
> \int_0^3 (x^3 - 6x)\,dx
> &= \lim_{n \to \infty} \sum_{i=1}^{n} f\Big(\frac{3i}{n}\Big) \frac3n
> = \lim_{n \to \infty} \frac3n \sum_{i=1}^{n} \Big[ \Big(\frac{3i}{n}\Big)^3 - 6\Big(\frac{3i}{n}\Big) \Big] && (n \text{ is constant in the sum}) \\
> &= \lim_{n \to \infty} \frac3n \sum_{i=1}^{n} \Big[ \frac{27}{n^3}\,i^3 - \frac{18}{n}\,i \Big]
> = \lim_{n \to \infty} \Big[ \frac{81}{n^4} \sum_{i=1}^{n} i^3 - \frac{54}{n^2} \sum_{i=1}^{n} i \Big] && \text{(Theorem §35.3)} \\
> &= \lim_{n \to \infty} \Big\{ \frac{81}{n^4} \Big[\frac{n(n + 1)}{2}\Big]^2 - \frac{54}{n^2} \cdot \frac{n(n + 1)}{2} \Big\} && \text{(sums of } i^3 \text{ and } i) \\
> &= \lim_{n \to \infty} \Big[ \frac{81}{4} \Big(1 + \frac1n\Big)^2 - 27\Big(1 + \frac1n\Big) \Big] = \frac{81}{4} - 27 = -\frac{27}{4} = -6.75 .
> \end{aligned}
> $$
>
> This is not an area. It is $A_1 - A_2$, where $A_1$ is the area between the graph and the $x$-axis for $\sqrt6 \le x \le 3$ (where $f \ge 0$) and $A_2$ the area for $0 \le x \le \sqrt6$ (where $f \le 0$). With $n = 40$, $R_{40} \approx -6.3998$; the right Riemann sums approach $-6.75$ slowly ($R_{5000} \approx -6.7473$). The Fundamental Theorem ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]) gets $-6.75$ in one line.
>
> *Stewart: Examples 5.2.1 and 5.2.3*

^ex-35-1

![[m233-35-1.svg]]
*Example §35.1. The integral of $x^3 - 6x$ over $[0, 3]$ is the net area $A_1 - A_2 = -6.75$: the blue region above the axis counts positively, the orange one below negatively. The dashed rectangles form the Riemann sum $R_6 = -3.9375$; the four below the axis contribute negative terms. With so few rectangles, the error is large.*

For $f(x) = e^x$ on $[1, 3]$ the same method gives $\int_1^3 e^x\,dx = \lim_{n \to \infty} \frac2n \sum_{i=1}^{n} e^{1 + 2i/n}$, a geometric sum that a computer algebra system evaluates to $e^3 - e$ (Stewart, Example 5.2.4). Integrals of positive functions whose graphs are familiar shapes can be read off as areas:

> [!example] Example §35.2: Integrals as Areas
> Evaluate by interpreting each integral in terms of areas: (a) $\displaystyle\int_0^1 \sqrt{1 - x^2}\,dx$; (b) $\displaystyle\int_0^3 (x - 1)\,dx$.
>
> **(a)** $f(x) = \sqrt{1 - x^2} \ge 0$, so the integral is the area under $y = \sqrt{1 - x^2}$ from $0$ to $1$. Squaring, $y^2 = 1 - x^2$, that is $x^2 + y^2 = 1$ with $y \ge 0$: the graph is the quarter of the unit circle in the first quadrant. So
>
> $$
> \int_0^1 \sqrt{1 - x^2}\,dx = \tfrac14 \pi (1)^2 = \frac{\pi}{4} .
> $$
>
> (That a circle of radius $r$ has area $\pi r^2$ is proved with integrals in [[§46 Trigonometric Substitution#^ex-46-2|Example §46.2]], the case $a = b = r$ of the ellipse.)
>
> **(b)** $y = x - 1$ is the line of slope $1$ through $(1, 0)$. On $[1, 3]$ it is above the axis, bounding a triangle $A_1$ with base $2$ and height $2$; on $[0, 1]$ it is below, bounding a triangle $A_2$ with base $1$ and height $1$. So
>
> $$
> \int_0^3 (x - 1)\,dx = A_1 - A_2 = \tfrac12 (2 \cdot 2) - \tfrac12 (1 \cdot 1) = 1.5 .
> $$
>
> *Stewart: Example 5.2.5*

^ex-35-2

## The Midpoint Rule

Right endpoints make the limit easy to compute. To *approximate* an integral, midpoints are usually better.

> [!definition] Definition §35.3: The Midpoint Rule
> $$
> \int_a^b f(x)\,dx \approx \sum_{i=1}^{n} f(\bar x_i)\,\Delta x = \Delta x \big[ f(\bar x_1) + \cdots + f(\bar x_n) \big] ,
> $$
>
> where
>
> $$
> \Delta x = \frac{b - a}{n} \qquad\text{and}\qquad \bar x_i = \tfrac12 (x_{i-1} + x_i) = \text{midpoint of } [x_{i-1}, x_i] .
> $$
>
> *Stewart: 5.2, Midpoint Rule*

^def-35-3

> [!example] Example §35.3: The Midpoint Rule for 1/x
> Use the Midpoint Rule with $n = 5$ to approximate $\displaystyle\int_1^2 \frac1x\,dx$.
>
> $\Delta x = (2 - 1)/5 = \frac15$. The endpoints of the five subintervals are $1, 1.2, 1.4, 1.6, 1.8, 2.0$, so the midpoints are $1.1, 1.3, 1.5, 1.7, 1.9$, and
>
> $$
> \int_1^2 \frac1x\,dx \approx \Delta x \big[ f(1.1) + f(1.3) + f(1.5) + f(1.7) + f(1.9) \big]
> = \frac15 \Big( \frac{1}{1.1} + \frac{1}{1.3} + \frac{1}{1.5} + \frac{1}{1.7} + \frac{1}{1.9} \Big) \approx 0.691908 .
> $$
>
> Since $1/x > 0$ on $[1, 2]$, this is the total area of five rectangles approximating the area under the hyperbola. (The exact value is $\ln 2 \approx 0.693147$, as [[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]] will show; error estimates for the Midpoint Rule come in [[§50 Approximate Integration#^thm-50-1|Theorem §50.1]].)
>
> For the integral of Example §35.1, the Midpoint Rule with $n = 40$ gives $M_{40} \approx -6.7563$, much closer to $-6.75$ than $R_{40} \approx -6.3998$.
>
> *Stewart: Example 5.2.6*

^ex-35-3

## Properties of the Definite Integral

Definition §35.1 tacitly assumed $a < b$, but the limit of Riemann sums makes sense for $a > b$ too. Interchanging $a$ and $b$ changes $\Delta x$ from $(b - a)/n$ to $(a - b)/n$, which changes the sign of every Riemann sum; and if $a = b$, then $\Delta x = 0$.

> [!definition] Definition §35.4: Reversed and Equal Limits
> $$
> \int_b^a f(x)\,dx = -\int_a^b f(x)\,dx , \qquad\qquad \int_a^a f(x)\,dx = 0 .
> $$
>
> *Stewart: 5.2 (text)*

^def-35-4

In the following properties $f$ and $g$ are continuous functions, so all the integrals exist (Theorem §35.1).

> [!theorem] Theorem §35.4: Properties of the Integral
> For any constant $c$:
> 1. $\displaystyle\int_a^b c\,dx = c(b - a)$;
> 2. $\displaystyle\int_a^b [f(x) + g(x)]\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$;
> 3. $\displaystyle\int_a^b c f(x)\,dx = c \int_a^b f(x)\,dx$;
> 4. $\displaystyle\int_a^b [f(x) - g(x)]\,dx = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx$.
>
> These hold whether $a < b$, $a = b$ or $a > b$.
>
> *Stewart: 5.2, Properties of the Integral 1–4*

^thm-35-4

> [!remark] Remark: Why It Works
> Property 1: if $c > 0$ and $a < b$, then $c(b - a)$ is the area of the rectangle of height $c$ over $[a, b]$. Property 2: for positive functions, the area under $f + g$ is the area under $f$ plus the area under $g$, because by graphical addition each vertical segment under $f + g$ has the length of the segment under $f$ plus that under $g$. Property 3: multiplying $f$ by $c > 0$ stretches or shrinks its graph vertically by the factor $c$, hence each approximating rectangle, hence the area. Only a constant can be taken out of an integral sign.

^rem-35-3

> [!proof]+ Proof
> In each part, compute with right-endpoint sums (Theorem §35.2), with $\Delta x = (b - a)/n$ and $x_i = a + i\,\Delta x$. The argument works for any sign of $b - a$; for $a = b$ every side is $0$.
>
> **1.** For $f(x) = c$, every Riemann sum is $\sum_{i=1}^{n} c\,\Delta x = n c\,\Delta x = c(b - a)$, so the limit is $c(b - a)$.
>
> **2.** Using Theorem §35.3 and the fact that the limit of a sum is the sum of the limits (both limits exist, since $f$ and $g$ are integrable):
>
> $$
> \begin{aligned}
> \int_a^b [f(x) + g(x)]\,dx &= \lim_{n \to \infty} \sum_{i=1}^{n} [f(x_i) + g(x_i)]\,\Delta x
> = \lim_{n \to \infty} \Big[ \sum_{i=1}^{n} f(x_i)\,\Delta x + \sum_{i=1}^{n} g(x_i)\,\Delta x \Big] \\
> &= \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i)\,\Delta x + \lim_{n \to \infty} \sum_{i=1}^{n} g(x_i)\,\Delta x
> = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx .
> \end{aligned}
> $$
>
> **3.** In the same way, by the first property of sums and the Constant Multiple Law for limits,
>
> $$
> \int_a^b c f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} c f(x_i)\,\Delta x = \lim_{n \to \infty} c \sum_{i=1}^{n} f(x_i)\,\Delta x = c \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i)\,\Delta x = c \int_a^b f(x)\,dx .
> $$
>
> **4.** Write $f - g = f + (-g)$ and use Property 2 and then Property 3 with $c = -1$:
>
> $$
> \int_a^b [f(x) - g(x)]\,dx = \int_a^b f(x)\,dx + \int_a^b (-1) g(x)\,dx = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx .
> $$

^pf-35-4

*Uses:* [[§35 The Definite Integral#^thm-35-1|§35.1]], [[§35 The Definite Integral#^thm-35-2|§35.2]], [[§35 The Definite Integral#^thm-35-3|§35.3]], [[§11 Limits at Infinity; Horizontal Asymptotes#^thm-11-2|§11.2]] (Sum and Constant Multiple Laws, for limits as $n \to \infty$)

> [!remark]- Connections
> - Rigorous treatment: linearity [[§33 Properties of the Riemann Integral#^thm-33-2|451 Thm. §33.2]], proved there with upper and lower sums for all integrable (not only continuous) $f$ and $g$.

> [!theorem] Theorem §35.5: Additivity over Adjacent Intervals
> $$
> \int_a^c f(x)\,dx + \int_c^b f(x)\,dx = \int_a^b f(x)\,dx .
> $$
>
> This holds whatever the order of $a$, $b$, $c$.
>
> *Stewart: 5.2, Property 5*

^thm-35-5

*Stewart omits the proof ("not easy to prove in general"). For $a < c < b$ it is [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]]. Every other order reduces to that case by Definition §35.4: for instance, if $a < b < c$, then $\int_a^c = \int_a^b + \int_b^c$, so $\int_a^b = \int_a^c - \int_b^c = \int_a^c + \int_c^b$.*

> [!remark] Remark: Why It Works
> For $f \ge 0$ and $a < c < b$: the area under $y = f(x)$ from $a$ to $c$ plus the area from $c$ to $b$ is the total area from $a$ to $b$.

^rem-35-4

Properties 1–5 hold for any order of the limits. The next three compare sizes and need $a \le b$.

> [!theorem] Theorem §35.6: Comparison Properties of the Integral
> Let $a \le b$.
>
> 6. If $f(x) \ge 0$ for $a \le x \le b$, then $\displaystyle\int_a^b f(x)\,dx \ge 0$.
> 7. If $f(x) \ge g(x)$ for $a \le x \le b$, then $\displaystyle\int_a^b f(x)\,dx \ge \int_a^b g(x)\,dx$.
> 8. If $m \le f(x) \le M$ for $a \le x \le b$, then
>
> $$
> m(b - a) \le \int_a^b f(x)\,dx \le M(b - a) .
> $$
>
> *Stewart: 5.2, Comparison Properties 6–8*

^thm-35-6

> [!remark] Remark: Why It Works
> For $f \ge 0$ the integral is an area, and areas are positive (Property 6); a bigger function has a bigger integral (Property 7). For $f \ge 0$ continuous, take $m$ and $M$ to be the absolute minimum and maximum of $f$ on $[a, b]$ ([[§25 Maximum and Minimum Values#^thm-25-1|Theorem §25.1]]). Then Property 8 says that the area under the graph lies between the areas of the rectangles over $[a, b]$ of heights $m$ and $M$.

^rem-35-5

> [!proof]+ Proof
> **6.** If $a = b$ the integral is $0$. If $a < b$, then $\Delta x > 0$ and $f(x_i) \ge 0$, so every Riemann sum $\sum_{i=1}^{n} f(x_i)\,\Delta x$ is $\ge 0$. A limit of numbers $\ge 0$ is $\ge 0$ (limits preserve inequalities), so $\int_a^b f(x)\,dx \ge 0$.
>
> **7.** Since $f - g \ge 0$ on $[a, b]$, Property 6 and Property 4 give
>
> $$
> 0 \le \int_a^b [f(x) - g(x)]\,dx = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx .
> $$
>
> **8.** (Stewart's proof.) Since $m \le f(x) \le M$, Property 7 gives
>
> $$
> \int_a^b m\,dx \le \int_a^b f(x)\,dx \le \int_a^b M\,dx .
> $$
>
> By Property 1 the outer integrals are $m(b - a)$ and $M(b - a)$.

^pf-35-6

*Uses:* [[§35 The Definite Integral#^thm-35-2|§35.2]], [[§35 The Definite Integral#^thm-35-4|§35.4]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-6|§8.6]] (limits preserve inequalities)

> [!remark]- Connections
> - Rigorous treatment: monotonicity [[§33 Properties of the Riemann Integral#^thm-33-3|451 Thm. §33.3]]; the companion estimate $\big|\int_a^b f\big| \le \int_a^b |f|$ is [[§33 Properties of the Riemann Integral#^thm-33-4|451 Thm. §33.4]].

> [!example] Example §35.4: Computing with the Properties
> **(a)** Evaluate $\displaystyle\int_0^1 (4 + 3x^2)\,dx$.
>
> By Properties 2 and 3, then Property 1 and [[§34 The Area and Distance Problems#^ex-34-2|Example §34.2]] ($\int_0^1 x^2\,dx = \frac13$),
>
> $$
> \int_0^1 (4 + 3x^2)\,dx = \int_0^1 4\,dx + 3 \int_0^1 x^2\,dx = 4(1 - 0) + 3 \cdot \tfrac13 = 5 .
> $$
>
> **(b)** If $\int_0^{10} f(x)\,dx = 17$ and $\int_0^8 f(x)\,dx = 12$, find $\int_8^{10} f(x)\,dx$.
>
> By Property 5, $\int_0^8 f(x)\,dx + \int_8^{10} f(x)\,dx = \int_0^{10} f(x)\,dx$, so
>
> $$
> \int_8^{10} f(x)\,dx = 17 - 12 = 5 .
> $$
>
> **(c)** Use Property 8 to estimate $\displaystyle\int_0^1 e^{-x^2}\,dx$.
>
> $f(x) = e^{-x^2}$ is decreasing on $[0, 1]$ (as $x^2$ increases, $-x^2$ decreases). So its absolute maximum is $M = f(0) = 1$ and its absolute minimum is $m = f(1) = e^{-1}$. By Property 8,
>
> $$
> e^{-1}(1 - 0) \le \int_0^1 e^{-x^2}\,dx \le 1(1 - 0), \qquad\text{that is}\qquad 0.367 \le \int_0^1 e^{-x^2}\,dx \le 1 ,
> $$
>
> since $e^{-1} \approx 0.3679$. The integral lies between the area of the rectangle of height $e^{-1}$ and the area of the unit square. Property 8 is useful when only a rough size of an integral is needed.
>
> *Stewart: Examples 5.2.7, 5.2.8 and 5.2.9*

^ex-35-4
