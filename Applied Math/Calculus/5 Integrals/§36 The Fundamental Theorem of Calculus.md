---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 36
stewart: "5.3"
aliases: ["Stewart 5.3"]
tags: [calculus]
---
← [[§35 The Definite Integral]] · ↑ [[· 5 Integrals]] · [[§37 Indefinite Integrals and the Net Change Theorem]] →

*Stewart, Section 5.3.*

Differential calculus grew out of the tangent problem and integral calculus out of the area problem, two problems that look unrelated. The Fundamental Theorem of Calculus (Barrow, then Newton and Leibniz) says that differentiation and integration are inverse processes. Part 1: the "area so far" function $g(x) = \int_a^x f(t)\,dt$ of a continuous $f$ is an antiderivative of $f$. Part 2: an integral can be evaluated from any antiderivative, $\int_a^b f(x)\,dx = F(b) - F(a)$. Part 2 replaces the limits of Riemann sums of [[§35 The Definite Integral|§35]] by a one-line calculation, and is the reason the rest of the course can compute areas, volumes and work.

## The Fundamental Theorem of Calculus, Part 1

Let $f$ be continuous on $[a, b]$ and define

$$
g(x) = \int_a^x f(t)\,dt , \qquad a \le x \le b . \qquad (1)
$$

For each fixed $x$ the integral is a number. As $x$ varies, it defines a function of $x$, which depends only on the upper limit $x$. If $f \ge 0$, then $g(x)$ is the area under the graph of $f$ from $a$ to $x$: think of $g$ as the "area so far" function. For example, with $f(t) = t$ and $a = 0$, the region under the graph is a triangle and $g(x) = \int_0^x t\,dt = \frac{x^2}{2}$ (Stewart, Exercise 5.2.47). Here $g'(x) = x$, that is, $g' = f$.

> [!remark] Remark: Why It Works
> For $f \ge 0$ and $h > 0$, $g(x + h) - g(x)$ is the area under the graph of $f$ from $x$ to $x + h$. For small $h$ this thin strip is nearly a rectangle of height $f(x)$ and width $h$:
>
> $$
> g(x + h) - g(x) \approx h f(x), \qquad\text{so}\qquad \frac{g(x + h) - g(x)}{h} \approx f(x) .
> $$
>
> So we expect $g'(x) = \lim_{h \to 0} \dfrac{g(x + h) - g(x)}{h} = f(x)$. The theorem says this is true even when $f$ is not positive.

^rem-36-1

> [!theorem] Theorem §36.1: The Fundamental Theorem of Calculus, Part 1
> If $f$ is continuous on $[a, b]$, then the function $g$ defined by
>
> $$
> g(x) = \int_a^x f(t)\,dt , \qquad a \le x \le b ,
> $$
>
> is continuous on $[a, b]$ and differentiable on $(a, b)$, and $g'(x) = f(x)$. In Leibniz notation,
>
> $$
> \frac{d}{dx} \int_a^x f(t)\,dt = f(x) . \qquad (5)
> $$
>
> In words: the derivative of a definite integral with respect to its upper limit is the integrand evaluated at the upper limit. (Abbreviated FTC1.)
>
> *Stewart: 5.3, Fundamental Theorem of Calculus, Part 1, and Equation 5*

^thm-36-1

