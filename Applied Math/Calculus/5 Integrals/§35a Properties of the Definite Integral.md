---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 35
stewart: "5.2"
aliases: ["Stewart 5.2 (cont.)"]
tags: [calculus]
---
← [[§35 The Definite Integral]] · ↑ [[· 5 Integrals]] · [[§36 The Fundamental Theorem of Calculus]] →

*Stewart, Section 5.2.*

[[§35 The Definite Integral#^def-35-1|Definition §35.1]] tacitly assumed $a < b$, but the limit of Riemann sums makes sense for $a > b$ too. Interchanging $a$ and $b$ changes $\Delta x$ from $(b - a)/n$ to $(a - b)/n$, which changes the sign of every Riemann sum; and if $a = b$, then $\Delta x = 0$.

## Properties of the Definite Integral

> [!definition] Definition §35.4: Reversed and Equal Limits
> $$
> \int_b^a f(x)\,dx = -\int_a^b f(x)\,dx , \qquad\qquad \int_a^a f(x)\,dx = 0 .
> $$
>
> *Stewart: 5.2 (text)*

^def-35-4

In the following properties $f$ and $g$ are continuous functions, so all the integrals exist ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]]).

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

> [!proof]+ Proof
> In each part, compute with right-endpoint sums ([[§35 The Definite Integral#^thm-35-2|Theorem §35.2]]), with $\Delta x = (b - a)/n$ and $x_i = a + i\,\Delta x$. The argument works for any sign of $b - a$; for $a = b$ every side is $0$.
>
> **1.** For $f(x) = c$, every Riemann sum is $\sum_{i=1}^{n} c\,\Delta x = n c\,\Delta x = c(b - a)$, so the limit is $c(b - a)$.
>
> **2.** Using [[§35 The Definite Integral#^thm-35-3|Theorem §35.3]] and the fact that the limit of a sum is the sum of the limits (both limits exist, since $f$ and $g$ are integrable):
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

> [!remark] Remark: Why It Works
> Property 1: if $c > 0$ and $a < b$, then $c(b - a)$ is the area of the rectangle of height $c$ over $[a, b]$. Property 2: for positive functions, the area under $f + g$ is the area under $f$ plus the area under $g$, because by graphical addition each vertical segment under $f + g$ has the length of the segment under $f$ plus that under $g$. Property 3: multiplying $f$ by $c > 0$ stretches or shrinks its graph vertically by the factor $c$, hence each approximating rectangle, hence the area. Only a constant can be taken out of an integral sign.

^rem-35-3

> [!theorem] Theorem §35.5: Additivity over Adjacent Intervals
> $$
> \int_a^c f(x)\,dx + \int_c^b f(x)\,dx = \int_a^b f(x)\,dx .
> $$
>
> This holds whatever the order of $a$, $b$, $c$.
>
> *Stewart: 5.2, Property 5*

^thm-35-5

*Stewart omits the proof ("not easy to prove in general"). For $a < c < b$ it is [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]]. Every other order reduces to that case by [[§35 The Definite Integral#^def-35-4|Definition §35.4]]: for instance, if $a < b < c$, then $\int_a^c = \int_a^b + \int_b^c$, so $\int_a^b = \int_a^c - \int_b^c = \int_a^c + \int_c^b$.*

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

> [!remark] Remark: Why It Works
> For $f \ge 0$ the integral is an area, and areas are positive (Property 6); a bigger function has a bigger integral (Property 7). For $f \ge 0$ continuous, take $m$ and $M$ to be the absolute minimum and maximum of $f$ on $[a, b]$ ([[§25 Maximum and Minimum Values#^thm-25-1|Theorem §25.1]]). Then Property 8 says that the area under the graph lies between the areas of the rectangles over $[a, b]$ of heights $m$ and $M$.

^rem-35-5

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
