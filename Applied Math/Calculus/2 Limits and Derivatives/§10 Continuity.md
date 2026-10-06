---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 10
stewart: "2.5"
aliases: ["Stewart 2.5"]
tags: [calculus]
---
← [[§9 The Precise Definition of a Limit]] · ↑ [[· 2 Limits and Derivatives]] · [[§11 Limits at Infinity; Horizontal Asymptotes]] →

*Stewart, Section 2.5 · MATH 233 (UMass, Spring 2023): Practice Final Set 1 (Part I, Q4).*

A function is continuous at $a$ when its limit at $a$ can be found by plugging in $a$. This section names the ways that can fail (removable, infinite and jump discontinuities) and shows that sums, products, quotients, inverses and composites of continuous functions are continuous. With these rules every familiar function is continuous on its domain, so most limits are computed by direct substitution. The section ends with the Intermediate Value Theorem, the first theorem about what a continuous function does on a whole interval: it cannot skip a value, which is how one proves that an equation has a root.

## Continuity of a Function

> [!definition] Definition §10.1: Continuous at a Number
> A function $f$ is **continuous at a number $a$** if
>
> $$
> \lim_{x \to a} f(x) = f(a).
> $$
>
> This asks for three things:
> 1. $f(a)$ is defined (that is, $a$ is in the domain of $f$);
> 2. $\lim_{x \to a} f(x)$ exists;
> 3. $\lim_{x \to a} f(x) = f(a)$.
>
> *Stewart: 2.5, Definition 1*

^def-10-1

> [!remark] Remark: What the Definition Says
> $f(x)$ approaches $f(a)$ as $x$ approaches $a$. On the graph, the points $(x, f(x))$ run into the point $(a, f(a))$, so the curve has no gap there. In other words, a small change in $x$ produces only a small change in $f(x)$, and the change in $f(x)$ can be kept as small as we please by keeping the change in $x$ small enough. With the precise definition of a limit ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]) this becomes: for every $\varepsilon > 0$ there is a $\delta > 0$ such that
>
> $$
> |x - a| < \delta \quad\Longrightarrow\quad |f(x) - f(a)| < \varepsilon .
> $$
>
> The limit definition excludes $x = a$, but here there is no need to, since $|f(a) - f(a)| = 0$. A function that is continuous at every number of an interval has a graph that can be drawn without lifting the pen from the paper.

^rem-10-1