> [!proof]+ Proof
> **The difference quotient.** If $x$ and $x + h$ are in $(a, b)$, then by Property 5 of integrals ([[§35 The Definite Integral#^thm-35-5|Theorem §35.5]]),
>
> $$
> g(x + h) - g(x) = \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt = \Big( \int_a^x f(t)\,dt + \int_x^{x+h} f(t)\,dt \Big) - \int_a^x f(t)\,dt = \int_x^{x+h} f(t)\,dt ,
> $$
>
> so for $h \ne 0$
>
> $$
> \frac{g(x + h) - g(x)}{h} = \frac1h \int_x^{x+h} f(t)\,dt . \qquad (2)
> $$
>
> **Case $h > 0$.** Since $f$ is continuous on $[x, x + h]$, the Extreme Value Theorem gives numbers $u$ and $v$ in $[x, x + h]$ with $f(u) = m$ and $f(v) = M$, the absolute minimum and maximum values of $f$ on $[x, x + h]$. By Property 8 of integrals ([[§35 The Definite Integral#^thm-35-6|Theorem §35.6]]),
>
> $$
> m h \le \int_x^{x+h} f(t)\,dt \le M h, \qquad\text{that is,}\qquad f(u) h \le \int_x^{x+h} f(t)\,dt \le f(v) h .
> $$
>
> Dividing by $h > 0$ and using (2):
>
> $$
> f(u) \le \frac{g(x + h) - g(x)}{h} \le f(v) . \qquad (3)
> $$
>
> **Case $h < 0$.** (Stewart leaves this as Exercise 87.) Now $x + h < x$. Let $u, v \in [x + h, x]$ be points where $f$ attains its minimum $m$ and maximum $M$ on $[x + h, x]$. By Definition §35.4 and (2),
>
> $$
> \frac{g(x + h) - g(x)}{h} = \frac1h \int_x^{x+h} f(t)\,dt = \frac{1}{-h} \int_{x+h}^{x} f(t)\,dt ,
> $$
>
> and Property 8 on the interval $[x + h, x]$ of length $-h > 0$ gives $f(u)(-h) \le \int_{x+h}^x f(t)\,dt \le f(v)(-h)$. Dividing by $-h > 0$ gives (3) again.
>
> **The limit.** In both cases $u$ and $v$ lie between $x$ and $x + h$, so $u \to x$ and $v \to x$ as $h \to 0$. Since $f$ is continuous at $x$,
>
> $$
> \lim_{h \to 0} f(u) = \lim_{u \to x} f(u) = f(x) \qquad\text{and}\qquad \lim_{h \to 0} f(v) = \lim_{v \to x} f(v) = f(x) .
> $$
>
> By (3) and the Squeeze Theorem,
>
> $$
> g'(x) = \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} = f(x) . \qquad (4)
> $$
>
> **Endpoints.** At $x = a$ (only $h > 0$) and at $x = b$ (only $h < 0$) the same argument gives (4) as a one-sided limit. A function with a derivative at a point is continuous there (Theorem 2.8.4, [[§13 The Derivative as a Function|§13]]); the one-sided version of that argument shows that $g$ is continuous from the right at $a$ and from the left at $b$. Together with differentiability on $(a, b)$, $g$ is continuous on $[a, b]$.

^pf-36-1

*Uses:* [[§35 The Definite Integral#^thm-35-5|§35.5]], [[§35 The Definite Integral#^thm-35-6|§35.6]], [[§35 The Definite Integral#^def-35-4|Def. §35.4]], [[§25 Maximum and Minimum Values|§25]] (Extreme Value Theorem), [[§8 Calculating Limits Using the Limit Laws|§8]] (Squeeze Theorem), [[§13 The Derivative as a Function|§13]] (Theorem 2.8.4: differentiable implies continuous)

![[m233-36-1.svg]]
*The proof of FTC1. The blue region is $g(x)$, and the red strip is $g(x + h) - g(x) = \int_x^{x+h} f(t)\,dt$. It contains the rectangle of height $m = f(u)$ and lies inside the rectangle of height $M = f(v)$ over $[x, x + h]$, so the difference quotient lies between $f(u)$ and $f(v)$. As $h \to 0$ both $u$ and $v$ are squeezed to $x$.*

> [!remark]- Connections
> - Rigorous treatment: [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (called *FTC II* there), with the same estimate $\big|\frac1h \int_x^{x+h} (f(t) - f(x))\,dt\big| \le \varepsilon$ in place of the Extreme Value Theorem. It needs $f$ only integrable for the continuity of $g$, and continuous at the one point $x$ for $g'(x) = f(x)$. Hub: [[Fundamental Theorem of Calculus]].
> - Lebesgue version, with no continuity at all: $g' = f$ almost everywhere, [[§18 Differentiation Theory#^thm-18-26|551 Thm. §18.26]].

> [!example] Example §36.1: Differentiating Integrals with Variable Upper Limits
> **(a)** Find the derivative of $g(x) = \displaystyle\int_0^x \sqrt{1 + t^2}\,dt$.
>
> $f(t) = \sqrt{1 + t^2}$ is continuous, so FTC1 gives at once
>
> $$
> g'(x) = \sqrt{1 + x^2} .
> $$
>
> **(b)** Find $\displaystyle\frac{d}{dx} \int_1^{x^4} \sec t\,dt$.
>
> The upper limit is $x^4$, not $x$, so combine FTC1 with the Chain Rule ([[§17 The Chain Rule|§17]]). Let $u = x^4$. Then
>
> $$
> \frac{d}{dx} \int_1^{x^4} \sec t\,dt = \frac{d}{dx} \int_1^{u} \sec t\,dt
> = \frac{d}{du} \Big[ \int_1^{u} \sec t\,dt \Big] \frac{du}{dx} \quad \text{(Chain Rule)}
> = \sec u \,\frac{du}{dx} \quad \text{(FTC1)}
> = \sec(x^4) \cdot 4x^3 .
> $$
>
> (FTC1 applies as long as $\sec$ is continuous between $1$ and $u = x^4$, that is, for $x^4 < \pi/2$.)
>
> In general, if $f$ is continuous and $h$ differentiable, $\dfrac{d}{dx} \displaystyle\int_a^{h(x)} f(t)\,dt = f(h(x))\,h'(x)$.
>
> *Stewart: Examples 5.3.2 and 5.3.4*

^ex-36-1

> [!example] Example §36.2: The Fresnel Function
> Functions defined by an integral, $g(x) = \int_a^x f(t)\,dt$, are common in physics, chemistry and statistics. The **Fresnel function**
>
> $$
> S(x) = \int_0^x \sin(\pi t^2/2)\,dt ,
> $$
>
> named after Augustin Fresnel (1788–1827), first appeared in his theory of the diffraction of light waves; it is also used in the design of highways. Its integrand has no elementary antiderivative, but FTC1 differentiates $S$ at once:
>
> $$
> S'(x) = \sin(\pi x^2/2) .
> $$
>
> So all the methods of differential calculus apply to $S$. For instance, $S$ is increasing where $\sin(\pi x^2/2) > 0$, that is, for $0 < x < \sqrt2$ (where $0 < \pi x^2/2 < \pi$), and decreasing for $\sqrt2 < x < 2$. So $S$ has a local maximum at $x = \sqrt2 \approx 1.4$, which is where $S(x)$ stops being an area and becomes a difference of areas. Graphs of $S$, computed numerically, confirm the picture: $S$ oscillates with decreasing amplitude, approaching $\frac12$ as $x \to \infty$.
>
> *Stewart: Example 5.3.3*

^ex-36-2

## The Fundamental Theorem of Calculus, Part 2

> [!theorem] Theorem §36.2: The Fundamental Theorem of Calculus, Part 2
> If $f$ is continuous on $[a, b]$, then
>
> $$
> \int_a^b f(x)\,dx = F(b) - F(a) ,
> $$
>
> where $F$ is any antiderivative of $f$, that is, a function such that $F' = f$. (Abbreviated FTC2.)
>
> *Stewart: 5.3, Fundamental Theorem of Calculus, Part 2*

^thm-36-2

> [!proof]+ Proof
> Let $g(x) = \int_a^x f(t)\,dt$. By Part 1 ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]), $g'(x) = f(x)$, so $g$ is an antiderivative of $f$. If $F$ is any other antiderivative of $f$ on $[a, b]$, then $F' = g'$ on $(a, b)$, and two functions with the same derivative on an interval differ by a constant (Corollary 4.2.7, [[§26 The Mean Value Theorem|§26]]):
>
> $$
> F(x) = g(x) + C \qquad \text{for } a < x < b . \qquad (6)
> $$
>
> Both $F$ and $g$ are continuous on $[a, b]$ ($F$ is differentiable, hence continuous, and $g$ by Part 1). Letting $x \to a^+$ and $x \to b^-$ in (6) shows that it also holds for $x = a$ and $x = b$. So $F(x) = g(x) + C$ for all $x$ in $[a, b]$.
>
> Putting $x = a$ in the formula for $g$ gives $g(a) = \int_a^a f(t)\,dt = 0$ (Definition §35.4). So, using (6) with $x = b$ and $x = a$,
>
> $$
> F(b) - F(a) = [g(b) + C] - [g(a) + C] = g(b) - g(a) = g(b) = \int_a^b f(t)\,dt .
> $$

^pf-36-2

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]], [[§26 The Mean Value Theorem|§26]] (Corollary 4.2.7), [[§35 The Definite Integral#^def-35-4|Def. §35.4]], [[§13 The Derivative as a Function|§13]] (differentiable implies continuous)

> [!remark]- Connections
> - Rigorous treatment: [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]] (called *FTC I* there) assumes only that $F$ is differentiable with integrable derivative, and proves it directly from the Mean Value Theorem on each subinterval. Stewart's route through Part 1, which needs $f$ continuous, is [[§34 Fundamental Theorem of Calculus#^ex-34-1|451 Ex. §34.1]].
> - Lebesgue version: $F(x) - F(a) = \int_a^x F'$ exactly for absolutely continuous $F$, [[§18 Differentiation Theory#^thm-18-13|551 Thm. §18.13]].

> [!remark] Remark: Why Part 2 Is Plausible
> It is surprising that $\int_a^b f(x)\,dx$, defined through all the values of $f$ on $[a, b]$, depends only on the values of $F$ at two points. Physically it is natural. If $s(t)$ is the position of an object and $v(t) = s'(t)$ its velocity, then $s$ is an antiderivative of $v$, and for an object that always moves forward the area under the velocity curve is the distance traveled ([[§34 The Area and Distance Problems|§34]]):
>
> $$
> \int_a^b v(t)\,dt = s(b) - s(a) .
> $$
>
> That is exactly FTC2 in this context.

^rem-36-2

> [!definition] Definition §36.1: Evaluation Notation
> $$
> F(x) \Big]_a^b = F(b) - F(a) .
> $$
>
> With it FTC2 reads $\displaystyle\int_a^b f(x)\,dx = F(x) \Big]_a^b$ where $F' = f$. Other common notations are $F(x) \big|_a^b$ and $\big[F(x)\big]_a^b$.
>
> *Stewart: 5.3 (text)*

^def-36-1

FTC2 allows *any* antiderivative $F$ of $f$, so one uses the simplest: the constant $C$ of the most general antiderivative ([[§33 Antiderivatives|§33]]) cancels in $F(b) - F(a)$.

> [!example] Example §36.3: Integrals in One Line
> **(a)** Evaluate $\displaystyle\int_1^3 e^x\,dx$. The function $e^x$ is continuous everywhere and $F(x) = e^x$ is an antiderivative (rather than $e^x + 7$ or $e^x + C$), so
>
> $$
> \int_1^3 e^x\,dx = F(3) - F(1) = e^3 - e .
> $$
>
> In [[§35 The Definite Integral|§35]] (Stewart, Example 5.2.4) the same value needed a limit of a geometric sum and a computer algebra system.
>
> **(b)** Find the area under the parabola $y = x^2$ from $0$ to $1$. An antiderivative of $x^2$ is $\frac13 x^3$, so
>
> $$
> A = \int_0^1 x^2\,dx = \frac{x^3}{3} \Big]_0^1 = \frac{1^3}{3} - \frac{0^3}{3} = \frac13 ,
> $$
>
> much shorter than the limit of sums in [[§34 The Area and Distance Problems#^ex-34-2|Example §34.2]]. Likewise the integral of [[§35 The Definite Integral#^ex-35-1|Example §35.1]] is $\big[\frac14 x^4 - 3x^2\big]_0^3 = \frac{81}{4} - 27 = -\frac{27}{4}$.
>
> *Stewart: Examples 5.3.5 and 5.3.6*

^ex-36-3

> [!example] Example §36.4: A Logarithm and the Area Under a Cosine
> **(a)** Evaluate $\displaystyle\int_3^6 \frac{dx}{x}$.
>
> This is another way of writing $\int_3^6 \frac1x\,dx$. An antiderivative of $1/x$ is $\ln|x|$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions|§19]]), and on $3 \le x \le 6$ we may write $\ln x$:
>
> $$
> \int_3^6 \frac1x\,dx = \ln x \Big]_3^6 = \ln 6 - \ln 3 = \ln \frac63 = \ln 2 .
> $$
>
> **(b)** Find the area under the cosine curve from $0$ to $b$, where $0 \le b \le \pi/2$.
>
> $\cos x \ge 0$ on $[0, \pi/2]$ and an antiderivative is $\sin x$, so
>
> $$
> A = \int_0^b \cos x\,dx = \sin x \Big]_0^b = \sin b - \sin 0 = \sin b .
> $$
>
> In particular, for $b = \pi/2$ the area under the cosine curve from $0$ to $\pi/2$ is $\sin(\pi/2) = 1$. When Roberval first found the areas under the sine and cosine curves in 1635, it took great ingenuity and no limits were available; with the Fundamental Theorem it is one line.
>
> *Stewart: Examples 5.3.7 and 5.3.8*