> [!remark]- Connections
> - Rigorous treatment: [[§20 Limits of Functions#^thm-20-1|451 Thm. §20.1]] shows that this agrees with the sequential definition [[§17 Continuous Functions#^def-17-1|451 Def. §17.1]], and [[§17 Continuous Functions#^thm-17-1|451 Thm. §17.1]] proves the ε–δ form above. There continuity is defined at every point of an arbitrary domain, using only nearby points of the domain, so Stewart's one-sided convention at the endpoints of an interval (Definition §10.5) is automatic.
> - One-sided limits, and the two-sided limit exists exactly when both one-sided limits exist and agree: [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]], [[§20 Limits of Functions#^thm-20-2|451 Thm. §20.2]]; so $f$ is continuous at $a$ if and only if it is continuous from the right and from the left (Definition §10.4). Kinds of discontinuity: a removable one filled in by its limit, [[§20 Limits of Functions#^ex-20-4|451 Ex. §20.4]]; a jump that no value can remove, [[§20 Limits of Functions#^ex-20-5|451 Ex. §20.5]]; and $\sin(1/x)$ at $0$, which is none of Stewart's three kinds ([[§20 Limits of Functions#^rem-20-3|451 Remark: Worse than a jump]]).

> [!definition] Definition §10.2: Discontinuity
> Suppose $f$ is defined near $a$, that is, on an open interval containing $a$, except perhaps at $a$ itself. Then $f$ is **discontinuous at $a$** (or $f$ has a **discontinuity at $a$**) if $f$ is not continuous at $a$.
>
> *Stewart: 2.5 (text)*

^def-10-2

> [!example] Example §10.1: Four Discontinuities
> Where are the following functions discontinuous?
>
> $$
> \text{(a)}\ f(x) = \frac{x^2 - x - 2}{x - 2} \qquad\qquad
> \text{(b)}\ f(x) = \begin{cases} \dfrac{x^2 - x - 2}{x - 2} & \text{if } x \ne 2 \\[4pt] 1 & \text{if } x = 2 \end{cases}
> $$
>
> $$
> \text{(c)}\ f(x) = \begin{cases} \dfrac{1}{x^2} & \text{if } x \ne 0 \\[4pt] 1 & \text{if } x = 0 \end{cases} \qquad\qquad
> \text{(d)}\ f(x) = \lfloor x \rfloor
> $$
>
> **(a)** $f(2)$ is not defined, so condition 1 of Definition §10.1 fails: $f$ is discontinuous at $2$. (It is continuous at every other number, by [[§10 Continuity#^thm-10-2|Theorem §10.2]].)
>
> **(b)** Now $f(2) = 1$ is defined, and the limit exists:
>
> $$
> \lim_{x \to 2} f(x) = \lim_{x \to 2} \frac{(x - 2)(x + 1)}{x - 2} = \lim_{x \to 2} (x + 1) = 3 .
> $$
>
> But $\lim_{x \to 2} f(x) = 3 \ne 1 = f(2)$, so condition 3 fails: $f$ is discontinuous at $2$.
>
> **(c)** $f(0) = 1$ is defined, but $\lim_{x \to 0} 1/x^2$ does not exist (the values grow without bound; [[§7 The Limit of a Function#^def-7-3|Definition §7.3]]). Condition 2 fails: $f$ is discontinuous at $0$.
>
> **(d)** The greatest integer function ($\lfloor x \rfloor$ is the largest integer $\le x$, [[§8 Calculating Limits Using the Limit Laws#^def-8-1|Definition §8.1]]; Stewart writes $[\![x]\!]$) is discontinuous at every integer $n$. For $n - 1 \le x < n$ we have $\lfloor x \rfloor = n - 1$, and for $n \le x < n + 1$ we have $\lfloor x \rfloor = n$. So
>
> $$
> \lim_{x \to n^-} \lfloor x \rfloor = n - 1 \ne n = \lim_{x \to n^+} \lfloor x \rfloor ,
> $$
>
> and $\lim_{x \to n} \lfloor x \rfloor$ does not exist ([[§8 Calculating Limits Using the Limit Laws#^thm-8-5|Theorem §8.5]]). At a non-integer $a$, $\lfloor x \rfloor$ is constant on an open interval around $a$, so it is continuous there.
>
> *Stewart: Example 2.5.2*

^ex-10-1

> [!definition] Definition §10.3: Removable, Infinite and Jump Discontinuities
> Let $f$ be discontinuous at $a$ (Definition §10.2).
> - The discontinuity is **removable** if $\lim_{x \to a} f(x)$ exists. Then redefining $f$ at the single number $a$ as $f(a) = \lim_{x \to a} f(x)$ makes $f$ continuous at $a$.
> - It is an **infinite discontinuity** if $f(x) \to \infty$ or $f(x) \to -\infty$ as $x \to a$ from at least one side.
> - It is a **jump discontinuity** if both one-sided limits $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ exist but are different: the function "jumps" from one value to another.
>
> In Example §10.1, (a) and (b) are removable (redefining $f(2) = 3$ turns $f$ into $g(x) = x + 1$, which is continuous), (c) is infinite, and (d) has a jump at every integer. Stewart introduces the three names through these examples.
>
> *Stewart: 2.5 (text)*

^def-10-3

![[m233-10-1.svg]]
*The discontinuities of Example §10.1. (a) Example §10.1(b): the limit $3$ exists but $f(2) = 1$ (red) is the wrong value; moving the one point up to the hole removes the discontinuity. (b) Example §10.1(c): no value $f(0)$ can help, since $f(x) \to \infty$. (c) $\lfloor x \rfloor$: at each integer the two one-sided limits differ by $1$. The filled dots are on the graph, so the function is continuous from the right there (Definition §10.4).*

> [!definition] Definition §10.4: Continuous from the Right and from the Left
> A function $f$ is **continuous from the right at a number $a$** if
>
> $$
> \lim_{x \to a^+} f(x) = f(a),
> $$
>
> and $f$ is **continuous from the left at $a$** if
>
> $$
> \lim_{x \to a^-} f(x) = f(a).
> $$
>
> For example, at each integer $n$ the greatest integer function is continuous from the right but not from the left, since by Example §10.1(d)
>
> $$
> \lim_{x \to n^+} \lfloor x \rfloor = n = \lfloor n \rfloor, \qquad \lim_{x \to n^-} \lfloor x \rfloor = n - 1 \ne \lfloor n \rfloor.
> $$
>
> *Stewart: 2.5, Definition 2; Example 2.5.3*

^def-10-4

> [!definition] Definition §10.5: Continuous on an Interval
> A function $f$ is **continuous on an interval** if it is continuous at every number in the interval. At an endpoint of the interval where $f$ is defined only on one side, *continuous* means continuous from the right (at a left endpoint) or continuous from the left (at a right endpoint).
>
> *Stewart: 2.5, Definition 3*

^def-10-5

## Properties of Continuous Functions

Instead of checking Definitions §10.1–§10.5 directly, one builds complicated continuous functions from simple ones.

> [!theorem] Theorem §10.1: Combining Continuous Functions
> If $f$ and $g$ are continuous at $a$ and $c$ is a constant, then the following functions are also continuous at $a$:
>
> $$
> 1.\ f + g \qquad 2.\ f - g \qquad 3.\ cf \qquad 4.\ fg \qquad 5.\ \frac{f}{g}\ \ \text{if } g(a) \ne 0 .
> $$
>
> By Definition §10.5, the same holds on an interval: if $f$ and $g$ are continuous on an interval, so are $f + g$, $f - g$, $cf$, $fg$ and (if $g$ is never $0$ there) $f/g$.
>
> *Stewart: 2.5, Theorem 4*

^thm-10-1

> [!proof]+ Proof
> Each part follows from the corresponding Limit Law. Since $f$ and $g$ are continuous at $a$,
>
> $$
> \lim_{x \to a} f(x) = f(a) \qquad\text{and}\qquad \lim_{x \to a} g(x) = g(a) .
> $$
>
> In particular both limits exist, so the Limit Laws apply:
>
> $$
> \begin{aligned}
> \lim_{x \to a} (f + g)(x) &= \lim_{x \to a} f(x) + \lim_{x \to a} g(x) = f(a) + g(a) = (f + g)(a) && \text{(Law 1)}, \\
> \lim_{x \to a} (f - g)(x) &= \lim_{x \to a} f(x) - \lim_{x \to a} g(x) = f(a) - g(a) = (f - g)(a) && \text{(Law 2)}, \\
> \lim_{x \to a} (cf)(x) &= c \lim_{x \to a} f(x) = c f(a) = (cf)(a) && \text{(Law 3)}, \\
> \lim_{x \to a} (fg)(x) &= \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x) = f(a) g(a) = (fg)(a) && \text{(Law 4)}, \\
> \lim_{x \to a} \Big(\frac{f}{g}\Big)(x) &= \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)} = \frac{f(a)}{g(a)} = \Big(\frac{f}{g}\Big)(a) && \text{(Law 5)}.
> \end{aligned}
> $$
>
> Law 5 applies because $\lim_{x \to a} g(x) = g(a) \ne 0$. Each line says that the combination is continuous at $a$. (Stewart writes out part 1 and leaves the others as Exercise 68.)

^pf-10-1

*Uses:* [[§10 Continuity#^def-10-1|Def. §10.1]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Limit Laws 1–5)

> [!theorem] Theorem §10.2: Polynomials and Rational Functions Are Continuous
> (a) Every polynomial is continuous everywhere, that is, on $\mathbb{R} = (-\infty, \infty)$.
>
> (b) Every rational function is continuous wherever it is defined, that is, on its domain.
>
> This is the Direct Substitution Property, [[§8 Calculating Limits Using the Limit Laws#^thm-8-3|Theorem §8.3]]: $\lim_{x \to a} f(x) = f(a)$ for $f$ polynomial or rational and $a$ in the domain of $f$.
>
> *Stewart: 2.5, Theorem 5*

^thm-10-2

> [!proof]+ Proof
> (a) A polynomial has the form $P(x) = c_n x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ with constants $c_0, \ldots, c_n$. For every $a$,
>
> $$
> \lim_{x \to a} c_0 = c_0 \quad \text{(Law 8)}, \qquad \lim_{x \to a} x^m = a^m, \quad m = 1, 2, \ldots, n \quad \text{(Law 10)} .
> $$
>
> The first says that constant functions are continuous, and the second says that $x \mapsto x^m$ is continuous. By part 3 of Theorem §10.1, each $x \mapsto c_m x^m$ is continuous. $P$ is the sum of these $n$ functions and a constant function, so $P$ is continuous by part 1 of Theorem §10.1, applied $n$ times.
>
> (b) A rational function has the form $f(x) = P(x)/Q(x)$ with $P$ and $Q$ polynomials, and its domain is $D = \{x \in \mathbb{R} \mid Q(x) \ne 0\}$. By (a), $P$ and $Q$ are continuous everywhere, so by part 5 of Theorem §10.1, $f$ is continuous at every number in $D$.

^pf-10-2

*Uses:* [[§10 Continuity#^thm-10-1|§10.1]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|§8.2]] (Limit Laws 8 and 10)

For instance, the volume $V(r) = \frac43 \pi r^3$ of a sphere is a continuous function of its radius, and the height $h = 50t - 16t^2$ (in ft) of a ball thrown upward at $50$ ft/s is a continuous function of time.

### The Trigonometric Functions

> [!theorem] Theorem §10.3: Limits of Sine and Cosine at 0
> $$
> \lim_{\theta \to 0} \cos\theta = 1, \qquad \lim_{\theta \to 0} \sin\theta = 0 .
> $$
>
> Since $\cos 0 = 1$ and $\sin 0 = 0$, this says that cosine and sine are continuous at $0$.
>
> *Stewart: 2.5, Equation 6*

^thm-10-3

> [!remark] Remark: Why It Works
> The point $P(\cos\theta, \sin\theta)$ lies on the unit circle at angle $\theta$ from the positive $x$-axis. As $\theta \to 0$, $P$ slides along the circle to the point $(1, 0)$, so its coordinates tend to $1$ and $0$. This is Stewart's argument. Stewart's margin suggests a second route, through the Squeeze Theorem, which the proof below carries out.

^rem-10-2

> [!proof]+ Proof
> **The inequality.** Let $0 < \theta < \pi/2$. On the unit circle, the arc from $(1, 0)$ to $P(\cos\theta, \sin\theta)$ has length $\theta$. The chord joining these two points is shorter than the arc, and the chord's vertical component is $\sin\theta$, so
>
> $$
> 0 < \sin\theta < \theta .
> $$
>
> (Stewart proves $\sin\theta < \theta$ this way in Section 3.3, in the [[§16 Derivatives of Trigonometric Functions#^pf-16-6|proof of Theorem §16.6]].) Since $\sin(-\theta) = -\sin\theta$, it follows that $|\sin\theta| \le |\theta|$ whenever $|\theta| < \pi/2$.
>
> **Sine.** For $|\theta| < \pi/2$ we have $-|\theta| \le \sin\theta \le |\theta|$. Both bounds tend to $0$ as $\theta \to 0$, so $\lim_{\theta \to 0} \sin\theta = 0$ by the Squeeze Theorem.
>
> **Cosine.** For $|\theta| < \pi/2$ we have $\cos\theta > 0$, so
>
> $$
> 0 \le 1 - \cos\theta = \frac{1 - \cos^2\theta}{1 + \cos\theta} = \frac{\sin^2\theta}{1 + \cos\theta} \le \sin^2\theta \le \theta^2 .
> $$
>
> Since $\theta^2 \to 0$, the Squeeze Theorem gives $1 - \cos\theta \to 0$, that is, $\lim_{\theta \to 0} \cos\theta = 1$.

^pf-10-3

*Uses:* [[§8 Calculating Limits Using the Limit Laws#^thm-8-7|§8.7]] (Squeeze Theorem)

> [!theorem] Theorem §10.4: Continuity of the Trigonometric Functions
> Sine and cosine are continuous on $\mathbb{R}$. Consequently $\tan x = \dfrac{\sin x}{\cos x}$ is continuous except where $\cos x = 0$, that is, except at the odd multiples of $\pi/2$. At $x = \pm\pi/2, \pm 3\pi/2, \pm 5\pi/2, \ldots$ it has infinite discontinuities. Likewise $\sec$, $\csc$ and $\cot$ are continuous on their domains.
>
> *Stewart: 2.5 (text; Exercises 65–67)*

^thm-10-4

> [!proof]+ Proof
> **A reformulation.** $f$ is continuous at $a$ if and only if $\lim_{h \to 0} f(a + h) = f(a)$. This is the substitution $x = a + h$: $x \to a$ exactly when $h \to 0$, and with $\delta$ the same in both limit statements (Stewart, Exercise 65).
>
> **Sine.** Let $a \in \mathbb{R}$. By the addition formula ([[§119 Trigonometry#^thm-119-6|Theorem §119.6]]),
>
> $$
> \sin(a + h) = \sin a \cos h + \cos a \sin h .
> $$
>
> Here $\sin a$ and $\cos a$ are constants, and by Theorem §10.3, $\cos h \to 1$ and $\sin h \to 0$ as $h \to 0$. By Limit Laws 1 and 3, $\sin(a + h) \to \sin a \cdot 1 + \cos a \cdot 0 = \sin a$. So sine is continuous at $a$.
>
> **Cosine.** In the same way, $\cos(a + h) = \cos a \cos h - \sin a \sin h \to \cos a \cdot 1 - \sin a \cdot 0 = \cos a$.
>
> **The other four.** $\tan = \sin/\cos$, $\cot = \cos/\sin$, $\sec = 1/\cos$ and $\csc = 1/\sin$ are quotients of continuous functions, so by part 5 of Theorem §10.1 they are continuous wherever the denominator is not $0$, which is exactly their domain.
>
> **Infinite discontinuities of tan.** As $x \to (\pi/2)^-$, $\sin x \to 1$, while $\cos x \to 0$ through positive values, so $\tan x \to \infty$. As $x \to (\pi/2)^+$, $\cos x \to 0$ through negative values, so $\tan x \to -\infty$. By periodicity the same happens at every odd multiple of $\pi/2$.

^pf-10-4

*Uses:* [[§10 Continuity#^thm-10-3|§10.3]], [[§10 Continuity#^thm-10-1|§10.1]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Limit Laws 1 and 3), [[§119 Trigonometry#^thm-119-6|§119.6]] (addition formulas)

### Inverse Functions

> [!theorem] Theorem §10.5: Continuity of Inverse Functions
> If $f$ is a one-to-one continuous function defined on an interval $(a, b)$, then its inverse function $f^{-1}$ is also continuous.
>
> *Stewart: 2.5 (text); proof in Appendix F*

^thm-10-5

> [!remark] Remark: Why It Works
> The graph of $f^{-1}$ is the reflection of the graph of $f$ in the line $y = x$. If the graph of $f$ has no break, neither does its mirror image.

^rem-10-3

> [!proof]- Proof
> **Step 1: $f$ is increasing or decreasing.** First, for any $x_1 < x_2 < x_3$ in $(a, b)$, the value $f(x_2)$ lies strictly between $f(x_1)$ and $f(x_3)$. Suppose not. The three values are distinct because $f$ is one-to-one, so $f(x_2)$ is the largest or the smallest of them. Then one of the two other values lies between the remaining two, and there are two cases.
> 1. $f(x_3)$ lies between $f(x_1)$ and $f(x_2)$. The Intermediate Value Theorem ([[§10 Continuity#^thm-10-10|Theorem §10.10]]) applied to $f$ on $[x_1, x_2]$ gives $c \in (x_1, x_2)$ with $f(c) = f(x_3)$. Since $c < x_2 < x_3$, $c \ne x_3$.
> 2. $f(x_1)$ lies between $f(x_2)$ and $f(x_3)$. The Intermediate Value Theorem on $[x_2, x_3]$ gives $c \in (x_2, x_3)$ with $f(c) = f(x_1)$, and $c \ne x_1$.
>
> Either way $f$ is not one-to-one, a contradiction.
>
> Now suppose $f$ is neither increasing nor decreasing. Then there are $p < q$ with $f(p) > f(q)$ and $r < s$ with $f(r) < f(s)$. List the distinct numbers among $p, q, r, s$ in increasing order as $z_1 < z_2 < \cdots < z_k$ ($k \le 4$). For each $i$, $f(z_{i+1})$ lies strictly between $f(z_i)$ and $f(z_{i+2})$, which means that the differences $f(z_{i+1}) - f(z_i)$ and $f(z_{i+2}) - f(z_{i+1})$ have the same sign. So all the consecutive differences have the same sign, and $f$ is increasing on $\{z_1, \ldots, z_k\}$ or decreasing there. The first contradicts $f(p) > f(q)$ and the second contradicts $f(r) < f(s)$. Hence $f$ is increasing or decreasing on $(a, b)$. (Stewart asserts this last step; the argument with $z_1, \ldots, z_k$ fills it in.)
>
> **Step 2: continuity of $f^{-1}$.** Say $f$ is increasing; the decreasing case is the same with the inequalities reversed. Let $y_0$ be in the domain of $f^{-1}$, and let $x_0 = f^{-1}(y_0)$, the number in $(a, b)$ with $f(x_0) = y_0$. Let $\varepsilon > 0$. Making $\varepsilon$ smaller only makes the goal harder, so we may assume $(x_0 - \varepsilon, x_0 + \varepsilon) \subseteq (a, b)$. Since $f$ is increasing, $f(x_0 - \varepsilon) < y_0 < f(x_0 + \varepsilon)$. Let
>
> $$
> \delta_1 = y_0 - f(x_0 - \varepsilon) > 0, \qquad \delta_2 = f(x_0 + \varepsilon) - y_0 > 0, \qquad \delta = \min\{\delta_1, \delta_2\} .
> $$
>
> Let $y$ be in the domain of $f^{-1}$ with $|y - y_0| < \delta$. Then $f(x_0 - \varepsilon) < y < f(x_0 + \varepsilon)$. Put $x = f^{-1}(y)$. If $x \le x_0 - \varepsilon$, then $y = f(x) \le f(x_0 - \varepsilon)$ because $f$ is increasing, which is false. If $x \ge x_0 + \varepsilon$, then $y \ge f(x_0 + \varepsilon)$, also false. So $x_0 - \varepsilon < x < x_0 + \varepsilon$, that is,
>
> $$
> |y - y_0| < \delta \quad\Longrightarrow\quad |f^{-1}(y) - f^{-1}(y_0)| < \varepsilon .
> $$
>
> Thus $\lim_{y \to y_0} f^{-1}(y) = f^{-1}(y_0)$, and $f^{-1}$ is continuous at every number $y_0$ of its domain. In words: $f$ maps $(x_0 - \varepsilon, x_0 + \varepsilon)$ into $\big(f(x_0 - \varepsilon), f(x_0 + \varepsilon)\big)$, and $f^{-1}$ maps back the part of that interval which lies in the range of $f$; the interval of half-width $\delta$ about $y_0$ fits inside it.

^pf-10-5

*Uses:* [[§10 Continuity#^thm-10-10|§10.10]], [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]] (precise definition of a limit)

> [!theorem] Theorem §10.6: The Familiar Functions Are Continuous
> The following types of functions are continuous at every number in their domains:
> - polynomials, rational functions and root functions;
> - trigonometric and inverse trigonometric functions;
> - exponential and logarithmic functions.
>
> *Stewart: 2.5, Theorem 7*

^thm-10-6

> [!proof]+ Proof
> **Polynomials and rational functions:** Theorem §10.2.
>
> **Root functions.** Stewart cites Limit Law 11, $\lim_{x \to a} \sqrt[n]{x} = \sqrt[n]{a}$. In Section 2.3 that law is derived from Law 7, whose proof comes only in this section ([[§10 Continuity#^cor-10-8|Corollary §10.8]]) and itself uses the continuity of roots. To avoid the circle, argue directly. If $n$ is odd, $x \mapsto x^n$ is continuous (Theorem §10.2) and one-to-one on $(-\infty, \infty)$, so its inverse $\sqrt[n]{x}$ is continuous on $\mathbb{R}$ by Theorem §10.5. If $n$ is even, $x \mapsto x^n$ is continuous and one-to-one on $(0, \infty)$, so $\sqrt[n]{x}$ is continuous on $(0, \infty)$. At $0$: if $0 \le x < \varepsilon^n$ then $0 \le \sqrt[n]{x} < \varepsilon$, so $\sqrt[n]{x}$ is continuous from the right at $0$.
>
> **Trigonometric functions:** Theorem §10.4.
>
> **Inverse trigonometric functions.** Sine is continuous and one-to-one on $(-\pi/2, \pi/2)$, so $\sin^{-1}$ is continuous on $(-1, 1)$ by Theorem §10.5. At $\pm 1$, Step 2 of that proof run on one side only shows that $\sin^{-1}$ is continuous from the left at $1$ and from the right at $-1$. In the same way $\cos^{-1}$ (from cosine on $[0, \pi]$) is continuous on $[-1, 1]$. Since $\tan$ is continuous and one-to-one on $(-\pi/2, \pi/2)$ with range $\mathbb{R}$, $\tan^{-1}$ is continuous on $\mathbb{R}$.
>
> **Exponential functions.** In Section 1.4 ([[§4 Exponential Functions#^def-4-3|Definition §4.3]]), $b^x$ for irrational $x$ is defined so as to fill in the holes in the graph of $b^x$, $x$ rational. In other words, the very definition of $b^x$ makes it continuous on $\mathbb{R}$. (This is Stewart's argument; a rigorous proof, with $e^x$ the inverse of the integral logarithm, is [[§121 The Logarithm Defined as an Integral#^thm-121-5|Theorem §121.5]].)
>
> **Logarithmic functions.** For $b > 0$, $b \ne 1$, $\log_b x$ is the inverse of the one-to-one continuous function $b^x$ on $(-\infty, \infty)$ ([[§5 Inverse Functions and Logarithms#^def-5-3|Definition §5.3]]), so it is continuous on its domain $(0, \infty)$ by Theorem §10.5.

^pf-10-6

*Uses:* [[§10 Continuity#^thm-10-2|§10.2]], [[§10 Continuity#^thm-10-4|§10.4]], [[§10 Continuity#^thm-10-5|§10.5]], [[§4 Exponential Functions#^def-4-3|Def. §4.3]] (definition of the exponential), [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]] (inverse functions)

> [!example] Example §10.2: Continuity at the Endpoints of the Domain
> **(a)** Show that $f(x) = 1 - \sqrt{1 - x^2}$ is continuous on $[-1, 1]$.
>
> **Interior points.** Let $-1 < a < 1$, so $1 - a^2 > 0$. By the Limit Laws ([[§8 Calculating Limits Using the Limit Laws#^thm-8-1|Theorems §8.1]] and [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|§8.2]]),
>
> $$
> \begin{aligned}
> \lim_{x \to a} f(x) &= 1 - \lim_{x \to a} \sqrt{1 - x^2} && \text{(Laws 2 and 8)} \\
> &= 1 - \sqrt{\lim_{x \to a} (1 - x^2)} && \text{(Law 7)} \\
> &= 1 - \sqrt{1 - a^2} = f(a) && \text{(Laws 2, 8 and 10)}.
> \end{aligned}
> $$
>
> So $f$ is continuous at $a$ by Definition §10.1.
>
> **Endpoints.** Stewart says "similar calculations show" $\lim_{x \to -1^+} f(x) = 1 = f(-1)$ and $\lim_{x \to 1^-} f(x) = 1 = f(1)$. Law 7 needs a positive limit under an even root, and here $1 - x^2 \to 0$, so estimate directly instead. For $-1 < x \le 0$,
>
> $$
> 0 \le \sqrt{1 - x^2} = \sqrt{(1 - x)(1 + x)} \le \sqrt{2(1 + x)} ,
> $$
>
> and $\sqrt{2(1 + x)} < \varepsilon$ as soon as $0 < 1 + x < \varepsilon^2 / 2$. By the Squeeze Theorem, $\sqrt{1 - x^2} \to 0$ as $x \to -1^+$, so $f(x) \to 1 = f(-1)$ and $f$ is continuous from the right at $-1$. The same estimate with $x$ and $-x$ exchanged shows that $f$ is continuous from the left at $1$. By Definition §10.5, $f$ is continuous on $[-1, 1]$. (The graph is the lower half of the circle $x^2 + (y - 1)^2 = 1$: from $y = 1 - \sqrt{1 - x^2}$ we get $(y - 1)^2 = 1 - x^2$.)
>
> **(b)** Determine the set on which $f(t) = \dfrac{\sqrt{t} - 1}{\sqrt{t} + 1}$ is continuous. (Choices: (a) $t > 0$, (b) $t \ge 0$, (c) $t > 1$, (d) $t \ge 0$ and $t \ne 1$, (e) $t \ne 0$, (f) all real numbers.)
>
> **Domain.** $\sqrt{t}$ requires $t \ge 0$, and the denominator satisfies $\sqrt{t} + 1 \ge 1 > 0$, so it is never $0$. The domain is $[0, \infty)$.
>
> **Interior.** For $t > 0$, the root function $\sqrt{t}$ is continuous at $t$ (Theorem §10.6), so the numerator and denominator are continuous and $f$ is continuous at $t$ by part 5 of Theorem §10.1.
>
> **The endpoint $0$.** $\sqrt{t}$ is continuous from the right at $0$, so by the one-sided Limit Laws
>
> $$
> \lim_{t \to 0^+} f(t) = \frac{0 - 1}{0 + 1} = -1 = f(0) .
> $$
>
> So $f$ is continuous from the right at $0$, and by Definition §10.5 it is continuous on $[0, \infty)$. **Answer: (b).**
>
> Choice (a) is the trap. There is no left-hand limit at $0$, but there is nothing to the left of $0$ in the domain. Definition §10.5 asks only for continuity from the right at a left endpoint, and Definition §10.2 speaks of a discontinuity only where $f$ is defined on both sides. Choice (d) is another trap: $f(1) = 0$ is harmless, because only a zero of the denominator matters.
>
> *Stewart: Example 2.5.4*
> *Source: 233 Practice Final Set 1, Part I Q4*

^ex-10-2

> [!theorem] Theorem §10.7: Limit of a Composite Function
> If $f$ is continuous at $b$ and $\lim_{x \to a} g(x) = b$, then $\lim_{x \to a} f(g(x)) = f(b)$. In other words,
>
> $$
> \lim_{x \to a} f(g(x)) = f\Big(\lim_{x \to a} g(x)\Big) .
> $$
>
> A limit symbol can be moved through a function symbol if the function is continuous and the limit exists.
>
> *Stewart: 2.5, Theorem 8; proof in Appendix F*

^thm-10-7

> [!proof]+ Proof
> Intuitively: if $x$ is close to $a$, then $g(x)$ is close to $b$, and since $f$ is continuous at $b$, $f(g(x))$ is then close to $f(b)$. Precisely: let $\varepsilon > 0$. We want $\delta > 0$ such that
>
> $$
> 0 < |x - a| < \delta \quad\Longrightarrow\quad |f(g(x)) - f(b)| < \varepsilon .
> $$
>
> Since $f$ is continuous at $b$, $\lim_{y \to b} f(y) = f(b)$, so there is $\delta_1 > 0$ such that
>
> $$
> |y - b| < \delta_1 \quad\Longrightarrow\quad |f(y) - f(b)| < \varepsilon .
> $$
>
> The limit definition only gives this for $0 < |y - b| < \delta_1$ (Stewart writes it that way), but for $y = b$ it holds trivially, since $|f(b) - f(b)| = 0 < \varepsilon$. The case $y = b$ is needed, because $g(x)$ may equal $b$. Since $\lim_{x \to a} g(x) = b$, there is $\delta > 0$ such that
>
> $$
> 0 < |x - a| < \delta \quad\Longrightarrow\quad |g(x) - b| < \delta_1 .
> $$
>
> Combining the two statements with $y = g(x)$: whenever $0 < |x - a| < \delta$, we have $|g(x) - b| < \delta_1$, hence $|f(g(x)) - f(b)| < \varepsilon$. Therefore $\lim_{x \to a} f(g(x)) = f(b)$.

^pf-10-7

*Uses:* [[§10 Continuity#^def-10-1|Def. §10.1]], [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]] (precise definition of a limit)

> [!example] Example §10.3: Limits by Continuity
> **(a)** Find $\displaystyle\lim_{x \to -2} \frac{x^3 + 2x^2 - 1}{5 - 3x}$.
>
> The function $f(x) = \dfrac{x^3 + 2x^2 - 1}{5 - 3x}$ is rational, so by Theorem §10.2 it is continuous on its domain $\{x \mid x \ne \frac53\}$, which contains $-2$. Therefore
>
> $$
> \lim_{x \to -2} f(x) = f(-2) = \frac{(-2)^3 + 2(-2)^2 - 1}{5 - 3(-2)} = \frac{-8 + 8 - 1}{11} = -\frac{1}{11} .
> $$
>
> **(b)** Find $\displaystyle\lim_{x \to \pi} \frac{\sin x}{2 + \cos x}$.
>
> By Theorem §10.6, $\sin x$ is continuous, and $2 + \cos x$ is a sum of two continuous functions, hence continuous. It is never $0$: $\cos x \ge -1$ for all $x$, so $2 + \cos x \ge 1 > 0$. By part 5 of Theorem §10.1, $f(x) = \dfrac{\sin x}{2 + \cos x}$ is continuous everywhere, and
>
> $$
> \lim_{x \to \pi} f(x) = f(\pi) = \frac{\sin\pi}{2 + \cos\pi} = \frac{0}{2 - 1} = 0 .
> $$
>
> **(c)** Evaluate $\displaystyle\lim_{x \to 1} \arcsin\Big(\frac{1 - \sqrt{x}}{1 - x}\Big)$.
>
> Here the inner function is not defined at $1$, so direct substitution fails; Theorem §10.7 is needed instead. Arcsin is continuous (Theorem §10.6), so we may move the limit inside, provided the inner limit exists. Factor $1 - x = (1 - \sqrt{x})(1 + \sqrt{x})$:
>
> $$
> \begin{aligned}
> \lim_{x \to 1} \arcsin\Big(\frac{1 - \sqrt{x}}{1 - x}\Big)
> &= \arcsin\Big(\lim_{x \to 1} \frac{1 - \sqrt{x}}{(1 - \sqrt{x})(1 + \sqrt{x})}\Big) \\
> &= \arcsin\Big(\lim_{x \to 1} \frac{1}{1 + \sqrt{x}}\Big) = \arcsin\frac12 = \frac{\pi}{6} .
> \end{aligned}
> $$
>
> The inner limit $\frac12$ lies in $(-1, 1)$, where arcsin is continuous, so the theorem applies.
>
> *Stewart: Examples 2.5.5, 2.5.7 and 2.5.8*

^ex-10-3

> [!theorem] Corollary §10.8: The Root Law
> If $n$ is a positive integer and $\lim_{x \to a} g(x)$ exists (and is positive when $n$ is even), then
>
> $$
> \lim_{x \to a} \sqrt[n]{g(x)} = \sqrt[n]{\lim_{x \to a} g(x)} .
> $$
>
> This is Limit Law 7 of [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|Theorem §8.2]], whose proof was postponed to this section.
>
> *Stewart: 2.3, Limit Law 7 (proved in 2.5)*

^cor-10-8

> [!proof]+ Proof
> Let $b = \lim_{x \to a} g(x)$ and $f(x) = \sqrt[n]{x}$. Then $f(g(x)) = \sqrt[n]{g(x)}$ and $f\big(\lim_{x \to a} g(x)\big) = \sqrt[n]{b}$. The root function $f$ is continuous at $b$ (Theorem §10.6; for even $n$, $b > 0$ lies inside the domain). So Theorem §10.7 gives the formula.
>
> Stewart cites Limit Law 11 for the continuity of $f$, but Law 11 was obtained from Law 7. The continuity of roots proved directly in Theorem §10.6 (as inverse functions) removes the circularity.

^pf-10-8

*Uses:* [[§10 Continuity#^thm-10-6|§10.6]], [[§10 Continuity#^thm-10-7|§10.7]]

> [!theorem] Theorem §10.9: Composites of Continuous Functions
> If $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then the composite function $f \circ g$, given by $(f \circ g)(x) = f(g(x))$, is continuous at $a$.
>
> Informally: a continuous function of a continuous function is a continuous function.
>
> *Stewart: 2.5, Theorem 9*

^thm-10-9

> [!proof]+ Proof
> Since $g$ is continuous at $a$, $\lim_{x \to a} g(x) = g(a)$. Since $f$ is continuous at $b = g(a)$, Theorem §10.7 gives
>
> $$
> \lim_{x \to a} f(g(x)) = f(g(a)) ,
> $$
>
> which is precisely the statement that $h(x) = f(g(x))$ is continuous at $a$.

^pf-10-9

*Uses:* [[§10 Continuity#^thm-10-7|§10.7]], [[§10 Continuity#^def-10-1|Def. §10.1]]

> [!remark]- Connections
> - Rigorous treatment of the combination rules: sums, products and quotients [[§17 Continuous Functions#^thm-17-3|451 Thm. §17.3]] (from the limit theorems for sequences), polynomials [[§17 Continuous Functions#^ex-17-6|451 Ex. §17.6]], composites [[§17 Continuous Functions#^thm-17-4|451 Thm. §17.4]] (one line with the sequential definition; several variables: [[§3 Continuity and Limits of Functions#^thm-3-4|452 Thm. §3.4]]).
> - Inverses and the familiar functions: [[§18 Properties of Continuous Functions#^thm-18-9|451 Thm. §18.9]] (a strictly increasing continuous function on a closed interval has a continuous inverse, proved with [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] instead of an explicit δ; topological form [[§15 Compact Spaces#^thm-15-7|590 Thm. §15.7]]). Once $\sin$, $\cos$ and $e^x$ are defined by power series, their continuity is [[§26 Differentiation and Integration of Power Series#^cor-26-2|451 Cor. §26.2]], and the logarithm is continuous as the inverse of $e^x$ ([[§18 Properties of Continuous Functions#^rem-18-8|451 Remark: Beyond closed intervals]]).

> [!example] Example §10.4: Where Is the Function Continuous?
> **(a)** $f(x) = \dfrac{\ln x + \tan^{-1} x}{x^2 - 1}$. By Theorem §10.6, $\ln x$ is continuous on $(0, \infty)$ and $\tan^{-1} x$ is continuous on $\mathbb{R}$, so by part 1 of Theorem §10.1 the numerator is continuous on $(0, \infty)$. The denominator $x^2 - 1$ is a polynomial, continuous everywhere. By part 5 of Theorem §10.1, $f$ is continuous at every $x > 0$ with $x^2 - 1 \ne 0$, that is, $x \ne \pm 1$. So $f$ is continuous on the intervals $(0, 1)$ and $(1, \infty)$.
>
> **(b)** $h(x) = \sin(x^2)$. Here $h = f \circ g$ with $g(x) = x^2$ and $f(x) = \sin x$. $g$ is a polynomial, continuous on $\mathbb{R}$, and $f$ is continuous everywhere (Theorem §10.6). By Theorem §10.9, $h$ is continuous on $\mathbb{R}$.
>
> **(c)** $F(x) = \ln(1 + \cos x)$. Here $F = f \circ g$ with $f(x) = \ln x$ and $g(x) = 1 + \cos x$. Both are continuous on their domains (Theorems §10.6 and §10.1), so by Theorem §10.9, $F$ is continuous wherever it is defined. $\ln(1 + \cos x)$ is defined when $1 + \cos x > 0$. Since $\cos x \ge -1$, this fails exactly when $\cos x = -1$, that is, at $x = \pm\pi, \pm 3\pi, \ldots$. So $F$ is continuous on the intervals between consecutive odd multiples of $\pi$ and has discontinuities at the odd multiples of $\pi$. (As $x \to \pi$, $1 + \cos x \to 0^+$ and $F(x) \to -\infty$: infinite discontinuities.)
>
> *Stewart: Examples 2.5.6 and 2.5.9*

^ex-10-4

> [!remark] Remark: Method — Showing a Function Is Continuous
> 1. Find the domain: exclude zeros of denominators, negative numbers under even roots, non-positive arguments of logarithms, and so on.
> 2. Write the function as sums, products, quotients and composites of the functions in [[§10 Continuity#^thm-10-6|Theorem §10.6]]. By [[§10 Continuity#^thm-10-1|Theorem §10.1]] and [[§10 Continuity#^thm-10-9|Theorem §10.9]], it is continuous at every number in its domain.
> 3. At an endpoint of the domain, check one-sided continuity ([[§10 Continuity#^def-10-5|Definition §10.5]]), as in [[§10 Continuity#^ex-10-2|Example §10.2]].
> 4. For a piecewise-defined function, step 2 settles the inside of each piece. At each break point $a$, compute both one-sided limits and compare them with $f(a)$ ([[§10 Continuity#^def-10-4|Definition §10.4]]). If the formula involves a constant, setting the two one-sided limits equal to $f(a)$ gives the equations for the constant.
> 5. To evaluate $\lim_{x \to a} f(x)$ for $f$ continuous at $a$, substitute: $\lim_{x \to a} f(x) = f(a)$.

^rem-10-4

## The Intermediate Value Theorem

> [!theorem] Theorem §10.10: The Intermediate Value Theorem
> Suppose that $f$ is continuous on the closed interval $[a, b]$, and let $N$ be any number between $f(a)$ and $f(b)$, where $f(a) \ne f(b)$. Then there exists a number $c$ in $(a, b)$ such that $f(c) = N$.
>
> *Stewart: 2.5, Theorem 10*

^thm-10-10

*Stewart does not prove the Intermediate Value Theorem ("its proof is found in more advanced books on calculus"). It depends on the completeness of the real numbers and is proved in [[§18 Properties of Continuous Functions#^thm-18-3|451 Thm. §18.3]].*

![[m233-10-2.svg]]
*A continuous $f$ on $[a, b]$ takes every value $N$ between $f(a)$ and $f(b)$ (the green range). The red line $y = N$ separates the endpoints $(a, f(a))$ and $(b, f(b))$ of the graph, so the graph must cross it. Here it does so three times, at $c_1, c_2, c_3$: the theorem guarantees at least one $c$, not a unique one.*

> [!remark]- Connections
> - Hub: [[Intermediate Value Theorem]]. Topological form: a continuous image of a connected space is connected, [[§13 Connected Spaces#^thm-13-3|590 Thm. §13.3]], which gives the theorem for maps into an ordered space, [[§14 Connected Subspaces of ℝ#^thm-14-3|590 Thm. §14.3]].
> - The sign-change form used in Example §10.5: [[§18 Properties of Continuous Functions#^cor-18-4|451 Cor. §18.4]]. Every polynomial of odd degree has a real root: [[§18 Properties of Continuous Functions#^prop-18-8|451 Prop. §18.8]].

> [!remark] Remark: Why It Works
> Think of a continuous function as one whose graph has no hole or break. Any horizontal line $y = N$ between $y = f(a)$ and $y = f(b)$ has the start of the graph on one side and the end on the other, so the graph cannot jump over the line: it must meet it somewhere. Continuity is essential. For example, $\lfloor x \rfloor$ on $[0, 1]$ has $\lfloor 0 \rfloor = 0$ and $\lfloor 1 \rfloor = 1$ but never takes the value $\frac12$. Graphing software relies on the theorem: it computes finitely many points and connects the dots, assuming that the function takes all the values in between.

^rem-10-5

> [!example] Example §10.5: Locating a Root
> Show that the equation $4x^3 - 6x^2 + 3x - 2 = 0$ has a solution between $1$ and $2$.
>
> Let $f(x) = 4x^3 - 6x^2 + 3x - 2$. We want $c \in (1, 2)$ with $f(c) = 0$, so take $a = 1$, $b = 2$, $N = 0$ in Theorem §10.10:
>
> $$
> f(1) = 4 - 6 + 3 - 2 = -1 < 0, \qquad f(2) = 32 - 24 + 6 - 2 = 12 > 0 .
> $$
>
> So $N = 0$ lies between $f(1)$ and $f(2)$. $f$ is a polynomial, hence continuous on $[1, 2]$ (Theorem §10.2). The Intermediate Value Theorem gives a number $c \in (1, 2)$ with $f(c) = 0$.
>
> **Narrowing down.** Apply the theorem again on smaller intervals:
>
> $$
> f(1.2) = 6.912 - 8.64 + 3.6 - 2 = -0.128 < 0, \qquad f(1.3) = 8.788 - 10.14 + 3.9 - 2 = 0.548 > 0 ,
> $$
>
> so a root lies in $(1.2, 1.3)$. Then
>
> $$
> f(1.22) = -0.007008 < 0, \qquad f(1.23) = 0.056068 > 0 ,
> $$
>
> so a root lies in $(1.22, 1.23)$.
>
> (It is the only real root: $f'(x) = 12x^2 - 12x + 3 = 3(2x - 1)^2$ is positive except at $x = \frac12$, so $f$ is increasing on each side of $\frac12$ by [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]], and in fact on all of $\mathbb{R}$: completing the cube, $f(x) = \frac12 (2x - 1)^3 - \frac32$, and $t \mapsto t^3$ is increasing. Solving $(2c - 1)^3 = 3$ also gives the root exactly, $c = \frac12\big(1 + \sqrt[3]{3}\big) \approx 1.2211$.)
>
> *Stewart: Example 2.5.10*

^ex-10-5