^ex-36-4

> [!example] Example §36.5: When FTC2 Does Not Apply
> What is wrong with the following calculation?
>
> $$
> \int_{-1}^{3} \frac{1}{x^2}\,dx = \frac{x^{-1}}{-1} \Big]_{-1}^{3} = -\frac13 - 1 = -\frac43 \qquad \text{(wrong)}
> $$
>
> The answer must be wrong: $f(x) = 1/x^2 \ge 0$, so by Property 6 of integrals ([[§35 The Definite Integral#^thm-35-6|Theorem §35.6]]) the integral, if it exists, is $\ge 0$. The error is that FTC2 applies to *continuous* functions, and $1/x^2$ is not continuous on $[-1, 3]$: it has an infinite discontinuity at $x = 0$. In fact $\int_{-1}^{3} \frac{1}{x^2}\,dx$ does not exist ([[§51 Improper Integrals|§51]]). (It is not even defined by Definition §35.1: $1/x^2$ is unbounded near $0$, so the Riemann sums with a sample point close to $0$ can be made arbitrarily large.)
>
> *Stewart: Example 5.3.9*

^ex-36-5

## Differentiation and Integration as Inverse Processes

> [!remark] Remark: The Two Parts Together
> Suppose $f$ is continuous on $[a, b]$. Then:
> 1. If $g(x) = \int_a^x f(t)\,dt$, then $g'(x) = f(x)$.
> 2. $\int_a^b f(x)\,dx = F(b) - F(a)$, where $F$ is any antiderivative of $f$, that is, $F' = f$.
>
> Part 1, $\dfrac{d}{dx} \displaystyle\int_a^x f(t)\,dt = f(x)$, says: integrate a continuous function, then differentiate, and you are back at $f$. Part 2 in the form
>
> $$
> \int_a^x F'(t)\,dt = F(x) - F(a)
> $$
>
> says: differentiate $F$, then integrate, and you are back at $F$, up to the constant $F(a)$. So integration and differentiation are inverse processes. Before the Fundamental Theorem, from Eudoxus and Archimedes to Galileo and Fermat, areas, volumes and lengths of curves were found one at a time by ingenious special arguments. Newton and Leibniz turned it into a systematic method.

^rem-36-3
